from ex49b import *
from ex48 import Lexicon
import unittest

class ParserTest(unittest.TestCase):
    def setUp(self):
        self.lexicon = Lexicon()

    def tearDown(self):
        self.lexicon.dispose()

    def convert(self, input):
        sentence = parse_sentence(self.lexicon.scan(input))
        return '%s %s %s' % (sentence.subject, sentence.verb, sentence.object)

    def test_simpleThreeTypes(self):
        self.assertEqual(self.convert('door go west'), 'door go west', 'test #1: noun verb direction')
        self.assertEqual(self.convert('bear love cabinet'), 'bear love cabinet', 'test #2: noun verb noun')
        with self.assertRaises(ParseError):
            self.convert('1234 bear go')

    def test_simpleTwoTypes(self):
        self.assertEqual(self.convert('go west'), 'player go west', 'test #3: verb direction')
        self.assertEqual(self.convert('love cabinet'), 'player love cabinet', 'test #4: verb noun')
        with self.assertRaises(ParseError):
            self.convert('1234 cabinet')

    def test_typeRepeats(self):
        with self.assertRaises(ParseError):
            self.convert('go love')
        with self.assertRaises(ParseError):
            self.convert('bear princess')
        with self.assertRaises(ParseError):
            self.convert('door west go')

    def test_stopSimpleThreeTypes(self):
        self.assertEqual(self.convert('the bear go west'), 'bear go west')
        self.assertEqual(self.convert('in the from bear go cabinet'), 'bear go cabinet')
        with self.assertRaises(ParseError):
            self.convert('in the from 1234 bear go')

    def test_twoStopsSimpleThreeTypes(self):
        self.assertEqual(self.convert('from the bear go of west'), 'bear go west')
        self.assertEqual(self.convert('in the from bear of at go cabinet'), 'bear go cabinet')
        with self.assertRaises(ParseError):
            self.convert('in the from 1234 the bear go')

    def test_threeStopsSimpleThreeTypes(self):
        self.assertEqual(self.convert('from the bear go of west at in'), 'bear go west')
        self.assertEqual(self.convert('in the from bear of at go cabinet at in'), 'bear go cabinet')
        with self.assertRaises(ParseError):
            self.convert('in the from 1234 the bear go at in')

    def test_wordsAfterStopsThreeTypes(self):
        self.assertEqual(self.convert('the bear from the go in the west at the princess love cabinet'), 'bear go west')
        self.assertEqual(self.convert('the bear from the love in the cabinet at the princess love cabinet'),
                         'bear love cabinet')
        with self.assertRaises(ParseError):
            self.convert('the bear from the 1234 in the cabinet at the princess love cabinet')

    def test_stopSimpleTwoTypes(self):
        self.assertEqual(self.convert('from the go west'), 'player go west')
        self.assertEqual(self.convert('from the love cabinet'), 'player love cabinet')
        with self.assertRaises(ParseError):
            self.convert('from the 1234 cabinet')

    def test_twoStopsSimpleTwoTypes(self):
        self.assertEqual(self.convert('from the go in the west'), 'player go west')
        self.assertEqual(self.convert('from the love in the cabinet'), 'player love cabinet')
        with self.assertRaises(ParseError):
            self.convert('from the 1234 in the cabinet')

    def test_threeStopsSimpleTwoTypes(self):
        self.assertEqual(self.convert('from the go in the west at the'), 'player go west')
        self.assertEqual(self.convert('from the love in the cabinet at the'), 'player love cabinet')
        with self.assertRaises(ParseError):
            self.convert('from the 1234 in the cabinet at the')

    def test_wordsAfterStopsTwoTypes(self):
        self.assertEqual(self.convert('from the go in the west at the princess love cabinet'), 'player go west')
        self.assertEqual(self.convert('from the love in the cabinet at the princess love cabinet'), 'player love cabinet')
        with self.assertRaises(ParseError):
            self.convert('from the 1234 in the cabinet at the princess love cabinet')

if __name__ == '__main__':
    unittest.main()
        
        