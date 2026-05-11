import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    types::EEnum,
    FunctionType,
    types::MethodType,
    types::EClass,
    NumberType,
    types::RealType,
    RealType,
    types::IntegerType,
    DataType,
    types::NumberType,
    types::StringType,
    types::BooleanType,
    Type,
    types::MapType,
    types::EnumType,
    types::CollectionType,
    types::FunctionType,
    types::ObjectType,
    types::DataType,
    types::Type,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_types::eenum_is_not_abstract():
    assert not inspect.isabstract(types::EEnum)


def test_types::eenum_constructor_exists():
    assert callable(types::EEnum.__init__)


def test_types::eenum_constructor_args():
    sig = inspect.signature(types::EEnum.__init__)
    params = list(sig.parameters.keys())



def test_functiontype_is_not_abstract():
    assert not inspect.isabstract(FunctionType)


def test_functiontype_constructor_exists():
    assert callable(FunctionType.__init__)


def test_functiontype_constructor_args():
    sig = inspect.signature(FunctionType.__init__)
    params = list(sig.parameters.keys())



def test_types::methodtype_is_not_abstract():
    assert not inspect.isabstract(types::MethodType)


def test_types::methodtype_constructor_exists():
    assert callable(types::MethodType.__init__)


def test_types::methodtype_constructor_args():
    sig = inspect.signature(types::MethodType.__init__)
    params = list(sig.parameters.keys())



def test_types::eclass_is_not_abstract():
    assert not inspect.isabstract(types::EClass)


def test_types::eclass_constructor_exists():
    assert callable(types::EClass.__init__)


def test_types::eclass_constructor_args():
    sig = inspect.signature(types::EClass.__init__)
    params = list(sig.parameters.keys())



def test_numbertype_is_not_abstract():
    assert not inspect.isabstract(NumberType)


def test_numbertype_constructor_exists():
    assert callable(NumberType.__init__)


def test_numbertype_constructor_args():
    sig = inspect.signature(NumberType.__init__)
    params = list(sig.parameters.keys())



def test_types::realtype_is_not_abstract():
    assert not inspect.isabstract(types::RealType)


def test_types::realtype_constructor_exists():
    assert callable(types::RealType.__init__)


def test_types::realtype_constructor_args():
    sig = inspect.signature(types::RealType.__init__)
    params = list(sig.parameters.keys())



def test_realtype_is_not_abstract():
    assert not inspect.isabstract(RealType)


def test_realtype_constructor_exists():
    assert callable(RealType.__init__)


def test_realtype_constructor_args():
    sig = inspect.signature(RealType.__init__)
    params = list(sig.parameters.keys())



def test_types::integertype_is_not_abstract():
    assert not inspect.isabstract(types::IntegerType)


def test_types::integertype_constructor_exists():
    assert callable(types::IntegerType.__init__)


def test_types::integertype_constructor_args():
    sig = inspect.signature(types::IntegerType.__init__)
    params = list(sig.parameters.keys())



def test_datatype_is_not_abstract():
    assert not inspect.isabstract(DataType)


def test_datatype_constructor_exists():
    assert callable(DataType.__init__)


def test_datatype_constructor_args():
    sig = inspect.signature(DataType.__init__)
    params = list(sig.parameters.keys())



def test_types::numbertype_is_not_abstract():
    assert not inspect.isabstract(types::NumberType)


def test_types::numbertype_constructor_exists():
    assert callable(types::NumberType.__init__)


def test_types::numbertype_constructor_args():
    sig = inspect.signature(types::NumberType.__init__)
    params = list(sig.parameters.keys())



def test_types::stringtype_is_not_abstract():
    assert not inspect.isabstract(types::StringType)


def test_types::stringtype_constructor_exists():
    assert callable(types::StringType.__init__)


def test_types::stringtype_constructor_args():
    sig = inspect.signature(types::StringType.__init__)
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



def test_types::maptype_is_not_abstract():
    assert not inspect.isabstract(types::MapType)


def test_types::maptype_constructor_exists():
    assert callable(types::MapType.__init__)


