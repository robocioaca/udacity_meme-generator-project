from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class TextIngestor(IngestorInterface):
    """Concrete startegy object class for TXT files """
    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Load quotes from location

        Arguments:
            path {str} -- the TXT file location, to load quotes.
        """
        if not cls.can_ingest(path):
            raise Exception('Can ingest TXT files only!')

        bag_of_quotes = []
        with open(path, 'r') as infile:
            for line in infile:
                body, author = line.split(' - ')
                new_quote = QuoteModel(author, body)
                bag_of_quotes.append(new_quote)

        return bag_of_quotes
