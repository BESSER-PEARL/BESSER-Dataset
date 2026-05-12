import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    nupn_EStringToStringMapEntry,
    nupn_NUPNToolspecificType,
    nupn_UnitType,
    nupn_SizeType,
    nupn_StructureType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_nupn_estringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(nupn_EStringToStringMapEntry)


def test_nupn_estringtostringmapentry_constructor_exists():
    assert callable(nupn_EStringToStringMapEntry.__init__)


def test_nupn_estringtostringmapentry_constructor_args():
    sig = inspect.signature(nupn_EStringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())



def test_nupn_nupntoolspecifictype_is_not_abstract():
    assert not inspect.isabstract(nupn_NUPNToolspecificType)


def test_nupn_nupntoolspecifictype_constructor_exists():
    assert callable(nupn_NUPNToolspecificType.__init__)


def test_nupn_nupntoolspecifictype_constructor_args():
    sig = inspect.signature(nupn_NUPNToolspecificType.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "tool" in params, "Missing parameter 'tool'"
    assert "version" in params, "Missing parameter 'version'"

def test_nupn_nupntoolspecifictype_has_mixed():
    assert hasattr(nupn_NUPNToolspecificType, "mixed")
    descriptor = None
    for klass in nupn_NUPNToolspecificType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_nupn_nupntoolspecifictype_has_tool():
    assert hasattr(nupn_NUPNToolspecificType, "tool")
    descriptor = None
    for klass in nupn_NUPNToolspecificType.__mro__:
        if "tool" in klass.__dict__:
            descriptor = klass.__dict__["tool"]
            break
    assert isinstance(descriptor, property)

def test_nupn_nupntoolspecifictype_has_version():
    assert hasattr(nupn_NUPNToolspecificType, "version")
    descriptor = None
    for klass in nupn_NUPNToolspecificType.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)



def test_nupn_unittype_is_not_abstract():
    assert not inspect.isabstract(nupn_UnitType)


def test_nupn_unittype_constructor_exists():
    assert callable(nupn_UnitType.__init__)


def test_nupn_unittype_constructor_args():
    sig = inspect.signature(nupn_UnitType.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "places" in params, "Missing parameter 'places'"
    assert "subunits" in params, "Missing parameter 'subunits'"

def test_nupn_unittype_has_id():
    assert hasattr(nupn_UnitType, "id")
    descriptor = None
    for klass in nupn_UnitType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_nupn_unittype_has_places():
    assert hasattr(nupn_UnitType, "places")
    descriptor = None
    for klass in nupn_UnitType.__mro__:
        if "places" in klass.__dict__:
            descriptor = klass.__dict__["places"]
            break
    assert isinstance(descriptor, property)

def test_nupn_unittype_has_subunits():
    assert hasattr(nupn_UnitType, "subunits")
    descriptor = None
    for klass in nupn_UnitType.__mro__:
        if "subunits" in klass.__dict__:
            descriptor = klass.__dict__["subunits"]
            break
    assert isinstance(descriptor, property)



def test_nupn_sizetype_is_not_abstract():
    assert not inspect.isabstract(nupn_SizeType)


def test_nupn_sizetype_constructor_exists():
    assert callable(nupn_SizeType.__init__)


def test_nupn_sizetype_constructor_args():
    sig = inspect.signature(nupn_SizeType.__init__)
    params = list(sig.parameters.keys())
    assert "transitions" in params, "Missing parameter 'transitions'"
    assert "places" in params, "Missing parameter 'places'"
    assert "arcs" in params, "Missing parameter 'arcs'"

def test_nupn_sizetype_has_transitions():
    assert hasattr(nupn_SizeType, "transitions")
    descriptor = None
    for klass in nupn_SizeType.__mro__:
        if "transitions" in klass.__dict__:
            descriptor = klass.__dict__["transitions"]
            break
    assert isinstance(descriptor, property)

def test_nupn_sizetype_has_places():
    assert hasattr(nupn_SizeType, "places")
    descriptor = None
    for klass in nupn_SizeType.__mro__:
        if "places" in klass.__dict__:
            descriptor = klass.__dict__["places"]
            break
    assert isinstance(descriptor, property)

def test_nupn_sizetype_has_arcs():
    assert hasattr(nupn_SizeType, "arcs")
    descriptor = None
    for klass in nupn_SizeType.__mro__:
        if "arcs" in klass.__dict__:
            descriptor = klass.__dict__["arcs"]
            break
    assert isinstance(descriptor, property)



def test_nupn_structuretype_is_not_abstract():
    assert not inspect.isabstract(nupn_StructureType)


def test_nupn_structuretype_constructor_exists():
    assert callable(nupn_StructureType.__init__)


def test_nupn_structuretype_constructor_args():
    sig = inspect.signature(nupn_StructureType.__init__)
    params = list(sig.parameters.keys())
    assert "units" in params, "Missing parameter 'units'"
    assert "safe" in params, "Missing parameter 'safe'"
    assert "root" in params, "Missing parameter 'root'"

def test_nupn_structuretype_has_units():
    assert hasattr(nupn_StructureType, "units")
    descriptor = None
    for klass in nupn_StructureType.__mro__:
        if "units" in klass.__dict__:
            descriptor = klass.__dict__["units"]
            break
    assert isinstance(descriptor, property)

def test_nupn_structuretype_has_safe():
    assert hasattr(nupn_StructureType, "safe")
    descriptor = None
    for klass in nupn_StructureType.__mro__:
        if "safe" in klass.__dict__:
            descriptor = klass.__dict__["safe"]
            break
    assert isinstance(descriptor, property)

def test_nupn_structuretype_has_root():
    assert hasattr(nupn_StructureType, "root")
    descriptor = None
    for klass in nupn_StructureType.__mro__:
        if "root" in klass.__dict__:
            descriptor = klass.__dict__["root"]
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
nupn_EStringToStringMapEntry_strategy = st.builds(
    nupn_EStringToStringMapEntry,
)
nupn_NUPNToolspecificType_strategy = st.builds(
    nupn_NUPNToolspecificType,
    mixed=
        safe_text,
    tool=
        safe_text,
    version=
        safe_text
)
nupn_UnitType_strategy = st.builds(
    nupn_UnitType,
    id=
        safe_text,
    places=
        safe_text,
    subunits=
        safe_text
)
nupn_SizeType_strategy = st.builds(
    nupn_SizeType,
    transitions=
        safe_text,
    places=
        safe_text,
    arcs=
        safe_text
)
nupn_StructureType_strategy = st.builds(
    nupn_StructureType,
    units=
        safe_text,
    safe=
        safe_text,
    root=
        safe_text
)

@given(instance=nupn_EStringToStringMapEntry_strategy)
@settings(max_examples=50)
def test_nupn_estringtostringmapentry_instantiation(instance):
    assert isinstance(instance, nupn_EStringToStringMapEntry)

@given(instance=nupn_NUPNToolspecificType_strategy)
@settings(max_examples=50)
def test_nupn_nupntoolspecifictype_instantiation(instance):
    assert isinstance(instance, nupn_NUPNToolspecificType)



@given(instance=nupn_NUPNToolspecificType_strategy)
def test_nupn_nupntoolspecifictype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=nupn_NUPNToolspecificType_strategy)
def test_nupn_nupntoolspecifictype_tool_setter(instance):
    original = instance.tool
    instance.tool = original
    assert instance.tool == original



