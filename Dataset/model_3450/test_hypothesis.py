import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    MembershipInfo,
    org::sgiusa::model::EStringToStringMapEntry,
    org::sgiusa::model::DocumentRoot,
    GohonzonInfo,
    FamilyMember,
    EmailList,
    org::aries::common::User,
    org::aries::common::ZipCode,
    org::aries::common::StreetAddress,
    org::aries::common::PhoneNumber,
    org::aries::common::Property,
    org::aries::common::Properties,
    org::aries::common::Person,
    org::aries::common::PersonName,
    org::sgiusa::model::View,
    org::sgiusa::model::Users,
    org::sgiusa::model::StudyDeptInfo,
    org::sgiusa::model::User,
    org::sgiusa::model::StudyDeptExam,
    org::sgiusa::model::Registration,
    org::sgiusa::model::SchoolInfo,
    org::sgiusa::model::Preferences,
    org::sgiusa::model::Permission,
    org::sgiusa::model::Organization,
    org::sgiusa::model::MembershipInfo,
    org::sgiusa::model::Note,
    org::sgiusa::model::Members,
    org::sgiusa::model::MemberSearchCriteria,
    org::sgiusa::model::Member,
    org::sgiusa::model::LeadershipInfo,
    org::sgiusa::model::LeadershipRole,
    org::sgiusa::model::GohonzonInfo,
    org::sgiusa::model::FamilyMember,
    org::sgiusa::model::Event,
    StudyDeptInfo,
    StudyDeptExam,
    SchoolInfo,
    Registration,
    org::sgiusa::model::EmailList,
    View,
    Users,
    MemberSearchCriteria,
    Members,
    Member,
    LeadershipRole,
    LeadershipInfo,
    Preferences,
    Permission,
    Organization,
    org::aries::common::EObject,
    org::aries::common::MapEntry,
    org::aries::common::Map,
    org::aries::common::Note,
    org::aries::common::Event,
    org::aries::common::EmailMessage,
    org::aries::common::EmailBox,
    org::aries::common::EmailAddressList,
    org::aries::common::EmailAddress,
    org::aries::common::EmailAccount,
    ZipCode,
    User,
    StreetAddress,
    PersonName,
    Person,
    Note,
    MapEntry,
    Property,
    Properties,
    PhoneNumber,
    EmailMessage,
    EmailBox,
    EmailAddressList,
    EmailAddress,
    Map,
    Event,
    org::aries::common::EStringToStringMapEntry,
    org::aries::common::DocumentRoot,
    EmailAccount,
    Attachment,
    org::aries::common::Attachment,
    SubDivision,
    Role,
    Position,
    OrganizationLevel,
    SchoolType,
    ViewType,
    PhoneNumberType,
    FamilyRelation,
    DivisionName,
    Capability,
    Language,
    ActivityGroupName,
    Country,
    EventStatus,
    SubDivisionName,
    State,
    Status,
    StudyDeptExamLevel,
    StudyDeptLanguage,
    PositionName,
    RoleType,
    GohonzonType,
    ActivityGroup,
    Division,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_membershipinfo_is_not_abstract():
    assert not inspect.isabstract(MembershipInfo)


def test_membershipinfo_constructor_exists():
    assert callable(MembershipInfo.__init__)


def test_membershipinfo_constructor_args():
    sig = inspect.signature(MembershipInfo.__init__)
    params = list(sig.parameters.keys())



def test_org::sgiusa::model::estringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(org::sgiusa::model::EStringToStringMapEntry)


def test_org::sgiusa::model::estringtostringmapentry_constructor_exists():
    assert callable(org::sgiusa::model::EStringToStringMapEntry.__init__)


def test_org::sgiusa::model::estringtostringmapentry_constructor_args():
    sig = inspect.signature(org::sgiusa::model::EStringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())



def test_org::sgiusa::model::documentroot_is_not_abstract():
    assert not inspect.isabstract(org::sgiusa::model::DocumentRoot)


def test_org::sgiusa::model::documentroot_constructor_exists():
    assert callable(org::sgiusa::model::DocumentRoot.__init__)


def test_org::sgiusa::model::documentroot_constructor_args():
    sig = inspect.signature(org::sgiusa::model::DocumentRoot.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_org::sgiusa::model::documentroot_has_mixed():
    assert hasattr(org::sgiusa::model::DocumentRoot, "mixed")
    descriptor = None
    for klass in org::sgiusa::model::DocumentRoot.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_gohonzoninfo_is_not_abstract():
    assert not inspect.isabstract(GohonzonInfo)


def test_gohonzoninfo_constructor_exists():
    assert callable(GohonzonInfo.__init__)


def test_gohonzoninfo_constructor_args():
    sig = inspect.signature(GohonzonInfo.__init__)
    params = list(sig.parameters.keys())



def test_familymember_is_not_abstract():
    assert not inspect.isabstract(FamilyMember)


def test_familymember_constructor_exists():
    assert callable(FamilyMember.__init__)


def test_familymember_constructor_args():
    sig = inspect.signature(FamilyMember.__init__)
    params = list(sig.parameters.keys())



def test_emaillist_is_not_abstract():
    assert not inspect.isabstract(EmailList)


def test_emaillist_constructor_exists():
    assert callable(EmailList.__init__)


def test_emaillist_constructor_args():
    sig = inspect.signature(EmailList.__init__)
    params = list(sig.parameters.keys())



def test_org::aries::common::user_is_not_abstract():
    assert not inspect.isabstract(org::aries::common::User)


def test_org::aries::common::user_constructor_exists():
    assert callable(org::aries::common::User.__init__)


def test_org::aries::common::user_constructor_args():
    sig = inspect.signature(org::aries::common::User.__init__)
    params = list(sig.parameters.keys())
    assert "lastName" in params, "Missing parameter 'lastName'"
    assert "password" in params, "Missing parameter 'password'"
    assert "firstName" in params, "Missing parameter 'firstName'"
    assert "id" in params, "Missing parameter 'id'"
    assert "enabled" in params, "Missing parameter 'enabled'"
    assert "userId" in params, "Missing parameter 'userId'"

def test_org::aries::common::user_has_lastName():
    assert hasattr(org::aries::common::User, "lastName")
    descriptor = None
    for klass in org::aries::common::User.__mro__:
        if "lastName" in klass.__dict__:
            descriptor = klass.__dict__["lastName"]
            break
    assert isinstance(descriptor, property)

def test_org::aries::common::user_has_password():
    assert hasattr(org::aries::common::User, "password")
    descriptor = None
    for klass in org::aries::common::User.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)

def test_org::aries::common::user_has_firstName():
    assert hasattr(org::aries::common::User, "firstName")
    descriptor = None
    for klass in org::aries::common::User.__mro__:
        if "firstName" in klass.__dict__:
            descriptor = klass.__dict__["firstName"]
            break
    assert isinstance(descriptor, property)

def test_org::aries::common::user_has_id():
    assert hasattr(org::aries::common::User, "id")
    descriptor = None
    for klass in org::aries::common::User.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_org::aries::common::user_has_enabled():
    assert hasattr(org::aries::common::User, "enabled")
    descriptor = None
    for klass in org::aries::common::User.__mro__:
        if "enabled" in klass.__dict__:
            descriptor = klass.__dict__["enabled"]
            break
    assert isinstance(descriptor, property)

def test_org::aries::common::user_has_userId():
    assert hasattr(org::aries::common::User, "userId")
    descriptor = None
    for klass in org::aries::common::User.__mro__:
        if "userId" in klass.__dict__:
            descriptor = klass.__dict__["userId"]
            break
    assert isinstance(descriptor, property)



def test_org::aries::common::zipcode_is_not_abstract():
    assert not inspect.isabstract(org::aries::common::ZipCode)


def test_org::aries::common::zipcode_constructor_exists():
    assert callable(org::aries::common::ZipCode.__init__)


def test_org::aries::common::zipcode_constructor_args():
    sig = inspect.signature(org::aries::common::ZipCode.__init__)
    params = list(sig.parameters.keys())
    assert "extension" in params, "Missing parameter 'extension'"
    assert "number" in params, "Missing parameter 'number'"
    assert "country" in params, "Missing parameter 'country'"

def test_org::aries::common::zipcode_has_extension():
    assert hasattr(org::aries::common::ZipCode, "extension")
    descriptor = None
    for klass in org::aries::common::ZipCode.__mro__:
        if "extension" in klass.__dict__:
            descriptor = klass.__dict__["extension"]
            break
    assert isinstance(descriptor, property)

def test_org::aries::common::zipcode_has_number():
    assert hasattr(org::aries::common::ZipCode, "number")
    descriptor = None
    for klass in org::aries::common::ZipCode.__mro__:
        if "number" in klass.__dict__:
            descriptor = klass.__dict__["number"]
            break
    assert isinstance(descriptor, property)

def test_org::aries::common::zipcode_has_country():
    assert hasattr(org::aries::common::ZipCode, "country")
    descriptor = None
    for klass in org::aries::common::ZipCode.__mro__:
        if "country" in klass.__dict__:
            descriptor = klass.__dict__["country"]
            break
    assert isinstance(descriptor, property)



def test_org::aries::common::streetaddress_is_not_abstract():
    assert not inspect.isabstract(org::aries::common::StreetAddress)


def test_org::aries::common::streetaddress_constructor_exists():
    assert callable(org::aries::common::StreetAddress.__init__)


def test_org::aries::common::streetaddress_constructor_args():
    sig = inspect.signature(org::aries::common::StreetAddress.__init__)
    params = list(sig.parameters.keys())
    assert "latitude" in params, "Missing parameter 'latitude'"
    assert "street" in params, "Missing parameter 'street'"
    assert "longitude" in params, "Missing parameter 'longitude'"
    assert "id" in params, "Missing parameter 'id'"
    assert "country" in params, "Missing parameter 'country'"
    assert "city" in params, "Missing parameter 'city'"
    assert "state" in params, "Missing parameter 'state'"

def test_org::aries::common::streetaddress_has_latitude():
    assert hasattr(org::aries::common::StreetAddress, "latitude")
    descriptor = None
    for klass in org::aries::common::StreetAddress.__mro__:
        if "latitude" in klass.__dict__:
            descriptor = klass.__dict__["latitude"]
            break
    assert isinstance(descriptor, property)

def test_org::aries::common::streetaddress_has_street():
    assert hasattr(org::aries::common::StreetAddress, "street")
    descriptor = None
    for klass in org::aries::common::StreetAddress.__mro__:
        if "street" in klass.__dict__:
            descriptor = klass.__dict__["street"]
            break
    assert isinstance(descriptor, property)

def test_org::aries::common::streetaddress_has_longitude():
    assert hasattr(org::aries::common::StreetAddress, "longitude")
    descriptor = None
    for klass in org::aries::common::StreetAddress.__mro__:
        if "longitude" in klass.__dict__:
            descriptor = klass.__dict__["longitude"]
            break
    assert isinstance(descriptor, property)

def test_org::aries::common::streetaddress_has_id():
    assert hasattr(org::aries::common::StreetAddress, "id")
    descriptor = None
    for klass in org::aries::common::StreetAddress.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_org::aries::common::streetaddress_has_country():
    assert hasattr(org::aries::common::StreetAddress, "country")
    descriptor = None
    for klass in org::aries::common::StreetAddress.__mro__:
        if "country" in klass.__dict__:
            descriptor = klass.__dict__["country"]
            break
    assert isinstance(descriptor, property)

def test_org::aries::common::streetaddress_has_city():
    assert hasattr(org::aries::common::StreetAddress, "city")
    descriptor = None
    for klass in org::aries::common::StreetAddress.__mro__:
        if "city" in klass.__dict__:
            descriptor = klass.__dict__["city"]
            break
    assert isinstance(descriptor, property)

def test_org::aries::common::streetaddress_has_state():
    assert hasattr(org::aries::common::StreetAddress, "state")
    descriptor = None
    for klass in org::aries::common::StreetAddress.__mro__:
        if "state" in klass.__dict__:
            descriptor = klass.__dict__["state"]
            break
    assert isinstance(descriptor, property)



def test_org::aries::common::phonenumber_is_not_abstract():
    assert not inspect.isabstract(org::aries::common::PhoneNumber)


def test_org::aries::common::phonenumber_constructor_exists():
    assert callable(org::aries::common::PhoneNumber.__init__)


