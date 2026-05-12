import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    annotations_atl_types_Type,
    annotations_atl_types_EObject,
    AtlAnnotation,
    atl_types_annotations_ExpressionAnnotation,
    atl_types_annotations_BindingAnnotation,
    atl_types_annotations_HelperAnnotation,
    atl_types_annotations_AtlAnnotation,
    ReflectiveType,
    atl_types_ReflectiveClass,
    PrimitiveType,
    atl_types_IntegerType,
    atl_types_BooleanType,
    Type,
    atl_types_PrimitiveType,
    atl_types_Type,
    atl_types_EObject,
    atl_types_EnumType,
    atl_types_EmptyCollection,
    RefType,
    atl_types_Metaclass,
    atl_types_Unknown,
    atl_types_RefType,
    atl_types_MapType,
    atl_types_TupleAttribute,
    atl_types_TupleType,
    atl_types_FloatType,
    atl_types_StringType,
    atl_types_ThisModuleType,
    atl_types_UnionType,
    atl_types_ReflectiveType,
    atl_types_EClass,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_annotations_atl_types_type_is_not_abstract():
    assert not inspect.isabstract(annotations_atl_types_Type)


def test_annotations_atl_types_type_constructor_exists():
    assert callable(annotations_atl_types_Type.__init__)


def test_annotations_atl_types_type_constructor_args():
    sig = inspect.signature(annotations_atl_types_Type.__init__)
    params = list(sig.parameters.keys())



def test_annotations_atl_types_eobject_is_not_abstract():
    assert not inspect.isabstract(annotations_atl_types_EObject)


def test_annotations_atl_types_eobject_constructor_exists():
    assert callable(annotations_atl_types_EObject.__init__)


def test_annotations_atl_types_eobject_constructor_args():
    sig = inspect.signature(annotations_atl_types_EObject.__init__)
    params = list(sig.parameters.keys())



def test_atlannotation_is_not_abstract():
    assert not inspect.isabstract(AtlAnnotation)


def test_atlannotation_constructor_exists():
    assert callable(AtlAnnotation.__init__)


def test_atlannotation_constructor_args():
    sig = inspect.signature(AtlAnnotation.__init__)
    params = list(sig.parameters.keys())



def test_atl_types_annotations_expressionannotation_is_not_abstract():
    assert not inspect.isabstract(atl_types_annotations_ExpressionAnnotation)


def test_atl_types_annotations_expressionannotation_constructor_exists():
    assert callable(atl_types_annotations_ExpressionAnnotation.__init__)


def test_atl_types_annotations_expressionannotation_constructor_args():
    sig = inspect.signature(atl_types_annotations_ExpressionAnnotation.__init__)
    params = list(sig.parameters.keys())



def test_atl_types_annotations_bindingannotation_is_not_abstract():
    assert not inspect.isabstract(atl_types_annotations_BindingAnnotation)


def test_atl_types_annotations_bindingannotation_constructor_exists():
    assert callable(atl_types_annotations_BindingAnnotation.__init__)


