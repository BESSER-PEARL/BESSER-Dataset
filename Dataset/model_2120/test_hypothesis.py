import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ValidationModel::UnitTest,
    ValidationModel::TestContainer,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_validationmodel::unittest_is_not_abstract():
    assert not inspect.isabstract(ValidationModel::UnitTest)


def test_validationmodel::unittest_constructor_exists():
    assert callable(ValidationModel::UnitTest.__init__)


def test_validationmodel::unittest_constructor_args():
    sig = inspect.signature(ValidationModel::UnitTest.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "isTested" in params, "Missing parameter 'isTested'"
    assert "id" in params, "Missing parameter 'id'"

def test_validationmodel::unittest_has_name():
    assert hasattr(ValidationModel::UnitTest, "name")
    descriptor = None
    for klass in ValidationModel::UnitTest.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_validationmodel::unittest_has_isTested():
    assert hasattr(ValidationModel::UnitTest, "isTested")
    descriptor = None
    for klass in ValidationModel::UnitTest.__mro__:
        if "isTested" in klass.__dict__:
            descriptor = klass.__dict__["isTested"]
            break
    assert isinstance(descriptor, property)

def test_validationmodel::unittest_has_id():
    assert hasattr(ValidationModel::UnitTest, "id")
    descriptor = None
    for klass in ValidationModel::UnitTest.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_validationmodel::testcontainer_is_not_abstract():
    assert not inspect.isabstract(ValidationModel::TestContainer)


def test_validationmodel::testcontainer_constructor_exists():
    assert callable(ValidationModel::TestContainer.__init__)


def test_validationmodel::testcontainer_constructor_args():
    sig = inspect.signature(ValidationModel::TestContainer.__init__)
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
ValidationModel::UnitTest_strategy = st.builds(
    ValidationModel::UnitTest,
    name=
        safe_text,
    isTested=
        st.booleans(),
    id=
        safe_text
)
ValidationModel::TestContainer_strategy = st.builds(
    ValidationModel::TestContainer,
)

@given(instance=ValidationModel::UnitTest_strategy)
@settings(max_examples=50)
def test_validationmodel::unittest_instantiation(instance):
    assert isinstance(instance, ValidationModel::UnitTest)

@given(instance=ValidationModel::UnitTest_strategy)
def test_validationmodel::unittest_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ValidationModel::UnitTest_strategy)
def test_validationmodel::unittest_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ValidationModel::UnitTest_strategy)
def test_validationmodel::unittest_isTested_type(instance):
    assert isinstance(instance.isTested, bool)


@given(instance=ValidationModel::UnitTest_strategy)
def test_validationmodel::unittest_isTested_setter(instance):
    original = instance.isTested
    instance.isTested = original
    assert instance.isTested == original

@given(instance=ValidationModel::UnitTest_strategy)
def test_validationmodel::unittest_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=ValidationModel::UnitTest_strategy)
def test_validationmodel::unittest_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=ValidationModel::TestContainer_strategy)
@settings(max_examples=50)
def test_validationmodel::testcontainer_instantiation(instance):
    assert isinstance(instance, ValidationModel::TestContainer)
