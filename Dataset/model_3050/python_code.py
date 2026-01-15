from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class domainmodel_XExpression:

    pass
class domainmodel_JvmFormalParameter:

    pass
class domainmodel_JvmTypeReference:

    pass
class domainmodel_JvmParameterizedTypeReference:

    pass
class domainmodel_Feature:

    def __init__(self, name: str, domainmodel_Feature7: "domainmodel_JvmTypeReference" = None, domainmodel_Feature: "domainmodel_Entity" = None):
        self.name = name
        self.domainmodel_Feature7 = domainmodel_Feature7
        self.domainmodel_Feature = domainmodel_Feature
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
            if hasattr(old_value, "domainmodel_Entity"):
                opp_val = getattr(old_value, "domainmodel_Entity", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domainmodel_Entity"):
                opp_val = getattr(value, "domainmodel_Entity", None)
                if opp_val is None:
                    setattr(value, "domainmodel_Entity", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def domainmodel_Feature7(self):
        return self.__domainmodel_Feature7

    @domainmodel_Feature7.setter
    def domainmodel_Feature7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domainmodel_Feature__domainmodel_Feature7", None)
        self.__domainmodel_Feature7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domainmodel_JvmTypeReference"):
                opp_val = getattr(old_value, "domainmodel_JvmTypeReference", None)
                if opp_val == self:
                    setattr(old_value, "domainmodel_JvmTypeReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domainmodel_JvmTypeReference"):
                opp_val = getattr(value, "domainmodel_JvmTypeReference", None)
                setattr(value, "domainmodel_JvmTypeReference", self)

class AbstractElement:

    pass
class domainmodel_Entity(AbstractElement):

    def __init__(self, name: str, domainmodel_Entity: set["domainmodel_Feature"] = None, domainmodel_Entity5: "domainmodel_JvmParameterizedTypeReference" = None):
        self.name = name
        self.domainmodel_Entity = domainmodel_Entity if domainmodel_Entity is not None else set()
        self.domainmodel_Entity5 = domainmodel_Entity5
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def domainmodel_Entity(self):
        return self.__domainmodel_Entity

    @domainmodel_Entity.setter
    def domainmodel_Entity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domainmodel_Entity__domainmodel_Entity", None)
        self.__domainmodel_Entity = value if value is not None else set()
        
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
    def domainmodel_Entity5(self):
        return self.__domainmodel_Entity5

    @domainmodel_Entity5.setter
    def domainmodel_Entity5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domainmodel_Entity__domainmodel_Entity5", None)
        self.__domainmodel_Entity5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domainmodel_JvmParameterizedTypeReference"):
                opp_val = getattr(old_value, "domainmodel_JvmParameterizedTypeReference", None)
                if opp_val == self:
                    setattr(old_value, "domainmodel_JvmParameterizedTypeReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domainmodel_JvmParameterizedTypeReference"):
                opp_val = getattr(value, "domainmodel_JvmParameterizedTypeReference", None)
                setattr(value, "domainmodel_JvmParameterizedTypeReference", self)

class domainmodel_PackageDeclaration(AbstractElement):

    def __init__(self, name: str, domainmodel_PackageDeclaration: set["domainmodel_AbstractElement"] = None):
        self.name = name
        self.domainmodel_PackageDeclaration = domainmodel_PackageDeclaration if domainmodel_PackageDeclaration is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def domainmodel_PackageDeclaration(self):
        return self.__domainmodel_PackageDeclaration

    @domainmodel_PackageDeclaration.setter
    def domainmodel_PackageDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domainmodel_PackageDeclaration__domainmodel_PackageDeclaration", None)
        self.__domainmodel_PackageDeclaration = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "domainmodel_AbstractElement2"):
                    opp_val = getattr(item, "domainmodel_AbstractElement2", None)
                    
                    if opp_val == self:
                        setattr(item, "domainmodel_AbstractElement2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "domainmodel_AbstractElement2"):
                    opp_val = getattr(item, "domainmodel_AbstractElement2", None)
                    
                    setattr(item, "domainmodel_AbstractElement2", self)
                    

class domainmodel_Import(AbstractElement):

    def __init__(self, importedNamespace: str):
        self.importedNamespace = importedNamespace
        
    @property
    def importedNamespace(self) -> str:
        return self.__importedNamespace

    @importedNamespace.setter
    def importedNamespace(self, importedNamespace: str):
        self.__importedNamespace = importedNamespace

class domainmodel_AbstractElement:

    pass
class domainmodel_DomainModel:

    pass
class Feature:

    pass
class domainmodel_Operation(Feature):

    pass
class domainmodel_Property(Feature):

    pass