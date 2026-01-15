from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class uml2CD_UMLModel:

    pass
class DataType:

    pass
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

class uml2CD_Parameter:

    def __init__(self, kind: str, defaultValue: str, uml2CD_Parameter: "uml2CD_Enumeration" = None, uml2CD_Parameter26: "uml2CD_PrimitiveType" = None):
        self.kind = kind
        self.defaultValue = defaultValue
        self.uml2CD_Parameter = uml2CD_Parameter
        self.uml2CD_Parameter26 = uml2CD_Parameter26
        
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
            if hasattr(old_value, "uml2CD_Enumeration24"):
                opp_val = getattr(old_value, "uml2CD_Enumeration24", None)
                if opp_val == self:
                    setattr(old_value, "uml2CD_Enumeration24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml2CD_Enumeration24"):
                opp_val = getattr(value, "uml2CD_Enumeration24", None)
                setattr(value, "uml2CD_Enumeration24", self)

    @property
    def uml2CD_Parameter26(self):
        return self.__uml2CD_Parameter26

    @uml2CD_Parameter26.setter
    def uml2CD_Parameter26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2CD_Parameter__uml2CD_Parameter26", None)
        self.__uml2CD_Parameter26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml2CD_PrimitiveType27"):
                opp_val = getattr(old_value, "uml2CD_PrimitiveType27", None)
                if opp_val == self:
                    setattr(old_value, "uml2CD_PrimitiveType27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml2CD_PrimitiveType27"):
                opp_val = getattr(value, "uml2CD_PrimitiveType27", None)
                setattr(value, "uml2CD_PrimitiveType27", self)

