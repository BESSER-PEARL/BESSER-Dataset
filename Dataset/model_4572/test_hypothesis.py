import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    lua::Functioncall::Arguments,
    lua::Field,
    LastStatement::Return,
    lua::LastStatement::ReturnWithValue,
    Field,
    lua::Field::AddEntryToTable,
    lua::Field::AppendEntryToTable,
    lua::Field::AddEntryToTable::Brackets,
    lua::Function,
    Expression,
    lua::Expression::True,
    lua::Expression::Negate,
    lua::Expression::Invert,
    lua::Expression::Exponentiation,
    lua::Expression::Division,
    lua::Expression::Equal,
    lua::Expression::Length,
    lua::Expression::False,
    lua::Expression::Not::Equal,
    lua::Expression::Larger,
    lua::Expression::Modulo,
    lua::Expression::Multiplication,
    lua::Expression::AccessArray,
    lua::Expression::AccessMember,
    lua::Expression::Number,
    lua::Expression::VariableName,
    lua::Expression::Smaller,
    lua::Expression::CallMemberFunction,
    lua::Expression::VarArgs,
    lua::Expression::Or,
    lua::Expression::And,
    lua::Expression::Function,
    lua::Expression::TableConstructor,
    lua::Expression::Concatenation,
    lua::Expression::CallFunction,
    lua::Expression::Plus,
    lua::Expression::Larger::Equal,
    lua::Expression::String,
    lua::Expression::Minus,
    lua::Expression::Smaller::Equal,
    lua::Expression::Nil,
    Statement::FunctioncallOrAssignment,
    lua::Statement::Assignment,
    lua::Statement::CallFunction,
    lua::Statement::CallMemberFunction,
    lua::Statement::If::Then::Else::ElseIfPart,
    lua::Expression,
    Statement,
    lua::Statement::FunctioncallOrAssignment,
    lua::Statement::For::Numeric,
    lua::Statement::Local::Variable::Declaration,
    lua::Statement::While,
    lua::Statement::If::Then::Else,
    lua::Statement::Repeat,
    lua::Statement::GlobalFunction::Declaration,
    lua::Statement::For::Generic,
    lua::Statement::LocalFunction::Declaration,
    lua::Statement::Block,
    LastStatement,
    lua::LastStatement::Break,
    lua::LastStatement::Return,
    lua::LastStatement,
    lua::Statement,
    Chunk,
    lua::Block,
    lua::Chunk,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_lua::functioncall::arguments_is_not_abstract():
    assert not inspect.isabstract(lua::Functioncall::Arguments)


def test_lua::functioncall::arguments_constructor_exists():
    assert callable(lua::Functioncall::Arguments.__init__)


def test_lua::functioncall::arguments_constructor_args():
    sig = inspect.signature(lua::Functioncall::Arguments.__init__)
    params = list(sig.parameters.keys())



def test_lua::field_is_not_abstract():
    assert not inspect.isabstract(lua::Field)


def test_lua::field_constructor_exists():
    assert callable(lua::Field.__init__)


def test_lua::field_constructor_args():
    sig = inspect.signature(lua::Field.__init__)
    params = list(sig.parameters.keys())



def test_laststatement::return_is_not_abstract():
    assert not inspect.isabstract(LastStatement::Return)


def test_laststatement::return_constructor_exists():
    assert callable(LastStatement::Return.__init__)


def test_laststatement::return_constructor_args():
    sig = inspect.signature(LastStatement::Return.__init__)
    params = list(sig.parameters.keys())



def test_lua::laststatement::returnwithvalue_is_not_abstract():
    assert not inspect.isabstract(lua::LastStatement::ReturnWithValue)


def test_lua::laststatement::returnwithvalue_constructor_exists():
    assert callable(lua::LastStatement::ReturnWithValue.__init__)


def test_lua::laststatement::returnwithvalue_constructor_args():
    sig = inspect.signature(lua::LastStatement::ReturnWithValue.__init__)
    params = list(sig.parameters.keys())



def test_field_is_not_abstract():
    assert not inspect.isabstract(Field)


def test_field_constructor_exists():
    assert callable(Field.__init__)


def test_field_constructor_args():
    sig = inspect.signature(Field.__init__)
    params = list(sig.parameters.keys())



def test_lua::field::addentrytotable_is_not_abstract():
    assert not inspect.isabstract(lua::Field::AddEntryToTable)


def test_lua::field::addentrytotable_constructor_exists():
    assert callable(lua::Field::AddEntryToTable.__init__)


