import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    graph::GAlignable,
    graph::GIssue,
    GAlignable,
    graph::GLayouting,
    graph::GEdgePlacement,
    graph::GEdgeLayoutable,
    graph::GDimension,
    graph::GBoundsAware,
    graph::GModelElement,
    graph::GPoint,
    GLayouting,
    GEdgeLayoutable,
    GShapeElement,
    graph::GPort,
    graph::GIssueMarker,
    graph::GLabel,
    graph::GCompartment,
    graph::GButton,
    graph::GNode,
    graph::GBounds,
    graph::StringToObjectMapEntry,
    GModelRoot,
    graph::GHtmlRoot,
    GBoundsAware,
    graph::GGraph,
    GModelElement,
    graph::GPreRenderedElement,
    graph::GEdge,
    graph::GModelRoot,
    graph::GShapeElement,
    GSeverity,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_graph::galignable_is_not_abstract():
    assert not inspect.isabstract(graph::GAlignable)


def test_graph::galignable_constructor_exists():
    assert callable(graph::GAlignable.__init__)


def test_graph::galignable_constructor_args():
    sig = inspect.signature(graph::GAlignable.__init__)
    params = list(sig.parameters.keys())



def test_graph::gissue_is_not_abstract():
    assert not inspect.isabstract(graph::GIssue)


def test_graph::gissue_constructor_exists():
    assert callable(graph::GIssue.__init__)


def test_graph::gissue_constructor_args():
    sig = inspect.signature(graph::GIssue.__init__)
    params = list(sig.parameters.keys())
    assert "severity" in params, "Missing parameter 'severity'"
    assert "message" in params, "Missing parameter 'message'"

def test_graph::gissue_has_severity():
    assert hasattr(graph::GIssue, "severity")
    descriptor = None
    for klass in graph::GIssue.__mro__:
        if "severity" in klass.__dict__:
            descriptor = klass.__dict__["severity"]
            break
    assert isinstance(descriptor, property)

def test_graph::gissue_has_message():
    assert hasattr(graph::GIssue, "message")
    descriptor = None
    for klass in graph::GIssue.__mro__:
        if "message" in klass.__dict__:
            descriptor = klass.__dict__["message"]
            break
    assert isinstance(descriptor, property)



def test_galignable_is_not_abstract():
    assert not inspect.isabstract(GAlignable)


def test_galignable_constructor_exists():
    assert callable(GAlignable.__init__)


def test_galignable_constructor_args():
    sig = inspect.signature(GAlignable.__init__)
    params = list(sig.parameters.keys())



def test_graph::glayouting_is_not_abstract():
    assert not inspect.isabstract(graph::GLayouting)


def test_graph::glayouting_constructor_exists():
    assert callable(graph::GLayouting.__init__)


def test_graph::glayouting_constructor_args():
    sig = inspect.signature(graph::GLayouting.__init__)
    params = list(sig.parameters.keys())
    assert "layout" in params, "Missing parameter 'layout'"

def test_graph::glayouting_has_layout():
    assert hasattr(graph::GLayouting, "layout")
    descriptor = None
    for klass in graph::GLayouting.__mro__:
        if "layout" in klass.__dict__:
            descriptor = klass.__dict__["layout"]
            break
    assert isinstance(descriptor, property)



def test_graph::gedgeplacement_is_not_abstract():
    assert not inspect.isabstract(graph::GEdgePlacement)


def test_graph::gedgeplacement_constructor_exists():
    assert callable(graph::GEdgePlacement.__init__)


def test_graph::gedgeplacement_constructor_args():
    sig = inspect.signature(graph::GEdgePlacement.__init__)
    params = list(sig.parameters.keys())
    assert "position" in params, "Missing parameter 'position'"
    assert "side" in params, "Missing parameter 'side'"
    assert "rotate" in params, "Missing parameter 'rotate'"
    assert "offset" in params, "Missing parameter 'offset'"

def test_graph::gedgeplacement_has_position():
    assert hasattr(graph::GEdgePlacement, "position")
    descriptor = None
    for klass in graph::GEdgePlacement.__mro__:
        if "position" in klass.__dict__:
            descriptor = klass.__dict__["position"]
            break
    assert isinstance(descriptor, property)

def test_graph::gedgeplacement_has_side():
    assert hasattr(graph::GEdgePlacement, "side")
    descriptor = None
    for klass in graph::GEdgePlacement.__mro__:
        if "side" in klass.__dict__:
            descriptor = klass.__dict__["side"]
            break
    assert isinstance(descriptor, property)

