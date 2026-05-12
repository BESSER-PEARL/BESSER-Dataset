import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    traceability_DeploymentElement,
    traceability_Identifiable,
    traceability_CPS2DeploymentTrace,
    traceability_Deployment,
    traceability_CyberPhysicalSystem,
    traceability_CPSToDeployment,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_traceability_deploymentelement_is_not_abstract():
    assert not inspect.isabstract(traceability_DeploymentElement)


def test_traceability_deploymentelement_constructor_exists():
    assert callable(traceability_DeploymentElement.__init__)


def test_traceability_deploymentelement_constructor_args():
    sig = inspect.signature(traceability_DeploymentElement.__init__)
    params = list(sig.parameters.keys())



def test_traceability_identifiable_is_not_abstract():
    assert not inspect.isabstract(traceability_Identifiable)


def test_traceability_identifiable_constructor_exists():
    assert callable(traceability_Identifiable.__init__)


def test_traceability_identifiable_constructor_args():
    sig = inspect.signature(traceability_Identifiable.__init__)
    params = list(sig.parameters.keys())



def test_traceability_cps2deploymenttrace_is_not_abstract():
    assert not inspect.isabstract(traceability_CPS2DeploymentTrace)


def test_traceability_cps2deploymenttrace_constructor_exists():
    assert callable(traceability_CPS2DeploymentTrace.__init__)


def test_traceability_cps2deploymenttrace_constructor_args():
    sig = inspect.signature(traceability_CPS2DeploymentTrace.__init__)
    params = list(sig.parameters.keys())



def test_traceability_deployment_is_not_abstract():
    assert not inspect.isabstract(traceability_Deployment)


def test_traceability_deployment_constructor_exists():
    assert callable(traceability_Deployment.__init__)


def test_traceability_deployment_constructor_args():
    sig = inspect.signature(traceability_Deployment.__init__)
    params = list(sig.parameters.keys())



def test_traceability_cyberphysicalsystem_is_not_abstract():
    assert not inspect.isabstract(traceability_CyberPhysicalSystem)


def test_traceability_cyberphysicalsystem_constructor_exists():
    assert callable(traceability_CyberPhysicalSystem.__init__)


def test_traceability_cyberphysicalsystem_constructor_args():
    sig = inspect.signature(traceability_CyberPhysicalSystem.__init__)
    params = list(sig.parameters.keys())



def test_traceability_cpstodeployment_is_not_abstract():
    assert not inspect.isabstract(traceability_CPSToDeployment)


def test_traceability_cpstodeployment_constructor_exists():
    assert callable(traceability_CPSToDeployment.__init__)


def test_traceability_cpstodeployment_constructor_args():
    sig = inspect.signature(traceability_CPSToDeployment.__init__)
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
traceability_DeploymentElement_strategy = st.builds(
    traceability_DeploymentElement,
)
traceability_Identifiable_strategy = st.builds(
    traceability_Identifiable,
)
traceability_CPS2DeploymentTrace_strategy = st.builds(
    traceability_CPS2DeploymentTrace,
)
traceability_Deployment_strategy = st.builds(
    traceability_Deployment,
)
traceability_CyberPhysicalSystem_strategy = st.builds(
    traceability_CyberPhysicalSystem,
)
traceability_CPSToDeployment_strategy = st.builds(
    traceability_CPSToDeployment,
)

@given(instance=traceability_DeploymentElement_strategy)
@settings(max_examples=50)
def test_traceability_deploymentelement_instantiation(instance):
    assert isinstance(instance, traceability_DeploymentElement)

@given(instance=traceability_Identifiable_strategy)
@settings(max_examples=50)
def test_traceability_identifiable_instantiation(instance):
    assert isinstance(instance, traceability_Identifiable)

@given(instance=traceability_CPS2DeploymentTrace_strategy)
@settings(max_examples=50)
def test_traceability_cps2deploymenttrace_instantiation(instance):
    assert isinstance(instance, traceability_CPS2DeploymentTrace)

@given(instance=traceability_Deployment_strategy)
@settings(max_examples=50)
def test_traceability_deployment_instantiation(instance):
    assert isinstance(instance, traceability_Deployment)

@given(instance=traceability_CyberPhysicalSystem_strategy)
@settings(max_examples=50)
def test_traceability_cyberphysicalsystem_instantiation(instance):
    assert isinstance(instance, traceability_CyberPhysicalSystem)

@given(instance=traceability_CPSToDeployment_strategy)
@settings(max_examples=50)
def test_traceability_cpstodeployment_instantiation(instance):
    assert isinstance(instance, traceability_CPSToDeployment)
