from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Containment(Enum):
    Source = "Source"
    Target = "Target"
    Non = "Non"
class RelationType(Enum):
    One2One = "One2One"
    One2Many = "One2Many"
    Many2Many = "Many2Many"


############################################
# Definition of Classes
############################################

class type_AttributePointer:

    pass
class type_MethodPointer:

    pass
class TypePointer:

    pass
class type_Link:

    def __init__(self, uid: str, type_Link: "type_Assosiation" = None, type_Link19: "type_Attribute" = None, type_Link21: "type_Attribute" = None):
        self.uid = uid
        self.type_Link = type_Link
        self.type_Link19 = type_Link19
        self.type_Link21 = type_Link21
        
    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def type_Link19(self):
        return self.__type_Link19

    @type_Link19.setter
    def type_Link19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_type_Link__type_Link19", None)
        self.__type_Link19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "type_Attribute"):
                opp_val = getattr(old_value, "type_Attribute", None)
                if opp_val == self:
                    setattr(old_value, "type_Attribute", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "type_Attribute"):
                opp_val = getattr(value, "type_Attribute", None)
                setattr(value, "type_Attribute", self)

    @property
    def type_Link(self):
        return self.__type_Link

    @type_Link.setter
    def type_Link(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_type_Link__type_Link", None)
        self.__type_Link = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "type_Assosiation"):
                opp_val = getattr(old_value, "type_Assosiation", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "type_Assosiation"):
                opp_val = getattr(value, "type_Assosiation", None)
                if opp_val is None:
                    setattr(value, "type_Assosiation", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def type_Link21(self):
        return self.__type_Link21

    @type_Link21.setter
    def type_Link21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_type_Link__type_Link21", None)
        self.__type_Link21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "type_Attribute22"):
                opp_val = getattr(old_value, "type_Attribute22", None)
                if opp_val == self:
                    setattr(old_value, "type_Attribute22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "type_Attribute22"):
                opp_val = getattr(value, "type_Attribute22", None)
                setattr(value, "type_Attribute22", self)

class type_PackagePointer:

    pass
class type_TypePointer:

    pass
class TypeElement:

    pass
class type_TypeReference(TypeElement, TypePointer):

    pass
class type_ReturnValue(TypePointer):

    def __init__(self, uid: str, type_ReturnValue: "type_Operation" = None):
        self.uid = uid
        self.type_ReturnValue = type_ReturnValue
        
    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def type_ReturnValue(self):
        return self.__type_ReturnValue

    @type_ReturnValue.setter
    def type_ReturnValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_type_ReturnValue__type_ReturnValue", None)
        self.__type_ReturnValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "type_Operation25"):
                opp_val = getattr(old_value, "type_Operation25", None)
                if opp_val == self:
                    setattr(old_value, "type_Operation25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "type_Operation25"):
                opp_val = getattr(value, "type_Operation25", None)
                setattr(value, "type_Operation25", self)

class type_Parameter(TypePointer):

    def __init__(self, uid: str, name: str, order: int, type_Parameter: "type_Operation" = None):
        self.uid = uid
        self.name = name
        self.order = order
        self.type_Parameter = type_Parameter
        
    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def order(self) -> int:
        return self.__order

    @order.setter
    def order(self, order: int):
        self.__order = order

    @property
    def type_Parameter(self):
        return self.__type_Parameter

    @type_Parameter.setter
    def type_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_type_Parameter__type_Parameter", None)
        self.__type_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "type_Operation"):
                opp_val = getattr(old_value, "type_Operation", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "type_Operation"):
                opp_val = getattr(value, "type_Operation", None)
                if opp_val is None:
                    setattr(value, "type_Operation", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Secured:

    pass
class type_Primitive(TypeElement):

    pass
class type_PrimitivesGroup:

    pass
class type_TypeElement:

    def __init__(self, uid: str, name: str, type_TypeElement6: "type_Relationship" = None, type_TypeElement9: "type_Relationship" = None, type_TypeElement: "type_TypeGroup" = None, type_TypeElement11: "type_TypePointer" = None):
        self.uid = uid
        self.name = name
        self.type_TypeElement6 = type_TypeElement6
        self.type_TypeElement9 = type_TypeElement9
        self.type_TypeElement = type_TypeElement
        self.type_TypeElement11 = type_TypeElement11
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def type_TypeElement9(self):
        return self.__type_TypeElement9

    @type_TypeElement9.setter
    def type_TypeElement9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_type_TypeElement__type_TypeElement9", None)
        self.__type_TypeElement9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "type_Relationship8"):
                opp_val = getattr(old_value, "type_Relationship8", None)
                if opp_val == self:
                    setattr(old_value, "type_Relationship8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "type_Relationship8"):
                opp_val = getattr(value, "type_Relationship8", None)
                setattr(value, "type_Relationship8", self)

    @property
    def type_TypeElement11(self):
        return self.__type_TypeElement11

    @type_TypeElement11.setter
    def type_TypeElement11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_type_TypeElement__type_TypeElement11", None)
        self.__type_TypeElement11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "type_TypePointer"):
                opp_val = getattr(old_value, "type_TypePointer", None)
                if opp_val == self:
                    setattr(old_value, "type_TypePointer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "type_TypePointer"):
                opp_val = getattr(value, "type_TypePointer", None)
                setattr(value, "type_TypePointer", self)

    @property
    def type_TypeElement6(self):
        return self.__type_TypeElement6

    @type_TypeElement6.setter
    def type_TypeElement6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_type_TypeElement__type_TypeElement6", None)
        self.__type_TypeElement6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "type_Relationship5"):
                opp_val = getattr(old_value, "type_Relationship5", None)
                if opp_val == self:
                    setattr(old_value, "type_Relationship5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "type_Relationship5"):
                opp_val = getattr(value, "type_Relationship5", None)
                setattr(value, "type_Relationship5", self)

    @property
    def type_TypeElement(self):
        return self.__type_TypeElement

    @type_TypeElement.setter
    def type_TypeElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_type_TypeElement__type_TypeElement", None)
        self.__type_TypeElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "type_TypeGroup"):
                opp_val = getattr(old_value, "type_TypeGroup", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "type_TypeGroup"):
                opp_val = getattr(value, "type_TypeGroup", None)
                if opp_val is None:
                    setattr(value, "type_TypeGroup", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class type_TypeGroup:

    def __init__(self, uid: str, name: str, type_TypeGroup: set["type_TypeElement"] = None, type_TypeGroup2: set["type_Relationship"] = None, type_TypeGroup13: "type_PackagePointer" = None):
        self.uid = uid
        self.name = name
        self.type_TypeGroup = type_TypeGroup if type_TypeGroup is not None else set()
        self.type_TypeGroup2 = type_TypeGroup2 if type_TypeGroup2 is not None else set()
        self.type_TypeGroup13 = type_TypeGroup13
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def type_TypeGroup(self):
        return self.__type_TypeGroup

    @type_TypeGroup.setter
    def type_TypeGroup(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_type_TypeGroup__type_TypeGroup", None)
        self.__type_TypeGroup = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "type_TypeElement"):
                    opp_val = getattr(item, "type_TypeElement", None)
                    
                    if opp_val == self:
                        setattr(item, "type_TypeElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "type_TypeElement"):
                    opp_val = getattr(item, "type_TypeElement", None)
                    
                    setattr(item, "type_TypeElement", self)
                    

    @property
    def type_TypeGroup2(self):
        return self.__type_TypeGroup2

    @type_TypeGroup2.setter
    def type_TypeGroup2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_type_TypeGroup__type_TypeGroup2", None)
        self.__type_TypeGroup2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "type_Relationship"):
                    opp_val = getattr(item, "type_Relationship", None)
                    
                    if opp_val == self:
                        setattr(item, "type_Relationship", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "type_Relationship"):
                    opp_val = getattr(item, "type_Relationship", None)
                    
                    setattr(item, "type_Relationship", self)
                    

    @property
    def type_TypeGroup13(self):
        return self.__type_TypeGroup13

    @type_TypeGroup13.setter
    def type_TypeGroup13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_type_TypeGroup__type_TypeGroup13", None)
        self.__type_TypeGroup13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "type_PackagePointer"):
                opp_val = getattr(old_value, "type_PackagePointer", None)
                if opp_val == self:
                    setattr(old_value, "type_PackagePointer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "type_PackagePointer"):
                opp_val = getattr(value, "type_PackagePointer", None)
                setattr(value, "type_PackagePointer", self)

class Relationship:

    pass
class type_Assosiation(Relationship):

    def __init__(self, type: str, containment: str, internal: bool, sourceOperation: str, targetOperation: str, type_Assosiation: set["type_Link"] = None, type_Assosiation16: "type_TypePointer" = None):
        self.type = type
        self.containment = containment
        self.internal = internal
        self.sourceOperation = sourceOperation
        self.targetOperation = targetOperation
        self.type_Assosiation = type_Assosiation if type_Assosiation is not None else set()
        self.type_Assosiation16 = type_Assosiation16
        
    @property
    def containment(self) -> str:
        return self.__containment

    @containment.setter
    def containment(self, containment: str):
        self.__containment = containment

    @property
    def internal(self) -> bool:
        return self.__internal

    @internal.setter
    def internal(self, internal: bool):
        self.__internal = internal

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def sourceOperation(self) -> str:
        return self.__sourceOperation

    @sourceOperation.setter
    def sourceOperation(self, sourceOperation: str):
        self.__sourceOperation = sourceOperation

    @property
    def targetOperation(self) -> str:
        return self.__targetOperation

    @targetOperation.setter
    def targetOperation(self, targetOperation: str):
        self.__targetOperation = targetOperation

    @property
    def type_Assosiation16(self):
        return self.__type_Assosiation16

    @type_Assosiation16.setter
    def type_Assosiation16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_type_Assosiation__type_Assosiation16", None)
        self.__type_Assosiation16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "type_TypePointer17"):
                opp_val = getattr(old_value, "type_TypePointer17", None)
                if opp_val == self:
                    setattr(old_value, "type_TypePointer17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "type_TypePointer17"):
                opp_val = getattr(value, "type_TypePointer17", None)
                setattr(value, "type_TypePointer17", self)

    @property
    def type_Assosiation(self):
        return self.__type_Assosiation

    @type_Assosiation.setter
    def type_Assosiation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_type_Assosiation__type_Assosiation", None)
        self.__type_Assosiation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "type_Link"):
                    opp_val = getattr(item, "type_Link", None)
                    
                    if opp_val == self:
                        setattr(item, "type_Link", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "type_Link"):
                    opp_val = getattr(item, "type_Link", None)
                    
                    setattr(item, "type_Link", self)
                    

