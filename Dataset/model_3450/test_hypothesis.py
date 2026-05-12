import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    org_sgiusa_model_View,
    org_sgiusa_model_Users,
    org_sgiusa_model_StudyDeptInfo,
    org_sgiusa_model_User,
    org_sgiusa_model_StudyDeptExam,
    org_sgiusa_model_Registration,
    org_sgiusa_model_SchoolInfo,
    org_sgiusa_model_Preferences,
    org_sgiusa_model_Permission,
    org_sgiusa_model_Organization,
    org_sgiusa_model_MembershipInfo,
    org_sgiusa_model_Note,
    org_sgiusa_model_Members,
    org_sgiusa_model_MemberSearchCriteria,
    org_sgiusa_model_Member,
    org_sgiusa_model_LeadershipInfo,
    org_sgiusa_model_LeadershipRole,
    org_sgiusa_model_GohonzonInfo,
    org_sgiusa_model_FamilyMember,
    org_sgiusa_model_Event,
    StudyDeptInfo,
    StudyDeptExam,
    SchoolInfo,
    Registration,
    org_sgiusa_model_EmailList,
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
    MembershipInfo,
    org_sgiusa_model_EStringToStringMapEntry,
    org_sgiusa_model_DocumentRoot,
    GohonzonInfo,
    FamilyMember,
    EmailList,
    org_aries_common_User,
    org_aries_common_ZipCode,
    org_aries_common_StreetAddress,
    org_aries_common_PhoneNumber,
    org_aries_common_Property,
    org_aries_common_Properties,
    org_aries_common_Person,
    org_aries_common_PersonName,
    org_aries_common_EObject,
    org_aries_common_MapEntry,
    org_aries_common_Map,
    org_aries_common_Note,
    org_aries_common_Event,
    org_aries_common_EmailMessage,
    org_aries_common_EmailBox,
    org_aries_common_EmailAddressList,
    org_aries_common_EmailAddress,
    org_aries_common_EmailAccount,
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
    org_aries_common_EStringToStringMapEntry,
    org_aries_common_DocumentRoot,
    EmailAccount,
    Attachment,
    org_aries_common_Attachment,
    ActivityGroupName,
    PhoneNumberType,
    DivisionName,
    ViewType,
    Role,
    SubDivision,
    FamilyRelation,
    Capability,
    RoleType,
    EventStatus,
    OrganizationLevel,
    Country,
    Division,
    StudyDeptLanguage,
    GohonzonType,
    PositionName,
    ActivityGroup,
    SubDivisionName,
    Position,
    StudyDeptExamLevel,
    State,
    SchoolType,
    Language,
    Status,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_org_sgiusa_model_view_is_not_abstract():
    assert not inspect.isabstract(org_sgiusa_model_View)


def test_org_sgiusa_model_view_constructor_exists():
    assert callable(org_sgiusa_model_View.__init__)


def test_org_sgiusa_model_view_constructor_args():
    sig = inspect.signature(org_sgiusa_model_View.__init__)
    params = list(sig.parameters.keys())
    assert "viewType" in params, "Missing parameter 'viewType'"
    assert "id" in params, "Missing parameter 'id'"
    assert "userId" in params, "Missing parameter 'userId'"

def test_org_sgiusa_model_view_has_viewType():
    assert hasattr(org_sgiusa_model_View, "viewType")
    descriptor = None
    for klass in org_sgiusa_model_View.__mro__:
        if "viewType" in klass.__dict__:
            descriptor = klass.__dict__["viewType"]
            break
    assert isinstance(descriptor, property)

def test_org_sgiusa_model_view_has_id():
    assert hasattr(org_sgiusa_model_View, "id")
    descriptor = None
    for klass in org_sgiusa_model_View.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_org_sgiusa_model_view_has_userId():
    assert hasattr(org_sgiusa_model_View, "userId")
    descriptor = None
    for klass in org_sgiusa_model_View.__mro__:
        if "userId" in klass.__dict__:
            descriptor = klass.__dict__["userId"]
            break
    assert isinstance(descriptor, property)



def test_org_sgiusa_model_users_is_not_abstract():
    assert not inspect.isabstract(org_sgiusa_model_Users)


def test_org_sgiusa_model_users_constructor_exists():
    assert callable(org_sgiusa_model_Users.__init__)


def test_org_sgiusa_model_users_constructor_args():
    sig = inspect.signature(org_sgiusa_model_Users.__init__)
    params = list(sig.parameters.keys())



def test_org_sgiusa_model_studydeptinfo_is_not_abstract():
    assert not inspect.isabstract(org_sgiusa_model_StudyDeptInfo)


def test_org_sgiusa_model_studydeptinfo_constructor_exists():
    assert callable(org_sgiusa_model_StudyDeptInfo.__init__)


def test_org_sgiusa_model_studydeptinfo_constructor_args():
    sig = inspect.signature(org_sgiusa_model_StudyDeptInfo.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "lastUpdate" in params, "Missing parameter 'lastUpdate'"

def test_org_sgiusa_model_studydeptinfo_has_id():
    assert hasattr(org_sgiusa_model_StudyDeptInfo, "id")
    descriptor = None
    for klass in org_sgiusa_model_StudyDeptInfo.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_org_sgiusa_model_studydeptinfo_has_lastUpdate():
    assert hasattr(org_sgiusa_model_StudyDeptInfo, "lastUpdate")
    descriptor = None
    for klass in org_sgiusa_model_StudyDeptInfo.__mro__:
        if "lastUpdate" in klass.__dict__:
            descriptor = klass.__dict__["lastUpdate"]
            break
    assert isinstance(descriptor, property)



def test_org_sgiusa_model_user_is_not_abstract():
    assert not inspect.isabstract(org_sgiusa_model_User)


def test_org_sgiusa_model_user_constructor_exists():
    assert callable(org_sgiusa_model_User.__init__)


def test_org_sgiusa_model_user_constructor_args():
    sig = inspect.signature(org_sgiusa_model_User.__init__)
    params = list(sig.parameters.keys())
    assert "lastName" in params, "Missing parameter 'lastName'"
    assert "password" in params, "Missing parameter 'password'"
    assert "id" in params, "Missing parameter 'id'"
    assert "role" in params, "Missing parameter 'role'"
    assert "userId" in params, "Missing parameter 'userId'"
    assert "firstName" in params, "Missing parameter 'firstName'"
    assert "enabled" in params, "Missing parameter 'enabled'"

def test_org_sgiusa_model_user_has_lastName():
    assert hasattr(org_sgiusa_model_User, "lastName")
    descriptor = None
    for klass in org_sgiusa_model_User.__mro__:
        if "lastName" in klass.__dict__:
            descriptor = klass.__dict__["lastName"]
            break
    assert isinstance(descriptor, property)

def test_org_sgiusa_model_user_has_password():
    assert hasattr(org_sgiusa_model_User, "password")
    descriptor = None
    for klass in org_sgiusa_model_User.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)

def test_org_sgiusa_model_user_has_id():
    assert hasattr(org_sgiusa_model_User, "id")
    descriptor = None
    for klass in org_sgiusa_model_User.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_org_sgiusa_model_user_has_role():
    assert hasattr(org_sgiusa_model_User, "role")
    descriptor = None
    for klass in org_sgiusa_model_User.__mro__:
        if "role" in klass.__dict__:
            descriptor = klass.__dict__["role"]
            break
    assert isinstance(descriptor, property)

def test_org_sgiusa_model_user_has_userId():
    assert hasattr(org_sgiusa_model_User, "userId")
    descriptor = None
    for klass in org_sgiusa_model_User.__mro__:
        if "userId" in klass.__dict__:
            descriptor = klass.__dict__["userId"]
            break
    assert isinstance(descriptor, property)

def test_org_sgiusa_model_user_has_firstName():
    assert hasattr(org_sgiusa_model_User, "firstName")
    descriptor = None
    for klass in org_sgiusa_model_User.__mro__:
        if "firstName" in klass.__dict__:
            descriptor = klass.__dict__["firstName"]
            break
    assert isinstance(descriptor, property)

def test_org_sgiusa_model_user_has_enabled():
    assert hasattr(org_sgiusa_model_User, "enabled")
    descriptor = None
    for klass in org_sgiusa_model_User.__mro__:
        if "enabled" in klass.__dict__:
            descriptor = klass.__dict__["enabled"]
            break
    assert isinstance(descriptor, property)



def test_org_sgiusa_model_studydeptexam_is_not_abstract():
    assert not inspect.isabstract(org_sgiusa_model_StudyDeptExam)


def test_org_sgiusa_model_studydeptexam_constructor_exists():
    assert callable(org_sgiusa_model_StudyDeptExam.__init__)


def test_org_sgiusa_model_studydeptexam_constructor_args():
    sig = inspect.signature(org_sgiusa_model_StudyDeptExam.__init__)
    params = list(sig.parameters.keys())
    assert "examLocation" in params, "Missing parameter 'examLocation'"
    assert "lastUpdate" in params, "Missing parameter 'lastUpdate'"
    assert "id" in params, "Missing parameter 'id'"
    assert "current" in params, "Missing parameter 'current'"
    assert "examLevel" in params, "Missing parameter 'examLevel'"
    assert "examDate" in params, "Missing parameter 'examDate'"
    assert "examLanguage" in params, "Missing parameter 'examLanguage'"

def test_org_sgiusa_model_studydeptexam_has_examLocation():
    assert hasattr(org_sgiusa_model_StudyDeptExam, "examLocation")
    descriptor = None
    for klass in org_sgiusa_model_StudyDeptExam.__mro__:
        if "examLocation" in klass.__dict__:
            descriptor = klass.__dict__["examLocation"]
            break
    assert isinstance(descriptor, property)

def test_org_sgiusa_model_studydeptexam_has_lastUpdate():
    assert hasattr(org_sgiusa_model_StudyDeptExam, "lastUpdate")
    descriptor = None
    for klass in org_sgiusa_model_StudyDeptExam.__mro__:
        if "lastUpdate" in klass.__dict__:
            descriptor = klass.__dict__["lastUpdate"]
            break
    assert isinstance(descriptor, property)

def test_org_sgiusa_model_studydeptexam_has_id():
    assert hasattr(org_sgiusa_model_StudyDeptExam, "id")
    descriptor = None
    for klass in org_sgiusa_model_StudyDeptExam.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_org_sgiusa_model_studydeptexam_has_current():
    assert hasattr(org_sgiusa_model_StudyDeptExam, "current")
    descriptor = None
    for klass in org_sgiusa_model_StudyDeptExam.__mro__:
        if "current" in klass.__dict__:
            descriptor = klass.__dict__["current"]
            break
    assert isinstance(descriptor, property)

def test_org_sgiusa_model_studydeptexam_has_examLevel():
    assert hasattr(org_sgiusa_model_StudyDeptExam, "examLevel")
    descriptor = None
    for klass in org_sgiusa_model_StudyDeptExam.__mro__:
        if "examLevel" in klass.__dict__:
            descriptor = klass.__dict__["examLevel"]
            break
    assert isinstance(descriptor, property)

def test_org_sgiusa_model_studydeptexam_has_examDate():
    assert hasattr(org_sgiusa_model_StudyDeptExam, "examDate")
    descriptor = None
    for klass in org_sgiusa_model_StudyDeptExam.__mro__:
        if "examDate" in klass.__dict__:
            descriptor = klass.__dict__["examDate"]
            break
    assert isinstance(descriptor, property)

def test_org_sgiusa_model_studydeptexam_has_examLanguage():
    assert hasattr(org_sgiusa_model_StudyDeptExam, "examLanguage")
    descriptor = None
    for klass in org_sgiusa_model_StudyDeptExam.__mro__:
        if "examLanguage" in klass.__dict__:
            descriptor = klass.__dict__["examLanguage"]
            break
    assert isinstance(descriptor, property)



def test_org_sgiusa_model_registration_is_not_abstract():
    assert not inspect.isabstract(org_sgiusa_model_Registration)


def test_org_sgiusa_model_registration_constructor_exists():
    assert callable(org_sgiusa_model_Registration.__init__)


def test_org_sgiusa_model_registration_constructor_args():
    sig = inspect.signature(org_sgiusa_model_Registration.__init__)
    params = list(sig.parameters.keys())
    assert "aborted" in params, "Missing parameter 'aborted'"
    assert "cancelled" in params, "Missing parameter 'cancelled'"
    assert "id" in params, "Missing parameter 'id'"
    assert "date" in params, "Missing parameter 'date'"

def test_org_sgiusa_model_registration_has_aborted():
    assert hasattr(org_sgiusa_model_Registration, "aborted")
    descriptor = None
    for klass in org_sgiusa_model_Registration.__mro__:
        if "aborted" in klass.__dict__:
            descriptor = klass.__dict__["aborted"]
            break
    assert isinstance(descriptor, property)

def test_org_sgiusa_model_registration_has_cancelled():
    assert hasattr(org_sgiusa_model_Registration, "cancelled")
    descriptor = None
    for klass in org_sgiusa_model_Registration.__mro__:
        if "cancelled" in klass.__dict__:
            descriptor = klass.__dict__["cancelled"]
            break
    assert isinstance(descriptor, property)

def test_org_sgiusa_model_registration_has_id():
    assert hasattr(org_sgiusa_model_Registration, "id")
    descriptor = None
    for klass in org_sgiusa_model_Registration.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_org_sgiusa_model_registration_has_date():
    assert hasattr(org_sgiusa_model_Registration, "date")
    descriptor = None
    for klass in org_sgiusa_model_Registration.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)



def test_org_sgiusa_model_schoolinfo_is_not_abstract():
    assert not inspect.isabstract(org_sgiusa_model_SchoolInfo)


def test_org_sgiusa_model_schoolinfo_constructor_exists():
    assert callable(org_sgiusa_model_SchoolInfo.__init__)


def test_org_sgiusa_model_schoolinfo_constructor_args():
    sig = inspect.signature(org_sgiusa_model_SchoolInfo.__init__)
    params = list(sig.parameters.keys())
    assert "startDate" in params, "Missing parameter 'startDate'"
    assert "schoolName" in params, "Missing parameter 'schoolName'"
    assert "fieldOfStudy" in params, "Missing parameter 'fieldOfStudy'"
    assert "id" in params, "Missing parameter 'id'"
    assert "endDate" in params, "Missing parameter 'endDate'"
    assert "schoolType" in params, "Missing parameter 'schoolType'"
    assert "lastUpdate" in params, "Missing parameter 'lastUpdate'"

def test_org_sgiusa_model_schoolinfo_has_startDate():
    assert hasattr(org_sgiusa_model_SchoolInfo, "startDate")
    descriptor = None
    for klass in org_sgiusa_model_SchoolInfo.__mro__:
        if "startDate" in klass.__dict__:
            descriptor = klass.__dict__["startDate"]
            break
    assert isinstance(descriptor, property)

def test_org_sgiusa_model_schoolinfo_has_schoolName():
    assert hasattr(org_sgiusa_model_SchoolInfo, "schoolName")
    descriptor = None
    for klass in org_sgiusa_model_SchoolInfo.__mro__:
        if "schoolName" in klass.__dict__:
            descriptor = klass.__dict__["schoolName"]
            break
    assert isinstance(descriptor, property)

def test_org_sgiusa_model_schoolinfo_has_fieldOfStudy():
    assert hasattr(org_sgiusa_model_SchoolInfo, "fieldOfStudy")
    descriptor = None
    for klass in org_sgiusa_model_SchoolInfo.__mro__:
        if "fieldOfStudy" in klass.__dict__:
            descriptor = klass.__dict__["fieldOfStudy"]
            break
    assert isinstance(descriptor, property)

def test_org_sgiusa_model_schoolinfo_has_id():
    assert hasattr(org_sgiusa_model_SchoolInfo, "id")
    descriptor = None
    for klass in org_sgiusa_model_SchoolInfo.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_org_sgiusa_model_schoolinfo_has_endDate():
    assert hasattr(org_sgiusa_model_SchoolInfo, "endDate")
    descriptor = None
    for klass in org_sgiusa_model_SchoolInfo.__mro__:
        if "endDate" in klass.__dict__:
            descriptor = klass.__dict__["endDate"]
            break
    assert isinstance(descriptor, property)

def test_org_sgiusa_model_schoolinfo_has_schoolType():
    assert hasattr(org_sgiusa_model_SchoolInfo, "schoolType")
    descriptor = None
    for klass in org_sgiusa_model_SchoolInfo.__mro__:
        if "schoolType" in klass.__dict__:
            descriptor = klass.__dict__["schoolType"]
            break
    assert isinstance(descriptor, property)

def test_org_sgiusa_model_schoolinfo_has_lastUpdate():
    assert hasattr(org_sgiusa_model_SchoolInfo, "lastUpdate")
    descriptor = None
    for klass in org_sgiusa_model_SchoolInfo.__mro__:
        if "lastUpdate" in klass.__dict__:
            descriptor = klass.__dict__["lastUpdate"]
            break
    assert isinstance(descriptor, property)



def test_org_sgiusa_model_preferences_is_not_abstract():
    assert not inspect.isabstract(org_sgiusa_model_Preferences)


def test_org_sgiusa_model_preferences_constructor_exists():
    assert callable(org_sgiusa_model_Preferences.__init__)


