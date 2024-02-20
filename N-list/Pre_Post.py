from collections import defaultdict

class Pre_Post:
    def __init__(self, itemName, tidSets):
        self.Item = tuple(itemName)
        self.TidSet = tidSets
        self.Pointer = {}

def clientPrePost(root, final_result):
    print(root.Item, root.TidSet)
    final_result.append(root.Item)
    for key, values in root.Pointer.items():
        clientPrePost(values, final_result)

def rootPP(tidSet):

    root = Pre_Post("Root", "NULL")

    for key, tidSet in tidSet.items():
        tmpRoot = Pre_Post(key, tidSet)
        root.Pointer[key] = tmpRoot

    return root

def get_keys_dict(dict):

    setDict = [key for key, value in dict.items()]

    return setDict

def convert_set(PP_code):
    result = {}
    for item in PP_code:
      result[tuple(item[:2])] = result.get(tuple(item[:2]), 0) + item[2]

    new_dict = [(key[0], key[1], value) for key, value in result.items()]
    return new_dict

def sum_count(PP_code):
    total = sum(t[2] for t in PP_code)

    return total

def createPrePost(firstroot, root, minsub, dicarditem, items):

    for key, values in root.Pointer.items():
        if key in items:
            items.remove(key)
        if items is None:
            return
        for x in items:
            save = list()
            if x not in dicarditem:
                for c in firstroot[x]:
                    for d in values.TidSet:
                        if d[0] > c[0] and d[1] < c[1]:
                            save.append(tuple([c[0], c[1], d[2]]))
                    result = convert_set(save)
                    if sum_count(save) >= minsub:
                        tid = key + x
                        newNode = Pre_Post(tid, result)
                        values.Pointer[tid] = newNode
                    else:
                        dicarditem.append(x)
        createPrePost(firstroot, values, minsub, dicarditem, items)
        dicarditem = []
