import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    railDsl::TrainRouteObject,
    railDsl::RouteObject,
    TrainRouteObject,
    railDsl::TrainRouteSegment,
    railDsl::TrainRoutePoint,
    railDsl::TrainSegment,
    railDsl::NamedElement,
    TrackObject,
    railDsl::Point,
    railDsl::Segment,
    RouteObject,
    Declaration,
    railDsl::Train,
    railDsl::Track,
    railDsl::TrainRoute,
    railDsl::Vertex,
    railDsl::TrackObject,
    SegmentObject,
    railDsl::LevelCrossing,
    railDsl::Platform,
    railDsl::Signal,
    railDsl::Derailer,
    railDsl::SegmentPosition,
    NamedElement,
    railDsl::SegmentObject,
    railDsl::Declaration,
    railDsl::Station,
    PointKind,
    SpeedLimit,
    Orientation,
    Side,
    TrainRouteKind,
    VertexKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_raildsl::trainrouteobject_is_not_abstract():
    assert not inspect.isabstract(railDsl::TrainRouteObject)


def test_raildsl::trainrouteobject_constructor_exists():
    assert callable(railDsl::TrainRouteObject.__init__)


def test_raildsl::trainrouteobject_constructor_args():
    sig = inspect.signature(railDsl::TrainRouteObject.__init__)
    params = list(sig.parameters.keys())
    assert "speedLimit" in params, "Missing parameter 'speedLimit'"

def test_raildsl::trainrouteobject_has_speedLimit():
    assert hasattr(railDsl::TrainRouteObject, "speedLimit")
    descriptor = None
    for klass in railDsl::TrainRouteObject.__mro__:
        if "speedLimit" in klass.__dict__:
            descriptor = klass.__dict__["speedLimit"]
            break
    assert isinstance(descriptor, property)



def test_raildsl::routeobject_is_not_abstract():
    assert not inspect.isabstract(railDsl::RouteObject)


def test_raildsl::routeobject_constructor_exists():
    assert callable(railDsl::RouteObject.__init__)


def test_raildsl::routeobject_constructor_args():
    sig = inspect.signature(railDsl::RouteObject.__init__)
    params = list(sig.parameters.keys())
    assert "speedLimit" in params, "Missing parameter 'speedLimit'"
    assert "error" in params, "Missing parameter 'error'"

def test_raildsl::routeobject_has_speedLimit():
    assert hasattr(railDsl::RouteObject, "speedLimit")
    descriptor = None
    for klass in railDsl::RouteObject.__mro__:
        if "speedLimit" in klass.__dict__:
            descriptor = klass.__dict__["speedLimit"]
            break
    assert isinstance(descriptor, property)

def test_raildsl::routeobject_has_error():
    assert hasattr(railDsl::RouteObject, "error")
    descriptor = None
    for klass in railDsl::RouteObject.__mro__:
        if "error" in klass.__dict__:
            descriptor = klass.__dict__["error"]
            break
    assert isinstance(descriptor, property)



def test_trainrouteobject_is_not_abstract():
    assert not inspect.isabstract(TrainRouteObject)


def test_trainrouteobject_constructor_exists():
    assert callable(TrainRouteObject.__init__)


def test_trainrouteobject_constructor_args():
    sig = inspect.signature(TrainRouteObject.__init__)
    params = list(sig.parameters.keys())



def test_raildsl::trainroutesegment_is_not_abstract():
    assert not inspect.isabstract(railDsl::TrainRouteSegment)


def test_raildsl::trainroutesegment_constructor_exists():
    assert callable(railDsl::TrainRouteSegment.__init__)


def test_raildsl::trainroutesegment_constructor_args():
    sig = inspect.signature(railDsl::TrainRouteSegment.__init__)
    params = list(sig.parameters.keys())



def test_raildsl::trainroutepoint_is_not_abstract():
    assert not inspect.isabstract(railDsl::TrainRoutePoint)


def test_raildsl::trainroutepoint_constructor_exists():
    assert callable(railDsl::TrainRoutePoint.__init__)


def test_raildsl::trainroutepoint_constructor_args():
    sig = inspect.signature(railDsl::TrainRoutePoint.__init__)
    params = list(sig.parameters.keys())
    assert "selectedInput" in params, "Missing parameter 'selectedInput'"
    assert "selectedOutput" in params, "Missing parameter 'selectedOutput'"

def test_raildsl::trainroutepoint_has_selectedInput():
    assert hasattr(railDsl::TrainRoutePoint, "selectedInput")
    descriptor = None
    for klass in railDsl::TrainRoutePoint.__mro__:
        if "selectedInput" in klass.__dict__:
            descriptor = klass.__dict__["selectedInput"]
            break
    assert isinstance(descriptor, property)

