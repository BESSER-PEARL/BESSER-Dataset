import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    EA::Model::Vehicle,
    Vehicle,
    EA::Model::TravelingVehicle,
    EA::Model::Travel,
    Roadway,
    EA::Model::Roadway,
    RoadTrafficAccident,
    EA::Model::RearEndCollision,
    EA::Model::Person,
    Traveler,
    EA::Model::Passenger,
    EA::Model::Victim,
    EA::Model::Driver,
    Person,
    EA::Model::Traveler,
    EA::Model::LivingPerson,
    EA::Model::DeceasedPerson,
    EA::Model::RoadTrafficAccident,
    TravelingVehicle,
    EA::Model::CrashedVehicle,
    EA::Model::RoadwayWithAccident,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_ea::model::vehicle_is_not_abstract():
    assert not inspect.isabstract(EA::Model::Vehicle)


def test_ea::model::vehicle_constructor_exists():
    assert callable(EA::Model::Vehicle.__init__)


def test_ea::model::vehicle_constructor_args():
    sig = inspect.signature(EA::Model::Vehicle.__init__)
    params = list(sig.parameters.keys())



def test_vehicle_is_not_abstract():
    assert not inspect.isabstract(Vehicle)


def test_vehicle_constructor_exists():
    assert callable(Vehicle.__init__)


def test_vehicle_constructor_args():
    sig = inspect.signature(Vehicle.__init__)
    params = list(sig.parameters.keys())



def test_ea::model::travelingvehicle_is_not_abstract():
    assert not inspect.isabstract(EA::Model::TravelingVehicle)


def test_ea::model::travelingvehicle_constructor_exists():
    assert callable(EA::Model::TravelingVehicle.__init__)


def test_ea::model::travelingvehicle_constructor_args():
    sig = inspect.signature(EA::Model::TravelingVehicle.__init__)
    params = list(sig.parameters.keys())



def test_ea::model::travel_is_not_abstract():
    assert not inspect.isabstract(EA::Model::Travel)


def test_ea::model::travel_constructor_exists():
    assert callable(EA::Model::Travel.__init__)


def test_ea::model::travel_constructor_args():
    sig = inspect.signature(EA::Model::Travel.__init__)
    params = list(sig.parameters.keys())



def test_roadway_is_not_abstract():
    assert not inspect.isabstract(Roadway)


def test_roadway_constructor_exists():
    assert callable(Roadway.__init__)


def test_roadway_constructor_args():
    sig = inspect.signature(Roadway.__init__)
    params = list(sig.parameters.keys())



def test_ea::model::roadway_is_not_abstract():
    assert not inspect.isabstract(EA::Model::Roadway)


def test_ea::model::roadway_constructor_exists():
    assert callable(EA::Model::Roadway.__init__)


def test_ea::model::roadway_constructor_args():
    sig = inspect.signature(EA::Model::Roadway.__init__)
    params = list(sig.parameters.keys())



def test_roadtrafficaccident_is_not_abstract():
    assert not inspect.isabstract(RoadTrafficAccident)


def test_roadtrafficaccident_constructor_exists():
    assert callable(RoadTrafficAccident.__init__)


def test_roadtrafficaccident_constructor_args():
    sig = inspect.signature(RoadTrafficAccident.__init__)
    params = list(sig.parameters.keys())



def test_ea::model::rearendcollision_is_not_abstract():
    assert not inspect.isabstract(EA::Model::RearEndCollision)


def test_ea::model::rearendcollision_constructor_exists():
    assert callable(EA::Model::RearEndCollision.__init__)


def test_ea::model::rearendcollision_constructor_args():
    sig = inspect.signature(EA::Model::RearEndCollision.__init__)
    params = list(sig.parameters.keys())



def test_ea::model::person_is_not_abstract():
    assert not inspect.isabstract(EA::Model::Person)