def test_types::maptype_constructor_args():
    sig = inspect.signature(types::MapType.__init__)
    params = list(sig.parameters.keys())



def test_types::enumtype_is_not_abstract():
    assert not inspect.isabstract(types::EnumType)


def test_types::enumtype_constructor_exists():
    assert callable(types::EnumType.__init__)


def test_types::enumtype_constructor_args():
    sig = inspect.signature(types::EnumType.__init__)
    params = list(sig.parameters.keys())



def test_types::collectiontype_is_not_abstract():
    assert not inspect.isabstract(types::CollectionType)


def test_types::collectiontype_constructor_exists():
    assert callable(types::CollectionType.__init__)


def test_types::collectiontype_constructor_args():
    sig = inspect.signature(types::CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_types::functiontype_is_not_abstract():
    assert not inspect.isabstract(types::FunctionType)


def test_types::functiontype_constructor_exists():
    assert callable(types::FunctionType.__init__)


def test_types::functiontype_constructor_args():
    sig = inspect.signature(types::FunctionType.__init__)
    params = list(sig.parameters.keys())
    assert "optionalParameterCount" in params, "Missing parameter 'optionalParameterCount'"

def test_types::functiontype_has_optionalParameterCount():
    assert hasattr(types::FunctionType, "optionalParameterCount")
    descriptor = None
    for klass in types::FunctionType.__mro__:
        if "optionalParameterCount" in klass.__dict__:
            descriptor = klass.__dict__["optionalParameterCount"]
            break
    assert isinstance(descriptor, property)



def test_types::objecttype_is_not_abstract():
    assert not inspect.isabstract(types::ObjectType)


def test_types::objecttype_constructor_exists():
    assert callable(types::ObjectType.__init__)


def test_types::objecttype_constructor_args():
    sig = inspect.signature(types::ObjectType.__init__)
    params = list(sig.parameters.keys())



def test_types::datatype_is_not_abstract():
    assert not inspect.isabstract(types::DataType)


def test_types::datatype_constructor_exists():
    assert callable(types::DataType.__init__)


def test_types::datatype_constructor_args():
    sig = inspect.signature(types::DataType.__init__)
    params = list(sig.parameters.keys())



def test_types::type_is_not_abstract():
    assert not inspect.isabstract(types::Type)


def test_types::type_constructor_exists():
    assert callable(types::Type.__init__)


def test_types::type_constructor_args():
    sig = inspect.signature(types::Type.__init__)
    params = list(sig.parameters.keys())
    assert "inExtentDomain" in params, "Missing parameter 'inExtentDomain'"

def test_types::type_has_inExtentDomain():
    assert hasattr(types::Type, "inExtentDomain")
    descriptor = None
    for klass in types::Type.__mro__:
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
types::EEnum_strategy = st.builds(
    types::EEnum,
)
FunctionType_strategy = st.builds(
    FunctionType,
)
types::MethodType_strategy = st.builds(
    types::MethodType,
)
types::EClass_strategy = st.builds(
    types::EClass,
)
NumberType_strategy = st.builds(
    NumberType,
)
types::RealType_strategy = st.builds(
    types::RealType,
)
RealType_strategy = st.builds(
    RealType,
)
types::IntegerType_strategy = st.builds(
    types::IntegerType,
)
DataType_strategy = st.builds(
    DataType,
)
types::NumberType_strategy = st.builds(
    types::NumberType,
)
types::StringType_strategy = st.builds(
    types::StringType,
)
types::BooleanType_strategy = st.builds(
    types::BooleanType,
)
Type_strategy = st.builds(
    Type,
)
types::MapType_strategy = st.builds(
    types::MapType,
)
types::EnumType_strategy = st.builds(
    types::EnumType,
)
types::CollectionType_strategy = st.builds(
    types::CollectionType,
)
types::FunctionType_strategy = st.builds(
    types::FunctionType,
    optionalParameterCount=
        st.integers()
)
types::ObjectType_strategy = st.builds(
    types::ObjectType,
)
types::DataType_strategy = st.builds(
    types::DataType,
)
types::Type_strategy = st.builds(
    types::Type,
    inExtentDomain=
        st.booleans()
)

@given(instance=types::EEnum_strategy)
@settings(max_examples=50)
def test_types::eenum_instantiation(instance):
    assert isinstance(instance, types::EEnum)

@given(instance=FunctionType_strategy)
@settings(max_examples=50)
def test_functiontype_instantiation(instance):
    assert isinstance(instance, FunctionType)

@given(instance=types::MethodType_strategy)
@settings(max_examples=50)
def test_types::methodtype_instantiation(instance):
    assert isinstance(instance, types::MethodType)

@given(instance=types::EClass_strategy)
@settings(max_examples=50)
def test_types::eclass_instantiation(instance):
    assert isinstance(instance, types::EClass)

@given(instance=NumberType_strategy)
@settings(max_examples=50)
def test_numbertype_instantiation(instance):
    assert isinstance(instance, NumberType)

@given(instance=types::RealType_strategy)
@settings(max_examples=50)
def test_types::realtype_instantiation(instance):
    assert isinstance(instance, types::RealType)

@given(instance=RealType_strategy)
@settings(max_examples=50)
def test_realtype_instantiation(instance):
    assert isinstance(instance, RealType)

@given(instance=types::IntegerType_strategy)
@settings(max_examples=50)
def test_types::integertype_instantiation(instance):
    assert isinstance(instance, types::IntegerType)

@given(instance=DataType_strategy)
@settings(max_examples=50)
def test_datatype_instantiation(instance):
    assert isinstance(instance, DataType)

@given(instance=types::NumberType_strategy)
@settings(max_examples=50)
def test_types::numbertype_instantiation(instance):
    assert isinstance(instance, types::NumberType)

@given(instance=types::StringType_strategy)
@settings(max_examples=50)
def test_types::stringtype_instantiation(instance):
    assert isinstance(instance, types::StringType)

@given(instance=types::BooleanType_strategy)
@settings(max_examples=50)
def test_types::booleantype_instantiation(instance):
    assert isinstance(instance, types::BooleanType)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=types::MapType_strategy)
