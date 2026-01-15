from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class basic2_Thing:

    def __init__(self, id: int, basic2_Thing3: "basic2_Thing" = None, basic2_Thing: "basic2_World" = None, basic2_Thing1: set["basic2_Thing"] = None):
        self.id = id
        self.basic2_Thing3 = basic2_Thing3
        self.basic2_Thing = basic2_Thing
        self.basic2_Thing1 = basic2_Thing1 if basic2_Thing1 is not None else set()
        
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def basic2_Thing1(self):
        return self.__basic2_Thing1

    @basic2_Thing1.setter
    def basic2_Thing1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basic2_Thing__basic2_Thing1", None)
        self.__basic2_Thing1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "basic2_Thing3"):
                    opp_val = getattr(item, "basic2_Thing3", None)
                    
                    if opp_val == self:
                        setattr(item, "basic2_Thing3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "basic2_Thing3"):
                    opp_val = getattr(item, "basic2_Thing3", None)
                    
                    setattr(item, "basic2_Thing3", self)
                    

    @property
    def basic2_Thing3(self):
        return self.__basic2_Thing3

    @basic2_Thing3.setter
    def basic2_Thing3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basic2_Thing__basic2_Thing3", None)
        self.__basic2_Thing3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "basic2_Thing1"):
                opp_val = getattr(old_value, "basic2_Thing1", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "basic2_Thing1"):
                opp_val = getattr(value, "basic2_Thing1", None)
                if opp_val is None:
                    setattr(value, "basic2_Thing1", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def basic2_Thing(self):
        return self.__basic2_Thing

    @basic2_Thing.setter
    def basic2_Thing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basic2_Thing__basic2_Thing", None)
        self.__basic2_Thing = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "basic2_World"):
                opp_val = getattr(old_value, "basic2_World", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "basic2_World"):
                opp_val = getattr(value, "basic2_World", None)
                if opp_val is None:
                    setattr(value, "basic2_World", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class basic2_World:

    pass