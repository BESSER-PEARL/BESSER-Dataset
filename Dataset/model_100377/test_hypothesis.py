import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    metaCompo_mTransition,
    metaCompo_mComp,
    metaCompo_mState,
    metaCompo_mVariable,
    metaCompo_mFSM,
    metaCompo_mPort,
    mIO,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_metacompo_mtransition_is_not_abstract():
    assert not inspect.isabstract(metaCompo_mTransition)


def test_metacompo_mtransition_constructor_exists():
    assert callable(metaCompo_mTransition.__init__)


def test_metacompo_mtransition_constructor_args():
    sig = inspect.signature(metaCompo_mTransition.__init__)
    params = list(sig.parameters.keys())
    assert "action" in params, "Missing parameter 'action'"
    assert "guard" in params, "Missing parameter 'guard'"
    assert "name" in params, "Missing parameter 'name'"
    assert "triggerExp" in params, "Missing parameter 'triggerExp'"

def test_metacompo_mtransition_has_action():
    assert hasattr(metaCompo_mTransition, "action")
    descriptor = None
    for klass in metaCompo_mTransition.__mro__:
        if "action" in klass.__dict__:
            descriptor = klass.__dict__["action"]
            break
    assert isinstance(descriptor, property)

def test_metacompo_mtransition_has_guard():
    assert hasattr(metaCompo_mTransition, "guard")
    descriptor = None
    for klass in metaCompo_mTransition.__mro__:
        if "guard" in klass.__dict__:
            descriptor = klass.__dict__["guard"]
            break
    assert isinstance(descriptor, property)

def test_metacompo_mtransition_has_name():
    assert hasattr(metaCompo_mTransition, "name")
    descriptor = None
    for klass in metaCompo_mTransition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_metacompo_mtransition_has_triggerExp():
    assert hasattr(metaCompo_mTransition, "triggerExp")
    descriptor = None
    for klass in metaCompo_mTransition.__mro__:
        if "triggerExp" in klass.__dict__:
            descriptor = klass.__dict__["triggerExp"]
            break
    assert isinstance(descriptor, property)



def test_metacompo_mcomp_is_not_abstract():
    assert not inspect.isabstract(metaCompo_mComp)


def test_metacompo_mcomp_constructor_exists():
    assert callable(metaCompo_mComp.__init__)


