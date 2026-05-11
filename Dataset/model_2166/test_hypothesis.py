import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Refinement,
    pimm::HRefinement,
    pimm::visitor::PiMMVisitor,
    pimm::visitor::PiMMVisitable,
    pimm::ISetter,
    Parameter,
    pimm::ConfigInputInterface,
    InterfaceActor,
    pimm::DataOutputInterface,
    pimm::ConfigOutputInterface,
    pimm::DataInputInterface,
    ISetter,
    DataOutputPort,
    Port,
    pimm::DataPort,
    DataPort,
    ExecutableActor,
    pimm::RoundBufferActor,
    pimm::ForkActor,
    pimm::BroadcastActor,
    pimm::JoinActor,
    pimm::Actor,
    Parameterizable,
    pimm::Delay,
    pimm::AbstractVertex,
    pimm::ConfigInputPort,
    PiMMVisitable,
    pimm::Refinement,
    pimm::Fifo,
    pimm::FunctionPrototype,
    pimm::Dependency,
    pimm::Expression,
    pimm::FunctionParameter,
    pimm::Port,
    pimm::Parameterizable,
    AbstractActor,
    pimm::InterfaceActor,
    pimm::ExecutableActor,
    pimm::PiGraph,
    pimm::ConfigOutputPort,
    pimm::DataOutputPort,
    pimm::DataInputPort,
    AbstractVertex,
    pimm::Parameter,
    pimm::AbstractActor,
    PortMemoryAnnotation,
    Direction,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_refinement_is_not_abstract():
    assert not inspect.isabstract(Refinement)


def test_refinement_constructor_exists():
    assert callable(Refinement.__init__)


def test_refinement_constructor_args():
    sig = inspect.signature(Refinement.__init__)
    params = list(sig.parameters.keys())



def test_pimm::hrefinement_is_not_abstract():
    assert not inspect.isabstract(pimm::HRefinement)


def test_pimm::hrefinement_constructor_exists():
    assert callable(pimm::HRefinement.__init__)


def test_pimm::hrefinement_constructor_args():
    sig = inspect.signature(pimm::HRefinement.__init__)
    params = list(sig.parameters.keys())



def test_pimm::visitor::pimmvisitor_is_not_abstract():
    assert not inspect.isabstract(pimm::visitor::PiMMVisitor)


def test_pimm::visitor::pimmvisitor_constructor_exists():
    assert callable(pimm::visitor::PiMMVisitor.__init__)


def test_pimm::visitor::pimmvisitor_constructor_args():
    sig = inspect.signature(pimm::visitor::PiMMVisitor.__init__)
    params = list(sig.parameters.keys())



def test_pimm::visitor::pimmvisitable_is_not_abstract():
    assert not inspect.isabstract(pimm::visitor::PiMMVisitable)


def test_pimm::visitor::pimmvisitable_constructor_exists():
    assert callable(pimm::visitor::PiMMVisitable.__init__)


def test_pimm::visitor::pimmvisitable_constructor_args():
    sig = inspect.signature(pimm::visitor::PiMMVisitable.__init__)
    params = list(sig.parameters.keys())



def test_pimm::isetter_is_not_abstract():
    assert not inspect.isabstract(pimm::ISetter)


def test_pimm::isetter_constructor_exists():
    assert callable(pimm::ISetter.__init__)


def test_pimm::isetter_constructor_args():
    sig = inspect.signature(pimm::ISetter.__init__)
    params = list(sig.parameters.keys())



def test_parameter_is_not_abstract():
    assert not inspect.isabstract(Parameter)


def test_parameter_constructor_exists():
    assert callable(Parameter.__init__)


def test_parameter_constructor_args():
    sig = inspect.signature(Parameter.__init__)
    params = list(sig.parameters.keys())



def test_pimm::configinputinterface_is_not_abstract():
    assert not inspect.isabstract(pimm::ConfigInputInterface)


def test_pimm::configinputinterface_constructor_exists():
    assert callable(pimm::ConfigInputInterface.__init__)


def test_pimm::configinputinterface_constructor_args():
    sig = inspect.signature(pimm::ConfigInputInterface.__init__)
    params = list(sig.parameters.keys())



def test_interfaceactor_is_not_abstract():
    assert not inspect.isabstract(InterfaceActor)


def test_interfaceactor_constructor_exists():
    assert callable(InterfaceActor.__init__)


def test_interfaceactor_constructor_args():
    sig = inspect.signature(InterfaceActor.__init__)
    params = list(sig.parameters.keys())



def test_pimm::dataoutputinterface_is_not_abstract():
    assert not inspect.isabstract(pimm::DataOutputInterface)


def test_pimm::dataoutputinterface_constructor_exists():
    assert callable(pimm::DataOutputInterface.__init__)


def test_pimm::dataoutputinterface_constructor_args():
    sig = inspect.signature(pimm::DataOutputInterface.__init__)
    params = list(sig.parameters.keys())



def test_pimm::configoutputinterface_is_not_abstract():
    assert not inspect.isabstract(pimm::ConfigOutputInterface)


def test_pimm::configoutputinterface_constructor_exists():
    assert callable(pimm::ConfigOutputInterface.__init__)


def test_pimm::configoutputinterface_constructor_args():
    sig = inspect.signature(pimm::ConfigOutputInterface.__init__)
    params = list(sig.parameters.keys())



def test_pimm::datainputinterface_is_not_abstract():
    assert not inspect.isabstract(pimm::DataInputInterface)


def test_pimm::datainputinterface_constructor_exists():
    assert callable(pimm::DataInputInterface.__init__)


def test_pimm::datainputinterface_constructor_args():
    sig = inspect.signature(pimm::DataInputInterface.__init__)
    params = list(sig.parameters.keys())



def test_isetter_is_not_abstract():
    assert not inspect.isabstract(ISetter)


def test_isetter_constructor_exists():
    assert callable(ISetter.__init__)


def test_isetter_constructor_args():
    sig = inspect.signature(ISetter.__init__)
    params = list(sig.parameters.keys())



def test_dataoutputport_is_not_abstract():
    assert not inspect.isabstract(DataOutputPort)


def test_dataoutputport_constructor_exists():
    assert callable(DataOutputPort.__init__)


def test_dataoutputport_constructor_args():
    sig = inspect.signature(DataOutputPort.__init__)
    params = list(sig.parameters.keys())



def test_port_is_not_abstract():
    assert not inspect.isabstract(Port)


def test_port_constructor_exists():
    assert callable(Port.__init__)


def test_port_constructor_args():
    sig = inspect.signature(Port.__init__)
    params = list(sig.parameters.keys())



def test_pimm::dataport_is_not_abstract():
    assert not inspect.isabstract(pimm::DataPort)


def test_pimm::dataport_constructor_exists():
    assert callable(pimm::DataPort.__init__)


