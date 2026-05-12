import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    attributeTest_Root,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_attributetest_root_is_not_abstract():
    assert not inspect.isabstract(attributeTest_Root)


def test_attributetest_root_constructor_exists():
    assert callable(attributeTest_Root.__init__)


def test_attributetest_root_constructor_args():
    sig = inspect.signature(attributeTest_Root.__init__)
    params = list(sig.parameters.keys())
    assert "listShort" in params, "Missing parameter 'listShort'"
    assert "byteObj" in params, "Missing parameter 'byteObj'"
    assert "stringObj" in params, "Missing parameter 'stringObj'"
    assert "doublePrimitive" in params, "Missing parameter 'doublePrimitive'"
    assert "charPrimitive" in params, "Missing parameter 'charPrimitive'"
    assert "date" in params, "Missing parameter 'date'"
    assert "eList" in params, "Missing parameter 'eList'"
    assert "charObj" in params, "Missing parameter 'charObj'"
    assert "boolObj" in params, "Missing parameter 'boolObj'"
    assert "boolPrimitive" in params, "Missing parameter 'boolPrimitive'"
    assert "floatPrimitive" in params, "Missing parameter 'floatPrimitive'"
    assert "shortObj" in params, "Missing parameter 'shortObj'"
    assert "doubleObj" in params, "Missing parameter 'doubleObj'"
    assert "listInt1" in params, "Missing parameter 'listInt1'"
    assert "floatObj" in params, "Missing parameter 'floatObj'"
    assert "bigInteger" in params, "Missing parameter 'bigInteger'"
    assert "intObj" in params, "Missing parameter 'intObj'"
    assert "longObj" in params, "Missing parameter 'longObj'"
    assert "listString" in params, "Missing parameter 'listString'"
    assert "bigDecimal" in params, "Missing parameter 'bigDecimal'"
    assert "byteArray" in params, "Missing parameter 'byteArray'"
    assert "javaObject" in params, "Missing parameter 'javaObject'"
    assert "shortPrimitive" in params, "Missing parameter 'shortPrimitive'"
    assert "longPrimitive" in params, "Missing parameter 'longPrimitive'"
    assert "bytePrimitive" in params, "Missing parameter 'bytePrimitive'"
    assert "intPrimitive" in params, "Missing parameter 'intPrimitive'"
    assert "map" in params, "Missing parameter 'map'"
    assert "listInt2" in params, "Missing parameter 'listInt2'"
    assert "listInt" in params, "Missing parameter 'listInt'"

def test_attributetest_root_has_listShort():
    assert hasattr(attributeTest_Root, "listShort")
    descriptor = None
    for klass in attributeTest_Root.__mro__:
        if "listShort" in klass.__dict__:
            descriptor = klass.__dict__["listShort"]
            break
    assert isinstance(descriptor, property)

def test_attributetest_root_has_byteObj():
    assert hasattr(attributeTest_Root, "byteObj")
    descriptor = None
    for klass in attributeTest_Root.__mro__:
        if "byteObj" in klass.__dict__:
            descriptor = klass.__dict__["byteObj"]
            break
    assert isinstance(descriptor, property)

def test_attributetest_root_has_stringObj():
    assert hasattr(attributeTest_Root, "stringObj")
    descriptor = None
    for klass in attributeTest_Root.__mro__:
        if "stringObj" in klass.__dict__:
            descriptor = klass.__dict__["stringObj"]
            break
    assert isinstance(descriptor, property)

def test_attributetest_root_has_doublePrimitive():
    assert hasattr(attributeTest_Root, "doublePrimitive")
    descriptor = None
    for klass in attributeTest_Root.__mro__:
        if "doublePrimitive" in klass.__dict__:
            descriptor = klass.__dict__["doublePrimitive"]
            break
    assert isinstance(descriptor, property)

def test_attributetest_root_has_charPrimitive():
    assert hasattr(attributeTest_Root, "charPrimitive")
    descriptor = None
    for klass in attributeTest_Root.__mro__:
        if "charPrimitive" in klass.__dict__:
            descriptor = klass.__dict__["charPrimitive"]
            break
    assert isinstance(descriptor, property)

def test_attributetest_root_has_date():
    assert hasattr(attributeTest_Root, "date")
    descriptor = None
    for klass in attributeTest_Root.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)

def test_attributetest_root_has_eList():
    assert hasattr(attributeTest_Root, "eList")
    descriptor = None
    for klass in attributeTest_Root.__mro__:
        if "eList" in klass.__dict__:
            descriptor = klass.__dict__["eList"]
            break
    assert isinstance(descriptor, property)

