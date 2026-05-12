import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    myffbd_Item,
    myffbd_Flow,
    myffbd_Port,
    Port,
    myffbd_InputPort,
    myffbd_OutputPort,
    myffbd_SequenceNode,
    myffbd_PortType,
    myffbd_Token,
    myffbd_Description,
    SequenceNode,
    myffbd_And,
    myffbd_Start,
    myffbd_LoopExit,
    myffbd_Iteration,
    myffbd_Final,
    myffbd_Loop,
    myffbd_Or,
    myffbd_Function,
    FunctionDomain,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_myffbd_item_is_not_abstract():
    assert not inspect.isabstract(myffbd_Item)


def test_myffbd_item_constructor_exists():
    assert callable(myffbd_Item.__init__)


def test_myffbd_item_constructor_args():
    sig = inspect.signature(myffbd_Item.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_myffbd_item_has_name():
    assert hasattr(myffbd_Item, "name")
    descriptor = None
    for klass in myffbd_Item.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_myffbd_flow_is_not_abstract():
    assert not inspect.isabstract(myffbd_Flow)


def test_myffbd_flow_constructor_exists():
    assert callable(myffbd_Flow.__init__)


def test_myffbd_flow_constructor_args():
    sig = inspect.signature(myffbd_Flow.__init__)
    params = list(sig.parameters.keys())



def test_myffbd_port_is_not_abstract():
    assert not inspect.isabstract(myffbd_Port)


def test_myffbd_port_constructor_exists():
    assert callable(myffbd_Port.__init__)


def test_myffbd_port_constructor_args():
    sig = inspect.signature(myffbd_Port.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_myffbd_port_has_id():
    assert hasattr(myffbd_Port, "id")
    descriptor = None
    for klass in myffbd_Port.__mro__:
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



def test_myffbd_inputport_is_not_abstract():
    assert not inspect.isabstract(myffbd_InputPort)


def test_myffbd_inputport_constructor_exists():
    assert callable(myffbd_InputPort.__init__)


def test_myffbd_inputport_constructor_args():
    sig = inspect.signature(myffbd_InputPort.__init__)
    params = list(sig.parameters.keys())



def test_myffbd_outputport_is_not_abstract():
    assert not inspect.isabstract(myffbd_OutputPort)


def test_myffbd_outputport_constructor_exists():
    assert callable(myffbd_OutputPort.__init__)


def test_myffbd_outputport_constructor_args():
    sig = inspect.signature(myffbd_OutputPort.__init__)
    params = list(sig.parameters.keys())



def test_myffbd_sequencenode_is_not_abstract():
    assert not inspect.isabstract(myffbd_SequenceNode)


def test_myffbd_sequencenode_constructor_exists():
    assert callable(myffbd_SequenceNode.__init__)


def test_myffbd_sequencenode_constructor_args():
    sig = inspect.signature(myffbd_SequenceNode.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_myffbd_sequencenode_has_name():
    assert hasattr(myffbd_SequenceNode, "name")
    descriptor = None
    for klass in myffbd_SequenceNode.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_myffbd_porttype_is_not_abstract():
    assert not inspect.isabstract(myffbd_PortType)


def test_myffbd_porttype_constructor_exists():
    assert callable(myffbd_PortType.__init__)


def test_myffbd_porttype_constructor_args():
    sig = inspect.signature(myffbd_PortType.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_myffbd_porttype_has_type():
    assert hasattr(myffbd_PortType, "type")
    descriptor = None
    for klass in myffbd_PortType.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_myffbd_token_is_not_abstract():
    assert not inspect.isabstract(myffbd_Token)


def test_myffbd_token_constructor_exists():
    assert callable(myffbd_Token.__init__)


def test_myffbd_token_constructor_args():
    sig = inspect.signature(myffbd_Token.__init__)
    params = list(sig.parameters.keys())



def test_myffbd_description_is_not_abstract():
    assert not inspect.isabstract(myffbd_Description)


def test_myffbd_description_constructor_exists():
    assert callable(myffbd_Description.__init__)


def test_myffbd_description_constructor_args():
    sig = inspect.signature(myffbd_Description.__init__)
    params = list(sig.parameters.keys())
    assert "content" in params, "Missing parameter 'content'"

def test_myffbd_description_has_content():
    assert hasattr(myffbd_Description, "content")
    descriptor = None
    for klass in myffbd_Description.__mro__:
        if "content" in klass.__dict__:
            descriptor = klass.__dict__["content"]
            break
    assert isinstance(descriptor, property)



def test_sequencenode_is_not_abstract():
    assert not inspect.isabstract(SequenceNode)


def test_sequencenode_constructor_exists():
    assert callable(SequenceNode.__init__)


def test_sequencenode_constructor_args():
    sig = inspect.signature(SequenceNode.__init__)
    params = list(sig.parameters.keys())



def test_myffbd_and_is_not_abstract():
    assert not inspect.isabstract(myffbd_And)


def test_myffbd_and_constructor_exists():
    assert callable(myffbd_And.__init__)


def test_myffbd_and_constructor_args():
    sig = inspect.signature(myffbd_And.__init__)
    params = list(sig.parameters.keys())



def test_myffbd_start_is_not_abstract():
    assert not inspect.isabstract(myffbd_Start)


def test_myffbd_start_constructor_exists():
    assert callable(myffbd_Start.__init__)


def test_myffbd_start_constructor_args():
    sig = inspect.signature(myffbd_Start.__init__)
    params = list(sig.parameters.keys())



def test_myffbd_loopexit_is_not_abstract():
    assert not inspect.isabstract(myffbd_LoopExit)


def test_myffbd_loopexit_constructor_exists():
    assert callable(myffbd_LoopExit.__init__)


def test_myffbd_loopexit_constructor_args():
    sig = inspect.signature(myffbd_LoopExit.__init__)
    params = list(sig.parameters.keys())



def test_myffbd_iteration_is_not_abstract():
    assert not inspect.isabstract(myffbd_Iteration)


def test_myffbd_iteration_constructor_exists():
    assert callable(myffbd_Iteration.__init__)


def test_myffbd_iteration_constructor_args():
    sig = inspect.signature(myffbd_Iteration.__init__)
    params = list(sig.parameters.keys())



def test_myffbd_final_is_not_abstract():
    assert not inspect.isabstract(myffbd_Final)


def test_myffbd_final_constructor_exists():
    assert callable(myffbd_Final.__init__)


def test_myffbd_final_constructor_args():
    sig = inspect.signature(myffbd_Final.__init__)
    params = list(sig.parameters.keys())



def test_myffbd_loop_is_not_abstract():
    assert not inspect.isabstract(myffbd_Loop)


def test_myffbd_loop_constructor_exists():
    assert callable(myffbd_Loop.__init__)


def test_myffbd_loop_constructor_args():
    sig = inspect.signature(myffbd_Loop.__init__)
    params = list(sig.parameters.keys())



def test_myffbd_or_is_not_abstract():
    assert not inspect.isabstract(myffbd_Or)


def test_myffbd_or_constructor_exists():
    assert callable(myffbd_Or.__init__)


def test_myffbd_or_constructor_args():
    sig = inspect.signature(myffbd_Or.__init__)
    params = list(sig.parameters.keys())



def test_myffbd_function_is_not_abstract():
    assert not inspect.isabstract(myffbd_Function)


def test_myffbd_function_constructor_exists():
    assert callable(myffbd_Function.__init__)


def test_myffbd_function_constructor_args():
    sig = inspect.signature(myffbd_Function.__init__)
    params = list(sig.parameters.keys())
    assert "tMin" in params, "Missing parameter 'tMin'"
    assert "tMax" in params, "Missing parameter 'tMax'"
    assert "domain" in params, "Missing parameter 'domain'"

def test_myffbd_function_has_tMin():
    assert hasattr(myffbd_Function, "tMin")
    descriptor = None
    for klass in myffbd_Function.__mro__:
        if "tMin" in klass.__dict__:
            descriptor = klass.__dict__["tMin"]
            break
    assert isinstance(descriptor, property)

def test_myffbd_function_has_tMax():
    assert hasattr(myffbd_Function, "tMax")
    descriptor = None
    for klass in myffbd_Function.__mro__:
        if "tMax" in klass.__dict__:
            descriptor = klass.__dict__["tMax"]
            break
    assert isinstance(descriptor, property)

def test_myffbd_function_has_domain():
    assert hasattr(myffbd_Function, "domain")
    descriptor = None
    for klass in myffbd_Function.__mro__:
        if "domain" in klass.__dict__:
            descriptor = klass.__dict__["domain"]
            break
    assert isinstance(descriptor, property)

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
myffbd_Item_strategy = st.builds(
    myffbd_Item,
    name=
        safe_text
)
myffbd_Flow_strategy = st.builds(
    myffbd_Flow,
)
myffbd_Port_strategy = st.builds(
    myffbd_Port,
    id=
        safe_text
)
Port_strategy = st.builds(
    Port,
)
myffbd_InputPort_strategy = st.builds(
    myffbd_InputPort,
)
myffbd_OutputPort_strategy = st.builds(
    myffbd_OutputPort,
)
myffbd_SequenceNode_strategy = st.builds(
    myffbd_SequenceNode,
    name=
        safe_text
)
myffbd_PortType_strategy = st.builds(
    myffbd_PortType,
    type=
        safe_text
)
myffbd_Token_strategy = st.builds(
    myffbd_Token,
)
myffbd_Description_strategy = st.builds(
    myffbd_Description,
    content=
        safe_text
)
SequenceNode_strategy = st.builds(
    SequenceNode,
)
myffbd_And_strategy = st.builds(
    myffbd_And,
)
myffbd_Start_strategy = st.builds(
    myffbd_Start,
)
myffbd_LoopExit_strategy = st.builds(
    myffbd_LoopExit,
)
myffbd_Iteration_strategy = st.builds(
    myffbd_Iteration,
)
myffbd_Final_strategy = st.builds(
    myffbd_Final,
)
myffbd_Loop_strategy = st.builds(
    myffbd_Loop,
)
myffbd_Or_strategy = st.builds(
    myffbd_Or,
)
myffbd_Function_strategy = st.builds(
    myffbd_Function,
    tMin=
        st.integers(),
    tMax=
        st.integers(),
    domain=
        safe_text
)

@given(instance=myffbd_Item_strategy)
@settings(max_examples=50)
def test_myffbd_item_instantiation(instance):
    assert isinstance(instance, myffbd_Item)



@given(instance=myffbd_Item_strategy)
def test_myffbd_item_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myffbd_Flow_strategy)
@settings(max_examples=50)
def test_myffbd_flow_instantiation(instance):
    assert isinstance(instance, myffbd_Flow)

@given(instance=myffbd_Port_strategy)
@settings(max_examples=50)
def test_myffbd_port_instantiation(instance):
    assert isinstance(instance, myffbd_Port)



@given(instance=myffbd_Port_strategy)
def test_myffbd_port_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Port_strategy)
@settings(max_examples=50)
def test_port_instantiation(instance):
    assert isinstance(instance, Port)

@given(instance=myffbd_InputPort_strategy)
@settings(max_examples=50)
def test_myffbd_inputport_instantiation(instance):
    assert isinstance(instance, myffbd_InputPort)

@given(instance=myffbd_OutputPort_strategy)
@settings(max_examples=50)
def test_myffbd_outputport_instantiation(instance):
    assert isinstance(instance, myffbd_OutputPort)

@given(instance=myffbd_SequenceNode_strategy)
@settings(max_examples=50)
def test_myffbd_sequencenode_instantiation(instance):
    assert isinstance(instance, myffbd_SequenceNode)



@given(instance=myffbd_SequenceNode_strategy)
def test_myffbd_sequencenode_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myffbd_PortType_strategy)
@settings(max_examples=50)
def test_myffbd_porttype_instantiation(instance):
    assert isinstance(instance, myffbd_PortType)



@given(instance=myffbd_PortType_strategy)
def test_myffbd_porttype_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=myffbd_Token_strategy)
@settings(max_examples=50)
def test_myffbd_token_instantiation(instance):
    assert isinstance(instance, myffbd_Token)

