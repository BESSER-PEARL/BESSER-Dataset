import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    AttributeValue,
    featuremodel::AttributeValueString,
    featuremodel::AttributeValueInt,
    AttributeType,
    featuremodel::AttributeTypeBoolean,
    featuremodel::AttributeTypeString,
    featuremodel::AttributeTypeEObject,
    featuremodel::AttributeTypeInt,
    featuremodel::AttributeType,
    featuremodel::AttributeValue,
    featuremodel::EObject,
    featuremodel::AttributeValueEObject,
    featuremodel::AttributeValueBoolean,
    featuremodel::Group,
    Rule,
    featuremodel::Constraint,
    featuremodel::Feature,
    featuremodel::Attribute,
    featuremodel::Description,
    featuremodel::FeatureModel,
    featuremodel::Rule,
    VariabilityType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_attributevalue_is_not_abstract():
    assert not inspect.isabstract(AttributeValue)


def test_attributevalue_constructor_exists():
    assert callable(AttributeValue.__init__)


def test_attributevalue_constructor_args():
    sig = inspect.signature(AttributeValue.__init__)
    params = list(sig.parameters.keys())



def test_featuremodel::attributevaluestring_is_not_abstract():
    assert not inspect.isabstract(featuremodel::AttributeValueString)


def test_featuremodel::attributevaluestring_constructor_exists():
    assert callable(featuremodel::AttributeValueString.__init__)


