import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    types::ManyTypes,
    types::SingleTypes,
    TestNextEnum,
    TestEnum,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_types::manytypes_is_not_abstract():
    assert not inspect.isabstract(types::ManyTypes)


def test_types::manytypes_constructor_exists():
    assert callable(types::ManyTypes.__init__)


def test_types::manytypes_constructor_args():
    sig = inspect.signature(types::ManyTypes.__init__)
    params = list(sig.parameters.keys())
    assert "enum" in params, "Missing parameter 'enum'"
    assert "longArray" in params, "Missing parameter 'longArray'"
    assert "string" in params, "Missing parameter 'string'"
    assert "byteObject" in params, "Missing parameter 'byteObject'"
    assert "charObject" in params, "Missing parameter 'charObject'"
    assert "doubleObject" in params, "Missing parameter 'doubleObject'"
    assert "integerObject" in params, "Missing parameter 'integerObject'"
    assert "byteArray" in params, "Missing parameter 'byteArray'"
    assert "stringArray" in params, "Missing parameter 'stringArray'"
    assert "bigInteger" in params, "Missing parameter 'bigInteger'"
    assert "clazz" in params, "Missing parameter 'clazz'"
    assert "long" in params, "Missing parameter 'long'"
    assert "floatObject" in params, "Missing parameter 'floatObject'"
    assert "date" in params, "Missing parameter 'date'"
    assert "bigDecimal" in params, "Missing parameter 'bigDecimal'"

def test_types::manytypes_has_enum():
    assert hasattr(types::ManyTypes, "enum")
    descriptor = None
    for klass in types::ManyTypes.__mro__:
        if "enum" in klass.__dict__:
            descriptor = klass.__dict__["enum"]
            break
    assert isinstance(descriptor, property)

def test_types::manytypes_has_longArray():
    assert hasattr(types::ManyTypes, "longArray")
    descriptor = None
    for klass in types::ManyTypes.__mro__:
        if "longArray" in klass.__dict__:
            descriptor = klass.__dict__["longArray"]
            break
    assert isinstance(descriptor, property)

def test_types::manytypes_has_string():
    assert hasattr(types::ManyTypes, "string")
    descriptor = None
    for klass in types::ManyTypes.__mro__:
        if "string" in klass.__dict__:
            descriptor = klass.__dict__["string"]
            break
    assert isinstance(descriptor, property)

def test_types::manytypes_has_byteObject():
    assert hasattr(types::ManyTypes, "byteObject")
    descriptor = None
    for klass in types::ManyTypes.__mro__:
        if "byteObject" in klass.__dict__:
            descriptor = klass.__dict__["byteObject"]
            break
    assert isinstance(descriptor, property)

def test_types::manytypes_has_charObject():
    assert hasattr(types::ManyTypes, "charObject")
    descriptor = None
    for klass in types::ManyTypes.__mro__:
        if "charObject" in klass.__dict__:
            descriptor = klass.__dict__["charObject"]
            break
    assert isinstance(descriptor, property)

def test_types::manytypes_has_doubleObject():
    assert hasattr(types::ManyTypes, "doubleObject")
    descriptor = None
    for klass in types::ManyTypes.__mro__:
        if "doubleObject" in klass.__dict__:
            descriptor = klass.__dict__["doubleObject"]
            break
    assert isinstance(descriptor, property)

def test_types::manytypes_has_integerObject():
    assert hasattr(types::ManyTypes, "integerObject")
    descriptor = None
    for klass in types::ManyTypes.__mro__:
        if "integerObject" in klass.__dict__:
            descriptor = klass.__dict__["integerObject"]
            break
    assert isinstance(descriptor, property)

def test_types::manytypes_has_byteArray():
    assert hasattr(types::ManyTypes, "byteArray")
    descriptor = None
    for klass in types::ManyTypes.__mro__:
        if "byteArray" in klass.__dict__:
            descriptor = klass.__dict__["byteArray"]
            break
    assert isinstance(descriptor, property)

