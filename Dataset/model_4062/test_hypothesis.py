import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    SimpleUML::UMLModelElement,
    Classifier,
    SimpleUML::PrimitiveDataType,
    SimpleUML::Class,
    UMLModelElement,
    SimpleUML::PackageElement,
    SimpleUML::Package,
    SimpleUML::Attribute,
    PackageElement,
    SimpleUML::Association,
    SimpleUML::Classifier,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_simpleuml::umlmodelelement_is_not_abstract():
    assert not inspect.isabstract(SimpleUML::UMLModelElement)


def test_simpleuml::umlmodelelement_constructor_exists():
    assert callable(SimpleUML::UMLModelElement.__init__)


def test_simpleuml::umlmodelelement_constructor_args():
    sig = inspect.signature(SimpleUML::UMLModelElement.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"
    assert "name" in params, "Missing parameter 'name'"

def test_simpleuml::umlmodelelement_has_kind():
    assert hasattr(SimpleUML::UMLModelElement, "kind")
    descriptor = None
    for klass in SimpleUML::UMLModelElement.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)

def test_simpleuml::umlmodelelement_has_name():
    assert hasattr(SimpleUML::UMLModelElement, "name")
    descriptor = None
    for klass in SimpleUML::UMLModelElement.__mro__:
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



def test_simpleuml::primitivedatatype_is_not_abstract():
    assert not inspect.isabstract(SimpleUML::PrimitiveDataType)


def test_simpleuml::primitivedatatype_constructor_exists():
    assert callable(SimpleUML::PrimitiveDataType.__init__)


def test_simpleuml::primitivedatatype_constructor_args():
    sig = inspect.signature(SimpleUML::PrimitiveDataType.__init__)
    params = list(sig.parameters.keys())



def test_simpleuml::class_is_not_abstract():
    assert not inspect.isabstract(SimpleUML::Class)


def test_simpleuml::class_constructor_exists():
    assert callable(SimpleUML::Class.__init__)


def test_simpleuml::class_constructor_args():
    sig = inspect.signature(SimpleUML::Class.__init__)
    params = list(sig.parameters.keys())



def test_umlmodelelement_is_not_abstract():
    assert not inspect.isabstract(UMLModelElement)


def test_umlmodelelement_constructor_exists():
    assert callable(UMLModelElement.__init__)


def test_umlmodelelement_constructor_args():
    sig = inspect.signature(UMLModelElement.__init__)
    params = list(sig.parameters.keys())



def test_simpleuml::packageelement_is_not_abstract():
    assert not inspect.isabstract(SimpleUML::PackageElement)


def test_simpleuml::packageelement_constructor_exists():
    assert callable(SimpleUML::PackageElement.__init__)


def test_simpleuml::packageelement_constructor_args():
    sig = inspect.signature(SimpleUML::PackageElement.__init__)
    params = list(sig.parameters.keys())



def test_simpleuml::package_is_not_abstract():
    assert not inspect.isabstract(SimpleUML::Package)


def test_simpleuml::package_constructor_exists():
    assert callable(SimpleUML::Package.__init__)


def test_simpleuml::package_constructor_args():
    sig = inspect.signature(SimpleUML::Package.__init__)
    params = list(sig.parameters.keys())



def test_simpleuml::attribute_is_not_abstract():
    assert not inspect.isabstract(SimpleUML::Attribute)


def test_simpleuml::attribute_constructor_exists():
    assert callable(SimpleUML::Attribute.__init__)


def test_simpleuml::attribute_constructor_args():
    sig = inspect.signature(SimpleUML::Attribute.__init__)
    params = list(sig.parameters.keys())



def test_packageelement_is_not_abstract():
    assert not inspect.isabstract(PackageElement)


def test_packageelement_constructor_exists():
    assert callable(PackageElement.__init__)


def test_packageelement_constructor_args():
    sig = inspect.signature(PackageElement.__init__)
    params = list(sig.parameters.keys())



def test_simpleuml::association_is_not_abstract():
    assert not inspect.isabstract(SimpleUML::Association)