def test_graph::gedgeplacement_has_rotate():
    assert hasattr(graph::GEdgePlacement, "rotate")
    descriptor = None
    for klass in graph::GEdgePlacement.__mro__:
        if "rotate" in klass.__dict__:
            descriptor = klass.__dict__["rotate"]
            break
    assert isinstance(descriptor, property)

def test_graph::gedgeplacement_has_offset():
    assert hasattr(graph::GEdgePlacement, "offset")
    descriptor = None
    for klass in graph::GEdgePlacement.__mro__:
        if "offset" in klass.__dict__:
            descriptor = klass.__dict__["offset"]
            break
    assert isinstance(descriptor, property)



def test_graph::gedgelayoutable_is_not_abstract():
    assert not inspect.isabstract(graph::GEdgeLayoutable)


def test_graph::gedgelayoutable_constructor_exists():
    assert callable(graph::GEdgeLayoutable.__init__)


def test_graph::gedgelayoutable_constructor_args():
    sig = inspect.signature(graph::GEdgeLayoutable.__init__)
    params = list(sig.parameters.keys())



def test_graph::gdimension_is_not_abstract():
    assert not inspect.isabstract(graph::GDimension)


def test_graph::gdimension_constructor_exists():
    assert callable(graph::GDimension.__init__)


def test_graph::gdimension_constructor_args():
    sig = inspect.signature(graph::GDimension.__init__)
    params = list(sig.parameters.keys())
    assert "height" in params, "Missing parameter 'height'"
    assert "width" in params, "Missing parameter 'width'"

def test_graph::gdimension_has_height():
    assert hasattr(graph::GDimension, "height")
    descriptor = None
    for klass in graph::GDimension.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)

def test_graph::gdimension_has_width():
    assert hasattr(graph::GDimension, "width")
    descriptor = None
    for klass in graph::GDimension.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)



def test_graph::gboundsaware_is_not_abstract():
    assert not inspect.isabstract(graph::GBoundsAware)


def test_graph::gboundsaware_constructor_exists():
    assert callable(graph::GBoundsAware.__init__)


def test_graph::gboundsaware_constructor_args():
    sig = inspect.signature(graph::GBoundsAware.__init__)
    params = list(sig.parameters.keys())



def test_graph::gmodelelement_is_not_abstract():
    assert not inspect.isabstract(graph::GModelElement)


def test_graph::gmodelelement_constructor_exists():
    assert callable(graph::GModelElement.__init__)


def test_graph::gmodelelement_constructor_args():
    sig = inspect.signature(graph::GModelElement.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "cssClasses" in params, "Missing parameter 'cssClasses'"
    assert "trace" in params, "Missing parameter 'trace'"
    assert "id" in params, "Missing parameter 'id'"

def test_graph::gmodelelement_has_type():
    assert hasattr(graph::GModelElement, "type")
    descriptor = None
    for klass in graph::GModelElement.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_graph::gmodelelement_has_cssClasses():
    assert hasattr(graph::GModelElement, "cssClasses")
    descriptor = None
    for klass in graph::GModelElement.__mro__:
        if "cssClasses" in klass.__dict__:
            descriptor = klass.__dict__["cssClasses"]
            break
    assert isinstance(descriptor, property)

def test_graph::gmodelelement_has_trace():
    assert hasattr(graph::GModelElement, "trace")
    descriptor = None
    for klass in graph::GModelElement.__mro__:
        if "trace" in klass.__dict__:
            descriptor = klass.__dict__["trace"]
            break
    assert isinstance(descriptor, property)

def test_graph::gmodelelement_has_id():
    assert hasattr(graph::GModelElement, "id")
    descriptor = None
    for klass in graph::GModelElement.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_graph::gpoint_is_not_abstract():
    assert not inspect.isabstract(graph::GPoint)


def test_graph::gpoint_constructor_exists():
    assert callable(graph::GPoint.__init__)


def test_graph::gpoint_constructor_args():
    sig = inspect.signature(graph::GPoint.__init__)
    params = list(sig.parameters.keys())
    assert "y" in params, "Missing parameter 'y'"
    assert "x" in params, "Missing parameter 'x'"

def test_graph::gpoint_has_y():
    assert hasattr(graph::GPoint, "y")
    descriptor = None
    for klass in graph::GPoint.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_graph::gpoint_has_x():
    assert hasattr(graph::GPoint, "x")
    descriptor = None
    for klass in graph::GPoint.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)



def test_glayouting_is_not_abstract():
    assert not inspect.isabstract(GLayouting)


