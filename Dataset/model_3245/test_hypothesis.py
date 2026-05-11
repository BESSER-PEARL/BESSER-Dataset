import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ToCompositeModeEdge,
    FromSubModeEdge,
    InitEdge,
    FromCompositeModeInitEdge,
    ToConditionalConnectorEdge,
    remes::EntryConditionalTopInitEdge,
    FromCompositeModeEdge,
    Edge,
    remes::EntryConditionalTopEdge,
    remes::ExitConditionalSubEdge,
    ToSubModeEdge,
    remes::EntryInitEdge,
    remes::EntryEdge,
    FromConditionalConnectorEdge,
    remes::ExitConditionalTopEdge,
    remes::EntryConditionalSubEdge,
    remes::Edge,
    remes::FromConditionalConnectorEdge,
    remes::ToConditionalConnectorEdge,
    remes::ConditionalConnector,
    remes::FromCompositeModeEdge,
    remes::FromCompositeModeInitEdge,
    remes::ToCompositeModeEdge,
    remes::Resource,
    remes::ToSubModeEdge,
    remes::RemesDiagram,
    remes::Variable,
    remes::Mode,
    remes::InternalEdge,
    remes::InitEdge,
    remes::FromSubModeEdge,
    remes::ExitEdge,
    Mode,
    remes::SubMode,
    remes::CompositeMode,
    PrimitiveTypes,
    ResourceTypes,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_tocompositemodeedge_is_not_abstract():
    assert not inspect.isabstract(ToCompositeModeEdge)


def test_tocompositemodeedge_constructor_exists():
    assert callable(ToCompositeModeEdge.__init__)


def test_tocompositemodeedge_constructor_args():
    sig = inspect.signature(ToCompositeModeEdge.__init__)
    params = list(sig.parameters.keys())



def test_fromsubmodeedge_is_not_abstract():
    assert not inspect.isabstract(FromSubModeEdge)


def test_fromsubmodeedge_constructor_exists():
    assert callable(FromSubModeEdge.__init__)


def test_fromsubmodeedge_constructor_args():
    sig = inspect.signature(FromSubModeEdge.__init__)
    params = list(sig.parameters.keys())



def test_initedge_is_not_abstract():
    assert not inspect.isabstract(InitEdge)


def test_initedge_constructor_exists():
    assert callable(InitEdge.__init__)


def test_initedge_constructor_args():
    sig = inspect.signature(InitEdge.__init__)
    params = list(sig.parameters.keys())



def test_fromcompositemodeinitedge_is_not_abstract():
    assert not inspect.isabstract(FromCompositeModeInitEdge)


def test_fromcompositemodeinitedge_constructor_exists():
    assert callable(FromCompositeModeInitEdge.__init__)


def test_fromcompositemodeinitedge_constructor_args():
    sig = inspect.signature(FromCompositeModeInitEdge.__init__)
    params = list(sig.parameters.keys())



def test_toconditionalconnectoredge_is_not_abstract():
    assert not inspect.isabstract(ToConditionalConnectorEdge)


def test_toconditionalconnectoredge_constructor_exists():
    assert callable(ToConditionalConnectorEdge.__init__)


def test_toconditionalconnectoredge_constructor_args():
    sig = inspect.signature(ToConditionalConnectorEdge.__init__)
    params = list(sig.parameters.keys())



def test_remes::entryconditionaltopinitedge_is_not_abstract():
    assert not inspect.isabstract(remes::EntryConditionalTopInitEdge)


def test_remes::entryconditionaltopinitedge_constructor_exists():
    assert callable(remes::EntryConditionalTopInitEdge.__init__)


def test_remes::entryconditionaltopinitedge_constructor_args():
    sig = inspect.signature(remes::EntryConditionalTopInitEdge.__init__)
    params = list(sig.parameters.keys())



def test_fromcompositemodeedge_is_not_abstract():
    assert not inspect.isabstract(FromCompositeModeEdge)


def test_fromcompositemodeedge_constructor_exists():
    assert callable(FromCompositeModeEdge.__init__)


def test_fromcompositemodeedge_constructor_args():
    sig = inspect.signature(FromCompositeModeEdge.__init__)
    params = list(sig.parameters.keys())



def test_edge_is_not_abstract():
    assert not inspect.isabstract(Edge)


def test_edge_constructor_exists():
    assert callable(Edge.__init__)


def test_edge_constructor_args():
    sig = inspect.signature(Edge.__init__)
    params = list(sig.parameters.keys())



