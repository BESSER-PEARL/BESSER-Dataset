import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    SubjectSheduleController,
    ActivityType,
    Subject,
    SubjectShedule,
    DocumentStorage,
    TimeCreditForEducationalSemester,
    EducationalPlan,
    Specialty,
    Group,
    TimeInterval,
    Auditorium,
    Users,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_subjectshedulecontroller_is_not_abstract():
    assert not inspect.isabstract(SubjectSheduleController)


def test_subjectshedulecontroller_constructor_exists():
    assert callable(SubjectSheduleController.__init__)


def test_subjectshedulecontroller_constructor_args():
    sig = inspect.signature(SubjectSheduleController.__init__)
    params = list(sig.parameters.keys())
    assert "auditoriumNumberService" in params, "Missing parameter 'auditoriumNumberService'"
    assert "groupNumberService" in params, "Missing parameter 'groupNumberService'"
    assert "subjectCodeService" in params, "Missing parameter 'subjectCodeService'"
    assert "individualIdentificationCodeService" in params, "Missing parameter 'individualIdentificationCodeService'"
    assert "dateService" in params, "Missing parameter 'dateService'"
    assert "activityTypeCodeService" in params, "Missing parameter 'activityTypeCodeService'"

def test_subjectshedulecontroller_has_auditoriumNumberService():
    assert hasattr(SubjectSheduleController, "auditoriumNumberService")
    descriptor = None
    for klass in SubjectSheduleController.__mro__:
        if "auditoriumNumberService" in klass.__dict__:
            descriptor = klass.__dict__["auditoriumNumberService"]
            break
    assert isinstance(descriptor, property)

def test_subjectshedulecontroller_has_groupNumberService():
    assert hasattr(SubjectSheduleController, "groupNumberService")
    descriptor = None
    for klass in SubjectSheduleController.__mro__:
        if "groupNumberService" in klass.__dict__:
            descriptor = klass.__dict__["groupNumberService"]
            break
    assert isinstance(descriptor, property)

def test_subjectshedulecontroller_has_subjectCodeService():
    assert hasattr(SubjectSheduleController, "subjectCodeService")
    descriptor = None
    for klass in SubjectSheduleController.__mro__:
        if "subjectCodeService" in klass.__dict__:
            descriptor = klass.__dict__["subjectCodeService"]
            break
    assert isinstance(descriptor, property)

def test_subjectshedulecontroller_has_individualIdentificationCodeService():
    assert hasattr(SubjectSheduleController, "individualIdentificationCodeService")
    descriptor = None
    for klass in SubjectSheduleController.__mro__:
        if "individualIdentificationCodeService" in klass.__dict__:
            descriptor = klass.__dict__["individualIdentificationCodeService"]
            break
    assert isinstance(descriptor, property)

def test_subjectshedulecontroller_has_dateService():
    assert hasattr(SubjectSheduleController, "dateService")
    descriptor = None
    for klass in SubjectSheduleController.__mro__:
        if "dateService" in klass.__dict__:
            descriptor = klass.__dict__["dateService"]
            break
    assert isinstance(descriptor, property)

def test_subjectshedulecontroller_has_activityTypeCodeService():
    assert hasattr(SubjectSheduleController, "activityTypeCodeService")
    descriptor = None
    for klass in SubjectSheduleController.__mro__:
        if "activityTypeCodeService" in klass.__dict__:
            descriptor = klass.__dict__["activityTypeCodeService"]
            break
    assert isinstance(descriptor, property)



def test_activitytype_is_not_abstract():
    assert not inspect.isabstract(ActivityType)


def test_activitytype_constructor_exists():
    assert callable(ActivityType.__init__)


def test_activitytype_constructor_args():
    sig = inspect.signature(ActivityType.__init__)
    params = list(sig.parameters.keys())
    assert "activityTypeCode" in params, "Missing parameter 'activityTypeCode'"
    assert "id" in params, "Missing parameter 'id'"
    assert "subjectCode" in params, "Missing parameter 'subjectCode'"
    assert "activityTypeName" in params, "Missing parameter 'activityTypeName'"

def test_activitytype_has_activityTypeCode():
    assert hasattr(ActivityType, "activityTypeCode")
    descriptor = None
    for klass in ActivityType.__mro__:
        if "activityTypeCode" in klass.__dict__:
            descriptor = klass.__dict__["activityTypeCode"]
            break
    assert isinstance(descriptor, property)

def test_activitytype_has_id():
    assert hasattr(ActivityType, "id")
    descriptor = None
    for klass in ActivityType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_activitytype_has_subjectCode():
    assert hasattr(ActivityType, "subjectCode")
    descriptor = None
    for klass in ActivityType.__mro__:
        if "subjectCode" in klass.__dict__:
            descriptor = klass.__dict__["subjectCode"]
            break
    assert isinstance(descriptor, property)

def test_activitytype_has_activityTypeName():
    assert hasattr(ActivityType, "activityTypeName")
    descriptor = None
    for klass in ActivityType.__mro__:
        if "activityTypeName" in klass.__dict__:
            descriptor = klass.__dict__["activityTypeName"]
            break
    assert isinstance(descriptor, property)



def test_subject_is_not_abstract():
    assert not inspect.isabstract(Subject)


def test_subject_constructor_exists():
    assert callable(Subject.__init__)