def test_lua::field::addentrytotable_constructor_args():
    sig = inspect.signature(lua::Field::AddEntryToTable.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"

def test_lua::field::addentrytotable_has_key():
    assert hasattr(lua::Field::AddEntryToTable, "key")
    descriptor = None
    for klass in lua::Field::AddEntryToTable.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_lua::field::appendentrytotable_is_not_abstract():
    assert not inspect.isabstract(lua::Field::AppendEntryToTable)


def test_lua::field::appendentrytotable_constructor_exists():
    assert callable(lua::Field::AppendEntryToTable.__init__)


def test_lua::field::appendentrytotable_constructor_args():
    sig = inspect.signature(lua::Field::AppendEntryToTable.__init__)
    params = list(sig.parameters.keys())



def test_lua::field::addentrytotable::brackets_is_not_abstract():
    assert not inspect.isabstract(lua::Field::AddEntryToTable::Brackets)


def test_lua::field::addentrytotable::brackets_constructor_exists():
    assert callable(lua::Field::AddEntryToTable::Brackets.__init__)


def test_lua::field::addentrytotable::brackets_constructor_args():
    sig = inspect.signature(lua::Field::AddEntryToTable::Brackets.__init__)
    params = list(sig.parameters.keys())



def test_lua::function_is_not_abstract():
    assert not inspect.isabstract(lua::Function)


def test_lua::function_constructor_exists():
    assert callable(lua::Function.__init__)


def test_lua::function_constructor_args():
    sig = inspect.signature(lua::Function.__init__)
    params = list(sig.parameters.keys())
    assert "varArgs" in params, "Missing parameter 'varArgs'"
    assert "parameters" in params, "Missing parameter 'parameters'"

def test_lua::function_has_varArgs():
    assert hasattr(lua::Function, "varArgs")
    descriptor = None
    for klass in lua::Function.__mro__:
        if "varArgs" in klass.__dict__:
            descriptor = klass.__dict__["varArgs"]
            break
    assert isinstance(descriptor, property)

def test_lua::function_has_parameters():
    assert hasattr(lua::Function, "parameters")
    descriptor = None
    for klass in lua::Function.__mro__:
        if "parameters" in klass.__dict__:
            descriptor = klass.__dict__["parameters"]
            break
    assert isinstance(descriptor, property)



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_lua::expression::true_is_not_abstract():
    assert not inspect.isabstract(lua::Expression::True)


def test_lua::expression::true_constructor_exists():
    assert callable(lua::Expression::True.__init__)


def test_lua::expression::true_constructor_args():
    sig = inspect.signature(lua::Expression::True.__init__)
    params = list(sig.parameters.keys())



def test_lua::expression::negate_is_not_abstract():
    assert not inspect.isabstract(lua::Expression::Negate)


def test_lua::expression::negate_constructor_exists():
    assert callable(lua::Expression::Negate.__init__)


def test_lua::expression::negate_constructor_args():
    sig = inspect.signature(lua::Expression::Negate.__init__)
    params = list(sig.parameters.keys())



def test_lua::expression::invert_is_not_abstract():
    assert not inspect.isabstract(lua::Expression::Invert)


def test_lua::expression::invert_constructor_exists():
    assert callable(lua::Expression::Invert.__init__)


def test_lua::expression::invert_constructor_args():
    sig = inspect.signature(lua::Expression::Invert.__init__)
    params = list(sig.parameters.keys())



def test_lua::expression::exponentiation_is_not_abstract():
    assert not inspect.isabstract(lua::Expression::Exponentiation)


def test_lua::expression::exponentiation_constructor_exists():
    assert callable(lua::Expression::Exponentiation.__init__)


def test_lua::expression::exponentiation_constructor_args():
    sig = inspect.signature(lua::Expression::Exponentiation.__init__)
    params = list(sig.parameters.keys())



def test_lua::expression::division_is_not_abstract():
    assert not inspect.isabstract(lua::Expression::Division)


def test_lua::expression::division_constructor_exists():
    assert callable(lua::Expression::Division.__init__)


def test_lua::expression::division_constructor_args():
    sig = inspect.signature(lua::Expression::Division.__init__)
    params = list(sig.parameters.keys())



def test_lua::expression::equal_is_not_abstract():
    assert not inspect.isabstract(lua::Expression::Equal)


def test_lua::expression::equal_constructor_exists():
    assert callable(lua::Expression::Equal.__init__)


def test_lua::expression::equal_constructor_args():
    sig = inspect.signature(lua::Expression::Equal.__init__)
    params = list(sig.parameters.keys())



def test_lua::expression::length_is_not_abstract():
    assert not inspect.isabstract(lua::Expression::Length)


def test_lua::expression::length_constructor_exists():
    assert callable(lua::Expression::Length.__init__)


def test_lua::expression::length_constructor_args():
    sig = inspect.signature(lua::Expression::Length.__init__)
    params = list(sig.parameters.keys())



def test_lua::expression::false_is_not_abstract():
    assert not inspect.isabstract(lua::Expression::False)


def test_lua::expression::false_constructor_exists():
    assert callable(lua::Expression::False.__init__)


def test_lua::expression::false_constructor_args():
    sig = inspect.signature(lua::Expression::False.__init__)
    params = list(sig.parameters.keys())



def test_lua::expression::not::equal_is_not_abstract():
    assert not inspect.isabstract(lua::Expression::Not::Equal)


def test_lua::expression::not::equal_constructor_exists():
    assert callable(lua::Expression::Not::Equal.__init__)


def test_lua::expression::not::equal_constructor_args():
    sig = inspect.signature(lua::Expression::Not::Equal.__init__)
    params = list(sig.parameters.keys())



def test_lua::expression::larger_is_not_abstract():
    assert not inspect.isabstract(lua::Expression::Larger)


def test_lua::expression::larger_constructor_exists():
    assert callable(lua::Expression::Larger.__init__)


def test_lua::expression::larger_constructor_args():
    sig = inspect.signature(lua::Expression::Larger.__init__)
    params = list(sig.parameters.keys())



def test_lua::expression::modulo_is_not_abstract():
    assert not inspect.isabstract(lua::Expression::Modulo)


def test_lua::expression::modulo_constructor_exists():
    assert callable(lua::Expression::Modulo.__init__)


def test_lua::expression::modulo_constructor_args():
    sig = inspect.signature(lua::Expression::Modulo.__init__)
    params = list(sig.parameters.keys())



def test_lua::expression::multiplication_is_not_abstract():
    assert not inspect.isabstract(lua::Expression::Multiplication)


def test_lua::expression::multiplication_constructor_exists():
    assert callable(lua::Expression::Multiplication.__init__)


def test_lua::expression::multiplication_constructor_args():
    sig = inspect.signature(lua::Expression::Multiplication.__init__)
    params = list(sig.parameters.keys())



def test_lua::expression::accessarray_is_not_abstract():
    assert not inspect.isabstract(lua::Expression::AccessArray)


def test_lua::expression::accessarray_constructor_exists():
    assert callable(lua::Expression::AccessArray.__init__)


def test_lua::expression::accessarray_constructor_args():
    sig = inspect.signature(lua::Expression::AccessArray.__init__)
    params = list(sig.parameters.keys())



def test_lua::expression::accessmember_is_not_abstract():
    assert not inspect.isabstract(lua::Expression::AccessMember)


def test_lua::expression::accessmember_constructor_exists():
    assert callable(lua::Expression::AccessMember.__init__)


def test_lua::expression::accessmember_constructor_args():
    sig = inspect.signature(lua::Expression::AccessMember.__init__)
    params = list(sig.parameters.keys())
    assert "memberName" in params, "Missing parameter 'memberName'"

def test_lua::expression::accessmember_has_memberName():
    assert hasattr(lua::Expression::AccessMember, "memberName")
    descriptor = None
    for klass in lua::Expression::AccessMember.__mro__:
        if "memberName" in klass.__dict__:
            descriptor = klass.__dict__["memberName"]
            break
    assert isinstance(descriptor, property)



def test_lua::expression::number_is_not_abstract():
    assert not inspect.isabstract(lua::Expression::Number)


def test_lua::expression::number_constructor_exists():
    assert callable(lua::Expression::Number.__init__)


def test_lua::expression::number_constructor_args():
    sig = inspect.signature(lua::Expression::Number.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_lua::expression::number_has_value():
    assert hasattr(lua::Expression::Number, "value")
    descriptor = None
    for klass in lua::Expression::Number.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_lua::expression::variablename_is_not_abstract():
    assert not inspect.isabstract(lua::Expression::VariableName)


def test_lua::expression::variablename_constructor_exists():
    assert callable(lua::Expression::VariableName.__init__)


def test_lua::expression::variablename_constructor_args():
    sig = inspect.signature(lua::Expression::VariableName.__init__)
    params = list(sig.parameters.keys())
    assert "variable" in params, "Missing parameter 'variable'"

def test_lua::expression::variablename_has_variable():
    assert hasattr(lua::Expression::VariableName, "variable")
    descriptor = None
    for klass in lua::Expression::VariableName.__mro__:
        if "variable" in klass.__dict__:
            descriptor = klass.__dict__["variable"]
            break
    assert isinstance(descriptor, property)



def test_lua::expression::smaller_is_not_abstract():
    assert not inspect.isabstract(lua::Expression::Smaller)


def test_lua::expression::smaller_constructor_exists():
    assert callable(lua::Expression::Smaller.__init__)


def test_lua::expression::smaller_constructor_args():
    sig = inspect.signature(lua::Expression::Smaller.__init__)
    params = list(sig.parameters.keys())



def test_lua::expression::callmemberfunction_is_not_abstract():
    assert not inspect.isabstract(lua::Expression::CallMemberFunction)


def test_lua::expression::callmemberfunction_constructor_exists():
    assert callable(lua::Expression::CallMemberFunction.__init__)


def test_lua::expression::callmemberfunction_constructor_args():
    sig = inspect.signature(lua::Expression::CallMemberFunction.__init__)
    params = list(sig.parameters.keys())
    assert "memberFunctionName" in params, "Missing parameter 'memberFunctionName'"

def test_lua::expression::callmemberfunction_has_memberFunctionName():
    assert hasattr(lua::Expression::CallMemberFunction, "memberFunctionName")
    descriptor = None
    for klass in lua::Expression::CallMemberFunction.__mro__:
        if "memberFunctionName" in klass.__dict__:
            descriptor = klass.__dict__["memberFunctionName"]
            break
    assert isinstance(descriptor, property)



def test_lua::expression::varargs_is_not_abstract():
    assert not inspect.isabstract(lua::Expression::VarArgs)


def test_lua::expression::varargs_constructor_exists():
    assert callable(lua::Expression::VarArgs.__init__)


def test_lua::expression::varargs_constructor_args():
    sig = inspect.signature(lua::Expression::VarArgs.__init__)
    params = list(sig.parameters.keys())



def test_lua::expression::or_is_not_abstract():
    assert not inspect.isabstract(lua::Expression::Or)


def test_lua::expression::or_constructor_exists():
    assert callable(lua::Expression::Or.__init__)


def test_lua::expression::or_constructor_args():
    sig = inspect.signature(lua::Expression::Or.__init__)
    params = list(sig.parameters.keys())



def test_lua::expression::and_is_not_abstract():
    assert not inspect.isabstract(lua::Expression::And)


def test_lua::expression::and_constructor_exists():
    assert callable(lua::Expression::And.__init__)


def test_lua::expression::and_constructor_args():
    sig = inspect.signature(lua::Expression::And.__init__)
    params = list(sig.parameters.keys())



def test_lua::expression::function_is_not_abstract():
    assert not inspect.isabstract(lua::Expression::Function)


def test_lua::expression::function_constructor_exists():
    assert callable(lua::Expression::Function.__init__)


def test_lua::expression::function_constructor_args():
    sig = inspect.signature(lua::Expression::Function.__init__)
    params = list(sig.parameters.keys())



def test_lua::expression::tableconstructor_is_not_abstract():
    assert not inspect.isabstract(lua::Expression::TableConstructor)


def test_lua::expression::tableconstructor_constructor_exists():
    assert callable(lua::Expression::TableConstructor.__init__)


def test_lua::expression::tableconstructor_constructor_args():
    sig = inspect.signature(lua::Expression::TableConstructor.__init__)
    params = list(sig.parameters.keys())



def test_lua::expression::concatenation_is_not_abstract():
    assert not inspect.isabstract(lua::Expression::Concatenation)


def test_lua::expression::concatenation_constructor_exists():
    assert callable(lua::Expression::Concatenation.__init__)


def test_lua::expression::concatenation_constructor_args():
    sig = inspect.signature(lua::Expression::Concatenation.__init__)
    params = list(sig.parameters.keys())



def test_lua::expression::callfunction_is_not_abstract():
    assert not inspect.isabstract(lua::Expression::CallFunction)


def test_lua::expression::callfunction_constructor_exists():
    assert callable(lua::Expression::CallFunction.__init__)


def test_lua::expression::callfunction_constructor_args():
    sig = inspect.signature(lua::Expression::CallFunction.__init__)
    params = list(sig.parameters.keys())



def test_lua::expression::plus_is_not_abstract():
    assert not inspect.isabstract(lua::Expression::Plus)


def test_lua::expression::plus_constructor_exists():
    assert callable(lua::Expression::Plus.__init__)


def test_lua::expression::plus_constructor_args():
    sig = inspect.signature(lua::Expression::Plus.__init__)
    params = list(sig.parameters.keys())



def test_lua::expression::larger::equal_is_not_abstract():
    assert not inspect.isabstract(lua::Expression::Larger::Equal)


def test_lua::expression::larger::equal_constructor_exists():
    assert callable(lua::Expression::Larger::Equal.__init__)


def test_lua::expression::larger::equal_constructor_args():
    sig = inspect.signature(lua::Expression::Larger::Equal.__init__)
    params = list(sig.parameters.keys())



def test_lua::expression::string_is_not_abstract():
    assert not inspect.isabstract(lua::Expression::String)


def test_lua::expression::string_constructor_exists():
    assert callable(lua::Expression::String.__init__)


def test_lua::expression::string_constructor_args():
    sig = inspect.signature(lua::Expression::String.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_lua::expression::string_has_value():
    assert hasattr(lua::Expression::String, "value")
    descriptor = None
    for klass in lua::Expression::String.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_lua::expression::minus_is_not_abstract():
    assert not inspect.isabstract(lua::Expression::Minus)


def test_lua::expression::minus_constructor_exists():
    assert callable(lua::Expression::Minus.__init__)


def test_lua::expression::minus_constructor_args():
    sig = inspect.signature(lua::Expression::Minus.__init__)
    params = list(sig.parameters.keys())



def test_lua::expression::smaller::equal_is_not_abstract():
    assert not inspect.isabstract(lua::Expression::Smaller::Equal)


def test_lua::expression::smaller::equal_constructor_exists():
    assert callable(lua::Expression::Smaller::Equal.__init__)


def test_lua::expression::smaller::equal_constructor_args():
    sig = inspect.signature(lua::Expression::Smaller::Equal.__init__)
    params = list(sig.parameters.keys())



def test_lua::expression::nil_is_not_abstract():
    assert not inspect.isabstract(lua::Expression::Nil)


def test_lua::expression::nil_constructor_exists():
    assert callable(lua::Expression::Nil.__init__)


def test_lua::expression::nil_constructor_args():
    sig = inspect.signature(lua::Expression::Nil.__init__)
    params = list(sig.parameters.keys())



def test_statement::functioncallorassignment_is_not_abstract():
    assert not inspect.isabstract(Statement::FunctioncallOrAssignment)


def test_statement::functioncallorassignment_constructor_exists():
    assert callable(Statement::FunctioncallOrAssignment.__init__)


def test_statement::functioncallorassignment_constructor_args():
    sig = inspect.signature(Statement::FunctioncallOrAssignment.__init__)
    params = list(sig.parameters.keys())



def test_lua::statement::assignment_is_not_abstract():
    assert not inspect.isabstract(lua::Statement::Assignment)


def test_lua::statement::assignment_constructor_exists():
    assert callable(lua::Statement::Assignment.__init__)


def test_lua::statement::assignment_constructor_args():
    sig = inspect.signature(lua::Statement::Assignment.__init__)
    params = list(sig.parameters.keys())



def test_lua::statement::callfunction_is_not_abstract():
    assert not inspect.isabstract(lua::Statement::CallFunction)


def test_lua::statement::callfunction_constructor_exists():
    assert callable(lua::Statement::CallFunction.__init__)


def test_lua::statement::callfunction_constructor_args():
    sig = inspect.signature(lua::Statement::CallFunction.__init__)
    params = list(sig.parameters.keys())



def test_lua::statement::callmemberfunction_is_not_abstract():
    assert not inspect.isabstract(lua::Statement::CallMemberFunction)


def test_lua::statement::callmemberfunction_constructor_exists():
    assert callable(lua::Statement::CallMemberFunction.__init__)


def test_lua::statement::callmemberfunction_constructor_args():
    sig = inspect.signature(lua::Statement::CallMemberFunction.__init__)
    params = list(sig.parameters.keys())
    assert "memberFunctionName" in params, "Missing parameter 'memberFunctionName'"

def test_lua::statement::callmemberfunction_has_memberFunctionName():
    assert hasattr(lua::Statement::CallMemberFunction, "memberFunctionName")
    descriptor = None
    for klass in lua::Statement::CallMemberFunction.__mro__:
        if "memberFunctionName" in klass.__dict__:
            descriptor = klass.__dict__["memberFunctionName"]
            break
    assert isinstance(descriptor, property)



def test_lua::statement::if::then::else::elseifpart_is_not_abstract():
    assert not inspect.isabstract(lua::Statement::If::Then::Else::ElseIfPart)


def test_lua::statement::if::then::else::elseifpart_constructor_exists():
    assert callable(lua::Statement::If::Then::Else::ElseIfPart.__init__)


def test_lua::statement::if::then::else::elseifpart_constructor_args():
    sig = inspect.signature(lua::Statement::If::Then::Else::ElseIfPart.__init__)
    params = list(sig.parameters.keys())



def test_lua::expression_is_not_abstract():
    assert not inspect.isabstract(lua::Expression)


def test_lua::expression_constructor_exists():
    assert callable(lua::Expression.__init__)


def test_lua::expression_constructor_args():
    sig = inspect.signature(lua::Expression.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_lua::statement::functioncallorassignment_is_not_abstract():
    assert not inspect.isabstract(lua::Statement::FunctioncallOrAssignment)


def test_lua::statement::functioncallorassignment_constructor_exists():
    assert callable(lua::Statement::FunctioncallOrAssignment.__init__)


def test_lua::statement::functioncallorassignment_constructor_args():
    sig = inspect.signature(lua::Statement::FunctioncallOrAssignment.__init__)
    params = list(sig.parameters.keys())



def test_lua::statement::for::numeric_is_not_abstract():
    assert not inspect.isabstract(lua::Statement::For::Numeric)


def test_lua::statement::for::numeric_constructor_exists():
    assert callable(lua::Statement::For::Numeric.__init__)


def test_lua::statement::for::numeric_constructor_args():
    sig = inspect.signature(lua::Statement::For::Numeric.__init__)
    params = list(sig.parameters.keys())
    assert "iteratorName" in params, "Missing parameter 'iteratorName'"

def test_lua::statement::for::numeric_has_iteratorName():
    assert hasattr(lua::Statement::For::Numeric, "iteratorName")
    descriptor = None
    for klass in lua::Statement::For::Numeric.__mro__:
        if "iteratorName" in klass.__dict__:
            descriptor = klass.__dict__["iteratorName"]
            break
    assert isinstance(descriptor, property)



def test_lua::statement::local::variable::declaration_is_not_abstract():
    assert not inspect.isabstract(lua::Statement::Local::Variable::Declaration)


def test_lua::statement::local::variable::declaration_constructor_exists():
    assert callable(lua::Statement::Local::Variable::Declaration.__init__)


def test_lua::statement::local::variable::declaration_constructor_args():
    sig = inspect.signature(lua::Statement::Local::Variable::Declaration.__init__)
    params = list(sig.parameters.keys())
    assert "variableNames" in params, "Missing parameter 'variableNames'"

def test_lua::statement::local::variable::declaration_has_variableNames():
    assert hasattr(lua::Statement::Local::Variable::Declaration, "variableNames")
    descriptor = None
    for klass in lua::Statement::Local::Variable::Declaration.__mro__:
        if "variableNames" in klass.__dict__:
            descriptor = klass.__dict__["variableNames"]
            break
    assert isinstance(descriptor, property)



def test_lua::statement::while_is_not_abstract():
    assert not inspect.isabstract(lua::Statement::While)


def test_lua::statement::while_constructor_exists():
    assert callable(lua::Statement::While.__init__)


def test_lua::statement::while_constructor_args():
    sig = inspect.signature(lua::Statement::While.__init__)
    params = list(sig.parameters.keys())



def test_lua::statement::if::then::else_is_not_abstract():
    assert not inspect.isabstract(lua::Statement::If::Then::Else)


def test_lua::statement::if::then::else_constructor_exists():
    assert callable(lua::Statement::If::Then::Else.__init__)


def test_lua::statement::if::then::else_constructor_args():
    sig = inspect.signature(lua::Statement::If::Then::Else.__init__)
    params = list(sig.parameters.keys())



def test_lua::statement::repeat_is_not_abstract():
    assert not inspect.isabstract(lua::Statement::Repeat)


def test_lua::statement::repeat_constructor_exists():
    assert callable(lua::Statement::Repeat.__init__)


def test_lua::statement::repeat_constructor_args():
    sig = inspect.signature(lua::Statement::Repeat.__init__)
    params = list(sig.parameters.keys())



def test_lua::statement::globalfunction::declaration_is_not_abstract():
    assert not inspect.isabstract(lua::Statement::GlobalFunction::Declaration)


def test_lua::statement::globalfunction::declaration_constructor_exists():
    assert callable(lua::Statement::GlobalFunction::Declaration.__init__)


def test_lua::statement::globalfunction::declaration_constructor_args():
    sig = inspect.signature(lua::Statement::GlobalFunction::Declaration.__init__)
    params = list(sig.parameters.keys())
    assert "functionName" in params, "Missing parameter 'functionName'"
    assert "prefix" in params, "Missing parameter 'prefix'"

def test_lua::statement::globalfunction::declaration_has_functionName():
    assert hasattr(lua::Statement::GlobalFunction::Declaration, "functionName")
    descriptor = None
    for klass in lua::Statement::GlobalFunction::Declaration.__mro__:
        if "functionName" in klass.__dict__:
            descriptor = klass.__dict__["functionName"]
            break
    assert isinstance(descriptor, property)

def test_lua::statement::globalfunction::declaration_has_prefix():
    assert hasattr(lua::Statement::GlobalFunction::Declaration, "prefix")
    descriptor = None
    for klass in lua::Statement::GlobalFunction::Declaration.__mro__:
        if "prefix" in klass.__dict__:
            descriptor = klass.__dict__["prefix"]
            break
    assert isinstance(descriptor, property)



def test_lua::statement::for::generic_is_not_abstract():
    assert not inspect.isabstract(lua::Statement::For::Generic)


def test_lua::statement::for::generic_constructor_exists():
    assert callable(lua::Statement::For::Generic.__init__)


def test_lua::statement::for::generic_constructor_args():
    sig = inspect.signature(lua::Statement::For::Generic.__init__)
    params = list(sig.parameters.keys())
    assert "names" in params, "Missing parameter 'names'"

def test_lua::statement::for::generic_has_names():
    assert hasattr(lua::Statement::For::Generic, "names")
    descriptor = None
    for klass in lua::Statement::For::Generic.__mro__:
        if "names" in klass.__dict__:
            descriptor = klass.__dict__["names"]
            break
    assert isinstance(descriptor, property)



def test_lua::statement::localfunction::declaration_is_not_abstract():
    assert not inspect.isabstract(lua::Statement::LocalFunction::Declaration)


def test_lua::statement::localfunction::declaration_constructor_exists():
    assert callable(lua::Statement::LocalFunction::Declaration.__init__)


def test_lua::statement::localfunction::declaration_constructor_args():
    sig = inspect.signature(lua::Statement::LocalFunction::Declaration.__init__)
    params = list(sig.parameters.keys())
    assert "functionName" in params, "Missing parameter 'functionName'"

def test_lua::statement::localfunction::declaration_has_functionName():
    assert hasattr(lua::Statement::LocalFunction::Declaration, "functionName")
    descriptor = None
    for klass in lua::Statement::LocalFunction::Declaration.__mro__:
        if "functionName" in klass.__dict__:
            descriptor = klass.__dict__["functionName"]
            break
    assert isinstance(descriptor, property)



def test_lua::statement::block_is_not_abstract():
    assert not inspect.isabstract(lua::Statement::Block)


def test_lua::statement::block_constructor_exists():
    assert callable(lua::Statement::Block.__init__)


def test_lua::statement::block_constructor_args():
    sig = inspect.signature(lua::Statement::Block.__init__)
    params = list(sig.parameters.keys())



def test_laststatement_is_not_abstract():
    assert not inspect.isabstract(LastStatement)


def test_laststatement_constructor_exists():
    assert callable(LastStatement.__init__)


def test_laststatement_constructor_args():
    sig = inspect.signature(LastStatement.__init__)
    params = list(sig.parameters.keys())



def test_lua::laststatement::break_is_not_abstract():
    assert not inspect.isabstract(lua::LastStatement::Break)


def test_lua::laststatement::break_constructor_exists():
    assert callable(lua::LastStatement::Break.__init__)


def test_lua::laststatement::break_constructor_args():
    sig = inspect.signature(lua::LastStatement::Break.__init__)
    params = list(sig.parameters.keys())



def test_lua::laststatement::return_is_not_abstract():
    assert not inspect.isabstract(lua::LastStatement::Return)


def test_lua::laststatement::return_constructor_exists():
    assert callable(lua::LastStatement::Return.__init__)


def test_lua::laststatement::return_constructor_args():
    sig = inspect.signature(lua::LastStatement::Return.__init__)
    params = list(sig.parameters.keys())



def test_lua::laststatement_is_not_abstract():
    assert not inspect.isabstract(lua::LastStatement)


def test_lua::laststatement_constructor_exists():
    assert callable(lua::LastStatement.__init__)


def test_lua::laststatement_constructor_args():
    sig = inspect.signature(lua::LastStatement.__init__)
    params = list(sig.parameters.keys())



def test_lua::statement_is_not_abstract():
    assert not inspect.isabstract(lua::Statement)


def test_lua::statement_constructor_exists():
    assert callable(lua::Statement.__init__)


def test_lua::statement_constructor_args():
    sig = inspect.signature(lua::Statement.__init__)
    params = list(sig.parameters.keys())



def test_chunk_is_not_abstract():
    assert not inspect.isabstract(Chunk)


def test_chunk_constructor_exists():
    assert callable(Chunk.__init__)


def test_chunk_constructor_args():
    sig = inspect.signature(Chunk.__init__)
    params = list(sig.parameters.keys())



def test_lua::block_is_not_abstract():
    assert not inspect.isabstract(lua::Block)


def test_lua::block_constructor_exists():
    assert callable(lua::Block.__init__)


def test_lua::block_constructor_args():
    sig = inspect.signature(lua::Block.__init__)
    params = list(sig.parameters.keys())



def test_lua::chunk_is_not_abstract():
    assert not inspect.isabstract(lua::Chunk)


def test_lua::chunk_constructor_exists():
    assert callable(lua::Chunk.__init__)


def test_lua::chunk_constructor_args():
    sig = inspect.signature(lua::Chunk.__init__)
    params = list(sig.parameters.keys())


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
lua::Functioncall::Arguments_strategy = st.builds(
    lua::Functioncall::Arguments,
)
lua::Field_strategy = st.builds(
    lua::Field,
)
LastStatement::Return_strategy = st.builds(
    LastStatement::Return,
)
lua::LastStatement::ReturnWithValue_strategy = st.builds(
    lua::LastStatement::ReturnWithValue,
)
Field_strategy = st.builds(
    Field,
)
lua::Field::AddEntryToTable_strategy = st.builds(
    lua::Field::AddEntryToTable,
    key=
        safe_text
)
lua::Field::AppendEntryToTable_strategy = st.builds(
    lua::Field::AppendEntryToTable,
)
lua::Field::AddEntryToTable::Brackets_strategy = st.builds(
    lua::Field::AddEntryToTable::Brackets,
)
lua::Function_strategy = st.builds(
    lua::Function,
    varArgs=
        st.booleans(),
    parameters=
        safe_text
)
Expression_strategy = st.builds(
    Expression,
)
lua::Expression::True_strategy = st.builds(
    lua::Expression::True,
)
lua::Expression::Negate_strategy = st.builds(
    lua::Expression::Negate,
)
lua::Expression::Invert_strategy = st.builds(
    lua::Expression::Invert,
)
lua::Expression::Exponentiation_strategy = st.builds(
    lua::Expression::Exponentiation,
)
lua::Expression::Division_strategy = st.builds(
    lua::Expression::Division,
)
lua::Expression::Equal_strategy = st.builds(
    lua::Expression::Equal,
)
lua::Expression::Length_strategy = st.builds(
    lua::Expression::Length,
)
lua::Expression::False_strategy = st.builds(
    lua::Expression::False,
)
lua::Expression::Not::Equal_strategy = st.builds(
    lua::Expression::Not::Equal,
)
lua::Expression::Larger_strategy = st.builds(
    lua::Expression::Larger,
)
lua::Expression::Modulo_strategy = st.builds(
    lua::Expression::Modulo,
)
lua::Expression::Multiplication_strategy = st.builds(
    lua::Expression::Multiplication,
)
lua::Expression::AccessArray_strategy = st.builds(
    lua::Expression::AccessArray,
)
lua::Expression::AccessMember_strategy = st.builds(
    lua::Expression::AccessMember,
    memberName=
        safe_text
)
lua::Expression::Number_strategy = st.builds(
    lua::Expression::Number,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
lua::Expression::VariableName_strategy = st.builds(
    lua::Expression::VariableName,
    variable=
        safe_text
)
lua::Expression::Smaller_strategy = st.builds(
    lua::Expression::Smaller,
)
lua::Expression::CallMemberFunction_strategy = st.builds(
    lua::Expression::CallMemberFunction,
    memberFunctionName=
        safe_text
)
lua::Expression::VarArgs_strategy = st.builds(
    lua::Expression::VarArgs,
)
lua::Expression::Or_strategy = st.builds(
    lua::Expression::Or,
)
lua::Expression::And_strategy = st.builds(
    lua::Expression::And,
)
lua::Expression::Function_strategy = st.builds(
    lua::Expression::Function,
)
lua::Expression::TableConstructor_strategy = st.builds(
    lua::Expression::TableConstructor,
)
lua::Expression::Concatenation_strategy = st.builds(
    lua::Expression::Concatenation,
)
lua::Expression::CallFunction_strategy = st.builds(
    lua::Expression::CallFunction,
)
lua::Expression::Plus_strategy = st.builds(
    lua::Expression::Plus,
)
lua::Expression::Larger::Equal_strategy = st.builds(
    lua::Expression::Larger::Equal,
)
lua::Expression::String_strategy = st.builds(
    lua::Expression::String,
    value=
        safe_text
)
lua::Expression::Minus_strategy = st.builds(
    lua::Expression::Minus,
)
lua::Expression::Smaller::Equal_strategy = st.builds(
    lua::Expression::Smaller::Equal,
)
lua::Expression::Nil_strategy = st.builds(
    lua::Expression::Nil,
)
Statement::FunctioncallOrAssignment_strategy = st.builds(
    Statement::FunctioncallOrAssignment,
)
lua::Statement::Assignment_strategy = st.builds(
    lua::Statement::Assignment,
)
lua::Statement::CallFunction_strategy = st.builds(
    lua::Statement::CallFunction,
)
lua::Statement::CallMemberFunction_strategy = st.builds(
    lua::Statement::CallMemberFunction,
    memberFunctionName=
        safe_text
)
lua::Statement::If::Then::Else::ElseIfPart_strategy = st.builds(
    lua::Statement::If::Then::Else::ElseIfPart,
)
lua::Expression_strategy = st.builds(
    lua::Expression,
)
Statement_strategy = st.builds(
    Statement,
)
lua::Statement::FunctioncallOrAssignment_strategy = st.builds(
    lua::Statement::FunctioncallOrAssignment,
)
lua::Statement::For::Numeric_strategy = st.builds(
    lua::Statement::For::Numeric,
    iteratorName=
        safe_text
)
lua::Statement::Local::Variable::Declaration_strategy = st.builds(
    lua::Statement::Local::Variable::Declaration,
    variableNames=
        safe_text
)
lua::Statement::While_strategy = st.builds(
    lua::Statement::While,
)
lua::Statement::If::Then::Else_strategy = st.builds(
    lua::Statement::If::Then::Else,
)
lua::Statement::Repeat_strategy = st.builds(
    lua::Statement::Repeat,
)
lua::Statement::GlobalFunction::Declaration_strategy = st.builds(
    lua::Statement::GlobalFunction::Declaration,
    functionName=
        safe_text,
    prefix=
        safe_text
)
lua::Statement::For::Generic_strategy = st.builds(
    lua::Statement::For::Generic,
    names=
        safe_text
)
lua::Statement::LocalFunction::Declaration_strategy = st.builds(
    lua::Statement::LocalFunction::Declaration,
    functionName=
        safe_text
)
lua::Statement::Block_strategy = st.builds(
    lua::Statement::Block,
)
LastStatement_strategy = st.builds(
    LastStatement,
)
lua::LastStatement::Break_strategy = st.builds(
    lua::LastStatement::Break,
)
lua::LastStatement::Return_strategy = st.builds(
    lua::LastStatement::Return,
)
lua::LastStatement_strategy = st.builds(
    lua::LastStatement,
)
lua::Statement_strategy = st.builds(
    lua::Statement,
)
Chunk_strategy = st.builds(
    Chunk,
)
lua::Block_strategy = st.builds(
    lua::Block,
)
lua::Chunk_strategy = st.builds(
    lua::Chunk,
)

@given(instance=lua::Functioncall::Arguments_strategy)
@settings(max_examples=50)
def test_lua::functioncall::arguments_instantiation(instance):
    assert isinstance(instance, lua::Functioncall::Arguments)

@given(instance=lua::Field_strategy)
@settings(max_examples=50)
def test_lua::field_instantiation(instance):
    assert isinstance(instance, lua::Field)

@given(instance=LastStatement::Return_strategy)
@settings(max_examples=50)
def test_laststatement::return_instantiation(instance):
    assert isinstance(instance, LastStatement::Return)

@given(instance=lua::LastStatement::ReturnWithValue_strategy)
@settings(max_examples=50)
def test_lua::laststatement::returnwithvalue_instantiation(instance):
    assert isinstance(instance, lua::LastStatement::ReturnWithValue)

@given(instance=Field_strategy)
@settings(max_examples=50)
def test_field_instantiation(instance):
    assert isinstance(instance, Field)

@given(instance=lua::Field::AddEntryToTable_strategy)
@settings(max_examples=50)
def test_lua::field::addentrytotable_instantiation(instance):
    assert isinstance(instance, lua::Field::AddEntryToTable)

@given(instance=lua::Field::AddEntryToTable_strategy)
def test_lua::field::addentrytotable_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=lua::Field::AddEntryToTable_strategy)
def test_lua::field::addentrytotable_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=lua::Field::AppendEntryToTable_strategy)
@settings(max_examples=50)
def test_lua::field::appendentrytotable_instantiation(instance):
    assert isinstance(instance, lua::Field::AppendEntryToTable)

@given(instance=lua::Field::AddEntryToTable::Brackets_strategy)
@settings(max_examples=50)
def test_lua::field::addentrytotable::brackets_instantiation(instance):
    assert isinstance(instance, lua::Field::AddEntryToTable::Brackets)

@given(instance=lua::Function_strategy)
@settings(max_examples=50)
def test_lua::function_instantiation(instance):
    assert isinstance(instance, lua::Function)

@given(instance=lua::Function_strategy)
def test_lua::function_varArgs_type(instance):
    assert isinstance(instance.varArgs, bool)


@given(instance=lua::Function_strategy)
def test_lua::function_varArgs_setter(instance):
    original = instance.varArgs
    instance.varArgs = original
    assert instance.varArgs == original

@given(instance=lua::Function_strategy)
def test_lua::function_parameters_type(instance):
    assert isinstance(instance.parameters, str)


@given(instance=lua::Function_strategy)
def test_lua::function_parameters_setter(instance):
    original = instance.parameters
    instance.parameters = original
    assert instance.parameters == original

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=lua::Expression::True_strategy)
@settings(max_examples=50)
def test_lua::expression::true_instantiation(instance):
    assert isinstance(instance, lua::Expression::True)

@given(instance=lua::Expression::Negate_strategy)
@settings(max_examples=50)
def test_lua::expression::negate_instantiation(instance):
    assert isinstance(instance, lua::Expression::Negate)

@given(instance=lua::Expression::Invert_strategy)
@settings(max_examples=50)
def test_lua::expression::invert_instantiation(instance):
    assert isinstance(instance, lua::Expression::Invert)

@given(instance=lua::Expression::Exponentiation_strategy)
@settings(max_examples=50)
def test_lua::expression::exponentiation_instantiation(instance):
    assert isinstance(instance, lua::Expression::Exponentiation)

@given(instance=lua::Expression::Division_strategy)
@settings(max_examples=50)
def test_lua::expression::division_instantiation(instance):
    assert isinstance(instance, lua::Expression::Division)

@given(instance=lua::Expression::Equal_strategy)
@settings(max_examples=50)
def test_lua::expression::equal_instantiation(instance):
    assert isinstance(instance, lua::Expression::Equal)

@given(instance=lua::Expression::Length_strategy)
@settings(max_examples=50)
def test_lua::expression::length_instantiation(instance):
    assert isinstance(instance, lua::Expression::Length)

@given(instance=lua::Expression::False_strategy)
@settings(max_examples=50)
def test_lua::expression::false_instantiation(instance):
    assert isinstance(instance, lua::Expression::False)

@given(instance=lua::Expression::Not::Equal_strategy)
@settings(max_examples=50)
def test_lua::expression::not::equal_instantiation(instance):
    assert isinstance(instance, lua::Expression::Not::Equal)

@given(instance=lua::Expression::Larger_strategy)
@settings(max_examples=50)
def test_lua::expression::larger_instantiation(instance):
    assert isinstance(instance, lua::Expression::Larger)

@given(instance=lua::Expression::Modulo_strategy)
@settings(max_examples=50)
def test_lua::expression::modulo_instantiation(instance):
    assert isinstance(instance, lua::Expression::Modulo)

@given(instance=lua::Expression::Multiplication_strategy)
@settings(max_examples=50)
def test_lua::expression::multiplication_instantiation(instance):
    assert isinstance(instance, lua::Expression::Multiplication)

@given(instance=lua::Expression::AccessArray_strategy)
@settings(max_examples=50)
def test_lua::expression::accessarray_instantiation(instance):
    assert isinstance(instance, lua::Expression::AccessArray)

@given(instance=lua::Expression::AccessMember_strategy)
@settings(max_examples=50)
def test_lua::expression::accessmember_instantiation(instance):
    assert isinstance(instance, lua::Expression::AccessMember)

@given(instance=lua::Expression::AccessMember_strategy)
def test_lua::expression::accessmember_memberName_type(instance):
    assert isinstance(instance.memberName, str)


@given(instance=lua::Expression::AccessMember_strategy)
def test_lua::expression::accessmember_memberName_setter(instance):
    original = instance.memberName
    instance.memberName = original
    assert instance.memberName == original

@given(instance=lua::Expression::Number_strategy)
@settings(max_examples=50)
def test_lua::expression::number_instantiation(instance):
    assert isinstance(instance, lua::Expression::Number)

@given(instance=lua::Expression::Number_strategy)
def test_lua::expression::number_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=lua::Expression::Number_strategy)
def test_lua::expression::number_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=lua::Expression::VariableName_strategy)
@settings(max_examples=50)
def test_lua::expression::variablename_instantiation(instance):
    assert isinstance(instance, lua::Expression::VariableName)

