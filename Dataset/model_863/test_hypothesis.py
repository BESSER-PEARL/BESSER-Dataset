import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    State,
    gfsm::InitialState,
    gfsm::FinalState,
    gfsm::IntOperation,
    gfsm::State,
    IntBinaryExpression,
    gfsm::IntMult,
    gfsm::IntAdd,
    gfsm::IntExpression,
    IntExpression,
    gfsm::IntVarRef,
    gfsm::IntBinaryExpression,
    gfsm::ConstExpr,
    gfsm::IntNeg,
    gfsm::FSM,
    gfsm::BooleanExpression,
    gfsm::Transition,
    BooleanExpression,
    gfsm::BooleanCompareExpression,
    gfsm::BooleanBinaryExpression,
    BooleanBinaryExpression,
    gfsm::BooleanAnd,
    gfsm::BooleanOr,
    BooleanCompareExpression,
    gfsm::BooleanGreaterThan,
    gfsm::BooleanEqual,
    IntOperation,
    gfsm::IntBlock,
    gfsm::IntVarAssign,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_gfsm::initialstate_is_not_abstract():
    assert not inspect.isabstract(gfsm::InitialState)


def test_gfsm::initialstate_constructor_exists():
    assert callable(gfsm::InitialState.__init__)


def test_gfsm::initialstate_constructor_args():
    sig = inspect.signature(gfsm::InitialState.__init__)
    params = list(sig.parameters.keys())



def test_gfsm::finalstate_is_not_abstract():
    assert not inspect.isabstract(gfsm::FinalState)


def test_gfsm::finalstate_constructor_exists():
    assert callable(gfsm::FinalState.__init__)


def test_gfsm::finalstate_constructor_args():
    sig = inspect.signature(gfsm::FinalState.__init__)
    params = list(sig.parameters.keys())



def test_gfsm::intoperation_is_not_abstract():
    assert not inspect.isabstract(gfsm::IntOperation)


def test_gfsm::intoperation_constructor_exists():
    assert callable(gfsm::IntOperation.__init__)


def test_gfsm::intoperation_constructor_args():
    sig = inspect.signature(gfsm::IntOperation.__init__)
    params = list(sig.parameters.keys())



def test_gfsm::state_is_not_abstract():
    assert not inspect.isabstract(gfsm::State)


def test_gfsm::state_constructor_exists():
    assert callable(gfsm::State.__init__)


