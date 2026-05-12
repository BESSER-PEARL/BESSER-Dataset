import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    StringExpression,
    urml_ConcatenateExpression,
    urml_StringExpression,
    urml_Identifiable,
    Literal,
    urml_FunctionCall,
    urml_BoolLiteral,
    urml_IntLiteral,
    Expression,
    urml_UnaryExpression,
    urml_Identifier,
    urml_Plus,
    urml_LessThanOrEqual,
    urml_ConditionalAndExpression,
    urml_Equal,
    urml_GreaterThanOrEqual,
    urml_GreaterThan,
    urml_LessThan,
    urml_NotEqual,
    urml_Literal,
    urml_ConditionalOrExpression,
    urml_Modulo,
    urml_Multiply,
    urml_Minus,
    urml_Divide,
    urml_NotBooleanExpression,
    Statement,
    urml_IfStatement,
    urml_Statement,
    urml_WhileLoop,
    urml_ActionCode,
    urml_Transition,
    urml_State_,
    StatementOperation,
    urml_NoOp,
    urml_IfStatementOperation,
    urml_SendTrigger,
    urml_ReturnStatement,
    urml_Variable,
    urml_Assignment,
    urml_LogStatement,
    urml_Invoke,
    urml_InformTimer,
    urml_WhileLoopOperation,
    urml_StatementOperation,
    urml_Trigger_out,
    Identifiable,
    urml_Assignable,
    urml_IncomingVariable,
    urml_Trigger_in,
    urml_Connector,
    urml_CapsuleInst,
    urml_LogPort,
    urml_TimerPort,
    urml_Port,
    urml_OperationCode,
    urml_StateMachine,
    urml_Operation,
    urml_Signal,
    urml_Expression,
    Assignable,
    urml_Attribute,
    urml_LocalVar,
    urml_Protocol,
    urml_Capsule,
    urml_Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_stringexpression_is_not_abstract():
    assert not inspect.isabstract(StringExpression)


def test_stringexpression_constructor_exists():
    assert callable(StringExpression.__init__)


def test_stringexpression_constructor_args():
    sig = inspect.signature(StringExpression.__init__)
    params = list(sig.parameters.keys())



def test_urml_concatenateexpression_is_not_abstract():
    assert not inspect.isabstract(urml_ConcatenateExpression)


def test_urml_concatenateexpression_constructor_exists():
    assert callable(urml_ConcatenateExpression.__init__)


def test_urml_concatenateexpression_constructor_args():
    sig = inspect.signature(urml_ConcatenateExpression.__init__)
    params = list(sig.parameters.keys())



def test_urml_stringexpression_is_not_abstract():
    assert not inspect.isabstract(urml_StringExpression)


def test_urml_stringexpression_constructor_exists():
    assert callable(urml_StringExpression.__init__)


def test_urml_stringexpression_constructor_args():
    sig = inspect.signature(urml_StringExpression.__init__)
    params = list(sig.parameters.keys())
    assert "str" in params, "Missing parameter 'str'"

def test_urml_stringexpression_has_str():
    assert hasattr(urml_StringExpression, "str")
    descriptor = None
    for klass in urml_StringExpression.__mro__:
        if "str" in klass.__dict__:
            descriptor = klass.__dict__["str"]
            break
    assert isinstance(descriptor, property)



def test_urml_identifiable_is_not_abstract():
    assert not inspect.isabstract(urml_Identifiable)


def test_urml_identifiable_constructor_exists():
    assert callable(urml_Identifiable.__init__)


def test_urml_identifiable_constructor_args():
    sig = inspect.signature(urml_Identifiable.__init__)
    params = list(sig.parameters.keys())
    assert "isInt" in params, "Missing parameter 'isInt'"
    assert "name" in params, "Missing parameter 'name'"
    assert "isBool" in params, "Missing parameter 'isBool'"

def test_urml_identifiable_has_isInt():
    assert hasattr(urml_Identifiable, "isInt")
    descriptor = None
    for klass in urml_Identifiable.__mro__:
        if "isInt" in klass.__dict__:
            descriptor = klass.__dict__["isInt"]
            break
    assert isinstance(descriptor, property)

def test_urml_identifiable_has_name():
    assert hasattr(urml_Identifiable, "name")
    descriptor = None
    for klass in urml_Identifiable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_urml_identifiable_has_isBool():
    assert hasattr(urml_Identifiable, "isBool")
    descriptor = None
    for klass in urml_Identifiable.__mro__:
        if "isBool" in klass.__dict__:
            descriptor = klass.__dict__["isBool"]
            break
    assert isinstance(descriptor, property)



def test_literal_is_not_abstract():
    assert not inspect.isabstract(Literal)


def test_literal_constructor_exists():
    assert callable(Literal.__init__)


def test_literal_constructor_args():
    sig = inspect.signature(Literal.__init__)
    params = list(sig.parameters.keys())



def test_urml_functioncall_is_not_abstract():
    assert not inspect.isabstract(urml_FunctionCall)


def test_urml_functioncall_constructor_exists():
    assert callable(urml_FunctionCall.__init__)


def test_urml_functioncall_constructor_args():
    sig = inspect.signature(urml_FunctionCall.__init__)
    params = list(sig.parameters.keys())



def test_urml_boolliteral_is_not_abstract():
    assert not inspect.isabstract(urml_BoolLiteral)


def test_urml_boolliteral_constructor_exists():
    assert callable(urml_BoolLiteral.__init__)


