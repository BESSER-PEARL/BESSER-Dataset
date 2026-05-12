import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Class,
    JavaMM_DAOClass,
    JavaMM_TestClass,
    JavaMM_EntityClass,
    JavaMM_Annotation,
    Type,
    JavaMM_Class,
    JavaMM_Container,
    JavaMM_PrimitiveType,
    JavaMM_Package,
    JavaMM_Program,
    JavaMM_Type,
    JavaMM_Attribute,
    Visibility,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_class_constructor_exists():
    assert callable(Class.__init__)


def test_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_javamm_daoclass_is_not_abstract():
    assert not inspect.isabstract(JavaMM_DAOClass)


def test_javamm_daoclass_constructor_exists():
    assert callable(JavaMM_DAOClass.__init__)


def test_javamm_daoclass_constructor_args():
    sig = inspect.signature(JavaMM_DAOClass.__init__)
    params = list(sig.parameters.keys())



def test_javamm_testclass_is_not_abstract():
    assert not inspect.isabstract(JavaMM_TestClass)


def test_javamm_testclass_constructor_exists():
    assert callable(JavaMM_TestClass.__init__)


def test_javamm_testclass_constructor_args():
    sig = inspect.signature(JavaMM_TestClass.__init__)
    params = list(sig.parameters.keys())



def test_javamm_entityclass_is_not_abstract():
    assert not inspect.isabstract(JavaMM_EntityClass)


def test_javamm_entityclass_constructor_exists():
    assert callable(JavaMM_EntityClass.__init__)


def test_javamm_entityclass_constructor_args():
    sig = inspect.signature(JavaMM_EntityClass.__init__)
    params = list(sig.parameters.keys())



def test_javamm_annotation_is_not_abstract():
    assert not inspect.isabstract(JavaMM_Annotation)


def test_javamm_annotation_constructor_exists():
    assert callable(JavaMM_Annotation.__init__)


def test_javamm_annotation_constructor_args():
    sig = inspect.signature(JavaMM_Annotation.__init__)
    params = list(sig.parameters.keys())
    assert "content" in params, "Missing parameter 'content'"
    assert "type" in params, "Missing parameter 'type'"

def test_javamm_annotation_has_content():
    assert hasattr(JavaMM_Annotation, "content")
    descriptor = None
    for klass in JavaMM_Annotation.__mro__:
        if "content" in klass.__dict__:
            descriptor = klass.__dict__["content"]
            break
    assert isinstance(descriptor, property)

def test_javamm_annotation_has_type():
    assert hasattr(JavaMM_Annotation, "type")
    descriptor = None
    for klass in JavaMM_Annotation.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_javamm_class_is_not_abstract():
    assert not inspect.isabstract(JavaMM_Class)


def test_javamm_class_constructor_exists():
    assert callable(JavaMM_Class.__init__)


def test_javamm_class_constructor_args():
    sig = inspect.signature(JavaMM_Class.__init__)
    params = list(sig.parameters.keys())



def test_javamm_container_is_not_abstract():
    assert not inspect.isabstract(JavaMM_Container)


def test_javamm_container_constructor_exists():
    assert callable(JavaMM_Container.__init__)


