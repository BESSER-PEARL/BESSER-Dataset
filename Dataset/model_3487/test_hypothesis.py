import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    fm::Constraint,
    fm::Feature,
    fm::FeatureModel,
    fm::Attribute,
    fm::Group,
    fm::EObject,
    AttributeType,
    ObjectiveFunctionType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_fm::constraint_is_not_abstract():
    assert not inspect.isabstract(fm::Constraint)


def test_fm::constraint_constructor_exists():
    assert callable(fm::Constraint.__init__)


def test_fm::constraint_constructor_args():
    sig = inspect.signature(fm::Constraint.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "language" in params, "Missing parameter 'language'"
    assert "description" in params, "Missing parameter 'description'"
    assert "comment" in params, "Missing parameter 'comment'"

def test_fm::constraint_has_value():
    assert hasattr(fm::Constraint, "value")
    descriptor = None
    for klass in fm::Constraint.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fm::constraint_has_language():
    assert hasattr(fm::Constraint, "language")
    descriptor = None
    for klass in fm::Constraint.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)

def test_fm::constraint_has_description():
    assert hasattr(fm::Constraint, "description")
    descriptor = None
    for klass in fm::Constraint.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_fm::constraint_has_comment():
    assert hasattr(fm::Constraint, "comment")
    descriptor = None
    for klass in fm::Constraint.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_fm::feature_is_not_abstract():
    assert not inspect.isabstract(fm::Feature)


def test_fm::feature_constructor_exists():
    assert callable(fm::Feature.__init__)


def test_fm::feature_constructor_args():
    sig = inspect.signature(fm::Feature.__init__)
    params = list(sig.parameters.keys())
    assert "upper" in params, "Missing parameter 'upper'"
    assert "orphan" in params, "Missing parameter 'orphan'"
    assert "cloneable" in params, "Missing parameter 'cloneable'"
    assert "optional" in params, "Missing parameter 'optional'"
    assert "id" in params, "Missing parameter 'id'"
    assert "mandatory" in params, "Missing parameter 'mandatory'"
    assert "name" in params, "Missing parameter 'name'"
    assert "comment" in params, "Missing parameter 'comment'"
    assert "lower" in params, "Missing parameter 'lower'"
    assert "description" in params, "Missing parameter 'description'"
    assert "root" in params, "Missing parameter 'root'"

def test_fm::feature_has_upper():
    assert hasattr(fm::Feature, "upper")
    descriptor = None
    for klass in fm::Feature.__mro__:
        if "upper" in klass.__dict__:
            descriptor = klass.__dict__["upper"]
            break
    assert isinstance(descriptor, property)

def test_fm::feature_has_orphan():
    assert hasattr(fm::Feature, "orphan")
    descriptor = None
    for klass in fm::Feature.__mro__:
        if "orphan" in klass.__dict__:
            descriptor = klass.__dict__["orphan"]
            break
    assert isinstance(descriptor, property)

def test_fm::feature_has_cloneable():
    assert hasattr(fm::Feature, "cloneable")
    descriptor = None
    for klass in fm::Feature.__mro__:
        if "cloneable" in klass.__dict__:
            descriptor = klass.__dict__["cloneable"]
            break
    assert isinstance(descriptor, property)

def test_fm::feature_has_optional():
    assert hasattr(fm::Feature, "optional")
    descriptor = None
    for klass in fm::Feature.__mro__:
        if "optional" in klass.__dict__:
            descriptor = klass.__dict__["optional"]
            break
    assert isinstance(descriptor, property)

def test_fm::feature_has_id():
    assert hasattr(fm::Feature, "id")
    descriptor = None
    for klass in fm::Feature.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_fm::feature_has_mandatory():
    assert hasattr(fm::Feature, "mandatory")
    descriptor = None
    for klass in fm::Feature.__mro__:
        if "mandatory" in klass.__dict__:
            descriptor = klass.__dict__["mandatory"]
            break
    assert isinstance(descriptor, property)

def test_fm::feature_has_name():
    assert hasattr(fm::Feature, "name")
    descriptor = None
    for klass in fm::Feature.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fm::feature_has_comment():
    assert hasattr(fm::Feature, "comment")
    descriptor = None
    for klass in fm::Feature.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_fm::feature_has_lower():
    assert hasattr(fm::Feature, "lower")
    descriptor = None
    for klass in fm::Feature.__mro__:
        if "lower" in klass.__dict__:
            descriptor = klass.__dict__["lower"]
            break
    assert isinstance(descriptor, property)

