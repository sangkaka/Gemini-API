from typing import Any

from pydantic import BaseModel

from .image import Image
from .candidate import Candidate


class ModelOutput(BaseModel):
    """
    Classified output from gemini.google.com

    Parameters
    ----------
    metadata: `list[str]`
        List of chat metadata `[cid, rid, rcid]`, can be shorter than 3 elements, like `[cid, rid]` or `[cid]` only
    candidates: `list[Candidate]`
        List of all candidates returned from gemini
    chosen: `int`, optional
        Index of the chosen candidate, by default will choose the first one
    parsed_json: `Any`, optional
        Raw parsed JSON response data from Gemini API
    raw_body: `str`, optional
        Raw unparsed response text from Gemini API
    """

    metadata: list[str]
    candidates: list[Candidate]
    chosen: int = 0
    parsed_json: Any = None
    raw_body: str | None = None

    def __str__(self):
        return self.text

    def __repr__(self):
        return f"ModelOutput(metadata={self.metadata}, chosen={self.chosen}, candidates={self.candidates}, parsed_json={self.parsed_json}, raw_body={self.raw_body})"

    @property
    def text(self) -> str:
        return self.candidates[self.chosen].text

    @property
    def thoughts(self) -> str | None:
        return self.candidates[self.chosen].thoughts

    @property
    def images(self) -> list[Image]:
        return self.candidates[self.chosen].images

    @property
    def rcid(self) -> str:
        return self.candidates[self.chosen].rcid
