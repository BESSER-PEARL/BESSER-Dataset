import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Requirement,
    Attendance,
    Login,
    Position,
    Registration,
    Admin,
    Applicant,
    Assessment__Self_Assessment,
    Assessment,
    Performance,
    Survey,
    New_Employee,
    Task,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_requirement_is_not_abstract():
    assert not inspect.isabstract(Requirement)


def test_requirement_constructor_exists():
    assert callable(Requirement.__init__)


def test_requirement_constructor_args():
    sig = inspect.signature(Requirement.__init__)
    params = list(sig.parameters.keys())
    assert "Photo" in params, "Missing parameter 'Photo'"
    assert "Curriculum_Vitae" in params, "Missing parameter 'Curriculum_Vitae'"
    assert "ID_Card" in params, "Missing parameter 'ID_Card'"
    assert "Diploma" in params, "Missing parameter 'Diploma'"
    assert "Transcript" in params, "Missing parameter 'Transcript'"

def test_requirement_has_Photo():
    assert hasattr(Requirement, "Photo")
    descriptor = None
    for klass in Requirement.__mro__:
        if "Photo" in klass.__dict__:
            descriptor = klass.__dict__["Photo"]
            break
    assert isinstance(descriptor, property)

def test_requirement_has_Curriculum_Vitae():
    assert hasattr(Requirement, "Curriculum_Vitae")
    descriptor = None
    for klass in Requirement.__mro__:
        if "Curriculum_Vitae" in klass.__dict__:
            descriptor = klass.__dict__["Curriculum_Vitae"]
            break
    assert isinstance(descriptor, property)

def test_requirement_has_ID_Card():
    assert hasattr(Requirement, "ID_Card")
    descriptor = None
    for klass in Requirement.__mro__:
        if "ID_Card" in klass.__dict__:
            descriptor = klass.__dict__["ID_Card"]
            break
    assert isinstance(descriptor, property)

def test_requirement_has_Diploma():
    assert hasattr(Requirement, "Diploma")
    descriptor = None
    for klass in Requirement.__mro__:
        if "Diploma" in klass.__dict__:
            descriptor = klass.__dict__["Diploma"]
            break
    assert isinstance(descriptor, property)

def test_requirement_has_Transcript():
    assert hasattr(Requirement, "Transcript")
    descriptor = None
    for klass in Requirement.__mro__:
        if "Transcript" in klass.__dict__:
            descriptor = klass.__dict__["Transcript"]
            break
    assert isinstance(descriptor, property)



def test_attendance_is_not_abstract():
    assert not inspect.isabstract(Attendance)


def test_attendance_constructor_exists():
    assert callable(Attendance.__init__)


def test_attendance_constructor_args():
    sig = inspect.signature(Attendance.__init__)
    params = list(sig.parameters.keys())
    assert "Date___Time" in params, "Missing parameter 'Date___Time'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Position" in params, "Missing parameter 'Position'"
    assert "Details" in params, "Missing parameter 'Details'"

def test_attendance_has_Date___Time():
    assert hasattr(Attendance, "Date___Time")
    descriptor = None
    for klass in Attendance.__mro__:
        if "Date___Time" in klass.__dict__:
            descriptor = klass.__dict__["Date___Time"]
            break
    assert isinstance(descriptor, property)

def test_attendance_has_Name():
    assert hasattr(Attendance, "Name")
    descriptor = None
    for klass in Attendance.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_attendance_has_Position():
    assert hasattr(Attendance, "Position")
    descriptor = None
    for klass in Attendance.__mro__:
        if "Position" in klass.__dict__:
            descriptor = klass.__dict__["Position"]
            break
    assert isinstance(descriptor, property)

def test_attendance_has_Details():
    assert hasattr(Attendance, "Details")
    descriptor = None
    for klass in Attendance.__mro__:
        if "Details" in klass.__dict__:
            descriptor = klass.__dict__["Details"]
            break
    assert isinstance(descriptor, property)



def test_login_is_not_abstract():
    assert not inspect.isabstract(Login)


def test_login_constructor_exists():
    assert callable(Login.__init__)


def test_login_constructor_args():
    sig = inspect.signature(Login.__init__)
    params = list(sig.parameters.keys())
    assert "password" in params, "Missing parameter 'password'"
    assert "userid" in params, "Missing parameter 'userid'"

def test_login_has_password():
    assert hasattr(Login, "password")
    descriptor = None
    for klass in Login.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)

