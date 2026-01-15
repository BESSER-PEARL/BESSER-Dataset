from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class classdiagram_AttributeValue(ABC):

    pass
class classdiagram_InterfaceRealization:

    pass
class classdiagram_Interface:

    def __init__(self, name: str, classdiagram_Interface: set["classdiagram_Attribute"] = None, classdiagram_Interface26: set["classdiagram_Method"] = None, classdiagram_Interface29: "classdiagram_InterfaceRealization" = None):
        self.name = name
        self.classdiagram_Interface = classdiagram_Interface if classdiagram_Interface is not None else set()
        self.classdiagram_Interface26 = classdiagram_Interface26 if classdiagram_Interface26 is not None else set()
        self.classdiagram_Interface29 = classdiagram_Interface29
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def classdiagram_Interface29(self):
        return self.__classdiagram_Interface29

    @classdiagram_Interface29.setter
    def classdiagram_Interface29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classdiagram_Interface__classdiagram_Interface29", None)
        self.__classdiagram_Interface29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classdiagram_InterfaceRealization"):
                opp_val = getattr(old_value, "classdiagram_InterfaceRealization", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classdiagram_InterfaceRealization"):
                opp_val = getattr(value, "classdiagram_InterfaceRealization", None)
                if opp_val is None:
                    setattr(value, "classdiagram_InterfaceRealization", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def classdiagram_Interface(self):
        return self.__classdiagram_Interface

    @classdiagram_Interface.setter
    def classdiagram_Interface(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classdiagram_Interface__classdiagram_Interface", None)
        self.__classdiagram_Interface = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "classdiagram_Attribute24"):
                    opp_val = getattr(item, "classdiagram_Attribute24", None)
                    
                    if opp_val == self:
                        setattr(item, "classdiagram_Attribute24", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "classdiagram_Attribute24"):
                    opp_val = getattr(item, "classdiagram_Attribute24", None)
                    
                    setattr(item, "classdiagram_Attribute24", self)
                    

    @property
    def classdiagram_Interface26(self):
        return self.__classdiagram_Interface26

    @classdiagram_Interface26.setter
    def classdiagram_Interface26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classdiagram_Interface__classdiagram_Interface26", None)
        self.__classdiagram_Interface26 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "classdiagram_Method27"):
                    opp_val = getattr(item, "classdiagram_Method27", None)
                    
                    if opp_val == self:
                        setattr(item, "classdiagram_Method27", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "classdiagram_Method27"):
                    opp_val = getattr(item, "classdiagram_Method27", None)
                    
                    setattr(item, "classdiagram_Method27", self)
                    

class classdiagram_Realization:

    pass
class classdiagram_Method:

    def __init__(self, name: str, classdiagram_Method: "classdiagram_Class" = None, classdiagram_Method27: "classdiagram_Interface" = None):
        self.name = name
        self.classdiagram_Method = classdiagram_Method
        self.classdiagram_Method27 = classdiagram_Method27
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def classdiagram_Method27(self):
        return self.__classdiagram_Method27

    @classdiagram_Method27.setter
    def classdiagram_Method27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classdiagram_Method__classdiagram_Method27", None)
        self.__classdiagram_Method27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classdiagram_Interface26"):
                opp_val = getattr(old_value, "classdiagram_Interface26", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classdiagram_Interface26"):
                opp_val = getattr(value, "classdiagram_Interface26", None)
                if opp_val is None:
                    setattr(value, "classdiagram_Interface26", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def classdiagram_Method(self):
        return self.__classdiagram_Method

    @classdiagram_Method.setter
    def classdiagram_Method(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classdiagram_Method__classdiagram_Method", None)
        self.__classdiagram_Method = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classdiagram_Class16"):
                opp_val = getattr(old_value, "classdiagram_Class16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classdiagram_Class16"):
                opp_val = getattr(value, "classdiagram_Class16", None)
                if opp_val is None:
                    setattr(value, "classdiagram_Class16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class classdiagram_Attribute:

    def __init__(self, name: str, is_primary: bool, classdiagram_Attribute: "classdiagram_Class" = None, classdiagram_Attribute24: "classdiagram_Interface" = None, classdiagram_Attribute39: "classdiagram_AttributeValue" = None):
        self.name = name
        self.is_primary = is_primary
        self.classdiagram_Attribute = classdiagram_Attribute
        self.classdiagram_Attribute24 = classdiagram_Attribute24
        self.classdiagram_Attribute39 = classdiagram_Attribute39
        
    @property
    def is_primary(self) -> bool:
        return self.__is_primary

    @is_primary.setter
    def is_primary(self, is_primary: bool):
        self.__is_primary = is_primary

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def classdiagram_Attribute39(self):
        return self.__classdiagram_Attribute39

    @classdiagram_Attribute39.setter
    def classdiagram_Attribute39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classdiagram_Attribute__classdiagram_Attribute39", None)
        self.__classdiagram_Attribute39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classdiagram_AttributeValue"):
                opp_val = getattr(old_value, "classdiagram_AttributeValue", None)
                if opp_val == self:
                    setattr(old_value, "classdiagram_AttributeValue", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classdiagram_AttributeValue"):
                opp_val = getattr(value, "classdiagram_AttributeValue", None)
                setattr(value, "classdiagram_AttributeValue", self)

    @property
    def classdiagram_Attribute24(self):
        return self.__classdiagram_Attribute24

    @classdiagram_Attribute24.setter
    def classdiagram_Attribute24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classdiagram_Attribute__classdiagram_Attribute24", None)
        self.__classdiagram_Attribute24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classdiagram_Interface"):
                opp_val = getattr(old_value, "classdiagram_Interface", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classdiagram_Interface"):
                opp_val = getattr(value, "classdiagram_Interface", None)
                if opp_val is None:
                    setattr(value, "classdiagram_Interface", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def classdiagram_Attribute(self):
        return self.__classdiagram_Attribute

    @classdiagram_Attribute.setter
    def classdiagram_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classdiagram_Attribute__classdiagram_Attribute", None)
        self.__classdiagram_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classdiagram_Class14"):
                opp_val = getattr(old_value, "classdiagram_Class14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classdiagram_Class14"):
                opp_val = getattr(value, "classdiagram_Class14", None)
                if opp_val is None:
                    setattr(value, "classdiagram_Class14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class AttributeValue:

    pass
class Association:

    pass
class classdiagram_Composition(Association):

    pass
class classdiagram_Dependency(Association):

    pass
class classdiagram_Aggregation(Association):

    pass
class classdiagram_PrimitiveDataType(AttributeValue):

    def __init__(self, name: str, classdiagram_PrimitiveDataType: "classdiagram_Diagram" = None):
        self.name = name
        self.classdiagram_PrimitiveDataType = classdiagram_PrimitiveDataType
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def classdiagram_PrimitiveDataType(self):
        return self.__classdiagram_PrimitiveDataType

    @classdiagram_PrimitiveDataType.setter
    def classdiagram_PrimitiveDataType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classdiagram_PrimitiveDataType__classdiagram_PrimitiveDataType", None)
        self.__classdiagram_PrimitiveDataType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classdiagram_Diagram4"):
                opp_val = getattr(old_value, "classdiagram_Diagram4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classdiagram_Diagram4"):
                opp_val = getattr(value, "classdiagram_Diagram4", None)
                if opp_val is None:
                    setattr(value, "classdiagram_Diagram4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class classdiagram_Association:

    def __init__(self, name: str, sourceMultiplicity: int, targetMultiplicity: int, classdiagram_Association8: "classdiagram_Class" = None, classdiagram_Association: "classdiagram_Diagram" = None, classdiagram_Association11: "classdiagram_Class" = None):
        self.name = name
        self.sourceMultiplicity = sourceMultiplicity
        self.targetMultiplicity = targetMultiplicity
        self.classdiagram_Association8 = classdiagram_Association8
        self.classdiagram_Association = classdiagram_Association
        self.classdiagram_Association11 = classdiagram_Association11
        
    @property
    def sourceMultiplicity(self) -> int:
        return self.__sourceMultiplicity

    @sourceMultiplicity.setter
    def sourceMultiplicity(self, sourceMultiplicity: int):
        self.__sourceMultiplicity = sourceMultiplicity

    @property
    def targetMultiplicity(self) -> int:
        return self.__targetMultiplicity

    @targetMultiplicity.setter
    def targetMultiplicity(self, targetMultiplicity: int):
        self.__targetMultiplicity = targetMultiplicity

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def classdiagram_Association11(self):
        return self.__classdiagram_Association11

    @classdiagram_Association11.setter
    def classdiagram_Association11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classdiagram_Association__classdiagram_Association11", None)
        self.__classdiagram_Association11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classdiagram_Class12"):
                opp_val = getattr(old_value, "classdiagram_Class12", None)
                if opp_val == self:
                    setattr(old_value, "classdiagram_Class12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classdiagram_Class12"):
                opp_val = getattr(value, "classdiagram_Class12", None)
                setattr(value, "classdiagram_Class12", self)

    @property
    def classdiagram_Association8(self):
        return self.__classdiagram_Association8

    @classdiagram_Association8.setter
    def classdiagram_Association8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classdiagram_Association__classdiagram_Association8", None)
        self.__classdiagram_Association8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classdiagram_Class9"):
                opp_val = getattr(old_value, "classdiagram_Class9", None)
                if opp_val == self:
                    setattr(old_value, "classdiagram_Class9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classdiagram_Class9"):
                opp_val = getattr(value, "classdiagram_Class9", None)
                setattr(value, "classdiagram_Class9", self)

    @property
    def classdiagram_Association(self):
        return self.__classdiagram_Association

    @classdiagram_Association.setter
    def classdiagram_Association(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classdiagram_Association__classdiagram_Association", None)
        self.__classdiagram_Association = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classdiagram_Diagram2"):
                opp_val = getattr(old_value, "classdiagram_Diagram2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classdiagram_Diagram2"):
                opp_val = getattr(value, "classdiagram_Diagram2", None)
                if opp_val is None:
                    setattr(value, "classdiagram_Diagram2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class classdiagram_Class(AttributeValue):

    def __init__(self, name: str, is_persistent: bool, classdiagram_Class9: "classdiagram_Association" = None, classdiagram_Class: "classdiagram_Diagram" = None, classdiagram_Class12: "classdiagram_Association" = None, classdiagram_Class14: set["classdiagram_Attribute"] = None, classdiagram_Class16: set["classdiagram_Method"] = None, classdiagram_Class32: "classdiagram_InterfaceRealization" = None, classdiagram_Class34: "classdiagram_Realization" = None, classdiagram_Class19: "classdiagram_Generalization" = None, classdiagram_Class22: "classdiagram_Generalization" = None, classdiagram_Class37: "classdiagram_Realization" = None):
        self.name = name
        self.is_persistent = is_persistent
        self.classdiagram_Class9 = classdiagram_Class9
        self.classdiagram_Class = classdiagram_Class
        self.classdiagram_Class12 = classdiagram_Class12
        self.classdiagram_Class14 = classdiagram_Class14 if classdiagram_Class14 is not None else set()
        self.classdiagram_Class16 = classdiagram_Class16 if classdiagram_Class16 is not None else set()
        self.classdiagram_Class32 = classdiagram_Class32
        self.classdiagram_Class34 = classdiagram_Class34
        self.classdiagram_Class19 = classdiagram_Class19
        self.classdiagram_Class22 = classdiagram_Class22
        self.classdiagram_Class37 = classdiagram_Class37
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def is_persistent(self) -> bool:
        return self.__is_persistent

    @is_persistent.setter
    def is_persistent(self, is_persistent: bool):
        self.__is_persistent = is_persistent

    @property
    def classdiagram_Class(self):
        return self.__classdiagram_Class

    @classdiagram_Class.setter
    def classdiagram_Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classdiagram_Class__classdiagram_Class", None)
        self.__classdiagram_Class = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classdiagram_Diagram"):
                opp_val = getattr(old_value, "classdiagram_Diagram", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classdiagram_Diagram"):
                opp_val = getattr(value, "classdiagram_Diagram", None)
                if opp_val is None:
                    setattr(value, "classdiagram_Diagram", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def classdiagram_Class9(self):
        return self.__classdiagram_Class9

    @classdiagram_Class9.setter
    def classdiagram_Class9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classdiagram_Class__classdiagram_Class9", None)
        self.__classdiagram_Class9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classdiagram_Association8"):
                opp_val = getattr(old_value, "classdiagram_Association8", None)
                if opp_val == self:
                    setattr(old_value, "classdiagram_Association8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classdiagram_Association8"):
                opp_val = getattr(value, "classdiagram_Association8", None)
                setattr(value, "classdiagram_Association8", self)

    @property
    def classdiagram_Class22(self):
        return self.__classdiagram_Class22

    @classdiagram_Class22.setter
    def classdiagram_Class22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classdiagram_Class__classdiagram_Class22", None)
        self.__classdiagram_Class22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classdiagram_Generalization21"):
                opp_val = getattr(old_value, "classdiagram_Generalization21", None)
                if opp_val == self:
                    setattr(old_value, "classdiagram_Generalization21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classdiagram_Generalization21"):
                opp_val = getattr(value, "classdiagram_Generalization21", None)
                setattr(value, "classdiagram_Generalization21", self)

    @property
    def classdiagram_Class37(self):
        return self.__classdiagram_Class37

    @classdiagram_Class37.setter
    def classdiagram_Class37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classdiagram_Class__classdiagram_Class37", None)
        self.__classdiagram_Class37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classdiagram_Realization36"):
                opp_val = getattr(old_value, "classdiagram_Realization36", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classdiagram_Realization36"):
                opp_val = getattr(value, "classdiagram_Realization36", None)
                if opp_val is None:
                    setattr(value, "classdiagram_Realization36", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def classdiagram_Class32(self):
        return self.__classdiagram_Class32

    @classdiagram_Class32.setter
    def classdiagram_Class32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classdiagram_Class__classdiagram_Class32", None)
        self.__classdiagram_Class32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classdiagram_InterfaceRealization31"):
                opp_val = getattr(old_value, "classdiagram_InterfaceRealization31", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classdiagram_InterfaceRealization31"):
                opp_val = getattr(value, "classdiagram_InterfaceRealization31", None)
                if opp_val is None:
                    setattr(value, "classdiagram_InterfaceRealization31", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def classdiagram_Class12(self):
        return self.__classdiagram_Class12

    @classdiagram_Class12.setter
    def classdiagram_Class12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classdiagram_Class__classdiagram_Class12", None)
        self.__classdiagram_Class12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classdiagram_Association11"):
                opp_val = getattr(old_value, "classdiagram_Association11", None)
                if opp_val == self:
                    setattr(old_value, "classdiagram_Association11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classdiagram_Association11"):
                opp_val = getattr(value, "classdiagram_Association11", None)
                setattr(value, "classdiagram_Association11", self)

    @property
    def classdiagram_Class16(self):
        return self.__classdiagram_Class16

    @classdiagram_Class16.setter
    def classdiagram_Class16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classdiagram_Class__classdiagram_Class16", None)
        self.__classdiagram_Class16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "classdiagram_Method"):
                    opp_val = getattr(item, "classdiagram_Method", None)
                    
                    if opp_val == self:
                        setattr(item, "classdiagram_Method", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "classdiagram_Method"):
                    opp_val = getattr(item, "classdiagram_Method", None)
                    
                    setattr(item, "classdiagram_Method", self)
                    

    @property
    def classdiagram_Class14(self):
        return self.__classdiagram_Class14

    @classdiagram_Class14.setter
    def classdiagram_Class14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classdiagram_Class__classdiagram_Class14", None)
        self.__classdiagram_Class14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "classdiagram_Attribute"):
                    opp_val = getattr(item, "classdiagram_Attribute", None)
                    
                    if opp_val == self:
                        setattr(item, "classdiagram_Attribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "classdiagram_Attribute"):
                    opp_val = getattr(item, "classdiagram_Attribute", None)
                    
                    setattr(item, "classdiagram_Attribute", self)
                    

    @property
    def classdiagram_Class19(self):
        return self.__classdiagram_Class19

    @classdiagram_Class19.setter
    def classdiagram_Class19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classdiagram_Class__classdiagram_Class19", None)
        self.__classdiagram_Class19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classdiagram_Generalization18"):
                opp_val = getattr(old_value, "classdiagram_Generalization18", None)
                if opp_val == self:
                    setattr(old_value, "classdiagram_Generalization18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classdiagram_Generalization18"):
                opp_val = getattr(value, "classdiagram_Generalization18", None)
                setattr(value, "classdiagram_Generalization18", self)

    @property
    def classdiagram_Class34(self):
        return self.__classdiagram_Class34

    @classdiagram_Class34.setter
    def classdiagram_Class34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classdiagram_Class__classdiagram_Class34", None)
        self.__classdiagram_Class34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classdiagram_Realization"):
                opp_val = getattr(old_value, "classdiagram_Realization", None)
                if opp_val == self:
                    setattr(old_value, "classdiagram_Realization", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classdiagram_Realization"):
                opp_val = getattr(value, "classdiagram_Realization", None)
                setattr(value, "classdiagram_Realization", self)

class classdiagram_Diagram:

    pass
class classdiagram_Generalization:

    pass