import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    metaCompo::mTransition,
    metaCompo::mComp,
    metaCompo::mState,
    metaCompo::mVariable,
    metaCompo::mFSM,
    metaCompo::mPort,
    mIO,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_metacompo::mtransition_is_not_abstract():
    assert not inspect.isabstract(metaCompo::mTransition)


def test_metacompo::mtransition_constructor_exists():
    assert callable(metaCompo::mTransition.__init__)


def test_metacompo::mtransition_constructor_args():
    sig = inspect.signature(metaCompo::mTransition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "guard" in params, "Missing parameter 'guard'"
    assert "triggerExp" in params, "Missing parameter 'triggerExp'"
    assert "action" in params, "Missing parameter 'action'"

def test_metacompo::mtransition_has_name():
    assert hasattr(metaCompo::mTransition, "name")
    descriptor = None
    for klass in metaCompo::mTransition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_metacompo::mtransition_has_guard():
    assert hasattr(metaCompo::mTransition, "guard")
    descriptor = None
    for klass in metaCompo::mTransition.__mro__:
        if "guard" in klass.__dict__:
            descriptor = klass.__dict__["guard"]
            break
    assert isinstance(descriptor, property)

def test_metacompo::mtransition_has_triggerExp():
    assert hasattr(metaCompo::mTransition, "triggerExp")
    descriptor = None
    for klass in metaCompo::mTransition.__mro__:
        if "triggerExp" in klass.__dict__:
            descriptor = klass.__dict__["triggerExp"]
            break
    assert isinstance(descriptor, property)

def test_metacompo::mtransition_has_action():
    assert hasattr(metaCompo::mTransition, "action")
    descriptor = None
    for klass in metaCompo::mTransition.__mro__:
        if "action" in klass.__dict__:
            descriptor = klass.__dict__["action"]
            break
    assert isinstance(descriptor, property)



def test_metacompo::mcomp_is_not_abstract():
    assert not inspect.isabstract(metaCompo::mComp)


def test_metacompo::mcomp_constructor_exists():
    assert callable(metaCompo::mComp.__init__)


def test_metacompo::mcomp_constructor_args():
    sig = inspect.signature(metaCompo::mComp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"

def test_metacompo::mcomp_has_name():
    assert hasattr(metaCompo::mComp, "name")
    descriptor = None
    for klass in metaCompo::mComp.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_metacompo::mcomp_has_type():
    assert hasattr(metaCompo::mComp, "type")
    descriptor = None
    for klass in metaCompo::mComp.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_metacompo::mstate_is_not_abstract():
    assert not inspect.isabstract(metaCompo::mState)


def test_metacompo::mstate_constructor_exists():
    assert callable(metaCompo::mState.__init__)


def test_metacompo::mstate_constructor_args():
    sig = inspect.signature(metaCompo::mState.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_metacompo::mstate_has_name():
    assert hasattr(metaCompo::mState, "name")
    descriptor = None
    for klass in metaCompo::mState.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_metacompo::mvariable_is_not_abstract():
    assert not inspect.isabstract(metaCompo::mVariable)


def test_metacompo::mvariable_constructor_exists():
    assert callable(metaCompo::mVariable.__init__)


def test_metacompo::mvariable_constructor_args():
    sig = inspect.signature(metaCompo::mVariable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"

def test_metacompo::mvariable_has_name():
    assert hasattr(metaCompo::mVariable, "name")
    descriptor = None
    for klass in metaCompo::mVariable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_metacompo::mvariable_has_type():
    assert hasattr(metaCompo::mVariable, "type")
    descriptor = None
    for klass in metaCompo::mVariable.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_metacompo::mfsm_is_not_abstract():
    assert not inspect.isabstract(metaCompo::mFSM)


def test_metacompo::mfsm_constructor_exists():
    assert callable(metaCompo::mFSM.__init__)


def test_metacompo::mfsm_constructor_args():
    sig = inspect.signature(metaCompo::mFSM.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_metacompo::mfsm_has_name():
    assert hasattr(metaCompo::mFSM, "name")
    descriptor = None
    for klass in metaCompo::mFSM.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_metacompo::mport_is_not_abstract():
    assert not inspect.isabstract(metaCompo::mPort)


def test_metacompo::mport_constructor_exists():
    assert callable(metaCompo::mPort.__init__)


def test_metacompo::mport_constructor_args():
    sig = inspect.signature(metaCompo::mPort.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"
    assert "io" in params, "Missing parameter 'io'"

def test_metacompo::mport_has_type():
    assert hasattr(metaCompo::mPort, "type")
    descriptor = None
    for klass in metaCompo::mPort.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_metacompo::mport_has_name():
    assert hasattr(metaCompo::mPort, "name")
    descriptor = None
    for klass in metaCompo::mPort.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_metacompo::mport_has_io():
    assert hasattr(metaCompo::mPort, "io")
    descriptor = None
    for klass in metaCompo::mPort.__mro__:
        if "io" in klass.__dict__:
            descriptor = klass.__dict__["io"]
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
metaCompo::mTransition_strategy = st.builds(
    metaCompo::mTransition,
    name=
        safe_text,
    guard=
        safe_text,
    triggerExp=
        safe_text,
    action=
        safe_text
)
metaCompo::mComp_strategy = st.builds(
    metaCompo::mComp,
    name=
        safe_text,
    type=
        safe_text
)
metaCompo::mState_strategy = st.builds(
    metaCompo::mState,
    name=
        safe_text
)
metaCompo::mVariable_strategy = st.builds(
    metaCompo::mVariable,
    name=
        safe_text,
    type=
        safe_text
)
metaCompo::mFSM_strategy = st.builds(
    metaCompo::mFSM,
    name=
        safe_text
)
metaCompo::mPort_strategy = st.builds(
    metaCompo::mPort,
    type=
        safe_text,
    name=
        safe_text,
    io=
        safe_text
)

@given(instance=metaCompo::mTransition_strategy)
@settings(max_examples=50)
def test_metacompo::mtransition_instantiation(instance):
    assert isinstance(instance, metaCompo::mTransition)

@given(instance=metaCompo::mTransition_strategy)
def test_metacompo::mtransition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=metaCompo::mTransition_strategy)
def test_metacompo::mtransition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=metaCompo::mTransition_strategy)
def test_metacompo::mtransition_guard_type(instance):
    assert isinstance(instance.guard, str)


@given(instance=metaCompo::mTransition_strategy)
def test_metacompo::mtransition_guard_setter(instance):
    original = instance.guard
    instance.guard = original
    assert instance.guard == original

@given(instance=metaCompo::mTransition_strategy)
def test_metacompo::mtransition_triggerExp_type(instance):
    assert isinstance(instance.triggerExp, str)


@given(instance=metaCompo::mTransition_strategy)
def test_metacompo::mtransition_triggerExp_setter(instance):
    original = instance.triggerExp
    instance.triggerExp = original
    assert instance.triggerExp == original

@given(instance=metaCompo::mTransition_strategy)
def test_metacompo::mtransition_action_type(instance):
    assert isinstance(instance.action, str)


@given(instance=metaCompo::mTransition_strategy)
def test_metacompo::mtransition_action_setter(instance):
    original = instance.action
    instance.action = original
    assert instance.action == original

@given(instance=metaCompo::mComp_strategy)
@settings(max_examples=50)
def test_metacompo::mcomp_instantiation(instance):
    assert isinstance(instance, metaCompo::mComp)

@given(instance=metaCompo::mComp_strategy)
def test_metacompo::mcomp_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=metaCompo::mComp_strategy)
def test_metacompo::mcomp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=metaCompo::mComp_strategy)
def test_metacompo::mcomp_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=metaCompo::mComp_strategy)
def test_metacompo::mcomp_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=metaCompo::mState_strategy)
@settings(max_examples=50)
def test_metacompo::mstate_instantiation(instance):
    assert isinstance(instance, metaCompo::mState)

