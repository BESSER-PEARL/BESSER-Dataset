from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class VisibilityKind(Enum):
    public = "public"
    private = "private"
    protected = "protected"
    package = "package"
class ParameterDirectionKind(Enum):
    in = "in"
    inout = "inout"
    out = "out"
    return = "return"


############################################
# Definition of Classes
############################################

class cmof_Link:

    def __init__(self, cmof_Link: "cmof_Element" = None, cmof_Link140: "cmof_Element" = None, cmof_Link143: "cmof_Association" = None):
        self.cmof_Link = cmof_Link
        self.cmof_Link140 = cmof_Link140
        self.cmof_Link143 = cmof_Link143
        
    @property
    def cmof_Link140(self):
        return self.__cmof_Link140

    @cmof_Link140.setter
    def cmof_Link140(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Link__cmof_Link140", None)
        self.__cmof_Link140 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_Element141"):
                opp_val = getattr(old_value, "cmof_Element141", None)
                if opp_val == self:
                    setattr(old_value, "cmof_Element141", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_Element141"):
                opp_val = getattr(value, "cmof_Element141", None)
                setattr(value, "cmof_Element141", self)

    @property
    def cmof_Link(self):
        return self.__cmof_Link

    @cmof_Link.setter
    def cmof_Link(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Link__cmof_Link", None)
        self.__cmof_Link = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_Element138"):
                opp_val = getattr(old_value, "cmof_Element138", None)
                if opp_val == self:
                    setattr(old_value, "cmof_Element138", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_Element138"):
                opp_val = getattr(value, "cmof_Element138", None)
                setattr(value, "cmof_Element138", self)

    @property
    def cmof_Link143(self):
        return self.__cmof_Link143

    @cmof_Link143.setter
    def cmof_Link143(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Link__cmof_Link143", None)
        self.__cmof_Link143 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_Association144"):
                opp_val = getattr(old_value, "cmof_Association144", None)
                if opp_val == self:
                    setattr(old_value, "cmof_Association144", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_Association144"):
                opp_val = getattr(value, "cmof_Association144", None)
                setattr(value, "cmof_Association144", self)

    def delete(self) -> str:
        # TODO: Implement delete method
        pass

    def equals(self, otherLink: str) -> bool:
        # TODO: Implement equals method
        pass

class cmof_Exception:

    def __init__(self, description: str, cmof_Exception: "cmof_Element" = None, cmof_Exception133: "cmof_Element" = None):
        self.description = description
        self.cmof_Exception = cmof_Exception
        self.cmof_Exception133 = cmof_Exception133
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def cmof_Exception(self):
        return self.__cmof_Exception

    @cmof_Exception.setter
    def cmof_Exception(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Exception__cmof_Exception", None)
        self.__cmof_Exception = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_Element131"):
                opp_val = getattr(old_value, "cmof_Element131", None)
                if opp_val == self:
                    setattr(old_value, "cmof_Element131", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_Element131"):
                opp_val = getattr(value, "cmof_Element131", None)
                setattr(value, "cmof_Element131", self)

    @property
    def cmof_Exception133(self):
        return self.__cmof_Exception133

    @cmof_Exception133.setter
    def cmof_Exception133(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Exception__cmof_Exception133", None)
        self.__cmof_Exception133 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_Element134"):
                opp_val = getattr(old_value, "cmof_Element134", None)
                if opp_val == self:
                    setattr(old_value, "cmof_Element134", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_Element134"):
                opp_val = getattr(value, "cmof_Element134", None)
                setattr(value, "cmof_Element134", self)

class DataType:

    pass
class cmof_Enumeration(DataType):

    pass
class cmof_PrimitiveType(DataType):

    pass
class ValueSpecification:

    pass
class cmof_Expression(ValueSpecification):

    pass
class cmof_OpaqueExpression(ValueSpecification):

    def __init__(self, body: str, language: str):
        self.body = body
        self.language = language
        
    @property
    def language(self) -> str:
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language

    @property
    def body(self) -> str:
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body

class cmof_Argument:

    def __init__(self, name: str, value: str):
        self.name = name
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class BehavioralFeature:

    pass
class Relationship:

    pass
class cmof_DirectedRelationship(Relationship):

    pass
class DirectedRelationship:

    pass
class cmof_PackageMerge(DirectedRelationship):

    pass
class PackageableElement:

    pass
class cmof_Type(PackageableElement):

    def __init__(self, cmof_Type: "cmof_TypedElement" = None, ownedType: "cmof_Package" = None, Type: "cmof_Package" = None, cmof_Type74: "cmof_Association" = None, cmof_Type105: "cmof_BehavioralFeature" = None):
        self.cmof_Type = cmof_Type
        self.ownedType = ownedType
        self.Type = Type
        self.cmof_Type74 = cmof_Type74
        self.cmof_Type105 = cmof_Type105
        
    @property
    def Type(self):
        return self.__Type

    @Type.setter
    def Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Type__Type", None)
        self.__Type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "package"):
                opp_val = getattr(old_value, "package", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "package"):
                opp_val = getattr(value, "package", None)
                if opp_val is None:
                    setattr(value, "package", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ownedType(self):
        return self.__ownedType

    @ownedType.setter
    def ownedType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Type__ownedType", None)
        self.__ownedType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Package"):
                opp_val = getattr(old_value, "Package", None)
                if opp_val == self:
                    setattr(old_value, "Package", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Package"):
                opp_val = getattr(value, "Package", None)
                setattr(value, "Package", self)

    @property
    def cmof_Type105(self):
        return self.__cmof_Type105

    @cmof_Type105.setter
    def cmof_Type105(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Type__cmof_Type105", None)
        self.__cmof_Type105 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_BehavioralFeature104"):
                opp_val = getattr(old_value, "cmof_BehavioralFeature104", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_BehavioralFeature104"):
                opp_val = getattr(value, "cmof_BehavioralFeature104", None)
                if opp_val is None:
                    setattr(value, "cmof_BehavioralFeature104", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cmof_Type74(self):
        return self.__cmof_Type74

    @cmof_Type74.setter
    def cmof_Type74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Type__cmof_Type74", None)
        self.__cmof_Type74 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_Association"):
                opp_val = getattr(old_value, "cmof_Association", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_Association"):
                opp_val = getattr(value, "cmof_Association", None)
                if opp_val is None:
                    setattr(value, "cmof_Association", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cmof_Type(self):
        return self.__cmof_Type

    @cmof_Type.setter
    def cmof_Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Type__cmof_Type", None)
        self.__cmof_Type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_TypedElement"):
                opp_val = getattr(old_value, "cmof_TypedElement", None)
                if opp_val == self:
                    setattr(old_value, "cmof_TypedElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_TypedElement"):
                opp_val = getattr(value, "cmof_TypedElement", None)
                setattr(value, "cmof_TypedElement", self)

    def conformsTo(self, other: Type) -> bool:
        # TODO: Implement conformsTo method
        pass

    def isInstance(self, object: str) -> bool:
        # TODO: Implement isInstance method
        pass

class Feature:

    pass
class RedefinableElement:

    pass
class TypedElement:

    pass
class cmof_ValueSpecification(TypedElement, PackageableElement):

    def __init__(self, cmof_ValueSpecification: "cmof_Constraint" = None, cmof_ValueSpecification127: "cmof_Expression" = None):
        self.cmof_ValueSpecification = cmof_ValueSpecification
        self.cmof_ValueSpecification127 = cmof_ValueSpecification127
        
    @property
    def cmof_ValueSpecification(self):
        return self.__cmof_ValueSpecification

    @cmof_ValueSpecification.setter
    def cmof_ValueSpecification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_ValueSpecification__cmof_ValueSpecification", None)
        self.__cmof_ValueSpecification = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_Constraint116"):
                opp_val = getattr(old_value, "cmof_Constraint116", None)
                if opp_val == self:
                    setattr(old_value, "cmof_Constraint116", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_Constraint116"):
                opp_val = getattr(value, "cmof_Constraint116", None)
                setattr(value, "cmof_Constraint116", self)

    @property
    def cmof_ValueSpecification127(self):
        return self.__cmof_ValueSpecification127

    @cmof_ValueSpecification127.setter
    def cmof_ValueSpecification127(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_ValueSpecification__cmof_ValueSpecification127", None)
        self.__cmof_ValueSpecification127 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_Expression"):
                opp_val = getattr(old_value, "cmof_Expression", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_Expression"):
                opp_val = getattr(value, "cmof_Expression", None)
                if opp_val is None:
                    setattr(value, "cmof_Expression", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def integerValue(self) -> int:
        # TODO: Implement integerValue method
        pass

    def stringValue(self) -> str:
        # TODO: Implement stringValue method
        pass

    def isNull(self) -> bool:
        # TODO: Implement isNull method
        pass

    def isComputable(self) -> bool:
        # TODO: Implement isComputable method
        pass

    def booleanValue(self) -> bool:
        # TODO: Implement booleanValue method
        pass

    def unlimitedValue(self) -> int:
        # TODO: Implement unlimitedValue method
        pass

class MultiplicityElement:

    pass
class cmof_StructuralFeature(Feature, MultiplicityElement, TypedElement):

    pass
class cmof_Parameter(MultiplicityElement, TypedElement):

    def __init__(self, direction: str, default: str, cmof_Parameter107: "cmof_Operation" = None, cmof_Parameter: "cmof_BehavioralFeature" = None):
        self.direction = direction
        self.default = default
        self.cmof_Parameter107 = cmof_Parameter107
        self.cmof_Parameter = cmof_Parameter
        
    @property
    def default(self) -> str:
        return self.__default

    @default.setter
    def default(self, default: str):
        self.__default = default

    @property
    def direction(self) -> str:
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction

    @property
    def cmof_Parameter107(self):
        return self.__cmof_Parameter107

    @cmof_Parameter107.setter
    def cmof_Parameter107(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Parameter__cmof_Parameter107", None)
        self.__cmof_Parameter107 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_Operation108"):
                opp_val = getattr(old_value, "cmof_Operation108", None)
                if opp_val == self:
                    setattr(old_value, "cmof_Operation108", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_Operation108"):
                opp_val = getattr(value, "cmof_Operation108", None)
                setattr(value, "cmof_Operation108", self)

    @property
    def cmof_Parameter(self):
        return self.__cmof_Parameter

    @cmof_Parameter.setter
    def cmof_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Parameter__cmof_Parameter", None)
        self.__cmof_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_BehavioralFeature"):
                opp_val = getattr(old_value, "cmof_BehavioralFeature", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_BehavioralFeature"):
                opp_val = getattr(value, "cmof_BehavioralFeature", None)
                if opp_val is None:
                    setattr(value, "cmof_BehavioralFeature", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class StructuralFeature:

    pass
class Classifier:

    pass
class cmof_Association(Relationship, Classifier):

    def __init__(self, isDerived: bool, Association: "cmof_Property" = None, Association31: "cmof_Property" = None, cmof_Association78: set["cmof_Property"] = None, owningAssociation: set["cmof_Property"] = None, cmof_Association: set["cmof_Type"] = None, association: set["cmof_Property"] = None, cmof_Association144: "cmof_Link" = None):
        self.isDerived = isDerived
        self.Association = Association
        self.Association31 = Association31
        self.cmof_Association78 = cmof_Association78 if cmof_Association78 is not None else set()
        self.owningAssociation = owningAssociation if owningAssociation is not None else set()
        self.cmof_Association = cmof_Association if cmof_Association is not None else set()
        self.association = association if association is not None else set()
        self.cmof_Association144 = cmof_Association144
        
    @property
    def isDerived(self) -> bool:
        return self.__isDerived

    @isDerived.setter
    def isDerived(self, isDerived: bool):
        self.__isDerived = isDerived

    @property
    def cmof_Association78(self):
        return self.__cmof_Association78

    @cmof_Association78.setter
    def cmof_Association78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Association__cmof_Association78", None)
        self.__cmof_Association78 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cmof_Property79"):
                    opp_val = getattr(item, "cmof_Property79", None)
                    
                    if opp_val == self:
                        setattr(item, "cmof_Property79", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cmof_Property79"):
                    opp_val = getattr(item, "cmof_Property79", None)
                    
                    setattr(item, "cmof_Property79", self)
                    

    @property
    def cmof_Association144(self):
        return self.__cmof_Association144

    @cmof_Association144.setter
    def cmof_Association144(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Association__cmof_Association144", None)
        self.__cmof_Association144 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_Link143"):
                opp_val = getattr(old_value, "cmof_Link143", None)
                if opp_val == self:
                    setattr(old_value, "cmof_Link143", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_Link143"):
                opp_val = getattr(value, "cmof_Link143", None)
                setattr(value, "cmof_Link143", self)

    @property
    def Association(self):
        return self.__Association

    @Association.setter
    def Association(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Association__Association", None)
        self.__Association = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ownedEnd"):
                opp_val = getattr(old_value, "ownedEnd", None)
                if opp_val == self:
                    setattr(old_value, "ownedEnd", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownedEnd"):
                opp_val = getattr(value, "ownedEnd", None)
                setattr(value, "ownedEnd", self)

    @property
    def cmof_Association(self):
        return self.__cmof_Association

    @cmof_Association.setter
    def cmof_Association(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Association__cmof_Association", None)
        self.__cmof_Association = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cmof_Type74"):
                    opp_val = getattr(item, "cmof_Type74", None)
                    
                    if opp_val == self:
                        setattr(item, "cmof_Type74", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cmof_Type74"):
                    opp_val = getattr(item, "cmof_Type74", None)
                    
                    setattr(item, "cmof_Type74", self)
                    

    @property
    def association(self):
        return self.__association

    @association.setter
    def association(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Association__association", None)
        self.__association = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Property76"):
                    opp_val = getattr(item, "Property76", None)
                    
                    if opp_val == self:
                        setattr(item, "Property76", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Property76"):
                    opp_val = getattr(item, "Property76", None)
                    
                    setattr(item, "Property76", self)
                    

    @property
    def Association31(self):
        return self.__Association31

    @Association31.setter
    def Association31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Association__Association31", None)
        self.__Association31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "memberEnd"):
                opp_val = getattr(old_value, "memberEnd", None)
                if opp_val == self:
                    setattr(old_value, "memberEnd", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "memberEnd"):
                opp_val = getattr(value, "memberEnd", None)
                setattr(value, "memberEnd", self)

    @property
    def owningAssociation(self):
        return self.__owningAssociation

    @owningAssociation.setter
    def owningAssociation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Association__owningAssociation", None)
        self.__owningAssociation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Property81"):
                    opp_val = getattr(item, "Property81", None)
                    
                    if opp_val == self:
                        setattr(item, "Property81", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Property81"):
                    opp_val = getattr(item, "Property81", None)
                    
                    setattr(item, "Property81", self)
                    

    def association_ends(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement association_ends method
        pass

class cmof_DataType(Classifier):

    pass
class cmof_Class(Classifier):

    def __init__(self, isAbstract: bool, class26: set["cmof_Operation"] = None, cmof_Class: "cmof_Class" = None, cmof_Class27: set["cmof_Class"] = None, class: set["cmof_Property"] = None, Class: "cmof_Property" = None, Class98: "cmof_Operation" = None):
        self.isAbstract = isAbstract
        self.class26 = class26 if class26 is not None else set()
        self.cmof_Class = cmof_Class
        self.cmof_Class27 = cmof_Class27 if cmof_Class27 is not None else set()
        self.class = class if class is not None else set()
        self.Class = Class
        self.Class98 = Class98
        
    @property
    def isAbstract(self) -> bool:
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: bool):
        self.__isAbstract = isAbstract

    @property
    def class(self):
        return self.__class

    @class.setter
    def class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Class__class", None)
        self.__class = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Property"):
                    opp_val = getattr(item, "Property", None)
                    
                    if opp_val == self:
                        setattr(item, "Property", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Property"):
                    opp_val = getattr(item, "Property", None)
                    
                    setattr(item, "Property", self)
                    

    @property
    def Class(self):
        return self.__Class

    @Class.setter
    def Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Class__Class", None)
        self.__Class = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ownedAttribute43"):
                opp_val = getattr(old_value, "ownedAttribute43", None)
                if opp_val == self:
                    setattr(old_value, "ownedAttribute43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownedAttribute43"):
                opp_val = getattr(value, "ownedAttribute43", None)
                setattr(value, "ownedAttribute43", self)

    @property
    def cmof_Class(self):
        return self.__cmof_Class

    @cmof_Class.setter
    def cmof_Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Class__cmof_Class", None)
        self.__cmof_Class = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_Class27"):
                opp_val = getattr(old_value, "cmof_Class27", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_Class27"):
                opp_val = getattr(value, "cmof_Class27", None)
                if opp_val is None:
                    setattr(value, "cmof_Class27", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Class98(self):
        return self.__Class98

    @Class98.setter
    def Class98(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Class__Class98", None)
        self.__Class98 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ownedOperation"):
                opp_val = getattr(old_value, "ownedOperation", None)
                if opp_val == self:
                    setattr(old_value, "ownedOperation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownedOperation"):
                opp_val = getattr(value, "ownedOperation", None)
                setattr(value, "ownedOperation", self)

    @property
    def cmof_Class27(self):
        return self.__cmof_Class27

    @cmof_Class27.setter
    def cmof_Class27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Class__cmof_Class27", None)
        self.__cmof_Class27 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cmof_Class"):
                    opp_val = getattr(item, "cmof_Class", None)
                    
                    if opp_val == self:
                        setattr(item, "cmof_Class", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cmof_Class"):
                    opp_val = getattr(item, "cmof_Class", None)
                    
                    setattr(item, "cmof_Class", self)
                    

    @property
    def class26(self):
        return self.__class26

    @class26.setter
    def class26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Class__class26", None)
        self.__class26 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Operation"):
                    opp_val = getattr(item, "Operation", None)
                    
                    if opp_val == self:
                        setattr(item, "Operation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Operation"):
                    opp_val = getattr(item, "Operation", None)
                    
                    setattr(item, "Operation", self)
                    

class cmof_Operation(BehavioralFeature, MultiplicityElement, TypedElement):

    def __init__(self, isQuery: bool, Operation: "cmof_Class" = None, Operation83: "cmof_DataType" = None, ownedOperation100: "cmof_DataType" = None, cmof_Operation: "cmof_Operation" = None, cmof_Operation87: set["cmof_Operation"] = None, cmof_Operation90: set["cmof_Constraint"] = None, cmof_Operation92: set["cmof_Constraint"] = None, cmof_Operation95: set["cmof_Constraint"] = None, ownedOperation: "cmof_Class" = None, cmof_Operation108: "cmof_Parameter" = None):
        self.isQuery = isQuery
        self.Operation = Operation
        self.Operation83 = Operation83
        self.ownedOperation100 = ownedOperation100
        self.cmof_Operation = cmof_Operation
        self.cmof_Operation87 = cmof_Operation87 if cmof_Operation87 is not None else set()
        self.cmof_Operation90 = cmof_Operation90 if cmof_Operation90 is not None else set()
        self.cmof_Operation92 = cmof_Operation92 if cmof_Operation92 is not None else set()
        self.cmof_Operation95 = cmof_Operation95 if cmof_Operation95 is not None else set()
        self.ownedOperation = ownedOperation
        self.cmof_Operation108 = cmof_Operation108
        
    @property
    def isQuery(self) -> bool:
        return self.__isQuery

    @isQuery.setter
    def isQuery(self, isQuery: bool):
        self.__isQuery = isQuery

    @property
    def cmof_Operation108(self):
        return self.__cmof_Operation108

    @cmof_Operation108.setter
    def cmof_Operation108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Operation__cmof_Operation108", None)
        self.__cmof_Operation108 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_Parameter107"):
                opp_val = getattr(old_value, "cmof_Parameter107", None)
                if opp_val == self:
                    setattr(old_value, "cmof_Parameter107", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_Parameter107"):
                opp_val = getattr(value, "cmof_Parameter107", None)
                setattr(value, "cmof_Parameter107", self)

    @property
    def Operation(self):
        return self.__Operation

    @Operation.setter
    def Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Operation__Operation", None)
        self.__Operation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "class26"):
                opp_val = getattr(old_value, "class26", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "class26"):
                opp_val = getattr(value, "class26", None)
                if opp_val is None:
                    setattr(value, "class26", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Operation83(self):
        return self.__Operation83

    @Operation83.setter
    def Operation83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Operation__Operation83", None)
        self.__Operation83 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "datatype"):
                opp_val = getattr(old_value, "datatype", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "datatype"):
                opp_val = getattr(value, "datatype", None)
                if opp_val is None:
                    setattr(value, "datatype", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ownedOperation(self):
        return self.__ownedOperation

    @ownedOperation.setter
    def ownedOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Operation__ownedOperation", None)
        self.__ownedOperation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Class98"):
                opp_val = getattr(old_value, "Class98", None)
                if opp_val == self:
                    setattr(old_value, "Class98", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Class98"):
                opp_val = getattr(value, "Class98", None)
                setattr(value, "Class98", self)

    @property
    def ownedOperation100(self):
        return self.__ownedOperation100

    @ownedOperation100.setter
    def ownedOperation100(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Operation__ownedOperation100", None)
        self.__ownedOperation100 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DataType101"):
                opp_val = getattr(old_value, "DataType101", None)
                if opp_val == self:
                    setattr(old_value, "DataType101", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DataType101"):
                opp_val = getattr(value, "DataType101", None)
                setattr(value, "DataType101", self)

    @property
    def cmof_Operation92(self):
        return self.__cmof_Operation92

    @cmof_Operation92.setter
    def cmof_Operation92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Operation__cmof_Operation92", None)
        self.__cmof_Operation92 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cmof_Constraint93"):
                    opp_val = getattr(item, "cmof_Constraint93", None)
                    
                    if opp_val == self:
                        setattr(item, "cmof_Constraint93", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cmof_Constraint93"):
                    opp_val = getattr(item, "cmof_Constraint93", None)
                    
                    setattr(item, "cmof_Constraint93", self)
                    

    @property
    def cmof_Operation95(self):
        return self.__cmof_Operation95

    @cmof_Operation95.setter
    def cmof_Operation95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Operation__cmof_Operation95", None)
        self.__cmof_Operation95 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cmof_Constraint96"):
                    opp_val = getattr(item, "cmof_Constraint96", None)
                    
                    if opp_val == self:
                        setattr(item, "cmof_Constraint96", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cmof_Constraint96"):
                    opp_val = getattr(item, "cmof_Constraint96", None)
                    
                    setattr(item, "cmof_Constraint96", self)
                    

    @property
    def cmof_Operation87(self):
        return self.__cmof_Operation87

    @cmof_Operation87.setter
    def cmof_Operation87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Operation__cmof_Operation87", None)
        self.__cmof_Operation87 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cmof_Operation"):
                    opp_val = getattr(item, "cmof_Operation", None)
                    
                    if opp_val == self:
                        setattr(item, "cmof_Operation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cmof_Operation"):
                    opp_val = getattr(item, "cmof_Operation", None)
                    
                    setattr(item, "cmof_Operation", self)
                    

    @property
    def cmof_Operation90(self):
        return self.__cmof_Operation90

    @cmof_Operation90.setter
    def cmof_Operation90(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Operation__cmof_Operation90", None)
        self.__cmof_Operation90 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cmof_Constraint"):
                    opp_val = getattr(item, "cmof_Constraint", None)
                    
                    if opp_val == self:
                        setattr(item, "cmof_Constraint", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cmof_Constraint"):
                    opp_val = getattr(item, "cmof_Constraint", None)
                    
                    setattr(item, "cmof_Constraint", self)
                    

    @property
    def cmof_Operation(self):
        return self.__cmof_Operation

    @cmof_Operation.setter
    def cmof_Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Operation__cmof_Operation", None)
        self.__cmof_Operation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_Operation87"):
                opp_val = getattr(old_value, "cmof_Operation87", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_Operation87"):
                opp_val = getattr(value, "cmof_Operation87", None)
                if opp_val is None:
                    setattr(value, "cmof_Operation87", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def isOrdered(self) -> bool:
        # TODO: Implement isOrdered method
        pass

    def only_body_for_query(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement only_body_for_query method
        pass

    def getType(self) -> Type:
        # TODO: Implement getType method
        pass

    def isUnique(self) -> bool:
        # TODO: Implement isUnique method
        pass

    def returnResult(self) -> str:
        # TODO: Implement returnResult method
        pass

    def at_most_one_return(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement at_most_one_return method
        pass

class cmof_Element(ABC):

    def __init__(self, Element: "cmof_Element" = None, owner: set["cmof_Element"] = None, Element19: "cmof_Element" = None, ownedElement: "cmof_Element" = None, cmof_Element: set["cmof_Comment"] = None, cmof_Element23: "cmof_Comment" = None, cmof_Element70: "cmof_DirectedRelationship" = None, cmof_Element67: "cmof_DirectedRelationship" = None, cmof_Element72: "cmof_Relationship" = None, cmof_Element114: "cmof_Constraint" = None, cmof_Element131: "cmof_Exception" = None, cmof_Element134: "cmof_Exception" = None, cmof_Element146: "cmof_Tag" = None, cmof_Element138: "cmof_Link" = None, cmof_Element141: "cmof_Link" = None):
        self.Element = Element
        self.owner = owner if owner is not None else set()
        self.Element19 = Element19
        self.ownedElement = ownedElement
        self.cmof_Element = cmof_Element if cmof_Element is not None else set()
        self.cmof_Element23 = cmof_Element23
        self.cmof_Element70 = cmof_Element70
        self.cmof_Element67 = cmof_Element67
        self.cmof_Element72 = cmof_Element72
        self.cmof_Element114 = cmof_Element114
        self.cmof_Element131 = cmof_Element131
        self.cmof_Element134 = cmof_Element134
        self.cmof_Element146 = cmof_Element146
        self.cmof_Element138 = cmof_Element138
        self.cmof_Element141 = cmof_Element141
        
    @property
    def cmof_Element131(self):
        return self.__cmof_Element131

    @cmof_Element131.setter
    def cmof_Element131(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Element__cmof_Element131", None)
        self.__cmof_Element131 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_Exception"):
                opp_val = getattr(old_value, "cmof_Exception", None)
                if opp_val == self:
                    setattr(old_value, "cmof_Exception", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_Exception"):
                opp_val = getattr(value, "cmof_Exception", None)
                setattr(value, "cmof_Exception", self)

    @property
    def Element19(self):
        return self.__Element19

    @Element19.setter
    def Element19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Element__Element19", None)
        self.__Element19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ownedElement"):
                opp_val = getattr(old_value, "ownedElement", None)
                if opp_val == self:
                    setattr(old_value, "ownedElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownedElement"):
                opp_val = getattr(value, "ownedElement", None)
                setattr(value, "ownedElement", self)

    @property
    def cmof_Element72(self):
        return self.__cmof_Element72

    @cmof_Element72.setter
    def cmof_Element72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Element__cmof_Element72", None)
        self.__cmof_Element72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_Relationship"):
                opp_val = getattr(old_value, "cmof_Relationship", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_Relationship"):
                opp_val = getattr(value, "cmof_Relationship", None)
                if opp_val is None:
                    setattr(value, "cmof_Relationship", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ownedElement(self):
        return self.__ownedElement

    @ownedElement.setter
    def ownedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Element__ownedElement", None)
        self.__ownedElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Element19"):
                opp_val = getattr(old_value, "Element19", None)
                if opp_val == self:
                    setattr(old_value, "Element19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Element19"):
                opp_val = getattr(value, "Element19", None)
                setattr(value, "Element19", self)

    @property
    def cmof_Element23(self):
        return self.__cmof_Element23

    @cmof_Element23.setter
    def cmof_Element23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Element__cmof_Element23", None)
        self.__cmof_Element23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_Comment22"):
                opp_val = getattr(old_value, "cmof_Comment22", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_Comment22"):
                opp_val = getattr(value, "cmof_Comment22", None)
                if opp_val is None:
                    setattr(value, "cmof_Comment22", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cmof_Element114(self):
        return self.__cmof_Element114

    @cmof_Element114.setter
    def cmof_Element114(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Element__cmof_Element114", None)
        self.__cmof_Element114 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_Constraint113"):
                opp_val = getattr(old_value, "cmof_Constraint113", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_Constraint113"):
                opp_val = getattr(value, "cmof_Constraint113", None)
                if opp_val is None:
                    setattr(value, "cmof_Constraint113", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cmof_Element141(self):
        return self.__cmof_Element141

    @cmof_Element141.setter
    def cmof_Element141(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Element__cmof_Element141", None)
        self.__cmof_Element141 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_Link140"):
                opp_val = getattr(old_value, "cmof_Link140", None)
                if opp_val == self:
                    setattr(old_value, "cmof_Link140", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_Link140"):
                opp_val = getattr(value, "cmof_Link140", None)
                setattr(value, "cmof_Link140", self)

    @property
    def cmof_Element67(self):
        return self.__cmof_Element67

    @cmof_Element67.setter
    def cmof_Element67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Element__cmof_Element67", None)
        self.__cmof_Element67 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_DirectedRelationship"):
                opp_val = getattr(old_value, "cmof_DirectedRelationship", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_DirectedRelationship"):
                opp_val = getattr(value, "cmof_DirectedRelationship", None)
                if opp_val is None:
                    setattr(value, "cmof_DirectedRelationship", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cmof_Element134(self):
        return self.__cmof_Element134

    @cmof_Element134.setter
    def cmof_Element134(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Element__cmof_Element134", None)
        self.__cmof_Element134 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_Exception133"):
                opp_val = getattr(old_value, "cmof_Exception133", None)
                if opp_val == self:
                    setattr(old_value, "cmof_Exception133", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_Exception133"):
                opp_val = getattr(value, "cmof_Exception133", None)
                setattr(value, "cmof_Exception133", self)

    @property
    def cmof_Element138(self):
        return self.__cmof_Element138

    @cmof_Element138.setter
    def cmof_Element138(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Element__cmof_Element138", None)
        self.__cmof_Element138 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_Link"):
                opp_val = getattr(old_value, "cmof_Link", None)
                if opp_val == self:
                    setattr(old_value, "cmof_Link", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_Link"):
                opp_val = getattr(value, "cmof_Link", None)
                setattr(value, "cmof_Link", self)

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Element__owner", None)
        self.__owner = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Element"):
                    opp_val = getattr(item, "Element", None)
                    
                    if opp_val == self:
                        setattr(item, "Element", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Element"):
                    opp_val = getattr(item, "Element", None)
                    
                    setattr(item, "Element", self)
                    

    @property
    def cmof_Element70(self):
        return self.__cmof_Element70

    @cmof_Element70.setter
    def cmof_Element70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Element__cmof_Element70", None)
        self.__cmof_Element70 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_DirectedRelationship69"):
                opp_val = getattr(old_value, "cmof_DirectedRelationship69", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_DirectedRelationship69"):
                opp_val = getattr(value, "cmof_DirectedRelationship69", None)
                if opp_val is None:
                    setattr(value, "cmof_DirectedRelationship69", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cmof_Element(self):
        return self.__cmof_Element

    @cmof_Element.setter
    def cmof_Element(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Element__cmof_Element", None)
        self.__cmof_Element = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cmof_Comment"):
                    opp_val = getattr(item, "cmof_Comment", None)
                    
                    if opp_val == self:
                        setattr(item, "cmof_Comment", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cmof_Comment"):
                    opp_val = getattr(item, "cmof_Comment", None)
                    
                    setattr(item, "cmof_Comment", self)
                    

    @property
    def Element(self):
        return self.__Element

    @Element.setter
    def Element(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Element__Element", None)
        self.__Element = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owner"):
                opp_val = getattr(old_value, "owner", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owner"):
                opp_val = getattr(value, "owner", None)
                if opp_val is None:
                    setattr(value, "owner", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cmof_Element146(self):
        return self.__cmof_Element146

    @cmof_Element146.setter
    def cmof_Element146(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Element__cmof_Element146", None)
        self.__cmof_Element146 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_Tag"):
                opp_val = getattr(old_value, "cmof_Tag", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_Tag"):
                opp_val = getattr(value, "cmof_Tag", None)
                if opp_val is None:
                    setattr(value, "cmof_Tag", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def unset(self, property: str) -> str:
        # TODO: Implement unset method
        pass

    def equals(self, otherElement: str) -> bool:
        # TODO: Implement equals method
        pass

    def delete(self) -> str:
        # TODO: Implement delete method
        pass

    def container(self) -> Element:
        # TODO: Implement container method
        pass

    def verify(self, deepVerify: bool) -> str:
        # TODO: Implement verify method
        pass

    def invoke(self, arguments: str, op: str) -> str:
        # TODO: Implement invoke method
        pass

    def set(self, value: str, property: str) -> str:
        # TODO: Implement set method
        pass

    def allOwnedElements(self) -> Element:
        # TODO: Implement allOwnedElements method
        pass

    def get(self, property: str) -> str:
        # TODO: Implement get method
        pass

    def not_own_self(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement not_own_self method
        pass

    def isSet(self, property: str) -> bool:
        # TODO: Implement isSet method
        pass

    def isInstanceOfType(self, type: str, includeSubtypes: bool) -> bool:
        # TODO: Implement isInstanceOfType method
        pass

    def mustBeOwned(self) -> bool:
        # TODO: Implement mustBeOwned method
        pass

    def has_owner(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement has_owner method
        pass

    def getMetaClass(self) -> str:
        # TODO: Implement getMetaClass method
        pass

class Element:

    pass
class cmof_MultiplicityElement(Element):

    def __init__(self, lower: int, upper: int, isOrdered: bool, isUnique: bool):
        self.lower = lower
        self.upper = upper
        self.isOrdered = isOrdered
        self.isUnique = isUnique
        
    @property
    def upper(self) -> int:
        return self.__upper

    @upper.setter
    def upper(self, upper: int):
        self.__upper = upper

    @property
    def isUnique(self) -> bool:
        return self.__isUnique

    @isUnique.setter
    def isUnique(self, isUnique: bool):
        self.__isUnique = isUnique

    @property
    def isOrdered(self) -> bool:
        return self.__isOrdered

    @isOrdered.setter
    def isOrdered(self, isOrdered: bool):
        self.__isOrdered = isOrdered

    @property
    def lower(self) -> int:
        return self.__lower

    @lower.setter
    def lower(self, lower: int):
        self.__lower = lower

    def lower_ge_0(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement lower_ge_0 method
        pass

    def isMultivalued(self) -> bool:
        # TODO: Implement isMultivalued method
        pass

    def upper_gt_0(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement upper_gt_0 method
        pass

    def includesCardinality(self, C: int) -> bool:
        # TODO: Implement includesCardinality method
        pass

    def upperBound(self) -> int:
        # TODO: Implement upperBound method
        pass

    def lowerBound(self) -> int:
        # TODO: Implement lowerBound method
        pass

    def includesMultiplicity(self, M: MultiplicityElement) -> bool:
        # TODO: Implement includesMultiplicity method
        pass

    def upper_ge_lower(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement upper_ge_lower method
        pass

class cmof_Factory(Element):

    def __init__(self, cmof_Factory: "cmof_Package" = None):
        self.cmof_Factory = cmof_Factory
        
    @property
    def cmof_Factory(self):
        return self.__cmof_Factory

    @cmof_Factory.setter
    def cmof_Factory(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Factory__cmof_Factory", None)
        self.__cmof_Factory = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_Package136"):
                opp_val = getattr(old_value, "cmof_Package136", None)
                if opp_val == self:
                    setattr(old_value, "cmof_Package136", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_Package136"):
                opp_val = getattr(value, "cmof_Package136", None)
                setattr(value, "cmof_Package136", self)

    def createElement(self, arguments: str, aClass: str) -> Element:
        # TODO: Implement createElement method
        pass

    def createFromString(self, string: str, dataType: DataType) -> str:
        # TODO: Implement createFromString method
        pass

    def createLink(self, secondElement: Element, firstElement: Element, association: str) -> str:
        # TODO: Implement createLink method
        pass

    def convertToString(self, object: str, dataType: DataType) -> str:
        # TODO: Implement convertToString method
        pass

    def create(self, metaClass: str) -> Element:
        # TODO: Implement create method
        pass

class cmof_Relationship(Element):

    pass
class cmof_Comment(Element):

    def __init__(self, body: str, cmof_Comment: "cmof_Element" = None, cmof_Comment22: set["cmof_Element"] = None):
        self.body = body
        self.cmof_Comment = cmof_Comment
        self.cmof_Comment22 = cmof_Comment22 if cmof_Comment22 is not None else set()
        
    @property
    def body(self) -> str:
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body

    @property
    def cmof_Comment(self):
        return self.__cmof_Comment

    @cmof_Comment.setter
    def cmof_Comment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Comment__cmof_Comment", None)
        self.__cmof_Comment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_Element"):
                opp_val = getattr(old_value, "cmof_Element", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_Element"):
                opp_val = getattr(value, "cmof_Element", None)
                if opp_val is None:
                    setattr(value, "cmof_Element", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cmof_Comment22(self):
        return self.__cmof_Comment22

    @cmof_Comment22.setter
    def cmof_Comment22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Comment__cmof_Comment22", None)
        self.__cmof_Comment22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cmof_Element23"):
                    opp_val = getattr(item, "cmof_Element23", None)
                    
                    if opp_val == self:
                        setattr(item, "cmof_Element23", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cmof_Element23"):
                    opp_val = getattr(item, "cmof_Element23", None)
                    
                    setattr(item, "cmof_Element23", self)
                    

class cmof_Tag(Element):

    def __init__(self, name: str, value: str, cmof_Tag: set["cmof_Element"] = None):
        self.name = name
        self.value = value
        self.cmof_Tag = cmof_Tag if cmof_Tag is not None else set()
        
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
    def cmof_Tag(self):
        return self.__cmof_Tag

    @cmof_Tag.setter
    def cmof_Tag(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Tag__cmof_Tag", None)
        self.__cmof_Tag = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cmof_Element146"):
                    opp_val = getattr(item, "cmof_Element146", None)
                    
                    if opp_val == self:
                        setattr(item, "cmof_Element146", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cmof_Element146"):
                    opp_val = getattr(item, "cmof_Element146", None)
                    
                    setattr(item, "cmof_Element146", self)
                    

class cmof_ElementImport(DirectedRelationship):

    def __init__(self, visibility: str, alias: str, ElementImport: "cmof_Namespace" = None, cmof_ElementImport: "cmof_PackageableElement" = None, elementImport: "cmof_Namespace" = None):
        self.visibility = visibility
        self.alias = alias
        self.ElementImport = ElementImport
        self.cmof_ElementImport = cmof_ElementImport
        self.elementImport = elementImport
        
    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

    @property
    def alias(self) -> str:
        return self.__alias

    @alias.setter
    def alias(self, alias: str):
        self.__alias = alias

    @property
    def cmof_ElementImport(self):
        return self.__cmof_ElementImport

    @cmof_ElementImport.setter
    def cmof_ElementImport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_ElementImport__cmof_ElementImport", None)
        self.__cmof_ElementImport = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_PackageableElement119"):
                opp_val = getattr(old_value, "cmof_PackageableElement119", None)
                if opp_val == self:
                    setattr(old_value, "cmof_PackageableElement119", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_PackageableElement119"):
                opp_val = getattr(value, "cmof_PackageableElement119", None)
                setattr(value, "cmof_PackageableElement119", self)

    @property
    def ElementImport(self):
        return self.__ElementImport

    @ElementImport.setter
    def ElementImport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_ElementImport__ElementImport", None)
        self.__ElementImport = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "importingNamespace"):
                opp_val = getattr(old_value, "importingNamespace", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "importingNamespace"):
                opp_val = getattr(value, "importingNamespace", None)
                if opp_val is None:
                    setattr(value, "importingNamespace", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def elementImport(self):
        return self.__elementImport

    @elementImport.setter
    def elementImport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_ElementImport__elementImport", None)
        self.__elementImport = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Namespace121"):
                opp_val = getattr(old_value, "Namespace121", None)
                if opp_val == self:
                    setattr(old_value, "Namespace121", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Namespace121"):
                opp_val = getattr(value, "Namespace121", None)
                setattr(value, "Namespace121", self)

    def getName(self) -> str:
        # TODO: Implement getName method
        pass

    def imported_element_is_public(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement imported_element_is_public method
        pass

    def visibility_public_or_private(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement visibility_public_or_private method
        pass

class cmof_Constraint(PackageableElement):

    def __init__(self, Constraint: "cmof_Namespace" = None, cmof_Constraint: "cmof_Operation" = None, cmof_Constraint93: "cmof_Operation" = None, cmof_Constraint96: "cmof_Operation" = None, cmof_Constraint110: "cmof_Namespace" = None, cmof_Constraint113: set["cmof_Element"] = None, cmof_Constraint116: "cmof_ValueSpecification" = None, ownedRule: "cmof_Namespace" = None):
        self.Constraint = Constraint
        self.cmof_Constraint = cmof_Constraint
        self.cmof_Constraint93 = cmof_Constraint93
        self.cmof_Constraint96 = cmof_Constraint96
        self.cmof_Constraint110 = cmof_Constraint110
        self.cmof_Constraint113 = cmof_Constraint113 if cmof_Constraint113 is not None else set()
        self.cmof_Constraint116 = cmof_Constraint116
        self.ownedRule = ownedRule
        
    @property
    def cmof_Constraint113(self):
        return self.__cmof_Constraint113

    @cmof_Constraint113.setter
    def cmof_Constraint113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Constraint__cmof_Constraint113", None)
        self.__cmof_Constraint113 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cmof_Element114"):
                    opp_val = getattr(item, "cmof_Element114", None)
                    
                    if opp_val == self:
                        setattr(item, "cmof_Element114", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cmof_Element114"):
                    opp_val = getattr(item, "cmof_Element114", None)
                    
                    setattr(item, "cmof_Element114", self)
                    

    @property
    def cmof_Constraint116(self):
        return self.__cmof_Constraint116

    @cmof_Constraint116.setter
    def cmof_Constraint116(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Constraint__cmof_Constraint116", None)
        self.__cmof_Constraint116 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_ValueSpecification"):
                opp_val = getattr(old_value, "cmof_ValueSpecification", None)
                if opp_val == self:
                    setattr(old_value, "cmof_ValueSpecification", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_ValueSpecification"):
                opp_val = getattr(value, "cmof_ValueSpecification", None)
                setattr(value, "cmof_ValueSpecification", self)

    @property
    def cmof_Constraint110(self):
        return self.__cmof_Constraint110

    @cmof_Constraint110.setter
    def cmof_Constraint110(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Constraint__cmof_Constraint110", None)
        self.__cmof_Constraint110 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_Namespace111"):
                opp_val = getattr(old_value, "cmof_Namespace111", None)
                if opp_val == self:
                    setattr(old_value, "cmof_Namespace111", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_Namespace111"):
                opp_val = getattr(value, "cmof_Namespace111", None)
                setattr(value, "cmof_Namespace111", self)

    @property
    def cmof_Constraint96(self):
        return self.__cmof_Constraint96

    @cmof_Constraint96.setter
    def cmof_Constraint96(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Constraint__cmof_Constraint96", None)
        self.__cmof_Constraint96 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_Operation95"):
                opp_val = getattr(old_value, "cmof_Operation95", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_Operation95"):
                opp_val = getattr(value, "cmof_Operation95", None)
                if opp_val is None:
                    setattr(value, "cmof_Operation95", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cmof_Constraint93(self):
        return self.__cmof_Constraint93

    @cmof_Constraint93.setter
    def cmof_Constraint93(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Constraint__cmof_Constraint93", None)
        self.__cmof_Constraint93 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_Operation92"):
                opp_val = getattr(old_value, "cmof_Operation92", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_Operation92"):
                opp_val = getattr(value, "cmof_Operation92", None)
                if opp_val is None:
                    setattr(value, "cmof_Operation92", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cmof_Constraint(self):
        return self.__cmof_Constraint

    @cmof_Constraint.setter
    def cmof_Constraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Constraint__cmof_Constraint", None)
        self.__cmof_Constraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_Operation90"):
                opp_val = getattr(old_value, "cmof_Operation90", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_Operation90"):
                opp_val = getattr(value, "cmof_Operation90", None)
                if opp_val is None:
                    setattr(value, "cmof_Operation90", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ownedRule(self):
        return self.__ownedRule

    @ownedRule.setter
    def ownedRule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Constraint__ownedRule", None)
        self.__ownedRule = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Namespace"):
                opp_val = getattr(old_value, "Namespace", None)
                if opp_val == self:
                    setattr(old_value, "Namespace", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Namespace"):
                opp_val = getattr(value, "Namespace", None)
                setattr(value, "Namespace", self)

    @property
    def Constraint(self):
        return self.__Constraint

    @Constraint.setter
    def Constraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Constraint__Constraint", None)
        self.__Constraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "namespace"):
                opp_val = getattr(old_value, "namespace", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "namespace"):
                opp_val = getattr(value, "namespace", None)
                if opp_val is None:
                    setattr(value, "namespace", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def not_apply_to_self(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement not_apply_to_self method
        pass

    def value_specification_boolean(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement value_specification_boolean method
        pass

class cmof_PackageImport(DirectedRelationship):

    def __init__(self, visibility: str, PackageImport: "cmof_Namespace" = None, cmof_PackageImport: "cmof_Package" = None, packageImport: "cmof_Namespace" = None):
        self.visibility = visibility
        self.PackageImport = PackageImport
        self.cmof_PackageImport = cmof_PackageImport
        self.packageImport = packageImport
        
    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

    @property
    def cmof_PackageImport(self):
        return self.__cmof_PackageImport

    @cmof_PackageImport.setter
    def cmof_PackageImport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_PackageImport__cmof_PackageImport", None)
        self.__cmof_PackageImport = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_Package123"):
                opp_val = getattr(old_value, "cmof_Package123", None)
                if opp_val == self:
                    setattr(old_value, "cmof_Package123", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_Package123"):
                opp_val = getattr(value, "cmof_Package123", None)
                setattr(value, "cmof_Package123", self)

    @property
    def PackageImport(self):
        return self.__PackageImport

    @PackageImport.setter
    def PackageImport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_PackageImport__PackageImport", None)
        self.__PackageImport = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "importingNamespace11"):
                opp_val = getattr(old_value, "importingNamespace11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "importingNamespace11"):
                opp_val = getattr(value, "importingNamespace11", None)
                if opp_val is None:
                    setattr(value, "importingNamespace11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def packageImport(self):
        return self.__packageImport

    @packageImport.setter
    def packageImport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_PackageImport__packageImport", None)
        self.__packageImport = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Namespace125"):
                opp_val = getattr(old_value, "Namespace125", None)
                if opp_val == self:
                    setattr(old_value, "Namespace125", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Namespace125"):
                opp_val = getattr(value, "Namespace125", None)
                setattr(value, "Namespace125", self)

    def public_or_private(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement public_or_private method
        pass

class NamedElement:

    pass
class cmof_TypedElement(NamedElement):

    pass
class cmof_RedefinableElement(NamedElement):

    def __init__(self, cmof_RedefinableElement: set["cmof_Classifier"] = None, cmof_RedefinableElement49: "cmof_RedefinableElement" = None, cmof_RedefinableElement47: set["cmof_RedefinableElement"] = None):
        self.cmof_RedefinableElement = cmof_RedefinableElement if cmof_RedefinableElement is not None else set()
        self.cmof_RedefinableElement49 = cmof_RedefinableElement49
        self.cmof_RedefinableElement47 = cmof_RedefinableElement47 if cmof_RedefinableElement47 is not None else set()
        
    @property
    def cmof_RedefinableElement(self):
        return self.__cmof_RedefinableElement

    @cmof_RedefinableElement.setter
    def cmof_RedefinableElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_RedefinableElement__cmof_RedefinableElement", None)
        self.__cmof_RedefinableElement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cmof_Classifier46"):
                    opp_val = getattr(item, "cmof_Classifier46", None)
                    
                    if opp_val == self:
                        setattr(item, "cmof_Classifier46", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cmof_Classifier46"):
                    opp_val = getattr(item, "cmof_Classifier46", None)
                    
                    setattr(item, "cmof_Classifier46", self)
                    

    @property
    def cmof_RedefinableElement49(self):
        return self.__cmof_RedefinableElement49

    @cmof_RedefinableElement49.setter
    def cmof_RedefinableElement49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_RedefinableElement__cmof_RedefinableElement49", None)
        self.__cmof_RedefinableElement49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_RedefinableElement47"):
                opp_val = getattr(old_value, "cmof_RedefinableElement47", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_RedefinableElement47"):
                opp_val = getattr(value, "cmof_RedefinableElement47", None)
                if opp_val is None:
                    setattr(value, "cmof_RedefinableElement47", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cmof_RedefinableElement47(self):
        return self.__cmof_RedefinableElement47

    @cmof_RedefinableElement47.setter
    def cmof_RedefinableElement47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_RedefinableElement__cmof_RedefinableElement47", None)
        self.__cmof_RedefinableElement47 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cmof_RedefinableElement49"):
                    opp_val = getattr(item, "cmof_RedefinableElement49", None)
                    
                    if opp_val == self:
                        setattr(item, "cmof_RedefinableElement49", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cmof_RedefinableElement49"):
                    opp_val = getattr(item, "cmof_RedefinableElement49", None)
                    
                    setattr(item, "cmof_RedefinableElement49", self)
                    

    def isRedefinitionContextValid(self, redefinable: RedefinableElement) -> bool:
        # TODO: Implement isRedefinitionContextValid method
        pass

    def isConsistentWith(self, redefinee: RedefinableElement) -> bool:
        # TODO: Implement isConsistentWith method
        pass

    def redefinition_context_valid(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement redefinition_context_valid method
        pass

    def redefinition_consistent(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement redefinition_consistent method
        pass

class cmof_EnumerationLiteral(NamedElement):

    pass
class cmof_PackageableElement(NamedElement):

    pass
class cmof_Namespace(NamedElement):

    def __init__(self, importingNamespace11: set["cmof_PackageImport"] = None, namespace: set["cmof_Constraint"] = None, cmof_Namespace: set["cmof_PackageableElement"] = None, importingNamespace: set["cmof_ElementImport"] = None, cmof_Namespace13: set["cmof_NamedElement"] = None, cmof_Namespace111: "cmof_Constraint" = None, Namespace: "cmof_Constraint" = None, Namespace121: "cmof_ElementImport" = None, Namespace125: "cmof_PackageImport" = None):
        self.importingNamespace11 = importingNamespace11 if importingNamespace11 is not None else set()
        self.namespace = namespace if namespace is not None else set()
        self.cmof_Namespace = cmof_Namespace if cmof_Namespace is not None else set()
        self.importingNamespace = importingNamespace if importingNamespace is not None else set()
        self.cmof_Namespace13 = cmof_Namespace13 if cmof_Namespace13 is not None else set()
        self.cmof_Namespace111 = cmof_Namespace111
        self.Namespace = Namespace
        self.Namespace121 = Namespace121
        self.Namespace125 = Namespace125
        
    @property
    def Namespace125(self):
        return self.__Namespace125

    @Namespace125.setter
    def Namespace125(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Namespace__Namespace125", None)
        self.__Namespace125 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "packageImport"):
                opp_val = getattr(old_value, "packageImport", None)
                if opp_val == self:
                    setattr(old_value, "packageImport", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "packageImport"):
                opp_val = getattr(value, "packageImport", None)
                setattr(value, "packageImport", self)

    @property
    def cmof_Namespace111(self):
        return self.__cmof_Namespace111

    @cmof_Namespace111.setter
    def cmof_Namespace111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Namespace__cmof_Namespace111", None)
        self.__cmof_Namespace111 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_Constraint110"):
                opp_val = getattr(old_value, "cmof_Constraint110", None)
                if opp_val == self:
                    setattr(old_value, "cmof_Constraint110", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_Constraint110"):
                opp_val = getattr(value, "cmof_Constraint110", None)
                setattr(value, "cmof_Constraint110", self)

    @property
    def Namespace121(self):
        return self.__Namespace121

    @Namespace121.setter
    def Namespace121(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Namespace__Namespace121", None)
        self.__Namespace121 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "elementImport"):
                opp_val = getattr(old_value, "elementImport", None)
                if opp_val == self:
                    setattr(old_value, "elementImport", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "elementImport"):
                opp_val = getattr(value, "elementImport", None)
                setattr(value, "elementImport", self)

    @property
    def importingNamespace11(self):
        return self.__importingNamespace11

    @importingNamespace11.setter
    def importingNamespace11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Namespace__importingNamespace11", None)
        self.__importingNamespace11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PackageImport"):
                    opp_val = getattr(item, "PackageImport", None)
                    
                    if opp_val == self:
                        setattr(item, "PackageImport", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PackageImport"):
                    opp_val = getattr(item, "PackageImport", None)
                    
                    setattr(item, "PackageImport", self)
                    

    @property
    def cmof_Namespace(self):
        return self.__cmof_Namespace

    @cmof_Namespace.setter
    def cmof_Namespace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Namespace__cmof_Namespace", None)
        self.__cmof_Namespace = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cmof_PackageableElement"):
                    opp_val = getattr(item, "cmof_PackageableElement", None)
                    
                    if opp_val == self:
                        setattr(item, "cmof_PackageableElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cmof_PackageableElement"):
                    opp_val = getattr(item, "cmof_PackageableElement", None)
                    
                    setattr(item, "cmof_PackageableElement", self)
                    

    @property
    def Namespace(self):
        return self.__Namespace

    @Namespace.setter
    def Namespace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Namespace__Namespace", None)
        self.__Namespace = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ownedRule"):
                opp_val = getattr(old_value, "ownedRule", None)
                if opp_val == self:
                    setattr(old_value, "ownedRule", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownedRule"):
                opp_val = getattr(value, "ownedRule", None)
                setattr(value, "ownedRule", self)

    @property
    def cmof_Namespace13(self):
        return self.__cmof_Namespace13

    @cmof_Namespace13.setter
    def cmof_Namespace13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Namespace__cmof_Namespace13", None)
        self.__cmof_Namespace13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cmof_NamedElement14"):
                    opp_val = getattr(item, "cmof_NamedElement14", None)
                    
                    if opp_val == self:
                        setattr(item, "cmof_NamedElement14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cmof_NamedElement14"):
                    opp_val = getattr(item, "cmof_NamedElement14", None)
                    
                    setattr(item, "cmof_NamedElement14", self)
                    

    @property
    def namespace(self):
        return self.__namespace

    @namespace.setter
    def namespace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Namespace__namespace", None)
        self.__namespace = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Constraint"):
                    opp_val = getattr(item, "Constraint", None)
                    
                    if opp_val == self:
                        setattr(item, "Constraint", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Constraint"):
                    opp_val = getattr(item, "Constraint", None)
                    
                    setattr(item, "Constraint", self)
                    

    @property
    def importingNamespace(self):
        return self.__importingNamespace

    @importingNamespace.setter
    def importingNamespace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Namespace__importingNamespace", None)
        self.__importingNamespace = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ElementImport"):
                    opp_val = getattr(item, "ElementImport", None)
                    
                    if opp_val == self:
                        setattr(item, "ElementImport", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ElementImport"):
                    opp_val = getattr(item, "ElementImport", None)
                    
                    setattr(item, "ElementImport", self)
                    

    def members_are_distinguishable(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement members_are_distinguishable method
        pass

    def getImportedMembers(self) -> str:
        # TODO: Implement getImportedMembers method
        pass

    def getNamesOfMember(self, element: NamedElement) -> str:
        # TODO: Implement getNamesOfMember method
        pass

    def membersAreDistinguishable(self) -> bool:
        # TODO: Implement membersAreDistinguishable method
        pass

    def importMembers(self, imps: str) -> str:
        # TODO: Implement importMembers method
        pass

    def excludeCollisions(self, imps: str) -> str:
        # TODO: Implement excludeCollisions method
        pass

class cmof_Property(StructuralFeature, MultiplicityElement):

    def __init__(self, isReadOnly: bool, isDerivedUnion: bool, default: str, isComposite: bool, isDerived: bool, isID: bool, cmof_Property: "cmof_Classifier" = None, Property: "cmof_Class" = None, ownedAttribute: "cmof_DataType" = None, ownedEnd: "cmof_Association" = None, memberEnd: "cmof_Association" = None, cmof_Property34: "cmof_Property" = None, cmof_Property32: set["cmof_Property"] = None, cmof_Property37: "cmof_Property" = None, cmof_Property35: set["cmof_Property"] = None, cmof_Property41: "cmof_Property" = None, cmof_Property39: "cmof_Property" = None, ownedAttribute43: "cmof_Class" = None, Property81: "cmof_Association" = None, Property76: "cmof_Association" = None, cmof_Property79: "cmof_Association" = None, Property86: "cmof_DataType" = None):
        self.isReadOnly = isReadOnly
        self.isDerivedUnion = isDerivedUnion
        self.default = default
        self.isComposite = isComposite
        self.isDerived = isDerived
        self.isID = isID
        self.cmof_Property = cmof_Property
        self.Property = Property
        self.ownedAttribute = ownedAttribute
        self.ownedEnd = ownedEnd
        self.memberEnd = memberEnd
        self.cmof_Property34 = cmof_Property34
        self.cmof_Property32 = cmof_Property32 if cmof_Property32 is not None else set()
        self.cmof_Property37 = cmof_Property37
        self.cmof_Property35 = cmof_Property35 if cmof_Property35 is not None else set()
        self.cmof_Property41 = cmof_Property41
        self.cmof_Property39 = cmof_Property39
        self.ownedAttribute43 = ownedAttribute43
        self.Property81 = Property81
        self.Property76 = Property76
        self.cmof_Property79 = cmof_Property79
        self.Property86 = Property86
        
    @property
    def isID(self) -> bool:
        return self.__isID

    @isID.setter
    def isID(self, isID: bool):
        self.__isID = isID

    @property
    def isDerivedUnion(self) -> bool:
        return self.__isDerivedUnion

    @isDerivedUnion.setter
    def isDerivedUnion(self, isDerivedUnion: bool):
        self.__isDerivedUnion = isDerivedUnion

    @property
    def isReadOnly(self) -> bool:
        return self.__isReadOnly

    @isReadOnly.setter
    def isReadOnly(self, isReadOnly: bool):
        self.__isReadOnly = isReadOnly

    @property
    def isComposite(self) -> bool:
        return self.__isComposite

    @isComposite.setter
    def isComposite(self, isComposite: bool):
        self.__isComposite = isComposite

    @property
    def default(self) -> str:
        return self.__default

    @default.setter
    def default(self, default: str):
        self.__default = default

    @property
    def isDerived(self) -> bool:
        return self.__isDerived

    @isDerived.setter
    def isDerived(self, isDerived: bool):
        self.__isDerived = isDerived

    @property
    def cmof_Property39(self):
        return self.__cmof_Property39

    @cmof_Property39.setter
    def cmof_Property39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Property__cmof_Property39", None)
        self.__cmof_Property39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_Property41"):
                opp_val = getattr(old_value, "cmof_Property41", None)
                if opp_val == self:
                    setattr(old_value, "cmof_Property41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_Property41"):
                opp_val = getattr(value, "cmof_Property41", None)
                setattr(value, "cmof_Property41", self)

    @property
    def cmof_Property79(self):
        return self.__cmof_Property79

    @cmof_Property79.setter
    def cmof_Property79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Property__cmof_Property79", None)
        self.__cmof_Property79 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_Association78"):
                opp_val = getattr(old_value, "cmof_Association78", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_Association78"):
                opp_val = getattr(value, "cmof_Association78", None)
                if opp_val is None:
                    setattr(value, "cmof_Association78", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Property86(self):
        return self.__Property86

    @Property86.setter
    def Property86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Property__Property86", None)
        self.__Property86 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "datatype85"):
                opp_val = getattr(old_value, "datatype85", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "datatype85"):
                opp_val = getattr(value, "datatype85", None)
                if opp_val is None:
                    setattr(value, "datatype85", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Property(self):
        return self.__Property

    @Property.setter
    def Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Property__Property", None)
        self.__Property = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "class"):
                opp_val = getattr(old_value, "class", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "class"):
                opp_val = getattr(value, "class", None)
                if opp_val is None:
                    setattr(value, "class", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ownedAttribute43(self):
        return self.__ownedAttribute43

    @ownedAttribute43.setter
    def ownedAttribute43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Property__ownedAttribute43", None)
        self.__ownedAttribute43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Class"):
                opp_val = getattr(old_value, "Class", None)
                if opp_val == self:
                    setattr(old_value, "Class", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Class"):
                opp_val = getattr(value, "Class", None)
                setattr(value, "Class", self)

    @property
    def cmof_Property35(self):
        return self.__cmof_Property35

    @cmof_Property35.setter
    def cmof_Property35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Property__cmof_Property35", None)
        self.__cmof_Property35 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cmof_Property37"):
                    opp_val = getattr(item, "cmof_Property37", None)
                    
                    if opp_val == self:
                        setattr(item, "cmof_Property37", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cmof_Property37"):
                    opp_val = getattr(item, "cmof_Property37", None)
                    
                    setattr(item, "cmof_Property37", self)
                    

    @property
    def cmof_Property34(self):
        return self.__cmof_Property34

    @cmof_Property34.setter
    def cmof_Property34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Property__cmof_Property34", None)
        self.__cmof_Property34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_Property32"):
                opp_val = getattr(old_value, "cmof_Property32", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_Property32"):
                opp_val = getattr(value, "cmof_Property32", None)
                if opp_val is None:
                    setattr(value, "cmof_Property32", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Property76(self):
        return self.__Property76

    @Property76.setter
    def Property76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Property__Property76", None)
        self.__Property76 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "association"):
                opp_val = getattr(old_value, "association", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "association"):
                opp_val = getattr(value, "association", None)
                if opp_val is None:
                    setattr(value, "association", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cmof_Property(self):
        return self.__cmof_Property

    @cmof_Property.setter
    def cmof_Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Property__cmof_Property", None)
        self.__cmof_Property = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_Classifier"):
                opp_val = getattr(old_value, "cmof_Classifier", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_Classifier"):
                opp_val = getattr(value, "cmof_Classifier", None)
                if opp_val is None:
                    setattr(value, "cmof_Classifier", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Property81(self):
        return self.__Property81

    @Property81.setter
    def Property81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Property__Property81", None)
        self.__Property81 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owningAssociation"):
                opp_val = getattr(old_value, "owningAssociation", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owningAssociation"):
                opp_val = getattr(value, "owningAssociation", None)
                if opp_val is None:
                    setattr(value, "owningAssociation", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cmof_Property37(self):
        return self.__cmof_Property37

    @cmof_Property37.setter
    def cmof_Property37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Property__cmof_Property37", None)
        self.__cmof_Property37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_Property35"):
                opp_val = getattr(old_value, "cmof_Property35", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_Property35"):
                opp_val = getattr(value, "cmof_Property35", None)
                if opp_val is None:
                    setattr(value, "cmof_Property35", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cmof_Property32(self):
        return self.__cmof_Property32

    @cmof_Property32.setter
    def cmof_Property32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Property__cmof_Property32", None)
        self.__cmof_Property32 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cmof_Property34"):
                    opp_val = getattr(item, "cmof_Property34", None)
                    
                    if opp_val == self:
                        setattr(item, "cmof_Property34", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cmof_Property34"):
                    opp_val = getattr(item, "cmof_Property34", None)
                    
                    setattr(item, "cmof_Property34", self)
                    

    @property
    def memberEnd(self):
        return self.__memberEnd

    @memberEnd.setter
    def memberEnd(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Property__memberEnd", None)
        self.__memberEnd = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Association31"):
                opp_val = getattr(old_value, "Association31", None)
                if opp_val == self:
                    setattr(old_value, "Association31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Association31"):
                opp_val = getattr(value, "Association31", None)
                setattr(value, "Association31", self)

    @property
    def cmof_Property41(self):
        return self.__cmof_Property41

    @cmof_Property41.setter
    def cmof_Property41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Property__cmof_Property41", None)
        self.__cmof_Property41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_Property39"):
                opp_val = getattr(old_value, "cmof_Property39", None)
                if opp_val == self:
                    setattr(old_value, "cmof_Property39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_Property39"):
                opp_val = getattr(value, "cmof_Property39", None)
                setattr(value, "cmof_Property39", self)

    @property
    def ownedAttribute(self):
        return self.__ownedAttribute

    @ownedAttribute.setter
    def ownedAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Property__ownedAttribute", None)
        self.__ownedAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DataType"):
                opp_val = getattr(old_value, "DataType", None)
                if opp_val == self:
                    setattr(old_value, "DataType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DataType"):
                opp_val = getattr(value, "DataType", None)
                setattr(value, "DataType", self)

    @property
    def ownedEnd(self):
        return self.__ownedEnd

    @ownedEnd.setter
    def ownedEnd(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Property__ownedEnd", None)
        self.__ownedEnd = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Association"):
                opp_val = getattr(old_value, "Association", None)
                if opp_val == self:
                    setattr(old_value, "Association", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Association"):
                opp_val = getattr(value, "Association", None)
                setattr(value, "Association", self)

    def navigable_property_redefinition(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement navigable_property_redefinition method
        pass

    def multiplicity_of_composite(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement multiplicity_of_composite method
        pass

    def subsettingContext(self) -> Classifier:
        # TODO: Implement subsettingContext method
        pass

    def subsetting_context(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement subsetting_context method
        pass

    def getOpposite(self) -> str:
        # TODO: Implement getOpposite method
        pass

    def isNavigable(self) -> bool:
        # TODO: Implement isNavigable method
        pass

    def navigable_readonly(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement navigable_readonly method
        pass

    def derived_union_is_derived(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement derived_union_is_derived method
        pass

    def subsetting_rules(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement subsetting_rules method
        pass

class cmof_Feature(RedefinableElement):

    pass
class cmof_NamedElement(Element):

    def __init__(self, visibility: str, name: str, cmof_NamedElement: "cmof_Classifier" = None, cmof_NamedElement14: "cmof_Namespace" = None):
        self.visibility = visibility
        self.name = name
        self.cmof_NamedElement = cmof_NamedElement
        self.cmof_NamedElement14 = cmof_NamedElement14
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

    @property
    def cmof_NamedElement14(self):
        return self.__cmof_NamedElement14

    @cmof_NamedElement14.setter
    def cmof_NamedElement14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_NamedElement__cmof_NamedElement14", None)
        self.__cmof_NamedElement14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_Namespace13"):
                opp_val = getattr(old_value, "cmof_Namespace13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_Namespace13"):
                opp_val = getattr(value, "cmof_Namespace13", None)
                if opp_val is None:
                    setattr(value, "cmof_Namespace13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cmof_NamedElement(self):
        return self.__cmof_NamedElement

    @cmof_NamedElement.setter
    def cmof_NamedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_NamedElement__cmof_NamedElement", None)
        self.__cmof_NamedElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_Classifier6"):
                opp_val = getattr(old_value, "cmof_Classifier6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_Classifier6"):
                opp_val = getattr(value, "cmof_Classifier6", None)
                if opp_val is None:
                    setattr(value, "cmof_Classifier6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def separator(self) -> str:
        # TODO: Implement separator method
        pass

    def visibility_needs_ownership(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement visibility_needs_ownership method
        pass

    def allNamespaces(self) -> Namespace:
        # TODO: Implement allNamespaces method
        pass

    def qualified_name(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement qualified_name method
        pass

    def qualifiedName(self) -> str:
        # TODO: Implement qualifiedName method
        pass

    def no_name(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement no_name method
        pass

    def isDistinguishableFrom(self, n: NamedElement, ns: Namespace) -> bool:
        # TODO: Implement isDistinguishableFrom method
        pass

class Type:

    pass
class Namespace:

    pass
class cmof_Package(Namespace, PackageableElement):

    def __init__(self, uRI: str, Package: "cmof_Type" = None, cmof_Package: set["cmof_PackageableElement"] = None, package: set["cmof_Type"] = None, receivingPackage: set["cmof_PackageMerge"] = None, Package57: "cmof_Package" = None, nestingPackage: set["cmof_Package"] = None, Package60: "cmof_Package" = None, nestedPackage: "cmof_Package" = None, cmof_Package63: "cmof_PackageMerge" = None, Package65: "cmof_PackageMerge" = None, cmof_Package123: "cmof_PackageImport" = None, cmof_Package136: "cmof_Factory" = None):
        self.uRI = uRI
        self.Package = Package
        self.cmof_Package = cmof_Package if cmof_Package is not None else set()
        self.package = package if package is not None else set()
        self.receivingPackage = receivingPackage if receivingPackage is not None else set()
        self.Package57 = Package57
        self.nestingPackage = nestingPackage if nestingPackage is not None else set()
        self.Package60 = Package60
        self.nestedPackage = nestedPackage
        self.cmof_Package63 = cmof_Package63
        self.Package65 = Package65
        self.cmof_Package123 = cmof_Package123
        self.cmof_Package136 = cmof_Package136
        
    @property
    def uRI(self) -> str:
        return self.__uRI

    @uRI.setter
    def uRI(self, uRI: str):
        self.__uRI = uRI

    @property
    def Package(self):
        return self.__Package

    @Package.setter
    def Package(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Package__Package", None)
        self.__Package = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ownedType"):
                opp_val = getattr(old_value, "ownedType", None)
                if opp_val == self:
                    setattr(old_value, "ownedType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownedType"):
                opp_val = getattr(value, "ownedType", None)
                setattr(value, "ownedType", self)

    @property
    def Package60(self):
        return self.__Package60

    @Package60.setter
    def Package60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Package__Package60", None)
        self.__Package60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nestedPackage"):
                opp_val = getattr(old_value, "nestedPackage", None)
                if opp_val == self:
                    setattr(old_value, "nestedPackage", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nestedPackage"):
                opp_val = getattr(value, "nestedPackage", None)
                setattr(value, "nestedPackage", self)

    @property
    def nestingPackage(self):
        return self.__nestingPackage

    @nestingPackage.setter
    def nestingPackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Package__nestingPackage", None)
        self.__nestingPackage = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Package57"):
                    opp_val = getattr(item, "Package57", None)
                    
                    if opp_val == self:
                        setattr(item, "Package57", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Package57"):
                    opp_val = getattr(item, "Package57", None)
                    
                    setattr(item, "Package57", self)
                    

    @property
    def receivingPackage(self):
        return self.__receivingPackage

    @receivingPackage.setter
    def receivingPackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Package__receivingPackage", None)
        self.__receivingPackage = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PackageMerge"):
                    opp_val = getattr(item, "PackageMerge", None)
                    
                    if opp_val == self:
                        setattr(item, "PackageMerge", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PackageMerge"):
                    opp_val = getattr(item, "PackageMerge", None)
                    
                    setattr(item, "PackageMerge", self)
                    

    @property
    def cmof_Package63(self):
        return self.__cmof_Package63

    @cmof_Package63.setter
    def cmof_Package63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Package__cmof_Package63", None)
        self.__cmof_Package63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_PackageMerge"):
                opp_val = getattr(old_value, "cmof_PackageMerge", None)
                if opp_val == self:
                    setattr(old_value, "cmof_PackageMerge", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_PackageMerge"):
                opp_val = getattr(value, "cmof_PackageMerge", None)
                setattr(value, "cmof_PackageMerge", self)

    @property
    def cmof_Package(self):
        return self.__cmof_Package

    @cmof_Package.setter
    def cmof_Package(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Package__cmof_Package", None)
        self.__cmof_Package = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cmof_PackageableElement53"):
                    opp_val = getattr(item, "cmof_PackageableElement53", None)
                    
                    if opp_val == self:
                        setattr(item, "cmof_PackageableElement53", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cmof_PackageableElement53"):
                    opp_val = getattr(item, "cmof_PackageableElement53", None)
                    
                    setattr(item, "cmof_PackageableElement53", self)
                    

    @property
    def package(self):
        return self.__package

    @package.setter
    def package(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Package__package", None)
        self.__package = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Type"):
                    opp_val = getattr(item, "Type", None)
                    
                    if opp_val == self:
                        setattr(item, "Type", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Type"):
                    opp_val = getattr(item, "Type", None)
                    
                    setattr(item, "Type", self)
                    

    @property
    def Package57(self):
        return self.__Package57

    @Package57.setter
    def Package57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Package__Package57", None)
        self.__Package57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nestingPackage"):
                opp_val = getattr(old_value, "nestingPackage", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nestingPackage"):
                opp_val = getattr(value, "nestingPackage", None)
                if opp_val is None:
                    setattr(value, "nestingPackage", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cmof_Package136(self):
        return self.__cmof_Package136

    @cmof_Package136.setter
    def cmof_Package136(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Package__cmof_Package136", None)
        self.__cmof_Package136 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_Factory"):
                opp_val = getattr(old_value, "cmof_Factory", None)
                if opp_val == self:
                    setattr(old_value, "cmof_Factory", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_Factory"):
                opp_val = getattr(value, "cmof_Factory", None)
                setattr(value, "cmof_Factory", self)

    @property
    def Package65(self):
        return self.__Package65

    @Package65.setter
    def Package65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Package__Package65", None)
        self.__Package65 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "packageMerge"):
                opp_val = getattr(old_value, "packageMerge", None)
                if opp_val == self:
                    setattr(old_value, "packageMerge", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "packageMerge"):
                opp_val = getattr(value, "packageMerge", None)
                setattr(value, "packageMerge", self)

    @property
    def nestedPackage(self):
        return self.__nestedPackage

    @nestedPackage.setter
    def nestedPackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Package__nestedPackage", None)
        self.__nestedPackage = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Package60"):
                opp_val = getattr(old_value, "Package60", None)
                if opp_val == self:
                    setattr(old_value, "Package60", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Package60"):
                opp_val = getattr(value, "Package60", None)
                setattr(value, "Package60", self)

    @property
    def cmof_Package123(self):
        return self.__cmof_Package123

    @cmof_Package123.setter
    def cmof_Package123(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Package__cmof_Package123", None)
        self.__cmof_Package123 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_PackageImport"):
                opp_val = getattr(old_value, "cmof_PackageImport", None)
                if opp_val == self:
                    setattr(old_value, "cmof_PackageImport", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_PackageImport"):
                opp_val = getattr(value, "cmof_PackageImport", None)
                setattr(value, "cmof_PackageImport", self)

    def makesVisible(self, el: NamedElement) -> bool:
        # TODO: Implement makesVisible method
        pass

    def elements_public_or_private(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement elements_public_or_private method
        pass

    def visibleMembers(self) -> PackageableElement:
        # TODO: Implement visibleMembers method
        pass

class cmof_BehavioralFeature(Feature, Namespace):

    pass
class cmof_Classifier(Namespace, Type):

    def __init__(self, cmof_Classifier4: "cmof_Classifier" = None, cmof_Classifier2: set["cmof_Classifier"] = None, cmof_Classifier6: set["cmof_NamedElement"] = None, featuringClassifier: set["cmof_Feature"] = None, cmof_Classifier: set["cmof_Property"] = None, Classifier: "cmof_Feature" = None, cmof_Classifier46: "cmof_RedefinableElement" = None):
        self.cmof_Classifier4 = cmof_Classifier4
        self.cmof_Classifier2 = cmof_Classifier2 if cmof_Classifier2 is not None else set()
        self.cmof_Classifier6 = cmof_Classifier6 if cmof_Classifier6 is not None else set()
        self.featuringClassifier = featuringClassifier if featuringClassifier is not None else set()
        self.cmof_Classifier = cmof_Classifier if cmof_Classifier is not None else set()
        self.Classifier = Classifier
        self.cmof_Classifier46 = cmof_Classifier46
        
    @property
    def cmof_Classifier46(self):
        return self.__cmof_Classifier46

    @cmof_Classifier46.setter
    def cmof_Classifier46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Classifier__cmof_Classifier46", None)
        self.__cmof_Classifier46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_RedefinableElement"):
                opp_val = getattr(old_value, "cmof_RedefinableElement", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_RedefinableElement"):
                opp_val = getattr(value, "cmof_RedefinableElement", None)
                if opp_val is None:
                    setattr(value, "cmof_RedefinableElement", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def featuringClassifier(self):
        return self.__featuringClassifier

    @featuringClassifier.setter
    def featuringClassifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Classifier__featuringClassifier", None)
        self.__featuringClassifier = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Feature"):
                    opp_val = getattr(item, "Feature", None)
                    
                    if opp_val == self:
                        setattr(item, "Feature", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Feature"):
                    opp_val = getattr(item, "Feature", None)
                    
                    setattr(item, "Feature", self)
                    

    @property
    def cmof_Classifier4(self):
        return self.__cmof_Classifier4

    @cmof_Classifier4.setter
    def cmof_Classifier4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Classifier__cmof_Classifier4", None)
        self.__cmof_Classifier4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_Classifier2"):
                opp_val = getattr(old_value, "cmof_Classifier2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_Classifier2"):
                opp_val = getattr(value, "cmof_Classifier2", None)
                if opp_val is None:
                    setattr(value, "cmof_Classifier2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cmof_Classifier(self):
        return self.__cmof_Classifier

    @cmof_Classifier.setter
    def cmof_Classifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Classifier__cmof_Classifier", None)
        self.__cmof_Classifier = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cmof_Property"):
                    opp_val = getattr(item, "cmof_Property", None)
                    
                    if opp_val == self:
                        setattr(item, "cmof_Property", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cmof_Property"):
                    opp_val = getattr(item, "cmof_Property", None)
                    
                    setattr(item, "cmof_Property", self)
                    

    @property
    def Classifier(self):
        return self.__Classifier

    @Classifier.setter
    def Classifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Classifier__Classifier", None)
        self.__Classifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "feature"):
                opp_val = getattr(old_value, "feature", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "feature"):
                opp_val = getattr(value, "feature", None)
                if opp_val is None:
                    setattr(value, "feature", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cmof_Classifier6(self):
        return self.__cmof_Classifier6

    @cmof_Classifier6.setter
    def cmof_Classifier6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Classifier__cmof_Classifier6", None)
        self.__cmof_Classifier6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cmof_NamedElement"):
                    opp_val = getattr(item, "cmof_NamedElement", None)
                    
                    if opp_val == self:
                        setattr(item, "cmof_NamedElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cmof_NamedElement"):
                    opp_val = getattr(item, "cmof_NamedElement", None)
                    
                    setattr(item, "cmof_NamedElement", self)
                    

    @property
    def cmof_Classifier2(self):
        return self.__cmof_Classifier2

    @cmof_Classifier2.setter
    def cmof_Classifier2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Classifier__cmof_Classifier2", None)
        self.__cmof_Classifier2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cmof_Classifier4"):
                    opp_val = getattr(item, "cmof_Classifier4", None)
                    
                    if opp_val == self:
                        setattr(item, "cmof_Classifier4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cmof_Classifier4"):
                    opp_val = getattr(item, "cmof_Classifier4", None)
                    
                    setattr(item, "cmof_Classifier4", self)
                    

    def allFeatures(self) -> str:
        # TODO: Implement allFeatures method
        pass

    def inherit(self, inhs: str) -> str:
        # TODO: Implement inherit method
        pass

    def getInheritedMembers(self) -> str:
        # TODO: Implement getInheritedMembers method
        pass

    def getGenerals(self) -> str:
        # TODO: Implement getGenerals method
        pass

    def conformsTo(self, other: str) -> bool:
        # TODO: Implement conformsTo method
        pass

    def no_cycles_in_generalization(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement no_cycles_in_generalization method
        pass

    def parents(self) -> str:
        # TODO: Implement parents method
        pass

    def allParents(self) -> str:
        # TODO: Implement allParents method
        pass

    def inheritableMembers(self, c: str) -> str:
        # TODO: Implement inheritableMembers method
        pass

    def maySpecializeType(self, c: str) -> bool:
        # TODO: Implement maySpecializeType method
        pass

    def hasVisibilityOf(self, n: str) -> bool:
        # TODO: Implement hasVisibilityOf method
        pass

    def specialize_type(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement specialize_type method
        pass