def test_fm::feature_has_description():
    assert hasattr(fm::Feature, "description")
    descriptor = None
    for klass in fm::Feature.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_fm::feature_has_root():
    assert hasattr(fm::Feature, "root")
    descriptor = None
    for klass in fm::Feature.__mro__:
        if "root" in klass.__dict__:
            descriptor = klass.__dict__["root"]
            break
    assert isinstance(descriptor, property)



def test_fm::featuremodel_is_not_abstract():
    assert not inspect.isabstract(fm::FeatureModel)


def test_fm::featuremodel_constructor_exists():
    assert callable(fm::FeatureModel.__init__)


def test_fm::featuremodel_constructor_args():
    sig = inspect.signature(fm::FeatureModel.__init__)
    params = list(sig.parameters.keys())
    assert "version" in params, "Missing parameter 'version'"
    assert "name" in params, "Missing parameter 'name'"
    assert "description" in params, "Missing parameter 'description'"
    assert "comment" in params, "Missing parameter 'comment'"

def test_fm::featuremodel_has_version():
    assert hasattr(fm::FeatureModel, "version")
    descriptor = None
    for klass in fm::FeatureModel.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_fm::featuremodel_has_name():
    assert hasattr(fm::FeatureModel, "name")
    descriptor = None
    for klass in fm::FeatureModel.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fm::featuremodel_has_description():
    assert hasattr(fm::FeatureModel, "description")
    descriptor = None
    for klass in fm::FeatureModel.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_fm::featuremodel_has_comment():
    assert hasattr(fm::FeatureModel, "comment")
    descriptor = None
    for klass in fm::FeatureModel.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_fm::attribute_is_not_abstract():
    assert not inspect.isabstract(fm::Attribute)


def test_fm::attribute_constructor_exists():
    assert callable(fm::Attribute.__init__)


