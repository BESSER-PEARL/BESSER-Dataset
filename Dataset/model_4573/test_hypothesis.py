import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    LastStatement_Return,
    lua_LastStatement_ReturnWithValue,
    Field,
    lua_Field_AppendEntryToTable,
    lua_Field_AddEntryToTable,
    lua_Field_AddEntryToTable_Brackets,
    lua_Functioncall_Arguments,
    lua_Field,
    Expression,
    lua_Expression_Division,
    lua_Expression_CallFunction,
    lua_Expression_VarArgs,
    lua_Expression_CallMemberFunction,
    lua_Expression_TableConstructor,
    lua_Expression_Invert,
    lua_Expression_Length,
    lua_Expression_Larger_Equal,
    lua_Expression_Modulo,
    lua_Expression_And,
    lua_Expression_Multiplication,
    lua_Expression_Plus,
    lua_Expression_Larger,
    lua_Expression_False,
    lua_Expression_String,
    lua_Expression_VariableName,
    lua_Expression_True,
    lua_Expression_Function,
    lua_Expression_Equal,
    lua_Expression_Negate,
    lua_Expression_Minus,
    lua_Expression_AccessMember,
    lua_Expression_Concatenation,
    lua_Expression_Not_Equal,
    lua_Expression_Number,
    lua_Expression_Smaller_Equal,
    lua_Expression_AccessArray,
    lua_Expression_Smaller,
    lua_Expression_Exponentiation,
    lua_Expression_Or,
    lua_Expression_Nil,
    Statement_FunctioncallOrAssignment,
    lua_Statement_Assignment,
    lua_Statement_CallMemberFunction,
    lua_Statement_CallFunction,
    lua_Function,
    lua_Statement_If_Then_Else_ElseIfPart,
    lua_Expression,
    Statement,
    lua_Statement_If_Then_Else,
    lua_Statement_While,
    lua_Statement_FunctioncallOrAssignment,
    lua_Statement_GlobalFunction_Declaration,
    lua_Statement_Local_Variable_Declaration,
    lua_Statement_For_Generic,
    lua_Statement_Repeat,
    lua_Statement_LocalFunction_Declaration,
    lua_Statement_For_Numeric,
    lua_Statement_Block,
    LastStatement,
    lua_LastStatement_Break,
    lua_LastStatement_Return,
    lua_LastStatement,
    lua_Statement,
    Chunk,
    lua_Block,
    lua_Chunk,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_laststatement_return_is_not_abstract():
    assert not inspect.isabstract(LastStatement_Return)


def test_laststatement_return_constructor_exists():
    assert callable(LastStatement_Return.__init__)


def test_laststatement_return_constructor_args():
    sig = inspect.signature(LastStatement_Return.__init__)
    params = list(sig.parameters.keys())



def test_lua_laststatement_returnwithvalue_is_not_abstract():
    assert not inspect.isabstract(lua_LastStatement_ReturnWithValue)


def test_lua_laststatement_returnwithvalue_constructor_exists():
    assert callable(lua_LastStatement_ReturnWithValue.__init__)


def test_lua_laststatement_returnwithvalue_constructor_args():
    sig = inspect.signature(lua_LastStatement_ReturnWithValue.__init__)
    params = list(sig.parameters.keys())



def test_field_is_not_abstract():
    assert not inspect.isabstract(Field)


def test_field_constructor_exists():
    assert callable(Field.__init__)


def test_field_constructor_args():
    sig = inspect.signature(Field.__init__)
    params = list(sig.parameters.keys())



def test_lua_field_appendentrytotable_is_not_abstract():
    assert not inspect.isabstract(lua_Field_AppendEntryToTable)


def test_lua_field_appendentrytotable_constructor_exists():
    assert callable(lua_Field_AppendEntryToTable.__init__)


def test_lua_field_appendentrytotable_constructor_args():
    sig = inspect.signature(lua_Field_AppendEntryToTable.__init__)
    params = list(sig.parameters.keys())



def test_lua_field_addentrytotable_is_not_abstract():
    assert not inspect.isabstract(lua_Field_AddEntryToTable)


def test_lua_field_addentrytotable_constructor_exists():
    assert callable(lua_Field_AddEntryToTable.__init__)


