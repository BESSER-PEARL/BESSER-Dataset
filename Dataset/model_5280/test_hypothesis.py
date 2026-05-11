import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    BaseContaineeB,
    MetamodelInheritance2::BaseContaineeC,
    MetamodelInheritance2::ChildContaineeD,
    MetamodelInheritance2::ChildB,
    BaseContaineeA,
    MetamodelInheritance2::ChildA,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_basecontaineeb_is_not_abstract():
    assert not inspect.isabstract(BaseContaineeB)


def test_basecontaineeb_constructor_exists():
    assert callable(BaseContaineeB.__init__)


def test_basecontaineeb_constructor_args():
    sig = inspect.signature(BaseContaineeB.__init__)
    params = list(sig.parameters.keys())



def test_metamodelinheritance2::basecontaineec_is_not_abstract():
    assert not inspect.isabstract(MetamodelInheritance2::BaseContaineeC)


def test_metamodelinheritance2::basecontaineec_constructor_exists():
    assert callable(MetamodelInheritance2::BaseContaineeC.__init__)


def test_metamodelinheritance2::basecontaineec_constructor_args():
    sig = inspect.signature(MetamodelInheritance2::BaseContaineeC.__init__)
    params = list(sig.parameters.keys())



def test_metamodelinheritance2::childcontaineed_is_not_abstract():
    assert not inspect.isabstract(MetamodelInheritance2::ChildContaineeD)


def test_metamodelinheritance2::childcontaineed_constructor_exists():
    assert callable(MetamodelInheritance2::ChildContaineeD.__init__)


def test_metamodelinheritance2::childcontaineed_constructor_args():
    sig = inspect.signature(MetamodelInheritance2::ChildContaineeD.__init__)
    params = list(sig.parameters.keys())



def test_metamodelinheritance2::childb_is_not_abstract():
    assert not inspect.isabstract(MetamodelInheritance2::ChildB)


def test_metamodelinheritance2::childb_constructor_exists():
    assert callable(MetamodelInheritance2::ChildB.__init__)


def test_metamodelinheritance2::childb_constructor_args():
    sig = inspect.signature(MetamodelInheritance2::ChildB.__init__)
    params = list(sig.parameters.keys())



def test_basecontaineea_is_not_abstract():
    assert not inspect.isabstract(BaseContaineeA)


def test_basecontaineea_constructor_exists():
    assert callable(BaseContaineeA.__init__)


def test_basecontaineea_constructor_args():
    sig = inspect.signature(BaseContaineeA.__init__)
    params = list(sig.parameters.keys())



def test_metamodelinheritance2::childa_is_not_abstract():
    assert not inspect.isabstract(MetamodelInheritance2::ChildA)


def test_metamodelinheritance2::childa_constructor_exists():
    assert callable(MetamodelInheritance2::ChildA.__init__)


def test_metamodelinheritance2::childa_constructor_args():
    sig = inspect.signature(MetamodelInheritance2::ChildA.__init__)
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
BaseContaineeB_strategy = st.builds(
    BaseContaineeB,
)
MetamodelInheritance2::BaseContaineeC_strategy = st.builds(
    MetamodelInheritance2::BaseContaineeC,
)
MetamodelInheritance2::ChildContaineeD_strategy = st.builds(
    MetamodelInheritance2::ChildContaineeD,
)
MetamodelInheritance2::ChildB_strategy = st.builds(
    MetamodelInheritance2::ChildB,
)
BaseContaineeA_strategy = st.builds(
    BaseContaineeA,
)
MetamodelInheritance2::ChildA_strategy = st.builds(
    MetamodelInheritance2::ChildA,
)

@given(instance=BaseContaineeB_strategy)
@settings(max_examples=50)
def test_basecontaineeb_instantiation(instance):
    assert isinstance(instance, BaseContaineeB)

@given(instance=MetamodelInheritance2::BaseContaineeC_strategy)
@settings(max_examples=50)
def test_metamodelinheritance2::basecontaineec_instantiation(instance):
    assert isinstance(instance, MetamodelInheritance2::BaseContaineeC)

@given(instance=MetamodelInheritance2::ChildContaineeD_strategy)
@settings(max_examples=50)
def test_metamodelinheritance2::childcontaineed_instantiation(instance):
    assert isinstance(instance, MetamodelInheritance2::ChildContaineeD)

@given(instance=MetamodelInheritance2::ChildB_strategy)
@settings(max_examples=50)
def test_metamodelinheritance2::childb_instantiation(instance):
    assert isinstance(instance, MetamodelInheritance2::ChildB)

@given(instance=BaseContaineeA_strategy)
@settings(max_examples=50)
def test_basecontaineea_instantiation(instance):
    assert isinstance(instance, BaseContaineeA)

@given(instance=MetamodelInheritance2::ChildA_strategy)
@settings(max_examples=50)
def test_metamodelinheritance2::childa_instantiation(instance):
    assert isinstance(instance, MetamodelInheritance2::ChildA)