def test_raildsl::trainroutepoint_has_selectedOutput():
    assert hasattr(railDsl::TrainRoutePoint, "selectedOutput")
    descriptor = None
    for klass in railDsl::TrainRoutePoint.__mro__:
        if "selectedOutput" in klass.__dict__:
            descriptor = klass.__dict__["selectedOutput"]
            break
    assert isinstance(descriptor, property)



def test_raildsl::trainsegment_is_not_abstract():
    assert not inspect.isabstract(railDsl::TrainSegment)


def test_raildsl::trainsegment_constructor_exists():
    assert callable(railDsl::TrainSegment.__init__)


def test_raildsl::trainsegment_constructor_args():
    sig = inspect.signature(railDsl::TrainSegment.__init__)
    params = list(sig.parameters.keys())
    assert "length" in params, "Missing parameter 'length'"

def test_raildsl::trainsegment_has_length():
    assert hasattr(railDsl::TrainSegment, "length")
    descriptor = None
    for klass in railDsl::TrainSegment.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)



def test_raildsl::namedelement_is_not_abstract():
    assert not inspect.isabstract(railDsl::NamedElement)


def test_raildsl::namedelement_constructor_exists():
    assert callable(railDsl::NamedElement.__init__)


def test_raildsl::namedelement_constructor_args():
    sig = inspect.signature(railDsl::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_raildsl::namedelement_has_name():
    assert hasattr(railDsl::NamedElement, "name")
    descriptor = None
    for klass in railDsl::NamedElement.__mro__:
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



def test_raildsl::point_is_not_abstract():
    assert not inspect.isabstract(railDsl::Point)


def test_raildsl::point_constructor_exists():
    assert callable(railDsl::Point.__init__)


def test_raildsl::point_constructor_args():
    sig = inspect.signature(railDsl::Point.__init__)
    params = list(sig.parameters.keys())
    assert "selectedInput" in params, "Missing parameter 'selectedInput'"
    assert "selectedOutput" in params, "Missing parameter 'selectedOutput'"
    assert "locked" in params, "Missing parameter 'locked'"
    assert "kind" in params, "Missing parameter 'kind'"

def test_raildsl::point_has_selectedInput():
    assert hasattr(railDsl::Point, "selectedInput")
    descriptor = None
    for klass in railDsl::Point.__mro__:
        if "selectedInput" in klass.__dict__:
            descriptor = klass.__dict__["selectedInput"]
            break
    assert isinstance(descriptor, property)

def test_raildsl::point_has_selectedOutput():
    assert hasattr(railDsl::Point, "selectedOutput")
    descriptor = None
    for klass in railDsl::Point.__mro__:
        if "selectedOutput" in klass.__dict__:
            descriptor = klass.__dict__["selectedOutput"]
            break
    assert isinstance(descriptor, property)

def test_raildsl::point_has_locked():
    assert hasattr(railDsl::Point, "locked")
    descriptor = None
    for klass in railDsl::Point.__mro__:
        if "locked" in klass.__dict__:
            descriptor = klass.__dict__["locked"]
            break
    assert isinstance(descriptor, property)

def test_raildsl::point_has_kind():
    assert hasattr(railDsl::Point, "kind")
    descriptor = None
    for klass in railDsl::Point.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_raildsl::segment_is_not_abstract():
    assert not inspect.isabstract(railDsl::Segment)


def test_raildsl::segment_constructor_exists():
    assert callable(railDsl::Segment.__init__)


def test_raildsl::segment_constructor_args():
    sig = inspect.signature(railDsl::Segment.__init__)
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



def test_raildsl::train_is_not_abstract():
    assert not inspect.isabstract(railDsl::Train)


def test_raildsl::train_constructor_exists():
    assert callable(railDsl::Train.__init__)


def test_raildsl::train_constructor_args():
    sig = inspect.signature(railDsl::Train.__init__)
    params = list(sig.parameters.keys())
    assert "acceleration" in params, "Missing parameter 'acceleration'"
    assert "length" in params, "Missing parameter 'length'"
    assert "speed" in params, "Missing parameter 'speed'"

def test_raildsl::train_has_acceleration():
    assert hasattr(railDsl::Train, "acceleration")
    descriptor = None
    for klass in railDsl::Train.__mro__:
        if "acceleration" in klass.__dict__:
            descriptor = klass.__dict__["acceleration"]
            break
    assert isinstance(descriptor, property)

def test_raildsl::train_has_length():
    assert hasattr(railDsl::Train, "length")
    descriptor = None
    for klass in railDsl::Train.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)

