from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class myDsl_Features:

    def __init__(self, name: str, myDsl_Features: "myDsl_Type" = None, myDsl_Features7: "myDsl_Entity" = None):
        self.name = name
        self.myDsl_Features = myDsl_Features
        self.myDsl_Features7 = myDsl_Features7
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myDsl_Features(self):
        return self.__myDsl_Features

    @myDsl_Features.setter
    def myDsl_Features(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Features__myDsl_Features", None)
        self.__myDsl_Features = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Type2"):
                opp_val = getattr(old_value, "myDsl_Type2", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Type2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Type2"):
                opp_val = getattr(value, "myDsl_Type2", None)
                setattr(value, "myDsl_Type2", self)

    @property
    def myDsl_Features7(self):
        return self.__myDsl_Features7

    @myDsl_Features7.setter
    def myDsl_Features7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Features__myDsl_Features7", None)
        self.__myDsl_Features7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Entity6"):
                opp_val = getattr(old_value, "myDsl_Entity6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Entity6"):
                opp_val = getattr(value, "myDsl_Entity6", None)
                if opp_val is None:
                    setattr(value, "myDsl_Entity6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Type:

    pass
class myDsl_Entity(Type):

    pass
class myDsl_DataType(Type):

    pass
class myDsl_Type:

    def __init__(self, name: str, myDsl_Type: "myDsl_DomainModel" = None, myDsl_Type2: "myDsl_Features" = None):
        self.name = name
        self.myDsl_Type = myDsl_Type
        self.myDsl_Type2 = myDsl_Type2
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myDsl_Type2(self):
        return self.__myDsl_Type2

    @myDsl_Type2.setter
    def myDsl_Type2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Type__myDsl_Type2", None)
        self.__myDsl_Type2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Features"):
                opp_val = getattr(old_value, "myDsl_Features", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Features", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Features"):
                opp_val = getattr(value, "myDsl_Features", None)
                setattr(value, "myDsl_Features", self)

    @property
    def myDsl_Type(self):
        return self.__myDsl_Type

    @myDsl_Type.setter
    def myDsl_Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Type__myDsl_Type", None)
        self.__myDsl_Type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_DomainModel"):
                opp_val = getattr(old_value, "myDsl_DomainModel", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_DomainModel"):
                opp_val = getattr(value, "myDsl_DomainModel", None)
                if opp_val is None:
                    setattr(value, "myDsl_DomainModel", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class myDsl_DomainModel:

    pass