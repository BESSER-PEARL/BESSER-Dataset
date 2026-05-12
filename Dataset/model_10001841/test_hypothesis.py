import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Other_employees,
    Dean,
    Moderator,
    Questionnaire_survey,
    Library,
    Schedule,
    Training_materials_IITU,
    News_in_Dl,
    Team,
    Course,
    Department,
    Students,
    Teachers,
    Administrator,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_other_employees_is_not_abstract():
    assert not inspect.isabstract(Other_employees)


def test_other_employees_constructor_exists():
    assert callable(Other_employees.__init__)


def test_other_employees_constructor_args():
    sig = inspect.signature(Other_employees.__init__)
    params = list(sig.parameters.keys())
    assert "Position" in params, "Missing parameter 'Position'"
    assert "Name" in params, "Missing parameter 'Name'"

def test_other_employees_has_Position():
    assert hasattr(Other_employees, "Position")
    descriptor = None
    for klass in Other_employees.__mro__:
        if "Position" in klass.__dict__:
            descriptor = klass.__dict__["Position"]
            break
    assert isinstance(descriptor, property)

def test_other_employees_has_Name():
    assert hasattr(Other_employees, "Name")
    descriptor = None
    for klass in Other_employees.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_dean_is_not_abstract():
    assert not inspect.isabstract(Dean)


def test_dean_constructor_exists():
    assert callable(Dean.__init__)


def test_dean_constructor_args():
    sig = inspect.signature(Dean.__init__)
    params = list(sig.parameters.keys())
    assert "Employees" in params, "Missing parameter 'Employees'"

def test_dean_has_Employees():
    assert hasattr(Dean, "Employees")
    descriptor = None
    for klass in Dean.__mro__:
        if "Employees" in klass.__dict__:
            descriptor = klass.__dict__["Employees"]
            break
    assert isinstance(descriptor, property)



def test_moderator_is_not_abstract():
    assert not inspect.isabstract(Moderator)


def test_moderator_constructor_exists():
    assert callable(Moderator.__init__)


