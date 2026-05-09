import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    geneology::Member,
    geneology::Family,
    geneology::Geneology,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_geneology::member_is_not_abstract():
    assert not inspect.isabstract(geneology::Member)


def test_geneology::member_constructor_exists():
    assert callable(geneology::Member.__init__)


def test_geneology::member_constructor_args():
    sig = inspect.signature(geneology::Member.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "female" in params, "Missing parameter 'female'"

def test_geneology::member_has_name():
    assert hasattr(geneology::Member, "name")
    descriptor = None
    for klass in geneology::Member.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_geneology::member_has_female():
    assert hasattr(geneology::Member, "female")
    descriptor = None
    for klass in geneology::Member.__mro__:
        if "female" in klass.__dict__:
            descriptor = klass.__dict__["female"]
            break
    assert isinstance(descriptor, property)



def test_geneology::family_is_not_abstract():
    assert not inspect.isabstract(geneology::Family)


def test_geneology::family_constructor_exists():
    assert callable(geneology::Family.__init__)


def test_geneology::family_constructor_args():
    sig = inspect.signature(geneology::Family.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_geneology::family_has_name():
    assert hasattr(geneology::Family, "name")
    descriptor = None
    for klass in geneology::Family.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_geneology::geneology_is_not_abstract():
    assert not inspect.isabstract(geneology::Geneology)


def test_geneology::geneology_constructor_exists():
    assert callable(geneology::Geneology.__init__)


def test_geneology::geneology_constructor_args():
    sig = inspect.signature(geneology::Geneology.__init__)
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
geneology::Member_strategy = st.builds(
    geneology::Member,
    name=
        safe_text,
    female=
        st.booleans()
)
geneology::Family_strategy = st.builds(
    geneology::Family,
    name=
        safe_text
)
geneology::Geneology_strategy = st.builds(
    geneology::Geneology,
)

@given(instance=geneology::Member_strategy)
@settings(max_examples=50)
def test_geneology::member_instantiation(instance):
    assert isinstance(instance, geneology::Member)

@given(instance=geneology::Member_strategy)
def test_geneology::member_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=geneology::Member_strategy)
def test_geneology::member_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=geneology::Member_strategy)
def test_geneology::member_female_type(instance):
    assert isinstance(instance.female, bool)


@given(instance=geneology::Member_strategy)
def test_geneology::member_female_setter(instance):
    original = instance.female
    instance.female = original
    assert instance.female == original

@given(instance=geneology::Family_strategy)
@settings(max_examples=50)
def test_geneology::family_instantiation(instance):
    assert isinstance(instance, geneology::Family)

@given(instance=geneology::Family_strategy)
def test_geneology::family_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=geneology::Family_strategy)
def test_geneology::family_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=geneology::Geneology_strategy)
@settings(max_examples=50)
def test_geneology::geneology_instantiation(instance):
    assert isinstance(instance, geneology::Geneology)
