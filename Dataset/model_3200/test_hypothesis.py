import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    iot2_Value,
    FinalNode,
    iot2_ActivityFinalNode,
    ControlNode,
    iot2_FinalNode,
    iot2_ForkNode,
    iot2_MergeNode,
    iot2_DecisionNode,
    iot2_JoinNode,
    iot2_InitialNode,
    Expression,
    iot2_Expression_CallMemberFunction,
    iot2_Expression_Exponentiation,
    iot2_Expression_Equal,
    iot2_Expression_AccessArray,
    iot2_Expression_String,
    iot2_Expression_Smaller_Equal,
    iot2_Expression_Negate,
    iot2_Expression_Plus,
    iot2_Expression_Or,
    iot2_Expression_CallFunction,
    iot2_Expression_Not_Equal,
    iot2_Expression_Division,
    iot2_Expression_Smaller,
    iot2_Expression_Length,
    iot2_Expression_Larger_Equal,
    iot2_Expression_Modulo,
    iot2_Expression_Number,
    iot2_Expression_Invert,
    iot2_Expression_Multiplication,
    iot2_Expression_Concatenation,
    iot2_Expression_AccessMember,
    iot2_Expression_And,
    iot2_Expression_VarArgs,
    iot2_Expression_True,
    iot2_Expression_Function,
    iot2_Expression_False,
    iot2_Expression_VariableName,
    iot2_Expression_Larger,
    iot2_Expression_Minus,
    iot2_Expression_Nil,
    Statement_FunctioncallOrAssignment,
    iot2_Statement_CallMemberFunction,
    iot2_Statement_CallFunction,
    iot2_Statement_Assignment,
    LastStatement_Return,
    iot2_LastStatement_ReturnWithValue,
    Field,
    iot2_Field_AddEntryToTable,
    iot2_Field_AppendEntryToTable,
    iot2_Field_AddEntryToTable_Brackets,
    iot2_Functioncall_Arguments,
    iot2_Expression_TableConstructor,
    iot2_Statement_If_Then_Else_ElseIfPart,
    iot2_Function,
    iot2_Expression,
    IDLType,
    Statement,
    iot2_Statement_Repeat,
    iot2_Statement_FunctioncallOrAssignment,
    iot2_Statement_For_Generic,
    iot2_Statement_Local_Variable_Declaration,
    iot2_Statement_LocalFunction_Declaration,
    iot2_Statement_While,
    iot2_Statement_GlobalFunction_Declaration,
    iot2_Statement_For_Numeric,
    iot2_Statement_If_Then_Else,
    iot2_Statement_Block,
    LastStatement,
    iot2_LastStatement_Break,
    iot2_LastStatement_Return,
    iot2_LastStatement,
    iot2_Statement,
    Chunk,
    iot2_Chunk,
    iot2_PrimitiveDef,
    Typed,
    iot2_Field,
    iot2_ParameterDef,
    Contained,
    iot2_Variable,
    NamedElement,
    iot2_ActivityNode,
    iot2_ActivityEdge,
    iot2_TypedefDef,
    iot2_IDLType,
    iot2_Typed,
    iot2_NamedElement,
    iot2_Container,
    iot2_Contained,
    iot2_Block,
    iot2_ExceptionDef,
    HWComponent,
    iot2_Actuator,
    iot2_Sensor,
    iot2_OperationDef,
    iot2_Activity,
    iot2_Sketch,
    iot2_Board,
    iot2_HWComponent,
    iot2_System,
    iot2_Trace,
    IntegerExpression,
    iot2_IntegerComparisonExpression,
    iot2_IntegerCalculationExpression,
    iot2_BooleanExpression,
    iot2_Token,
    iot2_Input,
    iot2_InputValue,
    BooleanExpression,
    iot2_BooleanBinaryExpression,
    iot2_BooleanUnaryExpression,
    Action,
    iot2_OpaqueAction,
    ExecutableNode,
    iot2_Action,
    ActivityNode,
    iot2_ExecutableNode,
    iot2_ControlNode,
    ActivityEdge,
    iot2_ControlFlow,
    iot2_IntegerExpression,
    Value,
    iot2_IntegerValue,
    iot2_BooleanValue,
    Variable,
    iot2_BooleanVariable,
    iot2_IntegerVariable,
    IntegerComparisonOperator,
    BoardType,
    BooleanUnaryOperator,
    ParameterMode,
    PrimitiveKind,
    IntegerCalculationOperator,
    BooleanBinaryOperator,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_iot2_value_is_not_abstract():
    assert not inspect.isabstract(iot2_Value)


def test_iot2_value_constructor_exists():
    assert callable(iot2_Value.__init__)


def test_iot2_value_constructor_args():
    sig = inspect.signature(iot2_Value.__init__)
    params = list(sig.parameters.keys())



def test_finalnode_is_not_abstract():
    assert not inspect.isabstract(FinalNode)


def test_finalnode_constructor_exists():
    assert callable(FinalNode.__init__)


def test_finalnode_constructor_args():
    sig = inspect.signature(FinalNode.__init__)
    params = list(sig.parameters.keys())



def test_iot2_activityfinalnode_is_not_abstract():
    assert not inspect.isabstract(iot2_ActivityFinalNode)


def test_iot2_activityfinalnode_constructor_exists():
    assert callable(iot2_ActivityFinalNode.__init__)


def test_iot2_activityfinalnode_constructor_args():
    sig = inspect.signature(iot2_ActivityFinalNode.__init__)
    params = list(sig.parameters.keys())



def test_controlnode_is_not_abstract():
    assert not inspect.isabstract(ControlNode)


def test_controlnode_constructor_exists():
    assert callable(ControlNode.__init__)


def test_controlnode_constructor_args():
    sig = inspect.signature(ControlNode.__init__)
    params = list(sig.parameters.keys())



def test_iot2_finalnode_is_not_abstract():
    assert not inspect.isabstract(iot2_FinalNode)


def test_iot2_finalnode_constructor_exists():
    assert callable(iot2_FinalNode.__init__)


def test_iot2_finalnode_constructor_args():
    sig = inspect.signature(iot2_FinalNode.__init__)
    params = list(sig.parameters.keys())



def test_iot2_forknode_is_not_abstract():
    assert not inspect.isabstract(iot2_ForkNode)


def test_iot2_forknode_constructor_exists():
    assert callable(iot2_ForkNode.__init__)


def test_iot2_forknode_constructor_args():
    sig = inspect.signature(iot2_ForkNode.__init__)
    params = list(sig.parameters.keys())



def test_iot2_mergenode_is_not_abstract():
    assert not inspect.isabstract(iot2_MergeNode)


def test_iot2_mergenode_constructor_exists():
    assert callable(iot2_MergeNode.__init__)


def test_iot2_mergenode_constructor_args():
    sig = inspect.signature(iot2_MergeNode.__init__)
    params = list(sig.parameters.keys())



def test_iot2_decisionnode_is_not_abstract():
    assert not inspect.isabstract(iot2_DecisionNode)


def test_iot2_decisionnode_constructor_exists():
    assert callable(iot2_DecisionNode.__init__)


def test_iot2_decisionnode_constructor_args():
    sig = inspect.signature(iot2_DecisionNode.__init__)
    params = list(sig.parameters.keys())



def test_iot2_joinnode_is_not_abstract():
    assert not inspect.isabstract(iot2_JoinNode)


def test_iot2_joinnode_constructor_exists():
    assert callable(iot2_JoinNode.__init__)


def test_iot2_joinnode_constructor_args():
    sig = inspect.signature(iot2_JoinNode.__init__)
    params = list(sig.parameters.keys())



def test_iot2_initialnode_is_not_abstract():
    assert not inspect.isabstract(iot2_InitialNode)


def test_iot2_initialnode_constructor_exists():
    assert callable(iot2_InitialNode.__init__)