def test_moderator_constructor_args():
    sig = inspect.signature(Moderator.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_moderator_has_Name():
    assert hasattr(Moderator, "Name")
    descriptor = None
    for klass in Moderator.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_questionnaire_survey_is_not_abstract():
    assert not inspect.isabstract(Questionnaire_survey)


def test_questionnaire_survey_constructor_exists():
    assert callable(Questionnaire_survey.__init__)


def test_questionnaire_survey_constructor_args():
    sig = inspect.signature(Questionnaire_survey.__init__)
    params = list(sig.parameters.keys())
    assert "Teachers" in params, "Missing parameter 'Teachers'"
    assert "Students" in params, "Missing parameter 'Students'"

def test_questionnaire_survey_has_Teachers():
    assert hasattr(Questionnaire_survey, "Teachers")
    descriptor = None
    for klass in Questionnaire_survey.__mro__:
        if "Teachers" in klass.__dict__:
            descriptor = klass.__dict__["Teachers"]
            break
    assert isinstance(descriptor, property)

def test_questionnaire_survey_has_Students():
    assert hasattr(Questionnaire_survey, "Students")
    descriptor = None
    for klass in Questionnaire_survey.__mro__:
        if "Students" in klass.__dict__:
            descriptor = klass.__dict__["Students"]
            break
    assert isinstance(descriptor, property)



def test_library_is_not_abstract():
    assert not inspect.isabstract(Library)


def test_library_constructor_exists():
    assert callable(Library.__init__)


def test_library_constructor_args():
    sig = inspect.signature(Library.__init__)
    params = list(sig.parameters.keys())
    assert "Books" in params, "Missing parameter 'Books'"
    assert "Materials" in params, "Missing parameter 'Materials'"

def test_library_has_Books():
    assert hasattr(Library, "Books")
    descriptor = None
    for klass in Library.__mro__:
        if "Books" in klass.__dict__:
            descriptor = klass.__dict__["Books"]
            break
    assert isinstance(descriptor, property)

def test_library_has_Materials():
    assert hasattr(Library, "Materials")
    descriptor = None
    for klass in Library.__mro__:
        if "Materials" in klass.__dict__:
            descriptor = klass.__dict__["Materials"]
            break
    assert isinstance(descriptor, property)



def test_schedule_is_not_abstract():
    assert not inspect.isabstract(Schedule)


def test_schedule_constructor_exists():
    assert callable(Schedule.__init__)


def test_schedule_constructor_args():
    sig = inspect.signature(Schedule.__init__)
    params = list(sig.parameters.keys())
    assert "Teacher" in params, "Missing parameter 'Teacher'"
    assert "Course" in params, "Missing parameter 'Course'"

def test_schedule_has_Teacher():
    assert hasattr(Schedule, "Teacher")
    descriptor = None
    for klass in Schedule.__mro__:
        if "Teacher" in klass.__dict__:
            descriptor = klass.__dict__["Teacher"]
            break
    assert isinstance(descriptor, property)

def test_schedule_has_Course():
    assert hasattr(Schedule, "Course")
    descriptor = None
    for klass in Schedule.__mro__:
        if "Course" in klass.__dict__:
            descriptor = klass.__dict__["Course"]
            break
    assert isinstance(descriptor, property)



def test_training_materials_iitu_is_not_abstract():
    assert not inspect.isabstract(Training_materials_IITU)


def test_training_materials_iitu_constructor_exists():
    assert callable(Training_materials_IITU.__init__)


def test_training_materials_iitu_constructor_args():
    sig = inspect.signature(Training_materials_IITU.__init__)
    params = list(sig.parameters.keys())
    assert "Materials" in params, "Missing parameter 'Materials'"

def test_training_materials_iitu_has_Materials():
    assert hasattr(Training_materials_IITU, "Materials")
    descriptor = None
    for klass in Training_materials_IITU.__mro__:
        if "Materials" in klass.__dict__:
            descriptor = klass.__dict__["Materials"]
            break
    assert isinstance(descriptor, property)



def test_news_in_dl_is_not_abstract():
    assert not inspect.isabstract(News_in_Dl)


def test_news_in_dl_constructor_exists():
    assert callable(News_in_Dl.__init__)


def test_news_in_dl_constructor_args():
    sig = inspect.signature(News_in_Dl.__init__)
    params = list(sig.parameters.keys())
    assert "Update_news" in params, "Missing parameter 'Update_news'"
    assert "Opens_news" in params, "Missing parameter 'Opens_news'"
    assert "Hyperlink" in params, "Missing parameter 'Hyperlink'"

def test_news_in_dl_has_Update_news():
    assert hasattr(News_in_Dl, "Update_news")
    descriptor = None
    for klass in News_in_Dl.__mro__:
        if "Update_news" in klass.__dict__:
            descriptor = klass.__dict__["Update_news"]
            break
    assert isinstance(descriptor, property)

def test_news_in_dl_has_Opens_news():
    assert hasattr(News_in_Dl, "Opens_news")
    descriptor = None
    for klass in News_in_Dl.__mro__:
        if "Opens_news" in klass.__dict__:
            descriptor = klass.__dict__["Opens_news"]
            break
    assert isinstance(descriptor, property)

def test_news_in_dl_has_Hyperlink():
    assert hasattr(News_in_Dl, "Hyperlink")
    descriptor = None
    for klass in News_in_Dl.__mro__:
        if "Hyperlink" in klass.__dict__:
            descriptor = klass.__dict__["Hyperlink"]
            break
    assert isinstance(descriptor, property)



def test_team_is_not_abstract():
    assert not inspect.isabstract(Team)


def test_team_constructor_exists():
    assert callable(Team.__init__)


def test_team_constructor_args():
    sig = inspect.signature(Team.__init__)
    params = list(sig.parameters.keys())
    assert "Footballs_teams" in params, "Missing parameter 'Footballs_teams'"
    assert "Ministry" in params, "Missing parameter 'Ministry'"
    assert "Robotric_teams" in params, "Missing parameter 'Robotric_teams'"
    assert "President" in params, "Missing parameter 'President'"

def test_team_has_Footballs_teams():
    assert hasattr(Team, "Footballs_teams")
    descriptor = None
    for klass in Team.__mro__:
        if "Footballs_teams" in klass.__dict__:
            descriptor = klass.__dict__["Footballs_teams"]
            break
    assert isinstance(descriptor, property)

def test_team_has_Ministry():
    assert hasattr(Team, "Ministry")
    descriptor = None
    for klass in Team.__mro__:
        if "Ministry" in klass.__dict__:
            descriptor = klass.__dict__["Ministry"]
            break
    assert isinstance(descriptor, property)

def test_team_has_Robotric_teams():
    assert hasattr(Team, "Robotric_teams")
    descriptor = None
    for klass in Team.__mro__:
        if "Robotric_teams" in klass.__dict__:
            descriptor = klass.__dict__["Robotric_teams"]
            break
    assert isinstance(descriptor, property)

def test_team_has_President():
    assert hasattr(Team, "President")
    descriptor = None
    for klass in Team.__mro__:
        if "President" in klass.__dict__:
            descriptor = klass.__dict__["President"]
            break
    assert isinstance(descriptor, property)



def test_course_is_not_abstract():
    assert not inspect.isabstract(Course)


def test_course_constructor_exists():
    assert callable(Course.__init__)


def test_course_constructor_args():
    sig = inspect.signature(Course.__init__)
    params = list(sig.parameters.keys())
    assert "_2_Course" in params, "Missing parameter '_2_Course'"
    assert "_4_Course" in params, "Missing parameter '_4_Course'"
    assert "_1_Course" in params, "Missing parameter '_1_Course'"
    assert "_3_Course" in params, "Missing parameter '_3_Course'"

def test_course_has__2_Course():
    assert hasattr(Course, "_2_Course")
    descriptor = None
    for klass in Course.__mro__:
        if "_2_Course" in klass.__dict__:
            descriptor = klass.__dict__["_2_Course"]
            break
    assert isinstance(descriptor, property)

def test_course_has__4_Course():
    assert hasattr(Course, "_4_Course")
    descriptor = None
    for klass in Course.__mro__:
        if "_4_Course" in klass.__dict__:
            descriptor = klass.__dict__["_4_Course"]
            break
    assert isinstance(descriptor, property)

def test_course_has__1_Course():
    assert hasattr(Course, "_1_Course")
    descriptor = None
    for klass in Course.__mro__:
        if "_1_Course" in klass.__dict__:
            descriptor = klass.__dict__["_1_Course"]
            break
    assert isinstance(descriptor, property)

def test_course_has__3_Course():
    assert hasattr(Course, "_3_Course")
    descriptor = None
    for klass in Course.__mro__:
        if "_3_Course" in klass.__dict__:
            descriptor = klass.__dict__["_3_Course"]
            break
    assert isinstance(descriptor, property)



def test_department_is_not_abstract():
    assert not inspect.isabstract(Department)


def test_department_constructor_exists():
    assert callable(Department.__init__)


def test_department_constructor_args():
    sig = inspect.signature(Department.__init__)
    params = list(sig.parameters.keys())
    assert "IS" in params, "Missing parameter 'IS'"
    assert "MCM" in params, "Missing parameter 'MCM'"
    assert "CS" in params, "Missing parameter 'CS'"
    assert "ITM" in params, "Missing parameter 'ITM'"
    assert "CSSE" in params, "Missing parameter 'CSSE'"
    assert "JUR" in params, "Missing parameter 'JUR'"

def test_department_has_IS():
    assert hasattr(Department, "IS")
    descriptor = None
    for klass in Department.__mro__:
        if "IS" in klass.__dict__:
            descriptor = klass.__dict__["IS"]
            break
    assert isinstance(descriptor, property)

def test_department_has_MCM():
    assert hasattr(Department, "MCM")
    descriptor = None
    for klass in Department.__mro__:
        if "MCM" in klass.__dict__:
            descriptor = klass.__dict__["MCM"]
            break
    assert isinstance(descriptor, property)

def test_department_has_CS():
    assert hasattr(Department, "CS")
    descriptor = None
    for klass in Department.__mro__:
        if "CS" in klass.__dict__:
            descriptor = klass.__dict__["CS"]
            break
    assert isinstance(descriptor, property)

def test_department_has_ITM():
    assert hasattr(Department, "ITM")
    descriptor = None
    for klass in Department.__mro__:
        if "ITM" in klass.__dict__:
            descriptor = klass.__dict__["ITM"]
            break
    assert isinstance(descriptor, property)

def test_department_has_CSSE():
    assert hasattr(Department, "CSSE")
    descriptor = None
    for klass in Department.__mro__:
        if "CSSE" in klass.__dict__:
            descriptor = klass.__dict__["CSSE"]
            break
    assert isinstance(descriptor, property)

def test_department_has_JUR():
    assert hasattr(Department, "JUR")
    descriptor = None
    for klass in Department.__mro__:
        if "JUR" in klass.__dict__:
            descriptor = klass.__dict__["JUR"]
            break
    assert isinstance(descriptor, property)



def test_students_is_not_abstract():
    assert not inspect.isabstract(Students)


def test_students_constructor_exists():
    assert callable(Students.__init__)


def test_students_constructor_args():
    sig = inspect.signature(Students.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Course" in params, "Missing parameter 'Course'"
    assert "ID" in params, "Missing parameter 'ID'"

def test_students_has_Name():
    assert hasattr(Students, "Name")
    descriptor = None
    for klass in Students.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_students_has_Course():
    assert hasattr(Students, "Course")
    descriptor = None
    for klass in Students.__mro__:
        if "Course" in klass.__dict__:
            descriptor = klass.__dict__["Course"]
            break
    assert isinstance(descriptor, property)

def test_students_has_ID():
    assert hasattr(Students, "ID")
    descriptor = None
    for klass in Students.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)



def test_teachers_is_not_abstract():
    assert not inspect.isabstract(Teachers)


def test_teachers_constructor_exists():
    assert callable(Teachers.__init__)


def test_teachers_constructor_args():
    sig = inspect.signature(Teachers.__init__)
    params = list(sig.parameters.keys())
    assert "ID" in params, "Missing parameter 'ID'"
    assert "Rank" in params, "Missing parameter 'Rank'"
    assert "Info" in params, "Missing parameter 'Info'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Department" in params, "Missing parameter 'Department'"
    assert "Course" in params, "Missing parameter 'Course'"

def test_teachers_has_ID():
    assert hasattr(Teachers, "ID")
    descriptor = None
    for klass in Teachers.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)

