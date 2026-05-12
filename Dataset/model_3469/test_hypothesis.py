import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    AttributeValue,
    featuremodel_AttributeValueString,
    featuremodel_AttributeValueInt,
    AttributeType,
    featuremodel_AttributeTypeEObject,
    featuremodel_AttributeTypeBoolean,
    featuremodel_AttributeTypeString,
    featuremodel_AttributeTypeInt,
    featuremodel_AttributeType,
    featuremodel_AttributeValue,
    featuremodel_EObject,
    featuremodel_AttributeValueEObject,
    featuremodel_AttributeValueBoolean,
    featuremodel_Group,
    Rule,
    featuremodel_Constraint,
    featuremodel_Feature,
    featuremodel_Attribute,
    featuremodel_Description,
    featuremodel_FeatureModel,
    featuremodel_Rule,
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



def test_featuremodel_attributevaluestring_is_not_abstract():
    assert not inspect.isabstract(featuremodel_AttributeValueString)


def test_featuremodel_attributevaluestring_constructor_exists():
    assert callable(featuremodel_AttributeValueString.__init__)


def test_featuremodel_attributevaluestring_constructor_args():
    sig = inspect.signature(featuremodel_AttributeValueString.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_featuremodel_attributevaluestring_has_value():
    assert hasattr(featuremodel_AttributeValueString, "value")
    descriptor = None
    for klass in featuremodel_AttributeValueString.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_featuremodel_attributevalueint_is_not_abstract():
    assert not inspect.isabstract(featuremodel_AttributeValueInt)


def test_featuremodel_attributevalueint_constructor_exists():
    assert callable(featuremodel_AttributeValueInt.__init__)


def test_featuremodel_attributevalueint_constructor_args():
    sig = inspect.signature(featuremodel_AttributeValueInt.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_featuremodel_attributevalueint_has_value():
    assert hasattr(featuremodel_AttributeValueInt, "value")
    descriptor = None
    for klass in featuremodel_AttributeValueInt.__mro__:
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



def test_featuremodel_attributetypeeobject_is_not_abstract():
    assert not inspect.isabstract(featuremodel_AttributeTypeEObject)


def test_featuremodel_attributetypeeobject_constructor_exists():
    assert callable(featuremodel_AttributeTypeEObject.__init__)


def test_featuremodel_attributetypeeobject_constructor_args():
    sig = inspect.signature(featuremodel_AttributeTypeEObject.__init__)
    params = list(sig.parameters.keys())



def test_featuremodel_attributetypeboolean_is_not_abstract():
    assert not inspect.isabstract(featuremodel_AttributeTypeBoolean)


def test_featuremodel_attributetypeboolean_constructor_exists():
    assert callable(featuremodel_AttributeTypeBoolean.__init__)


def test_featuremodel_attributetypeboolean_constructor_args():
    sig = inspect.signature(featuremodel_AttributeTypeBoolean.__init__)
    params = list(sig.parameters.keys())



def test_featuremodel_attributetypestring_is_not_abstract():
    assert not inspect.isabstract(featuremodel_AttributeTypeString)


def test_featuremodel_attributetypestring_constructor_exists():
    assert callable(featuremodel_AttributeTypeString.__init__)


def test_featuremodel_attributetypestring_constructor_args():
    sig = inspect.signature(featuremodel_AttributeTypeString.__init__)
    params = list(sig.parameters.keys())



def test_featuremodel_attributetypeint_is_not_abstract():
    assert not inspect.isabstract(featuremodel_AttributeTypeInt)


def test_featuremodel_attributetypeint_constructor_exists():
    assert callable(featuremodel_AttributeTypeInt.__init__)


def test_featuremodel_attributetypeint_constructor_args():
    sig = inspect.signature(featuremodel_AttributeTypeInt.__init__)
    params = list(sig.parameters.keys())



def test_featuremodel_attributetype_is_not_abstract():
    assert not inspect.isabstract(featuremodel_AttributeType)


def test_featuremodel_attributetype_constructor_exists():
    assert callable(featuremodel_AttributeType.__init__)


def test_featuremodel_attributetype_constructor_args():
    sig = inspect.signature(featuremodel_AttributeType.__init__)
    params = list(sig.parameters.keys())



def test_featuremodel_attributevalue_is_not_abstract():
    assert not inspect.isabstract(featuremodel_AttributeValue)


def test_featuremodel_attributevalue_constructor_exists():
    assert callable(featuremodel_AttributeValue.__init__)


def test_featuremodel_attributevalue_constructor_args():
    sig = inspect.signature(featuremodel_AttributeValue.__init__)
    params = list(sig.parameters.keys())



def test_featuremodel_eobject_is_not_abstract():
    assert not inspect.isabstract(featuremodel_EObject)


def test_featuremodel_eobject_constructor_exists():
    assert callable(featuremodel_EObject.__init__)


def test_featuremodel_eobject_constructor_args():
    sig = inspect.signature(featuremodel_EObject.__init__)
    params = list(sig.parameters.keys())



def test_featuremodel_attributevalueeobject_is_not_abstract():
    assert not inspect.isabstract(featuremodel_AttributeValueEObject)


def test_featuremodel_attributevalueeobject_constructor_exists():
    assert callable(featuremodel_AttributeValueEObject.__init__)


def test_featuremodel_attributevalueeobject_constructor_args():
    sig = inspect.signature(featuremodel_AttributeValueEObject.__init__)
    params = list(sig.parameters.keys())



def test_featuremodel_attributevalueboolean_is_not_abstract():
    assert not inspect.isabstract(featuremodel_AttributeValueBoolean)


def test_featuremodel_attributevalueboolean_constructor_exists():
    assert callable(featuremodel_AttributeValueBoolean.__init__)


def test_featuremodel_attributevalueboolean_constructor_args():
    sig = inspect.signature(featuremodel_AttributeValueBoolean.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_featuremodel_attributevalueboolean_has_value():
    assert hasattr(featuremodel_AttributeValueBoolean, "value")
    descriptor = None
    for klass in featuremodel_AttributeValueBoolean.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_featuremodel_group_is_not_abstract():
    assert not inspect.isabstract(featuremodel_Group)


def test_featuremodel_group_constructor_exists():
    assert callable(featuremodel_Group.__init__)


def test_featuremodel_group_constructor_args():
    sig = inspect.signature(featuremodel_Group.__init__)
    params = list(sig.parameters.keys())
    assert "upper" in params, "Missing parameter 'upper'"
    assert "lower" in params, "Missing parameter 'lower'"
    assert "id" in params, "Missing parameter 'id'"

def test_featuremodel_group_has_upper():
    assert hasattr(featuremodel_Group, "upper")
    descriptor = None
    for klass in featuremodel_Group.__mro__:
        if "upper" in klass.__dict__:
            descriptor = klass.__dict__["upper"]
            break
    assert isinstance(descriptor, property)

def test_featuremodel_group_has_lower():
    assert hasattr(featuremodel_Group, "lower")
    descriptor = None
    for klass in featuremodel_Group.__mro__:
        if "lower" in klass.__dict__:
            descriptor = klass.__dict__["lower"]
            break
    assert isinstance(descriptor, property)

def test_featuremodel_group_has_id():
    assert hasattr(featuremodel_Group, "id")
    descriptor = None
    for klass in featuremodel_Group.__mro__:
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



def test_featuremodel_constraint_is_not_abstract():
    assert not inspect.isabstract(featuremodel_Constraint)


def test_featuremodel_constraint_constructor_exists():
    assert callable(featuremodel_Constraint.__init__)


def test_featuremodel_constraint_constructor_args():
    sig = inspect.signature(featuremodel_Constraint.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_featuremodel_constraint_has_id():
    assert hasattr(featuremodel_Constraint, "id")
    descriptor = None
    for klass in featuremodel_Constraint.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_featuremodel_feature_is_not_abstract():
    assert not inspect.isabstract(featuremodel_Feature)


def test_featuremodel_feature_constructor_exists():
    assert callable(featuremodel_Feature.__init__)


def test_featuremodel_feature_constructor_args():
    sig = inspect.signature(featuremodel_Feature.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"

def test_featuremodel_feature_has_type():
    assert hasattr(featuremodel_Feature, "type")
    descriptor = None
    for klass in featuremodel_Feature.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_featuremodel_feature_has_id():
    assert hasattr(featuremodel_Feature, "id")
    descriptor = None
    for klass in featuremodel_Feature.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_featuremodel_feature_has_name():
    assert hasattr(featuremodel_Feature, "name")
    descriptor = None
    for klass in featuremodel_Feature.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_featuremodel_attribute_is_not_abstract():
    assert not inspect.isabstract(featuremodel_Attribute)


def test_featuremodel_attribute_constructor_exists():
    assert callable(featuremodel_Attribute.__init__)


def test_featuremodel_attribute_constructor_args():
    sig = inspect.signature(featuremodel_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"
    assert "setable" in params, "Missing parameter 'setable'"

def test_featuremodel_attribute_has_id():
    assert hasattr(featuremodel_Attribute, "id")
    descriptor = None
    for klass in featuremodel_Attribute.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_featuremodel_attribute_has_name():
    assert hasattr(featuremodel_Attribute, "name")
    descriptor = None
    for klass in featuremodel_Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_featuremodel_attribute_has_setable():
    assert hasattr(featuremodel_Attribute, "setable")
    descriptor = None
    for klass in featuremodel_Attribute.__mro__:
        if "setable" in klass.__dict__:
            descriptor = klass.__dict__["setable"]
            break
    assert isinstance(descriptor, property)



def test_featuremodel_description_is_not_abstract():
    assert not inspect.isabstract(featuremodel_Description)


def test_featuremodel_description_constructor_exists():
    assert callable(featuremodel_Description.__init__)


def test_featuremodel_description_constructor_args():
    sig = inspect.signature(featuremodel_Description.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "text" in params, "Missing parameter 'text'"

def test_featuremodel_description_has_id():
    assert hasattr(featuremodel_Description, "id")
    descriptor = None
    for klass in featuremodel_Description.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_featuremodel_description_has_text():
    assert hasattr(featuremodel_Description, "text")
    descriptor = None
    for klass in featuremodel_Description.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_featuremodel_featuremodel_is_not_abstract():
    assert not inspect.isabstract(featuremodel_FeatureModel)


def test_featuremodel_featuremodel_constructor_exists():
    assert callable(featuremodel_FeatureModel.__init__)


def test_featuremodel_featuremodel_constructor_args():
    sig = inspect.signature(featuremodel_FeatureModel.__init__)
    params = list(sig.parameters.keys())
    assert "version" in params, "Missing parameter 'version'"
    assert "id" in params, "Missing parameter 'id'"

def test_featuremodel_featuremodel_has_version():
    assert hasattr(featuremodel_FeatureModel, "version")
    descriptor = None
    for klass in featuremodel_FeatureModel.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_featuremodel_featuremodel_has_id():
    assert hasattr(featuremodel_FeatureModel, "id")
    descriptor = None
    for klass in featuremodel_FeatureModel.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_featuremodel_rule_is_not_abstract():
    assert not inspect.isabstract(featuremodel_Rule)


def test_featuremodel_rule_constructor_exists():
    assert callable(featuremodel_Rule.__init__)


def test_featuremodel_rule_constructor_args():
    sig = inspect.signature(featuremodel_Rule.__init__)
    params = list(sig.parameters.keys())
    assert "language" in params, "Missing parameter 'language'"
    assert "code" in params, "Missing parameter 'code'"

def test_featuremodel_rule_has_language():
    assert hasattr(featuremodel_Rule, "language")
    descriptor = None
    for klass in featuremodel_Rule.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)

def test_featuremodel_rule_has_code():
    assert hasattr(featuremodel_Rule, "code")
    descriptor = None
    for klass in featuremodel_Rule.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_variabilitytype_exists():
    # Check that the Enumeration exists
    assert VariabilityType is not None

def test_variabilitytype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in VariabilityType]
    expected_literals = [
        "mandatory",
        "or_",
        "optional",
        "alternative",
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
featuremodel_AttributeValueString_strategy = st.builds(
    featuremodel_AttributeValueString,
    value=
        safe_text
)
featuremodel_AttributeValueInt_strategy = st.builds(
    featuremodel_AttributeValueInt,
    value=
        st.integers()
)
AttributeType_strategy = st.builds(
    AttributeType,
)
featuremodel_AttributeTypeEObject_strategy = st.builds(
    featuremodel_AttributeTypeEObject,
)
featuremodel_AttributeTypeBoolean_strategy = st.builds(
    featuremodel_AttributeTypeBoolean,
)
featuremodel_AttributeTypeString_strategy = st.builds(
    featuremodel_AttributeTypeString,
)
featuremodel_AttributeTypeInt_strategy = st.builds(
    featuremodel_AttributeTypeInt,
)
featuremodel_AttributeType_strategy = st.builds(
    featuremodel_AttributeType,
)
featuremodel_AttributeValue_strategy = st.builds(
    featuremodel_AttributeValue,
)
featuremodel_EObject_strategy = st.builds(
    featuremodel_EObject,
)
featuremodel_AttributeValueEObject_strategy = st.builds(
    featuremodel_AttributeValueEObject,
)
featuremodel_AttributeValueBoolean_strategy = st.builds(
    featuremodel_AttributeValueBoolean,
    value=
        st.booleans()
)
featuremodel_Group_strategy = st.builds(
    featuremodel_Group,
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
featuremodel_Constraint_strategy = st.builds(
    featuremodel_Constraint,
    id=
        safe_text
)
featuremodel_Feature_strategy = st.builds(
    featuremodel_Feature,
    type=
        safe_text,
    id=
        safe_text,
    name=
        safe_text
)
featuremodel_Attribute_strategy = st.builds(
    featuremodel_Attribute,
    id=
        safe_text,
    name=
        safe_text,
    setable=
        st.booleans()
)
featuremodel_Description_strategy = st.builds(
    featuremodel_Description,
    id=
        safe_text,
    text=
        safe_text
)
featuremodel_FeatureModel_strategy = st.builds(
    featuremodel_FeatureModel,
    version=
        safe_text,
    id=
        safe_text
)
featuremodel_Rule_strategy = st.builds(
    featuremodel_Rule,
    language=
        safe_text,
    code=
        safe_text
)

@given(instance=AttributeValue_strategy)
@settings(max_examples=50)
def test_attributevalue_instantiation(instance):
    assert isinstance(instance, AttributeValue)

@given(instance=featuremodel_AttributeValueString_strategy)
@settings(max_examples=50)
def test_featuremodel_attributevaluestring_instantiation(instance):
    assert isinstance(instance, featuremodel_AttributeValueString)



@given(instance=featuremodel_AttributeValueString_strategy)
def test_featuremodel_attributevaluestring_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=featuremodel_AttributeValueInt_strategy)
@settings(max_examples=50)
def test_featuremodel_attributevalueint_instantiation(instance):
    assert isinstance(instance, featuremodel_AttributeValueInt)



@given(instance=featuremodel_AttributeValueInt_strategy)
def test_featuremodel_attributevalueint_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=AttributeType_strategy)
@settings(max_examples=50)
def test_attributetype_instantiation(instance):
    assert isinstance(instance, AttributeType)

@given(instance=featuremodel_AttributeTypeEObject_strategy)
@settings(max_examples=50)
def test_featuremodel_attributetypeeobject_instantiation(instance):
    assert isinstance(instance, featuremodel_AttributeTypeEObject)

@given(instance=featuremodel_AttributeTypeBoolean_strategy)
@settings(max_examples=50)
def test_featuremodel_attributetypeboolean_instantiation(instance):
    assert isinstance(instance, featuremodel_AttributeTypeBoolean)

@given(instance=featuremodel_AttributeTypeString_strategy)
@settings(max_examples=50)
def test_featuremodel_attributetypestring_instantiation(instance):
    assert isinstance(instance, featuremodel_AttributeTypeString)

@given(instance=featuremodel_AttributeTypeInt_strategy)
@settings(max_examples=50)
def test_featuremodel_attributetypeint_instantiation(instance):
    assert isinstance(instance, featuremodel_AttributeTypeInt)

@given(instance=featuremodel_AttributeType_strategy)
@settings(max_examples=50)
def test_featuremodel_attributetype_instantiation(instance):
    assert isinstance(instance, featuremodel_AttributeType)

@given(instance=featuremodel_AttributeValue_strategy)
@settings(max_examples=50)
def test_featuremodel_attributevalue_instantiation(instance):
    assert isinstance(instance, featuremodel_AttributeValue)

@given(instance=featuremodel_EObject_strategy)
@settings(max_examples=50)
def test_featuremodel_eobject_instantiation(instance):
    assert isinstance(instance, featuremodel_EObject)

@given(instance=featuremodel_AttributeValueEObject_strategy)
@settings(max_examples=50)
def test_featuremodel_attributevalueeobject_instantiation(instance):
    assert isinstance(instance, featuremodel_AttributeValueEObject)

@given(instance=featuremodel_AttributeValueBoolean_strategy)
@settings(max_examples=50)
def test_featuremodel_attributevalueboolean_instantiation(instance):
    assert isinstance(instance, featuremodel_AttributeValueBoolean)



@given(instance=featuremodel_AttributeValueBoolean_strategy)
def test_featuremodel_attributevalueboolean_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=featuremodel_Group_strategy)
@settings(max_examples=50)
def test_featuremodel_group_instantiation(instance):
    assert isinstance(instance, featuremodel_Group)



@given(instance=featuremodel_Group_strategy)
def test_featuremodel_group_upper_setter(instance):
    original = instance.upper
    instance.upper = original
    assert instance.upper == original



@given(instance=featuremodel_Group_strategy)
def test_featuremodel_group_lower_setter(instance):
    original = instance.lower
    instance.lower = original
    assert instance.lower == original



@given(instance=featuremodel_Group_strategy)
def test_featuremodel_group_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Rule_strategy)
@settings(max_examples=50)
def test_rule_instantiation(instance):
    assert isinstance(instance, Rule)

@given(instance=featuremodel_Constraint_strategy)
@settings(max_examples=50)
def test_featuremodel_constraint_instantiation(instance):
    assert isinstance(instance, featuremodel_Constraint)



@given(instance=featuremodel_Constraint_strategy)
def test_featuremodel_constraint_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=featuremodel_Feature_strategy)
@settings(max_examples=50)
def test_featuremodel_feature_instantiation(instance):
    assert isinstance(instance, featuremodel_Feature)



@given(instance=featuremodel_Feature_strategy)
def test_featuremodel_feature_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=featuremodel_Feature_strategy)
def test_featuremodel_feature_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=featuremodel_Feature_strategy)
def test_featuremodel_feature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=featuremodel_Attribute_strategy)
@settings(max_examples=50)
def test_featuremodel_attribute_instantiation(instance):
    assert isinstance(instance, featuremodel_Attribute)



