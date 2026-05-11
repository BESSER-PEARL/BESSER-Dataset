import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    testModel::Leafs,
    testModel::Node,
    Leafs,
    testModel::multiRefLeaf,
    testModel::upperBoundLeaf,
    testModel::referedLeaf,
    testModel::ContainedLeaf,
    ElementType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_testmodel::leafs_is_not_abstract():
    assert not inspect.isabstract(testModel::Leafs)


def test_testmodel::leafs_constructor_exists():
    assert callable(testModel::Leafs.__init__)


def test_testmodel::leafs_constructor_args():
    sig = inspect.signature(testModel::Leafs.__init__)
    params = list(sig.parameters.keys())



def test_testmodel::node_is_not_abstract():
    assert not inspect.isabstract(testModel::Node)


def test_testmodel::node_constructor_exists():
    assert callable(testModel::Node.__init__)


def test_testmodel::node_constructor_args():
    sig = inspect.signature(testModel::Node.__init__)
    params = list(sig.parameters.keys())
    assert "bigint" in params, "Missing parameter 'bigint'"
    assert "Boolean" in params, "Missing parameter 'Boolean'"
    assert "name" in params, "Missing parameter 'name'"
    assert "byte" in params, "Missing parameter 'byte'"
    assert "bigdeci" in params, "Missing parameter 'bigdeci'"
    assert "bool" in params, "Missing parameter 'bool'"

def test_testmodel::node_has_bigint():
    assert hasattr(testModel::Node, "bigint")
    descriptor = None
    for klass in testModel::Node.__mro__:
        if "bigint" in klass.__dict__:
            descriptor = klass.__dict__["bigint"]
            break
    assert isinstance(descriptor, property)

def test_testmodel::node_has_Boolean():
    assert hasattr(testModel::Node, "Boolean")
    descriptor = None
    for klass in testModel::Node.__mro__:
        if "Boolean" in klass.__dict__:
            descriptor = klass.__dict__["Boolean"]
            break
    assert isinstance(descriptor, property)

def test_testmodel::node_has_name():
    assert hasattr(testModel::Node, "name")
    descriptor = None
    for klass in testModel::Node.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_testmodel::node_has_byte():
    assert hasattr(testModel::Node, "byte")
    descriptor = None
    for klass in testModel::Node.__mro__:
        if "byte" in klass.__dict__:
            descriptor = klass.__dict__["byte"]
            break
    assert isinstance(descriptor, property)

def test_testmodel::node_has_bigdeci():
    assert hasattr(testModel::Node, "bigdeci")
    descriptor = None
    for klass in testModel::Node.__mro__:
        if "bigdeci" in klass.__dict__:
            descriptor = klass.__dict__["bigdeci"]
            break
    assert isinstance(descriptor, property)

def test_testmodel::node_has_bool():
    assert hasattr(testModel::Node, "bool")
    descriptor = None
    for klass in testModel::Node.__mro__:
        if "bool" in klass.__dict__:
            descriptor = klass.__dict__["bool"]
            break
    assert isinstance(descriptor, property)



def test_leafs_is_not_abstract():
    assert not inspect.isabstract(Leafs)


def test_leafs_constructor_exists():
    assert callable(Leafs.__init__)


def test_leafs_constructor_args():
    sig = inspect.signature(Leafs.__init__)
    params = list(sig.parameters.keys())



def test_testmodel::multirefleaf_is_not_abstract():
    assert not inspect.isabstract(testModel::multiRefLeaf)


def test_testmodel::multirefleaf_constructor_exists():
    assert callable(testModel::multiRefLeaf.__init__)


