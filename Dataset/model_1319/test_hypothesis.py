import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    stateMachineDsl::SetAction,
    stateMachineDsl::EObject,
    ChangeAction,
    stateMachineDsl::DecrementAction,
    stateMachineDsl::ResetAction,
    stateMachineDsl::IncrementAction,
    stateMachineDsl::ProcedureUse,
    Expression,
    stateMachineDsl::Parenthesis,
    stateMachineDsl::And,
    stateMachineDsl::MinusCond,
    stateMachineDsl::Or,
    stateMachineDsl::MulOrDiv,
    stateMachineDsl::BoolExp,
    stateMachineDsl::Not,
    stateMachineDsl::Equality,
    stateMachineDsl::PlusCond,
    stateMachineDsl::Comparison,
    stateMachineDsl::DoubleExp,
    stateMachineDsl::NumberExp,
    stateMachineDsl::StringExp,
    stateMachineDsl::VarRef,
    stateMachineDsl::FunctionUse,
    stateMachineDsl::ChangeAction,
    stateMachineDsl::Expression,
    stateMachineDsl::VarType,
    stateMachineDsl::VarParName,
    ExtDeclaration,
    stateMachineDsl::Function,
    stateMachineDsl::Parameter,
    stateMachineDsl::Member,
    stateMachineDsl::ParameterFunction,
    stateMachineDsl::Declaration,
    stateMachineDsl::StateMachine,
    stateMachineDsl::Condition,
    stateMachineDsl::CommandAction,
    stateMachineDsl::Transition,
    stateMachineDsl::Action,
    stateMachineDsl::MemberState,
    stateMachineDsl::Procedure,
    stateMachineDsl::Event,
    stateMachineDsl::ExtDeclaration,
    stateMachineDsl::Variable,
    stateMachineDsl::State,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_statemachinedsl::setaction_is_not_abstract():
    assert not inspect.isabstract(stateMachineDsl::SetAction)


def test_statemachinedsl::setaction_constructor_exists():
    assert callable(stateMachineDsl::SetAction.__init__)


def test_statemachinedsl::setaction_constructor_args():
    sig = inspect.signature(stateMachineDsl::SetAction.__init__)
    params = list(sig.parameters.keys())



def test_statemachinedsl::eobject_is_not_abstract():
    assert not inspect.isabstract(stateMachineDsl::EObject)


def test_statemachinedsl::eobject_constructor_exists():
    assert callable(stateMachineDsl::EObject.__init__)


def test_statemachinedsl::eobject_constructor_args():
    sig = inspect.signature(stateMachineDsl::EObject.__init__)
    params = list(sig.parameters.keys())



def test_changeaction_is_not_abstract():
    assert not inspect.isabstract(ChangeAction)


def test_changeaction_constructor_exists():
    assert callable(ChangeAction.__init__)


def test_changeaction_constructor_args():
    sig = inspect.signature(ChangeAction.__init__)
    params = list(sig.parameters.keys())



def test_statemachinedsl::decrementaction_is_not_abstract():
    assert not inspect.isabstract(stateMachineDsl::DecrementAction)


def test_statemachinedsl::decrementaction_constructor_exists():
    assert callable(stateMachineDsl::DecrementAction.__init__)


def test_statemachinedsl::decrementaction_constructor_args():
    sig = inspect.signature(stateMachineDsl::DecrementAction.__init__)
    params = list(sig.parameters.keys())



def test_statemachinedsl::resetaction_is_not_abstract():
    assert not inspect.isabstract(stateMachineDsl::ResetAction)


def test_statemachinedsl::resetaction_constructor_exists():
    assert callable(stateMachineDsl::ResetAction.__init__)


def test_statemachinedsl::resetaction_constructor_args():
    sig = inspect.signature(stateMachineDsl::ResetAction.__init__)
    params = list(sig.parameters.keys())



def test_statemachinedsl::incrementaction_is_not_abstract():
    assert not inspect.isabstract(stateMachineDsl::IncrementAction)


def test_statemachinedsl::incrementaction_constructor_exists():
    assert callable(stateMachineDsl::IncrementAction.__init__)


def test_statemachinedsl::incrementaction_constructor_args():
    sig = inspect.signature(stateMachineDsl::IncrementAction.__init__)
    params = list(sig.parameters.keys())



def test_statemachinedsl::procedureuse_is_not_abstract():
    assert not inspect.isabstract(stateMachineDsl::ProcedureUse)


def test_statemachinedsl::procedureuse_constructor_exists():
    assert callable(stateMachineDsl::ProcedureUse.__init__)


