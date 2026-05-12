import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    statesml_ChangeExpression,
    DataType,
    statesml_Boolean,
    statesml_Integer,
    statesml_String,
    statesml_ParameterValue,
    Event,
    statesml_ChangeEvent,
    State,
    statesml_TerminalState,
    statesml_MiddleState,
    statesml_InitialState,
    statesml_Trigger,
    statesml_FunctionCall,
    Node,
    statesml_Transition,
    statesml_SelectionDivergence,
    statesml_State,
    Parameter,
    statesml_SelectionConvergence,
    statesml_Event,
    statesml_Parameter,
    statesml_IncomingParameter,
    statesml_ReturnParameter,
    statesml_Edge,
    statesml_Node,
    statesml_StateSystem,
    statesml_StateSystemModel,
    statesml_SystemUnit,
    statesml_Function,
    statesml_SystemUnitLibrary,
    statesml_DataTypeLibrary,
    statesml_DataType,
    statesml_Attribute,
    statesml_StatesModel,
    statesml_SystemUnitModel,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_statesml_changeexpression_is_not_abstract():
    assert not inspect.isabstract(statesml_ChangeExpression)


def test_statesml_changeexpression_constructor_exists():
    assert callable(statesml_ChangeExpression.__init__)


def test_statesml_changeexpression_constructor_args():
    sig = inspect.signature(statesml_ChangeExpression.__init__)
    params = list(sig.parameters.keys())
    assert "fulfilled" in params, "Missing parameter 'fulfilled'"

def test_statesml_changeexpression_has_fulfilled():
    assert hasattr(statesml_ChangeExpression, "fulfilled")
    descriptor = None
    for klass in statesml_ChangeExpression.__mro__:
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



def test_statesml_boolean_is_not_abstract():
    assert not inspect.isabstract(statesml_Boolean)


def test_statesml_boolean_constructor_exists():
    assert callable(statesml_Boolean.__init__)


def test_statesml_boolean_constructor_args():
    sig = inspect.signature(statesml_Boolean.__init__)
    params = list(sig.parameters.keys())



def test_statesml_integer_is_not_abstract():
    assert not inspect.isabstract(statesml_Integer)


def test_statesml_integer_constructor_exists():
    assert callable(statesml_Integer.__init__)


def test_statesml_integer_constructor_args():
    sig = inspect.signature(statesml_Integer.__init__)
    params = list(sig.parameters.keys())



def test_statesml_string_is_not_abstract():
    assert not inspect.isabstract(statesml_String)


def test_statesml_string_constructor_exists():
    assert callable(statesml_String.__init__)


def test_statesml_string_constructor_args():
    sig = inspect.signature(statesml_String.__init__)
    params = list(sig.parameters.keys())



def test_statesml_parametervalue_is_not_abstract():
    assert not inspect.isabstract(statesml_ParameterValue)


def test_statesml_parametervalue_constructor_exists():
    assert callable(statesml_ParameterValue.__init__)


def test_statesml_parametervalue_constructor_args():
    sig = inspect.signature(statesml_ParameterValue.__init__)
    params = list(sig.parameters.keys())



def test_event_is_not_abstract():
    assert not inspect.isabstract(Event)


def test_event_constructor_exists():
    assert callable(Event.__init__)


def test_event_constructor_args():
    sig = inspect.signature(Event.__init__)
    params = list(sig.parameters.keys())



def test_statesml_changeevent_is_not_abstract():
    assert not inspect.isabstract(statesml_ChangeEvent)


def test_statesml_changeevent_constructor_exists():
    assert callable(statesml_ChangeEvent.__init__)


def test_statesml_changeevent_constructor_args():
    sig = inspect.signature(statesml_ChangeEvent.__init__)
    params = list(sig.parameters.keys())



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_statesml_terminalstate_is_not_abstract():
    assert not inspect.isabstract(statesml_TerminalState)


def test_statesml_terminalstate_constructor_exists():
    assert callable(statesml_TerminalState.__init__)


def test_statesml_terminalstate_constructor_args():
    sig = inspect.signature(statesml_TerminalState.__init__)
    params = list(sig.parameters.keys())



def test_statesml_middlestate_is_not_abstract():
    assert not inspect.isabstract(statesml_MiddleState)


