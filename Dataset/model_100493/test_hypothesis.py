import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    umlState_ExitRule,
    umlState_Namespace,
    umlState_StateMachine,
    umlState_QualifiedName,
    umlState_DoRule,
    umlState_EntryRule,
    umlState_SubmachineRule,
    umlState_StateRule,
    BehaviorKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_umlstate_exitrule_is_not_abstract():
    assert not inspect.isabstract(umlState_ExitRule)


def test_umlstate_exitrule_constructor_exists():
    assert callable(umlState_ExitRule.__init__)


def test_umlstate_exitrule_constructor_args():
    sig = inspect.signature(umlState_ExitRule.__init__)
    params = list(sig.parameters.keys())
    assert "behaviorName" in params, "Missing parameter 'behaviorName'"
    assert "kind" in params, "Missing parameter 'kind'"

def test_umlstate_exitrule_has_behaviorName():
    assert hasattr(umlState_ExitRule, "behaviorName")
    descriptor = None
    for klass in umlState_ExitRule.__mro__:
        if "behaviorName" in klass.__dict__:
            descriptor = klass.__dict__["behaviorName"]
            break
    assert isinstance(descriptor, property)

def test_umlstate_exitrule_has_kind():
    assert hasattr(umlState_ExitRule, "kind")
    descriptor = None
    for klass in umlState_ExitRule.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_umlstate_namespace_is_not_abstract():
    assert not inspect.isabstract(umlState_Namespace)


def test_umlstate_namespace_constructor_exists():
    assert callable(umlState_Namespace.__init__)


def test_umlstate_namespace_constructor_args():
    sig = inspect.signature(umlState_Namespace.__init__)
    params = list(sig.parameters.keys())



def test_umlstate_statemachine_is_not_abstract():
    assert not inspect.isabstract(umlState_StateMachine)


def test_umlstate_statemachine_constructor_exists():
    assert callable(umlState_StateMachine.__init__)