def test_org::aries::common::phonenumber_constructor_args():
    sig = inspect.signature(org::aries::common::PhoneNumber.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "value" in params, "Missing parameter 'value'"
    assert "number" in params, "Missing parameter 'number'"
    assert "type" in params, "Missing parameter 'type'"
    assert "area" in params, "Missing parameter 'area'"
    assert "extension" in params, "Missing parameter 'extension'"
    assert "country" in params, "Missing parameter 'country'"

def test_org::aries::common::phonenumber_has_id():
    assert hasattr(org::aries::common::PhoneNumber, "id")
    descriptor = None
    for klass in org::aries::common::PhoneNumber.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_org::aries::common::phonenumber_has_value():
    assert hasattr(org::aries::common::PhoneNumber, "value")
    descriptor = None
    for klass in org::aries::common::PhoneNumber.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_org::aries::common::phonenumber_has_number():
    assert hasattr(org::aries::common::PhoneNumber, "number")
    descriptor = None
    for klass in org::aries::common::PhoneNumber.__mro__:
        if "number" in klass.__dict__:
            descriptor = klass.__dict__["number"]
            break
    assert isinstance(descriptor, property)

def test_org::aries::common::phonenumber_has_type():
    assert hasattr(org::aries::common::PhoneNumber, "type")
    descriptor = None
    for klass in org::aries::common::PhoneNumber.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_org::aries::common::phonenumber_has_area():
    assert hasattr(org::aries::common::PhoneNumber, "area")
    descriptor = None
    for klass in org::aries::common::PhoneNumber.__mro__:
        if "area" in klass.__dict__:
            descriptor = klass.__dict__["area"]
            break
    assert isinstance(descriptor, property)

def test_org::aries::common::phonenumber_has_extension():
    assert hasattr(org::aries::common::PhoneNumber, "extension")
    descriptor = None
    for klass in org::aries::common::PhoneNumber.__mro__:
        if "extension" in klass.__dict__:
            descriptor = klass.__dict__["extension"]
            break
    assert isinstance(descriptor, property)

def test_org::aries::common::phonenumber_has_country():
    assert hasattr(org::aries::common::PhoneNumber, "country")
    descriptor = None
    for klass in org::aries::common::PhoneNumber.__mro__:
        if "country" in klass.__dict__:
            descriptor = klass.__dict__["country"]
            break
    assert isinstance(descriptor, property)



def test_org::aries::common::property_is_not_abstract():
    assert not inspect.isabstract(org::aries::common::Property)


def test_org::aries::common::property_constructor_exists():
    assert callable(org::aries::common::Property.__init__)


def test_org::aries::common::property_constructor_args():
    sig = inspect.signature(org::aries::common::Property.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_org::aries::common::property_has_id():
    assert hasattr(org::aries::common::Property, "id")
    descriptor = None
    for klass in org::aries::common::Property.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_org::aries::common::property_has_mixed():
    assert hasattr(org::aries::common::Property, "mixed")
    descriptor = None
    for klass in org::aries::common::Property.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_org::aries::common::property_has_value():
    assert hasattr(org::aries::common::Property, "value")
    descriptor = None
    for klass in org::aries::common::Property.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_org::aries::common::property_has_name():
    assert hasattr(org::aries::common::Property, "name")
    descriptor = None
    for klass in org::aries::common::Property.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_org::aries::common::properties_is_not_abstract():
    assert not inspect.isabstract(org::aries::common::Properties)


def test_org::aries::common::properties_constructor_exists():
    assert callable(org::aries::common::Properties.__init__)


def test_org::aries::common::properties_constructor_args():
    sig = inspect.signature(org::aries::common::Properties.__init__)
    params = list(sig.parameters.keys())



def test_org::aries::common::person_is_not_abstract():
    assert not inspect.isabstract(org::aries::common::Person)


def test_org::aries::common::person_constructor_exists():
    assert callable(org::aries::common::Person.__init__)


def test_org::aries::common::person_constructor_args():
    sig = inspect.signature(org::aries::common::Person.__init__)
    params = list(sig.parameters.keys())
    assert "userId" in params, "Missing parameter 'userId'"
    assert "id" in params, "Missing parameter 'id'"

def test_org::aries::common::person_has_userId():
    assert hasattr(org::aries::common::Person, "userId")
    descriptor = None
    for klass in org::aries::common::Person.__mro__:
        if "userId" in klass.__dict__:
            descriptor = klass.__dict__["userId"]
            break
    assert isinstance(descriptor, property)

def test_org::aries::common::person_has_id():
    assert hasattr(org::aries::common::Person, "id")
    descriptor = None
    for klass in org::aries::common::Person.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_org::aries::common::personname_is_not_abstract():
    assert not inspect.isabstract(org::aries::common::PersonName)


def test_org::aries::common::personname_constructor_exists():
    assert callable(org::aries::common::PersonName.__init__)


def test_org::aries::common::personname_constructor_args():
    sig = inspect.signature(org::aries::common::PersonName.__init__)
    params = list(sig.parameters.keys())
    assert "firstName" in params, "Missing parameter 'firstName'"
    assert "middleInitial" in params, "Missing parameter 'middleInitial'"
    assert "lastName" in params, "Missing parameter 'lastName'"

def test_org::aries::common::personname_has_firstName():
    assert hasattr(org::aries::common::PersonName, "firstName")
    descriptor = None
    for klass in org::aries::common::PersonName.__mro__:
        if "firstName" in klass.__dict__:
            descriptor = klass.__dict__["firstName"]
            break
    assert isinstance(descriptor, property)

def test_org::aries::common::personname_has_middleInitial():
    assert hasattr(org::aries::common::PersonName, "middleInitial")
    descriptor = None
    for klass in org::aries::common::PersonName.__mro__:
        if "middleInitial" in klass.__dict__:
            descriptor = klass.__dict__["middleInitial"]
            break
    assert isinstance(descriptor, property)

def test_org::aries::common::personname_has_lastName():
    assert hasattr(org::aries::common::PersonName, "lastName")
    descriptor = None
    for klass in org::aries::common::PersonName.__mro__:
        if "lastName" in klass.__dict__:
            descriptor = klass.__dict__["lastName"]
            break
    assert isinstance(descriptor, property)



def test_org::sgiusa::model::view_is_not_abstract():
    assert not inspect.isabstract(org::sgiusa::model::View)


def test_org::sgiusa::model::view_constructor_exists():
    assert callable(org::sgiusa::model::View.__init__)


def test_org::sgiusa::model::view_constructor_args():
    sig = inspect.signature(org::sgiusa::model::View.__init__)
    params = list(sig.parameters.keys())
    assert "viewType" in params, "Missing parameter 'viewType'"
    assert "userId" in params, "Missing parameter 'userId'"
    assert "id" in params, "Missing parameter 'id'"

def test_org::sgiusa::model::view_has_viewType():
    assert hasattr(org::sgiusa::model::View, "viewType")
    descriptor = None
    for klass in org::sgiusa::model::View.__mro__:
        if "viewType" in klass.__dict__:
            descriptor = klass.__dict__["viewType"]
            break
    assert isinstance(descriptor, property)

def test_org::sgiusa::model::view_has_userId():
    assert hasattr(org::sgiusa::model::View, "userId")
    descriptor = None
    for klass in org::sgiusa::model::View.__mro__:
        if "userId" in klass.__dict__:
            descriptor = klass.__dict__["userId"]
            break
    assert isinstance(descriptor, property)

def test_org::sgiusa::model::view_has_id():
    assert hasattr(org::sgiusa::model::View, "id")
    descriptor = None
    for klass in org::sgiusa::model::View.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_org::sgiusa::model::users_is_not_abstract():
    assert not inspect.isabstract(org::sgiusa::model::Users)


def test_org::sgiusa::model::users_constructor_exists():
    assert callable(org::sgiusa::model::Users.__init__)


def test_org::sgiusa::model::users_constructor_args():
    sig = inspect.signature(org::sgiusa::model::Users.__init__)
    params = list(sig.parameters.keys())



def test_org::sgiusa::model::studydeptinfo_is_not_abstract():
    assert not inspect.isabstract(org::sgiusa::model::StudyDeptInfo)


def test_org::sgiusa::model::studydeptinfo_constructor_exists():
    assert callable(org::sgiusa::model::StudyDeptInfo.__init__)


def test_org::sgiusa::model::studydeptinfo_constructor_args():
    sig = inspect.signature(org::sgiusa::model::StudyDeptInfo.__init__)
    params = list(sig.parameters.keys())
    assert "lastUpdate" in params, "Missing parameter 'lastUpdate'"
    assert "id" in params, "Missing parameter 'id'"

def test_org::sgiusa::model::studydeptinfo_has_lastUpdate():
    assert hasattr(org::sgiusa::model::StudyDeptInfo, "lastUpdate")
    descriptor = None
    for klass in org::sgiusa::model::StudyDeptInfo.__mro__:
        if "lastUpdate" in klass.__dict__:
            descriptor = klass.__dict__["lastUpdate"]
            break
    assert isinstance(descriptor, property)

def test_org::sgiusa::model::studydeptinfo_has_id():
    assert hasattr(org::sgiusa::model::StudyDeptInfo, "id")
    descriptor = None
    for klass in org::sgiusa::model::StudyDeptInfo.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_org::sgiusa::model::user_is_not_abstract():
    assert not inspect.isabstract(org::sgiusa::model::User)


def test_org::sgiusa::model::user_constructor_exists():
    assert callable(org::sgiusa::model::User.__init__)


def test_org::sgiusa::model::user_constructor_args():
    sig = inspect.signature(org::sgiusa::model::User.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "enabled" in params, "Missing parameter 'enabled'"
    assert "userId" in params, "Missing parameter 'userId'"
    assert "lastName" in params, "Missing parameter 'lastName'"
    assert "role" in params, "Missing parameter 'role'"
    assert "password" in params, "Missing parameter 'password'"
    assert "firstName" in params, "Missing parameter 'firstName'"

def test_org::sgiusa::model::user_has_id():
    assert hasattr(org::sgiusa::model::User, "id")
    descriptor = None
    for klass in org::sgiusa::model::User.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_org::sgiusa::model::user_has_enabled():
    assert hasattr(org::sgiusa::model::User, "enabled")
    descriptor = None
    for klass in org::sgiusa::model::User.__mro__:
        if "enabled" in klass.__dict__:
            descriptor = klass.__dict__["enabled"]
            break
    assert isinstance(descriptor, property)

def test_org::sgiusa::model::user_has_userId():
    assert hasattr(org::sgiusa::model::User, "userId")
    descriptor = None
    for klass in org::sgiusa::model::User.__mro__:
        if "userId" in klass.__dict__:
            descriptor = klass.__dict__["userId"]
            break
    assert isinstance(descriptor, property)

def test_org::sgiusa::model::user_has_lastName():
    assert hasattr(org::sgiusa::model::User, "lastName")
    descriptor = None
    for klass in org::sgiusa::model::User.__mro__:
        if "lastName" in klass.__dict__:
            descriptor = klass.__dict__["lastName"]
            break
    assert isinstance(descriptor, property)

def test_org::sgiusa::model::user_has_role():
    assert hasattr(org::sgiusa::model::User, "role")
    descriptor = None
    for klass in org::sgiusa::model::User.__mro__:
        if "role" in klass.__dict__:
            descriptor = klass.__dict__["role"]
            break
    assert isinstance(descriptor, property)

def test_org::sgiusa::model::user_has_password():
    assert hasattr(org::sgiusa::model::User, "password")
    descriptor = None
    for klass in org::sgiusa::model::User.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)

def test_org::sgiusa::model::user_has_firstName():
    assert hasattr(org::sgiusa::model::User, "firstName")
    descriptor = None
    for klass in org::sgiusa::model::User.__mro__:
        if "firstName" in klass.__dict__:
            descriptor = klass.__dict__["firstName"]
            break
    assert isinstance(descriptor, property)



def test_org::sgiusa::model::studydeptexam_is_not_abstract():
    assert not inspect.isabstract(org::sgiusa::model::StudyDeptExam)


def test_org::sgiusa::model::studydeptexam_constructor_exists():
    assert callable(org::sgiusa::model::StudyDeptExam.__init__)


def test_org::sgiusa::model::studydeptexam_constructor_args():
    sig = inspect.signature(org::sgiusa::model::StudyDeptExam.__init__)
    params = list(sig.parameters.keys())
    assert "examLevel" in params, "Missing parameter 'examLevel'"
    assert "current" in params, "Missing parameter 'current'"
    assert "examDate" in params, "Missing parameter 'examDate'"
    assert "examLanguage" in params, "Missing parameter 'examLanguage'"
    assert "lastUpdate" in params, "Missing parameter 'lastUpdate'"
    assert "examLocation" in params, "Missing parameter 'examLocation'"
    assert "id" in params, "Missing parameter 'id'"

def test_org::sgiusa::model::studydeptexam_has_examLevel():
    assert hasattr(org::sgiusa::model::StudyDeptExam, "examLevel")
    descriptor = None
    for klass in org::sgiusa::model::StudyDeptExam.__mro__:
        if "examLevel" in klass.__dict__:
            descriptor = klass.__dict__["examLevel"]
            break
    assert isinstance(descriptor, property)

def test_org::sgiusa::model::studydeptexam_has_current():
    assert hasattr(org::sgiusa::model::StudyDeptExam, "current")
    descriptor = None
    for klass in org::sgiusa::model::StudyDeptExam.__mro__:
        if "current" in klass.__dict__:
            descriptor = klass.__dict__["current"]
            break
    assert isinstance(descriptor, property)

def test_org::sgiusa::model::studydeptexam_has_examDate():
    assert hasattr(org::sgiusa::model::StudyDeptExam, "examDate")
    descriptor = None
    for klass in org::sgiusa::model::StudyDeptExam.__mro__:
        if "examDate" in klass.__dict__:
            descriptor = klass.__dict__["examDate"]
            break
    assert isinstance(descriptor, property)

def test_org::sgiusa::model::studydeptexam_has_examLanguage():
    assert hasattr(org::sgiusa::model::StudyDeptExam, "examLanguage")
    descriptor = None
    for klass in org::sgiusa::model::StudyDeptExam.__mro__:
        if "examLanguage" in klass.__dict__:
            descriptor = klass.__dict__["examLanguage"]
            break
    assert isinstance(descriptor, property)

def test_org::sgiusa::model::studydeptexam_has_lastUpdate():
    assert hasattr(org::sgiusa::model::StudyDeptExam, "lastUpdate")
    descriptor = None
    for klass in org::sgiusa::model::StudyDeptExam.__mro__:
        if "lastUpdate" in klass.__dict__:
            descriptor = klass.__dict__["lastUpdate"]
            break
    assert isinstance(descriptor, property)

def test_org::sgiusa::model::studydeptexam_has_examLocation():
    assert hasattr(org::sgiusa::model::StudyDeptExam, "examLocation")
    descriptor = None
    for klass in org::sgiusa::model::StudyDeptExam.__mro__:
        if "examLocation" in klass.__dict__:
            descriptor = klass.__dict__["examLocation"]
            break
    assert isinstance(descriptor, property)

def test_org::sgiusa::model::studydeptexam_has_id():
    assert hasattr(org::sgiusa::model::StudyDeptExam, "id")
    descriptor = None
    for klass in org::sgiusa::model::StudyDeptExam.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_org::sgiusa::model::registration_is_not_abstract():
    assert not inspect.isabstract(org::sgiusa::model::Registration)


def test_org::sgiusa::model::registration_constructor_exists():
    assert callable(org::sgiusa::model::Registration.__init__)


def test_org::sgiusa::model::registration_constructor_args():
    sig = inspect.signature(org::sgiusa::model::Registration.__init__)
    params = list(sig.parameters.keys())
    assert "cancelled" in params, "Missing parameter 'cancelled'"
    assert "aborted" in params, "Missing parameter 'aborted'"
    assert "date" in params, "Missing parameter 'date'"
    assert "id" in params, "Missing parameter 'id'"

def test_org::sgiusa::model::registration_has_cancelled():
    assert hasattr(org::sgiusa::model::Registration, "cancelled")
    descriptor = None
    for klass in org::sgiusa::model::Registration.__mro__:
        if "cancelled" in klass.__dict__:
            descriptor = klass.__dict__["cancelled"]
            break
    assert isinstance(descriptor, property)

def test_org::sgiusa::model::registration_has_aborted():
    assert hasattr(org::sgiusa::model::Registration, "aborted")
    descriptor = None
    for klass in org::sgiusa::model::Registration.__mro__:
        if "aborted" in klass.__dict__:
            descriptor = klass.__dict__["aborted"]
            break
    assert isinstance(descriptor, property)

def test_org::sgiusa::model::registration_has_date():
    assert hasattr(org::sgiusa::model::Registration, "date")
    descriptor = None
    for klass in org::sgiusa::model::Registration.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)

def test_org::sgiusa::model::registration_has_id():
    assert hasattr(org::sgiusa::model::Registration, "id")
    descriptor = None
    for klass in org::sgiusa::model::Registration.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_org::sgiusa::model::schoolinfo_is_not_abstract():
    assert not inspect.isabstract(org::sgiusa::model::SchoolInfo)


def test_org::sgiusa::model::schoolinfo_constructor_exists():
    assert callable(org::sgiusa::model::SchoolInfo.__init__)


def test_org::sgiusa::model::schoolinfo_constructor_args():
    sig = inspect.signature(org::sgiusa::model::SchoolInfo.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "fieldOfStudy" in params, "Missing parameter 'fieldOfStudy'"
    assert "endDate" in params, "Missing parameter 'endDate'"
    assert "schoolName" in params, "Missing parameter 'schoolName'"
    assert "lastUpdate" in params, "Missing parameter 'lastUpdate'"
    assert "startDate" in params, "Missing parameter 'startDate'"
    assert "schoolType" in params, "Missing parameter 'schoolType'"

def test_org::sgiusa::model::schoolinfo_has_id():
    assert hasattr(org::sgiusa::model::SchoolInfo, "id")
    descriptor = None
    for klass in org::sgiusa::model::SchoolInfo.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_org::sgiusa::model::schoolinfo_has_fieldOfStudy():
    assert hasattr(org::sgiusa::model::SchoolInfo, "fieldOfStudy")
    descriptor = None
    for klass in org::sgiusa::model::SchoolInfo.__mro__:
        if "fieldOfStudy" in klass.__dict__:
            descriptor = klass.__dict__["fieldOfStudy"]
            break
    assert isinstance(descriptor, property)

def test_org::sgiusa::model::schoolinfo_has_endDate():
    assert hasattr(org::sgiusa::model::SchoolInfo, "endDate")
    descriptor = None
    for klass in org::sgiusa::model::SchoolInfo.__mro__:
        if "endDate" in klass.__dict__:
            descriptor = klass.__dict__["endDate"]
            break
    assert isinstance(descriptor, property)

def test_org::sgiusa::model::schoolinfo_has_schoolName():
    assert hasattr(org::sgiusa::model::SchoolInfo, "schoolName")
    descriptor = None
    for klass in org::sgiusa::model::SchoolInfo.__mro__:
        if "schoolName" in klass.__dict__:
            descriptor = klass.__dict__["schoolName"]
            break
    assert isinstance(descriptor, property)

def test_org::sgiusa::model::schoolinfo_has_lastUpdate():
    assert hasattr(org::sgiusa::model::SchoolInfo, "lastUpdate")
    descriptor = None
    for klass in org::sgiusa::model::SchoolInfo.__mro__:
        if "lastUpdate" in klass.__dict__:
            descriptor = klass.__dict__["lastUpdate"]
            break
    assert isinstance(descriptor, property)

def test_org::sgiusa::model::schoolinfo_has_startDate():
    assert hasattr(org::sgiusa::model::SchoolInfo, "startDate")
    descriptor = None
    for klass in org::sgiusa::model::SchoolInfo.__mro__:
        if "startDate" in klass.__dict__:
            descriptor = klass.__dict__["startDate"]
            break
    assert isinstance(descriptor, property)

def test_org::sgiusa::model::schoolinfo_has_schoolType():
    assert hasattr(org::sgiusa::model::SchoolInfo, "schoolType")
    descriptor = None
    for klass in org::sgiusa::model::SchoolInfo.__mro__:
        if "schoolType" in klass.__dict__:
            descriptor = klass.__dict__["schoolType"]
            break
    assert isinstance(descriptor, property)



def test_org::sgiusa::model::preferences_is_not_abstract():
    assert not inspect.isabstract(org::sgiusa::model::Preferences)


def test_org::sgiusa::model::preferences_constructor_exists():
    assert callable(org::sgiusa::model::Preferences.__init__)


def test_org::sgiusa::model::preferences_constructor_args():
    sig = inspect.signature(org::sgiusa::model::Preferences.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "themeId" in params, "Missing parameter 'themeId'"
    assert "enableTooltips" in params, "Missing parameter 'enableTooltips'"
    assert "selectedView" in params, "Missing parameter 'selectedView'"
    assert "openNodes" in params, "Missing parameter 'openNodes'"
    assert "userId" in params, "Missing parameter 'userId'"
    assert "openViews" in params, "Missing parameter 'openViews'"
    assert "selectedNode" in params, "Missing parameter 'selectedNode'"

def test_org::sgiusa::model::preferences_has_id():
    assert hasattr(org::sgiusa::model::Preferences, "id")
    descriptor = None
    for klass in org::sgiusa::model::Preferences.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_org::sgiusa::model::preferences_has_themeId():
    assert hasattr(org::sgiusa::model::Preferences, "themeId")
    descriptor = None
    for klass in org::sgiusa::model::Preferences.__mro__:
        if "themeId" in klass.__dict__:
            descriptor = klass.__dict__["themeId"]
            break
    assert isinstance(descriptor, property)

def test_org::sgiusa::model::preferences_has_enableTooltips():
    assert hasattr(org::sgiusa::model::Preferences, "enableTooltips")
    descriptor = None
    for klass in org::sgiusa::model::Preferences.__mro__:
        if "enableTooltips" in klass.__dict__:
            descriptor = klass.__dict__["enableTooltips"]
            break
    assert isinstance(descriptor, property)

def test_org::sgiusa::model::preferences_has_selectedView():
    assert hasattr(org::sgiusa::model::Preferences, "selectedView")
    descriptor = None
    for klass in org::sgiusa::model::Preferences.__mro__:
        if "selectedView" in klass.__dict__:
            descriptor = klass.__dict__["selectedView"]
            break
    assert isinstance(descriptor, property)

def test_org::sgiusa::model::preferences_has_openNodes():
    assert hasattr(org::sgiusa::model::Preferences, "openNodes")
    descriptor = None
    for klass in org::sgiusa::model::Preferences.__mro__:
        if "openNodes" in klass.__dict__:
            descriptor = klass.__dict__["openNodes"]
            break
    assert isinstance(descriptor, property)

def test_org::sgiusa::model::preferences_has_userId():
    assert hasattr(org::sgiusa::model::Preferences, "userId")
    descriptor = None
    for klass in org::sgiusa::model::Preferences.__mro__:
        if "userId" in klass.__dict__:
            descriptor = klass.__dict__["userId"]
            break
    assert isinstance(descriptor, property)

def test_org::sgiusa::model::preferences_has_openViews():
    assert hasattr(org::sgiusa::model::Preferences, "openViews")
    descriptor = None
    for klass in org::sgiusa::model::Preferences.__mro__:
        if "openViews" in klass.__dict__:
            descriptor = klass.__dict__["openViews"]
            break
    assert isinstance(descriptor, property)

def test_org::sgiusa::model::preferences_has_selectedNode():
    assert hasattr(org::sgiusa::model::Preferences, "selectedNode")
    descriptor = None
    for klass in org::sgiusa::model::Preferences.__mro__:
        if "selectedNode" in klass.__dict__:
            descriptor = klass.__dict__["selectedNode"]
            break
    assert isinstance(descriptor, property)



def test_org::sgiusa::model::permission_is_not_abstract():
    assert not inspect.isabstract(org::sgiusa::model::Permission)


def test_org::sgiusa::model::permission_constructor_exists():
    assert callable(org::sgiusa::model::Permission.__init__)


def test_org::sgiusa::model::permission_constructor_args():
    sig = inspect.signature(org::sgiusa::model::Permission.__init__)
    params = list(sig.parameters.keys())
    assert "capabilities" in params, "Missing parameter 'capabilities'"
    assert "activityGroups" in params, "Missing parameter 'activityGroups'"
    assert "userId" in params, "Missing parameter 'userId'"
    assert "enabled" in params, "Missing parameter 'enabled'"
    assert "divisions" in params, "Missing parameter 'divisions'"
    assert "subDivisions" in params, "Missing parameter 'subDivisions'"
    assert "id" in params, "Missing parameter 'id'"

def test_org::sgiusa::model::permission_has_capabilities():
    assert hasattr(org::sgiusa::model::Permission, "capabilities")
    descriptor = None
    for klass in org::sgiusa::model::Permission.__mro__:
        if "capabilities" in klass.__dict__:
            descriptor = klass.__dict__["capabilities"]
            break
    assert isinstance(descriptor, property)

def test_org::sgiusa::model::permission_has_activityGroups():
    assert hasattr(org::sgiusa::model::Permission, "activityGroups")
    descriptor = None
    for klass in org::sgiusa::model::Permission.__mro__:
        if "activityGroups" in klass.__dict__:
            descriptor = klass.__dict__["activityGroups"]
            break
    assert isinstance(descriptor, property)

def test_org::sgiusa::model::permission_has_userId():
    assert hasattr(org::sgiusa::model::Permission, "userId")
    descriptor = None
    for klass in org::sgiusa::model::Permission.__mro__:
        if "userId" in klass.__dict__:
            descriptor = klass.__dict__["userId"]
            break
    assert isinstance(descriptor, property)

def test_org::sgiusa::model::permission_has_enabled():
    assert hasattr(org::sgiusa::model::Permission, "enabled")
    descriptor = None
    for klass in org::sgiusa::model::Permission.__mro__:
        if "enabled" in klass.__dict__:
            descriptor = klass.__dict__["enabled"]
            break
    assert isinstance(descriptor, property)

def test_org::sgiusa::model::permission_has_divisions():
    assert hasattr(org::sgiusa::model::Permission, "divisions")
    descriptor = None
    for klass in org::sgiusa::model::Permission.__mro__:
        if "divisions" in klass.__dict__:
            descriptor = klass.__dict__["divisions"]
            break
    assert isinstance(descriptor, property)

def test_org::sgiusa::model::permission_has_subDivisions():
    assert hasattr(org::sgiusa::model::Permission, "subDivisions")
    descriptor = None
    for klass in org::sgiusa::model::Permission.__mro__:
        if "subDivisions" in klass.__dict__:
            descriptor = klass.__dict__["subDivisions"]
            break
    assert isinstance(descriptor, property)

def test_org::sgiusa::model::permission_has_id():
    assert hasattr(org::sgiusa::model::Permission, "id")
    descriptor = None
    for klass in org::sgiusa::model::Permission.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_org::sgiusa::model::organization_is_not_abstract():
    assert not inspect.isabstract(org::sgiusa::model::Organization)


def test_org::sgiusa::model::organization_constructor_exists():
    assert callable(org::sgiusa::model::Organization.__init__)


def test_org::sgiusa::model::organization_constructor_args():
    sig = inspect.signature(org::sgiusa::model::Organization.__init__)
    params = list(sig.parameters.keys())
    assert "level" in params, "Missing parameter 'level'"
    assert "permissionId" in params, "Missing parameter 'permissionId'"
    assert "abbrv" in params, "Missing parameter 'abbrv'"
    assert "lastUpdate" in params, "Missing parameter 'lastUpdate'"
    assert "id" in params, "Missing parameter 'id'"
    assert "organizationId" in params, "Missing parameter 'organizationId'"
    assert "creationDate" in params, "Missing parameter 'creationDate'"
    assert "zipCodes" in params, "Missing parameter 'zipCodes'"
    assert "type" in params, "Missing parameter 'type'"
    assert "label" in params, "Missing parameter 'label'"
    assert "name" in params, "Missing parameter 'name'"

def test_org::sgiusa::model::organization_has_level():
    assert hasattr(org::sgiusa::model::Organization, "level")
    descriptor = None
    for klass in org::sgiusa::model::Organization.__mro__:
        if "level" in klass.__dict__:
            descriptor = klass.__dict__["level"]
            break
    assert isinstance(descriptor, property)

def test_org::sgiusa::model::organization_has_permissionId():
    assert hasattr(org::sgiusa::model::Organization, "permissionId")
    descriptor = None
    for klass in org::sgiusa::model::Organization.__mro__:
        if "permissionId" in klass.__dict__:
            descriptor = klass.__dict__["permissionId"]
            break
    assert isinstance(descriptor, property)

def test_org::sgiusa::model::organization_has_abbrv():
    assert hasattr(org::sgiusa::model::Organization, "abbrv")
    descriptor = None
    for klass in org::sgiusa::model::Organization.__mro__:
        if "abbrv" in klass.__dict__:
            descriptor = klass.__dict__["abbrv"]
            break
    assert isinstance(descriptor, property)

def test_org::sgiusa::model::organization_has_lastUpdate():
    assert hasattr(org::sgiusa::model::Organization, "lastUpdate")
    descriptor = None
    for klass in org::sgiusa::model::Organization.__mro__:
        if "lastUpdate" in klass.__dict__:
            descriptor = klass.__dict__["lastUpdate"]
            break
    assert isinstance(descriptor, property)

def test_org::sgiusa::model::organization_has_id():
    assert hasattr(org::sgiusa::model::Organization, "id")
    descriptor = None
    for klass in org::sgiusa::model::Organization.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_org::sgiusa::model::organization_has_organizationId():
    assert hasattr(org::sgiusa::model::Organization, "organizationId")
    descriptor = None
    for klass in org::sgiusa::model::Organization.__mro__:
        if "organizationId" in klass.__dict__:
            descriptor = klass.__dict__["organizationId"]
            break
    assert isinstance(descriptor, property)

def test_org::sgiusa::model::organization_has_creationDate():
    assert hasattr(org::sgiusa::model::Organization, "creationDate")
    descriptor = None
    for klass in org::sgiusa::model::Organization.__mro__:
        if "creationDate" in klass.__dict__:
            descriptor = klass.__dict__["creationDate"]
            break
    assert isinstance(descriptor, property)

def test_org::sgiusa::model::organization_has_zipCodes():
    assert hasattr(org::sgiusa::model::Organization, "zipCodes")
    descriptor = None
    for klass in org::sgiusa::model::Organization.__mro__:
        if "zipCodes" in klass.__dict__:
            descriptor = klass.__dict__["zipCodes"]
            break
    assert isinstance(descriptor, property)

def test_org::sgiusa::model::organization_has_type():
    assert hasattr(org::sgiusa::model::Organization, "type")
    descriptor = None
    for klass in org::sgiusa::model::Organization.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_org::sgiusa::model::organization_has_label():
    assert hasattr(org::sgiusa::model::Organization, "label")
    descriptor = None
    for klass in org::sgiusa::model::Organization.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_org::sgiusa::model::organization_has_name():
    assert hasattr(org::sgiusa::model::Organization, "name")
    descriptor = None
    for klass in org::sgiusa::model::Organization.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_org::sgiusa::model::membershipinfo_is_not_abstract():
    assert not inspect.isabstract(org::sgiusa::model::MembershipInfo)


def test_org::sgiusa::model::membershipinfo_constructor_exists():
    assert callable(org::sgiusa::model::MembershipInfo.__init__)


def test_org::sgiusa::model::membershipinfo_constructor_args():
    sig = inspect.signature(org::sgiusa::model::MembershipInfo.__init__)
    params = list(sig.parameters.keys())
    assert "friendOfSgi" in params, "Missing parameter 'friendOfSgi'"
    assert "notLocatable" in params, "Missing parameter 'notLocatable'"
    assert "id" in params, "Missing parameter 'id'"
    assert "receivedCertificate" in params, "Missing parameter 'receivedCertificate'"
    assert "notActivated" in params, "Missing parameter 'notActivated'"
    assert "lastUpdate" in params, "Missing parameter 'lastUpdate'"

def test_org::sgiusa::model::membershipinfo_has_friendOfSgi():
    assert hasattr(org::sgiusa::model::MembershipInfo, "friendOfSgi")
    descriptor = None
    for klass in org::sgiusa::model::MembershipInfo.__mro__:
        if "friendOfSgi" in klass.__dict__:
            descriptor = klass.__dict__["friendOfSgi"]
            break
    assert isinstance(descriptor, property)

def test_org::sgiusa::model::membershipinfo_has_notLocatable():
    assert hasattr(org::sgiusa::model::MembershipInfo, "notLocatable")
    descriptor = None
    for klass in org::sgiusa::model::MembershipInfo.__mro__:
        if "notLocatable" in klass.__dict__:
            descriptor = klass.__dict__["notLocatable"]
            break
    assert isinstance(descriptor, property)

def test_org::sgiusa::model::membershipinfo_has_id():
    assert hasattr(org::sgiusa::model::MembershipInfo, "id")
    descriptor = None
    for klass in org::sgiusa::model::MembershipInfo.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_org::sgiusa::model::membershipinfo_has_receivedCertificate():
    assert hasattr(org::sgiusa::model::MembershipInfo, "receivedCertificate")
    descriptor = None
    for klass in org::sgiusa::model::MembershipInfo.__mro__:
        if "receivedCertificate" in klass.__dict__:
            descriptor = klass.__dict__["receivedCertificate"]
            break
    assert isinstance(descriptor, property)

def test_org::sgiusa::model::membershipinfo_has_notActivated():
    assert hasattr(org::sgiusa::model::MembershipInfo, "notActivated")
    descriptor = None
    for klass in org::sgiusa::model::MembershipInfo.__mro__:
        if "notActivated" in klass.__dict__:
            descriptor = klass.__dict__["notActivated"]
            break
    assert isinstance(descriptor, property)

def test_org::sgiusa::model::membershipinfo_has_lastUpdate():
    assert hasattr(org::sgiusa::model::MembershipInfo, "lastUpdate")
    descriptor = None
    for klass in org::sgiusa::model::MembershipInfo.__mro__:
        if "lastUpdate" in klass.__dict__:
            descriptor = klass.__dict__["lastUpdate"]
            break
    assert isinstance(descriptor, property)



def test_org::sgiusa::model::note_is_not_abstract():
    assert not inspect.isabstract(org::sgiusa::model::Note)


def test_org::sgiusa::model::note_constructor_exists():
    assert callable(org::sgiusa::model::Note.__init__)


def test_org::sgiusa::model::note_constructor_args():
    sig = inspect.signature(org::sgiusa::model::Note.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "lastUpdate" in params, "Missing parameter 'lastUpdate'"
    assert "text" in params, "Missing parameter 'text'"
    assert "creationDate" in params, "Missing parameter 'creationDate'"

def test_org::sgiusa::model::note_has_id():
    assert hasattr(org::sgiusa::model::Note, "id")
    descriptor = None
    for klass in org::sgiusa::model::Note.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_org::sgiusa::model::note_has_lastUpdate():
    assert hasattr(org::sgiusa::model::Note, "lastUpdate")
    descriptor = None
    for klass in org::sgiusa::model::Note.__mro__:
        if "lastUpdate" in klass.__dict__:
            descriptor = klass.__dict__["lastUpdate"]
            break
    assert isinstance(descriptor, property)

def test_org::sgiusa::model::note_has_text():
    assert hasattr(org::sgiusa::model::Note, "text")
    descriptor = None
    for klass in org::sgiusa::model::Note.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)

def test_org::sgiusa::model::note_has_creationDate():
    assert hasattr(org::sgiusa::model::Note, "creationDate")
    descriptor = None
    for klass in org::sgiusa::model::Note.__mro__:
        if "creationDate" in klass.__dict__:
            descriptor = klass.__dict__["creationDate"]
            break
    assert isinstance(descriptor, property)



def test_org::sgiusa::model::members_is_not_abstract():
    assert not inspect.isabstract(org::sgiusa::model::Members)


def test_org::sgiusa::model::members_constructor_exists():
    assert callable(org::sgiusa::model::Members.__init__)


def test_org::sgiusa::model::members_constructor_args():
    sig = inspect.signature(org::sgiusa::model::Members.__init__)
    params = list(sig.parameters.keys())



def test_org::sgiusa::model::membersearchcriteria_is_not_abstract():
    assert not inspect.isabstract(org::sgiusa::model::MemberSearchCriteria)


def test_org::sgiusa::model::membersearchcriteria_constructor_exists():
    assert callable(org::sgiusa::model::MemberSearchCriteria.__init__)


def test_org::sgiusa::model::membersearchcriteria_constructor_args():
    sig = inspect.signature(org::sgiusa::model::MemberSearchCriteria.__init__)
    params = list(sig.parameters.keys())
    assert "divisions" in params, "Missing parameter 'divisions'"
    assert "activityGroups" in params, "Missing parameter 'activityGroups'"
    assert "subDivisions" in params, "Missing parameter 'subDivisions'"

def test_org::sgiusa::model::membersearchcriteria_has_divisions():
    assert hasattr(org::sgiusa::model::MemberSearchCriteria, "divisions")
    descriptor = None
    for klass in org::sgiusa::model::MemberSearchCriteria.__mro__:
        if "divisions" in klass.__dict__:
            descriptor = klass.__dict__["divisions"]
            break
    assert isinstance(descriptor, property)

def test_org::sgiusa::model::membersearchcriteria_has_activityGroups():
    assert hasattr(org::sgiusa::model::MemberSearchCriteria, "activityGroups")
    descriptor = None
    for klass in org::sgiusa::model::MemberSearchCriteria.__mro__:
        if "activityGroups" in klass.__dict__:
            descriptor = klass.__dict__["activityGroups"]
            break
    assert isinstance(descriptor, property)

def test_org::sgiusa::model::membersearchcriteria_has_subDivisions():
    assert hasattr(org::sgiusa::model::MemberSearchCriteria, "subDivisions")
    descriptor = None
    for klass in org::sgiusa::model::MemberSearchCriteria.__mro__:
        if "subDivisions" in klass.__dict__:
            descriptor = klass.__dict__["subDivisions"]
            break
    assert isinstance(descriptor, property)



def test_org::sgiusa::model::member_is_not_abstract():
    assert not inspect.isabstract(org::sgiusa::model::Member)


def test_org::sgiusa::model::member_constructor_exists():
    assert callable(org::sgiusa::model::Member.__init__)


def test_org::sgiusa::model::member_constructor_args():
    sig = inspect.signature(org::sgiusa::model::Member.__init__)
    params = list(sig.parameters.keys())
    assert "archived" in params, "Missing parameter 'archived'"
    assert "firstName" in params, "Missing parameter 'firstName'"
    assert "extraField2" in params, "Missing parameter 'extraField2'"
    assert "joinDate" in params, "Missing parameter 'joinDate'"
    assert "employer" in params, "Missing parameter 'employer'"
    assert "visible" in params, "Missing parameter 'visible'"
    assert "birthDate" in params, "Missing parameter 'birthDate'"
    assert "statusProfile" in params, "Missing parameter 'statusProfile'"
    assert "extraField1" in params, "Missing parameter 'extraField1'"
    assert "id" in params, "Missing parameter 'id'"
    assert "locatable" in params, "Missing parameter 'locatable'"
    assert "occupation" in params, "Missing parameter 'occupation'"
    assert "lastName" in params, "Missing parameter 'lastName'"
    assert "middleInitial" in params, "Missing parameter 'middleInitial'"
    assert "interests" in params, "Missing parameter 'interests'"
    assert "activityGroups" in params, "Missing parameter 'activityGroups'"
    assert "languages" in params, "Missing parameter 'languages'"
    assert "subDivision" in params, "Missing parameter 'subDivision'"
    assert "division" in params, "Missing parameter 'division'"

def test_org::sgiusa::model::member_has_archived():
    assert hasattr(org::sgiusa::model::Member, "archived")
    descriptor = None
    for klass in org::sgiusa::model::Member.__mro__:
        if "archived" in klass.__dict__:
            descriptor = klass.__dict__["archived"]
            break
    assert isinstance(descriptor, property)

def test_org::sgiusa::model::member_has_firstName():
    assert hasattr(org::sgiusa::model::Member, "firstName")
    descriptor = None
    for klass in org::sgiusa::model::Member.__mro__:
        if "firstName" in klass.__dict__:
            descriptor = klass.__dict__["firstName"]
            break
    assert isinstance(descriptor, property)

def test_org::sgiusa::model::member_has_extraField2():
    assert hasattr(org::sgiusa::model::Member, "extraField2")
    descriptor = None
    for klass in org::sgiusa::model::Member.__mro__:
        if "extraField2" in klass.__dict__:
            descriptor = klass.__dict__["extraField2"]
            break
    assert isinstance(descriptor, property)

def test_org::sgiusa::model::member_has_joinDate():
    assert hasattr(org::sgiusa::model::Member, "joinDate")
    descriptor = None
    for klass in org::sgiusa::model::Member.__mro__:
        if "joinDate" in klass.__dict__:
            descriptor = klass.__dict__["joinDate"]
            break
    assert isinstance(descriptor, property)

def test_org::sgiusa::model::member_has_employer():
    assert hasattr(org::sgiusa::model::Member, "employer")
    descriptor = None
    for klass in org::sgiusa::model::Member.__mro__:
        if "employer" in klass.__dict__:
            descriptor = klass.__dict__["employer"]
            break
    assert isinstance(descriptor, property)

def test_org::sgiusa::model::member_has_visible():
    assert hasattr(org::sgiusa::model::Member, "visible")
    descriptor = None
    for klass in org::sgiusa::model::Member.__mro__:
        if "visible" in klass.__dict__:
            descriptor = klass.__dict__["visible"]
            break
    assert isinstance(descriptor, property)

def test_org::sgiusa::model::member_has_birthDate():
    assert hasattr(org::sgiusa::model::Member, "birthDate")
    descriptor = None
    for klass in org::sgiusa::model::Member.__mro__:
        if "birthDate" in klass.__dict__:
            descriptor = klass.__dict__["birthDate"]
            break
    assert isinstance(descriptor, property)

def test_org::sgiusa::model::member_has_statusProfile():
    assert hasattr(org::sgiusa::model::Member, "statusProfile")
    descriptor = None
    for klass in org::sgiusa::model::Member.__mro__:
        if "statusProfile" in klass.__dict__:
            descriptor = klass.__dict__["statusProfile"]
            break
    assert isinstance(descriptor, property)

def test_org::sgiusa::model::member_has_extraField1():
    assert hasattr(org::sgiusa::model::Member, "extraField1")
    descriptor = None
    for klass in org::sgiusa::model::Member.__mro__:
        if "extraField1" in klass.__dict__:
            descriptor = klass.__dict__["extraField1"]
            break
    assert isinstance(descriptor, property)

def test_org::sgiusa::model::member_has_id():
    assert hasattr(org::sgiusa::model::Member, "id")
    descriptor = None
    for klass in org::sgiusa::model::Member.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_org::sgiusa::model::member_has_locatable():
    assert hasattr(org::sgiusa::model::Member, "locatable")
    descriptor = None
    for klass in org::sgiusa::model::Member.__mro__:
        if "locatable" in klass.__dict__:
            descriptor = klass.__dict__["locatable"]
            break
    assert isinstance(descriptor, property)

def test_org::sgiusa::model::member_has_occupation():
    assert hasattr(org::sgiusa::model::Member, "occupation")
    descriptor = None
    for klass in org::sgiusa::model::Member.__mro__:
        if "occupation" in klass.__dict__:
            descriptor = klass.__dict__["occupation"]
            break
    assert isinstance(descriptor, property)

def test_org::sgiusa::model::member_has_lastName():
    assert hasattr(org::sgiusa::model::Member, "lastName")
    descriptor = None
    for klass in org::sgiusa::model::Member.__mro__:
        if "lastName" in klass.__dict__:
            descriptor = klass.__dict__["lastName"]
            break
    assert isinstance(descriptor, property)

def test_org::sgiusa::model::member_has_middleInitial():
    assert hasattr(org::sgiusa::model::Member, "middleInitial")
    descriptor = None
    for klass in org::sgiusa::model::Member.__mro__:
        if "middleInitial" in klass.__dict__:
            descriptor = klass.__dict__["middleInitial"]
            break
    assert isinstance(descriptor, property)

def test_org::sgiusa::model::member_has_interests():
    assert hasattr(org::sgiusa::model::Member, "interests")
    descriptor = None
    for klass in org::sgiusa::model::Member.__mro__:
        if "interests" in klass.__dict__:
            descriptor = klass.__dict__["interests"]
            break
    assert isinstance(descriptor, property)

def test_org::sgiusa::model::member_has_activityGroups():
    assert hasattr(org::sgiusa::model::Member, "activityGroups")
    descriptor = None
    for klass in org::sgiusa::model::Member.__mro__:
        if "activityGroups" in klass.__dict__:
            descriptor = klass.__dict__["activityGroups"]
            break
    assert isinstance(descriptor, property)

def test_org::sgiusa::model::member_has_languages():
    assert hasattr(org::sgiusa::model::Member, "languages")
    descriptor = None
    for klass in org::sgiusa::model::Member.__mro__:
        if "languages" in klass.__dict__:
            descriptor = klass.__dict__["languages"]
            break
    assert isinstance(descriptor, property)

def test_org::sgiusa::model::member_has_subDivision():
    assert hasattr(org::sgiusa::model::Member, "subDivision")
    descriptor = None
    for klass in org::sgiusa::model::Member.__mro__:
        if "subDivision" in klass.__dict__:
            descriptor = klass.__dict__["subDivision"]
            break
    assert isinstance(descriptor, property)

def test_org::sgiusa::model::member_has_division():
    assert hasattr(org::sgiusa::model::Member, "division")
    descriptor = None
    for klass in org::sgiusa::model::Member.__mro__:
        if "division" in klass.__dict__:
            descriptor = klass.__dict__["division"]
            break
    assert isinstance(descriptor, property)



def test_org::sgiusa::model::leadershipinfo_is_not_abstract():
    assert not inspect.isabstract(org::sgiusa::model::LeadershipInfo)


def test_org::sgiusa::model::leadershipinfo_constructor_exists():
    assert callable(org::sgiusa::model::LeadershipInfo.__init__)


def test_org::sgiusa::model::leadershipinfo_constructor_args():
    sig = inspect.signature(org::sgiusa::model::LeadershipInfo.__init__)
    params = list(sig.parameters.keys())
    assert "manualSigned" in params, "Missing parameter 'manualSigned'"
    assert "examPassedDate" in params, "Missing parameter 'examPassedDate'"
    assert "examPassed" in params, "Missing parameter 'examPassed'"
    assert "lastUpdate" in params, "Missing parameter 'lastUpdate'"
    assert "manualSignedDate" in params, "Missing parameter 'manualSignedDate'"
    assert "id" in params, "Missing parameter 'id'"

def test_org::sgiusa::model::leadershipinfo_has_manualSigned():
    assert hasattr(org::sgiusa::model::LeadershipInfo, "manualSigned")
    descriptor = None
    for klass in org::sgiusa::model::LeadershipInfo.__mro__:
        if "manualSigned" in klass.__dict__:
            descriptor = klass.__dict__["manualSigned"]
            break
    assert isinstance(descriptor, property)

def test_org::sgiusa::model::leadershipinfo_has_examPassedDate():
    assert hasattr(org::sgiusa::model::LeadershipInfo, "examPassedDate")
    descriptor = None
    for klass in org::sgiusa::model::LeadershipInfo.__mro__:
        if "examPassedDate" in klass.__dict__:
            descriptor = klass.__dict__["examPassedDate"]
            break
    assert isinstance(descriptor, property)

def test_org::sgiusa::model::leadershipinfo_has_examPassed():
    assert hasattr(org::sgiusa::model::LeadershipInfo, "examPassed")
    descriptor = None
    for klass in org::sgiusa::model::LeadershipInfo.__mro__:
        if "examPassed" in klass.__dict__:
            descriptor = klass.__dict__["examPassed"]
            break
    assert isinstance(descriptor, property)

def test_org::sgiusa::model::leadershipinfo_has_lastUpdate():
    assert hasattr(org::sgiusa::model::LeadershipInfo, "lastUpdate")
    descriptor = None
    for klass in org::sgiusa::model::LeadershipInfo.__mro__:
        if "lastUpdate" in klass.__dict__:
            descriptor = klass.__dict__["lastUpdate"]
            break
    assert isinstance(descriptor, property)

def test_org::sgiusa::model::leadershipinfo_has_manualSignedDate():
    assert hasattr(org::sgiusa::model::LeadershipInfo, "manualSignedDate")
    descriptor = None
    for klass in org::sgiusa::model::LeadershipInfo.__mro__:
        if "manualSignedDate" in klass.__dict__:
            descriptor = klass.__dict__["manualSignedDate"]
            break
    assert isinstance(descriptor, property)

def test_org::sgiusa::model::leadershipinfo_has_id():
    assert hasattr(org::sgiusa::model::LeadershipInfo, "id")
    descriptor = None
    for klass in org::sgiusa::model::LeadershipInfo.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_org::sgiusa::model::leadershiprole_is_not_abstract():
    assert not inspect.isabstract(org::sgiusa::model::LeadershipRole)


def test_org::sgiusa::model::leadershiprole_constructor_exists():
    assert callable(org::sgiusa::model::LeadershipRole.__init__)


def test_org::sgiusa::model::leadershiprole_constructor_args():
    sig = inspect.signature(org::sgiusa::model::LeadershipRole.__init__)
    params = list(sig.parameters.keys())
    assert "level" in params, "Missing parameter 'level'"
    assert "lastUpdate" in params, "Missing parameter 'lastUpdate'"
    assert "position" in params, "Missing parameter 'position'"
    assert "subDivision" in params, "Missing parameter 'subDivision'"
    assert "active" in params, "Missing parameter 'active'"
    assert "division" in params, "Missing parameter 'division'"
    assert "activityGroup" in params, "Missing parameter 'activityGroup'"
    assert "startDate" in params, "Missing parameter 'startDate'"
    assert "endDate" in params, "Missing parameter 'endDate'"
    assert "id" in params, "Missing parameter 'id'"

def test_org::sgiusa::model::leadershiprole_has_level():
    assert hasattr(org::sgiusa::model::LeadershipRole, "level")
    descriptor = None
    for klass in org::sgiusa::model::LeadershipRole.__mro__:
        if "level" in klass.__dict__:
            descriptor = klass.__dict__["level"]
            break
    assert isinstance(descriptor, property)

def test_org::sgiusa::model::leadershiprole_has_lastUpdate():
    assert hasattr(org::sgiusa::model::LeadershipRole, "lastUpdate")
    descriptor = None
    for klass in org::sgiusa::model::LeadershipRole.__mro__:
        if "lastUpdate" in klass.__dict__:
            descriptor = klass.__dict__["lastUpdate"]
            break
    assert isinstance(descriptor, property)

def test_org::sgiusa::model::leadershiprole_has_position():
    assert hasattr(org::sgiusa::model::LeadershipRole, "position")
    descriptor = None
    for klass in org::sgiusa::model::LeadershipRole.__mro__:
        if "position" in klass.__dict__:
            descriptor = klass.__dict__["position"]
            break
    assert isinstance(descriptor, property)

def test_org::sgiusa::model::leadershiprole_has_subDivision():
    assert hasattr(org::sgiusa::model::LeadershipRole, "subDivision")
    descriptor = None
    for klass in org::sgiusa::model::LeadershipRole.__mro__:
        if "subDivision" in klass.__dict__:
            descriptor = klass.__dict__["subDivision"]
            break
    assert isinstance(descriptor, property)

def test_org::sgiusa::model::leadershiprole_has_active():
    assert hasattr(org::sgiusa::model::LeadershipRole, "active")
    descriptor = None
    for klass in org::sgiusa::model::LeadershipRole.__mro__:
        if "active" in klass.__dict__:
            descriptor = klass.__dict__["active"]
            break
    assert isinstance(descriptor, property)

def test_org::sgiusa::model::leadershiprole_has_division():
    assert hasattr(org::sgiusa::model::LeadershipRole, "division")
    descriptor = None
    for klass in org::sgiusa::model::LeadershipRole.__mro__:
        if "division" in klass.__dict__:
            descriptor = klass.__dict__["division"]
            break
    assert isinstance(descriptor, property)

def test_org::sgiusa::model::leadershiprole_has_activityGroup():
    assert hasattr(org::sgiusa::model::LeadershipRole, "activityGroup")
    descriptor = None
    for klass in org::sgiusa::model::LeadershipRole.__mro__:
        if "activityGroup" in klass.__dict__:
            descriptor = klass.__dict__["activityGroup"]
            break
    assert isinstance(descriptor, property)

def test_org::sgiusa::model::leadershiprole_has_startDate():
    assert hasattr(org::sgiusa::model::LeadershipRole, "startDate")
    descriptor = None
    for klass in org::sgiusa::model::LeadershipRole.__mro__:
        if "startDate" in klass.__dict__:
            descriptor = klass.__dict__["startDate"]
            break
    assert isinstance(descriptor, property)

def test_org::sgiusa::model::leadershiprole_has_endDate():
    assert hasattr(org::sgiusa::model::LeadershipRole, "endDate")
    descriptor = None
    for klass in org::sgiusa::model::LeadershipRole.__mro__:
        if "endDate" in klass.__dict__:
            descriptor = klass.__dict__["endDate"]
            break
    assert isinstance(descriptor, property)

def test_org::sgiusa::model::leadershiprole_has_id():
    assert hasattr(org::sgiusa::model::LeadershipRole, "id")
    descriptor = None
    for klass in org::sgiusa::model::LeadershipRole.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_org::sgiusa::model::gohonzoninfo_is_not_abstract():
    assert not inspect.isabstract(org::sgiusa::model::GohonzonInfo)


def test_org::sgiusa::model::gohonzoninfo_constructor_exists():
    assert callable(org::sgiusa::model::GohonzonInfo.__init__)


def test_org::sgiusa::model::gohonzoninfo_constructor_args():
    sig = inspect.signature(org::sgiusa::model::GohonzonInfo.__init__)
    params = list(sig.parameters.keys())
    assert "lastUpdate" in params, "Missing parameter 'lastUpdate'"
    assert "returned" in params, "Missing parameter 'returned'"
    assert "id" in params, "Missing parameter 'id'"
    assert "returnDate" in params, "Missing parameter 'returnDate'"
    assert "gohonzonType" in params, "Missing parameter 'gohonzonType'"
    assert "receiveDate" in params, "Missing parameter 'receiveDate'"

def test_org::sgiusa::model::gohonzoninfo_has_lastUpdate():
    assert hasattr(org::sgiusa::model::GohonzonInfo, "lastUpdate")
    descriptor = None
    for klass in org::sgiusa::model::GohonzonInfo.__mro__:
        if "lastUpdate" in klass.__dict__:
            descriptor = klass.__dict__["lastUpdate"]
            break
    assert isinstance(descriptor, property)

def test_org::sgiusa::model::gohonzoninfo_has_returned():
    assert hasattr(org::sgiusa::model::GohonzonInfo, "returned")
    descriptor = None
    for klass in org::sgiusa::model::GohonzonInfo.__mro__:
        if "returned" in klass.__dict__:
            descriptor = klass.__dict__["returned"]
            break
    assert isinstance(descriptor, property)

def test_org::sgiusa::model::gohonzoninfo_has_id():
    assert hasattr(org::sgiusa::model::GohonzonInfo, "id")
    descriptor = None
    for klass in org::sgiusa::model::GohonzonInfo.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_org::sgiusa::model::gohonzoninfo_has_returnDate():
    assert hasattr(org::sgiusa::model::GohonzonInfo, "returnDate")
    descriptor = None
    for klass in org::sgiusa::model::GohonzonInfo.__mro__:
        if "returnDate" in klass.__dict__:
            descriptor = klass.__dict__["returnDate"]
            break
    assert isinstance(descriptor, property)

def test_org::sgiusa::model::gohonzoninfo_has_gohonzonType():
    assert hasattr(org::sgiusa::model::GohonzonInfo, "gohonzonType")
    descriptor = None
    for klass in org::sgiusa::model::GohonzonInfo.__mro__:
        if "gohonzonType" in klass.__dict__:
            descriptor = klass.__dict__["gohonzonType"]
            break
    assert isinstance(descriptor, property)

def test_org::sgiusa::model::gohonzoninfo_has_receiveDate():
    assert hasattr(org::sgiusa::model::GohonzonInfo, "receiveDate")
    descriptor = None
    for klass in org::sgiusa::model::GohonzonInfo.__mro__:
        if "receiveDate" in klass.__dict__:
            descriptor = klass.__dict__["receiveDate"]
            break
    assert isinstance(descriptor, property)



def test_org::sgiusa::model::familymember_is_not_abstract():
    assert not inspect.isabstract(org::sgiusa::model::FamilyMember)


def test_org::sgiusa::model::familymember_constructor_exists():
    assert callable(org::sgiusa::model::FamilyMember.__init__)


def test_org::sgiusa::model::familymember_constructor_args():
    sig = inspect.signature(org::sgiusa::model::FamilyMember.__init__)
    params = list(sig.parameters.keys())
    assert "personName" in params, "Missing parameter 'personName'"
    assert "lastUpdate" in params, "Missing parameter 'lastUpdate'"
    assert "familyRelation" in params, "Missing parameter 'familyRelation'"
    assert "id" in params, "Missing parameter 'id'"
    assert "sgiMember" in params, "Missing parameter 'sgiMember'"

def test_org::sgiusa::model::familymember_has_personName():
    assert hasattr(org::sgiusa::model::FamilyMember, "personName")
    descriptor = None
    for klass in org::sgiusa::model::FamilyMember.__mro__:
        if "personName" in klass.__dict__:
            descriptor = klass.__dict__["personName"]
            break
    assert isinstance(descriptor, property)

def test_org::sgiusa::model::familymember_has_lastUpdate():
    assert hasattr(org::sgiusa::model::FamilyMember, "lastUpdate")
    descriptor = None
    for klass in org::sgiusa::model::FamilyMember.__mro__:
        if "lastUpdate" in klass.__dict__:
            descriptor = klass.__dict__["lastUpdate"]
            break
    assert isinstance(descriptor, property)

def test_org::sgiusa::model::familymember_has_familyRelation():
    assert hasattr(org::sgiusa::model::FamilyMember, "familyRelation")
    descriptor = None
    for klass in org::sgiusa::model::FamilyMember.__mro__:
        if "familyRelation" in klass.__dict__:
            descriptor = klass.__dict__["familyRelation"]
            break
    assert isinstance(descriptor, property)

def test_org::sgiusa::model::familymember_has_id():
    assert hasattr(org::sgiusa::model::FamilyMember, "id")
    descriptor = None
    for klass in org::sgiusa::model::FamilyMember.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_org::sgiusa::model::familymember_has_sgiMember():
    assert hasattr(org::sgiusa::model::FamilyMember, "sgiMember")
    descriptor = None
    for klass in org::sgiusa::model::FamilyMember.__mro__:
        if "sgiMember" in klass.__dict__:
            descriptor = klass.__dict__["sgiMember"]
            break
    assert isinstance(descriptor, property)



def test_org::sgiusa::model::event_is_not_abstract():
    assert not inspect.isabstract(org::sgiusa::model::Event)


def test_org::sgiusa::model::event_constructor_exists():
    assert callable(org::sgiusa::model::Event.__init__)


def test_org::sgiusa::model::event_constructor_args():
    sig = inspect.signature(org::sgiusa::model::Event.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "divisions" in params, "Missing parameter 'divisions'"
    assert "status" in params, "Missing parameter 'status'"
    assert "subDivisions" in params, "Missing parameter 'subDivisions'"
    assert "userId" in params, "Missing parameter 'userId'"

def test_org::sgiusa::model::event_has_id():
    assert hasattr(org::sgiusa::model::Event, "id")
    descriptor = None
    for klass in org::sgiusa::model::Event.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_org::sgiusa::model::event_has_divisions():
    assert hasattr(org::sgiusa::model::Event, "divisions")
    descriptor = None
    for klass in org::sgiusa::model::Event.__mro__:
        if "divisions" in klass.__dict__:
            descriptor = klass.__dict__["divisions"]
            break
    assert isinstance(descriptor, property)

def test_org::sgiusa::model::event_has_status():
    assert hasattr(org::sgiusa::model::Event, "status")
    descriptor = None
    for klass in org::sgiusa::model::Event.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)

def test_org::sgiusa::model::event_has_subDivisions():
    assert hasattr(org::sgiusa::model::Event, "subDivisions")
    descriptor = None
    for klass in org::sgiusa::model::Event.__mro__:
        if "subDivisions" in klass.__dict__:
            descriptor = klass.__dict__["subDivisions"]
            break
    assert isinstance(descriptor, property)

def test_org::sgiusa::model::event_has_userId():
    assert hasattr(org::sgiusa::model::Event, "userId")
    descriptor = None
    for klass in org::sgiusa::model::Event.__mro__:
        if "userId" in klass.__dict__:
            descriptor = klass.__dict__["userId"]
            break
    assert isinstance(descriptor, property)



def test_studydeptinfo_is_not_abstract():
    assert not inspect.isabstract(StudyDeptInfo)


def test_studydeptinfo_constructor_exists():
    assert callable(StudyDeptInfo.__init__)


def test_studydeptinfo_constructor_args():
    sig = inspect.signature(StudyDeptInfo.__init__)
    params = list(sig.parameters.keys())



def test_studydeptexam_is_not_abstract():
    assert not inspect.isabstract(StudyDeptExam)


def test_studydeptexam_constructor_exists():
    assert callable(StudyDeptExam.__init__)


def test_studydeptexam_constructor_args():
    sig = inspect.signature(StudyDeptExam.__init__)
    params = list(sig.parameters.keys())



def test_schoolinfo_is_not_abstract():
    assert not inspect.isabstract(SchoolInfo)


def test_schoolinfo_constructor_exists():
    assert callable(SchoolInfo.__init__)


def test_schoolinfo_constructor_args():
    sig = inspect.signature(SchoolInfo.__init__)
    params = list(sig.parameters.keys())



def test_registration_is_not_abstract():
    assert not inspect.isabstract(Registration)


def test_registration_constructor_exists():
    assert callable(Registration.__init__)


def test_registration_constructor_args():
    sig = inspect.signature(Registration.__init__)
    params = list(sig.parameters.keys())



def test_org::sgiusa::model::emaillist_is_not_abstract():
    assert not inspect.isabstract(org::sgiusa::model::EmailList)


def test_org::sgiusa::model::emaillist_constructor_exists():
    assert callable(org::sgiusa::model::EmailList.__init__)


def test_org::sgiusa::model::emaillist_constructor_args():
    sig = inspect.signature(org::sgiusa::model::EmailList.__init__)
    params = list(sig.parameters.keys())
    assert "divisions" in params, "Missing parameter 'divisions'"
    assert "id" in params, "Missing parameter 'id'"
    assert "subDivisions" in params, "Missing parameter 'subDivisions'"
    assert "enabled" in params, "Missing parameter 'enabled'"
    assert "activityGroups" in params, "Missing parameter 'activityGroups'"

def test_org::sgiusa::model::emaillist_has_divisions():
    assert hasattr(org::sgiusa::model::EmailList, "divisions")
    descriptor = None
    for klass in org::sgiusa::model::EmailList.__mro__:
        if "divisions" in klass.__dict__:
            descriptor = klass.__dict__["divisions"]
            break
    assert isinstance(descriptor, property)

def test_org::sgiusa::model::emaillist_has_id():
    assert hasattr(org::sgiusa::model::EmailList, "id")
    descriptor = None
    for klass in org::sgiusa::model::EmailList.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_org::sgiusa::model::emaillist_has_subDivisions():
    assert hasattr(org::sgiusa::model::EmailList, "subDivisions")
    descriptor = None
    for klass in org::sgiusa::model::EmailList.__mro__:
        if "subDivisions" in klass.__dict__:
            descriptor = klass.__dict__["subDivisions"]
            break
    assert isinstance(descriptor, property)

def test_org::sgiusa::model::emaillist_has_enabled():
    assert hasattr(org::sgiusa::model::EmailList, "enabled")
    descriptor = None
    for klass in org::sgiusa::model::EmailList.__mro__:
        if "enabled" in klass.__dict__:
            descriptor = klass.__dict__["enabled"]
            break
    assert isinstance(descriptor, property)

def test_org::sgiusa::model::emaillist_has_activityGroups():
    assert hasattr(org::sgiusa::model::EmailList, "activityGroups")
    descriptor = None
    for klass in org::sgiusa::model::EmailList.__mro__:
        if "activityGroups" in klass.__dict__:
            descriptor = klass.__dict__["activityGroups"]
            break
    assert isinstance(descriptor, property)



def test_view_is_not_abstract():
    assert not inspect.isabstract(View)


def test_view_constructor_exists():
    assert callable(View.__init__)


def test_view_constructor_args():
    sig = inspect.signature(View.__init__)
    params = list(sig.parameters.keys())



def test_users_is_not_abstract():
    assert not inspect.isabstract(Users)


def test_users_constructor_exists():
    assert callable(Users.__init__)


def test_users_constructor_args():
    sig = inspect.signature(Users.__init__)
    params = list(sig.parameters.keys())



def test_membersearchcriteria_is_not_abstract():
    assert not inspect.isabstract(MemberSearchCriteria)


def test_membersearchcriteria_constructor_exists():
    assert callable(MemberSearchCriteria.__init__)


def test_membersearchcriteria_constructor_args():
    sig = inspect.signature(MemberSearchCriteria.__init__)
    params = list(sig.parameters.keys())



def test_members_is_not_abstract():
    assert not inspect.isabstract(Members)


def test_members_constructor_exists():
    assert callable(Members.__init__)


def test_members_constructor_args():
    sig = inspect.signature(Members.__init__)
    params = list(sig.parameters.keys())



def test_member_is_not_abstract():
    assert not inspect.isabstract(Member)


def test_member_constructor_exists():
    assert callable(Member.__init__)


def test_member_constructor_args():
    sig = inspect.signature(Member.__init__)
    params = list(sig.parameters.keys())



def test_leadershiprole_is_not_abstract():
    assert not inspect.isabstract(LeadershipRole)


def test_leadershiprole_constructor_exists():
    assert callable(LeadershipRole.__init__)


def test_leadershiprole_constructor_args():
    sig = inspect.signature(LeadershipRole.__init__)
    params = list(sig.parameters.keys())



def test_leadershipinfo_is_not_abstract():
    assert not inspect.isabstract(LeadershipInfo)


def test_leadershipinfo_constructor_exists():
    assert callable(LeadershipInfo.__init__)


def test_leadershipinfo_constructor_args():
    sig = inspect.signature(LeadershipInfo.__init__)
    params = list(sig.parameters.keys())



def test_preferences_is_not_abstract():
    assert not inspect.isabstract(Preferences)


def test_preferences_constructor_exists():
    assert callable(Preferences.__init__)


def test_preferences_constructor_args():
    sig = inspect.signature(Preferences.__init__)
    params = list(sig.parameters.keys())



def test_permission_is_not_abstract():
    assert not inspect.isabstract(Permission)


def test_permission_constructor_exists():
    assert callable(Permission.__init__)


def test_permission_constructor_args():
    sig = inspect.signature(Permission.__init__)
    params = list(sig.parameters.keys())



def test_organization_is_not_abstract():
    assert not inspect.isabstract(Organization)


def test_organization_constructor_exists():
    assert callable(Organization.__init__)


def test_organization_constructor_args():
    sig = inspect.signature(Organization.__init__)
    params = list(sig.parameters.keys())



def test_org::aries::common::eobject_is_not_abstract():
    assert not inspect.isabstract(org::aries::common::EObject)


def test_org::aries::common::eobject_constructor_exists():
    assert callable(org::aries::common::EObject.__init__)


def test_org::aries::common::eobject_constructor_args():
    sig = inspect.signature(org::aries::common::EObject.__init__)
    params = list(sig.parameters.keys())



def test_org::aries::common::mapentry_is_not_abstract():
    assert not inspect.isabstract(org::aries::common::MapEntry)


def test_org::aries::common::mapentry_constructor_exists():
    assert callable(org::aries::common::MapEntry.__init__)


def test_org::aries::common::mapentry_constructor_args():
    sig = inspect.signature(org::aries::common::MapEntry.__init__)
    params = list(sig.parameters.keys())



def test_org::aries::common::map_is_not_abstract():
    assert not inspect.isabstract(org::aries::common::Map)


def test_org::aries::common::map_constructor_exists():
    assert callable(org::aries::common::Map.__init__)


def test_org::aries::common::map_constructor_args():
    sig = inspect.signature(org::aries::common::Map.__init__)
    params = list(sig.parameters.keys())



def test_org::aries::common::note_is_not_abstract():
    assert not inspect.isabstract(org::aries::common::Note)


def test_org::aries::common::note_constructor_exists():
    assert callable(org::aries::common::Note.__init__)


def test_org::aries::common::note_constructor_args():
    sig = inspect.signature(org::aries::common::Note.__init__)
    params = list(sig.parameters.keys())
    assert "lastUpdate" in params, "Missing parameter 'lastUpdate'"
    assert "id" in params, "Missing parameter 'id'"
    assert "creationDate" in params, "Missing parameter 'creationDate'"
    assert "text" in params, "Missing parameter 'text'"

def test_org::aries::common::note_has_lastUpdate():
    assert hasattr(org::aries::common::Note, "lastUpdate")
    descriptor = None
    for klass in org::aries::common::Note.__mro__:
        if "lastUpdate" in klass.__dict__:
            descriptor = klass.__dict__["lastUpdate"]
            break
    assert isinstance(descriptor, property)

def test_org::aries::common::note_has_id():
    assert hasattr(org::aries::common::Note, "id")
    descriptor = None
    for klass in org::aries::common::Note.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_org::aries::common::note_has_creationDate():
    assert hasattr(org::aries::common::Note, "creationDate")
    descriptor = None
    for klass in org::aries::common::Note.__mro__:
        if "creationDate" in klass.__dict__:
            descriptor = klass.__dict__["creationDate"]
            break
    assert isinstance(descriptor, property)

def test_org::aries::common::note_has_text():
    assert hasattr(org::aries::common::Note, "text")
    descriptor = None
    for klass in org::aries::common::Note.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_org::aries::common::event_is_not_abstract():
    assert not inspect.isabstract(org::aries::common::Event)


def test_org::aries::common::event_constructor_exists():
    assert callable(org::aries::common::Event.__init__)


def test_org::aries::common::event_constructor_args():
    sig = inspect.signature(org::aries::common::Event.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_org::aries::common::event_has_id():
    assert hasattr(org::aries::common::Event, "id")
    descriptor = None
    for klass in org::aries::common::Event.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_org::aries::common::emailmessage_is_not_abstract():
    assert not inspect.isabstract(org::aries::common::EmailMessage)


def test_org::aries::common::emailmessage_constructor_exists():
    assert callable(org::aries::common::EmailMessage.__init__)


def test_org::aries::common::emailmessage_constructor_args():
    sig = inspect.signature(org::aries::common::EmailMessage.__init__)
    params = list(sig.parameters.keys())
    assert "sourceId" in params, "Missing parameter 'sourceId'"
    assert "smtpHost" in params, "Missing parameter 'smtpHost'"
    assert "content" in params, "Missing parameter 'content'"
    assert "sendAsHtml" in params, "Missing parameter 'sendAsHtml'"
    assert "smtpPort" in params, "Missing parameter 'smtpPort'"
    assert "timestamp" in params, "Missing parameter 'timestamp'"
    assert "id" in params, "Missing parameter 'id'"
    assert "subject" in params, "Missing parameter 'subject'"

def test_org::aries::common::emailmessage_has_sourceId():
    assert hasattr(org::aries::common::EmailMessage, "sourceId")
    descriptor = None
    for klass in org::aries::common::EmailMessage.__mro__:
        if "sourceId" in klass.__dict__:
            descriptor = klass.__dict__["sourceId"]
            break
    assert isinstance(descriptor, property)

def test_org::aries::common::emailmessage_has_smtpHost():
    assert hasattr(org::aries::common::EmailMessage, "smtpHost")
    descriptor = None
    for klass in org::aries::common::EmailMessage.__mro__:
        if "smtpHost" in klass.__dict__:
            descriptor = klass.__dict__["smtpHost"]
            break
    assert isinstance(descriptor, property)

def test_org::aries::common::emailmessage_has_content():
    assert hasattr(org::aries::common::EmailMessage, "content")
    descriptor = None
    for klass in org::aries::common::EmailMessage.__mro__:
        if "content" in klass.__dict__:
            descriptor = klass.__dict__["content"]
            break
    assert isinstance(descriptor, property)

def test_org::aries::common::emailmessage_has_sendAsHtml():
    assert hasattr(org::aries::common::EmailMessage, "sendAsHtml")
    descriptor = None
    for klass in org::aries::common::EmailMessage.__mro__:
        if "sendAsHtml" in klass.__dict__:
            descriptor = klass.__dict__["sendAsHtml"]
            break
    assert isinstance(descriptor, property)

def test_org::aries::common::emailmessage_has_smtpPort():
    assert hasattr(org::aries::common::EmailMessage, "smtpPort")
    descriptor = None
    for klass in org::aries::common::EmailMessage.__mro__:
        if "smtpPort" in klass.__dict__:
            descriptor = klass.__dict__["smtpPort"]
            break
    assert isinstance(descriptor, property)

def test_org::aries::common::emailmessage_has_timestamp():
    assert hasattr(org::aries::common::EmailMessage, "timestamp")
    descriptor = None
    for klass in org::aries::common::EmailMessage.__mro__:
        if "timestamp" in klass.__dict__:
            descriptor = klass.__dict__["timestamp"]
            break
    assert isinstance(descriptor, property)

def test_org::aries::common::emailmessage_has_id():
    assert hasattr(org::aries::common::EmailMessage, "id")
    descriptor = None
    for klass in org::aries::common::EmailMessage.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_org::aries::common::emailmessage_has_subject():
    assert hasattr(org::aries::common::EmailMessage, "subject")
    descriptor = None
    for klass in org::aries::common::EmailMessage.__mro__:
        if "subject" in klass.__dict__:
            descriptor = klass.__dict__["subject"]
            break
    assert isinstance(descriptor, property)



def test_org::aries::common::emailbox_is_not_abstract():
    assert not inspect.isabstract(org::aries::common::EmailBox)


def test_org::aries::common::emailbox_constructor_exists():
    assert callable(org::aries::common::EmailBox.__init__)


def test_org::aries::common::emailbox_constructor_args():
    sig = inspect.signature(org::aries::common::EmailBox.__init__)
    params = list(sig.parameters.keys())
    assert "creationDate" in params, "Missing parameter 'creationDate'"
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"
    assert "type" in params, "Missing parameter 'type'"
    assert "lastUpdate" in params, "Missing parameter 'lastUpdate'"

def test_org::aries::common::emailbox_has_creationDate():
    assert hasattr(org::aries::common::EmailBox, "creationDate")
    descriptor = None
    for klass in org::aries::common::EmailBox.__mro__:
        if "creationDate" in klass.__dict__:
            descriptor = klass.__dict__["creationDate"]
            break
    assert isinstance(descriptor, property)

def test_org::aries::common::emailbox_has_name():
    assert hasattr(org::aries::common::EmailBox, "name")
    descriptor = None
    for klass in org::aries::common::EmailBox.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_org::aries::common::emailbox_has_id():
    assert hasattr(org::aries::common::EmailBox, "id")
    descriptor = None
    for klass in org::aries::common::EmailBox.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_org::aries::common::emailbox_has_type():
    assert hasattr(org::aries::common::EmailBox, "type")
    descriptor = None
    for klass in org::aries::common::EmailBox.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_org::aries::common::emailbox_has_lastUpdate():
    assert hasattr(org::aries::common::EmailBox, "lastUpdate")
    descriptor = None
    for klass in org::aries::common::EmailBox.__mro__:
        if "lastUpdate" in klass.__dict__:
            descriptor = klass.__dict__["lastUpdate"]
            break
    assert isinstance(descriptor, property)



def test_org::aries::common::emailaddresslist_is_not_abstract():
    assert not inspect.isabstract(org::aries::common::EmailAddressList)


def test_org::aries::common::emailaddresslist_constructor_exists():
    assert callable(org::aries::common::EmailAddressList.__init__)


def test_org::aries::common::emailaddresslist_constructor_args():
    sig = inspect.signature(org::aries::common::EmailAddressList.__init__)
    params = list(sig.parameters.keys())
    assert "emailAddress" in params, "Missing parameter 'emailAddress'"
    assert "name" in params, "Missing parameter 'name'"

def test_org::aries::common::emailaddresslist_has_emailAddress():
    assert hasattr(org::aries::common::EmailAddressList, "emailAddress")
    descriptor = None
    for klass in org::aries::common::EmailAddressList.__mro__:
        if "emailAddress" in klass.__dict__:
            descriptor = klass.__dict__["emailAddress"]
            break
    assert isinstance(descriptor, property)

def test_org::aries::common::emailaddresslist_has_name():
    assert hasattr(org::aries::common::EmailAddressList, "name")
    descriptor = None
    for klass in org::aries::common::EmailAddressList.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_org::aries::common::emailaddress_is_not_abstract():
    assert not inspect.isabstract(org::aries::common::EmailAddress)


def test_org::aries::common::emailaddress_constructor_exists():
    assert callable(org::aries::common::EmailAddress.__init__)


def test_org::aries::common::emailaddress_constructor_args():
    sig = inspect.signature(org::aries::common::EmailAddress.__init__)
    params = list(sig.parameters.keys())
    assert "creationDate" in params, "Missing parameter 'creationDate'"
    assert "id" in params, "Missing parameter 'id'"
    assert "enabled" in params, "Missing parameter 'enabled'"
    assert "organization" in params, "Missing parameter 'organization'"
    assert "lastUpdate" in params, "Missing parameter 'lastUpdate'"
    assert "userId" in params, "Missing parameter 'userId'"
    assert "url" in params, "Missing parameter 'url'"
    assert "firstName" in params, "Missing parameter 'firstName'"
    assert "lastName" in params, "Missing parameter 'lastName'"

def test_org::aries::common::emailaddress_has_creationDate():
    assert hasattr(org::aries::common::EmailAddress, "creationDate")
    descriptor = None
    for klass in org::aries::common::EmailAddress.__mro__:
        if "creationDate" in klass.__dict__:
            descriptor = klass.__dict__["creationDate"]
            break
    assert isinstance(descriptor, property)

def test_org::aries::common::emailaddress_has_id():
    assert hasattr(org::aries::common::EmailAddress, "id")
    descriptor = None
    for klass in org::aries::common::EmailAddress.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_org::aries::common::emailaddress_has_enabled():
    assert hasattr(org::aries::common::EmailAddress, "enabled")
    descriptor = None
    for klass in org::aries::common::EmailAddress.__mro__:
        if "enabled" in klass.__dict__:
            descriptor = klass.__dict__["enabled"]
            break
    assert isinstance(descriptor, property)

def test_org::aries::common::emailaddress_has_organization():
    assert hasattr(org::aries::common::EmailAddress, "organization")
    descriptor = None
    for klass in org::aries::common::EmailAddress.__mro__:
        if "organization" in klass.__dict__:
            descriptor = klass.__dict__["organization"]
            break
    assert isinstance(descriptor, property)

def test_org::aries::common::emailaddress_has_lastUpdate():
    assert hasattr(org::aries::common::EmailAddress, "lastUpdate")
    descriptor = None
    for klass in org::aries::common::EmailAddress.__mro__:
        if "lastUpdate" in klass.__dict__:
            descriptor = klass.__dict__["lastUpdate"]
            break
    assert isinstance(descriptor, property)

def test_org::aries::common::emailaddress_has_userId():
    assert hasattr(org::aries::common::EmailAddress, "userId")
    descriptor = None
    for klass in org::aries::common::EmailAddress.__mro__:
        if "userId" in klass.__dict__:
            descriptor = klass.__dict__["userId"]
            break
    assert isinstance(descriptor, property)

def test_org::aries::common::emailaddress_has_url():
    assert hasattr(org::aries::common::EmailAddress, "url")
    descriptor = None
    for klass in org::aries::common::EmailAddress.__mro__:
        if "url" in klass.__dict__:
            descriptor = klass.__dict__["url"]
            break
    assert isinstance(descriptor, property)

def test_org::aries::common::emailaddress_has_firstName():
    assert hasattr(org::aries::common::EmailAddress, "firstName")
    descriptor = None
    for klass in org::aries::common::EmailAddress.__mro__:
        if "firstName" in klass.__dict__:
            descriptor = klass.__dict__["firstName"]
            break
    assert isinstance(descriptor, property)

def test_org::aries::common::emailaddress_has_lastName():
    assert hasattr(org::aries::common::EmailAddress, "lastName")
    descriptor = None
    for klass in org::aries::common::EmailAddress.__mro__:
        if "lastName" in klass.__dict__:
            descriptor = klass.__dict__["lastName"]
            break
    assert isinstance(descriptor, property)



def test_org::aries::common::emailaccount_is_not_abstract():
    assert not inspect.isabstract(org::aries::common::EmailAccount)


def test_org::aries::common::emailaccount_constructor_exists():
    assert callable(org::aries::common::EmailAccount.__init__)


def test_org::aries::common::emailaccount_constructor_args():
    sig = inspect.signature(org::aries::common::EmailAccount.__init__)
    params = list(sig.parameters.keys())
    assert "enabled" in params, "Missing parameter 'enabled'"
    assert "password" in params, "Missing parameter 'password'"
    assert "id" in params, "Missing parameter 'id'"
    assert "lastName" in params, "Missing parameter 'lastName'"
    assert "firstName" in params, "Missing parameter 'firstName'"
    assert "userId" in params, "Missing parameter 'userId'"

def test_org::aries::common::emailaccount_has_enabled():
    assert hasattr(org::aries::common::EmailAccount, "enabled")
    descriptor = None
    for klass in org::aries::common::EmailAccount.__mro__:
        if "enabled" in klass.__dict__:
            descriptor = klass.__dict__["enabled"]
            break
    assert isinstance(descriptor, property)

def test_org::aries::common::emailaccount_has_password():
    assert hasattr(org::aries::common::EmailAccount, "password")
    descriptor = None
    for klass in org::aries::common::EmailAccount.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)

def test_org::aries::common::emailaccount_has_id():
    assert hasattr(org::aries::common::EmailAccount, "id")
    descriptor = None
    for klass in org::aries::common::EmailAccount.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_org::aries::common::emailaccount_has_lastName():
    assert hasattr(org::aries::common::EmailAccount, "lastName")
    descriptor = None
    for klass in org::aries::common::EmailAccount.__mro__:
        if "lastName" in klass.__dict__:
            descriptor = klass.__dict__["lastName"]
            break
    assert isinstance(descriptor, property)

def test_org::aries::common::emailaccount_has_firstName():
    assert hasattr(org::aries::common::EmailAccount, "firstName")
    descriptor = None
    for klass in org::aries::common::EmailAccount.__mro__:
        if "firstName" in klass.__dict__:
            descriptor = klass.__dict__["firstName"]
            break
    assert isinstance(descriptor, property)

def test_org::aries::common::emailaccount_has_userId():
    assert hasattr(org::aries::common::EmailAccount, "userId")
    descriptor = None
    for klass in org::aries::common::EmailAccount.__mro__:
        if "userId" in klass.__dict__:
            descriptor = klass.__dict__["userId"]
            break
    assert isinstance(descriptor, property)



def test_zipcode_is_not_abstract():
    assert not inspect.isabstract(ZipCode)


def test_zipcode_constructor_exists():
    assert callable(ZipCode.__init__)


def test_zipcode_constructor_args():
    sig = inspect.signature(ZipCode.__init__)
    params = list(sig.parameters.keys())



def test_user_is_not_abstract():
    assert not inspect.isabstract(User)


def test_user_constructor_exists():
    assert callable(User.__init__)


def test_user_constructor_args():
    sig = inspect.signature(User.__init__)
    params = list(sig.parameters.keys())



def test_streetaddress_is_not_abstract():
    assert not inspect.isabstract(StreetAddress)


def test_streetaddress_constructor_exists():
    assert callable(StreetAddress.__init__)


def test_streetaddress_constructor_args():
    sig = inspect.signature(StreetAddress.__init__)
    params = list(sig.parameters.keys())



def test_personname_is_not_abstract():
    assert not inspect.isabstract(PersonName)


def test_personname_constructor_exists():
    assert callable(PersonName.__init__)


def test_personname_constructor_args():
    sig = inspect.signature(PersonName.__init__)
    params = list(sig.parameters.keys())



def test_person_is_not_abstract():
    assert not inspect.isabstract(Person)


def test_person_constructor_exists():
    assert callable(Person.__init__)


def test_person_constructor_args():
    sig = inspect.signature(Person.__init__)
    params = list(sig.parameters.keys())



def test_note_is_not_abstract():
    assert not inspect.isabstract(Note)


def test_note_constructor_exists():
    assert callable(Note.__init__)


def test_note_constructor_args():
    sig = inspect.signature(Note.__init__)
    params = list(sig.parameters.keys())



def test_mapentry_is_not_abstract():
    assert not inspect.isabstract(MapEntry)


def test_mapentry_constructor_exists():
    assert callable(MapEntry.__init__)


def test_mapentry_constructor_args():
    sig = inspect.signature(MapEntry.__init__)
    params = list(sig.parameters.keys())



def test_property_is_not_abstract():
    assert not inspect.isabstract(Property)


def test_property_constructor_exists():
    assert callable(Property.__init__)


def test_property_constructor_args():
    sig = inspect.signature(Property.__init__)
    params = list(sig.parameters.keys())



def test_properties_is_not_abstract():
    assert not inspect.isabstract(Properties)


def test_properties_constructor_exists():
    assert callable(Properties.__init__)


def test_properties_constructor_args():
    sig = inspect.signature(Properties.__init__)
    params = list(sig.parameters.keys())



def test_phonenumber_is_not_abstract():
    assert not inspect.isabstract(PhoneNumber)


def test_phonenumber_constructor_exists():
    assert callable(PhoneNumber.__init__)


def test_phonenumber_constructor_args():
    sig = inspect.signature(PhoneNumber.__init__)
    params = list(sig.parameters.keys())



def test_emailmessage_is_not_abstract():
    assert not inspect.isabstract(EmailMessage)


def test_emailmessage_constructor_exists():
    assert callable(EmailMessage.__init__)


def test_emailmessage_constructor_args():
    sig = inspect.signature(EmailMessage.__init__)
    params = list(sig.parameters.keys())



def test_emailbox_is_not_abstract():
    assert not inspect.isabstract(EmailBox)


def test_emailbox_constructor_exists():
    assert callable(EmailBox.__init__)


def test_emailbox_constructor_args():
    sig = inspect.signature(EmailBox.__init__)
    params = list(sig.parameters.keys())



def test_emailaddresslist_is_not_abstract():
    assert not inspect.isabstract(EmailAddressList)


def test_emailaddresslist_constructor_exists():
    assert callable(EmailAddressList.__init__)


def test_emailaddresslist_constructor_args():
    sig = inspect.signature(EmailAddressList.__init__)
    params = list(sig.parameters.keys())



def test_emailaddress_is_not_abstract():
    assert not inspect.isabstract(EmailAddress)


def test_emailaddress_constructor_exists():
    assert callable(EmailAddress.__init__)


def test_emailaddress_constructor_args():
    sig = inspect.signature(EmailAddress.__init__)
    params = list(sig.parameters.keys())



def test_map_is_not_abstract():
    assert not inspect.isabstract(Map)


def test_map_constructor_exists():
    assert callable(Map.__init__)


def test_map_constructor_args():
    sig = inspect.signature(Map.__init__)
    params = list(sig.parameters.keys())



def test_event_is_not_abstract():
    assert not inspect.isabstract(Event)


def test_event_constructor_exists():
    assert callable(Event.__init__)


def test_event_constructor_args():
    sig = inspect.signature(Event.__init__)
    params = list(sig.parameters.keys())



def test_org::aries::common::estringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(org::aries::common::EStringToStringMapEntry)


def test_org::aries::common::estringtostringmapentry_constructor_exists():
    assert callable(org::aries::common::EStringToStringMapEntry.__init__)


def test_org::aries::common::estringtostringmapentry_constructor_args():
    sig = inspect.signature(org::aries::common::EStringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())



def test_org::aries::common::documentroot_is_not_abstract():
    assert not inspect.isabstract(org::aries::common::DocumentRoot)


def test_org::aries::common::documentroot_constructor_exists():
    assert callable(org::aries::common::DocumentRoot.__init__)


def test_org::aries::common::documentroot_constructor_args():
    sig = inspect.signature(org::aries::common::DocumentRoot.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_org::aries::common::documentroot_has_mixed():
    assert hasattr(org::aries::common::DocumentRoot, "mixed")
    descriptor = None
    for klass in org::aries::common::DocumentRoot.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_emailaccount_is_not_abstract():
    assert not inspect.isabstract(EmailAccount)


def test_emailaccount_constructor_exists():
    assert callable(EmailAccount.__init__)


def test_emailaccount_constructor_args():
    sig = inspect.signature(EmailAccount.__init__)
    params = list(sig.parameters.keys())



def test_attachment_is_not_abstract():
    assert not inspect.isabstract(Attachment)


def test_attachment_constructor_exists():
    assert callable(Attachment.__init__)


def test_attachment_constructor_args():
    sig = inspect.signature(Attachment.__init__)
    params = list(sig.parameters.keys())



def test_org::aries::common::attachment_is_not_abstract():
    assert not inspect.isabstract(org::aries::common::Attachment)


def test_org::aries::common::attachment_constructor_exists():
    assert callable(org::aries::common::Attachment.__init__)


def test_org::aries::common::attachment_constructor_args():
    sig = inspect.signature(org::aries::common::Attachment.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "fileData" in params, "Missing parameter 'fileData'"
    assert "fileName" in params, "Missing parameter 'fileName'"
    assert "contentType" in params, "Missing parameter 'contentType'"
    assert "size" in params, "Missing parameter 'size'"
    assert "name" in params, "Missing parameter 'name'"

def test_org::aries::common::attachment_has_id():
    assert hasattr(org::aries::common::Attachment, "id")
    descriptor = None
    for klass in org::aries::common::Attachment.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_org::aries::common::attachment_has_fileData():
    assert hasattr(org::aries::common::Attachment, "fileData")
    descriptor = None
    for klass in org::aries::common::Attachment.__mro__:
        if "fileData" in klass.__dict__:
            descriptor = klass.__dict__["fileData"]
            break
    assert isinstance(descriptor, property)

def test_org::aries::common::attachment_has_fileName():
    assert hasattr(org::aries::common::Attachment, "fileName")
    descriptor = None
    for klass in org::aries::common::Attachment.__mro__:
        if "fileName" in klass.__dict__:
            descriptor = klass.__dict__["fileName"]
            break
    assert isinstance(descriptor, property)

def test_org::aries::common::attachment_has_contentType():
    assert hasattr(org::aries::common::Attachment, "contentType")
    descriptor = None
    for klass in org::aries::common::Attachment.__mro__:
        if "contentType" in klass.__dict__:
            descriptor = klass.__dict__["contentType"]
            break
    assert isinstance(descriptor, property)

def test_org::aries::common::attachment_has_size():
    assert hasattr(org::aries::common::Attachment, "size")
    descriptor = None
    for klass in org::aries::common::Attachment.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)

def test_org::aries::common::attachment_has_name():
    assert hasattr(org::aries::common::Attachment, "name")
    descriptor = None
    for klass in org::aries::common::Attachment.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_subdivision_exists():
    # Check that the Enumeration exists
    assert SubDivision is not None

def test_subdivision_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SubDivision]
    expected_literals = [
        "HIGHSCHOOL",
        "ELEMENTARYSCHOOL",
        "JRHIGHSCHOOL",
        "ALL",
        "CHILDREN",
        "STUDENT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SubDivision"

def test_role_exists():
    # Check that the Enumeration exists
    assert Role is not None

def test_role_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Role]
    expected_literals = [
        "USER",
        "HOST",
        "MANAGER",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Role"

def test_position_exists():
    # Check that the Enumeration exists
    assert Position is not None

def test_position_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Position]
    expected_literals = [
        "VICEGENERALDIRECTOR",
        "SENIORVICEGENERALDIRECTOR",
        "ADVISOR",
        "MEMBERCAREADVISOR",
        "GENERALDIRECTOR",
        "SOKASPIRITCOORDINATOR",
        "PUBLICATIONSREPRESENTATIVE",
        "MEMBERSHIPDATABASEADMINISTRATOR",
        "LEADER",
        "CULTUREDEPTCOORDINATOR",
        "VICELEADER",
        "MEMBERSHIPSTATISTICSADMINISTRATOR",
        "GUIDANCE",
        "SENIORVICELEADER",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Position"

def test_organizationlevel_exists():
    # Check that the Enumeration exists
    assert OrganizationLevel is not None

def test_organizationlevel_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in OrganizationLevel]
    expected_literals = [
        "SGIUSA",
        "TEAM",
        "CHAPTER",
        "ZONE",
        "AREA",
        "DISTRICT",
        "REGION",
        "GROUP",
        "UNIT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in OrganizationLevel"

def test_schooltype_exists():
    # Check that the Enumeration exists
    assert SchoolType is not None

def test_schooltype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SchoolType]
    expected_literals = [
        "ELEMENTARY",
        "OTHER",
        "COLLEGE",
        "GRAMMER",
        "JRHIGHSCHOOL",
        "GRADUATE",
        "HIGHSCHOOL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SchoolType"

def test_viewtype_exists():
    # Check that the Enumeration exists
    assert ViewType is not None

def test_viewtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ViewType]
    expected_literals = [
        "USERLIST",
        "ORGANIZATIONNODE",
        "MEMBERLIST",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ViewType"

def test_phonenumbertype_exists():
    # Check that the Enumeration exists
    assert PhoneNumberType is not None

def test_phonenumbertype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PhoneNumberType]
    expected_literals = [
        "WORK",
        "CELL",
        "HOME",
        "OTHER",
        "FAX",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PhoneNumberType"

def test_familyrelation_exists():
    # Check that the Enumeration exists
    assert FamilyRelation is not None

def test_familyrelation_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FamilyRelation]
    expected_literals = [
        "SISTER",
        "BROTHER",
        "GRANDSON",
        "OTHER",
        "FATHERINLAW",
        "STEPBROTHER",
        "EXWIFE",
        "SON",
        "EXHUSBAND",
        "NEPHEW",
        "GRANDDAUGHTER",
        "COUSIN",
        "FATHER",
        "WIFE",
        "AUNT",
        "UNCLE",
        "DAUGHTERINLAW",
        "MOTHER",
        "HUSBAND",
        "SONINLAW",
        "GRANDMOTHER",
        "MOTHERINLAW",
        "DAUGHTER",
        "STEPSISTER",
        "NIECE",
        "GRANDFATHER",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FamilyRelation"

def test_divisionname_exists():
    # Check that the Enumeration exists
    assert DivisionName is not None

def test_divisionname_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DivisionName]
    expected_literals = [
        "WomanSDivision",
        "YoungWomenSDivision",
        "none",
        "YouthDivision",
        "AllDivisions",
        "MenSDivision",
        "YoungMenSDivision",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DivisionName"

def test_capability_exists():
    # Check that the Enumeration exists
    assert Capability is not None

def test_capability_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Capability]
    expected_literals = [
        "EXPORT",
        "DELETE",
        "ALL",
        "PRINT",
        "CREATE",
        "EMAIL",
        "UPDATE",
        "NONE",
        "READ",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Capability"

def test_language_exists():
    # Check that the Enumeration exists
    assert Language is not None

def test_language_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Language]
    expected_literals = [
        "SPANISH",
        "ITALIAN",
        "FRENCH",
        "THAI",
        "VIETNAMESE",
        "CHINESE",
        "JAPANESE",
        "OTHER",
        "GERMAN",
        "KOREAN",
        "ENGLISH",
        "PORTUGUESE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Language"

def test_activitygroupname_exists():
    # Check that the Enumeration exists
    assert ActivityGroupName is not None

def test_activitygroupname_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ActivityGroupName]
    expected_literals = [
        "CentralExecutiveCommittee",
        "GoldenStageCrew",
        "Secretariet",
        "YouthPeaceGroup",
        "PhoneToban",
        "BookstoreToban",
        "none",
        "FifeAndDrumCorp",
        "Byakuren",
        "YouthMusicCorp",
        "StudyGroup",
        "YouthSupportGroup",
        "BuildingCommittee",
        "SokaGroup",
        "CultureDept",
        "Gajokai",
        "SokaSpiritGroup",
        "WelcomingCommittee",
        "ChorusGroup",
        "CleanupCommittee",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ActivityGroupName"

def test_country_exists():
    # Check that the Enumeration exists
    assert Country is not None

def test_country_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Country]
    expected_literals = [
        "USA",
        "PR",
        "CAN",
        "MEX",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Country"

def test_eventstatus_exists():
    # Check that the Enumeration exists
    assert EventStatus is not None

def test_eventstatus_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EventStatus]
    expected_literals = [
        "HOST",
        "MANAGER",
        "USER",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EventStatus"

def test_subdivisionname_exists():
    # Check that the Enumeration exists
    assert SubDivisionName is not None

def test_subdivisionname_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SubDivisionName]
    expected_literals = [
        "StudentDivision",
        "ALLSubDivisions",
        "HighSchoolDivision",
        "ElementarySchoolDivision",
        "ChildrenSDivision",
        "JrHighSchoolDivision",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SubDivisionName"

def test_state_exists():
    # Check that the Enumeration exists
    assert State is not None

def test_state_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in State]
    expected_literals = [
        "OR",
        "NH",
        "RI",
        "CO",
        "UT",
        "DE",
        "ID",
        "SC",
        "ME",
        "AL",
        "OK",
        "IN",
        "MO",
        "OH",
        "WV",
        "WY",
        "NV",
        "NM",
        "VT",
        "SD",
        "NC",
        "TN",
        "VA",
        "MN",
        "NY",
        "KY",
        "CT",
        "WI",
        "LA",
        "MT",
        "HI",
        "MI",
        "NJ",
        "MA",
        "PA",
        "AZ",
        "WA",
        "FL",
        "TX",
        "NE",
        "AR",
        "AK",
        "ND",
        "GA",
        "IA",
        "IL",
        "MS",
        "CA",
        "KS",
        "MD",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in State"

def test_status_exists():
    # Check that the Enumeration exists
    assert Status is not None

def test_status_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Status]
    expected_literals = [
        "ERROR",
        "PROMPT",
        "WARNING",
        "INFO",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Status"

def test_studydeptexamlevel_exists():
    # Check that the Enumeration exists
    assert StudyDeptExamLevel is not None

def test_studydeptexamlevel_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in StudyDeptExamLevel]
    expected_literals = [
        "ENTRANCE",
        "POSTGRADUATE",
        "OTHER",
        "GRADUATE",
        "INTERMEDIATE",
        "ADVANCED",
        "ELEMENTARY",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in StudyDeptExamLevel"

def test_studydeptlanguage_exists():
    # Check that the Enumeration exists
    assert StudyDeptLanguage is not None

def test_studydeptlanguage_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in StudyDeptLanguage]
    expected_literals = [
        "FRENCH",
        "KOREAN",
        "OTHER",
        "ENGLISH",
        "CHINESE",
        "PORTUGUESE",
        "JAPANESE",
        "SPANISH",
        "THAI",
        "GERMAN",
        "VIETNAMESE",
        "ITALIAN",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in StudyDeptLanguage"

def test_positionname_exists():
    # Check that the Enumeration exists
    assert PositionName is not None

def test_positionname_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PositionName]
    expected_literals = [
        "MemberCareAdvisor",
        "Leader",
        "SokaSpiritCoordinator",
        "SeniorViceGeneralDirector",
        "Guidance",
        "GeneralDirector",
        "ViceGeneralDirector",
        "Advisor",
        "MembershipStatisticsAdministrator",
        "MembershipDatabaseAdministrator",
        "PublicationsRepresentative",
        "CultureDeptCoordinator",
        "SeniorViceLeader",
        "ViceLeader",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PositionName"

def test_roletype_exists():
    # Check that the Enumeration exists
    assert RoleType is not None

def test_roletype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in RoleType]
    expected_literals = [
        "MANAGER",
        "HOST",
        "USER",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in RoleType"

def test_gohonzontype_exists():
    # Check that the Enumeration exists
    assert GohonzonType is not None

def test_gohonzontype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in GohonzonType]
    expected_literals = [
        "FAMILY",
        "SMALL",
        "OMOMORI",
        "REGULAR",
        "OKATAGI",
        "LARGE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in GohonzonType"

def test_activitygroup_exists():
    # Check that the Enumeration exists
    assert ActivityGroup is not None

def test_activitygroup_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ActivityGroup]
    expected_literals = [
        "YOUTHPEACEGROUP",
        "CHORUSGROUP",
        "BYAKUREN",
        "WELCOMINGCOMMITTEE",
        "YOUTHMUSICCORP",
        "PHONETOBAN",
        "STUDYGROUP",
        "FIFEANDDRUMCORP",
        "BOOKSTORETOBAN",
        "SECRETARIET",
        "BUILDINGCOMMITTEE",
        "NONE",
        "YOUTHSUPPORTGROUP",
        "SOKAGROUP",
        "SOKASPIRITGROUP",
        "GOLDENSTAGECREW",
        "CLEANUPCOMMITTEE",
        "CENTRALEXECUTIVECOMMITTEE",
        "GAJOKAI",
        "CULTUREDEPT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ActivityGroup"

def test_division_exists():
    # Check that the Enumeration exists
    assert Division is not None

def test_division_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Division]
    expected_literals = [
        "WD",
        "MD",
        "NONE",
        "YMD",
        "ALL",
        "YD",
        "YWD",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Division"


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
MembershipInfo_strategy = st.builds(
    MembershipInfo,
)
org::sgiusa::model::EStringToStringMapEntry_strategy = st.builds(
    org::sgiusa::model::EStringToStringMapEntry,
)
org::sgiusa::model::DocumentRoot_strategy = st.builds(
    org::sgiusa::model::DocumentRoot,
    mixed=
        safe_text
)
GohonzonInfo_strategy = st.builds(
    GohonzonInfo,
)
FamilyMember_strategy = st.builds(
    FamilyMember,
)
EmailList_strategy = st.builds(
    EmailList,
)
org::aries::common::User_strategy = st.builds(
    org::aries::common::User,
    lastName=
        safe_text,
    password=
        safe_text,
    firstName=
        safe_text,
    id=
        safe_text,
    enabled=
        safe_text,
    userId=
        safe_text
)
org::aries::common::ZipCode_strategy = st.builds(
    org::aries::common::ZipCode,
    extension=
        safe_text,
    number=
        safe_text,
    country=
        safe_text
)
org::aries::common::StreetAddress_strategy = st.builds(
    org::aries::common::StreetAddress,
    latitude=
        safe_text,
    street=
        safe_text,
    longitude=
        safe_text,
    id=
        safe_text,
    country=
        safe_text,
    city=
        safe_text,
    state=
        safe_text
)
org::aries::common::PhoneNumber_strategy = st.builds(
    org::aries::common::PhoneNumber,
    id=
        safe_text,
    value=
        safe_text,
    number=
        safe_text,
    type=
        safe_text,
    area=
        safe_text,
    extension=
        safe_text,
    country=
        safe_text
)
org::aries::common::Property_strategy = st.builds(
    org::aries::common::Property,
    id=
        safe_text,
    mixed=
        safe_text,
    value=
        safe_text,
    name=
        safe_text
)
org::aries::common::Properties_strategy = st.builds(
    org::aries::common::Properties,
)
org::aries::common::Person_strategy = st.builds(
    org::aries::common::Person,
    userId=
        safe_text,
    id=
        safe_text
)
org::aries::common::PersonName_strategy = st.builds(
    org::aries::common::PersonName,
    firstName=
        safe_text,
    middleInitial=
        safe_text,
    lastName=
        safe_text
)
org::sgiusa::model::View_strategy = st.builds(
    org::sgiusa::model::View,
    viewType=
        safe_text,
    userId=
        safe_text,
    id=
        safe_text
)
org::sgiusa::model::Users_strategy = st.builds(
    org::sgiusa::model::Users,
)
org::sgiusa::model::StudyDeptInfo_strategy = st.builds(
    org::sgiusa::model::StudyDeptInfo,
    lastUpdate=
        safe_text,
    id=
        safe_text
)
org::sgiusa::model::User_strategy = st.builds(
    org::sgiusa::model::User,
    id=
        safe_text,
    enabled=
        safe_text,
    userId=
        safe_text,
    lastName=
        safe_text,
    role=
        safe_text,
    password=
        safe_text,
    firstName=
        safe_text
)
org::sgiusa::model::StudyDeptExam_strategy = st.builds(
    org::sgiusa::model::StudyDeptExam,
    examLevel=
        safe_text,
    current=
        safe_text,
    examDate=
        safe_text,
    examLanguage=
        safe_text,
    lastUpdate=
        safe_text,
    examLocation=
        safe_text,
    id=
        safe_text
)
org::sgiusa::model::Registration_strategy = st.builds(
    org::sgiusa::model::Registration,
    cancelled=
        safe_text,
    aborted=
        safe_text,
    date=
        safe_text,
    id=
        safe_text
)
org::sgiusa::model::SchoolInfo_strategy = st.builds(
    org::sgiusa::model::SchoolInfo,
    id=
        safe_text,
    fieldOfStudy=
        safe_text,
    endDate=
        safe_text,
    schoolName=
        safe_text,
    lastUpdate=
        safe_text,
    startDate=
        safe_text,
    schoolType=
        safe_text
)
org::sgiusa::model::Preferences_strategy = st.builds(
    org::sgiusa::model::Preferences,
    id=
        safe_text,
    themeId=
        safe_text,
    enableTooltips=
        safe_text,
    selectedView=
        safe_text,
    openNodes=
        safe_text,
    userId=
        safe_text,
    openViews=
        safe_text,
    selectedNode=
        safe_text
)
org::sgiusa::model::Permission_strategy = st.builds(
    org::sgiusa::model::Permission,
    capabilities=
        safe_text,
    activityGroups=
        safe_text,
    userId=
        safe_text,
    enabled=
        safe_text,
    divisions=
        safe_text,
    subDivisions=
        safe_text,
    id=
        safe_text
)
org::sgiusa::model::Organization_strategy = st.builds(
    org::sgiusa::model::Organization,
    level=
        safe_text,
    permissionId=
        safe_text,
    abbrv=
        safe_text,
    lastUpdate=
        safe_text,
    id=
        safe_text,
    organizationId=
        safe_text,
    creationDate=
        safe_text,
    zipCodes=
        safe_text,
    type=
        safe_text,
    label=
        safe_text,
    name=
        safe_text
)
org::sgiusa::model::MembershipInfo_strategy = st.builds(
    org::sgiusa::model::MembershipInfo,
    friendOfSgi=
        safe_text,
    notLocatable=
        safe_text,
    id=
        safe_text,
    receivedCertificate=
        safe_text,
    notActivated=
        safe_text,
    lastUpdate=
        safe_text
)
org::sgiusa::model::Note_strategy = st.builds(
    org::sgiusa::model::Note,
    id=
        safe_text,
    lastUpdate=
        safe_text,
    text=
        safe_text,
    creationDate=
        safe_text
)
org::sgiusa::model::Members_strategy = st.builds(
    org::sgiusa::model::Members,
)
org::sgiusa::model::MemberSearchCriteria_strategy = st.builds(
    org::sgiusa::model::MemberSearchCriteria,
    divisions=
        safe_text,
    activityGroups=
        safe_text,
    subDivisions=
        safe_text
)
org::sgiusa::model::Member_strategy = st.builds(
    org::sgiusa::model::Member,
    archived=
        safe_text,
    firstName=
        safe_text,
    extraField2=
        safe_text,
    joinDate=
        safe_text,
    employer=
        safe_text,
    visible=
        safe_text,
    birthDate=
        safe_text,
    statusProfile=
        safe_text,
    extraField1=
        safe_text,
    id=
        safe_text,
    locatable=
        safe_text,
    occupation=
        safe_text,
    lastName=
        safe_text,
    middleInitial=
        safe_text,
    interests=
        safe_text,
    activityGroups=
        safe_text,
    languages=
        safe_text,
    subDivision=
        safe_text,
    division=
        safe_text
)
org::sgiusa::model::LeadershipInfo_strategy = st.builds(
    org::sgiusa::model::LeadershipInfo,
    manualSigned=
        safe_text,
    examPassedDate=
        safe_text,
    examPassed=
        safe_text,
    lastUpdate=
        safe_text,
    manualSignedDate=
        safe_text,
    id=
        safe_text
)
org::sgiusa::model::LeadershipRole_strategy = st.builds(
    org::sgiusa::model::LeadershipRole,
    level=
        safe_text,
    lastUpdate=
        safe_text,
    position=
        safe_text,
    subDivision=
        safe_text,
    active=
        safe_text,
    division=
        safe_text,
    activityGroup=
        safe_text,
    startDate=
        safe_text,
    endDate=
        safe_text,
    id=
        safe_text
)
org::sgiusa::model::GohonzonInfo_strategy = st.builds(
    org::sgiusa::model::GohonzonInfo,
    lastUpdate=
        safe_text,
    returned=
        safe_text,
    id=
        safe_text,
    returnDate=
        safe_text,
    gohonzonType=
        safe_text,
    receiveDate=
        safe_text
)
org::sgiusa::model::FamilyMember_strategy = st.builds(
    org::sgiusa::model::FamilyMember,
    personName=
        safe_text,
    lastUpdate=
        safe_text,
    familyRelation=
        safe_text,
    id=
        safe_text,
    sgiMember=
        safe_text
)
org::sgiusa::model::Event_strategy = st.builds(
    org::sgiusa::model::Event,
    id=
        safe_text,
    divisions=
        safe_text,
    status=
        safe_text,
    subDivisions=
        safe_text,
    userId=
        safe_text
)
StudyDeptInfo_strategy = st.builds(
    StudyDeptInfo,
)
StudyDeptExam_strategy = st.builds(
    StudyDeptExam,
)
SchoolInfo_strategy = st.builds(
    SchoolInfo,
)
Registration_strategy = st.builds(
    Registration,
)
org::sgiusa::model::EmailList_strategy = st.builds(
    org::sgiusa::model::EmailList,
    divisions=
        safe_text,
    id=
        safe_text,
    subDivisions=
        safe_text,
    enabled=
        safe_text,
    activityGroups=
        safe_text
)
View_strategy = st.builds(
    View,
)
Users_strategy = st.builds(
    Users,
)
MemberSearchCriteria_strategy = st.builds(
    MemberSearchCriteria,
)
Members_strategy = st.builds(
    Members,
)
Member_strategy = st.builds(
    Member,
)
LeadershipRole_strategy = st.builds(
    LeadershipRole,
)
LeadershipInfo_strategy = st.builds(
    LeadershipInfo,
)
Preferences_strategy = st.builds(
    Preferences,
)
Permission_strategy = st.builds(
    Permission,
)
Organization_strategy = st.builds(
    Organization,
)
org::aries::common::EObject_strategy = st.builds(
    org::aries::common::EObject,
)
org::aries::common::MapEntry_strategy = st.builds(
    org::aries::common::MapEntry,
)
org::aries::common::Map_strategy = st.builds(
    org::aries::common::Map,
)
org::aries::common::Note_strategy = st.builds(
    org::aries::common::Note,
    lastUpdate=
        safe_text,
    id=
        safe_text,
    creationDate=
        safe_text,
    text=
        safe_text
)
org::aries::common::Event_strategy = st.builds(
    org::aries::common::Event,
    id=
        safe_text
)
org::aries::common::EmailMessage_strategy = st.builds(
    org::aries::common::EmailMessage,
    sourceId=
        safe_text,
    smtpHost=
        safe_text,
    content=
        safe_text,
    sendAsHtml=
        safe_text,
    smtpPort=
        safe_text,
    timestamp=
        safe_text,
    id=
        safe_text,
    subject=
        safe_text
)
org::aries::common::EmailBox_strategy = st.builds(
    org::aries::common::EmailBox,
    creationDate=
        safe_text,
    name=
        safe_text,
    id=
        safe_text,
    type=
        safe_text,
    lastUpdate=
        safe_text
)
org::aries::common::EmailAddressList_strategy = st.builds(
    org::aries::common::EmailAddressList,
    emailAddress=
        safe_text,
    name=
        safe_text
)
org::aries::common::EmailAddress_strategy = st.builds(
    org::aries::common::EmailAddress,
    creationDate=
        safe_text,
    id=
        safe_text,
    enabled=
        safe_text,
    organization=
        safe_text,
    lastUpdate=
        safe_text,
    userId=
        safe_text,
    url=
        safe_text,
    firstName=
        safe_text,
    lastName=
        safe_text
)
org::aries::common::EmailAccount_strategy = st.builds(
    org::aries::common::EmailAccount,
    enabled=
        safe_text,
    password=
        safe_text,
    id=
        safe_text,
    lastName=
        safe_text,
    firstName=
        safe_text,
    userId=
        safe_text
)
ZipCode_strategy = st.builds(
    ZipCode,
)
User_strategy = st.builds(
    User,
)
StreetAddress_strategy = st.builds(
    StreetAddress,
)
PersonName_strategy = st.builds(
    PersonName,
)
Person_strategy = st.builds(
    Person,
)
Note_strategy = st.builds(
    Note,
)
MapEntry_strategy = st.builds(
    MapEntry,
)
Property_strategy = st.builds(
    Property,
)
Properties_strategy = st.builds(
    Properties,
)
PhoneNumber_strategy = st.builds(
    PhoneNumber,
)
EmailMessage_strategy = st.builds(
    EmailMessage,
)
EmailBox_strategy = st.builds(
    EmailBox,
)
EmailAddressList_strategy = st.builds(
    EmailAddressList,
)
EmailAddress_strategy = st.builds(
    EmailAddress,
)
Map_strategy = st.builds(
    Map,
)
Event_strategy = st.builds(
    Event,
)
org::aries::common::EStringToStringMapEntry_strategy = st.builds(
    org::aries::common::EStringToStringMapEntry,
)
org::aries::common::DocumentRoot_strategy = st.builds(
    org::aries::common::DocumentRoot,
    mixed=
        safe_text
)
EmailAccount_strategy = st.builds(
    EmailAccount,
)
Attachment_strategy = st.builds(
    Attachment,
)
org::aries::common::Attachment_strategy = st.builds(
    org::aries::common::Attachment,
    id=
        safe_text,
    fileData=
        safe_text,
    fileName=
        safe_text,
    contentType=
        safe_text,
    size=
        safe_text,
    name=
        safe_text
)

@given(instance=MembershipInfo_strategy)
@settings(max_examples=50)
def test_membershipinfo_instantiation(instance):
    assert isinstance(instance, MembershipInfo)

@given(instance=org::sgiusa::model::EStringToStringMapEntry_strategy)
@settings(max_examples=50)
def test_org::sgiusa::model::estringtostringmapentry_instantiation(instance):
    assert isinstance(instance, org::sgiusa::model::EStringToStringMapEntry)

@given(instance=org::sgiusa::model::DocumentRoot_strategy)
@settings(max_examples=50)
def test_org::sgiusa::model::documentroot_instantiation(instance):
    assert isinstance(instance, org::sgiusa::model::DocumentRoot)

@given(instance=org::sgiusa::model::DocumentRoot_strategy)
def test_org::sgiusa::model::documentroot_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=org::sgiusa::model::DocumentRoot_strategy)
def test_org::sgiusa::model::documentroot_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=GohonzonInfo_strategy)
@settings(max_examples=50)
def test_gohonzoninfo_instantiation(instance):
    assert isinstance(instance, GohonzonInfo)

@given(instance=FamilyMember_strategy)
@settings(max_examples=50)
def test_familymember_instantiation(instance):
    assert isinstance(instance, FamilyMember)

@given(instance=EmailList_strategy)
@settings(max_examples=50)
def test_emaillist_instantiation(instance):
    assert isinstance(instance, EmailList)

@given(instance=org::aries::common::User_strategy)
@settings(max_examples=50)
def test_org::aries::common::user_instantiation(instance):
    assert isinstance(instance, org::aries::common::User)

@given(instance=org::aries::common::User_strategy)
def test_org::aries::common::user_lastName_type(instance):
    assert isinstance(instance.lastName, str)


@given(instance=org::aries::common::User_strategy)
def test_org::aries::common::user_lastName_setter(instance):
    original = instance.lastName
    instance.lastName = original
    assert instance.lastName == original

@given(instance=org::aries::common::User_strategy)
def test_org::aries::common::user_password_type(instance):
    assert isinstance(instance.password, str)


@given(instance=org::aries::common::User_strategy)
def test_org::aries::common::user_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original

@given(instance=org::aries::common::User_strategy)
def test_org::aries::common::user_firstName_type(instance):
    assert isinstance(instance.firstName, str)


@given(instance=org::aries::common::User_strategy)
def test_org::aries::common::user_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original

@given(instance=org::aries::common::User_strategy)
def test_org::aries::common::user_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=org::aries::common::User_strategy)
def test_org::aries::common::user_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=org::aries::common::User_strategy)
def test_org::aries::common::user_enabled_type(instance):
    assert isinstance(instance.enabled, str)


