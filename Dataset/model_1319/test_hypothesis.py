import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    stateMachineDsl_SetAction,
    stateMachineDsl_EObject,
    ChangeAction,
    stateMachineDsl_ResetAction,
    stateMachineDsl_DecrementAction,
    stateMachineDsl_IncrementAction,
    stateMachineDsl_ProcedureUse,
    Expression,
    stateMachineDsl_NumberExp,
    stateMachineDsl_Or,
    stateMachineDsl_MulOrDiv,
    stateMachineDsl_DoubleExp,
    stateMachineDsl_VarRef,
    stateMachineDsl_StringExp,
    stateMachineDsl_MinusCond,
    stateMachineDsl_Comparison,
    stateMachineDsl_Equality,
    stateMachineDsl_BoolExp,
    stateMachineDsl_Parenthesis,
    stateMachineDsl_And,
    stateMachineDsl_Not,
    stateMachineDsl_PlusCond,
    stateMachineDsl_FunctionUse,
    stateMachineDsl_ChangeAction,
    stateMachineDsl_Expression,
    stateMachineDsl_VarType,
    stateMachineDsl_VarParName,
    ExtDeclaration,
    stateMachineDsl_Function,
    stateMachineDsl_Parameter,
    stateMachineDsl_Member,
    stateMachineDsl_ParameterFunction,
    stateMachineDsl_Declaration,
    stateMachineDsl_StateMachine,
    stateMachineDsl_Condition,
    stateMachineDsl_CommandAction,
    stateMachineDsl_Transition,
    stateMachineDsl_Action,
    stateMachineDsl_MemberState,
    stateMachineDsl_Procedure,
    stateMachineDsl_Event,
    stateMachineDsl_ExtDeclaration,
    stateMachineDsl_Variable,
    stateMachineDsl_State,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_statemachinedsl_setaction_is_not_abstract():
    assert not inspect.isabstract(stateMachineDsl_SetAction)


def test_statemachinedsl_setaction_constructor_exists():
    assert callable(stateMachineDsl_SetAction.__init__)


def test_statemachinedsl_setaction_constructor_args():
    sig = inspect.signature(stateMachineDsl_SetAction.__init__)
    params = list(sig.parameters.keys())



def test_statemachinedsl_eobject_is_not_abstract():
    assert not inspect.isabstract(stateMachineDsl_EObject)


def test_statemachinedsl_eobject_constructor_exists():
    assert callable(stateMachineDsl_EObject.__init__)


def test_statemachinedsl_eobject_constructor_args():
    sig = inspect.signature(stateMachineDsl_EObject.__init__)
    params = list(sig.parameters.keys())



def test_changeaction_is_not_abstract():
    assert not inspect.isabstract(ChangeAction)


def test_changeaction_constructor_exists():
    assert callable(ChangeAction.__init__)


def test_changeaction_constructor_args():
    sig = inspect.signature(ChangeAction.__init__)
    params = list(sig.parameters.keys())



def test_statemachinedsl_resetaction_is_not_abstract():
    assert not inspect.isabstract(stateMachineDsl_ResetAction)


def test_statemachinedsl_resetaction_constructor_exists():
    assert callable(stateMachineDsl_ResetAction.__init__)


def test_statemachinedsl_resetaction_constructor_args():
    sig = inspect.signature(stateMachineDsl_ResetAction.__init__)
    params = list(sig.parameters.keys())



def test_statemachinedsl_decrementaction_is_not_abstract():
    assert not inspect.isabstract(stateMachineDsl_DecrementAction)


def test_statemachinedsl_decrementaction_constructor_exists():
    assert callable(stateMachineDsl_DecrementAction.__init__)


def test_statemachinedsl_decrementaction_constructor_args():
    sig = inspect.signature(stateMachineDsl_DecrementAction.__init__)
    params = list(sig.parameters.keys())



def test_statemachinedsl_incrementaction_is_not_abstract():
    assert not inspect.isabstract(stateMachineDsl_IncrementAction)


def test_statemachinedsl_incrementaction_constructor_exists():
    assert callable(stateMachineDsl_IncrementAction.__init__)


def test_statemachinedsl_incrementaction_constructor_args():
    sig = inspect.signature(stateMachineDsl_IncrementAction.__init__)
    params = list(sig.parameters.keys())



def test_statemachinedsl_procedureuse_is_not_abstract():
    assert not inspect.isabstract(stateMachineDsl_ProcedureUse)


def test_statemachinedsl_procedureuse_constructor_exists():
    assert callable(stateMachineDsl_ProcedureUse.__init__)


