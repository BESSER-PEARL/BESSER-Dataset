import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ulmDsl2::EntityFeatureType,
    ulmDsl2::AttributeFeatureType,
    ulmDsl2::FeatureType,
    ulmDsl2::Feature,
    ulmDsl2::AttributeDecimalType,
    ulmDsl2::LookupStringValue,
    ulmDsl2::LookupString,
    ulmDsl2::LookupIntValue,
    ulmDsl2::LookupInt,
    ulmDsl2::Context,
    ulmDsl2::Model,
    ulmDsl2::AttributeStringType,
    ulmDsl2::AttributeType,
    ulmDsl2::EObject,
    ulmDsl2::Entity,
    ulmDsl2::Lookup,
    ulmDsl2::Attribute,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_ulmdsl2::entityfeaturetype_is_not_abstract():
    assert not inspect.isabstract(ulmDsl2::EntityFeatureType)


def test_ulmdsl2::entityfeaturetype_constructor_exists():
    assert callable(ulmDsl2::EntityFeatureType.__init__)


def test_ulmdsl2::entityfeaturetype_constructor_args():
    sig = inspect.signature(ulmDsl2::EntityFeatureType.__init__)
    params = list(sig.parameters.keys())
    assert "array" in params, "Missing parameter 'array'"
    assert "length" in params, "Missing parameter 'length'"

def test_ulmdsl2::entityfeaturetype_has_array():
    assert hasattr(ulmDsl2::EntityFeatureType, "array")
    descriptor = None
    for klass in ulmDsl2::EntityFeatureType.__mro__:
        if "array" in klass.__dict__:
            descriptor = klass.__dict__["array"]
            break
    assert isinstance(descriptor, property)

def test_ulmdsl2::entityfeaturetype_has_length():
    assert hasattr(ulmDsl2::EntityFeatureType, "length")
    descriptor = None
    for klass in ulmDsl2::EntityFeatureType.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)



def test_ulmdsl2::attributefeaturetype_is_not_abstract():
    assert not inspect.isabstract(ulmDsl2::AttributeFeatureType)


def test_ulmdsl2::attributefeaturetype_constructor_exists():
    assert callable(ulmDsl2::AttributeFeatureType.__init__)


def test_ulmdsl2::attributefeaturetype_constructor_args():
    sig = inspect.signature(ulmDsl2::AttributeFeatureType.__init__)
    params = list(sig.parameters.keys())



def test_ulmdsl2::featuretype_is_not_abstract():
    assert not inspect.isabstract(ulmDsl2::FeatureType)


def test_ulmdsl2::featuretype_constructor_exists():
    assert callable(ulmDsl2::FeatureType.__init__)


def test_ulmdsl2::featuretype_constructor_args():
    sig = inspect.signature(ulmDsl2::FeatureType.__init__)
    params = list(sig.parameters.keys())



def test_ulmdsl2::feature_is_not_abstract():
    assert not inspect.isabstract(ulmDsl2::Feature)


def test_ulmdsl2::feature_constructor_exists():
    assert callable(ulmDsl2::Feature.__init__)


def test_ulmdsl2::feature_constructor_args():
    sig = inspect.signature(ulmDsl2::Feature.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"
    assert "mandatory" in params, "Missing parameter 'mandatory'"
    assert "name" in params, "Missing parameter 'name'"

def test_ulmdsl2::feature_has_identifier():
    assert hasattr(ulmDsl2::Feature, "identifier")
    descriptor = None
    for klass in ulmDsl2::Feature.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)

def test_ulmdsl2::feature_has_mandatory():
    assert hasattr(ulmDsl2::Feature, "mandatory")
    descriptor = None
    for klass in ulmDsl2::Feature.__mro__:
        if "mandatory" in klass.__dict__:
            descriptor = klass.__dict__["mandatory"]
            break
    assert isinstance(descriptor, property)

def test_ulmdsl2::feature_has_name():
    assert hasattr(ulmDsl2::Feature, "name")
    descriptor = None
    for klass in ulmDsl2::Feature.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ulmdsl2::attributedecimaltype_is_not_abstract():
    assert not inspect.isabstract(ulmDsl2::AttributeDecimalType)


