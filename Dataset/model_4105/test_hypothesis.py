import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    railDsl_TrainRouteObject,
    railDsl_RouteObject,
    TrainRouteObject,
    railDsl_TrainRouteSegment,
    railDsl_TrainRoutePoint,
    railDsl_TrainSegment,
    railDsl_NamedElement,
    TrackObject,
    railDsl_Point,
    railDsl_Segment,
    RouteObject,
    Declaration,
    railDsl_Vertex,
    railDsl_TrainRoute,
    railDsl_Track,
    railDsl_Train,
    railDsl_TrackObject,
    SegmentObject,
    railDsl_Signal,
    railDsl_Platform,
    railDsl_LevelCrossing,
    railDsl_Derailer,
    railDsl_SegmentPosition,
    NamedElement,
    railDsl_Station,
    railDsl_Declaration,
    railDsl_SegmentObject,
    Side,
    SpeedLimit,
    VertexKind,
    Orientation,
    TrainRouteKind,
    PointKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_raildsl_trainrouteobject_is_not_abstract():
    assert not inspect.isabstract(railDsl_TrainRouteObject)


def test_raildsl_trainrouteobject_constructor_exists():
    assert callable(railDsl_TrainRouteObject.__init__)


def test_raildsl_trainrouteobject_constructor_args():
    sig = inspect.signature(railDsl_TrainRouteObject.__init__)
    params = list(sig.parameters.keys())
    assert "speedLimit" in params, "Missing parameter 'speedLimit'"

def test_raildsl_trainrouteobject_has_speedLimit():
    assert hasattr(railDsl_TrainRouteObject, "speedLimit")
    descriptor = None
    for klass in railDsl_TrainRouteObject.__mro__:
        if "speedLimit" in klass.__dict__:
            descriptor = klass.__dict__["speedLimit"]
            break
    assert isinstance(descriptor, property)



def test_raildsl_routeobject_is_not_abstract():
    assert not inspect.isabstract(railDsl_RouteObject)


def test_raildsl_routeobject_constructor_exists():
    assert callable(railDsl_RouteObject.__init__)


def test_raildsl_routeobject_constructor_args():
    sig = inspect.signature(railDsl_RouteObject.__init__)
    params = list(sig.parameters.keys())
    assert "error" in params, "Missing parameter 'error'"
    assert "speedLimit" in params, "Missing parameter 'speedLimit'"

def test_raildsl_routeobject_has_error():
    assert hasattr(railDsl_RouteObject, "error")
    descriptor = None
    for klass in railDsl_RouteObject.__mro__:
        if "error" in klass.__dict__:
            descriptor = klass.__dict__["error"]
            break
    assert isinstance(descriptor, property)

def test_raildsl_routeobject_has_speedLimit():
    assert hasattr(railDsl_RouteObject, "speedLimit")
    descriptor = None
    for klass in railDsl_RouteObject.__mro__:
        if "speedLimit" in klass.__dict__:
            descriptor = klass.__dict__["speedLimit"]
            break
    assert isinstance(descriptor, property)



def test_trainrouteobject_is_not_abstract():
    assert not inspect.isabstract(TrainRouteObject)


def test_trainrouteobject_constructor_exists():
    assert callable(TrainRouteObject.__init__)


def test_trainrouteobject_constructor_args():
    sig = inspect.signature(TrainRouteObject.__init__)
    params = list(sig.parameters.keys())



def test_raildsl_trainroutesegment_is_not_abstract():
    assert not inspect.isabstract(railDsl_TrainRouteSegment)


def test_raildsl_trainroutesegment_constructor_exists():
    assert callable(railDsl_TrainRouteSegment.__init__)


def test_raildsl_trainroutesegment_constructor_args():
    sig = inspect.signature(railDsl_TrainRouteSegment.__init__)
    params = list(sig.parameters.keys())



def test_raildsl_trainroutepoint_is_not_abstract():
    assert not inspect.isabstract(railDsl_TrainRoutePoint)


def test_raildsl_trainroutepoint_constructor_exists():
    assert callable(railDsl_TrainRoutePoint.__init__)


def test_raildsl_trainroutepoint_constructor_args():
    sig = inspect.signature(railDsl_TrainRoutePoint.__init__)
    params = list(sig.parameters.keys())
    assert "selectedOutput" in params, "Missing parameter 'selectedOutput'"
    assert "selectedInput" in params, "Missing parameter 'selectedInput'"

