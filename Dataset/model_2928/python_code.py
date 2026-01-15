from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class myTuto_Feature:

    def __init__(self, many: bool, name: str, myTuto_Feature8: "myTuto_Type" = None, myTuto_Feature: "myTuto_Entity" = None):
        self.many = many
        self.name = name
        self.myTuto_Feature8 = myTuto_Feature8
        self.myTuto_Feature = myTuto_Feature
        
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
    def myTuto_Feature8(self):
        return self.__myTuto_Feature8

    @myTuto_Feature8.setter
    def myTuto_Feature8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myTuto_Feature__myTuto_Feature8", None)
        self.__myTuto_Feature8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myTuto_Type"):
                opp_val = getattr(old_value, "myTuto_Type", None)
                if opp_val == self:
                    setattr(old_value, "myTuto_Type", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myTuto_Type"):
                opp_val = getattr(value, "myTuto_Type", None)
                setattr(value, "myTuto_Type", self)

    @property
    def myTuto_Feature(self):
        return self.__myTuto_Feature

    @myTuto_Feature.setter
    def myTuto_Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myTuto_Feature__myTuto_Feature", None)
        self.__myTuto_Feature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myTuto_Entity6"):
                opp_val = getattr(old_value, "myTuto_Entity6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myTuto_Entity6"):
                opp_val = getattr(value, "myTuto_Entity6", None)
                if opp_val is None:
                    setattr(value, "myTuto_Entity6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Type:

    pass
class myTuto_Entity(Type):

    pass
class myTuto_DataType(Type):

    pass
class AbstractElement:

    pass
class myTuto_Type(AbstractElement):

    def __init__(self, name: str, myTuto_Type: "myTuto_Feature" = None):
        self.name = name
        self.myTuto_Type = myTuto_Type
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myTuto_Type(self):
        return self.__myTuto_Type

    @myTuto_Type.setter
    def myTuto_Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myTuto_Type__myTuto_Type", None)
        self.__myTuto_Type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myTuto_Feature8"):
                opp_val = getattr(old_value, "myTuto_Feature8", None)
                if opp_val == self:
                    setattr(old_value, "myTuto_Feature8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myTuto_Feature8"):
                opp_val = getattr(value, "myTuto_Feature8", None)
                setattr(value, "myTuto_Feature8", self)

class myTuto_PackageDeclaration(AbstractElement):

    def __init__(self, name: str, myTuto_PackageDeclaration: set["myTuto_AbstractElement"] = None):
        self.name = name
        self.myTuto_PackageDeclaration = myTuto_PackageDeclaration if myTuto_PackageDeclaration is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myTuto_PackageDeclaration(self):
        return self.__myTuto_PackageDeclaration

    @myTuto_PackageDeclaration.setter
    def myTuto_PackageDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myTuto_PackageDeclaration__myTuto_PackageDeclaration", None)
        self.__myTuto_PackageDeclaration = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "myTuto_AbstractElement2"):
                    opp_val = getattr(item, "myTuto_AbstractElement2", None)
                    
                    if opp_val == self:
                        setattr(item, "myTuto_AbstractElement2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "myTuto_AbstractElement2"):
                    opp_val = getattr(item, "myTuto_AbstractElement2", None)
                    
                    setattr(item, "myTuto_AbstractElement2", self)
                    

class myTuto_AbstractElement:

    pass
class myTuto_MyTuto:

    pass
class myTuto_Import(AbstractElement):

    def __init__(self, importedNameSpace: str):
        self.importedNameSpace = importedNameSpace
        
    @property
    def importedNameSpace(self) -> str:
        return self.__importedNameSpace

    @importedNameSpace.setter
    def importedNameSpace(self, importedNameSpace: str):
        self.__importedNameSpace = importedNameSpace
