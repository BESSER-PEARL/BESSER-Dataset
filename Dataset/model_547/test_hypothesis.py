import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    geneology_Member,
    geneology_Family,
    geneology_Geneology,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_geneology_member_is_not_abstract():
    assert not inspect.isabstract(geneology_Member)


def test_geneology_member_constructor_exists():
    assert callable(geneology_Member.__init__)


def test_geneology_member_constructor_args():
    sig = inspect.signature(geneology_Member.__init__)
    params = list(sig.parameters.keys())
    assert "female" in params, "Missing parameter 'female'"
    assert "name" in params, "Missing parameter 'name'"

def test_geneology_member_has_female():
    assert hasattr(geneology_Member, "female")
    descriptor = None
    for klass in geneology_Member.__mro__:
        if "female" in klass.__dict__:
            descriptor = klass.__dict__["female"]
            break
    assert isinstance(descriptor, property)

def test_geneology_member_has_name():
    assert hasattr(geneology_Member, "name")
    descriptor = None
    for klass in geneology_Member.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_geneology_family_is_not_abstract():
    assert not inspect.isabstract(geneology_Family)


def test_geneology_family_constructor_exists():
    assert callable(geneology_Family.__init__)


def test_geneology_family_constructor_args():
    sig = inspect.signature(geneology_Family.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_geneology_family_has_name():
    assert hasattr(geneology_Family, "name")
    descriptor = None
    for klass in geneology_Family.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_geneology_geneology_is_not_abstract():
    assert not inspect.isabstract(geneology_Geneology)


def test_geneology_geneology_constructor_exists():
    assert callable(geneology_Geneology.__init__)


def test_geneology_geneology_constructor_args():
    sig = inspect.signature(geneology_Geneology.__init__)
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
geneology_Member_strategy = st.builds(
    geneology_Member,
    female=
        st.booleans(),
    name=
        safe_text
)
geneology_Family_strategy = st.builds(
    geneology_Family,
    name=
        safe_text
)
geneology_Geneology_strategy = st.builds(
    geneology_Geneology,
)

@given(instance=geneology_Member_strategy)
@settings(max_examples=50)
def test_geneology_member_instantiation(instance):
    assert isinstance(instance, geneology_Member)



@given(instance=geneology_Member_strategy)
def test_geneology_member_female_setter(instance):
    original = instance.female
    instance.female = original
    assert instance.female == original



@given(instance=geneology_Member_strategy)
def test_geneology_member_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=geneology_Family_strategy)
@settings(max_examples=50)
def test_geneology_family_instantiation(instance):
    assert isinstance(instance, geneology_Family)



@given(instance=geneology_Family_strategy)
def test_geneology_family_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=geneology_Geneology_strategy)
@settings(max_examples=50)
def test_geneology_geneology_instantiation(instance):
    assert isinstance(instance, geneology_Geneology)
