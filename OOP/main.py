class Quadrilateral:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def square(self):
        area = self.length*self.breadth
        return area
    
sq = Quadrilateral(3,4)
print(sq.square())
print(Quadrilateral.square(sq))
