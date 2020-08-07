from rooms import Room
#from item import Item
from character import Enemy



#knife = Item("knife")
#knife.set_idescription("used to cut")
kitchen = Room("Kitchen")
kitchen.set_description("A place to cook and a place to experiment")

dininghall = Room("dininghall")
dininghall.set_description("very symmetrical place to eat")
#cleats = Item("cleats")
#cleats.set_idescription("used to dance")
ballroom = Room("ballroom")
ballroom.set_description("A free breathable space for one to fly")

#forks = Item("forks")
#forks.set_idescription("used to eat")
'''
knife.location(forks,"south")
forks.location(knife,"north")
forks.location(cleats,"west")       
cleats.location(forks,"east")
'''
kitchen.link_room(dininghall,"south")
dininghall.link_room(kitchen,"north")
dininghall.link_room(ballroom,"west")
ballroom.link_room(dininghall,"east")


#dininghall.get_details()
#kitchen.get_details()
#ballroom.get_details()
#initializing enemy
sid = Enemy('sid','demon from hell')
sid.describe()
sid.set_conversation("I lurk in the darkness")
#sid.talk()
sid.set_weakness('light')
#sid.get_weakness()
#x = input()
#sid.fight(x)

#dont add quote
dininghall.set_character(sid)

current_room = kitchen
#current_item = forks
while True:
  print("\n")
  current_room.get_details()
  #current_item.get_idetails()
  inhabitant = current_room.get_character()
  if inhabitant is not None:
    inhabitant.describe()

    
  command = input("dirction please :")
  current_room = current_room.move(command)

  #current_item = current_item.go(command)