import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    PackageElement,
    simpleUml::Classifier,
    simpleUml::UMLModelElement,
    simpleUml::Association,
    simpleUml::Attribute,
    Classifier,
    simpleUml::Class,
    UMLModelElement,
    simpleUml::PackageElement,
    simpleUml::Package,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_packageelement_is_not_abstract():
    assert not inspect.isabstract(PackageElement)


def test_packageelement_constructor_exists():
    assert callable(PackageElement.__init__)


def test_packageelement_constructor_args():
    sig = inspect.signature(PackageElement.__init__)
    params = list(sig.parameters.keys())



def test_simpleuml::classifier_is_not_abstract():
    assert not inspect.isabstract(simpleUml::Classifier)


def test_simpleuml::classifier_constructor_exists():
    assert callable(simpleUml::Classifier.__init__)


def test_simpleuml::classifier_constructor_args():
    sig = inspect.signature(simpleUml::Classifier.__init__)
    params = list(sig.parameters.keys())



def test_simpleuml::umlmodelelement_is_not_abstract():
    assert not inspect.isabstract(simpleUml::UMLModelElement)


def test_simpleuml::umlmodelelement_constructor_exists():
    assert callable(simpleUml::UMLModelElement.__init__)


def test_simpleuml::umlmodelelement_constructor_args():
    sig = inspect.signature(simpleUml::UMLModelElement.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"
    assert "name" in params, "Missing parameter 'name'"

def test_simpleuml::umlmodelelement_has_kind():
    assert hasattr(simpleUml::UMLModelElement, "kind")
    descriptor = None
    for klass in simpleUml::UMLModelElement.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)

def test_simpleuml::umlmodelelement_has_name():
    assert hasattr(simpleUml::UMLModelElement, "name")
    descriptor = None
    for klass in simpleUml::UMLModelElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simpleuml::association_is_not_abstract():
    assert not inspect.isabstract(simpleUml::Association)


def test_simpleuml::association_constructor_exists():
    assert callable(simpleUml::Association.__init__)


def test_simpleuml::association_constructor_args():
    sig = inspect.signature(simpleUml::Association.__init__)
    params = list(sig.parameters.keys())



def test_simpleuml::attribute_is_not_abstract():
    assert not inspect.isabstract(simpleUml::Attribute)


def test_simpleuml::attribute_constructor_exists():
    assert callable(simpleUml::Attribute.__init__)


def test_simpleuml::attribute_constructor_args():
    sig = inspect.signature(simpleUml::Attribute.__init__)
    params = list(sig.parameters.keys())



def test_classifier_is_not_abstract():
    assert not inspect.isabstract(Classifier)


def test_classifier_constructor_exists():
    assert callable(Classifier.__init__)


def test_classifier_constructor_args():
    sig = inspect.signature(Classifier.__init__)
    params = list(sig.parameters.keys())



def test_simpleuml::class_is_not_abstract():
    assert not inspect.isabstract(simpleUml::Class)


def test_simpleuml::class_constructor_exists():
    assert callable(simpleUml::Class.__init__)


def test_simpleuml::class_constructor_args():
    sig = inspect.signature(simpleUml::Class.__init__)
    params = list(sig.parameters.keys())



def test_umlmodelelement_is_not_abstract():
    assert not inspect.isabstract(UMLModelElement)


def test_umlmodelelement_constructor_exists():
    assert callable(UMLModelElement.__init__)


def test_umlmodelelement_constructor_args():
    sig = inspect.signature(UMLModelElement.__init__)
    params = list(sig.parameters.keys())



def test_simpleuml::packageelement_is_not_abstract():
    assert not inspect.isabstract(simpleUml::PackageElement)


def test_simpleuml::packageelement_constructor_exists():
    assert callable(simpleUml::PackageElement.__init__)


def test_simpleuml::packageelement_constructor_args():
    sig = inspect.signature(simpleUml::PackageElement.__init__)
    params = list(sig.parameters.keys())



def test_simpleuml::package_is_not_abstract():
    assert not inspect.isabstract(simpleUml::Package)


def test_simpleuml::package_constructor_exists():
    assert callable(simpleUml::Package.__init__)


def test_simpleuml::package_constructor_args():
    sig = inspect.signature(simpleUml::Package.__init__)
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
PackageElement_strategy = st.builds(
    PackageElement,
)
simpleUml::Classifier_strategy = st.builds(
    simpleUml::Classifier,
)
simpleUml::UMLModelElement_strategy = st.builds(
    simpleUml::UMLModelElement,
    kind=
        safe_text,
    name=
        safe_text
)
simpleUml::Association_strategy = st.builds(
    simpleUml::Association,
)
simpleUml::Attribute_strategy = st.builds(
    simpleUml::Attribute,
)
Classifier_strategy = st.builds(
    Classifier,
)
simpleUml::Class_strategy = st.builds(
    simpleUml::Class,
)
UMLModelElement_strategy = st.builds(
    UMLModelElement,
)
simpleUml::PackageElement_strategy = st.builds(
    simpleUml::PackageElement,
)
simpleUml::Package_strategy = st.builds(
    simpleUml::Package,
)

@given(instance=PackageElement_strategy)
@settings(max_examples=50)
def test_packageelement_instantiation(instance):
    assert isinstance(instance, PackageElement)

@given(instance=simpleUml::Classifier_strategy)
@settings(max_examples=50)
def test_simpleuml::classifier_instantiation(instance):
    assert isinstance(instance, simpleUml::Classifier)

@given(instance=simpleUml::UMLModelElement_strategy)
@settings(max_examples=50)
def test_simpleuml::umlmodelelement_instantiation(instance):
    assert isinstance(instance, simpleUml::UMLModelElement)

@given(instance=simpleUml::UMLModelElement_strategy)
def test_simpleuml::umlmodelelement_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=simpleUml::UMLModelElement_strategy)
def test_simpleuml::umlmodelelement_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=simpleUml::UMLModelElement_strategy)
def test_simpleuml::umlmodelelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=simpleUml::UMLModelElement_strategy)
def test_simpleuml::umlmodelelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simpleUml::Association_strategy)
@settings(max_examples=50)
def test_simpleuml::association_instantiation(instance):
    assert isinstance(instance, simpleUml::Association)

@given(instance=simpleUml::Attribute_strategy)
@settings(max_examples=50)
def test_simpleuml::attribute_instantiation(instance):
    assert isinstance(instance, simpleUml::Attribute)

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=simpleUml::Class_strategy)
@settings(max_examples=50)
def test_simpleuml::class_instantiation(instance):
    assert isinstance(instance, simpleUml::Class)

@given(instance=UMLModelElement_strategy)
@settings(max_examples=50)
def test_umlmodelelement_instantiation(instance):
    assert isinstance(instance, UMLModelElement)

@given(instance=simpleUml::PackageElement_strategy)
@settings(max_examples=50)
def test_simpleuml::packageelement_instantiation(instance):
    assert isinstance(instance, simpleUml::PackageElement)

@given(instance=simpleUml::Package_strategy)
@settings(max_examples=50)
def test_simpleuml::package_instantiation(instance):
    assert isinstance(instance, simpleUml::Package)
