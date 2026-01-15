from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class ModelElement:

    pass
class simpleuml_Property(ModelElement):

    pass
class simpleuml_Generalization:

    def __init__(self, isSubstitutable: bool, simpleuml_Generalization14: "simpleuml_Class" = None, simpleuml_Generalization: "simpleuml_Class" = None):
        self.isSubstitutable = isSubstitutable
        self.simpleuml_Generalization14 = simpleuml_Generalization14
        self.simpleuml_Generalization = simpleuml_Generalization
        
    @property
    def isSubstitutable(self) -> bool:
        return self.__isSubstitutable

    @isSubstitutable.setter
    def isSubstitutable(self, isSubstitutable: bool):
        self.__isSubstitutable = isSubstitutable

    @property
    def simpleuml_Generalization(self):
        return self.__simpleuml_Generalization

    @simpleuml_Generalization.setter
    def simpleuml_Generalization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleuml_Generalization__simpleuml_Generalization", None)
        self.__simpleuml_Generalization = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleuml_Class"):
                opp_val = getattr(old_value, "simpleuml_Class", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleuml_Class"):
                opp_val = getattr(value, "simpleuml_Class", None)
                if opp_val is None:
                    setattr(value, "simpleuml_Class", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def simpleuml_Generalization14(self):
        return self.__simpleuml_Generalization14

    @simpleuml_Generalization14.setter
    def simpleuml_Generalization14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleuml_Generalization__simpleuml_Generalization14", None)
        self.__simpleuml_Generalization14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleuml_Class15"):
                opp_val = getattr(old_value, "simpleuml_Class15", None)
                if opp_val == self:
                    setattr(old_value, "simpleuml_Class15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleuml_Class15"):
                opp_val = getattr(value, "simpleuml_Class15", None)
                setattr(value, "simpleuml_Class15", self)

class DataType:

    pass
class simpleuml_Class(DataType):

    def __init__(self, abstract: bool, simpleuml_Class5: "simpleuml_Association" = None, simpleuml_Class8: "simpleuml_Association" = None, simpleuml_Class15: "simpleuml_Generalization" = None, simpleuml_Class: set["simpleuml_Generalization"] = None):
        self.abstract = abstract
        self.simpleuml_Class5 = simpleuml_Class5
        self.simpleuml_Class8 = simpleuml_Class8
        self.simpleuml_Class15 = simpleuml_Class15
        self.simpleuml_Class = simpleuml_Class if simpleuml_Class is not None else set()
        
    @property
    def abstract(self) -> bool:
        return self.__abstract

    @abstract.setter
    def abstract(self, abstract: bool):
        self.__abstract = abstract

    @property
    def simpleuml_Class(self):
        return self.__simpleuml_Class

    @simpleuml_Class.setter
    def simpleuml_Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleuml_Class__simpleuml_Class", None)
        self.__simpleuml_Class = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "simpleuml_Generalization"):
                    opp_val = getattr(item, "simpleuml_Generalization", None)
                    
                    if opp_val == self:
                        setattr(item, "simpleuml_Generalization", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "simpleuml_Generalization"):
                    opp_val = getattr(item, "simpleuml_Generalization", None)
                    
                    setattr(item, "simpleuml_Generalization", self)
                    

    @property
    def simpleuml_Class15(self):
        return self.__simpleuml_Class15

    @simpleuml_Class15.setter
    def simpleuml_Class15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleuml_Class__simpleuml_Class15", None)
        self.__simpleuml_Class15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleuml_Generalization14"):
                opp_val = getattr(old_value, "simpleuml_Generalization14", None)
                if opp_val == self:
                    setattr(old_value, "simpleuml_Generalization14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleuml_Generalization14"):
                opp_val = getattr(value, "simpleuml_Generalization14", None)
                setattr(value, "simpleuml_Generalization14", self)

    @property
    def simpleuml_Class5(self):
        return self.__simpleuml_Class5

    @simpleuml_Class5.setter
    def simpleuml_Class5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleuml_Class__simpleuml_Class5", None)
        self.__simpleuml_Class5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleuml_Association"):
                opp_val = getattr(old_value, "simpleuml_Association", None)
                if opp_val == self:
                    setattr(old_value, "simpleuml_Association", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleuml_Association"):
                opp_val = getattr(value, "simpleuml_Association", None)
                setattr(value, "simpleuml_Association", self)

    @property
    def simpleuml_Class8(self):
        return self.__simpleuml_Class8

    @simpleuml_Class8.setter
    def simpleuml_Class8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleuml_Class__simpleuml_Class8", None)
        self.__simpleuml_Class8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleuml_Association7"):
                opp_val = getattr(old_value, "simpleuml_Association7", None)
                if opp_val == self:
                    setattr(old_value, "simpleuml_Association7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleuml_Association7"):
                opp_val = getattr(value, "simpleuml_Association7", None)
                setattr(value, "simpleuml_Association7", self)

class simpleuml_Packageable(ABC):

    pass
class Packageable:

    pass
class simpleuml_TaggedValue:

    def __init__(self, name: str, value: str, simpleuml_TaggedValue: "simpleuml_ModelElement" = None):
        self.name = name
        self.value = value
        self.simpleuml_TaggedValue = simpleuml_TaggedValue
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def simpleuml_TaggedValue(self):
        return self.__simpleuml_TaggedValue

    @simpleuml_TaggedValue.setter
    def simpleuml_TaggedValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleuml_TaggedValue__simpleuml_TaggedValue", None)
        self.__simpleuml_TaggedValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleuml_ModelElement"):
                opp_val = getattr(old_value, "simpleuml_ModelElement", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleuml_ModelElement"):
                opp_val = getattr(value, "simpleuml_ModelElement", None)
                if opp_val is None:
                    setattr(value, "simpleuml_ModelElement", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class simpleuml_ModelElement(ABC):

    def __init__(self, name: str, stereotype: str, simpleuml_ModelElement: set["simpleuml_TaggedValue"] = None):
        self.name = name
        self.stereotype = stereotype
        self.simpleuml_ModelElement = simpleuml_ModelElement if simpleuml_ModelElement is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def stereotype(self) -> str:
        return self.__stereotype

    @stereotype.setter
    def stereotype(self, stereotype: str):
        self.__stereotype = stereotype

    @property
    def simpleuml_ModelElement(self):
        return self.__simpleuml_ModelElement

    @simpleuml_ModelElement.setter
    def simpleuml_ModelElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleuml_ModelElement__simpleuml_ModelElement", None)
        self.__simpleuml_ModelElement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "simpleuml_TaggedValue"):
                    opp_val = getattr(item, "simpleuml_TaggedValue", None)
                    
                    if opp_val == self:
                        setattr(item, "simpleuml_TaggedValue", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "simpleuml_TaggedValue"):
                    opp_val = getattr(item, "simpleuml_TaggedValue", None)
                    
                    setattr(item, "simpleuml_TaggedValue", self)
                    

class simpleuml_Classifier(ModelElement):

    pass
class simpleuml_EnumerationLiteral:

    def __init__(self, name: str, simpleuml_EnumerationLiteral: "simpleuml_Enumeration" = None):
        self.name = name
        self.simpleuml_EnumerationLiteral = simpleuml_EnumerationLiteral
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def simpleuml_EnumerationLiteral(self):
        return self.__simpleuml_EnumerationLiteral

    @simpleuml_EnumerationLiteral.setter
    def simpleuml_EnumerationLiteral(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleuml_EnumerationLiteral__simpleuml_EnumerationLiteral", None)
        self.__simpleuml_EnumerationLiteral = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleuml_Enumeration"):
                opp_val = getattr(old_value, "simpleuml_Enumeration", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleuml_Enumeration"):
                opp_val = getattr(value, "simpleuml_Enumeration", None)
                if opp_val is None:
                    setattr(value, "simpleuml_Enumeration", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Type:

    pass
class simpleuml_Enumeration(Type):

    pass
class simpleuml_PrimitiveType(Type):

    pass
class simpleuml_Association(ModelElement, Packageable):

    pass
class simpleuml_DataType(Type):

    pass
class Classifier:

    pass
class simpleuml_Type(Packageable, Classifier):

    pass
class simpleuml_Package(Packageable, Classifier):

    pass
class Package:

    pass
class simpleuml_Model(Package):

    def __init__(self):
        
    def getCustomProperty(self, name: str) -> str:
        # TODO: Implement getCustomProperty method
        pass