def test_remes::entryconditionaltopedge_is_not_abstract():
    assert not inspect.isabstract(remes::EntryConditionalTopEdge)


def test_remes::entryconditionaltopedge_constructor_exists():
    assert callable(remes::EntryConditionalTopEdge.__init__)


def test_remes::entryconditionaltopedge_constructor_args():
    sig = inspect.signature(remes::EntryConditionalTopEdge.__init__)
    params = list(sig.parameters.keys())



def test_remes::exitconditionalsubedge_is_not_abstract():
    assert not inspect.isabstract(remes::ExitConditionalSubEdge)


def test_remes::exitconditionalsubedge_constructor_exists():
    assert callable(remes::ExitConditionalSubEdge.__init__)


def test_remes::exitconditionalsubedge_constructor_args():
    sig = inspect.signature(remes::ExitConditionalSubEdge.__init__)
    params = list(sig.parameters.keys())



def test_tosubmodeedge_is_not_abstract():
    assert not inspect.isabstract(ToSubModeEdge)


def test_tosubmodeedge_constructor_exists():
    assert callable(ToSubModeEdge.__init__)


def test_tosubmodeedge_constructor_args():
    sig = inspect.signature(ToSubModeEdge.__init__)
    params = list(sig.parameters.keys())



def test_remes::entryinitedge_is_not_abstract():
    assert not inspect.isabstract(remes::EntryInitEdge)


def test_remes::entryinitedge_constructor_exists():
    assert callable(remes::EntryInitEdge.__init__)


def test_remes::entryinitedge_constructor_args():
    sig = inspect.signature(remes::EntryInitEdge.__init__)
    params = list(sig.parameters.keys())



def test_remes::entryedge_is_not_abstract():
    assert not inspect.isabstract(remes::EntryEdge)


def test_remes::entryedge_constructor_exists():
    assert callable(remes::EntryEdge.__init__)


def test_remes::entryedge_constructor_args():
    sig = inspect.signature(remes::EntryEdge.__init__)
    params = list(sig.parameters.keys())



def test_fromconditionalconnectoredge_is_not_abstract():
    assert not inspect.isabstract(FromConditionalConnectorEdge)


def test_fromconditionalconnectoredge_constructor_exists():
    assert callable(FromConditionalConnectorEdge.__init__)


def test_fromconditionalconnectoredge_constructor_args():
    sig = inspect.signature(FromConditionalConnectorEdge.__init__)
    params = list(sig.parameters.keys())



def test_remes::exitconditionaltopedge_is_not_abstract():
    assert not inspect.isabstract(remes::ExitConditionalTopEdge)


def test_remes::exitconditionaltopedge_constructor_exists():
    assert callable(remes::ExitConditionalTopEdge.__init__)


def test_remes::exitconditionaltopedge_constructor_args():
    sig = inspect.signature(remes::ExitConditionalTopEdge.__init__)
    params = list(sig.parameters.keys())



def test_remes::entryconditionalsubedge_is_not_abstract():
    assert not inspect.isabstract(remes::EntryConditionalSubEdge)


def test_remes::entryconditionalsubedge_constructor_exists():
    assert callable(remes::EntryConditionalSubEdge.__init__)


def test_remes::entryconditionalsubedge_constructor_args():
    sig = inspect.signature(remes::EntryConditionalSubEdge.__init__)
    params = list(sig.parameters.keys())



def test_remes::edge_is_not_abstract():
    assert not inspect.isabstract(remes::Edge)


def test_remes::edge_constructor_exists():
    assert callable(remes::Edge.__init__)


def test_remes::edge_constructor_args():
    sig = inspect.signature(remes::Edge.__init__)
    params = list(sig.parameters.keys())
    assert "actionBody" in params, "Missing parameter 'actionBody'"
    assert "actionGuard" in params, "Missing parameter 'actionGuard'"

def test_remes::edge_has_actionBody():
    assert hasattr(remes::Edge, "actionBody")
    descriptor = None
    for klass in remes::Edge.__mro__:
        if "actionBody" in klass.__dict__:
            descriptor = klass.__dict__["actionBody"]
            break
    assert isinstance(descriptor, property)

def test_remes::edge_has_actionGuard():
    assert hasattr(remes::Edge, "actionGuard")
    descriptor = None
    for klass in remes::Edge.__mro__:
        if "actionGuard" in klass.__dict__:
            descriptor = klass.__dict__["actionGuard"]
            break
    assert isinstance(descriptor, property)