def test_org_sgiusa_model_preferences_constructor_args():
    sig = inspect.signature(org_sgiusa_model_Preferences.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "themeId" in params, "Missing parameter 'themeId'"
    assert "selectedNode" in params, "Missing parameter 'selectedNode'"
    assert "userId" in params, "Missing parameter 'userId'"
    assert "enableTooltips" in params, "Missing parameter 'enableTooltips'"
    assert "selectedView" in params, "Missing parameter 'selectedView'"
    assert "openViews" in params, "Missing parameter 'openViews'"
    assert "openNodes" in params, "Missing parameter 'openNodes'"

def test_org_sgiusa_model_preferences_has_id():
    assert hasattr(org_sgiusa_model_Preferences, "id")
    descriptor = None
    for klass in org_sgiusa_model_Preferences.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_org_sgiusa_model_preferences_has_themeId():
    assert hasattr(org_sgiusa_model_Preferences, "themeId")
    descriptor = None
    for klass in org_sgiusa_model_Preferences.__mro__:
        if "themeId" in klass.__dict__:
            descriptor = klass.__dict__["themeId"]
            break
    assert isinstance(descriptor, property)

def test_org_sgiusa_model_preferences_has_selectedNode():
    assert hasattr(org_sgiusa_model_Preferences, "selectedNode")
    descriptor = None
    for klass in org_sgiusa_model_Preferences.__mro__:
        if "selectedNode" in klass.__dict__:
            descriptor = klass.__dict__["selectedNode"]
            break
    assert isinstance(descriptor, property)

def test_org_sgiusa_model_preferences_has_userId():
    assert hasattr(org_sgiusa_model_Preferences, "userId")
    descriptor = None
    for klass in org_sgiusa_model_Preferences.__mro__:
        if "userId" in klass.__dict__:
            descriptor = klass.__dict__["userId"]
            break
    assert isinstance(descriptor, property)

def test_org_sgiusa_model_preferences_has_enableTooltips():
    assert hasattr(org_sgiusa_model_Preferences, "enableTooltips")
    descriptor = None
    for klass in org_sgiusa_model_Preferences.__mro__:
        if "enableTooltips" in klass.__dict__:
            descriptor = klass.__dict__["enableTooltips"]
            break
    assert isinstance(descriptor, property)

def test_org_sgiusa_model_preferences_has_selectedView():
    assert hasattr(org_sgiusa_model_Preferences, "selectedView")
    descriptor = None
    for klass in org_sgiusa_model_Preferences.__mro__:
        if "selectedView" in klass.__dict__:
            descriptor = klass.__dict__["selectedView"]
            break
    assert isinstance(descriptor, property)

def test_org_sgiusa_model_preferences_has_openViews():
    assert hasattr(org_sgiusa_model_Preferences, "openViews")
    descriptor = None
    for klass in org_sgiusa_model_Preferences.__mro__:
        if "openViews" in klass.__dict__:
            descriptor = klass.__dict__["openViews"]
            break
    assert isinstance(descriptor, property)

def test_org_sgiusa_model_preferences_has_openNodes():
    assert hasattr(org_sgiusa_model_Preferences, "openNodes")
    descriptor = None
    for klass in org_sgiusa_model_Preferences.__mro__:
        if "openNodes" in klass.__dict__:
            descriptor = klass.__dict__["openNodes"]
            break
    assert isinstance(descriptor, property)



def test_org_sgiusa_model_permission_is_not_abstract():
    assert not inspect.isabstract(org_sgiusa_model_Permission)


def test_org_sgiusa_model_permission_constructor_exists():
    assert callable(org_sgiusa_model_Permission.__init__)


def test_org_sgiusa_model_permission_constructor_args():
    sig = inspect.signature(org_sgiusa_model_Permission.__init__)
    params = list(sig.parameters.keys())
    assert "divisions" in params, "Missing parameter 'divisions'"
    assert "activityGroups" in params, "Missing parameter 'activityGroups'"
    assert "userId" in params, "Missing parameter 'userId'"
    assert "subDivisions" in params, "Missing parameter 'subDivisions'"
    assert "capabilities" in params, "Missing parameter 'capabilities'"
    assert "enabled" in params, "Missing parameter 'enabled'"
    assert "id" in params, "Missing parameter 'id'"

def test_org_sgiusa_model_permission_has_divisions():
    assert hasattr(org_sgiusa_model_Permission, "divisions")
    descriptor = None
    for klass in org_sgiusa_model_Permission.__mro__:
        if "divisions" in klass.__dict__:
            descriptor = klass.__dict__["divisions"]
            break
    assert isinstance(descriptor, property)

def test_org_sgiusa_model_permission_has_activityGroups():
    assert hasattr(org_sgiusa_model_Permission, "activityGroups")
    descriptor = None
    for klass in org_sgiusa_model_Permission.__mro__:
        if "activityGroups" in klass.__dict__:
            descriptor = klass.__dict__["activityGroups"]
            break
    assert isinstance(descriptor, property)

def test_org_sgiusa_model_permission_has_userId():
    assert hasattr(org_sgiusa_model_Permission, "userId")
    descriptor = None
    for klass in org_sgiusa_model_Permission.__mro__:
        if "userId" in klass.__dict__:
            descriptor = klass.__dict__["userId"]
            break
    assert isinstance(descriptor, property)

def test_org_sgiusa_model_permission_has_subDivisions():
    assert hasattr(org_sgiusa_model_Permission, "subDivisions")
    descriptor = None
    for klass in org_sgiusa_model_Permission.__mro__:
        if "subDivisions" in klass.__dict__:
            descriptor = klass.__dict__["subDivisions"]
            break
    assert isinstance(descriptor, property)

def test_org_sgiusa_model_permission_has_capabilities():
    assert hasattr(org_sgiusa_model_Permission, "capabilities")
    descriptor = None
    for klass in org_sgiusa_model_Permission.__mro__:
        if "capabilities" in klass.__dict__:
            descriptor = klass.__dict__["capabilities"]
            break
    assert isinstance(descriptor, property)

def test_org_sgiusa_model_permission_has_enabled():
    assert hasattr(org_sgiusa_model_Permission, "enabled")
    descriptor = None
    for klass in org_sgiusa_model_Permission.__mro__:
        if "enabled" in klass.__dict__:
            descriptor = klass.__dict__["enabled"]
            break
    assert isinstance(descriptor, property)

def test_org_sgiusa_model_permission_has_id():
    assert hasattr(org_sgiusa_model_Permission, "id")
    descriptor = None
    for klass in org_sgiusa_model_Permission.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_org_sgiusa_model_organization_is_not_abstract():
    assert not inspect.isabstract(org_sgiusa_model_Organization)


def test_org_sgiusa_model_organization_constructor_exists():
    assert callable(org_sgiusa_model_Organization.__init__)


def test_org_sgiusa_model_organization_constructor_args():
    sig = inspect.signature(org_sgiusa_model_Organization.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "creationDate" in params, "Missing parameter 'creationDate'"
    assert "zipCodes" in params, "Missing parameter 'zipCodes'"
    assert "organizationId" in params, "Missing parameter 'organizationId'"
    assert "permissionId" in params, "Missing parameter 'permissionId'"
    assert "level" in params, "Missing parameter 'level'"
    assert "abbrv" in params, "Missing parameter 'abbrv'"
    assert "label" in params, "Missing parameter 'label'"
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"
    assert "lastUpdate" in params, "Missing parameter 'lastUpdate'"

def test_org_sgiusa_model_organization_has_id():
    assert hasattr(org_sgiusa_model_Organization, "id")
    descriptor = None
    for klass in org_sgiusa_model_Organization.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_org_sgiusa_model_organization_has_creationDate():
    assert hasattr(org_sgiusa_model_Organization, "creationDate")
    descriptor = None
    for klass in org_sgiusa_model_Organization.__mro__:
        if "creationDate" in klass.__dict__:
            descriptor = klass.__dict__["creationDate"]
            break
    assert isinstance(descriptor, property)

def test_org_sgiusa_model_organization_has_zipCodes():
    assert hasattr(org_sgiusa_model_Organization, "zipCodes")
    descriptor = None
    for klass in org_sgiusa_model_Organization.__mro__:
        if "zipCodes" in klass.__dict__:
            descriptor = klass.__dict__["zipCodes"]
            break
    assert isinstance(descriptor, property)

def test_org_sgiusa_model_organization_has_organizationId():
    assert hasattr(org_sgiusa_model_Organization, "organizationId")
    descriptor = None
    for klass in org_sgiusa_model_Organization.__mro__:
        if "organizationId" in klass.__dict__:
            descriptor = klass.__dict__["organizationId"]
            break
    assert isinstance(descriptor, property)

def test_org_sgiusa_model_organization_has_permissionId():
    assert hasattr(org_sgiusa_model_Organization, "permissionId")
    descriptor = None
    for klass in org_sgiusa_model_Organization.__mro__:
        if "permissionId" in klass.__dict__:
            descriptor = klass.__dict__["permissionId"]
            break
    assert isinstance(descriptor, property)

def test_org_sgiusa_model_organization_has_level():
    assert hasattr(org_sgiusa_model_Organization, "level")
    descriptor = None
    for klass in org_sgiusa_model_Organization.__mro__:
        if "level" in klass.__dict__:
            descriptor = klass.__dict__["level"]
            break
    assert isinstance(descriptor, property)

def test_org_sgiusa_model_organization_has_abbrv():
    assert hasattr(org_sgiusa_model_Organization, "abbrv")
    descriptor = None
    for klass in org_sgiusa_model_Organization.__mro__:
        if "abbrv" in klass.__dict__:
            descriptor = klass.__dict__["abbrv"]
            break
    assert isinstance(descriptor, property)

def test_org_sgiusa_model_organization_has_label():
    assert hasattr(org_sgiusa_model_Organization, "label")
    descriptor = None
    for klass in org_sgiusa_model_Organization.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_org_sgiusa_model_organization_has_type():
    assert hasattr(org_sgiusa_model_Organization, "type")
    descriptor = None
    for klass in org_sgiusa_model_Organization.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_org_sgiusa_model_organization_has_name():
    assert hasattr(org_sgiusa_model_Organization, "name")
    descriptor = None
    for klass in org_sgiusa_model_Organization.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_org_sgiusa_model_organization_has_lastUpdate():
    assert hasattr(org_sgiusa_model_Organization, "lastUpdate")
    descriptor = None
    for klass in org_sgiusa_model_Organization.__mro__:
        if "lastUpdate" in klass.__dict__:
            descriptor = klass.__dict__["lastUpdate"]
            break
    assert isinstance(descriptor, property)



def test_org_sgiusa_model_membershipinfo_is_not_abstract():
    assert not inspect.isabstract(org_sgiusa_model_MembershipInfo)


def test_org_sgiusa_model_membershipinfo_constructor_exists():
    assert callable(org_sgiusa_model_MembershipInfo.__init__)


def test_org_sgiusa_model_membershipinfo_constructor_args():
    sig = inspect.signature(org_sgiusa_model_MembershipInfo.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "friendOfSgi" in params, "Missing parameter 'friendOfSgi'"
    assert "lastUpdate" in params, "Missing parameter 'lastUpdate'"
    assert "notLocatable" in params, "Missing parameter 'notLocatable'"
    assert "notActivated" in params, "Missing parameter 'notActivated'"
    assert "receivedCertificate" in params, "Missing parameter 'receivedCertificate'"

def test_org_sgiusa_model_membershipinfo_has_id():
    assert hasattr(org_sgiusa_model_MembershipInfo, "id")
    descriptor = None
    for klass in org_sgiusa_model_MembershipInfo.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_org_sgiusa_model_membershipinfo_has_friendOfSgi():
    assert hasattr(org_sgiusa_model_MembershipInfo, "friendOfSgi")
    descriptor = None
    for klass in org_sgiusa_model_MembershipInfo.__mro__:
        if "friendOfSgi" in klass.__dict__:
            descriptor = klass.__dict__["friendOfSgi"]
            break
    assert isinstance(descriptor, property)

def test_org_sgiusa_model_membershipinfo_has_lastUpdate():
    assert hasattr(org_sgiusa_model_MembershipInfo, "lastUpdate")
    descriptor = None
    for klass in org_sgiusa_model_MembershipInfo.__mro__:
        if "lastUpdate" in klass.__dict__:
            descriptor = klass.__dict__["lastUpdate"]
            break
    assert isinstance(descriptor, property)

def test_org_sgiusa_model_membershipinfo_has_notLocatable():
    assert hasattr(org_sgiusa_model_MembershipInfo, "notLocatable")
    descriptor = None
    for klass in org_sgiusa_model_MembershipInfo.__mro__:
        if "notLocatable" in klass.__dict__:
            descriptor = klass.__dict__["notLocatable"]
            break
    assert isinstance(descriptor, property)

def test_org_sgiusa_model_membershipinfo_has_notActivated():
    assert hasattr(org_sgiusa_model_MembershipInfo, "notActivated")
    descriptor = None
    for klass in org_sgiusa_model_MembershipInfo.__mro__:
        if "notActivated" in klass.__dict__:
            descriptor = klass.__dict__["notActivated"]
            break
    assert isinstance(descriptor, property)

def test_org_sgiusa_model_membershipinfo_has_receivedCertificate():
    assert hasattr(org_sgiusa_model_MembershipInfo, "receivedCertificate")
    descriptor = None
    for klass in org_sgiusa_model_MembershipInfo.__mro__:
        if "receivedCertificate" in klass.__dict__:
            descriptor = klass.__dict__["receivedCertificate"]
            break
    assert isinstance(descriptor, property)



def test_org_sgiusa_model_note_is_not_abstract():
    assert not inspect.isabstract(org_sgiusa_model_Note)


def test_org_sgiusa_model_note_constructor_exists():
    assert callable(org_sgiusa_model_Note.__init__)


def test_org_sgiusa_model_note_constructor_args():
    sig = inspect.signature(org_sgiusa_model_Note.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "text" in params, "Missing parameter 'text'"
    assert "creationDate" in params, "Missing parameter 'creationDate'"
    assert "lastUpdate" in params, "Missing parameter 'lastUpdate'"

def test_org_sgiusa_model_note_has_id():
    assert hasattr(org_sgiusa_model_Note, "id")
    descriptor = None
    for klass in org_sgiusa_model_Note.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_org_sgiusa_model_note_has_text():
    assert hasattr(org_sgiusa_model_Note, "text")
    descriptor = None
    for klass in org_sgiusa_model_Note.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)

def test_org_sgiusa_model_note_has_creationDate():
    assert hasattr(org_sgiusa_model_Note, "creationDate")
    descriptor = None
    for klass in org_sgiusa_model_Note.__mro__:
        if "creationDate" in klass.__dict__:
            descriptor = klass.__dict__["creationDate"]
            break
    assert isinstance(descriptor, property)

def test_org_sgiusa_model_note_has_lastUpdate():
    assert hasattr(org_sgiusa_model_Note, "lastUpdate")
    descriptor = None
    for klass in org_sgiusa_model_Note.__mro__:
        if "lastUpdate" in klass.__dict__:
            descriptor = klass.__dict__["lastUpdate"]
            break
    assert isinstance(descriptor, property)



def test_org_sgiusa_model_members_is_not_abstract():
    assert not inspect.isabstract(org_sgiusa_model_Members)


def test_org_sgiusa_model_members_constructor_exists():
    assert callable(org_sgiusa_model_Members.__init__)


def test_org_sgiusa_model_members_constructor_args():
    sig = inspect.signature(org_sgiusa_model_Members.__init__)
    params = list(sig.parameters.keys())



def test_org_sgiusa_model_membersearchcriteria_is_not_abstract():
    assert not inspect.isabstract(org_sgiusa_model_MemberSearchCriteria)


def test_org_sgiusa_model_membersearchcriteria_constructor_exists():
    assert callable(org_sgiusa_model_MemberSearchCriteria.__init__)


def test_org_sgiusa_model_membersearchcriteria_constructor_args():
    sig = inspect.signature(org_sgiusa_model_MemberSearchCriteria.__init__)
    params = list(sig.parameters.keys())
    assert "divisions" in params, "Missing parameter 'divisions'"
    assert "subDivisions" in params, "Missing parameter 'subDivisions'"
    assert "activityGroups" in params, "Missing parameter 'activityGroups'"

def test_org_sgiusa_model_membersearchcriteria_has_divisions():
    assert hasattr(org_sgiusa_model_MemberSearchCriteria, "divisions")
    descriptor = None
    for klass in org_sgiusa_model_MemberSearchCriteria.__mro__:
        if "divisions" in klass.__dict__:
            descriptor = klass.__dict__["divisions"]
            break
    assert isinstance(descriptor, property)

def test_org_sgiusa_model_membersearchcriteria_has_subDivisions():
    assert hasattr(org_sgiusa_model_MemberSearchCriteria, "subDivisions")
    descriptor = None
    for klass in org_sgiusa_model_MemberSearchCriteria.__mro__:
        if "subDivisions" in klass.__dict__:
            descriptor = klass.__dict__["subDivisions"]
            break
    assert isinstance(descriptor, property)

def test_org_sgiusa_model_membersearchcriteria_has_activityGroups():
    assert hasattr(org_sgiusa_model_MemberSearchCriteria, "activityGroups")
    descriptor = None
    for klass in org_sgiusa_model_MemberSearchCriteria.__mro__:
        if "activityGroups" in klass.__dict__:
            descriptor = klass.__dict__["activityGroups"]
            break
    assert isinstance(descriptor, property)



def test_org_sgiusa_model_member_is_not_abstract():
    assert not inspect.isabstract(org_sgiusa_model_Member)


def test_org_sgiusa_model_member_constructor_exists():
    assert callable(org_sgiusa_model_Member.__init__)


def test_org_sgiusa_model_member_constructor_args():
    sig = inspect.signature(org_sgiusa_model_Member.__init__)
    params = list(sig.parameters.keys())
    assert "archived" in params, "Missing parameter 'archived'"
    assert "division" in params, "Missing parameter 'division'"
    assert "extraField2" in params, "Missing parameter 'extraField2'"
    assert "interests" in params, "Missing parameter 'interests'"
    assert "employer" in params, "Missing parameter 'employer'"
    assert "activityGroups" in params, "Missing parameter 'activityGroups'"
    assert "lastName" in params, "Missing parameter 'lastName'"
    assert "firstName" in params, "Missing parameter 'firstName'"
    assert "middleInitial" in params, "Missing parameter 'middleInitial'"
    assert "statusProfile" in params, "Missing parameter 'statusProfile'"
    assert "languages" in params, "Missing parameter 'languages'"
    assert "locatable" in params, "Missing parameter 'locatable'"
    assert "birthDate" in params, "Missing parameter 'birthDate'"
    assert "subDivision" in params, "Missing parameter 'subDivision'"
    assert "visible" in params, "Missing parameter 'visible'"
    assert "joinDate" in params, "Missing parameter 'joinDate'"
    assert "extraField1" in params, "Missing parameter 'extraField1'"
    assert "id" in params, "Missing parameter 'id'"
    assert "occupation" in params, "Missing parameter 'occupation'"

def test_org_sgiusa_model_member_has_archived():
    assert hasattr(org_sgiusa_model_Member, "archived")
    descriptor = None
    for klass in org_sgiusa_model_Member.__mro__:
        if "archived" in klass.__dict__:
            descriptor = klass.__dict__["archived"]
            break
    assert isinstance(descriptor, property)

def test_org_sgiusa_model_member_has_division():
    assert hasattr(org_sgiusa_model_Member, "division")
    descriptor = None
    for klass in org_sgiusa_model_Member.__mro__:
        if "division" in klass.__dict__:
            descriptor = klass.__dict__["division"]
            break
    assert isinstance(descriptor, property)

def test_org_sgiusa_model_member_has_extraField2():
    assert hasattr(org_sgiusa_model_Member, "extraField2")
    descriptor = None
    for klass in org_sgiusa_model_Member.__mro__:
        if "extraField2" in klass.__dict__:
            descriptor = klass.__dict__["extraField2"]
            break
    assert isinstance(descriptor, property)

def test_org_sgiusa_model_member_has_interests():
    assert hasattr(org_sgiusa_model_Member, "interests")
    descriptor = None
    for klass in org_sgiusa_model_Member.__mro__:
        if "interests" in klass.__dict__:
            descriptor = klass.__dict__["interests"]
            break
    assert isinstance(descriptor, property)

def test_org_sgiusa_model_member_has_employer():
    assert hasattr(org_sgiusa_model_Member, "employer")
    descriptor = None
    for klass in org_sgiusa_model_Member.__mro__:
        if "employer" in klass.__dict__:
            descriptor = klass.__dict__["employer"]
            break
    assert isinstance(descriptor, property)

def test_org_sgiusa_model_member_has_activityGroups():
    assert hasattr(org_sgiusa_model_Member, "activityGroups")
    descriptor = None
    for klass in org_sgiusa_model_Member.__mro__:
        if "activityGroups" in klass.__dict__:
            descriptor = klass.__dict__["activityGroups"]
            break
    assert isinstance(descriptor, property)

def test_org_sgiusa_model_member_has_lastName():
    assert hasattr(org_sgiusa_model_Member, "lastName")
    descriptor = None
    for klass in org_sgiusa_model_Member.__mro__:
        if "lastName" in klass.__dict__:
            descriptor = klass.__dict__["lastName"]
            break
    assert isinstance(descriptor, property)

def test_org_sgiusa_model_member_has_firstName():
    assert hasattr(org_sgiusa_model_Member, "firstName")
    descriptor = None
    for klass in org_sgiusa_model_Member.__mro__:
        if "firstName" in klass.__dict__:
            descriptor = klass.__dict__["firstName"]
            break
    assert isinstance(descriptor, property)

def test_org_sgiusa_model_member_has_middleInitial():
    assert hasattr(org_sgiusa_model_Member, "middleInitial")
    descriptor = None
    for klass in org_sgiusa_model_Member.__mro__:
        if "middleInitial" in klass.__dict__:
            descriptor = klass.__dict__["middleInitial"]
            break
    assert isinstance(descriptor, property)

def test_org_sgiusa_model_member_has_statusProfile():
    assert hasattr(org_sgiusa_model_Member, "statusProfile")
    descriptor = None
    for klass in org_sgiusa_model_Member.__mro__:
        if "statusProfile" in klass.__dict__:
            descriptor = klass.__dict__["statusProfile"]
            break
    assert isinstance(descriptor, property)

def test_org_sgiusa_model_member_has_languages():
    assert hasattr(org_sgiusa_model_Member, "languages")
    descriptor = None
    for klass in org_sgiusa_model_Member.__mro__:
        if "languages" in klass.__dict__:
            descriptor = klass.__dict__["languages"]
            break
    assert isinstance(descriptor, property)

def test_org_sgiusa_model_member_has_locatable():
    assert hasattr(org_sgiusa_model_Member, "locatable")
    descriptor = None
    for klass in org_sgiusa_model_Member.__mro__:
        if "locatable" in klass.__dict__:
            descriptor = klass.__dict__["locatable"]
            break
    assert isinstance(descriptor, property)

def test_org_sgiusa_model_member_has_birthDate():
    assert hasattr(org_sgiusa_model_Member, "birthDate")
    descriptor = None
    for klass in org_sgiusa_model_Member.__mro__:
        if "birthDate" in klass.__dict__:
            descriptor = klass.__dict__["birthDate"]
            break
    assert isinstance(descriptor, property)

def test_org_sgiusa_model_member_has_subDivision():
    assert hasattr(org_sgiusa_model_Member, "subDivision")
    descriptor = None
    for klass in org_sgiusa_model_Member.__mro__:
        if "subDivision" in klass.__dict__:
            descriptor = klass.__dict__["subDivision"]
            break
    assert isinstance(descriptor, property)

def test_org_sgiusa_model_member_has_visible():
    assert hasattr(org_sgiusa_model_Member, "visible")
    descriptor = None
    for klass in org_sgiusa_model_Member.__mro__:
        if "visible" in klass.__dict__:
            descriptor = klass.__dict__["visible"]
            break
    assert isinstance(descriptor, property)

def test_org_sgiusa_model_member_has_joinDate():
    assert hasattr(org_sgiusa_model_Member, "joinDate")
    descriptor = None
    for klass in org_sgiusa_model_Member.__mro__:
        if "joinDate" in klass.__dict__:
            descriptor = klass.__dict__["joinDate"]
            break
    assert isinstance(descriptor, property)

def test_org_sgiusa_model_member_has_extraField1():
    assert hasattr(org_sgiusa_model_Member, "extraField1")
    descriptor = None
    for klass in org_sgiusa_model_Member.__mro__:
        if "extraField1" in klass.__dict__:
            descriptor = klass.__dict__["extraField1"]
            break
    assert isinstance(descriptor, property)

def test_org_sgiusa_model_member_has_id():
    assert hasattr(org_sgiusa_model_Member, "id")
    descriptor = None
    for klass in org_sgiusa_model_Member.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_org_sgiusa_model_member_has_occupation():
    assert hasattr(org_sgiusa_model_Member, "occupation")
    descriptor = None
    for klass in org_sgiusa_model_Member.__mro__:
        if "occupation" in klass.__dict__:
            descriptor = klass.__dict__["occupation"]
            break
    assert isinstance(descriptor, property)



def test_org_sgiusa_model_leadershipinfo_is_not_abstract():
    assert not inspect.isabstract(org_sgiusa_model_LeadershipInfo)


def test_org_sgiusa_model_leadershipinfo_constructor_exists():
    assert callable(org_sgiusa_model_LeadershipInfo.__init__)


def test_org_sgiusa_model_leadershipinfo_constructor_args():
    sig = inspect.signature(org_sgiusa_model_LeadershipInfo.__init__)
    params = list(sig.parameters.keys())
    assert "manualSigned" in params, "Missing parameter 'manualSigned'"
    assert "examPassed" in params, "Missing parameter 'examPassed'"
    assert "manualSignedDate" in params, "Missing parameter 'manualSignedDate'"
    assert "id" in params, "Missing parameter 'id'"
    assert "examPassedDate" in params, "Missing parameter 'examPassedDate'"
    assert "lastUpdate" in params, "Missing parameter 'lastUpdate'"

def test_org_sgiusa_model_leadershipinfo_has_manualSigned():
    assert hasattr(org_sgiusa_model_LeadershipInfo, "manualSigned")
    descriptor = None
    for klass in org_sgiusa_model_LeadershipInfo.__mro__:
        if "manualSigned" in klass.__dict__:
            descriptor = klass.__dict__["manualSigned"]
            break
    assert isinstance(descriptor, property)

def test_org_sgiusa_model_leadershipinfo_has_examPassed():
    assert hasattr(org_sgiusa_model_LeadershipInfo, "examPassed")
    descriptor = None
    for klass in org_sgiusa_model_LeadershipInfo.__mro__:
        if "examPassed" in klass.__dict__:
            descriptor = klass.__dict__["examPassed"]
            break
    assert isinstance(descriptor, property)

def test_org_sgiusa_model_leadershipinfo_has_manualSignedDate():
    assert hasattr(org_sgiusa_model_LeadershipInfo, "manualSignedDate")
    descriptor = None
    for klass in org_sgiusa_model_LeadershipInfo.__mro__:
        if "manualSignedDate" in klass.__dict__:
            descriptor = klass.__dict__["manualSignedDate"]
            break
    assert isinstance(descriptor, property)

def test_org_sgiusa_model_leadershipinfo_has_id():
    assert hasattr(org_sgiusa_model_LeadershipInfo, "id")
    descriptor = None
    for klass in org_sgiusa_model_LeadershipInfo.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_org_sgiusa_model_leadershipinfo_has_examPassedDate():
    assert hasattr(org_sgiusa_model_LeadershipInfo, "examPassedDate")
    descriptor = None
    for klass in org_sgiusa_model_LeadershipInfo.__mro__:
        if "examPassedDate" in klass.__dict__:
            descriptor = klass.__dict__["examPassedDate"]
            break
    assert isinstance(descriptor, property)

def test_org_sgiusa_model_leadershipinfo_has_lastUpdate():
    assert hasattr(org_sgiusa_model_LeadershipInfo, "lastUpdate")
    descriptor = None
    for klass in org_sgiusa_model_LeadershipInfo.__mro__:
        if "lastUpdate" in klass.__dict__:
            descriptor = klass.__dict__["lastUpdate"]
            break
    assert isinstance(descriptor, property)



def test_org_sgiusa_model_leadershiprole_is_not_abstract():
    assert not inspect.isabstract(org_sgiusa_model_LeadershipRole)


def test_org_sgiusa_model_leadershiprole_constructor_exists():
    assert callable(org_sgiusa_model_LeadershipRole.__init__)


def test_org_sgiusa_model_leadershiprole_constructor_args():
    sig = inspect.signature(org_sgiusa_model_LeadershipRole.__init__)
    params = list(sig.parameters.keys())
    assert "activityGroup" in params, "Missing parameter 'activityGroup'"
    assert "position" in params, "Missing parameter 'position'"
    assert "endDate" in params, "Missing parameter 'endDate'"
    assert "active" in params, "Missing parameter 'active'"
    assert "division" in params, "Missing parameter 'division'"
    assert "subDivision" in params, "Missing parameter 'subDivision'"
    assert "startDate" in params, "Missing parameter 'startDate'"
    assert "id" in params, "Missing parameter 'id'"
    assert "level" in params, "Missing parameter 'level'"
    assert "lastUpdate" in params, "Missing parameter 'lastUpdate'"

def test_org_sgiusa_model_leadershiprole_has_activityGroup():
    assert hasattr(org_sgiusa_model_LeadershipRole, "activityGroup")
    descriptor = None
    for klass in org_sgiusa_model_LeadershipRole.__mro__:
        if "activityGroup" in klass.__dict__:
            descriptor = klass.__dict__["activityGroup"]
            break
    assert isinstance(descriptor, property)

def test_org_sgiusa_model_leadershiprole_has_position():
    assert hasattr(org_sgiusa_model_LeadershipRole, "position")
    descriptor = None
    for klass in org_sgiusa_model_LeadershipRole.__mro__:
        if "position" in klass.__dict__:
            descriptor = klass.__dict__["position"]
            break
    assert isinstance(descriptor, property)

def test_org_sgiusa_model_leadershiprole_has_endDate():
    assert hasattr(org_sgiusa_model_LeadershipRole, "endDate")
    descriptor = None
    for klass in org_sgiusa_model_LeadershipRole.__mro__:
        if "endDate" in klass.__dict__:
            descriptor = klass.__dict__["endDate"]
            break
    assert isinstance(descriptor, property)

def test_org_sgiusa_model_leadershiprole_has_active():
    assert hasattr(org_sgiusa_model_LeadershipRole, "active")
    descriptor = None
    for klass in org_sgiusa_model_LeadershipRole.__mro__:
        if "active" in klass.__dict__:
            descriptor = klass.__dict__["active"]
            break
    assert isinstance(descriptor, property)

def test_org_sgiusa_model_leadershiprole_has_division():
    assert hasattr(org_sgiusa_model_LeadershipRole, "division")
    descriptor = None
    for klass in org_sgiusa_model_LeadershipRole.__mro__:
        if "division" in klass.__dict__:
            descriptor = klass.__dict__["division"]
            break
    assert isinstance(descriptor, property)

def test_org_sgiusa_model_leadershiprole_has_subDivision():
    assert hasattr(org_sgiusa_model_LeadershipRole, "subDivision")
    descriptor = None
    for klass in org_sgiusa_model_LeadershipRole.__mro__:
        if "subDivision" in klass.__dict__:
            descriptor = klass.__dict__["subDivision"]
            break
    assert isinstance(descriptor, property)

def test_org_sgiusa_model_leadershiprole_has_startDate():
    assert hasattr(org_sgiusa_model_LeadershipRole, "startDate")
    descriptor = None
    for klass in org_sgiusa_model_LeadershipRole.__mro__:
        if "startDate" in klass.__dict__:
            descriptor = klass.__dict__["startDate"]
            break
    assert isinstance(descriptor, property)

def test_org_sgiusa_model_leadershiprole_has_id():
    assert hasattr(org_sgiusa_model_LeadershipRole, "id")
    descriptor = None
    for klass in org_sgiusa_model_LeadershipRole.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_org_sgiusa_model_leadershiprole_has_level():
    assert hasattr(org_sgiusa_model_LeadershipRole, "level")
    descriptor = None
    for klass in org_sgiusa_model_LeadershipRole.__mro__:
        if "level" in klass.__dict__:
            descriptor = klass.__dict__["level"]
            break
    assert isinstance(descriptor, property)

def test_org_sgiusa_model_leadershiprole_has_lastUpdate():
    assert hasattr(org_sgiusa_model_LeadershipRole, "lastUpdate")
    descriptor = None
    for klass in org_sgiusa_model_LeadershipRole.__mro__:
        if "lastUpdate" in klass.__dict__:
            descriptor = klass.__dict__["lastUpdate"]
            break
    assert isinstance(descriptor, property)



def test_org_sgiusa_model_gohonzoninfo_is_not_abstract():
    assert not inspect.isabstract(org_sgiusa_model_GohonzonInfo)


def test_org_sgiusa_model_gohonzoninfo_constructor_exists():
    assert callable(org_sgiusa_model_GohonzonInfo.__init__)


def test_org_sgiusa_model_gohonzoninfo_constructor_args():
    sig = inspect.signature(org_sgiusa_model_GohonzonInfo.__init__)
    params = list(sig.parameters.keys())
    assert "returned" in params, "Missing parameter 'returned'"
    assert "gohonzonType" in params, "Missing parameter 'gohonzonType'"
    assert "receiveDate" in params, "Missing parameter 'receiveDate'"
    assert "returnDate" in params, "Missing parameter 'returnDate'"
    assert "id" in params, "Missing parameter 'id'"
    assert "lastUpdate" in params, "Missing parameter 'lastUpdate'"

def test_org_sgiusa_model_gohonzoninfo_has_returned():
    assert hasattr(org_sgiusa_model_GohonzonInfo, "returned")
    descriptor = None
    for klass in org_sgiusa_model_GohonzonInfo.__mro__:
        if "returned" in klass.__dict__:
            descriptor = klass.__dict__["returned"]
            break
    assert isinstance(descriptor, property)

def test_org_sgiusa_model_gohonzoninfo_has_gohonzonType():
    assert hasattr(org_sgiusa_model_GohonzonInfo, "gohonzonType")
    descriptor = None
    for klass in org_sgiusa_model_GohonzonInfo.__mro__:
        if "gohonzonType" in klass.__dict__:
            descriptor = klass.__dict__["gohonzonType"]
            break
    assert isinstance(descriptor, property)

def test_org_sgiusa_model_gohonzoninfo_has_receiveDate():
    assert hasattr(org_sgiusa_model_GohonzonInfo, "receiveDate")
    descriptor = None
    for klass in org_sgiusa_model_GohonzonInfo.__mro__:
        if "receiveDate" in klass.__dict__:
            descriptor = klass.__dict__["receiveDate"]
            break
    assert isinstance(descriptor, property)

def test_org_sgiusa_model_gohonzoninfo_has_returnDate():
    assert hasattr(org_sgiusa_model_GohonzonInfo, "returnDate")
    descriptor = None
    for klass in org_sgiusa_model_GohonzonInfo.__mro__:
        if "returnDate" in klass.__dict__:
            descriptor = klass.__dict__["returnDate"]
            break
    assert isinstance(descriptor, property)

def test_org_sgiusa_model_gohonzoninfo_has_id():
    assert hasattr(org_sgiusa_model_GohonzonInfo, "id")
    descriptor = None
    for klass in org_sgiusa_model_GohonzonInfo.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_org_sgiusa_model_gohonzoninfo_has_lastUpdate():
    assert hasattr(org_sgiusa_model_GohonzonInfo, "lastUpdate")
    descriptor = None
    for klass in org_sgiusa_model_GohonzonInfo.__mro__:
        if "lastUpdate" in klass.__dict__:
            descriptor = klass.__dict__["lastUpdate"]
            break
    assert isinstance(descriptor, property)



def test_org_sgiusa_model_familymember_is_not_abstract():
    assert not inspect.isabstract(org_sgiusa_model_FamilyMember)


def test_org_sgiusa_model_familymember_constructor_exists():
    assert callable(org_sgiusa_model_FamilyMember.__init__)


def test_org_sgiusa_model_familymember_constructor_args():
    sig = inspect.signature(org_sgiusa_model_FamilyMember.__init__)
    params = list(sig.parameters.keys())
    assert "familyRelation" in params, "Missing parameter 'familyRelation'"
    assert "sgiMember" in params, "Missing parameter 'sgiMember'"
    assert "id" in params, "Missing parameter 'id'"
    assert "personName" in params, "Missing parameter 'personName'"
    assert "lastUpdate" in params, "Missing parameter 'lastUpdate'"

def test_org_sgiusa_model_familymember_has_familyRelation():
    assert hasattr(org_sgiusa_model_FamilyMember, "familyRelation")
    descriptor = None
    for klass in org_sgiusa_model_FamilyMember.__mro__:
        if "familyRelation" in klass.__dict__:
            descriptor = klass.__dict__["familyRelation"]
            break
    assert isinstance(descriptor, property)

def test_org_sgiusa_model_familymember_has_sgiMember():
    assert hasattr(org_sgiusa_model_FamilyMember, "sgiMember")
    descriptor = None
    for klass in org_sgiusa_model_FamilyMember.__mro__:
        if "sgiMember" in klass.__dict__:
            descriptor = klass.__dict__["sgiMember"]
            break
    assert isinstance(descriptor, property)

def test_org_sgiusa_model_familymember_has_id():
    assert hasattr(org_sgiusa_model_FamilyMember, "id")
    descriptor = None
    for klass in org_sgiusa_model_FamilyMember.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_org_sgiusa_model_familymember_has_personName():
    assert hasattr(org_sgiusa_model_FamilyMember, "personName")
    descriptor = None
    for klass in org_sgiusa_model_FamilyMember.__mro__:
        if "personName" in klass.__dict__:
            descriptor = klass.__dict__["personName"]
            break
    assert isinstance(descriptor, property)

def test_org_sgiusa_model_familymember_has_lastUpdate():
    assert hasattr(org_sgiusa_model_FamilyMember, "lastUpdate")
    descriptor = None
    for klass in org_sgiusa_model_FamilyMember.__mro__:
        if "lastUpdate" in klass.__dict__:
            descriptor = klass.__dict__["lastUpdate"]
            break
    assert isinstance(descriptor, property)



def test_org_sgiusa_model_event_is_not_abstract():
    assert not inspect.isabstract(org_sgiusa_model_Event)


def test_org_sgiusa_model_event_constructor_exists():
    assert callable(org_sgiusa_model_Event.__init__)


def test_org_sgiusa_model_event_constructor_args():
    sig = inspect.signature(org_sgiusa_model_Event.__init__)
    params = list(sig.parameters.keys())
    assert "status" in params, "Missing parameter 'status'"
    assert "userId" in params, "Missing parameter 'userId'"
    assert "id" in params, "Missing parameter 'id'"
    assert "divisions" in params, "Missing parameter 'divisions'"
    assert "subDivisions" in params, "Missing parameter 'subDivisions'"

def test_org_sgiusa_model_event_has_status():
    assert hasattr(org_sgiusa_model_Event, "status")
    descriptor = None
    for klass in org_sgiusa_model_Event.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)

def test_org_sgiusa_model_event_has_userId():
    assert hasattr(org_sgiusa_model_Event, "userId")
    descriptor = None
    for klass in org_sgiusa_model_Event.__mro__:
        if "userId" in klass.__dict__:
            descriptor = klass.__dict__["userId"]
            break
    assert isinstance(descriptor, property)

def test_org_sgiusa_model_event_has_id():
    assert hasattr(org_sgiusa_model_Event, "id")
    descriptor = None
    for klass in org_sgiusa_model_Event.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_org_sgiusa_model_event_has_divisions():
    assert hasattr(org_sgiusa_model_Event, "divisions")
    descriptor = None
    for klass in org_sgiusa_model_Event.__mro__:
        if "divisions" in klass.__dict__:
            descriptor = klass.__dict__["divisions"]
            break
    assert isinstance(descriptor, property)

def test_org_sgiusa_model_event_has_subDivisions():
    assert hasattr(org_sgiusa_model_Event, "subDivisions")
    descriptor = None
    for klass in org_sgiusa_model_Event.__mro__:
        if "subDivisions" in klass.__dict__:
            descriptor = klass.__dict__["subDivisions"]
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



def test_org_sgiusa_model_emaillist_is_not_abstract():
    assert not inspect.isabstract(org_sgiusa_model_EmailList)


def test_org_sgiusa_model_emaillist_constructor_exists():
    assert callable(org_sgiusa_model_EmailList.__init__)


def test_org_sgiusa_model_emaillist_constructor_args():
    sig = inspect.signature(org_sgiusa_model_EmailList.__init__)
    params = list(sig.parameters.keys())
    assert "subDivisions" in params, "Missing parameter 'subDivisions'"
    assert "divisions" in params, "Missing parameter 'divisions'"
    assert "id" in params, "Missing parameter 'id'"
    assert "enabled" in params, "Missing parameter 'enabled'"
    assert "activityGroups" in params, "Missing parameter 'activityGroups'"

def test_org_sgiusa_model_emaillist_has_subDivisions():
    assert hasattr(org_sgiusa_model_EmailList, "subDivisions")
    descriptor = None
    for klass in org_sgiusa_model_EmailList.__mro__:
        if "subDivisions" in klass.__dict__:
            descriptor = klass.__dict__["subDivisions"]
            break
    assert isinstance(descriptor, property)

def test_org_sgiusa_model_emaillist_has_divisions():
    assert hasattr(org_sgiusa_model_EmailList, "divisions")
    descriptor = None
    for klass in org_sgiusa_model_EmailList.__mro__:
        if "divisions" in klass.__dict__:
            descriptor = klass.__dict__["divisions"]
            break
    assert isinstance(descriptor, property)

def test_org_sgiusa_model_emaillist_has_id():
    assert hasattr(org_sgiusa_model_EmailList, "id")
    descriptor = None
    for klass in org_sgiusa_model_EmailList.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_org_sgiusa_model_emaillist_has_enabled():
    assert hasattr(org_sgiusa_model_EmailList, "enabled")
    descriptor = None
    for klass in org_sgiusa_model_EmailList.__mro__:
        if "enabled" in klass.__dict__:
            descriptor = klass.__dict__["enabled"]
            break
    assert isinstance(descriptor, property)

def test_org_sgiusa_model_emaillist_has_activityGroups():
    assert hasattr(org_sgiusa_model_EmailList, "activityGroups")
    descriptor = None
    for klass in org_sgiusa_model_EmailList.__mro__:
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



def test_membershipinfo_is_not_abstract():
    assert not inspect.isabstract(MembershipInfo)


def test_membershipinfo_constructor_exists():
    assert callable(MembershipInfo.__init__)


def test_membershipinfo_constructor_args():
    sig = inspect.signature(MembershipInfo.__init__)
    params = list(sig.parameters.keys())



def test_org_sgiusa_model_estringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(org_sgiusa_model_EStringToStringMapEntry)


def test_org_sgiusa_model_estringtostringmapentry_constructor_exists():
    assert callable(org_sgiusa_model_EStringToStringMapEntry.__init__)


def test_org_sgiusa_model_estringtostringmapentry_constructor_args():
    sig = inspect.signature(org_sgiusa_model_EStringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())



def test_org_sgiusa_model_documentroot_is_not_abstract():
    assert not inspect.isabstract(org_sgiusa_model_DocumentRoot)


def test_org_sgiusa_model_documentroot_constructor_exists():
    assert callable(org_sgiusa_model_DocumentRoot.__init__)


def test_org_sgiusa_model_documentroot_constructor_args():
    sig = inspect.signature(org_sgiusa_model_DocumentRoot.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_org_sgiusa_model_documentroot_has_mixed():
    assert hasattr(org_sgiusa_model_DocumentRoot, "mixed")
    descriptor = None
    for klass in org_sgiusa_model_DocumentRoot.__mro__:
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



def test_org_aries_common_user_is_not_abstract():
    assert not inspect.isabstract(org_aries_common_User)


def test_org_aries_common_user_constructor_exists():
    assert callable(org_aries_common_User.__init__)


def test_org_aries_common_user_constructor_args():
    sig = inspect.signature(org_aries_common_User.__init__)
    params = list(sig.parameters.keys())
    assert "firstName" in params, "Missing parameter 'firstName'"
    assert "userId" in params, "Missing parameter 'userId'"
    assert "enabled" in params, "Missing parameter 'enabled'"
    assert "id" in params, "Missing parameter 'id'"
    assert "lastName" in params, "Missing parameter 'lastName'"
    assert "password" in params, "Missing parameter 'password'"

def test_org_aries_common_user_has_firstName():
    assert hasattr(org_aries_common_User, "firstName")
    descriptor = None
    for klass in org_aries_common_User.__mro__:
        if "firstName" in klass.__dict__:
            descriptor = klass.__dict__["firstName"]
            break
    assert isinstance(descriptor, property)

def test_org_aries_common_user_has_userId():
    assert hasattr(org_aries_common_User, "userId")
    descriptor = None
    for klass in org_aries_common_User.__mro__:
        if "userId" in klass.__dict__:
            descriptor = klass.__dict__["userId"]
            break
    assert isinstance(descriptor, property)

def test_org_aries_common_user_has_enabled():
    assert hasattr(org_aries_common_User, "enabled")
    descriptor = None
    for klass in org_aries_common_User.__mro__:
        if "enabled" in klass.__dict__:
            descriptor = klass.__dict__["enabled"]
            break
    assert isinstance(descriptor, property)

def test_org_aries_common_user_has_id():
    assert hasattr(org_aries_common_User, "id")
    descriptor = None
    for klass in org_aries_common_User.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_org_aries_common_user_has_lastName():
    assert hasattr(org_aries_common_User, "lastName")
    descriptor = None
    for klass in org_aries_common_User.__mro__:
        if "lastName" in klass.__dict__:
            descriptor = klass.__dict__["lastName"]
            break
    assert isinstance(descriptor, property)

def test_org_aries_common_user_has_password():
    assert hasattr(org_aries_common_User, "password")
    descriptor = None
    for klass in org_aries_common_User.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)



def test_org_aries_common_zipcode_is_not_abstract():
    assert not inspect.isabstract(org_aries_common_ZipCode)


def test_org_aries_common_zipcode_constructor_exists():
    assert callable(org_aries_common_ZipCode.__init__)


def test_org_aries_common_zipcode_constructor_args():
    sig = inspect.signature(org_aries_common_ZipCode.__init__)
    params = list(sig.parameters.keys())
    assert "country" in params, "Missing parameter 'country'"
    assert "extension" in params, "Missing parameter 'extension'"
    assert "number" in params, "Missing parameter 'number'"

def test_org_aries_common_zipcode_has_country():
    assert hasattr(org_aries_common_ZipCode, "country")
    descriptor = None
    for klass in org_aries_common_ZipCode.__mro__:
        if "country" in klass.__dict__:
            descriptor = klass.__dict__["country"]
            break
    assert isinstance(descriptor, property)

def test_org_aries_common_zipcode_has_extension():
    assert hasattr(org_aries_common_ZipCode, "extension")
    descriptor = None
    for klass in org_aries_common_ZipCode.__mro__:
        if "extension" in klass.__dict__:
            descriptor = klass.__dict__["extension"]
            break
    assert isinstance(descriptor, property)

def test_org_aries_common_zipcode_has_number():
    assert hasattr(org_aries_common_ZipCode, "number")
    descriptor = None
    for klass in org_aries_common_ZipCode.__mro__:
        if "number" in klass.__dict__:
            descriptor = klass.__dict__["number"]
            break
    assert isinstance(descriptor, property)



def test_org_aries_common_streetaddress_is_not_abstract():
    assert not inspect.isabstract(org_aries_common_StreetAddress)


def test_org_aries_common_streetaddress_constructor_exists():
    assert callable(org_aries_common_StreetAddress.__init__)


def test_org_aries_common_streetaddress_constructor_args():
    sig = inspect.signature(org_aries_common_StreetAddress.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "city" in params, "Missing parameter 'city'"
    assert "country" in params, "Missing parameter 'country'"
    assert "latitude" in params, "Missing parameter 'latitude'"
    assert "longitude" in params, "Missing parameter 'longitude'"
    assert "street" in params, "Missing parameter 'street'"
    assert "state" in params, "Missing parameter 'state'"

def test_org_aries_common_streetaddress_has_id():
    assert hasattr(org_aries_common_StreetAddress, "id")
    descriptor = None
    for klass in org_aries_common_StreetAddress.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_org_aries_common_streetaddress_has_city():
    assert hasattr(org_aries_common_StreetAddress, "city")
    descriptor = None
    for klass in org_aries_common_StreetAddress.__mro__:
        if "city" in klass.__dict__:
            descriptor = klass.__dict__["city"]
            break
    assert isinstance(descriptor, property)

def test_org_aries_common_streetaddress_has_country():
    assert hasattr(org_aries_common_StreetAddress, "country")
    descriptor = None
    for klass in org_aries_common_StreetAddress.__mro__:
        if "country" in klass.__dict__:
            descriptor = klass.__dict__["country"]
            break
    assert isinstance(descriptor, property)

def test_org_aries_common_streetaddress_has_latitude():
    assert hasattr(org_aries_common_StreetAddress, "latitude")
    descriptor = None
    for klass in org_aries_common_StreetAddress.__mro__:
        if "latitude" in klass.__dict__:
            descriptor = klass.__dict__["latitude"]
            break
    assert isinstance(descriptor, property)

def test_org_aries_common_streetaddress_has_longitude():
    assert hasattr(org_aries_common_StreetAddress, "longitude")
    descriptor = None
    for klass in org_aries_common_StreetAddress.__mro__:
        if "longitude" in klass.__dict__:
            descriptor = klass.__dict__["longitude"]
            break
    assert isinstance(descriptor, property)

def test_org_aries_common_streetaddress_has_street():
    assert hasattr(org_aries_common_StreetAddress, "street")
    descriptor = None
    for klass in org_aries_common_StreetAddress.__mro__:
        if "street" in klass.__dict__:
            descriptor = klass.__dict__["street"]
            break
    assert isinstance(descriptor, property)

def test_org_aries_common_streetaddress_has_state():
    assert hasattr(org_aries_common_StreetAddress, "state")
    descriptor = None
    for klass in org_aries_common_StreetAddress.__mro__:
        if "state" in klass.__dict__:
            descriptor = klass.__dict__["state"]
            break
    assert isinstance(descriptor, property)



def test_org_aries_common_phonenumber_is_not_abstract():
    assert not inspect.isabstract(org_aries_common_PhoneNumber)


def test_org_aries_common_phonenumber_constructor_exists():
    assert callable(org_aries_common_PhoneNumber.__init__)


def test_org_aries_common_phonenumber_constructor_args():
    sig = inspect.signature(org_aries_common_PhoneNumber.__init__)
    params = list(sig.parameters.keys())
    assert "extension" in params, "Missing parameter 'extension'"
    assert "country" in params, "Missing parameter 'country'"
    assert "number" in params, "Missing parameter 'number'"
    assert "id" in params, "Missing parameter 'id'"
    assert "area" in params, "Missing parameter 'area'"
    assert "value" in params, "Missing parameter 'value'"
    assert "type" in params, "Missing parameter 'type'"

def test_org_aries_common_phonenumber_has_extension():
    assert hasattr(org_aries_common_PhoneNumber, "extension")
    descriptor = None
    for klass in org_aries_common_PhoneNumber.__mro__:
        if "extension" in klass.__dict__:
            descriptor = klass.__dict__["extension"]
            break
    assert isinstance(descriptor, property)

def test_org_aries_common_phonenumber_has_country():
    assert hasattr(org_aries_common_PhoneNumber, "country")
    descriptor = None
    for klass in org_aries_common_PhoneNumber.__mro__:
        if "country" in klass.__dict__:
            descriptor = klass.__dict__["country"]
            break
    assert isinstance(descriptor, property)

def test_org_aries_common_phonenumber_has_number():
    assert hasattr(org_aries_common_PhoneNumber, "number")
    descriptor = None
    for klass in org_aries_common_PhoneNumber.__mro__:
        if "number" in klass.__dict__:
            descriptor = klass.__dict__["number"]
            break
    assert isinstance(descriptor, property)

def test_org_aries_common_phonenumber_has_id():
    assert hasattr(org_aries_common_PhoneNumber, "id")
    descriptor = None
    for klass in org_aries_common_PhoneNumber.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_org_aries_common_phonenumber_has_area():
    assert hasattr(org_aries_common_PhoneNumber, "area")
    descriptor = None
    for klass in org_aries_common_PhoneNumber.__mro__:
        if "area" in klass.__dict__:
            descriptor = klass.__dict__["area"]
            break
    assert isinstance(descriptor, property)

def test_org_aries_common_phonenumber_has_value():
    assert hasattr(org_aries_common_PhoneNumber, "value")
    descriptor = None
    for klass in org_aries_common_PhoneNumber.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_org_aries_common_phonenumber_has_type():
    assert hasattr(org_aries_common_PhoneNumber, "type")
    descriptor = None
    for klass in org_aries_common_PhoneNumber.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_org_aries_common_property_is_not_abstract():
    assert not inspect.isabstract(org_aries_common_Property)


def test_org_aries_common_property_constructor_exists():
    assert callable(org_aries_common_Property.__init__)


def test_org_aries_common_property_constructor_args():
    sig = inspect.signature(org_aries_common_Property.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"

def test_org_aries_common_property_has_value():
    assert hasattr(org_aries_common_Property, "value")
    descriptor = None
    for klass in org_aries_common_Property.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_org_aries_common_property_has_mixed():
    assert hasattr(org_aries_common_Property, "mixed")
    descriptor = None
    for klass in org_aries_common_Property.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_org_aries_common_property_has_name():
    assert hasattr(org_aries_common_Property, "name")
    descriptor = None
    for klass in org_aries_common_Property.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_org_aries_common_property_has_id():
    assert hasattr(org_aries_common_Property, "id")
    descriptor = None
    for klass in org_aries_common_Property.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_org_aries_common_properties_is_not_abstract():
    assert not inspect.isabstract(org_aries_common_Properties)


def test_org_aries_common_properties_constructor_exists():
    assert callable(org_aries_common_Properties.__init__)


def test_org_aries_common_properties_constructor_args():
    sig = inspect.signature(org_aries_common_Properties.__init__)
    params = list(sig.parameters.keys())



def test_org_aries_common_person_is_not_abstract():
    assert not inspect.isabstract(org_aries_common_Person)


def test_org_aries_common_person_constructor_exists():
    assert callable(org_aries_common_Person.__init__)


def test_org_aries_common_person_constructor_args():
    sig = inspect.signature(org_aries_common_Person.__init__)
    params = list(sig.parameters.keys())
    assert "userId" in params, "Missing parameter 'userId'"
    assert "id" in params, "Missing parameter 'id'"

def test_org_aries_common_person_has_userId():
    assert hasattr(org_aries_common_Person, "userId")
    descriptor = None
    for klass in org_aries_common_Person.__mro__:
        if "userId" in klass.__dict__:
            descriptor = klass.__dict__["userId"]
            break
    assert isinstance(descriptor, property)

def test_org_aries_common_person_has_id():
    assert hasattr(org_aries_common_Person, "id")
    descriptor = None
    for klass in org_aries_common_Person.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_org_aries_common_personname_is_not_abstract():
    assert not inspect.isabstract(org_aries_common_PersonName)


def test_org_aries_common_personname_constructor_exists():
    assert callable(org_aries_common_PersonName.__init__)


def test_org_aries_common_personname_constructor_args():
    sig = inspect.signature(org_aries_common_PersonName.__init__)
    params = list(sig.parameters.keys())
    assert "middleInitial" in params, "Missing parameter 'middleInitial'"
    assert "lastName" in params, "Missing parameter 'lastName'"
    assert "firstName" in params, "Missing parameter 'firstName'"

def test_org_aries_common_personname_has_middleInitial():
    assert hasattr(org_aries_common_PersonName, "middleInitial")
    descriptor = None
    for klass in org_aries_common_PersonName.__mro__:
        if "middleInitial" in klass.__dict__:
            descriptor = klass.__dict__["middleInitial"]
            break
    assert isinstance(descriptor, property)

def test_org_aries_common_personname_has_lastName():
    assert hasattr(org_aries_common_PersonName, "lastName")
    descriptor = None
    for klass in org_aries_common_PersonName.__mro__:
        if "lastName" in klass.__dict__:
            descriptor = klass.__dict__["lastName"]
            break
    assert isinstance(descriptor, property)

def test_org_aries_common_personname_has_firstName():
    assert hasattr(org_aries_common_PersonName, "firstName")
    descriptor = None
    for klass in org_aries_common_PersonName.__mro__:
        if "firstName" in klass.__dict__:
            descriptor = klass.__dict__["firstName"]
            break
    assert isinstance(descriptor, property)



def test_org_aries_common_eobject_is_not_abstract():
    assert not inspect.isabstract(org_aries_common_EObject)


def test_org_aries_common_eobject_constructor_exists():
    assert callable(org_aries_common_EObject.__init__)


def test_org_aries_common_eobject_constructor_args():
    sig = inspect.signature(org_aries_common_EObject.__init__)
    params = list(sig.parameters.keys())



def test_org_aries_common_mapentry_is_not_abstract():
    assert not inspect.isabstract(org_aries_common_MapEntry)


def test_org_aries_common_mapentry_constructor_exists():
    assert callable(org_aries_common_MapEntry.__init__)


def test_org_aries_common_mapentry_constructor_args():
    sig = inspect.signature(org_aries_common_MapEntry.__init__)
    params = list(sig.parameters.keys())



def test_org_aries_common_map_is_not_abstract():
    assert not inspect.isabstract(org_aries_common_Map)


def test_org_aries_common_map_constructor_exists():
    assert callable(org_aries_common_Map.__init__)


def test_org_aries_common_map_constructor_args():
    sig = inspect.signature(org_aries_common_Map.__init__)
    params = list(sig.parameters.keys())



def test_org_aries_common_note_is_not_abstract():
    assert not inspect.isabstract(org_aries_common_Note)


def test_org_aries_common_note_constructor_exists():
    assert callable(org_aries_common_Note.__init__)


def test_org_aries_common_note_constructor_args():
    sig = inspect.signature(org_aries_common_Note.__init__)
    params = list(sig.parameters.keys())
    assert "creationDate" in params, "Missing parameter 'creationDate'"
    assert "lastUpdate" in params, "Missing parameter 'lastUpdate'"
    assert "id" in params, "Missing parameter 'id'"
    assert "text" in params, "Missing parameter 'text'"

def test_org_aries_common_note_has_creationDate():
    assert hasattr(org_aries_common_Note, "creationDate")
    descriptor = None
    for klass in org_aries_common_Note.__mro__:
        if "creationDate" in klass.__dict__:
            descriptor = klass.__dict__["creationDate"]
            break
    assert isinstance(descriptor, property)

def test_org_aries_common_note_has_lastUpdate():
    assert hasattr(org_aries_common_Note, "lastUpdate")
    descriptor = None
    for klass in org_aries_common_Note.__mro__:
        if "lastUpdate" in klass.__dict__:
            descriptor = klass.__dict__["lastUpdate"]
            break
    assert isinstance(descriptor, property)

def test_org_aries_common_note_has_id():
    assert hasattr(org_aries_common_Note, "id")
    descriptor = None
    for klass in org_aries_common_Note.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_org_aries_common_note_has_text():
    assert hasattr(org_aries_common_Note, "text")
    descriptor = None
    for klass in org_aries_common_Note.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_org_aries_common_event_is_not_abstract():
    assert not inspect.isabstract(org_aries_common_Event)


def test_org_aries_common_event_constructor_exists():
    assert callable(org_aries_common_Event.__init__)


def test_org_aries_common_event_constructor_args():
    sig = inspect.signature(org_aries_common_Event.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_org_aries_common_event_has_id():
    assert hasattr(org_aries_common_Event, "id")
    descriptor = None
    for klass in org_aries_common_Event.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_org_aries_common_emailmessage_is_not_abstract():
    assert not inspect.isabstract(org_aries_common_EmailMessage)


def test_org_aries_common_emailmessage_constructor_exists():
    assert callable(org_aries_common_EmailMessage.__init__)


def test_org_aries_common_emailmessage_constructor_args():
    sig = inspect.signature(org_aries_common_EmailMessage.__init__)
    params = list(sig.parameters.keys())
    assert "subject" in params, "Missing parameter 'subject'"
    assert "timestamp" in params, "Missing parameter 'timestamp'"
    assert "smtpPort" in params, "Missing parameter 'smtpPort'"
    assert "smtpHost" in params, "Missing parameter 'smtpHost'"
    assert "sendAsHtml" in params, "Missing parameter 'sendAsHtml'"
    assert "id" in params, "Missing parameter 'id'"
    assert "sourceId" in params, "Missing parameter 'sourceId'"
    assert "content" in params, "Missing parameter 'content'"

def test_org_aries_common_emailmessage_has_subject():
    assert hasattr(org_aries_common_EmailMessage, "subject")
    descriptor = None
    for klass in org_aries_common_EmailMessage.__mro__:
        if "subject" in klass.__dict__:
            descriptor = klass.__dict__["subject"]
            break
    assert isinstance(descriptor, property)

def test_org_aries_common_emailmessage_has_timestamp():
    assert hasattr(org_aries_common_EmailMessage, "timestamp")
    descriptor = None
    for klass in org_aries_common_EmailMessage.__mro__:
        if "timestamp" in klass.__dict__:
            descriptor = klass.__dict__["timestamp"]
            break
    assert isinstance(descriptor, property)

def test_org_aries_common_emailmessage_has_smtpPort():
    assert hasattr(org_aries_common_EmailMessage, "smtpPort")
    descriptor = None
    for klass in org_aries_common_EmailMessage.__mro__:
        if "smtpPort" in klass.__dict__:
            descriptor = klass.__dict__["smtpPort"]
            break
    assert isinstance(descriptor, property)

def test_org_aries_common_emailmessage_has_smtpHost():
    assert hasattr(org_aries_common_EmailMessage, "smtpHost")
    descriptor = None
    for klass in org_aries_common_EmailMessage.__mro__:
        if "smtpHost" in klass.__dict__:
            descriptor = klass.__dict__["smtpHost"]
            break
    assert isinstance(descriptor, property)

def test_org_aries_common_emailmessage_has_sendAsHtml():
    assert hasattr(org_aries_common_EmailMessage, "sendAsHtml")
    descriptor = None
    for klass in org_aries_common_EmailMessage.__mro__:
        if "sendAsHtml" in klass.__dict__:
            descriptor = klass.__dict__["sendAsHtml"]
            break
    assert isinstance(descriptor, property)

def test_org_aries_common_emailmessage_has_id():
    assert hasattr(org_aries_common_EmailMessage, "id")
    descriptor = None
    for klass in org_aries_common_EmailMessage.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_org_aries_common_emailmessage_has_sourceId():
    assert hasattr(org_aries_common_EmailMessage, "sourceId")
    descriptor = None
    for klass in org_aries_common_EmailMessage.__mro__:
        if "sourceId" in klass.__dict__:
            descriptor = klass.__dict__["sourceId"]
            break
    assert isinstance(descriptor, property)

def test_org_aries_common_emailmessage_has_content():
    assert hasattr(org_aries_common_EmailMessage, "content")
    descriptor = None
    for klass in org_aries_common_EmailMessage.__mro__:
        if "content" in klass.__dict__:
            descriptor = klass.__dict__["content"]
            break
    assert isinstance(descriptor, property)



def test_org_aries_common_emailbox_is_not_abstract():
    assert not inspect.isabstract(org_aries_common_EmailBox)


def test_org_aries_common_emailbox_constructor_exists():
    assert callable(org_aries_common_EmailBox.__init__)


def test_org_aries_common_emailbox_constructor_args():
    sig = inspect.signature(org_aries_common_EmailBox.__init__)
    params = list(sig.parameters.keys())
    assert "creationDate" in params, "Missing parameter 'creationDate'"
    assert "type" in params, "Missing parameter 'type'"
    assert "lastUpdate" in params, "Missing parameter 'lastUpdate'"
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"

def test_org_aries_common_emailbox_has_creationDate():
    assert hasattr(org_aries_common_EmailBox, "creationDate")
    descriptor = None
    for klass in org_aries_common_EmailBox.__mro__:
        if "creationDate" in klass.__dict__:
            descriptor = klass.__dict__["creationDate"]
            break
    assert isinstance(descriptor, property)

def test_org_aries_common_emailbox_has_type():
    assert hasattr(org_aries_common_EmailBox, "type")
    descriptor = None
    for klass in org_aries_common_EmailBox.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_org_aries_common_emailbox_has_lastUpdate():
    assert hasattr(org_aries_common_EmailBox, "lastUpdate")
    descriptor = None
    for klass in org_aries_common_EmailBox.__mro__:
        if "lastUpdate" in klass.__dict__:
            descriptor = klass.__dict__["lastUpdate"]
            break
    assert isinstance(descriptor, property)

def test_org_aries_common_emailbox_has_id():
    assert hasattr(org_aries_common_EmailBox, "id")
    descriptor = None
    for klass in org_aries_common_EmailBox.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_org_aries_common_emailbox_has_name():
    assert hasattr(org_aries_common_EmailBox, "name")
    descriptor = None
    for klass in org_aries_common_EmailBox.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_org_aries_common_emailaddresslist_is_not_abstract():
    assert not inspect.isabstract(org_aries_common_EmailAddressList)


def test_org_aries_common_emailaddresslist_constructor_exists():
    assert callable(org_aries_common_EmailAddressList.__init__)


def test_org_aries_common_emailaddresslist_constructor_args():
    sig = inspect.signature(org_aries_common_EmailAddressList.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "emailAddress" in params, "Missing parameter 'emailAddress'"

def test_org_aries_common_emailaddresslist_has_name():
    assert hasattr(org_aries_common_EmailAddressList, "name")
    descriptor = None
    for klass in org_aries_common_EmailAddressList.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_org_aries_common_emailaddresslist_has_emailAddress():
    assert hasattr(org_aries_common_EmailAddressList, "emailAddress")
    descriptor = None
    for klass in org_aries_common_EmailAddressList.__mro__:
        if "emailAddress" in klass.__dict__:
            descriptor = klass.__dict__["emailAddress"]
            break
    assert isinstance(descriptor, property)



def test_org_aries_common_emailaddress_is_not_abstract():
    assert not inspect.isabstract(org_aries_common_EmailAddress)


def test_org_aries_common_emailaddress_constructor_exists():
    assert callable(org_aries_common_EmailAddress.__init__)


def test_org_aries_common_emailaddress_constructor_args():
    sig = inspect.signature(org_aries_common_EmailAddress.__init__)
    params = list(sig.parameters.keys())
    assert "creationDate" in params, "Missing parameter 'creationDate'"
    assert "lastName" in params, "Missing parameter 'lastName'"
    assert "url" in params, "Missing parameter 'url'"
    assert "organization" in params, "Missing parameter 'organization'"
    assert "enabled" in params, "Missing parameter 'enabled'"
    assert "lastUpdate" in params, "Missing parameter 'lastUpdate'"
    assert "id" in params, "Missing parameter 'id'"
    assert "firstName" in params, "Missing parameter 'firstName'"
    assert "userId" in params, "Missing parameter 'userId'"

def test_org_aries_common_emailaddress_has_creationDate():
    assert hasattr(org_aries_common_EmailAddress, "creationDate")
    descriptor = None
    for klass in org_aries_common_EmailAddress.__mro__:
        if "creationDate" in klass.__dict__:
            descriptor = klass.__dict__["creationDate"]
            break
    assert isinstance(descriptor, property)

def test_org_aries_common_emailaddress_has_lastName():
    assert hasattr(org_aries_common_EmailAddress, "lastName")
    descriptor = None
    for klass in org_aries_common_EmailAddress.__mro__:
        if "lastName" in klass.__dict__:
            descriptor = klass.__dict__["lastName"]
            break
    assert isinstance(descriptor, property)

def test_org_aries_common_emailaddress_has_url():
    assert hasattr(org_aries_common_EmailAddress, "url")
    descriptor = None
    for klass in org_aries_common_EmailAddress.__mro__:
        if "url" in klass.__dict__:
            descriptor = klass.__dict__["url"]
            break
    assert isinstance(descriptor, property)

def test_org_aries_common_emailaddress_has_organization():
    assert hasattr(org_aries_common_EmailAddress, "organization")
    descriptor = None
    for klass in org_aries_common_EmailAddress.__mro__:
        if "organization" in klass.__dict__:
            descriptor = klass.__dict__["organization"]
            break
    assert isinstance(descriptor, property)

def test_org_aries_common_emailaddress_has_enabled():
    assert hasattr(org_aries_common_EmailAddress, "enabled")
    descriptor = None
    for klass in org_aries_common_EmailAddress.__mro__:
        if "enabled" in klass.__dict__:
            descriptor = klass.__dict__["enabled"]
            break
    assert isinstance(descriptor, property)

def test_org_aries_common_emailaddress_has_lastUpdate():
    assert hasattr(org_aries_common_EmailAddress, "lastUpdate")
    descriptor = None
    for klass in org_aries_common_EmailAddress.__mro__:
        if "lastUpdate" in klass.__dict__:
            descriptor = klass.__dict__["lastUpdate"]
            break
    assert isinstance(descriptor, property)

def test_org_aries_common_emailaddress_has_id():
    assert hasattr(org_aries_common_EmailAddress, "id")
    descriptor = None
    for klass in org_aries_common_EmailAddress.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_org_aries_common_emailaddress_has_firstName():
    assert hasattr(org_aries_common_EmailAddress, "firstName")
    descriptor = None
    for klass in org_aries_common_EmailAddress.__mro__:
        if "firstName" in klass.__dict__:
            descriptor = klass.__dict__["firstName"]
            break
    assert isinstance(descriptor, property)

def test_org_aries_common_emailaddress_has_userId():
    assert hasattr(org_aries_common_EmailAddress, "userId")
    descriptor = None
    for klass in org_aries_common_EmailAddress.__mro__:
        if "userId" in klass.__dict__:
            descriptor = klass.__dict__["userId"]
            break
    assert isinstance(descriptor, property)



def test_org_aries_common_emailaccount_is_not_abstract():
    assert not inspect.isabstract(org_aries_common_EmailAccount)


def test_org_aries_common_emailaccount_constructor_exists():
    assert callable(org_aries_common_EmailAccount.__init__)


def test_org_aries_common_emailaccount_constructor_args():
    sig = inspect.signature(org_aries_common_EmailAccount.__init__)
    params = list(sig.parameters.keys())
    assert "firstName" in params, "Missing parameter 'firstName'"
    assert "id" in params, "Missing parameter 'id'"
    assert "password" in params, "Missing parameter 'password'"
    assert "enabled" in params, "Missing parameter 'enabled'"
    assert "userId" in params, "Missing parameter 'userId'"
    assert "lastName" in params, "Missing parameter 'lastName'"

def test_org_aries_common_emailaccount_has_firstName():
    assert hasattr(org_aries_common_EmailAccount, "firstName")
    descriptor = None
    for klass in org_aries_common_EmailAccount.__mro__:
        if "firstName" in klass.__dict__:
            descriptor = klass.__dict__["firstName"]
            break
    assert isinstance(descriptor, property)

def test_org_aries_common_emailaccount_has_id():
    assert hasattr(org_aries_common_EmailAccount, "id")
    descriptor = None
    for klass in org_aries_common_EmailAccount.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_org_aries_common_emailaccount_has_password():
    assert hasattr(org_aries_common_EmailAccount, "password")
    descriptor = None
    for klass in org_aries_common_EmailAccount.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)

def test_org_aries_common_emailaccount_has_enabled():
    assert hasattr(org_aries_common_EmailAccount, "enabled")
    descriptor = None
    for klass in org_aries_common_EmailAccount.__mro__:
        if "enabled" in klass.__dict__:
            descriptor = klass.__dict__["enabled"]
            break
    assert isinstance(descriptor, property)

def test_org_aries_common_emailaccount_has_userId():
    assert hasattr(org_aries_common_EmailAccount, "userId")
    descriptor = None
    for klass in org_aries_common_EmailAccount.__mro__:
        if "userId" in klass.__dict__:
            descriptor = klass.__dict__["userId"]
            break
    assert isinstance(descriptor, property)

def test_org_aries_common_emailaccount_has_lastName():
    assert hasattr(org_aries_common_EmailAccount, "lastName")
    descriptor = None
    for klass in org_aries_common_EmailAccount.__mro__:
        if "lastName" in klass.__dict__:
            descriptor = klass.__dict__["lastName"]
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



def test_org_aries_common_estringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(org_aries_common_EStringToStringMapEntry)


def test_org_aries_common_estringtostringmapentry_constructor_exists():
    assert callable(org_aries_common_EStringToStringMapEntry.__init__)


def test_org_aries_common_estringtostringmapentry_constructor_args():
    sig = inspect.signature(org_aries_common_EStringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())



def test_org_aries_common_documentroot_is_not_abstract():
    assert not inspect.isabstract(org_aries_common_DocumentRoot)


def test_org_aries_common_documentroot_constructor_exists():
    assert callable(org_aries_common_DocumentRoot.__init__)


def test_org_aries_common_documentroot_constructor_args():
    sig = inspect.signature(org_aries_common_DocumentRoot.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_org_aries_common_documentroot_has_mixed():
    assert hasattr(org_aries_common_DocumentRoot, "mixed")
    descriptor = None
    for klass in org_aries_common_DocumentRoot.__mro__:
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



def test_org_aries_common_attachment_is_not_abstract():
    assert not inspect.isabstract(org_aries_common_Attachment)


def test_org_aries_common_attachment_constructor_exists():
    assert callable(org_aries_common_Attachment.__init__)


def test_org_aries_common_attachment_constructor_args():
    sig = inspect.signature(org_aries_common_Attachment.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "size" in params, "Missing parameter 'size'"
    assert "contentType" in params, "Missing parameter 'contentType'"
    assert "fileName" in params, "Missing parameter 'fileName'"
    assert "fileData" in params, "Missing parameter 'fileData'"
    assert "id" in params, "Missing parameter 'id'"

def test_org_aries_common_attachment_has_name():
    assert hasattr(org_aries_common_Attachment, "name")
    descriptor = None
    for klass in org_aries_common_Attachment.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_org_aries_common_attachment_has_size():
    assert hasattr(org_aries_common_Attachment, "size")
    descriptor = None
    for klass in org_aries_common_Attachment.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)

def test_org_aries_common_attachment_has_contentType():
    assert hasattr(org_aries_common_Attachment, "contentType")
    descriptor = None
    for klass in org_aries_common_Attachment.__mro__:
        if "contentType" in klass.__dict__:
            descriptor = klass.__dict__["contentType"]
            break
    assert isinstance(descriptor, property)

def test_org_aries_common_attachment_has_fileName():
    assert hasattr(org_aries_common_Attachment, "fileName")
    descriptor = None
    for klass in org_aries_common_Attachment.__mro__:
        if "fileName" in klass.__dict__:
            descriptor = klass.__dict__["fileName"]
            break
    assert isinstance(descriptor, property)

def test_org_aries_common_attachment_has_fileData():
    assert hasattr(org_aries_common_Attachment, "fileData")
    descriptor = None
    for klass in org_aries_common_Attachment.__mro__:
        if "fileData" in klass.__dict__:
            descriptor = klass.__dict__["fileData"]
            break
    assert isinstance(descriptor, property)

def test_org_aries_common_attachment_has_id():
    assert hasattr(org_aries_common_Attachment, "id")
    descriptor = None
    for klass in org_aries_common_Attachment.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_activitygroupname_exists():
    # Check that the Enumeration exists
    assert ActivityGroupName is not None

def test_activitygroupname_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ActivityGroupName]
    expected_literals = [
        "BookstoreToban",
        "none",
        "Gajokai",
        "WelcomingCommittee",
        "SokaGroup",
        "Secretariet",
        "CleanupCommittee",
        "BuildingCommittee",
        "YouthSupportGroup",
        "FifeAndDrumCorp",
        "CultureDept",
        "SokaSpiritGroup",
        "StudyGroup",
        "YouthMusicCorp",
        "YouthPeaceGroup",
        "Byakuren",
        "PhoneToban",
        "ChorusGroup",
        "GoldenStageCrew",
        "CentralExecutiveCommittee",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ActivityGroupName"

def test_phonenumbertype_exists():
    # Check that the Enumeration exists
    assert PhoneNumberType is not None

def test_phonenumbertype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PhoneNumberType]
    expected_literals = [
        "WORK",
        "HOME",
        "OTHER",
        "FAX",
        "CELL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PhoneNumberType"

def test_divisionname_exists():
    # Check that the Enumeration exists
    assert DivisionName is not None

def test_divisionname_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DivisionName]
    expected_literals = [
        "WomanSDivision",
        "AllDivisions",
        "none",
        "YoungMenSDivision",
        "YoungWomenSDivision",
        "MenSDivision",
        "YouthDivision",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DivisionName"

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

def test_role_exists():
    # Check that the Enumeration exists
    assert Role is not None

def test_role_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Role]
    expected_literals = [
        "HOST",
        "MANAGER",
        "USER",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Role"

def test_subdivision_exists():
    # Check that the Enumeration exists
    assert SubDivision is not None

def test_subdivision_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SubDivision]
    expected_literals = [
        "HIGHSCHOOL",
        "ELEMENTARYSCHOOL",
        "ALL",
        "CHILDREN",
        "JRHIGHSCHOOL",
        "STUDENT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SubDivision"

def test_familyrelation_exists():
    # Check that the Enumeration exists
    assert FamilyRelation is not None

def test_familyrelation_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FamilyRelation]
    expected_literals = [
        "NEPHEW",
        "HUSBAND",
        "GRANDSON",
        "GRANDFATHER",
        "GRANDMOTHER",
        "EXHUSBAND",
        "FATHER",
        "GRANDDAUGHTER",
        "STEPSISTER",
        "UNCLE",
        "NIECE",
        "AUNT",
        "DAUGHTER",
        "BROTHER",
        "SONINLAW",
        "STEPBROTHER",
        "OTHER",
        "EXWIFE",
        "DAUGHTERINLAW",
        "WIFE",
        "COUSIN",
        "SISTER",
        "SON",
        "FATHERINLAW",
        "MOTHERINLAW",
        "MOTHER",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FamilyRelation"

def test_capability_exists():
    # Check that the Enumeration exists
    assert Capability is not None

def test_capability_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Capability]
    expected_literals = [
        "NONE",
        "PRINT",
        "ALL",
        "UPDATE",
        "READ",
        "DELETE",
        "EXPORT",
        "CREATE",
        "EMAIL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Capability"

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

def test_eventstatus_exists():
    # Check that the Enumeration exists
    assert EventStatus is not None

def test_eventstatus_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EventStatus]
    expected_literals = [
        "HOST",
        "USER",
        "MANAGER",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EventStatus"

def test_organizationlevel_exists():
    # Check that the Enumeration exists
    assert OrganizationLevel is not None

def test_organizationlevel_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in OrganizationLevel]
    expected_literals = [
        "AREA",
        "UNIT",
        "DISTRICT",
        "SGIUSA",
        "CHAPTER",
        "REGION",
        "ZONE",
        "GROUP",
        "TEAM",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in OrganizationLevel"

def test_country_exists():
    # Check that the Enumeration exists
    assert Country is not None

def test_country_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Country]
    expected_literals = [
        "PR",
        "CAN",
        "USA",
        "MEX",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Country"

def test_division_exists():
    # Check that the Enumeration exists
    assert Division is not None

def test_division_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Division]
    expected_literals = [
        "WD",
        "YMD",
        "NONE",
        "YD",
        "ALL",
        "YWD",
        "MD",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Division"

def test_studydeptlanguage_exists():
    # Check that the Enumeration exists
    assert StudyDeptLanguage is not None

def test_studydeptlanguage_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in StudyDeptLanguage]
    expected_literals = [
        "OTHER",
        "THAI",
        "CHINESE",
        "PORTUGUESE",
        "ENGLISH",
        "KOREAN",
        "ITALIAN",
        "VIETNAMESE",
        "FRENCH",
        "GERMAN",
        "SPANISH",
        "JAPANESE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in StudyDeptLanguage"

def test_gohonzontype_exists():
    # Check that the Enumeration exists
    assert GohonzonType is not None

def test_gohonzontype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in GohonzonType]
    expected_literals = [
        "LARGE",
        "REGULAR",
        "FAMILY",
        "OKATAGI",
        "OMOMORI",
        "SMALL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in GohonzonType"

def test_positionname_exists():
    # Check that the Enumeration exists
    assert PositionName is not None

def test_positionname_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PositionName]
    expected_literals = [
        "SeniorViceLeader",
        "Leader",
        "GeneralDirector",
        "SokaSpiritCoordinator",
        "MembershipStatisticsAdministrator",
        "CultureDeptCoordinator",
        "ViceLeader",
        "MembershipDatabaseAdministrator",
        "Advisor",
        "Guidance",
        "MemberCareAdvisor",
        "PublicationsRepresentative",
        "ViceGeneralDirector",
        "SeniorViceGeneralDirector",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PositionName"

def test_activitygroup_exists():
    # Check that the Enumeration exists
    assert ActivityGroup is not None

def test_activitygroup_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ActivityGroup]
    expected_literals = [
        "BYAKUREN",
        "FIFEANDDRUMCORP",
        "GAJOKAI",
        "CHORUSGROUP",
        "GOLDENSTAGECREW",
        "STUDYGROUP",
        "YOUTHPEACEGROUP",
        "CLEANUPCOMMITTEE",
        "CULTUREDEPT",
        "YOUTHMUSICCORP",
        "SOKASPIRITGROUP",
        "YOUTHSUPPORTGROUP",
        "BUILDINGCOMMITTEE",
        "SOKAGROUP",
        "CENTRALEXECUTIVECOMMITTEE",
        "WELCOMINGCOMMITTEE",
        "NONE",
        "PHONETOBAN",
        "SECRETARIET",
        "BOOKSTORETOBAN",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ActivityGroup"

def test_subdivisionname_exists():
    # Check that the Enumeration exists
    assert SubDivisionName is not None

def test_subdivisionname_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SubDivisionName]
    expected_literals = [
        "JrHighSchoolDivision",
        "ElementarySchoolDivision",
        "HighSchoolDivision",
        "StudentDivision",
        "ALLSubDivisions",
        "ChildrenSDivision",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SubDivisionName"

def test_position_exists():
    # Check that the Enumeration exists
    assert Position is not None

def test_position_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Position]
    expected_literals = [
        "MEMBERCAREADVISOR",
        "GENERALDIRECTOR",
        "GUIDANCE",
        "VICEGENERALDIRECTOR",
        "CULTUREDEPTCOORDINATOR",
        "MEMBERSHIPSTATISTICSADMINISTRATOR",
        "MEMBERSHIPDATABASEADMINISTRATOR",
        "PUBLICATIONSREPRESENTATIVE",
        "SENIORVICEGENERALDIRECTOR",
        "ADVISOR",
        "SOKASPIRITCOORDINATOR",
        "VICELEADER",
        "SENIORVICELEADER",
        "LEADER",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Position"

def test_studydeptexamlevel_exists():
    # Check that the Enumeration exists
    assert StudyDeptExamLevel is not None

def test_studydeptexamlevel_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in StudyDeptExamLevel]
    expected_literals = [
        "ADVANCED",
        "INTERMEDIATE",
        "ELEMENTARY",
        "GRADUATE",
        "OTHER",
        "ENTRANCE",
        "POSTGRADUATE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in StudyDeptExamLevel"

def test_state_exists():
    # Check that the Enumeration exists
    assert State is not None

def test_state_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in State]
    expected_literals = [
        "CT",
        "LA",
        "ME",
        "OR",
        "FL",
        "WA",
        "NE",
        "KY",
        "KS",
        "OH",
        "AK",
        "WV",
        "PA",
        "NY",
        "VA",
        "MT",
        "RI",
        "IA",
        "ND",
        "AL",
        "NJ",
        "AZ",
        "GA",
        "MN",
        "AR",
        "NC",
        "TX",
        "CO",
        "MO",
        "MA",
        "IN",
        "SD",
        "SC",
        "VT",
        "WY",
        "ID",
        "UT",
        "TN",
        "MS",
        "CA",
        "MD",
        "NV",
        "HI",
        "DE",
        "IL",
        "MI",
        "NM",
        "WI",
        "OK",
        "NH",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in State"

def test_schooltype_exists():
    # Check that the Enumeration exists
    assert SchoolType is not None

def test_schooltype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SchoolType]
    expected_literals = [
        "GRAMMER",
        "COLLEGE",
        "OTHER",
        "HIGHSCHOOL",
        "JRHIGHSCHOOL",
        "ELEMENTARY",
        "GRADUATE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SchoolType"

def test_language_exists():
    # Check that the Enumeration exists
    assert Language is not None

def test_language_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Language]
    expected_literals = [
        "SPANISH",
        "GERMAN",
        "JAPANESE",
        "CHINESE",
        "KOREAN",
        "OTHER",
        "ITALIAN",
        "FRENCH",
        "VIETNAMESE",
        "THAI",
        "PORTUGUESE",
        "ENGLISH",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Language"

def test_status_exists():
    # Check that the Enumeration exists
    assert Status is not None

def test_status_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Status]
    expected_literals = [
        "WARNING",
        "INFO",
        "PROMPT",
        "ERROR",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Status"


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
org_sgiusa_model_View_strategy = st.builds(
    org_sgiusa_model_View,
    viewType=
        safe_text,
    id=
        safe_text,
    userId=
        safe_text
)
org_sgiusa_model_Users_strategy = st.builds(
    org_sgiusa_model_Users,
)
org_sgiusa_model_StudyDeptInfo_strategy = st.builds(
    org_sgiusa_model_StudyDeptInfo,
    id=
        safe_text,
    lastUpdate=
        safe_text
)
org_sgiusa_model_User_strategy = st.builds(
    org_sgiusa_model_User,
    lastName=
        safe_text,
    password=
        safe_text,
    id=
        safe_text,
    role=
        safe_text,
    userId=
        safe_text,
    firstName=
        safe_text,
    enabled=
        safe_text
)
org_sgiusa_model_StudyDeptExam_strategy = st.builds(
    org_sgiusa_model_StudyDeptExam,
    examLocation=
        safe_text,
    lastUpdate=
        safe_text,
    id=
        safe_text,
    current=
        safe_text,
    examLevel=
        safe_text,
    examDate=
        safe_text,
    examLanguage=
        safe_text
)
org_sgiusa_model_Registration_strategy = st.builds(
    org_sgiusa_model_Registration,
    aborted=
        safe_text,
    cancelled=
        safe_text,
    id=
        safe_text,
    date=
        safe_text
)
org_sgiusa_model_SchoolInfo_strategy = st.builds(
    org_sgiusa_model_SchoolInfo,
    startDate=
        safe_text,
    schoolName=
        safe_text,
    fieldOfStudy=
        safe_text,
    id=
        safe_text,
    endDate=
        safe_text,
    schoolType=
        safe_text,
    lastUpdate=
        safe_text
)
org_sgiusa_model_Preferences_strategy = st.builds(
    org_sgiusa_model_Preferences,
    id=
        safe_text,
    themeId=
        safe_text,
    selectedNode=
        safe_text,
    userId=
        safe_text,
    enableTooltips=
        safe_text,
    selectedView=
        safe_text,
    openViews=
        safe_text,
    openNodes=
        safe_text
)
org_sgiusa_model_Permission_strategy = st.builds(
    org_sgiusa_model_Permission,
    divisions=
        safe_text,
    activityGroups=
        safe_text,
    userId=
        safe_text,
    subDivisions=
        safe_text,
    capabilities=
        safe_text,
    enabled=
        safe_text,
    id=
        safe_text
)
org_sgiusa_model_Organization_strategy = st.builds(
    org_sgiusa_model_Organization,
    id=
        safe_text,
    creationDate=
        safe_text,
    zipCodes=
        safe_text,
    organizationId=
        safe_text,
    permissionId=
        safe_text,
    level=
        safe_text,
    abbrv=
        safe_text,
    label=
        safe_text,
    type=
        safe_text,
    name=
        safe_text,
    lastUpdate=
        safe_text
)
org_sgiusa_model_MembershipInfo_strategy = st.builds(
    org_sgiusa_model_MembershipInfo,
    id=
        safe_text,
    friendOfSgi=
        safe_text,
    lastUpdate=
        safe_text,
    notLocatable=
        safe_text,
    notActivated=
        safe_text,
    receivedCertificate=
        safe_text
)
org_sgiusa_model_Note_strategy = st.builds(
    org_sgiusa_model_Note,
    id=
        safe_text,
    text=
        safe_text,
    creationDate=
        safe_text,
    lastUpdate=
        safe_text
)
org_sgiusa_model_Members_strategy = st.builds(
    org_sgiusa_model_Members,
)
org_sgiusa_model_MemberSearchCriteria_strategy = st.builds(
    org_sgiusa_model_MemberSearchCriteria,
    divisions=
        safe_text,
    subDivisions=
        safe_text,
    activityGroups=
        safe_text
)
org_sgiusa_model_Member_strategy = st.builds(
    org_sgiusa_model_Member,
    archived=
        safe_text,
    division=
        safe_text,
    extraField2=
        safe_text,
    interests=
        safe_text,
    employer=
        safe_text,
    activityGroups=
        safe_text,
    lastName=
        safe_text,
    firstName=
        safe_text,
    middleInitial=
        safe_text,
    statusProfile=
        safe_text,
    languages=
        safe_text,
    locatable=
        safe_text,
    birthDate=
        safe_text,
    subDivision=
        safe_text,
    visible=
        safe_text,
    joinDate=
        safe_text,
    extraField1=
        safe_text,
    id=
        safe_text,
    occupation=
        safe_text
)
org_sgiusa_model_LeadershipInfo_strategy = st.builds(
    org_sgiusa_model_LeadershipInfo,
    manualSigned=
        safe_text,
    examPassed=
        safe_text,
    manualSignedDate=
        safe_text,
    id=
        safe_text,
    examPassedDate=
        safe_text,
    lastUpdate=
        safe_text
)
org_sgiusa_model_LeadershipRole_strategy = st.builds(
    org_sgiusa_model_LeadershipRole,
    activityGroup=
        safe_text,
    position=
        safe_text,
    endDate=
        safe_text,
    active=
        safe_text,
    division=
        safe_text,
    subDivision=
        safe_text,
    startDate=
        safe_text,
    id=
        safe_text,
    level=
        safe_text,
    lastUpdate=
        safe_text
)
org_sgiusa_model_GohonzonInfo_strategy = st.builds(
    org_sgiusa_model_GohonzonInfo,
    returned=
        safe_text,
    gohonzonType=
        safe_text,
    receiveDate=
        safe_text,
    returnDate=
        safe_text,
    id=
        safe_text,
    lastUpdate=
        safe_text
)
org_sgiusa_model_FamilyMember_strategy = st.builds(
    org_sgiusa_model_FamilyMember,
    familyRelation=
        safe_text,
    sgiMember=
        safe_text,
    id=
        safe_text,
    personName=
        safe_text,
    lastUpdate=
        safe_text
)
org_sgiusa_model_Event_strategy = st.builds(
    org_sgiusa_model_Event,
    status=
        safe_text,
    userId=
        safe_text,
    id=
        safe_text,
    divisions=
        safe_text,
    subDivisions=
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
org_sgiusa_model_EmailList_strategy = st.builds(
    org_sgiusa_model_EmailList,
    subDivisions=
        safe_text,
    divisions=
        safe_text,
    id=
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
MembershipInfo_strategy = st.builds(
    MembershipInfo,
)
org_sgiusa_model_EStringToStringMapEntry_strategy = st.builds(
    org_sgiusa_model_EStringToStringMapEntry,
)
org_sgiusa_model_DocumentRoot_strategy = st.builds(
    org_sgiusa_model_DocumentRoot,
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
org_aries_common_User_strategy = st.builds(
    org_aries_common_User,
    firstName=
        safe_text,
    userId=
        safe_text,
    enabled=
        safe_text,
    id=
        safe_text,
    lastName=
        safe_text,
    password=
        safe_text
)
org_aries_common_ZipCode_strategy = st.builds(
    org_aries_common_ZipCode,
    country=
        safe_text,
    extension=
        safe_text,
    number=
        safe_text
)
org_aries_common_StreetAddress_strategy = st.builds(
    org_aries_common_StreetAddress,
    id=
        safe_text,
    city=
        safe_text,
    country=
        safe_text,
    latitude=
        safe_text,
    longitude=
        safe_text,
    street=
        safe_text,
    state=
        safe_text
)
org_aries_common_PhoneNumber_strategy = st.builds(
    org_aries_common_PhoneNumber,
    extension=
        safe_text,
    country=
        safe_text,
    number=
        safe_text,
    id=
        safe_text,
    area=
        safe_text,
    value=
        safe_text,
    type=
        safe_text
)
org_aries_common_Property_strategy = st.builds(
    org_aries_common_Property,
    value=
        safe_text,
    mixed=
        safe_text,
    name=
        safe_text,
    id=
        safe_text
)
org_aries_common_Properties_strategy = st.builds(
    org_aries_common_Properties,
)
org_aries_common_Person_strategy = st.builds(
    org_aries_common_Person,
    userId=
        safe_text,
    id=
        safe_text
)
org_aries_common_PersonName_strategy = st.builds(
    org_aries_common_PersonName,
    middleInitial=
        safe_text,
    lastName=
        safe_text,
    firstName=
        safe_text
)
org_aries_common_EObject_strategy = st.builds(
    org_aries_common_EObject,
)
org_aries_common_MapEntry_strategy = st.builds(
    org_aries_common_MapEntry,
)
org_aries_common_Map_strategy = st.builds(
    org_aries_common_Map,
)
org_aries_common_Note_strategy = st.builds(
    org_aries_common_Note,
    creationDate=
        safe_text,
    lastUpdate=
        safe_text,
    id=
        safe_text,
    text=
        safe_text
)
org_aries_common_Event_strategy = st.builds(
    org_aries_common_Event,
    id=
        safe_text
)
org_aries_common_EmailMessage_strategy = st.builds(
    org_aries_common_EmailMessage,
    subject=
        safe_text,
    timestamp=
        safe_text,
    smtpPort=
        safe_text,
    smtpHost=
        safe_text,
    sendAsHtml=
        safe_text,
    id=
        safe_text,
    sourceId=
        safe_text,
    content=
        safe_text
)
org_aries_common_EmailBox_strategy = st.builds(
    org_aries_common_EmailBox,
    creationDate=
        safe_text,
    type=
        safe_text,
    lastUpdate=
        safe_text,
    id=
        safe_text,
    name=
        safe_text
)
org_aries_common_EmailAddressList_strategy = st.builds(
    org_aries_common_EmailAddressList,
    name=
        safe_text,
    emailAddress=
        safe_text
)
org_aries_common_EmailAddress_strategy = st.builds(
    org_aries_common_EmailAddress,
    creationDate=
        safe_text,
    lastName=
        safe_text,
    url=
        safe_text,
    organization=
        safe_text,
    enabled=
        safe_text,
    lastUpdate=
        safe_text,
    id=
        safe_text,
    firstName=
        safe_text,
    userId=
        safe_text
)
org_aries_common_EmailAccount_strategy = st.builds(
    org_aries_common_EmailAccount,
    firstName=
        safe_text,
    id=
        safe_text,
    password=
        safe_text,
    enabled=
        safe_text,
    userId=
        safe_text,
    lastName=
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
org_aries_common_EStringToStringMapEntry_strategy = st.builds(
    org_aries_common_EStringToStringMapEntry,
)
org_aries_common_DocumentRoot_strategy = st.builds(
    org_aries_common_DocumentRoot,
    mixed=
        safe_text
)
EmailAccount_strategy = st.builds(
    EmailAccount,
)
Attachment_strategy = st.builds(
    Attachment,
)
org_aries_common_Attachment_strategy = st.builds(
    org_aries_common_Attachment,
    name=
        safe_text,
    size=
        safe_text,
    contentType=
        safe_text,
    fileName=
        safe_text,
    fileData=
        safe_text,
    id=
        safe_text
)

@given(instance=org_sgiusa_model_View_strategy)
@settings(max_examples=50)
def test_org_sgiusa_model_view_instantiation(instance):
    assert isinstance(instance, org_sgiusa_model_View)



@given(instance=org_sgiusa_model_View_strategy)
def test_org_sgiusa_model_view_viewType_setter(instance):
    original = instance.viewType
    instance.viewType = original
    assert instance.viewType == original



@given(instance=org_sgiusa_model_View_strategy)
def test_org_sgiusa_model_view_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=org_sgiusa_model_View_strategy)
def test_org_sgiusa_model_view_userId_setter(instance):
    original = instance.userId
    instance.userId = original
    assert instance.userId == original

@given(instance=org_sgiusa_model_Users_strategy)
@settings(max_examples=50)
def test_org_sgiusa_model_users_instantiation(instance):
    assert isinstance(instance, org_sgiusa_model_Users)

@given(instance=org_sgiusa_model_StudyDeptInfo_strategy)
@settings(max_examples=50)
def test_org_sgiusa_model_studydeptinfo_instantiation(instance):
    assert isinstance(instance, org_sgiusa_model_StudyDeptInfo)



@given(instance=org_sgiusa_model_StudyDeptInfo_strategy)
def test_org_sgiusa_model_studydeptinfo_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=org_sgiusa_model_StudyDeptInfo_strategy)
def test_org_sgiusa_model_studydeptinfo_lastUpdate_setter(instance):
    original = instance.lastUpdate
    instance.lastUpdate = original
    assert instance.lastUpdate == original

@given(instance=org_sgiusa_model_User_strategy)
@settings(max_examples=50)
def test_org_sgiusa_model_user_instantiation(instance):
    assert isinstance(instance, org_sgiusa_model_User)



@given(instance=org_sgiusa_model_User_strategy)
def test_org_sgiusa_model_user_lastName_setter(instance):
    original = instance.lastName
    instance.lastName = original
    assert instance.lastName == original



@given(instance=org_sgiusa_model_User_strategy)
def test_org_sgiusa_model_user_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=org_sgiusa_model_User_strategy)
def test_org_sgiusa_model_user_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=org_sgiusa_model_User_strategy)
def test_org_sgiusa_model_user_role_setter(instance):
    original = instance.role
    instance.role = original
    assert instance.role == original



@given(instance=org_sgiusa_model_User_strategy)
def test_org_sgiusa_model_user_userId_setter(instance):
    original = instance.userId
    instance.userId = original
    assert instance.userId == original



@given(instance=org_sgiusa_model_User_strategy)
def test_org_sgiusa_model_user_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original



@given(instance=org_sgiusa_model_User_strategy)
def test_org_sgiusa_model_user_enabled_setter(instance):
    original = instance.enabled
    instance.enabled = original
    assert instance.enabled == original

@given(instance=org_sgiusa_model_StudyDeptExam_strategy)
@settings(max_examples=50)
def test_org_sgiusa_model_studydeptexam_instantiation(instance):
    assert isinstance(instance, org_sgiusa_model_StudyDeptExam)



@given(instance=org_sgiusa_model_StudyDeptExam_strategy)
def test_org_sgiusa_model_studydeptexam_examLocation_setter(instance):
    original = instance.examLocation
    instance.examLocation = original
    assert instance.examLocation == original



@given(instance=org_sgiusa_model_StudyDeptExam_strategy)
def test_org_sgiusa_model_studydeptexam_lastUpdate_setter(instance):
    original = instance.lastUpdate
    instance.lastUpdate = original
    assert instance.lastUpdate == original



@given(instance=org_sgiusa_model_StudyDeptExam_strategy)
def test_org_sgiusa_model_studydeptexam_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=org_sgiusa_model_StudyDeptExam_strategy)
def test_org_sgiusa_model_studydeptexam_current_setter(instance):
    original = instance.current
    instance.current = original
    assert instance.current == original



@given(instance=org_sgiusa_model_StudyDeptExam_strategy)
def test_org_sgiusa_model_studydeptexam_examLevel_setter(instance):
    original = instance.examLevel
    instance.examLevel = original
    assert instance.examLevel == original



@given(instance=org_sgiusa_model_StudyDeptExam_strategy)
def test_org_sgiusa_model_studydeptexam_examDate_setter(instance):
    original = instance.examDate
    instance.examDate = original
    assert instance.examDate == original



@given(instance=org_sgiusa_model_StudyDeptExam_strategy)
def test_org_sgiusa_model_studydeptexam_examLanguage_setter(instance):
    original = instance.examLanguage
    instance.examLanguage = original
    assert instance.examLanguage == original

@given(instance=org_sgiusa_model_Registration_strategy)
@settings(max_examples=50)
def test_org_sgiusa_model_registration_instantiation(instance):
    assert isinstance(instance, org_sgiusa_model_Registration)



@given(instance=org_sgiusa_model_Registration_strategy)
def test_org_sgiusa_model_registration_aborted_setter(instance):
    original = instance.aborted
    instance.aborted = original
    assert instance.aborted == original



@given(instance=org_sgiusa_model_Registration_strategy)
def test_org_sgiusa_model_registration_cancelled_setter(instance):
    original = instance.cancelled
    instance.cancelled = original
    assert instance.cancelled == original



@given(instance=org_sgiusa_model_Registration_strategy)
def test_org_sgiusa_model_registration_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=org_sgiusa_model_Registration_strategy)
def test_org_sgiusa_model_registration_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original

@given(instance=org_sgiusa_model_SchoolInfo_strategy)
@settings(max_examples=50)
def test_org_sgiusa_model_schoolinfo_instantiation(instance):
    assert isinstance(instance, org_sgiusa_model_SchoolInfo)



@given(instance=org_sgiusa_model_SchoolInfo_strategy)
def test_org_sgiusa_model_schoolinfo_startDate_setter(instance):
    original = instance.startDate
    instance.startDate = original
    assert instance.startDate == original



@given(instance=org_sgiusa_model_SchoolInfo_strategy)
def test_org_sgiusa_model_schoolinfo_schoolName_setter(instance):
    original = instance.schoolName
    instance.schoolName = original
    assert instance.schoolName == original



@given(instance=org_sgiusa_model_SchoolInfo_strategy)
def test_org_sgiusa_model_schoolinfo_fieldOfStudy_setter(instance):
    original = instance.fieldOfStudy
    instance.fieldOfStudy = original
    assert instance.fieldOfStudy == original



@given(instance=org_sgiusa_model_SchoolInfo_strategy)
def test_org_sgiusa_model_schoolinfo_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=org_sgiusa_model_SchoolInfo_strategy)
def test_org_sgiusa_model_schoolinfo_endDate_setter(instance):
    original = instance.endDate
    instance.endDate = original
    assert instance.endDate == original



@given(instance=org_sgiusa_model_SchoolInfo_strategy)
def test_org_sgiusa_model_schoolinfo_schoolType_setter(instance):
    original = instance.schoolType
    instance.schoolType = original
    assert instance.schoolType == original



@given(instance=org_sgiusa_model_SchoolInfo_strategy)
def test_org_sgiusa_model_schoolinfo_lastUpdate_setter(instance):
    original = instance.lastUpdate
    instance.lastUpdate = original
    assert instance.lastUpdate == original

@given(instance=org_sgiusa_model_Preferences_strategy)
@settings(max_examples=50)
def test_org_sgiusa_model_preferences_instantiation(instance):
    assert isinstance(instance, org_sgiusa_model_Preferences)



@given(instance=org_sgiusa_model_Preferences_strategy)
def test_org_sgiusa_model_preferences_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=org_sgiusa_model_Preferences_strategy)
def test_org_sgiusa_model_preferences_themeId_setter(instance):
    original = instance.themeId
    instance.themeId = original
    assert instance.themeId == original



@given(instance=org_sgiusa_model_Preferences_strategy)
def test_org_sgiusa_model_preferences_selectedNode_setter(instance):
    original = instance.selectedNode
    instance.selectedNode = original
    assert instance.selectedNode == original



@given(instance=org_sgiusa_model_Preferences_strategy)
def test_org_sgiusa_model_preferences_userId_setter(instance):
    original = instance.userId
    instance.userId = original
    assert instance.userId == original



@given(instance=org_sgiusa_model_Preferences_strategy)
def test_org_sgiusa_model_preferences_enableTooltips_setter(instance):
    original = instance.enableTooltips
    instance.enableTooltips = original
    assert instance.enableTooltips == original



@given(instance=org_sgiusa_model_Preferences_strategy)
def test_org_sgiusa_model_preferences_selectedView_setter(instance):
    original = instance.selectedView
    instance.selectedView = original
    assert instance.selectedView == original



@given(instance=org_sgiusa_model_Preferences_strategy)
def test_org_sgiusa_model_preferences_openViews_setter(instance):
    original = instance.openViews
    instance.openViews = original
    assert instance.openViews == original



@given(instance=org_sgiusa_model_Preferences_strategy)
def test_org_sgiusa_model_preferences_openNodes_setter(instance):
    original = instance.openNodes
    instance.openNodes = original
    assert instance.openNodes == original

@given(instance=org_sgiusa_model_Permission_strategy)
@settings(max_examples=50)
def test_org_sgiusa_model_permission_instantiation(instance):
    assert isinstance(instance, org_sgiusa_model_Permission)



@given(instance=org_sgiusa_model_Permission_strategy)
def test_org_sgiusa_model_permission_divisions_setter(instance):
    original = instance.divisions
    instance.divisions = original
    assert instance.divisions == original



@given(instance=org_sgiusa_model_Permission_strategy)
def test_org_sgiusa_model_permission_activityGroups_setter(instance):
    original = instance.activityGroups
    instance.activityGroups = original
    assert instance.activityGroups == original



@given(instance=org_sgiusa_model_Permission_strategy)
def test_org_sgiusa_model_permission_userId_setter(instance):
    original = instance.userId
    instance.userId = original
    assert instance.userId == original



@given(instance=org_sgiusa_model_Permission_strategy)
def test_org_sgiusa_model_permission_subDivisions_setter(instance):
    original = instance.subDivisions
    instance.subDivisions = original
    assert instance.subDivisions == original



@given(instance=org_sgiusa_model_Permission_strategy)
def test_org_sgiusa_model_permission_capabilities_setter(instance):
    original = instance.capabilities
    instance.capabilities = original
    assert instance.capabilities == original



@given(instance=org_sgiusa_model_Permission_strategy)
def test_org_sgiusa_model_permission_enabled_setter(instance):
    original = instance.enabled
    instance.enabled = original
    assert instance.enabled == original



@given(instance=org_sgiusa_model_Permission_strategy)
def test_org_sgiusa_model_permission_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=org_sgiusa_model_Organization_strategy)
@settings(max_examples=50)
def test_org_sgiusa_model_organization_instantiation(instance):
    assert isinstance(instance, org_sgiusa_model_Organization)



@given(instance=org_sgiusa_model_Organization_strategy)
def test_org_sgiusa_model_organization_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=org_sgiusa_model_Organization_strategy)
def test_org_sgiusa_model_organization_creationDate_setter(instance):
    original = instance.creationDate
    instance.creationDate = original
    assert instance.creationDate == original



