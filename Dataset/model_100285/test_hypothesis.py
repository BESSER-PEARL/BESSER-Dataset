import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    nupn::EStringToStringMapEntry,
    nupn::NUPNToolspecificType,
    nupn::UnitType,
    nupn::SizeType,
    nupn::StructureType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_nupn::estringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(nupn::EStringToStringMapEntry)


def test_nupn::estringtostringmapentry_constructor_exists():
    assert callable(nupn::EStringToStringMapEntry.__init__)


def test_nupn::estringtostringmapentry_constructor_args():
    sig = inspect.signature(nupn::EStringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())



def test_nupn::nupntoolspecifictype_is_not_abstract():
    assert not inspect.isabstract(nupn::NUPNToolspecificType)


def test_nupn::nupntoolspecifictype_constructor_exists():
    assert callable(nupn::NUPNToolspecificType.__init__)


def test_nupn::nupntoolspecifictype_constructor_args():
    sig = inspect.signature(nupn::NUPNToolspecificType.__init__)
    params = list(sig.parameters.keys())
    assert "tool" in params, "Missing parameter 'tool'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "version" in params, "Missing parameter 'version'"

def test_nupn::nupntoolspecifictype_has_tool():
    assert hasattr(nupn::NUPNToolspecificType, "tool")
    descriptor = None
    for klass in nupn::NUPNToolspecificType.__mro__:
        if "tool" in klass.__dict__:
            descriptor = klass.__dict__["tool"]
            break
    assert isinstance(descriptor, property)

def test_nupn::nupntoolspecifictype_has_mixed():
    assert hasattr(nupn::NUPNToolspecificType, "mixed")
    descriptor = None
    for klass in nupn::NUPNToolspecificType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_nupn::nupntoolspecifictype_has_version():
    assert hasattr(nupn::NUPNToolspecificType, "version")
    descriptor = None
    for klass in nupn::NUPNToolspecificType.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)



def test_nupn::unittype_is_not_abstract():
    assert not inspect.isabstract(nupn::UnitType)


def test_nupn::unittype_constructor_exists():
    assert callable(nupn::UnitType.__init__)


def test_nupn::unittype_constructor_args():
    sig = inspect.signature(nupn::UnitType.__init__)
    params = list(sig.parameters.keys())
    assert "subunits" in params, "Missing parameter 'subunits'"
    assert "id" in params, "Missing parameter 'id'"
    assert "places" in params, "Missing parameter 'places'"

def test_nupn::unittype_has_subunits():
    assert hasattr(nupn::UnitType, "subunits")
    descriptor = None
    for klass in nupn::UnitType.__mro__:
        if "subunits" in klass.__dict__:
            descriptor = klass.__dict__["subunits"]
            break
    assert isinstance(descriptor, property)

def test_nupn::unittype_has_id():
    assert hasattr(nupn::UnitType, "id")
    descriptor = None
    for klass in nupn::UnitType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_nupn::unittype_has_places():
    assert hasattr(nupn::UnitType, "places")
    descriptor = None
    for klass in nupn::UnitType.__mro__:
        if "places" in klass.__dict__:
            descriptor = klass.__dict__["places"]
            break
    assert isinstance(descriptor, property)



def test_nupn::sizetype_is_not_abstract():
    assert not inspect.isabstract(nupn::SizeType)


def test_nupn::sizetype_constructor_exists():
    assert callable(nupn::SizeType.__init__)


def test_nupn::sizetype_constructor_args():
    sig = inspect.signature(nupn::SizeType.__init__)
    params = list(sig.parameters.keys())
    assert "places" in params, "Missing parameter 'places'"
    assert "arcs" in params, "Missing parameter 'arcs'"
    assert "transitions" in params, "Missing parameter 'transitions'"

def test_nupn::sizetype_has_places():
    assert hasattr(nupn::SizeType, "places")
    descriptor = None
    for klass in nupn::SizeType.__mro__:
        if "places" in klass.__dict__:
            descriptor = klass.__dict__["places"]
            break
    assert isinstance(descriptor, property)

def test_nupn::sizetype_has_arcs():
    assert hasattr(nupn::SizeType, "arcs")
    descriptor = None
    for klass in nupn::SizeType.__mro__:
        if "arcs" in klass.__dict__:
            descriptor = klass.__dict__["arcs"]
            break
    assert isinstance(descriptor, property)

def test_nupn::sizetype_has_transitions():
    assert hasattr(nupn::SizeType, "transitions")
    descriptor = None
    for klass in nupn::SizeType.__mro__:
        if "transitions" in klass.__dict__:
            descriptor = klass.__dict__["transitions"]
            break
    assert isinstance(descriptor, property)



def test_nupn::structuretype_is_not_abstract():
    assert not inspect.isabstract(nupn::StructureType)


def test_nupn::structuretype_constructor_exists():
    assert callable(nupn::StructureType.__init__)


def test_nupn::structuretype_constructor_args():
    sig = inspect.signature(nupn::StructureType.__init__)
    params = list(sig.parameters.keys())
    assert "root" in params, "Missing parameter 'root'"
    assert "safe" in params, "Missing parameter 'safe'"
    assert "units" in params, "Missing parameter 'units'"

def test_nupn::structuretype_has_root():
    assert hasattr(nupn::StructureType, "root")
    descriptor = None
    for klass in nupn::StructureType.__mro__:
        if "root" in klass.__dict__:
            descriptor = klass.__dict__["root"]
            break
    assert isinstance(descriptor, property)

def test_nupn::structuretype_has_safe():
    assert hasattr(nupn::StructureType, "safe")
    descriptor = None
    for klass in nupn::StructureType.__mro__:
        if "safe" in klass.__dict__:
            descriptor = klass.__dict__["safe"]
            break
    assert isinstance(descriptor, property)