def test_login_has_userid():
    assert hasattr(Login, "userid")
    descriptor = None
    for klass in Login.__mro__:
        if "userid" in klass.__dict__:
            descriptor = klass.__dict__["userid"]
            break
    assert isinstance(descriptor, property)



def test_position_is_not_abstract():
    assert not inspect.isabstract(Position)


def test_position_constructor_exists():
    assert callable(Position.__init__)


def test_position_constructor_args():
    sig = inspect.signature(Position.__init__)
    params = list(sig.parameters.keys())
    assert "jobID" in params, "Missing parameter 'jobID'"
    assert "positionID" in params, "Missing parameter 'positionID'"
    assert "positionName" in params, "Missing parameter 'positionName'"
    assert "divisionName" in params, "Missing parameter 'divisionName'"

def test_position_has_jobID():
    assert hasattr(Position, "jobID")
    descriptor = None
    for klass in Position.__mro__:
        if "jobID" in klass.__dict__:
            descriptor = klass.__dict__["jobID"]
            break
    assert isinstance(descriptor, property)

def test_position_has_positionID():
    assert hasattr(Position, "positionID")
    descriptor = None
    for klass in Position.__mro__:
        if "positionID" in klass.__dict__:
            descriptor = klass.__dict__["positionID"]
            break
    assert isinstance(descriptor, property)

def test_position_has_positionName():
    assert hasattr(Position, "positionName")
    descriptor = None
    for klass in Position.__mro__:
        if "positionName" in klass.__dict__:
            descriptor = klass.__dict__["positionName"]
            break
    assert isinstance(descriptor, property)

def test_position_has_divisionName():
    assert hasattr(Position, "divisionName")
    descriptor = None
    for klass in Position.__mro__:
        if "divisionName" in klass.__dict__:
            descriptor = klass.__dict__["divisionName"]
            break
    assert isinstance(descriptor, property)



def test_registration_is_not_abstract():
    assert not inspect.isabstract(Registration)


def test_registration_constructor_exists():
    assert callable(Registration.__init__)


def test_registration_constructor_args():
    sig = inspect.signature(Registration.__init__)
    params = list(sig.parameters.keys())
    assert "Address" in params, "Missing parameter 'Address'"
    assert "Email" in params, "Missing parameter 'Email'"
    assert "Date" in params, "Missing parameter 'Date'"
    assert "Position_Type" in params, "Missing parameter 'Position_Type'"
    assert "Applied_Position" in params, "Missing parameter 'Applied_Position'"
    assert "Phone" in params, "Missing parameter 'Phone'"
    assert "Skills___Requirement" in params, "Missing parameter 'Skills___Requirement'"
    assert "Name" in params, "Missing parameter 'Name'"

def test_registration_has_Address():
    assert hasattr(Registration, "Address")
    descriptor = None
    for klass in Registration.__mro__:
        if "Address" in klass.__dict__:
            descriptor = klass.__dict__["Address"]
            break
    assert isinstance(descriptor, property)

def test_registration_has_Email():
    assert hasattr(Registration, "Email")
    descriptor = None
    for klass in Registration.__mro__:
        if "Email" in klass.__dict__:
            descriptor = klass.__dict__["Email"]
            break
    assert isinstance(descriptor, property)

def test_registration_has_Date():
    assert hasattr(Registration, "Date")
    descriptor = None
    for klass in Registration.__mro__:
        if "Date" in klass.__dict__:
            descriptor = klass.__dict__["Date"]
            break
    assert isinstance(descriptor, property)

def test_registration_has_Position_Type():
    assert hasattr(Registration, "Position_Type")
    descriptor = None
    for klass in Registration.__mro__:
        if "Position_Type" in klass.__dict__:
            descriptor = klass.__dict__["Position_Type"]
            break
    assert isinstance(descriptor, property)

def test_registration_has_Applied_Position():
    assert hasattr(Registration, "Applied_Position")
    descriptor = None
    for klass in Registration.__mro__:
        if "Applied_Position" in klass.__dict__:
            descriptor = klass.__dict__["Applied_Position"]
            break
    assert isinstance(descriptor, property)

def test_registration_has_Phone():
    assert hasattr(Registration, "Phone")
    descriptor = None
    for klass in Registration.__mro__:
        if "Phone" in klass.__dict__:
            descriptor = klass.__dict__["Phone"]
            break
    assert isinstance(descriptor, property)

