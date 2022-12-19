import pickle as pkl
import os
import nltk



class QueryMixin:
    """
        Mixin for query provided by the user
    """
    AND = ("and", "&", "&&")
    OR = ("or", "|", "||")
    NOT = ("not", "-")

    def get_key(self, keyword: str):
        if keyword in self.AND:
            return "and"
        elif keyword in self.OR:
            return "or"
        elif keyword in self.NOT:
            return "not"
        else:
            None

    def get_query_type(self, tokens):
        for term in tokens:
            if self.get_key(term) == None:
                continue
            else:
                return self.get_key(term)

        return None


class SearchInvertedIndex(QueryMixin):
    def check_file(self, pkl_file: str):
        if not os.path.isfile(pkl_file):
            raise FileExistsError("File doesn't exist!")
        else:
            return True

    def __init__(self, file_path: str, query: str):
        self.index: {str: list} = (
            pkl.load(open(file_path, "rb")) if self.check_file(file_path) else None
        )
        self.query: str = query.lower()
        self.tokenized_query: list = nltk.word_tokenize(self.query)

    def and_search(self, list_1: list, list_2: list):
        result = []
        for doc in list_1:
            if doc in list_2:
                result.append(doc)
        return result

    def or_search(self, list_1: list, list_2: list):
        result = []
        for doc in list_1:
            result.append(doc)
        for doc in list_2:
            if not doc in result:
                result.append(doc)

        return result

    def search_index(self):
        #initialize result list
        result = []
        # get query type
        query_type = self.get_query_type(self.tokenized_query)
        if not query_type == None:
            # list of terms before keyword
            before_key = self.tokenized_query[:self.tokenized_query.index(query_type)]
            # list of terms after keyword
            after_key = self.tokenized_query[self.tokenized_query.index(query_type)+1:]
            # initialize lists to be updated with documents containing words
            before_res = []
            after_res = []

            # if else depending on key
            for term, corpus in self.index.items():
                if term in before_key:
                    # result list before query type (and, or, not)
                    before_res += corpus
                elif term in after_key:
                    # result list after query type (and, or, not)
                    after_res += corpus
                else:
                    continue
            # delegate to the right search query based on query type
            if query_type in self.AND:
                result = self.and_search(before_res, after_res)
            elif query_type in self.OR:
                result = self.or_search(before_res, after_res)

        else:
            for term in self.tokenized_query:
                if term in self.index:
                    for doc in self.index[term]: 
                        if not (doc in result):
                            result.append(doc)
        return result