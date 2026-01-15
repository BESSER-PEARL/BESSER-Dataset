from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class complworld_Thing:

    def __init__(self, name: str, complworld_Thing: "complworld_World" = None):
        self.name = name
        self.complworld_Thing = complworld_Thing
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def complworld_Thing(self):
        return self.__complworld_Thing

    @complworld_Thing.setter
    def complworld_Thing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_complworld_Thing__complworld_Thing", None)
        self.__complworld_Thing = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "complworld_World"):
                opp_val = getattr(old_value, "complworld_World", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "complworld_World"):
                opp_val = getattr(value, "complworld_World", None)
                if opp_val is None:
                    setattr(value, "complworld_World", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class complworld_World:

    pass
class complworld_Satellite:

    def __init__(self, name: str, complworld_Satellite: "complworld_Mars" = None):
        self.name = name
        self.complworld_Satellite = complworld_Satellite
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def complworld_Satellite(self):
        return self.__complworld_Satellite

    @complworld_Satellite.setter
    def complworld_Satellite(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_complworld_Satellite__complworld_Satellite", None)
        self.__complworld_Satellite = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "complworld_Mars"):
                opp_val = getattr(old_value, "complworld_Mars", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "complworld_Mars"):
                opp_val = getattr(value, "complworld_Mars", None)
                if opp_val is None:
                    setattr(value, "complworld_Mars", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class complworld_Mars:

    pass