@given(instance=lua::Expression::VariableName_strategy)
def test_lua::expression::variablename_variable_type(instance):
    assert isinstance(instance.variable, str)


@given(instance=lua::Expression::VariableName_strategy)
def test_lua::expression::variablename_variable_setter(instance):
    original = instance.variable
    instance.variable = original
    assert instance.variable == original

@given(instance=lua::Expression::Smaller_strategy)
@settings(max_examples=50)
def test_lua::expression::smaller_instantiation(instance):
    assert isinstance(instance, lua::Expression::Smaller)

@given(instance=lua::Expression::CallMemberFunction_strategy)
@settings(max_examples=50)
def test_lua::expression::callmemberfunction_instantiation(instance):
    assert isinstance(instance, lua::Expression::CallMemberFunction)

@given(instance=lua::Expression::CallMemberFunction_strategy)
def test_lua::expression::callmemberfunction_memberFunctionName_type(instance):
    assert isinstance(instance.memberFunctionName, str)


@given(instance=lua::Expression::CallMemberFunction_strategy)
def test_lua::expression::callmemberfunction_memberFunctionName_setter(instance):
    original = instance.memberFunctionName
    instance.memberFunctionName = original
    assert instance.memberFunctionName == original

@given(instance=lua::Expression::VarArgs_strategy)
@settings(max_examples=50)
def test_lua::expression::varargs_instantiation(instance):
    assert isinstance(instance, lua::Expression::VarArgs)

