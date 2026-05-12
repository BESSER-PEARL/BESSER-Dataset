import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    graph_GLayouting,
    graph_GEdgePlacement,
    graph_GEdgeLayoutable,
    graph_GDimension,
    graph_GBoundsAware,
    graph_GModelElement,
    graph_GPoint,
    GLayouting,
    GEdgeLayoutable,
    GShapeElement,
    graph_GButton,
    graph_GPort,
    graph_GNode,
    graph_GBounds,
    graph_StringToObjectMapEntry,
    GModelRoot,
    GBoundsAware,
    graph_GGraph,
    GModelElement,
    graph_GModelRoot,
    graph_GEdge,
    graph_GShapeElement,
    graph_GHtmlRoot,
    graph_GAlignable,
    graph_GPreRenderedElement,
    graph_GIssue,
    graph_GIssueMarker,
    GAlignable,
    graph_GLabel,
    graph_GCompartment,
    GSeverity,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_graph_glayouting_is_not_abstract():
    assert not inspect.isabstract(graph_GLayouting)


def test_graph_glayouting_constructor_exists():
    assert callable(graph_GLayouting.__init__)


def test_graph_glayouting_constructor_args():
    sig = inspect.signature(graph_GLayouting.__init__)
    params = list(sig.parameters.keys())
    assert "layout" in params, "Missing parameter 'layout'"

def test_graph_glayouting_has_layout():
    assert hasattr(graph_GLayouting, "layout")
    descriptor = None
    for klass in graph_GLayouting.__mro__:
        if "layout" in klass.__dict__:
            descriptor = klass.__dict__["layout"]
            break
    assert isinstance(descriptor, property)



def test_graph_gedgeplacement_is_not_abstract():
    assert not inspect.isabstract(graph_GEdgePlacement)


def test_graph_gedgeplacement_constructor_exists():
    assert callable(graph_GEdgePlacement.__init__)


def test_graph_gedgeplacement_constructor_args():
    sig = inspect.signature(graph_GEdgePlacement.__init__)
    params = list(sig.parameters.keys())
    assert "offset" in params, "Missing parameter 'offset'"
    assert "side" in params, "Missing parameter 'side'"
    assert "rotate" in params, "Missing parameter 'rotate'"
    assert "position" in params, "Missing parameter 'position'"

def test_graph_gedgeplacement_has_offset():
    assert hasattr(graph_GEdgePlacement, "offset")
    descriptor = None
    for klass in graph_GEdgePlacement.__mro__:
        if "offset" in klass.__dict__:
            descriptor = klass.__dict__["offset"]
            break
    assert isinstance(descriptor, property)

def test_graph_gedgeplacement_has_side():
    assert hasattr(graph_GEdgePlacement, "side")
    descriptor = None
    for klass in graph_GEdgePlacement.__mro__:
        if "side" in klass.__dict__:
            descriptor = klass.__dict__["side"]
            break
    assert isinstance(descriptor, property)

def test_graph_gedgeplacement_has_rotate():
    assert hasattr(graph_GEdgePlacement, "rotate")
    descriptor = None
    for klass in graph_GEdgePlacement.__mro__:
        if "rotate" in klass.__dict__:
            descriptor = klass.__dict__["rotate"]
            break
    assert isinstance(descriptor, property)

def test_graph_gedgeplacement_has_position():
    assert hasattr(graph_GEdgePlacement, "position")
    descriptor = None
    for klass in graph_GEdgePlacement.__mro__:
        if "position" in klass.__dict__:
            descriptor = klass.__dict__["position"]
            break
    assert isinstance(descriptor, property)



def test_graph_gedgelayoutable_is_not_abstract():
    assert not inspect.isabstract(graph_GEdgeLayoutable)


def test_graph_gedgelayoutable_constructor_exists():
    assert callable(graph_GEdgeLayoutable.__init__)


def test_graph_gedgelayoutable_constructor_args():
    sig = inspect.signature(graph_GEdgeLayoutable.__init__)
    params = list(sig.parameters.keys())



def test_graph_gdimension_is_not_abstract():
    assert not inspect.isabstract(graph_GDimension)


def test_graph_gdimension_constructor_exists():
    assert callable(graph_GDimension.__init__)


def test_graph_gdimension_constructor_args():
    sig = inspect.signature(graph_GDimension.__init__)
    params = list(sig.parameters.keys())
    assert "width" in params, "Missing parameter 'width'"
    assert "height" in params, "Missing parameter 'height'"