def test_registration_has_Skills___Requirement():
    assert hasattr(Registration, "Skills___Requirement")
    descriptor = None
    for klass in Registration.__mro__:
        if "Skills___Requirement" in klass.__dict__:
            descriptor = klass.__dict__["Skills___Requirement"]
            break
    assert isinstance(descriptor, property)

def test_registration_has_Name():
    assert hasattr(Registration, "Name")
    descriptor = None
    for klass in Registration.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_admin_is_not_abstract():
    assert not inspect.isabstract(Admin)


def test_admin_constructor_exists():
    assert callable(Admin.__init__)


def test_admin_constructor_args():
    sig = inspect.signature(Admin.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "address" in params, "Missing parameter 'address'"
    assert "qualification" in params, "Missing parameter 'qualification'"

def test_admin_has_name():
    assert hasattr(Admin, "name")
    descriptor = None
    for klass in Admin.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_admin_has_address():
    assert hasattr(Admin, "address")
    descriptor = None
    for klass in Admin.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)

def test_admin_has_qualification():
    assert hasattr(Admin, "qualification")
    descriptor = None
    for klass in Admin.__mro__:
        if "qualification" in klass.__dict__:
            descriptor = klass.__dict__["qualification"]
            break
    assert isinstance(descriptor, property)



def test_applicant_is_not_abstract():
    assert not inspect.isabstract(Applicant)


def test_applicant_constructor_exists():
    assert callable(Applicant.__init__)


def test_applicant_constructor_args():
    sig = inspect.signature(Applicant.__init__)
    params = list(sig.parameters.keys())
    assert "Phone" in params, "Missing parameter 'Phone'"
    assert "Email" in params, "Missing parameter 'Email'"
    assert "Date_of_Birth" in params, "Missing parameter 'Date_of_Birth'"
    assert "Last_Name" in params, "Missing parameter 'Last_Name'"
    assert "Applied_Position" in params, "Missing parameter 'Applied_Position'"
    assert "Password" in params, "Missing parameter 'Password'"
    assert "First_Name" in params, "Missing parameter 'First_Name'"
    assert "Address" in params, "Missing parameter 'Address'"

def test_applicant_has_Phone():
    assert hasattr(Applicant, "Phone")
    descriptor = None
    for klass in Applicant.__mro__:
        if "Phone" in klass.__dict__:
            descriptor = klass.__dict__["Phone"]
            break
    assert isinstance(descriptor, property)

def test_applicant_has_Email():
    assert hasattr(Applicant, "Email")
    descriptor = None
    for klass in Applicant.__mro__:
        if "Email" in klass.__dict__:
            descriptor = klass.__dict__["Email"]
            break
    assert isinstance(descriptor, property)

def test_applicant_has_Date_of_Birth():
    assert hasattr(Applicant, "Date_of_Birth")
    descriptor = None
    for klass in Applicant.__mro__:
        if "Date_of_Birth" in klass.__dict__:
            descriptor = klass.__dict__["Date_of_Birth"]
            break
    assert isinstance(descriptor, property)

def test_applicant_has_Last_Name():
    assert hasattr(Applicant, "Last_Name")
    descriptor = None
    for klass in Applicant.__mro__:
        if "Last_Name" in klass.__dict__:
            descriptor = klass.__dict__["Last_Name"]
            break
    assert isinstance(descriptor, property)

def test_applicant_has_Applied_Position():
    assert hasattr(Applicant, "Applied_Position")
    descriptor = None
    for klass in Applicant.__mro__:
        if "Applied_Position" in klass.__dict__:
            descriptor = klass.__dict__["Applied_Position"]
            break
    assert isinstance(descriptor, property)

def test_applicant_has_Password():
    assert hasattr(Applicant, "Password")
    descriptor = None
    for klass in Applicant.__mro__:
        if "Password" in klass.__dict__:
            descriptor = klass.__dict__["Password"]
            break
    assert isinstance(descriptor, property)

def test_applicant_has_First_Name():
    assert hasattr(Applicant, "First_Name")
    descriptor = None
    for klass in Applicant.__mro__:
        if "First_Name" in klass.__dict__:
            descriptor = klass.__dict__["First_Name"]
            break
    assert isinstance(descriptor, property)

def test_applicant_has_Address():
    assert hasattr(Applicant, "Address")
    descriptor = None
    for klass in Applicant.__mro__:
        if "Address" in klass.__dict__:
            descriptor = klass.__dict__["Address"]
            break
    assert isinstance(descriptor, property)