def test_raildsl::train_has_speed():
    assert hasattr(railDsl::Train, "speed")
    descriptor = None
    for klass in railDsl::Train.__mro__:
        if "speed" in klass.__dict__:
            descriptor = klass.__dict__["speed"]
            break
    assert isinstance(descriptor, property)



def test_raildsl::track_is_not_abstract():
    assert not inspect.isabstract(railDsl::Track)


def test_raildsl::track_constructor_exists():
    assert callable(railDsl::Track.__init__)


def test_raildsl::track_constructor_args():
    sig = inspect.signature(railDsl::Track.__init__)
    params = list(sig.parameters.keys())



def test_raildsl::trainroute_is_not_abstract():
    assert not inspect.isabstract(railDsl::TrainRoute)


def test_raildsl::trainroute_constructor_exists():
    assert callable(railDsl::TrainRoute.__init__)


def test_raildsl::trainroute_constructor_args():
    sig = inspect.signature(railDsl::TrainRoute.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"
    assert "locked" in params, "Missing parameter 'locked'"

def test_raildsl::trainroute_has_kind():
    assert hasattr(railDsl::TrainRoute, "kind")
    descriptor = None
    for klass in railDsl::TrainRoute.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)

def test_raildsl::trainroute_has_locked():
    assert hasattr(railDsl::TrainRoute, "locked")
    descriptor = None
    for klass in railDsl::TrainRoute.__mro__:
        if "locked" in klass.__dict__:
            descriptor = klass.__dict__["locked"]
            break
    assert isinstance(descriptor, property)



def test_raildsl::vertex_is_not_abstract():
    assert not inspect.isabstract(railDsl::Vertex)


def test_raildsl::vertex_constructor_exists():
    assert callable(railDsl::Vertex.__init__)


def test_raildsl::vertex_constructor_args():
    sig = inspect.signature(railDsl::Vertex.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_raildsl::vertex_has_kind():
    assert hasattr(railDsl::Vertex, "kind")
    descriptor = None
    for klass in railDsl::Vertex.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_raildsl::trackobject_is_not_abstract():
    assert not inspect.isabstract(railDsl::TrackObject)


def test_raildsl::trackobject_constructor_exists():
    assert callable(railDsl::TrackObject.__init__)


def test_raildsl::trackobject_constructor_args():
    sig = inspect.signature(railDsl::TrackObject.__init__)
    params = list(sig.parameters.keys())
    assert "length" in params, "Missing parameter 'length'"

def test_raildsl::trackobject_has_length():
    assert hasattr(railDsl::TrackObject, "length")
    descriptor = None
    for klass in railDsl::TrackObject.__mro__:
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



def test_raildsl::levelcrossing_is_not_abstract():
    assert not inspect.isabstract(railDsl::LevelCrossing)


def test_raildsl::levelcrossing_constructor_exists():
    assert callable(railDsl::LevelCrossing.__init__)


def test_raildsl::levelcrossing_constructor_args():
    sig = inspect.signature(railDsl::LevelCrossing.__init__)
    params = list(sig.parameters.keys())
    assert "length" in params, "Missing parameter 'length'"
    assert "closed" in params, "Missing parameter 'closed'"

def test_raildsl::levelcrossing_has_length():
    assert hasattr(railDsl::LevelCrossing, "length")
    descriptor = None
    for klass in railDsl::LevelCrossing.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)

def test_raildsl::levelcrossing_has_closed():
    assert hasattr(railDsl::LevelCrossing, "closed")
    descriptor = None
    for klass in railDsl::LevelCrossing.__mro__:
        if "closed" in klass.__dict__:
            descriptor = klass.__dict__["closed"]
            break
    assert isinstance(descriptor, property)



def test_raildsl::platform_is_not_abstract():
    assert not inspect.isabstract(railDsl::Platform)


def test_raildsl::platform_constructor_exists():
    assert callable(railDsl::Platform.__init__)


def test_raildsl::platform_constructor_args():
    sig = inspect.signature(railDsl::Platform.__init__)
    params = list(sig.parameters.keys())
    assert "length" in params, "Missing parameter 'length'"

def test_raildsl::platform_has_length():
    assert hasattr(railDsl::Platform, "length")
    descriptor = None
    for klass in railDsl::Platform.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)



def test_raildsl::signal_is_not_abstract():
    assert not inspect.isabstract(railDsl::Signal)


def test_raildsl::signal_constructor_exists():
    assert callable(railDsl::Signal.__init__)


