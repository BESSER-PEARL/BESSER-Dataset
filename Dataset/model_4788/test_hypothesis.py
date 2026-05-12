import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    UnsignedInt,
    types_ULong,
    OpenDDSLib,
    types_DataLib,
    types_UShort,
    types_ULongLong,
    FloatingPoint,
    types_Double,
    Type,
    types_Struct,
    types_Typedef,
    types_Union,
    types_Collection,
    types_Case,
    types_Field,
    types_Branch,
    Simple,
    types_Char,
    types_WChar,
    types_Simple,
    Int,
    types_UnsignedInt,
    types_SignedInt,
    types_Octet,
    types_LongDouble,
    SignedInt,
    types_Short,
    types_LongLong,
    types_Long,
    types_Key,
    types_Int,
    types_FloatingPoint,
    types_Float,
    types_Enum,
    types_Boolean,
    types_Type,
    Collection,
    types_WString,
    types_String,
    types_Sequence,
    types_Array,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_unsignedint_is_not_abstract():
    assert not inspect.isabstract(UnsignedInt)


def test_unsignedint_constructor_exists():
    assert callable(UnsignedInt.__init__)


def test_unsignedint_constructor_args():
    sig = inspect.signature(UnsignedInt.__init__)
    params = list(sig.parameters.keys())



def test_types_ulong_is_not_abstract():
    assert not inspect.isabstract(types_ULong)


def test_types_ulong_constructor_exists():
    assert callable(types_ULong.__init__)


def test_types_ulong_constructor_args():
    sig = inspect.signature(types_ULong.__init__)
    params = list(sig.parameters.keys())



def test_openddslib_is_not_abstract():
    assert not inspect.isabstract(OpenDDSLib)


def test_openddslib_constructor_exists():
    assert callable(OpenDDSLib.__init__)


def test_openddslib_constructor_args():
    sig = inspect.signature(OpenDDSLib.__init__)
    params = list(sig.parameters.keys())



def test_types_datalib_is_not_abstract():
    assert not inspect.isabstract(types_DataLib)


def test_types_datalib_constructor_exists():
    assert callable(types_DataLib.__init__)


def test_types_datalib_constructor_args():
    sig = inspect.signature(types_DataLib.__init__)
    params = list(sig.parameters.keys())



def test_types_ushort_is_not_abstract():
    assert not inspect.isabstract(types_UShort)


def test_types_ushort_constructor_exists():
    assert callable(types_UShort.__init__)


def test_types_ushort_constructor_args():
    sig = inspect.signature(types_UShort.__init__)
    params = list(sig.parameters.keys())



def test_types_ulonglong_is_not_abstract():
    assert not inspect.isabstract(types_ULongLong)


def test_types_ulonglong_constructor_exists():
    assert callable(types_ULongLong.__init__)


def test_types_ulonglong_constructor_args():
    sig = inspect.signature(types_ULongLong.__init__)
    params = list(sig.parameters.keys())



def test_floatingpoint_is_not_abstract():
    assert not inspect.isabstract(FloatingPoint)


def test_floatingpoint_constructor_exists():
    assert callable(FloatingPoint.__init__)


def test_floatingpoint_constructor_args():
    sig = inspect.signature(FloatingPoint.__init__)
    params = list(sig.parameters.keys())



def test_types_double_is_not_abstract():
    assert not inspect.isabstract(types_Double)


def test_types_double_constructor_exists():
    assert callable(types_Double.__init__)


