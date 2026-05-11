from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class ExecutionOrder(Enum):
    l2r = "l2r"
    r2l = "r2l"
    interleaved = "interleaved"


############################################
# Definition of Classes
############################################

class kernel_references_ElementReference(ABC):

    pass
class kernel_references_Reference(ABC):

    pass
class NamedElement:

    pass
class kernel_references_ReferenceableElement(NamedElement):

    pass
class ReferenceableElement:

    pass
class DataItem:

    pass
class kernel_parameters_Parameter(DataItem):

    def __init__(self, correspondingArgument: str, byReference: bool):
        self.correspondingArgument = correspondingArgument
        self.byReference = byReference
        
        pass
    @property
    def correspondingArgument(self):
        return self.__correspondingArgument

    @correspondingArgument.setter
    def correspondingArgument(self, correspondingArgument: str):
        self.__correspondingArgument = correspondingArgument


    @property
    def byReference(self):
        return self.__byReference

    @byReference.setter
    def byReference(self, byReference: bool):
        self.__byReference = byReference


class commons_Variable:

    pass
class kernel_members_Member(ABC):

    pass
class MainProcedure:

    pass
class KernelRoot:

    pass
class kernel_containers_CompilationUnit(KernelRoot):

    pass
class Usage:

    pass
class kernel_expressions_Uses(Usage):

    pass
class Definition:

    pass
class kernel_expressions_Affects(Definition):

    pass
class kernel_expressions_Defines(Definition):

    pass
class ElementReference:

    pass
class kernel_references_Argument(ElementReference):

    def __init__(self):
        
        pass
    def getCorrespondingParameter(self) :
        # TODO: Implement getCorrespondingParameter method
        pass

class kernel_expressions_SubExpression(ElementReference):

    pass
class SubExpression:

    pass
class kernel_expressions_Usage(SubExpression):

    pass
class kernel_expressions_Definition(SubExpression):

    pass
class End:

    pass
class Start:

    pass
class ProcedureCall:

    pass
class Parameter:

    pass
class Member:

    pass
class references_ReferenceableElement:

    pass
class procedures_Procedure:

    pass
class ReturnSite:

    pass
class Argument:

    pass
class references_ElementReference:

    pass
class procedures_ProcedureCall:

    pass
class Expression:

    pass
class kernel_statements_Conditional(ABC):

    pass
class ExceptionHandlerStatement:

    pass
class Jump:

    pass
class kernel_statements_Goto(Jump):

    pass
class LabellableElement:

    pass
class kernel_containers_KernelRoot(LabellableElement):

    pass
class kernel_expressions_Expression(LabellableElement):

    def __init__(self, kernel_expressions_Expression: set["SubExpression"] = None, LabellableElement: "kernel_statements_Jump" = None):
        self.kernel_expressions_Expression = kernel_expressions_Expression if kernel_expressions_Expression is not None else set()
        
        pass
    @property
    def kernel_expressions_Expression(self):
        return self.__kernel_expressions_Expression

    @kernel_expressions_Expression.setter
    def kernel_expressions_Expression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kernel_expressions_Expression__kernel_expressions_Expression", None)
        self.__kernel_expressions_Expression = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SubExpression"):
                    opp_val = getattr(item, "SubExpression", None)
                    
                    if opp_val == self:
                        setattr(item, "SubExpression", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SubExpression"):
                    opp_val = getattr(item, "SubExpression", None)
                    
                    setattr(item, "SubExpression", self)
                    

    def getUsedVariables(self) :
        # TODO: Implement getUsedVariables method
        pass

    def getDefinedVariables(self) :
        # TODO: Implement getDefinedVariables method
        pass

class kernel_procedures_MainProcedure(LabellableElement):

    pass
class statements_StatementListContainer:

    pass
class statements_Conditional:

    pass
class statements_StatementContainer:

    pass
class statements_Statement:

    pass
class kernel_statements_Block(statements_StatementListContainer, statements_Statement):

    pass
class kernel_statements_ParallelBlock(statements_StatementListContainer, statements_Statement):

    def __init__(self, order: str):
        self.order = order
        
        pass
    @property
    def order(self):
        return self.__order

    @order.setter
    def order(self, order: str):
        self.__order = order


class kernel_statements_StatementWithException(statements_StatementContainer, statements_Statement):

    pass
class kernel_statements_NonDeterministicBlock(statements_StatementListContainer, statements_Statement):

    pass
class kernel_statements_ProcedureCall(references_ElementReference, statements_Statement, procedures_ProcedureCall):

    pass
class kernel_statements_WhileLoop(statements_Conditional, statements_StatementContainer, statements_Statement):

    pass
class kernel_statements_Condition(statements_Conditional, statements_StatementContainer, statements_Statement):

    pass
class kernel_statements_StatementContainer(ABC):

    pass
class Statement:

    pass
class kernel_statements_Jump(Statement):

    pass
class kernel_statements_Abort(Statement):

    pass
class kernel_statements_Skip(Statement):

    pass
class kernel_statements_Return(Statement):

    pass
class kernel_statements_ExpressionStatement(Statement):

    pass
class kernel_statements_StatementListContainer(ABC):

    pass
class members_Member:

    pass
class kernel_dataitems_DataItem(members_Member, commons_Variable, references_ReferenceableElement):

    pass
class commons_LabellableElement:

    pass
class kernel_procedures_Procedure(commons_LabellableElement, procedures_Procedure, members_Member, references_ReferenceableElement):

    pass
class kernel_statements_ExceptionHandlerStatement(commons_LabellableElement, statements_StatementContainer):

    pass
class kernel_statements_Statement(commons_LabellableElement, members_Member):

    pass
class kernel_commons_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

