import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Volunteer_Forms,
    Mail,
    Donations,
    Logout,
    Attendance,
    System_Login,
    Calender_Event,
    Volunteer,
    Admin,
    Normal_user,
    void,
    Executive_Director,
    Profile,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_volunteer_forms_is_not_abstract():
    assert not inspect.isabstract(Volunteer_Forms)


def test_volunteer_forms_constructor_exists():
    assert callable(Volunteer_Forms.__init__)


def test_volunteer_forms_constructor_args():
    sig = inspect.signature(Volunteer_Forms.__init__)
    params = list(sig.parameters.keys())
    assert "userID" in params, "Missing parameter 'userID'"
    assert "password" in params, "Missing parameter 'password'"
    assert "userName" in params, "Missing parameter 'userName'"

def test_volunteer_forms_has_userID():
    assert hasattr(Volunteer_Forms, "userID")
    descriptor = None
    for klass in Volunteer_Forms.__mro__:
        if "userID" in klass.__dict__:
            descriptor = klass.__dict__["userID"]
            break
    assert isinstance(descriptor, property)

def test_volunteer_forms_has_password():
    assert hasattr(Volunteer_Forms, "password")
    descriptor = None
    for klass in Volunteer_Forms.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)

def test_volunteer_forms_has_userName():
    assert hasattr(Volunteer_Forms, "userName")
    descriptor = None
    for klass in Volunteer_Forms.__mro__:
        if "userName" in klass.__dict__:
            descriptor = klass.__dict__["userName"]
            break
    assert isinstance(descriptor, property)



def test_mail_is_not_abstract():
    assert not inspect.isabstract(Mail)


def test_mail_constructor_exists():
    assert callable(Mail.__init__)


def test_mail_constructor_args():
    sig = inspect.signature(Mail.__init__)
    params = list(sig.parameters.keys())
    assert "sendBy" in params, "Missing parameter 'sendBy'"
    assert "emailID" in params, "Missing parameter 'emailID'"
    assert "sendTo" in params, "Missing parameter 'sendTo'"
    assert "subject" in params, "Missing parameter 'subject'"

def test_mail_has_sendBy():
    assert hasattr(Mail, "sendBy")
    descriptor = None
    for klass in Mail.__mro__:
        if "sendBy" in klass.__dict__:
            descriptor = klass.__dict__["sendBy"]
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



def test_donations_is_not_abstract():
    assert not inspect.isabstract(Donations)


def test_donations_constructor_exists():
    assert callable(Donations.__init__)


def test_donations_constructor_args():
    sig = inspect.signature(Donations.__init__)
    params = list(sig.parameters.keys())
    assert "amount" in params, "Missing parameter 'amount'"
    assert "cardNumber" in params, "Missing parameter 'cardNumber'"
    assert "cardType" in params, "Missing parameter 'cardType'"
    assert "issuerName" in params, "Missing parameter 'issuerName'"
    assert "expirationDate" in params, "Missing parameter 'expirationDate'"

def test_donations_has_amount():
    assert hasattr(Donations, "amount")
    descriptor = None
    for klass in Donations.__mro__:
        if "amount" in klass.__dict__:
            descriptor = klass.__dict__["amount"]
            break
    assert isinstance(descriptor, property)

def test_donations_has_cardNumber():
    assert hasattr(Donations, "cardNumber")
    descriptor = None
    for klass in Donations.__mro__:
        if "cardNumber" in klass.__dict__:
            descriptor = klass.__dict__["cardNumber"]
            break
    assert isinstance(descriptor, property)

def test_donations_has_cardType():
    assert hasattr(Donations, "cardType")
    descriptor = None
    for klass in Donations.__mro__:
        if "cardType" in klass.__dict__:
            descriptor = klass.__dict__["cardType"]
            break
    assert isinstance(descriptor, property)

def test_donations_has_issuerName():
    assert hasattr(Donations, "issuerName")
    descriptor = None
    for klass in Donations.__mro__:
        if "issuerName" in klass.__dict__:
            descriptor = klass.__dict__["issuerName"]
            break
    assert isinstance(descriptor, property)