def test_types_double_constructor_args():
    sig = inspect.signature(types_Double.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_types_struct_is_not_abstract():
    assert not inspect.isabstract(types_Struct)


def test_types_struct_constructor_exists():
    assert callable(types_Struct.__init__)


def test_types_struct_constructor_args():
    sig = inspect.signature(types_Struct.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "isDcpsDataType" in params, "Missing parameter 'isDcpsDataType'"

def test_types_struct_has_name():
    assert hasattr(types_Struct, "name")
    descriptor = None
    for klass in types_Struct.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_types_struct_has_isDcpsDataType():
    assert hasattr(types_Struct, "isDcpsDataType")
    descriptor = None
    for klass in types_Struct.__mro__:
        if "isDcpsDataType" in klass.__dict__:
            descriptor = klass.__dict__["isDcpsDataType"]
            break
    assert isinstance(descriptor, property)



def test_types_typedef_is_not_abstract():
    assert not inspect.isabstract(types_Typedef)


def test_types_typedef_constructor_exists():
    assert callable(types_Typedef.__init__)


def test_types_typedef_constructor_args():
    sig = inspect.signature(types_Typedef.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_types_typedef_has_name():
    assert hasattr(types_Typedef, "name")
    descriptor = None
    for klass in types_Typedef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_types_union_is_not_abstract():
    assert not inspect.isabstract(types_Union)


def test_types_union_constructor_exists():
    assert callable(types_Union.__init__)


def test_types_union_constructor_args():
    sig = inspect.signature(types_Union.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_types_union_has_name():
    assert hasattr(types_Union, "name")
    descriptor = None
    for klass in types_Union.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_types_collection_is_not_abstract():
    assert not inspect.isabstract(types_Collection)


def test_types_collection_constructor_exists():
    assert callable(types_Collection.__init__)


def test_types_collection_constructor_args():
    sig = inspect.signature(types_Collection.__init__)
    params = list(sig.parameters.keys())
    assert "length" in params, "Missing parameter 'length'"

def test_types_collection_has_length():
    assert hasattr(types_Collection, "length")
    descriptor = None
    for klass in types_Collection.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)



def test_types_case_is_not_abstract():
    assert not inspect.isabstract(types_Case)


def test_types_case_constructor_exists():
    assert callable(types_Case.__init__)


def test_types_case_constructor_args():
    sig = inspect.signature(types_Case.__init__)
    params = list(sig.parameters.keys())
    assert "literal" in params, "Missing parameter 'literal'"

def test_types_case_has_literal():
    assert hasattr(types_Case, "literal")
    descriptor = None
    for klass in types_Case.__mro__:
        if "literal" in klass.__dict__:
            descriptor = klass.__dict__["literal"]
            break
    assert isinstance(descriptor, property)



def test_types_field_is_not_abstract():
    assert not inspect.isabstract(types_Field)


def test_types_field_constructor_exists():
    assert callable(types_Field.__init__)


def test_types_field_constructor_args():
    sig = inspect.signature(types_Field.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_types_field_has_name():
    assert hasattr(types_Field, "name")
    descriptor = None
    for klass in types_Field.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_types_branch_is_not_abstract():
    assert not inspect.isabstract(types_Branch)


def test_types_branch_constructor_exists():
    assert callable(types_Branch.__init__)


def test_types_branch_constructor_args():
    sig = inspect.signature(types_Branch.__init__)
    params = list(sig.parameters.keys())



def test_simple_is_not_abstract():
    assert not inspect.isabstract(Simple)


def test_simple_constructor_exists():
    assert callable(Simple.__init__)


def test_simple_constructor_args():
    sig = inspect.signature(Simple.__init__)
    params = list(sig.parameters.keys())



def test_types_char_is_not_abstract():
    assert not inspect.isabstract(types_Char)


def test_types_char_constructor_exists():
    assert callable(types_Char.__init__)


def test_types_char_constructor_args():
    sig = inspect.signature(types_Char.__init__)
    params = list(sig.parameters.keys())



def test_types_wchar_is_not_abstract():
    assert not inspect.isabstract(types_WChar)


def test_types_wchar_constructor_exists():
    assert callable(types_WChar.__init__)


def test_types_wchar_constructor_args():
    sig = inspect.signature(types_WChar.__init__)
    params = list(sig.parameters.keys())



def test_types_simple_is_not_abstract():
    assert not inspect.isabstract(types_Simple)


def test_types_simple_constructor_exists():
    assert callable(types_Simple.__init__)


def test_types_simple_constructor_args():
    sig = inspect.signature(types_Simple.__init__)
    params = list(sig.parameters.keys())



def test_int_is_not_abstract():
    assert not inspect.isabstract(Int)


def test_int_constructor_exists():
    assert callable(Int.__init__)


def test_int_constructor_args():
    sig = inspect.signature(Int.__init__)
    params = list(sig.parameters.keys())



def test_types_unsignedint_is_not_abstract():
    assert not inspect.isabstract(types_UnsignedInt)


def test_types_unsignedint_constructor_exists():
    assert callable(types_UnsignedInt.__init__)


def test_types_unsignedint_constructor_args():
    sig = inspect.signature(types_UnsignedInt.__init__)
    params = list(sig.parameters.keys())



def test_types_signedint_is_not_abstract():
    assert not inspect.isabstract(types_SignedInt)


def test_types_signedint_constructor_exists():
    assert callable(types_SignedInt.__init__)


def test_types_signedint_constructor_args():
    sig = inspect.signature(types_SignedInt.__init__)
    params = list(sig.parameters.keys())



def test_types_octet_is_not_abstract():
    assert not inspect.isabstract(types_Octet)


def test_types_octet_constructor_exists():
    assert callable(types_Octet.__init__)


def test_types_octet_constructor_args():
    sig = inspect.signature(types_Octet.__init__)
    params = list(sig.parameters.keys())



def test_types_longdouble_is_not_abstract():
    assert not inspect.isabstract(types_LongDouble)


def test_types_longdouble_constructor_exists():
    assert callable(types_LongDouble.__init__)


def test_types_longdouble_constructor_args():
    sig = inspect.signature(types_LongDouble.__init__)
    params = list(sig.parameters.keys())



def test_signedint_is_not_abstract():
    assert not inspect.isabstract(SignedInt)


def test_signedint_constructor_exists():
    assert callable(SignedInt.__init__)


def test_signedint_constructor_args():
    sig = inspect.signature(SignedInt.__init__)
    params = list(sig.parameters.keys())



def test_types_short_is_not_abstract():
    assert not inspect.isabstract(types_Short)


def test_types_short_constructor_exists():
    assert callable(types_Short.__init__)


def test_types_short_constructor_args():
    sig = inspect.signature(types_Short.__init__)
    params = list(sig.parameters.keys())



def test_types_longlong_is_not_abstract():
    assert not inspect.isabstract(types_LongLong)


def test_types_longlong_constructor_exists():
    assert callable(types_LongLong.__init__)


def test_types_longlong_constructor_args():
    sig = inspect.signature(types_LongLong.__init__)
    params = list(sig.parameters.keys())



def test_types_long_is_not_abstract():
    assert not inspect.isabstract(types_Long)


def test_types_long_constructor_exists():
    assert callable(types_Long.__init__)


def test_types_long_constructor_args():
    sig = inspect.signature(types_Long.__init__)
    params = list(sig.parameters.keys())



def test_types_key_is_not_abstract():
    assert not inspect.isabstract(types_Key)


def test_types_key_constructor_exists():
    assert callable(types_Key.__init__)


def test_types_key_constructor_args():
    sig = inspect.signature(types_Key.__init__)
    params = list(sig.parameters.keys())



def test_types_int_is_not_abstract():
    assert not inspect.isabstract(types_Int)


def test_types_int_constructor_exists():
    assert callable(types_Int.__init__)


def test_types_int_constructor_args():
    sig = inspect.signature(types_Int.__init__)
    params = list(sig.parameters.keys())



def test_types_floatingpoint_is_not_abstract():
    assert not inspect.isabstract(types_FloatingPoint)


def test_types_floatingpoint_constructor_exists():
    assert callable(types_FloatingPoint.__init__)


def test_types_floatingpoint_constructor_args():
    sig = inspect.signature(types_FloatingPoint.__init__)
    params = list(sig.parameters.keys())



def test_types_float_is_not_abstract():
    assert not inspect.isabstract(types_Float)


def test_types_float_constructor_exists():
    assert callable(types_Float.__init__)


def test_types_float_constructor_args():
    sig = inspect.signature(types_Float.__init__)
    params = list(sig.parameters.keys())



def test_types_enum_is_not_abstract():
    assert not inspect.isabstract(types_Enum)


def test_types_enum_constructor_exists():
    assert callable(types_Enum.__init__)


def test_types_enum_constructor_args():
    sig = inspect.signature(types_Enum.__init__)
    params = list(sig.parameters.keys())
    assert "literals" in params, "Missing parameter 'literals'"
    assert "name" in params, "Missing parameter 'name'"

def test_types_enum_has_literals():
    assert hasattr(types_Enum, "literals")
    descriptor = None
    for klass in types_Enum.__mro__:
        if "literals" in klass.__dict__:
            descriptor = klass.__dict__["literals"]
            break
    assert isinstance(descriptor, property)

def test_types_enum_has_name():
    assert hasattr(types_Enum, "name")
    descriptor = None
    for klass in types_Enum.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_types_boolean_is_not_abstract():
    assert not inspect.isabstract(types_Boolean)


def test_types_boolean_constructor_exists():
    assert callable(types_Boolean.__init__)


def test_types_boolean_constructor_args():
    sig = inspect.signature(types_Boolean.__init__)
    params = list(sig.parameters.keys())



def test_types_type_is_not_abstract():
    assert not inspect.isabstract(types_Type)


def test_types_type_constructor_exists():
    assert callable(types_Type.__init__)


def test_types_type_constructor_args():
    sig = inspect.signature(types_Type.__init__)
    params = list(sig.parameters.keys())



def test_collection_is_not_abstract():
    assert not inspect.isabstract(Collection)


def test_collection_constructor_exists():
    assert callable(Collection.__init__)


def test_collection_constructor_args():
    sig = inspect.signature(Collection.__init__)
    params = list(sig.parameters.keys())



def test_types_wstring_is_not_abstract():
    assert not inspect.isabstract(types_WString)


def test_types_wstring_constructor_exists():
    assert callable(types_WString.__init__)


def test_types_wstring_constructor_args():
    sig = inspect.signature(types_WString.__init__)
    params = list(sig.parameters.keys())



def test_types_string_is_not_abstract():
    assert not inspect.isabstract(types_String)


def test_types_string_constructor_exists():
    assert callable(types_String.__init__)


def test_types_string_constructor_args():
    sig = inspect.signature(types_String.__init__)
    params = list(sig.parameters.keys())



def test_types_sequence_is_not_abstract():
    assert not inspect.isabstract(types_Sequence)


def test_types_sequence_constructor_exists():
    assert callable(types_Sequence.__init__)


def test_types_sequence_constructor_args():
    sig = inspect.signature(types_Sequence.__init__)
    params = list(sig.parameters.keys())



def test_types_array_is_not_abstract():
    assert not inspect.isabstract(types_Array)


def test_types_array_constructor_exists():
    assert callable(types_Array.__init__)


def test_types_array_constructor_args():
    sig = inspect.signature(types_Array.__init__)
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
UnsignedInt_strategy = st.builds(
    UnsignedInt,
)
types_ULong_strategy = st.builds(
    types_ULong,
)
OpenDDSLib_strategy = st.builds(
    OpenDDSLib,
)
types_DataLib_strategy = st.builds(
    types_DataLib,
)
types_UShort_strategy = st.builds(
    types_UShort,
)
types_ULongLong_strategy = st.builds(
    types_ULongLong,
)
FloatingPoint_strategy = st.builds(
    FloatingPoint,
)
types_Double_strategy = st.builds(
    types_Double,
)
Type_strategy = st.builds(
    Type,
)
types_Struct_strategy = st.builds(
    types_Struct,
    name=
        safe_text,
    isDcpsDataType=
        st.booleans()
)
types_Typedef_strategy = st.builds(
    types_Typedef,
    name=
        safe_text
)
types_Union_strategy = st.builds(
    types_Union,
    name=
        safe_text
)
types_Collection_strategy = st.builds(
    types_Collection,
    length=
        safe_text
)
types_Case_strategy = st.builds(
    types_Case,
    literal=
        safe_text
)
types_Field_strategy = st.builds(
    types_Field,
    name=
        safe_text
)
types_Branch_strategy = st.builds(
    types_Branch,
)
Simple_strategy = st.builds(
    Simple,
)
types_Char_strategy = st.builds(
    types_Char,
)
types_WChar_strategy = st.builds(
    types_WChar,
)
types_Simple_strategy = st.builds(
    types_Simple,
)
Int_strategy = st.builds(
    Int,
)
types_UnsignedInt_strategy = st.builds(
    types_UnsignedInt,
)
types_SignedInt_strategy = st.builds(
    types_SignedInt,
)
types_Octet_strategy = st.builds(
    types_Octet,
)
types_LongDouble_strategy = st.builds(
    types_LongDouble,
)
SignedInt_strategy = st.builds(
    SignedInt,
)
types_Short_strategy = st.builds(
    types_Short,
)
types_LongLong_strategy = st.builds(
    types_LongLong,
)
types_Long_strategy = st.builds(
    types_Long,
)
types_Key_strategy = st.builds(
    types_Key,
)
types_Int_strategy = st.builds(
    types_Int,
)
types_FloatingPoint_strategy = st.builds(
    types_FloatingPoint,
)
types_Float_strategy = st.builds(
    types_Float,
)
types_Enum_strategy = st.builds(
    types_Enum,
    literals=
        safe_text,
    name=
        safe_text
)
types_Boolean_strategy = st.builds(
    types_Boolean,
)
types_Type_strategy = st.builds(
    types_Type,
)
Collection_strategy = st.builds(
    Collection,
)
types_WString_strategy = st.builds(
    types_WString,
)
types_String_strategy = st.builds(
    types_String,
)
types_Sequence_strategy = st.builds(
    types_Sequence,
)
types_Array_strategy = st.builds(
    types_Array,
)

@given(instance=UnsignedInt_strategy)
@settings(max_examples=50)
def test_unsignedint_instantiation(instance):
    assert isinstance(instance, UnsignedInt)

@given(instance=types_ULong_strategy)
@settings(max_examples=50)
def test_types_ulong_instantiation(instance):
    assert isinstance(instance, types_ULong)

@given(instance=OpenDDSLib_strategy)
@settings(max_examples=50)
def test_openddslib_instantiation(instance):
    assert isinstance(instance, OpenDDSLib)

@given(instance=types_DataLib_strategy)
@settings(max_examples=50)
def test_types_datalib_instantiation(instance):
    assert isinstance(instance, types_DataLib)

@given(instance=types_UShort_strategy)
@settings(max_examples=50)
def test_types_ushort_instantiation(instance):
    assert isinstance(instance, types_UShort)

@given(instance=types_ULongLong_strategy)
@settings(max_examples=50)
def test_types_ulonglong_instantiation(instance):
    assert isinstance(instance, types_ULongLong)

@given(instance=FloatingPoint_strategy)
@settings(max_examples=50)
def test_floatingpoint_instantiation(instance):
    assert isinstance(instance, FloatingPoint)

@given(instance=types_Double_strategy)
@settings(max_examples=50)
def test_types_double_instantiation(instance):
    assert isinstance(instance, types_Double)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=types_Struct_strategy)
@settings(max_examples=50)
def test_types_struct_instantiation(instance):
    assert isinstance(instance, types_Struct)



@given(instance=types_Struct_strategy)
def test_types_struct_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=types_Struct_strategy)
def test_types_struct_isDcpsDataType_setter(instance):
    original = instance.isDcpsDataType
    instance.isDcpsDataType = original
    assert instance.isDcpsDataType == original

@given(instance=types_Typedef_strategy)
@settings(max_examples=50)
def test_types_typedef_instantiation(instance):
    assert isinstance(instance, types_Typedef)



@given(instance=types_Typedef_strategy)
def test_types_typedef_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=types_Union_strategy)
@settings(max_examples=50)
def test_types_union_instantiation(instance):
    assert isinstance(instance, types_Union)



@given(instance=types_Union_strategy)
def test_types_union_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=types_Collection_strategy)
@settings(max_examples=50)
def test_types_collection_instantiation(instance):
    assert isinstance(instance, types_Collection)