def test_ea::model::person_constructor_exists():
    assert callable(EA::Model::Person.__init__)


def test_ea::model::person_constructor_args():
    sig = inspect.signature(EA::Model::Person.__init__)
    params = list(sig.parameters.keys())



def test_traveler_is_not_abstract():
    assert not inspect.isabstract(Traveler)


def test_traveler_constructor_exists():
    assert callable(Traveler.__init__)


def test_traveler_constructor_args():
    sig = inspect.signature(Traveler.__init__)
    params = list(sig.parameters.keys())



def test_ea::model::passenger_is_not_abstract():
    assert not inspect.isabstract(EA::Model::Passenger)


def test_ea::model::passenger_constructor_exists():
    assert callable(EA::Model::Passenger.__init__)


def test_ea::model::passenger_constructor_args():
    sig = inspect.signature(EA::Model::Passenger.__init__)
    params = list(sig.parameters.keys())



def test_ea::model::victim_is_not_abstract():
    assert not inspect.isabstract(EA::Model::Victim)


def test_ea::model::victim_constructor_exists():
    assert callable(EA::Model::Victim.__init__)


def test_ea::model::victim_constructor_args():
    sig = inspect.signature(EA::Model::Victim.__init__)
    params = list(sig.parameters.keys())



def test_ea::model::driver_is_not_abstract():
    assert not inspect.isabstract(EA::Model::Driver)


def test_ea::model::driver_constructor_exists():
    assert callable(EA::Model::Driver.__init__)


def test_ea::model::driver_constructor_args():
    sig = inspect.signature(EA::Model::Driver.__init__)
    params = list(sig.parameters.keys())



def test_person_is_not_abstract():
    assert not inspect.isabstract(Person)


def test_person_constructor_exists():
    assert callable(Person.__init__)


def test_person_constructor_args():
    sig = inspect.signature(Person.__init__)
    params = list(sig.parameters.keys())



def test_ea::model::traveler_is_not_abstract():
    assert not inspect.isabstract(EA::Model::Traveler)


def test_ea::model::traveler_constructor_exists():
    assert callable(EA::Model::Traveler.__init__)


def test_ea::model::traveler_constructor_args():
    sig = inspect.signature(EA::Model::Traveler.__init__)
    params = list(sig.parameters.keys())



def test_ea::model::livingperson_is_not_abstract():
    assert not inspect.isabstract(EA::Model::LivingPerson)


def test_ea::model::livingperson_constructor_exists():
    assert callable(EA::Model::LivingPerson.__init__)


def test_ea::model::livingperson_constructor_args():
    sig = inspect.signature(EA::Model::LivingPerson.__init__)
    params = list(sig.parameters.keys())



def test_ea::model::deceasedperson_is_not_abstract():
    assert not inspect.isabstract(EA::Model::DeceasedPerson)


def test_ea::model::deceasedperson_constructor_exists():
    assert callable(EA::Model::DeceasedPerson.__init__)


def test_ea::model::deceasedperson_constructor_args():
    sig = inspect.signature(EA::Model::DeceasedPerson.__init__)
    params = list(sig.parameters.keys())



def test_ea::model::roadtrafficaccident_is_not_abstract():
    assert not inspect.isabstract(EA::Model::RoadTrafficAccident)


def test_ea::model::roadtrafficaccident_constructor_exists():
    assert callable(EA::Model::RoadTrafficAccident.__init__)


def test_ea::model::roadtrafficaccident_constructor_args():
    sig = inspect.signature(EA::Model::RoadTrafficAccident.__init__)
    params = list(sig.parameters.keys())
    assert "fatalvictims" in params, "Missing parameter 'fatalvictims'"

def test_ea::model::roadtrafficaccident_has_fatalvictims():
    assert hasattr(EA::Model::RoadTrafficAccident, "fatalvictims")
    descriptor = None
    for klass in EA::Model::RoadTrafficAccident.__mro__:
        if "fatalvictims" in klass.__dict__:
            descriptor = klass.__dict__["fatalvictims"]
            break
    assert isinstance(descriptor, property)



