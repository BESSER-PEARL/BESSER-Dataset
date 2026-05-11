import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    StructuralFeature,
    simpleuml::Property,
    Classifier,
    simpleuml::Class,
    Feature,
    simpleuml::StructuralFeature,
    simpleuml::Generalization,
    Type,
    simpleuml::Classifier,
    NamedElement,
    simpleuml::Type,
    simpleuml::Feature,
    simpleuml::NamedElement,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_structuralfeature_is_not_abstract():
    assert not inspect.isabstract(StructuralFeature)


def test_structuralfeature_constructor_exists():
    assert callable(StructuralFeature.__init__)


def test_structuralfeature_constructor_args():
    sig = inspect.signature(StructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_simpleuml::property_is_not_abstract():
    assert not inspect.isabstract(simpleuml::Property)


def test_simpleuml::property_constructor_exists():
    assert callable(simpleuml::Property.__init__)


def test_simpleuml::property_constructor_args():
    sig = inspect.signature(simpleuml::Property.__init__)
    params = list(sig.parameters.keys())



def test_classifier_is_not_abstract():
    assert not inspect.isabstract(Classifier)


def test_classifier_constructor_exists():
    assert callable(Classifier.__init__)


def test_classifier_constructor_args():
    sig = inspect.signature(Classifier.__init__)
    params = list(sig.parameters.keys())



def test_simpleuml::class_is_not_abstract():
    assert not inspect.isabstract(simpleuml::Class)


def test_simpleuml::class_constructor_exists():
    assert callable(simpleuml::Class.__init__)


def test_simpleuml::class_constructor_args():
    sig = inspect.signature(simpleuml::Class.__init__)
    params = list(sig.parameters.keys())



def test_feature_is_not_abstract():
    assert not inspect.isabstract(Feature)


def test_feature_constructor_exists():
    assert callable(Feature.__init__)


def test_feature_constructor_args():
    sig = inspect.signature(Feature.__init__)
    params = list(sig.parameters.keys())



def test_simpleuml::structuralfeature_is_not_abstract():
    assert not inspect.isabstract(simpleuml::StructuralFeature)


def test_simpleuml::structuralfeature_constructor_exists():
    assert callable(simpleuml::StructuralFeature.__init__)


def test_simpleuml::structuralfeature_constructor_args():
    sig = inspect.signature(simpleuml::StructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_simpleuml::generalization_is_not_abstract():
    assert not inspect.isabstract(simpleuml::Generalization)


def test_simpleuml::generalization_constructor_exists():
    assert callable(simpleuml::Generalization.__init__)


def test_simpleuml::generalization_constructor_args():
    sig = inspect.signature(simpleuml::Generalization.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_simpleuml::classifier_is_not_abstract():
    assert not inspect.isabstract(simpleuml::Classifier)


def test_simpleuml::classifier_constructor_exists():
    assert callable(simpleuml::Classifier.__init__)


def test_simpleuml::classifier_constructor_args():
    sig = inspect.signature(simpleuml::Classifier.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_simpleuml::type_is_not_abstract():
    assert not inspect.isabstract(simpleuml::Type)


def test_simpleuml::type_constructor_exists():
    assert callable(simpleuml::Type.__init__)


def test_simpleuml::type_constructor_args():
    sig = inspect.signature(simpleuml::Type.__init__)
    params = list(sig.parameters.keys())



def test_simpleuml::feature_is_not_abstract():
    assert not inspect.isabstract(simpleuml::Feature)


def test_simpleuml::feature_constructor_exists():
    assert callable(simpleuml::Feature.__init__)


def test_simpleuml::feature_constructor_args():
    sig = inspect.signature(simpleuml::Feature.__init__)
    params = list(sig.parameters.keys())



def test_simpleuml::namedelement_is_not_abstract():
    assert not inspect.isabstract(simpleuml::NamedElement)


def test_simpleuml::namedelement_constructor_exists():
    assert callable(simpleuml::NamedElement.__init__)


def test_simpleuml::namedelement_constructor_args():
    sig = inspect.signature(simpleuml::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simpleuml::namedelement_has_name():
    assert hasattr(simpleuml::NamedElement, "name")
    descriptor = None
    for klass in simpleuml::NamedElement.__mro__:
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
StructuralFeature_strategy = st.builds(
    StructuralFeature,
)
simpleuml::Property_strategy = st.builds(
    simpleuml::Property,
)
Classifier_strategy = st.builds(
    Classifier,
)
simpleuml::Class_strategy = st.builds(
    simpleuml::Class,
)
Feature_strategy = st.builds(
    Feature,
)
simpleuml::StructuralFeature_strategy = st.builds(
    simpleuml::StructuralFeature,
)
simpleuml::Generalization_strategy = st.builds(
    simpleuml::Generalization,
)
Type_strategy = st.builds(
    Type,
)
simpleuml::Classifier_strategy = st.builds(
    simpleuml::Classifier,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
simpleuml::Type_strategy = st.builds(
    simpleuml::Type,
)
simpleuml::Feature_strategy = st.builds(
    simpleuml::Feature,
)
simpleuml::NamedElement_strategy = st.builds(
    simpleuml::NamedElement,
    name=
        safe_text
)

@given(instance=StructuralFeature_strategy)
@settings(max_examples=50)
def test_structuralfeature_instantiation(instance):
    assert isinstance(instance, StructuralFeature)

@given(instance=simpleuml::Property_strategy)
@settings(max_examples=50)
def test_simpleuml::property_instantiation(instance):
    assert isinstance(instance, simpleuml::Property)

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=simpleuml::Class_strategy)
@settings(max_examples=50)
def test_simpleuml::class_instantiation(instance):
    assert isinstance(instance, simpleuml::Class)

@given(instance=Feature_strategy)
@settings(max_examples=50)
def test_feature_instantiation(instance):
    assert isinstance(instance, Feature)

@given(instance=simpleuml::StructuralFeature_strategy)
@settings(max_examples=50)
def test_simpleuml::structuralfeature_instantiation(instance):
    assert isinstance(instance, simpleuml::StructuralFeature)

@given(instance=simpleuml::Generalization_strategy)
@settings(max_examples=50)
def test_simpleuml::generalization_instantiation(instance):
    assert isinstance(instance, simpleuml::Generalization)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=simpleuml::Classifier_strategy)
@settings(max_examples=50)
def test_simpleuml::classifier_instantiation(instance):
    assert isinstance(instance, simpleuml::Classifier)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=simpleuml::Type_strategy)
@settings(max_examples=50)
def test_simpleuml::type_instantiation(instance):
    assert isinstance(instance, simpleuml::Type)

@given(instance=simpleuml::Feature_strategy)
@settings(max_examples=50)
def test_simpleuml::feature_instantiation(instance):
    assert isinstance(instance, simpleuml::Feature)

@given(instance=simpleuml::NamedElement_strategy)
@settings(max_examples=50)
def test_simpleuml::namedelement_instantiation(instance):
    assert isinstance(instance, simpleuml::NamedElement)

@given(instance=simpleuml::NamedElement_strategy)
def test_simpleuml::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=simpleuml::NamedElement_strategy)
def test_simpleuml::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
