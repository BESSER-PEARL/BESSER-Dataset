from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class helloworld_Thing:

    def __init__(self, name: str, helloworld_Thing: "helloworld_World" = None, helloworld_Thing4: set["helloworld_Thing"] = None, helloworld_Thing3: "helloworld_Thing" = None, helloworld_Thing1: set["helloworld_Thing"] = None, helloworld_Thing6: "helloworld_Thing" = None):
        self.name = name
        self.helloworld_Thing = helloworld_Thing
        self.helloworld_Thing4 = helloworld_Thing4 if helloworld_Thing4 is not None else set()
        self.helloworld_Thing3 = helloworld_Thing3
        self.helloworld_Thing1 = helloworld_Thing1 if helloworld_Thing1 is not None else set()
        self.helloworld_Thing6 = helloworld_Thing6
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def helloworld_Thing1(self):
        return self.__helloworld_Thing1

    @helloworld_Thing1.setter
    def helloworld_Thing1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_helloworld_Thing__helloworld_Thing1", None)
        self.__helloworld_Thing1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "helloworld_Thing3"):
                    opp_val = getattr(item, "helloworld_Thing3", None)
                    
                    if opp_val == self:
                        setattr(item, "helloworld_Thing3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "helloworld_Thing3"):
                    opp_val = getattr(item, "helloworld_Thing3", None)
                    
                    setattr(item, "helloworld_Thing3", self)
                    

    @property
    def helloworld_Thing4(self):
        return self.__helloworld_Thing4

    @helloworld_Thing4.setter
    def helloworld_Thing4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_helloworld_Thing__helloworld_Thing4", None)
        self.__helloworld_Thing4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "helloworld_Thing6"):
                    opp_val = getattr(item, "helloworld_Thing6", None)
                    
                    if opp_val == self:
                        setattr(item, "helloworld_Thing6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "helloworld_Thing6"):
                    opp_val = getattr(item, "helloworld_Thing6", None)
                    
                    setattr(item, "helloworld_Thing6", self)
                    

    @property
    def helloworld_Thing(self):
        return self.__helloworld_Thing

    @helloworld_Thing.setter
    def helloworld_Thing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_helloworld_Thing__helloworld_Thing", None)
        self.__helloworld_Thing = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "helloworld_World"):
                opp_val = getattr(old_value, "helloworld_World", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "helloworld_World"):
                opp_val = getattr(value, "helloworld_World", None)
                if opp_val is None:
                    setattr(value, "helloworld_World", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def helloworld_Thing6(self):
        return self.__helloworld_Thing6

    @helloworld_Thing6.setter
    def helloworld_Thing6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_helloworld_Thing__helloworld_Thing6", None)
        self.__helloworld_Thing6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "helloworld_Thing4"):
                opp_val = getattr(old_value, "helloworld_Thing4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "helloworld_Thing4"):
                opp_val = getattr(value, "helloworld_Thing4", None)
                if opp_val is None:
                    setattr(value, "helloworld_Thing4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def helloworld_Thing3(self):
        return self.__helloworld_Thing3

    @helloworld_Thing3.setter
    def helloworld_Thing3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_helloworld_Thing__helloworld_Thing3", None)
        self.__helloworld_Thing3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "helloworld_Thing1"):
                opp_val = getattr(old_value, "helloworld_Thing1", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "helloworld_Thing1"):
                opp_val = getattr(value, "helloworld_Thing1", None)
                if opp_val is None:
                    setattr(value, "helloworld_Thing1", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class helloworld_World:

    pass