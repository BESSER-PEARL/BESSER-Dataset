import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    tallerE1Java_Program,
    Class,
    tallerE1Java_DAOClass,
    tallerE1Java_TestClass,
    tallerE1Java_EntityClass,
    tallerE1Java_Annotation,
    tallerE1Java_Type,
    tallerE1Java_Attribute,
    Type,
    tallerE1Java_Class,
    tallerE1Java_Container,
    tallerE1Java_PrimitiveType,
    tallerE1Java_Package,
    Visibility,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_tallere1java_program_is_not_abstract():
    assert not inspect.isabstract(tallerE1Java_Program)


def test_tallere1java_program_constructor_exists():
    assert callable(tallerE1Java_Program.__init__)


def test_tallere1java_program_constructor_args():
    sig = inspect.signature(tallerE1Java_Program.__init__)
    params = list(sig.parameters.keys())



def test_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_class_constructor_exists():
    assert callable(Class.__init__)


def test_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_tallere1java_daoclass_is_not_abstract():
    assert not inspect.isabstract(tallerE1Java_DAOClass)


def test_tallere1java_daoclass_constructor_exists():
    assert callable(tallerE1Java_DAOClass.__init__)


def test_tallere1java_daoclass_constructor_args():
    sig = inspect.signature(tallerE1Java_DAOClass.__init__)
    params = list(sig.parameters.keys())



def test_tallere1java_testclass_is_not_abstract():
    assert not inspect.isabstract(tallerE1Java_TestClass)


def test_tallere1java_testclass_constructor_exists():
    assert callable(tallerE1Java_TestClass.__init__)


def test_tallere1java_testclass_constructor_args():
    sig = inspect.signature(tallerE1Java_TestClass.__init__)
    params = list(sig.parameters.keys())



def test_tallere1java_entityclass_is_not_abstract():
    assert not inspect.isabstract(tallerE1Java_EntityClass)


def test_tallere1java_entityclass_constructor_exists():
    assert callable(tallerE1Java_EntityClass.__init__)


def test_tallere1java_entityclass_constructor_args():
    sig = inspect.signature(tallerE1Java_EntityClass.__init__)
    params = list(sig.parameters.keys())



def test_tallere1java_annotation_is_not_abstract():
    assert not inspect.isabstract(tallerE1Java_Annotation)


def test_tallere1java_annotation_constructor_exists():
    assert callable(tallerE1Java_Annotation.__init__)


