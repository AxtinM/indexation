from pathlib import Path
from nltk import regexp_tokenize


class IndexUtil:
    def file_tokenization(self, file_path: str):
        with open(Path(str(self.utils.absolute()) + "/" + file_path), "r") as f:
            words = regexp_tokenize(f.read(), pattern="[A-Za-z]+")
            for word in words:
                if word in self.doc:
                    self.doc[word].append(file_path.replace("\n", ""))
                else:
                    self.doc.update({word: [file_path.replace("\n", "")]})

    def make_index(self):
        try:
            file = open(self.list_file_path, "r")
            list_file = file.read().split("\n")[:-1]
            try:
                for file_path in list_file:
                    self.file_tokenization(file_path)
            except:
                print("something went wrong when writing to file")

            finally:
                file.close()
        except:
            print("Something went wrong when opening file")

    def __init__(self, utils: str):
        self.utils = Path(utils)
        self.list_file_path = Path(str(self.utils.absolute()) + "/collection.lst")
        self.doc: dict = {}
        self.make_index()
