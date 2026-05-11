import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    transformationtrace::ActivationTrace,
    transformationtrace::TransformationTrace,
    transformationtrace::RuleParameterTrace,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_transformationtrace::activationtrace_is_not_abstract():
    assert not inspect.isabstract(transformationtrace::ActivationTrace)


def test_transformationtrace::activationtrace_constructor_exists():
    assert callable(transformationtrace::ActivationTrace.__init__)


def test_transformationtrace::activationtrace_constructor_args():
    sig = inspect.signature(transformationtrace::ActivationTrace.__init__)
    params = list(sig.parameters.keys())
    assert "ruleName" in params, "Missing parameter 'ruleName'"

def test_transformationtrace::activationtrace_has_ruleName():
    assert hasattr(transformationtrace::ActivationTrace, "ruleName")
    descriptor = None
    for klass in transformationtrace::ActivationTrace.__mro__:
        if "ruleName" in klass.__dict__:
            descriptor = klass.__dict__["ruleName"]
            break
    assert isinstance(descriptor, property)



def test_transformationtrace::transformationtrace_is_not_abstract():
    assert not inspect.isabstract(transformationtrace::TransformationTrace)


def test_transformationtrace::transformationtrace_constructor_exists():
    assert callable(transformationtrace::TransformationTrace.__init__)


def test_transformationtrace::transformationtrace_constructor_args():
    sig = inspect.signature(transformationtrace::TransformationTrace.__init__)
    params = list(sig.parameters.keys())



def test_transformationtrace::ruleparametertrace_is_not_abstract():
    assert not inspect.isabstract(transformationtrace::RuleParameterTrace)


def test_transformationtrace::ruleparametertrace_constructor_exists():
    assert callable(transformationtrace::RuleParameterTrace.__init__)


def test_transformationtrace::ruleparametertrace_constructor_args():
    sig = inspect.signature(transformationtrace::RuleParameterTrace.__init__)
    params = list(sig.parameters.keys())
    assert "objectId" in params, "Missing parameter 'objectId'"
    assert "parameterName" in params, "Missing parameter 'parameterName'"

def test_transformationtrace::ruleparametertrace_has_objectId():
    assert hasattr(transformationtrace::RuleParameterTrace, "objectId")
    descriptor = None
    for klass in transformationtrace::RuleParameterTrace.__mro__:
        if "objectId" in klass.__dict__:
            descriptor = klass.__dict__["objectId"]
            break
    assert isinstance(descriptor, property)

def test_transformationtrace::ruleparametertrace_has_parameterName():
    assert hasattr(transformationtrace::RuleParameterTrace, "parameterName")
    descriptor = None
    for klass in transformationtrace::RuleParameterTrace.__mro__:
        if "parameterName" in klass.__dict__:
            descriptor = klass.__dict__["parameterName"]
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
transformationtrace::ActivationTrace_strategy = st.builds(
    transformationtrace::ActivationTrace,
    ruleName=
        safe_text
)
transformationtrace::TransformationTrace_strategy = st.builds(
    transformationtrace::TransformationTrace,
)
transformationtrace::RuleParameterTrace_strategy = st.builds(
    transformationtrace::RuleParameterTrace,
    objectId=
        safe_text,
    parameterName=
        safe_text
)

@given(instance=transformationtrace::ActivationTrace_strategy)
@settings(max_examples=50)
def test_transformationtrace::activationtrace_instantiation(instance):
    assert isinstance(instance, transformationtrace::ActivationTrace)

@given(instance=transformationtrace::ActivationTrace_strategy)
def test_transformationtrace::activationtrace_ruleName_type(instance):
    assert isinstance(instance.ruleName, str)


@given(instance=transformationtrace::ActivationTrace_strategy)
def test_transformationtrace::activationtrace_ruleName_setter(instance):
    original = instance.ruleName
    instance.ruleName = original
    assert instance.ruleName == original

@given(instance=transformationtrace::TransformationTrace_strategy)
@settings(max_examples=50)
def test_transformationtrace::transformationtrace_instantiation(instance):
    assert isinstance(instance, transformationtrace::TransformationTrace)

@given(instance=transformationtrace::RuleParameterTrace_strategy)
@settings(max_examples=50)
def test_transformationtrace::ruleparametertrace_instantiation(instance):
    assert isinstance(instance, transformationtrace::RuleParameterTrace)

@given(instance=transformationtrace::RuleParameterTrace_strategy)
def test_transformationtrace::ruleparametertrace_objectId_type(instance):
    assert isinstance(instance.objectId, str)


@given(instance=transformationtrace::RuleParameterTrace_strategy)
def test_transformationtrace::ruleparametertrace_objectId_setter(instance):
    original = instance.objectId
    instance.objectId = original
    assert instance.objectId == original

@given(instance=transformationtrace::RuleParameterTrace_strategy)
def test_transformationtrace::ruleparametertrace_parameterName_type(instance):
    assert isinstance(instance.parameterName, str)


@given(instance=transformationtrace::RuleParameterTrace_strategy)
def test_transformationtrace::ruleparametertrace_parameterName_setter(instance):
    original = instance.parameterName
    instance.parameterName = original
    assert instance.parameterName == original
