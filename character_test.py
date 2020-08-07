from character import Enemy 

sid = Enemy('sid','demon from hell')
sid.describe()
sid.set_conversation("I lurk in the darkness")
sid.talk()
sid.set_weakness('light')
sid.get_weakness()
x = input()
sid.fight(x)