def test_travelingvehicle_is_not_abstract():
    assert not inspect.isabstract(TravelingVehicle)


def test_travelingvehicle_constructor_exists():
    assert callable(TravelingVehicle.__init__)


def test_travelingvehicle_constructor_args():
    sig = inspect.signature(TravelingVehicle.__init__)
    params = list(sig.parameters.keys())



def test_ea::model::crashedvehicle_is_not_abstract():
    assert not inspect.isabstract(EA::Model::CrashedVehicle)


def test_ea::model::crashedvehicle_constructor_exists():
    assert callable(EA::Model::CrashedVehicle.__init__)


def test_ea::model::crashedvehicle_constructor_args():
    sig = inspect.signature(EA::Model::CrashedVehicle.__init__)
    params = list(sig.parameters.keys())



def test_ea::model::roadwaywithaccident_is_not_abstract():
    assert not inspect.isabstract(EA::Model::RoadwayWithAccident)


def test_ea::model::roadwaywithaccident_constructor_exists():
    assert callable(EA::Model::RoadwayWithAccident.__init__)


def test_ea::model::roadwaywithaccident_constructor_args():
    sig = inspect.signature(EA::Model::RoadwayWithAccident.__init__)
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
EA::Model::Vehicle_strategy = st.builds(
    EA::Model::Vehicle,
)
Vehicle_strategy = st.builds(
    Vehicle,
)
EA::Model::TravelingVehicle_strategy = st.builds(
    EA::Model::TravelingVehicle,
)
EA::Model::Travel_strategy = st.builds(
    EA::Model::Travel,
)
Roadway_strategy = st.builds(
    Roadway,
)
EA::Model::Roadway_strategy = st.builds(
    EA::Model::Roadway,
)
RoadTrafficAccident_strategy = st.builds(
    RoadTrafficAccident,
)
EA::Model::RearEndCollision_strategy = st.builds(
    EA::Model::RearEndCollision,
)
EA::Model::Person_strategy = st.builds(
    EA::Model::Person,
)
Traveler_strategy = st.builds(
    Traveler,
)
EA::Model::Passenger_strategy = st.builds(
    EA::Model::Passenger,
)
EA::Model::Victim_strategy = st.builds(
    EA::Model::Victim,
)
EA::Model::Driver_strategy = st.builds(
    EA::Model::Driver,
)
Person_strategy = st.builds(
    Person,
)
EA::Model::Traveler_strategy = st.builds(
    EA::Model::Traveler,
)
EA::Model::LivingPerson_strategy = st.builds(
    EA::Model::LivingPerson,
)
EA::Model::DeceasedPerson_strategy = st.builds(
    EA::Model::DeceasedPerson,
)
EA::Model::RoadTrafficAccident_strategy = st.builds(
    EA::Model::RoadTrafficAccident,
    fatalvictims=
        st.integers()
)
TravelingVehicle_strategy = st.builds(
    TravelingVehicle,
)
EA::Model::CrashedVehicle_strategy = st.builds(
    EA::Model::CrashedVehicle,
)
EA::Model::RoadwayWithAccident_strategy = st.builds(
    EA::Model::RoadwayWithAccident,
)

@given(instance=EA::Model::Vehicle_strategy)
@settings(max_examples=50)
def test_ea::model::vehicle_instantiation(instance):
    assert isinstance(instance, EA::Model::Vehicle)

@given(instance=Vehicle_strategy)
@settings(max_examples=50)
def test_vehicle_instantiation(instance):
    assert isinstance(instance, Vehicle)

@given(instance=EA::Model::TravelingVehicle_strategy)
@settings(max_examples=50)
def test_ea::model::travelingvehicle_instantiation(instance):
    assert isinstance(instance, EA::Model::TravelingVehicle)

