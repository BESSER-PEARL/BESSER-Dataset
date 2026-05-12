import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Booking,
    reservationsystem_City,
    reservationsystem_Plane,
    reservationsystem_Airport,
    reservationsystem_GeneralFlight,
    reservationsystem_Seat,
    reservationsystem_PaymentInfo,
    Crew,
    reservationsystem_Attendant,
    reservationsystem_Pilot,
    reservationsystem_Booking,
    reservationsystem_SpecificFlight,
    Person,
    reservationsystem_Passenger,
    reservationsystem_Crew,
    reservationsystem_User,
    reservationsystem_Person,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_booking_is_not_abstract():
    assert not inspect.isabstract(Booking)


def test_booking_constructor_exists():
    assert callable(Booking.__init__)


def test_booking_constructor_args():
    sig = inspect.signature(Booking.__init__)
    params = list(sig.parameters.keys())



def test_reservationsystem_city_is_not_abstract():
    assert not inspect.isabstract(reservationsystem_City)


def test_reservationsystem_city_constructor_exists():
    assert callable(reservationsystem_City.__init__)


def test_reservationsystem_city_constructor_args():
    sig = inspect.signature(reservationsystem_City.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "abbr" in params, "Missing parameter 'abbr'"
    assert "id" in params, "Missing parameter 'id'"

def test_reservationsystem_city_has_name():
    assert hasattr(reservationsystem_City, "name")
    descriptor = None
    for klass in reservationsystem_City.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_reservationsystem_city_has_abbr():
    assert hasattr(reservationsystem_City, "abbr")
    descriptor = None
    for klass in reservationsystem_City.__mro__:
        if "abbr" in klass.__dict__:
            descriptor = klass.__dict__["abbr"]
            break
    assert isinstance(descriptor, property)

def test_reservationsystem_city_has_id():
    assert hasattr(reservationsystem_City, "id")
    descriptor = None
    for klass in reservationsystem_City.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_reservationsystem_plane_is_not_abstract():
    assert not inspect.isabstract(reservationsystem_Plane)


def test_reservationsystem_plane_constructor_exists():
    assert callable(reservationsystem_Plane.__init__)


def test_reservationsystem_plane_constructor_args():
    sig = inspect.signature(reservationsystem_Plane.__init__)
    params = list(sig.parameters.keys())
    assert "model" in params, "Missing parameter 'model'"
    assert "crewNum" in params, "Missing parameter 'crewNum'"
    assert "id" in params, "Missing parameter 'id'"
    assert "capacity" in params, "Missing parameter 'capacity'"

def test_reservationsystem_plane_has_model():
    assert hasattr(reservationsystem_Plane, "model")
    descriptor = None
    for klass in reservationsystem_Plane.__mro__:
        if "model" in klass.__dict__:
            descriptor = klass.__dict__["model"]
            break
    assert isinstance(descriptor, property)

def test_reservationsystem_plane_has_crewNum():
    assert hasattr(reservationsystem_Plane, "crewNum")
    descriptor = None
    for klass in reservationsystem_Plane.__mro__:
        if "crewNum" in klass.__dict__:
            descriptor = klass.__dict__["crewNum"]
            break
    assert isinstance(descriptor, property)

def test_reservationsystem_plane_has_id():
    assert hasattr(reservationsystem_Plane, "id")
    descriptor = None
    for klass in reservationsystem_Plane.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_reservationsystem_plane_has_capacity():
    assert hasattr(reservationsystem_Plane, "capacity")
    descriptor = None
    for klass in reservationsystem_Plane.__mro__:
        if "capacity" in klass.__dict__:
            descriptor = klass.__dict__["capacity"]
            break
    assert isinstance(descriptor, property)



def test_reservationsystem_airport_is_not_abstract():
    assert not inspect.isabstract(reservationsystem_Airport)


def test_reservationsystem_airport_constructor_exists():
    assert callable(reservationsystem_Airport.__init__)


def test_reservationsystem_airport_constructor_args():
    sig = inspect.signature(reservationsystem_Airport.__init__)
    params = list(sig.parameters.keys())
    assert "abbr" in params, "Missing parameter 'abbr'"
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"

def test_reservationsystem_airport_has_abbr():
    assert hasattr(reservationsystem_Airport, "abbr")
    descriptor = None
    for klass in reservationsystem_Airport.__mro__:
        if "abbr" in klass.__dict__:
            descriptor = klass.__dict__["abbr"]
            break
    assert isinstance(descriptor, property)

def test_reservationsystem_airport_has_id():
    assert hasattr(reservationsystem_Airport, "id")
    descriptor = None
    for klass in reservationsystem_Airport.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_reservationsystem_airport_has_name():
    assert hasattr(reservationsystem_Airport, "name")
    descriptor = None
    for klass in reservationsystem_Airport.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_reservationsystem_generalflight_is_not_abstract():
    assert not inspect.isabstract(reservationsystem_GeneralFlight)


def test_reservationsystem_generalflight_constructor_exists():
    assert callable(reservationsystem_GeneralFlight.__init__)


def test_reservationsystem_generalflight_constructor_args():
    sig = inspect.signature(reservationsystem_GeneralFlight.__init__)
    params = list(sig.parameters.keys())
    assert "arrivalTime" in params, "Missing parameter 'arrivalTime'"
    assert "departureTime" in params, "Missing parameter 'departureTime'"
    assert "flightNo" in params, "Missing parameter 'flightNo'"

def test_reservationsystem_generalflight_has_arrivalTime():
    assert hasattr(reservationsystem_GeneralFlight, "arrivalTime")
    descriptor = None
    for klass in reservationsystem_GeneralFlight.__mro__:
        if "arrivalTime" in klass.__dict__:
            descriptor = klass.__dict__["arrivalTime"]
            break
    assert isinstance(descriptor, property)

def test_reservationsystem_generalflight_has_departureTime():
    assert hasattr(reservationsystem_GeneralFlight, "departureTime")
    descriptor = None
    for klass in reservationsystem_GeneralFlight.__mro__:
        if "departureTime" in klass.__dict__:
            descriptor = klass.__dict__["departureTime"]
            break
    assert isinstance(descriptor, property)

def test_reservationsystem_generalflight_has_flightNo():
    assert hasattr(reservationsystem_GeneralFlight, "flightNo")
    descriptor = None
    for klass in reservationsystem_GeneralFlight.__mro__:
        if "flightNo" in klass.__dict__:
            descriptor = klass.__dict__["flightNo"]
            break
    assert isinstance(descriptor, property)



def test_reservationsystem_seat_is_not_abstract():
    assert not inspect.isabstract(reservationsystem_Seat)


def test_reservationsystem_seat_constructor_exists():
    assert callable(reservationsystem_Seat.__init__)


def test_reservationsystem_seat_constructor_args():
    sig = inspect.signature(reservationsystem_Seat.__init__)
    params = list(sig.parameters.keys())
    assert "isExit" in params, "Missing parameter 'isExit'"
    assert "no" in params, "Missing parameter 'no'"
    assert "type" in params, "Missing parameter 'type'"

def test_reservationsystem_seat_has_isExit():
    assert hasattr(reservationsystem_Seat, "isExit")
    descriptor = None
    for klass in reservationsystem_Seat.__mro__:
        if "isExit" in klass.__dict__:
            descriptor = klass.__dict__["isExit"]
            break
    assert isinstance(descriptor, property)

def test_reservationsystem_seat_has_no():
    assert hasattr(reservationsystem_Seat, "no")
    descriptor = None
    for klass in reservationsystem_Seat.__mro__:
        if "no" in klass.__dict__:
            descriptor = klass.__dict__["no"]
            break
    assert isinstance(descriptor, property)

def test_reservationsystem_seat_has_type():
    assert hasattr(reservationsystem_Seat, "type")
    descriptor = None
    for klass in reservationsystem_Seat.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_reservationsystem_paymentinfo_is_not_abstract():
    assert not inspect.isabstract(reservationsystem_PaymentInfo)


def test_reservationsystem_paymentinfo_constructor_exists():
    assert callable(reservationsystem_PaymentInfo.__init__)


def test_reservationsystem_paymentinfo_constructor_args():
    sig = inspect.signature(reservationsystem_PaymentInfo.__init__)
    params = list(sig.parameters.keys())
    assert "cardNo" in params, "Missing parameter 'cardNo'"
    assert "id" in params, "Missing parameter 'id'"
    assert "type" in params, "Missing parameter 'type'"
    assert "createTime" in params, "Missing parameter 'createTime'"
    assert "payTime" in params, "Missing parameter 'payTime'"
    assert "cardOwner" in params, "Missing parameter 'cardOwner'"
    assert "status" in params, "Missing parameter 'status'"
    assert "cardAddr" in params, "Missing parameter 'cardAddr'"

def test_reservationsystem_paymentinfo_has_cardNo():
    assert hasattr(reservationsystem_PaymentInfo, "cardNo")
    descriptor = None
    for klass in reservationsystem_PaymentInfo.__mro__:
        if "cardNo" in klass.__dict__:
            descriptor = klass.__dict__["cardNo"]
            break
    assert isinstance(descriptor, property)

def test_reservationsystem_paymentinfo_has_id():
    assert hasattr(reservationsystem_PaymentInfo, "id")
    descriptor = None
    for klass in reservationsystem_PaymentInfo.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_reservationsystem_paymentinfo_has_type():
    assert hasattr(reservationsystem_PaymentInfo, "type")
    descriptor = None
    for klass in reservationsystem_PaymentInfo.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_reservationsystem_paymentinfo_has_createTime():
    assert hasattr(reservationsystem_PaymentInfo, "createTime")
    descriptor = None
    for klass in reservationsystem_PaymentInfo.__mro__:
        if "createTime" in klass.__dict__:
            descriptor = klass.__dict__["createTime"]
            break
    assert isinstance(descriptor, property)

def test_reservationsystem_paymentinfo_has_payTime():
    assert hasattr(reservationsystem_PaymentInfo, "payTime")
    descriptor = None
    for klass in reservationsystem_PaymentInfo.__mro__:
        if "payTime" in klass.__dict__:
            descriptor = klass.__dict__["payTime"]
            break
    assert isinstance(descriptor, property)

def test_reservationsystem_paymentinfo_has_cardOwner():
    assert hasattr(reservationsystem_PaymentInfo, "cardOwner")
    descriptor = None
    for klass in reservationsystem_PaymentInfo.__mro__:
        if "cardOwner" in klass.__dict__:
            descriptor = klass.__dict__["cardOwner"]
            break
    assert isinstance(descriptor, property)

def test_reservationsystem_paymentinfo_has_status():
    assert hasattr(reservationsystem_PaymentInfo, "status")
    descriptor = None
    for klass in reservationsystem_PaymentInfo.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)