@given(instance=org::aries::common::User_strategy)
def test_org::aries::common::user_enabled_setter(instance):
    original = instance.enabled
    instance.enabled = original
    assert instance.enabled == original

@given(instance=org::aries::common::User_strategy)
def test_org::aries::common::user_userId_type(instance):
    assert isinstance(instance.userId, str)


@given(instance=org::aries::common::User_strategy)
def test_org::aries::common::user_userId_setter(instance):
    original = instance.userId
    instance.userId = original
    assert instance.userId == original

@given(instance=org::aries::common::ZipCode_strategy)
@settings(max_examples=50)
def test_org::aries::common::zipcode_instantiation(instance):
    assert isinstance(instance, org::aries::common::ZipCode)

@given(instance=org::aries::common::ZipCode_strategy)
def test_org::aries::common::zipcode_extension_type(instance):
    assert isinstance(instance.extension, str)


@given(instance=org::aries::common::ZipCode_strategy)
def test_org::aries::common::zipcode_extension_setter(instance):
    original = instance.extension
    instance.extension = original
    assert instance.extension == original

@given(instance=org::aries::common::ZipCode_strategy)
def test_org::aries::common::zipcode_number_type(instance):
    assert isinstance(instance.number, str)


@given(instance=org::aries::common::ZipCode_strategy)
def test_org::aries::common::zipcode_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original