def test_raildsl_trainroutepoint_has_selectedOutput():
    assert hasattr(railDsl_TrainRoutePoint, "selectedOutput")
    descriptor = None
    for klass in railDsl_TrainRoutePoint.__mro__:
        if "selectedOutput" in klass.__dict__:
            descriptor = klass.__dict__["selectedOutput"]
            break
    assert isinstance(descriptor, property)

def test_raildsl_trainroutepoint_has_selectedInput():
    assert hasattr(railDsl_TrainRoutePoint, "selectedInput")
    descriptor = None
    for klass in railDsl_TrainRoutePoint.__mro__:
        if "selectedInput" in klass.__dict__:
            descriptor = klass.__dict__["selectedInput"]
            break
    assert isinstance(descriptor, property)



def test_raildsl_trainsegment_is_not_abstract():
    assert not inspect.isabstract(railDsl_TrainSegment)


def test_raildsl_trainsegment_constructor_exists():
    assert callable(railDsl_TrainSegment.__init__)


def test_raildsl_trainsegment_constructor_args():
    sig = inspect.signature(railDsl_TrainSegment.__init__)
    params = list(sig.parameters.keys())
    assert "length" in params, "Missing parameter 'length'"

def test_raildsl_trainsegment_has_length():
    assert hasattr(railDsl_TrainSegment, "length")
    descriptor = None
    for klass in railDsl_TrainSegment.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)



def test_raildsl_namedelement_is_not_abstract():
    assert not inspect.isabstract(railDsl_NamedElement)


def test_raildsl_namedelement_constructor_exists():
    assert callable(railDsl_NamedElement.__init__)


def test_raildsl_namedelement_constructor_args():
    sig = inspect.signature(railDsl_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_raildsl_namedelement_has_name():
    assert hasattr(railDsl_NamedElement, "name")
    descriptor = None
    for klass in railDsl_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_trackobject_is_not_abstract():
    assert not inspect.isabstract(TrackObject)


def test_trackobject_constructor_exists():
    assert callable(TrackObject.__init__)


def test_trackobject_constructor_args():
    sig = inspect.signature(TrackObject.__init__)
    params = list(sig.parameters.keys())



def test_raildsl_point_is_not_abstract():
    assert not inspect.isabstract(railDsl_Point)


def test_raildsl_point_constructor_exists():
    assert callable(railDsl_Point.__init__)


def test_raildsl_point_constructor_args():
    sig = inspect.signature(railDsl_Point.__init__)
    params = list(sig.parameters.keys())
    assert "locked" in params, "Missing parameter 'locked'"
    assert "kind" in params, "Missing parameter 'kind'"
    assert "selectedOutput" in params, "Missing parameter 'selectedOutput'"
    assert "selectedInput" in params, "Missing parameter 'selectedInput'"

def test_raildsl_point_has_locked():
    assert hasattr(railDsl_Point, "locked")
    descriptor = None
    for klass in railDsl_Point.__mro__:
        if "locked" in klass.__dict__:
            descriptor = klass.__dict__["locked"]
            break
    assert isinstance(descriptor, property)

def test_raildsl_point_has_kind():
    assert hasattr(railDsl_Point, "kind")
    descriptor = None
    for klass in railDsl_Point.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)

def test_raildsl_point_has_selectedOutput():
    assert hasattr(railDsl_Point, "selectedOutput")
    descriptor = None
    for klass in railDsl_Point.__mro__:
        if "selectedOutput" in klass.__dict__:
            descriptor = klass.__dict__["selectedOutput"]
            break
    assert isinstance(descriptor, property)

def test_raildsl_point_has_selectedInput():
    assert hasattr(railDsl_Point, "selectedInput")
    descriptor = None
    for klass in railDsl_Point.__mro__:
        if "selectedInput" in klass.__dict__:
            descriptor = klass.__dict__["selectedInput"]
            break
    assert isinstance(descriptor, property)



def test_raildsl_segment_is_not_abstract():
    assert not inspect.isabstract(railDsl_Segment)


def test_raildsl_segment_constructor_exists():
    assert callable(railDsl_Segment.__init__)