class type_Generalization(Relationship):

    pass
class type_References(Relationship):

    pass
class Categorized:

    pass
class type_Attribute(Categorized, TypePointer):

    def __init__(self, uid: str, name: str, pk: bool, type_Attribute: "type_Link" = None, type_Attribute22: "type_Link" = None, type_Attribute27: "type_Type" = None, type_Attribute35: "type_AttributePointer" = None):
        self.uid = uid
        self.name = name
        self.pk = pk
        self.type_Attribute = type_Attribute
        self.type_Attribute22 = type_Attribute22
        self.type_Attribute27 = type_Attribute27
        self.type_Attribute35 = type_Attribute35
        
    @property
    def pk(self) -> bool:
        return self.__pk

    @pk.setter
    def pk(self, pk: bool):
        self.__pk = pk

    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def type_Attribute22(self):
        return self.__type_Attribute22

    @type_Attribute22.setter
    def type_Attribute22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_type_Attribute__type_Attribute22", None)
        self.__type_Attribute22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "type_Link21"):
                opp_val = getattr(old_value, "type_Link21", None)
                if opp_val == self:
                    setattr(old_value, "type_Link21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "type_Link21"):
                opp_val = getattr(value, "type_Link21", None)
                setattr(value, "type_Link21", self)

    @property
    def type_Attribute(self):
        return self.__type_Attribute

    @type_Attribute.setter
    def type_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_type_Attribute__type_Attribute", None)
        self.__type_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "type_Link19"):
                opp_val = getattr(old_value, "type_Link19", None)
                if opp_val == self:
                    setattr(old_value, "type_Link19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "type_Link19"):
                opp_val = getattr(value, "type_Link19", None)
                setattr(value, "type_Link19", self)

    @property
    def type_Attribute35(self):
        return self.__type_Attribute35

    @type_Attribute35.setter
    def type_Attribute35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_type_Attribute__type_Attribute35", None)
        self.__type_Attribute35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "type_AttributePointer"):
                opp_val = getattr(old_value, "type_AttributePointer", None)
                if opp_val == self:
                    setattr(old_value, "type_AttributePointer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "type_AttributePointer"):
                opp_val = getattr(value, "type_AttributePointer", None)
                setattr(value, "type_AttributePointer", self)

    @property
    def type_Attribute27(self):
        return self.__type_Attribute27

    @type_Attribute27.setter
    def type_Attribute27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_type_Attribute__type_Attribute27", None)
        self.__type_Attribute27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "type_Type"):
                opp_val = getattr(old_value, "type_Type", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "type_Type"):
                opp_val = getattr(value, "type_Type", None)
                if opp_val is None:
                    setattr(value, "type_Type", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class type_Enumerator(TypeElement, Categorized):

    pass
class type_Operation(Categorized, Secured):

    def __init__(self, uid: str, name: str, type_Operation: set["type_Parameter"] = None, type_Operation25: "type_ReturnValue" = None, type_Operation30: "type_Type" = None, type_Operation33: "type_MethodPointer" = None):
        self.uid = uid
        self.name = name
        self.type_Operation = type_Operation if type_Operation is not None else set()
        self.type_Operation25 = type_Operation25
        self.type_Operation30 = type_Operation30
        self.type_Operation33 = type_Operation33
        
    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def type_Operation(self):
        return self.__type_Operation

    @type_Operation.setter
    def type_Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_type_Operation__type_Operation", None)
        self.__type_Operation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "type_Parameter"):
                    opp_val = getattr(item, "type_Parameter", None)
                    
                    if opp_val == self:
                        setattr(item, "type_Parameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "type_Parameter"):
                    opp_val = getattr(item, "type_Parameter", None)
                    
                    setattr(item, "type_Parameter", self)
                    

    @property
    def type_Operation33(self):
        return self.__type_Operation33

    @type_Operation33.setter
    def type_Operation33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_type_Operation__type_Operation33", None)
        self.__type_Operation33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "type_MethodPointer"):
                opp_val = getattr(old_value, "type_MethodPointer", None)
                if opp_val == self:
                    setattr(old_value, "type_MethodPointer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "type_MethodPointer"):
                opp_val = getattr(value, "type_MethodPointer", None)
                setattr(value, "type_MethodPointer", self)

    @property
    def type_Operation25(self):
        return self.__type_Operation25

    @type_Operation25.setter
    def type_Operation25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_type_Operation__type_Operation25", None)
        self.__type_Operation25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "type_ReturnValue"):
                opp_val = getattr(old_value, "type_ReturnValue", None)
                if opp_val == self:
                    setattr(old_value, "type_ReturnValue", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "type_ReturnValue"):
                opp_val = getattr(value, "type_ReturnValue", None)
                setattr(value, "type_ReturnValue", self)

    @property
    def type_Operation30(self):
        return self.__type_Operation30

    @type_Operation30.setter
    def type_Operation30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_type_Operation__type_Operation30", None)
        self.__type_Operation30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "type_Type29"):
                opp_val = getattr(old_value, "type_Type29", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "type_Type29"):
                opp_val = getattr(value, "type_Type29", None)
                if opp_val is None:
                    setattr(value, "type_Type29", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class type_EnumAttribute(Categorized):

    def __init__(self, uid: str, name: str, value: str, type_EnumAttribute: "type_Enumerator" = None):
        self.uid = uid
        self.name = name
        self.value = value
        self.type_EnumAttribute = type_EnumAttribute
        
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
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def type_EnumAttribute(self):
        return self.__type_EnumAttribute

    @type_EnumAttribute.setter
    def type_EnumAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_type_EnumAttribute__type_EnumAttribute", None)
        self.__type_EnumAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "type_Enumerator"):
                opp_val = getattr(old_value, "type_Enumerator", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "type_Enumerator"):
                opp_val = getattr(value, "type_Enumerator", None)
                if opp_val is None:
                    setattr(value, "type_Enumerator", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class type_Type(TypeElement, Categorized):

    pass
class type_Relationship(Categorized):

    def __init__(self, uid: str, type_Relationship5: "type_TypeElement" = None, type_Relationship8: "type_TypeElement" = None, type_Relationship: "type_TypeGroup" = None):
        self.uid = uid
        self.type_Relationship5 = type_Relationship5
        self.type_Relationship8 = type_Relationship8
        self.type_Relationship = type_Relationship
        
    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def type_Relationship5(self):
        return self.__type_Relationship5

    @type_Relationship5.setter
    def type_Relationship5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_type_Relationship__type_Relationship5", None)
        self.__type_Relationship5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "type_TypeElement6"):
                opp_val = getattr(old_value, "type_TypeElement6", None)
                if opp_val == self:
                    setattr(old_value, "type_TypeElement6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "type_TypeElement6"):
                opp_val = getattr(value, "type_TypeElement6", None)
                setattr(value, "type_TypeElement6", self)

    @property
    def type_Relationship8(self):
        return self.__type_Relationship8

    @type_Relationship8.setter
    def type_Relationship8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_type_Relationship__type_Relationship8", None)
        self.__type_Relationship8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "type_TypeElement9"):
                opp_val = getattr(old_value, "type_TypeElement9", None)
                if opp_val == self:
                    setattr(old_value, "type_TypeElement9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "type_TypeElement9"):
                opp_val = getattr(value, "type_TypeElement9", None)
                setattr(value, "type_TypeElement9", self)

    @property
    def type_Relationship(self):
        return self.__type_Relationship

    @type_Relationship.setter
    def type_Relationship(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_type_Relationship__type_Relationship", None)
        self.__type_Relationship = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "type_TypeGroup2"):
                opp_val = getattr(old_value, "type_TypeGroup2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "type_TypeGroup2"):
                opp_val = getattr(value, "type_TypeGroup2", None)
                if opp_val is None:
                    setattr(value, "type_TypeGroup2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