def test_remes::fromconditionalconnectoredge_is_not_abstract():
    assert not inspect.isabstract(remes::FromConditionalConnectorEdge)


def test_remes::fromconditionalconnectoredge_constructor_exists():
    assert callable(remes::FromConditionalConnectorEdge.__init__)


def test_remes::fromconditionalconnectoredge_constructor_args():
    sig = inspect.signature(remes::FromConditionalConnectorEdge.__init__)
    params = list(sig.parameters.keys())



def test_remes::toconditionalconnectoredge_is_not_abstract():
    assert not inspect.isabstract(remes::ToConditionalConnectorEdge)


def test_remes::toconditionalconnectoredge_constructor_exists():
    assert callable(remes::ToConditionalConnectorEdge.__init__)


def test_remes::toconditionalconnectoredge_constructor_args():
    sig = inspect.signature(remes::ToConditionalConnectorEdge.__init__)
    params = list(sig.parameters.keys())



def test_remes::conditionalconnector_is_not_abstract():
    assert not inspect.isabstract(remes::ConditionalConnector)


def test_remes::conditionalconnector_constructor_exists():
    assert callable(remes::ConditionalConnector.__init__)


def test_remes::conditionalconnector_constructor_args():
    sig = inspect.signature(remes::ConditionalConnector.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_remes::conditionalconnector_has_name():
    assert hasattr(remes::ConditionalConnector, "name")
    descriptor = None
    for klass in remes::ConditionalConnector.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_remes::fromcompositemodeedge_is_not_abstract():
    assert not inspect.isabstract(remes::FromCompositeModeEdge)


def test_remes::fromcompositemodeedge_constructor_exists():
    assert callable(remes::FromCompositeModeEdge.__init__)


def test_remes::fromcompositemodeedge_constructor_args():
    sig = inspect.signature(remes::FromCompositeModeEdge.__init__)
    params = list(sig.parameters.keys())



def test_remes::fromcompositemodeinitedge_is_not_abstract():
    assert not inspect.isabstract(remes::FromCompositeModeInitEdge)


def test_remes::fromcompositemodeinitedge_constructor_exists():
    assert callable(remes::FromCompositeModeInitEdge.__init__)


def test_remes::fromcompositemodeinitedge_constructor_args():
    sig = inspect.signature(remes::FromCompositeModeInitEdge.__init__)
    params = list(sig.parameters.keys())



def test_remes::tocompositemodeedge_is_not_abstract():
    assert not inspect.isabstract(remes::ToCompositeModeEdge)


def test_remes::tocompositemodeedge_constructor_exists():
    assert callable(remes::ToCompositeModeEdge.__init__)


def test_remes::tocompositemodeedge_constructor_args():
    sig = inspect.signature(remes::ToCompositeModeEdge.__init__)
    params = list(sig.parameters.keys())



def test_remes::resource_is_not_abstract():
    assert not inspect.isabstract(remes::Resource)


def test_remes::resource_constructor_exists():
    assert callable(remes::Resource.__init__)


def test_remes::resource_constructor_args():
    sig = inspect.signature(remes::Resource.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "expression" in params, "Missing parameter 'expression'"

def test_remes::resource_has_type():
    assert hasattr(remes::Resource, "type")
    descriptor = None
    for klass in remes::Resource.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_remes::resource_has_expression():
    assert hasattr(remes::Resource, "expression")
    descriptor = None
    for klass in remes::Resource.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)



def test_remes::tosubmodeedge_is_not_abstract():
    assert not inspect.isabstract(remes::ToSubModeEdge)


def test_remes::tosubmodeedge_constructor_exists():
    assert callable(remes::ToSubModeEdge.__init__)


def test_remes::tosubmodeedge_constructor_args():
    sig = inspect.signature(remes::ToSubModeEdge.__init__)
    params = list(sig.parameters.keys())



def test_remes::remesdiagram_is_not_abstract():
    assert not inspect.isabstract(remes::RemesDiagram)


def test_remes::remesdiagram_constructor_exists():
    assert callable(remes::RemesDiagram.__init__)


def test_remes::remesdiagram_constructor_args():
    sig = inspect.signature(remes::RemesDiagram.__init__)
    params = list(sig.parameters.keys())



def test_remes::variable_is_not_abstract():
    assert not inspect.isabstract(remes::Variable)


def test_remes::variable_constructor_exists():
    assert callable(remes::Variable.__init__)


def test_remes::variable_constructor_args():
    sig = inspect.signature(remes::Variable.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "global_" in params, "Missing parameter 'global_'"
    assert "readable" in params, "Missing parameter 'readable'"
    assert "name" in params, "Missing parameter 'name'"
    assert "writable" in params, "Missing parameter 'writable'"
    assert "vectorSize" in params, "Missing parameter 'vectorSize'"
    assert "type" in params, "Missing parameter 'type'"

def test_remes::variable_has_value():
    assert hasattr(remes::Variable, "value")
    descriptor = None
    for klass in remes::Variable.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_remes::variable_has_global_():
    assert hasattr(remes::Variable, "global_")
    descriptor = None
    for klass in remes::Variable.__mro__:
        if "global_" in klass.__dict__:
            descriptor = klass.__dict__["global_"]
            break
    assert isinstance(descriptor, property)

def test_remes::variable_has_readable():
    assert hasattr(remes::Variable, "readable")
    descriptor = None
    for klass in remes::Variable.__mro__:
        if "readable" in klass.__dict__:
            descriptor = klass.__dict__["readable"]
            break
    assert isinstance(descriptor, property)

def test_remes::variable_has_name():
    assert hasattr(remes::Variable, "name")
    descriptor = None
    for klass in remes::Variable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_remes::variable_has_writable():
    assert hasattr(remes::Variable, "writable")
    descriptor = None
    for klass in remes::Variable.__mro__:
        if "writable" in klass.__dict__:
            descriptor = klass.__dict__["writable"]
            break
    assert isinstance(descriptor, property)

def test_remes::variable_has_vectorSize():
    assert hasattr(remes::Variable, "vectorSize")
    descriptor = None
    for klass in remes::Variable.__mro__:
        if "vectorSize" in klass.__dict__:
            descriptor = klass.__dict__["vectorSize"]
            break
    assert isinstance(descriptor, property)

def test_remes::variable_has_type():
    assert hasattr(remes::Variable, "type")
    descriptor = None
    for klass in remes::Variable.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_remes::mode_is_not_abstract():
    assert not inspect.isabstract(remes::Mode)


def test_remes::mode_constructor_exists():
    assert callable(remes::Mode.__init__)


def test_remes::mode_constructor_args():
    sig = inspect.signature(remes::Mode.__init__)
    params = list(sig.parameters.keys())
    assert "initialization" in params, "Missing parameter 'initialization'"
    assert "name" in params, "Missing parameter 'name'"

def test_remes::mode_has_initialization():
    assert hasattr(remes::Mode, "initialization")
    descriptor = None
    for klass in remes::Mode.__mro__:
        if "initialization" in klass.__dict__:
            descriptor = klass.__dict__["initialization"]
            break
    assert isinstance(descriptor, property)

def test_remes::mode_has_name():
    assert hasattr(remes::Mode, "name")
    descriptor = None
    for klass in remes::Mode.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_remes::internaledge_is_not_abstract():
    assert not inspect.isabstract(remes::InternalEdge)


def test_remes::internaledge_constructor_exists():
    assert callable(remes::InternalEdge.__init__)


def test_remes::internaledge_constructor_args():
    sig = inspect.signature(remes::InternalEdge.__init__)
    params = list(sig.parameters.keys())



def test_remes::initedge_is_not_abstract():
    assert not inspect.isabstract(remes::InitEdge)


def test_remes::initedge_constructor_exists():
    assert callable(remes::InitEdge.__init__)


def test_remes::initedge_constructor_args():
    sig = inspect.signature(remes::InitEdge.__init__)
    params = list(sig.parameters.keys())
    assert "initialization" in params, "Missing parameter 'initialization'"

def test_remes::initedge_has_initialization():
    assert hasattr(remes::InitEdge, "initialization")
    descriptor = None
    for klass in remes::InitEdge.__mro__:
        if "initialization" in klass.__dict__:
            descriptor = klass.__dict__["initialization"]
            break
    assert isinstance(descriptor, property)



def test_remes::fromsubmodeedge_is_not_abstract():
    assert not inspect.isabstract(remes::FromSubModeEdge)


def test_remes::fromsubmodeedge_constructor_exists():
    assert callable(remes::FromSubModeEdge.__init__)


def test_remes::fromsubmodeedge_constructor_args():
    sig = inspect.signature(remes::FromSubModeEdge.__init__)
    params = list(sig.parameters.keys())



def test_remes::exitedge_is_not_abstract():
    assert not inspect.isabstract(remes::ExitEdge)


def test_remes::exitedge_constructor_exists():
    assert callable(remes::ExitEdge.__init__)


def test_remes::exitedge_constructor_args():
    sig = inspect.signature(remes::ExitEdge.__init__)
    params = list(sig.parameters.keys())



def test_mode_is_not_abstract():
    assert not inspect.isabstract(Mode)


def test_mode_constructor_exists():
    assert callable(Mode.__init__)


def test_mode_constructor_args():
    sig = inspect.signature(Mode.__init__)
    params = list(sig.parameters.keys())



def test_remes::submode_is_not_abstract():
    assert not inspect.isabstract(remes::SubMode)


def test_remes::submode_constructor_exists():
    assert callable(remes::SubMode.__init__)


def test_remes::submode_constructor_args():
    sig = inspect.signature(remes::SubMode.__init__)
    params = list(sig.parameters.keys())
    assert "invariant" in params, "Missing parameter 'invariant'"
    assert "isUrgent" in params, "Missing parameter 'isUrgent'"

def test_remes::submode_has_invariant():
    assert hasattr(remes::SubMode, "invariant")
    descriptor = None
    for klass in remes::SubMode.__mro__:
        if "invariant" in klass.__dict__:
            descriptor = klass.__dict__["invariant"]
            break
    assert isinstance(descriptor, property)

def test_remes::submode_has_isUrgent():
    assert hasattr(remes::SubMode, "isUrgent")
    descriptor = None
    for klass in remes::SubMode.__mro__:
        if "isUrgent" in klass.__dict__:
            descriptor = klass.__dict__["isUrgent"]
            break
    assert isinstance(descriptor, property)



def test_remes::compositemode_is_not_abstract():
    assert not inspect.isabstract(remes::CompositeMode)


def test_remes::compositemode_constructor_exists():
    assert callable(remes::CompositeMode.__init__)


def test_remes::compositemode_constructor_args():
    sig = inspect.signature(remes::CompositeMode.__init__)
    params = list(sig.parameters.keys())

def test_primitivetypes_exists():
    # Check that the Enumeration exists
    assert PrimitiveTypes is not None

def test_primitivetypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PrimitiveTypes]
    expected_literals = [
        "boolean",
        "clock",
        "natural",
        "integer",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PrimitiveTypes"

def test_resourcetypes_exists():
    # Check that the Enumeration exists
    assert ResourceTypes is not None

def test_resourcetypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ResourceTypes]
    expected_literals = [
        "cpu",
        "memory",
        "port",
        "bandwidth",
        "power",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ResourceTypes"


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
ToCompositeModeEdge_strategy = st.builds(
    ToCompositeModeEdge,
)
FromSubModeEdge_strategy = st.builds(
    FromSubModeEdge,
)
InitEdge_strategy = st.builds(
    InitEdge,
)
FromCompositeModeInitEdge_strategy = st.builds(
    FromCompositeModeInitEdge,
)
ToConditionalConnectorEdge_strategy = st.builds(
    ToConditionalConnectorEdge,
)
remes::EntryConditionalTopInitEdge_strategy = st.builds(
    remes::EntryConditionalTopInitEdge,
)
FromCompositeModeEdge_strategy = st.builds(
    FromCompositeModeEdge,
)
Edge_strategy = st.builds(
    Edge,
)
remes::EntryConditionalTopEdge_strategy = st.builds(
    remes::EntryConditionalTopEdge,
)
remes::ExitConditionalSubEdge_strategy = st.builds(
    remes::ExitConditionalSubEdge,
)
ToSubModeEdge_strategy = st.builds(
    ToSubModeEdge,
)
remes::EntryInitEdge_strategy = st.builds(
    remes::EntryInitEdge,
)
remes::EntryEdge_strategy = st.builds(
    remes::EntryEdge,
)
FromConditionalConnectorEdge_strategy = st.builds(
    FromConditionalConnectorEdge,
)
remes::ExitConditionalTopEdge_strategy = st.builds(
    remes::ExitConditionalTopEdge,
)
remes::EntryConditionalSubEdge_strategy = st.builds(
    remes::EntryConditionalSubEdge,
)
remes::Edge_strategy = st.builds(
    remes::Edge,
    actionBody=
        safe_text,
    actionGuard=
        safe_text
)
remes::FromConditionalConnectorEdge_strategy = st.builds(
    remes::FromConditionalConnectorEdge,
)
remes::ToConditionalConnectorEdge_strategy = st.builds(
    remes::ToConditionalConnectorEdge,
)
remes::ConditionalConnector_strategy = st.builds(
    remes::ConditionalConnector,
    name=
        safe_text
)
remes::FromCompositeModeEdge_strategy = st.builds(
    remes::FromCompositeModeEdge,
)
remes::FromCompositeModeInitEdge_strategy = st.builds(
    remes::FromCompositeModeInitEdge,
)
remes::ToCompositeModeEdge_strategy = st.builds(
    remes::ToCompositeModeEdge,
)
remes::Resource_strategy = st.builds(
    remes::Resource,
    type=
        safe_text,
    expression=
        safe_text
)
remes::ToSubModeEdge_strategy = st.builds(
    remes::ToSubModeEdge,
)
remes::RemesDiagram_strategy = st.builds(
    remes::RemesDiagram,
)
remes::Variable_strategy = st.builds(
    remes::Variable,
    value=
        safe_text,
    global_=
        st.booleans(),
    readable=
        st.booleans(),
    name=
        safe_text,
    writable=
        st.booleans(),
    vectorSize=
        st.integers(),
    type=
        safe_text
)
remes::Mode_strategy = st.builds(
    remes::Mode,
    initialization=
        safe_text,
    name=
        safe_text
)
remes::InternalEdge_strategy = st.builds(
    remes::InternalEdge,
)
remes::InitEdge_strategy = st.builds(
    remes::InitEdge,
    initialization=
        safe_text
)
remes::FromSubModeEdge_strategy = st.builds(
    remes::FromSubModeEdge,
)
remes::ExitEdge_strategy = st.builds(
    remes::ExitEdge,
)
Mode_strategy = st.builds(
    Mode,
)
remes::SubMode_strategy = st.builds(
    remes::SubMode,
    invariant=
        safe_text,
    isUrgent=
        st.booleans()
)
remes::CompositeMode_strategy = st.builds(
    remes::CompositeMode,
)

@given(instance=ToCompositeModeEdge_strategy)
@settings(max_examples=50)
def test_tocompositemodeedge_instantiation(instance):
    assert isinstance(instance, ToCompositeModeEdge)

@given(instance=FromSubModeEdge_strategy)
@settings(max_examples=50)
def test_fromsubmodeedge_instantiation(instance):
    assert isinstance(instance, FromSubModeEdge)

@given(instance=InitEdge_strategy)
@settings(max_examples=50)
def test_initedge_instantiation(instance):
    assert isinstance(instance, InitEdge)

@given(instance=FromCompositeModeInitEdge_strategy)
@settings(max_examples=50)
def test_fromcompositemodeinitedge_instantiation(instance):
    assert isinstance(instance, FromCompositeModeInitEdge)

@given(instance=ToConditionalConnectorEdge_strategy)
@settings(max_examples=50)
def test_toconditionalconnectoredge_instantiation(instance):
    assert isinstance(instance, ToConditionalConnectorEdge)

@given(instance=remes::EntryConditionalTopInitEdge_strategy)
@settings(max_examples=50)
def test_remes::entryconditionaltopinitedge_instantiation(instance):
    assert isinstance(instance, remes::EntryConditionalTopInitEdge)

@given(instance=FromCompositeModeEdge_strategy)
@settings(max_examples=50)
def test_fromcompositemodeedge_instantiation(instance):
    assert isinstance(instance, FromCompositeModeEdge)

@given(instance=Edge_strategy)
@settings(max_examples=50)
def test_edge_instantiation(instance):
    assert isinstance(instance, Edge)

@given(instance=remes::EntryConditionalTopEdge_strategy)
@settings(max_examples=50)
def test_remes::entryconditionaltopedge_instantiation(instance):
    assert isinstance(instance, remes::EntryConditionalTopEdge)

@given(instance=remes::ExitConditionalSubEdge_strategy)
@settings(max_examples=50)
def test_remes::exitconditionalsubedge_instantiation(instance):
    assert isinstance(instance, remes::ExitConditionalSubEdge)

@given(instance=ToSubModeEdge_strategy)
@settings(max_examples=50)
def test_tosubmodeedge_instantiation(instance):
    assert isinstance(instance, ToSubModeEdge)

@given(instance=remes::EntryInitEdge_strategy)
@settings(max_examples=50)
def test_remes::entryinitedge_instantiation(instance):
    assert isinstance(instance, remes::EntryInitEdge)

@given(instance=remes::EntryEdge_strategy)
@settings(max_examples=50)
def test_remes::entryedge_instantiation(instance):
    assert isinstance(instance, remes::EntryEdge)

@given(instance=FromConditionalConnectorEdge_strategy)
@settings(max_examples=50)
def test_fromconditionalconnectoredge_instantiation(instance):
    assert isinstance(instance, FromConditionalConnectorEdge)

@given(instance=remes::ExitConditionalTopEdge_strategy)
@settings(max_examples=50)
def test_remes::exitconditionaltopedge_instantiation(instance):
    assert isinstance(instance, remes::ExitConditionalTopEdge)

@given(instance=remes::EntryConditionalSubEdge_strategy)
@settings(max_examples=50)
def test_remes::entryconditionalsubedge_instantiation(instance):
    assert isinstance(instance, remes::EntryConditionalSubEdge)

@given(instance=remes::Edge_strategy)
@settings(max_examples=50)
def test_remes::edge_instantiation(instance):
    assert isinstance(instance, remes::Edge)

@given(instance=remes::Edge_strategy)
def test_remes::edge_actionBody_type(instance):
    assert isinstance(instance.actionBody, str)


@given(instance=remes::Edge_strategy)
def test_remes::edge_actionBody_setter(instance):
    original = instance.actionBody
    instance.actionBody = original
    assert instance.actionBody == original

@given(instance=remes::Edge_strategy)
def test_remes::edge_actionGuard_type(instance):
    assert isinstance(instance.actionGuard, str)


@given(instance=remes::Edge_strategy)
def test_remes::edge_actionGuard_setter(instance):
    original = instance.actionGuard
    instance.actionGuard = original
    assert instance.actionGuard == original

@given(instance=remes::FromConditionalConnectorEdge_strategy)
@settings(max_examples=50)
def test_remes::fromconditionalconnectoredge_instantiation(instance):
    assert isinstance(instance, remes::FromConditionalConnectorEdge)

@given(instance=remes::ToConditionalConnectorEdge_strategy)
@settings(max_examples=50)
def test_remes::toconditionalconnectoredge_instantiation(instance):
    assert isinstance(instance, remes::ToConditionalConnectorEdge)

@given(instance=remes::ConditionalConnector_strategy)
@settings(max_examples=50)
def test_remes::conditionalconnector_instantiation(instance):
    assert isinstance(instance, remes::ConditionalConnector)

@given(instance=remes::ConditionalConnector_strategy)
def test_remes::conditionalconnector_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=remes::ConditionalConnector_strategy)
def test_remes::conditionalconnector_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=remes::FromCompositeModeEdge_strategy)
@settings(max_examples=50)
def test_remes::fromcompositemodeedge_instantiation(instance):
    assert isinstance(instance, remes::FromCompositeModeEdge)