def test_reservationsystem_paymentinfo_has_cardAddr():
    assert hasattr(reservationsystem_PaymentInfo, "cardAddr")
    descriptor = None
    for klass in reservationsystem_PaymentInfo.__mro__:
        if "cardAddr" in klass.__dict__:
            descriptor = klass.__dict__["cardAddr"]
            break
    assert isinstance(descriptor, property)



def test_crew_is_not_abstract():
    assert not inspect.isabstract(Crew)


def test_crew_constructor_exists():
    assert callable(Crew.__init__)


def test_crew_constructor_args():
    sig = inspect.signature(Crew.__init__)
    params = list(sig.parameters.keys())



def test_reservationsystem_attendant_is_not_abstract():
    assert not inspect.isabstract(reservationsystem_Attendant)


def test_reservationsystem_attendant_constructor_exists():
    assert callable(reservationsystem_Attendant.__init__)


def test_reservationsystem_attendant_constructor_args():
    sig = inspect.signature(reservationsystem_Attendant.__init__)
    params = list(sig.parameters.keys())



def test_reservationsystem_pilot_is_not_abstract():
    assert not inspect.isabstract(reservationsystem_Pilot)


def test_reservationsystem_pilot_constructor_exists():
    assert callable(reservationsystem_Pilot.__init__)


