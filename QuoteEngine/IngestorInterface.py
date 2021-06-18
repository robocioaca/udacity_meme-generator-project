from abc import ABC, abstractmethod

from typing import List
from .QuoteModel import QuoteModel


class IngestorInterface(ABC):
    """Abstract base class for the supported ingestor strategies """

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Check if the filetype is suitable for parsing """
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Empty interface function, to be later realized
           in the concrete strategy objects with suitable
           implementation for specific file types
         """
        pass