class uml2CD_GeneralizationSet:

    def __init__(self, isCovering: str, isDisjoint: str, uml2CD_GeneralizationSet: "uml2CD_Generalization" = None):
        self.isCovering = isCovering
        self.isDisjoint = isDisjoint
        self.uml2CD_GeneralizationSet = uml2CD_GeneralizationSet
        
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
    def uml2CD_GeneralizationSet(self):
        return self.__uml2CD_GeneralizationSet

    @uml2CD_GeneralizationSet.setter
    def uml2CD_GeneralizationSet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2CD_GeneralizationSet__uml2CD_GeneralizationSet", None)
        self.__uml2CD_GeneralizationSet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml2CD_Generalization22"):
                opp_val = getattr(old_value, "uml2CD_Generalization22", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml2CD_Generalization22"):
                opp_val = getattr(value, "uml2CD_Generalization22", None)
                if opp_val is None:
                    setattr(value, "uml2CD_Generalization22", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class uml2CD_PrimitiveType(DataType):

    pass
class uml2CD_Generalization:

    def __init__(self, isSubstitutable: str, uml2CD_Generalization: "uml2CD_Package" = None, uml2CD_Generalization16: "uml2CD_Class" = None, uml2CD_Generalization19: "uml2CD_Class" = None, uml2CD_Generalization22: set["uml2CD_GeneralizationSet"] = None):
        self.isSubstitutable = isSubstitutable
        self.uml2CD_Generalization = uml2CD_Generalization
        self.uml2CD_Generalization16 = uml2CD_Generalization16
        self.uml2CD_Generalization19 = uml2CD_Generalization19
        self.uml2CD_Generalization22 = uml2CD_Generalization22 if uml2CD_Generalization22 is not None else set()
        
    @property
    def isSubstitutable(self) -> str:
        return self.__isSubstitutable

    @isSubstitutable.setter
    def isSubstitutable(self, isSubstitutable: str):
        self.__isSubstitutable = isSubstitutable

    @property
    def uml2CD_Generalization19(self):
        return self.__uml2CD_Generalization19

    @uml2CD_Generalization19.setter
    def uml2CD_Generalization19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2CD_Generalization__uml2CD_Generalization19", None)
        self.__uml2CD_Generalization19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml2CD_Class20"):
                opp_val = getattr(old_value, "uml2CD_Class20", None)
                if opp_val == self:
                    setattr(old_value, "uml2CD_Class20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml2CD_Class20"):
                opp_val = getattr(value, "uml2CD_Class20", None)
                setattr(value, "uml2CD_Class20", self)

    @property
    def uml2CD_Generalization22(self):
        return self.__uml2CD_Generalization22

    @uml2CD_Generalization22.setter
    def uml2CD_Generalization22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2CD_Generalization__uml2CD_Generalization22", None)
        self.__uml2CD_Generalization22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml2CD_GeneralizationSet"):
                    opp_val = getattr(item, "uml2CD_GeneralizationSet", None)
                    
                    if opp_val == self:
                        setattr(item, "uml2CD_GeneralizationSet", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml2CD_GeneralizationSet"):
                    opp_val = getattr(item, "uml2CD_GeneralizationSet", None)
                    
                    setattr(item, "uml2CD_GeneralizationSet", self)
                    

    @property
    def uml2CD_Generalization16(self):
        return self.__uml2CD_Generalization16

    @uml2CD_Generalization16.setter
    def uml2CD_Generalization16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2CD_Generalization__uml2CD_Generalization16", None)
        self.__uml2CD_Generalization16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml2CD_Class17"):
                opp_val = getattr(old_value, "uml2CD_Class17", None)
                if opp_val == self:
                    setattr(old_value, "uml2CD_Class17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml2CD_Class17"):
                opp_val = getattr(value, "uml2CD_Class17", None)
                setattr(value, "uml2CD_Class17", self)

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

class uml2CD_Enumeration(DataType):

    pass
class NamedElement:

    pass
class uml2CD_Association(NamedElement):

    def __init__(self, isDerived: str, uml2CD_Association: "uml2CD_Package" = None, uml2CD_Association36: set["uml2CD_Property"] = None, uml2CD_Association39: set["uml2CD_Property"] = None):
        self.isDerived = isDerived
        self.uml2CD_Association = uml2CD_Association
        self.uml2CD_Association36 = uml2CD_Association36 if uml2CD_Association36 is not None else set()
        self.uml2CD_Association39 = uml2CD_Association39 if uml2CD_Association39 is not None else set()
        
    @property
    def isDerived(self) -> str:
        return self.__isDerived

    @isDerived.setter
    def isDerived(self, isDerived: str):
        self.__isDerived = isDerived

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
    def uml2CD_Association39(self):
        return self.__uml2CD_Association39

    @uml2CD_Association39.setter
    def uml2CD_Association39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2CD_Association__uml2CD_Association39", None)
        self.__uml2CD_Association39 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml2CD_Property40"):
                    opp_val = getattr(item, "uml2CD_Property40", None)
                    
                    if opp_val == self:
                        setattr(item, "uml2CD_Property40", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml2CD_Property40"):
                    opp_val = getattr(item, "uml2CD_Property40", None)
                    
                    setattr(item, "uml2CD_Property40", self)
                    

    @property
    def uml2CD_Association36(self):
        return self.__uml2CD_Association36

    @uml2CD_Association36.setter
    def uml2CD_Association36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2CD_Association__uml2CD_Association36", None)
        self.__uml2CD_Association36 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml2CD_Property37"):
                    opp_val = getattr(item, "uml2CD_Property37", None)
                    
                    if opp_val == self:
                        setattr(item, "uml2CD_Property37", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml2CD_Property37"):
                    opp_val = getattr(item, "uml2CD_Property37", None)
                    
                    setattr(item, "uml2CD_Property37", self)
                    

class uml2CD_Operation(NamedElement):

    def __init__(self, isQuery: str, visibility: str, body: str, uml2CD_Operation: "uml2CD_Operation" = None, uml2CD_Operation28: set["uml2CD_Operation"] = None, uml2CD_Operation32: "uml2CD_Class" = None):
        self.isQuery = isQuery
        self.visibility = visibility
        self.body = body
        self.uml2CD_Operation = uml2CD_Operation
        self.uml2CD_Operation28 = uml2CD_Operation28 if uml2CD_Operation28 is not None else set()
        self.uml2CD_Operation32 = uml2CD_Operation32
        
    @property
    def isQuery(self) -> str:
        return self.__isQuery

    @isQuery.setter
    def isQuery(self, isQuery: str):
        self.__isQuery = isQuery

    @property
    def body(self) -> str:
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body

    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

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
            if hasattr(old_value, "uml2CD_Operation28"):
                opp_val = getattr(old_value, "uml2CD_Operation28", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml2CD_Operation28"):
                opp_val = getattr(value, "uml2CD_Operation28", None)
                if opp_val is None:
                    setattr(value, "uml2CD_Operation28", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml2CD_Operation32(self):
        return self.__uml2CD_Operation32

    @uml2CD_Operation32.setter
    def uml2CD_Operation32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2CD_Operation__uml2CD_Operation32", None)
        self.__uml2CD_Operation32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml2CD_Class31"):
                opp_val = getattr(old_value, "uml2CD_Class31", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml2CD_Class31"):
                opp_val = getattr(value, "uml2CD_Class31", None)
                if opp_val is None:
                    setattr(value, "uml2CD_Class31", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml2CD_Operation28(self):
        return self.__uml2CD_Operation28

    @uml2CD_Operation28.setter
    def uml2CD_Operation28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2CD_Operation__uml2CD_Operation28", None)
        self.__uml2CD_Operation28 = value if value is not None else set()
        
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
                    

class uml2CD_Property(NamedElement):

    def __init__(self, isDerived: str, aggregation: str, lower: str, upper: str, uml2CD_Property: "uml2CD_Class" = None, uml2CD_Property37: "uml2CD_Association" = None, uml2CD_Property40: "uml2CD_Association" = None):
        self.isDerived = isDerived
        self.aggregation = aggregation
        self.lower = lower
        self.upper = upper
        self.uml2CD_Property = uml2CD_Property
        self.uml2CD_Property37 = uml2CD_Property37
        self.uml2CD_Property40 = uml2CD_Property40
        
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
    def uml2CD_Property37(self):
        return self.__uml2CD_Property37

    @uml2CD_Property37.setter
    def uml2CD_Property37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2CD_Property__uml2CD_Property37", None)
        self.__uml2CD_Property37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml2CD_Association36"):
                opp_val = getattr(old_value, "uml2CD_Association36", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml2CD_Association36"):
                opp_val = getattr(value, "uml2CD_Association36", None)
                if opp_val is None:
                    setattr(value, "uml2CD_Association36", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml2CD_Property40(self):
        return self.__uml2CD_Property40

    @uml2CD_Property40.setter
    def uml2CD_Property40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2CD_Property__uml2CD_Property40", None)
        self.__uml2CD_Property40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml2CD_Association39"):
                opp_val = getattr(old_value, "uml2CD_Association39", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml2CD_Association39"):
                opp_val = getattr(value, "uml2CD_Association39", None)
                if opp_val is None:
                    setattr(value, "uml2CD_Association39", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
            if hasattr(old_value, "uml2CD_Class34"):
                opp_val = getattr(old_value, "uml2CD_Class34", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml2CD_Class34"):
                opp_val = getattr(value, "uml2CD_Class34", None)
                if opp_val is None:
                    setattr(value, "uml2CD_Class34", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class uml2CD_DataType(NamedElement):

    pass
class uml2CD_Class(NamedElement):

    def __init__(self, active: str, uml2CD_Class: "uml2CD_Package" = None, uml2CD_Class17: "uml2CD_Generalization" = None, uml2CD_Class20: "uml2CD_Generalization" = None, uml2CD_Class31: set["uml2CD_Operation"] = None, uml2CD_Class34: set["uml2CD_Property"] = None):
        self.active = active
        self.uml2CD_Class = uml2CD_Class
        self.uml2CD_Class17 = uml2CD_Class17
        self.uml2CD_Class20 = uml2CD_Class20
        self.uml2CD_Class31 = uml2CD_Class31 if uml2CD_Class31 is not None else set()
        self.uml2CD_Class34 = uml2CD_Class34 if uml2CD_Class34 is not None else set()
        
    @property
    def active(self) -> str:
        return self.__active

    @active.setter
    def active(self, active: str):
        self.__active = active

    @property
    def uml2CD_Class17(self):
        return self.__uml2CD_Class17

    @uml2CD_Class17.setter
    def uml2CD_Class17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2CD_Class__uml2CD_Class17", None)
        self.__uml2CD_Class17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml2CD_Generalization16"):
                opp_val = getattr(old_value, "uml2CD_Generalization16", None)
                if opp_val == self:
                    setattr(old_value, "uml2CD_Generalization16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml2CD_Generalization16"):
                opp_val = getattr(value, "uml2CD_Generalization16", None)
                setattr(value, "uml2CD_Generalization16", self)

    @property
    def uml2CD_Class31(self):
        return self.__uml2CD_Class31

    @uml2CD_Class31.setter
    def uml2CD_Class31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2CD_Class__uml2CD_Class31", None)
        self.__uml2CD_Class31 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml2CD_Operation32"):
                    opp_val = getattr(item, "uml2CD_Operation32", None)
                    
                    if opp_val == self:
                        setattr(item, "uml2CD_Operation32", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml2CD_Operation32"):
                    opp_val = getattr(item, "uml2CD_Operation32", None)
                    
                    setattr(item, "uml2CD_Operation32", self)
                    

    @property
    def uml2CD_Class20(self):
        return self.__uml2CD_Class20

    @uml2CD_Class20.setter
    def uml2CD_Class20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2CD_Class__uml2CD_Class20", None)
        self.__uml2CD_Class20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml2CD_Generalization19"):
                opp_val = getattr(old_value, "uml2CD_Generalization19", None)
                if opp_val == self:
                    setattr(old_value, "uml2CD_Generalization19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml2CD_Generalization19"):
                opp_val = getattr(value, "uml2CD_Generalization19", None)
                setattr(value, "uml2CD_Generalization19", self)

    @property
    def uml2CD_Class34(self):
        return self.__uml2CD_Class34

    @uml2CD_Class34.setter
    def uml2CD_Class34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2CD_Class__uml2CD_Class34", None)
        self.__uml2CD_Class34 = value if value is not None else set()
        
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