def test_raildsl_segment_constructor_args():
    sig = inspect.signature(railDsl_Segment.__init__)
    params = list(sig.parameters.keys())



def test_routeobject_is_not_abstract():
    assert not inspect.isabstract(RouteObject)


def test_routeobject_constructor_exists():
    assert callable(RouteObject.__init__)


def test_routeobject_constructor_args():
    sig = inspect.signature(RouteObject.__init__)
    params = list(sig.parameters.keys())



def test_declaration_is_not_abstract():
    assert not inspect.isabstract(Declaration)


def test_declaration_constructor_exists():
    assert callable(Declaration.__init__)


def test_declaration_constructor_args():
    sig = inspect.signature(Declaration.__init__)
    params = list(sig.parameters.keys())



def test_raildsl_vertex_is_not_abstract():
    assert not inspect.isabstract(railDsl_Vertex)


def test_raildsl_vertex_constructor_exists():
    assert callable(railDsl_Vertex.__init__)


def test_raildsl_vertex_constructor_args():
    sig = inspect.signature(railDsl_Vertex.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_raildsl_vertex_has_kind():
    assert hasattr(railDsl_Vertex, "kind")
    descriptor = None
    for klass in railDsl_Vertex.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_raildsl_trainroute_is_not_abstract():
    assert not inspect.isabstract(railDsl_TrainRoute)


def test_raildsl_trainroute_constructor_exists():
    assert callable(railDsl_TrainRoute.__init__)


def test_raildsl_trainroute_constructor_args():
    sig = inspect.signature(railDsl_TrainRoute.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"
    assert "locked" in params, "Missing parameter 'locked'"

def test_raildsl_trainroute_has_kind():
    assert hasattr(railDsl_TrainRoute, "kind")
    descriptor = None
    for klass in railDsl_TrainRoute.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)

def test_raildsl_trainroute_has_locked():
    assert hasattr(railDsl_TrainRoute, "locked")
    descriptor = None
    for klass in railDsl_TrainRoute.__mro__:
        if "locked" in klass.__dict__:
            descriptor = klass.__dict__["locked"]
            break
    assert isinstance(descriptor, property)



def test_raildsl_track_is_not_abstract():
    assert not inspect.isabstract(railDsl_Track)


def test_raildsl_track_constructor_exists():
    assert callable(railDsl_Track.__init__)


def test_raildsl_track_constructor_args():
    sig = inspect.signature(railDsl_Track.__init__)
    params = list(sig.parameters.keys())



def test_raildsl_train_is_not_abstract():
    assert not inspect.isabstract(railDsl_Train)


def test_raildsl_train_constructor_exists():
    assert callable(railDsl_Train.__init__)


def test_raildsl_train_constructor_args():
    sig = inspect.signature(railDsl_Train.__init__)
    params = list(sig.parameters.keys())
    assert "speed" in params, "Missing parameter 'speed'"
    assert "acceleration" in params, "Missing parameter 'acceleration'"
    assert "length" in params, "Missing parameter 'length'"

def test_raildsl_train_has_speed():
    assert hasattr(railDsl_Train, "speed")
    descriptor = None
    for klass in railDsl_Train.__mro__:
        if "speed" in klass.__dict__:
            descriptor = klass.__dict__["speed"]
            break
    assert isinstance(descriptor, property)

def test_raildsl_train_has_acceleration():
    assert hasattr(railDsl_Train, "acceleration")
    descriptor = None
    for klass in railDsl_Train.__mro__:
        if "acceleration" in klass.__dict__:
            descriptor = klass.__dict__["acceleration"]
            break
    assert isinstance(descriptor, property)

def test_raildsl_train_has_length():
    assert hasattr(railDsl_Train, "length")
    descriptor = None
    for klass in railDsl_Train.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)



def test_raildsl_trackobject_is_not_abstract():
    assert not inspect.isabstract(railDsl_TrackObject)


def test_raildsl_trackobject_constructor_exists():
    assert callable(railDsl_TrackObject.__init__)


def test_raildsl_trackobject_constructor_args():
    sig = inspect.signature(railDsl_TrackObject.__init__)
    params = list(sig.parameters.keys())
    assert "length" in params, "Missing parameter 'length'"

def test_raildsl_trackobject_has_length():
    assert hasattr(railDsl_TrackObject, "length")
    descriptor = None
    for klass in railDsl_TrackObject.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)



