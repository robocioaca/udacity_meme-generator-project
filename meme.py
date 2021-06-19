import os
import random
import itertools

from QuoteEngine import QuoteModel, Ingestor, NoIngestorFound
from MemeGenerator import MemeEngine
import argparse


def generate_meme(path=None, body=None, author=None):
    """ Generate a meme given an path and a quote """
    img = None
    quote = None

    if path is None:
        images = "./_data/photos/dog/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs.extend([os.path.join(root, name) for name in files])

        img = random.choice(imgs)
    else:
        img = path[0]

    if body is None:
        quote_folder = "./_data/DogQuotes/"
        quote_files = []

        for root, dirs, files in os.walk(quote_folder):
            quote_files.extend([os.path.join(root, name) for name in files])

        quotes = []
        for file in quote_files:
            try:
                quotes.extend(Ingestor.parse(file))
            except NoIngestorFound as e:
                print(f'{e.message}')

        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = QuoteModel(author, body)

    static_path = './static'
    if not os.path.isdir(static_path):
        os.mkdir(static_path)

    meme = MemeEngine(static_path)
    path = meme.make_meme(img, quote.body, quote.author)

    return path


if __name__ == "__main__":
    """Self-documenting CLI interface """
    parser = argparse.ArgumentParser(
        description="Utility for effortless meme generation :P")

    parser.add_argument('--path', type=str,
                        help="folder to load an image from")
    parser.add_argument('--body', type=str,
                        help="bits of practical wisdom for everyman")
    parser.add_argument('--author', type=str,
                        help="contemporary sage, fountain of such wisdom")

    args = parser.parse_args()

    print(generate_meme(args.path, args.body, args.author))
