import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Element,
    alldatatypes_Root,
    alldatatypes_Element,
    Type,
    alldatatypes_Shorts,
    alldatatypes_Booleans,
    alldatatypes_Enums,
    alldatatypes_Floats,
    alldatatypes_Dates,
    alldatatypes_Doubles,
    alldatatypes_Integers,
    alldatatypes_Longs,
    alldatatypes_BigDecimals,
    alldatatypes_BigIntegers,
    alldatatypes_Strings,
    alldatatypes_Type,
    AEnum,
    StateWithoutDefault,
    Heavy,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_element_constructor_exists():
    assert callable(Element.__init__)


def test_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_alldatatypes_root_is_not_abstract():
    assert not inspect.isabstract(alldatatypes_Root)


def test_alldatatypes_root_constructor_exists():
    assert callable(alldatatypes_Root.__init__)


def test_alldatatypes_root_constructor_args():
    sig = inspect.signature(alldatatypes_Root.__init__)
    params = list(sig.parameters.keys())



def test_alldatatypes_element_is_not_abstract():
    assert not inspect.isabstract(alldatatypes_Element)


def test_alldatatypes_element_constructor_exists():
    assert callable(alldatatypes_Element.__init__)


def test_alldatatypes_element_constructor_args():
    sig = inspect.signature(alldatatypes_Element.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"

def test_alldatatypes_element_has_id():
    assert hasattr(alldatatypes_Element, "id")
    descriptor = None
    for klass in alldatatypes_Element.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_alldatatypes_element_has_name():
    assert hasattr(alldatatypes_Element, "name")
    descriptor = None
    for klass in alldatatypes_Element.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_alldatatypes_shorts_is_not_abstract():
    assert not inspect.isabstract(alldatatypes_Shorts)


def test_alldatatypes_shorts_constructor_exists():
    assert callable(alldatatypes_Shorts.__init__)


def test_alldatatypes_shorts_constructor_args():
    sig = inspect.signature(alldatatypes_Shorts.__init__)
    params = list(sig.parameters.keys())
    assert "notEditableShort_01" in params, "Missing parameter 'notEditableShort_01'"
    assert "short_01" in params, "Missing parameter 'short_01'"
    assert "short_01_EmptyDefault" in params, "Missing parameter 'short_01_EmptyDefault'"
    assert "short_1" in params, "Missing parameter 'short_1'"

def test_alldatatypes_shorts_has_notEditableShort_01():
    assert hasattr(alldatatypes_Shorts, "notEditableShort_01")
    descriptor = None
    for klass in alldatatypes_Shorts.__mro__:
        if "notEditableShort_01" in klass.__dict__:
            descriptor = klass.__dict__["notEditableShort_01"]
            break
    assert isinstance(descriptor, property)

def test_alldatatypes_shorts_has_short_01():
    assert hasattr(alldatatypes_Shorts, "short_01")
    descriptor = None
    for klass in alldatatypes_Shorts.__mro__:
        if "short_01" in klass.__dict__:
            descriptor = klass.__dict__["short_01"]
            break
    assert isinstance(descriptor, property)

def test_alldatatypes_shorts_has_short_01_EmptyDefault():
    assert hasattr(alldatatypes_Shorts, "short_01_EmptyDefault")
    descriptor = None
    for klass in alldatatypes_Shorts.__mro__:
        if "short_01_EmptyDefault" in klass.__dict__:
            descriptor = klass.__dict__["short_01_EmptyDefault"]
            break
    assert isinstance(descriptor, property)

def test_alldatatypes_shorts_has_short_1():
    assert hasattr(alldatatypes_Shorts, "short_1")
    descriptor = None
    for klass in alldatatypes_Shorts.__mro__:
        if "short_1" in klass.__dict__:
            descriptor = klass.__dict__["short_1"]
            break
    assert isinstance(descriptor, property)



def test_alldatatypes_booleans_is_not_abstract():
    assert not inspect.isabstract(alldatatypes_Booleans)


def test_alldatatypes_booleans_constructor_exists():
    assert callable(alldatatypes_Booleans.__init__)


def test_alldatatypes_booleans_constructor_args():
    sig = inspect.signature(alldatatypes_Booleans.__init__)
    params = list(sig.parameters.keys())
    assert "boolean_01" in params, "Missing parameter 'boolean_01'"
    assert "notEditableBoolean_01" in params, "Missing parameter 'notEditableBoolean_01'"
    assert "boolean_01_EmptyDefault" in params, "Missing parameter 'boolean_01_EmptyDefault'"
    assert "boolean_1" in params, "Missing parameter 'boolean_1'"

def test_alldatatypes_booleans_has_boolean_01():
    assert hasattr(alldatatypes_Booleans, "boolean_01")
    descriptor = None
    for klass in alldatatypes_Booleans.__mro__:
        if "boolean_01" in klass.__dict__:
            descriptor = klass.__dict__["boolean_01"]
            break
    assert isinstance(descriptor, property)

def test_alldatatypes_booleans_has_notEditableBoolean_01():
    assert hasattr(alldatatypes_Booleans, "notEditableBoolean_01")
    descriptor = None
    for klass in alldatatypes_Booleans.__mro__:
        if "notEditableBoolean_01" in klass.__dict__:
            descriptor = klass.__dict__["notEditableBoolean_01"]
            break
    assert isinstance(descriptor, property)

def test_alldatatypes_booleans_has_boolean_01_EmptyDefault():
    assert hasattr(alldatatypes_Booleans, "boolean_01_EmptyDefault")
    descriptor = None
    for klass in alldatatypes_Booleans.__mro__:
        if "boolean_01_EmptyDefault" in klass.__dict__:
            descriptor = klass.__dict__["boolean_01_EmptyDefault"]
            break
    assert isinstance(descriptor, property)

def test_alldatatypes_booleans_has_boolean_1():
    assert hasattr(alldatatypes_Booleans, "boolean_1")
    descriptor = None
    for klass in alldatatypes_Booleans.__mro__:
        if "boolean_1" in klass.__dict__:
            descriptor = klass.__dict__["boolean_1"]
            break
    assert isinstance(descriptor, property)



def test_alldatatypes_enums_is_not_abstract():
    assert not inspect.isabstract(alldatatypes_Enums)


def test_alldatatypes_enums_constructor_exists():
    assert callable(alldatatypes_Enums.__init__)


def test_alldatatypes_enums_constructor_args():
    sig = inspect.signature(alldatatypes_Enums.__init__)
    params = list(sig.parameters.keys())
    assert "heavy" in params, "Missing parameter 'heavy'"
    assert "enum_01" in params, "Missing parameter 'enum_01'"
    assert "statesMax2" in params, "Missing parameter 'statesMax2'"
    assert "enum_01_EmptyDefault" in params, "Missing parameter 'enum_01_EmptyDefault'"
    assert "states" in params, "Missing parameter 'states'"
    assert "enums" in params, "Missing parameter 'enums'"
    assert "statesMin1Max2" in params, "Missing parameter 'statesMin1Max2'"
    assert "notEditableEnum_01" in params, "Missing parameter 'notEditableEnum_01'"
    assert "enum_1" in params, "Missing parameter 'enum_1'"

def test_alldatatypes_enums_has_heavy():
    assert hasattr(alldatatypes_Enums, "heavy")
    descriptor = None
    for klass in alldatatypes_Enums.__mro__:
        if "heavy" in klass.__dict__:
            descriptor = klass.__dict__["heavy"]
            break
    assert isinstance(descriptor, property)

def test_alldatatypes_enums_has_enum_01():
    assert hasattr(alldatatypes_Enums, "enum_01")
    descriptor = None
    for klass in alldatatypes_Enums.__mro__:
        if "enum_01" in klass.__dict__:
            descriptor = klass.__dict__["enum_01"]
            break
    assert isinstance(descriptor, property)

def test_alldatatypes_enums_has_statesMax2():
    assert hasattr(alldatatypes_Enums, "statesMax2")
    descriptor = None
    for klass in alldatatypes_Enums.__mro__:
        if "statesMax2" in klass.__dict__:
            descriptor = klass.__dict__["statesMax2"]
            break
    assert isinstance(descriptor, property)

def test_alldatatypes_enums_has_enum_01_EmptyDefault():
    assert hasattr(alldatatypes_Enums, "enum_01_EmptyDefault")
    descriptor = None
    for klass in alldatatypes_Enums.__mro__:
        if "enum_01_EmptyDefault" in klass.__dict__:
            descriptor = klass.__dict__["enum_01_EmptyDefault"]
            break
    assert isinstance(descriptor, property)

def test_alldatatypes_enums_has_states():
    assert hasattr(alldatatypes_Enums, "states")
    descriptor = None
    for klass in alldatatypes_Enums.__mro__:
        if "states" in klass.__dict__:
            descriptor = klass.__dict__["states"]
            break
    assert isinstance(descriptor, property)

def test_alldatatypes_enums_has_enums():
    assert hasattr(alldatatypes_Enums, "enums")
    descriptor = None
    for klass in alldatatypes_Enums.__mro__:
        if "enums" in klass.__dict__:
            descriptor = klass.__dict__["enums"]
            break
    assert isinstance(descriptor, property)

def test_alldatatypes_enums_has_statesMin1Max2():
    assert hasattr(alldatatypes_Enums, "statesMin1Max2")
    descriptor = None
    for klass in alldatatypes_Enums.__mro__:
        if "statesMin1Max2" in klass.__dict__:
            descriptor = klass.__dict__["statesMin1Max2"]
            break
    assert isinstance(descriptor, property)

def test_alldatatypes_enums_has_notEditableEnum_01():
    assert hasattr(alldatatypes_Enums, "notEditableEnum_01")
    descriptor = None
    for klass in alldatatypes_Enums.__mro__:
        if "notEditableEnum_01" in klass.__dict__:
            descriptor = klass.__dict__["notEditableEnum_01"]
            break
    assert isinstance(descriptor, property)

def test_alldatatypes_enums_has_enum_1():
    assert hasattr(alldatatypes_Enums, "enum_1")
    descriptor = None
    for klass in alldatatypes_Enums.__mro__:
        if "enum_1" in klass.__dict__:
            descriptor = klass.__dict__["enum_1"]
            break
    assert isinstance(descriptor, property)



def test_alldatatypes_floats_is_not_abstract():
    assert not inspect.isabstract(alldatatypes_Floats)


def test_alldatatypes_floats_constructor_exists():
    assert callable(alldatatypes_Floats.__init__)


def test_alldatatypes_floats_constructor_args():
    sig = inspect.signature(alldatatypes_Floats.__init__)
    params = list(sig.parameters.keys())
    assert "float_01" in params, "Missing parameter 'float_01'"
    assert "notEditableFloat_01" in params, "Missing parameter 'notEditableFloat_01'"
    assert "float_01_EmptyDefault" in params, "Missing parameter 'float_01_EmptyDefault'"
    assert "float_1" in params, "Missing parameter 'float_1'"

def test_alldatatypes_floats_has_float_01():
    assert hasattr(alldatatypes_Floats, "float_01")
    descriptor = None
    for klass in alldatatypes_Floats.__mro__:
        if "float_01" in klass.__dict__:
            descriptor = klass.__dict__["float_01"]
            break
    assert isinstance(descriptor, property)

def test_alldatatypes_floats_has_notEditableFloat_01():
    assert hasattr(alldatatypes_Floats, "notEditableFloat_01")
    descriptor = None
    for klass in alldatatypes_Floats.__mro__:
        if "notEditableFloat_01" in klass.__dict__:
            descriptor = klass.__dict__["notEditableFloat_01"]
            break
    assert isinstance(descriptor, property)

def test_alldatatypes_floats_has_float_01_EmptyDefault():
    assert hasattr(alldatatypes_Floats, "float_01_EmptyDefault")
    descriptor = None
    for klass in alldatatypes_Floats.__mro__:
        if "float_01_EmptyDefault" in klass.__dict__:
            descriptor = klass.__dict__["float_01_EmptyDefault"]
            break
    assert isinstance(descriptor, property)

def test_alldatatypes_floats_has_float_1():
    assert hasattr(alldatatypes_Floats, "float_1")
    descriptor = None
    for klass in alldatatypes_Floats.__mro__:
        if "float_1" in klass.__dict__:
            descriptor = klass.__dict__["float_1"]
            break
    assert isinstance(descriptor, property)



def test_alldatatypes_dates_is_not_abstract():
    assert not inspect.isabstract(alldatatypes_Dates)


def test_alldatatypes_dates_constructor_exists():
    assert callable(alldatatypes_Dates.__init__)


def test_alldatatypes_dates_constructor_args():
    sig = inspect.signature(alldatatypes_Dates.__init__)
    params = list(sig.parameters.keys())
    assert "notEditableDate_01" in params, "Missing parameter 'notEditableDate_01'"
    assert "date_1" in params, "Missing parameter 'date_1'"
    assert "date_01_HMS" in params, "Missing parameter 'date_01_HMS'"
    assert "date_01_HMSms" in params, "Missing parameter 'date_01_HMSms'"
    assert "date_01" in params, "Missing parameter 'date_01'"
    assert "date_01_HM" in params, "Missing parameter 'date_01_HM'"
    assert "dates" in params, "Missing parameter 'dates'"
    assert "dateEmptyDefault_01" in params, "Missing parameter 'dateEmptyDefault_01'"

def test_alldatatypes_dates_has_notEditableDate_01():
    assert hasattr(alldatatypes_Dates, "notEditableDate_01")
    descriptor = None
    for klass in alldatatypes_Dates.__mro__:
        if "notEditableDate_01" in klass.__dict__:
            descriptor = klass.__dict__["notEditableDate_01"]
            break
    assert isinstance(descriptor, property)

def test_alldatatypes_dates_has_date_1():
    assert hasattr(alldatatypes_Dates, "date_1")
    descriptor = None
    for klass in alldatatypes_Dates.__mro__:
        if "date_1" in klass.__dict__:
            descriptor = klass.__dict__["date_1"]
            break
    assert isinstance(descriptor, property)

def test_alldatatypes_dates_has_date_01_HMS():
    assert hasattr(alldatatypes_Dates, "date_01_HMS")
    descriptor = None
    for klass in alldatatypes_Dates.__mro__:
        if "date_01_HMS" in klass.__dict__:
            descriptor = klass.__dict__["date_01_HMS"]
            break
    assert isinstance(descriptor, property)

def test_alldatatypes_dates_has_date_01_HMSms():
    assert hasattr(alldatatypes_Dates, "date_01_HMSms")
    descriptor = None
    for klass in alldatatypes_Dates.__mro__:
        if "date_01_HMSms" in klass.__dict__:
            descriptor = klass.__dict__["date_01_HMSms"]
            break
    assert isinstance(descriptor, property)

def test_alldatatypes_dates_has_date_01():
    assert hasattr(alldatatypes_Dates, "date_01")
    descriptor = None
    for klass in alldatatypes_Dates.__mro__:
        if "date_01" in klass.__dict__:
            descriptor = klass.__dict__["date_01"]
            break
    assert isinstance(descriptor, property)

def test_alldatatypes_dates_has_date_01_HM():
    assert hasattr(alldatatypes_Dates, "date_01_HM")
    descriptor = None
    for klass in alldatatypes_Dates.__mro__:
        if "date_01_HM" in klass.__dict__:
            descriptor = klass.__dict__["date_01_HM"]
            break
    assert isinstance(descriptor, property)

def test_alldatatypes_dates_has_dates():
    assert hasattr(alldatatypes_Dates, "dates")
    descriptor = None
    for klass in alldatatypes_Dates.__mro__:
        if "dates" in klass.__dict__:
            descriptor = klass.__dict__["dates"]
            break
    assert isinstance(descriptor, property)

def test_alldatatypes_dates_has_dateEmptyDefault_01():
    assert hasattr(alldatatypes_Dates, "dateEmptyDefault_01")
    descriptor = None
    for klass in alldatatypes_Dates.__mro__:
        if "dateEmptyDefault_01" in klass.__dict__:
            descriptor = klass.__dict__["dateEmptyDefault_01"]
            break
    assert isinstance(descriptor, property)



def test_alldatatypes_doubles_is_not_abstract():
    assert not inspect.isabstract(alldatatypes_Doubles)


def test_alldatatypes_doubles_constructor_exists():
    assert callable(alldatatypes_Doubles.__init__)


def test_alldatatypes_doubles_constructor_args():
    sig = inspect.signature(alldatatypes_Doubles.__init__)
    params = list(sig.parameters.keys())
    assert "double_01_EmptyDefault" in params, "Missing parameter 'double_01_EmptyDefault'"
    assert "double_01" in params, "Missing parameter 'double_01'"
    assert "notEditableDouble_01" in params, "Missing parameter 'notEditableDouble_01'"
    assert "double_1" in params, "Missing parameter 'double_1'"

def test_alldatatypes_doubles_has_double_01_EmptyDefault():
    assert hasattr(alldatatypes_Doubles, "double_01_EmptyDefault")
    descriptor = None
    for klass in alldatatypes_Doubles.__mro__:
        if "double_01_EmptyDefault" in klass.__dict__:
            descriptor = klass.__dict__["double_01_EmptyDefault"]
            break
    assert isinstance(descriptor, property)

def test_alldatatypes_doubles_has_double_01():
    assert hasattr(alldatatypes_Doubles, "double_01")
    descriptor = None
    for klass in alldatatypes_Doubles.__mro__:
        if "double_01" in klass.__dict__:
            descriptor = klass.__dict__["double_01"]
            break
    assert isinstance(descriptor, property)

def test_alldatatypes_doubles_has_notEditableDouble_01():
    assert hasattr(alldatatypes_Doubles, "notEditableDouble_01")
    descriptor = None
    for klass in alldatatypes_Doubles.__mro__:
        if "notEditableDouble_01" in klass.__dict__:
            descriptor = klass.__dict__["notEditableDouble_01"]
            break
    assert isinstance(descriptor, property)

def test_alldatatypes_doubles_has_double_1():
    assert hasattr(alldatatypes_Doubles, "double_1")
    descriptor = None
    for klass in alldatatypes_Doubles.__mro__:
        if "double_1" in klass.__dict__:
            descriptor = klass.__dict__["double_1"]
            break
    assert isinstance(descriptor, property)



def test_alldatatypes_integers_is_not_abstract():
    assert not inspect.isabstract(alldatatypes_Integers)


def test_alldatatypes_integers_constructor_exists():
    assert callable(alldatatypes_Integers.__init__)


def test_alldatatypes_integers_constructor_args():
    sig = inspect.signature(alldatatypes_Integers.__init__)
    params = list(sig.parameters.keys())
    assert "int_01_EmptyDefault" in params, "Missing parameter 'int_01_EmptyDefault'"
    assert "ints" in params, "Missing parameter 'ints'"
    assert "hiddenInt_01" in params, "Missing parameter 'hiddenInt_01'"
    assert "int_1" in params, "Missing parameter 'int_1'"
    assert "int_01" in params, "Missing parameter 'int_01'"
    assert "notEditableInt_01" in params, "Missing parameter 'notEditableInt_01'"

def test_alldatatypes_integers_has_int_01_EmptyDefault():
    assert hasattr(alldatatypes_Integers, "int_01_EmptyDefault")
    descriptor = None
    for klass in alldatatypes_Integers.__mro__:
        if "int_01_EmptyDefault" in klass.__dict__:
            descriptor = klass.__dict__["int_01_EmptyDefault"]
            break
    assert isinstance(descriptor, property)

def test_alldatatypes_integers_has_ints():
    assert hasattr(alldatatypes_Integers, "ints")
    descriptor = None
    for klass in alldatatypes_Integers.__mro__:
        if "ints" in klass.__dict__:
            descriptor = klass.__dict__["ints"]
            break
    assert isinstance(descriptor, property)

def test_alldatatypes_integers_has_hiddenInt_01():
    assert hasattr(alldatatypes_Integers, "hiddenInt_01")
    descriptor = None
    for klass in alldatatypes_Integers.__mro__:
        if "hiddenInt_01" in klass.__dict__:
            descriptor = klass.__dict__["hiddenInt_01"]
            break
    assert isinstance(descriptor, property)

def test_alldatatypes_integers_has_int_1():
    assert hasattr(alldatatypes_Integers, "int_1")
    descriptor = None
    for klass in alldatatypes_Integers.__mro__:
        if "int_1" in klass.__dict__:
            descriptor = klass.__dict__["int_1"]
            break
    assert isinstance(descriptor, property)

def test_alldatatypes_integers_has_int_01():
    assert hasattr(alldatatypes_Integers, "int_01")
    descriptor = None
    for klass in alldatatypes_Integers.__mro__:
        if "int_01" in klass.__dict__:
            descriptor = klass.__dict__["int_01"]
            break
    assert isinstance(descriptor, property)

def test_alldatatypes_integers_has_notEditableInt_01():
    assert hasattr(alldatatypes_Integers, "notEditableInt_01")
    descriptor = None
    for klass in alldatatypes_Integers.__mro__:
        if "notEditableInt_01" in klass.__dict__:
            descriptor = klass.__dict__["notEditableInt_01"]
            break
    assert isinstance(descriptor, property)



def test_alldatatypes_longs_is_not_abstract():
    assert not inspect.isabstract(alldatatypes_Longs)


def test_alldatatypes_longs_constructor_exists():
    assert callable(alldatatypes_Longs.__init__)


def test_alldatatypes_longs_constructor_args():
    sig = inspect.signature(alldatatypes_Longs.__init__)
    params = list(sig.parameters.keys())
    assert "notEditableLong_01" in params, "Missing parameter 'notEditableLong_01'"
    assert "long_1" in params, "Missing parameter 'long_1'"
    assert "long_01" in params, "Missing parameter 'long_01'"
    assert "long_01_EmptyDefault" in params, "Missing parameter 'long_01_EmptyDefault'"

def test_alldatatypes_longs_has_notEditableLong_01():
    assert hasattr(alldatatypes_Longs, "notEditableLong_01")
    descriptor = None
    for klass in alldatatypes_Longs.__mro__:
        if "notEditableLong_01" in klass.__dict__:
            descriptor = klass.__dict__["notEditableLong_01"]
            break
    assert isinstance(descriptor, property)

def test_alldatatypes_longs_has_long_1():
    assert hasattr(alldatatypes_Longs, "long_1")
    descriptor = None
    for klass in alldatatypes_Longs.__mro__:
        if "long_1" in klass.__dict__:
            descriptor = klass.__dict__["long_1"]
            break
    assert isinstance(descriptor, property)

def test_alldatatypes_longs_has_long_01():
    assert hasattr(alldatatypes_Longs, "long_01")
    descriptor = None
    for klass in alldatatypes_Longs.__mro__:
        if "long_01" in klass.__dict__:
            descriptor = klass.__dict__["long_01"]
            break
    assert isinstance(descriptor, property)

def test_alldatatypes_longs_has_long_01_EmptyDefault():
    assert hasattr(alldatatypes_Longs, "long_01_EmptyDefault")
    descriptor = None
    for klass in alldatatypes_Longs.__mro__:
        if "long_01_EmptyDefault" in klass.__dict__:
            descriptor = klass.__dict__["long_01_EmptyDefault"]
            break
    assert isinstance(descriptor, property)



def test_alldatatypes_bigdecimals_is_not_abstract():
    assert not inspect.isabstract(alldatatypes_BigDecimals)


def test_alldatatypes_bigdecimals_constructor_exists():
    assert callable(alldatatypes_BigDecimals.__init__)


def test_alldatatypes_bigdecimals_constructor_args():
    sig = inspect.signature(alldatatypes_BigDecimals.__init__)
    params = list(sig.parameters.keys())
    assert "bigDecimals" in params, "Missing parameter 'bigDecimals'"
    assert "notEditableBigDecimal_01" in params, "Missing parameter 'notEditableBigDecimal_01'"
    assert "bigDecimal_01_EmptyDefault" in params, "Missing parameter 'bigDecimal_01_EmptyDefault'"
    assert "bigDecimal_01" in params, "Missing parameter 'bigDecimal_01'"
    assert "bigDecimal_1" in params, "Missing parameter 'bigDecimal_1'"

def test_alldatatypes_bigdecimals_has_bigDecimals():
    assert hasattr(alldatatypes_BigDecimals, "bigDecimals")
    descriptor = None
    for klass in alldatatypes_BigDecimals.__mro__:
        if "bigDecimals" in klass.__dict__:
            descriptor = klass.__dict__["bigDecimals"]
            break
    assert isinstance(descriptor, property)

def test_alldatatypes_bigdecimals_has_notEditableBigDecimal_01():
    assert hasattr(alldatatypes_BigDecimals, "notEditableBigDecimal_01")
    descriptor = None
    for klass in alldatatypes_BigDecimals.__mro__:
        if "notEditableBigDecimal_01" in klass.__dict__:
            descriptor = klass.__dict__["notEditableBigDecimal_01"]
            break
    assert isinstance(descriptor, property)

def test_alldatatypes_bigdecimals_has_bigDecimal_01_EmptyDefault():
    assert hasattr(alldatatypes_BigDecimals, "bigDecimal_01_EmptyDefault")
    descriptor = None
    for klass in alldatatypes_BigDecimals.__mro__:
        if "bigDecimal_01_EmptyDefault" in klass.__dict__:
            descriptor = klass.__dict__["bigDecimal_01_EmptyDefault"]
            break
    assert isinstance(descriptor, property)

def test_alldatatypes_bigdecimals_has_bigDecimal_01():
    assert hasattr(alldatatypes_BigDecimals, "bigDecimal_01")
    descriptor = None
    for klass in alldatatypes_BigDecimals.__mro__:
        if "bigDecimal_01" in klass.__dict__:
            descriptor = klass.__dict__["bigDecimal_01"]
            break
    assert isinstance(descriptor, property)

def test_alldatatypes_bigdecimals_has_bigDecimal_1():
    assert hasattr(alldatatypes_BigDecimals, "bigDecimal_1")
    descriptor = None
    for klass in alldatatypes_BigDecimals.__mro__:
        if "bigDecimal_1" in klass.__dict__:
            descriptor = klass.__dict__["bigDecimal_1"]
            break
    assert isinstance(descriptor, property)



def test_alldatatypes_bigintegers_is_not_abstract():
    assert not inspect.isabstract(alldatatypes_BigIntegers)


def test_alldatatypes_bigintegers_constructor_exists():
    assert callable(alldatatypes_BigIntegers.__init__)


def test_alldatatypes_bigintegers_constructor_args():
    sig = inspect.signature(alldatatypes_BigIntegers.__init__)
    params = list(sig.parameters.keys())
    assert "bigInts" in params, "Missing parameter 'bigInts'"
    assert "bigInt_01" in params, "Missing parameter 'bigInt_01'"
    assert "bigInt_1" in params, "Missing parameter 'bigInt_1'"
    assert "notEditableBigInt_01" in params, "Missing parameter 'notEditableBigInt_01'"
    assert "bigInt_01_EmptyDefault" in params, "Missing parameter 'bigInt_01_EmptyDefault'"

def test_alldatatypes_bigintegers_has_bigInts():
    assert hasattr(alldatatypes_BigIntegers, "bigInts")
    descriptor = None
    for klass in alldatatypes_BigIntegers.__mro__:
        if "bigInts" in klass.__dict__:
            descriptor = klass.__dict__["bigInts"]
            break
    assert isinstance(descriptor, property)

def test_alldatatypes_bigintegers_has_bigInt_01():
    assert hasattr(alldatatypes_BigIntegers, "bigInt_01")
    descriptor = None
    for klass in alldatatypes_BigIntegers.__mro__:
        if "bigInt_01" in klass.__dict__:
            descriptor = klass.__dict__["bigInt_01"]
            break
    assert isinstance(descriptor, property)

def test_alldatatypes_bigintegers_has_bigInt_1():
    assert hasattr(alldatatypes_BigIntegers, "bigInt_1")
    descriptor = None
    for klass in alldatatypes_BigIntegers.__mro__:
        if "bigInt_1" in klass.__dict__:
            descriptor = klass.__dict__["bigInt_1"]
            break
    assert isinstance(descriptor, property)

def test_alldatatypes_bigintegers_has_notEditableBigInt_01():
    assert hasattr(alldatatypes_BigIntegers, "notEditableBigInt_01")
    descriptor = None
    for klass in alldatatypes_BigIntegers.__mro__:
        if "notEditableBigInt_01" in klass.__dict__:
            descriptor = klass.__dict__["notEditableBigInt_01"]
            break
    assert isinstance(descriptor, property)

def test_alldatatypes_bigintegers_has_bigInt_01_EmptyDefault():
    assert hasattr(alldatatypes_BigIntegers, "bigInt_01_EmptyDefault")
    descriptor = None
    for klass in alldatatypes_BigIntegers.__mro__:
        if "bigInt_01_EmptyDefault" in klass.__dict__:
            descriptor = klass.__dict__["bigInt_01_EmptyDefault"]
            break
    assert isinstance(descriptor, property)



def test_alldatatypes_strings_is_not_abstract():
    assert not inspect.isabstract(alldatatypes_Strings)


def test_alldatatypes_strings_constructor_exists():
    assert callable(alldatatypes_Strings.__init__)


def test_alldatatypes_strings_constructor_args():
    sig = inspect.signature(alldatatypes_Strings.__init__)
    params = list(sig.parameters.keys())
    assert "textarea" in params, "Missing parameter 'textarea'"
    assert "text_01" in params, "Missing parameter 'text_01'"
    assert "text_1" in params, "Missing parameter 'text_1'"
    assert "notEditableText_01" in params, "Missing parameter 'notEditableText_01'"
    assert "link_01" in params, "Missing parameter 'link_01'"
    assert "text_01_EmptyDefault" in params, "Missing parameter 'text_01_EmptyDefault'"
    assert "html_01" in params, "Missing parameter 'html_01'"

def test_alldatatypes_strings_has_textarea():
    assert hasattr(alldatatypes_Strings, "textarea")
    descriptor = None
    for klass in alldatatypes_Strings.__mro__:
        if "textarea" in klass.__dict__:
            descriptor = klass.__dict__["textarea"]
            break
    assert isinstance(descriptor, property)

def test_alldatatypes_strings_has_text_01():
    assert hasattr(alldatatypes_Strings, "text_01")
    descriptor = None
    for klass in alldatatypes_Strings.__mro__:
        if "text_01" in klass.__dict__:
            descriptor = klass.__dict__["text_01"]
            break
    assert isinstance(descriptor, property)

def test_alldatatypes_strings_has_text_1():
    assert hasattr(alldatatypes_Strings, "text_1")
    descriptor = None
    for klass in alldatatypes_Strings.__mro__:
        if "text_1" in klass.__dict__:
            descriptor = klass.__dict__["text_1"]
            break
    assert isinstance(descriptor, property)

def test_alldatatypes_strings_has_notEditableText_01():
    assert hasattr(alldatatypes_Strings, "notEditableText_01")
    descriptor = None
    for klass in alldatatypes_Strings.__mro__:
        if "notEditableText_01" in klass.__dict__:
            descriptor = klass.__dict__["notEditableText_01"]
            break
    assert isinstance(descriptor, property)

def test_alldatatypes_strings_has_link_01():
    assert hasattr(alldatatypes_Strings, "link_01")
    descriptor = None
    for klass in alldatatypes_Strings.__mro__:
        if "link_01" in klass.__dict__:
            descriptor = klass.__dict__["link_01"]
            break
    assert isinstance(descriptor, property)

def test_alldatatypes_strings_has_text_01_EmptyDefault():
    assert hasattr(alldatatypes_Strings, "text_01_EmptyDefault")
    descriptor = None
    for klass in alldatatypes_Strings.__mro__:
        if "text_01_EmptyDefault" in klass.__dict__:
            descriptor = klass.__dict__["text_01_EmptyDefault"]
            break
    assert isinstance(descriptor, property)

def test_alldatatypes_strings_has_html_01():
    assert hasattr(alldatatypes_Strings, "html_01")
    descriptor = None
    for klass in alldatatypes_Strings.__mro__:
        if "html_01" in klass.__dict__:
            descriptor = klass.__dict__["html_01"]
            break
    assert isinstance(descriptor, property)



def test_alldatatypes_type_is_not_abstract():
    assert not inspect.isabstract(alldatatypes_Type)


def test_alldatatypes_type_constructor_exists():
    assert callable(alldatatypes_Type.__init__)


def test_alldatatypes_type_constructor_args():
    sig = inspect.signature(alldatatypes_Type.__init__)
    params = list(sig.parameters.keys())

def test_aenum_exists():
    # Check that the Enumeration exists
    assert AEnum is not None

def test_aenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AEnum]
    expected_literals = [
        "ENUM0",
        "ENUM1",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AEnum"

def test_statewithoutdefault_exists():
    # Check that the Enumeration exists
    assert StateWithoutDefault is not None

def test_statewithoutdefault_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in StateWithoutDefault]
    expected_literals = [
        "CLOSE",
        "MOVING",
        "OPEN",
        "DELETE",
        "MOVE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in StateWithoutDefault"

def test_heavy_exists():
    # Check that the Enumeration exists
    assert Heavy is not None

def test_heavy_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Heavy]
    expected_literals = [
        "DELETE",
        "DELETE1",
        "MOVING2",
        "MOVE3",
        "MOVING3",
        "CLOSE4",
        "CLOSE3",
        "OPEN3",
        "MOVING1",
        "DELETE2",
        "MOVE",
        "CLOSE",
        "MOVING4",
        "OPEN4",
        "MOVE2",
        "MOVE1",
        "OPEN2",
        "DELETE3",
        "CLOS1E",
        "CLOSE2",
        "OPEN1",
        "MOVING",
        "DELETE4",
        "OPEN",
        "MOVE4",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Heavy"


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
Element_strategy = st.builds(
    Element,
)
alldatatypes_Root_strategy = st.builds(
    alldatatypes_Root,
)
alldatatypes_Element_strategy = st.builds(
    alldatatypes_Element,
    id=
        safe_text,
    name=
        safe_text
)
Type_strategy = st.builds(
    Type,
)
alldatatypes_Shorts_strategy = st.builds(
    alldatatypes_Shorts,
    notEditableShort_01=
        safe_text,
    short_01=
        safe_text,
    short_01_EmptyDefault=
        safe_text,
    short_1=
        safe_text
)
alldatatypes_Booleans_strategy = st.builds(
    alldatatypes_Booleans,
    boolean_01=
        st.booleans(),
    notEditableBoolean_01=
        st.booleans(),
    boolean_01_EmptyDefault=
        st.booleans(),
    boolean_1=
        st.booleans()
)
alldatatypes_Enums_strategy = st.builds(
    alldatatypes_Enums,
    heavy=
        safe_text,
    enum_01=
        safe_text,
    statesMax2=
        safe_text,
    enum_01_EmptyDefault=
        safe_text,
    states=
        safe_text,
    enums=
        safe_text,
    statesMin1Max2=
        safe_text,
    notEditableEnum_01=
        safe_text,
    enum_1=
        safe_text
)
alldatatypes_Floats_strategy = st.builds(
    alldatatypes_Floats,
    float_01=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    notEditableFloat_01=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    float_01_EmptyDefault=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    float_1=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
alldatatypes_Dates_strategy = st.builds(
    alldatatypes_Dates,
    notEditableDate_01=
        st.dates(),
    date_1=
        st.dates(),
    date_01_HMS=
        st.dates(),
    date_01_HMSms=
        st.dates(),
    date_01=
        st.dates(),
    date_01_HM=
        st.dates(),
    dates=
        st.dates(),
    dateEmptyDefault_01=
        st.dates()
)
alldatatypes_Doubles_strategy = st.builds(
    alldatatypes_Doubles,
    double_01_EmptyDefault=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    double_01=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    notEditableDouble_01=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    double_1=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
alldatatypes_Integers_strategy = st.builds(
    alldatatypes_Integers,
    int_01_EmptyDefault=
        st.integers(),
    ints=
        st.integers(),
    hiddenInt_01=
        st.integers(),
    int_1=
        st.integers(),
    int_01=
        st.integers(),
    notEditableInt_01=
        st.integers()
)
alldatatypes_Longs_strategy = st.builds(
    alldatatypes_Longs,
    notEditableLong_01=
        safe_text,
    long_1=
        safe_text,
    long_01=
        safe_text,
    long_01_EmptyDefault=
        safe_text
)
alldatatypes_BigDecimals_strategy = st.builds(
    alldatatypes_BigDecimals,
    bigDecimals=
        safe_text,
    notEditableBigDecimal_01=
        safe_text,
    bigDecimal_01_EmptyDefault=
        safe_text,
    bigDecimal_01=
        safe_text,
    bigDecimal_1=
        safe_text
)
alldatatypes_BigIntegers_strategy = st.builds(
    alldatatypes_BigIntegers,
    bigInts=
        safe_text,
    bigInt_01=
        safe_text,
    bigInt_1=
        safe_text,
    notEditableBigInt_01=
        safe_text,
    bigInt_01_EmptyDefault=
        safe_text
)
alldatatypes_Strings_strategy = st.builds(
    alldatatypes_Strings,
    textarea=
        safe_text,
    text_01=
        safe_text,
    text_1=
        safe_text,
    notEditableText_01=
        safe_text,
    link_01=
        safe_text,
    text_01_EmptyDefault=
        safe_text,
    html_01=
        safe_text
)
alldatatypes_Type_strategy = st.builds(
    alldatatypes_Type,
)

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=alldatatypes_Root_strategy)
@settings(max_examples=50)
def test_alldatatypes_root_instantiation(instance):
    assert isinstance(instance, alldatatypes_Root)

@given(instance=alldatatypes_Element_strategy)
@settings(max_examples=50)
def test_alldatatypes_element_instantiation(instance):
    assert isinstance(instance, alldatatypes_Element)



@given(instance=alldatatypes_Element_strategy)
def test_alldatatypes_element_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=alldatatypes_Element_strategy)
def test_alldatatypes_element_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=alldatatypes_Shorts_strategy)
@settings(max_examples=50)
def test_alldatatypes_shorts_instantiation(instance):
    assert isinstance(instance, alldatatypes_Shorts)



