import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    BaseContaineeB,
    MetamodelInheritance2_BaseContaineeC,
    MetamodelInheritance2_ChildContaineeD,
    MetamodelInheritance2_ChildB,
    BaseContaineeA,
    MetamodelInheritance2_ChildA,
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



def test_metamodelinheritance2_basecontaineec_is_not_abstract():
    assert not inspect.isabstract(MetamodelInheritance2_BaseContaineeC)


def test_metamodelinheritance2_basecontaineec_constructor_exists():
    assert callable(MetamodelInheritance2_BaseContaineeC.__init__)


def test_metamodelinheritance2_basecontaineec_constructor_args():
    sig = inspect.signature(MetamodelInheritance2_BaseContaineeC.__init__)
    params = list(sig.parameters.keys())



def test_metamodelinheritance2_childcontaineed_is_not_abstract():
    assert not inspect.isabstract(MetamodelInheritance2_ChildContaineeD)


def test_metamodelinheritance2_childcontaineed_constructor_exists():
    assert callable(MetamodelInheritance2_ChildContaineeD.__init__)


def test_metamodelinheritance2_childcontaineed_constructor_args():
    sig = inspect.signature(MetamodelInheritance2_ChildContaineeD.__init__)
    params = list(sig.parameters.keys())



def test_metamodelinheritance2_childb_is_not_abstract():
    assert not inspect.isabstract(MetamodelInheritance2_ChildB)


def test_metamodelinheritance2_childb_constructor_exists():
    assert callable(MetamodelInheritance2_ChildB.__init__)


def test_metamodelinheritance2_childb_constructor_args():
    sig = inspect.signature(MetamodelInheritance2_ChildB.__init__)
    params = list(sig.parameters.keys())



def test_basecontaineea_is_not_abstract():
    assert not inspect.isabstract(BaseContaineeA)


def test_basecontaineea_constructor_exists():
    assert callable(BaseContaineeA.__init__)


def test_basecontaineea_constructor_args():
    sig = inspect.signature(BaseContaineeA.__init__)
    params = list(sig.parameters.keys())



def test_metamodelinheritance2_childa_is_not_abstract():
    assert not inspect.isabstract(MetamodelInheritance2_ChildA)


def test_metamodelinheritance2_childa_constructor_exists():
    assert callable(MetamodelInheritance2_ChildA.__init__)


def test_metamodelinheritance2_childa_constructor_args():
    sig = inspect.signature(MetamodelInheritance2_ChildA.__init__)
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
MetamodelInheritance2_BaseContaineeC_strategy = st.builds(
    MetamodelInheritance2_BaseContaineeC,
)
MetamodelInheritance2_ChildContaineeD_strategy = st.builds(
    MetamodelInheritance2_ChildContaineeD,
)
MetamodelInheritance2_ChildB_strategy = st.builds(
    MetamodelInheritance2_ChildB,
)
BaseContaineeA_strategy = st.builds(
    BaseContaineeA,
)
MetamodelInheritance2_ChildA_strategy = st.builds(
    MetamodelInheritance2_ChildA,
)

@given(instance=BaseContaineeB_strategy)
@settings(max_examples=50)
def test_basecontaineeb_instantiation(instance):
    assert isinstance(instance, BaseContaineeB)

@given(instance=MetamodelInheritance2_BaseContaineeC_strategy)
@settings(max_examples=50)
def test_metamodelinheritance2_basecontaineec_instantiation(instance):
    assert isinstance(instance, MetamodelInheritance2_BaseContaineeC)

@given(instance=MetamodelInheritance2_ChildContaineeD_strategy)
@settings(max_examples=50)
def test_metamodelinheritance2_childcontaineed_instantiation(instance):
    assert isinstance(instance, MetamodelInheritance2_ChildContaineeD)

@given(instance=MetamodelInheritance2_ChildB_strategy)
@settings(max_examples=50)
def test_metamodelinheritance2_childb_instantiation(instance):
    assert isinstance(instance, MetamodelInheritance2_ChildB)

@given(instance=BaseContaineeA_strategy)
@settings(max_examples=50)
def test_basecontaineea_instantiation(instance):
    assert isinstance(instance, BaseContaineeA)

@given(instance=MetamodelInheritance2_ChildA_strategy)
@settings(max_examples=50)
def test_metamodelinheritance2_childa_instantiation(instance):
    assert isinstance(instance, MetamodelInheritance2_ChildA)
