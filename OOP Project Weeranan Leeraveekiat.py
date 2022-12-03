#Weeranan Leeraveekiat
class circle:
    def __init__(self, r):
        self.r = r          
    def area(self):         
        return 22/7*((int(self.r))**2)
class rectangle:
    def __init__(self, w, h):
        self.w = w
        self.h = h
    def area(self):
        return (int(self.w))*(int(self.h))
class triangle:
    def __init__(self, b, h):
        self.b = b
        self.h = h
    def area(self):
        return 0.5*(int(self.b))*(int(self.h))
class trapezoid:
    def __init__(self, m, n, h):
        self.m = m
        self.n = n
        self.h = h
    def area(self):
        return 0.5*(int(self.h))*((int(self.m))+(int(self.n)))
class ellipse:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def area(self):
        return 22/7*(int(self.a))*(int(self.b))
while True:
    print("******* Area Calculator *******")
    print("** 1. Circle Area            **")
    print("** 2. Rectangle Area         **")
    print("** 3. Triangle Area          **")
    print("** 4. Trapezoid Area         **")
    print("** 5. Ellipse Area           **")
    print("** 6. EXIT                   **")
    print("*******************************")
    n = input("Select: ")
    if n == "1":
        r = input("Enter radius: ")
        C = circle(r)
        area = C.area
        print ("Area = " + '%.1f' %(area()))
        p = input("Press ENTER to return..")
    elif n == "2":
        width = input("Enter width(w): ")
        height = input("Enter height(h): ")
        R = rectangle(width, height)
        area = R.area
        print ("Area = " + str(area()))
        p = input("Press ENTER to return..")
    elif n == "3":
        base = input("Enter base(b): ")
        height = input("Enter height(h): ")
        Tr = triangle(base, height)
        area = Tr.area
        print ("Area = " + str(area()))
        p = input("Press ENTER to return..")
    elif n == "4":
        M = input("Enter length m: ")
        N = input("Enter length n: ")
        height = input("Enter height (h): ")
        Tra = trapezoid(M, N, height)
        area = Tra.area
        print ("Area = " + str(area()))
        p = input("Press ENTER to return..")
    elif n == "5":
        a = input("Enter radius a: ")
        b = input("Enter radius b: ")
        E = ellipse(a, b)
        area = E.area
        print ("Area = " + str(area()))
        p = input("Press ENTER to return..")
    elif n == "6":
        print ("Exit Program.")
        print (">>>")
        break