def test_iot2_initialnode_constructor_args():
    sig = inspect.signature(iot2_InitialNode.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_iot2_expression_callmemberfunction_is_not_abstract():
    assert not inspect.isabstract(iot2_Expression_CallMemberFunction)


def test_iot2_expression_callmemberfunction_constructor_exists():
    assert callable(iot2_Expression_CallMemberFunction.__init__)


def test_iot2_expression_callmemberfunction_constructor_args():
    sig = inspect.signature(iot2_Expression_CallMemberFunction.__init__)
    params = list(sig.parameters.keys())
    assert "memberFunctionName" in params, "Missing parameter 'memberFunctionName'"

def test_iot2_expression_callmemberfunction_has_memberFunctionName():
    assert hasattr(iot2_Expression_CallMemberFunction, "memberFunctionName")
    descriptor = None
    for klass in iot2_Expression_CallMemberFunction.__mro__:
        if "memberFunctionName" in klass.__dict__:
            descriptor = klass.__dict__["memberFunctionName"]
            break
    assert isinstance(descriptor, property)



def test_iot2_expression_exponentiation_is_not_abstract():
    assert not inspect.isabstract(iot2_Expression_Exponentiation)


def test_iot2_expression_exponentiation_constructor_exists():
    assert callable(iot2_Expression_Exponentiation.__init__)


def test_iot2_expression_exponentiation_constructor_args():
    sig = inspect.signature(iot2_Expression_Exponentiation.__init__)
    params = list(sig.parameters.keys())



def test_iot2_expression_equal_is_not_abstract():
    assert not inspect.isabstract(iot2_Expression_Equal)


def test_iot2_expression_equal_constructor_exists():
    assert callable(iot2_Expression_Equal.__init__)


def test_iot2_expression_equal_constructor_args():
    sig = inspect.signature(iot2_Expression_Equal.__init__)
    params = list(sig.parameters.keys())



def test_iot2_expression_accessarray_is_not_abstract():
    assert not inspect.isabstract(iot2_Expression_AccessArray)


def test_iot2_expression_accessarray_constructor_exists():
    assert callable(iot2_Expression_AccessArray.__init__)


def test_iot2_expression_accessarray_constructor_args():
    sig = inspect.signature(iot2_Expression_AccessArray.__init__)
    params = list(sig.parameters.keys())



def test_iot2_expression_string_is_not_abstract():
    assert not inspect.isabstract(iot2_Expression_String)


def test_iot2_expression_string_constructor_exists():
    assert callable(iot2_Expression_String.__init__)


def test_iot2_expression_string_constructor_args():
    sig = inspect.signature(iot2_Expression_String.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_iot2_expression_string_has_value():
    assert hasattr(iot2_Expression_String, "value")
    descriptor = None
    for klass in iot2_Expression_String.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_iot2_expression_smaller_equal_is_not_abstract():
    assert not inspect.isabstract(iot2_Expression_Smaller_Equal)


def test_iot2_expression_smaller_equal_constructor_exists():
    assert callable(iot2_Expression_Smaller_Equal.__init__)


def test_iot2_expression_smaller_equal_constructor_args():
    sig = inspect.signature(iot2_Expression_Smaller_Equal.__init__)
    params = list(sig.parameters.keys())



def test_iot2_expression_negate_is_not_abstract():
    assert not inspect.isabstract(iot2_Expression_Negate)


def test_iot2_expression_negate_constructor_exists():
    assert callable(iot2_Expression_Negate.__init__)


def test_iot2_expression_negate_constructor_args():
    sig = inspect.signature(iot2_Expression_Negate.__init__)
    params = list(sig.parameters.keys())



def test_iot2_expression_plus_is_not_abstract():
    assert not inspect.isabstract(iot2_Expression_Plus)


def test_iot2_expression_plus_constructor_exists():
    assert callable(iot2_Expression_Plus.__init__)


def test_iot2_expression_plus_constructor_args():
    sig = inspect.signature(iot2_Expression_Plus.__init__)
    params = list(sig.parameters.keys())



def test_iot2_expression_or_is_not_abstract():
    assert not inspect.isabstract(iot2_Expression_Or)


def test_iot2_expression_or_constructor_exists():
    assert callable(iot2_Expression_Or.__init__)


def test_iot2_expression_or_constructor_args():
    sig = inspect.signature(iot2_Expression_Or.__init__)
    params = list(sig.parameters.keys())



def test_iot2_expression_callfunction_is_not_abstract():
    assert not inspect.isabstract(iot2_Expression_CallFunction)


def test_iot2_expression_callfunction_constructor_exists():
    assert callable(iot2_Expression_CallFunction.__init__)


def test_iot2_expression_callfunction_constructor_args():
    sig = inspect.signature(iot2_Expression_CallFunction.__init__)
    params = list(sig.parameters.keys())



def test_iot2_expression_not_equal_is_not_abstract():
    assert not inspect.isabstract(iot2_Expression_Not_Equal)


def test_iot2_expression_not_equal_constructor_exists():
    assert callable(iot2_Expression_Not_Equal.__init__)


def test_iot2_expression_not_equal_constructor_args():
    sig = inspect.signature(iot2_Expression_Not_Equal.__init__)
    params = list(sig.parameters.keys())



def test_iot2_expression_division_is_not_abstract():
    assert not inspect.isabstract(iot2_Expression_Division)


def test_iot2_expression_division_constructor_exists():
    assert callable(iot2_Expression_Division.__init__)


def test_iot2_expression_division_constructor_args():
    sig = inspect.signature(iot2_Expression_Division.__init__)
    params = list(sig.parameters.keys())



def test_iot2_expression_smaller_is_not_abstract():
    assert not inspect.isabstract(iot2_Expression_Smaller)


def test_iot2_expression_smaller_constructor_exists():
    assert callable(iot2_Expression_Smaller.__init__)


def test_iot2_expression_smaller_constructor_args():
    sig = inspect.signature(iot2_Expression_Smaller.__init__)
    params = list(sig.parameters.keys())



def test_iot2_expression_length_is_not_abstract():
    assert not inspect.isabstract(iot2_Expression_Length)


def test_iot2_expression_length_constructor_exists():
    assert callable(iot2_Expression_Length.__init__)


def test_iot2_expression_length_constructor_args():
    sig = inspect.signature(iot2_Expression_Length.__init__)
    params = list(sig.parameters.keys())



def test_iot2_expression_larger_equal_is_not_abstract():
    assert not inspect.isabstract(iot2_Expression_Larger_Equal)


def test_iot2_expression_larger_equal_constructor_exists():
    assert callable(iot2_Expression_Larger_Equal.__init__)


def test_iot2_expression_larger_equal_constructor_args():
    sig = inspect.signature(iot2_Expression_Larger_Equal.__init__)
    params = list(sig.parameters.keys())



def test_iot2_expression_modulo_is_not_abstract():
    assert not inspect.isabstract(iot2_Expression_Modulo)


def test_iot2_expression_modulo_constructor_exists():
    assert callable(iot2_Expression_Modulo.__init__)


def test_iot2_expression_modulo_constructor_args():
    sig = inspect.signature(iot2_Expression_Modulo.__init__)
    params = list(sig.parameters.keys())



def test_iot2_expression_number_is_not_abstract():
    assert not inspect.isabstract(iot2_Expression_Number)


def test_iot2_expression_number_constructor_exists():
    assert callable(iot2_Expression_Number.__init__)


def test_iot2_expression_number_constructor_args():
    sig = inspect.signature(iot2_Expression_Number.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_iot2_expression_number_has_value():
    assert hasattr(iot2_Expression_Number, "value")
    descriptor = None
    for klass in iot2_Expression_Number.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_iot2_expression_invert_is_not_abstract():
    assert not inspect.isabstract(iot2_Expression_Invert)


def test_iot2_expression_invert_constructor_exists():
    assert callable(iot2_Expression_Invert.__init__)


def test_iot2_expression_invert_constructor_args():
    sig = inspect.signature(iot2_Expression_Invert.__init__)
    params = list(sig.parameters.keys())



def test_iot2_expression_multiplication_is_not_abstract():
    assert not inspect.isabstract(iot2_Expression_Multiplication)


def test_iot2_expression_multiplication_constructor_exists():
    assert callable(iot2_Expression_Multiplication.__init__)


def test_iot2_expression_multiplication_constructor_args():
    sig = inspect.signature(iot2_Expression_Multiplication.__init__)
    params = list(sig.parameters.keys())



def test_iot2_expression_concatenation_is_not_abstract():
    assert not inspect.isabstract(iot2_Expression_Concatenation)


def test_iot2_expression_concatenation_constructor_exists():
    assert callable(iot2_Expression_Concatenation.__init__)


def test_iot2_expression_concatenation_constructor_args():
    sig = inspect.signature(iot2_Expression_Concatenation.__init__)
    params = list(sig.parameters.keys())



def test_iot2_expression_accessmember_is_not_abstract():
    assert not inspect.isabstract(iot2_Expression_AccessMember)


def test_iot2_expression_accessmember_constructor_exists():
    assert callable(iot2_Expression_AccessMember.__init__)


def test_iot2_expression_accessmember_constructor_args():
    sig = inspect.signature(iot2_Expression_AccessMember.__init__)
    params = list(sig.parameters.keys())
    assert "memberName" in params, "Missing parameter 'memberName'"

def test_iot2_expression_accessmember_has_memberName():
    assert hasattr(iot2_Expression_AccessMember, "memberName")
    descriptor = None
    for klass in iot2_Expression_AccessMember.__mro__:
        if "memberName" in klass.__dict__:
            descriptor = klass.__dict__["memberName"]
            break
    assert isinstance(descriptor, property)



def test_iot2_expression_and_is_not_abstract():
    assert not inspect.isabstract(iot2_Expression_And)


def test_iot2_expression_and_constructor_exists():
    assert callable(iot2_Expression_And.__init__)


def test_iot2_expression_and_constructor_args():
    sig = inspect.signature(iot2_Expression_And.__init__)
    params = list(sig.parameters.keys())



def test_iot2_expression_varargs_is_not_abstract():
    assert not inspect.isabstract(iot2_Expression_VarArgs)


def test_iot2_expression_varargs_constructor_exists():
    assert callable(iot2_Expression_VarArgs.__init__)


def test_iot2_expression_varargs_constructor_args():
    sig = inspect.signature(iot2_Expression_VarArgs.__init__)
    params = list(sig.parameters.keys())



def test_iot2_expression_true_is_not_abstract():
    assert not inspect.isabstract(iot2_Expression_True)


def test_iot2_expression_true_constructor_exists():
    assert callable(iot2_Expression_True.__init__)


def test_iot2_expression_true_constructor_args():
    sig = inspect.signature(iot2_Expression_True.__init__)
    params = list(sig.parameters.keys())



def test_iot2_expression_function_is_not_abstract():
    assert not inspect.isabstract(iot2_Expression_Function)


def test_iot2_expression_function_constructor_exists():
    assert callable(iot2_Expression_Function.__init__)


def test_iot2_expression_function_constructor_args():
    sig = inspect.signature(iot2_Expression_Function.__init__)
    params = list(sig.parameters.keys())



def test_iot2_expression_false_is_not_abstract():
    assert not inspect.isabstract(iot2_Expression_False)


def test_iot2_expression_false_constructor_exists():
    assert callable(iot2_Expression_False.__init__)


def test_iot2_expression_false_constructor_args():
    sig = inspect.signature(iot2_Expression_False.__init__)
    params = list(sig.parameters.keys())



def test_iot2_expression_variablename_is_not_abstract():
    assert not inspect.isabstract(iot2_Expression_VariableName)


def test_iot2_expression_variablename_constructor_exists():
    assert callable(iot2_Expression_VariableName.__init__)


def test_iot2_expression_variablename_constructor_args():
    sig = inspect.signature(iot2_Expression_VariableName.__init__)
    params = list(sig.parameters.keys())
    assert "variable" in params, "Missing parameter 'variable'"

def test_iot2_expression_variablename_has_variable():
    assert hasattr(iot2_Expression_VariableName, "variable")
    descriptor = None
    for klass in iot2_Expression_VariableName.__mro__:
        if "variable" in klass.__dict__:
            descriptor = klass.__dict__["variable"]
            break
    assert isinstance(descriptor, property)



def test_iot2_expression_larger_is_not_abstract():
    assert not inspect.isabstract(iot2_Expression_Larger)


def test_iot2_expression_larger_constructor_exists():
    assert callable(iot2_Expression_Larger.__init__)


def test_iot2_expression_larger_constructor_args():
    sig = inspect.signature(iot2_Expression_Larger.__init__)
    params = list(sig.parameters.keys())



def test_iot2_expression_minus_is_not_abstract():
    assert not inspect.isabstract(iot2_Expression_Minus)


def test_iot2_expression_minus_constructor_exists():
    assert callable(iot2_Expression_Minus.__init__)


def test_iot2_expression_minus_constructor_args():
    sig = inspect.signature(iot2_Expression_Minus.__init__)
    params = list(sig.parameters.keys())



def test_iot2_expression_nil_is_not_abstract():
    assert not inspect.isabstract(iot2_Expression_Nil)


def test_iot2_expression_nil_constructor_exists():
    assert callable(iot2_Expression_Nil.__init__)


def test_iot2_expression_nil_constructor_args():
    sig = inspect.signature(iot2_Expression_Nil.__init__)
    params = list(sig.parameters.keys())



def test_statement_functioncallorassignment_is_not_abstract():
    assert not inspect.isabstract(Statement_FunctioncallOrAssignment)


def test_statement_functioncallorassignment_constructor_exists():
    assert callable(Statement_FunctioncallOrAssignment.__init__)


def test_statement_functioncallorassignment_constructor_args():
    sig = inspect.signature(Statement_FunctioncallOrAssignment.__init__)
    params = list(sig.parameters.keys())



def test_iot2_statement_callmemberfunction_is_not_abstract():
    assert not inspect.isabstract(iot2_Statement_CallMemberFunction)


def test_iot2_statement_callmemberfunction_constructor_exists():
    assert callable(iot2_Statement_CallMemberFunction.__init__)


def test_iot2_statement_callmemberfunction_constructor_args():
    sig = inspect.signature(iot2_Statement_CallMemberFunction.__init__)
    params = list(sig.parameters.keys())
    assert "memberFunctionName" in params, "Missing parameter 'memberFunctionName'"

def test_iot2_statement_callmemberfunction_has_memberFunctionName():
    assert hasattr(iot2_Statement_CallMemberFunction, "memberFunctionName")
    descriptor = None
    for klass in iot2_Statement_CallMemberFunction.__mro__:
        if "memberFunctionName" in klass.__dict__:
            descriptor = klass.__dict__["memberFunctionName"]
            break
    assert isinstance(descriptor, property)



def test_iot2_statement_callfunction_is_not_abstract():
    assert not inspect.isabstract(iot2_Statement_CallFunction)


def test_iot2_statement_callfunction_constructor_exists():
    assert callable(iot2_Statement_CallFunction.__init__)


def test_iot2_statement_callfunction_constructor_args():
    sig = inspect.signature(iot2_Statement_CallFunction.__init__)
    params = list(sig.parameters.keys())



def test_iot2_statement_assignment_is_not_abstract():
    assert not inspect.isabstract(iot2_Statement_Assignment)


def test_iot2_statement_assignment_constructor_exists():
    assert callable(iot2_Statement_Assignment.__init__)


def test_iot2_statement_assignment_constructor_args():
    sig = inspect.signature(iot2_Statement_Assignment.__init__)
    params = list(sig.parameters.keys())



def test_laststatement_return_is_not_abstract():
    assert not inspect.isabstract(LastStatement_Return)


def test_laststatement_return_constructor_exists():
    assert callable(LastStatement_Return.__init__)


def test_laststatement_return_constructor_args():
    sig = inspect.signature(LastStatement_Return.__init__)
    params = list(sig.parameters.keys())



def test_iot2_laststatement_returnwithvalue_is_not_abstract():
    assert not inspect.isabstract(iot2_LastStatement_ReturnWithValue)


def test_iot2_laststatement_returnwithvalue_constructor_exists():
    assert callable(iot2_LastStatement_ReturnWithValue.__init__)


def test_iot2_laststatement_returnwithvalue_constructor_args():
    sig = inspect.signature(iot2_LastStatement_ReturnWithValue.__init__)
    params = list(sig.parameters.keys())



def test_field_is_not_abstract():
    assert not inspect.isabstract(Field)


def test_field_constructor_exists():
    assert callable(Field.__init__)


def test_field_constructor_args():
    sig = inspect.signature(Field.__init__)
    params = list(sig.parameters.keys())



def test_iot2_field_addentrytotable_is_not_abstract():
    assert not inspect.isabstract(iot2_Field_AddEntryToTable)


def test_iot2_field_addentrytotable_constructor_exists():
    assert callable(iot2_Field_AddEntryToTable.__init__)


def test_iot2_field_addentrytotable_constructor_args():
    sig = inspect.signature(iot2_Field_AddEntryToTable.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"

def test_iot2_field_addentrytotable_has_key():
    assert hasattr(iot2_Field_AddEntryToTable, "key")
    descriptor = None
    for klass in iot2_Field_AddEntryToTable.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_iot2_field_appendentrytotable_is_not_abstract():
    assert not inspect.isabstract(iot2_Field_AppendEntryToTable)


def test_iot2_field_appendentrytotable_constructor_exists():
    assert callable(iot2_Field_AppendEntryToTable.__init__)


def test_iot2_field_appendentrytotable_constructor_args():
    sig = inspect.signature(iot2_Field_AppendEntryToTable.__init__)
    params = list(sig.parameters.keys())



def test_iot2_field_addentrytotable_brackets_is_not_abstract():
    assert not inspect.isabstract(iot2_Field_AddEntryToTable_Brackets)


def test_iot2_field_addentrytotable_brackets_constructor_exists():
    assert callable(iot2_Field_AddEntryToTable_Brackets.__init__)


def test_iot2_field_addentrytotable_brackets_constructor_args():
    sig = inspect.signature(iot2_Field_AddEntryToTable_Brackets.__init__)
    params = list(sig.parameters.keys())



def test_iot2_functioncall_arguments_is_not_abstract():
    assert not inspect.isabstract(iot2_Functioncall_Arguments)


def test_iot2_functioncall_arguments_constructor_exists():
    assert callable(iot2_Functioncall_Arguments.__init__)


def test_iot2_functioncall_arguments_constructor_args():
    sig = inspect.signature(iot2_Functioncall_Arguments.__init__)
    params = list(sig.parameters.keys())



def test_iot2_expression_tableconstructor_is_not_abstract():
    assert not inspect.isabstract(iot2_Expression_TableConstructor)


def test_iot2_expression_tableconstructor_constructor_exists():
    assert callable(iot2_Expression_TableConstructor.__init__)


def test_iot2_expression_tableconstructor_constructor_args():
    sig = inspect.signature(iot2_Expression_TableConstructor.__init__)
    params = list(sig.parameters.keys())



def test_iot2_statement_if_then_else_elseifpart_is_not_abstract():
    assert not inspect.isabstract(iot2_Statement_If_Then_Else_ElseIfPart)


def test_iot2_statement_if_then_else_elseifpart_constructor_exists():
    assert callable(iot2_Statement_If_Then_Else_ElseIfPart.__init__)


def test_iot2_statement_if_then_else_elseifpart_constructor_args():
    sig = inspect.signature(iot2_Statement_If_Then_Else_ElseIfPart.__init__)
    params = list(sig.parameters.keys())



def test_iot2_function_is_not_abstract():
    assert not inspect.isabstract(iot2_Function)


def test_iot2_function_constructor_exists():
    assert callable(iot2_Function.__init__)


def test_iot2_function_constructor_args():
    sig = inspect.signature(iot2_Function.__init__)
    params = list(sig.parameters.keys())
    assert "varArgs" in params, "Missing parameter 'varArgs'"
    assert "parameters" in params, "Missing parameter 'parameters'"

def test_iot2_function_has_varArgs():
    assert hasattr(iot2_Function, "varArgs")
    descriptor = None
    for klass in iot2_Function.__mro__:
        if "varArgs" in klass.__dict__:
            descriptor = klass.__dict__["varArgs"]
            break
    assert isinstance(descriptor, property)

def test_iot2_function_has_parameters():
    assert hasattr(iot2_Function, "parameters")
    descriptor = None
    for klass in iot2_Function.__mro__:
        if "parameters" in klass.__dict__:
            descriptor = klass.__dict__["parameters"]
            break
    assert isinstance(descriptor, property)



def test_iot2_expression_is_not_abstract():
    assert not inspect.isabstract(iot2_Expression)


def test_iot2_expression_constructor_exists():
    assert callable(iot2_Expression.__init__)


def test_iot2_expression_constructor_args():
    sig = inspect.signature(iot2_Expression.__init__)
    params = list(sig.parameters.keys())



def test_idltype_is_not_abstract():
    assert not inspect.isabstract(IDLType)


def test_idltype_constructor_exists():
    assert callable(IDLType.__init__)


def test_idltype_constructor_args():
    sig = inspect.signature(IDLType.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_iot2_statement_repeat_is_not_abstract():
    assert not inspect.isabstract(iot2_Statement_Repeat)


def test_iot2_statement_repeat_constructor_exists():
    assert callable(iot2_Statement_Repeat.__init__)


def test_iot2_statement_repeat_constructor_args():
    sig = inspect.signature(iot2_Statement_Repeat.__init__)
    params = list(sig.parameters.keys())



def test_iot2_statement_functioncallorassignment_is_not_abstract():
    assert not inspect.isabstract(iot2_Statement_FunctioncallOrAssignment)


def test_iot2_statement_functioncallorassignment_constructor_exists():
    assert callable(iot2_Statement_FunctioncallOrAssignment.__init__)


def test_iot2_statement_functioncallorassignment_constructor_args():
    sig = inspect.signature(iot2_Statement_FunctioncallOrAssignment.__init__)
    params = list(sig.parameters.keys())



def test_iot2_statement_for_generic_is_not_abstract():
    assert not inspect.isabstract(iot2_Statement_For_Generic)


def test_iot2_statement_for_generic_constructor_exists():
    assert callable(iot2_Statement_For_Generic.__init__)


def test_iot2_statement_for_generic_constructor_args():
    sig = inspect.signature(iot2_Statement_For_Generic.__init__)
    params = list(sig.parameters.keys())
    assert "names" in params, "Missing parameter 'names'"

def test_iot2_statement_for_generic_has_names():
    assert hasattr(iot2_Statement_For_Generic, "names")
    descriptor = None
    for klass in iot2_Statement_For_Generic.__mro__:
        if "names" in klass.__dict__:
            descriptor = klass.__dict__["names"]
            break
    assert isinstance(descriptor, property)



def test_iot2_statement_local_variable_declaration_is_not_abstract():
    assert not inspect.isabstract(iot2_Statement_Local_Variable_Declaration)


def test_iot2_statement_local_variable_declaration_constructor_exists():
    assert callable(iot2_Statement_Local_Variable_Declaration.__init__)


def test_iot2_statement_local_variable_declaration_constructor_args():
    sig = inspect.signature(iot2_Statement_Local_Variable_Declaration.__init__)
    params = list(sig.parameters.keys())
    assert "variableNames" in params, "Missing parameter 'variableNames'"

def test_iot2_statement_local_variable_declaration_has_variableNames():
    assert hasattr(iot2_Statement_Local_Variable_Declaration, "variableNames")
    descriptor = None
    for klass in iot2_Statement_Local_Variable_Declaration.__mro__:
        if "variableNames" in klass.__dict__:
            descriptor = klass.__dict__["variableNames"]
            break
    assert isinstance(descriptor, property)



def test_iot2_statement_localfunction_declaration_is_not_abstract():
    assert not inspect.isabstract(iot2_Statement_LocalFunction_Declaration)


def test_iot2_statement_localfunction_declaration_constructor_exists():
    assert callable(iot2_Statement_LocalFunction_Declaration.__init__)


def test_iot2_statement_localfunction_declaration_constructor_args():
    sig = inspect.signature(iot2_Statement_LocalFunction_Declaration.__init__)
    params = list(sig.parameters.keys())
    assert "functionName" in params, "Missing parameter 'functionName'"

def test_iot2_statement_localfunction_declaration_has_functionName():
    assert hasattr(iot2_Statement_LocalFunction_Declaration, "functionName")
    descriptor = None
    for klass in iot2_Statement_LocalFunction_Declaration.__mro__:
        if "functionName" in klass.__dict__:
            descriptor = klass.__dict__["functionName"]
            break
    assert isinstance(descriptor, property)



def test_iot2_statement_while_is_not_abstract():
    assert not inspect.isabstract(iot2_Statement_While)


def test_iot2_statement_while_constructor_exists():
    assert callable(iot2_Statement_While.__init__)


def test_iot2_statement_while_constructor_args():
    sig = inspect.signature(iot2_Statement_While.__init__)
    params = list(sig.parameters.keys())



def test_iot2_statement_globalfunction_declaration_is_not_abstract():
    assert not inspect.isabstract(iot2_Statement_GlobalFunction_Declaration)


def test_iot2_statement_globalfunction_declaration_constructor_exists():
    assert callable(iot2_Statement_GlobalFunction_Declaration.__init__)


def test_iot2_statement_globalfunction_declaration_constructor_args():
    sig = inspect.signature(iot2_Statement_GlobalFunction_Declaration.__init__)
    params = list(sig.parameters.keys())
    assert "prefix" in params, "Missing parameter 'prefix'"
    assert "functionName" in params, "Missing parameter 'functionName'"

def test_iot2_statement_globalfunction_declaration_has_prefix():
    assert hasattr(iot2_Statement_GlobalFunction_Declaration, "prefix")
    descriptor = None
    for klass in iot2_Statement_GlobalFunction_Declaration.__mro__:
        if "prefix" in klass.__dict__:
            descriptor = klass.__dict__["prefix"]
            break
    assert isinstance(descriptor, property)

def test_iot2_statement_globalfunction_declaration_has_functionName():
    assert hasattr(iot2_Statement_GlobalFunction_Declaration, "functionName")
    descriptor = None
    for klass in iot2_Statement_GlobalFunction_Declaration.__mro__:
        if "functionName" in klass.__dict__:
            descriptor = klass.__dict__["functionName"]
            break
    assert isinstance(descriptor, property)



def test_iot2_statement_for_numeric_is_not_abstract():
    assert not inspect.isabstract(iot2_Statement_For_Numeric)


def test_iot2_statement_for_numeric_constructor_exists():
    assert callable(iot2_Statement_For_Numeric.__init__)


def test_iot2_statement_for_numeric_constructor_args():
    sig = inspect.signature(iot2_Statement_For_Numeric.__init__)
    params = list(sig.parameters.keys())
    assert "iteratorName" in params, "Missing parameter 'iteratorName'"

def test_iot2_statement_for_numeric_has_iteratorName():
    assert hasattr(iot2_Statement_For_Numeric, "iteratorName")
    descriptor = None
    for klass in iot2_Statement_For_Numeric.__mro__:
        if "iteratorName" in klass.__dict__:
            descriptor = klass.__dict__["iteratorName"]
            break
    assert isinstance(descriptor, property)



def test_iot2_statement_if_then_else_is_not_abstract():
    assert not inspect.isabstract(iot2_Statement_If_Then_Else)


def test_iot2_statement_if_then_else_constructor_exists():
    assert callable(iot2_Statement_If_Then_Else.__init__)


def test_iot2_statement_if_then_else_constructor_args():
    sig = inspect.signature(iot2_Statement_If_Then_Else.__init__)
    params = list(sig.parameters.keys())



def test_iot2_statement_block_is_not_abstract():
    assert not inspect.isabstract(iot2_Statement_Block)


def test_iot2_statement_block_constructor_exists():
    assert callable(iot2_Statement_Block.__init__)


def test_iot2_statement_block_constructor_args():
    sig = inspect.signature(iot2_Statement_Block.__init__)
    params = list(sig.parameters.keys())



def test_laststatement_is_not_abstract():
    assert not inspect.isabstract(LastStatement)


def test_laststatement_constructor_exists():
    assert callable(LastStatement.__init__)


def test_laststatement_constructor_args():
    sig = inspect.signature(LastStatement.__init__)
    params = list(sig.parameters.keys())



def test_iot2_laststatement_break_is_not_abstract():
    assert not inspect.isabstract(iot2_LastStatement_Break)


def test_iot2_laststatement_break_constructor_exists():
    assert callable(iot2_LastStatement_Break.__init__)


def test_iot2_laststatement_break_constructor_args():
    sig = inspect.signature(iot2_LastStatement_Break.__init__)
    params = list(sig.parameters.keys())



def test_iot2_laststatement_return_is_not_abstract():
    assert not inspect.isabstract(iot2_LastStatement_Return)


def test_iot2_laststatement_return_constructor_exists():
    assert callable(iot2_LastStatement_Return.__init__)


def test_iot2_laststatement_return_constructor_args():
    sig = inspect.signature(iot2_LastStatement_Return.__init__)
    params = list(sig.parameters.keys())



def test_iot2_laststatement_is_not_abstract():
    assert not inspect.isabstract(iot2_LastStatement)


def test_iot2_laststatement_constructor_exists():
    assert callable(iot2_LastStatement.__init__)


def test_iot2_laststatement_constructor_args():
    sig = inspect.signature(iot2_LastStatement.__init__)
    params = list(sig.parameters.keys())



def test_iot2_statement_is_not_abstract():
    assert not inspect.isabstract(iot2_Statement)


def test_iot2_statement_constructor_exists():
    assert callable(iot2_Statement.__init__)


def test_iot2_statement_constructor_args():
    sig = inspect.signature(iot2_Statement.__init__)
    params = list(sig.parameters.keys())



def test_chunk_is_not_abstract():
    assert not inspect.isabstract(Chunk)


def test_chunk_constructor_exists():
    assert callable(Chunk.__init__)


def test_chunk_constructor_args():
    sig = inspect.signature(Chunk.__init__)
    params = list(sig.parameters.keys())



def test_iot2_chunk_is_not_abstract():
    assert not inspect.isabstract(iot2_Chunk)


def test_iot2_chunk_constructor_exists():
    assert callable(iot2_Chunk.__init__)


def test_iot2_chunk_constructor_args():
    sig = inspect.signature(iot2_Chunk.__init__)
    params = list(sig.parameters.keys())



def test_iot2_primitivedef_is_not_abstract():
    assert not inspect.isabstract(iot2_PrimitiveDef)


def test_iot2_primitivedef_constructor_exists():
    assert callable(iot2_PrimitiveDef.__init__)


def test_iot2_primitivedef_constructor_args():
    sig = inspect.signature(iot2_PrimitiveDef.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_iot2_primitivedef_has_kind():
    assert hasattr(iot2_PrimitiveDef, "kind")
    descriptor = None
    for klass in iot2_PrimitiveDef.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_typed_is_not_abstract():
    assert not inspect.isabstract(Typed)


def test_typed_constructor_exists():
    assert callable(Typed.__init__)


def test_typed_constructor_args():
    sig = inspect.signature(Typed.__init__)
    params = list(sig.parameters.keys())



def test_iot2_field_is_not_abstract():
    assert not inspect.isabstract(iot2_Field)


def test_iot2_field_constructor_exists():
    assert callable(iot2_Field.__init__)


def test_iot2_field_constructor_args():
    sig = inspect.signature(iot2_Field.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"

def test_iot2_field_has_identifier():
    assert hasattr(iot2_Field, "identifier")
    descriptor = None
    for klass in iot2_Field.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)



def test_iot2_parameterdef_is_not_abstract():
    assert not inspect.isabstract(iot2_ParameterDef)


def test_iot2_parameterdef_constructor_exists():
    assert callable(iot2_ParameterDef.__init__)


def test_iot2_parameterdef_constructor_args():
    sig = inspect.signature(iot2_ParameterDef.__init__)
    params = list(sig.parameters.keys())
    assert "direction" in params, "Missing parameter 'direction'"
    assert "identifier" in params, "Missing parameter 'identifier'"

def test_iot2_parameterdef_has_direction():
    assert hasattr(iot2_ParameterDef, "direction")
    descriptor = None
    for klass in iot2_ParameterDef.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)

def test_iot2_parameterdef_has_identifier():
    assert hasattr(iot2_ParameterDef, "identifier")
    descriptor = None
    for klass in iot2_ParameterDef.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)



def test_contained_is_not_abstract():
    assert not inspect.isabstract(Contained)


def test_contained_constructor_exists():
    assert callable(Contained.__init__)


def test_contained_constructor_args():
    sig = inspect.signature(Contained.__init__)
    params = list(sig.parameters.keys())



def test_iot2_variable_is_not_abstract():
    assert not inspect.isabstract(iot2_Variable)


def test_iot2_variable_constructor_exists():
    assert callable(iot2_Variable.__init__)


def test_iot2_variable_constructor_args():
    sig = inspect.signature(iot2_Variable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_iot2_variable_has_name():
    assert hasattr(iot2_Variable, "name")
    descriptor = None
    for klass in iot2_Variable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_iot2_activitynode_is_not_abstract():
    assert not inspect.isabstract(iot2_ActivityNode)


def test_iot2_activitynode_constructor_exists():
    assert callable(iot2_ActivityNode.__init__)


def test_iot2_activitynode_constructor_args():
    sig = inspect.signature(iot2_ActivityNode.__init__)
    params = list(sig.parameters.keys())
    assert "running" in params, "Missing parameter 'running'"

def test_iot2_activitynode_has_running():
    assert hasattr(iot2_ActivityNode, "running")
    descriptor = None
    for klass in iot2_ActivityNode.__mro__:
        if "running" in klass.__dict__:
            descriptor = klass.__dict__["running"]
            break
    assert isinstance(descriptor, property)



def test_iot2_activityedge_is_not_abstract():
    assert not inspect.isabstract(iot2_ActivityEdge)


def test_iot2_activityedge_constructor_exists():
    assert callable(iot2_ActivityEdge.__init__)


def test_iot2_activityedge_constructor_args():
    sig = inspect.signature(iot2_ActivityEdge.__init__)
    params = list(sig.parameters.keys())



def test_iot2_typedefdef_is_not_abstract():
    assert not inspect.isabstract(iot2_TypedefDef)


def test_iot2_typedefdef_constructor_exists():
    assert callable(iot2_TypedefDef.__init__)


def test_iot2_typedefdef_constructor_args():
    sig = inspect.signature(iot2_TypedefDef.__init__)
    params = list(sig.parameters.keys())



def test_iot2_idltype_is_not_abstract():
    assert not inspect.isabstract(iot2_IDLType)


def test_iot2_idltype_constructor_exists():
    assert callable(iot2_IDLType.__init__)


def test_iot2_idltype_constructor_args():
    sig = inspect.signature(iot2_IDLType.__init__)
    params = list(sig.parameters.keys())
    assert "typeCode" in params, "Missing parameter 'typeCode'"

def test_iot2_idltype_has_typeCode():
    assert hasattr(iot2_IDLType, "typeCode")
    descriptor = None
    for klass in iot2_IDLType.__mro__:
        if "typeCode" in klass.__dict__:
            descriptor = klass.__dict__["typeCode"]
            break
    assert isinstance(descriptor, property)



def test_iot2_typed_is_not_abstract():
    assert not inspect.isabstract(iot2_Typed)


def test_iot2_typed_constructor_exists():
    assert callable(iot2_Typed.__init__)


def test_iot2_typed_constructor_args():
    sig = inspect.signature(iot2_Typed.__init__)
    params = list(sig.parameters.keys())



def test_iot2_namedelement_is_not_abstract():
    assert not inspect.isabstract(iot2_NamedElement)


def test_iot2_namedelement_constructor_exists():
    assert callable(iot2_NamedElement.__init__)


def test_iot2_namedelement_constructor_args():
    sig = inspect.signature(iot2_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "identifier" in params, "Missing parameter 'identifier'"

def test_iot2_namedelement_has_name():
    assert hasattr(iot2_NamedElement, "name")
    descriptor = None
    for klass in iot2_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_iot2_namedelement_has_identifier():
    assert hasattr(iot2_NamedElement, "identifier")
    descriptor = None
    for klass in iot2_NamedElement.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)



def test_iot2_container_is_not_abstract():
    assert not inspect.isabstract(iot2_Container)


def test_iot2_container_constructor_exists():
    assert callable(iot2_Container.__init__)


def test_iot2_container_constructor_args():
    sig = inspect.signature(iot2_Container.__init__)
    params = list(sig.parameters.keys())



def test_iot2_contained_is_not_abstract():
    assert not inspect.isabstract(iot2_Contained)


def test_iot2_contained_constructor_exists():
    assert callable(iot2_Contained.__init__)


def test_iot2_contained_constructor_args():
    sig = inspect.signature(iot2_Contained.__init__)
    params = list(sig.parameters.keys())
    assert "repositoryId" in params, "Missing parameter 'repositoryId'"
    assert "absoluteName" in params, "Missing parameter 'absoluteName'"
    assert "version" in params, "Missing parameter 'version'"

def test_iot2_contained_has_repositoryId():
    assert hasattr(iot2_Contained, "repositoryId")
    descriptor = None
    for klass in iot2_Contained.__mro__:
        if "repositoryId" in klass.__dict__:
            descriptor = klass.__dict__["repositoryId"]
            break
    assert isinstance(descriptor, property)

def test_iot2_contained_has_absoluteName():
    assert hasattr(iot2_Contained, "absoluteName")
    descriptor = None
    for klass in iot2_Contained.__mro__:
        if "absoluteName" in klass.__dict__:
            descriptor = klass.__dict__["absoluteName"]
            break
    assert isinstance(descriptor, property)

def test_iot2_contained_has_version():
    assert hasattr(iot2_Contained, "version")
    descriptor = None
    for klass in iot2_Contained.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)



def test_iot2_block_is_not_abstract():
    assert not inspect.isabstract(iot2_Block)


def test_iot2_block_constructor_exists():
    assert callable(iot2_Block.__init__)


def test_iot2_block_constructor_args():
    sig = inspect.signature(iot2_Block.__init__)
    params = list(sig.parameters.keys())



def test_iot2_exceptiondef_is_not_abstract():
    assert not inspect.isabstract(iot2_ExceptionDef)


def test_iot2_exceptiondef_constructor_exists():
    assert callable(iot2_ExceptionDef.__init__)


def test_iot2_exceptiondef_constructor_args():
    sig = inspect.signature(iot2_ExceptionDef.__init__)
    params = list(sig.parameters.keys())
    assert "typeCode" in params, "Missing parameter 'typeCode'"

def test_iot2_exceptiondef_has_typeCode():
    assert hasattr(iot2_ExceptionDef, "typeCode")
    descriptor = None
    for klass in iot2_ExceptionDef.__mro__:
        if "typeCode" in klass.__dict__:
            descriptor = klass.__dict__["typeCode"]
            break
    assert isinstance(descriptor, property)



def test_hwcomponent_is_not_abstract():
    assert not inspect.isabstract(HWComponent)


def test_hwcomponent_constructor_exists():
    assert callable(HWComponent.__init__)


def test_hwcomponent_constructor_args():
    sig = inspect.signature(HWComponent.__init__)
    params = list(sig.parameters.keys())



def test_iot2_actuator_is_not_abstract():
    assert not inspect.isabstract(iot2_Actuator)


def test_iot2_actuator_constructor_exists():
    assert callable(iot2_Actuator.__init__)


def test_iot2_actuator_constructor_args():
    sig = inspect.signature(iot2_Actuator.__init__)
    params = list(sig.parameters.keys())



def test_iot2_sensor_is_not_abstract():
    assert not inspect.isabstract(iot2_Sensor)


def test_iot2_sensor_constructor_exists():
    assert callable(iot2_Sensor.__init__)


def test_iot2_sensor_constructor_args():
    sig = inspect.signature(iot2_Sensor.__init__)
    params = list(sig.parameters.keys())



def test_iot2_operationdef_is_not_abstract():
    assert not inspect.isabstract(iot2_OperationDef)


def test_iot2_operationdef_constructor_exists():
    assert callable(iot2_OperationDef.__init__)


def test_iot2_operationdef_constructor_args():
    sig = inspect.signature(iot2_OperationDef.__init__)
    params = list(sig.parameters.keys())
    assert "isOneway" in params, "Missing parameter 'isOneway'"
    assert "contexts" in params, "Missing parameter 'contexts'"

def test_iot2_operationdef_has_isOneway():
    assert hasattr(iot2_OperationDef, "isOneway")
    descriptor = None
    for klass in iot2_OperationDef.__mro__:
        if "isOneway" in klass.__dict__:
            descriptor = klass.__dict__["isOneway"]
            break
    assert isinstance(descriptor, property)

def test_iot2_operationdef_has_contexts():
    assert hasattr(iot2_OperationDef, "contexts")
    descriptor = None
    for klass in iot2_OperationDef.__mro__:
        if "contexts" in klass.__dict__:
            descriptor = klass.__dict__["contexts"]
            break
    assert isinstance(descriptor, property)



def test_iot2_activity_is_not_abstract():
    assert not inspect.isabstract(iot2_Activity)


def test_iot2_activity_constructor_exists():
    assert callable(iot2_Activity.__init__)


def test_iot2_activity_constructor_args():
    sig = inspect.signature(iot2_Activity.__init__)
    params = list(sig.parameters.keys())



def test_iot2_sketch_is_not_abstract():
    assert not inspect.isabstract(iot2_Sketch)


def test_iot2_sketch_constructor_exists():
    assert callable(iot2_Sketch.__init__)


def test_iot2_sketch_constructor_args():
    sig = inspect.signature(iot2_Sketch.__init__)
    params = list(sig.parameters.keys())



def test_iot2_board_is_not_abstract():
    assert not inspect.isabstract(iot2_Board)


def test_iot2_board_constructor_exists():
    assert callable(iot2_Board.__init__)


def test_iot2_board_constructor_args():
    sig = inspect.signature(iot2_Board.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"

def test_iot2_board_has_type():
    assert hasattr(iot2_Board, "type")
    descriptor = None
    for klass in iot2_Board.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_iot2_board_has_name():
    assert hasattr(iot2_Board, "name")
    descriptor = None
    for klass in iot2_Board.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_iot2_hwcomponent_is_not_abstract():
    assert not inspect.isabstract(iot2_HWComponent)


def test_iot2_hwcomponent_constructor_exists():
    assert callable(iot2_HWComponent.__init__)


def test_iot2_hwcomponent_constructor_args():
    sig = inspect.signature(iot2_HWComponent.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_iot2_hwcomponent_has_name():
    assert hasattr(iot2_HWComponent, "name")
    descriptor = None
    for klass in iot2_HWComponent.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_iot2_system_is_not_abstract():
    assert not inspect.isabstract(iot2_System)


def test_iot2_system_constructor_exists():
    assert callable(iot2_System.__init__)


def test_iot2_system_constructor_args():
    sig = inspect.signature(iot2_System.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_iot2_system_has_name():
    assert hasattr(iot2_System, "name")
    descriptor = None
    for klass in iot2_System.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_iot2_trace_is_not_abstract():
    assert not inspect.isabstract(iot2_Trace)


def test_iot2_trace_constructor_exists():
    assert callable(iot2_Trace.__init__)


def test_iot2_trace_constructor_args():
    sig = inspect.signature(iot2_Trace.__init__)
    params = list(sig.parameters.keys())



def test_integerexpression_is_not_abstract():
    assert not inspect.isabstract(IntegerExpression)


def test_integerexpression_constructor_exists():
    assert callable(IntegerExpression.__init__)


def test_integerexpression_constructor_args():
    sig = inspect.signature(IntegerExpression.__init__)
    params = list(sig.parameters.keys())



def test_iot2_integercomparisonexpression_is_not_abstract():
    assert not inspect.isabstract(iot2_IntegerComparisonExpression)


def test_iot2_integercomparisonexpression_constructor_exists():
    assert callable(iot2_IntegerComparisonExpression.__init__)


def test_iot2_integercomparisonexpression_constructor_args():
    sig = inspect.signature(iot2_IntegerComparisonExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_iot2_integercomparisonexpression_has_operator():
    assert hasattr(iot2_IntegerComparisonExpression, "operator")
    descriptor = None
    for klass in iot2_IntegerComparisonExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_iot2_integercalculationexpression_is_not_abstract():
    assert not inspect.isabstract(iot2_IntegerCalculationExpression)


def test_iot2_integercalculationexpression_constructor_exists():
    assert callable(iot2_IntegerCalculationExpression.__init__)


def test_iot2_integercalculationexpression_constructor_args():
    sig = inspect.signature(iot2_IntegerCalculationExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_iot2_integercalculationexpression_has_operator():
    assert hasattr(iot2_IntegerCalculationExpression, "operator")
    descriptor = None
    for klass in iot2_IntegerCalculationExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_iot2_booleanexpression_is_not_abstract():
    assert not inspect.isabstract(iot2_BooleanExpression)


def test_iot2_booleanexpression_constructor_exists():
    assert callable(iot2_BooleanExpression.__init__)


def test_iot2_booleanexpression_constructor_args():
    sig = inspect.signature(iot2_BooleanExpression.__init__)
    params = list(sig.parameters.keys())



def test_iot2_token_is_not_abstract():
    assert not inspect.isabstract(iot2_Token)


def test_iot2_token_constructor_exists():
    assert callable(iot2_Token.__init__)


def test_iot2_token_constructor_args():
    sig = inspect.signature(iot2_Token.__init__)
    params = list(sig.parameters.keys())



def test_iot2_input_is_not_abstract():
    assert not inspect.isabstract(iot2_Input)


def test_iot2_input_constructor_exists():
    assert callable(iot2_Input.__init__)


def test_iot2_input_constructor_args():
    sig = inspect.signature(iot2_Input.__init__)
    params = list(sig.parameters.keys())



def test_iot2_inputvalue_is_not_abstract():
    assert not inspect.isabstract(iot2_InputValue)


def test_iot2_inputvalue_constructor_exists():
    assert callable(iot2_InputValue.__init__)


def test_iot2_inputvalue_constructor_args():
    sig = inspect.signature(iot2_InputValue.__init__)
    params = list(sig.parameters.keys())



def test_booleanexpression_is_not_abstract():
    assert not inspect.isabstract(BooleanExpression)


def test_booleanexpression_constructor_exists():
    assert callable(BooleanExpression.__init__)


def test_booleanexpression_constructor_args():
    sig = inspect.signature(BooleanExpression.__init__)
    params = list(sig.parameters.keys())



def test_iot2_booleanbinaryexpression_is_not_abstract():
    assert not inspect.isabstract(iot2_BooleanBinaryExpression)


def test_iot2_booleanbinaryexpression_constructor_exists():
    assert callable(iot2_BooleanBinaryExpression.__init__)


def test_iot2_booleanbinaryexpression_constructor_args():
    sig = inspect.signature(iot2_BooleanBinaryExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_iot2_booleanbinaryexpression_has_operator():
    assert hasattr(iot2_BooleanBinaryExpression, "operator")
    descriptor = None
    for klass in iot2_BooleanBinaryExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_iot2_booleanunaryexpression_is_not_abstract():
    assert not inspect.isabstract(iot2_BooleanUnaryExpression)


def test_iot2_booleanunaryexpression_constructor_exists():
    assert callable(iot2_BooleanUnaryExpression.__init__)


def test_iot2_booleanunaryexpression_constructor_args():
    sig = inspect.signature(iot2_BooleanUnaryExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_iot2_booleanunaryexpression_has_operator():
    assert hasattr(iot2_BooleanUnaryExpression, "operator")
    descriptor = None
    for klass in iot2_BooleanUnaryExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_action_constructor_exists():
    assert callable(Action.__init__)


def test_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_iot2_opaqueaction_is_not_abstract():
    assert not inspect.isabstract(iot2_OpaqueAction)


def test_iot2_opaqueaction_constructor_exists():
    assert callable(iot2_OpaqueAction.__init__)


def test_iot2_opaqueaction_constructor_args():
    sig = inspect.signature(iot2_OpaqueAction.__init__)
    params = list(sig.parameters.keys())



def test_executablenode_is_not_abstract():
    assert not inspect.isabstract(ExecutableNode)


def test_executablenode_constructor_exists():
    assert callable(ExecutableNode.__init__)


def test_executablenode_constructor_args():
    sig = inspect.signature(ExecutableNode.__init__)
    params = list(sig.parameters.keys())



def test_iot2_action_is_not_abstract():
    assert not inspect.isabstract(iot2_Action)


def test_iot2_action_constructor_exists():
    assert callable(iot2_Action.__init__)


def test_iot2_action_constructor_args():
    sig = inspect.signature(iot2_Action.__init__)
    params = list(sig.parameters.keys())



def test_activitynode_is_not_abstract():
    assert not inspect.isabstract(ActivityNode)


def test_activitynode_constructor_exists():
    assert callable(ActivityNode.__init__)


def test_activitynode_constructor_args():
    sig = inspect.signature(ActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_iot2_executablenode_is_not_abstract():
    assert not inspect.isabstract(iot2_ExecutableNode)


def test_iot2_executablenode_constructor_exists():
    assert callable(iot2_ExecutableNode.__init__)


def test_iot2_executablenode_constructor_args():
    sig = inspect.signature(iot2_ExecutableNode.__init__)
    params = list(sig.parameters.keys())



def test_iot2_controlnode_is_not_abstract():
    assert not inspect.isabstract(iot2_ControlNode)


def test_iot2_controlnode_constructor_exists():
    assert callable(iot2_ControlNode.__init__)


def test_iot2_controlnode_constructor_args():
    sig = inspect.signature(iot2_ControlNode.__init__)
    params = list(sig.parameters.keys())



def test_activityedge_is_not_abstract():
    assert not inspect.isabstract(ActivityEdge)


def test_activityedge_constructor_exists():
    assert callable(ActivityEdge.__init__)


def test_activityedge_constructor_args():
    sig = inspect.signature(ActivityEdge.__init__)
    params = list(sig.parameters.keys())



def test_iot2_controlflow_is_not_abstract():
    assert not inspect.isabstract(iot2_ControlFlow)


def test_iot2_controlflow_constructor_exists():
    assert callable(iot2_ControlFlow.__init__)


def test_iot2_controlflow_constructor_args():
    sig = inspect.signature(iot2_ControlFlow.__init__)
    params = list(sig.parameters.keys())



def test_iot2_integerexpression_is_not_abstract():
    assert not inspect.isabstract(iot2_IntegerExpression)


def test_iot2_integerexpression_constructor_exists():
    assert callable(iot2_IntegerExpression.__init__)


def test_iot2_integerexpression_constructor_args():
    sig = inspect.signature(iot2_IntegerExpression.__init__)
    params = list(sig.parameters.keys())



def test_value_is_not_abstract():
    assert not inspect.isabstract(Value)


def test_value_constructor_exists():
    assert callable(Value.__init__)


def test_value_constructor_args():
    sig = inspect.signature(Value.__init__)
    params = list(sig.parameters.keys())



def test_iot2_integervalue_is_not_abstract():
    assert not inspect.isabstract(iot2_IntegerValue)


def test_iot2_integervalue_constructor_exists():
    assert callable(iot2_IntegerValue.__init__)


def test_iot2_integervalue_constructor_args():
    sig = inspect.signature(iot2_IntegerValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_iot2_integervalue_has_value():
    assert hasattr(iot2_IntegerValue, "value")
    descriptor = None
    for klass in iot2_IntegerValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_iot2_booleanvalue_is_not_abstract():
    assert not inspect.isabstract(iot2_BooleanValue)


def test_iot2_booleanvalue_constructor_exists():
    assert callable(iot2_BooleanValue.__init__)


def test_iot2_booleanvalue_constructor_args():
    sig = inspect.signature(iot2_BooleanValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_iot2_booleanvalue_has_value():
    assert hasattr(iot2_BooleanValue, "value")
    descriptor = None
    for klass in iot2_BooleanValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_variable_is_not_abstract():
    assert not inspect.isabstract(Variable)


def test_variable_constructor_exists():
    assert callable(Variable.__init__)


def test_variable_constructor_args():
    sig = inspect.signature(Variable.__init__)
    params = list(sig.parameters.keys())



def test_iot2_booleanvariable_is_not_abstract():
    assert not inspect.isabstract(iot2_BooleanVariable)


def test_iot2_booleanvariable_constructor_exists():
    assert callable(iot2_BooleanVariable.__init__)


def test_iot2_booleanvariable_constructor_args():
    sig = inspect.signature(iot2_BooleanVariable.__init__)
    params = list(sig.parameters.keys())



def test_iot2_integervariable_is_not_abstract():
    assert not inspect.isabstract(iot2_IntegerVariable)


def test_iot2_integervariable_constructor_exists():
    assert callable(iot2_IntegerVariable.__init__)


def test_iot2_integervariable_constructor_args():
    sig = inspect.signature(iot2_IntegerVariable.__init__)
    params = list(sig.parameters.keys())

def test_integercomparisonoperator_exists():
    # Check that the Enumeration exists
    assert IntegerComparisonOperator is not None

def test_integercomparisonoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in IntegerComparisonOperator]
    expected_literals = [
        "SMALLER_EQUALS",
        "GREATER",
        "GREATER_EQUALS",
        "SMALLER",
        "EQUALS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in IntegerComparisonOperator"

def test_boardtype_exists():
    # Check that the Enumeration exists
    assert BoardType is not None

def test_boardtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BoardType]
    expected_literals = [
        "BeagleBoard",
        "RaspberryPi",
        "Arduino",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BoardType"

def test_booleanunaryoperator_exists():
    # Check that the Enumeration exists
    assert BooleanUnaryOperator is not None

def test_booleanunaryoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BooleanUnaryOperator]
    expected_literals = [
        "NOT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BooleanUnaryOperator"

def test_parametermode_exists():
    # Check that the Enumeration exists
    assert ParameterMode is not None

def test_parametermode_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ParameterMode]
    expected_literals = [
        "PARAM_IN",
        "PARAM_INOUT",
        "PARAM_OUT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ParameterMode"

def test_primitivekind_exists():
    # Check that the Enumeration exists
    assert PrimitiveKind is not None

def test_primitivekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PrimitiveKind]
    expected_literals = [
        "PK_DOUBLE",
        "PK_LONG",
        "PK_ANY",
        "PK_TYPECODE",
        "PK_WSTRING",
        "PK_LONGLONG",
        "PK_CHAR",
        "PK_NULL",
        "PK_ULONGLONG",
        "PK_USHORT",
        "PK_OBJREF",
        "PK_ULONG",
        "PK_FLOAT",
        "PK_SHORT",
        "PK_OCTET",
        "PK_VOID",
        "PK_WCHAR",
        "PK_LONGDOUBLE",
        "PK_STRING",
        "PK_BOOLEAN",
        "PK_PRINCIPAL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PrimitiveKind"

def test_integercalculationoperator_exists():
    # Check that the Enumeration exists
    assert IntegerCalculationOperator is not None

def test_integercalculationoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in IntegerCalculationOperator]
    expected_literals = [
        "SUBRACT",
        "ADD",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in IntegerCalculationOperator"

def test_booleanbinaryoperator_exists():
    # Check that the Enumeration exists
    assert BooleanBinaryOperator is not None

def test_booleanbinaryoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BooleanBinaryOperator]
    expected_literals = [
        "AND",
        "OR",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BooleanBinaryOperator"


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
iot2_Value_strategy = st.builds(
    iot2_Value,
)
FinalNode_strategy = st.builds(
    FinalNode,
)
iot2_ActivityFinalNode_strategy = st.builds(
    iot2_ActivityFinalNode,
)
ControlNode_strategy = st.builds(
    ControlNode,
)
iot2_FinalNode_strategy = st.builds(
    iot2_FinalNode,
)
iot2_ForkNode_strategy = st.builds(
    iot2_ForkNode,
)
iot2_MergeNode_strategy = st.builds(
    iot2_MergeNode,
)
iot2_DecisionNode_strategy = st.builds(
    iot2_DecisionNode,
)
iot2_JoinNode_strategy = st.builds(
    iot2_JoinNode,
)
iot2_InitialNode_strategy = st.builds(
    iot2_InitialNode,
)
Expression_strategy = st.builds(
    Expression,
)
iot2_Expression_CallMemberFunction_strategy = st.builds(
    iot2_Expression_CallMemberFunction,
    memberFunctionName=
        safe_text
)
iot2_Expression_Exponentiation_strategy = st.builds(
    iot2_Expression_Exponentiation,
)
iot2_Expression_Equal_strategy = st.builds(
    iot2_Expression_Equal,
)
iot2_Expression_AccessArray_strategy = st.builds(
    iot2_Expression_AccessArray,
)
iot2_Expression_String_strategy = st.builds(
    iot2_Expression_String,
    value=
        safe_text
)
iot2_Expression_Smaller_Equal_strategy = st.builds(
    iot2_Expression_Smaller_Equal,
)
iot2_Expression_Negate_strategy = st.builds(
    iot2_Expression_Negate,
)
iot2_Expression_Plus_strategy = st.builds(
    iot2_Expression_Plus,
)
iot2_Expression_Or_strategy = st.builds(
    iot2_Expression_Or,
)
iot2_Expression_CallFunction_strategy = st.builds(
    iot2_Expression_CallFunction,
)
iot2_Expression_Not_Equal_strategy = st.builds(
    iot2_Expression_Not_Equal,
)
iot2_Expression_Division_strategy = st.builds(
    iot2_Expression_Division,
)
iot2_Expression_Smaller_strategy = st.builds(
    iot2_Expression_Smaller,
)
iot2_Expression_Length_strategy = st.builds(
    iot2_Expression_Length,
)
iot2_Expression_Larger_Equal_strategy = st.builds(
    iot2_Expression_Larger_Equal,
)
iot2_Expression_Modulo_strategy = st.builds(
    iot2_Expression_Modulo,
)
iot2_Expression_Number_strategy = st.builds(
    iot2_Expression_Number,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
iot2_Expression_Invert_strategy = st.builds(
    iot2_Expression_Invert,
)
iot2_Expression_Multiplication_strategy = st.builds(
    iot2_Expression_Multiplication,
)
iot2_Expression_Concatenation_strategy = st.builds(
    iot2_Expression_Concatenation,
)
iot2_Expression_AccessMember_strategy = st.builds(
    iot2_Expression_AccessMember,
    memberName=
        safe_text
)
iot2_Expression_And_strategy = st.builds(
    iot2_Expression_And,
)
iot2_Expression_VarArgs_strategy = st.builds(
    iot2_Expression_VarArgs,
)
iot2_Expression_True_strategy = st.builds(
    iot2_Expression_True,
)
iot2_Expression_Function_strategy = st.builds(
    iot2_Expression_Function,
)
iot2_Expression_False_strategy = st.builds(
    iot2_Expression_False,
)
iot2_Expression_VariableName_strategy = st.builds(
    iot2_Expression_VariableName,
    variable=
        safe_text
)
iot2_Expression_Larger_strategy = st.builds(
    iot2_Expression_Larger,
)
iot2_Expression_Minus_strategy = st.builds(
    iot2_Expression_Minus,
)
iot2_Expression_Nil_strategy = st.builds(
    iot2_Expression_Nil,
)
Statement_FunctioncallOrAssignment_strategy = st.builds(
    Statement_FunctioncallOrAssignment,
)
iot2_Statement_CallMemberFunction_strategy = st.builds(
    iot2_Statement_CallMemberFunction,
    memberFunctionName=
        safe_text
)
iot2_Statement_CallFunction_strategy = st.builds(
    iot2_Statement_CallFunction,
)
iot2_Statement_Assignment_strategy = st.builds(
    iot2_Statement_Assignment,
)
LastStatement_Return_strategy = st.builds(
    LastStatement_Return,
)
iot2_LastStatement_ReturnWithValue_strategy = st.builds(
    iot2_LastStatement_ReturnWithValue,
)
Field_strategy = st.builds(
    Field,
)
iot2_Field_AddEntryToTable_strategy = st.builds(
    iot2_Field_AddEntryToTable,
    key=
        safe_text
)
iot2_Field_AppendEntryToTable_strategy = st.builds(
    iot2_Field_AppendEntryToTable,
)
iot2_Field_AddEntryToTable_Brackets_strategy = st.builds(
    iot2_Field_AddEntryToTable_Brackets,
)
iot2_Functioncall_Arguments_strategy = st.builds(
    iot2_Functioncall_Arguments,
)
iot2_Expression_TableConstructor_strategy = st.builds(
    iot2_Expression_TableConstructor,
)
iot2_Statement_If_Then_Else_ElseIfPart_strategy = st.builds(
    iot2_Statement_If_Then_Else_ElseIfPart,
)
iot2_Function_strategy = st.builds(
    iot2_Function,
    varArgs=
        st.booleans(),
    parameters=
        safe_text
)
iot2_Expression_strategy = st.builds(
    iot2_Expression,
)
IDLType_strategy = st.builds(
    IDLType,
)
Statement_strategy = st.builds(
    Statement,
)
iot2_Statement_Repeat_strategy = st.builds(
    iot2_Statement_Repeat,
)
iot2_Statement_FunctioncallOrAssignment_strategy = st.builds(
    iot2_Statement_FunctioncallOrAssignment,
)
iot2_Statement_For_Generic_strategy = st.builds(
    iot2_Statement_For_Generic,
    names=
        safe_text
)
iot2_Statement_Local_Variable_Declaration_strategy = st.builds(
    iot2_Statement_Local_Variable_Declaration,
    variableNames=
        safe_text
)
iot2_Statement_LocalFunction_Declaration_strategy = st.builds(
    iot2_Statement_LocalFunction_Declaration,
    functionName=
        safe_text
)
iot2_Statement_While_strategy = st.builds(
    iot2_Statement_While,
)
iot2_Statement_GlobalFunction_Declaration_strategy = st.builds(
    iot2_Statement_GlobalFunction_Declaration,
    prefix=
        safe_text,
    functionName=
        safe_text
)
iot2_Statement_For_Numeric_strategy = st.builds(
    iot2_Statement_For_Numeric,
    iteratorName=
        safe_text
)
iot2_Statement_If_Then_Else_strategy = st.builds(
    iot2_Statement_If_Then_Else,
)
iot2_Statement_Block_strategy = st.builds(
    iot2_Statement_Block,
)
LastStatement_strategy = st.builds(
    LastStatement,
)
iot2_LastStatement_Break_strategy = st.builds(
    iot2_LastStatement_Break,
)
iot2_LastStatement_Return_strategy = st.builds(
    iot2_LastStatement_Return,
)
iot2_LastStatement_strategy = st.builds(
    iot2_LastStatement,
)
iot2_Statement_strategy = st.builds(
    iot2_Statement,
)
Chunk_strategy = st.builds(
    Chunk,
)
iot2_Chunk_strategy = st.builds(
    iot2_Chunk,
)
iot2_PrimitiveDef_strategy = st.builds(
    iot2_PrimitiveDef,
    kind=
        safe_text
)
Typed_strategy = st.builds(
    Typed,
)
iot2_Field_strategy = st.builds(
    iot2_Field,
    identifier=
        safe_text
)
iot2_ParameterDef_strategy = st.builds(
    iot2_ParameterDef,
    direction=
        safe_text,
    identifier=
        safe_text
)
Contained_strategy = st.builds(
    Contained,
)
iot2_Variable_strategy = st.builds(
    iot2_Variable,
    name=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
iot2_ActivityNode_strategy = st.builds(
    iot2_ActivityNode,
    running=
        st.booleans()
)
iot2_ActivityEdge_strategy = st.builds(
    iot2_ActivityEdge,
)
iot2_TypedefDef_strategy = st.builds(
    iot2_TypedefDef,
)
iot2_IDLType_strategy = st.builds(
    iot2_IDLType,
    typeCode=
        safe_text
)
iot2_Typed_strategy = st.builds(
    iot2_Typed,
)
iot2_NamedElement_strategy = st.builds(
    iot2_NamedElement,
    name=
        safe_text,
    identifier=
        safe_text
)
iot2_Container_strategy = st.builds(
    iot2_Container,
)
iot2_Contained_strategy = st.builds(
    iot2_Contained,
    repositoryId=
        safe_text,
    absoluteName=
        safe_text,
    version=
        safe_text
)
iot2_Block_strategy = st.builds(
    iot2_Block,
)
iot2_ExceptionDef_strategy = st.builds(
    iot2_ExceptionDef,
    typeCode=
        safe_text
)
HWComponent_strategy = st.builds(
    HWComponent,
)
iot2_Actuator_strategy = st.builds(
    iot2_Actuator,
)
iot2_Sensor_strategy = st.builds(
    iot2_Sensor,
)
iot2_OperationDef_strategy = st.builds(
    iot2_OperationDef,
    isOneway=
        st.booleans(),
    contexts=
        safe_text
)
iot2_Activity_strategy = st.builds(
    iot2_Activity,
)
iot2_Sketch_strategy = st.builds(
    iot2_Sketch,
)
iot2_Board_strategy = st.builds(
    iot2_Board,
    type=
        safe_text,
    name=
        safe_text
)
iot2_HWComponent_strategy = st.builds(
    iot2_HWComponent,
    name=
        safe_text
)
iot2_System_strategy = st.builds(
    iot2_System,
    name=
        safe_text
)
iot2_Trace_strategy = st.builds(
    iot2_Trace,
)
IntegerExpression_strategy = st.builds(
    IntegerExpression,
)
iot2_IntegerComparisonExpression_strategy = st.builds(
    iot2_IntegerComparisonExpression,
    operator=
        safe_text
)
iot2_IntegerCalculationExpression_strategy = st.builds(
    iot2_IntegerCalculationExpression,
    operator=
        safe_text
)
iot2_BooleanExpression_strategy = st.builds(
    iot2_BooleanExpression,
)
iot2_Token_strategy = st.builds(
    iot2_Token,
)
iot2_Input_strategy = st.builds(
    iot2_Input,
)
iot2_InputValue_strategy = st.builds(
    iot2_InputValue,
)
BooleanExpression_strategy = st.builds(
    BooleanExpression,
)
iot2_BooleanBinaryExpression_strategy = st.builds(
    iot2_BooleanBinaryExpression,
    operator=
        safe_text
)
iot2_BooleanUnaryExpression_strategy = st.builds(
    iot2_BooleanUnaryExpression,
    operator=
        safe_text
)
Action_strategy = st.builds(
    Action,
)
iot2_OpaqueAction_strategy = st.builds(
    iot2_OpaqueAction,
)
ExecutableNode_strategy = st.builds(
    ExecutableNode,
)
iot2_Action_strategy = st.builds(
    iot2_Action,
)
ActivityNode_strategy = st.builds(
    ActivityNode,
)
iot2_ExecutableNode_strategy = st.builds(
    iot2_ExecutableNode,
)
iot2_ControlNode_strategy = st.builds(
    iot2_ControlNode,
)
ActivityEdge_strategy = st.builds(
    ActivityEdge,
)
iot2_ControlFlow_strategy = st.builds(
    iot2_ControlFlow,
)
iot2_IntegerExpression_strategy = st.builds(
    iot2_IntegerExpression,
)
Value_strategy = st.builds(
    Value,
)
iot2_IntegerValue_strategy = st.builds(
    iot2_IntegerValue,
    value=
        st.integers()
)
iot2_BooleanValue_strategy = st.builds(
    iot2_BooleanValue,
    value=
        st.booleans()
)
Variable_strategy = st.builds(
    Variable,
)
iot2_BooleanVariable_strategy = st.builds(
    iot2_BooleanVariable,
)
iot2_IntegerVariable_strategy = st.builds(
    iot2_IntegerVariable,
)

@given(instance=iot2_Value_strategy)
@settings(max_examples=50)
def test_iot2_value_instantiation(instance):
    assert isinstance(instance, iot2_Value)

@given(instance=FinalNode_strategy)
@settings(max_examples=50)
def test_finalnode_instantiation(instance):
    assert isinstance(instance, FinalNode)

@given(instance=iot2_ActivityFinalNode_strategy)
@settings(max_examples=50)
def test_iot2_activityfinalnode_instantiation(instance):
    assert isinstance(instance, iot2_ActivityFinalNode)

@given(instance=ControlNode_strategy)
@settings(max_examples=50)
def test_controlnode_instantiation(instance):
    assert isinstance(instance, ControlNode)

@given(instance=iot2_FinalNode_strategy)
@settings(max_examples=50)
def test_iot2_finalnode_instantiation(instance):
    assert isinstance(instance, iot2_FinalNode)

@given(instance=iot2_ForkNode_strategy)
@settings(max_examples=50)
def test_iot2_forknode_instantiation(instance):
    assert isinstance(instance, iot2_ForkNode)

@given(instance=iot2_MergeNode_strategy)
@settings(max_examples=50)
def test_iot2_mergenode_instantiation(instance):
    assert isinstance(instance, iot2_MergeNode)

@given(instance=iot2_DecisionNode_strategy)
@settings(max_examples=50)
def test_iot2_decisionnode_instantiation(instance):
    assert isinstance(instance, iot2_DecisionNode)

@given(instance=iot2_JoinNode_strategy)
@settings(max_examples=50)
def test_iot2_joinnode_instantiation(instance):
    assert isinstance(instance, iot2_JoinNode)

@given(instance=iot2_InitialNode_strategy)
@settings(max_examples=50)
def test_iot2_initialnode_instantiation(instance):
    assert isinstance(instance, iot2_InitialNode)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=iot2_Expression_CallMemberFunction_strategy)
@settings(max_examples=50)
def test_iot2_expression_callmemberfunction_instantiation(instance):
    assert isinstance(instance, iot2_Expression_CallMemberFunction)



@given(instance=iot2_Expression_CallMemberFunction_strategy)
def test_iot2_expression_callmemberfunction_memberFunctionName_setter(instance):
    original = instance.memberFunctionName
    instance.memberFunctionName = original
    assert instance.memberFunctionName == original

@given(instance=iot2_Expression_Exponentiation_strategy)
@settings(max_examples=50)
def test_iot2_expression_exponentiation_instantiation(instance):
    assert isinstance(instance, iot2_Expression_Exponentiation)

@given(instance=iot2_Expression_Equal_strategy)
@settings(max_examples=50)
def test_iot2_expression_equal_instantiation(instance):
    assert isinstance(instance, iot2_Expression_Equal)

@given(instance=iot2_Expression_AccessArray_strategy)
@settings(max_examples=50)
def test_iot2_expression_accessarray_instantiation(instance):
    assert isinstance(instance, iot2_Expression_AccessArray)

@given(instance=iot2_Expression_String_strategy)
@settings(max_examples=50)
def test_iot2_expression_string_instantiation(instance):
    assert isinstance(instance, iot2_Expression_String)



@given(instance=iot2_Expression_String_strategy)
def test_iot2_expression_string_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=iot2_Expression_Smaller_Equal_strategy)
@settings(max_examples=50)
def test_iot2_expression_smaller_equal_instantiation(instance):
    assert isinstance(instance, iot2_Expression_Smaller_Equal)

@given(instance=iot2_Expression_Negate_strategy)
@settings(max_examples=50)
def test_iot2_expression_negate_instantiation(instance):
    assert isinstance(instance, iot2_Expression_Negate)

@given(instance=iot2_Expression_Plus_strategy)
@settings(max_examples=50)
def test_iot2_expression_plus_instantiation(instance):
    assert isinstance(instance, iot2_Expression_Plus)

@given(instance=iot2_Expression_Or_strategy)
@settings(max_examples=50)
def test_iot2_expression_or_instantiation(instance):
    assert isinstance(instance, iot2_Expression_Or)

@given(instance=iot2_Expression_CallFunction_strategy)
@settings(max_examples=50)
def test_iot2_expression_callfunction_instantiation(instance):
    assert isinstance(instance, iot2_Expression_CallFunction)

@given(instance=iot2_Expression_Not_Equal_strategy)
@settings(max_examples=50)
def test_iot2_expression_not_equal_instantiation(instance):
    assert isinstance(instance, iot2_Expression_Not_Equal)

@given(instance=iot2_Expression_Division_strategy)
@settings(max_examples=50)
def test_iot2_expression_division_instantiation(instance):
    assert isinstance(instance, iot2_Expression_Division)

@given(instance=iot2_Expression_Smaller_strategy)
@settings(max_examples=50)
def test_iot2_expression_smaller_instantiation(instance):
    assert isinstance(instance, iot2_Expression_Smaller)

@given(instance=iot2_Expression_Length_strategy)
@settings(max_examples=50)
def test_iot2_expression_length_instantiation(instance):
    assert isinstance(instance, iot2_Expression_Length)

@given(instance=iot2_Expression_Larger_Equal_strategy)
@settings(max_examples=50)
def test_iot2_expression_larger_equal_instantiation(instance):
    assert isinstance(instance, iot2_Expression_Larger_Equal)

@given(instance=iot2_Expression_Modulo_strategy)
@settings(max_examples=50)
def test_iot2_expression_modulo_instantiation(instance):
    assert isinstance(instance, iot2_Expression_Modulo)

@given(instance=iot2_Expression_Number_strategy)
@settings(max_examples=50)
def test_iot2_expression_number_instantiation(instance):
    assert isinstance(instance, iot2_Expression_Number)



@given(instance=iot2_Expression_Number_strategy)
def test_iot2_expression_number_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=iot2_Expression_Invert_strategy)
@settings(max_examples=50)
def test_iot2_expression_invert_instantiation(instance):
    assert isinstance(instance, iot2_Expression_Invert)

@given(instance=iot2_Expression_Multiplication_strategy)
@settings(max_examples=50)
def test_iot2_expression_multiplication_instantiation(instance):
    assert isinstance(instance, iot2_Expression_Multiplication)

@given(instance=iot2_Expression_Concatenation_strategy)
@settings(max_examples=50)
def test_iot2_expression_concatenation_instantiation(instance):
    assert isinstance(instance, iot2_Expression_Concatenation)

@given(instance=iot2_Expression_AccessMember_strategy)
@settings(max_examples=50)
def test_iot2_expression_accessmember_instantiation(instance):
    assert isinstance(instance, iot2_Expression_AccessMember)



@given(instance=iot2_Expression_AccessMember_strategy)
def test_iot2_expression_accessmember_memberName_setter(instance):
    original = instance.memberName
    instance.memberName = original
    assert instance.memberName == original

@given(instance=iot2_Expression_And_strategy)
@settings(max_examples=50)
def test_iot2_expression_and_instantiation(instance):
    assert isinstance(instance, iot2_Expression_And)

@given(instance=iot2_Expression_VarArgs_strategy)
@settings(max_examples=50)
def test_iot2_expression_varargs_instantiation(instance):
    assert isinstance(instance, iot2_Expression_VarArgs)

@given(instance=iot2_Expression_True_strategy)
@settings(max_examples=50)
def test_iot2_expression_true_instantiation(instance):
    assert isinstance(instance, iot2_Expression_True)

@given(instance=iot2_Expression_Function_strategy)
@settings(max_examples=50)
def test_iot2_expression_function_instantiation(instance):
    assert isinstance(instance, iot2_Expression_Function)

@given(instance=iot2_Expression_False_strategy)
@settings(max_examples=50)
def test_iot2_expression_false_instantiation(instance):
    assert isinstance(instance, iot2_Expression_False)

@given(instance=iot2_Expression_VariableName_strategy)
@settings(max_examples=50)
def test_iot2_expression_variablename_instantiation(instance):
    assert isinstance(instance, iot2_Expression_VariableName)



@given(instance=iot2_Expression_VariableName_strategy)
def test_iot2_expression_variablename_variable_setter(instance):
    original = instance.variable
    instance.variable = original
    assert instance.variable == original

@given(instance=iot2_Expression_Larger_strategy)
@settings(max_examples=50)
def test_iot2_expression_larger_instantiation(instance):
    assert isinstance(instance, iot2_Expression_Larger)

@given(instance=iot2_Expression_Minus_strategy)
@settings(max_examples=50)
def test_iot2_expression_minus_instantiation(instance):
    assert isinstance(instance, iot2_Expression_Minus)

@given(instance=iot2_Expression_Nil_strategy)
@settings(max_examples=50)
def test_iot2_expression_nil_instantiation(instance):
    assert isinstance(instance, iot2_Expression_Nil)

@given(instance=Statement_FunctioncallOrAssignment_strategy)
@settings(max_examples=50)
def test_statement_functioncallorassignment_instantiation(instance):
    assert isinstance(instance, Statement_FunctioncallOrAssignment)

@given(instance=iot2_Statement_CallMemberFunction_strategy)
@settings(max_examples=50)
def test_iot2_statement_callmemberfunction_instantiation(instance):
    assert isinstance(instance, iot2_Statement_CallMemberFunction)



@given(instance=iot2_Statement_CallMemberFunction_strategy)
def test_iot2_statement_callmemberfunction_memberFunctionName_setter(instance):
    original = instance.memberFunctionName
    instance.memberFunctionName = original
    assert instance.memberFunctionName == original

@given(instance=iot2_Statement_CallFunction_strategy)
@settings(max_examples=50)
def test_iot2_statement_callfunction_instantiation(instance):
    assert isinstance(instance, iot2_Statement_CallFunction)

@given(instance=iot2_Statement_Assignment_strategy)
@settings(max_examples=50)
def test_iot2_statement_assignment_instantiation(instance):
    assert isinstance(instance, iot2_Statement_Assignment)

@given(instance=LastStatement_Return_strategy)
@settings(max_examples=50)
def test_laststatement_return_instantiation(instance):
    assert isinstance(instance, LastStatement_Return)

@given(instance=iot2_LastStatement_ReturnWithValue_strategy)
@settings(max_examples=50)
def test_iot2_laststatement_returnwithvalue_instantiation(instance):
    assert isinstance(instance, iot2_LastStatement_ReturnWithValue)

@given(instance=Field_strategy)
@settings(max_examples=50)
def test_field_instantiation(instance):
    assert isinstance(instance, Field)

@given(instance=iot2_Field_AddEntryToTable_strategy)
@settings(max_examples=50)
def test_iot2_field_addentrytotable_instantiation(instance):
    assert isinstance(instance, iot2_Field_AddEntryToTable)



@given(instance=iot2_Field_AddEntryToTable_strategy)
def test_iot2_field_addentrytotable_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=iot2_Field_AppendEntryToTable_strategy)
@settings(max_examples=50)
def test_iot2_field_appendentrytotable_instantiation(instance):
    assert isinstance(instance, iot2_Field_AppendEntryToTable)

@given(instance=iot2_Field_AddEntryToTable_Brackets_strategy)
@settings(max_examples=50)
def test_iot2_field_addentrytotable_brackets_instantiation(instance):
    assert isinstance(instance, iot2_Field_AddEntryToTable_Brackets)

@given(instance=iot2_Functioncall_Arguments_strategy)
@settings(max_examples=50)
def test_iot2_functioncall_arguments_instantiation(instance):
    assert isinstance(instance, iot2_Functioncall_Arguments)

@given(instance=iot2_Expression_TableConstructor_strategy)
@settings(max_examples=50)
def test_iot2_expression_tableconstructor_instantiation(instance):
    assert isinstance(instance, iot2_Expression_TableConstructor)

@given(instance=iot2_Statement_If_Then_Else_ElseIfPart_strategy)
@settings(max_examples=50)
def test_iot2_statement_if_then_else_elseifpart_instantiation(instance):
    assert isinstance(instance, iot2_Statement_If_Then_Else_ElseIfPart)

@given(instance=iot2_Function_strategy)
@settings(max_examples=50)
def test_iot2_function_instantiation(instance):
    assert isinstance(instance, iot2_Function)



@given(instance=iot2_Function_strategy)
def test_iot2_function_varArgs_setter(instance):
    original = instance.varArgs
    instance.varArgs = original
    assert instance.varArgs == original



@given(instance=iot2_Function_strategy)
def test_iot2_function_parameters_setter(instance):
    original = instance.parameters
    instance.parameters = original
    assert instance.parameters == original

@given(instance=iot2_Expression_strategy)
@settings(max_examples=50)
def test_iot2_expression_instantiation(instance):
    assert isinstance(instance, iot2_Expression)

@given(instance=IDLType_strategy)
@settings(max_examples=50)
def test_idltype_instantiation(instance):
    assert isinstance(instance, IDLType)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=iot2_Statement_Repeat_strategy)
@settings(max_examples=50)
def test_iot2_statement_repeat_instantiation(instance):
    assert isinstance(instance, iot2_Statement_Repeat)

@given(instance=iot2_Statement_FunctioncallOrAssignment_strategy)
@settings(max_examples=50)
def test_iot2_statement_functioncallorassignment_instantiation(instance):
    assert isinstance(instance, iot2_Statement_FunctioncallOrAssignment)

@given(instance=iot2_Statement_For_Generic_strategy)
@settings(max_examples=50)
def test_iot2_statement_for_generic_instantiation(instance):
    assert isinstance(instance, iot2_Statement_For_Generic)



@given(instance=iot2_Statement_For_Generic_strategy)
def test_iot2_statement_for_generic_names_setter(instance):
    original = instance.names
    instance.names = original
    assert instance.names == original

@given(instance=iot2_Statement_Local_Variable_Declaration_strategy)
@settings(max_examples=50)
def test_iot2_statement_local_variable_declaration_instantiation(instance):
    assert isinstance(instance, iot2_Statement_Local_Variable_Declaration)



@given(instance=iot2_Statement_Local_Variable_Declaration_strategy)
def test_iot2_statement_local_variable_declaration_variableNames_setter(instance):
    original = instance.variableNames
    instance.variableNames = original
    assert instance.variableNames == original

@given(instance=iot2_Statement_LocalFunction_Declaration_strategy)
@settings(max_examples=50)
def test_iot2_statement_localfunction_declaration_instantiation(instance):
    assert isinstance(instance, iot2_Statement_LocalFunction_Declaration)



@given(instance=iot2_Statement_LocalFunction_Declaration_strategy)
def test_iot2_statement_localfunction_declaration_functionName_setter(instance):
    original = instance.functionName
    instance.functionName = original
    assert instance.functionName == original

@given(instance=iot2_Statement_While_strategy)
@settings(max_examples=50)
def test_iot2_statement_while_instantiation(instance):
    assert isinstance(instance, iot2_Statement_While)

@given(instance=iot2_Statement_GlobalFunction_Declaration_strategy)
@settings(max_examples=50)
def test_iot2_statement_globalfunction_declaration_instantiation(instance):
    assert isinstance(instance, iot2_Statement_GlobalFunction_Declaration)



@given(instance=iot2_Statement_GlobalFunction_Declaration_strategy)
def test_iot2_statement_globalfunction_declaration_prefix_setter(instance):
    original = instance.prefix
    instance.prefix = original
    assert instance.prefix == original



@given(instance=iot2_Statement_GlobalFunction_Declaration_strategy)
def test_iot2_statement_globalfunction_declaration_functionName_setter(instance):
    original = instance.functionName
    instance.functionName = original
    assert instance.functionName == original

@given(instance=iot2_Statement_For_Numeric_strategy)
@settings(max_examples=50)
def test_iot2_statement_for_numeric_instantiation(instance):
    assert isinstance(instance, iot2_Statement_For_Numeric)



@given(instance=iot2_Statement_For_Numeric_strategy)
def test_iot2_statement_for_numeric_iteratorName_setter(instance):
    original = instance.iteratorName
    instance.iteratorName = original
    assert instance.iteratorName == original

@given(instance=iot2_Statement_If_Then_Else_strategy)
@settings(max_examples=50)
def test_iot2_statement_if_then_else_instantiation(instance):
    assert isinstance(instance, iot2_Statement_If_Then_Else)

@given(instance=iot2_Statement_Block_strategy)
@settings(max_examples=50)
def test_iot2_statement_block_instantiation(instance):
    assert isinstance(instance, iot2_Statement_Block)

@given(instance=LastStatement_strategy)
@settings(max_examples=50)
def test_laststatement_instantiation(instance):
    assert isinstance(instance, LastStatement)

@given(instance=iot2_LastStatement_Break_strategy)
@settings(max_examples=50)
def test_iot2_laststatement_break_instantiation(instance):
    assert isinstance(instance, iot2_LastStatement_Break)

@given(instance=iot2_LastStatement_Return_strategy)
@settings(max_examples=50)
def test_iot2_laststatement_return_instantiation(instance):
    assert isinstance(instance, iot2_LastStatement_Return)

@given(instance=iot2_LastStatement_strategy)
@settings(max_examples=50)
def test_iot2_laststatement_instantiation(instance):
    assert isinstance(instance, iot2_LastStatement)

@given(instance=iot2_Statement_strategy)
@settings(max_examples=50)
def test_iot2_statement_instantiation(instance):
    assert isinstance(instance, iot2_Statement)

@given(instance=Chunk_strategy)
@settings(max_examples=50)
def test_chunk_instantiation(instance):
    assert isinstance(instance, Chunk)

@given(instance=iot2_Chunk_strategy)
@settings(max_examples=50)
def test_iot2_chunk_instantiation(instance):
    assert isinstance(instance, iot2_Chunk)

@given(instance=iot2_PrimitiveDef_strategy)
@settings(max_examples=50)
def test_iot2_primitivedef_instantiation(instance):
    assert isinstance(instance, iot2_PrimitiveDef)



@given(instance=iot2_PrimitiveDef_strategy)
def test_iot2_primitivedef_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=Typed_strategy)
@settings(max_examples=50)
def test_typed_instantiation(instance):
    assert isinstance(instance, Typed)

@given(instance=iot2_Field_strategy)
@settings(max_examples=50)
def test_iot2_field_instantiation(instance):
    assert isinstance(instance, iot2_Field)



@given(instance=iot2_Field_strategy)
def test_iot2_field_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=iot2_ParameterDef_strategy)
@settings(max_examples=50)
def test_iot2_parameterdef_instantiation(instance):
    assert isinstance(instance, iot2_ParameterDef)



@given(instance=iot2_ParameterDef_strategy)
def test_iot2_parameterdef_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original



@given(instance=iot2_ParameterDef_strategy)
def test_iot2_parameterdef_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=Contained_strategy)
@settings(max_examples=50)
def test_contained_instantiation(instance):
    assert isinstance(instance, Contained)

@given(instance=iot2_Variable_strategy)
@settings(max_examples=50)
def test_iot2_variable_instantiation(instance):
    assert isinstance(instance, iot2_Variable)



@given(instance=iot2_Variable_strategy)
def test_iot2_variable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=iot2_ActivityNode_strategy)
@settings(max_examples=50)
def test_iot2_activitynode_instantiation(instance):
    assert isinstance(instance, iot2_ActivityNode)



@given(instance=iot2_ActivityNode_strategy)
def test_iot2_activitynode_running_setter(instance):
    original = instance.running
    instance.running = original
    assert instance.running == original

@given(instance=iot2_ActivityEdge_strategy)
@settings(max_examples=50)
def test_iot2_activityedge_instantiation(instance):
    assert isinstance(instance, iot2_ActivityEdge)

@given(instance=iot2_TypedefDef_strategy)
@settings(max_examples=50)
def test_iot2_typedefdef_instantiation(instance):
    assert isinstance(instance, iot2_TypedefDef)

@given(instance=iot2_IDLType_strategy)
@settings(max_examples=50)
def test_iot2_idltype_instantiation(instance):
    assert isinstance(instance, iot2_IDLType)



@given(instance=iot2_IDLType_strategy)
def test_iot2_idltype_typeCode_setter(instance):
    original = instance.typeCode
    instance.typeCode = original
    assert instance.typeCode == original

@given(instance=iot2_Typed_strategy)
@settings(max_examples=50)
def test_iot2_typed_instantiation(instance):
    assert isinstance(instance, iot2_Typed)

@given(instance=iot2_NamedElement_strategy)
@settings(max_examples=50)
def test_iot2_namedelement_instantiation(instance):
    assert isinstance(instance, iot2_NamedElement)



@given(instance=iot2_NamedElement_strategy)
def test_iot2_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=iot2_NamedElement_strategy)
def test_iot2_namedelement_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=iot2_Container_strategy)
@settings(max_examples=50)
def test_iot2_container_instantiation(instance):
    assert isinstance(instance, iot2_Container)

@given(instance=iot2_Contained_strategy)
@settings(max_examples=50)
def test_iot2_contained_instantiation(instance):
    assert isinstance(instance, iot2_Contained)



@given(instance=iot2_Contained_strategy)
def test_iot2_contained_repositoryId_setter(instance):
    original = instance.repositoryId
    instance.repositoryId = original
    assert instance.repositoryId == original



@given(instance=iot2_Contained_strategy)
def test_iot2_contained_absoluteName_setter(instance):
    original = instance.absoluteName
    instance.absoluteName = original
    assert instance.absoluteName == original



@given(instance=iot2_Contained_strategy)
def test_iot2_contained_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=iot2_Block_strategy)
@settings(max_examples=50)
def test_iot2_block_instantiation(instance):
    assert isinstance(instance, iot2_Block)

@given(instance=iot2_ExceptionDef_strategy)
@settings(max_examples=50)
def test_iot2_exceptiondef_instantiation(instance):
    assert isinstance(instance, iot2_ExceptionDef)



@given(instance=iot2_ExceptionDef_strategy)
def test_iot2_exceptiondef_typeCode_setter(instance):
    original = instance.typeCode
    instance.typeCode = original
    assert instance.typeCode == original

@given(instance=HWComponent_strategy)
@settings(max_examples=50)
def test_hwcomponent_instantiation(instance):
    assert isinstance(instance, HWComponent)

@given(instance=iot2_Actuator_strategy)
@settings(max_examples=50)
def test_iot2_actuator_instantiation(instance):
    assert isinstance(instance, iot2_Actuator)

@given(instance=iot2_Sensor_strategy)
@settings(max_examples=50)
def test_iot2_sensor_instantiation(instance):
    assert isinstance(instance, iot2_Sensor)

@given(instance=iot2_OperationDef_strategy)
@settings(max_examples=50)
def test_iot2_operationdef_instantiation(instance):
    assert isinstance(instance, iot2_OperationDef)



@given(instance=iot2_OperationDef_strategy)
def test_iot2_operationdef_isOneway_setter(instance):
    original = instance.isOneway
    instance.isOneway = original
    assert instance.isOneway == original



@given(instance=iot2_OperationDef_strategy)
def test_iot2_operationdef_contexts_setter(instance):
    original = instance.contexts
    instance.contexts = original
    assert instance.contexts == original

@given(instance=iot2_Activity_strategy)
@settings(max_examples=50)
def test_iot2_activity_instantiation(instance):
    assert isinstance(instance, iot2_Activity)

@given(instance=iot2_Sketch_strategy)
@settings(max_examples=50)
def test_iot2_sketch_instantiation(instance):
    assert isinstance(instance, iot2_Sketch)

@given(instance=iot2_Board_strategy)
@settings(max_examples=50)
def test_iot2_board_instantiation(instance):
    assert isinstance(instance, iot2_Board)



@given(instance=iot2_Board_strategy)
def test_iot2_board_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=iot2_Board_strategy)
def test_iot2_board_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=iot2_HWComponent_strategy)
@settings(max_examples=50)
def test_iot2_hwcomponent_instantiation(instance):
    assert isinstance(instance, iot2_HWComponent)



@given(instance=iot2_HWComponent_strategy)
def test_iot2_hwcomponent_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=iot2_System_strategy)
@settings(max_examples=50)
def test_iot2_system_instantiation(instance):
    assert isinstance(instance, iot2_System)



@given(instance=iot2_System_strategy)
def test_iot2_system_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=iot2_Trace_strategy)
@settings(max_examples=50)
def test_iot2_trace_instantiation(instance):
    assert isinstance(instance, iot2_Trace)

