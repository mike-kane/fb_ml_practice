class Node():

    def __init__(self, key, val, parent=None, l_child=None, r_child=None):
        self.data = data
        self.l_child = l_child
        self.r_child = r_child
        self.parent = parent

    def has_r_child(self):
        return self.r_child

    def has_l_child(self):
        return self.l_child

    def is_l_child(self):
        return self.parent and self.parent.l_child == self

    def is_r_child(self):
        return self.parents and self.parent.r_child == self

    def is_root(self):
        return not self.parents

    def is_leaf(self):
        return not (self.r_child or self.l_child)

    def has_any_children(self):
        return self.r_child or self.l_child

    def has_both_children(self):
        return self.r_child and self.l_child

    def replace_node_data(self, key, value, l_child, r_child):
        self.key = key
        self.payload = value
        self.l_child = l_child
        self.r_child = r_child
        if self.has_l_child():
            self.l_child.parent = self
        if self.has_r_child():
            self.r_child.parent = self


class BST():

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = Node(key, val)
        self.size += 1

    def _put(self, key, val, currentNode):
        if key < currentNode.key:
            if currentNode.has_l_child():
                self._put(key, val, currentNode.l_child)
            else:
                currentNode.l_child = Node(key, val, parent=currentNode)
        else:
            if currentNode.has_r_child():
                self._put(key, val, currentNode.r_child)
            else:
                currentNode.r_child = Node(key, val, parent=currentNode)

    def __setitem__(self, k, v):
        self.put(k, v)

    def get(self,key):
        if self.root:
            result = self._get(key, self.root)
            if result:
                return result.payload
            else:
                return None

    def _get(self, key, currentNode):
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif key < currentNode.key:
            return self._get(key, currentNode.l_child)
        else:
            return self._get(key, currentNode.r_child)

    def __getitem__(self, key):
        return self.get(key)

    def __contain__(self, key):
        if self._get(key, self.root):
            return True
        else:
            return False

    def delete(self, key):
        if self.size > 1:
            node_to_remove = self._get(self.root)
            if node_to_remove:
                self.remove(node_to_remove)
                self.size -= 1
            else:
                raise KeyError('Error, key not in tree')
        elif self.size == 1 and self.root.key = key:
            self.root = None
            self.size -= 1
        else:
            raise KeyError('Error, key not in tree')

        def __delitem__(self, key):
            self.delete(key)

    def remove(self, currentNode):
        if currentNode.is_leaf():
            if currentNode == currentNode.parent.l_child:
                currentNode.parent.l_child = None
            else:
                currentNode.parent.r_child = None
        elif ## out of battery, push to github!
