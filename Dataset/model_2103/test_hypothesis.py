import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    GalileoNodeType,
    dft_Observer,
    dft_Parametrized,
    dft_Named,
    dft_GalileoNodeType,
    dft_GalileoFaultTreeNode,
    dft_GalileoDft,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_galileonodetype_is_not_abstract():
    assert not inspect.isabstract(GalileoNodeType)


def test_galileonodetype_constructor_exists():
    assert callable(GalileoNodeType.__init__)


def test_galileonodetype_constructor_args():
    sig = inspect.signature(GalileoNodeType.__init__)
    params = list(sig.parameters.keys())



def test_dft_observer_is_not_abstract():
    assert not inspect.isabstract(dft_Observer)


def test_dft_observer_constructor_exists():
    assert callable(dft_Observer.__init__)


def test_dft_observer_constructor_args():
    sig = inspect.signature(dft_Observer.__init__)
    params = list(sig.parameters.keys())
    assert "observationRate" in params, "Missing parameter 'observationRate'"

def test_dft_observer_has_observationRate():
    assert hasattr(dft_Observer, "observationRate")
    descriptor = None
    for klass in dft_Observer.__mro__:
        if "observationRate" in klass.__dict__:
            descriptor = klass.__dict__["observationRate"]
            break
    assert isinstance(descriptor, property)



def test_dft_parametrized_is_not_abstract():
    assert not inspect.isabstract(dft_Parametrized)


def test_dft_parametrized_constructor_exists():
    assert callable(dft_Parametrized.__init__)


def test_dft_parametrized_constructor_args():
    sig = inspect.signature(dft_Parametrized.__init__)
    params = list(sig.parameters.keys())
    assert "typeName" in params, "Missing parameter 'typeName'"
    assert "parameter" in params, "Missing parameter 'parameter'"

def test_dft_parametrized_has_typeName():
    assert hasattr(dft_Parametrized, "typeName")
    descriptor = None
    for klass in dft_Parametrized.__mro__:
        if "typeName" in klass.__dict__:
            descriptor = klass.__dict__["typeName"]
            break
    assert isinstance(descriptor, property)

def test_dft_parametrized_has_parameter():
    assert hasattr(dft_Parametrized, "parameter")
    descriptor = None
    for klass in dft_Parametrized.__mro__:
        if "parameter" in klass.__dict__:
            descriptor = klass.__dict__["parameter"]
            break
    assert isinstance(descriptor, property)



def test_dft_named_is_not_abstract():
    assert not inspect.isabstract(dft_Named)


def test_dft_named_constructor_exists():
    assert callable(dft_Named.__init__)


def test_dft_named_constructor_args():
    sig = inspect.signature(dft_Named.__init__)
    params = list(sig.parameters.keys())
    assert "typeName" in params, "Missing parameter 'typeName'"

def test_dft_named_has_typeName():
    assert hasattr(dft_Named, "typeName")
    descriptor = None
    for klass in dft_Named.__mro__:
        if "typeName" in klass.__dict__:
            descriptor = klass.__dict__["typeName"]
            break
    assert isinstance(descriptor, property)



def test_dft_galileonodetype_is_not_abstract():
    assert not inspect.isabstract(dft_GalileoNodeType)


def test_dft_galileonodetype_constructor_exists():
    assert callable(dft_GalileoNodeType.__init__)


def test_dft_galileonodetype_constructor_args():
    sig = inspect.signature(dft_GalileoNodeType.__init__)
    params = list(sig.parameters.keys())



def test_dft_galileofaulttreenode_is_not_abstract():
    assert not inspect.isabstract(dft_GalileoFaultTreeNode)


def test_dft_galileofaulttreenode_constructor_exists():
    assert callable(dft_GalileoFaultTreeNode.__init__)


def test_dft_galileofaulttreenode_constructor_args():
    sig = inspect.signature(dft_GalileoFaultTreeNode.__init__)
    params = list(sig.parameters.keys())
    assert "lambda_" in params, "Missing parameter 'lambda_'"
    assert "dorm" in params, "Missing parameter 'dorm'"
    assert "name" in params, "Missing parameter 'name'"
    assert "repair" in params, "Missing parameter 'repair'"

def test_dft_galileofaulttreenode_has_lambda_():
    assert hasattr(dft_GalileoFaultTreeNode, "lambda_")
    descriptor = None
    for klass in dft_GalileoFaultTreeNode.__mro__:
        if "lambda_" in klass.__dict__:
            descriptor = klass.__dict__["lambda_"]
            break
    assert isinstance(descriptor, property)

