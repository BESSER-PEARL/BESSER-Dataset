import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ProductionSystem::Piece,
    ProductionSystem::Conveyor,
    ProductionSystem::Machine,
    Piece,
    ProductionSystem::Processed,
    ProductionSystem::Raw,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_productionsystem::piece_is_not_abstract():
    assert not inspect.isabstract(ProductionSystem::Piece)


def test_productionsystem::piece_constructor_exists():
    assert callable(ProductionSystem::Piece.__init__)


def test_productionsystem::piece_constructor_args():
    sig = inspect.signature(ProductionSystem::Piece.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_productionsystem::piece_has_id():
    assert hasattr(ProductionSystem::Piece, "id")
    descriptor = None
    for klass in ProductionSystem::Piece.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_productionsystem::conveyor_is_not_abstract():
    assert not inspect.isabstract(ProductionSystem::Conveyor)


def test_productionsystem::conveyor_constructor_exists():
    assert callable(ProductionSystem::Conveyor.__init__)


def test_productionsystem::conveyor_constructor_args():
    sig = inspect.signature(ProductionSystem::Conveyor.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "capacity" in params, "Missing parameter 'capacity'"

def test_productionsystem::conveyor_has_id():
    assert hasattr(ProductionSystem::Conveyor, "id")
    descriptor = None
    for klass in ProductionSystem::Conveyor.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_productionsystem::conveyor_has_capacity():
    assert hasattr(ProductionSystem::Conveyor, "capacity")
    descriptor = None
    for klass in ProductionSystem::Conveyor.__mro__:
        if "capacity" in klass.__dict__:
            descriptor = klass.__dict__["capacity"]
            break
    assert isinstance(descriptor, property)



def test_productionsystem::machine_is_not_abstract():
    assert not inspect.isabstract(ProductionSystem::Machine)


def test_productionsystem::machine_constructor_exists():
    assert callable(ProductionSystem::Machine.__init__)


def test_productionsystem::machine_constructor_args():
    sig = inspect.signature(ProductionSystem::Machine.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_productionsystem::machine_has_id():
    assert hasattr(ProductionSystem::Machine, "id")
    descriptor = None
    for klass in ProductionSystem::Machine.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_piece_is_not_abstract():
    assert not inspect.isabstract(Piece)


def test_piece_constructor_exists():
    assert callable(Piece.__init__)


def test_piece_constructor_args():
    sig = inspect.signature(Piece.__init__)
    params = list(sig.parameters.keys())



def test_productionsystem::processed_is_not_abstract():
    assert not inspect.isabstract(ProductionSystem::Processed)


def test_productionsystem::processed_constructor_exists():
    assert callable(ProductionSystem::Processed.__init__)


def test_productionsystem::processed_constructor_args():
    sig = inspect.signature(ProductionSystem::Processed.__init__)
    params = list(sig.parameters.keys())



def test_productionsystem::raw_is_not_abstract():
    assert not inspect.isabstract(ProductionSystem::Raw)


def test_productionsystem::raw_constructor_exists():
    assert callable(ProductionSystem::Raw.__init__)


def test_productionsystem::raw_constructor_args():
    sig = inspect.signature(ProductionSystem::Raw.__init__)
    params = list(sig.parameters.keys())


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
ProductionSystem::Piece_strategy = st.builds(
    ProductionSystem::Piece,
    id=
        safe_text
)
ProductionSystem::Conveyor_strategy = st.builds(
    ProductionSystem::Conveyor,
    id=
        safe_text,
    capacity=
        st.integers()
)
ProductionSystem::Machine_strategy = st.builds(
    ProductionSystem::Machine,
    id=
        safe_text
)
Piece_strategy = st.builds(
    Piece,
)
ProductionSystem::Processed_strategy = st.builds(
    ProductionSystem::Processed,
)
ProductionSystem::Raw_strategy = st.builds(
    ProductionSystem::Raw,
)

@given(instance=ProductionSystem::Piece_strategy)
@settings(max_examples=50)
def test_productionsystem::piece_instantiation(instance):
    assert isinstance(instance, ProductionSystem::Piece)

@given(instance=ProductionSystem::Piece_strategy)
def test_productionsystem::piece_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=ProductionSystem::Piece_strategy)
def test_productionsystem::piece_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=ProductionSystem::Conveyor_strategy)
@settings(max_examples=50)
def test_productionsystem::conveyor_instantiation(instance):
    assert isinstance(instance, ProductionSystem::Conveyor)

@given(instance=ProductionSystem::Conveyor_strategy)
def test_productionsystem::conveyor_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=ProductionSystem::Conveyor_strategy)
def test_productionsystem::conveyor_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=ProductionSystem::Conveyor_strategy)
def test_productionsystem::conveyor_capacity_type(instance):
    assert isinstance(instance.capacity, int)


@given(instance=ProductionSystem::Conveyor_strategy)
def test_productionsystem::conveyor_capacity_setter(instance):
    original = instance.capacity
    instance.capacity = original
    assert instance.capacity == original

@given(instance=ProductionSystem::Machine_strategy)
@settings(max_examples=50)
def test_productionsystem::machine_instantiation(instance):
    assert isinstance(instance, ProductionSystem::Machine)

@given(instance=ProductionSystem::Machine_strategy)
def test_productionsystem::machine_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=ProductionSystem::Machine_strategy)
def test_productionsystem::machine_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Piece_strategy)
@settings(max_examples=50)
def test_piece_instantiation(instance):
    assert isinstance(instance, Piece)

@given(instance=ProductionSystem::Processed_strategy)
@settings(max_examples=50)
def test_productionsystem::processed_instantiation(instance):
    assert isinstance(instance, ProductionSystem::Processed)

@given(instance=ProductionSystem::Raw_strategy)
@settings(max_examples=50)
def test_productionsystem::raw_instantiation(instance):
    assert isinstance(instance, ProductionSystem::Raw)
