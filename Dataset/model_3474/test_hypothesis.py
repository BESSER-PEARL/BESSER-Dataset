import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    TreeConstraint,
    myDsl_OrAlternativeTreeConstraint,
    myDsl_OptionalTreeConstraint,
    myDsl_MandatoryTreeConstraint,
    myDsl_TreeConstraint,
    myDsl_FM,
    myDsl_CrossTreeConstraint,
    myDsl_FeatureAttribute,
    myDsl_ParentChildConstraint,
    myDsl_Feature,
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



def test_mydsl_oralternativetreeconstraint_is_not_abstract():
    assert not inspect.isabstract(myDsl_OrAlternativeTreeConstraint)


def test_mydsl_oralternativetreeconstraint_constructor_exists():
    assert callable(myDsl_OrAlternativeTreeConstraint.__init__)


def test_mydsl_oralternativetreeconstraint_constructor_args():
    sig = inspect.signature(myDsl_OrAlternativeTreeConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "max" in params, "Missing parameter 'max'"
    assert "min" in params, "Missing parameter 'min'"

def test_mydsl_oralternativetreeconstraint_has_max():
    assert hasattr(myDsl_OrAlternativeTreeConstraint, "max")
    descriptor = None
    for klass in myDsl_OrAlternativeTreeConstraint.__mro__:
        if "max" in klass.__dict__:
            descriptor = klass.__dict__["max"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_oralternativetreeconstraint_has_min():
    assert hasattr(myDsl_OrAlternativeTreeConstraint, "min")
    descriptor = None
    for klass in myDsl_OrAlternativeTreeConstraint.__mro__:
        if "min" in klass.__dict__:
            descriptor = klass.__dict__["min"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_optionaltreeconstraint_is_not_abstract():
    assert not inspect.isabstract(myDsl_OptionalTreeConstraint)


def test_mydsl_optionaltreeconstraint_constructor_exists():
    assert callable(myDsl_OptionalTreeConstraint.__init__)


def test_mydsl_optionaltreeconstraint_constructor_args():
    sig = inspect.signature(myDsl_OptionalTreeConstraint.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_mandatorytreeconstraint_is_not_abstract():
    assert not inspect.isabstract(myDsl_MandatoryTreeConstraint)


def test_mydsl_mandatorytreeconstraint_constructor_exists():
    assert callable(myDsl_MandatoryTreeConstraint.__init__)


def test_mydsl_mandatorytreeconstraint_constructor_args():
    sig = inspect.signature(myDsl_MandatoryTreeConstraint.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_treeconstraint_is_not_abstract():
    assert not inspect.isabstract(myDsl_TreeConstraint)


def test_mydsl_treeconstraint_constructor_exists():
    assert callable(myDsl_TreeConstraint.__init__)


def test_mydsl_treeconstraint_constructor_args():
    sig = inspect.signature(myDsl_TreeConstraint.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_fm_is_not_abstract():
    assert not inspect.isabstract(myDsl_FM)


def test_mydsl_fm_constructor_exists():
    assert callable(myDsl_FM.__init__)


def test_mydsl_fm_constructor_args():
    sig = inspect.signature(myDsl_FM.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_crosstreeconstraint_is_not_abstract():
    assert not inspect.isabstract(myDsl_CrossTreeConstraint)


def test_mydsl_crosstreeconstraint_constructor_exists():
    assert callable(myDsl_CrossTreeConstraint.__init__)


def test_mydsl_crosstreeconstraint_constructor_args():
    sig = inspect.signature(myDsl_CrossTreeConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_mydsl_crosstreeconstraint_has_type():
    assert hasattr(myDsl_CrossTreeConstraint, "type")
    descriptor = None
    for klass in myDsl_CrossTreeConstraint.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_featureattribute_is_not_abstract():
    assert not inspect.isabstract(myDsl_FeatureAttribute)


def test_mydsl_featureattribute_constructor_exists():
    assert callable(myDsl_FeatureAttribute.__init__)


def test_mydsl_featureattribute_constructor_args():
    sig = inspect.signature(myDsl_FeatureAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "defaultValue" in params, "Missing parameter 'defaultValue'"
    assert "minValue" in params, "Missing parameter 'minValue'"
    assert "maxValue" in params, "Missing parameter 'maxValue'"
    assert "nullValue" in params, "Missing parameter 'nullValue'"
    assert "attributeType" in params, "Missing parameter 'attributeType'"

def test_mydsl_featureattribute_has_defaultValue():
    assert hasattr(myDsl_FeatureAttribute, "defaultValue")
    descriptor = None
    for klass in myDsl_FeatureAttribute.__mro__:
        if "defaultValue" in klass.__dict__:
            descriptor = klass.__dict__["defaultValue"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_featureattribute_has_minValue():
    assert hasattr(myDsl_FeatureAttribute, "minValue")
    descriptor = None
    for klass in myDsl_FeatureAttribute.__mro__:
        if "minValue" in klass.__dict__:
            descriptor = klass.__dict__["minValue"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_featureattribute_has_maxValue():
    assert hasattr(myDsl_FeatureAttribute, "maxValue")
    descriptor = None
    for klass in myDsl_FeatureAttribute.__mro__:
        if "maxValue" in klass.__dict__:
            descriptor = klass.__dict__["maxValue"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_featureattribute_has_nullValue():
    assert hasattr(myDsl_FeatureAttribute, "nullValue")
    descriptor = None
    for klass in myDsl_FeatureAttribute.__mro__:
        if "nullValue" in klass.__dict__:
            descriptor = klass.__dict__["nullValue"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_featureattribute_has_attributeType():
    assert hasattr(myDsl_FeatureAttribute, "attributeType")
    descriptor = None
    for klass in myDsl_FeatureAttribute.__mro__:
        if "attributeType" in klass.__dict__:
            descriptor = klass.__dict__["attributeType"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_parentchildconstraint_is_not_abstract():
    assert not inspect.isabstract(myDsl_ParentChildConstraint)


def test_mydsl_parentchildconstraint_constructor_exists():
    assert callable(myDsl_ParentChildConstraint.__init__)


def test_mydsl_parentchildconstraint_constructor_args():
    sig = inspect.signature(myDsl_ParentChildConstraint.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_feature_is_not_abstract():
    assert not inspect.isabstract(myDsl_Feature)


def test_mydsl_feature_constructor_exists():
    assert callable(myDsl_Feature.__init__)


def test_mydsl_feature_constructor_args():
    sig = inspect.signature(myDsl_Feature.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl_feature_has_name():
    assert hasattr(myDsl_Feature, "name")
    descriptor = None
    for klass in myDsl_Feature.__mro__:
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
myDsl_OrAlternativeTreeConstraint_strategy = st.builds(
    myDsl_OrAlternativeTreeConstraint,
    max=
        st.integers(),
    min=
        st.integers()
)
myDsl_OptionalTreeConstraint_strategy = st.builds(
    myDsl_OptionalTreeConstraint,
)
myDsl_MandatoryTreeConstraint_strategy = st.builds(
    myDsl_MandatoryTreeConstraint,
)
myDsl_TreeConstraint_strategy = st.builds(
    myDsl_TreeConstraint,
)
myDsl_FM_strategy = st.builds(
    myDsl_FM,
)
myDsl_CrossTreeConstraint_strategy = st.builds(
    myDsl_CrossTreeConstraint,
    type=
        safe_text
)
myDsl_FeatureAttribute_strategy = st.builds(
    myDsl_FeatureAttribute,
    defaultValue=
        st.integers(),
    minValue=
        st.integers(),
    maxValue=
        st.integers(),
    nullValue=
        st.integers(),
    attributeType=
        safe_text
)
myDsl_ParentChildConstraint_strategy = st.builds(
    myDsl_ParentChildConstraint,
)
myDsl_Feature_strategy = st.builds(
    myDsl_Feature,
    name=
        safe_text
)

@given(instance=TreeConstraint_strategy)
@settings(max_examples=50)
def test_treeconstraint_instantiation(instance):
    assert isinstance(instance, TreeConstraint)

@given(instance=myDsl_OrAlternativeTreeConstraint_strategy)
@settings(max_examples=50)
def test_mydsl_oralternativetreeconstraint_instantiation(instance):
    assert isinstance(instance, myDsl_OrAlternativeTreeConstraint)



@given(instance=myDsl_OrAlternativeTreeConstraint_strategy)
def test_mydsl_oralternativetreeconstraint_max_setter(instance):
    original = instance.max
    instance.max = original
    assert instance.max == original



@given(instance=myDsl_OrAlternativeTreeConstraint_strategy)
def test_mydsl_oralternativetreeconstraint_min_setter(instance):
    original = instance.min
    instance.min = original
    assert instance.min == original

@given(instance=myDsl_OptionalTreeConstraint_strategy)
@settings(max_examples=50)
def test_mydsl_optionaltreeconstraint_instantiation(instance):
    assert isinstance(instance, myDsl_OptionalTreeConstraint)

@given(instance=myDsl_MandatoryTreeConstraint_strategy)
@settings(max_examples=50)
def test_mydsl_mandatorytreeconstraint_instantiation(instance):
    assert isinstance(instance, myDsl_MandatoryTreeConstraint)

@given(instance=myDsl_TreeConstraint_strategy)
@settings(max_examples=50)
def test_mydsl_treeconstraint_instantiation(instance):
    assert isinstance(instance, myDsl_TreeConstraint)

@given(instance=myDsl_FM_strategy)
@settings(max_examples=50)
def test_mydsl_fm_instantiation(instance):
    assert isinstance(instance, myDsl_FM)

@given(instance=myDsl_CrossTreeConstraint_strategy)
@settings(max_examples=50)
def test_mydsl_crosstreeconstraint_instantiation(instance):
    assert isinstance(instance, myDsl_CrossTreeConstraint)



@given(instance=myDsl_CrossTreeConstraint_strategy)
def test_mydsl_crosstreeconstraint_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=myDsl_FeatureAttribute_strategy)
@settings(max_examples=50)
def test_mydsl_featureattribute_instantiation(instance):
    assert isinstance(instance, myDsl_FeatureAttribute)



@given(instance=myDsl_FeatureAttribute_strategy)
def test_mydsl_featureattribute_defaultValue_setter(instance):
    original = instance.defaultValue
    instance.defaultValue = original
    assert instance.defaultValue == original



@given(instance=myDsl_FeatureAttribute_strategy)
def test_mydsl_featureattribute_minValue_setter(instance):
    original = instance.minValue
    instance.minValue = original
    assert instance.minValue == original



@given(instance=myDsl_FeatureAttribute_strategy)
def test_mydsl_featureattribute_maxValue_setter(instance):
    original = instance.maxValue
    instance.maxValue = original
    assert instance.maxValue == original



@given(instance=myDsl_FeatureAttribute_strategy)
def test_mydsl_featureattribute_nullValue_setter(instance):
    original = instance.nullValue
    instance.nullValue = original
    assert instance.nullValue == original



@given(instance=myDsl_FeatureAttribute_strategy)
def test_mydsl_featureattribute_attributeType_setter(instance):
    original = instance.attributeType
    instance.attributeType = original
    assert instance.attributeType == original

@given(instance=myDsl_ParentChildConstraint_strategy)
@settings(max_examples=50)
def test_mydsl_parentchildconstraint_instantiation(instance):
    assert isinstance(instance, myDsl_ParentChildConstraint)

@given(instance=myDsl_Feature_strategy)
@settings(max_examples=50)
def test_mydsl_feature_instantiation(instance):
    assert isinstance(instance, myDsl_Feature)



@given(instance=myDsl_Feature_strategy)
def test_mydsl_feature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
