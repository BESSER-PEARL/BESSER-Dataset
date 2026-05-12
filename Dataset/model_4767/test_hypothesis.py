import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    types_EEnum,
    FunctionType,
    types_MethodType,
    types_EClass,
    NumberType,
    types_RealType,
    RealType,
    types_IntegerType,
    DataType,
    types_StringType,
    types_NumberType,
    types_BooleanType,
    Type,
    types_CollectionType,
    types_FunctionType,
    types_EnumType,
    types_ObjectType,
    types_MapType,
    types_DataType,
    types_Type,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_types_eenum_is_not_abstract():
    assert not inspect.isabstract(types_EEnum)


def test_types_eenum_constructor_exists():
    assert callable(types_EEnum.__init__)


def test_types_eenum_constructor_args():
    sig = inspect.signature(types_EEnum.__init__)
    params = list(sig.parameters.keys())



def test_functiontype_is_not_abstract():
    assert not inspect.isabstract(FunctionType)


def test_functiontype_constructor_exists():
    assert callable(FunctionType.__init__)


def test_functiontype_constructor_args():
    sig = inspect.signature(FunctionType.__init__)
    params = list(sig.parameters.keys())



def test_types_methodtype_is_not_abstract():
    assert not inspect.isabstract(types_MethodType)


def test_types_methodtype_constructor_exists():
    assert callable(types_MethodType.__init__)


def test_types_methodtype_constructor_args():
    sig = inspect.signature(types_MethodType.__init__)
    params = list(sig.parameters.keys())



def test_types_eclass_is_not_abstract():
    assert not inspect.isabstract(types_EClass)


def test_types_eclass_constructor_exists():
    assert callable(types_EClass.__init__)


def test_types_eclass_constructor_args():
    sig = inspect.signature(types_EClass.__init__)
    params = list(sig.parameters.keys())



def test_numbertype_is_not_abstract():
    assert not inspect.isabstract(NumberType)


def test_numbertype_constructor_exists():
    assert callable(NumberType.__init__)


def test_numbertype_constructor_args():
    sig = inspect.signature(NumberType.__init__)
    params = list(sig.parameters.keys())



def test_types_realtype_is_not_abstract():
    assert not inspect.isabstract(types_RealType)


def test_types_realtype_constructor_exists():
    assert callable(types_RealType.__init__)


def test_types_realtype_constructor_args():
    sig = inspect.signature(types_RealType.__init__)
    params = list(sig.parameters.keys())



def test_realtype_is_not_abstract():
    assert not inspect.isabstract(RealType)


def test_realtype_constructor_exists():
    assert callable(RealType.__init__)


def test_realtype_constructor_args():
    sig = inspect.signature(RealType.__init__)
    params = list(sig.parameters.keys())



def test_types_integertype_is_not_abstract():
    assert not inspect.isabstract(types_IntegerType)


def test_types_integertype_constructor_exists():
    assert callable(types_IntegerType.__init__)


def test_types_integertype_constructor_args():
    sig = inspect.signature(types_IntegerType.__init__)
    params = list(sig.parameters.keys())



def test_datatype_is_not_abstract():
    assert not inspect.isabstract(DataType)


def test_datatype_constructor_exists():
    assert callable(DataType.__init__)


def test_datatype_constructor_args():
    sig = inspect.signature(DataType.__init__)
    params = list(sig.parameters.keys())



def test_types_stringtype_is_not_abstract():
    assert not inspect.isabstract(types_StringType)


def test_types_stringtype_constructor_exists():
    assert callable(types_StringType.__init__)


def test_types_stringtype_constructor_args():
    sig = inspect.signature(types_StringType.__init__)
    params = list(sig.parameters.keys())



def test_types_numbertype_is_not_abstract():
    assert not inspect.isabstract(types_NumberType)


def test_types_numbertype_constructor_exists():
    assert callable(types_NumberType.__init__)


def test_types_numbertype_constructor_args():
    sig = inspect.signature(types_NumberType.__init__)
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