def test_donations_has_expirationDate():
    assert hasattr(Donations, "expirationDate")
    descriptor = None
    for klass in Donations.__mro__:
        if "expirationDate" in klass.__dict__:
            descriptor = klass.__dict__["expirationDate"]
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



def test_system_login_is_not_abstract():
    assert not inspect.isabstract(System_Login)


def test_system_login_constructor_exists():
    assert callable(System_Login.__init__)


def test_system_login_constructor_args():
    sig = inspect.signature(System_Login.__init__)
    params = list(sig.parameters.keys())
    assert "loggedinTime" in params, "Missing parameter 'loggedinTime'"
    assert "loggedoutTime" in params, "Missing parameter 'loggedoutTime'"
    assert "userID" in params, "Missing parameter 'userID'"

def test_system_login_has_loggedinTime():
    assert hasattr(System_Login, "loggedinTime")
    descriptor = None
    for klass in System_Login.__mro__:
        if "loggedinTime" in klass.__dict__:
            descriptor = klass.__dict__["loggedinTime"]
            break
    assert isinstance(descriptor, property)

def test_system_login_has_loggedoutTime():
    assert hasattr(System_Login, "loggedoutTime")
    descriptor = None
    for klass in System_Login.__mro__:
        if "loggedoutTime" in klass.__dict__:
            descriptor = klass.__dict__["loggedoutTime"]
            break
    assert isinstance(descriptor, property)

def test_system_login_has_userID():
    assert hasattr(System_Login, "userID")
    descriptor = None
    for klass in System_Login.__mro__:
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
    assert "admin" in params, "Missing parameter 'admin'"
    assert "nomarlUser" in params, "Missing parameter 'nomarlUser'"
    assert "participantAmount" in params, "Missing parameter 'participantAmount'"
    assert "date" in params, "Missing parameter 'date'"
    assert "category" in params, "Missing parameter 'category'"
    assert "volunteer" in params, "Missing parameter 'volunteer'"
    assert "description" in params, "Missing parameter 'description'"
    assert "eventType" in params, "Missing parameter 'eventType'"

def test_calender_event_has_time():
    assert hasattr(Calender_Event, "time")
    descriptor = None
    for klass in Calender_Event.__mro__:
        if "time" in klass.__dict__:
            descriptor = klass.__dict__["time"]
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

def test_calender_event_has_nomarlUser():
    assert hasattr(Calender_Event, "nomarlUser")
    descriptor = None
    for klass in Calender_Event.__mro__:
        if "nomarlUser" in klass.__dict__:
            descriptor = klass.__dict__["nomarlUser"]
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

def test_calender_event_has_date():
    assert hasattr(Calender_Event, "date")
    descriptor = None
    for klass in Calender_Event.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
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

def test_calender_event_has_volunteer():
    assert hasattr(Calender_Event, "volunteer")
    descriptor = None
    for klass in Calender_Event.__mro__:
        if "volunteer" in klass.__dict__:
            descriptor = klass.__dict__["volunteer"]
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
    assert "userID" in params, "Missing parameter 'userID'"
    assert "password" in params, "Missing parameter 'password'"
    assert "userName" in params, "Missing parameter 'userName'"

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

def test_volunteer_has_userName():
    assert hasattr(Volunteer, "userName")
    descriptor = None
    for klass in Volunteer.__mro__:
        if "userName" in klass.__dict__:
            descriptor = klass.__dict__["userName"]
            break
    assert isinstance(descriptor, property)



def test_admin_is_not_abstract():
    assert not inspect.isabstract(Admin)


def test_admin_constructor_exists():
    assert callable(Admin.__init__)


def test_admin_constructor_args():
    sig = inspect.signature(Admin.__init__)
    params = list(sig.parameters.keys())
    assert "password" in params, "Missing parameter 'password'"
    assert "userID" in params, "Missing parameter 'userID'"
    assert "userName" in params, "Missing parameter 'userName'"

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

