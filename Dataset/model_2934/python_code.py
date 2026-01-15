from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class domainDsl_Validator:

    def __init__(self, name: str, value: int, svalue: str, domainDsl_Validator: "domainDsl_Feature" = None):
        self.name = name
        self.value = value
        self.svalue = svalue
        self.domainDsl_Validator = domainDsl_Validator
        
    @property
    def svalue(self) -> str:
        return self.__svalue

    @svalue.setter
    def svalue(self, svalue: str):
        self.__svalue = svalue

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def domainDsl_Validator(self):
        return self.__domainDsl_Validator

    @domainDsl_Validator.setter
    def domainDsl_Validator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domainDsl_Validator__domainDsl_Validator", None)
        self.__domainDsl_Validator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domainDsl_Feature10"):
                opp_val = getattr(old_value, "domainDsl_Feature10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domainDsl_Feature10"):
                opp_val = getattr(value, "domainDsl_Feature10", None)
                if opp_val is None:
                    setattr(value, "domainDsl_Feature10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class domainDsl_Feature:

    def __init__(self, many: bool, name: str, defaultVal: str, domainDsl_Feature: "domainDsl_Entity" = None, domainDsl_Feature8: "domainDsl_Type" = None, domainDsl_Feature10: set["domainDsl_Validator"] = None):
        self.many = many
        self.name = name
        self.defaultVal = defaultVal
        self.domainDsl_Feature = domainDsl_Feature
        self.domainDsl_Feature8 = domainDsl_Feature8
        self.domainDsl_Feature10 = domainDsl_Feature10 if domainDsl_Feature10 is not None else set()
        
    @property
    def defaultVal(self) -> str:
        return self.__defaultVal

    @defaultVal.setter
    def defaultVal(self, defaultVal: str):
        self.__defaultVal = defaultVal

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
    def domainDsl_Feature(self):
        return self.__domainDsl_Feature

    @domainDsl_Feature.setter
    def domainDsl_Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domainDsl_Feature__domainDsl_Feature", None)
        self.__domainDsl_Feature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domainDsl_Entity6"):
                opp_val = getattr(old_value, "domainDsl_Entity6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domainDsl_Entity6"):
                opp_val = getattr(value, "domainDsl_Entity6", None)
                if opp_val is None:
                    setattr(value, "domainDsl_Entity6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def domainDsl_Feature8(self):
        return self.__domainDsl_Feature8

    @domainDsl_Feature8.setter
    def domainDsl_Feature8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domainDsl_Feature__domainDsl_Feature8", None)
        self.__domainDsl_Feature8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domainDsl_Type"):
                opp_val = getattr(old_value, "domainDsl_Type", None)
                if opp_val == self:
                    setattr(old_value, "domainDsl_Type", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domainDsl_Type"):
                opp_val = getattr(value, "domainDsl_Type", None)
                setattr(value, "domainDsl_Type", self)

    @property
    def domainDsl_Feature10(self):
        return self.__domainDsl_Feature10

    @domainDsl_Feature10.setter
    def domainDsl_Feature10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domainDsl_Feature__domainDsl_Feature10", None)
        self.__domainDsl_Feature10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "domainDsl_Validator"):
                    opp_val = getattr(item, "domainDsl_Validator", None)
                    
                    if opp_val == self:
                        setattr(item, "domainDsl_Validator", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "domainDsl_Validator"):
                    opp_val = getattr(item, "domainDsl_Validator", None)
                    
                    setattr(item, "domainDsl_Validator", self)
                    

class Type:

    pass
class domainDsl_Entity(Type):

    pass
class domainDsl_DataType(Type):

    pass
class domainDsl_EType:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class AbstractElement:

    pass
class domainDsl_Type(AbstractElement):

    def __init__(self, name: str, domainDsl_Type: "domainDsl_Feature" = None):
        self.name = name
        self.domainDsl_Type = domainDsl_Type
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def domainDsl_Type(self):
        return self.__domainDsl_Type

    @domainDsl_Type.setter
    def domainDsl_Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domainDsl_Type__domainDsl_Type", None)
        self.__domainDsl_Type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domainDsl_Feature8"):
                opp_val = getattr(old_value, "domainDsl_Feature8", None)
                if opp_val == self:
                    setattr(old_value, "domainDsl_Feature8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domainDsl_Feature8"):
                opp_val = getattr(value, "domainDsl_Feature8", None)
                setattr(value, "domainDsl_Feature8", self)

class domainDsl_Import(AbstractElement):

    def __init__(self, importedNamespace: str):
        self.importedNamespace = importedNamespace
        
    @property
    def importedNamespace(self) -> str:
        return self.__importedNamespace

    @importedNamespace.setter
    def importedNamespace(self, importedNamespace: str):
        self.__importedNamespace = importedNamespace

class domainDsl_PackageDeclaration(AbstractElement):

    def __init__(self, name: str, domainDsl_PackageDeclaration: set["domainDsl_AbstractElement"] = None):
        self.name = name
        self.domainDsl_PackageDeclaration = domainDsl_PackageDeclaration if domainDsl_PackageDeclaration is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def domainDsl_PackageDeclaration(self):
        return self.__domainDsl_PackageDeclaration

    @domainDsl_PackageDeclaration.setter
    def domainDsl_PackageDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domainDsl_PackageDeclaration__domainDsl_PackageDeclaration", None)
        self.__domainDsl_PackageDeclaration = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "domainDsl_AbstractElement2"):
                    opp_val = getattr(item, "domainDsl_AbstractElement2", None)
                    
                    if opp_val == self:
                        setattr(item, "domainDsl_AbstractElement2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "domainDsl_AbstractElement2"):
                    opp_val = getattr(item, "domainDsl_AbstractElement2", None)
                    
                    setattr(item, "domainDsl_AbstractElement2", self)
                    

class domainDsl_AbstractElement:

    pass
class domainDsl_Domainmodel:

    pass