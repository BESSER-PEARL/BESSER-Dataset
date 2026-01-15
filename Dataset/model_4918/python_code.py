from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Error:

    pass
class Message:

    pass
class BaseElement:

    pass
class services_services_Operation(BaseElement):

    def __init__(self, name: str, services_services_Operation: "Message" = None, services_services_Operation5: "Message" = None, services_services_Operation8: set["Error"] = None, services_services_Operation10: "services_services_EObject" = None):
        self.name = name
        self.services_services_Operation = services_services_Operation
        self.services_services_Operation5 = services_services_Operation5
        self.services_services_Operation8 = services_services_Operation8 if services_services_Operation8 is not None else set()
        self.services_services_Operation10 = services_services_Operation10
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def services_services_Operation5(self):
        return self.__services_services_Operation5

    @services_services_Operation5.setter
    def services_services_Operation5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_services_services_Operation__services_services_Operation5", None)
        self.__services_services_Operation5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Message6"):
                opp_val = getattr(old_value, "Message6", None)
                if opp_val == self:
                    setattr(old_value, "Message6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Message6"):
                opp_val = getattr(value, "Message6", None)
                setattr(value, "Message6", self)

    @property
    def services_services_Operation8(self):
        return self.__services_services_Operation8

    @services_services_Operation8.setter
    def services_services_Operation8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_services_services_Operation__services_services_Operation8", None)
        self.__services_services_Operation8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Error"):
                    opp_val = getattr(item, "Error", None)
                    
                    if opp_val == self:
                        setattr(item, "Error", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Error"):
                    opp_val = getattr(item, "Error", None)
                    
                    setattr(item, "Error", self)
                    

    @property
    def services_services_Operation10(self):
        return self.__services_services_Operation10

    @services_services_Operation10.setter
    def services_services_Operation10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_services_services_Operation__services_services_Operation10", None)
        self.__services_services_Operation10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "services_services_EObject11"):
                opp_val = getattr(old_value, "services_services_EObject11", None)
                if opp_val == self:
                    setattr(old_value, "services_services_EObject11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "services_services_EObject11"):
                opp_val = getattr(value, "services_services_EObject11", None)
                setattr(value, "services_services_EObject11", self)

    @property
    def services_services_Operation(self):
        return self.__services_services_Operation

    @services_services_Operation.setter
    def services_services_Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_services_services_Operation__services_services_Operation", None)
        self.__services_services_Operation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Message"):
                opp_val = getattr(old_value, "Message", None)
                if opp_val == self:
                    setattr(old_value, "Message", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Message"):
                opp_val = getattr(value, "Message", None)
                setattr(value, "Message", self)

class services_services_EObject:

    pass
class Operation:

    pass
class RootElement:

    pass
class services_services_Interface(RootElement):

    def __init__(self, name: str, services_services_Interface: set["Operation"] = None, services_services_Interface2: "services_services_EObject" = None):
        self.name = name
        self.services_services_Interface = services_services_Interface if services_services_Interface is not None else set()
        self.services_services_Interface2 = services_services_Interface2
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def services_services_Interface2(self):
        return self.__services_services_Interface2

    @services_services_Interface2.setter
    def services_services_Interface2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_services_services_Interface__services_services_Interface2", None)
        self.__services_services_Interface2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "services_services_EObject"):
                opp_val = getattr(old_value, "services_services_EObject", None)
                if opp_val == self:
                    setattr(old_value, "services_services_EObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "services_services_EObject"):
                opp_val = getattr(value, "services_services_EObject", None)
                setattr(value, "services_services_EObject", self)

    @property
    def services_services_Interface(self):
        return self.__services_services_Interface

    @services_services_Interface.setter
    def services_services_Interface(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_services_services_Interface__services_services_Interface", None)
        self.__services_services_Interface = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Operation"):
                    opp_val = getattr(item, "Operation", None)
                    
                    if opp_val == self:
                        setattr(item, "Operation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Operation"):
                    opp_val = getattr(item, "Operation", None)
                    
                    setattr(item, "Operation", self)
                    

class services_services_EndPoint(RootElement):

    pass