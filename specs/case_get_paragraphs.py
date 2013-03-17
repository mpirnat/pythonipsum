import konira
import pythonipsum

describe "get_paragraph":

    it "will return a single paragraph from the data fixture":
        assert pythonipsum.get_paragraph()

describe "get_paragraphs":

    it "will return a list of paragraphs from the data fixture":
        assert pythonipsum.get_paragraphs(1)