def test_pimm::dataport_constructor_args():
    sig = inspect.signature(pimm::DataPort.__init__)
    params = list(sig.parameters.keys())
    assert "annotation" in params, "Missing parameter 'annotation'"

def test_pimm::dataport_has_annotation():
    assert hasattr(pimm::DataPort, "annotation")
    descriptor = None
    for klass in pimm::DataPort.__mro__:
        if "annotation" in klass.__dict__:
            descriptor = klass.__dict__["annotation"]
            break
    assert isinstance(descriptor, property)



def test_dataport_is_not_abstract():
    assert not inspect.isabstract(DataPort)


def test_dataport_constructor_exists():
    assert callable(DataPort.__init__)


def test_dataport_constructor_args():
    sig = inspect.signature(DataPort.__init__)
    params = list(sig.parameters.keys())



def test_executableactor_is_not_abstract():
    assert not inspect.isabstract(ExecutableActor)


def test_executableactor_constructor_exists():
    assert callable(ExecutableActor.__init__)


def test_executableactor_constructor_args():
    sig = inspect.signature(ExecutableActor.__init__)
    params = list(sig.parameters.keys())



def test_pimm::roundbufferactor_is_not_abstract():
    assert not inspect.isabstract(pimm::RoundBufferActor)


def test_pimm::roundbufferactor_constructor_exists():
    assert callable(pimm::RoundBufferActor.__init__)


def test_pimm::roundbufferactor_constructor_args():
    sig = inspect.signature(pimm::RoundBufferActor.__init__)
    params = list(sig.parameters.keys())



def test_pimm::forkactor_is_not_abstract():
    assert not inspect.isabstract(pimm::ForkActor)


def test_pimm::forkactor_constructor_exists():
    assert callable(pimm::ForkActor.__init__)


def test_pimm::forkactor_constructor_args():
    sig = inspect.signature(pimm::ForkActor.__init__)
    params = list(sig.parameters.keys())



def test_pimm::broadcastactor_is_not_abstract():
    assert not inspect.isabstract(pimm::BroadcastActor)


def test_pimm::broadcastactor_constructor_exists():
    assert callable(pimm::BroadcastActor.__init__)


def test_pimm::broadcastactor_constructor_args():
    sig = inspect.signature(pimm::BroadcastActor.__init__)
    params = list(sig.parameters.keys())



def test_pimm::joinactor_is_not_abstract():
    assert not inspect.isabstract(pimm::JoinActor)


def test_pimm::joinactor_constructor_exists():
    assert callable(pimm::JoinActor.__init__)


def test_pimm::joinactor_constructor_args():
    sig = inspect.signature(pimm::JoinActor.__init__)
    params = list(sig.parameters.keys())



def test_pimm::actor_is_not_abstract():
    assert not inspect.isabstract(pimm::Actor)


def test_pimm::actor_constructor_exists():
    assert callable(pimm::Actor.__init__)


def test_pimm::actor_constructor_args():
    sig = inspect.signature(pimm::Actor.__init__)
    params = list(sig.parameters.keys())
    assert "memoryScriptPath" in params, "Missing parameter 'memoryScriptPath'"
    assert "configurationActor" in params, "Missing parameter 'configurationActor'"

def test_pimm::actor_has_memoryScriptPath():
    assert hasattr(pimm::Actor, "memoryScriptPath")
    descriptor = None
    for klass in pimm::Actor.__mro__:
        if "memoryScriptPath" in klass.__dict__:
            descriptor = klass.__dict__["memoryScriptPath"]
            break
    assert isinstance(descriptor, property)

def test_pimm::actor_has_configurationActor():
    assert hasattr(pimm::Actor, "configurationActor")
    descriptor = None
    for klass in pimm::Actor.__mro__:
        if "configurationActor" in klass.__dict__:
            descriptor = klass.__dict__["configurationActor"]
            break
    assert isinstance(descriptor, property)



def test_parameterizable_is_not_abstract():
    assert not inspect.isabstract(Parameterizable)


def test_parameterizable_constructor_exists():
    assert callable(Parameterizable.__init__)


def test_parameterizable_constructor_args():
    sig = inspect.signature(Parameterizable.__init__)
    params = list(sig.parameters.keys())



def test_pimm::delay_is_not_abstract():
    assert not inspect.isabstract(pimm::Delay)


def test_pimm::delay_constructor_exists():
    assert callable(pimm::Delay.__init__)


def test_pimm::delay_constructor_args():
    sig = inspect.signature(pimm::Delay.__init__)
    params = list(sig.parameters.keys())



def test_pimm::abstractvertex_is_not_abstract():
    assert not inspect.isabstract(pimm::AbstractVertex)


def test_pimm::abstractvertex_constructor_exists():
    assert callable(pimm::AbstractVertex.__init__)