def test_tallere1java_annotation_constructor_args():
    sig = inspect.signature(tallerE1Java_Annotation.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "content" in params, "Missing parameter 'content'"

def test_tallere1java_annotation_has_type():
    assert hasattr(tallerE1Java_Annotation, "type")
    descriptor = None
    for klass in tallerE1Java_Annotation.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_tallere1java_annotation_has_content():
    assert hasattr(tallerE1Java_Annotation, "content")
    descriptor = None
    for klass in tallerE1Java_Annotation.__mro__:
        if "content" in klass.__dict__:
            descriptor = klass.__dict__["content"]
            break
    assert isinstance(descriptor, property)



def test_tallere1java_type_is_not_abstract():
    assert not inspect.isabstract(tallerE1Java_Type)


def test_tallere1java_type_constructor_exists():
    assert callable(tallerE1Java_Type.__init__)


def test_tallere1java_type_constructor_args():
    sig = inspect.signature(tallerE1Java_Type.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_tallere1java_type_has_name():
    assert hasattr(tallerE1Java_Type, "name")
    descriptor = None
    for klass in tallerE1Java_Type.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_tallere1java_attribute_is_not_abstract():
    assert not inspect.isabstract(tallerE1Java_Attribute)


def test_tallere1java_attribute_constructor_exists():
    assert callable(tallerE1Java_Attribute.__init__)


def test_tallere1java_attribute_constructor_args():
    sig = inspect.signature(tallerE1Java_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "visibility" in params, "Missing parameter 'visibility'"

def test_tallere1java_attribute_has_name():
    assert hasattr(tallerE1Java_Attribute, "name")
    descriptor = None
    for klass in tallerE1Java_Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_tallere1java_attribute_has_visibility():
    assert hasattr(tallerE1Java_Attribute, "visibility")
    descriptor = None
    for klass in tallerE1Java_Attribute.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_tallere1java_class_is_not_abstract():
    assert not inspect.isabstract(tallerE1Java_Class)


def test_tallere1java_class_constructor_exists():
    assert callable(tallerE1Java_Class.__init__)


def test_tallere1java_class_constructor_args():
    sig = inspect.signature(tallerE1Java_Class.__init__)
    params = list(sig.parameters.keys())



def test_tallere1java_container_is_not_abstract():
    assert not inspect.isabstract(tallerE1Java_Container)


def test_tallere1java_container_constructor_exists():
    assert callable(tallerE1Java_Container.__init__)


def test_tallere1java_container_constructor_args():
    sig = inspect.signature(tallerE1Java_Container.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_tallere1java_container_has_type():
    assert hasattr(tallerE1Java_Container, "type")
    descriptor = None
    for klass in tallerE1Java_Container.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_tallere1java_primitivetype_is_not_abstract():
    assert not inspect.isabstract(tallerE1Java_PrimitiveType)


def test_tallere1java_primitivetype_constructor_exists():
    assert callable(tallerE1Java_PrimitiveType.__init__)


def test_tallere1java_primitivetype_constructor_args():
    sig = inspect.signature(tallerE1Java_PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_tallere1java_package_is_not_abstract():
    assert not inspect.isabstract(tallerE1Java_Package)


def test_tallere1java_package_constructor_exists():
    assert callable(tallerE1Java_Package.__init__)


def test_tallere1java_package_constructor_args():
    sig = inspect.signature(tallerE1Java_Package.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_tallere1java_package_has_name():
    assert hasattr(tallerE1Java_Package, "name")
    descriptor = None
    for klass in tallerE1Java_Package.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_visibility_exists():
    # Check that the Enumeration exists
    assert Visibility is not None

def test_visibility_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Visibility]
    expected_literals = [
        "public",
        "private",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Visibility"


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
tallerE1Java_Program_strategy = st.builds(
    tallerE1Java_Program,
)
Class_strategy = st.builds(
    Class,
)
tallerE1Java_DAOClass_strategy = st.builds(
    tallerE1Java_DAOClass,
)
tallerE1Java_TestClass_strategy = st.builds(
    tallerE1Java_TestClass,
)
tallerE1Java_EntityClass_strategy = st.builds(
    tallerE1Java_EntityClass,
)
tallerE1Java_Annotation_strategy = st.builds(
    tallerE1Java_Annotation,
    type=
        safe_text,
    content=
        safe_text
)
tallerE1Java_Type_strategy = st.builds(
    tallerE1Java_Type,
    name=
        safe_text
)
tallerE1Java_Attribute_strategy = st.builds(
    tallerE1Java_Attribute,
    name=
        safe_text,
    visibility=
        safe_text
)
Type_strategy = st.builds(
    Type,
)
tallerE1Java_Class_strategy = st.builds(
    tallerE1Java_Class,
)
tallerE1Java_Container_strategy = st.builds(
    tallerE1Java_Container,
    type=
        safe_text
)
tallerE1Java_PrimitiveType_strategy = st.builds(
    tallerE1Java_PrimitiveType,
)
tallerE1Java_Package_strategy = st.builds(
    tallerE1Java_Package,
    name=
        safe_text
)

@given(instance=tallerE1Java_Program_strategy)
@settings(max_examples=50)
def test_tallere1java_program_instantiation(instance):
    assert isinstance(instance, tallerE1Java_Program)

@given(instance=Class_strategy)
@settings(max_examples=50)
def test_class_instantiation(instance):
    assert isinstance(instance, Class)

@given(instance=tallerE1Java_DAOClass_strategy)
@settings(max_examples=50)
def test_tallere1java_daoclass_instantiation(instance):
    assert isinstance(instance, tallerE1Java_DAOClass)

@given(instance=tallerE1Java_TestClass_strategy)
@settings(max_examples=50)
def test_tallere1java_testclass_instantiation(instance):
    assert isinstance(instance, tallerE1Java_TestClass)

@given(instance=tallerE1Java_EntityClass_strategy)
@settings(max_examples=50)
def test_tallere1java_entityclass_instantiation(instance):
    assert isinstance(instance, tallerE1Java_EntityClass)

@given(instance=tallerE1Java_Annotation_strategy)
@settings(max_examples=50)
def test_tallere1java_annotation_instantiation(instance):
    assert isinstance(instance, tallerE1Java_Annotation)



@given(instance=tallerE1Java_Annotation_strategy)
def test_tallere1java_annotation_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=tallerE1Java_Annotation_strategy)
def test_tallere1java_annotation_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original

@given(instance=tallerE1Java_Type_strategy)
@settings(max_examples=50)
def test_tallere1java_type_instantiation(instance):
    assert isinstance(instance, tallerE1Java_Type)



@given(instance=tallerE1Java_Type_strategy)
def test_tallere1java_type_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=tallerE1Java_Attribute_strategy)
@settings(max_examples=50)
def test_tallere1java_attribute_instantiation(instance):
    assert isinstance(instance, tallerE1Java_Attribute)



@given(instance=tallerE1Java_Attribute_strategy)
def test_tallere1java_attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=tallerE1Java_Attribute_strategy)
def test_tallere1java_attribute_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=tallerE1Java_Class_strategy)
@settings(max_examples=50)
def test_tallere1java_class_instantiation(instance):
    assert isinstance(instance, tallerE1Java_Class)

@given(instance=tallerE1Java_Container_strategy)
@settings(max_examples=50)
def test_tallere1java_container_instantiation(instance):
    assert isinstance(instance, tallerE1Java_Container)



@given(instance=tallerE1Java_Container_strategy)
def test_tallere1java_container_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=tallerE1Java_PrimitiveType_strategy)
@settings(max_examples=50)
def test_tallere1java_primitivetype_instantiation(instance):
    assert isinstance(instance, tallerE1Java_PrimitiveType)

@given(instance=tallerE1Java_Package_strategy)
@settings(max_examples=50)
def test_tallere1java_package_instantiation(instance):
    assert isinstance(instance, tallerE1Java_Package)



@given(instance=tallerE1Java_Package_strategy)
def test_tallere1java_package_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
