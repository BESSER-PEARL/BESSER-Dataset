from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class uml2CD_UMLModel:

    pass
class uml2CD_Parameter:

    def __init__(self, kind: str, defaultValue: str, uml2CD_Parameter: "uml2CD_DataType" = None):
        self.kind = kind
        self.defaultValue = defaultValue
        self.uml2CD_Parameter = uml2CD_Parameter
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def defaultValue(self) -> str:
        return self.__defaultValue

    @defaultValue.setter
    def defaultValue(self, defaultValue: str):
        self.__defaultValue = defaultValue

    @property
    def uml2CD_Parameter(self):
        return self.__uml2CD_Parameter

    @uml2CD_Parameter.setter
    def uml2CD_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2CD_Parameter__uml2CD_Parameter", None)
        self.__uml2CD_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml2CD_DataType21"):
                opp_val = getattr(old_value, "uml2CD_DataType21", None)
                if opp_val == self:
                    setattr(old_value, "uml2CD_DataType21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml2CD_DataType21"):
                opp_val = getattr(value, "uml2CD_DataType21", None)
                setattr(value, "uml2CD_DataType21", self)

class uml2CD_GeneralizationSet:

    def __init__(self, isCovering: str, isDisjoint: str, GeneralizationSet: "uml2CD_Generalization" = None, generalizationSet: set["uml2CD_Generalization"] = None):
        self.isCovering = isCovering
        self.isDisjoint = isDisjoint
        self.GeneralizationSet = GeneralizationSet
        self.generalizationSet = generalizationSet if generalizationSet is not None else set()
        
    @property
    def isCovering(self) -> str:
        return self.__isCovering

    @isCovering.setter
    def isCovering(self, isCovering: str):
        self.__isCovering = isCovering

    @property
    def isDisjoint(self) -> str:
        return self.__isDisjoint

    @isDisjoint.setter
    def isDisjoint(self, isDisjoint: str):
        self.__isDisjoint = isDisjoint

    @property
    def generalizationSet(self):
        return self.__generalizationSet

    @generalizationSet.setter
    def generalizationSet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2CD_GeneralizationSet__generalizationSet", None)
        self.__generalizationSet = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Generalization"):
                    opp_val = getattr(item, "Generalization", None)
                    
                    if opp_val == self:
                        setattr(item, "Generalization", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Generalization"):
                    opp_val = getattr(item, "Generalization", None)
                    
                    setattr(item, "Generalization", self)
                    

    @property
    def GeneralizationSet(self):
        return self.__GeneralizationSet

    @GeneralizationSet.setter
    def GeneralizationSet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2CD_GeneralizationSet__GeneralizationSet", None)
        self.__GeneralizationSet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "generalization"):
                opp_val = getattr(old_value, "generalization", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "generalization"):
                opp_val = getattr(value, "generalization", None)
                if opp_val is None:
                    setattr(value, "generalization", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class DataType:

    pass
class uml2CD_Enumeration(DataType):

    pass
class uml2CD_PrimitiveType(DataType):

    pass
class NamedElement:

    pass
class uml2CD_Operation(NamedElement):

    def __init__(self, isQuery: str, visibility: str, body: str, uml2CD_Operation: "uml2CD_Operation" = None, uml2CD_Operation22: set["uml2CD_Operation"] = None, uml2CD_Operation26: "uml2CD_Class" = None):
        self.isQuery = isQuery
        self.visibility = visibility
        self.body = body
        self.uml2CD_Operation = uml2CD_Operation
        self.uml2CD_Operation22 = uml2CD_Operation22 if uml2CD_Operation22 is not None else set()
        self.uml2CD_Operation26 = uml2CD_Operation26
        
    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

    @property
    def body(self) -> str:
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body

    @property
    def isQuery(self) -> str:
        return self.__isQuery

    @isQuery.setter
    def isQuery(self, isQuery: str):
        self.__isQuery = isQuery

    @property
    def uml2CD_Operation(self):
        return self.__uml2CD_Operation

    @uml2CD_Operation.setter
    def uml2CD_Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2CD_Operation__uml2CD_Operation", None)
        self.__uml2CD_Operation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml2CD_Operation22"):
                opp_val = getattr(old_value, "uml2CD_Operation22", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml2CD_Operation22"):
                opp_val = getattr(value, "uml2CD_Operation22", None)
                if opp_val is None:
                    setattr(value, "uml2CD_Operation22", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml2CD_Operation22(self):
        return self.__uml2CD_Operation22

    @uml2CD_Operation22.setter
    def uml2CD_Operation22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2CD_Operation__uml2CD_Operation22", None)
        self.__uml2CD_Operation22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml2CD_Operation"):
                    opp_val = getattr(item, "uml2CD_Operation", None)
                    
                    if opp_val == self:
                        setattr(item, "uml2CD_Operation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml2CD_Operation"):
                    opp_val = getattr(item, "uml2CD_Operation", None)
                    
                    setattr(item, "uml2CD_Operation", self)
                    

    @property
    def uml2CD_Operation26(self):
        return self.__uml2CD_Operation26

    @uml2CD_Operation26.setter
    def uml2CD_Operation26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2CD_Operation__uml2CD_Operation26", None)
        self.__uml2CD_Operation26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml2CD_Class25"):
                opp_val = getattr(old_value, "uml2CD_Class25", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml2CD_Class25"):
                opp_val = getattr(value, "uml2CD_Class25", None)
                if opp_val is None:
                    setattr(value, "uml2CD_Class25", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class uml2CD_Class(NamedElement):

    def __init__(self, active: str, uml2CD_Class15: "uml2CD_Generalization" = None, uml2CD_Class: "uml2CD_Package" = None, uml2CD_Class18: "uml2CD_Generalization" = None, uml2CD_Class25: set["uml2CD_Operation"] = None, uml2CD_Class28: set["uml2CD_Property"] = None):
        self.active = active
        self.uml2CD_Class15 = uml2CD_Class15
        self.uml2CD_Class = uml2CD_Class
        self.uml2CD_Class18 = uml2CD_Class18
        self.uml2CD_Class25 = uml2CD_Class25 if uml2CD_Class25 is not None else set()
        self.uml2CD_Class28 = uml2CD_Class28 if uml2CD_Class28 is not None else set()
        
    @property
    def active(self) -> str:
        return self.__active

    @active.setter
    def active(self, active: str):
        self.__active = active

    @property
    def uml2CD_Class(self):
        return self.__uml2CD_Class

    @uml2CD_Class.setter
    def uml2CD_Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2CD_Class__uml2CD_Class", None)
        self.__uml2CD_Class = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml2CD_Package6"):
                opp_val = getattr(old_value, "uml2CD_Package6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml2CD_Package6"):
                opp_val = getattr(value, "uml2CD_Package6", None)
                if opp_val is None:
                    setattr(value, "uml2CD_Package6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml2CD_Class28(self):
        return self.__uml2CD_Class28

    @uml2CD_Class28.setter
    def uml2CD_Class28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2CD_Class__uml2CD_Class28", None)
        self.__uml2CD_Class28 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml2CD_Property"):
                    opp_val = getattr(item, "uml2CD_Property", None)
                    
                    if opp_val == self:
                        setattr(item, "uml2CD_Property", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml2CD_Property"):
                    opp_val = getattr(item, "uml2CD_Property", None)
                    
                    setattr(item, "uml2CD_Property", self)
                    

    @property
    def uml2CD_Class18(self):
        return self.__uml2CD_Class18

    @uml2CD_Class18.setter
    def uml2CD_Class18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2CD_Class__uml2CD_Class18", None)
        self.__uml2CD_Class18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml2CD_Generalization17"):
                opp_val = getattr(old_value, "uml2CD_Generalization17", None)
                if opp_val == self:
                    setattr(old_value, "uml2CD_Generalization17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml2CD_Generalization17"):
                opp_val = getattr(value, "uml2CD_Generalization17", None)
                setattr(value, "uml2CD_Generalization17", self)

    @property
    def uml2CD_Class15(self):
        return self.__uml2CD_Class15

    @uml2CD_Class15.setter
    def uml2CD_Class15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2CD_Class__uml2CD_Class15", None)
        self.__uml2CD_Class15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml2CD_Generalization14"):
                opp_val = getattr(old_value, "uml2CD_Generalization14", None)
                if opp_val == self:
                    setattr(old_value, "uml2CD_Generalization14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml2CD_Generalization14"):
                opp_val = getattr(value, "uml2CD_Generalization14", None)
                setattr(value, "uml2CD_Generalization14", self)

    @property
    def uml2CD_Class25(self):
        return self.__uml2CD_Class25

    @uml2CD_Class25.setter
    def uml2CD_Class25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2CD_Class__uml2CD_Class25", None)
        self.__uml2CD_Class25 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml2CD_Operation26"):
                    opp_val = getattr(item, "uml2CD_Operation26", None)
                    
                    if opp_val == self:
                        setattr(item, "uml2CD_Operation26", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml2CD_Operation26"):
                    opp_val = getattr(item, "uml2CD_Operation26", None)
                    
                    setattr(item, "uml2CD_Operation26", self)
                    

class uml2CD_Property(NamedElement):

    def __init__(self, aggregation: str, lower: str, upper: str, isDerived: str, uml2CD_Property31: "uml2CD_Association" = None, uml2CD_Property34: "uml2CD_Association" = None, uml2CD_Property: "uml2CD_Class" = None):
        self.aggregation = aggregation
        self.lower = lower
        self.upper = upper
        self.isDerived = isDerived
        self.uml2CD_Property31 = uml2CD_Property31
        self.uml2CD_Property34 = uml2CD_Property34
        self.uml2CD_Property = uml2CD_Property
        
    @property
    def isDerived(self) -> str:
        return self.__isDerived

    @isDerived.setter
    def isDerived(self, isDerived: str):
        self.__isDerived = isDerived

    @property
    def aggregation(self) -> str:
        return self.__aggregation

    @aggregation.setter
    def aggregation(self, aggregation: str):
        self.__aggregation = aggregation

    @property
    def lower(self) -> str:
        return self.__lower

    @lower.setter
    def lower(self, lower: str):
        self.__lower = lower

    @property
    def upper(self) -> str:
        return self.__upper

    @upper.setter
    def upper(self, upper: str):
        self.__upper = upper

    @property
    def uml2CD_Property(self):
        return self.__uml2CD_Property

    @uml2CD_Property.setter
    def uml2CD_Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2CD_Property__uml2CD_Property", None)
        self.__uml2CD_Property = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml2CD_Class28"):
                opp_val = getattr(old_value, "uml2CD_Class28", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml2CD_Class28"):
                opp_val = getattr(value, "uml2CD_Class28", None)
                if opp_val is None:
                    setattr(value, "uml2CD_Class28", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml2CD_Property31(self):
        return self.__uml2CD_Property31

    @uml2CD_Property31.setter
    def uml2CD_Property31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2CD_Property__uml2CD_Property31", None)
        self.__uml2CD_Property31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml2CD_Association30"):
                opp_val = getattr(old_value, "uml2CD_Association30", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml2CD_Association30"):
                opp_val = getattr(value, "uml2CD_Association30", None)
                if opp_val is None:
                    setattr(value, "uml2CD_Association30", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml2CD_Property34(self):
        return self.__uml2CD_Property34

    @uml2CD_Property34.setter
    def uml2CD_Property34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2CD_Property__uml2CD_Property34", None)
        self.__uml2CD_Property34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml2CD_Association33"):
                opp_val = getattr(old_value, "uml2CD_Association33", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml2CD_Association33"):
                opp_val = getattr(value, "uml2CD_Association33", None)
                if opp_val is None:
                    setattr(value, "uml2CD_Association33", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class uml2CD_EnumerationLiteral(NamedElement):

    pass
class uml2CD_Package(NamedElement):

    pass
class uml2CD_Constraint:

    def __init__(self, specification: str, uml2CD_Constraint: "uml2CD_NamedElement" = None):
        self.specification = specification
        self.uml2CD_Constraint = uml2CD_Constraint
        
    @property
    def specification(self) -> str:
        return self.__specification

    @specification.setter
    def specification(self, specification: str):
        self.__specification = specification

    @property
    def uml2CD_Constraint(self):
        return self.__uml2CD_Constraint

    @uml2CD_Constraint.setter
    def uml2CD_Constraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2CD_Constraint__uml2CD_Constraint", None)
        self.__uml2CD_Constraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml2CD_NamedElement2"):
                opp_val = getattr(old_value, "uml2CD_NamedElement2", None)
                if opp_val == self:
                    setattr(old_value, "uml2CD_NamedElement2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml2CD_NamedElement2"):
                opp_val = getattr(value, "uml2CD_NamedElement2", None)
                setattr(value, "uml2CD_NamedElement2", self)

class uml2CD_NamedElement(ABC):

    def __init__(self, name: str, uml2CD_NamedElement: "uml2CD_Comment" = None, uml2CD_NamedElement2: "uml2CD_Constraint" = None):
        self.name = name
        self.uml2CD_NamedElement = uml2CD_NamedElement
        self.uml2CD_NamedElement2 = uml2CD_NamedElement2
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def uml2CD_NamedElement(self):
        return self.__uml2CD_NamedElement

    @uml2CD_NamedElement.setter
    def uml2CD_NamedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2CD_NamedElement__uml2CD_NamedElement", None)
        self.__uml2CD_NamedElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml2CD_Comment"):
                opp_val = getattr(old_value, "uml2CD_Comment", None)
                if opp_val == self:
                    setattr(old_value, "uml2CD_Comment", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml2CD_Comment"):
                opp_val = getattr(value, "uml2CD_Comment", None)
                setattr(value, "uml2CD_Comment", self)

    @property
    def uml2CD_NamedElement2(self):
        return self.__uml2CD_NamedElement2

    @uml2CD_NamedElement2.setter
    def uml2CD_NamedElement2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2CD_NamedElement__uml2CD_NamedElement2", None)
        self.__uml2CD_NamedElement2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml2CD_Constraint"):
                opp_val = getattr(old_value, "uml2CD_Constraint", None)
                if opp_val == self:
                    setattr(old_value, "uml2CD_Constraint", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml2CD_Constraint"):
                opp_val = getattr(value, "uml2CD_Constraint", None)
                setattr(value, "uml2CD_Constraint", self)

class uml2CD_Comment:

    def __init__(self, value: str, uml2CD_Comment: "uml2CD_NamedElement" = None):
        self.value = value
        self.uml2CD_Comment = uml2CD_Comment
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def uml2CD_Comment(self):
        return self.__uml2CD_Comment

    @uml2CD_Comment.setter
    def uml2CD_Comment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2CD_Comment__uml2CD_Comment", None)
        self.__uml2CD_Comment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml2CD_NamedElement"):
                opp_val = getattr(old_value, "uml2CD_NamedElement", None)
                if opp_val == self:
                    setattr(old_value, "uml2CD_NamedElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml2CD_NamedElement"):
                opp_val = getattr(value, "uml2CD_NamedElement", None)
                setattr(value, "uml2CD_NamedElement", self)

class uml2CD_Generalization:

    def __init__(self, isSubstitutable: bool, uml2CD_Generalization: "uml2CD_Package" = None, uml2CD_Generalization14: "uml2CD_Class" = None, uml2CD_Generalization17: "uml2CD_Class" = None, generalization: set["uml2CD_GeneralizationSet"] = None, Generalization: "uml2CD_GeneralizationSet" = None):
        self.isSubstitutable = isSubstitutable
        self.uml2CD_Generalization = uml2CD_Generalization
        self.uml2CD_Generalization14 = uml2CD_Generalization14
        self.uml2CD_Generalization17 = uml2CD_Generalization17
        self.generalization = generalization if generalization is not None else set()
        self.Generalization = Generalization
        
    @property
    def isSubstitutable(self) -> bool:
        return self.__isSubstitutable

    @isSubstitutable.setter
    def isSubstitutable(self, isSubstitutable: bool):
        self.__isSubstitutable = isSubstitutable

    @property
    def uml2CD_Generalization14(self):
        return self.__uml2CD_Generalization14

    @uml2CD_Generalization14.setter
    def uml2CD_Generalization14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2CD_Generalization__uml2CD_Generalization14", None)
        self.__uml2CD_Generalization14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml2CD_Class15"):
                opp_val = getattr(old_value, "uml2CD_Class15", None)
                if opp_val == self:
                    setattr(old_value, "uml2CD_Class15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml2CD_Class15"):
                opp_val = getattr(value, "uml2CD_Class15", None)
                setattr(value, "uml2CD_Class15", self)

    @property
    def Generalization(self):
        return self.__Generalization

    @Generalization.setter
    def Generalization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2CD_Generalization__Generalization", None)
        self.__Generalization = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "generalizationSet"):
                opp_val = getattr(old_value, "generalizationSet", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "generalizationSet"):
                opp_val = getattr(value, "generalizationSet", None)
                if opp_val is None:
                    setattr(value, "generalizationSet", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def generalization(self):
        return self.__generalization

    @generalization.setter
    def generalization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2CD_Generalization__generalization", None)
        self.__generalization = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GeneralizationSet"):
                    opp_val = getattr(item, "GeneralizationSet", None)
                    
                    if opp_val == self:
                        setattr(item, "GeneralizationSet", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GeneralizationSet"):
                    opp_val = getattr(item, "GeneralizationSet", None)
                    
                    setattr(item, "GeneralizationSet", self)
                    

    @property
    def uml2CD_Generalization(self):
        return self.__uml2CD_Generalization

    @uml2CD_Generalization.setter
    def uml2CD_Generalization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2CD_Generalization__uml2CD_Generalization", None)
        self.__uml2CD_Generalization = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml2CD_Package12"):
                opp_val = getattr(old_value, "uml2CD_Package12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml2CD_Package12"):
                opp_val = getattr(value, "uml2CD_Package12", None)
                if opp_val is None:
                    setattr(value, "uml2CD_Package12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml2CD_Generalization17(self):
        return self.__uml2CD_Generalization17

    @uml2CD_Generalization17.setter
    def uml2CD_Generalization17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2CD_Generalization__uml2CD_Generalization17", None)
        self.__uml2CD_Generalization17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml2CD_Class18"):
                opp_val = getattr(old_value, "uml2CD_Class18", None)
                if opp_val == self:
                    setattr(old_value, "uml2CD_Class18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml2CD_Class18"):
                opp_val = getattr(value, "uml2CD_Class18", None)
                setattr(value, "uml2CD_Class18", self)

class uml2CD_Association(NamedElement):

    def __init__(self, isDerived: str, uml2CD_Association: "uml2CD_Package" = None, uml2CD_Association30: set["uml2CD_Property"] = None, uml2CD_Association33: set["uml2CD_Property"] = None):
        self.isDerived = isDerived
        self.uml2CD_Association = uml2CD_Association
        self.uml2CD_Association30 = uml2CD_Association30 if uml2CD_Association30 is not None else set()
        self.uml2CD_Association33 = uml2CD_Association33 if uml2CD_Association33 is not None else set()
        
    @property
    def isDerived(self) -> str:
        return self.__isDerived

    @isDerived.setter
    def isDerived(self, isDerived: str):
        self.__isDerived = isDerived

    @property
    def uml2CD_Association33(self):
        return self.__uml2CD_Association33

    @uml2CD_Association33.setter
    def uml2CD_Association33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2CD_Association__uml2CD_Association33", None)
        self.__uml2CD_Association33 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml2CD_Property34"):
                    opp_val = getattr(item, "uml2CD_Property34", None)
                    
                    if opp_val == self:
                        setattr(item, "uml2CD_Property34", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml2CD_Property34"):
                    opp_val = getattr(item, "uml2CD_Property34", None)
                    
                    setattr(item, "uml2CD_Property34", self)
                    

    @property
    def uml2CD_Association(self):
        return self.__uml2CD_Association

    @uml2CD_Association.setter
    def uml2CD_Association(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2CD_Association__uml2CD_Association", None)
        self.__uml2CD_Association = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml2CD_Package10"):
                opp_val = getattr(old_value, "uml2CD_Package10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml2CD_Package10"):
                opp_val = getattr(value, "uml2CD_Package10", None)
                if opp_val is None:
                    setattr(value, "uml2CD_Package10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml2CD_Association30(self):
        return self.__uml2CD_Association30

    @uml2CD_Association30.setter
    def uml2CD_Association30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2CD_Association__uml2CD_Association30", None)
        self.__uml2CD_Association30 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml2CD_Property31"):
                    opp_val = getattr(item, "uml2CD_Property31", None)
                    
                    if opp_val == self:
                        setattr(item, "uml2CD_Property31", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml2CD_Property31"):
                    opp_val = getattr(item, "uml2CD_Property31", None)
                    
                    setattr(item, "uml2CD_Property31", self)
                    

class uml2CD_DataType(NamedElement):

    pass