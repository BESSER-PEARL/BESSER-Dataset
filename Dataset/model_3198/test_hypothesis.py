import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    plsql::declaration::NamedElement,
    TriggerBlock,
    plsql::declaration::PLSQLDefinition,
    statement::BlockStatement,
    SelectStatement,
    Argument,
    type::TypedElement,
    declaration::Declaration,
    plsql::declaration::FunctionDeclaration,
    plsql::declaration::VariableDeclaration,
    plsql::condition::SQLCondition,
    plsql::type::TypedElement,
    StringOperation,
    plsql::expression::ConcatString,
    NamedElement,
    plsql::declaration::Declaration,
    plsql::declaration::Package,
    plsql::expression::FunctionCallParameter,
    Type,
    plsql::type::IndirectType,
    plsql::type::GenericType,
    plsql::type::Datatype,
    plsql::type::Type,
    SQLCondition,
    plsql::condition::BooleanCondition,
    plsql::condition::ConditionComparison,
    plsql::condition::NotCondition,
    condition::SQLCondition,
    plsql::expression::Expression,
    plsql::statement::ExceptionSection,
    plsql::statement::UpdatePair,
    UpdatePair,
    ExceptionSection,
    Declaration,
    plsql::declaration::CursorDeclaration,
    plsql::declaration::ProcedureDeclaration,
    ModifySQLStatement,
    plsql::statement::UpdateStatement,
    plsql::statement::SetTransactionStatement,
    plsql::statement::DeleteStatement,
    plsql::statement::InsertStatement,
    plsql::statement::SelectStatement,
    VarRefExpression,
    plsql::expression::SQLVariable,
    plsql::expression::FormsVarRef,
    plsql::expression::SQLCursor,
    CursorDeclaration,
    ControlSQLStatement,
    plsql::statement::SavepointStatement,
    plsql::statement::FetchStatement,
    plsql::statement::OpenStatement,
    plsql::statement::CommitStatement,
    plsql::statement::LockTableStatement,
    plsql::statement::RollbackStatement,
    plsql::statement::CloseStatement,
    SQLStatement,
    plsql::statement::ModifySQLStatement,
    plsql::statement::ControlSQLStatement,
    FunctionCallParameter,
    expression::Expression,
    plsql::expression::BooleanExpression,
    declaration::NamedElement,
    plsql::declaration::Argument,
    plsql::declaration::TriggerBlock,
    statement::Statement,
    plsql::statement::FunctionCallStatement,
    plsql::statement::GotoStatement,
    Expression,
    plsql::expression::VarRefExpression,
    plsql::expression::LikeExpression,
    plsql::expression::IsNullExpression,
    plsql::expression::LiteralExpression,
    plsql::expression::StringOperation,
    plsql::expression::PropertyAccess,
    plsql::expression::ArithmeticExpression,
    plsql::expression::InRangeExpression,
    plsql::expression::FoundExpression,
    plsql::expression::NotExpression,
    Statement,
    plsql::statement::ExitStatement,
    plsql::statement::BlockStatement,
    plsql::statement::ReturnStatement,
    plsql::statement::SQLStatement,
    plsql::statement::AssignmentStatement,
    plsql::statement::Statement,
    plsql::statement::RaiseStatement,
    plsql::statement::NullStatement,
    VariableDeclaration,
    LoopStatement,
    plsql::statement::ForStatement,
    plsql::statement::LoopStatement,
    IfStatement,
    plsql::statement::IfStatement,
    plsql::statement::CaseStatement,
    ArithmeticOperatorType,
    LiteralExpressionType,
    BasicTypes,
    BooleanOperatorType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_plsql::declaration::namedelement_is_not_abstract():
    assert not inspect.isabstract(plsql::declaration::NamedElement)


def test_plsql::declaration::namedelement_constructor_exists():
    assert callable(plsql::declaration::NamedElement.__init__)