@given(instance=remes::FromCompositeModeInitEdge_strategy)
@settings(max_examples=50)
def test_remes::fromcompositemodeinitedge_instantiation(instance):
    assert isinstance(instance, remes::FromCompositeModeInitEdge)

@given(instance=remes::ToCompositeModeEdge_strategy)
@settings(max_examples=50)
def test_remes::tocompositemodeedge_instantiation(instance):
    assert isinstance(instance, remes::ToCompositeModeEdge)

@given(instance=remes::Resource_strategy)
@settings(max_examples=50)
def test_remes::resource_instantiation(instance):
    assert isinstance(instance, remes::Resource)

@given(instance=remes::Resource_strategy)
def test_remes::resource_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=remes::Resource_strategy)
def test_remes::resource_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=remes::Resource_strategy)
def test_remes::resource_expression_type(instance):
    assert isinstance(instance.expression, str)


@given(instance=remes::Resource_strategy)
def test_remes::resource_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=remes::ToSubModeEdge_strategy)
@settings(max_examples=50)
def test_remes::tosubmodeedge_instantiation(instance):
    assert isinstance(instance, remes::ToSubModeEdge)

@given(instance=remes::RemesDiagram_strategy)
@settings(max_examples=50)
def test_remes::remesdiagram_instantiation(instance):
    assert isinstance(instance, remes::RemesDiagram)

