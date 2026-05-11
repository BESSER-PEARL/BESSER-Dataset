import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    traceability::DeploymentElement,
    traceability::Identifiable,
    traceability::CPS2DeploymentTrace,
    traceability::Deployment,
    traceability::CyberPhysicalSystem,
    traceability::CPSToDeployment,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_traceability::deploymentelement_is_not_abstract():
    assert not inspect.isabstract(traceability::DeploymentElement)


def test_traceability::deploymentelement_constructor_exists():
    assert callable(traceability::DeploymentElement.__init__)


def test_traceability::deploymentelement_constructor_args():
    sig = inspect.signature(traceability::DeploymentElement.__init__)
    params = list(sig.parameters.keys())



def test_traceability::identifiable_is_not_abstract():
    assert not inspect.isabstract(traceability::Identifiable)


def test_traceability::identifiable_constructor_exists():
    assert callable(traceability::Identifiable.__init__)


def test_traceability::identifiable_constructor_args():
    sig = inspect.signature(traceability::Identifiable.__init__)
    params = list(sig.parameters.keys())



def test_traceability::cps2deploymenttrace_is_not_abstract():
    assert not inspect.isabstract(traceability::CPS2DeploymentTrace)


def test_traceability::cps2deploymenttrace_constructor_exists():
    assert callable(traceability::CPS2DeploymentTrace.__init__)


def test_traceability::cps2deploymenttrace_constructor_args():
    sig = inspect.signature(traceability::CPS2DeploymentTrace.__init__)
    params = list(sig.parameters.keys())



def test_traceability::deployment_is_not_abstract():
    assert not inspect.isabstract(traceability::Deployment)


def test_traceability::deployment_constructor_exists():
    assert callable(traceability::Deployment.__init__)


def test_traceability::deployment_constructor_args():
    sig = inspect.signature(traceability::Deployment.__init__)
    params = list(sig.parameters.keys())



def test_traceability::cyberphysicalsystem_is_not_abstract():
    assert not inspect.isabstract(traceability::CyberPhysicalSystem)


def test_traceability::cyberphysicalsystem_constructor_exists():
    assert callable(traceability::CyberPhysicalSystem.__init__)


def test_traceability::cyberphysicalsystem_constructor_args():
    sig = inspect.signature(traceability::CyberPhysicalSystem.__init__)
    params = list(sig.parameters.keys())



def test_traceability::cpstodeployment_is_not_abstract():
    assert not inspect.isabstract(traceability::CPSToDeployment)


def test_traceability::cpstodeployment_constructor_exists():
    assert callable(traceability::CPSToDeployment.__init__)


def test_traceability::cpstodeployment_constructor_args():
    sig = inspect.signature(traceability::CPSToDeployment.__init__)
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
traceability::DeploymentElement_strategy = st.builds(
    traceability::DeploymentElement,
)
traceability::Identifiable_strategy = st.builds(
    traceability::Identifiable,
)
traceability::CPS2DeploymentTrace_strategy = st.builds(
    traceability::CPS2DeploymentTrace,
)
traceability::Deployment_strategy = st.builds(
    traceability::Deployment,
)
traceability::CyberPhysicalSystem_strategy = st.builds(
    traceability::CyberPhysicalSystem,
)
traceability::CPSToDeployment_strategy = st.builds(
    traceability::CPSToDeployment,
)

@given(instance=traceability::DeploymentElement_strategy)
@settings(max_examples=50)
def test_traceability::deploymentelement_instantiation(instance):
    assert isinstance(instance, traceability::DeploymentElement)

@given(instance=traceability::Identifiable_strategy)
@settings(max_examples=50)
def test_traceability::identifiable_instantiation(instance):
    assert isinstance(instance, traceability::Identifiable)

@given(instance=traceability::CPS2DeploymentTrace_strategy)
@settings(max_examples=50)
def test_traceability::cps2deploymenttrace_instantiation(instance):
    assert isinstance(instance, traceability::CPS2DeploymentTrace)

@given(instance=traceability::Deployment_strategy)
@settings(max_examples=50)
def test_traceability::deployment_instantiation(instance):
    assert isinstance(instance, traceability::Deployment)

@given(instance=traceability::CyberPhysicalSystem_strategy)
@settings(max_examples=50)
def test_traceability::cyberphysicalsystem_instantiation(instance):
    assert isinstance(instance, traceability::CyberPhysicalSystem)

@given(instance=traceability::CPSToDeployment_strategy)
@settings(max_examples=50)
def test_traceability::cpstodeployment_instantiation(instance):
    assert isinstance(instance, traceability::CPSToDeployment)