def test_fm::attribute_constructor_args():
    sig = inspect.signature(fm::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "qualityAttribute" in params, "Missing parameter 'qualityAttribute'"
    assert "name" in params, "Missing parameter 'name'"
    assert "defaultValue" in params, "Missing parameter 'defaultValue'"
    assert "type" in params, "Missing parameter 'type'"
    assert "maxRangeValue" in params, "Missing parameter 'maxRangeValue'"
    assert "comment" in params, "Missing parameter 'comment'"
    assert "id" in params, "Missing parameter 'id'"
    assert "minimize" in params, "Missing parameter 'minimize'"
    assert "minRangeValue" in params, "Missing parameter 'minRangeValue'"
    assert "resourceAttribute" in params, "Missing parameter 'resourceAttribute'"
    assert "alert" in params, "Missing parameter 'alert'"
    assert "objectiveFunctionAggregator" in params, "Missing parameter 'objectiveFunctionAggregator'"
    assert "weight" in params, "Missing parameter 'weight'"

def test_fm::attribute_has_description():
    assert hasattr(fm::Attribute, "description")
    descriptor = None
    for klass in fm::Attribute.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_fm::attribute_has_qualityAttribute():
    assert hasattr(fm::Attribute, "qualityAttribute")
    descriptor = None
    for klass in fm::Attribute.__mro__:
        if "qualityAttribute" in klass.__dict__:
            descriptor = klass.__dict__["qualityAttribute"]
            break
    assert isinstance(descriptor, property)

def test_fm::attribute_has_name():
    assert hasattr(fm::Attribute, "name")
    descriptor = None
    for klass in fm::Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fm::attribute_has_defaultValue():
    assert hasattr(fm::Attribute, "defaultValue")
    descriptor = None
    for klass in fm::Attribute.__mro__:
        if "defaultValue" in klass.__dict__:
            descriptor = klass.__dict__["defaultValue"]
            break
    assert isinstance(descriptor, property)

def test_fm::attribute_has_type():
    assert hasattr(fm::Attribute, "type")
    descriptor = None
    for klass in fm::Attribute.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_fm::attribute_has_maxRangeValue():
    assert hasattr(fm::Attribute, "maxRangeValue")
    descriptor = None
    for klass in fm::Attribute.__mro__:
        if "maxRangeValue" in klass.__dict__:
            descriptor = klass.__dict__["maxRangeValue"]
            break
    assert isinstance(descriptor, property)

def test_fm::attribute_has_comment():
    assert hasattr(fm::Attribute, "comment")
    descriptor = None
    for klass in fm::Attribute.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_fm::attribute_has_id():
    assert hasattr(fm::Attribute, "id")
    descriptor = None
    for klass in fm::Attribute.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_fm::attribute_has_minimize():
    assert hasattr(fm::Attribute, "minimize")
    descriptor = None
    for klass in fm::Attribute.__mro__:
        if "minimize" in klass.__dict__:
            descriptor = klass.__dict__["minimize"]
            break
    assert isinstance(descriptor, property)

def test_fm::attribute_has_minRangeValue():
    assert hasattr(fm::Attribute, "minRangeValue")
    descriptor = None
    for klass in fm::Attribute.__mro__:
        if "minRangeValue" in klass.__dict__:
            descriptor = klass.__dict__["minRangeValue"]
            break
    assert isinstance(descriptor, property)

def test_fm::attribute_has_resourceAttribute():
    assert hasattr(fm::Attribute, "resourceAttribute")
    descriptor = None
    for klass in fm::Attribute.__mro__:
        if "resourceAttribute" in klass.__dict__:
            descriptor = klass.__dict__["resourceAttribute"]
            break
    assert isinstance(descriptor, property)

def test_fm::attribute_has_alert():
    assert hasattr(fm::Attribute, "alert")
    descriptor = None
    for klass in fm::Attribute.__mro__:
        if "alert" in klass.__dict__:
            descriptor = klass.__dict__["alert"]
            break
    assert isinstance(descriptor, property)

def test_fm::attribute_has_objectiveFunctionAggregator():
    assert hasattr(fm::Attribute, "objectiveFunctionAggregator")
    descriptor = None
    for klass in fm::Attribute.__mro__:
        if "objectiveFunctionAggregator" in klass.__dict__:
            descriptor = klass.__dict__["objectiveFunctionAggregator"]
            break
    assert isinstance(descriptor, property)

def test_fm::attribute_has_weight():
    assert hasattr(fm::Attribute, "weight")
    descriptor = None
    for klass in fm::Attribute.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)



def test_fm::group_is_not_abstract():
    assert not inspect.isabstract(fm::Group)


def test_fm::group_constructor_exists():
    assert callable(fm::Group.__init__)


def test_fm::group_constructor_args():
    sig = inspect.signature(fm::Group.__init__)
    params = list(sig.parameters.keys())
    assert "upper" in params, "Missing parameter 'upper'"
    assert "description" in params, "Missing parameter 'description'"
    assert "xor" in params, "Missing parameter 'xor'"
    assert "comment" in params, "Missing parameter 'comment'"
    assert "or_" in params, "Missing parameter 'or_'"
    assert "lower" in params, "Missing parameter 'lower'"

def test_fm::group_has_upper():
    assert hasattr(fm::Group, "upper")
    descriptor = None
    for klass in fm::Group.__mro__:
        if "upper" in klass.__dict__:
            descriptor = klass.__dict__["upper"]
            break
    assert isinstance(descriptor, property)

def test_fm::group_has_description():
    assert hasattr(fm::Group, "description")
    descriptor = None
    for klass in fm::Group.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_fm::group_has_xor():
    assert hasattr(fm::Group, "xor")
    descriptor = None
    for klass in fm::Group.__mro__:
        if "xor" in klass.__dict__:
            descriptor = klass.__dict__["xor"]
            break
    assert isinstance(descriptor, property)

def test_fm::group_has_comment():
    assert hasattr(fm::Group, "comment")
    descriptor = None
    for klass in fm::Group.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_fm::group_has_or_():
    assert hasattr(fm::Group, "or_")
    descriptor = None
    for klass in fm::Group.__mro__:
        if "or_" in klass.__dict__:
            descriptor = klass.__dict__["or_"]
            break
    assert isinstance(descriptor, property)

def test_fm::group_has_lower():
    assert hasattr(fm::Group, "lower")
    descriptor = None
    for klass in fm::Group.__mro__:
        if "lower" in klass.__dict__:
            descriptor = klass.__dict__["lower"]
            break
    assert isinstance(descriptor, property)



