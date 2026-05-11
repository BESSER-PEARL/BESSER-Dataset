import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    MetamodelInheritance3::BaseContaineeA,
    ChildContaineeD,
    MetamodelInheritance3::ChildD,
    BaseContaineeC,
    MetamodelInheritance3::ChildC,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_metamodelinheritance3::basecontaineea_is_not_abstract():
    assert not inspect.isabstract(MetamodelInheritance3::BaseContaineeA)


def test_metamodelinheritance3::basecontaineea_constructor_exists():
    assert callable(MetamodelInheritance3::BaseContaineeA.__init__)


def test_metamodelinheritance3::basecontaineea_constructor_args():
    sig = inspect.signature(MetamodelInheritance3::BaseContaineeA.__init__)
    params = list(sig.parameters.keys())



def test_childcontaineed_is_not_abstract():
    assert not inspect.isabstract(ChildContaineeD)


def test_childcontaineed_constructor_exists():
    assert callable(ChildContaineeD.__init__)


def test_childcontaineed_constructor_args():
    sig = inspect.signature(ChildContaineeD.__init__)
    params = list(sig.parameters.keys())



def test_metamodelinheritance3::childd_is_not_abstract():
    assert not inspect.isabstract(MetamodelInheritance3::ChildD)


def test_metamodelinheritance3::childd_constructor_exists():
    assert callable(MetamodelInheritance3::ChildD.__init__)


def test_metamodelinheritance3::childd_constructor_args():
    sig = inspect.signature(MetamodelInheritance3::ChildD.__init__)
    params = list(sig.parameters.keys())



def test_basecontaineec_is_not_abstract():
    assert not inspect.isabstract(BaseContaineeC)


def test_basecontaineec_constructor_exists():
    assert callable(BaseContaineeC.__init__)


def test_basecontaineec_constructor_args():
    sig = inspect.signature(BaseContaineeC.__init__)
    params = list(sig.parameters.keys())



def test_metamodelinheritance3::childc_is_not_abstract():
    assert not inspect.isabstract(MetamodelInheritance3::ChildC)


def test_metamodelinheritance3::childc_constructor_exists():
    assert callable(MetamodelInheritance3::ChildC.__init__)


def test_metamodelinheritance3::childc_constructor_args():
    sig = inspect.signature(MetamodelInheritance3::ChildC.__init__)
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
MetamodelInheritance3::BaseContaineeA_strategy = st.builds(
    MetamodelInheritance3::BaseContaineeA,
)
ChildContaineeD_strategy = st.builds(
    ChildContaineeD,
)
MetamodelInheritance3::ChildD_strategy = st.builds(
    MetamodelInheritance3::ChildD,
)
BaseContaineeC_strategy = st.builds(
    BaseContaineeC,
)
MetamodelInheritance3::ChildC_strategy = st.builds(
    MetamodelInheritance3::ChildC,
)

@given(instance=MetamodelInheritance3::BaseContaineeA_strategy)
@settings(max_examples=50)
def test_metamodelinheritance3::basecontaineea_instantiation(instance):
    assert isinstance(instance, MetamodelInheritance3::BaseContaineeA)

@given(instance=ChildContaineeD_strategy)
@settings(max_examples=50)
def test_childcontaineed_instantiation(instance):
    assert isinstance(instance, ChildContaineeD)

@given(instance=MetamodelInheritance3::ChildD_strategy)
@settings(max_examples=50)
def test_metamodelinheritance3::childd_instantiation(instance):
    assert isinstance(instance, MetamodelInheritance3::ChildD)

@given(instance=BaseContaineeC_strategy)
@settings(max_examples=50)
def test_basecontaineec_instantiation(instance):
    assert isinstance(instance, BaseContaineeC)

@given(instance=MetamodelInheritance3::ChildC_strategy)
@settings(max_examples=50)
def test_metamodelinheritance3::childc_instantiation(instance):
    assert isinstance(instance, MetamodelInheritance3::ChildC)
