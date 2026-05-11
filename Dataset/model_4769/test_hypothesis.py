import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    atl::types::EClass,
    atl::types::EObject,
    RefType,
    atl::types::Metaclass,
    atl::types::Unknown,
    annotations::atl::types::Type,
    annotations::atl::types::EObject,
    AtlAnnotation,
    atl::types::annotations::ExpressionAnnotation,
    atl::types::annotations::BindingAnnotation,
    atl::types::annotations::HelperAnnotation,
    atl::types::annotations::AtlAnnotation,
    ReflectiveType,
    atl::types::ReflectiveClass,
    atl::types::Type,
    atl::types::TupleAttribute,
    PrimitiveType,
    atl::types::FloatType,
    atl::types::IntegerType,
    atl::types::StringType,
    atl::types::BooleanType,
    Type,
    atl::types::MapType,
    atl::types::RefType,
    atl::types::EnumType,
    atl::types::ReflectiveType,
    atl::types::UnionType,
    atl::types::TupleType,
    atl::types::EmptyCollection,
    atl::types::ThisModuleType,
    atl::types::PrimitiveType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_atl::types::eclass_is_not_abstract():
    assert not inspect.isabstract(atl::types::EClass)


def test_atl::types::eclass_constructor_exists():
    assert callable(atl::types::EClass.__init__)


def test_atl::types::eclass_constructor_args():
    sig = inspect.signature(atl::types::EClass.__init__)
    params = list(sig.parameters.keys())



def test_atl::types::eobject_is_not_abstract():
    assert not inspect.isabstract(atl::types::EObject)


def test_atl::types::eobject_constructor_exists():
    assert callable(atl::types::EObject.__init__)


def test_atl::types::eobject_constructor_args():
    sig = inspect.signature(atl::types::EObject.__init__)
    params = list(sig.parameters.keys())



def test_reftype_is_not_abstract():
    assert not inspect.isabstract(RefType)


def test_reftype_constructor_exists():
    assert callable(RefType.__init__)


def test_reftype_constructor_args():
    sig = inspect.signature(RefType.__init__)
    params = list(sig.parameters.keys())



def test_atl::types::metaclass_is_not_abstract():
    assert not inspect.isabstract(atl::types::Metaclass)


def test_atl::types::metaclass_constructor_exists():
    assert callable(atl::types::Metaclass.__init__)


