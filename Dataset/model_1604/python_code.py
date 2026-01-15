from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class petrinetDsl_Storage:

    def __init__(self, count: int, capacity: int, petrinetDsl_Storage: "petrinetDsl_Place" = None, petrinetDsl_Storage8: "petrinetDsl_Resource" = None):
        self.count = count
        self.capacity = capacity
        self.petrinetDsl_Storage = petrinetDsl_Storage
        self.petrinetDsl_Storage8 = petrinetDsl_Storage8
        
    @property
    def capacity(self) -> int:
        return self.__capacity

    @capacity.setter
    def capacity(self, capacity: int):
        self.__capacity = capacity

    @property
    def count(self) -> int:
        return self.__count

    @count.setter
    def count(self, count: int):
        self.__count = count

    @property
    def petrinetDsl_Storage8(self):
        return self.__petrinetDsl_Storage8

    @petrinetDsl_Storage8.setter
    def petrinetDsl_Storage8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinetDsl_Storage__petrinetDsl_Storage8", None)
        self.__petrinetDsl_Storage8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinetDsl_Resource9"):
                opp_val = getattr(old_value, "petrinetDsl_Resource9", None)
                if opp_val == self:
                    setattr(old_value, "petrinetDsl_Resource9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinetDsl_Resource9"):
                opp_val = getattr(value, "petrinetDsl_Resource9", None)
                setattr(value, "petrinetDsl_Resource9", self)

    @property
    def petrinetDsl_Storage(self):
        return self.__petrinetDsl_Storage

    @petrinetDsl_Storage.setter
    def petrinetDsl_Storage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinetDsl_Storage__petrinetDsl_Storage", None)
        self.__petrinetDsl_Storage = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinetDsl_Place6"):
                opp_val = getattr(old_value, "petrinetDsl_Place6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinetDsl_Place6"):
                opp_val = getattr(value, "petrinetDsl_Place6", None)
                if opp_val is None:
                    setattr(value, "petrinetDsl_Place6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class petrinetDsl_PutStatement:

    def __init__(self, count: int, petrinetDsl_PutStatement: "petrinetDsl_Transaction" = None, petrinetDsl_PutStatement32: "petrinetDsl_Place" = None, petrinetDsl_PutStatement29: "petrinetDsl_Resource" = None):
        self.count = count
        self.petrinetDsl_PutStatement = petrinetDsl_PutStatement
        self.petrinetDsl_PutStatement32 = petrinetDsl_PutStatement32
        self.petrinetDsl_PutStatement29 = petrinetDsl_PutStatement29
        
    @property
    def count(self) -> int:
        return self.__count

    @count.setter
    def count(self, count: int):
        self.__count = count

    @property
    def petrinetDsl_PutStatement(self):
        return self.__petrinetDsl_PutStatement

    @petrinetDsl_PutStatement.setter
    def petrinetDsl_PutStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinetDsl_PutStatement__petrinetDsl_PutStatement", None)
        self.__petrinetDsl_PutStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinetDsl_Transaction15"):
                opp_val = getattr(old_value, "petrinetDsl_Transaction15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinetDsl_Transaction15"):
                opp_val = getattr(value, "petrinetDsl_Transaction15", None)
                if opp_val is None:
                    setattr(value, "petrinetDsl_Transaction15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def petrinetDsl_PutStatement32(self):
        return self.__petrinetDsl_PutStatement32

    @petrinetDsl_PutStatement32.setter
    def petrinetDsl_PutStatement32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinetDsl_PutStatement__petrinetDsl_PutStatement32", None)
        self.__petrinetDsl_PutStatement32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinetDsl_Place33"):
                opp_val = getattr(old_value, "petrinetDsl_Place33", None)
                if opp_val == self:
                    setattr(old_value, "petrinetDsl_Place33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinetDsl_Place33"):
                opp_val = getattr(value, "petrinetDsl_Place33", None)
                setattr(value, "petrinetDsl_Place33", self)

    @property
    def petrinetDsl_PutStatement29(self):
        return self.__petrinetDsl_PutStatement29

    @petrinetDsl_PutStatement29.setter
    def petrinetDsl_PutStatement29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinetDsl_PutStatement__petrinetDsl_PutStatement29", None)
        self.__petrinetDsl_PutStatement29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinetDsl_Resource30"):
                opp_val = getattr(old_value, "petrinetDsl_Resource30", None)
                if opp_val == self:
                    setattr(old_value, "petrinetDsl_Resource30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinetDsl_Resource30"):
                opp_val = getattr(value, "petrinetDsl_Resource30", None)
                setattr(value, "petrinetDsl_Resource30", self)

class petrinetDsl_TakeStatement:

    def __init__(self, count: int, petrinetDsl_TakeStatement: "petrinetDsl_Transaction" = None, petrinetDsl_TakeStatement23: "petrinetDsl_Resource" = None, petrinetDsl_TakeStatement26: "petrinetDsl_Place" = None):
        self.count = count
        self.petrinetDsl_TakeStatement = petrinetDsl_TakeStatement
        self.petrinetDsl_TakeStatement23 = petrinetDsl_TakeStatement23
        self.petrinetDsl_TakeStatement26 = petrinetDsl_TakeStatement26
        
    @property
    def count(self) -> int:
        return self.__count

    @count.setter
    def count(self, count: int):
        self.__count = count

    @property
    def petrinetDsl_TakeStatement(self):
        return self.__petrinetDsl_TakeStatement

    @petrinetDsl_TakeStatement.setter
    def petrinetDsl_TakeStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinetDsl_TakeStatement__petrinetDsl_TakeStatement", None)
        self.__petrinetDsl_TakeStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinetDsl_Transaction13"):
                opp_val = getattr(old_value, "petrinetDsl_Transaction13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinetDsl_Transaction13"):
                opp_val = getattr(value, "petrinetDsl_Transaction13", None)
                if opp_val is None:
                    setattr(value, "petrinetDsl_Transaction13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def petrinetDsl_TakeStatement23(self):
        return self.__petrinetDsl_TakeStatement23

    @petrinetDsl_TakeStatement23.setter
    def petrinetDsl_TakeStatement23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinetDsl_TakeStatement__petrinetDsl_TakeStatement23", None)
        self.__petrinetDsl_TakeStatement23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinetDsl_Resource24"):
                opp_val = getattr(old_value, "petrinetDsl_Resource24", None)
                if opp_val == self:
                    setattr(old_value, "petrinetDsl_Resource24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinetDsl_Resource24"):
                opp_val = getattr(value, "petrinetDsl_Resource24", None)
                setattr(value, "petrinetDsl_Resource24", self)

    @property
    def petrinetDsl_TakeStatement26(self):
        return self.__petrinetDsl_TakeStatement26

    @petrinetDsl_TakeStatement26.setter
    def petrinetDsl_TakeStatement26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinetDsl_TakeStatement__petrinetDsl_TakeStatement26", None)
        self.__petrinetDsl_TakeStatement26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinetDsl_Place27"):
                opp_val = getattr(old_value, "petrinetDsl_Place27", None)
                if opp_val == self:
                    setattr(old_value, "petrinetDsl_Place27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinetDsl_Place27"):
                opp_val = getattr(value, "petrinetDsl_Place27", None)
                setattr(value, "petrinetDsl_Place27", self)

class petrinetDsl_AssureStatement:

    def __init__(self, count: int, petrinetDsl_AssureStatement: "petrinetDsl_Transaction" = None, petrinetDsl_AssureStatement17: "petrinetDsl_Resource" = None, petrinetDsl_AssureStatement20: "petrinetDsl_Place" = None):
        self.count = count
        self.petrinetDsl_AssureStatement = petrinetDsl_AssureStatement
        self.petrinetDsl_AssureStatement17 = petrinetDsl_AssureStatement17
        self.petrinetDsl_AssureStatement20 = petrinetDsl_AssureStatement20
        
    @property
    def count(self) -> int:
        return self.__count

    @count.setter
    def count(self, count: int):
        self.__count = count

    @property
    def petrinetDsl_AssureStatement20(self):
        return self.__petrinetDsl_AssureStatement20

    @petrinetDsl_AssureStatement20.setter
    def petrinetDsl_AssureStatement20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinetDsl_AssureStatement__petrinetDsl_AssureStatement20", None)
        self.__petrinetDsl_AssureStatement20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinetDsl_Place21"):
                opp_val = getattr(old_value, "petrinetDsl_Place21", None)
                if opp_val == self:
                    setattr(old_value, "petrinetDsl_Place21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinetDsl_Place21"):
                opp_val = getattr(value, "petrinetDsl_Place21", None)
                setattr(value, "petrinetDsl_Place21", self)

    @property
    def petrinetDsl_AssureStatement(self):
        return self.__petrinetDsl_AssureStatement

    @petrinetDsl_AssureStatement.setter
    def petrinetDsl_AssureStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinetDsl_AssureStatement__petrinetDsl_AssureStatement", None)
        self.__petrinetDsl_AssureStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinetDsl_Transaction11"):
                opp_val = getattr(old_value, "petrinetDsl_Transaction11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinetDsl_Transaction11"):
                opp_val = getattr(value, "petrinetDsl_Transaction11", None)
                if opp_val is None:
                    setattr(value, "petrinetDsl_Transaction11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def petrinetDsl_AssureStatement17(self):
        return self.__petrinetDsl_AssureStatement17

    @petrinetDsl_AssureStatement17.setter
    def petrinetDsl_AssureStatement17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinetDsl_AssureStatement__petrinetDsl_AssureStatement17", None)
        self.__petrinetDsl_AssureStatement17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinetDsl_Resource18"):
                opp_val = getattr(old_value, "petrinetDsl_Resource18", None)
                if opp_val == self:
                    setattr(old_value, "petrinetDsl_Resource18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinetDsl_Resource18"):
                opp_val = getattr(value, "petrinetDsl_Resource18", None)
                setattr(value, "petrinetDsl_Resource18", self)

class petrinetDsl_Transaction:

    def __init__(self, name: str, petrinetDsl_Transaction: "petrinetDsl_PetriNet" = None, petrinetDsl_Transaction11: set["petrinetDsl_AssureStatement"] = None, petrinetDsl_Transaction13: set["petrinetDsl_TakeStatement"] = None, petrinetDsl_Transaction15: set["petrinetDsl_PutStatement"] = None):
        self.name = name
        self.petrinetDsl_Transaction = petrinetDsl_Transaction
        self.petrinetDsl_Transaction11 = petrinetDsl_Transaction11 if petrinetDsl_Transaction11 is not None else set()
        self.petrinetDsl_Transaction13 = petrinetDsl_Transaction13 if petrinetDsl_Transaction13 is not None else set()
        self.petrinetDsl_Transaction15 = petrinetDsl_Transaction15 if petrinetDsl_Transaction15 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def petrinetDsl_Transaction11(self):
        return self.__petrinetDsl_Transaction11

    @petrinetDsl_Transaction11.setter
    def petrinetDsl_Transaction11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinetDsl_Transaction__petrinetDsl_Transaction11", None)
        self.__petrinetDsl_Transaction11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "petrinetDsl_AssureStatement"):
                    opp_val = getattr(item, "petrinetDsl_AssureStatement", None)
                    
                    if opp_val == self:
                        setattr(item, "petrinetDsl_AssureStatement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "petrinetDsl_AssureStatement"):
                    opp_val = getattr(item, "petrinetDsl_AssureStatement", None)
                    
                    setattr(item, "petrinetDsl_AssureStatement", self)
                    

    @property
    def petrinetDsl_Transaction15(self):
        return self.__petrinetDsl_Transaction15

    @petrinetDsl_Transaction15.setter
    def petrinetDsl_Transaction15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinetDsl_Transaction__petrinetDsl_Transaction15", None)
        self.__petrinetDsl_Transaction15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "petrinetDsl_PutStatement"):
                    opp_val = getattr(item, "petrinetDsl_PutStatement", None)
                    
                    if opp_val == self:
                        setattr(item, "petrinetDsl_PutStatement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "petrinetDsl_PutStatement"):
                    opp_val = getattr(item, "petrinetDsl_PutStatement", None)
                    
                    setattr(item, "petrinetDsl_PutStatement", self)
                    

    @property
    def petrinetDsl_Transaction(self):
        return self.__petrinetDsl_Transaction

    @petrinetDsl_Transaction.setter
    def petrinetDsl_Transaction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinetDsl_Transaction__petrinetDsl_Transaction", None)
        self.__petrinetDsl_Transaction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinetDsl_PetriNet4"):
                opp_val = getattr(old_value, "petrinetDsl_PetriNet4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinetDsl_PetriNet4"):
                opp_val = getattr(value, "petrinetDsl_PetriNet4", None)
                if opp_val is None:
                    setattr(value, "petrinetDsl_PetriNet4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def petrinetDsl_Transaction13(self):
        return self.__petrinetDsl_Transaction13

    @petrinetDsl_Transaction13.setter
    def petrinetDsl_Transaction13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinetDsl_Transaction__petrinetDsl_Transaction13", None)
        self.__petrinetDsl_Transaction13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "petrinetDsl_TakeStatement"):
                    opp_val = getattr(item, "petrinetDsl_TakeStatement", None)
                    
                    if opp_val == self:
                        setattr(item, "petrinetDsl_TakeStatement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "petrinetDsl_TakeStatement"):
                    opp_val = getattr(item, "petrinetDsl_TakeStatement", None)
                    
                    setattr(item, "petrinetDsl_TakeStatement", self)
                    

class petrinetDsl_Place:

    def __init__(self, name: str, petrinetDsl_Place: "petrinetDsl_PetriNet" = None, petrinetDsl_Place21: "petrinetDsl_AssureStatement" = None, petrinetDsl_Place6: set["petrinetDsl_Storage"] = None, petrinetDsl_Place33: "petrinetDsl_PutStatement" = None, petrinetDsl_Place27: "petrinetDsl_TakeStatement" = None):
        self.name = name
        self.petrinetDsl_Place = petrinetDsl_Place
        self.petrinetDsl_Place21 = petrinetDsl_Place21
        self.petrinetDsl_Place6 = petrinetDsl_Place6 if petrinetDsl_Place6 is not None else set()
        self.petrinetDsl_Place33 = petrinetDsl_Place33
        self.petrinetDsl_Place27 = petrinetDsl_Place27
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def petrinetDsl_Place21(self):
        return self.__petrinetDsl_Place21

    @petrinetDsl_Place21.setter
    def petrinetDsl_Place21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinetDsl_Place__petrinetDsl_Place21", None)
        self.__petrinetDsl_Place21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinetDsl_AssureStatement20"):
                opp_val = getattr(old_value, "petrinetDsl_AssureStatement20", None)
                if opp_val == self:
                    setattr(old_value, "petrinetDsl_AssureStatement20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinetDsl_AssureStatement20"):
                opp_val = getattr(value, "petrinetDsl_AssureStatement20", None)
                setattr(value, "petrinetDsl_AssureStatement20", self)

    @property
    def petrinetDsl_Place27(self):
        return self.__petrinetDsl_Place27

    @petrinetDsl_Place27.setter
    def petrinetDsl_Place27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinetDsl_Place__petrinetDsl_Place27", None)
        self.__petrinetDsl_Place27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinetDsl_TakeStatement26"):
                opp_val = getattr(old_value, "petrinetDsl_TakeStatement26", None)
                if opp_val == self:
                    setattr(old_value, "petrinetDsl_TakeStatement26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinetDsl_TakeStatement26"):
                opp_val = getattr(value, "petrinetDsl_TakeStatement26", None)
                setattr(value, "petrinetDsl_TakeStatement26", self)

    @property
    def petrinetDsl_Place33(self):
        return self.__petrinetDsl_Place33

    @petrinetDsl_Place33.setter
    def petrinetDsl_Place33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinetDsl_Place__petrinetDsl_Place33", None)
        self.__petrinetDsl_Place33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinetDsl_PutStatement32"):
                opp_val = getattr(old_value, "petrinetDsl_PutStatement32", None)
                if opp_val == self:
                    setattr(old_value, "petrinetDsl_PutStatement32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinetDsl_PutStatement32"):
                opp_val = getattr(value, "petrinetDsl_PutStatement32", None)
                setattr(value, "petrinetDsl_PutStatement32", self)

    @property
    def petrinetDsl_Place(self):
        return self.__petrinetDsl_Place

    @petrinetDsl_Place.setter
    def petrinetDsl_Place(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinetDsl_Place__petrinetDsl_Place", None)
        self.__petrinetDsl_Place = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinetDsl_PetriNet2"):
                opp_val = getattr(old_value, "petrinetDsl_PetriNet2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinetDsl_PetriNet2"):
                opp_val = getattr(value, "petrinetDsl_PetriNet2", None)
                if opp_val is None:
                    setattr(value, "petrinetDsl_PetriNet2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def petrinetDsl_Place6(self):
        return self.__petrinetDsl_Place6

    @petrinetDsl_Place6.setter
    def petrinetDsl_Place6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinetDsl_Place__petrinetDsl_Place6", None)
        self.__petrinetDsl_Place6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "petrinetDsl_Storage"):
                    opp_val = getattr(item, "petrinetDsl_Storage", None)
                    
                    if opp_val == self:
                        setattr(item, "petrinetDsl_Storage", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "petrinetDsl_Storage"):
                    opp_val = getattr(item, "petrinetDsl_Storage", None)
                    
                    setattr(item, "petrinetDsl_Storage", self)
                    

class petrinetDsl_Resource:

    def __init__(self, name: str, petrinetDsl_Resource: "petrinetDsl_PetriNet" = None, petrinetDsl_Resource18: "petrinetDsl_AssureStatement" = None, petrinetDsl_Resource9: "petrinetDsl_Storage" = None, petrinetDsl_Resource24: "petrinetDsl_TakeStatement" = None, petrinetDsl_Resource30: "petrinetDsl_PutStatement" = None):
        self.name = name
        self.petrinetDsl_Resource = petrinetDsl_Resource
        self.petrinetDsl_Resource18 = petrinetDsl_Resource18
        self.petrinetDsl_Resource9 = petrinetDsl_Resource9
        self.petrinetDsl_Resource24 = petrinetDsl_Resource24
        self.petrinetDsl_Resource30 = petrinetDsl_Resource30
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def petrinetDsl_Resource(self):
        return self.__petrinetDsl_Resource

    @petrinetDsl_Resource.setter
    def petrinetDsl_Resource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinetDsl_Resource__petrinetDsl_Resource", None)
        self.__petrinetDsl_Resource = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinetDsl_PetriNet"):
                opp_val = getattr(old_value, "petrinetDsl_PetriNet", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinetDsl_PetriNet"):
                opp_val = getattr(value, "petrinetDsl_PetriNet", None)
                if opp_val is None:
                    setattr(value, "petrinetDsl_PetriNet", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def petrinetDsl_Resource9(self):
        return self.__petrinetDsl_Resource9

    @petrinetDsl_Resource9.setter
    def petrinetDsl_Resource9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinetDsl_Resource__petrinetDsl_Resource9", None)
        self.__petrinetDsl_Resource9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinetDsl_Storage8"):
                opp_val = getattr(old_value, "petrinetDsl_Storage8", None)
                if opp_val == self:
                    setattr(old_value, "petrinetDsl_Storage8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinetDsl_Storage8"):
                opp_val = getattr(value, "petrinetDsl_Storage8", None)
                setattr(value, "petrinetDsl_Storage8", self)

    @property
    def petrinetDsl_Resource24(self):
        return self.__petrinetDsl_Resource24

    @petrinetDsl_Resource24.setter
    def petrinetDsl_Resource24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinetDsl_Resource__petrinetDsl_Resource24", None)
        self.__petrinetDsl_Resource24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinetDsl_TakeStatement23"):
                opp_val = getattr(old_value, "petrinetDsl_TakeStatement23", None)
                if opp_val == self:
                    setattr(old_value, "petrinetDsl_TakeStatement23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinetDsl_TakeStatement23"):
                opp_val = getattr(value, "petrinetDsl_TakeStatement23", None)
                setattr(value, "petrinetDsl_TakeStatement23", self)

    @property
    def petrinetDsl_Resource30(self):
        return self.__petrinetDsl_Resource30

    @petrinetDsl_Resource30.setter
    def petrinetDsl_Resource30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinetDsl_Resource__petrinetDsl_Resource30", None)
        self.__petrinetDsl_Resource30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinetDsl_PutStatement29"):
                opp_val = getattr(old_value, "petrinetDsl_PutStatement29", None)
                if opp_val == self:
                    setattr(old_value, "petrinetDsl_PutStatement29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinetDsl_PutStatement29"):
                opp_val = getattr(value, "petrinetDsl_PutStatement29", None)
                setattr(value, "petrinetDsl_PutStatement29", self)

    @property
    def petrinetDsl_Resource18(self):
        return self.__petrinetDsl_Resource18

    @petrinetDsl_Resource18.setter
    def petrinetDsl_Resource18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinetDsl_Resource__petrinetDsl_Resource18", None)
        self.__petrinetDsl_Resource18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinetDsl_AssureStatement17"):
                opp_val = getattr(old_value, "petrinetDsl_AssureStatement17", None)
                if opp_val == self:
                    setattr(old_value, "petrinetDsl_AssureStatement17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinetDsl_AssureStatement17"):
                opp_val = getattr(value, "petrinetDsl_AssureStatement17", None)
                setattr(value, "petrinetDsl_AssureStatement17", self)

class petrinetDsl_PetriNet:

    pass