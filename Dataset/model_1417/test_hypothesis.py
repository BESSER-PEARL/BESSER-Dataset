import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    EModelElement,
    sam::IdentifiedItem,
    sam::Model,
    Flow,
    sam::DataFlow,
    sam::ControlFlow,
    SynchronisationGate,
    sam::Decomposition,
    sam::Composition,
    Port,
    sam::ControlPort,
    sam::OutputPort,
    OutputPort,
    sam::InputPort,
    DataPort,
    sam::OutDataPort,
    IdentifiedItem,
    sam::SynchronisationGate,
    sam::NamedItem,
    AbstractState,
    sam::MacroState,
    sam::State,
    State,
    sam::InitialState,
    ModelContent,
    sam::System,
    sam::Automaton,
    sam::Transition,
    NamedItem,
    sam::DataStore,
    sam::MultiPort,
    sam::Flow,
    sam::ModelContent,
    sam::Port,
    sam::AbstractState,
    InputPort,
    sam::InDataPort,
    ControlPort,
    sam::OutControlPort,
    sam::InControlPort,
    sam::DataPort,
    DataType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_emodelelement_is_not_abstract():
    assert not inspect.isabstract(EModelElement)


def test_emodelelement_constructor_exists():
    assert callable(EModelElement.__init__)


def test_emodelelement_constructor_args():
    sig = inspect.signature(EModelElement.__init__)
    params = list(sig.parameters.keys())



def test_sam::identifieditem_is_not_abstract():
    assert not inspect.isabstract(sam::IdentifiedItem)


def test_sam::identifieditem_constructor_exists():
    assert callable(sam::IdentifiedItem.__init__)


def test_sam::identifieditem_constructor_args():
    sig = inspect.signature(sam::IdentifiedItem.__init__)
    params = list(sig.parameters.keys())
    assert "requirements" in params, "Missing parameter 'requirements'"
    assert "comment" in params, "Missing parameter 'comment'"

def test_sam::identifieditem_has_requirements():
    assert hasattr(sam::IdentifiedItem, "requirements")
    descriptor = None
    for klass in sam::IdentifiedItem.__mro__:
        if "requirements" in klass.__dict__:
            descriptor = klass.__dict__["requirements"]
            break
    assert isinstance(descriptor, property)

def test_sam::identifieditem_has_comment():
    assert hasattr(sam::IdentifiedItem, "comment")
    descriptor = None
    for klass in sam::IdentifiedItem.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_sam::model_is_not_abstract():
    assert not inspect.isabstract(sam::Model)


def test_sam::model_constructor_exists():
    assert callable(sam::Model.__init__)


def test_sam::model_constructor_args():
    sig = inspect.signature(sam::Model.__init__)
    params = list(sig.parameters.keys())



def test_flow_is_not_abstract():
    assert not inspect.isabstract(Flow)


def test_flow_constructor_exists():
    assert callable(Flow.__init__)


def test_flow_constructor_args():
    sig = inspect.signature(Flow.__init__)
    params = list(sig.parameters.keys())



def test_sam::dataflow_is_not_abstract():
    assert not inspect.isabstract(sam::DataFlow)


def test_sam::dataflow_constructor_exists():
    assert callable(sam::DataFlow.__init__)


