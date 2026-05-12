import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    FeedBack,
    CheckOut_Entity,
    StayIn_Entity,
    User_Entity,
    CheckIn_Entity,
    PostStay_Entity,
    Payment,
    Booking_Entity,
    Bill_Details,
    Booking_Status,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_feedback_is_not_abstract():
    assert not inspect.isabstract(FeedBack)


def test_feedback_constructor_exists():
    assert callable(FeedBack.__init__)


def test_feedback_constructor_args():
    sig = inspect.signature(FeedBack.__init__)
    params = list(sig.parameters.keys())
    assert "Rating" in params, "Missing parameter 'Rating'"
    assert "FeedBackMessage" in params, "Missing parameter 'FeedBackMessage'"

def test_feedback_has_Rating():
    assert hasattr(FeedBack, "Rating")
    descriptor = None
    for klass in FeedBack.__mro__:
        if "Rating" in klass.__dict__:
            descriptor = klass.__dict__["Rating"]
            break
    assert isinstance(descriptor, property)

def test_feedback_has_FeedBackMessage():
    assert hasattr(FeedBack, "FeedBackMessage")
    descriptor = None
    for klass in FeedBack.__mro__:
        if "FeedBackMessage" in klass.__dict__:
            descriptor = klass.__dict__["FeedBackMessage"]
            break
    assert isinstance(descriptor, property)



def test_checkout_entity_is_not_abstract():
    assert not inspect.isabstract(CheckOut_Entity)


def test_checkout_entity_constructor_exists():
    assert callable(CheckOut_Entity.__init__)


def test_checkout_entity_constructor_args():
    sig = inspect.signature(CheckOut_Entity.__init__)
    params = list(sig.parameters.keys())
    assert "price" in params, "Missing parameter 'price'"
    assert "ItemisedBillDetails" in params, "Missing parameter 'ItemisedBillDetails'"

def test_checkout_entity_has_price():
    assert hasattr(CheckOut_Entity, "price")
    descriptor = None
    for klass in CheckOut_Entity.__mro__:
        if "price" in klass.__dict__:
            descriptor = klass.__dict__["price"]
            break
    assert isinstance(descriptor, property)

def test_checkout_entity_has_ItemisedBillDetails():
    assert hasattr(CheckOut_Entity, "ItemisedBillDetails")
    descriptor = None
    for klass in CheckOut_Entity.__mro__:
        if "ItemisedBillDetails" in klass.__dict__:
            descriptor = klass.__dict__["ItemisedBillDetails"]
            break
    assert isinstance(descriptor, property)



def test_stayin_entity_is_not_abstract():
    assert not inspect.isabstract(StayIn_Entity)


def test_stayin_entity_constructor_exists():
    assert callable(StayIn_Entity.__init__)


def test_stayin_entity_constructor_args():
    sig = inspect.signature(StayIn_Entity.__init__)
    params = list(sig.parameters.keys())
    assert "promotionsList" in params, "Missing parameter 'promotionsList'"
    assert "oodList" in params, "Missing parameter 'oodList'"
    assert "placeOfInterest" in params, "Missing parameter 'placeOfInterest'"
    assert "EntertainMentList" in params, "Missing parameter 'EntertainMentList'"
    assert "status" in params, "Missing parameter 'status'"
    assert "InPremisesList" in params, "Missing parameter 'InPremisesList'"

def test_stayin_entity_has_promotionsList():
    assert hasattr(StayIn_Entity, "promotionsList")
    descriptor = None
    for klass in StayIn_Entity.__mro__:
        if "promotionsList" in klass.__dict__:
            descriptor = klass.__dict__["promotionsList"]
            break
    assert isinstance(descriptor, property)

def test_stayin_entity_has_oodList():
    assert hasattr(StayIn_Entity, "oodList")
    descriptor = None
    for klass in StayIn_Entity.__mro__:
        if "oodList" in klass.__dict__:
            descriptor = klass.__dict__["oodList"]
            break
    assert isinstance(descriptor, property)

def test_stayin_entity_has_placeOfInterest():
    assert hasattr(StayIn_Entity, "placeOfInterest")
    descriptor = None
    for klass in StayIn_Entity.__mro__:
        if "placeOfInterest" in klass.__dict__:
            descriptor = klass.__dict__["placeOfInterest"]
            break
    assert isinstance(descriptor, property)