def test_teachers_has_Rank():
    assert hasattr(Teachers, "Rank")
    descriptor = None
    for klass in Teachers.__mro__:
        if "Rank" in klass.__dict__:
            descriptor = klass.__dict__["Rank"]
            break
    assert isinstance(descriptor, property)

def test_teachers_has_Info():
    assert hasattr(Teachers, "Info")
    descriptor = None
    for klass in Teachers.__mro__:
        if "Info" in klass.__dict__:
            descriptor = klass.__dict__["Info"]
            break
    assert isinstance(descriptor, property)

def test_teachers_has_Name():
    assert hasattr(Teachers, "Name")
    descriptor = None
    for klass in Teachers.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_teachers_has_Department():
    assert hasattr(Teachers, "Department")
    descriptor = None
    for klass in Teachers.__mro__:
        if "Department" in klass.__dict__:
            descriptor = klass.__dict__["Department"]
            break
    assert isinstance(descriptor, property)

def test_teachers_has_Course():
    assert hasattr(Teachers, "Course")
    descriptor = None
    for klass in Teachers.__mro__:
        if "Course" in klass.__dict__:
            descriptor = klass.__dict__["Course"]
            break
    assert isinstance(descriptor, property)



def test_administrator_is_not_abstract():
    assert not inspect.isabstract(Administrator)


