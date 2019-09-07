from ex48 import Lexicon
import unittest

class LexiconTest(unittest.TestCase):
    def setUp(self):
        self.lexicon = Lexicon()

    def tearDown(self):
        self.lexicon.dispose()

    def test_directions(self):
        # lexicon = Lexicon()
        self.assertEqual(self.lexicon.scan("north"), [('direction', 'north')])
        result = self.lexicon.scan("north south east")
        self.assertEqual(result, [('direction', 'north'),
                              ('direction', 'south'),
                              ('direction', 'east')])
        
    def test_verbs(self):
        # lexicon = Lexicon()
        self.assertEqual(self.lexicon.scan("go"), [('verb', 'go')])
        result = self.lexicon.scan("go love eat")
        self.assertEqual(result, [('verb', 'go'),
                              ('verb', 'love'),
                              ('verb', 'eat')])
        
    def test_stops(self):
        # lexicon = Lexicon()
        self.assertEqual(self.lexicon.scan("the"), [('stop', 'the')])
        result = self.lexicon.scan("the in of")
        self.assertEqual(result, [('stop', 'the'),
                              ('stop', 'in'),
                              ('stop', 'of')])
        
    def test_numbers(self):
        # lexicon = Lexicon()
        self.assertEqual(self.lexicon.scan("1234"), [('number', 1234)])
        result = self.lexicon.scan("3 91234")
        self.assertEqual(result, [('number', 3),
                              ('number', 91234)])
        
    def test_nouns(self):
        # lexicon = Lexicon()
        self.assertEqual(self.lexicon.scan("bear"), [('noun', 'bear')])
        result = self.lexicon.scan("bear princess")
        self.assertEqual(result, [('noun', 'bear'),
                              ('noun', 'princess')])
    
    def test_all(self):
        # lexicon = Lexicon()
        self.assertEqual(self.lexicon.scan("notRecognized"), [('error', 'notRecognized')])
        result = self.lexicon.scan("north notRecognized the south 1234 bear something in love")
        self.assertEqual(result, [('direction', 'north'),
                              ('error', 'notRecognized'),
                              ('stop', 'the'),
                              ('direction', 'south'),
                              ('number', 1234),
                              ('noun', 'bear'),
                              ('error', 'something'),
                              ('stop', 'in'),
                              ('verb', 'love')])


if __name__ == '__main__':
    unittest.main()