@given(instance=alldatatypes_Shorts_strategy)
def test_alldatatypes_shorts_notEditableShort_01_setter(instance):
    original = instance.notEditableShort_01
    instance.notEditableShort_01 = original
    assert instance.notEditableShort_01 == original



@given(instance=alldatatypes_Shorts_strategy)
def test_alldatatypes_shorts_short_01_setter(instance):
    original = instance.short_01
    instance.short_01 = original
    assert instance.short_01 == original



@given(instance=alldatatypes_Shorts_strategy)
def test_alldatatypes_shorts_short_01_EmptyDefault_setter(instance):
    original = instance.short_01_EmptyDefault
    instance.short_01_EmptyDefault = original
    assert instance.short_01_EmptyDefault == original



@given(instance=alldatatypes_Shorts_strategy)
def test_alldatatypes_shorts_short_1_setter(instance):
    original = instance.short_1
    instance.short_1 = original
    assert instance.short_1 == original

@given(instance=alldatatypes_Booleans_strategy)
@settings(max_examples=50)
def test_alldatatypes_booleans_instantiation(instance):
    assert isinstance(instance, alldatatypes_Booleans)



@given(instance=alldatatypes_Booleans_strategy)
def test_alldatatypes_booleans_boolean_01_setter(instance):
    original = instance.boolean_01
    instance.boolean_01 = original
    assert instance.boolean_01 == original



