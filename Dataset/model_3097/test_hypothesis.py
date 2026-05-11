import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    PrimitiveDataType,
    Association,
    Attribute,
    Class,
    Classifier,
    SimpleClass::PrimitiveDataType,
    SimpleClass::Schema,
    SimpleClass::Class,
    SimpleClass::Classifier,
    SimpleClass::Attribute,
    SimpleClass::Association,
    Vocabulary,
    EA,
    Entity,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_primitivedatatype_is_not_abstract():
    assert not inspect.isabstract(PrimitiveDataType)


def test_primitivedatatype_constructor_exists():
    assert callable(PrimitiveDataType.__init__)


def test_primitivedatatype_constructor_args():
    sig = inspect.signature(PrimitiveDataType.__init__)
    params = list(sig.parameters.keys())



def test_association_is_not_abstract():
    assert not inspect.isabstract(Association)


def test_association_constructor_exists():
    assert callable(Association.__init__)


def test_association_constructor_args():
    sig = inspect.signature(Association.__init__)
    params = list(sig.parameters.keys())



def test_attribute_is_not_abstract():
    assert not inspect.isabstract(Attribute)


def test_attribute_constructor_exists():
    assert callable(Attribute.__init__)


def test_attribute_constructor_args():
    sig = inspect.signature(Attribute.__init__)
    params = list(sig.parameters.keys())



def test_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_class_constructor_exists():
    assert callable(Class.__init__)


def test_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_classifier_is_not_abstract():
    assert not inspect.isabstract(Classifier)


def test_classifier_constructor_exists():
    assert callable(Classifier.__init__)


def test_classifier_constructor_args():
    sig = inspect.signature(Classifier.__init__)
    params = list(sig.parameters.keys())



def test_simpleclass::primitivedatatype_is_not_abstract():
    assert not inspect.isabstract(SimpleClass::PrimitiveDataType)


def test_simpleclass::primitivedatatype_constructor_exists():
    assert callable(SimpleClass::PrimitiveDataType.__init__)


def test_simpleclass::primitivedatatype_constructor_args():
    sig = inspect.signature(SimpleClass::PrimitiveDataType.__init__)
    params = list(sig.parameters.keys())



def test_simpleclass::schema_is_not_abstract():
    assert not inspect.isabstract(SimpleClass::Schema)


def test_simpleclass::schema_constructor_exists():
    assert callable(SimpleClass::Schema.__init__)


def test_simpleclass::schema_constructor_args():
    sig = inspect.signature(SimpleClass::Schema.__init__)
    params = list(sig.parameters.keys())



def test_simpleclass::class_is_not_abstract():
    assert not inspect.isabstract(SimpleClass::Class)


def test_simpleclass::class_constructor_exists():
    assert callable(SimpleClass::Class.__init__)


def test_simpleclass::class_constructor_args():
    sig = inspect.signature(SimpleClass::Class.__init__)
    params = list(sig.parameters.keys())
    assert "is_persistent" in params, "Missing parameter 'is_persistent'"

def test_simpleclass::class_has_is_persistent():
    assert hasattr(SimpleClass::Class, "is_persistent")
    descriptor = None
    for klass in SimpleClass::Class.__mro__:
        if "is_persistent" in klass.__dict__:
            descriptor = klass.__dict__["is_persistent"]
            break
    assert isinstance(descriptor, property)



def test_simpleclass::classifier_is_not_abstract():
    assert not inspect.isabstract(SimpleClass::Classifier)


def test_simpleclass::classifier_constructor_exists():
    assert callable(SimpleClass::Classifier.__init__)