@given(instance=EA::Model::Travel_strategy)
@settings(max_examples=50)
def test_ea::model::travel_instantiation(instance):
    assert isinstance(instance, EA::Model::Travel)

@given(instance=Roadway_strategy)
@settings(max_examples=50)
def test_roadway_instantiation(instance):
    assert isinstance(instance, Roadway)

@given(instance=EA::Model::Roadway_strategy)
@settings(max_examples=50)
def test_ea::model::roadway_instantiation(instance):
    assert isinstance(instance, EA::Model::Roadway)

@given(instance=RoadTrafficAccident_strategy)
@settings(max_examples=50)
def test_roadtrafficaccident_instantiation(instance):
    assert isinstance(instance, RoadTrafficAccident)

@given(instance=EA::Model::RearEndCollision_strategy)
@settings(max_examples=50)
def test_ea::model::rearendcollision_instantiation(instance):
    assert isinstance(instance, EA::Model::RearEndCollision)

@given(instance=EA::Model::Person_strategy)
@settings(max_examples=50)
def test_ea::model::person_instantiation(instance):
    assert isinstance(instance, EA::Model::Person)

@given(instance=Traveler_strategy)
@settings(max_examples=50)
def test_traveler_instantiation(instance):
    assert isinstance(instance, Traveler)

@given(instance=EA::Model::Passenger_strategy)
@settings(max_examples=50)
def test_ea::model::passenger_instantiation(instance):
    assert isinstance(instance, EA::Model::Passenger)

@given(instance=EA::Model::Victim_strategy)
@settings(max_examples=50)
def test_ea::model::victim_instantiation(instance):
    assert isinstance(instance, EA::Model::Victim)

@given(instance=EA::Model::Driver_strategy)
@settings(max_examples=50)
def test_ea::model::driver_instantiation(instance):
    assert isinstance(instance, EA::Model::Driver)

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)

@given(instance=EA::Model::Traveler_strategy)
@settings(max_examples=50)
def test_ea::model::traveler_instantiation(instance):
    assert isinstance(instance, EA::Model::Traveler)

@given(instance=EA::Model::LivingPerson_strategy)
@settings(max_examples=50)
def test_ea::model::livingperson_instantiation(instance):
    assert isinstance(instance, EA::Model::LivingPerson)

@given(instance=EA::Model::DeceasedPerson_strategy)
@settings(max_examples=50)
def test_ea::model::deceasedperson_instantiation(instance):
    assert isinstance(instance, EA::Model::DeceasedPerson)

@given(instance=EA::Model::RoadTrafficAccident_strategy)
@settings(max_examples=50)
def test_ea::model::roadtrafficaccident_instantiation(instance):
    assert isinstance(instance, EA::Model::RoadTrafficAccident)

@given(instance=EA::Model::RoadTrafficAccident_strategy)
def test_ea::model::roadtrafficaccident_fatalvictims_type(instance):
    assert isinstance(instance.fatalvictims, int)


@given(instance=EA::Model::RoadTrafficAccident_strategy)
def test_ea::model::roadtrafficaccident_fatalvictims_setter(instance):
    original = instance.fatalvictims
    instance.fatalvictims = original
    assert instance.fatalvictims == original

@given(instance=TravelingVehicle_strategy)
@settings(max_examples=50)
def test_travelingvehicle_instantiation(instance):
    assert isinstance(instance, TravelingVehicle)

@given(instance=EA::Model::CrashedVehicle_strategy)
@settings(max_examples=50)
def test_ea::model::crashedvehicle_instantiation(instance):
    assert isinstance(instance, EA::Model::CrashedVehicle)

@given(instance=EA::Model::RoadwayWithAccident_strategy)
@settings(max_examples=50)
def test_ea::model::roadwaywithaccident_instantiation(instance):
    assert isinstance(instance, EA::Model::RoadwayWithAccident)