def test_graph_gdimension_has_width():
    assert hasattr(graph_GDimension, "width")
    descriptor = None
    for klass in graph_GDimension.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_graph_gdimension_has_height():
    assert hasattr(graph_GDimension, "height")
    descriptor = None
    for klass in graph_GDimension.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)



def test_graph_gboundsaware_is_not_abstract():
    assert not inspect.isabstract(graph_GBoundsAware)


def test_graph_gboundsaware_constructor_exists():
    assert callable(graph_GBoundsAware.__init__)


def test_graph_gboundsaware_constructor_args():
    sig = inspect.signature(graph_GBoundsAware.__init__)
    params = list(sig.parameters.keys())



def test_graph_gmodelelement_is_not_abstract():
    assert not inspect.isabstract(graph_GModelElement)


def test_graph_gmodelelement_constructor_exists():
    assert callable(graph_GModelElement.__init__)


def test_graph_gmodelelement_constructor_args():
    sig = inspect.signature(graph_GModelElement.__init__)
    params = list(sig.parameters.keys())
    assert "trace" in params, "Missing parameter 'trace'"
    assert "cssClasses" in params, "Missing parameter 'cssClasses'"
    assert "id" in params, "Missing parameter 'id'"
    assert "type" in params, "Missing parameter 'type'"

def test_graph_gmodelelement_has_trace():
    assert hasattr(graph_GModelElement, "trace")
    descriptor = None
    for klass in graph_GModelElement.__mro__:
        if "trace" in klass.__dict__:
            descriptor = klass.__dict__["trace"]
            break
    assert isinstance(descriptor, property)

def test_graph_gmodelelement_has_cssClasses():
    assert hasattr(graph_GModelElement, "cssClasses")
    descriptor = None
    for klass in graph_GModelElement.__mro__:
        if "cssClasses" in klass.__dict__:
            descriptor = klass.__dict__["cssClasses"]
            break
    assert isinstance(descriptor, property)

def test_graph_gmodelelement_has_id():
    assert hasattr(graph_GModelElement, "id")
    descriptor = None
    for klass in graph_GModelElement.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_graph_gmodelelement_has_type():
    assert hasattr(graph_GModelElement, "type")
    descriptor = None
    for klass in graph_GModelElement.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_graph_gpoint_is_not_abstract():
    assert not inspect.isabstract(graph_GPoint)


def test_graph_gpoint_constructor_exists():
    assert callable(graph_GPoint.__init__)


def test_graph_gpoint_constructor_args():
    sig = inspect.signature(graph_GPoint.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"
    assert "y" in params, "Missing parameter 'y'"

def test_graph_gpoint_has_x():
    assert hasattr(graph_GPoint, "x")
    descriptor = None
    for klass in graph_GPoint.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_graph_gpoint_has_y():
    assert hasattr(graph_GPoint, "y")
    descriptor = None
    for klass in graph_GPoint.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
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



def test_graph_gbutton_is_not_abstract():
    assert not inspect.isabstract(graph_GButton)


def test_graph_gbutton_constructor_exists():
    assert callable(graph_GButton.__init__)


def test_graph_gbutton_constructor_args():
    sig = inspect.signature(graph_GButton.__init__)
    params = list(sig.parameters.keys())
    assert "enabled" in params, "Missing parameter 'enabled'"

def test_graph_gbutton_has_enabled():
    assert hasattr(graph_GButton, "enabled")
    descriptor = None
    for klass in graph_GButton.__mro__:
        if "enabled" in klass.__dict__:
            descriptor = klass.__dict__["enabled"]
            break
    assert isinstance(descriptor, property)



def test_graph_gport_is_not_abstract():
    assert not inspect.isabstract(graph_GPort)


def test_graph_gport_constructor_exists():
    assert callable(graph_GPort.__init__)


def test_graph_gport_constructor_args():
    sig = inspect.signature(graph_GPort.__init__)
    params = list(sig.parameters.keys())



def test_graph_gnode_is_not_abstract():
    assert not inspect.isabstract(graph_GNode)


def test_graph_gnode_constructor_exists():
    assert callable(graph_GNode.__init__)


def test_graph_gnode_constructor_args():
    sig = inspect.signature(graph_GNode.__init__)
    params = list(sig.parameters.keys())



def test_graph_gbounds_is_not_abstract():
    assert not inspect.isabstract(graph_GBounds)


def test_graph_gbounds_constructor_exists():
    assert callable(graph_GBounds.__init__)


def test_graph_gbounds_constructor_args():
    sig = inspect.signature(graph_GBounds.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"
    assert "width" in params, "Missing parameter 'width'"
    assert "height" in params, "Missing parameter 'height'"
    assert "y" in params, "Missing parameter 'y'"

def test_graph_gbounds_has_x():
    assert hasattr(graph_GBounds, "x")
    descriptor = None
    for klass in graph_GBounds.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_graph_gbounds_has_width():
    assert hasattr(graph_GBounds, "width")
    descriptor = None
    for klass in graph_GBounds.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_graph_gbounds_has_height():
    assert hasattr(graph_GBounds, "height")
    descriptor = None
    for klass in graph_GBounds.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)

def test_graph_gbounds_has_y():
    assert hasattr(graph_GBounds, "y")
    descriptor = None
    for klass in graph_GBounds.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)