@given(instance=org_sgiusa_model_Organization_strategy)
def test_org_sgiusa_model_organization_zipCodes_setter(instance):
    original = instance.zipCodes
    instance.zipCodes = original
    assert instance.zipCodes == original



@given(instance=org_sgiusa_model_Organization_strategy)
def test_org_sgiusa_model_organization_organizationId_setter(instance):
    original = instance.organizationId
    instance.organizationId = original
    assert instance.organizationId == original



@given(instance=org_sgiusa_model_Organization_strategy)
def test_org_sgiusa_model_organization_permissionId_setter(instance):
    original = instance.permissionId
    instance.permissionId = original
    assert instance.permissionId == original



@given(instance=org_sgiusa_model_Organization_strategy)
def test_org_sgiusa_model_organization_level_setter(instance):
    original = instance.level
    instance.level = original
    assert instance.level == original



@given(instance=org_sgiusa_model_Organization_strategy)
def test_org_sgiusa_model_organization_abbrv_setter(instance):
    original = instance.abbrv
    instance.abbrv = original
    assert instance.abbrv == original



@given(instance=org_sgiusa_model_Organization_strategy)
def test_org_sgiusa_model_organization_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original



@given(instance=org_sgiusa_model_Organization_strategy)
def test_org_sgiusa_model_organization_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=org_sgiusa_model_Organization_strategy)
def test_org_sgiusa_model_organization_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=org_sgiusa_model_Organization_strategy)
def test_org_sgiusa_model_organization_lastUpdate_setter(instance):
    original = instance.lastUpdate
    instance.lastUpdate = original
    assert instance.lastUpdate == original

