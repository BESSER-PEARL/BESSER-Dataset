from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Literal:

    pass
class xs_VectorLiteral(Literal):

    pass
class xs_LiteralBool(Literal):

    def __init__(self, value: bool):
        self.value = value
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

class xs_LiteralInt(Literal):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class xs_LiteralFloat(Literal):

    def __init__(self, value: float):
        self.value = value
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

class xs_LiteralString(Literal):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class Type:

    pass
class xs_BoolType(Type):

    pass
class xs_VectorType(Type):

    pass
class xs_FloatType(Type):

    pass
class xs_VoidType(Type):

    pass
class xs_StringType(Type):

    pass
class xs_IntType(Type):

    pass
class xs_SwitchDefault:

    pass
class xs_SwitchCase:

    pass
class xs_Statement:

    pass
class Expression:

    pass
class xs_Factor(Expression):

    def __init__(self, op: str, xs_Factor: "xs_Expression" = None, xs_Factor92: "xs_Expression" = None):
        self.op = op
        self.xs_Factor = xs_Factor
        self.xs_Factor92 = xs_Factor92
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def xs_Factor(self):
        return self.__xs_Factor

    @xs_Factor.setter
    def xs_Factor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xs_Factor__xs_Factor", None)
        self.__xs_Factor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xs_Expression90"):
                opp_val = getattr(old_value, "xs_Expression90", None)
                if opp_val == self:
                    setattr(old_value, "xs_Expression90", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xs_Expression90"):
                opp_val = getattr(value, "xs_Expression90", None)
                setattr(value, "xs_Expression90", self)

    @property
    def xs_Factor92(self):
        return self.__xs_Factor92

    @xs_Factor92.setter
    def xs_Factor92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xs_Factor__xs_Factor92", None)
        self.__xs_Factor92 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xs_Expression93"):
                opp_val = getattr(old_value, "xs_Expression93", None)
                if opp_val == self:
                    setattr(old_value, "xs_Expression93", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xs_Expression93"):
                opp_val = getattr(value, "xs_Expression93", None)
                setattr(value, "xs_Expression93", self)

class xs_ComparisonExpression(Expression):

    def __init__(self, op: str, xs_ComparisonExpression82: "xs_Expression" = None, xs_ComparisonExpression: "xs_Expression" = None):
        self.op = op
        self.xs_ComparisonExpression82 = xs_ComparisonExpression82
        self.xs_ComparisonExpression = xs_ComparisonExpression
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def xs_ComparisonExpression82(self):
        return self.__xs_ComparisonExpression82

    @xs_ComparisonExpression82.setter
    def xs_ComparisonExpression82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xs_ComparisonExpression__xs_ComparisonExpression82", None)
        self.__xs_ComparisonExpression82 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xs_Expression83"):
                opp_val = getattr(old_value, "xs_Expression83", None)
                if opp_val == self:
                    setattr(old_value, "xs_Expression83", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xs_Expression83"):
                opp_val = getattr(value, "xs_Expression83", None)
                setattr(value, "xs_Expression83", self)

    @property
    def xs_ComparisonExpression(self):
        return self.__xs_ComparisonExpression

    @xs_ComparisonExpression.setter
    def xs_ComparisonExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xs_ComparisonExpression__xs_ComparisonExpression", None)
        self.__xs_ComparisonExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xs_Expression80"):
                opp_val = getattr(old_value, "xs_Expression80", None)
                if opp_val == self:
                    setattr(old_value, "xs_Expression80", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xs_Expression80"):
                opp_val = getattr(value, "xs_Expression80", None)
                setattr(value, "xs_Expression80", self)

class xs_EqualsExpression(Expression):

    def __init__(self, op: str, xs_EqualsExpression: "xs_Expression" = None, xs_EqualsExpression77: "xs_Expression" = None):
        self.op = op
        self.xs_EqualsExpression = xs_EqualsExpression
        self.xs_EqualsExpression77 = xs_EqualsExpression77
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def xs_EqualsExpression77(self):
        return self.__xs_EqualsExpression77

    @xs_EqualsExpression77.setter
    def xs_EqualsExpression77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xs_EqualsExpression__xs_EqualsExpression77", None)
        self.__xs_EqualsExpression77 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xs_Expression78"):
                opp_val = getattr(old_value, "xs_Expression78", None)
                if opp_val == self:
                    setattr(old_value, "xs_Expression78", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xs_Expression78"):
                opp_val = getattr(value, "xs_Expression78", None)
                setattr(value, "xs_Expression78", self)

    @property
    def xs_EqualsExpression(self):
        return self.__xs_EqualsExpression

    @xs_EqualsExpression.setter
    def xs_EqualsExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xs_EqualsExpression__xs_EqualsExpression", None)
        self.__xs_EqualsExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xs_Expression75"):
                opp_val = getattr(old_value, "xs_Expression75", None)
                if opp_val == self:
                    setattr(old_value, "xs_Expression75", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xs_Expression75"):
                opp_val = getattr(value, "xs_Expression75", None)
                setattr(value, "xs_Expression75", self)

class xs_Literal(Expression):

    pass
class xs_Call(Expression):

    pass
class xs_AndExpression(Expression):

    def __init__(self, op: str, xs_AndExpression: "xs_Expression" = None, xs_AndExpression72: "xs_Expression" = None):
        self.op = op
        self.xs_AndExpression = xs_AndExpression
        self.xs_AndExpression72 = xs_AndExpression72
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def xs_AndExpression72(self):
        return self.__xs_AndExpression72

    @xs_AndExpression72.setter
    def xs_AndExpression72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xs_AndExpression__xs_AndExpression72", None)
        self.__xs_AndExpression72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xs_Expression73"):
                opp_val = getattr(old_value, "xs_Expression73", None)
                if opp_val == self:
                    setattr(old_value, "xs_Expression73", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xs_Expression73"):
                opp_val = getattr(value, "xs_Expression73", None)
                setattr(value, "xs_Expression73", self)

    @property
    def xs_AndExpression(self):
        return self.__xs_AndExpression

    @xs_AndExpression.setter
    def xs_AndExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xs_AndExpression__xs_AndExpression", None)
        self.__xs_AndExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xs_Expression70"):
                opp_val = getattr(old_value, "xs_Expression70", None)
                if opp_val == self:
                    setattr(old_value, "xs_Expression70", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xs_Expression70"):
                opp_val = getattr(value, "xs_Expression70", None)
                setattr(value, "xs_Expression70", self)

class xs_OrExpression(Expression):

    def __init__(self, op: str, xs_OrExpression67: "xs_Expression" = None, xs_OrExpression: "xs_Expression" = None):
        self.op = op
        self.xs_OrExpression67 = xs_OrExpression67
        self.xs_OrExpression = xs_OrExpression
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def xs_OrExpression67(self):
        return self.__xs_OrExpression67

    @xs_OrExpression67.setter
    def xs_OrExpression67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xs_OrExpression__xs_OrExpression67", None)
        self.__xs_OrExpression67 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xs_Expression68"):
                opp_val = getattr(old_value, "xs_Expression68", None)
                if opp_val == self:
                    setattr(old_value, "xs_Expression68", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xs_Expression68"):
                opp_val = getattr(value, "xs_Expression68", None)
                setattr(value, "xs_Expression68", self)

    @property
    def xs_OrExpression(self):
        return self.__xs_OrExpression

    @xs_OrExpression.setter
    def xs_OrExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xs_OrExpression__xs_OrExpression", None)
        self.__xs_OrExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xs_Expression65"):
                opp_val = getattr(old_value, "xs_Expression65", None)
                if opp_val == self:
                    setattr(old_value, "xs_Expression65", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xs_Expression65"):
                opp_val = getattr(value, "xs_Expression65", None)
                setattr(value, "xs_Expression65", self)

class xs_Term(Expression):

    def __init__(self, op: str, xs_Term: "xs_Expression" = None, xs_Term87: "xs_Expression" = None):
        self.op = op
        self.xs_Term = xs_Term
        self.xs_Term87 = xs_Term87
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def xs_Term87(self):
        return self.__xs_Term87

    @xs_Term87.setter
    def xs_Term87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xs_Term__xs_Term87", None)
        self.__xs_Term87 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xs_Expression88"):
                opp_val = getattr(old_value, "xs_Expression88", None)
                if opp_val == self:
                    setattr(old_value, "xs_Expression88", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xs_Expression88"):
                opp_val = getattr(value, "xs_Expression88", None)
                setattr(value, "xs_Expression88", self)

    @property
    def xs_Term(self):
        return self.__xs_Term

    @xs_Term.setter
    def xs_Term(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xs_Term__xs_Term", None)
        self.__xs_Term = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xs_Expression85"):
                opp_val = getattr(old_value, "xs_Expression85", None)
                if opp_val == self:
                    setattr(old_value, "xs_Expression85", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xs_Expression85"):
                opp_val = getattr(value, "xs_Expression85", None)
                setattr(value, "xs_Expression85", self)

class xs_Assign(Expression):

    pass
class xs_Var(Expression):

    pass
class xs_Type:

    pass
class Statement:

    pass
class xs_WhileStatement(Statement):

    pass
class xs_PostfixStatement(Statement):

    def __init__(self, op: str, xs_PostfixStatement: "xs_VarDeclaration" = None):
        self.op = op
        self.xs_PostfixStatement = xs_PostfixStatement
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def xs_PostfixStatement(self):
        return self.__xs_PostfixStatement

    @xs_PostfixStatement.setter
    def xs_PostfixStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xs_PostfixStatement__xs_PostfixStatement", None)
        self.__xs_PostfixStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xs_VarDeclaration28"):
                opp_val = getattr(old_value, "xs_VarDeclaration28", None)
                if opp_val == self:
                    setattr(old_value, "xs_VarDeclaration28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xs_VarDeclaration28"):
                opp_val = getattr(value, "xs_VarDeclaration28", None)
                setattr(value, "xs_VarDeclaration28", self)

class xs_IfElseStatement(Statement):

    pass
class xs_SwitchStatement(Statement):

    pass
class xs_ContinueStatement(Statement):

    pass
class xs_ForStatement(Statement):

    def __init__(self, op: str, xs_ForStatement: "xs_ForVarDeclaration" = None, xs_ForStatement44: "xs_Expression" = None, xs_ForStatement47: "xs_Statement" = None):
        self.op = op
        self.xs_ForStatement = xs_ForStatement
        self.xs_ForStatement44 = xs_ForStatement44
        self.xs_ForStatement47 = xs_ForStatement47
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def xs_ForStatement47(self):
        return self.__xs_ForStatement47

    @xs_ForStatement47.setter
    def xs_ForStatement47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xs_ForStatement__xs_ForStatement47", None)
        self.__xs_ForStatement47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xs_Statement48"):
                opp_val = getattr(old_value, "xs_Statement48", None)
                if opp_val == self:
                    setattr(old_value, "xs_Statement48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xs_Statement48"):
                opp_val = getattr(value, "xs_Statement48", None)
                setattr(value, "xs_Statement48", self)

    @property
    def xs_ForStatement44(self):
        return self.__xs_ForStatement44

    @xs_ForStatement44.setter
    def xs_ForStatement44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xs_ForStatement__xs_ForStatement44", None)
        self.__xs_ForStatement44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xs_Expression45"):
                opp_val = getattr(old_value, "xs_Expression45", None)
                if opp_val == self:
                    setattr(old_value, "xs_Expression45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xs_Expression45"):
                opp_val = getattr(value, "xs_Expression45", None)
                setattr(value, "xs_Expression45", self)

    @property
    def xs_ForStatement(self):
        return self.__xs_ForStatement

    @xs_ForStatement.setter
    def xs_ForStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xs_ForStatement__xs_ForStatement", None)
        self.__xs_ForStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xs_ForVarDeclaration"):
                opp_val = getattr(old_value, "xs_ForVarDeclaration", None)
                if opp_val == self:
                    setattr(old_value, "xs_ForVarDeclaration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xs_ForVarDeclaration"):
                opp_val = getattr(value, "xs_ForVarDeclaration", None)
                setattr(value, "xs_ForVarDeclaration", self)

class xs_BreakStatement(Statement):

    pass
class xs_ReturnStatement(Statement):

    pass
class VarDeclaration:

    pass
class xs_LocalVarDeclaration(VarDeclaration, Statement):

    pass
class xs_Expression(Statement):

    pass
class xs_VarDeclaration:

    def __init__(self, name: str, xs_VarDeclaration: "xs_Expression" = None, xs_VarDeclaration26: "xs_Var" = None, xs_VarDeclaration28: "xs_PostfixStatement" = None):
        self.name = name
        self.xs_VarDeclaration = xs_VarDeclaration
        self.xs_VarDeclaration26 = xs_VarDeclaration26
        self.xs_VarDeclaration28 = xs_VarDeclaration28
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def xs_VarDeclaration(self):
        return self.__xs_VarDeclaration

    @xs_VarDeclaration.setter
    def xs_VarDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xs_VarDeclaration__xs_VarDeclaration", None)
        self.__xs_VarDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xs_Expression"):
                opp_val = getattr(old_value, "xs_Expression", None)
                if opp_val == self:
                    setattr(old_value, "xs_Expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xs_Expression"):
                opp_val = getattr(value, "xs_Expression", None)
                setattr(value, "xs_Expression", self)

    @property
    def xs_VarDeclaration28(self):
        return self.__xs_VarDeclaration28

    @xs_VarDeclaration28.setter
    def xs_VarDeclaration28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xs_VarDeclaration__xs_VarDeclaration28", None)
        self.__xs_VarDeclaration28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xs_PostfixStatement"):
                opp_val = getattr(old_value, "xs_PostfixStatement", None)
                if opp_val == self:
                    setattr(old_value, "xs_PostfixStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xs_PostfixStatement"):
                opp_val = getattr(value, "xs_PostfixStatement", None)
                setattr(value, "xs_PostfixStatement", self)

    @property
    def xs_VarDeclaration26(self):
        return self.__xs_VarDeclaration26

    @xs_VarDeclaration26.setter
    def xs_VarDeclaration26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xs_VarDeclaration__xs_VarDeclaration26", None)
        self.__xs_VarDeclaration26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xs_Var"):
                opp_val = getattr(old_value, "xs_Var", None)
                if opp_val == self:
                    setattr(old_value, "xs_Var", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xs_Var"):
                opp_val = getattr(value, "xs_Var", None)
                setattr(value, "xs_Var", self)

class Declaration:

    pass
class xs_IncludeDeclaration(Declaration):

    def __init__(self, filePath: str):
        self.filePath = filePath
        
    @property
    def filePath(self) -> str:
        return self.__filePath

    @filePath.setter
    def filePath(self, filePath: str):
        self.__filePath = filePath

class xs_Declaration:

    pass
class xs_Program:

    pass
class xs_RuleDeclaration(Declaration):

    def __init__(self, name: str, active: bool, runImmediately: bool, highFrequency: bool, group: str, minInterval: int, maxInterval: int, priority: int, xs_RuleDeclaration: "xs_Block" = None):
        self.name = name
        self.active = active
        self.runImmediately = runImmediately
        self.highFrequency = highFrequency
        self.group = group
        self.minInterval = minInterval
        self.maxInterval = maxInterval
        self.priority = priority
        self.xs_RuleDeclaration = xs_RuleDeclaration
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def minInterval(self) -> int:
        return self.__minInterval

    @minInterval.setter
    def minInterval(self, minInterval: int):
        self.__minInterval = minInterval

    @property
    def maxInterval(self) -> int:
        return self.__maxInterval

    @maxInterval.setter
    def maxInterval(self, maxInterval: int):
        self.__maxInterval = maxInterval

    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def highFrequency(self) -> bool:
        return self.__highFrequency

    @highFrequency.setter
    def highFrequency(self, highFrequency: bool):
        self.__highFrequency = highFrequency

    @property
    def priority(self) -> int:
        return self.__priority

    @priority.setter
    def priority(self, priority: int):
        self.__priority = priority

    @property
    def runImmediately(self) -> bool:
        return self.__runImmediately

    @runImmediately.setter
    def runImmediately(self, runImmediately: bool):
        self.__runImmediately = runImmediately

    @property
    def active(self) -> bool:
        return self.__active

    @active.setter
    def active(self, active: bool):
        self.__active = active

    @property
    def xs_RuleDeclaration(self):
        return self.__xs_RuleDeclaration

    @xs_RuleDeclaration.setter
    def xs_RuleDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xs_RuleDeclaration__xs_RuleDeclaration", None)
        self.__xs_RuleDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xs_Block15"):
                opp_val = getattr(old_value, "xs_Block15", None)
                if opp_val == self:
                    setattr(old_value, "xs_Block15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xs_Block15"):
                opp_val = getattr(value, "xs_Block15", None)
                setattr(value, "xs_Block15", self)

class xs_Block(Statement):

    pass
class xs_FunctionDeclaration(Declaration):

    def __init__(self, mutable: bool, name: str, xs_FunctionDeclaration: "xs_Type" = None, xs_FunctionDeclaration10: set["xs_ParameterDeclaration"] = None, xs_FunctionDeclaration13: "xs_Block" = None, xs_FunctionDeclaration95: "xs_Call" = None):
        self.mutable = mutable
        self.name = name
        self.xs_FunctionDeclaration = xs_FunctionDeclaration
        self.xs_FunctionDeclaration10 = xs_FunctionDeclaration10 if xs_FunctionDeclaration10 is not None else set()
        self.xs_FunctionDeclaration13 = xs_FunctionDeclaration13
        self.xs_FunctionDeclaration95 = xs_FunctionDeclaration95
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mutable(self) -> bool:
        return self.__mutable

    @mutable.setter
    def mutable(self, mutable: bool):
        self.__mutable = mutable

    @property
    def xs_FunctionDeclaration10(self):
        return self.__xs_FunctionDeclaration10

    @xs_FunctionDeclaration10.setter
    def xs_FunctionDeclaration10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xs_FunctionDeclaration__xs_FunctionDeclaration10", None)
        self.__xs_FunctionDeclaration10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xs_ParameterDeclaration11"):
                    opp_val = getattr(item, "xs_ParameterDeclaration11", None)
                    
                    if opp_val == self:
                        setattr(item, "xs_ParameterDeclaration11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xs_ParameterDeclaration11"):
                    opp_val = getattr(item, "xs_ParameterDeclaration11", None)
                    
                    setattr(item, "xs_ParameterDeclaration11", self)
                    

    @property
    def xs_FunctionDeclaration(self):
        return self.__xs_FunctionDeclaration

    @xs_FunctionDeclaration.setter
    def xs_FunctionDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xs_FunctionDeclaration__xs_FunctionDeclaration", None)
        self.__xs_FunctionDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xs_Type8"):
                opp_val = getattr(old_value, "xs_Type8", None)
                if opp_val == self:
                    setattr(old_value, "xs_Type8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xs_Type8"):
                opp_val = getattr(value, "xs_Type8", None)
                setattr(value, "xs_Type8", self)

    @property
    def xs_FunctionDeclaration95(self):
        return self.__xs_FunctionDeclaration95

    @xs_FunctionDeclaration95.setter
    def xs_FunctionDeclaration95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xs_FunctionDeclaration__xs_FunctionDeclaration95", None)
        self.__xs_FunctionDeclaration95 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xs_Call"):
                opp_val = getattr(old_value, "xs_Call", None)
                if opp_val == self:
                    setattr(old_value, "xs_Call", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xs_Call"):
                opp_val = getattr(value, "xs_Call", None)
                setattr(value, "xs_Call", self)

    @property
    def xs_FunctionDeclaration13(self):
        return self.__xs_FunctionDeclaration13

    @xs_FunctionDeclaration13.setter
    def xs_FunctionDeclaration13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xs_FunctionDeclaration__xs_FunctionDeclaration13", None)
        self.__xs_FunctionDeclaration13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xs_Block"):
                opp_val = getattr(old_value, "xs_Block", None)
                if opp_val == self:
                    setattr(old_value, "xs_Block", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xs_Block"):
                opp_val = getattr(value, "xs_Block", None)
                setattr(value, "xs_Block", self)

class xs_ForVarDeclaration(VarDeclaration):

    pass
class xs_ParameterDeclaration(VarDeclaration):

    pass
class xs_GlobalVarDeclaration(VarDeclaration, Declaration):

    def __init__(self, const: bool, extern: bool, xs_GlobalVarDeclaration: "xs_Type" = None):
        self.const = const
        self.extern = extern
        self.xs_GlobalVarDeclaration = xs_GlobalVarDeclaration
        
    @property
    def const(self) -> bool:
        return self.__const

    @const.setter
    def const(self, const: bool):
        self.__const = const

    @property
    def extern(self) -> bool:
        return self.__extern

    @extern.setter
    def extern(self, extern: bool):
        self.__extern = extern

    @property
    def xs_GlobalVarDeclaration(self):
        return self.__xs_GlobalVarDeclaration

    @xs_GlobalVarDeclaration.setter
    def xs_GlobalVarDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xs_GlobalVarDeclaration__xs_GlobalVarDeclaration", None)
        self.__xs_GlobalVarDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xs_Type4"):
                opp_val = getattr(old_value, "xs_Type4", None)
                if opp_val == self:
                    setattr(old_value, "xs_Type4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xs_Type4"):
                opp_val = getattr(value, "xs_Type4", None)
                setattr(value, "xs_Type4", self)
