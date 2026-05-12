import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    First_Class,
    Business_Seats,
    Economy_Seats,
    Seats,
    Infant,
    Child,
    Adult,
    Offers,
    FFP_Members,
    Flight,
    Passengers,
    Qaboos_Airways,
    Contact_Center_Agent_Actor,
    Customer_Actor,
    Qaboos_Reservation_System_Manage_Booking_UseCase,
    Qaboos_Reservation_System_Choose_Seats_UseCase,
    Qaboos_Reservation_System_Update_Flight_Details_UseCase,
    Qaboos_Reservation_System_Join__Qaboos_FPP_Club_UseCase,
    Qaboos_Reservation_System_Check_In_Online_UseCase,
    Qaboos_Reservation_System_Cancel_booking_UseCase,
    Qaboos_Reservation_System_Make_Payment_UseCase,
    Qaboos_Reservation_System_Confirm_booking__UseCase,
    Qaboos_Reservation_System_Enter_Passengers_Details_UseCase,
    Qaboos_Reservation_System_Book_ticket__UseCase,
    Qaboos_Reservation_System_Check_Flights_Availability_UseCase,
    Qaboos_Reservation_System_Enter_flight_Details_UseCase,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_first_class_is_not_abstract():
    assert not inspect.isabstract(First_Class)


def test_first_class_constructor_exists():
    assert callable(First_Class.__init__)


def test_first_class_constructor_args():
    sig = inspect.signature(First_Class.__init__)
    params = list(sig.parameters.keys())
    assert "First_Seat_Price" in params, "Missing parameter 'First_Seat_Price'"
    assert "First_Seat_ID" in params, "Missing parameter 'First_Seat_ID'"

def test_first_class_has_First_Seat_Price():
    assert hasattr(First_Class, "First_Seat_Price")
    descriptor = None
    for klass in First_Class.__mro__:
        if "First_Seat_Price" in klass.__dict__:
            descriptor = klass.__dict__["First_Seat_Price"]
            break
    assert isinstance(descriptor, property)

def test_first_class_has_First_Seat_ID():
    assert hasattr(First_Class, "First_Seat_ID")
    descriptor = None
    for klass in First_Class.__mro__:
        if "First_Seat_ID" in klass.__dict__:
            descriptor = klass.__dict__["First_Seat_ID"]
            break
    assert isinstance(descriptor, property)



def test_business_seats_is_not_abstract():
    assert not inspect.isabstract(Business_Seats)


def test_business_seats_constructor_exists():
    assert callable(Business_Seats.__init__)


def test_business_seats_constructor_args():
    sig = inspect.signature(Business_Seats.__init__)
    params = list(sig.parameters.keys())
    assert "Buiss_Seat_ID" in params, "Missing parameter 'Buiss_Seat_ID'"
    assert "Buiss_Seat_Price" in params, "Missing parameter 'Buiss_Seat_Price'"

def test_business_seats_has_Buiss_Seat_ID():
    assert hasattr(Business_Seats, "Buiss_Seat_ID")
    descriptor = None
    for klass in Business_Seats.__mro__:
        if "Buiss_Seat_ID" in klass.__dict__:
            descriptor = klass.__dict__["Buiss_Seat_ID"]
            break
    assert isinstance(descriptor, property)

def test_business_seats_has_Buiss_Seat_Price():
    assert hasattr(Business_Seats, "Buiss_Seat_Price")
    descriptor = None
    for klass in Business_Seats.__mro__:
        if "Buiss_Seat_Price" in klass.__dict__:
            descriptor = klass.__dict__["Buiss_Seat_Price"]
            break
    assert isinstance(descriptor, property)



def test_economy_seats_is_not_abstract():
    assert not inspect.isabstract(Economy_Seats)


def test_economy_seats_constructor_exists():
    assert callable(Economy_Seats.__init__)


def test_economy_seats_constructor_args():
    sig = inspect.signature(Economy_Seats.__init__)
    params = list(sig.parameters.keys())
    assert "Eco_Seat_Price" in params, "Missing parameter 'Eco_Seat_Price'"
    assert "Eco_Seat_ID" in params, "Missing parameter 'Eco_Seat_ID'"

def test_economy_seats_has_Eco_Seat_Price():
    assert hasattr(Economy_Seats, "Eco_Seat_Price")
    descriptor = None
    for klass in Economy_Seats.__mro__:
        if "Eco_Seat_Price" in klass.__dict__:
            descriptor = klass.__dict__["Eco_Seat_Price"]
            break
    assert isinstance(descriptor, property)

def test_economy_seats_has_Eco_Seat_ID():
    assert hasattr(Economy_Seats, "Eco_Seat_ID")
    descriptor = None
    for klass in Economy_Seats.__mro__:
        if "Eco_Seat_ID" in klass.__dict__:
            descriptor = klass.__dict__["Eco_Seat_ID"]
            break
    assert isinstance(descriptor, property)



def test_seats_is_not_abstract():
    assert not inspect.isabstract(Seats)


def test_seats_constructor_exists():
    assert callable(Seats.__init__)


