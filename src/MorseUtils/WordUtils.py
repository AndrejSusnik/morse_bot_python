from MorseUtils import MorseUtils
import nltk
from nltk.corpus import udhr, udhr2
import random

nltk.download('udhr')
nltk.download('udhr2')


class WordUtils:
    @staticmethod
    def get_words(n: int) -> list[str]:
        words = udhr.words('Slovenian_Slovenscina-Latin2')
        words2 = udhr2.words('slv.txt')

        # combine both lists and remove stopwords
        all_words = sorted(words+words2)

        # remove punctuation
        all_words = [word for word in all_words if word.isalpha()]

        return random.sample(all_words, n)

    @staticmethod
    def get_morse_words(n: int) -> list[str]:
        words = WordUtils.get_words(n)
        return [MorseUtils.MorseUtils.encode(word) for word in words]


def test_get_0_words():
    words = WordUtils.get_words(0)
    assert len(words) == 0


def test_get_1_word():
    words = WordUtils.get_words(1)
    assert len(words) == 1


def test_get_10_words():
    words = WordUtils.get_words(10)
    assert len(words) == 10


def test_get_0_morse_words():
    words = WordUtils.get_morse_words(0)
    assert len(words) == 0


def test_get_1_morse_word():
    words = WordUtils.get_morse_words(1)
    print(words)
    assert len(words) == 1