def test_simpleclass::classifier_constructor_args():
    sig = inspect.signature(SimpleClass::Classifier.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simpleclass::classifier_has_name():
    assert hasattr(SimpleClass::Classifier, "name")
    descriptor = None
    for klass in SimpleClass::Classifier.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simpleclass::attribute_is_not_abstract():
    assert not inspect.isabstract(SimpleClass::Attribute)


def test_simpleclass::attribute_constructor_exists():
    assert callable(SimpleClass::Attribute.__init__)


def test_simpleclass::attribute_constructor_args():
    sig = inspect.signature(SimpleClass::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "is_primary" in params, "Missing parameter 'is_primary'"

def test_simpleclass::attribute_has_name():
    assert hasattr(SimpleClass::Attribute, "name")
    descriptor = None
    for klass in SimpleClass::Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_simpleclass::attribute_has_is_primary():
    assert hasattr(SimpleClass::Attribute, "is_primary")
    descriptor = None
    for klass in SimpleClass::Attribute.__mro__:
        if "is_primary" in klass.__dict__:
            descriptor = klass.__dict__["is_primary"]
            break
    assert isinstance(descriptor, property)



def test_simpleclass::association_is_not_abstract():
    assert not inspect.isabstract(SimpleClass::Association)


def test_simpleclass::association_constructor_exists():
    assert callable(SimpleClass::Association.__init__)


def test_simpleclass::association_constructor_args():
    sig = inspect.signature(SimpleClass::Association.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simpleclass::association_has_name():
    assert hasattr(SimpleClass::Association, "name")
    descriptor = None
    for klass in SimpleClass::Association.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_vocabulary_exists():
    # Check that the Enumeration exists
    assert Vocabulary is not None

def test_vocabulary_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Vocabulary]
    expected_literals = [
        "Language",
        "Eurovocs",
        "Normal",
        "Decs",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Vocabulary"

def test_ea_exists():
    # Check that the Enumeration exists
    assert EA is not None

def test_ea_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EA]
    expected_literals = [
        "Author",
        "Institution",
        "Journal",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EA"

def test_entity_exists():
    # Check that the Enumeration exists
    assert Entity is not None

def test_entity_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Entity]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Entity"


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
PrimitiveDataType_strategy = st.builds(
    PrimitiveDataType,
)
Association_strategy = st.builds(
    Association,
)
Attribute_strategy = st.builds(
    Attribute,
)
Class_strategy = st.builds(
    Class,
)
Classifier_strategy = st.builds(
    Classifier,
)
SimpleClass::PrimitiveDataType_strategy = st.builds(
    SimpleClass::PrimitiveDataType,
)
SimpleClass::Schema_strategy = st.builds(
    SimpleClass::Schema,
)
SimpleClass::Class_strategy = st.builds(
    SimpleClass::Class,
    is_persistent=
        safe_text
)
SimpleClass::Classifier_strategy = st.builds(
    SimpleClass::Classifier,
    name=
        safe_text
)
SimpleClass::Attribute_strategy = st.builds(
    SimpleClass::Attribute,
    name=
        safe_text,
    is_primary=
        safe_text
)
SimpleClass::Association_strategy = st.builds(
    SimpleClass::Association,
    name=
        safe_text
)

@given(instance=PrimitiveDataType_strategy)
@settings(max_examples=50)
def test_primitivedatatype_instantiation(instance):
    assert isinstance(instance, PrimitiveDataType)

@given(instance=Association_strategy)
@settings(max_examples=50)
def test_association_instantiation(instance):
    assert isinstance(instance, Association)

@given(instance=Attribute_strategy)
@settings(max_examples=50)
def test_attribute_instantiation(instance):
    assert isinstance(instance, Attribute)

@given(instance=Class_strategy)
@settings(max_examples=50)
def test_class_instantiation(instance):
    assert isinstance(instance, Class)

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=SimpleClass::PrimitiveDataType_strategy)
@settings(max_examples=50)
def test_simpleclass::primitivedatatype_instantiation(instance):
    assert isinstance(instance, SimpleClass::PrimitiveDataType)

@given(instance=SimpleClass::Schema_strategy)
@settings(max_examples=50)
def test_simpleclass::schema_instantiation(instance):
    assert isinstance(instance, SimpleClass::Schema)

@given(instance=SimpleClass::Class_strategy)
@settings(max_examples=50)
def test_simpleclass::class_instantiation(instance):
    assert isinstance(instance, SimpleClass::Class)

@given(instance=SimpleClass::Class_strategy)
def test_simpleclass::class_is_persistent_type(instance):
    assert isinstance(instance.is_persistent, str)


@given(instance=SimpleClass::Class_strategy)
def test_simpleclass::class_is_persistent_setter(instance):
    original = instance.is_persistent
    instance.is_persistent = original
    assert instance.is_persistent == original

@given(instance=SimpleClass::Classifier_strategy)
@settings(max_examples=50)
def test_simpleclass::classifier_instantiation(instance):
    assert isinstance(instance, SimpleClass::Classifier)

@given(instance=SimpleClass::Classifier_strategy)
def test_simpleclass::classifier_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=SimpleClass::Classifier_strategy)
def test_simpleclass::classifier_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SimpleClass::Attribute_strategy)
@settings(max_examples=50)
def test_simpleclass::attribute_instantiation(instance):
    assert isinstance(instance, SimpleClass::Attribute)

@given(instance=SimpleClass::Attribute_strategy)
def test_simpleclass::attribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=SimpleClass::Attribute_strategy)
def test_simpleclass::attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SimpleClass::Attribute_strategy)
def test_simpleclass::attribute_is_primary_type(instance):
    assert isinstance(instance.is_primary, str)


@given(instance=SimpleClass::Attribute_strategy)
def test_simpleclass::attribute_is_primary_setter(instance):
    original = instance.is_primary
    instance.is_primary = original
    assert instance.is_primary == original

@given(instance=SimpleClass::Association_strategy)
@settings(max_examples=50)
def test_simpleclass::association_instantiation(instance):
    assert isinstance(instance, SimpleClass::Association)

@given(instance=SimpleClass::Association_strategy)
def test_simpleclass::association_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=SimpleClass::Association_strategy)
def test_simpleclass::association_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
