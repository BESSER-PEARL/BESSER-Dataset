import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Class,
    JavaMM::DAOClass,
    JavaMM::TestClass,
    JavaMM::EntityClass,
    JavaMM::Annotation,
    Type,
    JavaMM::Class,
    JavaMM::Container,
    JavaMM::PrimitiveType,
    JavaMM::Package,
    JavaMM::Program,
    JavaMM::Type,
    JavaMM::Attribute,
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



def test_javamm::daoclass_is_not_abstract():
    assert not inspect.isabstract(JavaMM::DAOClass)


def test_javamm::daoclass_constructor_exists():
    assert callable(JavaMM::DAOClass.__init__)


def test_javamm::daoclass_constructor_args():
    sig = inspect.signature(JavaMM::DAOClass.__init__)
    params = list(sig.parameters.keys())



def test_javamm::testclass_is_not_abstract():
    assert not inspect.isabstract(JavaMM::TestClass)


def test_javamm::testclass_constructor_exists():
    assert callable(JavaMM::TestClass.__init__)


def test_javamm::testclass_constructor_args():
    sig = inspect.signature(JavaMM::TestClass.__init__)
    params = list(sig.parameters.keys())



def test_javamm::entityclass_is_not_abstract():
    assert not inspect.isabstract(JavaMM::EntityClass)


def test_javamm::entityclass_constructor_exists():
    assert callable(JavaMM::EntityClass.__init__)


def test_javamm::entityclass_constructor_args():
    sig = inspect.signature(JavaMM::EntityClass.__init__)
    params = list(sig.parameters.keys())



def test_javamm::annotation_is_not_abstract():
    assert not inspect.isabstract(JavaMM::Annotation)


def test_javamm::annotation_constructor_exists():
    assert callable(JavaMM::Annotation.__init__)


def test_javamm::annotation_constructor_args():
    sig = inspect.signature(JavaMM::Annotation.__init__)
    params = list(sig.parameters.keys())
    assert "content" in params, "Missing parameter 'content'"
    assert "type" in params, "Missing parameter 'type'"

def test_javamm::annotation_has_content():
    assert hasattr(JavaMM::Annotation, "content")
    descriptor = None
    for klass in JavaMM::Annotation.__mro__:
        if "content" in klass.__dict__:
            descriptor = klass.__dict__["content"]
            break
    assert isinstance(descriptor, property)

def test_javamm::annotation_has_type():
    assert hasattr(JavaMM::Annotation, "type")
    descriptor = None
    for klass in JavaMM::Annotation.__mro__:
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



def test_javamm::class_is_not_abstract():
    assert not inspect.isabstract(JavaMM::Class)


def test_javamm::class_constructor_exists():
    assert callable(JavaMM::Class.__init__)


def test_javamm::class_constructor_args():
    sig = inspect.signature(JavaMM::Class.__init__)
    params = list(sig.parameters.keys())



def test_javamm::container_is_not_abstract():
    assert not inspect.isabstract(JavaMM::Container)


def test_javamm::container_constructor_exists():
    assert callable(JavaMM::Container.__init__)


