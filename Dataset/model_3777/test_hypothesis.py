import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    fmp::Project,
    Node,
    fmp::Clonable,
    fmp::FeatureGroup,
    fmp::Constraint,
    fmp::Node,
    fmp::TypedValue,
    Clonable,
    fmp::Reference,
    fmp::Feature,
    ValueType,
    ConfigState,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_fmp::project_is_not_abstract():
    assert not inspect.isabstract(fmp::Project)


def test_fmp::project_constructor_exists():
    assert callable(fmp::Project.__init__)


def test_fmp::project_constructor_args():
    sig = inspect.signature(fmp::Project.__init__)
    params = list(sig.parameters.keys())



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_fmp::clonable_is_not_abstract():
    assert not inspect.isabstract(fmp::Clonable)


def test_fmp::clonable_constructor_exists():
    assert callable(fmp::Clonable.__init__)


def test_fmp::clonable_constructor_args():
    sig = inspect.signature(fmp::Clonable.__init__)
    params = list(sig.parameters.keys())
    assert "state" in params, "Missing parameter 'state'"

def test_fmp::clonable_has_state():
    assert hasattr(fmp::Clonable, "state")
    descriptor = None
    for klass in fmp::Clonable.__mro__:
        if "state" in klass.__dict__:
            descriptor = klass.__dict__["state"]
            break
    assert isinstance(descriptor, property)



def test_fmp::featuregroup_is_not_abstract():
    assert not inspect.isabstract(fmp::FeatureGroup)


def test_fmp::featuregroup_constructor_exists():
    assert callable(fmp::FeatureGroup.__init__)


def test_fmp::featuregroup_constructor_args():
    sig = inspect.signature(fmp::FeatureGroup.__init__)
    params = list(sig.parameters.keys())



def test_fmp::constraint_is_not_abstract():
    assert not inspect.isabstract(fmp::Constraint)


def test_fmp::constraint_constructor_exists():
    assert callable(fmp::Constraint.__init__)


