import spacy
try:
    nlp = spacy.load('en_default')
except OSError:
    nlp = spacy.load('en')

from nltk.corpus import wordnet as wn


class Ambiguity:
    """
    class to extract ambiguity stats about a sentence
    """

    def __init__(self, text):
        self.pos_mapping = {'NOUN': 'n', 'VERB': 'v', 'ADJ': 'a', 'ADV': 'r'}
        self.text = text
        self.doc = nlp(self.text)
        self.the_polysemy_string = self.loop()

    def loop(self):
        """
        """
        polysemy_strings = []
        combinations = []
        total_ambiguity = 1

        for token_obj in self.doc:

            token = token_obj.text
            lemma = token_obj.lemma_
            pos = token_obj.pos_

            if pos in self.pos_mapping:
                wn_pos = self.pos_mapping[pos]
                polysemy = len(wn.synsets(lemma,
                                          pos=wn_pos
                                          )
                               )


                if polysemy:
                    polysemy_string = f'{token}({polysemy})'
                    polysemy_strings.append(polysemy_string)
                    combinations.append(str(polysemy))

                    total_ambiguity *= polysemy

                else:
                    polysemy_strings.append(token)
            else:
                polysemy_strings.append(token)


        combinations = ' x '.join(combinations)
        polysemy_strings.append(combinations)
        result = f'= {total_ambiguity} possible meaning combinations'
        polysemy_strings.append(result)

        return ' '.join(polysemy_strings)


if __name__ == '__main__':
    source = 'https://en.chessbase.com/post/endgame-blog-karsten-mueller-922e'
    sentence = 'The bishop pair is a powerful weapon since two bishops working together can control many squares from the distance, which is useful in both attack and defense.'
    instance = Ambiguity(sentence)
    print(instance.the_polysemy_string)