def test_plsql::declaration::namedelement_constructor_args():
    sig = inspect.signature(plsql::declaration::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_plsql::declaration::namedelement_has_name():
    assert hasattr(plsql::declaration::NamedElement, "name")
    descriptor = None
    for klass in plsql::declaration::NamedElement.__mro__:
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



def test_plsql::declaration::plsqldefinition_is_not_abstract():
    assert not inspect.isabstract(plsql::declaration::PLSQLDefinition)


def test_plsql::declaration::plsqldefinition_constructor_exists():
    assert callable(plsql::declaration::PLSQLDefinition.__init__)


def test_plsql::declaration::plsqldefinition_constructor_args():
    sig = inspect.signature(plsql::declaration::PLSQLDefinition.__init__)
    params = list(sig.parameters.keys())



def test_statement::blockstatement_is_not_abstract():
    assert not inspect.isabstract(statement::BlockStatement)


def test_statement::blockstatement_constructor_exists():
    assert callable(statement::BlockStatement.__init__)


def test_statement::blockstatement_constructor_args():
    sig = inspect.signature(statement::BlockStatement.__init__)
    params = list(sig.parameters.keys())



def test_selectstatement_is_not_abstract():
    assert not inspect.isabstract(SelectStatement)


def test_selectstatement_constructor_exists():
    assert callable(SelectStatement.__init__)


def test_selectstatement_constructor_args():
    sig = inspect.signature(SelectStatement.__init__)
    params = list(sig.parameters.keys())



def test_argument_is_not_abstract():
    assert not inspect.isabstract(Argument)


def test_argument_constructor_exists():
    assert callable(Argument.__init__)


def test_argument_constructor_args():
    sig = inspect.signature(Argument.__init__)
    params = list(sig.parameters.keys())



def test_type::typedelement_is_not_abstract():
    assert not inspect.isabstract(type::TypedElement)


def test_type::typedelement_constructor_exists():
    assert callable(type::TypedElement.__init__)


def test_type::typedelement_constructor_args():
    sig = inspect.signature(type::TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_declaration::declaration_is_not_abstract():
    assert not inspect.isabstract(declaration::Declaration)


def test_declaration::declaration_constructor_exists():
    assert callable(declaration::Declaration.__init__)


def test_declaration::declaration_constructor_args():
    sig = inspect.signature(declaration::Declaration.__init__)
    params = list(sig.parameters.keys())



def test_plsql::declaration::functiondeclaration_is_not_abstract():
    assert not inspect.isabstract(plsql::declaration::FunctionDeclaration)


def test_plsql::declaration::functiondeclaration_constructor_exists():
    assert callable(plsql::declaration::FunctionDeclaration.__init__)


def test_plsql::declaration::functiondeclaration_constructor_args():
    sig = inspect.signature(plsql::declaration::FunctionDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_plsql::declaration::variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(plsql::declaration::VariableDeclaration)


def test_plsql::declaration::variabledeclaration_constructor_exists():
    assert callable(plsql::declaration::VariableDeclaration.__init__)


def test_plsql::declaration::variabledeclaration_constructor_args():
    sig = inspect.signature(plsql::declaration::VariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "notnull" in params, "Missing parameter 'notnull'"
    assert "default" in params, "Missing parameter 'default'"
    assert "constant" in params, "Missing parameter 'constant'"

def test_plsql::declaration::variabledeclaration_has_notnull():
    assert hasattr(plsql::declaration::VariableDeclaration, "notnull")
    descriptor = None
    for klass in plsql::declaration::VariableDeclaration.__mro__:
        if "notnull" in klass.__dict__:
            descriptor = klass.__dict__["notnull"]
            break
    assert isinstance(descriptor, property)

def test_plsql::declaration::variabledeclaration_has_default():
    assert hasattr(plsql::declaration::VariableDeclaration, "default")
    descriptor = None
    for klass in plsql::declaration::VariableDeclaration.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)

def test_plsql::declaration::variabledeclaration_has_constant():
    assert hasattr(plsql::declaration::VariableDeclaration, "constant")
    descriptor = None
    for klass in plsql::declaration::VariableDeclaration.__mro__:
        if "constant" in klass.__dict__:
            descriptor = klass.__dict__["constant"]
            break
    assert isinstance(descriptor, property)



def test_plsql::condition::sqlcondition_is_not_abstract():
    assert not inspect.isabstract(plsql::condition::SQLCondition)


def test_plsql::condition::sqlcondition_constructor_exists():
    assert callable(plsql::condition::SQLCondition.__init__)


def test_plsql::condition::sqlcondition_constructor_args():
    sig = inspect.signature(plsql::condition::SQLCondition.__init__)
    params = list(sig.parameters.keys())



def test_plsql::type::typedelement_is_not_abstract():
    assert not inspect.isabstract(plsql::type::TypedElement)


def test_plsql::type::typedelement_constructor_exists():
    assert callable(plsql::type::TypedElement.__init__)


def test_plsql::type::typedelement_constructor_args():
    sig = inspect.signature(plsql::type::TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_stringoperation_is_not_abstract():
    assert not inspect.isabstract(StringOperation)


def test_stringoperation_constructor_exists():
    assert callable(StringOperation.__init__)


def test_stringoperation_constructor_args():
    sig = inspect.signature(StringOperation.__init__)
    params = list(sig.parameters.keys())



def test_plsql::expression::concatstring_is_not_abstract():
    assert not inspect.isabstract(plsql::expression::ConcatString)


def test_plsql::expression::concatstring_constructor_exists():
    assert callable(plsql::expression::ConcatString.__init__)


def test_plsql::expression::concatstring_constructor_args():
    sig = inspect.signature(plsql::expression::ConcatString.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_plsql::declaration::declaration_is_not_abstract():
    assert not inspect.isabstract(plsql::declaration::Declaration)


def test_plsql::declaration::declaration_constructor_exists():
    assert callable(plsql::declaration::Declaration.__init__)


def test_plsql::declaration::declaration_constructor_args():
    sig = inspect.signature(plsql::declaration::Declaration.__init__)
    params = list(sig.parameters.keys())



def test_plsql::declaration::package_is_not_abstract():
    assert not inspect.isabstract(plsql::declaration::Package)


def test_plsql::declaration::package_constructor_exists():
    assert callable(plsql::declaration::Package.__init__)


def test_plsql::declaration::package_constructor_args():
    sig = inspect.signature(plsql::declaration::Package.__init__)
    params = list(sig.parameters.keys())



def test_plsql::expression::functioncallparameter_is_not_abstract():
    assert not inspect.isabstract(plsql::expression::FunctionCallParameter)


def test_plsql::expression::functioncallparameter_constructor_exists():
    assert callable(plsql::expression::FunctionCallParameter.__init__)


def test_plsql::expression::functioncallparameter_constructor_args():
    sig = inspect.signature(plsql::expression::FunctionCallParameter.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_plsql::type::indirecttype_is_not_abstract():
    assert not inspect.isabstract(plsql::type::IndirectType)


def test_plsql::type::indirecttype_constructor_exists():
    assert callable(plsql::type::IndirectType.__init__)


def test_plsql::type::indirecttype_constructor_args():
    sig = inspect.signature(plsql::type::IndirectType.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"
    assert "rowtype" in params, "Missing parameter 'rowtype'"
    assert "range" in params, "Missing parameter 'range'"
    assert "type" in params, "Missing parameter 'type'"

def test_plsql::type::indirecttype_has_identifier():
    assert hasattr(plsql::type::IndirectType, "identifier")
    descriptor = None
    for klass in plsql::type::IndirectType.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)

def test_plsql::type::indirecttype_has_rowtype():
    assert hasattr(plsql::type::IndirectType, "rowtype")
    descriptor = None
    for klass in plsql::type::IndirectType.__mro__:
        if "rowtype" in klass.__dict__:
            descriptor = klass.__dict__["rowtype"]
            break
    assert isinstance(descriptor, property)

def test_plsql::type::indirecttype_has_range():
    assert hasattr(plsql::type::IndirectType, "range")
    descriptor = None
    for klass in plsql::type::IndirectType.__mro__:
        if "range" in klass.__dict__:
            descriptor = klass.__dict__["range"]
            break
    assert isinstance(descriptor, property)

def test_plsql::type::indirecttype_has_type():
    assert hasattr(plsql::type::IndirectType, "type")
    descriptor = None
    for klass in plsql::type::IndirectType.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_plsql::type::generictype_is_not_abstract():
    assert not inspect.isabstract(plsql::type::GenericType)


def test_plsql::type::generictype_constructor_exists():
    assert callable(plsql::type::GenericType.__init__)


def test_plsql::type::generictype_constructor_args():
    sig = inspect.signature(plsql::type::GenericType.__init__)
    params = list(sig.parameters.keys())



def test_plsql::type::datatype_is_not_abstract():
    assert not inspect.isabstract(plsql::type::Datatype)


def test_plsql::type::datatype_constructor_exists():
    assert callable(plsql::type::Datatype.__init__)


def test_plsql::type::datatype_constructor_args():
    sig = inspect.signature(plsql::type::Datatype.__init__)
    params = list(sig.parameters.keys())
    assert "range" in params, "Missing parameter 'range'"
    assert "name" in params, "Missing parameter 'name'"

def test_plsql::type::datatype_has_range():
    assert hasattr(plsql::type::Datatype, "range")
    descriptor = None
    for klass in plsql::type::Datatype.__mro__:
        if "range" in klass.__dict__:
            descriptor = klass.__dict__["range"]
            break
    assert isinstance(descriptor, property)

def test_plsql::type::datatype_has_name():
    assert hasattr(plsql::type::Datatype, "name")
    descriptor = None
    for klass in plsql::type::Datatype.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_plsql::type::type_is_not_abstract():
    assert not inspect.isabstract(plsql::type::Type)


def test_plsql::type::type_constructor_exists():
    assert callable(plsql::type::Type.__init__)


def test_plsql::type::type_constructor_args():
    sig = inspect.signature(plsql::type::Type.__init__)
    params = list(sig.parameters.keys())



def test_sqlcondition_is_not_abstract():
    assert not inspect.isabstract(SQLCondition)


def test_sqlcondition_constructor_exists():
    assert callable(SQLCondition.__init__)


def test_sqlcondition_constructor_args():
    sig = inspect.signature(SQLCondition.__init__)
    params = list(sig.parameters.keys())



def test_plsql::condition::booleancondition_is_not_abstract():
    assert not inspect.isabstract(plsql::condition::BooleanCondition)


def test_plsql::condition::booleancondition_constructor_exists():
    assert callable(plsql::condition::BooleanCondition.__init__)


def test_plsql::condition::booleancondition_constructor_args():
    sig = inspect.signature(plsql::condition::BooleanCondition.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_plsql::condition::booleancondition_has_type():
    assert hasattr(plsql::condition::BooleanCondition, "type")
    descriptor = None
    for klass in plsql::condition::BooleanCondition.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_plsql::condition::conditioncomparison_is_not_abstract():
    assert not inspect.isabstract(plsql::condition::ConditionComparison)


def test_plsql::condition::conditioncomparison_constructor_exists():
    assert callable(plsql::condition::ConditionComparison.__init__)


def test_plsql::condition::conditioncomparison_constructor_args():
    sig = inspect.signature(plsql::condition::ConditionComparison.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_plsql::condition::conditioncomparison_has_type():
    assert hasattr(plsql::condition::ConditionComparison, "type")
    descriptor = None
    for klass in plsql::condition::ConditionComparison.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_plsql::condition::notcondition_is_not_abstract():
    assert not inspect.isabstract(plsql::condition::NotCondition)


def test_plsql::condition::notcondition_constructor_exists():
    assert callable(plsql::condition::NotCondition.__init__)


def test_plsql::condition::notcondition_constructor_args():
    sig = inspect.signature(plsql::condition::NotCondition.__init__)
    params = list(sig.parameters.keys())



def test_condition::sqlcondition_is_not_abstract():
    assert not inspect.isabstract(condition::SQLCondition)


def test_condition::sqlcondition_constructor_exists():
    assert callable(condition::SQLCondition.__init__)


def test_condition::sqlcondition_constructor_args():
    sig = inspect.signature(condition::SQLCondition.__init__)
    params = list(sig.parameters.keys())



def test_plsql::expression::expression_is_not_abstract():
    assert not inspect.isabstract(plsql::expression::Expression)


def test_plsql::expression::expression_constructor_exists():
    assert callable(plsql::expression::Expression.__init__)


def test_plsql::expression::expression_constructor_args():
    sig = inspect.signature(plsql::expression::Expression.__init__)
    params = list(sig.parameters.keys())



def test_plsql::statement::exceptionsection_is_not_abstract():
    assert not inspect.isabstract(plsql::statement::ExceptionSection)


def test_plsql::statement::exceptionsection_constructor_exists():
    assert callable(plsql::statement::ExceptionSection.__init__)


def test_plsql::statement::exceptionsection_constructor_args():
    sig = inspect.signature(plsql::statement::ExceptionSection.__init__)
    params = list(sig.parameters.keys())
    assert "exceptionNames" in params, "Missing parameter 'exceptionNames'"

def test_plsql::statement::exceptionsection_has_exceptionNames():
    assert hasattr(plsql::statement::ExceptionSection, "exceptionNames")
    descriptor = None
    for klass in plsql::statement::ExceptionSection.__mro__:
        if "exceptionNames" in klass.__dict__:
            descriptor = klass.__dict__["exceptionNames"]
            break
    assert isinstance(descriptor, property)



def test_plsql::statement::updatepair_is_not_abstract():
    assert not inspect.isabstract(plsql::statement::UpdatePair)


def test_plsql::statement::updatepair_constructor_exists():
    assert callable(plsql::statement::UpdatePair.__init__)


def test_plsql::statement::updatepair_constructor_args():
    sig = inspect.signature(plsql::statement::UpdatePair.__init__)
    params = list(sig.parameters.keys())
    assert "column" in params, "Missing parameter 'column'"

def test_plsql::statement::updatepair_has_column():
    assert hasattr(plsql::statement::UpdatePair, "column")
    descriptor = None
    for klass in plsql::statement::UpdatePair.__mro__:
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



def test_plsql::declaration::cursordeclaration_is_not_abstract():
    assert not inspect.isabstract(plsql::declaration::CursorDeclaration)


def test_plsql::declaration::cursordeclaration_constructor_exists():
    assert callable(plsql::declaration::CursorDeclaration.__init__)


def test_plsql::declaration::cursordeclaration_constructor_args():
    sig = inspect.signature(plsql::declaration::CursorDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_plsql::declaration::proceduredeclaration_is_not_abstract():
    assert not inspect.isabstract(plsql::declaration::ProcedureDeclaration)


def test_plsql::declaration::proceduredeclaration_constructor_exists():
    assert callable(plsql::declaration::ProcedureDeclaration.__init__)


def test_plsql::declaration::proceduredeclaration_constructor_args():
    sig = inspect.signature(plsql::declaration::ProcedureDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_modifysqlstatement_is_not_abstract():
    assert not inspect.isabstract(ModifySQLStatement)


def test_modifysqlstatement_constructor_exists():
    assert callable(ModifySQLStatement.__init__)


def test_modifysqlstatement_constructor_args():
    sig = inspect.signature(ModifySQLStatement.__init__)
    params = list(sig.parameters.keys())



def test_plsql::statement::updatestatement_is_not_abstract():
    assert not inspect.isabstract(plsql::statement::UpdateStatement)


def test_plsql::statement::updatestatement_constructor_exists():
    assert callable(plsql::statement::UpdateStatement.__init__)


def test_plsql::statement::updatestatement_constructor_args():
    sig = inspect.signature(plsql::statement::UpdateStatement.__init__)
    params = list(sig.parameters.keys())
    assert "table" in params, "Missing parameter 'table'"

def test_plsql::statement::updatestatement_has_table():
    assert hasattr(plsql::statement::UpdateStatement, "table")
    descriptor = None
    for klass in plsql::statement::UpdateStatement.__mro__:
        if "table" in klass.__dict__:
            descriptor = klass.__dict__["table"]
            break
    assert isinstance(descriptor, property)



def test_plsql::statement::settransactionstatement_is_not_abstract():
    assert not inspect.isabstract(plsql::statement::SetTransactionStatement)


def test_plsql::statement::settransactionstatement_constructor_exists():
    assert callable(plsql::statement::SetTransactionStatement.__init__)


def test_plsql::statement::settransactionstatement_constructor_args():
    sig = inspect.signature(plsql::statement::SetTransactionStatement.__init__)
    params = list(sig.parameters.keys())



def test_plsql::statement::deletestatement_is_not_abstract():
    assert not inspect.isabstract(plsql::statement::DeleteStatement)


def test_plsql::statement::deletestatement_constructor_exists():
    assert callable(plsql::statement::DeleteStatement.__init__)


def test_plsql::statement::deletestatement_constructor_args():
    sig = inspect.signature(plsql::statement::DeleteStatement.__init__)
    params = list(sig.parameters.keys())



def test_plsql::statement::insertstatement_is_not_abstract():
    assert not inspect.isabstract(plsql::statement::InsertStatement)


def test_plsql::statement::insertstatement_constructor_exists():
    assert callable(plsql::statement::InsertStatement.__init__)


def test_plsql::statement::insertstatement_constructor_args():
    sig = inspect.signature(plsql::statement::InsertStatement.__init__)
    params = list(sig.parameters.keys())
    assert "into" in params, "Missing parameter 'into'"
    assert "columns" in params, "Missing parameter 'columns'"

def test_plsql::statement::insertstatement_has_into():
    assert hasattr(plsql::statement::InsertStatement, "into")
    descriptor = None
    for klass in plsql::statement::InsertStatement.__mro__:
        if "into" in klass.__dict__:
            descriptor = klass.__dict__["into"]
            break
    assert isinstance(descriptor, property)

def test_plsql::statement::insertstatement_has_columns():
    assert hasattr(plsql::statement::InsertStatement, "columns")
    descriptor = None
    for klass in plsql::statement::InsertStatement.__mro__:
        if "columns" in klass.__dict__:
            descriptor = klass.__dict__["columns"]
            break
    assert isinstance(descriptor, property)



def test_plsql::statement::selectstatement_is_not_abstract():
    assert not inspect.isabstract(plsql::statement::SelectStatement)


def test_plsql::statement::selectstatement_constructor_exists():
    assert callable(plsql::statement::SelectStatement.__init__)


def test_plsql::statement::selectstatement_constructor_args():
    sig = inspect.signature(plsql::statement::SelectStatement.__init__)
    params = list(sig.parameters.keys())
    assert "bulk" in params, "Missing parameter 'bulk'"
    assert "distinct" in params, "Missing parameter 'distinct'"
    assert "collect" in params, "Missing parameter 'collect'"
    assert "selectList" in params, "Missing parameter 'selectList'"
    assert "unique" in params, "Missing parameter 'unique'"
    assert "isCount" in params, "Missing parameter 'isCount'"
    assert "all" in params, "Missing parameter 'all'"
    assert "from_" in params, "Missing parameter 'from_'"

def test_plsql::statement::selectstatement_has_bulk():
    assert hasattr(plsql::statement::SelectStatement, "bulk")
    descriptor = None
    for klass in plsql::statement::SelectStatement.__mro__:
        if "bulk" in klass.__dict__:
            descriptor = klass.__dict__["bulk"]
            break
    assert isinstance(descriptor, property)

def test_plsql::statement::selectstatement_has_distinct():
    assert hasattr(plsql::statement::SelectStatement, "distinct")
    descriptor = None
    for klass in plsql::statement::SelectStatement.__mro__:
        if "distinct" in klass.__dict__:
            descriptor = klass.__dict__["distinct"]
            break
    assert isinstance(descriptor, property)

def test_plsql::statement::selectstatement_has_collect():
    assert hasattr(plsql::statement::SelectStatement, "collect")
    descriptor = None
    for klass in plsql::statement::SelectStatement.__mro__:
        if "collect" in klass.__dict__:
            descriptor = klass.__dict__["collect"]
            break
    assert isinstance(descriptor, property)

def test_plsql::statement::selectstatement_has_selectList():
    assert hasattr(plsql::statement::SelectStatement, "selectList")
    descriptor = None
    for klass in plsql::statement::SelectStatement.__mro__:
        if "selectList" in klass.__dict__:
            descriptor = klass.__dict__["selectList"]
            break
    assert isinstance(descriptor, property)

def test_plsql::statement::selectstatement_has_unique():
    assert hasattr(plsql::statement::SelectStatement, "unique")
    descriptor = None
    for klass in plsql::statement::SelectStatement.__mro__:
        if "unique" in klass.__dict__:
            descriptor = klass.__dict__["unique"]
            break
    assert isinstance(descriptor, property)

def test_plsql::statement::selectstatement_has_isCount():
    assert hasattr(plsql::statement::SelectStatement, "isCount")
    descriptor = None
    for klass in plsql::statement::SelectStatement.__mro__:
        if "isCount" in klass.__dict__:
            descriptor = klass.__dict__["isCount"]
            break
    assert isinstance(descriptor, property)

def test_plsql::statement::selectstatement_has_all():
    assert hasattr(plsql::statement::SelectStatement, "all")
    descriptor = None
    for klass in plsql::statement::SelectStatement.__mro__:
        if "all" in klass.__dict__:
            descriptor = klass.__dict__["all"]
            break
    assert isinstance(descriptor, property)

def test_plsql::statement::selectstatement_has_from_():
    assert hasattr(plsql::statement::SelectStatement, "from_")
    descriptor = None
    for klass in plsql::statement::SelectStatement.__mro__:
        if "from_" in klass.__dict__:
            descriptor = klass.__dict__["from_"]
            break
    assert isinstance(descriptor, property)



def test_varrefexpression_is_not_abstract():
    assert not inspect.isabstract(VarRefExpression)


def test_varrefexpression_constructor_exists():
    assert callable(VarRefExpression.__init__)


def test_varrefexpression_constructor_args():
    sig = inspect.signature(VarRefExpression.__init__)
    params = list(sig.parameters.keys())



def test_plsql::expression::sqlvariable_is_not_abstract():
    assert not inspect.isabstract(plsql::expression::SQLVariable)


def test_plsql::expression::sqlvariable_constructor_exists():
    assert callable(plsql::expression::SQLVariable.__init__)


def test_plsql::expression::sqlvariable_constructor_args():
    sig = inspect.signature(plsql::expression::SQLVariable.__init__)
    params = list(sig.parameters.keys())



def test_plsql::expression::formsvarref_is_not_abstract():
    assert not inspect.isabstract(plsql::expression::FormsVarRef)


def test_plsql::expression::formsvarref_constructor_exists():
    assert callable(plsql::expression::FormsVarRef.__init__)


def test_plsql::expression::formsvarref_constructor_args():
    sig = inspect.signature(plsql::expression::FormsVarRef.__init__)
    params = list(sig.parameters.keys())
    assert "reference" in params, "Missing parameter 'reference'"

def test_plsql::expression::formsvarref_has_reference():
    assert hasattr(plsql::expression::FormsVarRef, "reference")
    descriptor = None
    for klass in plsql::expression::FormsVarRef.__mro__:
        if "reference" in klass.__dict__:
            descriptor = klass.__dict__["reference"]
            break
    assert isinstance(descriptor, property)



def test_plsql::expression::sqlcursor_is_not_abstract():
    assert not inspect.isabstract(plsql::expression::SQLCursor)


def test_plsql::expression::sqlcursor_constructor_exists():
    assert callable(plsql::expression::SQLCursor.__init__)


def test_plsql::expression::sqlcursor_constructor_args():
    sig = inspect.signature(plsql::expression::SQLCursor.__init__)
    params = list(sig.parameters.keys())



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



def test_plsql::statement::savepointstatement_is_not_abstract():
    assert not inspect.isabstract(plsql::statement::SavepointStatement)


def test_plsql::statement::savepointstatement_constructor_exists():
    assert callable(plsql::statement::SavepointStatement.__init__)


def test_plsql::statement::savepointstatement_constructor_args():
    sig = inspect.signature(plsql::statement::SavepointStatement.__init__)
    params = list(sig.parameters.keys())



def test_plsql::statement::fetchstatement_is_not_abstract():
    assert not inspect.isabstract(plsql::statement::FetchStatement)


def test_plsql::statement::fetchstatement_constructor_exists():
    assert callable(plsql::statement::FetchStatement.__init__)


def test_plsql::statement::fetchstatement_constructor_args():
    sig = inspect.signature(plsql::statement::FetchStatement.__init__)
    params = list(sig.parameters.keys())



def test_plsql::statement::openstatement_is_not_abstract():
    assert not inspect.isabstract(plsql::statement::OpenStatement)


def test_plsql::statement::openstatement_constructor_exists():
    assert callable(plsql::statement::OpenStatement.__init__)


def test_plsql::statement::openstatement_constructor_args():
    sig = inspect.signature(plsql::statement::OpenStatement.__init__)
    params = list(sig.parameters.keys())



def test_plsql::statement::commitstatement_is_not_abstract():
    assert not inspect.isabstract(plsql::statement::CommitStatement)


def test_plsql::statement::commitstatement_constructor_exists():
    assert callable(plsql::statement::CommitStatement.__init__)


def test_plsql::statement::commitstatement_constructor_args():
    sig = inspect.signature(plsql::statement::CommitStatement.__init__)
    params = list(sig.parameters.keys())



def test_plsql::statement::locktablestatement_is_not_abstract():
    assert not inspect.isabstract(plsql::statement::LockTableStatement)


def test_plsql::statement::locktablestatement_constructor_exists():
    assert callable(plsql::statement::LockTableStatement.__init__)


def test_plsql::statement::locktablestatement_constructor_args():
    sig = inspect.signature(plsql::statement::LockTableStatement.__init__)
    params = list(sig.parameters.keys())



def test_plsql::statement::rollbackstatement_is_not_abstract():
    assert not inspect.isabstract(plsql::statement::RollbackStatement)


def test_plsql::statement::rollbackstatement_constructor_exists():
    assert callable(plsql::statement::RollbackStatement.__init__)


def test_plsql::statement::rollbackstatement_constructor_args():
    sig = inspect.signature(plsql::statement::RollbackStatement.__init__)
    params = list(sig.parameters.keys())



def test_plsql::statement::closestatement_is_not_abstract():
    assert not inspect.isabstract(plsql::statement::CloseStatement)


def test_plsql::statement::closestatement_constructor_exists():
    assert callable(plsql::statement::CloseStatement.__init__)


def test_plsql::statement::closestatement_constructor_args():
    sig = inspect.signature(plsql::statement::CloseStatement.__init__)
    params = list(sig.parameters.keys())



def test_sqlstatement_is_not_abstract():
    assert not inspect.isabstract(SQLStatement)


def test_sqlstatement_constructor_exists():
    assert callable(SQLStatement.__init__)


def test_sqlstatement_constructor_args():
    sig = inspect.signature(SQLStatement.__init__)
    params = list(sig.parameters.keys())



def test_plsql::statement::modifysqlstatement_is_not_abstract():
    assert not inspect.isabstract(plsql::statement::ModifySQLStatement)


def test_plsql::statement::modifysqlstatement_constructor_exists():
    assert callable(plsql::statement::ModifySQLStatement.__init__)


def test_plsql::statement::modifysqlstatement_constructor_args():
    sig = inspect.signature(plsql::statement::ModifySQLStatement.__init__)
    params = list(sig.parameters.keys())



def test_plsql::statement::controlsqlstatement_is_not_abstract():
    assert not inspect.isabstract(plsql::statement::ControlSQLStatement)


def test_plsql::statement::controlsqlstatement_constructor_exists():
    assert callable(plsql::statement::ControlSQLStatement.__init__)


def test_plsql::statement::controlsqlstatement_constructor_args():
    sig = inspect.signature(plsql::statement::ControlSQLStatement.__init__)
    params = list(sig.parameters.keys())



def test_functioncallparameter_is_not_abstract():
    assert not inspect.isabstract(FunctionCallParameter)


def test_functioncallparameter_constructor_exists():
    assert callable(FunctionCallParameter.__init__)


def test_functioncallparameter_constructor_args():
    sig = inspect.signature(FunctionCallParameter.__init__)
    params = list(sig.parameters.keys())



def test_expression::expression_is_not_abstract():
    assert not inspect.isabstract(expression::Expression)


def test_expression::expression_constructor_exists():
    assert callable(expression::Expression.__init__)


def test_expression::expression_constructor_args():
    sig = inspect.signature(expression::Expression.__init__)
    params = list(sig.parameters.keys())



def test_plsql::expression::booleanexpression_is_not_abstract():
    assert not inspect.isabstract(plsql::expression::BooleanExpression)


def test_plsql::expression::booleanexpression_constructor_exists():
    assert callable(plsql::expression::BooleanExpression.__init__)


def test_plsql::expression::booleanexpression_constructor_args():
    sig = inspect.signature(plsql::expression::BooleanExpression.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_plsql::expression::booleanexpression_has_type():
    assert hasattr(plsql::expression::BooleanExpression, "type")
    descriptor = None
    for klass in plsql::expression::BooleanExpression.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_declaration::namedelement_is_not_abstract():
    assert not inspect.isabstract(declaration::NamedElement)


def test_declaration::namedelement_constructor_exists():
    assert callable(declaration::NamedElement.__init__)


def test_declaration::namedelement_constructor_args():
    sig = inspect.signature(declaration::NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_plsql::declaration::argument_is_not_abstract():
    assert not inspect.isabstract(plsql::declaration::Argument)


def test_plsql::declaration::argument_constructor_exists():
    assert callable(plsql::declaration::Argument.__init__)


def test_plsql::declaration::argument_constructor_args():
    sig = inspect.signature(plsql::declaration::Argument.__init__)
    params = list(sig.parameters.keys())
    assert "default" in params, "Missing parameter 'default'"
    assert "in_" in params, "Missing parameter 'in_'"
    assert "out" in params, "Missing parameter 'out'"

def test_plsql::declaration::argument_has_default():
    assert hasattr(plsql::declaration::Argument, "default")
    descriptor = None
    for klass in plsql::declaration::Argument.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)

def test_plsql::declaration::argument_has_in_():
    assert hasattr(plsql::declaration::Argument, "in_")
    descriptor = None
    for klass in plsql::declaration::Argument.__mro__:
        if "in_" in klass.__dict__:
            descriptor = klass.__dict__["in_"]
            break
    assert isinstance(descriptor, property)

def test_plsql::declaration::argument_has_out():
    assert hasattr(plsql::declaration::Argument, "out")
    descriptor = None
    for klass in plsql::declaration::Argument.__mro__:
        if "out" in klass.__dict__:
            descriptor = klass.__dict__["out"]
            break
    assert isinstance(descriptor, property)



def test_plsql::declaration::triggerblock_is_not_abstract():
    assert not inspect.isabstract(plsql::declaration::TriggerBlock)


def test_plsql::declaration::triggerblock_constructor_exists():
    assert callable(plsql::declaration::TriggerBlock.__init__)


def test_plsql::declaration::triggerblock_constructor_args():
    sig = inspect.signature(plsql::declaration::TriggerBlock.__init__)
    params = list(sig.parameters.keys())



def test_statement::statement_is_not_abstract():
    assert not inspect.isabstract(statement::Statement)


def test_statement::statement_constructor_exists():
    assert callable(statement::Statement.__init__)


def test_statement::statement_constructor_args():
    sig = inspect.signature(statement::Statement.__init__)
    params = list(sig.parameters.keys())



def test_plsql::statement::functioncallstatement_is_not_abstract():
    assert not inspect.isabstract(plsql::statement::FunctionCallStatement)


def test_plsql::statement::functioncallstatement_constructor_exists():
    assert callable(plsql::statement::FunctionCallStatement.__init__)


def test_plsql::statement::functioncallstatement_constructor_args():
    sig = inspect.signature(plsql::statement::FunctionCallStatement.__init__)
    params = list(sig.parameters.keys())



def test_plsql::statement::gotostatement_is_not_abstract():
    assert not inspect.isabstract(plsql::statement::GotoStatement)


def test_plsql::statement::gotostatement_constructor_exists():
    assert callable(plsql::statement::GotoStatement.__init__)


def test_plsql::statement::gotostatement_constructor_args():
    sig = inspect.signature(plsql::statement::GotoStatement.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_plsql::expression::varrefexpression_is_not_abstract():
    assert not inspect.isabstract(plsql::expression::VarRefExpression)


def test_plsql::expression::varrefexpression_constructor_exists():
    assert callable(plsql::expression::VarRefExpression.__init__)


def test_plsql::expression::varrefexpression_constructor_args():
    sig = inspect.signature(plsql::expression::VarRefExpression.__init__)
    params = list(sig.parameters.keys())



def test_plsql::expression::likeexpression_is_not_abstract():
    assert not inspect.isabstract(plsql::expression::LikeExpression)


def test_plsql::expression::likeexpression_constructor_exists():
    assert callable(plsql::expression::LikeExpression.__init__)


def test_plsql::expression::likeexpression_constructor_args():
    sig = inspect.signature(plsql::expression::LikeExpression.__init__)
    params = list(sig.parameters.keys())



def test_plsql::expression::isnullexpression_is_not_abstract():
    assert not inspect.isabstract(plsql::expression::IsNullExpression)


def test_plsql::expression::isnullexpression_constructor_exists():
    assert callable(plsql::expression::IsNullExpression.__init__)


def test_plsql::expression::isnullexpression_constructor_args():
    sig = inspect.signature(plsql::expression::IsNullExpression.__init__)
    params = list(sig.parameters.keys())



def test_plsql::expression::literalexpression_is_not_abstract():
    assert not inspect.isabstract(plsql::expression::LiteralExpression)


def test_plsql::expression::literalexpression_constructor_exists():
    assert callable(plsql::expression::LiteralExpression.__init__)


def test_plsql::expression::literalexpression_constructor_args():
    sig = inspect.signature(plsql::expression::LiteralExpression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "type" in params, "Missing parameter 'type'"

def test_plsql::expression::literalexpression_has_value():
    assert hasattr(plsql::expression::LiteralExpression, "value")
    descriptor = None
    for klass in plsql::expression::LiteralExpression.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_plsql::expression::literalexpression_has_type():
    assert hasattr(plsql::expression::LiteralExpression, "type")
    descriptor = None
    for klass in plsql::expression::LiteralExpression.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_plsql::expression::stringoperation_is_not_abstract():
    assert not inspect.isabstract(plsql::expression::StringOperation)


def test_plsql::expression::stringoperation_constructor_exists():
    assert callable(plsql::expression::StringOperation.__init__)


def test_plsql::expression::stringoperation_constructor_args():
    sig = inspect.signature(plsql::expression::StringOperation.__init__)
    params = list(sig.parameters.keys())



def test_plsql::expression::propertyaccess_is_not_abstract():
    assert not inspect.isabstract(plsql::expression::PropertyAccess)


def test_plsql::expression::propertyaccess_constructor_exists():
    assert callable(plsql::expression::PropertyAccess.__init__)


def test_plsql::expression::propertyaccess_constructor_args():
    sig = inspect.signature(plsql::expression::PropertyAccess.__init__)
    params = list(sig.parameters.keys())
    assert "propertyName" in params, "Missing parameter 'propertyName'"

def test_plsql::expression::propertyaccess_has_propertyName():
    assert hasattr(plsql::expression::PropertyAccess, "propertyName")
    descriptor = None
    for klass in plsql::expression::PropertyAccess.__mro__:
        if "propertyName" in klass.__dict__:
            descriptor = klass.__dict__["propertyName"]
            break
    assert isinstance(descriptor, property)



def test_plsql::expression::arithmeticexpression_is_not_abstract():
    assert not inspect.isabstract(plsql::expression::ArithmeticExpression)


def test_plsql::expression::arithmeticexpression_constructor_exists():
    assert callable(plsql::expression::ArithmeticExpression.__init__)


def test_plsql::expression::arithmeticexpression_constructor_args():
    sig = inspect.signature(plsql::expression::ArithmeticExpression.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_plsql::expression::arithmeticexpression_has_type():
    assert hasattr(plsql::expression::ArithmeticExpression, "type")
    descriptor = None
    for klass in plsql::expression::ArithmeticExpression.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_plsql::expression::inrangeexpression_is_not_abstract():
    assert not inspect.isabstract(plsql::expression::InRangeExpression)


def test_plsql::expression::inrangeexpression_constructor_exists():
    assert callable(plsql::expression::InRangeExpression.__init__)


def test_plsql::expression::inrangeexpression_constructor_args():
    sig = inspect.signature(plsql::expression::InRangeExpression.__init__)
    params = list(sig.parameters.keys())



def test_plsql::expression::foundexpression_is_not_abstract():
    assert not inspect.isabstract(plsql::expression::FoundExpression)


def test_plsql::expression::foundexpression_constructor_exists():
    assert callable(plsql::expression::FoundExpression.__init__)


def test_plsql::expression::foundexpression_constructor_args():
    sig = inspect.signature(plsql::expression::FoundExpression.__init__)
    params = list(sig.parameters.keys())



def test_plsql::expression::notexpression_is_not_abstract():
    assert not inspect.isabstract(plsql::expression::NotExpression)


def test_plsql::expression::notexpression_constructor_exists():
    assert callable(plsql::expression::NotExpression.__init__)


def test_plsql::expression::notexpression_constructor_args():
    sig = inspect.signature(plsql::expression::NotExpression.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_plsql::statement::exitstatement_is_not_abstract():
    assert not inspect.isabstract(plsql::statement::ExitStatement)


def test_plsql::statement::exitstatement_constructor_exists():
    assert callable(plsql::statement::ExitStatement.__init__)


def test_plsql::statement::exitstatement_constructor_args():
    sig = inspect.signature(plsql::statement::ExitStatement.__init__)
    params = list(sig.parameters.keys())



def test_plsql::statement::blockstatement_is_not_abstract():
    assert not inspect.isabstract(plsql::statement::BlockStatement)


def test_plsql::statement::blockstatement_constructor_exists():
    assert callable(plsql::statement::BlockStatement.__init__)


def test_plsql::statement::blockstatement_constructor_args():
    sig = inspect.signature(plsql::statement::BlockStatement.__init__)
    params = list(sig.parameters.keys())



def test_plsql::statement::returnstatement_is_not_abstract():
    assert not inspect.isabstract(plsql::statement::ReturnStatement)


def test_plsql::statement::returnstatement_constructor_exists():
    assert callable(plsql::statement::ReturnStatement.__init__)


def test_plsql::statement::returnstatement_constructor_args():
    sig = inspect.signature(plsql::statement::ReturnStatement.__init__)
    params = list(sig.parameters.keys())



def test_plsql::statement::sqlstatement_is_not_abstract():
    assert not inspect.isabstract(plsql::statement::SQLStatement)


def test_plsql::statement::sqlstatement_constructor_exists():
    assert callable(plsql::statement::SQLStatement.__init__)


def test_plsql::statement::sqlstatement_constructor_args():
    sig = inspect.signature(plsql::statement::SQLStatement.__init__)
    params = list(sig.parameters.keys())



def test_plsql::statement::assignmentstatement_is_not_abstract():
    assert not inspect.isabstract(plsql::statement::AssignmentStatement)


def test_plsql::statement::assignmentstatement_constructor_exists():
    assert callable(plsql::statement::AssignmentStatement.__init__)


def test_plsql::statement::assignmentstatement_constructor_args():
    sig = inspect.signature(plsql::statement::AssignmentStatement.__init__)
    params = list(sig.parameters.keys())



def test_plsql::statement::statement_is_not_abstract():
    assert not inspect.isabstract(plsql::statement::Statement)


def test_plsql::statement::statement_constructor_exists():
    assert callable(plsql::statement::Statement.__init__)


def test_plsql::statement::statement_constructor_args():
    sig = inspect.signature(plsql::statement::Statement.__init__)
    params = list(sig.parameters.keys())



def test_plsql::statement::raisestatement_is_not_abstract():
    assert not inspect.isabstract(plsql::statement::RaiseStatement)


def test_plsql::statement::raisestatement_constructor_exists():
    assert callable(plsql::statement::RaiseStatement.__init__)


def test_plsql::statement::raisestatement_constructor_args():
    sig = inspect.signature(plsql::statement::RaiseStatement.__init__)
    params = list(sig.parameters.keys())
    assert "exception" in params, "Missing parameter 'exception'"

def test_plsql::statement::raisestatement_has_exception():
    assert hasattr(plsql::statement::RaiseStatement, "exception")
    descriptor = None
    for klass in plsql::statement::RaiseStatement.__mro__:
        if "exception" in klass.__dict__:
            descriptor = klass.__dict__["exception"]
            break
    assert isinstance(descriptor, property)



def test_plsql::statement::nullstatement_is_not_abstract():
    assert not inspect.isabstract(plsql::statement::NullStatement)


def test_plsql::statement::nullstatement_constructor_exists():
    assert callable(plsql::statement::NullStatement.__init__)


def test_plsql::statement::nullstatement_constructor_args():
    sig = inspect.signature(plsql::statement::NullStatement.__init__)
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



def test_plsql::statement::forstatement_is_not_abstract():
    assert not inspect.isabstract(plsql::statement::ForStatement)


def test_plsql::statement::forstatement_constructor_exists():
    assert callable(plsql::statement::ForStatement.__init__)


def test_plsql::statement::forstatement_constructor_args():
    sig = inspect.signature(plsql::statement::ForStatement.__init__)
    params = list(sig.parameters.keys())



def test_plsql::statement::loopstatement_is_not_abstract():
    assert not inspect.isabstract(plsql::statement::LoopStatement)


def test_plsql::statement::loopstatement_constructor_exists():
    assert callable(plsql::statement::LoopStatement.__init__)


def test_plsql::statement::loopstatement_constructor_args():
    sig = inspect.signature(plsql::statement::LoopStatement.__init__)
    params = list(sig.parameters.keys())



def test_ifstatement_is_not_abstract():
    assert not inspect.isabstract(IfStatement)


def test_ifstatement_constructor_exists():
    assert callable(IfStatement.__init__)


def test_ifstatement_constructor_args():
    sig = inspect.signature(IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_plsql::statement::ifstatement_is_not_abstract():
    assert not inspect.isabstract(plsql::statement::IfStatement)


def test_plsql::statement::ifstatement_constructor_exists():
    assert callable(plsql::statement::IfStatement.__init__)


def test_plsql::statement::ifstatement_constructor_args():
    sig = inspect.signature(plsql::statement::IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_plsql::statement::casestatement_is_not_abstract():
    assert not inspect.isabstract(plsql::statement::CaseStatement)


def test_plsql::statement::casestatement_constructor_exists():
    assert callable(plsql::statement::CaseStatement.__init__)


def test_plsql::statement::casestatement_constructor_args():
    sig = inspect.signature(plsql::statement::CaseStatement.__init__)
    params = list(sig.parameters.keys())

def test_arithmeticoperatortype_exists():
    # Check that the Enumeration exists
    assert ArithmeticOperatorType is not None

def test_arithmeticoperatortype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ArithmeticOperatorType]
    expected_literals = [
        "POSITIVE",
        "EXPONENT",
        "DIVISION",
        "NEGATIVE",
        "MINUS",
        "PLUS",
        "MULTIPLICATION",
        "DOUBLEVERTICALBAR",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ArithmeticOperatorType"

def test_literalexpressiontype_exists():
    # Check that the Enumeration exists
    assert LiteralExpressionType is not None

def test_literalexpressiontype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LiteralExpressionType]
    expected_literals = [
        "STRING",
        "INTEGER",
        "BOOLEAN",
        "NULL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LiteralExpressionType"

def test_basictypes_exists():
    # Check that the Enumeration exists
    assert BasicTypes is not None

def test_basictypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BasicTypes]
    expected_literals = [
        "BOOLEAN",
        "DOUBLE",
        "NVARCHAR",
        "NCHAR",
        "CHAR",
        "NATURAL",
        "NVARCHAR2",
        "NUMBER",
        "DECIMAL",
        "DATE",
        "ROWID",
        "DEC",
        "INT",
        "VARCHAR",
        "BLOB",
        "BINARY_INTEGER",
        "CHARACTER",
        "REAL",
        "NUMERIC",
        "BINARY_FLOAT",
        "FLOAT",
        "LONG",
        "INTEGER",
        "VARCHAR2",
        "POSITIVE",
        "CLOB",
        "BINARY_DOUBLE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BasicTypes"

def test_booleanoperatortype_exists():
    # Check that the Enumeration exists
    assert BooleanOperatorType is not None

def test_booleanoperatortype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BooleanOperatorType]
    expected_literals = [
        "AND",
        "LESSEQUALS",
        "NOTEQUALS",
        "EQUALS",
        "LESSTHAN",
        "GREATERTHAN",
        "GREATEREQUALS",
        "OR",
        "NOT",
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
plsql::declaration::NamedElement_strategy = st.builds(
    plsql::declaration::NamedElement,
    name=
        safe_text
)
TriggerBlock_strategy = st.builds(
    TriggerBlock,
)
plsql::declaration::PLSQLDefinition_strategy = st.builds(
    plsql::declaration::PLSQLDefinition,
)
statement::BlockStatement_strategy = st.builds(
    statement::BlockStatement,
)
SelectStatement_strategy = st.builds(
    SelectStatement,
)
Argument_strategy = st.builds(
    Argument,
)
type::TypedElement_strategy = st.builds(
    type::TypedElement,
)
declaration::Declaration_strategy = st.builds(
    declaration::Declaration,
)
plsql::declaration::FunctionDeclaration_strategy = st.builds(
    plsql::declaration::FunctionDeclaration,
)
plsql::declaration::VariableDeclaration_strategy = st.builds(
    plsql::declaration::VariableDeclaration,
    notnull=
        st.booleans(),
    default=
        st.booleans(),
    constant=
        st.booleans()
)
plsql::condition::SQLCondition_strategy = st.builds(
    plsql::condition::SQLCondition,
)
plsql::type::TypedElement_strategy = st.builds(
    plsql::type::TypedElement,
)
StringOperation_strategy = st.builds(
    StringOperation,
)
plsql::expression::ConcatString_strategy = st.builds(
    plsql::expression::ConcatString,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
plsql::declaration::Declaration_strategy = st.builds(
    plsql::declaration::Declaration,
)
plsql::declaration::Package_strategy = st.builds(
    plsql::declaration::Package,
)
plsql::expression::FunctionCallParameter_strategy = st.builds(
    plsql::expression::FunctionCallParameter,
)
Type_strategy = st.builds(
    Type,
)
plsql::type::IndirectType_strategy = st.builds(
    plsql::type::IndirectType,
    identifier=
        safe_text,
    rowtype=
        st.booleans(),
    range=
        st.integers(),
    type=
        st.booleans()
)
plsql::type::GenericType_strategy = st.builds(
    plsql::type::GenericType,
)
plsql::type::Datatype_strategy = st.builds(
    plsql::type::Datatype,
    range=
        st.integers(),
    name=
        safe_text
)
plsql::type::Type_strategy = st.builds(
    plsql::type::Type,
)
SQLCondition_strategy = st.builds(
    SQLCondition,
)
plsql::condition::BooleanCondition_strategy = st.builds(
    plsql::condition::BooleanCondition,
    type=
        safe_text
)
plsql::condition::ConditionComparison_strategy = st.builds(
    plsql::condition::ConditionComparison,
    type=
        safe_text
)
plsql::condition::NotCondition_strategy = st.builds(
    plsql::condition::NotCondition,
)
condition::SQLCondition_strategy = st.builds(
    condition::SQLCondition,
)
plsql::expression::Expression_strategy = st.builds(
    plsql::expression::Expression,
)
plsql::statement::ExceptionSection_strategy = st.builds(
    plsql::statement::ExceptionSection,
    exceptionNames=
        safe_text
)
plsql::statement::UpdatePair_strategy = st.builds(
    plsql::statement::UpdatePair,
    column=
        safe_text
)
UpdatePair_strategy = st.builds(
    UpdatePair,
)
ExceptionSection_strategy = st.builds(
    ExceptionSection,
)
Declaration_strategy = st.builds(
    Declaration,
)
plsql::declaration::CursorDeclaration_strategy = st.builds(
    plsql::declaration::CursorDeclaration,
)
plsql::declaration::ProcedureDeclaration_strategy = st.builds(
    plsql::declaration::ProcedureDeclaration,
)
ModifySQLStatement_strategy = st.builds(
    ModifySQLStatement,
)
plsql::statement::UpdateStatement_strategy = st.builds(
    plsql::statement::UpdateStatement,
    table=
        safe_text
)
plsql::statement::SetTransactionStatement_strategy = st.builds(
    plsql::statement::SetTransactionStatement,
)
plsql::statement::DeleteStatement_strategy = st.builds(
    plsql::statement::DeleteStatement,
)
plsql::statement::InsertStatement_strategy = st.builds(
    plsql::statement::InsertStatement,
    into=
        safe_text,
    columns=
        safe_text
)
plsql::statement::SelectStatement_strategy = st.builds(
    plsql::statement::SelectStatement,
    bulk=
        st.booleans(),
    distinct=
        st.booleans(),
    collect=
        st.booleans(),
    selectList=
        safe_text,
    unique=
        st.booleans(),
    isCount=
        st.booleans(),
    all=
        st.booleans(),
    from_=
        safe_text
)
VarRefExpression_strategy = st.builds(
    VarRefExpression,
)
plsql::expression::SQLVariable_strategy = st.builds(
    plsql::expression::SQLVariable,
)
plsql::expression::FormsVarRef_strategy = st.builds(
    plsql::expression::FormsVarRef,
    reference=
        safe_text
)
plsql::expression::SQLCursor_strategy = st.builds(
    plsql::expression::SQLCursor,
)
CursorDeclaration_strategy = st.builds(
    CursorDeclaration,
)
ControlSQLStatement_strategy = st.builds(
    ControlSQLStatement,
)
plsql::statement::SavepointStatement_strategy = st.builds(
    plsql::statement::SavepointStatement,
)
plsql::statement::FetchStatement_strategy = st.builds(
    plsql::statement::FetchStatement,
)
plsql::statement::OpenStatement_strategy = st.builds(
    plsql::statement::OpenStatement,
)
plsql::statement::CommitStatement_strategy = st.builds(
    plsql::statement::CommitStatement,
)
plsql::statement::LockTableStatement_strategy = st.builds(
    plsql::statement::LockTableStatement,
)
plsql::statement::RollbackStatement_strategy = st.builds(
    plsql::statement::RollbackStatement,
)
plsql::statement::CloseStatement_strategy = st.builds(
    plsql::statement::CloseStatement,
)
SQLStatement_strategy = st.builds(
    SQLStatement,
)
plsql::statement::ModifySQLStatement_strategy = st.builds(
    plsql::statement::ModifySQLStatement,
)
plsql::statement::ControlSQLStatement_strategy = st.builds(
    plsql::statement::ControlSQLStatement,
)
FunctionCallParameter_strategy = st.builds(
    FunctionCallParameter,
)
expression::Expression_strategy = st.builds(
    expression::Expression,
)
plsql::expression::BooleanExpression_strategy = st.builds(
    plsql::expression::BooleanExpression,
    type=
        safe_text
)
declaration::NamedElement_strategy = st.builds(
    declaration::NamedElement,
)
plsql::declaration::Argument_strategy = st.builds(
    plsql::declaration::Argument,
    default=
        st.booleans(),
    in_=
        st.booleans(),
    out=
        st.booleans()
)
plsql::declaration::TriggerBlock_strategy = st.builds(
    plsql::declaration::TriggerBlock,
)
statement::Statement_strategy = st.builds(
    statement::Statement,
)
plsql::statement::FunctionCallStatement_strategy = st.builds(
    plsql::statement::FunctionCallStatement,
)
plsql::statement::GotoStatement_strategy = st.builds(
    plsql::statement::GotoStatement,
)
Expression_strategy = st.builds(
    Expression,
)
plsql::expression::VarRefExpression_strategy = st.builds(
    plsql::expression::VarRefExpression,
)
plsql::expression::LikeExpression_strategy = st.builds(
    plsql::expression::LikeExpression,
)
plsql::expression::IsNullExpression_strategy = st.builds(
    plsql::expression::IsNullExpression,
)
plsql::expression::LiteralExpression_strategy = st.builds(
    plsql::expression::LiteralExpression,
    value=
        safe_text,
    type=
        safe_text
)
plsql::expression::StringOperation_strategy = st.builds(
    plsql::expression::StringOperation,
)
plsql::expression::PropertyAccess_strategy = st.builds(
    plsql::expression::PropertyAccess,
    propertyName=
        safe_text
)
plsql::expression::ArithmeticExpression_strategy = st.builds(
    plsql::expression::ArithmeticExpression,
    type=
        safe_text
)
plsql::expression::InRangeExpression_strategy = st.builds(
    plsql::expression::InRangeExpression,
)
plsql::expression::FoundExpression_strategy = st.builds(
    plsql::expression::FoundExpression,
)
plsql::expression::NotExpression_strategy = st.builds(
    plsql::expression::NotExpression,
)
Statement_strategy = st.builds(
    Statement,
)
plsql::statement::ExitStatement_strategy = st.builds(
    plsql::statement::ExitStatement,
)
plsql::statement::BlockStatement_strategy = st.builds(
    plsql::statement::BlockStatement,
)
plsql::statement::ReturnStatement_strategy = st.builds(
    plsql::statement::ReturnStatement,
)
plsql::statement::SQLStatement_strategy = st.builds(
    plsql::statement::SQLStatement,
)
plsql::statement::AssignmentStatement_strategy = st.builds(
    plsql::statement::AssignmentStatement,
)
plsql::statement::Statement_strategy = st.builds(
    plsql::statement::Statement,
)
plsql::statement::RaiseStatement_strategy = st.builds(
    plsql::statement::RaiseStatement,
    exception=
        safe_text
)
plsql::statement::NullStatement_strategy = st.builds(
    plsql::statement::NullStatement,
)
VariableDeclaration_strategy = st.builds(
    VariableDeclaration,
)
LoopStatement_strategy = st.builds(
    LoopStatement,
)
plsql::statement::ForStatement_strategy = st.builds(
    plsql::statement::ForStatement,
)
plsql::statement::LoopStatement_strategy = st.builds(
    plsql::statement::LoopStatement,
)
IfStatement_strategy = st.builds(
    IfStatement,
)
plsql::statement::IfStatement_strategy = st.builds(
    plsql::statement::IfStatement,
)
plsql::statement::CaseStatement_strategy = st.builds(
    plsql::statement::CaseStatement,
)

@given(instance=plsql::declaration::NamedElement_strategy)
@settings(max_examples=50)
def test_plsql::declaration::namedelement_instantiation(instance):
    assert isinstance(instance, plsql::declaration::NamedElement)

@given(instance=plsql::declaration::NamedElement_strategy)
def test_plsql::declaration::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=plsql::declaration::NamedElement_strategy)
def test_plsql::declaration::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=TriggerBlock_strategy)
@settings(max_examples=50)
def test_triggerblock_instantiation(instance):
    assert isinstance(instance, TriggerBlock)

@given(instance=plsql::declaration::PLSQLDefinition_strategy)
@settings(max_examples=50)
def test_plsql::declaration::plsqldefinition_instantiation(instance):
    assert isinstance(instance, plsql::declaration::PLSQLDefinition)

@given(instance=statement::BlockStatement_strategy)
@settings(max_examples=50)
def test_statement::blockstatement_instantiation(instance):
    assert isinstance(instance, statement::BlockStatement)

@given(instance=SelectStatement_strategy)
@settings(max_examples=50)
def test_selectstatement_instantiation(instance):
    assert isinstance(instance, SelectStatement)

@given(instance=Argument_strategy)
@settings(max_examples=50)
def test_argument_instantiation(instance):
    assert isinstance(instance, Argument)

@given(instance=type::TypedElement_strategy)
@settings(max_examples=50)
def test_type::typedelement_instantiation(instance):
    assert isinstance(instance, type::TypedElement)

@given(instance=declaration::Declaration_strategy)
@settings(max_examples=50)
def test_declaration::declaration_instantiation(instance):
    assert isinstance(instance, declaration::Declaration)

@given(instance=plsql::declaration::FunctionDeclaration_strategy)
@settings(max_examples=50)
def test_plsql::declaration::functiondeclaration_instantiation(instance):
    assert isinstance(instance, plsql::declaration::FunctionDeclaration)

@given(instance=plsql::declaration::VariableDeclaration_strategy)
@settings(max_examples=50)
def test_plsql::declaration::variabledeclaration_instantiation(instance):
    assert isinstance(instance, plsql::declaration::VariableDeclaration)

@given(instance=plsql::declaration::VariableDeclaration_strategy)
def test_plsql::declaration::variabledeclaration_notnull_type(instance):
    assert isinstance(instance.notnull, bool)


@given(instance=plsql::declaration::VariableDeclaration_strategy)
def test_plsql::declaration::variabledeclaration_notnull_setter(instance):
    original = instance.notnull
    instance.notnull = original
    assert instance.notnull == original

@given(instance=plsql::declaration::VariableDeclaration_strategy)
def test_plsql::declaration::variabledeclaration_default_type(instance):
    assert isinstance(instance.default, bool)


@given(instance=plsql::declaration::VariableDeclaration_strategy)
def test_plsql::declaration::variabledeclaration_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original

@given(instance=plsql::declaration::VariableDeclaration_strategy)
def test_plsql::declaration::variabledeclaration_constant_type(instance):
    assert isinstance(instance.constant, bool)


@given(instance=plsql::declaration::VariableDeclaration_strategy)
def test_plsql::declaration::variabledeclaration_constant_setter(instance):
    original = instance.constant
    instance.constant = original
    assert instance.constant == original

@given(instance=plsql::condition::SQLCondition_strategy)
@settings(max_examples=50)
def test_plsql::condition::sqlcondition_instantiation(instance):
    assert isinstance(instance, plsql::condition::SQLCondition)

@given(instance=plsql::type::TypedElement_strategy)
@settings(max_examples=50)
def test_plsql::type::typedelement_instantiation(instance):
    assert isinstance(instance, plsql::type::TypedElement)

@given(instance=StringOperation_strategy)
@settings(max_examples=50)
def test_stringoperation_instantiation(instance):
    assert isinstance(instance, StringOperation)

@given(instance=plsql::expression::ConcatString_strategy)
@settings(max_examples=50)
def test_plsql::expression::concatstring_instantiation(instance):
    assert isinstance(instance, plsql::expression::ConcatString)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=plsql::declaration::Declaration_strategy)
@settings(max_examples=50)
def test_plsql::declaration::declaration_instantiation(instance):
    assert isinstance(instance, plsql::declaration::Declaration)

@given(instance=plsql::declaration::Package_strategy)
@settings(max_examples=50)
def test_plsql::declaration::package_instantiation(instance):
    assert isinstance(instance, plsql::declaration::Package)

@given(instance=plsql::expression::FunctionCallParameter_strategy)
@settings(max_examples=50)
def test_plsql::expression::functioncallparameter_instantiation(instance):
    assert isinstance(instance, plsql::expression::FunctionCallParameter)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=plsql::type::IndirectType_strategy)
@settings(max_examples=50)
def test_plsql::type::indirecttype_instantiation(instance):
    assert isinstance(instance, plsql::type::IndirectType)

@given(instance=plsql::type::IndirectType_strategy)
def test_plsql::type::indirecttype_identifier_type(instance):
    assert isinstance(instance.identifier, str)


@given(instance=plsql::type::IndirectType_strategy)
def test_plsql::type::indirecttype_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=plsql::type::IndirectType_strategy)
def test_plsql::type::indirecttype_rowtype_type(instance):
    assert isinstance(instance.rowtype, bool)


@given(instance=plsql::type::IndirectType_strategy)
def test_plsql::type::indirecttype_rowtype_setter(instance):
    original = instance.rowtype
    instance.rowtype = original
    assert instance.rowtype == original

@given(instance=plsql::type::IndirectType_strategy)
def test_plsql::type::indirecttype_range_type(instance):
    assert isinstance(instance.range, int)


@given(instance=plsql::type::IndirectType_strategy)
def test_plsql::type::indirecttype_range_setter(instance):
    original = instance.range
    instance.range = original
    assert instance.range == original

@given(instance=plsql::type::IndirectType_strategy)
def test_plsql::type::indirecttype_type_type(instance):
    assert isinstance(instance.type, bool)


@given(instance=plsql::type::IndirectType_strategy)
def test_plsql::type::indirecttype_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=plsql::type::GenericType_strategy)
@settings(max_examples=50)
def test_plsql::type::generictype_instantiation(instance):
    assert isinstance(instance, plsql::type::GenericType)

@given(instance=plsql::type::Datatype_strategy)
@settings(max_examples=50)
def test_plsql::type::datatype_instantiation(instance):
    assert isinstance(instance, plsql::type::Datatype)

@given(instance=plsql::type::Datatype_strategy)
def test_plsql::type::datatype_range_type(instance):
    assert isinstance(instance.range, int)


@given(instance=plsql::type::Datatype_strategy)
def test_plsql::type::datatype_range_setter(instance):
    original = instance.range
    instance.range = original
    assert instance.range == original

@given(instance=plsql::type::Datatype_strategy)
def test_plsql::type::datatype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=plsql::type::Datatype_strategy)
def test_plsql::type::datatype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=plsql::type::Type_strategy)
@settings(max_examples=50)
def test_plsql::type::type_instantiation(instance):
    assert isinstance(instance, plsql::type::Type)

@given(instance=SQLCondition_strategy)
@settings(max_examples=50)
def test_sqlcondition_instantiation(instance):
    assert isinstance(instance, SQLCondition)

@given(instance=plsql::condition::BooleanCondition_strategy)
@settings(max_examples=50)
def test_plsql::condition::booleancondition_instantiation(instance):
    assert isinstance(instance, plsql::condition::BooleanCondition)

@given(instance=plsql::condition::BooleanCondition_strategy)
def test_plsql::condition::booleancondition_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=plsql::condition::BooleanCondition_strategy)
def test_plsql::condition::booleancondition_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=plsql::condition::ConditionComparison_strategy)
@settings(max_examples=50)
def test_plsql::condition::conditioncomparison_instantiation(instance):
    assert isinstance(instance, plsql::condition::ConditionComparison)

@given(instance=plsql::condition::ConditionComparison_strategy)
def test_plsql::condition::conditioncomparison_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=plsql::condition::ConditionComparison_strategy)
def test_plsql::condition::conditioncomparison_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=plsql::condition::NotCondition_strategy)
@settings(max_examples=50)
def test_plsql::condition::notcondition_instantiation(instance):
    assert isinstance(instance, plsql::condition::NotCondition)

@given(instance=condition::SQLCondition_strategy)
@settings(max_examples=50)
def test_condition::sqlcondition_instantiation(instance):
    assert isinstance(instance, condition::SQLCondition)

@given(instance=plsql::expression::Expression_strategy)
@settings(max_examples=50)
def test_plsql::expression::expression_instantiation(instance):
    assert isinstance(instance, plsql::expression::Expression)

@given(instance=plsql::statement::ExceptionSection_strategy)
@settings(max_examples=50)
def test_plsql::statement::exceptionsection_instantiation(instance):
    assert isinstance(instance, plsql::statement::ExceptionSection)

@given(instance=plsql::statement::ExceptionSection_strategy)
def test_plsql::statement::exceptionsection_exceptionNames_type(instance):
    assert isinstance(instance.exceptionNames, str)


@given(instance=plsql::statement::ExceptionSection_strategy)
def test_plsql::statement::exceptionsection_exceptionNames_setter(instance):
    original = instance.exceptionNames
    instance.exceptionNames = original
    assert instance.exceptionNames == original

@given(instance=plsql::statement::UpdatePair_strategy)
@settings(max_examples=50)
def test_plsql::statement::updatepair_instantiation(instance):
    assert isinstance(instance, plsql::statement::UpdatePair)

@given(instance=plsql::statement::UpdatePair_strategy)
def test_plsql::statement::updatepair_column_type(instance):
    assert isinstance(instance.column, str)


@given(instance=plsql::statement::UpdatePair_strategy)
def test_plsql::statement::updatepair_column_setter(instance):
    original = instance.column
    instance.column = original
    assert instance.column == original

@given(instance=UpdatePair_strategy)
@settings(max_examples=50)
def test_updatepair_instantiation(instance):
    assert isinstance(instance, UpdatePair)

@given(instance=ExceptionSection_strategy)
@settings(max_examples=50)
def test_exceptionsection_instantiation(instance):
    assert isinstance(instance, ExceptionSection)

@given(instance=Declaration_strategy)
@settings(max_examples=50)
def test_declaration_instantiation(instance):
    assert isinstance(instance, Declaration)

@given(instance=plsql::declaration::CursorDeclaration_strategy)
@settings(max_examples=50)
def test_plsql::declaration::cursordeclaration_instantiation(instance):
    assert isinstance(instance, plsql::declaration::CursorDeclaration)

@given(instance=plsql::declaration::ProcedureDeclaration_strategy)
@settings(max_examples=50)
def test_plsql::declaration::proceduredeclaration_instantiation(instance):
    assert isinstance(instance, plsql::declaration::ProcedureDeclaration)

@given(instance=ModifySQLStatement_strategy)
@settings(max_examples=50)
def test_modifysqlstatement_instantiation(instance):
    assert isinstance(instance, ModifySQLStatement)

@given(instance=plsql::statement::UpdateStatement_strategy)
@settings(max_examples=50)
def test_plsql::statement::updatestatement_instantiation(instance):
    assert isinstance(instance, plsql::statement::UpdateStatement)

@given(instance=plsql::statement::UpdateStatement_strategy)
def test_plsql::statement::updatestatement_table_type(instance):
    assert isinstance(instance.table, str)


@given(instance=plsql::statement::UpdateStatement_strategy)
def test_plsql::statement::updatestatement_table_setter(instance):
    original = instance.table
    instance.table = original
    assert instance.table == original

@given(instance=plsql::statement::SetTransactionStatement_strategy)
@settings(max_examples=50)
def test_plsql::statement::settransactionstatement_instantiation(instance):
    assert isinstance(instance, plsql::statement::SetTransactionStatement)

@given(instance=plsql::statement::DeleteStatement_strategy)
@settings(max_examples=50)
def test_plsql::statement::deletestatement_instantiation(instance):
    assert isinstance(instance, plsql::statement::DeleteStatement)

@given(instance=plsql::statement::InsertStatement_strategy)
@settings(max_examples=50)
def test_plsql::statement::insertstatement_instantiation(instance):
    assert isinstance(instance, plsql::statement::InsertStatement)

@given(instance=plsql::statement::InsertStatement_strategy)
def test_plsql::statement::insertstatement_into_type(instance):
    assert isinstance(instance.into, str)


@given(instance=plsql::statement::InsertStatement_strategy)
def test_plsql::statement::insertstatement_into_setter(instance):
    original = instance.into
    instance.into = original
    assert instance.into == original

@given(instance=plsql::statement::InsertStatement_strategy)
def test_plsql::statement::insertstatement_columns_type(instance):
    assert isinstance(instance.columns, str)


@given(instance=plsql::statement::InsertStatement_strategy)
def test_plsql::statement::insertstatement_columns_setter(instance):
    original = instance.columns
    instance.columns = original
    assert instance.columns == original

@given(instance=plsql::statement::SelectStatement_strategy)
@settings(max_examples=50)
def test_plsql::statement::selectstatement_instantiation(instance):
    assert isinstance(instance, plsql::statement::SelectStatement)

@given(instance=plsql::statement::SelectStatement_strategy)
def test_plsql::statement::selectstatement_bulk_type(instance):
    assert isinstance(instance.bulk, bool)


@given(instance=plsql::statement::SelectStatement_strategy)
def test_plsql::statement::selectstatement_bulk_setter(instance):
    original = instance.bulk
    instance.bulk = original
    assert instance.bulk == original

@given(instance=plsql::statement::SelectStatement_strategy)
def test_plsql::statement::selectstatement_distinct_type(instance):
    assert isinstance(instance.distinct, bool)


@given(instance=plsql::statement::SelectStatement_strategy)
def test_plsql::statement::selectstatement_distinct_setter(instance):
    original = instance.distinct
    instance.distinct = original
    assert instance.distinct == original

@given(instance=plsql::statement::SelectStatement_strategy)
def test_plsql::statement::selectstatement_collect_type(instance):
    assert isinstance(instance.collect, bool)


@given(instance=plsql::statement::SelectStatement_strategy)
def test_plsql::statement::selectstatement_collect_setter(instance):
    original = instance.collect
    instance.collect = original
    assert instance.collect == original

@given(instance=plsql::statement::SelectStatement_strategy)
def test_plsql::statement::selectstatement_selectList_type(instance):
    assert isinstance(instance.selectList, str)


@given(instance=plsql::statement::SelectStatement_strategy)
def test_plsql::statement::selectstatement_selectList_setter(instance):
    original = instance.selectList
    instance.selectList = original
    assert instance.selectList == original

@given(instance=plsql::statement::SelectStatement_strategy)
def test_plsql::statement::selectstatement_unique_type(instance):
    assert isinstance(instance.unique, bool)


@given(instance=plsql::statement::SelectStatement_strategy)
def test_plsql::statement::selectstatement_unique_setter(instance):
    original = instance.unique
    instance.unique = original
    assert instance.unique == original

@given(instance=plsql::statement::SelectStatement_strategy)
def test_plsql::statement::selectstatement_isCount_type(instance):
    assert isinstance(instance.isCount, bool)


@given(instance=plsql::statement::SelectStatement_strategy)
def test_plsql::statement::selectstatement_isCount_setter(instance):
    original = instance.isCount
    instance.isCount = original
    assert instance.isCount == original

@given(instance=plsql::statement::SelectStatement_strategy)
def test_plsql::statement::selectstatement_all_type(instance):
    assert isinstance(instance.all, bool)


@given(instance=plsql::statement::SelectStatement_strategy)
def test_plsql::statement::selectstatement_all_setter(instance):
    original = instance.all
    instance.all = original
    assert instance.all == original

@given(instance=plsql::statement::SelectStatement_strategy)
def test_plsql::statement::selectstatement_from__type(instance):
    assert isinstance(instance.from_, str)


@given(instance=plsql::statement::SelectStatement_strategy)
def test_plsql::statement::selectstatement_from__setter(instance):
    original = instance.from_
    instance.from_ = original
    assert instance.from_ == original

@given(instance=VarRefExpression_strategy)
@settings(max_examples=50)
def test_varrefexpression_instantiation(instance):
    assert isinstance(instance, VarRefExpression)

@given(instance=plsql::expression::SQLVariable_strategy)
@settings(max_examples=50)
def test_plsql::expression::sqlvariable_instantiation(instance):
    assert isinstance(instance, plsql::expression::SQLVariable)

@given(instance=plsql::expression::FormsVarRef_strategy)
@settings(max_examples=50)
def test_plsql::expression::formsvarref_instantiation(instance):
    assert isinstance(instance, plsql::expression::FormsVarRef)

@given(instance=plsql::expression::FormsVarRef_strategy)
def test_plsql::expression::formsvarref_reference_type(instance):
    assert isinstance(instance.reference, str)


@given(instance=plsql::expression::FormsVarRef_strategy)
def test_plsql::expression::formsvarref_reference_setter(instance):
    original = instance.reference
    instance.reference = original
    assert instance.reference == original

@given(instance=plsql::expression::SQLCursor_strategy)
@settings(max_examples=50)
def test_plsql::expression::sqlcursor_instantiation(instance):
    assert isinstance(instance, plsql::expression::SQLCursor)

@given(instance=CursorDeclaration_strategy)
@settings(max_examples=50)
def test_cursordeclaration_instantiation(instance):
    assert isinstance(instance, CursorDeclaration)

@given(instance=ControlSQLStatement_strategy)
@settings(max_examples=50)
def test_controlsqlstatement_instantiation(instance):
    assert isinstance(instance, ControlSQLStatement)

@given(instance=plsql::statement::SavepointStatement_strategy)
@settings(max_examples=50)
def test_plsql::statement::savepointstatement_instantiation(instance):
    assert isinstance(instance, plsql::statement::SavepointStatement)

@given(instance=plsql::statement::FetchStatement_strategy)
@settings(max_examples=50)
def test_plsql::statement::fetchstatement_instantiation(instance):
    assert isinstance(instance, plsql::statement::FetchStatement)

@given(instance=plsql::statement::OpenStatement_strategy)
@settings(max_examples=50)
def test_plsql::statement::openstatement_instantiation(instance):
    assert isinstance(instance, plsql::statement::OpenStatement)

@given(instance=plsql::statement::CommitStatement_strategy)
@settings(max_examples=50)
def test_plsql::statement::commitstatement_instantiation(instance):
    assert isinstance(instance, plsql::statement::CommitStatement)

@given(instance=plsql::statement::LockTableStatement_strategy)
@settings(max_examples=50)
def test_plsql::statement::locktablestatement_instantiation(instance):
    assert isinstance(instance, plsql::statement::LockTableStatement)

@given(instance=plsql::statement::RollbackStatement_strategy)
@settings(max_examples=50)
def test_plsql::statement::rollbackstatement_instantiation(instance):
    assert isinstance(instance, plsql::statement::RollbackStatement)

@given(instance=plsql::statement::CloseStatement_strategy)
@settings(max_examples=50)
def test_plsql::statement::closestatement_instantiation(instance):
    assert isinstance(instance, plsql::statement::CloseStatement)

@given(instance=SQLStatement_strategy)
@settings(max_examples=50)
def test_sqlstatement_instantiation(instance):
    assert isinstance(instance, SQLStatement)

@given(instance=plsql::statement::ModifySQLStatement_strategy)
@settings(max_examples=50)
def test_plsql::statement::modifysqlstatement_instantiation(instance):
    assert isinstance(instance, plsql::statement::ModifySQLStatement)

@given(instance=plsql::statement::ControlSQLStatement_strategy)
@settings(max_examples=50)
def test_plsql::statement::controlsqlstatement_instantiation(instance):
    assert isinstance(instance, plsql::statement::ControlSQLStatement)

@given(instance=FunctionCallParameter_strategy)
@settings(max_examples=50)
def test_functioncallparameter_instantiation(instance):
    assert isinstance(instance, FunctionCallParameter)

@given(instance=expression::Expression_strategy)
@settings(max_examples=50)
def test_expression::expression_instantiation(instance):
    assert isinstance(instance, expression::Expression)

@given(instance=plsql::expression::BooleanExpression_strategy)
@settings(max_examples=50)
def test_plsql::expression::booleanexpression_instantiation(instance):
    assert isinstance(instance, plsql::expression::BooleanExpression)

@given(instance=plsql::expression::BooleanExpression_strategy)
def test_plsql::expression::booleanexpression_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=plsql::expression::BooleanExpression_strategy)
def test_plsql::expression::booleanexpression_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=declaration::NamedElement_strategy)
@settings(max_examples=50)
def test_declaration::namedelement_instantiation(instance):
    assert isinstance(instance, declaration::NamedElement)

@given(instance=plsql::declaration::Argument_strategy)
@settings(max_examples=50)
def test_plsql::declaration::argument_instantiation(instance):
    assert isinstance(instance, plsql::declaration::Argument)

@given(instance=plsql::declaration::Argument_strategy)
def test_plsql::declaration::argument_default_type(instance):
    assert isinstance(instance.default, bool)


@given(instance=plsql::declaration::Argument_strategy)
def test_plsql::declaration::argument_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original

@given(instance=plsql::declaration::Argument_strategy)
def test_plsql::declaration::argument_in__type(instance):
    assert isinstance(instance.in_, bool)


@given(instance=plsql::declaration::Argument_strategy)
def test_plsql::declaration::argument_in__setter(instance):
    original = instance.in_
    instance.in_ = original
    assert instance.in_ == original

@given(instance=plsql::declaration::Argument_strategy)
def test_plsql::declaration::argument_out_type(instance):
    assert isinstance(instance.out, bool)


@given(instance=plsql::declaration::Argument_strategy)
def test_plsql::declaration::argument_out_setter(instance):
    original = instance.out
    instance.out = original
    assert instance.out == original

@given(instance=plsql::declaration::TriggerBlock_strategy)
@settings(max_examples=50)
def test_plsql::declaration::triggerblock_instantiation(instance):
    assert isinstance(instance, plsql::declaration::TriggerBlock)

@given(instance=statement::Statement_strategy)
@settings(max_examples=50)
def test_statement::statement_instantiation(instance):
    assert isinstance(instance, statement::Statement)

@given(instance=plsql::statement::FunctionCallStatement_strategy)
@settings(max_examples=50)
def test_plsql::statement::functioncallstatement_instantiation(instance):
    assert isinstance(instance, plsql::statement::FunctionCallStatement)

@given(instance=plsql::statement::GotoStatement_strategy)
@settings(max_examples=50)
def test_plsql::statement::gotostatement_instantiation(instance):
    assert isinstance(instance, plsql::statement::GotoStatement)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=plsql::expression::VarRefExpression_strategy)
@settings(max_examples=50)
def test_plsql::expression::varrefexpression_instantiation(instance):
    assert isinstance(instance, plsql::expression::VarRefExpression)

@given(instance=plsql::expression::LikeExpression_strategy)
@settings(max_examples=50)
def test_plsql::expression::likeexpression_instantiation(instance):
    assert isinstance(instance, plsql::expression::LikeExpression)

@given(instance=plsql::expression::IsNullExpression_strategy)
@settings(max_examples=50)
def test_plsql::expression::isnullexpression_instantiation(instance):
    assert isinstance(instance, plsql::expression::IsNullExpression)

@given(instance=plsql::expression::LiteralExpression_strategy)
@settings(max_examples=50)
def test_plsql::expression::literalexpression_instantiation(instance):
    assert isinstance(instance, plsql::expression::LiteralExpression)

@given(instance=plsql::expression::LiteralExpression_strategy)
def test_plsql::expression::literalexpression_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=plsql::expression::LiteralExpression_strategy)
def test_plsql::expression::literalexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=plsql::expression::LiteralExpression_strategy)
def test_plsql::expression::literalexpression_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=plsql::expression::LiteralExpression_strategy)
def test_plsql::expression::literalexpression_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=plsql::expression::StringOperation_strategy)
@settings(max_examples=50)
def test_plsql::expression::stringoperation_instantiation(instance):
    assert isinstance(instance, plsql::expression::StringOperation)

