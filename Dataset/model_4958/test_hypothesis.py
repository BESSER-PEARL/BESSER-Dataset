import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Model,
    TypedElement,
    testmodel::Attribute,
    ModelElement,
    testmodel::Association,
    testmodel::Group,
    testmodel::Class,
    NamedElement,
    testmodel::ModelElement,
    testmodel::TypedElement,
    testmodel::NamedElement,
    testmodel::Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_model_is_not_abstract():
    assert not inspect.isabstract(Model)


def test_model_constructor_exists():
    assert callable(Model.__init__)


def test_model_constructor_args():
    sig = inspect.signature(Model.__init__)
    params = list(sig.parameters.keys())



def test_typedelement_is_not_abstract():
    assert not inspect.isabstract(TypedElement)


def test_typedelement_constructor_exists():
    assert callable(TypedElement.__init__)


def test_typedelement_constructor_args():
    sig = inspect.signature(TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_testmodel::attribute_is_not_abstract():
    assert not inspect.isabstract(testmodel::Attribute)


def test_testmodel::attribute_constructor_exists():
    assert callable(testmodel::Attribute.__init__)


def test_testmodel::attribute_constructor_args():
    sig = inspect.signature(testmodel::Attribute.__init__)
    params = list(sig.parameters.keys())



def test_modelelement_is_not_abstract():
    assert not inspect.isabstract(ModelElement)


def test_modelelement_constructor_exists():
    assert callable(ModelElement.__init__)


def test_modelelement_constructor_args():
    sig = inspect.signature(ModelElement.__init__)
    params = list(sig.parameters.keys())



def test_testmodel::association_is_not_abstract():
    assert not inspect.isabstract(testmodel::Association)


def test_testmodel::association_constructor_exists():
    assert callable(testmodel::Association.__init__)


def test_testmodel::association_constructor_args():
    sig = inspect.signature(testmodel::Association.__init__)
    params = list(sig.parameters.keys())
    assert "secondLabel" in params, "Missing parameter 'secondLabel'"
    assert "firstLabel" in params, "Missing parameter 'firstLabel'"

def test_testmodel::association_has_secondLabel():
    assert hasattr(testmodel::Association, "secondLabel")
    descriptor = None
    for klass in testmodel::Association.__mro__:
        if "secondLabel" in klass.__dict__:
            descriptor = klass.__dict__["secondLabel"]
            break
    assert isinstance(descriptor, property)

def test_testmodel::association_has_firstLabel():
    assert hasattr(testmodel::Association, "firstLabel")
    descriptor = None
    for klass in testmodel::Association.__mro__:
        if "firstLabel" in klass.__dict__:
            descriptor = klass.__dict__["firstLabel"]
            break
    assert isinstance(descriptor, property)



def test_testmodel::group_is_not_abstract():
    assert not inspect.isabstract(testmodel::Group)


def test_testmodel::group_constructor_exists():
    assert callable(testmodel::Group.__init__)


def test_testmodel::group_constructor_args():
    sig = inspect.signature(testmodel::Group.__init__)
    params = list(sig.parameters.keys())



def test_testmodel::class_is_not_abstract():
    assert not inspect.isabstract(testmodel::Class)


def test_testmodel::class_constructor_exists():
    assert callable(testmodel::Class.__init__)


def test_testmodel::class_constructor_args():
    sig = inspect.signature(testmodel::Class.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_testmodel::modelelement_is_not_abstract():
    assert not inspect.isabstract(testmodel::ModelElement)


def test_testmodel::modelelement_constructor_exists():
    assert callable(testmodel::ModelElement.__init__)


def test_testmodel::modelelement_constructor_args():
    sig = inspect.signature(testmodel::ModelElement.__init__)
    params = list(sig.parameters.keys())



def test_testmodel::typedelement_is_not_abstract():
    assert not inspect.isabstract(testmodel::TypedElement)


def test_testmodel::typedelement_constructor_exists():
    assert callable(testmodel::TypedElement.__init__)


def test_testmodel::typedelement_constructor_args():
    sig = inspect.signature(testmodel::TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_testmodel::namedelement_is_not_abstract():
    assert not inspect.isabstract(testmodel::NamedElement)


def test_testmodel::namedelement_constructor_exists():
    assert callable(testmodel::NamedElement.__init__)


def test_testmodel::namedelement_constructor_args():
    sig = inspect.signature(testmodel::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_testmodel::namedelement_has_name():
    assert hasattr(testmodel::NamedElement, "name")
    descriptor = None
    for klass in testmodel::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_testmodel::model_is_not_abstract():
    assert not inspect.isabstract(testmodel::Model)


def test_testmodel::model_constructor_exists():
    assert callable(testmodel::Model.__init__)


def test_testmodel::model_constructor_args():
    sig = inspect.signature(testmodel::Model.__init__)
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
Model_strategy = st.builds(
    Model,
)
TypedElement_strategy = st.builds(
    TypedElement,
)
testmodel::Attribute_strategy = st.builds(
    testmodel::Attribute,
)
ModelElement_strategy = st.builds(
    ModelElement,
)
testmodel::Association_strategy = st.builds(
    testmodel::Association,
    secondLabel=
        safe_text,
    firstLabel=
        safe_text
)
testmodel::Group_strategy = st.builds(
    testmodel::Group,
)
testmodel::Class_strategy = st.builds(
    testmodel::Class,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
testmodel::ModelElement_strategy = st.builds(
    testmodel::ModelElement,
)
testmodel::TypedElement_strategy = st.builds(
    testmodel::TypedElement,
)
testmodel::NamedElement_strategy = st.builds(
    testmodel::NamedElement,
    name=
        safe_text
)
testmodel::Model_strategy = st.builds(
    testmodel::Model,
)

@given(instance=Model_strategy)
@settings(max_examples=50)
def test_model_instantiation(instance):
    assert isinstance(instance, Model)

@given(instance=TypedElement_strategy)
@settings(max_examples=50)
def test_typedelement_instantiation(instance):
    assert isinstance(instance, TypedElement)

@given(instance=testmodel::Attribute_strategy)
@settings(max_examples=50)
def test_testmodel::attribute_instantiation(instance):
    assert isinstance(instance, testmodel::Attribute)

@given(instance=ModelElement_strategy)
@settings(max_examples=50)
def test_modelelement_instantiation(instance):
    assert isinstance(instance, ModelElement)

@given(instance=testmodel::Association_strategy)
@settings(max_examples=50)
def test_testmodel::association_instantiation(instance):
    assert isinstance(instance, testmodel::Association)

@given(instance=testmodel::Association_strategy)
def test_testmodel::association_secondLabel_type(instance):
    assert isinstance(instance.secondLabel, str)


@given(instance=testmodel::Association_strategy)
def test_testmodel::association_secondLabel_setter(instance):
    original = instance.secondLabel
    instance.secondLabel = original
    assert instance.secondLabel == original

@given(instance=testmodel::Association_strategy)
def test_testmodel::association_firstLabel_type(instance):
    assert isinstance(instance.firstLabel, str)


@given(instance=testmodel::Association_strategy)
def test_testmodel::association_firstLabel_setter(instance):
    original = instance.firstLabel
    instance.firstLabel = original
    assert instance.firstLabel == original

@given(instance=testmodel::Group_strategy)
@settings(max_examples=50)
def test_testmodel::group_instantiation(instance):
    assert isinstance(instance, testmodel::Group)

@given(instance=testmodel::Class_strategy)
@settings(max_examples=50)
def test_testmodel::class_instantiation(instance):
    assert isinstance(instance, testmodel::Class)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=testmodel::ModelElement_strategy)
@settings(max_examples=50)
def test_testmodel::modelelement_instantiation(instance):
    assert isinstance(instance, testmodel::ModelElement)

@given(instance=testmodel::TypedElement_strategy)
@settings(max_examples=50)
def test_testmodel::typedelement_instantiation(instance):
    assert isinstance(instance, testmodel::TypedElement)

@given(instance=testmodel::NamedElement_strategy)
@settings(max_examples=50)
def test_testmodel::namedelement_instantiation(instance):
    assert isinstance(instance, testmodel::NamedElement)

@given(instance=testmodel::NamedElement_strategy)
def test_testmodel::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=testmodel::NamedElement_strategy)
def test_testmodel::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=testmodel::Model_strategy)
@settings(max_examples=50)
def test_testmodel::model_instantiation(instance):
    assert isinstance(instance, testmodel::Model)
