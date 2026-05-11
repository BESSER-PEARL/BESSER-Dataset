import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Namespace,
    NamedElement,
    classes::Class,
    classes::Package,
    Element,
    classes::Root,
    classes::Namespace,
    classes::NamedElement,
    classes::Element,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_namespace_is_not_abstract():
    assert not inspect.isabstract(Namespace)


def test_namespace_constructor_exists():
    assert callable(Namespace.__init__)


def test_namespace_constructor_args():
    sig = inspect.signature(Namespace.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_classes::class_is_not_abstract():
    assert not inspect.isabstract(classes::Class)


def test_classes::class_constructor_exists():
    assert callable(classes::Class.__init__)


def test_classes::class_constructor_args():
    sig = inspect.signature(classes::Class.__init__)
    params = list(sig.parameters.keys())



def test_classes::package_is_not_abstract():
    assert not inspect.isabstract(classes::Package)


def test_classes::package_constructor_exists():
    assert callable(classes::Package.__init__)


def test_classes::package_constructor_args():
    sig = inspect.signature(classes::Package.__init__)
    params = list(sig.parameters.keys())



def test_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_element_constructor_exists():
    assert callable(Element.__init__)


def test_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_classes::root_is_not_abstract():
    assert not inspect.isabstract(classes::Root)


def test_classes::root_constructor_exists():
    assert callable(classes::Root.__init__)


def test_classes::root_constructor_args():
    sig = inspect.signature(classes::Root.__init__)
    params = list(sig.parameters.keys())



def test_classes::namespace_is_not_abstract():
    assert not inspect.isabstract(classes::Namespace)


def test_classes::namespace_constructor_exists():
    assert callable(classes::Namespace.__init__)


def test_classes::namespace_constructor_args():
    sig = inspect.signature(classes::Namespace.__init__)
    params = list(sig.parameters.keys())



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



def test_classes::element_is_not_abstract():
    assert not inspect.isabstract(classes::Element)


def test_classes::element_constructor_exists():
    assert callable(classes::Element.__init__)


def test_classes::element_constructor_args():
    sig = inspect.signature(classes::Element.__init__)
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
Namespace_strategy = st.builds(
    Namespace,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
classes::Class_strategy = st.builds(
    classes::Class,
)
classes::Package_strategy = st.builds(
    classes::Package,
)
Element_strategy = st.builds(
    Element,
)
classes::Root_strategy = st.builds(
    classes::Root,
)
classes::Namespace_strategy = st.builds(
    classes::Namespace,
)
classes::NamedElement_strategy = st.builds(
    classes::NamedElement,
    name=
        safe_text
)
classes::Element_strategy = st.builds(
    classes::Element,
)

@given(instance=Namespace_strategy)
@settings(max_examples=50)
def test_namespace_instantiation(instance):
    assert isinstance(instance, Namespace)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=classes::Class_strategy)
@settings(max_examples=50)
def test_classes::class_instantiation(instance):
    assert isinstance(instance, classes::Class)

@given(instance=classes::Package_strategy)
@settings(max_examples=50)
def test_classes::package_instantiation(instance):
    assert isinstance(instance, classes::Package)

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=classes::Root_strategy)
@settings(max_examples=50)
def test_classes::root_instantiation(instance):
    assert isinstance(instance, classes::Root)

@given(instance=classes::Namespace_strategy)
@settings(max_examples=50)
def test_classes::namespace_instantiation(instance):
    assert isinstance(instance, classes::Namespace)

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

@given(instance=classes::Element_strategy)
@settings(max_examples=50)
def test_classes::element_instantiation(instance):
    assert isinstance(instance, classes::Element)
