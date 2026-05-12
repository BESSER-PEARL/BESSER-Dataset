import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    types_ManyTypes,
    types_SingleTypes,
    TestEnum,
    TestNextEnum,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_types_manytypes_is_not_abstract():
    assert not inspect.isabstract(types_ManyTypes)


def test_types_manytypes_constructor_exists():
    assert callable(types_ManyTypes.__init__)


def test_types_manytypes_constructor_args():
    sig = inspect.signature(types_ManyTypes.__init__)
    params = list(sig.parameters.keys())
    assert "enum" in params, "Missing parameter 'enum'"
    assert "floatObject" in params, "Missing parameter 'floatObject'"
    assert "long" in params, "Missing parameter 'long'"
    assert "stringArray" in params, "Missing parameter 'stringArray'"
    assert "longArray" in params, "Missing parameter 'longArray'"
    assert "date" in params, "Missing parameter 'date'"
    assert "byteArray" in params, "Missing parameter 'byteArray'"
    assert "integerObject" in params, "Missing parameter 'integerObject'"
    assert "charObject" in params, "Missing parameter 'charObject'"
    assert "string" in params, "Missing parameter 'string'"
    assert "doubleObject" in params, "Missing parameter 'doubleObject'"
    assert "clazz" in params, "Missing parameter 'clazz'"
    assert "byteObject" in params, "Missing parameter 'byteObject'"
    assert "bigDecimal" in params, "Missing parameter 'bigDecimal'"
    assert "bigInteger" in params, "Missing parameter 'bigInteger'"

def test_types_manytypes_has_enum():
    assert hasattr(types_ManyTypes, "enum")
    descriptor = None
    for klass in types_ManyTypes.__mro__:
        if "enum" in klass.__dict__:
            descriptor = klass.__dict__["enum"]
            break
    assert isinstance(descriptor, property)

def test_types_manytypes_has_floatObject():
    assert hasattr(types_ManyTypes, "floatObject")
    descriptor = None
    for klass in types_ManyTypes.__mro__:
        if "floatObject" in klass.__dict__:
            descriptor = klass.__dict__["floatObject"]
            break
    assert isinstance(descriptor, property)

def test_types_manytypes_has_long():
    assert hasattr(types_ManyTypes, "long")
    descriptor = None
    for klass in types_ManyTypes.__mro__:
        if "long" in klass.__dict__:
            descriptor = klass.__dict__["long"]
            break
    assert isinstance(descriptor, property)

def test_types_manytypes_has_stringArray():
    assert hasattr(types_ManyTypes, "stringArray")
    descriptor = None
    for klass in types_ManyTypes.__mro__:
        if "stringArray" in klass.__dict__:
            descriptor = klass.__dict__["stringArray"]
            break
    assert isinstance(descriptor, property)

def test_types_manytypes_has_longArray():
    assert hasattr(types_ManyTypes, "longArray")
    descriptor = None
    for klass in types_ManyTypes.__mro__:
        if "longArray" in klass.__dict__:
            descriptor = klass.__dict__["longArray"]
            break
    assert isinstance(descriptor, property)

def test_types_manytypes_has_date():
    assert hasattr(types_ManyTypes, "date")
    descriptor = None
    for klass in types_ManyTypes.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)

def test_types_manytypes_has_byteArray():
    assert hasattr(types_ManyTypes, "byteArray")
    descriptor = None
    for klass in types_ManyTypes.__mro__:
        if "byteArray" in klass.__dict__:
            descriptor = klass.__dict__["byteArray"]
            break
    assert isinstance(descriptor, property)

def test_types_manytypes_has_integerObject():
    assert hasattr(types_ManyTypes, "integerObject")
    descriptor = None
    for klass in types_ManyTypes.__mro__:
        if "integerObject" in klass.__dict__:
            descriptor = klass.__dict__["integerObject"]
            break
    assert isinstance(descriptor, property)