def test_stayin_entity_has_EntertainMentList():
    assert hasattr(StayIn_Entity, "EntertainMentList")
    descriptor = None
    for klass in StayIn_Entity.__mro__:
        if "EntertainMentList" in klass.__dict__:
            descriptor = klass.__dict__["EntertainMentList"]
            break
    assert isinstance(descriptor, property)

def test_stayin_entity_has_status():
    assert hasattr(StayIn_Entity, "status")
    descriptor = None
    for klass in StayIn_Entity.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)

def test_stayin_entity_has_InPremisesList():
    assert hasattr(StayIn_Entity, "InPremisesList")
    descriptor = None
    for klass in StayIn_Entity.__mro__:
        if "InPremisesList" in klass.__dict__:
            descriptor = klass.__dict__["InPremisesList"]
            break
    assert isinstance(descriptor, property)



def test_user_entity_is_not_abstract():
    assert not inspect.isabstract(User_Entity)


def test_user_entity_constructor_exists():
    assert callable(User_Entity.__init__)


def test_user_entity_constructor_args():
    sig = inspect.signature(User_Entity.__init__)
    params = list(sig.parameters.keys())
    assert "City" in params, "Missing parameter 'City'"
    assert "login" in params, "Missing parameter 'login'"
    assert "password" in params, "Missing parameter 'password'"
    assert "Email" in params, "Missing parameter 'Email'"

def test_user_entity_has_City():
    assert hasattr(User_Entity, "City")
    descriptor = None
    for klass in User_Entity.__mro__:
        if "City" in klass.__dict__:
            descriptor = klass.__dict__["City"]
            break
    assert isinstance(descriptor, property)

def test_user_entity_has_login():
    assert hasattr(User_Entity, "login")
    descriptor = None
    for klass in User_Entity.__mro__:
        if "login" in klass.__dict__:
            descriptor = klass.__dict__["login"]
            break
    assert isinstance(descriptor, property)

def test_user_entity_has_password():
    assert hasattr(User_Entity, "password")
    descriptor = None
    for klass in User_Entity.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)

def test_user_entity_has_Email():
    assert hasattr(User_Entity, "Email")
    descriptor = None
    for klass in User_Entity.__mro__:
        if "Email" in klass.__dict__:
            descriptor = klass.__dict__["Email"]
            break
    assert isinstance(descriptor, property)



def test_checkin_entity_is_not_abstract():
    assert not inspect.isabstract(CheckIn_Entity)


def test_checkin_entity_constructor_exists():
    assert callable(CheckIn_Entity.__init__)


def test_checkin_entity_constructor_args():
    sig = inspect.signature(CheckIn_Entity.__init__)
    params = list(sig.parameters.keys())
    assert "QRCode" in params, "Missing parameter 'QRCode'"
    assert "CheckInStatus" in params, "Missing parameter 'CheckInStatus'"
    assert "paymentMode" in params, "Missing parameter 'paymentMode'"
    assert "MobileKey" in params, "Missing parameter 'MobileKey'"
    assert "PickUpAddress" in params, "Missing parameter 'PickUpAddress'"

def test_checkin_entity_has_QRCode():
    assert hasattr(CheckIn_Entity, "QRCode")
    descriptor = None
    for klass in CheckIn_Entity.__mro__:
        if "QRCode" in klass.__dict__:
            descriptor = klass.__dict__["QRCode"]
            break
    assert isinstance(descriptor, property)

def test_checkin_entity_has_CheckInStatus():
    assert hasattr(CheckIn_Entity, "CheckInStatus")
    descriptor = None
    for klass in CheckIn_Entity.__mro__:
        if "CheckInStatus" in klass.__dict__:
            descriptor = klass.__dict__["CheckInStatus"]
            break
    assert isinstance(descriptor, property)

def test_checkin_entity_has_paymentMode():
    assert hasattr(CheckIn_Entity, "paymentMode")
    descriptor = None
    for klass in CheckIn_Entity.__mro__:
        if "paymentMode" in klass.__dict__:
            descriptor = klass.__dict__["paymentMode"]
            break
    assert isinstance(descriptor, property)

def test_checkin_entity_has_MobileKey():
    assert hasattr(CheckIn_Entity, "MobileKey")
    descriptor = None
    for klass in CheckIn_Entity.__mro__:
        if "MobileKey" in klass.__dict__:
            descriptor = klass.__dict__["MobileKey"]
            break
    assert isinstance(descriptor, property)

def test_checkin_entity_has_PickUpAddress():
    assert hasattr(CheckIn_Entity, "PickUpAddress")
    descriptor = None
    for klass in CheckIn_Entity.__mro__:
        if "PickUpAddress" in klass.__dict__:
            descriptor = klass.__dict__["PickUpAddress"]
            break
    assert isinstance(descriptor, property)