def test_types::manytypes_has_stringArray():
    assert hasattr(types::ManyTypes, "stringArray")
    descriptor = None
    for klass in types::ManyTypes.__mro__:
        if "stringArray" in klass.__dict__:
            descriptor = klass.__dict__["stringArray"]
            break
    assert isinstance(descriptor, property)

def test_types::manytypes_has_bigInteger():
    assert hasattr(types::ManyTypes, "bigInteger")
    descriptor = None
    for klass in types::ManyTypes.__mro__:
        if "bigInteger" in klass.__dict__:
            descriptor = klass.__dict__["bigInteger"]
            break
    assert isinstance(descriptor, property)

def test_types::manytypes_has_clazz():
    assert hasattr(types::ManyTypes, "clazz")
    descriptor = None
    for klass in types::ManyTypes.__mro__:
        if "clazz" in klass.__dict__:
            descriptor = klass.__dict__["clazz"]
            break
    assert isinstance(descriptor, property)

def test_types::manytypes_has_long():
    assert hasattr(types::ManyTypes, "long")
    descriptor = None
    for klass in types::ManyTypes.__mro__:
        if "long" in klass.__dict__:
            descriptor = klass.__dict__["long"]
            break
    assert isinstance(descriptor, property)

def test_types::manytypes_has_floatObject():
    assert hasattr(types::ManyTypes, "floatObject")
    descriptor = None
    for klass in types::ManyTypes.__mro__:
        if "floatObject" in klass.__dict__:
            descriptor = klass.__dict__["floatObject"]
            break
    assert isinstance(descriptor, property)

def test_types::manytypes_has_date():
    assert hasattr(types::ManyTypes, "date")
    descriptor = None
    for klass in types::ManyTypes.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)

def test_types::manytypes_has_bigDecimal():
    assert hasattr(types::ManyTypes, "bigDecimal")
    descriptor = None
    for klass in types::ManyTypes.__mro__:
        if "bigDecimal" in klass.__dict__:
            descriptor = klass.__dict__["bigDecimal"]
            break
    assert isinstance(descriptor, property)



def test_types::singletypes_is_not_abstract():
    assert not inspect.isabstract(types::SingleTypes)


def test_types::singletypes_constructor_exists():
    assert callable(types::SingleTypes.__init__)


def test_types::singletypes_constructor_args():
    sig = inspect.signature(types::SingleTypes.__init__)
    params = list(sig.parameters.keys())
    assert "floatObject" in params, "Missing parameter 'floatObject'"
    assert "long" in params, "Missing parameter 'long'"
    assert "bigDecimal" in params, "Missing parameter 'bigDecimal'"
    assert "float" in params, "Missing parameter 'float'"
    assert "string" in params, "Missing parameter 'string'"
    assert "date" in params, "Missing parameter 'date'"
    assert "enum" in params, "Missing parameter 'enum'"
    assert "stringArray" in params, "Missing parameter 'stringArray'"
    assert "integerObject" in params, "Missing parameter 'integerObject'"
    assert "nextEnum" in params, "Missing parameter 'nextEnum'"
    assert "byte" in params, "Missing parameter 'byte'"
    assert "bigInteger" in params, "Missing parameter 'bigInteger'"
    assert "longArray" in params, "Missing parameter 'longArray'"
    assert "charObject" in params, "Missing parameter 'charObject'"
    assert "double" in params, "Missing parameter 'double'"
    assert "doubleObject" in params, "Missing parameter 'doubleObject'"
    assert "byteArray" in params, "Missing parameter 'byteArray'"
    assert "clazz" in params, "Missing parameter 'clazz'"
    assert "longObject" in params, "Missing parameter 'longObject'"
    assert "byteObject" in params, "Missing parameter 'byteObject'"
    assert "integer" in params, "Missing parameter 'integer'"
    assert "char" in params, "Missing parameter 'char'"

def test_types::singletypes_has_floatObject():
    assert hasattr(types::SingleTypes, "floatObject")
    descriptor = None
    for klass in types::SingleTypes.__mro__:
        if "floatObject" in klass.__dict__:
            descriptor = klass.__dict__["floatObject"]
            break
    assert isinstance(descriptor, property)

