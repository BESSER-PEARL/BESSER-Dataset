import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    testModel_Leafs,
    testModel_Node,
    Leafs,
    testModel_multiRefLeaf,
    testModel_upperBoundLeaf,
    testModel_referedLeaf,
    testModel_ContainedLeaf,
    ElementType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_testmodel_leafs_is_not_abstract():
    assert not inspect.isabstract(testModel_Leafs)


def test_testmodel_leafs_constructor_exists():
    assert callable(testModel_Leafs.__init__)


def test_testmodel_leafs_constructor_args():
    sig = inspect.signature(testModel_Leafs.__init__)
    params = list(sig.parameters.keys())



def test_testmodel_node_is_not_abstract():
    assert not inspect.isabstract(testModel_Node)


def test_testmodel_node_constructor_exists():
    assert callable(testModel_Node.__init__)


def test_testmodel_node_constructor_args():
    sig = inspect.signature(testModel_Node.__init__)
    params = list(sig.parameters.keys())
    assert "Boolean" in params, "Missing parameter 'Boolean'"
    assert "bigdeci" in params, "Missing parameter 'bigdeci'"
    assert "name" in params, "Missing parameter 'name'"
    assert "bigint" in params, "Missing parameter 'bigint'"
    assert "byte" in params, "Missing parameter 'byte'"
    assert "bool" in params, "Missing parameter 'bool'"

def test_testmodel_node_has_Boolean():
    assert hasattr(testModel_Node, "Boolean")
    descriptor = None
    for klass in testModel_Node.__mro__:
        if "Boolean" in klass.__dict__:
            descriptor = klass.__dict__["Boolean"]
            break
    assert isinstance(descriptor, property)

def test_testmodel_node_has_bigdeci():
    assert hasattr(testModel_Node, "bigdeci")
    descriptor = None
    for klass in testModel_Node.__mro__:
        if "bigdeci" in klass.__dict__:
            descriptor = klass.__dict__["bigdeci"]
            break
    assert isinstance(descriptor, property)

def test_testmodel_node_has_name():
    assert hasattr(testModel_Node, "name")
    descriptor = None
    for klass in testModel_Node.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_testmodel_node_has_bigint():
    assert hasattr(testModel_Node, "bigint")
    descriptor = None
    for klass in testModel_Node.__mro__:
        if "bigint" in klass.__dict__:
            descriptor = klass.__dict__["bigint"]
            break
    assert isinstance(descriptor, property)

def test_testmodel_node_has_byte():
    assert hasattr(testModel_Node, "byte")
    descriptor = None
    for klass in testModel_Node.__mro__:
        if "byte" in klass.__dict__:
            descriptor = klass.__dict__["byte"]
            break
    assert isinstance(descriptor, property)

def test_testmodel_node_has_bool():
    assert hasattr(testModel_Node, "bool")
    descriptor = None
    for klass in testModel_Node.__mro__:
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



def test_testmodel_multirefleaf_is_not_abstract():
    assert not inspect.isabstract(testModel_multiRefLeaf)


def test_testmodel_multirefleaf_constructor_exists():
    assert callable(testModel_multiRefLeaf.__init__)


