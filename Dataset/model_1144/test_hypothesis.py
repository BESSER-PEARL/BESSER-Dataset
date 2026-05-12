import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    TrgCompositeState,
    TrgTransition,
    jointPackage_HSM2FSM_TrgStateMachine,
    TrgStateMachine,
    jointPackage_HSM2FSM_TrgRoot,
    SrcCompositeState,
    jointPackage_HSM2FSM_SrcAbstractState,
    jointPackage_HSM2FSM_SrcTransition,
    SrcAbstractState,
    jointPackage_HSM2FSM_SrcInitialState,
    jointPackage_HSM2FSM_SrcRegularState,
    jointPackage_HSM2FSM_SrcCompositeState,
    SrcTransition,
    jointPackage_HSM2FSM_SrcStateMachine,
    jointPackage_HSM2FSM_TrgAbstractState,
    jointPackage_HSM2FSM_TrgTransition,
    TrgAbstractState,
    jointPackage_HSM2FSM_TrgRegularState,
    jointPackage_HSM2FSM_TrgInitialState,
    jointPackage_HSM2FSM_TrgCompositeState,
    jointPackage_HSM2FSM_JointMM,
    SrcStateMachine,
    jointPackage_HSM2FSM_SrcRoot,
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



def test_jointpackage_hsm2fsm_trgstatemachine_is_not_abstract():
    assert not inspect.isabstract(jointPackage_HSM2FSM_TrgStateMachine)


def test_jointpackage_hsm2fsm_trgstatemachine_constructor_exists():
    assert callable(jointPackage_HSM2FSM_TrgStateMachine.__init__)


