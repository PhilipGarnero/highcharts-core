from __future__ import annotations
from typing import Optional

from validator_collection import validators

from highcharts_core import constants
from highcharts_core.metaclasses import HighchartsMeta


class LegendTitle(HighchartsMeta):
    """A title to be added on top of the legend."""

    def __init__(self, **kwargs):
        self._style = None
        self._text = None

        self.style = kwargs.get('style', None)
        self.text = kwargs.get('text', None)

    @property
    def style(self) -> Optional[str | dict]:
        """CSS styling to apply to the title. Defaults to
        ``'{"fontSize": "0.75em", "fontWeight": "bold"}'``.

        :rtype: :class:`str <python:str>` or :class:`dict <python:dict>` or 
          :obj:`None <python:None>`
        """
        return self._style

    @style.setter
    def style(self, value):
        try:
            self._style = validators.dict(value, allow_empty = True)
        except (ValueError, TypeError):
            self._style = validators.string(value, 
                                            allow_empty = True,
                                            coerce_value = True)

    @property
    def text(self) -> Optional[str]:
        """A text or HTML string for the tite.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._text

    @text.setter
    def text(self, value):
        self._text = validators.string(value, allow_empty = True)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'style': as_dict.get('style', None),
            'text': as_dict.get('text', None)
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'style': self.style,
            'text': self.text
        }

        return untrimmed
