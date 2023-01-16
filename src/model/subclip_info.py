from dataclasses import dataclass


@dataclass
class SubClipInfo:
    start: str
    end: int
    file_name: str
