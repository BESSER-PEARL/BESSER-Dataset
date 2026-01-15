from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class detachelist_Person:

    def __init__(self, name: str, detachelist_Person: "detachelist_Contacts" = None, detachelist_Person3: "detachelist_Contacts" = None, detachelist_Person6: "detachelist_Person" = None, detachelist_Person4: set["detachelist_Person"] = None):
        self.name = name
        self.detachelist_Person = detachelist_Person
        self.detachelist_Person3 = detachelist_Person3
        self.detachelist_Person6 = detachelist_Person6
        self.detachelist_Person4 = detachelist_Person4 if detachelist_Person4 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def detachelist_Person(self):
        return self.__detachelist_Person

    @detachelist_Person.setter
    def detachelist_Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_detachelist_Person__detachelist_Person", None)
        self.__detachelist_Person = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "detachelist_Contacts"):
                opp_val = getattr(old_value, "detachelist_Contacts", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "detachelist_Contacts"):
                opp_val = getattr(value, "detachelist_Contacts", None)
                if opp_val is None:
                    setattr(value, "detachelist_Contacts", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def detachelist_Person4(self):
        return self.__detachelist_Person4

    @detachelist_Person4.setter
    def detachelist_Person4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_detachelist_Person__detachelist_Person4", None)
        self.__detachelist_Person4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "detachelist_Person6"):
                    opp_val = getattr(item, "detachelist_Person6", None)
                    
                    if opp_val == self:
                        setattr(item, "detachelist_Person6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "detachelist_Person6"):
                    opp_val = getattr(item, "detachelist_Person6", None)
                    
                    setattr(item, "detachelist_Person6", self)
                    

    @property
    def detachelist_Person3(self):
        return self.__detachelist_Person3

    @detachelist_Person3.setter
    def detachelist_Person3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_detachelist_Person__detachelist_Person3", None)
        self.__detachelist_Person3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "detachelist_Contacts2"):
                opp_val = getattr(old_value, "detachelist_Contacts2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "detachelist_Contacts2"):
                opp_val = getattr(value, "detachelist_Contacts2", None)
                if opp_val is None:
                    setattr(value, "detachelist_Contacts2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def detachelist_Person6(self):
        return self.__detachelist_Person6

    @detachelist_Person6.setter
    def detachelist_Person6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_detachelist_Person__detachelist_Person6", None)
        self.__detachelist_Person6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "detachelist_Person4"):
                opp_val = getattr(old_value, "detachelist_Person4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "detachelist_Person4"):
                opp_val = getattr(value, "detachelist_Person4", None)
                if opp_val is None:
                    setattr(value, "detachelist_Person4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class detachelist_Contacts:

    pass