def test_statesml_middlestate_constructor_exists():
    assert callable(statesml_MiddleState.__init__)


def test_statesml_middlestate_constructor_args():
    sig = inspect.signature(statesml_MiddleState.__init__)
    params = list(sig.parameters.keys())



def test_statesml_initialstate_is_not_abstract():
    assert not inspect.isabstract(statesml_InitialState)


def test_statesml_initialstate_constructor_exists():
    assert callable(statesml_InitialState.__init__)


def test_statesml_initialstate_constructor_args():
    sig = inspect.signature(statesml_InitialState.__init__)
    params = list(sig.parameters.keys())



def test_statesml_trigger_is_not_abstract():
    assert not inspect.isabstract(statesml_Trigger)


def test_statesml_trigger_constructor_exists():
    assert callable(statesml_Trigger.__init__)


def test_statesml_trigger_constructor_args():
    sig = inspect.signature(statesml_Trigger.__init__)
    params = list(sig.parameters.keys())



def test_statesml_functioncall_is_not_abstract():
    assert not inspect.isabstract(statesml_FunctionCall)


def test_statesml_functioncall_constructor_exists():
    assert callable(statesml_FunctionCall.__init__)


def test_statesml_functioncall_constructor_args():
    sig = inspect.signature(statesml_FunctionCall.__init__)
    params = list(sig.parameters.keys())



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_statesml_transition_is_not_abstract():
    assert not inspect.isabstract(statesml_Transition)


def test_statesml_transition_constructor_exists():
    assert callable(statesml_Transition.__init__)


def test_statesml_transition_constructor_args():
    sig = inspect.signature(statesml_Transition.__init__)
    params = list(sig.parameters.keys())



def test_statesml_selectiondivergence_is_not_abstract():
    assert not inspect.isabstract(statesml_SelectionDivergence)


def test_statesml_selectiondivergence_constructor_exists():
    assert callable(statesml_SelectionDivergence.__init__)


def test_statesml_selectiondivergence_constructor_args():
    sig = inspect.signature(statesml_SelectionDivergence.__init__)
    params = list(sig.parameters.keys())



def test_statesml_state_is_not_abstract():
    assert not inspect.isabstract(statesml_State)


def test_statesml_state_constructor_exists():
    assert callable(statesml_State.__init__)


def test_statesml_state_constructor_args():
    sig = inspect.signature(statesml_State.__init__)
    params = list(sig.parameters.keys())



def test_parameter_is_not_abstract():
    assert not inspect.isabstract(Parameter)


def test_parameter_constructor_exists():
    assert callable(Parameter.__init__)


def test_parameter_constructor_args():
    sig = inspect.signature(Parameter.__init__)
    params = list(sig.parameters.keys())



def test_statesml_selectionconvergence_is_not_abstract():
    assert not inspect.isabstract(statesml_SelectionConvergence)


def test_statesml_selectionconvergence_constructor_exists():
    assert callable(statesml_SelectionConvergence.__init__)


def test_statesml_selectionconvergence_constructor_args():
    sig = inspect.signature(statesml_SelectionConvergence.__init__)
    params = list(sig.parameters.keys())



def test_statesml_event_is_not_abstract():
    assert not inspect.isabstract(statesml_Event)


def test_statesml_event_constructor_exists():
    assert callable(statesml_Event.__init__)


