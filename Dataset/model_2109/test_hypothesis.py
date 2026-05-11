import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    SomeTestClass,
    test::SomeTestClassWithID,
    test::SomeTestClass,
    test::PatchTestModel,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_sometestclass_is_not_abstract():
    assert not inspect.isabstract(SomeTestClass)


def test_sometestclass_constructor_exists():
    assert callable(SomeTestClass.__init__)


def test_sometestclass_constructor_args():
    sig = inspect.signature(SomeTestClass.__init__)
    params = list(sig.parameters.keys())



def test_test::sometestclasswithid_is_not_abstract():
    assert not inspect.isabstract(test::SomeTestClassWithID)


def test_test::sometestclasswithid_constructor_exists():
    assert callable(test::SomeTestClassWithID.__init__)


def test_test::sometestclasswithid_constructor_args():
    sig = inspect.signature(test::SomeTestClassWithID.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_test::sometestclasswithid_has_id():
    assert hasattr(test::SomeTestClassWithID, "id")
    descriptor = None
    for klass in test::SomeTestClassWithID.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_test::sometestclass_is_not_abstract():
    assert not inspect.isabstract(test::SomeTestClass)


def test_test::sometestclass_constructor_exists():
    assert callable(test::SomeTestClass.__init__)


def test_test::sometestclass_constructor_args():
    sig = inspect.signature(test::SomeTestClass.__init__)
    params = list(sig.parameters.keys())
    assert "attribute" in params, "Missing parameter 'attribute'"

def test_test::sometestclass_has_attribute():
    assert hasattr(test::SomeTestClass, "attribute")
    descriptor = None
    for klass in test::SomeTestClass.__mro__:
        if "attribute" in klass.__dict__:
            descriptor = klass.__dict__["attribute"]
            break
    assert isinstance(descriptor, property)



def test_test::patchtestmodel_is_not_abstract():
    assert not inspect.isabstract(test::PatchTestModel)


def test_test::patchtestmodel_constructor_exists():
    assert callable(test::PatchTestModel.__init__)


def test_test::patchtestmodel_constructor_args():
    sig = inspect.signature(test::PatchTestModel.__init__)
    params = list(sig.parameters.keys())
    assert "multiAttribute" in params, "Missing parameter 'multiAttribute'"
    assert "oneAttribute" in params, "Missing parameter 'oneAttribute'"
    assert "id" in params, "Missing parameter 'id'"

def test_test::patchtestmodel_has_multiAttribute():
    assert hasattr(test::PatchTestModel, "multiAttribute")
    descriptor = None
    for klass in test::PatchTestModel.__mro__:
        if "multiAttribute" in klass.__dict__:
            descriptor = klass.__dict__["multiAttribute"]
            break
    assert isinstance(descriptor, property)

def test_test::patchtestmodel_has_oneAttribute():
    assert hasattr(test::PatchTestModel, "oneAttribute")
    descriptor = None
    for klass in test::PatchTestModel.__mro__:
        if "oneAttribute" in klass.__dict__:
            descriptor = klass.__dict__["oneAttribute"]
            break
    assert isinstance(descriptor, property)

def test_test::patchtestmodel_has_id():
    assert hasattr(test::PatchTestModel, "id")
    descriptor = None
    for klass in test::PatchTestModel.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
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
SomeTestClass_strategy = st.builds(
    SomeTestClass,
)
test::SomeTestClassWithID_strategy = st.builds(
    test::SomeTestClassWithID,
    id=
        safe_text
)
test::SomeTestClass_strategy = st.builds(
    test::SomeTestClass,
    attribute=
        safe_text
)
test::PatchTestModel_strategy = st.builds(
    test::PatchTestModel,
    multiAttribute=
        safe_text,
    oneAttribute=
        safe_text,
    id=
        safe_text
)

@given(instance=SomeTestClass_strategy)
@settings(max_examples=50)
def test_sometestclass_instantiation(instance):
    assert isinstance(instance, SomeTestClass)

@given(instance=test::SomeTestClassWithID_strategy)
@settings(max_examples=50)
def test_test::sometestclasswithid_instantiation(instance):
    assert isinstance(instance, test::SomeTestClassWithID)

@given(instance=test::SomeTestClassWithID_strategy)
def test_test::sometestclasswithid_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=test::SomeTestClassWithID_strategy)
def test_test::sometestclasswithid_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=test::SomeTestClass_strategy)
@settings(max_examples=50)
def test_test::sometestclass_instantiation(instance):
    assert isinstance(instance, test::SomeTestClass)

@given(instance=test::SomeTestClass_strategy)
def test_test::sometestclass_attribute_type(instance):
    assert isinstance(instance.attribute, str)


@given(instance=test::SomeTestClass_strategy)
def test_test::sometestclass_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original

@given(instance=test::PatchTestModel_strategy)
@settings(max_examples=50)
def test_test::patchtestmodel_instantiation(instance):
    assert isinstance(instance, test::PatchTestModel)

@given(instance=test::PatchTestModel_strategy)
def test_test::patchtestmodel_multiAttribute_type(instance):
    assert isinstance(instance.multiAttribute, str)


@given(instance=test::PatchTestModel_strategy)
def test_test::patchtestmodel_multiAttribute_setter(instance):
    original = instance.multiAttribute
    instance.multiAttribute = original
    assert instance.multiAttribute == original

@given(instance=test::PatchTestModel_strategy)
def test_test::patchtestmodel_oneAttribute_type(instance):
    assert isinstance(instance.oneAttribute, str)


@given(instance=test::PatchTestModel_strategy)
def test_test::patchtestmodel_oneAttribute_setter(instance):
    original = instance.oneAttribute
    instance.oneAttribute = original
    assert instance.oneAttribute == original

@given(instance=test::PatchTestModel_strategy)
def test_test::patchtestmodel_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=test::PatchTestModel_strategy)
def test_test::patchtestmodel_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original