def test_fm::eobject_is_not_abstract():
    assert not inspect.isabstract(fm::EObject)


def test_fm::eobject_constructor_exists():
    assert callable(fm::EObject.__init__)


def test_fm::eobject_constructor_args():
    sig = inspect.signature(fm::EObject.__init__)
    params = list(sig.parameters.keys())

def test_attributetype_exists():
    # Check that the Enumeration exists
    assert AttributeType is not None

def test_attributetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AttributeType]
    expected_literals = [
        "DOUBLE",
        "INTEGER",
        "BOOLEAN",
        "STRING",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AttributeType"

def test_objectivefunctiontype_exists():
    # Check that the Enumeration exists
    assert ObjectiveFunctionType is not None

def test_objectivefunctiontype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ObjectiveFunctionType]
    expected_literals = [
        "PRODUCT",
        "SUM",
        "NOT_ASSIGNED",
        "MINIMUM",
        "MAXIMUM",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ObjectiveFunctionType"


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
fm::Constraint_strategy = st.builds(
    fm::Constraint,
    value=
        safe_text,
    language=
        safe_text,
    description=
        safe_text,
    comment=
        safe_text
)
fm::Feature_strategy = st.builds(
    fm::Feature,
    upper=
        st.integers(),
    orphan=
        st.booleans(),
    cloneable=
        st.booleans(),
    optional=
        st.booleans(),
    id=
        safe_text,
    mandatory=
        st.booleans(),
    name=
        safe_text,
    comment=
        safe_text,
    lower=
        st.integers(),
    description=
        safe_text,
    root=
        st.booleans()
)
fm::FeatureModel_strategy = st.builds(
    fm::FeatureModel,
    version=
        safe_text,
    name=
        safe_text,
    description=
        safe_text,
    comment=
        safe_text
)
fm::Attribute_strategy = st.builds(
    fm::Attribute,
    description=
        safe_text,
    qualityAttribute=
        st.booleans(),
    name=
        safe_text,
    defaultValue=
        safe_text,
    type=
        safe_text,
    maxRangeValue=
        safe_text,
    comment=
        safe_text,
    id=
        safe_text,
    minimize=
        st.booleans(),
    minRangeValue=
        safe_text,
    resourceAttribute=
        st.booleans(),
    alert=
        st.booleans(),
    objectiveFunctionAggregator=
        safe_text,
    weight=
        safe_text
)
fm::Group_strategy = st.builds(
    fm::Group,
    upper=
        st.integers(),
    description=
        safe_text,
    xor=
        st.booleans(),
    comment=
        safe_text,
    or_=
        st.booleans(),
    lower=
        st.integers()
)
fm::EObject_strategy = st.builds(
    fm::EObject,
)

@given(instance=fm::Constraint_strategy)
@settings(max_examples=50)
def test_fm::constraint_instantiation(instance):
    assert isinstance(instance, fm::Constraint)

@given(instance=fm::Constraint_strategy)
def test_fm::constraint_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=fm::Constraint_strategy)
def test_fm::constraint_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fm::Constraint_strategy)
def test_fm::constraint_language_type(instance):
    assert isinstance(instance.language, str)


@given(instance=fm::Constraint_strategy)
def test_fm::constraint_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original

@given(instance=fm::Constraint_strategy)
def test_fm::constraint_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=fm::Constraint_strategy)
def test_fm::constraint_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=fm::Constraint_strategy)
def test_fm::constraint_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=fm::Constraint_strategy)
def test_fm::constraint_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=fm::Feature_strategy)
@settings(max_examples=50)
def test_fm::feature_instantiation(instance):
    assert isinstance(instance, fm::Feature)

@given(instance=fm::Feature_strategy)
def test_fm::feature_upper_type(instance):
    assert isinstance(instance.upper, int)


@given(instance=fm::Feature_strategy)
def test_fm::feature_upper_setter(instance):
    original = instance.upper
    instance.upper = original
    assert instance.upper == original

@given(instance=fm::Feature_strategy)
def test_fm::feature_orphan_type(instance):
    assert isinstance(instance.orphan, bool)


@given(instance=fm::Feature_strategy)
def test_fm::feature_orphan_setter(instance):
    original = instance.orphan
    instance.orphan = original
    assert instance.orphan == original