def test_sam::dataflow_constructor_args():
    sig = inspect.signature(sam::DataFlow.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_sam::dataflow_has_type():
    assert hasattr(sam::DataFlow, "type")
    descriptor = None
    for klass in sam::DataFlow.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_sam::controlflow_is_not_abstract():
    assert not inspect.isabstract(sam::ControlFlow)


def test_sam::controlflow_constructor_exists():
    assert callable(sam::ControlFlow.__init__)


def test_sam::controlflow_constructor_args():
    sig = inspect.signature(sam::ControlFlow.__init__)
    params = list(sig.parameters.keys())



def test_synchronisationgate_is_not_abstract():
    assert not inspect.isabstract(SynchronisationGate)


def test_synchronisationgate_constructor_exists():
    assert callable(SynchronisationGate.__init__)


def test_synchronisationgate_constructor_args():
    sig = inspect.signature(SynchronisationGate.__init__)
    params = list(sig.parameters.keys())



def test_sam::decomposition_is_not_abstract():
    assert not inspect.isabstract(sam::Decomposition)


def test_sam::decomposition_constructor_exists():
    assert callable(sam::Decomposition.__init__)


def test_sam::decomposition_constructor_args():
    sig = inspect.signature(sam::Decomposition.__init__)
    params = list(sig.parameters.keys())



def test_sam::composition_is_not_abstract():
    assert not inspect.isabstract(sam::Composition)


def test_sam::composition_constructor_exists():
    assert callable(sam::Composition.__init__)


def test_sam::composition_constructor_args():
    sig = inspect.signature(sam::Composition.__init__)
    params = list(sig.parameters.keys())



def test_port_is_not_abstract():
    assert not inspect.isabstract(Port)


def test_port_constructor_exists():
    assert callable(Port.__init__)


def test_port_constructor_args():
    sig = inspect.signature(Port.__init__)
    params = list(sig.parameters.keys())



def test_sam::controlport_is_not_abstract():
    assert not inspect.isabstract(sam::ControlPort)


def test_sam::controlport_constructor_exists():
    assert callable(sam::ControlPort.__init__)


def test_sam::controlport_constructor_args():
    sig = inspect.signature(sam::ControlPort.__init__)
    params = list(sig.parameters.keys())



def test_sam::outputport_is_not_abstract():
    assert not inspect.isabstract(sam::OutputPort)


def test_sam::outputport_constructor_exists():
    assert callable(sam::OutputPort.__init__)


def test_sam::outputport_constructor_args():
    sig = inspect.signature(sam::OutputPort.__init__)
    params = list(sig.parameters.keys())



def test_outputport_is_not_abstract():
    assert not inspect.isabstract(OutputPort)


def test_outputport_constructor_exists():
    assert callable(OutputPort.__init__)


def test_outputport_constructor_args():
    sig = inspect.signature(OutputPort.__init__)
    params = list(sig.parameters.keys())



def test_sam::inputport_is_not_abstract():
    assert not inspect.isabstract(sam::InputPort)


def test_sam::inputport_constructor_exists():
    assert callable(sam::InputPort.__init__)


def test_sam::inputport_constructor_args():
    sig = inspect.signature(sam::InputPort.__init__)
    params = list(sig.parameters.keys())



def test_dataport_is_not_abstract():
    assert not inspect.isabstract(DataPort)


def test_dataport_constructor_exists():
    assert callable(DataPort.__init__)


def test_dataport_constructor_args():
    sig = inspect.signature(DataPort.__init__)
    params = list(sig.parameters.keys())



def test_sam::outdataport_is_not_abstract():
    assert not inspect.isabstract(sam::OutDataPort)


def test_sam::outdataport_constructor_exists():
    assert callable(sam::OutDataPort.__init__)


def test_sam::outdataport_constructor_args():
    sig = inspect.signature(sam::OutDataPort.__init__)
    params = list(sig.parameters.keys())



def test_identifieditem_is_not_abstract():
    assert not inspect.isabstract(IdentifiedItem)


def test_identifieditem_constructor_exists():
    assert callable(IdentifiedItem.__init__)


def test_identifieditem_constructor_args():
    sig = inspect.signature(IdentifiedItem.__init__)
    params = list(sig.parameters.keys())



def test_sam::synchronisationgate_is_not_abstract():
    assert not inspect.isabstract(sam::SynchronisationGate)


def test_sam::synchronisationgate_constructor_exists():
    assert callable(sam::SynchronisationGate.__init__)


def test_sam::synchronisationgate_constructor_args():
    sig = inspect.signature(sam::SynchronisationGate.__init__)
    params = list(sig.parameters.keys())



def test_sam::nameditem_is_not_abstract():
    assert not inspect.isabstract(sam::NamedItem)


def test_sam::nameditem_constructor_exists():
    assert callable(sam::NamedItem.__init__)


def test_sam::nameditem_constructor_args():
    sig = inspect.signature(sam::NamedItem.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sam::nameditem_has_name():
    assert hasattr(sam::NamedItem, "name")
    descriptor = None
    for klass in sam::NamedItem.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_abstractstate_is_not_abstract():
    assert not inspect.isabstract(AbstractState)


def test_abstractstate_constructor_exists():
    assert callable(AbstractState.__init__)


def test_abstractstate_constructor_args():
    sig = inspect.signature(AbstractState.__init__)
    params = list(sig.parameters.keys())



def test_sam::macrostate_is_not_abstract():
    assert not inspect.isabstract(sam::MacroState)


def test_sam::macrostate_constructor_exists():
    assert callable(sam::MacroState.__init__)


def test_sam::macrostate_constructor_args():
    sig = inspect.signature(sam::MacroState.__init__)
    params = list(sig.parameters.keys())



def test_sam::state_is_not_abstract():
    assert not inspect.isabstract(sam::State)


def test_sam::state_constructor_exists():
    assert callable(sam::State.__init__)


def test_sam::state_constructor_args():
    sig = inspect.signature(sam::State.__init__)
    params = list(sig.parameters.keys())



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_sam::initialstate_is_not_abstract():
    assert not inspect.isabstract(sam::InitialState)


def test_sam::initialstate_constructor_exists():
    assert callable(sam::InitialState.__init__)


def test_sam::initialstate_constructor_args():
    sig = inspect.signature(sam::InitialState.__init__)
    params = list(sig.parameters.keys())



def test_modelcontent_is_not_abstract():
    assert not inspect.isabstract(ModelContent)


def test_modelcontent_constructor_exists():
    assert callable(ModelContent.__init__)


def test_modelcontent_constructor_args():
    sig = inspect.signature(ModelContent.__init__)
    params = list(sig.parameters.keys())



def test_sam::system_is_not_abstract():
    assert not inspect.isabstract(sam::System)


def test_sam::system_constructor_exists():
    assert callable(sam::System.__init__)


def test_sam::system_constructor_args():
    sig = inspect.signature(sam::System.__init__)
    params = list(sig.parameters.keys())



def test_sam::automaton_is_not_abstract():
    assert not inspect.isabstract(sam::Automaton)


def test_sam::automaton_constructor_exists():
    assert callable(sam::Automaton.__init__)


def test_sam::automaton_constructor_args():
    sig = inspect.signature(sam::Automaton.__init__)
    params = list(sig.parameters.keys())



def test_sam::transition_is_not_abstract():
    assert not inspect.isabstract(sam::Transition)


def test_sam::transition_constructor_exists():
    assert callable(sam::Transition.__init__)


def test_sam::transition_constructor_args():
    sig = inspect.signature(sam::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "priority" in params, "Missing parameter 'priority'"
    assert "emission" in params, "Missing parameter 'emission'"
    assert "condition" in params, "Missing parameter 'condition'"

def test_sam::transition_has_priority():
    assert hasattr(sam::Transition, "priority")
    descriptor = None
    for klass in sam::Transition.__mro__:
        if "priority" in klass.__dict__:
            descriptor = klass.__dict__["priority"]
            break
    assert isinstance(descriptor, property)

def test_sam::transition_has_emission():
    assert hasattr(sam::Transition, "emission")
    descriptor = None
    for klass in sam::Transition.__mro__:
        if "emission" in klass.__dict__:
            descriptor = klass.__dict__["emission"]
            break
    assert isinstance(descriptor, property)

def test_sam::transition_has_condition():
    assert hasattr(sam::Transition, "condition")
    descriptor = None
    for klass in sam::Transition.__mro__:
        if "condition" in klass.__dict__:
            descriptor = klass.__dict__["condition"]
            break
    assert isinstance(descriptor, property)



def test_nameditem_is_not_abstract():
    assert not inspect.isabstract(NamedItem)


def test_nameditem_constructor_exists():
    assert callable(NamedItem.__init__)


def test_nameditem_constructor_args():
    sig = inspect.signature(NamedItem.__init__)
    params = list(sig.parameters.keys())



def test_sam::datastore_is_not_abstract():
    assert not inspect.isabstract(sam::DataStore)


def test_sam::datastore_constructor_exists():
    assert callable(sam::DataStore.__init__)


def test_sam::datastore_constructor_args():
    sig = inspect.signature(sam::DataStore.__init__)
    params = list(sig.parameters.keys())



def test_sam::multiport_is_not_abstract():
    assert not inspect.isabstract(sam::MultiPort)


def test_sam::multiport_constructor_exists():
    assert callable(sam::MultiPort.__init__)


def test_sam::multiport_constructor_args():
    sig = inspect.signature(sam::MultiPort.__init__)
    params = list(sig.parameters.keys())



def test_sam::flow_is_not_abstract():
    assert not inspect.isabstract(sam::Flow)


def test_sam::flow_constructor_exists():
    assert callable(sam::Flow.__init__)


def test_sam::flow_constructor_args():
    sig = inspect.signature(sam::Flow.__init__)
    params = list(sig.parameters.keys())



def test_sam::modelcontent_is_not_abstract():
    assert not inspect.isabstract(sam::ModelContent)


def test_sam::modelcontent_constructor_exists():
    assert callable(sam::ModelContent.__init__)


def test_sam::modelcontent_constructor_args():
    sig = inspect.signature(sam::ModelContent.__init__)
    params = list(sig.parameters.keys())



def test_sam::port_is_not_abstract():
    assert not inspect.isabstract(sam::Port)


def test_sam::port_constructor_exists():
    assert callable(sam::Port.__init__)


def test_sam::port_constructor_args():
    sig = inspect.signature(sam::Port.__init__)
    params = list(sig.parameters.keys())



def test_sam::abstractstate_is_not_abstract():
    assert not inspect.isabstract(sam::AbstractState)


def test_sam::abstractstate_constructor_exists():
    assert callable(sam::AbstractState.__init__)


def test_sam::abstractstate_constructor_args():
    sig = inspect.signature(sam::AbstractState.__init__)
    params = list(sig.parameters.keys())



def test_inputport_is_not_abstract():
    assert not inspect.isabstract(InputPort)


def test_inputport_constructor_exists():
    assert callable(InputPort.__init__)


def test_inputport_constructor_args():
    sig = inspect.signature(InputPort.__init__)
    params = list(sig.parameters.keys())



def test_sam::indataport_is_not_abstract():
    assert not inspect.isabstract(sam::InDataPort)


def test_sam::indataport_constructor_exists():
    assert callable(sam::InDataPort.__init__)


def test_sam::indataport_constructor_args():
    sig = inspect.signature(sam::InDataPort.__init__)
    params = list(sig.parameters.keys())



def test_controlport_is_not_abstract():
    assert not inspect.isabstract(ControlPort)


def test_controlport_constructor_exists():
    assert callable(ControlPort.__init__)


def test_controlport_constructor_args():
    sig = inspect.signature(ControlPort.__init__)
    params = list(sig.parameters.keys())



def test_sam::outcontrolport_is_not_abstract():
    assert not inspect.isabstract(sam::OutControlPort)


def test_sam::outcontrolport_constructor_exists():
    assert callable(sam::OutControlPort.__init__)


def test_sam::outcontrolport_constructor_args():
    sig = inspect.signature(sam::OutControlPort.__init__)
    params = list(sig.parameters.keys())



def test_sam::incontrolport_is_not_abstract():
    assert not inspect.isabstract(sam::InControlPort)


def test_sam::incontrolport_constructor_exists():
    assert callable(sam::InControlPort.__init__)


def test_sam::incontrolport_constructor_args():
    sig = inspect.signature(sam::InControlPort.__init__)
    params = list(sig.parameters.keys())



def test_sam::dataport_is_not_abstract():
    assert not inspect.isabstract(sam::DataPort)


def test_sam::dataport_constructor_exists():
    assert callable(sam::DataPort.__init__)


def test_sam::dataport_constructor_args():
    sig = inspect.signature(sam::DataPort.__init__)
    params = list(sig.parameters.keys())

def test_datatype_exists():
    # Check that the Enumeration exists
    assert DataType is not None

def test_datatype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DataType]
    expected_literals = [
        "Real",
        "Float",
        "Double",
        "Integer",
        "Boolean",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DataType"


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
EModelElement_strategy = st.builds(
    EModelElement,
)
sam::IdentifiedItem_strategy = st.builds(
    sam::IdentifiedItem,
    requirements=
        safe_text,
    comment=
        safe_text
)
sam::Model_strategy = st.builds(
    sam::Model,
)
Flow_strategy = st.builds(
    Flow,
)
sam::DataFlow_strategy = st.builds(
    sam::DataFlow,
    type=
        safe_text
)
sam::ControlFlow_strategy = st.builds(
    sam::ControlFlow,
)
SynchronisationGate_strategy = st.builds(
    SynchronisationGate,
)
sam::Decomposition_strategy = st.builds(
    sam::Decomposition,
)
sam::Composition_strategy = st.builds(
    sam::Composition,
)
Port_strategy = st.builds(
    Port,
)
sam::ControlPort_strategy = st.builds(
    sam::ControlPort,
)
sam::OutputPort_strategy = st.builds(
    sam::OutputPort,
)
OutputPort_strategy = st.builds(
    OutputPort,
)
sam::InputPort_strategy = st.builds(
    sam::InputPort,
)
DataPort_strategy = st.builds(
    DataPort,
)
sam::OutDataPort_strategy = st.builds(
    sam::OutDataPort,
)
IdentifiedItem_strategy = st.builds(
    IdentifiedItem,
)
sam::SynchronisationGate_strategy = st.builds(
    sam::SynchronisationGate,
)
sam::NamedItem_strategy = st.builds(
    sam::NamedItem,
    name=
        safe_text
)
AbstractState_strategy = st.builds(
    AbstractState,
)
sam::MacroState_strategy = st.builds(
    sam::MacroState,
)
sam::State_strategy = st.builds(
    sam::State,
)
State_strategy = st.builds(
    State,
)
sam::InitialState_strategy = st.builds(
    sam::InitialState,
)
ModelContent_strategy = st.builds(
    ModelContent,
)
sam::System_strategy = st.builds(
    sam::System,
)
sam::Automaton_strategy = st.builds(
    sam::Automaton,
)
sam::Transition_strategy = st.builds(
    sam::Transition,
    priority=
        safe_text,
    emission=
        safe_text,
    condition=
        safe_text
)
NamedItem_strategy = st.builds(
    NamedItem,
)
sam::DataStore_strategy = st.builds(
    sam::DataStore,
)
sam::MultiPort_strategy = st.builds(
    sam::MultiPort,
)
sam::Flow_strategy = st.builds(
    sam::Flow,
)
sam::ModelContent_strategy = st.builds(
    sam::ModelContent,
)
sam::Port_strategy = st.builds(
    sam::Port,
)
sam::AbstractState_strategy = st.builds(
    sam::AbstractState,
)
InputPort_strategy = st.builds(
    InputPort,
)
sam::InDataPort_strategy = st.builds(
    sam::InDataPort,
)
ControlPort_strategy = st.builds(
    ControlPort,
)
sam::OutControlPort_strategy = st.builds(
    sam::OutControlPort,
)
sam::InControlPort_strategy = st.builds(
    sam::InControlPort,
)
sam::DataPort_strategy = st.builds(
    sam::DataPort,
)

@given(instance=EModelElement_strategy)
@settings(max_examples=50)
def test_emodelelement_instantiation(instance):
    assert isinstance(instance, EModelElement)

@given(instance=sam::IdentifiedItem_strategy)
@settings(max_examples=50)
def test_sam::identifieditem_instantiation(instance):
    assert isinstance(instance, sam::IdentifiedItem)

@given(instance=sam::IdentifiedItem_strategy)
def test_sam::identifieditem_requirements_type(instance):
    assert isinstance(instance.requirements, str)


@given(instance=sam::IdentifiedItem_strategy)
def test_sam::identifieditem_requirements_setter(instance):
    original = instance.requirements
    instance.requirements = original
    assert instance.requirements == original

@given(instance=sam::IdentifiedItem_strategy)
def test_sam::identifieditem_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=sam::IdentifiedItem_strategy)
def test_sam::identifieditem_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=sam::Model_strategy)
@settings(max_examples=50)
def test_sam::model_instantiation(instance):
    assert isinstance(instance, sam::Model)

@given(instance=Flow_strategy)
@settings(max_examples=50)
def test_flow_instantiation(instance):
    assert isinstance(instance, Flow)

@given(instance=sam::DataFlow_strategy)
@settings(max_examples=50)
def test_sam::dataflow_instantiation(instance):
    assert isinstance(instance, sam::DataFlow)

@given(instance=sam::DataFlow_strategy)
def test_sam::dataflow_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=sam::DataFlow_strategy)
def test_sam::dataflow_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=sam::ControlFlow_strategy)
@settings(max_examples=50)
def test_sam::controlflow_instantiation(instance):
    assert isinstance(instance, sam::ControlFlow)