@given(instance=lua::Expression::Or_strategy)
@settings(max_examples=50)
def test_lua::expression::or_instantiation(instance):
    assert isinstance(instance, lua::Expression::Or)

@given(instance=lua::Expression::And_strategy)
@settings(max_examples=50)
def test_lua::expression::and_instantiation(instance):
    assert isinstance(instance, lua::Expression::And)

@given(instance=lua::Expression::Function_strategy)
@settings(max_examples=50)
def test_lua::expression::function_instantiation(instance):
    assert isinstance(instance, lua::Expression::Function)

@given(instance=lua::Expression::TableConstructor_strategy)
@settings(max_examples=50)
def test_lua::expression::tableconstructor_instantiation(instance):
    assert isinstance(instance, lua::Expression::TableConstructor)

@given(instance=lua::Expression::Concatenation_strategy)
@settings(max_examples=50)
def test_lua::expression::concatenation_instantiation(instance):
    assert isinstance(instance, lua::Expression::Concatenation)

@given(instance=lua::Expression::CallFunction_strategy)
@settings(max_examples=50)
def test_lua::expression::callfunction_instantiation(instance):
    assert isinstance(instance, lua::Expression::CallFunction)

@given(instance=lua::Expression::Plus_strategy)
@settings(max_examples=50)
def test_lua::expression::plus_instantiation(instance):
    assert isinstance(instance, lua::Expression::Plus)

