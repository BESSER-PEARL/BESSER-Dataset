import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Common_fuctions,
    customer_Actor,
    print_ticket_UseCase,
    reserve_seats_UseCase,
    make_payment_UseCase,
    confirm_purchase_UseCase,
    select_flight_UseCase,
    search_flights_UseCase,
    enter_no__of_tickets_UseCase,
    enter_date_UseCase,
    enter_airport_UseCase1,
    round_trip_or_one_way__UseCase,
    Reservation_System_Actor1,
    UseCase_UseCase,
    enter_airport_UseCase,
    round_trip_or_one_way_UseCase,
    Reservation_System_Actor,
    Ticket,
    Booking_counter,
    Agent,
    Customer,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_common_fuctions_is_not_abstract():
    assert not inspect.isabstract(Common_fuctions)


def test_common_fuctions_constructor_exists():
    assert callable(Common_fuctions.__init__)


def test_common_fuctions_constructor_args():
    sig = inspect.signature(Common_fuctions.__init__)
    params = list(sig.parameters.keys())



def test_customer_actor_is_not_abstract():
    assert not inspect.isabstract(customer_Actor)


def test_customer_actor_constructor_exists():
    assert callable(customer_Actor.__init__)


def test_customer_actor_constructor_args():
    sig = inspect.signature(customer_Actor.__init__)
    params = list(sig.parameters.keys())



def test_print_ticket_usecase_is_not_abstract():
    assert not inspect.isabstract(print_ticket_UseCase)


def test_print_ticket_usecase_constructor_exists():
    assert callable(print_ticket_UseCase.__init__)