@settings(max_examples=50)
def test_types::maptype_instantiation(instance):
    assert isinstance(instance, types::MapType)

@given(instance=types::EnumType_strategy)
@settings(max_examples=50)
def test_types::enumtype_instantiation(instance):
    assert isinstance(instance, types::EnumType)

@given(instance=types::CollectionType_strategy)
@settings(max_examples=50)
def test_types::collectiontype_instantiation(instance):
    assert isinstance(instance, types::CollectionType)

@given(instance=types::FunctionType_strategy)
@settings(max_examples=50)
def test_types::functiontype_instantiation(instance):
    assert isinstance(instance, types::FunctionType)

@given(instance=types::FunctionType_strategy)
def test_types::functiontype_optionalParameterCount_type(instance):
    assert isinstance(instance.optionalParameterCount, int)


@given(instance=types::FunctionType_strategy)
def test_types::functiontype_optionalParameterCount_setter(instance):
    original = instance.optionalParameterCount
    instance.optionalParameterCount = original
    assert instance.optionalParameterCount == original

@given(instance=types::ObjectType_strategy)
@settings(max_examples=50)
def test_types::objecttype_instantiation(instance):
    assert isinstance(instance, types::ObjectType)

@given(instance=types::DataType_strategy)
@settings(max_examples=50)
def test_types::datatype_instantiation(instance):
    assert isinstance(instance, types::DataType)

@given(instance=types::Type_strategy)
@settings(max_examples=50)
def test_types::type_instantiation(instance):
    assert isinstance(instance, types::Type)

@given(instance=types::Type_strategy)
def test_types::type_inExtentDomain_type(instance):
    assert isinstance(instance.inExtentDomain, bool)


@given(instance=types::Type_strategy)
def test_types::type_inExtentDomain_setter(instance):
    original = instance.inExtentDomain
    instance.inExtentDomain = original
    assert instance.inExtentDomain == original
