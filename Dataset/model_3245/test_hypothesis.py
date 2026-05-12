import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    remes_Resource,
    remes_ToSubModeEdge,
    remes_RemesDiagram,
    remes_Variable,
    remes_Mode,
    remes_InitEdge,
    remes_FromSubModeEdge,
    ToCompositeModeEdge,
    FromSubModeEdge,
    InitEdge,
    FromCompositeModeInitEdge,
    ToConditionalConnectorEdge,
    remes_EntryConditionalTopInitEdge,
    FromCompositeModeEdge,
    Edge,
    remes_EntryConditionalTopEdge,
    remes_ExitEdge,
    remes_ExitConditionalSubEdge,
    ToSubModeEdge,
    remes_EntryInitEdge,
    remes_InternalEdge,
    remes_EntryEdge,
    FromConditionalConnectorEdge,
    remes_ExitConditionalTopEdge,
    remes_EntryConditionalSubEdge,
    remes_Edge,
    remes_FromConditionalConnectorEdge,
    remes_ToConditionalConnectorEdge,
    remes_ConditionalConnector,
    remes_FromCompositeModeEdge,
    remes_FromCompositeModeInitEdge,
    remes_ToCompositeModeEdge,
    Mode,
    remes_SubMode,
    remes_CompositeMode,
    ResourceTypes,
    PrimitiveTypes,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_remes_resource_is_not_abstract():
    assert not inspect.isabstract(remes_Resource)


def test_remes_resource_constructor_exists():
    assert callable(remes_Resource.__init__)


def test_remes_resource_constructor_args():
    sig = inspect.signature(remes_Resource.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"
    assert "type" in params, "Missing parameter 'type'"

def test_remes_resource_has_expression():
    assert hasattr(remes_Resource, "expression")
    descriptor = None
    for klass in remes_Resource.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)

def test_remes_resource_has_type():
    assert hasattr(remes_Resource, "type")
    descriptor = None
    for klass in remes_Resource.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_remes_tosubmodeedge_is_not_abstract():
    assert not inspect.isabstract(remes_ToSubModeEdge)


def test_remes_tosubmodeedge_constructor_exists():
    assert callable(remes_ToSubModeEdge.__init__)


def test_remes_tosubmodeedge_constructor_args():
    sig = inspect.signature(remes_ToSubModeEdge.__init__)
    params = list(sig.parameters.keys())



def test_remes_remesdiagram_is_not_abstract():
    assert not inspect.isabstract(remes_RemesDiagram)


def test_remes_remesdiagram_constructor_exists():
    assert callable(remes_RemesDiagram.__init__)


def test_remes_remesdiagram_constructor_args():
    sig = inspect.signature(remes_RemesDiagram.__init__)
    params = list(sig.parameters.keys())



def test_remes_variable_is_not_abstract():
    assert not inspect.isabstract(remes_Variable)


def test_remes_variable_constructor_exists():
    assert callable(remes_Variable.__init__)


