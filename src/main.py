import sys
from index_utils.search_mixin import QuerryMixin, SearchMixin


if __name__ == "__main__":
    arg_1 = sys.argv[1]

    query = QuerryMixin(arg_1)
    search_obj = SearchMixin("./pickle.pkl", query)