def test_atl::types::metaclass_constructor_args():
    sig = inspect.signature(atl::types::Metaclass.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_atl::types::metaclass_has_name():
    assert hasattr(atl::types::Metaclass, "name")
    descriptor = None
    for klass in atl::types::Metaclass.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_atl::types::unknown_is_not_abstract():
    assert not inspect.isabstract(atl::types::Unknown)


def test_atl::types::unknown_constructor_exists():
    assert callable(atl::types::Unknown.__init__)


def test_atl::types::unknown_constructor_args():
    sig = inspect.signature(atl::types::Unknown.__init__)
    params = list(sig.parameters.keys())



def test_annotations::atl::types::type_is_not_abstract():
    assert not inspect.isabstract(annotations::atl::types::Type)


def test_annotations::atl::types::type_constructor_exists():
    assert callable(annotations::atl::types::Type.__init__)


def test_annotations::atl::types::type_constructor_args():
    sig = inspect.signature(annotations::atl::types::Type.__init__)
    params = list(sig.parameters.keys())



def test_annotations::atl::types::eobject_is_not_abstract():
    assert not inspect.isabstract(annotations::atl::types::EObject)


def test_annotations::atl::types::eobject_constructor_exists():
    assert callable(annotations::atl::types::EObject.__init__)


def test_annotations::atl::types::eobject_constructor_args():
    sig = inspect.signature(annotations::atl::types::EObject.__init__)
    params = list(sig.parameters.keys())



def test_atlannotation_is_not_abstract():
    assert not inspect.isabstract(AtlAnnotation)


def test_atlannotation_constructor_exists():
    assert callable(AtlAnnotation.__init__)


def test_atlannotation_constructor_args():
    sig = inspect.signature(AtlAnnotation.__init__)
    params = list(sig.parameters.keys())



def test_atl::types::annotations::expressionannotation_is_not_abstract():
    assert not inspect.isabstract(atl::types::annotations::ExpressionAnnotation)


def test_atl::types::annotations::expressionannotation_constructor_exists():
    assert callable(atl::types::annotations::ExpressionAnnotation.__init__)


def test_atl::types::annotations::expressionannotation_constructor_args():
    sig = inspect.signature(atl::types::annotations::ExpressionAnnotation.__init__)
    params = list(sig.parameters.keys())



def test_atl::types::annotations::bindingannotation_is_not_abstract():
    assert not inspect.isabstract(atl::types::annotations::BindingAnnotation)


def test_atl::types::annotations::bindingannotation_constructor_exists():
    assert callable(atl::types::annotations::BindingAnnotation.__init__)


def test_atl::types::annotations::bindingannotation_constructor_args():
    sig = inspect.signature(atl::types::annotations::BindingAnnotation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_atl::types::annotations::bindingannotation_has_name():
    assert hasattr(atl::types::annotations::BindingAnnotation, "name")
    descriptor = None
    for klass in atl::types::annotations::BindingAnnotation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_atl::types::annotations::helperannotation_is_not_abstract():
    assert not inspect.isabstract(atl::types::annotations::HelperAnnotation)


def test_atl::types::annotations::helperannotation_constructor_exists():
    assert callable(atl::types::annotations::HelperAnnotation.__init__)


def test_atl::types::annotations::helperannotation_constructor_args():
    sig = inspect.signature(atl::types::annotations::HelperAnnotation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_atl::types::annotations::helperannotation_has_name():
    assert hasattr(atl::types::annotations::HelperAnnotation, "name")
    descriptor = None
    for klass in atl::types::annotations::HelperAnnotation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_atl::types::annotations::atlannotation_is_not_abstract():
    assert not inspect.isabstract(atl::types::annotations::AtlAnnotation)


def test_atl::types::annotations::atlannotation_constructor_exists():
    assert callable(atl::types::annotations::AtlAnnotation.__init__)


def test_atl::types::annotations::atlannotation_constructor_args():
    sig = inspect.signature(atl::types::annotations::AtlAnnotation.__init__)
    params = list(sig.parameters.keys())



def test_reflectivetype_is_not_abstract():
    assert not inspect.isabstract(ReflectiveType)


def test_reflectivetype_constructor_exists():
    assert callable(ReflectiveType.__init__)


def test_reflectivetype_constructor_args():
    sig = inspect.signature(ReflectiveType.__init__)
    params = list(sig.parameters.keys())



def test_atl::types::reflectiveclass_is_not_abstract():
    assert not inspect.isabstract(atl::types::ReflectiveClass)


def test_atl::types::reflectiveclass_constructor_exists():
    assert callable(atl::types::ReflectiveClass.__init__)


def test_atl::types::reflectiveclass_constructor_args():
    sig = inspect.signature(atl::types::ReflectiveClass.__init__)
    params = list(sig.parameters.keys())



def test_atl::types::type_is_not_abstract():
    assert not inspect.isabstract(atl::types::Type)


def test_atl::types::type_constructor_exists():
    assert callable(atl::types::Type.__init__)


def test_atl::types::type_constructor_args():
    sig = inspect.signature(atl::types::Type.__init__)
    params = list(sig.parameters.keys())
    assert "multivalued" in params, "Missing parameter 'multivalued'"

def test_atl::types::type_has_multivalued():
    assert hasattr(atl::types::Type, "multivalued")
    descriptor = None
    for klass in atl::types::Type.__mro__:
        if "multivalued" in klass.__dict__:
            descriptor = klass.__dict__["multivalued"]
            break
    assert isinstance(descriptor, property)



def test_atl::types::tupleattribute_is_not_abstract():
    assert not inspect.isabstract(atl::types::TupleAttribute)


def test_atl::types::tupleattribute_constructor_exists():
    assert callable(atl::types::TupleAttribute.__init__)


def test_atl::types::tupleattribute_constructor_args():
    sig = inspect.signature(atl::types::TupleAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_atl::types::tupleattribute_has_name():
    assert hasattr(atl::types::TupleAttribute, "name")
    descriptor = None
    for klass in atl::types::TupleAttribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_primitivetype_is_not_abstract():
    assert not inspect.isabstract(PrimitiveType)


def test_primitivetype_constructor_exists():
    assert callable(PrimitiveType.__init__)


def test_primitivetype_constructor_args():
    sig = inspect.signature(PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_atl::types::floattype_is_not_abstract():
    assert not inspect.isabstract(atl::types::FloatType)


def test_atl::types::floattype_constructor_exists():
    assert callable(atl::types::FloatType.__init__)


def test_atl::types::floattype_constructor_args():
    sig = inspect.signature(atl::types::FloatType.__init__)
    params = list(sig.parameters.keys())



def test_atl::types::integertype_is_not_abstract():
    assert not inspect.isabstract(atl::types::IntegerType)


def test_atl::types::integertype_constructor_exists():
    assert callable(atl::types::IntegerType.__init__)


def test_atl::types::integertype_constructor_args():
    sig = inspect.signature(atl::types::IntegerType.__init__)
    params = list(sig.parameters.keys())



def test_atl::types::stringtype_is_not_abstract():
    assert not inspect.isabstract(atl::types::StringType)


def test_atl::types::stringtype_constructor_exists():
    assert callable(atl::types::StringType.__init__)


def test_atl::types::stringtype_constructor_args():
    sig = inspect.signature(atl::types::StringType.__init__)
    params = list(sig.parameters.keys())



def test_atl::types::booleantype_is_not_abstract():
    assert not inspect.isabstract(atl::types::BooleanType)


def test_atl::types::booleantype_constructor_exists():
    assert callable(atl::types::BooleanType.__init__)


def test_atl::types::booleantype_constructor_args():
    sig = inspect.signature(atl::types::BooleanType.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_atl::types::maptype_is_not_abstract():
    assert not inspect.isabstract(atl::types::MapType)


def test_atl::types::maptype_constructor_exists():
    assert callable(atl::types::MapType.__init__)


def test_atl::types::maptype_constructor_args():
    sig = inspect.signature(atl::types::MapType.__init__)
    params = list(sig.parameters.keys())



def test_atl::types::reftype_is_not_abstract():
    assert not inspect.isabstract(atl::types::RefType)


def test_atl::types::reftype_constructor_exists():
    assert callable(atl::types::RefType.__init__)


def test_atl::types::reftype_constructor_args():
    sig = inspect.signature(atl::types::RefType.__init__)
    params = list(sig.parameters.keys())



def test_atl::types::enumtype_is_not_abstract():
    assert not inspect.isabstract(atl::types::EnumType)


def test_atl::types::enumtype_constructor_exists():
    assert callable(atl::types::EnumType.__init__)


def test_atl::types::enumtype_constructor_args():
    sig = inspect.signature(atl::types::EnumType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_atl::types::enumtype_has_name():
    assert hasattr(atl::types::EnumType, "name")
    descriptor = None
    for klass in atl::types::EnumType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_atl::types::reflectivetype_is_not_abstract():
    assert not inspect.isabstract(atl::types::ReflectiveType)


def test_atl::types::reflectivetype_constructor_exists():
    assert callable(atl::types::ReflectiveType.__init__)


def test_atl::types::reflectivetype_constructor_args():
    sig = inspect.signature(atl::types::ReflectiveType.__init__)
    params = list(sig.parameters.keys())



def test_atl::types::uniontype_is_not_abstract():
    assert not inspect.isabstract(atl::types::UnionType)


def test_atl::types::uniontype_constructor_exists():
    assert callable(atl::types::UnionType.__init__)


def test_atl::types::uniontype_constructor_args():
    sig = inspect.signature(atl::types::UnionType.__init__)
    params = list(sig.parameters.keys())



def test_atl::types::tupletype_is_not_abstract():
    assert not inspect.isabstract(atl::types::TupleType)


def test_atl::types::tupletype_constructor_exists():
    assert callable(atl::types::TupleType.__init__)


def test_atl::types::tupletype_constructor_args():
    sig = inspect.signature(atl::types::TupleType.__init__)
    params = list(sig.parameters.keys())



def test_atl::types::emptycollection_is_not_abstract():
    assert not inspect.isabstract(atl::types::EmptyCollection)


def test_atl::types::emptycollection_constructor_exists():
    assert callable(atl::types::EmptyCollection.__init__)


def test_atl::types::emptycollection_constructor_args():
    sig = inspect.signature(atl::types::EmptyCollection.__init__)
    params = list(sig.parameters.keys())



def test_atl::types::thismoduletype_is_not_abstract():
    assert not inspect.isabstract(atl::types::ThisModuleType)


def test_atl::types::thismoduletype_constructor_exists():
    assert callable(atl::types::ThisModuleType.__init__)


def test_atl::types::thismoduletype_constructor_args():
    sig = inspect.signature(atl::types::ThisModuleType.__init__)
    params = list(sig.parameters.keys())



def test_atl::types::primitivetype_is_not_abstract():
    assert not inspect.isabstract(atl::types::PrimitiveType)


def test_atl::types::primitivetype_constructor_exists():
    assert callable(atl::types::PrimitiveType.__init__)


def test_atl::types::primitivetype_constructor_args():
    sig = inspect.signature(atl::types::PrimitiveType.__init__)
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
atl::types::EClass_strategy = st.builds(
    atl::types::EClass,
)
atl::types::EObject_strategy = st.builds(
    atl::types::EObject,
)
RefType_strategy = st.builds(
    RefType,
)
atl::types::Metaclass_strategy = st.builds(
    atl::types::Metaclass,
    name=
        safe_text
)
atl::types::Unknown_strategy = st.builds(
    atl::types::Unknown,
)
annotations::atl::types::Type_strategy = st.builds(
    annotations::atl::types::Type,
)
annotations::atl::types::EObject_strategy = st.builds(
    annotations::atl::types::EObject,
)
AtlAnnotation_strategy = st.builds(
    AtlAnnotation,
)
atl::types::annotations::ExpressionAnnotation_strategy = st.builds(
    atl::types::annotations::ExpressionAnnotation,
)
atl::types::annotations::BindingAnnotation_strategy = st.builds(
    atl::types::annotations::BindingAnnotation,
    name=
        safe_text
)
atl::types::annotations::HelperAnnotation_strategy = st.builds(
    atl::types::annotations::HelperAnnotation,
    name=
        safe_text
)
atl::types::annotations::AtlAnnotation_strategy = st.builds(
    atl::types::annotations::AtlAnnotation,
)
ReflectiveType_strategy = st.builds(
    ReflectiveType,
)
atl::types::ReflectiveClass_strategy = st.builds(
    atl::types::ReflectiveClass,
)
atl::types::Type_strategy = st.builds(
    atl::types::Type,
    multivalued=
        st.booleans()
)
atl::types::TupleAttribute_strategy = st.builds(
    atl::types::TupleAttribute,
    name=
        safe_text
)
PrimitiveType_strategy = st.builds(
    PrimitiveType,
)
atl::types::FloatType_strategy = st.builds(
    atl::types::FloatType,
)
atl::types::IntegerType_strategy = st.builds(
    atl::types::IntegerType,
)
atl::types::StringType_strategy = st.builds(
    atl::types::StringType,
)
atl::types::BooleanType_strategy = st.builds(
    atl::types::BooleanType,
)
Type_strategy = st.builds(
    Type,
)
atl::types::MapType_strategy = st.builds(
    atl::types::MapType,
)
atl::types::RefType_strategy = st.builds(
    atl::types::RefType,
)
atl::types::EnumType_strategy = st.builds(
    atl::types::EnumType,
    name=
        safe_text
)
atl::types::ReflectiveType_strategy = st.builds(
    atl::types::ReflectiveType,
)
atl::types::UnionType_strategy = st.builds(
    atl::types::UnionType,
)
atl::types::TupleType_strategy = st.builds(
    atl::types::TupleType,
)
atl::types::EmptyCollection_strategy = st.builds(
    atl::types::EmptyCollection,
)
atl::types::ThisModuleType_strategy = st.builds(
    atl::types::ThisModuleType,
)
atl::types::PrimitiveType_strategy = st.builds(
    atl::types::PrimitiveType,
)

@given(instance=atl::types::EClass_strategy)
@settings(max_examples=50)
def test_atl::types::eclass_instantiation(instance):
    assert isinstance(instance, atl::types::EClass)

@given(instance=atl::types::EObject_strategy)
@settings(max_examples=50)
def test_atl::types::eobject_instantiation(instance):
    assert isinstance(instance, atl::types::EObject)

@given(instance=RefType_strategy)
@settings(max_examples=50)
def test_reftype_instantiation(instance):
    assert isinstance(instance, RefType)

@given(instance=atl::types::Metaclass_strategy)
@settings(max_examples=50)
def test_atl::types::metaclass_instantiation(instance):
    assert isinstance(instance, atl::types::Metaclass)

@given(instance=atl::types::Metaclass_strategy)
def test_atl::types::metaclass_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=atl::types::Metaclass_strategy)
def test_atl::types::metaclass_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=atl::types::Unknown_strategy)
@settings(max_examples=50)
def test_atl::types::unknown_instantiation(instance):
    assert isinstance(instance, atl::types::Unknown)

@given(instance=annotations::atl::types::Type_strategy)
@settings(max_examples=50)
def test_annotations::atl::types::type_instantiation(instance):
    assert isinstance(instance, annotations::atl::types::Type)

@given(instance=annotations::atl::types::EObject_strategy)
@settings(max_examples=50)
def test_annotations::atl::types::eobject_instantiation(instance):
    assert isinstance(instance, annotations::atl::types::EObject)

@given(instance=AtlAnnotation_strategy)
@settings(max_examples=50)
def test_atlannotation_instantiation(instance):
    assert isinstance(instance, AtlAnnotation)

@given(instance=atl::types::annotations::ExpressionAnnotation_strategy)
@settings(max_examples=50)
def test_atl::types::annotations::expressionannotation_instantiation(instance):
    assert isinstance(instance, atl::types::annotations::ExpressionAnnotation)

@given(instance=atl::types::annotations::BindingAnnotation_strategy)
@settings(max_examples=50)
def test_atl::types::annotations::bindingannotation_instantiation(instance):
    assert isinstance(instance, atl::types::annotations::BindingAnnotation)

@given(instance=atl::types::annotations::BindingAnnotation_strategy)
def test_atl::types::annotations::bindingannotation_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=atl::types::annotations::BindingAnnotation_strategy)
def test_atl::types::annotations::bindingannotation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=atl::types::annotations::HelperAnnotation_strategy)
@settings(max_examples=50)
def test_atl::types::annotations::helperannotation_instantiation(instance):
    assert isinstance(instance, atl::types::annotations::HelperAnnotation)

@given(instance=atl::types::annotations::HelperAnnotation_strategy)
def test_atl::types::annotations::helperannotation_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=atl::types::annotations::HelperAnnotation_strategy)
def test_atl::types::annotations::helperannotation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=atl::types::annotations::AtlAnnotation_strategy)
@settings(max_examples=50)
def test_atl::types::annotations::atlannotation_instantiation(instance):
    assert isinstance(instance, atl::types::annotations::AtlAnnotation)

@given(instance=ReflectiveType_strategy)
@settings(max_examples=50)
def test_reflectivetype_instantiation(instance):
    assert isinstance(instance, ReflectiveType)

@given(instance=atl::types::ReflectiveClass_strategy)
@settings(max_examples=50)
def test_atl::types::reflectiveclass_instantiation(instance):
    assert isinstance(instance, atl::types::ReflectiveClass)

@given(instance=atl::types::Type_strategy)
@settings(max_examples=50)
def test_atl::types::type_instantiation(instance):
    assert isinstance(instance, atl::types::Type)

@given(instance=atl::types::Type_strategy)
def test_atl::types::type_multivalued_type(instance):
    assert isinstance(instance.multivalued, bool)


@given(instance=atl::types::Type_strategy)
def test_atl::types::type_multivalued_setter(instance):
    original = instance.multivalued
    instance.multivalued = original
    assert instance.multivalued == original

@given(instance=atl::types::TupleAttribute_strategy)
@settings(max_examples=50)
def test_atl::types::tupleattribute_instantiation(instance):
    assert isinstance(instance, atl::types::TupleAttribute)

@given(instance=atl::types::TupleAttribute_strategy)
def test_atl::types::tupleattribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=atl::types::TupleAttribute_strategy)
def test_atl::types::tupleattribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=PrimitiveType_strategy)
@settings(max_examples=50)
def test_primitivetype_instantiation(instance):
    assert isinstance(instance, PrimitiveType)