def test_testmodel_multirefleaf_constructor_args():
    sig = inspect.signature(testModel_multiRefLeaf.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_testmodel_multirefleaf_has_name():
    assert hasattr(testModel_multiRefLeaf, "name")
    descriptor = None
    for klass in testModel_multiRefLeaf.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_testmodel_upperboundleaf_is_not_abstract():
    assert not inspect.isabstract(testModel_upperBoundLeaf)


def test_testmodel_upperboundleaf_constructor_exists():
    assert callable(testModel_upperBoundLeaf.__init__)


def test_testmodel_upperboundleaf_constructor_args():
    sig = inspect.signature(testModel_upperBoundLeaf.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_testmodel_upperboundleaf_has_name():
    assert hasattr(testModel_upperBoundLeaf, "name")
    descriptor = None
    for klass in testModel_upperBoundLeaf.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_testmodel_referedleaf_is_not_abstract():
    assert not inspect.isabstract(testModel_referedLeaf)


def test_testmodel_referedleaf_constructor_exists():
    assert callable(testModel_referedLeaf.__init__)


def test_testmodel_referedleaf_constructor_args():
    sig = inspect.signature(testModel_referedLeaf.__init__)
    params = list(sig.parameters.keys())
    assert "Float" in params, "Missing parameter 'Float'"
    assert "LongObj" in params, "Missing parameter 'LongObj'"
    assert "ShortObj" in params, "Missing parameter 'ShortObj'"
    assert "short" in params, "Missing parameter 'short'"
    assert "long" in params, "Missing parameter 'long'"
    assert "notChangeable" in params, "Missing parameter 'notChangeable'"
    assert "name" in params, "Missing parameter 'name'"
    assert "int" in params, "Missing parameter 'int'"
    assert "Integer" in params, "Missing parameter 'Integer'"

def test_testmodel_referedleaf_has_Float():
    assert hasattr(testModel_referedLeaf, "Float")
    descriptor = None
    for klass in testModel_referedLeaf.__mro__:
        if "Float" in klass.__dict__:
            descriptor = klass.__dict__["Float"]
            break
    assert isinstance(descriptor, property)

def test_testmodel_referedleaf_has_LongObj():
    assert hasattr(testModel_referedLeaf, "LongObj")
    descriptor = None
    for klass in testModel_referedLeaf.__mro__:
        if "LongObj" in klass.__dict__:
            descriptor = klass.__dict__["LongObj"]
            break
    assert isinstance(descriptor, property)

def test_testmodel_referedleaf_has_ShortObj():
    assert hasattr(testModel_referedLeaf, "ShortObj")
    descriptor = None
    for klass in testModel_referedLeaf.__mro__:
        if "ShortObj" in klass.__dict__:
            descriptor = klass.__dict__["ShortObj"]
            break
    assert isinstance(descriptor, property)

def test_testmodel_referedleaf_has_short():
    assert hasattr(testModel_referedLeaf, "short")
    descriptor = None
    for klass in testModel_referedLeaf.__mro__:
        if "short" in klass.__dict__:
            descriptor = klass.__dict__["short"]
            break
    assert isinstance(descriptor, property)

def test_testmodel_referedleaf_has_long():
    assert hasattr(testModel_referedLeaf, "long")
    descriptor = None
    for klass in testModel_referedLeaf.__mro__:
        if "long" in klass.__dict__:
            descriptor = klass.__dict__["long"]
            break
    assert isinstance(descriptor, property)

def test_testmodel_referedleaf_has_notChangeable():
    assert hasattr(testModel_referedLeaf, "notChangeable")
    descriptor = None
    for klass in testModel_referedLeaf.__mro__:
        if "notChangeable" in klass.__dict__:
            descriptor = klass.__dict__["notChangeable"]
            break
    assert isinstance(descriptor, property)

def test_testmodel_referedleaf_has_name():
    assert hasattr(testModel_referedLeaf, "name")
    descriptor = None
    for klass in testModel_referedLeaf.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_testmodel_referedleaf_has_int():
    assert hasattr(testModel_referedLeaf, "int")
    descriptor = None
    for klass in testModel_referedLeaf.__mro__:
        if "int" in klass.__dict__:
            descriptor = klass.__dict__["int"]
            break
    assert isinstance(descriptor, property)

def test_testmodel_referedleaf_has_Integer():
    assert hasattr(testModel_referedLeaf, "Integer")
    descriptor = None
    for klass in testModel_referedLeaf.__mro__:
        if "Integer" in klass.__dict__:
            descriptor = klass.__dict__["Integer"]
            break
    assert isinstance(descriptor, property)



def test_testmodel_containedleaf_is_not_abstract():
    assert not inspect.isabstract(testModel_ContainedLeaf)


def test_testmodel_containedleaf_constructor_exists():
    assert callable(testModel_ContainedLeaf.__init__)


def test_testmodel_containedleaf_constructor_args():
    sig = inspect.signature(testModel_ContainedLeaf.__init__)
    params = list(sig.parameters.keys())
    assert "char" in params, "Missing parameter 'char'"
    assert "Character" in params, "Missing parameter 'Character'"
    assert "DoubleObj" in params, "Missing parameter 'DoubleObj'"
    assert "name" in params, "Missing parameter 'name'"
    assert "elementType" in params, "Missing parameter 'elementType'"
    assert "byteArray" in params, "Missing parameter 'byteArray'"
    assert "float" in params, "Missing parameter 'float'"
    assert "double" in params, "Missing parameter 'double'"
    assert "byteObject" in params, "Missing parameter 'byteObject'"
    assert "date" in params, "Missing parameter 'date'"

def test_testmodel_containedleaf_has_char():
    assert hasattr(testModel_ContainedLeaf, "char")
    descriptor = None
    for klass in testModel_ContainedLeaf.__mro__:
        if "char" in klass.__dict__:
            descriptor = klass.__dict__["char"]
            break
    assert isinstance(descriptor, property)

def test_testmodel_containedleaf_has_Character():
    assert hasattr(testModel_ContainedLeaf, "Character")
    descriptor = None
    for klass in testModel_ContainedLeaf.__mro__:
        if "Character" in klass.__dict__:
            descriptor = klass.__dict__["Character"]
            break
    assert isinstance(descriptor, property)

def test_testmodel_containedleaf_has_DoubleObj():
    assert hasattr(testModel_ContainedLeaf, "DoubleObj")
    descriptor = None
    for klass in testModel_ContainedLeaf.__mro__:
        if "DoubleObj" in klass.__dict__:
            descriptor = klass.__dict__["DoubleObj"]
            break
    assert isinstance(descriptor, property)

def test_testmodel_containedleaf_has_name():
    assert hasattr(testModel_ContainedLeaf, "name")
    descriptor = None
    for klass in testModel_ContainedLeaf.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_testmodel_containedleaf_has_elementType():
    assert hasattr(testModel_ContainedLeaf, "elementType")
    descriptor = None
    for klass in testModel_ContainedLeaf.__mro__:
        if "elementType" in klass.__dict__:
            descriptor = klass.__dict__["elementType"]
            break
    assert isinstance(descriptor, property)

def test_testmodel_containedleaf_has_byteArray():
    assert hasattr(testModel_ContainedLeaf, "byteArray")
    descriptor = None
    for klass in testModel_ContainedLeaf.__mro__:
        if "byteArray" in klass.__dict__:
            descriptor = klass.__dict__["byteArray"]
            break
    assert isinstance(descriptor, property)

def test_testmodel_containedleaf_has_float():
    assert hasattr(testModel_ContainedLeaf, "float")
    descriptor = None
    for klass in testModel_ContainedLeaf.__mro__:
        if "float" in klass.__dict__:
            descriptor = klass.__dict__["float"]
            break
    assert isinstance(descriptor, property)

def test_testmodel_containedleaf_has_double():
    assert hasattr(testModel_ContainedLeaf, "double")
    descriptor = None
    for klass in testModel_ContainedLeaf.__mro__:
        if "double" in klass.__dict__:
            descriptor = klass.__dict__["double"]
            break
    assert isinstance(descriptor, property)

def test_testmodel_containedleaf_has_byteObject():
    assert hasattr(testModel_ContainedLeaf, "byteObject")
    descriptor = None
    for klass in testModel_ContainedLeaf.__mro__:
        if "byteObject" in klass.__dict__:
            descriptor = klass.__dict__["byteObject"]
            break
    assert isinstance(descriptor, property)

def test_testmodel_containedleaf_has_date():
    assert hasattr(testModel_ContainedLeaf, "date")
    descriptor = None
    for klass in testModel_ContainedLeaf.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)

def test_elementtype_exists():
    # Check that the Enumeration exists
    assert ElementType is not None

def test_elementtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ElementType]
    expected_literals = [
        "Type2",
        "Type1",
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
testModel_Leafs_strategy = st.builds(
    testModel_Leafs,
)
testModel_Node_strategy = st.builds(
    testModel_Node,
    Boolean=
        safe_text,
    bigdeci=
        safe_text,
    name=
        safe_text,
    bigint=
        safe_text,
    byte=
        safe_text,
    bool=
        st.booleans()
)
Leafs_strategy = st.builds(
    Leafs,
)
testModel_multiRefLeaf_strategy = st.builds(
    testModel_multiRefLeaf,
    name=
        safe_text
)
testModel_upperBoundLeaf_strategy = st.builds(
    testModel_upperBoundLeaf,
    name=
        safe_text
)
testModel_referedLeaf_strategy = st.builds(
    testModel_referedLeaf,
    Float=
        safe_text,
    LongObj=
        safe_text,
    ShortObj=
        safe_text,
    short=
        safe_text,
    long=
        safe_text,
    notChangeable=
        safe_text,
    name=
        safe_text,
    int=
        st.integers(),
    Integer=
        safe_text
)
testModel_ContainedLeaf_strategy = st.builds(
    testModel_ContainedLeaf,
    char=
        safe_text,
    Character=
        safe_text,
    DoubleObj=
        safe_text,
    name=
        safe_text,
    elementType=
        safe_text,
    byteArray=
        safe_text,
    float=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    double=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    byteObject=
        safe_text,
    date=
        st.dates()
)

@given(instance=testModel_Leafs_strategy)
@settings(max_examples=50)
def test_testmodel_leafs_instantiation(instance):
    assert isinstance(instance, testModel_Leafs)

@given(instance=testModel_Node_strategy)
@settings(max_examples=50)
def test_testmodel_node_instantiation(instance):
    assert isinstance(instance, testModel_Node)



@given(instance=testModel_Node_strategy)
def test_testmodel_node_Boolean_setter(instance):
    original = instance.Boolean
    instance.Boolean = original
    assert instance.Boolean == original



@given(instance=testModel_Node_strategy)
def test_testmodel_node_bigdeci_setter(instance):
    original = instance.bigdeci
    instance.bigdeci = original
    assert instance.bigdeci == original



@given(instance=testModel_Node_strategy)
def test_testmodel_node_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=testModel_Node_strategy)
def test_testmodel_node_bigint_setter(instance):
    original = instance.bigint
    instance.bigint = original
    assert instance.bigint == original