def test_types_collectiontype_is_not_abstract():
    assert not inspect.isabstract(types_CollectionType)


def test_types_collectiontype_constructor_exists():
    assert callable(types_CollectionType.__init__)


def test_types_collectiontype_constructor_args():
    sig = inspect.signature(types_CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_types_functiontype_is_not_abstract():
    assert not inspect.isabstract(types_FunctionType)


def test_types_functiontype_constructor_exists():
    assert callable(types_FunctionType.__init__)


def test_types_functiontype_constructor_args():
    sig = inspect.signature(types_FunctionType.__init__)
    params = list(sig.parameters.keys())
    assert "optionalParameterCount" in params, "Missing parameter 'optionalParameterCount'"

def test_types_functiontype_has_optionalParameterCount():
    assert hasattr(types_FunctionType, "optionalParameterCount")
    descriptor = None
    for klass in types_FunctionType.__mro__:
        if "optionalParameterCount" in klass.__dict__:
            descriptor = klass.__dict__["optionalParameterCount"]
            break
    assert isinstance(descriptor, property)



def test_types_enumtype_is_not_abstract():
    assert not inspect.isabstract(types_EnumType)


def test_types_enumtype_constructor_exists():
    assert callable(types_EnumType.__init__)


def test_types_enumtype_constructor_args():
    sig = inspect.signature(types_EnumType.__init__)
    params = list(sig.parameters.keys())



def test_types_objecttype_is_not_abstract():
    assert not inspect.isabstract(types_ObjectType)


def test_types_objecttype_constructor_exists():
    assert callable(types_ObjectType.__init__)


def test_types_objecttype_constructor_args():
    sig = inspect.signature(types_ObjectType.__init__)
    params = list(sig.parameters.keys())



def test_types_maptype_is_not_abstract():
    assert not inspect.isabstract(types_MapType)


def test_types_maptype_constructor_exists():
    assert callable(types_MapType.__init__)


def test_types_maptype_constructor_args():
    sig = inspect.signature(types_MapType.__init__)
    params = list(sig.parameters.keys())



def test_types_datatype_is_not_abstract():
    assert not inspect.isabstract(types_DataType)


def test_types_datatype_constructor_exists():
    assert callable(types_DataType.__init__)


def test_types_datatype_constructor_args():
    sig = inspect.signature(types_DataType.__init__)
    params = list(sig.parameters.keys())



def test_types_type_is_not_abstract():
    assert not inspect.isabstract(types_Type)


def test_types_type_constructor_exists():
    assert callable(types_Type.__init__)


def test_types_type_constructor_args():
    sig = inspect.signature(types_Type.__init__)
    params = list(sig.parameters.keys())
    assert "inExtentDomain" in params, "Missing parameter 'inExtentDomain'"

def test_types_type_has_inExtentDomain():
    assert hasattr(types_Type, "inExtentDomain")
    descriptor = None
    for klass in types_Type.__mro__:
        if "inExtentDomain" in klass.__dict__:
            descriptor = klass.__dict__["inExtentDomain"]
            break
    assert isinstance(descriptor, property)


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
types_EEnum_strategy = st.builds(
    types_EEnum,
)
FunctionType_strategy = st.builds(
    FunctionType,
)
types_MethodType_strategy = st.builds(
    types_MethodType,
)
types_EClass_strategy = st.builds(
    types_EClass,
)
NumberType_strategy = st.builds(
    NumberType,
)
types_RealType_strategy = st.builds(
    types_RealType,
)
RealType_strategy = st.builds(
    RealType,
)
types_IntegerType_strategy = st.builds(
    types_IntegerType,
)
DataType_strategy = st.builds(
    DataType,
)
types_StringType_strategy = st.builds(
    types_StringType,
)
types_NumberType_strategy = st.builds(
    types_NumberType,
)
types_BooleanType_strategy = st.builds(
    types_BooleanType,
)
Type_strategy = st.builds(
    Type,
)
types_CollectionType_strategy = st.builds(
    types_CollectionType,
)
types_FunctionType_strategy = st.builds(
    types_FunctionType,
    optionalParameterCount=
        st.integers()
)
types_EnumType_strategy = st.builds(
    types_EnumType,
)
types_ObjectType_strategy = st.builds(
    types_ObjectType,
)
types_MapType_strategy = st.builds(
    types_MapType,
)
types_DataType_strategy = st.builds(
    types_DataType,
)
types_Type_strategy = st.builds(
    types_Type,
    inExtentDomain=
        st.booleans()
)

@given(instance=types_EEnum_strategy)
@settings(max_examples=50)
def test_types_eenum_instantiation(instance):
    assert isinstance(instance, types_EEnum)

@given(instance=FunctionType_strategy)
@settings(max_examples=50)
def test_functiontype_instantiation(instance):
    assert isinstance(instance, FunctionType)

@given(instance=types_MethodType_strategy)
@settings(max_examples=50)
def test_types_methodtype_instantiation(instance):
    assert isinstance(instance, types_MethodType)

@given(instance=types_EClass_strategy)
@settings(max_examples=50)
def test_types_eclass_instantiation(instance):
    assert isinstance(instance, types_EClass)

@given(instance=NumberType_strategy)
@settings(max_examples=50)
def test_numbertype_instantiation(instance):
    assert isinstance(instance, NumberType)

@given(instance=types_RealType_strategy)
@settings(max_examples=50)
def test_types_realtype_instantiation(instance):
    assert isinstance(instance, types_RealType)

@given(instance=RealType_strategy)
@settings(max_examples=50)
def test_realtype_instantiation(instance):
    assert isinstance(instance, RealType)

@given(instance=types_IntegerType_strategy)
@settings(max_examples=50)
def test_types_integertype_instantiation(instance):
    assert isinstance(instance, types_IntegerType)

@given(instance=DataType_strategy)
@settings(max_examples=50)
def test_datatype_instantiation(instance):
    assert isinstance(instance, DataType)

@given(instance=types_StringType_strategy)
@settings(max_examples=50)
def test_types_stringtype_instantiation(instance):
    assert isinstance(instance, types_StringType)

@given(instance=types_NumberType_strategy)
@settings(max_examples=50)
def test_types_numbertype_instantiation(instance):
    assert isinstance(instance, types_NumberType)

@given(instance=types_BooleanType_strategy)
@settings(max_examples=50)
def test_types_booleantype_instantiation(instance):
    assert isinstance(instance, types_BooleanType)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=types_CollectionType_strategy)