def test_seats_constructor_args():
    sig = inspect.signature(Seats.__init__)
    params = list(sig.parameters.keys())
    assert "Seat_ID" in params, "Missing parameter 'Seat_ID'"
    assert "Seat_Catoegry" in params, "Missing parameter 'Seat_Catoegry'"
    assert "Seat_NO" in params, "Missing parameter 'Seat_NO'"

def test_seats_has_Seat_ID():
    assert hasattr(Seats, "Seat_ID")
    descriptor = None
    for klass in Seats.__mro__:
        if "Seat_ID" in klass.__dict__:
            descriptor = klass.__dict__["Seat_ID"]
            break
    assert isinstance(descriptor, property)

def test_seats_has_Seat_Catoegry():
    assert hasattr(Seats, "Seat_Catoegry")
    descriptor = None
    for klass in Seats.__mro__:
        if "Seat_Catoegry" in klass.__dict__:
            descriptor = klass.__dict__["Seat_Catoegry"]
            break
    assert isinstance(descriptor, property)

def test_seats_has_Seat_NO():
    assert hasattr(Seats, "Seat_NO")
    descriptor = None
    for klass in Seats.__mro__:
        if "Seat_NO" in klass.__dict__:
            descriptor = klass.__dict__["Seat_NO"]
            break
    assert isinstance(descriptor, property)



def test_infant_is_not_abstract():
    assert not inspect.isabstract(Infant)


def test_infant_constructor_exists():
    assert callable(Infant.__init__)


def test_infant_constructor_args():
    sig = inspect.signature(Infant.__init__)
    params = list(sig.parameters.keys())
    assert "Infant_Seat_Price" in params, "Missing parameter 'Infant_Seat_Price'"
    assert "Infant_No" in params, "Missing parameter 'Infant_No'"

def test_infant_has_Infant_Seat_Price():
    assert hasattr(Infant, "Infant_Seat_Price")
    descriptor = None
    for klass in Infant.__mro__:
        if "Infant_Seat_Price" in klass.__dict__:
            descriptor = klass.__dict__["Infant_Seat_Price"]
            break
    assert isinstance(descriptor, property)

def test_infant_has_Infant_No():
    assert hasattr(Infant, "Infant_No")
    descriptor = None
    for klass in Infant.__mro__:
        if "Infant_No" in klass.__dict__:
            descriptor = klass.__dict__["Infant_No"]
            break
    assert isinstance(descriptor, property)



def test_child_is_not_abstract():
    assert not inspect.isabstract(Child)


def test_child_constructor_exists():
    assert callable(Child.__init__)


def test_child_constructor_args():
    sig = inspect.signature(Child.__init__)
    params = list(sig.parameters.keys())
    assert "Child_Seat_Price" in params, "Missing parameter 'Child_Seat_Price'"
    assert "Child_ID" in params, "Missing parameter 'Child_ID'"

def test_child_has_Child_Seat_Price():
    assert hasattr(Child, "Child_Seat_Price")
    descriptor = None
    for klass in Child.__mro__:
        if "Child_Seat_Price" in klass.__dict__:
            descriptor = klass.__dict__["Child_Seat_Price"]
            break
    assert isinstance(descriptor, property)

def test_child_has_Child_ID():
    assert hasattr(Child, "Child_ID")
    descriptor = None
    for klass in Child.__mro__:
        if "Child_ID" in klass.__dict__:
            descriptor = klass.__dict__["Child_ID"]
            break
    assert isinstance(descriptor, property)



def test_adult_is_not_abstract():
    assert not inspect.isabstract(Adult)


def test_adult_constructor_exists():
    assert callable(Adult.__init__)


def test_adult_constructor_args():
    sig = inspect.signature(Adult.__init__)
    params = list(sig.parameters.keys())
    assert "Adult_ID" in params, "Missing parameter 'Adult_ID'"
    assert "Adult_Seat_Price" in params, "Missing parameter 'Adult_Seat_Price'"

def test_adult_has_Adult_ID():
    assert hasattr(Adult, "Adult_ID")
    descriptor = None
    for klass in Adult.__mro__:
        if "Adult_ID" in klass.__dict__:
            descriptor = klass.__dict__["Adult_ID"]
            break
    assert isinstance(descriptor, property)

def test_adult_has_Adult_Seat_Price():
    assert hasattr(Adult, "Adult_Seat_Price")
    descriptor = None
    for klass in Adult.__mro__:
        if "Adult_Seat_Price" in klass.__dict__:
            descriptor = klass.__dict__["Adult_Seat_Price"]
            break
    assert isinstance(descriptor, property)



def test_offers_is_not_abstract():
    assert not inspect.isabstract(Offers)


def test_offers_constructor_exists():
    assert callable(Offers.__init__)


def test_offers_constructor_args():
    sig = inspect.signature(Offers.__init__)
    params = list(sig.parameters.keys())
    assert "Offer_Expiry_Date" in params, "Missing parameter 'Offer_Expiry_Date'"
    assert "Offer_Det" in params, "Missing parameter 'Offer_Det'"
    assert "Offer_NO" in params, "Missing parameter 'Offer_NO'"