def test_gfsm::state_constructor_args():
    sig = inspect.signature(gfsm::State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_gfsm::state_has_name():
    assert hasattr(gfsm::State, "name")
    descriptor = None
    for klass in gfsm::State.__mro__:
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



def test_gfsm::intmult_is_not_abstract():
    assert not inspect.isabstract(gfsm::IntMult)


def test_gfsm::intmult_constructor_exists():
    assert callable(gfsm::IntMult.__init__)


def test_gfsm::intmult_constructor_args():
    sig = inspect.signature(gfsm::IntMult.__init__)
    params = list(sig.parameters.keys())



def test_gfsm::intadd_is_not_abstract():
    assert not inspect.isabstract(gfsm::IntAdd)


def test_gfsm::intadd_constructor_exists():
    assert callable(gfsm::IntAdd.__init__)


def test_gfsm::intadd_constructor_args():
    sig = inspect.signature(gfsm::IntAdd.__init__)
    params = list(sig.parameters.keys())



def test_gfsm::intexpression_is_not_abstract():
    assert not inspect.isabstract(gfsm::IntExpression)


def test_gfsm::intexpression_constructor_exists():
    assert callable(gfsm::IntExpression.__init__)


def test_gfsm::intexpression_constructor_args():
    sig = inspect.signature(gfsm::IntExpression.__init__)
    params = list(sig.parameters.keys())



def test_intexpression_is_not_abstract():
    assert not inspect.isabstract(IntExpression)


def test_intexpression_constructor_exists():
    assert callable(IntExpression.__init__)


def test_intexpression_constructor_args():
    sig = inspect.signature(IntExpression.__init__)
    params = list(sig.parameters.keys())



def test_gfsm::intvarref_is_not_abstract():
    assert not inspect.isabstract(gfsm::IntVarRef)


def test_gfsm::intvarref_constructor_exists():
    assert callable(gfsm::IntVarRef.__init__)


def test_gfsm::intvarref_constructor_args():
    sig = inspect.signature(gfsm::IntVarRef.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_gfsm::intvarref_has_name():
    assert hasattr(gfsm::IntVarRef, "name")
    descriptor = None
    for klass in gfsm::IntVarRef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_gfsm::intbinaryexpression_is_not_abstract():
    assert not inspect.isabstract(gfsm::IntBinaryExpression)


def test_gfsm::intbinaryexpression_constructor_exists():
    assert callable(gfsm::IntBinaryExpression.__init__)


def test_gfsm::intbinaryexpression_constructor_args():
    sig = inspect.signature(gfsm::IntBinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_gfsm::constexpr_is_not_abstract():
    assert not inspect.isabstract(gfsm::ConstExpr)


def test_gfsm::constexpr_constructor_exists():
    assert callable(gfsm::ConstExpr.__init__)


def test_gfsm::constexpr_constructor_args():
    sig = inspect.signature(gfsm::ConstExpr.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_gfsm::constexpr_has_value():
    assert hasattr(gfsm::ConstExpr, "value")
    descriptor = None
    for klass in gfsm::ConstExpr.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_gfsm::intneg_is_not_abstract():
    assert not inspect.isabstract(gfsm::IntNeg)


def test_gfsm::intneg_constructor_exists():
    assert callable(gfsm::IntNeg.__init__)


def test_gfsm::intneg_constructor_args():
    sig = inspect.signature(gfsm::IntNeg.__init__)
    params = list(sig.parameters.keys())



def test_gfsm::fsm_is_not_abstract():
    assert not inspect.isabstract(gfsm::FSM)


def test_gfsm::fsm_constructor_exists():
    assert callable(gfsm::FSM.__init__)


def test_gfsm::fsm_constructor_args():
    sig = inspect.signature(gfsm::FSM.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_gfsm::fsm_has_name():
    assert hasattr(gfsm::FSM, "name")
    descriptor = None
    for klass in gfsm::FSM.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_gfsm::booleanexpression_is_not_abstract():
    assert not inspect.isabstract(gfsm::BooleanExpression)


def test_gfsm::booleanexpression_constructor_exists():
    assert callable(gfsm::BooleanExpression.__init__)


def test_gfsm::booleanexpression_constructor_args():
    sig = inspect.signature(gfsm::BooleanExpression.__init__)
    params = list(sig.parameters.keys())



def test_gfsm::transition_is_not_abstract():
    assert not inspect.isabstract(gfsm::Transition)


def test_gfsm::transition_constructor_exists():
    assert callable(gfsm::Transition.__init__)


def test_gfsm::transition_constructor_args():
    sig = inspect.signature(gfsm::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "event" in params, "Missing parameter 'event'"

def test_gfsm::transition_has_event():
    assert hasattr(gfsm::Transition, "event")
    descriptor = None
    for klass in gfsm::Transition.__mro__:
        if "event" in klass.__dict__:
            descriptor = klass.__dict__["event"]
            break
    assert isinstance(descriptor, property)



def test_booleanexpression_is_not_abstract():
    assert not inspect.isabstract(BooleanExpression)


def test_booleanexpression_constructor_exists():
    assert callable(BooleanExpression.__init__)


def test_booleanexpression_constructor_args():
    sig = inspect.signature(BooleanExpression.__init__)
    params = list(sig.parameters.keys())



def test_gfsm::booleancompareexpression_is_not_abstract():
    assert not inspect.isabstract(gfsm::BooleanCompareExpression)


def test_gfsm::booleancompareexpression_constructor_exists():
    assert callable(gfsm::BooleanCompareExpression.__init__)


def test_gfsm::booleancompareexpression_constructor_args():
    sig = inspect.signature(gfsm::BooleanCompareExpression.__init__)
    params = list(sig.parameters.keys())



def test_gfsm::booleanbinaryexpression_is_not_abstract():
    assert not inspect.isabstract(gfsm::BooleanBinaryExpression)


def test_gfsm::booleanbinaryexpression_constructor_exists():
    assert callable(gfsm::BooleanBinaryExpression.__init__)


def test_gfsm::booleanbinaryexpression_constructor_args():
    sig = inspect.signature(gfsm::BooleanBinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_booleanbinaryexpression_is_not_abstract():
    assert not inspect.isabstract(BooleanBinaryExpression)


def test_booleanbinaryexpression_constructor_exists():
    assert callable(BooleanBinaryExpression.__init__)


def test_booleanbinaryexpression_constructor_args():
    sig = inspect.signature(BooleanBinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_gfsm::booleanand_is_not_abstract():
    assert not inspect.isabstract(gfsm::BooleanAnd)


def test_gfsm::booleanand_constructor_exists():
    assert callable(gfsm::BooleanAnd.__init__)


def test_gfsm::booleanand_constructor_args():
    sig = inspect.signature(gfsm::BooleanAnd.__init__)
    params = list(sig.parameters.keys())



def test_gfsm::booleanor_is_not_abstract():
    assert not inspect.isabstract(gfsm::BooleanOr)


def test_gfsm::booleanor_constructor_exists():
    assert callable(gfsm::BooleanOr.__init__)


def test_gfsm::booleanor_constructor_args():
    sig = inspect.signature(gfsm::BooleanOr.__init__)
    params = list(sig.parameters.keys())



def test_booleancompareexpression_is_not_abstract():
    assert not inspect.isabstract(BooleanCompareExpression)


def test_booleancompareexpression_constructor_exists():
    assert callable(BooleanCompareExpression.__init__)


def test_booleancompareexpression_constructor_args():
    sig = inspect.signature(BooleanCompareExpression.__init__)
    params = list(sig.parameters.keys())



def test_gfsm::booleangreaterthan_is_not_abstract():
    assert not inspect.isabstract(gfsm::BooleanGreaterThan)


def test_gfsm::booleangreaterthan_constructor_exists():
    assert callable(gfsm::BooleanGreaterThan.__init__)


def test_gfsm::booleangreaterthan_constructor_args():
    sig = inspect.signature(gfsm::BooleanGreaterThan.__init__)
    params = list(sig.parameters.keys())



def test_gfsm::booleanequal_is_not_abstract():
    assert not inspect.isabstract(gfsm::BooleanEqual)


def test_gfsm::booleanequal_constructor_exists():
    assert callable(gfsm::BooleanEqual.__init__)


def test_gfsm::booleanequal_constructor_args():
    sig = inspect.signature(gfsm::BooleanEqual.__init__)
    params = list(sig.parameters.keys())



def test_intoperation_is_not_abstract():
    assert not inspect.isabstract(IntOperation)


def test_intoperation_constructor_exists():
    assert callable(IntOperation.__init__)


def test_intoperation_constructor_args():
    sig = inspect.signature(IntOperation.__init__)
    params = list(sig.parameters.keys())



def test_gfsm::intblock_is_not_abstract():
    assert not inspect.isabstract(gfsm::IntBlock)


def test_gfsm::intblock_constructor_exists():
    assert callable(gfsm::IntBlock.__init__)


def test_gfsm::intblock_constructor_args():
    sig = inspect.signature(gfsm::IntBlock.__init__)
    params = list(sig.parameters.keys())



def test_gfsm::intvarassign_is_not_abstract():
    assert not inspect.isabstract(gfsm::IntVarAssign)


def test_gfsm::intvarassign_constructor_exists():
    assert callable(gfsm::IntVarAssign.__init__)


def test_gfsm::intvarassign_constructor_args():
    sig = inspect.signature(gfsm::IntVarAssign.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_gfsm::intvarassign_has_name():
    assert hasattr(gfsm::IntVarAssign, "name")
    descriptor = None
    for klass in gfsm::IntVarAssign.__mro__:
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
State_strategy = st.builds(
    State,
)
gfsm::InitialState_strategy = st.builds(
    gfsm::InitialState,
)
gfsm::FinalState_strategy = st.builds(
    gfsm::FinalState,
)
gfsm::IntOperation_strategy = st.builds(
    gfsm::IntOperation,
)
gfsm::State_strategy = st.builds(
    gfsm::State,
    name=
        safe_text
)
IntBinaryExpression_strategy = st.builds(
    IntBinaryExpression,
)
gfsm::IntMult_strategy = st.builds(
    gfsm::IntMult,
)
gfsm::IntAdd_strategy = st.builds(
    gfsm::IntAdd,
)
gfsm::IntExpression_strategy = st.builds(
    gfsm::IntExpression,
)
IntExpression_strategy = st.builds(
    IntExpression,
)
gfsm::IntVarRef_strategy = st.builds(
    gfsm::IntVarRef,
    name=
        safe_text
)
gfsm::IntBinaryExpression_strategy = st.builds(
    gfsm::IntBinaryExpression,
)
gfsm::ConstExpr_strategy = st.builds(
    gfsm::ConstExpr,
    value=
        st.integers()
)
gfsm::IntNeg_strategy = st.builds(
    gfsm::IntNeg,
)
gfsm::FSM_strategy = st.builds(
    gfsm::FSM,
    name=
        safe_text
)
gfsm::BooleanExpression_strategy = st.builds(
    gfsm::BooleanExpression,
)
gfsm::Transition_strategy = st.builds(
    gfsm::Transition,
    event=
        safe_text
)
BooleanExpression_strategy = st.builds(
    BooleanExpression,
)
gfsm::BooleanCompareExpression_strategy = st.builds(
    gfsm::BooleanCompareExpression,
)
gfsm::BooleanBinaryExpression_strategy = st.builds(
    gfsm::BooleanBinaryExpression,
)
BooleanBinaryExpression_strategy = st.builds(
    BooleanBinaryExpression,
)
gfsm::BooleanAnd_strategy = st.builds(
    gfsm::BooleanAnd,
)
gfsm::BooleanOr_strategy = st.builds(
    gfsm::BooleanOr,
)
BooleanCompareExpression_strategy = st.builds(
    BooleanCompareExpression,
)
gfsm::BooleanGreaterThan_strategy = st.builds(
    gfsm::BooleanGreaterThan,
)
gfsm::BooleanEqual_strategy = st.builds(
    gfsm::BooleanEqual,
)
IntOperation_strategy = st.builds(
    IntOperation,
)
gfsm::IntBlock_strategy = st.builds(
    gfsm::IntBlock,
)
gfsm::IntVarAssign_strategy = st.builds(
    gfsm::IntVarAssign,
    name=
        safe_text
)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=gfsm::InitialState_strategy)
@settings(max_examples=50)
def test_gfsm::initialstate_instantiation(instance):
    assert isinstance(instance, gfsm::InitialState)

@given(instance=gfsm::FinalState_strategy)
@settings(max_examples=50)
def test_gfsm::finalstate_instantiation(instance):
    assert isinstance(instance, gfsm::FinalState)

@given(instance=gfsm::IntOperation_strategy)
@settings(max_examples=50)
def test_gfsm::intoperation_instantiation(instance):
    assert isinstance(instance, gfsm::IntOperation)

@given(instance=gfsm::State_strategy)
@settings(max_examples=50)
def test_gfsm::state_instantiation(instance):
    assert isinstance(instance, gfsm::State)

@given(instance=gfsm::State_strategy)
def test_gfsm::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=gfsm::State_strategy)
def test_gfsm::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=IntBinaryExpression_strategy)
@settings(max_examples=50)
def test_intbinaryexpression_instantiation(instance):
    assert isinstance(instance, IntBinaryExpression)

@given(instance=gfsm::IntMult_strategy)
@settings(max_examples=50)
def test_gfsm::intmult_instantiation(instance):
    assert isinstance(instance, gfsm::IntMult)

@given(instance=gfsm::IntAdd_strategy)
@settings(max_examples=50)
def test_gfsm::intadd_instantiation(instance):
    assert isinstance(instance, gfsm::IntAdd)

@given(instance=gfsm::IntExpression_strategy)
@settings(max_examples=50)
def test_gfsm::intexpression_instantiation(instance):
    assert isinstance(instance, gfsm::IntExpression)

@given(instance=IntExpression_strategy)
@settings(max_examples=50)
def test_intexpression_instantiation(instance):
    assert isinstance(instance, IntExpression)

@given(instance=gfsm::IntVarRef_strategy)
@settings(max_examples=50)
def test_gfsm::intvarref_instantiation(instance):
    assert isinstance(instance, gfsm::IntVarRef)

@given(instance=gfsm::IntVarRef_strategy)
def test_gfsm::intvarref_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=gfsm::IntVarRef_strategy)
def test_gfsm::intvarref_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=gfsm::IntBinaryExpression_strategy)
@settings(max_examples=50)
def test_gfsm::intbinaryexpression_instantiation(instance):
    assert isinstance(instance, gfsm::IntBinaryExpression)

@given(instance=gfsm::ConstExpr_strategy)
@settings(max_examples=50)
def test_gfsm::constexpr_instantiation(instance):
    assert isinstance(instance, gfsm::ConstExpr)

@given(instance=gfsm::ConstExpr_strategy)
def test_gfsm::constexpr_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=gfsm::ConstExpr_strategy)
def test_gfsm::constexpr_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=gfsm::IntNeg_strategy)
@settings(max_examples=50)
def test_gfsm::intneg_instantiation(instance):
    assert isinstance(instance, gfsm::IntNeg)

@given(instance=gfsm::FSM_strategy)
@settings(max_examples=50)
def test_gfsm::fsm_instantiation(instance):
    assert isinstance(instance, gfsm::FSM)

@given(instance=gfsm::FSM_strategy)
def test_gfsm::fsm_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=gfsm::FSM_strategy)
def test_gfsm::fsm_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=gfsm::BooleanExpression_strategy)
@settings(max_examples=50)
def test_gfsm::booleanexpression_instantiation(instance):
    assert isinstance(instance, gfsm::BooleanExpression)

