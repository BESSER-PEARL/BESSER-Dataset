import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Transition,
    dtmc::InvokedTransition,
    dtmc::StandardTransition,
    dtmc::CallTransition,
    dtmc::SynchronizedTransition,
    dtmc::Transition,
    dtmc::Node,
    dtmc::Module,
    dtmc::Dtmc,
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



def test_dtmc::invokedtransition_is_not_abstract():
    assert not inspect.isabstract(dtmc::InvokedTransition)


def test_dtmc::invokedtransition_constructor_exists():
    assert callable(dtmc::InvokedTransition.__init__)


def test_dtmc::invokedtransition_constructor_args():
    sig = inspect.signature(dtmc::InvokedTransition.__init__)
    params = list(sig.parameters.keys())



def test_dtmc::standardtransition_is_not_abstract():
    assert not inspect.isabstract(dtmc::StandardTransition)


def test_dtmc::standardtransition_constructor_exists():
    assert callable(dtmc::StandardTransition.__init__)


def test_dtmc::standardtransition_constructor_args():
    sig = inspect.signature(dtmc::StandardTransition.__init__)
    params = list(sig.parameters.keys())



def test_dtmc::calltransition_is_not_abstract():
    assert not inspect.isabstract(dtmc::CallTransition)


def test_dtmc::calltransition_constructor_exists():
    assert callable(dtmc::CallTransition.__init__)


def test_dtmc::calltransition_constructor_args():
    sig = inspect.signature(dtmc::CallTransition.__init__)
    params = list(sig.parameters.keys())



def test_dtmc::synchronizedtransition_is_not_abstract():
    assert not inspect.isabstract(dtmc::SynchronizedTransition)


def test_dtmc::synchronizedtransition_constructor_exists():
    assert callable(dtmc::SynchronizedTransition.__init__)


def test_dtmc::synchronizedtransition_constructor_args():
    sig = inspect.signature(dtmc::SynchronizedTransition.__init__)
    params = list(sig.parameters.keys())



def test_dtmc::transition_is_not_abstract():
    assert not inspect.isabstract(dtmc::Transition)


def test_dtmc::transition_constructor_exists():
    assert callable(dtmc::Transition.__init__)


