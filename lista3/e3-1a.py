import numpy as np


class Node:
    def __init__(self, left, right, val):
        self.left = left
        self.right = right
        self.val = val

    def print(self, gap):
        if self.right is not None:
            print(gap + self.val)
            self.left.print(gap + self.val + "-left----")
            self.right.print(gap + self.val + "-right----")
        else:
            print(gap + "OTU:" + str(self.val))

        return


def get_min(dic: dict):
    min_v = np.inf
    min_k = ()
    for k in dic.keys():
        if dic[k] < min_v:
            min_v = dic[k]
            min_k = k

    return min_k


distances = {
    ('gori', 'oran'): 0.1890,
    ('gori', 'huma'): 0.1100,
    ('gori', 'chim'): 0.1130,
    ('gori', 'giba'): 0.2150,
    ('oran', 'huma'): 0.1790,
    ('oran', 'chim'): 0.1920,
    ('oran', 'giba'): 0.2110,
    ('huma', 'chim'): 0.0940,
    ('huma', 'giba'): 0.2050,
    ('chim', 'giba'): 0.2140
}
keys = [k for k in distances.keys()]
for k in keys:
    distances[(k[1], k[0])] = distances[k]

otus = {i[0] for i in distances.keys()}
tree = {i: Node(None, None, i) for i in otus}
root = Node(None, None, None)

while len(otus) > 1:
    new_node = get_min(distances)
    new_otu = '(' + new_node[0] + ',' + new_node[1] + ')'

    root = tree[new_otu] = Node(tree[new_node[0]],
                                tree[new_node[1]],
                                new_otu)

    otus.remove(new_node[0])
    otus.remove(new_node[1])
    distances.pop((new_node[0], new_node[1]))
    distances.pop((new_node[1], new_node[0]))

    for i in otus:
        distances[(new_otu, i)] = distances[(i, new_otu)] = (distances.pop((i, new_node[0])) + distances.pop((i, new_node[1]))) / 2
        distances.pop((new_node[0], i))
        distances.pop((new_node[1], i))

    otus.add(new_otu)

root.print('')
