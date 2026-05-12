import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    MetamodelInheritance3_BaseContaineeA,
    ChildContaineeD,
    MetamodelInheritance3_ChildD,
    BaseContaineeC,
    MetamodelInheritance3_ChildC,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_metamodelinheritance3_basecontaineea_is_not_abstract():
    assert not inspect.isabstract(MetamodelInheritance3_BaseContaineeA)


def test_metamodelinheritance3_basecontaineea_constructor_exists():
    assert callable(MetamodelInheritance3_BaseContaineeA.__init__)


def test_metamodelinheritance3_basecontaineea_constructor_args():
    sig = inspect.signature(MetamodelInheritance3_BaseContaineeA.__init__)
    params = list(sig.parameters.keys())



def test_childcontaineed_is_not_abstract():
    assert not inspect.isabstract(ChildContaineeD)


def test_childcontaineed_constructor_exists():
    assert callable(ChildContaineeD.__init__)


def test_childcontaineed_constructor_args():
    sig = inspect.signature(ChildContaineeD.__init__)
    params = list(sig.parameters.keys())



def test_metamodelinheritance3_childd_is_not_abstract():
    assert not inspect.isabstract(MetamodelInheritance3_ChildD)


def test_metamodelinheritance3_childd_constructor_exists():
    assert callable(MetamodelInheritance3_ChildD.__init__)


def test_metamodelinheritance3_childd_constructor_args():
    sig = inspect.signature(MetamodelInheritance3_ChildD.__init__)
    params = list(sig.parameters.keys())



def test_basecontaineec_is_not_abstract():
    assert not inspect.isabstract(BaseContaineeC)


def test_basecontaineec_constructor_exists():
    assert callable(BaseContaineeC.__init__)


def test_basecontaineec_constructor_args():
    sig = inspect.signature(BaseContaineeC.__init__)
    params = list(sig.parameters.keys())



def test_metamodelinheritance3_childc_is_not_abstract():
    assert not inspect.isabstract(MetamodelInheritance3_ChildC)


def test_metamodelinheritance3_childc_constructor_exists():
    assert callable(MetamodelInheritance3_ChildC.__init__)


def test_metamodelinheritance3_childc_constructor_args():
    sig = inspect.signature(MetamodelInheritance3_ChildC.__init__)
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
MetamodelInheritance3_BaseContaineeA_strategy = st.builds(
    MetamodelInheritance3_BaseContaineeA,
)
ChildContaineeD_strategy = st.builds(
    ChildContaineeD,
)
MetamodelInheritance3_ChildD_strategy = st.builds(
    MetamodelInheritance3_ChildD,
)
BaseContaineeC_strategy = st.builds(
    BaseContaineeC,
)
MetamodelInheritance3_ChildC_strategy = st.builds(
    MetamodelInheritance3_ChildC,
)

@given(instance=MetamodelInheritance3_BaseContaineeA_strategy)
@settings(max_examples=50)
def test_metamodelinheritance3_basecontaineea_instantiation(instance):
    assert isinstance(instance, MetamodelInheritance3_BaseContaineeA)

@given(instance=ChildContaineeD_strategy)
@settings(max_examples=50)
def test_childcontaineed_instantiation(instance):
    assert isinstance(instance, ChildContaineeD)

@given(instance=MetamodelInheritance3_ChildD_strategy)
@settings(max_examples=50)
def test_metamodelinheritance3_childd_instantiation(instance):
    assert isinstance(instance, MetamodelInheritance3_ChildD)

@given(instance=BaseContaineeC_strategy)
@settings(max_examples=50)
def test_basecontaineec_instantiation(instance):
    assert isinstance(instance, BaseContaineeC)

@given(instance=MetamodelInheritance3_ChildC_strategy)
@settings(max_examples=50)
def test_metamodelinheritance3_childc_instantiation(instance):
    assert isinstance(instance, MetamodelInheritance3_ChildC)