def test_umlstate_statemachine_constructor_args():
    sig = inspect.signature(umlState_StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_umlstate_qualifiedname_is_not_abstract():
    assert not inspect.isabstract(umlState_QualifiedName)


def test_umlstate_qualifiedname_constructor_exists():
    assert callable(umlState_QualifiedName.__init__)


def test_umlstate_qualifiedname_constructor_args():
    sig = inspect.signature(umlState_QualifiedName.__init__)
    params = list(sig.parameters.keys())



def test_umlstate_dorule_is_not_abstract():
    assert not inspect.isabstract(umlState_DoRule)


def test_umlstate_dorule_constructor_exists():
    assert callable(umlState_DoRule.__init__)


def test_umlstate_dorule_constructor_args():
    sig = inspect.signature(umlState_DoRule.__init__)
    params = list(sig.parameters.keys())
    assert "behaviorName" in params, "Missing parameter 'behaviorName'"
    assert "kind" in params, "Missing parameter 'kind'"

def test_umlstate_dorule_has_behaviorName():
    assert hasattr(umlState_DoRule, "behaviorName")
    descriptor = None
    for klass in umlState_DoRule.__mro__:
        if "behaviorName" in klass.__dict__:
            descriptor = klass.__dict__["behaviorName"]
            break
    assert isinstance(descriptor, property)

def test_umlstate_dorule_has_kind():
    assert hasattr(umlState_DoRule, "kind")
    descriptor = None
    for klass in umlState_DoRule.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_umlstate_entryrule_is_not_abstract():
    assert not inspect.isabstract(umlState_EntryRule)


def test_umlstate_entryrule_constructor_exists():
    assert callable(umlState_EntryRule.__init__)


def test_umlstate_entryrule_constructor_args():
    sig = inspect.signature(umlState_EntryRule.__init__)
    params = list(sig.parameters.keys())
    assert "behaviorName" in params, "Missing parameter 'behaviorName'"
    assert "kind" in params, "Missing parameter 'kind'"

def test_umlstate_entryrule_has_behaviorName():
    assert hasattr(umlState_EntryRule, "behaviorName")
    descriptor = None
    for klass in umlState_EntryRule.__mro__:
        if "behaviorName" in klass.__dict__:
            descriptor = klass.__dict__["behaviorName"]
            break
    assert isinstance(descriptor, property)

def test_umlstate_entryrule_has_kind():
    assert hasattr(umlState_EntryRule, "kind")
    descriptor = None
    for klass in umlState_EntryRule.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_umlstate_submachinerule_is_not_abstract():
    assert not inspect.isabstract(umlState_SubmachineRule)


def test_umlstate_submachinerule_constructor_exists():
    assert callable(umlState_SubmachineRule.__init__)


def test_umlstate_submachinerule_constructor_args():
    sig = inspect.signature(umlState_SubmachineRule.__init__)
    params = list(sig.parameters.keys())



def test_umlstate_staterule_is_not_abstract():
    assert not inspect.isabstract(umlState_StateRule)


def test_umlstate_staterule_constructor_exists():
    assert callable(umlState_StateRule.__init__)


def test_umlstate_staterule_constructor_args():
    sig = inspect.signature(umlState_StateRule.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_umlstate_staterule_has_name():
    assert hasattr(umlState_StateRule, "name")
    descriptor = None
    for klass in umlState_StateRule.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_behaviorkind_exists():
    # Check that the Enumeration exists
    assert BehaviorKind is not None

def test_behaviorkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BehaviorKind]
    expected_literals = [
        "ACTIVITY",
        "OPAQUE_BEHAVIOR",
        "STATE_MACHINE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BehaviorKind"


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
umlState_ExitRule_strategy = st.builds(
    umlState_ExitRule,
    behaviorName=
        safe_text,
    kind=
        safe_text
)
umlState_Namespace_strategy = st.builds(
    umlState_Namespace,
)
umlState_StateMachine_strategy = st.builds(
    umlState_StateMachine,
)
umlState_QualifiedName_strategy = st.builds(
    umlState_QualifiedName,
)
umlState_DoRule_strategy = st.builds(
    umlState_DoRule,
    behaviorName=
        safe_text,
    kind=
        safe_text
)
umlState_EntryRule_strategy = st.builds(
    umlState_EntryRule,
    behaviorName=
        safe_text,
    kind=
        safe_text
)
umlState_SubmachineRule_strategy = st.builds(
    umlState_SubmachineRule,
)
umlState_StateRule_strategy = st.builds(
    umlState_StateRule,
    name=
        safe_text
)

@given(instance=umlState_ExitRule_strategy)
@settings(max_examples=50)
def test_umlstate_exitrule_instantiation(instance):
    assert isinstance(instance, umlState_ExitRule)



@given(instance=umlState_ExitRule_strategy)
def test_umlstate_exitrule_behaviorName_setter(instance):
    original = instance.behaviorName
    instance.behaviorName = original
    assert instance.behaviorName == original



@given(instance=umlState_ExitRule_strategy)
def test_umlstate_exitrule_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=umlState_Namespace_strategy)
@settings(max_examples=50)
def test_umlstate_namespace_instantiation(instance):
    assert isinstance(instance, umlState_Namespace)

@given(instance=umlState_StateMachine_strategy)
@settings(max_examples=50)
def test_umlstate_statemachine_instantiation(instance):
    assert isinstance(instance, umlState_StateMachine)

@given(instance=umlState_QualifiedName_strategy)
@settings(max_examples=50)
def test_umlstate_qualifiedname_instantiation(instance):
    assert isinstance(instance, umlState_QualifiedName)

@given(instance=umlState_DoRule_strategy)
@settings(max_examples=50)
def test_umlstate_dorule_instantiation(instance):
    assert isinstance(instance, umlState_DoRule)



@given(instance=umlState_DoRule_strategy)
def test_umlstate_dorule_behaviorName_setter(instance):
    original = instance.behaviorName
    instance.behaviorName = original
    assert instance.behaviorName == original



@given(instance=umlState_DoRule_strategy)
def test_umlstate_dorule_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=umlState_EntryRule_strategy)
@settings(max_examples=50)
def test_umlstate_entryrule_instantiation(instance):
    assert isinstance(instance, umlState_EntryRule)



@given(instance=umlState_EntryRule_strategy)
def test_umlstate_entryrule_behaviorName_setter(instance):
    original = instance.behaviorName
    instance.behaviorName = original
    assert instance.behaviorName == original



@given(instance=umlState_EntryRule_strategy)
def test_umlstate_entryrule_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=umlState_SubmachineRule_strategy)
@settings(max_examples=50)
def test_umlstate_submachinerule_instantiation(instance):
    assert isinstance(instance, umlState_SubmachineRule)

@given(instance=umlState_StateRule_strategy)
@settings(max_examples=50)
def test_umlstate_staterule_instantiation(instance):
    assert isinstance(instance, umlState_StateRule)



@given(instance=umlState_StateRule_strategy)
def test_umlstate_staterule_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
