from FP_tree import *
from collections import defaultdict
def FP_growth(HeaderTable, minsub):
    all_frequent = set()
    for key, values in reversed(HeaderTable.items()):
        sortdict = []
        frequent_patterns = {}
        tmpList = defaultdict(list)
        find_nodeLink(values[1], tmpList, 0, minsub, frequent_patterns)
        sortdict = zip_pattern(minsub, frequent_patterns)
        generate_all_subsets(sortdict, key, all_frequent)
    print(all_frequent)
    print(len(all_frequent))
if __name__ == "__main__":
    pass
