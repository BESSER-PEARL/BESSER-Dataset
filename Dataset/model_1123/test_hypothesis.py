import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    uppaallite_TemplateType,
    uppaallite_UppaalDiagram,
    uppaallite_TransitionType,
    uppaallite_LocationType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_uppaallite_templatetype_is_not_abstract():
    assert not inspect.isabstract(uppaallite_TemplateType)


def test_uppaallite_templatetype_constructor_exists():
    assert callable(uppaallite_TemplateType.__init__)


def test_uppaallite_templatetype_constructor_args():
    sig = inspect.signature(uppaallite_TemplateType.__init__)
    params = list(sig.parameters.keys())
    assert "declaration" in params, "Missing parameter 'declaration'"
    assert "name" in params, "Missing parameter 'name'"

def test_uppaallite_templatetype_has_declaration():
    assert hasattr(uppaallite_TemplateType, "declaration")
    descriptor = None
    for klass in uppaallite_TemplateType.__mro__:
        if "declaration" in klass.__dict__:
            descriptor = klass.__dict__["declaration"]
            break
    assert isinstance(descriptor, property)

def test_uppaallite_templatetype_has_name():
    assert hasattr(uppaallite_TemplateType, "name")
    descriptor = None
    for klass in uppaallite_TemplateType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_uppaallite_uppaaldiagram_is_not_abstract():
    assert not inspect.isabstract(uppaallite_UppaalDiagram)


def test_uppaallite_uppaaldiagram_constructor_exists():
    assert callable(uppaallite_UppaalDiagram.__init__)


def test_uppaallite_uppaaldiagram_constructor_args():
    sig = inspect.signature(uppaallite_UppaalDiagram.__init__)
    params = list(sig.parameters.keys())
    assert "resourceWeightDeclaration" in params, "Missing parameter 'resourceWeightDeclaration'"
    assert "declaration" in params, "Missing parameter 'declaration'"

def test_uppaallite_uppaaldiagram_has_resourceWeightDeclaration():
    assert hasattr(uppaallite_UppaalDiagram, "resourceWeightDeclaration")
    descriptor = None
    for klass in uppaallite_UppaalDiagram.__mro__:
        if "resourceWeightDeclaration" in klass.__dict__:
            descriptor = klass.__dict__["resourceWeightDeclaration"]
            break
    assert isinstance(descriptor, property)

def test_uppaallite_uppaaldiagram_has_declaration():
    assert hasattr(uppaallite_UppaalDiagram, "declaration")
    descriptor = None
    for klass in uppaallite_UppaalDiagram.__mro__:
        if "declaration" in klass.__dict__:
            descriptor = klass.__dict__["declaration"]
            break
    assert isinstance(descriptor, property)



def test_uppaallite_transitiontype_is_not_abstract():
    assert not inspect.isabstract(uppaallite_TransitionType)


def test_uppaallite_transitiontype_constructor_exists():
    assert callable(uppaallite_TransitionType.__init__)


def test_uppaallite_transitiontype_constructor_args():
    sig = inspect.signature(uppaallite_TransitionType.__init__)
    params = list(sig.parameters.keys())
    assert "guard" in params, "Missing parameter 'guard'"
    assert "assignment" in params, "Missing parameter 'assignment'"
    assert "sync" in params, "Missing parameter 'sync'"
    assert "cost" in params, "Missing parameter 'cost'"

def test_uppaallite_transitiontype_has_guard():
    assert hasattr(uppaallite_TransitionType, "guard")
    descriptor = None
    for klass in uppaallite_TransitionType.__mro__:
        if "guard" in klass.__dict__:
            descriptor = klass.__dict__["guard"]
            break
    assert isinstance(descriptor, property)

def test_uppaallite_transitiontype_has_assignment():
    assert hasattr(uppaallite_TransitionType, "assignment")
    descriptor = None
    for klass in uppaallite_TransitionType.__mro__:
        if "assignment" in klass.__dict__:
            descriptor = klass.__dict__["assignment"]
            break
    assert isinstance(descriptor, property)