@given(instance=types_Collection_strategy)
def test_types_collection_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original

@given(instance=types_Case_strategy)
@settings(max_examples=50)
def test_types_case_instantiation(instance):
    assert isinstance(instance, types_Case)



@given(instance=types_Case_strategy)
def test_types_case_literal_setter(instance):
    original = instance.literal
    instance.literal = original
    assert instance.literal == original

@given(instance=types_Field_strategy)
@settings(max_examples=50)
def test_types_field_instantiation(instance):
    assert isinstance(instance, types_Field)



@given(instance=types_Field_strategy)
def test_types_field_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=types_Branch_strategy)
@settings(max_examples=50)
def test_types_branch_instantiation(instance):
    assert isinstance(instance, types_Branch)

@given(instance=Simple_strategy)
@settings(max_examples=50)
def test_simple_instantiation(instance):
    assert isinstance(instance, Simple)

@given(instance=types_Char_strategy)
@settings(max_examples=50)
def test_types_char_instantiation(instance):
    assert isinstance(instance, types_Char)

@given(instance=types_WChar_strategy)
@settings(max_examples=50)
def test_types_wchar_instantiation(instance):
    assert isinstance(instance, types_WChar)

@given(instance=types_Simple_strategy)
@settings(max_examples=50)
def test_types_simple_instantiation(instance):
    assert isinstance(instance, types_Simple)

