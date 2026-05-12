import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Transition,
    dtmc_CallTransition,
    dtmc_InvokedTransition,
    dtmc_StandardTransition,
    dtmc_SynchronizedTransition,
    dtmc_Transition,
    dtmc_Module,
    dtmc_Dtmc,
    dtmc_Node,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_transition_is_not_abstract():
    assert not inspect.isabstract(Transition)


def test_transition_constructor_exists():
    assert callable(Transition.__init__)


def test_transition_constructor_args():
    sig = inspect.signature(Transition.__init__)
    params = list(sig.parameters.keys())



def test_dtmc_calltransition_is_not_abstract():
    assert not inspect.isabstract(dtmc_CallTransition)


def test_dtmc_calltransition_constructor_exists():
    assert callable(dtmc_CallTransition.__init__)


def test_dtmc_calltransition_constructor_args():
    sig = inspect.signature(dtmc_CallTransition.__init__)
    params = list(sig.parameters.keys())



def test_dtmc_invokedtransition_is_not_abstract():
    assert not inspect.isabstract(dtmc_InvokedTransition)


def test_dtmc_invokedtransition_constructor_exists():
    assert callable(dtmc_InvokedTransition.__init__)


def test_dtmc_invokedtransition_constructor_args():
    sig = inspect.signature(dtmc_InvokedTransition.__init__)
    params = list(sig.parameters.keys())



def test_dtmc_standardtransition_is_not_abstract():
    assert not inspect.isabstract(dtmc_StandardTransition)


def test_dtmc_standardtransition_constructor_exists():
    assert callable(dtmc_StandardTransition.__init__)


def test_dtmc_standardtransition_constructor_args():
    sig = inspect.signature(dtmc_StandardTransition.__init__)
    params = list(sig.parameters.keys())



def test_dtmc_synchronizedtransition_is_not_abstract():
    assert not inspect.isabstract(dtmc_SynchronizedTransition)


def test_dtmc_synchronizedtransition_constructor_exists():
    assert callable(dtmc_SynchronizedTransition.__init__)


def test_dtmc_synchronizedtransition_constructor_args():
    sig = inspect.signature(dtmc_SynchronizedTransition.__init__)
    params = list(sig.parameters.keys())



def test_dtmc_transition_is_not_abstract():
    assert not inspect.isabstract(dtmc_Transition)


def test_dtmc_transition_constructor_exists():
    assert callable(dtmc_Transition.__init__)


