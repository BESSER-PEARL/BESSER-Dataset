import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    demo1::RatioExpression,
    demo1::Model,
    demo1::TestExpression,
    demo1::EObject,
    demo1::RuleExpression,
    demo1::Rule,
    demo1::Category,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_demo1::ratioexpression_is_not_abstract():
    assert not inspect.isabstract(demo1::RatioExpression)


def test_demo1::ratioexpression_constructor_exists():
    assert callable(demo1::RatioExpression.__init__)


def test_demo1::ratioexpression_constructor_args():
    sig = inspect.signature(demo1::RatioExpression.__init__)
    params = list(sig.parameters.keys())
    assert "ratio" in params, "Missing parameter 'ratio'"

def test_demo1::ratioexpression_has_ratio():
    assert hasattr(demo1::RatioExpression, "ratio")
    descriptor = None
    for klass in demo1::RatioExpression.__mro__:
        if "ratio" in klass.__dict__:
            descriptor = klass.__dict__["ratio"]
            break
    assert isinstance(descriptor, property)



def test_demo1::model_is_not_abstract():
    assert not inspect.isabstract(demo1::Model)


def test_demo1::model_constructor_exists():
    assert callable(demo1::Model.__init__)


def test_demo1::model_constructor_args():
    sig = inspect.signature(demo1::Model.__init__)
    params = list(sig.parameters.keys())



def test_demo1::testexpression_is_not_abstract():
    assert not inspect.isabstract(demo1::TestExpression)


def test_demo1::testexpression_constructor_exists():
    assert callable(demo1::TestExpression.__init__)


def test_demo1::testexpression_constructor_args():
    sig = inspect.signature(demo1::TestExpression.__init__)
    params = list(sig.parameters.keys())



def test_demo1::eobject_is_not_abstract():
    assert not inspect.isabstract(demo1::EObject)


def test_demo1::eobject_constructor_exists():
    assert callable(demo1::EObject.__init__)


def test_demo1::eobject_constructor_args():
    sig = inspect.signature(demo1::EObject.__init__)
    params = list(sig.parameters.keys())



def test_demo1::ruleexpression_is_not_abstract():
    assert not inspect.isabstract(demo1::RuleExpression)


def test_demo1::ruleexpression_constructor_exists():
    assert callable(demo1::RuleExpression.__init__)


def test_demo1::ruleexpression_constructor_args():
    sig = inspect.signature(demo1::RuleExpression.__init__)
    params = list(sig.parameters.keys())



def test_demo1::rule_is_not_abstract():
    assert not inspect.isabstract(demo1::Rule)


def test_demo1::rule_constructor_exists():
    assert callable(demo1::Rule.__init__)


def test_demo1::rule_constructor_args():
    sig = inspect.signature(demo1::Rule.__init__)
    params = list(sig.parameters.keys())



def test_demo1::category_is_not_abstract():
    assert not inspect.isabstract(demo1::Category)


def test_demo1::category_constructor_exists():
    assert callable(demo1::Category.__init__)


def test_demo1::category_constructor_args():
    sig = inspect.signature(demo1::Category.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_demo1::category_has_name():
    assert hasattr(demo1::Category, "name")
    descriptor = None
    for klass in demo1::Category.__mro__:
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
demo1::RatioExpression_strategy = st.builds(
    demo1::RatioExpression,
    ratio=
        st.integers()
)
demo1::Model_strategy = st.builds(
    demo1::Model,
)
demo1::TestExpression_strategy = st.builds(
    demo1::TestExpression,
)
demo1::EObject_strategy = st.builds(
    demo1::EObject,
)
demo1::RuleExpression_strategy = st.builds(
    demo1::RuleExpression,
)
demo1::Rule_strategy = st.builds(
    demo1::Rule,
)
demo1::Category_strategy = st.builds(
    demo1::Category,
    name=
        safe_text
)

@given(instance=demo1::RatioExpression_strategy)
@settings(max_examples=50)
def test_demo1::ratioexpression_instantiation(instance):
    assert isinstance(instance, demo1::RatioExpression)

@given(instance=demo1::RatioExpression_strategy)
def test_demo1::ratioexpression_ratio_type(instance):
    assert isinstance(instance.ratio, int)


@given(instance=demo1::RatioExpression_strategy)
def test_demo1::ratioexpression_ratio_setter(instance):
    original = instance.ratio
    instance.ratio = original
    assert instance.ratio == original

@given(instance=demo1::Model_strategy)
@settings(max_examples=50)
def test_demo1::model_instantiation(instance):
    assert isinstance(instance, demo1::Model)

@given(instance=demo1::TestExpression_strategy)
@settings(max_examples=50)
def test_demo1::testexpression_instantiation(instance):
    assert isinstance(instance, demo1::TestExpression)

@given(instance=demo1::EObject_strategy)
@settings(max_examples=50)
def test_demo1::eobject_instantiation(instance):
    assert isinstance(instance, demo1::EObject)

@given(instance=demo1::RuleExpression_strategy)
@settings(max_examples=50)
def test_demo1::ruleexpression_instantiation(instance):
    assert isinstance(instance, demo1::RuleExpression)

@given(instance=demo1::Rule_strategy)
@settings(max_examples=50)
def test_demo1::rule_instantiation(instance):
    assert isinstance(instance, demo1::Rule)

@given(instance=demo1::Category_strategy)
@settings(max_examples=50)
def test_demo1::category_instantiation(instance):
    assert isinstance(instance, demo1::Category)

@given(instance=demo1::Category_strategy)
def test_demo1::category_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=demo1::Category_strategy)
def test_demo1::category_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
