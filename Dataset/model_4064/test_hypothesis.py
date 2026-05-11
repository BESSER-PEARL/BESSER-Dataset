import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    simpleuml::UMLModelElement,
    UMLModelElement,
    simpleuml::Attribute,
    simpleuml::PackageElement,
    simpleuml::Package,
    Classifier,
    simpleuml::PrimitiveDataType,
    PackageElement,
    simpleuml::Association,
    simpleuml::Class,
    simpleuml::Classifier,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_simpleuml::umlmodelelement_is_not_abstract():
    assert not inspect.isabstract(simpleuml::UMLModelElement)


def test_simpleuml::umlmodelelement_constructor_exists():
    assert callable(simpleuml::UMLModelElement.__init__)


def test_simpleuml::umlmodelelement_constructor_args():
    sig = inspect.signature(simpleuml::UMLModelElement.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"
    assert "name" in params, "Missing parameter 'name'"

def test_simpleuml::umlmodelelement_has_kind():
    assert hasattr(simpleuml::UMLModelElement, "kind")
    descriptor = None
    for klass in simpleuml::UMLModelElement.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)

def test_simpleuml::umlmodelelement_has_name():
    assert hasattr(simpleuml::UMLModelElement, "name")
    descriptor = None
    for klass in simpleuml::UMLModelElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_umlmodelelement_is_not_abstract():
    assert not inspect.isabstract(UMLModelElement)


def test_umlmodelelement_constructor_exists():
    assert callable(UMLModelElement.__init__)


def test_umlmodelelement_constructor_args():
    sig = inspect.signature(UMLModelElement.__init__)
    params = list(sig.parameters.keys())



def test_simpleuml::attribute_is_not_abstract():
    assert not inspect.isabstract(simpleuml::Attribute)


def test_simpleuml::attribute_constructor_exists():
    assert callable(simpleuml::Attribute.__init__)


def test_simpleuml::attribute_constructor_args():
    sig = inspect.signature(simpleuml::Attribute.__init__)
    params = list(sig.parameters.keys())



def test_simpleuml::packageelement_is_not_abstract():
    assert not inspect.isabstract(simpleuml::PackageElement)


def test_simpleuml::packageelement_constructor_exists():
    assert callable(simpleuml::PackageElement.__init__)


def test_simpleuml::packageelement_constructor_args():
    sig = inspect.signature(simpleuml::PackageElement.__init__)
    params = list(sig.parameters.keys())



def test_simpleuml::package_is_not_abstract():
    assert not inspect.isabstract(simpleuml::Package)


def test_simpleuml::package_constructor_exists():
    assert callable(simpleuml::Package.__init__)


def test_simpleuml::package_constructor_args():
    sig = inspect.signature(simpleuml::Package.__init__)
    params = list(sig.parameters.keys())



def test_classifier_is_not_abstract():
    assert not inspect.isabstract(Classifier)


def test_classifier_constructor_exists():
    assert callable(Classifier.__init__)


def test_classifier_constructor_args():
    sig = inspect.signature(Classifier.__init__)
    params = list(sig.parameters.keys())



def test_simpleuml::primitivedatatype_is_not_abstract():
    assert not inspect.isabstract(simpleuml::PrimitiveDataType)


def test_simpleuml::primitivedatatype_constructor_exists():
    assert callable(simpleuml::PrimitiveDataType.__init__)


def test_simpleuml::primitivedatatype_constructor_args():
    sig = inspect.signature(simpleuml::PrimitiveDataType.__init__)
    params = list(sig.parameters.keys())



def test_packageelement_is_not_abstract():
    assert not inspect.isabstract(PackageElement)


def test_packageelement_constructor_exists():
    assert callable(PackageElement.__init__)


def test_packageelement_constructor_args():
    sig = inspect.signature(PackageElement.__init__)
    params = list(sig.parameters.keys())



def test_simpleuml::association_is_not_abstract():
    assert not inspect.isabstract(simpleuml::Association)


def test_simpleuml::association_constructor_exists():
    assert callable(simpleuml::Association.__init__)