def test_glayouting_constructor_exists():
    assert callable(GLayouting.__init__)


def test_glayouting_constructor_args():
    sig = inspect.signature(GLayouting.__init__)
    params = list(sig.parameters.keys())



def test_gedgelayoutable_is_not_abstract():
    assert not inspect.isabstract(GEdgeLayoutable)


def test_gedgelayoutable_constructor_exists():
    assert callable(GEdgeLayoutable.__init__)


def test_gedgelayoutable_constructor_args():
    sig = inspect.signature(GEdgeLayoutable.__init__)
    params = list(sig.parameters.keys())



def test_gshapeelement_is_not_abstract():
    assert not inspect.isabstract(GShapeElement)


def test_gshapeelement_constructor_exists():
    assert callable(GShapeElement.__init__)


def test_gshapeelement_constructor_args():
    sig = inspect.signature(GShapeElement.__init__)
    params = list(sig.parameters.keys())



def test_graph::gport_is_not_abstract():
    assert not inspect.isabstract(graph::GPort)


def test_graph::gport_constructor_exists():
    assert callable(graph::GPort.__init__)


def test_graph::gport_constructor_args():
    sig = inspect.signature(graph::GPort.__init__)
    params = list(sig.parameters.keys())



def test_graph::gissuemarker_is_not_abstract():
    assert not inspect.isabstract(graph::GIssueMarker)


def test_graph::gissuemarker_constructor_exists():
    assert callable(graph::GIssueMarker.__init__)


def test_graph::gissuemarker_constructor_args():
    sig = inspect.signature(graph::GIssueMarker.__init__)
    params = list(sig.parameters.keys())



def test_graph::glabel_is_not_abstract():
    assert not inspect.isabstract(graph::GLabel)


def test_graph::glabel_constructor_exists():
    assert callable(graph::GLabel.__init__)


def test_graph::glabel_constructor_args():
    sig = inspect.signature(graph::GLabel.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_graph::glabel_has_text():
    assert hasattr(graph::GLabel, "text")
    descriptor = None
    for klass in graph::GLabel.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_graph::gcompartment_is_not_abstract():
    assert not inspect.isabstract(graph::GCompartment)


def test_graph::gcompartment_constructor_exists():
    assert callable(graph::GCompartment.__init__)


def test_graph::gcompartment_constructor_args():
    sig = inspect.signature(graph::GCompartment.__init__)
    params = list(sig.parameters.keys())



def test_graph::gbutton_is_not_abstract():
    assert not inspect.isabstract(graph::GButton)


def test_graph::gbutton_constructor_exists():
    assert callable(graph::GButton.__init__)


def test_graph::gbutton_constructor_args():
    sig = inspect.signature(graph::GButton.__init__)
    params = list(sig.parameters.keys())
    assert "enabled" in params, "Missing parameter 'enabled'"

def test_graph::gbutton_has_enabled():
    assert hasattr(graph::GButton, "enabled")
    descriptor = None
    for klass in graph::GButton.__mro__:
        if "enabled" in klass.__dict__:
            descriptor = klass.__dict__["enabled"]
            break
    assert isinstance(descriptor, property)



def test_graph::gnode_is_not_abstract():
    assert not inspect.isabstract(graph::GNode)


def test_graph::gnode_constructor_exists():
    assert callable(graph::GNode.__init__)


def test_graph::gnode_constructor_args():
    sig = inspect.signature(graph::GNode.__init__)
    params = list(sig.parameters.keys())



def test_graph::gbounds_is_not_abstract():
    assert not inspect.isabstract(graph::GBounds)


def test_graph::gbounds_constructor_exists():
    assert callable(graph::GBounds.__init__)


def test_graph::gbounds_constructor_args():
    sig = inspect.signature(graph::GBounds.__init__)
    params = list(sig.parameters.keys())
    assert "y" in params, "Missing parameter 'y'"
    assert "width" in params, "Missing parameter 'width'"
    assert "height" in params, "Missing parameter 'height'"
    assert "x" in params, "Missing parameter 'x'"

def test_graph::gbounds_has_y():
    assert hasattr(graph::GBounds, "y")
    descriptor = None
    for klass in graph::GBounds.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_graph::gbounds_has_width():
    assert hasattr(graph::GBounds, "width")
    descriptor = None
    for klass in graph::GBounds.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_graph::gbounds_has_height():
    assert hasattr(graph::GBounds, "height")
    descriptor = None
    for klass in graph::GBounds.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)

def test_graph::gbounds_has_x():
    assert hasattr(graph::GBounds, "x")
    descriptor = None
    for klass in graph::GBounds.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)



