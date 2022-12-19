import sys
from utils import QueryMixin, SearchMixin

if __name__ == "__main__":
    arg_1 = sys.argv[1]

    query = QueryMixin(arg_1)
    search_obj = SearchMixin("./pickle.pkl", query)