@given(instance=org::aries::common::ZipCode_strategy)
def test_org::aries::common::zipcode_country_type(instance):
    assert isinstance(instance.country, str)


@given(instance=org::aries::common::ZipCode_strategy)
def test_org::aries::common::zipcode_country_setter(instance):
    original = instance.country
    instance.country = original
    assert instance.country == original

@given(instance=org::aries::common::StreetAddress_strategy)
@settings(max_examples=50)
def test_org::aries::common::streetaddress_instantiation(instance):
    assert isinstance(instance, org::aries::common::StreetAddress)

@given(instance=org::aries::common::StreetAddress_strategy)
def test_org::aries::common::streetaddress_latitude_type(instance):
    assert isinstance(instance.latitude, str)


@given(instance=org::aries::common::StreetAddress_strategy)
def test_org::aries::common::streetaddress_latitude_setter(instance):
    original = instance.latitude
    instance.latitude = original
    assert instance.latitude == original

@given(instance=org::aries::common::StreetAddress_strategy)
def test_org::aries::common::streetaddress_street_type(instance):
    assert isinstance(instance.street, str)


@given(instance=org::aries::common::StreetAddress_strategy)
def test_org::aries::common::streetaddress_street_setter(instance):
    original = instance.street
    instance.street = original
    assert instance.street == original

