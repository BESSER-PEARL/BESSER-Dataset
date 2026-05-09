import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    statesml::ChangeExpression,
    DataType,
    statesml::Boolean,
    statesml::Integer,
    statesml::String,
    statesml::ParameterValue,
    Event,
    statesml::ChangeEvent,
    State,
    statesml::MiddleState,
    statesml::TerminalState,
    statesml::InitialState,
    statesml::Trigger,
    statesml::FunctionCall,
    Node,
    statesml::Transition,
    statesml::SelectionDivergence,
    statesml::State,
    Parameter,
    statesml::SelectionConvergence,
    statesml::Event,
    statesml::Parameter,
    statesml::IncomingParameter,
    statesml::ReturnParameter,
    statesml::Edge,
    statesml::Node,
    statesml::StateSystem,
    statesml::StateSystemModel,
    statesml::SystemUnit,
    statesml::Function,
    statesml::SystemUnitLibrary,
    statesml::DataTypeLibrary,
    statesml::DataType,
    statesml::Attribute,
    statesml::StatesModel,
    statesml::SystemUnitModel,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_statesml::changeexpression_is_not_abstract():
    assert not inspect.isabstract(statesml::ChangeExpression)


def test_statesml::changeexpression_constructor_exists():
    assert callable(statesml::ChangeExpression.__init__)


def test_statesml::changeexpression_constructor_args():
    sig = inspect.signature(statesml::ChangeExpression.__init__)
    params = list(sig.parameters.keys())
    assert "fulfilled" in params, "Missing parameter 'fulfilled'"

def test_statesml::changeexpression_has_fulfilled():
    assert hasattr(statesml::ChangeExpression, "fulfilled")
    descriptor = None
    for klass in statesml::ChangeExpression.__mro__:
        if "fulfilled" in klass.__dict__:
            descriptor = klass.__dict__["fulfilled"]
            break
    assert isinstance(descriptor, property)



def test_datatype_is_not_abstract():
    assert not inspect.isabstract(DataType)


def test_datatype_constructor_exists():
    assert callable(DataType.__init__)


def test_datatype_constructor_args():
    sig = inspect.signature(DataType.__init__)
    params = list(sig.parameters.keys())



def test_statesml::boolean_is_not_abstract():
    assert not inspect.isabstract(statesml::Boolean)


def test_statesml::boolean_constructor_exists():
    assert callable(statesml::Boolean.__init__)


def test_statesml::boolean_constructor_args():
    sig = inspect.signature(statesml::Boolean.__init__)
    params = list(sig.parameters.keys())



def test_statesml::integer_is_not_abstract():
    assert not inspect.isabstract(statesml::Integer)


def test_statesml::integer_constructor_exists():
    assert callable(statesml::Integer.__init__)


def test_statesml::integer_constructor_args():
    sig = inspect.signature(statesml::Integer.__init__)
    params = list(sig.parameters.keys())



def test_statesml::string_is_not_abstract():
    assert not inspect.isabstract(statesml::String)


def test_statesml::string_constructor_exists():
    assert callable(statesml::String.__init__)


def test_statesml::string_constructor_args():
    sig = inspect.signature(statesml::String.__init__)
    params = list(sig.parameters.keys())



def test_statesml::parametervalue_is_not_abstract():
    assert not inspect.isabstract(statesml::ParameterValue)


def test_statesml::parametervalue_constructor_exists():
    assert callable(statesml::ParameterValue.__init__)


def test_statesml::parametervalue_constructor_args():
    sig = inspect.signature(statesml::ParameterValue.__init__)
    params = list(sig.parameters.keys())



def test_event_is_not_abstract():
    assert not inspect.isabstract(Event)


def test_event_constructor_exists():
    assert callable(Event.__init__)


def test_event_constructor_args():
    sig = inspect.signature(Event.__init__)
    params = list(sig.parameters.keys())



def test_statesml::changeevent_is_not_abstract():
    assert not inspect.isabstract(statesml::ChangeEvent)


def test_statesml::changeevent_constructor_exists():
    assert callable(statesml::ChangeEvent.__init__)


def test_statesml::changeevent_constructor_args():
    sig = inspect.signature(statesml::ChangeEvent.__init__)
    params = list(sig.parameters.keys())



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_statesml::middlestate_is_not_abstract():
    assert not inspect.isabstract(statesml::MiddleState)


def test_statesml::middlestate_constructor_exists():
    assert callable(statesml::MiddleState.__init__)