def test_poststay_entity_is_not_abstract():
    assert not inspect.isabstract(PostStay_Entity)


def test_poststay_entity_constructor_exists():
    assert callable(PostStay_Entity.__init__)


def test_poststay_entity_constructor_args():
    sig = inspect.signature(PostStay_Entity.__init__)
    params = list(sig.parameters.keys())
    assert "ThanksMessage" in params, "Missing parameter 'ThanksMessage'"
    assert "PromotionPoints" in params, "Missing parameter 'PromotionPoints'"
    assert "DiscountPoints" in params, "Missing parameter 'DiscountPoints'"

def test_poststay_entity_has_ThanksMessage():
    assert hasattr(PostStay_Entity, "ThanksMessage")
    descriptor = None
    for klass in PostStay_Entity.__mro__:
        if "ThanksMessage" in klass.__dict__:
            descriptor = klass.__dict__["ThanksMessage"]
            break
    assert isinstance(descriptor, property)

def test_poststay_entity_has_PromotionPoints():
    assert hasattr(PostStay_Entity, "PromotionPoints")
    descriptor = None
    for klass in PostStay_Entity.__mro__:
        if "PromotionPoints" in klass.__dict__:
            descriptor = klass.__dict__["PromotionPoints"]
            break
    assert isinstance(descriptor, property)

def test_poststay_entity_has_DiscountPoints():
    assert hasattr(PostStay_Entity, "DiscountPoints")
    descriptor = None
    for klass in PostStay_Entity.__mro__:
        if "DiscountPoints" in klass.__dict__:
            descriptor = klass.__dict__["DiscountPoints"]
            break
    assert isinstance(descriptor, property)



def test_payment_is_not_abstract():
    assert not inspect.isabstract(Payment)


def test_payment_constructor_exists():
    assert callable(Payment.__init__)


def test_payment_constructor_args():
    sig = inspect.signature(Payment.__init__)
    params = list(sig.parameters.keys())
    assert "paidDate" in params, "Missing parameter 'paidDate'"
    assert "details" in params, "Missing parameter 'details'"
    assert "total" in params, "Missing parameter 'total'"

def test_payment_has_paidDate():
    assert hasattr(Payment, "paidDate")
    descriptor = None
    for klass in Payment.__mro__:
        if "paidDate" in klass.__dict__:
            descriptor = klass.__dict__["paidDate"]
            break
    assert isinstance(descriptor, property)

def test_payment_has_details():
    assert hasattr(Payment, "details")
    descriptor = None
    for klass in Payment.__mro__:
        if "details" in klass.__dict__:
            descriptor = klass.__dict__["details"]
            break
    assert isinstance(descriptor, property)

def test_payment_has_total():
    assert hasattr(Payment, "total")
    descriptor = None
    for klass in Payment.__mro__:
        if "total" in klass.__dict__:
            descriptor = klass.__dict__["total"]
            break
    assert isinstance(descriptor, property)



def test_booking_entity_is_not_abstract():
    assert not inspect.isabstract(Booking_Entity)


def test_booking_entity_constructor_exists():
    assert callable(Booking_Entity.__init__)


def test_booking_entity_constructor_args():
    sig = inspect.signature(Booking_Entity.__init__)
    params = list(sig.parameters.keys())
    assert "NoOfDays" in params, "Missing parameter 'NoOfDays'"
    assert "email" in params, "Missing parameter 'email'"
    assert "phone" in params, "Missing parameter 'phone'"
    assert "CheckInDate" in params, "Missing parameter 'CheckInDate'"
    assert "address" in params, "Missing parameter 'address'"

def test_booking_entity_has_NoOfDays():
    assert hasattr(Booking_Entity, "NoOfDays")
    descriptor = None
    for klass in Booking_Entity.__mro__:
        if "NoOfDays" in klass.__dict__:
            descriptor = klass.__dict__["NoOfDays"]
            break
    assert isinstance(descriptor, property)

def test_booking_entity_has_email():
    assert hasattr(Booking_Entity, "email")
    descriptor = None
    for klass in Booking_Entity.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)

def test_booking_entity_has_phone():
    assert hasattr(Booking_Entity, "phone")
    descriptor = None
    for klass in Booking_Entity.__mro__:
        if "phone" in klass.__dict__:
            descriptor = klass.__dict__["phone"]
            break
    assert isinstance(descriptor, property)