def test_admin_has_userName():
    assert hasattr(Admin, "userName")
    descriptor = None
    for klass in Admin.__mro__:
        if "userName" in klass.__dict__:
            descriptor = klass.__dict__["userName"]
            break
    assert isinstance(descriptor, property)



def test_normal_user_is_not_abstract():
    assert not inspect.isabstract(Normal_user)


def test_normal_user_constructor_exists():
    assert callable(Normal_user.__init__)


def test_normal_user_constructor_args():
    sig = inspect.signature(Normal_user.__init__)
    params = list(sig.parameters.keys())
    assert "userName" in params, "Missing parameter 'userName'"
    assert "password" in params, "Missing parameter 'password'"
    assert "userID" in params, "Missing parameter 'userID'"

def test_normal_user_has_userName():
    assert hasattr(Normal_user, "userName")
    descriptor = None
    for klass in Normal_user.__mro__:
        if "userName" in klass.__dict__:
            descriptor = klass.__dict__["userName"]
            break
    assert isinstance(descriptor, property)

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



def test_void_is_not_abstract():
    assert not inspect.isabstract(void)


def test_void_constructor_exists():
    assert callable(void.__init__)


def test_void_constructor_args():
    sig = inspect.signature(void.__init__)
    params = list(sig.parameters.keys())



def test_executive_director_is_not_abstract():
    assert not inspect.isabstract(Executive_Director)


def test_executive_director_constructor_exists():
    assert callable(Executive_Director.__init__)


def test_executive_director_constructor_args():
    sig = inspect.signature(Executive_Director.__init__)
    params = list(sig.parameters.keys())
    assert "password" in params, "Missing parameter 'password'"
    assert "userName" in params, "Missing parameter 'userName'"
    assert "userID" in params, "Missing parameter 'userID'"

def test_executive_director_has_password():
    assert hasattr(Executive_Director, "password")
    descriptor = None
    for klass in Executive_Director.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)

def test_executive_director_has_userName():
    assert hasattr(Executive_Director, "userName")
    descriptor = None
    for klass in Executive_Director.__mro__:
        if "userName" in klass.__dict__:
            descriptor = klass.__dict__["userName"]
            break
    assert isinstance(descriptor, property)

def test_executive_director_has_userID():
    assert hasattr(Executive_Director, "userID")
    descriptor = None
    for klass in Executive_Director.__mro__:
        if "userID" in klass.__dict__:
            descriptor = klass.__dict__["userID"]
            break
    assert isinstance(descriptor, property)



def test_profile_is_not_abstract():
    assert not inspect.isabstract(Profile)


def test_profile_constructor_exists():
    assert callable(Profile.__init__)


def test_profile_constructor_args():
    sig = inspect.signature(Profile.__init__)
    params = list(sig.parameters.keys())
    assert "phone_Number" in params, "Missing parameter 'phone_Number'"
    assert "last_Name" in params, "Missing parameter 'last_Name'"
    assert "first_Name" in params, "Missing parameter 'first_Name'"
    assert "user_Name" in params, "Missing parameter 'user_Name'"
    assert "password" in params, "Missing parameter 'password'"

def test_profile_has_phone_Number():
    assert hasattr(Profile, "phone_Number")
    descriptor = None
    for klass in Profile.__mro__:
        if "phone_Number" in klass.__dict__:
            descriptor = klass.__dict__["phone_Number"]
            break
    assert isinstance(descriptor, property)

def test_profile_has_last_Name():
    assert hasattr(Profile, "last_Name")
    descriptor = None
    for klass in Profile.__mro__:
        if "last_Name" in klass.__dict__:
            descriptor = klass.__dict__["last_Name"]
            break
    assert isinstance(descriptor, property)

