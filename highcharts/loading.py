from typing import Optional

from validator_collection import validators

from highcharts import constants
from highcharts.metaclasses import HighchartsMeta


class Loading(HighchartsMeta):
    """The loading options control the appearance of the loading screen that covers
    the plot area on chart operations.

    This screen only appears after an explicit call to ``chart.showLoading()`` in the
    browser. It is a utility for developers to communicate to the end user that
    something is going on, for example while retrieving new data via an XHR
    connection.

    .. hint::

      The "Loading..." text itself is **not** part of this configuration object, but
      is instead part of the :meth:`.language <Options.language>` configuration.

    """

    def __init__(self, **kwargs):
        self._hide_duration = None
        self._label_style = None
        self._show_duration = None
        self._style = None

        self.hide_duration = kwargs.pop('hide_duration', None)
        self.label_style = kwargs.pop('label_style', None)
        self.show_duration = kwargs.pop('show_duration', None)
        self.style = kwargs.pop('style', None)

    @property
    def hide_duration(self) -> Optional[int]:
        f"""The duration in milliseconds of the fade out effect. Defaults to
        ``{constants.DEFAULT_LOADING.get('hide_duration')}``.

        :rtype: :class:`int <python:int>` or :obj:`None <python:None>`
        """
        return self._hide_duration

    @hide_duration.setter
    def hide_duration(self, value):
        self._hide_duration = validators.integer(value,
                                                 allow_empty = True,
                                                 minimum = 0)

    @property
    def label_style(self) -> Optional[str]:
        f"""CSS styles applied to the loading label's ``<span>``. Defaults to
        ``'{constants.DEFAULT_LOADING.get('label_style')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._label_style

    @label_style.setter
    def label_style(self, value):
        self._label_style = validators.string(value, allow_empty = True)

    @property
    def show_duration(self) -> Optional[int]:
        f"""The duration in milliseconds of the fade in effect. Defaults to
        ``{constants.DEFAULT_LOADING.get('show_duration')}``.

        :rtype: :class:`int <python:int>` or :obj:`None <python:None>`
        """
        return self._show_duration

    @show_duration.setter
    def show_duration(self, value):
        self._show_duration = validators.integer(value,
                                                 allow_empty = True,
                                                 minimum = 0)

    @property
    def style(self) -> Optional[str]:
        f"""CSS styles for the loading screen that covers the plot area. Defaults to
        ``'{constants.DEFAULT_LOADING.get('style')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._style

    @style.setter
    def style(self, value):
        self._style = validators.string(value, allow_empty = True)

    @classmethod
    def from_dict(cls, as_dict):
        kwargs = {
            'hide_duration': as_dict.pop('hideDuration', None),
            'label_style': as_dict.pop('labelStyle', None),
            'show_duration': as_dict.pop('showDuration', None),
            'style': as_dict.pop('style', None),
        }

        return cls(**kwargs)

    def _to_untrimmed_dict(self) -> dict:
        untrimmed = {
            'hideDuration': self.hide_duration,
            'labelStyle': self.label_style,
            'showDuration': self.show_duration,
            'style': self.style
        }

        return untrimmed
