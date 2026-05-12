import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Mail,
    Payment,
    Logout,
    Attendance,
    Login,
    Calender_Event,
    Volunteer,
    Admin,
    Normal_user,
    void,
    SuperAdmin,
    Profile,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mail_is_not_abstract():
    assert not inspect.isabstract(Mail)


def test_mail_constructor_exists():
    assert callable(Mail.__init__)


def test_mail_constructor_args():
    sig = inspect.signature(Mail.__init__)
    params = list(sig.parameters.keys())
    assert "sendTo" in params, "Missing parameter 'sendTo'"
    assert "subject" in params, "Missing parameter 'subject'"
    assert "emailID" in params, "Missing parameter 'emailID'"
    assert "sendBy" in params, "Missing parameter 'sendBy'"

def test_mail_has_sendTo():
    assert hasattr(Mail, "sendTo")
    descriptor = None
    for klass in Mail.__mro__:
        if "sendTo" in klass.__dict__:
            descriptor = klass.__dict__["sendTo"]
            break
    assert isinstance(descriptor, property)

def test_mail_has_subject():
    assert hasattr(Mail, "subject")
    descriptor = None
    for klass in Mail.__mro__:
        if "subject" in klass.__dict__:
            descriptor = klass.__dict__["subject"]
            break
    assert isinstance(descriptor, property)

def test_mail_has_emailID():
    assert hasattr(Mail, "emailID")
    descriptor = None
    for klass in Mail.__mro__:
        if "emailID" in klass.__dict__:
            descriptor = klass.__dict__["emailID"]
            break
    assert isinstance(descriptor, property)

def test_mail_has_sendBy():
    assert hasattr(Mail, "sendBy")
    descriptor = None
    for klass in Mail.__mro__:
        if "sendBy" in klass.__dict__:
            descriptor = klass.__dict__["sendBy"]
            break
    assert isinstance(descriptor, property)



def test_payment_is_not_abstract():
    assert not inspect.isabstract(Payment)


def test_payment_constructor_exists():
    assert callable(Payment.__init__)


def test_payment_constructor_args():
    sig = inspect.signature(Payment.__init__)
    params = list(sig.parameters.keys())
    assert "amount" in params, "Missing parameter 'amount'"
    assert "cardType" in params, "Missing parameter 'cardType'"
    assert "cardNumber" in params, "Missing parameter 'cardNumber'"
    assert "expiryDate" in params, "Missing parameter 'expiryDate'"
    assert "issuerName" in params, "Missing parameter 'issuerName'"

def test_payment_has_amount():
    assert hasattr(Payment, "amount")
    descriptor = None
    for klass in Payment.__mro__:
        if "amount" in klass.__dict__:
            descriptor = klass.__dict__["amount"]
            break
    assert isinstance(descriptor, property)

def test_payment_has_cardType():
    assert hasattr(Payment, "cardType")
    descriptor = None
    for klass in Payment.__mro__:
        if "cardType" in klass.__dict__:
            descriptor = klass.__dict__["cardType"]
            break
    assert isinstance(descriptor, property)

def test_payment_has_cardNumber():
    assert hasattr(Payment, "cardNumber")
    descriptor = None
    for klass in Payment.__mro__:
        if "cardNumber" in klass.__dict__:
            descriptor = klass.__dict__["cardNumber"]
            break
    assert isinstance(descriptor, property)

def test_payment_has_expiryDate():
    assert hasattr(Payment, "expiryDate")
    descriptor = None
    for klass in Payment.__mro__:
        if "expiryDate" in klass.__dict__:
            descriptor = klass.__dict__["expiryDate"]
            break
    assert isinstance(descriptor, property)

def test_payment_has_issuerName():
    assert hasattr(Payment, "issuerName")
    descriptor = None
    for klass in Payment.__mro__:
        if "issuerName" in klass.__dict__:
            descriptor = klass.__dict__["issuerName"]
            break
    assert isinstance(descriptor, property)



def test_logout_is_not_abstract():
    assert not inspect.isabstract(Logout)


def test_logout_constructor_exists():
    assert callable(Logout.__init__)


def test_logout_constructor_args():
    sig = inspect.signature(Logout.__init__)
    params = list(sig.parameters.keys())



def test_attendance_is_not_abstract():
    assert not inspect.isabstract(Attendance)


def test_attendance_constructor_exists():
    assert callable(Attendance.__init__)


