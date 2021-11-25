

class A:

    def __init__(self):
        print("In A __init__")

    def feature1(self):
        print("Feature 1")

    def feature2(self):
        print("Feature 2")


# class B(A):

class B:

    def __init__(self):
        super().__init__()
        print("In B __init__")

    def feature3(self):
        print("Feature 3")

    def feature4(self):
        print("Feature 4")


class C(A, B):

    def __init__(self):
        super().__init__()
        print("In C __init__")

    def feature5(self):
        super().feature2()


# a = A()
# a.feature1()
# a.feature2()

""" Output
    In A __init__
    Feature 1
    Feature 2
"""

# b = B()
""" Output
    In A __init__ => We've not created __init__ method into B Class.
"""

# b = B()
""" Output
    In B __init__ => We've created __init__ method into B Class.
"""

# b = B()
""" Output
    In A __init__
    In B __init__ => We've created super().__init__() in __init__ method of B Class.
"""

c = C()
c.feature5()