def test_dft_galileofaulttreenode_has_dorm():
    assert hasattr(dft_GalileoFaultTreeNode, "dorm")
    descriptor = None
    for klass in dft_GalileoFaultTreeNode.__mro__:
        if "dorm" in klass.__dict__:
            descriptor = klass.__dict__["dorm"]
            break
    assert isinstance(descriptor, property)

def test_dft_galileofaulttreenode_has_name():
    assert hasattr(dft_GalileoFaultTreeNode, "name")
    descriptor = None
    for klass in dft_GalileoFaultTreeNode.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_dft_galileofaulttreenode_has_repair():
    assert hasattr(dft_GalileoFaultTreeNode, "repair")
    descriptor = None
    for klass in dft_GalileoFaultTreeNode.__mro__:
        if "repair" in klass.__dict__:
            descriptor = klass.__dict__["repair"]
            break
    assert isinstance(descriptor, property)



def test_dft_galileodft_is_not_abstract():
    assert not inspect.isabstract(dft_GalileoDft)


def test_dft_galileodft_constructor_exists():
    assert callable(dft_GalileoDft.__init__)


def test_dft_galileodft_constructor_args():
    sig = inspect.signature(dft_GalileoDft.__init__)
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
GalileoNodeType_strategy = st.builds(
    GalileoNodeType,
)
dft_Observer_strategy = st.builds(
    dft_Observer,
    observationRate=
        safe_text
)
dft_Parametrized_strategy = st.builds(
    dft_Parametrized,
    typeName=
        safe_text,
    parameter=
        safe_text
)
dft_Named_strategy = st.builds(
    dft_Named,
    typeName=
        safe_text
)
dft_GalileoNodeType_strategy = st.builds(
    dft_GalileoNodeType,
)
dft_GalileoFaultTreeNode_strategy = st.builds(
    dft_GalileoFaultTreeNode,
    lambda_=
        safe_text,
    dorm=
        safe_text,
    name=
        safe_text,
    repair=
        safe_text
)
dft_GalileoDft_strategy = st.builds(
    dft_GalileoDft,
)

@given(instance=GalileoNodeType_strategy)
@settings(max_examples=50)
def test_galileonodetype_instantiation(instance):
    assert isinstance(instance, GalileoNodeType)

@given(instance=dft_Observer_strategy)
@settings(max_examples=50)
def test_dft_observer_instantiation(instance):
    assert isinstance(instance, dft_Observer)



@given(instance=dft_Observer_strategy)
def test_dft_observer_observationRate_setter(instance):
    original = instance.observationRate
    instance.observationRate = original
    assert instance.observationRate == original

@given(instance=dft_Parametrized_strategy)
@settings(max_examples=50)
def test_dft_parametrized_instantiation(instance):
    assert isinstance(instance, dft_Parametrized)



@given(instance=dft_Parametrized_strategy)
def test_dft_parametrized_typeName_setter(instance):
    original = instance.typeName
    instance.typeName = original
    assert instance.typeName == original



@given(instance=dft_Parametrized_strategy)
def test_dft_parametrized_parameter_setter(instance):
    original = instance.parameter
    instance.parameter = original
    assert instance.parameter == original

@given(instance=dft_Named_strategy)
@settings(max_examples=50)
def test_dft_named_instantiation(instance):
    assert isinstance(instance, dft_Named)



@given(instance=dft_Named_strategy)
def test_dft_named_typeName_setter(instance):
    original = instance.typeName
    instance.typeName = original
    assert instance.typeName == original

@given(instance=dft_GalileoNodeType_strategy)
@settings(max_examples=50)
def test_dft_galileonodetype_instantiation(instance):
    assert isinstance(instance, dft_GalileoNodeType)

@given(instance=dft_GalileoFaultTreeNode_strategy)
@settings(max_examples=50)
def test_dft_galileofaulttreenode_instantiation(instance):
    assert isinstance(instance, dft_GalileoFaultTreeNode)



@given(instance=dft_GalileoFaultTreeNode_strategy)
def test_dft_galileofaulttreenode_lambda__setter(instance):
    original = instance.lambda_
    instance.lambda_ = original
    assert instance.lambda_ == original



@given(instance=dft_GalileoFaultTreeNode_strategy)
def test_dft_galileofaulttreenode_dorm_setter(instance):
    original = instance.dorm
    instance.dorm = original
    assert instance.dorm == original



@given(instance=dft_GalileoFaultTreeNode_strategy)
def test_dft_galileofaulttreenode_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=dft_GalileoFaultTreeNode_strategy)
def test_dft_galileofaulttreenode_repair_setter(instance):
    original = instance.repair
    instance.repair = original
    assert instance.repair == original

@given(instance=dft_GalileoDft_strategy)
@settings(max_examples=50)
def test_dft_galileodft_instantiation(instance):
    assert isinstance(instance, dft_GalileoDft)
