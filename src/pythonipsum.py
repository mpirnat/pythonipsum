from loremipsum import Generator

sample = file('data/sample.txt').read()
dictionary = file('data/dictionary.txt').read().split('\n')
g = Generator(sample, dictionary)


def get_sentence():
    return list(g.generate_sentences(1))[-1][-1]


def get_sentences(amount):
    return [x[-1] for x in g.generate_sentences(amount)]


def get_paragraph():
    return list(g.generate_paragraphs(1))[-1][-1]


def get_paragraphs(amount):
    return [x[-1] for x in g.generate_paragraphs(amount)]


if __name__ == '__main__':
    print("Sentence: %s" % get_sentence())
    print("Sentences: %s" % get_sentences(5))
    print("Paragraph: %s" % get_paragraph())
    print("Paragraphs: %s" % get_paragraphs(5))