def test_ulmdsl2::attributedecimaltype_constructor_exists():
    assert callable(ulmDsl2::AttributeDecimalType.__init__)


def test_ulmdsl2::attributedecimaltype_constructor_args():
    sig = inspect.signature(ulmDsl2::AttributeDecimalType.__init__)
    params = list(sig.parameters.keys())
    assert "array" in params, "Missing parameter 'array'"
    assert "name" in params, "Missing parameter 'name'"
    assert "scale" in params, "Missing parameter 'scale'"
    assert "precision" in params, "Missing parameter 'precision'"

def test_ulmdsl2::attributedecimaltype_has_array():
    assert hasattr(ulmDsl2::AttributeDecimalType, "array")
    descriptor = None
    for klass in ulmDsl2::AttributeDecimalType.__mro__:
        if "array" in klass.__dict__:
            descriptor = klass.__dict__["array"]
            break
    assert isinstance(descriptor, property)

def test_ulmdsl2::attributedecimaltype_has_name():
    assert hasattr(ulmDsl2::AttributeDecimalType, "name")
    descriptor = None
    for klass in ulmDsl2::AttributeDecimalType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ulmdsl2::attributedecimaltype_has_scale():
    assert hasattr(ulmDsl2::AttributeDecimalType, "scale")
    descriptor = None
    for klass in ulmDsl2::AttributeDecimalType.__mro__:
        if "scale" in klass.__dict__:
            descriptor = klass.__dict__["scale"]
            break
    assert isinstance(descriptor, property)

def test_ulmdsl2::attributedecimaltype_has_precision():
    assert hasattr(ulmDsl2::AttributeDecimalType, "precision")
    descriptor = None
    for klass in ulmDsl2::AttributeDecimalType.__mro__:
        if "precision" in klass.__dict__:
            descriptor = klass.__dict__["precision"]
            break
    assert isinstance(descriptor, property)



def test_ulmdsl2::lookupstringvalue_is_not_abstract():
    assert not inspect.isabstract(ulmDsl2::LookupStringValue)


def test_ulmdsl2::lookupstringvalue_constructor_exists():
    assert callable(ulmDsl2::LookupStringValue.__init__)


