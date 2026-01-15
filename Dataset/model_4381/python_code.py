from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class AdressSpaceEnum(Enum):
    real = "real"
    virtual = "virtual"
class TypeRunEnum(Enum):
    copy = "copy"
    hold = "hold"
    jclhold = "jclhold"
    scan = "scan"


############################################
# Definition of Classes
############################################

class jcl_waters_Water:

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class jcl_members_Member(ABC):

    pass
class jcl_conditions_ReturnCode(ABC):

    pass
class ReturnCode:

    pass
class conditions_PrimaryCondition:

    pass
class PrimaryCondition:

    pass
class jcl_conditions_NestedCondition(PrimaryCondition):

    pass
class jcl_conditions_Only(PrimaryCondition):

    pass
class jcl_conditions_Even(PrimaryCondition):

    pass
class jcl_conditions_Condition(ABC):

    pass
class jcl_references_ReferenceableElement(ABC):

    pass
class references_ElementReference:

    pass
class jcl_conditions_RelationalCondition(conditions_PrimaryCondition, references_ElementReference):

    pass
class ReferenceableElement:

    pass
class Reference:

    pass
class jcl_references_ElementReference(Reference):

    pass
class jcl_references_Reference(ABC):

    pass
class conditions_ReturnCode:

    pass
class literals_Literal:

    pass
class jcl_literals_Literal(ABC):

    pass
class LogicOperator:

    pass
class jcl_operators_Or(LogicOperator):

    pass
class jcl_operators_And(LogicOperator):

    pass
class Operator:

    pass
class jcl_operators_LogicOperator(Operator):

    pass
class jcl_operators_RelationOperator(Operator):

    pass
class jcl_operators_UnaryOperator(Operator):

    pass
class PhraseableElement:

    pass
class jcl_operators_Operator(PhraseableElement):

    pass
class IdentifierReference:

    pass
class expressions_PrimaryExpression:

    pass
class jcl_references_IdentifierReference(conditions_ReturnCode, references_ElementReference, expressions_PrimaryExpression):

    pass
class jcl_literals_IntegerLiteral(conditions_ReturnCode, literals_Literal, expressions_PrimaryExpression):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class PrimaryExpression:

    pass
class jcl_expressions_NestedExpression(PrimaryExpression):

    pass
class UnaryOperator:

    pass
class jcl_operators_Negate(UnaryOperator):

    pass
class UnaryExpressionChild:

    pass
class jcl_expressions_PrimaryExpression(UnaryExpressionChild):

    pass
class And:

    pass
class Or:

    pass
class ConditionalOrExpressionChild:

    pass
class jcl_expressions_ConditionalAndExpression(ConditionalOrExpressionChild):

    pass
class jcl_expressions_ConditionalAndExpressionChild(ConditionalOrExpressionChild):

    pass
class ConditionalExpression:

    pass
class jcl_expressions_ConditionalOrExpressionChild(ConditionalExpression):

    pass
class jcl_expressions_ConditionalOrExpression(ConditionalExpression):

    pass
class RelationOperator:

    pass
class jcl_operators_GreaterEqual(RelationOperator):

    pass
class jcl_operators_NotEqual(RelationOperator):

    pass
class jcl_operators_GreaterThan(RelationOperator):

    pass
class jcl_operators_Equal(RelationOperator):

    pass
class jcl_operators_LessThan(RelationOperator):

    pass
class jcl_operators_LessEqual(RelationOperator):

    pass
class RelationalExpressionChild:

    pass
class jcl_expressions_UnaryExpression(RelationalExpressionChild):

    pass
class jcl_expressions_UnaryExpressionChild(RelationalExpressionChild):

    pass
class ConditionalAndExpressionChild:

    pass
class jcl_expressions_RelationalExpressionChild(ConditionalAndExpressionChild):

    pass
class jcl_expressions_RelationalExpression(ConditionalAndExpressionChild):

    pass
class Expression:

    pass
class jcl_expressions_ConditionalExpression(Expression):

    pass
class jcl_expressions_Expression(ABC):

    pass
class ExecuteProgram:

    pass
class commons_IncompleteElement:

    pass
class containers_JCLRoot:

    pass
class Member:

    pass
class jcl_containers_JCLRoot:

    pass
class Execute:

    pass
class jcl_statements_ExecuteProcedure(Execute):

    def __init__(self, procedureName: str):
        self.procedureName = procedureName
        
    @property
    def procedureName(self) -> str:
        return self.__procedureName

    @procedureName.setter
    def procedureName(self, procedureName: str):
        self.__procedureName = procedureName