def test_javamm::container_constructor_args():
    sig = inspect.signature(JavaMM::Container.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_javamm::container_has_type():
    assert hasattr(JavaMM::Container, "type")
    descriptor = None
    for klass in JavaMM::Container.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_javamm::primitivetype_is_not_abstract():
    assert not inspect.isabstract(JavaMM::PrimitiveType)


def test_javamm::primitivetype_constructor_exists():
    assert callable(JavaMM::PrimitiveType.__init__)


def test_javamm::primitivetype_constructor_args():
    sig = inspect.signature(JavaMM::PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_javamm::package_is_not_abstract():
    assert not inspect.isabstract(JavaMM::Package)


def test_javamm::package_constructor_exists():
    assert callable(JavaMM::Package.__init__)


def test_javamm::package_constructor_args():
    sig = inspect.signature(JavaMM::Package.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_javamm::package_has_name():
    assert hasattr(JavaMM::Package, "name")
    descriptor = None
    for klass in JavaMM::Package.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_javamm::program_is_not_abstract():
    assert not inspect.isabstract(JavaMM::Program)


def test_javamm::program_constructor_exists():
    assert callable(JavaMM::Program.__init__)


def test_javamm::program_constructor_args():
    sig = inspect.signature(JavaMM::Program.__init__)
    params = list(sig.parameters.keys())



def test_javamm::type_is_not_abstract():
    assert not inspect.isabstract(JavaMM::Type)


def test_javamm::type_constructor_exists():
    assert callable(JavaMM::Type.__init__)


def test_javamm::type_constructor_args():
    sig = inspect.signature(JavaMM::Type.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_javamm::type_has_name():
    assert hasattr(JavaMM::Type, "name")
    descriptor = None
    for klass in JavaMM::Type.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_javamm::attribute_is_not_abstract():
    assert not inspect.isabstract(JavaMM::Attribute)


def test_javamm::attribute_constructor_exists():
    assert callable(JavaMM::Attribute.__init__)


def test_javamm::attribute_constructor_args():
    sig = inspect.signature(JavaMM::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "visibility" in params, "Missing parameter 'visibility'"

def test_javamm::attribute_has_name():
    assert hasattr(JavaMM::Attribute, "name")
    descriptor = None
    for klass in JavaMM::Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_javamm::attribute_has_visibility():
    assert hasattr(JavaMM::Attribute, "visibility")
    descriptor = None
    for klass in JavaMM::Attribute.__mro__:
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
        "private",
        "public",
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
JavaMM::DAOClass_strategy = st.builds(
    JavaMM::DAOClass,
)
JavaMM::TestClass_strategy = st.builds(
    JavaMM::TestClass,
)
JavaMM::EntityClass_strategy = st.builds(
    JavaMM::EntityClass,
)
JavaMM::Annotation_strategy = st.builds(
    JavaMM::Annotation,
    content=
        safe_text,
    type=
        safe_text
)
Type_strategy = st.builds(
    Type,
)
JavaMM::Class_strategy = st.builds(
    JavaMM::Class,
)
JavaMM::Container_strategy = st.builds(
    JavaMM::Container,
    type=
        safe_text
)
JavaMM::PrimitiveType_strategy = st.builds(
    JavaMM::PrimitiveType,
)
JavaMM::Package_strategy = st.builds(
    JavaMM::Package,
    name=
        safe_text
)
JavaMM::Program_strategy = st.builds(
    JavaMM::Program,
)
JavaMM::Type_strategy = st.builds(
    JavaMM::Type,
    name=
        safe_text
)
JavaMM::Attribute_strategy = st.builds(
    JavaMM::Attribute,
    name=
        safe_text,
    visibility=
        safe_text
)

@given(instance=Class_strategy)
@settings(max_examples=50)
def test_class_instantiation(instance):
    assert isinstance(instance, Class)

@given(instance=JavaMM::DAOClass_strategy)
@settings(max_examples=50)
def test_javamm::daoclass_instantiation(instance):
    assert isinstance(instance, JavaMM::DAOClass)

@given(instance=JavaMM::TestClass_strategy)
@settings(max_examples=50)
def test_javamm::testclass_instantiation(instance):
    assert isinstance(instance, JavaMM::TestClass)

@given(instance=JavaMM::EntityClass_strategy)
@settings(max_examples=50)
def test_javamm::entityclass_instantiation(instance):
    assert isinstance(instance, JavaMM::EntityClass)

@given(instance=JavaMM::Annotation_strategy)
@settings(max_examples=50)
def test_javamm::annotation_instantiation(instance):
    assert isinstance(instance, JavaMM::Annotation)

@given(instance=JavaMM::Annotation_strategy)
def test_javamm::annotation_content_type(instance):
    assert isinstance(instance.content, str)


@given(instance=JavaMM::Annotation_strategy)
def test_javamm::annotation_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original

@given(instance=JavaMM::Annotation_strategy)
def test_javamm::annotation_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=JavaMM::Annotation_strategy)
def test_javamm::annotation_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=JavaMM::Class_strategy)
@settings(max_examples=50)
def test_javamm::class_instantiation(instance):
    assert isinstance(instance, JavaMM::Class)

@given(instance=JavaMM::Container_strategy)
@settings(max_examples=50)
def test_javamm::container_instantiation(instance):
    assert isinstance(instance, JavaMM::Container)

@given(instance=JavaMM::Container_strategy)
def test_javamm::container_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=JavaMM::Container_strategy)
def test_javamm::container_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=JavaMM::PrimitiveType_strategy)
@settings(max_examples=50)
def test_javamm::primitivetype_instantiation(instance):
    assert isinstance(instance, JavaMM::PrimitiveType)

@given(instance=JavaMM::Package_strategy)
@settings(max_examples=50)
def test_javamm::package_instantiation(instance):
    assert isinstance(instance, JavaMM::Package)

@given(instance=JavaMM::Package_strategy)
def test_javamm::package_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=JavaMM::Package_strategy)
def test_javamm::package_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=JavaMM::Program_strategy)
@settings(max_examples=50)
def test_javamm::program_instantiation(instance):
    assert isinstance(instance, JavaMM::Program)

@given(instance=JavaMM::Type_strategy)
@settings(max_examples=50)
def test_javamm::type_instantiation(instance):
    assert isinstance(instance, JavaMM::Type)

@given(instance=JavaMM::Type_strategy)
def test_javamm::type_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=JavaMM::Type_strategy)
def test_javamm::type_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=JavaMM::Attribute_strategy)
@settings(max_examples=50)
def test_javamm::attribute_instantiation(instance):
    assert isinstance(instance, JavaMM::Attribute)

@given(instance=JavaMM::Attribute_strategy)
def test_javamm::attribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=JavaMM::Attribute_strategy)
def test_javamm::attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=JavaMM::Attribute_strategy)
def test_javamm::attribute_visibility_type(instance):
    assert isinstance(instance.visibility, str)


@given(instance=JavaMM::Attribute_strategy)
def test_javamm::attribute_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original