def test_ulmdsl2::lookupstringvalue_constructor_args():
    sig = inspect.signature(ulmDsl2::LookupStringValue.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "value" in params, "Missing parameter 'value'"

def test_ulmdsl2::lookupstringvalue_has_description():
    assert hasattr(ulmDsl2::LookupStringValue, "description")
    descriptor = None
    for klass in ulmDsl2::LookupStringValue.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_ulmdsl2::lookupstringvalue_has_value():
    assert hasattr(ulmDsl2::LookupStringValue, "value")
    descriptor = None
    for klass in ulmDsl2::LookupStringValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_ulmdsl2::lookupstring_is_not_abstract():
    assert not inspect.isabstract(ulmDsl2::LookupString)


def test_ulmdsl2::lookupstring_constructor_exists():
    assert callable(ulmDsl2::LookupString.__init__)


def test_ulmdsl2::lookupstring_constructor_args():
    sig = inspect.signature(ulmDsl2::LookupString.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"

def test_ulmdsl2::lookupstring_has_description():
    assert hasattr(ulmDsl2::LookupString, "description")
    descriptor = None
    for klass in ulmDsl2::LookupString.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_ulmdsl2::lookupintvalue_is_not_abstract():
    assert not inspect.isabstract(ulmDsl2::LookupIntValue)


def test_ulmdsl2::lookupintvalue_constructor_exists():
    assert callable(ulmDsl2::LookupIntValue.__init__)


def test_ulmdsl2::lookupintvalue_constructor_args():
    sig = inspect.signature(ulmDsl2::LookupIntValue.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "value" in params, "Missing parameter 'value'"

def test_ulmdsl2::lookupintvalue_has_description():
    assert hasattr(ulmDsl2::LookupIntValue, "description")
    descriptor = None
    for klass in ulmDsl2::LookupIntValue.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_ulmdsl2::lookupintvalue_has_value():
    assert hasattr(ulmDsl2::LookupIntValue, "value")
    descriptor = None
    for klass in ulmDsl2::LookupIntValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_ulmdsl2::lookupint_is_not_abstract():
    assert not inspect.isabstract(ulmDsl2::LookupInt)


def test_ulmdsl2::lookupint_constructor_exists():
    assert callable(ulmDsl2::LookupInt.__init__)


def test_ulmdsl2::lookupint_constructor_args():
    sig = inspect.signature(ulmDsl2::LookupInt.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"

def test_ulmdsl2::lookupint_has_description():
    assert hasattr(ulmDsl2::LookupInt, "description")
    descriptor = None
    for klass in ulmDsl2::LookupInt.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_ulmdsl2::context_is_not_abstract():
    assert not inspect.isabstract(ulmDsl2::Context)


def test_ulmdsl2::context_constructor_exists():
    assert callable(ulmDsl2::Context.__init__)


def test_ulmdsl2::context_constructor_args():
    sig = inspect.signature(ulmDsl2::Context.__init__)
    params = list(sig.parameters.keys())
    assert "version" in params, "Missing parameter 'version'"
    assert "name" in params, "Missing parameter 'name'"

def test_ulmdsl2::context_has_version():
    assert hasattr(ulmDsl2::Context, "version")
    descriptor = None
    for klass in ulmDsl2::Context.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_ulmdsl2::context_has_name():
    assert hasattr(ulmDsl2::Context, "name")
    descriptor = None
    for klass in ulmDsl2::Context.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ulmdsl2::model_is_not_abstract():
    assert not inspect.isabstract(ulmDsl2::Model)


def test_ulmdsl2::model_constructor_exists():
    assert callable(ulmDsl2::Model.__init__)


def test_ulmdsl2::model_constructor_args():
    sig = inspect.signature(ulmDsl2::Model.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ulmdsl2::model_has_name():
    assert hasattr(ulmDsl2::Model, "name")
    descriptor = None
    for klass in ulmDsl2::Model.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ulmdsl2::attributestringtype_is_not_abstract():
    assert not inspect.isabstract(ulmDsl2::AttributeStringType)


def test_ulmdsl2::attributestringtype_constructor_exists():
    assert callable(ulmDsl2::AttributeStringType.__init__)


def test_ulmdsl2::attributestringtype_constructor_args():
    sig = inspect.signature(ulmDsl2::AttributeStringType.__init__)
    params = list(sig.parameters.keys())
    assert "length" in params, "Missing parameter 'length'"
    assert "name" in params, "Missing parameter 'name'"
    assert "array" in params, "Missing parameter 'array'"

def test_ulmdsl2::attributestringtype_has_length():
    assert hasattr(ulmDsl2::AttributeStringType, "length")
    descriptor = None
    for klass in ulmDsl2::AttributeStringType.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)

def test_ulmdsl2::attributestringtype_has_name():
    assert hasattr(ulmDsl2::AttributeStringType, "name")
    descriptor = None
    for klass in ulmDsl2::AttributeStringType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ulmdsl2::attributestringtype_has_array():
    assert hasattr(ulmDsl2::AttributeStringType, "array")
    descriptor = None
    for klass in ulmDsl2::AttributeStringType.__mro__:
        if "array" in klass.__dict__:
            descriptor = klass.__dict__["array"]
            break
    assert isinstance(descriptor, property)



def test_ulmdsl2::attributetype_is_not_abstract():
    assert not inspect.isabstract(ulmDsl2::AttributeType)


def test_ulmdsl2::attributetype_constructor_exists():
    assert callable(ulmDsl2::AttributeType.__init__)


def test_ulmdsl2::attributetype_constructor_args():
    sig = inspect.signature(ulmDsl2::AttributeType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ulmdsl2::attributetype_has_name():
    assert hasattr(ulmDsl2::AttributeType, "name")
    descriptor = None
    for klass in ulmDsl2::AttributeType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ulmdsl2::eobject_is_not_abstract():
    assert not inspect.isabstract(ulmDsl2::EObject)


def test_ulmdsl2::eobject_constructor_exists():
    assert callable(ulmDsl2::EObject.__init__)


def test_ulmdsl2::eobject_constructor_args():
    sig = inspect.signature(ulmDsl2::EObject.__init__)
    params = list(sig.parameters.keys())



def test_ulmdsl2::entity_is_not_abstract():
    assert not inspect.isabstract(ulmDsl2::Entity)


def test_ulmdsl2::entity_constructor_exists():
    assert callable(ulmDsl2::Entity.__init__)


def test_ulmdsl2::entity_constructor_args():
    sig = inspect.signature(ulmDsl2::Entity.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"
    assert "desc" in params, "Missing parameter 'desc'"

def test_ulmdsl2::entity_has_type():
    assert hasattr(ulmDsl2::Entity, "type")
    descriptor = None
    for klass in ulmDsl2::Entity.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_ulmdsl2::entity_has_name():
    assert hasattr(ulmDsl2::Entity, "name")
    descriptor = None
    for klass in ulmDsl2::Entity.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ulmdsl2::entity_has_desc():
    assert hasattr(ulmDsl2::Entity, "desc")
    descriptor = None
    for klass in ulmDsl2::Entity.__mro__:
        if "desc" in klass.__dict__:
            descriptor = klass.__dict__["desc"]
            break
    assert isinstance(descriptor, property)



def test_ulmdsl2::lookup_is_not_abstract():
    assert not inspect.isabstract(ulmDsl2::Lookup)


def test_ulmdsl2::lookup_constructor_exists():
    assert callable(ulmDsl2::Lookup.__init__)


def test_ulmdsl2::lookup_constructor_args():
    sig = inspect.signature(ulmDsl2::Lookup.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ulmdsl2::lookup_has_name():
    assert hasattr(ulmDsl2::Lookup, "name")
    descriptor = None
    for klass in ulmDsl2::Lookup.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ulmdsl2::attribute_is_not_abstract():
    assert not inspect.isabstract(ulmDsl2::Attribute)


def test_ulmdsl2::attribute_constructor_exists():
    assert callable(ulmDsl2::Attribute.__init__)


def test_ulmdsl2::attribute_constructor_args():
    sig = inspect.signature(ulmDsl2::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "desc" in params, "Missing parameter 'desc'"
    assert "name" in params, "Missing parameter 'name'"

def test_ulmdsl2::attribute_has_desc():
    assert hasattr(ulmDsl2::Attribute, "desc")
    descriptor = None
    for klass in ulmDsl2::Attribute.__mro__:
        if "desc" in klass.__dict__:
            descriptor = klass.__dict__["desc"]
            break
    assert isinstance(descriptor, property)

def test_ulmdsl2::attribute_has_name():
    assert hasattr(ulmDsl2::Attribute, "name")
    descriptor = None
    for klass in ulmDsl2::Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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
ulmDsl2::EntityFeatureType_strategy = st.builds(
    ulmDsl2::EntityFeatureType,
    array=
        st.booleans(),
    length=
        st.integers()
)
ulmDsl2::AttributeFeatureType_strategy = st.builds(
    ulmDsl2::AttributeFeatureType,
)
ulmDsl2::FeatureType_strategy = st.builds(
    ulmDsl2::FeatureType,
)
ulmDsl2::Feature_strategy = st.builds(
    ulmDsl2::Feature,
    identifier=
        st.booleans(),
    mandatory=
        st.booleans(),
    name=
        safe_text
)
ulmDsl2::AttributeDecimalType_strategy = st.builds(
    ulmDsl2::AttributeDecimalType,
    array=
        st.booleans(),
    name=
        safe_text,
    scale=
        st.integers(),
    precision=
        st.integers()
)
ulmDsl2::LookupStringValue_strategy = st.builds(
    ulmDsl2::LookupStringValue,
    description=
        safe_text,
    value=
        safe_text
)
ulmDsl2::LookupString_strategy = st.builds(
    ulmDsl2::LookupString,
    description=
        safe_text
)
ulmDsl2::LookupIntValue_strategy = st.builds(
    ulmDsl2::LookupIntValue,
    description=
        safe_text,
    value=
        st.integers()
)
ulmDsl2::LookupInt_strategy = st.builds(
    ulmDsl2::LookupInt,
    description=
        safe_text
)
ulmDsl2::Context_strategy = st.builds(
    ulmDsl2::Context,
    version=
        safe_text,
    name=
        safe_text
)
ulmDsl2::Model_strategy = st.builds(
    ulmDsl2::Model,
    name=
        safe_text
)
ulmDsl2::AttributeStringType_strategy = st.builds(
    ulmDsl2::AttributeStringType,
    length=
        st.integers(),
    name=
        safe_text,
    array=
        st.booleans()
)
ulmDsl2::AttributeType_strategy = st.builds(
    ulmDsl2::AttributeType,
    name=
        safe_text
)
ulmDsl2::EObject_strategy = st.builds(
    ulmDsl2::EObject,
)
ulmDsl2::Entity_strategy = st.builds(
    ulmDsl2::Entity,
    type=
        safe_text,
    name=
        safe_text,
    desc=
        safe_text
)
ulmDsl2::Lookup_strategy = st.builds(
    ulmDsl2::Lookup,
    name=
        safe_text
)
ulmDsl2::Attribute_strategy = st.builds(
    ulmDsl2::Attribute,
    desc=
        safe_text,
    name=
        safe_text
)

@given(instance=ulmDsl2::EntityFeatureType_strategy)
@settings(max_examples=50)
def test_ulmdsl2::entityfeaturetype_instantiation(instance):
    assert isinstance(instance, ulmDsl2::EntityFeatureType)

@given(instance=ulmDsl2::EntityFeatureType_strategy)
def test_ulmdsl2::entityfeaturetype_array_type(instance):
    assert isinstance(instance.array, bool)


@given(instance=ulmDsl2::EntityFeatureType_strategy)
def test_ulmdsl2::entityfeaturetype_array_setter(instance):
    original = instance.array
    instance.array = original
    assert instance.array == original

@given(instance=ulmDsl2::EntityFeatureType_strategy)
def test_ulmdsl2::entityfeaturetype_length_type(instance):
    assert isinstance(instance.length, int)


@given(instance=ulmDsl2::EntityFeatureType_strategy)
def test_ulmdsl2::entityfeaturetype_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original

@given(instance=ulmDsl2::AttributeFeatureType_strategy)
@settings(max_examples=50)
def test_ulmdsl2::attributefeaturetype_instantiation(instance):
    assert isinstance(instance, ulmDsl2::AttributeFeatureType)

@given(instance=ulmDsl2::FeatureType_strategy)
@settings(max_examples=50)
def test_ulmdsl2::featuretype_instantiation(instance):
    assert isinstance(instance, ulmDsl2::FeatureType)

@given(instance=ulmDsl2::Feature_strategy)
@settings(max_examples=50)
def test_ulmdsl2::feature_instantiation(instance):
    assert isinstance(instance, ulmDsl2::Feature)

@given(instance=ulmDsl2::Feature_strategy)
def test_ulmdsl2::feature_identifier_type(instance):
    assert isinstance(instance.identifier, bool)


@given(instance=ulmDsl2::Feature_strategy)
def test_ulmdsl2::feature_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=ulmDsl2::Feature_strategy)
def test_ulmdsl2::feature_mandatory_type(instance):
    assert isinstance(instance.mandatory, bool)


@given(instance=ulmDsl2::Feature_strategy)
def test_ulmdsl2::feature_mandatory_setter(instance):
    original = instance.mandatory
    instance.mandatory = original
    assert instance.mandatory == original

@given(instance=ulmDsl2::Feature_strategy)
def test_ulmdsl2::feature_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ulmDsl2::Feature_strategy)
def test_ulmdsl2::feature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ulmDsl2::AttributeDecimalType_strategy)
@settings(max_examples=50)
def test_ulmdsl2::attributedecimaltype_instantiation(instance):
    assert isinstance(instance, ulmDsl2::AttributeDecimalType)

@given(instance=ulmDsl2::AttributeDecimalType_strategy)
def test_ulmdsl2::attributedecimaltype_array_type(instance):
    assert isinstance(instance.array, bool)


@given(instance=ulmDsl2::AttributeDecimalType_strategy)
def test_ulmdsl2::attributedecimaltype_array_setter(instance):
    original = instance.array
    instance.array = original
    assert instance.array == original

@given(instance=ulmDsl2::AttributeDecimalType_strategy)
def test_ulmdsl2::attributedecimaltype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ulmDsl2::AttributeDecimalType_strategy)
def test_ulmdsl2::attributedecimaltype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ulmDsl2::AttributeDecimalType_strategy)
def test_ulmdsl2::attributedecimaltype_scale_type(instance):
    assert isinstance(instance.scale, int)


@given(instance=ulmDsl2::AttributeDecimalType_strategy)
def test_ulmdsl2::attributedecimaltype_scale_setter(instance):
    original = instance.scale
    instance.scale = original
    assert instance.scale == original

@given(instance=ulmDsl2::AttributeDecimalType_strategy)
def test_ulmdsl2::attributedecimaltype_precision_type(instance):
    assert isinstance(instance.precision, int)


@given(instance=ulmDsl2::AttributeDecimalType_strategy)
def test_ulmdsl2::attributedecimaltype_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original

@given(instance=ulmDsl2::LookupStringValue_strategy)
@settings(max_examples=50)
def test_ulmdsl2::lookupstringvalue_instantiation(instance):
    assert isinstance(instance, ulmDsl2::LookupStringValue)

@given(instance=ulmDsl2::LookupStringValue_strategy)
def test_ulmdsl2::lookupstringvalue_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=ulmDsl2::LookupStringValue_strategy)
def test_ulmdsl2::lookupstringvalue_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=ulmDsl2::LookupStringValue_strategy)
def test_ulmdsl2::lookupstringvalue_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=ulmDsl2::LookupStringValue_strategy)
def test_ulmdsl2::lookupstringvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ulmDsl2::LookupString_strategy)
@settings(max_examples=50)
def test_ulmdsl2::lookupstring_instantiation(instance):
    assert isinstance(instance, ulmDsl2::LookupString)

