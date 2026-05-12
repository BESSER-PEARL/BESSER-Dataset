import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    db2EntityDsl_Attribute,
    AbstractColumnMapper,
    db2EntityDsl_EntityColumnMapper,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_db2entitydsl_attribute_is_not_abstract():
    assert not inspect.isabstract(db2EntityDsl_Attribute)


def test_db2entitydsl_attribute_constructor_exists():
    assert callable(db2EntityDsl_Attribute.__init__)


def test_db2entitydsl_attribute_constructor_args():
    sig = inspect.signature(db2EntityDsl_Attribute.__init__)
    params = list(sig.parameters.keys())



def test_abstractcolumnmapper_is_not_abstract():
    assert not inspect.isabstract(AbstractColumnMapper)


def test_abstractcolumnmapper_constructor_exists():
    assert callable(AbstractColumnMapper.__init__)


def test_abstractcolumnmapper_constructor_args():
    sig = inspect.signature(AbstractColumnMapper.__init__)
    params = list(sig.parameters.keys())



def test_db2entitydsl_entitycolumnmapper_is_not_abstract():
    assert not inspect.isabstract(db2EntityDsl_EntityColumnMapper)


def test_db2entitydsl_entitycolumnmapper_constructor_exists():
    assert callable(db2EntityDsl_EntityColumnMapper.__init__)


def test_db2entitydsl_entitycolumnmapper_constructor_args():
    sig = inspect.signature(db2EntityDsl_EntityColumnMapper.__init__)
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
db2EntityDsl_Attribute_strategy = st.builds(
    db2EntityDsl_Attribute,
)
AbstractColumnMapper_strategy = st.builds(
    AbstractColumnMapper,
)
db2EntityDsl_EntityColumnMapper_strategy = st.builds(
    db2EntityDsl_EntityColumnMapper,
)

@given(instance=db2EntityDsl_Attribute_strategy)
@settings(max_examples=50)
def test_db2entitydsl_attribute_instantiation(instance):
    assert isinstance(instance, db2EntityDsl_Attribute)

@given(instance=AbstractColumnMapper_strategy)
@settings(max_examples=50)
def test_abstractcolumnmapper_instantiation(instance):
    assert isinstance(instance, AbstractColumnMapper)

@given(instance=db2EntityDsl_EntityColumnMapper_strategy)
@settings(max_examples=50)
def test_db2entitydsl_entitycolumnmapper_instantiation(instance):
    assert isinstance(instance, db2EntityDsl_EntityColumnMapper)
