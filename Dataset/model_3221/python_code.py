from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class AssignmentOperator(Enum):
    ASSIGN = "ASSIGN"
    MINUSASSIGN = "MINUSASSIGN"
    PLUSASSIGN = "PLUSASSIGN"
    MULTASSIGN = "MULTASSIGN"
    MODASSIGN = "MODASSIGN"
    DIVASSIGN = "DIVASSIGN"
    ORASSIGN = "ORASSIGN"
    ANDASSIGN = "ANDASSIGN"
class UnaryOperator(Enum):
    UNOT = "UNOT"
    UMINUS = "UMINUS"
    UPLUS = "UPLUS"
class BinaryOperator(Enum):
    BGE = "BGE"
    BPLUS = "BPLUS"
    BMINUS = "BMINUS"
    BMUL = "BMUL"
    BDIV = "BDIV"
    BMOD = "BMOD"
    BNOR = "BNOR"
    BNAND = "BNAND"
    BXOR = "BXOR"
    BOR = "BOR"
    BAND = "BAND"
    BEQ = "BEQ"
    BNE = "BNE"
    BLT = "BLT"
    BGT = "BGT"
    BLE = "BLE"


############################################
# Definition of Classes
############################################

class declarations_RepositoryDecl:

    pass
class RepositoryDecl:

    pass
class ClockRDL_declarations_SystemDecl(RepositoryDecl):

    pass
class declarations_RelationInstanceDecl:

    pass
class declarations_ClockDecl:

    pass
class declarations_TransitionDecl:

    pass
class AbstractRelationDecl:

    pass
class ClockRDL_declarations_CompositeRelationDecl(AbstractRelationDecl):

    pass
class ClockRDL_declarations_PrimitiveRelationDecl(AbstractRelationDecl):

    pass
class ClockRDL_declarations_FormalToActualMapEntry:

    def __init__(self, key: str, ClockRDL_declarations_FormalToActualMapEntry: "kernel_Expression" = None, ClockRDL_declarations_FormalToActualMapEntry81: "kernel_Declaration" = None):
        self.key = key
        self.ClockRDL_declarations_FormalToActualMapEntry = ClockRDL_declarations_FormalToActualMapEntry
        self.ClockRDL_declarations_FormalToActualMapEntry81 = ClockRDL_declarations_FormalToActualMapEntry81
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def ClockRDL_declarations_FormalToActualMapEntry81(self):
        return self.__ClockRDL_declarations_FormalToActualMapEntry81

    @ClockRDL_declarations_FormalToActualMapEntry81.setter
    def ClockRDL_declarations_FormalToActualMapEntry81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClockRDL_declarations_FormalToActualMapEntry__ClockRDL_declarations_FormalToActualMapEntry81", None)
        self.__ClockRDL_declarations_FormalToActualMapEntry81 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "kernel_Declaration"):
                opp_val = getattr(old_value, "kernel_Declaration", None)
                if opp_val == self:
                    setattr(old_value, "kernel_Declaration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "kernel_Declaration"):
                opp_val = getattr(value, "kernel_Declaration", None)
                setattr(value, "kernel_Declaration", self)

    @property
    def ClockRDL_declarations_FormalToActualMapEntry(self):
        return self.__ClockRDL_declarations_FormalToActualMapEntry

    @ClockRDL_declarations_FormalToActualMapEntry.setter
    def ClockRDL_declarations_FormalToActualMapEntry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClockRDL_declarations_FormalToActualMapEntry__ClockRDL_declarations_FormalToActualMapEntry", None)
        self.__ClockRDL_declarations_FormalToActualMapEntry = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "kernel_Expression79"):
                opp_val = getattr(old_value, "kernel_Expression79", None)
                if opp_val == self:
                    setattr(old_value, "kernel_Expression79", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "kernel_Expression79"):
                opp_val = getattr(value, "kernel_Expression79", None)
                setattr(value, "kernel_Expression79", self)

class declarations_FormalToActualMapEntry:

    pass