@given(instance=ulmDsl2::LookupString_strategy)
def test_ulmdsl2::lookupstring_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=ulmDsl2::LookupString_strategy)
def test_ulmdsl2::lookupstring_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=ulmDsl2::LookupIntValue_strategy)
@settings(max_examples=50)
def test_ulmdsl2::lookupintvalue_instantiation(instance):
    assert isinstance(instance, ulmDsl2::LookupIntValue)

@given(instance=ulmDsl2::LookupIntValue_strategy)
def test_ulmdsl2::lookupintvalue_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=ulmDsl2::LookupIntValue_strategy)
def test_ulmdsl2::lookupintvalue_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=ulmDsl2::LookupIntValue_strategy)
def test_ulmdsl2::lookupintvalue_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=ulmDsl2::LookupIntValue_strategy)
def test_ulmdsl2::lookupintvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ulmDsl2::LookupInt_strategy)
@settings(max_examples=50)
def test_ulmdsl2::lookupint_instantiation(instance):
    assert isinstance(instance, ulmDsl2::LookupInt)

@given(instance=ulmDsl2::LookupInt_strategy)
def test_ulmdsl2::lookupint_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=ulmDsl2::LookupInt_strategy)
def test_ulmdsl2::lookupint_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=ulmDsl2::Context_strategy)
@settings(max_examples=50)
def test_ulmdsl2::context_instantiation(instance):
    assert isinstance(instance, ulmDsl2::Context)