def test_attributetest_root_has_charObj():
    assert hasattr(attributeTest_Root, "charObj")
    descriptor = None
    for klass in attributeTest_Root.__mro__:
        if "charObj" in klass.__dict__:
            descriptor = klass.__dict__["charObj"]
            break
    assert isinstance(descriptor, property)

def test_attributetest_root_has_boolObj():
    assert hasattr(attributeTest_Root, "boolObj")
    descriptor = None
    for klass in attributeTest_Root.__mro__:
        if "boolObj" in klass.__dict__:
            descriptor = klass.__dict__["boolObj"]
            break
    assert isinstance(descriptor, property)

def test_attributetest_root_has_boolPrimitive():
    assert hasattr(attributeTest_Root, "boolPrimitive")
    descriptor = None
    for klass in attributeTest_Root.__mro__:
        if "boolPrimitive" in klass.__dict__:
            descriptor = klass.__dict__["boolPrimitive"]
            break
    assert isinstance(descriptor, property)

def test_attributetest_root_has_floatPrimitive():
    assert hasattr(attributeTest_Root, "floatPrimitive")
    descriptor = None
    for klass in attributeTest_Root.__mro__:
        if "floatPrimitive" in klass.__dict__:
            descriptor = klass.__dict__["floatPrimitive"]
            break
    assert isinstance(descriptor, property)

def test_attributetest_root_has_shortObj():
    assert hasattr(attributeTest_Root, "shortObj")
    descriptor = None
    for klass in attributeTest_Root.__mro__:
        if "shortObj" in klass.__dict__:
            descriptor = klass.__dict__["shortObj"]
            break
    assert isinstance(descriptor, property)

def test_attributetest_root_has_doubleObj():
    assert hasattr(attributeTest_Root, "doubleObj")
    descriptor = None
    for klass in attributeTest_Root.__mro__:
        if "doubleObj" in klass.__dict__:
            descriptor = klass.__dict__["doubleObj"]
            break
    assert isinstance(descriptor, property)

def test_attributetest_root_has_listInt1():
    assert hasattr(attributeTest_Root, "listInt1")
    descriptor = None
    for klass in attributeTest_Root.__mro__:
        if "listInt1" in klass.__dict__:
            descriptor = klass.__dict__["listInt1"]
            break
    assert isinstance(descriptor, property)

def test_attributetest_root_has_floatObj():
    assert hasattr(attributeTest_Root, "floatObj")
    descriptor = None
    for klass in attributeTest_Root.__mro__:
        if "floatObj" in klass.__dict__:
            descriptor = klass.__dict__["floatObj"]
            break
    assert isinstance(descriptor, property)

def test_attributetest_root_has_bigInteger():
    assert hasattr(attributeTest_Root, "bigInteger")
    descriptor = None
    for klass in attributeTest_Root.__mro__:
        if "bigInteger" in klass.__dict__:
            descriptor = klass.__dict__["bigInteger"]
            break
    assert isinstance(descriptor, property)

def test_attributetest_root_has_intObj():
    assert hasattr(attributeTest_Root, "intObj")
    descriptor = None
    for klass in attributeTest_Root.__mro__:
        if "intObj" in klass.__dict__:
            descriptor = klass.__dict__["intObj"]
            break
    assert isinstance(descriptor, property)

def test_attributetest_root_has_longObj():
    assert hasattr(attributeTest_Root, "longObj")
    descriptor = None
    for klass in attributeTest_Root.__mro__:
        if "longObj" in klass.__dict__:
            descriptor = klass.__dict__["longObj"]
            break
    assert isinstance(descriptor, property)

def test_attributetest_root_has_listString():
    assert hasattr(attributeTest_Root, "listString")
    descriptor = None
    for klass in attributeTest_Root.__mro__:
        if "listString" in klass.__dict__:
            descriptor = klass.__dict__["listString"]
            break
    assert isinstance(descriptor, property)

def test_attributetest_root_has_bigDecimal():
    assert hasattr(attributeTest_Root, "bigDecimal")
    descriptor = None
    for klass in attributeTest_Root.__mro__:
        if "bigDecimal" in klass.__dict__:
            descriptor = klass.__dict__["bigDecimal"]
            break
    assert isinstance(descriptor, property)

def test_attributetest_root_has_byteArray():
    assert hasattr(attributeTest_Root, "byteArray")
    descriptor = None
    for klass in attributeTest_Root.__mro__:
        if "byteArray" in klass.__dict__:
            descriptor = klass.__dict__["byteArray"]
            break
    assert isinstance(descriptor, property)

def test_attributetest_root_has_javaObject():
    assert hasattr(attributeTest_Root, "javaObject")
    descriptor = None
    for klass in attributeTest_Root.__mro__:
        if "javaObject" in klass.__dict__:
            descriptor = klass.__dict__["javaObject"]
            break
    assert isinstance(descriptor, property)