@given(instance=testModel_Node_strategy)
def test_testmodel_node_byte_setter(instance):
    original = instance.byte
    instance.byte = original
    assert instance.byte == original



@given(instance=testModel_Node_strategy)
def test_testmodel_node_bool_setter(instance):
    original = instance.bool
    instance.bool = original
    assert instance.bool == original

@given(instance=Leafs_strategy)
@settings(max_examples=50)
def test_leafs_instantiation(instance):
    assert isinstance(instance, Leafs)

@given(instance=testModel_multiRefLeaf_strategy)
@settings(max_examples=50)
def test_testmodel_multirefleaf_instantiation(instance):
    assert isinstance(instance, testModel_multiRefLeaf)



@given(instance=testModel_multiRefLeaf_strategy)
def test_testmodel_multirefleaf_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=testModel_upperBoundLeaf_strategy)
@settings(max_examples=50)
def test_testmodel_upperboundleaf_instantiation(instance):
    assert isinstance(instance, testModel_upperBoundLeaf)



@given(instance=testModel_upperBoundLeaf_strategy)
def test_testmodel_upperboundleaf_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=testModel_referedLeaf_strategy)
@settings(max_examples=50)
def test_testmodel_referedleaf_instantiation(instance):
    assert isinstance(instance, testModel_referedLeaf)