@given(instance=lua::Expression::Larger::Equal_strategy)
@settings(max_examples=50)
def test_lua::expression::larger::equal_instantiation(instance):
    assert isinstance(instance, lua::Expression::Larger::Equal)

@given(instance=lua::Expression::String_strategy)
@settings(max_examples=50)
def test_lua::expression::string_instantiation(instance):
    assert isinstance(instance, lua::Expression::String)

@given(instance=lua::Expression::String_strategy)
def test_lua::expression::string_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=lua::Expression::String_strategy)
def test_lua::expression::string_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=lua::Expression::Minus_strategy)
@settings(max_examples=50)
def test_lua::expression::minus_instantiation(instance):
    assert isinstance(instance, lua::Expression::Minus)

@given(instance=lua::Expression::Smaller::Equal_strategy)
@settings(max_examples=50)
def test_lua::expression::smaller::equal_instantiation(instance):
    assert isinstance(instance, lua::Expression::Smaller::Equal)

@given(instance=lua::Expression::Nil_strategy)
@settings(max_examples=50)
def test_lua::expression::nil_instantiation(instance):
    assert isinstance(instance, lua::Expression::Nil)

@given(instance=Statement::FunctioncallOrAssignment_strategy)
@settings(max_examples=50)
def test_statement::functioncallorassignment_instantiation(instance):
    assert isinstance(instance, Statement::FunctioncallOrAssignment)