def test_attendance_constructor_args():
    sig = inspect.signature(Attendance.__init__)
    params = list(sig.parameters.keys())
    assert "checkInTime" in params, "Missing parameter 'checkInTime'"
    assert "attendanceID" in params, "Missing parameter 'attendanceID'"
    assert "checkOutTime" in params, "Missing parameter 'checkOutTime'"

def test_attendance_has_checkInTime():
    assert hasattr(Attendance, "checkInTime")
    descriptor = None
    for klass in Attendance.__mro__:
        if "checkInTime" in klass.__dict__:
            descriptor = klass.__dict__["checkInTime"]
            break
    assert isinstance(descriptor, property)

def test_attendance_has_attendanceID():
    assert hasattr(Attendance, "attendanceID")
    descriptor = None
    for klass in Attendance.__mro__:
        if "attendanceID" in klass.__dict__:
            descriptor = klass.__dict__["attendanceID"]
            break
    assert isinstance(descriptor, property)

def test_attendance_has_checkOutTime():
    assert hasattr(Attendance, "checkOutTime")
    descriptor = None
    for klass in Attendance.__mro__:
        if "checkOutTime" in klass.__dict__:
            descriptor = klass.__dict__["checkOutTime"]
            break
    assert isinstance(descriptor, property)



def test_login_is_not_abstract():
    assert not inspect.isabstract(Login)


def test_login_constructor_exists():
    assert callable(Login.__init__)


def test_login_constructor_args():
    sig = inspect.signature(Login.__init__)
    params = list(sig.parameters.keys())
    assert "loggedinTime" in params, "Missing parameter 'loggedinTime'"
    assert "loggedoutTime" in params, "Missing parameter 'loggedoutTime'"
    assert "userID" in params, "Missing parameter 'userID'"

def test_login_has_loggedinTime():
    assert hasattr(Login, "loggedinTime")
    descriptor = None
    for klass in Login.__mro__:
        if "loggedinTime" in klass.__dict__:
            descriptor = klass.__dict__["loggedinTime"]
            break
    assert isinstance(descriptor, property)

def test_login_has_loggedoutTime():
    assert hasattr(Login, "loggedoutTime")
    descriptor = None
    for klass in Login.__mro__:
        if "loggedoutTime" in klass.__dict__:
            descriptor = klass.__dict__["loggedoutTime"]
            break
    assert isinstance(descriptor, property)

def test_login_has_userID():
    assert hasattr(Login, "userID")
    descriptor = None
    for klass in Login.__mro__:
        if "userID" in klass.__dict__:
            descriptor = klass.__dict__["userID"]
            break
    assert isinstance(descriptor, property)



def test_calender_event_is_not_abstract():
    assert not inspect.isabstract(Calender_Event)


def test_calender_event_constructor_exists():
    assert callable(Calender_Event.__init__)


def test_calender_event_constructor_args():
    sig = inspect.signature(Calender_Event.__init__)
    params = list(sig.parameters.keys())
    assert "time" in params, "Missing parameter 'time'"
    assert "participantAmount" in params, "Missing parameter 'participantAmount'"
    assert "category" in params, "Missing parameter 'category'"
    assert "nomarlUser" in params, "Missing parameter 'nomarlUser'"
    assert "date" in params, "Missing parameter 'date'"
    assert "description" in params, "Missing parameter 'description'"
    assert "admin" in params, "Missing parameter 'admin'"
    assert "volunteer" in params, "Missing parameter 'volunteer'"
    assert "eventType" in params, "Missing parameter 'eventType'"

def test_calender_event_has_time():
    assert hasattr(Calender_Event, "time")
    descriptor = None
    for klass in Calender_Event.__mro__:
        if "time" in klass.__dict__:
            descriptor = klass.__dict__["time"]
            break
    assert isinstance(descriptor, property)

def test_calender_event_has_participantAmount():
    assert hasattr(Calender_Event, "participantAmount")
    descriptor = None
    for klass in Calender_Event.__mro__:
        if "participantAmount" in klass.__dict__:
            descriptor = klass.__dict__["participantAmount"]
            break
    assert isinstance(descriptor, property)

def test_calender_event_has_category():
    assert hasattr(Calender_Event, "category")
    descriptor = None
    for klass in Calender_Event.__mro__:
        if "category" in klass.__dict__:
            descriptor = klass.__dict__["category"]
            break
    assert isinstance(descriptor, property)

