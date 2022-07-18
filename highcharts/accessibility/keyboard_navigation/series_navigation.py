from validator_collection import validators

from highcharts import errors
from highcharts.metaclasses import HighchartsMeta


class SeriesNavigation(HighchartsMeta):
    """Options for the keyboard navigation of data points and series."""

    def __init__(self, **kwargs):
        self._mode = 'normal'
        self._point_navigation_enabled_threshold = False
        self._remember_point_focus = False
        self._skip_null_points = True

        self.mode = kwargs.pop('mode', 'normal')
        self.point_navigation_enabled_threshold = kwargs.pop('point_navigation_enabled_threshold',
                                                             False)
        self.remember_point_focus = kwargs.pop('remember_point_focus', False)
        self.skip_null_points = kwargs.pop('skip_null_points', True)

    @property
    def mode(self) -> str:
        """Sets the keyboard navigation mode for the chart. Defaults to ``'normal'``.

        Can be ``"normal"`` or ``"serialize"``.

        In ``'normal'`` mode, left/right arrow keys move between points in a series, while
        up/down arrow keys move between series. Up/down navigation acts intelligently to
        figure out which series makes sense to move to from any given point.

        In ``'serialize'`` mode, points are instead navigated as a single list.
        Left/right behaves as in ``"normal"`` mode. Up/down arrow keys will behave like
        left/right. This can be useful for unifying navigation behavior with/without screen
        readers enabled.

        :returns: The keyboard navigation mode to apply to the chart.
        :rtype: :class:`str <python:str>`
        """
        return self._mode

    @mode.setter
    def mode(self, value):
        value = validators.string(value, allow_empty = False).lower()
        if value not in ['normal', 'serialize']:
            raise errors.HighchartsValueError(f'Expects either "normal" or "serialize". '
                                              f'Received: {value}')

        self._mode = value

    @property
    def point_navigation_enabled_threshold(self) -> bool | int:
        """When a series contains more points than this, we no longer allow keyboard
        navigation for it. Accepts either an :class:`int <python:int>` or a
        a :class:`bool <python:bool>` value of ``False``.

        Setting to ``False`` will disable any threshold.

        :rtype: :class:`int <python:int>` or :class:`bool <python:bool>`
        """
        return self._point_navigation_enabled_threshold

    @point_navigation_enabled_threshold.setter
    def point_navigation_enabled_threshold(self, value):
        if isinstance(value, bool) and value is False:
            self._point_navigation_enabled_threshold = False
        else:
            value = validators.integer(value,
                                       allow_empty = False,
                                       coerce_value = True)
            self._point_navigation_enabled_threshold = value

    @property
    def remember_point_focus(self) -> bool:
        """If ``True``, remembers which point was focused even after navigating away from
        the series, so that when navigating back to the series you start at the last
        focused point.

        Defaults to ``False``.

        :returns: Flag indicating whether to remember point focus.
        :rtype: :class:`bool <python:bool>`
        """
        return self.point_focus

    @remember_point_focus.setter
    def remember_point_focus(self, value):
        self._remember_point_focus = bool(value)

    @property
    def skip_null_points(self) -> bool:
        """If ``True``, skip null points when navigating through points with the keyboard.
        Defaults to ``True``.

        :returns: Flag indicating whether to skip null points in keyboard navigation.
        :rtype: :class:`bool <python:bool>`
        """
        return self._skip_null_points

    @skip_null_points.setter
    def skip_null_points(self, value):
        self._skip_null_points = bool(value)

    @classmethod
    def from_dict(cls, as_dict):
        kwargs = {
            'mode': as_dict.pop('mode', 'normal'),
            'point_navigation_enabled_threshold': as_dict.pop('pointNavigationEnabledThreshold',
                                                              False),
            'remember_point_focus': as_dict.pop('rememberPointFocus', False),
            'skip_null_points': as_dict.pop('skipNullPoints', True)
        }
        return cls(**kwargs)

    def to_dict(self):
        untrimmed = {
            'mode': self.mode,
            'pointNavigationEnabledThreshold': self.point_navigation_enabled_threshold,
            'rememberPointFocus': self.remmeber_point_focus,
            'skipNullPoints': self.skip_null_points
        }
        return self.trim_dict(untrimmed)