def test_administrator_constructor_exists():
    assert callable(Administrator.__init__)


def test_administrator_constructor_args():
    sig = inspect.signature(Administrator.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Privilege" in params, "Missing parameter 'Privilege'"

def test_administrator_has_Name():
    assert hasattr(Administrator, "Name")
    descriptor = None
    for klass in Administrator.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_administrator_has_Privilege():
    assert hasattr(Administrator, "Privilege")
    descriptor = None
    for klass in Administrator.__mro__:
        if "Privilege" in klass.__dict__:
            descriptor = klass.__dict__["Privilege"]
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
Other_employees_strategy = st.builds(
    Other_employees,
    Position=
        safe_text,
    Name=
        safe_text
)
Dean_strategy = st.builds(
    Dean,
    Employees=
        st.none()
)
Moderator_strategy = st.builds(
    Moderator,
    Name=
        st.none()
)
Questionnaire_survey_strategy = st.builds(
    Questionnaire_survey,
    Teachers=
        safe_text,
    Students=
        safe_text
)
Library_strategy = st.builds(
    Library,
    Books=
        st.none(),
    Materials=
        st.none()
)
Schedule_strategy = st.builds(
    Schedule,
    Teacher=
        st.none(),
    Course=
        st.none()
)
Training_materials_IITU_strategy = st.builds(
    Training_materials_IITU,
    Materials=
        safe_text
)
News_in_Dl_strategy = st.builds(
    News_in_Dl,
    Update_news=
        st.none(),
    Opens_news=
        st.none(),
    Hyperlink=
        safe_text
)
Team_strategy = st.builds(
    Team,
    Footballs_teams=
        st.none(),
    Ministry=
        safe_text,
    Robotric_teams=
        st.none(),
    President=
        safe_text
)
Course_strategy = st.builds(
    Course,
    _2_Course=
        st.none(),
    _4_Course=
        st.none(),
    _1_Course=
        st.none(),
    _3_Course=
        st.none()
)
Department_strategy = st.builds(
    Department,
    IS=
        safe_text,
    MCM=
        safe_text,
    CS=
        safe_text,
    ITM=
        safe_text,
    CSSE=
        safe_text,
    JUR=
        safe_text
)
Students_strategy = st.builds(
    Students,
    Name=
        safe_text,
    Course=
        st.none(),
    ID=
        st.none()
)
Teachers_strategy = st.builds(
    Teachers,
    ID=
        st.none(),
    Rank=
        st.none(),
    Info=
        st.none(),
    Name=
        safe_text,
    Department=
        st.none(),
    Course=
        st.none()
)
Administrator_strategy = st.builds(
    Administrator,
    Name=
        st.none(),
    Privilege=
        safe_text
)

@given(instance=Other_employees_strategy)
@settings(max_examples=50)
def test_other_employees_instantiation(instance):
    assert isinstance(instance, Other_employees)



@given(instance=Other_employees_strategy)
def test_other_employees_Position_setter(instance):
    original = instance.Position
    instance.Position = original
    assert instance.Position == original



@given(instance=Other_employees_strategy)
def test_other_employees_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=Dean_strategy)
@settings(max_examples=50)
def test_dean_instantiation(instance):
    assert isinstance(instance, Dean)



