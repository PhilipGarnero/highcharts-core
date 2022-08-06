from typing import Optional

from validator_collection import validators

from highcharts import constants
from highcharts.metaclasses import HighchartsMeta


class ZoomLanguageOptions(HighchartsMeta):
    """Chart and map zoom accessibility language options."""

    def __init__(self, **kwargs):
        self._map_zoom_in = None
        self._map_zoom_out = None
        self._reset_zoom_button = None

        self.map_zoom_in = kwargs.pop('map_zoom_in', None)
        self.map_zoom_out = kwargs.pop('map_zoom_out', None)
        self.reset_zoom_button = kwargs.pop('reset_zoom_button', None)

    @property
    def map_zoom_in(self) -> Optional[str]:
        f"""Defaults to
        ``'{constants.DEFAULT_LANG_ACS_ZOOM_MAP_ZOOM_IN}'``

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._map_zoom_in

    @map_zoom_in.setter
    def map_zoom_in(self, value):
        self._map_zoom_in = validators.string(value, allow_empty = True)

    @property
    def map_zoom_out(self) -> Optional[str]:
        f"""Defaults to
        ``'{constants.DEFAULT_LANG_ACS_ZOOM_MAP_ZOOM_OUT}'``

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._map_zoom_out

    @map_zoom_out.setter
    def map_zoom_out(self, value):
        self._map_zoom_out = validators.string(value, allow_empty = True)

    @property
    def reset_zoom_button(self) -> Optional[str]:
        f"""Defaults to
        ``'{constants.DEFAULT_LANG_ACS_ZOOM_RESET_ZOOM_BTN}'``

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._reset_zoom_button

    @reset_zoom_button.setter
    def reset_zoom_button(self, value):
        self._reset_zoom_button = validators.string(value, allow_empty = True)

    @classmethod
    def from_dict(cls, as_dict):
        kwargs = {
            'map_zoom_in': as_dict.pop('mapZoomIn', None),
            'map_zoom_out': as_dict.pop('mapZoomOut', None),
            'reset_zoom_button': as_dict.pop('resetZoomButton', None),
        }

        return cls(**kwargs)

    def _to_untrimmed_dict(self) -> dict:
        untrimmed = {
            'mapZoomIn': self.map_zoom_in,
            'mapZoomOut': self.map_zoom_out,
            'resetZoomButton': self.reset_zoom_button
        }

        return untrimmed
