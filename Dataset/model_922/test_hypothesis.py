import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    spem_WorkSequence,
    spem_Activity,
    spem_Process,
    WorkSequenceKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_spem_worksequence_is_not_abstract():
    assert not inspect.isabstract(spem_WorkSequence)


def test_spem_worksequence_constructor_exists():
    assert callable(spem_WorkSequence.__init__)


def test_spem_worksequence_constructor_args():
    sig = inspect.signature(spem_WorkSequence.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_spem_worksequence_has_kind():
    assert hasattr(spem_WorkSequence, "kind")
    descriptor = None
    for klass in spem_WorkSequence.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_spem_activity_is_not_abstract():
    assert not inspect.isabstract(spem_Activity)


def test_spem_activity_constructor_exists():
    assert callable(spem_Activity.__init__)


def test_spem_activity_constructor_args():
    sig = inspect.signature(spem_Activity.__init__)
    params = list(sig.parameters.keys())
    assert "durationmax" in params, "Missing parameter 'durationmax'"
    assert "name" in params, "Missing parameter 'name'"
    assert "durationmin" in params, "Missing parameter 'durationmin'"

def test_spem_activity_has_durationmax():
    assert hasattr(spem_Activity, "durationmax")
    descriptor = None
    for klass in spem_Activity.__mro__:
        if "durationmax" in klass.__dict__:
            descriptor = klass.__dict__["durationmax"]
            break
    assert isinstance(descriptor, property)

def test_spem_activity_has_name():
    assert hasattr(spem_Activity, "name")
    descriptor = None
    for klass in spem_Activity.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_spem_activity_has_durationmin():
    assert hasattr(spem_Activity, "durationmin")
    descriptor = None
    for klass in spem_Activity.__mro__:
        if "durationmin" in klass.__dict__:
            descriptor = klass.__dict__["durationmin"]
            break
    assert isinstance(descriptor, property)



def test_spem_process_is_not_abstract():
    assert not inspect.isabstract(spem_Process)


def test_spem_process_constructor_exists():
    assert callable(spem_Process.__init__)


def test_spem_process_constructor_args():
    sig = inspect.signature(spem_Process.__init__)
    params = list(sig.parameters.keys())

def test_worksequencekind_exists():
    # Check that the Enumeration exists
    assert WorkSequenceKind is not None

def test_worksequencekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in WorkSequenceKind]
    expected_literals = [
        "finishToFinish",
        "finishToStart",
        "startToFinish",
        "startToStart",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in WorkSequenceKind"


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
spem_WorkSequence_strategy = st.builds(
    spem_WorkSequence,
    kind=
        safe_text
)
spem_Activity_strategy = st.builds(
    spem_Activity,
    durationmax=
        st.integers(),
    name=
        safe_text,
    durationmin=
        st.integers()
)
spem_Process_strategy = st.builds(
    spem_Process,
)

@given(instance=spem_WorkSequence_strategy)
@settings(max_examples=50)
def test_spem_worksequence_instantiation(instance):
    assert isinstance(instance, spem_WorkSequence)



@given(instance=spem_WorkSequence_strategy)
def test_spem_worksequence_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=spem_Activity_strategy)
@settings(max_examples=50)
def test_spem_activity_instantiation(instance):
    assert isinstance(instance, spem_Activity)



@given(instance=spem_Activity_strategy)
def test_spem_activity_durationmax_setter(instance):
    original = instance.durationmax
    instance.durationmax = original
    assert instance.durationmax == original



@given(instance=spem_Activity_strategy)
def test_spem_activity_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=spem_Activity_strategy)
def test_spem_activity_durationmin_setter(instance):
    original = instance.durationmin
    instance.durationmin = original
    assert instance.durationmin == original

@given(instance=spem_Process_strategy)
@settings(max_examples=50)
def test_spem_process_instantiation(instance):
    assert isinstance(instance, spem_Process)