def test_subject_constructor_args():
    sig = inspect.signature(Subject.__init__)
    params = list(sig.parameters.keys())
    assert "subjectName" in params, "Missing parameter 'subjectName'"
    assert "subjectCode" in params, "Missing parameter 'subjectCode'"
    assert "id" in params, "Missing parameter 'id'"

def test_subject_has_subjectName():
    assert hasattr(Subject, "subjectName")
    descriptor = None
    for klass in Subject.__mro__:
        if "subjectName" in klass.__dict__:
            descriptor = klass.__dict__["subjectName"]
            break
    assert isinstance(descriptor, property)

def test_subject_has_subjectCode():
    assert hasattr(Subject, "subjectCode")
    descriptor = None
    for klass in Subject.__mro__:
        if "subjectCode" in klass.__dict__:
            descriptor = klass.__dict__["subjectCode"]
            break
    assert isinstance(descriptor, property)

def test_subject_has_id():
    assert hasattr(Subject, "id")
    descriptor = None
    for klass in Subject.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_subjectshedule_is_not_abstract():
    assert not inspect.isabstract(SubjectShedule)


def test_subjectshedule_constructor_exists():
    assert callable(SubjectShedule.__init__)


def test_subjectshedule_constructor_args():
    sig = inspect.signature(SubjectShedule.__init__)
    params = list(sig.parameters.keys())
    assert "individualIdentificationCode" in params, "Missing parameter 'individualIdentificationCode'"
    assert "auditoriumNumber" in params, "Missing parameter 'auditoriumNumber'"
    assert "groupNumber" in params, "Missing parameter 'groupNumber'"
    assert "subjectCode" in params, "Missing parameter 'subjectCode'"
    assert "activityTypeCode" in params, "Missing parameter 'activityTypeCode'"
    assert "date" in params, "Missing parameter 'date'"
    assert "id" in params, "Missing parameter 'id'"

def test_subjectshedule_has_individualIdentificationCode():
    assert hasattr(SubjectShedule, "individualIdentificationCode")
    descriptor = None
    for klass in SubjectShedule.__mro__:
        if "individualIdentificationCode" in klass.__dict__:
            descriptor = klass.__dict__["individualIdentificationCode"]
            break
    assert isinstance(descriptor, property)

def test_subjectshedule_has_auditoriumNumber():
    assert hasattr(SubjectShedule, "auditoriumNumber")
    descriptor = None
    for klass in SubjectShedule.__mro__:
        if "auditoriumNumber" in klass.__dict__:
            descriptor = klass.__dict__["auditoriumNumber"]
            break
    assert isinstance(descriptor, property)

def test_subjectshedule_has_groupNumber():
    assert hasattr(SubjectShedule, "groupNumber")
    descriptor = None
    for klass in SubjectShedule.__mro__:
        if "groupNumber" in klass.__dict__:
            descriptor = klass.__dict__["groupNumber"]
            break
    assert isinstance(descriptor, property)

def test_subjectshedule_has_subjectCode():
    assert hasattr(SubjectShedule, "subjectCode")
    descriptor = None
    for klass in SubjectShedule.__mro__:
        if "subjectCode" in klass.__dict__:
            descriptor = klass.__dict__["subjectCode"]
            break
    assert isinstance(descriptor, property)

def test_subjectshedule_has_activityTypeCode():
    assert hasattr(SubjectShedule, "activityTypeCode")
    descriptor = None
    for klass in SubjectShedule.__mro__:
        if "activityTypeCode" in klass.__dict__:
            descriptor = klass.__dict__["activityTypeCode"]
            break
    assert isinstance(descriptor, property)

def test_subjectshedule_has_date():
    assert hasattr(SubjectShedule, "date")
    descriptor = None
    for klass in SubjectShedule.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)

def test_subjectshedule_has_id():
    assert hasattr(SubjectShedule, "id")
    descriptor = None
    for klass in SubjectShedule.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_documentstorage_is_not_abstract():
    assert not inspect.isabstract(DocumentStorage)


def test_documentstorage_constructor_exists():
    assert callable(DocumentStorage.__init__)


def test_documentstorage_constructor_args():
    sig = inspect.signature(DocumentStorage.__init__)
    params = list(sig.parameters.keys())
    assert "documentPath" in params, "Missing parameter 'documentPath'"
    assert "documentCode" in params, "Missing parameter 'documentCode'"
    assert "id" in params, "Missing parameter 'id'"
    assert "is_exist" in params, "Missing parameter 'is_exist'"

def test_documentstorage_has_documentPath():
    assert hasattr(DocumentStorage, "documentPath")
    descriptor = None
    for klass in DocumentStorage.__mro__:
        if "documentPath" in klass.__dict__:
            descriptor = klass.__dict__["documentPath"]
            break
    assert isinstance(descriptor, property)

def test_documentstorage_has_documentCode():
    assert hasattr(DocumentStorage, "documentCode")
    descriptor = None
    for klass in DocumentStorage.__mro__:
        if "documentCode" in klass.__dict__:
            descriptor = klass.__dict__["documentCode"]
            break
    assert isinstance(descriptor, property)

