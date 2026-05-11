import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    dependability2stochasticpetrinet::ErrorModel,
    PetriNetModuleTraceLink,
    dependability2stochasticpetrinet::ErrorModel2PetriNetModule,
    dependability2stochasticpetrinet::TraceLink,
    dependability2stochasticpetrinet::DependabilityModel,
    dependability2stochasticpetrinet::RailwayContainer,
    dependability2stochasticpetrinet::RequiredElement2Connection,
    dependability2stochasticpetrinet::Arc,
    dependability2stochasticpetrinet::Node,
    dependability2stochasticpetrinet::PetriNet,
    TraceLink,
    dependability2stochasticpetrinet::PetriNetModuleTraceLink,
    dependability2stochasticpetrinet::RailwayContainer2PetriNet,
    dependability2stochasticpetrinet::Transition,
    dependability2stochasticpetrinet::Place,
    dependability2stochasticpetrinet::Dependability2StochasticPetriNetTrace,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_dependability2stochasticpetrinet::errormodel_is_not_abstract():
    assert not inspect.isabstract(dependability2stochasticpetrinet::ErrorModel)


def test_dependability2stochasticpetrinet::errormodel_constructor_exists():
    assert callable(dependability2stochasticpetrinet::ErrorModel.__init__)


def test_dependability2stochasticpetrinet::errormodel_constructor_args():
    sig = inspect.signature(dependability2stochasticpetrinet::ErrorModel.__init__)
    params = list(sig.parameters.keys())



def test_petrinetmoduletracelink_is_not_abstract():
    assert not inspect.isabstract(PetriNetModuleTraceLink)


def test_petrinetmoduletracelink_constructor_exists():
    assert callable(PetriNetModuleTraceLink.__init__)


def test_petrinetmoduletracelink_constructor_args():
    sig = inspect.signature(PetriNetModuleTraceLink.__init__)
    params = list(sig.parameters.keys())



def test_dependability2stochasticpetrinet::errormodel2petrinetmodule_is_not_abstract():
    assert not inspect.isabstract(dependability2stochasticpetrinet::ErrorModel2PetriNetModule)


def test_dependability2stochasticpetrinet::errormodel2petrinetmodule_constructor_exists():
    assert callable(dependability2stochasticpetrinet::ErrorModel2PetriNetModule.__init__)


def test_dependability2stochasticpetrinet::errormodel2petrinetmodule_constructor_args():
    sig = inspect.signature(dependability2stochasticpetrinet::ErrorModel2PetriNetModule.__init__)
    params = list(sig.parameters.keys())



def test_dependability2stochasticpetrinet::tracelink_is_not_abstract():
    assert not inspect.isabstract(dependability2stochasticpetrinet::TraceLink)


def test_dependability2stochasticpetrinet::tracelink_constructor_exists():
    assert callable(dependability2stochasticpetrinet::TraceLink.__init__)


def test_dependability2stochasticpetrinet::tracelink_constructor_args():
    sig = inspect.signature(dependability2stochasticpetrinet::TraceLink.__init__)
    params = list(sig.parameters.keys())



def test_dependability2stochasticpetrinet::dependabilitymodel_is_not_abstract():
    assert not inspect.isabstract(dependability2stochasticpetrinet::DependabilityModel)


def test_dependability2stochasticpetrinet::dependabilitymodel_constructor_exists():
    assert callable(dependability2stochasticpetrinet::DependabilityModel.__init__)


def test_dependability2stochasticpetrinet::dependabilitymodel_constructor_args():
    sig = inspect.signature(dependability2stochasticpetrinet::DependabilityModel.__init__)
    params = list(sig.parameters.keys())



def test_dependability2stochasticpetrinet::railwaycontainer_is_not_abstract():
    assert not inspect.isabstract(dependability2stochasticpetrinet::RailwayContainer)


def test_dependability2stochasticpetrinet::railwaycontainer_constructor_exists():
    assert callable(dependability2stochasticpetrinet::RailwayContainer.__init__)