def test_calender_event_has_nomarlUser():
    assert hasattr(Calender_Event, "nomarlUser")
    descriptor = None
    for klass in Calender_Event.__mro__:
        if "nomarlUser" in klass.__dict__:
            descriptor = klass.__dict__["nomarlUser"]
            break
    assert isinstance(descriptor, property)

def test_calender_event_has_date():
    assert hasattr(Calender_Event, "date")
    descriptor = None
    for klass in Calender_Event.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)

def test_calender_event_has_description():
    assert hasattr(Calender_Event, "description")
    descriptor = None
    for klass in Calender_Event.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_calender_event_has_admin():
    assert hasattr(Calender_Event, "admin")
    descriptor = None
    for klass in Calender_Event.__mro__:
        if "admin" in klass.__dict__:
            descriptor = klass.__dict__["admin"]
            break
    assert isinstance(descriptor, property)

def test_calender_event_has_volunteer():
    assert hasattr(Calender_Event, "volunteer")
    descriptor = None
    for klass in Calender_Event.__mro__:
        if "volunteer" in klass.__dict__:
            descriptor = klass.__dict__["volunteer"]
            break
    assert isinstance(descriptor, property)

def test_calender_event_has_eventType():
    assert hasattr(Calender_Event, "eventType")
    descriptor = None
    for klass in Calender_Event.__mro__:
        if "eventType" in klass.__dict__:
            descriptor = klass.__dict__["eventType"]
            break
    assert isinstance(descriptor, property)



def test_volunteer_is_not_abstract():
    assert not inspect.isabstract(Volunteer)


def test_volunteer_constructor_exists():
    assert callable(Volunteer.__init__)


def test_volunteer_constructor_args():
    sig = inspect.signature(Volunteer.__init__)
    params = list(sig.parameters.keys())
    assert "userName" in params, "Missing parameter 'userName'"
    assert "userID" in params, "Missing parameter 'userID'"
    assert "password" in params, "Missing parameter 'password'"

def test_volunteer_has_userName():
    assert hasattr(Volunteer, "userName")
    descriptor = None
    for klass in Volunteer.__mro__:
        if "userName" in klass.__dict__:
            descriptor = klass.__dict__["userName"]
            break
    assert isinstance(descriptor, property)

def test_volunteer_has_userID():
    assert hasattr(Volunteer, "userID")
    descriptor = None
    for klass in Volunteer.__mro__:
        if "userID" in klass.__dict__:
            descriptor = klass.__dict__["userID"]
            break
    assert isinstance(descriptor, property)

def test_volunteer_has_password():
    assert hasattr(Volunteer, "password")
    descriptor = None
    for klass in Volunteer.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)



def test_admin_is_not_abstract():
    assert not inspect.isabstract(Admin)


def test_admin_constructor_exists():
    assert callable(Admin.__init__)


def test_admin_constructor_args():
    sig = inspect.signature(Admin.__init__)
    params = list(sig.parameters.keys())
    assert "userName" in params, "Missing parameter 'userName'"
    assert "password" in params, "Missing parameter 'password'"
    assert "userID" in params, "Missing parameter 'userID'"

def test_admin_has_userName():
    assert hasattr(Admin, "userName")
    descriptor = None
    for klass in Admin.__mro__:
        if "userName" in klass.__dict__:
            descriptor = klass.__dict__["userName"]
            break
    assert isinstance(descriptor, property)

def test_admin_has_password():
    assert hasattr(Admin, "password")
    descriptor = None
    for klass in Admin.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)

def test_admin_has_userID():
    assert hasattr(Admin, "userID")
    descriptor = None
    for klass in Admin.__mro__:
        if "userID" in klass.__dict__:
            descriptor = klass.__dict__["userID"]
            break
    assert isinstance(descriptor, property)



def test_normal_user_is_not_abstract():
    assert not inspect.isabstract(Normal_user)


def test_normal_user_constructor_exists():
    assert callable(Normal_user.__init__)


def test_normal_user_constructor_args():
    sig = inspect.signature(Normal_user.__init__)
    params = list(sig.parameters.keys())
    assert "password" in params, "Missing parameter 'password'"
    assert "userID" in params, "Missing parameter 'userID'"
    assert "userName" in params, "Missing parameter 'userName'"

def test_normal_user_has_password():
    assert hasattr(Normal_user, "password")
    descriptor = None
    for klass in Normal_user.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)

