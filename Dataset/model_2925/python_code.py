from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class wh_Feature:

    def __init__(self, many: bool, name: str, wh_Feature: "wh_Entity" = None, wh_Feature8: "wh_Type" = None):
        self.many = many
        self.name = name
        self.wh_Feature = wh_Feature
        self.wh_Feature8 = wh_Feature8
        
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
    def wh_Feature(self):
        return self.__wh_Feature

    @wh_Feature.setter
    def wh_Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wh_Feature__wh_Feature", None)
        self.__wh_Feature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wh_Entity6"):
                opp_val = getattr(old_value, "wh_Entity6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wh_Entity6"):
                opp_val = getattr(value, "wh_Entity6", None)
                if opp_val is None:
                    setattr(value, "wh_Entity6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def wh_Feature8(self):
        return self.__wh_Feature8

    @wh_Feature8.setter
    def wh_Feature8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wh_Feature__wh_Feature8", None)
        self.__wh_Feature8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wh_Type"):
                opp_val = getattr(old_value, "wh_Type", None)
                if opp_val == self:
                    setattr(old_value, "wh_Type", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wh_Type"):
                opp_val = getattr(value, "wh_Type", None)
                setattr(value, "wh_Type", self)

class AbstractElement:

    pass
class wh_PackageDeclaration(AbstractElement):

    def __init__(self, name: str, wh_PackageDeclaration: set["wh_AbstractElement"] = None):
        self.name = name
        self.wh_PackageDeclaration = wh_PackageDeclaration if wh_PackageDeclaration is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def wh_PackageDeclaration(self):
        return self.__wh_PackageDeclaration

    @wh_PackageDeclaration.setter
    def wh_PackageDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wh_PackageDeclaration__wh_PackageDeclaration", None)
        self.__wh_PackageDeclaration = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "wh_AbstractElement2"):
                    opp_val = getattr(item, "wh_AbstractElement2", None)
                    
                    if opp_val == self:
                        setattr(item, "wh_AbstractElement2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "wh_AbstractElement2"):
                    opp_val = getattr(item, "wh_AbstractElement2", None)
                    
                    setattr(item, "wh_AbstractElement2", self)
                    

class wh_AbstractElement:

    pass
class wh_Wh:

    pass
class Type:

    pass
class wh_Entity(Type):

    pass
class wh_DataType(Type):

    pass
class wh_Type(AbstractElement):

    def __init__(self, name: str, wh_Type: "wh_Feature" = None):
        self.name = name
        self.wh_Type = wh_Type
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def wh_Type(self):
        return self.__wh_Type

    @wh_Type.setter
    def wh_Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wh_Type__wh_Type", None)
        self.__wh_Type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wh_Feature8"):
                opp_val = getattr(old_value, "wh_Feature8", None)
                if opp_val == self:
                    setattr(old_value, "wh_Feature8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wh_Feature8"):
                opp_val = getattr(value, "wh_Feature8", None)
                setattr(value, "wh_Feature8", self)

class wh_Import(AbstractElement):

    def __init__(self, importedNamespace: str):
        self.importedNamespace = importedNamespace
        
    @property
    def importedNamespace(self) -> str:
        return self.__importedNamespace

    @importedNamespace.setter
    def importedNamespace(self, importedNamespace: str):
        self.__importedNamespace = importedNamespace
