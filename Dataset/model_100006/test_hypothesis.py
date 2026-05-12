import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Topic,
    SWRC::ResearchTopic,
    SWRC::Topic,
    SWRC::Product,
    ProjectReport,
    Department,
    SWRC::Project,
    Institute,
    Product,
    SWRC::SoftwareComponent,
    TechnicalReport,
    SWRC::Organization,
    Graduate,
    SWRC::PhDStudent,
    Student,
    SWRC::Graduate,
    SWRC::Undergraduate,
    FacultyMember,
    SWRC::AssociateProfessor,
    SWRC::AssistantProfessor,
    SWRC::FullProfessor,
    ResearchTopic,
    PhDStudent,
    ResearchGroup,
    Employee,
    SWRC::TechnicalStaff,
    SWRC::AdministrativeStaff,
    SWRC::Manager,
    AcademicStaff,
    SWRC::Lecturer,
    SWRC::FacultyMember,
    SWRC::Person,
    Meeting,
    SWRC::ProjectMeeting,
    Event,
    SWRC::Exhibition,
    SWRC::Workshop,
    SWRC::Meeting,
    SWRC::Lecture,
    SWRC::Conference,
    SWRC::Event,
    Project,
    SWRC::DevelopmentProject,
    SWRC::ResearchProject,
    SWRC::SoftwareProject,
    Report,
    SWRC::TechnicalReport,
    SWRC::ProjectReport,
    Thesis,
    SWRC::PhDThesis,
    SWRC::MasterThesis,
    University,
    Organization,
    SWRC::Enterprise,
    SWRC::University,
    SWRC::Department,
    SWRC::Association,
    SWRC::ResearchGroup,
    SWRC::Institute,
    Person,
    SWRC::AcademicStaff,
    SWRC::Student,
    SWRC::Employee,
    Publication,
    SWRC::Manual,
    SWRC::Thesis,
    SWRC::Booklet,
    SWRC::Proceedings,
    SWRC::InProceedings,
    SWRC::Book,
    SWRC::InCollection,
    SWRC::InBook,
    SWRC::Unpublished,
    SWRC::Misc,
    SWRC::Report,
    SWRC::Article,
    SWRC::Publication,
    SWRC::Bibliography,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_topic_is_not_abstract():
    assert not inspect.isabstract(Topic)


def test_topic_constructor_exists():
    assert callable(Topic.__init__)


def test_topic_constructor_args():
    sig = inspect.signature(Topic.__init__)
    params = list(sig.parameters.keys())



def test_swrc::researchtopic_is_not_abstract():
    assert not inspect.isabstract(SWRC::ResearchTopic)


def test_swrc::researchtopic_constructor_exists():
    assert callable(SWRC::ResearchTopic.__init__)


def test_swrc::researchtopic_constructor_args():
    sig = inspect.signature(SWRC::ResearchTopic.__init__)
    params = list(sig.parameters.keys())



def test_swrc::topic_is_not_abstract():
    assert not inspect.isabstract(SWRC::Topic)


def test_swrc::topic_constructor_exists():
    assert callable(SWRC::Topic.__init__)


def test_swrc::topic_constructor_args():
    sig = inspect.signature(SWRC::Topic.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_swrc::topic_has_name():
    assert hasattr(SWRC::Topic, "name")
    descriptor = None
    for klass in SWRC::Topic.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_swrc::product_is_not_abstract():
    assert not inspect.isabstract(SWRC::Product)


def test_swrc::product_constructor_exists():
    assert callable(SWRC::Product.__init__)


def test_swrc::product_constructor_args():
    sig = inspect.signature(SWRC::Product.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_swrc::product_has_name():
    assert hasattr(SWRC::Product, "name")
    descriptor = None
    for klass in SWRC::Product.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_projectreport_is_not_abstract():
    assert not inspect.isabstract(ProjectReport)


def test_projectreport_constructor_exists():
    assert callable(ProjectReport.__init__)


def test_projectreport_constructor_args():
    sig = inspect.signature(ProjectReport.__init__)
    params = list(sig.parameters.keys())



def test_department_is_not_abstract():
    assert not inspect.isabstract(Department)


def test_department_constructor_exists():
    assert callable(Department.__init__)


def test_department_constructor_args():
    sig = inspect.signature(Department.__init__)
    params = list(sig.parameters.keys())



def test_swrc::project_is_not_abstract():
    assert not inspect.isabstract(SWRC::Project)


def test_swrc::project_constructor_exists():
    assert callable(SWRC::Project.__init__)


def test_swrc::project_constructor_args():
    sig = inspect.signature(SWRC::Project.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_swrc::project_has_name():
    assert hasattr(SWRC::Project, "name")
    descriptor = None
    for klass in SWRC::Project.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_institute_is_not_abstract():
    assert not inspect.isabstract(Institute)


def test_institute_constructor_exists():
    assert callable(Institute.__init__)


def test_institute_constructor_args():
    sig = inspect.signature(Institute.__init__)
    params = list(sig.parameters.keys())



def test_product_is_not_abstract():
    assert not inspect.isabstract(Product)


def test_product_constructor_exists():
    assert callable(Product.__init__)


def test_product_constructor_args():
    sig = inspect.signature(Product.__init__)
    params = list(sig.parameters.keys())



def test_swrc::softwarecomponent_is_not_abstract():
    assert not inspect.isabstract(SWRC::SoftwareComponent)


def test_swrc::softwarecomponent_constructor_exists():
    assert callable(SWRC::SoftwareComponent.__init__)


def test_swrc::softwarecomponent_constructor_args():
    sig = inspect.signature(SWRC::SoftwareComponent.__init__)
    params = list(sig.parameters.keys())
    assert "hasPrice" in params, "Missing parameter 'hasPrice'"

def test_swrc::softwarecomponent_has_hasPrice():
    assert hasattr(SWRC::SoftwareComponent, "hasPrice")
    descriptor = None
    for klass in SWRC::SoftwareComponent.__mro__:
        if "hasPrice" in klass.__dict__:
            descriptor = klass.__dict__["hasPrice"]
            break
    assert isinstance(descriptor, property)



def test_technicalreport_is_not_abstract():
    assert not inspect.isabstract(TechnicalReport)


def test_technicalreport_constructor_exists():
    assert callable(TechnicalReport.__init__)


def test_technicalreport_constructor_args():
    sig = inspect.signature(TechnicalReport.__init__)
    params = list(sig.parameters.keys())



def test_swrc::organization_is_not_abstract():
    assert not inspect.isabstract(SWRC::Organization)


def test_swrc::organization_constructor_exists():
    assert callable(SWRC::Organization.__init__)


def test_swrc::organization_constructor_args():
    sig = inspect.signature(SWRC::Organization.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "location" in params, "Missing parameter 'location'"

def test_swrc::organization_has_name():
    assert hasattr(SWRC::Organization, "name")
    descriptor = None
    for klass in SWRC::Organization.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_swrc::organization_has_location():
    assert hasattr(SWRC::Organization, "location")
    descriptor = None
    for klass in SWRC::Organization.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)



def test_graduate_is_not_abstract():
    assert not inspect.isabstract(Graduate)


def test_graduate_constructor_exists():
    assert callable(Graduate.__init__)


def test_graduate_constructor_args():
    sig = inspect.signature(Graduate.__init__)
    params = list(sig.parameters.keys())



def test_swrc::phdstudent_is_not_abstract():
    assert not inspect.isabstract(SWRC::PhDStudent)


def test_swrc::phdstudent_constructor_exists():
    assert callable(SWRC::PhDStudent.__init__)


def test_swrc::phdstudent_constructor_args():
    sig = inspect.signature(SWRC::PhDStudent.__init__)
    params = list(sig.parameters.keys())



def test_student_is_not_abstract():
    assert not inspect.isabstract(Student)


def test_student_constructor_exists():
    assert callable(Student.__init__)


def test_student_constructor_args():
    sig = inspect.signature(Student.__init__)
    params = list(sig.parameters.keys())



def test_swrc::graduate_is_not_abstract():
    assert not inspect.isabstract(SWRC::Graduate)


def test_swrc::graduate_constructor_exists():
    assert callable(SWRC::Graduate.__init__)


def test_swrc::graduate_constructor_args():
    sig = inspect.signature(SWRC::Graduate.__init__)
    params = list(sig.parameters.keys())



def test_swrc::undergraduate_is_not_abstract():
    assert not inspect.isabstract(SWRC::Undergraduate)


def test_swrc::undergraduate_constructor_exists():
    assert callable(SWRC::Undergraduate.__init__)


def test_swrc::undergraduate_constructor_args():
    sig = inspect.signature(SWRC::Undergraduate.__init__)
    params = list(sig.parameters.keys())



def test_facultymember_is_not_abstract():
    assert not inspect.isabstract(FacultyMember)


def test_facultymember_constructor_exists():
    assert callable(FacultyMember.__init__)


def test_facultymember_constructor_args():
    sig = inspect.signature(FacultyMember.__init__)
    params = list(sig.parameters.keys())



def test_swrc::associateprofessor_is_not_abstract():
    assert not inspect.isabstract(SWRC::AssociateProfessor)


def test_swrc::associateprofessor_constructor_exists():
    assert callable(SWRC::AssociateProfessor.__init__)


def test_swrc::associateprofessor_constructor_args():
    sig = inspect.signature(SWRC::AssociateProfessor.__init__)
    params = list(sig.parameters.keys())



def test_swrc::assistantprofessor_is_not_abstract():
    assert not inspect.isabstract(SWRC::AssistantProfessor)


def test_swrc::assistantprofessor_constructor_exists():
    assert callable(SWRC::AssistantProfessor.__init__)


def test_swrc::assistantprofessor_constructor_args():
    sig = inspect.signature(SWRC::AssistantProfessor.__init__)
    params = list(sig.parameters.keys())



def test_swrc::fullprofessor_is_not_abstract():
    assert not inspect.isabstract(SWRC::FullProfessor)


def test_swrc::fullprofessor_constructor_exists():
    assert callable(SWRC::FullProfessor.__init__)


def test_swrc::fullprofessor_constructor_args():
    sig = inspect.signature(SWRC::FullProfessor.__init__)
    params = list(sig.parameters.keys())



def test_researchtopic_is_not_abstract():
    assert not inspect.isabstract(ResearchTopic)


def test_researchtopic_constructor_exists():
    assert callable(ResearchTopic.__init__)


def test_researchtopic_constructor_args():
    sig = inspect.signature(ResearchTopic.__init__)
    params = list(sig.parameters.keys())



def test_phdstudent_is_not_abstract():
    assert not inspect.isabstract(PhDStudent)


def test_phdstudent_constructor_exists():
    assert callable(PhDStudent.__init__)


def test_phdstudent_constructor_args():
    sig = inspect.signature(PhDStudent.__init__)
    params = list(sig.parameters.keys())



def test_researchgroup_is_not_abstract():
    assert not inspect.isabstract(ResearchGroup)


def test_researchgroup_constructor_exists():
    assert callable(ResearchGroup.__init__)


def test_researchgroup_constructor_args():
    sig = inspect.signature(ResearchGroup.__init__)
    params = list(sig.parameters.keys())



def test_employee_is_not_abstract():
    assert not inspect.isabstract(Employee)


def test_employee_constructor_exists():
    assert callable(Employee.__init__)


def test_employee_constructor_args():
    sig = inspect.signature(Employee.__init__)
    params = list(sig.parameters.keys())



def test_swrc::technicalstaff_is_not_abstract():
    assert not inspect.isabstract(SWRC::TechnicalStaff)


def test_swrc::technicalstaff_constructor_exists():
    assert callable(SWRC::TechnicalStaff.__init__)


def test_swrc::technicalstaff_constructor_args():
    sig = inspect.signature(SWRC::TechnicalStaff.__init__)
    params = list(sig.parameters.keys())



def test_swrc::administrativestaff_is_not_abstract():
    assert not inspect.isabstract(SWRC::AdministrativeStaff)


def test_swrc::administrativestaff_constructor_exists():
    assert callable(SWRC::AdministrativeStaff.__init__)


def test_swrc::administrativestaff_constructor_args():
    sig = inspect.signature(SWRC::AdministrativeStaff.__init__)
    params = list(sig.parameters.keys())



def test_swrc::manager_is_not_abstract():
    assert not inspect.isabstract(SWRC::Manager)


def test_swrc::manager_constructor_exists():
    assert callable(SWRC::Manager.__init__)


def test_swrc::manager_constructor_args():
    sig = inspect.signature(SWRC::Manager.__init__)
    params = list(sig.parameters.keys())



def test_academicstaff_is_not_abstract():
    assert not inspect.isabstract(AcademicStaff)


def test_academicstaff_constructor_exists():
    assert callable(AcademicStaff.__init__)


def test_academicstaff_constructor_args():
    sig = inspect.signature(AcademicStaff.__init__)
    params = list(sig.parameters.keys())



def test_swrc::lecturer_is_not_abstract():
    assert not inspect.isabstract(SWRC::Lecturer)


def test_swrc::lecturer_constructor_exists():
    assert callable(SWRC::Lecturer.__init__)


def test_swrc::lecturer_constructor_args():
    sig = inspect.signature(SWRC::Lecturer.__init__)
    params = list(sig.parameters.keys())



def test_swrc::facultymember_is_not_abstract():
    assert not inspect.isabstract(SWRC::FacultyMember)


def test_swrc::facultymember_constructor_exists():
    assert callable(SWRC::FacultyMember.__init__)


def test_swrc::facultymember_constructor_args():
    sig = inspect.signature(SWRC::FacultyMember.__init__)
    params = list(sig.parameters.keys())



def test_swrc::person_is_not_abstract():
    assert not inspect.isabstract(SWRC::Person)


def test_swrc::person_constructor_exists():
    assert callable(SWRC::Person.__init__)


def test_swrc::person_constructor_args():
    sig = inspect.signature(SWRC::Person.__init__)
    params = list(sig.parameters.keys())
    assert "phone" in params, "Missing parameter 'phone'"
    assert "photo" in params, "Missing parameter 'photo'"
    assert "homepage" in params, "Missing parameter 'homepage'"
    assert "fax" in params, "Missing parameter 'fax'"
    assert "email" in params, "Missing parameter 'email'"
    assert "address" in params, "Missing parameter 'address'"
    assert "name" in params, "Missing parameter 'name'"

def test_swrc::person_has_phone():
    assert hasattr(SWRC::Person, "phone")
    descriptor = None
    for klass in SWRC::Person.__mro__:
        if "phone" in klass.__dict__:
            descriptor = klass.__dict__["phone"]
            break
    assert isinstance(descriptor, property)

def test_swrc::person_has_photo():
    assert hasattr(SWRC::Person, "photo")
    descriptor = None
    for klass in SWRC::Person.__mro__:
        if "photo" in klass.__dict__:
            descriptor = klass.__dict__["photo"]
            break
    assert isinstance(descriptor, property)

def test_swrc::person_has_homepage():
    assert hasattr(SWRC::Person, "homepage")
    descriptor = None
    for klass in SWRC::Person.__mro__:
        if "homepage" in klass.__dict__:
            descriptor = klass.__dict__["homepage"]
            break
    assert isinstance(descriptor, property)

def test_swrc::person_has_fax():
    assert hasattr(SWRC::Person, "fax")
    descriptor = None
    for klass in SWRC::Person.__mro__:
        if "fax" in klass.__dict__:
            descriptor = klass.__dict__["fax"]
            break
    assert isinstance(descriptor, property)

def test_swrc::person_has_email():
    assert hasattr(SWRC::Person, "email")
    descriptor = None
    for klass in SWRC::Person.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)

def test_swrc::person_has_address():
    assert hasattr(SWRC::Person, "address")
    descriptor = None
    for klass in SWRC::Person.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)

def test_swrc::person_has_name():
    assert hasattr(SWRC::Person, "name")
    descriptor = None
    for klass in SWRC::Person.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_meeting_is_not_abstract():
    assert not inspect.isabstract(Meeting)


def test_meeting_constructor_exists():
    assert callable(Meeting.__init__)


def test_meeting_constructor_args():
    sig = inspect.signature(Meeting.__init__)
    params = list(sig.parameters.keys())



def test_swrc::projectmeeting_is_not_abstract():
    assert not inspect.isabstract(SWRC::ProjectMeeting)


def test_swrc::projectmeeting_constructor_exists():
    assert callable(SWRC::ProjectMeeting.__init__)


def test_swrc::projectmeeting_constructor_args():
    sig = inspect.signature(SWRC::ProjectMeeting.__init__)
    params = list(sig.parameters.keys())



def test_event_is_not_abstract():
    assert not inspect.isabstract(Event)


def test_event_constructor_exists():
    assert callable(Event.__init__)


def test_event_constructor_args():
    sig = inspect.signature(Event.__init__)
    params = list(sig.parameters.keys())



def test_swrc::exhibition_is_not_abstract():
    assert not inspect.isabstract(SWRC::Exhibition)


def test_swrc::exhibition_constructor_exists():
    assert callable(SWRC::Exhibition.__init__)


def test_swrc::exhibition_constructor_args():
    sig = inspect.signature(SWRC::Exhibition.__init__)
    params = list(sig.parameters.keys())



def test_swrc::workshop_is_not_abstract():
    assert not inspect.isabstract(SWRC::Workshop)


def test_swrc::workshop_constructor_exists():
    assert callable(SWRC::Workshop.__init__)


def test_swrc::workshop_constructor_args():
    sig = inspect.signature(SWRC::Workshop.__init__)
    params = list(sig.parameters.keys())
    assert "series" in params, "Missing parameter 'series'"

def test_swrc::workshop_has_series():
    assert hasattr(SWRC::Workshop, "series")
    descriptor = None
    for klass in SWRC::Workshop.__mro__:
        if "series" in klass.__dict__:
            descriptor = klass.__dict__["series"]
            break
    assert isinstance(descriptor, property)



def test_swrc::meeting_is_not_abstract():
    assert not inspect.isabstract(SWRC::Meeting)


def test_swrc::meeting_constructor_exists():
    assert callable(SWRC::Meeting.__init__)


def test_swrc::meeting_constructor_args():
    sig = inspect.signature(SWRC::Meeting.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"

def test_swrc::meeting_has_title():
    assert hasattr(SWRC::Meeting, "title")
    descriptor = None
    for klass in SWRC::Meeting.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_swrc::lecture_is_not_abstract():
    assert not inspect.isabstract(SWRC::Lecture)


def test_swrc::lecture_constructor_exists():
    assert callable(SWRC::Lecture.__init__)


def test_swrc::lecture_constructor_args():
    sig = inspect.signature(SWRC::Lecture.__init__)
    params = list(sig.parameters.keys())



def test_swrc::conference_is_not_abstract():
    assert not inspect.isabstract(SWRC::Conference)


def test_swrc::conference_constructor_exists():
    assert callable(SWRC::Conference.__init__)


def test_swrc::conference_constructor_args():
    sig = inspect.signature(SWRC::Conference.__init__)
    params = list(sig.parameters.keys())
    assert "series" in params, "Missing parameter 'series'"

def test_swrc::conference_has_series():
    assert hasattr(SWRC::Conference, "series")
    descriptor = None
    for klass in SWRC::Conference.__mro__:
        if "series" in klass.__dict__:
            descriptor = klass.__dict__["series"]
            break
    assert isinstance(descriptor, property)



def test_swrc::event_is_not_abstract():
    assert not inspect.isabstract(SWRC::Event)


def test_swrc::event_constructor_exists():
    assert callable(SWRC::Event.__init__)


def test_swrc::event_constructor_args():
    sig = inspect.signature(SWRC::Event.__init__)
    params = list(sig.parameters.keys())
    assert "date" in params, "Missing parameter 'date'"
    assert "name" in params, "Missing parameter 'name'"
    assert "eventTitle" in params, "Missing parameter 'eventTitle'"
    assert "location" in params, "Missing parameter 'location'"

def test_swrc::event_has_date():
    assert hasattr(SWRC::Event, "date")
    descriptor = None
    for klass in SWRC::Event.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)

def test_swrc::event_has_name():
    assert hasattr(SWRC::Event, "name")
    descriptor = None
    for klass in SWRC::Event.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_swrc::event_has_eventTitle():
    assert hasattr(SWRC::Event, "eventTitle")
    descriptor = None
    for klass in SWRC::Event.__mro__:
        if "eventTitle" in klass.__dict__:
            descriptor = klass.__dict__["eventTitle"]
            break
    assert isinstance(descriptor, property)

def test_swrc::event_has_location():
    assert hasattr(SWRC::Event, "location")
    descriptor = None
    for klass in SWRC::Event.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)