def test_reservationsystem_pilot_constructor_args():
    sig = inspect.signature(reservationsystem_Pilot.__init__)
    params = list(sig.parameters.keys())
    assert "experience" in params, "Missing parameter 'experience'"
    assert "certificationId" in params, "Missing parameter 'certificationId'"

def test_reservationsystem_pilot_has_experience():
    assert hasattr(reservationsystem_Pilot, "experience")
    descriptor = None
    for klass in reservationsystem_Pilot.__mro__:
        if "experience" in klass.__dict__:
            descriptor = klass.__dict__["experience"]
            break
    assert isinstance(descriptor, property)

def test_reservationsystem_pilot_has_certificationId():
    assert hasattr(reservationsystem_Pilot, "certificationId")
    descriptor = None
    for klass in reservationsystem_Pilot.__mro__:
        if "certificationId" in klass.__dict__:
            descriptor = klass.__dict__["certificationId"]
            break
    assert isinstance(descriptor, property)



def test_reservationsystem_booking_is_not_abstract():
    assert not inspect.isabstract(reservationsystem_Booking)


def test_reservationsystem_booking_constructor_exists():
    assert callable(reservationsystem_Booking.__init__)


def test_reservationsystem_booking_constructor_args():
    sig = inspect.signature(reservationsystem_Booking.__init__)
    params = list(sig.parameters.keys())
    assert "baggageInfo" in params, "Missing parameter 'baggageInfo'"
    assert "bookingStatus" in params, "Missing parameter 'bookingStatus'"
    assert "bookNo" in params, "Missing parameter 'bookNo'"

def test_reservationsystem_booking_has_baggageInfo():
    assert hasattr(reservationsystem_Booking, "baggageInfo")
    descriptor = None
    for klass in reservationsystem_Booking.__mro__:
        if "baggageInfo" in klass.__dict__:
            descriptor = klass.__dict__["baggageInfo"]
            break
    assert isinstance(descriptor, property)

def test_reservationsystem_booking_has_bookingStatus():
    assert hasattr(reservationsystem_Booking, "bookingStatus")
    descriptor = None
    for klass in reservationsystem_Booking.__mro__:
        if "bookingStatus" in klass.__dict__:
            descriptor = klass.__dict__["bookingStatus"]
            break
    assert isinstance(descriptor, property)

def test_reservationsystem_booking_has_bookNo():
    assert hasattr(reservationsystem_Booking, "bookNo")
    descriptor = None
    for klass in reservationsystem_Booking.__mro__:
        if "bookNo" in klass.__dict__:
            descriptor = klass.__dict__["bookNo"]
            break
    assert isinstance(descriptor, property)



def test_reservationsystem_specificflight_is_not_abstract():
    assert not inspect.isabstract(reservationsystem_SpecificFlight)


def test_reservationsystem_specificflight_constructor_exists():
    assert callable(reservationsystem_SpecificFlight.__init__)


def test_reservationsystem_specificflight_constructor_args():
    sig = inspect.signature(reservationsystem_SpecificFlight.__init__)
    params = list(sig.parameters.keys())
    assert "realArriTime" in params, "Missing parameter 'realArriTime'"
    assert "status" in params, "Missing parameter 'status'"
    assert "date" in params, "Missing parameter 'date'"
    assert "realDepTime" in params, "Missing parameter 'realDepTime'"
    assert "id" in params, "Missing parameter 'id'"

