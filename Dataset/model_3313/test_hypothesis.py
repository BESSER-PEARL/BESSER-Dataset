import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    viatraTraceability::Identification,
    viatraTraceability::AbstractElement,
    viatraTraceability::DepToGSPNTrace,
    viatraTraceability::DepModel,
    viatraTraceability::PetriNet,
    viatraTraceability::DepToGSPN,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_viatratraceability::identification_is_not_abstract():
    assert not inspect.isabstract(viatraTraceability::Identification)


def test_viatratraceability::identification_constructor_exists():
    assert callable(viatraTraceability::Identification.__init__)


def test_viatratraceability::identification_constructor_args():
    sig = inspect.signature(viatraTraceability::Identification.__init__)
    params = list(sig.parameters.keys())



def test_viatratraceability::abstractelement_is_not_abstract():
    assert not inspect.isabstract(viatraTraceability::AbstractElement)


def test_viatratraceability::abstractelement_constructor_exists():
    assert callable(viatraTraceability::AbstractElement.__init__)


def test_viatratraceability::abstractelement_constructor_args():
    sig = inspect.signature(viatraTraceability::AbstractElement.__init__)
    params = list(sig.parameters.keys())



def test_viatratraceability::deptogspntrace_is_not_abstract():
    assert not inspect.isabstract(viatraTraceability::DepToGSPNTrace)


def test_viatratraceability::deptogspntrace_constructor_exists():
    assert callable(viatraTraceability::DepToGSPNTrace.__init__)


def test_viatratraceability::deptogspntrace_constructor_args():
    sig = inspect.signature(viatraTraceability::DepToGSPNTrace.__init__)
    params = list(sig.parameters.keys())



def test_viatratraceability::depmodel_is_not_abstract():
    assert not inspect.isabstract(viatraTraceability::DepModel)


def test_viatratraceability::depmodel_constructor_exists():
    assert callable(viatraTraceability::DepModel.__init__)


def test_viatratraceability::depmodel_constructor_args():
    sig = inspect.signature(viatraTraceability::DepModel.__init__)
    params = list(sig.parameters.keys())



def test_viatratraceability::petrinet_is_not_abstract():
    assert not inspect.isabstract(viatraTraceability::PetriNet)


def test_viatratraceability::petrinet_constructor_exists():
    assert callable(viatraTraceability::PetriNet.__init__)


def test_viatratraceability::petrinet_constructor_args():
    sig = inspect.signature(viatraTraceability::PetriNet.__init__)
    params = list(sig.parameters.keys())



def test_viatratraceability::deptogspn_is_not_abstract():
    assert not inspect.isabstract(viatraTraceability::DepToGSPN)


def test_viatratraceability::deptogspn_constructor_exists():
    assert callable(viatraTraceability::DepToGSPN.__init__)


def test_viatratraceability::deptogspn_constructor_args():
    sig = inspect.signature(viatraTraceability::DepToGSPN.__init__)
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
viatraTraceability::Identification_strategy = st.builds(
    viatraTraceability::Identification,
)
viatraTraceability::AbstractElement_strategy = st.builds(
    viatraTraceability::AbstractElement,
)
viatraTraceability::DepToGSPNTrace_strategy = st.builds(
    viatraTraceability::DepToGSPNTrace,
)
viatraTraceability::DepModel_strategy = st.builds(
    viatraTraceability::DepModel,
)
viatraTraceability::PetriNet_strategy = st.builds(
    viatraTraceability::PetriNet,
)
viatraTraceability::DepToGSPN_strategy = st.builds(
    viatraTraceability::DepToGSPN,
)

@given(instance=viatraTraceability::Identification_strategy)
@settings(max_examples=50)
def test_viatratraceability::identification_instantiation(instance):
    assert isinstance(instance, viatraTraceability::Identification)

@given(instance=viatraTraceability::AbstractElement_strategy)
@settings(max_examples=50)
def test_viatratraceability::abstractelement_instantiation(instance):
    assert isinstance(instance, viatraTraceability::AbstractElement)

@given(instance=viatraTraceability::DepToGSPNTrace_strategy)
@settings(max_examples=50)
def test_viatratraceability::deptogspntrace_instantiation(instance):
    assert isinstance(instance, viatraTraceability::DepToGSPNTrace)

@given(instance=viatraTraceability::DepModel_strategy)
@settings(max_examples=50)
def test_viatratraceability::depmodel_instantiation(instance):
    assert isinstance(instance, viatraTraceability::DepModel)

@given(instance=viatraTraceability::PetriNet_strategy)
@settings(max_examples=50)
def test_viatratraceability::petrinet_instantiation(instance):
    assert isinstance(instance, viatraTraceability::PetriNet)

@given(instance=viatraTraceability::DepToGSPN_strategy)
@settings(max_examples=50)
def test_viatratraceability::deptogspn_instantiation(instance):
    assert isinstance(instance, viatraTraceability::DepToGSPN)
