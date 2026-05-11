import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    tallerE1Java::Package,
    tallerE1Java::Program,
    Class,
    tallerE1Java::TestClass,
    tallerE1Java::DAOClass,
    tallerE1Java::EntityClass,
    tallerE1Java::Annotation,
    tallerE1Java::Type,
    tallerE1Java::Attribute,
    Type,
    tallerE1Java::PrimitiveType,
    tallerE1Java::Container,
    tallerE1Java::Class,
    Visibility,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_tallere1java::package_is_not_abstract():
    assert not inspect.isabstract(tallerE1Java::Package)


def test_tallere1java::package_constructor_exists():
    assert callable(tallerE1Java::Package.__init__)


def test_tallere1java::package_constructor_args():
    sig = inspect.signature(tallerE1Java::Package.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_tallere1java::package_has_name():
    assert hasattr(tallerE1Java::Package, "name")
    descriptor = None
    for klass in tallerE1Java::Package.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_tallere1java::program_is_not_abstract():
    assert not inspect.isabstract(tallerE1Java::Program)


def test_tallere1java::program_constructor_exists():
    assert callable(tallerE1Java::Program.__init__)


def test_tallere1java::program_constructor_args():
    sig = inspect.signature(tallerE1Java::Program.__init__)
    params = list(sig.parameters.keys())



def test_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_class_constructor_exists():
    assert callable(Class.__init__)


def test_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_tallere1java::testclass_is_not_abstract():
    assert not inspect.isabstract(tallerE1Java::TestClass)


def test_tallere1java::testclass_constructor_exists():
    assert callable(tallerE1Java::TestClass.__init__)


def test_tallere1java::testclass_constructor_args():
    sig = inspect.signature(tallerE1Java::TestClass.__init__)
    params = list(sig.parameters.keys())



def test_tallere1java::daoclass_is_not_abstract():
    assert not inspect.isabstract(tallerE1Java::DAOClass)


def test_tallere1java::daoclass_constructor_exists():
    assert callable(tallerE1Java::DAOClass.__init__)


def test_tallere1java::daoclass_constructor_args():
    sig = inspect.signature(tallerE1Java::DAOClass.__init__)
    params = list(sig.parameters.keys())



def test_tallere1java::entityclass_is_not_abstract():
    assert not inspect.isabstract(tallerE1Java::EntityClass)


def test_tallere1java::entityclass_constructor_exists():
    assert callable(tallerE1Java::EntityClass.__init__)


def test_tallere1java::entityclass_constructor_args():
    sig = inspect.signature(tallerE1Java::EntityClass.__init__)
    params = list(sig.parameters.keys())



def test_tallere1java::annotation_is_not_abstract():
    assert not inspect.isabstract(tallerE1Java::Annotation)


def test_tallere1java::annotation_constructor_exists():
    assert callable(tallerE1Java::Annotation.__init__)


def test_tallere1java::annotation_constructor_args():
    sig = inspect.signature(tallerE1Java::Annotation.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "content" in params, "Missing parameter 'content'"

def test_tallere1java::annotation_has_type():
    assert hasattr(tallerE1Java::Annotation, "type")
    descriptor = None
    for klass in tallerE1Java::Annotation.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_tallere1java::annotation_has_content():
    assert hasattr(tallerE1Java::Annotation, "content")
    descriptor = None
    for klass in tallerE1Java::Annotation.__mro__:
        if "content" in klass.__dict__:
            descriptor = klass.__dict__["content"]
            break
    assert isinstance(descriptor, property)



def test_tallere1java::type_is_not_abstract():
    assert not inspect.isabstract(tallerE1Java::Type)


def test_tallere1java::type_constructor_exists():
    assert callable(tallerE1Java::Type.__init__)


def test_tallere1java::type_constructor_args():
    sig = inspect.signature(tallerE1Java::Type.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_tallere1java::type_has_name():
    assert hasattr(tallerE1Java::Type, "name")
    descriptor = None
    for klass in tallerE1Java::Type.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_tallere1java::attribute_is_not_abstract():
    assert not inspect.isabstract(tallerE1Java::Attribute)


def test_tallere1java::attribute_constructor_exists():
    assert callable(tallerE1Java::Attribute.__init__)


def test_tallere1java::attribute_constructor_args():
    sig = inspect.signature(tallerE1Java::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "visibility" in params, "Missing parameter 'visibility'"
    assert "name" in params, "Missing parameter 'name'"

def test_tallere1java::attribute_has_visibility():
    assert hasattr(tallerE1Java::Attribute, "visibility")
    descriptor = None
    for klass in tallerE1Java::Attribute.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)

def test_tallere1java::attribute_has_name():
    assert hasattr(tallerE1Java::Attribute, "name")
    descriptor = None
    for klass in tallerE1Java::Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_tallere1java::primitivetype_is_not_abstract():
    assert not inspect.isabstract(tallerE1Java::PrimitiveType)


def test_tallere1java::primitivetype_constructor_exists():
    assert callable(tallerE1Java::PrimitiveType.__init__)


def test_tallere1java::primitivetype_constructor_args():
    sig = inspect.signature(tallerE1Java::PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_tallere1java::container_is_not_abstract():
    assert not inspect.isabstract(tallerE1Java::Container)


def test_tallere1java::container_constructor_exists():
    assert callable(tallerE1Java::Container.__init__)


def test_tallere1java::container_constructor_args():
    sig = inspect.signature(tallerE1Java::Container.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_tallere1java::container_has_type():
    assert hasattr(tallerE1Java::Container, "type")
    descriptor = None
    for klass in tallerE1Java::Container.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_tallere1java::class_is_not_abstract():
    assert not inspect.isabstract(tallerE1Java::Class)


def test_tallere1java::class_constructor_exists():
    assert callable(tallerE1Java::Class.__init__)


def test_tallere1java::class_constructor_args():
    sig = inspect.signature(tallerE1Java::Class.__init__)
    params = list(sig.parameters.keys())

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
tallerE1Java::Package_strategy = st.builds(
    tallerE1Java::Package,
    name=
        safe_text
)
tallerE1Java::Program_strategy = st.builds(
    tallerE1Java::Program,
)
Class_strategy = st.builds(
    Class,
)
tallerE1Java::TestClass_strategy = st.builds(
    tallerE1Java::TestClass,
)
tallerE1Java::DAOClass_strategy = st.builds(
    tallerE1Java::DAOClass,
)
tallerE1Java::EntityClass_strategy = st.builds(
    tallerE1Java::EntityClass,
)
tallerE1Java::Annotation_strategy = st.builds(
    tallerE1Java::Annotation,
    type=
        safe_text,
    content=
        safe_text
)
tallerE1Java::Type_strategy = st.builds(
    tallerE1Java::Type,
    name=
        safe_text
)
tallerE1Java::Attribute_strategy = st.builds(
    tallerE1Java::Attribute,
    visibility=
        safe_text,
    name=
        safe_text
)
Type_strategy = st.builds(
    Type,
)
tallerE1Java::PrimitiveType_strategy = st.builds(
    tallerE1Java::PrimitiveType,
)
tallerE1Java::Container_strategy = st.builds(
    tallerE1Java::Container,
    type=
        safe_text
)
tallerE1Java::Class_strategy = st.builds(
    tallerE1Java::Class,
)

@given(instance=tallerE1Java::Package_strategy)
@settings(max_examples=50)
def test_tallere1java::package_instantiation(instance):
    assert isinstance(instance, tallerE1Java::Package)

@given(instance=tallerE1Java::Package_strategy)
def test_tallere1java::package_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=tallerE1Java::Package_strategy)
def test_tallere1java::package_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=tallerE1Java::Program_strategy)
@settings(max_examples=50)
def test_tallere1java::program_instantiation(instance):
    assert isinstance(instance, tallerE1Java::Program)

@given(instance=Class_strategy)
@settings(max_examples=50)
def test_class_instantiation(instance):
    assert isinstance(instance, Class)

@given(instance=tallerE1Java::TestClass_strategy)
@settings(max_examples=50)
def test_tallere1java::testclass_instantiation(instance):
    assert isinstance(instance, tallerE1Java::TestClass)

@given(instance=tallerE1Java::DAOClass_strategy)
@settings(max_examples=50)
def test_tallere1java::daoclass_instantiation(instance):
    assert isinstance(instance, tallerE1Java::DAOClass)

@given(instance=tallerE1Java::EntityClass_strategy)
@settings(max_examples=50)
def test_tallere1java::entityclass_instantiation(instance):
    assert isinstance(instance, tallerE1Java::EntityClass)

@given(instance=tallerE1Java::Annotation_strategy)
@settings(max_examples=50)
def test_tallere1java::annotation_instantiation(instance):
    assert isinstance(instance, tallerE1Java::Annotation)

@given(instance=tallerE1Java::Annotation_strategy)
def test_tallere1java::annotation_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=tallerE1Java::Annotation_strategy)
def test_tallere1java::annotation_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=tallerE1Java::Annotation_strategy)
def test_tallere1java::annotation_content_type(instance):
    assert isinstance(instance.content, str)


@given(instance=tallerE1Java::Annotation_strategy)
def test_tallere1java::annotation_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original

@given(instance=tallerE1Java::Type_strategy)
@settings(max_examples=50)
def test_tallere1java::type_instantiation(instance):
    assert isinstance(instance, tallerE1Java::Type)

@given(instance=tallerE1Java::Type_strategy)
def test_tallere1java::type_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=tallerE1Java::Type_strategy)
def test_tallere1java::type_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=tallerE1Java::Attribute_strategy)
@settings(max_examples=50)
def test_tallere1java::attribute_instantiation(instance):
    assert isinstance(instance, tallerE1Java::Attribute)

@given(instance=tallerE1Java::Attribute_strategy)
def test_tallere1java::attribute_visibility_type(instance):
    assert isinstance(instance.visibility, str)


@given(instance=tallerE1Java::Attribute_strategy)
def test_tallere1java::attribute_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=tallerE1Java::Attribute_strategy)
def test_tallere1java::attribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=tallerE1Java::Attribute_strategy)
def test_tallere1java::attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=tallerE1Java::PrimitiveType_strategy)
@settings(max_examples=50)
def test_tallere1java::primitivetype_instantiation(instance):
    assert isinstance(instance, tallerE1Java::PrimitiveType)

@given(instance=tallerE1Java::Container_strategy)
@settings(max_examples=50)
def test_tallere1java::container_instantiation(instance):
    assert isinstance(instance, tallerE1Java::Container)

@given(instance=tallerE1Java::Container_strategy)
def test_tallere1java::container_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=tallerE1Java::Container_strategy)
def test_tallere1java::container_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=tallerE1Java::Class_strategy)
@settings(max_examples=50)
def test_tallere1java::class_instantiation(instance):
    assert isinstance(instance, tallerE1Java::Class)
