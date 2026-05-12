import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Boolean_external,
    Handicapped_Space,
    Regular_Space,
    Class,
    Parking_Level,
    Convertible,
    Electric,
    Motorbike,
    Truck,
    Car,
    Vehicle_Interface,
    Parking_Space,
    Parking_Structure,
    Parking_Space_Type,
    Enumeration,
    Structure_Type,
    Enumeration2,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_boolean_external_is_not_abstract():
    assert not inspect.isabstract(Boolean_external)


def test_boolean_external_constructor_exists():
    assert callable(Boolean_external.__init__)


def test_boolean_external_constructor_args():
    sig = inspect.signature(Boolean_external.__init__)
    params = list(sig.parameters.keys())



def test_handicapped_space_is_not_abstract():
    assert not inspect.isabstract(Handicapped_Space)


def test_handicapped_space_constructor_exists():
    assert callable(Handicapped_Space.__init__)


def test_handicapped_space_constructor_args():
    sig = inspect.signature(Handicapped_Space.__init__)
    params = list(sig.parameters.keys())



def test_regular_space_is_not_abstract():
    assert not inspect.isabstract(Regular_Space)


def test_regular_space_constructor_exists():
    assert callable(Regular_Space.__init__)


def test_regular_space_constructor_args():
    sig = inspect.signature(Regular_Space.__init__)
    params = list(sig.parameters.keys())



def test_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_class_constructor_exists():
    assert callable(Class.__init__)


def test_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_parking_level_is_not_abstract():
    assert not inspect.isabstract(Parking_Level)


def test_parking_level_constructor_exists():
    assert callable(Parking_Level.__init__)


def test_parking_level_constructor_args():
    sig = inspect.signature(Parking_Level.__init__)
    params = list(sig.parameters.keys())
    assert "Fl_Number" in params, "Missing parameter 'Fl_Number'"

def test_parking_level_has_Fl_Number():
    assert hasattr(Parking_Level, "Fl_Number")
    descriptor = None
    for klass in Parking_Level.__mro__:
        if "Fl_Number" in klass.__dict__:
            descriptor = klass.__dict__["Fl_Number"]
            break
    assert isinstance(descriptor, property)



def test_convertible_is_not_abstract():
    assert not inspect.isabstract(Convertible)


def test_convertible_constructor_exists():
    assert callable(Convertible.__init__)


def test_convertible_constructor_args():
    sig = inspect.signature(Convertible.__init__)
    params = list(sig.parameters.keys())



def test_electric_is_not_abstract():
    assert not inspect.isabstract(Electric)


def test_electric_constructor_exists():
    assert callable(Electric.__init__)


def test_electric_constructor_args():
    sig = inspect.signature(Electric.__init__)
    params = list(sig.parameters.keys())



def test_motorbike_is_not_abstract():
    assert not inspect.isabstract(Motorbike)


def test_motorbike_constructor_exists():
    assert callable(Motorbike.__init__)


def test_motorbike_constructor_args():
    sig = inspect.signature(Motorbike.__init__)
    params = list(sig.parameters.keys())



def test_truck_is_not_abstract():
    assert not inspect.isabstract(Truck)


def test_truck_constructor_exists():
    assert callable(Truck.__init__)


def test_truck_constructor_args():
    sig = inspect.signature(Truck.__init__)
    params = list(sig.parameters.keys())



def test_car_is_not_abstract():
    assert not inspect.isabstract(Car)


def test_car_constructor_exists():
    assert callable(Car.__init__)


def test_car_constructor_args():
    sig = inspect.signature(Car.__init__)
    params = list(sig.parameters.keys())



def test_vehicle_interface_is_not_abstract():
    assert not inspect.isabstract(Vehicle_Interface)


def test_vehicle_interface_constructor_exists():
    assert callable(Vehicle_Interface.__init__)


def test_vehicle_interface_constructor_args():
    sig = inspect.signature(Vehicle_Interface.__init__)
    params = list(sig.parameters.keys())