def test_testmodel::multirefleaf_constructor_args():
    sig = inspect.signature(testModel::multiRefLeaf.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_testmodel::multirefleaf_has_name():
    assert hasattr(testModel::multiRefLeaf, "name")
    descriptor = None
    for klass in testModel::multiRefLeaf.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_testmodel::upperboundleaf_is_not_abstract():
    assert not inspect.isabstract(testModel::upperBoundLeaf)


def test_testmodel::upperboundleaf_constructor_exists():
    assert callable(testModel::upperBoundLeaf.__init__)


def test_testmodel::upperboundleaf_constructor_args():
    sig = inspect.signature(testModel::upperBoundLeaf.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_testmodel::upperboundleaf_has_name():
    assert hasattr(testModel::upperBoundLeaf, "name")
    descriptor = None
    for klass in testModel::upperBoundLeaf.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_testmodel::referedleaf_is_not_abstract():
    assert not inspect.isabstract(testModel::referedLeaf)


def test_testmodel::referedleaf_constructor_exists():
    assert callable(testModel::referedLeaf.__init__)


def test_testmodel::referedleaf_constructor_args():
    sig = inspect.signature(testModel::referedLeaf.__init__)
    params = list(sig.parameters.keys())
    assert "ShortObj" in params, "Missing parameter 'ShortObj'"
    assert "name" in params, "Missing parameter 'name'"
    assert "Float" in params, "Missing parameter 'Float'"
    assert "int" in params, "Missing parameter 'int'"
    assert "Integer" in params, "Missing parameter 'Integer'"
    assert "short" in params, "Missing parameter 'short'"
    assert "LongObj" in params, "Missing parameter 'LongObj'"
    assert "long" in params, "Missing parameter 'long'"
    assert "notChangeable" in params, "Missing parameter 'notChangeable'"

def test_testmodel::referedleaf_has_ShortObj():
    assert hasattr(testModel::referedLeaf, "ShortObj")
    descriptor = None
    for klass in testModel::referedLeaf.__mro__:
        if "ShortObj" in klass.__dict__:
            descriptor = klass.__dict__["ShortObj"]
            break
    assert isinstance(descriptor, property)

def test_testmodel::referedleaf_has_name():
    assert hasattr(testModel::referedLeaf, "name")
    descriptor = None
    for klass in testModel::referedLeaf.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_testmodel::referedleaf_has_Float():
    assert hasattr(testModel::referedLeaf, "Float")
    descriptor = None
    for klass in testModel::referedLeaf.__mro__:
        if "Float" in klass.__dict__:
            descriptor = klass.__dict__["Float"]
            break
    assert isinstance(descriptor, property)

def test_testmodel::referedleaf_has_int():
    assert hasattr(testModel::referedLeaf, "int")
    descriptor = None
    for klass in testModel::referedLeaf.__mro__:
        if "int" in klass.__dict__:
            descriptor = klass.__dict__["int"]
            break
    assert isinstance(descriptor, property)

def test_testmodel::referedleaf_has_Integer():
    assert hasattr(testModel::referedLeaf, "Integer")
    descriptor = None
    for klass in testModel::referedLeaf.__mro__:
        if "Integer" in klass.__dict__:
            descriptor = klass.__dict__["Integer"]
            break
    assert isinstance(descriptor, property)

def test_testmodel::referedleaf_has_short():
    assert hasattr(testModel::referedLeaf, "short")
    descriptor = None
    for klass in testModel::referedLeaf.__mro__:
        if "short" in klass.__dict__:
            descriptor = klass.__dict__["short"]
            break
    assert isinstance(descriptor, property)

def test_testmodel::referedleaf_has_LongObj():
    assert hasattr(testModel::referedLeaf, "LongObj")
    descriptor = None
    for klass in testModel::referedLeaf.__mro__:
        if "LongObj" in klass.__dict__:
            descriptor = klass.__dict__["LongObj"]
            break
    assert isinstance(descriptor, property)

def test_testmodel::referedleaf_has_long():
    assert hasattr(testModel::referedLeaf, "long")
    descriptor = None
    for klass in testModel::referedLeaf.__mro__:
        if "long" in klass.__dict__:
            descriptor = klass.__dict__["long"]
            break
    assert isinstance(descriptor, property)

def test_testmodel::referedleaf_has_notChangeable():
    assert hasattr(testModel::referedLeaf, "notChangeable")
    descriptor = None
    for klass in testModel::referedLeaf.__mro__:
        if "notChangeable" in klass.__dict__:
            descriptor = klass.__dict__["notChangeable"]
            break
    assert isinstance(descriptor, property)



def test_testmodel::containedleaf_is_not_abstract():
    assert not inspect.isabstract(testModel::ContainedLeaf)


def test_testmodel::containedleaf_constructor_exists():
    assert callable(testModel::ContainedLeaf.__init__)


def test_testmodel::containedleaf_constructor_args():
    sig = inspect.signature(testModel::ContainedLeaf.__init__)
    params = list(sig.parameters.keys())
    assert "Character" in params, "Missing parameter 'Character'"
    assert "byteArray" in params, "Missing parameter 'byteArray'"
    assert "byteObject" in params, "Missing parameter 'byteObject'"
    assert "elementType" in params, "Missing parameter 'elementType'"
    assert "double" in params, "Missing parameter 'double'"
    assert "DoubleObj" in params, "Missing parameter 'DoubleObj'"
    assert "float" in params, "Missing parameter 'float'"
    assert "char" in params, "Missing parameter 'char'"
    assert "date" in params, "Missing parameter 'date'"
    assert "name" in params, "Missing parameter 'name'"

def test_testmodel::containedleaf_has_Character():
    assert hasattr(testModel::ContainedLeaf, "Character")
    descriptor = None
    for klass in testModel::ContainedLeaf.__mro__:
        if "Character" in klass.__dict__:
            descriptor = klass.__dict__["Character"]
            break
    assert isinstance(descriptor, property)

def test_testmodel::containedleaf_has_byteArray():
    assert hasattr(testModel::ContainedLeaf, "byteArray")
    descriptor = None
    for klass in testModel::ContainedLeaf.__mro__:
        if "byteArray" in klass.__dict__:
            descriptor = klass.__dict__["byteArray"]
            break
    assert isinstance(descriptor, property)

def test_testmodel::containedleaf_has_byteObject():
    assert hasattr(testModel::ContainedLeaf, "byteObject")
    descriptor = None
    for klass in testModel::ContainedLeaf.__mro__:
        if "byteObject" in klass.__dict__:
            descriptor = klass.__dict__["byteObject"]
            break
    assert isinstance(descriptor, property)

def test_testmodel::containedleaf_has_elementType():
    assert hasattr(testModel::ContainedLeaf, "elementType")
    descriptor = None
    for klass in testModel::ContainedLeaf.__mro__:
        if "elementType" in klass.__dict__:
            descriptor = klass.__dict__["elementType"]
            break
    assert isinstance(descriptor, property)

def test_testmodel::containedleaf_has_double():
    assert hasattr(testModel::ContainedLeaf, "double")
    descriptor = None
    for klass in testModel::ContainedLeaf.__mro__:
        if "double" in klass.__dict__:
            descriptor = klass.__dict__["double"]
            break
    assert isinstance(descriptor, property)

def test_testmodel::containedleaf_has_DoubleObj():
    assert hasattr(testModel::ContainedLeaf, "DoubleObj")
    descriptor = None
    for klass in testModel::ContainedLeaf.__mro__:
        if "DoubleObj" in klass.__dict__:
            descriptor = klass.__dict__["DoubleObj"]
            break
    assert isinstance(descriptor, property)

def test_testmodel::containedleaf_has_float():
    assert hasattr(testModel::ContainedLeaf, "float")
    descriptor = None
    for klass in testModel::ContainedLeaf.__mro__:
        if "float" in klass.__dict__:
            descriptor = klass.__dict__["float"]
            break
    assert isinstance(descriptor, property)

def test_testmodel::containedleaf_has_char():
    assert hasattr(testModel::ContainedLeaf, "char")
    descriptor = None
    for klass in testModel::ContainedLeaf.__mro__:
        if "char" in klass.__dict__:
            descriptor = klass.__dict__["char"]
            break
    assert isinstance(descriptor, property)

def test_testmodel::containedleaf_has_date():
    assert hasattr(testModel::ContainedLeaf, "date")
    descriptor = None
    for klass in testModel::ContainedLeaf.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)

def test_testmodel::containedleaf_has_name():
    assert hasattr(testModel::ContainedLeaf, "name")
    descriptor = None
    for klass in testModel::ContainedLeaf.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_elementtype_exists():
    # Check that the Enumeration exists
    assert ElementType is not None

def test_elementtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ElementType]
    expected_literals = [
        "Type1",
        "Type2",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ElementType"


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
testModel::Leafs_strategy = st.builds(
    testModel::Leafs,
)
testModel::Node_strategy = st.builds(
    testModel::Node,
    bigint=
        safe_text,
    Boolean=
        safe_text,
    name=
        safe_text,
    byte=
        safe_text,
    bigdeci=
        safe_text,
    bool=
        st.booleans()
)
Leafs_strategy = st.builds(
    Leafs,
)
testModel::multiRefLeaf_strategy = st.builds(
    testModel::multiRefLeaf,
    name=
        safe_text
)
testModel::upperBoundLeaf_strategy = st.builds(
    testModel::upperBoundLeaf,
    name=
        safe_text
)
testModel::referedLeaf_strategy = st.builds(
    testModel::referedLeaf,
    ShortObj=
        safe_text,
    name=
        safe_text,
    Float=
        safe_text,
    int=
        st.integers(),
    Integer=
        safe_text,
    short=
        safe_text,
    LongObj=
        safe_text,
    long=
        safe_text,
    notChangeable=
        safe_text
)
testModel::ContainedLeaf_strategy = st.builds(
    testModel::ContainedLeaf,
    Character=
        safe_text,
    byteArray=
        safe_text,
    byteObject=
        safe_text,
    elementType=
        safe_text,
    double=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    DoubleObj=
        safe_text,
    float=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    char=
        safe_text,
    date=
        st.dates(),
    name=
        safe_text
)

@given(instance=testModel::Leafs_strategy)
@settings(max_examples=50)
def test_testmodel::leafs_instantiation(instance):
    assert isinstance(instance, testModel::Leafs)

@given(instance=testModel::Node_strategy)
@settings(max_examples=50)
def test_testmodel::node_instantiation(instance):
    assert isinstance(instance, testModel::Node)

@given(instance=testModel::Node_strategy)
def test_testmodel::node_bigint_type(instance):
    assert isinstance(instance.bigint, str)


@given(instance=testModel::Node_strategy)
def test_testmodel::node_bigint_setter(instance):
    original = instance.bigint
    instance.bigint = original
    assert instance.bigint == original

@given(instance=testModel::Node_strategy)
def test_testmodel::node_Boolean_type(instance):
    assert isinstance(instance.Boolean, str)


@given(instance=testModel::Node_strategy)
def test_testmodel::node_Boolean_setter(instance):
    original = instance.Boolean
    instance.Boolean = original
    assert instance.Boolean == original

@given(instance=testModel::Node_strategy)
def test_testmodel::node_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=testModel::Node_strategy)
def test_testmodel::node_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=testModel::Node_strategy)
def test_testmodel::node_byte_type(instance):
    assert isinstance(instance.byte, str)


