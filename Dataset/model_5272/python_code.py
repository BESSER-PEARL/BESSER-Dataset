from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class AddBindingTarget_Type3:

    pass
class AddBindingTarget_Type2:

    def __init__(self, name: str, AddBindingTarget_Type2: "AddBindingTarget_Type1" = None):
        self.name = name
        self.AddBindingTarget_Type2 = AddBindingTarget_Type2
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def AddBindingTarget_Type2(self):
        return self.__AddBindingTarget_Type2

    @AddBindingTarget_Type2.setter
    def AddBindingTarget_Type2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_AddBindingTarget_Type2__AddBindingTarget_Type2", None)
        self.__AddBindingTarget_Type2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AddBindingTarget_Type1"):
                opp_val = getattr(old_value, "AddBindingTarget_Type1", None)
                if opp_val == self:
                    setattr(old_value, "AddBindingTarget_Type1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AddBindingTarget_Type1"):
                opp_val = getattr(value, "AddBindingTarget_Type1", None)
                setattr(value, "AddBindingTarget_Type1", self)

class AddBindingTarget_Type1:

    def __init__(self, name: str, AddBindingTarget_Type1: "AddBindingTarget_Type2" = None, AddBindingTarget_Type12: "AddBindingTarget_Type3" = None):
        self.name = name
        self.AddBindingTarget_Type1 = AddBindingTarget_Type1
        self.AddBindingTarget_Type12 = AddBindingTarget_Type12
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def AddBindingTarget_Type12(self):
        return self.__AddBindingTarget_Type12

    @AddBindingTarget_Type12.setter
    def AddBindingTarget_Type12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_AddBindingTarget_Type1__AddBindingTarget_Type12", None)
        self.__AddBindingTarget_Type12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AddBindingTarget_Type3"):
                opp_val = getattr(old_value, "AddBindingTarget_Type3", None)
                if opp_val == self:
                    setattr(old_value, "AddBindingTarget_Type3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AddBindingTarget_Type3"):
                opp_val = getattr(value, "AddBindingTarget_Type3", None)
                setattr(value, "AddBindingTarget_Type3", self)

    @property
    def AddBindingTarget_Type1(self):
        return self.__AddBindingTarget_Type1

    @AddBindingTarget_Type1.setter
    def AddBindingTarget_Type1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_AddBindingTarget_Type1__AddBindingTarget_Type1", None)
        self.__AddBindingTarget_Type1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AddBindingTarget_Type2"):
                opp_val = getattr(old_value, "AddBindingTarget_Type2", None)
                if opp_val == self:
                    setattr(old_value, "AddBindingTarget_Type2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AddBindingTarget_Type2"):
                opp_val = getattr(value, "AddBindingTarget_Type2", None)
                setattr(value, "AddBindingTarget_Type2", self)
