class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def update_height(self, node):
        if node:
            node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def rotate_right(self, k2):
        k1 = k2.left
        if not k1:
            return k2
        k2.left = k1.right
        k1.right = k2
        self.update_height(k2)
        self.update_height(k1)
        return k1

    def rotate_left(self, k1):
        k2 = k1.right
        if not k2:
            return k1
        k1.right = k2.left
        k2.left = k1
        self.update_height(k1)
        self.update_height(k2)
        return k2

    def double_rotate_left(self, k3):
        k3.left = self.rotate_left(k3.left)
        return self.rotate_right(k3)

    def double_rotate_right(self, k1):
        k1.right = self.rotate_right(k1.right)
        return self.rotate_left(k1)

    def insert(self, root, key):
        if not root:
            return AVLNode(key)

        if key < root.key:
            root.left = self.insert(root.left, key)
            if self.get_height(root.left) - self.get_height(root.right) == 2:
                if key < root.left.key:
                    root = self.rotate_right(root)
                else:
                    root = self.double_rotate_left(root)
        elif key > root.key:
            root.right = self.insert(root.right, key)
            if self.get_height(root.right) - self.get_height(root.left) == 2:
                if key > root.right.key:
                    root = self.rotate_left(root)
                else:
                    root = self.double_rotate_right(root)

        self.update_height(root)
        return root

    def delete(self, root, key):
        if not root:
            return root

        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            temp = self.find_min(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)

        if not root:
            return root

        self.update_height(root)
        balance = self.get_balance(root)

        if balance > 1:
            if self.get_balance(root.left) >= 0:
                return self.rotate_right(root)
            else:
                return self.double_rotate_left(root)
        if balance < -1:
            if self.get_balance(root.right) <= 0:
                return self.rotate_left(root)
            else:
                return self.double_rotate_right(root)

        return root

    def find_min(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def search(self, root, key):
        if not root or root.key == key:
            return root
        if key < root.key:
            return self.search(root.left, key)
        return self.search(root.right, key)

    def inorder(self, root, result=None):
        if result is None:
            result = []
        if root:
            self.inorder(root.left, result)
            result.append(root.key)
            self.inorder(root.right, result)
        return result

    def print_tree(self, root, level=0, prefix="Root: "):
        if root:
            print(" " * (level * 4) + prefix + f"{root.key} (H={root.height})")
            if root.left or root.right:
                if root.left:
                    self.print_tree(root.left, level + 1, "L--- ")
                else:
                    print(" " * ((level + 1) * 4) + "L--- None")
                if root.right:
                    self.print_tree(root.right, level + 1, "R--- ")
                else:
                    print(" " * ((level + 1) * 4) + "R--- None")