def test_parking_space_is_not_abstract():
    assert not inspect.isabstract(Parking_Space)


def test_parking_space_constructor_exists():
    assert callable(Parking_Space.__init__)


def test_parking_space_constructor_args():
    sig = inspect.signature(Parking_Space.__init__)
    params = list(sig.parameters.keys())
    assert "Floor_Number" in params, "Missing parameter 'Floor_Number'"
    assert "Space_Type" in params, "Missing parameter 'Space_Type'"
    assert "Space_Number" in params, "Missing parameter 'Space_Number'"

def test_parking_space_has_Floor_Number():
    assert hasattr(Parking_Space, "Floor_Number")
    descriptor = None
    for klass in Parking_Space.__mro__:
        if "Floor_Number" in klass.__dict__:
            descriptor = klass.__dict__["Floor_Number"]
            break
    assert isinstance(descriptor, property)

def test_parking_space_has_Space_Type():
    assert hasattr(Parking_Space, "Space_Type")
    descriptor = None
    for klass in Parking_Space.__mro__:
        if "Space_Type" in klass.__dict__:
            descriptor = klass.__dict__["Space_Type"]
            break
    assert isinstance(descriptor, property)

def test_parking_space_has_Space_Number():
    assert hasattr(Parking_Space, "Space_Number")
    descriptor = None
    for klass in Parking_Space.__mro__:
        if "Space_Number" in klass.__dict__:
            descriptor = klass.__dict__["Space_Number"]
            break
    assert isinstance(descriptor, property)



def test_parking_structure_is_not_abstract():
    assert not inspect.isabstract(Parking_Structure)


def test_parking_structure_constructor_exists():
    assert callable(Parking_Structure.__init__)


def test_parking_structure_constructor_args():
    sig = inspect.signature(Parking_Structure.__init__)
    params = list(sig.parameters.keys())
    assert "City" in params, "Missing parameter 'City'"
    assert "Type" in params, "Missing parameter 'Type'"
    assert "Address" in params, "Missing parameter 'Address'"

def test_parking_structure_has_City():
    assert hasattr(Parking_Structure, "City")
    descriptor = None
    for klass in Parking_Structure.__mro__:
        if "City" in klass.__dict__:
            descriptor = klass.__dict__["City"]
            break
    assert isinstance(descriptor, property)

def test_parking_structure_has_Type():
    assert hasattr(Parking_Structure, "Type")
    descriptor = None
    for klass in Parking_Structure.__mro__:
        if "Type" in klass.__dict__:
            descriptor = klass.__dict__["Type"]
            break
    assert isinstance(descriptor, property)

def test_parking_structure_has_Address():
    assert hasattr(Parking_Structure, "Address")
    descriptor = None
    for klass in Parking_Structure.__mro__:
        if "Address" in klass.__dict__:
            descriptor = klass.__dict__["Address"]
            break
    assert isinstance(descriptor, property)

def test_parking_space_type_exists():
    # Check that the Enumeration exists
    assert Parking_Space_Type is not None

def test_parking_space_type_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Parking_Space_Type]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Parking_Space_Type"

def test_enumeration_exists():
    # Check that the Enumeration exists
    assert Enumeration is not None

def test_enumeration_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Enumeration]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Enumeration"

def test_structure_type_exists():
    # Check that the Enumeration exists
    assert Structure_Type is not None

def test_structure_type_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Structure_Type]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Structure_Type"

def test_enumeration2_exists():
    # Check that the Enumeration exists
    assert Enumeration2 is not None

