import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Attribute,
    featuremodels::SimpleAttribute,
    featuremodels::Instance,
    featuremodels::Constraint,
    featuremodels::FeatureModel,
    featuremodels::Attribute,
    featuremodels::ContainmentAssociation,
    featuremodels::Feature,
    ConstraintType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_attribute_is_not_abstract():
    assert not inspect.isabstract(Attribute)


def test_attribute_constructor_exists():
    assert callable(Attribute.__init__)


def test_attribute_constructor_args():
    sig = inspect.signature(Attribute.__init__)
    params = list(sig.parameters.keys())



def test_featuremodels::simpleattribute_is_not_abstract():
    assert not inspect.isabstract(featuremodels::SimpleAttribute)


def test_featuremodels::simpleattribute_constructor_exists():
    assert callable(featuremodels::SimpleAttribute.__init__)


def test_featuremodels::simpleattribute_constructor_args():
    sig = inspect.signature(featuremodels::SimpleAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "value" in params, "Missing parameter 'value'"

def test_featuremodels::simpleattribute_has_type():
    assert hasattr(featuremodels::SimpleAttribute, "type")
    descriptor = None
    for klass in featuremodels::SimpleAttribute.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_featuremodels::simpleattribute_has_value():
    assert hasattr(featuremodels::SimpleAttribute, "value")
    descriptor = None
    for klass in featuremodels::SimpleAttribute.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_featuremodels::instance_is_not_abstract():
    assert not inspect.isabstract(featuremodels::Instance)


def test_featuremodels::instance_constructor_exists():
    assert callable(featuremodels::Instance.__init__)


def test_featuremodels::instance_constructor_args():
    sig = inspect.signature(featuremodels::Instance.__init__)
    params = list(sig.parameters.keys())
    assert "descritpion" in params, "Missing parameter 'descritpion'"
    assert "id" in params, "Missing parameter 'id'"

def test_featuremodels::instance_has_descritpion():
    assert hasattr(featuremodels::Instance, "descritpion")
    descriptor = None
    for klass in featuremodels::Instance.__mro__:
        if "descritpion" in klass.__dict__:
            descriptor = klass.__dict__["descritpion"]
            break
    assert isinstance(descriptor, property)

def test_featuremodels::instance_has_id():
    assert hasattr(featuremodels::Instance, "id")
    descriptor = None
    for klass in featuremodels::Instance.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_featuremodels::constraint_is_not_abstract():
    assert not inspect.isabstract(featuremodels::Constraint)


def test_featuremodels::constraint_constructor_exists():
    assert callable(featuremodels::Constraint.__init__)


def test_featuremodels::constraint_constructor_args():
    sig = inspect.signature(featuremodels::Constraint.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"
    assert "rule" in params, "Missing parameter 'rule'"

def test_featuremodels::constraint_has_name():
    assert hasattr(featuremodels::Constraint, "name")
    descriptor = None
    for klass in featuremodels::Constraint.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_featuremodels::constraint_has_type():
    assert hasattr(featuremodels::Constraint, "type")
    descriptor = None
    for klass in featuremodels::Constraint.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_featuremodels::constraint_has_rule():
    assert hasattr(featuremodels::Constraint, "rule")
    descriptor = None
    for klass in featuremodels::Constraint.__mro__:
        if "rule" in klass.__dict__:
            descriptor = klass.__dict__["rule"]
            break
    assert isinstance(descriptor, property)



def test_featuremodels::featuremodel_is_not_abstract():
    assert not inspect.isabstract(featuremodels::FeatureModel)


def test_featuremodels::featuremodel_constructor_exists():
    assert callable(featuremodels::FeatureModel.__init__)


def test_featuremodels::featuremodel_constructor_args():
    sig = inspect.signature(featuremodels::FeatureModel.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_featuremodels::featuremodel_has_name():
    assert hasattr(featuremodels::FeatureModel, "name")
    descriptor = None
    for klass in featuremodels::FeatureModel.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_featuremodels::attribute_is_not_abstract():
    assert not inspect.isabstract(featuremodels::Attribute)


def test_featuremodels::attribute_constructor_exists():
    assert callable(featuremodels::Attribute.__init__)


def test_featuremodels::attribute_constructor_args():
    sig = inspect.signature(featuremodels::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_featuremodels::attribute_has_name():
    assert hasattr(featuremodels::Attribute, "name")
    descriptor = None
    for klass in featuremodels::Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_featuremodels::containmentassociation_is_not_abstract():
    assert not inspect.isabstract(featuremodels::ContainmentAssociation)


def test_featuremodels::containmentassociation_constructor_exists():
    assert callable(featuremodels::ContainmentAssociation.__init__)


def test_featuremodels::containmentassociation_constructor_args():
    sig = inspect.signature(featuremodels::ContainmentAssociation.__init__)
    params = list(sig.parameters.keys())
    assert "upperBound" in params, "Missing parameter 'upperBound'"
    assert "lowerBound" in params, "Missing parameter 'lowerBound'"

def test_featuremodels::containmentassociation_has_upperBound():
    assert hasattr(featuremodels::ContainmentAssociation, "upperBound")
    descriptor = None
    for klass in featuremodels::ContainmentAssociation.__mro__:
        if "upperBound" in klass.__dict__:
            descriptor = klass.__dict__["upperBound"]
            break
    assert isinstance(descriptor, property)

def test_featuremodels::containmentassociation_has_lowerBound():
    assert hasattr(featuremodels::ContainmentAssociation, "lowerBound")
    descriptor = None
    for klass in featuremodels::ContainmentAssociation.__mro__:
        if "lowerBound" in klass.__dict__:
            descriptor = klass.__dict__["lowerBound"]
            break
    assert isinstance(descriptor, property)



def test_featuremodels::feature_is_not_abstract():
    assert not inspect.isabstract(featuremodels::Feature)


def test_featuremodels::feature_constructor_exists():
    assert callable(featuremodels::Feature.__init__)


def test_featuremodels::feature_constructor_args():
    sig = inspect.signature(featuremodels::Feature.__init__)
    params = list(sig.parameters.keys())
    assert "lowerBound" in params, "Missing parameter 'lowerBound'"
    assert "root" in params, "Missing parameter 'root'"
    assert "name" in params, "Missing parameter 'name'"
    assert "required" in params, "Missing parameter 'required'"
    assert "upperBound" in params, "Missing parameter 'upperBound'"

def test_featuremodels::feature_has_lowerBound():
    assert hasattr(featuremodels::Feature, "lowerBound")
    descriptor = None
    for klass in featuremodels::Feature.__mro__:
        if "lowerBound" in klass.__dict__:
            descriptor = klass.__dict__["lowerBound"]
            break
    assert isinstance(descriptor, property)

def test_featuremodels::feature_has_root():
    assert hasattr(featuremodels::Feature, "root")
    descriptor = None
    for klass in featuremodels::Feature.__mro__:
        if "root" in klass.__dict__:
            descriptor = klass.__dict__["root"]
            break
    assert isinstance(descriptor, property)

def test_featuremodels::feature_has_name():
    assert hasattr(featuremodels::Feature, "name")
    descriptor = None
    for klass in featuremodels::Feature.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_featuremodels::feature_has_required():
    assert hasattr(featuremodels::Feature, "required")
    descriptor = None
    for klass in featuremodels::Feature.__mro__:
        if "required" in klass.__dict__:
            descriptor = klass.__dict__["required"]
            break
    assert isinstance(descriptor, property)

def test_featuremodels::feature_has_upperBound():
    assert hasattr(featuremodels::Feature, "upperBound")
    descriptor = None
    for klass in featuremodels::Feature.__mro__:
        if "upperBound" in klass.__dict__:
            descriptor = klass.__dict__["upperBound"]
            break
    assert isinstance(descriptor, property)

def test_constrainttype_exists():
    # Check that the Enumeration exists
    assert ConstraintType is not None

def test_constrainttype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ConstraintType]
    expected_literals = [
        "REQUIRES",
        "EXCLUDES",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ConstraintType"


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
Attribute_strategy = st.builds(
    Attribute,
)
featuremodels::SimpleAttribute_strategy = st.builds(
    featuremodels::SimpleAttribute,
    type=
        safe_text,
    value=
        safe_text
)
featuremodels::Instance_strategy = st.builds(
    featuremodels::Instance,
    descritpion=
        safe_text,
    id=
        safe_text
)
featuremodels::Constraint_strategy = st.builds(
    featuremodels::Constraint,
    name=
        safe_text,
    type=
        safe_text,
    rule=
        safe_text
)
featuremodels::FeatureModel_strategy = st.builds(
    featuremodels::FeatureModel,
    name=
        safe_text
)
featuremodels::Attribute_strategy = st.builds(
    featuremodels::Attribute,
    name=
        safe_text
)
featuremodels::ContainmentAssociation_strategy = st.builds(
    featuremodels::ContainmentAssociation,
    upperBound=
        st.integers(),
    lowerBound=
        st.integers()
)
featuremodels::Feature_strategy = st.builds(
    featuremodels::Feature,
    lowerBound=
        st.integers(),
    root=
        st.booleans(),
    name=
        safe_text,
    required=
        st.booleans(),
    upperBound=
        st.integers()
)

@given(instance=Attribute_strategy)
@settings(max_examples=50)
def test_attribute_instantiation(instance):
    assert isinstance(instance, Attribute)

@given(instance=featuremodels::SimpleAttribute_strategy)
@settings(max_examples=50)
def test_featuremodels::simpleattribute_instantiation(instance):
    assert isinstance(instance, featuremodels::SimpleAttribute)

@given(instance=featuremodels::SimpleAttribute_strategy)
def test_featuremodels::simpleattribute_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=featuremodels::SimpleAttribute_strategy)
def test_featuremodels::simpleattribute_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=featuremodels::SimpleAttribute_strategy)
def test_featuremodels::simpleattribute_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=featuremodels::SimpleAttribute_strategy)
def test_featuremodels::simpleattribute_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=featuremodels::Instance_strategy)
@settings(max_examples=50)
def test_featuremodels::instance_instantiation(instance):
    assert isinstance(instance, featuremodels::Instance)