def test_graph::stringtoobjectmapentry_is_not_abstract():
    assert not inspect.isabstract(graph::StringToObjectMapEntry)


def test_graph::stringtoobjectmapentry_constructor_exists():
    assert callable(graph::StringToObjectMapEntry.__init__)


def test_graph::stringtoobjectmapentry_constructor_args():
    sig = inspect.signature(graph::StringToObjectMapEntry.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"
    assert "value" in params, "Missing parameter 'value'"

def test_graph::stringtoobjectmapentry_has_key():
    assert hasattr(graph::StringToObjectMapEntry, "key")
    descriptor = None
    for klass in graph::StringToObjectMapEntry.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_graph::stringtoobjectmapentry_has_value():
    assert hasattr(graph::StringToObjectMapEntry, "value")
    descriptor = None
    for klass in graph::StringToObjectMapEntry.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_gmodelroot_is_not_abstract():
    assert not inspect.isabstract(GModelRoot)


def test_gmodelroot_constructor_exists():
    assert callable(GModelRoot.__init__)


def test_gmodelroot_constructor_args():
    sig = inspect.signature(GModelRoot.__init__)
    params = list(sig.parameters.keys())



def test_graph::ghtmlroot_is_not_abstract():
    assert not inspect.isabstract(graph::GHtmlRoot)


def test_graph::ghtmlroot_constructor_exists():
    assert callable(graph::GHtmlRoot.__init__)


def test_graph::ghtmlroot_constructor_args():
    sig = inspect.signature(graph::GHtmlRoot.__init__)
    params = list(sig.parameters.keys())
    assert "classes" in params, "Missing parameter 'classes'"

def test_graph::ghtmlroot_has_classes():
    assert hasattr(graph::GHtmlRoot, "classes")
    descriptor = None
    for klass in graph::GHtmlRoot.__mro__:
        if "classes" in klass.__dict__:
            descriptor = klass.__dict__["classes"]
            break
    assert isinstance(descriptor, property)



def test_gboundsaware_is_not_abstract():
    assert not inspect.isabstract(GBoundsAware)


def test_gboundsaware_constructor_exists():
    assert callable(GBoundsAware.__init__)


def test_gboundsaware_constructor_args():
    sig = inspect.signature(GBoundsAware.__init__)
    params = list(sig.parameters.keys())



def test_graph::ggraph_is_not_abstract():
    assert not inspect.isabstract(graph::GGraph)


def test_graph::ggraph_constructor_exists():
    assert callable(graph::GGraph.__init__)


def test_graph::ggraph_constructor_args():
    sig = inspect.signature(graph::GGraph.__init__)
    params = list(sig.parameters.keys())



def test_gmodelelement_is_not_abstract():
    assert not inspect.isabstract(GModelElement)


def test_gmodelelement_constructor_exists():
    assert callable(GModelElement.__init__)


def test_gmodelelement_constructor_args():
    sig = inspect.signature(GModelElement.__init__)
    params = list(sig.parameters.keys())



def test_graph::gprerenderedelement_is_not_abstract():
    assert not inspect.isabstract(graph::GPreRenderedElement)


def test_graph::gprerenderedelement_constructor_exists():
    assert callable(graph::GPreRenderedElement.__init__)


def test_graph::gprerenderedelement_constructor_args():
    sig = inspect.signature(graph::GPreRenderedElement.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"

def test_graph::gprerenderedelement_has_code():
    assert hasattr(graph::GPreRenderedElement, "code")
    descriptor = None
    for klass in graph::GPreRenderedElement.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)



def test_graph::gedge_is_not_abstract():
    assert not inspect.isabstract(graph::GEdge)


def test_graph::gedge_constructor_exists():
    assert callable(graph::GEdge.__init__)


def test_graph::gedge_constructor_args():
    sig = inspect.signature(graph::GEdge.__init__)
    params = list(sig.parameters.keys())
    assert "targetId" in params, "Missing parameter 'targetId'"
    assert "sourceId" in params, "Missing parameter 'sourceId'"
    assert "routerKind" in params, "Missing parameter 'routerKind'"

def test_graph::gedge_has_targetId():
    assert hasattr(graph::GEdge, "targetId")
    descriptor = None
    for klass in graph::GEdge.__mro__:
        if "targetId" in klass.__dict__:
            descriptor = klass.__dict__["targetId"]
            break
    assert isinstance(descriptor, property)

def test_graph::gedge_has_sourceId():
    assert hasattr(graph::GEdge, "sourceId")
    descriptor = None
    for klass in graph::GEdge.__mro__:
        if "sourceId" in klass.__dict__:
            descriptor = klass.__dict__["sourceId"]
            break
    assert isinstance(descriptor, property)

def test_graph::gedge_has_routerKind():
    assert hasattr(graph::GEdge, "routerKind")
    descriptor = None
    for klass in graph::GEdge.__mro__:
        if "routerKind" in klass.__dict__:
            descriptor = klass.__dict__["routerKind"]
            break
    assert isinstance(descriptor, property)



def test_graph::gmodelroot_is_not_abstract():
    assert not inspect.isabstract(graph::GModelRoot)


def test_graph::gmodelroot_constructor_exists():
    assert callable(graph::GModelRoot.__init__)


def test_graph::gmodelroot_constructor_args():
    sig = inspect.signature(graph::GModelRoot.__init__)
    params = list(sig.parameters.keys())
    assert "revision" in params, "Missing parameter 'revision'"

def test_graph::gmodelroot_has_revision():
    assert hasattr(graph::GModelRoot, "revision")
    descriptor = None
    for klass in graph::GModelRoot.__mro__:
        if "revision" in klass.__dict__:
            descriptor = klass.__dict__["revision"]
            break
    assert isinstance(descriptor, property)



def test_graph::gshapeelement_is_not_abstract():
    assert not inspect.isabstract(graph::GShapeElement)


def test_graph::gshapeelement_constructor_exists():
    assert callable(graph::GShapeElement.__init__)


def test_graph::gshapeelement_constructor_args():
    sig = inspect.signature(graph::GShapeElement.__init__)
    params = list(sig.parameters.keys())

def test_gseverity_exists():
    # Check that the Enumeration exists
    assert GSeverity is not None

def test_gseverity_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in GSeverity]
    expected_literals = [
        "warning",
        "info",
        "error",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in GSeverity"


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
graph::GAlignable_strategy = st.builds(
    graph::GAlignable,
)
graph::GIssue_strategy = st.builds(
    graph::GIssue,
    severity=
        safe_text,
    message=
        safe_text
)
GAlignable_strategy = st.builds(
    GAlignable,
)
graph::GLayouting_strategy = st.builds(
    graph::GLayouting,
    layout=
        safe_text
)
graph::GEdgePlacement_strategy = st.builds(
    graph::GEdgePlacement,
    position=
        safe_text,
    side=
        safe_text,
    rotate=
        st.booleans(),
    offset=
        safe_text
)
graph::GEdgeLayoutable_strategy = st.builds(
    graph::GEdgeLayoutable,
)
graph::GDimension_strategy = st.builds(
    graph::GDimension,
    height=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    width=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
graph::GBoundsAware_strategy = st.builds(
    graph::GBoundsAware,
)
graph::GModelElement_strategy = st.builds(
    graph::GModelElement,
    type=
        safe_text,
    cssClasses=
        safe_text,
    trace=
        safe_text,
    id=
        safe_text
)
graph::GPoint_strategy = st.builds(
    graph::GPoint,
    y=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    x=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
GLayouting_strategy = st.builds(
    GLayouting,
)
GEdgeLayoutable_strategy = st.builds(
    GEdgeLayoutable,
)
GShapeElement_strategy = st.builds(
    GShapeElement,
)
graph::GPort_strategy = st.builds(
    graph::GPort,
)
graph::GIssueMarker_strategy = st.builds(
    graph::GIssueMarker,
)
graph::GLabel_strategy = st.builds(
    graph::GLabel,
    text=
        safe_text
)
graph::GCompartment_strategy = st.builds(
    graph::GCompartment,
)
graph::GButton_strategy = st.builds(
    graph::GButton,
    enabled=
        st.booleans()
)
graph::GNode_strategy = st.builds(
    graph::GNode,
)
graph::GBounds_strategy = st.builds(
    graph::GBounds,
    y=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    width=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    height=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    x=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
graph::StringToObjectMapEntry_strategy = st.builds(
    graph::StringToObjectMapEntry,
    key=
        safe_text,
    value=
        safe_text
)
GModelRoot_strategy = st.builds(
    GModelRoot,
)
graph::GHtmlRoot_strategy = st.builds(
    graph::GHtmlRoot,
    classes=
        safe_text
)
GBoundsAware_strategy = st.builds(
    GBoundsAware,
)
graph::GGraph_strategy = st.builds(
    graph::GGraph,
)
GModelElement_strategy = st.builds(
    GModelElement,
)
graph::GPreRenderedElement_strategy = st.builds(
    graph::GPreRenderedElement,
    code=
        safe_text
)
graph::GEdge_strategy = st.builds(
    graph::GEdge,
    targetId=
        safe_text,
    sourceId=
        safe_text,
    routerKind=
        safe_text
)
graph::GModelRoot_strategy = st.builds(
    graph::GModelRoot,
    revision=
        st.integers()
)
graph::GShapeElement_strategy = st.builds(
    graph::GShapeElement,
)

@given(instance=graph::GAlignable_strategy)
@settings(max_examples=50)
def test_graph::galignable_instantiation(instance):
    assert isinstance(instance, graph::GAlignable)

@given(instance=graph::GIssue_strategy)
@settings(max_examples=50)
def test_graph::gissue_instantiation(instance):
    assert isinstance(instance, graph::GIssue)

@given(instance=graph::GIssue_strategy)
def test_graph::gissue_severity_type(instance):
    assert isinstance(instance.severity, str)


@given(instance=graph::GIssue_strategy)
def test_graph::gissue_severity_setter(instance):
    original = instance.severity
    instance.severity = original
    assert instance.severity == original

@given(instance=graph::GIssue_strategy)
def test_graph::gissue_message_type(instance):
    assert isinstance(instance.message, str)


@given(instance=graph::GIssue_strategy)
def test_graph::gissue_message_setter(instance):
    original = instance.message
    instance.message = original
    assert instance.message == original

@given(instance=GAlignable_strategy)
@settings(max_examples=50)
def test_galignable_instantiation(instance):
    assert isinstance(instance, GAlignable)

@given(instance=graph::GLayouting_strategy)
@settings(max_examples=50)
def test_graph::glayouting_instantiation(instance):
    assert isinstance(instance, graph::GLayouting)

@given(instance=graph::GLayouting_strategy)
def test_graph::glayouting_layout_type(instance):
    assert isinstance(instance.layout, str)


@given(instance=graph::GLayouting_strategy)
def test_graph::glayouting_layout_setter(instance):
    original = instance.layout
    instance.layout = original
    assert instance.layout == original

@given(instance=graph::GEdgePlacement_strategy)
@settings(max_examples=50)
def test_graph::gedgeplacement_instantiation(instance):
    assert isinstance(instance, graph::GEdgePlacement)

@given(instance=graph::GEdgePlacement_strategy)
def test_graph::gedgeplacement_position_type(instance):
    assert isinstance(instance.position, str)


@given(instance=graph::GEdgePlacement_strategy)
def test_graph::gedgeplacement_position_setter(instance):
    original = instance.position
    instance.position = original
    assert instance.position == original

@given(instance=graph::GEdgePlacement_strategy)
def test_graph::gedgeplacement_side_type(instance):
    assert isinstance(instance.side, str)


@given(instance=graph::GEdgePlacement_strategy)
def test_graph::gedgeplacement_side_setter(instance):
    original = instance.side
    instance.side = original
    assert instance.side == original

@given(instance=graph::GEdgePlacement_strategy)
def test_graph::gedgeplacement_rotate_type(instance):
    assert isinstance(instance.rotate, bool)


@given(instance=graph::GEdgePlacement_strategy)
def test_graph::gedgeplacement_rotate_setter(instance):
    original = instance.rotate
    instance.rotate = original
    assert instance.rotate == original

@given(instance=graph::GEdgePlacement_strategy)
def test_graph::gedgeplacement_offset_type(instance):
    assert isinstance(instance.offset, str)


@given(instance=graph::GEdgePlacement_strategy)
def test_graph::gedgeplacement_offset_setter(instance):
    original = instance.offset
    instance.offset = original
    assert instance.offset == original

@given(instance=graph::GEdgeLayoutable_strategy)
@settings(max_examples=50)
def test_graph::gedgelayoutable_instantiation(instance):
    assert isinstance(instance, graph::GEdgeLayoutable)

@given(instance=graph::GDimension_strategy)
@settings(max_examples=50)
def test_graph::gdimension_instantiation(instance):
    assert isinstance(instance, graph::GDimension)

@given(instance=graph::GDimension_strategy)
def test_graph::gdimension_height_type(instance):
    assert isinstance(instance.height, float)


@given(instance=graph::GDimension_strategy)
def test_graph::gdimension_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original

@given(instance=graph::GDimension_strategy)
def test_graph::gdimension_width_type(instance):
    assert isinstance(instance.width, float)


@given(instance=graph::GDimension_strategy)
def test_graph::gdimension_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=graph::GBoundsAware_strategy)
@settings(max_examples=50)
def test_graph::gboundsaware_instantiation(instance):
    assert isinstance(instance, graph::GBoundsAware)

@given(instance=graph::GModelElement_strategy)
@settings(max_examples=50)
def test_graph::gmodelelement_instantiation(instance):
    assert isinstance(instance, graph::GModelElement)

@given(instance=graph::GModelElement_strategy)
def test_graph::gmodelelement_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=graph::GModelElement_strategy)
def test_graph::gmodelelement_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=graph::GModelElement_strategy)
def test_graph::gmodelelement_cssClasses_type(instance):
    assert isinstance(instance.cssClasses, str)


@given(instance=graph::GModelElement_strategy)
def test_graph::gmodelelement_cssClasses_setter(instance):
    original = instance.cssClasses
    instance.cssClasses = original
    assert instance.cssClasses == original

@given(instance=graph::GModelElement_strategy)
def test_graph::gmodelelement_trace_type(instance):
    assert isinstance(instance.trace, str)


@given(instance=graph::GModelElement_strategy)
def test_graph::gmodelelement_trace_setter(instance):
    original = instance.trace
    instance.trace = original
    assert instance.trace == original

@given(instance=graph::GModelElement_strategy)
def test_graph::gmodelelement_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=graph::GModelElement_strategy)
def test_graph::gmodelelement_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=graph::GPoint_strategy)
@settings(max_examples=50)
def test_graph::gpoint_instantiation(instance):
    assert isinstance(instance, graph::GPoint)