@given(instance=alldatatypes_Booleans_strategy)
def test_alldatatypes_booleans_notEditableBoolean_01_setter(instance):
    original = instance.notEditableBoolean_01
    instance.notEditableBoolean_01 = original
    assert instance.notEditableBoolean_01 == original



@given(instance=alldatatypes_Booleans_strategy)
def test_alldatatypes_booleans_boolean_01_EmptyDefault_setter(instance):
    original = instance.boolean_01_EmptyDefault
    instance.boolean_01_EmptyDefault = original
    assert instance.boolean_01_EmptyDefault == original



@given(instance=alldatatypes_Booleans_strategy)
def test_alldatatypes_booleans_boolean_1_setter(instance):
    original = instance.boolean_1
    instance.boolean_1 = original
    assert instance.boolean_1 == original

@given(instance=alldatatypes_Enums_strategy)
@settings(max_examples=50)
def test_alldatatypes_enums_instantiation(instance):
    assert isinstance(instance, alldatatypes_Enums)



@given(instance=alldatatypes_Enums_strategy)
def test_alldatatypes_enums_heavy_setter(instance):
    original = instance.heavy
    instance.heavy = original
    assert instance.heavy == original



@given(instance=alldatatypes_Enums_strategy)
def test_alldatatypes_enums_enum_01_setter(instance):
    original = instance.enum_01
    instance.enum_01 = original
    assert instance.enum_01 == original