@given(instance=featuremodels::Instance_strategy)
def test_featuremodels::instance_descritpion_type(instance):
    assert isinstance(instance.descritpion, str)


@given(instance=featuremodels::Instance_strategy)
def test_featuremodels::instance_descritpion_setter(instance):
    original = instance.descritpion
    instance.descritpion = original
    assert instance.descritpion == original

@given(instance=featuremodels::Instance_strategy)
def test_featuremodels::instance_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=featuremodels::Instance_strategy)
def test_featuremodels::instance_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=featuremodels::Constraint_strategy)
@settings(max_examples=50)
def test_featuremodels::constraint_instantiation(instance):
    assert isinstance(instance, featuremodels::Constraint)

@given(instance=featuremodels::Constraint_strategy)
def test_featuremodels::constraint_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=featuremodels::Constraint_strategy)
def test_featuremodels::constraint_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=featuremodels::Constraint_strategy)
def test_featuremodels::constraint_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=featuremodels::Constraint_strategy)
def test_featuremodels::constraint_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=featuremodels::Constraint_strategy)
def test_featuremodels::constraint_rule_type(instance):
    assert isinstance(instance.rule, str)


@given(instance=featuremodels::Constraint_strategy)
def test_featuremodels::constraint_rule_setter(instance):
    original = instance.rule
    instance.rule = original
    assert instance.rule == original