def test_statesml::middlestate_constructor_args():
    sig = inspect.signature(statesml::MiddleState.__init__)
    params = list(sig.parameters.keys())



def test_statesml::terminalstate_is_not_abstract():
    assert not inspect.isabstract(statesml::TerminalState)


def test_statesml::terminalstate_constructor_exists():
    assert callable(statesml::TerminalState.__init__)


def test_statesml::terminalstate_constructor_args():
    sig = inspect.signature(statesml::TerminalState.__init__)
    params = list(sig.parameters.keys())



def test_statesml::initialstate_is_not_abstract():
    assert not inspect.isabstract(statesml::InitialState)


def test_statesml::initialstate_constructor_exists():
    assert callable(statesml::InitialState.__init__)


def test_statesml::initialstate_constructor_args():
    sig = inspect.signature(statesml::InitialState.__init__)
    params = list(sig.parameters.keys())



def test_statesml::trigger_is_not_abstract():
    assert not inspect.isabstract(statesml::Trigger)


def test_statesml::trigger_constructor_exists():
    assert callable(statesml::Trigger.__init__)


def test_statesml::trigger_constructor_args():
    sig = inspect.signature(statesml::Trigger.__init__)
    params = list(sig.parameters.keys())



def test_statesml::functioncall_is_not_abstract():
    assert not inspect.isabstract(statesml::FunctionCall)


def test_statesml::functioncall_constructor_exists():
    assert callable(statesml::FunctionCall.__init__)


def test_statesml::functioncall_constructor_args():
    sig = inspect.signature(statesml::FunctionCall.__init__)
    params = list(sig.parameters.keys())



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_statesml::transition_is_not_abstract():
    assert not inspect.isabstract(statesml::Transition)


def test_statesml::transition_constructor_exists():
    assert callable(statesml::Transition.__init__)


def test_statesml::transition_constructor_args():
    sig = inspect.signature(statesml::Transition.__init__)
    params = list(sig.parameters.keys())



def test_statesml::selectiondivergence_is_not_abstract():
    assert not inspect.isabstract(statesml::SelectionDivergence)


def test_statesml::selectiondivergence_constructor_exists():
    assert callable(statesml::SelectionDivergence.__init__)


def test_statesml::selectiondivergence_constructor_args():
    sig = inspect.signature(statesml::SelectionDivergence.__init__)
    params = list(sig.parameters.keys())



def test_statesml::state_is_not_abstract():
    assert not inspect.isabstract(statesml::State)


def test_statesml::state_constructor_exists():
    assert callable(statesml::State.__init__)


def test_statesml::state_constructor_args():
    sig = inspect.signature(statesml::State.__init__)
    params = list(sig.parameters.keys())



def test_parameter_is_not_abstract():
    assert not inspect.isabstract(Parameter)


def test_parameter_constructor_exists():
    assert callable(Parameter.__init__)


def test_parameter_constructor_args():
    sig = inspect.signature(Parameter.__init__)
    params = list(sig.parameters.keys())



def test_statesml::selectionconvergence_is_not_abstract():
    assert not inspect.isabstract(statesml::SelectionConvergence)


def test_statesml::selectionconvergence_constructor_exists():
    assert callable(statesml::SelectionConvergence.__init__)


def test_statesml::selectionconvergence_constructor_args():
    sig = inspect.signature(statesml::SelectionConvergence.__init__)
    params = list(sig.parameters.keys())



def test_statesml::event_is_not_abstract():
    assert not inspect.isabstract(statesml::Event)


def test_statesml::event_constructor_exists():
    assert callable(statesml::Event.__init__)