def test_offers_has_Offer_Expiry_Date():
    assert hasattr(Offers, "Offer_Expiry_Date")
    descriptor = None
    for klass in Offers.__mro__:
        if "Offer_Expiry_Date" in klass.__dict__:
            descriptor = klass.__dict__["Offer_Expiry_Date"]
            break
    assert isinstance(descriptor, property)

def test_offers_has_Offer_Det():
    assert hasattr(Offers, "Offer_Det")
    descriptor = None
    for klass in Offers.__mro__:
        if "Offer_Det" in klass.__dict__:
            descriptor = klass.__dict__["Offer_Det"]
            break
    assert isinstance(descriptor, property)

def test_offers_has_Offer_NO():
    assert hasattr(Offers, "Offer_NO")
    descriptor = None
    for klass in Offers.__mro__:
        if "Offer_NO" in klass.__dict__:
            descriptor = klass.__dict__["Offer_NO"]
            break
    assert isinstance(descriptor, property)



def test_ffp_members_is_not_abstract():
    assert not inspect.isabstract(FFP_Members)


def test_ffp_members_constructor_exists():
    assert callable(FFP_Members.__init__)


def test_ffp_members_constructor_args():
    sig = inspect.signature(FFP_Members.__init__)
    params = list(sig.parameters.keys())
    assert "FFP_Category" in params, "Missing parameter 'FFP_Category'"
    assert "FFP_Qmiles" in params, "Missing parameter 'FFP_Qmiles'"
    assert "FFP_ID" in params, "Missing parameter 'FFP_ID'"

def test_ffp_members_has_FFP_Category():
    assert hasattr(FFP_Members, "FFP_Category")
    descriptor = None
    for klass in FFP_Members.__mro__:
        if "FFP_Category" in klass.__dict__:
            descriptor = klass.__dict__["FFP_Category"]
            break
    assert isinstance(descriptor, property)

def test_ffp_members_has_FFP_Qmiles():
    assert hasattr(FFP_Members, "FFP_Qmiles")
    descriptor = None
    for klass in FFP_Members.__mro__:
        if "FFP_Qmiles" in klass.__dict__:
            descriptor = klass.__dict__["FFP_Qmiles"]
            break
    assert isinstance(descriptor, property)

def test_ffp_members_has_FFP_ID():
    assert hasattr(FFP_Members, "FFP_ID")
    descriptor = None
    for klass in FFP_Members.__mro__:
        if "FFP_ID" in klass.__dict__:
            descriptor = klass.__dict__["FFP_ID"]
            break
    assert isinstance(descriptor, property)



def test_flight_is_not_abstract():
    assert not inspect.isabstract(Flight)


def test_flight_constructor_exists():
    assert callable(Flight.__init__)


def test_flight_constructor_args():
    sig = inspect.signature(Flight.__init__)
    params = list(sig.parameters.keys())
    assert "Flgt_NO" in params, "Missing parameter 'Flgt_NO'"
    assert "Flgt_Details" in params, "Missing parameter 'Flgt_Details'"

def test_flight_has_Flgt_NO():
    assert hasattr(Flight, "Flgt_NO")
    descriptor = None
    for klass in Flight.__mro__:
        if "Flgt_NO" in klass.__dict__:
            descriptor = klass.__dict__["Flgt_NO"]
            break
    assert isinstance(descriptor, property)

def test_flight_has_Flgt_Details():
    assert hasattr(Flight, "Flgt_Details")
    descriptor = None
    for klass in Flight.__mro__:
        if "Flgt_Details" in klass.__dict__:
            descriptor = klass.__dict__["Flgt_Details"]
            break
    assert isinstance(descriptor, property)



def test_passengers_is_not_abstract():
    assert not inspect.isabstract(Passengers)


def test_passengers_constructor_exists():
    assert callable(Passengers.__init__)


def test_passengers_constructor_args():
    sig = inspect.signature(Passengers.__init__)
    params = list(sig.parameters.keys())
    assert "Passenger_Details" in params, "Missing parameter 'Passenger_Details'"
    assert "passenger_name" in params, "Missing parameter 'passenger_name'"
    assert "Passenger_TKT_No" in params, "Missing parameter 'Passenger_TKT_No'"

def test_passengers_has_Passenger_Details():
    assert hasattr(Passengers, "Passenger_Details")
    descriptor = None
    for klass in Passengers.__mro__:
        if "Passenger_Details" in klass.__dict__:
            descriptor = klass.__dict__["Passenger_Details"]
            break
    assert isinstance(descriptor, property)

def test_passengers_has_passenger_name():
    assert hasattr(Passengers, "passenger_name")
    descriptor = None
    for klass in Passengers.__mro__:
        if "passenger_name" in klass.__dict__:
            descriptor = klass.__dict__["passenger_name"]
            break
    assert isinstance(descriptor, property)

