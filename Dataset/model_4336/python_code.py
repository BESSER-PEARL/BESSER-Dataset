from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Expression:

    pass
class Expression_Operation(Expression):

    def __init__(self, op: str, Operation: "Expression_Expression" = None, operation: "Expression_Expression" = None, Expression_Operation: "Expression_Expression" = None):
        self.op = op
        self.Operation = Operation
        self.operation = operation
        self.Expression_Operation = Expression_Operation
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def Expression_Operation(self):
        return self.__Expression_Operation

    @Expression_Operation.setter
    def Expression_Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Expression_Operation__Expression_Operation", None)
        self.__Expression_Operation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression_Expression"):
                opp_val = getattr(old_value, "Expression_Expression", None)
                if opp_val == self:
                    setattr(old_value, "Expression_Expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression_Expression"):
                opp_val = getattr(value, "Expression_Expression", None)
                setattr(value, "Expression_Expression", self)

    @property
    def Operation(self):
        return self.__Operation

    @Operation.setter
    def Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Expression_Operation__Operation", None)
        self.__Operation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "left"):
                opp_val = getattr(old_value, "left", None)
                if opp_val == self:
                    setattr(old_value, "left", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "left"):
                opp_val = getattr(value, "left", None)
                setattr(value, "left", self)

    @property
    def operation(self):
        return self.__operation

    @operation.setter
    def operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Expression_Operation__operation", None)
        self.__operation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression"):
                opp_val = getattr(old_value, "Expression", None)
                if opp_val == self:
                    setattr(old_value, "Expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression"):
                opp_val = getattr(value, "Expression", None)
                setattr(value, "Expression", self)

class Expression_Expression:

    def __init__(self, value: float, left: "Expression_Operation" = None, Expression: "Expression_Operation" = None, Expression_Expression: "Expression_Operation" = None):
        self.value = value
        self.left = left
        self.Expression = Expression
        self.Expression_Expression = Expression_Expression
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def Expression(self):
        return self.__Expression

    @Expression.setter
    def Expression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Expression_Expression__Expression", None)
        self.__Expression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operation"):
                opp_val = getattr(old_value, "operation", None)
                if opp_val == self:
                    setattr(old_value, "operation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operation"):
                opp_val = getattr(value, "operation", None)
                setattr(value, "operation", self)

    @property
    def Expression_Expression(self):
        return self.__Expression_Expression

    @Expression_Expression.setter
    def Expression_Expression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Expression_Expression__Expression_Expression", None)
        self.__Expression_Expression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression_Operation"):
                opp_val = getattr(old_value, "Expression_Operation", None)
                if opp_val == self:
                    setattr(old_value, "Expression_Operation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression_Operation"):
                opp_val = getattr(value, "Expression_Operation", None)
                setattr(value, "Expression_Operation", self)

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Expression_Expression__left", None)
        self.__left = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Operation"):
                opp_val = getattr(old_value, "Operation", None)
                if opp_val == self:
                    setattr(old_value, "Operation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Operation"):
                opp_val = getattr(value, "Operation", None)
                setattr(value, "Operation", self)
