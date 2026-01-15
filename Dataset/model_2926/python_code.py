from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class ling_Feature:

    def __init__(self, many: bool, name: str, ling_Feature8: "ling_Type" = None, ling_Feature: "ling_Entity" = None):
        self.many = many
        self.name = name
        self.ling_Feature8 = ling_Feature8
        self.ling_Feature = ling_Feature
        
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
    def ling_Feature(self):
        return self.__ling_Feature

    @ling_Feature.setter
    def ling_Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ling_Feature__ling_Feature", None)
        self.__ling_Feature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ling_Entity6"):
                opp_val = getattr(old_value, "ling_Entity6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ling_Entity6"):
                opp_val = getattr(value, "ling_Entity6", None)
                if opp_val is None:
                    setattr(value, "ling_Entity6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ling_Feature8(self):
        return self.__ling_Feature8

    @ling_Feature8.setter
    def ling_Feature8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ling_Feature__ling_Feature8", None)
        self.__ling_Feature8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ling_Type"):
                opp_val = getattr(old_value, "ling_Type", None)
                if opp_val == self:
                    setattr(old_value, "ling_Type", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ling_Type"):
                opp_val = getattr(value, "ling_Type", None)
                setattr(value, "ling_Type", self)

class AbstractElement:

    pass
class ling_PackageDeclaration(AbstractElement):

    def __init__(self, name: str, ling_PackageDeclaration: set["ling_AbstractElement"] = None):
        self.name = name
        self.ling_PackageDeclaration = ling_PackageDeclaration if ling_PackageDeclaration is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ling_PackageDeclaration(self):
        return self.__ling_PackageDeclaration

    @ling_PackageDeclaration.setter
    def ling_PackageDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ling_PackageDeclaration__ling_PackageDeclaration", None)
        self.__ling_PackageDeclaration = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ling_AbstractElement2"):
                    opp_val = getattr(item, "ling_AbstractElement2", None)
                    
                    if opp_val == self:
                        setattr(item, "ling_AbstractElement2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ling_AbstractElement2"):
                    opp_val = getattr(item, "ling_AbstractElement2", None)
                    
                    setattr(item, "ling_AbstractElement2", self)
                    

class ling_AbstractElement:

    pass
class Type:

    pass
class ling_Entity(Type):

    pass
class ling_DataType(Type):

    pass
class ling_Type(AbstractElement):

    def __init__(self, name: str, ling_Type: "ling_Feature" = None):
        self.name = name
        self.ling_Type = ling_Type
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ling_Type(self):
        return self.__ling_Type

    @ling_Type.setter
    def ling_Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ling_Type__ling_Type", None)
        self.__ling_Type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ling_Feature8"):
                opp_val = getattr(old_value, "ling_Feature8", None)
                if opp_val == self:
                    setattr(old_value, "ling_Feature8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ling_Feature8"):
                opp_val = getattr(value, "ling_Feature8", None)
                setattr(value, "ling_Feature8", self)

class ling_Import(AbstractElement):

    def __init__(self, importedNamespace: str):
        self.importedNamespace = importedNamespace
        
    @property
    def importedNamespace(self) -> str:
        return self.__importedNamespace

    @importedNamespace.setter
    def importedNamespace(self, importedNamespace: str):
        self.__importedNamespace = importedNamespace

class ling_Domainmodel:

    pass