@given(instance=org_sgiusa_model_MembershipInfo_strategy)
@settings(max_examples=50)
def test_org_sgiusa_model_membershipinfo_instantiation(instance):
    assert isinstance(instance, org_sgiusa_model_MembershipInfo)



@given(instance=org_sgiusa_model_MembershipInfo_strategy)
def test_org_sgiusa_model_membershipinfo_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=org_sgiusa_model_MembershipInfo_strategy)
def test_org_sgiusa_model_membershipinfo_friendOfSgi_setter(instance):
    original = instance.friendOfSgi
    instance.friendOfSgi = original
    assert instance.friendOfSgi == original



@given(instance=org_sgiusa_model_MembershipInfo_strategy)
def test_org_sgiusa_model_membershipinfo_lastUpdate_setter(instance):
    original = instance.lastUpdate
    instance.lastUpdate = original
    assert instance.lastUpdate == original



@given(instance=org_sgiusa_model_MembershipInfo_strategy)
def test_org_sgiusa_model_membershipinfo_notLocatable_setter(instance):
    original = instance.notLocatable
    instance.notLocatable = original
    assert instance.notLocatable == original



@given(instance=org_sgiusa_model_MembershipInfo_strategy)
def test_org_sgiusa_model_membershipinfo_notActivated_setter(instance):
    original = instance.notActivated
    instance.notActivated = original
    assert instance.notActivated == original