class declarations_AbstractRelationDecl:

    pass
class Declaration:

    pass
class ClockRDL_declarations_LibraryItemDecl(Declaration):

    pass
class ClockRDL_declarations_TransitionDecl(Declaration):

    pass
class AbstractFunctionDecl:

    pass
class ClockRDL_declarations_FunctionDecl(AbstractFunctionDecl):

    pass
class ClockRDL_declarations_PrimitiveFunctionDecl(AbstractFunctionDecl):

    pass
class declarations_ArgumentDecl:

    pass
class VariableDecl:

    pass
class declarations_LibraryItemDecl:

    pass
class ClockRDL_declarations_LibraryDecl(declarations_LibraryItemDecl, declarations_RepositoryDecl):

    pass
class expressions_ClockReference:

    pass
class ClockRDL_declarations_ConstantDecl(VariableDecl):

    pass
class literals_ClockLiteral:

    pass
class NamedDeclaration:

    pass
class ClockRDL_declarations_RepositoryDecl(NamedDeclaration):

    pass
class ClockRDL_declarations_AbstractFunctionDecl(NamedDeclaration):

    pass
class ClockRDL_declarations_VariableDecl(NamedDeclaration):

    pass
class ClockRDL_declarations_ArgumentDecl(NamedDeclaration):

    pass
class ClockRDL_declarations_RelationInstanceDecl(NamedDeclaration):

    def __init__(self, qualifiedName: str, ClockRDL_declarations_RelationInstanceDecl: "declarations_AbstractRelationDecl" = None, ClockRDL_declarations_RelationInstanceDecl77: set["declarations_FormalToActualMapEntry"] = None):
        self.qualifiedName = qualifiedName
        self.ClockRDL_declarations_RelationInstanceDecl = ClockRDL_declarations_RelationInstanceDecl
        self.ClockRDL_declarations_RelationInstanceDecl77 = ClockRDL_declarations_RelationInstanceDecl77 if ClockRDL_declarations_RelationInstanceDecl77 is not None else set()
        
    @property
    def qualifiedName(self) -> str:
        return self.__qualifiedName

    @qualifiedName.setter
    def qualifiedName(self, qualifiedName: str):
        self.__qualifiedName = qualifiedName

    @property
    def ClockRDL_declarations_RelationInstanceDecl(self):
        return self.__ClockRDL_declarations_RelationInstanceDecl

    @ClockRDL_declarations_RelationInstanceDecl.setter
    def ClockRDL_declarations_RelationInstanceDecl(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClockRDL_declarations_RelationInstanceDecl__ClockRDL_declarations_RelationInstanceDecl", None)
        self.__ClockRDL_declarations_RelationInstanceDecl = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "declarations_AbstractRelationDecl"):
                opp_val = getattr(old_value, "declarations_AbstractRelationDecl", None)
                if opp_val == self:
                    setattr(old_value, "declarations_AbstractRelationDecl", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "declarations_AbstractRelationDecl"):
                opp_val = getattr(value, "declarations_AbstractRelationDecl", None)
                setattr(value, "declarations_AbstractRelationDecl", self)

    @property
    def ClockRDL_declarations_RelationInstanceDecl77(self):
        return self.__ClockRDL_declarations_RelationInstanceDecl77

    @ClockRDL_declarations_RelationInstanceDecl77.setter
    def ClockRDL_declarations_RelationInstanceDecl77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClockRDL_declarations_RelationInstanceDecl__ClockRDL_declarations_RelationInstanceDecl77", None)
        self.__ClockRDL_declarations_RelationInstanceDecl77 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "declarations_FormalToActualMapEntry"):
                    opp_val = getattr(item, "declarations_FormalToActualMapEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "declarations_FormalToActualMapEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "declarations_FormalToActualMapEntry"):
                    opp_val = getattr(item, "declarations_FormalToActualMapEntry", None)
                    
                    setattr(item, "declarations_FormalToActualMapEntry", self)
                    

class ClockRDL_declarations_ClockDecl(NamedDeclaration):

    pass
