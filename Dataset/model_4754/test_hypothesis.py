import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    myffbd::Item,
    myffbd::Flow,
    myffbd::Port,
    Port,
    myffbd::InputPort,
    myffbd::OutputPort,
    myffbd::SequenceNode,
    myffbd::PortType,
    myffbd::Token,
    myffbd::Description,
    SequenceNode,
    myffbd::Iteration,
    myffbd::Loop,
    myffbd::LoopExit,
    myffbd::Start,
    myffbd::And,
    myffbd::Or,
    myffbd::Final,
    myffbd::Function,
    FunctionDomain,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_myffbd::item_is_not_abstract():
    assert not inspect.isabstract(myffbd::Item)


def test_myffbd::item_constructor_exists():
    assert callable(myffbd::Item.__init__)


def test_myffbd::item_constructor_args():
    sig = inspect.signature(myffbd::Item.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_myffbd::item_has_name():
    assert hasattr(myffbd::Item, "name")
    descriptor = None
    for klass in myffbd::Item.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_myffbd::flow_is_not_abstract():
    assert not inspect.isabstract(myffbd::Flow)


def test_myffbd::flow_constructor_exists():
    assert callable(myffbd::Flow.__init__)


def test_myffbd::flow_constructor_args():
    sig = inspect.signature(myffbd::Flow.__init__)
    params = list(sig.parameters.keys())



def test_myffbd::port_is_not_abstract():
    assert not inspect.isabstract(myffbd::Port)


def test_myffbd::port_constructor_exists():
    assert callable(myffbd::Port.__init__)


def test_myffbd::port_constructor_args():
    sig = inspect.signature(myffbd::Port.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_myffbd::port_has_id():
    assert hasattr(myffbd::Port, "id")
    descriptor = None
    for klass in myffbd::Port.__mro__:
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



def test_myffbd::inputport_is_not_abstract():
    assert not inspect.isabstract(myffbd::InputPort)


def test_myffbd::inputport_constructor_exists():
    assert callable(myffbd::InputPort.__init__)


def test_myffbd::inputport_constructor_args():
    sig = inspect.signature(myffbd::InputPort.__init__)
    params = list(sig.parameters.keys())



def test_myffbd::outputport_is_not_abstract():
    assert not inspect.isabstract(myffbd::OutputPort)


def test_myffbd::outputport_constructor_exists():
    assert callable(myffbd::OutputPort.__init__)


def test_myffbd::outputport_constructor_args():
    sig = inspect.signature(myffbd::OutputPort.__init__)
    params = list(sig.parameters.keys())



def test_myffbd::sequencenode_is_not_abstract():
    assert not inspect.isabstract(myffbd::SequenceNode)


def test_myffbd::sequencenode_constructor_exists():
    assert callable(myffbd::SequenceNode.__init__)


def test_myffbd::sequencenode_constructor_args():
    sig = inspect.signature(myffbd::SequenceNode.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_myffbd::sequencenode_has_name():
    assert hasattr(myffbd::SequenceNode, "name")
    descriptor = None
    for klass in myffbd::SequenceNode.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_myffbd::porttype_is_not_abstract():
    assert not inspect.isabstract(myffbd::PortType)


def test_myffbd::porttype_constructor_exists():
    assert callable(myffbd::PortType.__init__)


def test_myffbd::porttype_constructor_args():
    sig = inspect.signature(myffbd::PortType.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_myffbd::porttype_has_type():
    assert hasattr(myffbd::PortType, "type")
    descriptor = None
    for klass in myffbd::PortType.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_myffbd::token_is_not_abstract():
    assert not inspect.isabstract(myffbd::Token)


def test_myffbd::token_constructor_exists():
    assert callable(myffbd::Token.__init__)


def test_myffbd::token_constructor_args():
    sig = inspect.signature(myffbd::Token.__init__)
    params = list(sig.parameters.keys())



def test_myffbd::description_is_not_abstract():
    assert not inspect.isabstract(myffbd::Description)


def test_myffbd::description_constructor_exists():
    assert callable(myffbd::Description.__init__)


def test_myffbd::description_constructor_args():
    sig = inspect.signature(myffbd::Description.__init__)
    params = list(sig.parameters.keys())
    assert "content" in params, "Missing parameter 'content'"

def test_myffbd::description_has_content():
    assert hasattr(myffbd::Description, "content")
    descriptor = None
    for klass in myffbd::Description.__mro__:
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



def test_myffbd::iteration_is_not_abstract():
    assert not inspect.isabstract(myffbd::Iteration)


def test_myffbd::iteration_constructor_exists():
    assert callable(myffbd::Iteration.__init__)


def test_myffbd::iteration_constructor_args():
    sig = inspect.signature(myffbd::Iteration.__init__)
    params = list(sig.parameters.keys())



def test_myffbd::loop_is_not_abstract():
    assert not inspect.isabstract(myffbd::Loop)


def test_myffbd::loop_constructor_exists():
    assert callable(myffbd::Loop.__init__)


def test_myffbd::loop_constructor_args():
    sig = inspect.signature(myffbd::Loop.__init__)
    params = list(sig.parameters.keys())



def test_myffbd::loopexit_is_not_abstract():
    assert not inspect.isabstract(myffbd::LoopExit)


def test_myffbd::loopexit_constructor_exists():
    assert callable(myffbd::LoopExit.__init__)


def test_myffbd::loopexit_constructor_args():
    sig = inspect.signature(myffbd::LoopExit.__init__)
    params = list(sig.parameters.keys())



def test_myffbd::start_is_not_abstract():
    assert not inspect.isabstract(myffbd::Start)


def test_myffbd::start_constructor_exists():
    assert callable(myffbd::Start.__init__)


def test_myffbd::start_constructor_args():
    sig = inspect.signature(myffbd::Start.__init__)
    params = list(sig.parameters.keys())



def test_myffbd::and_is_not_abstract():
    assert not inspect.isabstract(myffbd::And)


def test_myffbd::and_constructor_exists():
    assert callable(myffbd::And.__init__)


def test_myffbd::and_constructor_args():
    sig = inspect.signature(myffbd::And.__init__)
    params = list(sig.parameters.keys())



def test_myffbd::or_is_not_abstract():
    assert not inspect.isabstract(myffbd::Or)


def test_myffbd::or_constructor_exists():
    assert callable(myffbd::Or.__init__)


def test_myffbd::or_constructor_args():
    sig = inspect.signature(myffbd::Or.__init__)
    params = list(sig.parameters.keys())



def test_myffbd::final_is_not_abstract():
    assert not inspect.isabstract(myffbd::Final)


def test_myffbd::final_constructor_exists():
    assert callable(myffbd::Final.__init__)


def test_myffbd::final_constructor_args():
    sig = inspect.signature(myffbd::Final.__init__)
    params = list(sig.parameters.keys())



def test_myffbd::function_is_not_abstract():
    assert not inspect.isabstract(myffbd::Function)


def test_myffbd::function_constructor_exists():
    assert callable(myffbd::Function.__init__)


def test_myffbd::function_constructor_args():
    sig = inspect.signature(myffbd::Function.__init__)
    params = list(sig.parameters.keys())
    assert "tMax" in params, "Missing parameter 'tMax'"
    assert "tMin" in params, "Missing parameter 'tMin'"
    assert "domain" in params, "Missing parameter 'domain'"

def test_myffbd::function_has_tMax():
    assert hasattr(myffbd::Function, "tMax")
    descriptor = None
    for klass in myffbd::Function.__mro__:
        if "tMax" in klass.__dict__:
            descriptor = klass.__dict__["tMax"]
            break
    assert isinstance(descriptor, property)

def test_myffbd::function_has_tMin():
    assert hasattr(myffbd::Function, "tMin")
    descriptor = None
    for klass in myffbd::Function.__mro__:
        if "tMin" in klass.__dict__:
            descriptor = klass.__dict__["tMin"]
            break
    assert isinstance(descriptor, property)

def test_myffbd::function_has_domain():
    assert hasattr(myffbd::Function, "domain")
    descriptor = None
    for klass in myffbd::Function.__mro__:
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
        "form",
        "time",
        "space",
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
myffbd::Item_strategy = st.builds(
    myffbd::Item,
    name=
        safe_text
)
myffbd::Flow_strategy = st.builds(
    myffbd::Flow,
)
myffbd::Port_strategy = st.builds(
    myffbd::Port,
    id=
        safe_text
)
Port_strategy = st.builds(
    Port,
)
myffbd::InputPort_strategy = st.builds(
    myffbd::InputPort,
)
myffbd::OutputPort_strategy = st.builds(
    myffbd::OutputPort,
)
myffbd::SequenceNode_strategy = st.builds(
    myffbd::SequenceNode,
    name=
        safe_text
)
myffbd::PortType_strategy = st.builds(
    myffbd::PortType,
    type=
        safe_text
)
myffbd::Token_strategy = st.builds(
    myffbd::Token,
)
myffbd::Description_strategy = st.builds(
    myffbd::Description,
    content=
        safe_text
)
SequenceNode_strategy = st.builds(
    SequenceNode,
)
myffbd::Iteration_strategy = st.builds(
    myffbd::Iteration,
)
myffbd::Loop_strategy = st.builds(
    myffbd::Loop,
)
myffbd::LoopExit_strategy = st.builds(
    myffbd::LoopExit,
)
myffbd::Start_strategy = st.builds(
    myffbd::Start,
)
myffbd::And_strategy = st.builds(
    myffbd::And,
)
myffbd::Or_strategy = st.builds(
    myffbd::Or,
)
myffbd::Final_strategy = st.builds(
    myffbd::Final,
)
myffbd::Function_strategy = st.builds(
    myffbd::Function,
    tMax=
        st.integers(),
    tMin=
        st.integers(),
    domain=
        safe_text
)

@given(instance=myffbd::Item_strategy)
@settings(max_examples=50)
def test_myffbd::item_instantiation(instance):
    assert isinstance(instance, myffbd::Item)

@given(instance=myffbd::Item_strategy)
def test_myffbd::item_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myffbd::Item_strategy)
def test_myffbd::item_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myffbd::Flow_strategy)
@settings(max_examples=50)
def test_myffbd::flow_instantiation(instance):
    assert isinstance(instance, myffbd::Flow)

@given(instance=myffbd::Port_strategy)
@settings(max_examples=50)
def test_myffbd::port_instantiation(instance):
    assert isinstance(instance, myffbd::Port)

@given(instance=myffbd::Port_strategy)
def test_myffbd::port_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=myffbd::Port_strategy)
def test_myffbd::port_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Port_strategy)
@settings(max_examples=50)
def test_port_instantiation(instance):
    assert isinstance(instance, Port)

