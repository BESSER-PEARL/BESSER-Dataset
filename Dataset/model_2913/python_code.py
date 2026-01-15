from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class myDsl_Feature:

    def __init__(self, many: bool, name: str, myDsl_Feature: "myDsl_Entity" = None, myDsl_Feature8: "myDsl_Type" = None):
        self.many = many
        self.name = name
        self.myDsl_Feature = myDsl_Feature
        self.myDsl_Feature8 = myDsl_Feature8
        
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
    def myDsl_Feature(self):
        return self.__myDsl_Feature

    @myDsl_Feature.setter
    def myDsl_Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Feature__myDsl_Feature", None)
        self.__myDsl_Feature = value
        
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

    @property
    def myDsl_Feature8(self):
        return self.__myDsl_Feature8

    @myDsl_Feature8.setter
    def myDsl_Feature8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Feature__myDsl_Feature8", None)
        self.__myDsl_Feature8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Type"):
                opp_val = getattr(old_value, "myDsl_Type", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Type", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Type"):
                opp_val = getattr(value, "myDsl_Type", None)
                setattr(value, "myDsl_Type", self)

class Type:

    pass
class myDsl_Entity(Type):

    pass
class myDsl_DataType(Type):

    pass
class AbstractElement:

    pass
class myDsl_Type(AbstractElement):

    def __init__(self, name: str, myDsl_Type: "myDsl_Feature" = None):
        self.name = name
        self.myDsl_Type = myDsl_Type
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
            if hasattr(old_value, "myDsl_Feature8"):
                opp_val = getattr(old_value, "myDsl_Feature8", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Feature8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Feature8"):
                opp_val = getattr(value, "myDsl_Feature8", None)
                setattr(value, "myDsl_Feature8", self)

class myDsl_Import(AbstractElement):

    def __init__(self, importedNamespace: str):
        self.importedNamespace = importedNamespace
        
    @property
    def importedNamespace(self) -> str:
        return self.__importedNamespace

    @importedNamespace.setter
    def importedNamespace(self, importedNamespace: str):
        self.__importedNamespace = importedNamespace

class myDsl_PackageDeclaration(AbstractElement):

    def __init__(self, name: str, myDsl_PackageDeclaration: set["myDsl_AbstractElement"] = None):
        self.name = name
        self.myDsl_PackageDeclaration = myDsl_PackageDeclaration if myDsl_PackageDeclaration is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myDsl_PackageDeclaration(self):
        return self.__myDsl_PackageDeclaration

    @myDsl_PackageDeclaration.setter
    def myDsl_PackageDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_PackageDeclaration__myDsl_PackageDeclaration", None)
        self.__myDsl_PackageDeclaration = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "myDsl_AbstractElement2"):
                    opp_val = getattr(item, "myDsl_AbstractElement2", None)
                    
                    if opp_val == self:
                        setattr(item, "myDsl_AbstractElement2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "myDsl_AbstractElement2"):
                    opp_val = getattr(item, "myDsl_AbstractElement2", None)
                    
                    setattr(item, "myDsl_AbstractElement2", self)
                    

class myDsl_AbstractElement:

    pass
class myDsl_Model:

    pass