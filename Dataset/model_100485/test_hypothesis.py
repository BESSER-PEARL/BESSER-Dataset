import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    State,
    model_state_StateAutomaton,
    StateAutomaton,
    Var,
    model_state_Action,
    Action,
    model_state_TransitionSegmentSpecification,
    TransitionSegmentSpecification,
    TransitionSegment,
    IExpressionTerm,
    model_expression_BoolConst,
    model_expression_Var,
    model_expression_IExpressionTerm,
    model_INamedElement,
    Port,
    model_component_InputPort,
    model_component_OutputPort,
    INamedElement,
    model_state_DataStateVariable,
    model_component_Port,
    model_state_TransitionSegment,
    model_state_State,
    model_component_Component,
    model_expression_Operation,
    model_expression_IntConst,
    EOperator,
    EType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_model_state_stateautomaton_is_not_abstract():
    assert not inspect.isabstract(model_state_StateAutomaton)


def test_model_state_stateautomaton_constructor_exists():
    assert callable(model_state_StateAutomaton.__init__)


def test_model_state_stateautomaton_constructor_args():
    sig = inspect.signature(model_state_StateAutomaton.__init__)
    params = list(sig.parameters.keys())



def test_stateautomaton_is_not_abstract():
    assert not inspect.isabstract(StateAutomaton)


def test_stateautomaton_constructor_exists():
    assert callable(StateAutomaton.__init__)


def test_stateautomaton_constructor_args():
    sig = inspect.signature(StateAutomaton.__init__)
    params = list(sig.parameters.keys())



def test_var_is_not_abstract():
    assert not inspect.isabstract(Var)


def test_var_constructor_exists():
    assert callable(Var.__init__)


def test_var_constructor_args():
    sig = inspect.signature(Var.__init__)
    params = list(sig.parameters.keys())



def test_model_state_action_is_not_abstract():
    assert not inspect.isabstract(model_state_Action)


def test_model_state_action_constructor_exists():
    assert callable(model_state_Action.__init__)


def test_model_state_action_constructor_args():
    sig = inspect.signature(model_state_Action.__init__)
    params = list(sig.parameters.keys())



def test_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_action_constructor_exists():
    assert callable(Action.__init__)


def test_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_model_state_transitionsegmentspecification_is_not_abstract():
    assert not inspect.isabstract(model_state_TransitionSegmentSpecification)


def test_model_state_transitionsegmentspecification_constructor_exists():
    assert callable(model_state_TransitionSegmentSpecification.__init__)


def test_model_state_transitionsegmentspecification_constructor_args():
    sig = inspect.signature(model_state_TransitionSegmentSpecification.__init__)
    params = list(sig.parameters.keys())



def test_transitionsegmentspecification_is_not_abstract():
    assert not inspect.isabstract(TransitionSegmentSpecification)


def test_transitionsegmentspecification_constructor_exists():
    assert callable(TransitionSegmentSpecification.__init__)


def test_transitionsegmentspecification_constructor_args():
    sig = inspect.signature(TransitionSegmentSpecification.__init__)
    params = list(sig.parameters.keys())



def test_transitionsegment_is_not_abstract():
    assert not inspect.isabstract(TransitionSegment)


def test_transitionsegment_constructor_exists():
    assert callable(TransitionSegment.__init__)


def test_transitionsegment_constructor_args():
    sig = inspect.signature(TransitionSegment.__init__)
    params = list(sig.parameters.keys())



def test_iexpressionterm_is_not_abstract():
    assert not inspect.isabstract(IExpressionTerm)


def test_iexpressionterm_constructor_exists():
    assert callable(IExpressionTerm.__init__)


def test_iexpressionterm_constructor_args():
    sig = inspect.signature(IExpressionTerm.__init__)
    params = list(sig.parameters.keys())



def test_model_expression_boolconst_is_not_abstract():
    assert not inspect.isabstract(model_expression_BoolConst)


def test_model_expression_boolconst_constructor_exists():
    assert callable(model_expression_BoolConst.__init__)