def test_featuremodel::attributevaluestring_constructor_args():
    sig = inspect.signature(featuremodel::AttributeValueString.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_featuremodel::attributevaluestring_has_value():
    assert hasattr(featuremodel::AttributeValueString, "value")
    descriptor = None
    for klass in featuremodel::AttributeValueString.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_featuremodel::attributevalueint_is_not_abstract():
    assert not inspect.isabstract(featuremodel::AttributeValueInt)


def test_featuremodel::attributevalueint_constructor_exists():
    assert callable(featuremodel::AttributeValueInt.__init__)


def test_featuremodel::attributevalueint_constructor_args():
    sig = inspect.signature(featuremodel::AttributeValueInt.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_featuremodel::attributevalueint_has_value():
    assert hasattr(featuremodel::AttributeValueInt, "value")
    descriptor = None
    for klass in featuremodel::AttributeValueInt.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_attributetype_is_not_abstract():
    assert not inspect.isabstract(AttributeType)


def test_attributetype_constructor_exists():
    assert callable(AttributeType.__init__)


def test_attributetype_constructor_args():
    sig = inspect.signature(AttributeType.__init__)
    params = list(sig.parameters.keys())



def test_featuremodel::attributetypeboolean_is_not_abstract():
    assert not inspect.isabstract(featuremodel::AttributeTypeBoolean)


def test_featuremodel::attributetypeboolean_constructor_exists():
    assert callable(featuremodel::AttributeTypeBoolean.__init__)


def test_featuremodel::attributetypeboolean_constructor_args():
    sig = inspect.signature(featuremodel::AttributeTypeBoolean.__init__)
    params = list(sig.parameters.keys())



def test_featuremodel::attributetypestring_is_not_abstract():
    assert not inspect.isabstract(featuremodel::AttributeTypeString)


def test_featuremodel::attributetypestring_constructor_exists():
    assert callable(featuremodel::AttributeTypeString.__init__)


def test_featuremodel::attributetypestring_constructor_args():
    sig = inspect.signature(featuremodel::AttributeTypeString.__init__)
    params = list(sig.parameters.keys())



def test_featuremodel::attributetypeeobject_is_not_abstract():
    assert not inspect.isabstract(featuremodel::AttributeTypeEObject)


def test_featuremodel::attributetypeeobject_constructor_exists():
    assert callable(featuremodel::AttributeTypeEObject.__init__)


def test_featuremodel::attributetypeeobject_constructor_args():
    sig = inspect.signature(featuremodel::AttributeTypeEObject.__init__)
    params = list(sig.parameters.keys())



def test_featuremodel::attributetypeint_is_not_abstract():
    assert not inspect.isabstract(featuremodel::AttributeTypeInt)


def test_featuremodel::attributetypeint_constructor_exists():
    assert callable(featuremodel::AttributeTypeInt.__init__)


def test_featuremodel::attributetypeint_constructor_args():
    sig = inspect.signature(featuremodel::AttributeTypeInt.__init__)
    params = list(sig.parameters.keys())



def test_featuremodel::attributetype_is_not_abstract():
    assert not inspect.isabstract(featuremodel::AttributeType)


def test_featuremodel::attributetype_constructor_exists():
    assert callable(featuremodel::AttributeType.__init__)


def test_featuremodel::attributetype_constructor_args():
    sig = inspect.signature(featuremodel::AttributeType.__init__)
    params = list(sig.parameters.keys())



def test_featuremodel::attributevalue_is_not_abstract():
    assert not inspect.isabstract(featuremodel::AttributeValue)


def test_featuremodel::attributevalue_constructor_exists():
    assert callable(featuremodel::AttributeValue.__init__)


def test_featuremodel::attributevalue_constructor_args():
    sig = inspect.signature(featuremodel::AttributeValue.__init__)
    params = list(sig.parameters.keys())



def test_featuremodel::eobject_is_not_abstract():
    assert not inspect.isabstract(featuremodel::EObject)


def test_featuremodel::eobject_constructor_exists():
    assert callable(featuremodel::EObject.__init__)


def test_featuremodel::eobject_constructor_args():
    sig = inspect.signature(featuremodel::EObject.__init__)
    params = list(sig.parameters.keys())



def test_featuremodel::attributevalueeobject_is_not_abstract():
    assert not inspect.isabstract(featuremodel::AttributeValueEObject)


def test_featuremodel::attributevalueeobject_constructor_exists():
    assert callable(featuremodel::AttributeValueEObject.__init__)


def test_featuremodel::attributevalueeobject_constructor_args():
    sig = inspect.signature(featuremodel::AttributeValueEObject.__init__)
    params = list(sig.parameters.keys())



def test_featuremodel::attributevalueboolean_is_not_abstract():
    assert not inspect.isabstract(featuremodel::AttributeValueBoolean)


def test_featuremodel::attributevalueboolean_constructor_exists():
    assert callable(featuremodel::AttributeValueBoolean.__init__)


def test_featuremodel::attributevalueboolean_constructor_args():
    sig = inspect.signature(featuremodel::AttributeValueBoolean.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_featuremodel::attributevalueboolean_has_value():
    assert hasattr(featuremodel::AttributeValueBoolean, "value")
    descriptor = None
    for klass in featuremodel::AttributeValueBoolean.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_featuremodel::group_is_not_abstract():
    assert not inspect.isabstract(featuremodel::Group)


def test_featuremodel::group_constructor_exists():
    assert callable(featuremodel::Group.__init__)


def test_featuremodel::group_constructor_args():
    sig = inspect.signature(featuremodel::Group.__init__)
    params = list(sig.parameters.keys())
    assert "upper" in params, "Missing parameter 'upper'"
    assert "lower" in params, "Missing parameter 'lower'"
    assert "id" in params, "Missing parameter 'id'"

def test_featuremodel::group_has_upper():
    assert hasattr(featuremodel::Group, "upper")
    descriptor = None
    for klass in featuremodel::Group.__mro__:
        if "upper" in klass.__dict__:
            descriptor = klass.__dict__["upper"]
            break
    assert isinstance(descriptor, property)

def test_featuremodel::group_has_lower():
    assert hasattr(featuremodel::Group, "lower")
    descriptor = None
    for klass in featuremodel::Group.__mro__:
        if "lower" in klass.__dict__:
            descriptor = klass.__dict__["lower"]
            break
    assert isinstance(descriptor, property)

def test_featuremodel::group_has_id():
    assert hasattr(featuremodel::Group, "id")
    descriptor = None
    for klass in featuremodel::Group.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_rule_is_not_abstract():
    assert not inspect.isabstract(Rule)


def test_rule_constructor_exists():
    assert callable(Rule.__init__)


def test_rule_constructor_args():
    sig = inspect.signature(Rule.__init__)
    params = list(sig.parameters.keys())



def test_featuremodel::constraint_is_not_abstract():
    assert not inspect.isabstract(featuremodel::Constraint)


def test_featuremodel::constraint_constructor_exists():
    assert callable(featuremodel::Constraint.__init__)


def test_featuremodel::constraint_constructor_args():
    sig = inspect.signature(featuremodel::Constraint.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_featuremodel::constraint_has_id():
    assert hasattr(featuremodel::Constraint, "id")
    descriptor = None
    for klass in featuremodel::Constraint.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_featuremodel::feature_is_not_abstract():
    assert not inspect.isabstract(featuremodel::Feature)


def test_featuremodel::feature_constructor_exists():
    assert callable(featuremodel::Feature.__init__)


def test_featuremodel::feature_constructor_args():
    sig = inspect.signature(featuremodel::Feature.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"

def test_featuremodel::feature_has_id():
    assert hasattr(featuremodel::Feature, "id")
    descriptor = None
    for klass in featuremodel::Feature.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_featuremodel::feature_has_name():
    assert hasattr(featuremodel::Feature, "name")
    descriptor = None
    for klass in featuremodel::Feature.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_featuremodel::feature_has_type():
    assert hasattr(featuremodel::Feature, "type")
    descriptor = None
    for klass in featuremodel::Feature.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_featuremodel::attribute_is_not_abstract():
    assert not inspect.isabstract(featuremodel::Attribute)


def test_featuremodel::attribute_constructor_exists():
    assert callable(featuremodel::Attribute.__init__)


def test_featuremodel::attribute_constructor_args():
    sig = inspect.signature(featuremodel::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"
    assert "setable" in params, "Missing parameter 'setable'"

def test_featuremodel::attribute_has_id():
    assert hasattr(featuremodel::Attribute, "id")
    descriptor = None
    for klass in featuremodel::Attribute.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_featuremodel::attribute_has_name():
    assert hasattr(featuremodel::Attribute, "name")
    descriptor = None
    for klass in featuremodel::Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_featuremodel::attribute_has_setable():
    assert hasattr(featuremodel::Attribute, "setable")
    descriptor = None
    for klass in featuremodel::Attribute.__mro__:
        if "setable" in klass.__dict__:
            descriptor = klass.__dict__["setable"]
            break
    assert isinstance(descriptor, property)



def test_featuremodel::description_is_not_abstract():
    assert not inspect.isabstract(featuremodel::Description)


def test_featuremodel::description_constructor_exists():
    assert callable(featuremodel::Description.__init__)


def test_featuremodel::description_constructor_args():
    sig = inspect.signature(featuremodel::Description.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "text" in params, "Missing parameter 'text'"

def test_featuremodel::description_has_id():
    assert hasattr(featuremodel::Description, "id")
    descriptor = None
    for klass in featuremodel::Description.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_featuremodel::description_has_text():
    assert hasattr(featuremodel::Description, "text")
    descriptor = None
    for klass in featuremodel::Description.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_featuremodel::featuremodel_is_not_abstract():
    assert not inspect.isabstract(featuremodel::FeatureModel)


def test_featuremodel::featuremodel_constructor_exists():
    assert callable(featuremodel::FeatureModel.__init__)


def test_featuremodel::featuremodel_constructor_args():
    sig = inspect.signature(featuremodel::FeatureModel.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "version" in params, "Missing parameter 'version'"

def test_featuremodel::featuremodel_has_id():
    assert hasattr(featuremodel::FeatureModel, "id")
    descriptor = None
    for klass in featuremodel::FeatureModel.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_featuremodel::featuremodel_has_version():
    assert hasattr(featuremodel::FeatureModel, "version")
    descriptor = None
    for klass in featuremodel::FeatureModel.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)



def test_featuremodel::rule_is_not_abstract():
    assert not inspect.isabstract(featuremodel::Rule)


def test_featuremodel::rule_constructor_exists():
    assert callable(featuremodel::Rule.__init__)


def test_featuremodel::rule_constructor_args():
    sig = inspect.signature(featuremodel::Rule.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "language" in params, "Missing parameter 'language'"

def test_featuremodel::rule_has_code():
    assert hasattr(featuremodel::Rule, "code")
    descriptor = None
    for klass in featuremodel::Rule.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_featuremodel::rule_has_language():
    assert hasattr(featuremodel::Rule, "language")
    descriptor = None
    for klass in featuremodel::Rule.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)

def test_variabilitytype_exists():
    # Check that the Enumeration exists
    assert VariabilityType is not None

def test_variabilitytype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in VariabilityType]
    expected_literals = [
        "alternative",
        "optional",
        "or_",
        "mandatory",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in VariabilityType"


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
AttributeValue_strategy = st.builds(
    AttributeValue,
)
featuremodel::AttributeValueString_strategy = st.builds(
    featuremodel::AttributeValueString,
    value=
        safe_text
)
featuremodel::AttributeValueInt_strategy = st.builds(
    featuremodel::AttributeValueInt,
    value=
        st.integers()
)
AttributeType_strategy = st.builds(
    AttributeType,
)
featuremodel::AttributeTypeBoolean_strategy = st.builds(
    featuremodel::AttributeTypeBoolean,
)
featuremodel::AttributeTypeString_strategy = st.builds(
    featuremodel::AttributeTypeString,
)
featuremodel::AttributeTypeEObject_strategy = st.builds(
    featuremodel::AttributeTypeEObject,
)
featuremodel::AttributeTypeInt_strategy = st.builds(
    featuremodel::AttributeTypeInt,
)
featuremodel::AttributeType_strategy = st.builds(
    featuremodel::AttributeType,
)
featuremodel::AttributeValue_strategy = st.builds(
    featuremodel::AttributeValue,
)
featuremodel::EObject_strategy = st.builds(
    featuremodel::EObject,
)
featuremodel::AttributeValueEObject_strategy = st.builds(
    featuremodel::AttributeValueEObject,
)
featuremodel::AttributeValueBoolean_strategy = st.builds(
    featuremodel::AttributeValueBoolean,
    value=
        st.booleans()
)
featuremodel::Group_strategy = st.builds(
    featuremodel::Group,
    upper=
        st.integers(),
    lower=
        st.integers(),
    id=
        safe_text
)
Rule_strategy = st.builds(
    Rule,
)
featuremodel::Constraint_strategy = st.builds(
    featuremodel::Constraint,
    id=
        safe_text
)
featuremodel::Feature_strategy = st.builds(
    featuremodel::Feature,
    id=
        safe_text,
    name=
        safe_text,
    type=
        safe_text
)
featuremodel::Attribute_strategy = st.builds(
    featuremodel::Attribute,
    id=
        safe_text,
    name=
        safe_text,
    setable=
        st.booleans()
)
featuremodel::Description_strategy = st.builds(
    featuremodel::Description,
    id=
        safe_text,
    text=
        safe_text
)
featuremodel::FeatureModel_strategy = st.builds(
    featuremodel::FeatureModel,
    id=
        safe_text,
    version=
        safe_text
)
featuremodel::Rule_strategy = st.builds(
    featuremodel::Rule,
    code=
        safe_text,
    language=
        safe_text
)

@given(instance=AttributeValue_strategy)
@settings(max_examples=50)
def test_attributevalue_instantiation(instance):
    assert isinstance(instance, AttributeValue)

@given(instance=featuremodel::AttributeValueString_strategy)
@settings(max_examples=50)
def test_featuremodel::attributevaluestring_instantiation(instance):
    assert isinstance(instance, featuremodel::AttributeValueString)

@given(instance=featuremodel::AttributeValueString_strategy)
def test_featuremodel::attributevaluestring_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=featuremodel::AttributeValueString_strategy)
def test_featuremodel::attributevaluestring_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=featuremodel::AttributeValueInt_strategy)
@settings(max_examples=50)
def test_featuremodel::attributevalueint_instantiation(instance):
    assert isinstance(instance, featuremodel::AttributeValueInt)

@given(instance=featuremodel::AttributeValueInt_strategy)
def test_featuremodel::attributevalueint_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=featuremodel::AttributeValueInt_strategy)
def test_featuremodel::attributevalueint_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=AttributeType_strategy)
@settings(max_examples=50)
def test_attributetype_instantiation(instance):
    assert isinstance(instance, AttributeType)

@given(instance=featuremodel::AttributeTypeBoolean_strategy)
@settings(max_examples=50)
def test_featuremodel::attributetypeboolean_instantiation(instance):
    assert isinstance(instance, featuremodel::AttributeTypeBoolean)

@given(instance=featuremodel::AttributeTypeString_strategy)
@settings(max_examples=50)
def test_featuremodel::attributetypestring_instantiation(instance):
    assert isinstance(instance, featuremodel::AttributeTypeString)

@given(instance=featuremodel::AttributeTypeEObject_strategy)
@settings(max_examples=50)
def test_featuremodel::attributetypeeobject_instantiation(instance):
    assert isinstance(instance, featuremodel::AttributeTypeEObject)

@given(instance=featuremodel::AttributeTypeInt_strategy)
@settings(max_examples=50)
def test_featuremodel::attributetypeint_instantiation(instance):
    assert isinstance(instance, featuremodel::AttributeTypeInt)

@given(instance=featuremodel::AttributeType_strategy)
@settings(max_examples=50)
def test_featuremodel::attributetype_instantiation(instance):
    assert isinstance(instance, featuremodel::AttributeType)

@given(instance=featuremodel::AttributeValue_strategy)
@settings(max_examples=50)
def test_featuremodel::attributevalue_instantiation(instance):
    assert isinstance(instance, featuremodel::AttributeValue)

@given(instance=featuremodel::EObject_strategy)
@settings(max_examples=50)
def test_featuremodel::eobject_instantiation(instance):
    assert isinstance(instance, featuremodel::EObject)

@given(instance=featuremodel::AttributeValueEObject_strategy)
@settings(max_examples=50)
def test_featuremodel::attributevalueeobject_instantiation(instance):
    assert isinstance(instance, featuremodel::AttributeValueEObject)

@given(instance=featuremodel::AttributeValueBoolean_strategy)
@settings(max_examples=50)
def test_featuremodel::attributevalueboolean_instantiation(instance):
    assert isinstance(instance, featuremodel::AttributeValueBoolean)

@given(instance=featuremodel::AttributeValueBoolean_strategy)
def test_featuremodel::attributevalueboolean_value_type(instance):
    assert isinstance(instance.value, bool)


@given(instance=featuremodel::AttributeValueBoolean_strategy)
def test_featuremodel::attributevalueboolean_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=featuremodel::Group_strategy)
@settings(max_examples=50)
def test_featuremodel::group_instantiation(instance):
    assert isinstance(instance, featuremodel::Group)

@given(instance=featuremodel::Group_strategy)
def test_featuremodel::group_upper_type(instance):
    assert isinstance(instance.upper, int)


@given(instance=featuremodel::Group_strategy)
def test_featuremodel::group_upper_setter(instance):
    original = instance.upper
    instance.upper = original
    assert instance.upper == original

@given(instance=featuremodel::Group_strategy)
def test_featuremodel::group_lower_type(instance):
    assert isinstance(instance.lower, int)


@given(instance=featuremodel::Group_strategy)
def test_featuremodel::group_lower_setter(instance):
    original = instance.lower
    instance.lower = original
    assert instance.lower == original

@given(instance=featuremodel::Group_strategy)
def test_featuremodel::group_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=featuremodel::Group_strategy)
def test_featuremodel::group_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Rule_strategy)
@settings(max_examples=50)
def test_rule_instantiation(instance):
    assert isinstance(instance, Rule)