def test_reservationsystem_specificflight_has_realArriTime():
    assert hasattr(reservationsystem_SpecificFlight, "realArriTime")
    descriptor = None
    for klass in reservationsystem_SpecificFlight.__mro__:
        if "realArriTime" in klass.__dict__:
            descriptor = klass.__dict__["realArriTime"]
            break
    assert isinstance(descriptor, property)

def test_reservationsystem_specificflight_has_status():
    assert hasattr(reservationsystem_SpecificFlight, "status")
    descriptor = None
    for klass in reservationsystem_SpecificFlight.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)

def test_reservationsystem_specificflight_has_date():
    assert hasattr(reservationsystem_SpecificFlight, "date")
    descriptor = None
    for klass in reservationsystem_SpecificFlight.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)

def test_reservationsystem_specificflight_has_realDepTime():
    assert hasattr(reservationsystem_SpecificFlight, "realDepTime")
    descriptor = None
    for klass in reservationsystem_SpecificFlight.__mro__:
        if "realDepTime" in klass.__dict__:
            descriptor = klass.__dict__["realDepTime"]
            break
    assert isinstance(descriptor, property)

def test_reservationsystem_specificflight_has_id():
    assert hasattr(reservationsystem_SpecificFlight, "id")
    descriptor = None
    for klass in reservationsystem_SpecificFlight.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_person_is_not_abstract():
    assert not inspect.isabstract(Person)


def test_person_constructor_exists():
    assert callable(Person.__init__)


def test_person_constructor_args():
    sig = inspect.signature(Person.__init__)
    params = list(sig.parameters.keys())



def test_reservationsystem_passenger_is_not_abstract():
    assert not inspect.isabstract(reservationsystem_Passenger)


def test_reservationsystem_passenger_constructor_exists():
    assert callable(reservationsystem_Passenger.__init__)


def test_reservationsystem_passenger_constructor_args():
    sig = inspect.signature(reservationsystem_Passenger.__init__)
    params = list(sig.parameters.keys())
    assert "foodPref" in params, "Missing parameter 'foodPref'"
    assert "specialNeeds" in params, "Missing parameter 'specialNeeds'"

def test_reservationsystem_passenger_has_foodPref():
    assert hasattr(reservationsystem_Passenger, "foodPref")
    descriptor = None
    for klass in reservationsystem_Passenger.__mro__:
        if "foodPref" in klass.__dict__:
            descriptor = klass.__dict__["foodPref"]
            break
    assert isinstance(descriptor, property)

def test_reservationsystem_passenger_has_specialNeeds():
    assert hasattr(reservationsystem_Passenger, "specialNeeds")
    descriptor = None
    for klass in reservationsystem_Passenger.__mro__:
        if "specialNeeds" in klass.__dict__:
            descriptor = klass.__dict__["specialNeeds"]
            break
    assert isinstance(descriptor, property)



def test_reservationsystem_crew_is_not_abstract():
    assert not inspect.isabstract(reservationsystem_Crew)


def test_reservationsystem_crew_constructor_exists():
    assert callable(reservationsystem_Crew.__init__)


def test_reservationsystem_crew_constructor_args():
    sig = inspect.signature(reservationsystem_Crew.__init__)
    params = list(sig.parameters.keys())
    assert "employeeId" in params, "Missing parameter 'employeeId'"

def test_reservationsystem_crew_has_employeeId():
    assert hasattr(reservationsystem_Crew, "employeeId")
    descriptor = None
    for klass in reservationsystem_Crew.__mro__:
        if "employeeId" in klass.__dict__:
            descriptor = klass.__dict__["employeeId"]
            break
    assert isinstance(descriptor, property)



def test_reservationsystem_user_is_not_abstract():
    assert not inspect.isabstract(reservationsystem_User)


def test_reservationsystem_user_constructor_exists():
    assert callable(reservationsystem_User.__init__)


def test_reservationsystem_user_constructor_args():
    sig = inspect.signature(reservationsystem_User.__init__)
    params = list(sig.parameters.keys())
    assert "userType" in params, "Missing parameter 'userType'"
    assert "userName" in params, "Missing parameter 'userName'"
    assert "md5Pwd" in params, "Missing parameter 'md5Pwd'"

def test_reservationsystem_user_has_userType():
    assert hasattr(reservationsystem_User, "userType")
    descriptor = None
    for klass in reservationsystem_User.__mro__:
        if "userType" in klass.__dict__:
            descriptor = klass.__dict__["userType"]
            break
    assert isinstance(descriptor, property)

def test_reservationsystem_user_has_userName():
    assert hasattr(reservationsystem_User, "userName")
    descriptor = None
    for klass in reservationsystem_User.__mro__:
        if "userName" in klass.__dict__:
            descriptor = klass.__dict__["userName"]
            break
    assert isinstance(descriptor, property)

def test_reservationsystem_user_has_md5Pwd():
    assert hasattr(reservationsystem_User, "md5Pwd")
    descriptor = None
    for klass in reservationsystem_User.__mro__:
        if "md5Pwd" in klass.__dict__:
            descriptor = klass.__dict__["md5Pwd"]
            break
    assert isinstance(descriptor, property)