class jcl_statements_ExecuteProgram(Execute):

    def __init__(self, programName: str):
        self.programName = programName
        
    @property
    def programName(self) -> str:
        return self.__programName

    @programName.setter
    def programName(self, programName: str):
        self.__programName = programName

class EndControl:

    pass
class statements_Statement:

    pass
class statements_StatementContainer:

    pass
class jcl_statements_Condition(statements_Statement, statements_StatementContainer):

    def __init__(self, elseName: str, endName: str, jcl_statements_Condition: set["Statement"] = None, jcl_statements_Condition8: "Expression" = None):
        self.elseName = elseName
        self.endName = endName
        self.jcl_statements_Condition = jcl_statements_Condition if jcl_statements_Condition is not None else set()
        self.jcl_statements_Condition8 = jcl_statements_Condition8
        
    @property
    def elseName(self) -> str:
        return self.__elseName

    @elseName.setter
    def elseName(self, elseName: str):
        self.__elseName = elseName

    @property
    def endName(self) -> str:
        return self.__endName

    @endName.setter
    def endName(self, endName: str):
        self.__endName = endName

    @property
    def jcl_statements_Condition(self):
        return self.__jcl_statements_Condition

    @jcl_statements_Condition.setter
    def jcl_statements_Condition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jcl_statements_Condition__jcl_statements_Condition", None)
        self.__jcl_statements_Condition = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Statement6"):
                    opp_val = getattr(item, "Statement6", None)
                    
                    if opp_val == self:
                        setattr(item, "Statement6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Statement6"):
                    opp_val = getattr(item, "Statement6", None)
                    
                    setattr(item, "Statement6", self)
                    

    @property
    def jcl_statements_Condition8(self):
        return self.__jcl_statements_Condition8

    @jcl_statements_Condition8.setter
    def jcl_statements_Condition8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jcl_statements_Condition__jcl_statements_Condition8", None)
        self.__jcl_statements_Condition8 = value
        
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

class jcl_statements_StatementContainer(ABC):

    pass
class Statement:

    pass
class jcl_statements_EndControl(Statement):

    pass
class jcl_statements_Set(Statement):

    pass
