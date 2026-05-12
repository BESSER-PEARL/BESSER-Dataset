import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    dependability2stochasticpetrinet_PetriNet,
    TraceLink,
    dependability2stochasticpetrinet_RailwayContainer2PetriNet,
    dependability2stochasticpetrinet_Transition,
    dependability2stochasticpetrinet_Place,
    dependability2stochasticpetrinet_Dependability2StochasticPetriNetTrace,
    dependability2stochasticpetrinet_ErrorModel,
    PetriNetModuleTraceLink,
    dependability2stochasticpetrinet_ErrorModel2PetriNetModule,
    dependability2stochasticpetrinet_TraceLink,
    dependability2stochasticpetrinet_DependabilityModel,
    dependability2stochasticpetrinet_RailwayContainer,
    dependability2stochasticpetrinet_RequiredElement2Connection,
    dependability2stochasticpetrinet_Arc,
    dependability2stochasticpetrinet_Node,
    dependability2stochasticpetrinet_PetriNetModuleTraceLink,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_dependability2stochasticpetrinet_petrinet_is_not_abstract():
    assert not inspect.isabstract(dependability2stochasticpetrinet_PetriNet)


def test_dependability2stochasticpetrinet_petrinet_constructor_exists():
    assert callable(dependability2stochasticpetrinet_PetriNet.__init__)


def test_dependability2stochasticpetrinet_petrinet_constructor_args():
    sig = inspect.signature(dependability2stochasticpetrinet_PetriNet.__init__)
    params = list(sig.parameters.keys())



def test_tracelink_is_not_abstract():
    assert not inspect.isabstract(TraceLink)


def test_tracelink_constructor_exists():
    assert callable(TraceLink.__init__)


def test_tracelink_constructor_args():
    sig = inspect.signature(TraceLink.__init__)
    params = list(sig.parameters.keys())



def test_dependability2stochasticpetrinet_railwaycontainer2petrinet_is_not_abstract():
    assert not inspect.isabstract(dependability2stochasticpetrinet_RailwayContainer2PetriNet)


def test_dependability2stochasticpetrinet_railwaycontainer2petrinet_constructor_exists():
    assert callable(dependability2stochasticpetrinet_RailwayContainer2PetriNet.__init__)


def test_dependability2stochasticpetrinet_railwaycontainer2petrinet_constructor_args():
    sig = inspect.signature(dependability2stochasticpetrinet_RailwayContainer2PetriNet.__init__)
    params = list(sig.parameters.keys())



def test_dependability2stochasticpetrinet_transition_is_not_abstract():
    assert not inspect.isabstract(dependability2stochasticpetrinet_Transition)


def test_dependability2stochasticpetrinet_transition_constructor_exists():
    assert callable(dependability2stochasticpetrinet_Transition.__init__)


def test_dependability2stochasticpetrinet_transition_constructor_args():
    sig = inspect.signature(dependability2stochasticpetrinet_Transition.__init__)
    params = list(sig.parameters.keys())



def test_dependability2stochasticpetrinet_place_is_not_abstract():
    assert not inspect.isabstract(dependability2stochasticpetrinet_Place)


def test_dependability2stochasticpetrinet_place_constructor_exists():
    assert callable(dependability2stochasticpetrinet_Place.__init__)


def test_dependability2stochasticpetrinet_place_constructor_args():
    sig = inspect.signature(dependability2stochasticpetrinet_Place.__init__)
    params = list(sig.parameters.keys())



def test_dependability2stochasticpetrinet_dependability2stochasticpetrinettrace_is_not_abstract():
    assert not inspect.isabstract(dependability2stochasticpetrinet_Dependability2StochasticPetriNetTrace)


def test_dependability2stochasticpetrinet_dependability2stochasticpetrinettrace_constructor_exists():
    assert callable(dependability2stochasticpetrinet_Dependability2StochasticPetriNetTrace.__init__)


def test_dependability2stochasticpetrinet_dependability2stochasticpetrinettrace_constructor_args():
    sig = inspect.signature(dependability2stochasticpetrinet_Dependability2StochasticPetriNetTrace.__init__)
    params = list(sig.parameters.keys())



