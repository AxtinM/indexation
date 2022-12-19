from pathlib import Path
from nltk import regexp_tokenize


class IndexUtil:
    """
    Inverted documents index based on file path of a directory containing a .lst file and
    a list of documents containing words.
    """
    def file_tokenization(self, file_path: str):
        with open(Path(str(self.utils.absolute()) + "/" + file_path), "r") as f:
            # tokenize words in each file
            words = regexp_tokenize(f.read(), pattern="[A-Za-z]+")
            for word in words:
                word = word.lower()
                file_name = file_path.replace("\n", "")
                # update doc with word : file1, file2, ...
                if word in self.doc:
                    if file_name in self.doc[word]:
                        continue
                    self.doc[word].append(file_name)
                else:
                    self.doc.update({word: [file_name]})

    def make_index(self):
        """ open .lst file and run file_tokenization() on each file. """
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