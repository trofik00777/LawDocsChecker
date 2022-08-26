from typing import List, Dict

from pydantic import BaseModel, Field


class ResponseModel(BaseModel):
    # signs: Dict[str, str]
    # verdict: str
    sentences: List[str] = Field(None, alias='docstrings')
