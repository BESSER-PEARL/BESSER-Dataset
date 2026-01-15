from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class expression_EObject:

    pass
class Term:

    pass
class expression_DoubleValue(Term):

    def __init__(self, value: float):
        self.value = value
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

class expression_IntegerValue(Term):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class expression_StringValue(Term):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class expression_List(Term):

    pass
class expression_KeyValuePairRest:

    pass
class KeyValuePairRest:

    pass
class expression_KeyValuePair(KeyValuePairRest):

    def __init__(self, key: str, expression_KeyValuePair: "expression_Expression" = None, expression_KeyValuePair25: set["expression_KeyValuePairRest"] = None, expression_KeyValuePair106: "expression_StructureExpression" = None):
        self.key = key
        self.expression_KeyValuePair = expression_KeyValuePair
        self.expression_KeyValuePair25 = expression_KeyValuePair25 if expression_KeyValuePair25 is not None else set()
        self.expression_KeyValuePair106 = expression_KeyValuePair106
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def expression_KeyValuePair106(self):
        return self.__expression_KeyValuePair106

    @expression_KeyValuePair106.setter
    def expression_KeyValuePair106(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expression_KeyValuePair__expression_KeyValuePair106", None)
        self.__expression_KeyValuePair106 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expression_StructureExpression"):
                opp_val = getattr(old_value, "expression_StructureExpression", None)
                if opp_val == self:
                    setattr(old_value, "expression_StructureExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expression_StructureExpression"):
                opp_val = getattr(value, "expression_StructureExpression", None)
                setattr(value, "expression_StructureExpression", self)

    @property
    def expression_KeyValuePair25(self):
        return self.__expression_KeyValuePair25

    @expression_KeyValuePair25.setter
    def expression_KeyValuePair25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expression_KeyValuePair__expression_KeyValuePair25", None)
        self.__expression_KeyValuePair25 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "expression_KeyValuePairRest"):
                    opp_val = getattr(item, "expression_KeyValuePairRest", None)
                    
                    if opp_val == self:
                        setattr(item, "expression_KeyValuePairRest", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "expression_KeyValuePairRest"):
                    opp_val = getattr(item, "expression_KeyValuePairRest", None)
                    
                    setattr(item, "expression_KeyValuePairRest", self)
                    

    @property
    def expression_KeyValuePair(self):
        return self.__expression_KeyValuePair

    @expression_KeyValuePair.setter
    def expression_KeyValuePair(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expression_KeyValuePair__expression_KeyValuePair", None)
        self.__expression_KeyValuePair = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expression_Expression23"):
                opp_val = getattr(old_value, "expression_Expression23", None)
                if opp_val == self:
                    setattr(old_value, "expression_Expression23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expression_Expression23"):
                opp_val = getattr(value, "expression_Expression23", None)
                setattr(value, "expression_Expression23", self)

class expression_ExpressionRest:

    pass
class expression_Procedure:

    pass
class expression_ProcedureCall:

    pass
class expression_ExpressionList:

    pass
class Function:

    pass
class Expression:

    pass
class expression_DashExpression(Expression):

    def __init__(self, op: str, expression_DashExpression: "expression_Expression" = None, expression_DashExpression50: "expression_Expression" = None):
        self.op = op
        self.expression_DashExpression = expression_DashExpression
        self.expression_DashExpression50 = expression_DashExpression50
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def expression_DashExpression(self):
        return self.__expression_DashExpression

    @expression_DashExpression.setter
    def expression_DashExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expression_DashExpression__expression_DashExpression", None)
        self.__expression_DashExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expression_Expression48"):
                opp_val = getattr(old_value, "expression_Expression48", None)
                if opp_val == self:
                    setattr(old_value, "expression_Expression48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expression_Expression48"):
                opp_val = getattr(value, "expression_Expression48", None)
                setattr(value, "expression_Expression48", self)

    @property
    def expression_DashExpression50(self):
        return self.__expression_DashExpression50

    @expression_DashExpression50.setter
    def expression_DashExpression50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expression_DashExpression__expression_DashExpression50", None)
        self.__expression_DashExpression50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expression_Expression51"):
                opp_val = getattr(old_value, "expression_Expression51", None)
                if opp_val == self:
                    setattr(old_value, "expression_Expression51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expression_Expression51"):
                opp_val = getattr(value, "expression_Expression51", None)
                setattr(value, "expression_Expression51", self)

class expression_UnaryExpression(Expression):

    pass
class expression_PowExpression(Expression):

    def __init__(self, op: str, expression_PowExpression: "expression_Expression" = None, expression_PowExpression60: "expression_Expression" = None):
        self.op = op
        self.expression_PowExpression = expression_PowExpression
        self.expression_PowExpression60 = expression_PowExpression60
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def expression_PowExpression(self):
        return self.__expression_PowExpression

    @expression_PowExpression.setter
    def expression_PowExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expression_PowExpression__expression_PowExpression", None)
        self.__expression_PowExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expression_Expression58"):
                opp_val = getattr(old_value, "expression_Expression58", None)
                if opp_val == self:
                    setattr(old_value, "expression_Expression58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expression_Expression58"):
                opp_val = getattr(value, "expression_Expression58", None)
                setattr(value, "expression_Expression58", self)

    @property
    def expression_PowExpression60(self):
        return self.__expression_PowExpression60

    @expression_PowExpression60.setter
    def expression_PowExpression60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expression_PowExpression__expression_PowExpression60", None)
        self.__expression_PowExpression60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expression_Expression61"):
                opp_val = getattr(old_value, "expression_Expression61", None)
                if opp_val == self:
                    setattr(old_value, "expression_Expression61", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expression_Expression61"):
                opp_val = getattr(value, "expression_Expression61", None)
                setattr(value, "expression_Expression61", self)

class expression_AndExpression(Expression):

    def __init__(self, op: str, expression_AndExpression: "expression_Expression" = None, expression_AndExpression40: "expression_Expression" = None):
        self.op = op
        self.expression_AndExpression = expression_AndExpression
        self.expression_AndExpression40 = expression_AndExpression40
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def expression_AndExpression40(self):
        return self.__expression_AndExpression40

    @expression_AndExpression40.setter
    def expression_AndExpression40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expression_AndExpression__expression_AndExpression40", None)
        self.__expression_AndExpression40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expression_Expression41"):
                opp_val = getattr(old_value, "expression_Expression41", None)
                if opp_val == self:
                    setattr(old_value, "expression_Expression41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expression_Expression41"):
                opp_val = getattr(value, "expression_Expression41", None)
                setattr(value, "expression_Expression41", self)

    @property
    def expression_AndExpression(self):
        return self.__expression_AndExpression

    @expression_AndExpression.setter
    def expression_AndExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expression_AndExpression__expression_AndExpression", None)
        self.__expression_AndExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expression_Expression38"):
                opp_val = getattr(old_value, "expression_Expression38", None)
                if opp_val == self:
                    setattr(old_value, "expression_Expression38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expression_Expression38"):
                opp_val = getattr(value, "expression_Expression38", None)
                setattr(value, "expression_Expression38", self)

class expression_ThereIsIn(Expression):

    pass
class expression_Apply(Expression):

    pass
class expression_EqualityExpression(Expression):

    def __init__(self, op: str, expression_EqualityExpression: "expression_Expression" = None, expression_EqualityExpression45: "expression_Expression" = None):
        self.op = op
        self.expression_EqualityExpression = expression_EqualityExpression
        self.expression_EqualityExpression45 = expression_EqualityExpression45
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def expression_EqualityExpression(self):
        return self.__expression_EqualityExpression

    @expression_EqualityExpression.setter
    def expression_EqualityExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expression_EqualityExpression__expression_EqualityExpression", None)
        self.__expression_EqualityExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expression_Expression43"):
                opp_val = getattr(old_value, "expression_Expression43", None)
                if opp_val == self:
                    setattr(old_value, "expression_Expression43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expression_Expression43"):
                opp_val = getattr(value, "expression_Expression43", None)
                setattr(value, "expression_Expression43", self)

    @property
    def expression_EqualityExpression45(self):
        return self.__expression_EqualityExpression45

    @expression_EqualityExpression45.setter
    def expression_EqualityExpression45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expression_EqualityExpression__expression_EqualityExpression45", None)
        self.__expression_EqualityExpression45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expression_Expression46"):
                opp_val = getattr(old_value, "expression_Expression46", None)
                if opp_val == self:
                    setattr(old_value, "expression_Expression46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expression_Expression46"):
                opp_val = getattr(value, "expression_Expression46", None)
                setattr(value, "expression_Expression46", self)

class expression_Term(Expression):

    pass
class expression_Count(Expression):

    pass
class expression_PointExpression(Expression):

    def __init__(self, op: str, expression_PointExpression: "expression_Expression" = None, expression_PointExpression55: "expression_Expression" = None):
        self.op = op
        self.expression_PointExpression = expression_PointExpression
        self.expression_PointExpression55 = expression_PointExpression55
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def expression_PointExpression55(self):
        return self.__expression_PointExpression55

    @expression_PointExpression55.setter
    def expression_PointExpression55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expression_PointExpression__expression_PointExpression55", None)
        self.__expression_PointExpression55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expression_Expression56"):
                opp_val = getattr(old_value, "expression_Expression56", None)
                if opp_val == self:
                    setattr(old_value, "expression_Expression56", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expression_Expression56"):
                opp_val = getattr(value, "expression_Expression56", None)
                setattr(value, "expression_Expression56", self)

    @property
    def expression_PointExpression(self):
        return self.__expression_PointExpression

    @expression_PointExpression.setter
    def expression_PointExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expression_PointExpression__expression_PointExpression", None)
        self.__expression_PointExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expression_Expression53"):
                opp_val = getattr(old_value, "expression_Expression53", None)
                if opp_val == self:
                    setattr(old_value, "expression_Expression53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expression_Expression53"):
                opp_val = getattr(value, "expression_Expression53", None)
                setattr(value, "expression_Expression53", self)

class expression_ForallIn(Expression):

    pass
class expression_OrExpression(Expression):

    def __init__(self, op: str, expression_OrExpression: "expression_Expression" = None, expression_OrExpression35: "expression_Expression" = None):
        self.op = op
        self.expression_OrExpression = expression_OrExpression
        self.expression_OrExpression35 = expression_OrExpression35
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def expression_OrExpression(self):
        return self.__expression_OrExpression

    @expression_OrExpression.setter
    def expression_OrExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expression_OrExpression__expression_OrExpression", None)
        self.__expression_OrExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expression_Expression33"):
                opp_val = getattr(old_value, "expression_Expression33", None)
                if opp_val == self:
                    setattr(old_value, "expression_Expression33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expression_Expression33"):
                opp_val = getattr(value, "expression_Expression33", None)
                setattr(value, "expression_Expression33", self)

    @property
    def expression_OrExpression35(self):
        return self.__expression_OrExpression35

    @expression_OrExpression35.setter
    def expression_OrExpression35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expression_OrExpression__expression_OrExpression35", None)
        self.__expression_OrExpression35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expression_Expression36"):
                opp_val = getattr(old_value, "expression_Expression36", None)
                if opp_val == self:
                    setattr(old_value, "expression_Expression36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expression_Expression36"):
                opp_val = getattr(value, "expression_Expression36", None)
                setattr(value, "expression_Expression36", self)

class expression_FirstIn(Expression):

    pass
class expression_Sum(Expression):

    pass
class expression_LastIn(Expression):

    pass
class expression_StructureExpression(Expression):

    pass
class expression_Map(Expression):

    pass
class expression_Reduce(Expression):

    pass
class expression_QualifierExpression(Expression):

    def __init__(self, op: str, expression_QualifierExpression: "expression_Expression" = None, expression_QualifierExpression65: "expression_Expression" = None):
        self.op = op
        self.expression_QualifierExpression = expression_QualifierExpression
        self.expression_QualifierExpression65 = expression_QualifierExpression65
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def expression_QualifierExpression65(self):
        return self.__expression_QualifierExpression65

    @expression_QualifierExpression65.setter
    def expression_QualifierExpression65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expression_QualifierExpression__expression_QualifierExpression65", None)
        self.__expression_QualifierExpression65 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expression_Expression66"):
                opp_val = getattr(old_value, "expression_Expression66", None)
                if opp_val == self:
                    setattr(old_value, "expression_Expression66", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expression_Expression66"):
                opp_val = getattr(value, "expression_Expression66", None)
                setattr(value, "expression_Expression66", self)

    @property
    def expression_QualifierExpression(self):
        return self.__expression_QualifierExpression

    @expression_QualifierExpression.setter
    def expression_QualifierExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expression_QualifierExpression__expression_QualifierExpression", None)
        self.__expression_QualifierExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expression_Expression63"):
                opp_val = getattr(old_value, "expression_Expression63", None)
                if opp_val == self:
                    setattr(old_value, "expression_Expression63", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expression_Expression63"):
                opp_val = getattr(value, "expression_Expression63", None)
                setattr(value, "expression_Expression63", self)

class expression_FunctionCall(Expression):

    pass
class ExpressionRest:

    pass
class expression_Designator(Term):

    pass
class AssignmentStatement:

    pass
class expression_SelfAssignmentStatement(AssignmentStatement):

    pass
class expression_VariableAssignmentStatement(AssignmentStatement):

    pass
class Statement:

    pass
class expression_AssignmentStatement(Statement):

    pass
class expression_Statement:

    pass
class Phrase:

    pass
class expression_Expression(Phrase, ExpressionRest):

    pass
class expression_StatementList(Phrase):

    pass
class expression_Phrase:

    pass
class expression_Model:

    pass