def test_booking_entity_has_CheckInDate():
    assert hasattr(Booking_Entity, "CheckInDate")
    descriptor = None
    for klass in Booking_Entity.__mro__:
        if "CheckInDate" in klass.__dict__:
            descriptor = klass.__dict__["CheckInDate"]
            break
    assert isinstance(descriptor, property)

def test_booking_entity_has_address():
    assert hasattr(Booking_Entity, "address")
    descriptor = None
    for klass in Booking_Entity.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)

def test_bill_details_exists():
    # Check that the Enumeration exists
    assert Bill_Details is not None

def test_bill_details_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Bill_Details]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Bill_Details"

def test_booking_status_exists():
    # Check that the Enumeration exists
    assert Booking_Status is not None

def test_booking_status_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Booking_Status]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Booking_Status"


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
FeedBack_strategy = st.builds(
    FeedBack,
    Rating=
        safe_text,
    FeedBackMessage=
        safe_text
)
CheckOut_Entity_strategy = st.builds(
    CheckOut_Entity,
    price=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    ItemisedBillDetails=
        st.none()
)
StayIn_Entity_strategy = st.builds(
    StayIn_Entity,
    promotionsList=
        safe_text,
    oodList=
        safe_text,
    placeOfInterest=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    EntertainMentList=
        safe_text,
    status=
        st.none(),
    InPremisesList=
        safe_text
)
User_Entity_strategy = st.builds(
    User_Entity,
    City=
        safe_text,
    login=
        safe_text,
    password=
        safe_text,
    Email=
        safe_text
)
CheckIn_Entity_strategy = st.builds(
    CheckIn_Entity,
    QRCode=
        safe_text,
    CheckInStatus=
        safe_text,
    paymentMode=
        safe_text,
    MobileKey=
        safe_text,
    PickUpAddress=
        safe_text
)
PostStay_Entity_strategy = st.builds(
    PostStay_Entity,
    ThanksMessage=
        safe_text,
    PromotionPoints=
        safe_text,
    DiscountPoints=
        safe_text
)
Payment_strategy = st.builds(
    Payment,
    paidDate=
        st.dates(),
    details=
        safe_text,
    total=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
Booking_Entity_strategy = st.builds(
    Booking_Entity,
    NoOfDays=
        st.integers(),
    email=
        safe_text,
    phone=
        safe_text,
    CheckInDate=
        st.dates(),
    address=
        safe_text
)

@given(instance=FeedBack_strategy)
@settings(max_examples=50)
def test_feedback_instantiation(instance):
    assert isinstance(instance, FeedBack)



@given(instance=FeedBack_strategy)
def test_feedback_Rating_setter(instance):
    original = instance.Rating
    instance.Rating = original
    assert instance.Rating == original



@given(instance=FeedBack_strategy)
def test_feedback_FeedBackMessage_setter(instance):
    original = instance.FeedBackMessage
    instance.FeedBackMessage = original
    assert instance.FeedBackMessage == original

@given(instance=CheckOut_Entity_strategy)
@settings(max_examples=50)
def test_checkout_entity_instantiation(instance):
    assert isinstance(instance, CheckOut_Entity)



@given(instance=CheckOut_Entity_strategy)
def test_checkout_entity_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original



@given(instance=CheckOut_Entity_strategy)
def test_checkout_entity_ItemisedBillDetails_setter(instance):
    original = instance.ItemisedBillDetails
    instance.ItemisedBillDetails = original
    assert instance.ItemisedBillDetails == original

@given(instance=StayIn_Entity_strategy)
@settings(max_examples=50)
def test_stayin_entity_instantiation(instance):
    assert isinstance(instance, StayIn_Entity)



@given(instance=StayIn_Entity_strategy)
def test_stayin_entity_promotionsList_setter(instance):
    original = instance.promotionsList
    instance.promotionsList = original
    assert instance.promotionsList == original



@given(instance=StayIn_Entity_strategy)
def test_stayin_entity_oodList_setter(instance):
    original = instance.oodList
    instance.oodList = original
    assert instance.oodList == original



@given(instance=StayIn_Entity_strategy)
def test_stayin_entity_placeOfInterest_setter(instance):
    original = instance.placeOfInterest
    instance.placeOfInterest = original
    assert instance.placeOfInterest == original



@given(instance=StayIn_Entity_strategy)
def test_stayin_entity_EntertainMentList_setter(instance):
    original = instance.EntertainMentList
    instance.EntertainMentList = original
    assert instance.EntertainMentList == original



@given(instance=StayIn_Entity_strategy)
def test_stayin_entity_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original



@given(instance=StayIn_Entity_strategy)
def test_stayin_entity_InPremisesList_setter(instance):
    original = instance.InPremisesList
    instance.InPremisesList = original
    assert instance.InPremisesList == original

@given(instance=User_Entity_strategy)
@settings(max_examples=50)
def test_user_entity_instantiation(instance):
    assert isinstance(instance, User_Entity)



@given(instance=User_Entity_strategy)
def test_user_entity_City_setter(instance):
    original = instance.City
    instance.City = original
    assert instance.City == original



@given(instance=User_Entity_strategy)
def test_user_entity_login_setter(instance):
    original = instance.login
    instance.login = original
    assert instance.login == original



@given(instance=User_Entity_strategy)
def test_user_entity_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=User_Entity_strategy)
def test_user_entity_Email_setter(instance):
    original = instance.Email
    instance.Email = original
    assert instance.Email == original

