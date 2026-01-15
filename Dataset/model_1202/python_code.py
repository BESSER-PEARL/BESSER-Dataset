from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class OclType:

    pass
class docl_OclAnyType(OclType):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class docl_RealType(OclType):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class docl_TupleType(OclType):

    pass
class docl_StringType(OclType):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class docl_IntegerType(OclType):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class docl_BooleanType(OclType):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class docl_OrderedSetType(OclType):

    def __init__(self, name: str, docl_OrderedSetType: "docl_OclType" = None):
        self.name = name
        self.docl_OrderedSetType = docl_OrderedSetType
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def docl_OrderedSetType(self):
        return self.__docl_OrderedSetType

    @docl_OrderedSetType.setter
    def docl_OrderedSetType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_docl_OrderedSetType__docl_OrderedSetType", None)
        self.__docl_OrderedSetType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "docl_OclType62"):
                opp_val = getattr(old_value, "docl_OclType62", None)
                if opp_val == self:
                    setattr(old_value, "docl_OclType62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "docl_OclType62"):
                opp_val = getattr(value, "docl_OclType62", None)
                setattr(value, "docl_OclType62", self)

class docl_SetType(OclType):

    def __init__(self, name: str, docl_SetType: "docl_OclType" = None):
        self.name = name
        self.docl_SetType = docl_SetType
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def docl_SetType(self):
        return self.__docl_SetType

    @docl_SetType.setter
    def docl_SetType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_docl_SetType__docl_SetType", None)
        self.__docl_SetType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "docl_OclType58"):
                opp_val = getattr(old_value, "docl_OclType58", None)
                if opp_val == self:
                    setattr(old_value, "docl_OclType58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "docl_OclType58"):
                opp_val = getattr(value, "docl_OclType58", None)
                setattr(value, "docl_OclType58", self)

class docl_EnvType(OclType):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class docl_MapType(OclType):

    def __init__(self, name: str, docl_MapType: "docl_OclType" = None, docl_MapType55: "docl_OclType" = None):
        self.name = name
        self.docl_MapType = docl_MapType
        self.docl_MapType55 = docl_MapType55
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def docl_MapType(self):
        return self.__docl_MapType

    @docl_MapType.setter
    def docl_MapType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_docl_MapType__docl_MapType", None)
        self.__docl_MapType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "docl_OclType53"):
                opp_val = getattr(old_value, "docl_OclType53", None)
                if opp_val == self:
                    setattr(old_value, "docl_OclType53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "docl_OclType53"):
                opp_val = getattr(value, "docl_OclType53", None)
                setattr(value, "docl_OclType53", self)

    @property
    def docl_MapType55(self):
        return self.__docl_MapType55

    @docl_MapType55.setter
    def docl_MapType55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_docl_MapType__docl_MapType55", None)
        self.__docl_MapType55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "docl_OclType56"):
                opp_val = getattr(old_value, "docl_OclType56", None)
                if opp_val == self:
                    setattr(old_value, "docl_OclType56", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "docl_OclType56"):
                opp_val = getattr(value, "docl_OclType56", None)
                setattr(value, "docl_OclType56", self)

class docl_BagType(OclType):

    def __init__(self, name: str, docl_BagType: "docl_OclType" = None):
        self.name = name
        self.docl_BagType = docl_BagType
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def docl_BagType(self):
        return self.__docl_BagType

    @docl_BagType.setter
    def docl_BagType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_docl_BagType__docl_BagType", None)
        self.__docl_BagType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "docl_OclType64"):
                opp_val = getattr(old_value, "docl_OclType64", None)
                if opp_val == self:
                    setattr(old_value, "docl_OclType64", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "docl_OclType64"):
                opp_val = getattr(value, "docl_OclType64", None)
                setattr(value, "docl_OclType64", self)

class docl_SequenceType(OclType):

    def __init__(self, name: str, docl_SequenceType: "docl_OclType" = None):
        self.name = name
        self.docl_SequenceType = docl_SequenceType
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def docl_SequenceType(self):
        return self.__docl_SequenceType

    @docl_SequenceType.setter
    def docl_SequenceType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_docl_SequenceType__docl_SequenceType", None)
        self.__docl_SequenceType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "docl_OclType60"):
                opp_val = getattr(old_value, "docl_OclType60", None)
                if opp_val == self:
                    setattr(old_value, "docl_OclType60", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "docl_OclType60"):
                opp_val = getattr(value, "docl_OclType60", None)
                setattr(value, "docl_OclType60", self)