@given(instance=testModel_referedLeaf_strategy)
def test_testmodel_referedleaf_Float_setter(instance):
    original = instance.Float
    instance.Float = original
    assert instance.Float == original



@given(instance=testModel_referedLeaf_strategy)
def test_testmodel_referedleaf_LongObj_setter(instance):
    original = instance.LongObj
    instance.LongObj = original
    assert instance.LongObj == original



@given(instance=testModel_referedLeaf_strategy)
def test_testmodel_referedleaf_ShortObj_setter(instance):
    original = instance.ShortObj
    instance.ShortObj = original
    assert instance.ShortObj == original



@given(instance=testModel_referedLeaf_strategy)
def test_testmodel_referedleaf_short_setter(instance):
    original = instance.short
    instance.short = original
    assert instance.short == original



@given(instance=testModel_referedLeaf_strategy)
def test_testmodel_referedleaf_long_setter(instance):
    original = instance.long
    instance.long = original
    assert instance.long == original



@given(instance=testModel_referedLeaf_strategy)
def test_testmodel_referedleaf_notChangeable_setter(instance):
    original = instance.notChangeable
    instance.notChangeable = original
    assert instance.notChangeable == original



@given(instance=testModel_referedLeaf_strategy)
def test_testmodel_referedleaf_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=testModel_referedLeaf_strategy)
def test_testmodel_referedleaf_int_setter(instance):
    original = instance.int
    instance.int = original
    assert instance.int == original