def test_remes_variable_constructor_args():
    sig = inspect.signature(remes_Variable.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "vectorSize" in params, "Missing parameter 'vectorSize'"
    assert "global_" in params, "Missing parameter 'global_'"
    assert "readable" in params, "Missing parameter 'readable'"
    assert "writable" in params, "Missing parameter 'writable'"
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_remes_variable_has_type():
    assert hasattr(remes_Variable, "type")
    descriptor = None
    for klass in remes_Variable.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_remes_variable_has_vectorSize():
    assert hasattr(remes_Variable, "vectorSize")
    descriptor = None
    for klass in remes_Variable.__mro__:
        if "vectorSize" in klass.__dict__:
            descriptor = klass.__dict__["vectorSize"]
            break
    assert isinstance(descriptor, property)

def test_remes_variable_has_global_():
    assert hasattr(remes_Variable, "global_")
    descriptor = None
    for klass in remes_Variable.__mro__:
        if "global_" in klass.__dict__:
            descriptor = klass.__dict__["global_"]
            break
    assert isinstance(descriptor, property)

def test_remes_variable_has_readable():
    assert hasattr(remes_Variable, "readable")
    descriptor = None
    for klass in remes_Variable.__mro__:
        if "readable" in klass.__dict__:
            descriptor = klass.__dict__["readable"]
            break
    assert isinstance(descriptor, property)

def test_remes_variable_has_writable():
    assert hasattr(remes_Variable, "writable")
    descriptor = None
    for klass in remes_Variable.__mro__:
        if "writable" in klass.__dict__:
            descriptor = klass.__dict__["writable"]
            break
    assert isinstance(descriptor, property)

def test_remes_variable_has_value():
    assert hasattr(remes_Variable, "value")
    descriptor = None
    for klass in remes_Variable.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_remes_variable_has_name():
    assert hasattr(remes_Variable, "name")
    descriptor = None
    for klass in remes_Variable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_remes_mode_is_not_abstract():
    assert not inspect.isabstract(remes_Mode)


def test_remes_mode_constructor_exists():
    assert callable(remes_Mode.__init__)


def test_remes_mode_constructor_args():
    sig = inspect.signature(remes_Mode.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "initialization" in params, "Missing parameter 'initialization'"

def test_remes_mode_has_name():
    assert hasattr(remes_Mode, "name")
    descriptor = None
    for klass in remes_Mode.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_remes_mode_has_initialization():
    assert hasattr(remes_Mode, "initialization")
    descriptor = None
    for klass in remes_Mode.__mro__:
        if "initialization" in klass.__dict__:
            descriptor = klass.__dict__["initialization"]
            break
    assert isinstance(descriptor, property)



def test_remes_initedge_is_not_abstract():
    assert not inspect.isabstract(remes_InitEdge)


def test_remes_initedge_constructor_exists():
    assert callable(remes_InitEdge.__init__)


def test_remes_initedge_constructor_args():
    sig = inspect.signature(remes_InitEdge.__init__)
    params = list(sig.parameters.keys())
    assert "initialization" in params, "Missing parameter 'initialization'"

def test_remes_initedge_has_initialization():
    assert hasattr(remes_InitEdge, "initialization")
    descriptor = None
    for klass in remes_InitEdge.__mro__:
        if "initialization" in klass.__dict__:
            descriptor = klass.__dict__["initialization"]
            break
    assert isinstance(descriptor, property)



def test_remes_fromsubmodeedge_is_not_abstract():
    assert not inspect.isabstract(remes_FromSubModeEdge)


def test_remes_fromsubmodeedge_constructor_exists():
    assert callable(remes_FromSubModeEdge.__init__)


def test_remes_fromsubmodeedge_constructor_args():
    sig = inspect.signature(remes_FromSubModeEdge.__init__)
    params = list(sig.parameters.keys())



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



def test_remes_entryconditionaltopinitedge_is_not_abstract():
    assert not inspect.isabstract(remes_EntryConditionalTopInitEdge)


def test_remes_entryconditionaltopinitedge_constructor_exists():
    assert callable(remes_EntryConditionalTopInitEdge.__init__)


def test_remes_entryconditionaltopinitedge_constructor_args():
    sig = inspect.signature(remes_EntryConditionalTopInitEdge.__init__)
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



def test_remes_entryconditionaltopedge_is_not_abstract():
    assert not inspect.isabstract(remes_EntryConditionalTopEdge)


def test_remes_entryconditionaltopedge_constructor_exists():
    assert callable(remes_EntryConditionalTopEdge.__init__)


def test_remes_entryconditionaltopedge_constructor_args():
    sig = inspect.signature(remes_EntryConditionalTopEdge.__init__)
    params = list(sig.parameters.keys())



def test_remes_exitedge_is_not_abstract():
    assert not inspect.isabstract(remes_ExitEdge)


def test_remes_exitedge_constructor_exists():
    assert callable(remes_ExitEdge.__init__)


def test_remes_exitedge_constructor_args():
    sig = inspect.signature(remes_ExitEdge.__init__)
    params = list(sig.parameters.keys())



def test_remes_exitconditionalsubedge_is_not_abstract():
    assert not inspect.isabstract(remes_ExitConditionalSubEdge)


def test_remes_exitconditionalsubedge_constructor_exists():
    assert callable(remes_ExitConditionalSubEdge.__init__)


def test_remes_exitconditionalsubedge_constructor_args():
    sig = inspect.signature(remes_ExitConditionalSubEdge.__init__)
    params = list(sig.parameters.keys())



def test_tosubmodeedge_is_not_abstract():
    assert not inspect.isabstract(ToSubModeEdge)


def test_tosubmodeedge_constructor_exists():
    assert callable(ToSubModeEdge.__init__)


def test_tosubmodeedge_constructor_args():
    sig = inspect.signature(ToSubModeEdge.__init__)
    params = list(sig.parameters.keys())



def test_remes_entryinitedge_is_not_abstract():
    assert not inspect.isabstract(remes_EntryInitEdge)


def test_remes_entryinitedge_constructor_exists():
    assert callable(remes_EntryInitEdge.__init__)


def test_remes_entryinitedge_constructor_args():
    sig = inspect.signature(remes_EntryInitEdge.__init__)
    params = list(sig.parameters.keys())



def test_remes_internaledge_is_not_abstract():
    assert not inspect.isabstract(remes_InternalEdge)


def test_remes_internaledge_constructor_exists():
    assert callable(remes_InternalEdge.__init__)


def test_remes_internaledge_constructor_args():
    sig = inspect.signature(remes_InternalEdge.__init__)
    params = list(sig.parameters.keys())



def test_remes_entryedge_is_not_abstract():
    assert not inspect.isabstract(remes_EntryEdge)


def test_remes_entryedge_constructor_exists():
    assert callable(remes_EntryEdge.__init__)


def test_remes_entryedge_constructor_args():
    sig = inspect.signature(remes_EntryEdge.__init__)
    params = list(sig.parameters.keys())



def test_fromconditionalconnectoredge_is_not_abstract():
    assert not inspect.isabstract(FromConditionalConnectorEdge)


def test_fromconditionalconnectoredge_constructor_exists():
    assert callable(FromConditionalConnectorEdge.__init__)


def test_fromconditionalconnectoredge_constructor_args():
    sig = inspect.signature(FromConditionalConnectorEdge.__init__)
    params = list(sig.parameters.keys())



def test_remes_exitconditionaltopedge_is_not_abstract():
    assert not inspect.isabstract(remes_ExitConditionalTopEdge)


def test_remes_exitconditionaltopedge_constructor_exists():
    assert callable(remes_ExitConditionalTopEdge.__init__)


def test_remes_exitconditionaltopedge_constructor_args():
    sig = inspect.signature(remes_ExitConditionalTopEdge.__init__)
    params = list(sig.parameters.keys())



def test_remes_entryconditionalsubedge_is_not_abstract():
    assert not inspect.isabstract(remes_EntryConditionalSubEdge)


def test_remes_entryconditionalsubedge_constructor_exists():
    assert callable(remes_EntryConditionalSubEdge.__init__)


def test_remes_entryconditionalsubedge_constructor_args():
    sig = inspect.signature(remes_EntryConditionalSubEdge.__init__)
    params = list(sig.parameters.keys())



def test_remes_edge_is_not_abstract():
    assert not inspect.isabstract(remes_Edge)


def test_remes_edge_constructor_exists():
    assert callable(remes_Edge.__init__)


def test_remes_edge_constructor_args():
    sig = inspect.signature(remes_Edge.__init__)
    params = list(sig.parameters.keys())
    assert "actionGuard" in params, "Missing parameter 'actionGuard'"
    assert "actionBody" in params, "Missing parameter 'actionBody'"

def test_remes_edge_has_actionGuard():
    assert hasattr(remes_Edge, "actionGuard")
    descriptor = None
    for klass in remes_Edge.__mro__:
        if "actionGuard" in klass.__dict__:
            descriptor = klass.__dict__["actionGuard"]
            break
    assert isinstance(descriptor, property)

def test_remes_edge_has_actionBody():
    assert hasattr(remes_Edge, "actionBody")
    descriptor = None
    for klass in remes_Edge.__mro__:
        if "actionBody" in klass.__dict__:
            descriptor = klass.__dict__["actionBody"]
            break
    assert isinstance(descriptor, property)



def test_remes_fromconditionalconnectoredge_is_not_abstract():
    assert not inspect.isabstract(remes_FromConditionalConnectorEdge)


def test_remes_fromconditionalconnectoredge_constructor_exists():
    assert callable(remes_FromConditionalConnectorEdge.__init__)


def test_remes_fromconditionalconnectoredge_constructor_args():
    sig = inspect.signature(remes_FromConditionalConnectorEdge.__init__)
    params = list(sig.parameters.keys())



def test_remes_toconditionalconnectoredge_is_not_abstract():
    assert not inspect.isabstract(remes_ToConditionalConnectorEdge)


def test_remes_toconditionalconnectoredge_constructor_exists():
    assert callable(remes_ToConditionalConnectorEdge.__init__)


def test_remes_toconditionalconnectoredge_constructor_args():
    sig = inspect.signature(remes_ToConditionalConnectorEdge.__init__)
    params = list(sig.parameters.keys())



def test_remes_conditionalconnector_is_not_abstract():
    assert not inspect.isabstract(remes_ConditionalConnector)


def test_remes_conditionalconnector_constructor_exists():
    assert callable(remes_ConditionalConnector.__init__)


def test_remes_conditionalconnector_constructor_args():
    sig = inspect.signature(remes_ConditionalConnector.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_remes_conditionalconnector_has_name():
    assert hasattr(remes_ConditionalConnector, "name")
    descriptor = None
    for klass in remes_ConditionalConnector.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_remes_fromcompositemodeedge_is_not_abstract():
    assert not inspect.isabstract(remes_FromCompositeModeEdge)


def test_remes_fromcompositemodeedge_constructor_exists():
    assert callable(remes_FromCompositeModeEdge.__init__)


def test_remes_fromcompositemodeedge_constructor_args():
    sig = inspect.signature(remes_FromCompositeModeEdge.__init__)
    params = list(sig.parameters.keys())



def test_remes_fromcompositemodeinitedge_is_not_abstract():
    assert not inspect.isabstract(remes_FromCompositeModeInitEdge)


def test_remes_fromcompositemodeinitedge_constructor_exists():
    assert callable(remes_FromCompositeModeInitEdge.__init__)


def test_remes_fromcompositemodeinitedge_constructor_args():
    sig = inspect.signature(remes_FromCompositeModeInitEdge.__init__)
    params = list(sig.parameters.keys())



def test_remes_tocompositemodeedge_is_not_abstract():
    assert not inspect.isabstract(remes_ToCompositeModeEdge)


def test_remes_tocompositemodeedge_constructor_exists():
    assert callable(remes_ToCompositeModeEdge.__init__)


def test_remes_tocompositemodeedge_constructor_args():
    sig = inspect.signature(remes_ToCompositeModeEdge.__init__)
    params = list(sig.parameters.keys())



def test_mode_is_not_abstract():
    assert not inspect.isabstract(Mode)


def test_mode_constructor_exists():
    assert callable(Mode.__init__)


def test_mode_constructor_args():
    sig = inspect.signature(Mode.__init__)
    params = list(sig.parameters.keys())



def test_remes_submode_is_not_abstract():
    assert not inspect.isabstract(remes_SubMode)


def test_remes_submode_constructor_exists():
    assert callable(remes_SubMode.__init__)


def test_remes_submode_constructor_args():
    sig = inspect.signature(remes_SubMode.__init__)
    params = list(sig.parameters.keys())
    assert "invariant" in params, "Missing parameter 'invariant'"
    assert "isUrgent" in params, "Missing parameter 'isUrgent'"

def test_remes_submode_has_invariant():
    assert hasattr(remes_SubMode, "invariant")
    descriptor = None
    for klass in remes_SubMode.__mro__:
        if "invariant" in klass.__dict__:
            descriptor = klass.__dict__["invariant"]
            break
    assert isinstance(descriptor, property)

def test_remes_submode_has_isUrgent():
    assert hasattr(remes_SubMode, "isUrgent")
    descriptor = None
    for klass in remes_SubMode.__mro__:
        if "isUrgent" in klass.__dict__:
            descriptor = klass.__dict__["isUrgent"]
            break
    assert isinstance(descriptor, property)



def test_remes_compositemode_is_not_abstract():
    assert not inspect.isabstract(remes_CompositeMode)


def test_remes_compositemode_constructor_exists():
    assert callable(remes_CompositeMode.__init__)


def test_remes_compositemode_constructor_args():
    sig = inspect.signature(remes_CompositeMode.__init__)
    params = list(sig.parameters.keys())

def test_resourcetypes_exists():
    # Check that the Enumeration exists
    assert ResourceTypes is not None

def test_resourcetypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ResourceTypes]
    expected_literals = [
        "power",
        "port",
        "memory",
        "cpu",
        "bandwidth",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ResourceTypes"

def test_primitivetypes_exists():
    # Check that the Enumeration exists
    assert PrimitiveTypes is not None

def test_primitivetypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PrimitiveTypes]
    expected_literals = [
        "clock",
        "boolean",
        "natural",
        "integer",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PrimitiveTypes"


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
remes_Resource_strategy = st.builds(
    remes_Resource,
    expression=
        safe_text,
    type=
        safe_text
)
remes_ToSubModeEdge_strategy = st.builds(
    remes_ToSubModeEdge,
)
remes_RemesDiagram_strategy = st.builds(
    remes_RemesDiagram,
)
remes_Variable_strategy = st.builds(
    remes_Variable,
    type=
        safe_text,
    vectorSize=
        st.integers(),
    global_=
        st.booleans(),
    readable=
        st.booleans(),
    writable=
        st.booleans(),
    value=
        safe_text,
    name=
        safe_text
)
remes_Mode_strategy = st.builds(
    remes_Mode,
    name=
        safe_text,
    initialization=
        safe_text
)
remes_InitEdge_strategy = st.builds(
    remes_InitEdge,
    initialization=
        safe_text
)
remes_FromSubModeEdge_strategy = st.builds(
    remes_FromSubModeEdge,
)
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
remes_EntryConditionalTopInitEdge_strategy = st.builds(
    remes_EntryConditionalTopInitEdge,
)
FromCompositeModeEdge_strategy = st.builds(
    FromCompositeModeEdge,
)
Edge_strategy = st.builds(
    Edge,
)
remes_EntryConditionalTopEdge_strategy = st.builds(
    remes_EntryConditionalTopEdge,
)
remes_ExitEdge_strategy = st.builds(
    remes_ExitEdge,
)
remes_ExitConditionalSubEdge_strategy = st.builds(
    remes_ExitConditionalSubEdge,
)
ToSubModeEdge_strategy = st.builds(
    ToSubModeEdge,
)
remes_EntryInitEdge_strategy = st.builds(
    remes_EntryInitEdge,
)
remes_InternalEdge_strategy = st.builds(
    remes_InternalEdge,
)
remes_EntryEdge_strategy = st.builds(
    remes_EntryEdge,
)
FromConditionalConnectorEdge_strategy = st.builds(
    FromConditionalConnectorEdge,
)
remes_ExitConditionalTopEdge_strategy = st.builds(
    remes_ExitConditionalTopEdge,
)
remes_EntryConditionalSubEdge_strategy = st.builds(
    remes_EntryConditionalSubEdge,
)
remes_Edge_strategy = st.builds(
    remes_Edge,
    actionGuard=
        safe_text,
    actionBody=
        safe_text
)
remes_FromConditionalConnectorEdge_strategy = st.builds(
    remes_FromConditionalConnectorEdge,
)
remes_ToConditionalConnectorEdge_strategy = st.builds(
    remes_ToConditionalConnectorEdge,
)
remes_ConditionalConnector_strategy = st.builds(
    remes_ConditionalConnector,
    name=
        safe_text
)
remes_FromCompositeModeEdge_strategy = st.builds(
    remes_FromCompositeModeEdge,
)
remes_FromCompositeModeInitEdge_strategy = st.builds(
    remes_FromCompositeModeInitEdge,
)
remes_ToCompositeModeEdge_strategy = st.builds(
    remes_ToCompositeModeEdge,
)
Mode_strategy = st.builds(
    Mode,
)
remes_SubMode_strategy = st.builds(
    remes_SubMode,
    invariant=
        safe_text,
    isUrgent=
        st.booleans()
)
remes_CompositeMode_strategy = st.builds(
    remes_CompositeMode,
)

@given(instance=remes_Resource_strategy)
@settings(max_examples=50)
def test_remes_resource_instantiation(instance):
    assert isinstance(instance, remes_Resource)



@given(instance=remes_Resource_strategy)
def test_remes_resource_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original



@given(instance=remes_Resource_strategy)
def test_remes_resource_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=remes_ToSubModeEdge_strategy)
@settings(max_examples=50)
def test_remes_tosubmodeedge_instantiation(instance):
    assert isinstance(instance, remes_ToSubModeEdge)

@given(instance=remes_RemesDiagram_strategy)
@settings(max_examples=50)
def test_remes_remesdiagram_instantiation(instance):
    assert isinstance(instance, remes_RemesDiagram)

@given(instance=remes_Variable_strategy)
@settings(max_examples=50)
def test_remes_variable_instantiation(instance):
    assert isinstance(instance, remes_Variable)



@given(instance=remes_Variable_strategy)
def test_remes_variable_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=remes_Variable_strategy)
def test_remes_variable_vectorSize_setter(instance):
    original = instance.vectorSize
    instance.vectorSize = original
    assert instance.vectorSize == original



@given(instance=remes_Variable_strategy)
def test_remes_variable_global__setter(instance):
    original = instance.global_
    instance.global_ = original
    assert instance.global_ == original



@given(instance=remes_Variable_strategy)
def test_remes_variable_readable_setter(instance):
    original = instance.readable
    instance.readable = original
    assert instance.readable == original



@given(instance=remes_Variable_strategy)
def test_remes_variable_writable_setter(instance):
    original = instance.writable
    instance.writable = original
    assert instance.writable == original



@given(instance=remes_Variable_strategy)
def test_remes_variable_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=remes_Variable_strategy)
def test_remes_variable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=remes_Mode_strategy)
@settings(max_examples=50)
def test_remes_mode_instantiation(instance):
    assert isinstance(instance, remes_Mode)



