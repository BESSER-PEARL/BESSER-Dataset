import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Lims::Sequenced,
    Lims::Run,
    Lims::Sequencer,
    Lims::Laboratory,
    Lims::Individual,
    Lims::Family,
    Lims::Sample,
    Gender,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_lims::sequenced_is_not_abstract():
    assert not inspect.isabstract(Lims::Sequenced)


def test_lims::sequenced_constructor_exists():
    assert callable(Lims::Sequenced.__init__)


def test_lims::sequenced_constructor_args():
    sig = inspect.signature(Lims::Sequenced.__init__)
    params = list(sig.parameters.keys())



def test_lims::run_is_not_abstract():
    assert not inspect.isabstract(Lims::Run)


def test_lims::run_constructor_exists():
    assert callable(Lims::Run.__init__)


def test_lims::run_constructor_args():
    sig = inspect.signature(Lims::Run.__init__)
    params = list(sig.parameters.keys())
    assert "date" in params, "Missing parameter 'date'"
    assert "name" in params, "Missing parameter 'name'"

def test_lims::run_has_date():
    assert hasattr(Lims::Run, "date")
    descriptor = None
    for klass in Lims::Run.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)

def test_lims::run_has_name():
    assert hasattr(Lims::Run, "name")
    descriptor = None
    for klass in Lims::Run.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_lims::sequencer_is_not_abstract():
    assert not inspect.isabstract(Lims::Sequencer)


def test_lims::sequencer_constructor_exists():
    assert callable(Lims::Sequencer.__init__)


def test_lims::sequencer_constructor_args():
    sig = inspect.signature(Lims::Sequencer.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_lims::sequencer_has_name():
    assert hasattr(Lims::Sequencer, "name")
    descriptor = None
    for klass in Lims::Sequencer.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_lims::laboratory_is_not_abstract():
    assert not inspect.isabstract(Lims::Laboratory)


def test_lims::laboratory_constructor_exists():
    assert callable(Lims::Laboratory.__init__)


def test_lims::laboratory_constructor_args():
    sig = inspect.signature(Lims::Laboratory.__init__)
    params = list(sig.parameters.keys())



def test_lims::individual_is_not_abstract():
    assert not inspect.isabstract(Lims::Individual)


def test_lims::individual_constructor_exists():
    assert callable(Lims::Individual.__init__)


def test_lims::individual_constructor_args():
    sig = inspect.signature(Lims::Individual.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "gender" in params, "Missing parameter 'gender'"

def test_lims::individual_has_name():
    assert hasattr(Lims::Individual, "name")
    descriptor = None
    for klass in Lims::Individual.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_lims::individual_has_gender():
    assert hasattr(Lims::Individual, "gender")
    descriptor = None
    for klass in Lims::Individual.__mro__:
        if "gender" in klass.__dict__:
            descriptor = klass.__dict__["gender"]
            break
    assert isinstance(descriptor, property)



def test_lims::family_is_not_abstract():
    assert not inspect.isabstract(Lims::Family)


def test_lims::family_constructor_exists():
    assert callable(Lims::Family.__init__)


def test_lims::family_constructor_args():
    sig = inspect.signature(Lims::Family.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_lims::family_has_name():
    assert hasattr(Lims::Family, "name")
    descriptor = None
    for klass in Lims::Family.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_lims::sample_is_not_abstract():
    assert not inspect.isabstract(Lims::Sample)


def test_lims::sample_constructor_exists():
    assert callable(Lims::Sample.__init__)


def test_lims::sample_constructor_args():
    sig = inspect.signature(Lims::Sample.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_lims::sample_has_id():
    assert hasattr(Lims::Sample, "id")
    descriptor = None
    for klass in Lims::Sample.__mro__:
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
        "UNKNOWN",
        "MALE",
        "FEMALE",
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
Lims::Sequenced_strategy = st.builds(
    Lims::Sequenced,
)
Lims::Run_strategy = st.builds(
    Lims::Run,
    date=
        st.dates(),
    name=
        safe_text
)
Lims::Sequencer_strategy = st.builds(
    Lims::Sequencer,
    name=
        safe_text
)
Lims::Laboratory_strategy = st.builds(
    Lims::Laboratory,
)
Lims::Individual_strategy = st.builds(
    Lims::Individual,
    name=
        safe_text,
    gender=
        safe_text
)
Lims::Family_strategy = st.builds(
    Lims::Family,
    name=
        safe_text
)
Lims::Sample_strategy = st.builds(
    Lims::Sample,
    id=
        safe_text
)

@given(instance=Lims::Sequenced_strategy)
@settings(max_examples=50)
def test_lims::sequenced_instantiation(instance):
    assert isinstance(instance, Lims::Sequenced)

@given(instance=Lims::Run_strategy)
@settings(max_examples=50)
def test_lims::run_instantiation(instance):
    assert isinstance(instance, Lims::Run)

@given(instance=Lims::Run_strategy)
def test_lims::run_date_type(instance):
    assert isinstance(instance.date, date)


@given(instance=Lims::Run_strategy)
def test_lims::run_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original

@given(instance=Lims::Run_strategy)
def test_lims::run_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Lims::Run_strategy)
def test_lims::run_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Lims::Sequencer_strategy)
@settings(max_examples=50)
def test_lims::sequencer_instantiation(instance):
    assert isinstance(instance, Lims::Sequencer)

@given(instance=Lims::Sequencer_strategy)
def test_lims::sequencer_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Lims::Sequencer_strategy)
def test_lims::sequencer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Lims::Laboratory_strategy)
@settings(max_examples=50)
def test_lims::laboratory_instantiation(instance):
    assert isinstance(instance, Lims::Laboratory)

@given(instance=Lims::Individual_strategy)
@settings(max_examples=50)
def test_lims::individual_instantiation(instance):
    assert isinstance(instance, Lims::Individual)

@given(instance=Lims::Individual_strategy)
def test_lims::individual_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Lims::Individual_strategy)
def test_lims::individual_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Lims::Individual_strategy)
def test_lims::individual_gender_type(instance):
    assert isinstance(instance.gender, str)


@given(instance=Lims::Individual_strategy)
def test_lims::individual_gender_setter(instance):
    original = instance.gender
    instance.gender = original
    assert instance.gender == original

@given(instance=Lims::Family_strategy)
@settings(max_examples=50)
def test_lims::family_instantiation(instance):
    assert isinstance(instance, Lims::Family)

@given(instance=Lims::Family_strategy)
def test_lims::family_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Lims::Family_strategy)
def test_lims::family_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Lims::Sample_strategy)
@settings(max_examples=50)
def test_lims::sample_instantiation(instance):
    assert isinstance(instance, Lims::Sample)

@given(instance=Lims::Sample_strategy)
def test_lims::sample_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=Lims::Sample_strategy)
def test_lims::sample_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original