def test_javamm_container_constructor_args():
    sig = inspect.signature(JavaMM_Container.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_javamm_container_has_type():
    assert hasattr(JavaMM_Container, "type")
    descriptor = None
    for klass in JavaMM_Container.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_javamm_primitivetype_is_not_abstract():
    assert not inspect.isabstract(JavaMM_PrimitiveType)


def test_javamm_primitivetype_constructor_exists():
    assert callable(JavaMM_PrimitiveType.__init__)


def test_javamm_primitivetype_constructor_args():
    sig = inspect.signature(JavaMM_PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_javamm_package_is_not_abstract():
    assert not inspect.isabstract(JavaMM_Package)


def test_javamm_package_constructor_exists():
    assert callable(JavaMM_Package.__init__)


def test_javamm_package_constructor_args():
    sig = inspect.signature(JavaMM_Package.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_javamm_package_has_name():
    assert hasattr(JavaMM_Package, "name")
    descriptor = None
    for klass in JavaMM_Package.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_javamm_program_is_not_abstract():
    assert not inspect.isabstract(JavaMM_Program)


def test_javamm_program_constructor_exists():
    assert callable(JavaMM_Program.__init__)


def test_javamm_program_constructor_args():
    sig = inspect.signature(JavaMM_Program.__init__)
    params = list(sig.parameters.keys())



def test_javamm_type_is_not_abstract():
    assert not inspect.isabstract(JavaMM_Type)


def test_javamm_type_constructor_exists():
    assert callable(JavaMM_Type.__init__)


def test_javamm_type_constructor_args():
    sig = inspect.signature(JavaMM_Type.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_javamm_type_has_name():
    assert hasattr(JavaMM_Type, "name")
    descriptor = None
    for klass in JavaMM_Type.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_javamm_attribute_is_not_abstract():
    assert not inspect.isabstract(JavaMM_Attribute)


def test_javamm_attribute_constructor_exists():
    assert callable(JavaMM_Attribute.__init__)


def test_javamm_attribute_constructor_args():
    sig = inspect.signature(JavaMM_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "visibility" in params, "Missing parameter 'visibility'"

def test_javamm_attribute_has_name():
    assert hasattr(JavaMM_Attribute, "name")
    descriptor = None
    for klass in JavaMM_Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_javamm_attribute_has_visibility():
    assert hasattr(JavaMM_Attribute, "visibility")
    descriptor = None
    for klass in JavaMM_Attribute.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
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
Class_strategy = st.builds(
    Class,
)
JavaMM_DAOClass_strategy = st.builds(
    JavaMM_DAOClass,
)
JavaMM_TestClass_strategy = st.builds(
    JavaMM_TestClass,
)
JavaMM_EntityClass_strategy = st.builds(
    JavaMM_EntityClass,
)
JavaMM_Annotation_strategy = st.builds(
    JavaMM_Annotation,
    content=
        safe_text,
    type=
        safe_text
)
Type_strategy = st.builds(
    Type,
)
JavaMM_Class_strategy = st.builds(
    JavaMM_Class,
)
JavaMM_Container_strategy = st.builds(
    JavaMM_Container,
    type=
        safe_text
)
JavaMM_PrimitiveType_strategy = st.builds(
    JavaMM_PrimitiveType,
)
JavaMM_Package_strategy = st.builds(
    JavaMM_Package,
    name=
        safe_text
)
JavaMM_Program_strategy = st.builds(
    JavaMM_Program,
)
JavaMM_Type_strategy = st.builds(
    JavaMM_Type,
    name=
        safe_text
)
JavaMM_Attribute_strategy = st.builds(
    JavaMM_Attribute,
    name=
        safe_text,
    visibility=
        safe_text
)

@given(instance=Class_strategy)
@settings(max_examples=50)
def test_class_instantiation(instance):
    assert isinstance(instance, Class)

@given(instance=JavaMM_DAOClass_strategy)
@settings(max_examples=50)
def test_javamm_daoclass_instantiation(instance):
    assert isinstance(instance, JavaMM_DAOClass)

@given(instance=JavaMM_TestClass_strategy)
@settings(max_examples=50)
def test_javamm_testclass_instantiation(instance):
    assert isinstance(instance, JavaMM_TestClass)

@given(instance=JavaMM_EntityClass_strategy)
@settings(max_examples=50)
def test_javamm_entityclass_instantiation(instance):
    assert isinstance(instance, JavaMM_EntityClass)

@given(instance=JavaMM_Annotation_strategy)
@settings(max_examples=50)
def test_javamm_annotation_instantiation(instance):
    assert isinstance(instance, JavaMM_Annotation)



@given(instance=JavaMM_Annotation_strategy)
def test_javamm_annotation_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original



@given(instance=JavaMM_Annotation_strategy)
def test_javamm_annotation_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=JavaMM_Class_strategy)
@settings(max_examples=50)
def test_javamm_class_instantiation(instance):
    assert isinstance(instance, JavaMM_Class)

@given(instance=JavaMM_Container_strategy)
@settings(max_examples=50)
def test_javamm_container_instantiation(instance):
    assert isinstance(instance, JavaMM_Container)



@given(instance=JavaMM_Container_strategy)
def test_javamm_container_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=JavaMM_PrimitiveType_strategy)
@settings(max_examples=50)
def test_javamm_primitivetype_instantiation(instance):
    assert isinstance(instance, JavaMM_PrimitiveType)

@given(instance=JavaMM_Package_strategy)
@settings(max_examples=50)
def test_javamm_package_instantiation(instance):
    assert isinstance(instance, JavaMM_Package)



@given(instance=JavaMM_Package_strategy)
def test_javamm_package_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=JavaMM_Program_strategy)
@settings(max_examples=50)
def test_javamm_program_instantiation(instance):
    assert isinstance(instance, JavaMM_Program)

@given(instance=JavaMM_Type_strategy)
@settings(max_examples=50)
def test_javamm_type_instantiation(instance):
    assert isinstance(instance, JavaMM_Type)



@given(instance=JavaMM_Type_strategy)
def test_javamm_type_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=JavaMM_Attribute_strategy)
@settings(max_examples=50)
def test_javamm_attribute_instantiation(instance):
    assert isinstance(instance, JavaMM_Attribute)



@given(instance=JavaMM_Attribute_strategy)
def test_javamm_attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=JavaMM_Attribute_strategy)
def test_javamm_attribute_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original