@given(instance=org::aries::common::StreetAddress_strategy)
def test_org::aries::common::streetaddress_longitude_type(instance):
    assert isinstance(instance.longitude, str)


@given(instance=org::aries::common::StreetAddress_strategy)
def test_org::aries::common::streetaddress_longitude_setter(instance):
    original = instance.longitude
    instance.longitude = original
    assert instance.longitude == original

@given(instance=org::aries::common::StreetAddress_strategy)
def test_org::aries::common::streetaddress_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=org::aries::common::StreetAddress_strategy)
def test_org::aries::common::streetaddress_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=org::aries::common::StreetAddress_strategy)
def test_org::aries::common::streetaddress_country_type(instance):
    assert isinstance(instance.country, str)


@given(instance=org::aries::common::StreetAddress_strategy)
def test_org::aries::common::streetaddress_country_setter(instance):
    original = instance.country
    instance.country = original
    assert instance.country == original

@given(instance=org::aries::common::StreetAddress_strategy)
def test_org::aries::common::streetaddress_city_type(instance):
    assert isinstance(instance.city, str)


@given(instance=org::aries::common::StreetAddress_strategy)
def test_org::aries::common::streetaddress_city_setter(instance):
    original = instance.city
    instance.city = original
    assert instance.city == original

@given(instance=org::aries::common::StreetAddress_strategy)
def test_org::aries::common::streetaddress_state_type(instance):
    assert isinstance(instance.state, str)