class Statement:

    pass
class ClockRDL_statements_BlockStmt(Statement):

    pass
class ClockRDL_statements_ReturnStmt(Statement):

    pass
class ClockRDL_statements_AssignmentStmt(Statement):

    def __init__(self, operator: str, ClockRDL_statements_AssignmentStmt: "kernel_Expression" = None, ClockRDL_statements_AssignmentStmt33: "kernel_Expression" = None):
        self.operator = operator
        self.ClockRDL_statements_AssignmentStmt = ClockRDL_statements_AssignmentStmt
        self.ClockRDL_statements_AssignmentStmt33 = ClockRDL_statements_AssignmentStmt33
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def ClockRDL_statements_AssignmentStmt(self):
        return self.__ClockRDL_statements_AssignmentStmt

    @ClockRDL_statements_AssignmentStmt.setter
    def ClockRDL_statements_AssignmentStmt(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClockRDL_statements_AssignmentStmt__ClockRDL_statements_AssignmentStmt", None)
        self.__ClockRDL_statements_AssignmentStmt = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "kernel_Expression31"):
                opp_val = getattr(old_value, "kernel_Expression31", None)
                if opp_val == self:
                    setattr(old_value, "kernel_Expression31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "kernel_Expression31"):
                opp_val = getattr(value, "kernel_Expression31", None)
                setattr(value, "kernel_Expression31", self)

    @property
    def ClockRDL_statements_AssignmentStmt33(self):
        return self.__ClockRDL_statements_AssignmentStmt33

    @ClockRDL_statements_AssignmentStmt33.setter
    def ClockRDL_statements_AssignmentStmt33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClockRDL_statements_AssignmentStmt__ClockRDL_statements_AssignmentStmt33", None)
        self.__ClockRDL_statements_AssignmentStmt33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "kernel_Expression34"):
                opp_val = getattr(old_value, "kernel_Expression34", None)
                if opp_val == self:
                    setattr(old_value, "kernel_Expression34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "kernel_Expression34"):
                opp_val = getattr(value, "kernel_Expression34", None)
                setattr(value, "kernel_Expression34", self)

class ClockRDL_statements_LoopStmt(Statement):

    pass
class statements_BlockStmt:

    pass
class ClockRDL_statements_ConditionalStmt(Statement):

    pass
class literals_FieldLiteral:

    pass
class expressions_Literal:

    pass
class Literal:

    pass
class ClockRDL_literals_BooleanLiteral(Literal):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class ClockRDL_literals_ClockLiteral(Literal):

    def __init__(self, name: str, isInternal: str):
        self.name = name
        self.isInternal = isInternal
        
    @property
    def isInternal(self) -> str:
        return self.__isInternal

    @isInternal.setter
    def isInternal(self, isInternal: str):
        self.__isInternal = isInternal

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class ClockRDL_literals_RecordLiteral(Literal):

    pass
class ClockRDL_literals_QueueLiteral(Literal):

    pass
class ClockRDL_literals_ArrayLiteral(Literal):

    pass
class ClockRDL_literals_IntegerLiteral(Literal):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class ReferenceExp:

    pass
class ClockRDL_expressions_ClockReference(ReferenceExp):

    pass
class kernel_NamedDeclaration:

    pass
class ClockRDL_declarations_AbstractRelationDecl(kernel_NamedDeclaration, declarations_LibraryItemDecl):

    pass
class PrefixedExp:

    pass
class ClockRDL_expressions_IndexedExp(PrefixedExp):

    pass
class kernel_Expression:

    pass
class Expression:

    pass
class ClockRDL_expressions_BinaryExp(Expression):

    def __init__(self, operator: str, ClockRDL_expressions_BinaryExp: "kernel_Expression" = None, ClockRDL_expressions_BinaryExp13: "kernel_Expression" = None):
        self.operator = operator
        self.ClockRDL_expressions_BinaryExp = ClockRDL_expressions_BinaryExp
        self.ClockRDL_expressions_BinaryExp13 = ClockRDL_expressions_BinaryExp13
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def ClockRDL_expressions_BinaryExp(self):
        return self.__ClockRDL_expressions_BinaryExp

    @ClockRDL_expressions_BinaryExp.setter
    def ClockRDL_expressions_BinaryExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClockRDL_expressions_BinaryExp__ClockRDL_expressions_BinaryExp", None)
        self.__ClockRDL_expressions_BinaryExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "kernel_Expression11"):
                opp_val = getattr(old_value, "kernel_Expression11", None)
                if opp_val == self:
                    setattr(old_value, "kernel_Expression11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "kernel_Expression11"):
                opp_val = getattr(value, "kernel_Expression11", None)
                setattr(value, "kernel_Expression11", self)

    @property
    def ClockRDL_expressions_BinaryExp13(self):
        return self.__ClockRDL_expressions_BinaryExp13

    @ClockRDL_expressions_BinaryExp13.setter
    def ClockRDL_expressions_BinaryExp13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClockRDL_expressions_BinaryExp__ClockRDL_expressions_BinaryExp13", None)
        self.__ClockRDL_expressions_BinaryExp13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "kernel_Expression14"):
                opp_val = getattr(old_value, "kernel_Expression14", None)
                if opp_val == self:
                    setattr(old_value, "kernel_Expression14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "kernel_Expression14"):
                opp_val = getattr(value, "kernel_Expression14", None)
                setattr(value, "kernel_Expression14", self)

class ClockRDL_expressions_ParenExp(Expression):

    pass
class ClockRDL_expressions_ConditionalExp(Expression):

    pass
class ClockRDL_expressions_PrefixedExp(Expression):

    pass
class ClockRDL_expressions_UnaryExp(Expression):

    def __init__(self, operator: str, ClockRDL_expressions_UnaryExp: "kernel_Expression" = None):
        self.operator = operator
        self.ClockRDL_expressions_UnaryExp = ClockRDL_expressions_UnaryExp
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def ClockRDL_expressions_UnaryExp(self):
        return self.__ClockRDL_expressions_UnaryExp

    @ClockRDL_expressions_UnaryExp.setter
    def ClockRDL_expressions_UnaryExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClockRDL_expressions_UnaryExp__ClockRDL_expressions_UnaryExp", None)
        self.__ClockRDL_expressions_UnaryExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "kernel_Expression9"):
                opp_val = getattr(old_value, "kernel_Expression9", None)
                if opp_val == self:
                    setattr(old_value, "kernel_Expression9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "kernel_Expression9"):
                opp_val = getattr(value, "kernel_Expression9", None)
                setattr(value, "kernel_Expression9", self)

class ClockRDL_expressions_Literal(Expression):

    pass
class ClockRDL_expressions_ReferenceExp(Expression):

    pass
class expressions_PrefixedExp:

    pass
class ClockRDL_expressions_SelectedExp(PrefixedExp):

    def __init__(self, selector: str):
        self.selector = selector
        
    @property
    def selector(self) -> str:
        return self.__selector

    @selector.setter
    def selector(self, selector: str):
        self.__selector = selector

class Element:

    pass
class ClockRDL_kernel_NamedElement(Element):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class ClockRDL_kernel_Element(ABC):

    pass
class kernel_Statement:

    pass
class ClockRDL_expressions_FunctionCallExp(kernel_Statement, expressions_PrefixedExp):

    pass
class kernel_Element:

    pass
class ClockRDL_kernel_Expression(kernel_Element, kernel_Statement):

    pass
class ClockRDL_kernel_Statement(Element):

    pass
class kernel_NamedElement:

    pass
class ClockRDL_literals_FieldLiteral(kernel_NamedElement, expressions_Literal):

    pass
class kernel_Declaration:

    pass
class ClockRDL_kernel_NamedDeclaration(kernel_NamedElement, kernel_Declaration):

    pass
class ClockRDL_kernel_Declaration(Element):

    pass