def test_enumeration2_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Enumeration2]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Enumeration2"


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
Boolean_external_strategy = st.builds(
    Boolean_external,
)
Handicapped_Space_strategy = st.builds(
    Handicapped_Space,
)
Regular_Space_strategy = st.builds(
    Regular_Space,
)
Class_strategy = st.builds(
    Class,
)
Parking_Level_strategy = st.builds(
    Parking_Level,
    Fl_Number=
        st.integers()
)
Convertible_strategy = st.builds(
    Convertible,
)
Electric_strategy = st.builds(
    Electric,
)
Motorbike_strategy = st.builds(
    Motorbike,
)
Truck_strategy = st.builds(
    Truck,
)
Car_strategy = st.builds(
    Car,
)
Vehicle_Interface_strategy = st.builds(
    Vehicle_Interface,
)
Parking_Space_strategy = st.builds(
    Parking_Space,
    Floor_Number=
        st.none(),
    Space_Type=
        st.none(),
    Space_Number=
        st.integers()
)
Parking_Structure_strategy = st.builds(
    Parking_Structure,
    City=
        safe_text,
    Type=
        st.none(),
    Address=
        safe_text
)

@given(instance=Boolean_external_strategy)
@settings(max_examples=50)
def test_boolean_external_instantiation(instance):
    assert isinstance(instance, Boolean_external)

@given(instance=Handicapped_Space_strategy)
@settings(max_examples=50)
def test_handicapped_space_instantiation(instance):
    assert isinstance(instance, Handicapped_Space)

@given(instance=Regular_Space_strategy)
@settings(max_examples=50)
def test_regular_space_instantiation(instance):
    assert isinstance(instance, Regular_Space)

@given(instance=Class_strategy)
@settings(max_examples=50)
def test_class_instantiation(instance):
    assert isinstance(instance, Class)

@given(instance=Parking_Level_strategy)
@settings(max_examples=50)
def test_parking_level_instantiation(instance):
    assert isinstance(instance, Parking_Level)



@given(instance=Parking_Level_strategy)
def test_parking_level_Fl_Number_setter(instance):
    original = instance.Fl_Number
    instance.Fl_Number = original
    assert instance.Fl_Number == original

@given(instance=Convertible_strategy)
@settings(max_examples=50)
def test_convertible_instantiation(instance):
    assert isinstance(instance, Convertible)

@given(instance=Electric_strategy)
@settings(max_examples=50)
def test_electric_instantiation(instance):
    assert isinstance(instance, Electric)

@given(instance=Motorbike_strategy)
@settings(max_examples=50)
def test_motorbike_instantiation(instance):
    assert isinstance(instance, Motorbike)

@given(instance=Truck_strategy)
@settings(max_examples=50)
def test_truck_instantiation(instance):
    assert isinstance(instance, Truck)

@given(instance=Car_strategy)
@settings(max_examples=50)
def test_car_instantiation(instance):
    assert isinstance(instance, Car)

@given(instance=Vehicle_Interface_strategy)
@settings(max_examples=50)
def test_vehicle_interface_instantiation(instance):
    assert isinstance(instance, Vehicle_Interface)

@given(instance=Parking_Space_strategy)
@settings(max_examples=50)
def test_parking_space_instantiation(instance):
    assert isinstance(instance, Parking_Space)



@given(instance=Parking_Space_strategy)
def test_parking_space_Floor_Number_setter(instance):
    original = instance.Floor_Number
    instance.Floor_Number = original
    assert instance.Floor_Number == original



@given(instance=Parking_Space_strategy)
def test_parking_space_Space_Type_setter(instance):
    original = instance.Space_Type
    instance.Space_Type = original
    assert instance.Space_Type == original



@given(instance=Parking_Space_strategy)
def test_parking_space_Space_Number_setter(instance):
    original = instance.Space_Number
    instance.Space_Number = original
    assert instance.Space_Number == original

@given(instance=Parking_Structure_strategy)
@settings(max_examples=50)
def test_parking_structure_instantiation(instance):
    assert isinstance(instance, Parking_Structure)



@given(instance=Parking_Structure_strategy)
def test_parking_structure_City_setter(instance):
    original = instance.City
    instance.City = original
    assert instance.City == original



@given(instance=Parking_Structure_strategy)
def test_parking_structure_Type_setter(instance):
    original = instance.Type
    instance.Type = original
    assert instance.Type == original



@given(instance=Parking_Structure_strategy)
def test_parking_structure_Address_setter(instance):
    original = instance.Address
    instance.Address = original
    assert instance.Address == original