def test_statesml::event_constructor_args():
    sig = inspect.signature(statesml::Event.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statesml::event_has_name():
    assert hasattr(statesml::Event, "name")
    descriptor = None
    for klass in statesml::Event.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statesml::parameter_is_not_abstract():
    assert not inspect.isabstract(statesml::Parameter)


def test_statesml::parameter_constructor_exists():
    assert callable(statesml::Parameter.__init__)


def test_statesml::parameter_constructor_args():
    sig = inspect.signature(statesml::Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statesml::parameter_has_name():
    assert hasattr(statesml::Parameter, "name")
    descriptor = None
    for klass in statesml::Parameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statesml::incomingparameter_is_not_abstract():
    assert not inspect.isabstract(statesml::IncomingParameter)


def test_statesml::incomingparameter_constructor_exists():
    assert callable(statesml::IncomingParameter.__init__)


def test_statesml::incomingparameter_constructor_args():
    sig = inspect.signature(statesml::IncomingParameter.__init__)
    params = list(sig.parameters.keys())



def test_statesml::returnparameter_is_not_abstract():
    assert not inspect.isabstract(statesml::ReturnParameter)


def test_statesml::returnparameter_constructor_exists():
    assert callable(statesml::ReturnParameter.__init__)


def test_statesml::returnparameter_constructor_args():
    sig = inspect.signature(statesml::ReturnParameter.__init__)
    params = list(sig.parameters.keys())



def test_statesml::edge_is_not_abstract():
    assert not inspect.isabstract(statesml::Edge)


def test_statesml::edge_constructor_exists():
    assert callable(statesml::Edge.__init__)


def test_statesml::edge_constructor_args():
    sig = inspect.signature(statesml::Edge.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statesml::edge_has_name():
    assert hasattr(statesml::Edge, "name")
    descriptor = None
    for klass in statesml::Edge.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statesml::node_is_not_abstract():
    assert not inspect.isabstract(statesml::Node)


def test_statesml::node_constructor_exists():
    assert callable(statesml::Node.__init__)


def test_statesml::node_constructor_args():
    sig = inspect.signature(statesml::Node.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statesml::node_has_name():
    assert hasattr(statesml::Node, "name")
    descriptor = None
    for klass in statesml::Node.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statesml::statesystem_is_not_abstract():
    assert not inspect.isabstract(statesml::StateSystem)


def test_statesml::statesystem_constructor_exists():
    assert callable(statesml::StateSystem.__init__)


def test_statesml::statesystem_constructor_args():
    sig = inspect.signature(statesml::StateSystem.__init__)
    params = list(sig.parameters.keys())



def test_statesml::statesystemmodel_is_not_abstract():
    assert not inspect.isabstract(statesml::StateSystemModel)


def test_statesml::statesystemmodel_constructor_exists():
    assert callable(statesml::StateSystemModel.__init__)


def test_statesml::statesystemmodel_constructor_args():
    sig = inspect.signature(statesml::StateSystemModel.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statesml::statesystemmodel_has_name():
    assert hasattr(statesml::StateSystemModel, "name")
    descriptor = None
    for klass in statesml::StateSystemModel.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statesml::systemunit_is_not_abstract():
    assert not inspect.isabstract(statesml::SystemUnit)


def test_statesml::systemunit_constructor_exists():
    assert callable(statesml::SystemUnit.__init__)


def test_statesml::systemunit_constructor_args():
    sig = inspect.signature(statesml::SystemUnit.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statesml::systemunit_has_name():
    assert hasattr(statesml::SystemUnit, "name")
    descriptor = None
    for klass in statesml::SystemUnit.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statesml::function_is_not_abstract():
    assert not inspect.isabstract(statesml::Function)


def test_statesml::function_constructor_exists():
    assert callable(statesml::Function.__init__)


def test_statesml::function_constructor_args():
    sig = inspect.signature(statesml::Function.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statesml::function_has_name():
    assert hasattr(statesml::Function, "name")
    descriptor = None
    for klass in statesml::Function.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statesml::systemunitlibrary_is_not_abstract():
    assert not inspect.isabstract(statesml::SystemUnitLibrary)


def test_statesml::systemunitlibrary_constructor_exists():
    assert callable(statesml::SystemUnitLibrary.__init__)


def test_statesml::systemunitlibrary_constructor_args():
    sig = inspect.signature(statesml::SystemUnitLibrary.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statesml::systemunitlibrary_has_name():
    assert hasattr(statesml::SystemUnitLibrary, "name")
    descriptor = None
    for klass in statesml::SystemUnitLibrary.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statesml::datatypelibrary_is_not_abstract():
    assert not inspect.isabstract(statesml::DataTypeLibrary)


def test_statesml::datatypelibrary_constructor_exists():
    assert callable(statesml::DataTypeLibrary.__init__)


def test_statesml::datatypelibrary_constructor_args():
    sig = inspect.signature(statesml::DataTypeLibrary.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statesml::datatypelibrary_has_name():
    assert hasattr(statesml::DataTypeLibrary, "name")
    descriptor = None
    for klass in statesml::DataTypeLibrary.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statesml::datatype_is_not_abstract():
    assert not inspect.isabstract(statesml::DataType)


def test_statesml::datatype_constructor_exists():
    assert callable(statesml::DataType.__init__)


def test_statesml::datatype_constructor_args():
    sig = inspect.signature(statesml::DataType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statesml::datatype_has_name():
    assert hasattr(statesml::DataType, "name")
    descriptor = None
    for klass in statesml::DataType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statesml::attribute_is_not_abstract():
    assert not inspect.isabstract(statesml::Attribute)


def test_statesml::attribute_constructor_exists():
    assert callable(statesml::Attribute.__init__)


def test_statesml::attribute_constructor_args():
    sig = inspect.signature(statesml::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statesml::attribute_has_name():
    assert hasattr(statesml::Attribute, "name")
    descriptor = None
    for klass in statesml::Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statesml::statesmodel_is_not_abstract():
    assert not inspect.isabstract(statesml::StatesModel)


def test_statesml::statesmodel_constructor_exists():
    assert callable(statesml::StatesModel.__init__)


def test_statesml::statesmodel_constructor_args():
    sig = inspect.signature(statesml::StatesModel.__init__)
    params = list(sig.parameters.keys())



def test_statesml::systemunitmodel_is_not_abstract():
    assert not inspect.isabstract(statesml::SystemUnitModel)


def test_statesml::systemunitmodel_constructor_exists():
    assert callable(statesml::SystemUnitModel.__init__)


def test_statesml::systemunitmodel_constructor_args():
    sig = inspect.signature(statesml::SystemUnitModel.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statesml::systemunitmodel_has_name():
    assert hasattr(statesml::SystemUnitModel, "name")
    descriptor = None
    for klass in statesml::SystemUnitModel.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)


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
statesml::ChangeExpression_strategy = st.builds(
    statesml::ChangeExpression,
    fulfilled=
        st.booleans()
)
DataType_strategy = st.builds(
    DataType,
)
statesml::Boolean_strategy = st.builds(
    statesml::Boolean,
)
statesml::Integer_strategy = st.builds(
    statesml::Integer,
)
statesml::String_strategy = st.builds(
    statesml::String,
)
statesml::ParameterValue_strategy = st.builds(
    statesml::ParameterValue,
)
Event_strategy = st.builds(
    Event,
)
statesml::ChangeEvent_strategy = st.builds(
    statesml::ChangeEvent,
)
State_strategy = st.builds(
    State,
)
statesml::MiddleState_strategy = st.builds(
    statesml::MiddleState,
)
statesml::TerminalState_strategy = st.builds(
    statesml::TerminalState,
)
statesml::InitialState_strategy = st.builds(
    statesml::InitialState,
)
statesml::Trigger_strategy = st.builds(
    statesml::Trigger,
)
statesml::FunctionCall_strategy = st.builds(
    statesml::FunctionCall,
)
Node_strategy = st.builds(
    Node,
)
statesml::Transition_strategy = st.builds(
    statesml::Transition,
)
statesml::SelectionDivergence_strategy = st.builds(
    statesml::SelectionDivergence,
)
statesml::State_strategy = st.builds(
    statesml::State,
)
Parameter_strategy = st.builds(
    Parameter,
)
statesml::SelectionConvergence_strategy = st.builds(
    statesml::SelectionConvergence,
)
statesml::Event_strategy = st.builds(
    statesml::Event,
    name=
        safe_text
)
statesml::Parameter_strategy = st.builds(
    statesml::Parameter,
    name=
        safe_text
)
statesml::IncomingParameter_strategy = st.builds(
    statesml::IncomingParameter,
)
statesml::ReturnParameter_strategy = st.builds(
    statesml::ReturnParameter,
)
statesml::Edge_strategy = st.builds(
    statesml::Edge,
    name=
        safe_text
)
statesml::Node_strategy = st.builds(
    statesml::Node,
    name=
        safe_text
)
statesml::StateSystem_strategy = st.builds(
    statesml::StateSystem,
)
statesml::StateSystemModel_strategy = st.builds(
    statesml::StateSystemModel,
    name=
        safe_text
)
statesml::SystemUnit_strategy = st.builds(
    statesml::SystemUnit,
    name=
        safe_text
)
statesml::Function_strategy = st.builds(
    statesml::Function,
    name=
        safe_text
)
statesml::SystemUnitLibrary_strategy = st.builds(
    statesml::SystemUnitLibrary,
    name=
        safe_text
)
statesml::DataTypeLibrary_strategy = st.builds(
    statesml::DataTypeLibrary,
    name=
        safe_text
)
statesml::DataType_strategy = st.builds(
    statesml::DataType,
    name=
        safe_text
)
statesml::Attribute_strategy = st.builds(
    statesml::Attribute,
    name=
        safe_text
)
statesml::StatesModel_strategy = st.builds(
    statesml::StatesModel,
)
statesml::SystemUnitModel_strategy = st.builds(
    statesml::SystemUnitModel,
    name=
        safe_text
)

@given(instance=statesml::ChangeExpression_strategy)
@settings(max_examples=50)
def test_statesml::changeexpression_instantiation(instance):
    assert isinstance(instance, statesml::ChangeExpression)

@given(instance=statesml::ChangeExpression_strategy)
def test_statesml::changeexpression_fulfilled_type(instance):
    assert isinstance(instance.fulfilled, bool)


@given(instance=statesml::ChangeExpression_strategy)
def test_statesml::changeexpression_fulfilled_setter(instance):
    original = instance.fulfilled
    instance.fulfilled = original
    assert instance.fulfilled == original

@given(instance=DataType_strategy)
@settings(max_examples=50)
def test_datatype_instantiation(instance):
    assert isinstance(instance, DataType)

@given(instance=statesml::Boolean_strategy)
@settings(max_examples=50)
def test_statesml::boolean_instantiation(instance):
    assert isinstance(instance, statesml::Boolean)

@given(instance=statesml::Integer_strategy)
@settings(max_examples=50)
def test_statesml::integer_instantiation(instance):
    assert isinstance(instance, statesml::Integer)

@given(instance=statesml::String_strategy)
@settings(max_examples=50)
def test_statesml::string_instantiation(instance):
    assert isinstance(instance, statesml::String)

@given(instance=statesml::ParameterValue_strategy)
@settings(max_examples=50)
def test_statesml::parametervalue_instantiation(instance):
    assert isinstance(instance, statesml::ParameterValue)

@given(instance=Event_strategy)
@settings(max_examples=50)
def test_event_instantiation(instance):
    assert isinstance(instance, Event)

@given(instance=statesml::ChangeEvent_strategy)
@settings(max_examples=50)
def test_statesml::changeevent_instantiation(instance):
    assert isinstance(instance, statesml::ChangeEvent)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=statesml::MiddleState_strategy)
@settings(max_examples=50)
def test_statesml::middlestate_instantiation(instance):
    assert isinstance(instance, statesml::MiddleState)

@given(instance=statesml::TerminalState_strategy)
@settings(max_examples=50)
def test_statesml::terminalstate_instantiation(instance):
    assert isinstance(instance, statesml::TerminalState)

@given(instance=statesml::InitialState_strategy)
@settings(max_examples=50)
def test_statesml::initialstate_instantiation(instance):
    assert isinstance(instance, statesml::InitialState)

@given(instance=statesml::Trigger_strategy)
@settings(max_examples=50)
def test_statesml::trigger_instantiation(instance):
    assert isinstance(instance, statesml::Trigger)

@given(instance=statesml::FunctionCall_strategy)
@settings(max_examples=50)
def test_statesml::functioncall_instantiation(instance):
    assert isinstance(instance, statesml::FunctionCall)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=statesml::Transition_strategy)
@settings(max_examples=50)
def test_statesml::transition_instantiation(instance):
    assert isinstance(instance, statesml::Transition)

@given(instance=statesml::SelectionDivergence_strategy)
@settings(max_examples=50)
def test_statesml::selectiondivergence_instantiation(instance):
    assert isinstance(instance, statesml::SelectionDivergence)

@given(instance=statesml::State_strategy)
@settings(max_examples=50)
def test_statesml::state_instantiation(instance):
    assert isinstance(instance, statesml::State)

@given(instance=Parameter_strategy)
@settings(max_examples=50)
def test_parameter_instantiation(instance):
    assert isinstance(instance, Parameter)

@given(instance=statesml::SelectionConvergence_strategy)
@settings(max_examples=50)
def test_statesml::selectionconvergence_instantiation(instance):
    assert isinstance(instance, statesml::SelectionConvergence)

@given(instance=statesml::Event_strategy)
@settings(max_examples=50)
def test_statesml::event_instantiation(instance):
    assert isinstance(instance, statesml::Event)

@given(instance=statesml::Event_strategy)
def test_statesml::event_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=statesml::Event_strategy)
def test_statesml::event_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=statesml::Parameter_strategy)
@settings(max_examples=50)
def test_statesml::parameter_instantiation(instance):
    assert isinstance(instance, statesml::Parameter)

@given(instance=statesml::Parameter_strategy)
def test_statesml::parameter_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=statesml::Parameter_strategy)
def test_statesml::parameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=statesml::IncomingParameter_strategy)
@settings(max_examples=50)
def test_statesml::incomingparameter_instantiation(instance):
    assert isinstance(instance, statesml::IncomingParameter)

@given(instance=statesml::ReturnParameter_strategy)
@settings(max_examples=50)
def test_statesml::returnparameter_instantiation(instance):
    assert isinstance(instance, statesml::ReturnParameter)

@given(instance=statesml::Edge_strategy)
@settings(max_examples=50)
def test_statesml::edge_instantiation(instance):
    assert isinstance(instance, statesml::Edge)

@given(instance=statesml::Edge_strategy)
def test_statesml::edge_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=statesml::Edge_strategy)
def test_statesml::edge_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=statesml::Node_strategy)
@settings(max_examples=50)
def test_statesml::node_instantiation(instance):
    assert isinstance(instance, statesml::Node)

@given(instance=statesml::Node_strategy)
def test_statesml::node_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=statesml::Node_strategy)
def test_statesml::node_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=statesml::StateSystem_strategy)
@settings(max_examples=50)
def test_statesml::statesystem_instantiation(instance):
    assert isinstance(instance, statesml::StateSystem)

@given(instance=statesml::StateSystemModel_strategy)
@settings(max_examples=50)
def test_statesml::statesystemmodel_instantiation(instance):
    assert isinstance(instance, statesml::StateSystemModel)

@given(instance=statesml::StateSystemModel_strategy)
def test_statesml::statesystemmodel_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=statesml::StateSystemModel_strategy)
def test_statesml::statesystemmodel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=statesml::SystemUnit_strategy)
@settings(max_examples=50)
def test_statesml::systemunit_instantiation(instance):
    assert isinstance(instance, statesml::SystemUnit)