def test_dependability2stochasticpetrinet::railwaycontainer_constructor_args():
    sig = inspect.signature(dependability2stochasticpetrinet::RailwayContainer.__init__)
    params = list(sig.parameters.keys())



def test_dependability2stochasticpetrinet::requiredelement2connection_is_not_abstract():
    assert not inspect.isabstract(dependability2stochasticpetrinet::RequiredElement2Connection)


def test_dependability2stochasticpetrinet::requiredelement2connection_constructor_exists():
    assert callable(dependability2stochasticpetrinet::RequiredElement2Connection.__init__)


def test_dependability2stochasticpetrinet::requiredelement2connection_constructor_args():
    sig = inspect.signature(dependability2stochasticpetrinet::RequiredElement2Connection.__init__)
    params = list(sig.parameters.keys())



def test_dependability2stochasticpetrinet::arc_is_not_abstract():
    assert not inspect.isabstract(dependability2stochasticpetrinet::Arc)


def test_dependability2stochasticpetrinet::arc_constructor_exists():
    assert callable(dependability2stochasticpetrinet::Arc.__init__)


def test_dependability2stochasticpetrinet::arc_constructor_args():
    sig = inspect.signature(dependability2stochasticpetrinet::Arc.__init__)
    params = list(sig.parameters.keys())



def test_dependability2stochasticpetrinet::node_is_not_abstract():
    assert not inspect.isabstract(dependability2stochasticpetrinet::Node)


def test_dependability2stochasticpetrinet::node_constructor_exists():
    assert callable(dependability2stochasticpetrinet::Node.__init__)


def test_dependability2stochasticpetrinet::node_constructor_args():
    sig = inspect.signature(dependability2stochasticpetrinet::Node.__init__)
    params = list(sig.parameters.keys())



def test_dependability2stochasticpetrinet::petrinet_is_not_abstract():
    assert not inspect.isabstract(dependability2stochasticpetrinet::PetriNet)


def test_dependability2stochasticpetrinet::petrinet_constructor_exists():
    assert callable(dependability2stochasticpetrinet::PetriNet.__init__)


def test_dependability2stochasticpetrinet::petrinet_constructor_args():
    sig = inspect.signature(dependability2stochasticpetrinet::PetriNet.__init__)
    params = list(sig.parameters.keys())



def test_tracelink_is_not_abstract():
    assert not inspect.isabstract(TraceLink)


def test_tracelink_constructor_exists():
    assert callable(TraceLink.__init__)


def test_tracelink_constructor_args():
    sig = inspect.signature(TraceLink.__init__)
    params = list(sig.parameters.keys())



def test_dependability2stochasticpetrinet::petrinetmoduletracelink_is_not_abstract():
    assert not inspect.isabstract(dependability2stochasticpetrinet::PetriNetModuleTraceLink)


def test_dependability2stochasticpetrinet::petrinetmoduletracelink_constructor_exists():
    assert callable(dependability2stochasticpetrinet::PetriNetModuleTraceLink.__init__)


def test_dependability2stochasticpetrinet::petrinetmoduletracelink_constructor_args():
    sig = inspect.signature(dependability2stochasticpetrinet::PetriNetModuleTraceLink.__init__)
    params = list(sig.parameters.keys())



def test_dependability2stochasticpetrinet::railwaycontainer2petrinet_is_not_abstract():
    assert not inspect.isabstract(dependability2stochasticpetrinet::RailwayContainer2PetriNet)


def test_dependability2stochasticpetrinet::railwaycontainer2petrinet_constructor_exists():
    assert callable(dependability2stochasticpetrinet::RailwayContainer2PetriNet.__init__)


def test_dependability2stochasticpetrinet::railwaycontainer2petrinet_constructor_args():
    sig = inspect.signature(dependability2stochasticpetrinet::RailwayContainer2PetriNet.__init__)
    params = list(sig.parameters.keys())



def test_dependability2stochasticpetrinet::transition_is_not_abstract():
    assert not inspect.isabstract(dependability2stochasticpetrinet::Transition)


