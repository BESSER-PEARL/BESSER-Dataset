import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    sample_Then,
    sample_Given,
    sample_When,
    sample_Scenario,
    sample_Story,
    sample_Sentence,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_sample_then_is_not_abstract():
    assert not inspect.isabstract(sample_Then)


def test_sample_then_constructor_exists():
    assert callable(sample_Then.__init__)


def test_sample_then_constructor_args():
    sig = inspect.signature(sample_Then.__init__)
    params = list(sig.parameters.keys())



def test_sample_given_is_not_abstract():
    assert not inspect.isabstract(sample_Given)


def test_sample_given_constructor_exists():
    assert callable(sample_Given.__init__)


def test_sample_given_constructor_args():
    sig = inspect.signature(sample_Given.__init__)
    params = list(sig.parameters.keys())



def test_sample_when_is_not_abstract():
    assert not inspect.isabstract(sample_When)


def test_sample_when_constructor_exists():
    assert callable(sample_When.__init__)


def test_sample_when_constructor_args():
    sig = inspect.signature(sample_When.__init__)
    params = list(sig.parameters.keys())



def test_sample_scenario_is_not_abstract():
    assert not inspect.isabstract(sample_Scenario)


def test_sample_scenario_constructor_exists():
    assert callable(sample_Scenario.__init__)


def test_sample_scenario_constructor_args():
    sig = inspect.signature(sample_Scenario.__init__)
    params = list(sig.parameters.keys())
    assert "Title" in params, "Missing parameter 'Title'"

def test_sample_scenario_has_Title():
    assert hasattr(sample_Scenario, "Title")
    descriptor = None
    for klass in sample_Scenario.__mro__:
        if "Title" in klass.__dict__:
            descriptor = klass.__dict__["Title"]
            break
    assert isinstance(descriptor, property)



def test_sample_story_is_not_abstract():
    assert not inspect.isabstract(sample_Story)


def test_sample_story_constructor_exists():
    assert callable(sample_Story.__init__)


def test_sample_story_constructor_args():
    sig = inspect.signature(sample_Story.__init__)
    params = list(sig.parameters.keys())
    assert "Title" in params, "Missing parameter 'Title'"
    assert "Role" in params, "Missing parameter 'Role'"
    assert "Feature" in params, "Missing parameter 'Feature'"
    assert "Benefit" in params, "Missing parameter 'Benefit'"

def test_sample_story_has_Title():
    assert hasattr(sample_Story, "Title")
    descriptor = None
    for klass in sample_Story.__mro__:
        if "Title" in klass.__dict__:
            descriptor = klass.__dict__["Title"]
            break
    assert isinstance(descriptor, property)

def test_sample_story_has_Role():
    assert hasattr(sample_Story, "Role")
    descriptor = None
    for klass in sample_Story.__mro__:
        if "Role" in klass.__dict__:
            descriptor = klass.__dict__["Role"]
            break
    assert isinstance(descriptor, property)

def test_sample_story_has_Feature():
    assert hasattr(sample_Story, "Feature")
    descriptor = None
    for klass in sample_Story.__mro__:
        if "Feature" in klass.__dict__:
            descriptor = klass.__dict__["Feature"]
            break
    assert isinstance(descriptor, property)

def test_sample_story_has_Benefit():
    assert hasattr(sample_Story, "Benefit")
    descriptor = None
    for klass in sample_Story.__mro__:
        if "Benefit" in klass.__dict__:
            descriptor = klass.__dict__["Benefit"]
            break
    assert isinstance(descriptor, property)



def test_sample_sentence_is_not_abstract():
    assert not inspect.isabstract(sample_Sentence)


def test_sample_sentence_constructor_exists():
    assert callable(sample_Sentence.__init__)


def test_sample_sentence_constructor_args():
    sig = inspect.signature(sample_Sentence.__init__)
    params = list(sig.parameters.keys())
    assert "Text" in params, "Missing parameter 'Text'"

def test_sample_sentence_has_Text():
    assert hasattr(sample_Sentence, "Text")
    descriptor = None
    for klass in sample_Sentence.__mro__:
        if "Text" in klass.__dict__:
            descriptor = klass.__dict__["Text"]
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
sample_Then_strategy = st.builds(
    sample_Then,
)
sample_Given_strategy = st.builds(
    sample_Given,
)
sample_When_strategy = st.builds(
    sample_When,
)
sample_Scenario_strategy = st.builds(
    sample_Scenario,
    Title=
        safe_text
)
sample_Story_strategy = st.builds(
    sample_Story,
    Title=
        safe_text,
    Role=
        safe_text,
    Feature=
        safe_text,
    Benefit=
        safe_text
)
sample_Sentence_strategy = st.builds(
    sample_Sentence,
    Text=
        safe_text
)

@given(instance=sample_Then_strategy)
@settings(max_examples=50)
def test_sample_then_instantiation(instance):
    assert isinstance(instance, sample_Then)

@given(instance=sample_Given_strategy)
@settings(max_examples=50)
def test_sample_given_instantiation(instance):
    assert isinstance(instance, sample_Given)

@given(instance=sample_When_strategy)
@settings(max_examples=50)
def test_sample_when_instantiation(instance):
    assert isinstance(instance, sample_When)

@given(instance=sample_Scenario_strategy)
@settings(max_examples=50)
def test_sample_scenario_instantiation(instance):
    assert isinstance(instance, sample_Scenario)



@given(instance=sample_Scenario_strategy)
def test_sample_scenario_Title_setter(instance):
    original = instance.Title
    instance.Title = original
    assert instance.Title == original

@given(instance=sample_Story_strategy)
@settings(max_examples=50)
def test_sample_story_instantiation(instance):
    assert isinstance(instance, sample_Story)



@given(instance=sample_Story_strategy)
def test_sample_story_Title_setter(instance):
    original = instance.Title
    instance.Title = original
    assert instance.Title == original



@given(instance=sample_Story_strategy)
def test_sample_story_Role_setter(instance):
    original = instance.Role
    instance.Role = original
    assert instance.Role == original



@given(instance=sample_Story_strategy)
def test_sample_story_Feature_setter(instance):
    original = instance.Feature
    instance.Feature = original
    assert instance.Feature == original



@given(instance=sample_Story_strategy)
def test_sample_story_Benefit_setter(instance):
    original = instance.Benefit
    instance.Benefit = original
    assert instance.Benefit == original

@given(instance=sample_Sentence_strategy)
@settings(max_examples=50)
def test_sample_sentence_instantiation(instance):
    assert isinstance(instance, sample_Sentence)



@given(instance=sample_Sentence_strategy)
def test_sample_sentence_Text_setter(instance):
    original = instance.Text
    instance.Text = original
    assert instance.Text == original