def test_project_is_not_abstract():
    assert not inspect.isabstract(Project)


def test_project_constructor_exists():
    assert callable(Project.__init__)


def test_project_constructor_args():
    sig = inspect.signature(Project.__init__)
    params = list(sig.parameters.keys())



def test_swrc::developmentproject_is_not_abstract():
    assert not inspect.isabstract(SWRC::DevelopmentProject)


def test_swrc::developmentproject_constructor_exists():
    assert callable(SWRC::DevelopmentProject.__init__)


def test_swrc::developmentproject_constructor_args():
    sig = inspect.signature(SWRC::DevelopmentProject.__init__)
    params = list(sig.parameters.keys())



def test_swrc::researchproject_is_not_abstract():
    assert not inspect.isabstract(SWRC::ResearchProject)


def test_swrc::researchproject_constructor_exists():
    assert callable(SWRC::ResearchProject.__init__)


def test_swrc::researchproject_constructor_args():
    sig = inspect.signature(SWRC::ResearchProject.__init__)
    params = list(sig.parameters.keys())



def test_swrc::softwareproject_is_not_abstract():
    assert not inspect.isabstract(SWRC::SoftwareProject)


def test_swrc::softwareproject_constructor_exists():
    assert callable(SWRC::SoftwareProject.__init__)


def test_swrc::softwareproject_constructor_args():
    sig = inspect.signature(SWRC::SoftwareProject.__init__)
    params = list(sig.parameters.keys())



def test_report_is_not_abstract():
    assert not inspect.isabstract(Report)


def test_report_constructor_exists():
    assert callable(Report.__init__)


def test_report_constructor_args():
    sig = inspect.signature(Report.__init__)
    params = list(sig.parameters.keys())



def test_swrc::technicalreport_is_not_abstract():
    assert not inspect.isabstract(SWRC::TechnicalReport)


def test_swrc::technicalreport_constructor_exists():
    assert callable(SWRC::TechnicalReport.__init__)


def test_swrc::technicalreport_constructor_args():
    sig = inspect.signature(SWRC::TechnicalReport.__init__)
    params = list(sig.parameters.keys())
    assert "series" in params, "Missing parameter 'series'"

def test_swrc::technicalreport_has_series():
    assert hasattr(SWRC::TechnicalReport, "series")
    descriptor = None
    for klass in SWRC::TechnicalReport.__mro__:
        if "series" in klass.__dict__:
            descriptor = klass.__dict__["series"]
            break
    assert isinstance(descriptor, property)



def test_swrc::projectreport_is_not_abstract():
    assert not inspect.isabstract(SWRC::ProjectReport)


def test_swrc::projectreport_constructor_exists():
    assert callable(SWRC::ProjectReport.__init__)


def test_swrc::projectreport_constructor_args():
    sig = inspect.signature(SWRC::ProjectReport.__init__)
    params = list(sig.parameters.keys())



def test_thesis_is_not_abstract():
    assert not inspect.isabstract(Thesis)


def test_thesis_constructor_exists():
    assert callable(Thesis.__init__)


def test_thesis_constructor_args():
    sig = inspect.signature(Thesis.__init__)
    params = list(sig.parameters.keys())



def test_swrc::phdthesis_is_not_abstract():
    assert not inspect.isabstract(SWRC::PhDThesis)


def test_swrc::phdthesis_constructor_exists():
    assert callable(SWRC::PhDThesis.__init__)


def test_swrc::phdthesis_constructor_args():
    sig = inspect.signature(SWRC::PhDThesis.__init__)
    params = list(sig.parameters.keys())



def test_swrc::masterthesis_is_not_abstract():
    assert not inspect.isabstract(SWRC::MasterThesis)


def test_swrc::masterthesis_constructor_exists():
    assert callable(SWRC::MasterThesis.__init__)