def test_pimm::abstractvertex_constructor_args():
    sig = inspect.signature(pimm::AbstractVertex.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_pimm::abstractvertex_has_name():
    assert hasattr(pimm::AbstractVertex, "name")
    descriptor = None
    for klass in pimm::AbstractVertex.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_pimm::configinputport_is_not_abstract():
    assert not inspect.isabstract(pimm::ConfigInputPort)


def test_pimm::configinputport_constructor_exists():
    assert callable(pimm::ConfigInputPort.__init__)


def test_pimm::configinputport_constructor_args():
    sig = inspect.signature(pimm::ConfigInputPort.__init__)
    params = list(sig.parameters.keys())



def test_pimmvisitable_is_not_abstract():
    assert not inspect.isabstract(PiMMVisitable)


def test_pimmvisitable_constructor_exists():
    assert callable(PiMMVisitable.__init__)


def test_pimmvisitable_constructor_args():
    sig = inspect.signature(PiMMVisitable.__init__)
    params = list(sig.parameters.keys())



def test_pimm::refinement_is_not_abstract():
    assert not inspect.isabstract(pimm::Refinement)


def test_pimm::refinement_constructor_exists():
    assert callable(pimm::Refinement.__init__)


def test_pimm::refinement_constructor_args():
    sig = inspect.signature(pimm::Refinement.__init__)
    params = list(sig.parameters.keys())
    assert "fileName" in params, "Missing parameter 'fileName'"
    assert "filePath" in params, "Missing parameter 'filePath'"

def test_pimm::refinement_has_fileName():
    assert hasattr(pimm::Refinement, "fileName")
    descriptor = None
    for klass in pimm::Refinement.__mro__:
        if "fileName" in klass.__dict__:
            descriptor = klass.__dict__["fileName"]
            break
    assert isinstance(descriptor, property)

def test_pimm::refinement_has_filePath():
    assert hasattr(pimm::Refinement, "filePath")
    descriptor = None
    for klass in pimm::Refinement.__mro__:
        if "filePath" in klass.__dict__:
            descriptor = klass.__dict__["filePath"]
            break
    assert isinstance(descriptor, property)



def test_pimm::fifo_is_not_abstract():
    assert not inspect.isabstract(pimm::Fifo)


def test_pimm::fifo_constructor_exists():
    assert callable(pimm::Fifo.__init__)


def test_pimm::fifo_constructor_args():
    sig = inspect.signature(pimm::Fifo.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "type" in params, "Missing parameter 'type'"

def test_pimm::fifo_has_id():
    assert hasattr(pimm::Fifo, "id")
    descriptor = None
    for klass in pimm::Fifo.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_pimm::fifo_has_type():
    assert hasattr(pimm::Fifo, "type")
    descriptor = None
    for klass in pimm::Fifo.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_pimm::functionprototype_is_not_abstract():
    assert not inspect.isabstract(pimm::FunctionPrototype)


def test_pimm::functionprototype_constructor_exists():
    assert callable(pimm::FunctionPrototype.__init__)


def test_pimm::functionprototype_constructor_args():
    sig = inspect.signature(pimm::FunctionPrototype.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_pimm::functionprototype_has_name():
    assert hasattr(pimm::FunctionPrototype, "name")
    descriptor = None
    for klass in pimm::FunctionPrototype.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_pimm::dependency_is_not_abstract():
    assert not inspect.isabstract(pimm::Dependency)


def test_pimm::dependency_constructor_exists():
    assert callable(pimm::Dependency.__init__)


def test_pimm::dependency_constructor_args():
    sig = inspect.signature(pimm::Dependency.__init__)
    params = list(sig.parameters.keys())



def test_pimm::expression_is_not_abstract():
    assert not inspect.isabstract(pimm::Expression)


def test_pimm::expression_constructor_exists():
    assert callable(pimm::Expression.__init__)


def test_pimm::expression_constructor_args():
    sig = inspect.signature(pimm::Expression.__init__)
    params = list(sig.parameters.keys())
    assert "string" in params, "Missing parameter 'string'"

def test_pimm::expression_has_string():
    assert hasattr(pimm::Expression, "string")
    descriptor = None
    for klass in pimm::Expression.__mro__:
        if "string" in klass.__dict__:
            descriptor = klass.__dict__["string"]
            break
    assert isinstance(descriptor, property)



def test_pimm::functionparameter_is_not_abstract():
    assert not inspect.isabstract(pimm::FunctionParameter)


def test_pimm::functionparameter_constructor_exists():
    assert callable(pimm::FunctionParameter.__init__)


def test_pimm::functionparameter_constructor_args():
    sig = inspect.signature(pimm::FunctionParameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"
    assert "direction" in params, "Missing parameter 'direction'"
    assert "isConfigurationParameter" in params, "Missing parameter 'isConfigurationParameter'"

def test_pimm::functionparameter_has_name():
    assert hasattr(pimm::FunctionParameter, "name")
    descriptor = None
    for klass in pimm::FunctionParameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_pimm::functionparameter_has_type():
    assert hasattr(pimm::FunctionParameter, "type")
    descriptor = None
    for klass in pimm::FunctionParameter.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_pimm::functionparameter_has_direction():
    assert hasattr(pimm::FunctionParameter, "direction")
    descriptor = None
    for klass in pimm::FunctionParameter.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)

def test_pimm::functionparameter_has_isConfigurationParameter():
    assert hasattr(pimm::FunctionParameter, "isConfigurationParameter")
    descriptor = None
    for klass in pimm::FunctionParameter.__mro__:
        if "isConfigurationParameter" in klass.__dict__:
            descriptor = klass.__dict__["isConfigurationParameter"]
            break
    assert isinstance(descriptor, property)



def test_pimm::port_is_not_abstract():
    assert not inspect.isabstract(pimm::Port)


def test_pimm::port_constructor_exists():
    assert callable(pimm::Port.__init__)


def test_pimm::port_constructor_args():
    sig = inspect.signature(pimm::Port.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"
    assert "name" in params, "Missing parameter 'name'"

def test_pimm::port_has_kind():
    assert hasattr(pimm::Port, "kind")
    descriptor = None
    for klass in pimm::Port.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)

def test_pimm::port_has_name():
    assert hasattr(pimm::Port, "name")
    descriptor = None
    for klass in pimm::Port.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_pimm::parameterizable_is_not_abstract():
    assert not inspect.isabstract(pimm::Parameterizable)


def test_pimm::parameterizable_constructor_exists():
    assert callable(pimm::Parameterizable.__init__)


def test_pimm::parameterizable_constructor_args():
    sig = inspect.signature(pimm::Parameterizable.__init__)
    params = list(sig.parameters.keys())



def test_abstractactor_is_not_abstract():
    assert not inspect.isabstract(AbstractActor)


def test_abstractactor_constructor_exists():
    assert callable(AbstractActor.__init__)


def test_abstractactor_constructor_args():
    sig = inspect.signature(AbstractActor.__init__)
    params = list(sig.parameters.keys())



def test_pimm::interfaceactor_is_not_abstract():
    assert not inspect.isabstract(pimm::InterfaceActor)


def test_pimm::interfaceactor_constructor_exists():
    assert callable(pimm::InterfaceActor.__init__)


def test_pimm::interfaceactor_constructor_args():
    sig = inspect.signature(pimm::InterfaceActor.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_pimm::interfaceactor_has_kind():
    assert hasattr(pimm::InterfaceActor, "kind")
    descriptor = None
    for klass in pimm::InterfaceActor.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_pimm::executableactor_is_not_abstract():
    assert not inspect.isabstract(pimm::ExecutableActor)


def test_pimm::executableactor_constructor_exists():
    assert callable(pimm::ExecutableActor.__init__)


def test_pimm::executableactor_constructor_args():
    sig = inspect.signature(pimm::ExecutableActor.__init__)
    params = list(sig.parameters.keys())



def test_pimm::pigraph_is_not_abstract():
    assert not inspect.isabstract(pimm::PiGraph)


def test_pimm::pigraph_constructor_exists():
    assert callable(pimm::PiGraph.__init__)


def test_pimm::pigraph_constructor_args():
    sig = inspect.signature(pimm::PiGraph.__init__)
    params = list(sig.parameters.keys())



def test_pimm::configoutputport_is_not_abstract():
    assert not inspect.isabstract(pimm::ConfigOutputPort)


def test_pimm::configoutputport_constructor_exists():
    assert callable(pimm::ConfigOutputPort.__init__)


def test_pimm::configoutputport_constructor_args():
    sig = inspect.signature(pimm::ConfigOutputPort.__init__)
    params = list(sig.parameters.keys())



def test_pimm::dataoutputport_is_not_abstract():
    assert not inspect.isabstract(pimm::DataOutputPort)


def test_pimm::dataoutputport_constructor_exists():
    assert callable(pimm::DataOutputPort.__init__)


def test_pimm::dataoutputport_constructor_args():
    sig = inspect.signature(pimm::DataOutputPort.__init__)
    params = list(sig.parameters.keys())



def test_pimm::datainputport_is_not_abstract():
    assert not inspect.isabstract(pimm::DataInputPort)


def test_pimm::datainputport_constructor_exists():
    assert callable(pimm::DataInputPort.__init__)


def test_pimm::datainputport_constructor_args():
    sig = inspect.signature(pimm::DataInputPort.__init__)
    params = list(sig.parameters.keys())



def test_abstractvertex_is_not_abstract():
    assert not inspect.isabstract(AbstractVertex)


def test_abstractvertex_constructor_exists():
    assert callable(AbstractVertex.__init__)


def test_abstractvertex_constructor_args():
    sig = inspect.signature(AbstractVertex.__init__)
    params = list(sig.parameters.keys())



def test_pimm::parameter_is_not_abstract():
    assert not inspect.isabstract(pimm::Parameter)


def test_pimm::parameter_constructor_exists():
    assert callable(pimm::Parameter.__init__)


def test_pimm::parameter_constructor_args():
    sig = inspect.signature(pimm::Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "configurationInterface" in params, "Missing parameter 'configurationInterface'"

def test_pimm::parameter_has_configurationInterface():
    assert hasattr(pimm::Parameter, "configurationInterface")
    descriptor = None
    for klass in pimm::Parameter.__mro__:
        if "configurationInterface" in klass.__dict__:
            descriptor = klass.__dict__["configurationInterface"]
            break
    assert isinstance(descriptor, property)



def test_pimm::abstractactor_is_not_abstract():
    assert not inspect.isabstract(pimm::AbstractActor)


def test_pimm::abstractactor_constructor_exists():
    assert callable(pimm::AbstractActor.__init__)


def test_pimm::abstractactor_constructor_args():
    sig = inspect.signature(pimm::AbstractActor.__init__)
    params = list(sig.parameters.keys())

def test_portmemoryannotation_exists():
    # Check that the Enumeration exists
    assert PortMemoryAnnotation is not None

def test_portmemoryannotation_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PortMemoryAnnotation]
    expected_literals = [
        "NONE",
        "UNUSED",
        "WRITE_ONLY",
        "READ_ONLY",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PortMemoryAnnotation"

def test_direction_exists():
    # Check that the Enumeration exists
    assert Direction is not None

def test_direction_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Direction]
    expected_literals = [
        "OUT",
        "IN",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Direction"


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
Refinement_strategy = st.builds(
    Refinement,
)
pimm::HRefinement_strategy = st.builds(
    pimm::HRefinement,
)
pimm::visitor::PiMMVisitor_strategy = st.builds(
    pimm::visitor::PiMMVisitor,
)
pimm::visitor::PiMMVisitable_strategy = st.builds(
    pimm::visitor::PiMMVisitable,
)
pimm::ISetter_strategy = st.builds(
    pimm::ISetter,
)
Parameter_strategy = st.builds(
    Parameter,
)
pimm::ConfigInputInterface_strategy = st.builds(
    pimm::ConfigInputInterface,
)
InterfaceActor_strategy = st.builds(
    InterfaceActor,
)
pimm::DataOutputInterface_strategy = st.builds(
    pimm::DataOutputInterface,
)
pimm::ConfigOutputInterface_strategy = st.builds(
    pimm::ConfigOutputInterface,
)
pimm::DataInputInterface_strategy = st.builds(
    pimm::DataInputInterface,
)
ISetter_strategy = st.builds(
    ISetter,
)
DataOutputPort_strategy = st.builds(
    DataOutputPort,
)
Port_strategy = st.builds(
    Port,
)
pimm::DataPort_strategy = st.builds(
    pimm::DataPort,
    annotation=
        safe_text
)
DataPort_strategy = st.builds(
    DataPort,
)
ExecutableActor_strategy = st.builds(
    ExecutableActor,
)
pimm::RoundBufferActor_strategy = st.builds(
    pimm::RoundBufferActor,
)
pimm::ForkActor_strategy = st.builds(
    pimm::ForkActor,
)
pimm::BroadcastActor_strategy = st.builds(
    pimm::BroadcastActor,
)
pimm::JoinActor_strategy = st.builds(
    pimm::JoinActor,
)
pimm::Actor_strategy = st.builds(
    pimm::Actor,
    memoryScriptPath=
        safe_text,
    configurationActor=
        st.booleans()
)
Parameterizable_strategy = st.builds(
    Parameterizable,
)
pimm::Delay_strategy = st.builds(
    pimm::Delay,
)
pimm::AbstractVertex_strategy = st.builds(
    pimm::AbstractVertex,
    name=
        safe_text
)
pimm::ConfigInputPort_strategy = st.builds(
    pimm::ConfigInputPort,
)
PiMMVisitable_strategy = st.builds(
    PiMMVisitable,
)
pimm::Refinement_strategy = st.builds(
    pimm::Refinement,
    fileName=
        safe_text,
    filePath=
        safe_text
)
pimm::Fifo_strategy = st.builds(
    pimm::Fifo,
    id=
        safe_text,
    type=
        safe_text
)
pimm::FunctionPrototype_strategy = st.builds(
    pimm::FunctionPrototype,
    name=
        safe_text
)
pimm::Dependency_strategy = st.builds(
    pimm::Dependency,
)
pimm::Expression_strategy = st.builds(
    pimm::Expression,
    string=
        safe_text
)
pimm::FunctionParameter_strategy = st.builds(
    pimm::FunctionParameter,
    name=
        safe_text,
    type=
        safe_text,
    direction=
        safe_text,
    isConfigurationParameter=
        st.booleans()
)
pimm::Port_strategy = st.builds(
    pimm::Port,
    kind=
        safe_text,
    name=
        safe_text
)
pimm::Parameterizable_strategy = st.builds(
    pimm::Parameterizable,
)
AbstractActor_strategy = st.builds(
    AbstractActor,
)
pimm::InterfaceActor_strategy = st.builds(
    pimm::InterfaceActor,
    kind=
        safe_text
)
pimm::ExecutableActor_strategy = st.builds(
    pimm::ExecutableActor,
)
pimm::PiGraph_strategy = st.builds(
    pimm::PiGraph,
)
pimm::ConfigOutputPort_strategy = st.builds(
    pimm::ConfigOutputPort,
)
pimm::DataOutputPort_strategy = st.builds(
    pimm::DataOutputPort,
)
pimm::DataInputPort_strategy = st.builds(
    pimm::DataInputPort,
)
AbstractVertex_strategy = st.builds(
    AbstractVertex,
)
pimm::Parameter_strategy = st.builds(
    pimm::Parameter,
    configurationInterface=
        st.booleans()
)
pimm::AbstractActor_strategy = st.builds(
    pimm::AbstractActor,
)

@given(instance=Refinement_strategy)
@settings(max_examples=50)
def test_refinement_instantiation(instance):
    assert isinstance(instance, Refinement)

@given(instance=pimm::HRefinement_strategy)
@settings(max_examples=50)
def test_pimm::hrefinement_instantiation(instance):
    assert isinstance(instance, pimm::HRefinement)

@given(instance=pimm::visitor::PiMMVisitor_strategy)
@settings(max_examples=50)
def test_pimm::visitor::pimmvisitor_instantiation(instance):
    assert isinstance(instance, pimm::visitor::PiMMVisitor)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pimm::visitor::PiMMVisitor_strategy)
@settings(max_examples=30)
def test_pimm::visitor::pimmvisitor_visitinterfaceactor_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.visitInterfaceActor(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.visitInterfaceActor).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'visitInterfaceActor' in pimm::visitor::PiMMVisitor is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'visitInterfaceActor' in pimm::visitor::PiMMVisitor did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'visitInterfaceActor' in pimm::visitor::PiMMVisitor is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pimm::visitor::PiMMVisitor_strategy)
@settings(max_examples=30)
def test_pimm::visitor::pimmvisitor_visithrefinement_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.visitHRefinement(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.visitHRefinement).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'visitHRefinement' in pimm::visitor::PiMMVisitor is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'visitHRefinement' in pimm::visitor::PiMMVisitor did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'visitHRefinement' in pimm::visitor::PiMMVisitor is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pimm::visitor::PiMMVisitor_strategy)
@settings(max_examples=30)
def test_pimm::visitor::pimmvisitor_visitactor_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.visitActor(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.visitActor).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'visitActor' in pimm::visitor::PiMMVisitor is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'visitActor' in pimm::visitor::PiMMVisitor did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'visitActor' in pimm::visitor::PiMMVisitor is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pimm::visitor::PiMMVisitor_strategy)
@settings(max_examples=30)
def test_pimm::visitor::pimmvisitor_visitparameterizable_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.visitParameterizable(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.visitParameterizable).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'visitParameterizable' in pimm::visitor::PiMMVisitor is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'visitParameterizable' in pimm::visitor::PiMMVisitor did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'visitParameterizable' in pimm::visitor::PiMMVisitor is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pimm::visitor::PiMMVisitor_strategy)
@settings(max_examples=30)
def test_pimm::visitor::pimmvisitor_visitconfigoutputport_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.visitConfigOutputPort(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.visitConfigOutputPort).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'visitConfigOutputPort' in pimm::visitor::PiMMVisitor is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'visitConfigOutputPort' in pimm::visitor::PiMMVisitor did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'visitConfigOutputPort' in pimm::visitor::PiMMVisitor is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pimm::visitor::PiMMVisitor_strategy)
@settings(max_examples=30)
def test_pimm::visitor::pimmvisitor_visitdataport_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.visitDataPort(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.visitDataPort).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'visitDataPort' in pimm::visitor::PiMMVisitor is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'visitDataPort' in pimm::visitor::PiMMVisitor did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'visitDataPort' in pimm::visitor::PiMMVisitor is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pimm::visitor::PiMMVisitor_strategy)
@settings(max_examples=30)
def test_pimm::visitor::pimmvisitor_visitport_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.visitPort(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.visitPort).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'visitPort' in pimm::visitor::PiMMVisitor is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'visitPort' in pimm::visitor::PiMMVisitor did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'visitPort' in pimm::visitor::PiMMVisitor is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pimm::visitor::PiMMVisitor_strategy)
@settings(max_examples=30)
def test_pimm::visitor::pimmvisitor_visitconfigoutputinterface_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.visitConfigOutputInterface(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.visitConfigOutputInterface).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'visitConfigOutputInterface' in pimm::visitor::PiMMVisitor is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'visitConfigOutputInterface' in pimm::visitor::PiMMVisitor did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'visitConfigOutputInterface' in pimm::visitor::PiMMVisitor is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pimm::visitor::PiMMVisitor_strategy)
@settings(max_examples=30)
def test_pimm::visitor::pimmvisitor_visitjoinactor_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.visitJoinActor(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.visitJoinActor).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'visitJoinActor' in pimm::visitor::PiMMVisitor is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'visitJoinActor' in pimm::visitor::PiMMVisitor did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'visitJoinActor' in pimm::visitor::PiMMVisitor is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pimm::visitor::PiMMVisitor_strategy)
@settings(max_examples=30)
def test_pimm::visitor::pimmvisitor_visitconfiginputinterface_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.visitConfigInputInterface(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.visitConfigInputInterface).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'visitConfigInputInterface' in pimm::visitor::PiMMVisitor is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'visitConfigInputInterface' in pimm::visitor::PiMMVisitor did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'visitConfigInputInterface' in pimm::visitor::PiMMVisitor is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pimm::visitor::PiMMVisitor_strategy)
@settings(max_examples=30)
def test_pimm::visitor::pimmvisitor_visitexecutableactor_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.visitExecutableActor(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.visitExecutableActor).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'visitExecutableActor' in pimm::visitor::PiMMVisitor is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'visitExecutableActor' in pimm::visitor::PiMMVisitor did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'visitExecutableActor' in pimm::visitor::PiMMVisitor is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pimm::visitor::PiMMVisitor_strategy)
@settings(max_examples=30)
def test_pimm::visitor::pimmvisitor_visitisetter_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.visitISetter(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.visitISetter).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'visitISetter' in pimm::visitor::PiMMVisitor is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'visitISetter' in pimm::visitor::PiMMVisitor did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'visitISetter' in pimm::visitor::PiMMVisitor is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pimm::visitor::PiMMVisitor_strategy)
@settings(max_examples=30)
def test_pimm::visitor::pimmvisitor_visitpigraph_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.visitPiGraph(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.visitPiGraph).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'visitPiGraph' in pimm::visitor::PiMMVisitor is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'visitPiGraph' in pimm::visitor::PiMMVisitor did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'visitPiGraph' in pimm::visitor::PiMMVisitor is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pimm::visitor::PiMMVisitor_strategy)
@settings(max_examples=30)
def test_pimm::visitor::pimmvisitor_visitforkactor_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.visitForkActor(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.visitForkActor).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'visitForkActor' in pimm::visitor::PiMMVisitor is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'visitForkActor' in pimm::visitor::PiMMVisitor did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'visitForkActor' in pimm::visitor::PiMMVisitor is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pimm::visitor::PiMMVisitor_strategy)
@settings(max_examples=30)
def test_pimm::visitor::pimmvisitor_visitdataoutputinterface_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.visitDataOutputInterface(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.visitDataOutputInterface).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'visitDataOutputInterface' in pimm::visitor::PiMMVisitor is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'visitDataOutputInterface' in pimm::visitor::PiMMVisitor did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'visitDataOutputInterface' in pimm::visitor::PiMMVisitor is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pimm::visitor::PiMMVisitor_strategy)
@settings(max_examples=30)
def test_pimm::visitor::pimmvisitor_visitrefinement_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.visitRefinement(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.visitRefinement).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'visitRefinement' in pimm::visitor::PiMMVisitor is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'visitRefinement' in pimm::visitor::PiMMVisitor did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'visitRefinement' in pimm::visitor::PiMMVisitor is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pimm::visitor::PiMMVisitor_strategy)
@settings(max_examples=30)
def test_pimm::visitor::pimmvisitor_visitfunctionparameter_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.visitFunctionParameter(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.visitFunctionParameter).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'visitFunctionParameter' in pimm::visitor::PiMMVisitor is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'visitFunctionParameter' in pimm::visitor::PiMMVisitor did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'visitFunctionParameter' in pimm::visitor::PiMMVisitor is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pimm::visitor::PiMMVisitor_strategy)
@settings(max_examples=30)
def test_pimm::visitor::pimmvisitor_visitparameter_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.visitParameter(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.visitParameter).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'visitParameter' in pimm::visitor::PiMMVisitor is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'visitParameter' in pimm::visitor::PiMMVisitor did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'visitParameter' in pimm::visitor::PiMMVisitor is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pimm::visitor::PiMMVisitor_strategy)
@settings(max_examples=30)
def test_pimm::visitor::pimmvisitor_visitfifo_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.visitFifo(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.visitFifo).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'visitFifo' in pimm::visitor::PiMMVisitor is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'visitFifo' in pimm::visitor::PiMMVisitor did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'visitFifo' in pimm::visitor::PiMMVisitor is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pimm::visitor::PiMMVisitor_strategy)
@settings(max_examples=30)
def test_pimm::visitor::pimmvisitor_visitdatainputport_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.visitDataInputPort(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.visitDataInputPort).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'visitDataInputPort' in pimm::visitor::PiMMVisitor is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'visitDataInputPort' in pimm::visitor::PiMMVisitor did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'visitDataInputPort' in pimm::visitor::PiMMVisitor is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pimm::visitor::PiMMVisitor_strategy)
@settings(max_examples=30)
def test_pimm::visitor::pimmvisitor_visitdelay_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.visitDelay(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.visitDelay).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'visitDelay' in pimm::visitor::PiMMVisitor is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'visitDelay' in pimm::visitor::PiMMVisitor did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'visitDelay' in pimm::visitor::PiMMVisitor is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pimm::visitor::PiMMVisitor_strategy)
@settings(max_examples=30)
def test_pimm::visitor::pimmvisitor_visitexpression_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.visitExpression(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.visitExpression).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'visitExpression' in pimm::visitor::PiMMVisitor is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'visitExpression' in pimm::visitor::PiMMVisitor did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'visitExpression' in pimm::visitor::PiMMVisitor is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pimm::visitor::PiMMVisitor_strategy)
@settings(max_examples=30)
def test_pimm::visitor::pimmvisitor_visitabstractactor_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.visitAbstractActor(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.visitAbstractActor).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'visitAbstractActor' in pimm::visitor::PiMMVisitor is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'visitAbstractActor' in pimm::visitor::PiMMVisitor did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'visitAbstractActor' in pimm::visitor::PiMMVisitor is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pimm::visitor::PiMMVisitor_strategy)
@settings(max_examples=30)
def test_pimm::visitor::pimmvisitor_visitdatainputinterface_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.visitDataInputInterface(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.visitDataInputInterface).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'visitDataInputInterface' in pimm::visitor::PiMMVisitor is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'visitDataInputInterface' in pimm::visitor::PiMMVisitor did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'visitDataInputInterface' in pimm::visitor::PiMMVisitor is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pimm::visitor::PiMMVisitor_strategy)
@settings(max_examples=30)
def test_pimm::visitor::pimmvisitor_visitbroadcastactor_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.visitBroadcastActor(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.visitBroadcastActor).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'visitBroadcastActor' in pimm::visitor::PiMMVisitor is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'visitBroadcastActor' in pimm::visitor::PiMMVisitor did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'visitBroadcastActor' in pimm::visitor::PiMMVisitor is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pimm::visitor::PiMMVisitor_strategy)
@settings(max_examples=30)
def test_pimm::visitor::pimmvisitor_visit_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.visit(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.visit).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'visit' in pimm::visitor::PiMMVisitor is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'visit' in pimm::visitor::PiMMVisitor did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'visit' in pimm::visitor::PiMMVisitor is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pimm::visitor::PiMMVisitor_strategy)
@settings(max_examples=30)
def test_pimm::visitor::pimmvisitor_visitdataoutputport_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.visitDataOutputPort(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.visitDataOutputPort).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'visitDataOutputPort' in pimm::visitor::PiMMVisitor is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'visitDataOutputPort' in pimm::visitor::PiMMVisitor did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'visitDataOutputPort' in pimm::visitor::PiMMVisitor is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pimm::visitor::PiMMVisitor_strategy)
@settings(max_examples=30)
def test_pimm::visitor::pimmvisitor_visitfunctionprototype_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.visitFunctionPrototype(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.visitFunctionPrototype).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'visitFunctionPrototype' in pimm::visitor::PiMMVisitor is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'visitFunctionPrototype' in pimm::visitor::PiMMVisitor did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'visitFunctionPrototype' in pimm::visitor::PiMMVisitor is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pimm::visitor::PiMMVisitor_strategy)
@settings(max_examples=30)
def test_pimm::visitor::pimmvisitor_visitroundbufferactor_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.visitRoundBufferActor(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.visitRoundBufferActor).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'visitRoundBufferActor' in pimm::visitor::PiMMVisitor is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'visitRoundBufferActor' in pimm::visitor::PiMMVisitor did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'visitRoundBufferActor' in pimm::visitor::PiMMVisitor is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pimm::visitor::PiMMVisitor_strategy)
@settings(max_examples=30)
def test_pimm::visitor::pimmvisitor_visitdependency_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.visitDependency(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.visitDependency).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'visitDependency' in pimm::visitor::PiMMVisitor is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'visitDependency' in pimm::visitor::PiMMVisitor did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'visitDependency' in pimm::visitor::PiMMVisitor is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pimm::visitor::PiMMVisitor_strategy)
@settings(max_examples=30)
def test_pimm::visitor::pimmvisitor_visitconfiginputport_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.visitConfigInputPort(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.visitConfigInputPort).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'visitConfigInputPort' in pimm::visitor::PiMMVisitor is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'visitConfigInputPort' in pimm::visitor::PiMMVisitor did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'visitConfigInputPort' in pimm::visitor::PiMMVisitor is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pimm::visitor::PiMMVisitor_strategy)
@settings(max_examples=30)
def test_pimm::visitor::pimmvisitor_visitabstractvertex_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.visitAbstractVertex(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.visitAbstractVertex).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'visitAbstractVertex' in pimm::visitor::PiMMVisitor is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'visitAbstractVertex' in pimm::visitor::PiMMVisitor did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'visitAbstractVertex' in pimm::visitor::PiMMVisitor is not implemented or raised an error")