def test_types::singletypes_has_long():
    assert hasattr(types::SingleTypes, "long")
    descriptor = None
    for klass in types::SingleTypes.__mro__:
        if "long" in klass.__dict__:
            descriptor = klass.__dict__["long"]
            break
    assert isinstance(descriptor, property)

def test_types::singletypes_has_bigDecimal():
    assert hasattr(types::SingleTypes, "bigDecimal")
    descriptor = None
    for klass in types::SingleTypes.__mro__:
        if "bigDecimal" in klass.__dict__:
            descriptor = klass.__dict__["bigDecimal"]
            break
    assert isinstance(descriptor, property)

def test_types::singletypes_has_float():
    assert hasattr(types::SingleTypes, "float")
    descriptor = None
    for klass in types::SingleTypes.__mro__:
        if "float" in klass.__dict__:
            descriptor = klass.__dict__["float"]
            break
    assert isinstance(descriptor, property)

def test_types::singletypes_has_string():
    assert hasattr(types::SingleTypes, "string")
    descriptor = None
    for klass in types::SingleTypes.__mro__:
        if "string" in klass.__dict__:
            descriptor = klass.__dict__["string"]
            break
    assert isinstance(descriptor, property)

def test_types::singletypes_has_date():
    assert hasattr(types::SingleTypes, "date")
    descriptor = None
    for klass in types::SingleTypes.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)

def test_types::singletypes_has_enum():
    assert hasattr(types::SingleTypes, "enum")
    descriptor = None
    for klass in types::SingleTypes.__mro__:
        if "enum" in klass.__dict__:
            descriptor = klass.__dict__["enum"]
            break
    assert isinstance(descriptor, property)

def test_types::singletypes_has_stringArray():
    assert hasattr(types::SingleTypes, "stringArray")
    descriptor = None
    for klass in types::SingleTypes.__mro__:
        if "stringArray" in klass.__dict__:
            descriptor = klass.__dict__["stringArray"]
            break
    assert isinstance(descriptor, property)

def test_types::singletypes_has_integerObject():
    assert hasattr(types::SingleTypes, "integerObject")
    descriptor = None
    for klass in types::SingleTypes.__mro__:
        if "integerObject" in klass.__dict__:
            descriptor = klass.__dict__["integerObject"]
            break
    assert isinstance(descriptor, property)

def test_types::singletypes_has_nextEnum():
    assert hasattr(types::SingleTypes, "nextEnum")
    descriptor = None
    for klass in types::SingleTypes.__mro__:
        if "nextEnum" in klass.__dict__:
            descriptor = klass.__dict__["nextEnum"]
            break
    assert isinstance(descriptor, property)

def test_types::singletypes_has_byte():
    assert hasattr(types::SingleTypes, "byte")
    descriptor = None
    for klass in types::SingleTypes.__mro__:
        if "byte" in klass.__dict__:
            descriptor = klass.__dict__["byte"]
            break
    assert isinstance(descriptor, property)

def test_types::singletypes_has_bigInteger():
    assert hasattr(types::SingleTypes, "bigInteger")
    descriptor = None
    for klass in types::SingleTypes.__mro__:
        if "bigInteger" in klass.__dict__:
            descriptor = klass.__dict__["bigInteger"]
            break
    assert isinstance(descriptor, property)

def test_types::singletypes_has_longArray():
    assert hasattr(types::SingleTypes, "longArray")
    descriptor = None
    for klass in types::SingleTypes.__mro__:
        if "longArray" in klass.__dict__:
            descriptor = klass.__dict__["longArray"]
            break
    assert isinstance(descriptor, property)

def test_types::singletypes_has_charObject():
    assert hasattr(types::SingleTypes, "charObject")
    descriptor = None
    for klass in types::SingleTypes.__mro__:
        if "charObject" in klass.__dict__:
            descriptor = klass.__dict__["charObject"]
            break
    assert isinstance(descriptor, property)

def test_types::singletypes_has_double():
    assert hasattr(types::SingleTypes, "double")
    descriptor = None
    for klass in types::SingleTypes.__mro__:
        if "double" in klass.__dict__:
            descriptor = klass.__dict__["double"]
            break
    assert isinstance(descriptor, property)