@given(instance=alldatatypes_Enums_strategy)
def test_alldatatypes_enums_statesMax2_setter(instance):
    original = instance.statesMax2
    instance.statesMax2 = original
    assert instance.statesMax2 == original



@given(instance=alldatatypes_Enums_strategy)
def test_alldatatypes_enums_enum_01_EmptyDefault_setter(instance):
    original = instance.enum_01_EmptyDefault
    instance.enum_01_EmptyDefault = original
    assert instance.enum_01_EmptyDefault == original



@given(instance=alldatatypes_Enums_strategy)
def test_alldatatypes_enums_states_setter(instance):
    original = instance.states
    instance.states = original
    assert instance.states == original



@given(instance=alldatatypes_Enums_strategy)
def test_alldatatypes_enums_enums_setter(instance):
    original = instance.enums
    instance.enums = original
    assert instance.enums == original



@given(instance=alldatatypes_Enums_strategy)
def test_alldatatypes_enums_statesMin1Max2_setter(instance):
    original = instance.statesMin1Max2
    instance.statesMin1Max2 = original
    assert instance.statesMin1Max2 == original



@given(instance=alldatatypes_Enums_strategy)
def test_alldatatypes_enums_notEditableEnum_01_setter(instance):
    original = instance.notEditableEnum_01
    instance.notEditableEnum_01 = original
    assert instance.notEditableEnum_01 == original