def test_metacompo_mcomp_constructor_args():
    sig = inspect.signature(metaCompo_mComp.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"

def test_metacompo_mcomp_has_type():
    assert hasattr(metaCompo_mComp, "type")
    descriptor = None
    for klass in metaCompo_mComp.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_metacompo_mcomp_has_name():
    assert hasattr(metaCompo_mComp, "name")
    descriptor = None
    for klass in metaCompo_mComp.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_metacompo_mstate_is_not_abstract():
    assert not inspect.isabstract(metaCompo_mState)


def test_metacompo_mstate_constructor_exists():
    assert callable(metaCompo_mState.__init__)


def test_metacompo_mstate_constructor_args():
    sig = inspect.signature(metaCompo_mState.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_metacompo_mstate_has_name():
    assert hasattr(metaCompo_mState, "name")
    descriptor = None
    for klass in metaCompo_mState.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_metacompo_mvariable_is_not_abstract():
    assert not inspect.isabstract(metaCompo_mVariable)


def test_metacompo_mvariable_constructor_exists():
    assert callable(metaCompo_mVariable.__init__)


def test_metacompo_mvariable_constructor_args():
    sig = inspect.signature(metaCompo_mVariable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"

def test_metacompo_mvariable_has_name():
    assert hasattr(metaCompo_mVariable, "name")
    descriptor = None
    for klass in metaCompo_mVariable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_metacompo_mvariable_has_type():
    assert hasattr(metaCompo_mVariable, "type")
    descriptor = None
    for klass in metaCompo_mVariable.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_metacompo_mfsm_is_not_abstract():
    assert not inspect.isabstract(metaCompo_mFSM)


def test_metacompo_mfsm_constructor_exists():
    assert callable(metaCompo_mFSM.__init__)


def test_metacompo_mfsm_constructor_args():
    sig = inspect.signature(metaCompo_mFSM.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_metacompo_mfsm_has_name():
    assert hasattr(metaCompo_mFSM, "name")
    descriptor = None
    for klass in metaCompo_mFSM.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_metacompo_mport_is_not_abstract():
    assert not inspect.isabstract(metaCompo_mPort)


def test_metacompo_mport_constructor_exists():
    assert callable(metaCompo_mPort.__init__)


def test_metacompo_mport_constructor_args():
    sig = inspect.signature(metaCompo_mPort.__init__)
    params = list(sig.parameters.keys())
    assert "io" in params, "Missing parameter 'io'"
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"

def test_metacompo_mport_has_io():
    assert hasattr(metaCompo_mPort, "io")
    descriptor = None
    for klass in metaCompo_mPort.__mro__:
        if "io" in klass.__dict__:
            descriptor = klass.__dict__["io"]
            break
    assert isinstance(descriptor, property)

def test_metacompo_mport_has_name():
    assert hasattr(metaCompo_mPort, "name")
    descriptor = None
    for klass in metaCompo_mPort.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_metacompo_mport_has_type():
    assert hasattr(metaCompo_mPort, "type")
    descriptor = None
    for klass in metaCompo_mPort.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_mio_exists():
    # Check that the Enumeration exists
    assert mIO is not None

def test_mio_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in mIO]
    expected_literals = [
        "out",
        "in_",
        "inout",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in mIO"


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
metaCompo_mTransition_strategy = st.builds(
    metaCompo_mTransition,
    action=
        safe_text,
    guard=
        safe_text,
    name=
        safe_text,
    triggerExp=
        safe_text
)
metaCompo_mComp_strategy = st.builds(
    metaCompo_mComp,
    type=
        safe_text,
    name=
        safe_text
)
metaCompo_mState_strategy = st.builds(
    metaCompo_mState,
    name=
        safe_text
)
metaCompo_mVariable_strategy = st.builds(
    metaCompo_mVariable,
    name=
        safe_text,
    type=
        safe_text
)
metaCompo_mFSM_strategy = st.builds(
    metaCompo_mFSM,
    name=
        safe_text
)
metaCompo_mPort_strategy = st.builds(
    metaCompo_mPort,
    io=
        safe_text,
    name=
        safe_text,
    type=
        safe_text
)

@given(instance=metaCompo_mTransition_strategy)
@settings(max_examples=50)
def test_metacompo_mtransition_instantiation(instance):
    assert isinstance(instance, metaCompo_mTransition)



@given(instance=metaCompo_mTransition_strategy)
def test_metacompo_mtransition_action_setter(instance):
    original = instance.action
    instance.action = original
    assert instance.action == original



@given(instance=metaCompo_mTransition_strategy)
def test_metacompo_mtransition_guard_setter(instance):
    original = instance.guard
    instance.guard = original
    assert instance.guard == original



@given(instance=metaCompo_mTransition_strategy)
def test_metacompo_mtransition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=metaCompo_mTransition_strategy)
def test_metacompo_mtransition_triggerExp_setter(instance):
    original = instance.triggerExp
    instance.triggerExp = original
    assert instance.triggerExp == original

@given(instance=metaCompo_mComp_strategy)
@settings(max_examples=50)
def test_metacompo_mcomp_instantiation(instance):
    assert isinstance(instance, metaCompo_mComp)



@given(instance=metaCompo_mComp_strategy)
def test_metacompo_mcomp_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=metaCompo_mComp_strategy)
def test_metacompo_mcomp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=metaCompo_mState_strategy)
@settings(max_examples=50)
def test_metacompo_mstate_instantiation(instance):
    assert isinstance(instance, metaCompo_mState)



@given(instance=metaCompo_mState_strategy)
def test_metacompo_mstate_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=metaCompo_mVariable_strategy)
@settings(max_examples=50)
def test_metacompo_mvariable_instantiation(instance):
    assert isinstance(instance, metaCompo_mVariable)



@given(instance=metaCompo_mVariable_strategy)
def test_metacompo_mvariable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=metaCompo_mVariable_strategy)
def test_metacompo_mvariable_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=metaCompo_mFSM_strategy)
@settings(max_examples=50)
def test_metacompo_mfsm_instantiation(instance):
    assert isinstance(instance, metaCompo_mFSM)



@given(instance=metaCompo_mFSM_strategy)
def test_metacompo_mfsm_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=metaCompo_mPort_strategy)
@settings(max_examples=50)
def test_metacompo_mport_instantiation(instance):
    assert isinstance(instance, metaCompo_mPort)



@given(instance=metaCompo_mPort_strategy)
def test_metacompo_mport_io_setter(instance):
    original = instance.io
    instance.io = original
    assert instance.io == original



@given(instance=metaCompo_mPort_strategy)
def test_metacompo_mport_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=metaCompo_mPort_strategy)
def test_metacompo_mport_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original
