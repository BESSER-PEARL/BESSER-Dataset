import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    classes::Description,
    BuiltInType,
    classes::IntegerType,
    classes::StringType,
    Type,
    classes::ClassRef,
    classes::BuiltInType,
    classes::Type,
    Value,
    classes::ConstantRef,
    classes::IntegerLiteral,
    classes::Value,
    Description,
    classes::Attribute,
    Content,
    classes::Constant,
    classes::Content,
    classes::ClassModel,
    classes::Class,
    classes::Association,
    Visibility,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_classes::description_is_not_abstract():
    assert not inspect.isabstract(classes::Description)


def test_classes::description_constructor_exists():
    assert callable(classes::Description.__init__)


def test_classes::description_constructor_args():
    sig = inspect.signature(classes::Description.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"

def test_classes::description_has_description():
    assert hasattr(classes::Description, "description")
    descriptor = None
    for klass in classes::Description.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_builtintype_is_not_abstract():
    assert not inspect.isabstract(BuiltInType)


def test_builtintype_constructor_exists():
    assert callable(BuiltInType.__init__)


def test_builtintype_constructor_args():
    sig = inspect.signature(BuiltInType.__init__)
    params = list(sig.parameters.keys())



def test_classes::integertype_is_not_abstract():
    assert not inspect.isabstract(classes::IntegerType)


def test_classes::integertype_constructor_exists():
    assert callable(classes::IntegerType.__init__)


def test_classes::integertype_constructor_args():
    sig = inspect.signature(classes::IntegerType.__init__)
    params = list(sig.parameters.keys())



def test_classes::stringtype_is_not_abstract():
    assert not inspect.isabstract(classes::StringType)


def test_classes::stringtype_constructor_exists():
    assert callable(classes::StringType.__init__)


def test_classes::stringtype_constructor_args():
    sig = inspect.signature(classes::StringType.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_classes::classref_is_not_abstract():
    assert not inspect.isabstract(classes::ClassRef)


def test_classes::classref_constructor_exists():
    assert callable(classes::ClassRef.__init__)


def test_classes::classref_constructor_args():
    sig = inspect.signature(classes::ClassRef.__init__)
    params = list(sig.parameters.keys())



def test_classes::builtintype_is_not_abstract():
    assert not inspect.isabstract(classes::BuiltInType)


def test_classes::builtintype_constructor_exists():
    assert callable(classes::BuiltInType.__init__)


def test_classes::builtintype_constructor_args():
    sig = inspect.signature(classes::BuiltInType.__init__)
    params = list(sig.parameters.keys())



def test_classes::type_is_not_abstract():
    assert not inspect.isabstract(classes::Type)


def test_classes::type_constructor_exists():
    assert callable(classes::Type.__init__)


def test_classes::type_constructor_args():
    sig = inspect.signature(classes::Type.__init__)
    params = list(sig.parameters.keys())



def test_value_is_not_abstract():
    assert not inspect.isabstract(Value)


def test_value_constructor_exists():
    assert callable(Value.__init__)


def test_value_constructor_args():
    sig = inspect.signature(Value.__init__)
    params = list(sig.parameters.keys())



def test_classes::constantref_is_not_abstract():
    assert not inspect.isabstract(classes::ConstantRef)


def test_classes::constantref_constructor_exists():
    assert callable(classes::ConstantRef.__init__)


def test_classes::constantref_constructor_args():
    sig = inspect.signature(classes::ConstantRef.__init__)
    params = list(sig.parameters.keys())



def test_classes::integerliteral_is_not_abstract():
    assert not inspect.isabstract(classes::IntegerLiteral)


def test_classes::integerliteral_constructor_exists():
    assert callable(classes::IntegerLiteral.__init__)


def test_classes::integerliteral_constructor_args():
    sig = inspect.signature(classes::IntegerLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_classes::integerliteral_has_value():
    assert hasattr(classes::IntegerLiteral, "value")
    descriptor = None
    for klass in classes::IntegerLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_classes::value_is_not_abstract():
    assert not inspect.isabstract(classes::Value)


def test_classes::value_constructor_exists():
    assert callable(classes::Value.__init__)


def test_classes::value_constructor_args():
    sig = inspect.signature(classes::Value.__init__)
    params = list(sig.parameters.keys())



def test_description_is_not_abstract():
    assert not inspect.isabstract(Description)


def test_description_constructor_exists():
    assert callable(Description.__init__)


def test_description_constructor_args():
    sig = inspect.signature(Description.__init__)
    params = list(sig.parameters.keys())



def test_classes::attribute_is_not_abstract():
    assert not inspect.isabstract(classes::Attribute)


def test_classes::attribute_constructor_exists():
    assert callable(classes::Attribute.__init__)


def test_classes::attribute_constructor_args():
    sig = inspect.signature(classes::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "visibility" in params, "Missing parameter 'visibility'"

def test_classes::attribute_has_name():
    assert hasattr(classes::Attribute, "name")
    descriptor = None
    for klass in classes::Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_classes::attribute_has_visibility():
    assert hasattr(classes::Attribute, "visibility")
    descriptor = None
    for klass in classes::Attribute.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)



def test_content_is_not_abstract():
    assert not inspect.isabstract(Content)


def test_content_constructor_exists():
    assert callable(Content.__init__)


def test_content_constructor_args():
    sig = inspect.signature(Content.__init__)
    params = list(sig.parameters.keys())



def test_classes::constant_is_not_abstract():
    assert not inspect.isabstract(classes::Constant)


def test_classes::constant_constructor_exists():
    assert callable(classes::Constant.__init__)


def test_classes::constant_constructor_args():
    sig = inspect.signature(classes::Constant.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_classes::constant_has_name():
    assert hasattr(classes::Constant, "name")
    descriptor = None
    for klass in classes::Constant.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_classes::content_is_not_abstract():
    assert not inspect.isabstract(classes::Content)


def test_classes::content_constructor_exists():
    assert callable(classes::Content.__init__)


def test_classes::content_constructor_args():
    sig = inspect.signature(classes::Content.__init__)
    params = list(sig.parameters.keys())



def test_classes::classmodel_is_not_abstract():
    assert not inspect.isabstract(classes::ClassModel)


def test_classes::classmodel_constructor_exists():
    assert callable(classes::ClassModel.__init__)


def test_classes::classmodel_constructor_args():
    sig = inspect.signature(classes::ClassModel.__init__)
    params = list(sig.parameters.keys())



def test_classes::class_is_not_abstract():
    assert not inspect.isabstract(classes::Class)


def test_classes::class_constructor_exists():
    assert callable(classes::Class.__init__)


def test_classes::class_constructor_args():
    sig = inspect.signature(classes::Class.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_classes::class_has_name():
    assert hasattr(classes::Class, "name")
    descriptor = None
    for klass in classes::Class.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_classes::association_is_not_abstract():
    assert not inspect.isabstract(classes::Association)


def test_classes::association_constructor_exists():
    assert callable(classes::Association.__init__)


def test_classes::association_constructor_args():
    sig = inspect.signature(classes::Association.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_classes::association_has_name():
    assert hasattr(classes::Association, "name")
    descriptor = None
    for klass in classes::Association.__mro__:
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
        "protected",
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
classes::Description_strategy = st.builds(
    classes::Description,
    description=
        safe_text
)
BuiltInType_strategy = st.builds(
    BuiltInType,
)
classes::IntegerType_strategy = st.builds(
    classes::IntegerType,
)
classes::StringType_strategy = st.builds(
    classes::StringType,
)
Type_strategy = st.builds(
    Type,
)
classes::ClassRef_strategy = st.builds(
    classes::ClassRef,
)
classes::BuiltInType_strategy = st.builds(
    classes::BuiltInType,
)
classes::Type_strategy = st.builds(
    classes::Type,
)
Value_strategy = st.builds(
    Value,
)
classes::ConstantRef_strategy = st.builds(
    classes::ConstantRef,
)
classes::IntegerLiteral_strategy = st.builds(
    classes::IntegerLiteral,
    value=
        st.integers()
)
classes::Value_strategy = st.builds(
    classes::Value,
)
Description_strategy = st.builds(
    Description,
)
classes::Attribute_strategy = st.builds(
    classes::Attribute,
    name=
        safe_text,
    visibility=
        safe_text
)
Content_strategy = st.builds(
    Content,
)
classes::Constant_strategy = st.builds(
    classes::Constant,
    name=
        safe_text
)
classes::Content_strategy = st.builds(
    classes::Content,
)
classes::ClassModel_strategy = st.builds(
    classes::ClassModel,
)
classes::Class_strategy = st.builds(
    classes::Class,
    name=
        safe_text
)
classes::Association_strategy = st.builds(
    classes::Association,
    name=
        safe_text
)

@given(instance=classes::Description_strategy)
@settings(max_examples=50)
def test_classes::description_instantiation(instance):
    assert isinstance(instance, classes::Description)

@given(instance=classes::Description_strategy)
def test_classes::description_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=classes::Description_strategy)
def test_classes::description_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=BuiltInType_strategy)
@settings(max_examples=50)
def test_builtintype_instantiation(instance):
    assert isinstance(instance, BuiltInType)

@given(instance=classes::IntegerType_strategy)
@settings(max_examples=50)
def test_classes::integertype_instantiation(instance):
    assert isinstance(instance, classes::IntegerType)

@given(instance=classes::StringType_strategy)
@settings(max_examples=50)
def test_classes::stringtype_instantiation(instance):
    assert isinstance(instance, classes::StringType)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=classes::ClassRef_strategy)
@settings(max_examples=50)
def test_classes::classref_instantiation(instance):
    assert isinstance(instance, classes::ClassRef)

@given(instance=classes::BuiltInType_strategy)
@settings(max_examples=50)
def test_classes::builtintype_instantiation(instance):
    assert isinstance(instance, classes::BuiltInType)

@given(instance=classes::Type_strategy)
@settings(max_examples=50)
def test_classes::type_instantiation(instance):
    assert isinstance(instance, classes::Type)

@given(instance=Value_strategy)
@settings(max_examples=50)
def test_value_instantiation(instance):
    assert isinstance(instance, Value)

@given(instance=classes::ConstantRef_strategy)
@settings(max_examples=50)
def test_classes::constantref_instantiation(instance):
    assert isinstance(instance, classes::ConstantRef)

@given(instance=classes::IntegerLiteral_strategy)
@settings(max_examples=50)
def test_classes::integerliteral_instantiation(instance):
    assert isinstance(instance, classes::IntegerLiteral)

@given(instance=classes::IntegerLiteral_strategy)
def test_classes::integerliteral_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=classes::IntegerLiteral_strategy)
def test_classes::integerliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=classes::Value_strategy)
@settings(max_examples=50)
def test_classes::value_instantiation(instance):
    assert isinstance(instance, classes::Value)

@given(instance=Description_strategy)
@settings(max_examples=50)
def test_description_instantiation(instance):
    assert isinstance(instance, Description)

@given(instance=classes::Attribute_strategy)
@settings(max_examples=50)
def test_classes::attribute_instantiation(instance):
    assert isinstance(instance, classes::Attribute)

@given(instance=classes::Attribute_strategy)
def test_classes::attribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=classes::Attribute_strategy)
def test_classes::attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=classes::Attribute_strategy)
def test_classes::attribute_visibility_type(instance):
    assert isinstance(instance.visibility, str)