def test_segmentobject_is_not_abstract():
    assert not inspect.isabstract(SegmentObject)


def test_segmentobject_constructor_exists():
    assert callable(SegmentObject.__init__)


def test_segmentobject_constructor_args():
    sig = inspect.signature(SegmentObject.__init__)
    params = list(sig.parameters.keys())



def test_raildsl_signal_is_not_abstract():
    assert not inspect.isabstract(railDsl_Signal)


def test_raildsl_signal_constructor_exists():
    assert callable(railDsl_Signal.__init__)


def test_raildsl_signal_constructor_args():
    sig = inspect.signature(railDsl_Signal.__init__)
    params = list(sig.parameters.keys())
    assert "shunting" in params, "Missing parameter 'shunting'"
    assert "main" in params, "Missing parameter 'main'"

def test_raildsl_signal_has_shunting():
    assert hasattr(railDsl_Signal, "shunting")
    descriptor = None
    for klass in railDsl_Signal.__mro__:
        if "shunting" in klass.__dict__:
            descriptor = klass.__dict__["shunting"]
            break
    assert isinstance(descriptor, property)

def test_raildsl_signal_has_main():
    assert hasattr(railDsl_Signal, "main")
    descriptor = None
    for klass in railDsl_Signal.__mro__:
        if "main" in klass.__dict__:
            descriptor = klass.__dict__["main"]
            break
    assert isinstance(descriptor, property)



def test_raildsl_platform_is_not_abstract():
    assert not inspect.isabstract(railDsl_Platform)


def test_raildsl_platform_constructor_exists():
    assert callable(railDsl_Platform.__init__)


def test_raildsl_platform_constructor_args():
    sig = inspect.signature(railDsl_Platform.__init__)
    params = list(sig.parameters.keys())
    assert "length" in params, "Missing parameter 'length'"

def test_raildsl_platform_has_length():
    assert hasattr(railDsl_Platform, "length")
    descriptor = None
    for klass in railDsl_Platform.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)



def test_raildsl_levelcrossing_is_not_abstract():
    assert not inspect.isabstract(railDsl_LevelCrossing)


def test_raildsl_levelcrossing_constructor_exists():
    assert callable(railDsl_LevelCrossing.__init__)


def test_raildsl_levelcrossing_constructor_args():
    sig = inspect.signature(railDsl_LevelCrossing.__init__)
    params = list(sig.parameters.keys())
    assert "length" in params, "Missing parameter 'length'"
    assert "closed" in params, "Missing parameter 'closed'"

def test_raildsl_levelcrossing_has_length():
    assert hasattr(railDsl_LevelCrossing, "length")
    descriptor = None
    for klass in railDsl_LevelCrossing.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)

def test_raildsl_levelcrossing_has_closed():
    assert hasattr(railDsl_LevelCrossing, "closed")
    descriptor = None
    for klass in railDsl_LevelCrossing.__mro__:
        if "closed" in klass.__dict__:
            descriptor = klass.__dict__["closed"]
            break
    assert isinstance(descriptor, property)



def test_raildsl_derailer_is_not_abstract():
    assert not inspect.isabstract(railDsl_Derailer)


def test_raildsl_derailer_constructor_exists():
    assert callable(railDsl_Derailer.__init__)


def test_raildsl_derailer_constructor_args():
    sig = inspect.signature(railDsl_Derailer.__init__)
    params = list(sig.parameters.keys())
    assert "active" in params, "Missing parameter 'active'"

def test_raildsl_derailer_has_active():
    assert hasattr(railDsl_Derailer, "active")
    descriptor = None
    for klass in railDsl_Derailer.__mro__:
        if "active" in klass.__dict__:
            descriptor = klass.__dict__["active"]
            break
    assert isinstance(descriptor, property)



def test_raildsl_segmentposition_is_not_abstract():
    assert not inspect.isabstract(railDsl_SegmentPosition)


def test_raildsl_segmentposition_constructor_exists():
    assert callable(railDsl_SegmentPosition.__init__)


def test_raildsl_segmentposition_constructor_args():
    sig = inspect.signature(railDsl_SegmentPosition.__init__)
    params = list(sig.parameters.keys())
    assert "atEnd" in params, "Missing parameter 'atEnd'"
    assert "atStart" in params, "Missing parameter 'atStart'"
    assert "side" in params, "Missing parameter 'side'"
    assert "orientation" in params, "Missing parameter 'orientation'"
    assert "position" in params, "Missing parameter 'position'"

