class QuoteModel():
    """
    Quotes which will be later added to memes.

    Parameters:
    author (str): The quote author
    body (str): The quote contents
    """
    def __init__(self, author: str, body: str):
        self.author = author
        self.body = body


    def __repr__(self):
        """Pretty print oneself"""
        return f'”{self.body}” - {self.author}'
