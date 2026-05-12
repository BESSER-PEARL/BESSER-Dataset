import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Lims_Sequenced,
    Lims_Run,
    Lims_Sequencer,
    Lims_Laboratory,
    Lims_Individual,
    Lims_Family,
    Lims_Sample,
    Gender,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_lims_sequenced_is_not_abstract():
    assert not inspect.isabstract(Lims_Sequenced)


def test_lims_sequenced_constructor_exists():
    assert callable(Lims_Sequenced.__init__)


def test_lims_sequenced_constructor_args():
    sig = inspect.signature(Lims_Sequenced.__init__)
    params = list(sig.parameters.keys())



def test_lims_run_is_not_abstract():
    assert not inspect.isabstract(Lims_Run)


def test_lims_run_constructor_exists():
    assert callable(Lims_Run.__init__)


def test_lims_run_constructor_args():
    sig = inspect.signature(Lims_Run.__init__)
    params = list(sig.parameters.keys())
    assert "date" in params, "Missing parameter 'date'"
    assert "name" in params, "Missing parameter 'name'"

def test_lims_run_has_date():
    assert hasattr(Lims_Run, "date")
    descriptor = None
    for klass in Lims_Run.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)

def test_lims_run_has_name():
    assert hasattr(Lims_Run, "name")
    descriptor = None
    for klass in Lims_Run.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_lims_sequencer_is_not_abstract():
    assert not inspect.isabstract(Lims_Sequencer)


def test_lims_sequencer_constructor_exists():
    assert callable(Lims_Sequencer.__init__)


def test_lims_sequencer_constructor_args():
    sig = inspect.signature(Lims_Sequencer.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_lims_sequencer_has_name():
    assert hasattr(Lims_Sequencer, "name")
    descriptor = None
    for klass in Lims_Sequencer.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_lims_laboratory_is_not_abstract():
    assert not inspect.isabstract(Lims_Laboratory)


def test_lims_laboratory_constructor_exists():
    assert callable(Lims_Laboratory.__init__)


def test_lims_laboratory_constructor_args():
    sig = inspect.signature(Lims_Laboratory.__init__)
    params = list(sig.parameters.keys())



def test_lims_individual_is_not_abstract():
    assert not inspect.isabstract(Lims_Individual)


def test_lims_individual_constructor_exists():
    assert callable(Lims_Individual.__init__)


def test_lims_individual_constructor_args():
    sig = inspect.signature(Lims_Individual.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "gender" in params, "Missing parameter 'gender'"

def test_lims_individual_has_name():
    assert hasattr(Lims_Individual, "name")
    descriptor = None
    for klass in Lims_Individual.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_lims_individual_has_gender():
    assert hasattr(Lims_Individual, "gender")
    descriptor = None
    for klass in Lims_Individual.__mro__:
        if "gender" in klass.__dict__:
            descriptor = klass.__dict__["gender"]
            break
    assert isinstance(descriptor, property)



def test_lims_family_is_not_abstract():
    assert not inspect.isabstract(Lims_Family)


def test_lims_family_constructor_exists():
    assert callable(Lims_Family.__init__)


def test_lims_family_constructor_args():
    sig = inspect.signature(Lims_Family.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_lims_family_has_name():
    assert hasattr(Lims_Family, "name")
    descriptor = None
    for klass in Lims_Family.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_lims_sample_is_not_abstract():
    assert not inspect.isabstract(Lims_Sample)


def test_lims_sample_constructor_exists():
    assert callable(Lims_Sample.__init__)


def test_lims_sample_constructor_args():
    sig = inspect.signature(Lims_Sample.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_lims_sample_has_id():
    assert hasattr(Lims_Sample, "id")
    descriptor = None
    for klass in Lims_Sample.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_gender_exists():
    # Check that the Enumeration exists
    assert Gender is not None

def test_gender_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Gender]
    expected_literals = [
        "MALE",
        "FEMALE",
        "UNKNOWN",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Gender"


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
Lims_Sequenced_strategy = st.builds(
    Lims_Sequenced,
)
Lims_Run_strategy = st.builds(
    Lims_Run,
    date=
        st.dates(),
    name=
        safe_text
)
Lims_Sequencer_strategy = st.builds(
    Lims_Sequencer,
    name=
        safe_text
)
Lims_Laboratory_strategy = st.builds(
    Lims_Laboratory,
)
Lims_Individual_strategy = st.builds(
    Lims_Individual,
    name=
        safe_text,
    gender=
        safe_text
)
Lims_Family_strategy = st.builds(
    Lims_Family,
    name=
        safe_text
)
Lims_Sample_strategy = st.builds(
    Lims_Sample,
    id=
        safe_text
)

@given(instance=Lims_Sequenced_strategy)
@settings(max_examples=50)
def test_lims_sequenced_instantiation(instance):
    assert isinstance(instance, Lims_Sequenced)

@given(instance=Lims_Run_strategy)
@settings(max_examples=50)
def test_lims_run_instantiation(instance):
    assert isinstance(instance, Lims_Run)



@given(instance=Lims_Run_strategy)
def test_lims_run_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original



@given(instance=Lims_Run_strategy)
def test_lims_run_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Lims_Sequencer_strategy)
@settings(max_examples=50)
def test_lims_sequencer_instantiation(instance):
    assert isinstance(instance, Lims_Sequencer)



@given(instance=Lims_Sequencer_strategy)
def test_lims_sequencer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Lims_Laboratory_strategy)
@settings(max_examples=50)
def test_lims_laboratory_instantiation(instance):
    assert isinstance(instance, Lims_Laboratory)

@given(instance=Lims_Individual_strategy)
@settings(max_examples=50)
def test_lims_individual_instantiation(instance):
    assert isinstance(instance, Lims_Individual)



@given(instance=Lims_Individual_strategy)
def test_lims_individual_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Lims_Individual_strategy)
def test_lims_individual_gender_setter(instance):
    original = instance.gender
    instance.gender = original
    assert instance.gender == original

@given(instance=Lims_Family_strategy)
@settings(max_examples=50)
def test_lims_family_instantiation(instance):
    assert isinstance(instance, Lims_Family)



@given(instance=Lims_Family_strategy)
def test_lims_family_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Lims_Sample_strategy)
@settings(max_examples=50)
def test_lims_sample_instantiation(instance):
    assert isinstance(instance, Lims_Sample)



@given(instance=Lims_Sample_strategy)
def test_lims_sample_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original