@given(instance=alldatatypes_Enums_strategy)
def test_alldatatypes_enums_enum_1_setter(instance):
    original = instance.enum_1
    instance.enum_1 = original
    assert instance.enum_1 == original

@given(instance=alldatatypes_Floats_strategy)
@settings(max_examples=50)
def test_alldatatypes_floats_instantiation(instance):
    assert isinstance(instance, alldatatypes_Floats)



@given(instance=alldatatypes_Floats_strategy)
def test_alldatatypes_floats_float_01_setter(instance):
    original = instance.float_01
    instance.float_01 = original
    assert instance.float_01 == original



@given(instance=alldatatypes_Floats_strategy)
def test_alldatatypes_floats_notEditableFloat_01_setter(instance):
    original = instance.notEditableFloat_01
    instance.notEditableFloat_01 = original
    assert instance.notEditableFloat_01 == original



@given(instance=alldatatypes_Floats_strategy)
def test_alldatatypes_floats_float_01_EmptyDefault_setter(instance):
    original = instance.float_01_EmptyDefault
    instance.float_01_EmptyDefault = original
    assert instance.float_01_EmptyDefault == original



@given(instance=alldatatypes_Floats_strategy)
def test_alldatatypes_floats_float_1_setter(instance):
    original = instance.float_1
    instance.float_1 = original
    assert instance.float_1 == original

