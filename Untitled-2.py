class myClass:
    __privateVar = 27;
    def Meth(self):
        print('Im inside myClass')
    def hello(self):
        print('Private Varible value', myClass. __privateVar)
foo = myClass()
foo.hello()
foo.Meth()