@given(instance=lua::Statement::Assignment_strategy)
@settings(max_examples=50)
def test_lua::statement::assignment_instantiation(instance):
    assert isinstance(instance, lua::Statement::Assignment)

@given(instance=lua::Statement::CallFunction_strategy)
@settings(max_examples=50)
def test_lua::statement::callfunction_instantiation(instance):
    assert isinstance(instance, lua::Statement::CallFunction)

@given(instance=lua::Statement::CallMemberFunction_strategy)
@settings(max_examples=50)
def test_lua::statement::callmemberfunction_instantiation(instance):
    assert isinstance(instance, lua::Statement::CallMemberFunction)

@given(instance=lua::Statement::CallMemberFunction_strategy)
def test_lua::statement::callmemberfunction_memberFunctionName_type(instance):
    assert isinstance(instance.memberFunctionName, str)


@given(instance=lua::Statement::CallMemberFunction_strategy)
def test_lua::statement::callmemberfunction_memberFunctionName_setter(instance):
    original = instance.memberFunctionName
    instance.memberFunctionName = original
    assert instance.memberFunctionName == original

@given(instance=lua::Statement::If::Then::Else::ElseIfPart_strategy)
@settings(max_examples=50)
def test_lua::statement::if::then::else::elseifpart_instantiation(instance):
    assert isinstance(instance, lua::Statement::If::Then::Else::ElseIfPart)