@given(instance=classes::Attribute_strategy)
def test_classes::attribute_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=Content_strategy)
@settings(max_examples=50)
def test_content_instantiation(instance):
    assert isinstance(instance, Content)

@given(instance=classes::Constant_strategy)
@settings(max_examples=50)
def test_classes::constant_instantiation(instance):
    assert isinstance(instance, classes::Constant)

@given(instance=classes::Constant_strategy)
def test_classes::constant_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=classes::Constant_strategy)
def test_classes::constant_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=classes::Content_strategy)
@settings(max_examples=50)
def test_classes::content_instantiation(instance):
    assert isinstance(instance, classes::Content)

@given(instance=classes::ClassModel_strategy)
@settings(max_examples=50)
def test_classes::classmodel_instantiation(instance):
    assert isinstance(instance, classes::ClassModel)

@given(instance=classes::Class_strategy)
@settings(max_examples=50)
def test_classes::class_instantiation(instance):
    assert isinstance(instance, classes::Class)

@given(instance=classes::Class_strategy)
def test_classes::class_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=classes::Class_strategy)
def test_classes::class_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=classes::Association_strategy)
@settings(max_examples=50)
def test_classes::association_instantiation(instance):
    assert isinstance(instance, classes::Association)

@given(instance=classes::Association_strategy)
def test_classes::association_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=classes::Association_strategy)
def test_classes::association_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
