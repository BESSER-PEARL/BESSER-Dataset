import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    syswbeff1065ok_Workbench,
    syswbeff1065ok_PatternCatalog,
    syswbeff1065ok_System,
    syswbeff1065ok_Thoughts,
    syswbeff1065ok_Thing,
    syswbeff1065ok_AssociatedTo,
    syswbeff1065ok_ProcessNode,
    syswbeff1065ok_Item,
    syswbeff1065ok_Port,
    Port,
    Sequence,
    syswbeff1065ok_Start,
    syswbeff1065ok_Or,
    syswbeff1065ok_LoopExit,
    syswbeff1065ok_Iteration,
    syswbeff1065ok_And,
    syswbeff1065ok_SequenceNode,
    syswbeff1065ok_Component,
    syswbeff1065ok_FunctionProperty,
    syswbeff1065ok_Loop,
    syswbeff1065ok_Final,
    syswbeff1065ok_OutputPort,
    ProcessNode,
    syswbeff1065ok_Flow,
    SequenceNode,
    syswbeff1065ok_Sequence,
    syswbeff1065ok_Function,
    syswbeff1065ok_Token,
    syswbeff1065ok_Description,
    syswbeff1065ok_InputPort,
    FunctionDomain,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_syswbeff1065ok_workbench_is_not_abstract():
    assert not inspect.isabstract(syswbeff1065ok_Workbench)


def test_syswbeff1065ok_workbench_constructor_exists():
    assert callable(syswbeff1065ok_Workbench.__init__)


def test_syswbeff1065ok_workbench_constructor_args():
    sig = inspect.signature(syswbeff1065ok_Workbench.__init__)
    params = list(sig.parameters.keys())



def test_syswbeff1065ok_patterncatalog_is_not_abstract():
    assert not inspect.isabstract(syswbeff1065ok_PatternCatalog)


def test_syswbeff1065ok_patterncatalog_constructor_exists():
    assert callable(syswbeff1065ok_PatternCatalog.__init__)


