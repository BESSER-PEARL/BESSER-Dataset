import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    fmp_Project,
    Node,
    fmp_Clonable,
    fmp_FeatureGroup,
    fmp_Constraint,
    fmp_Node,
    fmp_TypedValue,
    Clonable,
    fmp_Reference,
    fmp_Feature,
    ConfigState,
    ValueType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_fmp_project_is_not_abstract():
    assert not inspect.isabstract(fmp_Project)


def test_fmp_project_constructor_exists():
    assert callable(fmp_Project.__init__)


def test_fmp_project_constructor_args():
    sig = inspect.signature(fmp_Project.__init__)
    params = list(sig.parameters.keys())



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_fmp_clonable_is_not_abstract():
    assert not inspect.isabstract(fmp_Clonable)


def test_fmp_clonable_constructor_exists():
    assert callable(fmp_Clonable.__init__)


def test_fmp_clonable_constructor_args():
    sig = inspect.signature(fmp_Clonable.__init__)
    params = list(sig.parameters.keys())
    assert "state" in params, "Missing parameter 'state'"

def test_fmp_clonable_has_state():
    assert hasattr(fmp_Clonable, "state")
    descriptor = None
    for klass in fmp_Clonable.__mro__:
        if "state" in klass.__dict__:
            descriptor = klass.__dict__["state"]
            break
    assert isinstance(descriptor, property)



def test_fmp_featuregroup_is_not_abstract():
    assert not inspect.isabstract(fmp_FeatureGroup)


def test_fmp_featuregroup_constructor_exists():
    assert callable(fmp_FeatureGroup.__init__)


def test_fmp_featuregroup_constructor_args():
    sig = inspect.signature(fmp_FeatureGroup.__init__)
    params = list(sig.parameters.keys())



def test_fmp_constraint_is_not_abstract():
    assert not inspect.isabstract(fmp_Constraint)


def test_fmp_constraint_constructor_exists():
    assert callable(fmp_Constraint.__init__)