def test_lua_field_addentrytotable_constructor_args():
    sig = inspect.signature(lua_Field_AddEntryToTable.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"

def test_lua_field_addentrytotable_has_key():
    assert hasattr(lua_Field_AddEntryToTable, "key")
    descriptor = None
    for klass in lua_Field_AddEntryToTable.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_lua_field_addentrytotable_brackets_is_not_abstract():
    assert not inspect.isabstract(lua_Field_AddEntryToTable_Brackets)


def test_lua_field_addentrytotable_brackets_constructor_exists():
    assert callable(lua_Field_AddEntryToTable_Brackets.__init__)


def test_lua_field_addentrytotable_brackets_constructor_args():
    sig = inspect.signature(lua_Field_AddEntryToTable_Brackets.__init__)
    params = list(sig.parameters.keys())



def test_lua_functioncall_arguments_is_not_abstract():
    assert not inspect.isabstract(lua_Functioncall_Arguments)


def test_lua_functioncall_arguments_constructor_exists():
    assert callable(lua_Functioncall_Arguments.__init__)


def test_lua_functioncall_arguments_constructor_args():
    sig = inspect.signature(lua_Functioncall_Arguments.__init__)
    params = list(sig.parameters.keys())



def test_lua_field_is_not_abstract():
    assert not inspect.isabstract(lua_Field)


def test_lua_field_constructor_exists():
    assert callable(lua_Field.__init__)


def test_lua_field_constructor_args():
    sig = inspect.signature(lua_Field.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_lua_expression_division_is_not_abstract():
    assert not inspect.isabstract(lua_Expression_Division)


def test_lua_expression_division_constructor_exists():
    assert callable(lua_Expression_Division.__init__)


def test_lua_expression_division_constructor_args():
    sig = inspect.signature(lua_Expression_Division.__init__)
    params = list(sig.parameters.keys())



def test_lua_expression_callfunction_is_not_abstract():
    assert not inspect.isabstract(lua_Expression_CallFunction)


def test_lua_expression_callfunction_constructor_exists():
    assert callable(lua_Expression_CallFunction.__init__)


def test_lua_expression_callfunction_constructor_args():
    sig = inspect.signature(lua_Expression_CallFunction.__init__)
    params = list(sig.parameters.keys())



def test_lua_expression_varargs_is_not_abstract():
    assert not inspect.isabstract(lua_Expression_VarArgs)


def test_lua_expression_varargs_constructor_exists():
    assert callable(lua_Expression_VarArgs.__init__)


def test_lua_expression_varargs_constructor_args():
    sig = inspect.signature(lua_Expression_VarArgs.__init__)
    params = list(sig.parameters.keys())



def test_lua_expression_callmemberfunction_is_not_abstract():
    assert not inspect.isabstract(lua_Expression_CallMemberFunction)


def test_lua_expression_callmemberfunction_constructor_exists():
    assert callable(lua_Expression_CallMemberFunction.__init__)


def test_lua_expression_callmemberfunction_constructor_args():
    sig = inspect.signature(lua_Expression_CallMemberFunction.__init__)
    params = list(sig.parameters.keys())
    assert "memberFunctionName" in params, "Missing parameter 'memberFunctionName'"

def test_lua_expression_callmemberfunction_has_memberFunctionName():
    assert hasattr(lua_Expression_CallMemberFunction, "memberFunctionName")
    descriptor = None
    for klass in lua_Expression_CallMemberFunction.__mro__:
        if "memberFunctionName" in klass.__dict__:
            descriptor = klass.__dict__["memberFunctionName"]
            break
    assert isinstance(descriptor, property)



def test_lua_expression_tableconstructor_is_not_abstract():
    assert not inspect.isabstract(lua_Expression_TableConstructor)


def test_lua_expression_tableconstructor_constructor_exists():
    assert callable(lua_Expression_TableConstructor.__init__)


def test_lua_expression_tableconstructor_constructor_args():
    sig = inspect.signature(lua_Expression_TableConstructor.__init__)
    params = list(sig.parameters.keys())



def test_lua_expression_invert_is_not_abstract():
    assert not inspect.isabstract(lua_Expression_Invert)


def test_lua_expression_invert_constructor_exists():
    assert callable(lua_Expression_Invert.__init__)


def test_lua_expression_invert_constructor_args():
    sig = inspect.signature(lua_Expression_Invert.__init__)
    params = list(sig.parameters.keys())



def test_lua_expression_length_is_not_abstract():
    assert not inspect.isabstract(lua_Expression_Length)


def test_lua_expression_length_constructor_exists():
    assert callable(lua_Expression_Length.__init__)


def test_lua_expression_length_constructor_args():
    sig = inspect.signature(lua_Expression_Length.__init__)
    params = list(sig.parameters.keys())



def test_lua_expression_larger_equal_is_not_abstract():
    assert not inspect.isabstract(lua_Expression_Larger_Equal)


def test_lua_expression_larger_equal_constructor_exists():
    assert callable(lua_Expression_Larger_Equal.__init__)


def test_lua_expression_larger_equal_constructor_args():
    sig = inspect.signature(lua_Expression_Larger_Equal.__init__)
    params = list(sig.parameters.keys())



def test_lua_expression_modulo_is_not_abstract():
    assert not inspect.isabstract(lua_Expression_Modulo)


def test_lua_expression_modulo_constructor_exists():
    assert callable(lua_Expression_Modulo.__init__)


def test_lua_expression_modulo_constructor_args():
    sig = inspect.signature(lua_Expression_Modulo.__init__)
    params = list(sig.parameters.keys())



def test_lua_expression_and_is_not_abstract():
    assert not inspect.isabstract(lua_Expression_And)


def test_lua_expression_and_constructor_exists():
    assert callable(lua_Expression_And.__init__)


def test_lua_expression_and_constructor_args():
    sig = inspect.signature(lua_Expression_And.__init__)
    params = list(sig.parameters.keys())



def test_lua_expression_multiplication_is_not_abstract():
    assert not inspect.isabstract(lua_Expression_Multiplication)


def test_lua_expression_multiplication_constructor_exists():
    assert callable(lua_Expression_Multiplication.__init__)


def test_lua_expression_multiplication_constructor_args():
    sig = inspect.signature(lua_Expression_Multiplication.__init__)
    params = list(sig.parameters.keys())



def test_lua_expression_plus_is_not_abstract():
    assert not inspect.isabstract(lua_Expression_Plus)


def test_lua_expression_plus_constructor_exists():
    assert callable(lua_Expression_Plus.__init__)


def test_lua_expression_plus_constructor_args():
    sig = inspect.signature(lua_Expression_Plus.__init__)
    params = list(sig.parameters.keys())



def test_lua_expression_larger_is_not_abstract():
    assert not inspect.isabstract(lua_Expression_Larger)


def test_lua_expression_larger_constructor_exists():
    assert callable(lua_Expression_Larger.__init__)


def test_lua_expression_larger_constructor_args():
    sig = inspect.signature(lua_Expression_Larger.__init__)
    params = list(sig.parameters.keys())



def test_lua_expression_false_is_not_abstract():
    assert not inspect.isabstract(lua_Expression_False)


def test_lua_expression_false_constructor_exists():
    assert callable(lua_Expression_False.__init__)


def test_lua_expression_false_constructor_args():
    sig = inspect.signature(lua_Expression_False.__init__)
    params = list(sig.parameters.keys())



def test_lua_expression_string_is_not_abstract():
    assert not inspect.isabstract(lua_Expression_String)


def test_lua_expression_string_constructor_exists():
    assert callable(lua_Expression_String.__init__)


def test_lua_expression_string_constructor_args():
    sig = inspect.signature(lua_Expression_String.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_lua_expression_string_has_value():
    assert hasattr(lua_Expression_String, "value")
    descriptor = None
    for klass in lua_Expression_String.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_lua_expression_variablename_is_not_abstract():
    assert not inspect.isabstract(lua_Expression_VariableName)


def test_lua_expression_variablename_constructor_exists():
    assert callable(lua_Expression_VariableName.__init__)


def test_lua_expression_variablename_constructor_args():
    sig = inspect.signature(lua_Expression_VariableName.__init__)
    params = list(sig.parameters.keys())
    assert "variable" in params, "Missing parameter 'variable'"

def test_lua_expression_variablename_has_variable():
    assert hasattr(lua_Expression_VariableName, "variable")
    descriptor = None
    for klass in lua_Expression_VariableName.__mro__:
        if "variable" in klass.__dict__:
            descriptor = klass.__dict__["variable"]
            break
    assert isinstance(descriptor, property)



def test_lua_expression_true_is_not_abstract():
    assert not inspect.isabstract(lua_Expression_True)


def test_lua_expression_true_constructor_exists():
    assert callable(lua_Expression_True.__init__)


def test_lua_expression_true_constructor_args():
    sig = inspect.signature(lua_Expression_True.__init__)
    params = list(sig.parameters.keys())



def test_lua_expression_function_is_not_abstract():
    assert not inspect.isabstract(lua_Expression_Function)


def test_lua_expression_function_constructor_exists():
    assert callable(lua_Expression_Function.__init__)


def test_lua_expression_function_constructor_args():
    sig = inspect.signature(lua_Expression_Function.__init__)
    params = list(sig.parameters.keys())



def test_lua_expression_equal_is_not_abstract():
    assert not inspect.isabstract(lua_Expression_Equal)


def test_lua_expression_equal_constructor_exists():
    assert callable(lua_Expression_Equal.__init__)


def test_lua_expression_equal_constructor_args():
    sig = inspect.signature(lua_Expression_Equal.__init__)
    params = list(sig.parameters.keys())



def test_lua_expression_negate_is_not_abstract():
    assert not inspect.isabstract(lua_Expression_Negate)


def test_lua_expression_negate_constructor_exists():
    assert callable(lua_Expression_Negate.__init__)


def test_lua_expression_negate_constructor_args():
    sig = inspect.signature(lua_Expression_Negate.__init__)
    params = list(sig.parameters.keys())



def test_lua_expression_minus_is_not_abstract():
    assert not inspect.isabstract(lua_Expression_Minus)


def test_lua_expression_minus_constructor_exists():
    assert callable(lua_Expression_Minus.__init__)


def test_lua_expression_minus_constructor_args():
    sig = inspect.signature(lua_Expression_Minus.__init__)
    params = list(sig.parameters.keys())



def test_lua_expression_accessmember_is_not_abstract():
    assert not inspect.isabstract(lua_Expression_AccessMember)


def test_lua_expression_accessmember_constructor_exists():
    assert callable(lua_Expression_AccessMember.__init__)


def test_lua_expression_accessmember_constructor_args():
    sig = inspect.signature(lua_Expression_AccessMember.__init__)
    params = list(sig.parameters.keys())
    assert "memberName" in params, "Missing parameter 'memberName'"

def test_lua_expression_accessmember_has_memberName():
    assert hasattr(lua_Expression_AccessMember, "memberName")
    descriptor = None
    for klass in lua_Expression_AccessMember.__mro__:
        if "memberName" in klass.__dict__:
            descriptor = klass.__dict__["memberName"]
            break
    assert isinstance(descriptor, property)



def test_lua_expression_concatenation_is_not_abstract():
    assert not inspect.isabstract(lua_Expression_Concatenation)


def test_lua_expression_concatenation_constructor_exists():
    assert callable(lua_Expression_Concatenation.__init__)


def test_lua_expression_concatenation_constructor_args():
    sig = inspect.signature(lua_Expression_Concatenation.__init__)
    params = list(sig.parameters.keys())



def test_lua_expression_not_equal_is_not_abstract():
    assert not inspect.isabstract(lua_Expression_Not_Equal)


def test_lua_expression_not_equal_constructor_exists():
    assert callable(lua_Expression_Not_Equal.__init__)


def test_lua_expression_not_equal_constructor_args():
    sig = inspect.signature(lua_Expression_Not_Equal.__init__)
    params = list(sig.parameters.keys())



def test_lua_expression_number_is_not_abstract():
    assert not inspect.isabstract(lua_Expression_Number)


def test_lua_expression_number_constructor_exists():
    assert callable(lua_Expression_Number.__init__)


def test_lua_expression_number_constructor_args():
    sig = inspect.signature(lua_Expression_Number.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_lua_expression_number_has_value():
    assert hasattr(lua_Expression_Number, "value")
    descriptor = None
    for klass in lua_Expression_Number.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_lua_expression_smaller_equal_is_not_abstract():
    assert not inspect.isabstract(lua_Expression_Smaller_Equal)


def test_lua_expression_smaller_equal_constructor_exists():
    assert callable(lua_Expression_Smaller_Equal.__init__)


def test_lua_expression_smaller_equal_constructor_args():
    sig = inspect.signature(lua_Expression_Smaller_Equal.__init__)
    params = list(sig.parameters.keys())



def test_lua_expression_accessarray_is_not_abstract():
    assert not inspect.isabstract(lua_Expression_AccessArray)


def test_lua_expression_accessarray_constructor_exists():
    assert callable(lua_Expression_AccessArray.__init__)


def test_lua_expression_accessarray_constructor_args():
    sig = inspect.signature(lua_Expression_AccessArray.__init__)
    params = list(sig.parameters.keys())



def test_lua_expression_smaller_is_not_abstract():
    assert not inspect.isabstract(lua_Expression_Smaller)


def test_lua_expression_smaller_constructor_exists():
    assert callable(lua_Expression_Smaller.__init__)


def test_lua_expression_smaller_constructor_args():
    sig = inspect.signature(lua_Expression_Smaller.__init__)
    params = list(sig.parameters.keys())



def test_lua_expression_exponentiation_is_not_abstract():
    assert not inspect.isabstract(lua_Expression_Exponentiation)


def test_lua_expression_exponentiation_constructor_exists():
    assert callable(lua_Expression_Exponentiation.__init__)


def test_lua_expression_exponentiation_constructor_args():
    sig = inspect.signature(lua_Expression_Exponentiation.__init__)
    params = list(sig.parameters.keys())



def test_lua_expression_or_is_not_abstract():
    assert not inspect.isabstract(lua_Expression_Or)


def test_lua_expression_or_constructor_exists():
    assert callable(lua_Expression_Or.__init__)


def test_lua_expression_or_constructor_args():
    sig = inspect.signature(lua_Expression_Or.__init__)
    params = list(sig.parameters.keys())



def test_lua_expression_nil_is_not_abstract():
    assert not inspect.isabstract(lua_Expression_Nil)


def test_lua_expression_nil_constructor_exists():
    assert callable(lua_Expression_Nil.__init__)


def test_lua_expression_nil_constructor_args():
    sig = inspect.signature(lua_Expression_Nil.__init__)
    params = list(sig.parameters.keys())



def test_statement_functioncallorassignment_is_not_abstract():
    assert not inspect.isabstract(Statement_FunctioncallOrAssignment)


def test_statement_functioncallorassignment_constructor_exists():
    assert callable(Statement_FunctioncallOrAssignment.__init__)


def test_statement_functioncallorassignment_constructor_args():
    sig = inspect.signature(Statement_FunctioncallOrAssignment.__init__)
    params = list(sig.parameters.keys())



def test_lua_statement_assignment_is_not_abstract():
    assert not inspect.isabstract(lua_Statement_Assignment)


def test_lua_statement_assignment_constructor_exists():
    assert callable(lua_Statement_Assignment.__init__)


def test_lua_statement_assignment_constructor_args():
    sig = inspect.signature(lua_Statement_Assignment.__init__)
    params = list(sig.parameters.keys())



def test_lua_statement_callmemberfunction_is_not_abstract():
    assert not inspect.isabstract(lua_Statement_CallMemberFunction)


def test_lua_statement_callmemberfunction_constructor_exists():
    assert callable(lua_Statement_CallMemberFunction.__init__)


def test_lua_statement_callmemberfunction_constructor_args():
    sig = inspect.signature(lua_Statement_CallMemberFunction.__init__)
    params = list(sig.parameters.keys())
    assert "memberFunctionName" in params, "Missing parameter 'memberFunctionName'"

def test_lua_statement_callmemberfunction_has_memberFunctionName():
    assert hasattr(lua_Statement_CallMemberFunction, "memberFunctionName")
    descriptor = None
    for klass in lua_Statement_CallMemberFunction.__mro__:
        if "memberFunctionName" in klass.__dict__:
            descriptor = klass.__dict__["memberFunctionName"]
            break
    assert isinstance(descriptor, property)



def test_lua_statement_callfunction_is_not_abstract():
    assert not inspect.isabstract(lua_Statement_CallFunction)


def test_lua_statement_callfunction_constructor_exists():
    assert callable(lua_Statement_CallFunction.__init__)


def test_lua_statement_callfunction_constructor_args():
    sig = inspect.signature(lua_Statement_CallFunction.__init__)
    params = list(sig.parameters.keys())



def test_lua_function_is_not_abstract():
    assert not inspect.isabstract(lua_Function)


def test_lua_function_constructor_exists():
    assert callable(lua_Function.__init__)


def test_lua_function_constructor_args():
    sig = inspect.signature(lua_Function.__init__)
    params = list(sig.parameters.keys())
    assert "varArgs" in params, "Missing parameter 'varArgs'"
    assert "parameters" in params, "Missing parameter 'parameters'"

def test_lua_function_has_varArgs():
    assert hasattr(lua_Function, "varArgs")
    descriptor = None
    for klass in lua_Function.__mro__:
        if "varArgs" in klass.__dict__:
            descriptor = klass.__dict__["varArgs"]
            break
    assert isinstance(descriptor, property)

def test_lua_function_has_parameters():
    assert hasattr(lua_Function, "parameters")
    descriptor = None
    for klass in lua_Function.__mro__:
        if "parameters" in klass.__dict__:
            descriptor = klass.__dict__["parameters"]
            break
    assert isinstance(descriptor, property)



def test_lua_statement_if_then_else_elseifpart_is_not_abstract():
    assert not inspect.isabstract(lua_Statement_If_Then_Else_ElseIfPart)


def test_lua_statement_if_then_else_elseifpart_constructor_exists():
    assert callable(lua_Statement_If_Then_Else_ElseIfPart.__init__)


def test_lua_statement_if_then_else_elseifpart_constructor_args():
    sig = inspect.signature(lua_Statement_If_Then_Else_ElseIfPart.__init__)
    params = list(sig.parameters.keys())



def test_lua_expression_is_not_abstract():
    assert not inspect.isabstract(lua_Expression)


def test_lua_expression_constructor_exists():
    assert callable(lua_Expression.__init__)


def test_lua_expression_constructor_args():
    sig = inspect.signature(lua_Expression.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_lua_statement_if_then_else_is_not_abstract():
    assert not inspect.isabstract(lua_Statement_If_Then_Else)


def test_lua_statement_if_then_else_constructor_exists():
    assert callable(lua_Statement_If_Then_Else.__init__)


def test_lua_statement_if_then_else_constructor_args():
    sig = inspect.signature(lua_Statement_If_Then_Else.__init__)
    params = list(sig.parameters.keys())



def test_lua_statement_while_is_not_abstract():
    assert not inspect.isabstract(lua_Statement_While)


def test_lua_statement_while_constructor_exists():
    assert callable(lua_Statement_While.__init__)


def test_lua_statement_while_constructor_args():
    sig = inspect.signature(lua_Statement_While.__init__)
    params = list(sig.parameters.keys())



def test_lua_statement_functioncallorassignment_is_not_abstract():
    assert not inspect.isabstract(lua_Statement_FunctioncallOrAssignment)


def test_lua_statement_functioncallorassignment_constructor_exists():
    assert callable(lua_Statement_FunctioncallOrAssignment.__init__)


def test_lua_statement_functioncallorassignment_constructor_args():
    sig = inspect.signature(lua_Statement_FunctioncallOrAssignment.__init__)
    params = list(sig.parameters.keys())



def test_lua_statement_globalfunction_declaration_is_not_abstract():
    assert not inspect.isabstract(lua_Statement_GlobalFunction_Declaration)


def test_lua_statement_globalfunction_declaration_constructor_exists():
    assert callable(lua_Statement_GlobalFunction_Declaration.__init__)


def test_lua_statement_globalfunction_declaration_constructor_args():
    sig = inspect.signature(lua_Statement_GlobalFunction_Declaration.__init__)
    params = list(sig.parameters.keys())
    assert "functionName" in params, "Missing parameter 'functionName'"
    assert "prefix" in params, "Missing parameter 'prefix'"

def test_lua_statement_globalfunction_declaration_has_functionName():
    assert hasattr(lua_Statement_GlobalFunction_Declaration, "functionName")
    descriptor = None
    for klass in lua_Statement_GlobalFunction_Declaration.__mro__:
        if "functionName" in klass.__dict__:
            descriptor = klass.__dict__["functionName"]
            break
    assert isinstance(descriptor, property)

def test_lua_statement_globalfunction_declaration_has_prefix():
    assert hasattr(lua_Statement_GlobalFunction_Declaration, "prefix")
    descriptor = None
    for klass in lua_Statement_GlobalFunction_Declaration.__mro__:
        if "prefix" in klass.__dict__:
            descriptor = klass.__dict__["prefix"]
            break
    assert isinstance(descriptor, property)



def test_lua_statement_local_variable_declaration_is_not_abstract():
    assert not inspect.isabstract(lua_Statement_Local_Variable_Declaration)


def test_lua_statement_local_variable_declaration_constructor_exists():
    assert callable(lua_Statement_Local_Variable_Declaration.__init__)


def test_lua_statement_local_variable_declaration_constructor_args():
    sig = inspect.signature(lua_Statement_Local_Variable_Declaration.__init__)
    params = list(sig.parameters.keys())
    assert "variableNames" in params, "Missing parameter 'variableNames'"

def test_lua_statement_local_variable_declaration_has_variableNames():
    assert hasattr(lua_Statement_Local_Variable_Declaration, "variableNames")
    descriptor = None
    for klass in lua_Statement_Local_Variable_Declaration.__mro__:
        if "variableNames" in klass.__dict__:
            descriptor = klass.__dict__["variableNames"]
            break
    assert isinstance(descriptor, property)



def test_lua_statement_for_generic_is_not_abstract():
    assert not inspect.isabstract(lua_Statement_For_Generic)


def test_lua_statement_for_generic_constructor_exists():
    assert callable(lua_Statement_For_Generic.__init__)


def test_lua_statement_for_generic_constructor_args():
    sig = inspect.signature(lua_Statement_For_Generic.__init__)
    params = list(sig.parameters.keys())
    assert "names" in params, "Missing parameter 'names'"

def test_lua_statement_for_generic_has_names():
    assert hasattr(lua_Statement_For_Generic, "names")
    descriptor = None
    for klass in lua_Statement_For_Generic.__mro__:
        if "names" in klass.__dict__:
            descriptor = klass.__dict__["names"]
            break
    assert isinstance(descriptor, property)



def test_lua_statement_repeat_is_not_abstract():
    assert not inspect.isabstract(lua_Statement_Repeat)


def test_lua_statement_repeat_constructor_exists():
    assert callable(lua_Statement_Repeat.__init__)


def test_lua_statement_repeat_constructor_args():
    sig = inspect.signature(lua_Statement_Repeat.__init__)
    params = list(sig.parameters.keys())



def test_lua_statement_localfunction_declaration_is_not_abstract():
    assert not inspect.isabstract(lua_Statement_LocalFunction_Declaration)


def test_lua_statement_localfunction_declaration_constructor_exists():
    assert callable(lua_Statement_LocalFunction_Declaration.__init__)


def test_lua_statement_localfunction_declaration_constructor_args():
    sig = inspect.signature(lua_Statement_LocalFunction_Declaration.__init__)
    params = list(sig.parameters.keys())
    assert "functionName" in params, "Missing parameter 'functionName'"

def test_lua_statement_localfunction_declaration_has_functionName():
    assert hasattr(lua_Statement_LocalFunction_Declaration, "functionName")
    descriptor = None
    for klass in lua_Statement_LocalFunction_Declaration.__mro__:
        if "functionName" in klass.__dict__:
            descriptor = klass.__dict__["functionName"]
            break
    assert isinstance(descriptor, property)



def test_lua_statement_for_numeric_is_not_abstract():
    assert not inspect.isabstract(lua_Statement_For_Numeric)


def test_lua_statement_for_numeric_constructor_exists():
    assert callable(lua_Statement_For_Numeric.__init__)


def test_lua_statement_for_numeric_constructor_args():
    sig = inspect.signature(lua_Statement_For_Numeric.__init__)
    params = list(sig.parameters.keys())
    assert "iteratorName" in params, "Missing parameter 'iteratorName'"

def test_lua_statement_for_numeric_has_iteratorName():
    assert hasattr(lua_Statement_For_Numeric, "iteratorName")
    descriptor = None
    for klass in lua_Statement_For_Numeric.__mro__:
        if "iteratorName" in klass.__dict__:
            descriptor = klass.__dict__["iteratorName"]
            break
    assert isinstance(descriptor, property)



def test_lua_statement_block_is_not_abstract():
    assert not inspect.isabstract(lua_Statement_Block)


def test_lua_statement_block_constructor_exists():
    assert callable(lua_Statement_Block.__init__)


def test_lua_statement_block_constructor_args():
    sig = inspect.signature(lua_Statement_Block.__init__)
    params = list(sig.parameters.keys())



def test_laststatement_is_not_abstract():
    assert not inspect.isabstract(LastStatement)


def test_laststatement_constructor_exists():
    assert callable(LastStatement.__init__)


def test_laststatement_constructor_args():
    sig = inspect.signature(LastStatement.__init__)
    params = list(sig.parameters.keys())



def test_lua_laststatement_break_is_not_abstract():
    assert not inspect.isabstract(lua_LastStatement_Break)


def test_lua_laststatement_break_constructor_exists():
    assert callable(lua_LastStatement_Break.__init__)


def test_lua_laststatement_break_constructor_args():
    sig = inspect.signature(lua_LastStatement_Break.__init__)
    params = list(sig.parameters.keys())



def test_lua_laststatement_return_is_not_abstract():
    assert not inspect.isabstract(lua_LastStatement_Return)


def test_lua_laststatement_return_constructor_exists():
    assert callable(lua_LastStatement_Return.__init__)


def test_lua_laststatement_return_constructor_args():
    sig = inspect.signature(lua_LastStatement_Return.__init__)
    params = list(sig.parameters.keys())



def test_lua_laststatement_is_not_abstract():
    assert not inspect.isabstract(lua_LastStatement)


def test_lua_laststatement_constructor_exists():
    assert callable(lua_LastStatement.__init__)


def test_lua_laststatement_constructor_args():
    sig = inspect.signature(lua_LastStatement.__init__)
    params = list(sig.parameters.keys())



def test_lua_statement_is_not_abstract():
    assert not inspect.isabstract(lua_Statement)


def test_lua_statement_constructor_exists():
    assert callable(lua_Statement.__init__)


def test_lua_statement_constructor_args():
    sig = inspect.signature(lua_Statement.__init__)
    params = list(sig.parameters.keys())



def test_chunk_is_not_abstract():
    assert not inspect.isabstract(Chunk)


def test_chunk_constructor_exists():
    assert callable(Chunk.__init__)


def test_chunk_constructor_args():
    sig = inspect.signature(Chunk.__init__)
    params = list(sig.parameters.keys())



def test_lua_block_is_not_abstract():
    assert not inspect.isabstract(lua_Block)


def test_lua_block_constructor_exists():
    assert callable(lua_Block.__init__)


def test_lua_block_constructor_args():
    sig = inspect.signature(lua_Block.__init__)
    params = list(sig.parameters.keys())



def test_lua_chunk_is_not_abstract():
    assert not inspect.isabstract(lua_Chunk)


def test_lua_chunk_constructor_exists():
    assert callable(lua_Chunk.__init__)


def test_lua_chunk_constructor_args():
    sig = inspect.signature(lua_Chunk.__init__)
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
LastStatement_Return_strategy = st.builds(
    LastStatement_Return,
)
lua_LastStatement_ReturnWithValue_strategy = st.builds(
    lua_LastStatement_ReturnWithValue,
)
Field_strategy = st.builds(
    Field,
)
lua_Field_AppendEntryToTable_strategy = st.builds(
    lua_Field_AppendEntryToTable,
)
lua_Field_AddEntryToTable_strategy = st.builds(
    lua_Field_AddEntryToTable,
    key=
        safe_text
)
lua_Field_AddEntryToTable_Brackets_strategy = st.builds(
    lua_Field_AddEntryToTable_Brackets,
)
lua_Functioncall_Arguments_strategy = st.builds(
    lua_Functioncall_Arguments,
)
lua_Field_strategy = st.builds(
    lua_Field,
)
Expression_strategy = st.builds(
    Expression,
)
lua_Expression_Division_strategy = st.builds(
    lua_Expression_Division,
)
lua_Expression_CallFunction_strategy = st.builds(
    lua_Expression_CallFunction,
)
lua_Expression_VarArgs_strategy = st.builds(
    lua_Expression_VarArgs,
)
lua_Expression_CallMemberFunction_strategy = st.builds(
    lua_Expression_CallMemberFunction,
    memberFunctionName=
        safe_text
)
lua_Expression_TableConstructor_strategy = st.builds(
    lua_Expression_TableConstructor,
)
lua_Expression_Invert_strategy = st.builds(
    lua_Expression_Invert,
)
lua_Expression_Length_strategy = st.builds(
    lua_Expression_Length,
)
lua_Expression_Larger_Equal_strategy = st.builds(
    lua_Expression_Larger_Equal,
)
lua_Expression_Modulo_strategy = st.builds(
    lua_Expression_Modulo,
)
lua_Expression_And_strategy = st.builds(
    lua_Expression_And,
)
lua_Expression_Multiplication_strategy = st.builds(
    lua_Expression_Multiplication,
)
lua_Expression_Plus_strategy = st.builds(
    lua_Expression_Plus,
)
lua_Expression_Larger_strategy = st.builds(
    lua_Expression_Larger,
)
lua_Expression_False_strategy = st.builds(
    lua_Expression_False,
)
lua_Expression_String_strategy = st.builds(
    lua_Expression_String,
    value=
        safe_text
)
lua_Expression_VariableName_strategy = st.builds(
    lua_Expression_VariableName,
    variable=
        safe_text
)
lua_Expression_True_strategy = st.builds(
    lua_Expression_True,
)
lua_Expression_Function_strategy = st.builds(
    lua_Expression_Function,
)
lua_Expression_Equal_strategy = st.builds(
    lua_Expression_Equal,
)
lua_Expression_Negate_strategy = st.builds(
    lua_Expression_Negate,
)
lua_Expression_Minus_strategy = st.builds(
    lua_Expression_Minus,
)
lua_Expression_AccessMember_strategy = st.builds(
    lua_Expression_AccessMember,
    memberName=
        safe_text
)
lua_Expression_Concatenation_strategy = st.builds(
    lua_Expression_Concatenation,
)
lua_Expression_Not_Equal_strategy = st.builds(
    lua_Expression_Not_Equal,
)
lua_Expression_Number_strategy = st.builds(
    lua_Expression_Number,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
lua_Expression_Smaller_Equal_strategy = st.builds(
    lua_Expression_Smaller_Equal,
)
lua_Expression_AccessArray_strategy = st.builds(
    lua_Expression_AccessArray,
)
lua_Expression_Smaller_strategy = st.builds(
    lua_Expression_Smaller,
)
lua_Expression_Exponentiation_strategy = st.builds(
    lua_Expression_Exponentiation,
)
lua_Expression_Or_strategy = st.builds(
    lua_Expression_Or,
)
lua_Expression_Nil_strategy = st.builds(
    lua_Expression_Nil,
)
Statement_FunctioncallOrAssignment_strategy = st.builds(
    Statement_FunctioncallOrAssignment,
)
lua_Statement_Assignment_strategy = st.builds(
    lua_Statement_Assignment,
)
lua_Statement_CallMemberFunction_strategy = st.builds(
    lua_Statement_CallMemberFunction,
    memberFunctionName=
        safe_text
)
lua_Statement_CallFunction_strategy = st.builds(
    lua_Statement_CallFunction,
)
lua_Function_strategy = st.builds(
    lua_Function,
    varArgs=
        st.booleans(),
    parameters=
        safe_text
)
lua_Statement_If_Then_Else_ElseIfPart_strategy = st.builds(
    lua_Statement_If_Then_Else_ElseIfPart,
)
lua_Expression_strategy = st.builds(
    lua_Expression,
)
Statement_strategy = st.builds(
    Statement,
)
lua_Statement_If_Then_Else_strategy = st.builds(
    lua_Statement_If_Then_Else,
)
lua_Statement_While_strategy = st.builds(
    lua_Statement_While,
)
lua_Statement_FunctioncallOrAssignment_strategy = st.builds(
    lua_Statement_FunctioncallOrAssignment,
)
lua_Statement_GlobalFunction_Declaration_strategy = st.builds(
    lua_Statement_GlobalFunction_Declaration,
    functionName=
        safe_text,
    prefix=
        safe_text
)
lua_Statement_Local_Variable_Declaration_strategy = st.builds(
    lua_Statement_Local_Variable_Declaration,
    variableNames=
        safe_text
)
lua_Statement_For_Generic_strategy = st.builds(
    lua_Statement_For_Generic,
    names=
        safe_text
)
lua_Statement_Repeat_strategy = st.builds(
    lua_Statement_Repeat,
)
lua_Statement_LocalFunction_Declaration_strategy = st.builds(
    lua_Statement_LocalFunction_Declaration,
    functionName=
        safe_text
)
lua_Statement_For_Numeric_strategy = st.builds(
    lua_Statement_For_Numeric,
    iteratorName=
        safe_text
)
lua_Statement_Block_strategy = st.builds(
    lua_Statement_Block,
)
LastStatement_strategy = st.builds(
    LastStatement,
)
lua_LastStatement_Break_strategy = st.builds(
    lua_LastStatement_Break,
)
lua_LastStatement_Return_strategy = st.builds(
    lua_LastStatement_Return,
)
lua_LastStatement_strategy = st.builds(
    lua_LastStatement,
)
lua_Statement_strategy = st.builds(
    lua_Statement,
)
Chunk_strategy = st.builds(
    Chunk,
)
lua_Block_strategy = st.builds(
    lua_Block,
)
lua_Chunk_strategy = st.builds(
    lua_Chunk,
)

@given(instance=LastStatement_Return_strategy)
@settings(max_examples=50)
def test_laststatement_return_instantiation(instance):
    assert isinstance(instance, LastStatement_Return)

@given(instance=lua_LastStatement_ReturnWithValue_strategy)
@settings(max_examples=50)
def test_lua_laststatement_returnwithvalue_instantiation(instance):
    assert isinstance(instance, lua_LastStatement_ReturnWithValue)

@given(instance=Field_strategy)
@settings(max_examples=50)
def test_field_instantiation(instance):
    assert isinstance(instance, Field)

@given(instance=lua_Field_AppendEntryToTable_strategy)
@settings(max_examples=50)
def test_lua_field_appendentrytotable_instantiation(instance):
    assert isinstance(instance, lua_Field_AppendEntryToTable)

@given(instance=lua_Field_AddEntryToTable_strategy)
@settings(max_examples=50)
def test_lua_field_addentrytotable_instantiation(instance):
    assert isinstance(instance, lua_Field_AddEntryToTable)



@given(instance=lua_Field_AddEntryToTable_strategy)
def test_lua_field_addentrytotable_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=lua_Field_AddEntryToTable_Brackets_strategy)
@settings(max_examples=50)
def test_lua_field_addentrytotable_brackets_instantiation(instance):
    assert isinstance(instance, lua_Field_AddEntryToTable_Brackets)

@given(instance=lua_Functioncall_Arguments_strategy)
@settings(max_examples=50)
def test_lua_functioncall_arguments_instantiation(instance):
    assert isinstance(instance, lua_Functioncall_Arguments)

@given(instance=lua_Field_strategy)
@settings(max_examples=50)
def test_lua_field_instantiation(instance):
    assert isinstance(instance, lua_Field)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=lua_Expression_Division_strategy)
@settings(max_examples=50)
def test_lua_expression_division_instantiation(instance):
    assert isinstance(instance, lua_Expression_Division)

@given(instance=lua_Expression_CallFunction_strategy)
@settings(max_examples=50)
def test_lua_expression_callfunction_instantiation(instance):
    assert isinstance(instance, lua_Expression_CallFunction)

@given(instance=lua_Expression_VarArgs_strategy)
@settings(max_examples=50)
def test_lua_expression_varargs_instantiation(instance):
    assert isinstance(instance, lua_Expression_VarArgs)

@given(instance=lua_Expression_CallMemberFunction_strategy)
@settings(max_examples=50)
def test_lua_expression_callmemberfunction_instantiation(instance):
    assert isinstance(instance, lua_Expression_CallMemberFunction)



@given(instance=lua_Expression_CallMemberFunction_strategy)
def test_lua_expression_callmemberfunction_memberFunctionName_setter(instance):
    original = instance.memberFunctionName
    instance.memberFunctionName = original
    assert instance.memberFunctionName == original

@given(instance=lua_Expression_TableConstructor_strategy)
@settings(max_examples=50)
def test_lua_expression_tableconstructor_instantiation(instance):
    assert isinstance(instance, lua_Expression_TableConstructor)

@given(instance=lua_Expression_Invert_strategy)
@settings(max_examples=50)
def test_lua_expression_invert_instantiation(instance):
    assert isinstance(instance, lua_Expression_Invert)

@given(instance=lua_Expression_Length_strategy)
@settings(max_examples=50)
def test_lua_expression_length_instantiation(instance):
    assert isinstance(instance, lua_Expression_Length)

@given(instance=lua_Expression_Larger_Equal_strategy)
@settings(max_examples=50)
def test_lua_expression_larger_equal_instantiation(instance):
    assert isinstance(instance, lua_Expression_Larger_Equal)

@given(instance=lua_Expression_Modulo_strategy)
@settings(max_examples=50)
def test_lua_expression_modulo_instantiation(instance):
    assert isinstance(instance, lua_Expression_Modulo)

@given(instance=lua_Expression_And_strategy)
@settings(max_examples=50)
def test_lua_expression_and_instantiation(instance):
    assert isinstance(instance, lua_Expression_And)

@given(instance=lua_Expression_Multiplication_strategy)
@settings(max_examples=50)
def test_lua_expression_multiplication_instantiation(instance):
    assert isinstance(instance, lua_Expression_Multiplication)

@given(instance=lua_Expression_Plus_strategy)
@settings(max_examples=50)
def test_lua_expression_plus_instantiation(instance):
    assert isinstance(instance, lua_Expression_Plus)

@given(instance=lua_Expression_Larger_strategy)
@settings(max_examples=50)
def test_lua_expression_larger_instantiation(instance):
    assert isinstance(instance, lua_Expression_Larger)

@given(instance=lua_Expression_False_strategy)
@settings(max_examples=50)
def test_lua_expression_false_instantiation(instance):
    assert isinstance(instance, lua_Expression_False)

@given(instance=lua_Expression_String_strategy)
@settings(max_examples=50)
def test_lua_expression_string_instantiation(instance):
    assert isinstance(instance, lua_Expression_String)



@given(instance=lua_Expression_String_strategy)
def test_lua_expression_string_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=lua_Expression_VariableName_strategy)
@settings(max_examples=50)
def test_lua_expression_variablename_instantiation(instance):
    assert isinstance(instance, lua_Expression_VariableName)



@given(instance=lua_Expression_VariableName_strategy)
def test_lua_expression_variablename_variable_setter(instance):
    original = instance.variable
    instance.variable = original
    assert instance.variable == original

@given(instance=lua_Expression_True_strategy)
@settings(max_examples=50)
def test_lua_expression_true_instantiation(instance):
    assert isinstance(instance, lua_Expression_True)

@given(instance=lua_Expression_Function_strategy)
@settings(max_examples=50)
def test_lua_expression_function_instantiation(instance):
    assert isinstance(instance, lua_Expression_Function)

@given(instance=lua_Expression_Equal_strategy)
@settings(max_examples=50)
def test_lua_expression_equal_instantiation(instance):
    assert isinstance(instance, lua_Expression_Equal)

@given(instance=lua_Expression_Negate_strategy)
@settings(max_examples=50)
def test_lua_expression_negate_instantiation(instance):
    assert isinstance(instance, lua_Expression_Negate)

@given(instance=lua_Expression_Minus_strategy)
@settings(max_examples=50)
def test_lua_expression_minus_instantiation(instance):
    assert isinstance(instance, lua_Expression_Minus)

@given(instance=lua_Expression_AccessMember_strategy)
@settings(max_examples=50)
def test_lua_expression_accessmember_instantiation(instance):
    assert isinstance(instance, lua_Expression_AccessMember)



@given(instance=lua_Expression_AccessMember_strategy)
def test_lua_expression_accessmember_memberName_setter(instance):
    original = instance.memberName
    instance.memberName = original
    assert instance.memberName == original

@given(instance=lua_Expression_Concatenation_strategy)
@settings(max_examples=50)
def test_lua_expression_concatenation_instantiation(instance):
    assert isinstance(instance, lua_Expression_Concatenation)

@given(instance=lua_Expression_Not_Equal_strategy)
@settings(max_examples=50)
def test_lua_expression_not_equal_instantiation(instance):
    assert isinstance(instance, lua_Expression_Not_Equal)

@given(instance=lua_Expression_Number_strategy)
@settings(max_examples=50)
def test_lua_expression_number_instantiation(instance):
    assert isinstance(instance, lua_Expression_Number)



@given(instance=lua_Expression_Number_strategy)
def test_lua_expression_number_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=lua_Expression_Smaller_Equal_strategy)
@settings(max_examples=50)
def test_lua_expression_smaller_equal_instantiation(instance):
    assert isinstance(instance, lua_Expression_Smaller_Equal)

@given(instance=lua_Expression_AccessArray_strategy)
@settings(max_examples=50)
def test_lua_expression_accessarray_instantiation(instance):
    assert isinstance(instance, lua_Expression_AccessArray)

@given(instance=lua_Expression_Smaller_strategy)
@settings(max_examples=50)
def test_lua_expression_smaller_instantiation(instance):
    assert isinstance(instance, lua_Expression_Smaller)

@given(instance=lua_Expression_Exponentiation_strategy)
@settings(max_examples=50)
def test_lua_expression_exponentiation_instantiation(instance):
    assert isinstance(instance, lua_Expression_Exponentiation)

@given(instance=lua_Expression_Or_strategy)
@settings(max_examples=50)
def test_lua_expression_or_instantiation(instance):
    assert isinstance(instance, lua_Expression_Or)

@given(instance=lua_Expression_Nil_strategy)
@settings(max_examples=50)
def test_lua_expression_nil_instantiation(instance):
    assert isinstance(instance, lua_Expression_Nil)

@given(instance=Statement_FunctioncallOrAssignment_strategy)
@settings(max_examples=50)
def test_statement_functioncallorassignment_instantiation(instance):
    assert isinstance(instance, Statement_FunctioncallOrAssignment)

@given(instance=lua_Statement_Assignment_strategy)
@settings(max_examples=50)
def test_lua_statement_assignment_instantiation(instance):
    assert isinstance(instance, lua_Statement_Assignment)

@given(instance=lua_Statement_CallMemberFunction_strategy)
@settings(max_examples=50)
def test_lua_statement_callmemberfunction_instantiation(instance):
    assert isinstance(instance, lua_Statement_CallMemberFunction)



@given(instance=lua_Statement_CallMemberFunction_strategy)
def test_lua_statement_callmemberfunction_memberFunctionName_setter(instance):
    original = instance.memberFunctionName
    instance.memberFunctionName = original
    assert instance.memberFunctionName == original

@given(instance=lua_Statement_CallFunction_strategy)
@settings(max_examples=50)
def test_lua_statement_callfunction_instantiation(instance):
    assert isinstance(instance, lua_Statement_CallFunction)

@given(instance=lua_Function_strategy)
@settings(max_examples=50)
def test_lua_function_instantiation(instance):
    assert isinstance(instance, lua_Function)



@given(instance=lua_Function_strategy)
def test_lua_function_varArgs_setter(instance):
    original = instance.varArgs
    instance.varArgs = original
    assert instance.varArgs == original



@given(instance=lua_Function_strategy)
def test_lua_function_parameters_setter(instance):
    original = instance.parameters
    instance.parameters = original
    assert instance.parameters == original

@given(instance=lua_Statement_If_Then_Else_ElseIfPart_strategy)
@settings(max_examples=50)
def test_lua_statement_if_then_else_elseifpart_instantiation(instance):
    assert isinstance(instance, lua_Statement_If_Then_Else_ElseIfPart)

@given(instance=lua_Expression_strategy)
@settings(max_examples=50)
def test_lua_expression_instantiation(instance):
    assert isinstance(instance, lua_Expression)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=lua_Statement_If_Then_Else_strategy)
@settings(max_examples=50)
def test_lua_statement_if_then_else_instantiation(instance):
    assert isinstance(instance, lua_Statement_If_Then_Else)

@given(instance=lua_Statement_While_strategy)
@settings(max_examples=50)
def test_lua_statement_while_instantiation(instance):
    assert isinstance(instance, lua_Statement_While)

@given(instance=lua_Statement_FunctioncallOrAssignment_strategy)
@settings(max_examples=50)
def test_lua_statement_functioncallorassignment_instantiation(instance):
    assert isinstance(instance, lua_Statement_FunctioncallOrAssignment)

@given(instance=lua_Statement_GlobalFunction_Declaration_strategy)
@settings(max_examples=50)
def test_lua_statement_globalfunction_declaration_instantiation(instance):
    assert isinstance(instance, lua_Statement_GlobalFunction_Declaration)



@given(instance=lua_Statement_GlobalFunction_Declaration_strategy)
def test_lua_statement_globalfunction_declaration_functionName_setter(instance):
    original = instance.functionName
    instance.functionName = original
    assert instance.functionName == original



@given(instance=lua_Statement_GlobalFunction_Declaration_strategy)
def test_lua_statement_globalfunction_declaration_prefix_setter(instance):
    original = instance.prefix
    instance.prefix = original
    assert instance.prefix == original

@given(instance=lua_Statement_Local_Variable_Declaration_strategy)
@settings(max_examples=50)
def test_lua_statement_local_variable_declaration_instantiation(instance):
    assert isinstance(instance, lua_Statement_Local_Variable_Declaration)



@given(instance=lua_Statement_Local_Variable_Declaration_strategy)
def test_lua_statement_local_variable_declaration_variableNames_setter(instance):
    original = instance.variableNames
    instance.variableNames = original
    assert instance.variableNames == original

@given(instance=lua_Statement_For_Generic_strategy)
@settings(max_examples=50)
def test_lua_statement_for_generic_instantiation(instance):
    assert isinstance(instance, lua_Statement_For_Generic)



@given(instance=lua_Statement_For_Generic_strategy)
def test_lua_statement_for_generic_names_setter(instance):
    original = instance.names
    instance.names = original
    assert instance.names == original

@given(instance=lua_Statement_Repeat_strategy)
@settings(max_examples=50)
def test_lua_statement_repeat_instantiation(instance):
    assert isinstance(instance, lua_Statement_Repeat)

@given(instance=lua_Statement_LocalFunction_Declaration_strategy)
@settings(max_examples=50)
def test_lua_statement_localfunction_declaration_instantiation(instance):
    assert isinstance(instance, lua_Statement_LocalFunction_Declaration)



@given(instance=lua_Statement_LocalFunction_Declaration_strategy)
def test_lua_statement_localfunction_declaration_functionName_setter(instance):
    original = instance.functionName
    instance.functionName = original
    assert instance.functionName == original

@given(instance=lua_Statement_For_Numeric_strategy)
@settings(max_examples=50)
def test_lua_statement_for_numeric_instantiation(instance):
    assert isinstance(instance, lua_Statement_For_Numeric)



@given(instance=lua_Statement_For_Numeric_strategy)
def test_lua_statement_for_numeric_iteratorName_setter(instance):
    original = instance.iteratorName
    instance.iteratorName = original
    assert instance.iteratorName == original

@given(instance=lua_Statement_Block_strategy)
@settings(max_examples=50)
def test_lua_statement_block_instantiation(instance):
    assert isinstance(instance, lua_Statement_Block)

@given(instance=LastStatement_strategy)
@settings(max_examples=50)
def test_laststatement_instantiation(instance):
    assert isinstance(instance, LastStatement)

@given(instance=lua_LastStatement_Break_strategy)
@settings(max_examples=50)
def test_lua_laststatement_break_instantiation(instance):
    assert isinstance(instance, lua_LastStatement_Break)

@given(instance=lua_LastStatement_Return_strategy)
@settings(max_examples=50)
def test_lua_laststatement_return_instantiation(instance):
    assert isinstance(instance, lua_LastStatement_Return)

@given(instance=lua_LastStatement_strategy)
@settings(max_examples=50)
def test_lua_laststatement_instantiation(instance):
    assert isinstance(instance, lua_LastStatement)

@given(instance=lua_Statement_strategy)
@settings(max_examples=50)
def test_lua_statement_instantiation(instance):
    assert isinstance(instance, lua_Statement)

@given(instance=Chunk_strategy)
@settings(max_examples=50)
def test_chunk_instantiation(instance):
    assert isinstance(instance, Chunk)

@given(instance=lua_Block_strategy)
@settings(max_examples=50)
def test_lua_block_instantiation(instance):
    assert isinstance(instance, lua_Block)

@given(instance=lua_Chunk_strategy)
@settings(max_examples=50)
def test_lua_chunk_instantiation(instance):
    assert isinstance(instance, lua_Chunk)
