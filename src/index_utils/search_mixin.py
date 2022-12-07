import pickle as pkl
import os
import nltk


class QuerryMixin:
    AND = ("&", "&&", "and")
    OR = ("|", "||", "or")
    NOT = ("NOT", "-")

    def decompose_query(self, query):
        query_list_and = query.split(
            "/[{0}|{1}|{2}]/".format(self.AND[0], self.AND[1], self.AND[2])
        )
        query_list_or = query.split(
            "/[{0}|{1}|{2}]/".format(self.OR[0], self.OR[1], self.OR[2])
        )
        query_list_not = query.split("/[{0}|{1}]/".format(self.NOT[0], self.NOT[1]))

        return [query_list_and, query_list_or, query_list_not]

    def __init__(self, query: str):
        self.query = query
        self.query_ops = self.decompose_query(self.query)
        self.tokens = nltk.word_tokenize(self.query)
        print(self.tokens)


class SearchMixin:
    def check_file(self, file_path: str):
        if not os.path.isfile(file_path):
            raise FileExistsError("File doesn't exist!")
        else:
            return True

    def __init__(self, file_path: str, query: QuerryMixin):
        self.index = (
            pkl.load(open(file_path, "rb")) if self.check_file(file_path) else None
        )
        self.query = query
        print(self.index)
