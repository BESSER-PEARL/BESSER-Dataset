import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    sPLOT2CoCo_CrossTreeConstraint,
    sPLOT2CoCo_FeatureAttribute,
    sPLOT2CoCo_ParentChildConstraint,
    TreeConstraint,
    sPLOT2CoCo_OrAlternativeTreeConstraint,
    sPLOT2CoCo_OptionalTreeConstraint,
    sPLOT2CoCo_MandatoryTreeConstraint,
    sPLOT2CoCo_TreeConstraint,
    sPLOT2CoCo_Feature,
    sPLOT2CoCo_FM,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_splot2coco_crosstreeconstraint_is_not_abstract():
    assert not inspect.isabstract(sPLOT2CoCo_CrossTreeConstraint)


def test_splot2coco_crosstreeconstraint_constructor_exists():
    assert callable(sPLOT2CoCo_CrossTreeConstraint.__init__)


def test_splot2coco_crosstreeconstraint_constructor_args():
    sig = inspect.signature(sPLOT2CoCo_CrossTreeConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_splot2coco_crosstreeconstraint_has_type():
    assert hasattr(sPLOT2CoCo_CrossTreeConstraint, "type")
    descriptor = None
    for klass in sPLOT2CoCo_CrossTreeConstraint.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_splot2coco_featureattribute_is_not_abstract():
    assert not inspect.isabstract(sPLOT2CoCo_FeatureAttribute)


def test_splot2coco_featureattribute_constructor_exists():
    assert callable(sPLOT2CoCo_FeatureAttribute.__init__)


def test_splot2coco_featureattribute_constructor_args():
    sig = inspect.signature(sPLOT2CoCo_FeatureAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "defaultValue" in params, "Missing parameter 'defaultValue'"
    assert "nullValue" in params, "Missing parameter 'nullValue'"
    assert "maxValue" in params, "Missing parameter 'maxValue'"
    assert "minValue" in params, "Missing parameter 'minValue'"
    assert "attributeType" in params, "Missing parameter 'attributeType'"

def test_splot2coco_featureattribute_has_defaultValue():
    assert hasattr(sPLOT2CoCo_FeatureAttribute, "defaultValue")
    descriptor = None
    for klass in sPLOT2CoCo_FeatureAttribute.__mro__:
        if "defaultValue" in klass.__dict__:
            descriptor = klass.__dict__["defaultValue"]
            break
    assert isinstance(descriptor, property)

def test_splot2coco_featureattribute_has_nullValue():
    assert hasattr(sPLOT2CoCo_FeatureAttribute, "nullValue")
    descriptor = None
    for klass in sPLOT2CoCo_FeatureAttribute.__mro__:
        if "nullValue" in klass.__dict__:
            descriptor = klass.__dict__["nullValue"]
            break
    assert isinstance(descriptor, property)

def test_splot2coco_featureattribute_has_maxValue():
    assert hasattr(sPLOT2CoCo_FeatureAttribute, "maxValue")
    descriptor = None
    for klass in sPLOT2CoCo_FeatureAttribute.__mro__:
        if "maxValue" in klass.__dict__:
            descriptor = klass.__dict__["maxValue"]
            break
    assert isinstance(descriptor, property)

def test_splot2coco_featureattribute_has_minValue():
    assert hasattr(sPLOT2CoCo_FeatureAttribute, "minValue")
    descriptor = None
    for klass in sPLOT2CoCo_FeatureAttribute.__mro__:
        if "minValue" in klass.__dict__:
            descriptor = klass.__dict__["minValue"]
            break
    assert isinstance(descriptor, property)

def test_splot2coco_featureattribute_has_attributeType():
    assert hasattr(sPLOT2CoCo_FeatureAttribute, "attributeType")
    descriptor = None
    for klass in sPLOT2CoCo_FeatureAttribute.__mro__:
        if "attributeType" in klass.__dict__:
            descriptor = klass.__dict__["attributeType"]
            break
    assert isinstance(descriptor, property)



def test_splot2coco_parentchildconstraint_is_not_abstract():
    assert not inspect.isabstract(sPLOT2CoCo_ParentChildConstraint)


def test_splot2coco_parentchildconstraint_constructor_exists():
    assert callable(sPLOT2CoCo_ParentChildConstraint.__init__)


def test_splot2coco_parentchildconstraint_constructor_args():
    sig = inspect.signature(sPLOT2CoCo_ParentChildConstraint.__init__)
    params = list(sig.parameters.keys())



def test_treeconstraint_is_not_abstract():
    assert not inspect.isabstract(TreeConstraint)


def test_treeconstraint_constructor_exists():
    assert callable(TreeConstraint.__init__)


def test_treeconstraint_constructor_args():
    sig = inspect.signature(TreeConstraint.__init__)
    params = list(sig.parameters.keys())



def test_splot2coco_oralternativetreeconstraint_is_not_abstract():
    assert not inspect.isabstract(sPLOT2CoCo_OrAlternativeTreeConstraint)


def test_splot2coco_oralternativetreeconstraint_constructor_exists():
    assert callable(sPLOT2CoCo_OrAlternativeTreeConstraint.__init__)


def test_splot2coco_oralternativetreeconstraint_constructor_args():
    sig = inspect.signature(sPLOT2CoCo_OrAlternativeTreeConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "min" in params, "Missing parameter 'min'"
    assert "max" in params, "Missing parameter 'max'"

def test_splot2coco_oralternativetreeconstraint_has_min():
    assert hasattr(sPLOT2CoCo_OrAlternativeTreeConstraint, "min")
    descriptor = None
    for klass in sPLOT2CoCo_OrAlternativeTreeConstraint.__mro__:
        if "min" in klass.__dict__:
            descriptor = klass.__dict__["min"]
            break
    assert isinstance(descriptor, property)

def test_splot2coco_oralternativetreeconstraint_has_max():
    assert hasattr(sPLOT2CoCo_OrAlternativeTreeConstraint, "max")
    descriptor = None
    for klass in sPLOT2CoCo_OrAlternativeTreeConstraint.__mro__:
        if "max" in klass.__dict__:
            descriptor = klass.__dict__["max"]
            break
    assert isinstance(descriptor, property)



def test_splot2coco_optionaltreeconstraint_is_not_abstract():
    assert not inspect.isabstract(sPLOT2CoCo_OptionalTreeConstraint)


def test_splot2coco_optionaltreeconstraint_constructor_exists():
    assert callable(sPLOT2CoCo_OptionalTreeConstraint.__init__)


def test_splot2coco_optionaltreeconstraint_constructor_args():
    sig = inspect.signature(sPLOT2CoCo_OptionalTreeConstraint.__init__)
    params = list(sig.parameters.keys())



def test_splot2coco_mandatorytreeconstraint_is_not_abstract():
    assert not inspect.isabstract(sPLOT2CoCo_MandatoryTreeConstraint)


def test_splot2coco_mandatorytreeconstraint_constructor_exists():
    assert callable(sPLOT2CoCo_MandatoryTreeConstraint.__init__)


def test_splot2coco_mandatorytreeconstraint_constructor_args():
    sig = inspect.signature(sPLOT2CoCo_MandatoryTreeConstraint.__init__)
    params = list(sig.parameters.keys())



def test_splot2coco_treeconstraint_is_not_abstract():
    assert not inspect.isabstract(sPLOT2CoCo_TreeConstraint)


def test_splot2coco_treeconstraint_constructor_exists():
    assert callable(sPLOT2CoCo_TreeConstraint.__init__)


def test_splot2coco_treeconstraint_constructor_args():
    sig = inspect.signature(sPLOT2CoCo_TreeConstraint.__init__)
    params = list(sig.parameters.keys())



def test_splot2coco_feature_is_not_abstract():
    assert not inspect.isabstract(sPLOT2CoCo_Feature)


def test_splot2coco_feature_constructor_exists():
    assert callable(sPLOT2CoCo_Feature.__init__)


def test_splot2coco_feature_constructor_args():
    sig = inspect.signature(sPLOT2CoCo_Feature.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_splot2coco_feature_has_name():
    assert hasattr(sPLOT2CoCo_Feature, "name")
    descriptor = None
    for klass in sPLOT2CoCo_Feature.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_splot2coco_fm_is_not_abstract():
    assert not inspect.isabstract(sPLOT2CoCo_FM)


def test_splot2coco_fm_constructor_exists():
    assert callable(sPLOT2CoCo_FM.__init__)


def test_splot2coco_fm_constructor_args():
    sig = inspect.signature(sPLOT2CoCo_FM.__init__)
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
sPLOT2CoCo_CrossTreeConstraint_strategy = st.builds(
    sPLOT2CoCo_CrossTreeConstraint,
    type=
        safe_text
)
sPLOT2CoCo_FeatureAttribute_strategy = st.builds(
    sPLOT2CoCo_FeatureAttribute,
    defaultValue=
        st.integers(),
    nullValue=
        st.integers(),
    maxValue=
        st.integers(),
    minValue=
        st.integers(),
    attributeType=
        safe_text
)
sPLOT2CoCo_ParentChildConstraint_strategy = st.builds(
    sPLOT2CoCo_ParentChildConstraint,
)
TreeConstraint_strategy = st.builds(
    TreeConstraint,
)
sPLOT2CoCo_OrAlternativeTreeConstraint_strategy = st.builds(
    sPLOT2CoCo_OrAlternativeTreeConstraint,
    min=
        st.integers(),
    max=
        st.integers()
)
sPLOT2CoCo_OptionalTreeConstraint_strategy = st.builds(
    sPLOT2CoCo_OptionalTreeConstraint,
)
sPLOT2CoCo_MandatoryTreeConstraint_strategy = st.builds(
    sPLOT2CoCo_MandatoryTreeConstraint,
)
sPLOT2CoCo_TreeConstraint_strategy = st.builds(
    sPLOT2CoCo_TreeConstraint,
)
sPLOT2CoCo_Feature_strategy = st.builds(
    sPLOT2CoCo_Feature,
    name=
        safe_text
)
sPLOT2CoCo_FM_strategy = st.builds(
    sPLOT2CoCo_FM,
)

@given(instance=sPLOT2CoCo_CrossTreeConstraint_strategy)
@settings(max_examples=50)
def test_splot2coco_crosstreeconstraint_instantiation(instance):
    assert isinstance(instance, sPLOT2CoCo_CrossTreeConstraint)



@given(instance=sPLOT2CoCo_CrossTreeConstraint_strategy)
def test_splot2coco_crosstreeconstraint_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=sPLOT2CoCo_FeatureAttribute_strategy)
@settings(max_examples=50)
def test_splot2coco_featureattribute_instantiation(instance):
    assert isinstance(instance, sPLOT2CoCo_FeatureAttribute)



@given(instance=sPLOT2CoCo_FeatureAttribute_strategy)
def test_splot2coco_featureattribute_defaultValue_setter(instance):
    original = instance.defaultValue
    instance.defaultValue = original
    assert instance.defaultValue == original



@given(instance=sPLOT2CoCo_FeatureAttribute_strategy)
def test_splot2coco_featureattribute_nullValue_setter(instance):
    original = instance.nullValue
    instance.nullValue = original
    assert instance.nullValue == original



@given(instance=sPLOT2CoCo_FeatureAttribute_strategy)
def test_splot2coco_featureattribute_maxValue_setter(instance):
    original = instance.maxValue
    instance.maxValue = original
    assert instance.maxValue == original



@given(instance=sPLOT2CoCo_FeatureAttribute_strategy)
def test_splot2coco_featureattribute_minValue_setter(instance):
    original = instance.minValue
    instance.minValue = original
    assert instance.minValue == original



@given(instance=sPLOT2CoCo_FeatureAttribute_strategy)
def test_splot2coco_featureattribute_attributeType_setter(instance):
    original = instance.attributeType
    instance.attributeType = original
    assert instance.attributeType == original

@given(instance=sPLOT2CoCo_ParentChildConstraint_strategy)
@settings(max_examples=50)
def test_splot2coco_parentchildconstraint_instantiation(instance):
    assert isinstance(instance, sPLOT2CoCo_ParentChildConstraint)

@given(instance=TreeConstraint_strategy)
@settings(max_examples=50)
def test_treeconstraint_instantiation(instance):
    assert isinstance(instance, TreeConstraint)

@given(instance=sPLOT2CoCo_OrAlternativeTreeConstraint_strategy)
@settings(max_examples=50)
def test_splot2coco_oralternativetreeconstraint_instantiation(instance):
    assert isinstance(instance, sPLOT2CoCo_OrAlternativeTreeConstraint)



@given(instance=sPLOT2CoCo_OrAlternativeTreeConstraint_strategy)
def test_splot2coco_oralternativetreeconstraint_min_setter(instance):
    original = instance.min
    instance.min = original
    assert instance.min == original



@given(instance=sPLOT2CoCo_OrAlternativeTreeConstraint_strategy)
def test_splot2coco_oralternativetreeconstraint_max_setter(instance):
    original = instance.max
    instance.max = original
    assert instance.max == original

@given(instance=sPLOT2CoCo_OptionalTreeConstraint_strategy)
@settings(max_examples=50)
def test_splot2coco_optionaltreeconstraint_instantiation(instance):
    assert isinstance(instance, sPLOT2CoCo_OptionalTreeConstraint)

@given(instance=sPLOT2CoCo_MandatoryTreeConstraint_strategy)
@settings(max_examples=50)
def test_splot2coco_mandatorytreeconstraint_instantiation(instance):
    assert isinstance(instance, sPLOT2CoCo_MandatoryTreeConstraint)

@given(instance=sPLOT2CoCo_TreeConstraint_strategy)
@settings(max_examples=50)
def test_splot2coco_treeconstraint_instantiation(instance):
    assert isinstance(instance, sPLOT2CoCo_TreeConstraint)

@given(instance=sPLOT2CoCo_Feature_strategy)
@settings(max_examples=50)
def test_splot2coco_feature_instantiation(instance):
    assert isinstance(instance, sPLOT2CoCo_Feature)



@given(instance=sPLOT2CoCo_Feature_strategy)
def test_splot2coco_feature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sPLOT2CoCo_FM_strategy)
@settings(max_examples=50)
def test_splot2coco_fm_instantiation(instance):
    assert isinstance(instance, sPLOT2CoCo_FM)