@given(instance=myffbd_Description_strategy)
@settings(max_examples=50)
def test_myffbd_description_instantiation(instance):
    assert isinstance(instance, myffbd_Description)



@given(instance=myffbd_Description_strategy)
def test_myffbd_description_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original

@given(instance=SequenceNode_strategy)
@settings(max_examples=50)
def test_sequencenode_instantiation(instance):
    assert isinstance(instance, SequenceNode)

@given(instance=myffbd_And_strategy)
@settings(max_examples=50)
def test_myffbd_and_instantiation(instance):
    assert isinstance(instance, myffbd_And)

@given(instance=myffbd_Start_strategy)
@settings(max_examples=50)
def test_myffbd_start_instantiation(instance):
    assert isinstance(instance, myffbd_Start)

@given(instance=myffbd_LoopExit_strategy)
@settings(max_examples=50)
def test_myffbd_loopexit_instantiation(instance):
    assert isinstance(instance, myffbd_LoopExit)

@given(instance=myffbd_Iteration_strategy)
@settings(max_examples=50)
def test_myffbd_iteration_instantiation(instance):
    assert isinstance(instance, myffbd_Iteration)

@given(instance=myffbd_Final_strategy)
@settings(max_examples=50)
def test_myffbd_final_instantiation(instance):
    assert isinstance(instance, myffbd_Final)

@given(instance=myffbd_Loop_strategy)
@settings(max_examples=50)
def test_myffbd_loop_instantiation(instance):
    assert isinstance(instance, myffbd_Loop)

@given(instance=myffbd_Or_strategy)
@settings(max_examples=50)
def test_myffbd_or_instantiation(instance):
    assert isinstance(instance, myffbd_Or)

@given(instance=myffbd_Function_strategy)
@settings(max_examples=50)
def test_myffbd_function_instantiation(instance):
    assert isinstance(instance, myffbd_Function)



@given(instance=myffbd_Function_strategy)
def test_myffbd_function_tMin_setter(instance):
    original = instance.tMin
    instance.tMin = original
    assert instance.tMin == original



@given(instance=myffbd_Function_strategy)
def test_myffbd_function_tMax_setter(instance):
    original = instance.tMax
    instance.tMax = original
    assert instance.tMax == original



@given(instance=myffbd_Function_strategy)
def test_myffbd_function_domain_setter(instance):
    original = instance.domain
    instance.domain = original
    assert instance.domain == original
