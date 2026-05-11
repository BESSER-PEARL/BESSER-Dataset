import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    uml::UMLModelElement,
    Classifier,
    uml::PrimitiveDataType,
    PackageElement,
    uml::Association,
    uml::Classifier,
    uml::Class,
    UMLModelElement,
    uml::PackageElement,
    uml::Attribute,
    uml::Package,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_uml::umlmodelelement_is_not_abstract():
    assert not inspect.isabstract(uml::UMLModelElement)


def test_uml::umlmodelelement_constructor_exists():
    assert callable(uml::UMLModelElement.__init__)


def test_uml::umlmodelelement_constructor_args():
    sig = inspect.signature(uml::UMLModelElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "kind" in params, "Missing parameter 'kind'"

def test_uml::umlmodelelement_has_name():
    assert hasattr(uml::UMLModelElement, "name")
    descriptor = None
    for klass in uml::UMLModelElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_uml::umlmodelelement_has_kind():
    assert hasattr(uml::UMLModelElement, "kind")
    descriptor = None
    for klass in uml::UMLModelElement.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_classifier_is_not_abstract():
    assert not inspect.isabstract(Classifier)


def test_classifier_constructor_exists():
    assert callable(Classifier.__init__)


def test_classifier_constructor_args():
    sig = inspect.signature(Classifier.__init__)
    params = list(sig.parameters.keys())



def test_uml::primitivedatatype_is_not_abstract():
    assert not inspect.isabstract(uml::PrimitiveDataType)


def test_uml::primitivedatatype_constructor_exists():
    assert callable(uml::PrimitiveDataType.__init__)


def test_uml::primitivedatatype_constructor_args():
    sig = inspect.signature(uml::PrimitiveDataType.__init__)
    params = list(sig.parameters.keys())



def test_packageelement_is_not_abstract():
    assert not inspect.isabstract(PackageElement)


def test_packageelement_constructor_exists():
    assert callable(PackageElement.__init__)


def test_packageelement_constructor_args():
    sig = inspect.signature(PackageElement.__init__)
    params = list(sig.parameters.keys())



def test_uml::association_is_not_abstract():
    assert not inspect.isabstract(uml::Association)


def test_uml::association_constructor_exists():
    assert callable(uml::Association.__init__)


def test_uml::association_constructor_args():
    sig = inspect.signature(uml::Association.__init__)
    params = list(sig.parameters.keys())



def test_uml::classifier_is_not_abstract():
    assert not inspect.isabstract(uml::Classifier)


def test_uml::classifier_constructor_exists():
    assert callable(uml::Classifier.__init__)


def test_uml::classifier_constructor_args():
    sig = inspect.signature(uml::Classifier.__init__)
    params = list(sig.parameters.keys())



def test_uml::class_is_not_abstract():
    assert not inspect.isabstract(uml::Class)


def test_uml::class_constructor_exists():
    assert callable(uml::Class.__init__)


def test_uml::class_constructor_args():
    sig = inspect.signature(uml::Class.__init__)
    params = list(sig.parameters.keys())



def test_umlmodelelement_is_not_abstract():
    assert not inspect.isabstract(UMLModelElement)


def test_umlmodelelement_constructor_exists():
    assert callable(UMLModelElement.__init__)


def test_umlmodelelement_constructor_args():
    sig = inspect.signature(UMLModelElement.__init__)
    params = list(sig.parameters.keys())



def test_uml::packageelement_is_not_abstract():
    assert not inspect.isabstract(uml::PackageElement)


def test_uml::packageelement_constructor_exists():
    assert callable(uml::PackageElement.__init__)


def test_uml::packageelement_constructor_args():
    sig = inspect.signature(uml::PackageElement.__init__)
    params = list(sig.parameters.keys())



def test_uml::attribute_is_not_abstract():
    assert not inspect.isabstract(uml::Attribute)


def test_uml::attribute_constructor_exists():
    assert callable(uml::Attribute.__init__)


def test_uml::attribute_constructor_args():
    sig = inspect.signature(uml::Attribute.__init__)
    params = list(sig.parameters.keys())



def test_uml::package_is_not_abstract():
    assert not inspect.isabstract(uml::Package)


def test_uml::package_constructor_exists():
    assert callable(uml::Package.__init__)


def test_uml::package_constructor_args():
    sig = inspect.signature(uml::Package.__init__)
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
uml::UMLModelElement_strategy = st.builds(
    uml::UMLModelElement,
    name=
        safe_text,
    kind=
        safe_text
)
Classifier_strategy = st.builds(
    Classifier,
)
uml::PrimitiveDataType_strategy = st.builds(
    uml::PrimitiveDataType,
)
PackageElement_strategy = st.builds(
    PackageElement,
)
uml::Association_strategy = st.builds(
    uml::Association,
)
uml::Classifier_strategy = st.builds(
    uml::Classifier,
)
uml::Class_strategy = st.builds(
    uml::Class,
)
UMLModelElement_strategy = st.builds(
    UMLModelElement,
)
uml::PackageElement_strategy = st.builds(
    uml::PackageElement,
)
uml::Attribute_strategy = st.builds(
    uml::Attribute,
)
uml::Package_strategy = st.builds(
    uml::Package,
)

@given(instance=uml::UMLModelElement_strategy)
@settings(max_examples=50)
def test_uml::umlmodelelement_instantiation(instance):
    assert isinstance(instance, uml::UMLModelElement)

@given(instance=uml::UMLModelElement_strategy)
def test_uml::umlmodelelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=uml::UMLModelElement_strategy)
def test_uml::umlmodelelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=uml::UMLModelElement_strategy)
def test_uml::umlmodelelement_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=uml::UMLModelElement_strategy)
def test_uml::umlmodelelement_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=uml::PrimitiveDataType_strategy)
@settings(max_examples=50)
def test_uml::primitivedatatype_instantiation(instance):
    assert isinstance(instance, uml::PrimitiveDataType)

@given(instance=PackageElement_strategy)
@settings(max_examples=50)
def test_packageelement_instantiation(instance):
    assert isinstance(instance, PackageElement)

@given(instance=uml::Association_strategy)
@settings(max_examples=50)
def test_uml::association_instantiation(instance):
    assert isinstance(instance, uml::Association)

@given(instance=uml::Classifier_strategy)
@settings(max_examples=50)
def test_uml::classifier_instantiation(instance):
    assert isinstance(instance, uml::Classifier)

@given(instance=uml::Class_strategy)
@settings(max_examples=50)
def test_uml::class_instantiation(instance):
    assert isinstance(instance, uml::Class)

@given(instance=UMLModelElement_strategy)
@settings(max_examples=50)
def test_umlmodelelement_instantiation(instance):
    assert isinstance(instance, UMLModelElement)

@given(instance=uml::PackageElement_strategy)
@settings(max_examples=50)
def test_uml::packageelement_instantiation(instance):
    assert isinstance(instance, uml::PackageElement)

@given(instance=uml::Attribute_strategy)
@settings(max_examples=50)
def test_uml::attribute_instantiation(instance):
    assert isinstance(instance, uml::Attribute)

@given(instance=uml::Package_strategy)
@settings(max_examples=50)
def test_uml::package_instantiation(instance):
    assert isinstance(instance, uml::Package)