@given(instance=remes_Mode_strategy)
def test_remes_mode_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=remes_Mode_strategy)
def test_remes_mode_initialization_setter(instance):
    original = instance.initialization
    instance.initialization = original
    assert instance.initialization == original

@given(instance=remes_InitEdge_strategy)
@settings(max_examples=50)
def test_remes_initedge_instantiation(instance):
    assert isinstance(instance, remes_InitEdge)



@given(instance=remes_InitEdge_strategy)
def test_remes_initedge_initialization_setter(instance):
    original = instance.initialization
    instance.initialization = original
    assert instance.initialization == original

@given(instance=remes_FromSubModeEdge_strategy)
@settings(max_examples=50)
def test_remes_fromsubmodeedge_instantiation(instance):
    assert isinstance(instance, remes_FromSubModeEdge)

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

@given(instance=remes_EntryConditionalTopInitEdge_strategy)
@settings(max_examples=50)
def test_remes_entryconditionaltopinitedge_instantiation(instance):
    assert isinstance(instance, remes_EntryConditionalTopInitEdge)

@given(instance=FromCompositeModeEdge_strategy)
@settings(max_examples=50)
def test_fromcompositemodeedge_instantiation(instance):
    assert isinstance(instance, FromCompositeModeEdge)

@given(instance=Edge_strategy)
@settings(max_examples=50)
def test_edge_instantiation(instance):
    assert isinstance(instance, Edge)

