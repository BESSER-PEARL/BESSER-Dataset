from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Entity:

    pass
class my_AType(Entity):

    def __init__(self, my_AType: "my_BType" = None, my_AType5: "my_BType" = None):
        self.my_AType = my_AType
        self.my_AType5 = my_AType5
        
    @property
    def my_AType(self):
        return self.__my_AType

    @my_AType.setter
    def my_AType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_my_AType__my_AType", None)
        self.__my_AType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "my_BType2"):
                opp_val = getattr(old_value, "my_BType2", None)
                if opp_val == self:
                    setattr(old_value, "my_BType2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "my_BType2"):
                opp_val = getattr(value, "my_BType2", None)
                setattr(value, "my_BType2", self)

    @property
    def my_AType5(self):
        return self.__my_AType5

    @my_AType5.setter
    def my_AType5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_my_AType__my_AType5", None)
        self.__my_AType5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "my_BType4"):
                opp_val = getattr(old_value, "my_BType4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "my_BType4"):
                opp_val = getattr(value, "my_BType4", None)
                if opp_val is None:
                    setattr(value, "my_BType4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def referenced(self) -> str:
        # TODO: Implement referenced method
        pass

class my_BType(Entity):

    pass
class my_Model:

    pass
class my_Entity:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name