def test_statemachinedsl::procedureuse_constructor_args():
    sig = inspect.signature(stateMachineDsl::ProcedureUse.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_statemachinedsl::parenthesis_is_not_abstract():
    assert not inspect.isabstract(stateMachineDsl::Parenthesis)


def test_statemachinedsl::parenthesis_constructor_exists():
    assert callable(stateMachineDsl::Parenthesis.__init__)


def test_statemachinedsl::parenthesis_constructor_args():
    sig = inspect.signature(stateMachineDsl::Parenthesis.__init__)
    params = list(sig.parameters.keys())



def test_statemachinedsl::and_is_not_abstract():
    assert not inspect.isabstract(stateMachineDsl::And)


def test_statemachinedsl::and_constructor_exists():
    assert callable(stateMachineDsl::And.__init__)


def test_statemachinedsl::and_constructor_args():
    sig = inspect.signature(stateMachineDsl::And.__init__)
    params = list(sig.parameters.keys())



def test_statemachinedsl::minuscond_is_not_abstract():
    assert not inspect.isabstract(stateMachineDsl::MinusCond)


def test_statemachinedsl::minuscond_constructor_exists():
    assert callable(stateMachineDsl::MinusCond.__init__)


def test_statemachinedsl::minuscond_constructor_args():
    sig = inspect.signature(stateMachineDsl::MinusCond.__init__)
    params = list(sig.parameters.keys())



def test_statemachinedsl::or_is_not_abstract():
    assert not inspect.isabstract(stateMachineDsl::Or)


def test_statemachinedsl::or_constructor_exists():
    assert callable(stateMachineDsl::Or.__init__)


def test_statemachinedsl::or_constructor_args():
    sig = inspect.signature(stateMachineDsl::Or.__init__)
    params = list(sig.parameters.keys())



def test_statemachinedsl::mulordiv_is_not_abstract():
    assert not inspect.isabstract(stateMachineDsl::MulOrDiv)


def test_statemachinedsl::mulordiv_constructor_exists():
    assert callable(stateMachineDsl::MulOrDiv.__init__)


def test_statemachinedsl::mulordiv_constructor_args():
    sig = inspect.signature(stateMachineDsl::MulOrDiv.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_statemachinedsl::mulordiv_has_op():
    assert hasattr(stateMachineDsl::MulOrDiv, "op")
    descriptor = None
    for klass in stateMachineDsl::MulOrDiv.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_statemachinedsl::boolexp_is_not_abstract():
    assert not inspect.isabstract(stateMachineDsl::BoolExp)


def test_statemachinedsl::boolexp_constructor_exists():
    assert callable(stateMachineDsl::BoolExp.__init__)


def test_statemachinedsl::boolexp_constructor_args():
    sig = inspect.signature(stateMachineDsl::BoolExp.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_statemachinedsl::boolexp_has_value():
    assert hasattr(stateMachineDsl::BoolExp, "value")
    descriptor = None
    for klass in stateMachineDsl::BoolExp.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_statemachinedsl::not_is_not_abstract():
    assert not inspect.isabstract(stateMachineDsl::Not)


def test_statemachinedsl::not_constructor_exists():
    assert callable(stateMachineDsl::Not.__init__)


def test_statemachinedsl::not_constructor_args():
    sig = inspect.signature(stateMachineDsl::Not.__init__)
    params = list(sig.parameters.keys())



def test_statemachinedsl::equality_is_not_abstract():
    assert not inspect.isabstract(stateMachineDsl::Equality)


def test_statemachinedsl::equality_constructor_exists():
    assert callable(stateMachineDsl::Equality.__init__)


def test_statemachinedsl::equality_constructor_args():
    sig = inspect.signature(stateMachineDsl::Equality.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_statemachinedsl::equality_has_op():
    assert hasattr(stateMachineDsl::Equality, "op")
    descriptor = None
    for klass in stateMachineDsl::Equality.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_statemachinedsl::pluscond_is_not_abstract():
    assert not inspect.isabstract(stateMachineDsl::PlusCond)


def test_statemachinedsl::pluscond_constructor_exists():
    assert callable(stateMachineDsl::PlusCond.__init__)


def test_statemachinedsl::pluscond_constructor_args():
    sig = inspect.signature(stateMachineDsl::PlusCond.__init__)
    params = list(sig.parameters.keys())



def test_statemachinedsl::comparison_is_not_abstract():
    assert not inspect.isabstract(stateMachineDsl::Comparison)


def test_statemachinedsl::comparison_constructor_exists():
    assert callable(stateMachineDsl::Comparison.__init__)


def test_statemachinedsl::comparison_constructor_args():
    sig = inspect.signature(stateMachineDsl::Comparison.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_statemachinedsl::comparison_has_op():
    assert hasattr(stateMachineDsl::Comparison, "op")
    descriptor = None
    for klass in stateMachineDsl::Comparison.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_statemachinedsl::doubleexp_is_not_abstract():
    assert not inspect.isabstract(stateMachineDsl::DoubleExp)


def test_statemachinedsl::doubleexp_constructor_exists():
    assert callable(stateMachineDsl::DoubleExp.__init__)


def test_statemachinedsl::doubleexp_constructor_args():
    sig = inspect.signature(stateMachineDsl::DoubleExp.__init__)
    params = list(sig.parameters.keys())
    assert "negative" in params, "Missing parameter 'negative'"
    assert "number" in params, "Missing parameter 'number'"
    assert "decimal" in params, "Missing parameter 'decimal'"

def test_statemachinedsl::doubleexp_has_negative():
    assert hasattr(stateMachineDsl::DoubleExp, "negative")
    descriptor = None
    for klass in stateMachineDsl::DoubleExp.__mro__:
        if "negative" in klass.__dict__:
            descriptor = klass.__dict__["negative"]
            break
    assert isinstance(descriptor, property)

def test_statemachinedsl::doubleexp_has_number():
    assert hasattr(stateMachineDsl::DoubleExp, "number")
    descriptor = None
    for klass in stateMachineDsl::DoubleExp.__mro__:
        if "number" in klass.__dict__:
            descriptor = klass.__dict__["number"]
            break
    assert isinstance(descriptor, property)

def test_statemachinedsl::doubleexp_has_decimal():
    assert hasattr(stateMachineDsl::DoubleExp, "decimal")
    descriptor = None
    for klass in stateMachineDsl::DoubleExp.__mro__:
        if "decimal" in klass.__dict__:
            descriptor = klass.__dict__["decimal"]
            break
    assert isinstance(descriptor, property)



def test_statemachinedsl::numberexp_is_not_abstract():
    assert not inspect.isabstract(stateMachineDsl::NumberExp)


def test_statemachinedsl::numberexp_constructor_exists():
    assert callable(stateMachineDsl::NumberExp.__init__)


def test_statemachinedsl::numberexp_constructor_args():
    sig = inspect.signature(stateMachineDsl::NumberExp.__init__)
    params = list(sig.parameters.keys())
    assert "negative" in params, "Missing parameter 'negative'"
    assert "value" in params, "Missing parameter 'value'"

def test_statemachinedsl::numberexp_has_negative():
    assert hasattr(stateMachineDsl::NumberExp, "negative")
    descriptor = None
    for klass in stateMachineDsl::NumberExp.__mro__:
        if "negative" in klass.__dict__:
            descriptor = klass.__dict__["negative"]
            break
    assert isinstance(descriptor, property)

def test_statemachinedsl::numberexp_has_value():
    assert hasattr(stateMachineDsl::NumberExp, "value")
    descriptor = None
    for klass in stateMachineDsl::NumberExp.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_statemachinedsl::stringexp_is_not_abstract():
    assert not inspect.isabstract(stateMachineDsl::StringExp)


def test_statemachinedsl::stringexp_constructor_exists():
    assert callable(stateMachineDsl::StringExp.__init__)


def test_statemachinedsl::stringexp_constructor_args():
    sig = inspect.signature(stateMachineDsl::StringExp.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_statemachinedsl::stringexp_has_value():
    assert hasattr(stateMachineDsl::StringExp, "value")
    descriptor = None
    for klass in stateMachineDsl::StringExp.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_statemachinedsl::varref_is_not_abstract():
    assert not inspect.isabstract(stateMachineDsl::VarRef)


def test_statemachinedsl::varref_constructor_exists():
    assert callable(stateMachineDsl::VarRef.__init__)


def test_statemachinedsl::varref_constructor_args():
    sig = inspect.signature(stateMachineDsl::VarRef.__init__)
    params = list(sig.parameters.keys())



def test_statemachinedsl::functionuse_is_not_abstract():
    assert not inspect.isabstract(stateMachineDsl::FunctionUse)


def test_statemachinedsl::functionuse_constructor_exists():
    assert callable(stateMachineDsl::FunctionUse.__init__)


def test_statemachinedsl::functionuse_constructor_args():
    sig = inspect.signature(stateMachineDsl::FunctionUse.__init__)
    params = list(sig.parameters.keys())



def test_statemachinedsl::changeaction_is_not_abstract():
    assert not inspect.isabstract(stateMachineDsl::ChangeAction)


def test_statemachinedsl::changeaction_constructor_exists():
    assert callable(stateMachineDsl::ChangeAction.__init__)


def test_statemachinedsl::changeaction_constructor_args():
    sig = inspect.signature(stateMachineDsl::ChangeAction.__init__)
    params = list(sig.parameters.keys())



def test_statemachinedsl::expression_is_not_abstract():
    assert not inspect.isabstract(stateMachineDsl::Expression)


def test_statemachinedsl::expression_constructor_exists():
    assert callable(stateMachineDsl::Expression.__init__)


def test_statemachinedsl::expression_constructor_args():
    sig = inspect.signature(stateMachineDsl::Expression.__init__)
    params = list(sig.parameters.keys())



def test_statemachinedsl::vartype_is_not_abstract():
    assert not inspect.isabstract(stateMachineDsl::VarType)


def test_statemachinedsl::vartype_constructor_exists():
    assert callable(stateMachineDsl::VarType.__init__)


def test_statemachinedsl::vartype_constructor_args():
    sig = inspect.signature(stateMachineDsl::VarType.__init__)
    params = list(sig.parameters.keys())
    assert "vt" in params, "Missing parameter 'vt'"

def test_statemachinedsl::vartype_has_vt():
    assert hasattr(stateMachineDsl::VarType, "vt")
    descriptor = None
    for klass in stateMachineDsl::VarType.__mro__:
        if "vt" in klass.__dict__:
            descriptor = klass.__dict__["vt"]
            break
    assert isinstance(descriptor, property)



def test_statemachinedsl::varparname_is_not_abstract():
    assert not inspect.isabstract(stateMachineDsl::VarParName)


def test_statemachinedsl::varparname_constructor_exists():
    assert callable(stateMachineDsl::VarParName.__init__)


def test_statemachinedsl::varparname_constructor_args():
    sig = inspect.signature(stateMachineDsl::VarParName.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachinedsl::varparname_has_name():
    assert hasattr(stateMachineDsl::VarParName, "name")
    descriptor = None
    for klass in stateMachineDsl::VarParName.__mro__:
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



def test_statemachinedsl::function_is_not_abstract():
    assert not inspect.isabstract(stateMachineDsl::Function)


def test_statemachinedsl::function_constructor_exists():
    assert callable(stateMachineDsl::Function.__init__)


def test_statemachinedsl::function_constructor_args():
    sig = inspect.signature(stateMachineDsl::Function.__init__)
    params = list(sig.parameters.keys())



def test_statemachinedsl::parameter_is_not_abstract():
    assert not inspect.isabstract(stateMachineDsl::Parameter)


def test_statemachinedsl::parameter_constructor_exists():
    assert callable(stateMachineDsl::Parameter.__init__)


def test_statemachinedsl::parameter_constructor_args():
    sig = inspect.signature(stateMachineDsl::Parameter.__init__)
    params = list(sig.parameters.keys())



def test_statemachinedsl::member_is_not_abstract():
    assert not inspect.isabstract(stateMachineDsl::Member)


def test_statemachinedsl::member_constructor_exists():
    assert callable(stateMachineDsl::Member.__init__)


def test_statemachinedsl::member_constructor_args():
    sig = inspect.signature(stateMachineDsl::Member.__init__)
    params = list(sig.parameters.keys())



def test_statemachinedsl::parameterfunction_is_not_abstract():
    assert not inspect.isabstract(stateMachineDsl::ParameterFunction)


def test_statemachinedsl::parameterfunction_constructor_exists():
    assert callable(stateMachineDsl::ParameterFunction.__init__)


def test_statemachinedsl::parameterfunction_constructor_args():
    sig = inspect.signature(stateMachineDsl::ParameterFunction.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachinedsl::parameterfunction_has_name():
    assert hasattr(stateMachineDsl::ParameterFunction, "name")
    descriptor = None
    for klass in stateMachineDsl::ParameterFunction.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statemachinedsl::declaration_is_not_abstract():
    assert not inspect.isabstract(stateMachineDsl::Declaration)


def test_statemachinedsl::declaration_constructor_exists():
    assert callable(stateMachineDsl::Declaration.__init__)


def test_statemachinedsl::declaration_constructor_args():
    sig = inspect.signature(stateMachineDsl::Declaration.__init__)
    params = list(sig.parameters.keys())



def test_statemachinedsl::statemachine_is_not_abstract():
    assert not inspect.isabstract(stateMachineDsl::StateMachine)


def test_statemachinedsl::statemachine_constructor_exists():
    assert callable(stateMachineDsl::StateMachine.__init__)


def test_statemachinedsl::statemachine_constructor_args():
    sig = inspect.signature(stateMachineDsl::StateMachine.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachinedsl::statemachine_has_name():
    assert hasattr(stateMachineDsl::StateMachine, "name")
    descriptor = None
    for klass in stateMachineDsl::StateMachine.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statemachinedsl::condition_is_not_abstract():
    assert not inspect.isabstract(stateMachineDsl::Condition)


def test_statemachinedsl::condition_constructor_exists():
    assert callable(stateMachineDsl::Condition.__init__)


def test_statemachinedsl::condition_constructor_args():
    sig = inspect.signature(stateMachineDsl::Condition.__init__)
    params = list(sig.parameters.keys())



def test_statemachinedsl::commandaction_is_not_abstract():
    assert not inspect.isabstract(stateMachineDsl::CommandAction)


def test_statemachinedsl::commandaction_constructor_exists():
    assert callable(stateMachineDsl::CommandAction.__init__)


def test_statemachinedsl::commandaction_constructor_args():
    sig = inspect.signature(stateMachineDsl::CommandAction.__init__)
    params = list(sig.parameters.keys())



def test_statemachinedsl::transition_is_not_abstract():
    assert not inspect.isabstract(stateMachineDsl::Transition)


def test_statemachinedsl::transition_constructor_exists():
    assert callable(stateMachineDsl::Transition.__init__)


def test_statemachinedsl::transition_constructor_args():
    sig = inspect.signature(stateMachineDsl::Transition.__init__)
    params = list(sig.parameters.keys())



def test_statemachinedsl::action_is_not_abstract():
    assert not inspect.isabstract(stateMachineDsl::Action)


def test_statemachinedsl::action_constructor_exists():
    assert callable(stateMachineDsl::Action.__init__)


def test_statemachinedsl::action_constructor_args():
    sig = inspect.signature(stateMachineDsl::Action.__init__)
    params = list(sig.parameters.keys())



def test_statemachinedsl::memberstate_is_not_abstract():
    assert not inspect.isabstract(stateMachineDsl::MemberState)


def test_statemachinedsl::memberstate_constructor_exists():
    assert callable(stateMachineDsl::MemberState.__init__)


def test_statemachinedsl::memberstate_constructor_args():
    sig = inspect.signature(stateMachineDsl::MemberState.__init__)
    params = list(sig.parameters.keys())



def test_statemachinedsl::procedure_is_not_abstract():
    assert not inspect.isabstract(stateMachineDsl::Procedure)


def test_statemachinedsl::procedure_constructor_exists():
    assert callable(stateMachineDsl::Procedure.__init__)


def test_statemachinedsl::procedure_constructor_args():
    sig = inspect.signature(stateMachineDsl::Procedure.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachinedsl::procedure_has_name():
    assert hasattr(stateMachineDsl::Procedure, "name")
    descriptor = None
    for klass in stateMachineDsl::Procedure.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statemachinedsl::event_is_not_abstract():
    assert not inspect.isabstract(stateMachineDsl::Event)


def test_statemachinedsl::event_constructor_exists():
    assert callable(stateMachineDsl::Event.__init__)


def test_statemachinedsl::event_constructor_args():
    sig = inspect.signature(stateMachineDsl::Event.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachinedsl::event_has_name():
    assert hasattr(stateMachineDsl::Event, "name")
    descriptor = None
    for klass in stateMachineDsl::Event.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statemachinedsl::extdeclaration_is_not_abstract():
    assert not inspect.isabstract(stateMachineDsl::ExtDeclaration)


def test_statemachinedsl::extdeclaration_constructor_exists():
    assert callable(stateMachineDsl::ExtDeclaration.__init__)


def test_statemachinedsl::extdeclaration_constructor_args():
    sig = inspect.signature(stateMachineDsl::ExtDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachinedsl::extdeclaration_has_name():
    assert hasattr(stateMachineDsl::ExtDeclaration, "name")
    descriptor = None
    for klass in stateMachineDsl::ExtDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statemachinedsl::variable_is_not_abstract():
    assert not inspect.isabstract(stateMachineDsl::Variable)


def test_statemachinedsl::variable_constructor_exists():
    assert callable(stateMachineDsl::Variable.__init__)


def test_statemachinedsl::variable_constructor_args():
    sig = inspect.signature(stateMachineDsl::Variable.__init__)
    params = list(sig.parameters.keys())



def test_statemachinedsl::state_is_not_abstract():
    assert not inspect.isabstract(stateMachineDsl::State)


def test_statemachinedsl::state_constructor_exists():
    assert callable(stateMachineDsl::State.__init__)


def test_statemachinedsl::state_constructor_args():
    sig = inspect.signature(stateMachineDsl::State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachinedsl::state_has_name():
    assert hasattr(stateMachineDsl::State, "name")
    descriptor = None
    for klass in stateMachineDsl::State.__mro__:
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
stateMachineDsl::SetAction_strategy = st.builds(
    stateMachineDsl::SetAction,
)
stateMachineDsl::EObject_strategy = st.builds(
    stateMachineDsl::EObject,
)
ChangeAction_strategy = st.builds(
    ChangeAction,
)
stateMachineDsl::DecrementAction_strategy = st.builds(
    stateMachineDsl::DecrementAction,
)
stateMachineDsl::ResetAction_strategy = st.builds(
    stateMachineDsl::ResetAction,
)
stateMachineDsl::IncrementAction_strategy = st.builds(
    stateMachineDsl::IncrementAction,
)
stateMachineDsl::ProcedureUse_strategy = st.builds(
    stateMachineDsl::ProcedureUse,
)
Expression_strategy = st.builds(
    Expression,
)
stateMachineDsl::Parenthesis_strategy = st.builds(
    stateMachineDsl::Parenthesis,
)
stateMachineDsl::And_strategy = st.builds(
    stateMachineDsl::And,
)
stateMachineDsl::MinusCond_strategy = st.builds(
    stateMachineDsl::MinusCond,
)
stateMachineDsl::Or_strategy = st.builds(
    stateMachineDsl::Or,
)
stateMachineDsl::MulOrDiv_strategy = st.builds(
    stateMachineDsl::MulOrDiv,
    op=
        safe_text
)
stateMachineDsl::BoolExp_strategy = st.builds(
    stateMachineDsl::BoolExp,
    value=
        safe_text
)
stateMachineDsl::Not_strategy = st.builds(
    stateMachineDsl::Not,
)
stateMachineDsl::Equality_strategy = st.builds(
    stateMachineDsl::Equality,
    op=
        safe_text
)
stateMachineDsl::PlusCond_strategy = st.builds(
    stateMachineDsl::PlusCond,
)
stateMachineDsl::Comparison_strategy = st.builds(
    stateMachineDsl::Comparison,
    op=
        safe_text
)
stateMachineDsl::DoubleExp_strategy = st.builds(
    stateMachineDsl::DoubleExp,
    negative=
        safe_text,
    number=
        st.integers(),
    decimal=
        st.integers()
)
stateMachineDsl::NumberExp_strategy = st.builds(
    stateMachineDsl::NumberExp,
    negative=
        safe_text,
    value=
        st.integers()
)
stateMachineDsl::StringExp_strategy = st.builds(
    stateMachineDsl::StringExp,
    value=
        safe_text
)
stateMachineDsl::VarRef_strategy = st.builds(
    stateMachineDsl::VarRef,
)
stateMachineDsl::FunctionUse_strategy = st.builds(
    stateMachineDsl::FunctionUse,
)
stateMachineDsl::ChangeAction_strategy = st.builds(
    stateMachineDsl::ChangeAction,
)
stateMachineDsl::Expression_strategy = st.builds(
    stateMachineDsl::Expression,
)
stateMachineDsl::VarType_strategy = st.builds(
    stateMachineDsl::VarType,
    vt=
        safe_text
)
stateMachineDsl::VarParName_strategy = st.builds(
    stateMachineDsl::VarParName,
    name=
        safe_text
)
ExtDeclaration_strategy = st.builds(
    ExtDeclaration,
)
stateMachineDsl::Function_strategy = st.builds(
    stateMachineDsl::Function,
)
stateMachineDsl::Parameter_strategy = st.builds(
    stateMachineDsl::Parameter,
)
stateMachineDsl::Member_strategy = st.builds(
    stateMachineDsl::Member,
)
stateMachineDsl::ParameterFunction_strategy = st.builds(
    stateMachineDsl::ParameterFunction,
    name=
        safe_text
)
stateMachineDsl::Declaration_strategy = st.builds(
    stateMachineDsl::Declaration,
)
stateMachineDsl::StateMachine_strategy = st.builds(
    stateMachineDsl::StateMachine,
    name=
        safe_text
)
stateMachineDsl::Condition_strategy = st.builds(
    stateMachineDsl::Condition,
)
stateMachineDsl::CommandAction_strategy = st.builds(
    stateMachineDsl::CommandAction,
)
stateMachineDsl::Transition_strategy = st.builds(
    stateMachineDsl::Transition,
)
stateMachineDsl::Action_strategy = st.builds(
    stateMachineDsl::Action,
)
stateMachineDsl::MemberState_strategy = st.builds(
    stateMachineDsl::MemberState,
)
stateMachineDsl::Procedure_strategy = st.builds(
    stateMachineDsl::Procedure,
    name=
        safe_text
)
stateMachineDsl::Event_strategy = st.builds(
    stateMachineDsl::Event,
    name=
        safe_text
)
stateMachineDsl::ExtDeclaration_strategy = st.builds(
    stateMachineDsl::ExtDeclaration,
    name=
        safe_text
)
stateMachineDsl::Variable_strategy = st.builds(
    stateMachineDsl::Variable,
)
stateMachineDsl::State_strategy = st.builds(
    stateMachineDsl::State,
    name=
        safe_text
)

@given(instance=stateMachineDsl::SetAction_strategy)
@settings(max_examples=50)
def test_statemachinedsl::setaction_instantiation(instance):
    assert isinstance(instance, stateMachineDsl::SetAction)

@given(instance=stateMachineDsl::EObject_strategy)
@settings(max_examples=50)
def test_statemachinedsl::eobject_instantiation(instance):
    assert isinstance(instance, stateMachineDsl::EObject)

@given(instance=ChangeAction_strategy)
@settings(max_examples=50)
def test_changeaction_instantiation(instance):
    assert isinstance(instance, ChangeAction)

@given(instance=stateMachineDsl::DecrementAction_strategy)
@settings(max_examples=50)
def test_statemachinedsl::decrementaction_instantiation(instance):
    assert isinstance(instance, stateMachineDsl::DecrementAction)

@given(instance=stateMachineDsl::ResetAction_strategy)
@settings(max_examples=50)
def test_statemachinedsl::resetaction_instantiation(instance):
    assert isinstance(instance, stateMachineDsl::ResetAction)

@given(instance=stateMachineDsl::IncrementAction_strategy)
@settings(max_examples=50)
def test_statemachinedsl::incrementaction_instantiation(instance):
    assert isinstance(instance, stateMachineDsl::IncrementAction)

@given(instance=stateMachineDsl::ProcedureUse_strategy)
@settings(max_examples=50)
def test_statemachinedsl::procedureuse_instantiation(instance):
    assert isinstance(instance, stateMachineDsl::ProcedureUse)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=stateMachineDsl::Parenthesis_strategy)
@settings(max_examples=50)
def test_statemachinedsl::parenthesis_instantiation(instance):
    assert isinstance(instance, stateMachineDsl::Parenthesis)

@given(instance=stateMachineDsl::And_strategy)
@settings(max_examples=50)
def test_statemachinedsl::and_instantiation(instance):
    assert isinstance(instance, stateMachineDsl::And)

@given(instance=stateMachineDsl::MinusCond_strategy)
@settings(max_examples=50)
def test_statemachinedsl::minuscond_instantiation(instance):
    assert isinstance(instance, stateMachineDsl::MinusCond)

@given(instance=stateMachineDsl::Or_strategy)
@settings(max_examples=50)
def test_statemachinedsl::or_instantiation(instance):
    assert isinstance(instance, stateMachineDsl::Or)

@given(instance=stateMachineDsl::MulOrDiv_strategy)
@settings(max_examples=50)
def test_statemachinedsl::mulordiv_instantiation(instance):
    assert isinstance(instance, stateMachineDsl::MulOrDiv)

@given(instance=stateMachineDsl::MulOrDiv_strategy)
def test_statemachinedsl::mulordiv_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=stateMachineDsl::MulOrDiv_strategy)
def test_statemachinedsl::mulordiv_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=stateMachineDsl::BoolExp_strategy)
@settings(max_examples=50)
def test_statemachinedsl::boolexp_instantiation(instance):
    assert isinstance(instance, stateMachineDsl::BoolExp)

@given(instance=stateMachineDsl::BoolExp_strategy)
def test_statemachinedsl::boolexp_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=stateMachineDsl::BoolExp_strategy)
def test_statemachinedsl::boolexp_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=stateMachineDsl::Not_strategy)
@settings(max_examples=50)
def test_statemachinedsl::not_instantiation(instance):
    assert isinstance(instance, stateMachineDsl::Not)

@given(instance=stateMachineDsl::Equality_strategy)
@settings(max_examples=50)
def test_statemachinedsl::equality_instantiation(instance):
    assert isinstance(instance, stateMachineDsl::Equality)

@given(instance=stateMachineDsl::Equality_strategy)
def test_statemachinedsl::equality_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=stateMachineDsl::Equality_strategy)
def test_statemachinedsl::equality_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=stateMachineDsl::PlusCond_strategy)
@settings(max_examples=50)
def test_statemachinedsl::pluscond_instantiation(instance):
    assert isinstance(instance, stateMachineDsl::PlusCond)

@given(instance=stateMachineDsl::Comparison_strategy)
@settings(max_examples=50)
def test_statemachinedsl::comparison_instantiation(instance):
    assert isinstance(instance, stateMachineDsl::Comparison)

@given(instance=stateMachineDsl::Comparison_strategy)
def test_statemachinedsl::comparison_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=stateMachineDsl::Comparison_strategy)
def test_statemachinedsl::comparison_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=stateMachineDsl::DoubleExp_strategy)
@settings(max_examples=50)
def test_statemachinedsl::doubleexp_instantiation(instance):
    assert isinstance(instance, stateMachineDsl::DoubleExp)

@given(instance=stateMachineDsl::DoubleExp_strategy)
def test_statemachinedsl::doubleexp_negative_type(instance):
    assert isinstance(instance.negative, str)


@given(instance=stateMachineDsl::DoubleExp_strategy)
def test_statemachinedsl::doubleexp_negative_setter(instance):
    original = instance.negative
    instance.negative = original
    assert instance.negative == original

@given(instance=stateMachineDsl::DoubleExp_strategy)
def test_statemachinedsl::doubleexp_number_type(instance):
    assert isinstance(instance.number, int)


@given(instance=stateMachineDsl::DoubleExp_strategy)
def test_statemachinedsl::doubleexp_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original

@given(instance=stateMachineDsl::DoubleExp_strategy)
def test_statemachinedsl::doubleexp_decimal_type(instance):
    assert isinstance(instance.decimal, int)


@given(instance=stateMachineDsl::DoubleExp_strategy)
def test_statemachinedsl::doubleexp_decimal_setter(instance):
    original = instance.decimal
    instance.decimal = original
    assert instance.decimal == original

@given(instance=stateMachineDsl::NumberExp_strategy)
@settings(max_examples=50)
def test_statemachinedsl::numberexp_instantiation(instance):
    assert isinstance(instance, stateMachineDsl::NumberExp)

@given(instance=stateMachineDsl::NumberExp_strategy)
def test_statemachinedsl::numberexp_negative_type(instance):
    assert isinstance(instance.negative, str)


@given(instance=stateMachineDsl::NumberExp_strategy)
def test_statemachinedsl::numberexp_negative_setter(instance):
    original = instance.negative
    instance.negative = original
    assert instance.negative == original

@given(instance=stateMachineDsl::NumberExp_strategy)
def test_statemachinedsl::numberexp_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=stateMachineDsl::NumberExp_strategy)
def test_statemachinedsl::numberexp_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=stateMachineDsl::StringExp_strategy)
@settings(max_examples=50)
def test_statemachinedsl::stringexp_instantiation(instance):
    assert isinstance(instance, stateMachineDsl::StringExp)

@given(instance=stateMachineDsl::StringExp_strategy)
def test_statemachinedsl::stringexp_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=stateMachineDsl::StringExp_strategy)
def test_statemachinedsl::stringexp_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=stateMachineDsl::VarRef_strategy)
@settings(max_examples=50)
def test_statemachinedsl::varref_instantiation(instance):
    assert isinstance(instance, stateMachineDsl::VarRef)

