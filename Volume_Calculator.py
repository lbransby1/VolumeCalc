#Constants#
PI = 3.1416
CLEAR = "\n" * 20
VOLUME = "The Volume is"
SA = "The surface area is"

#Functions#
def mainMenu():
  clear()
  inputV = input("Shapes:\nCube - 1:\nSphere - 2:\nCylinder - 3:\nCuboid - 4\nPyramid - 5:\nType the number of the chosen shape\n\n")
  selectShape(inputV)

def clear():
  print(CLEAR)

def selectShape(shape):
  if shape == "1":
    print(CLEAR)
    cubeSel()
  elif shape == "2":
    sphereSel()
  elif shape == "3":
    print(CLEAR)
    cylinderSel()
  elif shape == "4":
    print(CLEAR)
    cuboidSel()
  elif shape == "5":
    print(CLEAR)
    pyramidSel()

  
def sphereSel():
  clear()
  radius = input("Whats the radius?")
  sphere1 = Sphere(radius)
  clear()

  print(SA, int(round(sphere1.SurfaceArea, -3)))
  print(VOLUME, int(round(sphere1.Volume, -3)))
  inputV = input("\nWhat would you like to do next?\n 0: go back\n 1: Change radius \n Type here: \n ")
  
  if inputV == "1":
    sphereSel()
  if inputV == "0":
    mainMenu()
  else:
    print("Enter a valid input, doofus")
    mainMenu()


def cylinderSel():
  clear()
  radius = input("Whats the radius?")
  length = input("Whats the length")
  cylinder1 = Cylinder(radius, length)
  clear()

  print(SA, int(round(cylinder1.SurfaceArea,-3)))
  print(VOLUME, int(round(cylinder1.Volume,-3)))
  inputV = input("\nWhat would you like to do next?\n0: go back\n1: Change Dimentions\nType here:\n")
  
  if inputV == "1":
    sphereSel()
  if inputV == "0":
    mainMenu()
  else:
    print("Enter a valid input, doofus")
    mainMenu()
  

  pass
def cuboidSel():
  pass
def pyramidSel():
  pass
def cubeSel():
  clear()
  Length = input("What is the length of all sides?")
  cube1 = Cube(Length)
  clear()

  print(SA, int(cube1.SurfaceArea))
  print(VOLUME, int(cube1.Volume))
  inputV = input("\nWhat would you like to do next?\n 0: go back\n 1: Change radius \n Type here: \n ")
  
  if inputV == "1":
    cubeSel()
  if inputV == "0":
    mainMenu()
  else:
    print("Enter a valid input, doofus")
    mainMenu()


class Shape:
  def __init__ (self, Volume, SurfaceArea):
    self.Volume = Volume
    self.SurfaceArea = SurfaceArea

class Sphere(Shape):
  def __init__ (self, Rad):
    self.Radius = Rad            
    self.Volume = (int(self.Radius)**3)*PI*(4/3)    #sphere vol equation
    self.SurfaceArea = (int(self.Radius)**2)*PI*4   #sphere sa equation



###for later START
class Cube(Shape):
  pass
class Pyramid(Shape):
  pass


class Cylinder(Shape):
  def __init__ (self, Rad, Length):
    self.Length = Length
    self.Radius = Rad            
    self.Volume = (int(self.Radius)**3)*PI*int(self.Length)   #sphere vol equation
    self.SurfaceArea = ((int(self.Radius)**2)*PI*2)+(2*PI*int(self.Radius)*int(self.Length))  #sphere sa equation

class Cuboid(Shape):
  pass
###for later END
mainMenu()