def test_normal_user_has_userID():
    assert hasattr(Normal_user, "userID")
    descriptor = None
    for klass in Normal_user.__mro__:
        if "userID" in klass.__dict__:
            descriptor = klass.__dict__["userID"]
            break
    assert isinstance(descriptor, property)

def test_normal_user_has_userName():
    assert hasattr(Normal_user, "userName")
    descriptor = None
    for klass in Normal_user.__mro__:
        if "userName" in klass.__dict__:
            descriptor = klass.__dict__["userName"]
            break
    assert isinstance(descriptor, property)



def test_void_is_not_abstract():
    assert not inspect.isabstract(void)


def test_void_constructor_exists():
    assert callable(void.__init__)


def test_void_constructor_args():
    sig = inspect.signature(void.__init__)
    params = list(sig.parameters.keys())



def test_superadmin_is_not_abstract():
    assert not inspect.isabstract(SuperAdmin)


def test_superadmin_constructor_exists():
    assert callable(SuperAdmin.__init__)


def test_superadmin_constructor_args():
    sig = inspect.signature(SuperAdmin.__init__)
    params = list(sig.parameters.keys())
    assert "userID" in params, "Missing parameter 'userID'"
    assert "password" in params, "Missing parameter 'password'"
    assert "userName" in params, "Missing parameter 'userName'"

def test_superadmin_has_userID():
    assert hasattr(SuperAdmin, "userID")
    descriptor = None
    for klass in SuperAdmin.__mro__:
        if "userID" in klass.__dict__:
            descriptor = klass.__dict__["userID"]
            break
    assert isinstance(descriptor, property)

def test_superadmin_has_password():
    assert hasattr(SuperAdmin, "password")
    descriptor = None
    for klass in SuperAdmin.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)

def test_superadmin_has_userName():
    assert hasattr(SuperAdmin, "userName")
    descriptor = None
    for klass in SuperAdmin.__mro__:
        if "userName" in klass.__dict__:
            descriptor = klass.__dict__["userName"]
            break
    assert isinstance(descriptor, property)



def test_profile_is_not_abstract():
    assert not inspect.isabstract(Profile)


def test_profile_constructor_exists():
    assert callable(Profile.__init__)


def test_profile_constructor_args():
    sig = inspect.signature(Profile.__init__)
    params = list(sig.parameters.keys())
    assert "f_Name" in params, "Missing parameter 'f_Name'"
    assert "user_Name" in params, "Missing parameter 'user_Name'"
    assert "l_Name" in params, "Missing parameter 'l_Name'"
    assert "password" in params, "Missing parameter 'password'"

def test_profile_has_f_Name():
    assert hasattr(Profile, "f_Name")
    descriptor = None
    for klass in Profile.__mro__:
        if "f_Name" in klass.__dict__:
            descriptor = klass.__dict__["f_Name"]
            break
    assert isinstance(descriptor, property)

def test_profile_has_user_Name():
    assert hasattr(Profile, "user_Name")
    descriptor = None
    for klass in Profile.__mro__:
        if "user_Name" in klass.__dict__:
            descriptor = klass.__dict__["user_Name"]
            break
    assert isinstance(descriptor, property)

def test_profile_has_l_Name():
    assert hasattr(Profile, "l_Name")
    descriptor = None
    for klass in Profile.__mro__:
        if "l_Name" in klass.__dict__:
            descriptor = klass.__dict__["l_Name"]
            break
    assert isinstance(descriptor, property)