@given(instance=stateMachineDsl::FunctionUse_strategy)
@settings(max_examples=50)
def test_statemachinedsl::functionuse_instantiation(instance):
    assert isinstance(instance, stateMachineDsl::FunctionUse)

@given(instance=stateMachineDsl::ChangeAction_strategy)
@settings(max_examples=50)
def test_statemachinedsl::changeaction_instantiation(instance):
    assert isinstance(instance, stateMachineDsl::ChangeAction)

@given(instance=stateMachineDsl::Expression_strategy)
@settings(max_examples=50)
def test_statemachinedsl::expression_instantiation(instance):
    assert isinstance(instance, stateMachineDsl::Expression)

@given(instance=stateMachineDsl::VarType_strategy)
@settings(max_examples=50)
def test_statemachinedsl::vartype_instantiation(instance):
    assert isinstance(instance, stateMachineDsl::VarType)

@given(instance=stateMachineDsl::VarType_strategy)
def test_statemachinedsl::vartype_vt_type(instance):
    assert isinstance(instance.vt, str)


@given(instance=stateMachineDsl::VarType_strategy)
def test_statemachinedsl::vartype_vt_setter(instance):
    original = instance.vt
    instance.vt = original
    assert instance.vt == original

@given(instance=stateMachineDsl::VarParName_strategy)
@settings(max_examples=50)
def test_statemachinedsl::varparname_instantiation(instance):
    assert isinstance(instance, stateMachineDsl::VarParName)

