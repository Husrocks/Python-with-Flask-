class MyComplexNumbers:
    def __init__(self , real=10 , img= 0):
        print("My complex numbers.... ")
        self.real = real
        self.img = img

    def display_numbers(self):
        print("the {0} + {1}j".format(self.real, self.img))


mynumbers = MyComplexNumbers ()
mynumbers.new_number = 90
mynumbers.display_numbers()
print((mynumbers.real , mynumbers.img , mynumbers.new_number))