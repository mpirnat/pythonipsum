import os
from loremipsum import Generator


PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

sample = file(PROJECT_ROOT+'/data/sample.txt').read()
dictionary = file(PROJECT_ROOT+'/data/dictionary.txt').read().split('\n')
ipsum_generator = Generator(sample, dictionary)


def get_sentence():
    return list(ipsum_generator.generate_sentences(1))[-1][-1]


def get_sentences(amount):
    return [x[-1] for x in ipsum_generator.generate_sentences(amount)]


def get_paragraph():
    return list(ipsum_generator.generate_paragraphs(1))[-1][-1]


def get_paragraphs(amount):
    return [x[-1] for x in ipsum_generator.generate_paragraphs(amount)]


if __name__ == '__main__':
    print("Sentence: %s" % get_sentence())
    print("Sentences: %s" % get_sentences(5))
    print("Paragraph: %s" % get_paragraph())
    print("Paragraphs: %s" % get_paragraphs(5))