class docl_OclModelElementExp(OclType):

    def __init__(self, name: str, docl_OclModelElementExp: "docl_OclModel" = None):
        self.name = name
        self.docl_OclModelElementExp = docl_OclModelElementExp
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def docl_OclModelElementExp(self):
        return self.__docl_OclModelElementExp

    @docl_OclModelElementExp.setter
    def docl_OclModelElementExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_docl_OclModelElementExp__docl_OclModelElementExp", None)
        self.__docl_OclModelElementExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "docl_OclModel46"):
                opp_val = getattr(old_value, "docl_OclModel46", None)
                if opp_val == self:
                    setattr(old_value, "docl_OclModel46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "docl_OclModel46"):
                opp_val = getattr(value, "docl_OclModel46", None)
                setattr(value, "docl_OclModel46", self)

class PrimitiveExp:

    pass
class docl_BooleanLiteralExp(PrimitiveExp):

    def __init__(self, symbol: str):
        self.symbol = symbol
        
    @property
    def symbol(self) -> str:
        return self.__symbol

    @symbol.setter
    def symbol(self, symbol: str):
        self.__symbol = symbol

class docl_UnlimitedNaturalLiteralExp(PrimitiveExp):

    pass
class docl_InvalidLiteralExp(PrimitiveExp):

    pass
class docl_NullLiteralExp(PrimitiveExp):

    pass
class docl_StringLiteralExp(PrimitiveExp):

    def __init__(self, segments: str):
        self.segments = segments
        
    @property
    def segments(self) -> str:
        return self.__segments

    @segments.setter
    def segments(self, segments: str):
        self.__segments = segments

class docl_NumberLiteralExp(PrimitiveExp):

    def __init__(self, symbol: int):
        self.symbol = symbol
        
    @property
    def symbol(self) -> int:
        return self.__symbol

    @symbol.setter
    def symbol(self, symbol: int):
        self.__symbol = symbol

class OclExpression:

    pass
class docl_NestedExp(OclExpression):

    pass
class docl_EqOpCallExp(OclExpression):

    pass
class docl_ElseIfThenExp(OclExpression):

    pass
class docl_IteratorExp(OclExpression):

    pass
class docl_NavigationOrAttributeCall(OclExpression):

    def __init__(self, feature: str):
        self.feature = feature
        
    @property
    def feature(self) -> str:
        return self.__feature

    @feature.setter
    def feature(self, feature: str):
        self.__feature = feature

class docl_BoolOpCallExp(OclExpression):

    pass
class docl_CollectionOpCallExp(OclExpression):

    pass
class docl_IterateExp(OclExpression):

    pass
class docl_AddOpCallExp(OclExpression):

    pass
class docl_LambdaExp(OclExpression):

    pass
class docl_ComOpCallExp(OclExpression):

    pass
class docl_TupleExp(OclExpression):

    pass
class docl_MulOpCallExp(OclExpression):

    pass
class docl_NavigationExp(OclExpression):

    pass
class docl_SelfExp(OclExpression):

    pass
class docl_IfExp(OclExpression):

    pass
class docl_OperationCall(OclExpression):

    pass
class docl_PrimitiveExp(OclExpression):

    pass
class docl_LambdaType(OclType):

    def __init__(self, name: str, docl_LambdaType: set["docl_OclType"] = None, docl_LambdaType50: "docl_OclType" = None):
        self.name = name
        self.docl_LambdaType = docl_LambdaType if docl_LambdaType is not None else set()
        self.docl_LambdaType50 = docl_LambdaType50
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def docl_LambdaType(self):
        return self.__docl_LambdaType

    @docl_LambdaType.setter
    def docl_LambdaType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_docl_LambdaType__docl_LambdaType", None)
        self.__docl_LambdaType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "docl_OclType48"):
                    opp_val = getattr(item, "docl_OclType48", None)
                    
                    if opp_val == self:
                        setattr(item, "docl_OclType48", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "docl_OclType48"):
                    opp_val = getattr(item, "docl_OclType48", None)
                    
                    setattr(item, "docl_OclType48", self)
                    

    @property
    def docl_LambdaType50(self):
        return self.__docl_LambdaType50

    @docl_LambdaType50.setter
    def docl_LambdaType50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_docl_LambdaType__docl_LambdaType50", None)
        self.__docl_LambdaType50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "docl_OclType51"):
                opp_val = getattr(old_value, "docl_OclType51", None)
                if opp_val == self:
                    setattr(old_value, "docl_OclType51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "docl_OclType51"):
                opp_val = getattr(value, "docl_OclType51", None)
                setattr(value, "docl_OclType51", self)

class docl_OclType:

    pass
class docl_Iterator:

    def __init__(self, name: str, docl_Iterator: "docl_OclType" = None, docl_Iterator80: "docl_IterateExp" = None, docl_Iterator88: "docl_IteratorExp" = None):
        self.name = name
        self.docl_Iterator = docl_Iterator
        self.docl_Iterator80 = docl_Iterator80
        self.docl_Iterator88 = docl_Iterator88
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def docl_Iterator88(self):
        return self.__docl_Iterator88

    @docl_Iterator88.setter
    def docl_Iterator88(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_docl_Iterator__docl_Iterator88", None)
        self.__docl_Iterator88 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "docl_IteratorExp"):
                opp_val = getattr(old_value, "docl_IteratorExp", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "docl_IteratorExp"):
                opp_val = getattr(value, "docl_IteratorExp", None)
                if opp_val is None:
                    setattr(value, "docl_IteratorExp", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def docl_Iterator(self):
        return self.__docl_Iterator

    @docl_Iterator.setter
    def docl_Iterator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_docl_Iterator__docl_Iterator", None)
        self.__docl_Iterator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "docl_OclType"):
                opp_val = getattr(old_value, "docl_OclType", None)
                if opp_val == self:
                    setattr(old_value, "docl_OclType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "docl_OclType"):
                opp_val = getattr(value, "docl_OclType", None)
                setattr(value, "docl_OclType", self)

    @property
    def docl_Iterator80(self):
        return self.__docl_Iterator80

    @docl_Iterator80.setter
    def docl_Iterator80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_docl_Iterator__docl_Iterator80", None)
        self.__docl_Iterator80 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "docl_IterateExp"):
                opp_val = getattr(old_value, "docl_IterateExp", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "docl_IterateExp"):
                opp_val = getattr(value, "docl_IterateExp", None)
                if opp_val is None:
                    setattr(value, "docl_IterateExp", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class docl_LocalVariable:

    def __init__(self, name: str, docl_LocalVariable: "docl_OclExpression" = None, docl_LocalVariable24: "docl_OclType" = None, docl_LocalVariable27: "docl_OclExpression" = None, docl_LocalVariable83: "docl_IterateExp" = None):
        self.name = name
        self.docl_LocalVariable = docl_LocalVariable
        self.docl_LocalVariable24 = docl_LocalVariable24
        self.docl_LocalVariable27 = docl_LocalVariable27
        self.docl_LocalVariable83 = docl_LocalVariable83
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def docl_LocalVariable24(self):
        return self.__docl_LocalVariable24

    @docl_LocalVariable24.setter
    def docl_LocalVariable24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_docl_LocalVariable__docl_LocalVariable24", None)
        self.__docl_LocalVariable24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "docl_OclType25"):
                opp_val = getattr(old_value, "docl_OclType25", None)
                if opp_val == self:
                    setattr(old_value, "docl_OclType25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "docl_OclType25"):
                opp_val = getattr(value, "docl_OclType25", None)
                setattr(value, "docl_OclType25", self)

    @property
    def docl_LocalVariable(self):
        return self.__docl_LocalVariable

    @docl_LocalVariable.setter
    def docl_LocalVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_docl_LocalVariable__docl_LocalVariable", None)
        self.__docl_LocalVariable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "docl_OclExpression12"):
                opp_val = getattr(old_value, "docl_OclExpression12", None)
                if opp_val == self:
                    setattr(old_value, "docl_OclExpression12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "docl_OclExpression12"):
                opp_val = getattr(value, "docl_OclExpression12", None)
                setattr(value, "docl_OclExpression12", self)

    @property
    def docl_LocalVariable27(self):
        return self.__docl_LocalVariable27

    @docl_LocalVariable27.setter
    def docl_LocalVariable27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_docl_LocalVariable__docl_LocalVariable27", None)
        self.__docl_LocalVariable27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "docl_OclExpression28"):
                opp_val = getattr(old_value, "docl_OclExpression28", None)
                if opp_val == self:
                    setattr(old_value, "docl_OclExpression28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "docl_OclExpression28"):
                opp_val = getattr(value, "docl_OclExpression28", None)
                setattr(value, "docl_OclExpression28", self)

    @property
    def docl_LocalVariable83(self):
        return self.__docl_LocalVariable83

    @docl_LocalVariable83.setter
    def docl_LocalVariable83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_docl_LocalVariable__docl_LocalVariable83", None)
        self.__docl_LocalVariable83 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "docl_IterateExp82"):
                opp_val = getattr(old_value, "docl_IterateExp82", None)
                if opp_val == self:
                    setattr(old_value, "docl_IterateExp82", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "docl_IterateExp82"):
                opp_val = getattr(value, "docl_IterateExp82", None)
                setattr(value, "docl_IterateExp82", self)

class docl_OclExpression:

    def __init__(self, name: str, elements: str, docl_OclExpression: "docl_Query" = None, docl_OclExpression12: "docl_LocalVariable" = None, docl_OclExpression15: "docl_OclExpression" = None, docl_OclExpression13: "docl_OclExpression" = None, docl_OclExpression18: "docl_OclExpression" = None, docl_OclExpression16: "docl_OclExpression" = None, docl_OclExpression20: "docl_OclModel" = None, docl_OclExpression28: "docl_LocalVariable" = None, docl_OclExpression33: "docl_TuplePart" = None, docl_OclExpression35: "docl_IfExp" = None, docl_OclExpression38: "docl_IfExp" = None, docl_OclExpression41: "docl_IfExp" = None, docl_OclExpression44: "docl_IfExp" = None, docl_OclExpression66: "docl_BoolOpCallExp" = None, docl_OclExpression68: "docl_EqOpCallExp" = None, docl_OclExpression70: "docl_ComOpCallExp" = None, docl_OclExpression72: "docl_AddOpCallExp" = None, docl_OclExpression74: "docl_MulOpCallExp" = None, docl_OclExpression76: "docl_NavigationExp" = None, docl_OclExpression78: "docl_CollectionOpCallExp" = None, docl_OclExpression104: "docl_NestedExp" = None, docl_OclExpression86: "docl_IterateExp" = None, docl_OclExpression91: "docl_IteratorExp" = None, docl_OclExpression93: "docl_OperationCall" = None, docl_OclExpression95: "docl_LambdaExp" = None, docl_OclExpression99: "docl_ElseIfThenExp" = None, docl_OclExpression102: "docl_ElseIfThenExp" = None):
        self.name = name
        self.elements = elements
        self.docl_OclExpression = docl_OclExpression
        self.docl_OclExpression12 = docl_OclExpression12
        self.docl_OclExpression15 = docl_OclExpression15
        self.docl_OclExpression13 = docl_OclExpression13
        self.docl_OclExpression18 = docl_OclExpression18
        self.docl_OclExpression16 = docl_OclExpression16
        self.docl_OclExpression20 = docl_OclExpression20
        self.docl_OclExpression28 = docl_OclExpression28
        self.docl_OclExpression33 = docl_OclExpression33
        self.docl_OclExpression35 = docl_OclExpression35
        self.docl_OclExpression38 = docl_OclExpression38
        self.docl_OclExpression41 = docl_OclExpression41
        self.docl_OclExpression44 = docl_OclExpression44
        self.docl_OclExpression66 = docl_OclExpression66
        self.docl_OclExpression68 = docl_OclExpression68
        self.docl_OclExpression70 = docl_OclExpression70
        self.docl_OclExpression72 = docl_OclExpression72
        self.docl_OclExpression74 = docl_OclExpression74
        self.docl_OclExpression76 = docl_OclExpression76
        self.docl_OclExpression78 = docl_OclExpression78
        self.docl_OclExpression104 = docl_OclExpression104
        self.docl_OclExpression86 = docl_OclExpression86
        self.docl_OclExpression91 = docl_OclExpression91
        self.docl_OclExpression93 = docl_OclExpression93
        self.docl_OclExpression95 = docl_OclExpression95
        self.docl_OclExpression99 = docl_OclExpression99
        self.docl_OclExpression102 = docl_OclExpression102
        
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
    def docl_OclExpression99(self):
        return self.__docl_OclExpression99

    @docl_OclExpression99.setter
    def docl_OclExpression99(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_docl_OclExpression__docl_OclExpression99", None)
        self.__docl_OclExpression99 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "docl_ElseIfThenExp"):
                opp_val = getattr(old_value, "docl_ElseIfThenExp", None)
                if opp_val == self:
                    setattr(old_value, "docl_ElseIfThenExp", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "docl_ElseIfThenExp"):
                opp_val = getattr(value, "docl_ElseIfThenExp", None)
                setattr(value, "docl_ElseIfThenExp", self)

    @property
    def docl_OclExpression20(self):
        return self.__docl_OclExpression20

    @docl_OclExpression20.setter
    def docl_OclExpression20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_docl_OclExpression__docl_OclExpression20", None)
        self.__docl_OclExpression20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "docl_OclModel21"):
                opp_val = getattr(old_value, "docl_OclModel21", None)
                if opp_val == self:
                    setattr(old_value, "docl_OclModel21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "docl_OclModel21"):
                opp_val = getattr(value, "docl_OclModel21", None)
                setattr(value, "docl_OclModel21", self)

    @property
    def docl_OclExpression93(self):
        return self.__docl_OclExpression93

    @docl_OclExpression93.setter
    def docl_OclExpression93(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_docl_OclExpression__docl_OclExpression93", None)
        self.__docl_OclExpression93 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "docl_OperationCall"):
                opp_val = getattr(old_value, "docl_OperationCall", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "docl_OperationCall"):
                opp_val = getattr(value, "docl_OperationCall", None)
                if opp_val is None:
                    setattr(value, "docl_OperationCall", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def docl_OclExpression18(self):
        return self.__docl_OclExpression18

    @docl_OclExpression18.setter
    def docl_OclExpression18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_docl_OclExpression__docl_OclExpression18", None)
        self.__docl_OclExpression18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "docl_OclExpression16"):
                opp_val = getattr(old_value, "docl_OclExpression16", None)
                if opp_val == self:
                    setattr(old_value, "docl_OclExpression16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "docl_OclExpression16"):
                opp_val = getattr(value, "docl_OclExpression16", None)
                setattr(value, "docl_OclExpression16", self)

    @property
    def docl_OclExpression86(self):
        return self.__docl_OclExpression86

    @docl_OclExpression86.setter
    def docl_OclExpression86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_docl_OclExpression__docl_OclExpression86", None)
        self.__docl_OclExpression86 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "docl_IterateExp85"):
                opp_val = getattr(old_value, "docl_IterateExp85", None)
                if opp_val == self:
                    setattr(old_value, "docl_IterateExp85", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "docl_IterateExp85"):
                opp_val = getattr(value, "docl_IterateExp85", None)
                setattr(value, "docl_IterateExp85", self)

    @property
    def docl_OclExpression12(self):
        return self.__docl_OclExpression12

    @docl_OclExpression12.setter
    def docl_OclExpression12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_docl_OclExpression__docl_OclExpression12", None)
        self.__docl_OclExpression12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "docl_LocalVariable"):
                opp_val = getattr(old_value, "docl_LocalVariable", None)
                if opp_val == self:
                    setattr(old_value, "docl_LocalVariable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "docl_LocalVariable"):
                opp_val = getattr(value, "docl_LocalVariable", None)
                setattr(value, "docl_LocalVariable", self)

    @property
    def docl_OclExpression41(self):
        return self.__docl_OclExpression41

    @docl_OclExpression41.setter
    def docl_OclExpression41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_docl_OclExpression__docl_OclExpression41", None)
        self.__docl_OclExpression41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "docl_IfExp40"):
                opp_val = getattr(old_value, "docl_IfExp40", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "docl_IfExp40"):
                opp_val = getattr(value, "docl_IfExp40", None)
                if opp_val is None:
                    setattr(value, "docl_IfExp40", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def docl_OclExpression16(self):
        return self.__docl_OclExpression16

    @docl_OclExpression16.setter
    def docl_OclExpression16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_docl_OclExpression__docl_OclExpression16", None)
        self.__docl_OclExpression16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "docl_OclExpression18"):
                opp_val = getattr(old_value, "docl_OclExpression18", None)
                if opp_val == self:
                    setattr(old_value, "docl_OclExpression18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "docl_OclExpression18"):
                opp_val = getattr(value, "docl_OclExpression18", None)
                setattr(value, "docl_OclExpression18", self)

    @property
    def docl_OclExpression95(self):
        return self.__docl_OclExpression95

    @docl_OclExpression95.setter
    def docl_OclExpression95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_docl_OclExpression__docl_OclExpression95", None)
        self.__docl_OclExpression95 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "docl_LambdaExp"):
                opp_val = getattr(old_value, "docl_LambdaExp", None)
                if opp_val == self:
                    setattr(old_value, "docl_LambdaExp", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "docl_LambdaExp"):
                opp_val = getattr(value, "docl_LambdaExp", None)
                setattr(value, "docl_LambdaExp", self)

    @property
    def docl_OclExpression15(self):
        return self.__docl_OclExpression15

    @docl_OclExpression15.setter
    def docl_OclExpression15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_docl_OclExpression__docl_OclExpression15", None)
        self.__docl_OclExpression15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "docl_OclExpression13"):
                opp_val = getattr(old_value, "docl_OclExpression13", None)
                if opp_val == self:
                    setattr(old_value, "docl_OclExpression13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "docl_OclExpression13"):
                opp_val = getattr(value, "docl_OclExpression13", None)
                setattr(value, "docl_OclExpression13", self)

    @property
    def docl_OclExpression38(self):
        return self.__docl_OclExpression38

    @docl_OclExpression38.setter
    def docl_OclExpression38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_docl_OclExpression__docl_OclExpression38", None)
        self.__docl_OclExpression38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "docl_IfExp37"):
                opp_val = getattr(old_value, "docl_IfExp37", None)
                if opp_val == self:
                    setattr(old_value, "docl_IfExp37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "docl_IfExp37"):
                opp_val = getattr(value, "docl_IfExp37", None)
                setattr(value, "docl_IfExp37", self)

    @property
    def docl_OclExpression70(self):
        return self.__docl_OclExpression70

    @docl_OclExpression70.setter
    def docl_OclExpression70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_docl_OclExpression__docl_OclExpression70", None)
        self.__docl_OclExpression70 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "docl_ComOpCallExp"):
                opp_val = getattr(old_value, "docl_ComOpCallExp", None)
                if opp_val == self:
                    setattr(old_value, "docl_ComOpCallExp", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "docl_ComOpCallExp"):
                opp_val = getattr(value, "docl_ComOpCallExp", None)
                setattr(value, "docl_ComOpCallExp", self)

    @property
    def docl_OclExpression28(self):
        return self.__docl_OclExpression28

    @docl_OclExpression28.setter
    def docl_OclExpression28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_docl_OclExpression__docl_OclExpression28", None)
        self.__docl_OclExpression28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "docl_LocalVariable27"):
                opp_val = getattr(old_value, "docl_LocalVariable27", None)
                if opp_val == self:
                    setattr(old_value, "docl_LocalVariable27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "docl_LocalVariable27"):
                opp_val = getattr(value, "docl_LocalVariable27", None)
                setattr(value, "docl_LocalVariable27", self)

    @property
    def docl_OclExpression78(self):
        return self.__docl_OclExpression78

    @docl_OclExpression78.setter
    def docl_OclExpression78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_docl_OclExpression__docl_OclExpression78", None)
        self.__docl_OclExpression78 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "docl_CollectionOpCallExp"):
                opp_val = getattr(old_value, "docl_CollectionOpCallExp", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "docl_CollectionOpCallExp"):
                opp_val = getattr(value, "docl_CollectionOpCallExp", None)
                if opp_val is None:
                    setattr(value, "docl_CollectionOpCallExp", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def docl_OclExpression104(self):
        return self.__docl_OclExpression104

    @docl_OclExpression104.setter
    def docl_OclExpression104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_docl_OclExpression__docl_OclExpression104", None)
        self.__docl_OclExpression104 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "docl_NestedExp"):
                opp_val = getattr(old_value, "docl_NestedExp", None)
                if opp_val == self:
                    setattr(old_value, "docl_NestedExp", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "docl_NestedExp"):
                opp_val = getattr(value, "docl_NestedExp", None)
                setattr(value, "docl_NestedExp", self)

    @property
    def docl_OclExpression(self):
        return self.__docl_OclExpression

    @docl_OclExpression.setter
    def docl_OclExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_docl_OclExpression__docl_OclExpression", None)
        self.__docl_OclExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "docl_Query"):
                opp_val = getattr(old_value, "docl_Query", None)
                if opp_val == self:
                    setattr(old_value, "docl_Query", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "docl_Query"):
                opp_val = getattr(value, "docl_Query", None)
                setattr(value, "docl_Query", self)

    @property
    def docl_OclExpression74(self):
        return self.__docl_OclExpression74

    @docl_OclExpression74.setter
    def docl_OclExpression74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_docl_OclExpression__docl_OclExpression74", None)
        self.__docl_OclExpression74 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "docl_MulOpCallExp"):
                opp_val = getattr(old_value, "docl_MulOpCallExp", None)
                if opp_val == self:
                    setattr(old_value, "docl_MulOpCallExp", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "docl_MulOpCallExp"):
                opp_val = getattr(value, "docl_MulOpCallExp", None)
                setattr(value, "docl_MulOpCallExp", self)

    @property
    def docl_OclExpression102(self):
        return self.__docl_OclExpression102

    @docl_OclExpression102.setter
    def docl_OclExpression102(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_docl_OclExpression__docl_OclExpression102", None)
        self.__docl_OclExpression102 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "docl_ElseIfThenExp101"):
                opp_val = getattr(old_value, "docl_ElseIfThenExp101", None)
                if opp_val == self:
                    setattr(old_value, "docl_ElseIfThenExp101", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "docl_ElseIfThenExp101"):
                opp_val = getattr(value, "docl_ElseIfThenExp101", None)
                setattr(value, "docl_ElseIfThenExp101", self)

    @property
    def docl_OclExpression68(self):
        return self.__docl_OclExpression68

    @docl_OclExpression68.setter
    def docl_OclExpression68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_docl_OclExpression__docl_OclExpression68", None)
        self.__docl_OclExpression68 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "docl_EqOpCallExp"):
                opp_val = getattr(old_value, "docl_EqOpCallExp", None)
                if opp_val == self:
                    setattr(old_value, "docl_EqOpCallExp", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "docl_EqOpCallExp"):
                opp_val = getattr(value, "docl_EqOpCallExp", None)
                setattr(value, "docl_EqOpCallExp", self)

    @property
    def docl_OclExpression91(self):
        return self.__docl_OclExpression91

    @docl_OclExpression91.setter
    def docl_OclExpression91(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_docl_OclExpression__docl_OclExpression91", None)
        self.__docl_OclExpression91 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "docl_IteratorExp90"):
                opp_val = getattr(old_value, "docl_IteratorExp90", None)
                if opp_val == self:
                    setattr(old_value, "docl_IteratorExp90", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "docl_IteratorExp90"):
                opp_val = getattr(value, "docl_IteratorExp90", None)
                setattr(value, "docl_IteratorExp90", self)

    @property
    def docl_OclExpression76(self):
        return self.__docl_OclExpression76

    @docl_OclExpression76.setter
    def docl_OclExpression76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_docl_OclExpression__docl_OclExpression76", None)
        self.__docl_OclExpression76 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "docl_NavigationExp"):
                opp_val = getattr(old_value, "docl_NavigationExp", None)
                if opp_val == self:
                    setattr(old_value, "docl_NavigationExp", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "docl_NavigationExp"):
                opp_val = getattr(value, "docl_NavigationExp", None)
                setattr(value, "docl_NavigationExp", self)

    @property
    def docl_OclExpression44(self):
        return self.__docl_OclExpression44

    @docl_OclExpression44.setter
    def docl_OclExpression44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_docl_OclExpression__docl_OclExpression44", None)
        self.__docl_OclExpression44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "docl_IfExp43"):
                opp_val = getattr(old_value, "docl_IfExp43", None)
                if opp_val == self:
                    setattr(old_value, "docl_IfExp43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "docl_IfExp43"):
                opp_val = getattr(value, "docl_IfExp43", None)
                setattr(value, "docl_IfExp43", self)

    @property
    def docl_OclExpression72(self):
        return self.__docl_OclExpression72

    @docl_OclExpression72.setter
    def docl_OclExpression72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_docl_OclExpression__docl_OclExpression72", None)
        self.__docl_OclExpression72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "docl_AddOpCallExp"):
                opp_val = getattr(old_value, "docl_AddOpCallExp", None)
                if opp_val == self:
                    setattr(old_value, "docl_AddOpCallExp", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "docl_AddOpCallExp"):
                opp_val = getattr(value, "docl_AddOpCallExp", None)
                setattr(value, "docl_AddOpCallExp", self)

    @property
    def docl_OclExpression33(self):
        return self.__docl_OclExpression33

    @docl_OclExpression33.setter
    def docl_OclExpression33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_docl_OclExpression__docl_OclExpression33", None)
        self.__docl_OclExpression33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "docl_TuplePart32"):
                opp_val = getattr(old_value, "docl_TuplePart32", None)
                if opp_val == self:
                    setattr(old_value, "docl_TuplePart32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "docl_TuplePart32"):
                opp_val = getattr(value, "docl_TuplePart32", None)
                setattr(value, "docl_TuplePart32", self)

    @property
    def docl_OclExpression13(self):
        return self.__docl_OclExpression13

    @docl_OclExpression13.setter
    def docl_OclExpression13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_docl_OclExpression__docl_OclExpression13", None)
        self.__docl_OclExpression13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "docl_OclExpression15"):
                opp_val = getattr(old_value, "docl_OclExpression15", None)
                if opp_val == self:
                    setattr(old_value, "docl_OclExpression15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "docl_OclExpression15"):
                opp_val = getattr(value, "docl_OclExpression15", None)
                setattr(value, "docl_OclExpression15", self)

    @property
    def docl_OclExpression66(self):
        return self.__docl_OclExpression66

    @docl_OclExpression66.setter
    def docl_OclExpression66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_docl_OclExpression__docl_OclExpression66", None)
        self.__docl_OclExpression66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "docl_BoolOpCallExp"):
                opp_val = getattr(old_value, "docl_BoolOpCallExp", None)
                if opp_val == self:
                    setattr(old_value, "docl_BoolOpCallExp", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "docl_BoolOpCallExp"):
                opp_val = getattr(value, "docl_BoolOpCallExp", None)
                setattr(value, "docl_BoolOpCallExp", self)

    @property
    def docl_OclExpression35(self):
        return self.__docl_OclExpression35

    @docl_OclExpression35.setter
    def docl_OclExpression35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_docl_OclExpression__docl_OclExpression35", None)
        self.__docl_OclExpression35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "docl_IfExp"):
                opp_val = getattr(old_value, "docl_IfExp", None)
                if opp_val == self:
                    setattr(old_value, "docl_IfExp", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "docl_IfExp"):
                opp_val = getattr(value, "docl_IfExp", None)
                setattr(value, "docl_IfExp", self)