@given(instance=alldatatypes_Dates_strategy)
@settings(max_examples=50)
def test_alldatatypes_dates_instantiation(instance):
    assert isinstance(instance, alldatatypes_Dates)



@given(instance=alldatatypes_Dates_strategy)
def test_alldatatypes_dates_notEditableDate_01_setter(instance):
    original = instance.notEditableDate_01
    instance.notEditableDate_01 = original
    assert instance.notEditableDate_01 == original



@given(instance=alldatatypes_Dates_strategy)
def test_alldatatypes_dates_date_1_setter(instance):
    original = instance.date_1
    instance.date_1 = original
    assert instance.date_1 == original



@given(instance=alldatatypes_Dates_strategy)
def test_alldatatypes_dates_date_01_HMS_setter(instance):
    original = instance.date_01_HMS
    instance.date_01_HMS = original
    assert instance.date_01_HMS == original



@given(instance=alldatatypes_Dates_strategy)
def test_alldatatypes_dates_date_01_HMSms_setter(instance):
    original = instance.date_01_HMSms
    instance.date_01_HMSms = original
    assert instance.date_01_HMSms == original



@given(instance=alldatatypes_Dates_strategy)
def test_alldatatypes_dates_date_01_setter(instance):
    original = instance.date_01
    instance.date_01 = original
    assert instance.date_01 == original