@given(instance=plsql::expression::PropertyAccess_strategy)
@settings(max_examples=50)
def test_plsql::expression::propertyaccess_instantiation(instance):
    assert isinstance(instance, plsql::expression::PropertyAccess)

@given(instance=plsql::expression::PropertyAccess_strategy)
def test_plsql::expression::propertyaccess_propertyName_type(instance):
    assert isinstance(instance.propertyName, str)


@given(instance=plsql::expression::PropertyAccess_strategy)
def test_plsql::expression::propertyaccess_propertyName_setter(instance):
    original = instance.propertyName
    instance.propertyName = original
    assert instance.propertyName == original

@given(instance=plsql::expression::ArithmeticExpression_strategy)
@settings(max_examples=50)
def test_plsql::expression::arithmeticexpression_instantiation(instance):
    assert isinstance(instance, plsql::expression::ArithmeticExpression)

@given(instance=plsql::expression::ArithmeticExpression_strategy)
def test_plsql::expression::arithmeticexpression_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=plsql::expression::ArithmeticExpression_strategy)
def test_plsql::expression::arithmeticexpression_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=plsql::expression::InRangeExpression_strategy)
@settings(max_examples=50)
def test_plsql::expression::inrangeexpression_instantiation(instance):
    assert isinstance(instance, plsql::expression::InRangeExpression)

