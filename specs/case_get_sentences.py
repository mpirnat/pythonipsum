import konira
import pythonipsum

describe "get_sentence":

    it "will return a single sentence from the data fixture":
        assert pythonipsum.get_sentence()

describe "get_sentences":

    it "will return a list of sentences from the data fixture":
        assert pythonipsum.get_sentences(1)