@given(instance=remes_EntryConditionalTopEdge_strategy)
@settings(max_examples=50)
def test_remes_entryconditionaltopedge_instantiation(instance):
    assert isinstance(instance, remes_EntryConditionalTopEdge)

@given(instance=remes_ExitEdge_strategy)
@settings(max_examples=50)
def test_remes_exitedge_instantiation(instance):
    assert isinstance(instance, remes_ExitEdge)

@given(instance=remes_ExitConditionalSubEdge_strategy)
@settings(max_examples=50)
def test_remes_exitconditionalsubedge_instantiation(instance):
    assert isinstance(instance, remes_ExitConditionalSubEdge)

@given(instance=ToSubModeEdge_strategy)
@settings(max_examples=50)
def test_tosubmodeedge_instantiation(instance):
    assert isinstance(instance, ToSubModeEdge)

@given(instance=remes_EntryInitEdge_strategy)
@settings(max_examples=50)
def test_remes_entryinitedge_instantiation(instance):
    assert isinstance(instance, remes_EntryInitEdge)

@given(instance=remes_InternalEdge_strategy)
@settings(max_examples=50)
def test_remes_internaledge_instantiation(instance):
    assert isinstance(instance, remes_InternalEdge)

@given(instance=remes_EntryEdge_strategy)
@settings(max_examples=50)
def test_remes_entryedge_instantiation(instance):
    assert isinstance(instance, remes_EntryEdge)