def test_documentstorage_has_id():
    assert hasattr(DocumentStorage, "id")
    descriptor = None
    for klass in DocumentStorage.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_documentstorage_has_is_exist():
    assert hasattr(DocumentStorage, "is_exist")
    descriptor = None
    for klass in DocumentStorage.__mro__:
        if "is_exist" in klass.__dict__:
            descriptor = klass.__dict__["is_exist"]
            break
    assert isinstance(descriptor, property)



def test_timecreditforeducationalsemester_is_not_abstract():
    assert not inspect.isabstract(TimeCreditForEducationalSemester)


def test_timecreditforeducationalsemester_constructor_exists():
    assert callable(TimeCreditForEducationalSemester.__init__)


def test_timecreditforeducationalsemester_constructor_args():
    sig = inspect.signature(TimeCreditForEducationalSemester.__init__)
    params = list(sig.parameters.keys())
    assert "groupNumber" in params, "Missing parameter 'groupNumber'"
    assert "subjectCode" in params, "Missing parameter 'subjectCode'"
    assert "totalHours" in params, "Missing parameter 'totalHours'"
    assert "activityTypeCode" in params, "Missing parameter 'activityTypeCode'"
    assert "id" in params, "Missing parameter 'id'"

def test_timecreditforeducationalsemester_has_groupNumber():
    assert hasattr(TimeCreditForEducationalSemester, "groupNumber")
    descriptor = None
    for klass in TimeCreditForEducationalSemester.__mro__:
        if "groupNumber" in klass.__dict__:
            descriptor = klass.__dict__["groupNumber"]
            break
    assert isinstance(descriptor, property)

def test_timecreditforeducationalsemester_has_subjectCode():
    assert hasattr(TimeCreditForEducationalSemester, "subjectCode")
    descriptor = None
    for klass in TimeCreditForEducationalSemester.__mro__:
        if "subjectCode" in klass.__dict__:
            descriptor = klass.__dict__["subjectCode"]
            break
    assert isinstance(descriptor, property)

def test_timecreditforeducationalsemester_has_totalHours():
    assert hasattr(TimeCreditForEducationalSemester, "totalHours")
    descriptor = None
    for klass in TimeCreditForEducationalSemester.__mro__:
        if "totalHours" in klass.__dict__:
            descriptor = klass.__dict__["totalHours"]
            break
    assert isinstance(descriptor, property)

def test_timecreditforeducationalsemester_has_activityTypeCode():
    assert hasattr(TimeCreditForEducationalSemester, "activityTypeCode")
    descriptor = None
    for klass in TimeCreditForEducationalSemester.__mro__:
        if "activityTypeCode" in klass.__dict__:
            descriptor = klass.__dict__["activityTypeCode"]
            break
    assert isinstance(descriptor, property)

def test_timecreditforeducationalsemester_has_id():
    assert hasattr(TimeCreditForEducationalSemester, "id")
    descriptor = None
    for klass in TimeCreditForEducationalSemester.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_educationalplan_is_not_abstract():
    assert not inspect.isabstract(EducationalPlan)


def test_educationalplan_constructor_exists():
    assert callable(EducationalPlan.__init__)


def test_educationalplan_constructor_args():
    sig = inspect.signature(EducationalPlan.__init__)
    params = list(sig.parameters.keys())
    assert "subjectCode" in params, "Missing parameter 'subjectCode'"
    assert "id" in params, "Missing parameter 'id'"
    assert "individualIdentificationCode" in params, "Missing parameter 'individualIdentificationCode'"

def test_educationalplan_has_subjectCode():
    assert hasattr(EducationalPlan, "subjectCode")
    descriptor = None
    for klass in EducationalPlan.__mro__:
        if "subjectCode" in klass.__dict__:
            descriptor = klass.__dict__["subjectCode"]
            break
    assert isinstance(descriptor, property)

def test_educationalplan_has_id():
    assert hasattr(EducationalPlan, "id")
    descriptor = None
    for klass in EducationalPlan.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_educationalplan_has_individualIdentificationCode():
    assert hasattr(EducationalPlan, "individualIdentificationCode")
    descriptor = None
    for klass in EducationalPlan.__mro__:
        if "individualIdentificationCode" in klass.__dict__:
            descriptor = klass.__dict__["individualIdentificationCode"]
            break
    assert isinstance(descriptor, property)



def test_specialty_is_not_abstract():
    assert not inspect.isabstract(Specialty)


def test_specialty_constructor_exists():
    assert callable(Specialty.__init__)


def test_specialty_constructor_args():
    sig = inspect.signature(Specialty.__init__)
    params = list(sig.parameters.keys())
    assert "specialtyCode" in params, "Missing parameter 'specialtyCode'"
    assert "specialtyName" in params, "Missing parameter 'specialtyName'"
    assert "id" in params, "Missing parameter 'id'"
    assert "subjectCode" in params, "Missing parameter 'subjectCode'"

def test_specialty_has_specialtyCode():
    assert hasattr(Specialty, "specialtyCode")
    descriptor = None
    for klass in Specialty.__mro__:
        if "specialtyCode" in klass.__dict__:
            descriptor = klass.__dict__["specialtyCode"]
            break
    assert isinstance(descriptor, property)

def test_specialty_has_specialtyName():
    assert hasattr(Specialty, "specialtyName")
    descriptor = None
    for klass in Specialty.__mro__:
        if "specialtyName" in klass.__dict__:
            descriptor = klass.__dict__["specialtyName"]
            break
    assert isinstance(descriptor, property)

