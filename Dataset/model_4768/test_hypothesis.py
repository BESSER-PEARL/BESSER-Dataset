import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    types::MetaModel,
    types::EClass,
    EStructuralFeature,
    types::UnknownFeature,
    Metaclass,
    TypeError,
    types::UnresolvedTypeError,
    types::EObject,
    RefType,
    CollectionType,
    types::OrderedSetType,
    types::SetType,
    types::BagType,
    types::SequenceType,
    ReflectiveType,
    types::ReflectiveClass,
    types::Metaclass,
    PrimitiveType,
    types::BooleanType,
    Type,
    types::UnionType,
    types::EnumType,
    types::ReflectiveType,
    types::TypeError,
    types::CollectionType,
    types::ThisModuleType,
    types::EmptyCollectionType,
    types::PrimitiveType,
    types::EmptyCollection,
    types::OclUndefinedType,
    types::Type,
    types::Unknown,
    types::RefType,
    types::MapType,
    types::TupleAttribute,
    types::TupleType,
    types::FloatType,
    types::StringType,
    types::IntegerType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_types::metamodel_is_not_abstract():
    assert not inspect.isabstract(types::MetaModel)


def test_types::metamodel_constructor_exists():
    assert callable(types::MetaModel.__init__)


def test_types::metamodel_constructor_args():
    sig = inspect.signature(types::MetaModel.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_types::metamodel_has_name():
    assert hasattr(types::MetaModel, "name")
    descriptor = None
    for klass in types::MetaModel.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_types::eclass_is_not_abstract():
    assert not inspect.isabstract(types::EClass)


def test_types::eclass_constructor_exists():
    assert callable(types::EClass.__init__)


def test_types::eclass_constructor_args():
    sig = inspect.signature(types::EClass.__init__)
    params = list(sig.parameters.keys())



def test_estructuralfeature_is_not_abstract():
    assert not inspect.isabstract(EStructuralFeature)


def test_estructuralfeature_constructor_exists():
    assert callable(EStructuralFeature.__init__)


def test_estructuralfeature_constructor_args():
    sig = inspect.signature(EStructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_types::unknownfeature_is_not_abstract():
    assert not inspect.isabstract(types::UnknownFeature)


def test_types::unknownfeature_constructor_exists():
    assert callable(types::UnknownFeature.__init__)


def test_types::unknownfeature_constructor_args():
    sig = inspect.signature(types::UnknownFeature.__init__)
    params = list(sig.parameters.keys())



def test_metaclass_is_not_abstract():
    assert not inspect.isabstract(Metaclass)


def test_metaclass_constructor_exists():
    assert callable(Metaclass.__init__)


def test_metaclass_constructor_args():
    sig = inspect.signature(Metaclass.__init__)
    params = list(sig.parameters.keys())



def test_typeerror_is_not_abstract():
    assert not inspect.isabstract(TypeError)


def test_typeerror_constructor_exists():
    assert callable(TypeError.__init__)


def test_typeerror_constructor_args():
    sig = inspect.signature(TypeError.__init__)
    params = list(sig.parameters.keys())



def test_types::unresolvedtypeerror_is_not_abstract():
    assert not inspect.isabstract(types::UnresolvedTypeError)


def test_types::unresolvedtypeerror_constructor_exists():
    assert callable(types::UnresolvedTypeError.__init__)


def test_types::unresolvedtypeerror_constructor_args():
    sig = inspect.signature(types::UnresolvedTypeError.__init__)
    params = list(sig.parameters.keys())



def test_types::eobject_is_not_abstract():
    assert not inspect.isabstract(types::EObject)


def test_types::eobject_constructor_exists():
    assert callable(types::EObject.__init__)


def test_types::eobject_constructor_args():
    sig = inspect.signature(types::EObject.__init__)
    params = list(sig.parameters.keys())



def test_reftype_is_not_abstract():
    assert not inspect.isabstract(RefType)


def test_reftype_constructor_exists():
    assert callable(RefType.__init__)


def test_reftype_constructor_args():
    sig = inspect.signature(RefType.__init__)
    params = list(sig.parameters.keys())



def test_collectiontype_is_not_abstract():
    assert not inspect.isabstract(CollectionType)


def test_collectiontype_constructor_exists():
    assert callable(CollectionType.__init__)


def test_collectiontype_constructor_args():
    sig = inspect.signature(CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_types::orderedsettype_is_not_abstract():
    assert not inspect.isabstract(types::OrderedSetType)


def test_types::orderedsettype_constructor_exists():
    assert callable(types::OrderedSetType.__init__)


def test_types::orderedsettype_constructor_args():
    sig = inspect.signature(types::OrderedSetType.__init__)
    params = list(sig.parameters.keys())



def test_types::settype_is_not_abstract():
    assert not inspect.isabstract(types::SetType)


def test_types::settype_constructor_exists():
    assert callable(types::SetType.__init__)


def test_types::settype_constructor_args():
    sig = inspect.signature(types::SetType.__init__)
    params = list(sig.parameters.keys())



def test_types::bagtype_is_not_abstract():
    assert not inspect.isabstract(types::BagType)


def test_types::bagtype_constructor_exists():
    assert callable(types::BagType.__init__)


def test_types::bagtype_constructor_args():
    sig = inspect.signature(types::BagType.__init__)
    params = list(sig.parameters.keys())



def test_types::sequencetype_is_not_abstract():
    assert not inspect.isabstract(types::SequenceType)


def test_types::sequencetype_constructor_exists():
    assert callable(types::SequenceType.__init__)


def test_types::sequencetype_constructor_args():
    sig = inspect.signature(types::SequenceType.__init__)
    params = list(sig.parameters.keys())



def test_reflectivetype_is_not_abstract():
    assert not inspect.isabstract(ReflectiveType)


def test_reflectivetype_constructor_exists():
    assert callable(ReflectiveType.__init__)


def test_reflectivetype_constructor_args():
    sig = inspect.signature(ReflectiveType.__init__)
    params = list(sig.parameters.keys())



def test_types::reflectiveclass_is_not_abstract():
    assert not inspect.isabstract(types::ReflectiveClass)


def test_types::reflectiveclass_constructor_exists():
    assert callable(types::ReflectiveClass.__init__)


def test_types::reflectiveclass_constructor_args():
    sig = inspect.signature(types::ReflectiveClass.__init__)
    params = list(sig.parameters.keys())



def test_types::metaclass_is_not_abstract():
    assert not inspect.isabstract(types::Metaclass)


def test_types::metaclass_constructor_exists():
    assert callable(types::Metaclass.__init__)


def test_types::metaclass_constructor_args():
    sig = inspect.signature(types::Metaclass.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "explicitOcurrence" in params, "Missing parameter 'explicitOcurrence'"

def test_types::metaclass_has_name():
    assert hasattr(types::Metaclass, "name")
    descriptor = None
    for klass in types::Metaclass.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_types::metaclass_has_explicitOcurrence():
    assert hasattr(types::Metaclass, "explicitOcurrence")
    descriptor = None
    for klass in types::Metaclass.__mro__:
        if "explicitOcurrence" in klass.__dict__:
            descriptor = klass.__dict__["explicitOcurrence"]
            break
    assert isinstance(descriptor, property)



def test_primitivetype_is_not_abstract():
    assert not inspect.isabstract(PrimitiveType)


def test_primitivetype_constructor_exists():
    assert callable(PrimitiveType.__init__)


def test_primitivetype_constructor_args():
    sig = inspect.signature(PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_types::booleantype_is_not_abstract():
    assert not inspect.isabstract(types::BooleanType)


def test_types::booleantype_constructor_exists():
    assert callable(types::BooleanType.__init__)


def test_types::booleantype_constructor_args():
    sig = inspect.signature(types::BooleanType.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_types::uniontype_is_not_abstract():
    assert not inspect.isabstract(types::UnionType)


def test_types::uniontype_constructor_exists():
    assert callable(types::UnionType.__init__)


def test_types::uniontype_constructor_args():
    sig = inspect.signature(types::UnionType.__init__)
    params = list(sig.parameters.keys())



def test_types::enumtype_is_not_abstract():
    assert not inspect.isabstract(types::EnumType)


def test_types::enumtype_constructor_exists():
    assert callable(types::EnumType.__init__)


def test_types::enumtype_constructor_args():
    sig = inspect.signature(types::EnumType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_types::enumtype_has_name():
    assert hasattr(types::EnumType, "name")
    descriptor = None
    for klass in types::EnumType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_types::reflectivetype_is_not_abstract():
    assert not inspect.isabstract(types::ReflectiveType)


def test_types::reflectivetype_constructor_exists():
    assert callable(types::ReflectiveType.__init__)


def test_types::reflectivetype_constructor_args():
    sig = inspect.signature(types::ReflectiveType.__init__)
    params = list(sig.parameters.keys())



def test_types::typeerror_is_not_abstract():
    assert not inspect.isabstract(types::TypeError)


def test_types::typeerror_constructor_exists():
    assert callable(types::TypeError.__init__)


def test_types::typeerror_constructor_args():
    sig = inspect.signature(types::TypeError.__init__)
    params = list(sig.parameters.keys())



def test_types::collectiontype_is_not_abstract():
    assert not inspect.isabstract(types::CollectionType)


def test_types::collectiontype_constructor_exists():
    assert callable(types::CollectionType.__init__)


def test_types::collectiontype_constructor_args():
    sig = inspect.signature(types::CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_types::thismoduletype_is_not_abstract():
    assert not inspect.isabstract(types::ThisModuleType)


def test_types::thismoduletype_constructor_exists():
    assert callable(types::ThisModuleType.__init__)


def test_types::thismoduletype_constructor_args():
    sig = inspect.signature(types::ThisModuleType.__init__)
    params = list(sig.parameters.keys())



def test_types::emptycollectiontype_is_not_abstract():
    assert not inspect.isabstract(types::EmptyCollectionType)


def test_types::emptycollectiontype_constructor_exists():
    assert callable(types::EmptyCollectionType.__init__)


def test_types::emptycollectiontype_constructor_args():
    sig = inspect.signature(types::EmptyCollectionType.__init__)
    params = list(sig.parameters.keys())



def test_types::primitivetype_is_not_abstract():
    assert not inspect.isabstract(types::PrimitiveType)


def test_types::primitivetype_constructor_exists():
    assert callable(types::PrimitiveType.__init__)


def test_types::primitivetype_constructor_args():
    sig = inspect.signature(types::PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_types::emptycollection_is_not_abstract():
    assert not inspect.isabstract(types::EmptyCollection)


def test_types::emptycollection_constructor_exists():
    assert callable(types::EmptyCollection.__init__)


def test_types::emptycollection_constructor_args():
    sig = inspect.signature(types::EmptyCollection.__init__)
    params = list(sig.parameters.keys())



def test_types::oclundefinedtype_is_not_abstract():
    assert not inspect.isabstract(types::OclUndefinedType)


def test_types::oclundefinedtype_constructor_exists():
    assert callable(types::OclUndefinedType.__init__)


def test_types::oclundefinedtype_constructor_args():
    sig = inspect.signature(types::OclUndefinedType.__init__)
    params = list(sig.parameters.keys())



def test_types::type_is_not_abstract():
    assert not inspect.isabstract(types::Type)


def test_types::type_constructor_exists():
    assert callable(types::Type.__init__)


def test_types::type_constructor_args():
    sig = inspect.signature(types::Type.__init__)
    params = list(sig.parameters.keys())
    assert "multivalued" in params, "Missing parameter 'multivalued'"
    assert "mayBeUndefined" in params, "Missing parameter 'mayBeUndefined'"
    assert "metamodelRef" in params, "Missing parameter 'metamodelRef'"

def test_types::type_has_multivalued():
    assert hasattr(types::Type, "multivalued")
    descriptor = None
    for klass in types::Type.__mro__:
        if "multivalued" in klass.__dict__:
            descriptor = klass.__dict__["multivalued"]
            break
    assert isinstance(descriptor, property)

def test_types::type_has_mayBeUndefined():
    assert hasattr(types::Type, "mayBeUndefined")
    descriptor = None
    for klass in types::Type.__mro__:
        if "mayBeUndefined" in klass.__dict__:
            descriptor = klass.__dict__["mayBeUndefined"]
            break
    assert isinstance(descriptor, property)

def test_types::type_has_metamodelRef():
    assert hasattr(types::Type, "metamodelRef")
    descriptor = None
    for klass in types::Type.__mro__:
        if "metamodelRef" in klass.__dict__:
            descriptor = klass.__dict__["metamodelRef"]
            break
    assert isinstance(descriptor, property)



def test_types::unknown_is_not_abstract():
    assert not inspect.isabstract(types::Unknown)


def test_types::unknown_constructor_exists():
    assert callable(types::Unknown.__init__)


def test_types::unknown_constructor_args():
    sig = inspect.signature(types::Unknown.__init__)
    params = list(sig.parameters.keys())



def test_types::reftype_is_not_abstract():
    assert not inspect.isabstract(types::RefType)


def test_types::reftype_constructor_exists():
    assert callable(types::RefType.__init__)


def test_types::reftype_constructor_args():
    sig = inspect.signature(types::RefType.__init__)
    params = list(sig.parameters.keys())



def test_types::maptype_is_not_abstract():
    assert not inspect.isabstract(types::MapType)


def test_types::maptype_constructor_exists():
    assert callable(types::MapType.__init__)


def test_types::maptype_constructor_args():
    sig = inspect.signature(types::MapType.__init__)
    params = list(sig.parameters.keys())



def test_types::tupleattribute_is_not_abstract():
    assert not inspect.isabstract(types::TupleAttribute)


def test_types::tupleattribute_constructor_exists():
    assert callable(types::TupleAttribute.__init__)


def test_types::tupleattribute_constructor_args():
    sig = inspect.signature(types::TupleAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_types::tupleattribute_has_name():
    assert hasattr(types::TupleAttribute, "name")
    descriptor = None
    for klass in types::TupleAttribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_types::tupletype_is_not_abstract():
    assert not inspect.isabstract(types::TupleType)


def test_types::tupletype_constructor_exists():
    assert callable(types::TupleType.__init__)


def test_types::tupletype_constructor_args():
    sig = inspect.signature(types::TupleType.__init__)
    params = list(sig.parameters.keys())



def test_types::floattype_is_not_abstract():
    assert not inspect.isabstract(types::FloatType)


def test_types::floattype_constructor_exists():
    assert callable(types::FloatType.__init__)


def test_types::floattype_constructor_args():
    sig = inspect.signature(types::FloatType.__init__)
    params = list(sig.parameters.keys())



def test_types::stringtype_is_not_abstract():
    assert not inspect.isabstract(types::StringType)


def test_types::stringtype_constructor_exists():
    assert callable(types::StringType.__init__)


def test_types::stringtype_constructor_args():
    sig = inspect.signature(types::StringType.__init__)
    params = list(sig.parameters.keys())



def test_types::integertype_is_not_abstract():
    assert not inspect.isabstract(types::IntegerType)


def test_types::integertype_constructor_exists():
    assert callable(types::IntegerType.__init__)


def test_types::integertype_constructor_args():
    sig = inspect.signature(types::IntegerType.__init__)
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
types::MetaModel_strategy = st.builds(
    types::MetaModel,
    name=
        safe_text
)
types::EClass_strategy = st.builds(
    types::EClass,
)
EStructuralFeature_strategy = st.builds(
    EStructuralFeature,
)
types::UnknownFeature_strategy = st.builds(
    types::UnknownFeature,
)
Metaclass_strategy = st.builds(
    Metaclass,
)
TypeError_strategy = st.builds(
    TypeError,
)
types::UnresolvedTypeError_strategy = st.builds(
    types::UnresolvedTypeError,
)
types::EObject_strategy = st.builds(
    types::EObject,
)
RefType_strategy = st.builds(
    RefType,
)
CollectionType_strategy = st.builds(
    CollectionType,
)
types::OrderedSetType_strategy = st.builds(
    types::OrderedSetType,
)
types::SetType_strategy = st.builds(
    types::SetType,
)
types::BagType_strategy = st.builds(
    types::BagType,
)
types::SequenceType_strategy = st.builds(
    types::SequenceType,
)
ReflectiveType_strategy = st.builds(
    ReflectiveType,
)
types::ReflectiveClass_strategy = st.builds(
    types::ReflectiveClass,
)
types::Metaclass_strategy = st.builds(
    types::Metaclass,
    name=
        safe_text,
    explicitOcurrence=
        st.booleans()
)
PrimitiveType_strategy = st.builds(
    PrimitiveType,
)
types::BooleanType_strategy = st.builds(
    types::BooleanType,
)
Type_strategy = st.builds(
    Type,
)
types::UnionType_strategy = st.builds(
    types::UnionType,
)
types::EnumType_strategy = st.builds(
    types::EnumType,
    name=
        safe_text
)
types::ReflectiveType_strategy = st.builds(
    types::ReflectiveType,
)
types::TypeError_strategy = st.builds(
    types::TypeError,
)
types::CollectionType_strategy = st.builds(
    types::CollectionType,
)
types::ThisModuleType_strategy = st.builds(
    types::ThisModuleType,
)
types::EmptyCollectionType_strategy = st.builds(
    types::EmptyCollectionType,
)
types::PrimitiveType_strategy = st.builds(
    types::PrimitiveType,
)
types::EmptyCollection_strategy = st.builds(
    types::EmptyCollection,
)
types::OclUndefinedType_strategy = st.builds(
    types::OclUndefinedType,
)
types::Type_strategy = st.builds(
    types::Type,
    multivalued=
        st.booleans(),
    mayBeUndefined=
        st.booleans(),
    metamodelRef=
        safe_text
)
types::Unknown_strategy = st.builds(
    types::Unknown,
)
types::RefType_strategy = st.builds(
    types::RefType,
)
types::MapType_strategy = st.builds(
    types::MapType,
)
types::TupleAttribute_strategy = st.builds(
    types::TupleAttribute,
    name=
        safe_text
)
types::TupleType_strategy = st.builds(
    types::TupleType,
)
types::FloatType_strategy = st.builds(
    types::FloatType,
)
types::StringType_strategy = st.builds(
    types::StringType,
)
types::IntegerType_strategy = st.builds(
    types::IntegerType,
)

@given(instance=types::MetaModel_strategy)
@settings(max_examples=50)
def test_types::metamodel_instantiation(instance):
    assert isinstance(instance, types::MetaModel)

@given(instance=types::MetaModel_strategy)
def test_types::metamodel_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=types::MetaModel_strategy)
def test_types::metamodel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=types::EClass_strategy)
@settings(max_examples=50)
def test_types::eclass_instantiation(instance):
    assert isinstance(instance, types::EClass)

@given(instance=EStructuralFeature_strategy)
@settings(max_examples=50)
def test_estructuralfeature_instantiation(instance):
    assert isinstance(instance, EStructuralFeature)

@given(instance=types::UnknownFeature_strategy)
@settings(max_examples=50)
def test_types::unknownfeature_instantiation(instance):
    assert isinstance(instance, types::UnknownFeature)

@given(instance=Metaclass_strategy)
@settings(max_examples=50)
def test_metaclass_instantiation(instance):
    assert isinstance(instance, Metaclass)

@given(instance=TypeError_strategy)
@settings(max_examples=50)
def test_typeerror_instantiation(instance):
    assert isinstance(instance, TypeError)

@given(instance=types::UnresolvedTypeError_strategy)
@settings(max_examples=50)
def test_types::unresolvedtypeerror_instantiation(instance):
    assert isinstance(instance, types::UnresolvedTypeError)

@given(instance=types::EObject_strategy)
@settings(max_examples=50)
def test_types::eobject_instantiation(instance):
    assert isinstance(instance, types::EObject)

@given(instance=RefType_strategy)
@settings(max_examples=50)
def test_reftype_instantiation(instance):
    assert isinstance(instance, RefType)

@given(instance=CollectionType_strategy)
@settings(max_examples=50)
def test_collectiontype_instantiation(instance):
    assert isinstance(instance, CollectionType)

@given(instance=types::OrderedSetType_strategy)
@settings(max_examples=50)
def test_types::orderedsettype_instantiation(instance):
    assert isinstance(instance, types::OrderedSetType)

@given(instance=types::SetType_strategy)
@settings(max_examples=50)
def test_types::settype_instantiation(instance):
    assert isinstance(instance, types::SetType)

@given(instance=types::BagType_strategy)
@settings(max_examples=50)
def test_types::bagtype_instantiation(instance):
    assert isinstance(instance, types::BagType)

@given(instance=types::SequenceType_strategy)
@settings(max_examples=50)
def test_types::sequencetype_instantiation(instance):
    assert isinstance(instance, types::SequenceType)

@given(instance=ReflectiveType_strategy)
@settings(max_examples=50)
def test_reflectivetype_instantiation(instance):
    assert isinstance(instance, ReflectiveType)

@given(instance=types::ReflectiveClass_strategy)
@settings(max_examples=50)
def test_types::reflectiveclass_instantiation(instance):
    assert isinstance(instance, types::ReflectiveClass)

@given(instance=types::Metaclass_strategy)
@settings(max_examples=50)
def test_types::metaclass_instantiation(instance):
    assert isinstance(instance, types::Metaclass)

@given(instance=types::Metaclass_strategy)
def test_types::metaclass_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=types::Metaclass_strategy)
def test_types::metaclass_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=types::Metaclass_strategy)
def test_types::metaclass_explicitOcurrence_type(instance):
    assert isinstance(instance.explicitOcurrence, bool)


@given(instance=types::Metaclass_strategy)
def test_types::metaclass_explicitOcurrence_setter(instance):
    original = instance.explicitOcurrence
    instance.explicitOcurrence = original
    assert instance.explicitOcurrence == original

@given(instance=PrimitiveType_strategy)
@settings(max_examples=50)
def test_primitivetype_instantiation(instance):
    assert isinstance(instance, PrimitiveType)

@given(instance=types::BooleanType_strategy)
@settings(max_examples=50)
def test_types::booleantype_instantiation(instance):
    assert isinstance(instance, types::BooleanType)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=types::UnionType_strategy)
@settings(max_examples=50)
def test_types::uniontype_instantiation(instance):
    assert isinstance(instance, types::UnionType)

@given(instance=types::EnumType_strategy)
@settings(max_examples=50)
def test_types::enumtype_instantiation(instance):
    assert isinstance(instance, types::EnumType)

@given(instance=types::EnumType_strategy)
def test_types::enumtype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=types::EnumType_strategy)
def test_types::enumtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=types::ReflectiveType_strategy)
@settings(max_examples=50)
def test_types::reflectivetype_instantiation(instance):
    assert isinstance(instance, types::ReflectiveType)

@given(instance=types::TypeError_strategy)
@settings(max_examples=50)
def test_types::typeerror_instantiation(instance):
    assert isinstance(instance, types::TypeError)

@given(instance=types::CollectionType_strategy)
@settings(max_examples=50)
def test_types::collectiontype_instantiation(instance):
    assert isinstance(instance, types::CollectionType)

@given(instance=types::ThisModuleType_strategy)
@settings(max_examples=50)
def test_types::thismoduletype_instantiation(instance):
    assert isinstance(instance, types::ThisModuleType)

@given(instance=types::EmptyCollectionType_strategy)
@settings(max_examples=50)
def test_types::emptycollectiontype_instantiation(instance):
    assert isinstance(instance, types::EmptyCollectionType)

@given(instance=types::PrimitiveType_strategy)
@settings(max_examples=50)
def test_types::primitivetype_instantiation(instance):
    assert isinstance(instance, types::PrimitiveType)

@given(instance=types::EmptyCollection_strategy)
@settings(max_examples=50)
def test_types::emptycollection_instantiation(instance):
    assert isinstance(instance, types::EmptyCollection)

@given(instance=types::OclUndefinedType_strategy)
@settings(max_examples=50)
def test_types::oclundefinedtype_instantiation(instance):
    assert isinstance(instance, types::OclUndefinedType)

@given(instance=types::Type_strategy)
@settings(max_examples=50)
def test_types::type_instantiation(instance):
    assert isinstance(instance, types::Type)

@given(instance=types::Type_strategy)
def test_types::type_multivalued_type(instance):
    assert isinstance(instance.multivalued, bool)


@given(instance=types::Type_strategy)
def test_types::type_multivalued_setter(instance):
    original = instance.multivalued
    instance.multivalued = original
    assert instance.multivalued == original

@given(instance=types::Type_strategy)
def test_types::type_mayBeUndefined_type(instance):
    assert isinstance(instance.mayBeUndefined, bool)


@given(instance=types::Type_strategy)
def test_types::type_mayBeUndefined_setter(instance):
    original = instance.mayBeUndefined
    instance.mayBeUndefined = original
    assert instance.mayBeUndefined == original

@given(instance=types::Type_strategy)
def test_types::type_metamodelRef_type(instance):
    assert isinstance(instance.metamodelRef, str)


@given(instance=types::Type_strategy)
def test_types::type_metamodelRef_setter(instance):
    original = instance.metamodelRef
    instance.metamodelRef = original
    assert instance.metamodelRef == original

@given(instance=types::Unknown_strategy)
@settings(max_examples=50)
def test_types::unknown_instantiation(instance):
    assert isinstance(instance, types::Unknown)

@given(instance=types::RefType_strategy)
@settings(max_examples=50)
def test_types::reftype_instantiation(instance):
    assert isinstance(instance, types::RefType)

@given(instance=types::MapType_strategy)
@settings(max_examples=50)
def test_types::maptype_instantiation(instance):
    assert isinstance(instance, types::MapType)

@given(instance=types::TupleAttribute_strategy)
@settings(max_examples=50)
def test_types::tupleattribute_instantiation(instance):
    assert isinstance(instance, types::TupleAttribute)

@given(instance=types::TupleAttribute_strategy)
def test_types::tupleattribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=types::TupleAttribute_strategy)
def test_types::tupleattribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=types::TupleType_strategy)
@settings(max_examples=50)
def test_types::tupletype_instantiation(instance):
    assert isinstance(instance, types::TupleType)

@given(instance=types::FloatType_strategy)
@settings(max_examples=50)
def test_types::floattype_instantiation(instance):
    assert isinstance(instance, types::FloatType)

@given(instance=types::StringType_strategy)
@settings(max_examples=50)
def test_types::stringtype_instantiation(instance):
    assert isinstance(instance, types::StringType)

@given(instance=types::IntegerType_strategy)
@settings(max_examples=50)
def test_types::integertype_instantiation(instance):
    assert isinstance(instance, types::IntegerType)