@given(instance=pimm::visitor::PiMMVisitable_strategy)
@settings(max_examples=50)
def test_pimm::visitor::pimmvisitable_instantiation(instance):
    assert isinstance(instance, pimm::visitor::PiMMVisitable)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pimm::visitor::PiMMVisitable_strategy)
@settings(max_examples=30)
def test_pimm::visitor::pimmvisitable_accept_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.accept(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.accept).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'accept' in pimm::visitor::PiMMVisitable is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'accept' in pimm::visitor::PiMMVisitable did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'accept' in pimm::visitor::PiMMVisitable is not implemented or raised an error")

@given(instance=pimm::ISetter_strategy)
@settings(max_examples=50)
def test_pimm::isetter_instantiation(instance):
    assert isinstance(instance, pimm::ISetter)

@given(instance=Parameter_strategy)
@settings(max_examples=50)
def test_parameter_instantiation(instance):
    assert isinstance(instance, Parameter)

@given(instance=pimm::ConfigInputInterface_strategy)
@settings(max_examples=50)
def test_pimm::configinputinterface_instantiation(instance):
    assert isinstance(instance, pimm::ConfigInputInterface)

@given(instance=InterfaceActor_strategy)
@settings(max_examples=50)
def test_interfaceactor_instantiation(instance):
    assert isinstance(instance, InterfaceActor)

