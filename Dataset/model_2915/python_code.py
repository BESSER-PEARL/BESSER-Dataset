from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Type:

    pass
class domainModel_Entity(Type):

    pass
class domainModel_DataType(Type):

    pass
class domainModel_Feature:

    def __init__(self, many: bool, name: str, domainModel_Feature: "domainModel_Entity" = None, domainModel_Feature8: "domainModel_Type" = None):
        self.many = many
        self.name = name
        self.domainModel_Feature = domainModel_Feature
        self.domainModel_Feature8 = domainModel_Feature8
        
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
    def domainModel_Feature8(self):
        return self.__domainModel_Feature8

    @domainModel_Feature8.setter
    def domainModel_Feature8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domainModel_Feature__domainModel_Feature8", None)
        self.__domainModel_Feature8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domainModel_Type"):
                opp_val = getattr(old_value, "domainModel_Type", None)
                if opp_val == self:
                    setattr(old_value, "domainModel_Type", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domainModel_Type"):
                opp_val = getattr(value, "domainModel_Type", None)
                setattr(value, "domainModel_Type", self)

    @property
    def domainModel_Feature(self):
        return self.__domainModel_Feature

    @domainModel_Feature.setter
    def domainModel_Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domainModel_Feature__domainModel_Feature", None)
        self.__domainModel_Feature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domainModel_Entity6"):
                opp_val = getattr(old_value, "domainModel_Entity6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domainModel_Entity6"):
                opp_val = getattr(value, "domainModel_Entity6", None)
                if opp_val is None:
                    setattr(value, "domainModel_Entity6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class domainModel_Model:

    pass
class AbstractElement:

    pass
class domainModel_Type(AbstractElement):

    def __init__(self, name: str, domainModel_Type: "domainModel_Feature" = None):
        self.name = name
        self.domainModel_Type = domainModel_Type
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def domainModel_Type(self):
        return self.__domainModel_Type

    @domainModel_Type.setter
    def domainModel_Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domainModel_Type__domainModel_Type", None)
        self.__domainModel_Type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domainModel_Feature8"):
                opp_val = getattr(old_value, "domainModel_Feature8", None)
                if opp_val == self:
                    setattr(old_value, "domainModel_Feature8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domainModel_Feature8"):
                opp_val = getattr(value, "domainModel_Feature8", None)
                setattr(value, "domainModel_Feature8", self)

class domainModel_Import(AbstractElement):

    def __init__(self, importedNamespace: str):
        self.importedNamespace = importedNamespace
        
    @property
    def importedNamespace(self) -> str:
        return self.__importedNamespace

    @importedNamespace.setter
    def importedNamespace(self, importedNamespace: str):
        self.__importedNamespace = importedNamespace

class domainModel_PackageDeclaration(AbstractElement):

    def __init__(self, name: str, domainModel_PackageDeclaration: set["domainModel_AbstractElement"] = None):
        self.name = name
        self.domainModel_PackageDeclaration = domainModel_PackageDeclaration if domainModel_PackageDeclaration is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def domainModel_PackageDeclaration(self):
        return self.__domainModel_PackageDeclaration

    @domainModel_PackageDeclaration.setter
    def domainModel_PackageDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domainModel_PackageDeclaration__domainModel_PackageDeclaration", None)
        self.__domainModel_PackageDeclaration = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "domainModel_AbstractElement2"):
                    opp_val = getattr(item, "domainModel_AbstractElement2", None)
                    
                    if opp_val == self:
                        setattr(item, "domainModel_AbstractElement2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "domainModel_AbstractElement2"):
                    opp_val = getattr(item, "domainModel_AbstractElement2", None)
                    
                    setattr(item, "domainModel_AbstractElement2", self)
                    

class domainModel_AbstractElement:

    pass