@given(instance=Int_strategy)
@settings(max_examples=50)
def test_int_instantiation(instance):
    assert isinstance(instance, Int)

@given(instance=types_UnsignedInt_strategy)
@settings(max_examples=50)
def test_types_unsignedint_instantiation(instance):
    assert isinstance(instance, types_UnsignedInt)

@given(instance=types_SignedInt_strategy)
@settings(max_examples=50)
def test_types_signedint_instantiation(instance):
    assert isinstance(instance, types_SignedInt)

@given(instance=types_Octet_strategy)
@settings(max_examples=50)
def test_types_octet_instantiation(instance):
    assert isinstance(instance, types_Octet)

@given(instance=types_LongDouble_strategy)
@settings(max_examples=50)
def test_types_longdouble_instantiation(instance):
    assert isinstance(instance, types_LongDouble)

@given(instance=SignedInt_strategy)
@settings(max_examples=50)
def test_signedint_instantiation(instance):
    assert isinstance(instance, SignedInt)

@given(instance=types_Short_strategy)
@settings(max_examples=50)
def test_types_short_instantiation(instance):
    assert isinstance(instance, types_Short)

@given(instance=types_LongLong_strategy)
@settings(max_examples=50)
def test_types_longlong_instantiation(instance):
    assert isinstance(instance, types_LongLong)