def test_dependability2stochasticpetrinet_errormodel_is_not_abstract():
    assert not inspect.isabstract(dependability2stochasticpetrinet_ErrorModel)


def test_dependability2stochasticpetrinet_errormodel_constructor_exists():
    assert callable(dependability2stochasticpetrinet_ErrorModel.__init__)


def test_dependability2stochasticpetrinet_errormodel_constructor_args():
    sig = inspect.signature(dependability2stochasticpetrinet_ErrorModel.__init__)
    params = list(sig.parameters.keys())



def test_petrinetmoduletracelink_is_not_abstract():
    assert not inspect.isabstract(PetriNetModuleTraceLink)


def test_petrinetmoduletracelink_constructor_exists():
    assert callable(PetriNetModuleTraceLink.__init__)


def test_petrinetmoduletracelink_constructor_args():
    sig = inspect.signature(PetriNetModuleTraceLink.__init__)
    params = list(sig.parameters.keys())



def test_dependability2stochasticpetrinet_errormodel2petrinetmodule_is_not_abstract():
    assert not inspect.isabstract(dependability2stochasticpetrinet_ErrorModel2PetriNetModule)


def test_dependability2stochasticpetrinet_errormodel2petrinetmodule_constructor_exists():
    assert callable(dependability2stochasticpetrinet_ErrorModel2PetriNetModule.__init__)


def test_dependability2stochasticpetrinet_errormodel2petrinetmodule_constructor_args():
    sig = inspect.signature(dependability2stochasticpetrinet_ErrorModel2PetriNetModule.__init__)
    params = list(sig.parameters.keys())



def test_dependability2stochasticpetrinet_tracelink_is_not_abstract():
    assert not inspect.isabstract(dependability2stochasticpetrinet_TraceLink)


def test_dependability2stochasticpetrinet_tracelink_constructor_exists():
    assert callable(dependability2stochasticpetrinet_TraceLink.__init__)


def test_dependability2stochasticpetrinet_tracelink_constructor_args():
    sig = inspect.signature(dependability2stochasticpetrinet_TraceLink.__init__)
    params = list(sig.parameters.keys())



def test_dependability2stochasticpetrinet_dependabilitymodel_is_not_abstract():
    assert not inspect.isabstract(dependability2stochasticpetrinet_DependabilityModel)


def test_dependability2stochasticpetrinet_dependabilitymodel_constructor_exists():
    assert callable(dependability2stochasticpetrinet_DependabilityModel.__init__)


def test_dependability2stochasticpetrinet_dependabilitymodel_constructor_args():
    sig = inspect.signature(dependability2stochasticpetrinet_DependabilityModel.__init__)
    params = list(sig.parameters.keys())



def test_dependability2stochasticpetrinet_railwaycontainer_is_not_abstract():
    assert not inspect.isabstract(dependability2stochasticpetrinet_RailwayContainer)


def test_dependability2stochasticpetrinet_railwaycontainer_constructor_exists():
    assert callable(dependability2stochasticpetrinet_RailwayContainer.__init__)


def test_dependability2stochasticpetrinet_railwaycontainer_constructor_args():
    sig = inspect.signature(dependability2stochasticpetrinet_RailwayContainer.__init__)
    params = list(sig.parameters.keys())



def test_dependability2stochasticpetrinet_requiredelement2connection_is_not_abstract():
    assert not inspect.isabstract(dependability2stochasticpetrinet_RequiredElement2Connection)


def test_dependability2stochasticpetrinet_requiredelement2connection_constructor_exists():
    assert callable(dependability2stochasticpetrinet_RequiredElement2Connection.__init__)


def test_dependability2stochasticpetrinet_requiredelement2connection_constructor_args():
    sig = inspect.signature(dependability2stochasticpetrinet_RequiredElement2Connection.__init__)
    params = list(sig.parameters.keys())



def test_dependability2stochasticpetrinet_arc_is_not_abstract():
    assert not inspect.isabstract(dependability2stochasticpetrinet_Arc)