def test_reservationsystem_person_is_not_abstract():
    assert not inspect.isabstract(reservationsystem_Person)


def test_reservationsystem_person_constructor_exists():
    assert callable(reservationsystem_Person.__init__)


def test_reservationsystem_person_constructor_args():
    sig = inspect.signature(reservationsystem_Person.__init__)
    params = list(sig.parameters.keys())
    assert "citizenship" in params, "Missing parameter 'citizenship'"
    assert "birthDate" in params, "Missing parameter 'birthDate'"
    assert "email" in params, "Missing parameter 'email'"
    assert "middleName" in params, "Missing parameter 'middleName'"
    assert "phone" in params, "Missing parameter 'phone'"
    assert "passportId" in params, "Missing parameter 'passportId'"
    assert "id" in params, "Missing parameter 'id'"
    assert "residence" in params, "Missing parameter 'residence'"
    assert "name" in params, "Missing parameter 'name'"
    assert "addr" in params, "Missing parameter 'addr'"
    assert "FamilyName" in params, "Missing parameter 'FamilyName'"
    assert "gender" in params, "Missing parameter 'gender'"

def test_reservationsystem_person_has_citizenship():
    assert hasattr(reservationsystem_Person, "citizenship")
    descriptor = None
    for klass in reservationsystem_Person.__mro__:
        if "citizenship" in klass.__dict__:
            descriptor = klass.__dict__["citizenship"]
            break
    assert isinstance(descriptor, property)

def test_reservationsystem_person_has_birthDate():
    assert hasattr(reservationsystem_Person, "birthDate")
    descriptor = None
    for klass in reservationsystem_Person.__mro__:
        if "birthDate" in klass.__dict__:
            descriptor = klass.__dict__["birthDate"]
            break
    assert isinstance(descriptor, property)

def test_reservationsystem_person_has_email():
    assert hasattr(reservationsystem_Person, "email")
    descriptor = None
    for klass in reservationsystem_Person.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)

def test_reservationsystem_person_has_middleName():
    assert hasattr(reservationsystem_Person, "middleName")
    descriptor = None
    for klass in reservationsystem_Person.__mro__:
        if "middleName" in klass.__dict__:
            descriptor = klass.__dict__["middleName"]
            break
    assert isinstance(descriptor, property)

def test_reservationsystem_person_has_phone():
    assert hasattr(reservationsystem_Person, "phone")
    descriptor = None
    for klass in reservationsystem_Person.__mro__:
        if "phone" in klass.__dict__:
            descriptor = klass.__dict__["phone"]
            break
    assert isinstance(descriptor, property)

def test_reservationsystem_person_has_passportId():
    assert hasattr(reservationsystem_Person, "passportId")
    descriptor = None
    for klass in reservationsystem_Person.__mro__:
        if "passportId" in klass.__dict__:
            descriptor = klass.__dict__["passportId"]
            break
    assert isinstance(descriptor, property)

def test_reservationsystem_person_has_id():
    assert hasattr(reservationsystem_Person, "id")
    descriptor = None
    for klass in reservationsystem_Person.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_reservationsystem_person_has_residence():
    assert hasattr(reservationsystem_Person, "residence")
    descriptor = None
    for klass in reservationsystem_Person.__mro__:
        if "residence" in klass.__dict__:
            descriptor = klass.__dict__["residence"]
            break
    assert isinstance(descriptor, property)

def test_reservationsystem_person_has_name():
    assert hasattr(reservationsystem_Person, "name")
    descriptor = None
    for klass in reservationsystem_Person.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_reservationsystem_person_has_addr():
    assert hasattr(reservationsystem_Person, "addr")
    descriptor = None
    for klass in reservationsystem_Person.__mro__:
        if "addr" in klass.__dict__:
            descriptor = klass.__dict__["addr"]
            break
    assert isinstance(descriptor, property)

def test_reservationsystem_person_has_FamilyName():
    assert hasattr(reservationsystem_Person, "FamilyName")
    descriptor = None
    for klass in reservationsystem_Person.__mro__:
        if "FamilyName" in klass.__dict__:
            descriptor = klass.__dict__["FamilyName"]
            break
    assert isinstance(descriptor, property)