def test_specialty_has_id():
    assert hasattr(Specialty, "id")
    descriptor = None
    for klass in Specialty.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_specialty_has_subjectCode():
    assert hasattr(Specialty, "subjectCode")
    descriptor = None
    for klass in Specialty.__mro__:
        if "subjectCode" in klass.__dict__:
            descriptor = klass.__dict__["subjectCode"]
            break
    assert isinstance(descriptor, property)



def test_group_is_not_abstract():
    assert not inspect.isabstract(Group)


def test_group_constructor_exists():
    assert callable(Group.__init__)


def test_group_constructor_args():
    sig = inspect.signature(Group.__init__)
    params = list(sig.parameters.keys())
    assert "groupNumber" in params, "Missing parameter 'groupNumber'"
    assert "educationalYear" in params, "Missing parameter 'educationalYear'"
    assert "specialtyCode" in params, "Missing parameter 'specialtyCode'"
    assert "id" in params, "Missing parameter 'id'"

def test_group_has_groupNumber():
    assert hasattr(Group, "groupNumber")
    descriptor = None
    for klass in Group.__mro__:
        if "groupNumber" in klass.__dict__:
            descriptor = klass.__dict__["groupNumber"]
            break
    assert isinstance(descriptor, property)

def test_group_has_educationalYear():
    assert hasattr(Group, "educationalYear")
    descriptor = None
    for klass in Group.__mro__:
        if "educationalYear" in klass.__dict__:
            descriptor = klass.__dict__["educationalYear"]
            break
    assert isinstance(descriptor, property)

def test_group_has_specialtyCode():
    assert hasattr(Group, "specialtyCode")
    descriptor = None
    for klass in Group.__mro__:
        if "specialtyCode" in klass.__dict__:
            descriptor = klass.__dict__["specialtyCode"]
            break
    assert isinstance(descriptor, property)

def test_group_has_id():
    assert hasattr(Group, "id")
    descriptor = None
    for klass in Group.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_timeinterval_is_not_abstract():
    assert not inspect.isabstract(TimeInterval)


def test_timeinterval_constructor_exists():
    assert callable(TimeInterval.__init__)


def test_timeinterval_constructor_args():
    sig = inspect.signature(TimeInterval.__init__)
    params = list(sig.parameters.keys())
    assert "date" in params, "Missing parameter 'date'"
    assert "weekIdentifier" in params, "Missing parameter 'weekIdentifier'"
    assert "id" in params, "Missing parameter 'id'"
    assert "weekday" in params, "Missing parameter 'weekday'"
    assert "classOrder" in params, "Missing parameter 'classOrder'"

def test_timeinterval_has_date():
    assert hasattr(TimeInterval, "date")
    descriptor = None
    for klass in TimeInterval.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)

def test_timeinterval_has_weekIdentifier():
    assert hasattr(TimeInterval, "weekIdentifier")
    descriptor = None
    for klass in TimeInterval.__mro__:
        if "weekIdentifier" in klass.__dict__:
            descriptor = klass.__dict__["weekIdentifier"]
            break
    assert isinstance(descriptor, property)

def test_timeinterval_has_id():
    assert hasattr(TimeInterval, "id")
    descriptor = None
    for klass in TimeInterval.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_timeinterval_has_weekday():
    assert hasattr(TimeInterval, "weekday")
    descriptor = None
    for klass in TimeInterval.__mro__:
        if "weekday" in klass.__dict__:
            descriptor = klass.__dict__["weekday"]
            break
    assert isinstance(descriptor, property)

def test_timeinterval_has_classOrder():
    assert hasattr(TimeInterval, "classOrder")
    descriptor = None
    for klass in TimeInterval.__mro__:
        if "classOrder" in klass.__dict__:
            descriptor = klass.__dict__["classOrder"]
            break
    assert isinstance(descriptor, property)



def test_auditorium_is_not_abstract():
    assert not inspect.isabstract(Auditorium)


def test_auditorium_constructor_exists():
    assert callable(Auditorium.__init__)


