"""Check that Quotes can be extracted from structured data files.

The `load_neos` function should load a collection of `NearEarthObject`s from a
CSV file, and the `load_approaches` function should load a collection of
`CloseApproach` objects from a JSON file.

To run these tests from the project root, run:

    $ python3 -m unittest --verbose tests.test_quote_engine

These tests should pass when the Quoate Engine is complete.
"""
from typing import List
import pathlib
import unittest

from QuoteEngine import QuoteModel, Ingestor, CSVIngestor,\
                        DocxIngestor, PDFIngestor,\
                        TextIngestor


TESTS_ROOT = pathlib.Path(
    __file__).parents[1].resolve() / '_data' / 'SimpleLines'
TEST_CSV_FILE = TESTS_ROOT / 'SimpleLines.csv'
TEST_DOCX_FILE = TESTS_ROOT / 'SimpleLines.docx'
TEST_PDF_FILE = TESTS_ROOT / 'SimpleLines.pdf'
TEST_TXT_FILE = TESTS_ROOT / 'SimpleLines.txt'


class TestCSVingestor(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.quotes = CSVIngestor.parse(fr'{TEST_CSV_FILE}')

    def test_Quotes_are_List(self):
        self.assertIsInstance(self.quotes, List)

    def test_Quotes_are_QuoteModel_type(self):
        for quote in self.quotes:
            self.assertIsNotNone(quote)
            self.assertIsInstance(quote, QuoteModel)

    def test_Quotes_contain_all_elements(self):
        self.assertEqual(len(self.quotes), 5)

    def test_3rd_quote_is_correct(self):
        self.assertEqual(self.quotes[2].author, 'Author 3')
        self.assertEqual(self.quotes[2].body, 'Line 3')


class TestDocxIngestor(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.quotes = DocxIngestor.parse(fr'{TEST_DOCX_FILE}')

    def test_Quotes_are_List(self):
        self.assertIsInstance(self.quotes, List)

    def test_Quotes_are_QuoteModel_type(self):
        for quote in self.quotes:
            self.assertIsNotNone(quote)
            self.assertIsInstance(quote, QuoteModel)

    def test_Quotes_contain_all_elements(self):
        self.assertEqual(len(self.quotes), 5)

    def test_3rd_quote_is_correct(self):
        self.assertEqual(self.quotes[2].author, 'Author 3')
        self.assertEqual(self.quotes[2].body, 'Line 3')


class TestPDFIngestor(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.quotes = PDFIngestor.parse(fr'{TEST_PDF_FILE}')

    def test_Quotes_are_List(self):
        self.assertIsInstance(self.quotes, List)

    def test_Quotes_are_QuoteModel_type(self):
        for quote in self.quotes:
            self.assertIsNotNone(quote)
            self.assertIsInstance(quote, QuoteModel)

    def test_Quotes_contain_all_elements(self):
        self.assertEqual(len(self.quotes), 5)

    def test_3rd_quote_is_correct(self):
        self.assertEqual(self.quotes[2].author, 'Author 3')
        self.assertEqual(self.quotes[2].body, 'Line 3')


class TestTextIngestor(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.quotes = TextIngestor.parse(fr'{TEST_TXT_FILE}')

    def test_Quotes_are_List(self):
        self.assertIsInstance(self.quotes, List)

    def test_Quotes_are_QuoteModel_type(self):
        for quote in self.quotes:
            self.assertIsNotNone(quote)
            self.assertIsInstance(quote, QuoteModel)

    def test_Quotes_contain_all_elements(self):
        self.assertEqual(len(self.quotes), 5)

    def test_3rd_quote_is_correct(self):
        self.assertEqual(self.quotes[2].author, 'Author 3')
        self.assertEqual(self.quotes[2].body, 'Line 3')


class TestGenericIngestor(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.quotes = Ingestor.parse(fr'{TEST_TXT_FILE}')

    def test_Quotes_are_List(self):
        self.assertIsInstance(self.quotes, List)

    def test_Quotes_are_QuoteModel_type(self):
        for quote in self.quotes:
            self.assertIsNotNone(quote)
            self.assertIsInstance(quote, QuoteModel)

    def test_Quotes_contain_all_elements(self):
        self.assertEqual(len(self.quotes), 5)

    def test_3rd_quote_is_correct(self):
        self.assertEqual(self.quotes[2].author, 'Author 3')
        self.assertEqual(self.quotes[2].body, 'Line 3')


if __name__ == '__main__':
    unittest.main()
