import numpy as np


class Node:
    def __init__(self, left, leftval, right, rightval, val):
        self.left = left
        self.leftval = leftval
        self.right = right
        self.rightval = rightval
        self.val = val

    def print(self, gap):
        if self.right is not None:
            print(gap + self.val)
            self.left.print(gap + self.val + "-left----" + str(self.leftval) + '---')
            self.right.print(gap + self.val + "-right----" + str(self.rightval) + '---')
        else:
            print(gap + "OTU:" + str(self.val))

        return


def compute_ulist(dic, lst):
    n = len(lst)
    u_list = {}
    for i_otu in lst:
        u_i = 0
        for j_otu in lst:
            if i_otu == j_otu:
                continue
            u_i += dic[(i_otu, j_otu)]
        u_i = u_i / (n - 2)
        u_list[i_otu] = u_i

    return u_list


def find_lowest(dst, ulst, lst):
    min_v = np.inf
    min_k = ()
    for i_otu in lst:
        ui = ulst[i_otu]
        for j_otu in lst:
            if i_otu == j_otu:
                continue
            val = dst[(i_otu, j_otu)] - ui - ulst[j_otu]
            if val < min_v:
                min_v = val
                min_k = (i_otu, j_otu)

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
tree = {i: Node(None, None, None, None, i) for i in otus}
root = Node(None, None, None, None, None)

while len(otus) > 2:
    u_list = compute_ulist(distances, otus)

    new_group = find_lowest(distances, u_list, otus)
    new_otu = '(' + new_group[0] + ',' + new_group[1] + ')'

    v0 = 0.5 * distances[new_group] + 0.5 * (u_list[new_group[0]] - u_list[new_group[1]])
    v1 = 0.5 * distances[new_group] + 0.5 * (u_list[new_group[1]] - u_list[new_group[0]])

    root = tree[new_otu] = Node(tree[new_group[0]], v0,
                                tree[new_group[1]], v1,
                                new_otu)

    otus.remove(new_group[0])
    otus.remove(new_group[1])

    for i in otus:
        distances[(new_otu, i)] = distances[(i, new_otu)] = (distances.pop((i, new_group[0])) + distances.pop((i, new_group[1])) - distances[new_group]) / 2
        distances.pop((new_group[0], i))
        distances.pop((new_group[1], i))

    distances.pop((new_group[0], new_group[1]))
    distances.pop((new_group[1], new_group[0]))

    otus.add(new_otu)


new_group = tuple(otus)
new_otu = '(' + new_group[0] + ',' + new_group[1] + ')'

v0 = distances[new_group]
v1 = distances[new_group]

root = tree[new_otu] = Node(tree[new_group[0]], v0,
                            tree[new_group[1]], v1,
                            new_otu)


root.print('')