@given(instance=fm::Feature_strategy)
def test_fm::feature_cloneable_type(instance):
    assert isinstance(instance.cloneable, bool)


@given(instance=fm::Feature_strategy)
def test_fm::feature_cloneable_setter(instance):
    original = instance.cloneable
    instance.cloneable = original
    assert instance.cloneable == original

@given(instance=fm::Feature_strategy)
def test_fm::feature_optional_type(instance):
    assert isinstance(instance.optional, bool)


@given(instance=fm::Feature_strategy)
def test_fm::feature_optional_setter(instance):
    original = instance.optional
    instance.optional = original
    assert instance.optional == original

@given(instance=fm::Feature_strategy)
def test_fm::feature_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=fm::Feature_strategy)
def test_fm::feature_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=fm::Feature_strategy)
def test_fm::feature_mandatory_type(instance):
    assert isinstance(instance.mandatory, bool)


@given(instance=fm::Feature_strategy)
def test_fm::feature_mandatory_setter(instance):
    original = instance.mandatory
    instance.mandatory = original
    assert instance.mandatory == original

@given(instance=fm::Feature_strategy)
def test_fm::feature_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fm::Feature_strategy)
def test_fm::feature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fm::Feature_strategy)
def test_fm::feature_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=fm::Feature_strategy)
def test_fm::feature_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=fm::Feature_strategy)
def test_fm::feature_lower_type(instance):
    assert isinstance(instance.lower, int)


@given(instance=fm::Feature_strategy)
def test_fm::feature_lower_setter(instance):
    original = instance.lower
    instance.lower = original
    assert instance.lower == original

@given(instance=fm::Feature_strategy)
def test_fm::feature_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=fm::Feature_strategy)
def test_fm::feature_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=fm::Feature_strategy)
def test_fm::feature_root_type(instance):
    assert isinstance(instance.root, bool)


@given(instance=fm::Feature_strategy)
def test_fm::feature_root_setter(instance):
    original = instance.root
    instance.root = original
    assert instance.root == original

@given(instance=fm::FeatureModel_strategy)
@settings(max_examples=50)
def test_fm::featuremodel_instantiation(instance):
    assert isinstance(instance, fm::FeatureModel)

@given(instance=fm::FeatureModel_strategy)
def test_fm::featuremodel_version_type(instance):
    assert isinstance(instance.version, str)


@given(instance=fm::FeatureModel_strategy)
def test_fm::featuremodel_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=fm::FeatureModel_strategy)
def test_fm::featuremodel_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fm::FeatureModel_strategy)
def test_fm::featuremodel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fm::FeatureModel_strategy)
def test_fm::featuremodel_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=fm::FeatureModel_strategy)
def test_fm::featuremodel_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=fm::FeatureModel_strategy)
def test_fm::featuremodel_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=fm::FeatureModel_strategy)
def test_fm::featuremodel_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=fm::Attribute_strategy)
@settings(max_examples=50)
def test_fm::attribute_instantiation(instance):
    assert isinstance(instance, fm::Attribute)

@given(instance=fm::Attribute_strategy)
def test_fm::attribute_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=fm::Attribute_strategy)
def test_fm::attribute_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=fm::Attribute_strategy)
def test_fm::attribute_qualityAttribute_type(instance):
    assert isinstance(instance.qualityAttribute, bool)


@given(instance=fm::Attribute_strategy)
def test_fm::attribute_qualityAttribute_setter(instance):
    original = instance.qualityAttribute
    instance.qualityAttribute = original
    assert instance.qualityAttribute == original

@given(instance=fm::Attribute_strategy)
def test_fm::attribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fm::Attribute_strategy)
def test_fm::attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fm::Attribute_strategy)
def test_fm::attribute_defaultValue_type(instance):
    assert isinstance(instance.defaultValue, str)


@given(instance=fm::Attribute_strategy)
def test_fm::attribute_defaultValue_setter(instance):
    original = instance.defaultValue
    instance.defaultValue = original
    assert instance.defaultValue == original

@given(instance=fm::Attribute_strategy)
def test_fm::attribute_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=fm::Attribute_strategy)
def test_fm::attribute_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=fm::Attribute_strategy)
def test_fm::attribute_maxRangeValue_type(instance):
    assert isinstance(instance.maxRangeValue, str)


