import re
import string
import html

import contractions
import emoji


class TweetCleaner:
    MENTION_REGEX = re.compile(r'@\w+\s')
    URL_REGEX = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    AMPERSAND_REGEX = re.compile(r'& ')

    @classmethod
    def _remove_mentions(cls, text: str) -> str:
        return re.sub(cls.MENTION_REGEX, '', text)

    @classmethod
    def _remove_links(cls, text: str) -> str:
        return re.sub(cls.URL_REGEX, '', text)

    @classmethod
    def _expand_contractions(cls, text: str) -> str:
        text = re.sub(cls.AMPERSAND_REGEX, 'and ', text)
        return ' '.join((contractions.fix(word) for word in text.split()))

    @staticmethod
    def _remove_punctuation(text: str) -> str:
        return text.translate(str.maketrans('', '', string.punctuation))

    @staticmethod
    def _remove_emojis(text: str) -> str:
        return emoji.demojize(text, delimiters=("", ""))

    @staticmethod
    def _remove_html_entities(text: str) -> str:
        return html.unescape(text)

    @classmethod
    def clean(cls, text: str) -> str:
        text = cls._remove_html_entities(text)
        text = cls._remove_mentions(text)
        text = cls._remove_links(text)
        text = cls._remove_emojis(text)
        text = cls._expand_contractions(text)
        text = cls._remove_punctuation(text)
        text = text.lower()

        return text
