import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    bug287941TestModel_Test2,
    bug287941TestModel_Test,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_bug287941testmodel_test2_is_not_abstract():
    assert not inspect.isabstract(bug287941TestModel_Test2)


def test_bug287941testmodel_test2_constructor_exists():
    assert callable(bug287941TestModel_Test2.__init__)


def test_bug287941testmodel_test2_constructor_args():
    sig = inspect.signature(bug287941TestModel_Test2.__init__)
    params = list(sig.parameters.keys())



def test_bug287941testmodel_test_is_not_abstract():
    assert not inspect.isabstract(bug287941TestModel_Test)


def test_bug287941testmodel_test_constructor_exists():
    assert callable(bug287941TestModel_Test.__init__)


def test_bug287941testmodel_test_constructor_args():
    sig = inspect.signature(bug287941TestModel_Test.__init__)
    params = list(sig.parameters.keys())
    assert "testAttr" in params, "Missing parameter 'testAttr'"

def test_bug287941testmodel_test_has_testAttr():
    assert hasattr(bug287941TestModel_Test, "testAttr")
    descriptor = None
    for klass in bug287941TestModel_Test.__mro__:
        if "testAttr" in klass.__dict__:
            descriptor = klass.__dict__["testAttr"]
            break
    assert isinstance(descriptor, property)


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
bug287941TestModel_Test2_strategy = st.builds(
    bug287941TestModel_Test2,
)
bug287941TestModel_Test_strategy = st.builds(
    bug287941TestModel_Test,
    testAttr=
        safe_text
)

@given(instance=bug287941TestModel_Test2_strategy)
@settings(max_examples=50)
def test_bug287941testmodel_test2_instantiation(instance):
    assert isinstance(instance, bug287941TestModel_Test2)

@given(instance=bug287941TestModel_Test_strategy)
@settings(max_examples=50)
def test_bug287941testmodel_test_instantiation(instance):
    assert isinstance(instance, bug287941TestModel_Test)



@given(instance=bug287941TestModel_Test_strategy)
def test_bug287941testmodel_test_testAttr_setter(instance):
    original = instance.testAttr
    instance.testAttr = original
    assert instance.testAttr == original
