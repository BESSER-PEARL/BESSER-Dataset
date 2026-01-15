from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class compartments_ChildOfB_F:

    def __init__(self, name: str, compartments_ChildOfB_F15: "compartments_ChildOfA_D" = None, compartments_ChildOfB_F: "compartments_TopNodeB" = None):
        self.name = name
        self.compartments_ChildOfB_F15 = compartments_ChildOfB_F15
        self.compartments_ChildOfB_F = compartments_ChildOfB_F
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def compartments_ChildOfB_F(self):
        return self.__compartments_ChildOfB_F

    @compartments_ChildOfB_F.setter
    def compartments_ChildOfB_F(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_compartments_ChildOfB_F__compartments_ChildOfB_F", None)
        self.__compartments_ChildOfB_F = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "compartments_TopNodeB8"):
                opp_val = getattr(old_value, "compartments_TopNodeB8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "compartments_TopNodeB8"):
                opp_val = getattr(value, "compartments_TopNodeB8", None)
                if opp_val is None:
                    setattr(value, "compartments_TopNodeB8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def compartments_ChildOfB_F15(self):
        return self.__compartments_ChildOfB_F15

    @compartments_ChildOfB_F15.setter
    def compartments_ChildOfB_F15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_compartments_ChildOfB_F__compartments_ChildOfB_F15", None)
        self.__compartments_ChildOfB_F15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "compartments_ChildOfA_D16"):
                opp_val = getattr(old_value, "compartments_ChildOfA_D16", None)
                if opp_val == self:
                    setattr(old_value, "compartments_ChildOfA_D16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "compartments_ChildOfA_D16"):
                opp_val = getattr(value, "compartments_ChildOfA_D16", None)
                setattr(value, "compartments_ChildOfA_D16", self)

class compartments_ChildOfAffixed:

    def __init__(self, description: str, compartments_ChildOfAffixed: "compartments_ChildOfB_G" = None):
        self.description = description
        self.compartments_ChildOfAffixed = compartments_ChildOfAffixed
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def compartments_ChildOfAffixed(self):
        return self.__compartments_ChildOfAffixed

    @compartments_ChildOfAffixed.setter
    def compartments_ChildOfAffixed(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_compartments_ChildOfAffixed__compartments_ChildOfAffixed", None)
        self.__compartments_ChildOfAffixed = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "compartments_ChildOfB_G13"):
                opp_val = getattr(old_value, "compartments_ChildOfB_G13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "compartments_ChildOfB_G13"):
                opp_val = getattr(value, "compartments_ChildOfB_G13", None)
                if opp_val is None:
                    setattr(value, "compartments_ChildOfB_G13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class compartments_ChildOfA_D:

    def __init__(self, name: str, compartments_ChildOfA_D: "compartments_TopNodeA" = None, compartments_ChildOfA_D16: "compartments_ChildOfB_F" = None):
        self.name = name
        self.compartments_ChildOfA_D = compartments_ChildOfA_D
        self.compartments_ChildOfA_D16 = compartments_ChildOfA_D16
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def compartments_ChildOfA_D(self):
        return self.__compartments_ChildOfA_D

    @compartments_ChildOfA_D.setter
    def compartments_ChildOfA_D(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_compartments_ChildOfA_D__compartments_ChildOfA_D", None)
        self.__compartments_ChildOfA_D = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "compartments_TopNodeA3"):
                opp_val = getattr(old_value, "compartments_TopNodeA3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "compartments_TopNodeA3"):
                opp_val = getattr(value, "compartments_TopNodeA3", None)
                if opp_val is None:
                    setattr(value, "compartments_TopNodeA3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def compartments_ChildOfA_D16(self):
        return self.__compartments_ChildOfA_D16

    @compartments_ChildOfA_D16.setter
    def compartments_ChildOfA_D16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_compartments_ChildOfA_D__compartments_ChildOfA_D16", None)
        self.__compartments_ChildOfA_D16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "compartments_ChildOfB_F15"):
                opp_val = getattr(old_value, "compartments_ChildOfB_F15", None)
                if opp_val == self:
                    setattr(old_value, "compartments_ChildOfB_F15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "compartments_ChildOfB_F15"):
                opp_val = getattr(value, "compartments_ChildOfB_F15", None)
                setattr(value, "compartments_ChildOfB_F15", self)

class compartments_ChildOfA_C:

    def __init__(self, name: str, compartments_ChildOfA_C: "compartments_TopNodeA" = None, compartments_ChildOfA_C11: "compartments_ChildOfB_E" = None):
        self.name = name
        self.compartments_ChildOfA_C = compartments_ChildOfA_C
        self.compartments_ChildOfA_C11 = compartments_ChildOfA_C11
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def compartments_ChildOfA_C11(self):
        return self.__compartments_ChildOfA_C11

    @compartments_ChildOfA_C11.setter
    def compartments_ChildOfA_C11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_compartments_ChildOfA_C__compartments_ChildOfA_C11", None)
        self.__compartments_ChildOfA_C11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "compartments_ChildOfB_E10"):
                opp_val = getattr(old_value, "compartments_ChildOfB_E10", None)
                if opp_val == self:
                    setattr(old_value, "compartments_ChildOfB_E10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "compartments_ChildOfB_E10"):
                opp_val = getattr(value, "compartments_ChildOfB_E10", None)
                setattr(value, "compartments_ChildOfB_E10", self)

    @property
    def compartments_ChildOfA_C(self):
        return self.__compartments_ChildOfA_C

    @compartments_ChildOfA_C.setter
    def compartments_ChildOfA_C(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_compartments_ChildOfA_C__compartments_ChildOfA_C", None)
        self.__compartments_ChildOfA_C = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "compartments_TopNodeA"):
                opp_val = getattr(old_value, "compartments_TopNodeA", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "compartments_TopNodeA"):
                opp_val = getattr(value, "compartments_TopNodeA", None)
                if opp_val is None:
                    setattr(value, "compartments_TopNodeA", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class compartments_ChildOfB_G:

    def __init__(self, number: int, compartments_ChildOfB_G: "compartments_TopNodeB" = None, compartments_ChildOfB_G13: set["compartments_ChildOfAffixed"] = None):
        self.number = number
        self.compartments_ChildOfB_G = compartments_ChildOfB_G
        self.compartments_ChildOfB_G13 = compartments_ChildOfB_G13 if compartments_ChildOfB_G13 is not None else set()
        
    @property
    def number(self) -> int:
        return self.__number

    @number.setter
    def number(self, number: int):
        self.__number = number

    @property
    def compartments_ChildOfB_G(self):
        return self.__compartments_ChildOfB_G

    @compartments_ChildOfB_G.setter
    def compartments_ChildOfB_G(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_compartments_ChildOfB_G__compartments_ChildOfB_G", None)
        self.__compartments_ChildOfB_G = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "compartments_TopNodeB6"):
                opp_val = getattr(old_value, "compartments_TopNodeB6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "compartments_TopNodeB6"):
                opp_val = getattr(value, "compartments_TopNodeB6", None)
                if opp_val is None:
                    setattr(value, "compartments_TopNodeB6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def compartments_ChildOfB_G13(self):
        return self.__compartments_ChildOfB_G13

    @compartments_ChildOfB_G13.setter
    def compartments_ChildOfB_G13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_compartments_ChildOfB_G__compartments_ChildOfB_G13", None)
        self.__compartments_ChildOfB_G13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "compartments_ChildOfAffixed"):
                    opp_val = getattr(item, "compartments_ChildOfAffixed", None)
                    
                    if opp_val == self:
                        setattr(item, "compartments_ChildOfAffixed", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "compartments_ChildOfAffixed"):
                    opp_val = getattr(item, "compartments_ChildOfAffixed", None)
                    
                    setattr(item, "compartments_ChildOfAffixed", self)
                    

class compartments_ChildOfB_E:

    def __init__(self, name: str, compartments_ChildOfB_E: "compartments_TopNodeB" = None, compartments_ChildOfB_E10: "compartments_ChildOfA_C" = None):
        self.name = name
        self.compartments_ChildOfB_E = compartments_ChildOfB_E
        self.compartments_ChildOfB_E10 = compartments_ChildOfB_E10
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def compartments_ChildOfB_E10(self):
        return self.__compartments_ChildOfB_E10

    @compartments_ChildOfB_E10.setter
    def compartments_ChildOfB_E10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_compartments_ChildOfB_E__compartments_ChildOfB_E10", None)
        self.__compartments_ChildOfB_E10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "compartments_ChildOfA_C11"):
                opp_val = getattr(old_value, "compartments_ChildOfA_C11", None)
                if opp_val == self:
                    setattr(old_value, "compartments_ChildOfA_C11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "compartments_ChildOfA_C11"):
                opp_val = getattr(value, "compartments_ChildOfA_C11", None)
                setattr(value, "compartments_ChildOfA_C11", self)

    @property
    def compartments_ChildOfB_E(self):
        return self.__compartments_ChildOfB_E

    @compartments_ChildOfB_E.setter
    def compartments_ChildOfB_E(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_compartments_ChildOfB_E__compartments_ChildOfB_E", None)
        self.__compartments_ChildOfB_E = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "compartments_TopNodeB"):
                opp_val = getattr(old_value, "compartments_TopNodeB", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "compartments_TopNodeB"):
                opp_val = getattr(value, "compartments_TopNodeB", None)
                if opp_val is None:
                    setattr(value, "compartments_TopNodeB", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class TopNode:

    pass
class compartments_TopNodeB(TopNode):

    def __init__(self, name: str, compartments_TopNodeB: set["compartments_ChildOfB_E"] = None, compartments_TopNodeB6: set["compartments_ChildOfB_G"] = None, compartments_TopNodeB8: set["compartments_ChildOfB_F"] = None):
        self.name = name
        self.compartments_TopNodeB = compartments_TopNodeB if compartments_TopNodeB is not None else set()
        self.compartments_TopNodeB6 = compartments_TopNodeB6 if compartments_TopNodeB6 is not None else set()
        self.compartments_TopNodeB8 = compartments_TopNodeB8 if compartments_TopNodeB8 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def compartments_TopNodeB6(self):
        return self.__compartments_TopNodeB6

    @compartments_TopNodeB6.setter
    def compartments_TopNodeB6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_compartments_TopNodeB__compartments_TopNodeB6", None)
        self.__compartments_TopNodeB6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "compartments_ChildOfB_G"):
                    opp_val = getattr(item, "compartments_ChildOfB_G", None)
                    
                    if opp_val == self:
                        setattr(item, "compartments_ChildOfB_G", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "compartments_ChildOfB_G"):
                    opp_val = getattr(item, "compartments_ChildOfB_G", None)
                    
                    setattr(item, "compartments_ChildOfB_G", self)
                    

    @property
    def compartments_TopNodeB8(self):
        return self.__compartments_TopNodeB8

    @compartments_TopNodeB8.setter
    def compartments_TopNodeB8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_compartments_TopNodeB__compartments_TopNodeB8", None)
        self.__compartments_TopNodeB8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "compartments_ChildOfB_F"):
                    opp_val = getattr(item, "compartments_ChildOfB_F", None)
                    
                    if opp_val == self:
                        setattr(item, "compartments_ChildOfB_F", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "compartments_ChildOfB_F"):
                    opp_val = getattr(item, "compartments_ChildOfB_F", None)
                    
                    setattr(item, "compartments_ChildOfB_F", self)
                    

    @property
    def compartments_TopNodeB(self):
        return self.__compartments_TopNodeB

    @compartments_TopNodeB.setter
    def compartments_TopNodeB(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_compartments_TopNodeB__compartments_TopNodeB", None)
        self.__compartments_TopNodeB = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "compartments_ChildOfB_E"):
                    opp_val = getattr(item, "compartments_ChildOfB_E", None)
                    
                    if opp_val == self:
                        setattr(item, "compartments_ChildOfB_E", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "compartments_ChildOfB_E"):
                    opp_val = getattr(item, "compartments_ChildOfB_E", None)
                    
                    setattr(item, "compartments_ChildOfB_E", self)
                    

class compartments_TopNodeA(TopNode):

    def __init__(self, name: str, compartments_TopNodeA: set["compartments_ChildOfA_C"] = None, compartments_TopNodeA3: set["compartments_ChildOfA_D"] = None):
        self.name = name
        self.compartments_TopNodeA = compartments_TopNodeA if compartments_TopNodeA is not None else set()
        self.compartments_TopNodeA3 = compartments_TopNodeA3 if compartments_TopNodeA3 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def compartments_TopNodeA3(self):
        return self.__compartments_TopNodeA3

    @compartments_TopNodeA3.setter
    def compartments_TopNodeA3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_compartments_TopNodeA__compartments_TopNodeA3", None)
        self.__compartments_TopNodeA3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "compartments_ChildOfA_D"):
                    opp_val = getattr(item, "compartments_ChildOfA_D", None)
                    
                    if opp_val == self:
                        setattr(item, "compartments_ChildOfA_D", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "compartments_ChildOfA_D"):
                    opp_val = getattr(item, "compartments_ChildOfA_D", None)
                    
                    setattr(item, "compartments_ChildOfA_D", self)
                    

    @property
    def compartments_TopNodeA(self):
        return self.__compartments_TopNodeA

    @compartments_TopNodeA.setter
    def compartments_TopNodeA(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_compartments_TopNodeA__compartments_TopNodeA", None)
        self.__compartments_TopNodeA = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "compartments_ChildOfA_C"):
                    opp_val = getattr(item, "compartments_ChildOfA_C", None)
                    
                    if opp_val == self:
                        setattr(item, "compartments_ChildOfA_C", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "compartments_ChildOfA_C"):
                    opp_val = getattr(item, "compartments_ChildOfA_C", None)
                    
                    setattr(item, "compartments_ChildOfA_C", self)
                    

class compartments_TopNode:

    pass
class compartments_Canvas:

    pass