def test_simpleuml::association_constructor_exists():
    assert callable(SimpleUML::Association.__init__)


def test_simpleuml::association_constructor_args():
    sig = inspect.signature(SimpleUML::Association.__init__)
    params = list(sig.parameters.keys())



def test_simpleuml::classifier_is_not_abstract():
    assert not inspect.isabstract(SimpleUML::Classifier)


def test_simpleuml::classifier_constructor_exists():
    assert callable(SimpleUML::Classifier.__init__)


def test_simpleuml::classifier_constructor_args():
    sig = inspect.signature(SimpleUML::Classifier.__init__)
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
SimpleUML::UMLModelElement_strategy = st.builds(
    SimpleUML::UMLModelElement,
    kind=
        safe_text,
    name=
        safe_text
)
Classifier_strategy = st.builds(
    Classifier,
)
SimpleUML::PrimitiveDataType_strategy = st.builds(
    SimpleUML::PrimitiveDataType,
)
SimpleUML::Class_strategy = st.builds(
    SimpleUML::Class,
)
UMLModelElement_strategy = st.builds(
    UMLModelElement,
)
SimpleUML::PackageElement_strategy = st.builds(
    SimpleUML::PackageElement,
)
SimpleUML::Package_strategy = st.builds(
    SimpleUML::Package,
)
SimpleUML::Attribute_strategy = st.builds(
    SimpleUML::Attribute,
)
PackageElement_strategy = st.builds(
    PackageElement,
)
SimpleUML::Association_strategy = st.builds(
    SimpleUML::Association,
)
SimpleUML::Classifier_strategy = st.builds(
    SimpleUML::Classifier,
)

@given(instance=SimpleUML::UMLModelElement_strategy)
@settings(max_examples=50)
def test_simpleuml::umlmodelelement_instantiation(instance):
    assert isinstance(instance, SimpleUML::UMLModelElement)

@given(instance=SimpleUML::UMLModelElement_strategy)
def test_simpleuml::umlmodelelement_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=SimpleUML::UMLModelElement_strategy)
def test_simpleuml::umlmodelelement_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=SimpleUML::UMLModelElement_strategy)
def test_simpleuml::umlmodelelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=SimpleUML::UMLModelElement_strategy)
def test_simpleuml::umlmodelelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=SimpleUML::PrimitiveDataType_strategy)
@settings(max_examples=50)
def test_simpleuml::primitivedatatype_instantiation(instance):
    assert isinstance(instance, SimpleUML::PrimitiveDataType)

@given(instance=SimpleUML::Class_strategy)
@settings(max_examples=50)
def test_simpleuml::class_instantiation(instance):
    assert isinstance(instance, SimpleUML::Class)

@given(instance=UMLModelElement_strategy)
@settings(max_examples=50)
def test_umlmodelelement_instantiation(instance):
    assert isinstance(instance, UMLModelElement)

@given(instance=SimpleUML::PackageElement_strategy)
@settings(max_examples=50)
def test_simpleuml::packageelement_instantiation(instance):
    assert isinstance(instance, SimpleUML::PackageElement)

@given(instance=SimpleUML::Package_strategy)
@settings(max_examples=50)
def test_simpleuml::package_instantiation(instance):
    assert isinstance(instance, SimpleUML::Package)

@given(instance=SimpleUML::Attribute_strategy)
@settings(max_examples=50)
def test_simpleuml::attribute_instantiation(instance):
    assert isinstance(instance, SimpleUML::Attribute)

@given(instance=PackageElement_strategy)
@settings(max_examples=50)
def test_packageelement_instantiation(instance):
    assert isinstance(instance, PackageElement)

@given(instance=SimpleUML::Association_strategy)
@settings(max_examples=50)
def test_simpleuml::association_instantiation(instance):
    assert isinstance(instance, SimpleUML::Association)

@given(instance=SimpleUML::Classifier_strategy)
@settings(max_examples=50)
def test_simpleuml::classifier_instantiation(instance):
    assert isinstance(instance, SimpleUML::Classifier)
