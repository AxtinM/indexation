import pickle as pkl
import os
import nltk


class QueryMixin:
    AND = ("&", "&&", "and")
    OR = ("|", "||", "or")
    NOT = ("not", "-")

    def decompose_query(self, query):
        if self.tokens[0] in self.AND or self.tokens[0] in self.OR or self.tokens[0] in self.NOT:
            raise Exception("Wrong query format")

        result = []

        for item in self.tokens:
            if item in self.AND or item in self.OR or item in self.NOT:
                pass
            

    def __init__(self, query: str):
        self.query = query.lower()
        self.tokens = nltk.word_tokenize(self.query)
        self.query_ops = self.decompose_query(self.query)
        print(self.tokens)


class SearchMixin:
    def check_file(self, file_path: str):
        if not os.path.isfile(file_path):
            raise FileExistsError("File doesn't exist!")
        else:
            return True

    def __init__(self, file_path: str, query: QueryMixin):
        self.index = (
            pkl.load(open(file_path, "rb")) if self.check_file(file_path) else None
        )
        self.query = query
