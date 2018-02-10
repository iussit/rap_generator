import random


class Markov(object):
    def __init__(self, file_path):
        with open(file_path) as open_file:
            open_file.seek(0)
            text = open_file.read()
            self.words = text.split()

        self.word_size = len(self.words)

        def triples():
            if len(self.words) < 3:
                return

            for i in range(len(self.words) - 2):
                yield (self.words[i], self.words[i + 1], self.words[i + 2])

        self.dictionary = {}
        for w1, w2, w3 in triples():
            key = (w1, w2)
            if key in self.dictionary:
                self.dictionary[key].append(w3)
            else:
                self.dictionary[key] = [w3]

    def generate_text(self, text_length=25):
        seed = random.randint(0, abs(self.word_size - 3))
        seed_word, next_word = self.words[seed], self.words[seed + 1]
        w1, w2 = seed_word, next_word
        gen_words = []
        for i in range(text_length):
            gen_words.append(w1)
            w1, w2 = w2, random.choice(self.dictionary[(w1, w2)])
        gen_words.append(w2)
        return ' '.join(gen_words)