@given(instance=org::aries::common::StreetAddress_strategy)
def test_org::aries::common::streetaddress_state_setter(instance):
    original = instance.state
    instance.state = original
    assert instance.state == original

@given(instance=org::aries::common::PhoneNumber_strategy)
@settings(max_examples=50)
def test_org::aries::common::phonenumber_instantiation(instance):
    assert isinstance(instance, org::aries::common::PhoneNumber)

@given(instance=org::aries::common::PhoneNumber_strategy)
def test_org::aries::common::phonenumber_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=org::aries::common::PhoneNumber_strategy)
def test_org::aries::common::phonenumber_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=org::aries::common::PhoneNumber_strategy)
def test_org::aries::common::phonenumber_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=org::aries::common::PhoneNumber_strategy)
def test_org::aries::common::phonenumber_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=org::aries::common::PhoneNumber_strategy)
def test_org::aries::common::phonenumber_number_type(instance):
    assert isinstance(instance.number, str)


@given(instance=org::aries::common::PhoneNumber_strategy)
def test_org::aries::common::phonenumber_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original

@given(instance=org::aries::common::PhoneNumber_strategy)
def test_org::aries::common::phonenumber_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=org::aries::common::PhoneNumber_strategy)
def test_org::aries::common::phonenumber_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=org::aries::common::PhoneNumber_strategy)
def test_org::aries::common::phonenumber_area_type(instance):
    assert isinstance(instance.area, str)


@given(instance=org::aries::common::PhoneNumber_strategy)
def test_org::aries::common::phonenumber_area_setter(instance):
    original = instance.area
    instance.area = original
    assert instance.area == original

@given(instance=org::aries::common::PhoneNumber_strategy)
def test_org::aries::common::phonenumber_extension_type(instance):
    assert isinstance(instance.extension, str)


@given(instance=org::aries::common::PhoneNumber_strategy)
def test_org::aries::common::phonenumber_extension_setter(instance):
    original = instance.extension
    instance.extension = original
    assert instance.extension == original

@given(instance=org::aries::common::PhoneNumber_strategy)
def test_org::aries::common::phonenumber_country_type(instance):
    assert isinstance(instance.country, str)


@given(instance=org::aries::common::PhoneNumber_strategy)
def test_org::aries::common::phonenumber_country_setter(instance):
    original = instance.country
    instance.country = original
    assert instance.country == original

@given(instance=org::aries::common::Property_strategy)
@settings(max_examples=50)
def test_org::aries::common::property_instantiation(instance):
    assert isinstance(instance, org::aries::common::Property)

@given(instance=org::aries::common::Property_strategy)
def test_org::aries::common::property_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=org::aries::common::Property_strategy)
def test_org::aries::common::property_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=org::aries::common::Property_strategy)
def test_org::aries::common::property_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=org::aries::common::Property_strategy)
def test_org::aries::common::property_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=org::aries::common::Property_strategy)
def test_org::aries::common::property_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=org::aries::common::Property_strategy)
def test_org::aries::common::property_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=org::aries::common::Property_strategy)
def test_org::aries::common::property_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=org::aries::common::Property_strategy)
def test_org::aries::common::property_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=org::aries::common::Properties_strategy)
@settings(max_examples=50)
def test_org::aries::common::properties_instantiation(instance):
    assert isinstance(instance, org::aries::common::Properties)

@given(instance=org::aries::common::Person_strategy)
@settings(max_examples=50)
def test_org::aries::common::person_instantiation(instance):
    assert isinstance(instance, org::aries::common::Person)

@given(instance=org::aries::common::Person_strategy)
def test_org::aries::common::person_userId_type(instance):
    assert isinstance(instance.userId, str)


@given(instance=org::aries::common::Person_strategy)
def test_org::aries::common::person_userId_setter(instance):
    original = instance.userId
    instance.userId = original
    assert instance.userId == original

@given(instance=org::aries::common::Person_strategy)
def test_org::aries::common::person_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=org::aries::common::Person_strategy)
def test_org::aries::common::person_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=org::aries::common::PersonName_strategy)
@settings(max_examples=50)
def test_org::aries::common::personname_instantiation(instance):
    assert isinstance(instance, org::aries::common::PersonName)

@given(instance=org::aries::common::PersonName_strategy)
def test_org::aries::common::personname_firstName_type(instance):
    assert isinstance(instance.firstName, str)


@given(instance=org::aries::common::PersonName_strategy)
def test_org::aries::common::personname_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original

@given(instance=org::aries::common::PersonName_strategy)
def test_org::aries::common::personname_middleInitial_type(instance):
    assert isinstance(instance.middleInitial, str)


@given(instance=org::aries::common::PersonName_strategy)
def test_org::aries::common::personname_middleInitial_setter(instance):
    original = instance.middleInitial
    instance.middleInitial = original
    assert instance.middleInitial == original

@given(instance=org::aries::common::PersonName_strategy)
def test_org::aries::common::personname_lastName_type(instance):
    assert isinstance(instance.lastName, str)


@given(instance=org::aries::common::PersonName_strategy)
def test_org::aries::common::personname_lastName_setter(instance):
    original = instance.lastName
    instance.lastName = original
    assert instance.lastName == original

@given(instance=org::sgiusa::model::View_strategy)
@settings(max_examples=50)
def test_org::sgiusa::model::view_instantiation(instance):
    assert isinstance(instance, org::sgiusa::model::View)

@given(instance=org::sgiusa::model::View_strategy)
def test_org::sgiusa::model::view_viewType_type(instance):
    assert isinstance(instance.viewType, str)


@given(instance=org::sgiusa::model::View_strategy)
def test_org::sgiusa::model::view_viewType_setter(instance):
    original = instance.viewType
    instance.viewType = original
    assert instance.viewType == original

@given(instance=org::sgiusa::model::View_strategy)
def test_org::sgiusa::model::view_userId_type(instance):
    assert isinstance(instance.userId, str)


@given(instance=org::sgiusa::model::View_strategy)
def test_org::sgiusa::model::view_userId_setter(instance):
    original = instance.userId
    instance.userId = original
    assert instance.userId == original

@given(instance=org::sgiusa::model::View_strategy)
def test_org::sgiusa::model::view_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=org::sgiusa::model::View_strategy)
def test_org::sgiusa::model::view_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=org::sgiusa::model::Users_strategy)
@settings(max_examples=50)
def test_org::sgiusa::model::users_instantiation(instance):
    assert isinstance(instance, org::sgiusa::model::Users)

@given(instance=org::sgiusa::model::StudyDeptInfo_strategy)
@settings(max_examples=50)
def test_org::sgiusa::model::studydeptinfo_instantiation(instance):
    assert isinstance(instance, org::sgiusa::model::StudyDeptInfo)

@given(instance=org::sgiusa::model::StudyDeptInfo_strategy)
def test_org::sgiusa::model::studydeptinfo_lastUpdate_type(instance):
    assert isinstance(instance.lastUpdate, str)


@given(instance=org::sgiusa::model::StudyDeptInfo_strategy)
def test_org::sgiusa::model::studydeptinfo_lastUpdate_setter(instance):
    original = instance.lastUpdate
    instance.lastUpdate = original
    assert instance.lastUpdate == original

@given(instance=org::sgiusa::model::StudyDeptInfo_strategy)
def test_org::sgiusa::model::studydeptinfo_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=org::sgiusa::model::StudyDeptInfo_strategy)
def test_org::sgiusa::model::studydeptinfo_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=org::sgiusa::model::User_strategy)
@settings(max_examples=50)
def test_org::sgiusa::model::user_instantiation(instance):
    assert isinstance(instance, org::sgiusa::model::User)

@given(instance=org::sgiusa::model::User_strategy)
def test_org::sgiusa::model::user_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=org::sgiusa::model::User_strategy)
def test_org::sgiusa::model::user_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=org::sgiusa::model::User_strategy)
def test_org::sgiusa::model::user_enabled_type(instance):
    assert isinstance(instance.enabled, str)


@given(instance=org::sgiusa::model::User_strategy)
def test_org::sgiusa::model::user_enabled_setter(instance):
    original = instance.enabled
    instance.enabled = original
    assert instance.enabled == original

@given(instance=org::sgiusa::model::User_strategy)
def test_org::sgiusa::model::user_userId_type(instance):
    assert isinstance(instance.userId, str)


@given(instance=org::sgiusa::model::User_strategy)
def test_org::sgiusa::model::user_userId_setter(instance):
    original = instance.userId
    instance.userId = original
    assert instance.userId == original

@given(instance=org::sgiusa::model::User_strategy)
def test_org::sgiusa::model::user_lastName_type(instance):
    assert isinstance(instance.lastName, str)


@given(instance=org::sgiusa::model::User_strategy)
def test_org::sgiusa::model::user_lastName_setter(instance):
    original = instance.lastName
    instance.lastName = original
    assert instance.lastName == original

@given(instance=org::sgiusa::model::User_strategy)
def test_org::sgiusa::model::user_role_type(instance):
    assert isinstance(instance.role, str)


@given(instance=org::sgiusa::model::User_strategy)
def test_org::sgiusa::model::user_role_setter(instance):
    original = instance.role
    instance.role = original
    assert instance.role == original

@given(instance=org::sgiusa::model::User_strategy)
def test_org::sgiusa::model::user_password_type(instance):
    assert isinstance(instance.password, str)


@given(instance=org::sgiusa::model::User_strategy)
def test_org::sgiusa::model::user_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original

@given(instance=org::sgiusa::model::User_strategy)
def test_org::sgiusa::model::user_firstName_type(instance):
    assert isinstance(instance.firstName, str)


@given(instance=org::sgiusa::model::User_strategy)
def test_org::sgiusa::model::user_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original

@given(instance=org::sgiusa::model::StudyDeptExam_strategy)
@settings(max_examples=50)
def test_org::sgiusa::model::studydeptexam_instantiation(instance):
    assert isinstance(instance, org::sgiusa::model::StudyDeptExam)

@given(instance=org::sgiusa::model::StudyDeptExam_strategy)
def test_org::sgiusa::model::studydeptexam_examLevel_type(instance):
    assert isinstance(instance.examLevel, str)


@given(instance=org::sgiusa::model::StudyDeptExam_strategy)
def test_org::sgiusa::model::studydeptexam_examLevel_setter(instance):
    original = instance.examLevel
    instance.examLevel = original
    assert instance.examLevel == original

@given(instance=org::sgiusa::model::StudyDeptExam_strategy)
def test_org::sgiusa::model::studydeptexam_current_type(instance):
    assert isinstance(instance.current, str)


@given(instance=org::sgiusa::model::StudyDeptExam_strategy)
def test_org::sgiusa::model::studydeptexam_current_setter(instance):
    original = instance.current
    instance.current = original
    assert instance.current == original

@given(instance=org::sgiusa::model::StudyDeptExam_strategy)
def test_org::sgiusa::model::studydeptexam_examDate_type(instance):
    assert isinstance(instance.examDate, str)


@given(instance=org::sgiusa::model::StudyDeptExam_strategy)
def test_org::sgiusa::model::studydeptexam_examDate_setter(instance):
    original = instance.examDate
    instance.examDate = original
    assert instance.examDate == original

@given(instance=org::sgiusa::model::StudyDeptExam_strategy)
def test_org::sgiusa::model::studydeptexam_examLanguage_type(instance):
    assert isinstance(instance.examLanguage, str)


@given(instance=org::sgiusa::model::StudyDeptExam_strategy)
def test_org::sgiusa::model::studydeptexam_examLanguage_setter(instance):
    original = instance.examLanguage
    instance.examLanguage = original
    assert instance.examLanguage == original

@given(instance=org::sgiusa::model::StudyDeptExam_strategy)
def test_org::sgiusa::model::studydeptexam_lastUpdate_type(instance):
    assert isinstance(instance.lastUpdate, str)


@given(instance=org::sgiusa::model::StudyDeptExam_strategy)
def test_org::sgiusa::model::studydeptexam_lastUpdate_setter(instance):
    original = instance.lastUpdate
    instance.lastUpdate = original
    assert instance.lastUpdate == original

@given(instance=org::sgiusa::model::StudyDeptExam_strategy)
def test_org::sgiusa::model::studydeptexam_examLocation_type(instance):
    assert isinstance(instance.examLocation, str)


@given(instance=org::sgiusa::model::StudyDeptExam_strategy)
def test_org::sgiusa::model::studydeptexam_examLocation_setter(instance):
    original = instance.examLocation
    instance.examLocation = original
    assert instance.examLocation == original

@given(instance=org::sgiusa::model::StudyDeptExam_strategy)
def test_org::sgiusa::model::studydeptexam_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=org::sgiusa::model::StudyDeptExam_strategy)
def test_org::sgiusa::model::studydeptexam_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=org::sgiusa::model::Registration_strategy)
@settings(max_examples=50)
def test_org::sgiusa::model::registration_instantiation(instance):
    assert isinstance(instance, org::sgiusa::model::Registration)

@given(instance=org::sgiusa::model::Registration_strategy)
def test_org::sgiusa::model::registration_cancelled_type(instance):
    assert isinstance(instance.cancelled, str)


@given(instance=org::sgiusa::model::Registration_strategy)
def test_org::sgiusa::model::registration_cancelled_setter(instance):
    original = instance.cancelled
    instance.cancelled = original
    assert instance.cancelled == original

@given(instance=org::sgiusa::model::Registration_strategy)
def test_org::sgiusa::model::registration_aborted_type(instance):
    assert isinstance(instance.aborted, str)


@given(instance=org::sgiusa::model::Registration_strategy)
def test_org::sgiusa::model::registration_aborted_setter(instance):
    original = instance.aborted
    instance.aborted = original
    assert instance.aborted == original

@given(instance=org::sgiusa::model::Registration_strategy)
def test_org::sgiusa::model::registration_date_type(instance):
    assert isinstance(instance.date, str)


@given(instance=org::sgiusa::model::Registration_strategy)
def test_org::sgiusa::model::registration_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original

@given(instance=org::sgiusa::model::Registration_strategy)
def test_org::sgiusa::model::registration_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=org::sgiusa::model::Registration_strategy)
def test_org::sgiusa::model::registration_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=org::sgiusa::model::SchoolInfo_strategy)
@settings(max_examples=50)
def test_org::sgiusa::model::schoolinfo_instantiation(instance):
    assert isinstance(instance, org::sgiusa::model::SchoolInfo)

@given(instance=org::sgiusa::model::SchoolInfo_strategy)
def test_org::sgiusa::model::schoolinfo_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=org::sgiusa::model::SchoolInfo_strategy)
def test_org::sgiusa::model::schoolinfo_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=org::sgiusa::model::SchoolInfo_strategy)
def test_org::sgiusa::model::schoolinfo_fieldOfStudy_type(instance):
    assert isinstance(instance.fieldOfStudy, str)


@given(instance=org::sgiusa::model::SchoolInfo_strategy)
def test_org::sgiusa::model::schoolinfo_fieldOfStudy_setter(instance):
    original = instance.fieldOfStudy
    instance.fieldOfStudy = original
    assert instance.fieldOfStudy == original

@given(instance=org::sgiusa::model::SchoolInfo_strategy)
def test_org::sgiusa::model::schoolinfo_endDate_type(instance):
    assert isinstance(instance.endDate, str)


@given(instance=org::sgiusa::model::SchoolInfo_strategy)
def test_org::sgiusa::model::schoolinfo_endDate_setter(instance):
    original = instance.endDate
    instance.endDate = original
    assert instance.endDate == original

@given(instance=org::sgiusa::model::SchoolInfo_strategy)
def test_org::sgiusa::model::schoolinfo_schoolName_type(instance):
    assert isinstance(instance.schoolName, str)


@given(instance=org::sgiusa::model::SchoolInfo_strategy)
def test_org::sgiusa::model::schoolinfo_schoolName_setter(instance):
    original = instance.schoolName
    instance.schoolName = original
    assert instance.schoolName == original

@given(instance=org::sgiusa::model::SchoolInfo_strategy)
def test_org::sgiusa::model::schoolinfo_lastUpdate_type(instance):
    assert isinstance(instance.lastUpdate, str)


@given(instance=org::sgiusa::model::SchoolInfo_strategy)
def test_org::sgiusa::model::schoolinfo_lastUpdate_setter(instance):
    original = instance.lastUpdate
    instance.lastUpdate = original
    assert instance.lastUpdate == original

@given(instance=org::sgiusa::model::SchoolInfo_strategy)
def test_org::sgiusa::model::schoolinfo_startDate_type(instance):
    assert isinstance(instance.startDate, str)


@given(instance=org::sgiusa::model::SchoolInfo_strategy)
def test_org::sgiusa::model::schoolinfo_startDate_setter(instance):
    original = instance.startDate
    instance.startDate = original
    assert instance.startDate == original

@given(instance=org::sgiusa::model::SchoolInfo_strategy)
def test_org::sgiusa::model::schoolinfo_schoolType_type(instance):
    assert isinstance(instance.schoolType, str)


@given(instance=org::sgiusa::model::SchoolInfo_strategy)
def test_org::sgiusa::model::schoolinfo_schoolType_setter(instance):
    original = instance.schoolType
    instance.schoolType = original
    assert instance.schoolType == original

@given(instance=org::sgiusa::model::Preferences_strategy)
@settings(max_examples=50)
def test_org::sgiusa::model::preferences_instantiation(instance):
    assert isinstance(instance, org::sgiusa::model::Preferences)

@given(instance=org::sgiusa::model::Preferences_strategy)
def test_org::sgiusa::model::preferences_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=org::sgiusa::model::Preferences_strategy)
def test_org::sgiusa::model::preferences_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=org::sgiusa::model::Preferences_strategy)
def test_org::sgiusa::model::preferences_themeId_type(instance):
    assert isinstance(instance.themeId, str)


@given(instance=org::sgiusa::model::Preferences_strategy)
def test_org::sgiusa::model::preferences_themeId_setter(instance):
    original = instance.themeId
    instance.themeId = original
    assert instance.themeId == original

@given(instance=org::sgiusa::model::Preferences_strategy)
def test_org::sgiusa::model::preferences_enableTooltips_type(instance):
    assert isinstance(instance.enableTooltips, str)


@given(instance=org::sgiusa::model::Preferences_strategy)
def test_org::sgiusa::model::preferences_enableTooltips_setter(instance):
    original = instance.enableTooltips
    instance.enableTooltips = original
    assert instance.enableTooltips == original

@given(instance=org::sgiusa::model::Preferences_strategy)
def test_org::sgiusa::model::preferences_selectedView_type(instance):
    assert isinstance(instance.selectedView, str)


@given(instance=org::sgiusa::model::Preferences_strategy)
def test_org::sgiusa::model::preferences_selectedView_setter(instance):
    original = instance.selectedView
    instance.selectedView = original
    assert instance.selectedView == original

@given(instance=org::sgiusa::model::Preferences_strategy)
def test_org::sgiusa::model::preferences_openNodes_type(instance):
    assert isinstance(instance.openNodes, str)


@given(instance=org::sgiusa::model::Preferences_strategy)
def test_org::sgiusa::model::preferences_openNodes_setter(instance):
    original = instance.openNodes
    instance.openNodes = original
    assert instance.openNodes == original

@given(instance=org::sgiusa::model::Preferences_strategy)
def test_org::sgiusa::model::preferences_userId_type(instance):
    assert isinstance(instance.userId, str)


@given(instance=org::sgiusa::model::Preferences_strategy)
def test_org::sgiusa::model::preferences_userId_setter(instance):
    original = instance.userId
    instance.userId = original
    assert instance.userId == original

@given(instance=org::sgiusa::model::Preferences_strategy)
def test_org::sgiusa::model::preferences_openViews_type(instance):
    assert isinstance(instance.openViews, str)


@given(instance=org::sgiusa::model::Preferences_strategy)
def test_org::sgiusa::model::preferences_openViews_setter(instance):
    original = instance.openViews
    instance.openViews = original
    assert instance.openViews == original

@given(instance=org::sgiusa::model::Preferences_strategy)
def test_org::sgiusa::model::preferences_selectedNode_type(instance):
    assert isinstance(instance.selectedNode, str)


@given(instance=org::sgiusa::model::Preferences_strategy)
def test_org::sgiusa::model::preferences_selectedNode_setter(instance):
    original = instance.selectedNode
    instance.selectedNode = original
    assert instance.selectedNode == original

@given(instance=org::sgiusa::model::Permission_strategy)
@settings(max_examples=50)
def test_org::sgiusa::model::permission_instantiation(instance):
    assert isinstance(instance, org::sgiusa::model::Permission)

@given(instance=org::sgiusa::model::Permission_strategy)
def test_org::sgiusa::model::permission_capabilities_type(instance):
    assert isinstance(instance.capabilities, str)


@given(instance=org::sgiusa::model::Permission_strategy)
def test_org::sgiusa::model::permission_capabilities_setter(instance):
    original = instance.capabilities
    instance.capabilities = original
    assert instance.capabilities == original

@given(instance=org::sgiusa::model::Permission_strategy)
def test_org::sgiusa::model::permission_activityGroups_type(instance):
    assert isinstance(instance.activityGroups, str)


@given(instance=org::sgiusa::model::Permission_strategy)
def test_org::sgiusa::model::permission_activityGroups_setter(instance):
    original = instance.activityGroups
    instance.activityGroups = original
    assert instance.activityGroups == original

@given(instance=org::sgiusa::model::Permission_strategy)
def test_org::sgiusa::model::permission_userId_type(instance):
    assert isinstance(instance.userId, str)


@given(instance=org::sgiusa::model::Permission_strategy)
def test_org::sgiusa::model::permission_userId_setter(instance):
    original = instance.userId
    instance.userId = original
    assert instance.userId == original

@given(instance=org::sgiusa::model::Permission_strategy)
def test_org::sgiusa::model::permission_enabled_type(instance):
    assert isinstance(instance.enabled, str)


@given(instance=org::sgiusa::model::Permission_strategy)
def test_org::sgiusa::model::permission_enabled_setter(instance):
    original = instance.enabled
    instance.enabled = original
    assert instance.enabled == original

@given(instance=org::sgiusa::model::Permission_strategy)
def test_org::sgiusa::model::permission_divisions_type(instance):
    assert isinstance(instance.divisions, str)


@given(instance=org::sgiusa::model::Permission_strategy)
def test_org::sgiusa::model::permission_divisions_setter(instance):
    original = instance.divisions
    instance.divisions = original
    assert instance.divisions == original

@given(instance=org::sgiusa::model::Permission_strategy)
def test_org::sgiusa::model::permission_subDivisions_type(instance):
    assert isinstance(instance.subDivisions, str)


