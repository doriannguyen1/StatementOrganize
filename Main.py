import os
from utils.Reader import Reader


def main():
    main_reader = Reader()
    input_folder = 'input'
    for filename in os.listdir(input_folder):
        if filename.endswith('.csv') or filename.endswith('.CSV'):
            print(f"Processing file: {filename}")
            main_reader.read(filename)


if __name__ == "__main__":
    main()
