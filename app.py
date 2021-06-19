from random import choice, randint
import itertools
import os
import requests
from flask import Flask, render_template, abort, request

from QuoteEngine import QuoteModel, Ingestor, NoIngestorFound
from MemeGenerator import MemeEngine

app = Flask(__name__)

static_path = './static'
if not os.path.isdir(static_path):
    os.mkdir(static_path)

meme = MemeEngine(static_path)


def setup():
    """ Load all resources """

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

    images_path = "./_data/photos/dog/"

    imgs = []
    for root, dirs, files in os.walk(images_path):
        imgs = [os.path.join(root, name) for name in files]

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """

    img = choice(imgs)
    quote = choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)

    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """

    image_url = request.form.get('image_url')
    answer = requests.get(image_url, allow_redirects=True)
    tmp = f'{static_path}/{randint(0, 100000000)}.jpg'
    with open(tmp, 'wb') as outfile:
        outfile.write(answer.content)

    quote = QuoteModel(request.form.get('author'), request.form.get('body'))

    path = meme.make_meme(tmp, quote.body, quote.author)
    os.remove(tmp)

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