def test_fmp_constraint_constructor_args():
    sig = inspect.signature(fmp_Constraint.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_fmp_constraint_has_text():
    assert hasattr(fmp_Constraint, "text")
    descriptor = None
    for klass in fmp_Constraint.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_fmp_node_is_not_abstract():
    assert not inspect.isabstract(fmp_Node)


def test_fmp_node_constructor_exists():
    assert callable(fmp_Node.__init__)


def test_fmp_node_constructor_args():
    sig = inspect.signature(fmp_Node.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "max" in params, "Missing parameter 'max'"
    assert "min" in params, "Missing parameter 'min'"

def test_fmp_node_has_id():
    assert hasattr(fmp_Node, "id")
    descriptor = None
    for klass in fmp_Node.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_fmp_node_has_max():
    assert hasattr(fmp_Node, "max")
    descriptor = None
    for klass in fmp_Node.__mro__:
        if "max" in klass.__dict__:
            descriptor = klass.__dict__["max"]
            break
    assert isinstance(descriptor, property)

def test_fmp_node_has_min():
    assert hasattr(fmp_Node, "min")
    descriptor = None
    for klass in fmp_Node.__mro__:
        if "min" in klass.__dict__:
            descriptor = klass.__dict__["min"]
            break
    assert isinstance(descriptor, property)



def test_fmp_typedvalue_is_not_abstract():
    assert not inspect.isabstract(fmp_TypedValue)


def test_fmp_typedvalue_constructor_exists():
    assert callable(fmp_TypedValue.__init__)


def test_fmp_typedvalue_constructor_args():
    sig = inspect.signature(fmp_TypedValue.__init__)
    params = list(sig.parameters.keys())
    assert "stringValue" in params, "Missing parameter 'stringValue'"
    assert "integerValue" in params, "Missing parameter 'integerValue'"
    assert "floatValue" in params, "Missing parameter 'floatValue'"

def test_fmp_typedvalue_has_stringValue():
    assert hasattr(fmp_TypedValue, "stringValue")
    descriptor = None
    for klass in fmp_TypedValue.__mro__:
        if "stringValue" in klass.__dict__:
            descriptor = klass.__dict__["stringValue"]
            break
    assert isinstance(descriptor, property)

def test_fmp_typedvalue_has_integerValue():
    assert hasattr(fmp_TypedValue, "integerValue")
    descriptor = None
    for klass in fmp_TypedValue.__mro__:
        if "integerValue" in klass.__dict__:
            descriptor = klass.__dict__["integerValue"]
            break
    assert isinstance(descriptor, property)

def test_fmp_typedvalue_has_floatValue():
    assert hasattr(fmp_TypedValue, "floatValue")
    descriptor = None
    for klass in fmp_TypedValue.__mro__:
        if "floatValue" in klass.__dict__:
            descriptor = klass.__dict__["floatValue"]
            break
    assert isinstance(descriptor, property)



def test_clonable_is_not_abstract():
    assert not inspect.isabstract(Clonable)


def test_clonable_constructor_exists():
    assert callable(Clonable.__init__)


def test_clonable_constructor_args():
    sig = inspect.signature(Clonable.__init__)
    params = list(sig.parameters.keys())



def test_fmp_reference_is_not_abstract():
    assert not inspect.isabstract(fmp_Reference)


def test_fmp_reference_constructor_exists():
    assert callable(fmp_Reference.__init__)


def test_fmp_reference_constructor_args():
    sig = inspect.signature(fmp_Reference.__init__)
    params = list(sig.parameters.keys())



def test_fmp_feature_is_not_abstract():
    assert not inspect.isabstract(fmp_Feature)


def test_fmp_feature_constructor_exists():
    assert callable(fmp_Feature.__init__)


def test_fmp_feature_constructor_args():
    sig = inspect.signature(fmp_Feature.__init__)
    params = list(sig.parameters.keys())
    assert "valueType" in params, "Missing parameter 'valueType'"
    assert "name" in params, "Missing parameter 'name'"

def test_fmp_feature_has_valueType():
    assert hasattr(fmp_Feature, "valueType")
    descriptor = None
    for klass in fmp_Feature.__mro__:
        if "valueType" in klass.__dict__:
            descriptor = klass.__dict__["valueType"]
            break
    assert isinstance(descriptor, property)

def test_fmp_feature_has_name():
    assert hasattr(fmp_Feature, "name")
    descriptor = None
    for klass in fmp_Feature.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_configstate_exists():
    # Check that the Enumeration exists
    assert ConfigState is not None

def test_configstate_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ConfigState]
    expected_literals = [
        "MACHINE_SELECTED",
        "USER_SELECTED",
        "USER_ELIMINATED",
        "UNDECIDED",
        "MACHINE_ELIMINATED",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ConfigState"

def test_valuetype_exists():
    # Check that the Enumeration exists
    assert ValueType is not None

def test_valuetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ValueType]
    expected_literals = [
        "STRING",
        "FEATURE",
        "FLOAT",
        "NONE",
        "INTEGER",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ValueType"


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
fmp_Project_strategy = st.builds(
    fmp_Project,
)
Node_strategy = st.builds(
    Node,
)
fmp_Clonable_strategy = st.builds(
    fmp_Clonable,
    state=
        safe_text
)
fmp_FeatureGroup_strategy = st.builds(
    fmp_FeatureGroup,
)
fmp_Constraint_strategy = st.builds(
    fmp_Constraint,
    text=
        safe_text
)
fmp_Node_strategy = st.builds(
    fmp_Node,
    id=
        safe_text,
    max=
        st.integers(),
    min=
        st.integers()
)
fmp_TypedValue_strategy = st.builds(
    fmp_TypedValue,
    stringValue=
        safe_text,
    integerValue=
        safe_text,
    floatValue=
        safe_text
)
Clonable_strategy = st.builds(
    Clonable,
)
fmp_Reference_strategy = st.builds(
    fmp_Reference,
)
fmp_Feature_strategy = st.builds(
    fmp_Feature,
    valueType=
        safe_text,
    name=
        safe_text
)

@given(instance=fmp_Project_strategy)
@settings(max_examples=50)
def test_fmp_project_instantiation(instance):
    assert isinstance(instance, fmp_Project)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=fmp_Clonable_strategy)
@settings(max_examples=50)
def test_fmp_clonable_instantiation(instance):
    assert isinstance(instance, fmp_Clonable)



@given(instance=fmp_Clonable_strategy)
def test_fmp_clonable_state_setter(instance):
    original = instance.state
    instance.state = original
    assert instance.state == original

@given(instance=fmp_FeatureGroup_strategy)
@settings(max_examples=50)
def test_fmp_featuregroup_instantiation(instance):
    assert isinstance(instance, fmp_FeatureGroup)

@given(instance=fmp_Constraint_strategy)
@settings(max_examples=50)
def test_fmp_constraint_instantiation(instance):
    assert isinstance(instance, fmp_Constraint)



@given(instance=fmp_Constraint_strategy)
def test_fmp_constraint_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=fmp_Node_strategy)
@settings(max_examples=50)
def test_fmp_node_instantiation(instance):
    assert isinstance(instance, fmp_Node)



@given(instance=fmp_Node_strategy)
def test_fmp_node_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=fmp_Node_strategy)
def test_fmp_node_max_setter(instance):
    original = instance.max
    instance.max = original
    assert instance.max == original



@given(instance=fmp_Node_strategy)
def test_fmp_node_min_setter(instance):
    original = instance.min
    instance.min = original
    assert instance.min == original

@given(instance=fmp_TypedValue_strategy)
@settings(max_examples=50)
def test_fmp_typedvalue_instantiation(instance):
    assert isinstance(instance, fmp_TypedValue)



@given(instance=fmp_TypedValue_strategy)
def test_fmp_typedvalue_stringValue_setter(instance):
    original = instance.stringValue
    instance.stringValue = original
    assert instance.stringValue == original



@given(instance=fmp_TypedValue_strategy)
def test_fmp_typedvalue_integerValue_setter(instance):
    original = instance.integerValue
    instance.integerValue = original
    assert instance.integerValue == original



@given(instance=fmp_TypedValue_strategy)
def test_fmp_typedvalue_floatValue_setter(instance):
    original = instance.floatValue
    instance.floatValue = original
    assert instance.floatValue == original

@given(instance=Clonable_strategy)
@settings(max_examples=50)
def test_clonable_instantiation(instance):
    assert isinstance(instance, Clonable)

@given(instance=fmp_Reference_strategy)
@settings(max_examples=50)
def test_fmp_reference_instantiation(instance):
    assert isinstance(instance, fmp_Reference)

@given(instance=fmp_Feature_strategy)
@settings(max_examples=50)
def test_fmp_feature_instantiation(instance):
    assert isinstance(instance, fmp_Feature)



@given(instance=fmp_Feature_strategy)
def test_fmp_feature_valueType_setter(instance):
    original = instance.valueType
    instance.valueType = original
    assert instance.valueType == original



@given(instance=fmp_Feature_strategy)
def test_fmp_feature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
