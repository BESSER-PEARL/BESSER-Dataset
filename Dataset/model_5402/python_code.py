from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class UML2_Class:

    def __init__(self, isActive: bool, UML2_Class: set["UML2_Reception"] = None):
        self.isActive = isActive
        self.UML2_Class = UML2_Class if UML2_Class is not None else set()
        
    @property
    def isActive(self) -> bool:
        return self.__isActive

    @isActive.setter
    def isActive(self, isActive: bool):
        self.__isActive = isActive

    @property
    def UML2_Class(self):
        return self.__UML2_Class

    @UML2_Class.setter
    def UML2_Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Class__UML2_Class", None)
        self.__UML2_Class = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2_Reception"):
                    opp_val = getattr(item, "UML2_Reception", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2_Reception", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2_Reception"):
                    opp_val = getattr(item, "UML2_Reception", None)
                    
                    setattr(item, "UML2_Reception", self)
                    

class UML2_Reception:

    pass