def test_assessment__self_assessment_is_not_abstract():
    assert not inspect.isabstract(Assessment__Self_Assessment)


def test_assessment__self_assessment_constructor_exists():
    assert callable(Assessment__Self_Assessment.__init__)


def test_assessment__self_assessment_constructor_args():
    sig = inspect.signature(Assessment__Self_Assessment.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Score" in params, "Missing parameter 'Score'"
    assert "Question" in params, "Missing parameter 'Question'"

def test_assessment__self_assessment_has_Name():
    assert hasattr(Assessment__Self_Assessment, "Name")
    descriptor = None
    for klass in Assessment__Self_Assessment.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_assessment__self_assessment_has_Score():
    assert hasattr(Assessment__Self_Assessment, "Score")
    descriptor = None
    for klass in Assessment__Self_Assessment.__mro__:
        if "Score" in klass.__dict__:
            descriptor = klass.__dict__["Score"]
            break
    assert isinstance(descriptor, property)

def test_assessment__self_assessment_has_Question():
    assert hasattr(Assessment__Self_Assessment, "Question")
    descriptor = None
    for klass in Assessment__Self_Assessment.__mro__:
        if "Question" in klass.__dict__:
            descriptor = klass.__dict__["Question"]
            break
    assert isinstance(descriptor, property)



def test_assessment_is_not_abstract():
    assert not inspect.isabstract(Assessment)


def test_assessment_constructor_exists():
    assert callable(Assessment.__init__)


def test_assessment_constructor_args():
    sig = inspect.signature(Assessment.__init__)
    params = list(sig.parameters.keys())
    assert "Type_of_Assessment" in params, "Missing parameter 'Type_of_Assessment'"
    assert "Total_Score" in params, "Missing parameter 'Total_Score'"
    assert "Name" in params, "Missing parameter 'Name'"

def test_assessment_has_Type_of_Assessment():
    assert hasattr(Assessment, "Type_of_Assessment")
    descriptor = None
    for klass in Assessment.__mro__:
        if "Type_of_Assessment" in klass.__dict__:
            descriptor = klass.__dict__["Type_of_Assessment"]
            break
    assert isinstance(descriptor, property)

def test_assessment_has_Total_Score():
    assert hasattr(Assessment, "Total_Score")
    descriptor = None
    for klass in Assessment.__mro__:
        if "Total_Score" in klass.__dict__:
            descriptor = klass.__dict__["Total_Score"]
            break
    assert isinstance(descriptor, property)

def test_assessment_has_Name():
    assert hasattr(Assessment, "Name")
    descriptor = None
    for klass in Assessment.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_performance_is_not_abstract():
    assert not inspect.isabstract(Performance)


def test_performance_constructor_exists():
    assert callable(Performance.__init__)


def test_performance_constructor_args():
    sig = inspect.signature(Performance.__init__)
    params = list(sig.parameters.keys())
    assert "Coordination" in params, "Missing parameter 'Coordination'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Target" in params, "Missing parameter 'Target'"
    assert "Punctuality" in params, "Missing parameter 'Punctuality'"

def test_performance_has_Coordination():
    assert hasattr(Performance, "Coordination")
    descriptor = None
    for klass in Performance.__mro__:
        if "Coordination" in klass.__dict__:
            descriptor = klass.__dict__["Coordination"]
            break
    assert isinstance(descriptor, property)

def test_performance_has_Name():
    assert hasattr(Performance, "Name")
    descriptor = None
    for klass in Performance.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_performance_has_Target():
    assert hasattr(Performance, "Target")
    descriptor = None
    for klass in Performance.__mro__:
        if "Target" in klass.__dict__:
            descriptor = klass.__dict__["Target"]
            break
    assert isinstance(descriptor, property)

def test_performance_has_Punctuality():
    assert hasattr(Performance, "Punctuality")
    descriptor = None
    for klass in Performance.__mro__:
        if "Punctuality" in klass.__dict__:
            descriptor = klass.__dict__["Punctuality"]
            break
    assert isinstance(descriptor, property)



def test_survey_is_not_abstract():
    assert not inspect.isabstract(Survey)


def test_survey_constructor_exists():
    assert callable(Survey.__init__)


def test_survey_constructor_args():
    sig = inspect.signature(Survey.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Score" in params, "Missing parameter 'Score'"
    assert "Question" in params, "Missing parameter 'Question'"

def test_survey_has_Name():
    assert hasattr(Survey, "Name")
    descriptor = None
    for klass in Survey.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_survey_has_Score():
    assert hasattr(Survey, "Score")
    descriptor = None
    for klass in Survey.__mro__:
        if "Score" in klass.__dict__:
            descriptor = klass.__dict__["Score"]
            break
    assert isinstance(descriptor, property)

def test_survey_has_Question():
    assert hasattr(Survey, "Question")
    descriptor = None
    for klass in Survey.__mro__:
        if "Question" in klass.__dict__:
            descriptor = klass.__dict__["Question"]
            break
    assert isinstance(descriptor, property)



def test_new_employee_is_not_abstract():
    assert not inspect.isabstract(New_Employee)


def test_new_employee_constructor_exists():
    assert callable(New_Employee.__init__)


def test_new_employee_constructor_args():
    sig = inspect.signature(New_Employee.__init__)
    params = list(sig.parameters.keys())
    assert "Position" in params, "Missing parameter 'Position'"
    assert "Date_of_Birth" in params, "Missing parameter 'Date_of_Birth'"
    assert "Division" in params, "Missing parameter 'Division'"
    assert "Working_Since" in params, "Missing parameter 'Working_Since'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Place_of_Birth" in params, "Missing parameter 'Place_of_Birth'"

def test_new_employee_has_Position():
    assert hasattr(New_Employee, "Position")
    descriptor = None
    for klass in New_Employee.__mro__:
        if "Position" in klass.__dict__:
            descriptor = klass.__dict__["Position"]
            break
    assert isinstance(descriptor, property)

def test_new_employee_has_Date_of_Birth():
    assert hasattr(New_Employee, "Date_of_Birth")
    descriptor = None
    for klass in New_Employee.__mro__:
        if "Date_of_Birth" in klass.__dict__:
            descriptor = klass.__dict__["Date_of_Birth"]
            break
    assert isinstance(descriptor, property)

def test_new_employee_has_Division():
    assert hasattr(New_Employee, "Division")
    descriptor = None
    for klass in New_Employee.__mro__:
        if "Division" in klass.__dict__:
            descriptor = klass.__dict__["Division"]
            break
    assert isinstance(descriptor, property)

def test_new_employee_has_Working_Since():
    assert hasattr(New_Employee, "Working_Since")
    descriptor = None
    for klass in New_Employee.__mro__:
        if "Working_Since" in klass.__dict__:
            descriptor = klass.__dict__["Working_Since"]
            break
    assert isinstance(descriptor, property)

def test_new_employee_has_Name():
    assert hasattr(New_Employee, "Name")
    descriptor = None
    for klass in New_Employee.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_new_employee_has_Place_of_Birth():
    assert hasattr(New_Employee, "Place_of_Birth")
    descriptor = None
    for klass in New_Employee.__mro__:
        if "Place_of_Birth" in klass.__dict__:
            descriptor = klass.__dict__["Place_of_Birth"]
            break
    assert isinstance(descriptor, property)



def test_task_is_not_abstract():
    assert not inspect.isabstract(Task)


def test_task_constructor_exists():
    assert callable(Task.__init__)


def test_task_constructor_args():
    sig = inspect.signature(Task.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Task_Detail" in params, "Missing parameter 'Task_Detail'"
    assert "Deadline" in params, "Missing parameter 'Deadline'"
    assert "Task_Name" in params, "Missing parameter 'Task_Name'"

def test_task_has_Name():
    assert hasattr(Task, "Name")
    descriptor = None
    for klass in Task.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_task_has_Task_Detail():
    assert hasattr(Task, "Task_Detail")
    descriptor = None
    for klass in Task.__mro__:
        if "Task_Detail" in klass.__dict__:
            descriptor = klass.__dict__["Task_Detail"]
            break
    assert isinstance(descriptor, property)

def test_task_has_Deadline():
    assert hasattr(Task, "Deadline")
    descriptor = None
    for klass in Task.__mro__:
        if "Deadline" in klass.__dict__:
            descriptor = klass.__dict__["Deadline"]
            break
    assert isinstance(descriptor, property)

def test_task_has_Task_Name():
    assert hasattr(Task, "Task_Name")
    descriptor = None
    for klass in Task.__mro__:
        if "Task_Name" in klass.__dict__:
            descriptor = klass.__dict__["Task_Name"]
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
Requirement_strategy = st.builds(
    Requirement,
    Photo=
        safe_text,
    Curriculum_Vitae=
        safe_text,
    ID_Card=
        safe_text,
    Diploma=
        safe_text,
    Transcript=
        safe_text
)
Attendance_strategy = st.builds(
    Attendance,
    Date___Time=
        safe_text,
    Name=
        safe_text,
    Position=
        safe_text,
    Details=
        safe_text
)
Login_strategy = st.builds(
    Login,
    password=
        safe_text,
    userid=
        safe_text
)
Position_strategy = st.builds(
    Position,
    jobID=
        safe_text,
    positionID=
        st.integers(),
    positionName=
        safe_text,
    divisionName=
        safe_text
)
Registration_strategy = st.builds(
    Registration,
    Address=
        safe_text,
    Email=
        safe_text,
    Date=
        safe_text,
    Position_Type=
        safe_text,
    Applied_Position=
        safe_text,
    Phone=
        safe_text,
    Skills___Requirement=
        safe_text,
    Name=
        safe_text
)
Admin_strategy = st.builds(
    Admin,
    name=
        safe_text,
    address=
        safe_text,
    qualification=
        safe_text
)
Applicant_strategy = st.builds(
    Applicant,
    Phone=
        safe_text,
    Email=
        safe_text,
    Date_of_Birth=
        safe_text,
    Last_Name=
        safe_text,
    Applied_Position=
        safe_text,
    Password=
        safe_text,
    First_Name=
        safe_text,
    Address=
        safe_text
)
Assessment__Self_Assessment_strategy = st.builds(
    Assessment__Self_Assessment,
    Name=
        safe_text,
    Score=
        safe_text,
    Question=
        safe_text
)
Assessment_strategy = st.builds(
    Assessment,
    Type_of_Assessment=
        safe_text,
    Total_Score=
        safe_text,
    Name=
        safe_text
)
Performance_strategy = st.builds(
    Performance,
    Coordination=
        safe_text,
    Name=
        safe_text,
    Target=
        safe_text,
    Punctuality=
        safe_text
)
Survey_strategy = st.builds(
    Survey,
    Name=
        safe_text,
    Score=
        safe_text,
    Question=
        safe_text
)
New_Employee_strategy = st.builds(
    New_Employee,
    Position=
        safe_text,
    Date_of_Birth=
        safe_text,
    Division=
        safe_text,
    Working_Since=
        safe_text,
    Name=
        safe_text,
    Place_of_Birth=
        safe_text
)
Task_strategy = st.builds(
    Task,
    Name=
        safe_text,
    Task_Detail=
        safe_text,
    Deadline=
        safe_text,
    Task_Name=
        safe_text
)

@given(instance=Requirement_strategy)
@settings(max_examples=50)
def test_requirement_instantiation(instance):
    assert isinstance(instance, Requirement)



@given(instance=Requirement_strategy)
def test_requirement_Photo_setter(instance):
    original = instance.Photo
    instance.Photo = original
    assert instance.Photo == original



@given(instance=Requirement_strategy)
def test_requirement_Curriculum_Vitae_setter(instance):
    original = instance.Curriculum_Vitae
    instance.Curriculum_Vitae = original
    assert instance.Curriculum_Vitae == original



@given(instance=Requirement_strategy)
def test_requirement_ID_Card_setter(instance):
    original = instance.ID_Card
    instance.ID_Card = original
    assert instance.ID_Card == original



@given(instance=Requirement_strategy)
def test_requirement_Diploma_setter(instance):
    original = instance.Diploma
    instance.Diploma = original
    assert instance.Diploma == original



@given(instance=Requirement_strategy)
def test_requirement_Transcript_setter(instance):
    original = instance.Transcript
    instance.Transcript = original
    assert instance.Transcript == original

@given(instance=Attendance_strategy)
@settings(max_examples=50)
def test_attendance_instantiation(instance):
    assert isinstance(instance, Attendance)



@given(instance=Attendance_strategy)
def test_attendance_Date___Time_setter(instance):
    original = instance.Date___Time
    instance.Date___Time = original
    assert instance.Date___Time == original



@given(instance=Attendance_strategy)
def test_attendance_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=Attendance_strategy)
def test_attendance_Position_setter(instance):
    original = instance.Position
    instance.Position = original
    assert instance.Position == original



@given(instance=Attendance_strategy)
def test_attendance_Details_setter(instance):
    original = instance.Details
    instance.Details = original
    assert instance.Details == original

@given(instance=Login_strategy)
@settings(max_examples=50)
def test_login_instantiation(instance):
    assert isinstance(instance, Login)



@given(instance=Login_strategy)
def test_login_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=Login_strategy)
def test_login_userid_setter(instance):
    original = instance.userid
    instance.userid = original
    assert instance.userid == original

@given(instance=Position_strategy)
@settings(max_examples=50)
def test_position_instantiation(instance):
    assert isinstance(instance, Position)



@given(instance=Position_strategy)
def test_position_jobID_setter(instance):
    original = instance.jobID
    instance.jobID = original
    assert instance.jobID == original



@given(instance=Position_strategy)
def test_position_positionID_setter(instance):
    original = instance.positionID
    instance.positionID = original
    assert instance.positionID == original



@given(instance=Position_strategy)
def test_position_positionName_setter(instance):
    original = instance.positionName
    instance.positionName = original
    assert instance.positionName == original



@given(instance=Position_strategy)
def test_position_divisionName_setter(instance):
    original = instance.divisionName
    instance.divisionName = original
    assert instance.divisionName == original

@given(instance=Registration_strategy)
@settings(max_examples=50)
def test_registration_instantiation(instance):
    assert isinstance(instance, Registration)



@given(instance=Registration_strategy)
def test_registration_Address_setter(instance):
    original = instance.Address
    instance.Address = original
    assert instance.Address == original



@given(instance=Registration_strategy)
def test_registration_Email_setter(instance):
    original = instance.Email
    instance.Email = original
    assert instance.Email == original



@given(instance=Registration_strategy)
def test_registration_Date_setter(instance):
    original = instance.Date
    instance.Date = original
    assert instance.Date == original



@given(instance=Registration_strategy)
def test_registration_Position_Type_setter(instance):
    original = instance.Position_Type
    instance.Position_Type = original
    assert instance.Position_Type == original



@given(instance=Registration_strategy)
def test_registration_Applied_Position_setter(instance):
    original = instance.Applied_Position
    instance.Applied_Position = original
    assert instance.Applied_Position == original



@given(instance=Registration_strategy)
def test_registration_Phone_setter(instance):
    original = instance.Phone
    instance.Phone = original
    assert instance.Phone == original



@given(instance=Registration_strategy)
def test_registration_Skills___Requirement_setter(instance):
    original = instance.Skills___Requirement
    instance.Skills___Requirement = original
    assert instance.Skills___Requirement == original



@given(instance=Registration_strategy)
def test_registration_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=Admin_strategy)
@settings(max_examples=50)
def test_admin_instantiation(instance):
    assert isinstance(instance, Admin)



