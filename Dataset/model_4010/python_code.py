from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class UML_14_EnumerationLiteral:

    def __init__(self, value: str, UML_14_EnumerationLiteral: "UML_14_Enumeration" = None):
        self.value = value
        self.UML_14_EnumerationLiteral = UML_14_EnumerationLiteral
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def UML_14_EnumerationLiteral(self):
        return self.__UML_14_EnumerationLiteral

    @UML_14_EnumerationLiteral.setter
    def UML_14_EnumerationLiteral(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_EnumerationLiteral__UML_14_EnumerationLiteral", None)
        self.__UML_14_EnumerationLiteral = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML_14_Enumeration33"):
                opp_val = getattr(old_value, "UML_14_Enumeration33", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML_14_Enumeration33"):
                opp_val = getattr(value, "UML_14_Enumeration33", None)
                if opp_val is None:
                    setattr(value, "UML_14_Enumeration33", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class UML_14_NamedElement(ABC):

    def __init__(self, name: str, UML_14_NamedElement: set["UML_14_Comment"] = None, UML_14_NamedElement54: set["UML_14_Constraint"] = None):
        self.name = name
        self.UML_14_NamedElement = UML_14_NamedElement if UML_14_NamedElement is not None else set()
        self.UML_14_NamedElement54 = UML_14_NamedElement54 if UML_14_NamedElement54 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def UML_14_NamedElement54(self):
        return self.__UML_14_NamedElement54

    @UML_14_NamedElement54.setter
    def UML_14_NamedElement54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_NamedElement__UML_14_NamedElement54", None)
        self.__UML_14_NamedElement54 = value if value is not None else set()
        
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

class UML_14_MultiplicityRange:

    def __init__(self, lower: str, upper: str, UML_14_MultiplicityRange: "UML_14_Attribute" = None, UML_14_MultiplicityRange22: "UML_14_AssociationEnd" = None):
        self.lower = lower
        self.upper = upper
        self.UML_14_MultiplicityRange = UML_14_MultiplicityRange
        self.UML_14_MultiplicityRange22 = UML_14_MultiplicityRange22
        
    @property
    def upper(self) -> str:
        return self.__upper

    @upper.setter
    def upper(self, upper: str):
        self.__upper = upper

    @property
    def lower(self) -> str:
        return self.__lower

    @lower.setter
    def lower(self, lower: str):
        self.__lower = lower

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
    def UML_14_MultiplicityRange22(self):
        return self.__UML_14_MultiplicityRange22

    @UML_14_MultiplicityRange22.setter
    def UML_14_MultiplicityRange22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_MultiplicityRange__UML_14_MultiplicityRange22", None)
        self.__UML_14_MultiplicityRange22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML_14_AssociationEnd21"):
                opp_val = getattr(old_value, "UML_14_AssociationEnd21", None)
                if opp_val == self:
                    setattr(old_value, "UML_14_AssociationEnd21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML_14_AssociationEnd21"):
                opp_val = getattr(value, "UML_14_AssociationEnd21", None)
                setattr(value, "UML_14_AssociationEnd21", self)

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
            if hasattr(old_value, "UML_14_NamedElement54"):
                opp_val = getattr(old_value, "UML_14_NamedElement54", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML_14_NamedElement54"):
                opp_val = getattr(value, "UML_14_NamedElement54", None)
                if opp_val is None:
                    setattr(value, "UML_14_NamedElement54", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class UML_14_Generalization:

    def __init__(self, discriminator: str, UML_14_Generalization: set["UML_14_Class"] = None, UML_14_Generalization14: set["UML_14_Class"] = None, UML_14_Generalization46: "UML_14_Package" = None):
        self.discriminator = discriminator
        self.UML_14_Generalization = UML_14_Generalization if UML_14_Generalization is not None else set()
        self.UML_14_Generalization14 = UML_14_Generalization14 if UML_14_Generalization14 is not None else set()
        self.UML_14_Generalization46 = UML_14_Generalization46
        
    @property
    def discriminator(self) -> str:
        return self.__discriminator

    @discriminator.setter
    def discriminator(self, discriminator: str):
        self.__discriminator = discriminator

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
    def UML_14_Generalization14(self):
        return self.__UML_14_Generalization14

    @UML_14_Generalization14.setter
    def UML_14_Generalization14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_Generalization__UML_14_Generalization14", None)
        self.__UML_14_Generalization14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML_14_Class15"):
                    opp_val = getattr(item, "UML_14_Class15", None)
                    
                    if opp_val == self:
                        setattr(item, "UML_14_Class15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML_14_Class15"):
                    opp_val = getattr(item, "UML_14_Class15", None)
                    
                    setattr(item, "UML_14_Class15", self)
                    

    @property
    def UML_14_Generalization46(self):
        return self.__UML_14_Generalization46

    @UML_14_Generalization46.setter
    def UML_14_Generalization46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_Generalization__UML_14_Generalization46", None)
        self.__UML_14_Generalization46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML_14_Package45"):
                opp_val = getattr(old_value, "UML_14_Package45", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML_14_Package45"):
                opp_val = getattr(value, "UML_14_Package45", None)
                if opp_val is None:
                    setattr(value, "UML_14_Package45", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class NamedElement:

    pass
class UML_14_Class(NamedElement):

    def __init__(self, isActive: str, UML_14_Class: "UML_14_Generalization" = None, UML_14_Class15: "UML_14_Generalization" = None, UML_14_Class19: "UML_14_AssociationEnd" = None, UML_14_Class37: "UML_14_Package" = None, UML_14_Class27: set["UML_14_Attribute"] = None, UML_14_Class30: set["UML_14_Method"] = None):
        self.isActive = isActive
        self.UML_14_Class = UML_14_Class
        self.UML_14_Class15 = UML_14_Class15
        self.UML_14_Class19 = UML_14_Class19
        self.UML_14_Class37 = UML_14_Class37
        self.UML_14_Class27 = UML_14_Class27 if UML_14_Class27 is not None else set()
        self.UML_14_Class30 = UML_14_Class30 if UML_14_Class30 is not None else set()
        
    @property
    def isActive(self) -> str:
        return self.__isActive

    @isActive.setter
    def isActive(self, isActive: str):
        self.__isActive = isActive

    @property
    def UML_14_Class27(self):
        return self.__UML_14_Class27

    @UML_14_Class27.setter
    def UML_14_Class27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_Class__UML_14_Class27", None)
        self.__UML_14_Class27 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML_14_Attribute28"):
                    opp_val = getattr(item, "UML_14_Attribute28", None)
                    
                    if opp_val == self:
                        setattr(item, "UML_14_Attribute28", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML_14_Attribute28"):
                    opp_val = getattr(item, "UML_14_Attribute28", None)
                    
                    setattr(item, "UML_14_Attribute28", self)
                    

    @property
    def UML_14_Class30(self):
        return self.__UML_14_Class30

    @UML_14_Class30.setter
    def UML_14_Class30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_Class__UML_14_Class30", None)
        self.__UML_14_Class30 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML_14_Method31"):
                    opp_val = getattr(item, "UML_14_Method31", None)
                    
                    if opp_val == self:
                        setattr(item, "UML_14_Method31", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML_14_Method31"):
                    opp_val = getattr(item, "UML_14_Method31", None)
                    
                    setattr(item, "UML_14_Method31", self)
                    

    @property
    def UML_14_Class15(self):
        return self.__UML_14_Class15

    @UML_14_Class15.setter
    def UML_14_Class15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_Class__UML_14_Class15", None)
        self.__UML_14_Class15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML_14_Generalization14"):
                opp_val = getattr(old_value, "UML_14_Generalization14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML_14_Generalization14"):
                opp_val = getattr(value, "UML_14_Generalization14", None)
                if opp_val is None:
                    setattr(value, "UML_14_Generalization14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML_14_Class37(self):
        return self.__UML_14_Class37

    @UML_14_Class37.setter
    def UML_14_Class37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_Class__UML_14_Class37", None)
        self.__UML_14_Class37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML_14_Package36"):
                opp_val = getattr(old_value, "UML_14_Package36", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML_14_Package36"):
                opp_val = getattr(value, "UML_14_Package36", None)
                if opp_val is None:
                    setattr(value, "UML_14_Package36", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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

    @property
    def UML_14_Class19(self):
        return self.__UML_14_Class19

    @UML_14_Class19.setter
    def UML_14_Class19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_Class__UML_14_Class19", None)
        self.__UML_14_Class19 = value
        
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

class UML_14_Method(NamedElement):

    def __init__(self, body: str, visibility: str, UML_14_Method: set["UML_14_Parameter"] = None, UML_14_Method31: "UML_14_Class" = None):
        self.body = body
        self.visibility = visibility
        self.UML_14_Method = UML_14_Method if UML_14_Method is not None else set()
        self.UML_14_Method31 = UML_14_Method31
        
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
    def UML_14_Method31(self):
        return self.__UML_14_Method31

    @UML_14_Method31.setter
    def UML_14_Method31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_Method__UML_14_Method31", None)
        self.__UML_14_Method31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML_14_Class30"):
                opp_val = getattr(old_value, "UML_14_Class30", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML_14_Class30"):
                opp_val = getattr(value, "UML_14_Class30", None)
                if opp_val is None:
                    setattr(value, "UML_14_Class30", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
                if hasattr(item, "UML_14_Parameter5"):
                    opp_val = getattr(item, "UML_14_Parameter5", None)
                    
                    if opp_val == self:
                        setattr(item, "UML_14_Parameter5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML_14_Parameter5"):
                    opp_val = getattr(item, "UML_14_Parameter5", None)
                    
                    setattr(item, "UML_14_Parameter5", self)
                    

class UML_14_AssociationEnd(NamedElement):

    def __init__(self, isNavigable: str, visibility: str, AssociationEnd: "UML_14_Association" = None, connection: "UML_14_Association" = None, UML_14_AssociationEnd: "UML_14_Class" = None, UML_14_AssociationEnd21: "UML_14_MultiplicityRange" = None, UML_14_AssociationEnd24: "UML_14_Attribute" = None):
        self.isNavigable = isNavigable
        self.visibility = visibility
        self.AssociationEnd = AssociationEnd
        self.connection = connection
        self.UML_14_AssociationEnd = UML_14_AssociationEnd
        self.UML_14_AssociationEnd21 = UML_14_AssociationEnd21
        self.UML_14_AssociationEnd24 = UML_14_AssociationEnd24
        
    @property
    def isNavigable(self) -> str:
        return self.__isNavigable

    @isNavigable.setter
    def isNavigable(self, isNavigable: str):
        self.__isNavigable = isNavigable

    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

    @property
    def UML_14_AssociationEnd24(self):
        return self.__UML_14_AssociationEnd24

    @UML_14_AssociationEnd24.setter
    def UML_14_AssociationEnd24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_AssociationEnd__UML_14_AssociationEnd24", None)
        self.__UML_14_AssociationEnd24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML_14_Attribute25"):
                opp_val = getattr(old_value, "UML_14_Attribute25", None)
                if opp_val == self:
                    setattr(old_value, "UML_14_Attribute25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML_14_Attribute25"):
                opp_val = getattr(value, "UML_14_Attribute25", None)
                setattr(value, "UML_14_Attribute25", self)

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
    def UML_14_AssociationEnd21(self):
        return self.__UML_14_AssociationEnd21

    @UML_14_AssociationEnd21.setter
    def UML_14_AssociationEnd21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_AssociationEnd__UML_14_AssociationEnd21", None)
        self.__UML_14_AssociationEnd21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML_14_MultiplicityRange22"):
                opp_val = getattr(old_value, "UML_14_MultiplicityRange22", None)
                if opp_val == self:
                    setattr(old_value, "UML_14_MultiplicityRange22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML_14_MultiplicityRange22"):
                opp_val = getattr(value, "UML_14_MultiplicityRange22", None)
                setattr(value, "UML_14_MultiplicityRange22", self)

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
            if hasattr(old_value, "UML_14_Class19"):
                opp_val = getattr(old_value, "UML_14_Class19", None)
                if opp_val == self:
                    setattr(old_value, "UML_14_Class19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML_14_Class19"):
                opp_val = getattr(value, "UML_14_Class19", None)
                setattr(value, "UML_14_Class19", self)

class UML_14_Attribute(NamedElement):

    def __init__(self, visibility: str, initialValue: str, UML_14_Attribute: "UML_14_MultiplicityRange" = None, UML_14_Attribute8: "UML_14_Enumeration" = None, UML_14_Attribute11: "UML_14_Primitive" = None, UML_14_Attribute25: "UML_14_AssociationEnd" = None, UML_14_Attribute28: "UML_14_Class" = None):
        self.visibility = visibility
        self.initialValue = initialValue
        self.UML_14_Attribute = UML_14_Attribute
        self.UML_14_Attribute8 = UML_14_Attribute8
        self.UML_14_Attribute11 = UML_14_Attribute11
        self.UML_14_Attribute25 = UML_14_Attribute25
        self.UML_14_Attribute28 = UML_14_Attribute28
        
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
    def UML_14_Attribute8(self):
        return self.__UML_14_Attribute8

    @UML_14_Attribute8.setter
    def UML_14_Attribute8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_Attribute__UML_14_Attribute8", None)
        self.__UML_14_Attribute8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML_14_Enumeration9"):
                opp_val = getattr(old_value, "UML_14_Enumeration9", None)
                if opp_val == self:
                    setattr(old_value, "UML_14_Enumeration9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML_14_Enumeration9"):
                opp_val = getattr(value, "UML_14_Enumeration9", None)
                setattr(value, "UML_14_Enumeration9", self)

    @property
    def UML_14_Attribute25(self):
        return self.__UML_14_Attribute25

    @UML_14_Attribute25.setter
    def UML_14_Attribute25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_Attribute__UML_14_Attribute25", None)
        self.__UML_14_Attribute25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML_14_AssociationEnd24"):
                opp_val = getattr(old_value, "UML_14_AssociationEnd24", None)
                if opp_val == self:
                    setattr(old_value, "UML_14_AssociationEnd24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML_14_AssociationEnd24"):
                opp_val = getattr(value, "UML_14_AssociationEnd24", None)
                setattr(value, "UML_14_AssociationEnd24", self)

    @property
    def UML_14_Attribute28(self):
        return self.__UML_14_Attribute28

    @UML_14_Attribute28.setter
    def UML_14_Attribute28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_Attribute__UML_14_Attribute28", None)
        self.__UML_14_Attribute28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML_14_Class27"):
                opp_val = getattr(old_value, "UML_14_Class27", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML_14_Class27"):
                opp_val = getattr(value, "UML_14_Class27", None)
                if opp_val is None:
                    setattr(value, "UML_14_Class27", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML_14_Attribute11(self):
        return self.__UML_14_Attribute11

    @UML_14_Attribute11.setter
    def UML_14_Attribute11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_Attribute__UML_14_Attribute11", None)
        self.__UML_14_Attribute11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML_14_Primitive"):
                opp_val = getattr(old_value, "UML_14_Primitive", None)
                if opp_val == self:
                    setattr(old_value, "UML_14_Primitive", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML_14_Primitive"):
                opp_val = getattr(value, "UML_14_Primitive", None)
                setattr(value, "UML_14_Primitive", self)

class UML_14_Primitive(NamedElement):

    pass
class UML_14_Package(NamedElement):

    pass
class UML_14_Association(NamedElement):

    pass
class UML_14_Enumeration(NamedElement):

    pass
class UML_14_Parameter(NamedElement):

    def __init__(self, kind: str, defaultValue: str, UML_14_Parameter: "UML_14_Enumeration" = None, UML_14_Parameter2: "UML_14_Enumeration" = None, UML_14_Parameter5: "UML_14_Method" = None):
        self.kind = kind
        self.defaultValue = defaultValue
        self.UML_14_Parameter = UML_14_Parameter
        self.UML_14_Parameter2 = UML_14_Parameter2
        self.UML_14_Parameter5 = UML_14_Parameter5
        
    @property
    def defaultValue(self) -> str:
        return self.__defaultValue

    @defaultValue.setter
    def defaultValue(self, defaultValue: str):
        self.__defaultValue = defaultValue

    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

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
            if hasattr(old_value, "UML_14_Enumeration"):
                opp_val = getattr(old_value, "UML_14_Enumeration", None)
                if opp_val == self:
                    setattr(old_value, "UML_14_Enumeration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML_14_Enumeration"):
                opp_val = getattr(value, "UML_14_Enumeration", None)
                setattr(value, "UML_14_Enumeration", self)

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
            if hasattr(old_value, "UML_14_Enumeration3"):
                opp_val = getattr(old_value, "UML_14_Enumeration3", None)
                if opp_val == self:
                    setattr(old_value, "UML_14_Enumeration3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML_14_Enumeration3"):
                opp_val = getattr(value, "UML_14_Enumeration3", None)
                setattr(value, "UML_14_Enumeration3", self)

    @property
    def UML_14_Parameter5(self):
        return self.__UML_14_Parameter5

    @UML_14_Parameter5.setter
    def UML_14_Parameter5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_Parameter__UML_14_Parameter5", None)
        self.__UML_14_Parameter5 = value
        
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