def test_types_manytypes_has_charObject():
    assert hasattr(types_ManyTypes, "charObject")
    descriptor = None
    for klass in types_ManyTypes.__mro__:
        if "charObject" in klass.__dict__:
            descriptor = klass.__dict__["charObject"]
            break
    assert isinstance(descriptor, property)

def test_types_manytypes_has_string():
    assert hasattr(types_ManyTypes, "string")
    descriptor = None
    for klass in types_ManyTypes.__mro__:
        if "string" in klass.__dict__:
            descriptor = klass.__dict__["string"]
            break
    assert isinstance(descriptor, property)

def test_types_manytypes_has_doubleObject():
    assert hasattr(types_ManyTypes, "doubleObject")
    descriptor = None
    for klass in types_ManyTypes.__mro__:
        if "doubleObject" in klass.__dict__:
            descriptor = klass.__dict__["doubleObject"]
            break
    assert isinstance(descriptor, property)

def test_types_manytypes_has_clazz():
    assert hasattr(types_ManyTypes, "clazz")
    descriptor = None
    for klass in types_ManyTypes.__mro__:
        if "clazz" in klass.__dict__:
            descriptor = klass.__dict__["clazz"]
            break
    assert isinstance(descriptor, property)

def test_types_manytypes_has_byteObject():
    assert hasattr(types_ManyTypes, "byteObject")
    descriptor = None
    for klass in types_ManyTypes.__mro__:
        if "byteObject" in klass.__dict__:
            descriptor = klass.__dict__["byteObject"]
            break
    assert isinstance(descriptor, property)

def test_types_manytypes_has_bigDecimal():
    assert hasattr(types_ManyTypes, "bigDecimal")
    descriptor = None
    for klass in types_ManyTypes.__mro__:
        if "bigDecimal" in klass.__dict__:
            descriptor = klass.__dict__["bigDecimal"]
            break
    assert isinstance(descriptor, property)

def test_types_manytypes_has_bigInteger():
    assert hasattr(types_ManyTypes, "bigInteger")
    descriptor = None
    for klass in types_ManyTypes.__mro__:
        if "bigInteger" in klass.__dict__:
            descriptor = klass.__dict__["bigInteger"]
            break
    assert isinstance(descriptor, property)



def test_types_singletypes_is_not_abstract():
    assert not inspect.isabstract(types_SingleTypes)


def test_types_singletypes_constructor_exists():
    assert callable(types_SingleTypes.__init__)


def test_types_singletypes_constructor_args():
    sig = inspect.signature(types_SingleTypes.__init__)
    params = list(sig.parameters.keys())
    assert "longArray" in params, "Missing parameter 'longArray'"
    assert "doubleObject" in params, "Missing parameter 'doubleObject'"
    assert "byteArray" in params, "Missing parameter 'byteArray'"
    assert "byte" in params, "Missing parameter 'byte'"
    assert "long" in params, "Missing parameter 'long'"
    assert "charObject" in params, "Missing parameter 'charObject'"
    assert "float" in params, "Missing parameter 'float'"
    assert "date" in params, "Missing parameter 'date'"
    assert "longObject" in params, "Missing parameter 'longObject'"
    assert "nextEnum" in params, "Missing parameter 'nextEnum'"
    assert "byteObject" in params, "Missing parameter 'byteObject'"
    assert "stringArray" in params, "Missing parameter 'stringArray'"
    assert "integerObject" in params, "Missing parameter 'integerObject'"
    assert "enum" in params, "Missing parameter 'enum'"
    assert "double" in params, "Missing parameter 'double'"
    assert "bigDecimal" in params, "Missing parameter 'bigDecimal'"
    assert "floatObject" in params, "Missing parameter 'floatObject'"
    assert "integer" in params, "Missing parameter 'integer'"
    assert "bigInteger" in params, "Missing parameter 'bigInteger'"
    assert "string" in params, "Missing parameter 'string'"
    assert "char" in params, "Missing parameter 'char'"
    assert "clazz" in params, "Missing parameter 'clazz'"