@given(instance=FromConditionalConnectorEdge_strategy)
@settings(max_examples=50)
def test_fromconditionalconnectoredge_instantiation(instance):
    assert isinstance(instance, FromConditionalConnectorEdge)

@given(instance=remes_ExitConditionalTopEdge_strategy)
@settings(max_examples=50)
def test_remes_exitconditionaltopedge_instantiation(instance):
    assert isinstance(instance, remes_ExitConditionalTopEdge)

@given(instance=remes_EntryConditionalSubEdge_strategy)
@settings(max_examples=50)
def test_remes_entryconditionalsubedge_instantiation(instance):
    assert isinstance(instance, remes_EntryConditionalSubEdge)

@given(instance=remes_Edge_strategy)
@settings(max_examples=50)
def test_remes_edge_instantiation(instance):
    assert isinstance(instance, remes_Edge)



@given(instance=remes_Edge_strategy)
def test_remes_edge_actionGuard_setter(instance):
    original = instance.actionGuard
    instance.actionGuard = original
    assert instance.actionGuard == original



@given(instance=remes_Edge_strategy)
def test_remes_edge_actionBody_setter(instance):
    original = instance.actionBody
    instance.actionBody = original
    assert instance.actionBody == original

@given(instance=remes_FromConditionalConnectorEdge_strategy)
@settings(max_examples=50)
def test_remes_fromconditionalconnectoredge_instantiation(instance):
    assert isinstance(instance, remes_FromConditionalConnectorEdge)