def test_profile_has_first_Name():
    assert hasattr(Profile, "first_Name")
    descriptor = None
    for klass in Profile.__mro__:
        if "first_Name" in klass.__dict__:
            descriptor = klass.__dict__["first_Name"]
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
Volunteer_Forms_strategy = st.builds(
    Volunteer_Forms,
    userID=
        st.integers(),
    password=
        safe_text,
    userName=
        safe_text
)
Mail_strategy = st.builds(
    Mail,
    sendBy=
        safe_text,
    emailID=
        safe_text,
    sendTo=
        safe_text,
    subject=
        safe_text
)
Donations_strategy = st.builds(
    Donations,
    amount=
        st.integers(),
    cardNumber=
        st.integers(),
    cardType=
        safe_text,
    issuerName=
        safe_text,
    expirationDate=
        st.integers()
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
System_Login_strategy = st.builds(
    System_Login,
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
    admin=
        st.none(),
    nomarlUser=
        st.none(),
    participantAmount=
        safe_text,
    date=
        safe_text,
    category=
        safe_text,
    volunteer=
        st.none(),
    description=
        safe_text,
    eventType=
        safe_text
)
Volunteer_strategy = st.builds(
    Volunteer,
    userID=
        st.integers(),
    password=
        safe_text,
    userName=
        safe_text
)
Admin_strategy = st.builds(
    Admin,
    password=
        safe_text,
    userID=
        st.integers(),
    userName=
        safe_text
)
Normal_user_strategy = st.builds(
    Normal_user,
    userName=
        safe_text,
    password=
        safe_text,
    userID=
        st.integers()
)
void_strategy = st.builds(
    void,
)
Executive_Director_strategy = st.builds(
    Executive_Director,
    password=
        safe_text,
    userName=
        safe_text,
    userID=
        st.integers()
)
Profile_strategy = st.builds(
    Profile,
    phone_Number=
        st.integers(),
    last_Name=
        safe_text,
    first_Name=
        safe_text,
    user_Name=
        safe_text,
    password=
        safe_text
)

@given(instance=Volunteer_Forms_strategy)
@settings(max_examples=50)
def test_volunteer_forms_instantiation(instance):
    assert isinstance(instance, Volunteer_Forms)



@given(instance=Volunteer_Forms_strategy)
def test_volunteer_forms_userID_setter(instance):
    original = instance.userID
    instance.userID = original
    assert instance.userID == original



@given(instance=Volunteer_Forms_strategy)
def test_volunteer_forms_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=Volunteer_Forms_strategy)
def test_volunteer_forms_userName_setter(instance):
    original = instance.userName
    instance.userName = original
    assert instance.userName == original

@given(instance=Mail_strategy)
@settings(max_examples=50)
def test_mail_instantiation(instance):
    assert isinstance(instance, Mail)



@given(instance=Mail_strategy)
def test_mail_sendBy_setter(instance):
    original = instance.sendBy
    instance.sendBy = original
    assert instance.sendBy == original



@given(instance=Mail_strategy)
def test_mail_emailID_setter(instance):
    original = instance.emailID
    instance.emailID = original
    assert instance.emailID == original



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

@given(instance=Donations_strategy)
@settings(max_examples=50)
def test_donations_instantiation(instance):
    assert isinstance(instance, Donations)



@given(instance=Donations_strategy)
def test_donations_amount_setter(instance):
    original = instance.amount
    instance.amount = original
    assert instance.amount == original



@given(instance=Donations_strategy)
def test_donations_cardNumber_setter(instance):
    original = instance.cardNumber
    instance.cardNumber = original
    assert instance.cardNumber == original



@given(instance=Donations_strategy)
def test_donations_cardType_setter(instance):
    original = instance.cardType
    instance.cardType = original
    assert instance.cardType == original



@given(instance=Donations_strategy)
def test_donations_issuerName_setter(instance):
    original = instance.issuerName
    instance.issuerName = original
    assert instance.issuerName == original



@given(instance=Donations_strategy)
def test_donations_expirationDate_setter(instance):
    original = instance.expirationDate
    instance.expirationDate = original
    assert instance.expirationDate == original

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

@given(instance=System_Login_strategy)
@settings(max_examples=50)
def test_system_login_instantiation(instance):
    assert isinstance(instance, System_Login)



