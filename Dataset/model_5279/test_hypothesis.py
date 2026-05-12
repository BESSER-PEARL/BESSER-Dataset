import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    sample_SampleClassInterface,
    SampleClassInterface,
    sample_SampleClassA,
    sample_SampleClassB,
    sample_SampleClassC,
    Tristate,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_sample_sampleclassinterface_is_not_abstract():
    assert not inspect.isabstract(sample_SampleClassInterface)


def test_sample_sampleclassinterface_constructor_exists():
    assert callable(sample_SampleClassInterface.__init__)


def test_sample_sampleclassinterface_constructor_args():
    sig = inspect.signature(sample_SampleClassInterface.__init__)
    params = list(sig.parameters.keys())



def test_sampleclassinterface_is_not_abstract():
    assert not inspect.isabstract(SampleClassInterface)


def test_sampleclassinterface_constructor_exists():
    assert callable(SampleClassInterface.__init__)


def test_sampleclassinterface_constructor_args():
    sig = inspect.signature(SampleClassInterface.__init__)
    params = list(sig.parameters.keys())



def test_sample_sampleclassa_is_not_abstract():
    assert not inspect.isabstract(sample_SampleClassA)


def test_sample_sampleclassa_constructor_exists():
    assert callable(sample_SampleClassA.__init__)


def test_sample_sampleclassa_constructor_args():
    sig = inspect.signature(sample_SampleClassA.__init__)
    params = list(sig.parameters.keys())
    assert "sampleAttribute" in params, "Missing parameter 'sampleAttribute'"

def test_sample_sampleclassa_has_sampleAttribute():
    assert hasattr(sample_SampleClassA, "sampleAttribute")
    descriptor = None
    for klass in sample_SampleClassA.__mro__:
        if "sampleAttribute" in klass.__dict__:
            descriptor = klass.__dict__["sampleAttribute"]
            break
    assert isinstance(descriptor, property)



def test_sample_sampleclassb_is_not_abstract():
    assert not inspect.isabstract(sample_SampleClassB)


def test_sample_sampleclassb_constructor_exists():
    assert callable(sample_SampleClassB.__init__)


def test_sample_sampleclassb_constructor_args():
    sig = inspect.signature(sample_SampleClassB.__init__)
    params = list(sig.parameters.keys())



def test_sample_sampleclassc_is_not_abstract():
    assert not inspect.isabstract(sample_SampleClassC)


def test_sample_sampleclassc_constructor_exists():
    assert callable(sample_SampleClassC.__init__)


def test_sample_sampleclassc_constructor_args():
    sig = inspect.signature(sample_SampleClassC.__init__)
    params = list(sig.parameters.keys())

def test_tristate_exists():
    # Check that the Enumeration exists
    assert Tristate is not None

def test_tristate_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Tristate]
    expected_literals = [
        "TRUE",
        "UNDEFINED",
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
sample_SampleClassInterface_strategy = st.builds(
    sample_SampleClassInterface,
)
SampleClassInterface_strategy = st.builds(
    SampleClassInterface,
)
sample_SampleClassA_strategy = st.builds(
    sample_SampleClassA,
    sampleAttribute=
        safe_text
)
sample_SampleClassB_strategy = st.builds(
    sample_SampleClassB,
)
sample_SampleClassC_strategy = st.builds(
    sample_SampleClassC,
)

@given(instance=sample_SampleClassInterface_strategy)
@settings(max_examples=50)
def test_sample_sampleclassinterface_instantiation(instance):
    assert isinstance(instance, sample_SampleClassInterface)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=sample_SampleClassInterface_strategy)
@settings(max_examples=30)
def test_sample_sampleclassinterface_dosomething_changes_state(instance):
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
        assert has_statements, f"Function 'doSomething' in sample_SampleClassInterface is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'doSomething' in sample_SampleClassInterface did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'doSomething' in sample_SampleClassInterface is not implemented or raised an error")

@given(instance=SampleClassInterface_strategy)
@settings(max_examples=50)
def test_sampleclassinterface_instantiation(instance):
    assert isinstance(instance, SampleClassInterface)

@given(instance=sample_SampleClassA_strategy)
@settings(max_examples=50)
def test_sample_sampleclassa_instantiation(instance):
    assert isinstance(instance, sample_SampleClassA)



@given(instance=sample_SampleClassA_strategy)
def test_sample_sampleclassa_sampleAttribute_setter(instance):
    original = instance.sampleAttribute
    instance.sampleAttribute = original
    assert instance.sampleAttribute == original

@given(instance=sample_SampleClassB_strategy)
@settings(max_examples=50)
def test_sample_sampleclassb_instantiation(instance):
    assert isinstance(instance, sample_SampleClassB)

@given(instance=sample_SampleClassC_strategy)
@settings(max_examples=50)
def test_sample_sampleclassc_instantiation(instance):
    assert isinstance(instance, sample_SampleClassC)
