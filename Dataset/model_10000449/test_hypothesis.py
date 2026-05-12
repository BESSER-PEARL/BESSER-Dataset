import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    UpdateWeight,
    NeuralNetwork,
    Backpropagation,
    Forward,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_updateweight_is_not_abstract():
    assert not inspect.isabstract(UpdateWeight)


def test_updateweight_constructor_exists():
    assert callable(UpdateWeight.__init__)


def test_updateweight_constructor_args():
    sig = inspect.signature(UpdateWeight.__init__)
    params = list(sig.parameters.keys())
    assert "BiasesWeigths" in params, "Missing parameter 'BiasesWeigths'"
    assert "Weights" in params, "Missing parameter 'Weights'"

def test_updateweight_has_BiasesWeigths():
    assert hasattr(UpdateWeight, "BiasesWeigths")
    descriptor = None
    for klass in UpdateWeight.__mro__:
        if "BiasesWeigths" in klass.__dict__:
            descriptor = klass.__dict__["BiasesWeigths"]
            break
    assert isinstance(descriptor, property)

def test_updateweight_has_Weights():
    assert hasattr(UpdateWeight, "Weights")
    descriptor = None
    for klass in UpdateWeight.__mro__:
        if "Weights" in klass.__dict__:
            descriptor = klass.__dict__["Weights"]
            break
    assert isinstance(descriptor, property)



def test_neuralnetwork_is_not_abstract():
    assert not inspect.isabstract(NeuralNetwork)


def test_neuralnetwork_constructor_exists():
    assert callable(NeuralNetwork.__init__)


def test_neuralnetwork_constructor_args():
    sig = inspect.signature(NeuralNetwork.__init__)
    params = list(sig.parameters.keys())



def test_backpropagation_is_not_abstract():
    assert not inspect.isabstract(Backpropagation)


def test_backpropagation_constructor_exists():
    assert callable(Backpropagation.__init__)


def test_backpropagation_constructor_args():
    sig = inspect.signature(Backpropagation.__init__)
    params = list(sig.parameters.keys())
    assert "BiasesWeigths" in params, "Missing parameter 'BiasesWeigths'"
    assert "target" in params, "Missing parameter 'target'"
    assert "output" in params, "Missing parameter 'output'"
    assert "Weigths" in params, "Missing parameter 'Weigths'"

def test_backpropagation_has_BiasesWeigths():
    assert hasattr(Backpropagation, "BiasesWeigths")
    descriptor = None
    for klass in Backpropagation.__mro__:
        if "BiasesWeigths" in klass.__dict__:
            descriptor = klass.__dict__["BiasesWeigths"]
            break
    assert isinstance(descriptor, property)

def test_backpropagation_has_target():
    assert hasattr(Backpropagation, "target")
    descriptor = None
    for klass in Backpropagation.__mro__:
        if "target" in klass.__dict__:
            descriptor = klass.__dict__["target"]
            break
    assert isinstance(descriptor, property)

def test_backpropagation_has_output():
    assert hasattr(Backpropagation, "output")
    descriptor = None
    for klass in Backpropagation.__mro__:
        if "output" in klass.__dict__:
            descriptor = klass.__dict__["output"]
            break
    assert isinstance(descriptor, property)

def test_backpropagation_has_Weigths():
    assert hasattr(Backpropagation, "Weigths")
    descriptor = None
    for klass in Backpropagation.__mro__:
        if "Weigths" in klass.__dict__:
            descriptor = klass.__dict__["Weigths"]
            break
    assert isinstance(descriptor, property)



def test_forward_is_not_abstract():
    assert not inspect.isabstract(Forward)


def test_forward_constructor_exists():
    assert callable(Forward.__init__)


def test_forward_constructor_args():
    sig = inspect.signature(Forward.__init__)
    params = list(sig.parameters.keys())
    assert "Weights" in params, "Missing parameter 'Weights'"
    assert "Input" in params, "Missing parameter 'Input'"
    assert "BiasesWeigths" in params, "Missing parameter 'BiasesWeigths'"

def test_forward_has_Weights():
    assert hasattr(Forward, "Weights")
    descriptor = None
    for klass in Forward.__mro__:
        if "Weights" in klass.__dict__:
            descriptor = klass.__dict__["Weights"]
            break
    assert isinstance(descriptor, property)

def test_forward_has_Input():
    assert hasattr(Forward, "Input")
    descriptor = None
    for klass in Forward.__mro__:
        if "Input" in klass.__dict__:
            descriptor = klass.__dict__["Input"]
            break
    assert isinstance(descriptor, property)

def test_forward_has_BiasesWeigths():
    assert hasattr(Forward, "BiasesWeigths")
    descriptor = None
    for klass in Forward.__mro__:
        if "BiasesWeigths" in klass.__dict__:
            descriptor = klass.__dict__["BiasesWeigths"]
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
UpdateWeight_strategy = st.builds(
    UpdateWeight,
    BiasesWeigths=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    Weights=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
NeuralNetwork_strategy = st.builds(
    NeuralNetwork,
)
Backpropagation_strategy = st.builds(
    Backpropagation,
    BiasesWeigths=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    target=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    output=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    Weigths=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
Forward_strategy = st.builds(
    Forward,
    Weights=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    Input=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    BiasesWeigths=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)

@given(instance=UpdateWeight_strategy)
@settings(max_examples=50)
def test_updateweight_instantiation(instance):
    assert isinstance(instance, UpdateWeight)



@given(instance=UpdateWeight_strategy)
def test_updateweight_BiasesWeigths_setter(instance):
    original = instance.BiasesWeigths
    instance.BiasesWeigths = original
    assert instance.BiasesWeigths == original



@given(instance=UpdateWeight_strategy)
def test_updateweight_Weights_setter(instance):
    original = instance.Weights
    instance.Weights = original
    assert instance.Weights == original

@given(instance=NeuralNetwork_strategy)
@settings(max_examples=50)
def test_neuralnetwork_instantiation(instance):
    assert isinstance(instance, NeuralNetwork)

@given(instance=Backpropagation_strategy)
@settings(max_examples=50)
def test_backpropagation_instantiation(instance):
    assert isinstance(instance, Backpropagation)



@given(instance=Backpropagation_strategy)
def test_backpropagation_BiasesWeigths_setter(instance):
    original = instance.BiasesWeigths
    instance.BiasesWeigths = original
    assert instance.BiasesWeigths == original



@given(instance=Backpropagation_strategy)
def test_backpropagation_target_setter(instance):
    original = instance.target
    instance.target = original
    assert instance.target == original



@given(instance=Backpropagation_strategy)
def test_backpropagation_output_setter(instance):
    original = instance.output
    instance.output = original
    assert instance.output == original



@given(instance=Backpropagation_strategy)
def test_backpropagation_Weigths_setter(instance):
    original = instance.Weigths
    instance.Weigths = original
    assert instance.Weigths == original

@given(instance=Forward_strategy)
@settings(max_examples=50)
def test_forward_instantiation(instance):
    assert isinstance(instance, Forward)



@given(instance=Forward_strategy)
def test_forward_Weights_setter(instance):
    original = instance.Weights
    instance.Weights = original
    assert instance.Weights == original



@given(instance=Forward_strategy)
def test_forward_Input_setter(instance):
    original = instance.Input
    instance.Input = original
    assert instance.Input == original



@given(instance=Forward_strategy)
def test_forward_BiasesWeigths_setter(instance):
    original = instance.BiasesWeigths
    instance.BiasesWeigths = original
    assert instance.BiasesWeigths == original