def test_urml_boolliteral_constructor_args():
    sig = inspect.signature(urml_BoolLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "true" in params, "Missing parameter 'true'"

def test_urml_boolliteral_has_true():
    assert hasattr(urml_BoolLiteral, "true")
    descriptor = None
    for klass in urml_BoolLiteral.__mro__:
        if "true" in klass.__dict__:
            descriptor = klass.__dict__["true"]
            break
    assert isinstance(descriptor, property)



def test_urml_intliteral_is_not_abstract():
    assert not inspect.isabstract(urml_IntLiteral)


def test_urml_intliteral_constructor_exists():
    assert callable(urml_IntLiteral.__init__)


def test_urml_intliteral_constructor_args():
    sig = inspect.signature(urml_IntLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "int" in params, "Missing parameter 'int'"

def test_urml_intliteral_has_int():
    assert hasattr(urml_IntLiteral, "int")
    descriptor = None
    for klass in urml_IntLiteral.__mro__:
        if "int" in klass.__dict__:
            descriptor = klass.__dict__["int"]
            break
    assert isinstance(descriptor, property)



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_urml_unaryexpression_is_not_abstract():
    assert not inspect.isabstract(urml_UnaryExpression)


def test_urml_unaryexpression_constructor_exists():
    assert callable(urml_UnaryExpression.__init__)


def test_urml_unaryexpression_constructor_args():
    sig = inspect.signature(urml_UnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_urml_identifier_is_not_abstract():
    assert not inspect.isabstract(urml_Identifier)


def test_urml_identifier_constructor_exists():
    assert callable(urml_Identifier.__init__)


def test_urml_identifier_constructor_args():
    sig = inspect.signature(urml_Identifier.__init__)
    params = list(sig.parameters.keys())



def test_urml_plus_is_not_abstract():
    assert not inspect.isabstract(urml_Plus)


def test_urml_plus_constructor_exists():
    assert callable(urml_Plus.__init__)


def test_urml_plus_constructor_args():
    sig = inspect.signature(urml_Plus.__init__)
    params = list(sig.parameters.keys())



def test_urml_lessthanorequal_is_not_abstract():
    assert not inspect.isabstract(urml_LessThanOrEqual)


def test_urml_lessthanorequal_constructor_exists():
    assert callable(urml_LessThanOrEqual.__init__)


def test_urml_lessthanorequal_constructor_args():
    sig = inspect.signature(urml_LessThanOrEqual.__init__)
    params = list(sig.parameters.keys())



def test_urml_conditionalandexpression_is_not_abstract():
    assert not inspect.isabstract(urml_ConditionalAndExpression)


def test_urml_conditionalandexpression_constructor_exists():
    assert callable(urml_ConditionalAndExpression.__init__)


def test_urml_conditionalandexpression_constructor_args():
    sig = inspect.signature(urml_ConditionalAndExpression.__init__)
    params = list(sig.parameters.keys())



def test_urml_equal_is_not_abstract():
    assert not inspect.isabstract(urml_Equal)


def test_urml_equal_constructor_exists():
    assert callable(urml_Equal.__init__)


def test_urml_equal_constructor_args():
    sig = inspect.signature(urml_Equal.__init__)
    params = list(sig.parameters.keys())



def test_urml_greaterthanorequal_is_not_abstract():
    assert not inspect.isabstract(urml_GreaterThanOrEqual)


def test_urml_greaterthanorequal_constructor_exists():
    assert callable(urml_GreaterThanOrEqual.__init__)


def test_urml_greaterthanorequal_constructor_args():
    sig = inspect.signature(urml_GreaterThanOrEqual.__init__)
    params = list(sig.parameters.keys())



def test_urml_greaterthan_is_not_abstract():
    assert not inspect.isabstract(urml_GreaterThan)


def test_urml_greaterthan_constructor_exists():
    assert callable(urml_GreaterThan.__init__)


def test_urml_greaterthan_constructor_args():
    sig = inspect.signature(urml_GreaterThan.__init__)
    params = list(sig.parameters.keys())



def test_urml_lessthan_is_not_abstract():
    assert not inspect.isabstract(urml_LessThan)


def test_urml_lessthan_constructor_exists():
    assert callable(urml_LessThan.__init__)


def test_urml_lessthan_constructor_args():
    sig = inspect.signature(urml_LessThan.__init__)
    params = list(sig.parameters.keys())



def test_urml_notequal_is_not_abstract():
    assert not inspect.isabstract(urml_NotEqual)


def test_urml_notequal_constructor_exists():
    assert callable(urml_NotEqual.__init__)


def test_urml_notequal_constructor_args():
    sig = inspect.signature(urml_NotEqual.__init__)
    params = list(sig.parameters.keys())



def test_urml_literal_is_not_abstract():
    assert not inspect.isabstract(urml_Literal)


def test_urml_literal_constructor_exists():
    assert callable(urml_Literal.__init__)


def test_urml_literal_constructor_args():
    sig = inspect.signature(urml_Literal.__init__)
    params = list(sig.parameters.keys())



def test_urml_conditionalorexpression_is_not_abstract():
    assert not inspect.isabstract(urml_ConditionalOrExpression)


def test_urml_conditionalorexpression_constructor_exists():
    assert callable(urml_ConditionalOrExpression.__init__)


def test_urml_conditionalorexpression_constructor_args():
    sig = inspect.signature(urml_ConditionalOrExpression.__init__)
    params = list(sig.parameters.keys())



def test_urml_modulo_is_not_abstract():
    assert not inspect.isabstract(urml_Modulo)


def test_urml_modulo_constructor_exists():
    assert callable(urml_Modulo.__init__)


def test_urml_modulo_constructor_args():
    sig = inspect.signature(urml_Modulo.__init__)
    params = list(sig.parameters.keys())



def test_urml_multiply_is_not_abstract():
    assert not inspect.isabstract(urml_Multiply)


def test_urml_multiply_constructor_exists():
    assert callable(urml_Multiply.__init__)


def test_urml_multiply_constructor_args():
    sig = inspect.signature(urml_Multiply.__init__)
    params = list(sig.parameters.keys())



def test_urml_minus_is_not_abstract():
    assert not inspect.isabstract(urml_Minus)


def test_urml_minus_constructor_exists():
    assert callable(urml_Minus.__init__)


def test_urml_minus_constructor_args():
    sig = inspect.signature(urml_Minus.__init__)
    params = list(sig.parameters.keys())



def test_urml_divide_is_not_abstract():
    assert not inspect.isabstract(urml_Divide)


def test_urml_divide_constructor_exists():
    assert callable(urml_Divide.__init__)


def test_urml_divide_constructor_args():
    sig = inspect.signature(urml_Divide.__init__)
    params = list(sig.parameters.keys())



def test_urml_notbooleanexpression_is_not_abstract():
    assert not inspect.isabstract(urml_NotBooleanExpression)


def test_urml_notbooleanexpression_constructor_exists():
    assert callable(urml_NotBooleanExpression.__init__)


def test_urml_notbooleanexpression_constructor_args():
    sig = inspect.signature(urml_NotBooleanExpression.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_urml_ifstatement_is_not_abstract():
    assert not inspect.isabstract(urml_IfStatement)


def test_urml_ifstatement_constructor_exists():
    assert callable(urml_IfStatement.__init__)


def test_urml_ifstatement_constructor_args():
    sig = inspect.signature(urml_IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_urml_statement_is_not_abstract():
    assert not inspect.isabstract(urml_Statement)


def test_urml_statement_constructor_exists():
    assert callable(urml_Statement.__init__)


def test_urml_statement_constructor_args():
    sig = inspect.signature(urml_Statement.__init__)
    params = list(sig.parameters.keys())



def test_urml_whileloop_is_not_abstract():
    assert not inspect.isabstract(urml_WhileLoop)


def test_urml_whileloop_constructor_exists():
    assert callable(urml_WhileLoop.__init__)


def test_urml_whileloop_constructor_args():
    sig = inspect.signature(urml_WhileLoop.__init__)
    params = list(sig.parameters.keys())



def test_urml_actioncode_is_not_abstract():
    assert not inspect.isabstract(urml_ActionCode)


def test_urml_actioncode_constructor_exists():
    assert callable(urml_ActionCode.__init__)


def test_urml_actioncode_constructor_args():
    sig = inspect.signature(urml_ActionCode.__init__)
    params = list(sig.parameters.keys())



def test_urml_transition_is_not_abstract():
    assert not inspect.isabstract(urml_Transition)


def test_urml_transition_constructor_exists():
    assert callable(urml_Transition.__init__)


def test_urml_transition_constructor_args():
    sig = inspect.signature(urml_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "init" in params, "Missing parameter 'init'"
    assert "universal" in params, "Missing parameter 'universal'"

def test_urml_transition_has_name():
    assert hasattr(urml_Transition, "name")
    descriptor = None
    for klass in urml_Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_urml_transition_has_init():
    assert hasattr(urml_Transition, "init")
    descriptor = None
    for klass in urml_Transition.__mro__:
        if "init" in klass.__dict__:
            descriptor = klass.__dict__["init"]
            break
    assert isinstance(descriptor, property)

def test_urml_transition_has_universal():
    assert hasattr(urml_Transition, "universal")
    descriptor = None
    for klass in urml_Transition.__mro__:
        if "universal" in klass.__dict__:
            descriptor = klass.__dict__["universal"]
            break
    assert isinstance(descriptor, property)



def test_urml_state__is_not_abstract():
    assert not inspect.isabstract(urml_State_)


def test_urml_state__constructor_exists():
    assert callable(urml_State_.__init__)


def test_urml_state__constructor_args():
    sig = inspect.signature(urml_State_.__init__)
    params = list(sig.parameters.keys())
    assert "final" in params, "Missing parameter 'final'"
    assert "name" in params, "Missing parameter 'name'"

def test_urml_state__has_final():
    assert hasattr(urml_State_, "final")
    descriptor = None
    for klass in urml_State_.__mro__:
        if "final" in klass.__dict__:
            descriptor = klass.__dict__["final"]
            break
    assert isinstance(descriptor, property)

def test_urml_state__has_name():
    assert hasattr(urml_State_, "name")
    descriptor = None
    for klass in urml_State_.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statementoperation_is_not_abstract():
    assert not inspect.isabstract(StatementOperation)


def test_statementoperation_constructor_exists():
    assert callable(StatementOperation.__init__)


def test_statementoperation_constructor_args():
    sig = inspect.signature(StatementOperation.__init__)
    params = list(sig.parameters.keys())



def test_urml_noop_is_not_abstract():
    assert not inspect.isabstract(urml_NoOp)


def test_urml_noop_constructor_exists():
    assert callable(urml_NoOp.__init__)


def test_urml_noop_constructor_args():
    sig = inspect.signature(urml_NoOp.__init__)
    params = list(sig.parameters.keys())



def test_urml_ifstatementoperation_is_not_abstract():
    assert not inspect.isabstract(urml_IfStatementOperation)


def test_urml_ifstatementoperation_constructor_exists():
    assert callable(urml_IfStatementOperation.__init__)


def test_urml_ifstatementoperation_constructor_args():
    sig = inspect.signature(urml_IfStatementOperation.__init__)
    params = list(sig.parameters.keys())



def test_urml_sendtrigger_is_not_abstract():
    assert not inspect.isabstract(urml_SendTrigger)


def test_urml_sendtrigger_constructor_exists():
    assert callable(urml_SendTrigger.__init__)


def test_urml_sendtrigger_constructor_args():
    sig = inspect.signature(urml_SendTrigger.__init__)
    params = list(sig.parameters.keys())



def test_urml_returnstatement_is_not_abstract():
    assert not inspect.isabstract(urml_ReturnStatement)


def test_urml_returnstatement_constructor_exists():
    assert callable(urml_ReturnStatement.__init__)


def test_urml_returnstatement_constructor_args():
    sig = inspect.signature(urml_ReturnStatement.__init__)
    params = list(sig.parameters.keys())



def test_urml_variable_is_not_abstract():
    assert not inspect.isabstract(urml_Variable)


def test_urml_variable_constructor_exists():
    assert callable(urml_Variable.__init__)


def test_urml_variable_constructor_args():
    sig = inspect.signature(urml_Variable.__init__)
    params = list(sig.parameters.keys())
    assert "assign" in params, "Missing parameter 'assign'"

def test_urml_variable_has_assign():
    assert hasattr(urml_Variable, "assign")
    descriptor = None
    for klass in urml_Variable.__mro__:
        if "assign" in klass.__dict__:
            descriptor = klass.__dict__["assign"]
            break
    assert isinstance(descriptor, property)



def test_urml_assignment_is_not_abstract():
    assert not inspect.isabstract(urml_Assignment)


def test_urml_assignment_constructor_exists():
    assert callable(urml_Assignment.__init__)


def test_urml_assignment_constructor_args():
    sig = inspect.signature(urml_Assignment.__init__)
    params = list(sig.parameters.keys())



def test_urml_logstatement_is_not_abstract():
    assert not inspect.isabstract(urml_LogStatement)


def test_urml_logstatement_constructor_exists():
    assert callable(urml_LogStatement.__init__)


def test_urml_logstatement_constructor_args():
    sig = inspect.signature(urml_LogStatement.__init__)
    params = list(sig.parameters.keys())



def test_urml_invoke_is_not_abstract():
    assert not inspect.isabstract(urml_Invoke)


def test_urml_invoke_constructor_exists():
    assert callable(urml_Invoke.__init__)


def test_urml_invoke_constructor_args():
    sig = inspect.signature(urml_Invoke.__init__)
    params = list(sig.parameters.keys())



def test_urml_informtimer_is_not_abstract():
    assert not inspect.isabstract(urml_InformTimer)


def test_urml_informtimer_constructor_exists():
    assert callable(urml_InformTimer.__init__)


def test_urml_informtimer_constructor_args():
    sig = inspect.signature(urml_InformTimer.__init__)
    params = list(sig.parameters.keys())



def test_urml_whileloopoperation_is_not_abstract():
    assert not inspect.isabstract(urml_WhileLoopOperation)


def test_urml_whileloopoperation_constructor_exists():
    assert callable(urml_WhileLoopOperation.__init__)


def test_urml_whileloopoperation_constructor_args():
    sig = inspect.signature(urml_WhileLoopOperation.__init__)
    params = list(sig.parameters.keys())



def test_urml_statementoperation_is_not_abstract():
    assert not inspect.isabstract(urml_StatementOperation)


def test_urml_statementoperation_constructor_exists():
    assert callable(urml_StatementOperation.__init__)


def test_urml_statementoperation_constructor_args():
    sig = inspect.signature(urml_StatementOperation.__init__)
    params = list(sig.parameters.keys())



def test_urml_trigger_out_is_not_abstract():
    assert not inspect.isabstract(urml_Trigger_out)


def test_urml_trigger_out_constructor_exists():
    assert callable(urml_Trigger_out.__init__)


def test_urml_trigger_out_constructor_args():
    sig = inspect.signature(urml_Trigger_out.__init__)
    params = list(sig.parameters.keys())



def test_identifiable_is_not_abstract():
    assert not inspect.isabstract(Identifiable)


def test_identifiable_constructor_exists():
    assert callable(Identifiable.__init__)


def test_identifiable_constructor_args():
    sig = inspect.signature(Identifiable.__init__)
    params = list(sig.parameters.keys())



def test_urml_assignable_is_not_abstract():
    assert not inspect.isabstract(urml_Assignable)


def test_urml_assignable_constructor_exists():
    assert callable(urml_Assignable.__init__)


def test_urml_assignable_constructor_args():
    sig = inspect.signature(urml_Assignable.__init__)
    params = list(sig.parameters.keys())



def test_urml_incomingvariable_is_not_abstract():
    assert not inspect.isabstract(urml_IncomingVariable)


def test_urml_incomingvariable_constructor_exists():
    assert callable(urml_IncomingVariable.__init__)


def test_urml_incomingvariable_constructor_args():
    sig = inspect.signature(urml_IncomingVariable.__init__)
    params = list(sig.parameters.keys())



def test_urml_trigger_in_is_not_abstract():
    assert not inspect.isabstract(urml_Trigger_in)


def test_urml_trigger_in_constructor_exists():
    assert callable(urml_Trigger_in.__init__)


def test_urml_trigger_in_constructor_args():
    sig = inspect.signature(urml_Trigger_in.__init__)
    params = list(sig.parameters.keys())



def test_urml_connector_is_not_abstract():
    assert not inspect.isabstract(urml_Connector)


def test_urml_connector_constructor_exists():
    assert callable(urml_Connector.__init__)


def test_urml_connector_constructor_args():
    sig = inspect.signature(urml_Connector.__init__)
    params = list(sig.parameters.keys())



def test_urml_capsuleinst_is_not_abstract():
    assert not inspect.isabstract(urml_CapsuleInst)


def test_urml_capsuleinst_constructor_exists():
    assert callable(urml_CapsuleInst.__init__)


def test_urml_capsuleinst_constructor_args():
    sig = inspect.signature(urml_CapsuleInst.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_urml_capsuleinst_has_name():
    assert hasattr(urml_CapsuleInst, "name")
    descriptor = None
    for klass in urml_CapsuleInst.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_urml_logport_is_not_abstract():
    assert not inspect.isabstract(urml_LogPort)


def test_urml_logport_constructor_exists():
    assert callable(urml_LogPort.__init__)


def test_urml_logport_constructor_args():
    sig = inspect.signature(urml_LogPort.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_urml_logport_has_name():
    assert hasattr(urml_LogPort, "name")
    descriptor = None
    for klass in urml_LogPort.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_urml_timerport_is_not_abstract():
    assert not inspect.isabstract(urml_TimerPort)


def test_urml_timerport_constructor_exists():
    assert callable(urml_TimerPort.__init__)


def test_urml_timerport_constructor_args():
    sig = inspect.signature(urml_TimerPort.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_urml_timerport_has_name():
    assert hasattr(urml_TimerPort, "name")
    descriptor = None
    for klass in urml_TimerPort.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_urml_port_is_not_abstract():
    assert not inspect.isabstract(urml_Port)


def test_urml_port_constructor_exists():
    assert callable(urml_Port.__init__)


def test_urml_port_constructor_args():
    sig = inspect.signature(urml_Port.__init__)
    params = list(sig.parameters.keys())
    assert "conjugated" in params, "Missing parameter 'conjugated'"
    assert "name" in params, "Missing parameter 'name'"

def test_urml_port_has_conjugated():
    assert hasattr(urml_Port, "conjugated")
    descriptor = None
    for klass in urml_Port.__mro__:
        if "conjugated" in klass.__dict__:
            descriptor = klass.__dict__["conjugated"]
            break
    assert isinstance(descriptor, property)

def test_urml_port_has_name():
    assert hasattr(urml_Port, "name")
    descriptor = None
    for klass in urml_Port.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_urml_operationcode_is_not_abstract():
    assert not inspect.isabstract(urml_OperationCode)


def test_urml_operationcode_constructor_exists():
    assert callable(urml_OperationCode.__init__)


def test_urml_operationcode_constructor_args():
    sig = inspect.signature(urml_OperationCode.__init__)
    params = list(sig.parameters.keys())



def test_urml_statemachine_is_not_abstract():
    assert not inspect.isabstract(urml_StateMachine)


def test_urml_statemachine_constructor_exists():
    assert callable(urml_StateMachine.__init__)


def test_urml_statemachine_constructor_args():
    sig = inspect.signature(urml_StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_urml_operation_is_not_abstract():
    assert not inspect.isabstract(urml_Operation)


def test_urml_operation_constructor_exists():
    assert callable(urml_Operation.__init__)


def test_urml_operation_constructor_args():
    sig = inspect.signature(urml_Operation.__init__)
    params = list(sig.parameters.keys())
    assert "isInt" in params, "Missing parameter 'isInt'"
    assert "isVoid" in params, "Missing parameter 'isVoid'"
    assert "isBool" in params, "Missing parameter 'isBool'"
    assert "name" in params, "Missing parameter 'name'"

def test_urml_operation_has_isInt():
    assert hasattr(urml_Operation, "isInt")
    descriptor = None
    for klass in urml_Operation.__mro__:
        if "isInt" in klass.__dict__:
            descriptor = klass.__dict__["isInt"]
            break
    assert isinstance(descriptor, property)

def test_urml_operation_has_isVoid():
    assert hasattr(urml_Operation, "isVoid")
    descriptor = None
    for klass in urml_Operation.__mro__:
        if "isVoid" in klass.__dict__:
            descriptor = klass.__dict__["isVoid"]
            break
    assert isinstance(descriptor, property)

def test_urml_operation_has_isBool():
    assert hasattr(urml_Operation, "isBool")
    descriptor = None
    for klass in urml_Operation.__mro__:
        if "isBool" in klass.__dict__:
            descriptor = klass.__dict__["isBool"]
            break
    assert isinstance(descriptor, property)

def test_urml_operation_has_name():
    assert hasattr(urml_Operation, "name")
    descriptor = None
    for klass in urml_Operation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_urml_signal_is_not_abstract():
    assert not inspect.isabstract(urml_Signal)


def test_urml_signal_constructor_exists():
    assert callable(urml_Signal.__init__)


def test_urml_signal_constructor_args():
    sig = inspect.signature(urml_Signal.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_urml_signal_has_name():
    assert hasattr(urml_Signal, "name")
    descriptor = None
    for klass in urml_Signal.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_urml_expression_is_not_abstract():
    assert not inspect.isabstract(urml_Expression)


def test_urml_expression_constructor_exists():
    assert callable(urml_Expression.__init__)


def test_urml_expression_constructor_args():
    sig = inspect.signature(urml_Expression.__init__)
    params = list(sig.parameters.keys())



def test_assignable_is_not_abstract():
    assert not inspect.isabstract(Assignable)


def test_assignable_constructor_exists():
    assert callable(Assignable.__init__)


def test_assignable_constructor_args():
    sig = inspect.signature(Assignable.__init__)
    params = list(sig.parameters.keys())



def test_urml_attribute_is_not_abstract():
    assert not inspect.isabstract(urml_Attribute)


def test_urml_attribute_constructor_exists():
    assert callable(urml_Attribute.__init__)


def test_urml_attribute_constructor_args():
    sig = inspect.signature(urml_Attribute.__init__)
    params = list(sig.parameters.keys())



def test_urml_localvar_is_not_abstract():
    assert not inspect.isabstract(urml_LocalVar)


def test_urml_localvar_constructor_exists():
    assert callable(urml_LocalVar.__init__)


def test_urml_localvar_constructor_args():
    sig = inspect.signature(urml_LocalVar.__init__)
    params = list(sig.parameters.keys())



def test_urml_protocol_is_not_abstract():
    assert not inspect.isabstract(urml_Protocol)


def test_urml_protocol_constructor_exists():
    assert callable(urml_Protocol.__init__)


def test_urml_protocol_constructor_args():
    sig = inspect.signature(urml_Protocol.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_urml_protocol_has_name():
    assert hasattr(urml_Protocol, "name")
    descriptor = None
    for klass in urml_Protocol.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_urml_capsule_is_not_abstract():
    assert not inspect.isabstract(urml_Capsule)


def test_urml_capsule_constructor_exists():
    assert callable(urml_Capsule.__init__)


def test_urml_capsule_constructor_args():
    sig = inspect.signature(urml_Capsule.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "root" in params, "Missing parameter 'root'"

def test_urml_capsule_has_name():
    assert hasattr(urml_Capsule, "name")
    descriptor = None
    for klass in urml_Capsule.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_urml_capsule_has_root():
    assert hasattr(urml_Capsule, "root")
    descriptor = None
    for klass in urml_Capsule.__mro__:
        if "root" in klass.__dict__:
            descriptor = klass.__dict__["root"]
            break
    assert isinstance(descriptor, property)



def test_urml_model_is_not_abstract():
    assert not inspect.isabstract(urml_Model)


def test_urml_model_constructor_exists():
    assert callable(urml_Model.__init__)


def test_urml_model_constructor_args():
    sig = inspect.signature(urml_Model.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_urml_model_has_name():
    assert hasattr(urml_Model, "name")
    descriptor = None
    for klass in urml_Model.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)


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
StringExpression_strategy = st.builds(
    StringExpression,
)
urml_ConcatenateExpression_strategy = st.builds(
    urml_ConcatenateExpression,
)
urml_StringExpression_strategy = st.builds(
    urml_StringExpression,
    str=
        safe_text
)
urml_Identifiable_strategy = st.builds(
    urml_Identifiable,
    isInt=
        st.booleans(),
    name=
        safe_text,
    isBool=
        st.booleans()
)
Literal_strategy = st.builds(
    Literal,
)
urml_FunctionCall_strategy = st.builds(
    urml_FunctionCall,
)
urml_BoolLiteral_strategy = st.builds(
    urml_BoolLiteral,
    true=
        st.booleans()
)
urml_IntLiteral_strategy = st.builds(
    urml_IntLiteral,
    int=
        st.integers()
)
Expression_strategy = st.builds(
    Expression,
)
urml_UnaryExpression_strategy = st.builds(
    urml_UnaryExpression,
)
urml_Identifier_strategy = st.builds(
    urml_Identifier,
)
urml_Plus_strategy = st.builds(
    urml_Plus,
)
urml_LessThanOrEqual_strategy = st.builds(
    urml_LessThanOrEqual,
)
urml_ConditionalAndExpression_strategy = st.builds(
    urml_ConditionalAndExpression,
)
urml_Equal_strategy = st.builds(
    urml_Equal,
)
urml_GreaterThanOrEqual_strategy = st.builds(
    urml_GreaterThanOrEqual,
)
urml_GreaterThan_strategy = st.builds(
    urml_GreaterThan,
)
urml_LessThan_strategy = st.builds(
    urml_LessThan,
)
urml_NotEqual_strategy = st.builds(
    urml_NotEqual,
)
urml_Literal_strategy = st.builds(
    urml_Literal,
)
urml_ConditionalOrExpression_strategy = st.builds(
    urml_ConditionalOrExpression,
)
urml_Modulo_strategy = st.builds(
    urml_Modulo,
)
urml_Multiply_strategy = st.builds(
    urml_Multiply,
)
urml_Minus_strategy = st.builds(
    urml_Minus,
)
urml_Divide_strategy = st.builds(
    urml_Divide,
)
urml_NotBooleanExpression_strategy = st.builds(
    urml_NotBooleanExpression,
)
Statement_strategy = st.builds(
    Statement,
)
urml_IfStatement_strategy = st.builds(
    urml_IfStatement,
)
urml_Statement_strategy = st.builds(
    urml_Statement,
)
urml_WhileLoop_strategy = st.builds(
    urml_WhileLoop,
)
urml_ActionCode_strategy = st.builds(
    urml_ActionCode,
)
urml_Transition_strategy = st.builds(
    urml_Transition,
    name=
        safe_text,
    init=
        st.booleans(),
    universal=
        st.booleans()
)
urml_State__strategy = st.builds(
    urml_State_,
    final=
        st.booleans(),
    name=
        safe_text
)
StatementOperation_strategy = st.builds(
    StatementOperation,
)
urml_NoOp_strategy = st.builds(
    urml_NoOp,
)
urml_IfStatementOperation_strategy = st.builds(
    urml_IfStatementOperation,
)
urml_SendTrigger_strategy = st.builds(
    urml_SendTrigger,
)
urml_ReturnStatement_strategy = st.builds(
    urml_ReturnStatement,
)
urml_Variable_strategy = st.builds(
    urml_Variable,
    assign=
        st.booleans()
)
urml_Assignment_strategy = st.builds(
    urml_Assignment,
)
urml_LogStatement_strategy = st.builds(
    urml_LogStatement,
)
urml_Invoke_strategy = st.builds(
    urml_Invoke,
)
urml_InformTimer_strategy = st.builds(
    urml_InformTimer,
)
urml_WhileLoopOperation_strategy = st.builds(
    urml_WhileLoopOperation,
)
urml_StatementOperation_strategy = st.builds(
    urml_StatementOperation,
)
urml_Trigger_out_strategy = st.builds(
    urml_Trigger_out,
)
Identifiable_strategy = st.builds(
    Identifiable,
)
urml_Assignable_strategy = st.builds(
    urml_Assignable,
)
urml_IncomingVariable_strategy = st.builds(
    urml_IncomingVariable,
)
urml_Trigger_in_strategy = st.builds(
    urml_Trigger_in,
)
urml_Connector_strategy = st.builds(
    urml_Connector,
)
urml_CapsuleInst_strategy = st.builds(
    urml_CapsuleInst,
    name=
        safe_text
)
urml_LogPort_strategy = st.builds(
    urml_LogPort,
    name=
        safe_text
)
urml_TimerPort_strategy = st.builds(
    urml_TimerPort,
    name=
        safe_text
)
urml_Port_strategy = st.builds(
    urml_Port,
    conjugated=
        st.booleans(),
    name=
        safe_text
)
urml_OperationCode_strategy = st.builds(
    urml_OperationCode,
)
urml_StateMachine_strategy = st.builds(
    urml_StateMachine,
)
urml_Operation_strategy = st.builds(
    urml_Operation,
    isInt=
        st.booleans(),
    isVoid=
        st.booleans(),
    isBool=
        st.booleans(),
    name=
        safe_text
)
urml_Signal_strategy = st.builds(
    urml_Signal,
    name=
        safe_text
)
urml_Expression_strategy = st.builds(
    urml_Expression,
)
Assignable_strategy = st.builds(
    Assignable,
)
urml_Attribute_strategy = st.builds(
    urml_Attribute,
)
urml_LocalVar_strategy = st.builds(
    urml_LocalVar,
)
urml_Protocol_strategy = st.builds(
    urml_Protocol,
    name=
        safe_text
)
urml_Capsule_strategy = st.builds(
    urml_Capsule,
    name=
        safe_text,
    root=
        st.booleans()
)
urml_Model_strategy = st.builds(
    urml_Model,
    name=
        safe_text
)

@given(instance=StringExpression_strategy)
@settings(max_examples=50)
def test_stringexpression_instantiation(instance):
    assert isinstance(instance, StringExpression)

@given(instance=urml_ConcatenateExpression_strategy)
@settings(max_examples=50)
def test_urml_concatenateexpression_instantiation(instance):
    assert isinstance(instance, urml_ConcatenateExpression)

@given(instance=urml_StringExpression_strategy)
@settings(max_examples=50)
def test_urml_stringexpression_instantiation(instance):
    assert isinstance(instance, urml_StringExpression)



@given(instance=urml_StringExpression_strategy)
def test_urml_stringexpression_str_setter(instance):
    original = instance.str
    instance.str = original
    assert instance.str == original

@given(instance=urml_Identifiable_strategy)
@settings(max_examples=50)
def test_urml_identifiable_instantiation(instance):
    assert isinstance(instance, urml_Identifiable)



@given(instance=urml_Identifiable_strategy)
def test_urml_identifiable_isInt_setter(instance):
    original = instance.isInt
    instance.isInt = original
    assert instance.isInt == original



@given(instance=urml_Identifiable_strategy)
def test_urml_identifiable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=urml_Identifiable_strategy)
def test_urml_identifiable_isBool_setter(instance):
    original = instance.isBool
    instance.isBool = original
    assert instance.isBool == original

@given(instance=Literal_strategy)
@settings(max_examples=50)
def test_literal_instantiation(instance):
    assert isinstance(instance, Literal)

@given(instance=urml_FunctionCall_strategy)
@settings(max_examples=50)
def test_urml_functioncall_instantiation(instance):
    assert isinstance(instance, urml_FunctionCall)

@given(instance=urml_BoolLiteral_strategy)
@settings(max_examples=50)
def test_urml_boolliteral_instantiation(instance):
    assert isinstance(instance, urml_BoolLiteral)



@given(instance=urml_BoolLiteral_strategy)
def test_urml_boolliteral_true_setter(instance):
    original = instance.true
    instance.true = original
    assert instance.true == original

@given(instance=urml_IntLiteral_strategy)
@settings(max_examples=50)
def test_urml_intliteral_instantiation(instance):
    assert isinstance(instance, urml_IntLiteral)



@given(instance=urml_IntLiteral_strategy)
def test_urml_intliteral_int_setter(instance):
    original = instance.int
    instance.int = original
    assert instance.int == original

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=urml_UnaryExpression_strategy)
@settings(max_examples=50)
def test_urml_unaryexpression_instantiation(instance):
    assert isinstance(instance, urml_UnaryExpression)

@given(instance=urml_Identifier_strategy)
@settings(max_examples=50)
def test_urml_identifier_instantiation(instance):
    assert isinstance(instance, urml_Identifier)

@given(instance=urml_Plus_strategy)
@settings(max_examples=50)
def test_urml_plus_instantiation(instance):
    assert isinstance(instance, urml_Plus)

@given(instance=urml_LessThanOrEqual_strategy)
@settings(max_examples=50)
def test_urml_lessthanorequal_instantiation(instance):
    assert isinstance(instance, urml_LessThanOrEqual)

@given(instance=urml_ConditionalAndExpression_strategy)
@settings(max_examples=50)
def test_urml_conditionalandexpression_instantiation(instance):
    assert isinstance(instance, urml_ConditionalAndExpression)

@given(instance=urml_Equal_strategy)
@settings(max_examples=50)
def test_urml_equal_instantiation(instance):
    assert isinstance(instance, urml_Equal)

@given(instance=urml_GreaterThanOrEqual_strategy)
@settings(max_examples=50)
def test_urml_greaterthanorequal_instantiation(instance):
    assert isinstance(instance, urml_GreaterThanOrEqual)

@given(instance=urml_GreaterThan_strategy)
@settings(max_examples=50)
def test_urml_greaterthan_instantiation(instance):
    assert isinstance(instance, urml_GreaterThan)

@given(instance=urml_LessThan_strategy)
@settings(max_examples=50)
def test_urml_lessthan_instantiation(instance):
    assert isinstance(instance, urml_LessThan)

@given(instance=urml_NotEqual_strategy)
@settings(max_examples=50)
def test_urml_notequal_instantiation(instance):
    assert isinstance(instance, urml_NotEqual)

@given(instance=urml_Literal_strategy)
@settings(max_examples=50)
def test_urml_literal_instantiation(instance):
    assert isinstance(instance, urml_Literal)

@given(instance=urml_ConditionalOrExpression_strategy)
@settings(max_examples=50)
def test_urml_conditionalorexpression_instantiation(instance):
    assert isinstance(instance, urml_ConditionalOrExpression)

@given(instance=urml_Modulo_strategy)
@settings(max_examples=50)
def test_urml_modulo_instantiation(instance):
    assert isinstance(instance, urml_Modulo)

@given(instance=urml_Multiply_strategy)
@settings(max_examples=50)
def test_urml_multiply_instantiation(instance):
    assert isinstance(instance, urml_Multiply)

@given(instance=urml_Minus_strategy)
@settings(max_examples=50)
def test_urml_minus_instantiation(instance):
    assert isinstance(instance, urml_Minus)

@given(instance=urml_Divide_strategy)
@settings(max_examples=50)
def test_urml_divide_instantiation(instance):
    assert isinstance(instance, urml_Divide)

@given(instance=urml_NotBooleanExpression_strategy)
@settings(max_examples=50)
def test_urml_notbooleanexpression_instantiation(instance):
    assert isinstance(instance, urml_NotBooleanExpression)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=urml_IfStatement_strategy)
@settings(max_examples=50)
def test_urml_ifstatement_instantiation(instance):
    assert isinstance(instance, urml_IfStatement)

@given(instance=urml_Statement_strategy)
@settings(max_examples=50)
def test_urml_statement_instantiation(instance):
    assert isinstance(instance, urml_Statement)

@given(instance=urml_WhileLoop_strategy)
@settings(max_examples=50)
def test_urml_whileloop_instantiation(instance):
    assert isinstance(instance, urml_WhileLoop)

@given(instance=urml_ActionCode_strategy)
@settings(max_examples=50)
def test_urml_actioncode_instantiation(instance):
    assert isinstance(instance, urml_ActionCode)

@given(instance=urml_Transition_strategy)
@settings(max_examples=50)
def test_urml_transition_instantiation(instance):
    assert isinstance(instance, urml_Transition)



@given(instance=urml_Transition_strategy)
def test_urml_transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=urml_Transition_strategy)
def test_urml_transition_init_setter(instance):
    original = instance.init
    instance.init = original
    assert instance.init == original



@given(instance=urml_Transition_strategy)
def test_urml_transition_universal_setter(instance):
    original = instance.universal
    instance.universal = original
    assert instance.universal == original

@given(instance=urml_State__strategy)
@settings(max_examples=50)
def test_urml_state__instantiation(instance):
    assert isinstance(instance, urml_State_)



@given(instance=urml_State__strategy)
def test_urml_state__final_setter(instance):
    original = instance.final
    instance.final = original
    assert instance.final == original



@given(instance=urml_State__strategy)
def test_urml_state__name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=StatementOperation_strategy)
@settings(max_examples=50)
def test_statementoperation_instantiation(instance):
    assert isinstance(instance, StatementOperation)

@given(instance=urml_NoOp_strategy)
@settings(max_examples=50)
def test_urml_noop_instantiation(instance):
    assert isinstance(instance, urml_NoOp)

@given(instance=urml_IfStatementOperation_strategy)
@settings(max_examples=50)
def test_urml_ifstatementoperation_instantiation(instance):
    assert isinstance(instance, urml_IfStatementOperation)

@given(instance=urml_SendTrigger_strategy)
@settings(max_examples=50)
def test_urml_sendtrigger_instantiation(instance):
    assert isinstance(instance, urml_SendTrigger)

@given(instance=urml_ReturnStatement_strategy)
@settings(max_examples=50)
def test_urml_returnstatement_instantiation(instance):
    assert isinstance(instance, urml_ReturnStatement)

@given(instance=urml_Variable_strategy)
@settings(max_examples=50)
def test_urml_variable_instantiation(instance):
    assert isinstance(instance, urml_Variable)



@given(instance=urml_Variable_strategy)
def test_urml_variable_assign_setter(instance):
    original = instance.assign
    instance.assign = original
    assert instance.assign == original

@given(instance=urml_Assignment_strategy)
@settings(max_examples=50)
def test_urml_assignment_instantiation(instance):
    assert isinstance(instance, urml_Assignment)

@given(instance=urml_LogStatement_strategy)
@settings(max_examples=50)
def test_urml_logstatement_instantiation(instance):
    assert isinstance(instance, urml_LogStatement)

@given(instance=urml_Invoke_strategy)
@settings(max_examples=50)
def test_urml_invoke_instantiation(instance):
    assert isinstance(instance, urml_Invoke)

@given(instance=urml_InformTimer_strategy)
@settings(max_examples=50)
def test_urml_informtimer_instantiation(instance):
    assert isinstance(instance, urml_InformTimer)

@given(instance=urml_WhileLoopOperation_strategy)
@settings(max_examples=50)
def test_urml_whileloopoperation_instantiation(instance):
    assert isinstance(instance, urml_WhileLoopOperation)

@given(instance=urml_StatementOperation_strategy)
@settings(max_examples=50)
def test_urml_statementoperation_instantiation(instance):
    assert isinstance(instance, urml_StatementOperation)

@given(instance=urml_Trigger_out_strategy)
@settings(max_examples=50)
def test_urml_trigger_out_instantiation(instance):
    assert isinstance(instance, urml_Trigger_out)

@given(instance=Identifiable_strategy)
@settings(max_examples=50)
def test_identifiable_instantiation(instance):
    assert isinstance(instance, Identifiable)

@given(instance=urml_Assignable_strategy)
@settings(max_examples=50)
def test_urml_assignable_instantiation(instance):
    assert isinstance(instance, urml_Assignable)

@given(instance=urml_IncomingVariable_strategy)
@settings(max_examples=50)
def test_urml_incomingvariable_instantiation(instance):
    assert isinstance(instance, urml_IncomingVariable)

@given(instance=urml_Trigger_in_strategy)
@settings(max_examples=50)
def test_urml_trigger_in_instantiation(instance):
    assert isinstance(instance, urml_Trigger_in)

@given(instance=urml_Connector_strategy)
@settings(max_examples=50)
def test_urml_connector_instantiation(instance):
    assert isinstance(instance, urml_Connector)

@given(instance=urml_CapsuleInst_strategy)
@settings(max_examples=50)
def test_urml_capsuleinst_instantiation(instance):
    assert isinstance(instance, urml_CapsuleInst)



@given(instance=urml_CapsuleInst_strategy)
def test_urml_capsuleinst_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=urml_LogPort_strategy)
@settings(max_examples=50)
def test_urml_logport_instantiation(instance):
    assert isinstance(instance, urml_LogPort)



@given(instance=urml_LogPort_strategy)
def test_urml_logport_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=urml_TimerPort_strategy)
@settings(max_examples=50)
def test_urml_timerport_instantiation(instance):
    assert isinstance(instance, urml_TimerPort)



@given(instance=urml_TimerPort_strategy)
def test_urml_timerport_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=urml_Port_strategy)
@settings(max_examples=50)
def test_urml_port_instantiation(instance):
    assert isinstance(instance, urml_Port)



@given(instance=urml_Port_strategy)
def test_urml_port_conjugated_setter(instance):
    original = instance.conjugated
    instance.conjugated = original
    assert instance.conjugated == original



@given(instance=urml_Port_strategy)
def test_urml_port_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=urml_OperationCode_strategy)
@settings(max_examples=50)
def test_urml_operationcode_instantiation(instance):
    assert isinstance(instance, urml_OperationCode)

@given(instance=urml_StateMachine_strategy)
@settings(max_examples=50)
def test_urml_statemachine_instantiation(instance):
    assert isinstance(instance, urml_StateMachine)

@given(instance=urml_Operation_strategy)
@settings(max_examples=50)
def test_urml_operation_instantiation(instance):
    assert isinstance(instance, urml_Operation)



@given(instance=urml_Operation_strategy)
def test_urml_operation_isInt_setter(instance):
    original = instance.isInt
    instance.isInt = original
    assert instance.isInt == original



@given(instance=urml_Operation_strategy)
def test_urml_operation_isVoid_setter(instance):
    original = instance.isVoid
    instance.isVoid = original
    assert instance.isVoid == original



@given(instance=urml_Operation_strategy)
def test_urml_operation_isBool_setter(instance):
    original = instance.isBool
    instance.isBool = original
    assert instance.isBool == original



@given(instance=urml_Operation_strategy)
def test_urml_operation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=urml_Signal_strategy)
@settings(max_examples=50)
def test_urml_signal_instantiation(instance):
    assert isinstance(instance, urml_Signal)



@given(instance=urml_Signal_strategy)
def test_urml_signal_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=urml_Expression_strategy)
@settings(max_examples=50)
def test_urml_expression_instantiation(instance):
    assert isinstance(instance, urml_Expression)

@given(instance=Assignable_strategy)
@settings(max_examples=50)
def test_assignable_instantiation(instance):
    assert isinstance(instance, Assignable)

@given(instance=urml_Attribute_strategy)
@settings(max_examples=50)
def test_urml_attribute_instantiation(instance):
    assert isinstance(instance, urml_Attribute)

@given(instance=urml_LocalVar_strategy)
@settings(max_examples=50)
def test_urml_localvar_instantiation(instance):
    assert isinstance(instance, urml_LocalVar)

@given(instance=urml_Protocol_strategy)
@settings(max_examples=50)
def test_urml_protocol_instantiation(instance):
    assert isinstance(instance, urml_Protocol)



@given(instance=urml_Protocol_strategy)
def test_urml_protocol_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=urml_Capsule_strategy)
@settings(max_examples=50)
def test_urml_capsule_instantiation(instance):
    assert isinstance(instance, urml_Capsule)



@given(instance=urml_Capsule_strategy)
def test_urml_capsule_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=urml_Capsule_strategy)
def test_urml_capsule_root_setter(instance):
    original = instance.root
    instance.root = original
    assert instance.root == original

@given(instance=urml_Model_strategy)
@settings(max_examples=50)
def test_urml_model_instantiation(instance):
    assert isinstance(instance, urml_Model)



@given(instance=urml_Model_strategy)
def test_urml_model_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