@given(instance=IntegerExpression_strategy)
@settings(max_examples=50)
def test_integerexpression_instantiation(instance):
    assert isinstance(instance, IntegerExpression)

@given(instance=iot2_IntegerComparisonExpression_strategy)
@settings(max_examples=50)
def test_iot2_integercomparisonexpression_instantiation(instance):
    assert isinstance(instance, iot2_IntegerComparisonExpression)



@given(instance=iot2_IntegerComparisonExpression_strategy)
def test_iot2_integercomparisonexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=iot2_IntegerCalculationExpression_strategy)
@settings(max_examples=50)
def test_iot2_integercalculationexpression_instantiation(instance):
    assert isinstance(instance, iot2_IntegerCalculationExpression)



@given(instance=iot2_IntegerCalculationExpression_strategy)
def test_iot2_integercalculationexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=iot2_BooleanExpression_strategy)
@settings(max_examples=50)
def test_iot2_booleanexpression_instantiation(instance):
    assert isinstance(instance, iot2_BooleanExpression)

@given(instance=iot2_Token_strategy)
@settings(max_examples=50)
def test_iot2_token_instantiation(instance):
    assert isinstance(instance, iot2_Token)

@given(instance=iot2_Input_strategy)
@settings(max_examples=50)
def test_iot2_input_instantiation(instance):
    assert isinstance(instance, iot2_Input)

