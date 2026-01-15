from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class petrinet_Net:

    pass
class petrinet_Box:

    def __init__(self, id: int, name: str, petrinet_Box13: "petrinet_Net" = None, petrinet_Box15: set["petrinet_Place"] = None, petrinet_Box: "petrinet_Transition" = None):
        self.id = id
        self.name = name
        self.petrinet_Box13 = petrinet_Box13
        self.petrinet_Box15 = petrinet_Box15 if petrinet_Box15 is not None else set()
        self.petrinet_Box = petrinet_Box
        
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def petrinet_Box(self):
        return self.__petrinet_Box

    @petrinet_Box.setter
    def petrinet_Box(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Box__petrinet_Box", None)
        self.__petrinet_Box = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinet_Transition2"):
                opp_val = getattr(old_value, "petrinet_Transition2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinet_Transition2"):
                opp_val = getattr(value, "petrinet_Transition2", None)
                if opp_val is None:
                    setattr(value, "petrinet_Transition2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def petrinet_Box15(self):
        return self.__petrinet_Box15

    @petrinet_Box15.setter
    def petrinet_Box15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Box__petrinet_Box15", None)
        self.__petrinet_Box15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "petrinet_Place16"):
                    opp_val = getattr(item, "petrinet_Place16", None)
                    
                    if opp_val == self:
                        setattr(item, "petrinet_Place16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "petrinet_Place16"):
                    opp_val = getattr(item, "petrinet_Place16", None)
                    
                    setattr(item, "petrinet_Place16", self)
                    

    @property
    def petrinet_Box13(self):
        return self.__petrinet_Box13

    @petrinet_Box13.setter
    def petrinet_Box13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Box__petrinet_Box13", None)
        self.__petrinet_Box13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinet_Net12"):
                opp_val = getattr(old_value, "petrinet_Net12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinet_Net12"):
                opp_val = getattr(value, "petrinet_Net12", None)
                if opp_val is None:
                    setattr(value, "petrinet_Net12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class petrinet_Transition:

    def __init__(self, id: int, name: str, petrinet_Transition: "petrinet_Place" = None, petrinet_Transition2: set["petrinet_Box"] = None, petrinet_Transition4: set["petrinet_Place"] = None, petrinet_Transition10: "petrinet_Net" = None):
        self.id = id
        self.name = name
        self.petrinet_Transition = petrinet_Transition
        self.petrinet_Transition2 = petrinet_Transition2 if petrinet_Transition2 is not None else set()
        self.petrinet_Transition4 = petrinet_Transition4 if petrinet_Transition4 is not None else set()
        self.petrinet_Transition10 = petrinet_Transition10
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def petrinet_Transition10(self):
        return self.__petrinet_Transition10

    @petrinet_Transition10.setter
    def petrinet_Transition10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Transition__petrinet_Transition10", None)
        self.__petrinet_Transition10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinet_Net9"):
                opp_val = getattr(old_value, "petrinet_Net9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinet_Net9"):
                opp_val = getattr(value, "petrinet_Net9", None)
                if opp_val is None:
                    setattr(value, "petrinet_Net9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def petrinet_Transition(self):
        return self.__petrinet_Transition

    @petrinet_Transition.setter
    def petrinet_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Transition__petrinet_Transition", None)
        self.__petrinet_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinet_Place"):
                opp_val = getattr(old_value, "petrinet_Place", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinet_Place"):
                opp_val = getattr(value, "petrinet_Place", None)
                if opp_val is None:
                    setattr(value, "petrinet_Place", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def petrinet_Transition2(self):
        return self.__petrinet_Transition2

    @petrinet_Transition2.setter
    def petrinet_Transition2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Transition__petrinet_Transition2", None)
        self.__petrinet_Transition2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "petrinet_Box"):
                    opp_val = getattr(item, "petrinet_Box", None)
                    
                    if opp_val == self:
                        setattr(item, "petrinet_Box", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "petrinet_Box"):
                    opp_val = getattr(item, "petrinet_Box", None)
                    
                    setattr(item, "petrinet_Box", self)
                    

    @property
    def petrinet_Transition4(self):
        return self.__petrinet_Transition4

    @petrinet_Transition4.setter
    def petrinet_Transition4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Transition__petrinet_Transition4", None)
        self.__petrinet_Transition4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "petrinet_Place5"):
                    opp_val = getattr(item, "petrinet_Place5", None)
                    
                    if opp_val == self:
                        setattr(item, "petrinet_Place5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "petrinet_Place5"):
                    opp_val = getattr(item, "petrinet_Place5", None)
                    
                    setattr(item, "petrinet_Place5", self)
                    

class petrinet_Place:

    def __init__(self, id: int, name: str, petrinet_Place16: "petrinet_Box" = None, petrinet_Place: set["petrinet_Transition"] = None, petrinet_Place5: "petrinet_Transition" = None, petrinet_Place7: "petrinet_Net" = None):
        self.id = id
        self.name = name
        self.petrinet_Place16 = petrinet_Place16
        self.petrinet_Place = petrinet_Place if petrinet_Place is not None else set()
        self.petrinet_Place5 = petrinet_Place5
        self.petrinet_Place7 = petrinet_Place7
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def petrinet_Place5(self):
        return self.__petrinet_Place5

    @petrinet_Place5.setter
    def petrinet_Place5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Place__petrinet_Place5", None)
        self.__petrinet_Place5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinet_Transition4"):
                opp_val = getattr(old_value, "petrinet_Transition4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinet_Transition4"):
                opp_val = getattr(value, "petrinet_Transition4", None)
                if opp_val is None:
                    setattr(value, "petrinet_Transition4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def petrinet_Place(self):
        return self.__petrinet_Place

    @petrinet_Place.setter
    def petrinet_Place(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Place__petrinet_Place", None)
        self.__petrinet_Place = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "petrinet_Transition"):
                    opp_val = getattr(item, "petrinet_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "petrinet_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "petrinet_Transition"):
                    opp_val = getattr(item, "petrinet_Transition", None)
                    
                    setattr(item, "petrinet_Transition", self)
                    

    @property
    def petrinet_Place7(self):
        return self.__petrinet_Place7

    @petrinet_Place7.setter
    def petrinet_Place7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Place__petrinet_Place7", None)
        self.__petrinet_Place7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinet_Net"):
                opp_val = getattr(old_value, "petrinet_Net", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinet_Net"):
                opp_val = getattr(value, "petrinet_Net", None)
                if opp_val is None:
                    setattr(value, "petrinet_Net", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def petrinet_Place16(self):
        return self.__petrinet_Place16

    @petrinet_Place16.setter
    def petrinet_Place16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Place__petrinet_Place16", None)
        self.__petrinet_Place16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinet_Box15"):
                opp_val = getattr(old_value, "petrinet_Box15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinet_Box15"):
                opp_val = getattr(value, "petrinet_Box15", None)
                if opp_val is None:
                    setattr(value, "petrinet_Box15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
