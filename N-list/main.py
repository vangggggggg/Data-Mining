from collections import defaultdict
from N_list import *
from Pre_Post import *

def read_file(filename):
    with open(filename, "r") as f:
        content = f.readlines()

    dataset = defaultdict(set)


    for i in range(1, len(content)):
        id = content[i][0]
        itemset = content[i][2]
        dataset[id].add(itemset)

    ord_dataset = sorted(dataset.items(), key=lambda x: x[0])
    return dict(ord_dataset)

if __name__ == "__main__":
    try:
        filename = input("Please Enter File Name: ")
        dataset = read_file(filename)
        minsub = float(input("Please Enter Minimum Support(% ex:0.5): "))
        sub = int(len(dataset) * minsub)
        final_result = []
        orderditemset = countFrequent(dataset, sub)
        PPC = createPPCtree(dataset, sub, orderditemset)
        PP_code = defaultdict(list)
        PreandPost(PPC, PP_code)
        root_PrePost = rootPP(PP_code)
        items = get_keys_dict(root_PrePost.Pointer)
        createPrePost(PP_code, root_PrePost, sub, [], items)
        print("\nVisual tree")
        clientPrePost(root_PrePost, final_result)
        print("\nAll frequent :", final_result[1:])
    except Exception:
        print("ERROR")