@given(instance=org_sgiusa_model_MembershipInfo_strategy)
def test_org_sgiusa_model_membershipinfo_receivedCertificate_setter(instance):
    original = instance.receivedCertificate
    instance.receivedCertificate = original
    assert instance.receivedCertificate == original

@given(instance=org_sgiusa_model_Note_strategy)
@settings(max_examples=50)
def test_org_sgiusa_model_note_instantiation(instance):
    assert isinstance(instance, org_sgiusa_model_Note)



@given(instance=org_sgiusa_model_Note_strategy)
def test_org_sgiusa_model_note_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=org_sgiusa_model_Note_strategy)
def test_org_sgiusa_model_note_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original



@given(instance=org_sgiusa_model_Note_strategy)
def test_org_sgiusa_model_note_creationDate_setter(instance):
    original = instance.creationDate
    instance.creationDate = original
    assert instance.creationDate == original



@given(instance=org_sgiusa_model_Note_strategy)
def test_org_sgiusa_model_note_lastUpdate_setter(instance):
    original = instance.lastUpdate
    instance.lastUpdate = original
    assert instance.lastUpdate == original

@given(instance=org_sgiusa_model_Members_strategy)
@settings(max_examples=50)
def test_org_sgiusa_model_members_instantiation(instance):
    assert isinstance(instance, org_sgiusa_model_Members)