@given(instance=featuremodel::Constraint_strategy)
@settings(max_examples=50)
def test_featuremodel::constraint_instantiation(instance):
    assert isinstance(instance, featuremodel::Constraint)

@given(instance=featuremodel::Constraint_strategy)
def test_featuremodel::constraint_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=featuremodel::Constraint_strategy)
def test_featuremodel::constraint_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=featuremodel::Feature_strategy)
@settings(max_examples=50)
def test_featuremodel::feature_instantiation(instance):
    assert isinstance(instance, featuremodel::Feature)

@given(instance=featuremodel::Feature_strategy)
def test_featuremodel::feature_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=featuremodel::Feature_strategy)
def test_featuremodel::feature_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=featuremodel::Feature_strategy)
def test_featuremodel::feature_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=featuremodel::Feature_strategy)
def test_featuremodel::feature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=featuremodel::Feature_strategy)
def test_featuremodel::feature_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=featuremodel::Feature_strategy)
def test_featuremodel::feature_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=featuremodel::Attribute_strategy)
@settings(max_examples=50)
def test_featuremodel::attribute_instantiation(instance):
    assert isinstance(instance, featuremodel::Attribute)

@given(instance=featuremodel::Attribute_strategy)
def test_featuremodel::attribute_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=featuremodel::Attribute_strategy)
def test_featuremodel::attribute_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=featuremodel::Attribute_strategy)
def test_featuremodel::attribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=featuremodel::Attribute_strategy)
def test_featuremodel::attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=featuremodel::Attribute_strategy)
def test_featuremodel::attribute_setable_type(instance):
    assert isinstance(instance.setable, bool)