class ModuleElement:

    pass
class docl_Query(ModuleElement):

    def __init__(self, name: str, docl_Query: "docl_OclExpression" = None):
        self.name = name
        self.docl_Query = docl_Query
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def docl_Query(self):
        return self.__docl_Query

    @docl_Query.setter
    def docl_Query(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_docl_Query__docl_Query", None)
        self.__docl_Query = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "docl_OclExpression"):
                opp_val = getattr(old_value, "docl_OclExpression", None)
                if opp_val == self:
                    setattr(old_value, "docl_OclExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "docl_OclExpression"):
                opp_val = getattr(value, "docl_OclExpression", None)
                setattr(value, "docl_OclExpression", self)

class docl_URI_:

    def __init__(self, scheme: str, authority: str, fragment_: str, docl_URI_: "docl_OclModel" = None):
        self.scheme = scheme
        self.authority = authority
        self.fragment_ = fragment_
        self.docl_URI_ = docl_URI_
        
    @property
    def fragment_(self) -> str:
        return self.__fragment_

    @fragment_.setter
    def fragment_(self, fragment_: str):
        self.__fragment_ = fragment_

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
    def docl_URI_(self):
        return self.__docl_URI_

    @docl_URI_.setter
    def docl_URI_(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_docl_URI___docl_URI_", None)
        self.__docl_URI_ = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "docl_OclModel9"):
                opp_val = getattr(old_value, "docl_OclModel9", None)
                if opp_val == self:
                    setattr(old_value, "docl_OclModel9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "docl_OclModel9"):
                opp_val = getattr(value, "docl_OclModel9", None)
                setattr(value, "docl_OclModel9", self)

class docl_TuplePart:

    def __init__(self, name: str, docl_TuplePart: "docl_OclType" = None, docl_TuplePart32: "docl_OclExpression" = None, docl_TuplePart97: "docl_TupleExp" = None):
        self.name = name
        self.docl_TuplePart = docl_TuplePart
        self.docl_TuplePart32 = docl_TuplePart32
        self.docl_TuplePart97 = docl_TuplePart97
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def docl_TuplePart32(self):
        return self.__docl_TuplePart32

    @docl_TuplePart32.setter
    def docl_TuplePart32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_docl_TuplePart__docl_TuplePart32", None)
        self.__docl_TuplePart32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "docl_OclExpression33"):
                opp_val = getattr(old_value, "docl_OclExpression33", None)
                if opp_val == self:
                    setattr(old_value, "docl_OclExpression33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "docl_OclExpression33"):
                opp_val = getattr(value, "docl_OclExpression33", None)
                setattr(value, "docl_OclExpression33", self)

    @property
    def docl_TuplePart97(self):
        return self.__docl_TuplePart97

    @docl_TuplePart97.setter
    def docl_TuplePart97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_docl_TuplePart__docl_TuplePart97", None)
        self.__docl_TuplePart97 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "docl_TupleExp"):
                opp_val = getattr(old_value, "docl_TupleExp", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "docl_TupleExp"):
                opp_val = getattr(value, "docl_TupleExp", None)
                if opp_val is None:
                    setattr(value, "docl_TupleExp", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def docl_TuplePart(self):
        return self.__docl_TuplePart

    @docl_TuplePart.setter
    def docl_TuplePart(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_docl_TuplePart__docl_TuplePart", None)
        self.__docl_TuplePart = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "docl_OclType30"):
                opp_val = getattr(old_value, "docl_OclType30", None)
                if opp_val == self:
                    setattr(old_value, "docl_OclType30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "docl_OclType30"):
                opp_val = getattr(value, "docl_OclType30", None)
                setattr(value, "docl_OclType30", self)

class docl_Import:

    def __init__(self, name: str, docl_Import: "docl_Module" = None):
        self.name = name
        self.docl_Import = docl_Import
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def docl_Import(self):
        return self.__docl_Import

    @docl_Import.setter
    def docl_Import(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_docl_Import__docl_Import", None)
        self.__docl_Import = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "docl_Module5"):
                opp_val = getattr(old_value, "docl_Module5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "docl_Module5"):
                opp_val = getattr(value, "docl_Module5", None)
                if opp_val is None:
                    setattr(value, "docl_Module5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class docl_OclModel:

    def __init__(self, name: str, docl_OclModel: "docl_Module" = None, docl_OclModel3: "docl_Module" = None, docl_OclModel9: "docl_URI_" = None, docl_OclModel21: "docl_OclExpression" = None, docl_OclModel46: "docl_OclModelElementExp" = None):
        self.name = name
        self.docl_OclModel = docl_OclModel
        self.docl_OclModel3 = docl_OclModel3
        self.docl_OclModel9 = docl_OclModel9
        self.docl_OclModel21 = docl_OclModel21
        self.docl_OclModel46 = docl_OclModel46
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def docl_OclModel9(self):
        return self.__docl_OclModel9

    @docl_OclModel9.setter
    def docl_OclModel9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_docl_OclModel__docl_OclModel9", None)
        self.__docl_OclModel9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "docl_URI_"):
                opp_val = getattr(old_value, "docl_URI_", None)
                if opp_val == self:
                    setattr(old_value, "docl_URI_", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "docl_URI_"):
                opp_val = getattr(value, "docl_URI_", None)
                setattr(value, "docl_URI_", self)

    @property
    def docl_OclModel21(self):
        return self.__docl_OclModel21

    @docl_OclModel21.setter
    def docl_OclModel21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_docl_OclModel__docl_OclModel21", None)
        self.__docl_OclModel21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "docl_OclExpression20"):
                opp_val = getattr(old_value, "docl_OclExpression20", None)
                if opp_val == self:
                    setattr(old_value, "docl_OclExpression20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "docl_OclExpression20"):
                opp_val = getattr(value, "docl_OclExpression20", None)
                setattr(value, "docl_OclExpression20", self)

    @property
    def docl_OclModel3(self):
        return self.__docl_OclModel3

    @docl_OclModel3.setter
    def docl_OclModel3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_docl_OclModel__docl_OclModel3", None)
        self.__docl_OclModel3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "docl_Module2"):
                opp_val = getattr(old_value, "docl_Module2", None)
                if opp_val == self:
                    setattr(old_value, "docl_Module2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "docl_Module2"):
                opp_val = getattr(value, "docl_Module2", None)
                setattr(value, "docl_Module2", self)

    @property
    def docl_OclModel46(self):
        return self.__docl_OclModel46

    @docl_OclModel46.setter
    def docl_OclModel46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_docl_OclModel__docl_OclModel46", None)
        self.__docl_OclModel46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "docl_OclModelElementExp"):
                opp_val = getattr(old_value, "docl_OclModelElementExp", None)
                if opp_val == self:
                    setattr(old_value, "docl_OclModelElementExp", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "docl_OclModelElementExp"):
                opp_val = getattr(value, "docl_OclModelElementExp", None)
                setattr(value, "docl_OclModelElementExp", self)

    @property
    def docl_OclModel(self):
        return self.__docl_OclModel

    @docl_OclModel.setter
    def docl_OclModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_docl_OclModel__docl_OclModel", None)
        self.__docl_OclModel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "docl_Module"):
                opp_val = getattr(old_value, "docl_Module", None)
                if opp_val == self:
                    setattr(old_value, "docl_Module", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "docl_Module"):
                opp_val = getattr(value, "docl_Module", None)
                setattr(value, "docl_Module", self)

class docl_Module:

    def __init__(self, name: str, docl_Module7: set["docl_ModuleElement"] = None, docl_Module: "docl_OclModel" = None, docl_Module2: "docl_OclModel" = None, docl_Module5: set["docl_Import"] = None):
        self.name = name
        self.docl_Module7 = docl_Module7 if docl_Module7 is not None else set()
        self.docl_Module = docl_Module
        self.docl_Module2 = docl_Module2
        self.docl_Module5 = docl_Module5 if docl_Module5 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def docl_Module2(self):
        return self.__docl_Module2

    @docl_Module2.setter
    def docl_Module2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_docl_Module__docl_Module2", None)
        self.__docl_Module2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "docl_OclModel3"):
                opp_val = getattr(old_value, "docl_OclModel3", None)
                if opp_val == self:
                    setattr(old_value, "docl_OclModel3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "docl_OclModel3"):
                opp_val = getattr(value, "docl_OclModel3", None)
                setattr(value, "docl_OclModel3", self)

    @property
    def docl_Module5(self):
        return self.__docl_Module5

    @docl_Module5.setter
    def docl_Module5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_docl_Module__docl_Module5", None)
        self.__docl_Module5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "docl_Import"):
                    opp_val = getattr(item, "docl_Import", None)
                    
                    if opp_val == self:
                        setattr(item, "docl_Import", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "docl_Import"):
                    opp_val = getattr(item, "docl_Import", None)
                    
                    setattr(item, "docl_Import", self)
                    

    @property
    def docl_Module7(self):
        return self.__docl_Module7

    @docl_Module7.setter
    def docl_Module7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_docl_Module__docl_Module7", None)
        self.__docl_Module7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "docl_ModuleElement"):
                    opp_val = getattr(item, "docl_ModuleElement", None)
                    
                    if opp_val == self:
                        setattr(item, "docl_ModuleElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "docl_ModuleElement"):
                    opp_val = getattr(item, "docl_ModuleElement", None)
                    
                    setattr(item, "docl_ModuleElement", self)
                    

    @property
    def docl_Module(self):
        return self.__docl_Module

    @docl_Module.setter
    def docl_Module(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_docl_Module__docl_Module", None)
        self.__docl_Module = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "docl_OclModel"):
                opp_val = getattr(old_value, "docl_OclModel", None)
                if opp_val == self:
                    setattr(old_value, "docl_OclModel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "docl_OclModel"):
                opp_val = getattr(value, "docl_OclModel", None)
                setattr(value, "docl_OclModel", self)

class docl_ModuleElement:

    pass