@given(instance=testModel::Node_strategy)
def test_testmodel::node_byte_setter(instance):
    original = instance.byte
    instance.byte = original
    assert instance.byte == original

@given(instance=testModel::Node_strategy)
def test_testmodel::node_bigdeci_type(instance):
    assert isinstance(instance.bigdeci, str)


@given(instance=testModel::Node_strategy)
def test_testmodel::node_bigdeci_setter(instance):
    original = instance.bigdeci
    instance.bigdeci = original
    assert instance.bigdeci == original

@given(instance=testModel::Node_strategy)
def test_testmodel::node_bool_type(instance):
    assert isinstance(instance.bool, bool)


@given(instance=testModel::Node_strategy)
def test_testmodel::node_bool_setter(instance):
    original = instance.bool
    instance.bool = original
    assert instance.bool == original

@given(instance=Leafs_strategy)
@settings(max_examples=50)
def test_leafs_instantiation(instance):
    assert isinstance(instance, Leafs)

@given(instance=testModel::multiRefLeaf_strategy)
@settings(max_examples=50)
def test_testmodel::multirefleaf_instantiation(instance):
    assert isinstance(instance, testModel::multiRefLeaf)

@given(instance=testModel::multiRefLeaf_strategy)
def test_testmodel::multirefleaf_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=testModel::multiRefLeaf_strategy)
def test_testmodel::multirefleaf_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=testModel::upperBoundLeaf_strategy)
@settings(max_examples=50)
def test_testmodel::upperboundleaf_instantiation(instance):
    assert isinstance(instance, testModel::upperBoundLeaf)