@given(instance=org_sgiusa_model_MemberSearchCriteria_strategy)
@settings(max_examples=50)
def test_org_sgiusa_model_membersearchcriteria_instantiation(instance):
    assert isinstance(instance, org_sgiusa_model_MemberSearchCriteria)



@given(instance=org_sgiusa_model_MemberSearchCriteria_strategy)
def test_org_sgiusa_model_membersearchcriteria_divisions_setter(instance):
    original = instance.divisions
    instance.divisions = original
    assert instance.divisions == original



@given(instance=org_sgiusa_model_MemberSearchCriteria_strategy)
def test_org_sgiusa_model_membersearchcriteria_subDivisions_setter(instance):
    original = instance.subDivisions
    instance.subDivisions = original
    assert instance.subDivisions == original



@given(instance=org_sgiusa_model_MemberSearchCriteria_strategy)
def test_org_sgiusa_model_membersearchcriteria_activityGroups_setter(instance):
    original = instance.activityGroups
    instance.activityGroups = original
    assert instance.activityGroups == original

@given(instance=org_sgiusa_model_Member_strategy)
@settings(max_examples=50)
def test_org_sgiusa_model_member_instantiation(instance):
    assert isinstance(instance, org_sgiusa_model_Member)



@given(instance=org_sgiusa_model_Member_strategy)
def test_org_sgiusa_model_member_archived_setter(instance):
    original = instance.archived
    instance.archived = original
    assert instance.archived == original