def test_swrc::masterthesis_constructor_args():
    sig = inspect.signature(SWRC::MasterThesis.__init__)
    params = list(sig.parameters.keys())



def test_university_is_not_abstract():
    assert not inspect.isabstract(University)


def test_university_constructor_exists():
    assert callable(University.__init__)


def test_university_constructor_args():
    sig = inspect.signature(University.__init__)
    params = list(sig.parameters.keys())



def test_organization_is_not_abstract():
    assert not inspect.isabstract(Organization)


def test_organization_constructor_exists():
    assert callable(Organization.__init__)


def test_organization_constructor_args():
    sig = inspect.signature(Organization.__init__)
    params = list(sig.parameters.keys())



def test_swrc::enterprise_is_not_abstract():
    assert not inspect.isabstract(SWRC::Enterprise)


def test_swrc::enterprise_constructor_exists():
    assert callable(SWRC::Enterprise.__init__)


def test_swrc::enterprise_constructor_args():
    sig = inspect.signature(SWRC::Enterprise.__init__)
    params = list(sig.parameters.keys())



def test_swrc::university_is_not_abstract():
    assert not inspect.isabstract(SWRC::University)


def test_swrc::university_constructor_exists():
    assert callable(SWRC::University.__init__)


def test_swrc::university_constructor_args():
    sig = inspect.signature(SWRC::University.__init__)
    params = list(sig.parameters.keys())



def test_swrc::department_is_not_abstract():
    assert not inspect.isabstract(SWRC::Department)


def test_swrc::department_constructor_exists():
    assert callable(SWRC::Department.__init__)


def test_swrc::department_constructor_args():
    sig = inspect.signature(SWRC::Department.__init__)
    params = list(sig.parameters.keys())



def test_swrc::association_is_not_abstract():
    assert not inspect.isabstract(SWRC::Association)


def test_swrc::association_constructor_exists():
    assert callable(SWRC::Association.__init__)


def test_swrc::association_constructor_args():
    sig = inspect.signature(SWRC::Association.__init__)
    params = list(sig.parameters.keys())



def test_swrc::researchgroup_is_not_abstract():
    assert not inspect.isabstract(SWRC::ResearchGroup)


def test_swrc::researchgroup_constructor_exists():
    assert callable(SWRC::ResearchGroup.__init__)


def test_swrc::researchgroup_constructor_args():
    sig = inspect.signature(SWRC::ResearchGroup.__init__)
    params = list(sig.parameters.keys())



def test_swrc::institute_is_not_abstract():
    assert not inspect.isabstract(SWRC::Institute)


def test_swrc::institute_constructor_exists():
    assert callable(SWRC::Institute.__init__)


def test_swrc::institute_constructor_args():
    sig = inspect.signature(SWRC::Institute.__init__)
    params = list(sig.parameters.keys())



def test_person_is_not_abstract():
    assert not inspect.isabstract(Person)


def test_person_constructor_exists():
    assert callable(Person.__init__)


def test_person_constructor_args():
    sig = inspect.signature(Person.__init__)
    params = list(sig.parameters.keys())



def test_swrc::academicstaff_is_not_abstract():
    assert not inspect.isabstract(SWRC::AcademicStaff)


def test_swrc::academicstaff_constructor_exists():
    assert callable(SWRC::AcademicStaff.__init__)


def test_swrc::academicstaff_constructor_args():
    sig = inspect.signature(SWRC::AcademicStaff.__init__)
    params = list(sig.parameters.keys())



def test_swrc::student_is_not_abstract():
    assert not inspect.isabstract(SWRC::Student)


def test_swrc::student_constructor_exists():
    assert callable(SWRC::Student.__init__)


def test_swrc::student_constructor_args():
    sig = inspect.signature(SWRC::Student.__init__)
    params = list(sig.parameters.keys())



def test_swrc::employee_is_not_abstract():
    assert not inspect.isabstract(SWRC::Employee)


def test_swrc::employee_constructor_exists():
    assert callable(SWRC::Employee.__init__)


def test_swrc::employee_constructor_args():
    sig = inspect.signature(SWRC::Employee.__init__)
    params = list(sig.parameters.keys())



def test_publication_is_not_abstract():
    assert not inspect.isabstract(Publication)


def test_publication_constructor_exists():
    assert callable(Publication.__init__)


def test_publication_constructor_args():
    sig = inspect.signature(Publication.__init__)
    params = list(sig.parameters.keys())



def test_swrc::manual_is_not_abstract():
    assert not inspect.isabstract(SWRC::Manual)


def test_swrc::manual_constructor_exists():
    assert callable(SWRC::Manual.__init__)


def test_swrc::manual_constructor_args():
    sig = inspect.signature(SWRC::Manual.__init__)
    params = list(sig.parameters.keys())
    assert "address" in params, "Missing parameter 'address'"
    assert "month" in params, "Missing parameter 'month'"
    assert "edition" in params, "Missing parameter 'edition'"

def test_swrc::manual_has_address():
    assert hasattr(SWRC::Manual, "address")
    descriptor = None
    for klass in SWRC::Manual.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)

def test_swrc::manual_has_month():
    assert hasattr(SWRC::Manual, "month")
    descriptor = None
    for klass in SWRC::Manual.__mro__:
        if "month" in klass.__dict__:
            descriptor = klass.__dict__["month"]
            break
    assert isinstance(descriptor, property)

def test_swrc::manual_has_edition():
    assert hasattr(SWRC::Manual, "edition")
    descriptor = None
    for klass in SWRC::Manual.__mro__:
        if "edition" in klass.__dict__:
            descriptor = klass.__dict__["edition"]
            break
    assert isinstance(descriptor, property)



def test_swrc::thesis_is_not_abstract():
    assert not inspect.isabstract(SWRC::Thesis)


def test_swrc::thesis_constructor_exists():
    assert callable(SWRC::Thesis.__init__)


def test_swrc::thesis_constructor_args():
    sig = inspect.signature(SWRC::Thesis.__init__)
    params = list(sig.parameters.keys())
    assert "address" in params, "Missing parameter 'address'"
    assert "month" in params, "Missing parameter 'month'"
    assert "type" in params, "Missing parameter 'type'"

def test_swrc::thesis_has_address():
    assert hasattr(SWRC::Thesis, "address")
    descriptor = None
    for klass in SWRC::Thesis.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)

def test_swrc::thesis_has_month():
    assert hasattr(SWRC::Thesis, "month")
    descriptor = None
    for klass in SWRC::Thesis.__mro__:
        if "month" in klass.__dict__:
            descriptor = klass.__dict__["month"]
            break
    assert isinstance(descriptor, property)

def test_swrc::thesis_has_type():
    assert hasattr(SWRC::Thesis, "type")
    descriptor = None
    for klass in SWRC::Thesis.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_swrc::booklet_is_not_abstract():
    assert not inspect.isabstract(SWRC::Booklet)


def test_swrc::booklet_constructor_exists():
    assert callable(SWRC::Booklet.__init__)


def test_swrc::booklet_constructor_args():
    sig = inspect.signature(SWRC::Booklet.__init__)
    params = list(sig.parameters.keys())
    assert "month" in params, "Missing parameter 'month'"
    assert "howpublished" in params, "Missing parameter 'howpublished'"
    assert "edition" in params, "Missing parameter 'edition'"
    assert "address" in params, "Missing parameter 'address'"

def test_swrc::booklet_has_month():
    assert hasattr(SWRC::Booklet, "month")
    descriptor = None
    for klass in SWRC::Booklet.__mro__:
        if "month" in klass.__dict__:
            descriptor = klass.__dict__["month"]
            break
    assert isinstance(descriptor, property)

def test_swrc::booklet_has_howpublished():
    assert hasattr(SWRC::Booklet, "howpublished")
    descriptor = None
    for klass in SWRC::Booklet.__mro__:
        if "howpublished" in klass.__dict__:
            descriptor = klass.__dict__["howpublished"]
            break
    assert isinstance(descriptor, property)

def test_swrc::booklet_has_edition():
    assert hasattr(SWRC::Booklet, "edition")
    descriptor = None
    for klass in SWRC::Booklet.__mro__:
        if "edition" in klass.__dict__:
            descriptor = klass.__dict__["edition"]
            break
    assert isinstance(descriptor, property)

def test_swrc::booklet_has_address():
    assert hasattr(SWRC::Booklet, "address")
    descriptor = None
    for klass in SWRC::Booklet.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)



def test_swrc::proceedings_is_not_abstract():
    assert not inspect.isabstract(SWRC::Proceedings)


def test_swrc::proceedings_constructor_exists():
    assert callable(SWRC::Proceedings.__init__)


def test_swrc::proceedings_constructor_args():
    sig = inspect.signature(SWRC::Proceedings.__init__)
    params = list(sig.parameters.keys())
    assert "volume" in params, "Missing parameter 'volume'"
    assert "address" in params, "Missing parameter 'address'"
    assert "series" in params, "Missing parameter 'series'"
    assert "month" in params, "Missing parameter 'month'"
    assert "number" in params, "Missing parameter 'number'"

def test_swrc::proceedings_has_volume():
    assert hasattr(SWRC::Proceedings, "volume")
    descriptor = None
    for klass in SWRC::Proceedings.__mro__:
        if "volume" in klass.__dict__:
            descriptor = klass.__dict__["volume"]
            break
    assert isinstance(descriptor, property)

def test_swrc::proceedings_has_address():
    assert hasattr(SWRC::Proceedings, "address")
    descriptor = None
    for klass in SWRC::Proceedings.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)

def test_swrc::proceedings_has_series():
    assert hasattr(SWRC::Proceedings, "series")
    descriptor = None
    for klass in SWRC::Proceedings.__mro__:
        if "series" in klass.__dict__:
            descriptor = klass.__dict__["series"]
            break
    assert isinstance(descriptor, property)

def test_swrc::proceedings_has_month():
    assert hasattr(SWRC::Proceedings, "month")
    descriptor = None
    for klass in SWRC::Proceedings.__mro__:
        if "month" in klass.__dict__:
            descriptor = klass.__dict__["month"]
            break
    assert isinstance(descriptor, property)

def test_swrc::proceedings_has_number():
    assert hasattr(SWRC::Proceedings, "number")
    descriptor = None
    for klass in SWRC::Proceedings.__mro__:
        if "number" in klass.__dict__:
            descriptor = klass.__dict__["number"]
            break
    assert isinstance(descriptor, property)



def test_swrc::inproceedings_is_not_abstract():
    assert not inspect.isabstract(SWRC::InProceedings)


def test_swrc::inproceedings_constructor_exists():
    assert callable(SWRC::InProceedings.__init__)


def test_swrc::inproceedings_constructor_args():
    sig = inspect.signature(SWRC::InProceedings.__init__)
    params = list(sig.parameters.keys())
    assert "volume" in params, "Missing parameter 'volume'"
    assert "month" in params, "Missing parameter 'month'"
    assert "series" in params, "Missing parameter 'series'"
    assert "booktitle" in params, "Missing parameter 'booktitle'"
    assert "pages" in params, "Missing parameter 'pages'"
    assert "number" in params, "Missing parameter 'number'"
    assert "address" in params, "Missing parameter 'address'"

def test_swrc::inproceedings_has_volume():
    assert hasattr(SWRC::InProceedings, "volume")
    descriptor = None
    for klass in SWRC::InProceedings.__mro__:
        if "volume" in klass.__dict__:
            descriptor = klass.__dict__["volume"]
            break
    assert isinstance(descriptor, property)

def test_swrc::inproceedings_has_month():
    assert hasattr(SWRC::InProceedings, "month")
    descriptor = None
    for klass in SWRC::InProceedings.__mro__:
        if "month" in klass.__dict__:
            descriptor = klass.__dict__["month"]
            break
    assert isinstance(descriptor, property)

def test_swrc::inproceedings_has_series():
    assert hasattr(SWRC::InProceedings, "series")
    descriptor = None
    for klass in SWRC::InProceedings.__mro__:
        if "series" in klass.__dict__:
            descriptor = klass.__dict__["series"]
            break
    assert isinstance(descriptor, property)

