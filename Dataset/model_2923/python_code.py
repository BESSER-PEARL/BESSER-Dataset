from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class aGES_Feature:

    def __init__(self, many: bool, name: str, aGES_Feature: "aGES_Entity" = None, aGES_Feature8: "aGES_Type" = None):
        self.many = many
        self.name = name
        self.aGES_Feature = aGES_Feature
        self.aGES_Feature8 = aGES_Feature8
        
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
    def aGES_Feature8(self):
        return self.__aGES_Feature8

    @aGES_Feature8.setter
    def aGES_Feature8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aGES_Feature__aGES_Feature8", None)
        self.__aGES_Feature8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aGES_Type"):
                opp_val = getattr(old_value, "aGES_Type", None)
                if opp_val == self:
                    setattr(old_value, "aGES_Type", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aGES_Type"):
                opp_val = getattr(value, "aGES_Type", None)
                setattr(value, "aGES_Type", self)

    @property
    def aGES_Feature(self):
        return self.__aGES_Feature

    @aGES_Feature.setter
    def aGES_Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aGES_Feature__aGES_Feature", None)
        self.__aGES_Feature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aGES_Entity6"):
                opp_val = getattr(old_value, "aGES_Entity6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aGES_Entity6"):
                opp_val = getattr(value, "aGES_Entity6", None)
                if opp_val is None:
                    setattr(value, "aGES_Entity6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Type:

    pass
class aGES_Entity(Type):

    pass
class aGES_DataType(Type):

    pass
class aGES_AbstractElement:

    pass
class aGES_Domainmodel:

    pass
class AbstractElement:

    pass
class aGES_Import(AbstractElement):

    def __init__(self, importedNamespace: str):
        self.importedNamespace = importedNamespace
        
    @property
    def importedNamespace(self) -> str:
        return self.__importedNamespace

    @importedNamespace.setter
    def importedNamespace(self, importedNamespace: str):
        self.__importedNamespace = importedNamespace

class aGES_PackageDeclaration(AbstractElement):

    def __init__(self, name: str, aGES_PackageDeclaration: set["aGES_AbstractElement"] = None):
        self.name = name
        self.aGES_PackageDeclaration = aGES_PackageDeclaration if aGES_PackageDeclaration is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def aGES_PackageDeclaration(self):
        return self.__aGES_PackageDeclaration

    @aGES_PackageDeclaration.setter
    def aGES_PackageDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aGES_PackageDeclaration__aGES_PackageDeclaration", None)
        self.__aGES_PackageDeclaration = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aGES_AbstractElement2"):
                    opp_val = getattr(item, "aGES_AbstractElement2", None)
                    
                    if opp_val == self:
                        setattr(item, "aGES_AbstractElement2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aGES_AbstractElement2"):
                    opp_val = getattr(item, "aGES_AbstractElement2", None)
                    
                    setattr(item, "aGES_AbstractElement2", self)
                    

class aGES_Type(AbstractElement):

    def __init__(self, name: str, aGES_Type: "aGES_Feature" = None):
        self.name = name
        self.aGES_Type = aGES_Type
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def aGES_Type(self):
        return self.__aGES_Type

    @aGES_Type.setter
    def aGES_Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aGES_Type__aGES_Type", None)
        self.__aGES_Type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aGES_Feature8"):
                opp_val = getattr(old_value, "aGES_Feature8", None)
                if opp_val == self:
                    setattr(old_value, "aGES_Feature8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aGES_Feature8"):
                opp_val = getattr(value, "aGES_Feature8", None)
                setattr(value, "aGES_Feature8", self)