def test_profile_has_password():
    assert hasattr(Profile, "password")
    descriptor = None
    for klass in Profile.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
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
Mail_strategy = st.builds(
    Mail,
    sendTo=
        safe_text,
    subject=
        safe_text,
    emailID=
        safe_text,
    sendBy=
        safe_text
)
Payment_strategy = st.builds(
    Payment,
    amount=
        st.integers(),
    cardType=
        safe_text,
    cardNumber=
        st.integers(),
    expiryDate=
        safe_text,
    issuerName=
        safe_text
)
Logout_strategy = st.builds(
    Logout,
)
Attendance_strategy = st.builds(
    Attendance,
    checkInTime=
        safe_text,
    attendanceID=
        st.integers(),
    checkOutTime=
        safe_text
)
Login_strategy = st.builds(
    Login,
    loggedinTime=
        safe_text,
    loggedoutTime=
        safe_text,
    userID=
        st.none()
)
Calender_Event_strategy = st.builds(
    Calender_Event,
    time=
        safe_text,
    participantAmount=
        safe_text,
    category=
        safe_text,
    nomarlUser=
        st.none(),
    date=
        safe_text,
    description=
        safe_text,
    admin=
        st.none(),
    volunteer=
        st.none(),
    eventType=
        safe_text
)
Volunteer_strategy = st.builds(
    Volunteer,
    userName=
        safe_text,
    userID=
        st.integers(),
    password=
        safe_text
)
Admin_strategy = st.builds(
    Admin,
    userName=
        safe_text,
    password=
        safe_text,
    userID=
        st.integers()
)
Normal_user_strategy = st.builds(
    Normal_user,
    password=
        safe_text,
    userID=
        st.integers(),
    userName=
        safe_text
)
void_strategy = st.builds(
    void,
)
SuperAdmin_strategy = st.builds(
    SuperAdmin,
    userID=
        st.integers(),
    password=
        safe_text,
    userName=
        safe_text
)
Profile_strategy = st.builds(
    Profile,
    f_Name=
        safe_text,
    user_Name=
        safe_text,
    l_Name=
        safe_text,
    password=
        safe_text
)

@given(instance=Mail_strategy)
@settings(max_examples=50)
def test_mail_instantiation(instance):
    assert isinstance(instance, Mail)



@given(instance=Mail_strategy)
def test_mail_sendTo_setter(instance):
    original = instance.sendTo
    instance.sendTo = original
    assert instance.sendTo == original



@given(instance=Mail_strategy)
def test_mail_subject_setter(instance):
    original = instance.subject
    instance.subject = original
    assert instance.subject == original



@given(instance=Mail_strategy)
def test_mail_emailID_setter(instance):
    original = instance.emailID
    instance.emailID = original
    assert instance.emailID == original



@given(instance=Mail_strategy)
def test_mail_sendBy_setter(instance):
    original = instance.sendBy
    instance.sendBy = original
    assert instance.sendBy == original

@given(instance=Payment_strategy)
@settings(max_examples=50)
def test_payment_instantiation(instance):
    assert isinstance(instance, Payment)



@given(instance=Payment_strategy)
def test_payment_amount_setter(instance):
    original = instance.amount
    instance.amount = original
    assert instance.amount == original



@given(instance=Payment_strategy)
def test_payment_cardType_setter(instance):
    original = instance.cardType
    instance.cardType = original
    assert instance.cardType == original



@given(instance=Payment_strategy)
def test_payment_cardNumber_setter(instance):
    original = instance.cardNumber
    instance.cardNumber = original
    assert instance.cardNumber == original



@given(instance=Payment_strategy)
def test_payment_expiryDate_setter(instance):
    original = instance.expiryDate
    instance.expiryDate = original
    assert instance.expiryDate == original



@given(instance=Payment_strategy)
def test_payment_issuerName_setter(instance):
    original = instance.issuerName
    instance.issuerName = original
    assert instance.issuerName == original

@given(instance=Logout_strategy)
@settings(max_examples=50)
def test_logout_instantiation(instance):
    assert isinstance(instance, Logout)

@given(instance=Attendance_strategy)
@settings(max_examples=50)
def test_attendance_instantiation(instance):
    assert isinstance(instance, Attendance)



@given(instance=Attendance_strategy)
def test_attendance_checkInTime_setter(instance):
    original = instance.checkInTime
    instance.checkInTime = original
    assert instance.checkInTime == original



@given(instance=Attendance_strategy)
def test_attendance_attendanceID_setter(instance):
    original = instance.attendanceID
    instance.attendanceID = original
    assert instance.attendanceID == original



@given(instance=Attendance_strategy)
def test_attendance_checkOutTime_setter(instance):
    original = instance.checkOutTime
    instance.checkOutTime = original
    assert instance.checkOutTime == original

@given(instance=Login_strategy)
@settings(max_examples=50)
def test_login_instantiation(instance):
    assert isinstance(instance, Login)



@given(instance=Login_strategy)
def test_login_loggedinTime_setter(instance):
    original = instance.loggedinTime
    instance.loggedinTime = original
    assert instance.loggedinTime == original



@given(instance=Login_strategy)
def test_login_loggedoutTime_setter(instance):
    original = instance.loggedoutTime
    instance.loggedoutTime = original
    assert instance.loggedoutTime == original



@given(instance=Login_strategy)
def test_login_userID_setter(instance):
    original = instance.userID
    instance.userID = original
    assert instance.userID == original