class jcl_statements_Control(Statement):

    def __init__(self, endName: str, jcl_statements_Control: "EndControl" = None, Statement: "jcl_statements_StatementContainer", Statement6: "jcl_statements_Condition"):
        self.endName = endName
        self.jcl_statements_Control = jcl_statements_Control
        
    @property
    def endName(self) -> str:
        return self.__endName

    @endName.setter
    def endName(self, endName: str):
        self.__endName = endName

    @property
    def jcl_statements_Control(self):
        return self.__jcl_statements_Control

    @jcl_statements_Control.setter
    def jcl_statements_Control(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jcl_statements_Control__jcl_statements_Control", None)
        self.__jcl_statements_Control = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EndControl"):
                opp_val = getattr(old_value, "EndControl", None)
                if opp_val == self:
                    setattr(old_value, "EndControl", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EndControl"):
                opp_val = getattr(value, "EndControl", None)
                setattr(value, "EndControl", self)

class jcl_statements_Input(Statement):

    pass
class jcl_statements_JCLLibrary(Statement):

    pass
class jcl_statements_Include(Statement):

    pass
class jcl_statements_Output(Statement):

    pass
class jcl_statements_Command(Statement):

    def __init__(self, value: str, Statement: "jcl_statements_StatementContainer", Statement6: "jcl_statements_Condition"):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class jcl_statements_Execute(Statement):

    pass
class members_Member:

    pass
class commons_NamedElement:

    pass
class jcl_statements_Statement(commons_NamedElement, members_Member):

    pass
class jcl_procedures_Procedure(commons_NamedElement, members_Member, containers_JCLRoot):

    def __init__(self, endName: str):
        self.endName = endName
        
    @property
    def endName(self) -> str:
        return self.__endName

    @endName.setter
    def endName(self, endName: str):
        self.__endName = endName

class jcl_containers_JobUnit(containers_JCLRoot, commons_IncompleteElement, commons_NamedElement):

    pass
class Condition:

    pass
class jcl_conditions_PrimaryCondition(Condition):

    pass
class Literal:

    pass
class jcl_literals_SpecialLiteral(Literal):

    def __init__(self, value: str, Literal15: "jcl_containers_JobUnit", Literal: "jcl_parameters_AccountInfo"):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class jcl_literals_StringLiteral(Literal):

    def __init__(self, value: str, Literal15: "jcl_containers_JobUnit", Literal: "jcl_parameters_AccountInfo"):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class jcl_commons_ProcedureStepElement(ABC):

    def __init__(self, procStepName: str):
        self.procStepName = procStepName
        
    @property
    def procStepName(self) -> str:
        return self.__procStepName

    @procStepName.setter
    def procStepName(self, procStepName: str):
        self.__procStepName = procStepName

class commons_ProcedureStepElement:

    pass
class jcl_expressions_Run(expressions_PrimaryExpression, commons_ProcedureStepElement):

    pass
class jcl_expressions_Abend(expressions_PrimaryExpression, commons_ProcedureStepElement):

    pass
class jcl_statements_DataDefinition(statements_Statement, commons_ProcedureStepElement):

    pass
class parameters_Parameter:

    pass
class jcl_parameters_Other(commons_NamedElement, parameters_Parameter, commons_ProcedureStepElement):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class jcl_parameters_AccountInfo(parameters_Parameter, commons_ProcedureStepElement):

    pass
class jcl_parameters_Condition(parameters_Parameter, commons_ProcedureStepElement):

    pass
class jcl_parameters_Argument(parameters_Parameter, commons_ProcedureStepElement):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class jcl_parameters_AddressSpace(parameters_Parameter, commons_ProcedureStepElement):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class Parameter:

    pass
class jcl_parameters_JobClass(Parameter):

    def __init__(self, value: int, Parameter: "jcl_statements_Statement", Parameter12: "jcl_containers_JobUnit"):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class jcl_parameters_TypeRun(Parameter):

    def __init__(self, value: str, Parameter: "jcl_statements_Statement", Parameter12: "jcl_containers_JobUnit"):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class jcl_parameters_Bytes(Parameter):

    def __init__(self, value: int, Parameter: "jcl_statements_Statement", Parameter12: "jcl_containers_JobUnit"):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class jcl_parameters_MessageLevel(Parameter):

    def __init__(self, statements: int, messages: int, Parameter: "jcl_statements_Statement", Parameter12: "jcl_containers_JobUnit"):
        self.statements = statements
        self.messages = messages
        
    @property
    def statements(self) -> int:
        return self.__statements

    @statements.setter
    def statements(self, statements: int):
        self.__statements = statements

    @property
    def messages(self) -> int:
        return self.__messages

    @messages.setter
    def messages(self, messages: int):
        self.__messages = messages

class jcl_parameters_MessageClass(Parameter):

    def __init__(self, value: str, Parameter: "jcl_statements_Statement", Parameter12: "jcl_containers_JobUnit"):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class jcl_parameters_Password(Parameter):

    def __init__(self, old: str, new: str, Parameter: "jcl_statements_Statement", Parameter12: "jcl_containers_JobUnit"):
        self.old = old
        self.new = new
        
    @property
    def old(self) -> str:
        return self.__old

    @old.setter
    def old(self, old: str):
        self.__old = old

    @property
    def new(self) -> str:
        return self.__new

    @new.setter
    def new(self, new: str):
        self.__new = new

class jcl_parameters_UserID(Parameter):

    def __init__(self, value: str, Parameter: "jcl_statements_Statement", Parameter12: "jcl_containers_JobUnit"):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class jcl_parameters_DatasetName(Parameter):

    def __init__(self, value: str, Parameter: "jcl_statements_Statement", Parameter12: "jcl_containers_JobUnit"):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class jcl_parameters_Priority(Parameter):

    def __init__(self, value: int, Parameter: "jcl_statements_Statement", Parameter12: "jcl_containers_JobUnit"):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class jcl_parameters_Display(Parameter):

    def __init__(self, value: str, Parameter: "jcl_statements_Statement", Parameter12: "jcl_containers_JobUnit"):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class jcl_parameters_Parameter(ABC):

    pass
class Water:

    pass
class jcl_commons_IncompleteElement(ABC):

    pass
class jcl_commons_CommentableElement(ABC):

    def __init__(self, comment: str):
        self.comment = comment
        
    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

class jcl_commons_PhraseableElement:

    def __init__(self, isPhrase: bool):
        self.isPhrase = isPhrase
        
    @property
    def isPhrase(self) -> bool:
        return self.__isPhrase

    @isPhrase.setter
    def isPhrase(self, isPhrase: bool):
        self.__isPhrase = isPhrase

class jcl_commons_NamedElement:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name