def test_attributetest_root_has_shortPrimitive():
    assert hasattr(attributeTest_Root, "shortPrimitive")
    descriptor = None
    for klass in attributeTest_Root.__mro__:
        if "shortPrimitive" in klass.__dict__:
            descriptor = klass.__dict__["shortPrimitive"]
            break
    assert isinstance(descriptor, property)

def test_attributetest_root_has_longPrimitive():
    assert hasattr(attributeTest_Root, "longPrimitive")
    descriptor = None
    for klass in attributeTest_Root.__mro__:
        if "longPrimitive" in klass.__dict__:
            descriptor = klass.__dict__["longPrimitive"]
            break
    assert isinstance(descriptor, property)

def test_attributetest_root_has_bytePrimitive():
    assert hasattr(attributeTest_Root, "bytePrimitive")
    descriptor = None
    for klass in attributeTest_Root.__mro__:
        if "bytePrimitive" in klass.__dict__:
            descriptor = klass.__dict__["bytePrimitive"]
            break
    assert isinstance(descriptor, property)

def test_attributetest_root_has_intPrimitive():
    assert hasattr(attributeTest_Root, "intPrimitive")
    descriptor = None
    for klass in attributeTest_Root.__mro__:
        if "intPrimitive" in klass.__dict__:
            descriptor = klass.__dict__["intPrimitive"]
            break
    assert isinstance(descriptor, property)

def test_attributetest_root_has_map():
    assert hasattr(attributeTest_Root, "map")
    descriptor = None
    for klass in attributeTest_Root.__mro__:
        if "map" in klass.__dict__:
            descriptor = klass.__dict__["map"]
            break
    assert isinstance(descriptor, property)

def test_attributetest_root_has_listInt2():
    assert hasattr(attributeTest_Root, "listInt2")
    descriptor = None
    for klass in attributeTest_Root.__mro__:
        if "listInt2" in klass.__dict__:
            descriptor = klass.__dict__["listInt2"]
            break
    assert isinstance(descriptor, property)

def test_attributetest_root_has_listInt():
    assert hasattr(attributeTest_Root, "listInt")
    descriptor = None
    for klass in attributeTest_Root.__mro__:
        if "listInt" in klass.__dict__:
            descriptor = klass.__dict__["listInt"]
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
attributeTest_Root_strategy = st.builds(
    attributeTest_Root,
    listShort=
        safe_text,
    byteObj=
        safe_text,
    stringObj=
        safe_text,
    doublePrimitive=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    charPrimitive=
        safe_text,
    date=
        st.dates(),
    eList=
        safe_text,
    charObj=
        safe_text,
    boolObj=
        safe_text,
    boolPrimitive=
        st.booleans(),
    floatPrimitive=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    shortObj=
        safe_text,
    doubleObj=
        safe_text,
    listInt1=
        st.integers(),
    floatObj=
        safe_text,
    bigInteger=
        safe_text,
    intObj=
        safe_text,
    longObj=
        safe_text,
    listString=
        safe_text,
    bigDecimal=
        safe_text,
    byteArray=
        safe_text,
    javaObject=
        safe_text,
    shortPrimitive=
        safe_text,
    longPrimitive=
        safe_text,
    bytePrimitive=
        safe_text,
    intPrimitive=
        st.integers(),
    map=
        safe_text,
    listInt2=
        st.integers(),
    listInt=
        st.integers()
)

@given(instance=attributeTest_Root_strategy)
@settings(max_examples=50)
def test_attributetest_root_instantiation(instance):
    assert isinstance(instance, attributeTest_Root)



@given(instance=attributeTest_Root_strategy)
def test_attributetest_root_listShort_setter(instance):
    original = instance.listShort
    instance.listShort = original
    assert instance.listShort == original



@given(instance=attributeTest_Root_strategy)
def test_attributetest_root_byteObj_setter(instance):
    original = instance.byteObj
    instance.byteObj = original
    assert instance.byteObj == original



@given(instance=attributeTest_Root_strategy)
def test_attributetest_root_stringObj_setter(instance):
    original = instance.stringObj
    instance.stringObj = original
    assert instance.stringObj == original



@given(instance=attributeTest_Root_strategy)
def test_attributetest_root_doublePrimitive_setter(instance):
    original = instance.doublePrimitive
    instance.doublePrimitive = original
    assert instance.doublePrimitive == original



@given(instance=attributeTest_Root_strategy)
def test_attributetest_root_charPrimitive_setter(instance):
    original = instance.charPrimitive
    instance.charPrimitive = original
    assert instance.charPrimitive == original