@given(instance=Calender_Event_strategy)
@settings(max_examples=50)
def test_calender_event_instantiation(instance):
    assert isinstance(instance, Calender_Event)



@given(instance=Calender_Event_strategy)
def test_calender_event_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original



@given(instance=Calender_Event_strategy)
def test_calender_event_participantAmount_setter(instance):
    original = instance.participantAmount
    instance.participantAmount = original
    assert instance.participantAmount == original



@given(instance=Calender_Event_strategy)
def test_calender_event_category_setter(instance):
    original = instance.category
    instance.category = original
    assert instance.category == original



@given(instance=Calender_Event_strategy)
def test_calender_event_nomarlUser_setter(instance):
    original = instance.nomarlUser
    instance.nomarlUser = original
    assert instance.nomarlUser == original



@given(instance=Calender_Event_strategy)
def test_calender_event_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original



@given(instance=Calender_Event_strategy)
def test_calender_event_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=Calender_Event_strategy)
def test_calender_event_admin_setter(instance):
    original = instance.admin
    instance.admin = original
    assert instance.admin == original



@given(instance=Calender_Event_strategy)
def test_calender_event_volunteer_setter(instance):
    original = instance.volunteer
    instance.volunteer = original
    assert instance.volunteer == original



@given(instance=Calender_Event_strategy)
def test_calender_event_eventType_setter(instance):
    original = instance.eventType
    instance.eventType = original
    assert instance.eventType == original

@given(instance=Volunteer_strategy)
@settings(max_examples=50)
def test_volunteer_instantiation(instance):
    assert isinstance(instance, Volunteer)



@given(instance=Volunteer_strategy)
def test_volunteer_userName_setter(instance):
    original = instance.userName
    instance.userName = original
    assert instance.userName == original



@given(instance=Volunteer_strategy)
def test_volunteer_userID_setter(instance):
    original = instance.userID
    instance.userID = original
    assert instance.userID == original



@given(instance=Volunteer_strategy)
def test_volunteer_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original

@given(instance=Admin_strategy)
@settings(max_examples=50)
def test_admin_instantiation(instance):
    assert isinstance(instance, Admin)



@given(instance=Admin_strategy)
def test_admin_userName_setter(instance):
    original = instance.userName
    instance.userName = original
    assert instance.userName == original



@given(instance=Admin_strategy)
def test_admin_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=Admin_strategy)
def test_admin_userID_setter(instance):
    original = instance.userID
    instance.userID = original
    assert instance.userID == original

@given(instance=Normal_user_strategy)
@settings(max_examples=50)
def test_normal_user_instantiation(instance):
    assert isinstance(instance, Normal_user)



@given(instance=Normal_user_strategy)
def test_normal_user_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=Normal_user_strategy)
def test_normal_user_userID_setter(instance):
    original = instance.userID
    instance.userID = original
    assert instance.userID == original



@given(instance=Normal_user_strategy)
def test_normal_user_userName_setter(instance):
    original = instance.userName
    instance.userName = original
    assert instance.userName == original

@given(instance=void_strategy)
@settings(max_examples=50)
def test_void_instantiation(instance):
    assert isinstance(instance, void)

@given(instance=SuperAdmin_strategy)
@settings(max_examples=50)
def test_superadmin_instantiation(instance):
    assert isinstance(instance, SuperAdmin)



@given(instance=SuperAdmin_strategy)
def test_superadmin_userID_setter(instance):
    original = instance.userID
    instance.userID = original
    assert instance.userID == original



@given(instance=SuperAdmin_strategy)
def test_superadmin_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=SuperAdmin_strategy)
def test_superadmin_userName_setter(instance):
    original = instance.userName
    instance.userName = original
    assert instance.userName == original

@given(instance=Profile_strategy)
@settings(max_examples=50)
def test_profile_instantiation(instance):
    assert isinstance(instance, Profile)



@given(instance=Profile_strategy)
def test_profile_f_Name_setter(instance):
    original = instance.f_Name
    instance.f_Name = original
    assert instance.f_Name == original



@given(instance=Profile_strategy)
def test_profile_user_Name_setter(instance):
    original = instance.user_Name
    instance.user_Name = original
    assert instance.user_Name == original



@given(instance=Profile_strategy)
def test_profile_l_Name_setter(instance):
    original = instance.l_Name
    instance.l_Name = original
    assert instance.l_Name == original



@given(instance=Profile_strategy)
def test_profile_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original