@given(instance=org_sgiusa_model_Member_strategy)
def test_org_sgiusa_model_member_division_setter(instance):
    original = instance.division
    instance.division = original
    assert instance.division == original



@given(instance=org_sgiusa_model_Member_strategy)
def test_org_sgiusa_model_member_extraField2_setter(instance):
    original = instance.extraField2
    instance.extraField2 = original
    assert instance.extraField2 == original



@given(instance=org_sgiusa_model_Member_strategy)
def test_org_sgiusa_model_member_interests_setter(instance):
    original = instance.interests
    instance.interests = original
    assert instance.interests == original



@given(instance=org_sgiusa_model_Member_strategy)
def test_org_sgiusa_model_member_employer_setter(instance):
    original = instance.employer
    instance.employer = original
    assert instance.employer == original



@given(instance=org_sgiusa_model_Member_strategy)
def test_org_sgiusa_model_member_activityGroups_setter(instance):
    original = instance.activityGroups
    instance.activityGroups = original
    assert instance.activityGroups == original



@given(instance=org_sgiusa_model_Member_strategy)
def test_org_sgiusa_model_member_lastName_setter(instance):
    original = instance.lastName
    instance.lastName = original
    assert instance.lastName == original



@given(instance=org_sgiusa_model_Member_strategy)
def test_org_sgiusa_model_member_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original



@given(instance=org_sgiusa_model_Member_strategy)
def test_org_sgiusa_model_member_middleInitial_setter(instance):
    original = instance.middleInitial
    instance.middleInitial = original
    assert instance.middleInitial == original



@given(instance=org_sgiusa_model_Member_strategy)
def test_org_sgiusa_model_member_statusProfile_setter(instance):
    original = instance.statusProfile
    instance.statusProfile = original
    assert instance.statusProfile == original



@given(instance=org_sgiusa_model_Member_strategy)
def test_org_sgiusa_model_member_languages_setter(instance):
    original = instance.languages
    instance.languages = original
    assert instance.languages == original



@given(instance=org_sgiusa_model_Member_strategy)
def test_org_sgiusa_model_member_locatable_setter(instance):
    original = instance.locatable
    instance.locatable = original
    assert instance.locatable == original



@given(instance=org_sgiusa_model_Member_strategy)
def test_org_sgiusa_model_member_birthDate_setter(instance):
    original = instance.birthDate
    instance.birthDate = original
    assert instance.birthDate == original



@given(instance=org_sgiusa_model_Member_strategy)
def test_org_sgiusa_model_member_subDivision_setter(instance):
    original = instance.subDivision
    instance.subDivision = original
    assert instance.subDivision == original



@given(instance=org_sgiusa_model_Member_strategy)
def test_org_sgiusa_model_member_visible_setter(instance):
    original = instance.visible
    instance.visible = original
    assert instance.visible == original



@given(instance=org_sgiusa_model_Member_strategy)
def test_org_sgiusa_model_member_joinDate_setter(instance):
    original = instance.joinDate
    instance.joinDate = original
    assert instance.joinDate == original



@given(instance=org_sgiusa_model_Member_strategy)
def test_org_sgiusa_model_member_extraField1_setter(instance):
    original = instance.extraField1
    instance.extraField1 = original
    assert instance.extraField1 == original



@given(instance=org_sgiusa_model_Member_strategy)
def test_org_sgiusa_model_member_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=org_sgiusa_model_Member_strategy)
def test_org_sgiusa_model_member_occupation_setter(instance):
    original = instance.occupation
    instance.occupation = original
    assert instance.occupation == original

@given(instance=org_sgiusa_model_LeadershipInfo_strategy)
@settings(max_examples=50)
def test_org_sgiusa_model_leadershipinfo_instantiation(instance):
    assert isinstance(instance, org_sgiusa_model_LeadershipInfo)



@given(instance=org_sgiusa_model_LeadershipInfo_strategy)
def test_org_sgiusa_model_leadershipinfo_manualSigned_setter(instance):
    original = instance.manualSigned
    instance.manualSigned = original
    assert instance.manualSigned == original



@given(instance=org_sgiusa_model_LeadershipInfo_strategy)
def test_org_sgiusa_model_leadershipinfo_examPassed_setter(instance):
    original = instance.examPassed
    instance.examPassed = original
    assert instance.examPassed == original



@given(instance=org_sgiusa_model_LeadershipInfo_strategy)
def test_org_sgiusa_model_leadershipinfo_manualSignedDate_setter(instance):
    original = instance.manualSignedDate
    instance.manualSignedDate = original
    assert instance.manualSignedDate == original



@given(instance=org_sgiusa_model_LeadershipInfo_strategy)
def test_org_sgiusa_model_leadershipinfo_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=org_sgiusa_model_LeadershipInfo_strategy)
def test_org_sgiusa_model_leadershipinfo_examPassedDate_setter(instance):
    original = instance.examPassedDate
    instance.examPassedDate = original
    assert instance.examPassedDate == original



@given(instance=org_sgiusa_model_LeadershipInfo_strategy)
def test_org_sgiusa_model_leadershipinfo_lastUpdate_setter(instance):
    original = instance.lastUpdate
    instance.lastUpdate = original
    assert instance.lastUpdate == original

@given(instance=org_sgiusa_model_LeadershipRole_strategy)
@settings(max_examples=50)
def test_org_sgiusa_model_leadershiprole_instantiation(instance):
    assert isinstance(instance, org_sgiusa_model_LeadershipRole)



@given(instance=org_sgiusa_model_LeadershipRole_strategy)
def test_org_sgiusa_model_leadershiprole_activityGroup_setter(instance):
    original = instance.activityGroup
    instance.activityGroup = original
    assert instance.activityGroup == original



@given(instance=org_sgiusa_model_LeadershipRole_strategy)
def test_org_sgiusa_model_leadershiprole_position_setter(instance):
    original = instance.position
    instance.position = original
    assert instance.position == original



@given(instance=org_sgiusa_model_LeadershipRole_strategy)
def test_org_sgiusa_model_leadershiprole_endDate_setter(instance):
    original = instance.endDate
    instance.endDate = original
    assert instance.endDate == original



@given(instance=org_sgiusa_model_LeadershipRole_strategy)
def test_org_sgiusa_model_leadershiprole_active_setter(instance):
    original = instance.active
    instance.active = original
    assert instance.active == original



@given(instance=org_sgiusa_model_LeadershipRole_strategy)
def test_org_sgiusa_model_leadershiprole_division_setter(instance):
    original = instance.division
    instance.division = original
    assert instance.division == original



@given(instance=org_sgiusa_model_LeadershipRole_strategy)
def test_org_sgiusa_model_leadershiprole_subDivision_setter(instance):
    original = instance.subDivision
    instance.subDivision = original
    assert instance.subDivision == original



@given(instance=org_sgiusa_model_LeadershipRole_strategy)
def test_org_sgiusa_model_leadershiprole_startDate_setter(instance):
    original = instance.startDate
    instance.startDate = original
    assert instance.startDate == original



@given(instance=org_sgiusa_model_LeadershipRole_strategy)
def test_org_sgiusa_model_leadershiprole_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=org_sgiusa_model_LeadershipRole_strategy)
def test_org_sgiusa_model_leadershiprole_level_setter(instance):
    original = instance.level
    instance.level = original
    assert instance.level == original



@given(instance=org_sgiusa_model_LeadershipRole_strategy)
def test_org_sgiusa_model_leadershiprole_lastUpdate_setter(instance):
    original = instance.lastUpdate
    instance.lastUpdate = original
    assert instance.lastUpdate == original

@given(instance=org_sgiusa_model_GohonzonInfo_strategy)
@settings(max_examples=50)
def test_org_sgiusa_model_gohonzoninfo_instantiation(instance):
    assert isinstance(instance, org_sgiusa_model_GohonzonInfo)



@given(instance=org_sgiusa_model_GohonzonInfo_strategy)
def test_org_sgiusa_model_gohonzoninfo_returned_setter(instance):
    original = instance.returned
    instance.returned = original
    assert instance.returned == original



@given(instance=org_sgiusa_model_GohonzonInfo_strategy)
def test_org_sgiusa_model_gohonzoninfo_gohonzonType_setter(instance):
    original = instance.gohonzonType
    instance.gohonzonType = original
    assert instance.gohonzonType == original



@given(instance=org_sgiusa_model_GohonzonInfo_strategy)
def test_org_sgiusa_model_gohonzoninfo_receiveDate_setter(instance):
    original = instance.receiveDate
    instance.receiveDate = original
    assert instance.receiveDate == original



@given(instance=org_sgiusa_model_GohonzonInfo_strategy)
def test_org_sgiusa_model_gohonzoninfo_returnDate_setter(instance):
    original = instance.returnDate
    instance.returnDate = original
    assert instance.returnDate == original



