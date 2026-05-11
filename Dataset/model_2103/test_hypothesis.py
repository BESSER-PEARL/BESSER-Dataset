import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    GalileoNodeType,
    dft::Observer,
    dft::Parametrized,
    dft::Named,
    dft::GalileoNodeType,
    dft::GalileoFaultTreeNode,
    dft::GalileoDft,
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



def test_dft::observer_is_not_abstract():
    assert not inspect.isabstract(dft::Observer)


def test_dft::observer_constructor_exists():
    assert callable(dft::Observer.__init__)


def test_dft::observer_constructor_args():
    sig = inspect.signature(dft::Observer.__init__)
    params = list(sig.parameters.keys())
    assert "observationRate" in params, "Missing parameter 'observationRate'"

def test_dft::observer_has_observationRate():
    assert hasattr(dft::Observer, "observationRate")
    descriptor = None
    for klass in dft::Observer.__mro__:
        if "observationRate" in klass.__dict__:
            descriptor = klass.__dict__["observationRate"]
            break
    assert isinstance(descriptor, property)



def test_dft::parametrized_is_not_abstract():
    assert not inspect.isabstract(dft::Parametrized)


def test_dft::parametrized_constructor_exists():
    assert callable(dft::Parametrized.__init__)


def test_dft::parametrized_constructor_args():
    sig = inspect.signature(dft::Parametrized.__init__)
    params = list(sig.parameters.keys())
    assert "parameter" in params, "Missing parameter 'parameter'"
    assert "typeName" in params, "Missing parameter 'typeName'"

def test_dft::parametrized_has_parameter():
    assert hasattr(dft::Parametrized, "parameter")
    descriptor = None
    for klass in dft::Parametrized.__mro__:
        if "parameter" in klass.__dict__:
            descriptor = klass.__dict__["parameter"]
            break
    assert isinstance(descriptor, property)

def test_dft::parametrized_has_typeName():
    assert hasattr(dft::Parametrized, "typeName")
    descriptor = None
    for klass in dft::Parametrized.__mro__:
        if "typeName" in klass.__dict__:
            descriptor = klass.__dict__["typeName"]
            break
    assert isinstance(descriptor, property)



def test_dft::named_is_not_abstract():
    assert not inspect.isabstract(dft::Named)


def test_dft::named_constructor_exists():
    assert callable(dft::Named.__init__)


def test_dft::named_constructor_args():
    sig = inspect.signature(dft::Named.__init__)
    params = list(sig.parameters.keys())
    assert "typeName" in params, "Missing parameter 'typeName'"

def test_dft::named_has_typeName():
    assert hasattr(dft::Named, "typeName")
    descriptor = None
    for klass in dft::Named.__mro__:
        if "typeName" in klass.__dict__:
            descriptor = klass.__dict__["typeName"]
            break
    assert isinstance(descriptor, property)



def test_dft::galileonodetype_is_not_abstract():
    assert not inspect.isabstract(dft::GalileoNodeType)


def test_dft::galileonodetype_constructor_exists():
    assert callable(dft::GalileoNodeType.__init__)


def test_dft::galileonodetype_constructor_args():
    sig = inspect.signature(dft::GalileoNodeType.__init__)
    params = list(sig.parameters.keys())



def test_dft::galileofaulttreenode_is_not_abstract():
    assert not inspect.isabstract(dft::GalileoFaultTreeNode)


def test_dft::galileofaulttreenode_constructor_exists():
    assert callable(dft::GalileoFaultTreeNode.__init__)


def test_dft::galileofaulttreenode_constructor_args():
    sig = inspect.signature(dft::GalileoFaultTreeNode.__init__)
    params = list(sig.parameters.keys())
    assert "lambda_" in params, "Missing parameter 'lambda_'"
    assert "repair" in params, "Missing parameter 'repair'"
    assert "dorm" in params, "Missing parameter 'dorm'"
    assert "name" in params, "Missing parameter 'name'"

def test_dft::galileofaulttreenode_has_lambda_():
    assert hasattr(dft::GalileoFaultTreeNode, "lambda_")
    descriptor = None
    for klass in dft::GalileoFaultTreeNode.__mro__:
        if "lambda_" in klass.__dict__:
            descriptor = klass.__dict__["lambda_"]
            break
    assert isinstance(descriptor, property)

def test_dft::galileofaulttreenode_has_repair():
    assert hasattr(dft::GalileoFaultTreeNode, "repair")
    descriptor = None
    for klass in dft::GalileoFaultTreeNode.__mro__:
        if "repair" in klass.__dict__:
            descriptor = klass.__dict__["repair"]
            break
    assert isinstance(descriptor, property)

def test_dft::galileofaulttreenode_has_dorm():
    assert hasattr(dft::GalileoFaultTreeNode, "dorm")
    descriptor = None
    for klass in dft::GalileoFaultTreeNode.__mro__:
        if "dorm" in klass.__dict__:
            descriptor = klass.__dict__["dorm"]
            break
    assert isinstance(descriptor, property)

