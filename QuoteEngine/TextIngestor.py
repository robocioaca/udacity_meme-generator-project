from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

class TextIngestor(IngestorInterface):
    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('Can ingest TXT files only!')

        bag_of_quotes = []
        with open(path, 'r') as infile:
            for line in infile:
                body, author = line.split(' - ')
                new_quote = QuoteModel(author, body)
                bag_of_quotes.append(new_quote)

        return bag_of_quotes
