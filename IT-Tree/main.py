from collections import defaultdict
from IT_Tree import *
def read_file(filename):
    with open(filename, "r") as f:
        content = f.readlines()

    dataset = set()
    keys = defaultdict(set)

    for i in range(1, len(content)):
        tid = content[i][0]
        itemset = int(content[i][2])
        dataset.add(itemset)
        keys[tuple([tid])].add(itemset)

    return dataset, keys
if __name__ == "__main__":
   try:
        filename = input("Please Enter File Name: ")
        dataset, keys = read_file(filename)
        minsub = float(input("Please Enter Minimum Support: "))
        root = rootITtree(dataset, keys)
        items = get_keys_dict(root.Pointer)
        createITtree(root, root, minsub, [], items)
        clientITTree(root)
   except Exception:
        print("ERROR")