def test_swrc::inproceedings_has_booktitle():
    assert hasattr(SWRC::InProceedings, "booktitle")
    descriptor = None
    for klass in SWRC::InProceedings.__mro__:
        if "booktitle" in klass.__dict__:
            descriptor = klass.__dict__["booktitle"]
            break
    assert isinstance(descriptor, property)

def test_swrc::inproceedings_has_pages():
    assert hasattr(SWRC::InProceedings, "pages")
    descriptor = None
    for klass in SWRC::InProceedings.__mro__:
        if "pages" in klass.__dict__:
            descriptor = klass.__dict__["pages"]
            break
    assert isinstance(descriptor, property)

def test_swrc::inproceedings_has_number():
    assert hasattr(SWRC::InProceedings, "number")
    descriptor = None
    for klass in SWRC::InProceedings.__mro__:
        if "number" in klass.__dict__:
            descriptor = klass.__dict__["number"]
            break
    assert isinstance(descriptor, property)

def test_swrc::inproceedings_has_address():
    assert hasattr(SWRC::InProceedings, "address")
    descriptor = None
    for klass in SWRC::InProceedings.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)



def test_swrc::book_is_not_abstract():
    assert not inspect.isabstract(SWRC::Book)


def test_swrc::book_constructor_exists():
    assert callable(SWRC::Book.__init__)


def test_swrc::book_constructor_args():
    sig = inspect.signature(SWRC::Book.__init__)
    params = list(sig.parameters.keys())
    assert "price" in params, "Missing parameter 'price'"
    assert "series" in params, "Missing parameter 'series'"
    assert "edition" in params, "Missing parameter 'edition'"
    assert "number" in params, "Missing parameter 'number'"
    assert "address" in params, "Missing parameter 'address'"
    assert "month" in params, "Missing parameter 'month'"
    assert "source" in params, "Missing parameter 'source'"
    assert "volume" in params, "Missing parameter 'volume'"
    assert "isbn" in params, "Missing parameter 'isbn'"

def test_swrc::book_has_price():
    assert hasattr(SWRC::Book, "price")
    descriptor = None
    for klass in SWRC::Book.__mro__:
        if "price" in klass.__dict__:
            descriptor = klass.__dict__["price"]
            break
    assert isinstance(descriptor, property)

def test_swrc::book_has_series():
    assert hasattr(SWRC::Book, "series")
    descriptor = None
    for klass in SWRC::Book.__mro__:
        if "series" in klass.__dict__:
            descriptor = klass.__dict__["series"]
            break
    assert isinstance(descriptor, property)

def test_swrc::book_has_edition():
    assert hasattr(SWRC::Book, "edition")
    descriptor = None
    for klass in SWRC::Book.__mro__:
        if "edition" in klass.__dict__:
            descriptor = klass.__dict__["edition"]
            break
    assert isinstance(descriptor, property)

def test_swrc::book_has_number():
    assert hasattr(SWRC::Book, "number")
    descriptor = None
    for klass in SWRC::Book.__mro__:
        if "number" in klass.__dict__:
            descriptor = klass.__dict__["number"]
            break
    assert isinstance(descriptor, property)

def test_swrc::book_has_address():
    assert hasattr(SWRC::Book, "address")
    descriptor = None
    for klass in SWRC::Book.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)

def test_swrc::book_has_month():
    assert hasattr(SWRC::Book, "month")
    descriptor = None
    for klass in SWRC::Book.__mro__:
        if "month" in klass.__dict__:
            descriptor = klass.__dict__["month"]
            break
    assert isinstance(descriptor, property)

def test_swrc::book_has_source():
    assert hasattr(SWRC::Book, "source")
    descriptor = None
    for klass in SWRC::Book.__mro__:
        if "source" in klass.__dict__:
            descriptor = klass.__dict__["source"]
            break
    assert isinstance(descriptor, property)

def test_swrc::book_has_volume():
    assert hasattr(SWRC::Book, "volume")
    descriptor = None
    for klass in SWRC::Book.__mro__:
        if "volume" in klass.__dict__:
            descriptor = klass.__dict__["volume"]
            break
    assert isinstance(descriptor, property)

def test_swrc::book_has_isbn():
    assert hasattr(SWRC::Book, "isbn")
    descriptor = None
    for klass in SWRC::Book.__mro__:
        if "isbn" in klass.__dict__:
            descriptor = klass.__dict__["isbn"]
            break
    assert isinstance(descriptor, property)



def test_swrc::incollection_is_not_abstract():
    assert not inspect.isabstract(SWRC::InCollection)


def test_swrc::incollection_constructor_exists():
    assert callable(SWRC::InCollection.__init__)


def test_swrc::incollection_constructor_args():
    sig = inspect.signature(SWRC::InCollection.__init__)
    params = list(sig.parameters.keys())
    assert "booktitle" in params, "Missing parameter 'booktitle'"
    assert "pages" in params, "Missing parameter 'pages'"
    assert "number" in params, "Missing parameter 'number'"
    assert "month" in params, "Missing parameter 'month'"
    assert "chapter" in params, "Missing parameter 'chapter'"
    assert "series" in params, "Missing parameter 'series'"
    assert "volume" in params, "Missing parameter 'volume'"
    assert "address" in params, "Missing parameter 'address'"
    assert "type" in params, "Missing parameter 'type'"
    assert "edition" in params, "Missing parameter 'edition'"

def test_swrc::incollection_has_booktitle():
    assert hasattr(SWRC::InCollection, "booktitle")
    descriptor = None
    for klass in SWRC::InCollection.__mro__:
        if "booktitle" in klass.__dict__:
            descriptor = klass.__dict__["booktitle"]
            break
    assert isinstance(descriptor, property)

def test_swrc::incollection_has_pages():
    assert hasattr(SWRC::InCollection, "pages")
    descriptor = None
    for klass in SWRC::InCollection.__mro__:
        if "pages" in klass.__dict__:
            descriptor = klass.__dict__["pages"]
            break
    assert isinstance(descriptor, property)

def test_swrc::incollection_has_number():
    assert hasattr(SWRC::InCollection, "number")
    descriptor = None
    for klass in SWRC::InCollection.__mro__:
        if "number" in klass.__dict__:
            descriptor = klass.__dict__["number"]
            break
    assert isinstance(descriptor, property)

def test_swrc::incollection_has_month():
    assert hasattr(SWRC::InCollection, "month")
    descriptor = None
    for klass in SWRC::InCollection.__mro__:
        if "month" in klass.__dict__:
            descriptor = klass.__dict__["month"]
            break
    assert isinstance(descriptor, property)

def test_swrc::incollection_has_chapter():
    assert hasattr(SWRC::InCollection, "chapter")
    descriptor = None
    for klass in SWRC::InCollection.__mro__:
        if "chapter" in klass.__dict__:
            descriptor = klass.__dict__["chapter"]
            break
    assert isinstance(descriptor, property)

def test_swrc::incollection_has_series():
    assert hasattr(SWRC::InCollection, "series")
    descriptor = None
    for klass in SWRC::InCollection.__mro__:
        if "series" in klass.__dict__:
            descriptor = klass.__dict__["series"]
            break
    assert isinstance(descriptor, property)

def test_swrc::incollection_has_volume():
    assert hasattr(SWRC::InCollection, "volume")
    descriptor = None
    for klass in SWRC::InCollection.__mro__:
        if "volume" in klass.__dict__:
            descriptor = klass.__dict__["volume"]
            break
    assert isinstance(descriptor, property)

def test_swrc::incollection_has_address():
    assert hasattr(SWRC::InCollection, "address")
    descriptor = None
    for klass in SWRC::InCollection.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)

def test_swrc::incollection_has_type():
    assert hasattr(SWRC::InCollection, "type")
    descriptor = None
    for klass in SWRC::InCollection.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_swrc::incollection_has_edition():
    assert hasattr(SWRC::InCollection, "edition")
    descriptor = None
    for klass in SWRC::InCollection.__mro__:
        if "edition" in klass.__dict__:
            descriptor = klass.__dict__["edition"]
            break
    assert isinstance(descriptor, property)



def test_swrc::inbook_is_not_abstract():
    assert not inspect.isabstract(SWRC::InBook)


def test_swrc::inbook_constructor_exists():
    assert callable(SWRC::InBook.__init__)


def test_swrc::inbook_constructor_args():
    sig = inspect.signature(SWRC::InBook.__init__)
    params = list(sig.parameters.keys())
    assert "number" in params, "Missing parameter 'number'"
    assert "volume" in params, "Missing parameter 'volume'"
    assert "address" in params, "Missing parameter 'address'"
    assert "month" in params, "Missing parameter 'month'"
    assert "series" in params, "Missing parameter 'series'"
    assert "chapter" in params, "Missing parameter 'chapter'"
    assert "type" in params, "Missing parameter 'type'"
    assert "pages" in params, "Missing parameter 'pages'"

def test_swrc::inbook_has_number():
    assert hasattr(SWRC::InBook, "number")
    descriptor = None
    for klass in SWRC::InBook.__mro__:
        if "number" in klass.__dict__:
            descriptor = klass.__dict__["number"]
            break
    assert isinstance(descriptor, property)

def test_swrc::inbook_has_volume():
    assert hasattr(SWRC::InBook, "volume")
    descriptor = None
    for klass in SWRC::InBook.__mro__:
        if "volume" in klass.__dict__:
            descriptor = klass.__dict__["volume"]
            break
    assert isinstance(descriptor, property)

def test_swrc::inbook_has_address():
    assert hasattr(SWRC::InBook, "address")
    descriptor = None
    for klass in SWRC::InBook.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)

def test_swrc::inbook_has_month():
    assert hasattr(SWRC::InBook, "month")
    descriptor = None
    for klass in SWRC::InBook.__mro__:
        if "month" in klass.__dict__:
            descriptor = klass.__dict__["month"]
            break
    assert isinstance(descriptor, property)

def test_swrc::inbook_has_series():
    assert hasattr(SWRC::InBook, "series")
    descriptor = None
    for klass in SWRC::InBook.__mro__:
        if "series" in klass.__dict__:
            descriptor = klass.__dict__["series"]
            break
    assert isinstance(descriptor, property)

def test_swrc::inbook_has_chapter():
    assert hasattr(SWRC::InBook, "chapter")
    descriptor = None
    for klass in SWRC::InBook.__mro__:
        if "chapter" in klass.__dict__:
            descriptor = klass.__dict__["chapter"]
            break
    assert isinstance(descriptor, property)

def test_swrc::inbook_has_type():
    assert hasattr(SWRC::InBook, "type")
    descriptor = None
    for klass in SWRC::InBook.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_swrc::inbook_has_pages():
    assert hasattr(SWRC::InBook, "pages")
    descriptor = None
    for klass in SWRC::InBook.__mro__:
        if "pages" in klass.__dict__:
            descriptor = klass.__dict__["pages"]
            break
    assert isinstance(descriptor, property)



def test_swrc::unpublished_is_not_abstract():
    assert not inspect.isabstract(SWRC::Unpublished)


def test_swrc::unpublished_constructor_exists():
    assert callable(SWRC::Unpublished.__init__)


def test_swrc::unpublished_constructor_args():
    sig = inspect.signature(SWRC::Unpublished.__init__)
    params = list(sig.parameters.keys())
    assert "month" in params, "Missing parameter 'month'"

def test_swrc::unpublished_has_month():
    assert hasattr(SWRC::Unpublished, "month")
    descriptor = None
    for klass in SWRC::Unpublished.__mro__:
        if "month" in klass.__dict__:
            descriptor = klass.__dict__["month"]
            break
    assert isinstance(descriptor, property)



def test_swrc::misc_is_not_abstract():
    assert not inspect.isabstract(SWRC::Misc)


def test_swrc::misc_constructor_exists():
    assert callable(SWRC::Misc.__init__)


def test_swrc::misc_constructor_args():
    sig = inspect.signature(SWRC::Misc.__init__)
    params = list(sig.parameters.keys())
    assert "howpublished" in params, "Missing parameter 'howpublished'"
    assert "month" in params, "Missing parameter 'month'"

def test_swrc::misc_has_howpublished():
    assert hasattr(SWRC::Misc, "howpublished")
    descriptor = None
    for klass in SWRC::Misc.__mro__:
        if "howpublished" in klass.__dict__:
            descriptor = klass.__dict__["howpublished"]
            break
    assert isinstance(descriptor, property)

