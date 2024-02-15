from collections import defaultdict

def C_scan(database, minsub, last_itemset,cant_use):
    itemset_tmp = {}
    itemset = []
    for key, values in database.items():
        for i in last_itemset:
            all_L1 = True
            for j in i:
                if j not in values:
                    all_L1 = False
                    break
            if all_L1:
                itemset_tmp[tuple(i)] = 1 + itemset_tmp.get(tuple(i), 0)
    #print(itemset_tmp)
    for key, values in itemset_tmp.items():
        if minsub > itemset_tmp[key]:
            cant_use.append(set(key))
        else:
            itemset.append(set(key))
    return cant_use, itemset

def L_applicant(database, cant_use):
    double = []
    itemset = []
    k = 0
    for i in range(0, len(database)):
        for j in range(i+1, len(database)):
            itemtmp = set()
            tmp = database[i].union(database[j])
            if len(tmp) == len(database[j]) + 1:
                itemtmp.update(tmp)
                for check in cant_use:
                    if check.issubset(itemtmp):
                        itemtmp = set()
                        double.append(itemtmp)
                        break
            if itemtmp not in double and len(itemtmp) != 0:
                itemset.append(itemtmp)
                double.append(itemtmp)

    return cant_use, itemset

if __name__ == "__main__":
    x, y = input().split()
    cant_use = []
    L = defaultdict(list)
    first_itemset = []
    double = []
    while True:
        try:
            a, b = [int(x) for x in input().split()]
        except ValueError:
            break
        L[a].append(b)
        c = set()
        c.update({b})
        if c not in double:
            first_itemset.append(c)
            double.append(c)

    minsub = int(0.5*int(x))

    itemset = first_itemset
    while True:
        cant_use, itemset = C_scan(L, minsub, itemset, cant_use)
        last_itemset = itemset
        cant_use, itemset = L_applicant(itemset, cant_use)
        if len(itemset) == 0:
            print(last_itemset)
            break