@given(instance=remes_ToConditionalConnectorEdge_strategy)
@settings(max_examples=50)
def test_remes_toconditionalconnectoredge_instantiation(instance):
    assert isinstance(instance, remes_ToConditionalConnectorEdge)

@given(instance=remes_ConditionalConnector_strategy)
@settings(max_examples=50)
def test_remes_conditionalconnector_instantiation(instance):
    assert isinstance(instance, remes_ConditionalConnector)



@given(instance=remes_ConditionalConnector_strategy)
def test_remes_conditionalconnector_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=remes_FromCompositeModeEdge_strategy)
@settings(max_examples=50)
def test_remes_fromcompositemodeedge_instantiation(instance):
    assert isinstance(instance, remes_FromCompositeModeEdge)

@given(instance=remes_FromCompositeModeInitEdge_strategy)
@settings(max_examples=50)
def test_remes_fromcompositemodeinitedge_instantiation(instance):
    assert isinstance(instance, remes_FromCompositeModeInitEdge)

@given(instance=remes_ToCompositeModeEdge_strategy)
@settings(max_examples=50)
def test_remes_tocompositemodeedge_instantiation(instance):
    assert isinstance(instance, remes_ToCompositeModeEdge)

@given(instance=Mode_strategy)
@settings(max_examples=50)
def test_mode_instantiation(instance):
    assert isinstance(instance, Mode)

@given(instance=remes_SubMode_strategy)
@settings(max_examples=50)
def test_remes_submode_instantiation(instance):
    assert isinstance(instance, remes_SubMode)



@given(instance=remes_SubMode_strategy)
def test_remes_submode_invariant_setter(instance):
    original = instance.invariant
    instance.invariant = original
    assert instance.invariant == original



@given(instance=remes_SubMode_strategy)
def test_remes_submode_isUrgent_setter(instance):
    original = instance.isUrgent
    instance.isUrgent = original
    assert instance.isUrgent == original

@given(instance=remes_CompositeMode_strategy)
@settings(max_examples=50)
def test_remes_compositemode_instantiation(instance):
    assert isinstance(instance, remes_CompositeMode)