@given(instance=graph::GPoint_strategy)
def test_graph::gpoint_y_type(instance):
    assert isinstance(instance.y, float)


@given(instance=graph::GPoint_strategy)
def test_graph::gpoint_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=graph::GPoint_strategy)
def test_graph::gpoint_x_type(instance):
    assert isinstance(instance.x, float)


@given(instance=graph::GPoint_strategy)
def test_graph::gpoint_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=GLayouting_strategy)
@settings(max_examples=50)
def test_glayouting_instantiation(instance):
    assert isinstance(instance, GLayouting)

@given(instance=GEdgeLayoutable_strategy)
@settings(max_examples=50)
def test_gedgelayoutable_instantiation(instance):
    assert isinstance(instance, GEdgeLayoutable)

@given(instance=GShapeElement_strategy)
@settings(max_examples=50)
def test_gshapeelement_instantiation(instance):
    assert isinstance(instance, GShapeElement)

@given(instance=graph::GPort_strategy)
@settings(max_examples=50)
def test_graph::gport_instantiation(instance):
    assert isinstance(instance, graph::GPort)

@given(instance=graph::GIssueMarker_strategy)
@settings(max_examples=50)
def test_graph::gissuemarker_instantiation(instance):
    assert isinstance(instance, graph::GIssueMarker)