@given(instance=gfsm::Transition_strategy)
@settings(max_examples=50)
def test_gfsm::transition_instantiation(instance):
    assert isinstance(instance, gfsm::Transition)

@given(instance=gfsm::Transition_strategy)
def test_gfsm::transition_event_type(instance):
    assert isinstance(instance.event, str)


@given(instance=gfsm::Transition_strategy)
def test_gfsm::transition_event_setter(instance):
    original = instance.event
    instance.event = original
    assert instance.event == original

@given(instance=BooleanExpression_strategy)
@settings(max_examples=50)
def test_booleanexpression_instantiation(instance):
    assert isinstance(instance, BooleanExpression)

@given(instance=gfsm::BooleanCompareExpression_strategy)
@settings(max_examples=50)
def test_gfsm::booleancompareexpression_instantiation(instance):
    assert isinstance(instance, gfsm::BooleanCompareExpression)

@given(instance=gfsm::BooleanBinaryExpression_strategy)
@settings(max_examples=50)
def test_gfsm::booleanbinaryexpression_instantiation(instance):
    assert isinstance(instance, gfsm::BooleanBinaryExpression)

@given(instance=BooleanBinaryExpression_strategy)
@settings(max_examples=50)
def test_booleanbinaryexpression_instantiation(instance):
    assert isinstance(instance, BooleanBinaryExpression)