def test_fmp::constraint_constructor_args():
    sig = inspect.signature(fmp::Constraint.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_fmp::constraint_has_text():
    assert hasattr(fmp::Constraint, "text")
    descriptor = None
    for klass in fmp::Constraint.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_fmp::node_is_not_abstract():
    assert not inspect.isabstract(fmp::Node)


def test_fmp::node_constructor_exists():
    assert callable(fmp::Node.__init__)


def test_fmp::node_constructor_args():
    sig = inspect.signature(fmp::Node.__init__)
    params = list(sig.parameters.keys())
    assert "max" in params, "Missing parameter 'max'"
    assert "min" in params, "Missing parameter 'min'"
    assert "id" in params, "Missing parameter 'id'"

def test_fmp::node_has_max():
    assert hasattr(fmp::Node, "max")
    descriptor = None
    for klass in fmp::Node.__mro__:
        if "max" in klass.__dict__:
            descriptor = klass.__dict__["max"]
            break
    assert isinstance(descriptor, property)

def test_fmp::node_has_min():
    assert hasattr(fmp::Node, "min")
    descriptor = None
    for klass in fmp::Node.__mro__:
        if "min" in klass.__dict__:
            descriptor = klass.__dict__["min"]
            break
    assert isinstance(descriptor, property)

def test_fmp::node_has_id():
    assert hasattr(fmp::Node, "id")
    descriptor = None
    for klass in fmp::Node.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_fmp::typedvalue_is_not_abstract():
    assert not inspect.isabstract(fmp::TypedValue)


def test_fmp::typedvalue_constructor_exists():
    assert callable(fmp::TypedValue.__init__)


def test_fmp::typedvalue_constructor_args():
    sig = inspect.signature(fmp::TypedValue.__init__)
    params = list(sig.parameters.keys())
    assert "floatValue" in params, "Missing parameter 'floatValue'"
    assert "stringValue" in params, "Missing parameter 'stringValue'"
    assert "integerValue" in params, "Missing parameter 'integerValue'"

def test_fmp::typedvalue_has_floatValue():
    assert hasattr(fmp::TypedValue, "floatValue")
    descriptor = None
    for klass in fmp::TypedValue.__mro__:
        if "floatValue" in klass.__dict__:
            descriptor = klass.__dict__["floatValue"]
            break
    assert isinstance(descriptor, property)

def test_fmp::typedvalue_has_stringValue():
    assert hasattr(fmp::TypedValue, "stringValue")
    descriptor = None
    for klass in fmp::TypedValue.__mro__:
        if "stringValue" in klass.__dict__:
            descriptor = klass.__dict__["stringValue"]
            break
    assert isinstance(descriptor, property)

def test_fmp::typedvalue_has_integerValue():
    assert hasattr(fmp::TypedValue, "integerValue")
    descriptor = None
    for klass in fmp::TypedValue.__mro__:
        if "integerValue" in klass.__dict__:
            descriptor = klass.__dict__["integerValue"]
            break
    assert isinstance(descriptor, property)



def test_clonable_is_not_abstract():
    assert not inspect.isabstract(Clonable)


def test_clonable_constructor_exists():
    assert callable(Clonable.__init__)


def test_clonable_constructor_args():
    sig = inspect.signature(Clonable.__init__)
    params = list(sig.parameters.keys())



def test_fmp::reference_is_not_abstract():
    assert not inspect.isabstract(fmp::Reference)


def test_fmp::reference_constructor_exists():
    assert callable(fmp::Reference.__init__)


def test_fmp::reference_constructor_args():
    sig = inspect.signature(fmp::Reference.__init__)
    params = list(sig.parameters.keys())



def test_fmp::feature_is_not_abstract():
    assert not inspect.isabstract(fmp::Feature)


def test_fmp::feature_constructor_exists():
    assert callable(fmp::Feature.__init__)


def test_fmp::feature_constructor_args():
    sig = inspect.signature(fmp::Feature.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "valueType" in params, "Missing parameter 'valueType'"

def test_fmp::feature_has_name():
    assert hasattr(fmp::Feature, "name")
    descriptor = None
    for klass in fmp::Feature.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fmp::feature_has_valueType():
    assert hasattr(fmp::Feature, "valueType")
    descriptor = None
    for klass in fmp::Feature.__mro__:
        if "valueType" in klass.__dict__:
            descriptor = klass.__dict__["valueType"]
            break
    assert isinstance(descriptor, property)

def test_valuetype_exists():
    # Check that the Enumeration exists
    assert ValueType is not None

def test_valuetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ValueType]
    expected_literals = [
        "FEATURE",
        "STRING",
        "FLOAT",
        "NONE",
        "INTEGER",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ValueType"

def test_configstate_exists():
    # Check that the Enumeration exists
    assert ConfigState is not None

def test_configstate_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ConfigState]
    expected_literals = [
        "MACHINE_ELIMINATED",
        "MACHINE_SELECTED",
        "USER_ELIMINATED",
        "UNDECIDED",
        "USER_SELECTED",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ConfigState"


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
fmp::Project_strategy = st.builds(
    fmp::Project,
)
Node_strategy = st.builds(
    Node,
)
fmp::Clonable_strategy = st.builds(
    fmp::Clonable,
    state=
        safe_text
)
fmp::FeatureGroup_strategy = st.builds(
    fmp::FeatureGroup,
)
fmp::Constraint_strategy = st.builds(
    fmp::Constraint,
    text=
        safe_text
)
fmp::Node_strategy = st.builds(
    fmp::Node,
    max=
        st.integers(),
    min=
        st.integers(),
    id=
        safe_text
)
fmp::TypedValue_strategy = st.builds(
    fmp::TypedValue,
    floatValue=
        safe_text,
    stringValue=
        safe_text,
    integerValue=
        safe_text
)
Clonable_strategy = st.builds(
    Clonable,
)
fmp::Reference_strategy = st.builds(
    fmp::Reference,
)
fmp::Feature_strategy = st.builds(
    fmp::Feature,
    name=
        safe_text,
    valueType=
        safe_text
)

@given(instance=fmp::Project_strategy)
@settings(max_examples=50)
def test_fmp::project_instantiation(instance):
    assert isinstance(instance, fmp::Project)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=fmp::Clonable_strategy)
@settings(max_examples=50)
def test_fmp::clonable_instantiation(instance):
    assert isinstance(instance, fmp::Clonable)

@given(instance=fmp::Clonable_strategy)
def test_fmp::clonable_state_type(instance):
    assert isinstance(instance.state, str)


@given(instance=fmp::Clonable_strategy)
def test_fmp::clonable_state_setter(instance):
    original = instance.state
    instance.state = original
    assert instance.state == original

@given(instance=fmp::FeatureGroup_strategy)
@settings(max_examples=50)
def test_fmp::featuregroup_instantiation(instance):
    assert isinstance(instance, fmp::FeatureGroup)

@given(instance=fmp::Constraint_strategy)
@settings(max_examples=50)
def test_fmp::constraint_instantiation(instance):
    assert isinstance(instance, fmp::Constraint)

@given(instance=fmp::Constraint_strategy)
def test_fmp::constraint_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=fmp::Constraint_strategy)
def test_fmp::constraint_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=fmp::Node_strategy)
@settings(max_examples=50)
def test_fmp::node_instantiation(instance):
    assert isinstance(instance, fmp::Node)