def test_swrc::misc_has_month():
    assert hasattr(SWRC::Misc, "month")
    descriptor = None
    for klass in SWRC::Misc.__mro__:
        if "month" in klass.__dict__:
            descriptor = klass.__dict__["month"]
            break
    assert isinstance(descriptor, property)



def test_swrc::report_is_not_abstract():
    assert not inspect.isabstract(SWRC::Report)


def test_swrc::report_constructor_exists():
    assert callable(SWRC::Report.__init__)


def test_swrc::report_constructor_args():
    sig = inspect.signature(SWRC::Report.__init__)
    params = list(sig.parameters.keys())



def test_swrc::article_is_not_abstract():
    assert not inspect.isabstract(SWRC::Article)


def test_swrc::article_constructor_exists():
    assert callable(SWRC::Article.__init__)


def test_swrc::article_constructor_args():
    sig = inspect.signature(SWRC::Article.__init__)
    params = list(sig.parameters.keys())
    assert "volume" in params, "Missing parameter 'volume'"
    assert "journal" in params, "Missing parameter 'journal'"
    assert "month" in params, "Missing parameter 'month'"
    assert "number" in params, "Missing parameter 'number'"
    assert "pages" in params, "Missing parameter 'pages'"

def test_swrc::article_has_volume():
    assert hasattr(SWRC::Article, "volume")
    descriptor = None
    for klass in SWRC::Article.__mro__:
        if "volume" in klass.__dict__:
            descriptor = klass.__dict__["volume"]
            break
    assert isinstance(descriptor, property)

def test_swrc::article_has_journal():
    assert hasattr(SWRC::Article, "journal")
    descriptor = None
    for klass in SWRC::Article.__mro__:
        if "journal" in klass.__dict__:
            descriptor = klass.__dict__["journal"]
            break
    assert isinstance(descriptor, property)

def test_swrc::article_has_month():
    assert hasattr(SWRC::Article, "month")
    descriptor = None
    for klass in SWRC::Article.__mro__:
        if "month" in klass.__dict__:
            descriptor = klass.__dict__["month"]
            break
    assert isinstance(descriptor, property)

def test_swrc::article_has_number():
    assert hasattr(SWRC::Article, "number")
    descriptor = None
    for klass in SWRC::Article.__mro__:
        if "number" in klass.__dict__:
            descriptor = klass.__dict__["number"]
            break
    assert isinstance(descriptor, property)

def test_swrc::article_has_pages():
    assert hasattr(SWRC::Article, "pages")
    descriptor = None
    for klass in SWRC::Article.__mro__:
        if "pages" in klass.__dict__:
            descriptor = klass.__dict__["pages"]
            break
    assert isinstance(descriptor, property)



def test_swrc::publication_is_not_abstract():
    assert not inspect.isabstract(SWRC::Publication)


def test_swrc::publication_constructor_exists():
    assert callable(SWRC::Publication.__init__)


def test_swrc::publication_constructor_args():
    sig = inspect.signature(SWRC::Publication.__init__)
    params = list(sig.parameters.keys())
    assert "year" in params, "Missing parameter 'year'"
    assert "note" in params, "Missing parameter 'note'"
    assert "title" in params, "Missing parameter 'title'"
    assert "abstract" in params, "Missing parameter 'abstract'"
    assert "keywords" in params, "Missing parameter 'keywords'"

def test_swrc::publication_has_year():
    assert hasattr(SWRC::Publication, "year")
    descriptor = None
    for klass in SWRC::Publication.__mro__:
        if "year" in klass.__dict__:
            descriptor = klass.__dict__["year"]
            break
    assert isinstance(descriptor, property)

def test_swrc::publication_has_note():
    assert hasattr(SWRC::Publication, "note")
    descriptor = None
    for klass in SWRC::Publication.__mro__:
        if "note" in klass.__dict__:
            descriptor = klass.__dict__["note"]
            break
    assert isinstance(descriptor, property)

def test_swrc::publication_has_title():
    assert hasattr(SWRC::Publication, "title")
    descriptor = None
    for klass in SWRC::Publication.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_swrc::publication_has_abstract():
    assert hasattr(SWRC::Publication, "abstract")
    descriptor = None
    for klass in SWRC::Publication.__mro__:
        if "abstract" in klass.__dict__:
            descriptor = klass.__dict__["abstract"]
            break
    assert isinstance(descriptor, property)

def test_swrc::publication_has_keywords():
    assert hasattr(SWRC::Publication, "keywords")
    descriptor = None
    for klass in SWRC::Publication.__mro__:
        if "keywords" in klass.__dict__:
            descriptor = klass.__dict__["keywords"]
            break
    assert isinstance(descriptor, property)



def test_swrc::bibliography_is_not_abstract():
    assert not inspect.isabstract(SWRC::Bibliography)


def test_swrc::bibliography_constructor_exists():
    assert callable(SWRC::Bibliography.__init__)


def test_swrc::bibliography_constructor_args():
    sig = inspect.signature(SWRC::Bibliography.__init__)
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
Topic_strategy = st.builds(
    Topic,
)
SWRC::ResearchTopic_strategy = st.builds(
    SWRC::ResearchTopic,
)
SWRC::Topic_strategy = st.builds(
    SWRC::Topic,
    name=
        safe_text
)
SWRC::Product_strategy = st.builds(
    SWRC::Product,
    name=
        safe_text
)
ProjectReport_strategy = st.builds(
    ProjectReport,
)
Department_strategy = st.builds(
    Department,
)
SWRC::Project_strategy = st.builds(
    SWRC::Project,
    name=
        safe_text
)
Institute_strategy = st.builds(
    Institute,
)
Product_strategy = st.builds(
    Product,
)
SWRC::SoftwareComponent_strategy = st.builds(
    SWRC::SoftwareComponent,
    hasPrice=
        safe_text
)
TechnicalReport_strategy = st.builds(
    TechnicalReport,
)
SWRC::Organization_strategy = st.builds(
    SWRC::Organization,
    name=
        safe_text,
    location=
        safe_text
)
Graduate_strategy = st.builds(
    Graduate,
)
SWRC::PhDStudent_strategy = st.builds(
    SWRC::PhDStudent,
)
Student_strategy = st.builds(
    Student,
)
SWRC::Graduate_strategy = st.builds(
    SWRC::Graduate,
)
SWRC::Undergraduate_strategy = st.builds(
    SWRC::Undergraduate,
)
FacultyMember_strategy = st.builds(
    FacultyMember,
)
SWRC::AssociateProfessor_strategy = st.builds(
    SWRC::AssociateProfessor,
)
SWRC::AssistantProfessor_strategy = st.builds(
    SWRC::AssistantProfessor,
)
SWRC::FullProfessor_strategy = st.builds(
    SWRC::FullProfessor,
)
ResearchTopic_strategy = st.builds(
    ResearchTopic,
)
PhDStudent_strategy = st.builds(
    PhDStudent,
)
ResearchGroup_strategy = st.builds(
    ResearchGroup,
)
Employee_strategy = st.builds(
    Employee,
)
SWRC::TechnicalStaff_strategy = st.builds(
    SWRC::TechnicalStaff,
)
SWRC::AdministrativeStaff_strategy = st.builds(
    SWRC::AdministrativeStaff,
)
SWRC::Manager_strategy = st.builds(
    SWRC::Manager,
)
AcademicStaff_strategy = st.builds(
    AcademicStaff,
)
SWRC::Lecturer_strategy = st.builds(
    SWRC::Lecturer,
)
SWRC::FacultyMember_strategy = st.builds(
    SWRC::FacultyMember,
)
SWRC::Person_strategy = st.builds(
    SWRC::Person,
    phone=
        safe_text,
    photo=
        safe_text,
    homepage=
        safe_text,
    fax=
        safe_text,
    email=
        safe_text,
    address=
        safe_text,
    name=
        safe_text
)
Meeting_strategy = st.builds(
    Meeting,
)
SWRC::ProjectMeeting_strategy = st.builds(
    SWRC::ProjectMeeting,
)
Event_strategy = st.builds(
    Event,
)
SWRC::Exhibition_strategy = st.builds(
    SWRC::Exhibition,
)
SWRC::Workshop_strategy = st.builds(
    SWRC::Workshop,
    series=
        safe_text
)
SWRC::Meeting_strategy = st.builds(
    SWRC::Meeting,
    title=
        safe_text
)
SWRC::Lecture_strategy = st.builds(
    SWRC::Lecture,
)
SWRC::Conference_strategy = st.builds(
    SWRC::Conference,
    series=
        safe_text
)
SWRC::Event_strategy = st.builds(
    SWRC::Event,
    date=
        safe_text,
    name=
        safe_text,
    eventTitle=
        safe_text,
    location=
        safe_text
)
Project_strategy = st.builds(
    Project,
)
SWRC::DevelopmentProject_strategy = st.builds(
    SWRC::DevelopmentProject,
)
SWRC::ResearchProject_strategy = st.builds(
    SWRC::ResearchProject,
)
SWRC::SoftwareProject_strategy = st.builds(
    SWRC::SoftwareProject,
)
Report_strategy = st.builds(
    Report,
)
SWRC::TechnicalReport_strategy = st.builds(
    SWRC::TechnicalReport,
    series=
        safe_text
)
SWRC::ProjectReport_strategy = st.builds(
    SWRC::ProjectReport,
)
Thesis_strategy = st.builds(
    Thesis,
)
SWRC::PhDThesis_strategy = st.builds(
    SWRC::PhDThesis,
)
SWRC::MasterThesis_strategy = st.builds(
    SWRC::MasterThesis,
)
University_strategy = st.builds(
    University,
)
Organization_strategy = st.builds(
    Organization,
)
SWRC::Enterprise_strategy = st.builds(
    SWRC::Enterprise,
)
SWRC::University_strategy = st.builds(
    SWRC::University,
)
SWRC::Department_strategy = st.builds(
    SWRC::Department,
)
SWRC::Association_strategy = st.builds(
    SWRC::Association,
)
SWRC::ResearchGroup_strategy = st.builds(
    SWRC::ResearchGroup,
)
SWRC::Institute_strategy = st.builds(
    SWRC::Institute,
)
Person_strategy = st.builds(
    Person,
)
SWRC::AcademicStaff_strategy = st.builds(
    SWRC::AcademicStaff,
)
SWRC::Student_strategy = st.builds(
    SWRC::Student,
)
SWRC::Employee_strategy = st.builds(
    SWRC::Employee,
)
Publication_strategy = st.builds(
    Publication,
)
SWRC::Manual_strategy = st.builds(
    SWRC::Manual,
    address=
        safe_text,
    month=
        safe_text,
    edition=
        safe_text
)
SWRC::Thesis_strategy = st.builds(
    SWRC::Thesis,
    address=
        safe_text,
    month=
        safe_text,
    type=
        safe_text
)
SWRC::Booklet_strategy = st.builds(
    SWRC::Booklet,
    month=
        safe_text,
    howpublished=
        safe_text,
    edition=
        safe_text,
    address=
        safe_text
)
SWRC::Proceedings_strategy = st.builds(
    SWRC::Proceedings,
    volume=
        safe_text,
    address=
        safe_text,
    series=
        safe_text,
    month=
        safe_text,
    number=
        safe_text
)
SWRC::InProceedings_strategy = st.builds(
    SWRC::InProceedings,
    volume=
        safe_text,
    month=
        safe_text,
    series=
        safe_text,
    booktitle=
        safe_text,
    pages=
        safe_text,
    number=
        safe_text,
    address=
        safe_text
)
SWRC::Book_strategy = st.builds(
    SWRC::Book,
    price=
        safe_text,
    series=
        safe_text,
    edition=
        safe_text,
    number=
        safe_text,
    address=
        safe_text,
    month=
        safe_text,
    source=
        safe_text,
    volume=
        safe_text,
    isbn=
        safe_text
)
SWRC::InCollection_strategy = st.builds(
    SWRC::InCollection,
    booktitle=
        safe_text,
    pages=
        safe_text,
    number=
        safe_text,
    month=
        safe_text,
    chapter=
        safe_text,
    series=
        safe_text,
    volume=
        safe_text,
    address=
        safe_text,
    type=
        safe_text,
    edition=
        safe_text
)
SWRC::InBook_strategy = st.builds(
    SWRC::InBook,
    number=
        safe_text,
    volume=
        safe_text,
    address=
        safe_text,
    month=
        safe_text,
    series=
        safe_text,
    chapter=
        safe_text,
    type=
        safe_text,
    pages=
        safe_text
)
SWRC::Unpublished_strategy = st.builds(
    SWRC::Unpublished,
    month=
        safe_text
)
SWRC::Misc_strategy = st.builds(
    SWRC::Misc,
    howpublished=
        safe_text,
    month=
        safe_text
)
SWRC::Report_strategy = st.builds(
    SWRC::Report,
)
SWRC::Article_strategy = st.builds(
    SWRC::Article,
    volume=
        safe_text,
    journal=
        safe_text,
    month=
        safe_text,
    number=
        safe_text,
    pages=
        safe_text
)
SWRC::Publication_strategy = st.builds(
    SWRC::Publication,
    year=
        safe_text,
    note=
        safe_text,
    title=
        safe_text,
    abstract=
        safe_text,
    keywords=
        safe_text
)
SWRC::Bibliography_strategy = st.builds(
    SWRC::Bibliography,
)

