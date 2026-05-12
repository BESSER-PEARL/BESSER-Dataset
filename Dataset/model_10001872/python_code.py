from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Food:

    def __init__(self, foodID: int, name: str, chef5: set["Chef"] = None, guest6: set["Guest"] = None):
        self.foodID = foodID
        self.name = name
        self.chef5 = chef5 if chef5 is not None else set()
        self.guest6 = guest6 if guest6 is not None else set()
        
        pass
    @property
    def foodID(self):
        return self.__foodID
    @foodID.setter
    def foodID(self, foodID: int):
        self.__foodID = foodID

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def guest6(self):
        return self.__guest6
    @guest6.setter
    def guest6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Food__guest6", None)
        self.__guest6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "food7"):
                    opp_val = getattr(item, "food7", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "food7"):
                    opp_val = getattr(item, "food7", None)
                    
                    if opp_val is None:
                        setattr(item, "food7", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def chef5(self):
        return self.__chef5
    @chef5.setter
    def chef5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Food__chef5", None)
        self.__chef5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "food4"):
                    opp_val = getattr(item, "food4", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "food4"):
                    opp_val = getattr(item, "food4", None)
                    
                    if opp_val is None:
                        setattr(item, "food4", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Housekeeping:

    def __init__(self, name: str, hkID: int, branch: str, rooms13: "Rooms" = None):
        self.name = name
        self.hkID = hkID
        self.branch = branch
        self.rooms13 = rooms13
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def branch(self):
        return self.__branch
    @branch.setter
    def branch(self, branch: str):
        self.__branch = branch

    @property
    def hkID(self):
        return self.__hkID
    @hkID.setter
    def hkID(self, hkID: int):
        self.__hkID = hkID

    @property
    def rooms13(self):
        return self.__rooms13
    @rooms13.setter
    def rooms13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Housekeeping__rooms13", None)
        self.__rooms13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "housekeeping12"):
                opp_val = getattr(old_value, "housekeeping12", None)
                if opp_val == self:
                    setattr(old_value, "housekeeping12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "housekeeping12"):
                opp_val = getattr(value, "housekeeping12", None)
                setattr(value, "housekeeping12", self)



class Bill:

    def __init__(self, billNo: int, guestID: int, guest11: "Guest" = None, receptionist15: set["Receptionist"] = None):
        self.billNo = billNo
        self.guestID = guestID
        self.guest11 = guest11
        self.receptionist15 = receptionist15 if receptionist15 is not None else set()
        
        pass
    @property
    def guestID(self):
        return self.__guestID
    @guestID.setter
    def guestID(self, guestID: int):
        self.__guestID = guestID

    @property
    def billNo(self):
        return self.__billNo
    @billNo.setter
    def billNo(self, billNo: int):
        self.__billNo = billNo

    @property
    def receptionist15(self):
        return self.__receptionist15
    @receptionist15.setter
    def receptionist15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Bill__receptionist15", None)
        self.__receptionist15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bill14"):
                    opp_val = getattr(item, "bill14", None)
                    
                    if opp_val == self:
                        setattr(item, "bill14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bill14"):
                    opp_val = getattr(item, "bill14", None)
                    
                    setattr(item, "bill14", self)
                    

    @property
    def guest11(self):
        return self.__guest11
    @guest11.setter
    def guest11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Bill__guest11", None)
        self.__guest11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bill10"):
                opp_val = getattr(old_value, "bill10", None)
                if opp_val == self:
                    setattr(old_value, "bill10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bill10"):
                opp_val = getattr(value, "bill10", None)
                setattr(value, "bill10", self)



class Rooms:

    def __init__(self, roomNo: int, type: str, housekeeping12: "Housekeeping" = None, receptionist16: set["Receptionist"] = None, guest9: "Guest" = None):
        self.roomNo = roomNo
        self.type = type
        self.housekeeping12 = housekeeping12
        self.receptionist16 = receptionist16 if receptionist16 is not None else set()
        self.guest9 = guest9
        
        pass
    @property
    def roomNo(self):
        return self.__roomNo
    @roomNo.setter
    def roomNo(self, roomNo: int):
        self.__roomNo = roomNo

    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def guest9(self):
        return self.__guest9
    @guest9.setter
    def guest9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Rooms__guest9", None)
        self.__guest9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rooms8"):
                opp_val = getattr(old_value, "rooms8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rooms8"):
                opp_val = getattr(value, "rooms8", None)
                if opp_val is None:
                    setattr(value, "rooms8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def receptionist16(self):
        return self.__receptionist16
    @receptionist16.setter
    def receptionist16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Rooms__receptionist16", None)
        self.__receptionist16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rooms17"):
                    opp_val = getattr(item, "rooms17", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rooms17"):
                    opp_val = getattr(item, "rooms17", None)
                    
                    if opp_val is None:
                        setattr(item, "rooms17", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def housekeeping12(self):
        return self.__housekeeping12
    @housekeeping12.setter
    def housekeeping12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Rooms__housekeeping12", None)
        self.__housekeeping12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rooms13"):
                opp_val = getattr(old_value, "rooms13", None)
                if opp_val == self:
                    setattr(old_value, "rooms13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rooms13"):
                opp_val = getattr(value, "rooms13", None)
                setattr(value, "rooms13", self)



class Chef:

    def __init__(self, chefID: int, name: str, branch: str, food4: set["Food"] = None):
        self.chefID = chefID
        self.name = name
        self.branch = branch
        self.food4 = food4 if food4 is not None else set()
        
        pass
    @property
    def branch(self):
        return self.__branch
    @branch.setter
    def branch(self, branch: str):
        self.__branch = branch

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def chefID(self):
        return self.__chefID
    @chefID.setter
    def chefID(self, chefID: int):
        self.__chefID = chefID

    @property
    def food4(self):
        return self.__food4
    @food4.setter
    def food4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Chef__food4", None)
        self.__food4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "chef5"):
                    opp_val = getattr(item, "chef5", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "chef5"):
                    opp_val = getattr(item, "chef5", None)
                    
                    if opp_val is None:
                        setattr(item, "chef5", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Guest:

    def __init__(self, name: str, guestID: int, address: str, phoneNo: int, roomNo: int, manager3: "Manager" = None, food7: set["Food"] = None, rooms8: set["Rooms"] = None, bill10: "Bill" = None):
        self.name = name
        self.guestID = guestID
        self.address = address
        self.phoneNo = phoneNo
        self.roomNo = roomNo
        self.manager3 = manager3
        self.food7 = food7 if food7 is not None else set()
        self.rooms8 = rooms8 if rooms8 is not None else set()
        self.bill10 = bill10
        
        pass
    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def guestID(self):
        return self.__guestID
    @guestID.setter
    def guestID(self, guestID: int):
        self.__guestID = guestID

    @property
    def phoneNo(self):
        return self.__phoneNo
    @phoneNo.setter
    def phoneNo(self, phoneNo: int):
        self.__phoneNo = phoneNo

    @property
    def roomNo(self):
        return self.__roomNo
    @roomNo.setter
    def roomNo(self, roomNo: int):
        self.__roomNo = roomNo

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def bill10(self):
        return self.__bill10
    @bill10.setter
    def bill10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Guest__bill10", None)
        self.__bill10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "guest11"):
                opp_val = getattr(old_value, "guest11", None)
                if opp_val == self:
                    setattr(old_value, "guest11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "guest11"):
                opp_val = getattr(value, "guest11", None)
                setattr(value, "guest11", self)

    @property
    def rooms8(self):
        return self.__rooms8
    @rooms8.setter
    def rooms8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Guest__rooms8", None)
        self.__rooms8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "guest9"):
                    opp_val = getattr(item, "guest9", None)
                    
                    if opp_val == self:
                        setattr(item, "guest9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "guest9"):
                    opp_val = getattr(item, "guest9", None)
                    
                    setattr(item, "guest9", self)
                    

    @property
    def food7(self):
        return self.__food7
    @food7.setter
    def food7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Guest__food7", None)
        self.__food7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "guest6"):
                    opp_val = getattr(item, "guest6", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "guest6"):
                    opp_val = getattr(item, "guest6", None)
                    
                    if opp_val is None:
                        setattr(item, "guest6", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def manager3(self):
        return self.__manager3
    @manager3.setter
    def manager3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Guest__manager3", None)
        self.__manager3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "guest2"):
                opp_val = getattr(old_value, "guest2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "guest2"):
                opp_val = getattr(value, "guest2", None)
                if opp_val is None:
                    setattr(value, "guest2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Inventory:

    def __init__(self, type: str, status: str, manager1: "Manager" = None):
        self.type = type
        self.status = status
        self.manager1 = manager1
        
        pass
    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self, status: str):
        self.__status = status

    @property
    def manager1(self):
        return self.__manager1
    @manager1.setter
    def manager1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Inventory__manager1", None)
        self.__manager1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "inventory0"):
                opp_val = getattr(old_value, "inventory0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "inventory0"):
                opp_val = getattr(value, "inventory0", None)
                if opp_val is None:
                    setattr(value, "inventory0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Receptionist:

    def __init__(self, rID: int, name: str, phoneNo: int, branch: str, bill14: "Bill" = None, rooms17: set["Rooms"] = None):
        self.rID = rID
        self.name = name
        self.phoneNo = phoneNo
        self.branch = branch
        self.bill14 = bill14
        self.rooms17 = rooms17 if rooms17 is not None else set()
        
        pass
    @property
    def phoneNo(self):
        return self.__phoneNo
    @phoneNo.setter
    def phoneNo(self, phoneNo: int):
        self.__phoneNo = phoneNo

    @property
    def rID(self):
        return self.__rID
    @rID.setter
    def rID(self, rID: int):
        self.__rID = rID

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def branch(self):
        return self.__branch
    @branch.setter
    def branch(self, branch: str):
        self.__branch = branch

    @property
    def bill14(self):
        return self.__bill14
    @bill14.setter
    def bill14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Receptionist__bill14", None)
        self.__bill14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "receptionist15"):
                opp_val = getattr(old_value, "receptionist15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "receptionist15"):
                opp_val = getattr(value, "receptionist15", None)
                if opp_val is None:
                    setattr(value, "receptionist15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rooms17(self):
        return self.__rooms17
    @rooms17.setter
    def rooms17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Receptionist__rooms17", None)
        self.__rooms17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "receptionist16"):
                    opp_val = getattr(item, "receptionist16", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "receptionist16"):
                    opp_val = getattr(item, "receptionist16", None)
                    
                    if opp_val is None:
                        setattr(item, "receptionist16", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Manager:

    def __init__(self, managerID: int, name: str, phoneNo: int, branch: str, inventory0: set["Inventory"] = None, guest2: set["Guest"] = None):
        self.managerID = managerID
        self.name = name
        self.phoneNo = phoneNo
        self.branch = branch
        self.inventory0 = inventory0 if inventory0 is not None else set()
        self.guest2 = guest2 if guest2 is not None else set()
        
        pass
    @property
    def phoneNo(self):
        return self.__phoneNo
    @phoneNo.setter
    def phoneNo(self, phoneNo: int):
        self.__phoneNo = phoneNo

    @property
    def branch(self):
        return self.__branch
    @branch.setter
    def branch(self, branch: str):
        self.__branch = branch

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def managerID(self):
        return self.__managerID
    @managerID.setter
    def managerID(self, managerID: int):
        self.__managerID = managerID

    @property
    def guest2(self):
        return self.__guest2
    @guest2.setter
    def guest2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Manager__guest2", None)
        self.__guest2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "manager3"):
                    opp_val = getattr(item, "manager3", None)
                    
                    if opp_val == self:
                        setattr(item, "manager3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "manager3"):
                    opp_val = getattr(item, "manager3", None)
                    
                    setattr(item, "manager3", self)
                    

    @property
    def inventory0(self):
        return self.__inventory0
    @inventory0.setter
    def inventory0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Manager__inventory0", None)
        self.__inventory0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "manager1"):
                    opp_val = getattr(item, "manager1", None)
                    
                    if opp_val == self:
                        setattr(item, "manager1", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "manager1"):
                    opp_val = getattr(item, "manager1", None)
                    
                    setattr(item, "manager1", self)
                    

