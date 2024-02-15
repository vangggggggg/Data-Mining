from FP_tree import *
from FP_growth import *
from collections import defaultdict

def read_file(filename):
    with open(filename, "r") as f:
        content = f.readlines()

    dataset = defaultdict(list)
    for i in range(1, len(content)):
        tid = content[i][0]
        itemset = int(content[i][2])
        dataset[tid].append(itemset)
    return dataset

if __name__ == "__main__":

    try:
        filename = input("Please Enter File Name: ")
        dataset = read_file(filename)
        minsub = int(input("Please Enter Minimum Support: "))
        orderitem, tmplist = countFrequent(minsub, dataset)
        FPtree, HeaderTable = createFPtree(dataset, minsub, orderitem)
        frequentitem = {}
        print(HeaderTable)
        FP_growth(HeaderTable, minsub)
        # sortdict = []
        # all_frequent = set()
        # frequent_patterns = {}
        # tmpList = defaultdict(list)
        # find_nodeLink(HeaderTable[4][1], tmpList, 0, minsub, frequent_patterns)
        # sortdict = zip_pattern(minsub, frequent_patterns)
        # generate_all_subsets(sortdict, 4, all_frequent)
        # print(len(all_frequent))
        # print(all_frequent)
    except Exception:
        print("ERROR")