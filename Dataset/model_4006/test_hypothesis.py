import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Namespace,
    NamedElement,
    classes_Class,
    classes_Package,
    Element,
    classes_Root,
    classes_Namespace,
    classes_NamedElement,
    classes_Element,
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



def test_classes_class_is_not_abstract():
    assert not inspect.isabstract(classes_Class)


def test_classes_class_constructor_exists():
    assert callable(classes_Class.__init__)


def test_classes_class_constructor_args():
    sig = inspect.signature(classes_Class.__init__)
    params = list(sig.parameters.keys())



def test_classes_package_is_not_abstract():
    assert not inspect.isabstract(classes_Package)


def test_classes_package_constructor_exists():
    assert callable(classes_Package.__init__)


def test_classes_package_constructor_args():
    sig = inspect.signature(classes_Package.__init__)
    params = list(sig.parameters.keys())



def test_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_element_constructor_exists():
    assert callable(Element.__init__)


def test_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_classes_root_is_not_abstract():
    assert not inspect.isabstract(classes_Root)


def test_classes_root_constructor_exists():
    assert callable(classes_Root.__init__)


def test_classes_root_constructor_args():
    sig = inspect.signature(classes_Root.__init__)
    params = list(sig.parameters.keys())



def test_classes_namespace_is_not_abstract():
    assert not inspect.isabstract(classes_Namespace)


def test_classes_namespace_constructor_exists():
    assert callable(classes_Namespace.__init__)


def test_classes_namespace_constructor_args():
    sig = inspect.signature(classes_Namespace.__init__)
    params = list(sig.parameters.keys())



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



def test_classes_element_is_not_abstract():
    assert not inspect.isabstract(classes_Element)


def test_classes_element_constructor_exists():
    assert callable(classes_Element.__init__)


def test_classes_element_constructor_args():
    sig = inspect.signature(classes_Element.__init__)
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
classes_Class_strategy = st.builds(
    classes_Class,
)
classes_Package_strategy = st.builds(
    classes_Package,
)
Element_strategy = st.builds(
    Element,
)
classes_Root_strategy = st.builds(
    classes_Root,
)
classes_Namespace_strategy = st.builds(
    classes_Namespace,
)
classes_NamedElement_strategy = st.builds(
    classes_NamedElement,
    name=
        safe_text
)
classes_Element_strategy = st.builds(
    classes_Element,
)

@given(instance=Namespace_strategy)
@settings(max_examples=50)
def test_namespace_instantiation(instance):
    assert isinstance(instance, Namespace)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=classes_Class_strategy)
@settings(max_examples=50)
def test_classes_class_instantiation(instance):
    assert isinstance(instance, classes_Class)

@given(instance=classes_Package_strategy)
@settings(max_examples=50)
def test_classes_package_instantiation(instance):
    assert isinstance(instance, classes_Package)

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=classes_Root_strategy)
@settings(max_examples=50)
def test_classes_root_instantiation(instance):
    assert isinstance(instance, classes_Root)

@given(instance=classes_Namespace_strategy)
@settings(max_examples=50)
def test_classes_namespace_instantiation(instance):
    assert isinstance(instance, classes_Namespace)

@given(instance=classes_NamedElement_strategy)
@settings(max_examples=50)
def test_classes_namedelement_instantiation(instance):
    assert isinstance(instance, classes_NamedElement)



@given(instance=classes_NamedElement_strategy)
def test_classes_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=classes_Element_strategy)
@settings(max_examples=50)
def test_classes_element_instantiation(instance):
    assert isinstance(instance, classes_Element)