@given(instance=testModel_referedLeaf_strategy)
def test_testmodel_referedleaf_Integer_setter(instance):
    original = instance.Integer
    instance.Integer = original
    assert instance.Integer == original

@given(instance=testModel_ContainedLeaf_strategy)
@settings(max_examples=50)
def test_testmodel_containedleaf_instantiation(instance):
    assert isinstance(instance, testModel_ContainedLeaf)



@given(instance=testModel_ContainedLeaf_strategy)
def test_testmodel_containedleaf_char_setter(instance):
    original = instance.char
    instance.char = original
    assert instance.char == original



@given(instance=testModel_ContainedLeaf_strategy)
def test_testmodel_containedleaf_Character_setter(instance):
    original = instance.Character
    instance.Character = original
    assert instance.Character == original



@given(instance=testModel_ContainedLeaf_strategy)
def test_testmodel_containedleaf_DoubleObj_setter(instance):
    original = instance.DoubleObj
    instance.DoubleObj = original
    assert instance.DoubleObj == original



@given(instance=testModel_ContainedLeaf_strategy)
def test_testmodel_containedleaf_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=testModel_ContainedLeaf_strategy)
def test_testmodel_containedleaf_elementType_setter(instance):
    original = instance.elementType
    instance.elementType = original
    assert instance.elementType == original



@given(instance=testModel_ContainedLeaf_strategy)
def test_testmodel_containedleaf_byteArray_setter(instance):
    original = instance.byteArray
    instance.byteArray = original
    assert instance.byteArray == original



@given(instance=testModel_ContainedLeaf_strategy)
def test_testmodel_containedleaf_float_setter(instance):
    original = instance.float
    instance.float = original
    assert instance.float == original



@given(instance=testModel_ContainedLeaf_strategy)
def test_testmodel_containedleaf_double_setter(instance):
    original = instance.double
    instance.double = original
    assert instance.double == original



@given(instance=testModel_ContainedLeaf_strategy)
def test_testmodel_containedleaf_byteObject_setter(instance):
    original = instance.byteObject
    instance.byteObject = original
    assert instance.byteObject == original



@given(instance=testModel_ContainedLeaf_strategy)
def test_testmodel_containedleaf_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original
