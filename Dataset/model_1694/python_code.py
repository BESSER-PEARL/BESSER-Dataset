from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class helloworld1_Thing:

    def __init__(self, id: int, helloworld1_Thing: "helloworld1_World" = None, helloworld1_Thing3: "helloworld1_Thing" = None, helloworld1_Thing1: set["helloworld1_Thing"] = None):
        self.id = id
        self.helloworld1_Thing = helloworld1_Thing
        self.helloworld1_Thing3 = helloworld1_Thing3
        self.helloworld1_Thing1 = helloworld1_Thing1 if helloworld1_Thing1 is not None else set()
        
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def helloworld1_Thing1(self):
        return self.__helloworld1_Thing1

    @helloworld1_Thing1.setter
    def helloworld1_Thing1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_helloworld1_Thing__helloworld1_Thing1", None)
        self.__helloworld1_Thing1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "helloworld1_Thing3"):
                    opp_val = getattr(item, "helloworld1_Thing3", None)
                    
                    if opp_val == self:
                        setattr(item, "helloworld1_Thing3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "helloworld1_Thing3"):
                    opp_val = getattr(item, "helloworld1_Thing3", None)
                    
                    setattr(item, "helloworld1_Thing3", self)
                    

    @property
    def helloworld1_Thing(self):
        return self.__helloworld1_Thing

    @helloworld1_Thing.setter
    def helloworld1_Thing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_helloworld1_Thing__helloworld1_Thing", None)
        self.__helloworld1_Thing = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "helloworld1_World"):
                opp_val = getattr(old_value, "helloworld1_World", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "helloworld1_World"):
                opp_val = getattr(value, "helloworld1_World", None)
                if opp_val is None:
                    setattr(value, "helloworld1_World", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def helloworld1_Thing3(self):
        return self.__helloworld1_Thing3

    @helloworld1_Thing3.setter
    def helloworld1_Thing3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_helloworld1_Thing__helloworld1_Thing3", None)
        self.__helloworld1_Thing3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "helloworld1_Thing1"):
                opp_val = getattr(old_value, "helloworld1_Thing1", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "helloworld1_Thing1"):
                opp_val = getattr(value, "helloworld1_Thing1", None)
                if opp_val is None:
                    setattr(value, "helloworld1_Thing1", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class helloworld1_World:

    pass