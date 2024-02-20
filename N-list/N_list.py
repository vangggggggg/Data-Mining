class PPC:
    static_countPre = 0
    static_countPost = 0
    def __init__(self, counter, item_name, parentNode):
        self.count = counter
        self.itemName = item_name
        self.parent = parentNode
        self.children = {}
        self.nodeLink = None
        self.pre = 0
        self.post = 0

    def increamet(self):
        self.count += 1

    def display_tree_list(self):
        print(self.itemName, self.count, self.pre, self.post, end='')
        if len(self.children) > 0:
            print(",[", end='')
        for c in self.children.values():
            print("[", end='')
            c.display_tree_list()
            if len(c.children) == 0:
                print("]", end='')
        print("]", end='')

def InsertorUpdate(itemset, treeNode):
    if itemset[0] in treeNode.children:
        treeNode.children[itemset[0]].increamet()
    else:
        treeNode.children[itemset[0]] = PPC(1, itemset[0], treeNode)
    if len(itemset) > 1:
        InsertorUpdate(itemset[1::], treeNode.children[itemset[0]])

def createPPCtree(dataset, minsub, orderditemset):
    frequent_itemset = countFrequent(dataset, minsub)

    if len(frequent_itemset) == 0:
        return None, None

    PPCtree = PPC(0,   "NULL Root", None)

    for key, values in dataset.items():
        orderd_itemset = sort_by_priority_list(values, orderditemset)
        InsertorUpdate(orderd_itemset, PPCtree)

    return PPCtree
def countFrequent(dataset , minsub):
    HeaderTable = {}
    for key, values in dataset.items():
        for item in values:
            HeaderTable[item] = HeaderTable.get(item, 0) + 1

    sorted_item = sorted([items for items in HeaderTable.items() if items[1] >= minsub], key=lambda x: x[1], reverse=True)

    frequent_itemset = [item[0] for item in sorted_item]

    return frequent_itemset

def PreandPost(PPCtree, PP_code):
    PPCtree.pre = PPC.static_countPre
    PPC.static_countPre += 1

    for values in PPCtree.children.values():
        PreandPost(values, PP_code)

    PPCtree.post = PPC.static_countPost
    PPC.static_countPost += 1
    if PPCtree.pre != 0:
        PP_code[tuple(PPCtree.itemName)].extend([tuple([PPCtree.pre, PPCtree.post, PPCtree.count])])

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