@given(instance=SynchronisationGate_strategy)
@settings(max_examples=50)
def test_synchronisationgate_instantiation(instance):
    assert isinstance(instance, SynchronisationGate)

@given(instance=sam::Decomposition_strategy)
@settings(max_examples=50)
def test_sam::decomposition_instantiation(instance):
    assert isinstance(instance, sam::Decomposition)

@given(instance=sam::Composition_strategy)
@settings(max_examples=50)
def test_sam::composition_instantiation(instance):
    assert isinstance(instance, sam::Composition)

@given(instance=Port_strategy)
@settings(max_examples=50)
def test_port_instantiation(instance):
    assert isinstance(instance, Port)

@given(instance=sam::ControlPort_strategy)
@settings(max_examples=50)
def test_sam::controlport_instantiation(instance):
    assert isinstance(instance, sam::ControlPort)

@given(instance=sam::OutputPort_strategy)
@settings(max_examples=50)
def test_sam::outputport_instantiation(instance):
    assert isinstance(instance, sam::OutputPort)

@given(instance=OutputPort_strategy)
@settings(max_examples=50)
def test_outputport_instantiation(instance):
    assert isinstance(instance, OutputPort)

@given(instance=sam::InputPort_strategy)
@settings(max_examples=50)
def test_sam::inputport_instantiation(instance):
    assert isinstance(instance, sam::InputPort)

