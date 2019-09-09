from ex48 import Lexicon

class ParseError(Exception):
    pass

class SentenceB(object):
    def __init__(self, subject, verb, object):
        # each input is a tuple of (type, word)
        self.subject = subject[1]
        self.verb = verb[1]
        self.object = object[1]

def parse_sentence(word_list):
    types = [('noun',), ('verb',), ('noun', 'direction')]
    sentence = []
    while word_list and types:
        next_word = word_list.pop(0)
        if next_word[0] != 'stop':
            nextType = types.pop(0)
            if next_word[0] in nextType:
                sentence.append(next_word)
            elif nextType == ('noun',) and next_word[0] == 'verb':
                # expect subject but does not get a noun, will assume subject as player
                sentence.append(('noun', 'player'))
                sentence.append(next_word)
                types.pop(0)
            else:
                raise ParseError("Expect type %s but got %s" % (list(nextType), next_word[0]))
    return SentenceB(sentence[0], sentence[1], sentence[2])

if __name__ == '__main__':
    lexicon = Lexicon()
    mySentence = parse_sentence(lexicon.scan("bear go west"))
    print(mySentence.subject, mySentence.verb, mySentence.object)