def test_dependability2stochasticpetrinet_arc_constructor_exists():
    assert callable(dependability2stochasticpetrinet_Arc.__init__)


def test_dependability2stochasticpetrinet_arc_constructor_args():
    sig = inspect.signature(dependability2stochasticpetrinet_Arc.__init__)
    params = list(sig.parameters.keys())



def test_dependability2stochasticpetrinet_node_is_not_abstract():
    assert not inspect.isabstract(dependability2stochasticpetrinet_Node)


def test_dependability2stochasticpetrinet_node_constructor_exists():
    assert callable(dependability2stochasticpetrinet_Node.__init__)


def test_dependability2stochasticpetrinet_node_constructor_args():
    sig = inspect.signature(dependability2stochasticpetrinet_Node.__init__)
    params = list(sig.parameters.keys())



def test_dependability2stochasticpetrinet_petrinetmoduletracelink_is_not_abstract():
    assert not inspect.isabstract(dependability2stochasticpetrinet_PetriNetModuleTraceLink)


def test_dependability2stochasticpetrinet_petrinetmoduletracelink_constructor_exists():
    assert callable(dependability2stochasticpetrinet_PetriNetModuleTraceLink.__init__)


def test_dependability2stochasticpetrinet_petrinetmoduletracelink_constructor_args():
    sig = inspect.signature(dependability2stochasticpetrinet_PetriNetModuleTraceLink.__init__)
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
dependability2stochasticpetrinet_PetriNet_strategy = st.builds(
    dependability2stochasticpetrinet_PetriNet,
)
TraceLink_strategy = st.builds(
    TraceLink,
)
dependability2stochasticpetrinet_RailwayContainer2PetriNet_strategy = st.builds(
    dependability2stochasticpetrinet_RailwayContainer2PetriNet,
)
dependability2stochasticpetrinet_Transition_strategy = st.builds(
    dependability2stochasticpetrinet_Transition,
)
dependability2stochasticpetrinet_Place_strategy = st.builds(
    dependability2stochasticpetrinet_Place,
)
dependability2stochasticpetrinet_Dependability2StochasticPetriNetTrace_strategy = st.builds(
    dependability2stochasticpetrinet_Dependability2StochasticPetriNetTrace,
)
dependability2stochasticpetrinet_ErrorModel_strategy = st.builds(
    dependability2stochasticpetrinet_ErrorModel,
)
PetriNetModuleTraceLink_strategy = st.builds(
    PetriNetModuleTraceLink,
)
dependability2stochasticpetrinet_ErrorModel2PetriNetModule_strategy = st.builds(
    dependability2stochasticpetrinet_ErrorModel2PetriNetModule,
)
dependability2stochasticpetrinet_TraceLink_strategy = st.builds(
    dependability2stochasticpetrinet_TraceLink,
)
dependability2stochasticpetrinet_DependabilityModel_strategy = st.builds(
    dependability2stochasticpetrinet_DependabilityModel,
)
dependability2stochasticpetrinet_RailwayContainer_strategy = st.builds(
    dependability2stochasticpetrinet_RailwayContainer,
)
dependability2stochasticpetrinet_RequiredElement2Connection_strategy = st.builds(
    dependability2stochasticpetrinet_RequiredElement2Connection,
)
dependability2stochasticpetrinet_Arc_strategy = st.builds(
    dependability2stochasticpetrinet_Arc,
)
dependability2stochasticpetrinet_Node_strategy = st.builds(
    dependability2stochasticpetrinet_Node,
)
dependability2stochasticpetrinet_PetriNetModuleTraceLink_strategy = st.builds(
    dependability2stochasticpetrinet_PetriNetModuleTraceLink,
)

@given(instance=dependability2stochasticpetrinet_PetriNet_strategy)
@settings(max_examples=50)
def test_dependability2stochasticpetrinet_petrinet_instantiation(instance):
    assert isinstance(instance, dependability2stochasticpetrinet_PetriNet)

