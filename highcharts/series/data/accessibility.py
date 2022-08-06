from typing import Optional

from validator_collection import validators

from highcharts.metaclasses import HighchartsMeta


class DataPointAccessibility(HighchartsMeta):
    """Accessibility options for a series."""

    def __init__(self, **kwargs):
        self._description = None
        self._enabled = None

        self.description = kwargs.pop('description', None)
        self.enabled = kwargs.pop('enabled', None)

    @property
    def description(self) -> Optional[str]:
        """Provide a description of the data point, announced to screen readers.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._description

    @description.setter
    def description(self, value):
        self._description = validators.string(value, allow_empty = True)

    @property
    def enabled(self) -> Optional[bool]:
        """If ``True``, enable accessibility functionality for the data point.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._enabled

    @enabled.setter
    def enabled(self, value):
        if value is None:
            self._enabled = None
        else:
            self._enabled = bool(value)

    @classmethod
    def from_dict(cls, as_dict):
        kwargs = {
            'description': as_dict.pop('description', None),
            'enabled': as_dict.pop('enabled', None),
        }

        return cls(**kwargs)

    def _to_untrimmed_dict(self) -> dict:
        untrimmed = {
            'description': self.description,
            'enabled': self.enabled,
        }

        return untrimmed