@given(instance=stateMachineDsl::VarParName_strategy)
def test_statemachinedsl::varparname_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=stateMachineDsl::VarParName_strategy)
def test_statemachinedsl::varparname_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ExtDeclaration_strategy)
@settings(max_examples=50)
def test_extdeclaration_instantiation(instance):
    assert isinstance(instance, ExtDeclaration)

@given(instance=stateMachineDsl::Function_strategy)
@settings(max_examples=50)
def test_statemachinedsl::function_instantiation(instance):
    assert isinstance(instance, stateMachineDsl::Function)

@given(instance=stateMachineDsl::Parameter_strategy)
@settings(max_examples=50)
def test_statemachinedsl::parameter_instantiation(instance):
    assert isinstance(instance, stateMachineDsl::Parameter)

@given(instance=stateMachineDsl::Member_strategy)
@settings(max_examples=50)
def test_statemachinedsl::member_instantiation(instance):
    assert isinstance(instance, stateMachineDsl::Member)

@given(instance=stateMachineDsl::ParameterFunction_strategy)
@settings(max_examples=50)
def test_statemachinedsl::parameterfunction_instantiation(instance):
    assert isinstance(instance, stateMachineDsl::ParameterFunction)

@given(instance=stateMachineDsl::ParameterFunction_strategy)
def test_statemachinedsl::parameterfunction_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=stateMachineDsl::ParameterFunction_strategy)
def test_statemachinedsl::parameterfunction_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=stateMachineDsl::Declaration_strategy)
@settings(max_examples=50)
def test_statemachinedsl::declaration_instantiation(instance):
    assert isinstance(instance, stateMachineDsl::Declaration)