def test_atl_types_annotations_bindingannotation_constructor_args():
    sig = inspect.signature(atl_types_annotations_BindingAnnotation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_atl_types_annotations_bindingannotation_has_name():
    assert hasattr(atl_types_annotations_BindingAnnotation, "name")
    descriptor = None
    for klass in atl_types_annotations_BindingAnnotation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_atl_types_annotations_helperannotation_is_not_abstract():
    assert not inspect.isabstract(atl_types_annotations_HelperAnnotation)


def test_atl_types_annotations_helperannotation_constructor_exists():
    assert callable(atl_types_annotations_HelperAnnotation.__init__)


def test_atl_types_annotations_helperannotation_constructor_args():
    sig = inspect.signature(atl_types_annotations_HelperAnnotation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_atl_types_annotations_helperannotation_has_name():
    assert hasattr(atl_types_annotations_HelperAnnotation, "name")
    descriptor = None
    for klass in atl_types_annotations_HelperAnnotation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_atl_types_annotations_atlannotation_is_not_abstract():
    assert not inspect.isabstract(atl_types_annotations_AtlAnnotation)


def test_atl_types_annotations_atlannotation_constructor_exists():
    assert callable(atl_types_annotations_AtlAnnotation.__init__)


def test_atl_types_annotations_atlannotation_constructor_args():
    sig = inspect.signature(atl_types_annotations_AtlAnnotation.__init__)
    params = list(sig.parameters.keys())



def test_reflectivetype_is_not_abstract():
    assert not inspect.isabstract(ReflectiveType)


def test_reflectivetype_constructor_exists():
    assert callable(ReflectiveType.__init__)


def test_reflectivetype_constructor_args():
    sig = inspect.signature(ReflectiveType.__init__)
    params = list(sig.parameters.keys())



def test_atl_types_reflectiveclass_is_not_abstract():
    assert not inspect.isabstract(atl_types_ReflectiveClass)


def test_atl_types_reflectiveclass_constructor_exists():
    assert callable(atl_types_ReflectiveClass.__init__)


def test_atl_types_reflectiveclass_constructor_args():
    sig = inspect.signature(atl_types_ReflectiveClass.__init__)
    params = list(sig.parameters.keys())



def test_primitivetype_is_not_abstract():
    assert not inspect.isabstract(PrimitiveType)


def test_primitivetype_constructor_exists():
    assert callable(PrimitiveType.__init__)


def test_primitivetype_constructor_args():
    sig = inspect.signature(PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_atl_types_integertype_is_not_abstract():
    assert not inspect.isabstract(atl_types_IntegerType)


def test_atl_types_integertype_constructor_exists():
    assert callable(atl_types_IntegerType.__init__)


def test_atl_types_integertype_constructor_args():
    sig = inspect.signature(atl_types_IntegerType.__init__)
    params = list(sig.parameters.keys())



def test_atl_types_booleantype_is_not_abstract():
    assert not inspect.isabstract(atl_types_BooleanType)


def test_atl_types_booleantype_constructor_exists():
    assert callable(atl_types_BooleanType.__init__)


def test_atl_types_booleantype_constructor_args():
    sig = inspect.signature(atl_types_BooleanType.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_atl_types_primitivetype_is_not_abstract():
    assert not inspect.isabstract(atl_types_PrimitiveType)


def test_atl_types_primitivetype_constructor_exists():
    assert callable(atl_types_PrimitiveType.__init__)


def test_atl_types_primitivetype_constructor_args():
    sig = inspect.signature(atl_types_PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_atl_types_type_is_not_abstract():
    assert not inspect.isabstract(atl_types_Type)


def test_atl_types_type_constructor_exists():
    assert callable(atl_types_Type.__init__)


def test_atl_types_type_constructor_args():
    sig = inspect.signature(atl_types_Type.__init__)
    params = list(sig.parameters.keys())
    assert "multivalued" in params, "Missing parameter 'multivalued'"

def test_atl_types_type_has_multivalued():
    assert hasattr(atl_types_Type, "multivalued")
    descriptor = None
    for klass in atl_types_Type.__mro__:
        if "multivalued" in klass.__dict__:
            descriptor = klass.__dict__["multivalued"]
            break
    assert isinstance(descriptor, property)



def test_atl_types_eobject_is_not_abstract():
    assert not inspect.isabstract(atl_types_EObject)


def test_atl_types_eobject_constructor_exists():
    assert callable(atl_types_EObject.__init__)


def test_atl_types_eobject_constructor_args():
    sig = inspect.signature(atl_types_EObject.__init__)
    params = list(sig.parameters.keys())



def test_atl_types_enumtype_is_not_abstract():
    assert not inspect.isabstract(atl_types_EnumType)


def test_atl_types_enumtype_constructor_exists():
    assert callable(atl_types_EnumType.__init__)


def test_atl_types_enumtype_constructor_args():
    sig = inspect.signature(atl_types_EnumType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_atl_types_enumtype_has_name():
    assert hasattr(atl_types_EnumType, "name")
    descriptor = None
    for klass in atl_types_EnumType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_atl_types_emptycollection_is_not_abstract():
    assert not inspect.isabstract(atl_types_EmptyCollection)


def test_atl_types_emptycollection_constructor_exists():
    assert callable(atl_types_EmptyCollection.__init__)


def test_atl_types_emptycollection_constructor_args():
    sig = inspect.signature(atl_types_EmptyCollection.__init__)
    params = list(sig.parameters.keys())



def test_reftype_is_not_abstract():
    assert not inspect.isabstract(RefType)


def test_reftype_constructor_exists():
    assert callable(RefType.__init__)


def test_reftype_constructor_args():
    sig = inspect.signature(RefType.__init__)
    params = list(sig.parameters.keys())



def test_atl_types_metaclass_is_not_abstract():
    assert not inspect.isabstract(atl_types_Metaclass)


def test_atl_types_metaclass_constructor_exists():
    assert callable(atl_types_Metaclass.__init__)


def test_atl_types_metaclass_constructor_args():
    sig = inspect.signature(atl_types_Metaclass.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_atl_types_metaclass_has_name():
    assert hasattr(atl_types_Metaclass, "name")
    descriptor = None
    for klass in atl_types_Metaclass.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_atl_types_unknown_is_not_abstract():
    assert not inspect.isabstract(atl_types_Unknown)


def test_atl_types_unknown_constructor_exists():
    assert callable(atl_types_Unknown.__init__)


def test_atl_types_unknown_constructor_args():
    sig = inspect.signature(atl_types_Unknown.__init__)
    params = list(sig.parameters.keys())



def test_atl_types_reftype_is_not_abstract():
    assert not inspect.isabstract(atl_types_RefType)


def test_atl_types_reftype_constructor_exists():
    assert callable(atl_types_RefType.__init__)


def test_atl_types_reftype_constructor_args():
    sig = inspect.signature(atl_types_RefType.__init__)
    params = list(sig.parameters.keys())



def test_atl_types_maptype_is_not_abstract():
    assert not inspect.isabstract(atl_types_MapType)


def test_atl_types_maptype_constructor_exists():
    assert callable(atl_types_MapType.__init__)


def test_atl_types_maptype_constructor_args():
    sig = inspect.signature(atl_types_MapType.__init__)
    params = list(sig.parameters.keys())



def test_atl_types_tupleattribute_is_not_abstract():
    assert not inspect.isabstract(atl_types_TupleAttribute)


def test_atl_types_tupleattribute_constructor_exists():
    assert callable(atl_types_TupleAttribute.__init__)


def test_atl_types_tupleattribute_constructor_args():
    sig = inspect.signature(atl_types_TupleAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_atl_types_tupleattribute_has_name():
    assert hasattr(atl_types_TupleAttribute, "name")
    descriptor = None
    for klass in atl_types_TupleAttribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_atl_types_tupletype_is_not_abstract():
    assert not inspect.isabstract(atl_types_TupleType)


def test_atl_types_tupletype_constructor_exists():
    assert callable(atl_types_TupleType.__init__)


def test_atl_types_tupletype_constructor_args():
    sig = inspect.signature(atl_types_TupleType.__init__)
    params = list(sig.parameters.keys())



def test_atl_types_floattype_is_not_abstract():
    assert not inspect.isabstract(atl_types_FloatType)


def test_atl_types_floattype_constructor_exists():
    assert callable(atl_types_FloatType.__init__)


def test_atl_types_floattype_constructor_args():
    sig = inspect.signature(atl_types_FloatType.__init__)
    params = list(sig.parameters.keys())



def test_atl_types_stringtype_is_not_abstract():
    assert not inspect.isabstract(atl_types_StringType)


def test_atl_types_stringtype_constructor_exists():
    assert callable(atl_types_StringType.__init__)


def test_atl_types_stringtype_constructor_args():
    sig = inspect.signature(atl_types_StringType.__init__)
    params = list(sig.parameters.keys())



def test_atl_types_thismoduletype_is_not_abstract():
    assert not inspect.isabstract(atl_types_ThisModuleType)


def test_atl_types_thismoduletype_constructor_exists():
    assert callable(atl_types_ThisModuleType.__init__)


def test_atl_types_thismoduletype_constructor_args():
    sig = inspect.signature(atl_types_ThisModuleType.__init__)
    params = list(sig.parameters.keys())



def test_atl_types_uniontype_is_not_abstract():
    assert not inspect.isabstract(atl_types_UnionType)


def test_atl_types_uniontype_constructor_exists():
    assert callable(atl_types_UnionType.__init__)


def test_atl_types_uniontype_constructor_args():
    sig = inspect.signature(atl_types_UnionType.__init__)
    params = list(sig.parameters.keys())



def test_atl_types_reflectivetype_is_not_abstract():
    assert not inspect.isabstract(atl_types_ReflectiveType)


def test_atl_types_reflectivetype_constructor_exists():
    assert callable(atl_types_ReflectiveType.__init__)


def test_atl_types_reflectivetype_constructor_args():
    sig = inspect.signature(atl_types_ReflectiveType.__init__)
    params = list(sig.parameters.keys())



def test_atl_types_eclass_is_not_abstract():
    assert not inspect.isabstract(atl_types_EClass)


def test_atl_types_eclass_constructor_exists():
    assert callable(atl_types_EClass.__init__)


def test_atl_types_eclass_constructor_args():
    sig = inspect.signature(atl_types_EClass.__init__)
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
annotations_atl_types_Type_strategy = st.builds(
    annotations_atl_types_Type,
)
annotations_atl_types_EObject_strategy = st.builds(
    annotations_atl_types_EObject,
)
AtlAnnotation_strategy = st.builds(
    AtlAnnotation,
)
atl_types_annotations_ExpressionAnnotation_strategy = st.builds(
    atl_types_annotations_ExpressionAnnotation,
)
atl_types_annotations_BindingAnnotation_strategy = st.builds(
    atl_types_annotations_BindingAnnotation,
    name=
        safe_text
)
atl_types_annotations_HelperAnnotation_strategy = st.builds(
    atl_types_annotations_HelperAnnotation,
    name=
        safe_text
)
atl_types_annotations_AtlAnnotation_strategy = st.builds(
    atl_types_annotations_AtlAnnotation,
)
ReflectiveType_strategy = st.builds(
    ReflectiveType,
)
atl_types_ReflectiveClass_strategy = st.builds(
    atl_types_ReflectiveClass,
)
PrimitiveType_strategy = st.builds(
    PrimitiveType,
)
atl_types_IntegerType_strategy = st.builds(
    atl_types_IntegerType,
)
atl_types_BooleanType_strategy = st.builds(
    atl_types_BooleanType,
)
Type_strategy = st.builds(
    Type,
)
atl_types_PrimitiveType_strategy = st.builds(
    atl_types_PrimitiveType,
)
atl_types_Type_strategy = st.builds(
    atl_types_Type,
    multivalued=
        st.booleans()
)
atl_types_EObject_strategy = st.builds(
    atl_types_EObject,
)
atl_types_EnumType_strategy = st.builds(
    atl_types_EnumType,
    name=
        safe_text
)
atl_types_EmptyCollection_strategy = st.builds(
    atl_types_EmptyCollection,
)
RefType_strategy = st.builds(
    RefType,
)
atl_types_Metaclass_strategy = st.builds(
    atl_types_Metaclass,
    name=
        safe_text
)
atl_types_Unknown_strategy = st.builds(
    atl_types_Unknown,
)
atl_types_RefType_strategy = st.builds(
    atl_types_RefType,
)
atl_types_MapType_strategy = st.builds(
    atl_types_MapType,
)
atl_types_TupleAttribute_strategy = st.builds(
    atl_types_TupleAttribute,
    name=
        safe_text
)
atl_types_TupleType_strategy = st.builds(
    atl_types_TupleType,
)
atl_types_FloatType_strategy = st.builds(
    atl_types_FloatType,
)
atl_types_StringType_strategy = st.builds(
    atl_types_StringType,
)
atl_types_ThisModuleType_strategy = st.builds(
    atl_types_ThisModuleType,
)
atl_types_UnionType_strategy = st.builds(
    atl_types_UnionType,
)
atl_types_ReflectiveType_strategy = st.builds(
    atl_types_ReflectiveType,
)
atl_types_EClass_strategy = st.builds(
    atl_types_EClass,
)

@given(instance=annotations_atl_types_Type_strategy)
@settings(max_examples=50)
def test_annotations_atl_types_type_instantiation(instance):
    assert isinstance(instance, annotations_atl_types_Type)

@given(instance=annotations_atl_types_EObject_strategy)
@settings(max_examples=50)
def test_annotations_atl_types_eobject_instantiation(instance):
    assert isinstance(instance, annotations_atl_types_EObject)

@given(instance=AtlAnnotation_strategy)
@settings(max_examples=50)
def test_atlannotation_instantiation(instance):
    assert isinstance(instance, AtlAnnotation)

@given(instance=atl_types_annotations_ExpressionAnnotation_strategy)
@settings(max_examples=50)
def test_atl_types_annotations_expressionannotation_instantiation(instance):
    assert isinstance(instance, atl_types_annotations_ExpressionAnnotation)

@given(instance=atl_types_annotations_BindingAnnotation_strategy)
@settings(max_examples=50)
def test_atl_types_annotations_bindingannotation_instantiation(instance):
    assert isinstance(instance, atl_types_annotations_BindingAnnotation)



@given(instance=atl_types_annotations_BindingAnnotation_strategy)
def test_atl_types_annotations_bindingannotation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=atl_types_annotations_HelperAnnotation_strategy)
@settings(max_examples=50)
def test_atl_types_annotations_helperannotation_instantiation(instance):
    assert isinstance(instance, atl_types_annotations_HelperAnnotation)



@given(instance=atl_types_annotations_HelperAnnotation_strategy)
def test_atl_types_annotations_helperannotation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=atl_types_annotations_AtlAnnotation_strategy)
@settings(max_examples=50)
def test_atl_types_annotations_atlannotation_instantiation(instance):
    assert isinstance(instance, atl_types_annotations_AtlAnnotation)

@given(instance=ReflectiveType_strategy)
@settings(max_examples=50)
def test_reflectivetype_instantiation(instance):
    assert isinstance(instance, ReflectiveType)

@given(instance=atl_types_ReflectiveClass_strategy)
@settings(max_examples=50)
def test_atl_types_reflectiveclass_instantiation(instance):
    assert isinstance(instance, atl_types_ReflectiveClass)

@given(instance=PrimitiveType_strategy)
@settings(max_examples=50)
def test_primitivetype_instantiation(instance):
    assert isinstance(instance, PrimitiveType)

@given(instance=atl_types_IntegerType_strategy)
@settings(max_examples=50)
def test_atl_types_integertype_instantiation(instance):
    assert isinstance(instance, atl_types_IntegerType)

@given(instance=atl_types_BooleanType_strategy)
@settings(max_examples=50)
def test_atl_types_booleantype_instantiation(instance):
    assert isinstance(instance, atl_types_BooleanType)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=atl_types_PrimitiveType_strategy)
@settings(max_examples=50)
def test_atl_types_primitivetype_instantiation(instance):
    assert isinstance(instance, atl_types_PrimitiveType)

@given(instance=atl_types_Type_strategy)
@settings(max_examples=50)
def test_atl_types_type_instantiation(instance):
    assert isinstance(instance, atl_types_Type)



@given(instance=atl_types_Type_strategy)
def test_atl_types_type_multivalued_setter(instance):
    original = instance.multivalued
    instance.multivalued = original
    assert instance.multivalued == original

@given(instance=atl_types_EObject_strategy)
@settings(max_examples=50)
def test_atl_types_eobject_instantiation(instance):
    assert isinstance(instance, atl_types_EObject)

@given(instance=atl_types_EnumType_strategy)
@settings(max_examples=50)
def test_atl_types_enumtype_instantiation(instance):
    assert isinstance(instance, atl_types_EnumType)



@given(instance=atl_types_EnumType_strategy)
def test_atl_types_enumtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=atl_types_EmptyCollection_strategy)
@settings(max_examples=50)
def test_atl_types_emptycollection_instantiation(instance):
    assert isinstance(instance, atl_types_EmptyCollection)

@given(instance=RefType_strategy)
@settings(max_examples=50)
def test_reftype_instantiation(instance):
    assert isinstance(instance, RefType)

@given(instance=atl_types_Metaclass_strategy)
@settings(max_examples=50)
def test_atl_types_metaclass_instantiation(instance):
    assert isinstance(instance, atl_types_Metaclass)



@given(instance=atl_types_Metaclass_strategy)
def test_atl_types_metaclass_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=atl_types_Unknown_strategy)
@settings(max_examples=50)
def test_atl_types_unknown_instantiation(instance):
    assert isinstance(instance, atl_types_Unknown)

@given(instance=atl_types_RefType_strategy)
@settings(max_examples=50)
def test_atl_types_reftype_instantiation(instance):
    assert isinstance(instance, atl_types_RefType)

@given(instance=atl_types_MapType_strategy)
@settings(max_examples=50)
def test_atl_types_maptype_instantiation(instance):
    assert isinstance(instance, atl_types_MapType)

@given(instance=atl_types_TupleAttribute_strategy)
@settings(max_examples=50)
def test_atl_types_tupleattribute_instantiation(instance):
    assert isinstance(instance, atl_types_TupleAttribute)



@given(instance=atl_types_TupleAttribute_strategy)
def test_atl_types_tupleattribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=atl_types_TupleType_strategy)
@settings(max_examples=50)
def test_atl_types_tupletype_instantiation(instance):
    assert isinstance(instance, atl_types_TupleType)

@given(instance=atl_types_FloatType_strategy)
@settings(max_examples=50)
def test_atl_types_floattype_instantiation(instance):
    assert isinstance(instance, atl_types_FloatType)

@given(instance=atl_types_StringType_strategy)
@settings(max_examples=50)
def test_atl_types_stringtype_instantiation(instance):
    assert isinstance(instance, atl_types_StringType)

@given(instance=atl_types_ThisModuleType_strategy)
@settings(max_examples=50)
def test_atl_types_thismoduletype_instantiation(instance):
    assert isinstance(instance, atl_types_ThisModuleType)

@given(instance=atl_types_UnionType_strategy)
@settings(max_examples=50)
def test_atl_types_uniontype_instantiation(instance):
    assert isinstance(instance, atl_types_UnionType)

@given(instance=atl_types_ReflectiveType_strategy)
@settings(max_examples=50)
def test_atl_types_reflectivetype_instantiation(instance):
    assert isinstance(instance, atl_types_ReflectiveType)

@given(instance=atl_types_EClass_strategy)
@settings(max_examples=50)
def test_atl_types_eclass_instantiation(instance):
    assert isinstance(instance, atl_types_EClass)
