import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    umlMM::dummy,
    umlMM::Attribute,
    Classifier,
    umlMM::PrimitiveDataType,
    umlMM::Class,
    umlMM::Association,
    umlMM::Classifier,
    umlMM::Package,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_umlmm::dummy_is_not_abstract():
    assert not inspect.isabstract(umlMM::dummy)


def test_umlmm::dummy_constructor_exists():
    assert callable(umlMM::dummy.__init__)


def test_umlmm::dummy_constructor_args():
    sig = inspect.signature(umlMM::dummy.__init__)
    params = list(sig.parameters.keys())



def test_umlmm::attribute_is_not_abstract():
    assert not inspect.isabstract(umlMM::Attribute)


def test_umlmm::attribute_constructor_exists():
    assert callable(umlMM::Attribute.__init__)


def test_umlmm::attribute_constructor_args():
    sig = inspect.signature(umlMM::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_umlmm::attribute_has_name():
    assert hasattr(umlMM::Attribute, "name")
    descriptor = None
    for klass in umlMM::Attribute.__mro__:
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



def test_umlmm::primitivedatatype_is_not_abstract():
    assert not inspect.isabstract(umlMM::PrimitiveDataType)


def test_umlmm::primitivedatatype_constructor_exists():
    assert callable(umlMM::PrimitiveDataType.__init__)


def test_umlmm::primitivedatatype_constructor_args():
    sig = inspect.signature(umlMM::PrimitiveDataType.__init__)
    params = list(sig.parameters.keys())



def test_umlmm::class_is_not_abstract():
    assert not inspect.isabstract(umlMM::Class)


def test_umlmm::class_constructor_exists():
    assert callable(umlMM::Class.__init__)


def test_umlmm::class_constructor_args():
    sig = inspect.signature(umlMM::Class.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_umlmm::class_has_kind():
    assert hasattr(umlMM::Class, "kind")
    descriptor = None
    for klass in umlMM::Class.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_umlmm::association_is_not_abstract():
    assert not inspect.isabstract(umlMM::Association)


def test_umlmm::association_constructor_exists():
    assert callable(umlMM::Association.__init__)


def test_umlmm::association_constructor_args():
    sig = inspect.signature(umlMM::Association.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_umlmm::association_has_name():
    assert hasattr(umlMM::Association, "name")
    descriptor = None
    for klass in umlMM::Association.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_umlmm::classifier_is_not_abstract():
    assert not inspect.isabstract(umlMM::Classifier)


def test_umlmm::classifier_constructor_exists():
    assert callable(umlMM::Classifier.__init__)


def test_umlmm::classifier_constructor_args():
    sig = inspect.signature(umlMM::Classifier.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_umlmm::classifier_has_name():
    assert hasattr(umlMM::Classifier, "name")
    descriptor = None
    for klass in umlMM::Classifier.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_umlmm::package_is_not_abstract():
    assert not inspect.isabstract(umlMM::Package)


def test_umlmm::package_constructor_exists():
    assert callable(umlMM::Package.__init__)


def test_umlmm::package_constructor_args():
    sig = inspect.signature(umlMM::Package.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_umlmm::package_has_name():
    assert hasattr(umlMM::Package, "name")
    descriptor = None
    for klass in umlMM::Package.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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
umlMM::dummy_strategy = st.builds(
    umlMM::dummy,
)
umlMM::Attribute_strategy = st.builds(
    umlMM::Attribute,
    name=
        safe_text
)
Classifier_strategy = st.builds(
    Classifier,
)
umlMM::PrimitiveDataType_strategy = st.builds(
    umlMM::PrimitiveDataType,
)
umlMM::Class_strategy = st.builds(
    umlMM::Class,
    kind=
        safe_text
)
umlMM::Association_strategy = st.builds(
    umlMM::Association,
    name=
        safe_text
)
umlMM::Classifier_strategy = st.builds(
    umlMM::Classifier,
    name=
        safe_text
)
umlMM::Package_strategy = st.builds(
    umlMM::Package,
    name=
        safe_text
)

@given(instance=umlMM::dummy_strategy)
@settings(max_examples=50)
def test_umlmm::dummy_instantiation(instance):
    assert isinstance(instance, umlMM::dummy)

@given(instance=umlMM::Attribute_strategy)
@settings(max_examples=50)
def test_umlmm::attribute_instantiation(instance):
    assert isinstance(instance, umlMM::Attribute)

@given(instance=umlMM::Attribute_strategy)
def test_umlmm::attribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=umlMM::Attribute_strategy)
def test_umlmm::attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=umlMM::PrimitiveDataType_strategy)
@settings(max_examples=50)
def test_umlmm::primitivedatatype_instantiation(instance):
    assert isinstance(instance, umlMM::PrimitiveDataType)

@given(instance=umlMM::Class_strategy)
@settings(max_examples=50)
def test_umlmm::class_instantiation(instance):
    assert isinstance(instance, umlMM::Class)

@given(instance=umlMM::Class_strategy)
def test_umlmm::class_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=umlMM::Class_strategy)
def test_umlmm::class_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=umlMM::Association_strategy)
@settings(max_examples=50)
def test_umlmm::association_instantiation(instance):
    assert isinstance(instance, umlMM::Association)

@given(instance=umlMM::Association_strategy)
def test_umlmm::association_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=umlMM::Association_strategy)
def test_umlmm::association_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=umlMM::Classifier_strategy)
@settings(max_examples=50)
def test_umlmm::classifier_instantiation(instance):
    assert isinstance(instance, umlMM::Classifier)

@given(instance=umlMM::Classifier_strategy)
def test_umlmm::classifier_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=umlMM::Classifier_strategy)
def test_umlmm::classifier_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=umlMM::Package_strategy)
@settings(max_examples=50)
def test_umlmm::package_instantiation(instance):
    assert isinstance(instance, umlMM::Package)

@given(instance=umlMM::Package_strategy)
def test_umlmm::package_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=umlMM::Package_strategy)
def test_umlmm::package_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
