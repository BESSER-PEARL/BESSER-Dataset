import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    MetamodelInheritance_BaseContaineeC,
    MetamodelInheritance_BaseContaineeB,
    MetamodelInheritance_BaseContaineeA,
    MetamodelInheritance_BaseContainer,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_metamodelinheritance_basecontaineec_is_not_abstract():
    assert not inspect.isabstract(MetamodelInheritance_BaseContaineeC)


def test_metamodelinheritance_basecontaineec_constructor_exists():
    assert callable(MetamodelInheritance_BaseContaineeC.__init__)


def test_metamodelinheritance_basecontaineec_constructor_args():
    sig = inspect.signature(MetamodelInheritance_BaseContaineeC.__init__)
    params = list(sig.parameters.keys())



def test_metamodelinheritance_basecontaineeb_is_not_abstract():
    assert not inspect.isabstract(MetamodelInheritance_BaseContaineeB)


def test_metamodelinheritance_basecontaineeb_constructor_exists():
    assert callable(MetamodelInheritance_BaseContaineeB.__init__)


def test_metamodelinheritance_basecontaineeb_constructor_args():
    sig = inspect.signature(MetamodelInheritance_BaseContaineeB.__init__)
    params = list(sig.parameters.keys())



def test_metamodelinheritance_basecontaineea_is_not_abstract():
    assert not inspect.isabstract(MetamodelInheritance_BaseContaineeA)


def test_metamodelinheritance_basecontaineea_constructor_exists():
    assert callable(MetamodelInheritance_BaseContaineeA.__init__)


def test_metamodelinheritance_basecontaineea_constructor_args():
    sig = inspect.signature(MetamodelInheritance_BaseContaineeA.__init__)
    params = list(sig.parameters.keys())



def test_metamodelinheritance_basecontainer_is_not_abstract():
    assert not inspect.isabstract(MetamodelInheritance_BaseContainer)


def test_metamodelinheritance_basecontainer_constructor_exists():
    assert callable(MetamodelInheritance_BaseContainer.__init__)


def test_metamodelinheritance_basecontainer_constructor_args():
    sig = inspect.signature(MetamodelInheritance_BaseContainer.__init__)
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
MetamodelInheritance_BaseContaineeC_strategy = st.builds(
    MetamodelInheritance_BaseContaineeC,
)
MetamodelInheritance_BaseContaineeB_strategy = st.builds(
    MetamodelInheritance_BaseContaineeB,
)
MetamodelInheritance_BaseContaineeA_strategy = st.builds(
    MetamodelInheritance_BaseContaineeA,
)
MetamodelInheritance_BaseContainer_strategy = st.builds(
    MetamodelInheritance_BaseContainer,
)

@given(instance=MetamodelInheritance_BaseContaineeC_strategy)
@settings(max_examples=50)
def test_metamodelinheritance_basecontaineec_instantiation(instance):
    assert isinstance(instance, MetamodelInheritance_BaseContaineeC)

@given(instance=MetamodelInheritance_BaseContaineeB_strategy)
@settings(max_examples=50)
def test_metamodelinheritance_basecontaineeb_instantiation(instance):
    assert isinstance(instance, MetamodelInheritance_BaseContaineeB)

@given(instance=MetamodelInheritance_BaseContaineeA_strategy)
@settings(max_examples=50)
def test_metamodelinheritance_basecontaineea_instantiation(instance):
    assert isinstance(instance, MetamodelInheritance_BaseContaineeA)

@given(instance=MetamodelInheritance_BaseContainer_strategy)
@settings(max_examples=50)
def test_metamodelinheritance_basecontainer_instantiation(instance):
    assert isinstance(instance, MetamodelInheritance_BaseContainer)