def test_passengers_has_Passenger_TKT_No():
    assert hasattr(Passengers, "Passenger_TKT_No")
    descriptor = None
    for klass in Passengers.__mro__:
        if "Passenger_TKT_No" in klass.__dict__:
            descriptor = klass.__dict__["Passenger_TKT_No"]
            break
    assert isinstance(descriptor, property)



def test_qaboos_airways_is_not_abstract():
    assert not inspect.isabstract(Qaboos_Airways)


def test_qaboos_airways_constructor_exists():
    assert callable(Qaboos_Airways.__init__)


def test_qaboos_airways_constructor_args():
    sig = inspect.signature(Qaboos_Airways.__init__)
    params = list(sig.parameters.keys())
    assert "Comp_location" in params, "Missing parameter 'Comp_location'"
    assert "Comp_Commercial_NO" in params, "Missing parameter 'Comp_Commercial_NO'"

def test_qaboos_airways_has_Comp_location():
    assert hasattr(Qaboos_Airways, "Comp_location")
    descriptor = None
    for klass in Qaboos_Airways.__mro__:
        if "Comp_location" in klass.__dict__:
            descriptor = klass.__dict__["Comp_location"]
            break
    assert isinstance(descriptor, property)

def test_qaboos_airways_has_Comp_Commercial_NO():
    assert hasattr(Qaboos_Airways, "Comp_Commercial_NO")
    descriptor = None
    for klass in Qaboos_Airways.__mro__:
        if "Comp_Commercial_NO" in klass.__dict__:
            descriptor = klass.__dict__["Comp_Commercial_NO"]
            break
    assert isinstance(descriptor, property)



def test_contact_center_agent_actor_is_not_abstract():
    assert not inspect.isabstract(Contact_Center_Agent_Actor)


def test_contact_center_agent_actor_constructor_exists():
    assert callable(Contact_Center_Agent_Actor.__init__)


def test_contact_center_agent_actor_constructor_args():
    sig = inspect.signature(Contact_Center_Agent_Actor.__init__)
    params = list(sig.parameters.keys())



def test_customer_actor_is_not_abstract():
    assert not inspect.isabstract(Customer_Actor)


def test_customer_actor_constructor_exists():
    assert callable(Customer_Actor.__init__)


def test_customer_actor_constructor_args():
    sig = inspect.signature(Customer_Actor.__init__)
    params = list(sig.parameters.keys())



def test_qaboos_reservation_system_manage_booking_usecase_is_not_abstract():
    assert not inspect.isabstract(Qaboos_Reservation_System_Manage_Booking_UseCase)


def test_qaboos_reservation_system_manage_booking_usecase_constructor_exists():
    assert callable(Qaboos_Reservation_System_Manage_Booking_UseCase.__init__)