@given(instance=DataPort_strategy)
@settings(max_examples=50)
def test_dataport_instantiation(instance):
    assert isinstance(instance, DataPort)

@given(instance=sam::OutDataPort_strategy)
@settings(max_examples=50)
def test_sam::outdataport_instantiation(instance):
    assert isinstance(instance, sam::OutDataPort)

@given(instance=IdentifiedItem_strategy)
@settings(max_examples=50)
def test_identifieditem_instantiation(instance):
    assert isinstance(instance, IdentifiedItem)

@given(instance=sam::SynchronisationGate_strategy)
@settings(max_examples=50)
def test_sam::synchronisationgate_instantiation(instance):
    assert isinstance(instance, sam::SynchronisationGate)

@given(instance=sam::NamedItem_strategy)
@settings(max_examples=50)
def test_sam::nameditem_instantiation(instance):
    assert isinstance(instance, sam::NamedItem)

@given(instance=sam::NamedItem_strategy)
def test_sam::nameditem_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=sam::NamedItem_strategy)
def test_sam::nameditem_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=AbstractState_strategy)
@settings(max_examples=50)
def test_abstractstate_instantiation(instance):
    assert isinstance(instance, AbstractState)

@given(instance=sam::MacroState_strategy)
@settings(max_examples=50)
def test_sam::macrostate_instantiation(instance):
    assert isinstance(instance, sam::MacroState)