def test_graph_stringtoobjectmapentry_is_not_abstract():
    assert not inspect.isabstract(graph_StringToObjectMapEntry)


def test_graph_stringtoobjectmapentry_constructor_exists():
    assert callable(graph_StringToObjectMapEntry.__init__)


def test_graph_stringtoobjectmapentry_constructor_args():
    sig = inspect.signature(graph_StringToObjectMapEntry.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"
    assert "value" in params, "Missing parameter 'value'"

def test_graph_stringtoobjectmapentry_has_key():
    assert hasattr(graph_StringToObjectMapEntry, "key")
    descriptor = None
    for klass in graph_StringToObjectMapEntry.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_graph_stringtoobjectmapentry_has_value():
    assert hasattr(graph_StringToObjectMapEntry, "value")
    descriptor = None
    for klass in graph_StringToObjectMapEntry.__mro__:
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



def test_gboundsaware_is_not_abstract():
    assert not inspect.isabstract(GBoundsAware)


def test_gboundsaware_constructor_exists():
    assert callable(GBoundsAware.__init__)


def test_gboundsaware_constructor_args():
    sig = inspect.signature(GBoundsAware.__init__)
    params = list(sig.parameters.keys())



def test_graph_ggraph_is_not_abstract():
    assert not inspect.isabstract(graph_GGraph)


def test_graph_ggraph_constructor_exists():
    assert callable(graph_GGraph.__init__)


def test_graph_ggraph_constructor_args():
    sig = inspect.signature(graph_GGraph.__init__)
    params = list(sig.parameters.keys())



def test_gmodelelement_is_not_abstract():
    assert not inspect.isabstract(GModelElement)


def test_gmodelelement_constructor_exists():
    assert callable(GModelElement.__init__)


def test_gmodelelement_constructor_args():
    sig = inspect.signature(GModelElement.__init__)
    params = list(sig.parameters.keys())



def test_graph_gmodelroot_is_not_abstract():
    assert not inspect.isabstract(graph_GModelRoot)


def test_graph_gmodelroot_constructor_exists():
    assert callable(graph_GModelRoot.__init__)


def test_graph_gmodelroot_constructor_args():
    sig = inspect.signature(graph_GModelRoot.__init__)
    params = list(sig.parameters.keys())
    assert "revision" in params, "Missing parameter 'revision'"

def test_graph_gmodelroot_has_revision():
    assert hasattr(graph_GModelRoot, "revision")
    descriptor = None
    for klass in graph_GModelRoot.__mro__:
        if "revision" in klass.__dict__:
            descriptor = klass.__dict__["revision"]
            break
    assert isinstance(descriptor, property)



def test_graph_gedge_is_not_abstract():
    assert not inspect.isabstract(graph_GEdge)


def test_graph_gedge_constructor_exists():
    assert callable(graph_GEdge.__init__)


def test_graph_gedge_constructor_args():
    sig = inspect.signature(graph_GEdge.__init__)
    params = list(sig.parameters.keys())
    assert "sourceId" in params, "Missing parameter 'sourceId'"
    assert "targetId" in params, "Missing parameter 'targetId'"
    assert "routerKind" in params, "Missing parameter 'routerKind'"

def test_graph_gedge_has_sourceId():
    assert hasattr(graph_GEdge, "sourceId")
    descriptor = None
    for klass in graph_GEdge.__mro__:
        if "sourceId" in klass.__dict__:
            descriptor = klass.__dict__["sourceId"]
            break
    assert isinstance(descriptor, property)

def test_graph_gedge_has_targetId():
    assert hasattr(graph_GEdge, "targetId")
    descriptor = None
    for klass in graph_GEdge.__mro__:
        if "targetId" in klass.__dict__:
            descriptor = klass.__dict__["targetId"]
            break
    assert isinstance(descriptor, property)

def test_graph_gedge_has_routerKind():
    assert hasattr(graph_GEdge, "routerKind")
    descriptor = None
    for klass in graph_GEdge.__mro__:
        if "routerKind" in klass.__dict__:
            descriptor = klass.__dict__["routerKind"]
            break
    assert isinstance(descriptor, property)



def test_graph_gshapeelement_is_not_abstract():
    assert not inspect.isabstract(graph_GShapeElement)


def test_graph_gshapeelement_constructor_exists():
    assert callable(graph_GShapeElement.__init__)


def test_graph_gshapeelement_constructor_args():
    sig = inspect.signature(graph_GShapeElement.__init__)
    params = list(sig.parameters.keys())



def test_graph_ghtmlroot_is_not_abstract():
    assert not inspect.isabstract(graph_GHtmlRoot)


def test_graph_ghtmlroot_constructor_exists():
    assert callable(graph_GHtmlRoot.__init__)


def test_graph_ghtmlroot_constructor_args():
    sig = inspect.signature(graph_GHtmlRoot.__init__)
    params = list(sig.parameters.keys())
    assert "classes" in params, "Missing parameter 'classes'"

def test_graph_ghtmlroot_has_classes():
    assert hasattr(graph_GHtmlRoot, "classes")
    descriptor = None
    for klass in graph_GHtmlRoot.__mro__:
        if "classes" in klass.__dict__:
            descriptor = klass.__dict__["classes"]
            break
    assert isinstance(descriptor, property)



def test_graph_galignable_is_not_abstract():
    assert not inspect.isabstract(graph_GAlignable)


def test_graph_galignable_constructor_exists():
    assert callable(graph_GAlignable.__init__)


def test_graph_galignable_constructor_args():
    sig = inspect.signature(graph_GAlignable.__init__)
    params = list(sig.parameters.keys())



def test_graph_gprerenderedelement_is_not_abstract():
    assert not inspect.isabstract(graph_GPreRenderedElement)


def test_graph_gprerenderedelement_constructor_exists():
    assert callable(graph_GPreRenderedElement.__init__)


def test_graph_gprerenderedelement_constructor_args():
    sig = inspect.signature(graph_GPreRenderedElement.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"

def test_graph_gprerenderedelement_has_code():
    assert hasattr(graph_GPreRenderedElement, "code")
    descriptor = None
    for klass in graph_GPreRenderedElement.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)



def test_graph_gissue_is_not_abstract():
    assert not inspect.isabstract(graph_GIssue)


def test_graph_gissue_constructor_exists():
    assert callable(graph_GIssue.__init__)


def test_graph_gissue_constructor_args():
    sig = inspect.signature(graph_GIssue.__init__)
    params = list(sig.parameters.keys())
    assert "severity" in params, "Missing parameter 'severity'"
    assert "message" in params, "Missing parameter 'message'"

def test_graph_gissue_has_severity():
    assert hasattr(graph_GIssue, "severity")
    descriptor = None
    for klass in graph_GIssue.__mro__:
        if "severity" in klass.__dict__:
            descriptor = klass.__dict__["severity"]
            break
    assert isinstance(descriptor, property)

def test_graph_gissue_has_message():
    assert hasattr(graph_GIssue, "message")
    descriptor = None
    for klass in graph_GIssue.__mro__:
        if "message" in klass.__dict__:
            descriptor = klass.__dict__["message"]
            break
    assert isinstance(descriptor, property)



def test_graph_gissuemarker_is_not_abstract():
    assert not inspect.isabstract(graph_GIssueMarker)


def test_graph_gissuemarker_constructor_exists():
    assert callable(graph_GIssueMarker.__init__)


def test_graph_gissuemarker_constructor_args():
    sig = inspect.signature(graph_GIssueMarker.__init__)
    params = list(sig.parameters.keys())



def test_galignable_is_not_abstract():
    assert not inspect.isabstract(GAlignable)


def test_galignable_constructor_exists():
    assert callable(GAlignable.__init__)


def test_galignable_constructor_args():
    sig = inspect.signature(GAlignable.__init__)
    params = list(sig.parameters.keys())



def test_graph_glabel_is_not_abstract():
    assert not inspect.isabstract(graph_GLabel)


def test_graph_glabel_constructor_exists():
    assert callable(graph_GLabel.__init__)


def test_graph_glabel_constructor_args():
    sig = inspect.signature(graph_GLabel.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_graph_glabel_has_text():
    assert hasattr(graph_GLabel, "text")
    descriptor = None
    for klass in graph_GLabel.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_graph_gcompartment_is_not_abstract():
    assert not inspect.isabstract(graph_GCompartment)


def test_graph_gcompartment_constructor_exists():
    assert callable(graph_GCompartment.__init__)


def test_graph_gcompartment_constructor_args():
    sig = inspect.signature(graph_GCompartment.__init__)
    params = list(sig.parameters.keys())

def test_gseverity_exists():
    # Check that the Enumeration exists
    assert GSeverity is not None

def test_gseverity_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in GSeverity]
    expected_literals = [
        "info",
        "error",
        "warning",
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
graph_GLayouting_strategy = st.builds(
    graph_GLayouting,
    layout=
        safe_text
)
graph_GEdgePlacement_strategy = st.builds(
    graph_GEdgePlacement,
    offset=
        safe_text,
    side=
        safe_text,
    rotate=
        st.booleans(),
    position=
        safe_text
)
graph_GEdgeLayoutable_strategy = st.builds(
    graph_GEdgeLayoutable,
)
graph_GDimension_strategy = st.builds(
    graph_GDimension,
    width=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    height=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
graph_GBoundsAware_strategy = st.builds(
    graph_GBoundsAware,
)
graph_GModelElement_strategy = st.builds(
    graph_GModelElement,
    trace=
        safe_text,
    cssClasses=
        safe_text,
    id=
        safe_text,
    type=
        safe_text
)
graph_GPoint_strategy = st.builds(
    graph_GPoint,
    x=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    y=
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
graph_GButton_strategy = st.builds(
    graph_GButton,
    enabled=
        st.booleans()
)
graph_GPort_strategy = st.builds(
    graph_GPort,
)
graph_GNode_strategy = st.builds(
    graph_GNode,
)
graph_GBounds_strategy = st.builds(
    graph_GBounds,
    x=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    width=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    height=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    y=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
graph_StringToObjectMapEntry_strategy = st.builds(
    graph_StringToObjectMapEntry,
    key=
        safe_text,
    value=
        safe_text
)
GModelRoot_strategy = st.builds(
    GModelRoot,
)
GBoundsAware_strategy = st.builds(
    GBoundsAware,
)
graph_GGraph_strategy = st.builds(
    graph_GGraph,
)
GModelElement_strategy = st.builds(
    GModelElement,
)
graph_GModelRoot_strategy = st.builds(
    graph_GModelRoot,
    revision=
        st.integers()
)
graph_GEdge_strategy = st.builds(
    graph_GEdge,
    sourceId=
        safe_text,
    targetId=
        safe_text,
    routerKind=
        safe_text
)
graph_GShapeElement_strategy = st.builds(
    graph_GShapeElement,
)
graph_GHtmlRoot_strategy = st.builds(
    graph_GHtmlRoot,
    classes=
        safe_text
)
graph_GAlignable_strategy = st.builds(
    graph_GAlignable,
)
graph_GPreRenderedElement_strategy = st.builds(
    graph_GPreRenderedElement,
    code=
        safe_text
)
graph_GIssue_strategy = st.builds(
    graph_GIssue,
    severity=
        safe_text,
    message=
        safe_text
)
graph_GIssueMarker_strategy = st.builds(
    graph_GIssueMarker,
)
GAlignable_strategy = st.builds(
    GAlignable,
)
graph_GLabel_strategy = st.builds(
    graph_GLabel,
    text=
        safe_text
)
graph_GCompartment_strategy = st.builds(
    graph_GCompartment,
)

@given(instance=graph_GLayouting_strategy)
@settings(max_examples=50)
def test_graph_glayouting_instantiation(instance):
    assert isinstance(instance, graph_GLayouting)



@given(instance=graph_GLayouting_strategy)
def test_graph_glayouting_layout_setter(instance):
    original = instance.layout
    instance.layout = original
    assert instance.layout == original

@given(instance=graph_GEdgePlacement_strategy)
@settings(max_examples=50)
def test_graph_gedgeplacement_instantiation(instance):
    assert isinstance(instance, graph_GEdgePlacement)



@given(instance=graph_GEdgePlacement_strategy)
def test_graph_gedgeplacement_offset_setter(instance):
    original = instance.offset
    instance.offset = original
    assert instance.offset == original



@given(instance=graph_GEdgePlacement_strategy)
def test_graph_gedgeplacement_side_setter(instance):
    original = instance.side
    instance.side = original
    assert instance.side == original



@given(instance=graph_GEdgePlacement_strategy)
def test_graph_gedgeplacement_rotate_setter(instance):
    original = instance.rotate
    instance.rotate = original
    assert instance.rotate == original



@given(instance=graph_GEdgePlacement_strategy)
def test_graph_gedgeplacement_position_setter(instance):
    original = instance.position
    instance.position = original
    assert instance.position == original

@given(instance=graph_GEdgeLayoutable_strategy)
@settings(max_examples=50)
def test_graph_gedgelayoutable_instantiation(instance):
    assert isinstance(instance, graph_GEdgeLayoutable)

@given(instance=graph_GDimension_strategy)
@settings(max_examples=50)
def test_graph_gdimension_instantiation(instance):
    assert isinstance(instance, graph_GDimension)



@given(instance=graph_GDimension_strategy)
def test_graph_gdimension_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original



@given(instance=graph_GDimension_strategy)
def test_graph_gdimension_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original

@given(instance=graph_GBoundsAware_strategy)
@settings(max_examples=50)
def test_graph_gboundsaware_instantiation(instance):
    assert isinstance(instance, graph_GBoundsAware)

@given(instance=graph_GModelElement_strategy)
@settings(max_examples=50)
def test_graph_gmodelelement_instantiation(instance):
    assert isinstance(instance, graph_GModelElement)



@given(instance=graph_GModelElement_strategy)
def test_graph_gmodelelement_trace_setter(instance):
    original = instance.trace
    instance.trace = original
    assert instance.trace == original



@given(instance=graph_GModelElement_strategy)
def test_graph_gmodelelement_cssClasses_setter(instance):
    original = instance.cssClasses
    instance.cssClasses = original
    assert instance.cssClasses == original



@given(instance=graph_GModelElement_strategy)
def test_graph_gmodelelement_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=graph_GModelElement_strategy)
def test_graph_gmodelelement_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=graph_GPoint_strategy)
@settings(max_examples=50)
def test_graph_gpoint_instantiation(instance):
    assert isinstance(instance, graph_GPoint)



@given(instance=graph_GPoint_strategy)
def test_graph_gpoint_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=graph_GPoint_strategy)
def test_graph_gpoint_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

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

@given(instance=graph_GButton_strategy)
@settings(max_examples=50)
def test_graph_gbutton_instantiation(instance):
    assert isinstance(instance, graph_GButton)



@given(instance=graph_GButton_strategy)
def test_graph_gbutton_enabled_setter(instance):
    original = instance.enabled
    instance.enabled = original
    assert instance.enabled == original

@given(instance=graph_GPort_strategy)
@settings(max_examples=50)
def test_graph_gport_instantiation(instance):
    assert isinstance(instance, graph_GPort)

@given(instance=graph_GNode_strategy)
@settings(max_examples=50)
def test_graph_gnode_instantiation(instance):
    assert isinstance(instance, graph_GNode)

@given(instance=graph_GBounds_strategy)
@settings(max_examples=50)
def test_graph_gbounds_instantiation(instance):
    assert isinstance(instance, graph_GBounds)



@given(instance=graph_GBounds_strategy)
def test_graph_gbounds_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=graph_GBounds_strategy)
def test_graph_gbounds_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original



@given(instance=graph_GBounds_strategy)
def test_graph_gbounds_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original



@given(instance=graph_GBounds_strategy)
def test_graph_gbounds_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=graph_StringToObjectMapEntry_strategy)
@settings(max_examples=50)
def test_graph_stringtoobjectmapentry_instantiation(instance):
    assert isinstance(instance, graph_StringToObjectMapEntry)