@given(instance=statesml::SystemUnit_strategy)
def test_statesml::systemunit_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=statesml::SystemUnit_strategy)
def test_statesml::systemunit_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=statesml::Function_strategy)
@settings(max_examples=50)
def test_statesml::function_instantiation(instance):
    assert isinstance(instance, statesml::Function)

@given(instance=statesml::Function_strategy)
def test_statesml::function_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=statesml::Function_strategy)
def test_statesml::function_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=statesml::SystemUnitLibrary_strategy)
@settings(max_examples=50)
def test_statesml::systemunitlibrary_instantiation(instance):
    assert isinstance(instance, statesml::SystemUnitLibrary)

@given(instance=statesml::SystemUnitLibrary_strategy)
def test_statesml::systemunitlibrary_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=statesml::SystemUnitLibrary_strategy)
def test_statesml::systemunitlibrary_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=statesml::DataTypeLibrary_strategy)
@settings(max_examples=50)
def test_statesml::datatypelibrary_instantiation(instance):
    assert isinstance(instance, statesml::DataTypeLibrary)

@given(instance=statesml::DataTypeLibrary_strategy)
def test_statesml::datatypelibrary_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=statesml::DataTypeLibrary_strategy)
def test_statesml::datatypelibrary_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=statesml::DataType_strategy)
@settings(max_examples=50)
def test_statesml::datatype_instantiation(instance):
    assert isinstance(instance, statesml::DataType)

@given(instance=statesml::DataType_strategy)
def test_statesml::datatype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=statesml::DataType_strategy)
def test_statesml::datatype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=statesml::Attribute_strategy)
@settings(max_examples=50)
def test_statesml::attribute_instantiation(instance):
    assert isinstance(instance, statesml::Attribute)

@given(instance=statesml::Attribute_strategy)
def test_statesml::attribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=statesml::Attribute_strategy)
def test_statesml::attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=statesml::StatesModel_strategy)
@settings(max_examples=50)
def test_statesml::statesmodel_instantiation(instance):
    assert isinstance(instance, statesml::StatesModel)

@given(instance=statesml::SystemUnitModel_strategy)
@settings(max_examples=50)
def test_statesml::systemunitmodel_instantiation(instance):
    assert isinstance(instance, statesml::SystemUnitModel)

@given(instance=statesml::SystemUnitModel_strategy)
def test_statesml::systemunitmodel_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=statesml::SystemUnitModel_strategy)
def test_statesml::systemunitmodel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
