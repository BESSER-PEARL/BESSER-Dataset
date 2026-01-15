from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class myAtl_EObject:

    pass
class ExpCS:

    pass
class myAtl_InfixedExpCS(ExpCS):

    pass
class NavigatingArgExpCS:

    pass
class IndexExpCS:

    pass
class PrefixedExpCS:

    pass
class myAtl_PrefixExpCS(PrefixedExpCS):

    pass
class myAtl_PrimaryExpCS(PrefixedExpCS):

    pass
class NavigatingExpCS:

    pass
class myAtl_NavigatingExpCS_Base(NavigatingExpCS):

    pass
class NavigatingExpCS_Base:

    pass
class myAtl_IndexExpCS(NavigatingExpCS_Base):

    pass
class myAtl_UnaryOperatorCS:

    def __init__(self, name: str, myAtl_UnaryOperatorCS: "myAtl_PrefixExpCS" = None):
        self.name = name
        self.myAtl_UnaryOperatorCS = myAtl_UnaryOperatorCS
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myAtl_UnaryOperatorCS(self):
        return self.__myAtl_UnaryOperatorCS

    @myAtl_UnaryOperatorCS.setter
    def myAtl_UnaryOperatorCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myAtl_UnaryOperatorCS__myAtl_UnaryOperatorCS", None)
        self.__myAtl_UnaryOperatorCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myAtl_PrefixExpCS"):
                opp_val = getattr(old_value, "myAtl_PrefixExpCS", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myAtl_PrefixExpCS"):
                opp_val = getattr(value, "myAtl_PrefixExpCS", None)
                if opp_val is None:
                    setattr(value, "myAtl_PrefixExpCS", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class InfixedExpCS:

    pass
class myAtl_InfixExpCS(InfixedExpCS):

    pass
class myAtl_PrefixedExpCS(InfixedExpCS):

    pass
class BinaryOperatorCS:

    pass
class myAtl_NavigationOperatorCS(BinaryOperatorCS):

    pass
class myAtl_InfixOperatorCS(BinaryOperatorCS):

    pass
class myAtl_BinaryOperatorCS:

    def __init__(self, name: str, myAtl_BinaryOperatorCS: "myAtl_InfixExpCS" = None):
        self.name = name
        self.myAtl_BinaryOperatorCS = myAtl_BinaryOperatorCS
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myAtl_BinaryOperatorCS(self):
        return self.__myAtl_BinaryOperatorCS

    @myAtl_BinaryOperatorCS.setter
    def myAtl_BinaryOperatorCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myAtl_BinaryOperatorCS__myAtl_BinaryOperatorCS", None)
        self.__myAtl_BinaryOperatorCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myAtl_InfixExpCS148"):
                opp_val = getattr(old_value, "myAtl_InfixExpCS148", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myAtl_InfixExpCS148"):
                opp_val = getattr(value, "myAtl_InfixExpCS148", None)
                if opp_val is None:
                    setattr(value, "myAtl_InfixExpCS148", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class myAtl_NavigatingSemiArgCS:

    def __init__(self, prefix: str, myAtl_NavigatingSemiArgCS: "myAtl_NavigatingArgExpCS" = None, myAtl_NavigatingSemiArgCS113: "myAtl_TypeExpCS" = None, myAtl_NavigatingSemiArgCS116: "myAtl_ExpCS" = None):
        self.prefix = prefix
        self.myAtl_NavigatingSemiArgCS = myAtl_NavigatingSemiArgCS
        self.myAtl_NavigatingSemiArgCS113 = myAtl_NavigatingSemiArgCS113
        self.myAtl_NavigatingSemiArgCS116 = myAtl_NavigatingSemiArgCS116
        
    @property
    def prefix(self) -> str:
        return self.__prefix

    @prefix.setter
    def prefix(self, prefix: str):
        self.__prefix = prefix

    @property
    def myAtl_NavigatingSemiArgCS113(self):
        return self.__myAtl_NavigatingSemiArgCS113

    @myAtl_NavigatingSemiArgCS113.setter
    def myAtl_NavigatingSemiArgCS113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myAtl_NavigatingSemiArgCS__myAtl_NavigatingSemiArgCS113", None)
        self.__myAtl_NavigatingSemiArgCS113 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myAtl_TypeExpCS114"):
                opp_val = getattr(old_value, "myAtl_TypeExpCS114", None)
                if opp_val == self:
                    setattr(old_value, "myAtl_TypeExpCS114", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myAtl_TypeExpCS114"):
                opp_val = getattr(value, "myAtl_TypeExpCS114", None)
                setattr(value, "myAtl_TypeExpCS114", self)

    @property
    def myAtl_NavigatingSemiArgCS(self):
        return self.__myAtl_NavigatingSemiArgCS

    @myAtl_NavigatingSemiArgCS.setter
    def myAtl_NavigatingSemiArgCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myAtl_NavigatingSemiArgCS__myAtl_NavigatingSemiArgCS", None)
        self.__myAtl_NavigatingSemiArgCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myAtl_NavigatingArgExpCS111"):
                opp_val = getattr(old_value, "myAtl_NavigatingArgExpCS111", None)
                if opp_val == self:
                    setattr(old_value, "myAtl_NavigatingArgExpCS111", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myAtl_NavigatingArgExpCS111"):
                opp_val = getattr(value, "myAtl_NavigatingArgExpCS111", None)
                setattr(value, "myAtl_NavigatingArgExpCS111", self)

    @property
    def myAtl_NavigatingSemiArgCS116(self):
        return self.__myAtl_NavigatingSemiArgCS116

    @myAtl_NavigatingSemiArgCS116.setter
    def myAtl_NavigatingSemiArgCS116(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myAtl_NavigatingSemiArgCS__myAtl_NavigatingSemiArgCS116", None)
        self.__myAtl_NavigatingSemiArgCS116 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myAtl_ExpCS117"):
                opp_val = getattr(old_value, "myAtl_ExpCS117", None)
                if opp_val == self:
                    setattr(old_value, "myAtl_ExpCS117", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myAtl_ExpCS117"):
                opp_val = getattr(value, "myAtl_ExpCS117", None)
                setattr(value, "myAtl_ExpCS117", self)

class myAtl_LetVariableCS:

    def __init__(self, name: str, myAtl_LetVariableCS: "myAtl_LetExpCS" = None, myAtl_LetVariableCS131: "myAtl_TypeExpCS" = None, myAtl_LetVariableCS134: "myAtl_ExpCS" = None):
        self.name = name
        self.myAtl_LetVariableCS = myAtl_LetVariableCS
        self.myAtl_LetVariableCS131 = myAtl_LetVariableCS131
        self.myAtl_LetVariableCS134 = myAtl_LetVariableCS134
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myAtl_LetVariableCS(self):
        return self.__myAtl_LetVariableCS

    @myAtl_LetVariableCS.setter
    def myAtl_LetVariableCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myAtl_LetVariableCS__myAtl_LetVariableCS", None)
        self.__myAtl_LetVariableCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myAtl_LetExpCS"):
                opp_val = getattr(old_value, "myAtl_LetExpCS", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myAtl_LetExpCS"):
                opp_val = getattr(value, "myAtl_LetExpCS", None)
                if opp_val is None:
                    setattr(value, "myAtl_LetExpCS", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def myAtl_LetVariableCS131(self):
        return self.__myAtl_LetVariableCS131

    @myAtl_LetVariableCS131.setter
    def myAtl_LetVariableCS131(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myAtl_LetVariableCS__myAtl_LetVariableCS131", None)
        self.__myAtl_LetVariableCS131 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myAtl_TypeExpCS132"):
                opp_val = getattr(old_value, "myAtl_TypeExpCS132", None)
                if opp_val == self:
                    setattr(old_value, "myAtl_TypeExpCS132", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myAtl_TypeExpCS132"):
                opp_val = getattr(value, "myAtl_TypeExpCS132", None)
                setattr(value, "myAtl_TypeExpCS132", self)

    @property
    def myAtl_LetVariableCS134(self):
        return self.__myAtl_LetVariableCS134

    @myAtl_LetVariableCS134.setter
    def myAtl_LetVariableCS134(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myAtl_LetVariableCS__myAtl_LetVariableCS134", None)
        self.__myAtl_LetVariableCS134 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myAtl_ExpCS135"):
                opp_val = getattr(old_value, "myAtl_ExpCS135", None)
                if opp_val == self:
                    setattr(old_value, "myAtl_ExpCS135", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myAtl_ExpCS135"):
                opp_val = getattr(value, "myAtl_ExpCS135", None)
                setattr(value, "myAtl_ExpCS135", self)

class myAtl_NavigatingArgExpCS:

    pass
class myAtl_NavigatingArgCS:

    pass
class myAtl_NavigatingCommaArgCS:

    def __init__(self, prefix: str, myAtl_NavigatingCommaArgCS: "myAtl_NavigatingArgExpCS" = None, myAtl_NavigatingCommaArgCS105: "myAtl_TypeExpCS" = None, myAtl_NavigatingCommaArgCS108: "myAtl_ExpCS" = None):
        self.prefix = prefix
        self.myAtl_NavigatingCommaArgCS = myAtl_NavigatingCommaArgCS
        self.myAtl_NavigatingCommaArgCS105 = myAtl_NavigatingCommaArgCS105
        self.myAtl_NavigatingCommaArgCS108 = myAtl_NavigatingCommaArgCS108
        
    @property
    def prefix(self) -> str:
        return self.__prefix

    @prefix.setter
    def prefix(self, prefix: str):
        self.__prefix = prefix

    @property
    def myAtl_NavigatingCommaArgCS(self):
        return self.__myAtl_NavigatingCommaArgCS

    @myAtl_NavigatingCommaArgCS.setter
    def myAtl_NavigatingCommaArgCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myAtl_NavigatingCommaArgCS__myAtl_NavigatingCommaArgCS", None)
        self.__myAtl_NavigatingCommaArgCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myAtl_NavigatingArgExpCS103"):
                opp_val = getattr(old_value, "myAtl_NavigatingArgExpCS103", None)
                if opp_val == self:
                    setattr(old_value, "myAtl_NavigatingArgExpCS103", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myAtl_NavigatingArgExpCS103"):
                opp_val = getattr(value, "myAtl_NavigatingArgExpCS103", None)
                setattr(value, "myAtl_NavigatingArgExpCS103", self)

    @property
    def myAtl_NavigatingCommaArgCS108(self):
        return self.__myAtl_NavigatingCommaArgCS108

    @myAtl_NavigatingCommaArgCS108.setter
    def myAtl_NavigatingCommaArgCS108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myAtl_NavigatingCommaArgCS__myAtl_NavigatingCommaArgCS108", None)
        self.__myAtl_NavigatingCommaArgCS108 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myAtl_ExpCS109"):
                opp_val = getattr(old_value, "myAtl_ExpCS109", None)
                if opp_val == self:
                    setattr(old_value, "myAtl_ExpCS109", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myAtl_ExpCS109"):
                opp_val = getattr(value, "myAtl_ExpCS109", None)
                setattr(value, "myAtl_ExpCS109", self)

    @property
    def myAtl_NavigatingCommaArgCS105(self):
        return self.__myAtl_NavigatingCommaArgCS105

    @myAtl_NavigatingCommaArgCS105.setter
    def myAtl_NavigatingCommaArgCS105(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myAtl_NavigatingCommaArgCS__myAtl_NavigatingCommaArgCS105", None)
        self.__myAtl_NavigatingCommaArgCS105 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myAtl_TypeExpCS106"):
                opp_val = getattr(old_value, "myAtl_TypeExpCS106", None)
                if opp_val == self:
                    setattr(old_value, "myAtl_TypeExpCS106", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myAtl_TypeExpCS106"):
                opp_val = getattr(value, "myAtl_TypeExpCS106", None)
                setattr(value, "myAtl_TypeExpCS106", self)

class myAtl_NavigatingBarArgCS:

    def __init__(self, prefix: str, myAtl_NavigatingBarArgCS: "myAtl_NavigatingArgExpCS" = None, myAtl_NavigatingBarArgCS97: "myAtl_TypeExpCS" = None, myAtl_NavigatingBarArgCS100: "myAtl_ExpCS" = None):
        self.prefix = prefix
        self.myAtl_NavigatingBarArgCS = myAtl_NavigatingBarArgCS
        self.myAtl_NavigatingBarArgCS97 = myAtl_NavigatingBarArgCS97
        self.myAtl_NavigatingBarArgCS100 = myAtl_NavigatingBarArgCS100
        
    @property
    def prefix(self) -> str:
        return self.__prefix

    @prefix.setter
    def prefix(self, prefix: str):
        self.__prefix = prefix

    @property
    def myAtl_NavigatingBarArgCS100(self):
        return self.__myAtl_NavigatingBarArgCS100

    @myAtl_NavigatingBarArgCS100.setter
    def myAtl_NavigatingBarArgCS100(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myAtl_NavigatingBarArgCS__myAtl_NavigatingBarArgCS100", None)
        self.__myAtl_NavigatingBarArgCS100 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myAtl_ExpCS101"):
                opp_val = getattr(old_value, "myAtl_ExpCS101", None)
                if opp_val == self:
                    setattr(old_value, "myAtl_ExpCS101", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myAtl_ExpCS101"):
                opp_val = getattr(value, "myAtl_ExpCS101", None)
                setattr(value, "myAtl_ExpCS101", self)

    @property
    def myAtl_NavigatingBarArgCS(self):
        return self.__myAtl_NavigatingBarArgCS

    @myAtl_NavigatingBarArgCS.setter
    def myAtl_NavigatingBarArgCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myAtl_NavigatingBarArgCS__myAtl_NavigatingBarArgCS", None)
        self.__myAtl_NavigatingBarArgCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myAtl_NavigatingArgExpCS95"):
                opp_val = getattr(old_value, "myAtl_NavigatingArgExpCS95", None)
                if opp_val == self:
                    setattr(old_value, "myAtl_NavigatingArgExpCS95", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myAtl_NavigatingArgExpCS95"):
                opp_val = getattr(value, "myAtl_NavigatingArgExpCS95", None)
                setattr(value, "myAtl_NavigatingArgExpCS95", self)

    @property
    def myAtl_NavigatingBarArgCS97(self):
        return self.__myAtl_NavigatingBarArgCS97

    @myAtl_NavigatingBarArgCS97.setter
    def myAtl_NavigatingBarArgCS97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myAtl_NavigatingBarArgCS__myAtl_NavigatingBarArgCS97", None)
        self.__myAtl_NavigatingBarArgCS97 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myAtl_TypeExpCS98"):
                opp_val = getattr(old_value, "myAtl_TypeExpCS98", None)
                if opp_val == self:
                    setattr(old_value, "myAtl_TypeExpCS98", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myAtl_TypeExpCS98"):
                opp_val = getattr(value, "myAtl_TypeExpCS98", None)
                setattr(value, "myAtl_TypeExpCS98", self)

class PrimitiveLiteralExpCS:

    pass
class myAtl_InvalidLiteralExpCS(PrimitiveLiteralExpCS):

    pass
class myAtl_BooleanLiteralExpCS(PrimitiveLiteralExpCS):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class myAtl_UnlimitedNaturalLiteralExpCS(PrimitiveLiteralExpCS):

    pass
class myAtl_StringLiteralExpCS(PrimitiveLiteralExpCS):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class myAtl_TypeLiteralExpCS:

    pass
class TypeExpCS:

    pass
class myAtl_TypeNameExpCS(TypeExpCS):

    def __init__(self, namespace: str, element: str):
        self.namespace = namespace
        self.element = element
        
    @property
    def element(self) -> str:
        return self.__element

    @element.setter
    def element(self, element: str):
        self.__element = element

    @property
    def namespace(self) -> str:
        return self.__namespace

    @namespace.setter
    def namespace(self, namespace: str):
        self.__namespace = namespace

class myAtl_TypeLiteralCS(TypeExpCS):

    def __init__(self, name: str, myAtl_TypeLiteralCS: "myAtl_TypeLiteralExpCS" = None):
        self.name = name
        self.myAtl_TypeLiteralCS = myAtl_TypeLiteralCS
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myAtl_TypeLiteralCS(self):
        return self.__myAtl_TypeLiteralCS

    @myAtl_TypeLiteralCS.setter
    def myAtl_TypeLiteralCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myAtl_TypeLiteralCS__myAtl_TypeLiteralCS", None)
        self.__myAtl_TypeLiteralCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myAtl_TypeLiteralExpCS"):
                opp_val = getattr(old_value, "myAtl_TypeLiteralExpCS", None)
                if opp_val == self:
                    setattr(old_value, "myAtl_TypeLiteralExpCS", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myAtl_TypeLiteralExpCS"):
                opp_val = getattr(value, "myAtl_TypeLiteralExpCS", None)
                setattr(value, "myAtl_TypeLiteralExpCS", self)

class myAtl_NullLiteralExpCS(PrimitiveLiteralExpCS):

    pass
class myAtl_tuplePartCS:

    def __init__(self, name: str, myAtl_tuplePartCS: "myAtl_TupleTypeCS" = None, myAtl_tuplePartCS77: "myAtl_TypeExpCS" = None):
        self.name = name
        self.myAtl_tuplePartCS = myAtl_tuplePartCS
        self.myAtl_tuplePartCS77 = myAtl_tuplePartCS77
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myAtl_tuplePartCS77(self):
        return self.__myAtl_tuplePartCS77

    @myAtl_tuplePartCS77.setter
    def myAtl_tuplePartCS77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myAtl_tuplePartCS__myAtl_tuplePartCS77", None)
        self.__myAtl_tuplePartCS77 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myAtl_TypeExpCS78"):
                opp_val = getattr(old_value, "myAtl_TypeExpCS78", None)
                if opp_val == self:
                    setattr(old_value, "myAtl_TypeExpCS78", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myAtl_TypeExpCS78"):
                opp_val = getattr(value, "myAtl_TypeExpCS78", None)
                setattr(value, "myAtl_TypeExpCS78", self)

    @property
    def myAtl_tuplePartCS(self):
        return self.__myAtl_tuplePartCS

    @myAtl_tuplePartCS.setter
    def myAtl_tuplePartCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myAtl_tuplePartCS__myAtl_tuplePartCS", None)
        self.__myAtl_tuplePartCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myAtl_TupleTypeCS"):
                opp_val = getattr(old_value, "myAtl_TupleTypeCS", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myAtl_TupleTypeCS"):
                opp_val = getattr(value, "myAtl_TupleTypeCS", None)
                if opp_val is None:
                    setattr(value, "myAtl_TupleTypeCS", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class myAtl_NumberLiteralExpCS(PrimitiveLiteralExpCS):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class myAtl_TupleLiteralPartCS:

    def __init__(self, name: str, myAtl_TupleLiteralPartCS: "myAtl_TupleLiteralExpCS" = None, myAtl_TupleLiteralPartCS81: "myAtl_TypeExpCS" = None, myAtl_TupleLiteralPartCS84: "myAtl_ExpCS" = None):
        self.name = name
        self.myAtl_TupleLiteralPartCS = myAtl_TupleLiteralPartCS
        self.myAtl_TupleLiteralPartCS81 = myAtl_TupleLiteralPartCS81
        self.myAtl_TupleLiteralPartCS84 = myAtl_TupleLiteralPartCS84
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myAtl_TupleLiteralPartCS81(self):
        return self.__myAtl_TupleLiteralPartCS81

    @myAtl_TupleLiteralPartCS81.setter
    def myAtl_TupleLiteralPartCS81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myAtl_TupleLiteralPartCS__myAtl_TupleLiteralPartCS81", None)
        self.__myAtl_TupleLiteralPartCS81 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myAtl_TypeExpCS82"):
                opp_val = getattr(old_value, "myAtl_TypeExpCS82", None)
                if opp_val == self:
                    setattr(old_value, "myAtl_TypeExpCS82", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myAtl_TypeExpCS82"):
                opp_val = getattr(value, "myAtl_TypeExpCS82", None)
                setattr(value, "myAtl_TypeExpCS82", self)

    @property
    def myAtl_TupleLiteralPartCS84(self):
        return self.__myAtl_TupleLiteralPartCS84

    @myAtl_TupleLiteralPartCS84.setter
    def myAtl_TupleLiteralPartCS84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myAtl_TupleLiteralPartCS__myAtl_TupleLiteralPartCS84", None)
        self.__myAtl_TupleLiteralPartCS84 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myAtl_ExpCS85"):
                opp_val = getattr(old_value, "myAtl_ExpCS85", None)
                if opp_val == self:
                    setattr(old_value, "myAtl_ExpCS85", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myAtl_ExpCS85"):
                opp_val = getattr(value, "myAtl_ExpCS85", None)
                setattr(value, "myAtl_ExpCS85", self)

    @property
    def myAtl_TupleLiteralPartCS(self):
        return self.__myAtl_TupleLiteralPartCS

    @myAtl_TupleLiteralPartCS.setter
    def myAtl_TupleLiteralPartCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myAtl_TupleLiteralPartCS__myAtl_TupleLiteralPartCS", None)
        self.__myAtl_TupleLiteralPartCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myAtl_TupleLiteralExpCS"):
                opp_val = getattr(old_value, "myAtl_TupleLiteralExpCS", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myAtl_TupleLiteralExpCS"):
                opp_val = getattr(value, "myAtl_TupleLiteralExpCS", None)
                if opp_val is None:
                    setattr(value, "myAtl_TupleLiteralExpCS", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class PrimaryExpCS:

    pass
class myAtl_NavigatingExpCS(PrimaryExpCS):

    pass
class myAtl_SelfExpCS(PrimaryExpCS):

    pass
class myAtl_NestedExpCS(PrimaryExpCS):

    pass
class myAtl_IfExpCS(PrimaryExpCS):

    pass
class myAtl_StringExpCs(PrimaryExpCS):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class myAtl_LetExpCS(PrimaryExpCS):

    pass
class myAtl_TupleLiteralExpCS(PrimaryExpCS):

    pass
class myAtl_PrimitiveLiteralExpCS(PrimaryExpCS):

    pass
class Statement:

    pass
class myAtl_BindingStat(Statement):

    def __init__(self, propertyName: str, myAtl_BindingStat: "myAtl_ExpCS" = None, myAtl_BindingStat69: "myAtl_ExpCS" = None):
        self.propertyName = propertyName
        self.myAtl_BindingStat = myAtl_BindingStat
        self.myAtl_BindingStat69 = myAtl_BindingStat69
        
    @property
    def propertyName(self) -> str:
        return self.__propertyName

    @propertyName.setter
    def propertyName(self, propertyName: str):
        self.__propertyName = propertyName

    @property
    def myAtl_BindingStat69(self):
        return self.__myAtl_BindingStat69

    @myAtl_BindingStat69.setter
    def myAtl_BindingStat69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myAtl_BindingStat__myAtl_BindingStat69", None)
        self.__myAtl_BindingStat69 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myAtl_ExpCS70"):
                opp_val = getattr(old_value, "myAtl_ExpCS70", None)
                if opp_val == self:
                    setattr(old_value, "myAtl_ExpCS70", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myAtl_ExpCS70"):
                opp_val = getattr(value, "myAtl_ExpCS70", None)
                setattr(value, "myAtl_ExpCS70", self)

    @property
    def myAtl_BindingStat(self):
        return self.__myAtl_BindingStat

    @myAtl_BindingStat.setter
    def myAtl_BindingStat(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myAtl_BindingStat__myAtl_BindingStat", None)
        self.__myAtl_BindingStat = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myAtl_ExpCS67"):
                opp_val = getattr(old_value, "myAtl_ExpCS67", None)
                if opp_val == self:
                    setattr(old_value, "myAtl_ExpCS67", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myAtl_ExpCS67"):
                opp_val = getattr(value, "myAtl_ExpCS67", None)
                setattr(value, "myAtl_ExpCS67", self)

class myAtl_Statement:

    pass
class TypeLiteralCS:

    pass
class myAtl_PrimitiveTypeCS(TypeLiteralCS):

    pass
class myAtl_TupleTypeCS(TypeLiteralCS):

    def __init__(self, backtrack: str, myAtl_TupleTypeCS: set["myAtl_tuplePartCS"] = None):
        self.backtrack = backtrack
        self.myAtl_TupleTypeCS = myAtl_TupleTypeCS if myAtl_TupleTypeCS is not None else set()
        
    @property
    def backtrack(self) -> str:
        return self.__backtrack

    @backtrack.setter
    def backtrack(self, backtrack: str):
        self.__backtrack = backtrack

    @property
    def myAtl_TupleTypeCS(self):
        return self.__myAtl_TupleTypeCS

    @myAtl_TupleTypeCS.setter
    def myAtl_TupleTypeCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myAtl_TupleTypeCS__myAtl_TupleTypeCS", None)
        self.__myAtl_TupleTypeCS = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "myAtl_tuplePartCS"):
                    opp_val = getattr(item, "myAtl_tuplePartCS", None)
                    
                    if opp_val == self:
                        setattr(item, "myAtl_tuplePartCS", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "myAtl_tuplePartCS"):
                    opp_val = getattr(item, "myAtl_tuplePartCS", None)
                    
                    setattr(item, "myAtl_tuplePartCS", self)
                    

class myAtl_CollectionTypeCS(TypeLiteralCS):

    pass
class myAtl_TypeExpCS:

    pass
class myAtl_Binding:

    def __init__(self, propertyName: str, myAtl_Binding: "myAtl_SimpleOutPatternElement" = None, myAtl_Binding62: "myAtl_ExpCS" = None):
        self.propertyName = propertyName
        self.myAtl_Binding = myAtl_Binding
        self.myAtl_Binding62 = myAtl_Binding62
        
    @property
    def propertyName(self) -> str:
        return self.__propertyName

    @propertyName.setter
    def propertyName(self, propertyName: str):
        self.__propertyName = propertyName

    @property
    def myAtl_Binding(self):
        return self.__myAtl_Binding

    @myAtl_Binding.setter
    def myAtl_Binding(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myAtl_Binding__myAtl_Binding", None)
        self.__myAtl_Binding = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myAtl_SimpleOutPatternElement58"):
                opp_val = getattr(old_value, "myAtl_SimpleOutPatternElement58", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myAtl_SimpleOutPatternElement58"):
                opp_val = getattr(value, "myAtl_SimpleOutPatternElement58", None)
                if opp_val is None:
                    setattr(value, "myAtl_SimpleOutPatternElement58", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def myAtl_Binding62(self):
        return self.__myAtl_Binding62

    @myAtl_Binding62.setter
    def myAtl_Binding62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myAtl_Binding__myAtl_Binding62", None)
        self.__myAtl_Binding62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myAtl_ExpCS63"):
                opp_val = getattr(old_value, "myAtl_ExpCS63", None)
                if opp_val == self:
                    setattr(old_value, "myAtl_ExpCS63", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myAtl_ExpCS63"):
                opp_val = getattr(value, "myAtl_ExpCS63", None)
                setattr(value, "myAtl_ExpCS63", self)

class myAtl_OutPatternElement:

    pass
class OutPatternElement:

    pass
class myAtl_ForEachOutPatternElement(OutPatternElement):

    pass
class myAtl_SimpleOutPatternElement(OutPatternElement):

    def __init__(self, varName: str, myAtl_SimpleOutPatternElement58: set["myAtl_Binding"] = None, myAtl_SimpleOutPatternElement: "myAtl_ATLType" = None):
        self.varName = varName
        self.myAtl_SimpleOutPatternElement58 = myAtl_SimpleOutPatternElement58 if myAtl_SimpleOutPatternElement58 is not None else set()
        self.myAtl_SimpleOutPatternElement = myAtl_SimpleOutPatternElement
        
    @property
    def varName(self) -> str:
        return self.__varName

    @varName.setter
    def varName(self, varName: str):
        self.__varName = varName

    @property
    def myAtl_SimpleOutPatternElement(self):
        return self.__myAtl_SimpleOutPatternElement

    @myAtl_SimpleOutPatternElement.setter
    def myAtl_SimpleOutPatternElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myAtl_SimpleOutPatternElement__myAtl_SimpleOutPatternElement", None)
        self.__myAtl_SimpleOutPatternElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myAtl_ATLType56"):
                opp_val = getattr(old_value, "myAtl_ATLType56", None)
                if opp_val == self:
                    setattr(old_value, "myAtl_ATLType56", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myAtl_ATLType56"):
                opp_val = getattr(value, "myAtl_ATLType56", None)
                setattr(value, "myAtl_ATLType56", self)

    @property
    def myAtl_SimpleOutPatternElement58(self):
        return self.__myAtl_SimpleOutPatternElement58

    @myAtl_SimpleOutPatternElement58.setter
    def myAtl_SimpleOutPatternElement58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myAtl_SimpleOutPatternElement__myAtl_SimpleOutPatternElement58", None)
        self.__myAtl_SimpleOutPatternElement58 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "myAtl_Binding"):
                    opp_val = getattr(item, "myAtl_Binding", None)
                    
                    if opp_val == self:
                        setattr(item, "myAtl_Binding", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "myAtl_Binding"):
                    opp_val = getattr(item, "myAtl_Binding", None)
                    
                    setattr(item, "myAtl_Binding", self)
                    

class myAtl_InPatternElement:

    def __init__(self, varName: str, myAtl_InPatternElement51: "myAtl_ATLType" = None, myAtl_InPatternElement: "myAtl_InPattern" = None):
        self.varName = varName
        self.myAtl_InPatternElement51 = myAtl_InPatternElement51
        self.myAtl_InPatternElement = myAtl_InPatternElement
        
    @property
    def varName(self) -> str:
        return self.__varName

    @varName.setter
    def varName(self, varName: str):
        self.__varName = varName

    @property
    def myAtl_InPatternElement51(self):
        return self.__myAtl_InPatternElement51

    @myAtl_InPatternElement51.setter
    def myAtl_InPatternElement51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myAtl_InPatternElement__myAtl_InPatternElement51", None)
        self.__myAtl_InPatternElement51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myAtl_ATLType52"):
                opp_val = getattr(old_value, "myAtl_ATLType52", None)
                if opp_val == self:
                    setattr(old_value, "myAtl_ATLType52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myAtl_ATLType52"):
                opp_val = getattr(value, "myAtl_ATLType52", None)
                setattr(value, "myAtl_ATLType52", self)

    @property
    def myAtl_InPatternElement(self):
        return self.__myAtl_InPatternElement

    @myAtl_InPatternElement.setter
    def myAtl_InPatternElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myAtl_InPatternElement__myAtl_InPatternElement", None)
        self.__myAtl_InPatternElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myAtl_InPattern46"):
                opp_val = getattr(old_value, "myAtl_InPattern46", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myAtl_InPattern46"):
                opp_val = getattr(value, "myAtl_InPattern46", None)
                if opp_val is None:
                    setattr(value, "myAtl_InPattern46", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class myAtl_ATLDefCS:

    def __init__(self, varName: str, myAtl_ATLDefCS29: set["myAtl_ATLParameterCS"] = None, myAtl_ATLDefCS: "myAtl_Helper" = None, myAtl_ATLDefCS32: "myAtl_ATLType" = None, myAtl_ATLDefCS34: "myAtl_ExpCS" = None):
        self.varName = varName
        self.myAtl_ATLDefCS29 = myAtl_ATLDefCS29 if myAtl_ATLDefCS29 is not None else set()
        self.myAtl_ATLDefCS = myAtl_ATLDefCS
        self.myAtl_ATLDefCS32 = myAtl_ATLDefCS32
        self.myAtl_ATLDefCS34 = myAtl_ATLDefCS34
        
    @property
    def varName(self) -> str:
        return self.__varName

    @varName.setter
    def varName(self, varName: str):
        self.__varName = varName

    @property
    def myAtl_ATLDefCS32(self):
        return self.__myAtl_ATLDefCS32

    @myAtl_ATLDefCS32.setter
    def myAtl_ATLDefCS32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myAtl_ATLDefCS__myAtl_ATLDefCS32", None)
        self.__myAtl_ATLDefCS32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myAtl_ATLType"):
                opp_val = getattr(old_value, "myAtl_ATLType", None)
                if opp_val == self:
                    setattr(old_value, "myAtl_ATLType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myAtl_ATLType"):
                opp_val = getattr(value, "myAtl_ATLType", None)
                setattr(value, "myAtl_ATLType", self)

    @property
    def myAtl_ATLDefCS34(self):
        return self.__myAtl_ATLDefCS34

    @myAtl_ATLDefCS34.setter
    def myAtl_ATLDefCS34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myAtl_ATLDefCS__myAtl_ATLDefCS34", None)
        self.__myAtl_ATLDefCS34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myAtl_ExpCS35"):
                opp_val = getattr(old_value, "myAtl_ExpCS35", None)
                if opp_val == self:
                    setattr(old_value, "myAtl_ExpCS35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myAtl_ExpCS35"):
                opp_val = getattr(value, "myAtl_ExpCS35", None)
                setattr(value, "myAtl_ExpCS35", self)

    @property
    def myAtl_ATLDefCS29(self):
        return self.__myAtl_ATLDefCS29

    @myAtl_ATLDefCS29.setter
    def myAtl_ATLDefCS29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myAtl_ATLDefCS__myAtl_ATLDefCS29", None)
        self.__myAtl_ATLDefCS29 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "myAtl_ATLParameterCS30"):
                    opp_val = getattr(item, "myAtl_ATLParameterCS30", None)
                    
                    if opp_val == self:
                        setattr(item, "myAtl_ATLParameterCS30", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "myAtl_ATLParameterCS30"):
                    opp_val = getattr(item, "myAtl_ATLParameterCS30", None)
                    
                    setattr(item, "myAtl_ATLParameterCS30", self)
                    

    @property
    def myAtl_ATLDefCS(self):
        return self.__myAtl_ATLDefCS

    @myAtl_ATLDefCS.setter
    def myAtl_ATLDefCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myAtl_ATLDefCS__myAtl_ATLDefCS", None)
        self.__myAtl_ATLDefCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myAtl_Helper"):
                opp_val = getattr(old_value, "myAtl_Helper", None)
                if opp_val == self:
                    setattr(old_value, "myAtl_Helper", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myAtl_Helper"):
                opp_val = getattr(value, "myAtl_Helper", None)
                setattr(value, "myAtl_Helper", self)

class myAtl_ATLType:

    def __init__(self, modelName: str, myAtl_ATLType: "myAtl_ATLDefCS" = None, myAtl_ATLType38: "myAtl_ATLParameterCS" = None, myAtl_ATLType41: "myAtl_RuleVariableDeclaration" = None, myAtl_ATLType52: "myAtl_InPatternElement" = None, myAtl_ATLType56: "myAtl_SimpleOutPatternElement" = None, myAtl_ATLType72: "myAtl_TypeExpCS" = None):
        self.modelName = modelName
        self.myAtl_ATLType = myAtl_ATLType
        self.myAtl_ATLType38 = myAtl_ATLType38
        self.myAtl_ATLType41 = myAtl_ATLType41
        self.myAtl_ATLType52 = myAtl_ATLType52
        self.myAtl_ATLType56 = myAtl_ATLType56
        self.myAtl_ATLType72 = myAtl_ATLType72
        
    @property
    def modelName(self) -> str:
        return self.__modelName

    @modelName.setter
    def modelName(self, modelName: str):
        self.__modelName = modelName

    @property
    def myAtl_ATLType38(self):
        return self.__myAtl_ATLType38

    @myAtl_ATLType38.setter
    def myAtl_ATLType38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myAtl_ATLType__myAtl_ATLType38", None)
        self.__myAtl_ATLType38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myAtl_ATLParameterCS37"):
                opp_val = getattr(old_value, "myAtl_ATLParameterCS37", None)
                if opp_val == self:
                    setattr(old_value, "myAtl_ATLParameterCS37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myAtl_ATLParameterCS37"):
                opp_val = getattr(value, "myAtl_ATLParameterCS37", None)
                setattr(value, "myAtl_ATLParameterCS37", self)

    @property
    def myAtl_ATLType72(self):
        return self.__myAtl_ATLType72

    @myAtl_ATLType72.setter
    def myAtl_ATLType72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myAtl_ATLType__myAtl_ATLType72", None)
        self.__myAtl_ATLType72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myAtl_TypeExpCS"):
                opp_val = getattr(old_value, "myAtl_TypeExpCS", None)
                if opp_val == self:
                    setattr(old_value, "myAtl_TypeExpCS", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myAtl_TypeExpCS"):
                opp_val = getattr(value, "myAtl_TypeExpCS", None)
                setattr(value, "myAtl_TypeExpCS", self)

    @property
    def myAtl_ATLType(self):
        return self.__myAtl_ATLType

    @myAtl_ATLType.setter
    def myAtl_ATLType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myAtl_ATLType__myAtl_ATLType", None)
        self.__myAtl_ATLType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myAtl_ATLDefCS32"):
                opp_val = getattr(old_value, "myAtl_ATLDefCS32", None)
                if opp_val == self:
                    setattr(old_value, "myAtl_ATLDefCS32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myAtl_ATLDefCS32"):
                opp_val = getattr(value, "myAtl_ATLDefCS32", None)
                setattr(value, "myAtl_ATLDefCS32", self)

    @property
    def myAtl_ATLType52(self):
        return self.__myAtl_ATLType52

    @myAtl_ATLType52.setter
    def myAtl_ATLType52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myAtl_ATLType__myAtl_ATLType52", None)
        self.__myAtl_ATLType52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myAtl_InPatternElement51"):
                opp_val = getattr(old_value, "myAtl_InPatternElement51", None)
                if opp_val == self:
                    setattr(old_value, "myAtl_InPatternElement51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myAtl_InPatternElement51"):
                opp_val = getattr(value, "myAtl_InPatternElement51", None)
                setattr(value, "myAtl_InPatternElement51", self)

    @property
    def myAtl_ATLType56(self):
        return self.__myAtl_ATLType56

    @myAtl_ATLType56.setter
    def myAtl_ATLType56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myAtl_ATLType__myAtl_ATLType56", None)
        self.__myAtl_ATLType56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myAtl_SimpleOutPatternElement"):
                opp_val = getattr(old_value, "myAtl_SimpleOutPatternElement", None)
                if opp_val == self:
                    setattr(old_value, "myAtl_SimpleOutPatternElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myAtl_SimpleOutPatternElement"):
                opp_val = getattr(value, "myAtl_SimpleOutPatternElement", None)
                setattr(value, "myAtl_SimpleOutPatternElement", self)

    @property
    def myAtl_ATLType41(self):
        return self.__myAtl_ATLType41

    @myAtl_ATLType41.setter
    def myAtl_ATLType41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myAtl_ATLType__myAtl_ATLType41", None)
        self.__myAtl_ATLType41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myAtl_RuleVariableDeclaration40"):
                opp_val = getattr(old_value, "myAtl_RuleVariableDeclaration40", None)
                if opp_val == self:
                    setattr(old_value, "myAtl_RuleVariableDeclaration40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myAtl_RuleVariableDeclaration40"):
                opp_val = getattr(value, "myAtl_RuleVariableDeclaration40", None)
                setattr(value, "myAtl_RuleVariableDeclaration40", self)

class myAtl_ATLParameterCS:

    def __init__(self, varName: str, myAtl_ATLParameterCS: "myAtl_QueryRule" = None, myAtl_ATLParameterCS30: "myAtl_ATLDefCS" = None, myAtl_ATLParameterCS37: "myAtl_ATLType" = None):
        self.varName = varName
        self.myAtl_ATLParameterCS = myAtl_ATLParameterCS
        self.myAtl_ATLParameterCS30 = myAtl_ATLParameterCS30
        self.myAtl_ATLParameterCS37 = myAtl_ATLParameterCS37
        
    @property
    def varName(self) -> str:
        return self.__varName

    @varName.setter
    def varName(self, varName: str):
        self.__varName = varName

    @property
    def myAtl_ATLParameterCS(self):
        return self.__myAtl_ATLParameterCS

    @myAtl_ATLParameterCS.setter
    def myAtl_ATLParameterCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myAtl_ATLParameterCS__myAtl_ATLParameterCS", None)
        self.__myAtl_ATLParameterCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myAtl_QueryRule"):
                opp_val = getattr(old_value, "myAtl_QueryRule", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myAtl_QueryRule"):
                opp_val = getattr(value, "myAtl_QueryRule", None)
                if opp_val is None:
                    setattr(value, "myAtl_QueryRule", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def myAtl_ATLParameterCS30(self):
        return self.__myAtl_ATLParameterCS30

    @myAtl_ATLParameterCS30.setter
    def myAtl_ATLParameterCS30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myAtl_ATLParameterCS__myAtl_ATLParameterCS30", None)
        self.__myAtl_ATLParameterCS30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myAtl_ATLDefCS29"):
                opp_val = getattr(old_value, "myAtl_ATLDefCS29", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myAtl_ATLDefCS29"):
                opp_val = getattr(value, "myAtl_ATLDefCS29", None)
                if opp_val is None:
                    setattr(value, "myAtl_ATLDefCS29", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def myAtl_ATLParameterCS37(self):
        return self.__myAtl_ATLParameterCS37

    @myAtl_ATLParameterCS37.setter
    def myAtl_ATLParameterCS37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myAtl_ATLParameterCS__myAtl_ATLParameterCS37", None)
        self.__myAtl_ATLParameterCS37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myAtl_ATLType38"):
                opp_val = getattr(old_value, "myAtl_ATLType38", None)
                if opp_val == self:
                    setattr(old_value, "myAtl_ATLType38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myAtl_ATLType38"):
                opp_val = getattr(value, "myAtl_ATLType38", None)
                setattr(value, "myAtl_ATLType38", self)

class myAtl_ExpCS(NavigatingArgExpCS):

    pass
class myAtl_ActionBlock:

    pass
class myAtl_OutPattern:

    pass
class myAtl_NameExpCS(IndexExpCS):

    def __init__(self, namespace: str, element: str, myAtl_NameExpCS: "myAtl_Module" = None, myAtl_NameExpCS3: "myAtl_Module" = None, myAtl_NameExpCS6: "myAtl_Module" = None):
        self.namespace = namespace
        self.element = element
        self.myAtl_NameExpCS = myAtl_NameExpCS
        self.myAtl_NameExpCS3 = myAtl_NameExpCS3
        self.myAtl_NameExpCS6 = myAtl_NameExpCS6
        
    @property
    def element(self) -> str:
        return self.__element

    @element.setter
    def element(self, element: str):
        self.__element = element

    @property
    def namespace(self) -> str:
        return self.__namespace

    @namespace.setter
    def namespace(self, namespace: str):
        self.__namespace = namespace

    @property
    def myAtl_NameExpCS(self):
        return self.__myAtl_NameExpCS

    @myAtl_NameExpCS.setter
    def myAtl_NameExpCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myAtl_NameExpCS__myAtl_NameExpCS", None)
        self.__myAtl_NameExpCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myAtl_Module"):
                opp_val = getattr(old_value, "myAtl_Module", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myAtl_Module"):
                opp_val = getattr(value, "myAtl_Module", None)
                if opp_val is None:
                    setattr(value, "myAtl_Module", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def myAtl_NameExpCS6(self):
        return self.__myAtl_NameExpCS6

    @myAtl_NameExpCS6.setter
    def myAtl_NameExpCS6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myAtl_NameExpCS__myAtl_NameExpCS6", None)
        self.__myAtl_NameExpCS6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myAtl_Module5"):
                opp_val = getattr(old_value, "myAtl_Module5", None)
                if opp_val == self:
                    setattr(old_value, "myAtl_Module5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myAtl_Module5"):
                opp_val = getattr(value, "myAtl_Module5", None)
                setattr(value, "myAtl_Module5", self)

    @property
    def myAtl_NameExpCS3(self):
        return self.__myAtl_NameExpCS3

    @myAtl_NameExpCS3.setter
    def myAtl_NameExpCS3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myAtl_NameExpCS__myAtl_NameExpCS3", None)
        self.__myAtl_NameExpCS3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myAtl_Module2"):
                opp_val = getattr(old_value, "myAtl_Module2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myAtl_Module2"):
                opp_val = getattr(value, "myAtl_Module2", None)
                if opp_val is None:
                    setattr(value, "myAtl_Module2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class myAtl_RuleVariableDeclaration:

    def __init__(self, varName: str, myAtl_RuleVariableDeclaration: "myAtl_MatchedRule" = None, myAtl_RuleVariableDeclaration17: "myAtl_CalledRule" = None, myAtl_RuleVariableDeclaration43: "myAtl_ExpCS" = None, myAtl_RuleVariableDeclaration40: "myAtl_ATLType" = None):
        self.varName = varName
        self.myAtl_RuleVariableDeclaration = myAtl_RuleVariableDeclaration
        self.myAtl_RuleVariableDeclaration17 = myAtl_RuleVariableDeclaration17
        self.myAtl_RuleVariableDeclaration43 = myAtl_RuleVariableDeclaration43
        self.myAtl_RuleVariableDeclaration40 = myAtl_RuleVariableDeclaration40
        
    @property
    def varName(self) -> str:
        return self.__varName

    @varName.setter
    def varName(self, varName: str):
        self.__varName = varName

    @property
    def myAtl_RuleVariableDeclaration17(self):
        return self.__myAtl_RuleVariableDeclaration17

    @myAtl_RuleVariableDeclaration17.setter
    def myAtl_RuleVariableDeclaration17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myAtl_RuleVariableDeclaration__myAtl_RuleVariableDeclaration17", None)
        self.__myAtl_RuleVariableDeclaration17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myAtl_CalledRule"):
                opp_val = getattr(old_value, "myAtl_CalledRule", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myAtl_CalledRule"):
                opp_val = getattr(value, "myAtl_CalledRule", None)
                if opp_val is None:
                    setattr(value, "myAtl_CalledRule", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def myAtl_RuleVariableDeclaration(self):
        return self.__myAtl_RuleVariableDeclaration

    @myAtl_RuleVariableDeclaration.setter
    def myAtl_RuleVariableDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myAtl_RuleVariableDeclaration__myAtl_RuleVariableDeclaration", None)
        self.__myAtl_RuleVariableDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myAtl_MatchedRule11"):
                opp_val = getattr(old_value, "myAtl_MatchedRule11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myAtl_MatchedRule11"):
                opp_val = getattr(value, "myAtl_MatchedRule11", None)
                if opp_val is None:
                    setattr(value, "myAtl_MatchedRule11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def myAtl_RuleVariableDeclaration40(self):
        return self.__myAtl_RuleVariableDeclaration40

    @myAtl_RuleVariableDeclaration40.setter
    def myAtl_RuleVariableDeclaration40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myAtl_RuleVariableDeclaration__myAtl_RuleVariableDeclaration40", None)
        self.__myAtl_RuleVariableDeclaration40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myAtl_ATLType41"):
                opp_val = getattr(old_value, "myAtl_ATLType41", None)
                if opp_val == self:
                    setattr(old_value, "myAtl_ATLType41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myAtl_ATLType41"):
                opp_val = getattr(value, "myAtl_ATLType41", None)
                setattr(value, "myAtl_ATLType41", self)

    @property
    def myAtl_RuleVariableDeclaration43(self):
        return self.__myAtl_RuleVariableDeclaration43

    @myAtl_RuleVariableDeclaration43.setter
    def myAtl_RuleVariableDeclaration43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myAtl_RuleVariableDeclaration__myAtl_RuleVariableDeclaration43", None)
        self.__myAtl_RuleVariableDeclaration43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myAtl_ExpCS44"):
                opp_val = getattr(old_value, "myAtl_ExpCS44", None)
                if opp_val == self:
                    setattr(old_value, "myAtl_ExpCS44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myAtl_ExpCS44"):
                opp_val = getattr(value, "myAtl_ExpCS44", None)
                setattr(value, "myAtl_ExpCS44", self)

class myAtl_InPattern:

    pass
class ModuleElement:

    pass
class myAtl_CalledRule(ModuleElement):

    pass
class myAtl_Helper(ModuleElement):

    pass
class myAtl_QueryRule(ModuleElement):

    pass
class myAtl_MatchedRule(ModuleElement):

    pass
class myAtl_ModuleElement:

    def __init__(self, name: str, myAtl_ModuleElement: "myAtl_Module" = None):
        self.name = name
        self.myAtl_ModuleElement = myAtl_ModuleElement
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myAtl_ModuleElement(self):
        return self.__myAtl_ModuleElement

    @myAtl_ModuleElement.setter
    def myAtl_ModuleElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myAtl_ModuleElement__myAtl_ModuleElement", None)
        self.__myAtl_ModuleElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myAtl_Module8"):
                opp_val = getattr(old_value, "myAtl_Module8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myAtl_Module8"):
                opp_val = getattr(value, "myAtl_Module8", None)
                if opp_val is None:
                    setattr(value, "myAtl_Module8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class myAtl_Module:

    def __init__(self, name: str, myAtl_Module8: set["myAtl_ModuleElement"] = None, myAtl_Module: set["myAtl_NameExpCS"] = None, myAtl_Module2: set["myAtl_NameExpCS"] = None, myAtl_Module5: "myAtl_NameExpCS" = None):
        self.name = name
        self.myAtl_Module8 = myAtl_Module8 if myAtl_Module8 is not None else set()
        self.myAtl_Module = myAtl_Module if myAtl_Module is not None else set()
        self.myAtl_Module2 = myAtl_Module2 if myAtl_Module2 is not None else set()
        self.myAtl_Module5 = myAtl_Module5
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myAtl_Module(self):
        return self.__myAtl_Module

    @myAtl_Module.setter
    def myAtl_Module(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myAtl_Module__myAtl_Module", None)
        self.__myAtl_Module = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "myAtl_NameExpCS"):
                    opp_val = getattr(item, "myAtl_NameExpCS", None)
                    
                    if opp_val == self:
                        setattr(item, "myAtl_NameExpCS", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "myAtl_NameExpCS"):
                    opp_val = getattr(item, "myAtl_NameExpCS", None)
                    
                    setattr(item, "myAtl_NameExpCS", self)
                    

    @property
    def myAtl_Module2(self):
        return self.__myAtl_Module2

    @myAtl_Module2.setter
    def myAtl_Module2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myAtl_Module__myAtl_Module2", None)
        self.__myAtl_Module2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "myAtl_NameExpCS3"):
                    opp_val = getattr(item, "myAtl_NameExpCS3", None)
                    
                    if opp_val == self:
                        setattr(item, "myAtl_NameExpCS3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "myAtl_NameExpCS3"):
                    opp_val = getattr(item, "myAtl_NameExpCS3", None)
                    
                    setattr(item, "myAtl_NameExpCS3", self)
                    

    @property
    def myAtl_Module8(self):
        return self.__myAtl_Module8

    @myAtl_Module8.setter
    def myAtl_Module8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myAtl_Module__myAtl_Module8", None)
        self.__myAtl_Module8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "myAtl_ModuleElement"):
                    opp_val = getattr(item, "myAtl_ModuleElement", None)
                    
                    if opp_val == self:
                        setattr(item, "myAtl_ModuleElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "myAtl_ModuleElement"):
                    opp_val = getattr(item, "myAtl_ModuleElement", None)
                    
                    setattr(item, "myAtl_ModuleElement", self)
                    

    @property
    def myAtl_Module5(self):
        return self.__myAtl_Module5

    @myAtl_Module5.setter
    def myAtl_Module5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myAtl_Module__myAtl_Module5", None)
        self.__myAtl_Module5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myAtl_NameExpCS6"):
                opp_val = getattr(old_value, "myAtl_NameExpCS6", None)
                if opp_val == self:
                    setattr(old_value, "myAtl_NameExpCS6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myAtl_NameExpCS6"):
                opp_val = getattr(value, "myAtl_NameExpCS6", None)
                setattr(value, "myAtl_NameExpCS6", self)