def test_jointpackage_hsm2fsm_trgstatemachine_constructor_args():
    sig = inspect.signature(jointPackage_HSM2FSM_TrgStateMachine.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_jointpackage_hsm2fsm_trgstatemachine_has_name():
    assert hasattr(jointPackage_HSM2FSM_TrgStateMachine, "name")
    descriptor = None
    for klass in jointPackage_HSM2FSM_TrgStateMachine.__mro__:
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



def test_jointpackage_hsm2fsm_trgroot_is_not_abstract():
    assert not inspect.isabstract(jointPackage_HSM2FSM_TrgRoot)


def test_jointpackage_hsm2fsm_trgroot_constructor_exists():
    assert callable(jointPackage_HSM2FSM_TrgRoot.__init__)


def test_jointpackage_hsm2fsm_trgroot_constructor_args():
    sig = inspect.signature(jointPackage_HSM2FSM_TrgRoot.__init__)
    params = list(sig.parameters.keys())



def test_srccompositestate_is_not_abstract():
    assert not inspect.isabstract(SrcCompositeState)


def test_srccompositestate_constructor_exists():
    assert callable(SrcCompositeState.__init__)


def test_srccompositestate_constructor_args():
    sig = inspect.signature(SrcCompositeState.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_hsm2fsm_srcabstractstate_is_not_abstract():
    assert not inspect.isabstract(jointPackage_HSM2FSM_SrcAbstractState)


def test_jointpackage_hsm2fsm_srcabstractstate_constructor_exists():
    assert callable(jointPackage_HSM2FSM_SrcAbstractState.__init__)


def test_jointpackage_hsm2fsm_srcabstractstate_constructor_args():
    sig = inspect.signature(jointPackage_HSM2FSM_SrcAbstractState.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_jointpackage_hsm2fsm_srcabstractstate_has_name():
    assert hasattr(jointPackage_HSM2FSM_SrcAbstractState, "name")
    descriptor = None
    for klass in jointPackage_HSM2FSM_SrcAbstractState.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage_hsm2fsm_srctransition_is_not_abstract():
    assert not inspect.isabstract(jointPackage_HSM2FSM_SrcTransition)


def test_jointpackage_hsm2fsm_srctransition_constructor_exists():
    assert callable(jointPackage_HSM2FSM_SrcTransition.__init__)


def test_jointpackage_hsm2fsm_srctransition_constructor_args():
    sig = inspect.signature(jointPackage_HSM2FSM_SrcTransition.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_jointpackage_hsm2fsm_srctransition_has_label():
    assert hasattr(jointPackage_HSM2FSM_SrcTransition, "label")
    descriptor = None
    for klass in jointPackage_HSM2FSM_SrcTransition.__mro__:
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



def test_jointpackage_hsm2fsm_srcinitialstate_is_not_abstract():
    assert not inspect.isabstract(jointPackage_HSM2FSM_SrcInitialState)


def test_jointpackage_hsm2fsm_srcinitialstate_constructor_exists():
    assert callable(jointPackage_HSM2FSM_SrcInitialState.__init__)


def test_jointpackage_hsm2fsm_srcinitialstate_constructor_args():
    sig = inspect.signature(jointPackage_HSM2FSM_SrcInitialState.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_hsm2fsm_srcregularstate_is_not_abstract():
    assert not inspect.isabstract(jointPackage_HSM2FSM_SrcRegularState)


def test_jointpackage_hsm2fsm_srcregularstate_constructor_exists():
    assert callable(jointPackage_HSM2FSM_SrcRegularState.__init__)


def test_jointpackage_hsm2fsm_srcregularstate_constructor_args():
    sig = inspect.signature(jointPackage_HSM2FSM_SrcRegularState.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_hsm2fsm_srccompositestate_is_not_abstract():
    assert not inspect.isabstract(jointPackage_HSM2FSM_SrcCompositeState)


def test_jointpackage_hsm2fsm_srccompositestate_constructor_exists():
    assert callable(jointPackage_HSM2FSM_SrcCompositeState.__init__)


def test_jointpackage_hsm2fsm_srccompositestate_constructor_args():
    sig = inspect.signature(jointPackage_HSM2FSM_SrcCompositeState.__init__)
    params = list(sig.parameters.keys())



def test_srctransition_is_not_abstract():
    assert not inspect.isabstract(SrcTransition)


def test_srctransition_constructor_exists():
    assert callable(SrcTransition.__init__)


def test_srctransition_constructor_args():
    sig = inspect.signature(SrcTransition.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_hsm2fsm_srcstatemachine_is_not_abstract():
    assert not inspect.isabstract(jointPackage_HSM2FSM_SrcStateMachine)


def test_jointpackage_hsm2fsm_srcstatemachine_constructor_exists():
    assert callable(jointPackage_HSM2FSM_SrcStateMachine.__init__)


def test_jointpackage_hsm2fsm_srcstatemachine_constructor_args():
    sig = inspect.signature(jointPackage_HSM2FSM_SrcStateMachine.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_jointpackage_hsm2fsm_srcstatemachine_has_name():
    assert hasattr(jointPackage_HSM2FSM_SrcStateMachine, "name")
    descriptor = None
    for klass in jointPackage_HSM2FSM_SrcStateMachine.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage_hsm2fsm_trgabstractstate_is_not_abstract():
    assert not inspect.isabstract(jointPackage_HSM2FSM_TrgAbstractState)


def test_jointpackage_hsm2fsm_trgabstractstate_constructor_exists():
    assert callable(jointPackage_HSM2FSM_TrgAbstractState.__init__)


def test_jointpackage_hsm2fsm_trgabstractstate_constructor_args():
    sig = inspect.signature(jointPackage_HSM2FSM_TrgAbstractState.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_jointpackage_hsm2fsm_trgabstractstate_has_name():
    assert hasattr(jointPackage_HSM2FSM_TrgAbstractState, "name")
    descriptor = None
    for klass in jointPackage_HSM2FSM_TrgAbstractState.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage_hsm2fsm_trgtransition_is_not_abstract():
    assert not inspect.isabstract(jointPackage_HSM2FSM_TrgTransition)


def test_jointpackage_hsm2fsm_trgtransition_constructor_exists():
    assert callable(jointPackage_HSM2FSM_TrgTransition.__init__)


def test_jointpackage_hsm2fsm_trgtransition_constructor_args():
    sig = inspect.signature(jointPackage_HSM2FSM_TrgTransition.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_jointpackage_hsm2fsm_trgtransition_has_label():
    assert hasattr(jointPackage_HSM2FSM_TrgTransition, "label")
    descriptor = None
    for klass in jointPackage_HSM2FSM_TrgTransition.__mro__:
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



def test_jointpackage_hsm2fsm_trgregularstate_is_not_abstract():
    assert not inspect.isabstract(jointPackage_HSM2FSM_TrgRegularState)


def test_jointpackage_hsm2fsm_trgregularstate_constructor_exists():
    assert callable(jointPackage_HSM2FSM_TrgRegularState.__init__)


def test_jointpackage_hsm2fsm_trgregularstate_constructor_args():
    sig = inspect.signature(jointPackage_HSM2FSM_TrgRegularState.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_hsm2fsm_trginitialstate_is_not_abstract():
    assert not inspect.isabstract(jointPackage_HSM2FSM_TrgInitialState)


def test_jointpackage_hsm2fsm_trginitialstate_constructor_exists():
    assert callable(jointPackage_HSM2FSM_TrgInitialState.__init__)


def test_jointpackage_hsm2fsm_trginitialstate_constructor_args():
    sig = inspect.signature(jointPackage_HSM2FSM_TrgInitialState.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_hsm2fsm_trgcompositestate_is_not_abstract():
    assert not inspect.isabstract(jointPackage_HSM2FSM_TrgCompositeState)


def test_jointpackage_hsm2fsm_trgcompositestate_constructor_exists():
    assert callable(jointPackage_HSM2FSM_TrgCompositeState.__init__)


def test_jointpackage_hsm2fsm_trgcompositestate_constructor_args():
    sig = inspect.signature(jointPackage_HSM2FSM_TrgCompositeState.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_hsm2fsm_jointmm_is_not_abstract():
    assert not inspect.isabstract(jointPackage_HSM2FSM_JointMM)


def test_jointpackage_hsm2fsm_jointmm_constructor_exists():
    assert callable(jointPackage_HSM2FSM_JointMM.__init__)


def test_jointpackage_hsm2fsm_jointmm_constructor_args():
    sig = inspect.signature(jointPackage_HSM2FSM_JointMM.__init__)
    params = list(sig.parameters.keys())



def test_srcstatemachine_is_not_abstract():
    assert not inspect.isabstract(SrcStateMachine)


def test_srcstatemachine_constructor_exists():
    assert callable(SrcStateMachine.__init__)


def test_srcstatemachine_constructor_args():
    sig = inspect.signature(SrcStateMachine.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_hsm2fsm_srcroot_is_not_abstract():
    assert not inspect.isabstract(jointPackage_HSM2FSM_SrcRoot)


def test_jointpackage_hsm2fsm_srcroot_constructor_exists():
    assert callable(jointPackage_HSM2FSM_SrcRoot.__init__)


def test_jointpackage_hsm2fsm_srcroot_constructor_args():
    sig = inspect.signature(jointPackage_HSM2FSM_SrcRoot.__init__)
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
jointPackage_HSM2FSM_TrgStateMachine_strategy = st.builds(
    jointPackage_HSM2FSM_TrgStateMachine,
    name=
        safe_text
)
TrgStateMachine_strategy = st.builds(
    TrgStateMachine,
)
jointPackage_HSM2FSM_TrgRoot_strategy = st.builds(
    jointPackage_HSM2FSM_TrgRoot,
)
SrcCompositeState_strategy = st.builds(
    SrcCompositeState,
)
jointPackage_HSM2FSM_SrcAbstractState_strategy = st.builds(
    jointPackage_HSM2FSM_SrcAbstractState,
    name=
        safe_text
)
jointPackage_HSM2FSM_SrcTransition_strategy = st.builds(
    jointPackage_HSM2FSM_SrcTransition,
    label=
        safe_text
)
SrcAbstractState_strategy = st.builds(
    SrcAbstractState,
)
jointPackage_HSM2FSM_SrcInitialState_strategy = st.builds(
    jointPackage_HSM2FSM_SrcInitialState,
)
jointPackage_HSM2FSM_SrcRegularState_strategy = st.builds(
    jointPackage_HSM2FSM_SrcRegularState,
)
jointPackage_HSM2FSM_SrcCompositeState_strategy = st.builds(
    jointPackage_HSM2FSM_SrcCompositeState,
)
SrcTransition_strategy = st.builds(
    SrcTransition,
)
jointPackage_HSM2FSM_SrcStateMachine_strategy = st.builds(
    jointPackage_HSM2FSM_SrcStateMachine,
    name=
        safe_text
)
jointPackage_HSM2FSM_TrgAbstractState_strategy = st.builds(
    jointPackage_HSM2FSM_TrgAbstractState,
    name=
        safe_text
)
jointPackage_HSM2FSM_TrgTransition_strategy = st.builds(
    jointPackage_HSM2FSM_TrgTransition,
    label=
        safe_text
)
TrgAbstractState_strategy = st.builds(
    TrgAbstractState,
)
jointPackage_HSM2FSM_TrgRegularState_strategy = st.builds(
    jointPackage_HSM2FSM_TrgRegularState,
)
jointPackage_HSM2FSM_TrgInitialState_strategy = st.builds(
    jointPackage_HSM2FSM_TrgInitialState,
)
jointPackage_HSM2FSM_TrgCompositeState_strategy = st.builds(
    jointPackage_HSM2FSM_TrgCompositeState,
)
jointPackage_HSM2FSM_JointMM_strategy = st.builds(
    jointPackage_HSM2FSM_JointMM,
)
SrcStateMachine_strategy = st.builds(
    SrcStateMachine,
)
jointPackage_HSM2FSM_SrcRoot_strategy = st.builds(
    jointPackage_HSM2FSM_SrcRoot,
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

@given(instance=jointPackage_HSM2FSM_TrgStateMachine_strategy)
@settings(max_examples=50)
def test_jointpackage_hsm2fsm_trgstatemachine_instantiation(instance):
    assert isinstance(instance, jointPackage_HSM2FSM_TrgStateMachine)



@given(instance=jointPackage_HSM2FSM_TrgStateMachine_strategy)
def test_jointpackage_hsm2fsm_trgstatemachine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=TrgStateMachine_strategy)
@settings(max_examples=50)
def test_trgstatemachine_instantiation(instance):
    assert isinstance(instance, TrgStateMachine)

@given(instance=jointPackage_HSM2FSM_TrgRoot_strategy)
@settings(max_examples=50)
def test_jointpackage_hsm2fsm_trgroot_instantiation(instance):
    assert isinstance(instance, jointPackage_HSM2FSM_TrgRoot)

@given(instance=SrcCompositeState_strategy)
@settings(max_examples=50)
def test_srccompositestate_instantiation(instance):
    assert isinstance(instance, SrcCompositeState)

@given(instance=jointPackage_HSM2FSM_SrcAbstractState_strategy)
@settings(max_examples=50)
def test_jointpackage_hsm2fsm_srcabstractstate_instantiation(instance):
    assert isinstance(instance, jointPackage_HSM2FSM_SrcAbstractState)



@given(instance=jointPackage_HSM2FSM_SrcAbstractState_strategy)
def test_jointpackage_hsm2fsm_srcabstractstate_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=jointPackage_HSM2FSM_SrcTransition_strategy)
@settings(max_examples=50)
def test_jointpackage_hsm2fsm_srctransition_instantiation(instance):
    assert isinstance(instance, jointPackage_HSM2FSM_SrcTransition)



@given(instance=jointPackage_HSM2FSM_SrcTransition_strategy)
def test_jointpackage_hsm2fsm_srctransition_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=SrcAbstractState_strategy)
@settings(max_examples=50)
def test_srcabstractstate_instantiation(instance):
    assert isinstance(instance, SrcAbstractState)

@given(instance=jointPackage_HSM2FSM_SrcInitialState_strategy)
@settings(max_examples=50)
def test_jointpackage_hsm2fsm_srcinitialstate_instantiation(instance):
    assert isinstance(instance, jointPackage_HSM2FSM_SrcInitialState)

@given(instance=jointPackage_HSM2FSM_SrcRegularState_strategy)
@settings(max_examples=50)
def test_jointpackage_hsm2fsm_srcregularstate_instantiation(instance):
    assert isinstance(instance, jointPackage_HSM2FSM_SrcRegularState)

@given(instance=jointPackage_HSM2FSM_SrcCompositeState_strategy)
@settings(max_examples=50)
def test_jointpackage_hsm2fsm_srccompositestate_instantiation(instance):
    assert isinstance(instance, jointPackage_HSM2FSM_SrcCompositeState)

@given(instance=SrcTransition_strategy)
@settings(max_examples=50)
def test_srctransition_instantiation(instance):
    assert isinstance(instance, SrcTransition)

@given(instance=jointPackage_HSM2FSM_SrcStateMachine_strategy)
@settings(max_examples=50)
def test_jointpackage_hsm2fsm_srcstatemachine_instantiation(instance):
    assert isinstance(instance, jointPackage_HSM2FSM_SrcStateMachine)



@given(instance=jointPackage_HSM2FSM_SrcStateMachine_strategy)
def test_jointpackage_hsm2fsm_srcstatemachine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=jointPackage_HSM2FSM_TrgAbstractState_strategy)
@settings(max_examples=50)
def test_jointpackage_hsm2fsm_trgabstractstate_instantiation(instance):
    assert isinstance(instance, jointPackage_HSM2FSM_TrgAbstractState)



@given(instance=jointPackage_HSM2FSM_TrgAbstractState_strategy)
def test_jointpackage_hsm2fsm_trgabstractstate_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=jointPackage_HSM2FSM_TrgTransition_strategy)
@settings(max_examples=50)
def test_jointpackage_hsm2fsm_trgtransition_instantiation(instance):
    assert isinstance(instance, jointPackage_HSM2FSM_TrgTransition)



@given(instance=jointPackage_HSM2FSM_TrgTransition_strategy)
def test_jointpackage_hsm2fsm_trgtransition_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=TrgAbstractState_strategy)
@settings(max_examples=50)
def test_trgabstractstate_instantiation(instance):
    assert isinstance(instance, TrgAbstractState)

@given(instance=jointPackage_HSM2FSM_TrgRegularState_strategy)
@settings(max_examples=50)
def test_jointpackage_hsm2fsm_trgregularstate_instantiation(instance):
    assert isinstance(instance, jointPackage_HSM2FSM_TrgRegularState)

@given(instance=jointPackage_HSM2FSM_TrgInitialState_strategy)
@settings(max_examples=50)
def test_jointpackage_hsm2fsm_trginitialstate_instantiation(instance):
    assert isinstance(instance, jointPackage_HSM2FSM_TrgInitialState)

@given(instance=jointPackage_HSM2FSM_TrgCompositeState_strategy)
@settings(max_examples=50)
def test_jointpackage_hsm2fsm_trgcompositestate_instantiation(instance):
    assert isinstance(instance, jointPackage_HSM2FSM_TrgCompositeState)

@given(instance=jointPackage_HSM2FSM_JointMM_strategy)
@settings(max_examples=50)
def test_jointpackage_hsm2fsm_jointmm_instantiation(instance):
    assert isinstance(instance, jointPackage_HSM2FSM_JointMM)

@given(instance=SrcStateMachine_strategy)
@settings(max_examples=50)
def test_srcstatemachine_instantiation(instance):
    assert isinstance(instance, SrcStateMachine)

@given(instance=jointPackage_HSM2FSM_SrcRoot_strategy)
@settings(max_examples=50)
def test_jointpackage_hsm2fsm_srcroot_instantiation(instance):
    assert isinstance(instance, jointPackage_HSM2FSM_SrcRoot)

@given(instance=TrgRoot_strategy)
@settings(max_examples=50)
def test_trgroot_instantiation(instance):
    assert isinstance(instance, TrgRoot)

@given(instance=SrcRoot_strategy)
@settings(max_examples=50)
def test_srcroot_instantiation(instance):
    assert isinstance(instance, SrcRoot)
