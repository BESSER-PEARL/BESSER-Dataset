import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    db2EntityDsl::Attribute,
    AbstractColumnMapper,
    db2EntityDsl::EntityColumnMapper,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_db2entitydsl::attribute_is_not_abstract():
    assert not inspect.isabstract(db2EntityDsl::Attribute)


def test_db2entitydsl::attribute_constructor_exists():
    assert callable(db2EntityDsl::Attribute.__init__)


def test_db2entitydsl::attribute_constructor_args():
    sig = inspect.signature(db2EntityDsl::Attribute.__init__)
    params = list(sig.parameters.keys())



def test_abstractcolumnmapper_is_not_abstract():
    assert not inspect.isabstract(AbstractColumnMapper)


def test_abstractcolumnmapper_constructor_exists():
    assert callable(AbstractColumnMapper.__init__)


def test_abstractcolumnmapper_constructor_args():
    sig = inspect.signature(AbstractColumnMapper.__init__)
    params = list(sig.parameters.keys())



def test_db2entitydsl::entitycolumnmapper_is_not_abstract():
    assert not inspect.isabstract(db2EntityDsl::EntityColumnMapper)


def test_db2entitydsl::entitycolumnmapper_constructor_exists():
    assert callable(db2EntityDsl::EntityColumnMapper.__init__)


def test_db2entitydsl::entitycolumnmapper_constructor_args():
    sig = inspect.signature(db2EntityDsl::EntityColumnMapper.__init__)
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
db2EntityDsl::Attribute_strategy = st.builds(
    db2EntityDsl::Attribute,
)
AbstractColumnMapper_strategy = st.builds(
    AbstractColumnMapper,
)
db2EntityDsl::EntityColumnMapper_strategy = st.builds(
    db2EntityDsl::EntityColumnMapper,
)

@given(instance=db2EntityDsl::Attribute_strategy)
@settings(max_examples=50)
def test_db2entitydsl::attribute_instantiation(instance):
    assert isinstance(instance, db2EntityDsl::Attribute)

@given(instance=AbstractColumnMapper_strategy)
@settings(max_examples=50)
def test_abstractcolumnmapper_instantiation(instance):
    assert isinstance(instance, AbstractColumnMapper)

@given(instance=db2EntityDsl::EntityColumnMapper_strategy)
@settings(max_examples=50)
def test_db2entitydsl::entitycolumnmapper_instantiation(instance):
    assert isinstance(instance, db2EntityDsl::EntityColumnMapper)
