import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    plsql_declaration_NamedElement,
    TriggerBlock,
    SelectStatement,
    plsql_declaration_PLSQLDefinition,
    statement_BlockStatement,
    plsql_condition_SQLCondition,
    plsql_type_TypedElement,
    Argument,
    type_TypedElement,
    declaration_Declaration,
    plsql_declaration_FunctionDeclaration,
    plsql_declaration_VariableDeclaration,
    NamedElement,
    plsql_declaration_Declaration,
    plsql_declaration_Package,
    plsql_expression_FunctionCallParameter,
    Type,
    plsql_type_GenericType,
    plsql_type_IndirectType,
    plsql_type_Datatype,
    plsql_type_Type,
    StringOperation,
    plsql_expression_ConcatString,
    plsql_statement_ExceptionSection,
    plsql_statement_UpdatePair,
    UpdatePair,
    condition_SQLCondition,
    plsql_expression_Expression,
    SQLCondition,
    plsql_condition_BooleanCondition,
    plsql_condition_ConditionComparison,
    plsql_condition_NotCondition,
    ModifySQLStatement,
    plsql_statement_UpdateStatement,
    plsql_statement_DeleteStatement,
    plsql_statement_SetTransactionStatement,
    plsql_statement_InsertStatement,
    plsql_statement_SelectStatement,
    ExceptionSection,
    Declaration,
    plsql_declaration_CursorDeclaration,
    plsql_declaration_ProcedureDeclaration,
    VariableDeclaration,
    LoopStatement,
    plsql_statement_ForStatement,
    VarRefExpression,
    plsql_expression_SQLCursor,
    plsql_expression_SQLVariable,
    plsql_expression_FormsVarRef,
    CursorDeclaration,
    ControlSQLStatement,
    plsql_statement_LockTableStatement,
    plsql_statement_CommitStatement,
    plsql_statement_FetchStatement,
    plsql_statement_SavepointStatement,
    plsql_statement_RollbackStatement,
    plsql_statement_OpenStatement,
    plsql_statement_CloseStatement,
    SQLStatement,
    plsql_statement_ModifySQLStatement,
    plsql_statement_ControlSQLStatement,
    FunctionCallParameter,
    expression_Expression,
    plsql_expression_BooleanExpression,
    Statement,
    plsql_statement_NullStatement,
    plsql_statement_ReturnStatement,
    plsql_statement_RaiseStatement,
    plsql_statement_SQLStatement,
    plsql_statement_BlockStatement,
    plsql_statement_AssignmentStatement,
    plsql_statement_Statement,
    plsql_statement_LoopStatement,
    IfStatement,
    plsql_statement_IfStatement,
    plsql_statement_CaseStatement,
    declaration_NamedElement,
    plsql_declaration_Argument,
    plsql_declaration_TriggerBlock,
    statement_Statement,
    plsql_statement_FunctionCallStatement,
    plsql_statement_GotoStatement,
    plsql_statement_ExitStatement,
    Expression,
    plsql_expression_PropertyAccess,
    plsql_expression_VarRefExpression,
    plsql_expression_InRangeExpression,
    plsql_expression_ArithmeticExpression,
    plsql_expression_LiteralExpression,
    plsql_expression_LikeExpression,
    plsql_expression_NotExpression,
    plsql_expression_StringOperation,
    plsql_expression_IsNullExpression,
    plsql_expression_FoundExpression,
    BasicTypes,
    LiteralExpressionType,
    ArithmeticOperatorType,
    BooleanOperatorType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_plsql_declaration_namedelement_is_not_abstract():
    assert not inspect.isabstract(plsql_declaration_NamedElement)


def test_plsql_declaration_namedelement_constructor_exists():
    assert callable(plsql_declaration_NamedElement.__init__)