@given(instance=Dean_strategy)
def test_dean_Employees_setter(instance):
    original = instance.Employees
    instance.Employees = original
    assert instance.Employees == original

@given(instance=Moderator_strategy)
@settings(max_examples=50)
def test_moderator_instantiation(instance):
    assert isinstance(instance, Moderator)



@given(instance=Moderator_strategy)
def test_moderator_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=Questionnaire_survey_strategy)
@settings(max_examples=50)
def test_questionnaire_survey_instantiation(instance):
    assert isinstance(instance, Questionnaire_survey)



@given(instance=Questionnaire_survey_strategy)
def test_questionnaire_survey_Teachers_setter(instance):
    original = instance.Teachers
    instance.Teachers = original
    assert instance.Teachers == original



@given(instance=Questionnaire_survey_strategy)
def test_questionnaire_survey_Students_setter(instance):
    original = instance.Students
    instance.Students = original
    assert instance.Students == original

@given(instance=Library_strategy)
@settings(max_examples=50)
def test_library_instantiation(instance):
    assert isinstance(instance, Library)



@given(instance=Library_strategy)
def test_library_Books_setter(instance):
    original = instance.Books
    instance.Books = original
    assert instance.Books == original



@given(instance=Library_strategy)
def test_library_Materials_setter(instance):
    original = instance.Materials
    instance.Materials = original
    assert instance.Materials == original

@given(instance=Schedule_strategy)
@settings(max_examples=50)
def test_schedule_instantiation(instance):
    assert isinstance(instance, Schedule)



@given(instance=Schedule_strategy)
def test_schedule_Teacher_setter(instance):
    original = instance.Teacher
    instance.Teacher = original
    assert instance.Teacher == original



@given(instance=Schedule_strategy)
def test_schedule_Course_setter(instance):
    original = instance.Course
    instance.Course = original
    assert instance.Course == original

@given(instance=Training_materials_IITU_strategy)
@settings(max_examples=50)
def test_training_materials_iitu_instantiation(instance):
    assert isinstance(instance, Training_materials_IITU)



@given(instance=Training_materials_IITU_strategy)
def test_training_materials_iitu_Materials_setter(instance):
    original = instance.Materials
    instance.Materials = original
    assert instance.Materials == original

@given(instance=News_in_Dl_strategy)
@settings(max_examples=50)
def test_news_in_dl_instantiation(instance):
    assert isinstance(instance, News_in_Dl)



@given(instance=News_in_Dl_strategy)
def test_news_in_dl_Update_news_setter(instance):
    original = instance.Update_news
    instance.Update_news = original
    assert instance.Update_news == original



@given(instance=News_in_Dl_strategy)
def test_news_in_dl_Opens_news_setter(instance):
    original = instance.Opens_news
    instance.Opens_news = original
    assert instance.Opens_news == original



@given(instance=News_in_Dl_strategy)
def test_news_in_dl_Hyperlink_setter(instance):
    original = instance.Hyperlink
    instance.Hyperlink = original
    assert instance.Hyperlink == original