def test_uppaallite_transitiontype_has_sync():
    assert hasattr(uppaallite_TransitionType, "sync")
    descriptor = None
    for klass in uppaallite_TransitionType.__mro__:
        if "sync" in klass.__dict__:
            descriptor = klass.__dict__["sync"]
            break
    assert isinstance(descriptor, property)

def test_uppaallite_transitiontype_has_cost():
    assert hasattr(uppaallite_TransitionType, "cost")
    descriptor = None
    for klass in uppaallite_TransitionType.__mro__:
        if "cost" in klass.__dict__:
            descriptor = klass.__dict__["cost"]
            break
    assert isinstance(descriptor, property)



def test_uppaallite_locationtype_is_not_abstract():
    assert not inspect.isabstract(uppaallite_LocationType)


def test_uppaallite_locationtype_constructor_exists():
    assert callable(uppaallite_LocationType.__init__)


def test_uppaallite_locationtype_constructor_args():
    sig = inspect.signature(uppaallite_LocationType.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "x" in params, "Missing parameter 'x'"
    assert "committed" in params, "Missing parameter 'committed'"
    assert "y" in params, "Missing parameter 'y'"
    assert "urgent" in params, "Missing parameter 'urgent'"
    assert "invariant" in params, "Missing parameter 'invariant'"
    assert "cost" in params, "Missing parameter 'cost'"
    assert "name" in params, "Missing parameter 'name'"
    assert "initial" in params, "Missing parameter 'initial'"

def test_uppaallite_locationtype_has_id():
    assert hasattr(uppaallite_LocationType, "id")
    descriptor = None
    for klass in uppaallite_LocationType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_uppaallite_locationtype_has_x():
    assert hasattr(uppaallite_LocationType, "x")
    descriptor = None
    for klass in uppaallite_LocationType.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_uppaallite_locationtype_has_committed():
    assert hasattr(uppaallite_LocationType, "committed")
    descriptor = None
    for klass in uppaallite_LocationType.__mro__:
        if "committed" in klass.__dict__:
            descriptor = klass.__dict__["committed"]
            break
    assert isinstance(descriptor, property)

def test_uppaallite_locationtype_has_y():
    assert hasattr(uppaallite_LocationType, "y")
    descriptor = None
    for klass in uppaallite_LocationType.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_uppaallite_locationtype_has_urgent():
    assert hasattr(uppaallite_LocationType, "urgent")
    descriptor = None
    for klass in uppaallite_LocationType.__mro__:
        if "urgent" in klass.__dict__:
            descriptor = klass.__dict__["urgent"]
            break
    assert isinstance(descriptor, property)

def test_uppaallite_locationtype_has_invariant():
    assert hasattr(uppaallite_LocationType, "invariant")
    descriptor = None
    for klass in uppaallite_LocationType.__mro__:
        if "invariant" in klass.__dict__:
            descriptor = klass.__dict__["invariant"]
            break
    assert isinstance(descriptor, property)

def test_uppaallite_locationtype_has_cost():
    assert hasattr(uppaallite_LocationType, "cost")
    descriptor = None
    for klass in uppaallite_LocationType.__mro__:
        if "cost" in klass.__dict__:
            descriptor = klass.__dict__["cost"]
            break
    assert isinstance(descriptor, property)

def test_uppaallite_locationtype_has_name():
    assert hasattr(uppaallite_LocationType, "name")
    descriptor = None
    for klass in uppaallite_LocationType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_uppaallite_locationtype_has_initial():
    assert hasattr(uppaallite_LocationType, "initial")
    descriptor = None
    for klass in uppaallite_LocationType.__mro__:
        if "initial" in klass.__dict__:
            descriptor = klass.__dict__["initial"]
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
uppaallite_TemplateType_strategy = st.builds(
    uppaallite_TemplateType,
    declaration=
        safe_text,
    name=
        safe_text
)
uppaallite_UppaalDiagram_strategy = st.builds(
    uppaallite_UppaalDiagram,
    resourceWeightDeclaration=
        safe_text,
    declaration=
        safe_text
)
uppaallite_TransitionType_strategy = st.builds(
    uppaallite_TransitionType,
    guard=
        safe_text,
    assignment=
        safe_text,
    sync=
        safe_text,
    cost=
        safe_text
)
uppaallite_LocationType_strategy = st.builds(
    uppaallite_LocationType,
    id=
        safe_text,
    x=
        st.integers(),
    committed=
        st.booleans(),
    y=
        st.integers(),
    urgent=
        st.booleans(),
    invariant=
        safe_text,
    cost=
        safe_text,
    name=
        safe_text,
    initial=
        st.booleans()
)

@given(instance=uppaallite_TemplateType_strategy)
@settings(max_examples=50)
def test_uppaallite_templatetype_instantiation(instance):
    assert isinstance(instance, uppaallite_TemplateType)



@given(instance=uppaallite_TemplateType_strategy)
def test_uppaallite_templatetype_declaration_setter(instance):
    original = instance.declaration
    instance.declaration = original
    assert instance.declaration == original



@given(instance=uppaallite_TemplateType_strategy)
def test_uppaallite_templatetype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=uppaallite_UppaalDiagram_strategy)
@settings(max_examples=50)
def test_uppaallite_uppaaldiagram_instantiation(instance):
    assert isinstance(instance, uppaallite_UppaalDiagram)