@given(instance=featuremodel_Attribute_strategy)
def test_featuremodel_attribute_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=featuremodel_Attribute_strategy)
def test_featuremodel_attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=featuremodel_Attribute_strategy)
def test_featuremodel_attribute_setable_setter(instance):
    original = instance.setable
    instance.setable = original
    assert instance.setable == original

@given(instance=featuremodel_Description_strategy)
@settings(max_examples=50)
def test_featuremodel_description_instantiation(instance):
    assert isinstance(instance, featuremodel_Description)



@given(instance=featuremodel_Description_strategy)
def test_featuremodel_description_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=featuremodel_Description_strategy)
def test_featuremodel_description_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=featuremodel_FeatureModel_strategy)
@settings(max_examples=50)
def test_featuremodel_featuremodel_instantiation(instance):
    assert isinstance(instance, featuremodel_FeatureModel)



@given(instance=featuremodel_FeatureModel_strategy)
def test_featuremodel_featuremodel_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original



@given(instance=featuremodel_FeatureModel_strategy)
def test_featuremodel_featuremodel_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=featuremodel_Rule_strategy)
@settings(max_examples=50)
def test_featuremodel_rule_instantiation(instance):
    assert isinstance(instance, featuremodel_Rule)



@given(instance=featuremodel_Rule_strategy)
def test_featuremodel_rule_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original



@given(instance=featuremodel_Rule_strategy)
def test_featuremodel_rule_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original
