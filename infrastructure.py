import os
from collections import namedtuple

import database
from markov import Markov

Lyric = namedtuple('Lyric', ['id', 'text', 'rating', 'datetime'])

file_path = os.path.join(os.path.dirname(__file__), 'static', 'text', 'all_sample.txt')
markov = Markov(file_path)


def generate_lyric(text_length=25):
    lyric = database.Lyric(markov.generate_text(text_length))
    lyric.create()


def rating_lyric(lyric_id, rating_diff):
    lyric = database.lyric(lyric_id)
    lyric.rating += rating_diff
    lyric.save_changes()


def get_lyrics():
    def capitalize_text(text):
        return text.capitalize()

    for lyric in database.lyrics()[::-1]:
        text = '.'.join(map(capitalize_text, lyric.text.split('.')))
        yield Lyric(lyric.id, text.split('\n'), lyric.rating, lyric.datetime.strftime("%Y-%m-%d %H:%M:%S"))
