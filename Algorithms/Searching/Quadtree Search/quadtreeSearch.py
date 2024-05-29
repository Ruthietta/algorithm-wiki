class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class QuadTreeNode:
    def __init__(self, x_min, y_min, x_max, y_max):
        self.x_min = x_min
        self.y_min = y_min
        self.x_max = x_max
        self.y_max = y_max
        self.children = [None, None, None, None]
        self.points = []

def insert_point(root, point):
    if not root:
        return
    if root.x_min <= point.x <= root.x_max and root.y_min <= point.y <= root.y_max:
        if len(root.points) < 4:
            root.points.append(point)
        else:
            x_mid = (root.x_min + root.x_max) // 2
            y_mid = (root.y_min + root.y_max) // 2
            if point.x <= x_mid:
                if point.y <= y_mid:
                    if not root.children[0]:
                        root.children[0] = QuadTreeNode(root.x_min, root.y_min, x_mid, y_mid)
                    insert_point(root.children[0], point)
                else:
                    if not root.children[1]:
                        root.children[1] = QuadTreeNode(root.x_min, y_mid + 1, x_mid, root.y_max)
                    insert_point(root.children[1], point)
            else:
                if point.y <= y_mid:
                    if not root.children[2]:
                        root.children[2] = QuadTreeNode(x_mid + 1, root.y_min, root.x_max, y_mid)
                    insert_point(root.children[2], point)
                else:
                    if not root.children[3]:
                        root.children[3] = QuadTreeNode(x_mid + 1, y_mid + 1, root.x_max, root.y_max)
                    insert_point(root.children[3], point)

def quadtree_search(root, target):
    if not root:
        return False
    if root.x_min <= target.x <= root.x_max and root.y_min <= target.y <= root.y_max:
        for point in root.points:
            if point.x == target.x and point.y == target.y:
                return True
        for child in root.children:
            if quadtree_search(child, target):
                return True
    return False

# Example usage:
root = QuadTreeNode(0, 0, 100, 100)
insert_point(root, Point(10, 10))
insert_point(root, Point(30, 30))
insert_point(root, Point(70, 70))

target = Point(30, 30)
if quadtree_search(root, target):
    print("Point found in Quadtree.")
else:
    print("Point not found in Quadtree.")