@given(instance=sam::State_strategy)
@settings(max_examples=50)
def test_sam::state_instantiation(instance):
    assert isinstance(instance, sam::State)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=sam::InitialState_strategy)
@settings(max_examples=50)
def test_sam::initialstate_instantiation(instance):
    assert isinstance(instance, sam::InitialState)

@given(instance=ModelContent_strategy)
@settings(max_examples=50)
def test_modelcontent_instantiation(instance):
    assert isinstance(instance, ModelContent)

@given(instance=sam::System_strategy)
@settings(max_examples=50)
def test_sam::system_instantiation(instance):
    assert isinstance(instance, sam::System)

@given(instance=sam::Automaton_strategy)
@settings(max_examples=50)
def test_sam::automaton_instantiation(instance):
    assert isinstance(instance, sam::Automaton)

@given(instance=sam::Transition_strategy)
@settings(max_examples=50)
def test_sam::transition_instantiation(instance):
    assert isinstance(instance, sam::Transition)

@given(instance=sam::Transition_strategy)
def test_sam::transition_priority_type(instance):
    assert isinstance(instance.priority, str)


@given(instance=sam::Transition_strategy)
def test_sam::transition_priority_setter(instance):
    original = instance.priority
    instance.priority = original
    assert instance.priority == original

@given(instance=sam::Transition_strategy)
def test_sam::transition_emission_type(instance):
    assert isinstance(instance.emission, str)


