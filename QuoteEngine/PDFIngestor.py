from typing import List
import subprocess
import os
import random

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class PDFIngestor(IngestorInterface):
    """Concrete startegy object class for PDF files """
    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Load quotes from location

        Arguments:
            path {str} -- the PDF file location, to load quotes.
        """
        if not cls.can_ingest(path):
            raise Exception('Can ingest PDF files only!')

        tmp = f'{random.randint(0,1000000)}.txt'
        call = subprocess.run(['pdftotext', path, tmp])

        bag_of_quotes = []
        with open(tmp, 'r') as infile:
            for line in infile:
                if line:
                    try:
                        body, author = line.strip().split(' - ')
                    except ValueError:
                        # ignore various PDF conversion artefacts
                        pass
                    else:
                        new_quote = QuoteModel(author, body.strip('"'))
                        bag_of_quotes.append(new_quote)

        os.remove(tmp)  # cleanup temp file

        return bag_of_quotes