@given(instance=fm::Attribute_strategy)
def test_fm::attribute_maxRangeValue_setter(instance):
    original = instance.maxRangeValue
    instance.maxRangeValue = original
    assert instance.maxRangeValue == original

@given(instance=fm::Attribute_strategy)
def test_fm::attribute_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=fm::Attribute_strategy)
def test_fm::attribute_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=fm::Attribute_strategy)
def test_fm::attribute_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=fm::Attribute_strategy)
def test_fm::attribute_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=fm::Attribute_strategy)
def test_fm::attribute_minimize_type(instance):
    assert isinstance(instance.minimize, bool)


@given(instance=fm::Attribute_strategy)
def test_fm::attribute_minimize_setter(instance):
    original = instance.minimize
    instance.minimize = original
    assert instance.minimize == original

@given(instance=fm::Attribute_strategy)
def test_fm::attribute_minRangeValue_type(instance):
    assert isinstance(instance.minRangeValue, str)


@given(instance=fm::Attribute_strategy)
def test_fm::attribute_minRangeValue_setter(instance):
    original = instance.minRangeValue
    instance.minRangeValue = original
    assert instance.minRangeValue == original

@given(instance=fm::Attribute_strategy)
def test_fm::attribute_resourceAttribute_type(instance):
    assert isinstance(instance.resourceAttribute, bool)


@given(instance=fm::Attribute_strategy)
def test_fm::attribute_resourceAttribute_setter(instance):
    original = instance.resourceAttribute
    instance.resourceAttribute = original
    assert instance.resourceAttribute == original

@given(instance=fm::Attribute_strategy)
def test_fm::attribute_alert_type(instance):
    assert isinstance(instance.alert, bool)


@given(instance=fm::Attribute_strategy)
def test_fm::attribute_alert_setter(instance):
    original = instance.alert
    instance.alert = original
    assert instance.alert == original

@given(instance=fm::Attribute_strategy)
def test_fm::attribute_objectiveFunctionAggregator_type(instance):
    assert isinstance(instance.objectiveFunctionAggregator, str)


@given(instance=fm::Attribute_strategy)
def test_fm::attribute_objectiveFunctionAggregator_setter(instance):
    original = instance.objectiveFunctionAggregator
    instance.objectiveFunctionAggregator = original
    assert instance.objectiveFunctionAggregator == original

@given(instance=fm::Attribute_strategy)
def test_fm::attribute_weight_type(instance):
    assert isinstance(instance.weight, str)


@given(instance=fm::Attribute_strategy)
def test_fm::attribute_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=fm::Group_strategy)
@settings(max_examples=50)
def test_fm::group_instantiation(instance):
    assert isinstance(instance, fm::Group)

@given(instance=fm::Group_strategy)
def test_fm::group_upper_type(instance):
    assert isinstance(instance.upper, int)


@given(instance=fm::Group_strategy)
def test_fm::group_upper_setter(instance):
    original = instance.upper
    instance.upper = original
    assert instance.upper == original

@given(instance=fm::Group_strategy)
def test_fm::group_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=fm::Group_strategy)
def test_fm::group_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=fm::Group_strategy)
def test_fm::group_xor_type(instance):
    assert isinstance(instance.xor, bool)


@given(instance=fm::Group_strategy)
def test_fm::group_xor_setter(instance):
    original = instance.xor
    instance.xor = original
    assert instance.xor == original

@given(instance=fm::Group_strategy)
def test_fm::group_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=fm::Group_strategy)
def test_fm::group_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=fm::Group_strategy)
def test_fm::group_or__type(instance):
    assert isinstance(instance.or_, bool)


@given(instance=fm::Group_strategy)
def test_fm::group_or__setter(instance):
    original = instance.or_
    instance.or_ = original
    assert instance.or_ == original

@given(instance=fm::Group_strategy)
def test_fm::group_lower_type(instance):
    assert isinstance(instance.lower, int)


@given(instance=fm::Group_strategy)
def test_fm::group_lower_setter(instance):
    original = instance.lower
    instance.lower = original
    assert instance.lower == original

@given(instance=fm::EObject_strategy)
@settings(max_examples=50)
def test_fm::eobject_instantiation(instance):
    assert isinstance(instance, fm::EObject)
