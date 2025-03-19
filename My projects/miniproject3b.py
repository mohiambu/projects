
baskets = {}
with open("C://Users//M7MDA//Downloads//archive (1)//Groceries_dataset.csv", "r") as file:
    next(file)
    for i in file:
        i = i.strip().split(",")
        customer = i[0]
        item = i[2]

        if customer not in baskets:
          baskets[customer] = set()
        baskets[customer].add(item)
dataset = list(baskets.values())
dataset[:1]



def support(itemset, dataset):
    c = 0
    for i in dataset:
        if itemset.issubset(i):
            c += 1
    support = c/len(dataset)
    return support


def confidence(itemset1, itemset2, dataset):
    return support(itemset1.union(itemset2), dataset)/support(itemset1, dataset)


def lift(itemset1, itemset2, dataset):
    return confidence(itemset1, itemset2, dataset)/support(itemset2, dataset)



def pass1(dataset, min_support=0.02):
    count = {}
    f = {}
    
    # Count occurrences of each item
    for basket in dataset:
        for item in basket:
            if item in count:
                count[item] += 1
            else:
                count[item] = 1
    
    for item, cnt in count.items():
        if cnt / len(dataset) >= min_support:
            f[item] = 1  # Mark as frequent

    # Debugging output
    print("Pass 1 - Frequent items count:", len(f))
    print("Frequent items:", f)
    
    return f, count


def pass2(dataset, f, min_support=0.02):
    count = {}
    f2 = {}
    
    # Find candidate pairs only from frequent items
    for basket in dataset:
        items = sorted([item for item in basket if item in f])  # Filter only frequent items
        for idx_i, i in enumerate(items):
            for j in items[idx_i + 1:]:  # Pairs (i, j) where j > i
                if (i, j) in count:
                    count[(i, j)] += 1
                else:
                    count[(i, j)] = 1

    # Filter pairs by minimum support threshold
    for (i, j), cnt in count.items():
        if cnt / len(dataset) >= min_support:
            f2[(i, j)] = 1  # Mark as frequent

    # Debugging output
    print("Pass 2 - Frequent pairs count:", len(f2))
    print("Frequent pairs:", f2)
    
    return f2, count


def pass3(dataset, f2, f, min_support=0.02):
    count = {}
    f3 = {}
    
    # Find candidate triplets only from frequent pairs and items
    for basket in dataset:
        items = sorted([item for item in basket if item in f])  # Filter only frequent items
        for idx_i, i in enumerate(items):
            for j in items[idx_i + 1:]:
                if (i, j) in f2:  # Only consider pairs that are frequent
                    for k in items[idx_i + 2:]:  # Triplet (i, j, k) where k > j
                        if (i, j, k) in count:
                            count[(i, j, k)] += 1
                        else:
                            count[(i, j, k)] = 1

    # Filter triplets by minimum support threshold
    for (i, j, k), cnt in count.items():
        if cnt / len(dataset) >= min_support:
            f3[(i, j, k)] = 1  # Mark as frequent

    # Debugging output
    print("Pass 3 - Frequent triplets count:", len(f3))
    print("Frequent triplets:", f3)
    
    return f3, count

# Usage
f_items, support_items = pass1(dataset)
f2, support_pairs = pass2(dataset, f_items)
f3, support_triplets = pass3(dataset, f2, f_items)

print("Total transactions:", len(dataset))
print("Frequent items:", len(f_items))
print("Frequent pairs:", len(f2))
print("Frequent triplets:", len(f3))