def test_types_singletypes_has_longArray():
    assert hasattr(types_SingleTypes, "longArray")
    descriptor = None
    for klass in types_SingleTypes.__mro__:
        if "longArray" in klass.__dict__:
            descriptor = klass.__dict__["longArray"]
            break
    assert isinstance(descriptor, property)

def test_types_singletypes_has_doubleObject():
    assert hasattr(types_SingleTypes, "doubleObject")
    descriptor = None
    for klass in types_SingleTypes.__mro__:
        if "doubleObject" in klass.__dict__:
            descriptor = klass.__dict__["doubleObject"]
            break
    assert isinstance(descriptor, property)

def test_types_singletypes_has_byteArray():
    assert hasattr(types_SingleTypes, "byteArray")
    descriptor = None
    for klass in types_SingleTypes.__mro__:
        if "byteArray" in klass.__dict__:
            descriptor = klass.__dict__["byteArray"]
            break
    assert isinstance(descriptor, property)

def test_types_singletypes_has_byte():
    assert hasattr(types_SingleTypes, "byte")
    descriptor = None
    for klass in types_SingleTypes.__mro__:
        if "byte" in klass.__dict__:
            descriptor = klass.__dict__["byte"]
            break
    assert isinstance(descriptor, property)

def test_types_singletypes_has_long():
    assert hasattr(types_SingleTypes, "long")
    descriptor = None
    for klass in types_SingleTypes.__mro__:
        if "long" in klass.__dict__:
            descriptor = klass.__dict__["long"]
            break
    assert isinstance(descriptor, property)

def test_types_singletypes_has_charObject():
    assert hasattr(types_SingleTypes, "charObject")
    descriptor = None
    for klass in types_SingleTypes.__mro__:
        if "charObject" in klass.__dict__:
            descriptor = klass.__dict__["charObject"]
            break
    assert isinstance(descriptor, property)

def test_types_singletypes_has_float():
    assert hasattr(types_SingleTypes, "float")
    descriptor = None
    for klass in types_SingleTypes.__mro__:
        if "float" in klass.__dict__:
            descriptor = klass.__dict__["float"]
            break
    assert isinstance(descriptor, property)

def test_types_singletypes_has_date():
    assert hasattr(types_SingleTypes, "date")
    descriptor = None
    for klass in types_SingleTypes.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)

def test_types_singletypes_has_longObject():
    assert hasattr(types_SingleTypes, "longObject")
    descriptor = None
    for klass in types_SingleTypes.__mro__:
        if "longObject" in klass.__dict__:
            descriptor = klass.__dict__["longObject"]
            break
    assert isinstance(descriptor, property)

def test_types_singletypes_has_nextEnum():
    assert hasattr(types_SingleTypes, "nextEnum")
    descriptor = None
    for klass in types_SingleTypes.__mro__:
        if "nextEnum" in klass.__dict__:
            descriptor = klass.__dict__["nextEnum"]
            break
    assert isinstance(descriptor, property)

def test_types_singletypes_has_byteObject():
    assert hasattr(types_SingleTypes, "byteObject")
    descriptor = None
    for klass in types_SingleTypes.__mro__:
        if "byteObject" in klass.__dict__:
            descriptor = klass.__dict__["byteObject"]
            break
    assert isinstance(descriptor, property)

def test_types_singletypes_has_stringArray():
    assert hasattr(types_SingleTypes, "stringArray")
    descriptor = None
    for klass in types_SingleTypes.__mro__:
        if "stringArray" in klass.__dict__:
            descriptor = klass.__dict__["stringArray"]
            break
    assert isinstance(descriptor, property)