def test_auditorium_constructor_args():
    sig = inspect.signature(Auditorium.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "educationalBuilding" in params, "Missing parameter 'educationalBuilding'"
    assert "is_busy" in params, "Missing parameter 'is_busy'"
    assert "auditoriumNumber" in params, "Missing parameter 'auditoriumNumber'"

def test_auditorium_has_id():
    assert hasattr(Auditorium, "id")
    descriptor = None
    for klass in Auditorium.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_auditorium_has_educationalBuilding():
    assert hasattr(Auditorium, "educationalBuilding")
    descriptor = None
    for klass in Auditorium.__mro__:
        if "educationalBuilding" in klass.__dict__:
            descriptor = klass.__dict__["educationalBuilding"]
            break
    assert isinstance(descriptor, property)

def test_auditorium_has_is_busy():
    assert hasattr(Auditorium, "is_busy")
    descriptor = None
    for klass in Auditorium.__mro__:
        if "is_busy" in klass.__dict__:
            descriptor = klass.__dict__["is_busy"]
            break
    assert isinstance(descriptor, property)

def test_auditorium_has_auditoriumNumber():
    assert hasattr(Auditorium, "auditoriumNumber")
    descriptor = None
    for klass in Auditorium.__mro__:
        if "auditoriumNumber" in klass.__dict__:
            descriptor = klass.__dict__["auditoriumNumber"]
            break
    assert isinstance(descriptor, property)



def test_users_is_not_abstract():
    assert not inspect.isabstract(Users)


def test_users_constructor_exists():
    assert callable(Users.__init__)


def test_users_constructor_args():
    sig = inspect.signature(Users.__init__)
    params = list(sig.parameters.keys())
    assert "residentBirthday" in params, "Missing parameter 'residentBirthday'"
    assert "universityStructureUnit" in params, "Missing parameter 'universityStructureUnit'"
    assert "residentPosition" in params, "Missing parameter 'residentPosition'"
    assert "residentSurname" in params, "Missing parameter 'residentSurname'"
    assert "residentName" in params, "Missing parameter 'residentName'"
    assert "registrationCertificateCode" in params, "Missing parameter 'registrationCertificateCode'"
    assert "residentPassword" in params, "Missing parameter 'residentPassword'"
    assert "residentUserType" in params, "Missing parameter 'residentUserType'"
    assert "residentPatronymic" in params, "Missing parameter 'residentPatronymic'"
    assert "residentDepartment" in params, "Missing parameter 'residentDepartment'"
    assert "residentEmail" in params, "Missing parameter 'residentEmail'"
    assert "individuadIdentificationCode" in params, "Missing parameter 'individuadIdentificationCode'"
    assert "id" in params, "Missing parameter 'id'"

def test_users_has_residentBirthday():
    assert hasattr(Users, "residentBirthday")
    descriptor = None
    for klass in Users.__mro__:
        if "residentBirthday" in klass.__dict__:
            descriptor = klass.__dict__["residentBirthday"]
            break
    assert isinstance(descriptor, property)

def test_users_has_universityStructureUnit():
    assert hasattr(Users, "universityStructureUnit")
    descriptor = None
    for klass in Users.__mro__:
        if "universityStructureUnit" in klass.__dict__:
            descriptor = klass.__dict__["universityStructureUnit"]
            break
    assert isinstance(descriptor, property)

def test_users_has_residentPosition():
    assert hasattr(Users, "residentPosition")
    descriptor = None
    for klass in Users.__mro__:
        if "residentPosition" in klass.__dict__:
            descriptor = klass.__dict__["residentPosition"]
            break
    assert isinstance(descriptor, property)

def test_users_has_residentSurname():
    assert hasattr(Users, "residentSurname")
    descriptor = None
    for klass in Users.__mro__:
        if "residentSurname" in klass.__dict__:
            descriptor = klass.__dict__["residentSurname"]
            break
    assert isinstance(descriptor, property)

def test_users_has_residentName():
    assert hasattr(Users, "residentName")
    descriptor = None
    for klass in Users.__mro__:
        if "residentName" in klass.__dict__:
            descriptor = klass.__dict__["residentName"]
            break
    assert isinstance(descriptor, property)

def test_users_has_registrationCertificateCode():
    assert hasattr(Users, "registrationCertificateCode")
    descriptor = None
    for klass in Users.__mro__:
        if "registrationCertificateCode" in klass.__dict__:
            descriptor = klass.__dict__["registrationCertificateCode"]
            break
    assert isinstance(descriptor, property)

def test_users_has_residentPassword():
    assert hasattr(Users, "residentPassword")
    descriptor = None
    for klass in Users.__mro__:
        if "residentPassword" in klass.__dict__:
            descriptor = klass.__dict__["residentPassword"]
            break
    assert isinstance(descriptor, property)

def test_users_has_residentUserType():
    assert hasattr(Users, "residentUserType")
    descriptor = None
    for klass in Users.__mro__:
        if "residentUserType" in klass.__dict__:
            descriptor = klass.__dict__["residentUserType"]
            break
    assert isinstance(descriptor, property)

def test_users_has_residentPatronymic():
    assert hasattr(Users, "residentPatronymic")
    descriptor = None
    for klass in Users.__mro__:
        if "residentPatronymic" in klass.__dict__:
            descriptor = klass.__dict__["residentPatronymic"]
            break
    assert isinstance(descriptor, property)

def test_users_has_residentDepartment():
    assert hasattr(Users, "residentDepartment")
    descriptor = None
    for klass in Users.__mro__:
        if "residentDepartment" in klass.__dict__:
            descriptor = klass.__dict__["residentDepartment"]
            break
    assert isinstance(descriptor, property)

def test_users_has_residentEmail():
    assert hasattr(Users, "residentEmail")
    descriptor = None
    for klass in Users.__mro__:
        if "residentEmail" in klass.__dict__:
            descriptor = klass.__dict__["residentEmail"]
            break
    assert isinstance(descriptor, property)

def test_users_has_individuadIdentificationCode():
    assert hasattr(Users, "individuadIdentificationCode")
    descriptor = None
    for klass in Users.__mro__:
        if "individuadIdentificationCode" in klass.__dict__:
            descriptor = klass.__dict__["individuadIdentificationCode"]
            break
    assert isinstance(descriptor, property)

def test_users_has_id():
    assert hasattr(Users, "id")
    descriptor = None
    for klass in Users.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
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
SubjectSheduleController_strategy = st.builds(
    SubjectSheduleController,
    auditoriumNumberService=
        st.integers(),
    groupNumberService=
        st.integers(),
    subjectCodeService=
        safe_text,
    individualIdentificationCodeService=
        st.integers(),
    dateService=
        safe_text,
    activityTypeCodeService=
        st.integers()
)
ActivityType_strategy = st.builds(
    ActivityType,
    activityTypeCode=
        st.integers(),
    id=
        st.integers(),
    subjectCode=
        st.integers(),
    activityTypeName=
        safe_text
)
Subject_strategy = st.builds(
    Subject,
    subjectName=
        safe_text,
    subjectCode=
        st.integers(),
    id=
        st.integers()
)
SubjectShedule_strategy = st.builds(
    SubjectShedule,
    individualIdentificationCode=
        st.integers(),
    auditoriumNumber=
        st.integers(),
    groupNumber=
        st.integers(),
    subjectCode=
        st.integers(),
    activityTypeCode=
        st.integers(),
    date=
        safe_text,
    id=
        st.integers()
)
DocumentStorage_strategy = st.builds(
    DocumentStorage,
    documentPath=
        safe_text,
    documentCode=
        st.integers(),
    id=
        st.integers(),
    is_exist=
        st.booleans()
)
TimeCreditForEducationalSemester_strategy = st.builds(
    TimeCreditForEducationalSemester,
    groupNumber=
        st.integers(),
    subjectCode=
        st.integers(),
    totalHours=
        st.integers(),
    activityTypeCode=
        st.integers(),
    id=
        st.integers()
)
EducationalPlan_strategy = st.builds(
    EducationalPlan,
    subjectCode=
        st.integers(),
    id=
        st.integers(),
    individualIdentificationCode=
        st.integers()
)
Specialty_strategy = st.builds(
    Specialty,
    specialtyCode=
        st.integers(),
    specialtyName=
        safe_text,
    id=
        st.integers(),
    subjectCode=
        st.integers()
)
Group_strategy = st.builds(
    Group,
    groupNumber=
        st.integers(),
    educationalYear=
        st.integers(),
    specialtyCode=
        st.integers(),
    id=
        st.integers()
)
TimeInterval_strategy = st.builds(
    TimeInterval,
    date=
        safe_text,
    weekIdentifier=
        st.integers(),
    id=
        st.integers(),
    weekday=
        st.integers(),
    classOrder=
        st.integers()
)
Auditorium_strategy = st.builds(
    Auditorium,
    id=
        st.integers(),
    educationalBuilding=
        safe_text,
    is_busy=
        st.booleans(),
    auditoriumNumber=
        st.integers()
)
Users_strategy = st.builds(
    Users,
    residentBirthday=
        safe_text,
    universityStructureUnit=
        safe_text,
    residentPosition=
        safe_text,
    residentSurname=
        safe_text,
    residentName=
        safe_text,
    registrationCertificateCode=
        st.integers(),
    residentPassword=
        safe_text,
    residentUserType=
        safe_text,
    residentPatronymic=
        safe_text,
    residentDepartment=
        safe_text,
    residentEmail=
        safe_text,
    individuadIdentificationCode=
        st.integers(),
    id=
        st.integers()
)

@given(instance=SubjectSheduleController_strategy)
@settings(max_examples=50)
def test_subjectshedulecontroller_instantiation(instance):
    assert isinstance(instance, SubjectSheduleController)



@given(instance=SubjectSheduleController_strategy)
def test_subjectshedulecontroller_auditoriumNumberService_setter(instance):
    original = instance.auditoriumNumberService
    instance.auditoriumNumberService = original
    assert instance.auditoriumNumberService == original



@given(instance=SubjectSheduleController_strategy)
def test_subjectshedulecontroller_groupNumberService_setter(instance):
    original = instance.groupNumberService
    instance.groupNumberService = original
    assert instance.groupNumberService == original



@given(instance=SubjectSheduleController_strategy)
def test_subjectshedulecontroller_subjectCodeService_setter(instance):
    original = instance.subjectCodeService
    instance.subjectCodeService = original
    assert instance.subjectCodeService == original



@given(instance=SubjectSheduleController_strategy)
def test_subjectshedulecontroller_individualIdentificationCodeService_setter(instance):
    original = instance.individualIdentificationCodeService
    instance.individualIdentificationCodeService = original
    assert instance.individualIdentificationCodeService == original



@given(instance=SubjectSheduleController_strategy)
def test_subjectshedulecontroller_dateService_setter(instance):
    original = instance.dateService
    instance.dateService = original
    assert instance.dateService == original



@given(instance=SubjectSheduleController_strategy)
def test_subjectshedulecontroller_activityTypeCodeService_setter(instance):
    original = instance.activityTypeCodeService
    instance.activityTypeCodeService = original
    assert instance.activityTypeCodeService == original

@given(instance=ActivityType_strategy)
@settings(max_examples=50)
def test_activitytype_instantiation(instance):
    assert isinstance(instance, ActivityType)



@given(instance=ActivityType_strategy)
def test_activitytype_activityTypeCode_setter(instance):
    original = instance.activityTypeCode
    instance.activityTypeCode = original
    assert instance.activityTypeCode == original



@given(instance=ActivityType_strategy)
def test_activitytype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=ActivityType_strategy)
def test_activitytype_subjectCode_setter(instance):
    original = instance.subjectCode
    instance.subjectCode = original
    assert instance.subjectCode == original



