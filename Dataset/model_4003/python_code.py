from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class UML_14_Model:

    pass
class UML_14_Comment:

    def __init__(self, body: str, UML_14_Comment: "UML_14_NamedElement" = None):
        self.body = body
        self.UML_14_Comment = UML_14_Comment
        
    @property
    def body(self) -> str:
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body

    @property
    def UML_14_Comment(self):
        return self.__UML_14_Comment

    @UML_14_Comment.setter
    def UML_14_Comment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_Comment__UML_14_Comment", None)
        self.__UML_14_Comment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML_14_NamedElement"):
                opp_val = getattr(old_value, "UML_14_NamedElement", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML_14_NamedElement"):
                opp_val = getattr(value, "UML_14_NamedElement", None)
                if opp_val is None:
                    setattr(value, "UML_14_NamedElement", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class UML_14_EnumerationLiteral:

    def __init__(self, value: str, EnumerationLiteral: "UML_14_Enumeration" = None, literal: "UML_14_Enumeration" = None):
        self.value = value
        self.EnumerationLiteral = EnumerationLiteral
        self.literal = literal
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def literal(self):
        return self.__literal

    @literal.setter
    def literal(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_EnumerationLiteral__literal", None)
        self.__literal = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Enumeration"):
                opp_val = getattr(old_value, "Enumeration", None)
                if opp_val == self:
                    setattr(old_value, "Enumeration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Enumeration"):
                opp_val = getattr(value, "Enumeration", None)
                setattr(value, "Enumeration", self)

    @property
    def EnumerationLiteral(self):
        return self.__EnumerationLiteral

    @EnumerationLiteral.setter
    def EnumerationLiteral(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_EnumerationLiteral__EnumerationLiteral", None)
        self.__EnumerationLiteral = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "enumeration"):
                opp_val = getattr(old_value, "enumeration", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "enumeration"):
                opp_val = getattr(value, "enumeration", None)
                if opp_val is None:
                    setattr(value, "enumeration", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class UML_14_NamedElement(ABC):

    def __init__(self, name: str, UML_14_NamedElement: set["UML_14_Comment"] = None, UML_14_NamedElement46: set["UML_14_Constraint"] = None):
        self.name = name
        self.UML_14_NamedElement = UML_14_NamedElement if UML_14_NamedElement is not None else set()
        self.UML_14_NamedElement46 = UML_14_NamedElement46 if UML_14_NamedElement46 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def UML_14_NamedElement(self):
        return self.__UML_14_NamedElement

    @UML_14_NamedElement.setter
    def UML_14_NamedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_NamedElement__UML_14_NamedElement", None)
        self.__UML_14_NamedElement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML_14_Comment"):
                    opp_val = getattr(item, "UML_14_Comment", None)
                    
                    if opp_val == self:
                        setattr(item, "UML_14_Comment", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML_14_Comment"):
                    opp_val = getattr(item, "UML_14_Comment", None)
                    
                    setattr(item, "UML_14_Comment", self)
                    

    @property
    def UML_14_NamedElement46(self):
        return self.__UML_14_NamedElement46

    @UML_14_NamedElement46.setter
    def UML_14_NamedElement46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_NamedElement__UML_14_NamedElement46", None)
        self.__UML_14_NamedElement46 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML_14_Constraint"):
                    opp_val = getattr(item, "UML_14_Constraint", None)
                    
                    if opp_val == self:
                        setattr(item, "UML_14_Constraint", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML_14_Constraint"):
                    opp_val = getattr(item, "UML_14_Constraint", None)
                    
                    setattr(item, "UML_14_Constraint", self)
                    

class UML_14_Generalization:

    def __init__(self, discriminator: str, UML_14_Generalization: set["UML_14_Class"] = None, UML_14_Generalization9: set["UML_14_Class"] = None, UML_14_Generalization41: "UML_14_Package" = None):
        self.discriminator = discriminator
        self.UML_14_Generalization = UML_14_Generalization if UML_14_Generalization is not None else set()
        self.UML_14_Generalization9 = UML_14_Generalization9 if UML_14_Generalization9 is not None else set()
        self.UML_14_Generalization41 = UML_14_Generalization41
        
    @property
    def discriminator(self) -> str:
        return self.__discriminator

    @discriminator.setter
    def discriminator(self, discriminator: str):
        self.__discriminator = discriminator

    @property
    def UML_14_Generalization41(self):
        return self.__UML_14_Generalization41

    @UML_14_Generalization41.setter
    def UML_14_Generalization41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_Generalization__UML_14_Generalization41", None)
        self.__UML_14_Generalization41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML_14_Package40"):
                opp_val = getattr(old_value, "UML_14_Package40", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML_14_Package40"):
                opp_val = getattr(value, "UML_14_Package40", None)
                if opp_val is None:
                    setattr(value, "UML_14_Package40", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML_14_Generalization(self):
        return self.__UML_14_Generalization

    @UML_14_Generalization.setter
    def UML_14_Generalization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_Generalization__UML_14_Generalization", None)
        self.__UML_14_Generalization = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML_14_Class"):
                    opp_val = getattr(item, "UML_14_Class", None)
                    
                    if opp_val == self:
                        setattr(item, "UML_14_Class", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML_14_Class"):
                    opp_val = getattr(item, "UML_14_Class", None)
                    
                    setattr(item, "UML_14_Class", self)
                    

    @property
    def UML_14_Generalization9(self):
        return self.__UML_14_Generalization9

    @UML_14_Generalization9.setter
    def UML_14_Generalization9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_Generalization__UML_14_Generalization9", None)
        self.__UML_14_Generalization9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML_14_Class10"):
                    opp_val = getattr(item, "UML_14_Class10", None)
                    
                    if opp_val == self:
                        setattr(item, "UML_14_Class10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML_14_Class10"):
                    opp_val = getattr(item, "UML_14_Class10", None)
                    
                    setattr(item, "UML_14_Class10", self)
                    

class DataType:

    pass
class UML_14_Enumeration(DataType):

    pass
class UML_14_Primitive(DataType):

    pass
class UML_14_MultiplicityRange:

    def __init__(self, lower: str, upper: str, UML_14_MultiplicityRange17: "UML_14_AssociationEnd" = None, UML_14_MultiplicityRange: "UML_14_Attribute" = None):
        self.lower = lower
        self.upper = upper
        self.UML_14_MultiplicityRange17 = UML_14_MultiplicityRange17
        self.UML_14_MultiplicityRange = UML_14_MultiplicityRange
        
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
    def UML_14_MultiplicityRange(self):
        return self.__UML_14_MultiplicityRange

    @UML_14_MultiplicityRange.setter
    def UML_14_MultiplicityRange(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_MultiplicityRange__UML_14_MultiplicityRange", None)
        self.__UML_14_MultiplicityRange = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML_14_Attribute"):
                opp_val = getattr(old_value, "UML_14_Attribute", None)
                if opp_val == self:
                    setattr(old_value, "UML_14_Attribute", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML_14_Attribute"):
                opp_val = getattr(value, "UML_14_Attribute", None)
                setattr(value, "UML_14_Attribute", self)

    @property
    def UML_14_MultiplicityRange17(self):
        return self.__UML_14_MultiplicityRange17

    @UML_14_MultiplicityRange17.setter
    def UML_14_MultiplicityRange17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_MultiplicityRange__UML_14_MultiplicityRange17", None)
        self.__UML_14_MultiplicityRange17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML_14_AssociationEnd16"):
                opp_val = getattr(old_value, "UML_14_AssociationEnd16", None)
                if opp_val == self:
                    setattr(old_value, "UML_14_AssociationEnd16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML_14_AssociationEnd16"):
                opp_val = getattr(value, "UML_14_AssociationEnd16", None)
                setattr(value, "UML_14_AssociationEnd16", self)

class UML_14_Constraint(ABC):

    def __init__(self, body: str, UML_14_Constraint: "UML_14_NamedElement" = None):
        self.body = body
        self.UML_14_Constraint = UML_14_Constraint
        
    @property
    def body(self) -> str:
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body

    @property
    def UML_14_Constraint(self):
        return self.__UML_14_Constraint

    @UML_14_Constraint.setter
    def UML_14_Constraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_Constraint__UML_14_Constraint", None)
        self.__UML_14_Constraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML_14_NamedElement46"):
                opp_val = getattr(old_value, "UML_14_NamedElement46", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML_14_NamedElement46"):
                opp_val = getattr(value, "UML_14_NamedElement46", None)
                if opp_val is None:
                    setattr(value, "UML_14_NamedElement46", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class NamedElement:

    pass
class UML_14_Method(NamedElement):

    def __init__(self, body: str, visibility: str, UML_14_Method26: "UML_14_Class" = None, UML_14_Method: set["UML_14_Parameter"] = None):
        self.body = body
        self.visibility = visibility
        self.UML_14_Method26 = UML_14_Method26
        self.UML_14_Method = UML_14_Method if UML_14_Method is not None else set()
        
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
    def UML_14_Method(self):
        return self.__UML_14_Method

    @UML_14_Method.setter
    def UML_14_Method(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_Method__UML_14_Method", None)
        self.__UML_14_Method = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML_14_Parameter2"):
                    opp_val = getattr(item, "UML_14_Parameter2", None)
                    
                    if opp_val == self:
                        setattr(item, "UML_14_Parameter2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML_14_Parameter2"):
                    opp_val = getattr(item, "UML_14_Parameter2", None)
                    
                    setattr(item, "UML_14_Parameter2", self)
                    

    @property
    def UML_14_Method26(self):
        return self.__UML_14_Method26

    @UML_14_Method26.setter
    def UML_14_Method26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_Method__UML_14_Method26", None)
        self.__UML_14_Method26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML_14_Class25"):
                opp_val = getattr(old_value, "UML_14_Class25", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML_14_Class25"):
                opp_val = getattr(value, "UML_14_Class25", None)
                if opp_val is None:
                    setattr(value, "UML_14_Class25", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class UML_14_Association(NamedElement):

    pass
class UML_14_AssociationEnd(NamedElement):

    def __init__(self, isNavigable: str, visibility: str, AssociationEnd: "UML_14_Association" = None, connection: "UML_14_Association" = None, UML_14_AssociationEnd: "UML_14_Class" = None, UML_14_AssociationEnd16: "UML_14_MultiplicityRange" = None, UML_14_AssociationEnd19: "UML_14_Attribute" = None):
        self.isNavigable = isNavigable
        self.visibility = visibility
        self.AssociationEnd = AssociationEnd
        self.connection = connection
        self.UML_14_AssociationEnd = UML_14_AssociationEnd
        self.UML_14_AssociationEnd16 = UML_14_AssociationEnd16
        self.UML_14_AssociationEnd19 = UML_14_AssociationEnd19
        
    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

    @property
    def isNavigable(self) -> str:
        return self.__isNavigable

    @isNavigable.setter
    def isNavigable(self, isNavigable: str):
        self.__isNavigable = isNavigable

    @property
    def UML_14_AssociationEnd19(self):
        return self.__UML_14_AssociationEnd19

    @UML_14_AssociationEnd19.setter
    def UML_14_AssociationEnd19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_AssociationEnd__UML_14_AssociationEnd19", None)
        self.__UML_14_AssociationEnd19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML_14_Attribute20"):
                opp_val = getattr(old_value, "UML_14_Attribute20", None)
                if opp_val == self:
                    setattr(old_value, "UML_14_Attribute20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML_14_Attribute20"):
                opp_val = getattr(value, "UML_14_Attribute20", None)
                setattr(value, "UML_14_Attribute20", self)

    @property
    def AssociationEnd(self):
        return self.__AssociationEnd

    @AssociationEnd.setter
    def AssociationEnd(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_AssociationEnd__AssociationEnd", None)
        self.__AssociationEnd = value
        
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
    def connection(self):
        return self.__connection

    @connection.setter
    def connection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_AssociationEnd__connection", None)
        self.__connection = value
        
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

    @property
    def UML_14_AssociationEnd(self):
        return self.__UML_14_AssociationEnd

    @UML_14_AssociationEnd.setter
    def UML_14_AssociationEnd(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_AssociationEnd__UML_14_AssociationEnd", None)
        self.__UML_14_AssociationEnd = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML_14_Class14"):
                opp_val = getattr(old_value, "UML_14_Class14", None)
                if opp_val == self:
                    setattr(old_value, "UML_14_Class14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML_14_Class14"):
                opp_val = getattr(value, "UML_14_Class14", None)
                setattr(value, "UML_14_Class14", self)

    @property
    def UML_14_AssociationEnd16(self):
        return self.__UML_14_AssociationEnd16

    @UML_14_AssociationEnd16.setter
    def UML_14_AssociationEnd16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_AssociationEnd__UML_14_AssociationEnd16", None)
        self.__UML_14_AssociationEnd16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML_14_MultiplicityRange17"):
                opp_val = getattr(old_value, "UML_14_MultiplicityRange17", None)
                if opp_val == self:
                    setattr(old_value, "UML_14_MultiplicityRange17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML_14_MultiplicityRange17"):
                opp_val = getattr(value, "UML_14_MultiplicityRange17", None)
                setattr(value, "UML_14_MultiplicityRange17", self)

class UML_14_Package(NamedElement):

    pass
class UML_14_DataType(NamedElement):

    pass
class UML_14_Class(NamedElement):

    def __init__(self, isActive: str, UML_14_Class: "UML_14_Generalization" = None, UML_14_Class10: "UML_14_Generalization" = None, UML_14_Class14: "UML_14_AssociationEnd" = None, UML_14_Class22: set["UML_14_Attribute"] = None, UML_14_Class25: set["UML_14_Method"] = None, UML_14_Class32: "UML_14_Package" = None):
        self.isActive = isActive
        self.UML_14_Class = UML_14_Class
        self.UML_14_Class10 = UML_14_Class10
        self.UML_14_Class14 = UML_14_Class14
        self.UML_14_Class22 = UML_14_Class22 if UML_14_Class22 is not None else set()
        self.UML_14_Class25 = UML_14_Class25 if UML_14_Class25 is not None else set()
        self.UML_14_Class32 = UML_14_Class32
        
    @property
    def isActive(self) -> str:
        return self.__isActive

    @isActive.setter
    def isActive(self, isActive: str):
        self.__isActive = isActive

    @property
    def UML_14_Class32(self):
        return self.__UML_14_Class32

    @UML_14_Class32.setter
    def UML_14_Class32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_Class__UML_14_Class32", None)
        self.__UML_14_Class32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML_14_Package31"):
                opp_val = getattr(old_value, "UML_14_Package31", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML_14_Package31"):
                opp_val = getattr(value, "UML_14_Package31", None)
                if opp_val is None:
                    setattr(value, "UML_14_Package31", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML_14_Class10(self):
        return self.__UML_14_Class10

    @UML_14_Class10.setter
    def UML_14_Class10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_Class__UML_14_Class10", None)
        self.__UML_14_Class10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML_14_Generalization9"):
                opp_val = getattr(old_value, "UML_14_Generalization9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML_14_Generalization9"):
                opp_val = getattr(value, "UML_14_Generalization9", None)
                if opp_val is None:
                    setattr(value, "UML_14_Generalization9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML_14_Class22(self):
        return self.__UML_14_Class22

    @UML_14_Class22.setter
    def UML_14_Class22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_Class__UML_14_Class22", None)
        self.__UML_14_Class22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML_14_Attribute23"):
                    opp_val = getattr(item, "UML_14_Attribute23", None)
                    
                    if opp_val == self:
                        setattr(item, "UML_14_Attribute23", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML_14_Attribute23"):
                    opp_val = getattr(item, "UML_14_Attribute23", None)
                    
                    setattr(item, "UML_14_Attribute23", self)
                    

    @property
    def UML_14_Class25(self):
        return self.__UML_14_Class25

    @UML_14_Class25.setter
    def UML_14_Class25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_Class__UML_14_Class25", None)
        self.__UML_14_Class25 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML_14_Method26"):
                    opp_val = getattr(item, "UML_14_Method26", None)
                    
                    if opp_val == self:
                        setattr(item, "UML_14_Method26", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML_14_Method26"):
                    opp_val = getattr(item, "UML_14_Method26", None)
                    
                    setattr(item, "UML_14_Method26", self)
                    

    @property
    def UML_14_Class14(self):
        return self.__UML_14_Class14

    @UML_14_Class14.setter
    def UML_14_Class14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_Class__UML_14_Class14", None)
        self.__UML_14_Class14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML_14_AssociationEnd"):
                opp_val = getattr(old_value, "UML_14_AssociationEnd", None)
                if opp_val == self:
                    setattr(old_value, "UML_14_AssociationEnd", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML_14_AssociationEnd"):
                opp_val = getattr(value, "UML_14_AssociationEnd", None)
                setattr(value, "UML_14_AssociationEnd", self)

    @property
    def UML_14_Class(self):
        return self.__UML_14_Class

    @UML_14_Class.setter
    def UML_14_Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_Class__UML_14_Class", None)
        self.__UML_14_Class = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML_14_Generalization"):
                opp_val = getattr(old_value, "UML_14_Generalization", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML_14_Generalization"):
                opp_val = getattr(value, "UML_14_Generalization", None)
                if opp_val is None:
                    setattr(value, "UML_14_Generalization", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class UML_14_Attribute(NamedElement):

    def __init__(self, initialValue: str, visibility: str, UML_14_Attribute20: "UML_14_AssociationEnd" = None, UML_14_Attribute23: "UML_14_Class" = None, UML_14_Attribute: "UML_14_MultiplicityRange" = None, UML_14_Attribute5: "UML_14_DataType" = None):
        self.initialValue = initialValue
        self.visibility = visibility
        self.UML_14_Attribute20 = UML_14_Attribute20
        self.UML_14_Attribute23 = UML_14_Attribute23
        self.UML_14_Attribute = UML_14_Attribute
        self.UML_14_Attribute5 = UML_14_Attribute5
        
    @property
    def initialValue(self) -> str:
        return self.__initialValue

    @initialValue.setter
    def initialValue(self, initialValue: str):
        self.__initialValue = initialValue

    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

    @property
    def UML_14_Attribute(self):
        return self.__UML_14_Attribute

    @UML_14_Attribute.setter
    def UML_14_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_Attribute__UML_14_Attribute", None)
        self.__UML_14_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML_14_MultiplicityRange"):
                opp_val = getattr(old_value, "UML_14_MultiplicityRange", None)
                if opp_val == self:
                    setattr(old_value, "UML_14_MultiplicityRange", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML_14_MultiplicityRange"):
                opp_val = getattr(value, "UML_14_MultiplicityRange", None)
                setattr(value, "UML_14_MultiplicityRange", self)

    @property
    def UML_14_Attribute23(self):
        return self.__UML_14_Attribute23

    @UML_14_Attribute23.setter
    def UML_14_Attribute23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_Attribute__UML_14_Attribute23", None)
        self.__UML_14_Attribute23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML_14_Class22"):
                opp_val = getattr(old_value, "UML_14_Class22", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML_14_Class22"):
                opp_val = getattr(value, "UML_14_Class22", None)
                if opp_val is None:
                    setattr(value, "UML_14_Class22", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML_14_Attribute5(self):
        return self.__UML_14_Attribute5

    @UML_14_Attribute5.setter
    def UML_14_Attribute5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_Attribute__UML_14_Attribute5", None)
        self.__UML_14_Attribute5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML_14_DataType6"):
                opp_val = getattr(old_value, "UML_14_DataType6", None)
                if opp_val == self:
                    setattr(old_value, "UML_14_DataType6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML_14_DataType6"):
                opp_val = getattr(value, "UML_14_DataType6", None)
                setattr(value, "UML_14_DataType6", self)

    @property
    def UML_14_Attribute20(self):
        return self.__UML_14_Attribute20

    @UML_14_Attribute20.setter
    def UML_14_Attribute20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_Attribute__UML_14_Attribute20", None)
        self.__UML_14_Attribute20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML_14_AssociationEnd19"):
                opp_val = getattr(old_value, "UML_14_AssociationEnd19", None)
                if opp_val == self:
                    setattr(old_value, "UML_14_AssociationEnd19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML_14_AssociationEnd19"):
                opp_val = getattr(value, "UML_14_AssociationEnd19", None)
                setattr(value, "UML_14_AssociationEnd19", self)

class UML_14_Parameter(NamedElement):

    def __init__(self, kind: str, defaultValue: str, UML_14_Parameter: "UML_14_DataType" = None, UML_14_Parameter2: "UML_14_Method" = None):
        self.kind = kind
        self.defaultValue = defaultValue
        self.UML_14_Parameter = UML_14_Parameter
        self.UML_14_Parameter2 = UML_14_Parameter2
        
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
    def UML_14_Parameter2(self):
        return self.__UML_14_Parameter2

    @UML_14_Parameter2.setter
    def UML_14_Parameter2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_Parameter__UML_14_Parameter2", None)
        self.__UML_14_Parameter2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML_14_Method"):
                opp_val = getattr(old_value, "UML_14_Method", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML_14_Method"):
                opp_val = getattr(value, "UML_14_Method", None)
                if opp_val is None:
                    setattr(value, "UML_14_Method", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML_14_Parameter(self):
        return self.__UML_14_Parameter

    @UML_14_Parameter.setter
    def UML_14_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_Parameter__UML_14_Parameter", None)
        self.__UML_14_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML_14_DataType"):
                opp_val = getattr(old_value, "UML_14_DataType", None)
                if opp_val == self:
                    setattr(old_value, "UML_14_DataType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML_14_DataType"):
                opp_val = getattr(value, "UML_14_DataType", None)
                setattr(value, "UML_14_DataType", self)