def test_print_ticket_usecase_constructor_args():
    sig = inspect.signature(print_ticket_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_reserve_seats_usecase_is_not_abstract():
    assert not inspect.isabstract(reserve_seats_UseCase)


def test_reserve_seats_usecase_constructor_exists():
    assert callable(reserve_seats_UseCase.__init__)


def test_reserve_seats_usecase_constructor_args():
    sig = inspect.signature(reserve_seats_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_make_payment_usecase_is_not_abstract():
    assert not inspect.isabstract(make_payment_UseCase)


def test_make_payment_usecase_constructor_exists():
    assert callable(make_payment_UseCase.__init__)


def test_make_payment_usecase_constructor_args():
    sig = inspect.signature(make_payment_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_confirm_purchase_usecase_is_not_abstract():
    assert not inspect.isabstract(confirm_purchase_UseCase)


def test_confirm_purchase_usecase_constructor_exists():
    assert callable(confirm_purchase_UseCase.__init__)


def test_confirm_purchase_usecase_constructor_args():
    sig = inspect.signature(confirm_purchase_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_select_flight_usecase_is_not_abstract():
    assert not inspect.isabstract(select_flight_UseCase)


def test_select_flight_usecase_constructor_exists():
    assert callable(select_flight_UseCase.__init__)


def test_select_flight_usecase_constructor_args():
    sig = inspect.signature(select_flight_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_search_flights_usecase_is_not_abstract():
    assert not inspect.isabstract(search_flights_UseCase)


def test_search_flights_usecase_constructor_exists():
    assert callable(search_flights_UseCase.__init__)


def test_search_flights_usecase_constructor_args():
    sig = inspect.signature(search_flights_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_enter_no__of_tickets_usecase_is_not_abstract():
    assert not inspect.isabstract(enter_no__of_tickets_UseCase)


def test_enter_no__of_tickets_usecase_constructor_exists():
    assert callable(enter_no__of_tickets_UseCase.__init__)


def test_enter_no__of_tickets_usecase_constructor_args():
    sig = inspect.signature(enter_no__of_tickets_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_enter_date_usecase_is_not_abstract():
    assert not inspect.isabstract(enter_date_UseCase)


def test_enter_date_usecase_constructor_exists():
    assert callable(enter_date_UseCase.__init__)


def test_enter_date_usecase_constructor_args():
    sig = inspect.signature(enter_date_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_enter_airport_usecase1_is_not_abstract():
    assert not inspect.isabstract(enter_airport_UseCase1)


def test_enter_airport_usecase1_constructor_exists():
    assert callable(enter_airport_UseCase1.__init__)


def test_enter_airport_usecase1_constructor_args():
    sig = inspect.signature(enter_airport_UseCase1.__init__)
    params = list(sig.parameters.keys())



def test_round_trip_or_one_way__usecase_is_not_abstract():
    assert not inspect.isabstract(round_trip_or_one_way__UseCase)


def test_round_trip_or_one_way__usecase_constructor_exists():
    assert callable(round_trip_or_one_way__UseCase.__init__)


def test_round_trip_or_one_way__usecase_constructor_args():
    sig = inspect.signature(round_trip_or_one_way__UseCase.__init__)
    params = list(sig.parameters.keys())



def test_reservation_system_actor1_is_not_abstract():
    assert not inspect.isabstract(Reservation_System_Actor1)


def test_reservation_system_actor1_constructor_exists():
    assert callable(Reservation_System_Actor1.__init__)


def test_reservation_system_actor1_constructor_args():
    sig = inspect.signature(Reservation_System_Actor1.__init__)
    params = list(sig.parameters.keys())



def test_usecase_usecase_is_not_abstract():
    assert not inspect.isabstract(UseCase_UseCase)


def test_usecase_usecase_constructor_exists():
    assert callable(UseCase_UseCase.__init__)


def test_usecase_usecase_constructor_args():
    sig = inspect.signature(UseCase_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_enter_airport_usecase_is_not_abstract():
    assert not inspect.isabstract(enter_airport_UseCase)


def test_enter_airport_usecase_constructor_exists():
    assert callable(enter_airport_UseCase.__init__)


def test_enter_airport_usecase_constructor_args():
    sig = inspect.signature(enter_airport_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_round_trip_or_one_way_usecase_is_not_abstract():
    assert not inspect.isabstract(round_trip_or_one_way_UseCase)


def test_round_trip_or_one_way_usecase_constructor_exists():
    assert callable(round_trip_or_one_way_UseCase.__init__)


def test_round_trip_or_one_way_usecase_constructor_args():
    sig = inspect.signature(round_trip_or_one_way_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_reservation_system_actor_is_not_abstract():
    assert not inspect.isabstract(Reservation_System_Actor)


def test_reservation_system_actor_constructor_exists():
    assert callable(Reservation_System_Actor.__init__)


def test_reservation_system_actor_constructor_args():
    sig = inspect.signature(Reservation_System_Actor.__init__)
    params = list(sig.parameters.keys())



def test_ticket_is_not_abstract():
    assert not inspect.isabstract(Ticket)


def test_ticket_constructor_exists():
    assert callable(Ticket.__init__)


def test_ticket_constructor_args():
    sig = inspect.signature(Ticket.__init__)
    params = list(sig.parameters.keys())
    assert "flight_name" in params, "Missing parameter 'flight_name'"
    assert "source" in params, "Missing parameter 'source'"
    assert "time" in params, "Missing parameter 'time'"
    assert "destination" in params, "Missing parameter 'destination'"
    assert "dateofjourney" in params, "Missing parameter 'dateofjourney'"
    assert "flight_No" in params, "Missing parameter 'flight_No'"

def test_ticket_has_flight_name():
    assert hasattr(Ticket, "flight_name")
    descriptor = None
    for klass in Ticket.__mro__:
        if "flight_name" in klass.__dict__:
            descriptor = klass.__dict__["flight_name"]
            break
    assert isinstance(descriptor, property)

def test_ticket_has_source():
    assert hasattr(Ticket, "source")
    descriptor = None
    for klass in Ticket.__mro__:
        if "source" in klass.__dict__:
            descriptor = klass.__dict__["source"]
            break
    assert isinstance(descriptor, property)

def test_ticket_has_time():
    assert hasattr(Ticket, "time")
    descriptor = None
    for klass in Ticket.__mro__:
        if "time" in klass.__dict__:
            descriptor = klass.__dict__["time"]
            break
    assert isinstance(descriptor, property)

def test_ticket_has_destination():
    assert hasattr(Ticket, "destination")
    descriptor = None
    for klass in Ticket.__mro__:
        if "destination" in klass.__dict__:
            descriptor = klass.__dict__["destination"]
            break
    assert isinstance(descriptor, property)

def test_ticket_has_dateofjourney():
    assert hasattr(Ticket, "dateofjourney")
    descriptor = None
    for klass in Ticket.__mro__:
        if "dateofjourney" in klass.__dict__:
            descriptor = klass.__dict__["dateofjourney"]
            break
    assert isinstance(descriptor, property)

def test_ticket_has_flight_No():
    assert hasattr(Ticket, "flight_No")
    descriptor = None
    for klass in Ticket.__mro__:
        if "flight_No" in klass.__dict__:
            descriptor = klass.__dict__["flight_No"]
            break
    assert isinstance(descriptor, property)



def test_booking_counter_is_not_abstract():
    assert not inspect.isabstract(Booking_counter)


def test_booking_counter_constructor_exists():
    assert callable(Booking_counter.__init__)


def test_booking_counter_constructor_args():
    sig = inspect.signature(Booking_counter.__init__)
    params = list(sig.parameters.keys())



def test_agent_is_not_abstract():
    assert not inspect.isabstract(Agent)


def test_agent_constructor_exists():
    assert callable(Agent.__init__)


def test_agent_constructor_args():
    sig = inspect.signature(Agent.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_agent_has_name():
    assert hasattr(Agent, "name")
    descriptor = None
    for klass in Agent.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_customer_is_not_abstract():
    assert not inspect.isabstract(Customer)


def test_customer_constructor_exists():
    assert callable(Customer.__init__)


def test_customer_constructor_args():
    sig = inspect.signature(Customer.__init__)
    params = list(sig.parameters.keys())
    assert "address" in params, "Missing parameter 'address'"
    assert "ph_no" in params, "Missing parameter 'ph_no'"
    assert "name" in params, "Missing parameter 'name'"

def test_customer_has_address():
    assert hasattr(Customer, "address")
    descriptor = None
    for klass in Customer.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_ph_no():
    assert hasattr(Customer, "ph_no")
    descriptor = None
    for klass in Customer.__mro__:
        if "ph_no" in klass.__dict__:
            descriptor = klass.__dict__["ph_no"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_name():
    assert hasattr(Customer, "name")
    descriptor = None
    for klass in Customer.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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
Common_fuctions_strategy = st.builds(
    Common_fuctions,
)
customer_Actor_strategy = st.builds(
    customer_Actor,
)
print_ticket_UseCase_strategy = st.builds(
    print_ticket_UseCase,
)
reserve_seats_UseCase_strategy = st.builds(
    reserve_seats_UseCase,
)
make_payment_UseCase_strategy = st.builds(
    make_payment_UseCase,
)
confirm_purchase_UseCase_strategy = st.builds(
    confirm_purchase_UseCase,
)
select_flight_UseCase_strategy = st.builds(
    select_flight_UseCase,
)
search_flights_UseCase_strategy = st.builds(
    search_flights_UseCase,
)
enter_no__of_tickets_UseCase_strategy = st.builds(
    enter_no__of_tickets_UseCase,
)
enter_date_UseCase_strategy = st.builds(
    enter_date_UseCase,
)
enter_airport_UseCase1_strategy = st.builds(
    enter_airport_UseCase1,
)
round_trip_or_one_way__UseCase_strategy = st.builds(
    round_trip_or_one_way__UseCase,
)
Reservation_System_Actor1_strategy = st.builds(
    Reservation_System_Actor1,
)
UseCase_UseCase_strategy = st.builds(
    UseCase_UseCase,
)
enter_airport_UseCase_strategy = st.builds(
    enter_airport_UseCase,
)
round_trip_or_one_way_UseCase_strategy = st.builds(
    round_trip_or_one_way_UseCase,
)
Reservation_System_Actor_strategy = st.builds(
    Reservation_System_Actor,
)
Ticket_strategy = st.builds(
    Ticket,
    flight_name=
        safe_text,
    source=
        safe_text,
    time=
        st.integers(),
    destination=
        safe_text,
    dateofjourney=
        st.dates(),
    flight_No=
        safe_text
)
Booking_counter_strategy = st.builds(
    Booking_counter,
)
Agent_strategy = st.builds(
    Agent,
    name=
        safe_text
)
Customer_strategy = st.builds(
    Customer,
    address=
        safe_text,
    ph_no=
        st.integers(),
    name=
        safe_text
)

@given(instance=Common_fuctions_strategy)
@settings(max_examples=50)
def test_common_fuctions_instantiation(instance):
    assert isinstance(instance, Common_fuctions)

@given(instance=customer_Actor_strategy)
@settings(max_examples=50)
def test_customer_actor_instantiation(instance):
    assert isinstance(instance, customer_Actor)

@given(instance=print_ticket_UseCase_strategy)
@settings(max_examples=50)
def test_print_ticket_usecase_instantiation(instance):
    assert isinstance(instance, print_ticket_UseCase)

@given(instance=reserve_seats_UseCase_strategy)
@settings(max_examples=50)
def test_reserve_seats_usecase_instantiation(instance):
    assert isinstance(instance, reserve_seats_UseCase)

@given(instance=make_payment_UseCase_strategy)
@settings(max_examples=50)
def test_make_payment_usecase_instantiation(instance):
    assert isinstance(instance, make_payment_UseCase)

@given(instance=confirm_purchase_UseCase_strategy)
@settings(max_examples=50)
def test_confirm_purchase_usecase_instantiation(instance):
    assert isinstance(instance, confirm_purchase_UseCase)

@given(instance=select_flight_UseCase_strategy)
@settings(max_examples=50)
def test_select_flight_usecase_instantiation(instance):
    assert isinstance(instance, select_flight_UseCase)

@given(instance=search_flights_UseCase_strategy)
@settings(max_examples=50)
def test_search_flights_usecase_instantiation(instance):
    assert isinstance(instance, search_flights_UseCase)

@given(instance=enter_no__of_tickets_UseCase_strategy)
@settings(max_examples=50)
def test_enter_no__of_tickets_usecase_instantiation(instance):
    assert isinstance(instance, enter_no__of_tickets_UseCase)

@given(instance=enter_date_UseCase_strategy)
@settings(max_examples=50)
def test_enter_date_usecase_instantiation(instance):
    assert isinstance(instance, enter_date_UseCase)

@given(instance=enter_airport_UseCase1_strategy)
@settings(max_examples=50)
def test_enter_airport_usecase1_instantiation(instance):
    assert isinstance(instance, enter_airport_UseCase1)

@given(instance=round_trip_or_one_way__UseCase_strategy)
@settings(max_examples=50)
def test_round_trip_or_one_way__usecase_instantiation(instance):
    assert isinstance(instance, round_trip_or_one_way__UseCase)

@given(instance=Reservation_System_Actor1_strategy)
@settings(max_examples=50)
def test_reservation_system_actor1_instantiation(instance):
    assert isinstance(instance, Reservation_System_Actor1)

@given(instance=UseCase_UseCase_strategy)
@settings(max_examples=50)
def test_usecase_usecase_instantiation(instance):
    assert isinstance(instance, UseCase_UseCase)

@given(instance=enter_airport_UseCase_strategy)
@settings(max_examples=50)
def test_enter_airport_usecase_instantiation(instance):
    assert isinstance(instance, enter_airport_UseCase)

@given(instance=round_trip_or_one_way_UseCase_strategy)
@settings(max_examples=50)
def test_round_trip_or_one_way_usecase_instantiation(instance):
    assert isinstance(instance, round_trip_or_one_way_UseCase)

@given(instance=Reservation_System_Actor_strategy)
@settings(max_examples=50)
def test_reservation_system_actor_instantiation(instance):
    assert isinstance(instance, Reservation_System_Actor)

@given(instance=Ticket_strategy)
@settings(max_examples=50)
def test_ticket_instantiation(instance):
    assert isinstance(instance, Ticket)



@given(instance=Ticket_strategy)
def test_ticket_flight_name_setter(instance):
    original = instance.flight_name
    instance.flight_name = original
    assert instance.flight_name == original



@given(instance=Ticket_strategy)
def test_ticket_source_setter(instance):
    original = instance.source
    instance.source = original
    assert instance.source == original



@given(instance=Ticket_strategy)
def test_ticket_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original



@given(instance=Ticket_strategy)
def test_ticket_destination_setter(instance):
    original = instance.destination
    instance.destination = original
    assert instance.destination == original



@given(instance=Ticket_strategy)
def test_ticket_dateofjourney_setter(instance):
    original = instance.dateofjourney
    instance.dateofjourney = original
    assert instance.dateofjourney == original



@given(instance=Ticket_strategy)
def test_ticket_flight_No_setter(instance):
    original = instance.flight_No
    instance.flight_No = original
    assert instance.flight_No == original

@given(instance=Booking_counter_strategy)
@settings(max_examples=50)
def test_booking_counter_instantiation(instance):
    assert isinstance(instance, Booking_counter)

@given(instance=Agent_strategy)
@settings(max_examples=50)
def test_agent_instantiation(instance):
    assert isinstance(instance, Agent)



@given(instance=Agent_strategy)
def test_agent_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Customer_strategy)
@settings(max_examples=50)
def test_customer_instantiation(instance):
    assert isinstance(instance, Customer)



@given(instance=Customer_strategy)
def test_customer_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=Customer_strategy)
def test_customer_ph_no_setter(instance):
    original = instance.ph_no
    instance.ph_no = original
    assert instance.ph_no == original



@given(instance=Customer_strategy)
def test_customer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