@given(instance=Admin_strategy)
def test_admin_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Admin_strategy)
def test_admin_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=Admin_strategy)
def test_admin_qualification_setter(instance):
    original = instance.qualification
    instance.qualification = original
    assert instance.qualification == original

@given(instance=Applicant_strategy)
@settings(max_examples=50)
def test_applicant_instantiation(instance):
    assert isinstance(instance, Applicant)



@given(instance=Applicant_strategy)
def test_applicant_Phone_setter(instance):
    original = instance.Phone
    instance.Phone = original
    assert instance.Phone == original



@given(instance=Applicant_strategy)
def test_applicant_Email_setter(instance):
    original = instance.Email
    instance.Email = original
    assert instance.Email == original



@given(instance=Applicant_strategy)
def test_applicant_Date_of_Birth_setter(instance):
    original = instance.Date_of_Birth
    instance.Date_of_Birth = original
    assert instance.Date_of_Birth == original



@given(instance=Applicant_strategy)
def test_applicant_Last_Name_setter(instance):
    original = instance.Last_Name
    instance.Last_Name = original
    assert instance.Last_Name == original



@given(instance=Applicant_strategy)
def test_applicant_Applied_Position_setter(instance):
    original = instance.Applied_Position
    instance.Applied_Position = original
    assert instance.Applied_Position == original