def test_raildsl::signal_constructor_args():
    sig = inspect.signature(railDsl::Signal.__init__)
    params = list(sig.parameters.keys())
    assert "shunting" in params, "Missing parameter 'shunting'"
    assert "main" in params, "Missing parameter 'main'"

def test_raildsl::signal_has_shunting():
    assert hasattr(railDsl::Signal, "shunting")
    descriptor = None
    for klass in railDsl::Signal.__mro__:
        if "shunting" in klass.__dict__:
            descriptor = klass.__dict__["shunting"]
            break
    assert isinstance(descriptor, property)

def test_raildsl::signal_has_main():
    assert hasattr(railDsl::Signal, "main")
    descriptor = None
    for klass in railDsl::Signal.__mro__:
        if "main" in klass.__dict__:
            descriptor = klass.__dict__["main"]
            break
    assert isinstance(descriptor, property)



def test_raildsl::derailer_is_not_abstract():
    assert not inspect.isabstract(railDsl::Derailer)


def test_raildsl::derailer_constructor_exists():
    assert callable(railDsl::Derailer.__init__)


def test_raildsl::derailer_constructor_args():
    sig = inspect.signature(railDsl::Derailer.__init__)
    params = list(sig.parameters.keys())
    assert "active" in params, "Missing parameter 'active'"

def test_raildsl::derailer_has_active():
    assert hasattr(railDsl::Derailer, "active")
    descriptor = None
    for klass in railDsl::Derailer.__mro__:
        if "active" in klass.__dict__:
            descriptor = klass.__dict__["active"]
            break
    assert isinstance(descriptor, property)



def test_raildsl::segmentposition_is_not_abstract():
    assert not inspect.isabstract(railDsl::SegmentPosition)


def test_raildsl::segmentposition_constructor_exists():
    assert callable(railDsl::SegmentPosition.__init__)


def test_raildsl::segmentposition_constructor_args():
    sig = inspect.signature(railDsl::SegmentPosition.__init__)
    params = list(sig.parameters.keys())
    assert "side" in params, "Missing parameter 'side'"
    assert "position" in params, "Missing parameter 'position'"
    assert "atEnd" in params, "Missing parameter 'atEnd'"
    assert "atStart" in params, "Missing parameter 'atStart'"
    assert "orientation" in params, "Missing parameter 'orientation'"

def test_raildsl::segmentposition_has_side():
    assert hasattr(railDsl::SegmentPosition, "side")
    descriptor = None
    for klass in railDsl::SegmentPosition.__mro__:
        if "side" in klass.__dict__:
            descriptor = klass.__dict__["side"]
            break
    assert isinstance(descriptor, property)

def test_raildsl::segmentposition_has_position():
    assert hasattr(railDsl::SegmentPosition, "position")
    descriptor = None
    for klass in railDsl::SegmentPosition.__mro__:
        if "position" in klass.__dict__:
            descriptor = klass.__dict__["position"]
            break
    assert isinstance(descriptor, property)

def test_raildsl::segmentposition_has_atEnd():
    assert hasattr(railDsl::SegmentPosition, "atEnd")
    descriptor = None
    for klass in railDsl::SegmentPosition.__mro__:
        if "atEnd" in klass.__dict__:
            descriptor = klass.__dict__["atEnd"]
            break
    assert isinstance(descriptor, property)

def test_raildsl::segmentposition_has_atStart():
    assert hasattr(railDsl::SegmentPosition, "atStart")
    descriptor = None
    for klass in railDsl::SegmentPosition.__mro__:
        if "atStart" in klass.__dict__:
            descriptor = klass.__dict__["atStart"]
            break
    assert isinstance(descriptor, property)

