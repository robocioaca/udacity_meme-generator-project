from typing import List

from .IngestorInterface import IngestorInterface

from .QuoteModel import QuoteModel

from .TextIngestor import TextIngestor
from .CSVIngestor import CSVIngestor
from .DocxIngestor import DocxIngestor
from .PDFIngestor import PDFIngestor


class NoIngestorFound(Exception):
    """Raised when no suitable ingestor could be found"""

    def __init__(self, message):
        self.message = message


class Ingestor(IngestorInterface):
    """This  will encapsulate all concrete Ingestor classes.

       It should realize the IngestorInterface strategy.
    """
    # List of available concrete ingestors
    ingestors = [TextIngestor, CSVIngestor, DocxIngestor, PDFIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Flexible loading of quotes, according to filetype"""
        joy = False
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                joy = True
                return ingestor.parse(path)
        if not joy:
            raise NoIngestorFound(
                f'Could not find suitable ingestor for: {path}')
