#single level inheritance
class parent():
    def display(self):
        print("I am a parent")
class child(parent):
    def displayc(self):
        print(" i m child")
d=child() 
d.display()
d.displayc()


# multilevel in heritance
class grandfather():
    def displaygf(self):
        print("I m a grandfather")
class father(grandfather):
    def display(self):
        print("i m a father")
class child(father):
    def displayd(self):
        print("i m a child")
t=child()
t.displaygf()
t.display()
t.displayd()



#multiple in heritance
class father():
    def displayo(self):
        print("i m father")
class mother():
    def displayz(self):
        print("i m mother")
class child(father,mother):
    def displayn(self):
        print("i m child")
x = child()
x.displayo()   # ✅ calls father method
x.displayz()   # ✅ calls mother method
x.displayn()


#Hierarchical inheritance
class parent():
    def display(self):
        print("i m a parent")
class child1(parent):
    def displaye(self):
        print("i a child1")
class child2(parent):
    def displayw(self):
        print("i m child2")
g=child1()
g2=child2()
g.display()
g.displaye()
g2.display()
g2.displayw()

class vehicles():
    def start(self):
        print("starting")
class car(vehicles):
    def drive(self):
        print("driving")
d=car()
d.start()
d.drive()