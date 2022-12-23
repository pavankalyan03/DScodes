class BST:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None

    def addchild(self, val):
        if self.data == val:
            return
        if self.data > val:
            if self.left:
                self.left.addchild(val)
            else:
                self.left = BST(val)
                self.left.parent = self
        else:
            if self.right:
                self.right.addchild(val)
            else:
                self.right = BST(val)
                self.right.parent = self

    def inorder(self):
        elements = []
        # visit left node
        if self.left:
            elements += self.left.inorder()
        # visit base node
        elements.append(self.data)
        # visit right node
        if self.right:
            elements += self.right.inorder()
        return elements

    def preorder(self):
        elements = []

        elements.append(self.data)
        if self.left:
            elements += self.left.inorder()
        if self.right:
            elements += self.right.inorder()
        return elements

    def postorder(self):
        elements = []
        if self.left:
            elements += self.left.inorder()
        if self.right:
            elements += self.right.inorder()
        elements.append(self.data)
        return elements

    def levelorder(self):
        traversed = []
        traversed.append(self)
        if self is None:
            return traversed
        while traversed:
            print(traversed[0].data, end=' ')
            x = traversed.pop(0)
            if x.left:
                traversed.append(x.left)
            if x.right:
                traversed.append(x.right)

    def delete(self, val):
        # -->check if exist
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
            minval = self.right.findmin()
            self.data = minval
            self.right = self.right.delete(minval)

        return self

    def delleaf(self):
        if self.left is None and self.right is None:
            return None
        else:
            if self.left:
                self.left = self.left.delleaf()
            if self.right:
                self.right = self.right.delleaf()
        return self

    # def delinorder(self, val):
    #     if val < self.data:
    #         if self.left:
    #             self.left = self.left.delinorder(val)
    #     elif val > self.data:
    #         if self.right:
    #             self.right = self.right.delinorder(val)
    #     else:
    #         if self.right:
    #             return self.delete(self.right.findmin())
    #         else:
    #             p = self.parent
    #             while p is not None:
    #                 if self.data != p.right.data:
    #                     break
    #                 self = self.parent
    #                 p = p.parent
    #             return self.delete(p.parent.data)

    def delleftchild(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delleftchild(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delleftchild(val)
        else:
            if self.left:
                self.delete(self.left.data)
        return self

    def delrightchild(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delrightchild(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delrightchild(val)
        else:
            if self.right:
                self.delete(self.right.data)
        return self

    def find_45and55(self):
        if (self.left.data == 45 and self.right.data == 55) or (self.right.data == 45 and self.left.data == 55):
            return self.data
        if self.left:
            self.left = self.left.find_45and55()
        if self.right:
            self.right = self.right.find_45and55()
        else:
            return None

    def height(self):
        if self is None:
            return 0
        left_height = 0
        if self.left:
            left_height = self.left.height()
        right_height = 0
        if self.right:
            right_height = self.right.height()
        return max(left_height, right_height) + 1

    def height5(self, height = 2):
        if self is None:
            return
        if self.height() == height:
            print(self.data)
        if self.left:
            self.left.height5(height)
        if self.right:
            self.right.height5(height)
        return

    def findmin(self):
        if self.left is None:
            return self.data
        return self.left.findmin()

    def findmax(self):
        if self.right is None:
            return self.data
        return self.right.findmax()

    def findparent(self, val):
        if (self.left and self.left.data == val) or (self.right and self.right.data == val):
            return self.data
        elif val < self.data:
            if self.left:
                return self.left.findparent(val)
        else:
            if self.right:
                return self.right.findparent(val)

    def deleteparent(self, val):
        if self.data == val:
            print("NO PARENT FOUND")
        else:
            parent = self.findparent(val)
            return self.delete(parent)


def buildtree(elements):
    root = BST(elements[0])
    for i in range(1, len(elements)):
        root.addchild(elements[i])
    return root


if __name__ == "__main__":
    numbers = [8, 3, 10, 1, 6, 14, 4, 7, 13, 18, 17, 15, 16]
    tree = buildtree(numbers)
    print(tree.inorder())