@given(instance=graph::GLabel_strategy)
@settings(max_examples=50)
def test_graph::glabel_instantiation(instance):
    assert isinstance(instance, graph::GLabel)

@given(instance=graph::GLabel_strategy)
def test_graph::glabel_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=graph::GLabel_strategy)
def test_graph::glabel_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=graph::GCompartment_strategy)
@settings(max_examples=50)
def test_graph::gcompartment_instantiation(instance):
    assert isinstance(instance, graph::GCompartment)

@given(instance=graph::GButton_strategy)
@settings(max_examples=50)
def test_graph::gbutton_instantiation(instance):
    assert isinstance(instance, graph::GButton)

@given(instance=graph::GButton_strategy)
def test_graph::gbutton_enabled_type(instance):
    assert isinstance(instance.enabled, bool)


@given(instance=graph::GButton_strategy)
def test_graph::gbutton_enabled_setter(instance):
    original = instance.enabled
    instance.enabled = original
    assert instance.enabled == original

@given(instance=graph::GNode_strategy)
@settings(max_examples=50)
def test_graph::gnode_instantiation(instance):
    assert isinstance(instance, graph::GNode)

@given(instance=graph::GBounds_strategy)
@settings(max_examples=50)
def test_graph::gbounds_instantiation(instance):
    assert isinstance(instance, graph::GBounds)