def test_raildsl::segmentposition_has_orientation():
    assert hasattr(railDsl::SegmentPosition, "orientation")
    descriptor = None
    for klass in railDsl::SegmentPosition.__mro__:
        if "orientation" in klass.__dict__:
            descriptor = klass.__dict__["orientation"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_raildsl::segmentobject_is_not_abstract():
    assert not inspect.isabstract(railDsl::SegmentObject)


def test_raildsl::segmentobject_constructor_exists():
    assert callable(railDsl::SegmentObject.__init__)


def test_raildsl::segmentobject_constructor_args():
    sig = inspect.signature(railDsl::SegmentObject.__init__)
    params = list(sig.parameters.keys())



def test_raildsl::declaration_is_not_abstract():
    assert not inspect.isabstract(railDsl::Declaration)


def test_raildsl::declaration_constructor_exists():
    assert callable(railDsl::Declaration.__init__)


def test_raildsl::declaration_constructor_args():
    sig = inspect.signature(railDsl::Declaration.__init__)
    params = list(sig.parameters.keys())



def test_raildsl::station_is_not_abstract():
    assert not inspect.isabstract(railDsl::Station)


def test_raildsl::station_constructor_exists():
    assert callable(railDsl::Station.__init__)


def test_raildsl::station_constructor_args():
    sig = inspect.signature(railDsl::Station.__init__)
    params = list(sig.parameters.keys())

def test_pointkind_exists():
    # Check that the Enumeration exists
    assert PointKind is not None

def test_pointkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PointKind]
    expected_literals = [
        "FixedCrossing",
        "DoublePoint",
        "DoubleSlipPoint",
        "SimplePoint",
        "SingleSlipPoint",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PointKind"

def test_speedlimit_exists():
    # Check that the Enumeration exists
    assert SpeedLimit is not None

def test_speedlimit_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SpeedLimit]
    expected_literals = [
        "Stop",
        "Speed80",
        "Max",
        "Speed120",
        "Speed40",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SpeedLimit"

def test_orientation_exists():
    # Check that the Enumeration exists
    assert Orientation is not None

def test_orientation_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Orientation]
    expected_literals = [
        "Backwards",
        "Forwards",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Orientation"

def test_side_exists():
    # Check that the Enumeration exists
    assert Side is not None

def test_side_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Side]
    expected_literals = [
        "Left",
        "Right",
        "Both",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Side"

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

def test_vertexkind_exists():
    # Check that the Enumeration exists
    assert VertexKind is not None

def test_vertexkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in VertexKind]
    expected_literals = [
        "StationBorder",
        "InnerVertex",
        "TrackEnd",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in VertexKind"


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
railDsl::TrainRouteObject_strategy = st.builds(
    railDsl::TrainRouteObject,
    speedLimit=
        safe_text
)
railDsl::RouteObject_strategy = st.builds(
    railDsl::RouteObject,
    speedLimit=
        safe_text,
    error=
        st.booleans()
)
TrainRouteObject_strategy = st.builds(
    TrainRouteObject,
)
railDsl::TrainRouteSegment_strategy = st.builds(
    railDsl::TrainRouteSegment,
)
railDsl::TrainRoutePoint_strategy = st.builds(
    railDsl::TrainRoutePoint,
    selectedInput=
        st.integers(),
    selectedOutput=
        st.integers()
)
railDsl::TrainSegment_strategy = st.builds(
    railDsl::TrainSegment,
    length=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
railDsl::NamedElement_strategy = st.builds(
    railDsl::NamedElement,
    name=
        safe_text
)
TrackObject_strategy = st.builds(
    TrackObject,
)
railDsl::Point_strategy = st.builds(
    railDsl::Point,
    selectedInput=
        st.integers(),
    selectedOutput=
        st.integers(),
    locked=
        st.booleans(),
    kind=
        safe_text
)
railDsl::Segment_strategy = st.builds(
    railDsl::Segment,
)
RouteObject_strategy = st.builds(
    RouteObject,
)
Declaration_strategy = st.builds(
    Declaration,
)
railDsl::Train_strategy = st.builds(
    railDsl::Train,
    acceleration=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    length=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    speed=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
railDsl::Track_strategy = st.builds(
    railDsl::Track,
)
railDsl::TrainRoute_strategy = st.builds(
    railDsl::TrainRoute,
    kind=
        safe_text,
    locked=
        st.booleans()
)
railDsl::Vertex_strategy = st.builds(
    railDsl::Vertex,
    kind=
        safe_text
)
railDsl::TrackObject_strategy = st.builds(
    railDsl::TrackObject,
    length=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
SegmentObject_strategy = st.builds(
    SegmentObject,
)
railDsl::LevelCrossing_strategy = st.builds(
    railDsl::LevelCrossing,
    length=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    closed=
        st.booleans()
)
railDsl::Platform_strategy = st.builds(
    railDsl::Platform,
    length=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
railDsl::Signal_strategy = st.builds(
    railDsl::Signal,
    shunting=
        st.booleans(),
    main=
        st.booleans()
)
railDsl::Derailer_strategy = st.builds(
    railDsl::Derailer,
    active=
        st.booleans()
)
railDsl::SegmentPosition_strategy = st.builds(
    railDsl::SegmentPosition,
    side=
        safe_text,
    position=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    atEnd=
        st.booleans(),
    atStart=
        st.booleans(),
    orientation=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
railDsl::SegmentObject_strategy = st.builds(
    railDsl::SegmentObject,
)
railDsl::Declaration_strategy = st.builds(
    railDsl::Declaration,
)
railDsl::Station_strategy = st.builds(
    railDsl::Station,
)

@given(instance=railDsl::TrainRouteObject_strategy)
@settings(max_examples=50)
def test_raildsl::trainrouteobject_instantiation(instance):
    assert isinstance(instance, railDsl::TrainRouteObject)

@given(instance=railDsl::TrainRouteObject_strategy)
def test_raildsl::trainrouteobject_speedLimit_type(instance):
    assert isinstance(instance.speedLimit, str)


@given(instance=railDsl::TrainRouteObject_strategy)
def test_raildsl::trainrouteobject_speedLimit_setter(instance):
    original = instance.speedLimit
    instance.speedLimit = original
    assert instance.speedLimit == original

@given(instance=railDsl::RouteObject_strategy)
@settings(max_examples=50)
def test_raildsl::routeobject_instantiation(instance):
    assert isinstance(instance, railDsl::RouteObject)

@given(instance=railDsl::RouteObject_strategy)
def test_raildsl::routeobject_speedLimit_type(instance):
    assert isinstance(instance.speedLimit, str)


@given(instance=railDsl::RouteObject_strategy)
def test_raildsl::routeobject_speedLimit_setter(instance):
    original = instance.speedLimit
    instance.speedLimit = original
    assert instance.speedLimit == original

@given(instance=railDsl::RouteObject_strategy)
def test_raildsl::routeobject_error_type(instance):
    assert isinstance(instance.error, bool)


@given(instance=railDsl::RouteObject_strategy)
def test_raildsl::routeobject_error_setter(instance):
    original = instance.error
    instance.error = original
    assert instance.error == original

@given(instance=TrainRouteObject_strategy)
@settings(max_examples=50)
def test_trainrouteobject_instantiation(instance):
    assert isinstance(instance, TrainRouteObject)

@given(instance=railDsl::TrainRouteSegment_strategy)
@settings(max_examples=50)
def test_raildsl::trainroutesegment_instantiation(instance):
    assert isinstance(instance, railDsl::TrainRouteSegment)

@given(instance=railDsl::TrainRoutePoint_strategy)
@settings(max_examples=50)
def test_raildsl::trainroutepoint_instantiation(instance):
    assert isinstance(instance, railDsl::TrainRoutePoint)

@given(instance=railDsl::TrainRoutePoint_strategy)
def test_raildsl::trainroutepoint_selectedInput_type(instance):
    assert isinstance(instance.selectedInput, int)


@given(instance=railDsl::TrainRoutePoint_strategy)
def test_raildsl::trainroutepoint_selectedInput_setter(instance):
    original = instance.selectedInput
    instance.selectedInput = original
    assert instance.selectedInput == original

@given(instance=railDsl::TrainRoutePoint_strategy)
def test_raildsl::trainroutepoint_selectedOutput_type(instance):
    assert isinstance(instance.selectedOutput, int)


@given(instance=railDsl::TrainRoutePoint_strategy)
def test_raildsl::trainroutepoint_selectedOutput_setter(instance):
    original = instance.selectedOutput
    instance.selectedOutput = original
    assert instance.selectedOutput == original

@given(instance=railDsl::TrainSegment_strategy)
@settings(max_examples=50)
def test_raildsl::trainsegment_instantiation(instance):
    assert isinstance(instance, railDsl::TrainSegment)

@given(instance=railDsl::TrainSegment_strategy)
def test_raildsl::trainsegment_length_type(instance):
    assert isinstance(instance.length, float)


@given(instance=railDsl::TrainSegment_strategy)
def test_raildsl::trainsegment_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original

@given(instance=railDsl::NamedElement_strategy)
@settings(max_examples=50)
def test_raildsl::namedelement_instantiation(instance):
    assert isinstance(instance, railDsl::NamedElement)

@given(instance=railDsl::NamedElement_strategy)
def test_raildsl::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=railDsl::NamedElement_strategy)
def test_raildsl::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=TrackObject_strategy)
@settings(max_examples=50)
def test_trackobject_instantiation(instance):
    assert isinstance(instance, TrackObject)

@given(instance=railDsl::Point_strategy)
@settings(max_examples=50)
def test_raildsl::point_instantiation(instance):
    assert isinstance(instance, railDsl::Point)

@given(instance=railDsl::Point_strategy)
def test_raildsl::point_selectedInput_type(instance):
    assert isinstance(instance.selectedInput, int)


@given(instance=railDsl::Point_strategy)
def test_raildsl::point_selectedInput_setter(instance):
    original = instance.selectedInput
    instance.selectedInput = original
    assert instance.selectedInput == original

@given(instance=railDsl::Point_strategy)
def test_raildsl::point_selectedOutput_type(instance):
    assert isinstance(instance.selectedOutput, int)


@given(instance=railDsl::Point_strategy)
def test_raildsl::point_selectedOutput_setter(instance):
    original = instance.selectedOutput
    instance.selectedOutput = original
    assert instance.selectedOutput == original

@given(instance=railDsl::Point_strategy)
def test_raildsl::point_locked_type(instance):
    assert isinstance(instance.locked, bool)


@given(instance=railDsl::Point_strategy)
def test_raildsl::point_locked_setter(instance):
    original = instance.locked
    instance.locked = original
    assert instance.locked == original

@given(instance=railDsl::Point_strategy)
def test_raildsl::point_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=railDsl::Point_strategy)
def test_raildsl::point_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=railDsl::Segment_strategy)
@settings(max_examples=50)
def test_raildsl::segment_instantiation(instance):
    assert isinstance(instance, railDsl::Segment)

@given(instance=RouteObject_strategy)
@settings(max_examples=50)
def test_routeobject_instantiation(instance):
    assert isinstance(instance, RouteObject)

@given(instance=Declaration_strategy)
@settings(max_examples=50)
def test_declaration_instantiation(instance):
    assert isinstance(instance, Declaration)

@given(instance=railDsl::Train_strategy)
@settings(max_examples=50)
def test_raildsl::train_instantiation(instance):
    assert isinstance(instance, railDsl::Train)

@given(instance=railDsl::Train_strategy)
def test_raildsl::train_acceleration_type(instance):
    assert isinstance(instance.acceleration, float)


@given(instance=railDsl::Train_strategy)
def test_raildsl::train_acceleration_setter(instance):
    original = instance.acceleration
    instance.acceleration = original
    assert instance.acceleration == original

@given(instance=railDsl::Train_strategy)
def test_raildsl::train_length_type(instance):
    assert isinstance(instance.length, float)


@given(instance=railDsl::Train_strategy)
def test_raildsl::train_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original

@given(instance=railDsl::Train_strategy)
def test_raildsl::train_speed_type(instance):
    assert isinstance(instance.speed, float)


@given(instance=railDsl::Train_strategy)
def test_raildsl::train_speed_setter(instance):
    original = instance.speed
    instance.speed = original
    assert instance.speed == original

@given(instance=railDsl::Track_strategy)
@settings(max_examples=50)
def test_raildsl::track_instantiation(instance):
    assert isinstance(instance, railDsl::Track)

@given(instance=railDsl::TrainRoute_strategy)
@settings(max_examples=50)
def test_raildsl::trainroute_instantiation(instance):
    assert isinstance(instance, railDsl::TrainRoute)

@given(instance=railDsl::TrainRoute_strategy)
def test_raildsl::trainroute_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=railDsl::TrainRoute_strategy)
def test_raildsl::trainroute_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=railDsl::TrainRoute_strategy)
def test_raildsl::trainroute_locked_type(instance):
    assert isinstance(instance.locked, bool)