@given(instance=iot2_InputValue_strategy)
@settings(max_examples=50)
def test_iot2_inputvalue_instantiation(instance):
    assert isinstance(instance, iot2_InputValue)

@given(instance=BooleanExpression_strategy)
@settings(max_examples=50)
def test_booleanexpression_instantiation(instance):
    assert isinstance(instance, BooleanExpression)

@given(instance=iot2_BooleanBinaryExpression_strategy)
@settings(max_examples=50)
def test_iot2_booleanbinaryexpression_instantiation(instance):
    assert isinstance(instance, iot2_BooleanBinaryExpression)



@given(instance=iot2_BooleanBinaryExpression_strategy)
def test_iot2_booleanbinaryexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=iot2_BooleanUnaryExpression_strategy)
@settings(max_examples=50)
def test_iot2_booleanunaryexpression_instantiation(instance):
    assert isinstance(instance, iot2_BooleanUnaryExpression)



@given(instance=iot2_BooleanUnaryExpression_strategy)
def test_iot2_booleanunaryexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=Action_strategy)
@settings(max_examples=50)
def test_action_instantiation(instance):
    assert isinstance(instance, Action)

@given(instance=iot2_OpaqueAction_strategy)
@settings(max_examples=50)
def test_iot2_opaqueaction_instantiation(instance):
    assert isinstance(instance, iot2_OpaqueAction)