def test_dtmc::transition_constructor_args():
    sig = inspect.signature(dtmc::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "probability" in params, "Missing parameter 'probability'"

def test_dtmc::transition_has_probability():
    assert hasattr(dtmc::Transition, "probability")
    descriptor = None
    for klass in dtmc::Transition.__mro__:
        if "probability" in klass.__dict__:
            descriptor = klass.__dict__["probability"]
            break
    assert isinstance(descriptor, property)



def test_dtmc::node_is_not_abstract():
    assert not inspect.isabstract(dtmc::Node)


def test_dtmc::node_constructor_exists():
    assert callable(dtmc::Node.__init__)


def test_dtmc::node_constructor_args():
    sig = inspect.signature(dtmc::Node.__init__)
    params = list(sig.parameters.keys())
    assert "isFail" in params, "Missing parameter 'isFail'"
    assert "isEnd" in params, "Missing parameter 'isEnd'"
    assert "isStart" in params, "Missing parameter 'isStart'"

def test_dtmc::node_has_isFail():
    assert hasattr(dtmc::Node, "isFail")
    descriptor = None
    for klass in dtmc::Node.__mro__:
        if "isFail" in klass.__dict__:
            descriptor = klass.__dict__["isFail"]
            break
    assert isinstance(descriptor, property)

def test_dtmc::node_has_isEnd():
    assert hasattr(dtmc::Node, "isEnd")
    descriptor = None
    for klass in dtmc::Node.__mro__:
        if "isEnd" in klass.__dict__:
            descriptor = klass.__dict__["isEnd"]
            break
    assert isinstance(descriptor, property)

def test_dtmc::node_has_isStart():
    assert hasattr(dtmc::Node, "isStart")
    descriptor = None
    for klass in dtmc::Node.__mro__:
        if "isStart" in klass.__dict__:
            descriptor = klass.__dict__["isStart"]
            break
    assert isinstance(descriptor, property)



def test_dtmc::module_is_not_abstract():
    assert not inspect.isabstract(dtmc::Module)


def test_dtmc::module_constructor_exists():
    assert callable(dtmc::Module.__init__)


def test_dtmc::module_constructor_args():
    sig = inspect.signature(dtmc::Module.__init__)
    params = list(sig.parameters.keys())
    assert "isAutonomous" in params, "Missing parameter 'isAutonomous'"

def test_dtmc::module_has_isAutonomous():
    assert hasattr(dtmc::Module, "isAutonomous")
    descriptor = None
    for klass in dtmc::Module.__mro__:
        if "isAutonomous" in klass.__dict__:
            descriptor = klass.__dict__["isAutonomous"]
            break
    assert isinstance(descriptor, property)



def test_dtmc::dtmc_is_not_abstract():
    assert not inspect.isabstract(dtmc::Dtmc)


def test_dtmc::dtmc_constructor_exists():
    assert callable(dtmc::Dtmc.__init__)


def test_dtmc::dtmc_constructor_args():
    sig = inspect.signature(dtmc::Dtmc.__init__)
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
Transition_strategy = st.builds(
    Transition,
)
dtmc::InvokedTransition_strategy = st.builds(
    dtmc::InvokedTransition,
)
dtmc::StandardTransition_strategy = st.builds(
    dtmc::StandardTransition,
)
dtmc::CallTransition_strategy = st.builds(
    dtmc::CallTransition,
)
dtmc::SynchronizedTransition_strategy = st.builds(
    dtmc::SynchronizedTransition,
)
dtmc::Transition_strategy = st.builds(
    dtmc::Transition,
    probability=
        safe_text
)
dtmc::Node_strategy = st.builds(
    dtmc::Node,
    isFail=
        st.booleans(),
    isEnd=
        st.booleans(),
    isStart=
        st.booleans()
)
dtmc::Module_strategy = st.builds(
    dtmc::Module,
    isAutonomous=
        st.booleans()
)
dtmc::Dtmc_strategy = st.builds(
    dtmc::Dtmc,
)

@given(instance=Transition_strategy)
@settings(max_examples=50)
def test_transition_instantiation(instance):
    assert isinstance(instance, Transition)

@given(instance=dtmc::InvokedTransition_strategy)
@settings(max_examples=50)
def test_dtmc::invokedtransition_instantiation(instance):
    assert isinstance(instance, dtmc::InvokedTransition)

@given(instance=dtmc::StandardTransition_strategy)
@settings(max_examples=50)
def test_dtmc::standardtransition_instantiation(instance):
    assert isinstance(instance, dtmc::StandardTransition)

@given(instance=dtmc::CallTransition_strategy)
@settings(max_examples=50)
def test_dtmc::calltransition_instantiation(instance):
    assert isinstance(instance, dtmc::CallTransition)

@given(instance=dtmc::SynchronizedTransition_strategy)
@settings(max_examples=50)
def test_dtmc::synchronizedtransition_instantiation(instance):
    assert isinstance(instance, dtmc::SynchronizedTransition)

@given(instance=dtmc::Transition_strategy)
@settings(max_examples=50)
def test_dtmc::transition_instantiation(instance):
    assert isinstance(instance, dtmc::Transition)

@given(instance=dtmc::Transition_strategy)
def test_dtmc::transition_probability_type(instance):
    assert isinstance(instance.probability, str)


@given(instance=dtmc::Transition_strategy)
def test_dtmc::transition_probability_setter(instance):
    original = instance.probability
    instance.probability = original
    assert instance.probability == original

@given(instance=dtmc::Node_strategy)
@settings(max_examples=50)
def test_dtmc::node_instantiation(instance):
    assert isinstance(instance, dtmc::Node)

@given(instance=dtmc::Node_strategy)
def test_dtmc::node_isFail_type(instance):
    assert isinstance(instance.isFail, bool)


@given(instance=dtmc::Node_strategy)
def test_dtmc::node_isFail_setter(instance):
    original = instance.isFail
    instance.isFail = original
    assert instance.isFail == original

@given(instance=dtmc::Node_strategy)
def test_dtmc::node_isEnd_type(instance):
    assert isinstance(instance.isEnd, bool)


@given(instance=dtmc::Node_strategy)
def test_dtmc::node_isEnd_setter(instance):
    original = instance.isEnd
    instance.isEnd = original
    assert instance.isEnd == original

@given(instance=dtmc::Node_strategy)
def test_dtmc::node_isStart_type(instance):
    assert isinstance(instance.isStart, bool)


@given(instance=dtmc::Node_strategy)
def test_dtmc::node_isStart_setter(instance):
    original = instance.isStart
    instance.isStart = original
    assert instance.isStart == original

@given(instance=dtmc::Module_strategy)
@settings(max_examples=50)
def test_dtmc::module_instantiation(instance):
    assert isinstance(instance, dtmc::Module)

@given(instance=dtmc::Module_strategy)
def test_dtmc::module_isAutonomous_type(instance):
    assert isinstance(instance.isAutonomous, bool)


@given(instance=dtmc::Module_strategy)
def test_dtmc::module_isAutonomous_setter(instance):
    original = instance.isAutonomous
    instance.isAutonomous = original
    assert instance.isAutonomous == original

@given(instance=dtmc::Dtmc_strategy)
@settings(max_examples=50)
def test_dtmc::dtmc_instantiation(instance):
    assert isinstance(instance, dtmc::Dtmc)
