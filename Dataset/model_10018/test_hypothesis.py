import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ProductionSystem_Piece,
    ProductionSystem_Conveyor,
    ProductionSystem_Machine,
    Piece,
    ProductionSystem_Processed,
    ProductionSystem_Raw,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_productionsystem_piece_is_not_abstract():
    assert not inspect.isabstract(ProductionSystem_Piece)


def test_productionsystem_piece_constructor_exists():
    assert callable(ProductionSystem_Piece.__init__)


def test_productionsystem_piece_constructor_args():
    sig = inspect.signature(ProductionSystem_Piece.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_productionsystem_piece_has_id():
    assert hasattr(ProductionSystem_Piece, "id")
    descriptor = None
    for klass in ProductionSystem_Piece.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_productionsystem_conveyor_is_not_abstract():
    assert not inspect.isabstract(ProductionSystem_Conveyor)


def test_productionsystem_conveyor_constructor_exists():
    assert callable(ProductionSystem_Conveyor.__init__)


def test_productionsystem_conveyor_constructor_args():
    sig = inspect.signature(ProductionSystem_Conveyor.__init__)
    params = list(sig.parameters.keys())
    assert "capacity" in params, "Missing parameter 'capacity'"
    assert "id" in params, "Missing parameter 'id'"

def test_productionsystem_conveyor_has_capacity():
    assert hasattr(ProductionSystem_Conveyor, "capacity")
    descriptor = None
    for klass in ProductionSystem_Conveyor.__mro__:
        if "capacity" in klass.__dict__:
            descriptor = klass.__dict__["capacity"]
            break
    assert isinstance(descriptor, property)

def test_productionsystem_conveyor_has_id():
    assert hasattr(ProductionSystem_Conveyor, "id")
    descriptor = None
    for klass in ProductionSystem_Conveyor.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_productionsystem_machine_is_not_abstract():
    assert not inspect.isabstract(ProductionSystem_Machine)


def test_productionsystem_machine_constructor_exists():
    assert callable(ProductionSystem_Machine.__init__)


def test_productionsystem_machine_constructor_args():
    sig = inspect.signature(ProductionSystem_Machine.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_productionsystem_machine_has_id():
    assert hasattr(ProductionSystem_Machine, "id")
    descriptor = None
    for klass in ProductionSystem_Machine.__mro__:
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



def test_productionsystem_processed_is_not_abstract():
    assert not inspect.isabstract(ProductionSystem_Processed)


def test_productionsystem_processed_constructor_exists():
    assert callable(ProductionSystem_Processed.__init__)


def test_productionsystem_processed_constructor_args():
    sig = inspect.signature(ProductionSystem_Processed.__init__)
    params = list(sig.parameters.keys())



def test_productionsystem_raw_is_not_abstract():
    assert not inspect.isabstract(ProductionSystem_Raw)


def test_productionsystem_raw_constructor_exists():
    assert callable(ProductionSystem_Raw.__init__)


def test_productionsystem_raw_constructor_args():
    sig = inspect.signature(ProductionSystem_Raw.__init__)
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
ProductionSystem_Piece_strategy = st.builds(
    ProductionSystem_Piece,
    id=
        safe_text
)
ProductionSystem_Conveyor_strategy = st.builds(
    ProductionSystem_Conveyor,
    capacity=
        st.integers(),
    id=
        safe_text
)
ProductionSystem_Machine_strategy = st.builds(
    ProductionSystem_Machine,
    id=
        safe_text
)
Piece_strategy = st.builds(
    Piece,
)
ProductionSystem_Processed_strategy = st.builds(
    ProductionSystem_Processed,
)
ProductionSystem_Raw_strategy = st.builds(
    ProductionSystem_Raw,
)

@given(instance=ProductionSystem_Piece_strategy)
@settings(max_examples=50)
def test_productionsystem_piece_instantiation(instance):
    assert isinstance(instance, ProductionSystem_Piece)



@given(instance=ProductionSystem_Piece_strategy)
def test_productionsystem_piece_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=ProductionSystem_Conveyor_strategy)
@settings(max_examples=50)
def test_productionsystem_conveyor_instantiation(instance):
    assert isinstance(instance, ProductionSystem_Conveyor)



@given(instance=ProductionSystem_Conveyor_strategy)
def test_productionsystem_conveyor_capacity_setter(instance):
    original = instance.capacity
    instance.capacity = original
    assert instance.capacity == original



@given(instance=ProductionSystem_Conveyor_strategy)
def test_productionsystem_conveyor_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=ProductionSystem_Machine_strategy)
@settings(max_examples=50)
def test_productionsystem_machine_instantiation(instance):
    assert isinstance(instance, ProductionSystem_Machine)



@given(instance=ProductionSystem_Machine_strategy)
def test_productionsystem_machine_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Piece_strategy)
@settings(max_examples=50)
def test_piece_instantiation(instance):
    assert isinstance(instance, Piece)

@given(instance=ProductionSystem_Processed_strategy)
@settings(max_examples=50)
def test_productionsystem_processed_instantiation(instance):
    assert isinstance(instance, ProductionSystem_Processed)

@given(instance=ProductionSystem_Raw_strategy)
@settings(max_examples=50)
def test_productionsystem_raw_instantiation(instance):
    assert isinstance(instance, ProductionSystem_Raw)