@given(instance=gfsm::BooleanAnd_strategy)
@settings(max_examples=50)
def test_gfsm::booleanand_instantiation(instance):
    assert isinstance(instance, gfsm::BooleanAnd)

@given(instance=gfsm::BooleanOr_strategy)
@settings(max_examples=50)
def test_gfsm::booleanor_instantiation(instance):
    assert isinstance(instance, gfsm::BooleanOr)

@given(instance=BooleanCompareExpression_strategy)
@settings(max_examples=50)
def test_booleancompareexpression_instantiation(instance):
    assert isinstance(instance, BooleanCompareExpression)

@given(instance=gfsm::BooleanGreaterThan_strategy)
@settings(max_examples=50)
def test_gfsm::booleangreaterthan_instantiation(instance):
    assert isinstance(instance, gfsm::BooleanGreaterThan)

@given(instance=gfsm::BooleanEqual_strategy)
@settings(max_examples=50)
def test_gfsm::booleanequal_instantiation(instance):
    assert isinstance(instance, gfsm::BooleanEqual)

@given(instance=IntOperation_strategy)
@settings(max_examples=50)
def test_intoperation_instantiation(instance):
    assert isinstance(instance, IntOperation)

@given(instance=gfsm::IntBlock_strategy)
@settings(max_examples=50)
def test_gfsm::intblock_instantiation(instance):
    assert isinstance(instance, gfsm::IntBlock)

@given(instance=gfsm::IntVarAssign_strategy)
@settings(max_examples=50)
def test_gfsm::intvarassign_instantiation(instance):
    assert isinstance(instance, gfsm::IntVarAssign)

@given(instance=gfsm::IntVarAssign_strategy)
def test_gfsm::intvarassign_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=gfsm::IntVarAssign_strategy)
def test_gfsm::intvarassign_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
