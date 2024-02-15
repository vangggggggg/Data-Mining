class ITtree:
    def __init__(self, itemName, tidSets):
        self.Item = tuple(itemName)
        self.TidSet = tidSets
        self.Pointer = {}

def clientITTree(root):
    print(root.Item, root.TidSet)
    for key, values in root.Pointer.items():
        clientITTree(values)
def rootITtree(id, tidSet):

    root = ITtree("{}", id)

    for key, tidSet in tidSet.items():
        tmpRoot = ITtree(key, tidSet)
        root.Pointer[key] = tmpRoot

    return root

def get_keys_dict(dict):

    setDict = {key for key, value in dict.items()}

    return list(setDict)

def createITtree(firstroot, root, minsub, dicarditem, items):

    for key, values in root.Pointer.items():
        if key in items:
            items.remove(key)
        if items is None:
            return
        for x in items:

            if x in dicarditem:
                break
            if x[0] in key:
                break

            tid = key + x
            iter = values.TidSet.intersection(firstroot.Pointer[x].TidSet)

            if len(iter) > len(values.TidSet)/minsub:
                newNode = ITtree(tid, iter)
                values.Pointer[tid] = newNode
            else:
                dicarditem.append(x)

        createITtree(firstroot, values, minsub, dicarditem, items)
        dicarditem = []

if __name__ == "__main__":
   x = (2, 1)
   y = (2,)
   if y[0] in x:
       print("YES")
   else:
       print("NO")
