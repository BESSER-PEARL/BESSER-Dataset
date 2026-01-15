from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class model_Part:

    def __init__(self, name: str, model_Part: "model_Type" = None):
        self.name = name
        self.model_Part = model_Part
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def model_Part(self):
        return self.__model_Part

    @model_Part.setter
    def model_Part(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Part__model_Part", None)
        self.__model_Part = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Type76"):
                opp_val = getattr(old_value, "model_Type76", None)
                if opp_val == self:
                    setattr(old_value, "model_Type76", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Type76"):
                opp_val = getattr(value, "model_Type76", None)
                setattr(value, "model_Type76", self)

class model_Expression:

    pass
class model_VarDeclList:

    pass
class MAssociation:

    pass
class MClass:

    pass
class model_MAssociationClass(MClass, MAssociation):

    def __init__(self):
        
    def processWithVisitor(self, v: str):
        # TODO: Implement processWithVisitor method
        pass

class model_MRange:

    def __init__(self, lower: int, upper: int, model_MRange: "model_MMultiplicity" = None):
        self.lower = lower
        self.upper = upper
        self.model_MRange = model_MRange
        
    @property
    def upper(self) -> int:
        return self.__upper

    @upper.setter
    def upper(self, upper: int):
        self.__upper = upper

    @property
    def lower(self) -> int:
        return self.__lower

    @lower.setter
    def lower(self, lower: int):
        self.__lower = lower

    @property
    def model_MRange(self):
        return self.__model_MRange

    @model_MRange.setter
    def model_MRange(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_MRange__model_MRange", None)
        self.__model_MRange = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_MMultiplicity53"):
                opp_val = getattr(old_value, "model_MMultiplicity53", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_MMultiplicity53"):
                opp_val = getattr(value, "model_MMultiplicity53", None)
                if opp_val is None:
                    setattr(value, "model_MMultiplicity53", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class model_MMultiplicity:

    def __init__(self, model_MMultiplicity: "model_MAssociationEnd" = None, model_MMultiplicity53: set["model_MRange"] = None):
        self.model_MMultiplicity = model_MMultiplicity
        self.model_MMultiplicity53 = model_MMultiplicity53 if model_MMultiplicity53 is not None else set()
        
    @property
    def model_MMultiplicity(self):
        return self.__model_MMultiplicity

    @model_MMultiplicity.setter
    def model_MMultiplicity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_MMultiplicity__model_MMultiplicity", None)
        self.__model_MMultiplicity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_MAssociationEnd48"):
                opp_val = getattr(old_value, "model_MAssociationEnd48", None)
                if opp_val == self:
                    setattr(old_value, "model_MAssociationEnd48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_MAssociationEnd48"):
                opp_val = getattr(value, "model_MAssociationEnd48", None)
                setattr(value, "model_MAssociationEnd48", self)

    @property
    def model_MMultiplicity53(self):
        return self.__model_MMultiplicity53

    @model_MMultiplicity53.setter
    def model_MMultiplicity53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_MMultiplicity__model_MMultiplicity53", None)
        self.__model_MMultiplicity53 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_MRange"):
                    opp_val = getattr(item, "model_MRange", None)
                    
                    if opp_val == self:
                        setattr(item, "model_MRange", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_MRange"):
                    opp_val = getattr(item, "model_MRange", None)
                    
                    setattr(item, "model_MRange", self)
                    

    def addRange(self, r: str):
        # TODO: Implement addRange method
        pass

class model_MAggregationKind:

    def __init__(self, name: str, kind: int, model_MAggregationKind: "model_MAssociation" = None, model_MAggregationKind51: "model_MAssociationEnd" = None):
        self.name = name
        self.kind = kind
        self.model_MAggregationKind = model_MAggregationKind
        self.model_MAggregationKind51 = model_MAggregationKind51
        
    @property
    def kind(self) -> int:
        return self.__kind

    @kind.setter
    def kind(self, kind: int):
        self.__kind = kind

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def model_MAggregationKind51(self):
        return self.__model_MAggregationKind51

    @model_MAggregationKind51.setter
    def model_MAggregationKind51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_MAggregationKind__model_MAggregationKind51", None)
        self.__model_MAggregationKind51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_MAssociationEnd50"):
                opp_val = getattr(old_value, "model_MAssociationEnd50", None)
                if opp_val == self:
                    setattr(old_value, "model_MAssociationEnd50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_MAssociationEnd50"):
                opp_val = getattr(value, "model_MAssociationEnd50", None)
                setattr(value, "model_MAssociationEnd50", self)

    @property
    def model_MAggregationKind(self):
        return self.__model_MAggregationKind

    @model_MAggregationKind.setter
    def model_MAggregationKind(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_MAggregationKind__model_MAggregationKind", None)
        self.__model_MAggregationKind = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_MAssociation40"):
                opp_val = getattr(old_value, "model_MAssociation40", None)
                if opp_val == self:
                    setattr(old_value, "model_MAssociation40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_MAssociation40"):
                opp_val = getattr(value, "model_MAssociation40", None)
                setattr(value, "model_MAssociation40", self)

class model_MNavigableElement:

    def __init__(self, nameAsRolename: str, model_MNavigableElement: "model_MClass" = None, model_MNavigableElement57: "model_MAssociation" = None):
        self.nameAsRolename = nameAsRolename
        self.model_MNavigableElement = model_MNavigableElement
        self.model_MNavigableElement57 = model_MNavigableElement57
        
    @property
    def nameAsRolename(self) -> str:
        return self.__nameAsRolename

    @nameAsRolename.setter
    def nameAsRolename(self, nameAsRolename: str):
        self.__nameAsRolename = nameAsRolename

    @property
    def model_MNavigableElement(self):
        return self.__model_MNavigableElement

    @model_MNavigableElement.setter
    def model_MNavigableElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_MNavigableElement__model_MNavigableElement", None)
        self.__model_MNavigableElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_MClass55"):
                opp_val = getattr(old_value, "model_MClass55", None)
                if opp_val == self:
                    setattr(old_value, "model_MClass55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_MClass55"):
                opp_val = getattr(value, "model_MClass55", None)
                setattr(value, "model_MClass55", self)

    @property
    def model_MNavigableElement57(self):
        return self.__model_MNavigableElement57

    @model_MNavigableElement57.setter
    def model_MNavigableElement57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_MNavigableElement__model_MNavigableElement57", None)
        self.__model_MNavigableElement57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_MAssociation58"):
                opp_val = getattr(old_value, "model_MAssociation58", None)
                if opp_val == self:
                    setattr(old_value, "model_MAssociation58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_MAssociation58"):
                opp_val = getattr(value, "model_MAssociation58", None)
                setattr(value, "model_MAssociation58", self)

    def getType(self, src: str) -> Type:
        # TODO: Implement getType method
        pass

class CollectionType:

    pass
class model_OrderedSetType(CollectionType):

    pass
class model_BagType(CollectionType):

    pass
class model_SetType(CollectionType):

    pass
class model_Comparable(ABC):

    pass
class model_VarDecl:

    def __init__(self, var: str, model_VarDecl: "model_MOperation" = None, model_VarDecl31: "model_Type" = None):
        self.var = var
        self.model_VarDecl = model_VarDecl
        self.model_VarDecl31 = model_VarDecl31
        
    @property
    def var(self) -> str:
        return self.__var

    @var.setter
    def var(self, var: str):
        self.__var = var

    @property
    def model_VarDecl31(self):
        return self.__model_VarDecl31

    @model_VarDecl31.setter
    def model_VarDecl31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_VarDecl__model_VarDecl31", None)
        self.__model_VarDecl31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Type32"):
                opp_val = getattr(old_value, "model_Type32", None)
                if opp_val == self:
                    setattr(old_value, "model_Type32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Type32"):
                opp_val = getattr(value, "model_Type32", None)
                setattr(value, "model_Type32", self)

    @property
    def model_VarDecl(self):
        return self.__model_VarDecl

    @model_VarDecl.setter
    def model_VarDecl(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_VarDecl__model_VarDecl", None)
        self.__model_VarDecl = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_MOperation29"):
                opp_val = getattr(old_value, "model_MOperation29", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_MOperation29"):
                opp_val = getattr(value, "model_MOperation29", None)
                if opp_val is None:
                    setattr(value, "model_MOperation29", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class model_SequenceType(CollectionType):

    pass
class model_MMVisitor:

    pass
class MModelElement:

    pass
class model_MClassInvariant(MModelElement):

    def __init__(self, positionInModel: int, name: str, model_MClassInvariant: "model_MModel" = None, model_MClassInvariant60: "model_VarDeclList" = None, model_MClassInvariant62: "model_MClass" = None, model_MClassInvariant65: "model_Expression" = None, model_MClassInvariant67: "model_Expression" = None):
        self.positionInModel = positionInModel
        self.name = name
        self.model_MClassInvariant = model_MClassInvariant
        self.model_MClassInvariant60 = model_MClassInvariant60
        self.model_MClassInvariant62 = model_MClassInvariant62
        self.model_MClassInvariant65 = model_MClassInvariant65
        self.model_MClassInvariant67 = model_MClassInvariant67
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def positionInModel(self) -> int:
        return self.__positionInModel

    @positionInModel.setter
    def positionInModel(self, positionInModel: int):
        self.__positionInModel = positionInModel

    @property
    def model_MClassInvariant60(self):
        return self.__model_MClassInvariant60

    @model_MClassInvariant60.setter
    def model_MClassInvariant60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_MClassInvariant__model_MClassInvariant60", None)
        self.__model_MClassInvariant60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_VarDeclList"):
                opp_val = getattr(old_value, "model_VarDeclList", None)
                if opp_val == self:
                    setattr(old_value, "model_VarDeclList", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_VarDeclList"):
                opp_val = getattr(value, "model_VarDeclList", None)
                setattr(value, "model_VarDeclList", self)

    @property
    def model_MClassInvariant67(self):
        return self.__model_MClassInvariant67

    @model_MClassInvariant67.setter
    def model_MClassInvariant67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_MClassInvariant__model_MClassInvariant67", None)
        self.__model_MClassInvariant67 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Expression68"):
                opp_val = getattr(old_value, "model_Expression68", None)
                if opp_val == self:
                    setattr(old_value, "model_Expression68", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Expression68"):
                opp_val = getattr(value, "model_Expression68", None)
                setattr(value, "model_Expression68", self)

    @property
    def model_MClassInvariant65(self):
        return self.__model_MClassInvariant65

    @model_MClassInvariant65.setter
    def model_MClassInvariant65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_MClassInvariant__model_MClassInvariant65", None)
        self.__model_MClassInvariant65 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Expression"):
                opp_val = getattr(old_value, "model_Expression", None)
                if opp_val == self:
                    setattr(old_value, "model_Expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Expression"):
                opp_val = getattr(value, "model_Expression", None)
                setattr(value, "model_Expression", self)

    @property
    def model_MClassInvariant(self):
        return self.__model_MClassInvariant

    @model_MClassInvariant.setter
    def model_MClassInvariant(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_MClassInvariant__model_MClassInvariant", None)
        self.__model_MClassInvariant = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_MModel19"):
                opp_val = getattr(old_value, "model_MModel19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_MModel19"):
                opp_val = getattr(value, "model_MModel19", None)
                if opp_val is None:
                    setattr(value, "model_MModel19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_MClassInvariant62(self):
        return self.__model_MClassInvariant62

    @model_MClassInvariant62.setter
    def model_MClassInvariant62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_MClassInvariant__model_MClassInvariant62", None)
        self.__model_MClassInvariant62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_MClass63"):
                opp_val = getattr(old_value, "model_MClass63", None)
                if opp_val == self:
                    setattr(old_value, "model_MClass63", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_MClass63"):
                opp_val = getattr(value, "model_MClass63", None)
                setattr(value, "model_MClass63", self)

    def getIsExistential(self) -> bool:
        # TODO: Implement getIsExistential method
        pass

    def getHasVars(self) -> bool:
        # TODO: Implement getHasVars method
        pass

class model_MModelElementEx(MModelElement):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    def processWithVisitor(self, v: str):
        # TODO: Implement processWithVisitor method
        pass

class model_MModelElement:

    def __init__(self):
        
    def name(self) -> str:
        # TODO: Implement name method
        pass

    def processWithVisitor(self, v: str):
        # TODO: Implement processWithVisitor method
        pass

class model_MPrePostCondition(MModelElement):

    def __init__(self, positionInModel: int, model_MPrePostCondition: "model_MModel" = None, model_MPrePostCondition70: "model_MOperation" = None, model_MPrePostCondition73: "model_Expression" = None):
        self.positionInModel = positionInModel
        self.model_MPrePostCondition = model_MPrePostCondition
        self.model_MPrePostCondition70 = model_MPrePostCondition70
        self.model_MPrePostCondition73 = model_MPrePostCondition73
        
    @property
    def positionInModel(self) -> int:
        return self.__positionInModel

    @positionInModel.setter
    def positionInModel(self, positionInModel: int):
        self.__positionInModel = positionInModel

    @property
    def model_MPrePostCondition73(self):
        return self.__model_MPrePostCondition73

    @model_MPrePostCondition73.setter
    def model_MPrePostCondition73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_MPrePostCondition__model_MPrePostCondition73", None)
        self.__model_MPrePostCondition73 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Expression74"):
                opp_val = getattr(old_value, "model_Expression74", None)
                if opp_val == self:
                    setattr(old_value, "model_Expression74", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Expression74"):
                opp_val = getattr(value, "model_Expression74", None)
                setattr(value, "model_Expression74", self)

    @property
    def model_MPrePostCondition(self):
        return self.__model_MPrePostCondition

    @model_MPrePostCondition.setter
    def model_MPrePostCondition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_MPrePostCondition__model_MPrePostCondition", None)
        self.__model_MPrePostCondition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_MModel21"):
                opp_val = getattr(old_value, "model_MModel21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_MModel21"):
                opp_val = getattr(value, "model_MModel21", None)
                if opp_val is None:
                    setattr(value, "model_MModel21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_MPrePostCondition70(self):
        return self.__model_MPrePostCondition70

    @model_MPrePostCondition70.setter
    def model_MPrePostCondition70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_MPrePostCondition__model_MPrePostCondition70", None)
        self.__model_MPrePostCondition70 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_MOperation71"):
                opp_val = getattr(old_value, "model_MOperation71", None)
                if opp_val == self:
                    setattr(old_value, "model_MOperation71", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_MOperation71"):
                opp_val = getattr(value, "model_MOperation71", None)
                setattr(value, "model_MOperation71", self)

    def setPre(self, b: bool):
        # TODO: Implement setPre method
        pass

    def getIsPre(self) -> bool:
        # TODO: Implement getIsPre method
        pass

class MModelElementEx:

    pass
class model_MOperation(MModelElementEx):

    def __init__(self, model_MOperation: "model_MClass" = None, model_MOperation23: "model_MClass" = None, model_MOperation26: "model_Type" = None, model_MOperation29: set["model_VarDecl"] = None, model_MOperation71: "model_MPrePostCondition" = None):
        self.model_MOperation = model_MOperation
        self.model_MOperation23 = model_MOperation23
        self.model_MOperation26 = model_MOperation26
        self.model_MOperation29 = model_MOperation29 if model_MOperation29 is not None else set()
        self.model_MOperation71 = model_MOperation71
        
    @property
    def model_MOperation26(self):
        return self.__model_MOperation26

    @model_MOperation26.setter
    def model_MOperation26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_MOperation__model_MOperation26", None)
        self.__model_MOperation26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Type27"):
                opp_val = getattr(old_value, "model_Type27", None)
                if opp_val == self:
                    setattr(old_value, "model_Type27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Type27"):
                opp_val = getattr(value, "model_Type27", None)
                setattr(value, "model_Type27", self)

    @property
    def model_MOperation(self):
        return self.__model_MOperation

    @model_MOperation.setter
    def model_MOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_MOperation__model_MOperation", None)
        self.__model_MOperation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_MClass7"):
                opp_val = getattr(old_value, "model_MClass7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_MClass7"):
                opp_val = getattr(value, "model_MClass7", None)
                if opp_val is None:
                    setattr(value, "model_MClass7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_MOperation71(self):
        return self.__model_MOperation71

    @model_MOperation71.setter
    def model_MOperation71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_MOperation__model_MOperation71", None)
        self.__model_MOperation71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_MPrePostCondition70"):
                opp_val = getattr(old_value, "model_MPrePostCondition70", None)
                if opp_val == self:
                    setattr(old_value, "model_MPrePostCondition70", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_MPrePostCondition70"):
                opp_val = getattr(value, "model_MPrePostCondition70", None)
                setattr(value, "model_MPrePostCondition70", self)

    @property
    def model_MOperation23(self):
        return self.__model_MOperation23

    @model_MOperation23.setter
    def model_MOperation23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_MOperation__model_MOperation23", None)
        self.__model_MOperation23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_MClass24"):
                opp_val = getattr(old_value, "model_MClass24", None)
                if opp_val == self:
                    setattr(old_value, "model_MClass24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_MClass24"):
                opp_val = getattr(value, "model_MClass24", None)
                setattr(value, "model_MClass24", self)

    @property
    def model_MOperation29(self):
        return self.__model_MOperation29

    @model_MOperation29.setter
    def model_MOperation29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_MOperation__model_MOperation29", None)
        self.__model_MOperation29 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_VarDecl"):
                    opp_val = getattr(item, "model_VarDecl", None)
                    
                    if opp_val == self:
                        setattr(item, "model_VarDecl", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_VarDecl"):
                    opp_val = getattr(item, "model_VarDecl", None)
                    
                    setattr(item, "model_VarDecl", self)
                    

    def addVarDecl(self, vd: str):
        # TODO: Implement addVarDecl method
        pass

class model_MAssociation(MModelElementEx):

    def __init__(self, model_MAssociation: "model_MClass" = None, model_MAssociation58: "model_MNavigableElement" = None, model_MAssociation38: set["model_MAssociationEnd"] = None, model_MAssociation40: "model_MAggregationKind" = None, model_MAssociation43: "model_MAssociationEnd" = None):
        self.model_MAssociation = model_MAssociation
        self.model_MAssociation58 = model_MAssociation58
        self.model_MAssociation38 = model_MAssociation38 if model_MAssociation38 is not None else set()
        self.model_MAssociation40 = model_MAssociation40
        self.model_MAssociation43 = model_MAssociation43
        
    @property
    def model_MAssociation58(self):
        return self.__model_MAssociation58

    @model_MAssociation58.setter
    def model_MAssociation58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_MAssociation__model_MAssociation58", None)
        self.__model_MAssociation58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_MNavigableElement57"):
                opp_val = getattr(old_value, "model_MNavigableElement57", None)
                if opp_val == self:
                    setattr(old_value, "model_MNavigableElement57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_MNavigableElement57"):
                opp_val = getattr(value, "model_MNavigableElement57", None)
                setattr(value, "model_MNavigableElement57", self)

    @property
    def model_MAssociation38(self):
        return self.__model_MAssociation38

    @model_MAssociation38.setter
    def model_MAssociation38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_MAssociation__model_MAssociation38", None)
        self.__model_MAssociation38 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_MAssociationEnd"):
                    opp_val = getattr(item, "model_MAssociationEnd", None)
                    
                    if opp_val == self:
                        setattr(item, "model_MAssociationEnd", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_MAssociationEnd"):
                    opp_val = getattr(item, "model_MAssociationEnd", None)
                    
                    setattr(item, "model_MAssociationEnd", self)
                    

    @property
    def model_MAssociation40(self):
        return self.__model_MAssociation40

    @model_MAssociation40.setter
    def model_MAssociation40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_MAssociation__model_MAssociation40", None)
        self.__model_MAssociation40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_MAggregationKind"):
                opp_val = getattr(old_value, "model_MAggregationKind", None)
                if opp_val == self:
                    setattr(old_value, "model_MAggregationKind", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_MAggregationKind"):
                opp_val = getattr(value, "model_MAggregationKind", None)
                setattr(value, "model_MAggregationKind", self)

    @property
    def model_MAssociation(self):
        return self.__model_MAssociation

    @model_MAssociation.setter
    def model_MAssociation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_MAssociation__model_MAssociation", None)
        self.__model_MAssociation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_MClass9"):
                opp_val = getattr(old_value, "model_MClass9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_MClass9"):
                opp_val = getattr(value, "model_MClass9", None)
                if opp_val is None:
                    setattr(value, "model_MClass9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_MAssociation43(self):
        return self.__model_MAssociation43

    @model_MAssociation43.setter
    def model_MAssociation43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_MAssociation__model_MAssociation43", None)
        self.__model_MAssociation43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_MAssociationEnd42"):
                opp_val = getattr(old_value, "model_MAssociationEnd42", None)
                if opp_val == self:
                    setattr(old_value, "model_MAssociationEnd42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_MAssociationEnd42"):
                opp_val = getattr(value, "model_MAssociationEnd42", None)
                setattr(value, "model_MAssociationEnd42", self)

    def processWithVisitor(self, v: str):
        # TODO: Implement processWithVisitor method
        pass

    def addAssociationEnd(self, ae: str):
        # TODO: Implement addAssociationEnd method
        pass

class model_MAssociationEnd(MModelElementEx):

    def __init__(self, mClassName: str, model_MAssociationEnd: "model_MAssociation" = None, model_MAssociationEnd42: "model_MAssociation" = None, model_MAssociationEnd45: "model_MClass" = None, model_MAssociationEnd48: "model_MMultiplicity" = None, model_MAssociationEnd50: "model_MAggregationKind" = None):
        self.mClassName = mClassName
        self.model_MAssociationEnd = model_MAssociationEnd
        self.model_MAssociationEnd42 = model_MAssociationEnd42
        self.model_MAssociationEnd45 = model_MAssociationEnd45
        self.model_MAssociationEnd48 = model_MAssociationEnd48
        self.model_MAssociationEnd50 = model_MAssociationEnd50
        
    @property
    def mClassName(self) -> str:
        return self.__mClassName

    @mClassName.setter
    def mClassName(self, mClassName: str):
        self.__mClassName = mClassName

    @property
    def model_MAssociationEnd48(self):
        return self.__model_MAssociationEnd48

    @model_MAssociationEnd48.setter
    def model_MAssociationEnd48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_MAssociationEnd__model_MAssociationEnd48", None)
        self.__model_MAssociationEnd48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_MMultiplicity"):
                opp_val = getattr(old_value, "model_MMultiplicity", None)
                if opp_val == self:
                    setattr(old_value, "model_MMultiplicity", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_MMultiplicity"):
                opp_val = getattr(value, "model_MMultiplicity", None)
                setattr(value, "model_MMultiplicity", self)

    @property
    def model_MAssociationEnd42(self):
        return self.__model_MAssociationEnd42

    @model_MAssociationEnd42.setter
    def model_MAssociationEnd42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_MAssociationEnd__model_MAssociationEnd42", None)
        self.__model_MAssociationEnd42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_MAssociation43"):
                opp_val = getattr(old_value, "model_MAssociation43", None)
                if opp_val == self:
                    setattr(old_value, "model_MAssociation43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_MAssociation43"):
                opp_val = getattr(value, "model_MAssociation43", None)
                setattr(value, "model_MAssociation43", self)

    @property
    def model_MAssociationEnd(self):
        return self.__model_MAssociationEnd

    @model_MAssociationEnd.setter
    def model_MAssociationEnd(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_MAssociationEnd__model_MAssociationEnd", None)
        self.__model_MAssociationEnd = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_MAssociation38"):
                opp_val = getattr(old_value, "model_MAssociation38", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_MAssociation38"):
                opp_val = getattr(value, "model_MAssociation38", None)
                if opp_val is None:
                    setattr(value, "model_MAssociation38", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_MAssociationEnd50(self):
        return self.__model_MAssociationEnd50

    @model_MAssociationEnd50.setter
    def model_MAssociationEnd50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_MAssociationEnd__model_MAssociationEnd50", None)
        self.__model_MAssociationEnd50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_MAggregationKind51"):
                opp_val = getattr(old_value, "model_MAggregationKind51", None)
                if opp_val == self:
                    setattr(old_value, "model_MAggregationKind51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_MAggregationKind51"):
                opp_val = getattr(value, "model_MAggregationKind51", None)
                setattr(value, "model_MAggregationKind51", self)

    @property
    def model_MAssociationEnd45(self):
        return self.__model_MAssociationEnd45

    @model_MAssociationEnd45.setter
    def model_MAssociationEnd45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_MAssociationEnd__model_MAssociationEnd45", None)
        self.__model_MAssociationEnd45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_MClass46"):
                opp_val = getattr(old_value, "model_MClass46", None)
                if opp_val == self:
                    setattr(old_value, "model_MClass46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_MClass46"):
                opp_val = getattr(value, "model_MClass46", None)
                setattr(value, "model_MClass46", self)

    def getOrdered(self) -> bool:
        # TODO: Implement getOrdered method
        pass

    def getNavigation(self) -> bool:
        # TODO: Implement getNavigation method
        pass

    def getExplicitNavigation(self) -> bool:
        # TODO: Implement getExplicitNavigation method
        pass

class model_MModel(MModelElementEx):

    def __init__(self, model_MModel21: set["model_MPrePostCondition"] = None, model_MModel: set["model_MClass"] = None, model_MModel19: set["model_MClassInvariant"] = None):
        self.model_MModel21 = model_MModel21 if model_MModel21 is not None else set()
        self.model_MModel = model_MModel if model_MModel is not None else set()
        self.model_MModel19 = model_MModel19 if model_MModel19 is not None else set()
        
    @property
    def model_MModel19(self):
        return self.__model_MModel19

    @model_MModel19.setter
    def model_MModel19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_MModel__model_MModel19", None)
        self.__model_MModel19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_MClassInvariant"):
                    opp_val = getattr(item, "model_MClassInvariant", None)
                    
                    if opp_val == self:
                        setattr(item, "model_MClassInvariant", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_MClassInvariant"):
                    opp_val = getattr(item, "model_MClassInvariant", None)
                    
                    setattr(item, "model_MClassInvariant", self)
                    

    @property
    def model_MModel21(self):
        return self.__model_MModel21

    @model_MModel21.setter
    def model_MModel21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_MModel__model_MModel21", None)
        self.__model_MModel21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_MPrePostCondition"):
                    opp_val = getattr(item, "model_MPrePostCondition", None)
                    
                    if opp_val == self:
                        setattr(item, "model_MPrePostCondition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_MPrePostCondition"):
                    opp_val = getattr(item, "model_MPrePostCondition", None)
                    
                    setattr(item, "model_MPrePostCondition", self)
                    

    @property
    def model_MModel(self):
        return self.__model_MModel

    @model_MModel.setter
    def model_MModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_MModel__model_MModel", None)
        self.__model_MModel = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_MClass17"):
                    opp_val = getattr(item, "model_MClass17", None)
                    
                    if opp_val == self:
                        setattr(item, "model_MClass17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_MClass17"):
                    opp_val = getattr(item, "model_MClass17", None)
                    
                    setattr(item, "model_MClass17", self)
                    

    def addPrePostCondition(self, ppc: str):
        # TODO: Implement addPrePostCondition method
        pass

    def addClass(self, cls: str):
        # TODO: Implement addClass method
        pass

    def processWithVisitor(self, v: str):
        # TODO: Implement processWithVisitor method
        pass

    def addClassInvariant(self, inv: str):
        # TODO: Implement addClassInvariant method
        pass

class model_MAttribute(MModelElementEx):

    def __init__(self, model_MAttribute: "model_MClass" = None, model_MAttribute2: "model_Type" = None, model_MAttribute5: "model_MClass" = None):
        self.model_MAttribute = model_MAttribute
        self.model_MAttribute2 = model_MAttribute2
        self.model_MAttribute5 = model_MAttribute5
        
    @property
    def model_MAttribute(self):
        return self.__model_MAttribute

    @model_MAttribute.setter
    def model_MAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_MAttribute__model_MAttribute", None)
        self.__model_MAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_MClass"):
                opp_val = getattr(old_value, "model_MClass", None)
                if opp_val == self:
                    setattr(old_value, "model_MClass", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_MClass"):
                opp_val = getattr(value, "model_MClass", None)
                setattr(value, "model_MClass", self)

    @property
    def model_MAttribute5(self):
        return self.__model_MAttribute5

    @model_MAttribute5.setter
    def model_MAttribute5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_MAttribute__model_MAttribute5", None)
        self.__model_MAttribute5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_MClass4"):
                opp_val = getattr(old_value, "model_MClass4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_MClass4"):
                opp_val = getattr(value, "model_MClass4", None)
                if opp_val is None:
                    setattr(value, "model_MClass4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_MAttribute2(self):
        return self.__model_MAttribute2

    @model_MAttribute2.setter
    def model_MAttribute2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_MAttribute__model_MAttribute2", None)
        self.__model_MAttribute2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Type"):
                opp_val = getattr(old_value, "model_Type", None)
                if opp_val == self:
                    setattr(old_value, "model_Type", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Type"):
                opp_val = getattr(value, "model_Type", None)
                setattr(value, "model_Type", self)

    def processWithVisitor(self, v: str):
        # TODO: Implement processWithVisitor method
        pass

class BasicType:

    pass
class model_RealType(BasicType):

    pass
class model_StringType(BasicType):

    pass
class model_BooleanType(BasicType):

    pass
class model_IntegerType(BasicType):

    pass
class Type:

    pass
class model_EnumType(Type):

    def __init__(self, name: str, literals: str):
        self.name = name
        self.literals = literals
        
    @property
    def literals(self) -> str:
        return self.__literals

    @literals.setter
    def literals(self, literals: str):
        self.__literals = literals

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    def addLiteral(self, literal: str):
        # TODO: Implement addLiteral method
        pass

class model_CollectionType(Type):

    pass
class model_ObjectType(Type):

    pass
class model_TupleType(Type):

    def __init__(self, parts: str):
        self.parts = parts
        
    @property
    def parts(self) -> str:
        return self.__parts

    @parts.setter
    def parts(self, parts: str):
        self.__parts = parts

class model_VoidType(Type):

    pass
class model_OclAnyType(Type):

    pass
class model_BasicType(Type):

    pass
class model_Type:

    def __init__(self, typeName: str, typeId: int, model_Type: "model_MAttribute" = None, model_Type27: "model_MOperation" = None, model_Type32: "model_VarDecl" = None, model_Type34: "model_CollectionType" = None, model_Type76: "model_Part" = None):
        self.typeName = typeName
        self.typeId = typeId
        self.model_Type = model_Type
        self.model_Type27 = model_Type27
        self.model_Type32 = model_Type32
        self.model_Type34 = model_Type34
        self.model_Type76 = model_Type76
        
    @property
    def typeId(self) -> int:
        return self.__typeId

    @typeId.setter
    def typeId(self, typeId: int):
        self.__typeId = typeId

    @property
    def typeName(self) -> str:
        return self.__typeName

    @typeName.setter
    def typeName(self, typeName: str):
        self.__typeName = typeName

    @property
    def model_Type(self):
        return self.__model_Type

    @model_Type.setter
    def model_Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Type__model_Type", None)
        self.__model_Type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_MAttribute2"):
                opp_val = getattr(old_value, "model_MAttribute2", None)
                if opp_val == self:
                    setattr(old_value, "model_MAttribute2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_MAttribute2"):
                opp_val = getattr(value, "model_MAttribute2", None)
                setattr(value, "model_MAttribute2", self)

    @property
    def model_Type27(self):
        return self.__model_Type27

    @model_Type27.setter
    def model_Type27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Type__model_Type27", None)
        self.__model_Type27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_MOperation26"):
                opp_val = getattr(old_value, "model_MOperation26", None)
                if opp_val == self:
                    setattr(old_value, "model_MOperation26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_MOperation26"):
                opp_val = getattr(value, "model_MOperation26", None)
                setattr(value, "model_MOperation26", self)

    @property
    def model_Type32(self):
        return self.__model_Type32

    @model_Type32.setter
    def model_Type32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Type__model_Type32", None)
        self.__model_Type32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_VarDecl31"):
                opp_val = getattr(old_value, "model_VarDecl31", None)
                if opp_val == self:
                    setattr(old_value, "model_VarDecl31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_VarDecl31"):
                opp_val = getattr(value, "model_VarDecl31", None)
                setattr(value, "model_VarDecl31", self)

    @property
    def model_Type34(self):
        return self.__model_Type34

    @model_Type34.setter
    def model_Type34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Type__model_Type34", None)
        self.__model_Type34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_CollectionType"):
                opp_val = getattr(old_value, "model_CollectionType", None)
                if opp_val == self:
                    setattr(old_value, "model_CollectionType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_CollectionType"):
                opp_val = getattr(value, "model_CollectionType", None)
                setattr(value, "model_CollectionType", self)

    @property
    def model_Type76(self):
        return self.__model_Type76

    @model_Type76.setter
    def model_Type76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Type__model_Type76", None)
        self.__model_Type76 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Part"):
                opp_val = getattr(old_value, "model_Part", None)
                if opp_val == self:
                    setattr(old_value, "model_Part", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Part"):
                opp_val = getattr(value, "model_Part", None)
                setattr(value, "model_Part", self)

class model_MClass(MModelElementEx):

    def __init__(self, model_MClass: "model_MAttribute" = None, model_MClass4: set["model_MAttribute"] = None, model_MClass7: set["model_MOperation"] = None, model_MClass9: set["model_MAssociation"] = None, model_MClass12: "model_MClass" = None, model_MClass10: set["model_MClass"] = None, model_MClass15: "model_MClass" = None, model_MClass13: set["model_MClass"] = None, model_MClass17: "model_MModel" = None, model_MClass24: "model_MOperation" = None, model_MClass36: "model_ObjectType" = None, model_MClass55: "model_MNavigableElement" = None, model_MClass46: "model_MAssociationEnd" = None, model_MClass63: "model_MClassInvariant" = None):
        self.model_MClass = model_MClass
        self.model_MClass4 = model_MClass4 if model_MClass4 is not None else set()
        self.model_MClass7 = model_MClass7 if model_MClass7 is not None else set()
        self.model_MClass9 = model_MClass9 if model_MClass9 is not None else set()
        self.model_MClass12 = model_MClass12
        self.model_MClass10 = model_MClass10 if model_MClass10 is not None else set()
        self.model_MClass15 = model_MClass15
        self.model_MClass13 = model_MClass13 if model_MClass13 is not None else set()
        self.model_MClass17 = model_MClass17
        self.model_MClass24 = model_MClass24
        self.model_MClass36 = model_MClass36
        self.model_MClass55 = model_MClass55
        self.model_MClass46 = model_MClass46
        self.model_MClass63 = model_MClass63
        
    @property
    def model_MClass36(self):
        return self.__model_MClass36

    @model_MClass36.setter
    def model_MClass36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_MClass__model_MClass36", None)
        self.__model_MClass36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_ObjectType"):
                opp_val = getattr(old_value, "model_ObjectType", None)
                if opp_val == self:
                    setattr(old_value, "model_ObjectType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_ObjectType"):
                opp_val = getattr(value, "model_ObjectType", None)
                setattr(value, "model_ObjectType", self)

    @property
    def model_MClass46(self):
        return self.__model_MClass46

    @model_MClass46.setter
    def model_MClass46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_MClass__model_MClass46", None)
        self.__model_MClass46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_MAssociationEnd45"):
                opp_val = getattr(old_value, "model_MAssociationEnd45", None)
                if opp_val == self:
                    setattr(old_value, "model_MAssociationEnd45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_MAssociationEnd45"):
                opp_val = getattr(value, "model_MAssociationEnd45", None)
                setattr(value, "model_MAssociationEnd45", self)

    @property
    def model_MClass15(self):
        return self.__model_MClass15

    @model_MClass15.setter
    def model_MClass15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_MClass__model_MClass15", None)
        self.__model_MClass15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_MClass13"):
                opp_val = getattr(old_value, "model_MClass13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_MClass13"):
                opp_val = getattr(value, "model_MClass13", None)
                if opp_val is None:
                    setattr(value, "model_MClass13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_MClass13(self):
        return self.__model_MClass13

    @model_MClass13.setter
    def model_MClass13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_MClass__model_MClass13", None)
        self.__model_MClass13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_MClass15"):
                    opp_val = getattr(item, "model_MClass15", None)
                    
                    if opp_val == self:
                        setattr(item, "model_MClass15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_MClass15"):
                    opp_val = getattr(item, "model_MClass15", None)
                    
                    setattr(item, "model_MClass15", self)
                    

    @property
    def model_MClass7(self):
        return self.__model_MClass7

    @model_MClass7.setter
    def model_MClass7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_MClass__model_MClass7", None)
        self.__model_MClass7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_MOperation"):
                    opp_val = getattr(item, "model_MOperation", None)
                    
                    if opp_val == self:
                        setattr(item, "model_MOperation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_MOperation"):
                    opp_val = getattr(item, "model_MOperation", None)
                    
                    setattr(item, "model_MOperation", self)
                    

    @property
    def model_MClass17(self):
        return self.__model_MClass17

    @model_MClass17.setter
    def model_MClass17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_MClass__model_MClass17", None)
        self.__model_MClass17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_MModel"):
                opp_val = getattr(old_value, "model_MModel", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_MModel"):
                opp_val = getattr(value, "model_MModel", None)
                if opp_val is None:
                    setattr(value, "model_MModel", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_MClass24(self):
        return self.__model_MClass24

    @model_MClass24.setter
    def model_MClass24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_MClass__model_MClass24", None)
        self.__model_MClass24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_MOperation23"):
                opp_val = getattr(old_value, "model_MOperation23", None)
                if opp_val == self:
                    setattr(old_value, "model_MOperation23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_MOperation23"):
                opp_val = getattr(value, "model_MOperation23", None)
                setattr(value, "model_MOperation23", self)

    @property
    def model_MClass4(self):
        return self.__model_MClass4

    @model_MClass4.setter
    def model_MClass4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_MClass__model_MClass4", None)
        self.__model_MClass4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_MAttribute5"):
                    opp_val = getattr(item, "model_MAttribute5", None)
                    
                    if opp_val == self:
                        setattr(item, "model_MAttribute5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_MAttribute5"):
                    opp_val = getattr(item, "model_MAttribute5", None)
                    
                    setattr(item, "model_MAttribute5", self)
                    

    @property
    def model_MClass55(self):
        return self.__model_MClass55

    @model_MClass55.setter
    def model_MClass55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_MClass__model_MClass55", None)
        self.__model_MClass55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_MNavigableElement"):
                opp_val = getattr(old_value, "model_MNavigableElement", None)
                if opp_val == self:
                    setattr(old_value, "model_MNavigableElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_MNavigableElement"):
                opp_val = getattr(value, "model_MNavigableElement", None)
                setattr(value, "model_MNavigableElement", self)

    @property
    def model_MClass12(self):
        return self.__model_MClass12

    @model_MClass12.setter
    def model_MClass12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_MClass__model_MClass12", None)
        self.__model_MClass12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_MClass10"):
                opp_val = getattr(old_value, "model_MClass10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_MClass10"):
                opp_val = getattr(value, "model_MClass10", None)
                if opp_val is None:
                    setattr(value, "model_MClass10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_MClass9(self):
        return self.__model_MClass9

    @model_MClass9.setter
    def model_MClass9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_MClass__model_MClass9", None)
        self.__model_MClass9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_MAssociation"):
                    opp_val = getattr(item, "model_MAssociation", None)
                    
                    if opp_val == self:
                        setattr(item, "model_MAssociation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_MAssociation"):
                    opp_val = getattr(item, "model_MAssociation", None)
                    
                    setattr(item, "model_MAssociation", self)
                    

    @property
    def model_MClass63(self):
        return self.__model_MClass63

    @model_MClass63.setter
    def model_MClass63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_MClass__model_MClass63", None)
        self.__model_MClass63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_MClassInvariant62"):
                opp_val = getattr(old_value, "model_MClassInvariant62", None)
                if opp_val == self:
                    setattr(old_value, "model_MClassInvariant62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_MClassInvariant62"):
                opp_val = getattr(value, "model_MClassInvariant62", None)
                setattr(value, "model_MClassInvariant62", self)

    @property
    def model_MClass(self):
        return self.__model_MClass

    @model_MClass.setter
    def model_MClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_MClass__model_MClass", None)
        self.__model_MClass = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_MAttribute"):
                opp_val = getattr(old_value, "model_MAttribute", None)
                if opp_val == self:
                    setattr(old_value, "model_MAttribute", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_MAttribute"):
                opp_val = getattr(value, "model_MAttribute", None)
                setattr(value, "model_MAttribute", self)

    @property
    def model_MClass10(self):
        return self.__model_MClass10

    @model_MClass10.setter
    def model_MClass10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_MClass__model_MClass10", None)
        self.__model_MClass10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_MClass12"):
                    opp_val = getattr(item, "model_MClass12", None)
                    
                    if opp_val == self:
                        setattr(item, "model_MClass12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_MClass12"):
                    opp_val = getattr(item, "model_MClass12", None)
                    
                    setattr(item, "model_MClass12", self)
                    

    def addAssociation(self, a: str):
        # TODO: Implement addAssociation method
        pass

    def getAbstract(self) -> bool:
        # TODO: Implement getAbstract method
        pass

    def addOperation(self, op: str):
        # TODO: Implement addOperation method
        pass

    def addParent(self, c: str):
        # TODO: Implement addParent method
        pass

    def processWithVisitor(self, v: str):
        # TODO: Implement processWithVisitor method
        pass

    def addAttribute(self, attr: str):
        # TODO: Implement addAttribute method
        pass

    def setAbstract(self, b: bool):
        # TODO: Implement setAbstract method
        pass

    def addChild(self, c: str):
        # TODO: Implement addChild method
        pass