@given(instance=remes::Variable_strategy)
@settings(max_examples=50)
def test_remes::variable_instantiation(instance):
    assert isinstance(instance, remes::Variable)

@given(instance=remes::Variable_strategy)
def test_remes::variable_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=remes::Variable_strategy)
def test_remes::variable_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=remes::Variable_strategy)
def test_remes::variable_global__type(instance):
    assert isinstance(instance.global_, bool)


@given(instance=remes::Variable_strategy)
def test_remes::variable_global__setter(instance):
    original = instance.global_
    instance.global_ = original
    assert instance.global_ == original

@given(instance=remes::Variable_strategy)
def test_remes::variable_readable_type(instance):
    assert isinstance(instance.readable, bool)


@given(instance=remes::Variable_strategy)
def test_remes::variable_readable_setter(instance):
    original = instance.readable
    instance.readable = original
    assert instance.readable == original

@given(instance=remes::Variable_strategy)
def test_remes::variable_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=remes::Variable_strategy)
def test_remes::variable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=remes::Variable_strategy)
def test_remes::variable_writable_type(instance):
    assert isinstance(instance.writable, bool)


@given(instance=remes::Variable_strategy)
def test_remes::variable_writable_setter(instance):
    original = instance.writable
    instance.writable = original
    assert instance.writable == original

