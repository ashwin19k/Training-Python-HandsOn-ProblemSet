class Money:
    def __init__(self,dollars,cents):
        self.dollars=dollars
        self.cents=cents
    def __repr__(self,sym):
        self.doll=self.cents/100
        print(self.dollars+self.doll,self.sym)
object=Money(45,10)
object.__repr__('$')