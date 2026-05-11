import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Classifier,
    classes::CClass,
    classes::TypedElement,
    classes::Datatype,
    TypedElement,
    NamedElement,
    classes::Attribute,
    classes::NamedElement,
    classes::Classifier,
    classes::CModel,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_classifier_is_not_abstract():
    assert not inspect.isabstract(Classifier)


def test_classifier_constructor_exists():
    assert callable(Classifier.__init__)


def test_classifier_constructor_args():
    sig = inspect.signature(Classifier.__init__)
    params = list(sig.parameters.keys())



def test_classes::cclass_is_not_abstract():
    assert not inspect.isabstract(classes::CClass)


def test_classes::cclass_constructor_exists():
    assert callable(classes::CClass.__init__)


def test_classes::cclass_constructor_args():
    sig = inspect.signature(classes::CClass.__init__)
    params = list(sig.parameters.keys())
    assert "abstract" in params, "Missing parameter 'abstract'"

def test_classes::cclass_has_abstract():
    assert hasattr(classes::CClass, "abstract")
    descriptor = None
    for klass in classes::CClass.__mro__:
        if "abstract" in klass.__dict__:
            descriptor = klass.__dict__["abstract"]
            break
    assert isinstance(descriptor, property)



def test_classes::typedelement_is_not_abstract():
    assert not inspect.isabstract(classes::TypedElement)


def test_classes::typedelement_constructor_exists():
    assert callable(classes::TypedElement.__init__)


def test_classes::typedelement_constructor_args():
    sig = inspect.signature(classes::TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_classes::datatype_is_not_abstract():
    assert not inspect.isabstract(classes::Datatype)


def test_classes::datatype_constructor_exists():
    assert callable(classes::Datatype.__init__)


def test_classes::datatype_constructor_args():
    sig = inspect.signature(classes::Datatype.__init__)
    params = list(sig.parameters.keys())



def test_typedelement_is_not_abstract():
    assert not inspect.isabstract(TypedElement)


def test_typedelement_constructor_exists():
    assert callable(TypedElement.__init__)


def test_typedelement_constructor_args():
    sig = inspect.signature(TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_classes::attribute_is_not_abstract():
    assert not inspect.isabstract(classes::Attribute)


def test_classes::attribute_constructor_exists():
    assert callable(classes::Attribute.__init__)


def test_classes::attribute_constructor_args():
    sig = inspect.signature(classes::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "isMany" in params, "Missing parameter 'isMany'"

def test_classes::attribute_has_isMany():
    assert hasattr(classes::Attribute, "isMany")
    descriptor = None
    for klass in classes::Attribute.__mro__:
        if "isMany" in klass.__dict__:
            descriptor = klass.__dict__["isMany"]
            break
    assert isinstance(descriptor, property)



def test_classes::namedelement_is_not_abstract():
    assert not inspect.isabstract(classes::NamedElement)


def test_classes::namedelement_constructor_exists():
    assert callable(classes::NamedElement.__init__)


def test_classes::namedelement_constructor_args():
    sig = inspect.signature(classes::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_classes::namedelement_has_name():
    assert hasattr(classes::NamedElement, "name")
    descriptor = None
    for klass in classes::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_classes::classifier_is_not_abstract():
    assert not inspect.isabstract(classes::Classifier)


def test_classes::classifier_constructor_exists():
    assert callable(classes::Classifier.__init__)


def test_classes::classifier_constructor_args():
    sig = inspect.signature(classes::Classifier.__init__)
    params = list(sig.parameters.keys())



def test_classes::cmodel_is_not_abstract():
    assert not inspect.isabstract(classes::CModel)


def test_classes::cmodel_constructor_exists():
    assert callable(classes::CModel.__init__)


def test_classes::cmodel_constructor_args():
    sig = inspect.signature(classes::CModel.__init__)
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
Classifier_strategy = st.builds(
    Classifier,
)
classes::CClass_strategy = st.builds(
    classes::CClass,
    abstract=
        st.booleans()
)
classes::TypedElement_strategy = st.builds(
    classes::TypedElement,
)
classes::Datatype_strategy = st.builds(
    classes::Datatype,
)
TypedElement_strategy = st.builds(
    TypedElement,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
classes::Attribute_strategy = st.builds(
    classes::Attribute,
    isMany=
        st.booleans()
)
classes::NamedElement_strategy = st.builds(
    classes::NamedElement,
    name=
        safe_text
)
classes::Classifier_strategy = st.builds(
    classes::Classifier,
)
classes::CModel_strategy = st.builds(
    classes::CModel,
)

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=classes::CClass_strategy)
@settings(max_examples=50)
def test_classes::cclass_instantiation(instance):
    assert isinstance(instance, classes::CClass)

@given(instance=classes::CClass_strategy)
def test_classes::cclass_abstract_type(instance):
    assert isinstance(instance.abstract, bool)


@given(instance=classes::CClass_strategy)
def test_classes::cclass_abstract_setter(instance):
    original = instance.abstract
    instance.abstract = original
    assert instance.abstract == original

@given(instance=classes::TypedElement_strategy)
@settings(max_examples=50)
def test_classes::typedelement_instantiation(instance):
    assert isinstance(instance, classes::TypedElement)

@given(instance=classes::Datatype_strategy)
@settings(max_examples=50)
def test_classes::datatype_instantiation(instance):
    assert isinstance(instance, classes::Datatype)

@given(instance=TypedElement_strategy)
@settings(max_examples=50)
def test_typedelement_instantiation(instance):
    assert isinstance(instance, TypedElement)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=classes::Attribute_strategy)
@settings(max_examples=50)
def test_classes::attribute_instantiation(instance):
    assert isinstance(instance, classes::Attribute)

@given(instance=classes::Attribute_strategy)
def test_classes::attribute_isMany_type(instance):
    assert isinstance(instance.isMany, bool)


@given(instance=classes::Attribute_strategy)
def test_classes::attribute_isMany_setter(instance):
    original = instance.isMany
    instance.isMany = original
    assert instance.isMany == original

@given(instance=classes::NamedElement_strategy)
@settings(max_examples=50)
def test_classes::namedelement_instantiation(instance):
    assert isinstance(instance, classes::NamedElement)

@given(instance=classes::NamedElement_strategy)
def test_classes::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=classes::NamedElement_strategy)
def test_classes::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=classes::Classifier_strategy)
@settings(max_examples=50)
def test_classes::classifier_instantiation(instance):
    assert isinstance(instance, classes::Classifier)

@given(instance=classes::CModel_strategy)
@settings(max_examples=50)
def test_classes::cmodel_instantiation(instance):
    assert isinstance(instance, classes::CModel)
