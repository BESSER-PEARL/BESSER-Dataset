import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    TrgCompositeState,
    TrgTransition,
    jointPackage::HSM2FSM::TrgStateMachine,
    TrgStateMachine,
    jointPackage::HSM2FSM::TrgRoot,
    SrcCompositeState,
    jointPackage::HSM2FSM::SrcAbstractState,
    jointPackage::HSM2FSM::SrcTransition,
    SrcAbstractState,
    jointPackage::HSM2FSM::SrcCompositeState,
    jointPackage::HSM2FSM::SrcInitialState,
    jointPackage::HSM2FSM::SrcRegularState,
    SrcTransition,
    jointPackage::HSM2FSM::SrcStateMachine,
    jointPackage::HSM2FSM::TrgAbstractState,
    jointPackage::HSM2FSM::TrgTransition,
    TrgAbstractState,
    jointPackage::HSM2FSM::TrgRegularState,
    jointPackage::HSM2FSM::TrgCompositeState,
    jointPackage::HSM2FSM::TrgInitialState,
    jointPackage::HSM2FSM::JointMM,
    SrcStateMachine,
    jointPackage::HSM2FSM::SrcRoot,
    TrgRoot,
    SrcRoot,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_trgcompositestate_is_not_abstract():
    assert not inspect.isabstract(TrgCompositeState)


def test_trgcompositestate_constructor_exists():
    assert callable(TrgCompositeState.__init__)


def test_trgcompositestate_constructor_args():
    sig = inspect.signature(TrgCompositeState.__init__)
    params = list(sig.parameters.keys())



def test_trgtransition_is_not_abstract():
    assert not inspect.isabstract(TrgTransition)


def test_trgtransition_constructor_exists():
    assert callable(TrgTransition.__init__)