@given(instance=ExecutableNode_strategy)
@settings(max_examples=50)
def test_executablenode_instantiation(instance):
    assert isinstance(instance, ExecutableNode)

@given(instance=iot2_Action_strategy)
@settings(max_examples=50)
def test_iot2_action_instantiation(instance):
    assert isinstance(instance, iot2_Action)

@given(instance=ActivityNode_strategy)
@settings(max_examples=50)
def test_activitynode_instantiation(instance):
    assert isinstance(instance, ActivityNode)

@given(instance=iot2_ExecutableNode_strategy)
@settings(max_examples=50)
def test_iot2_executablenode_instantiation(instance):
    assert isinstance(instance, iot2_ExecutableNode)

@given(instance=iot2_ControlNode_strategy)
@settings(max_examples=50)
def test_iot2_controlnode_instantiation(instance):
    assert isinstance(instance, iot2_ControlNode)

@given(instance=ActivityEdge_strategy)
@settings(max_examples=50)
def test_activityedge_instantiation(instance):
    assert isinstance(instance, ActivityEdge)

@given(instance=iot2_ControlFlow_strategy)
@settings(max_examples=50)
def test_iot2_controlflow_instantiation(instance):
    assert isinstance(instance, iot2_ControlFlow)

@given(instance=iot2_IntegerExpression_strategy)
@settings(max_examples=50)
def test_iot2_integerexpression_instantiation(instance):
    assert isinstance(instance, iot2_IntegerExpression)

@given(instance=Value_strategy)
@settings(max_examples=50)
def test_value_instantiation(instance):
    assert isinstance(instance, Value)

@given(instance=iot2_IntegerValue_strategy)
@settings(max_examples=50)
def test_iot2_integervalue_instantiation(instance):
    assert isinstance(instance, iot2_IntegerValue)



@given(instance=iot2_IntegerValue_strategy)
def test_iot2_integervalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=iot2_BooleanValue_strategy)
@settings(max_examples=50)
def test_iot2_booleanvalue_instantiation(instance):
    assert isinstance(instance, iot2_BooleanValue)



@given(instance=iot2_BooleanValue_strategy)
def test_iot2_booleanvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Variable_strategy)
@settings(max_examples=50)
def test_variable_instantiation(instance):
    assert isinstance(instance, Variable)

@given(instance=iot2_BooleanVariable_strategy)
@settings(max_examples=50)
def test_iot2_booleanvariable_instantiation(instance):
    assert isinstance(instance, iot2_BooleanVariable)

@given(instance=iot2_IntegerVariable_strategy)
@settings(max_examples=50)
def test_iot2_integervariable_instantiation(instance):
    assert isinstance(instance, iot2_IntegerVariable)