@given(instance=Topic_strategy)
@settings(max_examples=50)
def test_topic_instantiation(instance):
    assert isinstance(instance, Topic)

@given(instance=SWRC::ResearchTopic_strategy)
@settings(max_examples=50)
def test_swrc::researchtopic_instantiation(instance):
    assert isinstance(instance, SWRC::ResearchTopic)

@given(instance=SWRC::Topic_strategy)
@settings(max_examples=50)
def test_swrc::topic_instantiation(instance):
    assert isinstance(instance, SWRC::Topic)

@given(instance=SWRC::Topic_strategy)
def test_swrc::topic_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=SWRC::Topic_strategy)
def test_swrc::topic_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SWRC::Product_strategy)
@settings(max_examples=50)
def test_swrc::product_instantiation(instance):
    assert isinstance(instance, SWRC::Product)

@given(instance=SWRC::Product_strategy)
def test_swrc::product_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=SWRC::Product_strategy)
def test_swrc::product_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ProjectReport_strategy)
@settings(max_examples=50)
def test_projectreport_instantiation(instance):
    assert isinstance(instance, ProjectReport)

@given(instance=Department_strategy)
@settings(max_examples=50)
def test_department_instantiation(instance):
    assert isinstance(instance, Department)

@given(instance=SWRC::Project_strategy)
@settings(max_examples=50)
def test_swrc::project_instantiation(instance):
    assert isinstance(instance, SWRC::Project)

@given(instance=SWRC::Project_strategy)
def test_swrc::project_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=SWRC::Project_strategy)
def test_swrc::project_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Institute_strategy)
@settings(max_examples=50)
def test_institute_instantiation(instance):
    assert isinstance(instance, Institute)

@given(instance=Product_strategy)
@settings(max_examples=50)
def test_product_instantiation(instance):
    assert isinstance(instance, Product)

@given(instance=SWRC::SoftwareComponent_strategy)
@settings(max_examples=50)
def test_swrc::softwarecomponent_instantiation(instance):
    assert isinstance(instance, SWRC::SoftwareComponent)

@given(instance=SWRC::SoftwareComponent_strategy)
def test_swrc::softwarecomponent_hasPrice_type(instance):
    assert isinstance(instance.hasPrice, str)


@given(instance=SWRC::SoftwareComponent_strategy)
def test_swrc::softwarecomponent_hasPrice_setter(instance):
    original = instance.hasPrice
    instance.hasPrice = original
    assert instance.hasPrice == original

@given(instance=TechnicalReport_strategy)
@settings(max_examples=50)
def test_technicalreport_instantiation(instance):
    assert isinstance(instance, TechnicalReport)

@given(instance=SWRC::Organization_strategy)
@settings(max_examples=50)
def test_swrc::organization_instantiation(instance):
    assert isinstance(instance, SWRC::Organization)

@given(instance=SWRC::Organization_strategy)
def test_swrc::organization_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=SWRC::Organization_strategy)
def test_swrc::organization_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SWRC::Organization_strategy)
def test_swrc::organization_location_type(instance):
    assert isinstance(instance.location, str)


@given(instance=SWRC::Organization_strategy)
def test_swrc::organization_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=Graduate_strategy)
@settings(max_examples=50)
def test_graduate_instantiation(instance):
    assert isinstance(instance, Graduate)

@given(instance=SWRC::PhDStudent_strategy)
@settings(max_examples=50)
def test_swrc::phdstudent_instantiation(instance):
    assert isinstance(instance, SWRC::PhDStudent)

@given(instance=Student_strategy)
@settings(max_examples=50)
def test_student_instantiation(instance):
    assert isinstance(instance, Student)

@given(instance=SWRC::Graduate_strategy)
@settings(max_examples=50)
def test_swrc::graduate_instantiation(instance):
    assert isinstance(instance, SWRC::Graduate)

@given(instance=SWRC::Undergraduate_strategy)
@settings(max_examples=50)
def test_swrc::undergraduate_instantiation(instance):
    assert isinstance(instance, SWRC::Undergraduate)

@given(instance=FacultyMember_strategy)
@settings(max_examples=50)
def test_facultymember_instantiation(instance):
    assert isinstance(instance, FacultyMember)

@given(instance=SWRC::AssociateProfessor_strategy)
@settings(max_examples=50)
def test_swrc::associateprofessor_instantiation(instance):
    assert isinstance(instance, SWRC::AssociateProfessor)

@given(instance=SWRC::AssistantProfessor_strategy)
@settings(max_examples=50)
def test_swrc::assistantprofessor_instantiation(instance):
    assert isinstance(instance, SWRC::AssistantProfessor)

@given(instance=SWRC::FullProfessor_strategy)
@settings(max_examples=50)
def test_swrc::fullprofessor_instantiation(instance):
    assert isinstance(instance, SWRC::FullProfessor)

@given(instance=ResearchTopic_strategy)
@settings(max_examples=50)
def test_researchtopic_instantiation(instance):
    assert isinstance(instance, ResearchTopic)

@given(instance=PhDStudent_strategy)
@settings(max_examples=50)
def test_phdstudent_instantiation(instance):
    assert isinstance(instance, PhDStudent)

@given(instance=ResearchGroup_strategy)
@settings(max_examples=50)
def test_researchgroup_instantiation(instance):
    assert isinstance(instance, ResearchGroup)

@given(instance=Employee_strategy)
@settings(max_examples=50)
def test_employee_instantiation(instance):
    assert isinstance(instance, Employee)

@given(instance=SWRC::TechnicalStaff_strategy)
@settings(max_examples=50)
def test_swrc::technicalstaff_instantiation(instance):
    assert isinstance(instance, SWRC::TechnicalStaff)

@given(instance=SWRC::AdministrativeStaff_strategy)
@settings(max_examples=50)
def test_swrc::administrativestaff_instantiation(instance):
    assert isinstance(instance, SWRC::AdministrativeStaff)

@given(instance=SWRC::Manager_strategy)
@settings(max_examples=50)
def test_swrc::manager_instantiation(instance):
    assert isinstance(instance, SWRC::Manager)

@given(instance=AcademicStaff_strategy)
@settings(max_examples=50)
def test_academicstaff_instantiation(instance):
    assert isinstance(instance, AcademicStaff)

@given(instance=SWRC::Lecturer_strategy)
@settings(max_examples=50)
def test_swrc::lecturer_instantiation(instance):
    assert isinstance(instance, SWRC::Lecturer)

@given(instance=SWRC::FacultyMember_strategy)
@settings(max_examples=50)
def test_swrc::facultymember_instantiation(instance):
    assert isinstance(instance, SWRC::FacultyMember)

@given(instance=SWRC::Person_strategy)
@settings(max_examples=50)
def test_swrc::person_instantiation(instance):
    assert isinstance(instance, SWRC::Person)

@given(instance=SWRC::Person_strategy)
def test_swrc::person_phone_type(instance):
    assert isinstance(instance.phone, str)


@given(instance=SWRC::Person_strategy)
def test_swrc::person_phone_setter(instance):
    original = instance.phone
    instance.phone = original
    assert instance.phone == original

@given(instance=SWRC::Person_strategy)
def test_swrc::person_photo_type(instance):
    assert isinstance(instance.photo, str)


@given(instance=SWRC::Person_strategy)
def test_swrc::person_photo_setter(instance):
    original = instance.photo
    instance.photo = original
    assert instance.photo == original

@given(instance=SWRC::Person_strategy)
def test_swrc::person_homepage_type(instance):
    assert isinstance(instance.homepage, str)


@given(instance=SWRC::Person_strategy)
def test_swrc::person_homepage_setter(instance):
    original = instance.homepage
    instance.homepage = original
    assert instance.homepage == original

@given(instance=SWRC::Person_strategy)
def test_swrc::person_fax_type(instance):
    assert isinstance(instance.fax, str)


@given(instance=SWRC::Person_strategy)
def test_swrc::person_fax_setter(instance):
    original = instance.fax
    instance.fax = original
    assert instance.fax == original

@given(instance=SWRC::Person_strategy)
def test_swrc::person_email_type(instance):
    assert isinstance(instance.email, str)


@given(instance=SWRC::Person_strategy)
def test_swrc::person_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original

@given(instance=SWRC::Person_strategy)
def test_swrc::person_address_type(instance):
    assert isinstance(instance.address, str)


@given(instance=SWRC::Person_strategy)
def test_swrc::person_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original

@given(instance=SWRC::Person_strategy)
def test_swrc::person_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=SWRC::Person_strategy)
def test_swrc::person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Meeting_strategy)
@settings(max_examples=50)
def test_meeting_instantiation(instance):
    assert isinstance(instance, Meeting)

@given(instance=SWRC::ProjectMeeting_strategy)
@settings(max_examples=50)
def test_swrc::projectmeeting_instantiation(instance):
    assert isinstance(instance, SWRC::ProjectMeeting)

@given(instance=Event_strategy)
@settings(max_examples=50)
def test_event_instantiation(instance):
    assert isinstance(instance, Event)

@given(instance=SWRC::Exhibition_strategy)
@settings(max_examples=50)
def test_swrc::exhibition_instantiation(instance):
    assert isinstance(instance, SWRC::Exhibition)

@given(instance=SWRC::Workshop_strategy)
@settings(max_examples=50)
def test_swrc::workshop_instantiation(instance):
    assert isinstance(instance, SWRC::Workshop)

@given(instance=SWRC::Workshop_strategy)
def test_swrc::workshop_series_type(instance):
    assert isinstance(instance.series, str)


@given(instance=SWRC::Workshop_strategy)
def test_swrc::workshop_series_setter(instance):
    original = instance.series
    instance.series = original
    assert instance.series == original

@given(instance=SWRC::Meeting_strategy)
@settings(max_examples=50)
def test_swrc::meeting_instantiation(instance):
    assert isinstance(instance, SWRC::Meeting)

@given(instance=SWRC::Meeting_strategy)
def test_swrc::meeting_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=SWRC::Meeting_strategy)
def test_swrc::meeting_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=SWRC::Lecture_strategy)
@settings(max_examples=50)
def test_swrc::lecture_instantiation(instance):
    assert isinstance(instance, SWRC::Lecture)

@given(instance=SWRC::Conference_strategy)
@settings(max_examples=50)
def test_swrc::conference_instantiation(instance):
    assert isinstance(instance, SWRC::Conference)

@given(instance=SWRC::Conference_strategy)
def test_swrc::conference_series_type(instance):
    assert isinstance(instance.series, str)


@given(instance=SWRC::Conference_strategy)
def test_swrc::conference_series_setter(instance):
    original = instance.series
    instance.series = original
    assert instance.series == original

@given(instance=SWRC::Event_strategy)
@settings(max_examples=50)
def test_swrc::event_instantiation(instance):
    assert isinstance(instance, SWRC::Event)

@given(instance=SWRC::Event_strategy)
def test_swrc::event_date_type(instance):
    assert isinstance(instance.date, str)


@given(instance=SWRC::Event_strategy)
def test_swrc::event_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original