def test_syswbeff1065ok_patterncatalog_constructor_args():
    sig = inspect.signature(syswbeff1065ok_PatternCatalog.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_syswbeff1065ok_patterncatalog_has_id():
    assert hasattr(syswbeff1065ok_PatternCatalog, "id")
    descriptor = None
    for klass in syswbeff1065ok_PatternCatalog.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_syswbeff1065ok_system_is_not_abstract():
    assert not inspect.isabstract(syswbeff1065ok_System)


def test_syswbeff1065ok_system_constructor_exists():
    assert callable(syswbeff1065ok_System.__init__)


def test_syswbeff1065ok_system_constructor_args():
    sig = inspect.signature(syswbeff1065ok_System.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_syswbeff1065ok_system_has_id():
    assert hasattr(syswbeff1065ok_System, "id")
    descriptor = None
    for klass in syswbeff1065ok_System.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_syswbeff1065ok_thoughts_is_not_abstract():
    assert not inspect.isabstract(syswbeff1065ok_Thoughts)


def test_syswbeff1065ok_thoughts_constructor_exists():
    assert callable(syswbeff1065ok_Thoughts.__init__)


def test_syswbeff1065ok_thoughts_constructor_args():
    sig = inspect.signature(syswbeff1065ok_Thoughts.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_syswbeff1065ok_thoughts_has_id():
    assert hasattr(syswbeff1065ok_Thoughts, "id")
    descriptor = None
    for klass in syswbeff1065ok_Thoughts.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_syswbeff1065ok_thing_is_not_abstract():
    assert not inspect.isabstract(syswbeff1065ok_Thing)


def test_syswbeff1065ok_thing_constructor_exists():
    assert callable(syswbeff1065ok_Thing.__init__)


def test_syswbeff1065ok_thing_constructor_args():
    sig = inspect.signature(syswbeff1065ok_Thing.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_syswbeff1065ok_thing_has_id():
    assert hasattr(syswbeff1065ok_Thing, "id")
    descriptor = None
    for klass in syswbeff1065ok_Thing.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_syswbeff1065ok_associatedto_is_not_abstract():
    assert not inspect.isabstract(syswbeff1065ok_AssociatedTo)


def test_syswbeff1065ok_associatedto_constructor_exists():
    assert callable(syswbeff1065ok_AssociatedTo.__init__)


def test_syswbeff1065ok_associatedto_constructor_args():
    sig = inspect.signature(syswbeff1065ok_AssociatedTo.__init__)
    params = list(sig.parameters.keys())
    assert "since" in params, "Missing parameter 'since'"

def test_syswbeff1065ok_associatedto_has_since():
    assert hasattr(syswbeff1065ok_AssociatedTo, "since")
    descriptor = None
    for klass in syswbeff1065ok_AssociatedTo.__mro__:
        if "since" in klass.__dict__:
            descriptor = klass.__dict__["since"]
            break
    assert isinstance(descriptor, property)



def test_syswbeff1065ok_processnode_is_not_abstract():
    assert not inspect.isabstract(syswbeff1065ok_ProcessNode)


def test_syswbeff1065ok_processnode_constructor_exists():
    assert callable(syswbeff1065ok_ProcessNode.__init__)


def test_syswbeff1065ok_processnode_constructor_args():
    sig = inspect.signature(syswbeff1065ok_ProcessNode.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_syswbeff1065ok_processnode_has_label():
    assert hasattr(syswbeff1065ok_ProcessNode, "label")
    descriptor = None
    for klass in syswbeff1065ok_ProcessNode.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_syswbeff1065ok_item_is_not_abstract():
    assert not inspect.isabstract(syswbeff1065ok_Item)


def test_syswbeff1065ok_item_constructor_exists():
    assert callable(syswbeff1065ok_Item.__init__)


def test_syswbeff1065ok_item_constructor_args():
    sig = inspect.signature(syswbeff1065ok_Item.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_syswbeff1065ok_item_has_name():
    assert hasattr(syswbeff1065ok_Item, "name")
    descriptor = None
    for klass in syswbeff1065ok_Item.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_syswbeff1065ok_port_is_not_abstract():
    assert not inspect.isabstract(syswbeff1065ok_Port)


def test_syswbeff1065ok_port_constructor_exists():
    assert callable(syswbeff1065ok_Port.__init__)


def test_syswbeff1065ok_port_constructor_args():
    sig = inspect.signature(syswbeff1065ok_Port.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_syswbeff1065ok_port_has_id():
    assert hasattr(syswbeff1065ok_Port, "id")
    descriptor = None
    for klass in syswbeff1065ok_Port.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_port_is_not_abstract():
    assert not inspect.isabstract(Port)


def test_port_constructor_exists():
    assert callable(Port.__init__)


def test_port_constructor_args():
    sig = inspect.signature(Port.__init__)
    params = list(sig.parameters.keys())



def test_sequence_is_not_abstract():
    assert not inspect.isabstract(Sequence)


def test_sequence_constructor_exists():
    assert callable(Sequence.__init__)


def test_sequence_constructor_args():
    sig = inspect.signature(Sequence.__init__)
    params = list(sig.parameters.keys())



def test_syswbeff1065ok_start_is_not_abstract():
    assert not inspect.isabstract(syswbeff1065ok_Start)


def test_syswbeff1065ok_start_constructor_exists():
    assert callable(syswbeff1065ok_Start.__init__)


def test_syswbeff1065ok_start_constructor_args():
    sig = inspect.signature(syswbeff1065ok_Start.__init__)
    params = list(sig.parameters.keys())



def test_syswbeff1065ok_or_is_not_abstract():
    assert not inspect.isabstract(syswbeff1065ok_Or)


def test_syswbeff1065ok_or_constructor_exists():
    assert callable(syswbeff1065ok_Or.__init__)


def test_syswbeff1065ok_or_constructor_args():
    sig = inspect.signature(syswbeff1065ok_Or.__init__)
    params = list(sig.parameters.keys())



def test_syswbeff1065ok_loopexit_is_not_abstract():
    assert not inspect.isabstract(syswbeff1065ok_LoopExit)


def test_syswbeff1065ok_loopexit_constructor_exists():
    assert callable(syswbeff1065ok_LoopExit.__init__)


def test_syswbeff1065ok_loopexit_constructor_args():
    sig = inspect.signature(syswbeff1065ok_LoopExit.__init__)
    params = list(sig.parameters.keys())



def test_syswbeff1065ok_iteration_is_not_abstract():
    assert not inspect.isabstract(syswbeff1065ok_Iteration)


def test_syswbeff1065ok_iteration_constructor_exists():
    assert callable(syswbeff1065ok_Iteration.__init__)


def test_syswbeff1065ok_iteration_constructor_args():
    sig = inspect.signature(syswbeff1065ok_Iteration.__init__)
    params = list(sig.parameters.keys())



def test_syswbeff1065ok_and_is_not_abstract():
    assert not inspect.isabstract(syswbeff1065ok_And)


def test_syswbeff1065ok_and_constructor_exists():
    assert callable(syswbeff1065ok_And.__init__)


def test_syswbeff1065ok_and_constructor_args():
    sig = inspect.signature(syswbeff1065ok_And.__init__)
    params = list(sig.parameters.keys())



def test_syswbeff1065ok_sequencenode_is_not_abstract():
    assert not inspect.isabstract(syswbeff1065ok_SequenceNode)


def test_syswbeff1065ok_sequencenode_constructor_exists():
    assert callable(syswbeff1065ok_SequenceNode.__init__)


def test_syswbeff1065ok_sequencenode_constructor_args():
    sig = inspect.signature(syswbeff1065ok_SequenceNode.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "tMax" in params, "Missing parameter 'tMax'"
    assert "tMin" in params, "Missing parameter 'tMin'"

def test_syswbeff1065ok_sequencenode_has_name():
    assert hasattr(syswbeff1065ok_SequenceNode, "name")
    descriptor = None
    for klass in syswbeff1065ok_SequenceNode.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_syswbeff1065ok_sequencenode_has_tMax():
    assert hasattr(syswbeff1065ok_SequenceNode, "tMax")
    descriptor = None
    for klass in syswbeff1065ok_SequenceNode.__mro__:
        if "tMax" in klass.__dict__:
            descriptor = klass.__dict__["tMax"]
            break
    assert isinstance(descriptor, property)

def test_syswbeff1065ok_sequencenode_has_tMin():
    assert hasattr(syswbeff1065ok_SequenceNode, "tMin")
    descriptor = None
    for klass in syswbeff1065ok_SequenceNode.__mro__:
        if "tMin" in klass.__dict__:
            descriptor = klass.__dict__["tMin"]
            break
    assert isinstance(descriptor, property)



def test_syswbeff1065ok_component_is_not_abstract():
    assert not inspect.isabstract(syswbeff1065ok_Component)


def test_syswbeff1065ok_component_constructor_exists():
    assert callable(syswbeff1065ok_Component.__init__)


def test_syswbeff1065ok_component_constructor_args():
    sig = inspect.signature(syswbeff1065ok_Component.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_syswbeff1065ok_component_has_name():
    assert hasattr(syswbeff1065ok_Component, "name")
    descriptor = None
    for klass in syswbeff1065ok_Component.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_syswbeff1065ok_functionproperty_is_not_abstract():
    assert not inspect.isabstract(syswbeff1065ok_FunctionProperty)


def test_syswbeff1065ok_functionproperty_constructor_exists():
    assert callable(syswbeff1065ok_FunctionProperty.__init__)


def test_syswbeff1065ok_functionproperty_constructor_args():
    sig = inspect.signature(syswbeff1065ok_FunctionProperty.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"

def test_syswbeff1065ok_functionproperty_has_description():
    assert hasattr(syswbeff1065ok_FunctionProperty, "description")
    descriptor = None
    for klass in syswbeff1065ok_FunctionProperty.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_syswbeff1065ok_loop_is_not_abstract():
    assert not inspect.isabstract(syswbeff1065ok_Loop)


def test_syswbeff1065ok_loop_constructor_exists():
    assert callable(syswbeff1065ok_Loop.__init__)


def test_syswbeff1065ok_loop_constructor_args():
    sig = inspect.signature(syswbeff1065ok_Loop.__init__)
    params = list(sig.parameters.keys())



def test_syswbeff1065ok_final_is_not_abstract():
    assert not inspect.isabstract(syswbeff1065ok_Final)


def test_syswbeff1065ok_final_constructor_exists():
    assert callable(syswbeff1065ok_Final.__init__)


def test_syswbeff1065ok_final_constructor_args():
    sig = inspect.signature(syswbeff1065ok_Final.__init__)
    params = list(sig.parameters.keys())



def test_syswbeff1065ok_outputport_is_not_abstract():
    assert not inspect.isabstract(syswbeff1065ok_OutputPort)


def test_syswbeff1065ok_outputport_constructor_exists():
    assert callable(syswbeff1065ok_OutputPort.__init__)


def test_syswbeff1065ok_outputport_constructor_args():
    sig = inspect.signature(syswbeff1065ok_OutputPort.__init__)
    params = list(sig.parameters.keys())



def test_processnode_is_not_abstract():
    assert not inspect.isabstract(ProcessNode)


def test_processnode_constructor_exists():
    assert callable(ProcessNode.__init__)


def test_processnode_constructor_args():
    sig = inspect.signature(ProcessNode.__init__)
    params = list(sig.parameters.keys())



def test_syswbeff1065ok_flow_is_not_abstract():
    assert not inspect.isabstract(syswbeff1065ok_Flow)


def test_syswbeff1065ok_flow_constructor_exists():
    assert callable(syswbeff1065ok_Flow.__init__)


def test_syswbeff1065ok_flow_constructor_args():
    sig = inspect.signature(syswbeff1065ok_Flow.__init__)
    params = list(sig.parameters.keys())



def test_sequencenode_is_not_abstract():
    assert not inspect.isabstract(SequenceNode)


def test_sequencenode_constructor_exists():
    assert callable(SequenceNode.__init__)


def test_sequencenode_constructor_args():
    sig = inspect.signature(SequenceNode.__init__)
    params = list(sig.parameters.keys())



def test_syswbeff1065ok_sequence_is_not_abstract():
    assert not inspect.isabstract(syswbeff1065ok_Sequence)


def test_syswbeff1065ok_sequence_constructor_exists():
    assert callable(syswbeff1065ok_Sequence.__init__)


def test_syswbeff1065ok_sequence_constructor_args():
    sig = inspect.signature(syswbeff1065ok_Sequence.__init__)
    params = list(sig.parameters.keys())



def test_syswbeff1065ok_function_is_not_abstract():
    assert not inspect.isabstract(syswbeff1065ok_Function)


def test_syswbeff1065ok_function_constructor_exists():
    assert callable(syswbeff1065ok_Function.__init__)


def test_syswbeff1065ok_function_constructor_args():
    sig = inspect.signature(syswbeff1065ok_Function.__init__)
    params = list(sig.parameters.keys())
    assert "domain" in params, "Missing parameter 'domain'"

def test_syswbeff1065ok_function_has_domain():
    assert hasattr(syswbeff1065ok_Function, "domain")
    descriptor = None
    for klass in syswbeff1065ok_Function.__mro__:
        if "domain" in klass.__dict__:
            descriptor = klass.__dict__["domain"]
            break
    assert isinstance(descriptor, property)



def test_syswbeff1065ok_token_is_not_abstract():
    assert not inspect.isabstract(syswbeff1065ok_Token)


def test_syswbeff1065ok_token_constructor_exists():
    assert callable(syswbeff1065ok_Token.__init__)


def test_syswbeff1065ok_token_constructor_args():
    sig = inspect.signature(syswbeff1065ok_Token.__init__)
    params = list(sig.parameters.keys())



def test_syswbeff1065ok_description_is_not_abstract():
    assert not inspect.isabstract(syswbeff1065ok_Description)


def test_syswbeff1065ok_description_constructor_exists():
    assert callable(syswbeff1065ok_Description.__init__)


def test_syswbeff1065ok_description_constructor_args():
    sig = inspect.signature(syswbeff1065ok_Description.__init__)
    params = list(sig.parameters.keys())
    assert "content" in params, "Missing parameter 'content'"

def test_syswbeff1065ok_description_has_content():
    assert hasattr(syswbeff1065ok_Description, "content")
    descriptor = None
    for klass in syswbeff1065ok_Description.__mro__:
        if "content" in klass.__dict__:
            descriptor = klass.__dict__["content"]
            break
    assert isinstance(descriptor, property)



def test_syswbeff1065ok_inputport_is_not_abstract():
    assert not inspect.isabstract(syswbeff1065ok_InputPort)


def test_syswbeff1065ok_inputport_constructor_exists():
    assert callable(syswbeff1065ok_InputPort.__init__)


def test_syswbeff1065ok_inputport_constructor_args():
    sig = inspect.signature(syswbeff1065ok_InputPort.__init__)
    params = list(sig.parameters.keys())

def test_functiondomain_exists():
    # Check that the Enumeration exists
    assert FunctionDomain is not None

def test_functiondomain_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FunctionDomain]
    expected_literals = [
        "time",
        "space",
        "form",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FunctionDomain"


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
syswbeff1065ok_Workbench_strategy = st.builds(
    syswbeff1065ok_Workbench,
)
syswbeff1065ok_PatternCatalog_strategy = st.builds(
    syswbeff1065ok_PatternCatalog,
    id=
        safe_text
)
syswbeff1065ok_System_strategy = st.builds(
    syswbeff1065ok_System,
    id=
        safe_text
)
syswbeff1065ok_Thoughts_strategy = st.builds(
    syswbeff1065ok_Thoughts,
    id=
        safe_text
)
syswbeff1065ok_Thing_strategy = st.builds(
    syswbeff1065ok_Thing,
    id=
        st.integers()
)
syswbeff1065ok_AssociatedTo_strategy = st.builds(
    syswbeff1065ok_AssociatedTo,
    since=
        safe_text
)
syswbeff1065ok_ProcessNode_strategy = st.builds(
    syswbeff1065ok_ProcessNode,
    label=
        safe_text
)
syswbeff1065ok_Item_strategy = st.builds(
    syswbeff1065ok_Item,
    name=
        safe_text
)
syswbeff1065ok_Port_strategy = st.builds(
    syswbeff1065ok_Port,
    id=
        safe_text
)
Port_strategy = st.builds(
    Port,
)
Sequence_strategy = st.builds(
    Sequence,
)
syswbeff1065ok_Start_strategy = st.builds(
    syswbeff1065ok_Start,
)
syswbeff1065ok_Or_strategy = st.builds(
    syswbeff1065ok_Or,
)
syswbeff1065ok_LoopExit_strategy = st.builds(
    syswbeff1065ok_LoopExit,
)
syswbeff1065ok_Iteration_strategy = st.builds(
    syswbeff1065ok_Iteration,
)
syswbeff1065ok_And_strategy = st.builds(
    syswbeff1065ok_And,
)
syswbeff1065ok_SequenceNode_strategy = st.builds(
    syswbeff1065ok_SequenceNode,
    name=
        safe_text,
    tMax=
        st.integers(),
    tMin=
        st.integers()
)
syswbeff1065ok_Component_strategy = st.builds(
    syswbeff1065ok_Component,
    name=
        safe_text
)
syswbeff1065ok_FunctionProperty_strategy = st.builds(
    syswbeff1065ok_FunctionProperty,
    description=
        safe_text
)
syswbeff1065ok_Loop_strategy = st.builds(
    syswbeff1065ok_Loop,
)
syswbeff1065ok_Final_strategy = st.builds(
    syswbeff1065ok_Final,
)
syswbeff1065ok_OutputPort_strategy = st.builds(
    syswbeff1065ok_OutputPort,
)
ProcessNode_strategy = st.builds(
    ProcessNode,
)
syswbeff1065ok_Flow_strategy = st.builds(
    syswbeff1065ok_Flow,
)
SequenceNode_strategy = st.builds(
    SequenceNode,
)
syswbeff1065ok_Sequence_strategy = st.builds(
    syswbeff1065ok_Sequence,
)
syswbeff1065ok_Function_strategy = st.builds(
    syswbeff1065ok_Function,
    domain=
        safe_text
)
syswbeff1065ok_Token_strategy = st.builds(
    syswbeff1065ok_Token,
)
syswbeff1065ok_Description_strategy = st.builds(
    syswbeff1065ok_Description,
    content=
        safe_text
)
syswbeff1065ok_InputPort_strategy = st.builds(
    syswbeff1065ok_InputPort,
)

@given(instance=syswbeff1065ok_Workbench_strategy)
@settings(max_examples=50)
def test_syswbeff1065ok_workbench_instantiation(instance):
    assert isinstance(instance, syswbeff1065ok_Workbench)

@given(instance=syswbeff1065ok_PatternCatalog_strategy)
@settings(max_examples=50)
def test_syswbeff1065ok_patterncatalog_instantiation(instance):
    assert isinstance(instance, syswbeff1065ok_PatternCatalog)



@given(instance=syswbeff1065ok_PatternCatalog_strategy)
def test_syswbeff1065ok_patterncatalog_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=syswbeff1065ok_System_strategy)
@settings(max_examples=50)
def test_syswbeff1065ok_system_instantiation(instance):
    assert isinstance(instance, syswbeff1065ok_System)



@given(instance=syswbeff1065ok_System_strategy)
def test_syswbeff1065ok_system_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=syswbeff1065ok_Thoughts_strategy)
@settings(max_examples=50)
def test_syswbeff1065ok_thoughts_instantiation(instance):
    assert isinstance(instance, syswbeff1065ok_Thoughts)



@given(instance=syswbeff1065ok_Thoughts_strategy)
def test_syswbeff1065ok_thoughts_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=syswbeff1065ok_Thing_strategy)
@settings(max_examples=50)
def test_syswbeff1065ok_thing_instantiation(instance):
    assert isinstance(instance, syswbeff1065ok_Thing)



@given(instance=syswbeff1065ok_Thing_strategy)
def test_syswbeff1065ok_thing_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=syswbeff1065ok_AssociatedTo_strategy)
@settings(max_examples=50)
def test_syswbeff1065ok_associatedto_instantiation(instance):
    assert isinstance(instance, syswbeff1065ok_AssociatedTo)



@given(instance=syswbeff1065ok_AssociatedTo_strategy)
def test_syswbeff1065ok_associatedto_since_setter(instance):
    original = instance.since
    instance.since = original
    assert instance.since == original

@given(instance=syswbeff1065ok_ProcessNode_strategy)
@settings(max_examples=50)
def test_syswbeff1065ok_processnode_instantiation(instance):
    assert isinstance(instance, syswbeff1065ok_ProcessNode)



@given(instance=syswbeff1065ok_ProcessNode_strategy)
def test_syswbeff1065ok_processnode_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=syswbeff1065ok_Item_strategy)
@settings(max_examples=50)
def test_syswbeff1065ok_item_instantiation(instance):
    assert isinstance(instance, syswbeff1065ok_Item)



@given(instance=syswbeff1065ok_Item_strategy)
def test_syswbeff1065ok_item_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=syswbeff1065ok_Port_strategy)
@settings(max_examples=50)
def test_syswbeff1065ok_port_instantiation(instance):
    assert isinstance(instance, syswbeff1065ok_Port)



@given(instance=syswbeff1065ok_Port_strategy)
def test_syswbeff1065ok_port_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Port_strategy)
@settings(max_examples=50)
def test_port_instantiation(instance):
    assert isinstance(instance, Port)

@given(instance=Sequence_strategy)
@settings(max_examples=50)
def test_sequence_instantiation(instance):
    assert isinstance(instance, Sequence)

@given(instance=syswbeff1065ok_Start_strategy)
@settings(max_examples=50)
def test_syswbeff1065ok_start_instantiation(instance):
    assert isinstance(instance, syswbeff1065ok_Start)

@given(instance=syswbeff1065ok_Or_strategy)
@settings(max_examples=50)
def test_syswbeff1065ok_or_instantiation(instance):
    assert isinstance(instance, syswbeff1065ok_Or)

@given(instance=syswbeff1065ok_LoopExit_strategy)
@settings(max_examples=50)
def test_syswbeff1065ok_loopexit_instantiation(instance):
    assert isinstance(instance, syswbeff1065ok_LoopExit)

@given(instance=syswbeff1065ok_Iteration_strategy)
@settings(max_examples=50)
def test_syswbeff1065ok_iteration_instantiation(instance):
    assert isinstance(instance, syswbeff1065ok_Iteration)

@given(instance=syswbeff1065ok_And_strategy)
@settings(max_examples=50)
def test_syswbeff1065ok_and_instantiation(instance):
    assert isinstance(instance, syswbeff1065ok_And)

@given(instance=syswbeff1065ok_SequenceNode_strategy)
@settings(max_examples=50)
def test_syswbeff1065ok_sequencenode_instantiation(instance):
    assert isinstance(instance, syswbeff1065ok_SequenceNode)



@given(instance=syswbeff1065ok_SequenceNode_strategy)
def test_syswbeff1065ok_sequencenode_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=syswbeff1065ok_SequenceNode_strategy)
def test_syswbeff1065ok_sequencenode_tMax_setter(instance):
    original = instance.tMax
    instance.tMax = original
    assert instance.tMax == original



@given(instance=syswbeff1065ok_SequenceNode_strategy)
def test_syswbeff1065ok_sequencenode_tMin_setter(instance):
    original = instance.tMin
    instance.tMin = original
    assert instance.tMin == original

@given(instance=syswbeff1065ok_Component_strategy)
@settings(max_examples=50)
def test_syswbeff1065ok_component_instantiation(instance):
    assert isinstance(instance, syswbeff1065ok_Component)



@given(instance=syswbeff1065ok_Component_strategy)
def test_syswbeff1065ok_component_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=syswbeff1065ok_FunctionProperty_strategy)
@settings(max_examples=50)
def test_syswbeff1065ok_functionproperty_instantiation(instance):
    assert isinstance(instance, syswbeff1065ok_FunctionProperty)



@given(instance=syswbeff1065ok_FunctionProperty_strategy)
def test_syswbeff1065ok_functionproperty_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=syswbeff1065ok_Loop_strategy)
@settings(max_examples=50)
def test_syswbeff1065ok_loop_instantiation(instance):
    assert isinstance(instance, syswbeff1065ok_Loop)

