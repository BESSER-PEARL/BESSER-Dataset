import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    simpleuml_UMLPackage,
    ModelElement,
    simpleuml_Classifier,
    simpleuml_Association,
    simpleuml_ModelElement,
    simpleuml_Attribute,
    Classifier,
    simpleuml_PrimitiveDataType,
    simpleuml_UMLClass,
    Ignore,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_simpleuml_umlpackage_is_not_abstract():
    assert not inspect.isabstract(simpleuml_UMLPackage)


def test_simpleuml_umlpackage_constructor_exists():
    assert callable(simpleuml_UMLPackage.__init__)


def test_simpleuml_umlpackage_constructor_args():
    sig = inspect.signature(simpleuml_UMLPackage.__init__)
    params = list(sig.parameters.keys())



def test_modelelement_is_not_abstract():
    assert not inspect.isabstract(ModelElement)


def test_modelelement_constructor_exists():
    assert callable(ModelElement.__init__)


def test_modelelement_constructor_args():
    sig = inspect.signature(ModelElement.__init__)
    params = list(sig.parameters.keys())



def test_simpleuml_classifier_is_not_abstract():
    assert not inspect.isabstract(simpleuml_Classifier)


def test_simpleuml_classifier_constructor_exists():
    assert callable(simpleuml_Classifier.__init__)


def test_simpleuml_classifier_constructor_args():
    sig = inspect.signature(simpleuml_Classifier.__init__)
    params = list(sig.parameters.keys())



def test_simpleuml_association_is_not_abstract():
    assert not inspect.isabstract(simpleuml_Association)


def test_simpleuml_association_constructor_exists():
    assert callable(simpleuml_Association.__init__)


def test_simpleuml_association_constructor_args():
    sig = inspect.signature(simpleuml_Association.__init__)
    params = list(sig.parameters.keys())



def test_simpleuml_modelelement_is_not_abstract():
    assert not inspect.isabstract(simpleuml_ModelElement)


def test_simpleuml_modelelement_constructor_exists():
    assert callable(simpleuml_ModelElement.__init__)


def test_simpleuml_modelelement_constructor_args():
    sig = inspect.signature(simpleuml_ModelElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simpleuml_modelelement_has_name():
    assert hasattr(simpleuml_ModelElement, "name")
    descriptor = None
    for klass in simpleuml_ModelElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



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



def test_simpleuml_umlclass_is_not_abstract():
    assert not inspect.isabstract(simpleuml_UMLClass)


def test_simpleuml_umlclass_constructor_exists():
    assert callable(simpleuml_UMLClass.__init__)


def test_simpleuml_umlclass_constructor_args():
    sig = inspect.signature(simpleuml_UMLClass.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_simpleuml_umlclass_has_kind():
    assert hasattr(simpleuml_UMLClass, "kind")
    descriptor = None
    for klass in simpleuml_UMLClass.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)

def test_ignore_exists():
    # Check that the Enumeration exists
    assert Ignore is not None

def test_ignore_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Ignore]
    expected_literals = [
        "lit1",
        "anotherlit",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Ignore"


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
simpleuml_UMLPackage_strategy = st.builds(
    simpleuml_UMLPackage,
)
ModelElement_strategy = st.builds(
    ModelElement,
)
simpleuml_Classifier_strategy = st.builds(
    simpleuml_Classifier,
)
simpleuml_Association_strategy = st.builds(
    simpleuml_Association,
)
simpleuml_ModelElement_strategy = st.builds(
    simpleuml_ModelElement,
    name=
        safe_text
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
simpleuml_UMLClass_strategy = st.builds(
    simpleuml_UMLClass,
    kind=
        safe_text
)

@given(instance=simpleuml_UMLPackage_strategy)
@settings(max_examples=50)
def test_simpleuml_umlpackage_instantiation(instance):
    assert isinstance(instance, simpleuml_UMLPackage)

@given(instance=ModelElement_strategy)
@settings(max_examples=50)
def test_modelelement_instantiation(instance):
    assert isinstance(instance, ModelElement)

@given(instance=simpleuml_Classifier_strategy)
@settings(max_examples=50)
def test_simpleuml_classifier_instantiation(instance):
    assert isinstance(instance, simpleuml_Classifier)

@given(instance=simpleuml_Association_strategy)
@settings(max_examples=50)
def test_simpleuml_association_instantiation(instance):
    assert isinstance(instance, simpleuml_Association)

@given(instance=simpleuml_ModelElement_strategy)
@settings(max_examples=50)
def test_simpleuml_modelelement_instantiation(instance):
    assert isinstance(instance, simpleuml_ModelElement)



@given(instance=simpleuml_ModelElement_strategy)
def test_simpleuml_modelelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

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

@given(instance=simpleuml_UMLClass_strategy)
@settings(max_examples=50)
def test_simpleuml_umlclass_instantiation(instance):
    assert isinstance(instance, simpleuml_UMLClass)



@given(instance=simpleuml_UMLClass_strategy)
def test_simpleuml_umlclass_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original