@given(instance=myffbd::InputPort_strategy)
@settings(max_examples=50)
def test_myffbd::inputport_instantiation(instance):
    assert isinstance(instance, myffbd::InputPort)

@given(instance=myffbd::OutputPort_strategy)
@settings(max_examples=50)
def test_myffbd::outputport_instantiation(instance):
    assert isinstance(instance, myffbd::OutputPort)

@given(instance=myffbd::SequenceNode_strategy)
@settings(max_examples=50)
def test_myffbd::sequencenode_instantiation(instance):
    assert isinstance(instance, myffbd::SequenceNode)

@given(instance=myffbd::SequenceNode_strategy)
def test_myffbd::sequencenode_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myffbd::SequenceNode_strategy)
def test_myffbd::sequencenode_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myffbd::PortType_strategy)
@settings(max_examples=50)
def test_myffbd::porttype_instantiation(instance):
    assert isinstance(instance, myffbd::PortType)

@given(instance=myffbd::PortType_strategy)
def test_myffbd::porttype_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=myffbd::PortType_strategy)
def test_myffbd::porttype_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=myffbd::Token_strategy)
@settings(max_examples=50)
def test_myffbd::token_instantiation(instance):
    assert isinstance(instance, myffbd::Token)

@given(instance=myffbd::Description_strategy)
@settings(max_examples=50)
def test_myffbd::description_instantiation(instance):
    assert isinstance(instance, myffbd::Description)