@given(instance=testModel::upperBoundLeaf_strategy)
def test_testmodel::upperboundleaf_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=testModel::upperBoundLeaf_strategy)
def test_testmodel::upperboundleaf_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=testModel::referedLeaf_strategy)
@settings(max_examples=50)
def test_testmodel::referedleaf_instantiation(instance):
    assert isinstance(instance, testModel::referedLeaf)

@given(instance=testModel::referedLeaf_strategy)
def test_testmodel::referedleaf_ShortObj_type(instance):
    assert isinstance(instance.ShortObj, str)


@given(instance=testModel::referedLeaf_strategy)
def test_testmodel::referedleaf_ShortObj_setter(instance):
    original = instance.ShortObj
    instance.ShortObj = original
    assert instance.ShortObj == original

@given(instance=testModel::referedLeaf_strategy)
def test_testmodel::referedleaf_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=testModel::referedLeaf_strategy)
def test_testmodel::referedleaf_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=testModel::referedLeaf_strategy)
def test_testmodel::referedleaf_Float_type(instance):
    assert isinstance(instance.Float, str)


@given(instance=testModel::referedLeaf_strategy)
def test_testmodel::referedleaf_Float_setter(instance):
    original = instance.Float
    instance.Float = original
    assert instance.Float == original

@given(instance=testModel::referedLeaf_strategy)
def test_testmodel::referedleaf_int_type(instance):
    assert isinstance(instance.int, int)


