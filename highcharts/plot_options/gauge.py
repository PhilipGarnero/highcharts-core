from typing import Optional, List, Any
from decimal import Decimal

from validator_collection import validators

from highcharts import errors
from highcharts.decorators import class_sensitive, validate_types
from highcharts.metaclasses import HighchartsMeta
from highcharts.plot_options.generic import GenericTypeOptions
from highcharts.plot_options.series import SeriesOptions
from highcharts.utility_classes.gradients import Gradient
from highcharts.utility_classes.patterns import Pattern
from highcharts.utility_classes.shadows import ShadowOptions


class DialOptions(HighchartsMeta):
    """Options for the dial or arrow pointer of the gauge."""

    def __init__(self, **kwargs):
        self._background_color = None
        self._base_length = None
        self._base_width = None
        self._border_color = None
        self._border_width = None
        self._path = None
        self._radius = None
        self._rear_length = None
        self._top_width = None

        self.background_color = kwargs.pop('background_color', None)
        self.base_length = kwargs.pop('base_length', None)
        self.base_width = kwargs.pop('base_width', None)
        self.border_color = kwargs.pop('border_color', None)
        self.border_width = kwargs.pop('border_width', None)
        self.path = kwargs.pop('path', None)
        self.radius = kwargs.pop('radius', None)
        self.rear_length = kwargs.pop('rear_length', None)
        self.top_width = kwargs.pop('top_width', None)

    @property
    def background_color(self) -> Optional[str | Gradient | Pattern]:
        """The background or fill color of the gauge's dial. Defaults to '#000000'.

        :rtype: :class:`str <python:str>`, :class:`Gradient`, :class:`Pattern``, or
          :obj:`None <python:None>`
        """
        return self._background_color

    @background_color.setter
    def background_color(self, value):
        if not value:
            self._background_color = None
        elif isinstance(value, (Gradient, Pattern)):
            self._background_color = value
        elif isinstance(value, (dict, str)) and 'linearGradient' in value:
            try:
                self._background_color = Gradient.from_json(value)
            except ValueError:
                if isinstance(value, dict):
                    self._background_color = Gradient.from_dict(value)
                else:
                    self._background_color = validators.string(value)
        elif isinstance(value, dict) and 'linear_gradient' in value:
            self._background_color = Gradient(**value)
        elif isinstance(value, (dict, str)) and 'patternOptions' in value:
            try:
                self._background_color = Pattern.from_json(value)
            except ValueError:
                if isinstance(value, dict):
                    self._background_color = Pattern.from_dict(value)
                else:
                    self._background_color = validators.string(value)
        elif isinstance(value, dict) and 'pattern_options' in value:
            self._background_color = Pattern(**value)
        else:
            raise errors.HighchartsValueError(f'Unable to resolve value to a string, '
                                              f'Gradient, or Pattern. Value received '
                                              f'was: {value}')

    @property
    def base_length(self) -> Optional[str]:
        """The length of the dial's base part, expressed as a percentage of the total
        radius or length of the dial. Defaults to ``70%``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._base_length

    @base_length.setter
    def base_length(self, value):
        if value is None:
            self._base_length = None
        else:
            value = validators.string(value)
            if '%' not in value:
                raise errors.HighchartsValueError(f'base_length expects a percentage '
                                                  f'string. Received: {value}')
            self._base_length = value

    @property
    def base_width(self) -> Optional[int | float | Decimal]:
        """The pixel width of the base of the gauge dial. Defaults to ``3``.

        .. note::

          The base is the part closest to the pivot, defined by
          :meth:`DialOptions.base_length`.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._base_width

    @base_width.setter
    def base_width(self, value):
        self._base_width = validators.numeric(value,
                                              allow_empty = True,
                                              minimum = 0)

    @property
    def border_color(self) -> Optional[str | Gradient | Pattern]:
        """The border color or stroke of the gauge's dial. Defaults to ``'#cccccc'``.

        .. warning::

          By default, the :meth:`DialOptions.border_width` is ``0``, so be sure to set
          that property to a non-default value if you wish to apply a border color.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._border_color

    @border_color.setter
    def border_color(self, value):
        if not value:
            self._border_color = None
        elif isinstance(value, (Gradient, Pattern)):
            self._border_color = value
        elif isinstance(value, (dict, str)) and 'linearGradient' in value:
            try:
                self._border_color = Gradient.from_json(value)
            except ValueError:
                if isinstance(value, dict):
                    self._border_color = Gradient.from_dict(value)
                else:
                    self._border_color = validators.string(value)
        elif isinstance(value, dict) and 'linear_gradient' in value:
            self._border_color = Gradient(**value)
        elif isinstance(value, (dict, str)) and 'patternOptions' in value:
            try:
                self._border_color = Pattern.from_json(value)
            except ValueError:
                if isinstance(value, dict):
                    self._border_color = Pattern.from_dict(value)
                else:
                    self._border_color = validators.string(value)
        elif isinstance(value, dict) and 'pattern_options' in value:
            self._border_color = Pattern(**value)
        else:
            raise errors.HighchartsValueError(f'Unable to resolve value to a string, '
                                              f'Gradient, or Pattern. Value received '
                                              f'was: {value}')

    @property
    def border_width(self) -> Optional[int | float | Decimal]:
        """The width of the gauge dial border in pixels. Defaults to ``0``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._border_width

    @border_width.setter
    def border_width(self, value):
        self._border_width = validators.numeric(value,
                                                allow_empty = True,
                                                minimum = 0)

    @property
    def path(self) -> Optional[List[Any]]:
        """An array with an SVG path for the custom dial. Defaults to
        :obj:`None <python:None>`.

        :rtype: :class:`list <python:list>` of any instances, or :obj:`None <python:None>`
        """
        return self._path

    @path.setter
    def path(self, value):
        if not value:
            self._path = None
        else:
            self._path = validators.iterable(value)

    @property
    def radius(self) -> Optional[str]:
        """The radius or length of the dial, in percentages relative to the radius of the
        gauge itself. Defaults to ``'80%'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._radius

    @radius.setter
    def radius(self, value):
        if not value:
            self._radius = None
        else:
            value = validators.string(value)
            if '%' not in value:
                raise errors.HighchartsValueError(f'radius expects a percentage string. '
                                                  f'Received: {value}')
            self._radius = value

    @property
    def rear_length(self) -> Optional[str]:
        """The length of the dial's rear end, the part that extends out on the other side
        of the pivot. Expressed as a percentage of the dial's length. Defaults to
        ``'10%'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._rear_length

    @rear_length.setter
    def rear_length(self, value):
        if not value:
            self._rear_length = None
        else:
            value = validators.string(value)
            if '%' not in value:
                raise errors.HighchartsValueError(f'rear_length expects a percentage '
                                                  f'string. Received: {value}')
            self._rear_length = value

    @property
    def top_width(self) -> Optional[int | float | Decimal]:
        """The width of the top of the dial, closest to the perimeter. Defaults to ``1``.

        .. note::

          The pivot narrows in from the base to the top.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._top_width

    @top_width.setter
    def top_width(self, value):
        self._top_width = validators.numeric(value, minimum = 0)

    @classmethod
    def from_dict(cls, as_dict):
        kwargs = {
            'background_color': as_dict.pop('backgroundColor', None),
            'base_length': as_dict.pop('baseLength', None),
            'base_width': as_dict.pop('baseWidth', None),
            'border_color': as_dict.pop('borderColor', None),
            'border_width': as_dict.pop('borderWidth', None),
            'path': as_dict.pop('path', None),
            'radius': as_dict.pop('radius', None),
            'rear_length': as_dict.pop('rearLength', None),
            'top_width': as_dict.pop('topWidth', None)
        }

        return cls(**kwargs)

    def to_dict(self) -> Optional[dict]:
        untrimmed = {
            'backgroundColor': self.background_color,
            'baseLength': self.base_length,
            'baseWidth': self.base_width,
            'borderColor': self.border_color,
            'borderWidth': self.border_width,
            'path': self.path,
            'radius': self.radius,
            'rearLength': self.rear_length,
            'topWidth': self.top_width
        }

        return self.trim_dict(untrimmed)


class PivotOptions(HighchartsMeta):
    """Options for the pivot or the center point of the gauge."""

    def __init__(self, **kwargs):
        self._background_color = None
        self._border_color = None
        self._border_width = None
        self._radius = None

        self.background_color = kwargs.pop('background_color', None)
        self.border_color = kwargs.pop('border_color', None)
        self.border_width = kwargs.pop('border_width', None)
        self.radius = kwargs.pop('radius', None)

    @property
    def background_color(self) -> Optional[str | Gradient | Pattern]:
        """The background color or fill of the pivot. Defaults to '#000000'.

        :rtype: :class:`str <python:str>`, :class:`Gradient`, :class:`Pattern``, or
          :obj:`None <python:None>`
        """
        return self._background_color

    @background_color.setter
    def background_color(self, value):
        if not value:
            self._background_color = None
        elif isinstance(value, (Gradient, Pattern)):
            self._background_color = value
        elif isinstance(value, (dict, str)) and 'linearGradient' in value:
            try:
                self._background_color = Gradient.from_json(value)
            except ValueError:
                if isinstance(value, dict):
                    self._background_color = Gradient.from_dict(value)
                else:
                    self._background_color = validators.string(value)
        elif isinstance(value, dict) and 'linear_gradient' in value:
            self._background_color = Gradient(**value)
        elif isinstance(value, (dict, str)) and 'patternOptions' in value:
            try:
                self._background_color = Pattern.from_json(value)
            except ValueError:
                if isinstance(value, dict):
                    self._background_color = Pattern.from_dict(value)
                else:
                    self._background_color = validators.string(value)
        elif isinstance(value, dict) and 'pattern_options' in value:
            self._background_color = Pattern(**value)
        else:
            raise errors.HighchartsValueError(f'Unable to resolve value to a string, '
                                              f'Gradient, or Pattern. Value received '
                                              f'was: {value}')

    @property
    def border_color(self) -> Optional[str | Gradient | Pattern]:
        """The border or stroke color of the pivot. Defaults to ``'#cccccc'``.

        .. warning::

          By default, the :meth:`PivotOptions.border_width` is ``0``, so be sure to set
          that property to a non-default value if you wish to apply a border color.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._border_color

    @border_color.setter
    def border_color(self, value):
        if not value:
            self._border_color = None
        elif isinstance(value, (Gradient, Pattern)):
            self._border_color = value
        elif isinstance(value, (dict, str)) and 'linearGradient' in value:
            try:
                self._border_color = Gradient.from_json(value)
            except ValueError:
                if isinstance(value, dict):
                    self._border_color = Gradient.from_dict(value)
                else:
                    self._border_color = validators.string(value)
        elif isinstance(value, dict) and 'linear_gradient' in value:
            self._border_color = Gradient(**value)
        elif isinstance(value, (dict, str)) and 'patternOptions' in value:
            try:
                self._border_color = Pattern.from_json(value)
            except ValueError:
                if isinstance(value, dict):
                    self._border_color = Pattern.from_dict(value)
                else:
                    self._border_color = validators.string(value)
        elif isinstance(value, dict) and 'pattern_options' in value:
            self._border_color = Pattern(**value)
        else:
            raise errors.HighchartsValueError(f'Unable to resolve value to a string, '
                                              f'Gradient, or Pattern. Value received '
                                              f'was: {value}')

    @property
    def border_width(self) -> Optional[int | float | Decimal]:
        """TThe border or stroke width of the pivot. Defaults to ``0``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._border_width

    @border_width.setter
    def border_width(self, value):
        self._border_width = validators.numeric(value,
                                                allow_empty = True,
                                                minimum = 0)

    @property
    def radius(self) -> Optional[int | float | Decimal]:
        """The pixel radius of the pivot. Defaults to ``5``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = validators.numeric(value, allow_empty = True)

    @classmethod
    def from_dict(cls, as_dict):
        kwargs = {
            'background_color': as_dict.pop('backgroundColor', None),
            'border_color': as_dict.pop('borderColor', None),
            'border_width': as_dict.pop('borderWidth', None),
            'radius': as_dict.pop('radius', None)
        }

        return cls(**kwargs)

    def to_dict(self) -> Optional[dict]:
        untrimmed = {
            'backgroundColor': self.background_color,
            'borderColor': self.border_color,
            'borderWidth': self.border_width,
            'radius': self.radius
        }

        return self.trim_dict(untrimmed)


class GaugeOptions(GenericTypeOptions):
    """General options to apply to all Gauge series types.

    Gauges are circular plots displaying one or more values with a dial pointing to
    values along the perimeter.

    .. figure:: _static/gauge-example.png
      :alt: Gauge Example Chart
      :align: center

    """

    def __init__(self, **kwargs):
        self._color_index = None
        self._crisp = None
        self._dial = None
        self._linecap = None
        self._line_width = None
        self._overshoot = None
        self._pivot = None
        self._point_interval = None
        self._point_interval_unit = None
        self._point_start = None
        self._relative_x_value = None
        self._shadow = None
        self._wrap = None

        self.color_index = kwargs.pop('color_index', None)
        self.crisp = kwargs.pop('crisp', None)
        self.dial = kwargs.pop('dial', None)
        self.linecap = kwargs.pop('linecap', None)
        self.line_width = kwargs.pop('line_width', None)
        self.overshoot = kwargs.pop('overshoot', None)
        self.pivot = kwargs.pop('pivot', None)
        self.point_interval = kwargs.pop('point_interval', None)
        self.point_interval_unit = kwargs.pop('point_interval_unit', None)
        self.point_start = kwargs.pop('point_start', None)
        self.relative_x_value = kwargs.pop('relative_x_value', None)
        self.shadow = kwargs.pop('shadow', None)
        self.wrap = kwargs.pop('wrap', None)

        super().__init__(**kwargs)

    @property
    def color_index(self) -> Optional[int]:
        """When operating in :term:`styled mode`, a specific color index to use for the
        series, so that its graphic representations are given the class name
        ``highcharts-color-{n}``.

        Defaults to :obj:`None <python:None>`.

        :rtype: :class:`int <python:int>` or :obj:`None <python:None>`
        """
        return self._color_index

    @color_index.setter
    def color_index(self, value):
        self._color_index = validators.integer(value,
                                               allow_empty = True,
                                               minimum = 0)

    @property
    def crisp(self) -> Optional[bool]:
        """If ``True``, each point or column edge is rounded to its nearest pixel in order
        to render sharp on screen. Defaults to ``True``.

        .. hint::

          In some cases, when there are a lot of densely packed columns, this leads to
          visible difference in column widths or distance between columns. In these cases,
          setting ``crisp`` to ``False`` may look better, even though each column is
          rendered blurry.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._crisp

    @crisp.setter
    def crisp(self, value):
        if value is None:
            self._crisp = None
        else:
            self._crisp = bool(value)

    @property
    def dial(self) -> Optional[DialOptions]:
        """Options for the dial or arrow pointer of the gauge.

        :rtype: :class:`DialOptions` or :obj:`None <python:None>`
        """
        return self._dial

    @dial.setter
    @class_sensitive(DialOptions)
    def dial(self, value):
        self._dial = value

    @property
    def linecap(self) -> Optional[str]:
        """The SVG value used for the ``stroke-linecap`` and ``stroke-linejoin`` of a line
        graph. Defaults to ``'round'``, which means that lines are rounded in the ends and
        bends.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._linecap

    @linecap.setter
    def linecap(self, value):
        self._linecap = validators.string(value, allow_empty = True)

    @property
    def line_width(self) -> Optional[int | float | Decimal]:
        """Pixel width of the graph line. Defaults to ``2``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._line_width

    @line_width.setter
    def line_width(self, value):
        self._line_width = validators.numeric(value,
                                              allow_empty = True,
                                              minimum = 0)

    @property
    def overshoot(self) -> Optional[int | float | Decimal]:
        """Allow the dial to overshoot the end of the perimeter axis by this many degrees.

        For example, if this option is set to ``5`` and the gauge axis goes from ``0`` to
        ``60``, a value of ``100``, or ``1000``, will show ``5`` degrees beyond the end of
        the axis.

        Defaults to :obj:`None <python:None>`.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._overshoot

    @overshoot.setter
    def overshoot(self, value):
        self._overshoot = validators.numeric(value,
                                             allow_empty = True,
                                             minimum = 0)

    @property
    def pivot(self) -> Optional[PivotOptions]:
        """Options for the pivot or the center point of the gauge.

        :rtype: :class:`PivotOptions` or :obj:`None <python:None>`
        """
        return self._pivot

    @pivot.setter
    @class_sensitive(PivotOptions)
    def pivot(self, value):
        self._pivot = value

    @property
    def point_interval(self) -> Optional[int | float | Decimal]:
        """If no x values are given for the points in a series, ``point_interval`` defines
        the interval of the x values. Defaults to ``1``.

        For example, if a series contains one value every decade starting from year 0, set
        ``point_interval`` to ``10``. In true datetime axes, the ``point_interval`` is set
        in milliseconds.

        .. hint::

          ``point_interval`` can be also be combined with
          :meth:`point_interval_unit <AreaOptions.point_interval_unit>` to draw irregular
          time intervals.

        .. note::

          If combined with :meth:`relative_x_value <AreaOptions.relative_x_value>`, an x
          value can be set on each point, and the ``point_interval`` is added x times to
          the :meth:`point_start <AreaOptions.point_start>` setting.

        .. warning::

          This options applies to the series data, not the interval of the axis ticks,
          which is independent.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._point_interval

    @point_interval.setter
    def point_interval(self, value):
        self._point_interval = validators.numeric(value,
                                                  allow_empty = True,
                                                  minimum = 0)

    @property
    def point_interval_unit(self) -> Optional[str]:
        """On datetime series, this allows for setting the
        :meth:`point_interval <AreaOptions.point_interval>` to irregular time units, day,
        month, and year.

        A day is usually the same as 24 hours, but ``point_interval_unit`` also takes the
        DST crossover into consideration when dealing with local time.

        Combine this option with :meth:`point_interval <AreaOptions.point_interval>` to
        draw weeks, quarters, 6 month periods, 10 year periods, etc.

        .. warning::

          This options applies to the series data, not the interval of the axis ticks,
          which is independent.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._point_interval_unit

    @point_interval_unit.setter
    def point_interval_unit(self, value):
        self._point_interval_unit = validators.string(value, allow_empty = True)

    @property
    def point_start(self) -> Optional[int | float | Decimal]:
        """If no x values are given for the points in a series, ``point_start`` defines
        on what value to start. For example, if a series contains one yearly value
        starting from 1945, set ``point_start`` to ``1945``. Defaults to ``0``.

        .. note::

          If combined with :meth:`relative_x_value <AreaOptions.relative_x_value>`, an x
          value can be set on each point. The x value from the point options is multiplied
          by :meth:`point_interval <AreaOptions.point_interval>` and added to
          ``point_start`` to produce a modified x value.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._point_start

    @point_start.setter
    def point_start(self, value):
        self._point_start = validators.numeric(value, allow_empty = True)

    @property
    def relative_x_value(self) -> Optional[bool]:
        """When ``True``, X values in the data set are relative to the current
        :meth:`point_start <AreaOptions.point_start>`,
        :meth:`point_interval <AreaOptions.point_interval>`, and
        :meth:`point_interval_unit <AreaOptions.point_interval_unit>` settings. This
        allows compression of the data for datasets with irregular X values. Defaults to
        ``False``.

        The real X values are computed on the formula ``f(x) = ax + b``, where ``a`` is
        the :meth:`point_interval <AreaOptions.point_interval>` (optionally with a time
        unit given by :meth:`point_interval_unit <AreaOptions.point_interval_unit>`), and
        ``b`` is the :meth:`point_start <AreaOptions.point_start>`.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._relative_x_value

    @relative_x_value.setter
    def relative_x_value(self, value):
        if value is None:
            self._relative_x_value = None
        else:
            self._relative_x_value = bool(value)

    @property
    def shadow(self) -> Optional[bool | ShadowOptions]:
        """Configuration for the shadow to apply to the tooltip. Defaults to
        ``False``.

        If ``False``, no shadow is applied.

        :returns: The shadow configuration to apply or a boolean setting which hides the
          shadow or displays the default shadow.
        :rtype: :class:`bool <python:bool>` or :class:`ShadowOptions`
        """
        return self._shadow

    @shadow.setter
    def shadow(self, value):
        if isinstance(value, bool):
            self._shadow = value
        elif not value:
            self._shadow = None
        else:
            value = validate_types(value,
                                   types = ShadowOptions)
            self._shadow = value

    @property
    def wrap(self) -> Optional[bool]:
        """When ``True``, the dial will wrap around the axes. When wrap is ``False``, the
        dial stops at 360. Defaults to ``True``.

        For instance, if ``True`` in a full-range gauge going from ``0`` to ``360``, a
        value of ``400`` will point to ``40``.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._wrap

    @wrap.setter
    def wrap(self, value):
        if value is None:
            self._wrap = None
        else:
            self._wrap = bool(value)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        """Convenience method which returns the keyword arguments used to initialize the
        class from a Highcharts Javascript-compatible :class:`dict <python:dict>` object.

        :param as_dict: The HighCharts JS compatible :class:`dict <python:dict>`
          representation of the object.
        :type as_dict: :class:`dict <python:dict>`

        :returns: The keyword arguments that would be used to initialize an instance.
        :rtype: :class:`dict <python:dict>`

        """
        kwargs = {
            'accessibility': as_dict.pop('accessibility', None),
            'allow_point_select': as_dict.pop('allowPointSelect', False),
            'animation': as_dict.pop('animation', None),
            'class_name': as_dict.pop('className', None),
            'clip': as_dict.pop('clip', True),
            'color': as_dict.pop('color', None),
            'cursor': as_dict.pop('cursor', None),
            'custom': as_dict.pop('custom', None),
            'dash_style': as_dict.pop('dashStyle', None),
            'data_labels': as_dict.pop('dataLabels', None),
            'description': as_dict.pop('description', None),
            'enable_mouse_tracking': as_dict.pop('enableMouseTracking', True),
            'events': as_dict.pop('events', None),
            'include_in_data_export': as_dict.pop('includeInDataExport', None),
            'keys': as_dict.pop('keys', None),
            'label': as_dict.pop('label', None),
            'linked_to': as_dict.pop('linkedTo', None),
            'marker': as_dict.pop('marker', None),
            'on_point': as_dict.pop('onPoint', None),
            'opacity': as_dict.pop('opacity', None),
            'point': as_dict.pop('point', None),
            'point_description_formatter': as_dict.pop('pointDescriptionFormatter', None),
            'selected': as_dict.pop('selected', False),
            'show_checkbox': as_dict.pop('showCheckbox', False),
            'show_in_legend': as_dict.pop('showInLegend', None),
            'skip_keyboard_navigation': as_dict.pop('skipKeyboardNavigation', None),
            'states': as_dict.pop('states', None),
            'sticky_tracking': as_dict.pop('stickyTracking', None),
            'threshold': as_dict.pop('threshold', None),
            'tooltip': as_dict.pop('tooltip', None),
            'turbo_threshold': as_dict.pop('turboThreshold', None),
            'visible': as_dict.pop('visible', True),

            'color_index': as_dict.pop('colorIndex', None),
            'crisp': as_dict.pop('crisp', True),
            'linecap': as_dict.pop('linecap', 'round'),
            'line_width': as_dict.pop('lineWidth', 2),
            'point_interval': as_dict.pop('pointInterval', 1),
            'point_interval_unit': as_dict.pop('pointIntervalUnit', None),
            'point_placement': as_dict.pop('pointPlacement', None),
            'relative_x_value': as_dict.pop('relativeXValue', False),
            'shadow': as_dict.pop('shadow', False),

            'dial': as_dict.pop('dial', None),
            'overshoot': as_dict.pop('overshoot', None),
            'pivot': as_dict.pop('pivot', None),
            'wrap': as_dict.pop('wrap', None)
        }

        return kwargs

    def to_dict(self) -> dict:
        untrimmed = {
            'colorIndex': self.color_index,
            'crisp': self.crisp,
            'dial': self.dial,
            'linecap': self.linecap,
            'lineWidth': self.line_width,
            'overshoot': self.overshoot,
            'pivot': self.pivot,
            'pointInterval': self.point_interval,
            'pointIntervalUnit': self.point_interval_unit,
            'pointStart': self.point_start,
            'relativeXValue': self.relative_x_value,
            'shadow': self.shadow,
            'wrap': self.wrap
        }
        parent_as_dict = super().to_dict()

        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return self.trim_dict(untrimmed)


class SolidGauge(SeriesOptions):
    """General options to apply to all Solid Gauge series types.

    A solid gauge is a circular gauge where the value is indicated by a filled arc,
    and the color of the arc may variate with the value.

    .. figure:: _static/solidgauge-example.png
      :alt: SolidGauge Example Chart
      :align: center

    """

    def __init__(self, **kwargs):
        self._inner_radius = None
        self._overshoot = None
        self._radius = None
        self._rounded = None

        self.inner_radius = kwargs.pop('inner_radius', None)
        self.overshoot = kwargs.pop('overshoot', None)
        self.radius = kwargs.pop('radius', None)
        self.rounded = kwargs.pop('rounded', None)

        super().__init__(**kwargs)

    @property
    def inner_radius(self) -> Optional[str | int | float | Decimal]:
        """The inner radius for points in a solid gauge. Can be given as a number (pixels)
        or percentage string. Defaults to ``60``.

        :rtype: numeric, :class:`str <python:str>`, or :obj:`None <python:None>`
        """
        return self._inner_radius

    @inner_radius.setter
    def inner_radius(self, value):
        if value is None:
            self._inner_radius = None
        else:
            try:
                value = validators.string(value)
                if '%' not in value:
                    raise ValueError
            except ValueError:
                value = validators.numeric(value, minimum = 0)

            self._inner_radius = value

    @property
    def overshoot(self) -> Optional[int | float | Decimal]:
        """Allow the dial to overshoot the end of the perimeter axis by this many degrees.

        For example, if this option is set to ``5`` and the gauge axis goes from ``0`` to
        ``60``, a value of ``100``, or ``1000``, will show ``5`` degrees beyond the end of
        the axis.

        Defaults to ``0``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._overshoot

    @overshoot.setter
    def overshoot(self, value):
        self._overshoot = validators.numeric(value,
                                             allow_empty = True,
                                             minimum = 0)

    @property
    def radius(self) -> Optional[str | int | float | Decimal]:
        """The outer radius for points in a solid gauge. Can be given as a number (pixels)
        or percentage string. Defaults to ``100``.

        :rtype: numeric, :class:`str <python:str>`, or :obj:`None <python:None>`
        """
        return self._radius

    @radius.setter
    def radius(self, value):
        if value is None:
            self._radius = None
        else:
            try:
                value = validators.string(value)
                if '%' not in value:
                    raise ValueError
            except ValueError:
                value = validators.numeric(value, minimum = 0)

            self._radius = value

    @property
    def rounded(self) -> Optional[bool]:
        """If ``True``, draws rounded edges on the gauge. Defaults to ``False``.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._rounded

    @rounded.setter
    def rounded(self, value):
        if value is None:
            self._rounded = None
        else:
            self._rounded = bool(value)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'accessibility': as_dict.pop('accessibility', None),
            'allow_point_select': as_dict.pop('allowPointSelect', False),
            'animation': as_dict.pop('animation', None),
            'class_name': as_dict.pop('className', None),
            'clip': as_dict.pop('clip', True),
            'color': as_dict.pop('color', None),
            'cursor': as_dict.pop('cursor', None),
            'custom': as_dict.pop('custom', None),
            'dash_style': as_dict.pop('dashStyle', None),
            'data_labels': as_dict.pop('dataLabels', None),
            'description': as_dict.pop('description', None),
            'enable_mouse_tracking': as_dict.pop('enableMouseTracking', True),
            'events': as_dict.pop('events', None),
            'include_in_data_export': as_dict.pop('includeInDataExport', None),
            'keys': as_dict.pop('keys', None),
            'label': as_dict.pop('label', None),
            'linked_to': as_dict.pop('linkedTo', None),
            'marker': as_dict.pop('marker', None),
            'on_point': as_dict.pop('onPoint', None),
            'opacity': as_dict.pop('opacity', None),
            'point': as_dict.pop('point', None),
            'point_description_formatter': as_dict.pop('pointDescriptionFormatter', None),
            'selected': as_dict.pop('selected', False),
            'show_checkbox': as_dict.pop('showCheckbox', False),
            'show_in_legend': as_dict.pop('showInLegend', None),
            'skip_keyboard_navigation': as_dict.pop('skipKeyboardNavigation', None),
            'states': as_dict.pop('states', None),
            'threshold': as_dict.pop('threshold', None),
            'tooltip': as_dict.pop('tooltip', None),
            'turbo_threshold': as_dict.pop('turboThreshold', None),
            'visible': as_dict.pop('visible', True),

            'animation_limit': as_dict.pop('animationLimit', None),
            'boost_blending': as_dict.pop('boostBlending', None),
            'boost_threshold': as_dict.pop('boostThreshold', 5000),
            'color_axis': as_dict.pop('colorAxis', None),
            'color_index': as_dict.pop('colorIndex', None),
            'color_key': as_dict.pop('colorKey', None),
            'connect_ends': as_dict.pop('connectEnds', None),
            'connect_nulls': as_dict.pop('connectNulls', False),
            'crisp': as_dict.pop('crisp', True),
            'crop_threshold': as_dict.pop('cropThreshold', 300),
            'data_sorting': as_dict.pop('dataSorting', None),
            'drag_drop': as_dict.pop('dragDrop', None),
            'find_nearest_point_by': as_dict.pop('findNearestPointBy', None),
            'get_extremes_for_all': as_dict.pop('getExtremesForAll', False),
            'linecap': as_dict.pop('linecap', 'round'),
            'line_width': as_dict.pop('lineWidth', 2),
            'negative_color': as_dict.pop('negativeColor', None),
            'point_interval': as_dict.pop('pointInterval', 1),
            'point_interval_unit': as_dict.pop('pointIntervalUnit', None),
            'point_placement': as_dict.pop('pointPlacement', None),
            'point_start': as_dict.pop('pointStart', 0),
            'relative_x_value': as_dict.pop('relativeXValue', False),
            'shadow': as_dict.pop('shadow', False),
            'soft_threshold': as_dict.pop('softThreshold', True),
            'stacking': as_dict.pop('stacking', None),
            'step': as_dict.pop('step', None),
            'zone_axis': as_dict.pop('zoneAxis', 'y'),
            'zones': as_dict.pop('zones', None),

            'inner_radius': as_dict.pop('innerRadius', None),
            'overshoot': as_dict.pop('overshoot', None),
            'radius': as_dict.pop('radius', None),
            'rounded': as_dict.pop('rounded', None)
        }

        return kwargs

    def to_dict(self) -> dict:
        untrimmed = {
            'inner_radius': self.inner_radius,
            'overshoot': self.overshoot,
            'radius': self.radius,
            'rounded': self.rounded
        }
        parent_as_dict = super(self).to_dict()

        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return self.trim_dict(untrimmed)