@given(instance=graph_StringToObjectMapEntry_strategy)
def test_graph_stringtoobjectmapentry_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original



@given(instance=graph_StringToObjectMapEntry_strategy)
def test_graph_stringtoobjectmapentry_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=GModelRoot_strategy)
@settings(max_examples=50)
def test_gmodelroot_instantiation(instance):
    assert isinstance(instance, GModelRoot)

@given(instance=GBoundsAware_strategy)
@settings(max_examples=50)
def test_gboundsaware_instantiation(instance):
    assert isinstance(instance, GBoundsAware)

@given(instance=graph_GGraph_strategy)
@settings(max_examples=50)
def test_graph_ggraph_instantiation(instance):
    assert isinstance(instance, graph_GGraph)

@given(instance=GModelElement_strategy)
@settings(max_examples=50)
def test_gmodelelement_instantiation(instance):
    assert isinstance(instance, GModelElement)

@given(instance=graph_GModelRoot_strategy)
@settings(max_examples=50)
def test_graph_gmodelroot_instantiation(instance):
    assert isinstance(instance, graph_GModelRoot)



@given(instance=graph_GModelRoot_strategy)
def test_graph_gmodelroot_revision_setter(instance):
    original = instance.revision
    instance.revision = original
    assert instance.revision == original

