from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class OclLType:

    pass
class oCLlite_RealType(OclLType):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class oCLlite_StringType(OclLType):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class oCLlite_SequenceType(OclLType):

    def __init__(self, name: str, oCLlite_SequenceType: "oCLlite_OclLType" = None):
        self.name = name
        self.oCLlite_SequenceType = oCLlite_SequenceType
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def oCLlite_SequenceType(self):
        return self.__oCLlite_SequenceType

    @oCLlite_SequenceType.setter
    def oCLlite_SequenceType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oCLlite_SequenceType__oCLlite_SequenceType", None)
        self.__oCLlite_SequenceType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oCLlite_OclLType69"):
                opp_val = getattr(old_value, "oCLlite_OclLType69", None)
                if opp_val == self:
                    setattr(old_value, "oCLlite_OclLType69", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oCLlite_OclLType69"):
                opp_val = getattr(value, "oCLlite_OclLType69", None)
                setattr(value, "oCLlite_OclLType69", self)

class oCLlite_IntegerType(OclLType):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class oCLlite_OrderedSetType(OclLType):

    def __init__(self, name: str, oCLlite_OrderedSetType: "oCLlite_OclLType" = None):
        self.name = name
        self.oCLlite_OrderedSetType = oCLlite_OrderedSetType
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def oCLlite_OrderedSetType(self):
        return self.__oCLlite_OrderedSetType

    @oCLlite_OrderedSetType.setter
    def oCLlite_OrderedSetType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oCLlite_OrderedSetType__oCLlite_OrderedSetType", None)
        self.__oCLlite_OrderedSetType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oCLlite_OclLType71"):
                opp_val = getattr(old_value, "oCLlite_OclLType71", None)
                if opp_val == self:
                    setattr(old_value, "oCLlite_OclLType71", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oCLlite_OclLType71"):
                opp_val = getattr(value, "oCLlite_OclLType71", None)
                setattr(value, "oCLlite_OclLType71", self)

class oCLlite_BooleanType(OclLType):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class oCLlite_BagType(OclLType):

    def __init__(self, name: str, oCLlite_BagType: "oCLlite_OclLType" = None):
        self.name = name
        self.oCLlite_BagType = oCLlite_BagType
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def oCLlite_BagType(self):
        return self.__oCLlite_BagType

    @oCLlite_BagType.setter
    def oCLlite_BagType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oCLlite_BagType__oCLlite_BagType", None)
        self.__oCLlite_BagType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oCLlite_OclLType73"):
                opp_val = getattr(old_value, "oCLlite_OclLType73", None)
                if opp_val == self:
                    setattr(old_value, "oCLlite_OclLType73", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oCLlite_OclLType73"):
                opp_val = getattr(value, "oCLlite_OclLType73", None)
                setattr(value, "oCLlite_OclLType73", self)

class oCLlite_OclLModelElementExp(OclLType):

    def __init__(self, name: str, oCLlite_OclLModelElementExp: "oCLlite_OclLModel" = None):
        self.name = name
        self.oCLlite_OclLModelElementExp = oCLlite_OclLModelElementExp
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def oCLlite_OclLModelElementExp(self):
        return self.__oCLlite_OclLModelElementExp

    @oCLlite_OclLModelElementExp.setter
    def oCLlite_OclLModelElementExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oCLlite_OclLModelElementExp__oCLlite_OclLModelElementExp", None)
        self.__oCLlite_OclLModelElementExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oCLlite_OclLModel55"):
                opp_val = getattr(old_value, "oCLlite_OclLModel55", None)
                if opp_val == self:
                    setattr(old_value, "oCLlite_OclLModel55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oCLlite_OclLModel55"):
                opp_val = getattr(value, "oCLlite_OclLModel55", None)
                setattr(value, "oCLlite_OclLModel55", self)

class oCLlite_SetType(OclLType):

    def __init__(self, name: str, oCLlite_SetType: "oCLlite_OclLType" = None):
        self.name = name
        self.oCLlite_SetType = oCLlite_SetType
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def oCLlite_SetType(self):
        return self.__oCLlite_SetType

    @oCLlite_SetType.setter
    def oCLlite_SetType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oCLlite_SetType__oCLlite_SetType", None)
        self.__oCLlite_SetType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oCLlite_OclLType67"):
                opp_val = getattr(old_value, "oCLlite_OclLType67", None)
                if opp_val == self:
                    setattr(old_value, "oCLlite_OclLType67", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oCLlite_OclLType67"):
                opp_val = getattr(value, "oCLlite_OclLType67", None)
                setattr(value, "oCLlite_OclLType67", self)

class oCLlite_OclLAnyType(OclLType):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class oCLlite_TupleType(OclLType):

    pass
class oCLlite_MapType(OclLType):

    def __init__(self, name: str, oCLlite_MapType: "oCLlite_OclLType" = None, oCLlite_MapType64: "oCLlite_OclLType" = None):
        self.name = name
        self.oCLlite_MapType = oCLlite_MapType
        self.oCLlite_MapType64 = oCLlite_MapType64
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def oCLlite_MapType(self):
        return self.__oCLlite_MapType

    @oCLlite_MapType.setter
    def oCLlite_MapType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oCLlite_MapType__oCLlite_MapType", None)
        self.__oCLlite_MapType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oCLlite_OclLType62"):
                opp_val = getattr(old_value, "oCLlite_OclLType62", None)
                if opp_val == self:
                    setattr(old_value, "oCLlite_OclLType62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oCLlite_OclLType62"):
                opp_val = getattr(value, "oCLlite_OclLType62", None)
                setattr(value, "oCLlite_OclLType62", self)

    @property
    def oCLlite_MapType64(self):
        return self.__oCLlite_MapType64

    @oCLlite_MapType64.setter
    def oCLlite_MapType64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oCLlite_MapType__oCLlite_MapType64", None)
        self.__oCLlite_MapType64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oCLlite_OclLType65"):
                opp_val = getattr(old_value, "oCLlite_OclLType65", None)
                if opp_val == self:
                    setattr(old_value, "oCLlite_OclLType65", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oCLlite_OclLType65"):
                opp_val = getattr(value, "oCLlite_OclLType65", None)
                setattr(value, "oCLlite_OclLType65", self)

class oCLlite_LambdaType(OclLType):

    def __init__(self, name: str, oCLlite_LambdaType: set["oCLlite_OclLType"] = None, oCLlite_LambdaType59: "oCLlite_OclLType" = None):
        self.name = name
        self.oCLlite_LambdaType = oCLlite_LambdaType if oCLlite_LambdaType is not None else set()
        self.oCLlite_LambdaType59 = oCLlite_LambdaType59
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def oCLlite_LambdaType59(self):
        return self.__oCLlite_LambdaType59

    @oCLlite_LambdaType59.setter
    def oCLlite_LambdaType59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oCLlite_LambdaType__oCLlite_LambdaType59", None)
        self.__oCLlite_LambdaType59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oCLlite_OclLType60"):
                opp_val = getattr(old_value, "oCLlite_OclLType60", None)
                if opp_val == self:
                    setattr(old_value, "oCLlite_OclLType60", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oCLlite_OclLType60"):
                opp_val = getattr(value, "oCLlite_OclLType60", None)
                setattr(value, "oCLlite_OclLType60", self)

    @property
    def oCLlite_LambdaType(self):
        return self.__oCLlite_LambdaType

    @oCLlite_LambdaType.setter
    def oCLlite_LambdaType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oCLlite_LambdaType__oCLlite_LambdaType", None)
        self.__oCLlite_LambdaType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "oCLlite_OclLType57"):
                    opp_val = getattr(item, "oCLlite_OclLType57", None)
                    
                    if opp_val == self:
                        setattr(item, "oCLlite_OclLType57", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "oCLlite_OclLType57"):
                    opp_val = getattr(item, "oCLlite_OclLType57", None)
                    
                    setattr(item, "oCLlite_OclLType57", self)
                    

class oCLlite_EnvType(OclLType):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class oCLlite_MapElement:

    pass
class CollectionExp:

    pass
class oCLlite_OrderedSetExp(CollectionExp):

    pass
class oCLlite_SetExp(CollectionExp):

    pass
class oCLlite_SequenceExp(CollectionExp):

    pass
class oCLlite_BagExp(CollectionExp):

    pass
class PrimitiveExp:

    pass
class oCLlite_InvalidLiteralExp(PrimitiveExp):

    pass
class oCLlite_NullLiteralExp(PrimitiveExp):

    pass
class oCLlite_UnlimitedNaturalLiteralExp(PrimitiveExp):

    pass
class oCLlite_BooleanLiteralExp(PrimitiveExp):

    def __init__(self, symbol: str):
        self.symbol = symbol
        
    @property
    def symbol(self) -> str:
        return self.__symbol

    @symbol.setter
    def symbol(self, symbol: str):
        self.__symbol = symbol

class oCLlite_StringLiteralExp(PrimitiveExp):

    def __init__(self, segments: str):
        self.segments = segments
        
    @property
    def segments(self) -> str:
        return self.__segments

    @segments.setter
    def segments(self, segments: str):
        self.__segments = segments

class oCLlite_NumberLiteralExp(PrimitiveExp):

    def __init__(self, symbol: int):
        self.symbol = symbol
        
    @property
    def symbol(self) -> int:
        return self.__symbol

    @symbol.setter
    def symbol(self, symbol: int):
        self.__symbol = symbol

class oCLlite_TuplePart:

    def __init__(self, name: str, oCLlite_TuplePart: "oCLlite_OclLType" = None, oCLlite_TuplePart41: "oCLlite_OclLExpression" = None, oCLlite_TuplePart106: "oCLlite_TupleExp" = None):
        self.name = name
        self.oCLlite_TuplePart = oCLlite_TuplePart
        self.oCLlite_TuplePart41 = oCLlite_TuplePart41
        self.oCLlite_TuplePart106 = oCLlite_TuplePart106
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def oCLlite_TuplePart(self):
        return self.__oCLlite_TuplePart

    @oCLlite_TuplePart.setter
    def oCLlite_TuplePart(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oCLlite_TuplePart__oCLlite_TuplePart", None)
        self.__oCLlite_TuplePart = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oCLlite_OclLType39"):
                opp_val = getattr(old_value, "oCLlite_OclLType39", None)
                if opp_val == self:
                    setattr(old_value, "oCLlite_OclLType39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oCLlite_OclLType39"):
                opp_val = getattr(value, "oCLlite_OclLType39", None)
                setattr(value, "oCLlite_OclLType39", self)

    @property
    def oCLlite_TuplePart106(self):
        return self.__oCLlite_TuplePart106

    @oCLlite_TuplePart106.setter
    def oCLlite_TuplePart106(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oCLlite_TuplePart__oCLlite_TuplePart106", None)
        self.__oCLlite_TuplePart106 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oCLlite_TupleExp"):
                opp_val = getattr(old_value, "oCLlite_TupleExp", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oCLlite_TupleExp"):
                opp_val = getattr(value, "oCLlite_TupleExp", None)
                if opp_val is None:
                    setattr(value, "oCLlite_TupleExp", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def oCLlite_TuplePart41(self):
        return self.__oCLlite_TuplePart41

    @oCLlite_TuplePart41.setter
    def oCLlite_TuplePart41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oCLlite_TuplePart__oCLlite_TuplePart41", None)
        self.__oCLlite_TuplePart41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oCLlite_OclLExpression42"):
                opp_val = getattr(old_value, "oCLlite_OclLExpression42", None)
                if opp_val == self:
                    setattr(old_value, "oCLlite_OclLExpression42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oCLlite_OclLExpression42"):
                opp_val = getattr(value, "oCLlite_OclLExpression42", None)
                setattr(value, "oCLlite_OclLExpression42", self)

class ModuleElement:

    pass
class oCLlite_Query(ModuleElement):

    def __init__(self, name: str, oCLlite_Query: "oCLlite_OclLExpression" = None):
        self.name = name
        self.oCLlite_Query = oCLlite_Query
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def oCLlite_Query(self):
        return self.__oCLlite_Query

    @oCLlite_Query.setter
    def oCLlite_Query(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oCLlite_Query__oCLlite_Query", None)
        self.__oCLlite_Query = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oCLlite_OclLExpression"):
                opp_val = getattr(old_value, "oCLlite_OclLExpression", None)
                if opp_val == self:
                    setattr(old_value, "oCLlite_OclLExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oCLlite_OclLExpression"):
                opp_val = getattr(value, "oCLlite_OclLExpression", None)
                setattr(value, "oCLlite_OclLExpression", self)

class oCLlite_URI_:

    def __init__(self, scheme: str, authority: str, fragment_: str, oCLlite_URI_: "oCLlite_OclLModel" = None):
        self.scheme = scheme
        self.authority = authority
        self.fragment_ = fragment_
        self.oCLlite_URI_ = oCLlite_URI_
        
    @property
    def authority(self) -> str:
        return self.__authority

    @authority.setter
    def authority(self, authority: str):
        self.__authority = authority

    @property
    def scheme(self) -> str:
        return self.__scheme

    @scheme.setter
    def scheme(self, scheme: str):
        self.__scheme = scheme

    @property
    def fragment_(self) -> str:
        return self.__fragment_

    @fragment_.setter
    def fragment_(self, fragment_: str):
        self.__fragment_ = fragment_

    @property
    def oCLlite_URI_(self):
        return self.__oCLlite_URI_

    @oCLlite_URI_.setter
    def oCLlite_URI_(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oCLlite_URI___oCLlite_URI_", None)
        self.__oCLlite_URI_ = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oCLlite_OclLModel9"):
                opp_val = getattr(old_value, "oCLlite_OclLModel9", None)
                if opp_val == self:
                    setattr(old_value, "oCLlite_OclLModel9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oCLlite_OclLModel9"):
                opp_val = getattr(value, "oCLlite_OclLModel9", None)
                setattr(value, "oCLlite_OclLModel9", self)

class OclLExpression:

    pass
class oCLlite_PrimitiveExp(OclLExpression):

    pass
class oCLlite_EqOpCallExp(OclLExpression):

    pass
class oCLlite_CollectionOpCallExp(OclLExpression):

    pass
class oCLlite_ElseIfThenExp(OclLExpression):

    pass
class oCLlite_ComOpCallExp(OclLExpression):

    pass
class oCLlite_MulOpCallExp(OclLExpression):

    pass
class oCLlite_MapExp(OclLExpression):

    pass
class oCLlite_LambdaExp(OclLExpression):

    pass
class oCLlite_BoolOpCallExp(OclLExpression):

    pass
class oCLlite_IfExp(OclLExpression):

    pass
class oCLlite_IteratorExp(OclLExpression):

    pass
class oCLlite_SelfExp(OclLExpression):

    pass
class oCLlite_TupleExp(OclLExpression):

    pass
class oCLlite_AddOpCallExp(OclLExpression):

    pass
class oCLlite_NavigationOrAttributeCall(OclLExpression):

    def __init__(self, feature: str):
        self.feature = feature
        
    @property
    def feature(self) -> str:
        return self.__feature

    @feature.setter
    def feature(self, feature: str):
        self.__feature = feature

class oCLlite_IterateExp(OclLExpression):

    pass
class oCLlite_NestedExp(OclLExpression):

    pass
class oCLlite_NavigationExp(OclLExpression):

    pass
class oCLlite_OperationCall(OclLExpression):

    pass
class oCLlite_CollectionExp(OclLExpression):

    pass
class oCLlite_OclLType:

    pass
class oCLlite_Iterator:

    def __init__(self, name: str, oCLlite_Iterator: "oCLlite_OclLType" = None, oCLlite_Iterator89: "oCLlite_IterateExp" = None, oCLlite_Iterator97: "oCLlite_IteratorExp" = None):
        self.name = name
        self.oCLlite_Iterator = oCLlite_Iterator
        self.oCLlite_Iterator89 = oCLlite_Iterator89
        self.oCLlite_Iterator97 = oCLlite_Iterator97
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def oCLlite_Iterator97(self):
        return self.__oCLlite_Iterator97

    @oCLlite_Iterator97.setter
    def oCLlite_Iterator97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oCLlite_Iterator__oCLlite_Iterator97", None)
        self.__oCLlite_Iterator97 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oCLlite_IteratorExp"):
                opp_val = getattr(old_value, "oCLlite_IteratorExp", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oCLlite_IteratorExp"):
                opp_val = getattr(value, "oCLlite_IteratorExp", None)
                if opp_val is None:
                    setattr(value, "oCLlite_IteratorExp", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def oCLlite_Iterator89(self):
        return self.__oCLlite_Iterator89

    @oCLlite_Iterator89.setter
    def oCLlite_Iterator89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oCLlite_Iterator__oCLlite_Iterator89", None)
        self.__oCLlite_Iterator89 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oCLlite_IterateExp"):
                opp_val = getattr(old_value, "oCLlite_IterateExp", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oCLlite_IterateExp"):
                opp_val = getattr(value, "oCLlite_IterateExp", None)
                if opp_val is None:
                    setattr(value, "oCLlite_IterateExp", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def oCLlite_Iterator(self):
        return self.__oCLlite_Iterator

    @oCLlite_Iterator.setter
    def oCLlite_Iterator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oCLlite_Iterator__oCLlite_Iterator", None)
        self.__oCLlite_Iterator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oCLlite_OclLType"):
                opp_val = getattr(old_value, "oCLlite_OclLType", None)
                if opp_val == self:
                    setattr(old_value, "oCLlite_OclLType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oCLlite_OclLType"):
                opp_val = getattr(value, "oCLlite_OclLType", None)
                setattr(value, "oCLlite_OclLType", self)

class oCLlite_LocalVariable:

    def __init__(self, name: str, oCLlite_LocalVariable: "oCLlite_OclLExpression" = None, oCLlite_LocalVariable24: "oCLlite_OclLType" = None, oCLlite_LocalVariable27: "oCLlite_OclLExpression" = None, oCLlite_LocalVariable92: "oCLlite_IterateExp" = None):
        self.name = name
        self.oCLlite_LocalVariable = oCLlite_LocalVariable
        self.oCLlite_LocalVariable24 = oCLlite_LocalVariable24
        self.oCLlite_LocalVariable27 = oCLlite_LocalVariable27
        self.oCLlite_LocalVariable92 = oCLlite_LocalVariable92
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def oCLlite_LocalVariable(self):
        return self.__oCLlite_LocalVariable

    @oCLlite_LocalVariable.setter
    def oCLlite_LocalVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oCLlite_LocalVariable__oCLlite_LocalVariable", None)
        self.__oCLlite_LocalVariable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oCLlite_OclLExpression12"):
                opp_val = getattr(old_value, "oCLlite_OclLExpression12", None)
                if opp_val == self:
                    setattr(old_value, "oCLlite_OclLExpression12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oCLlite_OclLExpression12"):
                opp_val = getattr(value, "oCLlite_OclLExpression12", None)
                setattr(value, "oCLlite_OclLExpression12", self)

    @property
    def oCLlite_LocalVariable24(self):
        return self.__oCLlite_LocalVariable24

    @oCLlite_LocalVariable24.setter
    def oCLlite_LocalVariable24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oCLlite_LocalVariable__oCLlite_LocalVariable24", None)
        self.__oCLlite_LocalVariable24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oCLlite_OclLType25"):
                opp_val = getattr(old_value, "oCLlite_OclLType25", None)
                if opp_val == self:
                    setattr(old_value, "oCLlite_OclLType25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oCLlite_OclLType25"):
                opp_val = getattr(value, "oCLlite_OclLType25", None)
                setattr(value, "oCLlite_OclLType25", self)

    @property
    def oCLlite_LocalVariable92(self):
        return self.__oCLlite_LocalVariable92

    @oCLlite_LocalVariable92.setter
    def oCLlite_LocalVariable92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oCLlite_LocalVariable__oCLlite_LocalVariable92", None)
        self.__oCLlite_LocalVariable92 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oCLlite_IterateExp91"):
                opp_val = getattr(old_value, "oCLlite_IterateExp91", None)
                if opp_val == self:
                    setattr(old_value, "oCLlite_IterateExp91", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oCLlite_IterateExp91"):
                opp_val = getattr(value, "oCLlite_IterateExp91", None)
                setattr(value, "oCLlite_IterateExp91", self)

    @property
    def oCLlite_LocalVariable27(self):
        return self.__oCLlite_LocalVariable27

    @oCLlite_LocalVariable27.setter
    def oCLlite_LocalVariable27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oCLlite_LocalVariable__oCLlite_LocalVariable27", None)
        self.__oCLlite_LocalVariable27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oCLlite_OclLExpression28"):
                opp_val = getattr(old_value, "oCLlite_OclLExpression28", None)
                if opp_val == self:
                    setattr(old_value, "oCLlite_OclLExpression28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oCLlite_OclLExpression28"):
                opp_val = getattr(value, "oCLlite_OclLExpression28", None)
                setattr(value, "oCLlite_OclLExpression28", self)

class oCLlite_OclLExpression:

    def __init__(self, name: str, elements: str, oCLlite_OclLExpression: "oCLlite_Query" = None, oCLlite_OclLExpression12: "oCLlite_LocalVariable" = None, oCLlite_OclLExpression15: "oCLlite_OclLExpression" = None, oCLlite_OclLExpression13: "oCLlite_OclLExpression" = None, oCLlite_OclLExpression18: "oCLlite_OclLExpression" = None, oCLlite_OclLExpression16: "oCLlite_OclLExpression" = None, oCLlite_OclLExpression20: "oCLlite_OclLModel" = None, oCLlite_OclLExpression28: "oCLlite_LocalVariable" = None, oCLlite_OclLExpression34: "oCLlite_MapElement" = None, oCLlite_OclLExpression37: "oCLlite_MapElement" = None, oCLlite_OclLExpression42: "oCLlite_TuplePart" = None, oCLlite_OclLExpression44: "oCLlite_IfExp" = None, oCLlite_OclLExpression30: "oCLlite_CollectionExp" = None, oCLlite_OclLExpression47: "oCLlite_IfExp" = None, oCLlite_OclLExpression50: "oCLlite_IfExp" = None, oCLlite_OclLExpression53: "oCLlite_IfExp" = None, oCLlite_OclLExpression75: "oCLlite_BoolOpCallExp" = None, oCLlite_OclLExpression77: "oCLlite_EqOpCallExp" = None, oCLlite_OclLExpression79: "oCLlite_ComOpCallExp" = None, oCLlite_OclLExpression81: "oCLlite_AddOpCallExp" = None, oCLlite_OclLExpression87: "oCLlite_CollectionOpCallExp" = None, oCLlite_OclLExpression95: "oCLlite_IterateExp" = None, oCLlite_OclLExpression100: "oCLlite_IteratorExp" = None, oCLlite_OclLExpression102: "oCLlite_OperationCall" = None, oCLlite_OclLExpression83: "oCLlite_MulOpCallExp" = None, oCLlite_OclLExpression85: "oCLlite_NavigationExp" = None, oCLlite_OclLExpression111: "oCLlite_ElseIfThenExp" = None, oCLlite_OclLExpression113: "oCLlite_NestedExp" = None, oCLlite_OclLExpression104: "oCLlite_LambdaExp" = None, oCLlite_OclLExpression108: "oCLlite_ElseIfThenExp" = None):
        self.name = name
        self.elements = elements
        self.oCLlite_OclLExpression = oCLlite_OclLExpression
        self.oCLlite_OclLExpression12 = oCLlite_OclLExpression12
        self.oCLlite_OclLExpression15 = oCLlite_OclLExpression15
        self.oCLlite_OclLExpression13 = oCLlite_OclLExpression13
        self.oCLlite_OclLExpression18 = oCLlite_OclLExpression18
        self.oCLlite_OclLExpression16 = oCLlite_OclLExpression16
        self.oCLlite_OclLExpression20 = oCLlite_OclLExpression20
        self.oCLlite_OclLExpression28 = oCLlite_OclLExpression28
        self.oCLlite_OclLExpression34 = oCLlite_OclLExpression34
        self.oCLlite_OclLExpression37 = oCLlite_OclLExpression37
        self.oCLlite_OclLExpression42 = oCLlite_OclLExpression42
        self.oCLlite_OclLExpression44 = oCLlite_OclLExpression44
        self.oCLlite_OclLExpression30 = oCLlite_OclLExpression30
        self.oCLlite_OclLExpression47 = oCLlite_OclLExpression47
        self.oCLlite_OclLExpression50 = oCLlite_OclLExpression50
        self.oCLlite_OclLExpression53 = oCLlite_OclLExpression53
        self.oCLlite_OclLExpression75 = oCLlite_OclLExpression75
        self.oCLlite_OclLExpression77 = oCLlite_OclLExpression77
        self.oCLlite_OclLExpression79 = oCLlite_OclLExpression79
        self.oCLlite_OclLExpression81 = oCLlite_OclLExpression81
        self.oCLlite_OclLExpression87 = oCLlite_OclLExpression87
        self.oCLlite_OclLExpression95 = oCLlite_OclLExpression95
        self.oCLlite_OclLExpression100 = oCLlite_OclLExpression100
        self.oCLlite_OclLExpression102 = oCLlite_OclLExpression102
        self.oCLlite_OclLExpression83 = oCLlite_OclLExpression83
        self.oCLlite_OclLExpression85 = oCLlite_OclLExpression85
        self.oCLlite_OclLExpression111 = oCLlite_OclLExpression111
        self.oCLlite_OclLExpression113 = oCLlite_OclLExpression113
        self.oCLlite_OclLExpression104 = oCLlite_OclLExpression104
        self.oCLlite_OclLExpression108 = oCLlite_OclLExpression108
        
    @property
    def elements(self) -> str:
        return self.__elements

    @elements.setter
    def elements(self, elements: str):
        self.__elements = elements

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def oCLlite_OclLExpression47(self):
        return self.__oCLlite_OclLExpression47

    @oCLlite_OclLExpression47.setter
    def oCLlite_OclLExpression47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oCLlite_OclLExpression__oCLlite_OclLExpression47", None)
        self.__oCLlite_OclLExpression47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oCLlite_IfExp46"):
                opp_val = getattr(old_value, "oCLlite_IfExp46", None)
                if opp_val == self:
                    setattr(old_value, "oCLlite_IfExp46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oCLlite_IfExp46"):
                opp_val = getattr(value, "oCLlite_IfExp46", None)
                setattr(value, "oCLlite_IfExp46", self)

    @property
    def oCLlite_OclLExpression108(self):
        return self.__oCLlite_OclLExpression108

    @oCLlite_OclLExpression108.setter
    def oCLlite_OclLExpression108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oCLlite_OclLExpression__oCLlite_OclLExpression108", None)
        self.__oCLlite_OclLExpression108 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oCLlite_ElseIfThenExp"):
                opp_val = getattr(old_value, "oCLlite_ElseIfThenExp", None)
                if opp_val == self:
                    setattr(old_value, "oCLlite_ElseIfThenExp", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oCLlite_ElseIfThenExp"):
                opp_val = getattr(value, "oCLlite_ElseIfThenExp", None)
                setattr(value, "oCLlite_ElseIfThenExp", self)

    @property
    def oCLlite_OclLExpression100(self):
        return self.__oCLlite_OclLExpression100

    @oCLlite_OclLExpression100.setter
    def oCLlite_OclLExpression100(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oCLlite_OclLExpression__oCLlite_OclLExpression100", None)
        self.__oCLlite_OclLExpression100 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oCLlite_IteratorExp99"):
                opp_val = getattr(old_value, "oCLlite_IteratorExp99", None)
                if opp_val == self:
                    setattr(old_value, "oCLlite_IteratorExp99", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oCLlite_IteratorExp99"):
                opp_val = getattr(value, "oCLlite_IteratorExp99", None)
                setattr(value, "oCLlite_IteratorExp99", self)

    @property
    def oCLlite_OclLExpression81(self):
        return self.__oCLlite_OclLExpression81

    @oCLlite_OclLExpression81.setter
    def oCLlite_OclLExpression81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oCLlite_OclLExpression__oCLlite_OclLExpression81", None)
        self.__oCLlite_OclLExpression81 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oCLlite_AddOpCallExp"):
                opp_val = getattr(old_value, "oCLlite_AddOpCallExp", None)
                if opp_val == self:
                    setattr(old_value, "oCLlite_AddOpCallExp", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oCLlite_AddOpCallExp"):
                opp_val = getattr(value, "oCLlite_AddOpCallExp", None)
                setattr(value, "oCLlite_AddOpCallExp", self)

    @property
    def oCLlite_OclLExpression102(self):
        return self.__oCLlite_OclLExpression102

    @oCLlite_OclLExpression102.setter
    def oCLlite_OclLExpression102(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oCLlite_OclLExpression__oCLlite_OclLExpression102", None)
        self.__oCLlite_OclLExpression102 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oCLlite_OperationCall"):
                opp_val = getattr(old_value, "oCLlite_OperationCall", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oCLlite_OperationCall"):
                opp_val = getattr(value, "oCLlite_OperationCall", None)
                if opp_val is None:
                    setattr(value, "oCLlite_OperationCall", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def oCLlite_OclLExpression50(self):
        return self.__oCLlite_OclLExpression50

    @oCLlite_OclLExpression50.setter
    def oCLlite_OclLExpression50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oCLlite_OclLExpression__oCLlite_OclLExpression50", None)
        self.__oCLlite_OclLExpression50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oCLlite_IfExp49"):
                opp_val = getattr(old_value, "oCLlite_IfExp49", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oCLlite_IfExp49"):
                opp_val = getattr(value, "oCLlite_IfExp49", None)
                if opp_val is None:
                    setattr(value, "oCLlite_IfExp49", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def oCLlite_OclLExpression53(self):
        return self.__oCLlite_OclLExpression53

    @oCLlite_OclLExpression53.setter
    def oCLlite_OclLExpression53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oCLlite_OclLExpression__oCLlite_OclLExpression53", None)
        self.__oCLlite_OclLExpression53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oCLlite_IfExp52"):
                opp_val = getattr(old_value, "oCLlite_IfExp52", None)
                if opp_val == self:
                    setattr(old_value, "oCLlite_IfExp52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oCLlite_IfExp52"):
                opp_val = getattr(value, "oCLlite_IfExp52", None)
                setattr(value, "oCLlite_IfExp52", self)

    @property
    def oCLlite_OclLExpression(self):
        return self.__oCLlite_OclLExpression

    @oCLlite_OclLExpression.setter
    def oCLlite_OclLExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oCLlite_OclLExpression__oCLlite_OclLExpression", None)
        self.__oCLlite_OclLExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oCLlite_Query"):
                opp_val = getattr(old_value, "oCLlite_Query", None)
                if opp_val == self:
                    setattr(old_value, "oCLlite_Query", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oCLlite_Query"):
                opp_val = getattr(value, "oCLlite_Query", None)
                setattr(value, "oCLlite_Query", self)

    @property
    def oCLlite_OclLExpression30(self):
        return self.__oCLlite_OclLExpression30

    @oCLlite_OclLExpression30.setter
    def oCLlite_OclLExpression30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oCLlite_OclLExpression__oCLlite_OclLExpression30", None)
        self.__oCLlite_OclLExpression30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oCLlite_CollectionExp"):
                opp_val = getattr(old_value, "oCLlite_CollectionExp", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oCLlite_CollectionExp"):
                opp_val = getattr(value, "oCLlite_CollectionExp", None)
                if opp_val is None:
                    setattr(value, "oCLlite_CollectionExp", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def oCLlite_OclLExpression12(self):
        return self.__oCLlite_OclLExpression12

    @oCLlite_OclLExpression12.setter
    def oCLlite_OclLExpression12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oCLlite_OclLExpression__oCLlite_OclLExpression12", None)
        self.__oCLlite_OclLExpression12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oCLlite_LocalVariable"):
                opp_val = getattr(old_value, "oCLlite_LocalVariable", None)
                if opp_val == self:
                    setattr(old_value, "oCLlite_LocalVariable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oCLlite_LocalVariable"):
                opp_val = getattr(value, "oCLlite_LocalVariable", None)
                setattr(value, "oCLlite_LocalVariable", self)

    @property
    def oCLlite_OclLExpression83(self):
        return self.__oCLlite_OclLExpression83

    @oCLlite_OclLExpression83.setter
    def oCLlite_OclLExpression83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oCLlite_OclLExpression__oCLlite_OclLExpression83", None)
        self.__oCLlite_OclLExpression83 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oCLlite_MulOpCallExp"):
                opp_val = getattr(old_value, "oCLlite_MulOpCallExp", None)
                if opp_val == self:
                    setattr(old_value, "oCLlite_MulOpCallExp", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oCLlite_MulOpCallExp"):
                opp_val = getattr(value, "oCLlite_MulOpCallExp", None)
                setattr(value, "oCLlite_MulOpCallExp", self)

    @property
    def oCLlite_OclLExpression37(self):
        return self.__oCLlite_OclLExpression37

    @oCLlite_OclLExpression37.setter
    def oCLlite_OclLExpression37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oCLlite_OclLExpression__oCLlite_OclLExpression37", None)
        self.__oCLlite_OclLExpression37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oCLlite_MapElement36"):
                opp_val = getattr(old_value, "oCLlite_MapElement36", None)
                if opp_val == self:
                    setattr(old_value, "oCLlite_MapElement36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oCLlite_MapElement36"):
                opp_val = getattr(value, "oCLlite_MapElement36", None)
                setattr(value, "oCLlite_MapElement36", self)

    @property
    def oCLlite_OclLExpression113(self):
        return self.__oCLlite_OclLExpression113

    @oCLlite_OclLExpression113.setter
    def oCLlite_OclLExpression113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oCLlite_OclLExpression__oCLlite_OclLExpression113", None)
        self.__oCLlite_OclLExpression113 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oCLlite_NestedExp"):
                opp_val = getattr(old_value, "oCLlite_NestedExp", None)
                if opp_val == self:
                    setattr(old_value, "oCLlite_NestedExp", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oCLlite_NestedExp"):
                opp_val = getattr(value, "oCLlite_NestedExp", None)
                setattr(value, "oCLlite_NestedExp", self)

    @property
    def oCLlite_OclLExpression16(self):
        return self.__oCLlite_OclLExpression16

    @oCLlite_OclLExpression16.setter
    def oCLlite_OclLExpression16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oCLlite_OclLExpression__oCLlite_OclLExpression16", None)
        self.__oCLlite_OclLExpression16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oCLlite_OclLExpression18"):
                opp_val = getattr(old_value, "oCLlite_OclLExpression18", None)
                if opp_val == self:
                    setattr(old_value, "oCLlite_OclLExpression18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oCLlite_OclLExpression18"):
                opp_val = getattr(value, "oCLlite_OclLExpression18", None)
                setattr(value, "oCLlite_OclLExpression18", self)

    @property
    def oCLlite_OclLExpression13(self):
        return self.__oCLlite_OclLExpression13

    @oCLlite_OclLExpression13.setter
    def oCLlite_OclLExpression13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oCLlite_OclLExpression__oCLlite_OclLExpression13", None)
        self.__oCLlite_OclLExpression13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oCLlite_OclLExpression15"):
                opp_val = getattr(old_value, "oCLlite_OclLExpression15", None)
                if opp_val == self:
                    setattr(old_value, "oCLlite_OclLExpression15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oCLlite_OclLExpression15"):
                opp_val = getattr(value, "oCLlite_OclLExpression15", None)
                setattr(value, "oCLlite_OclLExpression15", self)

    @property
    def oCLlite_OclLExpression77(self):
        return self.__oCLlite_OclLExpression77

    @oCLlite_OclLExpression77.setter
    def oCLlite_OclLExpression77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oCLlite_OclLExpression__oCLlite_OclLExpression77", None)
        self.__oCLlite_OclLExpression77 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oCLlite_EqOpCallExp"):
                opp_val = getattr(old_value, "oCLlite_EqOpCallExp", None)
                if opp_val == self:
                    setattr(old_value, "oCLlite_EqOpCallExp", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oCLlite_EqOpCallExp"):
                opp_val = getattr(value, "oCLlite_EqOpCallExp", None)
                setattr(value, "oCLlite_EqOpCallExp", self)

    @property
    def oCLlite_OclLExpression42(self):
        return self.__oCLlite_OclLExpression42

    @oCLlite_OclLExpression42.setter
    def oCLlite_OclLExpression42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oCLlite_OclLExpression__oCLlite_OclLExpression42", None)
        self.__oCLlite_OclLExpression42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oCLlite_TuplePart41"):
                opp_val = getattr(old_value, "oCLlite_TuplePart41", None)
                if opp_val == self:
                    setattr(old_value, "oCLlite_TuplePart41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oCLlite_TuplePart41"):
                opp_val = getattr(value, "oCLlite_TuplePart41", None)
                setattr(value, "oCLlite_TuplePart41", self)

    @property
    def oCLlite_OclLExpression44(self):
        return self.__oCLlite_OclLExpression44

    @oCLlite_OclLExpression44.setter
    def oCLlite_OclLExpression44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oCLlite_OclLExpression__oCLlite_OclLExpression44", None)
        self.__oCLlite_OclLExpression44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oCLlite_IfExp"):
                opp_val = getattr(old_value, "oCLlite_IfExp", None)
                if opp_val == self:
                    setattr(old_value, "oCLlite_IfExp", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oCLlite_IfExp"):
                opp_val = getattr(value, "oCLlite_IfExp", None)
                setattr(value, "oCLlite_IfExp", self)

    @property
    def oCLlite_OclLExpression104(self):
        return self.__oCLlite_OclLExpression104

    @oCLlite_OclLExpression104.setter
    def oCLlite_OclLExpression104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oCLlite_OclLExpression__oCLlite_OclLExpression104", None)
        self.__oCLlite_OclLExpression104 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oCLlite_LambdaExp"):
                opp_val = getattr(old_value, "oCLlite_LambdaExp", None)
                if opp_val == self:
                    setattr(old_value, "oCLlite_LambdaExp", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oCLlite_LambdaExp"):
                opp_val = getattr(value, "oCLlite_LambdaExp", None)
                setattr(value, "oCLlite_LambdaExp", self)

    @property
    def oCLlite_OclLExpression20(self):
        return self.__oCLlite_OclLExpression20

    @oCLlite_OclLExpression20.setter
    def oCLlite_OclLExpression20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oCLlite_OclLExpression__oCLlite_OclLExpression20", None)
        self.__oCLlite_OclLExpression20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oCLlite_OclLModel21"):
                opp_val = getattr(old_value, "oCLlite_OclLModel21", None)
                if opp_val == self:
                    setattr(old_value, "oCLlite_OclLModel21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oCLlite_OclLModel21"):
                opp_val = getattr(value, "oCLlite_OclLModel21", None)
                setattr(value, "oCLlite_OclLModel21", self)

    @property
    def oCLlite_OclLExpression34(self):
        return self.__oCLlite_OclLExpression34

    @oCLlite_OclLExpression34.setter
    def oCLlite_OclLExpression34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oCLlite_OclLExpression__oCLlite_OclLExpression34", None)
        self.__oCLlite_OclLExpression34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oCLlite_MapElement33"):
                opp_val = getattr(old_value, "oCLlite_MapElement33", None)
                if opp_val == self:
                    setattr(old_value, "oCLlite_MapElement33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oCLlite_MapElement33"):
                opp_val = getattr(value, "oCLlite_MapElement33", None)
                setattr(value, "oCLlite_MapElement33", self)

    @property
    def oCLlite_OclLExpression95(self):
        return self.__oCLlite_OclLExpression95

    @oCLlite_OclLExpression95.setter
    def oCLlite_OclLExpression95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oCLlite_OclLExpression__oCLlite_OclLExpression95", None)
        self.__oCLlite_OclLExpression95 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oCLlite_IterateExp94"):
                opp_val = getattr(old_value, "oCLlite_IterateExp94", None)
                if opp_val == self:
                    setattr(old_value, "oCLlite_IterateExp94", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oCLlite_IterateExp94"):
                opp_val = getattr(value, "oCLlite_IterateExp94", None)
                setattr(value, "oCLlite_IterateExp94", self)

    @property
    def oCLlite_OclLExpression111(self):
        return self.__oCLlite_OclLExpression111

    @oCLlite_OclLExpression111.setter
    def oCLlite_OclLExpression111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oCLlite_OclLExpression__oCLlite_OclLExpression111", None)
        self.__oCLlite_OclLExpression111 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oCLlite_ElseIfThenExp110"):
                opp_val = getattr(old_value, "oCLlite_ElseIfThenExp110", None)
                if opp_val == self:
                    setattr(old_value, "oCLlite_ElseIfThenExp110", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oCLlite_ElseIfThenExp110"):
                opp_val = getattr(value, "oCLlite_ElseIfThenExp110", None)
                setattr(value, "oCLlite_ElseIfThenExp110", self)

    @property
    def oCLlite_OclLExpression15(self):
        return self.__oCLlite_OclLExpression15

    @oCLlite_OclLExpression15.setter
    def oCLlite_OclLExpression15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oCLlite_OclLExpression__oCLlite_OclLExpression15", None)
        self.__oCLlite_OclLExpression15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oCLlite_OclLExpression13"):
                opp_val = getattr(old_value, "oCLlite_OclLExpression13", None)
                if opp_val == self:
                    setattr(old_value, "oCLlite_OclLExpression13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oCLlite_OclLExpression13"):
                opp_val = getattr(value, "oCLlite_OclLExpression13", None)
                setattr(value, "oCLlite_OclLExpression13", self)

    @property
    def oCLlite_OclLExpression87(self):
        return self.__oCLlite_OclLExpression87

    @oCLlite_OclLExpression87.setter
    def oCLlite_OclLExpression87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oCLlite_OclLExpression__oCLlite_OclLExpression87", None)
        self.__oCLlite_OclLExpression87 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oCLlite_CollectionOpCallExp"):
                opp_val = getattr(old_value, "oCLlite_CollectionOpCallExp", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oCLlite_CollectionOpCallExp"):
                opp_val = getattr(value, "oCLlite_CollectionOpCallExp", None)
                if opp_val is None:
                    setattr(value, "oCLlite_CollectionOpCallExp", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def oCLlite_OclLExpression28(self):
        return self.__oCLlite_OclLExpression28

    @oCLlite_OclLExpression28.setter
    def oCLlite_OclLExpression28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oCLlite_OclLExpression__oCLlite_OclLExpression28", None)
        self.__oCLlite_OclLExpression28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oCLlite_LocalVariable27"):
                opp_val = getattr(old_value, "oCLlite_LocalVariable27", None)
                if opp_val == self:
                    setattr(old_value, "oCLlite_LocalVariable27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oCLlite_LocalVariable27"):
                opp_val = getattr(value, "oCLlite_LocalVariable27", None)
                setattr(value, "oCLlite_LocalVariable27", self)

    @property
    def oCLlite_OclLExpression75(self):
        return self.__oCLlite_OclLExpression75

    @oCLlite_OclLExpression75.setter
    def oCLlite_OclLExpression75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oCLlite_OclLExpression__oCLlite_OclLExpression75", None)
        self.__oCLlite_OclLExpression75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oCLlite_BoolOpCallExp"):
                opp_val = getattr(old_value, "oCLlite_BoolOpCallExp", None)
                if opp_val == self:
                    setattr(old_value, "oCLlite_BoolOpCallExp", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oCLlite_BoolOpCallExp"):
                opp_val = getattr(value, "oCLlite_BoolOpCallExp", None)
                setattr(value, "oCLlite_BoolOpCallExp", self)

    @property
    def oCLlite_OclLExpression85(self):
        return self.__oCLlite_OclLExpression85

    @oCLlite_OclLExpression85.setter
    def oCLlite_OclLExpression85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oCLlite_OclLExpression__oCLlite_OclLExpression85", None)
        self.__oCLlite_OclLExpression85 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oCLlite_NavigationExp"):
                opp_val = getattr(old_value, "oCLlite_NavigationExp", None)
                if opp_val == self:
                    setattr(old_value, "oCLlite_NavigationExp", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oCLlite_NavigationExp"):
                opp_val = getattr(value, "oCLlite_NavigationExp", None)
                setattr(value, "oCLlite_NavigationExp", self)

    @property
    def oCLlite_OclLExpression79(self):
        return self.__oCLlite_OclLExpression79

    @oCLlite_OclLExpression79.setter
    def oCLlite_OclLExpression79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oCLlite_OclLExpression__oCLlite_OclLExpression79", None)
        self.__oCLlite_OclLExpression79 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oCLlite_ComOpCallExp"):
                opp_val = getattr(old_value, "oCLlite_ComOpCallExp", None)
                if opp_val == self:
                    setattr(old_value, "oCLlite_ComOpCallExp", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oCLlite_ComOpCallExp"):
                opp_val = getattr(value, "oCLlite_ComOpCallExp", None)
                setattr(value, "oCLlite_ComOpCallExp", self)

    @property
    def oCLlite_OclLExpression18(self):
        return self.__oCLlite_OclLExpression18

    @oCLlite_OclLExpression18.setter
    def oCLlite_OclLExpression18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oCLlite_OclLExpression__oCLlite_OclLExpression18", None)
        self.__oCLlite_OclLExpression18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oCLlite_OclLExpression16"):
                opp_val = getattr(old_value, "oCLlite_OclLExpression16", None)
                if opp_val == self:
                    setattr(old_value, "oCLlite_OclLExpression16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oCLlite_OclLExpression16"):
                opp_val = getattr(value, "oCLlite_OclLExpression16", None)
                setattr(value, "oCLlite_OclLExpression16", self)

class oCLlite_ModuleElement:

    pass
class oCLlite_Import:

    def __init__(self, name: str, oCLlite_Import: "oCLlite_Module" = None):
        self.name = name
        self.oCLlite_Import = oCLlite_Import
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def oCLlite_Import(self):
        return self.__oCLlite_Import

    @oCLlite_Import.setter
    def oCLlite_Import(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oCLlite_Import__oCLlite_Import", None)
        self.__oCLlite_Import = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oCLlite_Module5"):
                opp_val = getattr(old_value, "oCLlite_Module5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oCLlite_Module5"):
                opp_val = getattr(value, "oCLlite_Module5", None)
                if opp_val is None:
                    setattr(value, "oCLlite_Module5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class oCLlite_OclLModel:

    def __init__(self, name: str, oCLlite_OclLModel: "oCLlite_Module" = None, oCLlite_OclLModel3: "oCLlite_Module" = None, oCLlite_OclLModel21: "oCLlite_OclLExpression" = None, oCLlite_OclLModel9: "oCLlite_URI_" = None, oCLlite_OclLModel55: "oCLlite_OclLModelElementExp" = None):
        self.name = name
        self.oCLlite_OclLModel = oCLlite_OclLModel
        self.oCLlite_OclLModel3 = oCLlite_OclLModel3
        self.oCLlite_OclLModel21 = oCLlite_OclLModel21
        self.oCLlite_OclLModel9 = oCLlite_OclLModel9
        self.oCLlite_OclLModel55 = oCLlite_OclLModel55
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def oCLlite_OclLModel21(self):
        return self.__oCLlite_OclLModel21

    @oCLlite_OclLModel21.setter
    def oCLlite_OclLModel21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oCLlite_OclLModel__oCLlite_OclLModel21", None)
        self.__oCLlite_OclLModel21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oCLlite_OclLExpression20"):
                opp_val = getattr(old_value, "oCLlite_OclLExpression20", None)
                if opp_val == self:
                    setattr(old_value, "oCLlite_OclLExpression20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oCLlite_OclLExpression20"):
                opp_val = getattr(value, "oCLlite_OclLExpression20", None)
                setattr(value, "oCLlite_OclLExpression20", self)

    @property
    def oCLlite_OclLModel55(self):
        return self.__oCLlite_OclLModel55

    @oCLlite_OclLModel55.setter
    def oCLlite_OclLModel55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oCLlite_OclLModel__oCLlite_OclLModel55", None)
        self.__oCLlite_OclLModel55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oCLlite_OclLModelElementExp"):
                opp_val = getattr(old_value, "oCLlite_OclLModelElementExp", None)
                if opp_val == self:
                    setattr(old_value, "oCLlite_OclLModelElementExp", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oCLlite_OclLModelElementExp"):
                opp_val = getattr(value, "oCLlite_OclLModelElementExp", None)
                setattr(value, "oCLlite_OclLModelElementExp", self)

    @property
    def oCLlite_OclLModel(self):
        return self.__oCLlite_OclLModel

    @oCLlite_OclLModel.setter
    def oCLlite_OclLModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oCLlite_OclLModel__oCLlite_OclLModel", None)
        self.__oCLlite_OclLModel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oCLlite_Module"):
                opp_val = getattr(old_value, "oCLlite_Module", None)
                if opp_val == self:
                    setattr(old_value, "oCLlite_Module", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oCLlite_Module"):
                opp_val = getattr(value, "oCLlite_Module", None)
                setattr(value, "oCLlite_Module", self)

    @property
    def oCLlite_OclLModel9(self):
        return self.__oCLlite_OclLModel9

    @oCLlite_OclLModel9.setter
    def oCLlite_OclLModel9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oCLlite_OclLModel__oCLlite_OclLModel9", None)
        self.__oCLlite_OclLModel9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oCLlite_URI_"):
                opp_val = getattr(old_value, "oCLlite_URI_", None)
                if opp_val == self:
                    setattr(old_value, "oCLlite_URI_", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oCLlite_URI_"):
                opp_val = getattr(value, "oCLlite_URI_", None)
                setattr(value, "oCLlite_URI_", self)

    @property
    def oCLlite_OclLModel3(self):
        return self.__oCLlite_OclLModel3

    @oCLlite_OclLModel3.setter
    def oCLlite_OclLModel3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oCLlite_OclLModel__oCLlite_OclLModel3", None)
        self.__oCLlite_OclLModel3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oCLlite_Module2"):
                opp_val = getattr(old_value, "oCLlite_Module2", None)
                if opp_val == self:
                    setattr(old_value, "oCLlite_Module2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oCLlite_Module2"):
                opp_val = getattr(value, "oCLlite_Module2", None)
                setattr(value, "oCLlite_Module2", self)

class oCLlite_Module:

    def __init__(self, name: str, oCLlite_Module: "oCLlite_OclLModel" = None, oCLlite_Module2: "oCLlite_OclLModel" = None, oCLlite_Module5: set["oCLlite_Import"] = None, oCLlite_Module7: set["oCLlite_ModuleElement"] = None):
        self.name = name
        self.oCLlite_Module = oCLlite_Module
        self.oCLlite_Module2 = oCLlite_Module2
        self.oCLlite_Module5 = oCLlite_Module5 if oCLlite_Module5 is not None else set()
        self.oCLlite_Module7 = oCLlite_Module7 if oCLlite_Module7 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def oCLlite_Module2(self):
        return self.__oCLlite_Module2

    @oCLlite_Module2.setter
    def oCLlite_Module2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oCLlite_Module__oCLlite_Module2", None)
        self.__oCLlite_Module2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oCLlite_OclLModel3"):
                opp_val = getattr(old_value, "oCLlite_OclLModel3", None)
                if opp_val == self:
                    setattr(old_value, "oCLlite_OclLModel3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oCLlite_OclLModel3"):
                opp_val = getattr(value, "oCLlite_OclLModel3", None)
                setattr(value, "oCLlite_OclLModel3", self)

    @property
    def oCLlite_Module7(self):
        return self.__oCLlite_Module7

    @oCLlite_Module7.setter
    def oCLlite_Module7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oCLlite_Module__oCLlite_Module7", None)
        self.__oCLlite_Module7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "oCLlite_ModuleElement"):
                    opp_val = getattr(item, "oCLlite_ModuleElement", None)
                    
                    if opp_val == self:
                        setattr(item, "oCLlite_ModuleElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "oCLlite_ModuleElement"):
                    opp_val = getattr(item, "oCLlite_ModuleElement", None)
                    
                    setattr(item, "oCLlite_ModuleElement", self)
                    

    @property
    def oCLlite_Module(self):
        return self.__oCLlite_Module

    @oCLlite_Module.setter
    def oCLlite_Module(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oCLlite_Module__oCLlite_Module", None)
        self.__oCLlite_Module = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oCLlite_OclLModel"):
                opp_val = getattr(old_value, "oCLlite_OclLModel", None)
                if opp_val == self:
                    setattr(old_value, "oCLlite_OclLModel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oCLlite_OclLModel"):
                opp_val = getattr(value, "oCLlite_OclLModel", None)
                setattr(value, "oCLlite_OclLModel", self)

    @property
    def oCLlite_Module5(self):
        return self.__oCLlite_Module5

    @oCLlite_Module5.setter
    def oCLlite_Module5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oCLlite_Module__oCLlite_Module5", None)
        self.__oCLlite_Module5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "oCLlite_Import"):
                    opp_val = getattr(item, "oCLlite_Import", None)
                    
                    if opp_val == self:
                        setattr(item, "oCLlite_Import", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "oCLlite_Import"):
                    opp_val = getattr(item, "oCLlite_Import", None)
                    
                    setattr(item, "oCLlite_Import", self)
                    
