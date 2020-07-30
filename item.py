class Item():
    def  __init__(self,item_name):
       self.iname = item_name
       self.idescription = None
       self.items_dict={}
    
    def set_iname(self,item_name):
        self.iname = item_name
    def get_iname(self):
        return self.iname

    def set_idescription(self,item_idescription):
        self.idescription = item_idescription

    def get_idescription(self):
        return self.idescription
    def idescribe(self):
        print(self.idescription)
    
    def location(self,items_to_link,idirection):
        self.items_dict[idirection] = items_to_link
        print(self.iname+"items present are "+repr(self.items_dict))

    def get_idetails(self):
        print("\n")
        print(self.get_iname())
        print("-----------------------------------")
        print(self.get_idescription())
        for idirection in self.items_dict : 
            item = self.items_dict[idirection]
            print("the item"+item.get_iname()+"is in"+idirection)
        print("======================================")

    def go(self,idirection):
        if idirection in self.items_dict:
            return self.items_dict[idirection]
        else:
            print("wrong direction")
            return self 



