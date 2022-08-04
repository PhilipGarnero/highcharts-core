from typing import Optional
from decimal import Decimal

from validator_collection import validators, checkers

from highcharts import constants, errors
from highcharts.series.data.cartesian import CartesianData


class VectorData(CartesianData):
    """Variant of :class:`CartesianData` which extends the data point with ``direction``
    and ``length`` attributes."""

    def __init__(self, **kwargs):
        self._direction = None
        self._length = None

        self.direction = kwargs.pop('direction', None)
        self.length = kwargs.pop('length', None)

        super().__init__(**kwargs)

    @property
    def direction(self) -> Optional[int | float | Decimal]:
        """The vector direction expressed in degrees, where ``0`` is north (pointing
        towards south). Defaults to :obj:`None <python:None>`.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._direction

    @direction.setter
    def direction(self, value):
        self._direction = validators.numeric(value, allow_empty = True)

    @property
    def length(self) -> Optional[int | float | Decimal]:
        """The length of the vector. Defaults to :obj:`None <python:None>`.

        .. note::

          The actual length rendered on-screen will be tied to
          :meth:`VectorSeries.vector_length`.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._length

    @length.setter
    def length(self, value):
        self._length = validators.numeric(value, allow_empty = True)

    @classmethod
    def from_setter(cls, value):
        """Generator method which produces a collection of :class:`VectorData`
        instances derived from ``value``. Generally consumed by the setter methods in
        series-type specific data classes.

        :rtype: :class:`list <python:list>` of :obj:`VectorData` instances
        """
        if not value:
            return []
        elif not checkers.is_iterable(value):
            value = [value]

        collection = []
        for item in value:
            if checkers.is_type(item, 'VectorData'):
                as_obj = item
            elif checkers.is_dict(item):
                as_obj = cls.from_dict(item)
            elif item is None or isinstance(item, constants.EnforcedNullType):
                as_obj = cls()
            elif len(item) == 4:
                as_obj = cls(x = item[0],
                             y = item[1],
                             length = item[2],
                             direction = item[3])
            elif len(item) == 3:
                as_obj = cls(x = None,
                             y = item[0],
                             length = item[1],
                             direction = item[2])
            else:
                raise errors.HighchartsValueError(f'each data point supplied must either '
                                                  f'be a Vector Data Point or be '
                                                  f'coercable to one. Could not coerce: '
                                                  f'{item}')

            collection.append(as_obj)

        return collection

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
            'class_name': as_dict.pop('className', None),
            'color': as_dict.pop('color', None),
            'color_index': as_dict.pop('colorIndex', None),
            'custom': as_dict.pop('custom', None),
            'description': as_dict.pop('description', None),
            'events': as_dict.pop('events', None),
            'id': as_dict.pop('id', None),
            'label_rank': as_dict.pop('labelrank', None),
            'name': as_dict.pop('name', None),
            'selected': as_dict.pop('selected', None),

            'data_labels': as_dict.pop('dataLabels', None),
            'drag_drop': as_dict.pop('dragDrop', None),
            'drilldown': as_dict.pop('drilldown', None),
            'marker': as_dict.pop('marker', None),
            'x': as_dict.pop('x', None),
            'y': as_dict.pop('y', None),

            'direction': as_dict.pop('direction', None),
            'length': as_dict.pop('length', None),
        }

        return kwargs

    def to_dict(self) -> Optional[dict]:
        untrimmed = {
            'accessibility': self.accessibility,
            'className': self.class_name,
            'color': self.color,
            'colorIndex': self.color_index,
            'custom': self.custom,
            'description': self.description,
            'events': self.events,
            'id': self.id,
            'labelrank': self.label_rank,
            'name': self.name,
            'selected': self.selected,

            'dataLabels': self.data_labels,
            'dragDrop': self.drag_drop,
            'drilldown': self.drilldown,
            'marker': self.marker,
            'x': self.x,
            'y': self.y,

            'direction': self.direction,
            'length': self.length,
        }

        return self.trim_dict(untrimmed)
