import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Classifier,
    UMLModelElement,
    umlMM::Package,
    umlMM::PackageElement,
    umlMM::Attribute,
    umlMM::Class,
    umlMM::UMLModelElement,
    umlMM::PrimitiveDataType,
    PackageElement,
    umlMM::Classifier,
    umlMM::Association,
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



def test_umlmodelelement_is_not_abstract():
    assert not inspect.isabstract(UMLModelElement)


def test_umlmodelelement_constructor_exists():
    assert callable(UMLModelElement.__init__)


def test_umlmodelelement_constructor_args():
    sig = inspect.signature(UMLModelElement.__init__)
    params = list(sig.parameters.keys())



def test_umlmm::package_is_not_abstract():
    assert not inspect.isabstract(umlMM::Package)


def test_umlmm::package_constructor_exists():
    assert callable(umlMM::Package.__init__)


def test_umlmm::package_constructor_args():
    sig = inspect.signature(umlMM::Package.__init__)
    params = list(sig.parameters.keys())



def test_umlmm::packageelement_is_not_abstract():
    assert not inspect.isabstract(umlMM::PackageElement)


def test_umlmm::packageelement_constructor_exists():
    assert callable(umlMM::PackageElement.__init__)


def test_umlmm::packageelement_constructor_args():
    sig = inspect.signature(umlMM::PackageElement.__init__)
    params = list(sig.parameters.keys())



def test_umlmm::attribute_is_not_abstract():
    assert not inspect.isabstract(umlMM::Attribute)


def test_umlmm::attribute_constructor_exists():
    assert callable(umlMM::Attribute.__init__)


def test_umlmm::attribute_constructor_args():
    sig = inspect.signature(umlMM::Attribute.__init__)
    params = list(sig.parameters.keys())



def test_umlmm::class_is_not_abstract():
    assert not inspect.isabstract(umlMM::Class)


def test_umlmm::class_constructor_exists():
    assert callable(umlMM::Class.__init__)


def test_umlmm::class_constructor_args():
    sig = inspect.signature(umlMM::Class.__init__)
    params = list(sig.parameters.keys())



def test_umlmm::umlmodelelement_is_not_abstract():
    assert not inspect.isabstract(umlMM::UMLModelElement)


def test_umlmm::umlmodelelement_constructor_exists():
    assert callable(umlMM::UMLModelElement.__init__)


def test_umlmm::umlmodelelement_constructor_args():
    sig = inspect.signature(umlMM::UMLModelElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "kind" in params, "Missing parameter 'kind'"

def test_umlmm::umlmodelelement_has_name():
    assert hasattr(umlMM::UMLModelElement, "name")
    descriptor = None
    for klass in umlMM::UMLModelElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_umlmm::umlmodelelement_has_kind():
    assert hasattr(umlMM::UMLModelElement, "kind")
    descriptor = None
    for klass in umlMM::UMLModelElement.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_umlmm::primitivedatatype_is_not_abstract():
    assert not inspect.isabstract(umlMM::PrimitiveDataType)


def test_umlmm::primitivedatatype_constructor_exists():
    assert callable(umlMM::PrimitiveDataType.__init__)


def test_umlmm::primitivedatatype_constructor_args():
    sig = inspect.signature(umlMM::PrimitiveDataType.__init__)
    params = list(sig.parameters.keys())



def test_packageelement_is_not_abstract():
    assert not inspect.isabstract(PackageElement)


def test_packageelement_constructor_exists():
    assert callable(PackageElement.__init__)


def test_packageelement_constructor_args():
    sig = inspect.signature(PackageElement.__init__)
    params = list(sig.parameters.keys())



def test_umlmm::classifier_is_not_abstract():
    assert not inspect.isabstract(umlMM::Classifier)


def test_umlmm::classifier_constructor_exists():
    assert callable(umlMM::Classifier.__init__)


def test_umlmm::classifier_constructor_args():
    sig = inspect.signature(umlMM::Classifier.__init__)
    params = list(sig.parameters.keys())



def test_umlmm::association_is_not_abstract():
    assert not inspect.isabstract(umlMM::Association)


def test_umlmm::association_constructor_exists():
    assert callable(umlMM::Association.__init__)


def test_umlmm::association_constructor_args():
    sig = inspect.signature(umlMM::Association.__init__)
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
UMLModelElement_strategy = st.builds(
    UMLModelElement,
)
umlMM::Package_strategy = st.builds(
    umlMM::Package,
)
umlMM::PackageElement_strategy = st.builds(
    umlMM::PackageElement,
)
umlMM::Attribute_strategy = st.builds(
    umlMM::Attribute,
)
umlMM::Class_strategy = st.builds(
    umlMM::Class,
)
umlMM::UMLModelElement_strategy = st.builds(
    umlMM::UMLModelElement,
    name=
        safe_text,
    kind=
        safe_text
)
umlMM::PrimitiveDataType_strategy = st.builds(
    umlMM::PrimitiveDataType,
)
PackageElement_strategy = st.builds(
    PackageElement,
)
umlMM::Classifier_strategy = st.builds(
    umlMM::Classifier,
)
umlMM::Association_strategy = st.builds(
    umlMM::Association,
)

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=UMLModelElement_strategy)
@settings(max_examples=50)
def test_umlmodelelement_instantiation(instance):
    assert isinstance(instance, UMLModelElement)

@given(instance=umlMM::Package_strategy)
@settings(max_examples=50)
def test_umlmm::package_instantiation(instance):
    assert isinstance(instance, umlMM::Package)

@given(instance=umlMM::PackageElement_strategy)
@settings(max_examples=50)
def test_umlmm::packageelement_instantiation(instance):
    assert isinstance(instance, umlMM::PackageElement)

@given(instance=umlMM::Attribute_strategy)
@settings(max_examples=50)
def test_umlmm::attribute_instantiation(instance):
    assert isinstance(instance, umlMM::Attribute)

@given(instance=umlMM::Class_strategy)
@settings(max_examples=50)
def test_umlmm::class_instantiation(instance):
    assert isinstance(instance, umlMM::Class)

@given(instance=umlMM::UMLModelElement_strategy)
@settings(max_examples=50)
def test_umlmm::umlmodelelement_instantiation(instance):
    assert isinstance(instance, umlMM::UMLModelElement)

@given(instance=umlMM::UMLModelElement_strategy)
def test_umlmm::umlmodelelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=umlMM::UMLModelElement_strategy)
def test_umlmm::umlmodelelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=umlMM::UMLModelElement_strategy)
def test_umlmm::umlmodelelement_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=umlMM::UMLModelElement_strategy)
def test_umlmm::umlmodelelement_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=umlMM::PrimitiveDataType_strategy)
@settings(max_examples=50)
def test_umlmm::primitivedatatype_instantiation(instance):
    assert isinstance(instance, umlMM::PrimitiveDataType)

@given(instance=PackageElement_strategy)
@settings(max_examples=50)
def test_packageelement_instantiation(instance):
    assert isinstance(instance, PackageElement)

@given(instance=umlMM::Classifier_strategy)
@settings(max_examples=50)
def test_umlmm::classifier_instantiation(instance):
    assert isinstance(instance, umlMM::Classifier)

@given(instance=umlMM::Association_strategy)
@settings(max_examples=50)
def test_umlmm::association_instantiation(instance):
    assert isinstance(instance, umlMM::Association)
