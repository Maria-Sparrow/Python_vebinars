from abc import ABC, abstractmethod

class AbstractParent(ABC):

  @abstractmethod
  def hello_friend():
    raise NotImplementedError

class Mother(AbstractParent):
  def init(self, age = 0):
    self.age = age
    print('Mother constructor!')
    
  def cook_meal(self):
      print("Hey, I was cooked dinner!")  

  def do_work(self):
    print("I'm working")

  def do_house_work(self):
    print('listening music')

class Father(AbstractParent):
  def init(self):
    print('Father constructor!')

  def play_guitar(self):
    print('play guitar')

  def do_house_work(self):
    print('sitting on the sofa and drink beer')


class Daughter(Mother, Father):
  
  def init(self, age = 0, name = None):
    Mother.init(self, age=age)
    Father.init(self)

  def do_work(self):
    print("I'm working like a horse!")
    
  def cook_meal(self):
      print("Hey,Can l help you?")  


  def hello_friend(self):
    pass

class Friend:
  pass

def greet_mother(mother : Mother):
  print("Hello mother!!!")
  mother.do_work()


def greet_father(father : Father):
  print('time to beer!')
  father.play_guitar()




if __name__ == "__main__":

  daughter = Daughter()
  #mother.do_work()

  #change object class
  #daughter.class = Friend

  greet_mother(daughter)
  greet_father(daughter)

  daughter.hello_friend()
  daughter.do_house_work()
  daughter.cook_meal()