@given(instance=org::sgiusa::model::Permission_strategy)
def test_org::sgiusa::model::permission_subDivisions_setter(instance):
    original = instance.subDivisions
    instance.subDivisions = original
    assert instance.subDivisions == original

@given(instance=org::sgiusa::model::Permission_strategy)
def test_org::sgiusa::model::permission_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=org::sgiusa::model::Permission_strategy)
def test_org::sgiusa::model::permission_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=org::sgiusa::model::Organization_strategy)
@settings(max_examples=50)
def test_org::sgiusa::model::organization_instantiation(instance):
    assert isinstance(instance, org::sgiusa::model::Organization)

@given(instance=org::sgiusa::model::Organization_strategy)
def test_org::sgiusa::model::organization_level_type(instance):
    assert isinstance(instance.level, str)


@given(instance=org::sgiusa::model::Organization_strategy)
def test_org::sgiusa::model::organization_level_setter(instance):
    original = instance.level
    instance.level = original
    assert instance.level == original

@given(instance=org::sgiusa::model::Organization_strategy)
def test_org::sgiusa::model::organization_permissionId_type(instance):
    assert isinstance(instance.permissionId, str)


@given(instance=org::sgiusa::model::Organization_strategy)
def test_org::sgiusa::model::organization_permissionId_setter(instance):
    original = instance.permissionId
    instance.permissionId = original
    assert instance.permissionId == original

@given(instance=org::sgiusa::model::Organization_strategy)
def test_org::sgiusa::model::organization_abbrv_type(instance):
    assert isinstance(instance.abbrv, str)


@given(instance=org::sgiusa::model::Organization_strategy)
def test_org::sgiusa::model::organization_abbrv_setter(instance):
    original = instance.abbrv
    instance.abbrv = original
    assert instance.abbrv == original

@given(instance=org::sgiusa::model::Organization_strategy)
def test_org::sgiusa::model::organization_lastUpdate_type(instance):
    assert isinstance(instance.lastUpdate, str)


@given(instance=org::sgiusa::model::Organization_strategy)
def test_org::sgiusa::model::organization_lastUpdate_setter(instance):
    original = instance.lastUpdate
    instance.lastUpdate = original
    assert instance.lastUpdate == original

@given(instance=org::sgiusa::model::Organization_strategy)
def test_org::sgiusa::model::organization_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=org::sgiusa::model::Organization_strategy)
def test_org::sgiusa::model::organization_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=org::sgiusa::model::Organization_strategy)
def test_org::sgiusa::model::organization_organizationId_type(instance):
    assert isinstance(instance.organizationId, str)


@given(instance=org::sgiusa::model::Organization_strategy)
def test_org::sgiusa::model::organization_organizationId_setter(instance):
    original = instance.organizationId
    instance.organizationId = original
    assert instance.organizationId == original

@given(instance=org::sgiusa::model::Organization_strategy)
def test_org::sgiusa::model::organization_creationDate_type(instance):
    assert isinstance(instance.creationDate, str)


@given(instance=org::sgiusa::model::Organization_strategy)
def test_org::sgiusa::model::organization_creationDate_setter(instance):
    original = instance.creationDate
    instance.creationDate = original
    assert instance.creationDate == original

@given(instance=org::sgiusa::model::Organization_strategy)
def test_org::sgiusa::model::organization_zipCodes_type(instance):
    assert isinstance(instance.zipCodes, str)


@given(instance=org::sgiusa::model::Organization_strategy)
def test_org::sgiusa::model::organization_zipCodes_setter(instance):
    original = instance.zipCodes
    instance.zipCodes = original
    assert instance.zipCodes == original

@given(instance=org::sgiusa::model::Organization_strategy)
def test_org::sgiusa::model::organization_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=org::sgiusa::model::Organization_strategy)
def test_org::sgiusa::model::organization_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=org::sgiusa::model::Organization_strategy)
def test_org::sgiusa::model::organization_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=org::sgiusa::model::Organization_strategy)
def test_org::sgiusa::model::organization_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=org::sgiusa::model::Organization_strategy)
def test_org::sgiusa::model::organization_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=org::sgiusa::model::Organization_strategy)
def test_org::sgiusa::model::organization_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=org::sgiusa::model::MembershipInfo_strategy)
@settings(max_examples=50)
def test_org::sgiusa::model::membershipinfo_instantiation(instance):
    assert isinstance(instance, org::sgiusa::model::MembershipInfo)

@given(instance=org::sgiusa::model::MembershipInfo_strategy)
def test_org::sgiusa::model::membershipinfo_friendOfSgi_type(instance):
    assert isinstance(instance.friendOfSgi, str)


@given(instance=org::sgiusa::model::MembershipInfo_strategy)
def test_org::sgiusa::model::membershipinfo_friendOfSgi_setter(instance):
    original = instance.friendOfSgi
    instance.friendOfSgi = original
    assert instance.friendOfSgi == original

@given(instance=org::sgiusa::model::MembershipInfo_strategy)
def test_org::sgiusa::model::membershipinfo_notLocatable_type(instance):
    assert isinstance(instance.notLocatable, str)


@given(instance=org::sgiusa::model::MembershipInfo_strategy)
def test_org::sgiusa::model::membershipinfo_notLocatable_setter(instance):
    original = instance.notLocatable
    instance.notLocatable = original
    assert instance.notLocatable == original

@given(instance=org::sgiusa::model::MembershipInfo_strategy)
def test_org::sgiusa::model::membershipinfo_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=org::sgiusa::model::MembershipInfo_strategy)
def test_org::sgiusa::model::membershipinfo_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=org::sgiusa::model::MembershipInfo_strategy)
def test_org::sgiusa::model::membershipinfo_receivedCertificate_type(instance):
    assert isinstance(instance.receivedCertificate, str)


@given(instance=org::sgiusa::model::MembershipInfo_strategy)
def test_org::sgiusa::model::membershipinfo_receivedCertificate_setter(instance):
    original = instance.receivedCertificate
    instance.receivedCertificate = original
    assert instance.receivedCertificate == original

@given(instance=org::sgiusa::model::MembershipInfo_strategy)
def test_org::sgiusa::model::membershipinfo_notActivated_type(instance):
    assert isinstance(instance.notActivated, str)


@given(instance=org::sgiusa::model::MembershipInfo_strategy)
def test_org::sgiusa::model::membershipinfo_notActivated_setter(instance):
    original = instance.notActivated
    instance.notActivated = original
    assert instance.notActivated == original

@given(instance=org::sgiusa::model::MembershipInfo_strategy)
def test_org::sgiusa::model::membershipinfo_lastUpdate_type(instance):
    assert isinstance(instance.lastUpdate, str)


@given(instance=org::sgiusa::model::MembershipInfo_strategy)
def test_org::sgiusa::model::membershipinfo_lastUpdate_setter(instance):
    original = instance.lastUpdate
    instance.lastUpdate = original
    assert instance.lastUpdate == original

@given(instance=org::sgiusa::model::Note_strategy)
@settings(max_examples=50)
def test_org::sgiusa::model::note_instantiation(instance):
    assert isinstance(instance, org::sgiusa::model::Note)

@given(instance=org::sgiusa::model::Note_strategy)
def test_org::sgiusa::model::note_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=org::sgiusa::model::Note_strategy)
def test_org::sgiusa::model::note_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=org::sgiusa::model::Note_strategy)
def test_org::sgiusa::model::note_lastUpdate_type(instance):
    assert isinstance(instance.lastUpdate, str)


@given(instance=org::sgiusa::model::Note_strategy)
def test_org::sgiusa::model::note_lastUpdate_setter(instance):
    original = instance.lastUpdate
    instance.lastUpdate = original
    assert instance.lastUpdate == original

@given(instance=org::sgiusa::model::Note_strategy)
def test_org::sgiusa::model::note_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=org::sgiusa::model::Note_strategy)
def test_org::sgiusa::model::note_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=org::sgiusa::model::Note_strategy)
def test_org::sgiusa::model::note_creationDate_type(instance):
    assert isinstance(instance.creationDate, str)


@given(instance=org::sgiusa::model::Note_strategy)
def test_org::sgiusa::model::note_creationDate_setter(instance):
    original = instance.creationDate
    instance.creationDate = original
    assert instance.creationDate == original

@given(instance=org::sgiusa::model::Members_strategy)
@settings(max_examples=50)
def test_org::sgiusa::model::members_instantiation(instance):
    assert isinstance(instance, org::sgiusa::model::Members)

@given(instance=org::sgiusa::model::MemberSearchCriteria_strategy)
@settings(max_examples=50)
def test_org::sgiusa::model::membersearchcriteria_instantiation(instance):
    assert isinstance(instance, org::sgiusa::model::MemberSearchCriteria)

@given(instance=org::sgiusa::model::MemberSearchCriteria_strategy)
def test_org::sgiusa::model::membersearchcriteria_divisions_type(instance):
    assert isinstance(instance.divisions, str)


@given(instance=org::sgiusa::model::MemberSearchCriteria_strategy)
def test_org::sgiusa::model::membersearchcriteria_divisions_setter(instance):
    original = instance.divisions
    instance.divisions = original
    assert instance.divisions == original

@given(instance=org::sgiusa::model::MemberSearchCriteria_strategy)
def test_org::sgiusa::model::membersearchcriteria_activityGroups_type(instance):
    assert isinstance(instance.activityGroups, str)


@given(instance=org::sgiusa::model::MemberSearchCriteria_strategy)
def test_org::sgiusa::model::membersearchcriteria_activityGroups_setter(instance):
    original = instance.activityGroups
    instance.activityGroups = original
    assert instance.activityGroups == original

@given(instance=org::sgiusa::model::MemberSearchCriteria_strategy)
def test_org::sgiusa::model::membersearchcriteria_subDivisions_type(instance):
    assert isinstance(instance.subDivisions, str)


@given(instance=org::sgiusa::model::MemberSearchCriteria_strategy)
def test_org::sgiusa::model::membersearchcriteria_subDivisions_setter(instance):
    original = instance.subDivisions
    instance.subDivisions = original
    assert instance.subDivisions == original

@given(instance=org::sgiusa::model::Member_strategy)
@settings(max_examples=50)
def test_org::sgiusa::model::member_instantiation(instance):
    assert isinstance(instance, org::sgiusa::model::Member)

@given(instance=org::sgiusa::model::Member_strategy)
def test_org::sgiusa::model::member_archived_type(instance):
    assert isinstance(instance.archived, str)


@given(instance=org::sgiusa::model::Member_strategy)
def test_org::sgiusa::model::member_archived_setter(instance):
    original = instance.archived
    instance.archived = original
    assert instance.archived == original

@given(instance=org::sgiusa::model::Member_strategy)
def test_org::sgiusa::model::member_firstName_type(instance):
    assert isinstance(instance.firstName, str)


@given(instance=org::sgiusa::model::Member_strategy)
def test_org::sgiusa::model::member_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original

@given(instance=org::sgiusa::model::Member_strategy)
def test_org::sgiusa::model::member_extraField2_type(instance):
    assert isinstance(instance.extraField2, str)


@given(instance=org::sgiusa::model::Member_strategy)
def test_org::sgiusa::model::member_extraField2_setter(instance):
    original = instance.extraField2
    instance.extraField2 = original
    assert instance.extraField2 == original

@given(instance=org::sgiusa::model::Member_strategy)
def test_org::sgiusa::model::member_joinDate_type(instance):
    assert isinstance(instance.joinDate, str)


@given(instance=org::sgiusa::model::Member_strategy)
def test_org::sgiusa::model::member_joinDate_setter(instance):
    original = instance.joinDate
    instance.joinDate = original
    assert instance.joinDate == original

@given(instance=org::sgiusa::model::Member_strategy)
def test_org::sgiusa::model::member_employer_type(instance):
    assert isinstance(instance.employer, str)


@given(instance=org::sgiusa::model::Member_strategy)
def test_org::sgiusa::model::member_employer_setter(instance):
    original = instance.employer
    instance.employer = original
    assert instance.employer == original

@given(instance=org::sgiusa::model::Member_strategy)
def test_org::sgiusa::model::member_visible_type(instance):
    assert isinstance(instance.visible, str)


@given(instance=org::sgiusa::model::Member_strategy)
def test_org::sgiusa::model::member_visible_setter(instance):
    original = instance.visible
    instance.visible = original
    assert instance.visible == original

@given(instance=org::sgiusa::model::Member_strategy)
def test_org::sgiusa::model::member_birthDate_type(instance):
    assert isinstance(instance.birthDate, str)


@given(instance=org::sgiusa::model::Member_strategy)
def test_org::sgiusa::model::member_birthDate_setter(instance):
    original = instance.birthDate
    instance.birthDate = original
    assert instance.birthDate == original

@given(instance=org::sgiusa::model::Member_strategy)
def test_org::sgiusa::model::member_statusProfile_type(instance):
    assert isinstance(instance.statusProfile, str)


@given(instance=org::sgiusa::model::Member_strategy)
def test_org::sgiusa::model::member_statusProfile_setter(instance):
    original = instance.statusProfile
    instance.statusProfile = original
    assert instance.statusProfile == original

@given(instance=org::sgiusa::model::Member_strategy)
def test_org::sgiusa::model::member_extraField1_type(instance):
    assert isinstance(instance.extraField1, str)


@given(instance=org::sgiusa::model::Member_strategy)
def test_org::sgiusa::model::member_extraField1_setter(instance):
    original = instance.extraField1
    instance.extraField1 = original
    assert instance.extraField1 == original

@given(instance=org::sgiusa::model::Member_strategy)
def test_org::sgiusa::model::member_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=org::sgiusa::model::Member_strategy)
def test_org::sgiusa::model::member_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=org::sgiusa::model::Member_strategy)
def test_org::sgiusa::model::member_locatable_type(instance):
    assert isinstance(instance.locatable, str)


@given(instance=org::sgiusa::model::Member_strategy)
def test_org::sgiusa::model::member_locatable_setter(instance):
    original = instance.locatable
    instance.locatable = original
    assert instance.locatable == original

@given(instance=org::sgiusa::model::Member_strategy)
def test_org::sgiusa::model::member_occupation_type(instance):
    assert isinstance(instance.occupation, str)


@given(instance=org::sgiusa::model::Member_strategy)
def test_org::sgiusa::model::member_occupation_setter(instance):
    original = instance.occupation
    instance.occupation = original
    assert instance.occupation == original

@given(instance=org::sgiusa::model::Member_strategy)
def test_org::sgiusa::model::member_lastName_type(instance):
    assert isinstance(instance.lastName, str)


@given(instance=org::sgiusa::model::Member_strategy)
def test_org::sgiusa::model::member_lastName_setter(instance):
    original = instance.lastName
    instance.lastName = original
    assert instance.lastName == original

@given(instance=org::sgiusa::model::Member_strategy)
def test_org::sgiusa::model::member_middleInitial_type(instance):
    assert isinstance(instance.middleInitial, str)


@given(instance=org::sgiusa::model::Member_strategy)
def test_org::sgiusa::model::member_middleInitial_setter(instance):
    original = instance.middleInitial
    instance.middleInitial = original
    assert instance.middleInitial == original

@given(instance=org::sgiusa::model::Member_strategy)
def test_org::sgiusa::model::member_interests_type(instance):
    assert isinstance(instance.interests, str)


@given(instance=org::sgiusa::model::Member_strategy)
def test_org::sgiusa::model::member_interests_setter(instance):
    original = instance.interests
    instance.interests = original
    assert instance.interests == original

@given(instance=org::sgiusa::model::Member_strategy)
def test_org::sgiusa::model::member_activityGroups_type(instance):
    assert isinstance(instance.activityGroups, str)


@given(instance=org::sgiusa::model::Member_strategy)
def test_org::sgiusa::model::member_activityGroups_setter(instance):
    original = instance.activityGroups
    instance.activityGroups = original
    assert instance.activityGroups == original

@given(instance=org::sgiusa::model::Member_strategy)
def test_org::sgiusa::model::member_languages_type(instance):
    assert isinstance(instance.languages, str)


@given(instance=org::sgiusa::model::Member_strategy)
def test_org::sgiusa::model::member_languages_setter(instance):
    original = instance.languages
    instance.languages = original
    assert instance.languages == original

@given(instance=org::sgiusa::model::Member_strategy)
def test_org::sgiusa::model::member_subDivision_type(instance):
    assert isinstance(instance.subDivision, str)


@given(instance=org::sgiusa::model::Member_strategy)
def test_org::sgiusa::model::member_subDivision_setter(instance):
    original = instance.subDivision
    instance.subDivision = original
    assert instance.subDivision == original

@given(instance=org::sgiusa::model::Member_strategy)
def test_org::sgiusa::model::member_division_type(instance):
    assert isinstance(instance.division, str)


@given(instance=org::sgiusa::model::Member_strategy)
def test_org::sgiusa::model::member_division_setter(instance):
    original = instance.division
    instance.division = original
    assert instance.division == original

@given(instance=org::sgiusa::model::LeadershipInfo_strategy)
@settings(max_examples=50)
def test_org::sgiusa::model::leadershipinfo_instantiation(instance):
    assert isinstance(instance, org::sgiusa::model::LeadershipInfo)

@given(instance=org::sgiusa::model::LeadershipInfo_strategy)
def test_org::sgiusa::model::leadershipinfo_manualSigned_type(instance):
    assert isinstance(instance.manualSigned, str)


@given(instance=org::sgiusa::model::LeadershipInfo_strategy)
def test_org::sgiusa::model::leadershipinfo_manualSigned_setter(instance):
    original = instance.manualSigned
    instance.manualSigned = original
    assert instance.manualSigned == original

@given(instance=org::sgiusa::model::LeadershipInfo_strategy)
def test_org::sgiusa::model::leadershipinfo_examPassedDate_type(instance):
    assert isinstance(instance.examPassedDate, str)


@given(instance=org::sgiusa::model::LeadershipInfo_strategy)
def test_org::sgiusa::model::leadershipinfo_examPassedDate_setter(instance):
    original = instance.examPassedDate
    instance.examPassedDate = original
    assert instance.examPassedDate == original

@given(instance=org::sgiusa::model::LeadershipInfo_strategy)
def test_org::sgiusa::model::leadershipinfo_examPassed_type(instance):
    assert isinstance(instance.examPassed, str)


@given(instance=org::sgiusa::model::LeadershipInfo_strategy)
def test_org::sgiusa::model::leadershipinfo_examPassed_setter(instance):
    original = instance.examPassed
    instance.examPassed = original
    assert instance.examPassed == original

@given(instance=org::sgiusa::model::LeadershipInfo_strategy)
def test_org::sgiusa::model::leadershipinfo_lastUpdate_type(instance):
    assert isinstance(instance.lastUpdate, str)


@given(instance=org::sgiusa::model::LeadershipInfo_strategy)
def test_org::sgiusa::model::leadershipinfo_lastUpdate_setter(instance):
    original = instance.lastUpdate
    instance.lastUpdate = original
    assert instance.lastUpdate == original

@given(instance=org::sgiusa::model::LeadershipInfo_strategy)
def test_org::sgiusa::model::leadershipinfo_manualSignedDate_type(instance):
    assert isinstance(instance.manualSignedDate, str)


@given(instance=org::sgiusa::model::LeadershipInfo_strategy)
def test_org::sgiusa::model::leadershipinfo_manualSignedDate_setter(instance):
    original = instance.manualSignedDate
    instance.manualSignedDate = original
    assert instance.manualSignedDate == original

@given(instance=org::sgiusa::model::LeadershipInfo_strategy)
def test_org::sgiusa::model::leadershipinfo_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=org::sgiusa::model::LeadershipInfo_strategy)
def test_org::sgiusa::model::leadershipinfo_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=org::sgiusa::model::LeadershipRole_strategy)
@settings(max_examples=50)
def test_org::sgiusa::model::leadershiprole_instantiation(instance):
    assert isinstance(instance, org::sgiusa::model::LeadershipRole)

@given(instance=org::sgiusa::model::LeadershipRole_strategy)
def test_org::sgiusa::model::leadershiprole_level_type(instance):
    assert isinstance(instance.level, str)


@given(instance=org::sgiusa::model::LeadershipRole_strategy)
def test_org::sgiusa::model::leadershiprole_level_setter(instance):
    original = instance.level
    instance.level = original
    assert instance.level == original

@given(instance=org::sgiusa::model::LeadershipRole_strategy)
def test_org::sgiusa::model::leadershiprole_lastUpdate_type(instance):
    assert isinstance(instance.lastUpdate, str)


@given(instance=org::sgiusa::model::LeadershipRole_strategy)
def test_org::sgiusa::model::leadershiprole_lastUpdate_setter(instance):
    original = instance.lastUpdate
    instance.lastUpdate = original
    assert instance.lastUpdate == original

@given(instance=org::sgiusa::model::LeadershipRole_strategy)
def test_org::sgiusa::model::leadershiprole_position_type(instance):
    assert isinstance(instance.position, str)


@given(instance=org::sgiusa::model::LeadershipRole_strategy)
def test_org::sgiusa::model::leadershiprole_position_setter(instance):
    original = instance.position
    instance.position = original
    assert instance.position == original

@given(instance=org::sgiusa::model::LeadershipRole_strategy)
def test_org::sgiusa::model::leadershiprole_subDivision_type(instance):
    assert isinstance(instance.subDivision, str)


@given(instance=org::sgiusa::model::LeadershipRole_strategy)
def test_org::sgiusa::model::leadershiprole_subDivision_setter(instance):
    original = instance.subDivision
    instance.subDivision = original
    assert instance.subDivision == original

@given(instance=org::sgiusa::model::LeadershipRole_strategy)
def test_org::sgiusa::model::leadershiprole_active_type(instance):
    assert isinstance(instance.active, str)


@given(instance=org::sgiusa::model::LeadershipRole_strategy)
def test_org::sgiusa::model::leadershiprole_active_setter(instance):
    original = instance.active
    instance.active = original
    assert instance.active == original

@given(instance=org::sgiusa::model::LeadershipRole_strategy)
def test_org::sgiusa::model::leadershiprole_division_type(instance):
    assert isinstance(instance.division, str)


@given(instance=org::sgiusa::model::LeadershipRole_strategy)
def test_org::sgiusa::model::leadershiprole_division_setter(instance):
    original = instance.division
    instance.division = original
    assert instance.division == original

@given(instance=org::sgiusa::model::LeadershipRole_strategy)
def test_org::sgiusa::model::leadershiprole_activityGroup_type(instance):
    assert isinstance(instance.activityGroup, str)


@given(instance=org::sgiusa::model::LeadershipRole_strategy)
def test_org::sgiusa::model::leadershiprole_activityGroup_setter(instance):
    original = instance.activityGroup
    instance.activityGroup = original
    assert instance.activityGroup == original

@given(instance=org::sgiusa::model::LeadershipRole_strategy)
def test_org::sgiusa::model::leadershiprole_startDate_type(instance):
    assert isinstance(instance.startDate, str)


@given(instance=org::sgiusa::model::LeadershipRole_strategy)
def test_org::sgiusa::model::leadershiprole_startDate_setter(instance):
    original = instance.startDate
    instance.startDate = original
    assert instance.startDate == original

@given(instance=org::sgiusa::model::LeadershipRole_strategy)
def test_org::sgiusa::model::leadershiprole_endDate_type(instance):
    assert isinstance(instance.endDate, str)


@given(instance=org::sgiusa::model::LeadershipRole_strategy)
def test_org::sgiusa::model::leadershiprole_endDate_setter(instance):
    original = instance.endDate
    instance.endDate = original
    assert instance.endDate == original

@given(instance=org::sgiusa::model::LeadershipRole_strategy)
def test_org::sgiusa::model::leadershiprole_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=org::sgiusa::model::LeadershipRole_strategy)
def test_org::sgiusa::model::leadershiprole_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=org::sgiusa::model::GohonzonInfo_strategy)
@settings(max_examples=50)
def test_org::sgiusa::model::gohonzoninfo_instantiation(instance):
    assert isinstance(instance, org::sgiusa::model::GohonzonInfo)

@given(instance=org::sgiusa::model::GohonzonInfo_strategy)
def test_org::sgiusa::model::gohonzoninfo_lastUpdate_type(instance):
    assert isinstance(instance.lastUpdate, str)


@given(instance=org::sgiusa::model::GohonzonInfo_strategy)
def test_org::sgiusa::model::gohonzoninfo_lastUpdate_setter(instance):
    original = instance.lastUpdate
    instance.lastUpdate = original
    assert instance.lastUpdate == original

@given(instance=org::sgiusa::model::GohonzonInfo_strategy)
def test_org::sgiusa::model::gohonzoninfo_returned_type(instance):
    assert isinstance(instance.returned, str)


@given(instance=org::sgiusa::model::GohonzonInfo_strategy)
def test_org::sgiusa::model::gohonzoninfo_returned_setter(instance):
    original = instance.returned
    instance.returned = original
    assert instance.returned == original

@given(instance=org::sgiusa::model::GohonzonInfo_strategy)
def test_org::sgiusa::model::gohonzoninfo_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=org::sgiusa::model::GohonzonInfo_strategy)
def test_org::sgiusa::model::gohonzoninfo_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=org::sgiusa::model::GohonzonInfo_strategy)
def test_org::sgiusa::model::gohonzoninfo_returnDate_type(instance):
    assert isinstance(instance.returnDate, str)


@given(instance=org::sgiusa::model::GohonzonInfo_strategy)
def test_org::sgiusa::model::gohonzoninfo_returnDate_setter(instance):
    original = instance.returnDate
    instance.returnDate = original
    assert instance.returnDate == original

@given(instance=org::sgiusa::model::GohonzonInfo_strategy)
def test_org::sgiusa::model::gohonzoninfo_gohonzonType_type(instance):
    assert isinstance(instance.gohonzonType, str)


@given(instance=org::sgiusa::model::GohonzonInfo_strategy)
def test_org::sgiusa::model::gohonzoninfo_gohonzonType_setter(instance):
    original = instance.gohonzonType
    instance.gohonzonType = original
    assert instance.gohonzonType == original

@given(instance=org::sgiusa::model::GohonzonInfo_strategy)
def test_org::sgiusa::model::gohonzoninfo_receiveDate_type(instance):
    assert isinstance(instance.receiveDate, str)