@given(instance=alldatatypes_Dates_strategy)
def test_alldatatypes_dates_date_01_HM_setter(instance):
    original = instance.date_01_HM
    instance.date_01_HM = original
    assert instance.date_01_HM == original



@given(instance=alldatatypes_Dates_strategy)
def test_alldatatypes_dates_dates_setter(instance):
    original = instance.dates
    instance.dates = original
    assert instance.dates == original



@given(instance=alldatatypes_Dates_strategy)
def test_alldatatypes_dates_dateEmptyDefault_01_setter(instance):
    original = instance.dateEmptyDefault_01
    instance.dateEmptyDefault_01 = original
    assert instance.dateEmptyDefault_01 == original

@given(instance=alldatatypes_Doubles_strategy)
@settings(max_examples=50)
def test_alldatatypes_doubles_instantiation(instance):
    assert isinstance(instance, alldatatypes_Doubles)



@given(instance=alldatatypes_Doubles_strategy)
def test_alldatatypes_doubles_double_01_EmptyDefault_setter(instance):
    original = instance.double_01_EmptyDefault
    instance.double_01_EmptyDefault = original
    assert instance.double_01_EmptyDefault == original



@given(instance=alldatatypes_Doubles_strategy)
def test_alldatatypes_doubles_double_01_setter(instance):
    original = instance.double_01
    instance.double_01 = original
    assert instance.double_01 == original



@given(instance=alldatatypes_Doubles_strategy)
def test_alldatatypes_doubles_notEditableDouble_01_setter(instance):
    original = instance.notEditableDouble_01
    instance.notEditableDouble_01 = original
    assert instance.notEditableDouble_01 == original



@given(instance=alldatatypes_Doubles_strategy)
def test_alldatatypes_doubles_double_1_setter(instance):
    original = instance.double_1
    instance.double_1 = original
    assert instance.double_1 == original

@given(instance=alldatatypes_Integers_strategy)
@settings(max_examples=50)
def test_alldatatypes_integers_instantiation(instance):
    assert isinstance(instance, alldatatypes_Integers)



@given(instance=alldatatypes_Integers_strategy)
def test_alldatatypes_integers_int_01_EmptyDefault_setter(instance):
    original = instance.int_01_EmptyDefault
    instance.int_01_EmptyDefault = original
    assert instance.int_01_EmptyDefault == original



@given(instance=alldatatypes_Integers_strategy)
def test_alldatatypes_integers_ints_setter(instance):
    original = instance.ints
    instance.ints = original
    assert instance.ints == original



@given(instance=alldatatypes_Integers_strategy)
def test_alldatatypes_integers_hiddenInt_01_setter(instance):
    original = instance.hiddenInt_01
    instance.hiddenInt_01 = original
    assert instance.hiddenInt_01 == original



