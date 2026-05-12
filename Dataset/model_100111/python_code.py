from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Literal:

    pass
class d3ql_StringLiteral(Literal):

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class d3ql_BooleanLiteral(Literal):

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class d3ql_IntegerLiteral(Literal):

    def __init__(self, value: int):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value


class d3ql_Literal:

    pass
class d3ql_FunctionArgument:

    pass
class d3ql_FunctionCall:

    def __init__(self, function: str, d3ql_FunctionCall: set["d3ql_FunctionArgument"] = None):
        self.function = function
        self.d3ql_FunctionCall = d3ql_FunctionCall if d3ql_FunctionCall is not None else set()
        
        pass
    @property
    def function(self):
        return self.__function

    @function.setter
    def function(self, function: str):
        self.__function = function


    @property
    def d3ql_FunctionCall(self):
        return self.__d3ql_FunctionCall

    @d3ql_FunctionCall.setter
    def d3ql_FunctionCall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_d3ql_FunctionCall__d3ql_FunctionCall", None)
        self.__d3ql_FunctionCall = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "d3ql_FunctionArgument"):
                    opp_val = getattr(item, "d3ql_FunctionArgument", None)
                    
                    if opp_val == self:
                        setattr(item, "d3ql_FunctionArgument", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "d3ql_FunctionArgument"):
                    opp_val = getattr(item, "d3ql_FunctionArgument", None)
                    
                    setattr(item, "d3ql_FunctionArgument", self)
                    

class d3ql_PathElement:

    def __init__(self, name: str, d3ql_PathElement: "d3ql_PathExpression" = None):
        self.name = name
        self.d3ql_PathElement = d3ql_PathElement
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def d3ql_PathElement(self):
        return self.__d3ql_PathElement

    @d3ql_PathElement.setter
    def d3ql_PathElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_d3ql_PathElement__d3ql_PathElement", None)
        self.__d3ql_PathElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "d3ql_PathExpression16"):
                opp_val = getattr(old_value, "d3ql_PathExpression16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "d3ql_PathExpression16"):
                opp_val = getattr(value, "d3ql_PathExpression16", None)
                if opp_val is None:
                    setattr(value, "d3ql_PathExpression16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class d3ql_PathExpression:

    pass
class d3ql_EObject:

    pass
class d3ql_SelectExpression:

    pass
class Named:

    pass
class d3ql_Alias(Named):

    pass
class d3ql_Named:

    def __init__(self, name: str, d3ql_Named: "d3ql_PathExpression" = None):
        self.name = name
        self.d3ql_Named = d3ql_Named
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def d3ql_Named(self):
        return self.__d3ql_Named

    @d3ql_Named.setter
    def d3ql_Named(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_d3ql_Named__d3ql_Named", None)
        self.__d3ql_Named = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "d3ql_PathExpression"):
                opp_val = getattr(old_value, "d3ql_PathExpression", None)
                if opp_val == self:
                    setattr(old_value, "d3ql_PathExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "d3ql_PathExpression"):
                opp_val = getattr(value, "d3ql_PathExpression", None)
                setattr(value, "d3ql_PathExpression", self)

class d3ql_AggregateRoot(Named):

    pass
class d3ql_SelectStatement:

    pass
class d3ql_FromStatement:

    pass
class d3ql_Query:

    pass