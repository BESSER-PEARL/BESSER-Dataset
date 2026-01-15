from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Operation:

    pass
class umlClass_AlternativeOperation(Operation):

    pass
class umlClass_OptionalOperation(Operation):

    pass
class umlClass_Element(ABC):

    pass
class DirectedRelationship:

    pass
class Relationship:

    pass
class umlClass_DirectedRelationship(Relationship):

    pass
class Classifier:

    pass
class umlClass_Class(Classifier):

    def __init__(self, isActive: str, class: set["umlClass_Operation"] = None, class7: set["umlClass_Property"] = None, umlClass_Class: "umlClass_Class" = None, umlClass_Class9: set["umlClass_Class"] = None, umlClass_Class12: "umlClass_Association" = None, umlClass_Class14: set["umlClass_Classifier"] = None, Class: "umlClass_Property" = None, umlClass_Class40: "umlClass_Association" = None, Class42: "umlClass_Operation" = None, umlClass_Class56: "umlClass_Generalization" = None, umlClass_Class59: "umlClass_Generalization" = None):
        self.isActive = isActive
        self.class = class if class is not None else set()
        self.class7 = class7 if class7 is not None else set()
        self.umlClass_Class = umlClass_Class
        self.umlClass_Class9 = umlClass_Class9 if umlClass_Class9 is not None else set()
        self.umlClass_Class12 = umlClass_Class12
        self.umlClass_Class14 = umlClass_Class14 if umlClass_Class14 is not None else set()
        self.Class = Class
        self.umlClass_Class40 = umlClass_Class40
        self.Class42 = Class42
        self.umlClass_Class56 = umlClass_Class56
        self.umlClass_Class59 = umlClass_Class59
        
    @property
    def isActive(self) -> str:
        return self.__isActive

    @isActive.setter
    def isActive(self, isActive: str):
        self.__isActive = isActive

    @property
    def umlClass_Class9(self):
        return self.__umlClass_Class9

    @umlClass_Class9.setter
    def umlClass_Class9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlClass_Class__umlClass_Class9", None)
        self.__umlClass_Class9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "umlClass_Class"):
                    opp_val = getattr(item, "umlClass_Class", None)
                    
                    if opp_val == self:
                        setattr(item, "umlClass_Class", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "umlClass_Class"):
                    opp_val = getattr(item, "umlClass_Class", None)
                    
                    setattr(item, "umlClass_Class", self)
                    

    @property
    def Class(self):
        return self.__Class

    @Class.setter
    def Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlClass_Class__Class", None)
        self.__Class = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ownedAttribute"):
                opp_val = getattr(old_value, "ownedAttribute", None)
                if opp_val == self:
                    setattr(old_value, "ownedAttribute", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownedAttribute"):
                opp_val = getattr(value, "ownedAttribute", None)
                setattr(value, "ownedAttribute", self)

    @property
    def umlClass_Class40(self):
        return self.__umlClass_Class40

    @umlClass_Class40.setter
    def umlClass_Class40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlClass_Class__umlClass_Class40", None)
        self.__umlClass_Class40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umlClass_Association39"):
                opp_val = getattr(old_value, "umlClass_Association39", None)
                if opp_val == self:
                    setattr(old_value, "umlClass_Association39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umlClass_Association39"):
                opp_val = getattr(value, "umlClass_Association39", None)
                setattr(value, "umlClass_Association39", self)

    @property
    def umlClass_Class59(self):
        return self.__umlClass_Class59

    @umlClass_Class59.setter
    def umlClass_Class59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlClass_Class__umlClass_Class59", None)
        self.__umlClass_Class59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umlClass_Generalization58"):
                opp_val = getattr(old_value, "umlClass_Generalization58", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umlClass_Generalization58"):
                opp_val = getattr(value, "umlClass_Generalization58", None)
                if opp_val is None:
                    setattr(value, "umlClass_Generalization58", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def umlClass_Class56(self):
        return self.__umlClass_Class56

    @umlClass_Class56.setter
    def umlClass_Class56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlClass_Class__umlClass_Class56", None)
        self.__umlClass_Class56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umlClass_Generalization"):
                opp_val = getattr(old_value, "umlClass_Generalization", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umlClass_Generalization"):
                opp_val = getattr(value, "umlClass_Generalization", None)
                if opp_val is None:
                    setattr(value, "umlClass_Generalization", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def umlClass_Class12(self):
        return self.__umlClass_Class12

    @umlClass_Class12.setter
    def umlClass_Class12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlClass_Class__umlClass_Class12", None)
        self.__umlClass_Class12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umlClass_Association"):
                opp_val = getattr(old_value, "umlClass_Association", None)
                if opp_val == self:
                    setattr(old_value, "umlClass_Association", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umlClass_Association"):
                opp_val = getattr(value, "umlClass_Association", None)
                setattr(value, "umlClass_Association", self)

    @property
    def class(self):
        return self.__class

    @class.setter
    def class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlClass_Class__class", None)
        self.__class = value if value is not None else set()
        
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
                    

    @property
    def class7(self):
        return self.__class7

    @class7.setter
    def class7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlClass_Class__class7", None)
        self.__class7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Property8"):
                    opp_val = getattr(item, "Property8", None)
                    
                    if opp_val == self:
                        setattr(item, "Property8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Property8"):
                    opp_val = getattr(item, "Property8", None)
                    
                    setattr(item, "Property8", self)
                    

    @property
    def Class42(self):
        return self.__Class42

    @Class42.setter
    def Class42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlClass_Class__Class42", None)
        self.__Class42 = value
        
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
    def umlClass_Class14(self):
        return self.__umlClass_Class14

    @umlClass_Class14.setter
    def umlClass_Class14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlClass_Class__umlClass_Class14", None)
        self.__umlClass_Class14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "umlClass_Classifier15"):
                    opp_val = getattr(item, "umlClass_Classifier15", None)
                    
                    if opp_val == self:
                        setattr(item, "umlClass_Classifier15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "umlClass_Classifier15"):
                    opp_val = getattr(item, "umlClass_Classifier15", None)
                    
                    setattr(item, "umlClass_Classifier15", self)
                    

    @property
    def umlClass_Class(self):
        return self.__umlClass_Class

    @umlClass_Class.setter
    def umlClass_Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlClass_Class__umlClass_Class", None)
        self.__umlClass_Class = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umlClass_Class9"):
                opp_val = getattr(old_value, "umlClass_Class9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umlClass_Class9"):
                opp_val = getattr(value, "umlClass_Class9", None)
                if opp_val is None:
                    setattr(value, "umlClass_Class9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class TypedElement:

    pass
class umlClass_StructuralFeature(TypedElement):

    def __init__(self, isReadOnly: str):
        self.isReadOnly = isReadOnly
        
    @property
    def isReadOnly(self) -> str:
        return self.__isReadOnly

    @isReadOnly.setter
    def isReadOnly(self, isReadOnly: str):
        self.__isReadOnly = isReadOnly

class umlClass_Generalization(DirectedRelationship):

    pass
class NamedElement:

    pass
class umlClass_TypedElement(NamedElement):

    pass
class umlClass_Package(NamedElement):

    pass
class umlClass_Classifier(NamedElement):

    pass
class Element:

    pass
class umlClass_Relationship(Element):

    pass
class umlClass_NamedElement(Element):

    def __init__(self, name: str, Archpoint: str):
        self.name = name
        self.Archpoint = Archpoint
        
    @property
    def Archpoint(self) -> str:
        return self.__Archpoint

    @Archpoint.setter
    def Archpoint(self, Archpoint: str):
        self.__Archpoint = Archpoint

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class umlClass_DataType(Classifier):

    pass
class StructuralFeature:

    pass
class umlClass_Property(StructuralFeature):

    pass
class umlClass_Association(Classifier, Relationship):

    pass
class umlClass_Operation(NamedElement):

    def __init__(self, isQuery: str, isOrdered: str, isUnique: str, lower: str, upper: str, Operation: "umlClass_Class" = None, Operation50: "umlClass_DataType" = None, ownedOperation: "umlClass_Class" = None, ownedOperation44: "umlClass_DataType" = None, umlClass_Operation: "umlClass_AlternativeOperation" = None):
        self.isQuery = isQuery
        self.isOrdered = isOrdered
        self.isUnique = isUnique
        self.lower = lower
        self.upper = upper
        self.Operation = Operation
        self.Operation50 = Operation50
        self.ownedOperation = ownedOperation
        self.ownedOperation44 = ownedOperation44
        self.umlClass_Operation = umlClass_Operation
        
    @property
    def isOrdered(self) -> str:
        return self.__isOrdered

    @isOrdered.setter
    def isOrdered(self, isOrdered: str):
        self.__isOrdered = isOrdered

    @property
    def lower(self) -> str:
        return self.__lower

    @lower.setter
    def lower(self, lower: str):
        self.__lower = lower

    @property
    def isQuery(self) -> str:
        return self.__isQuery

    @isQuery.setter
    def isQuery(self, isQuery: str):
        self.__isQuery = isQuery

    @property
    def upper(self) -> str:
        return self.__upper

    @upper.setter
    def upper(self, upper: str):
        self.__upper = upper

    @property
    def isUnique(self) -> str:
        return self.__isUnique

    @isUnique.setter
    def isUnique(self, isUnique: str):
        self.__isUnique = isUnique

    @property
    def ownedOperation(self):
        return self.__ownedOperation

    @ownedOperation.setter
    def ownedOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlClass_Operation__ownedOperation", None)
        self.__ownedOperation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Class42"):
                opp_val = getattr(old_value, "Class42", None)
                if opp_val == self:
                    setattr(old_value, "Class42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Class42"):
                opp_val = getattr(value, "Class42", None)
                setattr(value, "Class42", self)

    @property
    def Operation(self):
        return self.__Operation

    @Operation.setter
    def Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlClass_Operation__Operation", None)
        self.__Operation = value
        
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
    def umlClass_Operation(self):
        return self.__umlClass_Operation

    @umlClass_Operation.setter
    def umlClass_Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlClass_Operation__umlClass_Operation", None)
        self.__umlClass_Operation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umlClass_AlternativeOperation"):
                opp_val = getattr(old_value, "umlClass_AlternativeOperation", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umlClass_AlternativeOperation"):
                opp_val = getattr(value, "umlClass_AlternativeOperation", None)
                if opp_val is None:
                    setattr(value, "umlClass_AlternativeOperation", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Operation50(self):
        return self.__Operation50

    @Operation50.setter
    def Operation50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlClass_Operation__Operation50", None)
        self.__Operation50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "datatype49"):
                opp_val = getattr(old_value, "datatype49", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "datatype49"):
                opp_val = getattr(value, "datatype49", None)
                if opp_val is None:
                    setattr(value, "datatype49", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ownedOperation44(self):
        return self.__ownedOperation44

    @ownedOperation44.setter
    def ownedOperation44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlClass_Operation__ownedOperation44", None)
        self.__ownedOperation44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DataType45"):
                opp_val = getattr(old_value, "DataType45", None)
                if opp_val == self:
                    setattr(old_value, "DataType45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DataType45"):
                opp_val = getattr(value, "DataType45", None)
                setattr(value, "DataType45", self)