@given(instance=featuremodels::FeatureModel_strategy)
@settings(max_examples=50)
def test_featuremodels::featuremodel_instantiation(instance):
    assert isinstance(instance, featuremodels::FeatureModel)

@given(instance=featuremodels::FeatureModel_strategy)
def test_featuremodels::featuremodel_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=featuremodels::FeatureModel_strategy)
def test_featuremodels::featuremodel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=featuremodels::Attribute_strategy)
@settings(max_examples=50)
def test_featuremodels::attribute_instantiation(instance):
    assert isinstance(instance, featuremodels::Attribute)

@given(instance=featuremodels::Attribute_strategy)
def test_featuremodels::attribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=featuremodels::Attribute_strategy)
def test_featuremodels::attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=featuremodels::ContainmentAssociation_strategy)
@settings(max_examples=50)
def test_featuremodels::containmentassociation_instantiation(instance):
    assert isinstance(instance, featuremodels::ContainmentAssociation)

@given(instance=featuremodels::ContainmentAssociation_strategy)
def test_featuremodels::containmentassociation_upperBound_type(instance):
    assert isinstance(instance.upperBound, int)


@given(instance=featuremodels::ContainmentAssociation_strategy)
def test_featuremodels::containmentassociation_upperBound_setter(instance):
    original = instance.upperBound
    instance.upperBound = original
    assert instance.upperBound == original

@given(instance=featuremodels::ContainmentAssociation_strategy)
def test_featuremodels::containmentassociation_lowerBound_type(instance):
    assert isinstance(instance.lowerBound, int)


@given(instance=featuremodels::ContainmentAssociation_strategy)
def test_featuremodels::containmentassociation_lowerBound_setter(instance):
    original = instance.lowerBound
    instance.lowerBound = original
    assert instance.lowerBound == original

@given(instance=featuremodels::Feature_strategy)
@settings(max_examples=50)
def test_featuremodels::feature_instantiation(instance):
    assert isinstance(instance, featuremodels::Feature)

@given(instance=featuremodels::Feature_strategy)
def test_featuremodels::feature_lowerBound_type(instance):
    assert isinstance(instance.lowerBound, int)


@given(instance=featuremodels::Feature_strategy)
def test_featuremodels::feature_lowerBound_setter(instance):
    original = instance.lowerBound
    instance.lowerBound = original
    assert instance.lowerBound == original

@given(instance=featuremodels::Feature_strategy)
def test_featuremodels::feature_root_type(instance):
    assert isinstance(instance.root, bool)


@given(instance=featuremodels::Feature_strategy)
def test_featuremodels::feature_root_setter(instance):
    original = instance.root
    instance.root = original
    assert instance.root == original

@given(instance=featuremodels::Feature_strategy)
def test_featuremodels::feature_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=featuremodels::Feature_strategy)
def test_featuremodels::feature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=featuremodels::Feature_strategy)
def test_featuremodels::feature_required_type(instance):
    assert isinstance(instance.required, bool)


@given(instance=featuremodels::Feature_strategy)
def test_featuremodels::feature_required_setter(instance):
    original = instance.required
    instance.required = original
    assert instance.required == original

@given(instance=featuremodels::Feature_strategy)
def test_featuremodels::feature_upperBound_type(instance):
    assert isinstance(instance.upperBound, int)


@given(instance=featuremodels::Feature_strategy)
def test_featuremodels::feature_upperBound_setter(instance):
    original = instance.upperBound
    instance.upperBound = original
    assert instance.upperBound == original
