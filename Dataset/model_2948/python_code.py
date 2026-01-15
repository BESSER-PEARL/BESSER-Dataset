from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class domainmodel_Type:

    pass
class domainmodel_Domainmodel:

    pass
class domainmodel_Feature:

    def __init__(self, many: bool, name: str, type: str, s: str, domainmodel_Feature: "domainmodel_Entity" = None):
        self.many = many
        self.name = name
        self.type = type
        self.s = s
        self.domainmodel_Feature = domainmodel_Feature
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def many(self) -> bool:
        return self.__many

    @many.setter
    def many(self, many: bool):
        self.__many = many

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def s(self) -> str:
        return self.__s

    @s.setter
    def s(self, s: str):
        self.__s = s

    @property
    def domainmodel_Feature(self):
        return self.__domainmodel_Feature

    @domainmodel_Feature.setter
    def domainmodel_Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domainmodel_Feature__domainmodel_Feature", None)
        self.__domainmodel_Feature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domainmodel_Entity6"):
                opp_val = getattr(old_value, "domainmodel_Entity6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domainmodel_Entity6"):
                opp_val = getattr(value, "domainmodel_Entity6", None)
                if opp_val is None:
                    setattr(value, "domainmodel_Entity6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Type:

    pass
class domainmodel_Entity(Type):

    def __init__(self, name: str, domainmodel_Entity: "domainmodel_Entity" = None, domainmodel_Entity3: "domainmodel_Entity" = None, domainmodel_Entity6: set["domainmodel_Feature"] = None):
        self.name = name
        self.domainmodel_Entity = domainmodel_Entity
        self.domainmodel_Entity3 = domainmodel_Entity3
        self.domainmodel_Entity6 = domainmodel_Entity6 if domainmodel_Entity6 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def domainmodel_Entity6(self):
        return self.__domainmodel_Entity6

    @domainmodel_Entity6.setter
    def domainmodel_Entity6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domainmodel_Entity__domainmodel_Entity6", None)
        self.__domainmodel_Entity6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "domainmodel_Feature"):
                    opp_val = getattr(item, "domainmodel_Feature", None)
                    
                    if opp_val == self:
                        setattr(item, "domainmodel_Feature", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "domainmodel_Feature"):
                    opp_val = getattr(item, "domainmodel_Feature", None)
                    
                    setattr(item, "domainmodel_Feature", self)
                    

    @property
    def domainmodel_Entity3(self):
        return self.__domainmodel_Entity3

    @domainmodel_Entity3.setter
    def domainmodel_Entity3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domainmodel_Entity__domainmodel_Entity3", None)
        self.__domainmodel_Entity3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domainmodel_Entity"):
                opp_val = getattr(old_value, "domainmodel_Entity", None)
                if opp_val == self:
                    setattr(old_value, "domainmodel_Entity", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domainmodel_Entity"):
                opp_val = getattr(value, "domainmodel_Entity", None)
                setattr(value, "domainmodel_Entity", self)

    @property
    def domainmodel_Entity(self):
        return self.__domainmodel_Entity

    @domainmodel_Entity.setter
    def domainmodel_Entity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domainmodel_Entity__domainmodel_Entity", None)
        self.__domainmodel_Entity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domainmodel_Entity3"):
                opp_val = getattr(old_value, "domainmodel_Entity3", None)
                if opp_val == self:
                    setattr(old_value, "domainmodel_Entity3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domainmodel_Entity3"):
                opp_val = getattr(value, "domainmodel_Entity3", None)
                setattr(value, "domainmodel_Entity3", self)

class domainmodel_DataType:

    def __init__(self, name: str, domainmodel_DataType: "domainmodel_Type" = None):
        self.name = name
        self.domainmodel_DataType = domainmodel_DataType
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def domainmodel_DataType(self):
        return self.__domainmodel_DataType

    @domainmodel_DataType.setter
    def domainmodel_DataType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domainmodel_DataType__domainmodel_DataType", None)
        self.__domainmodel_DataType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domainmodel_Type2"):
                opp_val = getattr(old_value, "domainmodel_Type2", None)
                if opp_val == self:
                    setattr(old_value, "domainmodel_Type2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domainmodel_Type2"):
                opp_val = getattr(value, "domainmodel_Type2", None)
                setattr(value, "domainmodel_Type2", self)
