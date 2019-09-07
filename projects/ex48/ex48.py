class Lexicon(object):

    def __init__(self):
        self.dic = {
                'north': 'direction',
                'south': 'direction',
                'east': 'direction',
                'west': 'direction',
                'down': 'direction',
                'up': 'direction',
                'left': 'direction',
                'right': 'direction',
                'the': 'stop',
                'in': 'stop',
                'of': 'stop',
                'from': 'stop',
                'at': 'stop',
                'go': 'verb',
                'love': 'verb',
                'eat': 'verb',
                'door': 'noun',
                'bear': 'noun',
                'princess': 'noun',
                'cabinet': 'noun',
            }

    def dispose(self):
        self.dic = None

    def scan(self, input):
        result = []
        words = input.split()
        for word in words:
            type = 'number'
            try:
                num = int(word)
                result.append((type,num))
            except ValueError:
                type = self.dic.get(word, 'error')
                result.append((type, word))
        return result
