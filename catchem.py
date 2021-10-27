from sense_hat import SenseHat
from time import sleep
from random import choice, randint

sense = SenseHat()
sense.clear()

game_over = False

catcher_x = 0
berry_x = 0
berry_y = 7

score = 0

r = (255, 0, 0) #red
g = (0, 255, 0) #green
b = (0, 0, 255) #blue
k = (0, 0, 0) #blank
w = (255, 255, 255) #white
c = (0, 255, 255) #cyan
y = (255, 255, 0) #yellow
o = (255, 128, 0) #orange
n = (255, 128, 128) #pink
p = (128, 0, 128) #purple
d = (255, 0, 128) #darkPink
l = (128, 255, 128) #lightGreen

class Game:
  def __init__(self):
    self.catcher_x = 0
    self.berries = [
      {
        "name": "strawberry",
        "color": d,
        "pos_x" : 0,
        "pos_y" : 0,
        "points" : 10
      },
      {
        "name": "raspberry",
        "color": r,
        "pos_x" : 3,
        "pos_y" : 0,
        "points" : 5
      },
      {
        "name": "blueberry",
        "color": b,
        "pos_x" : 1,
        "pos_y" : 0,
        "points" : 15
      },
      {
        "name": "poison",
        "color": l,
        "pos_x" : 3,
        "pos_y" : 0,
        "points" : -5
      }
    ]
    self.berry = choice(self.berries)
    self.berry_x = self.berry["pos_x"]
    self.berry_y = self.berry["pos_y"]
    self.berry_color = self.berry["color"]
    self.score = 0
    self.game_over = False

  def move_left(self):
    if self.catcher_x >= 1:
       self.catcher_x -= 1
       self.update()

  def move_right(self):
     
      if self.catcher_x < 7:
         self.catcher_x += 1
         self.update()

  def berry_fall(self):
      
      if self.berry_y < 7:
         self.berry_y += 1
         sleep(.25)
         sense.set_pixel(self.berry_x, self.berry_y, self.berry_color)
      else:
         self.score += self.berry["points"]
         print(self.score)
         sense.show_message("bye")
         self.game_over = True

  def update(self):
      sense.clear()
      sense.set_pixel(self.catcher_x, 7,b)
      self.berry_fall()

  def run(self):
    # self.update()

    while game_over == False:
        
        for event in sense.stick.get_events():
            print(event)
            if event.action =="pressed" and event.direction == "left":
                self.move_left()
            elif event.action == "pressed" and event.direction == "right":
                self.move_right()
            # else:
            #   sense.show.message("Hello")

        # if berry_x == catcher_x and berry_y == 7:
        #   self.score += self.berry["points"]
        #   print(self.score)

        self.update()
        sleep(.3)

game = Game()
game.run()

# from sense_hat import SenseHat
# from time import sleep
# import random

# sense = SenseHat()
# sense.clear()

# game_over = False

# # catcher_x = 0
# # berry_x = random.randint(0,7)
# # berry_y = 0

# # score = 0

# r = (255, 0, 0) #red
# g = (0, 255, 0) #green
# b = (0, 0, 255) #blue
# k = (0, 0, 0) #blank
# w = (255, 255, 255) #white
# c = (0, 255, 255) #cyan
# y = (255, 255, 0) #yellow
# o = (255, 128, 0) #orange
# n = (255, 128, 128) #pink
# p = (128, 0, 128) #purple
# d = (255, 0, 128) #darkPink
# l = (128, 255, 128) #lightGreen

# # Intro text or animation
# # 3, 2, 1 countdown

# class Game:
#   def __init__(self):
#     self.catcher_x = 0
#     self.berry_x = random.randint(0,7)
#     self.berry_y = 0
#     self.score = 0

#   def move_left():
#     if catcher_x >= 1:
#        catcher_x -= 1
#        update()

#   def move_right():
#       if catcher_x <= 7:
#          catcher_x += 1
#          update()

#   def berry_fall():
#       if berry_y < 7:
#           berry_y += 1
#           sense.set_pixel(berry_x, berry_y, b)
#           update()
#       else:
#           sense.show_message("Game Over")
#           game_over = True
#           new_berry()

#   def new_berry():
#       if berry_y < 7:
#           berry_y += 1
#           sense.set_pixel(berry_x, berry_y, b)

#   def update():
#       sense.clear()
#       berry_fall()
#       sense.set_pixel(catcher_x, 7, d)
    

# while game_over == False:
  
#   for event in sense.stick.get_events():
#     print(event)

#     if event.action == "pressed" and event.direction == "left":
#       move_left()
#     elif event.action == "pressed" and event.direction == "right":
#       move_right()
    
#   update()
#   sleep(1)
  