@given(instance=sam::Transition_strategy)
def test_sam::transition_emission_setter(instance):
    original = instance.emission
    instance.emission = original
    assert instance.emission == original

@given(instance=sam::Transition_strategy)
def test_sam::transition_condition_type(instance):
    assert isinstance(instance.condition, str)


@given(instance=sam::Transition_strategy)
def test_sam::transition_condition_setter(instance):
    original = instance.condition
    instance.condition = original
    assert instance.condition == original

@given(instance=NamedItem_strategy)
@settings(max_examples=50)
def test_nameditem_instantiation(instance):
    assert isinstance(instance, NamedItem)

@given(instance=sam::DataStore_strategy)
@settings(max_examples=50)
def test_sam::datastore_instantiation(instance):
    assert isinstance(instance, sam::DataStore)

@given(instance=sam::MultiPort_strategy)
@settings(max_examples=50)
def test_sam::multiport_instantiation(instance):
    assert isinstance(instance, sam::MultiPort)

@given(instance=sam::Flow_strategy)
@settings(max_examples=50)
def test_sam::flow_instantiation(instance):
    assert isinstance(instance, sam::Flow)

@given(instance=sam::ModelContent_strategy)
@settings(max_examples=50)
def test_sam::modelcontent_instantiation(instance):
    assert isinstance(instance, sam::ModelContent)