@given(instance=plsql::expression::FoundExpression_strategy)
@settings(max_examples=50)
def test_plsql::expression::foundexpression_instantiation(instance):
    assert isinstance(instance, plsql::expression::FoundExpression)

@given(instance=plsql::expression::NotExpression_strategy)
@settings(max_examples=50)
def test_plsql::expression::notexpression_instantiation(instance):
    assert isinstance(instance, plsql::expression::NotExpression)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=plsql::statement::ExitStatement_strategy)
@settings(max_examples=50)
def test_plsql::statement::exitstatement_instantiation(instance):
    assert isinstance(instance, plsql::statement::ExitStatement)

@given(instance=plsql::statement::BlockStatement_strategy)
@settings(max_examples=50)
def test_plsql::statement::blockstatement_instantiation(instance):
    assert isinstance(instance, plsql::statement::BlockStatement)

@given(instance=plsql::statement::ReturnStatement_strategy)
@settings(max_examples=50)
def test_plsql::statement::returnstatement_instantiation(instance):
    assert isinstance(instance, plsql::statement::ReturnStatement)

@given(instance=plsql::statement::SQLStatement_strategy)
@settings(max_examples=50)
def test_plsql::statement::sqlstatement_instantiation(instance):
    assert isinstance(instance, plsql::statement::SQLStatement)

