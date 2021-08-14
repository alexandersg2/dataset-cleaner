import pandas
from pandas import DataFrame


class TweetLoader:
    SENTIMENT_COL = 0
    CONTENT_COL = 5

    @classmethod
    def load(cls, path: str) -> DataFrame:
        return pandas.read_csv(
            path,
            usecols=[cls.SENTIMENT_COL, cls.CONTENT_COL],
            encoding='ISO-8859-1',
        )