@given(instance=Team_strategy)
@settings(max_examples=50)
def test_team_instantiation(instance):
    assert isinstance(instance, Team)



@given(instance=Team_strategy)
def test_team_Footballs_teams_setter(instance):
    original = instance.Footballs_teams
    instance.Footballs_teams = original
    assert instance.Footballs_teams == original



@given(instance=Team_strategy)
def test_team_Ministry_setter(instance):
    original = instance.Ministry
    instance.Ministry = original
    assert instance.Ministry == original



@given(instance=Team_strategy)
def test_team_Robotric_teams_setter(instance):
    original = instance.Robotric_teams
    instance.Robotric_teams = original
    assert instance.Robotric_teams == original



@given(instance=Team_strategy)
def test_team_President_setter(instance):
    original = instance.President
    instance.President = original
    assert instance.President == original

@given(instance=Course_strategy)
@settings(max_examples=50)
def test_course_instantiation(instance):
    assert isinstance(instance, Course)



@given(instance=Course_strategy)
def test_course__2_Course_setter(instance):
    original = instance._2_Course
    instance._2_Course = original
    assert instance._2_Course == original



@given(instance=Course_strategy)
def test_course__4_Course_setter(instance):
    original = instance._4_Course
    instance._4_Course = original
    assert instance._4_Course == original



@given(instance=Course_strategy)
def test_course__1_Course_setter(instance):
    original = instance._1_Course
    instance._1_Course = original
    assert instance._1_Course == original



@given(instance=Course_strategy)
def test_course__3_Course_setter(instance):
    original = instance._3_Course
    instance._3_Course = original
    assert instance._3_Course == original

@given(instance=Department_strategy)
@settings(max_examples=50)
def test_department_instantiation(instance):
    assert isinstance(instance, Department)



@given(instance=Department_strategy)
def test_department_IS_setter(instance):
    original = instance.IS
    instance.IS = original
    assert instance.IS == original



@given(instance=Department_strategy)
def test_department_MCM_setter(instance):
    original = instance.MCM
    instance.MCM = original
    assert instance.MCM == original



@given(instance=Department_strategy)
def test_department_CS_setter(instance):
    original = instance.CS
    instance.CS = original
    assert instance.CS == original



@given(instance=Department_strategy)
def test_department_ITM_setter(instance):
    original = instance.ITM
    instance.ITM = original
    assert instance.ITM == original



@given(instance=Department_strategy)
def test_department_CSSE_setter(instance):
    original = instance.CSSE
    instance.CSSE = original
    assert instance.CSSE == original



@given(instance=Department_strategy)
def test_department_JUR_setter(instance):
    original = instance.JUR
    instance.JUR = original
    assert instance.JUR == original

@given(instance=Students_strategy)
@settings(max_examples=50)
def test_students_instantiation(instance):
    assert isinstance(instance, Students)



@given(instance=Students_strategy)
def test_students_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=Students_strategy)
def test_students_Course_setter(instance):
    original = instance.Course
    instance.Course = original
    assert instance.Course == original



@given(instance=Students_strategy)
def test_students_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original

@given(instance=Teachers_strategy)
@settings(max_examples=50)
def test_teachers_instantiation(instance):
    assert isinstance(instance, Teachers)



@given(instance=Teachers_strategy)
def test_teachers_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original



@given(instance=Teachers_strategy)
def test_teachers_Rank_setter(instance):
    original = instance.Rank
    instance.Rank = original
    assert instance.Rank == original



@given(instance=Teachers_strategy)
def test_teachers_Info_setter(instance):
    original = instance.Info
    instance.Info = original
    assert instance.Info == original



@given(instance=Teachers_strategy)
def test_teachers_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=Teachers_strategy)
def test_teachers_Department_setter(instance):
    original = instance.Department
    instance.Department = original
    assert instance.Department == original



@given(instance=Teachers_strategy)
def test_teachers_Course_setter(instance):
    original = instance.Course
    instance.Course = original
    assert instance.Course == original

@given(instance=Administrator_strategy)
@settings(max_examples=50)
def test_administrator_instantiation(instance):
    assert isinstance(instance, Administrator)



@given(instance=Administrator_strategy)
def test_administrator_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=Administrator_strategy)
def test_administrator_Privilege_setter(instance):
    original = instance.Privilege
    instance.Privilege = original
    assert instance.Privilege == original
