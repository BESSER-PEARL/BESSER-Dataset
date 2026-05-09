import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    uppaallite::TemplateType,
    uppaallite::UppaalDiagram,
    uppaallite::TransitionType,
    uppaallite::LocationType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_uppaallite::templatetype_is_not_abstract():
    assert not inspect.isabstract(uppaallite::TemplateType)


def test_uppaallite::templatetype_constructor_exists():
    assert callable(uppaallite::TemplateType.__init__)


def test_uppaallite::templatetype_constructor_args():
    sig = inspect.signature(uppaallite::TemplateType.__init__)
    params = list(sig.parameters.keys())
    assert "declaration" in params, "Missing parameter 'declaration'"
    assert "name" in params, "Missing parameter 'name'"

def test_uppaallite::templatetype_has_declaration():
    assert hasattr(uppaallite::TemplateType, "declaration")
    descriptor = None
    for klass in uppaallite::TemplateType.__mro__:
        if "declaration" in klass.__dict__:
            descriptor = klass.__dict__["declaration"]
            break
    assert isinstance(descriptor, property)

def test_uppaallite::templatetype_has_name():
    assert hasattr(uppaallite::TemplateType, "name")
    descriptor = None
    for klass in uppaallite::TemplateType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_uppaallite::uppaaldiagram_is_not_abstract():
    assert not inspect.isabstract(uppaallite::UppaalDiagram)


def test_uppaallite::uppaaldiagram_constructor_exists():
    assert callable(uppaallite::UppaalDiagram.__init__)


def test_uppaallite::uppaaldiagram_constructor_args():
    sig = inspect.signature(uppaallite::UppaalDiagram.__init__)
    params = list(sig.parameters.keys())
    assert "resourceWeightDeclaration" in params, "Missing parameter 'resourceWeightDeclaration'"
    assert "declaration" in params, "Missing parameter 'declaration'"

def test_uppaallite::uppaaldiagram_has_resourceWeightDeclaration():
    assert hasattr(uppaallite::UppaalDiagram, "resourceWeightDeclaration")
    descriptor = None
    for klass in uppaallite::UppaalDiagram.__mro__:
        if "resourceWeightDeclaration" in klass.__dict__:
            descriptor = klass.__dict__["resourceWeightDeclaration"]
            break
    assert isinstance(descriptor, property)

def test_uppaallite::uppaaldiagram_has_declaration():
    assert hasattr(uppaallite::UppaalDiagram, "declaration")
    descriptor = None
    for klass in uppaallite::UppaalDiagram.__mro__:
        if "declaration" in klass.__dict__:
            descriptor = klass.__dict__["declaration"]
            break
    assert isinstance(descriptor, property)



def test_uppaallite::transitiontype_is_not_abstract():
    assert not inspect.isabstract(uppaallite::TransitionType)


def test_uppaallite::transitiontype_constructor_exists():
    assert callable(uppaallite::TransitionType.__init__)


def test_uppaallite::transitiontype_constructor_args():
    sig = inspect.signature(uppaallite::TransitionType.__init__)
    params = list(sig.parameters.keys())
    assert "guard" in params, "Missing parameter 'guard'"
    assert "cost" in params, "Missing parameter 'cost'"
    assert "assignment" in params, "Missing parameter 'assignment'"
    assert "sync" in params, "Missing parameter 'sync'"

def test_uppaallite::transitiontype_has_guard():
    assert hasattr(uppaallite::TransitionType, "guard")
    descriptor = None
    for klass in uppaallite::TransitionType.__mro__:
        if "guard" in klass.__dict__:
            descriptor = klass.__dict__["guard"]
            break
    assert isinstance(descriptor, property)

def test_uppaallite::transitiontype_has_cost():
    assert hasattr(uppaallite::TransitionType, "cost")
    descriptor = None
    for klass in uppaallite::TransitionType.__mro__:
        if "cost" in klass.__dict__:
            descriptor = klass.__dict__["cost"]
            break
    assert isinstance(descriptor, property)

def test_uppaallite::transitiontype_has_assignment():
    assert hasattr(uppaallite::TransitionType, "assignment")
    descriptor = None
    for klass in uppaallite::TransitionType.__mro__:
        if "assignment" in klass.__dict__:
            descriptor = klass.__dict__["assignment"]
            break
    assert isinstance(descriptor, property)

def test_uppaallite::transitiontype_has_sync():
    assert hasattr(uppaallite::TransitionType, "sync")
    descriptor = None
    for klass in uppaallite::TransitionType.__mro__:
        if "sync" in klass.__dict__:
            descriptor = klass.__dict__["sync"]
            break
    assert isinstance(descriptor, property)



def test_uppaallite::locationtype_is_not_abstract():
    assert not inspect.isabstract(uppaallite::LocationType)


def test_uppaallite::locationtype_constructor_exists():
    assert callable(uppaallite::LocationType.__init__)


