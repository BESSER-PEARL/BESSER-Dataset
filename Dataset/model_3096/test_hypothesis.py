import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    SimpleClass_Association,
    Attribute,
    Class,
    Classifier,
    SimpleClass_PrimitiveDataType,
    SimpleClass_Class,
    SimpleClass_Attribute,
    SimpleClass_Classifier,
    Entity,
    EA,
    Vocabulary,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_simpleclass_association_is_not_abstract():
    assert not inspect.isabstract(SimpleClass_Association)


def test_simpleclass_association_constructor_exists():
    assert callable(SimpleClass_Association.__init__)


def test_simpleclass_association_constructor_args():
    sig = inspect.signature(SimpleClass_Association.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simpleclass_association_has_name():
    assert hasattr(SimpleClass_Association, "name")
    descriptor = None
    for klass in SimpleClass_Association.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



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



def test_simpleclass_primitivedatatype_is_not_abstract():
    assert not inspect.isabstract(SimpleClass_PrimitiveDataType)


def test_simpleclass_primitivedatatype_constructor_exists():
    assert callable(SimpleClass_PrimitiveDataType.__init__)


def test_simpleclass_primitivedatatype_constructor_args():
    sig = inspect.signature(SimpleClass_PrimitiveDataType.__init__)
    params = list(sig.parameters.keys())



def test_simpleclass_class_is_not_abstract():
    assert not inspect.isabstract(SimpleClass_Class)


def test_simpleclass_class_constructor_exists():
    assert callable(SimpleClass_Class.__init__)


def test_simpleclass_class_constructor_args():
    sig = inspect.signature(SimpleClass_Class.__init__)
    params = list(sig.parameters.keys())
    assert "tipo" in params, "Missing parameter 'tipo'"
    assert "is_persistent" in params, "Missing parameter 'is_persistent'"

def test_simpleclass_class_has_tipo():
    assert hasattr(SimpleClass_Class, "tipo")
    descriptor = None
    for klass in SimpleClass_Class.__mro__:
        if "tipo" in klass.__dict__:
            descriptor = klass.__dict__["tipo"]
            break
    assert isinstance(descriptor, property)

def test_simpleclass_class_has_is_persistent():
    assert hasattr(SimpleClass_Class, "is_persistent")
    descriptor = None
    for klass in SimpleClass_Class.__mro__:
        if "is_persistent" in klass.__dict__:
            descriptor = klass.__dict__["is_persistent"]
            break
    assert isinstance(descriptor, property)



def test_simpleclass_attribute_is_not_abstract():
    assert not inspect.isabstract(SimpleClass_Attribute)


def test_simpleclass_attribute_constructor_exists():
    assert callable(SimpleClass_Attribute.__init__)


def test_simpleclass_attribute_constructor_args():
    sig = inspect.signature(SimpleClass_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "is_primary" in params, "Missing parameter 'is_primary'"
    assert "name" in params, "Missing parameter 'name'"

def test_simpleclass_attribute_has_is_primary():
    assert hasattr(SimpleClass_Attribute, "is_primary")
    descriptor = None
    for klass in SimpleClass_Attribute.__mro__:
        if "is_primary" in klass.__dict__:
            descriptor = klass.__dict__["is_primary"]
            break
    assert isinstance(descriptor, property)

def test_simpleclass_attribute_has_name():
    assert hasattr(SimpleClass_Attribute, "name")
    descriptor = None
    for klass in SimpleClass_Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simpleclass_classifier_is_not_abstract():
    assert not inspect.isabstract(SimpleClass_Classifier)


def test_simpleclass_classifier_constructor_exists():
    assert callable(SimpleClass_Classifier.__init__)


def test_simpleclass_classifier_constructor_args():
    sig = inspect.signature(SimpleClass_Classifier.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simpleclass_classifier_has_name():
    assert hasattr(SimpleClass_Classifier, "name")
    descriptor = None
    for klass in SimpleClass_Classifier.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

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

def test_ea_exists():
    # Check that the Enumeration exists
    assert EA is not None

def test_ea_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EA]
    expected_literals = [
        "Institution",
        "Author",
        "Journal",
        "Normal",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EA"

def test_vocabulary_exists():
    # Check that the Enumeration exists
    assert Vocabulary is not None

def test_vocabulary_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Vocabulary]
    expected_literals = [
        "Eurovocs",
        "Language",
        "Normal",
        "Decs",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Vocabulary"


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
SimpleClass_Association_strategy = st.builds(
    SimpleClass_Association,
    name=
        safe_text
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
SimpleClass_PrimitiveDataType_strategy = st.builds(
    SimpleClass_PrimitiveDataType,
)
SimpleClass_Class_strategy = st.builds(
    SimpleClass_Class,
    tipo=
        safe_text,
    is_persistent=
        safe_text
)
SimpleClass_Attribute_strategy = st.builds(
    SimpleClass_Attribute,
    is_primary=
        safe_text,
    name=
        safe_text
)
SimpleClass_Classifier_strategy = st.builds(
    SimpleClass_Classifier,
    name=
        safe_text
)

@given(instance=SimpleClass_Association_strategy)
@settings(max_examples=50)
def test_simpleclass_association_instantiation(instance):
    assert isinstance(instance, SimpleClass_Association)



@given(instance=SimpleClass_Association_strategy)
def test_simpleclass_association_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

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

@given(instance=SimpleClass_PrimitiveDataType_strategy)
@settings(max_examples=50)
def test_simpleclass_primitivedatatype_instantiation(instance):
    assert isinstance(instance, SimpleClass_PrimitiveDataType)

@given(instance=SimpleClass_Class_strategy)
@settings(max_examples=50)
def test_simpleclass_class_instantiation(instance):
    assert isinstance(instance, SimpleClass_Class)



@given(instance=SimpleClass_Class_strategy)
def test_simpleclass_class_tipo_setter(instance):
    original = instance.tipo
    instance.tipo = original
    assert instance.tipo == original



@given(instance=SimpleClass_Class_strategy)
def test_simpleclass_class_is_persistent_setter(instance):
    original = instance.is_persistent
    instance.is_persistent = original
    assert instance.is_persistent == original

@given(instance=SimpleClass_Attribute_strategy)
@settings(max_examples=50)
def test_simpleclass_attribute_instantiation(instance):
    assert isinstance(instance, SimpleClass_Attribute)



@given(instance=SimpleClass_Attribute_strategy)
def test_simpleclass_attribute_is_primary_setter(instance):
    original = instance.is_primary
    instance.is_primary = original
    assert instance.is_primary == original



@given(instance=SimpleClass_Attribute_strategy)
def test_simpleclass_attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SimpleClass_Classifier_strategy)
@settings(max_examples=50)
def test_simpleclass_classifier_instantiation(instance):
    assert isinstance(instance, SimpleClass_Classifier)



@given(instance=SimpleClass_Classifier_strategy)
def test_simpleclass_classifier_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
