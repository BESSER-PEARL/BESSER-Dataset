from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class type(Enum):
    BOOLEAN = "BOOLEAN"
    INTEGER = "INTEGER"
    STRING = "STRING"


############################################
# Definition of Classes
############################################

class pascal_repetitive_arit_expression:

    def __init__(self, op: str, value: str, pascal_repetitive_arit_expression: "pascal_arit_expression" = None, pascal_repetitive_arit_expression16: "pascal_repetitive_arit_expression" = None, pascal_repetitive_arit_expression14: set["pascal_repetitive_arit_expression"] = None):
        self.op = op
        self.value = value
        self.pascal_repetitive_arit_expression = pascal_repetitive_arit_expression
        self.pascal_repetitive_arit_expression16 = pascal_repetitive_arit_expression16
        self.pascal_repetitive_arit_expression14 = pascal_repetitive_arit_expression14 if pascal_repetitive_arit_expression14 is not None else set()
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def pascal_repetitive_arit_expression(self):
        return self.__pascal_repetitive_arit_expression

    @pascal_repetitive_arit_expression.setter
    def pascal_repetitive_arit_expression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_repetitive_arit_expression__pascal_repetitive_arit_expression", None)
        self.__pascal_repetitive_arit_expression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_arit_expression"):
                opp_val = getattr(old_value, "pascal_arit_expression", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_arit_expression"):
                opp_val = getattr(value, "pascal_arit_expression", None)
                if opp_val is None:
                    setattr(value, "pascal_arit_expression", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pascal_repetitive_arit_expression14(self):
        return self.__pascal_repetitive_arit_expression14

    @pascal_repetitive_arit_expression14.setter
    def pascal_repetitive_arit_expression14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_repetitive_arit_expression__pascal_repetitive_arit_expression14", None)
        self.__pascal_repetitive_arit_expression14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pascal_repetitive_arit_expression16"):
                    opp_val = getattr(item, "pascal_repetitive_arit_expression16", None)
                    
                    if opp_val == self:
                        setattr(item, "pascal_repetitive_arit_expression16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pascal_repetitive_arit_expression16"):
                    opp_val = getattr(item, "pascal_repetitive_arit_expression16", None)
                    
                    setattr(item, "pascal_repetitive_arit_expression16", self)
                    

    @property
    def pascal_repetitive_arit_expression16(self):
        return self.__pascal_repetitive_arit_expression16

    @pascal_repetitive_arit_expression16.setter
    def pascal_repetitive_arit_expression16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_repetitive_arit_expression__pascal_repetitive_arit_expression16", None)
        self.__pascal_repetitive_arit_expression16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_repetitive_arit_expression14"):
                opp_val = getattr(old_value, "pascal_repetitive_arit_expression14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_repetitive_arit_expression14"):
                opp_val = getattr(value, "pascal_repetitive_arit_expression14", None)
                if opp_val is None:
                    setattr(value, "pascal_repetitive_arit_expression14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class expression:

    pass
class pascal_rel_expression(expression):

    def __init__(self, open: str, first: str, op: str, second: str, close: str):
        self.open = open
        self.first = first
        self.op = op
        self.second = second
        self.close = close
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def open(self) -> str:
        return self.__open

    @open.setter
    def open(self, open: str):
        self.__open = open

    @property
    def first(self) -> str:
        return self.__first

    @first.setter
    def first(self, first: str):
        self.__first = first

    @property
    def close(self) -> str:
        return self.__close

    @close.setter
    def close(self, close: str):
        self.__close = close

    @property
    def second(self) -> str:
        return self.__second

    @second.setter
    def second(self, second: str):
        self.__second = second

class pascal_arit_expression(expression):

    def __init__(self, value: str, pascal_arit_expression: set["pascal_repetitive_arit_expression"] = None):
        self.value = value
        self.pascal_arit_expression = pascal_arit_expression if pascal_arit_expression is not None else set()
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def pascal_arit_expression(self):
        return self.__pascal_arit_expression

    @pascal_arit_expression.setter
    def pascal_arit_expression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_arit_expression__pascal_arit_expression", None)
        self.__pascal_arit_expression = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pascal_repetitive_arit_expression"):
                    opp_val = getattr(item, "pascal_repetitive_arit_expression", None)
                    
                    if opp_val == self:
                        setattr(item, "pascal_repetitive_arit_expression", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pascal_repetitive_arit_expression"):
                    opp_val = getattr(item, "pascal_repetitive_arit_expression", None)
                    
                    setattr(item, "pascal_repetitive_arit_expression", self)
                    

class pascal_expression:

    pass
class pascal_atrib:

    def __init__(self, var_id: str, pascal_atrib: "pascal_statement" = None, pascal_atrib12: "pascal_expression" = None):
        self.var_id = var_id
        self.pascal_atrib = pascal_atrib
        self.pascal_atrib12 = pascal_atrib12
        
    @property
    def var_id(self) -> str:
        return self.__var_id

    @var_id.setter
    def var_id(self, var_id: str):
        self.__var_id = var_id

    @property
    def pascal_atrib(self):
        return self.__pascal_atrib

    @pascal_atrib.setter
    def pascal_atrib(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_atrib__pascal_atrib", None)
        self.__pascal_atrib = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_statement10"):
                opp_val = getattr(old_value, "pascal_statement10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_statement10"):
                opp_val = getattr(value, "pascal_statement10", None)
                if opp_val is None:
                    setattr(value, "pascal_statement10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pascal_atrib12(self):
        return self.__pascal_atrib12

    @pascal_atrib12.setter
    def pascal_atrib12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_atrib__pascal_atrib12", None)
        self.__pascal_atrib12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_expression"):
                opp_val = getattr(old_value, "pascal_expression", None)
                if opp_val == self:
                    setattr(old_value, "pascal_expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_expression"):
                opp_val = getattr(value, "pascal_expression", None)
                setattr(value, "pascal_expression", self)

class pascal_statement:

    pass
class pascal_var_list:

    def __init__(self, var_id: str, var_ids: str, var_type: str):
        self.var_id = var_id
        self.var_ids = var_ids
        self.var_type = var_type
        
    @property
    def var_id(self) -> str:
        return self.__var_id

    @var_id.setter
    def var_id(self, var_id: str):
        self.__var_id = var_id

    @property
    def var_type(self) -> str:
        return self.__var_type

    @var_type.setter
    def var_type(self, var_type: str):
        self.__var_type = var_type

    @property
    def var_ids(self) -> str:
        return self.__var_ids

    @var_ids.setter
    def var_ids(self, var_ids: str):
        self.__var_ids = var_ids

class pascal_var_decl:

    def __init__(self, var_id: str, var_type: str, value: str):
        self.var_id = var_id
        self.var_type = var_type
        self.value = value
        
    @property
    def var_id(self) -> str:
        return self.__var_id

    @var_id.setter
    def var_id(self, var_id: str):
        self.__var_id = var_id

    @property
    def var_type(self) -> str:
        return self.__var_type

    @var_type.setter
    def var_type(self, var_type: str):
        self.__var_type = var_type

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class pascal_EObject:

    pass
class pascal_block:

    pass
class pascal_var_block:

    pass
class pascal_program:

    def __init__(self, name: str, pascal_program: "pascal_Pascal" = None):
        self.name = name
        self.pascal_program = pascal_program
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def pascal_program(self):
        return self.__pascal_program

    @pascal_program.setter
    def pascal_program(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_program__pascal_program", None)
        self.__pascal_program = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_Pascal"):
                opp_val = getattr(old_value, "pascal_Pascal", None)
                if opp_val == self:
                    setattr(old_value, "pascal_Pascal", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_Pascal"):
                opp_val = getattr(value, "pascal_Pascal", None)
                setattr(value, "pascal_Pascal", self)

class pascal_Pascal:

    pass