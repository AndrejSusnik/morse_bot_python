MorseToAlpha = {
    '.-': 'A',
    '-...': 'B',
    '-.-.': 'C',
    '-..': 'D',
    '.': 'E',
    '..-.': 'F',
    '--.': 'G',
    '....': 'H',
    '..': 'I',
    '.---': 'J',
    '-.-': 'K',
    '.-..': 'L',
    '--': 'M',
    '-.': 'N',
    '---': 'O',
    '.--.': 'P',
    '--.-': 'Q',
    '.-.': 'R',
    '...': 'S',
    '-': 'T',
    '..-': 'U',
    '...-': 'V',
    '.--': 'W',
    '-..-': 'X',
    '-.--': 'Y',
    '--..': 'Z',
    '-----': '0',
    '.----': '1',
    '..---': '2',
    '...--': '3',
    '....-': '4',
    '.....': '5',
    '-....': '6',
    '--...': '7',
    '---..': '8',
    '----.': '9',
    ' ': ' '
}

AlphaToMorse = {v: k for k, v in MorseToAlpha.items()}


class InvalidCharacterError(Exception):
    pass


class InvalidMorseError(Exception):
    pass


class MorseUtils:
    @staticmethod
    def encode(message: str):
        any_invalid = any(c not in AlphaToMorse for c in message.upper())

        message = ' '.join(message.split())

        if any_invalid:
            raise InvalidCharacterError("Invalid character found in message")

        return ' '.join(map(lambda c: AlphaToMorse[c], message.upper()))

    @staticmethod
    def decode(encoded_message):
        if not encoded_message:
            return ""

        morse_chars = encoded_message.split(' ')

        any_invalid = any(c not in MorseToAlpha for c in morse_chars)

        if any_invalid:
            raise InvalidMorseError("Invalid morse code found in message")

        return ''.join(map(lambda c: MorseToAlpha[c], morse_chars))


def test_basic_encode():
    assert MorseUtils.encode(
        "Hello World") == ".... . .-.. .-.. ---   .-- --- .-. .-.. -.."


def test_encode_empty_string():
    assert MorseUtils.encode("") == ""


def test_encode_invalid_character():
    try:
        MorseUtils.encode("Hello World!")
    except InvalidCharacterError:
        assert True


def test_encode_invalid_character_2():
    try:
        MorseUtils.encode("Hello World@")
    except InvalidCharacterError:
        assert True


def test_encode_whitespaces():
    assert MorseUtils.encode(
        "Hello World") == ".... . .-.. .-.. ---   .-- --- .-. .-.. -.."


def test_encode_whitespaces_2():
    assert MorseUtils.encode(
        "Hello  World") == ".... . .-.. .-.. ---   .-- --- .-. .-.. -.."


def test_encode_whitespaces_3():
    assert MorseUtils.encode(
        "       Hello World") == ".... . .-.. .-.. ---   .-- --- .-. .-.. -.."


def test_encode_whitespaces_4():
    assert MorseUtils.encode(
        "Hello World      ") == ".... . .-.. .-.. ---   .-- --- .-. .-.. -.."


def test_basic_decode():
    assert MorseUtils.decode(
        ".... . .-.. .-.. --- .-- --- .-. .-.. -.."
    ) == ''.join("Hello World".split(' ')).upper()


def test_decode_empty_string():
    assert MorseUtils.decode("") == ""


def test_decode_invalid_morse():
    try:
        MorseUtils.decode(".... . .-.. .-.. ---   .-- --- .-. .-.. -.. !")
    except InvalidMorseError:
        assert True


def test_decode_invalid_morse_2():
    try:
        MorseUtils.decode(".... . .-.. .-.. ---   .-- --- .-. .-.. -.. @")
    except InvalidMorseError:
        assert True


def test_decode_invalid_morse_3():
    try:
        MorseUtils.decode(".... . .-.. .-.. ---   .-- --- .-. .-.. -..  ")
    except InvalidMorseError:
        assert True


def test_decode_invalid_morse_4():
    try:
        MorseUtils.decode(".... . .-.. .-.. ---   .-- --- .-. .-.. -..  ")
    except InvalidMorseError:
        assert True
