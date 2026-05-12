import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    simpleuml_UMLModelElement,
    UMLModelElement,
    simpleuml_Package,
    simpleuml_PackageElement,
    simpleuml_Attribute,
    Classifier,
    simpleuml_PrimitiveDataType,
    PackageElement,
    simpleuml_Association,
    simpleuml_Class,
    simpleuml_Classifier,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_simpleuml_umlmodelelement_is_not_abstract():
    assert not inspect.isabstract(simpleuml_UMLModelElement)


def test_simpleuml_umlmodelelement_constructor_exists():
    assert callable(simpleuml_UMLModelElement.__init__)


def test_simpleuml_umlmodelelement_constructor_args():
    sig = inspect.signature(simpleuml_UMLModelElement.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"
    assert "name" in params, "Missing parameter 'name'"

def test_simpleuml_umlmodelelement_has_kind():
    assert hasattr(simpleuml_UMLModelElement, "kind")
    descriptor = None
    for klass in simpleuml_UMLModelElement.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)

def test_simpleuml_umlmodelelement_has_name():
    assert hasattr(simpleuml_UMLModelElement, "name")
    descriptor = None
    for klass in simpleuml_UMLModelElement.__mro__:
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



def test_simpleuml_package_is_not_abstract():
    assert not inspect.isabstract(simpleuml_Package)


def test_simpleuml_package_constructor_exists():
    assert callable(simpleuml_Package.__init__)


def test_simpleuml_package_constructor_args():
    sig = inspect.signature(simpleuml_Package.__init__)
    params = list(sig.parameters.keys())



def test_simpleuml_packageelement_is_not_abstract():
    assert not inspect.isabstract(simpleuml_PackageElement)


def test_simpleuml_packageelement_constructor_exists():
    assert callable(simpleuml_PackageElement.__init__)


def test_simpleuml_packageelement_constructor_args():
    sig = inspect.signature(simpleuml_PackageElement.__init__)
    params = list(sig.parameters.keys())



def test_simpleuml_attribute_is_not_abstract():
    assert not inspect.isabstract(simpleuml_Attribute)


def test_simpleuml_attribute_constructor_exists():
    assert callable(simpleuml_Attribute.__init__)


def test_simpleuml_attribute_constructor_args():
    sig = inspect.signature(simpleuml_Attribute.__init__)
    params = list(sig.parameters.keys())



def test_classifier_is_not_abstract():
    assert not inspect.isabstract(Classifier)


def test_classifier_constructor_exists():
    assert callable(Classifier.__init__)


def test_classifier_constructor_args():
    sig = inspect.signature(Classifier.__init__)
    params = list(sig.parameters.keys())



def test_simpleuml_primitivedatatype_is_not_abstract():
    assert not inspect.isabstract(simpleuml_PrimitiveDataType)


def test_simpleuml_primitivedatatype_constructor_exists():
    assert callable(simpleuml_PrimitiveDataType.__init__)


def test_simpleuml_primitivedatatype_constructor_args():
    sig = inspect.signature(simpleuml_PrimitiveDataType.__init__)
    params = list(sig.parameters.keys())



def test_packageelement_is_not_abstract():
    assert not inspect.isabstract(PackageElement)


def test_packageelement_constructor_exists():
    assert callable(PackageElement.__init__)


def test_packageelement_constructor_args():
    sig = inspect.signature(PackageElement.__init__)
    params = list(sig.parameters.keys())



def test_simpleuml_association_is_not_abstract():
    assert not inspect.isabstract(simpleuml_Association)


def test_simpleuml_association_constructor_exists():
    assert callable(simpleuml_Association.__init__)


def test_simpleuml_association_constructor_args():
    sig = inspect.signature(simpleuml_Association.__init__)
    params = list(sig.parameters.keys())



def test_simpleuml_class_is_not_abstract():
    assert not inspect.isabstract(simpleuml_Class)


def test_simpleuml_class_constructor_exists():
    assert callable(simpleuml_Class.__init__)


def test_simpleuml_class_constructor_args():
    sig = inspect.signature(simpleuml_Class.__init__)
    params = list(sig.parameters.keys())



def test_simpleuml_classifier_is_not_abstract():
    assert not inspect.isabstract(simpleuml_Classifier)


def test_simpleuml_classifier_constructor_exists():
    assert callable(simpleuml_Classifier.__init__)


def test_simpleuml_classifier_constructor_args():
    sig = inspect.signature(simpleuml_Classifier.__init__)
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
simpleuml_UMLModelElement_strategy = st.builds(
    simpleuml_UMLModelElement,
    kind=
        safe_text,
    name=
        safe_text
)
UMLModelElement_strategy = st.builds(
    UMLModelElement,
)
simpleuml_Package_strategy = st.builds(
    simpleuml_Package,
)
simpleuml_PackageElement_strategy = st.builds(
    simpleuml_PackageElement,
)
simpleuml_Attribute_strategy = st.builds(
    simpleuml_Attribute,
)
Classifier_strategy = st.builds(
    Classifier,
)
simpleuml_PrimitiveDataType_strategy = st.builds(
    simpleuml_PrimitiveDataType,
)
PackageElement_strategy = st.builds(
    PackageElement,
)
simpleuml_Association_strategy = st.builds(
    simpleuml_Association,
)
simpleuml_Class_strategy = st.builds(
    simpleuml_Class,
)
simpleuml_Classifier_strategy = st.builds(
    simpleuml_Classifier,
)

@given(instance=simpleuml_UMLModelElement_strategy)
@settings(max_examples=50)
def test_simpleuml_umlmodelelement_instantiation(instance):
    assert isinstance(instance, simpleuml_UMLModelElement)



@given(instance=simpleuml_UMLModelElement_strategy)
def test_simpleuml_umlmodelelement_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original



@given(instance=simpleuml_UMLModelElement_strategy)
def test_simpleuml_umlmodelelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=UMLModelElement_strategy)
@settings(max_examples=50)
def test_umlmodelelement_instantiation(instance):
    assert isinstance(instance, UMLModelElement)

@given(instance=simpleuml_Package_strategy)
@settings(max_examples=50)
def test_simpleuml_package_instantiation(instance):
    assert isinstance(instance, simpleuml_Package)

@given(instance=simpleuml_PackageElement_strategy)
@settings(max_examples=50)
def test_simpleuml_packageelement_instantiation(instance):
    assert isinstance(instance, simpleuml_PackageElement)

@given(instance=simpleuml_Attribute_strategy)
@settings(max_examples=50)
def test_simpleuml_attribute_instantiation(instance):
    assert isinstance(instance, simpleuml_Attribute)

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=simpleuml_PrimitiveDataType_strategy)
@settings(max_examples=50)
def test_simpleuml_primitivedatatype_instantiation(instance):
    assert isinstance(instance, simpleuml_PrimitiveDataType)

@given(instance=PackageElement_strategy)
@settings(max_examples=50)
def test_packageelement_instantiation(instance):
    assert isinstance(instance, PackageElement)

@given(instance=simpleuml_Association_strategy)
@settings(max_examples=50)
def test_simpleuml_association_instantiation(instance):
    assert isinstance(instance, simpleuml_Association)

@given(instance=simpleuml_Class_strategy)
@settings(max_examples=50)
def test_simpleuml_class_instantiation(instance):
    assert isinstance(instance, simpleuml_Class)

@given(instance=simpleuml_Classifier_strategy)
@settings(max_examples=50)
def test_simpleuml_classifier_instantiation(instance):
    assert isinstance(instance, simpleuml_Classifier)
