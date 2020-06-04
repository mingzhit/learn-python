class Point:
    def __init__(self, x, y):   #构造函数，__init__初始化对象
        self.x = x
        self.y = y
    def move(self):
        print("move")

    def draw(self):
        print("draw")

point = Point(10, 20)
print(point.x)