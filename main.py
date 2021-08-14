from cleaner import DatasetCleaner
from tweet_loader import TweetLoader
from tqdm import tqdm


FILENAME = 'cleaned_dataset.txt'


def get_path():
    return input("Enter the absolute path to the dataset to be cleaned: ")


def clean_dataset(path):
    dataframe = TweetLoader.load(path)
    num_rows = len(dataframe.index)

    with open(FILENAME, 'w') as file:
        for index, row in tqdm(dataframe.iterrows(), total=num_rows):
            sentiment = row[0]
            tweet = DatasetCleaner.clean(row[1])
            file.write(f'"{sentiment}","{tweet}"\n')


if __name__ == '__main__':
    clean_dataset(get_path())
    print(f'Export complete. Find the cleaned dataset in {FILENAME}.')
