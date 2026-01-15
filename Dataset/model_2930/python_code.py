from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class domainmodel_Method:

    def __init__(self, name: str, body: str, domainmodel_Method: "domainmodel_Entity" = None):
        self.name = name
        self.body = body
        self.domainmodel_Method = domainmodel_Method
        
    @property
    def body(self) -> str:
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def domainmodel_Method(self):
        return self.__domainmodel_Method

    @domainmodel_Method.setter
    def domainmodel_Method(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domainmodel_Method__domainmodel_Method", None)
        self.__domainmodel_Method = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domainmodel_Entity8"):
                opp_val = getattr(old_value, "domainmodel_Entity8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domainmodel_Entity8"):
                opp_val = getattr(value, "domainmodel_Entity8", None)
                if opp_val is None:
                    setattr(value, "domainmodel_Entity8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class domainmodel_Feature:

    def __init__(self, value: str, many: bool, name: str, domainmodel_Feature10: "domainmodel_Type" = None, domainmodel_Feature: "domainmodel_Entity" = None):
        self.value = value
        self.many = many
        self.name = name
        self.domainmodel_Feature10 = domainmodel_Feature10
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
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def domainmodel_Feature10(self):
        return self.__domainmodel_Feature10

    @domainmodel_Feature10.setter
    def domainmodel_Feature10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domainmodel_Feature__domainmodel_Feature10", None)
        self.__domainmodel_Feature10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domainmodel_Type"):
                opp_val = getattr(old_value, "domainmodel_Type", None)
                if opp_val == self:
                    setattr(old_value, "domainmodel_Type", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domainmodel_Type"):
                opp_val = getattr(value, "domainmodel_Type", None)
                setattr(value, "domainmodel_Type", self)

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

    pass
class domainmodel_DataType(Type):

    pass
class AbstractElement:

    pass
class domainmodel_Import(AbstractElement):

    def __init__(self, importedNamespace: str):
        self.importedNamespace = importedNamespace
        
    @property
    def importedNamespace(self) -> str:
        return self.__importedNamespace

    @importedNamespace.setter
    def importedNamespace(self, importedNamespace: str):
        self.__importedNamespace = importedNamespace

class domainmodel_Type(AbstractElement):

    def __init__(self, name: str, domainmodel_Type: "domainmodel_Feature" = None):
        self.name = name
        self.domainmodel_Type = domainmodel_Type
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def domainmodel_Type(self):
        return self.__domainmodel_Type

    @domainmodel_Type.setter
    def domainmodel_Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domainmodel_Type__domainmodel_Type", None)
        self.__domainmodel_Type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domainmodel_Feature10"):
                opp_val = getattr(old_value, "domainmodel_Feature10", None)
                if opp_val == self:
                    setattr(old_value, "domainmodel_Feature10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domainmodel_Feature10"):
                opp_val = getattr(value, "domainmodel_Feature10", None)
                setattr(value, "domainmodel_Feature10", self)

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
                    

class domainmodel_AbstractElement:

    pass
class domainmodel_Domainmodel:

    pass