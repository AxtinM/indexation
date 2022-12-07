import os
import sys
from index_utils import IndexUtil
import pickle

def check_arg(arg_1: str):
    file_path = os.path.isdir(arg_1)
    return file_path


if __name__ == "__main__":
    arg_1 = sys.argv[1]
    arg_2 = sys.argv[2]
    while not check_arg(arg_1):
        print("Please provide apropriate arguments")
        arg_1 = input("Provide directory path : ")

    index = IndexUtil(arg_1)

    print(f"{len(index.doc.keys())} WORDS \n")
    with open("./pickle.pkl", "wb") as pkl:
        pickle.dump(index.doc, pkl)