@given(instance=org_sgiusa_model_GohonzonInfo_strategy)
def test_org_sgiusa_model_gohonzoninfo_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=org_sgiusa_model_GohonzonInfo_strategy)
def test_org_sgiusa_model_gohonzoninfo_lastUpdate_setter(instance):
    original = instance.lastUpdate
    instance.lastUpdate = original
    assert instance.lastUpdate == original

@given(instance=org_sgiusa_model_FamilyMember_strategy)
@settings(max_examples=50)
def test_org_sgiusa_model_familymember_instantiation(instance):
    assert isinstance(instance, org_sgiusa_model_FamilyMember)



@given(instance=org_sgiusa_model_FamilyMember_strategy)
def test_org_sgiusa_model_familymember_familyRelation_setter(instance):
    original = instance.familyRelation
    instance.familyRelation = original
    assert instance.familyRelation == original



@given(instance=org_sgiusa_model_FamilyMember_strategy)
def test_org_sgiusa_model_familymember_sgiMember_setter(instance):
    original = instance.sgiMember
    instance.sgiMember = original
    assert instance.sgiMember == original



@given(instance=org_sgiusa_model_FamilyMember_strategy)
def test_org_sgiusa_model_familymember_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=org_sgiusa_model_FamilyMember_strategy)
def test_org_sgiusa_model_familymember_personName_setter(instance):
    original = instance.personName
    instance.personName = original
    assert instance.personName == original



@given(instance=org_sgiusa_model_FamilyMember_strategy)
def test_org_sgiusa_model_familymember_lastUpdate_setter(instance):
    original = instance.lastUpdate
    instance.lastUpdate = original
    assert instance.lastUpdate == original

@given(instance=org_sgiusa_model_Event_strategy)
@settings(max_examples=50)
def test_org_sgiusa_model_event_instantiation(instance):
    assert isinstance(instance, org_sgiusa_model_Event)



@given(instance=org_sgiusa_model_Event_strategy)
def test_org_sgiusa_model_event_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original



@given(instance=org_sgiusa_model_Event_strategy)
def test_org_sgiusa_model_event_userId_setter(instance):
    original = instance.userId
    instance.userId = original
    assert instance.userId == original



@given(instance=org_sgiusa_model_Event_strategy)
def test_org_sgiusa_model_event_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=org_sgiusa_model_Event_strategy)
def test_org_sgiusa_model_event_divisions_setter(instance):
    original = instance.divisions
    instance.divisions = original
    assert instance.divisions == original



@given(instance=org_sgiusa_model_Event_strategy)
def test_org_sgiusa_model_event_subDivisions_setter(instance):
    original = instance.subDivisions
    instance.subDivisions = original
    assert instance.subDivisions == original

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

@given(instance=org_sgiusa_model_EmailList_strategy)
@settings(max_examples=50)
def test_org_sgiusa_model_emaillist_instantiation(instance):
    assert isinstance(instance, org_sgiusa_model_EmailList)



@given(instance=org_sgiusa_model_EmailList_strategy)
def test_org_sgiusa_model_emaillist_subDivisions_setter(instance):
    original = instance.subDivisions
    instance.subDivisions = original
    assert instance.subDivisions == original



@given(instance=org_sgiusa_model_EmailList_strategy)
def test_org_sgiusa_model_emaillist_divisions_setter(instance):
    original = instance.divisions
    instance.divisions = original
    assert instance.divisions == original



@given(instance=org_sgiusa_model_EmailList_strategy)
def test_org_sgiusa_model_emaillist_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=org_sgiusa_model_EmailList_strategy)
def test_org_sgiusa_model_emaillist_enabled_setter(instance):
    original = instance.enabled
    instance.enabled = original
    assert instance.enabled == original



@given(instance=org_sgiusa_model_EmailList_strategy)
def test_org_sgiusa_model_emaillist_activityGroups_setter(instance):
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

@given(instance=MembershipInfo_strategy)
@settings(max_examples=50)
def test_membershipinfo_instantiation(instance):
    assert isinstance(instance, MembershipInfo)

@given(instance=org_sgiusa_model_EStringToStringMapEntry_strategy)
@settings(max_examples=50)
def test_org_sgiusa_model_estringtostringmapentry_instantiation(instance):
    assert isinstance(instance, org_sgiusa_model_EStringToStringMapEntry)

@given(instance=org_sgiusa_model_DocumentRoot_strategy)
@settings(max_examples=50)
def test_org_sgiusa_model_documentroot_instantiation(instance):
    assert isinstance(instance, org_sgiusa_model_DocumentRoot)



@given(instance=org_sgiusa_model_DocumentRoot_strategy)
def test_org_sgiusa_model_documentroot_mixed_setter(instance):
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

@given(instance=org_aries_common_User_strategy)
@settings(max_examples=50)
def test_org_aries_common_user_instantiation(instance):
    assert isinstance(instance, org_aries_common_User)



@given(instance=org_aries_common_User_strategy)
def test_org_aries_common_user_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original



@given(instance=org_aries_common_User_strategy)
def test_org_aries_common_user_userId_setter(instance):
    original = instance.userId
    instance.userId = original
    assert instance.userId == original



@given(instance=org_aries_common_User_strategy)
def test_org_aries_common_user_enabled_setter(instance):
    original = instance.enabled
    instance.enabled = original
    assert instance.enabled == original



@given(instance=org_aries_common_User_strategy)
def test_org_aries_common_user_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=org_aries_common_User_strategy)
def test_org_aries_common_user_lastName_setter(instance):
    original = instance.lastName
    instance.lastName = original
    assert instance.lastName == original



@given(instance=org_aries_common_User_strategy)
def test_org_aries_common_user_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original

@given(instance=org_aries_common_ZipCode_strategy)
@settings(max_examples=50)
def test_org_aries_common_zipcode_instantiation(instance):
    assert isinstance(instance, org_aries_common_ZipCode)



@given(instance=org_aries_common_ZipCode_strategy)
def test_org_aries_common_zipcode_country_setter(instance):
    original = instance.country
    instance.country = original
    assert instance.country == original



@given(instance=org_aries_common_ZipCode_strategy)
def test_org_aries_common_zipcode_extension_setter(instance):
    original = instance.extension
    instance.extension = original
    assert instance.extension == original



@given(instance=org_aries_common_ZipCode_strategy)
def test_org_aries_common_zipcode_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original

@given(instance=org_aries_common_StreetAddress_strategy)
@settings(max_examples=50)
def test_org_aries_common_streetaddress_instantiation(instance):
    assert isinstance(instance, org_aries_common_StreetAddress)



@given(instance=org_aries_common_StreetAddress_strategy)
def test_org_aries_common_streetaddress_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=org_aries_common_StreetAddress_strategy)
def test_org_aries_common_streetaddress_city_setter(instance):
    original = instance.city
    instance.city = original
    assert instance.city == original



@given(instance=org_aries_common_StreetAddress_strategy)
def test_org_aries_common_streetaddress_country_setter(instance):
    original = instance.country
    instance.country = original
    assert instance.country == original



@given(instance=org_aries_common_StreetAddress_strategy)
def test_org_aries_common_streetaddress_latitude_setter(instance):
    original = instance.latitude
    instance.latitude = original
    assert instance.latitude == original



@given(instance=org_aries_common_StreetAddress_strategy)
def test_org_aries_common_streetaddress_longitude_setter(instance):
    original = instance.longitude
    instance.longitude = original
    assert instance.longitude == original



@given(instance=org_aries_common_StreetAddress_strategy)
def test_org_aries_common_streetaddress_street_setter(instance):
    original = instance.street
    instance.street = original
    assert instance.street == original



@given(instance=org_aries_common_StreetAddress_strategy)
def test_org_aries_common_streetaddress_state_setter(instance):
    original = instance.state
    instance.state = original
    assert instance.state == original

@given(instance=org_aries_common_PhoneNumber_strategy)
@settings(max_examples=50)
def test_org_aries_common_phonenumber_instantiation(instance):
    assert isinstance(instance, org_aries_common_PhoneNumber)



@given(instance=org_aries_common_PhoneNumber_strategy)
def test_org_aries_common_phonenumber_extension_setter(instance):
    original = instance.extension
    instance.extension = original
    assert instance.extension == original



@given(instance=org_aries_common_PhoneNumber_strategy)
def test_org_aries_common_phonenumber_country_setter(instance):
    original = instance.country
    instance.country = original
    assert instance.country == original



@given(instance=org_aries_common_PhoneNumber_strategy)
def test_org_aries_common_phonenumber_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original



@given(instance=org_aries_common_PhoneNumber_strategy)
def test_org_aries_common_phonenumber_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=org_aries_common_PhoneNumber_strategy)
def test_org_aries_common_phonenumber_area_setter(instance):
    original = instance.area
    instance.area = original
    assert instance.area == original



@given(instance=org_aries_common_PhoneNumber_strategy)
def test_org_aries_common_phonenumber_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=org_aries_common_PhoneNumber_strategy)
def test_org_aries_common_phonenumber_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=org_aries_common_Property_strategy)
@settings(max_examples=50)
def test_org_aries_common_property_instantiation(instance):
    assert isinstance(instance, org_aries_common_Property)



@given(instance=org_aries_common_Property_strategy)
def test_org_aries_common_property_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=org_aries_common_Property_strategy)
def test_org_aries_common_property_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=org_aries_common_Property_strategy)
def test_org_aries_common_property_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=org_aries_common_Property_strategy)
def test_org_aries_common_property_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=org_aries_common_Properties_strategy)
@settings(max_examples=50)
def test_org_aries_common_properties_instantiation(instance):
    assert isinstance(instance, org_aries_common_Properties)

@given(instance=org_aries_common_Person_strategy)
@settings(max_examples=50)
def test_org_aries_common_person_instantiation(instance):
    assert isinstance(instance, org_aries_common_Person)



@given(instance=org_aries_common_Person_strategy)
def test_org_aries_common_person_userId_setter(instance):
    original = instance.userId
    instance.userId = original
    assert instance.userId == original



@given(instance=org_aries_common_Person_strategy)
def test_org_aries_common_person_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=org_aries_common_PersonName_strategy)
@settings(max_examples=50)
def test_org_aries_common_personname_instantiation(instance):
    assert isinstance(instance, org_aries_common_PersonName)



@given(instance=org_aries_common_PersonName_strategy)
def test_org_aries_common_personname_middleInitial_setter(instance):
    original = instance.middleInitial
    instance.middleInitial = original
    assert instance.middleInitial == original



@given(instance=org_aries_common_PersonName_strategy)
def test_org_aries_common_personname_lastName_setter(instance):
    original = instance.lastName
    instance.lastName = original
    assert instance.lastName == original



@given(instance=org_aries_common_PersonName_strategy)
def test_org_aries_common_personname_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original

@given(instance=org_aries_common_EObject_strategy)
@settings(max_examples=50)
def test_org_aries_common_eobject_instantiation(instance):
    assert isinstance(instance, org_aries_common_EObject)

@given(instance=org_aries_common_MapEntry_strategy)
@settings(max_examples=50)
def test_org_aries_common_mapentry_instantiation(instance):
    assert isinstance(instance, org_aries_common_MapEntry)

@given(instance=org_aries_common_Map_strategy)
@settings(max_examples=50)
def test_org_aries_common_map_instantiation(instance):
    assert isinstance(instance, org_aries_common_Map)

@given(instance=org_aries_common_Note_strategy)
@settings(max_examples=50)
def test_org_aries_common_note_instantiation(instance):
    assert isinstance(instance, org_aries_common_Note)



@given(instance=org_aries_common_Note_strategy)
def test_org_aries_common_note_creationDate_setter(instance):
    original = instance.creationDate
    instance.creationDate = original
    assert instance.creationDate == original



@given(instance=org_aries_common_Note_strategy)
def test_org_aries_common_note_lastUpdate_setter(instance):
    original = instance.lastUpdate
    instance.lastUpdate = original
    assert instance.lastUpdate == original



@given(instance=org_aries_common_Note_strategy)
def test_org_aries_common_note_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=org_aries_common_Note_strategy)
def test_org_aries_common_note_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=org_aries_common_Event_strategy)
@settings(max_examples=50)
def test_org_aries_common_event_instantiation(instance):
    assert isinstance(instance, org_aries_common_Event)



@given(instance=org_aries_common_Event_strategy)
def test_org_aries_common_event_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=org_aries_common_EmailMessage_strategy)
@settings(max_examples=50)
def test_org_aries_common_emailmessage_instantiation(instance):
    assert isinstance(instance, org_aries_common_EmailMessage)



@given(instance=org_aries_common_EmailMessage_strategy)
def test_org_aries_common_emailmessage_subject_setter(instance):
    original = instance.subject
    instance.subject = original
    assert instance.subject == original



@given(instance=org_aries_common_EmailMessage_strategy)
def test_org_aries_common_emailmessage_timestamp_setter(instance):
    original = instance.timestamp
    instance.timestamp = original
    assert instance.timestamp == original



@given(instance=org_aries_common_EmailMessage_strategy)
def test_org_aries_common_emailmessage_smtpPort_setter(instance):
    original = instance.smtpPort
    instance.smtpPort = original
    assert instance.smtpPort == original



@given(instance=org_aries_common_EmailMessage_strategy)
def test_org_aries_common_emailmessage_smtpHost_setter(instance):
    original = instance.smtpHost
    instance.smtpHost = original
    assert instance.smtpHost == original



@given(instance=org_aries_common_EmailMessage_strategy)
def test_org_aries_common_emailmessage_sendAsHtml_setter(instance):
    original = instance.sendAsHtml
    instance.sendAsHtml = original
    assert instance.sendAsHtml == original



@given(instance=org_aries_common_EmailMessage_strategy)
def test_org_aries_common_emailmessage_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=org_aries_common_EmailMessage_strategy)
def test_org_aries_common_emailmessage_sourceId_setter(instance):
    original = instance.sourceId
    instance.sourceId = original
    assert instance.sourceId == original



@given(instance=org_aries_common_EmailMessage_strategy)
def test_org_aries_common_emailmessage_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original

@given(instance=org_aries_common_EmailBox_strategy)
@settings(max_examples=50)
def test_org_aries_common_emailbox_instantiation(instance):
    assert isinstance(instance, org_aries_common_EmailBox)



@given(instance=org_aries_common_EmailBox_strategy)
def test_org_aries_common_emailbox_creationDate_setter(instance):
    original = instance.creationDate
    instance.creationDate = original
    assert instance.creationDate == original



@given(instance=org_aries_common_EmailBox_strategy)
def test_org_aries_common_emailbox_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=org_aries_common_EmailBox_strategy)
def test_org_aries_common_emailbox_lastUpdate_setter(instance):
    original = instance.lastUpdate
    instance.lastUpdate = original
    assert instance.lastUpdate == original



@given(instance=org_aries_common_EmailBox_strategy)
def test_org_aries_common_emailbox_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=org_aries_common_EmailBox_strategy)
def test_org_aries_common_emailbox_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=org_aries_common_EmailAddressList_strategy)
@settings(max_examples=50)
def test_org_aries_common_emailaddresslist_instantiation(instance):
    assert isinstance(instance, org_aries_common_EmailAddressList)



@given(instance=org_aries_common_EmailAddressList_strategy)
def test_org_aries_common_emailaddresslist_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=org_aries_common_EmailAddressList_strategy)
def test_org_aries_common_emailaddresslist_emailAddress_setter(instance):
    original = instance.emailAddress
    instance.emailAddress = original
    assert instance.emailAddress == original

@given(instance=org_aries_common_EmailAddress_strategy)
@settings(max_examples=50)
def test_org_aries_common_emailaddress_instantiation(instance):
    assert isinstance(instance, org_aries_common_EmailAddress)



@given(instance=org_aries_common_EmailAddress_strategy)
def test_org_aries_common_emailaddress_creationDate_setter(instance):
    original = instance.creationDate
    instance.creationDate = original
    assert instance.creationDate == original



@given(instance=org_aries_common_EmailAddress_strategy)
def test_org_aries_common_emailaddress_lastName_setter(instance):
    original = instance.lastName
    instance.lastName = original
    assert instance.lastName == original



@given(instance=org_aries_common_EmailAddress_strategy)
def test_org_aries_common_emailaddress_url_setter(instance):
    original = instance.url
    instance.url = original
    assert instance.url == original



@given(instance=org_aries_common_EmailAddress_strategy)
def test_org_aries_common_emailaddress_organization_setter(instance):
    original = instance.organization
    instance.organization = original
    assert instance.organization == original



@given(instance=org_aries_common_EmailAddress_strategy)
def test_org_aries_common_emailaddress_enabled_setter(instance):
    original = instance.enabled
    instance.enabled = original
    assert instance.enabled == original



@given(instance=org_aries_common_EmailAddress_strategy)
def test_org_aries_common_emailaddress_lastUpdate_setter(instance):
    original = instance.lastUpdate
    instance.lastUpdate = original
    assert instance.lastUpdate == original



@given(instance=org_aries_common_EmailAddress_strategy)
def test_org_aries_common_emailaddress_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=org_aries_common_EmailAddress_strategy)
def test_org_aries_common_emailaddress_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original



@given(instance=org_aries_common_EmailAddress_strategy)
def test_org_aries_common_emailaddress_userId_setter(instance):
    original = instance.userId
    instance.userId = original
    assert instance.userId == original

@given(instance=org_aries_common_EmailAccount_strategy)
@settings(max_examples=50)
def test_org_aries_common_emailaccount_instantiation(instance):
    assert isinstance(instance, org_aries_common_EmailAccount)



@given(instance=org_aries_common_EmailAccount_strategy)
def test_org_aries_common_emailaccount_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original



@given(instance=org_aries_common_EmailAccount_strategy)
def test_org_aries_common_emailaccount_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=org_aries_common_EmailAccount_strategy)
def test_org_aries_common_emailaccount_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=org_aries_common_EmailAccount_strategy)
def test_org_aries_common_emailaccount_enabled_setter(instance):
    original = instance.enabled
    instance.enabled = original
    assert instance.enabled == original



@given(instance=org_aries_common_EmailAccount_strategy)
def test_org_aries_common_emailaccount_userId_setter(instance):
    original = instance.userId
    instance.userId = original
    assert instance.userId == original



@given(instance=org_aries_common_EmailAccount_strategy)
def test_org_aries_common_emailaccount_lastName_setter(instance):
    original = instance.lastName
    instance.lastName = original
    assert instance.lastName == original

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

@given(instance=org_aries_common_EStringToStringMapEntry_strategy)
@settings(max_examples=50)
def test_org_aries_common_estringtostringmapentry_instantiation(instance):
    assert isinstance(instance, org_aries_common_EStringToStringMapEntry)

@given(instance=org_aries_common_DocumentRoot_strategy)
@settings(max_examples=50)
def test_org_aries_common_documentroot_instantiation(instance):
    assert isinstance(instance, org_aries_common_DocumentRoot)



@given(instance=org_aries_common_DocumentRoot_strategy)
def test_org_aries_common_documentroot_mixed_setter(instance):
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

@given(instance=org_aries_common_Attachment_strategy)
@settings(max_examples=50)
def test_org_aries_common_attachment_instantiation(instance):
    assert isinstance(instance, org_aries_common_Attachment)



@given(instance=org_aries_common_Attachment_strategy)
def test_org_aries_common_attachment_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=org_aries_common_Attachment_strategy)
def test_org_aries_common_attachment_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original



@given(instance=org_aries_common_Attachment_strategy)
def test_org_aries_common_attachment_contentType_setter(instance):
    original = instance.contentType
    instance.contentType = original
    assert instance.contentType == original



@given(instance=org_aries_common_Attachment_strategy)
def test_org_aries_common_attachment_fileName_setter(instance):
    original = instance.fileName
    instance.fileName = original
    assert instance.fileName == original



@given(instance=org_aries_common_Attachment_strategy)
def test_org_aries_common_attachment_fileData_setter(instance):
    original = instance.fileData
    instance.fileData = original
    assert instance.fileData == original



@given(instance=org_aries_common_Attachment_strategy)
def test_org_aries_common_attachment_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original