@given(instance=railDsl::TrainRoute_strategy)
def test_raildsl::trainroute_locked_setter(instance):
    original = instance.locked
    instance.locked = original
    assert instance.locked == original

@given(instance=railDsl::Vertex_strategy)
@settings(max_examples=50)
def test_raildsl::vertex_instantiation(instance):
    assert isinstance(instance, railDsl::Vertex)

@given(instance=railDsl::Vertex_strategy)
def test_raildsl::vertex_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=railDsl::Vertex_strategy)
def test_raildsl::vertex_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=railDsl::TrackObject_strategy)
@settings(max_examples=50)
def test_raildsl::trackobject_instantiation(instance):
    assert isinstance(instance, railDsl::TrackObject)

@given(instance=railDsl::TrackObject_strategy)
def test_raildsl::trackobject_length_type(instance):
    assert isinstance(instance.length, float)


@given(instance=railDsl::TrackObject_strategy)
def test_raildsl::trackobject_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original

@given(instance=SegmentObject_strategy)
@settings(max_examples=50)
def test_segmentobject_instantiation(instance):
    assert isinstance(instance, SegmentObject)

@given(instance=railDsl::LevelCrossing_strategy)
@settings(max_examples=50)
def test_raildsl::levelcrossing_instantiation(instance):
    assert isinstance(instance, railDsl::LevelCrossing)