@settings(max_examples=50)
def test_types_collectiontype_instantiation(instance):
    assert isinstance(instance, types_CollectionType)

@given(instance=types_FunctionType_strategy)
@settings(max_examples=50)
def test_types_functiontype_instantiation(instance):
    assert isinstance(instance, types_FunctionType)



@given(instance=types_FunctionType_strategy)
def test_types_functiontype_optionalParameterCount_setter(instance):
    original = instance.optionalParameterCount
    instance.optionalParameterCount = original
    assert instance.optionalParameterCount == original

@given(instance=types_EnumType_strategy)
@settings(max_examples=50)
def test_types_enumtype_instantiation(instance):
    assert isinstance(instance, types_EnumType)

@given(instance=types_ObjectType_strategy)
@settings(max_examples=50)
def test_types_objecttype_instantiation(instance):
    assert isinstance(instance, types_ObjectType)

@given(instance=types_MapType_strategy)
@settings(max_examples=50)
def test_types_maptype_instantiation(instance):
    assert isinstance(instance, types_MapType)

@given(instance=types_DataType_strategy)
@settings(max_examples=50)
def test_types_datatype_instantiation(instance):
    assert isinstance(instance, types_DataType)

@given(instance=types_Type_strategy)
@settings(max_examples=50)
def test_types_type_instantiation(instance):
    assert isinstance(instance, types_Type)



@given(instance=types_Type_strategy)
def test_types_type_inExtentDomain_setter(instance):
    original = instance.inExtentDomain
    instance.inExtentDomain = original
    assert instance.inExtentDomain == original
