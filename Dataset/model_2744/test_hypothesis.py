import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    MetamodelInheritance::BaseContaineeC,
    MetamodelInheritance::BaseContaineeB,
    MetamodelInheritance::BaseContaineeA,
    MetamodelInheritance::BaseContainer,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_metamodelinheritance::basecontaineec_is_not_abstract():
    assert not inspect.isabstract(MetamodelInheritance::BaseContaineeC)


def test_metamodelinheritance::basecontaineec_constructor_exists():
    assert callable(MetamodelInheritance::BaseContaineeC.__init__)


def test_metamodelinheritance::basecontaineec_constructor_args():
    sig = inspect.signature(MetamodelInheritance::BaseContaineeC.__init__)
    params = list(sig.parameters.keys())



def test_metamodelinheritance::basecontaineeb_is_not_abstract():
    assert not inspect.isabstract(MetamodelInheritance::BaseContaineeB)


def test_metamodelinheritance::basecontaineeb_constructor_exists():
    assert callable(MetamodelInheritance::BaseContaineeB.__init__)


def test_metamodelinheritance::basecontaineeb_constructor_args():
    sig = inspect.signature(MetamodelInheritance::BaseContaineeB.__init__)
    params = list(sig.parameters.keys())



def test_metamodelinheritance::basecontaineea_is_not_abstract():
    assert not inspect.isabstract(MetamodelInheritance::BaseContaineeA)


def test_metamodelinheritance::basecontaineea_constructor_exists():
    assert callable(MetamodelInheritance::BaseContaineeA.__init__)


def test_metamodelinheritance::basecontaineea_constructor_args():
    sig = inspect.signature(MetamodelInheritance::BaseContaineeA.__init__)
    params = list(sig.parameters.keys())



def test_metamodelinheritance::basecontainer_is_not_abstract():
    assert not inspect.isabstract(MetamodelInheritance::BaseContainer)


def test_metamodelinheritance::basecontainer_constructor_exists():
    assert callable(MetamodelInheritance::BaseContainer.__init__)


def test_metamodelinheritance::basecontainer_constructor_args():
    sig = inspect.signature(MetamodelInheritance::BaseContainer.__init__)
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
MetamodelInheritance::BaseContaineeC_strategy = st.builds(
    MetamodelInheritance::BaseContaineeC,
)
MetamodelInheritance::BaseContaineeB_strategy = st.builds(
    MetamodelInheritance::BaseContaineeB,
)
MetamodelInheritance::BaseContaineeA_strategy = st.builds(
    MetamodelInheritance::BaseContaineeA,
)
MetamodelInheritance::BaseContainer_strategy = st.builds(
    MetamodelInheritance::BaseContainer,
)

@given(instance=MetamodelInheritance::BaseContaineeC_strategy)
@settings(max_examples=50)
def test_metamodelinheritance::basecontaineec_instantiation(instance):
    assert isinstance(instance, MetamodelInheritance::BaseContaineeC)

@given(instance=MetamodelInheritance::BaseContaineeB_strategy)
@settings(max_examples=50)
def test_metamodelinheritance::basecontaineeb_instantiation(instance):
    assert isinstance(instance, MetamodelInheritance::BaseContaineeB)

@given(instance=MetamodelInheritance::BaseContaineeA_strategy)
@settings(max_examples=50)
def test_metamodelinheritance::basecontaineea_instantiation(instance):
    assert isinstance(instance, MetamodelInheritance::BaseContaineeA)

@given(instance=MetamodelInheritance::BaseContainer_strategy)
@settings(max_examples=50)
def test_metamodelinheritance::basecontainer_instantiation(instance):
    assert isinstance(instance, MetamodelInheritance::BaseContainer)
