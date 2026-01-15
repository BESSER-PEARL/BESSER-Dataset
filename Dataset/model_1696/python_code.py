from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class stuff_World:

    pass
class stuff_Property:

    def __init__(self, name: str, intrinsic: bool, stuff_Property: "stuff_Thing" = None, stuff_Property5: "stuff_World" = None):
        self.name = name
        self.intrinsic = intrinsic
        self.stuff_Property = stuff_Property
        self.stuff_Property5 = stuff_Property5
        
    @property
    def intrinsic(self) -> bool:
        return self.__intrinsic

    @intrinsic.setter
    def intrinsic(self, intrinsic: bool):
        self.__intrinsic = intrinsic

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def stuff_Property5(self):
        return self.__stuff_Property5

    @stuff_Property5.setter
    def stuff_Property5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stuff_Property__stuff_Property5", None)
        self.__stuff_Property5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stuff_World4"):
                opp_val = getattr(old_value, "stuff_World4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stuff_World4"):
                opp_val = getattr(value, "stuff_World4", None)
                if opp_val is None:
                    setattr(value, "stuff_World4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def stuff_Property(self):
        return self.__stuff_Property

    @stuff_Property.setter
    def stuff_Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stuff_Property__stuff_Property", None)
        self.__stuff_Property = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stuff_Thing"):
                opp_val = getattr(old_value, "stuff_Thing", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stuff_Thing"):
                opp_val = getattr(value, "stuff_Thing", None)
                if opp_val is None:
                    setattr(value, "stuff_Thing", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class stuff_Thing:

    def __init__(self, name: str, stuff_Thing: set["stuff_Property"] = None, stuff_Thing2: "stuff_World" = None):
        self.name = name
        self.stuff_Thing = stuff_Thing if stuff_Thing is not None else set()
        self.stuff_Thing2 = stuff_Thing2
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def stuff_Thing2(self):
        return self.__stuff_Thing2

    @stuff_Thing2.setter
    def stuff_Thing2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stuff_Thing__stuff_Thing2", None)
        self.__stuff_Thing2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stuff_World"):
                opp_val = getattr(old_value, "stuff_World", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stuff_World"):
                opp_val = getattr(value, "stuff_World", None)
                if opp_val is None:
                    setattr(value, "stuff_World", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def stuff_Thing(self):
        return self.__stuff_Thing

    @stuff_Thing.setter
    def stuff_Thing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stuff_Thing__stuff_Thing", None)
        self.__stuff_Thing = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "stuff_Property"):
                    opp_val = getattr(item, "stuff_Property", None)
                    
                    if opp_val == self:
                        setattr(item, "stuff_Property", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "stuff_Property"):
                    opp_val = getattr(item, "stuff_Property", None)
                    
                    setattr(item, "stuff_Property", self)
                    