@given(instance=attributeTest_Root_strategy)
def test_attributetest_root_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original



@given(instance=attributeTest_Root_strategy)
def test_attributetest_root_eList_setter(instance):
    original = instance.eList
    instance.eList = original
    assert instance.eList == original



@given(instance=attributeTest_Root_strategy)
def test_attributetest_root_charObj_setter(instance):
    original = instance.charObj
    instance.charObj = original
    assert instance.charObj == original



@given(instance=attributeTest_Root_strategy)
def test_attributetest_root_boolObj_setter(instance):
    original = instance.boolObj
    instance.boolObj = original
    assert instance.boolObj == original



@given(instance=attributeTest_Root_strategy)
def test_attributetest_root_boolPrimitive_setter(instance):
    original = instance.boolPrimitive
    instance.boolPrimitive = original
    assert instance.boolPrimitive == original



@given(instance=attributeTest_Root_strategy)
def test_attributetest_root_floatPrimitive_setter(instance):
    original = instance.floatPrimitive
    instance.floatPrimitive = original
    assert instance.floatPrimitive == original



@given(instance=attributeTest_Root_strategy)
def test_attributetest_root_shortObj_setter(instance):
    original = instance.shortObj
    instance.shortObj = original
    assert instance.shortObj == original



@given(instance=attributeTest_Root_strategy)
def test_attributetest_root_doubleObj_setter(instance):
    original = instance.doubleObj
    instance.doubleObj = original
    assert instance.doubleObj == original



@given(instance=attributeTest_Root_strategy)
def test_attributetest_root_listInt1_setter(instance):
    original = instance.listInt1
    instance.listInt1 = original
    assert instance.listInt1 == original



@given(instance=attributeTest_Root_strategy)
def test_attributetest_root_floatObj_setter(instance):
    original = instance.floatObj
    instance.floatObj = original
    assert instance.floatObj == original



@given(instance=attributeTest_Root_strategy)
def test_attributetest_root_bigInteger_setter(instance):
    original = instance.bigInteger
    instance.bigInteger = original
    assert instance.bigInteger == original



@given(instance=attributeTest_Root_strategy)
def test_attributetest_root_intObj_setter(instance):
    original = instance.intObj
    instance.intObj = original
    assert instance.intObj == original



@given(instance=attributeTest_Root_strategy)
def test_attributetest_root_longObj_setter(instance):
    original = instance.longObj
    instance.longObj = original
    assert instance.longObj == original



@given(instance=attributeTest_Root_strategy)
def test_attributetest_root_listString_setter(instance):
    original = instance.listString
    instance.listString = original
    assert instance.listString == original



@given(instance=attributeTest_Root_strategy)
def test_attributetest_root_bigDecimal_setter(instance):
    original = instance.bigDecimal
    instance.bigDecimal = original
    assert instance.bigDecimal == original



@given(instance=attributeTest_Root_strategy)
def test_attributetest_root_byteArray_setter(instance):
    original = instance.byteArray
    instance.byteArray = original
    assert instance.byteArray == original



@given(instance=attributeTest_Root_strategy)
def test_attributetest_root_javaObject_setter(instance):
    original = instance.javaObject
    instance.javaObject = original
    assert instance.javaObject == original



@given(instance=attributeTest_Root_strategy)
def test_attributetest_root_shortPrimitive_setter(instance):
    original = instance.shortPrimitive
    instance.shortPrimitive = original
    assert instance.shortPrimitive == original



@given(instance=attributeTest_Root_strategy)
def test_attributetest_root_longPrimitive_setter(instance):
    original = instance.longPrimitive
    instance.longPrimitive = original
    assert instance.longPrimitive == original



@given(instance=attributeTest_Root_strategy)
def test_attributetest_root_bytePrimitive_setter(instance):
    original = instance.bytePrimitive
    instance.bytePrimitive = original
    assert instance.bytePrimitive == original



@given(instance=attributeTest_Root_strategy)
def test_attributetest_root_intPrimitive_setter(instance):
    original = instance.intPrimitive
    instance.intPrimitive = original
    assert instance.intPrimitive == original



@given(instance=attributeTest_Root_strategy)
def test_attributetest_root_map_setter(instance):
    original = instance.map
    instance.map = original
    assert instance.map == original



@given(instance=attributeTest_Root_strategy)
def test_attributetest_root_listInt2_setter(instance):
    original = instance.listInt2
    instance.listInt2 = original
    assert instance.listInt2 == original



@given(instance=attributeTest_Root_strategy)
def test_attributetest_root_listInt_setter(instance):
    original = instance.listInt
    instance.listInt = original
    assert instance.listInt == original