@given(instance=alldatatypes_Integers_strategy)
def test_alldatatypes_integers_int_1_setter(instance):
    original = instance.int_1
    instance.int_1 = original
    assert instance.int_1 == original



@given(instance=alldatatypes_Integers_strategy)
def test_alldatatypes_integers_int_01_setter(instance):
    original = instance.int_01
    instance.int_01 = original
    assert instance.int_01 == original



@given(instance=alldatatypes_Integers_strategy)
def test_alldatatypes_integers_notEditableInt_01_setter(instance):
    original = instance.notEditableInt_01
    instance.notEditableInt_01 = original
    assert instance.notEditableInt_01 == original

@given(instance=alldatatypes_Longs_strategy)
@settings(max_examples=50)
def test_alldatatypes_longs_instantiation(instance):
    assert isinstance(instance, alldatatypes_Longs)



@given(instance=alldatatypes_Longs_strategy)
def test_alldatatypes_longs_notEditableLong_01_setter(instance):
    original = instance.notEditableLong_01
    instance.notEditableLong_01 = original
    assert instance.notEditableLong_01 == original



@given(instance=alldatatypes_Longs_strategy)
def test_alldatatypes_longs_long_1_setter(instance):
    original = instance.long_1
    instance.long_1 = original
    assert instance.long_1 == original



@given(instance=alldatatypes_Longs_strategy)
def test_alldatatypes_longs_long_01_setter(instance):
    original = instance.long_01
    instance.long_01 = original
    assert instance.long_01 == original



@given(instance=alldatatypes_Longs_strategy)
def test_alldatatypes_longs_long_01_EmptyDefault_setter(instance):
    original = instance.long_01_EmptyDefault
    instance.long_01_EmptyDefault = original
    assert instance.long_01_EmptyDefault == original

@given(instance=alldatatypes_BigDecimals_strategy)
@settings(max_examples=50)
def test_alldatatypes_bigdecimals_instantiation(instance):
    assert isinstance(instance, alldatatypes_BigDecimals)



@given(instance=alldatatypes_BigDecimals_strategy)
def test_alldatatypes_bigdecimals_bigDecimals_setter(instance):
    original = instance.bigDecimals
    instance.bigDecimals = original
    assert instance.bigDecimals == original



@given(instance=alldatatypes_BigDecimals_strategy)
def test_alldatatypes_bigdecimals_notEditableBigDecimal_01_setter(instance):
    original = instance.notEditableBigDecimal_01
    instance.notEditableBigDecimal_01 = original
    assert instance.notEditableBigDecimal_01 == original



@given(instance=alldatatypes_BigDecimals_strategy)
def test_alldatatypes_bigdecimals_bigDecimal_01_EmptyDefault_setter(instance):
    original = instance.bigDecimal_01_EmptyDefault
    instance.bigDecimal_01_EmptyDefault = original
    assert instance.bigDecimal_01_EmptyDefault == original



@given(instance=alldatatypes_BigDecimals_strategy)
def test_alldatatypes_bigdecimals_bigDecimal_01_setter(instance):
    original = instance.bigDecimal_01
    instance.bigDecimal_01 = original
    assert instance.bigDecimal_01 == original



@given(instance=alldatatypes_BigDecimals_strategy)
def test_alldatatypes_bigdecimals_bigDecimal_1_setter(instance):
    original = instance.bigDecimal_1
    instance.bigDecimal_1 = original
    assert instance.bigDecimal_1 == original

@given(instance=alldatatypes_BigIntegers_strategy)
@settings(max_examples=50)
def test_alldatatypes_bigintegers_instantiation(instance):
    assert isinstance(instance, alldatatypes_BigIntegers)



@given(instance=alldatatypes_BigIntegers_strategy)
def test_alldatatypes_bigintegers_bigInts_setter(instance):
    original = instance.bigInts
    instance.bigInts = original
    assert instance.bigInts == original



@given(instance=alldatatypes_BigIntegers_strategy)
def test_alldatatypes_bigintegers_bigInt_01_setter(instance):
    original = instance.bigInt_01
    instance.bigInt_01 = original
    assert instance.bigInt_01 == original



@given(instance=alldatatypes_BigIntegers_strategy)
def test_alldatatypes_bigintegers_bigInt_1_setter(instance):
    original = instance.bigInt_1
    instance.bigInt_1 = original
    assert instance.bigInt_1 == original



@given(instance=alldatatypes_BigIntegers_strategy)
def test_alldatatypes_bigintegers_notEditableBigInt_01_setter(instance):
    original = instance.notEditableBigInt_01
    instance.notEditableBigInt_01 = original
    assert instance.notEditableBigInt_01 == original



@given(instance=alldatatypes_BigIntegers_strategy)
def test_alldatatypes_bigintegers_bigInt_01_EmptyDefault_setter(instance):
    original = instance.bigInt_01_EmptyDefault
    instance.bigInt_01_EmptyDefault = original
    assert instance.bigInt_01_EmptyDefault == original

@given(instance=alldatatypes_Strings_strategy)
@settings(max_examples=50)
def test_alldatatypes_strings_instantiation(instance):
    assert isinstance(instance, alldatatypes_Strings)



@given(instance=alldatatypes_Strings_strategy)
def test_alldatatypes_strings_textarea_setter(instance):
    original = instance.textarea
    instance.textarea = original
    assert instance.textarea == original



@given(instance=alldatatypes_Strings_strategy)
def test_alldatatypes_strings_text_01_setter(instance):
    original = instance.text_01
    instance.text_01 = original
    assert instance.text_01 == original



@given(instance=alldatatypes_Strings_strategy)
def test_alldatatypes_strings_text_1_setter(instance):
    original = instance.text_1
    instance.text_1 = original
    assert instance.text_1 == original



@given(instance=alldatatypes_Strings_strategy)
def test_alldatatypes_strings_notEditableText_01_setter(instance):
    original = instance.notEditableText_01
    instance.notEditableText_01 = original
    assert instance.notEditableText_01 == original



@given(instance=alldatatypes_Strings_strategy)
def test_alldatatypes_strings_link_01_setter(instance):
    original = instance.link_01
    instance.link_01 = original
    assert instance.link_01 == original



@given(instance=alldatatypes_Strings_strategy)
def test_alldatatypes_strings_text_01_EmptyDefault_setter(instance):
    original = instance.text_01_EmptyDefault
    instance.text_01_EmptyDefault = original
    assert instance.text_01_EmptyDefault == original



@given(instance=alldatatypes_Strings_strategy)
def test_alldatatypes_strings_html_01_setter(instance):
    original = instance.html_01
    instance.html_01 = original
    assert instance.html_01 == original

@given(instance=alldatatypes_Type_strategy)
@settings(max_examples=50)
def test_alldatatypes_type_instantiation(instance):
    assert isinstance(instance, alldatatypes_Type)
