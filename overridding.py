class addition:
                  def add(self,x,y):
                    print(x+y)
               class child(addition):
                  def add(self,x,y,z):
                    print(x+y+z)
               i=child()
               i.add(5,6,7)  