def test_types_singletypes_has_integerObject():
    assert hasattr(types_SingleTypes, "integerObject")
    descriptor = None
    for klass in types_SingleTypes.__mro__:
        if "integerObject" in klass.__dict__:
            descriptor = klass.__dict__["integerObject"]
            break
    assert isinstance(descriptor, property)

def test_types_singletypes_has_enum():
    assert hasattr(types_SingleTypes, "enum")
    descriptor = None
    for klass in types_SingleTypes.__mro__:
        if "enum" in klass.__dict__:
            descriptor = klass.__dict__["enum"]
            break
    assert isinstance(descriptor, property)

def test_types_singletypes_has_double():
    assert hasattr(types_SingleTypes, "double")
    descriptor = None
    for klass in types_SingleTypes.__mro__:
        if "double" in klass.__dict__:
            descriptor = klass.__dict__["double"]
            break
    assert isinstance(descriptor, property)

def test_types_singletypes_has_bigDecimal():
    assert hasattr(types_SingleTypes, "bigDecimal")
    descriptor = None
    for klass in types_SingleTypes.__mro__:
        if "bigDecimal" in klass.__dict__:
            descriptor = klass.__dict__["bigDecimal"]
            break
    assert isinstance(descriptor, property)

def test_types_singletypes_has_floatObject():
    assert hasattr(types_SingleTypes, "floatObject")
    descriptor = None
    for klass in types_SingleTypes.__mro__:
        if "floatObject" in klass.__dict__:
            descriptor = klass.__dict__["floatObject"]
            break
    assert isinstance(descriptor, property)

def test_types_singletypes_has_integer():
    assert hasattr(types_SingleTypes, "integer")
    descriptor = None
    for klass in types_SingleTypes.__mro__:
        if "integer" in klass.__dict__:
            descriptor = klass.__dict__["integer"]
            break
    assert isinstance(descriptor, property)

def test_types_singletypes_has_bigInteger():
    assert hasattr(types_SingleTypes, "bigInteger")
    descriptor = None
    for klass in types_SingleTypes.__mro__:
        if "bigInteger" in klass.__dict__:
            descriptor = klass.__dict__["bigInteger"]
            break
    assert isinstance(descriptor, property)

def test_types_singletypes_has_string():
    assert hasattr(types_SingleTypes, "string")
    descriptor = None
    for klass in types_SingleTypes.__mro__:
        if "string" in klass.__dict__:
            descriptor = klass.__dict__["string"]
            break
    assert isinstance(descriptor, property)

def test_types_singletypes_has_char():
    assert hasattr(types_SingleTypes, "char")
    descriptor = None
    for klass in types_SingleTypes.__mro__:
        if "char" in klass.__dict__:
            descriptor = klass.__dict__["char"]
            break
    assert isinstance(descriptor, property)

def test_types_singletypes_has_clazz():
    assert hasattr(types_SingleTypes, "clazz")
    descriptor = None
    for klass in types_SingleTypes.__mro__:
        if "clazz" in klass.__dict__:
            descriptor = klass.__dict__["clazz"]
            break
    assert isinstance(descriptor, property)

def test_testenum_exists():
    # Check that the Enumeration exists
    assert TestEnum is not None