@given(instance=featuremodel::Attribute_strategy)
def test_featuremodel::attribute_setable_setter(instance):
    original = instance.setable
    instance.setable = original
    assert instance.setable == original

@given(instance=featuremodel::Description_strategy)
@settings(max_examples=50)
def test_featuremodel::description_instantiation(instance):
    assert isinstance(instance, featuremodel::Description)

@given(instance=featuremodel::Description_strategy)
def test_featuremodel::description_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=featuremodel::Description_strategy)
def test_featuremodel::description_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=featuremodel::Description_strategy)
def test_featuremodel::description_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=featuremodel::Description_strategy)
def test_featuremodel::description_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=featuremodel::FeatureModel_strategy)
@settings(max_examples=50)
def test_featuremodel::featuremodel_instantiation(instance):
    assert isinstance(instance, featuremodel::FeatureModel)

@given(instance=featuremodel::FeatureModel_strategy)
def test_featuremodel::featuremodel_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=featuremodel::FeatureModel_strategy)
def test_featuremodel::featuremodel_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=featuremodel::FeatureModel_strategy)
def test_featuremodel::featuremodel_version_type(instance):
    assert isinstance(instance.version, str)


@given(instance=featuremodel::FeatureModel_strategy)
def test_featuremodel::featuremodel_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=featuremodel::Rule_strategy)
@settings(max_examples=50)
def test_featuremodel::rule_instantiation(instance):
    assert isinstance(instance, featuremodel::Rule)

@given(instance=featuremodel::Rule_strategy)
def test_featuremodel::rule_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=featuremodel::Rule_strategy)
def test_featuremodel::rule_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=featuremodel::Rule_strategy)
def test_featuremodel::rule_language_type(instance):
    assert isinstance(instance.language, str)


@given(instance=featuremodel::Rule_strategy)
def test_featuremodel::rule_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original
