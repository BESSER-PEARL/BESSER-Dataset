import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    spem::WorkSequence,
    spem::Activity,
    spem::Process,
    WorkSequenceKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_spem::worksequence_is_not_abstract():
    assert not inspect.isabstract(spem::WorkSequence)


def test_spem::worksequence_constructor_exists():
    assert callable(spem::WorkSequence.__init__)


def test_spem::worksequence_constructor_args():
    sig = inspect.signature(spem::WorkSequence.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_spem::worksequence_has_kind():
    assert hasattr(spem::WorkSequence, "kind")
    descriptor = None
    for klass in spem::WorkSequence.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_spem::activity_is_not_abstract():
    assert not inspect.isabstract(spem::Activity)


def test_spem::activity_constructor_exists():
    assert callable(spem::Activity.__init__)


def test_spem::activity_constructor_args():
    sig = inspect.signature(spem::Activity.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "durationmax" in params, "Missing parameter 'durationmax'"
    assert "durationmin" in params, "Missing parameter 'durationmin'"

def test_spem::activity_has_name():
    assert hasattr(spem::Activity, "name")
    descriptor = None
    for klass in spem::Activity.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_spem::activity_has_durationmax():
    assert hasattr(spem::Activity, "durationmax")
    descriptor = None
    for klass in spem::Activity.__mro__:
        if "durationmax" in klass.__dict__:
            descriptor = klass.__dict__["durationmax"]
            break
    assert isinstance(descriptor, property)

def test_spem::activity_has_durationmin():
    assert hasattr(spem::Activity, "durationmin")
    descriptor = None
    for klass in spem::Activity.__mro__:
        if "durationmin" in klass.__dict__:
            descriptor = klass.__dict__["durationmin"]
            break
    assert isinstance(descriptor, property)



def test_spem::process_is_not_abstract():
    assert not inspect.isabstract(spem::Process)


def test_spem::process_constructor_exists():
    assert callable(spem::Process.__init__)


def test_spem::process_constructor_args():
    sig = inspect.signature(spem::Process.__init__)
    params = list(sig.parameters.keys())

def test_worksequencekind_exists():
    # Check that the Enumeration exists
    assert WorkSequenceKind is not None

def test_worksequencekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in WorkSequenceKind]
    expected_literals = [
        "startToStart",
        "finishToFinish",
        "startToFinish",
        "finishToStart",
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
spem::WorkSequence_strategy = st.builds(
    spem::WorkSequence,
    kind=
        safe_text
)
spem::Activity_strategy = st.builds(
    spem::Activity,
    name=
        safe_text,
    durationmax=
        st.integers(),
    durationmin=
        st.integers()
)
spem::Process_strategy = st.builds(
    spem::Process,
)

@given(instance=spem::WorkSequence_strategy)
@settings(max_examples=50)
def test_spem::worksequence_instantiation(instance):
    assert isinstance(instance, spem::WorkSequence)

@given(instance=spem::WorkSequence_strategy)
def test_spem::worksequence_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=spem::WorkSequence_strategy)
def test_spem::worksequence_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=spem::Activity_strategy)
@settings(max_examples=50)
def test_spem::activity_instantiation(instance):
    assert isinstance(instance, spem::Activity)

@given(instance=spem::Activity_strategy)
def test_spem::activity_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=spem::Activity_strategy)
def test_spem::activity_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=spem::Activity_strategy)
def test_spem::activity_durationmax_type(instance):
    assert isinstance(instance.durationmax, int)


@given(instance=spem::Activity_strategy)
def test_spem::activity_durationmax_setter(instance):
    original = instance.durationmax
    instance.durationmax = original
    assert instance.durationmax == original

@given(instance=spem::Activity_strategy)
def test_spem::activity_durationmin_type(instance):
    assert isinstance(instance.durationmin, int)


@given(instance=spem::Activity_strategy)
def test_spem::activity_durationmin_setter(instance):
    original = instance.durationmin
    instance.durationmin = original
    assert instance.durationmin == original

@given(instance=spem::Process_strategy)
@settings(max_examples=50)
def test_spem::process_instantiation(instance):
    assert isinstance(instance, spem::Process)