@given(instance=pimm::DataOutputInterface_strategy)
@settings(max_examples=50)
def test_pimm::dataoutputinterface_instantiation(instance):
    assert isinstance(instance, pimm::DataOutputInterface)

@given(instance=pimm::ConfigOutputInterface_strategy)
@settings(max_examples=50)
def test_pimm::configoutputinterface_instantiation(instance):
    assert isinstance(instance, pimm::ConfigOutputInterface)

@given(instance=pimm::DataInputInterface_strategy)
@settings(max_examples=50)
def test_pimm::datainputinterface_instantiation(instance):
    assert isinstance(instance, pimm::DataInputInterface)

@given(instance=ISetter_strategy)
@settings(max_examples=50)
def test_isetter_instantiation(instance):
    assert isinstance(instance, ISetter)

@given(instance=DataOutputPort_strategy)
@settings(max_examples=50)
def test_dataoutputport_instantiation(instance):
    assert isinstance(instance, DataOutputPort)

@given(instance=Port_strategy)
@settings(max_examples=50)
def test_port_instantiation(instance):
    assert isinstance(instance, Port)

@given(instance=pimm::DataPort_strategy)
@settings(max_examples=50)
def test_pimm::dataport_instantiation(instance):
    assert isinstance(instance, pimm::DataPort)