@given(instance=Applicant_strategy)
def test_applicant_Password_setter(instance):
    original = instance.Password
    instance.Password = original
    assert instance.Password == original



@given(instance=Applicant_strategy)
def test_applicant_First_Name_setter(instance):
    original = instance.First_Name
    instance.First_Name = original
    assert instance.First_Name == original



@given(instance=Applicant_strategy)
def test_applicant_Address_setter(instance):
    original = instance.Address
    instance.Address = original
    assert instance.Address == original

@given(instance=Assessment__Self_Assessment_strategy)
@settings(max_examples=50)
def test_assessment__self_assessment_instantiation(instance):
    assert isinstance(instance, Assessment__Self_Assessment)



@given(instance=Assessment__Self_Assessment_strategy)
def test_assessment__self_assessment_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=Assessment__Self_Assessment_strategy)
def test_assessment__self_assessment_Score_setter(instance):
    original = instance.Score
    instance.Score = original
    assert instance.Score == original



@given(instance=Assessment__Self_Assessment_strategy)
def test_assessment__self_assessment_Question_setter(instance):
    original = instance.Question
    instance.Question = original
    assert instance.Question == original

@given(instance=Assessment_strategy)
@settings(max_examples=50)
def test_assessment_instantiation(instance):
    assert isinstance(instance, Assessment)



