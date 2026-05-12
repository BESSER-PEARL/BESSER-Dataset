import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    fm_Attribute,
    fm_Group,
    fm_EObject,
    fm_Constraint,
    fm_FeatureModel,
    fm_Feature,
    AttributeType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_fm_attribute_is_not_abstract():
    assert not inspect.isabstract(fm_Attribute)


def test_fm_attribute_constructor_exists():
    assert callable(fm_Attribute.__init__)


def test_fm_attribute_constructor_args():
    sig = inspect.signature(fm_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "defaultValue" in params, "Missing parameter 'defaultValue'"
    assert "type" in params, "Missing parameter 'type'"
    assert "comment" in params, "Missing parameter 'comment'"
    assert "id" in params, "Missing parameter 'id'"
    assert "description" in params, "Missing parameter 'description'"
    assert "name" in params, "Missing parameter 'name'"

def test_fm_attribute_has_defaultValue():
    assert hasattr(fm_Attribute, "defaultValue")
    descriptor = None
    for klass in fm_Attribute.__mro__:
        if "defaultValue" in klass.__dict__:
            descriptor = klass.__dict__["defaultValue"]
            break
    assert isinstance(descriptor, property)

def test_fm_attribute_has_type():
    assert hasattr(fm_Attribute, "type")
    descriptor = None
    for klass in fm_Attribute.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_fm_attribute_has_comment():
    assert hasattr(fm_Attribute, "comment")
    descriptor = None
    for klass in fm_Attribute.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_fm_attribute_has_id():
    assert hasattr(fm_Attribute, "id")
    descriptor = None
    for klass in fm_Attribute.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_fm_attribute_has_description():
    assert hasattr(fm_Attribute, "description")
    descriptor = None
    for klass in fm_Attribute.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_fm_attribute_has_name():
    assert hasattr(fm_Attribute, "name")
    descriptor = None
    for klass in fm_Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fm_group_is_not_abstract():
    assert not inspect.isabstract(fm_Group)


def test_fm_group_constructor_exists():
    assert callable(fm_Group.__init__)


def test_fm_group_constructor_args():
    sig = inspect.signature(fm_Group.__init__)
    params = list(sig.parameters.keys())
    assert "or_" in params, "Missing parameter 'or_'"
    assert "xor" in params, "Missing parameter 'xor'"
    assert "upper" in params, "Missing parameter 'upper'"
    assert "description" in params, "Missing parameter 'description'"
    assert "lower" in params, "Missing parameter 'lower'"
    assert "comment" in params, "Missing parameter 'comment'"

def test_fm_group_has_or_():
    assert hasattr(fm_Group, "or_")
    descriptor = None
    for klass in fm_Group.__mro__:
        if "or_" in klass.__dict__:
            descriptor = klass.__dict__["or_"]
            break
    assert isinstance(descriptor, property)

def test_fm_group_has_xor():
    assert hasattr(fm_Group, "xor")
    descriptor = None
    for klass in fm_Group.__mro__:
        if "xor" in klass.__dict__:
            descriptor = klass.__dict__["xor"]
            break
    assert isinstance(descriptor, property)

def test_fm_group_has_upper():
    assert hasattr(fm_Group, "upper")
    descriptor = None
    for klass in fm_Group.__mro__:
        if "upper" in klass.__dict__:
            descriptor = klass.__dict__["upper"]
            break
    assert isinstance(descriptor, property)

def test_fm_group_has_description():
    assert hasattr(fm_Group, "description")
    descriptor = None
    for klass in fm_Group.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_fm_group_has_lower():
    assert hasattr(fm_Group, "lower")
    descriptor = None
    for klass in fm_Group.__mro__:
        if "lower" in klass.__dict__:
            descriptor = klass.__dict__["lower"]
            break
    assert isinstance(descriptor, property)

def test_fm_group_has_comment():
    assert hasattr(fm_Group, "comment")
    descriptor = None
    for klass in fm_Group.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_fm_eobject_is_not_abstract():
    assert not inspect.isabstract(fm_EObject)


def test_fm_eobject_constructor_exists():
    assert callable(fm_EObject.__init__)


def test_fm_eobject_constructor_args():
    sig = inspect.signature(fm_EObject.__init__)
    params = list(sig.parameters.keys())



def test_fm_constraint_is_not_abstract():
    assert not inspect.isabstract(fm_Constraint)


def test_fm_constraint_constructor_exists():
    assert callable(fm_Constraint.__init__)


def test_fm_constraint_constructor_args():
    sig = inspect.signature(fm_Constraint.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"
    assert "language" in params, "Missing parameter 'language'"
    assert "description" in params, "Missing parameter 'description'"
    assert "value" in params, "Missing parameter 'value'"

def test_fm_constraint_has_comment():
    assert hasattr(fm_Constraint, "comment")
    descriptor = None
    for klass in fm_Constraint.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_fm_constraint_has_language():
    assert hasattr(fm_Constraint, "language")
    descriptor = None
    for klass in fm_Constraint.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)

def test_fm_constraint_has_description():
    assert hasattr(fm_Constraint, "description")
    descriptor = None
    for klass in fm_Constraint.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_fm_constraint_has_value():
    assert hasattr(fm_Constraint, "value")
    descriptor = None
    for klass in fm_Constraint.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fm_featuremodel_is_not_abstract():
    assert not inspect.isabstract(fm_FeatureModel)


def test_fm_featuremodel_constructor_exists():
    assert callable(fm_FeatureModel.__init__)


def test_fm_featuremodel_constructor_args():
    sig = inspect.signature(fm_FeatureModel.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "comment" in params, "Missing parameter 'comment'"
    assert "version" in params, "Missing parameter 'version'"
    assert "description" in params, "Missing parameter 'description'"

def test_fm_featuremodel_has_name():
    assert hasattr(fm_FeatureModel, "name")
    descriptor = None
    for klass in fm_FeatureModel.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fm_featuremodel_has_comment():
    assert hasattr(fm_FeatureModel, "comment")
    descriptor = None
    for klass in fm_FeatureModel.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_fm_featuremodel_has_version():
    assert hasattr(fm_FeatureModel, "version")
    descriptor = None
    for klass in fm_FeatureModel.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_fm_featuremodel_has_description():
    assert hasattr(fm_FeatureModel, "description")
    descriptor = None
    for klass in fm_FeatureModel.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_fm_feature_is_not_abstract():
    assert not inspect.isabstract(fm_Feature)


def test_fm_feature_constructor_exists():
    assert callable(fm_Feature.__init__)


def test_fm_feature_constructor_args():
    sig = inspect.signature(fm_Feature.__init__)
    params = list(sig.parameters.keys())
    assert "optional" in params, "Missing parameter 'optional'"
    assert "description" in params, "Missing parameter 'description'"
    assert "upper" in params, "Missing parameter 'upper'"
    assert "orphan" in params, "Missing parameter 'orphan'"
    assert "id" in params, "Missing parameter 'id'"
    assert "root" in params, "Missing parameter 'root'"
    assert "lower" in params, "Missing parameter 'lower'"
    assert "cloneable" in params, "Missing parameter 'cloneable'"
    assert "name" in params, "Missing parameter 'name'"
    assert "comment" in params, "Missing parameter 'comment'"
    assert "mandatory" in params, "Missing parameter 'mandatory'"

def test_fm_feature_has_optional():
    assert hasattr(fm_Feature, "optional")
    descriptor = None
    for klass in fm_Feature.__mro__:
        if "optional" in klass.__dict__:
            descriptor = klass.__dict__["optional"]
            break
    assert isinstance(descriptor, property)

def test_fm_feature_has_description():
    assert hasattr(fm_Feature, "description")
    descriptor = None
    for klass in fm_Feature.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_fm_feature_has_upper():
    assert hasattr(fm_Feature, "upper")
    descriptor = None
    for klass in fm_Feature.__mro__:
        if "upper" in klass.__dict__:
            descriptor = klass.__dict__["upper"]
            break
    assert isinstance(descriptor, property)

def test_fm_feature_has_orphan():
    assert hasattr(fm_Feature, "orphan")
    descriptor = None
    for klass in fm_Feature.__mro__:
        if "orphan" in klass.__dict__:
            descriptor = klass.__dict__["orphan"]
            break
    assert isinstance(descriptor, property)

def test_fm_feature_has_id():
    assert hasattr(fm_Feature, "id")
    descriptor = None
    for klass in fm_Feature.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_fm_feature_has_root():
    assert hasattr(fm_Feature, "root")
    descriptor = None
    for klass in fm_Feature.__mro__:
        if "root" in klass.__dict__:
            descriptor = klass.__dict__["root"]
            break
    assert isinstance(descriptor, property)

def test_fm_feature_has_lower():
    assert hasattr(fm_Feature, "lower")
    descriptor = None
    for klass in fm_Feature.__mro__:
        if "lower" in klass.__dict__:
            descriptor = klass.__dict__["lower"]
            break
    assert isinstance(descriptor, property)

def test_fm_feature_has_cloneable():
    assert hasattr(fm_Feature, "cloneable")
    descriptor = None
    for klass in fm_Feature.__mro__:
        if "cloneable" in klass.__dict__:
            descriptor = klass.__dict__["cloneable"]
            break
    assert isinstance(descriptor, property)

def test_fm_feature_has_name():
    assert hasattr(fm_Feature, "name")
    descriptor = None
    for klass in fm_Feature.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fm_feature_has_comment():
    assert hasattr(fm_Feature, "comment")
    descriptor = None
    for klass in fm_Feature.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_fm_feature_has_mandatory():
    assert hasattr(fm_Feature, "mandatory")
    descriptor = None
    for klass in fm_Feature.__mro__:
        if "mandatory" in klass.__dict__:
            descriptor = klass.__dict__["mandatory"]
            break
    assert isinstance(descriptor, property)

def test_attributetype_exists():
    # Check that the Enumeration exists
    assert AttributeType is not None

def test_attributetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AttributeType]
    expected_literals = [
        "INTEGER",
        "BOOLEAN",
        "DOUBLE",
        "STRING",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AttributeType"


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
fm_Attribute_strategy = st.builds(
    fm_Attribute,
    defaultValue=
        safe_text,
    type=
        safe_text,
    comment=
        safe_text,
    id=
        safe_text,
    description=
        safe_text,
    name=
        safe_text
)
fm_Group_strategy = st.builds(
    fm_Group,
    or_=
        st.booleans(),
    xor=
        st.booleans(),
    upper=
        st.integers(),
    description=
        safe_text,
    lower=
        st.integers(),
    comment=
        safe_text
)
fm_EObject_strategy = st.builds(
    fm_EObject,
)
fm_Constraint_strategy = st.builds(
    fm_Constraint,
    comment=
        safe_text,
    language=
        safe_text,
    description=
        safe_text,
    value=
        safe_text
)
fm_FeatureModel_strategy = st.builds(
    fm_FeatureModel,
    name=
        safe_text,
    comment=
        safe_text,
    version=
        safe_text,
    description=
        safe_text
)
fm_Feature_strategy = st.builds(
    fm_Feature,
    optional=
        st.booleans(),
    description=
        safe_text,
    upper=
        st.integers(),
    orphan=
        st.booleans(),
    id=
        safe_text,
    root=
        st.booleans(),
    lower=
        st.integers(),
    cloneable=
        st.booleans(),
    name=
        safe_text,
    comment=
        safe_text,
    mandatory=
        st.booleans()
)

@given(instance=fm_Attribute_strategy)
@settings(max_examples=50)
def test_fm_attribute_instantiation(instance):
    assert isinstance(instance, fm_Attribute)



@given(instance=fm_Attribute_strategy)
def test_fm_attribute_defaultValue_setter(instance):
    original = instance.defaultValue
    instance.defaultValue = original
    assert instance.defaultValue == original



@given(instance=fm_Attribute_strategy)
def test_fm_attribute_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=fm_Attribute_strategy)
def test_fm_attribute_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original



@given(instance=fm_Attribute_strategy)
def test_fm_attribute_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=fm_Attribute_strategy)
def test_fm_attribute_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=fm_Attribute_strategy)
def test_fm_attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fm_Group_strategy)
@settings(max_examples=50)
def test_fm_group_instantiation(instance):
    assert isinstance(instance, fm_Group)