def test_testenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TestEnum]
    expected_literals = [
        "Enum0",
        "Enum2",
        "Enum1",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TestEnum"

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
types_ManyTypes_strategy = st.builds(
    types_ManyTypes,
    enum=
        safe_text,
    floatObject=
        safe_text,
    long=
        safe_text,
    stringArray=
        safe_text,
    longArray=
        safe_text,
    date=
        st.dates(),
    byteArray=
        safe_text,
    integerObject=
        safe_text,
    charObject=
        safe_text,
    string=
        safe_text,
    doubleObject=
        safe_text,
    clazz=
        safe_text,
    byteObject=
        safe_text,
    bigDecimal=
        safe_text,
    bigInteger=
        safe_text
)
types_SingleTypes_strategy = st.builds(
    types_SingleTypes,
    longArray=
        safe_text,
    doubleObject=
        safe_text,
    byteArray=
        safe_text,
    byte=
        safe_text,
    long=
        safe_text,
    charObject=
        safe_text,
    float=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    date=
        st.dates(),
    longObject=
        safe_text,
    nextEnum=
        safe_text,
    byteObject=
        safe_text,
    stringArray=
        safe_text,
    integerObject=
        safe_text,
    enum=
        safe_text,
    double=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    bigDecimal=
        safe_text,
    floatObject=
        safe_text,
    integer=
        st.integers(),
    bigInteger=
        safe_text,
    string=
        safe_text,
    char=
        safe_text,
    clazz=
        safe_text
)

@given(instance=types_ManyTypes_strategy)
@settings(max_examples=50)
def test_types_manytypes_instantiation(instance):
    assert isinstance(instance, types_ManyTypes)



@given(instance=types_ManyTypes_strategy)
def test_types_manytypes_enum_setter(instance):
    original = instance.enum
    instance.enum = original
    assert instance.enum == original



@given(instance=types_ManyTypes_strategy)
def test_types_manytypes_floatObject_setter(instance):
    original = instance.floatObject
    instance.floatObject = original
    assert instance.floatObject == original



@given(instance=types_ManyTypes_strategy)
def test_types_manytypes_long_setter(instance):
    original = instance.long
    instance.long = original
    assert instance.long == original



@given(instance=types_ManyTypes_strategy)
def test_types_manytypes_stringArray_setter(instance):
    original = instance.stringArray
    instance.stringArray = original
    assert instance.stringArray == original



@given(instance=types_ManyTypes_strategy)
def test_types_manytypes_longArray_setter(instance):
    original = instance.longArray
    instance.longArray = original
    assert instance.longArray == original



@given(instance=types_ManyTypes_strategy)
def test_types_manytypes_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original



@given(instance=types_ManyTypes_strategy)
def test_types_manytypes_byteArray_setter(instance):
    original = instance.byteArray
    instance.byteArray = original
    assert instance.byteArray == original



@given(instance=types_ManyTypes_strategy)
def test_types_manytypes_integerObject_setter(instance):
    original = instance.integerObject
    instance.integerObject = original
    assert instance.integerObject == original



@given(instance=types_ManyTypes_strategy)
def test_types_manytypes_charObject_setter(instance):
    original = instance.charObject
    instance.charObject = original
    assert instance.charObject == original



@given(instance=types_ManyTypes_strategy)
def test_types_manytypes_string_setter(instance):
    original = instance.string
    instance.string = original
    assert instance.string == original



@given(instance=types_ManyTypes_strategy)
def test_types_manytypes_doubleObject_setter(instance):
    original = instance.doubleObject
    instance.doubleObject = original
    assert instance.doubleObject == original



@given(instance=types_ManyTypes_strategy)
def test_types_manytypes_clazz_setter(instance):
    original = instance.clazz
    instance.clazz = original
    assert instance.clazz == original



@given(instance=types_ManyTypes_strategy)
def test_types_manytypes_byteObject_setter(instance):
    original = instance.byteObject
    instance.byteObject = original
    assert instance.byteObject == original



@given(instance=types_ManyTypes_strategy)
def test_types_manytypes_bigDecimal_setter(instance):
    original = instance.bigDecimal
    instance.bigDecimal = original
    assert instance.bigDecimal == original



@given(instance=types_ManyTypes_strategy)
def test_types_manytypes_bigInteger_setter(instance):
    original = instance.bigInteger
    instance.bigInteger = original
    assert instance.bigInteger == original

@given(instance=types_SingleTypes_strategy)
@settings(max_examples=50)
def test_types_singletypes_instantiation(instance):
    assert isinstance(instance, types_SingleTypes)



@given(instance=types_SingleTypes_strategy)
def test_types_singletypes_longArray_setter(instance):
    original = instance.longArray
    instance.longArray = original
    assert instance.longArray == original



@given(instance=types_SingleTypes_strategy)
def test_types_singletypes_doubleObject_setter(instance):
    original = instance.doubleObject
    instance.doubleObject = original
    assert instance.doubleObject == original



@given(instance=types_SingleTypes_strategy)
def test_types_singletypes_byteArray_setter(instance):
    original = instance.byteArray
    instance.byteArray = original
    assert instance.byteArray == original



@given(instance=types_SingleTypes_strategy)
def test_types_singletypes_byte_setter(instance):
    original = instance.byte
    instance.byte = original
    assert instance.byte == original



@given(instance=types_SingleTypes_strategy)
def test_types_singletypes_long_setter(instance):
    original = instance.long
    instance.long = original
    assert instance.long == original



@given(instance=types_SingleTypes_strategy)
def test_types_singletypes_charObject_setter(instance):
    original = instance.charObject
    instance.charObject = original
    assert instance.charObject == original



@given(instance=types_SingleTypes_strategy)
def test_types_singletypes_float_setter(instance):
    original = instance.float
    instance.float = original
    assert instance.float == original



@given(instance=types_SingleTypes_strategy)
def test_types_singletypes_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original



@given(instance=types_SingleTypes_strategy)
def test_types_singletypes_longObject_setter(instance):
    original = instance.longObject
    instance.longObject = original
    assert instance.longObject == original



@given(instance=types_SingleTypes_strategy)
def test_types_singletypes_nextEnum_setter(instance):
    original = instance.nextEnum
    instance.nextEnum = original
    assert instance.nextEnum == original



@given(instance=types_SingleTypes_strategy)
def test_types_singletypes_byteObject_setter(instance):
    original = instance.byteObject
    instance.byteObject = original
    assert instance.byteObject == original



@given(instance=types_SingleTypes_strategy)
def test_types_singletypes_stringArray_setter(instance):
    original = instance.stringArray
    instance.stringArray = original
    assert instance.stringArray == original



@given(instance=types_SingleTypes_strategy)
def test_types_singletypes_integerObject_setter(instance):
    original = instance.integerObject
    instance.integerObject = original
    assert instance.integerObject == original



@given(instance=types_SingleTypes_strategy)
def test_types_singletypes_enum_setter(instance):
    original = instance.enum
    instance.enum = original
    assert instance.enum == original



@given(instance=types_SingleTypes_strategy)
def test_types_singletypes_double_setter(instance):
    original = instance.double
    instance.double = original
    assert instance.double == original



@given(instance=types_SingleTypes_strategy)
def test_types_singletypes_bigDecimal_setter(instance):
    original = instance.bigDecimal
    instance.bigDecimal = original
    assert instance.bigDecimal == original



@given(instance=types_SingleTypes_strategy)
def test_types_singletypes_floatObject_setter(instance):
    original = instance.floatObject
    instance.floatObject = original
    assert instance.floatObject == original



@given(instance=types_SingleTypes_strategy)
def test_types_singletypes_integer_setter(instance):
    original = instance.integer
    instance.integer = original
    assert instance.integer == original



@given(instance=types_SingleTypes_strategy)
def test_types_singletypes_bigInteger_setter(instance):
    original = instance.bigInteger
    instance.bigInteger = original
    assert instance.bigInteger == original



@given(instance=types_SingleTypes_strategy)
def test_types_singletypes_string_setter(instance):
    original = instance.string
    instance.string = original
    assert instance.string == original



@given(instance=types_SingleTypes_strategy)
def test_types_singletypes_char_setter(instance):
    original = instance.char
    instance.char = original
    assert instance.char == original



@given(instance=types_SingleTypes_strategy)
def test_types_singletypes_clazz_setter(instance):
    original = instance.clazz
    instance.clazz = original
    assert instance.clazz == original