@given(instance=ulmDsl2::Context_strategy)
def test_ulmdsl2::context_version_type(instance):
    assert isinstance(instance.version, str)


@given(instance=ulmDsl2::Context_strategy)
def test_ulmdsl2::context_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=ulmDsl2::Context_strategy)
def test_ulmdsl2::context_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ulmDsl2::Context_strategy)
def test_ulmdsl2::context_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ulmDsl2::Model_strategy)
@settings(max_examples=50)
def test_ulmdsl2::model_instantiation(instance):
    assert isinstance(instance, ulmDsl2::Model)

@given(instance=ulmDsl2::Model_strategy)
def test_ulmdsl2::model_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ulmDsl2::Model_strategy)
def test_ulmdsl2::model_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ulmDsl2::AttributeStringType_strategy)
@settings(max_examples=50)
def test_ulmdsl2::attributestringtype_instantiation(instance):
    assert isinstance(instance, ulmDsl2::AttributeStringType)

@given(instance=ulmDsl2::AttributeStringType_strategy)
def test_ulmdsl2::attributestringtype_length_type(instance):
    assert isinstance(instance.length, int)


@given(instance=ulmDsl2::AttributeStringType_strategy)
def test_ulmdsl2::attributestringtype_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original

@given(instance=ulmDsl2::AttributeStringType_strategy)
def test_ulmdsl2::attributestringtype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ulmDsl2::AttributeStringType_strategy)
def test_ulmdsl2::attributestringtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ulmDsl2::AttributeStringType_strategy)
def test_ulmdsl2::attributestringtype_array_type(instance):
    assert isinstance(instance.array, bool)


