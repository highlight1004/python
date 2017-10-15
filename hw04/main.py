class Ellipse():
    def __init__(ellipse,cbz,dbz):
        ellipse.cbz=cbz
        ellipse.dbz=dbz
    def get_area(ellipse):
        return ellipse.cbz*ellipse.dbz*3.14
class Circle(Ellipse):
        def __init__(circle,r):
            circle.cbz=r
            circle.dbz=r
class Rectangle():
        def __init__(rectangle,c,k):
            rectangle.c=c
            rectangle.k=k
        def get_area(rectangle):
            return rectangle.k*rectangle.c
class Square(Rectangle):
    def __init__(square,board):
        square.c=board
        square.k=board

        
def compute_area(shapes):
    z=0
    for i in shapes:
        z+=i.get_area()
    return z

shapes=[Ellipse(10,20),Square(15),Circle(5),Rectangle(20,15),Ellipse(10,20),Square(15),Circle(5)]
a=compute_area(shapes)
print(a)
