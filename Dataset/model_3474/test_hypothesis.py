import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    TreeConstraint,
    myDsl::OptionalTreeConstraint,
    myDsl::OrAlternativeTreeConstraint,
    myDsl::MandatoryTreeConstraint,
    myDsl::TreeConstraint,
    myDsl::FM,
    myDsl::CrossTreeConstraint,
    myDsl::FeatureAttribute,
    myDsl::ParentChildConstraint,
    myDsl::Feature,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_treeconstraint_is_not_abstract():
    assert not inspect.isabstract(TreeConstraint)


def test_treeconstraint_constructor_exists():
    assert callable(TreeConstraint.__init__)


def test_treeconstraint_constructor_args():
    sig = inspect.signature(TreeConstraint.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::optionaltreeconstraint_is_not_abstract():
    assert not inspect.isabstract(myDsl::OptionalTreeConstraint)


def test_mydsl::optionaltreeconstraint_constructor_exists():
    assert callable(myDsl::OptionalTreeConstraint.__init__)


def test_mydsl::optionaltreeconstraint_constructor_args():
    sig = inspect.signature(myDsl::OptionalTreeConstraint.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::oralternativetreeconstraint_is_not_abstract():
    assert not inspect.isabstract(myDsl::OrAlternativeTreeConstraint)


def test_mydsl::oralternativetreeconstraint_constructor_exists():
    assert callable(myDsl::OrAlternativeTreeConstraint.__init__)


def test_mydsl::oralternativetreeconstraint_constructor_args():
    sig = inspect.signature(myDsl::OrAlternativeTreeConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "max" in params, "Missing parameter 'max'"
    assert "min" in params, "Missing parameter 'min'"

def test_mydsl::oralternativetreeconstraint_has_max():
    assert hasattr(myDsl::OrAlternativeTreeConstraint, "max")
    descriptor = None
    for klass in myDsl::OrAlternativeTreeConstraint.__mro__:
        if "max" in klass.__dict__:
            descriptor = klass.__dict__["max"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::oralternativetreeconstraint_has_min():
    assert hasattr(myDsl::OrAlternativeTreeConstraint, "min")
    descriptor = None
    for klass in myDsl::OrAlternativeTreeConstraint.__mro__:
        if "min" in klass.__dict__:
            descriptor = klass.__dict__["min"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::mandatorytreeconstraint_is_not_abstract():
    assert not inspect.isabstract(myDsl::MandatoryTreeConstraint)


def test_mydsl::mandatorytreeconstraint_constructor_exists():
    assert callable(myDsl::MandatoryTreeConstraint.__init__)


def test_mydsl::mandatorytreeconstraint_constructor_args():
    sig = inspect.signature(myDsl::MandatoryTreeConstraint.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::treeconstraint_is_not_abstract():
    assert not inspect.isabstract(myDsl::TreeConstraint)


def test_mydsl::treeconstraint_constructor_exists():
    assert callable(myDsl::TreeConstraint.__init__)


def test_mydsl::treeconstraint_constructor_args():
    sig = inspect.signature(myDsl::TreeConstraint.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::fm_is_not_abstract():
    assert not inspect.isabstract(myDsl::FM)


def test_mydsl::fm_constructor_exists():
    assert callable(myDsl::FM.__init__)


def test_mydsl::fm_constructor_args():
    sig = inspect.signature(myDsl::FM.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::crosstreeconstraint_is_not_abstract():
    assert not inspect.isabstract(myDsl::CrossTreeConstraint)


def test_mydsl::crosstreeconstraint_constructor_exists():
    assert callable(myDsl::CrossTreeConstraint.__init__)


def test_mydsl::crosstreeconstraint_constructor_args():
    sig = inspect.signature(myDsl::CrossTreeConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_mydsl::crosstreeconstraint_has_type():
    assert hasattr(myDsl::CrossTreeConstraint, "type")
    descriptor = None
    for klass in myDsl::CrossTreeConstraint.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::featureattribute_is_not_abstract():
    assert not inspect.isabstract(myDsl::FeatureAttribute)


def test_mydsl::featureattribute_constructor_exists():
    assert callable(myDsl::FeatureAttribute.__init__)


def test_mydsl::featureattribute_constructor_args():
    sig = inspect.signature(myDsl::FeatureAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "defaultValue" in params, "Missing parameter 'defaultValue'"
    assert "nullValue" in params, "Missing parameter 'nullValue'"
    assert "maxValue" in params, "Missing parameter 'maxValue'"
    assert "attributeType" in params, "Missing parameter 'attributeType'"
    assert "minValue" in params, "Missing parameter 'minValue'"

def test_mydsl::featureattribute_has_defaultValue():
    assert hasattr(myDsl::FeatureAttribute, "defaultValue")
    descriptor = None
    for klass in myDsl::FeatureAttribute.__mro__:
        if "defaultValue" in klass.__dict__:
            descriptor = klass.__dict__["defaultValue"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::featureattribute_has_nullValue():
    assert hasattr(myDsl::FeatureAttribute, "nullValue")
    descriptor = None
    for klass in myDsl::FeatureAttribute.__mro__:
        if "nullValue" in klass.__dict__:
            descriptor = klass.__dict__["nullValue"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::featureattribute_has_maxValue():
    assert hasattr(myDsl::FeatureAttribute, "maxValue")
    descriptor = None
    for klass in myDsl::FeatureAttribute.__mro__:
        if "maxValue" in klass.__dict__:
            descriptor = klass.__dict__["maxValue"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::featureattribute_has_attributeType():
    assert hasattr(myDsl::FeatureAttribute, "attributeType")
    descriptor = None
    for klass in myDsl::FeatureAttribute.__mro__:
        if "attributeType" in klass.__dict__:
            descriptor = klass.__dict__["attributeType"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::featureattribute_has_minValue():
    assert hasattr(myDsl::FeatureAttribute, "minValue")
    descriptor = None
    for klass in myDsl::FeatureAttribute.__mro__:
        if "minValue" in klass.__dict__:
            descriptor = klass.__dict__["minValue"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::parentchildconstraint_is_not_abstract():
    assert not inspect.isabstract(myDsl::ParentChildConstraint)


def test_mydsl::parentchildconstraint_constructor_exists():
    assert callable(myDsl::ParentChildConstraint.__init__)


def test_mydsl::parentchildconstraint_constructor_args():
    sig = inspect.signature(myDsl::ParentChildConstraint.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::feature_is_not_abstract():
    assert not inspect.isabstract(myDsl::Feature)


def test_mydsl::feature_constructor_exists():
    assert callable(myDsl::Feature.__init__)


def test_mydsl::feature_constructor_args():
    sig = inspect.signature(myDsl::Feature.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::feature_has_name():
    assert hasattr(myDsl::Feature, "name")
    descriptor = None
    for klass in myDsl::Feature.__mro__:
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
TreeConstraint_strategy = st.builds(
    TreeConstraint,
)
myDsl::OptionalTreeConstraint_strategy = st.builds(
    myDsl::OptionalTreeConstraint,
)
myDsl::OrAlternativeTreeConstraint_strategy = st.builds(
    myDsl::OrAlternativeTreeConstraint,
    max=
        st.integers(),
    min=
        st.integers()
)
myDsl::MandatoryTreeConstraint_strategy = st.builds(
    myDsl::MandatoryTreeConstraint,
)
myDsl::TreeConstraint_strategy = st.builds(
    myDsl::TreeConstraint,
)
myDsl::FM_strategy = st.builds(
    myDsl::FM,
)
myDsl::CrossTreeConstraint_strategy = st.builds(
    myDsl::CrossTreeConstraint,
    type=
        safe_text
)
myDsl::FeatureAttribute_strategy = st.builds(
    myDsl::FeatureAttribute,
    defaultValue=
        st.integers(),
    nullValue=
        st.integers(),
    maxValue=
        st.integers(),
    attributeType=
        safe_text,
    minValue=
        st.integers()
)
myDsl::ParentChildConstraint_strategy = st.builds(
    myDsl::ParentChildConstraint,
)
myDsl::Feature_strategy = st.builds(
    myDsl::Feature,
    name=
        safe_text
)

@given(instance=TreeConstraint_strategy)
@settings(max_examples=50)
def test_treeconstraint_instantiation(instance):
    assert isinstance(instance, TreeConstraint)

@given(instance=myDsl::OptionalTreeConstraint_strategy)
@settings(max_examples=50)
def test_mydsl::optionaltreeconstraint_instantiation(instance):
    assert isinstance(instance, myDsl::OptionalTreeConstraint)

@given(instance=myDsl::OrAlternativeTreeConstraint_strategy)
@settings(max_examples=50)
def test_mydsl::oralternativetreeconstraint_instantiation(instance):
    assert isinstance(instance, myDsl::OrAlternativeTreeConstraint)

@given(instance=myDsl::OrAlternativeTreeConstraint_strategy)
def test_mydsl::oralternativetreeconstraint_max_type(instance):
    assert isinstance(instance.max, int)


@given(instance=myDsl::OrAlternativeTreeConstraint_strategy)
def test_mydsl::oralternativetreeconstraint_max_setter(instance):
    original = instance.max
    instance.max = original
    assert instance.max == original

@given(instance=myDsl::OrAlternativeTreeConstraint_strategy)
def test_mydsl::oralternativetreeconstraint_min_type(instance):
    assert isinstance(instance.min, int)


@given(instance=myDsl::OrAlternativeTreeConstraint_strategy)
def test_mydsl::oralternativetreeconstraint_min_setter(instance):
    original = instance.min
    instance.min = original
    assert instance.min == original

@given(instance=myDsl::MandatoryTreeConstraint_strategy)
@settings(max_examples=50)
def test_mydsl::mandatorytreeconstraint_instantiation(instance):
    assert isinstance(instance, myDsl::MandatoryTreeConstraint)

@given(instance=myDsl::TreeConstraint_strategy)
@settings(max_examples=50)
def test_mydsl::treeconstraint_instantiation(instance):
    assert isinstance(instance, myDsl::TreeConstraint)

@given(instance=myDsl::FM_strategy)
@settings(max_examples=50)
def test_mydsl::fm_instantiation(instance):
    assert isinstance(instance, myDsl::FM)

@given(instance=myDsl::CrossTreeConstraint_strategy)
@settings(max_examples=50)
def test_mydsl::crosstreeconstraint_instantiation(instance):
    assert isinstance(instance, myDsl::CrossTreeConstraint)

@given(instance=myDsl::CrossTreeConstraint_strategy)
def test_mydsl::crosstreeconstraint_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=myDsl::CrossTreeConstraint_strategy)
def test_mydsl::crosstreeconstraint_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=myDsl::FeatureAttribute_strategy)
@settings(max_examples=50)
def test_mydsl::featureattribute_instantiation(instance):
    assert isinstance(instance, myDsl::FeatureAttribute)

@given(instance=myDsl::FeatureAttribute_strategy)
def test_mydsl::featureattribute_defaultValue_type(instance):
    assert isinstance(instance.defaultValue, int)


@given(instance=myDsl::FeatureAttribute_strategy)
def test_mydsl::featureattribute_defaultValue_setter(instance):
    original = instance.defaultValue
    instance.defaultValue = original
    assert instance.defaultValue == original

@given(instance=myDsl::FeatureAttribute_strategy)
def test_mydsl::featureattribute_nullValue_type(instance):
    assert isinstance(instance.nullValue, int)


@given(instance=myDsl::FeatureAttribute_strategy)
def test_mydsl::featureattribute_nullValue_setter(instance):
    original = instance.nullValue
    instance.nullValue = original
    assert instance.nullValue == original

@given(instance=myDsl::FeatureAttribute_strategy)
def test_mydsl::featureattribute_maxValue_type(instance):
    assert isinstance(instance.maxValue, int)


@given(instance=myDsl::FeatureAttribute_strategy)
def test_mydsl::featureattribute_maxValue_setter(instance):
    original = instance.maxValue
    instance.maxValue = original
    assert instance.maxValue == original

@given(instance=myDsl::FeatureAttribute_strategy)
def test_mydsl::featureattribute_attributeType_type(instance):
    assert isinstance(instance.attributeType, str)


@given(instance=myDsl::FeatureAttribute_strategy)
def test_mydsl::featureattribute_attributeType_setter(instance):
    original = instance.attributeType
    instance.attributeType = original
    assert instance.attributeType == original

@given(instance=myDsl::FeatureAttribute_strategy)
def test_mydsl::featureattribute_minValue_type(instance):
    assert isinstance(instance.minValue, int)


@given(instance=myDsl::FeatureAttribute_strategy)
def test_mydsl::featureattribute_minValue_setter(instance):
    original = instance.minValue
    instance.minValue = original
    assert instance.minValue == original

@given(instance=myDsl::ParentChildConstraint_strategy)
@settings(max_examples=50)
def test_mydsl::parentchildconstraint_instantiation(instance):
    assert isinstance(instance, myDsl::ParentChildConstraint)

@given(instance=myDsl::Feature_strategy)
@settings(max_examples=50)
def test_mydsl::feature_instantiation(instance):
    assert isinstance(instance, myDsl::Feature)

@given(instance=myDsl::Feature_strategy)
def test_mydsl::feature_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::Feature_strategy)
def test_mydsl::feature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
