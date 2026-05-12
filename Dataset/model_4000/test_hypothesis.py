import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Classifier,
    classes_CClass,
    classes_TypedElement,
    classes_Datatype,
    TypedElement,
    NamedElement,
    classes_Attribute,
    classes_NamedElement,
    classes_Classifier,
    classes_CModel,
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



def test_classes_cclass_is_not_abstract():
    assert not inspect.isabstract(classes_CClass)


def test_classes_cclass_constructor_exists():
    assert callable(classes_CClass.__init__)


def test_classes_cclass_constructor_args():
    sig = inspect.signature(classes_CClass.__init__)
    params = list(sig.parameters.keys())
    assert "abstract" in params, "Missing parameter 'abstract'"

def test_classes_cclass_has_abstract():
    assert hasattr(classes_CClass, "abstract")
    descriptor = None
    for klass in classes_CClass.__mro__:
        if "abstract" in klass.__dict__:
            descriptor = klass.__dict__["abstract"]
            break
    assert isinstance(descriptor, property)



def test_classes_typedelement_is_not_abstract():
    assert not inspect.isabstract(classes_TypedElement)


def test_classes_typedelement_constructor_exists():
    assert callable(classes_TypedElement.__init__)


def test_classes_typedelement_constructor_args():
    sig = inspect.signature(classes_TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_classes_datatype_is_not_abstract():
    assert not inspect.isabstract(classes_Datatype)


def test_classes_datatype_constructor_exists():
    assert callable(classes_Datatype.__init__)


def test_classes_datatype_constructor_args():
    sig = inspect.signature(classes_Datatype.__init__)
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



def test_classes_attribute_is_not_abstract():
    assert not inspect.isabstract(classes_Attribute)


def test_classes_attribute_constructor_exists():
    assert callable(classes_Attribute.__init__)


def test_classes_attribute_constructor_args():
    sig = inspect.signature(classes_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "isMany" in params, "Missing parameter 'isMany'"

def test_classes_attribute_has_isMany():
    assert hasattr(classes_Attribute, "isMany")
    descriptor = None
    for klass in classes_Attribute.__mro__:
        if "isMany" in klass.__dict__:
            descriptor = klass.__dict__["isMany"]
            break
    assert isinstance(descriptor, property)



def test_classes_namedelement_is_not_abstract():
    assert not inspect.isabstract(classes_NamedElement)


def test_classes_namedelement_constructor_exists():
    assert callable(classes_NamedElement.__init__)


def test_classes_namedelement_constructor_args():
    sig = inspect.signature(classes_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_classes_namedelement_has_name():
    assert hasattr(classes_NamedElement, "name")
    descriptor = None
    for klass in classes_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_classes_classifier_is_not_abstract():
    assert not inspect.isabstract(classes_Classifier)


def test_classes_classifier_constructor_exists():
    assert callable(classes_Classifier.__init__)


def test_classes_classifier_constructor_args():
    sig = inspect.signature(classes_Classifier.__init__)
    params = list(sig.parameters.keys())



def test_classes_cmodel_is_not_abstract():
    assert not inspect.isabstract(classes_CModel)


def test_classes_cmodel_constructor_exists():
    assert callable(classes_CModel.__init__)


def test_classes_cmodel_constructor_args():
    sig = inspect.signature(classes_CModel.__init__)
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
classes_CClass_strategy = st.builds(
    classes_CClass,
    abstract=
        st.booleans()
)
classes_TypedElement_strategy = st.builds(
    classes_TypedElement,
)
classes_Datatype_strategy = st.builds(
    classes_Datatype,
)
TypedElement_strategy = st.builds(
    TypedElement,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
classes_Attribute_strategy = st.builds(
    classes_Attribute,
    isMany=
        st.booleans()
)
classes_NamedElement_strategy = st.builds(
    classes_NamedElement,
    name=
        safe_text
)
classes_Classifier_strategy = st.builds(
    classes_Classifier,
)
classes_CModel_strategy = st.builds(
    classes_CModel,
)

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=classes_CClass_strategy)
@settings(max_examples=50)
def test_classes_cclass_instantiation(instance):
    assert isinstance(instance, classes_CClass)



@given(instance=classes_CClass_strategy)
def test_classes_cclass_abstract_setter(instance):
    original = instance.abstract
    instance.abstract = original
    assert instance.abstract == original

@given(instance=classes_TypedElement_strategy)
@settings(max_examples=50)
def test_classes_typedelement_instantiation(instance):
    assert isinstance(instance, classes_TypedElement)

@given(instance=classes_Datatype_strategy)
@settings(max_examples=50)
def test_classes_datatype_instantiation(instance):
    assert isinstance(instance, classes_Datatype)

@given(instance=TypedElement_strategy)
@settings(max_examples=50)
def test_typedelement_instantiation(instance):
    assert isinstance(instance, TypedElement)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=classes_Attribute_strategy)
@settings(max_examples=50)
def test_classes_attribute_instantiation(instance):
    assert isinstance(instance, classes_Attribute)



@given(instance=classes_Attribute_strategy)
def test_classes_attribute_isMany_setter(instance):
    original = instance.isMany
    instance.isMany = original
    assert instance.isMany == original

@given(instance=classes_NamedElement_strategy)
@settings(max_examples=50)
def test_classes_namedelement_instantiation(instance):
    assert isinstance(instance, classes_NamedElement)



@given(instance=classes_NamedElement_strategy)
def test_classes_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=classes_Classifier_strategy)
@settings(max_examples=50)
def test_classes_classifier_instantiation(instance):
    assert isinstance(instance, classes_Classifier)

@given(instance=classes_CModel_strategy)
@settings(max_examples=50)
def test_classes_cmodel_instantiation(instance):
    assert isinstance(instance, classes_CModel)