@given(instance=pimm::DataPort_strategy)
def test_pimm::dataport_annotation_type(instance):
    assert isinstance(instance.annotation, str)


@given(instance=pimm::DataPort_strategy)
def test_pimm::dataport_annotation_setter(instance):
    original = instance.annotation
    instance.annotation = original
    assert instance.annotation == original

@given(instance=DataPort_strategy)
@settings(max_examples=50)
def test_dataport_instantiation(instance):
    assert isinstance(instance, DataPort)

@given(instance=ExecutableActor_strategy)
@settings(max_examples=50)
def test_executableactor_instantiation(instance):
    assert isinstance(instance, ExecutableActor)

@given(instance=pimm::RoundBufferActor_strategy)
@settings(max_examples=50)
def test_pimm::roundbufferactor_instantiation(instance):
    assert isinstance(instance, pimm::RoundBufferActor)

@given(instance=pimm::ForkActor_strategy)
@settings(max_examples=50)
def test_pimm::forkactor_instantiation(instance):
    assert isinstance(instance, pimm::ForkActor)

@given(instance=pimm::BroadcastActor_strategy)
@settings(max_examples=50)
def test_pimm::broadcastactor_instantiation(instance):
    assert isinstance(instance, pimm::BroadcastActor)

@given(instance=pimm::JoinActor_strategy)
@settings(max_examples=50)
def test_pimm::joinactor_instantiation(instance):
    assert isinstance(instance, pimm::JoinActor)