@given(instance=stateMachineDsl::StateMachine_strategy)
@settings(max_examples=50)
def test_statemachinedsl::statemachine_instantiation(instance):
    assert isinstance(instance, stateMachineDsl::StateMachine)

@given(instance=stateMachineDsl::StateMachine_strategy)
def test_statemachinedsl::statemachine_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=stateMachineDsl::StateMachine_strategy)
def test_statemachinedsl::statemachine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=stateMachineDsl::Condition_strategy)
@settings(max_examples=50)
def test_statemachinedsl::condition_instantiation(instance):
    assert isinstance(instance, stateMachineDsl::Condition)

@given(instance=stateMachineDsl::CommandAction_strategy)
@settings(max_examples=50)
def test_statemachinedsl::commandaction_instantiation(instance):
    assert isinstance(instance, stateMachineDsl::CommandAction)

@given(instance=stateMachineDsl::Transition_strategy)
@settings(max_examples=50)
def test_statemachinedsl::transition_instantiation(instance):
    assert isinstance(instance, stateMachineDsl::Transition)

@given(instance=stateMachineDsl::Action_strategy)
@settings(max_examples=50)
def test_statemachinedsl::action_instantiation(instance):
    assert isinstance(instance, stateMachineDsl::Action)

@given(instance=stateMachineDsl::MemberState_strategy)
@settings(max_examples=50)
def test_statemachinedsl::memberstate_instantiation(instance):
    assert isinstance(instance, stateMachineDsl::MemberState)