@given(instance=fm_Group_strategy)
def test_fm_group_or__setter(instance):
    original = instance.or_
    instance.or_ = original
    assert instance.or_ == original



@given(instance=fm_Group_strategy)
def test_fm_group_xor_setter(instance):
    original = instance.xor
    instance.xor = original
    assert instance.xor == original



@given(instance=fm_Group_strategy)
def test_fm_group_upper_setter(instance):
    original = instance.upper
    instance.upper = original
    assert instance.upper == original



@given(instance=fm_Group_strategy)
def test_fm_group_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=fm_Group_strategy)
def test_fm_group_lower_setter(instance):
    original = instance.lower
    instance.lower = original
    assert instance.lower == original



@given(instance=fm_Group_strategy)
def test_fm_group_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=fm_EObject_strategy)
@settings(max_examples=50)
def test_fm_eobject_instantiation(instance):
    assert isinstance(instance, fm_EObject)

@given(instance=fm_Constraint_strategy)
@settings(max_examples=50)
def test_fm_constraint_instantiation(instance):
    assert isinstance(instance, fm_Constraint)



@given(instance=fm_Constraint_strategy)
def test_fm_constraint_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original



@given(instance=fm_Constraint_strategy)
def test_fm_constraint_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original



@given(instance=fm_Constraint_strategy)
def test_fm_constraint_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=fm_Constraint_strategy)
def test_fm_constraint_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fm_FeatureModel_strategy)
@settings(max_examples=50)
def test_fm_featuremodel_instantiation(instance):
    assert isinstance(instance, fm_FeatureModel)



