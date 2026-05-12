from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Database:

    def __init__(self, service: str, income: int, Details: str, receptionist13: set["Receptionist"] = None, manager15: "Manager" = None):
        self.service = service
        self.income = income
        self.Details = Details
        self.receptionist13 = receptionist13 if receptionist13 is not None else set()
        self.manager15 = manager15
        
        pass
    @property
    def Details(self):
        return self.__Details
    @Details.setter
    def Details(self, Details: str):
        self.__Details = Details

    @property
    def income(self):
        return self.__income
    @income.setter
    def income(self, income: int):
        self.__income = income

    @property
    def service(self):
        return self.__service
    @service.setter
    def service(self, service: str):
        self.__service = service

    @property
    def receptionist13(self):
        return self.__receptionist13
    @receptionist13.setter
    def receptionist13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Database__receptionist13", None)
        self.__receptionist13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "database12"):
                    opp_val = getattr(item, "database12", None)
                    
                    if opp_val == self:
                        setattr(item, "database12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "database12"):
                    opp_val = getattr(item, "database12", None)
                    
                    setattr(item, "database12", self)
                    

    @property
    def manager15(self):
        return self.__manager15
    @manager15.setter
    def manager15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Database__manager15", None)
        self.__manager15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "database14"):
                opp_val = getattr(old_value, "database14", None)
                if opp_val == self:
                    setattr(old_value, "database14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "database14"):
                opp_val = getattr(value, "database14", None)
                setattr(value, "database14", self)



class Inventory:

    def __init__(self, type: str, Status: str, manager10: "Manager" = None):
        self.type = type
        self.Status = Status
        self.manager10 = manager10
        
        pass
    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def Status(self):
        return self.__Status
    @Status.setter
    def Status(self, Status: str):
        self.__Status = Status

    @property
    def manager10(self):
        return self.__manager10
    @manager10.setter
    def manager10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Inventory__manager10", None)
        self.__manager10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "inventory11"):
                opp_val = getattr(old_value, "inventory11", None)
                if opp_val == self:
                    setattr(old_value, "inventory11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "inventory11"):
                opp_val = getattr(value, "inventory11", None)
                setattr(value, "inventory11", self)



class Bill:

    def __init__(self, bill_No: int, GuestName: str, guest3: "Guest" = None, receptionist7: set["Receptionist"] = None):
        self.bill_No = bill_No
        self.GuestName = GuestName
        self.guest3 = guest3
        self.receptionist7 = receptionist7 if receptionist7 is not None else set()
        
        pass
    @property
    def bill_No(self):
        return self.__bill_No
    @bill_No.setter
    def bill_No(self, bill_No: int):
        self.__bill_No = bill_No

    @property
    def GuestName(self):
        return self.__GuestName
    @GuestName.setter
    def GuestName(self, GuestName: str):
        self.__GuestName = GuestName

    @property
    def receptionist7(self):
        return self.__receptionist7
    @receptionist7.setter
    def receptionist7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Bill__receptionist7", None)
        self.__receptionist7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bill6"):
                    opp_val = getattr(item, "bill6", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bill6"):
                    opp_val = getattr(item, "bill6", None)
                    
                    if opp_val is None:
                        setattr(item, "bill6", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def guest3(self):
        return self.__guest3
    @guest3.setter
    def guest3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Bill__guest3", None)
        self.__guest3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bill2"):
                opp_val = getattr(old_value, "bill2", None)
                if opp_val == self:
                    setattr(old_value, "bill2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bill2"):
                opp_val = getattr(value, "bill2", None)
                setattr(value, "bill2", self)



class Room:

    def __init__(self, roomNo: int, typeOfRoom: str, RatesofRoom: int, guest1: "Guest" = None, receptionist5: set["Receptionist"] = None):
        self.roomNo = roomNo
        self.typeOfRoom = typeOfRoom
        self.RatesofRoom = RatesofRoom
        self.guest1 = guest1
        self.receptionist5 = receptionist5 if receptionist5 is not None else set()
        
        pass
    @property
    def roomNo(self):
        return self.__roomNo
    @roomNo.setter
    def roomNo(self, roomNo: int):
        self.__roomNo = roomNo

    @property
    def typeOfRoom(self):
        return self.__typeOfRoom
    @typeOfRoom.setter
    def typeOfRoom(self, typeOfRoom: str):
        self.__typeOfRoom = typeOfRoom

    @property
    def RatesofRoom(self):
        return self.__RatesofRoom
    @RatesofRoom.setter
    def RatesofRoom(self, RatesofRoom: int):
        self.__RatesofRoom = RatesofRoom

    @property
    def receptionist5(self):
        return self.__receptionist5
    @receptionist5.setter
    def receptionist5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Room__receptionist5", None)
        self.__receptionist5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "room4"):
                    opp_val = getattr(item, "room4", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "room4"):
                    opp_val = getattr(item, "room4", None)
                    
                    if opp_val is None:
                        setattr(item, "room4", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def guest1(self):
        return self.__guest1
    @guest1.setter
    def guest1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Room__guest1", None)
        self.__guest1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room0"):
                opp_val = getattr(old_value, "room0", None)
                if opp_val == self:
                    setattr(old_value, "room0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room0"):
                opp_val = getattr(value, "room0", None)
                setattr(value, "room0", self)



class Manager:

    def __init__(self, id: int, name: str, receptionist9: set["Receptionist"] = None, inventory11: "Inventory" = None, database14: "Database" = None):
        self.id = id
        self.name = name
        self.receptionist9 = receptionist9 if receptionist9 is not None else set()
        self.inventory11 = inventory11
        self.database14 = database14
        
        pass
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def database14(self):
        return self.__database14
    @database14.setter
    def database14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Manager__database14", None)
        self.__database14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "manager15"):
                opp_val = getattr(old_value, "manager15", None)
                if opp_val == self:
                    setattr(old_value, "manager15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "manager15"):
                opp_val = getattr(value, "manager15", None)
                setattr(value, "manager15", self)

    @property
    def inventory11(self):
        return self.__inventory11
    @inventory11.setter
    def inventory11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Manager__inventory11", None)
        self.__inventory11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "manager10"):
                opp_val = getattr(old_value, "manager10", None)
                if opp_val == self:
                    setattr(old_value, "manager10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "manager10"):
                opp_val = getattr(value, "manager10", None)
                setattr(value, "manager10", self)

    @property
    def receptionist9(self):
        return self.__receptionist9
    @receptionist9.setter
    def receptionist9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Manager__receptionist9", None)
        self.__receptionist9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "manager8"):
                    opp_val = getattr(item, "manager8", None)
                    
                    if opp_val == self:
                        setattr(item, "manager8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "manager8"):
                    opp_val = getattr(item, "manager8", None)
                    
                    setattr(item, "manager8", self)
                    



class Receptionist:

    def __init__(self, Id: int, name: str, room4: set["Room"] = None, bill6: set["Bill"] = None, manager8: "Manager" = None, database12: "Database" = None):
        self.Id = Id
        self.name = name
        self.room4 = room4 if room4 is not None else set()
        self.bill6 = bill6 if bill6 is not None else set()
        self.manager8 = manager8
        self.database12 = database12
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Id(self):
        return self.__Id
    @Id.setter
    def Id(self, Id: int):
        self.__Id = Id

    @property
    def database12(self):
        return self.__database12
    @database12.setter
    def database12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Receptionist__database12", None)
        self.__database12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "receptionist13"):
                opp_val = getattr(old_value, "receptionist13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "receptionist13"):
                opp_val = getattr(value, "receptionist13", None)
                if opp_val is None:
                    setattr(value, "receptionist13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bill6(self):
        return self.__bill6
    @bill6.setter
    def bill6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Receptionist__bill6", None)
        self.__bill6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "receptionist7"):
                    opp_val = getattr(item, "receptionist7", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "receptionist7"):
                    opp_val = getattr(item, "receptionist7", None)
                    
                    if opp_val is None:
                        setattr(item, "receptionist7", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def room4(self):
        return self.__room4
    @room4.setter
    def room4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Receptionist__room4", None)
        self.__room4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "receptionist5"):
                    opp_val = getattr(item, "receptionist5", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "receptionist5"):
                    opp_val = getattr(item, "receptionist5", None)
                    
                    if opp_val is None:
                        setattr(item, "receptionist5", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def manager8(self):
        return self.__manager8
    @manager8.setter
    def manager8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Receptionist__manager8", None)
        self.__manager8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "receptionist9"):
                opp_val = getattr(old_value, "receptionist9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "receptionist9"):
                opp_val = getattr(value, "receptionist9", None)
                if opp_val is None:
                    setattr(value, "receptionist9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Guest:

    def __init__(self, name: str, id: int, phoneNo: int, Address: str, Room: int, credit_card: int, room0: "Room" = None, bill2: "Bill" = None):
        self.name = name
        self.id = id
        self.phoneNo = phoneNo
        self.Address = Address
        self.Room = Room
        self.credit_card = credit_card
        self.room0 = room0
        self.bill2 = bill2
        
        pass
    @property
    def phoneNo(self):
        return self.__phoneNo
    @phoneNo.setter
    def phoneNo(self, phoneNo: int):
        self.__phoneNo = phoneNo

    @property
    def credit_card(self):
        return self.__credit_card
    @credit_card.setter
    def credit_card(self, credit_card: int):
        self.__credit_card = credit_card

    @property
    def Address(self):
        return self.__Address
    @Address.setter
    def Address(self, Address: str):
        self.__Address = Address

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def Room(self):
        return self.__Room
    @Room.setter
    def Room(self, Room: int):
        self.__Room = Room

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def room0(self):
        return self.__room0
    @room0.setter
    def room0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Guest__room0", None)
        self.__room0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "guest1"):
                opp_val = getattr(old_value, "guest1", None)
                if opp_val == self:
                    setattr(old_value, "guest1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "guest1"):
                opp_val = getattr(value, "guest1", None)
                setattr(value, "guest1", self)

    @property
    def bill2(self):
        return self.__bill2
    @bill2.setter
    def bill2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Guest__bill2", None)
        self.__bill2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "guest3"):
                opp_val = getattr(old_value, "guest3", None)
                if opp_val == self:
                    setattr(old_value, "guest3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "guest3"):
                opp_val = getattr(value, "guest3", None)
                setattr(value, "guest3", self)

