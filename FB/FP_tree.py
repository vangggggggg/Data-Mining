from collections import defaultdict

class Node:
    length_FBtree = 0
    def __init__(self, counter, item_name, parentNode):
        self.count = counter
        self.itemName = item_name
        self.parent = parentNode
        self.children = {}
        self.nodeLink = None

    def increamet(self):
        self.count += 1
    def display_tree_list(self):
        print(self.itemName, self.count, end='')
        if len(self.children) > 0:
            print(",[", end='')
        for c in self.children.values():
            print("[", end='')
            c.display_tree_list()
            if len(c.children) == 0:
                print("]", end='')
        print("]", end='')

    def isSinglePath(self, FPtree):
        countChilderen = len(self.children)
        if countChilderen > 1:
            return False
        elif countChilderen == 0:
            return True
        else:
            return True and self.isSinglePath(FPtree.childeren[0])
def countFrequent(min_sub, dataset):
    HeaderTable = {}
    for key, values in dataset.items():
        for item in values:
            HeaderTable[item] = HeaderTable.get(item, 0) + 1

    sorted_item = sorted([items for items in HeaderTable.items()], key=lambda x: x[1], reverse=True)

    frequent_itemset = [item[0] for item in sorted_item]

    #frequent_itemset = set(HeaderTable.keys())

    return frequent_itemset, dict(sorted_item)

def createFPtree(dataset, minsub, orderditemset):
    frequent_itemset, HeaderTable = countFrequent(minsub, dataset)
    if len(frequent_itemset) == 0:
        return None, None

    for k in HeaderTable:
        HeaderTable[k] = [HeaderTable[k], None]
    FPTree = Node(1,   "NULL Root", None)

    for key, values in dataset.items():
        orderd_itemset = sort_by_priority_list(values, orderditemset)
        InsertorUpdate(orderd_itemset, FPTree, HeaderTable)

    return FPTree, HeaderTable

#Find pointer at the end of nodelink

def InsertorUpdate(itemset, treeNode, headerTable):
    if itemset[0] in treeNode.children:
        treeNode.children[itemset[0]].increamet()
    else:
        treeNode.children[itemset[0]] = Node(1, itemset[0], treeNode)
        if headerTable[itemset[0]][1] is None:
            headerTable[itemset[0]][1] = treeNode.children[itemset[0]]
        else:
            update_NodeLink(headerTable[itemset[0]][1], treeNode.children[itemset[0]])

    if len(itemset) > 1:
        InsertorUpdate(itemset[1::], treeNode.children[itemset[0]], headerTable)

def sort_by_priority_list(values, priority):

    if len(values) == 1:
        return values
    else:
        priority_dict = {k: i for i, k in enumerate(priority)}

        def priority_getter(value):
            return priority_dict.get(value, len(values))

        priority_sort = sorted(values, key=priority_getter)
        x = 0
        lens_priority = len(priority) - 1
        lens_orderd = len(priority_sort) - 1

        if lens_priority < lens_orderd:
            for i in range(0, lens_priority):
                if priority_sort[lens_priority - i] in priority:
                    x = lens_priority - i + 1
                    return priority_sort[:x]
        else:
            for i in range(0, lens_orderd):
                if priority_sort[lens_orderd - i] in priority:
                    x = lens_orderd - i + 1
                    return priority_sort[:x]

def update_NodeLink(nodeTmp , nodeTarget):
    while nodeTmp.nodeLink is not None:
        nodeTmp = nodeTmp.nodeLink

    nodeTmp.nodeLink = nodeTarget

def go_back_FPtree(leaf_Node):
    prefixNode = []

    if leaf_Node is None:
        return None
    leaf_Node = leaf_Node.parent

    while leaf_Node.parent is not None:
        prefixNode.append(leaf_Node.itemName)
        leaf_Node = leaf_Node.parent

    return prefixNode

def zip_pattern(minsub, datatmp):
    dict_scan = {}

    for key, values in datatmp.items():
        for x in key:
            dict_scan[x] = dict_scan.get(x, 0) + values

    sorted_item = sorted([items for items in dict_scan.items() if items[1] >= minsub], key=lambda x: x[1], reverse=True)
    sorted_dict = [item[0] for item in sorted_item]

    return sorted_dict

def find_nodeLink(address, pattern, count, minsub, frequentItem):
    tmpList = go_back_FPtree(address)

    if tmpList != None and address.parent.parent is not None:
        count += 1
        pattern[count].extend(tmpList)
        tmpTuple = tuple(tmpList)
        frequentItem[tmpTuple] = address.count

    if tmpList is not None and address.nodeLink is not None:
        address = address.nodeLink
        find_nodeLink(address, pattern, count, minsub, frequentItem)

def generate_all_subsets(arr, value, all_frequent):
    for i in range(1, 1 << len(arr)):
        subset = []
        for j in range(len(arr)):
            if (i >> j) % 2 == 1:
                subset.append(arr[j])
        all_frequent.add(tuple(subset+[value]))
    all_frequent.add(tuple([value]))

if __name__ == "__main__":
    pass