def test_uppaallite::locationtype_constructor_args():
    sig = inspect.signature(uppaallite::LocationType.__init__)
    params = list(sig.parameters.keys())
    assert "cost" in params, "Missing parameter 'cost'"
    assert "x" in params, "Missing parameter 'x'"
    assert "invariant" in params, "Missing parameter 'invariant'"
    assert "y" in params, "Missing parameter 'y'"
    assert "name" in params, "Missing parameter 'name'"
    assert "committed" in params, "Missing parameter 'committed'"
    assert "id" in params, "Missing parameter 'id'"
    assert "initial" in params, "Missing parameter 'initial'"
    assert "urgent" in params, "Missing parameter 'urgent'"

def test_uppaallite::locationtype_has_cost():
    assert hasattr(uppaallite::LocationType, "cost")
    descriptor = None
    for klass in uppaallite::LocationType.__mro__:
        if "cost" in klass.__dict__:
            descriptor = klass.__dict__["cost"]
            break
    assert isinstance(descriptor, property)

def test_uppaallite::locationtype_has_x():
    assert hasattr(uppaallite::LocationType, "x")
    descriptor = None
    for klass in uppaallite::LocationType.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_uppaallite::locationtype_has_invariant():
    assert hasattr(uppaallite::LocationType, "invariant")
    descriptor = None
    for klass in uppaallite::LocationType.__mro__:
        if "invariant" in klass.__dict__:
            descriptor = klass.__dict__["invariant"]
            break
    assert isinstance(descriptor, property)

def test_uppaallite::locationtype_has_y():
    assert hasattr(uppaallite::LocationType, "y")
    descriptor = None
    for klass in uppaallite::LocationType.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_uppaallite::locationtype_has_name():
    assert hasattr(uppaallite::LocationType, "name")
    descriptor = None
    for klass in uppaallite::LocationType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_uppaallite::locationtype_has_committed():
    assert hasattr(uppaallite::LocationType, "committed")
    descriptor = None
    for klass in uppaallite::LocationType.__mro__:
        if "committed" in klass.__dict__:
            descriptor = klass.__dict__["committed"]
            break
    assert isinstance(descriptor, property)

def test_uppaallite::locationtype_has_id():
    assert hasattr(uppaallite::LocationType, "id")
    descriptor = None
    for klass in uppaallite::LocationType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_uppaallite::locationtype_has_initial():
    assert hasattr(uppaallite::LocationType, "initial")
    descriptor = None
    for klass in uppaallite::LocationType.__mro__:
        if "initial" in klass.__dict__:
            descriptor = klass.__dict__["initial"]
            break
    assert isinstance(descriptor, property)

def test_uppaallite::locationtype_has_urgent():
    assert hasattr(uppaallite::LocationType, "urgent")
    descriptor = None
    for klass in uppaallite::LocationType.__mro__:
        if "urgent" in klass.__dict__:
            descriptor = klass.__dict__["urgent"]
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
uppaallite::TemplateType_strategy = st.builds(
    uppaallite::TemplateType,
    declaration=
        safe_text,
    name=
        safe_text
)
uppaallite::UppaalDiagram_strategy = st.builds(
    uppaallite::UppaalDiagram,
    resourceWeightDeclaration=
        safe_text,
    declaration=
        safe_text
)
uppaallite::TransitionType_strategy = st.builds(
    uppaallite::TransitionType,
    guard=
        safe_text,
    cost=
        safe_text,
    assignment=
        safe_text,
    sync=
        safe_text
)
uppaallite::LocationType_strategy = st.builds(
    uppaallite::LocationType,
    cost=
        safe_text,
    x=
        st.integers(),
    invariant=
        safe_text,
    y=
        st.integers(),
    name=
        safe_text,
    committed=
        st.booleans(),
    id=
        safe_text,
    initial=
        st.booleans(),
    urgent=
        st.booleans()
)

@given(instance=uppaallite::TemplateType_strategy)
@settings(max_examples=50)
def test_uppaallite::templatetype_instantiation(instance):
    assert isinstance(instance, uppaallite::TemplateType)

@given(instance=uppaallite::TemplateType_strategy)
def test_uppaallite::templatetype_declaration_type(instance):
    assert isinstance(instance.declaration, str)


@given(instance=uppaallite::TemplateType_strategy)
def test_uppaallite::templatetype_declaration_setter(instance):
    original = instance.declaration
    instance.declaration = original
    assert instance.declaration == original

@given(instance=uppaallite::TemplateType_strategy)
def test_uppaallite::templatetype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=uppaallite::TemplateType_strategy)
def test_uppaallite::templatetype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=uppaallite::UppaalDiagram_strategy)
@settings(max_examples=50)
def test_uppaallite::uppaaldiagram_instantiation(instance):
    assert isinstance(instance, uppaallite::UppaalDiagram)

@given(instance=uppaallite::UppaalDiagram_strategy)
def test_uppaallite::uppaaldiagram_resourceWeightDeclaration_type(instance):
    assert isinstance(instance.resourceWeightDeclaration, str)