@given(instance=testModel::referedLeaf_strategy)
def test_testmodel::referedleaf_int_setter(instance):
    original = instance.int
    instance.int = original
    assert instance.int == original

@given(instance=testModel::referedLeaf_strategy)
def test_testmodel::referedleaf_Integer_type(instance):
    assert isinstance(instance.Integer, str)


@given(instance=testModel::referedLeaf_strategy)
def test_testmodel::referedleaf_Integer_setter(instance):
    original = instance.Integer
    instance.Integer = original
    assert instance.Integer == original

@given(instance=testModel::referedLeaf_strategy)
def test_testmodel::referedleaf_short_type(instance):
    assert isinstance(instance.short, str)


@given(instance=testModel::referedLeaf_strategy)
def test_testmodel::referedleaf_short_setter(instance):
    original = instance.short
    instance.short = original
    assert instance.short == original

@given(instance=testModel::referedLeaf_strategy)
def test_testmodel::referedleaf_LongObj_type(instance):
    assert isinstance(instance.LongObj, str)


@given(instance=testModel::referedLeaf_strategy)
def test_testmodel::referedleaf_LongObj_setter(instance):
    original = instance.LongObj
    instance.LongObj = original
    assert instance.LongObj == original

@given(instance=testModel::referedLeaf_strategy)
def test_testmodel::referedleaf_long_type(instance):
    assert isinstance(instance.long, str)


@given(instance=testModel::referedLeaf_strategy)
def test_testmodel::referedleaf_long_setter(instance):
    original = instance.long
    instance.long = original
    assert instance.long == original

