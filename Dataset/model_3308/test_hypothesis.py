import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    StochasticSEIRDiseaseModel,
    experimental_PerculationDiseaseModel,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_stochasticseirdiseasemodel_is_not_abstract():
    assert not inspect.isabstract(StochasticSEIRDiseaseModel)


def test_stochasticseirdiseasemodel_constructor_exists():
    assert callable(StochasticSEIRDiseaseModel.__init__)


def test_stochasticseirdiseasemodel_constructor_args():
    sig = inspect.signature(StochasticSEIRDiseaseModel.__init__)
    params = list(sig.parameters.keys())



def test_experimental_perculationdiseasemodel_is_not_abstract():
    assert not inspect.isabstract(experimental_PerculationDiseaseModel)


def test_experimental_perculationdiseasemodel_constructor_exists():
    assert callable(experimental_PerculationDiseaseModel.__init__)


def test_experimental_perculationdiseasemodel_constructor_args():
    sig = inspect.signature(experimental_PerculationDiseaseModel.__init__)
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
StochasticSEIRDiseaseModel_strategy = st.builds(
    StochasticSEIRDiseaseModel,
)
experimental_PerculationDiseaseModel_strategy = st.builds(
    experimental_PerculationDiseaseModel,
)

@given(instance=StochasticSEIRDiseaseModel_strategy)
@settings(max_examples=50)
def test_stochasticseirdiseasemodel_instantiation(instance):
    assert isinstance(instance, StochasticSEIRDiseaseModel)

@given(instance=experimental_PerculationDiseaseModel_strategy)
@settings(max_examples=50)
def test_experimental_perculationdiseasemodel_instantiation(instance):
    assert isinstance(instance, experimental_PerculationDiseaseModel)