@given(instance=uppaallite_UppaalDiagram_strategy)
def test_uppaallite_uppaaldiagram_resourceWeightDeclaration_setter(instance):
    original = instance.resourceWeightDeclaration
    instance.resourceWeightDeclaration = original
    assert instance.resourceWeightDeclaration == original



@given(instance=uppaallite_UppaalDiagram_strategy)
def test_uppaallite_uppaaldiagram_declaration_setter(instance):
    original = instance.declaration
    instance.declaration = original
    assert instance.declaration == original

@given(instance=uppaallite_TransitionType_strategy)
@settings(max_examples=50)
def test_uppaallite_transitiontype_instantiation(instance):
    assert isinstance(instance, uppaallite_TransitionType)



@given(instance=uppaallite_TransitionType_strategy)
def test_uppaallite_transitiontype_guard_setter(instance):
    original = instance.guard
    instance.guard = original
    assert instance.guard == original



@given(instance=uppaallite_TransitionType_strategy)
def test_uppaallite_transitiontype_assignment_setter(instance):
    original = instance.assignment
    instance.assignment = original
    assert instance.assignment == original



@given(instance=uppaallite_TransitionType_strategy)
def test_uppaallite_transitiontype_sync_setter(instance):
    original = instance.sync
    instance.sync = original
    assert instance.sync == original



@given(instance=uppaallite_TransitionType_strategy)
def test_uppaallite_transitiontype_cost_setter(instance):
    original = instance.cost
    instance.cost = original
    assert instance.cost == original

@given(instance=uppaallite_LocationType_strategy)
@settings(max_examples=50)
def test_uppaallite_locationtype_instantiation(instance):
    assert isinstance(instance, uppaallite_LocationType)



@given(instance=uppaallite_LocationType_strategy)
def test_uppaallite_locationtype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=uppaallite_LocationType_strategy)
def test_uppaallite_locationtype_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=uppaallite_LocationType_strategy)
def test_uppaallite_locationtype_committed_setter(instance):
    original = instance.committed
    instance.committed = original
    assert instance.committed == original



@given(instance=uppaallite_LocationType_strategy)
def test_uppaallite_locationtype_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original



@given(instance=uppaallite_LocationType_strategy)
def test_uppaallite_locationtype_urgent_setter(instance):
    original = instance.urgent
    instance.urgent = original
    assert instance.urgent == original



@given(instance=uppaallite_LocationType_strategy)
def test_uppaallite_locationtype_invariant_setter(instance):
    original = instance.invariant
    instance.invariant = original
    assert instance.invariant == original



@given(instance=uppaallite_LocationType_strategy)
def test_uppaallite_locationtype_cost_setter(instance):
    original = instance.cost
    instance.cost = original
    assert instance.cost == original



@given(instance=uppaallite_LocationType_strategy)
def test_uppaallite_locationtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=uppaallite_LocationType_strategy)
def test_uppaallite_locationtype_initial_setter(instance):
    original = instance.initial
    instance.initial = original
    assert instance.initial == original