@given(instance=lua::Expression_strategy)
@settings(max_examples=50)
def test_lua::expression_instantiation(instance):
    assert isinstance(instance, lua::Expression)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=lua::Statement::FunctioncallOrAssignment_strategy)
@settings(max_examples=50)
def test_lua::statement::functioncallorassignment_instantiation(instance):
    assert isinstance(instance, lua::Statement::FunctioncallOrAssignment)

@given(instance=lua::Statement::For::Numeric_strategy)
@settings(max_examples=50)
def test_lua::statement::for::numeric_instantiation(instance):
    assert isinstance(instance, lua::Statement::For::Numeric)

@given(instance=lua::Statement::For::Numeric_strategy)
def test_lua::statement::for::numeric_iteratorName_type(instance):
    assert isinstance(instance.iteratorName, str)


@given(instance=lua::Statement::For::Numeric_strategy)
def test_lua::statement::for::numeric_iteratorName_setter(instance):
    original = instance.iteratorName
    instance.iteratorName = original
    assert instance.iteratorName == original

@given(instance=lua::Statement::Local::Variable::Declaration_strategy)
@settings(max_examples=50)
def test_lua::statement::local::variable::declaration_instantiation(instance):
    assert isinstance(instance, lua::Statement::Local::Variable::Declaration)