def test_simpleuml::association_constructor_args():
    sig = inspect.signature(simpleuml::Association.__init__)
    params = list(sig.parameters.keys())



def test_simpleuml::class_is_not_abstract():
    assert not inspect.isabstract(simpleuml::Class)


def test_simpleuml::class_constructor_exists():
    assert callable(simpleuml::Class.__init__)


def test_simpleuml::class_constructor_args():
    sig = inspect.signature(simpleuml::Class.__init__)
    params = list(sig.parameters.keys())



def test_simpleuml::classifier_is_not_abstract():
    assert not inspect.isabstract(simpleuml::Classifier)


def test_simpleuml::classifier_constructor_exists():
    assert callable(simpleuml::Classifier.__init__)


def test_simpleuml::classifier_constructor_args():
    sig = inspect.signature(simpleuml::Classifier.__init__)
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
simpleuml::UMLModelElement_strategy = st.builds(
    simpleuml::UMLModelElement,
    kind=
        safe_text,
    name=
        safe_text
)
UMLModelElement_strategy = st.builds(
    UMLModelElement,
)
simpleuml::Attribute_strategy = st.builds(
    simpleuml::Attribute,
)
simpleuml::PackageElement_strategy = st.builds(
    simpleuml::PackageElement,
)
simpleuml::Package_strategy = st.builds(
    simpleuml::Package,
)
Classifier_strategy = st.builds(
    Classifier,
)
simpleuml::PrimitiveDataType_strategy = st.builds(
    simpleuml::PrimitiveDataType,
)
PackageElement_strategy = st.builds(
    PackageElement,
)
simpleuml::Association_strategy = st.builds(
    simpleuml::Association,
)
simpleuml::Class_strategy = st.builds(
    simpleuml::Class,
)
simpleuml::Classifier_strategy = st.builds(
    simpleuml::Classifier,
)

@given(instance=simpleuml::UMLModelElement_strategy)
@settings(max_examples=50)
def test_simpleuml::umlmodelelement_instantiation(instance):
    assert isinstance(instance, simpleuml::UMLModelElement)

@given(instance=simpleuml::UMLModelElement_strategy)
def test_simpleuml::umlmodelelement_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=simpleuml::UMLModelElement_strategy)
def test_simpleuml::umlmodelelement_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=simpleuml::UMLModelElement_strategy)
def test_simpleuml::umlmodelelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=simpleuml::UMLModelElement_strategy)
def test_simpleuml::umlmodelelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=UMLModelElement_strategy)
@settings(max_examples=50)
def test_umlmodelelement_instantiation(instance):
    assert isinstance(instance, UMLModelElement)

@given(instance=simpleuml::Attribute_strategy)
@settings(max_examples=50)
def test_simpleuml::attribute_instantiation(instance):
    assert isinstance(instance, simpleuml::Attribute)

@given(instance=simpleuml::PackageElement_strategy)
@settings(max_examples=50)
def test_simpleuml::packageelement_instantiation(instance):
    assert isinstance(instance, simpleuml::PackageElement)

@given(instance=simpleuml::Package_strategy)
@settings(max_examples=50)
def test_simpleuml::package_instantiation(instance):
    assert isinstance(instance, simpleuml::Package)

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=simpleuml::PrimitiveDataType_strategy)
@settings(max_examples=50)
def test_simpleuml::primitivedatatype_instantiation(instance):
    assert isinstance(instance, simpleuml::PrimitiveDataType)

@given(instance=PackageElement_strategy)
@settings(max_examples=50)
def test_packageelement_instantiation(instance):
    assert isinstance(instance, PackageElement)

@given(instance=simpleuml::Association_strategy)
@settings(max_examples=50)
def test_simpleuml::association_instantiation(instance):
    assert isinstance(instance, simpleuml::Association)

@given(instance=simpleuml::Class_strategy)
@settings(max_examples=50)
def test_simpleuml::class_instantiation(instance):
    assert isinstance(instance, simpleuml::Class)

@given(instance=simpleuml::Classifier_strategy)
@settings(max_examples=50)
def test_simpleuml::classifier_instantiation(instance):
    assert isinstance(instance, simpleuml::Classifier)