@given(instance=sam::Port_strategy)
@settings(max_examples=50)
def test_sam::port_instantiation(instance):
    assert isinstance(instance, sam::Port)

@given(instance=sam::AbstractState_strategy)
@settings(max_examples=50)
def test_sam::abstractstate_instantiation(instance):
    assert isinstance(instance, sam::AbstractState)

@given(instance=InputPort_strategy)
@settings(max_examples=50)
def test_inputport_instantiation(instance):
    assert isinstance(instance, InputPort)

@given(instance=sam::InDataPort_strategy)
@settings(max_examples=50)
def test_sam::indataport_instantiation(instance):
    assert isinstance(instance, sam::InDataPort)

@given(instance=ControlPort_strategy)
@settings(max_examples=50)
def test_controlport_instantiation(instance):
    assert isinstance(instance, ControlPort)

@given(instance=sam::OutControlPort_strategy)
@settings(max_examples=50)
def test_sam::outcontrolport_instantiation(instance):
    assert isinstance(instance, sam::OutControlPort)

@given(instance=sam::InControlPort_strategy)
@settings(max_examples=50)
def test_sam::incontrolport_instantiation(instance):
    assert isinstance(instance, sam::InControlPort)

@given(instance=sam::DataPort_strategy)
@settings(max_examples=50)
def test_sam::dataport_instantiation(instance):
    assert isinstance(instance, sam::DataPort)