@given(instance=System_Login_strategy)
def test_system_login_loggedinTime_setter(instance):
    original = instance.loggedinTime
    instance.loggedinTime = original
    assert instance.loggedinTime == original



@given(instance=System_Login_strategy)
def test_system_login_loggedoutTime_setter(instance):
    original = instance.loggedoutTime
    instance.loggedoutTime = original
    assert instance.loggedoutTime == original



@given(instance=System_Login_strategy)
def test_system_login_userID_setter(instance):
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
def test_calender_event_admin_setter(instance):
    original = instance.admin
    instance.admin = original
    assert instance.admin == original



@given(instance=Calender_Event_strategy)
def test_calender_event_nomarlUser_setter(instance):
    original = instance.nomarlUser
    instance.nomarlUser = original
    assert instance.nomarlUser == original



@given(instance=Calender_Event_strategy)
def test_calender_event_participantAmount_setter(instance):
    original = instance.participantAmount
    instance.participantAmount = original
    assert instance.participantAmount == original



@given(instance=Calender_Event_strategy)
def test_calender_event_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original



@given(instance=Calender_Event_strategy)
def test_calender_event_category_setter(instance):
    original = instance.category
    instance.category = original
    assert instance.category == original



@given(instance=Calender_Event_strategy)
def test_calender_event_volunteer_setter(instance):
    original = instance.volunteer
    instance.volunteer = original
    assert instance.volunteer == original



@given(instance=Calender_Event_strategy)
def test_calender_event_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



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
def test_volunteer_userID_setter(instance):
    original = instance.userID
    instance.userID = original
    assert instance.userID == original



@given(instance=Volunteer_strategy)
def test_volunteer_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=Volunteer_strategy)
def test_volunteer_userName_setter(instance):
    original = instance.userName
    instance.userName = original
    assert instance.userName == original

@given(instance=Admin_strategy)
@settings(max_examples=50)
def test_admin_instantiation(instance):
    assert isinstance(instance, Admin)



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



@given(instance=Admin_strategy)
def test_admin_userName_setter(instance):
    original = instance.userName
    instance.userName = original
    assert instance.userName == original

@given(instance=Normal_user_strategy)
@settings(max_examples=50)
def test_normal_user_instantiation(instance):
    assert isinstance(instance, Normal_user)



@given(instance=Normal_user_strategy)
def test_normal_user_userName_setter(instance):
    original = instance.userName
    instance.userName = original
    assert instance.userName == original



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

@given(instance=void_strategy)
@settings(max_examples=50)
def test_void_instantiation(instance):
    assert isinstance(instance, void)

@given(instance=Executive_Director_strategy)
@settings(max_examples=50)
def test_executive_director_instantiation(instance):
    assert isinstance(instance, Executive_Director)



@given(instance=Executive_Director_strategy)
def test_executive_director_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=Executive_Director_strategy)
def test_executive_director_userName_setter(instance):
    original = instance.userName
    instance.userName = original
    assert instance.userName == original



@given(instance=Executive_Director_strategy)
def test_executive_director_userID_setter(instance):
    original = instance.userID
    instance.userID = original
    assert instance.userID == original

@given(instance=Profile_strategy)
@settings(max_examples=50)
def test_profile_instantiation(instance):
    assert isinstance(instance, Profile)



@given(instance=Profile_strategy)
def test_profile_phone_Number_setter(instance):
    original = instance.phone_Number
    instance.phone_Number = original
    assert instance.phone_Number == original



@given(instance=Profile_strategy)
def test_profile_last_Name_setter(instance):
    original = instance.last_Name
    instance.last_Name = original
    assert instance.last_Name == original



@given(instance=Profile_strategy)
def test_profile_first_Name_setter(instance):
    original = instance.first_Name
    instance.first_Name = original
    assert instance.first_Name == original



@given(instance=Profile_strategy)
def test_profile_user_Name_setter(instance):
    original = instance.user_Name
    instance.user_Name = original
    assert instance.user_Name == original



@given(instance=Profile_strategy)
def test_profile_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original
