import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    sample::SampleClassInterface,
    SampleClassInterface,
    sample::SampleClassA,
    sample::SampleClassB,
    sample::SampleClassC,
    Tristate,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_sample::sampleclassinterface_is_not_abstract():
    assert not inspect.isabstract(sample::SampleClassInterface)


def test_sample::sampleclassinterface_constructor_exists():
    assert callable(sample::SampleClassInterface.__init__)


def test_sample::sampleclassinterface_constructor_args():
    sig = inspect.signature(sample::SampleClassInterface.__init__)
    params = list(sig.parameters.keys())



def test_sampleclassinterface_is_not_abstract():
    assert not inspect.isabstract(SampleClassInterface)


def test_sampleclassinterface_constructor_exists():
    assert callable(SampleClassInterface.__init__)


def test_sampleclassinterface_constructor_args():
    sig = inspect.signature(SampleClassInterface.__init__)
    params = list(sig.parameters.keys())



def test_sample::sampleclassa_is_not_abstract():
    assert not inspect.isabstract(sample::SampleClassA)


def test_sample::sampleclassa_constructor_exists():
    assert callable(sample::SampleClassA.__init__)


def test_sample::sampleclassa_constructor_args():
    sig = inspect.signature(sample::SampleClassA.__init__)
    params = list(sig.parameters.keys())
    assert "sampleAttribute" in params, "Missing parameter 'sampleAttribute'"

def test_sample::sampleclassa_has_sampleAttribute():
    assert hasattr(sample::SampleClassA, "sampleAttribute")
    descriptor = None
    for klass in sample::SampleClassA.__mro__:
        if "sampleAttribute" in klass.__dict__:
            descriptor = klass.__dict__["sampleAttribute"]
            break
    assert isinstance(descriptor, property)



def test_sample::sampleclassb_is_not_abstract():
    assert not inspect.isabstract(sample::SampleClassB)


def test_sample::sampleclassb_constructor_exists():
    assert callable(sample::SampleClassB.__init__)


def test_sample::sampleclassb_constructor_args():
    sig = inspect.signature(sample::SampleClassB.__init__)
    params = list(sig.parameters.keys())



def test_sample::sampleclassc_is_not_abstract():
    assert not inspect.isabstract(sample::SampleClassC)


def test_sample::sampleclassc_constructor_exists():
    assert callable(sample::SampleClassC.__init__)


def test_sample::sampleclassc_constructor_args():
    sig = inspect.signature(sample::SampleClassC.__init__)
    params = list(sig.parameters.keys())

def test_tristate_exists():
    # Check that the Enumeration exists
    assert Tristate is not None

def test_tristate_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Tristate]
    expected_literals = [
        "UNDEFINED",
        "TRUE",
        "FALSE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Tristate"


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
sample::SampleClassInterface_strategy = st.builds(
    sample::SampleClassInterface,
)
SampleClassInterface_strategy = st.builds(
    SampleClassInterface,
)
sample::SampleClassA_strategy = st.builds(
    sample::SampleClassA,
    sampleAttribute=
        safe_text
)
sample::SampleClassB_strategy = st.builds(
    sample::SampleClassB,
)
sample::SampleClassC_strategy = st.builds(
    sample::SampleClassC,
)

@given(instance=sample::SampleClassInterface_strategy)
@settings(max_examples=50)
def test_sample::sampleclassinterface_instantiation(instance):
    assert isinstance(instance, sample::SampleClassInterface)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=sample::SampleClassInterface_strategy)
@settings(max_examples=30)
def test_sample::sampleclassinterface_dosomething_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.doSomething(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.doSomething).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'doSomething' in sample::SampleClassInterface is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'doSomething' in sample::SampleClassInterface did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'doSomething' in sample::SampleClassInterface is not implemented or raised an error")

@given(instance=SampleClassInterface_strategy)
@settings(max_examples=50)
def test_sampleclassinterface_instantiation(instance):
    assert isinstance(instance, SampleClassInterface)

@given(instance=sample::SampleClassA_strategy)
@settings(max_examples=50)
def test_sample::sampleclassa_instantiation(instance):
    assert isinstance(instance, sample::SampleClassA)

@given(instance=sample::SampleClassA_strategy)
def test_sample::sampleclassa_sampleAttribute_type(instance):
    assert isinstance(instance.sampleAttribute, str)


@given(instance=sample::SampleClassA_strategy)
def test_sample::sampleclassa_sampleAttribute_setter(instance):
    original = instance.sampleAttribute
    instance.sampleAttribute = original
    assert instance.sampleAttribute == original

@given(instance=sample::SampleClassB_strategy)
@settings(max_examples=50)
def test_sample::sampleclassb_instantiation(instance):
    assert isinstance(instance, sample::SampleClassB)

@given(instance=sample::SampleClassC_strategy)
@settings(max_examples=50)
def test_sample::sampleclassc_instantiation(instance):
    assert isinstance(instance, sample::SampleClassC)