@given(instance=ulmDsl2::AttributeStringType_strategy)
def test_ulmdsl2::attributestringtype_array_setter(instance):
    original = instance.array
    instance.array = original
    assert instance.array == original

@given(instance=ulmDsl2::AttributeType_strategy)
@settings(max_examples=50)
def test_ulmdsl2::attributetype_instantiation(instance):
    assert isinstance(instance, ulmDsl2::AttributeType)

@given(instance=ulmDsl2::AttributeType_strategy)
def test_ulmdsl2::attributetype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ulmDsl2::AttributeType_strategy)
def test_ulmdsl2::attributetype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ulmDsl2::EObject_strategy)
@settings(max_examples=50)
def test_ulmdsl2::eobject_instantiation(instance):
    assert isinstance(instance, ulmDsl2::EObject)

@given(instance=ulmDsl2::Entity_strategy)
@settings(max_examples=50)
def test_ulmdsl2::entity_instantiation(instance):
    assert isinstance(instance, ulmDsl2::Entity)

@given(instance=ulmDsl2::Entity_strategy)
def test_ulmdsl2::entity_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=ulmDsl2::Entity_strategy)
def test_ulmdsl2::entity_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=ulmDsl2::Entity_strategy)
def test_ulmdsl2::entity_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ulmDsl2::Entity_strategy)
def test_ulmdsl2::entity_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ulmDsl2::Entity_strategy)
def test_ulmdsl2::entity_desc_type(instance):
    assert isinstance(instance.desc, str)


