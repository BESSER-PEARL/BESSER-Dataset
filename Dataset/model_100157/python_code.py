from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Operator(Enum):
    lessThen = "lessThen"
    greaterThen = "greaterThen"
    lessEqual = "lessEqual"
    greaterEqual = "greaterEqual"
    equal = "equal"
    notEqual = "notEqual"
    like = "like"
    notLike = "notLike"
    notIn = "notIn"
    in_ = "in_"
class ArrayOperator(Enum):
    mongo_all = "mongo_all"
    mongo_in = "mongo_in"
    sql_in = "sql_in"
    mongo_nin = "mongo_nin"
    sql_notIn = "sql_notIn"


############################################
# Definition of Classes
############################################

class ArrayExpression:

    pass
class query_NullArrayExpression(ArrayExpression):

    def __init__(self, values: str):
        self.values = values
        
        pass
    @property
    def values(self):
        return self.__values

    @values.setter
    def values(self, values: str):
        self.__values = values


class query_DateArrayExpression(ArrayExpression):

    def __init__(self, values: date):
        self.values = values
        
        pass
    @property
    def values(self):
        return self.__values

    @values.setter
    def values(self, values: date):
        self.__values = values


class query_LongArrayExpression(ArrayExpression):

    def __init__(self, values: str):
        self.values = values
        
        pass
    @property
    def values(self):
        return self.__values

    @values.setter
    def values(self, values: str):
        self.__values = values


class query_BooleanArrayExpression(ArrayExpression):

    def __init__(self, values: str):
        self.values = values
        
        pass
    @property
    def values(self):
        return self.__values

    @values.setter
    def values(self, values: str):
        self.__values = values


class query_StringArrayExpression(ArrayExpression):

    def __init__(self, values: str):
        self.values = values
        
        pass
    @property
    def values(self):
        return self.__values

    @values.setter
    def values(self, values: str):
        self.__values = values


class query_DoubleArrayExpression(ArrayExpression):

    def __init__(self, values: float):
        self.values = values
        
        pass
    @property
    def values(self):
        return self.__values

    @values.setter
    def values(self, values: float):
        self.__values = values


class query_ArrayExpression:

    pass
class Expression:

    pass
class query_DoubleExpression(Expression):

    def __init__(self, value: float):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value


class query_StringExpression(Expression):

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class query_BooleanExpression(Expression):

    def __init__(self, true: str):
        self.true = true
        
        pass
    @property
    def true(self):
        return self.__true

    @true.setter
    def true(self, true: str):
        self.__true = true


class query_NullExpression(Expression):

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class query_LongExpression(Expression):

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class query_DateExpression(Expression):

    def __init__(self, value: date):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: date):
        self.__value = value


class query_ReplacableValue(Expression):

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class query_Expression:

    pass
class ExpressionWhereEntry:

    pass
class query_MultiExpressionWhereEntry(ExpressionWhereEntry):

    def __init__(self, operator: str, query_MultiExpressionWhereEntry: "query_ArrayExpression" = None):
        self.operator = operator
        self.query_MultiExpressionWhereEntry = query_MultiExpressionWhereEntry
        
        pass
    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator


    @property
    def query_MultiExpressionWhereEntry(self):
        return self.__query_MultiExpressionWhereEntry

    @query_MultiExpressionWhereEntry.setter
    def query_MultiExpressionWhereEntry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_MultiExpressionWhereEntry__query_MultiExpressionWhereEntry", None)
        self.__query_MultiExpressionWhereEntry = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "query_ArrayExpression"):
                opp_val = getattr(old_value, "query_ArrayExpression", None)
                if opp_val == self:
                    setattr(old_value, "query_ArrayExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "query_ArrayExpression"):
                opp_val = getattr(value, "query_ArrayExpression", None)
                setattr(value, "query_ArrayExpression", self)

class query_SingleExpressionWhereEntry(ExpressionWhereEntry):

    def __init__(self, operator: str, query_SingleExpressionWhereEntry: "query_Expression" = None):
        self.operator = operator
        self.query_SingleExpressionWhereEntry = query_SingleExpressionWhereEntry
        
        pass
    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator


    @property
    def query_SingleExpressionWhereEntry(self):
        return self.__query_SingleExpressionWhereEntry

    @query_SingleExpressionWhereEntry.setter
    def query_SingleExpressionWhereEntry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_SingleExpressionWhereEntry__query_SingleExpressionWhereEntry", None)
        self.__query_SingleExpressionWhereEntry = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "query_Expression"):
                opp_val = getattr(old_value, "query_Expression", None)
                if opp_val == self:
                    setattr(old_value, "query_Expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "query_Expression"):
                opp_val = getattr(value, "query_Expression", None)
                setattr(value, "query_Expression", self)

class WhereEntry:

    pass
class query_AndWhereEntry(WhereEntry):

    pass
class query_OrWhereEntry(WhereEntry):

    pass
class query_ExpressionWhereEntry(WhereEntry):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class query_WhereEntry:

    pass
class query_Database:

    def __init__(self, url: str, port: str, dbName: str, name: str, query_Database: "query_Model" = None):
        self.url = url
        self.port = port
        self.dbName = dbName
        self.name = name
        self.query_Database = query_Database
        
        pass
    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, url: str):
        self.__url = url


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def port(self):
        return self.__port

    @port.setter
    def port(self, port: str):
        self.__port = port


    @property
    def dbName(self):
        return self.__dbName

    @dbName.setter
    def dbName(self, dbName: str):
        self.__dbName = dbName


    @property
    def query_Database(self):
        return self.__query_Database

    @query_Database.setter
    def query_Database(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_Database__query_Database", None)
        self.__query_Database = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "query_Model"):
                opp_val = getattr(old_value, "query_Model", None)
                if opp_val == self:
                    setattr(old_value, "query_Model", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "query_Model"):
                opp_val = getattr(value, "query_Model", None)
                setattr(value, "query_Model", self)

class query_Model:

    def __init__(self, attrs: str, query_Model: "query_Database" = None, query_Model2: "query_WhereEntry" = None):
        self.attrs = attrs
        self.query_Model = query_Model
        self.query_Model2 = query_Model2
        
        pass
    @property
    def attrs(self):
        return self.__attrs

    @attrs.setter
    def attrs(self, attrs: str):
        self.__attrs = attrs


    @property
    def query_Model2(self):
        return self.__query_Model2

    @query_Model2.setter
    def query_Model2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_Model__query_Model2", None)
        self.__query_Model2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "query_WhereEntry"):
                opp_val = getattr(old_value, "query_WhereEntry", None)
                if opp_val == self:
                    setattr(old_value, "query_WhereEntry", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "query_WhereEntry"):
                opp_val = getattr(value, "query_WhereEntry", None)
                setattr(value, "query_WhereEntry", self)

    @property
    def query_Model(self):
        return self.__query_Model

    @query_Model.setter
    def query_Model(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_Model__query_Model", None)
        self.__query_Model = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "query_Database"):
                opp_val = getattr(old_value, "query_Database", None)
                if opp_val == self:
                    setattr(old_value, "query_Database", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "query_Database"):
                opp_val = getattr(value, "query_Database", None)
                setattr(value, "query_Database", self)