@given(instance=syswbeff1065ok_Final_strategy)
@settings(max_examples=50)
def test_syswbeff1065ok_final_instantiation(instance):
    assert isinstance(instance, syswbeff1065ok_Final)

@given(instance=syswbeff1065ok_OutputPort_strategy)
@settings(max_examples=50)
def test_syswbeff1065ok_outputport_instantiation(instance):
    assert isinstance(instance, syswbeff1065ok_OutputPort)

@given(instance=ProcessNode_strategy)
@settings(max_examples=50)
def test_processnode_instantiation(instance):
    assert isinstance(instance, ProcessNode)

@given(instance=syswbeff1065ok_Flow_strategy)
@settings(max_examples=50)
def test_syswbeff1065ok_flow_instantiation(instance):
    assert isinstance(instance, syswbeff1065ok_Flow)

@given(instance=SequenceNode_strategy)
@settings(max_examples=50)
def test_sequencenode_instantiation(instance):
    assert isinstance(instance, SequenceNode)

@given(instance=syswbeff1065ok_Sequence_strategy)
@settings(max_examples=50)
def test_syswbeff1065ok_sequence_instantiation(instance):
    assert isinstance(instance, syswbeff1065ok_Sequence)

@given(instance=syswbeff1065ok_Function_strategy)
@settings(max_examples=50)
def test_syswbeff1065ok_function_instantiation(instance):
    assert isinstance(instance, syswbeff1065ok_Function)



@given(instance=syswbeff1065ok_Function_strategy)
def test_syswbeff1065ok_function_domain_setter(instance):
    original = instance.domain
    instance.domain = original
    assert instance.domain == original

@given(instance=syswbeff1065ok_Token_strategy)
@settings(max_examples=50)
def test_syswbeff1065ok_token_instantiation(instance):
    assert isinstance(instance, syswbeff1065ok_Token)

@given(instance=syswbeff1065ok_Description_strategy)
@settings(max_examples=50)
def test_syswbeff1065ok_description_instantiation(instance):
    assert isinstance(instance, syswbeff1065ok_Description)



@given(instance=syswbeff1065ok_Description_strategy)
def test_syswbeff1065ok_description_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original

@given(instance=syswbeff1065ok_InputPort_strategy)
@settings(max_examples=50)
def test_syswbeff1065ok_inputport_instantiation(instance):
    assert isinstance(instance, syswbeff1065ok_InputPort)