@given(instance=graph::GBounds_strategy)
def test_graph::gbounds_y_type(instance):
    assert isinstance(instance.y, float)


@given(instance=graph::GBounds_strategy)
def test_graph::gbounds_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=graph::GBounds_strategy)
def test_graph::gbounds_width_type(instance):
    assert isinstance(instance.width, float)


@given(instance=graph::GBounds_strategy)
def test_graph::gbounds_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=graph::GBounds_strategy)
def test_graph::gbounds_height_type(instance):
    assert isinstance(instance.height, float)


@given(instance=graph::GBounds_strategy)
def test_graph::gbounds_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original

@given(instance=graph::GBounds_strategy)
def test_graph::gbounds_x_type(instance):
    assert isinstance(instance.x, float)


@given(instance=graph::GBounds_strategy)
def test_graph::gbounds_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=graph::StringToObjectMapEntry_strategy)
@settings(max_examples=50)
def test_graph::stringtoobjectmapentry_instantiation(instance):
    assert isinstance(instance, graph::StringToObjectMapEntry)

@given(instance=graph::StringToObjectMapEntry_strategy)
def test_graph::stringtoobjectmapentry_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=graph::StringToObjectMapEntry_strategy)
def test_graph::stringtoobjectmapentry_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=graph::StringToObjectMapEntry_strategy)
def test_graph::stringtoobjectmapentry_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=graph::StringToObjectMapEntry_strategy)
def test_graph::stringtoobjectmapentry_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=GModelRoot_strategy)
@settings(max_examples=50)
def test_gmodelroot_instantiation(instance):
    assert isinstance(instance, GModelRoot)

