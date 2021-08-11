def find_internal_nodes_num(tree):

    internal_node_count = 0

    for i in range(len(tree)):
        # if an element is someone's parent, it is an internal node
        if i in tree:
            internal_node_count += 1

    return internal_node_count


my_tree = [4, 2, 4, 5, -1, 4, 5]
print('The number of internal nodes are', find_internal_nodes_num(my_tree))