def test_reservationsystem_person_has_gender():
    assert hasattr(reservationsystem_Person, "gender")
    descriptor = None
    for klass in reservationsystem_Person.__mro__:
        if "gender" in klass.__dict__:
            descriptor = klass.__dict__["gender"]
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
Booking_strategy = st.builds(
    Booking,
)
reservationsystem_City_strategy = st.builds(
    reservationsystem_City,
    name=
        safe_text,
    abbr=
        safe_text,
    id=
        st.integers()
)
reservationsystem_Plane_strategy = st.builds(
    reservationsystem_Plane,
    model=
        safe_text,
    crewNum=
        st.integers(),
    id=
        safe_text,
    capacity=
        st.integers()
)
reservationsystem_Airport_strategy = st.builds(
    reservationsystem_Airport,
    abbr=
        safe_text,
    id=
        st.integers(),
    name=
        safe_text
)
reservationsystem_GeneralFlight_strategy = st.builds(
    reservationsystem_GeneralFlight,
    arrivalTime=
        safe_text,
    departureTime=
        safe_text,
    flightNo=
        safe_text
)
reservationsystem_Seat_strategy = st.builds(
    reservationsystem_Seat,
    isExit=
        st.booleans(),
    no=
        safe_text,
    type=
        st.integers()
)
reservationsystem_PaymentInfo_strategy = st.builds(
    reservationsystem_PaymentInfo,
    cardNo=
        safe_text,
    id=
        safe_text,
    type=
        st.integers(),
    createTime=
        st.dates(),
    payTime=
        st.dates(),
    cardOwner=
        safe_text,
    status=
        st.integers(),
    cardAddr=
        safe_text
)
Crew_strategy = st.builds(
    Crew,
)
reservationsystem_Attendant_strategy = st.builds(
    reservationsystem_Attendant,
)
reservationsystem_Pilot_strategy = st.builds(
    reservationsystem_Pilot,
    experience=
        st.integers(),
    certificationId=
        safe_text
)
reservationsystem_Booking_strategy = st.builds(
    reservationsystem_Booking,
    baggageInfo=
        safe_text,
    bookingStatus=
        st.integers(),
    bookNo=
        safe_text
)
reservationsystem_SpecificFlight_strategy = st.builds(
    reservationsystem_SpecificFlight,
    realArriTime=
        st.dates(),
    status=
        st.integers(),
    date=
        st.dates(),
    realDepTime=
        st.dates(),
    id=
        st.integers()
)
Person_strategy = st.builds(
    Person,
)
reservationsystem_Passenger_strategy = st.builds(
    reservationsystem_Passenger,
    foodPref=
        safe_text,
    specialNeeds=
        safe_text
)
reservationsystem_Crew_strategy = st.builds(
    reservationsystem_Crew,
    employeeId=
        safe_text
)
reservationsystem_User_strategy = st.builds(
    reservationsystem_User,
    userType=
        safe_text,
    userName=
        safe_text,
    md5Pwd=
        safe_text
)
reservationsystem_Person_strategy = st.builds(
    reservationsystem_Person,
    citizenship=
        safe_text,
    birthDate=
        st.dates(),
    email=
        safe_text,
    middleName=
        safe_text,
    phone=
        safe_text,
    passportId=
        safe_text,
    id=
        st.integers(),
    residence=
        safe_text,
    name=
        safe_text,
    addr=
        safe_text,
    FamilyName=
        safe_text,
    gender=
        st.integers()
)

@given(instance=Booking_strategy)
@settings(max_examples=50)
def test_booking_instantiation(instance):
    assert isinstance(instance, Booking)

@given(instance=reservationsystem_City_strategy)
@settings(max_examples=50)
def test_reservationsystem_city_instantiation(instance):
    assert isinstance(instance, reservationsystem_City)



@given(instance=reservationsystem_City_strategy)
def test_reservationsystem_city_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=reservationsystem_City_strategy)
def test_reservationsystem_city_abbr_setter(instance):
    original = instance.abbr
    instance.abbr = original
    assert instance.abbr == original



@given(instance=reservationsystem_City_strategy)
def test_reservationsystem_city_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=reservationsystem_Plane_strategy)
@settings(max_examples=50)
def test_reservationsystem_plane_instantiation(instance):
    assert isinstance(instance, reservationsystem_Plane)



@given(instance=reservationsystem_Plane_strategy)
def test_reservationsystem_plane_model_setter(instance):
    original = instance.model
    instance.model = original
    assert instance.model == original



@given(instance=reservationsystem_Plane_strategy)
def test_reservationsystem_plane_crewNum_setter(instance):
    original = instance.crewNum
    instance.crewNum = original
    assert instance.crewNum == original



@given(instance=reservationsystem_Plane_strategy)
def test_reservationsystem_plane_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=reservationsystem_Plane_strategy)
def test_reservationsystem_plane_capacity_setter(instance):
    original = instance.capacity
    instance.capacity = original
    assert instance.capacity == original

@given(instance=reservationsystem_Airport_strategy)
@settings(max_examples=50)
def test_reservationsystem_airport_instantiation(instance):
    assert isinstance(instance, reservationsystem_Airport)



@given(instance=reservationsystem_Airport_strategy)
def test_reservationsystem_airport_abbr_setter(instance):
    original = instance.abbr
    instance.abbr = original
    assert instance.abbr == original



@given(instance=reservationsystem_Airport_strategy)
def test_reservationsystem_airport_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=reservationsystem_Airport_strategy)
def test_reservationsystem_airport_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=reservationsystem_GeneralFlight_strategy)
@settings(max_examples=50)
def test_reservationsystem_generalflight_instantiation(instance):
    assert isinstance(instance, reservationsystem_GeneralFlight)



@given(instance=reservationsystem_GeneralFlight_strategy)
def test_reservationsystem_generalflight_arrivalTime_setter(instance):
    original = instance.arrivalTime
    instance.arrivalTime = original
    assert instance.arrivalTime == original



@given(instance=reservationsystem_GeneralFlight_strategy)
def test_reservationsystem_generalflight_departureTime_setter(instance):
    original = instance.departureTime
    instance.departureTime = original
    assert instance.departureTime == original