def test_model_expression_boolconst_constructor_args():
    sig = inspect.signature(model_expression_BoolConst.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_model_expression_boolconst_has_value():
    assert hasattr(model_expression_BoolConst, "value")
    descriptor = None
    for klass in model_expression_BoolConst.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_model_expression_var_is_not_abstract():
    assert not inspect.isabstract(model_expression_Var)


def test_model_expression_var_constructor_exists():
    assert callable(model_expression_Var.__init__)


def test_model_expression_var_constructor_args():
    sig = inspect.signature(model_expression_Var.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"

def test_model_expression_var_has_identifier():
    assert hasattr(model_expression_Var, "identifier")
    descriptor = None
    for klass in model_expression_Var.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)



def test_model_expression_iexpressionterm_is_not_abstract():
    assert not inspect.isabstract(model_expression_IExpressionTerm)


def test_model_expression_iexpressionterm_constructor_exists():
    assert callable(model_expression_IExpressionTerm.__init__)


def test_model_expression_iexpressionterm_constructor_args():
    sig = inspect.signature(model_expression_IExpressionTerm.__init__)
    params = list(sig.parameters.keys())



def test_model_inamedelement_is_not_abstract():
    assert not inspect.isabstract(model_INamedElement)


def test_model_inamedelement_constructor_exists():
    assert callable(model_INamedElement.__init__)


def test_model_inamedelement_constructor_args():
    sig = inspect.signature(model_INamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_model_inamedelement_has_name():
    assert hasattr(model_INamedElement, "name")
    descriptor = None
    for klass in model_INamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_port_is_not_abstract():
    assert not inspect.isabstract(Port)


def test_port_constructor_exists():
    assert callable(Port.__init__)


def test_port_constructor_args():
    sig = inspect.signature(Port.__init__)
    params = list(sig.parameters.keys())



def test_model_component_inputport_is_not_abstract():
    assert not inspect.isabstract(model_component_InputPort)


def test_model_component_inputport_constructor_exists():
    assert callable(model_component_InputPort.__init__)


def test_model_component_inputport_constructor_args():
    sig = inspect.signature(model_component_InputPort.__init__)
    params = list(sig.parameters.keys())



def test_model_component_outputport_is_not_abstract():
    assert not inspect.isabstract(model_component_OutputPort)


def test_model_component_outputport_constructor_exists():
    assert callable(model_component_OutputPort.__init__)


def test_model_component_outputport_constructor_args():
    sig = inspect.signature(model_component_OutputPort.__init__)
    params = list(sig.parameters.keys())



def test_inamedelement_is_not_abstract():
    assert not inspect.isabstract(INamedElement)


def test_inamedelement_constructor_exists():
    assert callable(INamedElement.__init__)


def test_inamedelement_constructor_args():
    sig = inspect.signature(INamedElement.__init__)
    params = list(sig.parameters.keys())



def test_model_state_datastatevariable_is_not_abstract():
    assert not inspect.isabstract(model_state_DataStateVariable)


def test_model_state_datastatevariable_constructor_exists():
    assert callable(model_state_DataStateVariable.__init__)


def test_model_state_datastatevariable_constructor_args():
    sig = inspect.signature(model_state_DataStateVariable.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_model_state_datastatevariable_has_type():
    assert hasattr(model_state_DataStateVariable, "type")
    descriptor = None
    for klass in model_state_DataStateVariable.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_model_component_port_is_not_abstract():
    assert not inspect.isabstract(model_component_Port)


def test_model_component_port_constructor_exists():
    assert callable(model_component_Port.__init__)


def test_model_component_port_constructor_args():
    sig = inspect.signature(model_component_Port.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_model_component_port_has_type():
    assert hasattr(model_component_Port, "type")
    descriptor = None
    for klass in model_component_Port.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_model_state_transitionsegment_is_not_abstract():
    assert not inspect.isabstract(model_state_TransitionSegment)


def test_model_state_transitionsegment_constructor_exists():
    assert callable(model_state_TransitionSegment.__init__)


def test_model_state_transitionsegment_constructor_args():
    sig = inspect.signature(model_state_TransitionSegment.__init__)
    params = list(sig.parameters.keys())



def test_model_state_state_is_not_abstract():
    assert not inspect.isabstract(model_state_State)


def test_model_state_state_constructor_exists():
    assert callable(model_state_State.__init__)


def test_model_state_state_constructor_args():
    sig = inspect.signature(model_state_State.__init__)
    params = list(sig.parameters.keys())
    assert "isInitial" in params, "Missing parameter 'isInitial'"

def test_model_state_state_has_isInitial():
    assert hasattr(model_state_State, "isInitial")
    descriptor = None
    for klass in model_state_State.__mro__:
        if "isInitial" in klass.__dict__:
            descriptor = klass.__dict__["isInitial"]
            break
    assert isinstance(descriptor, property)



def test_model_component_component_is_not_abstract():
    assert not inspect.isabstract(model_component_Component)


def test_model_component_component_constructor_exists():
    assert callable(model_component_Component.__init__)


def test_model_component_component_constructor_args():
    sig = inspect.signature(model_component_Component.__init__)
    params = list(sig.parameters.keys())



def test_model_expression_operation_is_not_abstract():
    assert not inspect.isabstract(model_expression_Operation)


def test_model_expression_operation_constructor_exists():
    assert callable(model_expression_Operation.__init__)


def test_model_expression_operation_constructor_args():
    sig = inspect.signature(model_expression_Operation.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_model_expression_operation_has_operator():
    assert hasattr(model_expression_Operation, "operator")
    descriptor = None
    for klass in model_expression_Operation.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_model_expression_intconst_is_not_abstract():
    assert not inspect.isabstract(model_expression_IntConst)


def test_model_expression_intconst_constructor_exists():
    assert callable(model_expression_IntConst.__init__)


def test_model_expression_intconst_constructor_args():
    sig = inspect.signature(model_expression_IntConst.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_model_expression_intconst_has_value():
    assert hasattr(model_expression_IntConst, "value")
    descriptor = None
    for klass in model_expression_IntConst.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_eoperator_exists():
    # Check that the Enumeration exists
    assert EOperator is not None

def test_eoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EOperator]
    expected_literals = [
        "LowerThan",
        "GreaterEqual",
        "GreaterThan",
        "LowerEqual",
        "Multiply",
        "Subtract",
        "Add",
        "Equal",
        "Or",
        "NotEqual",
        "Divide",
        "Negate",
        "Not",
        "And",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EOperator"

def test_etype_exists():
    # Check that the Enumeration exists
    assert EType is not None

def test_etype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EType]
    expected_literals = [
        "TInt",
        "TBool",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EType"


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
State_strategy = st.builds(
    State,
)
model_state_StateAutomaton_strategy = st.builds(
    model_state_StateAutomaton,
)
StateAutomaton_strategy = st.builds(
    StateAutomaton,
)
Var_strategy = st.builds(
    Var,
)
model_state_Action_strategy = st.builds(
    model_state_Action,
)
Action_strategy = st.builds(
    Action,
)
model_state_TransitionSegmentSpecification_strategy = st.builds(
    model_state_TransitionSegmentSpecification,
)
TransitionSegmentSpecification_strategy = st.builds(
    TransitionSegmentSpecification,
)
TransitionSegment_strategy = st.builds(
    TransitionSegment,
)
IExpressionTerm_strategy = st.builds(
    IExpressionTerm,
)
model_expression_BoolConst_strategy = st.builds(
    model_expression_BoolConst,
    value=
        st.booleans()
)
model_expression_Var_strategy = st.builds(
    model_expression_Var,
    identifier=
        safe_text
)
model_expression_IExpressionTerm_strategy = st.builds(
    model_expression_IExpressionTerm,
)
model_INamedElement_strategy = st.builds(
    model_INamedElement,
    name=
        safe_text
)
Port_strategy = st.builds(
    Port,
)
model_component_InputPort_strategy = st.builds(
    model_component_InputPort,
)
model_component_OutputPort_strategy = st.builds(
    model_component_OutputPort,
)
INamedElement_strategy = st.builds(
    INamedElement,
)
model_state_DataStateVariable_strategy = st.builds(
    model_state_DataStateVariable,
    type=
        safe_text
)
model_component_Port_strategy = st.builds(
    model_component_Port,
    type=
        safe_text
)
model_state_TransitionSegment_strategy = st.builds(
    model_state_TransitionSegment,
)
model_state_State_strategy = st.builds(
    model_state_State,
    isInitial=
        st.booleans()
)
model_component_Component_strategy = st.builds(
    model_component_Component,
)
model_expression_Operation_strategy = st.builds(
    model_expression_Operation,
    operator=
        safe_text
)
model_expression_IntConst_strategy = st.builds(
    model_expression_IntConst,
    value=
        st.integers()
)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=model_state_StateAutomaton_strategy)
@settings(max_examples=50)
def test_model_state_stateautomaton_instantiation(instance):
    assert isinstance(instance, model_state_StateAutomaton)

@given(instance=StateAutomaton_strategy)
@settings(max_examples=50)
def test_stateautomaton_instantiation(instance):
    assert isinstance(instance, StateAutomaton)

@given(instance=Var_strategy)
@settings(max_examples=50)
def test_var_instantiation(instance):
    assert isinstance(instance, Var)

@given(instance=model_state_Action_strategy)
@settings(max_examples=50)
def test_model_state_action_instantiation(instance):
    assert isinstance(instance, model_state_Action)

@given(instance=Action_strategy)
@settings(max_examples=50)
def test_action_instantiation(instance):
    assert isinstance(instance, Action)

@given(instance=model_state_TransitionSegmentSpecification_strategy)
@settings(max_examples=50)
def test_model_state_transitionsegmentspecification_instantiation(instance):
    assert isinstance(instance, model_state_TransitionSegmentSpecification)

@given(instance=TransitionSegmentSpecification_strategy)
@settings(max_examples=50)
def test_transitionsegmentspecification_instantiation(instance):
    assert isinstance(instance, TransitionSegmentSpecification)

@given(instance=TransitionSegment_strategy)
@settings(max_examples=50)
def test_transitionsegment_instantiation(instance):
    assert isinstance(instance, TransitionSegment)

@given(instance=IExpressionTerm_strategy)
@settings(max_examples=50)
def test_iexpressionterm_instantiation(instance):
    assert isinstance(instance, IExpressionTerm)

@given(instance=model_expression_BoolConst_strategy)
@settings(max_examples=50)
def test_model_expression_boolconst_instantiation(instance):
    assert isinstance(instance, model_expression_BoolConst)



@given(instance=model_expression_BoolConst_strategy)
def test_model_expression_boolconst_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=model_expression_Var_strategy)
@settings(max_examples=50)
def test_model_expression_var_instantiation(instance):
    assert isinstance(instance, model_expression_Var)



@given(instance=model_expression_Var_strategy)
def test_model_expression_var_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=model_expression_IExpressionTerm_strategy)
@settings(max_examples=50)
def test_model_expression_iexpressionterm_instantiation(instance):
    assert isinstance(instance, model_expression_IExpressionTerm)

@given(instance=model_INamedElement_strategy)
@settings(max_examples=50)
def test_model_inamedelement_instantiation(instance):
    assert isinstance(instance, model_INamedElement)



@given(instance=model_INamedElement_strategy)
def test_model_inamedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Port_strategy)
@settings(max_examples=50)
def test_port_instantiation(instance):
    assert isinstance(instance, Port)

@given(instance=model_component_InputPort_strategy)
@settings(max_examples=50)
def test_model_component_inputport_instantiation(instance):
    assert isinstance(instance, model_component_InputPort)

@given(instance=model_component_OutputPort_strategy)
@settings(max_examples=50)
def test_model_component_outputport_instantiation(instance):
    assert isinstance(instance, model_component_OutputPort)

@given(instance=INamedElement_strategy)
@settings(max_examples=50)
def test_inamedelement_instantiation(instance):
    assert isinstance(instance, INamedElement)

@given(instance=model_state_DataStateVariable_strategy)
@settings(max_examples=50)
def test_model_state_datastatevariable_instantiation(instance):
    assert isinstance(instance, model_state_DataStateVariable)



@given(instance=model_state_DataStateVariable_strategy)
def test_model_state_datastatevariable_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=model_component_Port_strategy)
@settings(max_examples=50)
def test_model_component_port_instantiation(instance):
    assert isinstance(instance, model_component_Port)



@given(instance=model_component_Port_strategy)
def test_model_component_port_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=model_state_TransitionSegment_strategy)
@settings(max_examples=50)
def test_model_state_transitionsegment_instantiation(instance):
    assert isinstance(instance, model_state_TransitionSegment)

@given(instance=model_state_State_strategy)
@settings(max_examples=50)
def test_model_state_state_instantiation(instance):
    assert isinstance(instance, model_state_State)



@given(instance=model_state_State_strategy)
def test_model_state_state_isInitial_setter(instance):
    original = instance.isInitial
    instance.isInitial = original
    assert instance.isInitial == original

@given(instance=model_component_Component_strategy)
@settings(max_examples=50)
def test_model_component_component_instantiation(instance):
    assert isinstance(instance, model_component_Component)

@given(instance=model_expression_Operation_strategy)
@settings(max_examples=50)
def test_model_expression_operation_instantiation(instance):
    assert isinstance(instance, model_expression_Operation)



@given(instance=model_expression_Operation_strategy)
def test_model_expression_operation_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=model_expression_IntConst_strategy)
@settings(max_examples=50)
def test_model_expression_intconst_instantiation(instance):
    assert isinstance(instance, model_expression_IntConst)



@given(instance=model_expression_IntConst_strategy)
def test_model_expression_intconst_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original