@given(instance=Assessment_strategy)
def test_assessment_Type_of_Assessment_setter(instance):
    original = instance.Type_of_Assessment
    instance.Type_of_Assessment = original
    assert instance.Type_of_Assessment == original



@given(instance=Assessment_strategy)
def test_assessment_Total_Score_setter(instance):
    original = instance.Total_Score
    instance.Total_Score = original
    assert instance.Total_Score == original



@given(instance=Assessment_strategy)
def test_assessment_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=Performance_strategy)
@settings(max_examples=50)
def test_performance_instantiation(instance):
    assert isinstance(instance, Performance)



@given(instance=Performance_strategy)
def test_performance_Coordination_setter(instance):
    original = instance.Coordination
    instance.Coordination = original
    assert instance.Coordination == original



@given(instance=Performance_strategy)
def test_performance_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=Performance_strategy)
def test_performance_Target_setter(instance):
    original = instance.Target
    instance.Target = original
    assert instance.Target == original



@given(instance=Performance_strategy)
def test_performance_Punctuality_setter(instance):
    original = instance.Punctuality
    instance.Punctuality = original
    assert instance.Punctuality == original

@given(instance=Survey_strategy)
@settings(max_examples=50)
def test_survey_instantiation(instance):
    assert isinstance(instance, Survey)



