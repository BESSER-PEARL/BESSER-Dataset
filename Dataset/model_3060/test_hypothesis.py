import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    PrimitiveType,
    muddle::StringType,
    muddle::BooleanType,
    muddle::RealType,
    muddle::IntegerType,
    muddle::Feature,
    muddle::Slot,
    MuddleElementType,
    muddle::LinkElementType,
    Type,
    muddle::MuddleElementType,
    muddle::PrimitiveType,
    muddle::MuddleElement,
    muddle::Type,
    muddle::Muddle,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_primitivetype_is_not_abstract():
    assert not inspect.isabstract(PrimitiveType)


def test_primitivetype_constructor_exists():
    assert callable(PrimitiveType.__init__)


def test_primitivetype_constructor_args():
    sig = inspect.signature(PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_muddle::stringtype_is_not_abstract():
    assert not inspect.isabstract(muddle::StringType)


def test_muddle::stringtype_constructor_exists():
    assert callable(muddle::StringType.__init__)


def test_muddle::stringtype_constructor_args():
    sig = inspect.signature(muddle::StringType.__init__)
    params = list(sig.parameters.keys())



def test_muddle::booleantype_is_not_abstract():
    assert not inspect.isabstract(muddle::BooleanType)


def test_muddle::booleantype_constructor_exists():
    assert callable(muddle::BooleanType.__init__)


def test_muddle::booleantype_constructor_args():
    sig = inspect.signature(muddle::BooleanType.__init__)
    params = list(sig.parameters.keys())



def test_muddle::realtype_is_not_abstract():
    assert not inspect.isabstract(muddle::RealType)


def test_muddle::realtype_constructor_exists():
    assert callable(muddle::RealType.__init__)


def test_muddle::realtype_constructor_args():
    sig = inspect.signature(muddle::RealType.__init__)
    params = list(sig.parameters.keys())



def test_muddle::integertype_is_not_abstract():
    assert not inspect.isabstract(muddle::IntegerType)


def test_muddle::integertype_constructor_exists():
    assert callable(muddle::IntegerType.__init__)


def test_muddle::integertype_constructor_args():
    sig = inspect.signature(muddle::IntegerType.__init__)
    params = list(sig.parameters.keys())



def test_muddle::feature_is_not_abstract():
    assert not inspect.isabstract(muddle::Feature)


def test_muddle::feature_constructor_exists():
    assert callable(muddle::Feature.__init__)


def test_muddle::feature_constructor_args():
    sig = inspect.signature(muddle::Feature.__init__)
    params = list(sig.parameters.keys())
    assert "primary" in params, "Missing parameter 'primary'"
    assert "name" in params, "Missing parameter 'name'"
    assert "runtime" in params, "Missing parameter 'runtime'"
    assert "many" in params, "Missing parameter 'many'"

def test_muddle::feature_has_primary():
    assert hasattr(muddle::Feature, "primary")
    descriptor = None
    for klass in muddle::Feature.__mro__:
        if "primary" in klass.__dict__:
            descriptor = klass.__dict__["primary"]
            break
    assert isinstance(descriptor, property)

def test_muddle::feature_has_name():
    assert hasattr(muddle::Feature, "name")
    descriptor = None
    for klass in muddle::Feature.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_muddle::feature_has_runtime():
    assert hasattr(muddle::Feature, "runtime")
    descriptor = None
    for klass in muddle::Feature.__mro__:
        if "runtime" in klass.__dict__:
            descriptor = klass.__dict__["runtime"]
            break
    assert isinstance(descriptor, property)

def test_muddle::feature_has_many():
    assert hasattr(muddle::Feature, "many")
    descriptor = None
    for klass in muddle::Feature.__mro__:
        if "many" in klass.__dict__:
            descriptor = klass.__dict__["many"]
            break
    assert isinstance(descriptor, property)



def test_muddle::slot_is_not_abstract():
    assert not inspect.isabstract(muddle::Slot)


def test_muddle::slot_constructor_exists():
    assert callable(muddle::Slot.__init__)


def test_muddle::slot_constructor_args():
    sig = inspect.signature(muddle::Slot.__init__)
    params = list(sig.parameters.keys())
    assert "values" in params, "Missing parameter 'values'"

def test_muddle::slot_has_values():
    assert hasattr(muddle::Slot, "values")
    descriptor = None
    for klass in muddle::Slot.__mro__:
        if "values" in klass.__dict__:
            descriptor = klass.__dict__["values"]
            break
    assert isinstance(descriptor, property)



def test_muddleelementtype_is_not_abstract():
    assert not inspect.isabstract(MuddleElementType)


def test_muddleelementtype_constructor_exists():
    assert callable(MuddleElementType.__init__)


def test_muddleelementtype_constructor_args():
    sig = inspect.signature(MuddleElementType.__init__)
    params = list(sig.parameters.keys())



def test_muddle::linkelementtype_is_not_abstract():
    assert not inspect.isabstract(muddle::LinkElementType)


def test_muddle::linkelementtype_constructor_exists():
    assert callable(muddle::LinkElementType.__init__)


def test_muddle::linkelementtype_constructor_args():
    sig = inspect.signature(muddle::LinkElementType.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_muddle::muddleelementtype_is_not_abstract():
    assert not inspect.isabstract(muddle::MuddleElementType)


def test_muddle::muddleelementtype_constructor_exists():
    assert callable(muddle::MuddleElementType.__init__)


def test_muddle::muddleelementtype_constructor_args():
    sig = inspect.signature(muddle::MuddleElementType.__init__)
    params = list(sig.parameters.keys())



def test_muddle::primitivetype_is_not_abstract():
    assert not inspect.isabstract(muddle::PrimitiveType)


def test_muddle::primitivetype_constructor_exists():
    assert callable(muddle::PrimitiveType.__init__)


def test_muddle::primitivetype_constructor_args():
    sig = inspect.signature(muddle::PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_muddle::muddleelement_is_not_abstract():
    assert not inspect.isabstract(muddle::MuddleElement)


def test_muddle::muddleelement_constructor_exists():
    assert callable(muddle::MuddleElement.__init__)


def test_muddle::muddleelement_constructor_args():
    sig = inspect.signature(muddle::MuddleElement.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_muddle::muddleelement_has_id():
    assert hasattr(muddle::MuddleElement, "id")
    descriptor = None
    for klass in muddle::MuddleElement.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_muddle::type_is_not_abstract():
    assert not inspect.isabstract(muddle::Type)


def test_muddle::type_constructor_exists():
    assert callable(muddle::Type.__init__)


def test_muddle::type_constructor_args():
    sig = inspect.signature(muddle::Type.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_muddle::type_has_name():
    assert hasattr(muddle::Type, "name")
    descriptor = None
    for klass in muddle::Type.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_muddle::muddle_is_not_abstract():
    assert not inspect.isabstract(muddle::Muddle)


def test_muddle::muddle_constructor_exists():
    assert callable(muddle::Muddle.__init__)


def test_muddle::muddle_constructor_args():
    sig = inspect.signature(muddle::Muddle.__init__)
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
PrimitiveType_strategy = st.builds(
    PrimitiveType,
)
muddle::StringType_strategy = st.builds(
    muddle::StringType,
)
muddle::BooleanType_strategy = st.builds(
    muddle::BooleanType,
)
muddle::RealType_strategy = st.builds(
    muddle::RealType,
)
muddle::IntegerType_strategy = st.builds(
    muddle::IntegerType,
)
muddle::Feature_strategy = st.builds(
    muddle::Feature,
    primary=
        st.booleans(),
    name=
        safe_text,
    runtime=
        st.booleans(),
    many=
        st.booleans()
)
muddle::Slot_strategy = st.builds(
    muddle::Slot,
    values=
        safe_text
)
MuddleElementType_strategy = st.builds(
    MuddleElementType,
)
muddle::LinkElementType_strategy = st.builds(
    muddle::LinkElementType,
)
Type_strategy = st.builds(
    Type,
)
muddle::MuddleElementType_strategy = st.builds(
    muddle::MuddleElementType,
)
muddle::PrimitiveType_strategy = st.builds(
    muddle::PrimitiveType,
)
muddle::MuddleElement_strategy = st.builds(
    muddle::MuddleElement,
    id=
        safe_text
)
muddle::Type_strategy = st.builds(
    muddle::Type,
    name=
        safe_text
)
muddle::Muddle_strategy = st.builds(
    muddle::Muddle,
)

@given(instance=PrimitiveType_strategy)
@settings(max_examples=50)
def test_primitivetype_instantiation(instance):
    assert isinstance(instance, PrimitiveType)

@given(instance=muddle::StringType_strategy)
@settings(max_examples=50)
def test_muddle::stringtype_instantiation(instance):
    assert isinstance(instance, muddle::StringType)

@given(instance=muddle::BooleanType_strategy)
@settings(max_examples=50)
def test_muddle::booleantype_instantiation(instance):
    assert isinstance(instance, muddle::BooleanType)

@given(instance=muddle::RealType_strategy)
@settings(max_examples=50)
def test_muddle::realtype_instantiation(instance):
    assert isinstance(instance, muddle::RealType)

@given(instance=muddle::IntegerType_strategy)
@settings(max_examples=50)
def test_muddle::integertype_instantiation(instance):
    assert isinstance(instance, muddle::IntegerType)

@given(instance=muddle::Feature_strategy)
@settings(max_examples=50)
def test_muddle::feature_instantiation(instance):
    assert isinstance(instance, muddle::Feature)

@given(instance=muddle::Feature_strategy)
def test_muddle::feature_primary_type(instance):
    assert isinstance(instance.primary, bool)


@given(instance=muddle::Feature_strategy)
def test_muddle::feature_primary_setter(instance):
    original = instance.primary
    instance.primary = original
    assert instance.primary == original

@given(instance=muddle::Feature_strategy)
def test_muddle::feature_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=muddle::Feature_strategy)
def test_muddle::feature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=muddle::Feature_strategy)
def test_muddle::feature_runtime_type(instance):
    assert isinstance(instance.runtime, bool)


@given(instance=muddle::Feature_strategy)
def test_muddle::feature_runtime_setter(instance):
    original = instance.runtime
    instance.runtime = original
    assert instance.runtime == original

@given(instance=muddle::Feature_strategy)
def test_muddle::feature_many_type(instance):
    assert isinstance(instance.many, bool)


@given(instance=muddle::Feature_strategy)
def test_muddle::feature_many_setter(instance):
    original = instance.many
    instance.many = original
    assert instance.many == original

@given(instance=muddle::Slot_strategy)
@settings(max_examples=50)
def test_muddle::slot_instantiation(instance):
    assert isinstance(instance, muddle::Slot)

@given(instance=muddle::Slot_strategy)
def test_muddle::slot_values_type(instance):
    assert isinstance(instance.values, str)


@given(instance=muddle::Slot_strategy)
def test_muddle::slot_values_setter(instance):
    original = instance.values
    instance.values = original
    assert instance.values == original

@given(instance=MuddleElementType_strategy)
@settings(max_examples=50)
def test_muddleelementtype_instantiation(instance):
    assert isinstance(instance, MuddleElementType)

@given(instance=muddle::LinkElementType_strategy)
@settings(max_examples=50)
def test_muddle::linkelementtype_instantiation(instance):
    assert isinstance(instance, muddle::LinkElementType)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=muddle::MuddleElementType_strategy)
@settings(max_examples=50)
def test_muddle::muddleelementtype_instantiation(instance):
    assert isinstance(instance, muddle::MuddleElementType)

@given(instance=muddle::PrimitiveType_strategy)
@settings(max_examples=50)
def test_muddle::primitivetype_instantiation(instance):
    assert isinstance(instance, muddle::PrimitiveType)

@given(instance=muddle::MuddleElement_strategy)
@settings(max_examples=50)
def test_muddle::muddleelement_instantiation(instance):
    assert isinstance(instance, muddle::MuddleElement)

@given(instance=muddle::MuddleElement_strategy)
def test_muddle::muddleelement_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=muddle::MuddleElement_strategy)
def test_muddle::muddleelement_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=muddle::Type_strategy)
@settings(max_examples=50)
def test_muddle::type_instantiation(instance):
    assert isinstance(instance, muddle::Type)

@given(instance=muddle::Type_strategy)
def test_muddle::type_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=muddle::Type_strategy)
def test_muddle::type_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=muddle::Muddle_strategy)
@settings(max_examples=50)
def test_muddle::muddle_instantiation(instance):
    assert isinstance(instance, muddle::Muddle)
