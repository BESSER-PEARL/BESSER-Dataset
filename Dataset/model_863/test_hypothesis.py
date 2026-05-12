import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    BooleanExpression,
    gfsm_BooleanCompareExpression,
    gfsm_BooleanBinaryExpression,
    BooleanBinaryExpression,
    gfsm_BooleanAnd,
    gfsm_BooleanOr,
    BooleanCompareExpression,
    gfsm_BooleanGreaterThan,
    gfsm_BooleanEqual,
    IntOperation,
    gfsm_IntBlock,
    gfsm_IntVarAssign,
    State,
    gfsm_InitialState,
    gfsm_FinalState,
    gfsm_IntOperation,
    gfsm_State,
    IntBinaryExpression,
    gfsm_IntMult,
    gfsm_IntAdd,
    gfsm_IntExpression,
    IntExpression,
    gfsm_IntVarRef,
    gfsm_IntBinaryExpression,
    gfsm_IntNeg,
    gfsm_ConstExpr,
    gfsm_FSM,
    gfsm_BooleanExpression,
    gfsm_Transition,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_booleanexpression_is_not_abstract():
    assert not inspect.isabstract(BooleanExpression)


def test_booleanexpression_constructor_exists():
    assert callable(BooleanExpression.__init__)


def test_booleanexpression_constructor_args():
    sig = inspect.signature(BooleanExpression.__init__)
    params = list(sig.parameters.keys())



def test_gfsm_booleancompareexpression_is_not_abstract():
    assert not inspect.isabstract(gfsm_BooleanCompareExpression)


def test_gfsm_booleancompareexpression_constructor_exists():
    assert callable(gfsm_BooleanCompareExpression.__init__)


def test_gfsm_booleancompareexpression_constructor_args():
    sig = inspect.signature(gfsm_BooleanCompareExpression.__init__)
    params = list(sig.parameters.keys())



def test_gfsm_booleanbinaryexpression_is_not_abstract():
    assert not inspect.isabstract(gfsm_BooleanBinaryExpression)


def test_gfsm_booleanbinaryexpression_constructor_exists():
    assert callable(gfsm_BooleanBinaryExpression.__init__)