@given(instance=fmp::Node_strategy)
def test_fmp::node_max_type(instance):
    assert isinstance(instance.max, int)


@given(instance=fmp::Node_strategy)
def test_fmp::node_max_setter(instance):
    original = instance.max
    instance.max = original
    assert instance.max == original

@given(instance=fmp::Node_strategy)
def test_fmp::node_min_type(instance):
    assert isinstance(instance.min, int)


@given(instance=fmp::Node_strategy)
def test_fmp::node_min_setter(instance):
    original = instance.min
    instance.min = original
    assert instance.min == original

@given(instance=fmp::Node_strategy)
def test_fmp::node_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=fmp::Node_strategy)
def test_fmp::node_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=fmp::TypedValue_strategy)
@settings(max_examples=50)
def test_fmp::typedvalue_instantiation(instance):
    assert isinstance(instance, fmp::TypedValue)

@given(instance=fmp::TypedValue_strategy)
def test_fmp::typedvalue_floatValue_type(instance):
    assert isinstance(instance.floatValue, str)


@given(instance=fmp::TypedValue_strategy)
def test_fmp::typedvalue_floatValue_setter(instance):
    original = instance.floatValue
    instance.floatValue = original
    assert instance.floatValue == original

@given(instance=fmp::TypedValue_strategy)
def test_fmp::typedvalue_stringValue_type(instance):
    assert isinstance(instance.stringValue, str)


@given(instance=fmp::TypedValue_strategy)
def test_fmp::typedvalue_stringValue_setter(instance):
    original = instance.stringValue
    instance.stringValue = original
    assert instance.stringValue == original

@given(instance=fmp::TypedValue_strategy)
def test_fmp::typedvalue_integerValue_type(instance):
    assert isinstance(instance.integerValue, str)


@given(instance=fmp::TypedValue_strategy)
def test_fmp::typedvalue_integerValue_setter(instance):
    original = instance.integerValue
    instance.integerValue = original
    assert instance.integerValue == original

@given(instance=Clonable_strategy)
@settings(max_examples=50)
def test_clonable_instantiation(instance):
    assert isinstance(instance, Clonable)

@given(instance=fmp::Reference_strategy)
@settings(max_examples=50)
def test_fmp::reference_instantiation(instance):
    assert isinstance(instance, fmp::Reference)

@given(instance=fmp::Feature_strategy)
@settings(max_examples=50)
def test_fmp::feature_instantiation(instance):
    assert isinstance(instance, fmp::Feature)

@given(instance=fmp::Feature_strategy)
def test_fmp::feature_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fmp::Feature_strategy)
def test_fmp::feature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fmp::Feature_strategy)
def test_fmp::feature_valueType_type(instance):
    assert isinstance(instance.valueType, str)


@given(instance=fmp::Feature_strategy)
def test_fmp::feature_valueType_setter(instance):
    original = instance.valueType
    instance.valueType = original
    assert instance.valueType == original