@given(instance=ActivityType_strategy)
def test_activitytype_activityTypeName_setter(instance):
    original = instance.activityTypeName
    instance.activityTypeName = original
    assert instance.activityTypeName == original

@given(instance=Subject_strategy)
@settings(max_examples=50)
def test_subject_instantiation(instance):
    assert isinstance(instance, Subject)



@given(instance=Subject_strategy)
def test_subject_subjectName_setter(instance):
    original = instance.subjectName
    instance.subjectName = original
    assert instance.subjectName == original



@given(instance=Subject_strategy)
def test_subject_subjectCode_setter(instance):
    original = instance.subjectCode
    instance.subjectCode = original
    assert instance.subjectCode == original



@given(instance=Subject_strategy)
def test_subject_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=SubjectShedule_strategy)
@settings(max_examples=50)
def test_subjectshedule_instantiation(instance):
    assert isinstance(instance, SubjectShedule)



@given(instance=SubjectShedule_strategy)
def test_subjectshedule_individualIdentificationCode_setter(instance):
    original = instance.individualIdentificationCode
    instance.individualIdentificationCode = original
    assert instance.individualIdentificationCode == original



@given(instance=SubjectShedule_strategy)
def test_subjectshedule_auditoriumNumber_setter(instance):
    original = instance.auditoriumNumber
    instance.auditoriumNumber = original
    assert instance.auditoriumNumber == original



