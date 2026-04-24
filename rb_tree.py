class RBNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.color = 1


class RBTree:
    def __init__(self):
        self.TNULL = RBNode(0)
        self.TNULL.color = 0
        self.root = self.TNULL

    def rotate_left(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.TNULL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def rotate_right(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.TNULL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def insert_fix(self, k):
        while k.parent.color == 1:
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left
                if u.color == 1:
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.rotate_right(k)
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.rotate_left(k.parent.parent)
            else:
                u = k.parent.parent.right
                if u.color == 1:
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.rotate_left(k)
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.rotate_right(k.parent.parent)
            if k == self.root:
                break
        self.root.color = 0

    def insert(self, key):
        node = RBNode(key)
        node.left = self.TNULL
        node.right = self.TNULL
        node.parent = None
        node.color = 1

        y = None
        x = self.root
        while x != self.TNULL:
            y = x
            if node.key < x.key:
                x = x.left
            else:
                x = x.right

        node.parent = y
        if y == None:
            self.root = node
        elif node.key < y.key:
            y.left = node
        else:
            y.right = node

        if node.parent == None:
            node.color = 0
            return
        if node.parent.parent == None:
            return
        self.insert_fix(node)

    def inorder_helper(self, node, result):
        if node != self.TNULL:
            self.inorder_helper(node.left, result)
            color = "RED" if node.color == 1 else "BLACK"
            result.append(f"{node.key}({color})")
            self.inorder_helper(node.right, result)
        return result

    def inorder(self):
        return self.inorder_helper(self.root, [])

    def print_tree(self, node=None, level=0, prefix="Root: "):
        if node is None:
            node = self.root
        if node != self.TNULL:
            color = "RED" if node.color == 1 else "BLACK"
            print(" " * (level * 4) + prefix + f"{node.key} ({color})")
            if node.left != self.TNULL or node.right != self.TNULL:
                if node.left != self.TNULL:
                    self.print_tree(node.left, level + 1, "L--- ")
                else:
                    print(" " * ((level + 1) * 4) + "L--- NIL")
                if node.right != self.TNULL:
                    self.print_tree(node.right, level + 1, "R--- ")
                else:
                    print(" " * ((level + 1) * 4) + "R--- NIL")