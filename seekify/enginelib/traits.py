import dataclasses
import typing
from typing import Dict, Optional, Literal, Union, Iterable


class EngineTraits:
    regns: Dict[str, str] = dataclasses.field(default_factory=dict)
    langs: Dict[str, str] = dataclasses.field(default_factory=dict)
    all_locale: Optional[str] = None
    data_type: Literal['traits_v1'] = 'traits_v1'
    custom: Dict[str, Union[Dict[str, Dict], Iterable[str]]] = dataclasses.field(default_factory=dict)

    def get_lang(self, seekify_local: str, default=None):
        if seekify_local == 'all' and self.all_locale is not None:
            return self.all_locale
        else:
            