@given(instance=SubjectShedule_strategy)
def test_subjectshedule_groupNumber_setter(instance):
    original = instance.groupNumber
    instance.groupNumber = original
    assert instance.groupNumber == original



@given(instance=SubjectShedule_strategy)
def test_subjectshedule_subjectCode_setter(instance):
    original = instance.subjectCode
    instance.subjectCode = original
    assert instance.subjectCode == original



@given(instance=SubjectShedule_strategy)
def test_subjectshedule_activityTypeCode_setter(instance):
    original = instance.activityTypeCode
    instance.activityTypeCode = original
    assert instance.activityTypeCode == original



@given(instance=SubjectShedule_strategy)
def test_subjectshedule_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original



@given(instance=SubjectShedule_strategy)
def test_subjectshedule_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=DocumentStorage_strategy)
@settings(max_examples=50)
def test_documentstorage_instantiation(instance):
    assert isinstance(instance, DocumentStorage)



@given(instance=DocumentStorage_strategy)
def test_documentstorage_documentPath_setter(instance):
    original = instance.documentPath
    instance.documentPath = original
    assert instance.documentPath == original



@given(instance=DocumentStorage_strategy)
def test_documentstorage_documentCode_setter(instance):
    original = instance.documentCode
    instance.documentCode = original
    assert instance.documentCode == original



@given(instance=DocumentStorage_strategy)
def test_documentstorage_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=DocumentStorage_strategy)
def test_documentstorage_is_exist_setter(instance):
    original = instance.is_exist
    instance.is_exist = original
    assert instance.is_exist == original

@given(instance=TimeCreditForEducationalSemester_strategy)
@settings(max_examples=50)
def test_timecreditforeducationalsemester_instantiation(instance):
    assert isinstance(instance, TimeCreditForEducationalSemester)



@given(instance=TimeCreditForEducationalSemester_strategy)
def test_timecreditforeducationalsemester_groupNumber_setter(instance):
    original = instance.groupNumber
    instance.groupNumber = original
    assert instance.groupNumber == original



@given(instance=TimeCreditForEducationalSemester_strategy)
def test_timecreditforeducationalsemester_subjectCode_setter(instance):
    original = instance.subjectCode
    instance.subjectCode = original
    assert instance.subjectCode == original



@given(instance=TimeCreditForEducationalSemester_strategy)
def test_timecreditforeducationalsemester_totalHours_setter(instance):
    original = instance.totalHours
    instance.totalHours = original
    assert instance.totalHours == original



@given(instance=TimeCreditForEducationalSemester_strategy)
def test_timecreditforeducationalsemester_activityTypeCode_setter(instance):
    original = instance.activityTypeCode
    instance.activityTypeCode = original
    assert instance.activityTypeCode == original



@given(instance=TimeCreditForEducationalSemester_strategy)
def test_timecreditforeducationalsemester_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=EducationalPlan_strategy)
@settings(max_examples=50)
def test_educationalplan_instantiation(instance):
    assert isinstance(instance, EducationalPlan)



@given(instance=EducationalPlan_strategy)
def test_educationalplan_subjectCode_setter(instance):
    original = instance.subjectCode
    instance.subjectCode = original
    assert instance.subjectCode == original



@given(instance=EducationalPlan_strategy)
def test_educationalplan_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=EducationalPlan_strategy)
def test_educationalplan_individualIdentificationCode_setter(instance):
    original = instance.individualIdentificationCode
    instance.individualIdentificationCode = original
    assert instance.individualIdentificationCode == original

@given(instance=Specialty_strategy)
@settings(max_examples=50)
def test_specialty_instantiation(instance):
    assert isinstance(instance, Specialty)



@given(instance=Specialty_strategy)
def test_specialty_specialtyCode_setter(instance):
    original = instance.specialtyCode
    instance.specialtyCode = original
    assert instance.specialtyCode == original



