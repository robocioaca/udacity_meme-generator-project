class QuoteModel():
    """Quotes which will be later added to memes."""

    def __init__(self, author: str, body: str) -> None:
        """Build a quote

        Arguments:
            author {str} -- quote's author.
            body {str} -- the actual quote message.
        """
        self.author = author
        self.body = body

    def __repr__(self):
        """Pretty print oneself"""
        return f'”{self.body}” - {self.author}'