@given(instance=ulmDsl2::Entity_strategy)
def test_ulmdsl2::entity_desc_setter(instance):
    original = instance.desc
    instance.desc = original
    assert instance.desc == original

@given(instance=ulmDsl2::Lookup_strategy)
@settings(max_examples=50)
def test_ulmdsl2::lookup_instantiation(instance):
    assert isinstance(instance, ulmDsl2::Lookup)

@given(instance=ulmDsl2::Lookup_strategy)
def test_ulmdsl2::lookup_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ulmDsl2::Lookup_strategy)
def test_ulmdsl2::lookup_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ulmDsl2::Attribute_strategy)
@settings(max_examples=50)
def test_ulmdsl2::attribute_instantiation(instance):
    assert isinstance(instance, ulmDsl2::Attribute)

@given(instance=ulmDsl2::Attribute_strategy)
def test_ulmdsl2::attribute_desc_type(instance):
    assert isinstance(instance.desc, str)


@given(instance=ulmDsl2::Attribute_strategy)
def test_ulmdsl2::attribute_desc_setter(instance):
    original = instance.desc
    instance.desc = original
    assert instance.desc == original

@given(instance=ulmDsl2::Attribute_strategy)
def test_ulmdsl2::attribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ulmDsl2::Attribute_strategy)
def test_ulmdsl2::attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
