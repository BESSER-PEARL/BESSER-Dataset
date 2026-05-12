import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ulmDsl2_EntityFeatureType,
    ulmDsl2_AttributeFeatureType,
    ulmDsl2_FeatureType,
    ulmDsl2_Feature,
    ulmDsl2_AttributeDecimalType,
    ulmDsl2_LookupStringValue,
    ulmDsl2_LookupString,
    ulmDsl2_LookupIntValue,
    ulmDsl2_LookupInt,
    ulmDsl2_Context,
    ulmDsl2_Model,
    ulmDsl2_AttributeStringType,
    ulmDsl2_AttributeType,
    ulmDsl2_EObject,
    ulmDsl2_Entity,
    ulmDsl2_Lookup,
    ulmDsl2_Attribute,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_ulmdsl2_entityfeaturetype_is_not_abstract():
    assert not inspect.isabstract(ulmDsl2_EntityFeatureType)


def test_ulmdsl2_entityfeaturetype_constructor_exists():
    assert callable(ulmDsl2_EntityFeatureType.__init__)


def test_ulmdsl2_entityfeaturetype_constructor_args():
    sig = inspect.signature(ulmDsl2_EntityFeatureType.__init__)
    params = list(sig.parameters.keys())
    assert "length" in params, "Missing parameter 'length'"
    assert "array" in params, "Missing parameter 'array'"

def test_ulmdsl2_entityfeaturetype_has_length():
    assert hasattr(ulmDsl2_EntityFeatureType, "length")
    descriptor = None
    for klass in ulmDsl2_EntityFeatureType.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)

def test_ulmdsl2_entityfeaturetype_has_array():
    assert hasattr(ulmDsl2_EntityFeatureType, "array")
    descriptor = None
    for klass in ulmDsl2_EntityFeatureType.__mro__:
        if "array" in klass.__dict__:
            descriptor = klass.__dict__["array"]
            break
    assert isinstance(descriptor, property)



def test_ulmdsl2_attributefeaturetype_is_not_abstract():
    assert not inspect.isabstract(ulmDsl2_AttributeFeatureType)


def test_ulmdsl2_attributefeaturetype_constructor_exists():
    assert callable(ulmDsl2_AttributeFeatureType.__init__)


def test_ulmdsl2_attributefeaturetype_constructor_args():
    sig = inspect.signature(ulmDsl2_AttributeFeatureType.__init__)
    params = list(sig.parameters.keys())



def test_ulmdsl2_featuretype_is_not_abstract():
    assert not inspect.isabstract(ulmDsl2_FeatureType)


def test_ulmdsl2_featuretype_constructor_exists():
    assert callable(ulmDsl2_FeatureType.__init__)


def test_ulmdsl2_featuretype_constructor_args():
    sig = inspect.signature(ulmDsl2_FeatureType.__init__)
    params = list(sig.parameters.keys())



def test_ulmdsl2_feature_is_not_abstract():
    assert not inspect.isabstract(ulmDsl2_Feature)


def test_ulmdsl2_feature_constructor_exists():
    assert callable(ulmDsl2_Feature.__init__)


def test_ulmdsl2_feature_constructor_args():
    sig = inspect.signature(ulmDsl2_Feature.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"
    assert "name" in params, "Missing parameter 'name'"
    assert "mandatory" in params, "Missing parameter 'mandatory'"

def test_ulmdsl2_feature_has_identifier():
    assert hasattr(ulmDsl2_Feature, "identifier")
    descriptor = None
    for klass in ulmDsl2_Feature.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)

def test_ulmdsl2_feature_has_name():
    assert hasattr(ulmDsl2_Feature, "name")
    descriptor = None
    for klass in ulmDsl2_Feature.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ulmdsl2_feature_has_mandatory():
    assert hasattr(ulmDsl2_Feature, "mandatory")
    descriptor = None
    for klass in ulmDsl2_Feature.__mro__:
        if "mandatory" in klass.__dict__:
            descriptor = klass.__dict__["mandatory"]
            break
    assert isinstance(descriptor, property)



def test_ulmdsl2_attributedecimaltype_is_not_abstract():
    assert not inspect.isabstract(ulmDsl2_AttributeDecimalType)