@given(instance=types_Long_strategy)
@settings(max_examples=50)
def test_types_long_instantiation(instance):
    assert isinstance(instance, types_Long)

@given(instance=types_Key_strategy)
@settings(max_examples=50)
def test_types_key_instantiation(instance):
    assert isinstance(instance, types_Key)

@given(instance=types_Int_strategy)
@settings(max_examples=50)
def test_types_int_instantiation(instance):
    assert isinstance(instance, types_Int)

@given(instance=types_FloatingPoint_strategy)
@settings(max_examples=50)
def test_types_floatingpoint_instantiation(instance):
    assert isinstance(instance, types_FloatingPoint)

@given(instance=types_Float_strategy)
@settings(max_examples=50)
def test_types_float_instantiation(instance):
    assert isinstance(instance, types_Float)

@given(instance=types_Enum_strategy)
@settings(max_examples=50)
def test_types_enum_instantiation(instance):
    assert isinstance(instance, types_Enum)



@given(instance=types_Enum_strategy)
def test_types_enum_literals_setter(instance):
    original = instance.literals
    instance.literals = original
    assert instance.literals == original



@given(instance=types_Enum_strategy)
def test_types_enum_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=types_Boolean_strategy)
@settings(max_examples=50)
def test_types_boolean_instantiation(instance):
    assert isinstance(instance, types_Boolean)

@given(instance=types_Type_strategy)
@settings(max_examples=50)
def test_types_type_instantiation(instance):
    assert isinstance(instance, types_Type)

@given(instance=Collection_strategy)
@settings(max_examples=50)
def test_collection_instantiation(instance):
    assert isinstance(instance, Collection)

@given(instance=types_WString_strategy)
@settings(max_examples=50)
def test_types_wstring_instantiation(instance):
    assert isinstance(instance, types_WString)

@given(instance=types_String_strategy)
@settings(max_examples=50)
def test_types_string_instantiation(instance):
    assert isinstance(instance, types_String)

@given(instance=types_Sequence_strategy)
@settings(max_examples=50)
def test_types_sequence_instantiation(instance):
    assert isinstance(instance, types_Sequence)

@given(instance=types_Array_strategy)
@settings(max_examples=50)
def test_types_array_instantiation(instance):
    assert isinstance(instance, types_Array)