def test_dependability2stochasticpetrinet::transition_constructor_exists():
    assert callable(dependability2stochasticpetrinet::Transition.__init__)


def test_dependability2stochasticpetrinet::transition_constructor_args():
    sig = inspect.signature(dependability2stochasticpetrinet::Transition.__init__)
    params = list(sig.parameters.keys())



def test_dependability2stochasticpetrinet::place_is_not_abstract():
    assert not inspect.isabstract(dependability2stochasticpetrinet::Place)


def test_dependability2stochasticpetrinet::place_constructor_exists():
    assert callable(dependability2stochasticpetrinet::Place.__init__)


def test_dependability2stochasticpetrinet::place_constructor_args():
    sig = inspect.signature(dependability2stochasticpetrinet::Place.__init__)
    params = list(sig.parameters.keys())



def test_dependability2stochasticpetrinet::dependability2stochasticpetrinettrace_is_not_abstract():
    assert not inspect.isabstract(dependability2stochasticpetrinet::Dependability2StochasticPetriNetTrace)


def test_dependability2stochasticpetrinet::dependability2stochasticpetrinettrace_constructor_exists():
    assert callable(dependability2stochasticpetrinet::Dependability2StochasticPetriNetTrace.__init__)


def test_dependability2stochasticpetrinet::dependability2stochasticpetrinettrace_constructor_args():
    sig = inspect.signature(dependability2stochasticpetrinet::Dependability2StochasticPetriNetTrace.__init__)
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
dependability2stochasticpetrinet::ErrorModel_strategy = st.builds(
    dependability2stochasticpetrinet::ErrorModel,
)
PetriNetModuleTraceLink_strategy = st.builds(
    PetriNetModuleTraceLink,
)
dependability2stochasticpetrinet::ErrorModel2PetriNetModule_strategy = st.builds(
    dependability2stochasticpetrinet::ErrorModel2PetriNetModule,
)
dependability2stochasticpetrinet::TraceLink_strategy = st.builds(
    dependability2stochasticpetrinet::TraceLink,
)
dependability2stochasticpetrinet::DependabilityModel_strategy = st.builds(
    dependability2stochasticpetrinet::DependabilityModel,
)
dependability2stochasticpetrinet::RailwayContainer_strategy = st.builds(
    dependability2stochasticpetrinet::RailwayContainer,
)
dependability2stochasticpetrinet::RequiredElement2Connection_strategy = st.builds(
    dependability2stochasticpetrinet::RequiredElement2Connection,
)
dependability2stochasticpetrinet::Arc_strategy = st.builds(
    dependability2stochasticpetrinet::Arc,
)
dependability2stochasticpetrinet::Node_strategy = st.builds(
    dependability2stochasticpetrinet::Node,
)
dependability2stochasticpetrinet::PetriNet_strategy = st.builds(
    dependability2stochasticpetrinet::PetriNet,
)
TraceLink_strategy = st.builds(
    TraceLink,
)
dependability2stochasticpetrinet::PetriNetModuleTraceLink_strategy = st.builds(
    dependability2stochasticpetrinet::PetriNetModuleTraceLink,
)
dependability2stochasticpetrinet::RailwayContainer2PetriNet_strategy = st.builds(
    dependability2stochasticpetrinet::RailwayContainer2PetriNet,
)
dependability2stochasticpetrinet::Transition_strategy = st.builds(
    dependability2stochasticpetrinet::Transition,
)
dependability2stochasticpetrinet::Place_strategy = st.builds(
    dependability2stochasticpetrinet::Place,
)
dependability2stochasticpetrinet::Dependability2StochasticPetriNetTrace_strategy = st.builds(
    dependability2stochasticpetrinet::Dependability2StochasticPetriNetTrace,
)

@given(instance=dependability2stochasticpetrinet::ErrorModel_strategy)
@settings(max_examples=50)
def test_dependability2stochasticpetrinet::errormodel_instantiation(instance):
    assert isinstance(instance, dependability2stochasticpetrinet::ErrorModel)