@given(instance=fm_FeatureModel_strategy)
def test_fm_featuremodel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fm_FeatureModel_strategy)
def test_fm_featuremodel_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original



@given(instance=fm_FeatureModel_strategy)
def test_fm_featuremodel_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original



@given(instance=fm_FeatureModel_strategy)
def test_fm_featuremodel_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=fm_Feature_strategy)
@settings(max_examples=50)
def test_fm_feature_instantiation(instance):
    assert isinstance(instance, fm_Feature)



@given(instance=fm_Feature_strategy)
def test_fm_feature_optional_setter(instance):
    original = instance.optional
    instance.optional = original
    assert instance.optional == original



@given(instance=fm_Feature_strategy)
def test_fm_feature_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=fm_Feature_strategy)
def test_fm_feature_upper_setter(instance):
    original = instance.upper
    instance.upper = original
    assert instance.upper == original



@given(instance=fm_Feature_strategy)
def test_fm_feature_orphan_setter(instance):
    original = instance.orphan
    instance.orphan = original
    assert instance.orphan == original



@given(instance=fm_Feature_strategy)
def test_fm_feature_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=fm_Feature_strategy)
def test_fm_feature_root_setter(instance):
    original = instance.root
    instance.root = original
    assert instance.root == original



@given(instance=fm_Feature_strategy)
def test_fm_feature_lower_setter(instance):
    original = instance.lower
    instance.lower = original
    assert instance.lower == original



@given(instance=fm_Feature_strategy)
def test_fm_feature_cloneable_setter(instance):
    original = instance.cloneable
    instance.cloneable = original
    assert instance.cloneable == original



@given(instance=fm_Feature_strategy)
def test_fm_feature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fm_Feature_strategy)
def test_fm_feature_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original



@given(instance=fm_Feature_strategy)
def test_fm_feature_mandatory_setter(instance):
    original = instance.mandatory
    instance.mandatory = original
    assert instance.mandatory == original