@given(instance=reservationsystem_GeneralFlight_strategy)
def test_reservationsystem_generalflight_flightNo_setter(instance):
    original = instance.flightNo
    instance.flightNo = original
    assert instance.flightNo == original

@given(instance=reservationsystem_Seat_strategy)
@settings(max_examples=50)
def test_reservationsystem_seat_instantiation(instance):
    assert isinstance(instance, reservationsystem_Seat)



@given(instance=reservationsystem_Seat_strategy)
def test_reservationsystem_seat_isExit_setter(instance):
    original = instance.isExit
    instance.isExit = original
    assert instance.isExit == original



@given(instance=reservationsystem_Seat_strategy)
def test_reservationsystem_seat_no_setter(instance):
    original = instance.no
    instance.no = original
    assert instance.no == original



@given(instance=reservationsystem_Seat_strategy)
def test_reservationsystem_seat_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=reservationsystem_PaymentInfo_strategy)
@settings(max_examples=50)
def test_reservationsystem_paymentinfo_instantiation(instance):
    assert isinstance(instance, reservationsystem_PaymentInfo)



@given(instance=reservationsystem_PaymentInfo_strategy)
def test_reservationsystem_paymentinfo_cardNo_setter(instance):
    original = instance.cardNo
    instance.cardNo = original
    assert instance.cardNo == original



@given(instance=reservationsystem_PaymentInfo_strategy)
def test_reservationsystem_paymentinfo_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=reservationsystem_PaymentInfo_strategy)
def test_reservationsystem_paymentinfo_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=reservationsystem_PaymentInfo_strategy)
def test_reservationsystem_paymentinfo_createTime_setter(instance):
    original = instance.createTime
    instance.createTime = original
    assert instance.createTime == original



@given(instance=reservationsystem_PaymentInfo_strategy)
def test_reservationsystem_paymentinfo_payTime_setter(instance):
    original = instance.payTime
    instance.payTime = original
    assert instance.payTime == original



@given(instance=reservationsystem_PaymentInfo_strategy)
def test_reservationsystem_paymentinfo_cardOwner_setter(instance):
    original = instance.cardOwner
    instance.cardOwner = original
    assert instance.cardOwner == original



@given(instance=reservationsystem_PaymentInfo_strategy)
def test_reservationsystem_paymentinfo_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original



@given(instance=reservationsystem_PaymentInfo_strategy)
def test_reservationsystem_paymentinfo_cardAddr_setter(instance):
    original = instance.cardAddr
    instance.cardAddr = original
    assert instance.cardAddr == original

@given(instance=Crew_strategy)
@settings(max_examples=50)
def test_crew_instantiation(instance):
    assert isinstance(instance, Crew)

@given(instance=reservationsystem_Attendant_strategy)
@settings(max_examples=50)
def test_reservationsystem_attendant_instantiation(instance):
    assert isinstance(instance, reservationsystem_Attendant)

@given(instance=reservationsystem_Pilot_strategy)
@settings(max_examples=50)
def test_reservationsystem_pilot_instantiation(instance):
    assert isinstance(instance, reservationsystem_Pilot)



@given(instance=reservationsystem_Pilot_strategy)
def test_reservationsystem_pilot_experience_setter(instance):
    original = instance.experience
    instance.experience = original
    assert instance.experience == original



@given(instance=reservationsystem_Pilot_strategy)
def test_reservationsystem_pilot_certificationId_setter(instance):
    original = instance.certificationId
    instance.certificationId = original
    assert instance.certificationId == original

@given(instance=reservationsystem_Booking_strategy)
@settings(max_examples=50)
def test_reservationsystem_booking_instantiation(instance):
    assert isinstance(instance, reservationsystem_Booking)



@given(instance=reservationsystem_Booking_strategy)
def test_reservationsystem_booking_baggageInfo_setter(instance):
    original = instance.baggageInfo
    instance.baggageInfo = original
    assert instance.baggageInfo == original



@given(instance=reservationsystem_Booking_strategy)
def test_reservationsystem_booking_bookingStatus_setter(instance):
    original = instance.bookingStatus
    instance.bookingStatus = original
    assert instance.bookingStatus == original



@given(instance=reservationsystem_Booking_strategy)
def test_reservationsystem_booking_bookNo_setter(instance):
    original = instance.bookNo
    instance.bookNo = original
    assert instance.bookNo == original

@given(instance=reservationsystem_SpecificFlight_strategy)
@settings(max_examples=50)
def test_reservationsystem_specificflight_instantiation(instance):
    assert isinstance(instance, reservationsystem_SpecificFlight)



@given(instance=reservationsystem_SpecificFlight_strategy)
def test_reservationsystem_specificflight_realArriTime_setter(instance):
    original = instance.realArriTime
    instance.realArriTime = original
    assert instance.realArriTime == original



@given(instance=reservationsystem_SpecificFlight_strategy)
def test_reservationsystem_specificflight_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original



@given(instance=reservationsystem_SpecificFlight_strategy)
def test_reservationsystem_specificflight_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original



@given(instance=reservationsystem_SpecificFlight_strategy)
def test_reservationsystem_specificflight_realDepTime_setter(instance):
    original = instance.realDepTime
    instance.realDepTime = original
    assert instance.realDepTime == original



