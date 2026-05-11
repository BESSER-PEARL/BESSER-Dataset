import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    simpleuml::UMLPackage,
    ModelElement,
    simpleuml::Classifier,
    simpleuml::Association,
    simpleuml::ModelElement,
    simpleuml::Attribute,
    Classifier,
    simpleuml::PrimitiveDataType,
    simpleuml::UMLClass,
    Ignore,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_simpleuml::umlpackage_is_not_abstract():
    assert not inspect.isabstract(simpleuml::UMLPackage)


def test_simpleuml::umlpackage_constructor_exists():
    assert callable(simpleuml::UMLPackage.__init__)


def test_simpleuml::umlpackage_constructor_args():
    sig = inspect.signature(simpleuml::UMLPackage.__init__)
    params = list(sig.parameters.keys())



def test_modelelement_is_not_abstract():
    assert not inspect.isabstract(ModelElement)


def test_modelelement_constructor_exists():
    assert callable(ModelElement.__init__)


def test_modelelement_constructor_args():
    sig = inspect.signature(ModelElement.__init__)
    params = list(sig.parameters.keys())



def test_simpleuml::classifier_is_not_abstract():
    assert not inspect.isabstract(simpleuml::Classifier)


def test_simpleuml::classifier_constructor_exists():
    assert callable(simpleuml::Classifier.__init__)


def test_simpleuml::classifier_constructor_args():
    sig = inspect.signature(simpleuml::Classifier.__init__)
    params = list(sig.parameters.keys())



def test_simpleuml::association_is_not_abstract():
    assert not inspect.isabstract(simpleuml::Association)


def test_simpleuml::association_constructor_exists():
    assert callable(simpleuml::Association.__init__)


def test_simpleuml::association_constructor_args():
    sig = inspect.signature(simpleuml::Association.__init__)
    params = list(sig.parameters.keys())



def test_simpleuml::modelelement_is_not_abstract():
    assert not inspect.isabstract(simpleuml::ModelElement)


def test_simpleuml::modelelement_constructor_exists():
    assert callable(simpleuml::ModelElement.__init__)


def test_simpleuml::modelelement_constructor_args():
    sig = inspect.signature(simpleuml::ModelElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simpleuml::modelelement_has_name():
    assert hasattr(simpleuml::ModelElement, "name")
    descriptor = None
    for klass in simpleuml::ModelElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simpleuml::attribute_is_not_abstract():
    assert not inspect.isabstract(simpleuml::Attribute)


def test_simpleuml::attribute_constructor_exists():
    assert callable(simpleuml::Attribute.__init__)


def test_simpleuml::attribute_constructor_args():
    sig = inspect.signature(simpleuml::Attribute.__init__)
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



def test_simpleuml::umlclass_is_not_abstract():
    assert not inspect.isabstract(simpleuml::UMLClass)


def test_simpleuml::umlclass_constructor_exists():
    assert callable(simpleuml::UMLClass.__init__)


def test_simpleuml::umlclass_constructor_args():
    sig = inspect.signature(simpleuml::UMLClass.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_simpleuml::umlclass_has_kind():
    assert hasattr(simpleuml::UMLClass, "kind")
    descriptor = None
    for klass in simpleuml::UMLClass.__mro__:
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
        "anotherlit",
        "lit1",
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
simpleuml::UMLPackage_strategy = st.builds(
    simpleuml::UMLPackage,
)
ModelElement_strategy = st.builds(
    ModelElement,
)
simpleuml::Classifier_strategy = st.builds(
    simpleuml::Classifier,
)
simpleuml::Association_strategy = st.builds(
    simpleuml::Association,
)
simpleuml::ModelElement_strategy = st.builds(
    simpleuml::ModelElement,
    name=
        safe_text
)
simpleuml::Attribute_strategy = st.builds(
    simpleuml::Attribute,
)
Classifier_strategy = st.builds(
    Classifier,
)
simpleuml::PrimitiveDataType_strategy = st.builds(
    simpleuml::PrimitiveDataType,
)
simpleuml::UMLClass_strategy = st.builds(
    simpleuml::UMLClass,
    kind=
        safe_text
)

@given(instance=simpleuml::UMLPackage_strategy)
@settings(max_examples=50)
def test_simpleuml::umlpackage_instantiation(instance):
    assert isinstance(instance, simpleuml::UMLPackage)

@given(instance=ModelElement_strategy)
@settings(max_examples=50)
def test_modelelement_instantiation(instance):
    assert isinstance(instance, ModelElement)

@given(instance=simpleuml::Classifier_strategy)
@settings(max_examples=50)
def test_simpleuml::classifier_instantiation(instance):
    assert isinstance(instance, simpleuml::Classifier)

@given(instance=simpleuml::Association_strategy)
@settings(max_examples=50)
def test_simpleuml::association_instantiation(instance):
    assert isinstance(instance, simpleuml::Association)

@given(instance=simpleuml::ModelElement_strategy)
@settings(max_examples=50)
def test_simpleuml::modelelement_instantiation(instance):
    assert isinstance(instance, simpleuml::ModelElement)

@given(instance=simpleuml::ModelElement_strategy)
def test_simpleuml::modelelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=simpleuml::ModelElement_strategy)
def test_simpleuml::modelelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simpleuml::Attribute_strategy)
@settings(max_examples=50)
def test_simpleuml::attribute_instantiation(instance):
    assert isinstance(instance, simpleuml::Attribute)

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=simpleuml::PrimitiveDataType_strategy)
@settings(max_examples=50)
def test_simpleuml::primitivedatatype_instantiation(instance):
    assert isinstance(instance, simpleuml::PrimitiveDataType)

@given(instance=simpleuml::UMLClass_strategy)
@settings(max_examples=50)
def test_simpleuml::umlclass_instantiation(instance):
    assert isinstance(instance, simpleuml::UMLClass)

@given(instance=simpleuml::UMLClass_strategy)
def test_simpleuml::umlclass_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=simpleuml::UMLClass_strategy)
def test_simpleuml::umlclass_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original