@given(instance=SWRC::Event_strategy)
def test_swrc::event_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=SWRC::Event_strategy)
def test_swrc::event_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SWRC::Event_strategy)
def test_swrc::event_eventTitle_type(instance):
    assert isinstance(instance.eventTitle, str)


@given(instance=SWRC::Event_strategy)
def test_swrc::event_eventTitle_setter(instance):
    original = instance.eventTitle
    instance.eventTitle = original
    assert instance.eventTitle == original

@given(instance=SWRC::Event_strategy)
def test_swrc::event_location_type(instance):
    assert isinstance(instance.location, str)


@given(instance=SWRC::Event_strategy)
def test_swrc::event_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=Project_strategy)
@settings(max_examples=50)
def test_project_instantiation(instance):
    assert isinstance(instance, Project)

@given(instance=SWRC::DevelopmentProject_strategy)
@settings(max_examples=50)
def test_swrc::developmentproject_instantiation(instance):
    assert isinstance(instance, SWRC::DevelopmentProject)

@given(instance=SWRC::ResearchProject_strategy)
@settings(max_examples=50)
def test_swrc::researchproject_instantiation(instance):
    assert isinstance(instance, SWRC::ResearchProject)

@given(instance=SWRC::SoftwareProject_strategy)
@settings(max_examples=50)
def test_swrc::softwareproject_instantiation(instance):
    assert isinstance(instance, SWRC::SoftwareProject)

@given(instance=Report_strategy)
@settings(max_examples=50)
def test_report_instantiation(instance):
    assert isinstance(instance, Report)

@given(instance=SWRC::TechnicalReport_strategy)
@settings(max_examples=50)
def test_swrc::technicalreport_instantiation(instance):
    assert isinstance(instance, SWRC::TechnicalReport)

@given(instance=SWRC::TechnicalReport_strategy)
def test_swrc::technicalreport_series_type(instance):
    assert isinstance(instance.series, str)


@given(instance=SWRC::TechnicalReport_strategy)
def test_swrc::technicalreport_series_setter(instance):
    original = instance.series
    instance.series = original
    assert instance.series == original

@given(instance=SWRC::ProjectReport_strategy)
@settings(max_examples=50)
def test_swrc::projectreport_instantiation(instance):
    assert isinstance(instance, SWRC::ProjectReport)

@given(instance=Thesis_strategy)
@settings(max_examples=50)
def test_thesis_instantiation(instance):
    assert isinstance(instance, Thesis)

@given(instance=SWRC::PhDThesis_strategy)
@settings(max_examples=50)
def test_swrc::phdthesis_instantiation(instance):
    assert isinstance(instance, SWRC::PhDThesis)

@given(instance=SWRC::MasterThesis_strategy)
@settings(max_examples=50)
def test_swrc::masterthesis_instantiation(instance):
    assert isinstance(instance, SWRC::MasterThesis)

@given(instance=University_strategy)
@settings(max_examples=50)
def test_university_instantiation(instance):
    assert isinstance(instance, University)

@given(instance=Organization_strategy)
@settings(max_examples=50)
def test_organization_instantiation(instance):
    assert isinstance(instance, Organization)

@given(instance=SWRC::Enterprise_strategy)
@settings(max_examples=50)
def test_swrc::enterprise_instantiation(instance):
    assert isinstance(instance, SWRC::Enterprise)

@given(instance=SWRC::University_strategy)
@settings(max_examples=50)
def test_swrc::university_instantiation(instance):
    assert isinstance(instance, SWRC::University)

@given(instance=SWRC::Department_strategy)
@settings(max_examples=50)
def test_swrc::department_instantiation(instance):
    assert isinstance(instance, SWRC::Department)

@given(instance=SWRC::Association_strategy)
@settings(max_examples=50)
def test_swrc::association_instantiation(instance):
    assert isinstance(instance, SWRC::Association)

@given(instance=SWRC::ResearchGroup_strategy)
@settings(max_examples=50)
def test_swrc::researchgroup_instantiation(instance):
    assert isinstance(instance, SWRC::ResearchGroup)

@given(instance=SWRC::Institute_strategy)
@settings(max_examples=50)
def test_swrc::institute_instantiation(instance):
    assert isinstance(instance, SWRC::Institute)

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)

@given(instance=SWRC::AcademicStaff_strategy)
@settings(max_examples=50)
def test_swrc::academicstaff_instantiation(instance):
    assert isinstance(instance, SWRC::AcademicStaff)

@given(instance=SWRC::Student_strategy)
@settings(max_examples=50)
def test_swrc::student_instantiation(instance):
    assert isinstance(instance, SWRC::Student)

@given(instance=SWRC::Employee_strategy)
@settings(max_examples=50)
def test_swrc::employee_instantiation(instance):
    assert isinstance(instance, SWRC::Employee)

@given(instance=Publication_strategy)
@settings(max_examples=50)
def test_publication_instantiation(instance):
    assert isinstance(instance, Publication)

@given(instance=SWRC::Manual_strategy)
@settings(max_examples=50)
def test_swrc::manual_instantiation(instance):
    assert isinstance(instance, SWRC::Manual)

@given(instance=SWRC::Manual_strategy)
def test_swrc::manual_address_type(instance):
    assert isinstance(instance.address, str)


@given(instance=SWRC::Manual_strategy)
def test_swrc::manual_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original

@given(instance=SWRC::Manual_strategy)
def test_swrc::manual_month_type(instance):
    assert isinstance(instance.month, str)


@given(instance=SWRC::Manual_strategy)
def test_swrc::manual_month_setter(instance):
    original = instance.month
    instance.month = original
    assert instance.month == original

@given(instance=SWRC::Manual_strategy)
def test_swrc::manual_edition_type(instance):
    assert isinstance(instance.edition, str)


@given(instance=SWRC::Manual_strategy)
def test_swrc::manual_edition_setter(instance):
    original = instance.edition
    instance.edition = original
    assert instance.edition == original

@given(instance=SWRC::Thesis_strategy)
@settings(max_examples=50)
def test_swrc::thesis_instantiation(instance):
    assert isinstance(instance, SWRC::Thesis)

@given(instance=SWRC::Thesis_strategy)
def test_swrc::thesis_address_type(instance):
    assert isinstance(instance.address, str)


@given(instance=SWRC::Thesis_strategy)
def test_swrc::thesis_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original

@given(instance=SWRC::Thesis_strategy)
def test_swrc::thesis_month_type(instance):
    assert isinstance(instance.month, str)


@given(instance=SWRC::Thesis_strategy)
def test_swrc::thesis_month_setter(instance):
    original = instance.month
    instance.month = original
    assert instance.month == original

@given(instance=SWRC::Thesis_strategy)
def test_swrc::thesis_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=SWRC::Thesis_strategy)
def test_swrc::thesis_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=SWRC::Booklet_strategy)
@settings(max_examples=50)
def test_swrc::booklet_instantiation(instance):
    assert isinstance(instance, SWRC::Booklet)

@given(instance=SWRC::Booklet_strategy)
def test_swrc::booklet_month_type(instance):
    assert isinstance(instance.month, str)


@given(instance=SWRC::Booklet_strategy)
def test_swrc::booklet_month_setter(instance):
    original = instance.month
    instance.month = original
    assert instance.month == original

@given(instance=SWRC::Booklet_strategy)
def test_swrc::booklet_howpublished_type(instance):
    assert isinstance(instance.howpublished, str)


@given(instance=SWRC::Booklet_strategy)
def test_swrc::booklet_howpublished_setter(instance):
    original = instance.howpublished
    instance.howpublished = original
    assert instance.howpublished == original

@given(instance=SWRC::Booklet_strategy)
def test_swrc::booklet_edition_type(instance):
    assert isinstance(instance.edition, str)


@given(instance=SWRC::Booklet_strategy)
def test_swrc::booklet_edition_setter(instance):
    original = instance.edition
    instance.edition = original
    assert instance.edition == original

@given(instance=SWRC::Booklet_strategy)
def test_swrc::booklet_address_type(instance):
    assert isinstance(instance.address, str)


@given(instance=SWRC::Booklet_strategy)
def test_swrc::booklet_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original

@given(instance=SWRC::Proceedings_strategy)
@settings(max_examples=50)
def test_swrc::proceedings_instantiation(instance):
    assert isinstance(instance, SWRC::Proceedings)

@given(instance=SWRC::Proceedings_strategy)
def test_swrc::proceedings_volume_type(instance):
    assert isinstance(instance.volume, str)


@given(instance=SWRC::Proceedings_strategy)
def test_swrc::proceedings_volume_setter(instance):
    original = instance.volume
    instance.volume = original
    assert instance.volume == original

@given(instance=SWRC::Proceedings_strategy)
def test_swrc::proceedings_address_type(instance):
    assert isinstance(instance.address, str)


@given(instance=SWRC::Proceedings_strategy)
def test_swrc::proceedings_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original

@given(instance=SWRC::Proceedings_strategy)
def test_swrc::proceedings_series_type(instance):
    assert isinstance(instance.series, str)


@given(instance=SWRC::Proceedings_strategy)
def test_swrc::proceedings_series_setter(instance):
    original = instance.series
    instance.series = original
    assert instance.series == original

@given(instance=SWRC::Proceedings_strategy)
def test_swrc::proceedings_month_type(instance):
    assert isinstance(instance.month, str)


@given(instance=SWRC::Proceedings_strategy)
def test_swrc::proceedings_month_setter(instance):
    original = instance.month
    instance.month = original
    assert instance.month == original

@given(instance=SWRC::Proceedings_strategy)
def test_swrc::proceedings_number_type(instance):
    assert isinstance(instance.number, str)


@given(instance=SWRC::Proceedings_strategy)
def test_swrc::proceedings_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original

@given(instance=SWRC::InProceedings_strategy)
@settings(max_examples=50)
def test_swrc::inproceedings_instantiation(instance):
    assert isinstance(instance, SWRC::InProceedings)

@given(instance=SWRC::InProceedings_strategy)
def test_swrc::inproceedings_volume_type(instance):
    assert isinstance(instance.volume, str)


@given(instance=SWRC::InProceedings_strategy)
def test_swrc::inproceedings_volume_setter(instance):
    original = instance.volume
    instance.volume = original
    assert instance.volume == original

@given(instance=SWRC::InProceedings_strategy)
def test_swrc::inproceedings_month_type(instance):
    assert isinstance(instance.month, str)


@given(instance=SWRC::InProceedings_strategy)
def test_swrc::inproceedings_month_setter(instance):
    original = instance.month
    instance.month = original
    assert instance.month == original

@given(instance=SWRC::InProceedings_strategy)
def test_swrc::inproceedings_series_type(instance):
    assert isinstance(instance.series, str)


@given(instance=SWRC::InProceedings_strategy)
def test_swrc::inproceedings_series_setter(instance):
    original = instance.series
    instance.series = original
    assert instance.series == original

@given(instance=SWRC::InProceedings_strategy)
def test_swrc::inproceedings_booktitle_type(instance):
    assert isinstance(instance.booktitle, str)


@given(instance=SWRC::InProceedings_strategy)
def test_swrc::inproceedings_booktitle_setter(instance):
    original = instance.booktitle
    instance.booktitle = original
    assert instance.booktitle == original

@given(instance=SWRC::InProceedings_strategy)
def test_swrc::inproceedings_pages_type(instance):
    assert isinstance(instance.pages, str)


@given(instance=SWRC::InProceedings_strategy)
def test_swrc::inproceedings_pages_setter(instance):
    original = instance.pages
    instance.pages = original
    assert instance.pages == original

@given(instance=SWRC::InProceedings_strategy)
def test_swrc::inproceedings_number_type(instance):
    assert isinstance(instance.number, str)


@given(instance=SWRC::InProceedings_strategy)
def test_swrc::inproceedings_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original

@given(instance=SWRC::InProceedings_strategy)
def test_swrc::inproceedings_address_type(instance):
    assert isinstance(instance.address, str)


@given(instance=SWRC::InProceedings_strategy)
def test_swrc::inproceedings_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original

@given(instance=SWRC::Book_strategy)
@settings(max_examples=50)
def test_swrc::book_instantiation(instance):
    assert isinstance(instance, SWRC::Book)

@given(instance=SWRC::Book_strategy)
def test_swrc::book_price_type(instance):
    assert isinstance(instance.price, str)