def test_raildsl_segmentposition_has_atEnd():
    assert hasattr(railDsl_SegmentPosition, "atEnd")
    descriptor = None
    for klass in railDsl_SegmentPosition.__mro__:
        if "atEnd" in klass.__dict__:
            descriptor = klass.__dict__["atEnd"]
            break
    assert isinstance(descriptor, property)

def test_raildsl_segmentposition_has_atStart():
    assert hasattr(railDsl_SegmentPosition, "atStart")
    descriptor = None
    for klass in railDsl_SegmentPosition.__mro__:
        if "atStart" in klass.__dict__:
            descriptor = klass.__dict__["atStart"]
            break
    assert isinstance(descriptor, property)

def test_raildsl_segmentposition_has_side():
    assert hasattr(railDsl_SegmentPosition, "side")
    descriptor = None
    for klass in railDsl_SegmentPosition.__mro__:
        if "side" in klass.__dict__:
            descriptor = klass.__dict__["side"]
            break
    assert isinstance(descriptor, property)

def test_raildsl_segmentposition_has_orientation():
    assert hasattr(railDsl_SegmentPosition, "orientation")
    descriptor = None
    for klass in railDsl_SegmentPosition.__mro__:
        if "orientation" in klass.__dict__:
            descriptor = klass.__dict__["orientation"]
            break
    assert isinstance(descriptor, property)