@given(instance=TraceLink_strategy)
@settings(max_examples=50)
def test_tracelink_instantiation(instance):
    assert isinstance(instance, TraceLink)

@given(instance=dependability2stochasticpetrinet_RailwayContainer2PetriNet_strategy)
@settings(max_examples=50)
def test_dependability2stochasticpetrinet_railwaycontainer2petrinet_instantiation(instance):
    assert isinstance(instance, dependability2stochasticpetrinet_RailwayContainer2PetriNet)

@given(instance=dependability2stochasticpetrinet_Transition_strategy)
@settings(max_examples=50)
def test_dependability2stochasticpetrinet_transition_instantiation(instance):
    assert isinstance(instance, dependability2stochasticpetrinet_Transition)

@given(instance=dependability2stochasticpetrinet_Place_strategy)
@settings(max_examples=50)
def test_dependability2stochasticpetrinet_place_instantiation(instance):
    assert isinstance(instance, dependability2stochasticpetrinet_Place)

@given(instance=dependability2stochasticpetrinet_Dependability2StochasticPetriNetTrace_strategy)
@settings(max_examples=50)
def test_dependability2stochasticpetrinet_dependability2stochasticpetrinettrace_instantiation(instance):
    assert isinstance(instance, dependability2stochasticpetrinet_Dependability2StochasticPetriNetTrace)

@given(instance=dependability2stochasticpetrinet_ErrorModel_strategy)
@settings(max_examples=50)
def test_dependability2stochasticpetrinet_errormodel_instantiation(instance):
    assert isinstance(instance, dependability2stochasticpetrinet_ErrorModel)

@given(instance=PetriNetModuleTraceLink_strategy)
@settings(max_examples=50)
def test_petrinetmoduletracelink_instantiation(instance):
    assert isinstance(instance, PetriNetModuleTraceLink)

@given(instance=dependability2stochasticpetrinet_ErrorModel2PetriNetModule_strategy)
@settings(max_examples=50)
def test_dependability2stochasticpetrinet_errormodel2petrinetmodule_instantiation(instance):
    assert isinstance(instance, dependability2stochasticpetrinet_ErrorModel2PetriNetModule)

@given(instance=dependability2stochasticpetrinet_TraceLink_strategy)
@settings(max_examples=50)
def test_dependability2stochasticpetrinet_tracelink_instantiation(instance):
    assert isinstance(instance, dependability2stochasticpetrinet_TraceLink)

@given(instance=dependability2stochasticpetrinet_DependabilityModel_strategy)
@settings(max_examples=50)
def test_dependability2stochasticpetrinet_dependabilitymodel_instantiation(instance):
    assert isinstance(instance, dependability2stochasticpetrinet_DependabilityModel)

@given(instance=dependability2stochasticpetrinet_RailwayContainer_strategy)
@settings(max_examples=50)
def test_dependability2stochasticpetrinet_railwaycontainer_instantiation(instance):
    assert isinstance(instance, dependability2stochasticpetrinet_RailwayContainer)

@given(instance=dependability2stochasticpetrinet_RequiredElement2Connection_strategy)
@settings(max_examples=50)
def test_dependability2stochasticpetrinet_requiredelement2connection_instantiation(instance):
    assert isinstance(instance, dependability2stochasticpetrinet_RequiredElement2Connection)

@given(instance=dependability2stochasticpetrinet_Arc_strategy)
@settings(max_examples=50)
def test_dependability2stochasticpetrinet_arc_instantiation(instance):
    assert isinstance(instance, dependability2stochasticpetrinet_Arc)

@given(instance=dependability2stochasticpetrinet_Node_strategy)
@settings(max_examples=50)
def test_dependability2stochasticpetrinet_node_instantiation(instance):
    assert isinstance(instance, dependability2stochasticpetrinet_Node)

@given(instance=dependability2stochasticpetrinet_PetriNetModuleTraceLink_strategy)
@settings(max_examples=50)
def test_dependability2stochasticpetrinet_petrinetmoduletracelink_instantiation(instance):
    assert isinstance(instance, dependability2stochasticpetrinet_PetriNetModuleTraceLink)