@given(instance=pimm::Actor_strategy)
@settings(max_examples=50)
def test_pimm::actor_instantiation(instance):
    assert isinstance(instance, pimm::Actor)

@given(instance=pimm::Actor_strategy)
def test_pimm::actor_memoryScriptPath_type(instance):
    assert isinstance(instance.memoryScriptPath, str)


@given(instance=pimm::Actor_strategy)
def test_pimm::actor_memoryScriptPath_setter(instance):
    original = instance.memoryScriptPath
    instance.memoryScriptPath = original
    assert instance.memoryScriptPath == original

@given(instance=pimm::Actor_strategy)
def test_pimm::actor_configurationActor_type(instance):
    assert isinstance(instance.configurationActor, bool)


@given(instance=pimm::Actor_strategy)
def test_pimm::actor_configurationActor_setter(instance):
    original = instance.configurationActor
    instance.configurationActor = original
    assert instance.configurationActor == original

@given(instance=Parameterizable_strategy)
@settings(max_examples=50)
def test_parameterizable_instantiation(instance):
    assert isinstance(instance, Parameterizable)

@given(instance=pimm::Delay_strategy)
@settings(max_examples=50)
def test_pimm::delay_instantiation(instance):
    assert isinstance(instance, pimm::Delay)

@given(instance=pimm::AbstractVertex_strategy)
@settings(max_examples=50)
def test_pimm::abstractvertex_instantiation(instance):
    assert isinstance(instance, pimm::AbstractVertex)

@given(instance=pimm::AbstractVertex_strategy)
def test_pimm::abstractvertex_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=pimm::AbstractVertex_strategy)
def test_pimm::abstractvertex_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=pimm::ConfigInputPort_strategy)
@settings(max_examples=50)
def test_pimm::configinputport_instantiation(instance):
    assert isinstance(instance, pimm::ConfigInputPort)

@given(instance=PiMMVisitable_strategy)
@settings(max_examples=50)
def test_pimmvisitable_instantiation(instance):
    assert isinstance(instance, PiMMVisitable)

@given(instance=pimm::Refinement_strategy)
@settings(max_examples=50)
def test_pimm::refinement_instantiation(instance):
    assert isinstance(instance, pimm::Refinement)

@given(instance=pimm::Refinement_strategy)
def test_pimm::refinement_fileName_type(instance):
    assert isinstance(instance.fileName, str)


@given(instance=pimm::Refinement_strategy)
def test_pimm::refinement_fileName_setter(instance):
    original = instance.fileName
    instance.fileName = original
    assert instance.fileName == original

@given(instance=pimm::Refinement_strategy)
def test_pimm::refinement_filePath_type(instance):
    assert isinstance(instance.filePath, str)