def test_qaboos_reservation_system_manage_booking_usecase_constructor_args():
    sig = inspect.signature(Qaboos_Reservation_System_Manage_Booking_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_qaboos_reservation_system_choose_seats_usecase_is_not_abstract():
    assert not inspect.isabstract(Qaboos_Reservation_System_Choose_Seats_UseCase)


def test_qaboos_reservation_system_choose_seats_usecase_constructor_exists():
    assert callable(Qaboos_Reservation_System_Choose_Seats_UseCase.__init__)


def test_qaboos_reservation_system_choose_seats_usecase_constructor_args():
    sig = inspect.signature(Qaboos_Reservation_System_Choose_Seats_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_qaboos_reservation_system_update_flight_details_usecase_is_not_abstract():
    assert not inspect.isabstract(Qaboos_Reservation_System_Update_Flight_Details_UseCase)


def test_qaboos_reservation_system_update_flight_details_usecase_constructor_exists():
    assert callable(Qaboos_Reservation_System_Update_Flight_Details_UseCase.__init__)


def test_qaboos_reservation_system_update_flight_details_usecase_constructor_args():
    sig = inspect.signature(Qaboos_Reservation_System_Update_Flight_Details_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_qaboos_reservation_system_join__qaboos_fpp_club_usecase_is_not_abstract():
    assert not inspect.isabstract(Qaboos_Reservation_System_Join__Qaboos_FPP_Club_UseCase)


def test_qaboos_reservation_system_join__qaboos_fpp_club_usecase_constructor_exists():
    assert callable(Qaboos_Reservation_System_Join__Qaboos_FPP_Club_UseCase.__init__)


def test_qaboos_reservation_system_join__qaboos_fpp_club_usecase_constructor_args():
    sig = inspect.signature(Qaboos_Reservation_System_Join__Qaboos_FPP_Club_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_qaboos_reservation_system_check_in_online_usecase_is_not_abstract():
    assert not inspect.isabstract(Qaboos_Reservation_System_Check_In_Online_UseCase)


def test_qaboos_reservation_system_check_in_online_usecase_constructor_exists():
    assert callable(Qaboos_Reservation_System_Check_In_Online_UseCase.__init__)


def test_qaboos_reservation_system_check_in_online_usecase_constructor_args():
    sig = inspect.signature(Qaboos_Reservation_System_Check_In_Online_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_qaboos_reservation_system_cancel_booking_usecase_is_not_abstract():
    assert not inspect.isabstract(Qaboos_Reservation_System_Cancel_booking_UseCase)


def test_qaboos_reservation_system_cancel_booking_usecase_constructor_exists():
    assert callable(Qaboos_Reservation_System_Cancel_booking_UseCase.__init__)


def test_qaboos_reservation_system_cancel_booking_usecase_constructor_args():
    sig = inspect.signature(Qaboos_Reservation_System_Cancel_booking_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_qaboos_reservation_system_make_payment_usecase_is_not_abstract():
    assert not inspect.isabstract(Qaboos_Reservation_System_Make_Payment_UseCase)


def test_qaboos_reservation_system_make_payment_usecase_constructor_exists():
    assert callable(Qaboos_Reservation_System_Make_Payment_UseCase.__init__)


def test_qaboos_reservation_system_make_payment_usecase_constructor_args():
    sig = inspect.signature(Qaboos_Reservation_System_Make_Payment_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_qaboos_reservation_system_confirm_booking__usecase_is_not_abstract():
    assert not inspect.isabstract(Qaboos_Reservation_System_Confirm_booking__UseCase)


def test_qaboos_reservation_system_confirm_booking__usecase_constructor_exists():
    assert callable(Qaboos_Reservation_System_Confirm_booking__UseCase.__init__)


def test_qaboos_reservation_system_confirm_booking__usecase_constructor_args():
    sig = inspect.signature(Qaboos_Reservation_System_Confirm_booking__UseCase.__init__)
    params = list(sig.parameters.keys())



def test_qaboos_reservation_system_enter_passengers_details_usecase_is_not_abstract():
    assert not inspect.isabstract(Qaboos_Reservation_System_Enter_Passengers_Details_UseCase)


def test_qaboos_reservation_system_enter_passengers_details_usecase_constructor_exists():
    assert callable(Qaboos_Reservation_System_Enter_Passengers_Details_UseCase.__init__)


def test_qaboos_reservation_system_enter_passengers_details_usecase_constructor_args():
    sig = inspect.signature(Qaboos_Reservation_System_Enter_Passengers_Details_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_qaboos_reservation_system_book_ticket__usecase_is_not_abstract():
    assert not inspect.isabstract(Qaboos_Reservation_System_Book_ticket__UseCase)


def test_qaboos_reservation_system_book_ticket__usecase_constructor_exists():
    assert callable(Qaboos_Reservation_System_Book_ticket__UseCase.__init__)


def test_qaboos_reservation_system_book_ticket__usecase_constructor_args():
    sig = inspect.signature(Qaboos_Reservation_System_Book_ticket__UseCase.__init__)
    params = list(sig.parameters.keys())



def test_qaboos_reservation_system_check_flights_availability_usecase_is_not_abstract():
    assert not inspect.isabstract(Qaboos_Reservation_System_Check_Flights_Availability_UseCase)


def test_qaboos_reservation_system_check_flights_availability_usecase_constructor_exists():
    assert callable(Qaboos_Reservation_System_Check_Flights_Availability_UseCase.__init__)


def test_qaboos_reservation_system_check_flights_availability_usecase_constructor_args():
    sig = inspect.signature(Qaboos_Reservation_System_Check_Flights_Availability_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_qaboos_reservation_system_enter_flight_details_usecase_is_not_abstract():
    assert not inspect.isabstract(Qaboos_Reservation_System_Enter_flight_Details_UseCase)


def test_qaboos_reservation_system_enter_flight_details_usecase_constructor_exists():
    assert callable(Qaboos_Reservation_System_Enter_flight_Details_UseCase.__init__)


def test_qaboos_reservation_system_enter_flight_details_usecase_constructor_args():
    sig = inspect.signature(Qaboos_Reservation_System_Enter_flight_Details_UseCase.__init__)
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
First_Class_strategy = st.builds(
    First_Class,
    First_Seat_Price=
        safe_text,
    First_Seat_ID=
        safe_text
)
Business_Seats_strategy = st.builds(
    Business_Seats,
    Buiss_Seat_ID=
        safe_text,
    Buiss_Seat_Price=
        safe_text
)
Economy_Seats_strategy = st.builds(
    Economy_Seats,
    Eco_Seat_Price=
        safe_text,
    Eco_Seat_ID=
        safe_text
)
Seats_strategy = st.builds(
    Seats,
    Seat_ID=
        safe_text,
    Seat_Catoegry=
        safe_text,
    Seat_NO=
        safe_text
)
Infant_strategy = st.builds(
    Infant,
    Infant_Seat_Price=
        safe_text,
    Infant_No=
        safe_text
)
Child_strategy = st.builds(
    Child,
    Child_Seat_Price=
        safe_text,
    Child_ID=
        safe_text
)
Adult_strategy = st.builds(
    Adult,
    Adult_ID=
        safe_text,
    Adult_Seat_Price=
        safe_text
)
Offers_strategy = st.builds(
    Offers,
    Offer_Expiry_Date=
        safe_text,
    Offer_Det=
        safe_text,
    Offer_NO=
        safe_text
)
FFP_Members_strategy = st.builds(
    FFP_Members,
    FFP_Category=
        safe_text,
    FFP_Qmiles=
        safe_text,
    FFP_ID=
        safe_text
)
Flight_strategy = st.builds(
    Flight,
    Flgt_NO=
        safe_text,
    Flgt_Details=
        safe_text
)
Passengers_strategy = st.builds(
    Passengers,
    Passenger_Details=
        safe_text,
    passenger_name=
        safe_text,
    Passenger_TKT_No=
        safe_text
)
Qaboos_Airways_strategy = st.builds(
    Qaboos_Airways,
    Comp_location=
        safe_text,
    Comp_Commercial_NO=
        safe_text
)
Contact_Center_Agent_Actor_strategy = st.builds(
    Contact_Center_Agent_Actor,
)
Customer_Actor_strategy = st.builds(
    Customer_Actor,
)
Qaboos_Reservation_System_Manage_Booking_UseCase_strategy = st.builds(
    Qaboos_Reservation_System_Manage_Booking_UseCase,
)
Qaboos_Reservation_System_Choose_Seats_UseCase_strategy = st.builds(
    Qaboos_Reservation_System_Choose_Seats_UseCase,
)
Qaboos_Reservation_System_Update_Flight_Details_UseCase_strategy = st.builds(
    Qaboos_Reservation_System_Update_Flight_Details_UseCase,
)
Qaboos_Reservation_System_Join__Qaboos_FPP_Club_UseCase_strategy = st.builds(
    Qaboos_Reservation_System_Join__Qaboos_FPP_Club_UseCase,
)
Qaboos_Reservation_System_Check_In_Online_UseCase_strategy = st.builds(
    Qaboos_Reservation_System_Check_In_Online_UseCase,
)
Qaboos_Reservation_System_Cancel_booking_UseCase_strategy = st.builds(
    Qaboos_Reservation_System_Cancel_booking_UseCase,
)
Qaboos_Reservation_System_Make_Payment_UseCase_strategy = st.builds(
    Qaboos_Reservation_System_Make_Payment_UseCase,
)
Qaboos_Reservation_System_Confirm_booking__UseCase_strategy = st.builds(
    Qaboos_Reservation_System_Confirm_booking__UseCase,
)
Qaboos_Reservation_System_Enter_Passengers_Details_UseCase_strategy = st.builds(
    Qaboos_Reservation_System_Enter_Passengers_Details_UseCase,
)
Qaboos_Reservation_System_Book_ticket__UseCase_strategy = st.builds(
    Qaboos_Reservation_System_Book_ticket__UseCase,
)
Qaboos_Reservation_System_Check_Flights_Availability_UseCase_strategy = st.builds(
    Qaboos_Reservation_System_Check_Flights_Availability_UseCase,
)
Qaboos_Reservation_System_Enter_flight_Details_UseCase_strategy = st.builds(
    Qaboos_Reservation_System_Enter_flight_Details_UseCase,
)

@given(instance=First_Class_strategy)
@settings(max_examples=50)
def test_first_class_instantiation(instance):
    assert isinstance(instance, First_Class)



@given(instance=First_Class_strategy)
def test_first_class_First_Seat_Price_setter(instance):
    original = instance.First_Seat_Price
    instance.First_Seat_Price = original
    assert instance.First_Seat_Price == original



@given(instance=First_Class_strategy)
def test_first_class_First_Seat_ID_setter(instance):
    original = instance.First_Seat_ID
    instance.First_Seat_ID = original
    assert instance.First_Seat_ID == original

@given(instance=Business_Seats_strategy)
@settings(max_examples=50)
def test_business_seats_instantiation(instance):
    assert isinstance(instance, Business_Seats)



@given(instance=Business_Seats_strategy)
def test_business_seats_Buiss_Seat_ID_setter(instance):
    original = instance.Buiss_Seat_ID
    instance.Buiss_Seat_ID = original
    assert instance.Buiss_Seat_ID == original



@given(instance=Business_Seats_strategy)
def test_business_seats_Buiss_Seat_Price_setter(instance):
    original = instance.Buiss_Seat_Price
    instance.Buiss_Seat_Price = original
    assert instance.Buiss_Seat_Price == original

@given(instance=Economy_Seats_strategy)
@settings(max_examples=50)
def test_economy_seats_instantiation(instance):
    assert isinstance(instance, Economy_Seats)



@given(instance=Economy_Seats_strategy)
def test_economy_seats_Eco_Seat_Price_setter(instance):
    original = instance.Eco_Seat_Price
    instance.Eco_Seat_Price = original
    assert instance.Eco_Seat_Price == original



@given(instance=Economy_Seats_strategy)
def test_economy_seats_Eco_Seat_ID_setter(instance):
    original = instance.Eco_Seat_ID
    instance.Eco_Seat_ID = original
    assert instance.Eco_Seat_ID == original

@given(instance=Seats_strategy)
@settings(max_examples=50)
def test_seats_instantiation(instance):
    assert isinstance(instance, Seats)



@given(instance=Seats_strategy)
def test_seats_Seat_ID_setter(instance):
    original = instance.Seat_ID
    instance.Seat_ID = original
    assert instance.Seat_ID == original



@given(instance=Seats_strategy)
def test_seats_Seat_Catoegry_setter(instance):
    original = instance.Seat_Catoegry
    instance.Seat_Catoegry = original
    assert instance.Seat_Catoegry == original



@given(instance=Seats_strategy)
def test_seats_Seat_NO_setter(instance):
    original = instance.Seat_NO
    instance.Seat_NO = original
    assert instance.Seat_NO == original

@given(instance=Infant_strategy)
@settings(max_examples=50)
def test_infant_instantiation(instance):
    assert isinstance(instance, Infant)



@given(instance=Infant_strategy)
def test_infant_Infant_Seat_Price_setter(instance):
    original = instance.Infant_Seat_Price
    instance.Infant_Seat_Price = original
    assert instance.Infant_Seat_Price == original



@given(instance=Infant_strategy)
def test_infant_Infant_No_setter(instance):
    original = instance.Infant_No
    instance.Infant_No = original
    assert instance.Infant_No == original

@given(instance=Child_strategy)
@settings(max_examples=50)
def test_child_instantiation(instance):
    assert isinstance(instance, Child)



@given(instance=Child_strategy)
def test_child_Child_Seat_Price_setter(instance):
    original = instance.Child_Seat_Price
    instance.Child_Seat_Price = original
    assert instance.Child_Seat_Price == original



@given(instance=Child_strategy)
def test_child_Child_ID_setter(instance):
    original = instance.Child_ID
    instance.Child_ID = original
    assert instance.Child_ID == original

@given(instance=Adult_strategy)
@settings(max_examples=50)
def test_adult_instantiation(instance):
    assert isinstance(instance, Adult)



@given(instance=Adult_strategy)
def test_adult_Adult_ID_setter(instance):
    original = instance.Adult_ID
    instance.Adult_ID = original
    assert instance.Adult_ID == original



@given(instance=Adult_strategy)
def test_adult_Adult_Seat_Price_setter(instance):
    original = instance.Adult_Seat_Price
    instance.Adult_Seat_Price = original
    assert instance.Adult_Seat_Price == original

@given(instance=Offers_strategy)
@settings(max_examples=50)
def test_offers_instantiation(instance):
    assert isinstance(instance, Offers)



@given(instance=Offers_strategy)
def test_offers_Offer_Expiry_Date_setter(instance):
    original = instance.Offer_Expiry_Date
    instance.Offer_Expiry_Date = original
    assert instance.Offer_Expiry_Date == original



@given(instance=Offers_strategy)
def test_offers_Offer_Det_setter(instance):
    original = instance.Offer_Det
    instance.Offer_Det = original
    assert instance.Offer_Det == original



@given(instance=Offers_strategy)
def test_offers_Offer_NO_setter(instance):
    original = instance.Offer_NO
    instance.Offer_NO = original
    assert instance.Offer_NO == original

@given(instance=FFP_Members_strategy)
@settings(max_examples=50)
def test_ffp_members_instantiation(instance):
    assert isinstance(instance, FFP_Members)



@given(instance=FFP_Members_strategy)
def test_ffp_members_FFP_Category_setter(instance):
    original = instance.FFP_Category
    instance.FFP_Category = original
    assert instance.FFP_Category == original



@given(instance=FFP_Members_strategy)
def test_ffp_members_FFP_Qmiles_setter(instance):
    original = instance.FFP_Qmiles
    instance.FFP_Qmiles = original
    assert instance.FFP_Qmiles == original



@given(instance=FFP_Members_strategy)
def test_ffp_members_FFP_ID_setter(instance):
    original = instance.FFP_ID
    instance.FFP_ID = original
    assert instance.FFP_ID == original

@given(instance=Flight_strategy)
@settings(max_examples=50)
def test_flight_instantiation(instance):
    assert isinstance(instance, Flight)



@given(instance=Flight_strategy)
def test_flight_Flgt_NO_setter(instance):
    original = instance.Flgt_NO
    instance.Flgt_NO = original
    assert instance.Flgt_NO == original



@given(instance=Flight_strategy)
def test_flight_Flgt_Details_setter(instance):
    original = instance.Flgt_Details
    instance.Flgt_Details = original
    assert instance.Flgt_Details == original

@given(instance=Passengers_strategy)
@settings(max_examples=50)
def test_passengers_instantiation(instance):
    assert isinstance(instance, Passengers)



@given(instance=Passengers_strategy)
def test_passengers_Passenger_Details_setter(instance):
    original = instance.Passenger_Details
    instance.Passenger_Details = original
    assert instance.Passenger_Details == original



@given(instance=Passengers_strategy)
def test_passengers_passenger_name_setter(instance):
    original = instance.passenger_name
    instance.passenger_name = original
    assert instance.passenger_name == original



@given(instance=Passengers_strategy)
def test_passengers_Passenger_TKT_No_setter(instance):
    original = instance.Passenger_TKT_No
    instance.Passenger_TKT_No = original
    assert instance.Passenger_TKT_No == original

@given(instance=Qaboos_Airways_strategy)
@settings(max_examples=50)
def test_qaboos_airways_instantiation(instance):
    assert isinstance(instance, Qaboos_Airways)



@given(instance=Qaboos_Airways_strategy)
def test_qaboos_airways_Comp_location_setter(instance):
    original = instance.Comp_location
    instance.Comp_location = original
    assert instance.Comp_location == original



@given(instance=Qaboos_Airways_strategy)
def test_qaboos_airways_Comp_Commercial_NO_setter(instance):
    original = instance.Comp_Commercial_NO
    instance.Comp_Commercial_NO = original
    assert instance.Comp_Commercial_NO == original

@given(instance=Contact_Center_Agent_Actor_strategy)
@settings(max_examples=50)
def test_contact_center_agent_actor_instantiation(instance):
    assert isinstance(instance, Contact_Center_Agent_Actor)

@given(instance=Customer_Actor_strategy)
@settings(max_examples=50)
def test_customer_actor_instantiation(instance):
    assert isinstance(instance, Customer_Actor)

@given(instance=Qaboos_Reservation_System_Manage_Booking_UseCase_strategy)
@settings(max_examples=50)
def test_qaboos_reservation_system_manage_booking_usecase_instantiation(instance):
    assert isinstance(instance, Qaboos_Reservation_System_Manage_Booking_UseCase)

@given(instance=Qaboos_Reservation_System_Choose_Seats_UseCase_strategy)
@settings(max_examples=50)
def test_qaboos_reservation_system_choose_seats_usecase_instantiation(instance):
    assert isinstance(instance, Qaboos_Reservation_System_Choose_Seats_UseCase)

@given(instance=Qaboos_Reservation_System_Update_Flight_Details_UseCase_strategy)
@settings(max_examples=50)
def test_qaboos_reservation_system_update_flight_details_usecase_instantiation(instance):
    assert isinstance(instance, Qaboos_Reservation_System_Update_Flight_Details_UseCase)

@given(instance=Qaboos_Reservation_System_Join__Qaboos_FPP_Club_UseCase_strategy)
@settings(max_examples=50)
def test_qaboos_reservation_system_join__qaboos_fpp_club_usecase_instantiation(instance):
    assert isinstance(instance, Qaboos_Reservation_System_Join__Qaboos_FPP_Club_UseCase)

@given(instance=Qaboos_Reservation_System_Check_In_Online_UseCase_strategy)
@settings(max_examples=50)
def test_qaboos_reservation_system_check_in_online_usecase_instantiation(instance):
    assert isinstance(instance, Qaboos_Reservation_System_Check_In_Online_UseCase)

@given(instance=Qaboos_Reservation_System_Cancel_booking_UseCase_strategy)
@settings(max_examples=50)
def test_qaboos_reservation_system_cancel_booking_usecase_instantiation(instance):
    assert isinstance(instance, Qaboos_Reservation_System_Cancel_booking_UseCase)

@given(instance=Qaboos_Reservation_System_Make_Payment_UseCase_strategy)
@settings(max_examples=50)
def test_qaboos_reservation_system_make_payment_usecase_instantiation(instance):
    assert isinstance(instance, Qaboos_Reservation_System_Make_Payment_UseCase)

@given(instance=Qaboos_Reservation_System_Confirm_booking__UseCase_strategy)
@settings(max_examples=50)
def test_qaboos_reservation_system_confirm_booking__usecase_instantiation(instance):
    assert isinstance(instance, Qaboos_Reservation_System_Confirm_booking__UseCase)

@given(instance=Qaboos_Reservation_System_Enter_Passengers_Details_UseCase_strategy)
@settings(max_examples=50)
def test_qaboos_reservation_system_enter_passengers_details_usecase_instantiation(instance):
    assert isinstance(instance, Qaboos_Reservation_System_Enter_Passengers_Details_UseCase)

@given(instance=Qaboos_Reservation_System_Book_ticket__UseCase_strategy)
@settings(max_examples=50)
def test_qaboos_reservation_system_book_ticket__usecase_instantiation(instance):
    assert isinstance(instance, Qaboos_Reservation_System_Book_ticket__UseCase)

@given(instance=Qaboos_Reservation_System_Check_Flights_Availability_UseCase_strategy)
@settings(max_examples=50)
def test_qaboos_reservation_system_check_flights_availability_usecase_instantiation(instance):
    assert isinstance(instance, Qaboos_Reservation_System_Check_Flights_Availability_UseCase)

@given(instance=Qaboos_Reservation_System_Enter_flight_Details_UseCase_strategy)
@settings(max_examples=50)
def test_qaboos_reservation_system_enter_flight_details_usecase_instantiation(instance):
    assert isinstance(instance, Qaboos_Reservation_System_Enter_flight_Details_UseCase)