@given(instance=plsql::statement::AssignmentStatement_strategy)
@settings(max_examples=50)
def test_plsql::statement::assignmentstatement_instantiation(instance):
    assert isinstance(instance, plsql::statement::AssignmentStatement)

@given(instance=plsql::statement::Statement_strategy)
@settings(max_examples=50)
def test_plsql::statement::statement_instantiation(instance):
    assert isinstance(instance, plsql::statement::Statement)

@given(instance=plsql::statement::RaiseStatement_strategy)
@settings(max_examples=50)
def test_plsql::statement::raisestatement_instantiation(instance):
    assert isinstance(instance, plsql::statement::RaiseStatement)

@given(instance=plsql::statement::RaiseStatement_strategy)
def test_plsql::statement::raisestatement_exception_type(instance):
    assert isinstance(instance.exception, str)


@given(instance=plsql::statement::RaiseStatement_strategy)
def test_plsql::statement::raisestatement_exception_setter(instance):
    original = instance.exception
    instance.exception = original
    assert instance.exception == original

@given(instance=plsql::statement::NullStatement_strategy)
@settings(max_examples=50)
def test_plsql::statement::nullstatement_instantiation(instance):
    assert isinstance(instance, plsql::statement::NullStatement)

@given(instance=VariableDeclaration_strategy)
@settings(max_examples=50)
def test_variabledeclaration_instantiation(instance):
    assert isinstance(instance, VariableDeclaration)

@given(instance=LoopStatement_strategy)
@settings(max_examples=50)
def test_loopstatement_instantiation(instance):
    assert isinstance(instance, LoopStatement)

@given(instance=plsql::statement::ForStatement_strategy)
@settings(max_examples=50)
def test_plsql::statement::forstatement_instantiation(instance):
    assert isinstance(instance, plsql::statement::ForStatement)

@given(instance=plsql::statement::LoopStatement_strategy)
@settings(max_examples=50)
def test_plsql::statement::loopstatement_instantiation(instance):
    assert isinstance(instance, plsql::statement::LoopStatement)

@given(instance=IfStatement_strategy)
@settings(max_examples=50)
def test_ifstatement_instantiation(instance):
    assert isinstance(instance, IfStatement)

@given(instance=plsql::statement::IfStatement_strategy)
@settings(max_examples=50)
def test_plsql::statement::ifstatement_instantiation(instance):
    assert isinstance(instance, plsql::statement::IfStatement)

@given(instance=plsql::statement::CaseStatement_strategy)
@settings(max_examples=50)
def test_plsql::statement::casestatement_instantiation(instance):
    assert isinstance(instance, plsql::statement::CaseStatement)