def test_ulmdsl2_attributedecimaltype_constructor_exists():
    assert callable(ulmDsl2_AttributeDecimalType.__init__)


def test_ulmdsl2_attributedecimaltype_constructor_args():
    sig = inspect.signature(ulmDsl2_AttributeDecimalType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "array" in params, "Missing parameter 'array'"
    assert "scale" in params, "Missing parameter 'scale'"
    assert "precision" in params, "Missing parameter 'precision'"

def test_ulmdsl2_attributedecimaltype_has_name():
    assert hasattr(ulmDsl2_AttributeDecimalType, "name")
    descriptor = None
    for klass in ulmDsl2_AttributeDecimalType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ulmdsl2_attributedecimaltype_has_array():
    assert hasattr(ulmDsl2_AttributeDecimalType, "array")
    descriptor = None
    for klass in ulmDsl2_AttributeDecimalType.__mro__:
        if "array" in klass.__dict__:
            descriptor = klass.__dict__["array"]
            break
    assert isinstance(descriptor, property)

def test_ulmdsl2_attributedecimaltype_has_scale():
    assert hasattr(ulmDsl2_AttributeDecimalType, "scale")
    descriptor = None
    for klass in ulmDsl2_AttributeDecimalType.__mro__:
        if "scale" in klass.__dict__:
            descriptor = klass.__dict__["scale"]
            break
    assert isinstance(descriptor, property)

def test_ulmdsl2_attributedecimaltype_has_precision():
    assert hasattr(ulmDsl2_AttributeDecimalType, "precision")
    descriptor = None
    for klass in ulmDsl2_AttributeDecimalType.__mro__:
        if "precision" in klass.__dict__:
            descriptor = klass.__dict__["precision"]
            break
    assert isinstance(descriptor, property)



def test_ulmdsl2_lookupstringvalue_is_not_abstract():
    assert not inspect.isabstract(ulmDsl2_LookupStringValue)


def test_ulmdsl2_lookupstringvalue_constructor_exists():
    assert callable(ulmDsl2_LookupStringValue.__init__)


def test_ulmdsl2_lookupstringvalue_constructor_args():
    sig = inspect.signature(ulmDsl2_LookupStringValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "description" in params, "Missing parameter 'description'"

def test_ulmdsl2_lookupstringvalue_has_value():
    assert hasattr(ulmDsl2_LookupStringValue, "value")
    descriptor = None
    for klass in ulmDsl2_LookupStringValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_ulmdsl2_lookupstringvalue_has_description():
    assert hasattr(ulmDsl2_LookupStringValue, "description")
    descriptor = None
    for klass in ulmDsl2_LookupStringValue.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_ulmdsl2_lookupstring_is_not_abstract():
    assert not inspect.isabstract(ulmDsl2_LookupString)


def test_ulmdsl2_lookupstring_constructor_exists():
    assert callable(ulmDsl2_LookupString.__init__)


def test_ulmdsl2_lookupstring_constructor_args():
    sig = inspect.signature(ulmDsl2_LookupString.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"

def test_ulmdsl2_lookupstring_has_description():
    assert hasattr(ulmDsl2_LookupString, "description")
    descriptor = None
    for klass in ulmDsl2_LookupString.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_ulmdsl2_lookupintvalue_is_not_abstract():
    assert not inspect.isabstract(ulmDsl2_LookupIntValue)


def test_ulmdsl2_lookupintvalue_constructor_exists():
    assert callable(ulmDsl2_LookupIntValue.__init__)


def test_ulmdsl2_lookupintvalue_constructor_args():
    sig = inspect.signature(ulmDsl2_LookupIntValue.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "value" in params, "Missing parameter 'value'"

def test_ulmdsl2_lookupintvalue_has_description():
    assert hasattr(ulmDsl2_LookupIntValue, "description")
    descriptor = None
    for klass in ulmDsl2_LookupIntValue.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_ulmdsl2_lookupintvalue_has_value():
    assert hasattr(ulmDsl2_LookupIntValue, "value")
    descriptor = None
    for klass in ulmDsl2_LookupIntValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_ulmdsl2_lookupint_is_not_abstract():
    assert not inspect.isabstract(ulmDsl2_LookupInt)


def test_ulmdsl2_lookupint_constructor_exists():
    assert callable(ulmDsl2_LookupInt.__init__)


def test_ulmdsl2_lookupint_constructor_args():
    sig = inspect.signature(ulmDsl2_LookupInt.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"

def test_ulmdsl2_lookupint_has_description():
    assert hasattr(ulmDsl2_LookupInt, "description")
    descriptor = None
    for klass in ulmDsl2_LookupInt.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_ulmdsl2_context_is_not_abstract():
    assert not inspect.isabstract(ulmDsl2_Context)


def test_ulmdsl2_context_constructor_exists():
    assert callable(ulmDsl2_Context.__init__)


def test_ulmdsl2_context_constructor_args():
    sig = inspect.signature(ulmDsl2_Context.__init__)
    params = list(sig.parameters.keys())
    assert "version" in params, "Missing parameter 'version'"
    assert "name" in params, "Missing parameter 'name'"

def test_ulmdsl2_context_has_version():
    assert hasattr(ulmDsl2_Context, "version")
    descriptor = None
    for klass in ulmDsl2_Context.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_ulmdsl2_context_has_name():
    assert hasattr(ulmDsl2_Context, "name")
    descriptor = None
    for klass in ulmDsl2_Context.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ulmdsl2_model_is_not_abstract():
    assert not inspect.isabstract(ulmDsl2_Model)


def test_ulmdsl2_model_constructor_exists():
    assert callable(ulmDsl2_Model.__init__)


def test_ulmdsl2_model_constructor_args():
    sig = inspect.signature(ulmDsl2_Model.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ulmdsl2_model_has_name():
    assert hasattr(ulmDsl2_Model, "name")
    descriptor = None
    for klass in ulmDsl2_Model.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ulmdsl2_attributestringtype_is_not_abstract():
    assert not inspect.isabstract(ulmDsl2_AttributeStringType)


def test_ulmdsl2_attributestringtype_constructor_exists():
    assert callable(ulmDsl2_AttributeStringType.__init__)


def test_ulmdsl2_attributestringtype_constructor_args():
    sig = inspect.signature(ulmDsl2_AttributeStringType.__init__)
    params = list(sig.parameters.keys())
    assert "array" in params, "Missing parameter 'array'"
    assert "length" in params, "Missing parameter 'length'"
    assert "name" in params, "Missing parameter 'name'"

def test_ulmdsl2_attributestringtype_has_array():
    assert hasattr(ulmDsl2_AttributeStringType, "array")
    descriptor = None
    for klass in ulmDsl2_AttributeStringType.__mro__:
        if "array" in klass.__dict__:
            descriptor = klass.__dict__["array"]
            break
    assert isinstance(descriptor, property)

def test_ulmdsl2_attributestringtype_has_length():
    assert hasattr(ulmDsl2_AttributeStringType, "length")
    descriptor = None
    for klass in ulmDsl2_AttributeStringType.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)

def test_ulmdsl2_attributestringtype_has_name():
    assert hasattr(ulmDsl2_AttributeStringType, "name")
    descriptor = None
    for klass in ulmDsl2_AttributeStringType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ulmdsl2_attributetype_is_not_abstract():
    assert not inspect.isabstract(ulmDsl2_AttributeType)


def test_ulmdsl2_attributetype_constructor_exists():
    assert callable(ulmDsl2_AttributeType.__init__)


def test_ulmdsl2_attributetype_constructor_args():
    sig = inspect.signature(ulmDsl2_AttributeType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ulmdsl2_attributetype_has_name():
    assert hasattr(ulmDsl2_AttributeType, "name")
    descriptor = None
    for klass in ulmDsl2_AttributeType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ulmdsl2_eobject_is_not_abstract():
    assert not inspect.isabstract(ulmDsl2_EObject)


def test_ulmdsl2_eobject_constructor_exists():
    assert callable(ulmDsl2_EObject.__init__)


def test_ulmdsl2_eobject_constructor_args():
    sig = inspect.signature(ulmDsl2_EObject.__init__)
    params = list(sig.parameters.keys())



def test_ulmdsl2_entity_is_not_abstract():
    assert not inspect.isabstract(ulmDsl2_Entity)


def test_ulmdsl2_entity_constructor_exists():
    assert callable(ulmDsl2_Entity.__init__)


def test_ulmdsl2_entity_constructor_args():
    sig = inspect.signature(ulmDsl2_Entity.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"
    assert "desc" in params, "Missing parameter 'desc'"

def test_ulmdsl2_entity_has_type():
    assert hasattr(ulmDsl2_Entity, "type")
    descriptor = None
    for klass in ulmDsl2_Entity.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_ulmdsl2_entity_has_name():
    assert hasattr(ulmDsl2_Entity, "name")
    descriptor = None
    for klass in ulmDsl2_Entity.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ulmdsl2_entity_has_desc():
    assert hasattr(ulmDsl2_Entity, "desc")
    descriptor = None
    for klass in ulmDsl2_Entity.__mro__:
        if "desc" in klass.__dict__:
            descriptor = klass.__dict__["desc"]
            break
    assert isinstance(descriptor, property)



def test_ulmdsl2_lookup_is_not_abstract():
    assert not inspect.isabstract(ulmDsl2_Lookup)


def test_ulmdsl2_lookup_constructor_exists():
    assert callable(ulmDsl2_Lookup.__init__)


def test_ulmdsl2_lookup_constructor_args():
    sig = inspect.signature(ulmDsl2_Lookup.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ulmdsl2_lookup_has_name():
    assert hasattr(ulmDsl2_Lookup, "name")
    descriptor = None
    for klass in ulmDsl2_Lookup.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ulmdsl2_attribute_is_not_abstract():
    assert not inspect.isabstract(ulmDsl2_Attribute)


def test_ulmdsl2_attribute_constructor_exists():
    assert callable(ulmDsl2_Attribute.__init__)


def test_ulmdsl2_attribute_constructor_args():
    sig = inspect.signature(ulmDsl2_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "desc" in params, "Missing parameter 'desc'"

def test_ulmdsl2_attribute_has_name():
    assert hasattr(ulmDsl2_Attribute, "name")
    descriptor = None
    for klass in ulmDsl2_Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ulmdsl2_attribute_has_desc():
    assert hasattr(ulmDsl2_Attribute, "desc")
    descriptor = None
    for klass in ulmDsl2_Attribute.__mro__:
        if "desc" in klass.__dict__:
            descriptor = klass.__dict__["desc"]
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
ulmDsl2_EntityFeatureType_strategy = st.builds(
    ulmDsl2_EntityFeatureType,
    length=
        st.integers(),
    array=
        st.booleans()
)
ulmDsl2_AttributeFeatureType_strategy = st.builds(
    ulmDsl2_AttributeFeatureType,
)
ulmDsl2_FeatureType_strategy = st.builds(
    ulmDsl2_FeatureType,
)
ulmDsl2_Feature_strategy = st.builds(
    ulmDsl2_Feature,
    identifier=
        st.booleans(),
    name=
        safe_text,
    mandatory=
        st.booleans()
)
ulmDsl2_AttributeDecimalType_strategy = st.builds(
    ulmDsl2_AttributeDecimalType,
    name=
        safe_text,
    array=
        st.booleans(),
    scale=
        st.integers(),
    precision=
        st.integers()
)
ulmDsl2_LookupStringValue_strategy = st.builds(
    ulmDsl2_LookupStringValue,
    value=
        safe_text,
    description=
        safe_text
)
ulmDsl2_LookupString_strategy = st.builds(
    ulmDsl2_LookupString,
    description=
        safe_text
)
ulmDsl2_LookupIntValue_strategy = st.builds(
    ulmDsl2_LookupIntValue,
    description=
        safe_text,
    value=
        st.integers()
)
ulmDsl2_LookupInt_strategy = st.builds(
    ulmDsl2_LookupInt,
    description=
        safe_text
)
ulmDsl2_Context_strategy = st.builds(
    ulmDsl2_Context,
    version=
        safe_text,
    name=
        safe_text
)
ulmDsl2_Model_strategy = st.builds(
    ulmDsl2_Model,
    name=
        safe_text
)
ulmDsl2_AttributeStringType_strategy = st.builds(
    ulmDsl2_AttributeStringType,
    array=
        st.booleans(),
    length=
        st.integers(),
    name=
        safe_text
)
ulmDsl2_AttributeType_strategy = st.builds(
    ulmDsl2_AttributeType,
    name=
        safe_text
)
ulmDsl2_EObject_strategy = st.builds(
    ulmDsl2_EObject,
)
ulmDsl2_Entity_strategy = st.builds(
    ulmDsl2_Entity,
    type=
        safe_text,
    name=
        safe_text,
    desc=
        safe_text
)
ulmDsl2_Lookup_strategy = st.builds(
    ulmDsl2_Lookup,
    name=
        safe_text
)
ulmDsl2_Attribute_strategy = st.builds(
    ulmDsl2_Attribute,
    name=
        safe_text,
    desc=
        safe_text
)

@given(instance=ulmDsl2_EntityFeatureType_strategy)
@settings(max_examples=50)
def test_ulmdsl2_entityfeaturetype_instantiation(instance):
    assert isinstance(instance, ulmDsl2_EntityFeatureType)



@given(instance=ulmDsl2_EntityFeatureType_strategy)
def test_ulmdsl2_entityfeaturetype_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original



@given(instance=ulmDsl2_EntityFeatureType_strategy)
def test_ulmdsl2_entityfeaturetype_array_setter(instance):
    original = instance.array
    instance.array = original
    assert instance.array == original

@given(instance=ulmDsl2_AttributeFeatureType_strategy)
@settings(max_examples=50)
def test_ulmdsl2_attributefeaturetype_instantiation(instance):
    assert isinstance(instance, ulmDsl2_AttributeFeatureType)

@given(instance=ulmDsl2_FeatureType_strategy)
@settings(max_examples=50)
def test_ulmdsl2_featuretype_instantiation(instance):
    assert isinstance(instance, ulmDsl2_FeatureType)

@given(instance=ulmDsl2_Feature_strategy)
@settings(max_examples=50)
def test_ulmdsl2_feature_instantiation(instance):
    assert isinstance(instance, ulmDsl2_Feature)



@given(instance=ulmDsl2_Feature_strategy)
def test_ulmdsl2_feature_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original



@given(instance=ulmDsl2_Feature_strategy)
def test_ulmdsl2_feature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=ulmDsl2_Feature_strategy)
def test_ulmdsl2_feature_mandatory_setter(instance):
    original = instance.mandatory
    instance.mandatory = original
    assert instance.mandatory == original

@given(instance=ulmDsl2_AttributeDecimalType_strategy)
@settings(max_examples=50)
def test_ulmdsl2_attributedecimaltype_instantiation(instance):
    assert isinstance(instance, ulmDsl2_AttributeDecimalType)



@given(instance=ulmDsl2_AttributeDecimalType_strategy)
def test_ulmdsl2_attributedecimaltype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=ulmDsl2_AttributeDecimalType_strategy)
def test_ulmdsl2_attributedecimaltype_array_setter(instance):
    original = instance.array
    instance.array = original
    assert instance.array == original



@given(instance=ulmDsl2_AttributeDecimalType_strategy)
def test_ulmdsl2_attributedecimaltype_scale_setter(instance):
    original = instance.scale
    instance.scale = original
    assert instance.scale == original



@given(instance=ulmDsl2_AttributeDecimalType_strategy)
def test_ulmdsl2_attributedecimaltype_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original

@given(instance=ulmDsl2_LookupStringValue_strategy)
@settings(max_examples=50)
def test_ulmdsl2_lookupstringvalue_instantiation(instance):
    assert isinstance(instance, ulmDsl2_LookupStringValue)



@given(instance=ulmDsl2_LookupStringValue_strategy)
def test_ulmdsl2_lookupstringvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=ulmDsl2_LookupStringValue_strategy)
def test_ulmdsl2_lookupstringvalue_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=ulmDsl2_LookupString_strategy)
@settings(max_examples=50)
def test_ulmdsl2_lookupstring_instantiation(instance):
    assert isinstance(instance, ulmDsl2_LookupString)



@given(instance=ulmDsl2_LookupString_strategy)
def test_ulmdsl2_lookupstring_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=ulmDsl2_LookupIntValue_strategy)
@settings(max_examples=50)
def test_ulmdsl2_lookupintvalue_instantiation(instance):
    assert isinstance(instance, ulmDsl2_LookupIntValue)



@given(instance=ulmDsl2_LookupIntValue_strategy)
def test_ulmdsl2_lookupintvalue_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=ulmDsl2_LookupIntValue_strategy)
def test_ulmdsl2_lookupintvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ulmDsl2_LookupInt_strategy)
@settings(max_examples=50)
def test_ulmdsl2_lookupint_instantiation(instance):
    assert isinstance(instance, ulmDsl2_LookupInt)



@given(instance=ulmDsl2_LookupInt_strategy)
def test_ulmdsl2_lookupint_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=ulmDsl2_Context_strategy)
@settings(max_examples=50)
def test_ulmdsl2_context_instantiation(instance):
    assert isinstance(instance, ulmDsl2_Context)



@given(instance=ulmDsl2_Context_strategy)
def test_ulmdsl2_context_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original



@given(instance=ulmDsl2_Context_strategy)
def test_ulmdsl2_context_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ulmDsl2_Model_strategy)
@settings(max_examples=50)
def test_ulmdsl2_model_instantiation(instance):
    assert isinstance(instance, ulmDsl2_Model)