@given(instance=railDsl::LevelCrossing_strategy)
def test_raildsl::levelcrossing_length_type(instance):
    assert isinstance(instance.length, float)


@given(instance=railDsl::LevelCrossing_strategy)
def test_raildsl::levelcrossing_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original

@given(instance=railDsl::LevelCrossing_strategy)
def test_raildsl::levelcrossing_closed_type(instance):
    assert isinstance(instance.closed, bool)


@given(instance=railDsl::LevelCrossing_strategy)
def test_raildsl::levelcrossing_closed_setter(instance):
    original = instance.closed
    instance.closed = original
    assert instance.closed == original

@given(instance=railDsl::Platform_strategy)
@settings(max_examples=50)
def test_raildsl::platform_instantiation(instance):
    assert isinstance(instance, railDsl::Platform)

@given(instance=railDsl::Platform_strategy)
def test_raildsl::platform_length_type(instance):
    assert isinstance(instance.length, float)


@given(instance=railDsl::Platform_strategy)
def test_raildsl::platform_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original

@given(instance=railDsl::Signal_strategy)
@settings(max_examples=50)
def test_raildsl::signal_instantiation(instance):
    assert isinstance(instance, railDsl::Signal)

@given(instance=railDsl::Signal_strategy)
def test_raildsl::signal_shunting_type(instance):
    assert isinstance(instance.shunting, bool)