@given(instance=uppaallite::UppaalDiagram_strategy)
def test_uppaallite::uppaaldiagram_resourceWeightDeclaration_setter(instance):
    original = instance.resourceWeightDeclaration
    instance.resourceWeightDeclaration = original
    assert instance.resourceWeightDeclaration == original

@given(instance=uppaallite::UppaalDiagram_strategy)
def test_uppaallite::uppaaldiagram_declaration_type(instance):
    assert isinstance(instance.declaration, str)


@given(instance=uppaallite::UppaalDiagram_strategy)
def test_uppaallite::uppaaldiagram_declaration_setter(instance):
    original = instance.declaration
    instance.declaration = original
    assert instance.declaration == original

@given(instance=uppaallite::TransitionType_strategy)
@settings(max_examples=50)
def test_uppaallite::transitiontype_instantiation(instance):
    assert isinstance(instance, uppaallite::TransitionType)

@given(instance=uppaallite::TransitionType_strategy)
def test_uppaallite::transitiontype_guard_type(instance):
    assert isinstance(instance.guard, str)


@given(instance=uppaallite::TransitionType_strategy)
def test_uppaallite::transitiontype_guard_setter(instance):
    original = instance.guard
    instance.guard = original
    assert instance.guard == original

@given(instance=uppaallite::TransitionType_strategy)
def test_uppaallite::transitiontype_cost_type(instance):
    assert isinstance(instance.cost, str)


@given(instance=uppaallite::TransitionType_strategy)
def test_uppaallite::transitiontype_cost_setter(instance):
    original = instance.cost
    instance.cost = original
    assert instance.cost == original

@given(instance=uppaallite::TransitionType_strategy)
def test_uppaallite::transitiontype_assignment_type(instance):
    assert isinstance(instance.assignment, str)


@given(instance=uppaallite::TransitionType_strategy)
def test_uppaallite::transitiontype_assignment_setter(instance):
    original = instance.assignment
    instance.assignment = original
    assert instance.assignment == original

@given(instance=uppaallite::TransitionType_strategy)
def test_uppaallite::transitiontype_sync_type(instance):
    assert isinstance(instance.sync, str)


@given(instance=uppaallite::TransitionType_strategy)
def test_uppaallite::transitiontype_sync_setter(instance):
    original = instance.sync
    instance.sync = original
    assert instance.sync == original

@given(instance=uppaallite::LocationType_strategy)
@settings(max_examples=50)
def test_uppaallite::locationtype_instantiation(instance):
    assert isinstance(instance, uppaallite::LocationType)

@given(instance=uppaallite::LocationType_strategy)
def test_uppaallite::locationtype_cost_type(instance):
    assert isinstance(instance.cost, str)


@given(instance=uppaallite::LocationType_strategy)
def test_uppaallite::locationtype_cost_setter(instance):
    original = instance.cost
    instance.cost = original
    assert instance.cost == original

@given(instance=uppaallite::LocationType_strategy)
def test_uppaallite::locationtype_x_type(instance):
    assert isinstance(instance.x, int)


@given(instance=uppaallite::LocationType_strategy)
def test_uppaallite::locationtype_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=uppaallite::LocationType_strategy)
def test_uppaallite::locationtype_invariant_type(instance):
    assert isinstance(instance.invariant, str)


@given(instance=uppaallite::LocationType_strategy)
def test_uppaallite::locationtype_invariant_setter(instance):
    original = instance.invariant
    instance.invariant = original
    assert instance.invariant == original

@given(instance=uppaallite::LocationType_strategy)
def test_uppaallite::locationtype_y_type(instance):
    assert isinstance(instance.y, int)


@given(instance=uppaallite::LocationType_strategy)
def test_uppaallite::locationtype_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=uppaallite::LocationType_strategy)
def test_uppaallite::locationtype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=uppaallite::LocationType_strategy)
def test_uppaallite::locationtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=uppaallite::LocationType_strategy)
def test_uppaallite::locationtype_committed_type(instance):
    assert isinstance(instance.committed, bool)


@given(instance=uppaallite::LocationType_strategy)
def test_uppaallite::locationtype_committed_setter(instance):
    original = instance.committed
    instance.committed = original
    assert instance.committed == original

@given(instance=uppaallite::LocationType_strategy)
def test_uppaallite::locationtype_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=uppaallite::LocationType_strategy)
def test_uppaallite::locationtype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=uppaallite::LocationType_strategy)
def test_uppaallite::locationtype_initial_type(instance):
    assert isinstance(instance.initial, bool)


@given(instance=uppaallite::LocationType_strategy)
def test_uppaallite::locationtype_initial_setter(instance):
    original = instance.initial
    instance.initial = original
    assert instance.initial == original

@given(instance=uppaallite::LocationType_strategy)
def test_uppaallite::locationtype_urgent_type(instance):
    assert isinstance(instance.urgent, bool)


@given(instance=uppaallite::LocationType_strategy)
def test_uppaallite::locationtype_urgent_setter(instance):
    original = instance.urgent
    instance.urgent = original
    assert instance.urgent == original