def test_gfsm_booleanbinaryexpression_constructor_args():
    sig = inspect.signature(gfsm_BooleanBinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_booleanbinaryexpression_is_not_abstract():
    assert not inspect.isabstract(BooleanBinaryExpression)


def test_booleanbinaryexpression_constructor_exists():
    assert callable(BooleanBinaryExpression.__init__)


def test_booleanbinaryexpression_constructor_args():
    sig = inspect.signature(BooleanBinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_gfsm_booleanand_is_not_abstract():
    assert not inspect.isabstract(gfsm_BooleanAnd)


def test_gfsm_booleanand_constructor_exists():
    assert callable(gfsm_BooleanAnd.__init__)


def test_gfsm_booleanand_constructor_args():
    sig = inspect.signature(gfsm_BooleanAnd.__init__)
    params = list(sig.parameters.keys())



def test_gfsm_booleanor_is_not_abstract():
    assert not inspect.isabstract(gfsm_BooleanOr)


def test_gfsm_booleanor_constructor_exists():
    assert callable(gfsm_BooleanOr.__init__)


def test_gfsm_booleanor_constructor_args():
    sig = inspect.signature(gfsm_BooleanOr.__init__)
    params = list(sig.parameters.keys())



def test_booleancompareexpression_is_not_abstract():
    assert not inspect.isabstract(BooleanCompareExpression)


def test_booleancompareexpression_constructor_exists():
    assert callable(BooleanCompareExpression.__init__)


def test_booleancompareexpression_constructor_args():
    sig = inspect.signature(BooleanCompareExpression.__init__)
    params = list(sig.parameters.keys())



def test_gfsm_booleangreaterthan_is_not_abstract():
    assert not inspect.isabstract(gfsm_BooleanGreaterThan)


def test_gfsm_booleangreaterthan_constructor_exists():
    assert callable(gfsm_BooleanGreaterThan.__init__)


def test_gfsm_booleangreaterthan_constructor_args():
    sig = inspect.signature(gfsm_BooleanGreaterThan.__init__)
    params = list(sig.parameters.keys())



def test_gfsm_booleanequal_is_not_abstract():
    assert not inspect.isabstract(gfsm_BooleanEqual)


def test_gfsm_booleanequal_constructor_exists():
    assert callable(gfsm_BooleanEqual.__init__)


def test_gfsm_booleanequal_constructor_args():
    sig = inspect.signature(gfsm_BooleanEqual.__init__)
    params = list(sig.parameters.keys())



def test_intoperation_is_not_abstract():
    assert not inspect.isabstract(IntOperation)


def test_intoperation_constructor_exists():
    assert callable(IntOperation.__init__)


def test_intoperation_constructor_args():
    sig = inspect.signature(IntOperation.__init__)
    params = list(sig.parameters.keys())



def test_gfsm_intblock_is_not_abstract():
    assert not inspect.isabstract(gfsm_IntBlock)


def test_gfsm_intblock_constructor_exists():
    assert callable(gfsm_IntBlock.__init__)


def test_gfsm_intblock_constructor_args():
    sig = inspect.signature(gfsm_IntBlock.__init__)
    params = list(sig.parameters.keys())



def test_gfsm_intvarassign_is_not_abstract():
    assert not inspect.isabstract(gfsm_IntVarAssign)


def test_gfsm_intvarassign_constructor_exists():
    assert callable(gfsm_IntVarAssign.__init__)


def test_gfsm_intvarassign_constructor_args():
    sig = inspect.signature(gfsm_IntVarAssign.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_gfsm_intvarassign_has_name():
    assert hasattr(gfsm_IntVarAssign, "name")
    descriptor = None
    for klass in gfsm_IntVarAssign.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_gfsm_initialstate_is_not_abstract():
    assert not inspect.isabstract(gfsm_InitialState)


def test_gfsm_initialstate_constructor_exists():
    assert callable(gfsm_InitialState.__init__)


def test_gfsm_initialstate_constructor_args():
    sig = inspect.signature(gfsm_InitialState.__init__)
    params = list(sig.parameters.keys())



def test_gfsm_finalstate_is_not_abstract():
    assert not inspect.isabstract(gfsm_FinalState)


def test_gfsm_finalstate_constructor_exists():
    assert callable(gfsm_FinalState.__init__)


def test_gfsm_finalstate_constructor_args():
    sig = inspect.signature(gfsm_FinalState.__init__)
    params = list(sig.parameters.keys())



def test_gfsm_intoperation_is_not_abstract():
    assert not inspect.isabstract(gfsm_IntOperation)


def test_gfsm_intoperation_constructor_exists():
    assert callable(gfsm_IntOperation.__init__)


def test_gfsm_intoperation_constructor_args():
    sig = inspect.signature(gfsm_IntOperation.__init__)
    params = list(sig.parameters.keys())



def test_gfsm_state_is_not_abstract():
    assert not inspect.isabstract(gfsm_State)


def test_gfsm_state_constructor_exists():
    assert callable(gfsm_State.__init__)


def test_gfsm_state_constructor_args():
    sig = inspect.signature(gfsm_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_gfsm_state_has_name():
    assert hasattr(gfsm_State, "name")
    descriptor = None
    for klass in gfsm_State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_intbinaryexpression_is_not_abstract():
    assert not inspect.isabstract(IntBinaryExpression)


def test_intbinaryexpression_constructor_exists():
    assert callable(IntBinaryExpression.__init__)


def test_intbinaryexpression_constructor_args():
    sig = inspect.signature(IntBinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_gfsm_intmult_is_not_abstract():
    assert not inspect.isabstract(gfsm_IntMult)


def test_gfsm_intmult_constructor_exists():
    assert callable(gfsm_IntMult.__init__)


def test_gfsm_intmult_constructor_args():
    sig = inspect.signature(gfsm_IntMult.__init__)
    params = list(sig.parameters.keys())



def test_gfsm_intadd_is_not_abstract():
    assert not inspect.isabstract(gfsm_IntAdd)


def test_gfsm_intadd_constructor_exists():
    assert callable(gfsm_IntAdd.__init__)


def test_gfsm_intadd_constructor_args():
    sig = inspect.signature(gfsm_IntAdd.__init__)
    params = list(sig.parameters.keys())



def test_gfsm_intexpression_is_not_abstract():
    assert not inspect.isabstract(gfsm_IntExpression)


def test_gfsm_intexpression_constructor_exists():
    assert callable(gfsm_IntExpression.__init__)


def test_gfsm_intexpression_constructor_args():
    sig = inspect.signature(gfsm_IntExpression.__init__)
    params = list(sig.parameters.keys())



def test_intexpression_is_not_abstract():
    assert not inspect.isabstract(IntExpression)


def test_intexpression_constructor_exists():
    assert callable(IntExpression.__init__)


def test_intexpression_constructor_args():
    sig = inspect.signature(IntExpression.__init__)
    params = list(sig.parameters.keys())



def test_gfsm_intvarref_is_not_abstract():
    assert not inspect.isabstract(gfsm_IntVarRef)


def test_gfsm_intvarref_constructor_exists():
    assert callable(gfsm_IntVarRef.__init__)


def test_gfsm_intvarref_constructor_args():
    sig = inspect.signature(gfsm_IntVarRef.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_gfsm_intvarref_has_name():
    assert hasattr(gfsm_IntVarRef, "name")
    descriptor = None
    for klass in gfsm_IntVarRef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_gfsm_intbinaryexpression_is_not_abstract():
    assert not inspect.isabstract(gfsm_IntBinaryExpression)


def test_gfsm_intbinaryexpression_constructor_exists():
    assert callable(gfsm_IntBinaryExpression.__init__)


def test_gfsm_intbinaryexpression_constructor_args():
    sig = inspect.signature(gfsm_IntBinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_gfsm_intneg_is_not_abstract():
    assert not inspect.isabstract(gfsm_IntNeg)


def test_gfsm_intneg_constructor_exists():
    assert callable(gfsm_IntNeg.__init__)


def test_gfsm_intneg_constructor_args():
    sig = inspect.signature(gfsm_IntNeg.__init__)
    params = list(sig.parameters.keys())



def test_gfsm_constexpr_is_not_abstract():
    assert not inspect.isabstract(gfsm_ConstExpr)


def test_gfsm_constexpr_constructor_exists():
    assert callable(gfsm_ConstExpr.__init__)


def test_gfsm_constexpr_constructor_args():
    sig = inspect.signature(gfsm_ConstExpr.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_gfsm_constexpr_has_value():
    assert hasattr(gfsm_ConstExpr, "value")
    descriptor = None
    for klass in gfsm_ConstExpr.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_gfsm_fsm_is_not_abstract():
    assert not inspect.isabstract(gfsm_FSM)


def test_gfsm_fsm_constructor_exists():
    assert callable(gfsm_FSM.__init__)


def test_gfsm_fsm_constructor_args():
    sig = inspect.signature(gfsm_FSM.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_gfsm_fsm_has_name():
    assert hasattr(gfsm_FSM, "name")
    descriptor = None
    for klass in gfsm_FSM.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_gfsm_booleanexpression_is_not_abstract():
    assert not inspect.isabstract(gfsm_BooleanExpression)


def test_gfsm_booleanexpression_constructor_exists():
    assert callable(gfsm_BooleanExpression.__init__)


def test_gfsm_booleanexpression_constructor_args():
    sig = inspect.signature(gfsm_BooleanExpression.__init__)
    params = list(sig.parameters.keys())



def test_gfsm_transition_is_not_abstract():
    assert not inspect.isabstract(gfsm_Transition)


def test_gfsm_transition_constructor_exists():
    assert callable(gfsm_Transition.__init__)


def test_gfsm_transition_constructor_args():
    sig = inspect.signature(gfsm_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "event" in params, "Missing parameter 'event'"

def test_gfsm_transition_has_event():
    assert hasattr(gfsm_Transition, "event")
    descriptor = None
    for klass in gfsm_Transition.__mro__:
        if "event" in klass.__dict__:
            descriptor = klass.__dict__["event"]
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
BooleanExpression_strategy = st.builds(
    BooleanExpression,
)
gfsm_BooleanCompareExpression_strategy = st.builds(
    gfsm_BooleanCompareExpression,
)
gfsm_BooleanBinaryExpression_strategy = st.builds(
    gfsm_BooleanBinaryExpression,
)
BooleanBinaryExpression_strategy = st.builds(
    BooleanBinaryExpression,
)
gfsm_BooleanAnd_strategy = st.builds(
    gfsm_BooleanAnd,
)
gfsm_BooleanOr_strategy = st.builds(
    gfsm_BooleanOr,
)
BooleanCompareExpression_strategy = st.builds(
    BooleanCompareExpression,
)
gfsm_BooleanGreaterThan_strategy = st.builds(
    gfsm_BooleanGreaterThan,
)
gfsm_BooleanEqual_strategy = st.builds(
    gfsm_BooleanEqual,
)
IntOperation_strategy = st.builds(
    IntOperation,
)
gfsm_IntBlock_strategy = st.builds(
    gfsm_IntBlock,
)
gfsm_IntVarAssign_strategy = st.builds(
    gfsm_IntVarAssign,
    name=
        safe_text
)
State_strategy = st.builds(
    State,
)
gfsm_InitialState_strategy = st.builds(
    gfsm_InitialState,
)
gfsm_FinalState_strategy = st.builds(
    gfsm_FinalState,
)
gfsm_IntOperation_strategy = st.builds(
    gfsm_IntOperation,
)
gfsm_State_strategy = st.builds(
    gfsm_State,
    name=
        safe_text
)
IntBinaryExpression_strategy = st.builds(
    IntBinaryExpression,
)
gfsm_IntMult_strategy = st.builds(
    gfsm_IntMult,
)
gfsm_IntAdd_strategy = st.builds(
    gfsm_IntAdd,
)
gfsm_IntExpression_strategy = st.builds(
    gfsm_IntExpression,
)
IntExpression_strategy = st.builds(
    IntExpression,
)
gfsm_IntVarRef_strategy = st.builds(
    gfsm_IntVarRef,
    name=
        safe_text
)
gfsm_IntBinaryExpression_strategy = st.builds(
    gfsm_IntBinaryExpression,
)
gfsm_IntNeg_strategy = st.builds(
    gfsm_IntNeg,
)
gfsm_ConstExpr_strategy = st.builds(
    gfsm_ConstExpr,
    value=
        st.integers()
)
gfsm_FSM_strategy = st.builds(
    gfsm_FSM,
    name=
        safe_text
)
gfsm_BooleanExpression_strategy = st.builds(
    gfsm_BooleanExpression,
)
gfsm_Transition_strategy = st.builds(
    gfsm_Transition,
    event=
        safe_text
)

@given(instance=BooleanExpression_strategy)
@settings(max_examples=50)
def test_booleanexpression_instantiation(instance):
    assert isinstance(instance, BooleanExpression)

@given(instance=gfsm_BooleanCompareExpression_strategy)
@settings(max_examples=50)
def test_gfsm_booleancompareexpression_instantiation(instance):
    assert isinstance(instance, gfsm_BooleanCompareExpression)

@given(instance=gfsm_BooleanBinaryExpression_strategy)
@settings(max_examples=50)
def test_gfsm_booleanbinaryexpression_instantiation(instance):
    assert isinstance(instance, gfsm_BooleanBinaryExpression)

@given(instance=BooleanBinaryExpression_strategy)
@settings(max_examples=50)
def test_booleanbinaryexpression_instantiation(instance):
    assert isinstance(instance, BooleanBinaryExpression)

@given(instance=gfsm_BooleanAnd_strategy)
@settings(max_examples=50)
def test_gfsm_booleanand_instantiation(instance):
    assert isinstance(instance, gfsm_BooleanAnd)

@given(instance=gfsm_BooleanOr_strategy)
@settings(max_examples=50)
def test_gfsm_booleanor_instantiation(instance):
    assert isinstance(instance, gfsm_BooleanOr)

@given(instance=BooleanCompareExpression_strategy)
@settings(max_examples=50)
def test_booleancompareexpression_instantiation(instance):
    assert isinstance(instance, BooleanCompareExpression)

@given(instance=gfsm_BooleanGreaterThan_strategy)
@settings(max_examples=50)
def test_gfsm_booleangreaterthan_instantiation(instance):
    assert isinstance(instance, gfsm_BooleanGreaterThan)

@given(instance=gfsm_BooleanEqual_strategy)
@settings(max_examples=50)
def test_gfsm_booleanequal_instantiation(instance):
    assert isinstance(instance, gfsm_BooleanEqual)

@given(instance=IntOperation_strategy)
@settings(max_examples=50)
def test_intoperation_instantiation(instance):
    assert isinstance(instance, IntOperation)

@given(instance=gfsm_IntBlock_strategy)
@settings(max_examples=50)
def test_gfsm_intblock_instantiation(instance):
    assert isinstance(instance, gfsm_IntBlock)

@given(instance=gfsm_IntVarAssign_strategy)
@settings(max_examples=50)
def test_gfsm_intvarassign_instantiation(instance):
    assert isinstance(instance, gfsm_IntVarAssign)



@given(instance=gfsm_IntVarAssign_strategy)
def test_gfsm_intvarassign_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=gfsm_InitialState_strategy)
@settings(max_examples=50)
def test_gfsm_initialstate_instantiation(instance):
    assert isinstance(instance, gfsm_InitialState)

@given(instance=gfsm_FinalState_strategy)
@settings(max_examples=50)
def test_gfsm_finalstate_instantiation(instance):
    assert isinstance(instance, gfsm_FinalState)

@given(instance=gfsm_IntOperation_strategy)
@settings(max_examples=50)
def test_gfsm_intoperation_instantiation(instance):
    assert isinstance(instance, gfsm_IntOperation)

@given(instance=gfsm_State_strategy)
@settings(max_examples=50)
def test_gfsm_state_instantiation(instance):
    assert isinstance(instance, gfsm_State)



@given(instance=gfsm_State_strategy)
def test_gfsm_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=IntBinaryExpression_strategy)
@settings(max_examples=50)
def test_intbinaryexpression_instantiation(instance):
    assert isinstance(instance, IntBinaryExpression)

@given(instance=gfsm_IntMult_strategy)
@settings(max_examples=50)
def test_gfsm_intmult_instantiation(instance):
    assert isinstance(instance, gfsm_IntMult)

@given(instance=gfsm_IntAdd_strategy)
@settings(max_examples=50)
def test_gfsm_intadd_instantiation(instance):
    assert isinstance(instance, gfsm_IntAdd)

@given(instance=gfsm_IntExpression_strategy)
@settings(max_examples=50)
def test_gfsm_intexpression_instantiation(instance):
    assert isinstance(instance, gfsm_IntExpression)

@given(instance=IntExpression_strategy)
@settings(max_examples=50)
def test_intexpression_instantiation(instance):
    assert isinstance(instance, IntExpression)

@given(instance=gfsm_IntVarRef_strategy)
@settings(max_examples=50)
def test_gfsm_intvarref_instantiation(instance):
    assert isinstance(instance, gfsm_IntVarRef)



@given(instance=gfsm_IntVarRef_strategy)
def test_gfsm_intvarref_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=gfsm_IntBinaryExpression_strategy)
@settings(max_examples=50)
def test_gfsm_intbinaryexpression_instantiation(instance):
    assert isinstance(instance, gfsm_IntBinaryExpression)

@given(instance=gfsm_IntNeg_strategy)
@settings(max_examples=50)
def test_gfsm_intneg_instantiation(instance):
    assert isinstance(instance, gfsm_IntNeg)

@given(instance=gfsm_ConstExpr_strategy)
@settings(max_examples=50)
def test_gfsm_constexpr_instantiation(instance):
    assert isinstance(instance, gfsm_ConstExpr)



@given(instance=gfsm_ConstExpr_strategy)
def test_gfsm_constexpr_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=gfsm_FSM_strategy)
@settings(max_examples=50)
def test_gfsm_fsm_instantiation(instance):
    assert isinstance(instance, gfsm_FSM)



@given(instance=gfsm_FSM_strategy)
def test_gfsm_fsm_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=gfsm_BooleanExpression_strategy)
@settings(max_examples=50)
def test_gfsm_booleanexpression_instantiation(instance):
    assert isinstance(instance, gfsm_BooleanExpression)

@given(instance=gfsm_Transition_strategy)
@settings(max_examples=50)
def test_gfsm_transition_instantiation(instance):
    assert isinstance(instance, gfsm_Transition)



@given(instance=gfsm_Transition_strategy)
def test_gfsm_transition_event_setter(instance):
    original = instance.event
    instance.event = original
    assert instance.event == original
