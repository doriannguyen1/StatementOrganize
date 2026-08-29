import Reader
import os
def main():
    Mainreader = Reader.Reader()
    input_folder = 'input'
    for filename in os.listdir(input_folder):
        if filename.endswith('.csv') or filename.endswith('.CSV'):
            print(f"Processing file: {filename}")
            Mainreader.read(filename)
main()
