import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    types_MetaModel,
    types_EClass,
    EStructuralFeature,
    types_UnknownFeature,
    Metaclass,
    TypeError,
    types_UnresolvedTypeError,
    types_EObject,
    RefType,
    CollectionType,
    types_SetType,
    types_OrderedSetType,
    types_BagType,
    types_SequenceType,
    ReflectiveType,
    types_ReflectiveClass,
    types_Metaclass,
    PrimitiveType,
    types_IntegerType,
    types_StringType,
    types_BooleanType,
    Type,
    types_ReflectiveType,
    types_ThisModuleType,
    types_UnionType,
    types_EnumType,
    types_EmptyCollectionType,
    types_EmptyCollection,
    types_TypeError,
    types_CollectionType,
    types_PrimitiveType,
    types_OclUndefinedType,
    types_Type,
    types_Unknown,
    types_RefType,
    types_MapType,
    types_TupleAttribute,
    types_TupleType,
    types_FloatType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_types_metamodel_is_not_abstract():
    assert not inspect.isabstract(types_MetaModel)


def test_types_metamodel_constructor_exists():
    assert callable(types_MetaModel.__init__)


def test_types_metamodel_constructor_args():
    sig = inspect.signature(types_MetaModel.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_types_metamodel_has_name():
    assert hasattr(types_MetaModel, "name")
    descriptor = None
    for klass in types_MetaModel.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_types_eclass_is_not_abstract():
    assert not inspect.isabstract(types_EClass)


def test_types_eclass_constructor_exists():
    assert callable(types_EClass.__init__)


def test_types_eclass_constructor_args():
    sig = inspect.signature(types_EClass.__init__)
    params = list(sig.parameters.keys())



def test_estructuralfeature_is_not_abstract():
    assert not inspect.isabstract(EStructuralFeature)


def test_estructuralfeature_constructor_exists():
    assert callable(EStructuralFeature.__init__)


def test_estructuralfeature_constructor_args():
    sig = inspect.signature(EStructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_types_unknownfeature_is_not_abstract():
    assert not inspect.isabstract(types_UnknownFeature)


def test_types_unknownfeature_constructor_exists():
    assert callable(types_UnknownFeature.__init__)


def test_types_unknownfeature_constructor_args():
    sig = inspect.signature(types_UnknownFeature.__init__)
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



def test_types_unresolvedtypeerror_is_not_abstract():
    assert not inspect.isabstract(types_UnresolvedTypeError)


def test_types_unresolvedtypeerror_constructor_exists():
    assert callable(types_UnresolvedTypeError.__init__)


def test_types_unresolvedtypeerror_constructor_args():
    sig = inspect.signature(types_UnresolvedTypeError.__init__)
    params = list(sig.parameters.keys())



def test_types_eobject_is_not_abstract():
    assert not inspect.isabstract(types_EObject)


def test_types_eobject_constructor_exists():
    assert callable(types_EObject.__init__)


def test_types_eobject_constructor_args():
    sig = inspect.signature(types_EObject.__init__)
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



def test_types_settype_is_not_abstract():
    assert not inspect.isabstract(types_SetType)


def test_types_settype_constructor_exists():
    assert callable(types_SetType.__init__)


def test_types_settype_constructor_args():
    sig = inspect.signature(types_SetType.__init__)
    params = list(sig.parameters.keys())



def test_types_orderedsettype_is_not_abstract():
    assert not inspect.isabstract(types_OrderedSetType)


def test_types_orderedsettype_constructor_exists():
    assert callable(types_OrderedSetType.__init__)


def test_types_orderedsettype_constructor_args():
    sig = inspect.signature(types_OrderedSetType.__init__)
    params = list(sig.parameters.keys())



def test_types_bagtype_is_not_abstract():
    assert not inspect.isabstract(types_BagType)


def test_types_bagtype_constructor_exists():
    assert callable(types_BagType.__init__)


def test_types_bagtype_constructor_args():
    sig = inspect.signature(types_BagType.__init__)
    params = list(sig.parameters.keys())



def test_types_sequencetype_is_not_abstract():
    assert not inspect.isabstract(types_SequenceType)


def test_types_sequencetype_constructor_exists():
    assert callable(types_SequenceType.__init__)


def test_types_sequencetype_constructor_args():
    sig = inspect.signature(types_SequenceType.__init__)
    params = list(sig.parameters.keys())



def test_reflectivetype_is_not_abstract():
    assert not inspect.isabstract(ReflectiveType)


def test_reflectivetype_constructor_exists():
    assert callable(ReflectiveType.__init__)


def test_reflectivetype_constructor_args():
    sig = inspect.signature(ReflectiveType.__init__)
    params = list(sig.parameters.keys())



def test_types_reflectiveclass_is_not_abstract():
    assert not inspect.isabstract(types_ReflectiveClass)


def test_types_reflectiveclass_constructor_exists():
    assert callable(types_ReflectiveClass.__init__)


def test_types_reflectiveclass_constructor_args():
    sig = inspect.signature(types_ReflectiveClass.__init__)
    params = list(sig.parameters.keys())



def test_types_metaclass_is_not_abstract():
    assert not inspect.isabstract(types_Metaclass)


def test_types_metaclass_constructor_exists():
    assert callable(types_Metaclass.__init__)


def test_types_metaclass_constructor_args():
    sig = inspect.signature(types_Metaclass.__init__)
    params = list(sig.parameters.keys())
    assert "explicitOcurrence" in params, "Missing parameter 'explicitOcurrence'"
    assert "name" in params, "Missing parameter 'name'"

def test_types_metaclass_has_explicitOcurrence():
    assert hasattr(types_Metaclass, "explicitOcurrence")
    descriptor = None
    for klass in types_Metaclass.__mro__:
        if "explicitOcurrence" in klass.__dict__:
            descriptor = klass.__dict__["explicitOcurrence"]
            break
    assert isinstance(descriptor, property)

def test_types_metaclass_has_name():
    assert hasattr(types_Metaclass, "name")
    descriptor = None
    for klass in types_Metaclass.__mro__:
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



def test_types_integertype_is_not_abstract():
    assert not inspect.isabstract(types_IntegerType)


def test_types_integertype_constructor_exists():
    assert callable(types_IntegerType.__init__)


def test_types_integertype_constructor_args():
    sig = inspect.signature(types_IntegerType.__init__)
    params = list(sig.parameters.keys())



def test_types_stringtype_is_not_abstract():
    assert not inspect.isabstract(types_StringType)


def test_types_stringtype_constructor_exists():
    assert callable(types_StringType.__init__)


def test_types_stringtype_constructor_args():
    sig = inspect.signature(types_StringType.__init__)
    params = list(sig.parameters.keys())



def test_types_booleantype_is_not_abstract():
    assert not inspect.isabstract(types_BooleanType)


def test_types_booleantype_constructor_exists():
    assert callable(types_BooleanType.__init__)


def test_types_booleantype_constructor_args():
    sig = inspect.signature(types_BooleanType.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_types_reflectivetype_is_not_abstract():
    assert not inspect.isabstract(types_ReflectiveType)


def test_types_reflectivetype_constructor_exists():
    assert callable(types_ReflectiveType.__init__)


def test_types_reflectivetype_constructor_args():
    sig = inspect.signature(types_ReflectiveType.__init__)
    params = list(sig.parameters.keys())



def test_types_thismoduletype_is_not_abstract():
    assert not inspect.isabstract(types_ThisModuleType)


def test_types_thismoduletype_constructor_exists():
    assert callable(types_ThisModuleType.__init__)


def test_types_thismoduletype_constructor_args():
    sig = inspect.signature(types_ThisModuleType.__init__)
    params = list(sig.parameters.keys())



def test_types_uniontype_is_not_abstract():
    assert not inspect.isabstract(types_UnionType)


def test_types_uniontype_constructor_exists():
    assert callable(types_UnionType.__init__)


def test_types_uniontype_constructor_args():
    sig = inspect.signature(types_UnionType.__init__)
    params = list(sig.parameters.keys())



def test_types_enumtype_is_not_abstract():
    assert not inspect.isabstract(types_EnumType)


def test_types_enumtype_constructor_exists():
    assert callable(types_EnumType.__init__)


def test_types_enumtype_constructor_args():
    sig = inspect.signature(types_EnumType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_types_enumtype_has_name():
    assert hasattr(types_EnumType, "name")
    descriptor = None
    for klass in types_EnumType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_types_emptycollectiontype_is_not_abstract():
    assert not inspect.isabstract(types_EmptyCollectionType)


def test_types_emptycollectiontype_constructor_exists():
    assert callable(types_EmptyCollectionType.__init__)


def test_types_emptycollectiontype_constructor_args():
    sig = inspect.signature(types_EmptyCollectionType.__init__)
    params = list(sig.parameters.keys())



def test_types_emptycollection_is_not_abstract():
    assert not inspect.isabstract(types_EmptyCollection)


def test_types_emptycollection_constructor_exists():
    assert callable(types_EmptyCollection.__init__)


def test_types_emptycollection_constructor_args():
    sig = inspect.signature(types_EmptyCollection.__init__)
    params = list(sig.parameters.keys())



def test_types_typeerror_is_not_abstract():
    assert not inspect.isabstract(types_TypeError)


def test_types_typeerror_constructor_exists():
    assert callable(types_TypeError.__init__)


def test_types_typeerror_constructor_args():
    sig = inspect.signature(types_TypeError.__init__)
    params = list(sig.parameters.keys())



def test_types_collectiontype_is_not_abstract():
    assert not inspect.isabstract(types_CollectionType)


def test_types_collectiontype_constructor_exists():
    assert callable(types_CollectionType.__init__)


def test_types_collectiontype_constructor_args():
    sig = inspect.signature(types_CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_types_primitivetype_is_not_abstract():
    assert not inspect.isabstract(types_PrimitiveType)


def test_types_primitivetype_constructor_exists():
    assert callable(types_PrimitiveType.__init__)


def test_types_primitivetype_constructor_args():
    sig = inspect.signature(types_PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_types_oclundefinedtype_is_not_abstract():
    assert not inspect.isabstract(types_OclUndefinedType)


def test_types_oclundefinedtype_constructor_exists():
    assert callable(types_OclUndefinedType.__init__)


def test_types_oclundefinedtype_constructor_args():
    sig = inspect.signature(types_OclUndefinedType.__init__)
    params = list(sig.parameters.keys())



def test_types_type_is_not_abstract():
    assert not inspect.isabstract(types_Type)


def test_types_type_constructor_exists():
    assert callable(types_Type.__init__)


def test_types_type_constructor_args():
    sig = inspect.signature(types_Type.__init__)
    params = list(sig.parameters.keys())
    assert "multivalued" in params, "Missing parameter 'multivalued'"
    assert "metamodelRef" in params, "Missing parameter 'metamodelRef'"
    assert "mayBeUndefined" in params, "Missing parameter 'mayBeUndefined'"

def test_types_type_has_multivalued():
    assert hasattr(types_Type, "multivalued")
    descriptor = None
    for klass in types_Type.__mro__:
        if "multivalued" in klass.__dict__:
            descriptor = klass.__dict__["multivalued"]
            break
    assert isinstance(descriptor, property)

def test_types_type_has_metamodelRef():
    assert hasattr(types_Type, "metamodelRef")
    descriptor = None
    for klass in types_Type.__mro__:
        if "metamodelRef" in klass.__dict__:
            descriptor = klass.__dict__["metamodelRef"]
            break
    assert isinstance(descriptor, property)

def test_types_type_has_mayBeUndefined():
    assert hasattr(types_Type, "mayBeUndefined")
    descriptor = None
    for klass in types_Type.__mro__:
        if "mayBeUndefined" in klass.__dict__:
            descriptor = klass.__dict__["mayBeUndefined"]
            break
    assert isinstance(descriptor, property)



def test_types_unknown_is_not_abstract():
    assert not inspect.isabstract(types_Unknown)


def test_types_unknown_constructor_exists():
    assert callable(types_Unknown.__init__)


def test_types_unknown_constructor_args():
    sig = inspect.signature(types_Unknown.__init__)
    params = list(sig.parameters.keys())



def test_types_reftype_is_not_abstract():
    assert not inspect.isabstract(types_RefType)


def test_types_reftype_constructor_exists():
    assert callable(types_RefType.__init__)


def test_types_reftype_constructor_args():
    sig = inspect.signature(types_RefType.__init__)
    params = list(sig.parameters.keys())



def test_types_maptype_is_not_abstract():
    assert not inspect.isabstract(types_MapType)


def test_types_maptype_constructor_exists():
    assert callable(types_MapType.__init__)


def test_types_maptype_constructor_args():
    sig = inspect.signature(types_MapType.__init__)
    params = list(sig.parameters.keys())



def test_types_tupleattribute_is_not_abstract():
    assert not inspect.isabstract(types_TupleAttribute)


def test_types_tupleattribute_constructor_exists():
    assert callable(types_TupleAttribute.__init__)


def test_types_tupleattribute_constructor_args():
    sig = inspect.signature(types_TupleAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_types_tupleattribute_has_name():
    assert hasattr(types_TupleAttribute, "name")
    descriptor = None
    for klass in types_TupleAttribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_types_tupletype_is_not_abstract():
    assert not inspect.isabstract(types_TupleType)


def test_types_tupletype_constructor_exists():
    assert callable(types_TupleType.__init__)


def test_types_tupletype_constructor_args():
    sig = inspect.signature(types_TupleType.__init__)
    params = list(sig.parameters.keys())



def test_types_floattype_is_not_abstract():
    assert not inspect.isabstract(types_FloatType)


def test_types_floattype_constructor_exists():
    assert callable(types_FloatType.__init__)


def test_types_floattype_constructor_args():
    sig = inspect.signature(types_FloatType.__init__)
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
types_MetaModel_strategy = st.builds(
    types_MetaModel,
    name=
        safe_text
)
types_EClass_strategy = st.builds(
    types_EClass,
)
EStructuralFeature_strategy = st.builds(
    EStructuralFeature,
)
types_UnknownFeature_strategy = st.builds(
    types_UnknownFeature,
)
Metaclass_strategy = st.builds(
    Metaclass,
)
TypeError_strategy = st.builds(
    TypeError,
)
types_UnresolvedTypeError_strategy = st.builds(
    types_UnresolvedTypeError,
)
types_EObject_strategy = st.builds(
    types_EObject,
)
RefType_strategy = st.builds(
    RefType,
)
CollectionType_strategy = st.builds(
    CollectionType,
)
types_SetType_strategy = st.builds(
    types_SetType,
)
types_OrderedSetType_strategy = st.builds(
    types_OrderedSetType,
)
types_BagType_strategy = st.builds(
    types_BagType,
)
types_SequenceType_strategy = st.builds(
    types_SequenceType,
)
ReflectiveType_strategy = st.builds(
    ReflectiveType,
)
types_ReflectiveClass_strategy = st.builds(
    types_ReflectiveClass,
)
types_Metaclass_strategy = st.builds(
    types_Metaclass,
    explicitOcurrence=
        st.booleans(),
    name=
        safe_text
)
PrimitiveType_strategy = st.builds(
    PrimitiveType,
)
types_IntegerType_strategy = st.builds(
    types_IntegerType,
)
types_StringType_strategy = st.builds(
    types_StringType,
)
types_BooleanType_strategy = st.builds(
    types_BooleanType,
)
Type_strategy = st.builds(
    Type,
)
types_ReflectiveType_strategy = st.builds(
    types_ReflectiveType,
)
types_ThisModuleType_strategy = st.builds(
    types_ThisModuleType,
)
types_UnionType_strategy = st.builds(
    types_UnionType,
)
types_EnumType_strategy = st.builds(
    types_EnumType,
    name=
        safe_text
)
types_EmptyCollectionType_strategy = st.builds(
    types_EmptyCollectionType,
)
types_EmptyCollection_strategy = st.builds(
    types_EmptyCollection,
)
types_TypeError_strategy = st.builds(
    types_TypeError,
)
types_CollectionType_strategy = st.builds(
    types_CollectionType,
)
types_PrimitiveType_strategy = st.builds(
    types_PrimitiveType,
)
types_OclUndefinedType_strategy = st.builds(
    types_OclUndefinedType,
)
types_Type_strategy = st.builds(
    types_Type,
    multivalued=
        st.booleans(),
    metamodelRef=
        safe_text,
    mayBeUndefined=
        st.booleans()
)
types_Unknown_strategy = st.builds(
    types_Unknown,
)
types_RefType_strategy = st.builds(
    types_RefType,
)
types_MapType_strategy = st.builds(
    types_MapType,
)
types_TupleAttribute_strategy = st.builds(
    types_TupleAttribute,
    name=
        safe_text
)
types_TupleType_strategy = st.builds(
    types_TupleType,
)
types_FloatType_strategy = st.builds(
    types_FloatType,
)

@given(instance=types_MetaModel_strategy)
@settings(max_examples=50)
def test_types_metamodel_instantiation(instance):
    assert isinstance(instance, types_MetaModel)



@given(instance=types_MetaModel_strategy)
def test_types_metamodel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=types_EClass_strategy)
@settings(max_examples=50)
def test_types_eclass_instantiation(instance):
    assert isinstance(instance, types_EClass)

@given(instance=EStructuralFeature_strategy)
@settings(max_examples=50)
def test_estructuralfeature_instantiation(instance):
    assert isinstance(instance, EStructuralFeature)

@given(instance=types_UnknownFeature_strategy)
@settings(max_examples=50)
def test_types_unknownfeature_instantiation(instance):
    assert isinstance(instance, types_UnknownFeature)

@given(instance=Metaclass_strategy)
@settings(max_examples=50)
def test_metaclass_instantiation(instance):
    assert isinstance(instance, Metaclass)

@given(instance=TypeError_strategy)
@settings(max_examples=50)
def test_typeerror_instantiation(instance):
    assert isinstance(instance, TypeError)

@given(instance=types_UnresolvedTypeError_strategy)
@settings(max_examples=50)
def test_types_unresolvedtypeerror_instantiation(instance):
    assert isinstance(instance, types_UnresolvedTypeError)

@given(instance=types_EObject_strategy)
@settings(max_examples=50)
def test_types_eobject_instantiation(instance):
    assert isinstance(instance, types_EObject)

@given(instance=RefType_strategy)
@settings(max_examples=50)
def test_reftype_instantiation(instance):
    assert isinstance(instance, RefType)

@given(instance=CollectionType_strategy)
@settings(max_examples=50)
def test_collectiontype_instantiation(instance):
    assert isinstance(instance, CollectionType)

@given(instance=types_SetType_strategy)
@settings(max_examples=50)
def test_types_settype_instantiation(instance):
    assert isinstance(instance, types_SetType)

@given(instance=types_OrderedSetType_strategy)
@settings(max_examples=50)
def test_types_orderedsettype_instantiation(instance):
    assert isinstance(instance, types_OrderedSetType)

@given(instance=types_BagType_strategy)
@settings(max_examples=50)
def test_types_bagtype_instantiation(instance):
    assert isinstance(instance, types_BagType)

@given(instance=types_SequenceType_strategy)
@settings(max_examples=50)
def test_types_sequencetype_instantiation(instance):
    assert isinstance(instance, types_SequenceType)

@given(instance=ReflectiveType_strategy)
@settings(max_examples=50)
def test_reflectivetype_instantiation(instance):
    assert isinstance(instance, ReflectiveType)

@given(instance=types_ReflectiveClass_strategy)
@settings(max_examples=50)
def test_types_reflectiveclass_instantiation(instance):
    assert isinstance(instance, types_ReflectiveClass)

@given(instance=types_Metaclass_strategy)
@settings(max_examples=50)
def test_types_metaclass_instantiation(instance):
    assert isinstance(instance, types_Metaclass)



@given(instance=types_Metaclass_strategy)
def test_types_metaclass_explicitOcurrence_setter(instance):
    original = instance.explicitOcurrence
    instance.explicitOcurrence = original
    assert instance.explicitOcurrence == original



@given(instance=types_Metaclass_strategy)
def test_types_metaclass_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=PrimitiveType_strategy)
@settings(max_examples=50)
def test_primitivetype_instantiation(instance):
    assert isinstance(instance, PrimitiveType)

@given(instance=types_IntegerType_strategy)
@settings(max_examples=50)
def test_types_integertype_instantiation(instance):
    assert isinstance(instance, types_IntegerType)

@given(instance=types_StringType_strategy)
@settings(max_examples=50)
def test_types_stringtype_instantiation(instance):
    assert isinstance(instance, types_StringType)

@given(instance=types_BooleanType_strategy)
@settings(max_examples=50)
def test_types_booleantype_instantiation(instance):
    assert isinstance(instance, types_BooleanType)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=types_ReflectiveType_strategy)
@settings(max_examples=50)
def test_types_reflectivetype_instantiation(instance):
    assert isinstance(instance, types_ReflectiveType)

@given(instance=types_ThisModuleType_strategy)
@settings(max_examples=50)
def test_types_thismoduletype_instantiation(instance):
    assert isinstance(instance, types_ThisModuleType)

@given(instance=types_UnionType_strategy)
@settings(max_examples=50)
def test_types_uniontype_instantiation(instance):
    assert isinstance(instance, types_UnionType)

@given(instance=types_EnumType_strategy)
@settings(max_examples=50)
def test_types_enumtype_instantiation(instance):
    assert isinstance(instance, types_EnumType)



@given(instance=types_EnumType_strategy)
def test_types_enumtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=types_EmptyCollectionType_strategy)
@settings(max_examples=50)
def test_types_emptycollectiontype_instantiation(instance):
    assert isinstance(instance, types_EmptyCollectionType)

@given(instance=types_EmptyCollection_strategy)
@settings(max_examples=50)
def test_types_emptycollection_instantiation(instance):
    assert isinstance(instance, types_EmptyCollection)

@given(instance=types_TypeError_strategy)
@settings(max_examples=50)
def test_types_typeerror_instantiation(instance):
    assert isinstance(instance, types_TypeError)

@given(instance=types_CollectionType_strategy)
@settings(max_examples=50)
def test_types_collectiontype_instantiation(instance):
    assert isinstance(instance, types_CollectionType)

@given(instance=types_PrimitiveType_strategy)
@settings(max_examples=50)
def test_types_primitivetype_instantiation(instance):
    assert isinstance(instance, types_PrimitiveType)

@given(instance=types_OclUndefinedType_strategy)
@settings(max_examples=50)
def test_types_oclundefinedtype_instantiation(instance):
    assert isinstance(instance, types_OclUndefinedType)

@given(instance=types_Type_strategy)
@settings(max_examples=50)
def test_types_type_instantiation(instance):
    assert isinstance(instance, types_Type)



@given(instance=types_Type_strategy)
def test_types_type_multivalued_setter(instance):
    original = instance.multivalued
    instance.multivalued = original
    assert instance.multivalued == original



@given(instance=types_Type_strategy)
def test_types_type_metamodelRef_setter(instance):
    original = instance.metamodelRef
    instance.metamodelRef = original
    assert instance.metamodelRef == original



@given(instance=types_Type_strategy)
def test_types_type_mayBeUndefined_setter(instance):
    original = instance.mayBeUndefined
    instance.mayBeUndefined = original
    assert instance.mayBeUndefined == original

@given(instance=types_Unknown_strategy)
@settings(max_examples=50)
def test_types_unknown_instantiation(instance):
    assert isinstance(instance, types_Unknown)

@given(instance=types_RefType_strategy)
@settings(max_examples=50)
def test_types_reftype_instantiation(instance):
    assert isinstance(instance, types_RefType)

@given(instance=types_MapType_strategy)
@settings(max_examples=50)
def test_types_maptype_instantiation(instance):
    assert isinstance(instance, types_MapType)

@given(instance=types_TupleAttribute_strategy)
@settings(max_examples=50)
def test_types_tupleattribute_instantiation(instance):
    assert isinstance(instance, types_TupleAttribute)



@given(instance=types_TupleAttribute_strategy)
def test_types_tupleattribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=types_TupleType_strategy)
@settings(max_examples=50)
def test_types_tupletype_instantiation(instance):
    assert isinstance(instance, types_TupleType)

@given(instance=types_FloatType_strategy)
@settings(max_examples=50)
def test_types_floattype_instantiation(instance):
    assert isinstance(instance, types_FloatType)