def test_statesml_event_constructor_args():
    sig = inspect.signature(statesml_Event.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statesml_event_has_name():
    assert hasattr(statesml_Event, "name")
    descriptor = None
    for klass in statesml_Event.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statesml_parameter_is_not_abstract():
    assert not inspect.isabstract(statesml_Parameter)


def test_statesml_parameter_constructor_exists():
    assert callable(statesml_Parameter.__init__)


def test_statesml_parameter_constructor_args():
    sig = inspect.signature(statesml_Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statesml_parameter_has_name():
    assert hasattr(statesml_Parameter, "name")
    descriptor = None
    for klass in statesml_Parameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statesml_incomingparameter_is_not_abstract():
    assert not inspect.isabstract(statesml_IncomingParameter)


def test_statesml_incomingparameter_constructor_exists():
    assert callable(statesml_IncomingParameter.__init__)


def test_statesml_incomingparameter_constructor_args():
    sig = inspect.signature(statesml_IncomingParameter.__init__)
    params = list(sig.parameters.keys())



def test_statesml_returnparameter_is_not_abstract():
    assert not inspect.isabstract(statesml_ReturnParameter)


def test_statesml_returnparameter_constructor_exists():
    assert callable(statesml_ReturnParameter.__init__)


def test_statesml_returnparameter_constructor_args():
    sig = inspect.signature(statesml_ReturnParameter.__init__)
    params = list(sig.parameters.keys())



def test_statesml_edge_is_not_abstract():
    assert not inspect.isabstract(statesml_Edge)


def test_statesml_edge_constructor_exists():
    assert callable(statesml_Edge.__init__)


def test_statesml_edge_constructor_args():
    sig = inspect.signature(statesml_Edge.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statesml_edge_has_name():
    assert hasattr(statesml_Edge, "name")
    descriptor = None
    for klass in statesml_Edge.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statesml_node_is_not_abstract():
    assert not inspect.isabstract(statesml_Node)


def test_statesml_node_constructor_exists():
    assert callable(statesml_Node.__init__)


def test_statesml_node_constructor_args():
    sig = inspect.signature(statesml_Node.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statesml_node_has_name():
    assert hasattr(statesml_Node, "name")
    descriptor = None
    for klass in statesml_Node.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statesml_statesystem_is_not_abstract():
    assert not inspect.isabstract(statesml_StateSystem)


def test_statesml_statesystem_constructor_exists():
    assert callable(statesml_StateSystem.__init__)


def test_statesml_statesystem_constructor_args():
    sig = inspect.signature(statesml_StateSystem.__init__)
    params = list(sig.parameters.keys())



def test_statesml_statesystemmodel_is_not_abstract():
    assert not inspect.isabstract(statesml_StateSystemModel)


def test_statesml_statesystemmodel_constructor_exists():
    assert callable(statesml_StateSystemModel.__init__)


def test_statesml_statesystemmodel_constructor_args():
    sig = inspect.signature(statesml_StateSystemModel.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statesml_statesystemmodel_has_name():
    assert hasattr(statesml_StateSystemModel, "name")
    descriptor = None
    for klass in statesml_StateSystemModel.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statesml_systemunit_is_not_abstract():
    assert not inspect.isabstract(statesml_SystemUnit)


def test_statesml_systemunit_constructor_exists():
    assert callable(statesml_SystemUnit.__init__)


def test_statesml_systemunit_constructor_args():
    sig = inspect.signature(statesml_SystemUnit.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statesml_systemunit_has_name():
    assert hasattr(statesml_SystemUnit, "name")
    descriptor = None
    for klass in statesml_SystemUnit.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statesml_function_is_not_abstract():
    assert not inspect.isabstract(statesml_Function)


def test_statesml_function_constructor_exists():
    assert callable(statesml_Function.__init__)


def test_statesml_function_constructor_args():
    sig = inspect.signature(statesml_Function.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statesml_function_has_name():
    assert hasattr(statesml_Function, "name")
    descriptor = None
    for klass in statesml_Function.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statesml_systemunitlibrary_is_not_abstract():
    assert not inspect.isabstract(statesml_SystemUnitLibrary)


def test_statesml_systemunitlibrary_constructor_exists():
    assert callable(statesml_SystemUnitLibrary.__init__)


def test_statesml_systemunitlibrary_constructor_args():
    sig = inspect.signature(statesml_SystemUnitLibrary.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statesml_systemunitlibrary_has_name():
    assert hasattr(statesml_SystemUnitLibrary, "name")
    descriptor = None
    for klass in statesml_SystemUnitLibrary.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statesml_datatypelibrary_is_not_abstract():
    assert not inspect.isabstract(statesml_DataTypeLibrary)


def test_statesml_datatypelibrary_constructor_exists():
    assert callable(statesml_DataTypeLibrary.__init__)


def test_statesml_datatypelibrary_constructor_args():
    sig = inspect.signature(statesml_DataTypeLibrary.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statesml_datatypelibrary_has_name():
    assert hasattr(statesml_DataTypeLibrary, "name")
    descriptor = None
    for klass in statesml_DataTypeLibrary.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statesml_datatype_is_not_abstract():
    assert not inspect.isabstract(statesml_DataType)


def test_statesml_datatype_constructor_exists():
    assert callable(statesml_DataType.__init__)


def test_statesml_datatype_constructor_args():
    sig = inspect.signature(statesml_DataType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statesml_datatype_has_name():
    assert hasattr(statesml_DataType, "name")
    descriptor = None
    for klass in statesml_DataType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statesml_attribute_is_not_abstract():
    assert not inspect.isabstract(statesml_Attribute)


def test_statesml_attribute_constructor_exists():
    assert callable(statesml_Attribute.__init__)


def test_statesml_attribute_constructor_args():
    sig = inspect.signature(statesml_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statesml_attribute_has_name():
    assert hasattr(statesml_Attribute, "name")
    descriptor = None
    for klass in statesml_Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statesml_statesmodel_is_not_abstract():
    assert not inspect.isabstract(statesml_StatesModel)


def test_statesml_statesmodel_constructor_exists():
    assert callable(statesml_StatesModel.__init__)


def test_statesml_statesmodel_constructor_args():
    sig = inspect.signature(statesml_StatesModel.__init__)
    params = list(sig.parameters.keys())



def test_statesml_systemunitmodel_is_not_abstract():
    assert not inspect.isabstract(statesml_SystemUnitModel)


def test_statesml_systemunitmodel_constructor_exists():
    assert callable(statesml_SystemUnitModel.__init__)


def test_statesml_systemunitmodel_constructor_args():
    sig = inspect.signature(statesml_SystemUnitModel.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statesml_systemunitmodel_has_name():
    assert hasattr(statesml_SystemUnitModel, "name")
    descriptor = None
    for klass in statesml_SystemUnitModel.__mro__:
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
statesml_ChangeExpression_strategy = st.builds(
    statesml_ChangeExpression,
    fulfilled=
        st.booleans()
)
DataType_strategy = st.builds(
    DataType,
)
statesml_Boolean_strategy = st.builds(
    statesml_Boolean,
)
statesml_Integer_strategy = st.builds(
    statesml_Integer,
)
statesml_String_strategy = st.builds(
    statesml_String,
)
statesml_ParameterValue_strategy = st.builds(
    statesml_ParameterValue,
)
Event_strategy = st.builds(
    Event,
)
statesml_ChangeEvent_strategy = st.builds(
    statesml_ChangeEvent,
)
State_strategy = st.builds(
    State,
)
statesml_TerminalState_strategy = st.builds(
    statesml_TerminalState,
)
statesml_MiddleState_strategy = st.builds(
    statesml_MiddleState,
)
statesml_InitialState_strategy = st.builds(
    statesml_InitialState,
)
statesml_Trigger_strategy = st.builds(
    statesml_Trigger,
)
statesml_FunctionCall_strategy = st.builds(
    statesml_FunctionCall,
)
Node_strategy = st.builds(
    Node,
)
statesml_Transition_strategy = st.builds(
    statesml_Transition,
)
statesml_SelectionDivergence_strategy = st.builds(
    statesml_SelectionDivergence,
)
statesml_State_strategy = st.builds(
    statesml_State,
)
Parameter_strategy = st.builds(
    Parameter,
)
statesml_SelectionConvergence_strategy = st.builds(
    statesml_SelectionConvergence,
)
statesml_Event_strategy = st.builds(
    statesml_Event,
    name=
        safe_text
)
statesml_Parameter_strategy = st.builds(
    statesml_Parameter,
    name=
        safe_text
)
statesml_IncomingParameter_strategy = st.builds(
    statesml_IncomingParameter,
)
statesml_ReturnParameter_strategy = st.builds(
    statesml_ReturnParameter,
)
statesml_Edge_strategy = st.builds(
    statesml_Edge,
    name=
        safe_text
)
statesml_Node_strategy = st.builds(
    statesml_Node,
    name=
        safe_text
)
statesml_StateSystem_strategy = st.builds(
    statesml_StateSystem,
)
statesml_StateSystemModel_strategy = st.builds(
    statesml_StateSystemModel,
    name=
        safe_text
)
statesml_SystemUnit_strategy = st.builds(
    statesml_SystemUnit,
    name=
        safe_text
)
statesml_Function_strategy = st.builds(
    statesml_Function,
    name=
        safe_text
)
statesml_SystemUnitLibrary_strategy = st.builds(
    statesml_SystemUnitLibrary,
    name=
        safe_text
)
statesml_DataTypeLibrary_strategy = st.builds(
    statesml_DataTypeLibrary,
    name=
        safe_text
)
statesml_DataType_strategy = st.builds(
    statesml_DataType,
    name=
        safe_text
)
statesml_Attribute_strategy = st.builds(
    statesml_Attribute,
    name=
        safe_text
)
statesml_StatesModel_strategy = st.builds(
    statesml_StatesModel,
)
statesml_SystemUnitModel_strategy = st.builds(
    statesml_SystemUnitModel,
    name=
        safe_text
)

@given(instance=statesml_ChangeExpression_strategy)
@settings(max_examples=50)
def test_statesml_changeexpression_instantiation(instance):
    assert isinstance(instance, statesml_ChangeExpression)



@given(instance=statesml_ChangeExpression_strategy)
def test_statesml_changeexpression_fulfilled_setter(instance):
    original = instance.fulfilled
    instance.fulfilled = original
    assert instance.fulfilled == original

@given(instance=DataType_strategy)
@settings(max_examples=50)
def test_datatype_instantiation(instance):
    assert isinstance(instance, DataType)

@given(instance=statesml_Boolean_strategy)
@settings(max_examples=50)
def test_statesml_boolean_instantiation(instance):
    assert isinstance(instance, statesml_Boolean)

@given(instance=statesml_Integer_strategy)
@settings(max_examples=50)
def test_statesml_integer_instantiation(instance):
    assert isinstance(instance, statesml_Integer)

@given(instance=statesml_String_strategy)
@settings(max_examples=50)
def test_statesml_string_instantiation(instance):
    assert isinstance(instance, statesml_String)

@given(instance=statesml_ParameterValue_strategy)
@settings(max_examples=50)
def test_statesml_parametervalue_instantiation(instance):
    assert isinstance(instance, statesml_ParameterValue)

@given(instance=Event_strategy)
@settings(max_examples=50)
def test_event_instantiation(instance):
    assert isinstance(instance, Event)

@given(instance=statesml_ChangeEvent_strategy)
@settings(max_examples=50)
def test_statesml_changeevent_instantiation(instance):
    assert isinstance(instance, statesml_ChangeEvent)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=statesml_TerminalState_strategy)
@settings(max_examples=50)
def test_statesml_terminalstate_instantiation(instance):
    assert isinstance(instance, statesml_TerminalState)

@given(instance=statesml_MiddleState_strategy)
@settings(max_examples=50)
def test_statesml_middlestate_instantiation(instance):
    assert isinstance(instance, statesml_MiddleState)

@given(instance=statesml_InitialState_strategy)
@settings(max_examples=50)
def test_statesml_initialstate_instantiation(instance):
    assert isinstance(instance, statesml_InitialState)

@given(instance=statesml_Trigger_strategy)
@settings(max_examples=50)
def test_statesml_trigger_instantiation(instance):
    assert isinstance(instance, statesml_Trigger)

@given(instance=statesml_FunctionCall_strategy)
@settings(max_examples=50)
def test_statesml_functioncall_instantiation(instance):
    assert isinstance(instance, statesml_FunctionCall)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=statesml_Transition_strategy)
@settings(max_examples=50)
def test_statesml_transition_instantiation(instance):
    assert isinstance(instance, statesml_Transition)

@given(instance=statesml_SelectionDivergence_strategy)
@settings(max_examples=50)
def test_statesml_selectiondivergence_instantiation(instance):
    assert isinstance(instance, statesml_SelectionDivergence)

@given(instance=statesml_State_strategy)
@settings(max_examples=50)
def test_statesml_state_instantiation(instance):
    assert isinstance(instance, statesml_State)

@given(instance=Parameter_strategy)
@settings(max_examples=50)
def test_parameter_instantiation(instance):
    assert isinstance(instance, Parameter)

@given(instance=statesml_SelectionConvergence_strategy)
@settings(max_examples=50)
def test_statesml_selectionconvergence_instantiation(instance):
    assert isinstance(instance, statesml_SelectionConvergence)

@given(instance=statesml_Event_strategy)
@settings(max_examples=50)
def test_statesml_event_instantiation(instance):
    assert isinstance(instance, statesml_Event)



@given(instance=statesml_Event_strategy)
def test_statesml_event_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=statesml_Parameter_strategy)
@settings(max_examples=50)
def test_statesml_parameter_instantiation(instance):
    assert isinstance(instance, statesml_Parameter)



@given(instance=statesml_Parameter_strategy)
def test_statesml_parameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=statesml_IncomingParameter_strategy)
@settings(max_examples=50)
def test_statesml_incomingparameter_instantiation(instance):
    assert isinstance(instance, statesml_IncomingParameter)

@given(instance=statesml_ReturnParameter_strategy)
@settings(max_examples=50)
def test_statesml_returnparameter_instantiation(instance):
    assert isinstance(instance, statesml_ReturnParameter)

@given(instance=statesml_Edge_strategy)
@settings(max_examples=50)
def test_statesml_edge_instantiation(instance):
    assert isinstance(instance, statesml_Edge)



@given(instance=statesml_Edge_strategy)
def test_statesml_edge_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=statesml_Node_strategy)
@settings(max_examples=50)
def test_statesml_node_instantiation(instance):
    assert isinstance(instance, statesml_Node)



@given(instance=statesml_Node_strategy)
def test_statesml_node_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=statesml_StateSystem_strategy)
@settings(max_examples=50)
def test_statesml_statesystem_instantiation(instance):
    assert isinstance(instance, statesml_StateSystem)

@given(instance=statesml_StateSystemModel_strategy)
@settings(max_examples=50)
def test_statesml_statesystemmodel_instantiation(instance):
    assert isinstance(instance, statesml_StateSystemModel)



@given(instance=statesml_StateSystemModel_strategy)
def test_statesml_statesystemmodel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=statesml_SystemUnit_strategy)
@settings(max_examples=50)
def test_statesml_systemunit_instantiation(instance):
    assert isinstance(instance, statesml_SystemUnit)



@given(instance=statesml_SystemUnit_strategy)
def test_statesml_systemunit_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=statesml_Function_strategy)
@settings(max_examples=50)
def test_statesml_function_instantiation(instance):
    assert isinstance(instance, statesml_Function)



@given(instance=statesml_Function_strategy)
def test_statesml_function_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=statesml_SystemUnitLibrary_strategy)
@settings(max_examples=50)
def test_statesml_systemunitlibrary_instantiation(instance):
    assert isinstance(instance, statesml_SystemUnitLibrary)



@given(instance=statesml_SystemUnitLibrary_strategy)
def test_statesml_systemunitlibrary_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=statesml_DataTypeLibrary_strategy)
@settings(max_examples=50)
def test_statesml_datatypelibrary_instantiation(instance):
    assert isinstance(instance, statesml_DataTypeLibrary)



@given(instance=statesml_DataTypeLibrary_strategy)
def test_statesml_datatypelibrary_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=statesml_DataType_strategy)
@settings(max_examples=50)
def test_statesml_datatype_instantiation(instance):
    assert isinstance(instance, statesml_DataType)



@given(instance=statesml_DataType_strategy)
def test_statesml_datatype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=statesml_Attribute_strategy)
@settings(max_examples=50)
def test_statesml_attribute_instantiation(instance):
    assert isinstance(instance, statesml_Attribute)



@given(instance=statesml_Attribute_strategy)
def test_statesml_attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=statesml_StatesModel_strategy)
@settings(max_examples=50)
def test_statesml_statesmodel_instantiation(instance):
    assert isinstance(instance, statesml_StatesModel)

@given(instance=statesml_SystemUnitModel_strategy)
@settings(max_examples=50)
def test_statesml_systemunitmodel_instantiation(instance):
    assert isinstance(instance, statesml_SystemUnitModel)



@given(instance=statesml_SystemUnitModel_strategy)
def test_statesml_systemunitmodel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
