import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    PackageElement,
    simpleUml_Classifier,
    simpleUml_UMLModelElement,
    simpleUml_Association,
    simpleUml_Attribute,
    Classifier,
    simpleUml_Class,
    UMLModelElement,
    simpleUml_PackageElement,
    simpleUml_Package,
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



def test_simpleuml_classifier_is_not_abstract():
    assert not inspect.isabstract(simpleUml_Classifier)


def test_simpleuml_classifier_constructor_exists():
    assert callable(simpleUml_Classifier.__init__)


def test_simpleuml_classifier_constructor_args():
    sig = inspect.signature(simpleUml_Classifier.__init__)
    params = list(sig.parameters.keys())



def test_simpleuml_umlmodelelement_is_not_abstract():
    assert not inspect.isabstract(simpleUml_UMLModelElement)


def test_simpleuml_umlmodelelement_constructor_exists():
    assert callable(simpleUml_UMLModelElement.__init__)


def test_simpleuml_umlmodelelement_constructor_args():
    sig = inspect.signature(simpleUml_UMLModelElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "kind" in params, "Missing parameter 'kind'"

def test_simpleuml_umlmodelelement_has_name():
    assert hasattr(simpleUml_UMLModelElement, "name")
    descriptor = None
    for klass in simpleUml_UMLModelElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_simpleuml_umlmodelelement_has_kind():
    assert hasattr(simpleUml_UMLModelElement, "kind")
    descriptor = None
    for klass in simpleUml_UMLModelElement.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_simpleuml_association_is_not_abstract():
    assert not inspect.isabstract(simpleUml_Association)


def test_simpleuml_association_constructor_exists():
    assert callable(simpleUml_Association.__init__)


def test_simpleuml_association_constructor_args():
    sig = inspect.signature(simpleUml_Association.__init__)
    params = list(sig.parameters.keys())



def test_simpleuml_attribute_is_not_abstract():
    assert not inspect.isabstract(simpleUml_Attribute)


def test_simpleuml_attribute_constructor_exists():
    assert callable(simpleUml_Attribute.__init__)


def test_simpleuml_attribute_constructor_args():
    sig = inspect.signature(simpleUml_Attribute.__init__)
    params = list(sig.parameters.keys())



def test_classifier_is_not_abstract():
    assert not inspect.isabstract(Classifier)


def test_classifier_constructor_exists():
    assert callable(Classifier.__init__)


def test_classifier_constructor_args():
    sig = inspect.signature(Classifier.__init__)
    params = list(sig.parameters.keys())



def test_simpleuml_class_is_not_abstract():
    assert not inspect.isabstract(simpleUml_Class)


def test_simpleuml_class_constructor_exists():
    assert callable(simpleUml_Class.__init__)


def test_simpleuml_class_constructor_args():
    sig = inspect.signature(simpleUml_Class.__init__)
    params = list(sig.parameters.keys())



def test_umlmodelelement_is_not_abstract():
    assert not inspect.isabstract(UMLModelElement)


def test_umlmodelelement_constructor_exists():
    assert callable(UMLModelElement.__init__)


def test_umlmodelelement_constructor_args():
    sig = inspect.signature(UMLModelElement.__init__)
    params = list(sig.parameters.keys())



def test_simpleuml_packageelement_is_not_abstract():
    assert not inspect.isabstract(simpleUml_PackageElement)


def test_simpleuml_packageelement_constructor_exists():
    assert callable(simpleUml_PackageElement.__init__)


def test_simpleuml_packageelement_constructor_args():
    sig = inspect.signature(simpleUml_PackageElement.__init__)
    params = list(sig.parameters.keys())



def test_simpleuml_package_is_not_abstract():
    assert not inspect.isabstract(simpleUml_Package)


def test_simpleuml_package_constructor_exists():
    assert callable(simpleUml_Package.__init__)


def test_simpleuml_package_constructor_args():
    sig = inspect.signature(simpleUml_Package.__init__)
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
simpleUml_Classifier_strategy = st.builds(
    simpleUml_Classifier,
)
simpleUml_UMLModelElement_strategy = st.builds(
    simpleUml_UMLModelElement,
    name=
        safe_text,
    kind=
        safe_text
)
simpleUml_Association_strategy = st.builds(
    simpleUml_Association,
)
simpleUml_Attribute_strategy = st.builds(
    simpleUml_Attribute,
)
Classifier_strategy = st.builds(
    Classifier,
)
simpleUml_Class_strategy = st.builds(
    simpleUml_Class,
)
UMLModelElement_strategy = st.builds(
    UMLModelElement,
)
simpleUml_PackageElement_strategy = st.builds(
    simpleUml_PackageElement,
)
simpleUml_Package_strategy = st.builds(
    simpleUml_Package,
)

@given(instance=PackageElement_strategy)
@settings(max_examples=50)
def test_packageelement_instantiation(instance):
    assert isinstance(instance, PackageElement)

@given(instance=simpleUml_Classifier_strategy)
@settings(max_examples=50)
def test_simpleuml_classifier_instantiation(instance):
    assert isinstance(instance, simpleUml_Classifier)

@given(instance=simpleUml_UMLModelElement_strategy)
@settings(max_examples=50)
def test_simpleuml_umlmodelelement_instantiation(instance):
    assert isinstance(instance, simpleUml_UMLModelElement)



@given(instance=simpleUml_UMLModelElement_strategy)
def test_simpleuml_umlmodelelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=simpleUml_UMLModelElement_strategy)
def test_simpleuml_umlmodelelement_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=simpleUml_Association_strategy)
@settings(max_examples=50)
def test_simpleuml_association_instantiation(instance):
    assert isinstance(instance, simpleUml_Association)

@given(instance=simpleUml_Attribute_strategy)
@settings(max_examples=50)
def test_simpleuml_attribute_instantiation(instance):
    assert isinstance(instance, simpleUml_Attribute)

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=simpleUml_Class_strategy)
@settings(max_examples=50)
def test_simpleuml_class_instantiation(instance):
    assert isinstance(instance, simpleUml_Class)

@given(instance=UMLModelElement_strategy)
@settings(max_examples=50)
def test_umlmodelelement_instantiation(instance):
    assert isinstance(instance, UMLModelElement)

@given(instance=simpleUml_PackageElement_strategy)
@settings(max_examples=50)
def test_simpleuml_packageelement_instantiation(instance):
    assert isinstance(instance, simpleUml_PackageElement)

@given(instance=simpleUml_Package_strategy)
@settings(max_examples=50)
def test_simpleuml_package_instantiation(instance):
    assert isinstance(instance, simpleUml_Package)