def test_plsql_declaration_namedelement_constructor_args():
    sig = inspect.signature(plsql_declaration_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_plsql_declaration_namedelement_has_name():
    assert hasattr(plsql_declaration_NamedElement, "name")
    descriptor = None
    for klass in plsql_declaration_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_triggerblock_is_not_abstract():
    assert not inspect.isabstract(TriggerBlock)


def test_triggerblock_constructor_exists():
    assert callable(TriggerBlock.__init__)


def test_triggerblock_constructor_args():
    sig = inspect.signature(TriggerBlock.__init__)
    params = list(sig.parameters.keys())



def test_selectstatement_is_not_abstract():
    assert not inspect.isabstract(SelectStatement)


def test_selectstatement_constructor_exists():
    assert callable(SelectStatement.__init__)


def test_selectstatement_constructor_args():
    sig = inspect.signature(SelectStatement.__init__)
    params = list(sig.parameters.keys())



def test_plsql_declaration_plsqldefinition_is_not_abstract():
    assert not inspect.isabstract(plsql_declaration_PLSQLDefinition)


def test_plsql_declaration_plsqldefinition_constructor_exists():
    assert callable(plsql_declaration_PLSQLDefinition.__init__)


def test_plsql_declaration_plsqldefinition_constructor_args():
    sig = inspect.signature(plsql_declaration_PLSQLDefinition.__init__)
    params = list(sig.parameters.keys())



def test_statement_blockstatement_is_not_abstract():
    assert not inspect.isabstract(statement_BlockStatement)


def test_statement_blockstatement_constructor_exists():
    assert callable(statement_BlockStatement.__init__)


def test_statement_blockstatement_constructor_args():
    sig = inspect.signature(statement_BlockStatement.__init__)
    params = list(sig.parameters.keys())



def test_plsql_condition_sqlcondition_is_not_abstract():
    assert not inspect.isabstract(plsql_condition_SQLCondition)


def test_plsql_condition_sqlcondition_constructor_exists():
    assert callable(plsql_condition_SQLCondition.__init__)


def test_plsql_condition_sqlcondition_constructor_args():
    sig = inspect.signature(plsql_condition_SQLCondition.__init__)
    params = list(sig.parameters.keys())



def test_plsql_type_typedelement_is_not_abstract():
    assert not inspect.isabstract(plsql_type_TypedElement)


def test_plsql_type_typedelement_constructor_exists():
    assert callable(plsql_type_TypedElement.__init__)


def test_plsql_type_typedelement_constructor_args():
    sig = inspect.signature(plsql_type_TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_argument_is_not_abstract():
    assert not inspect.isabstract(Argument)


def test_argument_constructor_exists():
    assert callable(Argument.__init__)


def test_argument_constructor_args():
    sig = inspect.signature(Argument.__init__)
    params = list(sig.parameters.keys())



def test_type_typedelement_is_not_abstract():
    assert not inspect.isabstract(type_TypedElement)


def test_type_typedelement_constructor_exists():
    assert callable(type_TypedElement.__init__)


def test_type_typedelement_constructor_args():
    sig = inspect.signature(type_TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_declaration_declaration_is_not_abstract():
    assert not inspect.isabstract(declaration_Declaration)


def test_declaration_declaration_constructor_exists():
    assert callable(declaration_Declaration.__init__)


def test_declaration_declaration_constructor_args():
    sig = inspect.signature(declaration_Declaration.__init__)
    params = list(sig.parameters.keys())



def test_plsql_declaration_functiondeclaration_is_not_abstract():
    assert not inspect.isabstract(plsql_declaration_FunctionDeclaration)


def test_plsql_declaration_functiondeclaration_constructor_exists():
    assert callable(plsql_declaration_FunctionDeclaration.__init__)


def test_plsql_declaration_functiondeclaration_constructor_args():
    sig = inspect.signature(plsql_declaration_FunctionDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_plsql_declaration_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(plsql_declaration_VariableDeclaration)


def test_plsql_declaration_variabledeclaration_constructor_exists():
    assert callable(plsql_declaration_VariableDeclaration.__init__)


def test_plsql_declaration_variabledeclaration_constructor_args():
    sig = inspect.signature(plsql_declaration_VariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "constant" in params, "Missing parameter 'constant'"
    assert "default" in params, "Missing parameter 'default'"
    assert "notnull" in params, "Missing parameter 'notnull'"

def test_plsql_declaration_variabledeclaration_has_constant():
    assert hasattr(plsql_declaration_VariableDeclaration, "constant")
    descriptor = None
    for klass in plsql_declaration_VariableDeclaration.__mro__:
        if "constant" in klass.__dict__:
            descriptor = klass.__dict__["constant"]
            break
    assert isinstance(descriptor, property)

def test_plsql_declaration_variabledeclaration_has_default():
    assert hasattr(plsql_declaration_VariableDeclaration, "default")
    descriptor = None
    for klass in plsql_declaration_VariableDeclaration.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)

def test_plsql_declaration_variabledeclaration_has_notnull():
    assert hasattr(plsql_declaration_VariableDeclaration, "notnull")
    descriptor = None
    for klass in plsql_declaration_VariableDeclaration.__mro__:
        if "notnull" in klass.__dict__:
            descriptor = klass.__dict__["notnull"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_plsql_declaration_declaration_is_not_abstract():
    assert not inspect.isabstract(plsql_declaration_Declaration)


def test_plsql_declaration_declaration_constructor_exists():
    assert callable(plsql_declaration_Declaration.__init__)


def test_plsql_declaration_declaration_constructor_args():
    sig = inspect.signature(plsql_declaration_Declaration.__init__)
    params = list(sig.parameters.keys())



def test_plsql_declaration_package_is_not_abstract():
    assert not inspect.isabstract(plsql_declaration_Package)


def test_plsql_declaration_package_constructor_exists():
    assert callable(plsql_declaration_Package.__init__)


def test_plsql_declaration_package_constructor_args():
    sig = inspect.signature(plsql_declaration_Package.__init__)
    params = list(sig.parameters.keys())



def test_plsql_expression_functioncallparameter_is_not_abstract():
    assert not inspect.isabstract(plsql_expression_FunctionCallParameter)


def test_plsql_expression_functioncallparameter_constructor_exists():
    assert callable(plsql_expression_FunctionCallParameter.__init__)


def test_plsql_expression_functioncallparameter_constructor_args():
    sig = inspect.signature(plsql_expression_FunctionCallParameter.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_plsql_type_generictype_is_not_abstract():
    assert not inspect.isabstract(plsql_type_GenericType)


def test_plsql_type_generictype_constructor_exists():
    assert callable(plsql_type_GenericType.__init__)


def test_plsql_type_generictype_constructor_args():
    sig = inspect.signature(plsql_type_GenericType.__init__)
    params = list(sig.parameters.keys())



def test_plsql_type_indirecttype_is_not_abstract():
    assert not inspect.isabstract(plsql_type_IndirectType)


def test_plsql_type_indirecttype_constructor_exists():
    assert callable(plsql_type_IndirectType.__init__)


def test_plsql_type_indirecttype_constructor_args():
    sig = inspect.signature(plsql_type_IndirectType.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"
    assert "range" in params, "Missing parameter 'range'"
    assert "type" in params, "Missing parameter 'type'"
    assert "rowtype" in params, "Missing parameter 'rowtype'"

def test_plsql_type_indirecttype_has_identifier():
    assert hasattr(plsql_type_IndirectType, "identifier")
    descriptor = None
    for klass in plsql_type_IndirectType.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)

def test_plsql_type_indirecttype_has_range():
    assert hasattr(plsql_type_IndirectType, "range")
    descriptor = None
    for klass in plsql_type_IndirectType.__mro__:
        if "range" in klass.__dict__:
            descriptor = klass.__dict__["range"]
            break
    assert isinstance(descriptor, property)

def test_plsql_type_indirecttype_has_type():
    assert hasattr(plsql_type_IndirectType, "type")
    descriptor = None
    for klass in plsql_type_IndirectType.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_plsql_type_indirecttype_has_rowtype():
    assert hasattr(plsql_type_IndirectType, "rowtype")
    descriptor = None
    for klass in plsql_type_IndirectType.__mro__:
        if "rowtype" in klass.__dict__:
            descriptor = klass.__dict__["rowtype"]
            break
    assert isinstance(descriptor, property)



def test_plsql_type_datatype_is_not_abstract():
    assert not inspect.isabstract(plsql_type_Datatype)


def test_plsql_type_datatype_constructor_exists():
    assert callable(plsql_type_Datatype.__init__)


def test_plsql_type_datatype_constructor_args():
    sig = inspect.signature(plsql_type_Datatype.__init__)
    params = list(sig.parameters.keys())
    assert "range" in params, "Missing parameter 'range'"
    assert "name" in params, "Missing parameter 'name'"

def test_plsql_type_datatype_has_range():
    assert hasattr(plsql_type_Datatype, "range")
    descriptor = None
    for klass in plsql_type_Datatype.__mro__:
        if "range" in klass.__dict__:
            descriptor = klass.__dict__["range"]
            break
    assert isinstance(descriptor, property)

def test_plsql_type_datatype_has_name():
    assert hasattr(plsql_type_Datatype, "name")
    descriptor = None
    for klass in plsql_type_Datatype.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_plsql_type_type_is_not_abstract():
    assert not inspect.isabstract(plsql_type_Type)


def test_plsql_type_type_constructor_exists():
    assert callable(plsql_type_Type.__init__)


def test_plsql_type_type_constructor_args():
    sig = inspect.signature(plsql_type_Type.__init__)
    params = list(sig.parameters.keys())



def test_stringoperation_is_not_abstract():
    assert not inspect.isabstract(StringOperation)


def test_stringoperation_constructor_exists():
    assert callable(StringOperation.__init__)


def test_stringoperation_constructor_args():
    sig = inspect.signature(StringOperation.__init__)
    params = list(sig.parameters.keys())



def test_plsql_expression_concatstring_is_not_abstract():
    assert not inspect.isabstract(plsql_expression_ConcatString)


def test_plsql_expression_concatstring_constructor_exists():
    assert callable(plsql_expression_ConcatString.__init__)


def test_plsql_expression_concatstring_constructor_args():
    sig = inspect.signature(plsql_expression_ConcatString.__init__)
    params = list(sig.parameters.keys())



def test_plsql_statement_exceptionsection_is_not_abstract():
    assert not inspect.isabstract(plsql_statement_ExceptionSection)


def test_plsql_statement_exceptionsection_constructor_exists():
    assert callable(plsql_statement_ExceptionSection.__init__)


def test_plsql_statement_exceptionsection_constructor_args():
    sig = inspect.signature(plsql_statement_ExceptionSection.__init__)
    params = list(sig.parameters.keys())
    assert "exceptionNames" in params, "Missing parameter 'exceptionNames'"

def test_plsql_statement_exceptionsection_has_exceptionNames():
    assert hasattr(plsql_statement_ExceptionSection, "exceptionNames")
    descriptor = None
    for klass in plsql_statement_ExceptionSection.__mro__:
        if "exceptionNames" in klass.__dict__:
            descriptor = klass.__dict__["exceptionNames"]
            break
    assert isinstance(descriptor, property)



def test_plsql_statement_updatepair_is_not_abstract():
    assert not inspect.isabstract(plsql_statement_UpdatePair)


def test_plsql_statement_updatepair_constructor_exists():
    assert callable(plsql_statement_UpdatePair.__init__)


def test_plsql_statement_updatepair_constructor_args():
    sig = inspect.signature(plsql_statement_UpdatePair.__init__)
    params = list(sig.parameters.keys())
    assert "column" in params, "Missing parameter 'column'"

def test_plsql_statement_updatepair_has_column():
    assert hasattr(plsql_statement_UpdatePair, "column")
    descriptor = None
    for klass in plsql_statement_UpdatePair.__mro__:
        if "column" in klass.__dict__:
            descriptor = klass.__dict__["column"]
            break
    assert isinstance(descriptor, property)



def test_updatepair_is_not_abstract():
    assert not inspect.isabstract(UpdatePair)


def test_updatepair_constructor_exists():
    assert callable(UpdatePair.__init__)


def test_updatepair_constructor_args():
    sig = inspect.signature(UpdatePair.__init__)
    params = list(sig.parameters.keys())



def test_condition_sqlcondition_is_not_abstract():
    assert not inspect.isabstract(condition_SQLCondition)


def test_condition_sqlcondition_constructor_exists():
    assert callable(condition_SQLCondition.__init__)


def test_condition_sqlcondition_constructor_args():
    sig = inspect.signature(condition_SQLCondition.__init__)
    params = list(sig.parameters.keys())



def test_plsql_expression_expression_is_not_abstract():
    assert not inspect.isabstract(plsql_expression_Expression)


def test_plsql_expression_expression_constructor_exists():
    assert callable(plsql_expression_Expression.__init__)


def test_plsql_expression_expression_constructor_args():
    sig = inspect.signature(plsql_expression_Expression.__init__)
    params = list(sig.parameters.keys())



def test_sqlcondition_is_not_abstract():
    assert not inspect.isabstract(SQLCondition)


def test_sqlcondition_constructor_exists():
    assert callable(SQLCondition.__init__)


def test_sqlcondition_constructor_args():
    sig = inspect.signature(SQLCondition.__init__)
    params = list(sig.parameters.keys())



def test_plsql_condition_booleancondition_is_not_abstract():
    assert not inspect.isabstract(plsql_condition_BooleanCondition)


def test_plsql_condition_booleancondition_constructor_exists():
    assert callable(plsql_condition_BooleanCondition.__init__)


def test_plsql_condition_booleancondition_constructor_args():
    sig = inspect.signature(plsql_condition_BooleanCondition.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_plsql_condition_booleancondition_has_type():
    assert hasattr(plsql_condition_BooleanCondition, "type")
    descriptor = None
    for klass in plsql_condition_BooleanCondition.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_plsql_condition_conditioncomparison_is_not_abstract():
    assert not inspect.isabstract(plsql_condition_ConditionComparison)


def test_plsql_condition_conditioncomparison_constructor_exists():
    assert callable(plsql_condition_ConditionComparison.__init__)


def test_plsql_condition_conditioncomparison_constructor_args():
    sig = inspect.signature(plsql_condition_ConditionComparison.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_plsql_condition_conditioncomparison_has_type():
    assert hasattr(plsql_condition_ConditionComparison, "type")
    descriptor = None
    for klass in plsql_condition_ConditionComparison.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_plsql_condition_notcondition_is_not_abstract():
    assert not inspect.isabstract(plsql_condition_NotCondition)


def test_plsql_condition_notcondition_constructor_exists():
    assert callable(plsql_condition_NotCondition.__init__)


def test_plsql_condition_notcondition_constructor_args():
    sig = inspect.signature(plsql_condition_NotCondition.__init__)
    params = list(sig.parameters.keys())



def test_modifysqlstatement_is_not_abstract():
    assert not inspect.isabstract(ModifySQLStatement)


def test_modifysqlstatement_constructor_exists():
    assert callable(ModifySQLStatement.__init__)


def test_modifysqlstatement_constructor_args():
    sig = inspect.signature(ModifySQLStatement.__init__)
    params = list(sig.parameters.keys())



def test_plsql_statement_updatestatement_is_not_abstract():
    assert not inspect.isabstract(plsql_statement_UpdateStatement)


def test_plsql_statement_updatestatement_constructor_exists():
    assert callable(plsql_statement_UpdateStatement.__init__)


def test_plsql_statement_updatestatement_constructor_args():
    sig = inspect.signature(plsql_statement_UpdateStatement.__init__)
    params = list(sig.parameters.keys())
    assert "table" in params, "Missing parameter 'table'"

def test_plsql_statement_updatestatement_has_table():
    assert hasattr(plsql_statement_UpdateStatement, "table")
    descriptor = None
    for klass in plsql_statement_UpdateStatement.__mro__:
        if "table" in klass.__dict__:
            descriptor = klass.__dict__["table"]
            break
    assert isinstance(descriptor, property)



def test_plsql_statement_deletestatement_is_not_abstract():
    assert not inspect.isabstract(plsql_statement_DeleteStatement)


def test_plsql_statement_deletestatement_constructor_exists():
    assert callable(plsql_statement_DeleteStatement.__init__)


def test_plsql_statement_deletestatement_constructor_args():
    sig = inspect.signature(plsql_statement_DeleteStatement.__init__)
    params = list(sig.parameters.keys())



def test_plsql_statement_settransactionstatement_is_not_abstract():
    assert not inspect.isabstract(plsql_statement_SetTransactionStatement)


def test_plsql_statement_settransactionstatement_constructor_exists():
    assert callable(plsql_statement_SetTransactionStatement.__init__)


def test_plsql_statement_settransactionstatement_constructor_args():
    sig = inspect.signature(plsql_statement_SetTransactionStatement.__init__)
    params = list(sig.parameters.keys())



def test_plsql_statement_insertstatement_is_not_abstract():
    assert not inspect.isabstract(plsql_statement_InsertStatement)


def test_plsql_statement_insertstatement_constructor_exists():
    assert callable(plsql_statement_InsertStatement.__init__)


def test_plsql_statement_insertstatement_constructor_args():
    sig = inspect.signature(plsql_statement_InsertStatement.__init__)
    params = list(sig.parameters.keys())
    assert "columns" in params, "Missing parameter 'columns'"
    assert "into" in params, "Missing parameter 'into'"

def test_plsql_statement_insertstatement_has_columns():
    assert hasattr(plsql_statement_InsertStatement, "columns")
    descriptor = None
    for klass in plsql_statement_InsertStatement.__mro__:
        if "columns" in klass.__dict__:
            descriptor = klass.__dict__["columns"]
            break
    assert isinstance(descriptor, property)

def test_plsql_statement_insertstatement_has_into():
    assert hasattr(plsql_statement_InsertStatement, "into")
    descriptor = None
    for klass in plsql_statement_InsertStatement.__mro__:
        if "into" in klass.__dict__:
            descriptor = klass.__dict__["into"]
            break
    assert isinstance(descriptor, property)



def test_plsql_statement_selectstatement_is_not_abstract():
    assert not inspect.isabstract(plsql_statement_SelectStatement)


def test_plsql_statement_selectstatement_constructor_exists():
    assert callable(plsql_statement_SelectStatement.__init__)


def test_plsql_statement_selectstatement_constructor_args():
    sig = inspect.signature(plsql_statement_SelectStatement.__init__)
    params = list(sig.parameters.keys())
    assert "collect" in params, "Missing parameter 'collect'"
    assert "unique" in params, "Missing parameter 'unique'"
    assert "all" in params, "Missing parameter 'all'"
    assert "from_" in params, "Missing parameter 'from_'"
    assert "selectList" in params, "Missing parameter 'selectList'"
    assert "distinct" in params, "Missing parameter 'distinct'"
    assert "isCount" in params, "Missing parameter 'isCount'"
    assert "bulk" in params, "Missing parameter 'bulk'"

def test_plsql_statement_selectstatement_has_collect():
    assert hasattr(plsql_statement_SelectStatement, "collect")
    descriptor = None
    for klass in plsql_statement_SelectStatement.__mro__:
        if "collect" in klass.__dict__:
            descriptor = klass.__dict__["collect"]
            break
    assert isinstance(descriptor, property)

def test_plsql_statement_selectstatement_has_unique():
    assert hasattr(plsql_statement_SelectStatement, "unique")
    descriptor = None
    for klass in plsql_statement_SelectStatement.__mro__:
        if "unique" in klass.__dict__:
            descriptor = klass.__dict__["unique"]
            break
    assert isinstance(descriptor, property)

def test_plsql_statement_selectstatement_has_all():
    assert hasattr(plsql_statement_SelectStatement, "all")
    descriptor = None
    for klass in plsql_statement_SelectStatement.__mro__:
        if "all" in klass.__dict__:
            descriptor = klass.__dict__["all"]
            break
    assert isinstance(descriptor, property)

def test_plsql_statement_selectstatement_has_from_():
    assert hasattr(plsql_statement_SelectStatement, "from_")
    descriptor = None
    for klass in plsql_statement_SelectStatement.__mro__:
        if "from_" in klass.__dict__:
            descriptor = klass.__dict__["from_"]
            break
    assert isinstance(descriptor, property)

def test_plsql_statement_selectstatement_has_selectList():
    assert hasattr(plsql_statement_SelectStatement, "selectList")
    descriptor = None
    for klass in plsql_statement_SelectStatement.__mro__:
        if "selectList" in klass.__dict__:
            descriptor = klass.__dict__["selectList"]
            break
    assert isinstance(descriptor, property)

def test_plsql_statement_selectstatement_has_distinct():
    assert hasattr(plsql_statement_SelectStatement, "distinct")
    descriptor = None
    for klass in plsql_statement_SelectStatement.__mro__:
        if "distinct" in klass.__dict__:
            descriptor = klass.__dict__["distinct"]
            break
    assert isinstance(descriptor, property)

def test_plsql_statement_selectstatement_has_isCount():
    assert hasattr(plsql_statement_SelectStatement, "isCount")
    descriptor = None
    for klass in plsql_statement_SelectStatement.__mro__:
        if "isCount" in klass.__dict__:
            descriptor = klass.__dict__["isCount"]
            break
    assert isinstance(descriptor, property)

def test_plsql_statement_selectstatement_has_bulk():
    assert hasattr(plsql_statement_SelectStatement, "bulk")
    descriptor = None
    for klass in plsql_statement_SelectStatement.__mro__:
        if "bulk" in klass.__dict__:
            descriptor = klass.__dict__["bulk"]
            break
    assert isinstance(descriptor, property)



def test_exceptionsection_is_not_abstract():
    assert not inspect.isabstract(ExceptionSection)


def test_exceptionsection_constructor_exists():
    assert callable(ExceptionSection.__init__)


def test_exceptionsection_constructor_args():
    sig = inspect.signature(ExceptionSection.__init__)
    params = list(sig.parameters.keys())



def test_declaration_is_not_abstract():
    assert not inspect.isabstract(Declaration)


def test_declaration_constructor_exists():
    assert callable(Declaration.__init__)


def test_declaration_constructor_args():
    sig = inspect.signature(Declaration.__init__)
    params = list(sig.parameters.keys())



def test_plsql_declaration_cursordeclaration_is_not_abstract():
    assert not inspect.isabstract(plsql_declaration_CursorDeclaration)


def test_plsql_declaration_cursordeclaration_constructor_exists():
    assert callable(plsql_declaration_CursorDeclaration.__init__)


def test_plsql_declaration_cursordeclaration_constructor_args():
    sig = inspect.signature(plsql_declaration_CursorDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_plsql_declaration_proceduredeclaration_is_not_abstract():
    assert not inspect.isabstract(plsql_declaration_ProcedureDeclaration)


def test_plsql_declaration_proceduredeclaration_constructor_exists():
    assert callable(plsql_declaration_ProcedureDeclaration.__init__)


def test_plsql_declaration_proceduredeclaration_constructor_args():
    sig = inspect.signature(plsql_declaration_ProcedureDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(VariableDeclaration)


def test_variabledeclaration_constructor_exists():
    assert callable(VariableDeclaration.__init__)


def test_variabledeclaration_constructor_args():
    sig = inspect.signature(VariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_loopstatement_is_not_abstract():
    assert not inspect.isabstract(LoopStatement)


def test_loopstatement_constructor_exists():
    assert callable(LoopStatement.__init__)


def test_loopstatement_constructor_args():
    sig = inspect.signature(LoopStatement.__init__)
    params = list(sig.parameters.keys())



def test_plsql_statement_forstatement_is_not_abstract():
    assert not inspect.isabstract(plsql_statement_ForStatement)


def test_plsql_statement_forstatement_constructor_exists():
    assert callable(plsql_statement_ForStatement.__init__)


def test_plsql_statement_forstatement_constructor_args():
    sig = inspect.signature(plsql_statement_ForStatement.__init__)
    params = list(sig.parameters.keys())



def test_varrefexpression_is_not_abstract():
    assert not inspect.isabstract(VarRefExpression)


def test_varrefexpression_constructor_exists():
    assert callable(VarRefExpression.__init__)


def test_varrefexpression_constructor_args():
    sig = inspect.signature(VarRefExpression.__init__)
    params = list(sig.parameters.keys())



def test_plsql_expression_sqlcursor_is_not_abstract():
    assert not inspect.isabstract(plsql_expression_SQLCursor)


def test_plsql_expression_sqlcursor_constructor_exists():
    assert callable(plsql_expression_SQLCursor.__init__)


def test_plsql_expression_sqlcursor_constructor_args():
    sig = inspect.signature(plsql_expression_SQLCursor.__init__)
    params = list(sig.parameters.keys())



def test_plsql_expression_sqlvariable_is_not_abstract():
    assert not inspect.isabstract(plsql_expression_SQLVariable)


def test_plsql_expression_sqlvariable_constructor_exists():
    assert callable(plsql_expression_SQLVariable.__init__)


def test_plsql_expression_sqlvariable_constructor_args():
    sig = inspect.signature(plsql_expression_SQLVariable.__init__)
    params = list(sig.parameters.keys())



def test_plsql_expression_formsvarref_is_not_abstract():
    assert not inspect.isabstract(plsql_expression_FormsVarRef)


def test_plsql_expression_formsvarref_constructor_exists():
    assert callable(plsql_expression_FormsVarRef.__init__)


def test_plsql_expression_formsvarref_constructor_args():
    sig = inspect.signature(plsql_expression_FormsVarRef.__init__)
    params = list(sig.parameters.keys())
    assert "reference" in params, "Missing parameter 'reference'"

def test_plsql_expression_formsvarref_has_reference():
    assert hasattr(plsql_expression_FormsVarRef, "reference")
    descriptor = None
    for klass in plsql_expression_FormsVarRef.__mro__:
        if "reference" in klass.__dict__:
            descriptor = klass.__dict__["reference"]
            break
    assert isinstance(descriptor, property)



def test_cursordeclaration_is_not_abstract():
    assert not inspect.isabstract(CursorDeclaration)


def test_cursordeclaration_constructor_exists():
    assert callable(CursorDeclaration.__init__)


def test_cursordeclaration_constructor_args():
    sig = inspect.signature(CursorDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_controlsqlstatement_is_not_abstract():
    assert not inspect.isabstract(ControlSQLStatement)


def test_controlsqlstatement_constructor_exists():
    assert callable(ControlSQLStatement.__init__)


def test_controlsqlstatement_constructor_args():
    sig = inspect.signature(ControlSQLStatement.__init__)
    params = list(sig.parameters.keys())



def test_plsql_statement_locktablestatement_is_not_abstract():
    assert not inspect.isabstract(plsql_statement_LockTableStatement)


def test_plsql_statement_locktablestatement_constructor_exists():
    assert callable(plsql_statement_LockTableStatement.__init__)


def test_plsql_statement_locktablestatement_constructor_args():
    sig = inspect.signature(plsql_statement_LockTableStatement.__init__)
    params = list(sig.parameters.keys())



def test_plsql_statement_commitstatement_is_not_abstract():
    assert not inspect.isabstract(plsql_statement_CommitStatement)


def test_plsql_statement_commitstatement_constructor_exists():
    assert callable(plsql_statement_CommitStatement.__init__)


def test_plsql_statement_commitstatement_constructor_args():
    sig = inspect.signature(plsql_statement_CommitStatement.__init__)
    params = list(sig.parameters.keys())



def test_plsql_statement_fetchstatement_is_not_abstract():
    assert not inspect.isabstract(plsql_statement_FetchStatement)


def test_plsql_statement_fetchstatement_constructor_exists():
    assert callable(plsql_statement_FetchStatement.__init__)


def test_plsql_statement_fetchstatement_constructor_args():
    sig = inspect.signature(plsql_statement_FetchStatement.__init__)
    params = list(sig.parameters.keys())



def test_plsql_statement_savepointstatement_is_not_abstract():
    assert not inspect.isabstract(plsql_statement_SavepointStatement)


def test_plsql_statement_savepointstatement_constructor_exists():
    assert callable(plsql_statement_SavepointStatement.__init__)


def test_plsql_statement_savepointstatement_constructor_args():
    sig = inspect.signature(plsql_statement_SavepointStatement.__init__)
    params = list(sig.parameters.keys())



def test_plsql_statement_rollbackstatement_is_not_abstract():
    assert not inspect.isabstract(plsql_statement_RollbackStatement)


def test_plsql_statement_rollbackstatement_constructor_exists():
    assert callable(plsql_statement_RollbackStatement.__init__)


def test_plsql_statement_rollbackstatement_constructor_args():
    sig = inspect.signature(plsql_statement_RollbackStatement.__init__)
    params = list(sig.parameters.keys())



def test_plsql_statement_openstatement_is_not_abstract():
    assert not inspect.isabstract(plsql_statement_OpenStatement)


def test_plsql_statement_openstatement_constructor_exists():
    assert callable(plsql_statement_OpenStatement.__init__)


def test_plsql_statement_openstatement_constructor_args():
    sig = inspect.signature(plsql_statement_OpenStatement.__init__)
    params = list(sig.parameters.keys())



def test_plsql_statement_closestatement_is_not_abstract():
    assert not inspect.isabstract(plsql_statement_CloseStatement)


def test_plsql_statement_closestatement_constructor_exists():
    assert callable(plsql_statement_CloseStatement.__init__)


def test_plsql_statement_closestatement_constructor_args():
    sig = inspect.signature(plsql_statement_CloseStatement.__init__)
    params = list(sig.parameters.keys())



def test_sqlstatement_is_not_abstract():
    assert not inspect.isabstract(SQLStatement)


def test_sqlstatement_constructor_exists():
    assert callable(SQLStatement.__init__)


def test_sqlstatement_constructor_args():
    sig = inspect.signature(SQLStatement.__init__)
    params = list(sig.parameters.keys())



def test_plsql_statement_modifysqlstatement_is_not_abstract():
    assert not inspect.isabstract(plsql_statement_ModifySQLStatement)


def test_plsql_statement_modifysqlstatement_constructor_exists():
    assert callable(plsql_statement_ModifySQLStatement.__init__)


def test_plsql_statement_modifysqlstatement_constructor_args():
    sig = inspect.signature(plsql_statement_ModifySQLStatement.__init__)
    params = list(sig.parameters.keys())



def test_plsql_statement_controlsqlstatement_is_not_abstract():
    assert not inspect.isabstract(plsql_statement_ControlSQLStatement)


def test_plsql_statement_controlsqlstatement_constructor_exists():
    assert callable(plsql_statement_ControlSQLStatement.__init__)


def test_plsql_statement_controlsqlstatement_constructor_args():
    sig = inspect.signature(plsql_statement_ControlSQLStatement.__init__)
    params = list(sig.parameters.keys())



def test_functioncallparameter_is_not_abstract():
    assert not inspect.isabstract(FunctionCallParameter)


def test_functioncallparameter_constructor_exists():
    assert callable(FunctionCallParameter.__init__)


def test_functioncallparameter_constructor_args():
    sig = inspect.signature(FunctionCallParameter.__init__)
    params = list(sig.parameters.keys())



def test_expression_expression_is_not_abstract():
    assert not inspect.isabstract(expression_Expression)


def test_expression_expression_constructor_exists():
    assert callable(expression_Expression.__init__)


def test_expression_expression_constructor_args():
    sig = inspect.signature(expression_Expression.__init__)
    params = list(sig.parameters.keys())



def test_plsql_expression_booleanexpression_is_not_abstract():
    assert not inspect.isabstract(plsql_expression_BooleanExpression)


def test_plsql_expression_booleanexpression_constructor_exists():
    assert callable(plsql_expression_BooleanExpression.__init__)


def test_plsql_expression_booleanexpression_constructor_args():
    sig = inspect.signature(plsql_expression_BooleanExpression.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_plsql_expression_booleanexpression_has_type():
    assert hasattr(plsql_expression_BooleanExpression, "type")
    descriptor = None
    for klass in plsql_expression_BooleanExpression.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_plsql_statement_nullstatement_is_not_abstract():
    assert not inspect.isabstract(plsql_statement_NullStatement)


def test_plsql_statement_nullstatement_constructor_exists():
    assert callable(plsql_statement_NullStatement.__init__)


def test_plsql_statement_nullstatement_constructor_args():
    sig = inspect.signature(plsql_statement_NullStatement.__init__)
    params = list(sig.parameters.keys())



def test_plsql_statement_returnstatement_is_not_abstract():
    assert not inspect.isabstract(plsql_statement_ReturnStatement)


def test_plsql_statement_returnstatement_constructor_exists():
    assert callable(plsql_statement_ReturnStatement.__init__)


def test_plsql_statement_returnstatement_constructor_args():
    sig = inspect.signature(plsql_statement_ReturnStatement.__init__)
    params = list(sig.parameters.keys())



def test_plsql_statement_raisestatement_is_not_abstract():
    assert not inspect.isabstract(plsql_statement_RaiseStatement)


def test_plsql_statement_raisestatement_constructor_exists():
    assert callable(plsql_statement_RaiseStatement.__init__)


def test_plsql_statement_raisestatement_constructor_args():
    sig = inspect.signature(plsql_statement_RaiseStatement.__init__)
    params = list(sig.parameters.keys())
    assert "exception" in params, "Missing parameter 'exception'"

def test_plsql_statement_raisestatement_has_exception():
    assert hasattr(plsql_statement_RaiseStatement, "exception")
    descriptor = None
    for klass in plsql_statement_RaiseStatement.__mro__:
        if "exception" in klass.__dict__:
            descriptor = klass.__dict__["exception"]
            break
    assert isinstance(descriptor, property)



def test_plsql_statement_sqlstatement_is_not_abstract():
    assert not inspect.isabstract(plsql_statement_SQLStatement)


def test_plsql_statement_sqlstatement_constructor_exists():
    assert callable(plsql_statement_SQLStatement.__init__)


def test_plsql_statement_sqlstatement_constructor_args():
    sig = inspect.signature(plsql_statement_SQLStatement.__init__)
    params = list(sig.parameters.keys())



def test_plsql_statement_blockstatement_is_not_abstract():
    assert not inspect.isabstract(plsql_statement_BlockStatement)


def test_plsql_statement_blockstatement_constructor_exists():
    assert callable(plsql_statement_BlockStatement.__init__)


def test_plsql_statement_blockstatement_constructor_args():
    sig = inspect.signature(plsql_statement_BlockStatement.__init__)
    params = list(sig.parameters.keys())



def test_plsql_statement_assignmentstatement_is_not_abstract():
    assert not inspect.isabstract(plsql_statement_AssignmentStatement)


def test_plsql_statement_assignmentstatement_constructor_exists():
    assert callable(plsql_statement_AssignmentStatement.__init__)


def test_plsql_statement_assignmentstatement_constructor_args():
    sig = inspect.signature(plsql_statement_AssignmentStatement.__init__)
    params = list(sig.parameters.keys())



def test_plsql_statement_statement_is_not_abstract():
    assert not inspect.isabstract(plsql_statement_Statement)


def test_plsql_statement_statement_constructor_exists():
    assert callable(plsql_statement_Statement.__init__)


def test_plsql_statement_statement_constructor_args():
    sig = inspect.signature(plsql_statement_Statement.__init__)
    params = list(sig.parameters.keys())



def test_plsql_statement_loopstatement_is_not_abstract():
    assert not inspect.isabstract(plsql_statement_LoopStatement)


def test_plsql_statement_loopstatement_constructor_exists():
    assert callable(plsql_statement_LoopStatement.__init__)


def test_plsql_statement_loopstatement_constructor_args():
    sig = inspect.signature(plsql_statement_LoopStatement.__init__)
    params = list(sig.parameters.keys())



def test_ifstatement_is_not_abstract():
    assert not inspect.isabstract(IfStatement)


def test_ifstatement_constructor_exists():
    assert callable(IfStatement.__init__)


def test_ifstatement_constructor_args():
    sig = inspect.signature(IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_plsql_statement_ifstatement_is_not_abstract():
    assert not inspect.isabstract(plsql_statement_IfStatement)


def test_plsql_statement_ifstatement_constructor_exists():
    assert callable(plsql_statement_IfStatement.__init__)


def test_plsql_statement_ifstatement_constructor_args():
    sig = inspect.signature(plsql_statement_IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_plsql_statement_casestatement_is_not_abstract():
    assert not inspect.isabstract(plsql_statement_CaseStatement)


def test_plsql_statement_casestatement_constructor_exists():
    assert callable(plsql_statement_CaseStatement.__init__)


def test_plsql_statement_casestatement_constructor_args():
    sig = inspect.signature(plsql_statement_CaseStatement.__init__)
    params = list(sig.parameters.keys())



def test_declaration_namedelement_is_not_abstract():
    assert not inspect.isabstract(declaration_NamedElement)


def test_declaration_namedelement_constructor_exists():
    assert callable(declaration_NamedElement.__init__)


def test_declaration_namedelement_constructor_args():
    sig = inspect.signature(declaration_NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_plsql_declaration_argument_is_not_abstract():
    assert not inspect.isabstract(plsql_declaration_Argument)


def test_plsql_declaration_argument_constructor_exists():
    assert callable(plsql_declaration_Argument.__init__)


def test_plsql_declaration_argument_constructor_args():
    sig = inspect.signature(plsql_declaration_Argument.__init__)
    params = list(sig.parameters.keys())
    assert "out" in params, "Missing parameter 'out'"
    assert "default" in params, "Missing parameter 'default'"
    assert "in_" in params, "Missing parameter 'in_'"

def test_plsql_declaration_argument_has_out():
    assert hasattr(plsql_declaration_Argument, "out")
    descriptor = None
    for klass in plsql_declaration_Argument.__mro__:
        if "out" in klass.__dict__:
            descriptor = klass.__dict__["out"]
            break
    assert isinstance(descriptor, property)

def test_plsql_declaration_argument_has_default():
    assert hasattr(plsql_declaration_Argument, "default")
    descriptor = None
    for klass in plsql_declaration_Argument.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)

def test_plsql_declaration_argument_has_in_():
    assert hasattr(plsql_declaration_Argument, "in_")
    descriptor = None
    for klass in plsql_declaration_Argument.__mro__:
        if "in_" in klass.__dict__:
            descriptor = klass.__dict__["in_"]
            break
    assert isinstance(descriptor, property)



def test_plsql_declaration_triggerblock_is_not_abstract():
    assert not inspect.isabstract(plsql_declaration_TriggerBlock)


def test_plsql_declaration_triggerblock_constructor_exists():
    assert callable(plsql_declaration_TriggerBlock.__init__)


def test_plsql_declaration_triggerblock_constructor_args():
    sig = inspect.signature(plsql_declaration_TriggerBlock.__init__)
    params = list(sig.parameters.keys())



def test_statement_statement_is_not_abstract():
    assert not inspect.isabstract(statement_Statement)


def test_statement_statement_constructor_exists():
    assert callable(statement_Statement.__init__)


def test_statement_statement_constructor_args():
    sig = inspect.signature(statement_Statement.__init__)
    params = list(sig.parameters.keys())



def test_plsql_statement_functioncallstatement_is_not_abstract():
    assert not inspect.isabstract(plsql_statement_FunctionCallStatement)


def test_plsql_statement_functioncallstatement_constructor_exists():
    assert callable(plsql_statement_FunctionCallStatement.__init__)


def test_plsql_statement_functioncallstatement_constructor_args():
    sig = inspect.signature(plsql_statement_FunctionCallStatement.__init__)
    params = list(sig.parameters.keys())



def test_plsql_statement_gotostatement_is_not_abstract():
    assert not inspect.isabstract(plsql_statement_GotoStatement)


def test_plsql_statement_gotostatement_constructor_exists():
    assert callable(plsql_statement_GotoStatement.__init__)


def test_plsql_statement_gotostatement_constructor_args():
    sig = inspect.signature(plsql_statement_GotoStatement.__init__)
    params = list(sig.parameters.keys())



def test_plsql_statement_exitstatement_is_not_abstract():
    assert not inspect.isabstract(plsql_statement_ExitStatement)


def test_plsql_statement_exitstatement_constructor_exists():
    assert callable(plsql_statement_ExitStatement.__init__)


def test_plsql_statement_exitstatement_constructor_args():
    sig = inspect.signature(plsql_statement_ExitStatement.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_plsql_expression_propertyaccess_is_not_abstract():
    assert not inspect.isabstract(plsql_expression_PropertyAccess)


def test_plsql_expression_propertyaccess_constructor_exists():
    assert callable(plsql_expression_PropertyAccess.__init__)


def test_plsql_expression_propertyaccess_constructor_args():
    sig = inspect.signature(plsql_expression_PropertyAccess.__init__)
    params = list(sig.parameters.keys())
    assert "propertyName" in params, "Missing parameter 'propertyName'"

def test_plsql_expression_propertyaccess_has_propertyName():
    assert hasattr(plsql_expression_PropertyAccess, "propertyName")
    descriptor = None
    for klass in plsql_expression_PropertyAccess.__mro__:
        if "propertyName" in klass.__dict__:
            descriptor = klass.__dict__["propertyName"]
            break
    assert isinstance(descriptor, property)



def test_plsql_expression_varrefexpression_is_not_abstract():
    assert not inspect.isabstract(plsql_expression_VarRefExpression)


def test_plsql_expression_varrefexpression_constructor_exists():
    assert callable(plsql_expression_VarRefExpression.__init__)


def test_plsql_expression_varrefexpression_constructor_args():
    sig = inspect.signature(plsql_expression_VarRefExpression.__init__)
    params = list(sig.parameters.keys())



def test_plsql_expression_inrangeexpression_is_not_abstract():
    assert not inspect.isabstract(plsql_expression_InRangeExpression)


def test_plsql_expression_inrangeexpression_constructor_exists():
    assert callable(plsql_expression_InRangeExpression.__init__)


def test_plsql_expression_inrangeexpression_constructor_args():
    sig = inspect.signature(plsql_expression_InRangeExpression.__init__)
    params = list(sig.parameters.keys())



def test_plsql_expression_arithmeticexpression_is_not_abstract():
    assert not inspect.isabstract(plsql_expression_ArithmeticExpression)


def test_plsql_expression_arithmeticexpression_constructor_exists():
    assert callable(plsql_expression_ArithmeticExpression.__init__)


def test_plsql_expression_arithmeticexpression_constructor_args():
    sig = inspect.signature(plsql_expression_ArithmeticExpression.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_plsql_expression_arithmeticexpression_has_type():
    assert hasattr(plsql_expression_ArithmeticExpression, "type")
    descriptor = None
    for klass in plsql_expression_ArithmeticExpression.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_plsql_expression_literalexpression_is_not_abstract():
    assert not inspect.isabstract(plsql_expression_LiteralExpression)


def test_plsql_expression_literalexpression_constructor_exists():
    assert callable(plsql_expression_LiteralExpression.__init__)


def test_plsql_expression_literalexpression_constructor_args():
    sig = inspect.signature(plsql_expression_LiteralExpression.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "value" in params, "Missing parameter 'value'"

def test_plsql_expression_literalexpression_has_type():
    assert hasattr(plsql_expression_LiteralExpression, "type")
    descriptor = None
    for klass in plsql_expression_LiteralExpression.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_plsql_expression_literalexpression_has_value():
    assert hasattr(plsql_expression_LiteralExpression, "value")
    descriptor = None
    for klass in plsql_expression_LiteralExpression.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_plsql_expression_likeexpression_is_not_abstract():
    assert not inspect.isabstract(plsql_expression_LikeExpression)


def test_plsql_expression_likeexpression_constructor_exists():
    assert callable(plsql_expression_LikeExpression.__init__)


def test_plsql_expression_likeexpression_constructor_args():
    sig = inspect.signature(plsql_expression_LikeExpression.__init__)
    params = list(sig.parameters.keys())



def test_plsql_expression_notexpression_is_not_abstract():
    assert not inspect.isabstract(plsql_expression_NotExpression)


def test_plsql_expression_notexpression_constructor_exists():
    assert callable(plsql_expression_NotExpression.__init__)


def test_plsql_expression_notexpression_constructor_args():
    sig = inspect.signature(plsql_expression_NotExpression.__init__)
    params = list(sig.parameters.keys())



def test_plsql_expression_stringoperation_is_not_abstract():
    assert not inspect.isabstract(plsql_expression_StringOperation)


def test_plsql_expression_stringoperation_constructor_exists():
    assert callable(plsql_expression_StringOperation.__init__)


def test_plsql_expression_stringoperation_constructor_args():
    sig = inspect.signature(plsql_expression_StringOperation.__init__)
    params = list(sig.parameters.keys())



def test_plsql_expression_isnullexpression_is_not_abstract():
    assert not inspect.isabstract(plsql_expression_IsNullExpression)


def test_plsql_expression_isnullexpression_constructor_exists():
    assert callable(plsql_expression_IsNullExpression.__init__)


def test_plsql_expression_isnullexpression_constructor_args():
    sig = inspect.signature(plsql_expression_IsNullExpression.__init__)
    params = list(sig.parameters.keys())



def test_plsql_expression_foundexpression_is_not_abstract():
    assert not inspect.isabstract(plsql_expression_FoundExpression)


def test_plsql_expression_foundexpression_constructor_exists():
    assert callable(plsql_expression_FoundExpression.__init__)


def test_plsql_expression_foundexpression_constructor_args():
    sig = inspect.signature(plsql_expression_FoundExpression.__init__)
    params = list(sig.parameters.keys())

def test_basictypes_exists():
    # Check that the Enumeration exists
    assert BasicTypes is not None

def test_basictypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BasicTypes]
    expected_literals = [
        "DECIMAL",
        "INT",
        "DEC",
        "FLOAT",
        "DOUBLE",
        "BLOB",
        "REAL",
        "VARCHAR",
        "CLOB",
        "LONG",
        "NUMBER",
        "NCHAR",
        "VARCHAR2",
        "BINARY_FLOAT",
        "NUMERIC",
        "BINARY_DOUBLE",
        "INTEGER",
        "NATURAL",
        "DATE",
        "NVARCHAR",
        "BOOLEAN",
        "CHARACTER",
        "BINARY_INTEGER",
        "NVARCHAR2",
        "CHAR",
        "POSITIVE",
        "ROWID",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BasicTypes"

def test_literalexpressiontype_exists():
    # Check that the Enumeration exists
    assert LiteralExpressionType is not None

def test_literalexpressiontype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LiteralExpressionType]
    expected_literals = [
        "NULL",
        "STRING",
        "BOOLEAN",
        "INTEGER",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LiteralExpressionType"

def test_arithmeticoperatortype_exists():
    # Check that the Enumeration exists
    assert ArithmeticOperatorType is not None

def test_arithmeticoperatortype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ArithmeticOperatorType]
    expected_literals = [
        "PLUS",
        "NEGATIVE",
        "EXPONENT",
        "MULTIPLICATION",
        "DIVISION",
        "POSITIVE",
        "MINUS",
        "DOUBLEVERTICALBAR",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ArithmeticOperatorType"

def test_booleanoperatortype_exists():
    # Check that the Enumeration exists
    assert BooleanOperatorType is not None

def test_booleanoperatortype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BooleanOperatorType]
    expected_literals = [
        "GREATERTHAN",
        "OR",
        "NOT",
        "NOTEQUALS",
        "LESSEQUALS",
        "EQUALS",
        "GREATEREQUALS",
        "LESSTHAN",
        "AND",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BooleanOperatorType"


# =============================================================================
# HYPOTHESIS STRATEGIES
# =============================================================================

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())
plsql_declaration_NamedElement_strategy = st.builds(
    plsql_declaration_NamedElement,
    name=
        safe_text
)
TriggerBlock_strategy = st.builds(
    TriggerBlock,
)
SelectStatement_strategy = st.builds(
    SelectStatement,
)
plsql_declaration_PLSQLDefinition_strategy = st.builds(
    plsql_declaration_PLSQLDefinition,
)
statement_BlockStatement_strategy = st.builds(
    statement_BlockStatement,
)
plsql_condition_SQLCondition_strategy = st.builds(
    plsql_condition_SQLCondition,
)
plsql_type_TypedElement_strategy = st.builds(
    plsql_type_TypedElement,
)
Argument_strategy = st.builds(
    Argument,
)
type_TypedElement_strategy = st.builds(
    type_TypedElement,
)
declaration_Declaration_strategy = st.builds(
    declaration_Declaration,
)
plsql_declaration_FunctionDeclaration_strategy = st.builds(
    plsql_declaration_FunctionDeclaration,
)
plsql_declaration_VariableDeclaration_strategy = st.builds(
    plsql_declaration_VariableDeclaration,
    constant=
        st.booleans(),
    default=
        st.booleans(),
    notnull=
        st.booleans()
)
NamedElement_strategy = st.builds(
    NamedElement,
)
plsql_declaration_Declaration_strategy = st.builds(
    plsql_declaration_Declaration,
)
plsql_declaration_Package_strategy = st.builds(
    plsql_declaration_Package,
)
plsql_expression_FunctionCallParameter_strategy = st.builds(
    plsql_expression_FunctionCallParameter,
)
Type_strategy = st.builds(
    Type,
)
plsql_type_GenericType_strategy = st.builds(
    plsql_type_GenericType,
)
plsql_type_IndirectType_strategy = st.builds(
    plsql_type_IndirectType,
    identifier=
        safe_text,
    range=
        st.integers(),
    type=
        st.booleans(),
    rowtype=
        st.booleans()
)
plsql_type_Datatype_strategy = st.builds(
    plsql_type_Datatype,
    range=
        st.integers(),
    name=
        safe_text
)
plsql_type_Type_strategy = st.builds(
    plsql_type_Type,
)
StringOperation_strategy = st.builds(
    StringOperation,
)
plsql_expression_ConcatString_strategy = st.builds(
    plsql_expression_ConcatString,
)
plsql_statement_ExceptionSection_strategy = st.builds(
    plsql_statement_ExceptionSection,
    exceptionNames=
        safe_text
)
plsql_statement_UpdatePair_strategy = st.builds(
    plsql_statement_UpdatePair,
    column=
        safe_text
)
UpdatePair_strategy = st.builds(
    UpdatePair,
)
condition_SQLCondition_strategy = st.builds(
    condition_SQLCondition,
)
plsql_expression_Expression_strategy = st.builds(
    plsql_expression_Expression,
)
SQLCondition_strategy = st.builds(
    SQLCondition,
)
plsql_condition_BooleanCondition_strategy = st.builds(
    plsql_condition_BooleanCondition,
    type=
        safe_text
)
plsql_condition_ConditionComparison_strategy = st.builds(
    plsql_condition_ConditionComparison,
    type=
        safe_text
)
plsql_condition_NotCondition_strategy = st.builds(
    plsql_condition_NotCondition,
)
ModifySQLStatement_strategy = st.builds(
    ModifySQLStatement,
)
plsql_statement_UpdateStatement_strategy = st.builds(
    plsql_statement_UpdateStatement,
    table=
        safe_text
)
plsql_statement_DeleteStatement_strategy = st.builds(
    plsql_statement_DeleteStatement,
)
plsql_statement_SetTransactionStatement_strategy = st.builds(
    plsql_statement_SetTransactionStatement,
)
plsql_statement_InsertStatement_strategy = st.builds(
    plsql_statement_InsertStatement,
    columns=
        safe_text,
    into=
        safe_text
)
plsql_statement_SelectStatement_strategy = st.builds(
    plsql_statement_SelectStatement,
    collect=
        st.booleans(),
    unique=
        st.booleans(),
    all=
        st.booleans(),
    from_=
        safe_text,
    selectList=
        safe_text,
    distinct=
        st.booleans(),
    isCount=
        st.booleans(),
    bulk=
        st.booleans()
)
ExceptionSection_strategy = st.builds(
    ExceptionSection,
)
Declaration_strategy = st.builds(
    Declaration,
)
plsql_declaration_CursorDeclaration_strategy = st.builds(
    plsql_declaration_CursorDeclaration,
)
plsql_declaration_ProcedureDeclaration_strategy = st.builds(
    plsql_declaration_ProcedureDeclaration,
)
VariableDeclaration_strategy = st.builds(
    VariableDeclaration,
)
LoopStatement_strategy = st.builds(
    LoopStatement,
)
plsql_statement_ForStatement_strategy = st.builds(
    plsql_statement_ForStatement,
)
VarRefExpression_strategy = st.builds(
    VarRefExpression,
)
plsql_expression_SQLCursor_strategy = st.builds(
    plsql_expression_SQLCursor,
)
plsql_expression_SQLVariable_strategy = st.builds(
    plsql_expression_SQLVariable,
)
plsql_expression_FormsVarRef_strategy = st.builds(
    plsql_expression_FormsVarRef,
    reference=
        safe_text
)
CursorDeclaration_strategy = st.builds(
    CursorDeclaration,
)
ControlSQLStatement_strategy = st.builds(
    ControlSQLStatement,
)
plsql_statement_LockTableStatement_strategy = st.builds(
    plsql_statement_LockTableStatement,
)
plsql_statement_CommitStatement_strategy = st.builds(
    plsql_statement_CommitStatement,
)
plsql_statement_FetchStatement_strategy = st.builds(
    plsql_statement_FetchStatement,
)
plsql_statement_SavepointStatement_strategy = st.builds(
    plsql_statement_SavepointStatement,
)
plsql_statement_RollbackStatement_strategy = st.builds(
    plsql_statement_RollbackStatement,
)
plsql_statement_OpenStatement_strategy = st.builds(
    plsql_statement_OpenStatement,
)
plsql_statement_CloseStatement_strategy = st.builds(
    plsql_statement_CloseStatement,
)
SQLStatement_strategy = st.builds(
    SQLStatement,
)
plsql_statement_ModifySQLStatement_strategy = st.builds(
    plsql_statement_ModifySQLStatement,
)
plsql_statement_ControlSQLStatement_strategy = st.builds(
    plsql_statement_ControlSQLStatement,
)
FunctionCallParameter_strategy = st.builds(
    FunctionCallParameter,
)
expression_Expression_strategy = st.builds(
    expression_Expression,
)
plsql_expression_BooleanExpression_strategy = st.builds(
    plsql_expression_BooleanExpression,
    type=
        safe_text
)
Statement_strategy = st.builds(
    Statement,
)
plsql_statement_NullStatement_strategy = st.builds(
    plsql_statement_NullStatement,
)
plsql_statement_ReturnStatement_strategy = st.builds(
    plsql_statement_ReturnStatement,
)
plsql_statement_RaiseStatement_strategy = st.builds(
    plsql_statement_RaiseStatement,
    exception=
        safe_text
)
plsql_statement_SQLStatement_strategy = st.builds(
    plsql_statement_SQLStatement,
)
plsql_statement_BlockStatement_strategy = st.builds(
    plsql_statement_BlockStatement,
)
plsql_statement_AssignmentStatement_strategy = st.builds(
    plsql_statement_AssignmentStatement,
)
plsql_statement_Statement_strategy = st.builds(
    plsql_statement_Statement,
)
plsql_statement_LoopStatement_strategy = st.builds(
    plsql_statement_LoopStatement,
)
IfStatement_strategy = st.builds(
    IfStatement,
)
plsql_statement_IfStatement_strategy = st.builds(
    plsql_statement_IfStatement,
)
plsql_statement_CaseStatement_strategy = st.builds(
    plsql_statement_CaseStatement,
)
declaration_NamedElement_strategy = st.builds(
    declaration_NamedElement,
)
plsql_declaration_Argument_strategy = st.builds(
    plsql_declaration_Argument,
    out=
        st.booleans(),
    default=
        st.booleans(),
    in_=
        st.booleans()
)
plsql_declaration_TriggerBlock_strategy = st.builds(
    plsql_declaration_TriggerBlock,
)
statement_Statement_strategy = st.builds(
    statement_Statement,
)
plsql_statement_FunctionCallStatement_strategy = st.builds(
    plsql_statement_FunctionCallStatement,
)
plsql_statement_GotoStatement_strategy = st.builds(
    plsql_statement_GotoStatement,
)
plsql_statement_ExitStatement_strategy = st.builds(
    plsql_statement_ExitStatement,
)
Expression_strategy = st.builds(
    Expression,
)
plsql_expression_PropertyAccess_strategy = st.builds(
    plsql_expression_PropertyAccess,
    propertyName=
        safe_text
)
plsql_expression_VarRefExpression_strategy = st.builds(
    plsql_expression_VarRefExpression,
)
plsql_expression_InRangeExpression_strategy = st.builds(
    plsql_expression_InRangeExpression,
)
plsql_expression_ArithmeticExpression_strategy = st.builds(
    plsql_expression_ArithmeticExpression,
    type=
        safe_text
)
plsql_expression_LiteralExpression_strategy = st.builds(
    plsql_expression_LiteralExpression,
    type=
        safe_text,
    value=
        safe_text
)
plsql_expression_LikeExpression_strategy = st.builds(
    plsql_expression_LikeExpression,
)
plsql_expression_NotExpression_strategy = st.builds(
    plsql_expression_NotExpression,
)
plsql_expression_StringOperation_strategy = st.builds(
    plsql_expression_StringOperation,
)
plsql_expression_IsNullExpression_strategy = st.builds(
    plsql_expression_IsNullExpression,
)
plsql_expression_FoundExpression_strategy = st.builds(
    plsql_expression_FoundExpression,
)

@given(instance=plsql_declaration_NamedElement_strategy)
@settings(max_examples=50)
def test_plsql_declaration_namedelement_instantiation(instance):
    assert isinstance(instance, plsql_declaration_NamedElement)



@given(instance=plsql_declaration_NamedElement_strategy)
def test_plsql_declaration_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=TriggerBlock_strategy)
@settings(max_examples=50)
def test_triggerblock_instantiation(instance):
    assert isinstance(instance, TriggerBlock)

@given(instance=SelectStatement_strategy)
@settings(max_examples=50)
def test_selectstatement_instantiation(instance):
    assert isinstance(instance, SelectStatement)

@given(instance=plsql_declaration_PLSQLDefinition_strategy)
@settings(max_examples=50)
def test_plsql_declaration_plsqldefinition_instantiation(instance):
    assert isinstance(instance, plsql_declaration_PLSQLDefinition)

@given(instance=statement_BlockStatement_strategy)
@settings(max_examples=50)
def test_statement_blockstatement_instantiation(instance):
    assert isinstance(instance, statement_BlockStatement)

@given(instance=plsql_condition_SQLCondition_strategy)
@settings(max_examples=50)
def test_plsql_condition_sqlcondition_instantiation(instance):
    assert isinstance(instance, plsql_condition_SQLCondition)

@given(instance=plsql_type_TypedElement_strategy)
@settings(max_examples=50)
def test_plsql_type_typedelement_instantiation(instance):
    assert isinstance(instance, plsql_type_TypedElement)

@given(instance=Argument_strategy)
@settings(max_examples=50)
def test_argument_instantiation(instance):
    assert isinstance(instance, Argument)

@given(instance=type_TypedElement_strategy)
@settings(max_examples=50)
def test_type_typedelement_instantiation(instance):
    assert isinstance(instance, type_TypedElement)

@given(instance=declaration_Declaration_strategy)
@settings(max_examples=50)
def test_declaration_declaration_instantiation(instance):
    assert isinstance(instance, declaration_Declaration)

@given(instance=plsql_declaration_FunctionDeclaration_strategy)
@settings(max_examples=50)
def test_plsql_declaration_functiondeclaration_instantiation(instance):
    assert isinstance(instance, plsql_declaration_FunctionDeclaration)

@given(instance=plsql_declaration_VariableDeclaration_strategy)
@settings(max_examples=50)
def test_plsql_declaration_variabledeclaration_instantiation(instance):
    assert isinstance(instance, plsql_declaration_VariableDeclaration)



@given(instance=plsql_declaration_VariableDeclaration_strategy)
def test_plsql_declaration_variabledeclaration_constant_setter(instance):
    original = instance.constant
    instance.constant = original
    assert instance.constant == original



@given(instance=plsql_declaration_VariableDeclaration_strategy)
def test_plsql_declaration_variabledeclaration_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original



@given(instance=plsql_declaration_VariableDeclaration_strategy)
def test_plsql_declaration_variabledeclaration_notnull_setter(instance):
    original = instance.notnull
    instance.notnull = original
    assert instance.notnull == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=plsql_declaration_Declaration_strategy)
@settings(max_examples=50)
def test_plsql_declaration_declaration_instantiation(instance):
    assert isinstance(instance, plsql_declaration_Declaration)

@given(instance=plsql_declaration_Package_strategy)
@settings(max_examples=50)
def test_plsql_declaration_package_instantiation(instance):
    assert isinstance(instance, plsql_declaration_Package)

@given(instance=plsql_expression_FunctionCallParameter_strategy)
@settings(max_examples=50)
def test_plsql_expression_functioncallparameter_instantiation(instance):
    assert isinstance(instance, plsql_expression_FunctionCallParameter)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=plsql_type_GenericType_strategy)
@settings(max_examples=50)
def test_plsql_type_generictype_instantiation(instance):
    assert isinstance(instance, plsql_type_GenericType)

@given(instance=plsql_type_IndirectType_strategy)
@settings(max_examples=50)
def test_plsql_type_indirecttype_instantiation(instance):
    assert isinstance(instance, plsql_type_IndirectType)



@given(instance=plsql_type_IndirectType_strategy)
def test_plsql_type_indirecttype_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original



@given(instance=plsql_type_IndirectType_strategy)
def test_plsql_type_indirecttype_range_setter(instance):
    original = instance.range
    instance.range = original
    assert instance.range == original



@given(instance=plsql_type_IndirectType_strategy)
def test_plsql_type_indirecttype_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=plsql_type_IndirectType_strategy)
def test_plsql_type_indirecttype_rowtype_setter(instance):
    original = instance.rowtype
    instance.rowtype = original
    assert instance.rowtype == original

@given(instance=plsql_type_Datatype_strategy)
@settings(max_examples=50)
def test_plsql_type_datatype_instantiation(instance):
    assert isinstance(instance, plsql_type_Datatype)



@given(instance=plsql_type_Datatype_strategy)
def test_plsql_type_datatype_range_setter(instance):
    original = instance.range
    instance.range = original
    assert instance.range == original



@given(instance=plsql_type_Datatype_strategy)
def test_plsql_type_datatype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=plsql_type_Type_strategy)
@settings(max_examples=50)
def test_plsql_type_type_instantiation(instance):
    assert isinstance(instance, plsql_type_Type)

@given(instance=StringOperation_strategy)
@settings(max_examples=50)
def test_stringoperation_instantiation(instance):
    assert isinstance(instance, StringOperation)

@given(instance=plsql_expression_ConcatString_strategy)
@settings(max_examples=50)
def test_plsql_expression_concatstring_instantiation(instance):
    assert isinstance(instance, plsql_expression_ConcatString)

@given(instance=plsql_statement_ExceptionSection_strategy)
@settings(max_examples=50)
def test_plsql_statement_exceptionsection_instantiation(instance):
    assert isinstance(instance, plsql_statement_ExceptionSection)



@given(instance=plsql_statement_ExceptionSection_strategy)
def test_plsql_statement_exceptionsection_exceptionNames_setter(instance):
    original = instance.exceptionNames
    instance.exceptionNames = original
    assert instance.exceptionNames == original

@given(instance=plsql_statement_UpdatePair_strategy)
@settings(max_examples=50)
def test_plsql_statement_updatepair_instantiation(instance):
    assert isinstance(instance, plsql_statement_UpdatePair)



@given(instance=plsql_statement_UpdatePair_strategy)
def test_plsql_statement_updatepair_column_setter(instance):
    original = instance.column
    instance.column = original
    assert instance.column == original

@given(instance=UpdatePair_strategy)
@settings(max_examples=50)
def test_updatepair_instantiation(instance):
    assert isinstance(instance, UpdatePair)

@given(instance=condition_SQLCondition_strategy)
@settings(max_examples=50)
def test_condition_sqlcondition_instantiation(instance):
    assert isinstance(instance, condition_SQLCondition)

@given(instance=plsql_expression_Expression_strategy)
@settings(max_examples=50)
def test_plsql_expression_expression_instantiation(instance):
    assert isinstance(instance, plsql_expression_Expression)

@given(instance=SQLCondition_strategy)
@settings(max_examples=50)
def test_sqlcondition_instantiation(instance):
    assert isinstance(instance, SQLCondition)

@given(instance=plsql_condition_BooleanCondition_strategy)
@settings(max_examples=50)
def test_plsql_condition_booleancondition_instantiation(instance):
    assert isinstance(instance, plsql_condition_BooleanCondition)



@given(instance=plsql_condition_BooleanCondition_strategy)
def test_plsql_condition_booleancondition_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=plsql_condition_ConditionComparison_strategy)
@settings(max_examples=50)
def test_plsql_condition_conditioncomparison_instantiation(instance):
    assert isinstance(instance, plsql_condition_ConditionComparison)



@given(instance=plsql_condition_ConditionComparison_strategy)
def test_plsql_condition_conditioncomparison_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=plsql_condition_NotCondition_strategy)
@settings(max_examples=50)
def test_plsql_condition_notcondition_instantiation(instance):
    assert isinstance(instance, plsql_condition_NotCondition)

@given(instance=ModifySQLStatement_strategy)
@settings(max_examples=50)
def test_modifysqlstatement_instantiation(instance):
    assert isinstance(instance, ModifySQLStatement)

@given(instance=plsql_statement_UpdateStatement_strategy)
@settings(max_examples=50)
def test_plsql_statement_updatestatement_instantiation(instance):
    assert isinstance(instance, plsql_statement_UpdateStatement)



@given(instance=plsql_statement_UpdateStatement_strategy)
def test_plsql_statement_updatestatement_table_setter(instance):
    original = instance.table
    instance.table = original
    assert instance.table == original

@given(instance=plsql_statement_DeleteStatement_strategy)
@settings(max_examples=50)
def test_plsql_statement_deletestatement_instantiation(instance):
    assert isinstance(instance, plsql_statement_DeleteStatement)

@given(instance=plsql_statement_SetTransactionStatement_strategy)
@settings(max_examples=50)
def test_plsql_statement_settransactionstatement_instantiation(instance):
    assert isinstance(instance, plsql_statement_SetTransactionStatement)

@given(instance=plsql_statement_InsertStatement_strategy)
@settings(max_examples=50)
def test_plsql_statement_insertstatement_instantiation(instance):
    assert isinstance(instance, plsql_statement_InsertStatement)



@given(instance=plsql_statement_InsertStatement_strategy)
def test_plsql_statement_insertstatement_columns_setter(instance):
    original = instance.columns
    instance.columns = original
    assert instance.columns == original



@given(instance=plsql_statement_InsertStatement_strategy)
def test_plsql_statement_insertstatement_into_setter(instance):
    original = instance.into
    instance.into = original
    assert instance.into == original

@given(instance=plsql_statement_SelectStatement_strategy)
@settings(max_examples=50)
def test_plsql_statement_selectstatement_instantiation(instance):
    assert isinstance(instance, plsql_statement_SelectStatement)



@given(instance=plsql_statement_SelectStatement_strategy)
def test_plsql_statement_selectstatement_collect_setter(instance):
    original = instance.collect
    instance.collect = original
    assert instance.collect == original



@given(instance=plsql_statement_SelectStatement_strategy)
def test_plsql_statement_selectstatement_unique_setter(instance):
    original = instance.unique
    instance.unique = original
    assert instance.unique == original



@given(instance=plsql_statement_SelectStatement_strategy)
def test_plsql_statement_selectstatement_all_setter(instance):
    original = instance.all
    instance.all = original
    assert instance.all == original



@given(instance=plsql_statement_SelectStatement_strategy)
def test_plsql_statement_selectstatement_from__setter(instance):
    original = instance.from_
    instance.from_ = original
    assert instance.from_ == original



@given(instance=plsql_statement_SelectStatement_strategy)
def test_plsql_statement_selectstatement_selectList_setter(instance):
    original = instance.selectList
    instance.selectList = original
    assert instance.selectList == original



@given(instance=plsql_statement_SelectStatement_strategy)
def test_plsql_statement_selectstatement_distinct_setter(instance):
    original = instance.distinct
    instance.distinct = original
    assert instance.distinct == original



@given(instance=plsql_statement_SelectStatement_strategy)
def test_plsql_statement_selectstatement_isCount_setter(instance):
    original = instance.isCount
    instance.isCount = original
    assert instance.isCount == original



@given(instance=plsql_statement_SelectStatement_strategy)
def test_plsql_statement_selectstatement_bulk_setter(instance):
    original = instance.bulk
    instance.bulk = original
    assert instance.bulk == original

@given(instance=ExceptionSection_strategy)
@settings(max_examples=50)
def test_exceptionsection_instantiation(instance):
    assert isinstance(instance, ExceptionSection)

@given(instance=Declaration_strategy)
@settings(max_examples=50)
def test_declaration_instantiation(instance):
    assert isinstance(instance, Declaration)

@given(instance=plsql_declaration_CursorDeclaration_strategy)
@settings(max_examples=50)
def test_plsql_declaration_cursordeclaration_instantiation(instance):
    assert isinstance(instance, plsql_declaration_CursorDeclaration)

@given(instance=plsql_declaration_ProcedureDeclaration_strategy)
@settings(max_examples=50)
def test_plsql_declaration_proceduredeclaration_instantiation(instance):
    assert isinstance(instance, plsql_declaration_ProcedureDeclaration)

@given(instance=VariableDeclaration_strategy)
@settings(max_examples=50)
def test_variabledeclaration_instantiation(instance):
    assert isinstance(instance, VariableDeclaration)

@given(instance=LoopStatement_strategy)
@settings(max_examples=50)
def test_loopstatement_instantiation(instance):
    assert isinstance(instance, LoopStatement)

@given(instance=plsql_statement_ForStatement_strategy)
@settings(max_examples=50)
def test_plsql_statement_forstatement_instantiation(instance):
    assert isinstance(instance, plsql_statement_ForStatement)

@given(instance=VarRefExpression_strategy)
@settings(max_examples=50)
def test_varrefexpression_instantiation(instance):
    assert isinstance(instance, VarRefExpression)

@given(instance=plsql_expression_SQLCursor_strategy)
@settings(max_examples=50)
def test_plsql_expression_sqlcursor_instantiation(instance):
    assert isinstance(instance, plsql_expression_SQLCursor)

@given(instance=plsql_expression_SQLVariable_strategy)
@settings(max_examples=50)
def test_plsql_expression_sqlvariable_instantiation(instance):
    assert isinstance(instance, plsql_expression_SQLVariable)

@given(instance=plsql_expression_FormsVarRef_strategy)
@settings(max_examples=50)
def test_plsql_expression_formsvarref_instantiation(instance):
    assert isinstance(instance, plsql_expression_FormsVarRef)



@given(instance=plsql_expression_FormsVarRef_strategy)
def test_plsql_expression_formsvarref_reference_setter(instance):
    original = instance.reference
    instance.reference = original
    assert instance.reference == original

@given(instance=CursorDeclaration_strategy)
@settings(max_examples=50)
def test_cursordeclaration_instantiation(instance):
    assert isinstance(instance, CursorDeclaration)

@given(instance=ControlSQLStatement_strategy)
@settings(max_examples=50)
def test_controlsqlstatement_instantiation(instance):
    assert isinstance(instance, ControlSQLStatement)

@given(instance=plsql_statement_LockTableStatement_strategy)
@settings(max_examples=50)
def test_plsql_statement_locktablestatement_instantiation(instance):
    assert isinstance(instance, plsql_statement_LockTableStatement)

@given(instance=plsql_statement_CommitStatement_strategy)
@settings(max_examples=50)
def test_plsql_statement_commitstatement_instantiation(instance):
    assert isinstance(instance, plsql_statement_CommitStatement)

@given(instance=plsql_statement_FetchStatement_strategy)
@settings(max_examples=50)
def test_plsql_statement_fetchstatement_instantiation(instance):
    assert isinstance(instance, plsql_statement_FetchStatement)

@given(instance=plsql_statement_SavepointStatement_strategy)
@settings(max_examples=50)
def test_plsql_statement_savepointstatement_instantiation(instance):
    assert isinstance(instance, plsql_statement_SavepointStatement)

@given(instance=plsql_statement_RollbackStatement_strategy)
@settings(max_examples=50)
def test_plsql_statement_rollbackstatement_instantiation(instance):
    assert isinstance(instance, plsql_statement_RollbackStatement)

@given(instance=plsql_statement_OpenStatement_strategy)
@settings(max_examples=50)
def test_plsql_statement_openstatement_instantiation(instance):
    assert isinstance(instance, plsql_statement_OpenStatement)

@given(instance=plsql_statement_CloseStatement_strategy)
@settings(max_examples=50)
def test_plsql_statement_closestatement_instantiation(instance):
    assert isinstance(instance, plsql_statement_CloseStatement)

@given(instance=SQLStatement_strategy)
@settings(max_examples=50)
def test_sqlstatement_instantiation(instance):
    assert isinstance(instance, SQLStatement)

@given(instance=plsql_statement_ModifySQLStatement_strategy)
@settings(max_examples=50)
def test_plsql_statement_modifysqlstatement_instantiation(instance):
    assert isinstance(instance, plsql_statement_ModifySQLStatement)

@given(instance=plsql_statement_ControlSQLStatement_strategy)
@settings(max_examples=50)
def test_plsql_statement_controlsqlstatement_instantiation(instance):
    assert isinstance(instance, plsql_statement_ControlSQLStatement)

@given(instance=FunctionCallParameter_strategy)
@settings(max_examples=50)
def test_functioncallparameter_instantiation(instance):
    assert isinstance(instance, FunctionCallParameter)

@given(instance=expression_Expression_strategy)
@settings(max_examples=50)
def test_expression_expression_instantiation(instance):
    assert isinstance(instance, expression_Expression)

@given(instance=plsql_expression_BooleanExpression_strategy)
@settings(max_examples=50)
def test_plsql_expression_booleanexpression_instantiation(instance):
    assert isinstance(instance, plsql_expression_BooleanExpression)



@given(instance=plsql_expression_BooleanExpression_strategy)
def test_plsql_expression_booleanexpression_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=plsql_statement_NullStatement_strategy)
@settings(max_examples=50)
def test_plsql_statement_nullstatement_instantiation(instance):
    assert isinstance(instance, plsql_statement_NullStatement)

@given(instance=plsql_statement_ReturnStatement_strategy)
@settings(max_examples=50)
def test_plsql_statement_returnstatement_instantiation(instance):
    assert isinstance(instance, plsql_statement_ReturnStatement)

@given(instance=plsql_statement_RaiseStatement_strategy)
@settings(max_examples=50)
def test_plsql_statement_raisestatement_instantiation(instance):
    assert isinstance(instance, plsql_statement_RaiseStatement)



@given(instance=plsql_statement_RaiseStatement_strategy)
def test_plsql_statement_raisestatement_exception_setter(instance):
    original = instance.exception
    instance.exception = original
    assert instance.exception == original

@given(instance=plsql_statement_SQLStatement_strategy)
@settings(max_examples=50)
def test_plsql_statement_sqlstatement_instantiation(instance):
    assert isinstance(instance, plsql_statement_SQLStatement)

@given(instance=plsql_statement_BlockStatement_strategy)
@settings(max_examples=50)
def test_plsql_statement_blockstatement_instantiation(instance):
    assert isinstance(instance, plsql_statement_BlockStatement)

@given(instance=plsql_statement_AssignmentStatement_strategy)
@settings(max_examples=50)
def test_plsql_statement_assignmentstatement_instantiation(instance):
    assert isinstance(instance, plsql_statement_AssignmentStatement)

@given(instance=plsql_statement_Statement_strategy)
@settings(max_examples=50)
def test_plsql_statement_statement_instantiation(instance):
    assert isinstance(instance, plsql_statement_Statement)

@given(instance=plsql_statement_LoopStatement_strategy)
@settings(max_examples=50)
def test_plsql_statement_loopstatement_instantiation(instance):
    assert isinstance(instance, plsql_statement_LoopStatement)

@given(instance=IfStatement_strategy)
@settings(max_examples=50)
def test_ifstatement_instantiation(instance):
    assert isinstance(instance, IfStatement)

@given(instance=plsql_statement_IfStatement_strategy)
@settings(max_examples=50)
def test_plsql_statement_ifstatement_instantiation(instance):
    assert isinstance(instance, plsql_statement_IfStatement)

@given(instance=plsql_statement_CaseStatement_strategy)
@settings(max_examples=50)
def test_plsql_statement_casestatement_instantiation(instance):
    assert isinstance(instance, plsql_statement_CaseStatement)

@given(instance=declaration_NamedElement_strategy)
@settings(max_examples=50)
def test_declaration_namedelement_instantiation(instance):
    assert isinstance(instance, declaration_NamedElement)

@given(instance=plsql_declaration_Argument_strategy)
@settings(max_examples=50)
def test_plsql_declaration_argument_instantiation(instance):
    assert isinstance(instance, plsql_declaration_Argument)



@given(instance=plsql_declaration_Argument_strategy)
def test_plsql_declaration_argument_out_setter(instance):
    original = instance.out
    instance.out = original
    assert instance.out == original



@given(instance=plsql_declaration_Argument_strategy)
def test_plsql_declaration_argument_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original



@given(instance=plsql_declaration_Argument_strategy)
def test_plsql_declaration_argument_in__setter(instance):
    original = instance.in_
    instance.in_ = original
    assert instance.in_ == original

@given(instance=plsql_declaration_TriggerBlock_strategy)
@settings(max_examples=50)
def test_plsql_declaration_triggerblock_instantiation(instance):
    assert isinstance(instance, plsql_declaration_TriggerBlock)

@given(instance=statement_Statement_strategy)
@settings(max_examples=50)
def test_statement_statement_instantiation(instance):
    assert isinstance(instance, statement_Statement)

@given(instance=plsql_statement_FunctionCallStatement_strategy)
@settings(max_examples=50)
def test_plsql_statement_functioncallstatement_instantiation(instance):
    assert isinstance(instance, plsql_statement_FunctionCallStatement)

@given(instance=plsql_statement_GotoStatement_strategy)
@settings(max_examples=50)
def test_plsql_statement_gotostatement_instantiation(instance):
    assert isinstance(instance, plsql_statement_GotoStatement)

@given(instance=plsql_statement_ExitStatement_strategy)
@settings(max_examples=50)
def test_plsql_statement_exitstatement_instantiation(instance):
    assert isinstance(instance, plsql_statement_ExitStatement)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=plsql_expression_PropertyAccess_strategy)
@settings(max_examples=50)
def test_plsql_expression_propertyaccess_instantiation(instance):
    assert isinstance(instance, plsql_expression_PropertyAccess)



@given(instance=plsql_expression_PropertyAccess_strategy)
def test_plsql_expression_propertyaccess_propertyName_setter(instance):
    original = instance.propertyName
    instance.propertyName = original
    assert instance.propertyName == original

@given(instance=plsql_expression_VarRefExpression_strategy)
@settings(max_examples=50)
def test_plsql_expression_varrefexpression_instantiation(instance):
    assert isinstance(instance, plsql_expression_VarRefExpression)

@given(instance=plsql_expression_InRangeExpression_strategy)
@settings(max_examples=50)
def test_plsql_expression_inrangeexpression_instantiation(instance):
    assert isinstance(instance, plsql_expression_InRangeExpression)

@given(instance=plsql_expression_ArithmeticExpression_strategy)
@settings(max_examples=50)
def test_plsql_expression_arithmeticexpression_instantiation(instance):
    assert isinstance(instance, plsql_expression_ArithmeticExpression)



@given(instance=plsql_expression_ArithmeticExpression_strategy)
def test_plsql_expression_arithmeticexpression_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=plsql_expression_LiteralExpression_strategy)
@settings(max_examples=50)
def test_plsql_expression_literalexpression_instantiation(instance):
    assert isinstance(instance, plsql_expression_LiteralExpression)



@given(instance=plsql_expression_LiteralExpression_strategy)
def test_plsql_expression_literalexpression_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=plsql_expression_LiteralExpression_strategy)
def test_plsql_expression_literalexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=plsql_expression_LikeExpression_strategy)
@settings(max_examples=50)
def test_plsql_expression_likeexpression_instantiation(instance):
    assert isinstance(instance, plsql_expression_LikeExpression)

@given(instance=plsql_expression_NotExpression_strategy)
@settings(max_examples=50)
def test_plsql_expression_notexpression_instantiation(instance):
    assert isinstance(instance, plsql_expression_NotExpression)

@given(instance=plsql_expression_StringOperation_strategy)
@settings(max_examples=50)
def test_plsql_expression_stringoperation_instantiation(instance):
    assert isinstance(instance, plsql_expression_StringOperation)

@given(instance=plsql_expression_IsNullExpression_strategy)
@settings(max_examples=50)
def test_plsql_expression_isnullexpression_instantiation(instance):
    assert isinstance(instance, plsql_expression_IsNullExpression)

@given(instance=plsql_expression_FoundExpression_strategy)
@settings(max_examples=50)
def test_plsql_expression_foundexpression_instantiation(instance):
    assert isinstance(instance, plsql_expression_FoundExpression)