@given(instance=atl::types::FloatType_strategy)
@settings(max_examples=50)
def test_atl::types::floattype_instantiation(instance):
    assert isinstance(instance, atl::types::FloatType)

@given(instance=atl::types::IntegerType_strategy)
@settings(max_examples=50)
def test_atl::types::integertype_instantiation(instance):
    assert isinstance(instance, atl::types::IntegerType)

@given(instance=atl::types::StringType_strategy)
@settings(max_examples=50)
def test_atl::types::stringtype_instantiation(instance):
    assert isinstance(instance, atl::types::StringType)

@given(instance=atl::types::BooleanType_strategy)
@settings(max_examples=50)
def test_atl::types::booleantype_instantiation(instance):
    assert isinstance(instance, atl::types::BooleanType)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=atl::types::MapType_strategy)
@settings(max_examples=50)
def test_atl::types::maptype_instantiation(instance):
    assert isinstance(instance, atl::types::MapType)

@given(instance=atl::types::RefType_strategy)
@settings(max_examples=50)
def test_atl::types::reftype_instantiation(instance):
    assert isinstance(instance, atl::types::RefType)

@given(instance=atl::types::EnumType_strategy)
@settings(max_examples=50)
def test_atl::types::enumtype_instantiation(instance):
    assert isinstance(instance, atl::types::EnumType)