@given(instance=testModel::referedLeaf_strategy)
def test_testmodel::referedleaf_notChangeable_type(instance):
    assert isinstance(instance.notChangeable, str)


@given(instance=testModel::referedLeaf_strategy)
def test_testmodel::referedleaf_notChangeable_setter(instance):
    original = instance.notChangeable
    instance.notChangeable = original
    assert instance.notChangeable == original

@given(instance=testModel::ContainedLeaf_strategy)
@settings(max_examples=50)
def test_testmodel::containedleaf_instantiation(instance):
    assert isinstance(instance, testModel::ContainedLeaf)

@given(instance=testModel::ContainedLeaf_strategy)
def test_testmodel::containedleaf_Character_type(instance):
    assert isinstance(instance.Character, str)


@given(instance=testModel::ContainedLeaf_strategy)
def test_testmodel::containedleaf_Character_setter(instance):
    original = instance.Character
    instance.Character = original
    assert instance.Character == original

@given(instance=testModel::ContainedLeaf_strategy)
def test_testmodel::containedleaf_byteArray_type(instance):
    assert isinstance(instance.byteArray, str)


@given(instance=testModel::ContainedLeaf_strategy)
def test_testmodel::containedleaf_byteArray_setter(instance):
    original = instance.byteArray
    instance.byteArray = original
    assert instance.byteArray == original

@given(instance=testModel::ContainedLeaf_strategy)
def test_testmodel::containedleaf_byteObject_type(instance):
    assert isinstance(instance.byteObject, str)


@given(instance=testModel::ContainedLeaf_strategy)
def test_testmodel::containedleaf_byteObject_setter(instance):
    original = instance.byteObject
    instance.byteObject = original
    assert instance.byteObject == original

@given(instance=testModel::ContainedLeaf_strategy)
def test_testmodel::containedleaf_elementType_type(instance):
    assert isinstance(instance.elementType, str)


@given(instance=testModel::ContainedLeaf_strategy)
def test_testmodel::containedleaf_elementType_setter(instance):
    original = instance.elementType
    instance.elementType = original
    assert instance.elementType == original

@given(instance=testModel::ContainedLeaf_strategy)
def test_testmodel::containedleaf_double_type(instance):
    assert isinstance(instance.double, float)


@given(instance=testModel::ContainedLeaf_strategy)
def test_testmodel::containedleaf_double_setter(instance):
    original = instance.double
    instance.double = original
    assert instance.double == original

@given(instance=testModel::ContainedLeaf_strategy)
def test_testmodel::containedleaf_DoubleObj_type(instance):
    assert isinstance(instance.DoubleObj, str)


@given(instance=testModel::ContainedLeaf_strategy)
def test_testmodel::containedleaf_DoubleObj_setter(instance):
    original = instance.DoubleObj
    instance.DoubleObj = original
    assert instance.DoubleObj == original

@given(instance=testModel::ContainedLeaf_strategy)
def test_testmodel::containedleaf_float_type(instance):
    assert isinstance(instance.float, float)


@given(instance=testModel::ContainedLeaf_strategy)
def test_testmodel::containedleaf_float_setter(instance):
    original = instance.float
    instance.float = original
    assert instance.float == original

@given(instance=testModel::ContainedLeaf_strategy)
def test_testmodel::containedleaf_char_type(instance):
    assert isinstance(instance.char, str)


@given(instance=testModel::ContainedLeaf_strategy)
def test_testmodel::containedleaf_char_setter(instance):
    original = instance.char
    instance.char = original
    assert instance.char == original

@given(instance=testModel::ContainedLeaf_strategy)
def test_testmodel::containedleaf_date_type(instance):
    assert isinstance(instance.date, date)


@given(instance=testModel::ContainedLeaf_strategy)
def test_testmodel::containedleaf_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original

@given(instance=testModel::ContainedLeaf_strategy)
def test_testmodel::containedleaf_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=testModel::ContainedLeaf_strategy)
def test_testmodel::containedleaf_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