@given(instance=myffbd::Description_strategy)
def test_myffbd::description_content_type(instance):
    assert isinstance(instance.content, str)


@given(instance=myffbd::Description_strategy)
def test_myffbd::description_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original

@given(instance=SequenceNode_strategy)
@settings(max_examples=50)
def test_sequencenode_instantiation(instance):
    assert isinstance(instance, SequenceNode)

@given(instance=myffbd::Iteration_strategy)
@settings(max_examples=50)
def test_myffbd::iteration_instantiation(instance):
    assert isinstance(instance, myffbd::Iteration)

@given(instance=myffbd::Loop_strategy)
@settings(max_examples=50)
def test_myffbd::loop_instantiation(instance):
    assert isinstance(instance, myffbd::Loop)

@given(instance=myffbd::LoopExit_strategy)
@settings(max_examples=50)
def test_myffbd::loopexit_instantiation(instance):
    assert isinstance(instance, myffbd::LoopExit)

@given(instance=myffbd::Start_strategy)
@settings(max_examples=50)
def test_myffbd::start_instantiation(instance):
    assert isinstance(instance, myffbd::Start)

@given(instance=myffbd::And_strategy)
@settings(max_examples=50)
def test_myffbd::and_instantiation(instance):
    assert isinstance(instance, myffbd::And)

@given(instance=myffbd::Or_strategy)
@settings(max_examples=50)
def test_myffbd::or_instantiation(instance):
    assert isinstance(instance, myffbd::Or)

@given(instance=myffbd::Final_strategy)
@settings(max_examples=50)
def test_myffbd::final_instantiation(instance):
    assert isinstance(instance, myffbd::Final)

@given(instance=myffbd::Function_strategy)
@settings(max_examples=50)
def test_myffbd::function_instantiation(instance):
    assert isinstance(instance, myffbd::Function)

@given(instance=myffbd::Function_strategy)
def test_myffbd::function_tMax_type(instance):
    assert isinstance(instance.tMax, int)


@given(instance=myffbd::Function_strategy)
def test_myffbd::function_tMax_setter(instance):
    original = instance.tMax
    instance.tMax = original
    assert instance.tMax == original

@given(instance=myffbd::Function_strategy)
def test_myffbd::function_tMin_type(instance):
    assert isinstance(instance.tMin, int)


@given(instance=myffbd::Function_strategy)
def test_myffbd::function_tMin_setter(instance):
    original = instance.tMin
    instance.tMin = original
    assert instance.tMin == original

@given(instance=myffbd::Function_strategy)
def test_myffbd::function_domain_type(instance):
    assert isinstance(instance.domain, str)


@given(instance=myffbd::Function_strategy)
def test_myffbd::function_domain_setter(instance):
    original = instance.domain
    instance.domain = original
    assert instance.domain == original