@given(instance=CheckIn_Entity_strategy)
@settings(max_examples=50)
def test_checkin_entity_instantiation(instance):
    assert isinstance(instance, CheckIn_Entity)



@given(instance=CheckIn_Entity_strategy)
def test_checkin_entity_QRCode_setter(instance):
    original = instance.QRCode
    instance.QRCode = original
    assert instance.QRCode == original



@given(instance=CheckIn_Entity_strategy)
def test_checkin_entity_CheckInStatus_setter(instance):
    original = instance.CheckInStatus
    instance.CheckInStatus = original
    assert instance.CheckInStatus == original



@given(instance=CheckIn_Entity_strategy)
def test_checkin_entity_paymentMode_setter(instance):
    original = instance.paymentMode
    instance.paymentMode = original
    assert instance.paymentMode == original



@given(instance=CheckIn_Entity_strategy)
def test_checkin_entity_MobileKey_setter(instance):
    original = instance.MobileKey
    instance.MobileKey = original
    assert instance.MobileKey == original



@given(instance=CheckIn_Entity_strategy)
def test_checkin_entity_PickUpAddress_setter(instance):
    original = instance.PickUpAddress
    instance.PickUpAddress = original
    assert instance.PickUpAddress == original

@given(instance=PostStay_Entity_strategy)
@settings(max_examples=50)
def test_poststay_entity_instantiation(instance):
    assert isinstance(instance, PostStay_Entity)



@given(instance=PostStay_Entity_strategy)
def test_poststay_entity_ThanksMessage_setter(instance):
    original = instance.ThanksMessage
    instance.ThanksMessage = original
    assert instance.ThanksMessage == original



@given(instance=PostStay_Entity_strategy)
def test_poststay_entity_PromotionPoints_setter(instance):
    original = instance.PromotionPoints
    instance.PromotionPoints = original
    assert instance.PromotionPoints == original



@given(instance=PostStay_Entity_strategy)
def test_poststay_entity_DiscountPoints_setter(instance):
    original = instance.DiscountPoints
    instance.DiscountPoints = original
    assert instance.DiscountPoints == original

@given(instance=Payment_strategy)
@settings(max_examples=50)
def test_payment_instantiation(instance):
    assert isinstance(instance, Payment)



@given(instance=Payment_strategy)
def test_payment_paidDate_setter(instance):
    original = instance.paidDate
    instance.paidDate = original
    assert instance.paidDate == original



@given(instance=Payment_strategy)
def test_payment_details_setter(instance):
    original = instance.details
    instance.details = original
    assert instance.details == original



@given(instance=Payment_strategy)
def test_payment_total_setter(instance):
    original = instance.total
    instance.total = original
    assert instance.total == original

@given(instance=Booking_Entity_strategy)
@settings(max_examples=50)
def test_booking_entity_instantiation(instance):
    assert isinstance(instance, Booking_Entity)



@given(instance=Booking_Entity_strategy)
def test_booking_entity_NoOfDays_setter(instance):
    original = instance.NoOfDays
    instance.NoOfDays = original
    assert instance.NoOfDays == original



@given(instance=Booking_Entity_strategy)
def test_booking_entity_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=Booking_Entity_strategy)
def test_booking_entity_phone_setter(instance):
    original = instance.phone
    instance.phone = original
    assert instance.phone == original



@given(instance=Booking_Entity_strategy)
def test_booking_entity_CheckInDate_setter(instance):
    original = instance.CheckInDate
    instance.CheckInDate = original
    assert instance.CheckInDate == original



@given(instance=Booking_Entity_strategy)
def test_booking_entity_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original