@given(instance=Survey_strategy)
def test_survey_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=Survey_strategy)
def test_survey_Score_setter(instance):
    original = instance.Score
    instance.Score = original
    assert instance.Score == original



@given(instance=Survey_strategy)
def test_survey_Question_setter(instance):
    original = instance.Question
    instance.Question = original
    assert instance.Question == original

@given(instance=New_Employee_strategy)
@settings(max_examples=50)
def test_new_employee_instantiation(instance):
    assert isinstance(instance, New_Employee)



@given(instance=New_Employee_strategy)
def test_new_employee_Position_setter(instance):
    original = instance.Position
    instance.Position = original
    assert instance.Position == original



@given(instance=New_Employee_strategy)
def test_new_employee_Date_of_Birth_setter(instance):
    original = instance.Date_of_Birth
    instance.Date_of_Birth = original
    assert instance.Date_of_Birth == original



@given(instance=New_Employee_strategy)
def test_new_employee_Division_setter(instance):
    original = instance.Division
    instance.Division = original
    assert instance.Division == original



@given(instance=New_Employee_strategy)
def test_new_employee_Working_Since_setter(instance):
    original = instance.Working_Since
    instance.Working_Since = original
    assert instance.Working_Since == original



@given(instance=New_Employee_strategy)
def test_new_employee_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=New_Employee_strategy)
def test_new_employee_Place_of_Birth_setter(instance):
    original = instance.Place_of_Birth
    instance.Place_of_Birth = original
    assert instance.Place_of_Birth == original

@given(instance=Task_strategy)
@settings(max_examples=50)
def test_task_instantiation(instance):
    assert isinstance(instance, Task)



@given(instance=Task_strategy)
def test_task_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=Task_strategy)
def test_task_Task_Detail_setter(instance):
    original = instance.Task_Detail
    instance.Task_Detail = original
    assert instance.Task_Detail == original



@given(instance=Task_strategy)
def test_task_Deadline_setter(instance):
    original = instance.Deadline
    instance.Deadline = original
    assert instance.Deadline == original



@given(instance=Task_strategy)
def test_task_Task_Name_setter(instance):
    original = instance.Task_Name
    instance.Task_Name = original
    assert instance.Task_Name == original