def test_dft::galileofaulttreenode_has_name():
    assert hasattr(dft::GalileoFaultTreeNode, "name")
    descriptor = None
    for klass in dft::GalileoFaultTreeNode.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dft::galileodft_is_not_abstract():
    assert not inspect.isabstract(dft::GalileoDft)


def test_dft::galileodft_constructor_exists():
    assert callable(dft::GalileoDft.__init__)


def test_dft::galileodft_constructor_args():
    sig = inspect.signature(dft::GalileoDft.__init__)
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
dft::Observer_strategy = st.builds(
    dft::Observer,
    observationRate=
        safe_text
)
dft::Parametrized_strategy = st.builds(
    dft::Parametrized,
    parameter=
        safe_text,
    typeName=
        safe_text
)
dft::Named_strategy = st.builds(
    dft::Named,
    typeName=
        safe_text
)
dft::GalileoNodeType_strategy = st.builds(
    dft::GalileoNodeType,
)
dft::GalileoFaultTreeNode_strategy = st.builds(
    dft::GalileoFaultTreeNode,
    lambda_=
        safe_text,
    repair=
        safe_text,
    dorm=
        safe_text,
    name=
        safe_text
)
dft::GalileoDft_strategy = st.builds(
    dft::GalileoDft,
)

@given(instance=GalileoNodeType_strategy)
@settings(max_examples=50)
def test_galileonodetype_instantiation(instance):
    assert isinstance(instance, GalileoNodeType)

@given(instance=dft::Observer_strategy)
@settings(max_examples=50)
def test_dft::observer_instantiation(instance):
    assert isinstance(instance, dft::Observer)

@given(instance=dft::Observer_strategy)
def test_dft::observer_observationRate_type(instance):
    assert isinstance(instance.observationRate, str)


@given(instance=dft::Observer_strategy)
def test_dft::observer_observationRate_setter(instance):
    original = instance.observationRate
    instance.observationRate = original
    assert instance.observationRate == original

@given(instance=dft::Parametrized_strategy)
@settings(max_examples=50)
def test_dft::parametrized_instantiation(instance):
    assert isinstance(instance, dft::Parametrized)

@given(instance=dft::Parametrized_strategy)
def test_dft::parametrized_parameter_type(instance):
    assert isinstance(instance.parameter, str)


@given(instance=dft::Parametrized_strategy)
def test_dft::parametrized_parameter_setter(instance):
    original = instance.parameter
    instance.parameter = original
    assert instance.parameter == original

@given(instance=dft::Parametrized_strategy)
def test_dft::parametrized_typeName_type(instance):
    assert isinstance(instance.typeName, str)


@given(instance=dft::Parametrized_strategy)
def test_dft::parametrized_typeName_setter(instance):
    original = instance.typeName
    instance.typeName = original
    assert instance.typeName == original

@given(instance=dft::Named_strategy)
@settings(max_examples=50)
def test_dft::named_instantiation(instance):
    assert isinstance(instance, dft::Named)

@given(instance=dft::Named_strategy)
def test_dft::named_typeName_type(instance):
    assert isinstance(instance.typeName, str)


@given(instance=dft::Named_strategy)
def test_dft::named_typeName_setter(instance):
    original = instance.typeName
    instance.typeName = original
    assert instance.typeName == original

@given(instance=dft::GalileoNodeType_strategy)
@settings(max_examples=50)
def test_dft::galileonodetype_instantiation(instance):
    assert isinstance(instance, dft::GalileoNodeType)

@given(instance=dft::GalileoFaultTreeNode_strategy)
@settings(max_examples=50)
def test_dft::galileofaulttreenode_instantiation(instance):
    assert isinstance(instance, dft::GalileoFaultTreeNode)

@given(instance=dft::GalileoFaultTreeNode_strategy)
def test_dft::galileofaulttreenode_lambda__type(instance):
    assert isinstance(instance.lambda_, str)


@given(instance=dft::GalileoFaultTreeNode_strategy)
def test_dft::galileofaulttreenode_lambda__setter(instance):
    original = instance.lambda_
    instance.lambda_ = original
    assert instance.lambda_ == original

@given(instance=dft::GalileoFaultTreeNode_strategy)
def test_dft::galileofaulttreenode_repair_type(instance):
    assert isinstance(instance.repair, str)


@given(instance=dft::GalileoFaultTreeNode_strategy)
def test_dft::galileofaulttreenode_repair_setter(instance):
    original = instance.repair
    instance.repair = original
    assert instance.repair == original

@given(instance=dft::GalileoFaultTreeNode_strategy)
def test_dft::galileofaulttreenode_dorm_type(instance):
    assert isinstance(instance.dorm, str)


@given(instance=dft::GalileoFaultTreeNode_strategy)
def test_dft::galileofaulttreenode_dorm_setter(instance):
    original = instance.dorm
    instance.dorm = original
    assert instance.dorm == original

@given(instance=dft::GalileoFaultTreeNode_strategy)
def test_dft::galileofaulttreenode_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=dft::GalileoFaultTreeNode_strategy)
def test_dft::galileofaulttreenode_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dft::GalileoDft_strategy)
@settings(max_examples=50)
def test_dft::galileodft_instantiation(instance):
    assert isinstance(instance, dft::GalileoDft)