@given(instance=graph_GEdge_strategy)
@settings(max_examples=50)
def test_graph_gedge_instantiation(instance):
    assert isinstance(instance, graph_GEdge)



@given(instance=graph_GEdge_strategy)
def test_graph_gedge_sourceId_setter(instance):
    original = instance.sourceId
    instance.sourceId = original
    assert instance.sourceId == original



@given(instance=graph_GEdge_strategy)
def test_graph_gedge_targetId_setter(instance):
    original = instance.targetId
    instance.targetId = original
    assert instance.targetId == original



@given(instance=graph_GEdge_strategy)
def test_graph_gedge_routerKind_setter(instance):
    original = instance.routerKind
    instance.routerKind = original
    assert instance.routerKind == original

@given(instance=graph_GShapeElement_strategy)
@settings(max_examples=50)
def test_graph_gshapeelement_instantiation(instance):
    assert isinstance(instance, graph_GShapeElement)

@given(instance=graph_GHtmlRoot_strategy)
@settings(max_examples=50)
def test_graph_ghtmlroot_instantiation(instance):
    assert isinstance(instance, graph_GHtmlRoot)



@given(instance=graph_GHtmlRoot_strategy)
def test_graph_ghtmlroot_classes_setter(instance):
    original = instance.classes
    instance.classes = original
    assert instance.classes == original