@given(instance=stateMachineDsl::Procedure_strategy)
@settings(max_examples=50)
def test_statemachinedsl::procedure_instantiation(instance):
    assert isinstance(instance, stateMachineDsl::Procedure)

@given(instance=stateMachineDsl::Procedure_strategy)
def test_statemachinedsl::procedure_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=stateMachineDsl::Procedure_strategy)
def test_statemachinedsl::procedure_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=stateMachineDsl::Event_strategy)
@settings(max_examples=50)
def test_statemachinedsl::event_instantiation(instance):
    assert isinstance(instance, stateMachineDsl::Event)

@given(instance=stateMachineDsl::Event_strategy)
def test_statemachinedsl::event_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=stateMachineDsl::Event_strategy)
def test_statemachinedsl::event_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=stateMachineDsl::ExtDeclaration_strategy)
@settings(max_examples=50)
def test_statemachinedsl::extdeclaration_instantiation(instance):
    assert isinstance(instance, stateMachineDsl::ExtDeclaration)

@given(instance=stateMachineDsl::ExtDeclaration_strategy)
def test_statemachinedsl::extdeclaration_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=stateMachineDsl::ExtDeclaration_strategy)
def test_statemachinedsl::extdeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=stateMachineDsl::Variable_strategy)
@settings(max_examples=50)
def test_statemachinedsl::variable_instantiation(instance):
    assert isinstance(instance, stateMachineDsl::Variable)

@given(instance=stateMachineDsl::State_strategy)
@settings(max_examples=50)
def test_statemachinedsl::state_instantiation(instance):
    assert isinstance(instance, stateMachineDsl::State)

@given(instance=stateMachineDsl::State_strategy)
def test_statemachinedsl::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=stateMachineDsl::State_strategy)
def test_statemachinedsl::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