def test_types::singletypes_has_doubleObject():
    assert hasattr(types::SingleTypes, "doubleObject")
    descriptor = None
    for klass in types::SingleTypes.__mro__:
        if "doubleObject" in klass.__dict__:
            descriptor = klass.__dict__["doubleObject"]
            break
    assert isinstance(descriptor, property)

def test_types::singletypes_has_byteArray():
    assert hasattr(types::SingleTypes, "byteArray")
    descriptor = None
    for klass in types::SingleTypes.__mro__:
        if "byteArray" in klass.__dict__:
            descriptor = klass.__dict__["byteArray"]
            break
    assert isinstance(descriptor, property)

def test_types::singletypes_has_clazz():
    assert hasattr(types::SingleTypes, "clazz")
    descriptor = None
    for klass in types::SingleTypes.__mro__:
        if "clazz" in klass.__dict__:
            descriptor = klass.__dict__["clazz"]
            break
    assert isinstance(descriptor, property)

def test_types::singletypes_has_longObject():
    assert hasattr(types::SingleTypes, "longObject")
    descriptor = None
    for klass in types::SingleTypes.__mro__:
        if "longObject" in klass.__dict__:
            descriptor = klass.__dict__["longObject"]
            break
    assert isinstance(descriptor, property)

def test_types::singletypes_has_byteObject():
    assert hasattr(types::SingleTypes, "byteObject")
    descriptor = None
    for klass in types::SingleTypes.__mro__:
        if "byteObject" in klass.__dict__:
            descriptor = klass.__dict__["byteObject"]
            break
    assert isinstance(descriptor, property)

def test_types::singletypes_has_integer():
    assert hasattr(types::SingleTypes, "integer")
    descriptor = None
    for klass in types::SingleTypes.__mro__:
        if "integer" in klass.__dict__:
            descriptor = klass.__dict__["integer"]
            break
    assert isinstance(descriptor, property)

def test_types::singletypes_has_char():
    assert hasattr(types::SingleTypes, "char")
    descriptor = None
    for klass in types::SingleTypes.__mro__:
        if "char" in klass.__dict__:
            descriptor = klass.__dict__["char"]
            break
    assert isinstance(descriptor, property)

def test_testnextenum_exists():
    # Check that the Enumeration exists
    assert TestNextEnum is not None