def test_raildsl_segmentposition_has_position():
    assert hasattr(railDsl_SegmentPosition, "position")
    descriptor = None
    for klass in railDsl_SegmentPosition.__mro__:
        if "position" in klass.__dict__:
            descriptor = klass.__dict__["position"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_raildsl_station_is_not_abstract():
    assert not inspect.isabstract(railDsl_Station)


def test_raildsl_station_constructor_exists():
    assert callable(railDsl_Station.__init__)


def test_raildsl_station_constructor_args():
    sig = inspect.signature(railDsl_Station.__init__)
    params = list(sig.parameters.keys())



def test_raildsl_declaration_is_not_abstract():
    assert not inspect.isabstract(railDsl_Declaration)


def test_raildsl_declaration_constructor_exists():
    assert callable(railDsl_Declaration.__init__)


def test_raildsl_declaration_constructor_args():
    sig = inspect.signature(railDsl_Declaration.__init__)
    params = list(sig.parameters.keys())



def test_raildsl_segmentobject_is_not_abstract():
    assert not inspect.isabstract(railDsl_SegmentObject)


def test_raildsl_segmentobject_constructor_exists():
    assert callable(railDsl_SegmentObject.__init__)


def test_raildsl_segmentobject_constructor_args():
    sig = inspect.signature(railDsl_SegmentObject.__init__)
    params = list(sig.parameters.keys())

def test_side_exists():
    # Check that the Enumeration exists
    assert Side is not None

def test_side_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Side]
    expected_literals = [
        "Left",
        "Both",
        "Right",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Side"

def test_speedlimit_exists():
    # Check that the Enumeration exists
    assert SpeedLimit is not None

def test_speedlimit_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SpeedLimit]
    expected_literals = [
        "Speed40",
        "Stop",
        "Max",
        "Speed120",
        "Speed80",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SpeedLimit"

def test_vertexkind_exists():
    # Check that the Enumeration exists
    assert VertexKind is not None

def test_vertexkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in VertexKind]
    expected_literals = [
        "TrackEnd",
        "StationBorder",
        "InnerVertex",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in VertexKind"

def test_orientation_exists():
    # Check that the Enumeration exists
    assert Orientation is not None

def test_orientation_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Orientation]
    expected_literals = [
        "Forwards",
        "Backwards",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Orientation"

def test_trainroutekind_exists():
    # Check that the Enumeration exists
    assert TrainRouteKind is not None

def test_trainroutekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TrainRouteKind]
    expected_literals = [
        "Shunting",
        "Main",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TrainRouteKind"

def test_pointkind_exists():
    # Check that the Enumeration exists
    assert PointKind is not None

def test_pointkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PointKind]
    expected_literals = [
        "SimplePoint",
        "DoubleSlipPoint",
        "SingleSlipPoint",
        "DoublePoint",
        "FixedCrossing",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PointKind"


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
railDsl_TrainRouteObject_strategy = st.builds(
    railDsl_TrainRouteObject,
    speedLimit=
        safe_text
)
railDsl_RouteObject_strategy = st.builds(
    railDsl_RouteObject,
    error=
        st.booleans(),
    speedLimit=
        safe_text
)
TrainRouteObject_strategy = st.builds(
    TrainRouteObject,
)
railDsl_TrainRouteSegment_strategy = st.builds(
    railDsl_TrainRouteSegment,
)
railDsl_TrainRoutePoint_strategy = st.builds(
    railDsl_TrainRoutePoint,
    selectedOutput=
        st.integers(),
    selectedInput=
        st.integers()
)
railDsl_TrainSegment_strategy = st.builds(
    railDsl_TrainSegment,
    length=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
railDsl_NamedElement_strategy = st.builds(
    railDsl_NamedElement,
    name=
        safe_text
)
TrackObject_strategy = st.builds(
    TrackObject,
)
railDsl_Point_strategy = st.builds(
    railDsl_Point,
    locked=
        st.booleans(),
    kind=
        safe_text,
    selectedOutput=
        st.integers(),
    selectedInput=
        st.integers()
)
railDsl_Segment_strategy = st.builds(
    railDsl_Segment,
)
RouteObject_strategy = st.builds(
    RouteObject,
)
Declaration_strategy = st.builds(
    Declaration,
)
railDsl_Vertex_strategy = st.builds(
    railDsl_Vertex,
    kind=
        safe_text
)
railDsl_TrainRoute_strategy = st.builds(
    railDsl_TrainRoute,
    kind=
        safe_text,
    locked=
        st.booleans()
)
railDsl_Track_strategy = st.builds(
    railDsl_Track,
)
railDsl_Train_strategy = st.builds(
    railDsl_Train,
    speed=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    acceleration=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    length=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
railDsl_TrackObject_strategy = st.builds(
    railDsl_TrackObject,
    length=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
SegmentObject_strategy = st.builds(
    SegmentObject,
)
railDsl_Signal_strategy = st.builds(
    railDsl_Signal,
    shunting=
        st.booleans(),
    main=
        st.booleans()
)
railDsl_Platform_strategy = st.builds(
    railDsl_Platform,
    length=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
railDsl_LevelCrossing_strategy = st.builds(
    railDsl_LevelCrossing,
    length=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    closed=
        st.booleans()
)
railDsl_Derailer_strategy = st.builds(
    railDsl_Derailer,
    active=
        st.booleans()
)
railDsl_SegmentPosition_strategy = st.builds(
    railDsl_SegmentPosition,
    atEnd=
        st.booleans(),
    atStart=
        st.booleans(),
    side=
        safe_text,
    orientation=
        safe_text,
    position=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
NamedElement_strategy = st.builds(
    NamedElement,
)
railDsl_Station_strategy = st.builds(
    railDsl_Station,
)
railDsl_Declaration_strategy = st.builds(
    railDsl_Declaration,
)
railDsl_SegmentObject_strategy = st.builds(
    railDsl_SegmentObject,
)

@given(instance=railDsl_TrainRouteObject_strategy)
@settings(max_examples=50)
def test_raildsl_trainrouteobject_instantiation(instance):
    assert isinstance(instance, railDsl_TrainRouteObject)



@given(instance=railDsl_TrainRouteObject_strategy)
def test_raildsl_trainrouteobject_speedLimit_setter(instance):
    original = instance.speedLimit
    instance.speedLimit = original
    assert instance.speedLimit == original

@given(instance=railDsl_RouteObject_strategy)
@settings(max_examples=50)
def test_raildsl_routeobject_instantiation(instance):
    assert isinstance(instance, railDsl_RouteObject)



@given(instance=railDsl_RouteObject_strategy)
def test_raildsl_routeobject_error_setter(instance):
    original = instance.error
    instance.error = original
    assert instance.error == original



@given(instance=railDsl_RouteObject_strategy)
def test_raildsl_routeobject_speedLimit_setter(instance):
    original = instance.speedLimit
    instance.speedLimit = original
    assert instance.speedLimit == original

@given(instance=TrainRouteObject_strategy)
@settings(max_examples=50)
def test_trainrouteobject_instantiation(instance):
    assert isinstance(instance, TrainRouteObject)

@given(instance=railDsl_TrainRouteSegment_strategy)
@settings(max_examples=50)
def test_raildsl_trainroutesegment_instantiation(instance):
    assert isinstance(instance, railDsl_TrainRouteSegment)

@given(instance=railDsl_TrainRoutePoint_strategy)
@settings(max_examples=50)
def test_raildsl_trainroutepoint_instantiation(instance):
    assert isinstance(instance, railDsl_TrainRoutePoint)



@given(instance=railDsl_TrainRoutePoint_strategy)
def test_raildsl_trainroutepoint_selectedOutput_setter(instance):
    original = instance.selectedOutput
    instance.selectedOutput = original
    assert instance.selectedOutput == original



@given(instance=railDsl_TrainRoutePoint_strategy)
def test_raildsl_trainroutepoint_selectedInput_setter(instance):
    original = instance.selectedInput
    instance.selectedInput = original
    assert instance.selectedInput == original

@given(instance=railDsl_TrainSegment_strategy)
@settings(max_examples=50)
def test_raildsl_trainsegment_instantiation(instance):
    assert isinstance(instance, railDsl_TrainSegment)



@given(instance=railDsl_TrainSegment_strategy)
def test_raildsl_trainsegment_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original

@given(instance=railDsl_NamedElement_strategy)
@settings(max_examples=50)
def test_raildsl_namedelement_instantiation(instance):
    assert isinstance(instance, railDsl_NamedElement)



@given(instance=railDsl_NamedElement_strategy)
def test_raildsl_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=TrackObject_strategy)
@settings(max_examples=50)
def test_trackobject_instantiation(instance):
    assert isinstance(instance, TrackObject)

@given(instance=railDsl_Point_strategy)
@settings(max_examples=50)
def test_raildsl_point_instantiation(instance):
    assert isinstance(instance, railDsl_Point)



@given(instance=railDsl_Point_strategy)
def test_raildsl_point_locked_setter(instance):
    original = instance.locked
    instance.locked = original
    assert instance.locked == original



@given(instance=railDsl_Point_strategy)
def test_raildsl_point_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original



@given(instance=railDsl_Point_strategy)
def test_raildsl_point_selectedOutput_setter(instance):
    original = instance.selectedOutput
    instance.selectedOutput = original
    assert instance.selectedOutput == original



@given(instance=railDsl_Point_strategy)
def test_raildsl_point_selectedInput_setter(instance):
    original = instance.selectedInput
    instance.selectedInput = original
    assert instance.selectedInput == original

@given(instance=railDsl_Segment_strategy)
@settings(max_examples=50)
def test_raildsl_segment_instantiation(instance):
    assert isinstance(instance, railDsl_Segment)

@given(instance=RouteObject_strategy)
@settings(max_examples=50)
def test_routeobject_instantiation(instance):
    assert isinstance(instance, RouteObject)

@given(instance=Declaration_strategy)
@settings(max_examples=50)
def test_declaration_instantiation(instance):
    assert isinstance(instance, Declaration)

@given(instance=railDsl_Vertex_strategy)
@settings(max_examples=50)
def test_raildsl_vertex_instantiation(instance):
    assert isinstance(instance, railDsl_Vertex)



@given(instance=railDsl_Vertex_strategy)
def test_raildsl_vertex_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=railDsl_TrainRoute_strategy)
@settings(max_examples=50)
def test_raildsl_trainroute_instantiation(instance):
    assert isinstance(instance, railDsl_TrainRoute)



@given(instance=railDsl_TrainRoute_strategy)
def test_raildsl_trainroute_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original



@given(instance=railDsl_TrainRoute_strategy)
def test_raildsl_trainroute_locked_setter(instance):
    original = instance.locked
    instance.locked = original
    assert instance.locked == original

@given(instance=railDsl_Track_strategy)
@settings(max_examples=50)
def test_raildsl_track_instantiation(instance):
    assert isinstance(instance, railDsl_Track)

@given(instance=railDsl_Train_strategy)
@settings(max_examples=50)
def test_raildsl_train_instantiation(instance):
    assert isinstance(instance, railDsl_Train)



@given(instance=railDsl_Train_strategy)
def test_raildsl_train_speed_setter(instance):
    original = instance.speed
    instance.speed = original
    assert instance.speed == original



@given(instance=railDsl_Train_strategy)
def test_raildsl_train_acceleration_setter(instance):
    original = instance.acceleration
    instance.acceleration = original
    assert instance.acceleration == original



@given(instance=railDsl_Train_strategy)
def test_raildsl_train_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original

@given(instance=railDsl_TrackObject_strategy)
@settings(max_examples=50)
def test_raildsl_trackobject_instantiation(instance):
    assert isinstance(instance, railDsl_TrackObject)



@given(instance=railDsl_TrackObject_strategy)
def test_raildsl_trackobject_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original

@given(instance=SegmentObject_strategy)
@settings(max_examples=50)
def test_segmentobject_instantiation(instance):
    assert isinstance(instance, SegmentObject)

@given(instance=railDsl_Signal_strategy)
@settings(max_examples=50)
def test_raildsl_signal_instantiation(instance):
    assert isinstance(instance, railDsl_Signal)



@given(instance=railDsl_Signal_strategy)
def test_raildsl_signal_shunting_setter(instance):
    original = instance.shunting
    instance.shunting = original
    assert instance.shunting == original



@given(instance=railDsl_Signal_strategy)
def test_raildsl_signal_main_setter(instance):
    original = instance.main
    instance.main = original
    assert instance.main == original

@given(instance=railDsl_Platform_strategy)
@settings(max_examples=50)
def test_raildsl_platform_instantiation(instance):
    assert isinstance(instance, railDsl_Platform)



@given(instance=railDsl_Platform_strategy)
def test_raildsl_platform_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original

@given(instance=railDsl_LevelCrossing_strategy)
@settings(max_examples=50)
def test_raildsl_levelcrossing_instantiation(instance):
    assert isinstance(instance, railDsl_LevelCrossing)



@given(instance=railDsl_LevelCrossing_strategy)
def test_raildsl_levelcrossing_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original



@given(instance=railDsl_LevelCrossing_strategy)
def test_raildsl_levelcrossing_closed_setter(instance):
    original = instance.closed
    instance.closed = original
    assert instance.closed == original

@given(instance=railDsl_Derailer_strategy)
@settings(max_examples=50)
def test_raildsl_derailer_instantiation(instance):
    assert isinstance(instance, railDsl_Derailer)



@given(instance=railDsl_Derailer_strategy)
def test_raildsl_derailer_active_setter(instance):
    original = instance.active
    instance.active = original
    assert instance.active == original

@given(instance=railDsl_SegmentPosition_strategy)
@settings(max_examples=50)
def test_raildsl_segmentposition_instantiation(instance):
    assert isinstance(instance, railDsl_SegmentPosition)



@given(instance=railDsl_SegmentPosition_strategy)
def test_raildsl_segmentposition_atEnd_setter(instance):
    original = instance.atEnd
    instance.atEnd = original
    assert instance.atEnd == original



@given(instance=railDsl_SegmentPosition_strategy)
def test_raildsl_segmentposition_atStart_setter(instance):
    original = instance.atStart
    instance.atStart = original
    assert instance.atStart == original



@given(instance=railDsl_SegmentPosition_strategy)
def test_raildsl_segmentposition_side_setter(instance):
    original = instance.side
    instance.side = original
    assert instance.side == original



@given(instance=railDsl_SegmentPosition_strategy)
def test_raildsl_segmentposition_orientation_setter(instance):
    original = instance.orientation
    instance.orientation = original
    assert instance.orientation == original



@given(instance=railDsl_SegmentPosition_strategy)
def test_raildsl_segmentposition_position_setter(instance):
    original = instance.position
    instance.position = original
    assert instance.position == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=railDsl_Station_strategy)
@settings(max_examples=50)
def test_raildsl_station_instantiation(instance):
    assert isinstance(instance, railDsl_Station)

@given(instance=railDsl_Declaration_strategy)
@settings(max_examples=50)
def test_raildsl_declaration_instantiation(instance):
    assert isinstance(instance, railDsl_Declaration)

@given(instance=railDsl_SegmentObject_strategy)
@settings(max_examples=50)
def test_raildsl_segmentobject_instantiation(instance):
    assert isinstance(instance, railDsl_SegmentObject)
