import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    sPLOT2CoCo::CrossTreeConstraint,
    sPLOT2CoCo::FeatureAttribute,
    sPLOT2CoCo::ParentChildConstraint,
    TreeConstraint,
    sPLOT2CoCo::OptionalTreeConstraint,
    sPLOT2CoCo::OrAlternativeTreeConstraint,
    sPLOT2CoCo::MandatoryTreeConstraint,
    sPLOT2CoCo::TreeConstraint,
    sPLOT2CoCo::Feature,
    sPLOT2CoCo::FM,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_splot2coco::crosstreeconstraint_is_not_abstract():
    assert not inspect.isabstract(sPLOT2CoCo::CrossTreeConstraint)


def test_splot2coco::crosstreeconstraint_constructor_exists():
    assert callable(sPLOT2CoCo::CrossTreeConstraint.__init__)


def test_splot2coco::crosstreeconstraint_constructor_args():
    sig = inspect.signature(sPLOT2CoCo::CrossTreeConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_splot2coco::crosstreeconstraint_has_type():
    assert hasattr(sPLOT2CoCo::CrossTreeConstraint, "type")
    descriptor = None
    for klass in sPLOT2CoCo::CrossTreeConstraint.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_splot2coco::featureattribute_is_not_abstract():
    assert not inspect.isabstract(sPLOT2CoCo::FeatureAttribute)


def test_splot2coco::featureattribute_constructor_exists():
    assert callable(sPLOT2CoCo::FeatureAttribute.__init__)


def test_splot2coco::featureattribute_constructor_args():
    sig = inspect.signature(sPLOT2CoCo::FeatureAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "attributeType" in params, "Missing parameter 'attributeType'"
    assert "nullValue" in params, "Missing parameter 'nullValue'"
    assert "minValue" in params, "Missing parameter 'minValue'"
    assert "defaultValue" in params, "Missing parameter 'defaultValue'"
    assert "maxValue" in params, "Missing parameter 'maxValue'"

def test_splot2coco::featureattribute_has_attributeType():
    assert hasattr(sPLOT2CoCo::FeatureAttribute, "attributeType")
    descriptor = None
    for klass in sPLOT2CoCo::FeatureAttribute.__mro__:
        if "attributeType" in klass.__dict__:
            descriptor = klass.__dict__["attributeType"]
            break
    assert isinstance(descriptor, property)

def test_splot2coco::featureattribute_has_nullValue():
    assert hasattr(sPLOT2CoCo::FeatureAttribute, "nullValue")
    descriptor = None
    for klass in sPLOT2CoCo::FeatureAttribute.__mro__:
        if "nullValue" in klass.__dict__:
            descriptor = klass.__dict__["nullValue"]
            break
    assert isinstance(descriptor, property)

def test_splot2coco::featureattribute_has_minValue():
    assert hasattr(sPLOT2CoCo::FeatureAttribute, "minValue")
    descriptor = None
    for klass in sPLOT2CoCo::FeatureAttribute.__mro__:
        if "minValue" in klass.__dict__:
            descriptor = klass.__dict__["minValue"]
            break
    assert isinstance(descriptor, property)

def test_splot2coco::featureattribute_has_defaultValue():
    assert hasattr(sPLOT2CoCo::FeatureAttribute, "defaultValue")
    descriptor = None
    for klass in sPLOT2CoCo::FeatureAttribute.__mro__:
        if "defaultValue" in klass.__dict__:
            descriptor = klass.__dict__["defaultValue"]
            break
    assert isinstance(descriptor, property)

def test_splot2coco::featureattribute_has_maxValue():
    assert hasattr(sPLOT2CoCo::FeatureAttribute, "maxValue")
    descriptor = None
    for klass in sPLOT2CoCo::FeatureAttribute.__mro__:
        if "maxValue" in klass.__dict__:
            descriptor = klass.__dict__["maxValue"]
            break
    assert isinstance(descriptor, property)



def test_splot2coco::parentchildconstraint_is_not_abstract():
    assert not inspect.isabstract(sPLOT2CoCo::ParentChildConstraint)


def test_splot2coco::parentchildconstraint_constructor_exists():
    assert callable(sPLOT2CoCo::ParentChildConstraint.__init__)


def test_splot2coco::parentchildconstraint_constructor_args():
    sig = inspect.signature(sPLOT2CoCo::ParentChildConstraint.__init__)
    params = list(sig.parameters.keys())



def test_treeconstraint_is_not_abstract():
    assert not inspect.isabstract(TreeConstraint)


def test_treeconstraint_constructor_exists():
    assert callable(TreeConstraint.__init__)


def test_treeconstraint_constructor_args():
    sig = inspect.signature(TreeConstraint.__init__)
    params = list(sig.parameters.keys())



def test_splot2coco::optionaltreeconstraint_is_not_abstract():
    assert not inspect.isabstract(sPLOT2CoCo::OptionalTreeConstraint)


def test_splot2coco::optionaltreeconstraint_constructor_exists():
    assert callable(sPLOT2CoCo::OptionalTreeConstraint.__init__)


def test_splot2coco::optionaltreeconstraint_constructor_args():
    sig = inspect.signature(sPLOT2CoCo::OptionalTreeConstraint.__init__)
    params = list(sig.parameters.keys())



def test_splot2coco::oralternativetreeconstraint_is_not_abstract():
    assert not inspect.isabstract(sPLOT2CoCo::OrAlternativeTreeConstraint)


def test_splot2coco::oralternativetreeconstraint_constructor_exists():
    assert callable(sPLOT2CoCo::OrAlternativeTreeConstraint.__init__)


def test_splot2coco::oralternativetreeconstraint_constructor_args():
    sig = inspect.signature(sPLOT2CoCo::OrAlternativeTreeConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "max" in params, "Missing parameter 'max'"
    assert "min" in params, "Missing parameter 'min'"

def test_splot2coco::oralternativetreeconstraint_has_max():
    assert hasattr(sPLOT2CoCo::OrAlternativeTreeConstraint, "max")
    descriptor = None
    for klass in sPLOT2CoCo::OrAlternativeTreeConstraint.__mro__:
        if "max" in klass.__dict__:
            descriptor = klass.__dict__["max"]
            break
    assert isinstance(descriptor, property)

def test_splot2coco::oralternativetreeconstraint_has_min():
    assert hasattr(sPLOT2CoCo::OrAlternativeTreeConstraint, "min")
    descriptor = None
    for klass in sPLOT2CoCo::OrAlternativeTreeConstraint.__mro__:
        if "min" in klass.__dict__:
            descriptor = klass.__dict__["min"]
            break
    assert isinstance(descriptor, property)



def test_splot2coco::mandatorytreeconstraint_is_not_abstract():
    assert not inspect.isabstract(sPLOT2CoCo::MandatoryTreeConstraint)


def test_splot2coco::mandatorytreeconstraint_constructor_exists():
    assert callable(sPLOT2CoCo::MandatoryTreeConstraint.__init__)


def test_splot2coco::mandatorytreeconstraint_constructor_args():
    sig = inspect.signature(sPLOT2CoCo::MandatoryTreeConstraint.__init__)
    params = list(sig.parameters.keys())



def test_splot2coco::treeconstraint_is_not_abstract():
    assert not inspect.isabstract(sPLOT2CoCo::TreeConstraint)


def test_splot2coco::treeconstraint_constructor_exists():
    assert callable(sPLOT2CoCo::TreeConstraint.__init__)


def test_splot2coco::treeconstraint_constructor_args():
    sig = inspect.signature(sPLOT2CoCo::TreeConstraint.__init__)
    params = list(sig.parameters.keys())



def test_splot2coco::feature_is_not_abstract():
    assert not inspect.isabstract(sPLOT2CoCo::Feature)


def test_splot2coco::feature_constructor_exists():
    assert callable(sPLOT2CoCo::Feature.__init__)


def test_splot2coco::feature_constructor_args():
    sig = inspect.signature(sPLOT2CoCo::Feature.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_splot2coco::feature_has_name():
    assert hasattr(sPLOT2CoCo::Feature, "name")
    descriptor = None
    for klass in sPLOT2CoCo::Feature.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_splot2coco::fm_is_not_abstract():
    assert not inspect.isabstract(sPLOT2CoCo::FM)


def test_splot2coco::fm_constructor_exists():
    assert callable(sPLOT2CoCo::FM.__init__)


def test_splot2coco::fm_constructor_args():
    sig = inspect.signature(sPLOT2CoCo::FM.__init__)
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
sPLOT2CoCo::CrossTreeConstraint_strategy = st.builds(
    sPLOT2CoCo::CrossTreeConstraint,
    type=
        safe_text
)
sPLOT2CoCo::FeatureAttribute_strategy = st.builds(
    sPLOT2CoCo::FeatureAttribute,
    attributeType=
        safe_text,
    nullValue=
        st.integers(),
    minValue=
        st.integers(),
    defaultValue=
        st.integers(),
    maxValue=
        st.integers()
)
sPLOT2CoCo::ParentChildConstraint_strategy = st.builds(
    sPLOT2CoCo::ParentChildConstraint,
)
TreeConstraint_strategy = st.builds(
    TreeConstraint,
)
sPLOT2CoCo::OptionalTreeConstraint_strategy = st.builds(
    sPLOT2CoCo::OptionalTreeConstraint,
)
sPLOT2CoCo::OrAlternativeTreeConstraint_strategy = st.builds(
    sPLOT2CoCo::OrAlternativeTreeConstraint,
    max=
        st.integers(),
    min=
        st.integers()
)
sPLOT2CoCo::MandatoryTreeConstraint_strategy = st.builds(
    sPLOT2CoCo::MandatoryTreeConstraint,
)
sPLOT2CoCo::TreeConstraint_strategy = st.builds(
    sPLOT2CoCo::TreeConstraint,
)
sPLOT2CoCo::Feature_strategy = st.builds(
    sPLOT2CoCo::Feature,
    name=
        safe_text
)
sPLOT2CoCo::FM_strategy = st.builds(
    sPLOT2CoCo::FM,
)

@given(instance=sPLOT2CoCo::CrossTreeConstraint_strategy)
@settings(max_examples=50)
def test_splot2coco::crosstreeconstraint_instantiation(instance):
    assert isinstance(instance, sPLOT2CoCo::CrossTreeConstraint)

@given(instance=sPLOT2CoCo::CrossTreeConstraint_strategy)
def test_splot2coco::crosstreeconstraint_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=sPLOT2CoCo::CrossTreeConstraint_strategy)
def test_splot2coco::crosstreeconstraint_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=sPLOT2CoCo::FeatureAttribute_strategy)
@settings(max_examples=50)
def test_splot2coco::featureattribute_instantiation(instance):
    assert isinstance(instance, sPLOT2CoCo::FeatureAttribute)

@given(instance=sPLOT2CoCo::FeatureAttribute_strategy)
def test_splot2coco::featureattribute_attributeType_type(instance):
    assert isinstance(instance.attributeType, str)


@given(instance=sPLOT2CoCo::FeatureAttribute_strategy)
def test_splot2coco::featureattribute_attributeType_setter(instance):
    original = instance.attributeType
    instance.attributeType = original
    assert instance.attributeType == original

@given(instance=sPLOT2CoCo::FeatureAttribute_strategy)
def test_splot2coco::featureattribute_nullValue_type(instance):
    assert isinstance(instance.nullValue, int)


@given(instance=sPLOT2CoCo::FeatureAttribute_strategy)
def test_splot2coco::featureattribute_nullValue_setter(instance):
    original = instance.nullValue
    instance.nullValue = original
    assert instance.nullValue == original

@given(instance=sPLOT2CoCo::FeatureAttribute_strategy)
def test_splot2coco::featureattribute_minValue_type(instance):
    assert isinstance(instance.minValue, int)


@given(instance=sPLOT2CoCo::FeatureAttribute_strategy)
def test_splot2coco::featureattribute_minValue_setter(instance):
    original = instance.minValue
    instance.minValue = original
    assert instance.minValue == original

@given(instance=sPLOT2CoCo::FeatureAttribute_strategy)
def test_splot2coco::featureattribute_defaultValue_type(instance):
    assert isinstance(instance.defaultValue, int)


@given(instance=sPLOT2CoCo::FeatureAttribute_strategy)
def test_splot2coco::featureattribute_defaultValue_setter(instance):
    original = instance.defaultValue
    instance.defaultValue = original
    assert instance.defaultValue == original

@given(instance=sPLOT2CoCo::FeatureAttribute_strategy)
def test_splot2coco::featureattribute_maxValue_type(instance):
    assert isinstance(instance.maxValue, int)


@given(instance=sPLOT2CoCo::FeatureAttribute_strategy)
def test_splot2coco::featureattribute_maxValue_setter(instance):
    original = instance.maxValue
    instance.maxValue = original
    assert instance.maxValue == original

@given(instance=sPLOT2CoCo::ParentChildConstraint_strategy)
@settings(max_examples=50)
def test_splot2coco::parentchildconstraint_instantiation(instance):
    assert isinstance(instance, sPLOT2CoCo::ParentChildConstraint)

@given(instance=TreeConstraint_strategy)
@settings(max_examples=50)
def test_treeconstraint_instantiation(instance):
    assert isinstance(instance, TreeConstraint)

@given(instance=sPLOT2CoCo::OptionalTreeConstraint_strategy)
@settings(max_examples=50)
def test_splot2coco::optionaltreeconstraint_instantiation(instance):
    assert isinstance(instance, sPLOT2CoCo::OptionalTreeConstraint)

@given(instance=sPLOT2CoCo::OrAlternativeTreeConstraint_strategy)
@settings(max_examples=50)
def test_splot2coco::oralternativetreeconstraint_instantiation(instance):
    assert isinstance(instance, sPLOT2CoCo::OrAlternativeTreeConstraint)

@given(instance=sPLOT2CoCo::OrAlternativeTreeConstraint_strategy)
def test_splot2coco::oralternativetreeconstraint_max_type(instance):
    assert isinstance(instance.max, int)


@given(instance=sPLOT2CoCo::OrAlternativeTreeConstraint_strategy)
def test_splot2coco::oralternativetreeconstraint_max_setter(instance):
    original = instance.max
    instance.max = original
    assert instance.max == original

@given(instance=sPLOT2CoCo::OrAlternativeTreeConstraint_strategy)
def test_splot2coco::oralternativetreeconstraint_min_type(instance):
    assert isinstance(instance.min, int)


@given(instance=sPLOT2CoCo::OrAlternativeTreeConstraint_strategy)
def test_splot2coco::oralternativetreeconstraint_min_setter(instance):
    original = instance.min
    instance.min = original
    assert instance.min == original

@given(instance=sPLOT2CoCo::MandatoryTreeConstraint_strategy)
@settings(max_examples=50)
def test_splot2coco::mandatorytreeconstraint_instantiation(instance):
    assert isinstance(instance, sPLOT2CoCo::MandatoryTreeConstraint)

@given(instance=sPLOT2CoCo::TreeConstraint_strategy)
@settings(max_examples=50)
def test_splot2coco::treeconstraint_instantiation(instance):
    assert isinstance(instance, sPLOT2CoCo::TreeConstraint)

@given(instance=sPLOT2CoCo::Feature_strategy)
@settings(max_examples=50)
def test_splot2coco::feature_instantiation(instance):
    assert isinstance(instance, sPLOT2CoCo::Feature)

@given(instance=sPLOT2CoCo::Feature_strategy)
def test_splot2coco::feature_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=sPLOT2CoCo::Feature_strategy)
def test_splot2coco::feature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sPLOT2CoCo::FM_strategy)
@settings(max_examples=50)
def test_splot2coco::fm_instantiation(instance):
    assert isinstance(instance, sPLOT2CoCo::FM)