@given(instance=remes::Variable_strategy)
def test_remes::variable_vectorSize_type(instance):
    assert isinstance(instance.vectorSize, int)


@given(instance=remes::Variable_strategy)
def test_remes::variable_vectorSize_setter(instance):
    original = instance.vectorSize
    instance.vectorSize = original
    assert instance.vectorSize == original

@given(instance=remes::Variable_strategy)
def test_remes::variable_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=remes::Variable_strategy)
def test_remes::variable_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=remes::Mode_strategy)
@settings(max_examples=50)
def test_remes::mode_instantiation(instance):
    assert isinstance(instance, remes::Mode)

@given(instance=remes::Mode_strategy)
def test_remes::mode_initialization_type(instance):
    assert isinstance(instance.initialization, str)


@given(instance=remes::Mode_strategy)
def test_remes::mode_initialization_setter(instance):
    original = instance.initialization
    instance.initialization = original
    assert instance.initialization == original

@given(instance=remes::Mode_strategy)
def test_remes::mode_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=remes::Mode_strategy)
def test_remes::mode_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=remes::InternalEdge_strategy)
@settings(max_examples=50)
def test_remes::internaledge_instantiation(instance):
    assert isinstance(instance, remes::InternalEdge)

@given(instance=remes::InitEdge_strategy)
@settings(max_examples=50)
def test_remes::initedge_instantiation(instance):
    assert isinstance(instance, remes::InitEdge)