def test_testnextenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TestNextEnum]
    expected_literals = [
        "Enum2",
        "Enum1",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TestNextEnum"

def test_testenum_exists():
    # Check that the Enumeration exists
    assert TestEnum is not None

def test_testenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TestEnum]
    expected_literals = [
        "Enum0",
        "Enum1",
        "Enum2",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TestEnum"


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
types::ManyTypes_strategy = st.builds(
    types::ManyTypes,
    enum=
        safe_text,
    longArray=
        safe_text,
    string=
        safe_text,
    byteObject=
        safe_text,
    charObject=
        safe_text,
    doubleObject=
        safe_text,
    integerObject=
        safe_text,
    byteArray=
        safe_text,
    stringArray=
        safe_text,
    bigInteger=
        safe_text,
    clazz=
        safe_text,
    long=
        safe_text,
    floatObject=
        safe_text,
    date=
        st.dates(),
    bigDecimal=
        safe_text
)
types::SingleTypes_strategy = st.builds(
    types::SingleTypes,
    floatObject=
        safe_text,
    long=
        safe_text,
    bigDecimal=
        safe_text,
    float=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    string=
        safe_text,
    date=
        st.dates(),
    enum=
        safe_text,
    stringArray=
        safe_text,
    integerObject=
        safe_text,
    nextEnum=
        safe_text,
    byte=
        safe_text,
    bigInteger=
        safe_text,
    longArray=
        safe_text,
    charObject=
        safe_text,
    double=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    doubleObject=
        safe_text,
    byteArray=
        safe_text,
    clazz=
        safe_text,
    longObject=
        safe_text,
    byteObject=
        safe_text,
    integer=
        st.integers(),
    char=
        safe_text
)

@given(instance=types::ManyTypes_strategy)
@settings(max_examples=50)
def test_types::manytypes_instantiation(instance):
    assert isinstance(instance, types::ManyTypes)

@given(instance=types::ManyTypes_strategy)
def test_types::manytypes_enum_type(instance):
    assert isinstance(instance.enum, str)


@given(instance=types::ManyTypes_strategy)
def test_types::manytypes_enum_setter(instance):
    original = instance.enum
    instance.enum = original
    assert instance.enum == original

@given(instance=types::ManyTypes_strategy)
def test_types::manytypes_longArray_type(instance):
    assert isinstance(instance.longArray, str)


@given(instance=types::ManyTypes_strategy)
def test_types::manytypes_longArray_setter(instance):
    original = instance.longArray
    instance.longArray = original
    assert instance.longArray == original

@given(instance=types::ManyTypes_strategy)
def test_types::manytypes_string_type(instance):
    assert isinstance(instance.string, str)


@given(instance=types::ManyTypes_strategy)
def test_types::manytypes_string_setter(instance):
    original = instance.string
    instance.string = original
    assert instance.string == original

@given(instance=types::ManyTypes_strategy)
def test_types::manytypes_byteObject_type(instance):
    assert isinstance(instance.byteObject, str)


@given(instance=types::ManyTypes_strategy)
def test_types::manytypes_byteObject_setter(instance):
    original = instance.byteObject
    instance.byteObject = original
    assert instance.byteObject == original

@given(instance=types::ManyTypes_strategy)
def test_types::manytypes_charObject_type(instance):
    assert isinstance(instance.charObject, str)


@given(instance=types::ManyTypes_strategy)
def test_types::manytypes_charObject_setter(instance):
    original = instance.charObject
    instance.charObject = original
    assert instance.charObject == original

@given(instance=types::ManyTypes_strategy)
def test_types::manytypes_doubleObject_type(instance):
    assert isinstance(instance.doubleObject, str)


@given(instance=types::ManyTypes_strategy)
def test_types::manytypes_doubleObject_setter(instance):
    original = instance.doubleObject
    instance.doubleObject = original
    assert instance.doubleObject == original

@given(instance=types::ManyTypes_strategy)
def test_types::manytypes_integerObject_type(instance):
    assert isinstance(instance.integerObject, str)


@given(instance=types::ManyTypes_strategy)
def test_types::manytypes_integerObject_setter(instance):
    original = instance.integerObject
    instance.integerObject = original
    assert instance.integerObject == original

@given(instance=types::ManyTypes_strategy)
def test_types::manytypes_byteArray_type(instance):
    assert isinstance(instance.byteArray, str)


@given(instance=types::ManyTypes_strategy)
def test_types::manytypes_byteArray_setter(instance):
    original = instance.byteArray
    instance.byteArray = original
    assert instance.byteArray == original

@given(instance=types::ManyTypes_strategy)
def test_types::manytypes_stringArray_type(instance):
    assert isinstance(instance.stringArray, str)


@given(instance=types::ManyTypes_strategy)
def test_types::manytypes_stringArray_setter(instance):
    original = instance.stringArray
    instance.stringArray = original
    assert instance.stringArray == original

@given(instance=types::ManyTypes_strategy)
def test_types::manytypes_bigInteger_type(instance):
    assert isinstance(instance.bigInteger, str)


@given(instance=types::ManyTypes_strategy)
def test_types::manytypes_bigInteger_setter(instance):
    original = instance.bigInteger
    instance.bigInteger = original
    assert instance.bigInteger == original

@given(instance=types::ManyTypes_strategy)
def test_types::manytypes_clazz_type(instance):
    assert isinstance(instance.clazz, str)


@given(instance=types::ManyTypes_strategy)
def test_types::manytypes_clazz_setter(instance):
    original = instance.clazz
    instance.clazz = original
    assert instance.clazz == original

@given(instance=types::ManyTypes_strategy)
def test_types::manytypes_long_type(instance):
    assert isinstance(instance.long, str)


@given(instance=types::ManyTypes_strategy)
def test_types::manytypes_long_setter(instance):
    original = instance.long
    instance.long = original
    assert instance.long == original

@given(instance=types::ManyTypes_strategy)
def test_types::manytypes_floatObject_type(instance):
    assert isinstance(instance.floatObject, str)


@given(instance=types::ManyTypes_strategy)
def test_types::manytypes_floatObject_setter(instance):
    original = instance.floatObject
    instance.floatObject = original
    assert instance.floatObject == original

@given(instance=types::ManyTypes_strategy)
def test_types::manytypes_date_type(instance):
    assert isinstance(instance.date, date)


@given(instance=types::ManyTypes_strategy)
def test_types::manytypes_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original

@given(instance=types::ManyTypes_strategy)
def test_types::manytypes_bigDecimal_type(instance):
    assert isinstance(instance.bigDecimal, str)


@given(instance=types::ManyTypes_strategy)
def test_types::manytypes_bigDecimal_setter(instance):
    original = instance.bigDecimal
    instance.bigDecimal = original
    assert instance.bigDecimal == original

@given(instance=types::SingleTypes_strategy)
@settings(max_examples=50)
def test_types::singletypes_instantiation(instance):
    assert isinstance(instance, types::SingleTypes)

@given(instance=types::SingleTypes_strategy)
def test_types::singletypes_floatObject_type(instance):
    assert isinstance(instance.floatObject, str)


@given(instance=types::SingleTypes_strategy)
def test_types::singletypes_floatObject_setter(instance):
    original = instance.floatObject
    instance.floatObject = original
    assert instance.floatObject == original

@given(instance=types::SingleTypes_strategy)
def test_types::singletypes_long_type(instance):
    assert isinstance(instance.long, str)


@given(instance=types::SingleTypes_strategy)
def test_types::singletypes_long_setter(instance):
    original = instance.long
    instance.long = original
    assert instance.long == original

@given(instance=types::SingleTypes_strategy)
def test_types::singletypes_bigDecimal_type(instance):
    assert isinstance(instance.bigDecimal, str)


@given(instance=types::SingleTypes_strategy)
def test_types::singletypes_bigDecimal_setter(instance):
    original = instance.bigDecimal
    instance.bigDecimal = original
    assert instance.bigDecimal == original

@given(instance=types::SingleTypes_strategy)
def test_types::singletypes_float_type(instance):
    assert isinstance(instance.float, float)


@given(instance=types::SingleTypes_strategy)
def test_types::singletypes_float_setter(instance):
    original = instance.float
    instance.float = original
    assert instance.float == original

@given(instance=types::SingleTypes_strategy)
def test_types::singletypes_string_type(instance):
    assert isinstance(instance.string, str)


@given(instance=types::SingleTypes_strategy)
def test_types::singletypes_string_setter(instance):
    original = instance.string
    instance.string = original
    assert instance.string == original

@given(instance=types::SingleTypes_strategy)
def test_types::singletypes_date_type(instance):
    assert isinstance(instance.date, date)


@given(instance=types::SingleTypes_strategy)
def test_types::singletypes_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original

@given(instance=types::SingleTypes_strategy)
def test_types::singletypes_enum_type(instance):
    assert isinstance(instance.enum, str)


@given(instance=types::SingleTypes_strategy)
def test_types::singletypes_enum_setter(instance):
    original = instance.enum
    instance.enum = original
    assert instance.enum == original

@given(instance=types::SingleTypes_strategy)
def test_types::singletypes_stringArray_type(instance):
    assert isinstance(instance.stringArray, str)


@given(instance=types::SingleTypes_strategy)
def test_types::singletypes_stringArray_setter(instance):
    original = instance.stringArray
    instance.stringArray = original
    assert instance.stringArray == original

@given(instance=types::SingleTypes_strategy)
def test_types::singletypes_integerObject_type(instance):
    assert isinstance(instance.integerObject, str)


@given(instance=types::SingleTypes_strategy)
def test_types::singletypes_integerObject_setter(instance):
    original = instance.integerObject
    instance.integerObject = original
    assert instance.integerObject == original

@given(instance=types::SingleTypes_strategy)
def test_types::singletypes_nextEnum_type(instance):
    assert isinstance(instance.nextEnum, str)


@given(instance=types::SingleTypes_strategy)
def test_types::singletypes_nextEnum_setter(instance):
    original = instance.nextEnum
    instance.nextEnum = original
    assert instance.nextEnum == original

@given(instance=types::SingleTypes_strategy)
def test_types::singletypes_byte_type(instance):
    assert isinstance(instance.byte, str)


@given(instance=types::SingleTypes_strategy)
def test_types::singletypes_byte_setter(instance):
    original = instance.byte
    instance.byte = original
    assert instance.byte == original

@given(instance=types::SingleTypes_strategy)
def test_types::singletypes_bigInteger_type(instance):
    assert isinstance(instance.bigInteger, str)


@given(instance=types::SingleTypes_strategy)
def test_types::singletypes_bigInteger_setter(instance):
    original = instance.bigInteger
    instance.bigInteger = original
    assert instance.bigInteger == original

@given(instance=types::SingleTypes_strategy)
def test_types::singletypes_longArray_type(instance):
    assert isinstance(instance.longArray, str)


@given(instance=types::SingleTypes_strategy)
def test_types::singletypes_longArray_setter(instance):
    original = instance.longArray
    instance.longArray = original
    assert instance.longArray == original

@given(instance=types::SingleTypes_strategy)
def test_types::singletypes_charObject_type(instance):
    assert isinstance(instance.charObject, str)


@given(instance=types::SingleTypes_strategy)
def test_types::singletypes_charObject_setter(instance):
    original = instance.charObject
    instance.charObject = original
    assert instance.charObject == original

@given(instance=types::SingleTypes_strategy)
def test_types::singletypes_double_type(instance):
    assert isinstance(instance.double, float)


@given(instance=types::SingleTypes_strategy)
def test_types::singletypes_double_setter(instance):
    original = instance.double
    instance.double = original
    assert instance.double == original

@given(instance=types::SingleTypes_strategy)
def test_types::singletypes_doubleObject_type(instance):
    assert isinstance(instance.doubleObject, str)


@given(instance=types::SingleTypes_strategy)
def test_types::singletypes_doubleObject_setter(instance):
    original = instance.doubleObject
    instance.doubleObject = original
    assert instance.doubleObject == original

@given(instance=types::SingleTypes_strategy)
def test_types::singletypes_byteArray_type(instance):
    assert isinstance(instance.byteArray, str)


@given(instance=types::SingleTypes_strategy)
def test_types::singletypes_byteArray_setter(instance):
    original = instance.byteArray
    instance.byteArray = original
    assert instance.byteArray == original

@given(instance=types::SingleTypes_strategy)
def test_types::singletypes_clazz_type(instance):
    assert isinstance(instance.clazz, str)


@given(instance=types::SingleTypes_strategy)
def test_types::singletypes_clazz_setter(instance):
    original = instance.clazz
    instance.clazz = original
    assert instance.clazz == original

@given(instance=types::SingleTypes_strategy)
def test_types::singletypes_longObject_type(instance):
    assert isinstance(instance.longObject, str)


@given(instance=types::SingleTypes_strategy)
def test_types::singletypes_longObject_setter(instance):
    original = instance.longObject
    instance.longObject = original
    assert instance.longObject == original

@given(instance=types::SingleTypes_strategy)
def test_types::singletypes_byteObject_type(instance):
    assert isinstance(instance.byteObject, str)


@given(instance=types::SingleTypes_strategy)
def test_types::singletypes_byteObject_setter(instance):
    original = instance.byteObject
    instance.byteObject = original
    assert instance.byteObject == original

@given(instance=types::SingleTypes_strategy)
def test_types::singletypes_integer_type(instance):
    assert isinstance(instance.integer, int)


@given(instance=types::SingleTypes_strategy)
def test_types::singletypes_integer_setter(instance):
    original = instance.integer
    instance.integer = original
    assert instance.integer == original

@given(instance=types::SingleTypes_strategy)
def test_types::singletypes_char_type(instance):
    assert isinstance(instance.char, str)


@given(instance=types::SingleTypes_strategy)
def test_types::singletypes_char_setter(instance):
    original = instance.char
    instance.char = original
    assert instance.char == original