@given(instance=SWRC::Book_strategy)
def test_swrc::book_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original

@given(instance=SWRC::Book_strategy)
def test_swrc::book_series_type(instance):
    assert isinstance(instance.series, str)


@given(instance=SWRC::Book_strategy)
def test_swrc::book_series_setter(instance):
    original = instance.series
    instance.series = original
    assert instance.series == original

@given(instance=SWRC::Book_strategy)
def test_swrc::book_edition_type(instance):
    assert isinstance(instance.edition, str)


@given(instance=SWRC::Book_strategy)
def test_swrc::book_edition_setter(instance):
    original = instance.edition
    instance.edition = original
    assert instance.edition == original

@given(instance=SWRC::Book_strategy)
def test_swrc::book_number_type(instance):
    assert isinstance(instance.number, str)


@given(instance=SWRC::Book_strategy)
def test_swrc::book_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original

@given(instance=SWRC::Book_strategy)
def test_swrc::book_address_type(instance):
    assert isinstance(instance.address, str)


@given(instance=SWRC::Book_strategy)
def test_swrc::book_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original

@given(instance=SWRC::Book_strategy)
def test_swrc::book_month_type(instance):
    assert isinstance(instance.month, str)


@given(instance=SWRC::Book_strategy)
def test_swrc::book_month_setter(instance):
    original = instance.month
    instance.month = original
    assert instance.month == original

@given(instance=SWRC::Book_strategy)
def test_swrc::book_source_type(instance):
    assert isinstance(instance.source, str)


@given(instance=SWRC::Book_strategy)
def test_swrc::book_source_setter(instance):
    original = instance.source
    instance.source = original
    assert instance.source == original

@given(instance=SWRC::Book_strategy)
def test_swrc::book_volume_type(instance):
    assert isinstance(instance.volume, str)


@given(instance=SWRC::Book_strategy)
def test_swrc::book_volume_setter(instance):
    original = instance.volume
    instance.volume = original
    assert instance.volume == original

@given(instance=SWRC::Book_strategy)
def test_swrc::book_isbn_type(instance):
    assert isinstance(instance.isbn, str)


@given(instance=SWRC::Book_strategy)
def test_swrc::book_isbn_setter(instance):
    original = instance.isbn
    instance.isbn = original
    assert instance.isbn == original

@given(instance=SWRC::InCollection_strategy)
@settings(max_examples=50)
def test_swrc::incollection_instantiation(instance):
    assert isinstance(instance, SWRC::InCollection)

@given(instance=SWRC::InCollection_strategy)
def test_swrc::incollection_booktitle_type(instance):
    assert isinstance(instance.booktitle, str)


@given(instance=SWRC::InCollection_strategy)
def test_swrc::incollection_booktitle_setter(instance):
    original = instance.booktitle
    instance.booktitle = original
    assert instance.booktitle == original

@given(instance=SWRC::InCollection_strategy)
def test_swrc::incollection_pages_type(instance):
    assert isinstance(instance.pages, str)


@given(instance=SWRC::InCollection_strategy)
def test_swrc::incollection_pages_setter(instance):
    original = instance.pages
    instance.pages = original
    assert instance.pages == original

@given(instance=SWRC::InCollection_strategy)
def test_swrc::incollection_number_type(instance):
    assert isinstance(instance.number, str)


@given(instance=SWRC::InCollection_strategy)
def test_swrc::incollection_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original

@given(instance=SWRC::InCollection_strategy)
def test_swrc::incollection_month_type(instance):
    assert isinstance(instance.month, str)


@given(instance=SWRC::InCollection_strategy)
def test_swrc::incollection_month_setter(instance):
    original = instance.month
    instance.month = original
    assert instance.month == original

@given(instance=SWRC::InCollection_strategy)
def test_swrc::incollection_chapter_type(instance):
    assert isinstance(instance.chapter, str)


@given(instance=SWRC::InCollection_strategy)
def test_swrc::incollection_chapter_setter(instance):
    original = instance.chapter
    instance.chapter = original
    assert instance.chapter == original

@given(instance=SWRC::InCollection_strategy)
def test_swrc::incollection_series_type(instance):
    assert isinstance(instance.series, str)


@given(instance=SWRC::InCollection_strategy)
def test_swrc::incollection_series_setter(instance):
    original = instance.series
    instance.series = original
    assert instance.series == original

@given(instance=SWRC::InCollection_strategy)
def test_swrc::incollection_volume_type(instance):
    assert isinstance(instance.volume, str)


@given(instance=SWRC::InCollection_strategy)
def test_swrc::incollection_volume_setter(instance):
    original = instance.volume
    instance.volume = original
    assert instance.volume == original

@given(instance=SWRC::InCollection_strategy)
def test_swrc::incollection_address_type(instance):
    assert isinstance(instance.address, str)


@given(instance=SWRC::InCollection_strategy)
def test_swrc::incollection_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original

@given(instance=SWRC::InCollection_strategy)
def test_swrc::incollection_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=SWRC::InCollection_strategy)
def test_swrc::incollection_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=SWRC::InCollection_strategy)
def test_swrc::incollection_edition_type(instance):
    assert isinstance(instance.edition, str)


@given(instance=SWRC::InCollection_strategy)
def test_swrc::incollection_edition_setter(instance):
    original = instance.edition
    instance.edition = original
    assert instance.edition == original

@given(instance=SWRC::InBook_strategy)
@settings(max_examples=50)
def test_swrc::inbook_instantiation(instance):
    assert isinstance(instance, SWRC::InBook)

@given(instance=SWRC::InBook_strategy)
def test_swrc::inbook_number_type(instance):
    assert isinstance(instance.number, str)


@given(instance=SWRC::InBook_strategy)
def test_swrc::inbook_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original

@given(instance=SWRC::InBook_strategy)
def test_swrc::inbook_volume_type(instance):
    assert isinstance(instance.volume, str)


@given(instance=SWRC::InBook_strategy)
def test_swrc::inbook_volume_setter(instance):
    original = instance.volume
    instance.volume = original
    assert instance.volume == original

@given(instance=SWRC::InBook_strategy)
def test_swrc::inbook_address_type(instance):
    assert isinstance(instance.address, str)


@given(instance=SWRC::InBook_strategy)
def test_swrc::inbook_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original

@given(instance=SWRC::InBook_strategy)
def test_swrc::inbook_month_type(instance):
    assert isinstance(instance.month, str)


@given(instance=SWRC::InBook_strategy)
def test_swrc::inbook_month_setter(instance):
    original = instance.month
    instance.month = original
    assert instance.month == original

@given(instance=SWRC::InBook_strategy)
def test_swrc::inbook_series_type(instance):
    assert isinstance(instance.series, str)


@given(instance=SWRC::InBook_strategy)
def test_swrc::inbook_series_setter(instance):
    original = instance.series
    instance.series = original
    assert instance.series == original

@given(instance=SWRC::InBook_strategy)
def test_swrc::inbook_chapter_type(instance):
    assert isinstance(instance.chapter, str)


@given(instance=SWRC::InBook_strategy)
def test_swrc::inbook_chapter_setter(instance):
    original = instance.chapter
    instance.chapter = original
    assert instance.chapter == original

@given(instance=SWRC::InBook_strategy)
def test_swrc::inbook_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=SWRC::InBook_strategy)
def test_swrc::inbook_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=SWRC::InBook_strategy)
def test_swrc::inbook_pages_type(instance):
    assert isinstance(instance.pages, str)


@given(instance=SWRC::InBook_strategy)
def test_swrc::inbook_pages_setter(instance):
    original = instance.pages
    instance.pages = original
    assert instance.pages == original

@given(instance=SWRC::Unpublished_strategy)
@settings(max_examples=50)
def test_swrc::unpublished_instantiation(instance):
    assert isinstance(instance, SWRC::Unpublished)

@given(instance=SWRC::Unpublished_strategy)
def test_swrc::unpublished_month_type(instance):
    assert isinstance(instance.month, str)


@given(instance=SWRC::Unpublished_strategy)
def test_swrc::unpublished_month_setter(instance):
    original = instance.month
    instance.month = original
    assert instance.month == original

@given(instance=SWRC::Misc_strategy)
@settings(max_examples=50)
def test_swrc::misc_instantiation(instance):
    assert isinstance(instance, SWRC::Misc)

@given(instance=SWRC::Misc_strategy)
def test_swrc::misc_howpublished_type(instance):
    assert isinstance(instance.howpublished, str)


@given(instance=SWRC::Misc_strategy)
def test_swrc::misc_howpublished_setter(instance):
    original = instance.howpublished
    instance.howpublished = original
    assert instance.howpublished == original

@given(instance=SWRC::Misc_strategy)
def test_swrc::misc_month_type(instance):
    assert isinstance(instance.month, str)


@given(instance=SWRC::Misc_strategy)
def test_swrc::misc_month_setter(instance):
    original = instance.month
    instance.month = original
    assert instance.month == original

@given(instance=SWRC::Report_strategy)
@settings(max_examples=50)
def test_swrc::report_instantiation(instance):
    assert isinstance(instance, SWRC::Report)

@given(instance=SWRC::Article_strategy)
@settings(max_examples=50)
def test_swrc::article_instantiation(instance):
    assert isinstance(instance, SWRC::Article)

@given(instance=SWRC::Article_strategy)
def test_swrc::article_volume_type(instance):
    assert isinstance(instance.volume, str)


@given(instance=SWRC::Article_strategy)
def test_swrc::article_volume_setter(instance):
    original = instance.volume
    instance.volume = original
    assert instance.volume == original

@given(instance=SWRC::Article_strategy)
def test_swrc::article_journal_type(instance):
    assert isinstance(instance.journal, str)


@given(instance=SWRC::Article_strategy)
def test_swrc::article_journal_setter(instance):
    original = instance.journal
    instance.journal = original
    assert instance.journal == original

@given(instance=SWRC::Article_strategy)
def test_swrc::article_month_type(instance):
    assert isinstance(instance.month, str)


@given(instance=SWRC::Article_strategy)
def test_swrc::article_month_setter(instance):
    original = instance.month
    instance.month = original
    assert instance.month == original

@given(instance=SWRC::Article_strategy)
def test_swrc::article_number_type(instance):
    assert isinstance(instance.number, str)


@given(instance=SWRC::Article_strategy)
def test_swrc::article_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original

@given(instance=SWRC::Article_strategy)
def test_swrc::article_pages_type(instance):
    assert isinstance(instance.pages, str)


@given(instance=SWRC::Article_strategy)
def test_swrc::article_pages_setter(instance):
    original = instance.pages
    instance.pages = original
    assert instance.pages == original

@given(instance=SWRC::Publication_strategy)
@settings(max_examples=50)
def test_swrc::publication_instantiation(instance):
    assert isinstance(instance, SWRC::Publication)

@given(instance=SWRC::Publication_strategy)
def test_swrc::publication_year_type(instance):
    assert isinstance(instance.year, str)


@given(instance=SWRC::Publication_strategy)
def test_swrc::publication_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original

@given(instance=SWRC::Publication_strategy)
def test_swrc::publication_note_type(instance):
    assert isinstance(instance.note, str)


@given(instance=SWRC::Publication_strategy)
def test_swrc::publication_note_setter(instance):
    original = instance.note
    instance.note = original
    assert instance.note == original

@given(instance=SWRC::Publication_strategy)
def test_swrc::publication_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=SWRC::Publication_strategy)
def test_swrc::publication_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=SWRC::Publication_strategy)
def test_swrc::publication_abstract_type(instance):
    assert isinstance(instance.abstract, str)


@given(instance=SWRC::Publication_strategy)
def test_swrc::publication_abstract_setter(instance):
    original = instance.abstract
    instance.abstract = original
    assert instance.abstract == original

@given(instance=SWRC::Publication_strategy)
def test_swrc::publication_keywords_type(instance):
    assert isinstance(instance.keywords, str)


@given(instance=SWRC::Publication_strategy)
def test_swrc::publication_keywords_setter(instance):
    original = instance.keywords
    instance.keywords = original
    assert instance.keywords == original

@given(instance=SWRC::Bibliography_strategy)
@settings(max_examples=50)
def test_swrc::bibliography_instantiation(instance):
    assert isinstance(instance, SWRC::Bibliography)
