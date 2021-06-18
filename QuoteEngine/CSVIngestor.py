from typing import List
import pandas

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class CSVIngestor(IngestorInterface):
    """Concrete startegy object class for CSV files """
    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Load quotes from location

        Arguments:
            path {str} -- the CSV file location, to load quotes.
        """
        if not cls.can_ingest(path):
            raise Exception('Can ingest CSV files only!')

        quotes = []
        df = pandas.read_csv(path, header=0)

        for index, row in df.iterrows():
            new_quote = QuoteModel(row['author'], row['body'])
            quotes.append(new_quote)

        return quotes