@given(instance=graph_GAlignable_strategy)
@settings(max_examples=50)
def test_graph_galignable_instantiation(instance):
    assert isinstance(instance, graph_GAlignable)

@given(instance=graph_GPreRenderedElement_strategy)
@settings(max_examples=50)
def test_graph_gprerenderedelement_instantiation(instance):
    assert isinstance(instance, graph_GPreRenderedElement)



@given(instance=graph_GPreRenderedElement_strategy)
def test_graph_gprerenderedelement_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=graph_GIssue_strategy)
@settings(max_examples=50)
def test_graph_gissue_instantiation(instance):
    assert isinstance(instance, graph_GIssue)



@given(instance=graph_GIssue_strategy)
def test_graph_gissue_severity_setter(instance):
    original = instance.severity
    instance.severity = original
    assert instance.severity == original



@given(instance=graph_GIssue_strategy)
def test_graph_gissue_message_setter(instance):
    original = instance.message
    instance.message = original
    assert instance.message == original

@given(instance=graph_GIssueMarker_strategy)
@settings(max_examples=50)
def test_graph_gissuemarker_instantiation(instance):
    assert isinstance(instance, graph_GIssueMarker)

@given(instance=GAlignable_strategy)
@settings(max_examples=50)
def test_galignable_instantiation(instance):
    assert isinstance(instance, GAlignable)

@given(instance=graph_GLabel_strategy)
@settings(max_examples=50)
def test_graph_glabel_instantiation(instance):
    assert isinstance(instance, graph_GLabel)



@given(instance=graph_GLabel_strategy)
def test_graph_glabel_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=graph_GCompartment_strategy)
@settings(max_examples=50)
def test_graph_gcompartment_instantiation(instance):
    assert isinstance(instance, graph_GCompartment)