@given(instance=reservationsystem_SpecificFlight_strategy)
def test_reservationsystem_specificflight_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=reservationsystem_SpecificFlight_strategy)
@settings(max_examples=30)
def test_reservationsystem_specificflight_assignpilot_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.assignPilot(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.assignPilot).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'assignPilot' in reservationsystem_SpecificFlight is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'assignPilot' in reservationsystem_SpecificFlight did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'assignPilot' in reservationsystem_SpecificFlight is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=reservationsystem_SpecificFlight_strategy)
@settings(max_examples=30)
def test_reservationsystem_specificflight_assignattd_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.assignAttd(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.assignAttd).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'assignAttd' in reservationsystem_SpecificFlight is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'assignAttd' in reservationsystem_SpecificFlight did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'assignAttd' in reservationsystem_SpecificFlight is not implemented or raised an error")

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)

@given(instance=reservationsystem_Passenger_strategy)
@settings(max_examples=50)
def test_reservationsystem_passenger_instantiation(instance):
    assert isinstance(instance, reservationsystem_Passenger)



@given(instance=reservationsystem_Passenger_strategy)
def test_reservationsystem_passenger_foodPref_setter(instance):
    original = instance.foodPref
    instance.foodPref = original
    assert instance.foodPref == original



@given(instance=reservationsystem_Passenger_strategy)
def test_reservationsystem_passenger_specialNeeds_setter(instance):
    original = instance.specialNeeds
    instance.specialNeeds = original
    assert instance.specialNeeds == original

@given(instance=reservationsystem_Crew_strategy)
@settings(max_examples=50)
def test_reservationsystem_crew_instantiation(instance):
    assert isinstance(instance, reservationsystem_Crew)



@given(instance=reservationsystem_Crew_strategy)
def test_reservationsystem_crew_employeeId_setter(instance):
    original = instance.employeeId
    instance.employeeId = original
    assert instance.employeeId == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=reservationsystem_Crew_strategy)
@settings(max_examples=30)
def test_reservationsystem_crew_setleader_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.setLeader()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.setLeader).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'setLeader' in reservationsystem_Crew is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'setLeader' in reservationsystem_Crew did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'setLeader' in reservationsystem_Crew is not implemented or raised an error")

@given(instance=reservationsystem_User_strategy)
@settings(max_examples=50)
def test_reservationsystem_user_instantiation(instance):
    assert isinstance(instance, reservationsystem_User)



@given(instance=reservationsystem_User_strategy)
def test_reservationsystem_user_userType_setter(instance):
    original = instance.userType
    instance.userType = original
    assert instance.userType == original



@given(instance=reservationsystem_User_strategy)
def test_reservationsystem_user_userName_setter(instance):
    original = instance.userName
    instance.userName = original
    assert instance.userName == original



@given(instance=reservationsystem_User_strategy)
def test_reservationsystem_user_md5Pwd_setter(instance):
    original = instance.md5Pwd
    instance.md5Pwd = original
    assert instance.md5Pwd == original

@given(instance=reservationsystem_Person_strategy)
@settings(max_examples=50)
def test_reservationsystem_person_instantiation(instance):
    assert isinstance(instance, reservationsystem_Person)



@given(instance=reservationsystem_Person_strategy)
def test_reservationsystem_person_citizenship_setter(instance):
    original = instance.citizenship
    instance.citizenship = original
    assert instance.citizenship == original



@given(instance=reservationsystem_Person_strategy)
def test_reservationsystem_person_birthDate_setter(instance):
    original = instance.birthDate
    instance.birthDate = original
    assert instance.birthDate == original



@given(instance=reservationsystem_Person_strategy)
def test_reservationsystem_person_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=reservationsystem_Person_strategy)
def test_reservationsystem_person_middleName_setter(instance):
    original = instance.middleName
    instance.middleName = original
    assert instance.middleName == original



@given(instance=reservationsystem_Person_strategy)
def test_reservationsystem_person_phone_setter(instance):
    original = instance.phone
    instance.phone = original
    assert instance.phone == original



@given(instance=reservationsystem_Person_strategy)
def test_reservationsystem_person_passportId_setter(instance):
    original = instance.passportId
    instance.passportId = original
    assert instance.passportId == original



@given(instance=reservationsystem_Person_strategy)
def test_reservationsystem_person_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=reservationsystem_Person_strategy)
def test_reservationsystem_person_residence_setter(instance):
    original = instance.residence
    instance.residence = original
    assert instance.residence == original



@given(instance=reservationsystem_Person_strategy)
def test_reservationsystem_person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=reservationsystem_Person_strategy)
def test_reservationsystem_person_addr_setter(instance):
    original = instance.addr
    instance.addr = original
    assert instance.addr == original



@given(instance=reservationsystem_Person_strategy)
def test_reservationsystem_person_FamilyName_setter(instance):
    original = instance.FamilyName
    instance.FamilyName = original
    assert instance.FamilyName == original



@given(instance=reservationsystem_Person_strategy)
def test_reservationsystem_person_gender_setter(instance):
    original = instance.gender
    instance.gender = original
    assert instance.gender == original