@given(instance=PetriNetModuleTraceLink_strategy)
@settings(max_examples=50)
def test_petrinetmoduletracelink_instantiation(instance):
    assert isinstance(instance, PetriNetModuleTraceLink)

@given(instance=dependability2stochasticpetrinet::ErrorModel2PetriNetModule_strategy)
@settings(max_examples=50)
def test_dependability2stochasticpetrinet::errormodel2petrinetmodule_instantiation(instance):
    assert isinstance(instance, dependability2stochasticpetrinet::ErrorModel2PetriNetModule)

@given(instance=dependability2stochasticpetrinet::TraceLink_strategy)
@settings(max_examples=50)
def test_dependability2stochasticpetrinet::tracelink_instantiation(instance):
    assert isinstance(instance, dependability2stochasticpetrinet::TraceLink)

@given(instance=dependability2stochasticpetrinet::DependabilityModel_strategy)
@settings(max_examples=50)
def test_dependability2stochasticpetrinet::dependabilitymodel_instantiation(instance):
    assert isinstance(instance, dependability2stochasticpetrinet::DependabilityModel)

@given(instance=dependability2stochasticpetrinet::RailwayContainer_strategy)
@settings(max_examples=50)
def test_dependability2stochasticpetrinet::railwaycontainer_instantiation(instance):
    assert isinstance(instance, dependability2stochasticpetrinet::RailwayContainer)

@given(instance=dependability2stochasticpetrinet::RequiredElement2Connection_strategy)
@settings(max_examples=50)
def test_dependability2stochasticpetrinet::requiredelement2connection_instantiation(instance):
    assert isinstance(instance, dependability2stochasticpetrinet::RequiredElement2Connection)

@given(instance=dependability2stochasticpetrinet::Arc_strategy)
@settings(max_examples=50)
def test_dependability2stochasticpetrinet::arc_instantiation(instance):
    assert isinstance(instance, dependability2stochasticpetrinet::Arc)

@given(instance=dependability2stochasticpetrinet::Node_strategy)
@settings(max_examples=50)
def test_dependability2stochasticpetrinet::node_instantiation(instance):
    assert isinstance(instance, dependability2stochasticpetrinet::Node)

@given(instance=dependability2stochasticpetrinet::PetriNet_strategy)
@settings(max_examples=50)
def test_dependability2stochasticpetrinet::petrinet_instantiation(instance):
    assert isinstance(instance, dependability2stochasticpetrinet::PetriNet)

@given(instance=TraceLink_strategy)
@settings(max_examples=50)
def test_tracelink_instantiation(instance):
    assert isinstance(instance, TraceLink)

@given(instance=dependability2stochasticpetrinet::PetriNetModuleTraceLink_strategy)
@settings(max_examples=50)
def test_dependability2stochasticpetrinet::petrinetmoduletracelink_instantiation(instance):
    assert isinstance(instance, dependability2stochasticpetrinet::PetriNetModuleTraceLink)

@given(instance=dependability2stochasticpetrinet::RailwayContainer2PetriNet_strategy)
@settings(max_examples=50)
def test_dependability2stochasticpetrinet::railwaycontainer2petrinet_instantiation(instance):
    assert isinstance(instance, dependability2stochasticpetrinet::RailwayContainer2PetriNet)

@given(instance=dependability2stochasticpetrinet::Transition_strategy)
@settings(max_examples=50)
def test_dependability2stochasticpetrinet::transition_instantiation(instance):
    assert isinstance(instance, dependability2stochasticpetrinet::Transition)

@given(instance=dependability2stochasticpetrinet::Place_strategy)
@settings(max_examples=50)
def test_dependability2stochasticpetrinet::place_instantiation(instance):
    assert isinstance(instance, dependability2stochasticpetrinet::Place)

@given(instance=dependability2stochasticpetrinet::Dependability2StochasticPetriNetTrace_strategy)
@settings(max_examples=50)
def test_dependability2stochasticpetrinet::dependability2stochasticpetrinettrace_instantiation(instance):
    assert isinstance(instance, dependability2stochasticpetrinet::Dependability2StochasticPetriNetTrace)