def test_trgtransition_constructor_args():
    sig = inspect.signature(TrgTransition.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::hsm2fsm::trgstatemachine_is_not_abstract():
    assert not inspect.isabstract(jointPackage::HSM2FSM::TrgStateMachine)


def test_jointpackage::hsm2fsm::trgstatemachine_constructor_exists():
    assert callable(jointPackage::HSM2FSM::TrgStateMachine.__init__)


def test_jointpackage::hsm2fsm::trgstatemachine_constructor_args():
    sig = inspect.signature(jointPackage::HSM2FSM::TrgStateMachine.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_jointpackage::hsm2fsm::trgstatemachine_has_name():
    assert hasattr(jointPackage::HSM2FSM::TrgStateMachine, "name")
    descriptor = None
    for klass in jointPackage::HSM2FSM::TrgStateMachine.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_trgstatemachine_is_not_abstract():
    assert not inspect.isabstract(TrgStateMachine)


def test_trgstatemachine_constructor_exists():
    assert callable(TrgStateMachine.__init__)


def test_trgstatemachine_constructor_args():
    sig = inspect.signature(TrgStateMachine.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::hsm2fsm::trgroot_is_not_abstract():
    assert not inspect.isabstract(jointPackage::HSM2FSM::TrgRoot)


def test_jointpackage::hsm2fsm::trgroot_constructor_exists():
    assert callable(jointPackage::HSM2FSM::TrgRoot.__init__)


def test_jointpackage::hsm2fsm::trgroot_constructor_args():
    sig = inspect.signature(jointPackage::HSM2FSM::TrgRoot.__init__)
    params = list(sig.parameters.keys())



def test_srccompositestate_is_not_abstract():
    assert not inspect.isabstract(SrcCompositeState)


def test_srccompositestate_constructor_exists():
    assert callable(SrcCompositeState.__init__)


def test_srccompositestate_constructor_args():
    sig = inspect.signature(SrcCompositeState.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::hsm2fsm::srcabstractstate_is_not_abstract():
    assert not inspect.isabstract(jointPackage::HSM2FSM::SrcAbstractState)


def test_jointpackage::hsm2fsm::srcabstractstate_constructor_exists():
    assert callable(jointPackage::HSM2FSM::SrcAbstractState.__init__)


def test_jointpackage::hsm2fsm::srcabstractstate_constructor_args():
    sig = inspect.signature(jointPackage::HSM2FSM::SrcAbstractState.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_jointpackage::hsm2fsm::srcabstractstate_has_name():
    assert hasattr(jointPackage::HSM2FSM::SrcAbstractState, "name")
    descriptor = None
    for klass in jointPackage::HSM2FSM::SrcAbstractState.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage::hsm2fsm::srctransition_is_not_abstract():
    assert not inspect.isabstract(jointPackage::HSM2FSM::SrcTransition)


def test_jointpackage::hsm2fsm::srctransition_constructor_exists():
    assert callable(jointPackage::HSM2FSM::SrcTransition.__init__)


def test_jointpackage::hsm2fsm::srctransition_constructor_args():
    sig = inspect.signature(jointPackage::HSM2FSM::SrcTransition.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_jointpackage::hsm2fsm::srctransition_has_label():
    assert hasattr(jointPackage::HSM2FSM::SrcTransition, "label")
    descriptor = None
    for klass in jointPackage::HSM2FSM::SrcTransition.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_srcabstractstate_is_not_abstract():
    assert not inspect.isabstract(SrcAbstractState)


def test_srcabstractstate_constructor_exists():
    assert callable(SrcAbstractState.__init__)


def test_srcabstractstate_constructor_args():
    sig = inspect.signature(SrcAbstractState.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::hsm2fsm::srccompositestate_is_not_abstract():
    assert not inspect.isabstract(jointPackage::HSM2FSM::SrcCompositeState)


def test_jointpackage::hsm2fsm::srccompositestate_constructor_exists():
    assert callable(jointPackage::HSM2FSM::SrcCompositeState.__init__)


def test_jointpackage::hsm2fsm::srccompositestate_constructor_args():
    sig = inspect.signature(jointPackage::HSM2FSM::SrcCompositeState.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::hsm2fsm::srcinitialstate_is_not_abstract():
    assert not inspect.isabstract(jointPackage::HSM2FSM::SrcInitialState)


def test_jointpackage::hsm2fsm::srcinitialstate_constructor_exists():
    assert callable(jointPackage::HSM2FSM::SrcInitialState.__init__)


def test_jointpackage::hsm2fsm::srcinitialstate_constructor_args():
    sig = inspect.signature(jointPackage::HSM2FSM::SrcInitialState.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::hsm2fsm::srcregularstate_is_not_abstract():
    assert not inspect.isabstract(jointPackage::HSM2FSM::SrcRegularState)


def test_jointpackage::hsm2fsm::srcregularstate_constructor_exists():
    assert callable(jointPackage::HSM2FSM::SrcRegularState.__init__)


def test_jointpackage::hsm2fsm::srcregularstate_constructor_args():
    sig = inspect.signature(jointPackage::HSM2FSM::SrcRegularState.__init__)
    params = list(sig.parameters.keys())



def test_srctransition_is_not_abstract():
    assert not inspect.isabstract(SrcTransition)


def test_srctransition_constructor_exists():
    assert callable(SrcTransition.__init__)


def test_srctransition_constructor_args():
    sig = inspect.signature(SrcTransition.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::hsm2fsm::srcstatemachine_is_not_abstract():
    assert not inspect.isabstract(jointPackage::HSM2FSM::SrcStateMachine)


def test_jointpackage::hsm2fsm::srcstatemachine_constructor_exists():
    assert callable(jointPackage::HSM2FSM::SrcStateMachine.__init__)


def test_jointpackage::hsm2fsm::srcstatemachine_constructor_args():
    sig = inspect.signature(jointPackage::HSM2FSM::SrcStateMachine.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_jointpackage::hsm2fsm::srcstatemachine_has_name():
    assert hasattr(jointPackage::HSM2FSM::SrcStateMachine, "name")
    descriptor = None
    for klass in jointPackage::HSM2FSM::SrcStateMachine.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage::hsm2fsm::trgabstractstate_is_not_abstract():
    assert not inspect.isabstract(jointPackage::HSM2FSM::TrgAbstractState)


def test_jointpackage::hsm2fsm::trgabstractstate_constructor_exists():
    assert callable(jointPackage::HSM2FSM::TrgAbstractState.__init__)


def test_jointpackage::hsm2fsm::trgabstractstate_constructor_args():
    sig = inspect.signature(jointPackage::HSM2FSM::TrgAbstractState.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_jointpackage::hsm2fsm::trgabstractstate_has_name():
    assert hasattr(jointPackage::HSM2FSM::TrgAbstractState, "name")
    descriptor = None
    for klass in jointPackage::HSM2FSM::TrgAbstractState.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage::hsm2fsm::trgtransition_is_not_abstract():
    assert not inspect.isabstract(jointPackage::HSM2FSM::TrgTransition)


def test_jointpackage::hsm2fsm::trgtransition_constructor_exists():
    assert callable(jointPackage::HSM2FSM::TrgTransition.__init__)


def test_jointpackage::hsm2fsm::trgtransition_constructor_args():
    sig = inspect.signature(jointPackage::HSM2FSM::TrgTransition.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_jointpackage::hsm2fsm::trgtransition_has_label():
    assert hasattr(jointPackage::HSM2FSM::TrgTransition, "label")
    descriptor = None
    for klass in jointPackage::HSM2FSM::TrgTransition.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_trgabstractstate_is_not_abstract():
    assert not inspect.isabstract(TrgAbstractState)


def test_trgabstractstate_constructor_exists():
    assert callable(TrgAbstractState.__init__)


def test_trgabstractstate_constructor_args():
    sig = inspect.signature(TrgAbstractState.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::hsm2fsm::trgregularstate_is_not_abstract():
    assert not inspect.isabstract(jointPackage::HSM2FSM::TrgRegularState)


def test_jointpackage::hsm2fsm::trgregularstate_constructor_exists():
    assert callable(jointPackage::HSM2FSM::TrgRegularState.__init__)


def test_jointpackage::hsm2fsm::trgregularstate_constructor_args():
    sig = inspect.signature(jointPackage::HSM2FSM::TrgRegularState.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::hsm2fsm::trgcompositestate_is_not_abstract():
    assert not inspect.isabstract(jointPackage::HSM2FSM::TrgCompositeState)


def test_jointpackage::hsm2fsm::trgcompositestate_constructor_exists():
    assert callable(jointPackage::HSM2FSM::TrgCompositeState.__init__)


def test_jointpackage::hsm2fsm::trgcompositestate_constructor_args():
    sig = inspect.signature(jointPackage::HSM2FSM::TrgCompositeState.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::hsm2fsm::trginitialstate_is_not_abstract():
    assert not inspect.isabstract(jointPackage::HSM2FSM::TrgInitialState)


def test_jointpackage::hsm2fsm::trginitialstate_constructor_exists():
    assert callable(jointPackage::HSM2FSM::TrgInitialState.__init__)


def test_jointpackage::hsm2fsm::trginitialstate_constructor_args():
    sig = inspect.signature(jointPackage::HSM2FSM::TrgInitialState.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::hsm2fsm::jointmm_is_not_abstract():
    assert not inspect.isabstract(jointPackage::HSM2FSM::JointMM)


def test_jointpackage::hsm2fsm::jointmm_constructor_exists():
    assert callable(jointPackage::HSM2FSM::JointMM.__init__)


def test_jointpackage::hsm2fsm::jointmm_constructor_args():
    sig = inspect.signature(jointPackage::HSM2FSM::JointMM.__init__)
    params = list(sig.parameters.keys())



def test_srcstatemachine_is_not_abstract():
    assert not inspect.isabstract(SrcStateMachine)


def test_srcstatemachine_constructor_exists():
    assert callable(SrcStateMachine.__init__)


def test_srcstatemachine_constructor_args():
    sig = inspect.signature(SrcStateMachine.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::hsm2fsm::srcroot_is_not_abstract():
    assert not inspect.isabstract(jointPackage::HSM2FSM::SrcRoot)


def test_jointpackage::hsm2fsm::srcroot_constructor_exists():
    assert callable(jointPackage::HSM2FSM::SrcRoot.__init__)


def test_jointpackage::hsm2fsm::srcroot_constructor_args():
    sig = inspect.signature(jointPackage::HSM2FSM::SrcRoot.__init__)
    params = list(sig.parameters.keys())



def test_trgroot_is_not_abstract():
    assert not inspect.isabstract(TrgRoot)


def test_trgroot_constructor_exists():
    assert callable(TrgRoot.__init__)


def test_trgroot_constructor_args():
    sig = inspect.signature(TrgRoot.__init__)
    params = list(sig.parameters.keys())



def test_srcroot_is_not_abstract():
    assert not inspect.isabstract(SrcRoot)


def test_srcroot_constructor_exists():
    assert callable(SrcRoot.__init__)


def test_srcroot_constructor_args():
    sig = inspect.signature(SrcRoot.__init__)
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
TrgCompositeState_strategy = st.builds(
    TrgCompositeState,
)
TrgTransition_strategy = st.builds(
    TrgTransition,
)
jointPackage::HSM2FSM::TrgStateMachine_strategy = st.builds(
    jointPackage::HSM2FSM::TrgStateMachine,
    name=
        safe_text
)
TrgStateMachine_strategy = st.builds(
    TrgStateMachine,
)
jointPackage::HSM2FSM::TrgRoot_strategy = st.builds(
    jointPackage::HSM2FSM::TrgRoot,
)
SrcCompositeState_strategy = st.builds(
    SrcCompositeState,
)
jointPackage::HSM2FSM::SrcAbstractState_strategy = st.builds(
    jointPackage::HSM2FSM::SrcAbstractState,
    name=
        safe_text
)
jointPackage::HSM2FSM::SrcTransition_strategy = st.builds(
    jointPackage::HSM2FSM::SrcTransition,
    label=
        safe_text
)
SrcAbstractState_strategy = st.builds(
    SrcAbstractState,
)
jointPackage::HSM2FSM::SrcCompositeState_strategy = st.builds(
    jointPackage::HSM2FSM::SrcCompositeState,
)
jointPackage::HSM2FSM::SrcInitialState_strategy = st.builds(
    jointPackage::HSM2FSM::SrcInitialState,
)
jointPackage::HSM2FSM::SrcRegularState_strategy = st.builds(
    jointPackage::HSM2FSM::SrcRegularState,
)
SrcTransition_strategy = st.builds(
    SrcTransition,
)
jointPackage::HSM2FSM::SrcStateMachine_strategy = st.builds(
    jointPackage::HSM2FSM::SrcStateMachine,
    name=
        safe_text
)
jointPackage::HSM2FSM::TrgAbstractState_strategy = st.builds(
    jointPackage::HSM2FSM::TrgAbstractState,
    name=
        safe_text
)
jointPackage::HSM2FSM::TrgTransition_strategy = st.builds(
    jointPackage::HSM2FSM::TrgTransition,
    label=
        safe_text
)
TrgAbstractState_strategy = st.builds(
    TrgAbstractState,
)
jointPackage::HSM2FSM::TrgRegularState_strategy = st.builds(
    jointPackage::HSM2FSM::TrgRegularState,
)
jointPackage::HSM2FSM::TrgCompositeState_strategy = st.builds(
    jointPackage::HSM2FSM::TrgCompositeState,
)
jointPackage::HSM2FSM::TrgInitialState_strategy = st.builds(
    jointPackage::HSM2FSM::TrgInitialState,
)
jointPackage::HSM2FSM::JointMM_strategy = st.builds(
    jointPackage::HSM2FSM::JointMM,
)
SrcStateMachine_strategy = st.builds(
    SrcStateMachine,
)
jointPackage::HSM2FSM::SrcRoot_strategy = st.builds(
    jointPackage::HSM2FSM::SrcRoot,
)
TrgRoot_strategy = st.builds(
    TrgRoot,
)
SrcRoot_strategy = st.builds(
    SrcRoot,
)

@given(instance=TrgCompositeState_strategy)
@settings(max_examples=50)
def test_trgcompositestate_instantiation(instance):
    assert isinstance(instance, TrgCompositeState)

@given(instance=TrgTransition_strategy)
@settings(max_examples=50)
def test_trgtransition_instantiation(instance):
    assert isinstance(instance, TrgTransition)

@given(instance=jointPackage::HSM2FSM::TrgStateMachine_strategy)
@settings(max_examples=50)
def test_jointpackage::hsm2fsm::trgstatemachine_instantiation(instance):
    assert isinstance(instance, jointPackage::HSM2FSM::TrgStateMachine)

@given(instance=jointPackage::HSM2FSM::TrgStateMachine_strategy)
def test_jointpackage::hsm2fsm::trgstatemachine_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=jointPackage::HSM2FSM::TrgStateMachine_strategy)
def test_jointpackage::hsm2fsm::trgstatemachine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=TrgStateMachine_strategy)
@settings(max_examples=50)
def test_trgstatemachine_instantiation(instance):
    assert isinstance(instance, TrgStateMachine)

@given(instance=jointPackage::HSM2FSM::TrgRoot_strategy)
@settings(max_examples=50)
def test_jointpackage::hsm2fsm::trgroot_instantiation(instance):
    assert isinstance(instance, jointPackage::HSM2FSM::TrgRoot)

@given(instance=SrcCompositeState_strategy)
@settings(max_examples=50)
def test_srccompositestate_instantiation(instance):
    assert isinstance(instance, SrcCompositeState)

@given(instance=jointPackage::HSM2FSM::SrcAbstractState_strategy)
@settings(max_examples=50)
def test_jointpackage::hsm2fsm::srcabstractstate_instantiation(instance):
    assert isinstance(instance, jointPackage::HSM2FSM::SrcAbstractState)

@given(instance=jointPackage::HSM2FSM::SrcAbstractState_strategy)
def test_jointpackage::hsm2fsm::srcabstractstate_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=jointPackage::HSM2FSM::SrcAbstractState_strategy)
def test_jointpackage::hsm2fsm::srcabstractstate_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=jointPackage::HSM2FSM::SrcTransition_strategy)
@settings(max_examples=50)
def test_jointpackage::hsm2fsm::srctransition_instantiation(instance):
    assert isinstance(instance, jointPackage::HSM2FSM::SrcTransition)

@given(instance=jointPackage::HSM2FSM::SrcTransition_strategy)
def test_jointpackage::hsm2fsm::srctransition_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=jointPackage::HSM2FSM::SrcTransition_strategy)
def test_jointpackage::hsm2fsm::srctransition_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=SrcAbstractState_strategy)
@settings(max_examples=50)
def test_srcabstractstate_instantiation(instance):
    assert isinstance(instance, SrcAbstractState)

@given(instance=jointPackage::HSM2FSM::SrcCompositeState_strategy)
@settings(max_examples=50)
def test_jointpackage::hsm2fsm::srccompositestate_instantiation(instance):
    assert isinstance(instance, jointPackage::HSM2FSM::SrcCompositeState)

@given(instance=jointPackage::HSM2FSM::SrcInitialState_strategy)
@settings(max_examples=50)
def test_jointpackage::hsm2fsm::srcinitialstate_instantiation(instance):
    assert isinstance(instance, jointPackage::HSM2FSM::SrcInitialState)

@given(instance=jointPackage::HSM2FSM::SrcRegularState_strategy)
@settings(max_examples=50)
def test_jointpackage::hsm2fsm::srcregularstate_instantiation(instance):
    assert isinstance(instance, jointPackage::HSM2FSM::SrcRegularState)

@given(instance=SrcTransition_strategy)
@settings(max_examples=50)
def test_srctransition_instantiation(instance):
    assert isinstance(instance, SrcTransition)

@given(instance=jointPackage::HSM2FSM::SrcStateMachine_strategy)
@settings(max_examples=50)
def test_jointpackage::hsm2fsm::srcstatemachine_instantiation(instance):
    assert isinstance(instance, jointPackage::HSM2FSM::SrcStateMachine)

@given(instance=jointPackage::HSM2FSM::SrcStateMachine_strategy)
def test_jointpackage::hsm2fsm::srcstatemachine_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=jointPackage::HSM2FSM::SrcStateMachine_strategy)
def test_jointpackage::hsm2fsm::srcstatemachine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=jointPackage::HSM2FSM::TrgAbstractState_strategy)
@settings(max_examples=50)
def test_jointpackage::hsm2fsm::trgabstractstate_instantiation(instance):
    assert isinstance(instance, jointPackage::HSM2FSM::TrgAbstractState)

@given(instance=jointPackage::HSM2FSM::TrgAbstractState_strategy)
def test_jointpackage::hsm2fsm::trgabstractstate_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=jointPackage::HSM2FSM::TrgAbstractState_strategy)
def test_jointpackage::hsm2fsm::trgabstractstate_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=jointPackage::HSM2FSM::TrgTransition_strategy)
@settings(max_examples=50)
def test_jointpackage::hsm2fsm::trgtransition_instantiation(instance):
    assert isinstance(instance, jointPackage::HSM2FSM::TrgTransition)

@given(instance=jointPackage::HSM2FSM::TrgTransition_strategy)
def test_jointpackage::hsm2fsm::trgtransition_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=jointPackage::HSM2FSM::TrgTransition_strategy)
def test_jointpackage::hsm2fsm::trgtransition_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=TrgAbstractState_strategy)
@settings(max_examples=50)
def test_trgabstractstate_instantiation(instance):
    assert isinstance(instance, TrgAbstractState)

@given(instance=jointPackage::HSM2FSM::TrgRegularState_strategy)
@settings(max_examples=50)
def test_jointpackage::hsm2fsm::trgregularstate_instantiation(instance):
    assert isinstance(instance, jointPackage::HSM2FSM::TrgRegularState)

@given(instance=jointPackage::HSM2FSM::TrgCompositeState_strategy)
@settings(max_examples=50)
def test_jointpackage::hsm2fsm::trgcompositestate_instantiation(instance):
    assert isinstance(instance, jointPackage::HSM2FSM::TrgCompositeState)

@given(instance=jointPackage::HSM2FSM::TrgInitialState_strategy)
@settings(max_examples=50)
def test_jointpackage::hsm2fsm::trginitialstate_instantiation(instance):
    assert isinstance(instance, jointPackage::HSM2FSM::TrgInitialState)

@given(instance=jointPackage::HSM2FSM::JointMM_strategy)
@settings(max_examples=50)
def test_jointpackage::hsm2fsm::jointmm_instantiation(instance):
    assert isinstance(instance, jointPackage::HSM2FSM::JointMM)

@given(instance=SrcStateMachine_strategy)
@settings(max_examples=50)
def test_srcstatemachine_instantiation(instance):
    assert isinstance(instance, SrcStateMachine)

@given(instance=jointPackage::HSM2FSM::SrcRoot_strategy)
@settings(max_examples=50)
def test_jointpackage::hsm2fsm::srcroot_instantiation(instance):
    assert isinstance(instance, jointPackage::HSM2FSM::SrcRoot)

@given(instance=TrgRoot_strategy)
@settings(max_examples=50)
def test_trgroot_instantiation(instance):
    assert isinstance(instance, TrgRoot)

@given(instance=SrcRoot_strategy)
@settings(max_examples=50)
def test_srcroot_instantiation(instance):
    assert isinstance(instance, SrcRoot)
