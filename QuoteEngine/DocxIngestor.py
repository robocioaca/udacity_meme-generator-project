from typing import List
import docx

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

class DocxIngestor(IngestorInterface):
    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('Can ingest DOCX files only!')

        quotes = []
        doc = docx.Document(path)

        for para in doc.paragraphs:
            if para.text:
                parse = para.text.split(' - ')
                new_quote = QuoteModel(parse[1], parse[0].strip('"'))
                quotes.append(new_quote)

        return quotes