@given(instance=lua::Statement::Local::Variable::Declaration_strategy)
def test_lua::statement::local::variable::declaration_variableNames_type(instance):
    assert isinstance(instance.variableNames, str)


@given(instance=lua::Statement::Local::Variable::Declaration_strategy)
def test_lua::statement::local::variable::declaration_variableNames_setter(instance):
    original = instance.variableNames
    instance.variableNames = original
    assert instance.variableNames == original

@given(instance=lua::Statement::While_strategy)
@settings(max_examples=50)
def test_lua::statement::while_instantiation(instance):
    assert isinstance(instance, lua::Statement::While)

@given(instance=lua::Statement::If::Then::Else_strategy)
@settings(max_examples=50)
def test_lua::statement::if::then::else_instantiation(instance):
    assert isinstance(instance, lua::Statement::If::Then::Else)

@given(instance=lua::Statement::Repeat_strategy)
@settings(max_examples=50)
def test_lua::statement::repeat_instantiation(instance):
    assert isinstance(instance, lua::Statement::Repeat)

@given(instance=lua::Statement::GlobalFunction::Declaration_strategy)
@settings(max_examples=50)
def test_lua::statement::globalfunction::declaration_instantiation(instance):
    assert isinstance(instance, lua::Statement::GlobalFunction::Declaration)

@given(instance=lua::Statement::GlobalFunction::Declaration_strategy)
def test_lua::statement::globalfunction::declaration_functionName_type(instance):
    assert isinstance(instance.functionName, str)


@given(instance=lua::Statement::GlobalFunction::Declaration_strategy)
def test_lua::statement::globalfunction::declaration_functionName_setter(instance):
    original = instance.functionName
    instance.functionName = original
    assert instance.functionName == original

@given(instance=lua::Statement::GlobalFunction::Declaration_strategy)
def test_lua::statement::globalfunction::declaration_prefix_type(instance):
    assert isinstance(instance.prefix, str)


@given(instance=lua::Statement::GlobalFunction::Declaration_strategy)
def test_lua::statement::globalfunction::declaration_prefix_setter(instance):
    original = instance.prefix
    instance.prefix = original
    assert instance.prefix == original

@given(instance=lua::Statement::For::Generic_strategy)
@settings(max_examples=50)
def test_lua::statement::for::generic_instantiation(instance):
    assert isinstance(instance, lua::Statement::For::Generic)

@given(instance=lua::Statement::For::Generic_strategy)
def test_lua::statement::for::generic_names_type(instance):
    assert isinstance(instance.names, str)


@given(instance=lua::Statement::For::Generic_strategy)
def test_lua::statement::for::generic_names_setter(instance):
    original = instance.names
    instance.names = original
    assert instance.names == original

@given(instance=lua::Statement::LocalFunction::Declaration_strategy)
@settings(max_examples=50)
def test_lua::statement::localfunction::declaration_instantiation(instance):
    assert isinstance(instance, lua::Statement::LocalFunction::Declaration)

@given(instance=lua::Statement::LocalFunction::Declaration_strategy)
def test_lua::statement::localfunction::declaration_functionName_type(instance):
    assert isinstance(instance.functionName, str)


@given(instance=lua::Statement::LocalFunction::Declaration_strategy)
def test_lua::statement::localfunction::declaration_functionName_setter(instance):
    original = instance.functionName
    instance.functionName = original
    assert instance.functionName == original

@given(instance=lua::Statement::Block_strategy)
@settings(max_examples=50)
def test_lua::statement::block_instantiation(instance):
    assert isinstance(instance, lua::Statement::Block)

@given(instance=LastStatement_strategy)
@settings(max_examples=50)
def test_laststatement_instantiation(instance):
    assert isinstance(instance, LastStatement)

@given(instance=lua::LastStatement::Break_strategy)
@settings(max_examples=50)
def test_lua::laststatement::break_instantiation(instance):
    assert isinstance(instance, lua::LastStatement::Break)

@given(instance=lua::LastStatement::Return_strategy)
@settings(max_examples=50)
def test_lua::laststatement::return_instantiation(instance):
    assert isinstance(instance, lua::LastStatement::Return)

@given(instance=lua::LastStatement_strategy)
@settings(max_examples=50)
def test_lua::laststatement_instantiation(instance):
    assert isinstance(instance, lua::LastStatement)

@given(instance=lua::Statement_strategy)
@settings(max_examples=50)
def test_lua::statement_instantiation(instance):
    assert isinstance(instance, lua::Statement)

@given(instance=Chunk_strategy)
@settings(max_examples=50)
def test_chunk_instantiation(instance):
    assert isinstance(instance, Chunk)

@given(instance=lua::Block_strategy)
@settings(max_examples=50)
def test_lua::block_instantiation(instance):
    assert isinstance(instance, lua::Block)

@given(instance=lua::Chunk_strategy)
@settings(max_examples=50)
def test_lua::chunk_instantiation(instance):
    assert isinstance(instance, lua::Chunk)