def test_statemachinedsl_procedureuse_constructor_args():
    sig = inspect.signature(stateMachineDsl_ProcedureUse.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_statemachinedsl_numberexp_is_not_abstract():
    assert not inspect.isabstract(stateMachineDsl_NumberExp)


def test_statemachinedsl_numberexp_constructor_exists():
    assert callable(stateMachineDsl_NumberExp.__init__)


def test_statemachinedsl_numberexp_constructor_args():
    sig = inspect.signature(stateMachineDsl_NumberExp.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "negative" in params, "Missing parameter 'negative'"

def test_statemachinedsl_numberexp_has_value():
    assert hasattr(stateMachineDsl_NumberExp, "value")
    descriptor = None
    for klass in stateMachineDsl_NumberExp.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_statemachinedsl_numberexp_has_negative():
    assert hasattr(stateMachineDsl_NumberExp, "negative")
    descriptor = None
    for klass in stateMachineDsl_NumberExp.__mro__:
        if "negative" in klass.__dict__:
            descriptor = klass.__dict__["negative"]
            break
    assert isinstance(descriptor, property)



def test_statemachinedsl_or_is_not_abstract():
    assert not inspect.isabstract(stateMachineDsl_Or)


def test_statemachinedsl_or_constructor_exists():
    assert callable(stateMachineDsl_Or.__init__)


def test_statemachinedsl_or_constructor_args():
    sig = inspect.signature(stateMachineDsl_Or.__init__)
    params = list(sig.parameters.keys())



def test_statemachinedsl_mulordiv_is_not_abstract():
    assert not inspect.isabstract(stateMachineDsl_MulOrDiv)


def test_statemachinedsl_mulordiv_constructor_exists():
    assert callable(stateMachineDsl_MulOrDiv.__init__)


def test_statemachinedsl_mulordiv_constructor_args():
    sig = inspect.signature(stateMachineDsl_MulOrDiv.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_statemachinedsl_mulordiv_has_op():
    assert hasattr(stateMachineDsl_MulOrDiv, "op")
    descriptor = None
    for klass in stateMachineDsl_MulOrDiv.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_statemachinedsl_doubleexp_is_not_abstract():
    assert not inspect.isabstract(stateMachineDsl_DoubleExp)


def test_statemachinedsl_doubleexp_constructor_exists():
    assert callable(stateMachineDsl_DoubleExp.__init__)


def test_statemachinedsl_doubleexp_constructor_args():
    sig = inspect.signature(stateMachineDsl_DoubleExp.__init__)
    params = list(sig.parameters.keys())
    assert "number" in params, "Missing parameter 'number'"
    assert "negative" in params, "Missing parameter 'negative'"
    assert "decimal" in params, "Missing parameter 'decimal'"

def test_statemachinedsl_doubleexp_has_number():
    assert hasattr(stateMachineDsl_DoubleExp, "number")
    descriptor = None
    for klass in stateMachineDsl_DoubleExp.__mro__:
        if "number" in klass.__dict__:
            descriptor = klass.__dict__["number"]
            break
    assert isinstance(descriptor, property)

def test_statemachinedsl_doubleexp_has_negative():
    assert hasattr(stateMachineDsl_DoubleExp, "negative")
    descriptor = None
    for klass in stateMachineDsl_DoubleExp.__mro__:
        if "negative" in klass.__dict__:
            descriptor = klass.__dict__["negative"]
            break
    assert isinstance(descriptor, property)

def test_statemachinedsl_doubleexp_has_decimal():
    assert hasattr(stateMachineDsl_DoubleExp, "decimal")
    descriptor = None
    for klass in stateMachineDsl_DoubleExp.__mro__:
        if "decimal" in klass.__dict__:
            descriptor = klass.__dict__["decimal"]
            break
    assert isinstance(descriptor, property)



def test_statemachinedsl_varref_is_not_abstract():
    assert not inspect.isabstract(stateMachineDsl_VarRef)


def test_statemachinedsl_varref_constructor_exists():
    assert callable(stateMachineDsl_VarRef.__init__)


def test_statemachinedsl_varref_constructor_args():
    sig = inspect.signature(stateMachineDsl_VarRef.__init__)
    params = list(sig.parameters.keys())



def test_statemachinedsl_stringexp_is_not_abstract():
    assert not inspect.isabstract(stateMachineDsl_StringExp)


def test_statemachinedsl_stringexp_constructor_exists():
    assert callable(stateMachineDsl_StringExp.__init__)


def test_statemachinedsl_stringexp_constructor_args():
    sig = inspect.signature(stateMachineDsl_StringExp.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_statemachinedsl_stringexp_has_value():
    assert hasattr(stateMachineDsl_StringExp, "value")
    descriptor = None
    for klass in stateMachineDsl_StringExp.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_statemachinedsl_minuscond_is_not_abstract():
    assert not inspect.isabstract(stateMachineDsl_MinusCond)


def test_statemachinedsl_minuscond_constructor_exists():
    assert callable(stateMachineDsl_MinusCond.__init__)


def test_statemachinedsl_minuscond_constructor_args():
    sig = inspect.signature(stateMachineDsl_MinusCond.__init__)
    params = list(sig.parameters.keys())



def test_statemachinedsl_comparison_is_not_abstract():
    assert not inspect.isabstract(stateMachineDsl_Comparison)


def test_statemachinedsl_comparison_constructor_exists():
    assert callable(stateMachineDsl_Comparison.__init__)


def test_statemachinedsl_comparison_constructor_args():
    sig = inspect.signature(stateMachineDsl_Comparison.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_statemachinedsl_comparison_has_op():
    assert hasattr(stateMachineDsl_Comparison, "op")
    descriptor = None
    for klass in stateMachineDsl_Comparison.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_statemachinedsl_equality_is_not_abstract():
    assert not inspect.isabstract(stateMachineDsl_Equality)


def test_statemachinedsl_equality_constructor_exists():
    assert callable(stateMachineDsl_Equality.__init__)


def test_statemachinedsl_equality_constructor_args():
    sig = inspect.signature(stateMachineDsl_Equality.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_statemachinedsl_equality_has_op():
    assert hasattr(stateMachineDsl_Equality, "op")
    descriptor = None
    for klass in stateMachineDsl_Equality.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_statemachinedsl_boolexp_is_not_abstract():
    assert not inspect.isabstract(stateMachineDsl_BoolExp)


def test_statemachinedsl_boolexp_constructor_exists():
    assert callable(stateMachineDsl_BoolExp.__init__)


def test_statemachinedsl_boolexp_constructor_args():
    sig = inspect.signature(stateMachineDsl_BoolExp.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_statemachinedsl_boolexp_has_value():
    assert hasattr(stateMachineDsl_BoolExp, "value")
    descriptor = None
    for klass in stateMachineDsl_BoolExp.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_statemachinedsl_parenthesis_is_not_abstract():
    assert not inspect.isabstract(stateMachineDsl_Parenthesis)


def test_statemachinedsl_parenthesis_constructor_exists():
    assert callable(stateMachineDsl_Parenthesis.__init__)


def test_statemachinedsl_parenthesis_constructor_args():
    sig = inspect.signature(stateMachineDsl_Parenthesis.__init__)
    params = list(sig.parameters.keys())



def test_statemachinedsl_and_is_not_abstract():
    assert not inspect.isabstract(stateMachineDsl_And)


def test_statemachinedsl_and_constructor_exists():
    assert callable(stateMachineDsl_And.__init__)


def test_statemachinedsl_and_constructor_args():
    sig = inspect.signature(stateMachineDsl_And.__init__)
    params = list(sig.parameters.keys())



def test_statemachinedsl_not_is_not_abstract():
    assert not inspect.isabstract(stateMachineDsl_Not)


def test_statemachinedsl_not_constructor_exists():
    assert callable(stateMachineDsl_Not.__init__)


def test_statemachinedsl_not_constructor_args():
    sig = inspect.signature(stateMachineDsl_Not.__init__)
    params = list(sig.parameters.keys())



def test_statemachinedsl_pluscond_is_not_abstract():
    assert not inspect.isabstract(stateMachineDsl_PlusCond)


def test_statemachinedsl_pluscond_constructor_exists():
    assert callable(stateMachineDsl_PlusCond.__init__)


def test_statemachinedsl_pluscond_constructor_args():
    sig = inspect.signature(stateMachineDsl_PlusCond.__init__)
    params = list(sig.parameters.keys())



def test_statemachinedsl_functionuse_is_not_abstract():
    assert not inspect.isabstract(stateMachineDsl_FunctionUse)


def test_statemachinedsl_functionuse_constructor_exists():
    assert callable(stateMachineDsl_FunctionUse.__init__)


def test_statemachinedsl_functionuse_constructor_args():
    sig = inspect.signature(stateMachineDsl_FunctionUse.__init__)
    params = list(sig.parameters.keys())



def test_statemachinedsl_changeaction_is_not_abstract():
    assert not inspect.isabstract(stateMachineDsl_ChangeAction)


def test_statemachinedsl_changeaction_constructor_exists():
    assert callable(stateMachineDsl_ChangeAction.__init__)


def test_statemachinedsl_changeaction_constructor_args():
    sig = inspect.signature(stateMachineDsl_ChangeAction.__init__)
    params = list(sig.parameters.keys())



def test_statemachinedsl_expression_is_not_abstract():
    assert not inspect.isabstract(stateMachineDsl_Expression)


def test_statemachinedsl_expression_constructor_exists():
    assert callable(stateMachineDsl_Expression.__init__)


def test_statemachinedsl_expression_constructor_args():
    sig = inspect.signature(stateMachineDsl_Expression.__init__)
    params = list(sig.parameters.keys())



def test_statemachinedsl_vartype_is_not_abstract():
    assert not inspect.isabstract(stateMachineDsl_VarType)


def test_statemachinedsl_vartype_constructor_exists():
    assert callable(stateMachineDsl_VarType.__init__)


def test_statemachinedsl_vartype_constructor_args():
    sig = inspect.signature(stateMachineDsl_VarType.__init__)
    params = list(sig.parameters.keys())
    assert "vt" in params, "Missing parameter 'vt'"

def test_statemachinedsl_vartype_has_vt():
    assert hasattr(stateMachineDsl_VarType, "vt")
    descriptor = None
    for klass in stateMachineDsl_VarType.__mro__:
        if "vt" in klass.__dict__:
            descriptor = klass.__dict__["vt"]
            break
    assert isinstance(descriptor, property)



def test_statemachinedsl_varparname_is_not_abstract():
    assert not inspect.isabstract(stateMachineDsl_VarParName)


def test_statemachinedsl_varparname_constructor_exists():
    assert callable(stateMachineDsl_VarParName.__init__)


def test_statemachinedsl_varparname_constructor_args():
    sig = inspect.signature(stateMachineDsl_VarParName.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachinedsl_varparname_has_name():
    assert hasattr(stateMachineDsl_VarParName, "name")
    descriptor = None
    for klass in stateMachineDsl_VarParName.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_extdeclaration_is_not_abstract():
    assert not inspect.isabstract(ExtDeclaration)


def test_extdeclaration_constructor_exists():
    assert callable(ExtDeclaration.__init__)


def test_extdeclaration_constructor_args():
    sig = inspect.signature(ExtDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_statemachinedsl_function_is_not_abstract():
    assert not inspect.isabstract(stateMachineDsl_Function)


def test_statemachinedsl_function_constructor_exists():
    assert callable(stateMachineDsl_Function.__init__)


def test_statemachinedsl_function_constructor_args():
    sig = inspect.signature(stateMachineDsl_Function.__init__)
    params = list(sig.parameters.keys())



def test_statemachinedsl_parameter_is_not_abstract():
    assert not inspect.isabstract(stateMachineDsl_Parameter)


def test_statemachinedsl_parameter_constructor_exists():
    assert callable(stateMachineDsl_Parameter.__init__)


def test_statemachinedsl_parameter_constructor_args():
    sig = inspect.signature(stateMachineDsl_Parameter.__init__)
    params = list(sig.parameters.keys())



def test_statemachinedsl_member_is_not_abstract():
    assert not inspect.isabstract(stateMachineDsl_Member)


def test_statemachinedsl_member_constructor_exists():
    assert callable(stateMachineDsl_Member.__init__)


def test_statemachinedsl_member_constructor_args():
    sig = inspect.signature(stateMachineDsl_Member.__init__)
    params = list(sig.parameters.keys())



def test_statemachinedsl_parameterfunction_is_not_abstract():
    assert not inspect.isabstract(stateMachineDsl_ParameterFunction)


def test_statemachinedsl_parameterfunction_constructor_exists():
    assert callable(stateMachineDsl_ParameterFunction.__init__)


def test_statemachinedsl_parameterfunction_constructor_args():
    sig = inspect.signature(stateMachineDsl_ParameterFunction.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachinedsl_parameterfunction_has_name():
    assert hasattr(stateMachineDsl_ParameterFunction, "name")
    descriptor = None
    for klass in stateMachineDsl_ParameterFunction.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statemachinedsl_declaration_is_not_abstract():
    assert not inspect.isabstract(stateMachineDsl_Declaration)


def test_statemachinedsl_declaration_constructor_exists():
    assert callable(stateMachineDsl_Declaration.__init__)


def test_statemachinedsl_declaration_constructor_args():
    sig = inspect.signature(stateMachineDsl_Declaration.__init__)
    params = list(sig.parameters.keys())



def test_statemachinedsl_statemachine_is_not_abstract():
    assert not inspect.isabstract(stateMachineDsl_StateMachine)


def test_statemachinedsl_statemachine_constructor_exists():
    assert callable(stateMachineDsl_StateMachine.__init__)


def test_statemachinedsl_statemachine_constructor_args():
    sig = inspect.signature(stateMachineDsl_StateMachine.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachinedsl_statemachine_has_name():
    assert hasattr(stateMachineDsl_StateMachine, "name")
    descriptor = None
    for klass in stateMachineDsl_StateMachine.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statemachinedsl_condition_is_not_abstract():
    assert not inspect.isabstract(stateMachineDsl_Condition)


def test_statemachinedsl_condition_constructor_exists():
    assert callable(stateMachineDsl_Condition.__init__)


def test_statemachinedsl_condition_constructor_args():
    sig = inspect.signature(stateMachineDsl_Condition.__init__)
    params = list(sig.parameters.keys())



def test_statemachinedsl_commandaction_is_not_abstract():
    assert not inspect.isabstract(stateMachineDsl_CommandAction)


def test_statemachinedsl_commandaction_constructor_exists():
    assert callable(stateMachineDsl_CommandAction.__init__)


def test_statemachinedsl_commandaction_constructor_args():
    sig = inspect.signature(stateMachineDsl_CommandAction.__init__)
    params = list(sig.parameters.keys())



def test_statemachinedsl_transition_is_not_abstract():
    assert not inspect.isabstract(stateMachineDsl_Transition)


def test_statemachinedsl_transition_constructor_exists():
    assert callable(stateMachineDsl_Transition.__init__)


def test_statemachinedsl_transition_constructor_args():
    sig = inspect.signature(stateMachineDsl_Transition.__init__)
    params = list(sig.parameters.keys())



def test_statemachinedsl_action_is_not_abstract():
    assert not inspect.isabstract(stateMachineDsl_Action)


def test_statemachinedsl_action_constructor_exists():
    assert callable(stateMachineDsl_Action.__init__)


def test_statemachinedsl_action_constructor_args():
    sig = inspect.signature(stateMachineDsl_Action.__init__)
    params = list(sig.parameters.keys())



def test_statemachinedsl_memberstate_is_not_abstract():
    assert not inspect.isabstract(stateMachineDsl_MemberState)


def test_statemachinedsl_memberstate_constructor_exists():
    assert callable(stateMachineDsl_MemberState.__init__)


def test_statemachinedsl_memberstate_constructor_args():
    sig = inspect.signature(stateMachineDsl_MemberState.__init__)
    params = list(sig.parameters.keys())



def test_statemachinedsl_procedure_is_not_abstract():
    assert not inspect.isabstract(stateMachineDsl_Procedure)


def test_statemachinedsl_procedure_constructor_exists():
    assert callable(stateMachineDsl_Procedure.__init__)


def test_statemachinedsl_procedure_constructor_args():
    sig = inspect.signature(stateMachineDsl_Procedure.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachinedsl_procedure_has_name():
    assert hasattr(stateMachineDsl_Procedure, "name")
    descriptor = None
    for klass in stateMachineDsl_Procedure.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statemachinedsl_event_is_not_abstract():
    assert not inspect.isabstract(stateMachineDsl_Event)


def test_statemachinedsl_event_constructor_exists():
    assert callable(stateMachineDsl_Event.__init__)


def test_statemachinedsl_event_constructor_args():
    sig = inspect.signature(stateMachineDsl_Event.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachinedsl_event_has_name():
    assert hasattr(stateMachineDsl_Event, "name")
    descriptor = None
    for klass in stateMachineDsl_Event.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statemachinedsl_extdeclaration_is_not_abstract():
    assert not inspect.isabstract(stateMachineDsl_ExtDeclaration)


def test_statemachinedsl_extdeclaration_constructor_exists():
    assert callable(stateMachineDsl_ExtDeclaration.__init__)


def test_statemachinedsl_extdeclaration_constructor_args():
    sig = inspect.signature(stateMachineDsl_ExtDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachinedsl_extdeclaration_has_name():
    assert hasattr(stateMachineDsl_ExtDeclaration, "name")
    descriptor = None
    for klass in stateMachineDsl_ExtDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statemachinedsl_variable_is_not_abstract():
    assert not inspect.isabstract(stateMachineDsl_Variable)


def test_statemachinedsl_variable_constructor_exists():
    assert callable(stateMachineDsl_Variable.__init__)


def test_statemachinedsl_variable_constructor_args():
    sig = inspect.signature(stateMachineDsl_Variable.__init__)
    params = list(sig.parameters.keys())



def test_statemachinedsl_state_is_not_abstract():
    assert not inspect.isabstract(stateMachineDsl_State)


def test_statemachinedsl_state_constructor_exists():
    assert callable(stateMachineDsl_State.__init__)


def test_statemachinedsl_state_constructor_args():
    sig = inspect.signature(stateMachineDsl_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachinedsl_state_has_name():
    assert hasattr(stateMachineDsl_State, "name")
    descriptor = None
    for klass in stateMachineDsl_State.__mro__:
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
stateMachineDsl_SetAction_strategy = st.builds(
    stateMachineDsl_SetAction,
)
stateMachineDsl_EObject_strategy = st.builds(
    stateMachineDsl_EObject,
)
ChangeAction_strategy = st.builds(
    ChangeAction,
)
stateMachineDsl_ResetAction_strategy = st.builds(
    stateMachineDsl_ResetAction,
)
stateMachineDsl_DecrementAction_strategy = st.builds(
    stateMachineDsl_DecrementAction,
)
stateMachineDsl_IncrementAction_strategy = st.builds(
    stateMachineDsl_IncrementAction,
)
stateMachineDsl_ProcedureUse_strategy = st.builds(
    stateMachineDsl_ProcedureUse,
)
Expression_strategy = st.builds(
    Expression,
)
stateMachineDsl_NumberExp_strategy = st.builds(
    stateMachineDsl_NumberExp,
    value=
        st.integers(),
    negative=
        safe_text
)
stateMachineDsl_Or_strategy = st.builds(
    stateMachineDsl_Or,
)
stateMachineDsl_MulOrDiv_strategy = st.builds(
    stateMachineDsl_MulOrDiv,
    op=
        safe_text
)
stateMachineDsl_DoubleExp_strategy = st.builds(
    stateMachineDsl_DoubleExp,
    number=
        st.integers(),
    negative=
        safe_text,
    decimal=
        st.integers()
)
stateMachineDsl_VarRef_strategy = st.builds(
    stateMachineDsl_VarRef,
)
stateMachineDsl_StringExp_strategy = st.builds(
    stateMachineDsl_StringExp,
    value=
        safe_text
)
stateMachineDsl_MinusCond_strategy = st.builds(
    stateMachineDsl_MinusCond,
)
stateMachineDsl_Comparison_strategy = st.builds(
    stateMachineDsl_Comparison,
    op=
        safe_text
)
stateMachineDsl_Equality_strategy = st.builds(
    stateMachineDsl_Equality,
    op=
        safe_text
)
stateMachineDsl_BoolExp_strategy = st.builds(
    stateMachineDsl_BoolExp,
    value=
        safe_text
)
stateMachineDsl_Parenthesis_strategy = st.builds(
    stateMachineDsl_Parenthesis,
)
stateMachineDsl_And_strategy = st.builds(
    stateMachineDsl_And,
)
stateMachineDsl_Not_strategy = st.builds(
    stateMachineDsl_Not,
)
stateMachineDsl_PlusCond_strategy = st.builds(
    stateMachineDsl_PlusCond,
)
stateMachineDsl_FunctionUse_strategy = st.builds(
    stateMachineDsl_FunctionUse,
)
stateMachineDsl_ChangeAction_strategy = st.builds(
    stateMachineDsl_ChangeAction,
)
stateMachineDsl_Expression_strategy = st.builds(
    stateMachineDsl_Expression,
)
stateMachineDsl_VarType_strategy = st.builds(
    stateMachineDsl_VarType,
    vt=
        safe_text
)
stateMachineDsl_VarParName_strategy = st.builds(
    stateMachineDsl_VarParName,
    name=
        safe_text
)
ExtDeclaration_strategy = st.builds(
    ExtDeclaration,
)
stateMachineDsl_Function_strategy = st.builds(
    stateMachineDsl_Function,
)
stateMachineDsl_Parameter_strategy = st.builds(
    stateMachineDsl_Parameter,
)
stateMachineDsl_Member_strategy = st.builds(
    stateMachineDsl_Member,
)
stateMachineDsl_ParameterFunction_strategy = st.builds(
    stateMachineDsl_ParameterFunction,
    name=
        safe_text
)
stateMachineDsl_Declaration_strategy = st.builds(
    stateMachineDsl_Declaration,
)
stateMachineDsl_StateMachine_strategy = st.builds(
    stateMachineDsl_StateMachine,
    name=
        safe_text
)
stateMachineDsl_Condition_strategy = st.builds(
    stateMachineDsl_Condition,
)
stateMachineDsl_CommandAction_strategy = st.builds(
    stateMachineDsl_CommandAction,
)
stateMachineDsl_Transition_strategy = st.builds(
    stateMachineDsl_Transition,
)
stateMachineDsl_Action_strategy = st.builds(
    stateMachineDsl_Action,
)
stateMachineDsl_MemberState_strategy = st.builds(
    stateMachineDsl_MemberState,
)
stateMachineDsl_Procedure_strategy = st.builds(
    stateMachineDsl_Procedure,
    name=
        safe_text
)
stateMachineDsl_Event_strategy = st.builds(
    stateMachineDsl_Event,
    name=
        safe_text
)
stateMachineDsl_ExtDeclaration_strategy = st.builds(
    stateMachineDsl_ExtDeclaration,
    name=
        safe_text
)
stateMachineDsl_Variable_strategy = st.builds(
    stateMachineDsl_Variable,
)
stateMachineDsl_State_strategy = st.builds(
    stateMachineDsl_State,
    name=
        safe_text
)

@given(instance=stateMachineDsl_SetAction_strategy)
@settings(max_examples=50)
def test_statemachinedsl_setaction_instantiation(instance):
    assert isinstance(instance, stateMachineDsl_SetAction)

@given(instance=stateMachineDsl_EObject_strategy)
@settings(max_examples=50)
def test_statemachinedsl_eobject_instantiation(instance):
    assert isinstance(instance, stateMachineDsl_EObject)

@given(instance=ChangeAction_strategy)
@settings(max_examples=50)
def test_changeaction_instantiation(instance):
    assert isinstance(instance, ChangeAction)

@given(instance=stateMachineDsl_ResetAction_strategy)
@settings(max_examples=50)
def test_statemachinedsl_resetaction_instantiation(instance):
    assert isinstance(instance, stateMachineDsl_ResetAction)

@given(instance=stateMachineDsl_DecrementAction_strategy)
@settings(max_examples=50)
def test_statemachinedsl_decrementaction_instantiation(instance):
    assert isinstance(instance, stateMachineDsl_DecrementAction)

@given(instance=stateMachineDsl_IncrementAction_strategy)
@settings(max_examples=50)
def test_statemachinedsl_incrementaction_instantiation(instance):
    assert isinstance(instance, stateMachineDsl_IncrementAction)

@given(instance=stateMachineDsl_ProcedureUse_strategy)
@settings(max_examples=50)
def test_statemachinedsl_procedureuse_instantiation(instance):
    assert isinstance(instance, stateMachineDsl_ProcedureUse)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=stateMachineDsl_NumberExp_strategy)
@settings(max_examples=50)
def test_statemachinedsl_numberexp_instantiation(instance):
    assert isinstance(instance, stateMachineDsl_NumberExp)



@given(instance=stateMachineDsl_NumberExp_strategy)
def test_statemachinedsl_numberexp_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=stateMachineDsl_NumberExp_strategy)
def test_statemachinedsl_numberexp_negative_setter(instance):
    original = instance.negative
    instance.negative = original
    assert instance.negative == original

@given(instance=stateMachineDsl_Or_strategy)
@settings(max_examples=50)
def test_statemachinedsl_or_instantiation(instance):
    assert isinstance(instance, stateMachineDsl_Or)

@given(instance=stateMachineDsl_MulOrDiv_strategy)
@settings(max_examples=50)
def test_statemachinedsl_mulordiv_instantiation(instance):
    assert isinstance(instance, stateMachineDsl_MulOrDiv)



@given(instance=stateMachineDsl_MulOrDiv_strategy)
def test_statemachinedsl_mulordiv_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=stateMachineDsl_DoubleExp_strategy)
@settings(max_examples=50)
def test_statemachinedsl_doubleexp_instantiation(instance):
    assert isinstance(instance, stateMachineDsl_DoubleExp)



@given(instance=stateMachineDsl_DoubleExp_strategy)
def test_statemachinedsl_doubleexp_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original



@given(instance=stateMachineDsl_DoubleExp_strategy)
def test_statemachinedsl_doubleexp_negative_setter(instance):
    original = instance.negative
    instance.negative = original
    assert instance.negative == original



@given(instance=stateMachineDsl_DoubleExp_strategy)
def test_statemachinedsl_doubleexp_decimal_setter(instance):
    original = instance.decimal
    instance.decimal = original
    assert instance.decimal == original

@given(instance=stateMachineDsl_VarRef_strategy)
@settings(max_examples=50)
def test_statemachinedsl_varref_instantiation(instance):
    assert isinstance(instance, stateMachineDsl_VarRef)

@given(instance=stateMachineDsl_StringExp_strategy)
@settings(max_examples=50)
def test_statemachinedsl_stringexp_instantiation(instance):
    assert isinstance(instance, stateMachineDsl_StringExp)



@given(instance=stateMachineDsl_StringExp_strategy)
def test_statemachinedsl_stringexp_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=stateMachineDsl_MinusCond_strategy)
@settings(max_examples=50)
def test_statemachinedsl_minuscond_instantiation(instance):
    assert isinstance(instance, stateMachineDsl_MinusCond)

@given(instance=stateMachineDsl_Comparison_strategy)
@settings(max_examples=50)
def test_statemachinedsl_comparison_instantiation(instance):
    assert isinstance(instance, stateMachineDsl_Comparison)



@given(instance=stateMachineDsl_Comparison_strategy)
def test_statemachinedsl_comparison_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=stateMachineDsl_Equality_strategy)
@settings(max_examples=50)
def test_statemachinedsl_equality_instantiation(instance):
    assert isinstance(instance, stateMachineDsl_Equality)



@given(instance=stateMachineDsl_Equality_strategy)
def test_statemachinedsl_equality_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=stateMachineDsl_BoolExp_strategy)
@settings(max_examples=50)
def test_statemachinedsl_boolexp_instantiation(instance):
    assert isinstance(instance, stateMachineDsl_BoolExp)



@given(instance=stateMachineDsl_BoolExp_strategy)
def test_statemachinedsl_boolexp_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=stateMachineDsl_Parenthesis_strategy)
@settings(max_examples=50)
def test_statemachinedsl_parenthesis_instantiation(instance):
    assert isinstance(instance, stateMachineDsl_Parenthesis)

@given(instance=stateMachineDsl_And_strategy)
@settings(max_examples=50)
def test_statemachinedsl_and_instantiation(instance):
    assert isinstance(instance, stateMachineDsl_And)

@given(instance=stateMachineDsl_Not_strategy)
@settings(max_examples=50)
def test_statemachinedsl_not_instantiation(instance):
    assert isinstance(instance, stateMachineDsl_Not)

@given(instance=stateMachineDsl_PlusCond_strategy)
@settings(max_examples=50)
def test_statemachinedsl_pluscond_instantiation(instance):
    assert isinstance(instance, stateMachineDsl_PlusCond)

@given(instance=stateMachineDsl_FunctionUse_strategy)
@settings(max_examples=50)
def test_statemachinedsl_functionuse_instantiation(instance):
    assert isinstance(instance, stateMachineDsl_FunctionUse)

@given(instance=stateMachineDsl_ChangeAction_strategy)
@settings(max_examples=50)
def test_statemachinedsl_changeaction_instantiation(instance):
    assert isinstance(instance, stateMachineDsl_ChangeAction)

@given(instance=stateMachineDsl_Expression_strategy)
@settings(max_examples=50)
def test_statemachinedsl_expression_instantiation(instance):
    assert isinstance(instance, stateMachineDsl_Expression)

@given(instance=stateMachineDsl_VarType_strategy)
@settings(max_examples=50)
def test_statemachinedsl_vartype_instantiation(instance):
    assert isinstance(instance, stateMachineDsl_VarType)



@given(instance=stateMachineDsl_VarType_strategy)
def test_statemachinedsl_vartype_vt_setter(instance):
    original = instance.vt
    instance.vt = original
    assert instance.vt == original

@given(instance=stateMachineDsl_VarParName_strategy)
@settings(max_examples=50)
def test_statemachinedsl_varparname_instantiation(instance):
    assert isinstance(instance, stateMachineDsl_VarParName)



@given(instance=stateMachineDsl_VarParName_strategy)
def test_statemachinedsl_varparname_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ExtDeclaration_strategy)
@settings(max_examples=50)
def test_extdeclaration_instantiation(instance):
    assert isinstance(instance, ExtDeclaration)

@given(instance=stateMachineDsl_Function_strategy)
@settings(max_examples=50)
def test_statemachinedsl_function_instantiation(instance):
    assert isinstance(instance, stateMachineDsl_Function)

@given(instance=stateMachineDsl_Parameter_strategy)
@settings(max_examples=50)
def test_statemachinedsl_parameter_instantiation(instance):
    assert isinstance(instance, stateMachineDsl_Parameter)

@given(instance=stateMachineDsl_Member_strategy)
@settings(max_examples=50)
def test_statemachinedsl_member_instantiation(instance):
    assert isinstance(instance, stateMachineDsl_Member)

@given(instance=stateMachineDsl_ParameterFunction_strategy)
@settings(max_examples=50)
def test_statemachinedsl_parameterfunction_instantiation(instance):
    assert isinstance(instance, stateMachineDsl_ParameterFunction)



@given(instance=stateMachineDsl_ParameterFunction_strategy)
def test_statemachinedsl_parameterfunction_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=stateMachineDsl_Declaration_strategy)
@settings(max_examples=50)
def test_statemachinedsl_declaration_instantiation(instance):
    assert isinstance(instance, stateMachineDsl_Declaration)

@given(instance=stateMachineDsl_StateMachine_strategy)
@settings(max_examples=50)
def test_statemachinedsl_statemachine_instantiation(instance):
    assert isinstance(instance, stateMachineDsl_StateMachine)



@given(instance=stateMachineDsl_StateMachine_strategy)
def test_statemachinedsl_statemachine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=stateMachineDsl_Condition_strategy)
@settings(max_examples=50)
def test_statemachinedsl_condition_instantiation(instance):
    assert isinstance(instance, stateMachineDsl_Condition)

@given(instance=stateMachineDsl_CommandAction_strategy)
@settings(max_examples=50)
def test_statemachinedsl_commandaction_instantiation(instance):
    assert isinstance(instance, stateMachineDsl_CommandAction)

@given(instance=stateMachineDsl_Transition_strategy)
@settings(max_examples=50)
def test_statemachinedsl_transition_instantiation(instance):
    assert isinstance(instance, stateMachineDsl_Transition)

@given(instance=stateMachineDsl_Action_strategy)
@settings(max_examples=50)
def test_statemachinedsl_action_instantiation(instance):
    assert isinstance(instance, stateMachineDsl_Action)

@given(instance=stateMachineDsl_MemberState_strategy)
@settings(max_examples=50)
def test_statemachinedsl_memberstate_instantiation(instance):
    assert isinstance(instance, stateMachineDsl_MemberState)

@given(instance=stateMachineDsl_Procedure_strategy)
@settings(max_examples=50)
def test_statemachinedsl_procedure_instantiation(instance):
    assert isinstance(instance, stateMachineDsl_Procedure)



@given(instance=stateMachineDsl_Procedure_strategy)
def test_statemachinedsl_procedure_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=stateMachineDsl_Event_strategy)
@settings(max_examples=50)
def test_statemachinedsl_event_instantiation(instance):
    assert isinstance(instance, stateMachineDsl_Event)



@given(instance=stateMachineDsl_Event_strategy)
def test_statemachinedsl_event_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=stateMachineDsl_ExtDeclaration_strategy)
@settings(max_examples=50)
def test_statemachinedsl_extdeclaration_instantiation(instance):
    assert isinstance(instance, stateMachineDsl_ExtDeclaration)



@given(instance=stateMachineDsl_ExtDeclaration_strategy)
def test_statemachinedsl_extdeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=stateMachineDsl_Variable_strategy)
@settings(max_examples=50)
def test_statemachinedsl_variable_instantiation(instance):
    assert isinstance(instance, stateMachineDsl_Variable)

@given(instance=stateMachineDsl_State_strategy)
@settings(max_examples=50)
def test_statemachinedsl_state_instantiation(instance):
    assert isinstance(instance, stateMachineDsl_State)



@given(instance=stateMachineDsl_State_strategy)
def test_statemachinedsl_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