def test_dtmc_transition_constructor_args():
    sig = inspect.signature(dtmc_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "probability" in params, "Missing parameter 'probability'"

def test_dtmc_transition_has_probability():
    assert hasattr(dtmc_Transition, "probability")
    descriptor = None
    for klass in dtmc_Transition.__mro__:
        if "probability" in klass.__dict__:
            descriptor = klass.__dict__["probability"]
            break
    assert isinstance(descriptor, property)



def test_dtmc_module_is_not_abstract():
    assert not inspect.isabstract(dtmc_Module)


def test_dtmc_module_constructor_exists():
    assert callable(dtmc_Module.__init__)


def test_dtmc_module_constructor_args():
    sig = inspect.signature(dtmc_Module.__init__)
    params = list(sig.parameters.keys())
    assert "isAutonomous" in params, "Missing parameter 'isAutonomous'"

def test_dtmc_module_has_isAutonomous():
    assert hasattr(dtmc_Module, "isAutonomous")
    descriptor = None
    for klass in dtmc_Module.__mro__:
        if "isAutonomous" in klass.__dict__:
            descriptor = klass.__dict__["isAutonomous"]
            break
    assert isinstance(descriptor, property)



def test_dtmc_dtmc_is_not_abstract():
    assert not inspect.isabstract(dtmc_Dtmc)


def test_dtmc_dtmc_constructor_exists():
    assert callable(dtmc_Dtmc.__init__)


def test_dtmc_dtmc_constructor_args():
    sig = inspect.signature(dtmc_Dtmc.__init__)
    params = list(sig.parameters.keys())



def test_dtmc_node_is_not_abstract():
    assert not inspect.isabstract(dtmc_Node)


def test_dtmc_node_constructor_exists():
    assert callable(dtmc_Node.__init__)


def test_dtmc_node_constructor_args():
    sig = inspect.signature(dtmc_Node.__init__)
    params = list(sig.parameters.keys())
    assert "isEnd" in params, "Missing parameter 'isEnd'"
    assert "isStart" in params, "Missing parameter 'isStart'"
    assert "isFail" in params, "Missing parameter 'isFail'"

def test_dtmc_node_has_isEnd():
    assert hasattr(dtmc_Node, "isEnd")
    descriptor = None
    for klass in dtmc_Node.__mro__:
        if "isEnd" in klass.__dict__:
            descriptor = klass.__dict__["isEnd"]
            break
    assert isinstance(descriptor, property)

def test_dtmc_node_has_isStart():
    assert hasattr(dtmc_Node, "isStart")
    descriptor = None
    for klass in dtmc_Node.__mro__:
        if "isStart" in klass.__dict__:
            descriptor = klass.__dict__["isStart"]
            break
    assert isinstance(descriptor, property)

def test_dtmc_node_has_isFail():
    assert hasattr(dtmc_Node, "isFail")
    descriptor = None
    for klass in dtmc_Node.__mro__:
        if "isFail" in klass.__dict__:
            descriptor = klass.__dict__["isFail"]
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
Transition_strategy = st.builds(
    Transition,
)
dtmc_CallTransition_strategy = st.builds(
    dtmc_CallTransition,
)
dtmc_InvokedTransition_strategy = st.builds(
    dtmc_InvokedTransition,
)
dtmc_StandardTransition_strategy = st.builds(
    dtmc_StandardTransition,
)
dtmc_SynchronizedTransition_strategy = st.builds(
    dtmc_SynchronizedTransition,
)
dtmc_Transition_strategy = st.builds(
    dtmc_Transition,
    probability=
        safe_text
)
dtmc_Module_strategy = st.builds(
    dtmc_Module,
    isAutonomous=
        st.booleans()
)
dtmc_Dtmc_strategy = st.builds(
    dtmc_Dtmc,
)
dtmc_Node_strategy = st.builds(
    dtmc_Node,
    isEnd=
        st.booleans(),
    isStart=
        st.booleans(),
    isFail=
        st.booleans()
)

@given(instance=Transition_strategy)
@settings(max_examples=50)
def test_transition_instantiation(instance):
    assert isinstance(instance, Transition)

@given(instance=dtmc_CallTransition_strategy)
@settings(max_examples=50)
def test_dtmc_calltransition_instantiation(instance):
    assert isinstance(instance, dtmc_CallTransition)

@given(instance=dtmc_InvokedTransition_strategy)
@settings(max_examples=50)
def test_dtmc_invokedtransition_instantiation(instance):
    assert isinstance(instance, dtmc_InvokedTransition)

@given(instance=dtmc_StandardTransition_strategy)
@settings(max_examples=50)
def test_dtmc_standardtransition_instantiation(instance):
    assert isinstance(instance, dtmc_StandardTransition)

@given(instance=dtmc_SynchronizedTransition_strategy)
@settings(max_examples=50)
def test_dtmc_synchronizedtransition_instantiation(instance):
    assert isinstance(instance, dtmc_SynchronizedTransition)

@given(instance=dtmc_Transition_strategy)
@settings(max_examples=50)
def test_dtmc_transition_instantiation(instance):
    assert isinstance(instance, dtmc_Transition)



@given(instance=dtmc_Transition_strategy)
def test_dtmc_transition_probability_setter(instance):
    original = instance.probability
    instance.probability = original
    assert instance.probability == original

@given(instance=dtmc_Module_strategy)
@settings(max_examples=50)
def test_dtmc_module_instantiation(instance):
    assert isinstance(instance, dtmc_Module)



@given(instance=dtmc_Module_strategy)
def test_dtmc_module_isAutonomous_setter(instance):
    original = instance.isAutonomous
    instance.isAutonomous = original
    assert instance.isAutonomous == original

@given(instance=dtmc_Dtmc_strategy)
@settings(max_examples=50)
def test_dtmc_dtmc_instantiation(instance):
    assert isinstance(instance, dtmc_Dtmc)

@given(instance=dtmc_Node_strategy)
@settings(max_examples=50)
def test_dtmc_node_instantiation(instance):
    assert isinstance(instance, dtmc_Node)



@given(instance=dtmc_Node_strategy)
def test_dtmc_node_isEnd_setter(instance):
    original = instance.isEnd
    instance.isEnd = original
    assert instance.isEnd == original



@given(instance=dtmc_Node_strategy)
def test_dtmc_node_isStart_setter(instance):
    original = instance.isStart
    instance.isStart = original
    assert instance.isStart == original



@given(instance=dtmc_Node_strategy)
def test_dtmc_node_isFail_setter(instance):
    original = instance.isFail
    instance.isFail = original
    assert instance.isFail == original