@given(instance=railDsl::Signal_strategy)
def test_raildsl::signal_shunting_setter(instance):
    original = instance.shunting
    instance.shunting = original
    assert instance.shunting == original

@given(instance=railDsl::Signal_strategy)
def test_raildsl::signal_main_type(instance):
    assert isinstance(instance.main, bool)


@given(instance=railDsl::Signal_strategy)
def test_raildsl::signal_main_setter(instance):
    original = instance.main
    instance.main = original
    assert instance.main == original

@given(instance=railDsl::Derailer_strategy)
@settings(max_examples=50)
def test_raildsl::derailer_instantiation(instance):
    assert isinstance(instance, railDsl::Derailer)

@given(instance=railDsl::Derailer_strategy)
def test_raildsl::derailer_active_type(instance):
    assert isinstance(instance.active, bool)


@given(instance=railDsl::Derailer_strategy)
def test_raildsl::derailer_active_setter(instance):
    original = instance.active
    instance.active = original
    assert instance.active == original

@given(instance=railDsl::SegmentPosition_strategy)
@settings(max_examples=50)
def test_raildsl::segmentposition_instantiation(instance):
    assert isinstance(instance, railDsl::SegmentPosition)

@given(instance=railDsl::SegmentPosition_strategy)
def test_raildsl::segmentposition_side_type(instance):
    assert isinstance(instance.side, str)


@given(instance=railDsl::SegmentPosition_strategy)
def test_raildsl::segmentposition_side_setter(instance):
    original = instance.side
    instance.side = original
    assert instance.side == original

@given(instance=railDsl::SegmentPosition_strategy)
def test_raildsl::segmentposition_position_type(instance):
    assert isinstance(instance.position, float)


@given(instance=railDsl::SegmentPosition_strategy)
def test_raildsl::segmentposition_position_setter(instance):
    original = instance.position
    instance.position = original
    assert instance.position == original

@given(instance=railDsl::SegmentPosition_strategy)
def test_raildsl::segmentposition_atEnd_type(instance):
    assert isinstance(instance.atEnd, bool)


@given(instance=railDsl::SegmentPosition_strategy)
def test_raildsl::segmentposition_atEnd_setter(instance):
    original = instance.atEnd
    instance.atEnd = original
    assert instance.atEnd == original

@given(instance=railDsl::SegmentPosition_strategy)
def test_raildsl::segmentposition_atStart_type(instance):
    assert isinstance(instance.atStart, bool)


@given(instance=railDsl::SegmentPosition_strategy)
def test_raildsl::segmentposition_atStart_setter(instance):
    original = instance.atStart
    instance.atStart = original
    assert instance.atStart == original

@given(instance=railDsl::SegmentPosition_strategy)
def test_raildsl::segmentposition_orientation_type(instance):
    assert isinstance(instance.orientation, str)


@given(instance=railDsl::SegmentPosition_strategy)
def test_raildsl::segmentposition_orientation_setter(instance):
    original = instance.orientation
    instance.orientation = original
    assert instance.orientation == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=railDsl::SegmentObject_strategy)
@settings(max_examples=50)
def test_raildsl::segmentobject_instantiation(instance):
    assert isinstance(instance, railDsl::SegmentObject)

@given(instance=railDsl::Declaration_strategy)
@settings(max_examples=50)
def test_raildsl::declaration_instantiation(instance):
    assert isinstance(instance, railDsl::Declaration)

@given(instance=railDsl::Station_strategy)
@settings(max_examples=50)
def test_raildsl::station_instantiation(instance):
    assert isinstance(instance, railDsl::Station)
