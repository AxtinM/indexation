import sys
from utils import QueryMixin, SearchInvertedIndex

if __name__ == "__main__":
    # arg_1 -> query
    arg_1 = sys.argv[1]

    search_obj = SearchInvertedIndex("./pickle.pkl", arg_1)
    print(search_obj.search_index())