@given(instance=metaCompo::mState_strategy)
def test_metacompo::mstate_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=metaCompo::mState_strategy)
def test_metacompo::mstate_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=metaCompo::mVariable_strategy)
@settings(max_examples=50)
def test_metacompo::mvariable_instantiation(instance):
    assert isinstance(instance, metaCompo::mVariable)

@given(instance=metaCompo::mVariable_strategy)
def test_metacompo::mvariable_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=metaCompo::mVariable_strategy)
def test_metacompo::mvariable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=metaCompo::mVariable_strategy)
def test_metacompo::mvariable_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=metaCompo::mVariable_strategy)
def test_metacompo::mvariable_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=metaCompo::mFSM_strategy)
@settings(max_examples=50)
def test_metacompo::mfsm_instantiation(instance):
    assert isinstance(instance, metaCompo::mFSM)

@given(instance=metaCompo::mFSM_strategy)
def test_metacompo::mfsm_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=metaCompo::mFSM_strategy)
def test_metacompo::mfsm_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=metaCompo::mPort_strategy)
@settings(max_examples=50)
def test_metacompo::mport_instantiation(instance):
    assert isinstance(instance, metaCompo::mPort)

@given(instance=metaCompo::mPort_strategy)
def test_metacompo::mport_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=metaCompo::mPort_strategy)
def test_metacompo::mport_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=metaCompo::mPort_strategy)
def test_metacompo::mport_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=metaCompo::mPort_strategy)
def test_metacompo::mport_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=metaCompo::mPort_strategy)
def test_metacompo::mport_io_type(instance):
    assert isinstance(instance.io, str)


@given(instance=metaCompo::mPort_strategy)
def test_metacompo::mport_io_setter(instance):
    original = instance.io
    instance.io = original
    assert instance.io == original