@given(instance=Specialty_strategy)
def test_specialty_specialtyName_setter(instance):
    original = instance.specialtyName
    instance.specialtyName = original
    assert instance.specialtyName == original



@given(instance=Specialty_strategy)
def test_specialty_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Specialty_strategy)
def test_specialty_subjectCode_setter(instance):
    original = instance.subjectCode
    instance.subjectCode = original
    assert instance.subjectCode == original

@given(instance=Group_strategy)
@settings(max_examples=50)
def test_group_instantiation(instance):
    assert isinstance(instance, Group)



@given(instance=Group_strategy)
def test_group_groupNumber_setter(instance):
    original = instance.groupNumber
    instance.groupNumber = original
    assert instance.groupNumber == original



@given(instance=Group_strategy)
def test_group_educationalYear_setter(instance):
    original = instance.educationalYear
    instance.educationalYear = original
    assert instance.educationalYear == original



@given(instance=Group_strategy)
def test_group_specialtyCode_setter(instance):
    original = instance.specialtyCode
    instance.specialtyCode = original
    assert instance.specialtyCode == original



@given(instance=Group_strategy)
def test_group_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=TimeInterval_strategy)
@settings(max_examples=50)
def test_timeinterval_instantiation(instance):
    assert isinstance(instance, TimeInterval)



@given(instance=TimeInterval_strategy)
def test_timeinterval_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original



@given(instance=TimeInterval_strategy)
def test_timeinterval_weekIdentifier_setter(instance):
    original = instance.weekIdentifier
    instance.weekIdentifier = original
    assert instance.weekIdentifier == original



@given(instance=TimeInterval_strategy)
def test_timeinterval_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=TimeInterval_strategy)
def test_timeinterval_weekday_setter(instance):
    original = instance.weekday
    instance.weekday = original
    assert instance.weekday == original



@given(instance=TimeInterval_strategy)
def test_timeinterval_classOrder_setter(instance):
    original = instance.classOrder
    instance.classOrder = original
    assert instance.classOrder == original

@given(instance=Auditorium_strategy)
@settings(max_examples=50)
def test_auditorium_instantiation(instance):
    assert isinstance(instance, Auditorium)



@given(instance=Auditorium_strategy)
def test_auditorium_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Auditorium_strategy)
def test_auditorium_educationalBuilding_setter(instance):
    original = instance.educationalBuilding
    instance.educationalBuilding = original
    assert instance.educationalBuilding == original



@given(instance=Auditorium_strategy)
def test_auditorium_is_busy_setter(instance):
    original = instance.is_busy
    instance.is_busy = original
    assert instance.is_busy == original



@given(instance=Auditorium_strategy)
def test_auditorium_auditoriumNumber_setter(instance):
    original = instance.auditoriumNumber
    instance.auditoriumNumber = original
    assert instance.auditoriumNumber == original

@given(instance=Users_strategy)
@settings(max_examples=50)
def test_users_instantiation(instance):
    assert isinstance(instance, Users)



@given(instance=Users_strategy)
def test_users_residentBirthday_setter(instance):
    original = instance.residentBirthday
    instance.residentBirthday = original
    assert instance.residentBirthday == original



@given(instance=Users_strategy)
def test_users_universityStructureUnit_setter(instance):
    original = instance.universityStructureUnit
    instance.universityStructureUnit = original
    assert instance.universityStructureUnit == original



@given(instance=Users_strategy)
def test_users_residentPosition_setter(instance):
    original = instance.residentPosition
    instance.residentPosition = original
    assert instance.residentPosition == original



@given(instance=Users_strategy)
def test_users_residentSurname_setter(instance):
    original = instance.residentSurname
    instance.residentSurname = original
    assert instance.residentSurname == original



@given(instance=Users_strategy)
def test_users_residentName_setter(instance):
    original = instance.residentName
    instance.residentName = original
    assert instance.residentName == original



@given(instance=Users_strategy)
def test_users_registrationCertificateCode_setter(instance):
    original = instance.registrationCertificateCode
    instance.registrationCertificateCode = original
    assert instance.registrationCertificateCode == original



@given(instance=Users_strategy)
def test_users_residentPassword_setter(instance):
    original = instance.residentPassword
    instance.residentPassword = original
    assert instance.residentPassword == original



@given(instance=Users_strategy)
def test_users_residentUserType_setter(instance):
    original = instance.residentUserType
    instance.residentUserType = original
    assert instance.residentUserType == original



@given(instance=Users_strategy)
def test_users_residentPatronymic_setter(instance):
    original = instance.residentPatronymic
    instance.residentPatronymic = original
    assert instance.residentPatronymic == original



@given(instance=Users_strategy)
def test_users_residentDepartment_setter(instance):
    original = instance.residentDepartment
    instance.residentDepartment = original
    assert instance.residentDepartment == original



@given(instance=Users_strategy)
def test_users_residentEmail_setter(instance):
    original = instance.residentEmail
    instance.residentEmail = original
    assert instance.residentEmail == original



@given(instance=Users_strategy)
def test_users_individuadIdentificationCode_setter(instance):
    original = instance.individuadIdentificationCode
    instance.individuadIdentificationCode = original
    assert instance.individuadIdentificationCode == original



@given(instance=Users_strategy)
def test_users_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original
