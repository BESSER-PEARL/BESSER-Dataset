from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class myDsl_Feature:

    def __init__(self, many: bool, name: str, myDsl_Feature: "myDsl_Entity" = None, myDsl_Feature6: "myDsl_Type" = None):
        self.many = many
        self.name = name
        self.myDsl_Feature = myDsl_Feature
        self.myDsl_Feature6 = myDsl_Feature6
        
    @property
    def many(self) -> bool:
        return self.__many

    @many.setter
    def many(self, many: bool):
        self.__many = many

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myDsl_Feature6(self):
        return self.__myDsl_Feature6

    @myDsl_Feature6.setter
    def myDsl_Feature6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Feature__myDsl_Feature6", None)
        self.__myDsl_Feature6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Type7"):
                opp_val = getattr(old_value, "myDsl_Type7", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Type7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Type7"):
                opp_val = getattr(value, "myDsl_Type7", None)
                setattr(value, "myDsl_Type7", self)

    @property
    def myDsl_Feature(self):
        return self.__myDsl_Feature

    @myDsl_Feature.setter
    def myDsl_Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Feature__myDsl_Feature", None)
        self.__myDsl_Feature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Entity4"):
                opp_val = getattr(old_value, "myDsl_Entity4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Entity4"):
                opp_val = getattr(value, "myDsl_Entity4", None)
                if opp_val is None:
                    setattr(value, "myDsl_Entity4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Type:

    pass
class myDsl_Entity(Type):

    pass
class myDsl_DataType(Type):

    pass
class myDsl_Type:

    def __init__(self, name: str, myDsl_Type: "myDsl_Domainmodel" = None, myDsl_Type7: "myDsl_Feature" = None):
        self.name = name
        self.myDsl_Type = myDsl_Type
        self.myDsl_Type7 = myDsl_Type7
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myDsl_Type7(self):
        return self.__myDsl_Type7

    @myDsl_Type7.setter
    def myDsl_Type7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Type__myDsl_Type7", None)
        self.__myDsl_Type7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Feature6"):
                opp_val = getattr(old_value, "myDsl_Feature6", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Feature6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Feature6"):
                opp_val = getattr(value, "myDsl_Feature6", None)
                setattr(value, "myDsl_Feature6", self)

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
            if hasattr(old_value, "myDsl_Domainmodel"):
                opp_val = getattr(old_value, "myDsl_Domainmodel", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Domainmodel"):
                opp_val = getattr(value, "myDsl_Domainmodel", None)
                if opp_val is None:
                    setattr(value, "myDsl_Domainmodel", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class myDsl_Domainmodel:

    pass