@given(instance=nupn_NUPNToolspecificType_strategy)
def test_nupn_nupntoolspecifictype_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=nupn_UnitType_strategy)
@settings(max_examples=50)
def test_nupn_unittype_instantiation(instance):
    assert isinstance(instance, nupn_UnitType)



@given(instance=nupn_UnitType_strategy)
def test_nupn_unittype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=nupn_UnitType_strategy)
def test_nupn_unittype_places_setter(instance):
    original = instance.places
    instance.places = original
    assert instance.places == original



@given(instance=nupn_UnitType_strategy)
def test_nupn_unittype_subunits_setter(instance):
    original = instance.subunits
    instance.subunits = original
    assert instance.subunits == original

@given(instance=nupn_SizeType_strategy)
@settings(max_examples=50)
def test_nupn_sizetype_instantiation(instance):
    assert isinstance(instance, nupn_SizeType)



@given(instance=nupn_SizeType_strategy)
def test_nupn_sizetype_transitions_setter(instance):
    original = instance.transitions
    instance.transitions = original
    assert instance.transitions == original



@given(instance=nupn_SizeType_strategy)
def test_nupn_sizetype_places_setter(instance):
    original = instance.places
    instance.places = original
    assert instance.places == original



@given(instance=nupn_SizeType_strategy)
def test_nupn_sizetype_arcs_setter(instance):
    original = instance.arcs
    instance.arcs = original
    assert instance.arcs == original

@given(instance=nupn_StructureType_strategy)
@settings(max_examples=50)
def test_nupn_structuretype_instantiation(instance):
    assert isinstance(instance, nupn_StructureType)



@given(instance=nupn_StructureType_strategy)
def test_nupn_structuretype_units_setter(instance):
    original = instance.units
    instance.units = original
    assert instance.units == original



@given(instance=nupn_StructureType_strategy)
def test_nupn_structuretype_safe_setter(instance):
    original = instance.safe
    instance.safe = original
    assert instance.safe == original



@given(instance=nupn_StructureType_strategy)
def test_nupn_structuretype_root_setter(instance):
    original = instance.root
    instance.root = original
    assert instance.root == original