@given(instance=atl::types::EnumType_strategy)
def test_atl::types::enumtype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=atl::types::EnumType_strategy)
def test_atl::types::enumtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=atl::types::ReflectiveType_strategy)
@settings(max_examples=50)
def test_atl::types::reflectivetype_instantiation(instance):
    assert isinstance(instance, atl::types::ReflectiveType)

@given(instance=atl::types::UnionType_strategy)
@settings(max_examples=50)
def test_atl::types::uniontype_instantiation(instance):
    assert isinstance(instance, atl::types::UnionType)

@given(instance=atl::types::TupleType_strategy)
@settings(max_examples=50)
def test_atl::types::tupletype_instantiation(instance):
    assert isinstance(instance, atl::types::TupleType)

@given(instance=atl::types::EmptyCollection_strategy)
@settings(max_examples=50)
def test_atl::types::emptycollection_instantiation(instance):
    assert isinstance(instance, atl::types::EmptyCollection)

@given(instance=atl::types::ThisModuleType_strategy)
@settings(max_examples=50)
def test_atl::types::thismoduletype_instantiation(instance):
    assert isinstance(instance, atl::types::ThisModuleType)

@given(instance=atl::types::PrimitiveType_strategy)
@settings(max_examples=50)
def test_atl::types::primitivetype_instantiation(instance):
    assert isinstance(instance, atl::types::PrimitiveType)