@given(instance=org::sgiusa::model::GohonzonInfo_strategy)
def test_org::sgiusa::model::gohonzoninfo_receiveDate_setter(instance):
    original = instance.receiveDate
    instance.receiveDate = original
    assert instance.receiveDate == original

@given(instance=org::sgiusa::model::FamilyMember_strategy)
@settings(max_examples=50)
def test_org::sgiusa::model::familymember_instantiation(instance):
    assert isinstance(instance, org::sgiusa::model::FamilyMember)

@given(instance=org::sgiusa::model::FamilyMember_strategy)
def test_org::sgiusa::model::familymember_personName_type(instance):
    assert isinstance(instance.personName, str)


@given(instance=org::sgiusa::model::FamilyMember_strategy)
def test_org::sgiusa::model::familymember_personName_setter(instance):
    original = instance.personName
    instance.personName = original
    assert instance.personName == original

@given(instance=org::sgiusa::model::FamilyMember_strategy)
def test_org::sgiusa::model::familymember_lastUpdate_type(instance):
    assert isinstance(instance.lastUpdate, str)


@given(instance=org::sgiusa::model::FamilyMember_strategy)
def test_org::sgiusa::model::familymember_lastUpdate_setter(instance):
    original = instance.lastUpdate
    instance.lastUpdate = original
    assert instance.lastUpdate == original

@given(instance=org::sgiusa::model::FamilyMember_strategy)
def test_org::sgiusa::model::familymember_familyRelation_type(instance):
    assert isinstance(instance.familyRelation, str)


@given(instance=org::sgiusa::model::FamilyMember_strategy)
def test_org::sgiusa::model::familymember_familyRelation_setter(instance):
    original = instance.familyRelation
    instance.familyRelation = original
    assert instance.familyRelation == original

@given(instance=org::sgiusa::model::FamilyMember_strategy)
def test_org::sgiusa::model::familymember_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=org::sgiusa::model::FamilyMember_strategy)
def test_org::sgiusa::model::familymember_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=org::sgiusa::model::FamilyMember_strategy)
def test_org::sgiusa::model::familymember_sgiMember_type(instance):
    assert isinstance(instance.sgiMember, str)


@given(instance=org::sgiusa::model::FamilyMember_strategy)
def test_org::sgiusa::model::familymember_sgiMember_setter(instance):
    original = instance.sgiMember
    instance.sgiMember = original
    assert instance.sgiMember == original

@given(instance=org::sgiusa::model::Event_strategy)
@settings(max_examples=50)
def test_org::sgiusa::model::event_instantiation(instance):
    assert isinstance(instance, org::sgiusa::model::Event)

@given(instance=org::sgiusa::model::Event_strategy)
def test_org::sgiusa::model::event_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=org::sgiusa::model::Event_strategy)
def test_org::sgiusa::model::event_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=org::sgiusa::model::Event_strategy)
def test_org::sgiusa::model::event_divisions_type(instance):
    assert isinstance(instance.divisions, str)


@given(instance=org::sgiusa::model::Event_strategy)
def test_org::sgiusa::model::event_divisions_setter(instance):
    original = instance.divisions
    instance.divisions = original
    assert instance.divisions == original

@given(instance=org::sgiusa::model::Event_strategy)
def test_org::sgiusa::model::event_status_type(instance):
    assert isinstance(instance.status, str)


@given(instance=org::sgiusa::model::Event_strategy)
def test_org::sgiusa::model::event_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original

@given(instance=org::sgiusa::model::Event_strategy)
def test_org::sgiusa::model::event_subDivisions_type(instance):
    assert isinstance(instance.subDivisions, str)


@given(instance=org::sgiusa::model::Event_strategy)
def test_org::sgiusa::model::event_subDivisions_setter(instance):
    original = instance.subDivisions
    instance.subDivisions = original
    assert instance.subDivisions == original

@given(instance=org::sgiusa::model::Event_strategy)
def test_org::sgiusa::model::event_userId_type(instance):
    assert isinstance(instance.userId, str)


@given(instance=org::sgiusa::model::Event_strategy)
def test_org::sgiusa::model::event_userId_setter(instance):
    original = instance.userId
    instance.userId = original
    assert instance.userId == original

@given(instance=StudyDeptInfo_strategy)
@settings(max_examples=50)
def test_studydeptinfo_instantiation(instance):
    assert isinstance(instance, StudyDeptInfo)

@given(instance=StudyDeptExam_strategy)
@settings(max_examples=50)
def test_studydeptexam_instantiation(instance):
    assert isinstance(instance, StudyDeptExam)

@given(instance=SchoolInfo_strategy)
@settings(max_examples=50)
def test_schoolinfo_instantiation(instance):
    assert isinstance(instance, SchoolInfo)

@given(instance=Registration_strategy)
@settings(max_examples=50)
def test_registration_instantiation(instance):
    assert isinstance(instance, Registration)

@given(instance=org::sgiusa::model::EmailList_strategy)
@settings(max_examples=50)
def test_org::sgiusa::model::emaillist_instantiation(instance):
    assert isinstance(instance, org::sgiusa::model::EmailList)

@given(instance=org::sgiusa::model::EmailList_strategy)
def test_org::sgiusa::model::emaillist_divisions_type(instance):
    assert isinstance(instance.divisions, str)


@given(instance=org::sgiusa::model::EmailList_strategy)
def test_org::sgiusa::model::emaillist_divisions_setter(instance):
    original = instance.divisions
    instance.divisions = original
    assert instance.divisions == original

@given(instance=org::sgiusa::model::EmailList_strategy)
def test_org::sgiusa::model::emaillist_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=org::sgiusa::model::EmailList_strategy)
def test_org::sgiusa::model::emaillist_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=org::sgiusa::model::EmailList_strategy)
def test_org::sgiusa::model::emaillist_subDivisions_type(instance):
    assert isinstance(instance.subDivisions, str)


@given(instance=org::sgiusa::model::EmailList_strategy)
def test_org::sgiusa::model::emaillist_subDivisions_setter(instance):
    original = instance.subDivisions
    instance.subDivisions = original
    assert instance.subDivisions == original

@given(instance=org::sgiusa::model::EmailList_strategy)
def test_org::sgiusa::model::emaillist_enabled_type(instance):
    assert isinstance(instance.enabled, str)


@given(instance=org::sgiusa::model::EmailList_strategy)
def test_org::sgiusa::model::emaillist_enabled_setter(instance):
    original = instance.enabled
    instance.enabled = original
    assert instance.enabled == original

@given(instance=org::sgiusa::model::EmailList_strategy)
def test_org::sgiusa::model::emaillist_activityGroups_type(instance):
    assert isinstance(instance.activityGroups, str)


@given(instance=org::sgiusa::model::EmailList_strategy)
def test_org::sgiusa::model::emaillist_activityGroups_setter(instance):
    original = instance.activityGroups
    instance.activityGroups = original
    assert instance.activityGroups == original

@given(instance=View_strategy)
@settings(max_examples=50)
def test_view_instantiation(instance):
    assert isinstance(instance, View)

@given(instance=Users_strategy)
@settings(max_examples=50)
def test_users_instantiation(instance):
    assert isinstance(instance, Users)

@given(instance=MemberSearchCriteria_strategy)
@settings(max_examples=50)
def test_membersearchcriteria_instantiation(instance):
    assert isinstance(instance, MemberSearchCriteria)

@given(instance=Members_strategy)
@settings(max_examples=50)
def test_members_instantiation(instance):
    assert isinstance(instance, Members)

@given(instance=Member_strategy)
@settings(max_examples=50)
def test_member_instantiation(instance):
    assert isinstance(instance, Member)

@given(instance=LeadershipRole_strategy)
@settings(max_examples=50)
def test_leadershiprole_instantiation(instance):
    assert isinstance(instance, LeadershipRole)

@given(instance=LeadershipInfo_strategy)
@settings(max_examples=50)
def test_leadershipinfo_instantiation(instance):
    assert isinstance(instance, LeadershipInfo)

@given(instance=Preferences_strategy)
@settings(max_examples=50)
def test_preferences_instantiation(instance):
    assert isinstance(instance, Preferences)

@given(instance=Permission_strategy)
@settings(max_examples=50)
def test_permission_instantiation(instance):
    assert isinstance(instance, Permission)

@given(instance=Organization_strategy)
@settings(max_examples=50)
def test_organization_instantiation(instance):
    assert isinstance(instance, Organization)

@given(instance=org::aries::common::EObject_strategy)
@settings(max_examples=50)
def test_org::aries::common::eobject_instantiation(instance):
    assert isinstance(instance, org::aries::common::EObject)

@given(instance=org::aries::common::MapEntry_strategy)
@settings(max_examples=50)
def test_org::aries::common::mapentry_instantiation(instance):
    assert isinstance(instance, org::aries::common::MapEntry)

@given(instance=org::aries::common::Map_strategy)
@settings(max_examples=50)
def test_org::aries::common::map_instantiation(instance):
    assert isinstance(instance, org::aries::common::Map)

@given(instance=org::aries::common::Note_strategy)
@settings(max_examples=50)
def test_org::aries::common::note_instantiation(instance):
    assert isinstance(instance, org::aries::common::Note)

@given(instance=org::aries::common::Note_strategy)
def test_org::aries::common::note_lastUpdate_type(instance):
    assert isinstance(instance.lastUpdate, str)


@given(instance=org::aries::common::Note_strategy)
def test_org::aries::common::note_lastUpdate_setter(instance):
    original = instance.lastUpdate
    instance.lastUpdate = original
    assert instance.lastUpdate == original

@given(instance=org::aries::common::Note_strategy)
def test_org::aries::common::note_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=org::aries::common::Note_strategy)
def test_org::aries::common::note_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=org::aries::common::Note_strategy)
def test_org::aries::common::note_creationDate_type(instance):
    assert isinstance(instance.creationDate, str)


@given(instance=org::aries::common::Note_strategy)
def test_org::aries::common::note_creationDate_setter(instance):
    original = instance.creationDate
    instance.creationDate = original
    assert instance.creationDate == original

@given(instance=org::aries::common::Note_strategy)
def test_org::aries::common::note_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=org::aries::common::Note_strategy)
def test_org::aries::common::note_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=org::aries::common::Event_strategy)
@settings(max_examples=50)
def test_org::aries::common::event_instantiation(instance):
    assert isinstance(instance, org::aries::common::Event)

@given(instance=org::aries::common::Event_strategy)
def test_org::aries::common::event_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=org::aries::common::Event_strategy)
def test_org::aries::common::event_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=org::aries::common::EmailMessage_strategy)
@settings(max_examples=50)
def test_org::aries::common::emailmessage_instantiation(instance):
    assert isinstance(instance, org::aries::common::EmailMessage)

@given(instance=org::aries::common::EmailMessage_strategy)
def test_org::aries::common::emailmessage_sourceId_type(instance):
    assert isinstance(instance.sourceId, str)


@given(instance=org::aries::common::EmailMessage_strategy)
def test_org::aries::common::emailmessage_sourceId_setter(instance):
    original = instance.sourceId
    instance.sourceId = original
    assert instance.sourceId == original

@given(instance=org::aries::common::EmailMessage_strategy)
def test_org::aries::common::emailmessage_smtpHost_type(instance):
    assert isinstance(instance.smtpHost, str)


@given(instance=org::aries::common::EmailMessage_strategy)
def test_org::aries::common::emailmessage_smtpHost_setter(instance):
    original = instance.smtpHost
    instance.smtpHost = original
    assert instance.smtpHost == original

@given(instance=org::aries::common::EmailMessage_strategy)
def test_org::aries::common::emailmessage_content_type(instance):
    assert isinstance(instance.content, str)


@given(instance=org::aries::common::EmailMessage_strategy)
def test_org::aries::common::emailmessage_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original

@given(instance=org::aries::common::EmailMessage_strategy)
def test_org::aries::common::emailmessage_sendAsHtml_type(instance):
    assert isinstance(instance.sendAsHtml, str)


@given(instance=org::aries::common::EmailMessage_strategy)
def test_org::aries::common::emailmessage_sendAsHtml_setter(instance):
    original = instance.sendAsHtml
    instance.sendAsHtml = original
    assert instance.sendAsHtml == original

@given(instance=org::aries::common::EmailMessage_strategy)
def test_org::aries::common::emailmessage_smtpPort_type(instance):
    assert isinstance(instance.smtpPort, str)


@given(instance=org::aries::common::EmailMessage_strategy)
def test_org::aries::common::emailmessage_smtpPort_setter(instance):
    original = instance.smtpPort
    instance.smtpPort = original
    assert instance.smtpPort == original

@given(instance=org::aries::common::EmailMessage_strategy)
def test_org::aries::common::emailmessage_timestamp_type(instance):
    assert isinstance(instance.timestamp, str)


@given(instance=org::aries::common::EmailMessage_strategy)
def test_org::aries::common::emailmessage_timestamp_setter(instance):
    original = instance.timestamp
    instance.timestamp = original
    assert instance.timestamp == original

@given(instance=org::aries::common::EmailMessage_strategy)
def test_org::aries::common::emailmessage_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=org::aries::common::EmailMessage_strategy)
def test_org::aries::common::emailmessage_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=org::aries::common::EmailMessage_strategy)
def test_org::aries::common::emailmessage_subject_type(instance):
    assert isinstance(instance.subject, str)


@given(instance=org::aries::common::EmailMessage_strategy)
def test_org::aries::common::emailmessage_subject_setter(instance):
    original = instance.subject
    instance.subject = original
    assert instance.subject == original

@given(instance=org::aries::common::EmailBox_strategy)
@settings(max_examples=50)
def test_org::aries::common::emailbox_instantiation(instance):
    assert isinstance(instance, org::aries::common::EmailBox)

@given(instance=org::aries::common::EmailBox_strategy)
def test_org::aries::common::emailbox_creationDate_type(instance):
    assert isinstance(instance.creationDate, str)


@given(instance=org::aries::common::EmailBox_strategy)
def test_org::aries::common::emailbox_creationDate_setter(instance):
    original = instance.creationDate
    instance.creationDate = original
    assert instance.creationDate == original

@given(instance=org::aries::common::EmailBox_strategy)
def test_org::aries::common::emailbox_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=org::aries::common::EmailBox_strategy)
def test_org::aries::common::emailbox_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=org::aries::common::EmailBox_strategy)
def test_org::aries::common::emailbox_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=org::aries::common::EmailBox_strategy)
def test_org::aries::common::emailbox_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=org::aries::common::EmailBox_strategy)
def test_org::aries::common::emailbox_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=org::aries::common::EmailBox_strategy)
def test_org::aries::common::emailbox_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=org::aries::common::EmailBox_strategy)
def test_org::aries::common::emailbox_lastUpdate_type(instance):
    assert isinstance(instance.lastUpdate, str)


@given(instance=org::aries::common::EmailBox_strategy)
def test_org::aries::common::emailbox_lastUpdate_setter(instance):
    original = instance.lastUpdate
    instance.lastUpdate = original
    assert instance.lastUpdate == original

@given(instance=org::aries::common::EmailAddressList_strategy)
@settings(max_examples=50)
def test_org::aries::common::emailaddresslist_instantiation(instance):
    assert isinstance(instance, org::aries::common::EmailAddressList)

@given(instance=org::aries::common::EmailAddressList_strategy)
def test_org::aries::common::emailaddresslist_emailAddress_type(instance):
    assert isinstance(instance.emailAddress, str)


@given(instance=org::aries::common::EmailAddressList_strategy)
def test_org::aries::common::emailaddresslist_emailAddress_setter(instance):
    original = instance.emailAddress
    instance.emailAddress = original
    assert instance.emailAddress == original

@given(instance=org::aries::common::EmailAddressList_strategy)
def test_org::aries::common::emailaddresslist_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=org::aries::common::EmailAddressList_strategy)
def test_org::aries::common::emailaddresslist_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=org::aries::common::EmailAddress_strategy)
@settings(max_examples=50)
def test_org::aries::common::emailaddress_instantiation(instance):
    assert isinstance(instance, org::aries::common::EmailAddress)

@given(instance=org::aries::common::EmailAddress_strategy)
def test_org::aries::common::emailaddress_creationDate_type(instance):
    assert isinstance(instance.creationDate, str)


@given(instance=org::aries::common::EmailAddress_strategy)
def test_org::aries::common::emailaddress_creationDate_setter(instance):
    original = instance.creationDate
    instance.creationDate = original
    assert instance.creationDate == original

@given(instance=org::aries::common::EmailAddress_strategy)
def test_org::aries::common::emailaddress_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=org::aries::common::EmailAddress_strategy)
def test_org::aries::common::emailaddress_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=org::aries::common::EmailAddress_strategy)
def test_org::aries::common::emailaddress_enabled_type(instance):
    assert isinstance(instance.enabled, str)


@given(instance=org::aries::common::EmailAddress_strategy)
def test_org::aries::common::emailaddress_enabled_setter(instance):
    original = instance.enabled
    instance.enabled = original
    assert instance.enabled == original

@given(instance=org::aries::common::EmailAddress_strategy)
def test_org::aries::common::emailaddress_organization_type(instance):
    assert isinstance(instance.organization, str)


@given(instance=org::aries::common::EmailAddress_strategy)
def test_org::aries::common::emailaddress_organization_setter(instance):
    original = instance.organization
    instance.organization = original
    assert instance.organization == original

@given(instance=org::aries::common::EmailAddress_strategy)
def test_org::aries::common::emailaddress_lastUpdate_type(instance):
    assert isinstance(instance.lastUpdate, str)


@given(instance=org::aries::common::EmailAddress_strategy)
def test_org::aries::common::emailaddress_lastUpdate_setter(instance):
    original = instance.lastUpdate
    instance.lastUpdate = original
    assert instance.lastUpdate == original

@given(instance=org::aries::common::EmailAddress_strategy)
def test_org::aries::common::emailaddress_userId_type(instance):
    assert isinstance(instance.userId, str)


@given(instance=org::aries::common::EmailAddress_strategy)
def test_org::aries::common::emailaddress_userId_setter(instance):
    original = instance.userId
    instance.userId = original
    assert instance.userId == original

@given(instance=org::aries::common::EmailAddress_strategy)
def test_org::aries::common::emailaddress_url_type(instance):
    assert isinstance(instance.url, str)


@given(instance=org::aries::common::EmailAddress_strategy)
def test_org::aries::common::emailaddress_url_setter(instance):
    original = instance.url
    instance.url = original
    assert instance.url == original

@given(instance=org::aries::common::EmailAddress_strategy)
def test_org::aries::common::emailaddress_firstName_type(instance):
    assert isinstance(instance.firstName, str)


@given(instance=org::aries::common::EmailAddress_strategy)
def test_org::aries::common::emailaddress_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original

@given(instance=org::aries::common::EmailAddress_strategy)
def test_org::aries::common::emailaddress_lastName_type(instance):
    assert isinstance(instance.lastName, str)


@given(instance=org::aries::common::EmailAddress_strategy)
def test_org::aries::common::emailaddress_lastName_setter(instance):
    original = instance.lastName
    instance.lastName = original
    assert instance.lastName == original

@given(instance=org::aries::common::EmailAccount_strategy)
@settings(max_examples=50)
def test_org::aries::common::emailaccount_instantiation(instance):
    assert isinstance(instance, org::aries::common::EmailAccount)

@given(instance=org::aries::common::EmailAccount_strategy)
def test_org::aries::common::emailaccount_enabled_type(instance):
    assert isinstance(instance.enabled, str)


@given(instance=org::aries::common::EmailAccount_strategy)
def test_org::aries::common::emailaccount_enabled_setter(instance):
    original = instance.enabled
    instance.enabled = original
    assert instance.enabled == original

@given(instance=org::aries::common::EmailAccount_strategy)
def test_org::aries::common::emailaccount_password_type(instance):
    assert isinstance(instance.password, str)


@given(instance=org::aries::common::EmailAccount_strategy)
def test_org::aries::common::emailaccount_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original

@given(instance=org::aries::common::EmailAccount_strategy)
def test_org::aries::common::emailaccount_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=org::aries::common::EmailAccount_strategy)
def test_org::aries::common::emailaccount_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=org::aries::common::EmailAccount_strategy)
def test_org::aries::common::emailaccount_lastName_type(instance):
    assert isinstance(instance.lastName, str)


@given(instance=org::aries::common::EmailAccount_strategy)
def test_org::aries::common::emailaccount_lastName_setter(instance):
    original = instance.lastName
    instance.lastName = original
    assert instance.lastName == original

@given(instance=org::aries::common::EmailAccount_strategy)
def test_org::aries::common::emailaccount_firstName_type(instance):
    assert isinstance(instance.firstName, str)


@given(instance=org::aries::common::EmailAccount_strategy)
def test_org::aries::common::emailaccount_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original

@given(instance=org::aries::common::EmailAccount_strategy)
def test_org::aries::common::emailaccount_userId_type(instance):
    assert isinstance(instance.userId, str)


@given(instance=org::aries::common::EmailAccount_strategy)
def test_org::aries::common::emailaccount_userId_setter(instance):
    original = instance.userId
    instance.userId = original
    assert instance.userId == original

@given(instance=ZipCode_strategy)
@settings(max_examples=50)
def test_zipcode_instantiation(instance):
    assert isinstance(instance, ZipCode)

@given(instance=User_strategy)
@settings(max_examples=50)
def test_user_instantiation(instance):
    assert isinstance(instance, User)

@given(instance=StreetAddress_strategy)
@settings(max_examples=50)
def test_streetaddress_instantiation(instance):
    assert isinstance(instance, StreetAddress)

@given(instance=PersonName_strategy)
@settings(max_examples=50)
def test_personname_instantiation(instance):
    assert isinstance(instance, PersonName)

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)

@given(instance=Note_strategy)
@settings(max_examples=50)
def test_note_instantiation(instance):
    assert isinstance(instance, Note)

@given(instance=MapEntry_strategy)
@settings(max_examples=50)
def test_mapentry_instantiation(instance):
    assert isinstance(instance, MapEntry)

@given(instance=Property_strategy)
@settings(max_examples=50)
def test_property_instantiation(instance):
    assert isinstance(instance, Property)

@given(instance=Properties_strategy)
@settings(max_examples=50)
def test_properties_instantiation(instance):
    assert isinstance(instance, Properties)

@given(instance=PhoneNumber_strategy)
@settings(max_examples=50)
def test_phonenumber_instantiation(instance):
    assert isinstance(instance, PhoneNumber)

@given(instance=EmailMessage_strategy)
@settings(max_examples=50)
def test_emailmessage_instantiation(instance):
    assert isinstance(instance, EmailMessage)

@given(instance=EmailBox_strategy)
@settings(max_examples=50)
def test_emailbox_instantiation(instance):
    assert isinstance(instance, EmailBox)

@given(instance=EmailAddressList_strategy)
@settings(max_examples=50)
def test_emailaddresslist_instantiation(instance):
    assert isinstance(instance, EmailAddressList)

@given(instance=EmailAddress_strategy)
@settings(max_examples=50)
def test_emailaddress_instantiation(instance):
    assert isinstance(instance, EmailAddress)

@given(instance=Map_strategy)
@settings(max_examples=50)
def test_map_instantiation(instance):
    assert isinstance(instance, Map)

@given(instance=Event_strategy)
@settings(max_examples=50)
def test_event_instantiation(instance):
    assert isinstance(instance, Event)

@given(instance=org::aries::common::EStringToStringMapEntry_strategy)
@settings(max_examples=50)
def test_org::aries::common::estringtostringmapentry_instantiation(instance):
    assert isinstance(instance, org::aries::common::EStringToStringMapEntry)

@given(instance=org::aries::common::DocumentRoot_strategy)
@settings(max_examples=50)
def test_org::aries::common::documentroot_instantiation(instance):
    assert isinstance(instance, org::aries::common::DocumentRoot)

@given(instance=org::aries::common::DocumentRoot_strategy)
def test_org::aries::common::documentroot_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=org::aries::common::DocumentRoot_strategy)
def test_org::aries::common::documentroot_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=EmailAccount_strategy)
@settings(max_examples=50)
def test_emailaccount_instantiation(instance):
    assert isinstance(instance, EmailAccount)

@given(instance=Attachment_strategy)
@settings(max_examples=50)
def test_attachment_instantiation(instance):
    assert isinstance(instance, Attachment)

@given(instance=org::aries::common::Attachment_strategy)
@settings(max_examples=50)
def test_org::aries::common::attachment_instantiation(instance):
    assert isinstance(instance, org::aries::common::Attachment)

@given(instance=org::aries::common::Attachment_strategy)
def test_org::aries::common::attachment_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=org::aries::common::Attachment_strategy)
def test_org::aries::common::attachment_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=org::aries::common::Attachment_strategy)
def test_org::aries::common::attachment_fileData_type(instance):
    assert isinstance(instance.fileData, str)


@given(instance=org::aries::common::Attachment_strategy)
def test_org::aries::common::attachment_fileData_setter(instance):
    original = instance.fileData
    instance.fileData = original
    assert instance.fileData == original

@given(instance=org::aries::common::Attachment_strategy)
def test_org::aries::common::attachment_fileName_type(instance):
    assert isinstance(instance.fileName, str)


@given(instance=org::aries::common::Attachment_strategy)
def test_org::aries::common::attachment_fileName_setter(instance):
    original = instance.fileName
    instance.fileName = original
    assert instance.fileName == original

@given(instance=org::aries::common::Attachment_strategy)
def test_org::aries::common::attachment_contentType_type(instance):
    assert isinstance(instance.contentType, str)


@given(instance=org::aries::common::Attachment_strategy)
def test_org::aries::common::attachment_contentType_setter(instance):
    original = instance.contentType
    instance.contentType = original
    assert instance.contentType == original

@given(instance=org::aries::common::Attachment_strategy)
def test_org::aries::common::attachment_size_type(instance):
    assert isinstance(instance.size, str)


@given(instance=org::aries::common::Attachment_strategy)
def test_org::aries::common::attachment_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=org::aries::common::Attachment_strategy)
def test_org::aries::common::attachment_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=org::aries::common::Attachment_strategy)
def test_org::aries::common::attachment_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