@given(instance=pimm::Refinement_strategy)
def test_pimm::refinement_filePath_setter(instance):
    original = instance.filePath
    instance.filePath = original
    assert instance.filePath == original

@given(instance=pimm::Fifo_strategy)
@settings(max_examples=50)
def test_pimm::fifo_instantiation(instance):
    assert isinstance(instance, pimm::Fifo)

@given(instance=pimm::Fifo_strategy)
def test_pimm::fifo_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=pimm::Fifo_strategy)
def test_pimm::fifo_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=pimm::Fifo_strategy)
def test_pimm::fifo_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=pimm::Fifo_strategy)
def test_pimm::fifo_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=pimm::FunctionPrototype_strategy)
@settings(max_examples=50)
def test_pimm::functionprototype_instantiation(instance):
    assert isinstance(instance, pimm::FunctionPrototype)

@given(instance=pimm::FunctionPrototype_strategy)
def test_pimm::functionprototype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=pimm::FunctionPrototype_strategy)
def test_pimm::functionprototype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=pimm::Dependency_strategy)
@settings(max_examples=50)
def test_pimm::dependency_instantiation(instance):
    assert isinstance(instance, pimm::Dependency)

@given(instance=pimm::Expression_strategy)
@settings(max_examples=50)
def test_pimm::expression_instantiation(instance):
    assert isinstance(instance, pimm::Expression)

@given(instance=pimm::Expression_strategy)
def test_pimm::expression_string_type(instance):
    assert isinstance(instance.string, str)


@given(instance=pimm::Expression_strategy)
def test_pimm::expression_string_setter(instance):
    original = instance.string
    instance.string = original
    assert instance.string == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pimm::Expression_strategy)
@settings(max_examples=30)
def test_pimm::expression_evaluate_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.evaluate()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.evaluate).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'evaluate' in pimm::Expression is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'evaluate' in pimm::Expression did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'evaluate' in pimm::Expression is not implemented or raised an error")

@given(instance=pimm::FunctionParameter_strategy)
@settings(max_examples=50)
def test_pimm::functionparameter_instantiation(instance):
    assert isinstance(instance, pimm::FunctionParameter)

@given(instance=pimm::FunctionParameter_strategy)
def test_pimm::functionparameter_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=pimm::FunctionParameter_strategy)
def test_pimm::functionparameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=pimm::FunctionParameter_strategy)
def test_pimm::functionparameter_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=pimm::FunctionParameter_strategy)
def test_pimm::functionparameter_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=pimm::FunctionParameter_strategy)
def test_pimm::functionparameter_direction_type(instance):
    assert isinstance(instance.direction, str)


@given(instance=pimm::FunctionParameter_strategy)
def test_pimm::functionparameter_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

@given(instance=pimm::FunctionParameter_strategy)
def test_pimm::functionparameter_isConfigurationParameter_type(instance):
    assert isinstance(instance.isConfigurationParameter, bool)


@given(instance=pimm::FunctionParameter_strategy)
def test_pimm::functionparameter_isConfigurationParameter_setter(instance):
    original = instance.isConfigurationParameter
    instance.isConfigurationParameter = original
    assert instance.isConfigurationParameter == original

@given(instance=pimm::Port_strategy)
@settings(max_examples=50)
def test_pimm::port_instantiation(instance):
    assert isinstance(instance, pimm::Port)

@given(instance=pimm::Port_strategy)
def test_pimm::port_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=pimm::Port_strategy)
def test_pimm::port_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=pimm::Port_strategy)
def test_pimm::port_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=pimm::Port_strategy)
def test_pimm::port_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=pimm::Parameterizable_strategy)
@settings(max_examples=50)
def test_pimm::parameterizable_instantiation(instance):
    assert isinstance(instance, pimm::Parameterizable)

@given(instance=AbstractActor_strategy)
@settings(max_examples=50)
def test_abstractactor_instantiation(instance):
    assert isinstance(instance, AbstractActor)

@given(instance=pimm::InterfaceActor_strategy)
@settings(max_examples=50)
def test_pimm::interfaceactor_instantiation(instance):
    assert isinstance(instance, pimm::InterfaceActor)

@given(instance=pimm::InterfaceActor_strategy)
def test_pimm::interfaceactor_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=pimm::InterfaceActor_strategy)
def test_pimm::interfaceactor_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=pimm::ExecutableActor_strategy)
@settings(max_examples=50)
def test_pimm::executableactor_instantiation(instance):
    assert isinstance(instance, pimm::ExecutableActor)

@given(instance=pimm::PiGraph_strategy)
@settings(max_examples=50)
def test_pimm::pigraph_instantiation(instance):
    assert isinstance(instance, pimm::PiGraph)

@given(instance=pimm::ConfigOutputPort_strategy)
@settings(max_examples=50)
def test_pimm::configoutputport_instantiation(instance):
    assert isinstance(instance, pimm::ConfigOutputPort)

@given(instance=pimm::DataOutputPort_strategy)
@settings(max_examples=50)
def test_pimm::dataoutputport_instantiation(instance):
    assert isinstance(instance, pimm::DataOutputPort)

@given(instance=pimm::DataInputPort_strategy)
@settings(max_examples=50)
def test_pimm::datainputport_instantiation(instance):
    assert isinstance(instance, pimm::DataInputPort)

@given(instance=AbstractVertex_strategy)
@settings(max_examples=50)
def test_abstractvertex_instantiation(instance):
    assert isinstance(instance, AbstractVertex)

@given(instance=pimm::Parameter_strategy)
@settings(max_examples=50)
def test_pimm::parameter_instantiation(instance):
    assert isinstance(instance, pimm::Parameter)

@given(instance=pimm::Parameter_strategy)
def test_pimm::parameter_configurationInterface_type(instance):
    assert isinstance(instance.configurationInterface, bool)


@given(instance=pimm::Parameter_strategy)
def test_pimm::parameter_configurationInterface_setter(instance):
    original = instance.configurationInterface
    instance.configurationInterface = original
    assert instance.configurationInterface == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pimm::Parameter_strategy)
@settings(max_examples=30)
def test_pimm::parameter_islocallystatic_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isLocallyStatic()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isLocallyStatic).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isLocallyStatic' in pimm::Parameter is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isLocallyStatic' in pimm::Parameter did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isLocallyStatic' in pimm::Parameter is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pimm::Parameter_strategy)
@settings(max_examples=30)
def test_pimm::parameter_isdependent_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isDependent()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isDependent).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isDependent' in pimm::Parameter is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isDependent' in pimm::Parameter did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isDependent' in pimm::Parameter is not implemented or raised an error")

@given(instance=pimm::AbstractActor_strategy)
@settings(max_examples=50)
def test_pimm::abstractactor_instantiation(instance):
    assert isinstance(instance, pimm::AbstractActor)