@given(instance=ulmDsl2_Model_strategy)
def test_ulmdsl2_model_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ulmDsl2_AttributeStringType_strategy)
@settings(max_examples=50)
def test_ulmdsl2_attributestringtype_instantiation(instance):
    assert isinstance(instance, ulmDsl2_AttributeStringType)



@given(instance=ulmDsl2_AttributeStringType_strategy)
def test_ulmdsl2_attributestringtype_array_setter(instance):
    original = instance.array
    instance.array = original
    assert instance.array == original



@given(instance=ulmDsl2_AttributeStringType_strategy)
def test_ulmdsl2_attributestringtype_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original



@given(instance=ulmDsl2_AttributeStringType_strategy)
def test_ulmdsl2_attributestringtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ulmDsl2_AttributeType_strategy)
@settings(max_examples=50)
def test_ulmdsl2_attributetype_instantiation(instance):
    assert isinstance(instance, ulmDsl2_AttributeType)



@given(instance=ulmDsl2_AttributeType_strategy)
def test_ulmdsl2_attributetype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ulmDsl2_EObject_strategy)
@settings(max_examples=50)
def test_ulmdsl2_eobject_instantiation(instance):
    assert isinstance(instance, ulmDsl2_EObject)

@given(instance=ulmDsl2_Entity_strategy)
@settings(max_examples=50)
def test_ulmdsl2_entity_instantiation(instance):
    assert isinstance(instance, ulmDsl2_Entity)



@given(instance=ulmDsl2_Entity_strategy)
def test_ulmdsl2_entity_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=ulmDsl2_Entity_strategy)
def test_ulmdsl2_entity_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=ulmDsl2_Entity_strategy)
def test_ulmdsl2_entity_desc_setter(instance):
    original = instance.desc
    instance.desc = original
    assert instance.desc == original

@given(instance=ulmDsl2_Lookup_strategy)
@settings(max_examples=50)
def test_ulmdsl2_lookup_instantiation(instance):
    assert isinstance(instance, ulmDsl2_Lookup)



@given(instance=ulmDsl2_Lookup_strategy)
def test_ulmdsl2_lookup_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ulmDsl2_Attribute_strategy)
@settings(max_examples=50)
def test_ulmdsl2_attribute_instantiation(instance):
    assert isinstance(instance, ulmDsl2_Attribute)



@given(instance=ulmDsl2_Attribute_strategy)
def test_ulmdsl2_attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=ulmDsl2_Attribute_strategy)
def test_ulmdsl2_attribute_desc_setter(instance):
    original = instance.desc
    instance.desc = original
    assert instance.desc == original