def test_nupn::structuretype_has_units():
    assert hasattr(nupn::StructureType, "units")
    descriptor = None
    for klass in nupn::StructureType.__mro__:
        if "units" in klass.__dict__:
            descriptor = klass.__dict__["units"]
            break
    assert isinstance(descriptor, property)


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
nupn::EStringToStringMapEntry_strategy = st.builds(
    nupn::EStringToStringMapEntry,
)
nupn::NUPNToolspecificType_strategy = st.builds(
    nupn::NUPNToolspecificType,
    tool=
        safe_text,
    mixed=
        safe_text,
    version=
        safe_text
)
nupn::UnitType_strategy = st.builds(
    nupn::UnitType,
    subunits=
        safe_text,
    id=
        safe_text,
    places=
        safe_text
)
nupn::SizeType_strategy = st.builds(
    nupn::SizeType,
    places=
        safe_text,
    arcs=
        safe_text,
    transitions=
        safe_text
)
nupn::StructureType_strategy = st.builds(
    nupn::StructureType,
    root=
        safe_text,
    safe=
        safe_text,
    units=
        safe_text
)

@given(instance=nupn::EStringToStringMapEntry_strategy)
@settings(max_examples=50)
def test_nupn::estringtostringmapentry_instantiation(instance):
    assert isinstance(instance, nupn::EStringToStringMapEntry)

@given(instance=nupn::NUPNToolspecificType_strategy)
@settings(max_examples=50)
def test_nupn::nupntoolspecifictype_instantiation(instance):
    assert isinstance(instance, nupn::NUPNToolspecificType)

@given(instance=nupn::NUPNToolspecificType_strategy)
def test_nupn::nupntoolspecifictype_tool_type(instance):
    assert isinstance(instance.tool, str)


@given(instance=nupn::NUPNToolspecificType_strategy)
def test_nupn::nupntoolspecifictype_tool_setter(instance):
    original = instance.tool
    instance.tool = original
    assert instance.tool == original

@given(instance=nupn::NUPNToolspecificType_strategy)
def test_nupn::nupntoolspecifictype_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=nupn::NUPNToolspecificType_strategy)
def test_nupn::nupntoolspecifictype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=nupn::NUPNToolspecificType_strategy)
def test_nupn::nupntoolspecifictype_version_type(instance):
    assert isinstance(instance.version, str)


@given(instance=nupn::NUPNToolspecificType_strategy)
def test_nupn::nupntoolspecifictype_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=nupn::UnitType_strategy)
@settings(max_examples=50)
def test_nupn::unittype_instantiation(instance):
    assert isinstance(instance, nupn::UnitType)

@given(instance=nupn::UnitType_strategy)
def test_nupn::unittype_subunits_type(instance):
    assert isinstance(instance.subunits, str)


@given(instance=nupn::UnitType_strategy)
def test_nupn::unittype_subunits_setter(instance):
    original = instance.subunits
    instance.subunits = original
    assert instance.subunits == original

@given(instance=nupn::UnitType_strategy)
def test_nupn::unittype_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=nupn::UnitType_strategy)
def test_nupn::unittype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=nupn::UnitType_strategy)
def test_nupn::unittype_places_type(instance):
    assert isinstance(instance.places, str)


@given(instance=nupn::UnitType_strategy)
def test_nupn::unittype_places_setter(instance):
    original = instance.places
    instance.places = original
    assert instance.places == original

@given(instance=nupn::SizeType_strategy)
@settings(max_examples=50)
def test_nupn::sizetype_instantiation(instance):
    assert isinstance(instance, nupn::SizeType)

@given(instance=nupn::SizeType_strategy)
def test_nupn::sizetype_places_type(instance):
    assert isinstance(instance.places, str)


@given(instance=nupn::SizeType_strategy)
def test_nupn::sizetype_places_setter(instance):
    original = instance.places
    instance.places = original
    assert instance.places == original

@given(instance=nupn::SizeType_strategy)
def test_nupn::sizetype_arcs_type(instance):
    assert isinstance(instance.arcs, str)


@given(instance=nupn::SizeType_strategy)
def test_nupn::sizetype_arcs_setter(instance):
    original = instance.arcs
    instance.arcs = original
    assert instance.arcs == original

@given(instance=nupn::SizeType_strategy)
def test_nupn::sizetype_transitions_type(instance):
    assert isinstance(instance.transitions, str)


@given(instance=nupn::SizeType_strategy)
def test_nupn::sizetype_transitions_setter(instance):
    original = instance.transitions
    instance.transitions = original
    assert instance.transitions == original

@given(instance=nupn::StructureType_strategy)
@settings(max_examples=50)
def test_nupn::structuretype_instantiation(instance):
    assert isinstance(instance, nupn::StructureType)

@given(instance=nupn::StructureType_strategy)
def test_nupn::structuretype_root_type(instance):
    assert isinstance(instance.root, str)


@given(instance=nupn::StructureType_strategy)
def test_nupn::structuretype_root_setter(instance):
    original = instance.root
    instance.root = original
    assert instance.root == original

@given(instance=nupn::StructureType_strategy)
def test_nupn::structuretype_safe_type(instance):
    assert isinstance(instance.safe, str)


@given(instance=nupn::StructureType_strategy)
def test_nupn::structuretype_safe_setter(instance):
    original = instance.safe
    instance.safe = original
    assert instance.safe == original

@given(instance=nupn::StructureType_strategy)
def test_nupn::structuretype_units_type(instance):
    assert isinstance(instance.units, str)


@given(instance=nupn::StructureType_strategy)
def test_nupn::structuretype_units_setter(instance):
    original = instance.units
    instance.units = original
    assert instance.units == original