@given(instance=remes::InitEdge_strategy)
def test_remes::initedge_initialization_type(instance):
    assert isinstance(instance.initialization, str)


@given(instance=remes::InitEdge_strategy)
def test_remes::initedge_initialization_setter(instance):
    original = instance.initialization
    instance.initialization = original
    assert instance.initialization == original

@given(instance=remes::FromSubModeEdge_strategy)
@settings(max_examples=50)
def test_remes::fromsubmodeedge_instantiation(instance):
    assert isinstance(instance, remes::FromSubModeEdge)

@given(instance=remes::ExitEdge_strategy)
@settings(max_examples=50)
def test_remes::exitedge_instantiation(instance):
    assert isinstance(instance, remes::ExitEdge)

@given(instance=Mode_strategy)
@settings(max_examples=50)
def test_mode_instantiation(instance):
    assert isinstance(instance, Mode)

@given(instance=remes::SubMode_strategy)
@settings(max_examples=50)
def test_remes::submode_instantiation(instance):
    assert isinstance(instance, remes::SubMode)

@given(instance=remes::SubMode_strategy)
def test_remes::submode_invariant_type(instance):
    assert isinstance(instance.invariant, str)


@given(instance=remes::SubMode_strategy)
def test_remes::submode_invariant_setter(instance):
    original = instance.invariant
    instance.invariant = original
    assert instance.invariant == original

@given(instance=remes::SubMode_strategy)
def test_remes::submode_isUrgent_type(instance):
    assert isinstance(instance.isUrgent, bool)


@given(instance=remes::SubMode_strategy)
def test_remes::submode_isUrgent_setter(instance):
    original = instance.isUrgent
    instance.isUrgent = original
    assert instance.isUrgent == original

@given(instance=remes::CompositeMode_strategy)
@settings(max_examples=50)
def test_remes::compositemode_instantiation(instance):
    assert isinstance(instance, remes::CompositeMode)
