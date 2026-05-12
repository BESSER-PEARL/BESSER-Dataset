import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    umlMM__Attribute,
    Classifier,
    umlMM__PrimitiveDataType,
    umlMM__Class,
    umlMM__dummy,
    umlMM__Association,
    umlMM__Classifier,
    umlMM__Package,
    KIND,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_umlmm__attribute_is_not_abstract():
    assert not inspect.isabstract(umlMM__Attribute)


def test_umlmm__attribute_constructor_exists():
    assert callable(umlMM__Attribute.__init__)


def test_umlmm__attribute_constructor_args():
    sig = inspect.signature(umlMM__Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_umlmm__attribute_has_name():
    assert hasattr(umlMM__Attribute, "name")
    descriptor = None
    for klass in umlMM__Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_classifier_is_not_abstract():
    assert not inspect.isabstract(Classifier)


def test_classifier_constructor_exists():
    assert callable(Classifier.__init__)


def test_classifier_constructor_args():
    sig = inspect.signature(Classifier.__init__)
    params = list(sig.parameters.keys())



def test_umlmm__primitivedatatype_is_not_abstract():
    assert not inspect.isabstract(umlMM__PrimitiveDataType)


def test_umlmm__primitivedatatype_constructor_exists():
    assert callable(umlMM__PrimitiveDataType.__init__)


def test_umlmm__primitivedatatype_constructor_args():
    sig = inspect.signature(umlMM__PrimitiveDataType.__init__)
    params = list(sig.parameters.keys())



def test_umlmm__class_is_not_abstract():
    assert not inspect.isabstract(umlMM__Class)


def test_umlmm__class_constructor_exists():
    assert callable(umlMM__Class.__init__)


def test_umlmm__class_constructor_args():
    sig = inspect.signature(umlMM__Class.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_umlmm__class_has_kind():
    assert hasattr(umlMM__Class, "kind")
    descriptor = None
    for klass in umlMM__Class.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_umlmm__dummy_is_not_abstract():
    assert not inspect.isabstract(umlMM__dummy)


def test_umlmm__dummy_constructor_exists():
    assert callable(umlMM__dummy.__init__)


def test_umlmm__dummy_constructor_args():
    sig = inspect.signature(umlMM__dummy.__init__)
    params = list(sig.parameters.keys())



def test_umlmm__association_is_not_abstract():
    assert not inspect.isabstract(umlMM__Association)


def test_umlmm__association_constructor_exists():
    assert callable(umlMM__Association.__init__)


def test_umlmm__association_constructor_args():
    sig = inspect.signature(umlMM__Association.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_umlmm__association_has_name():
    assert hasattr(umlMM__Association, "name")
    descriptor = None
    for klass in umlMM__Association.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_umlmm__classifier_is_not_abstract():
    assert not inspect.isabstract(umlMM__Classifier)


def test_umlmm__classifier_constructor_exists():
    assert callable(umlMM__Classifier.__init__)


def test_umlmm__classifier_constructor_args():
    sig = inspect.signature(umlMM__Classifier.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_umlmm__classifier_has_name():
    assert hasattr(umlMM__Classifier, "name")
    descriptor = None
    for klass in umlMM__Classifier.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_umlmm__package_is_not_abstract():
    assert not inspect.isabstract(umlMM__Package)


def test_umlmm__package_constructor_exists():
    assert callable(umlMM__Package.__init__)


def test_umlmm__package_constructor_args():
    sig = inspect.signature(umlMM__Package.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_umlmm__package_has_name():
    assert hasattr(umlMM__Package, "name")
    descriptor = None
    for klass in umlMM__Package.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_kind_exists():
    # Check that the Enumeration exists
    assert KIND is not None

def test_kind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in KIND]
    expected_literals = [
        "OTHER",
        "PERSISTENT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in KIND"


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
umlMM__Attribute_strategy = st.builds(
    umlMM__Attribute,
    name=
        safe_text
)
Classifier_strategy = st.builds(
    Classifier,
)
umlMM__PrimitiveDataType_strategy = st.builds(
    umlMM__PrimitiveDataType,
)
umlMM__Class_strategy = st.builds(
    umlMM__Class,
    kind=
        safe_text
)
umlMM__dummy_strategy = st.builds(
    umlMM__dummy,
)
umlMM__Association_strategy = st.builds(
    umlMM__Association,
    name=
        safe_text
)
umlMM__Classifier_strategy = st.builds(
    umlMM__Classifier,
    name=
        safe_text
)
umlMM__Package_strategy = st.builds(
    umlMM__Package,
    name=
        safe_text
)

@given(instance=umlMM__Attribute_strategy)
@settings(max_examples=50)
def test_umlmm__attribute_instantiation(instance):
    assert isinstance(instance, umlMM__Attribute)



@given(instance=umlMM__Attribute_strategy)
def test_umlmm__attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=umlMM__PrimitiveDataType_strategy)
@settings(max_examples=50)
def test_umlmm__primitivedatatype_instantiation(instance):
    assert isinstance(instance, umlMM__PrimitiveDataType)

@given(instance=umlMM__Class_strategy)
@settings(max_examples=50)
def test_umlmm__class_instantiation(instance):
    assert isinstance(instance, umlMM__Class)



@given(instance=umlMM__Class_strategy)
def test_umlmm__class_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=umlMM__dummy_strategy)
@settings(max_examples=50)
def test_umlmm__dummy_instantiation(instance):
    assert isinstance(instance, umlMM__dummy)

@given(instance=umlMM__Association_strategy)
@settings(max_examples=50)
def test_umlmm__association_instantiation(instance):
    assert isinstance(instance, umlMM__Association)



@given(instance=umlMM__Association_strategy)
def test_umlmm__association_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=umlMM__Classifier_strategy)
@settings(max_examples=50)
def test_umlmm__classifier_instantiation(instance):
    assert isinstance(instance, umlMM__Classifier)



@given(instance=umlMM__Classifier_strategy)
def test_umlmm__classifier_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=umlMM__Package_strategy)
@settings(max_examples=50)
def test_umlmm__package_instantiation(instance):
    assert isinstance(instance, umlMM__Package)



@given(instance=umlMM__Package_strategy)
def test_umlmm__package_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