@given(instance=graph::GHtmlRoot_strategy)
@settings(max_examples=50)
def test_graph::ghtmlroot_instantiation(instance):
    assert isinstance(instance, graph::GHtmlRoot)

@given(instance=graph::GHtmlRoot_strategy)
def test_graph::ghtmlroot_classes_type(instance):
    assert isinstance(instance.classes, str)


@given(instance=graph::GHtmlRoot_strategy)
def test_graph::ghtmlroot_classes_setter(instance):
    original = instance.classes
    instance.classes = original
    assert instance.classes == original

@given(instance=GBoundsAware_strategy)
@settings(max_examples=50)
def test_gboundsaware_instantiation(instance):
    assert isinstance(instance, GBoundsAware)

@given(instance=graph::GGraph_strategy)
@settings(max_examples=50)
def test_graph::ggraph_instantiation(instance):
    assert isinstance(instance, graph::GGraph)

@given(instance=GModelElement_strategy)
@settings(max_examples=50)
def test_gmodelelement_instantiation(instance):
    assert isinstance(instance, GModelElement)

@given(instance=graph::GPreRenderedElement_strategy)
@settings(max_examples=50)
def test_graph::gprerenderedelement_instantiation(instance):
    assert isinstance(instance, graph::GPreRenderedElement)

@given(instance=graph::GPreRenderedElement_strategy)
def test_graph::gprerenderedelement_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=graph::GPreRenderedElement_strategy)
def test_graph::gprerenderedelement_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=graph::GEdge_strategy)
@settings(max_examples=50)
def test_graph::gedge_instantiation(instance):
    assert isinstance(instance, graph::GEdge)

@given(instance=graph::GEdge_strategy)
def test_graph::gedge_targetId_type(instance):
    assert isinstance(instance.targetId, str)


@given(instance=graph::GEdge_strategy)
def test_graph::gedge_targetId_setter(instance):
    original = instance.targetId
    instance.targetId = original
    assert instance.targetId == original

@given(instance=graph::GEdge_strategy)
def test_graph::gedge_sourceId_type(instance):
    assert isinstance(instance.sourceId, str)


@given(instance=graph::GEdge_strategy)
def test_graph::gedge_sourceId_setter(instance):
    original = instance.sourceId
    instance.sourceId = original
    assert instance.sourceId == original

@given(instance=graph::GEdge_strategy)
def test_graph::gedge_routerKind_type(instance):
    assert isinstance(instance.routerKind, str)


@given(instance=graph::GEdge_strategy)
def test_graph::gedge_routerKind_setter(instance):
    original = instance.routerKind
    instance.routerKind = original
    assert instance.routerKind == original

@given(instance=graph::GModelRoot_strategy)
@settings(max_examples=50)
def test_graph::gmodelroot_instantiation(instance):
    assert isinstance(instance, graph::GModelRoot)

@given(instance=graph::GModelRoot_strategy)
def test_graph::gmodelroot_revision_type(instance):
    assert isinstance(instance.revision, int)


@given(instance=graph::GModelRoot_strategy)
def test_graph::gmodelroot_revision_setter(instance):
    original = instance.revision
    instance.revision = original
    assert instance.revision == original

@given(instance=graph::GShapeElement_strategy)
@settings(max_examples=50)
def test_graph::gshapeelement_instantiation(instance):
    assert isinstance(instance, graph::GShapeElement)
