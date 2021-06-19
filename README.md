# Meme Generator - Capstone project

This should serve as proof of aquired knowledge, after completion of the module "Large Codebases with Libraries" - the last unit of the [Intermediate Python Nanodegree Program](https://www.udacity.com/course/intermediate-python-nanodegree--nd303) offered by **Udacity**.

This project's aim is building a _naive_ "meme generator" – a multimedia application to dynamically generate _memes_ - that is images with an overlaid quote. 

This project serves as a hands-on opportunity to practice what I've learned in this course, such as:

* Object-oriented thinking in Python, including abstract classes, class methods, and static methods.
* DRY (don’t repeat yourself) principles of class and method design.
* Working with modules and packages in Python.

## The application's functional overview
The code in the `QuoteEngine` and `MemeGenerator` modules should:
* Interact with a variety of complex filetypes. This emulates the kind of data you’ll encounter in a data engineering role.
* Load quotes from a variety of filetypes (PDF, Word Documents, CSVs, Text files).
* Load, manipulate, and save images.
* Accept dynamic user input through a command-line tool and a web service. 
This emulates the kind of work I might encounter as a full stack developer/data engineer.

I'll make sure to demonstrate coding best practices for style and documentation by having my code, docstrings, and comments adhere to [PEP 8](https://www.python.org/dev/peps/pep-0008/) Standards.


## Setup instructions

Please shallow clone the repository (quicker and space efficient):

```
git clone --depth 1 https://github.com/robocioaca/udacity_meme-generator-project.git
```

I've developed and tested my code on a Linux machine, running `Python 3.9.5`. YMMV. Please create a virtual environment and load the specified [requirements](requirements.txt):

```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Module overview

### The **Quote Engine** module

The `QuoteEngine` module is responsible for ingesting many types of files that contain quotes. This module will be composed of many classes and will demonstrate my understanding of complex inheritance, abstract classes, classmethods, strategy objects and other fundamental programming principles.

`QuoteModel` class: a quote contains a body and an author. Example quotes are provided in a variety of files. Take a moment to review the file formats in `./_data/SimpleLines` and `./_data/DogQuotes`. I'll  design a system to extract each quote line-by-line from these files.

`IngestorInterface` is an abstract base class, it defines two methods with the following class method signatures:

```
def can_ingest(cls, path: str) -> boolean
def parse(cls, path: str) -> List[QuoteModel]
```

Separate strategy objects will realize `IngestorInterface` for each file type (csv, docx, pdf, txt): `CSVIngestor, DocxIngestor, PDFIngestor, TextIngestor`. These concrete startegy objects rely on functionality provided by the `pandas`, `python-docx` modules and the external `pdftotext` executable.

A final `Ingestor` class will realize the `IngestorInterface` abstract base class and encapsulate your helper classes. It implements logic to flexibly select the appropriate helper for a given file based on filetype.

### The **Meme Engine** Module

The `MemeGenerator` Module is responsible for manipulating and drawing text onto images. It reinforces my understanding of object-oriented thinking while demonstrating my skill using a more advanced third party library for image manipulation.

The image processing is handled by the `Pillow` module.

## Packaging my Application

Larger, complex systems need an interface for users to interact with. I'll package the project as a command line tool and as a simple web service.

### A Command-Line Interface tool (CLI)
The project contains a simple cli app starter code in `meme.py`. The utility can be run from the terminal by invoking `python meme.py` and relies on the `argparse` module.

The script takes three optional CLI arguments:

* `--body` a string quote body
* `--author` a string quote author
* `--path` an image path

The script returns a relative path to a generated image. If any argument is not defined, a random selection is used.

###  A simple Flask web service
The project contains a barebones [Flask](https://flask.palletsprojects.com/en/2.0.x/) app code in `app.py`. 

The app uses the `QuoteEngine` and `MemeGenerator` Modules to generate a random captioned image.

It uses the `requests` package to fetch an image from a user submitted URL.

## License

The content of this repository is licensed under a
[MIT License](LICENSE)