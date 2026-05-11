import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    coursePages::Reduction,
    coursePages::Precondition,
    coursePages::CourseWorker,
    coursePages::CourseInstance,
    coursePages::CourseWork,
    coursePages::CourseWorkObject,
    coursePages::Department,
    coursePages::Course,
    coursePages::StudyPrograms,
    Person,
    coursePages::Employee,
    coursePages::Student,
    coursePages::Evaluations,
    coursePages::EvaluationObject,
    coursePages::Person,
    TermType,
    EvaluationType,
    personRoleType,
    CourseWorkType,
    PrecondistionType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_coursepages::reduction_is_not_abstract():
    assert not inspect.isabstract(coursePages::Reduction)


def test_coursepages::reduction_constructor_exists():
    assert callable(coursePages::Reduction.__init__)


def test_coursepages::reduction_constructor_args():
    sig = inspect.signature(coursePages::Reduction.__init__)
    params = list(sig.parameters.keys())
    assert "creditReduction" in params, "Missing parameter 'creditReduction'"

def test_coursepages::reduction_has_creditReduction():
    assert hasattr(coursePages::Reduction, "creditReduction")
    descriptor = None
    for klass in coursePages::Reduction.__mro__:
        if "creditReduction" in klass.__dict__:
            descriptor = klass.__dict__["creditReduction"]
            break
    assert isinstance(descriptor, property)



def test_coursepages::precondition_is_not_abstract():
    assert not inspect.isabstract(coursePages::Precondition)


def test_coursepages::precondition_constructor_exists():
    assert callable(coursePages::Precondition.__init__)


def test_coursepages::precondition_constructor_args():
    sig = inspect.signature(coursePages::Precondition.__init__)
    params = list(sig.parameters.keys())
    assert "preconditionStatus" in params, "Missing parameter 'preconditionStatus'"

def test_coursepages::precondition_has_preconditionStatus():
    assert hasattr(coursePages::Precondition, "preconditionStatus")
    descriptor = None
    for klass in coursePages::Precondition.__mro__:
        if "preconditionStatus" in klass.__dict__:
            descriptor = klass.__dict__["preconditionStatus"]
            break
    assert isinstance(descriptor, property)



def test_coursepages::courseworker_is_not_abstract():
    assert not inspect.isabstract(coursePages::CourseWorker)


def test_coursepages::courseworker_constructor_exists():
    assert callable(coursePages::CourseWorker.__init__)


def test_coursepages::courseworker_constructor_args():
    sig = inspect.signature(coursePages::CourseWorker.__init__)
    params = list(sig.parameters.keys())
    assert "courseRole" in params, "Missing parameter 'courseRole'"

def test_coursepages::courseworker_has_courseRole():
    assert hasattr(coursePages::CourseWorker, "courseRole")
    descriptor = None
    for klass in coursePages::CourseWorker.__mro__:
        if "courseRole" in klass.__dict__:
            descriptor = klass.__dict__["courseRole"]
            break
    assert isinstance(descriptor, property)



def test_coursepages::courseinstance_is_not_abstract():
    assert not inspect.isabstract(coursePages::CourseInstance)


def test_coursepages::courseinstance_constructor_exists():
    assert callable(coursePages::CourseInstance.__init__)


def test_coursepages::courseinstance_constructor_args():
    sig = inspect.signature(coursePages::CourseInstance.__init__)
    params = list(sig.parameters.keys())
    assert "term" in params, "Missing parameter 'term'"
    assert "courseYear" in params, "Missing parameter 'courseYear'"

def test_coursepages::courseinstance_has_term():
    assert hasattr(coursePages::CourseInstance, "term")
    descriptor = None
    for klass in coursePages::CourseInstance.__mro__:
        if "term" in klass.__dict__:
            descriptor = klass.__dict__["term"]
            break
    assert isinstance(descriptor, property)

def test_coursepages::courseinstance_has_courseYear():
    assert hasattr(coursePages::CourseInstance, "courseYear")
    descriptor = None
    for klass in coursePages::CourseInstance.__mro__:
        if "courseYear" in klass.__dict__:
            descriptor = klass.__dict__["courseYear"]
            break
    assert isinstance(descriptor, property)



def test_coursepages::coursework_is_not_abstract():
    assert not inspect.isabstract(coursePages::CourseWork)


def test_coursepages::coursework_constructor_exists():
    assert callable(coursePages::CourseWork.__init__)


def test_coursepages::coursework_constructor_args():
    sig = inspect.signature(coursePages::CourseWork.__init__)
    params = list(sig.parameters.keys())



def test_coursepages::courseworkobject_is_not_abstract():
    assert not inspect.isabstract(coursePages::CourseWorkObject)


def test_coursepages::courseworkobject_constructor_exists():
    assert callable(coursePages::CourseWorkObject.__init__)


def test_coursepages::courseworkobject_constructor_args():
    sig = inspect.signature(coursePages::CourseWorkObject.__init__)
    params = list(sig.parameters.keys())
    assert "courseWorkType" in params, "Missing parameter 'courseWorkType'"
    assert "end" in params, "Missing parameter 'end'"
    assert "start" in params, "Missing parameter 'start'"
    assert "room" in params, "Missing parameter 'room'"
    assert "day" in params, "Missing parameter 'day'"

def test_coursepages::courseworkobject_has_courseWorkType():
    assert hasattr(coursePages::CourseWorkObject, "courseWorkType")
    descriptor = None
    for klass in coursePages::CourseWorkObject.__mro__:
        if "courseWorkType" in klass.__dict__:
            descriptor = klass.__dict__["courseWorkType"]
            break
    assert isinstance(descriptor, property)

def test_coursepages::courseworkobject_has_end():
    assert hasattr(coursePages::CourseWorkObject, "end")
    descriptor = None
    for klass in coursePages::CourseWorkObject.__mro__:
        if "end" in klass.__dict__:
            descriptor = klass.__dict__["end"]
            break
    assert isinstance(descriptor, property)

def test_coursepages::courseworkobject_has_start():
    assert hasattr(coursePages::CourseWorkObject, "start")
    descriptor = None
    for klass in coursePages::CourseWorkObject.__mro__:
        if "start" in klass.__dict__:
            descriptor = klass.__dict__["start"]
            break
    assert isinstance(descriptor, property)

def test_coursepages::courseworkobject_has_room():
    assert hasattr(coursePages::CourseWorkObject, "room")
    descriptor = None
    for klass in coursePages::CourseWorkObject.__mro__:
        if "room" in klass.__dict__:
            descriptor = klass.__dict__["room"]
            break
    assert isinstance(descriptor, property)

def test_coursepages::courseworkobject_has_day():
    assert hasattr(coursePages::CourseWorkObject, "day")
    descriptor = None
    for klass in coursePages::CourseWorkObject.__mro__:
        if "day" in klass.__dict__:
            descriptor = klass.__dict__["day"]
            break
    assert isinstance(descriptor, property)



def test_coursepages::department_is_not_abstract():
    assert not inspect.isabstract(coursePages::Department)


def test_coursepages::department_constructor_exists():
    assert callable(coursePages::Department.__init__)


def test_coursepages::department_constructor_args():
    sig = inspect.signature(coursePages::Department.__init__)
    params = list(sig.parameters.keys())
    assert "phoneNummber" in params, "Missing parameter 'phoneNummber'"
    assert "departmentName" in params, "Missing parameter 'departmentName'"
    assert "email" in params, "Missing parameter 'email'"

def test_coursepages::department_has_phoneNummber():
    assert hasattr(coursePages::Department, "phoneNummber")
    descriptor = None
    for klass in coursePages::Department.__mro__:
        if "phoneNummber" in klass.__dict__:
            descriptor = klass.__dict__["phoneNummber"]
            break
    assert isinstance(descriptor, property)

def test_coursepages::department_has_departmentName():
    assert hasattr(coursePages::Department, "departmentName")
    descriptor = None
    for klass in coursePages::Department.__mro__:
        if "departmentName" in klass.__dict__:
            descriptor = klass.__dict__["departmentName"]
            break
    assert isinstance(descriptor, property)

def test_coursepages::department_has_email():
    assert hasattr(coursePages::Department, "email")
    descriptor = None
    for klass in coursePages::Department.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)



def test_coursepages::course_is_not_abstract():
    assert not inspect.isabstract(coursePages::Course)


def test_coursepages::course_constructor_exists():
    assert callable(coursePages::Course.__init__)


def test_coursepages::course_constructor_args():
    sig = inspect.signature(coursePages::Course.__init__)
    params = list(sig.parameters.keys())
    assert "courseCredits" in params, "Missing parameter 'courseCredits'"
    assert "courseContent" in params, "Missing parameter 'courseContent'"
    assert "courseName" in params, "Missing parameter 'courseName'"
    assert "courseCode" in params, "Missing parameter 'courseCode'"

def test_coursepages::course_has_courseCredits():
    assert hasattr(coursePages::Course, "courseCredits")
    descriptor = None
    for klass in coursePages::Course.__mro__:
        if "courseCredits" in klass.__dict__:
            descriptor = klass.__dict__["courseCredits"]
            break
    assert isinstance(descriptor, property)

def test_coursepages::course_has_courseContent():
    assert hasattr(coursePages::Course, "courseContent")
    descriptor = None
    for klass in coursePages::Course.__mro__:
        if "courseContent" in klass.__dict__:
            descriptor = klass.__dict__["courseContent"]
            break
    assert isinstance(descriptor, property)

def test_coursepages::course_has_courseName():
    assert hasattr(coursePages::Course, "courseName")
    descriptor = None
    for klass in coursePages::Course.__mro__:
        if "courseName" in klass.__dict__:
            descriptor = klass.__dict__["courseName"]
            break
    assert isinstance(descriptor, property)

def test_coursepages::course_has_courseCode():
    assert hasattr(coursePages::Course, "courseCode")
    descriptor = None
    for klass in coursePages::Course.__mro__:
        if "courseCode" in klass.__dict__:
            descriptor = klass.__dict__["courseCode"]
            break
    assert isinstance(descriptor, property)



def test_coursepages::studyprograms_is_not_abstract():
    assert not inspect.isabstract(coursePages::StudyPrograms)


def test_coursepages::studyprograms_constructor_exists():
    assert callable(coursePages::StudyPrograms.__init__)


def test_coursepages::studyprograms_constructor_args():
    sig = inspect.signature(coursePages::StudyPrograms.__init__)
    params = list(sig.parameters.keys())
    assert "studyProgramName" in params, "Missing parameter 'studyProgramName'"
    assert "studyProgramCode" in params, "Missing parameter 'studyProgramCode'"

def test_coursepages::studyprograms_has_studyProgramName():
    assert hasattr(coursePages::StudyPrograms, "studyProgramName")
    descriptor = None
    for klass in coursePages::StudyPrograms.__mro__:
        if "studyProgramName" in klass.__dict__:
            descriptor = klass.__dict__["studyProgramName"]
            break
    assert isinstance(descriptor, property)

def test_coursepages::studyprograms_has_studyProgramCode():
    assert hasattr(coursePages::StudyPrograms, "studyProgramCode")
    descriptor = None
    for klass in coursePages::StudyPrograms.__mro__:
        if "studyProgramCode" in klass.__dict__:
            descriptor = klass.__dict__["studyProgramCode"]
            break
    assert isinstance(descriptor, property)



def test_person_is_not_abstract():
    assert not inspect.isabstract(Person)


def test_person_constructor_exists():
    assert callable(Person.__init__)


def test_person_constructor_args():
    sig = inspect.signature(Person.__init__)
    params = list(sig.parameters.keys())



def test_coursepages::employee_is_not_abstract():
    assert not inspect.isabstract(coursePages::Employee)


def test_coursepages::employee_constructor_exists():
    assert callable(coursePages::Employee.__init__)


def test_coursepages::employee_constructor_args():
    sig = inspect.signature(coursePages::Employee.__init__)
    params = list(sig.parameters.keys())
    assert "position" in params, "Missing parameter 'position'"

def test_coursepages::employee_has_position():
    assert hasattr(coursePages::Employee, "position")
    descriptor = None
    for klass in coursePages::Employee.__mro__:
        if "position" in klass.__dict__:
            descriptor = klass.__dict__["position"]
            break
    assert isinstance(descriptor, property)



def test_coursepages::student_is_not_abstract():
    assert not inspect.isabstract(coursePages::Student)


def test_coursepages::student_constructor_exists():
    assert callable(coursePages::Student.__init__)


def test_coursepages::student_constructor_args():
    sig = inspect.signature(coursePages::Student.__init__)
    params = list(sig.parameters.keys())
    assert "studentID" in params, "Missing parameter 'studentID'"

def test_coursepages::student_has_studentID():
    assert hasattr(coursePages::Student, "studentID")
    descriptor = None
    for klass in coursePages::Student.__mro__:
        if "studentID" in klass.__dict__:
            descriptor = klass.__dict__["studentID"]
            break
    assert isinstance(descriptor, property)



def test_coursepages::evaluations_is_not_abstract():
    assert not inspect.isabstract(coursePages::Evaluations)


def test_coursepages::evaluations_constructor_exists():
    assert callable(coursePages::Evaluations.__init__)


def test_coursepages::evaluations_constructor_args():
    sig = inspect.signature(coursePages::Evaluations.__init__)
    params = list(sig.parameters.keys())



def test_coursepages::evaluationobject_is_not_abstract():
    assert not inspect.isabstract(coursePages::EvaluationObject)


def test_coursepages::evaluationobject_constructor_exists():
    assert callable(coursePages::EvaluationObject.__init__)


def test_coursepages::evaluationobject_constructor_args():
    sig = inspect.signature(coursePages::EvaluationObject.__init__)
    params = list(sig.parameters.keys())
    assert "evaluationsForm" in params, "Missing parameter 'evaluationsForm'"
    assert "term" in params, "Missing parameter 'term'"
    assert "credits" in params, "Missing parameter 'credits'"
    assert "date" in params, "Missing parameter 'date'"

def test_coursepages::evaluationobject_has_evaluationsForm():
    assert hasattr(coursePages::EvaluationObject, "evaluationsForm")
    descriptor = None
    for klass in coursePages::EvaluationObject.__mro__:
        if "evaluationsForm" in klass.__dict__:
            descriptor = klass.__dict__["evaluationsForm"]
            break
    assert isinstance(descriptor, property)

def test_coursepages::evaluationobject_has_term():
    assert hasattr(coursePages::EvaluationObject, "term")
    descriptor = None
    for klass in coursePages::EvaluationObject.__mro__:
        if "term" in klass.__dict__:
            descriptor = klass.__dict__["term"]
            break
    assert isinstance(descriptor, property)

def test_coursepages::evaluationobject_has_credits():
    assert hasattr(coursePages::EvaluationObject, "credits")
    descriptor = None
    for klass in coursePages::EvaluationObject.__mro__:
        if "credits" in klass.__dict__:
            descriptor = klass.__dict__["credits"]
            break
    assert isinstance(descriptor, property)

def test_coursepages::evaluationobject_has_date():
    assert hasattr(coursePages::EvaluationObject, "date")
    descriptor = None
    for klass in coursePages::EvaluationObject.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)



def test_coursepages::person_is_not_abstract():
    assert not inspect.isabstract(coursePages::Person)


def test_coursepages::person_constructor_exists():
    assert callable(coursePages::Person.__init__)


def test_coursepages::person_constructor_args():
    sig = inspect.signature(coursePages::Person.__init__)
    params = list(sig.parameters.keys())
    assert "surName" in params, "Missing parameter 'surName'"
    assert "phoneNummber" in params, "Missing parameter 'phoneNummber'"
    assert "email" in params, "Missing parameter 'email'"
    assert "firstName" in params, "Missing parameter 'firstName'"

def test_coursepages::person_has_surName():
    assert hasattr(coursePages::Person, "surName")
    descriptor = None
    for klass in coursePages::Person.__mro__:
        if "surName" in klass.__dict__:
            descriptor = klass.__dict__["surName"]
            break
    assert isinstance(descriptor, property)

def test_coursepages::person_has_phoneNummber():
    assert hasattr(coursePages::Person, "phoneNummber")
    descriptor = None
    for klass in coursePages::Person.__mro__:
        if "phoneNummber" in klass.__dict__:
            descriptor = klass.__dict__["phoneNummber"]
            break
    assert isinstance(descriptor, property)

def test_coursepages::person_has_email():
    assert hasattr(coursePages::Person, "email")
    descriptor = None
    for klass in coursePages::Person.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)

def test_coursepages::person_has_firstName():
    assert hasattr(coursePages::Person, "firstName")
    descriptor = None
    for klass in coursePages::Person.__mro__:
        if "firstName" in klass.__dict__:
            descriptor = klass.__dict__["firstName"]
            break
    assert isinstance(descriptor, property)

def test_termtype_exists():
    # Check that the Enumeration exists
    assert TermType is not None

def test_termtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TermType]
    expected_literals = [
        "Fall",
        "Summer",
        "Spring",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TermType"

def test_evaluationtype_exists():
    # Check that the Enumeration exists
    assert EvaluationType is not None

def test_evaluationtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EvaluationType]
    expected_literals = [
        "Participated",
        "Assignments",
        "OralExam",
        "WrittenExam",
        "PracticalExam",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EvaluationType"

def test_personroletype_exists():
    # Check that the Enumeration exists
    assert personRoleType is not None

def test_personroletype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in personRoleType]
    expected_literals = [
        "CourseCordinator",
        "Lecture",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in personRoleType"

def test_courseworktype_exists():
    # Check that the Enumeration exists
    assert CourseWorkType is not None

def test_courseworktype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CourseWorkType]
    expected_literals = [
        "Exercise",
        "Lecture",
        "Lab",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CourseWorkType"

def test_precondistiontype_exists():
    # Check that the Enumeration exists
    assert PrecondistionType is not None

def test_precondistiontype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PrecondistionType]
    expected_literals = [
        "Recommended",
        "Required",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PrecondistionType"


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
coursePages::Reduction_strategy = st.builds(
    coursePages::Reduction,
    creditReduction=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
coursePages::Precondition_strategy = st.builds(
    coursePages::Precondition,
    preconditionStatus=
        safe_text
)
coursePages::CourseWorker_strategy = st.builds(
    coursePages::CourseWorker,
    courseRole=
        safe_text
)
coursePages::CourseInstance_strategy = st.builds(
    coursePages::CourseInstance,
    term=
        safe_text,
    courseYear=
        safe_text
)
coursePages::CourseWork_strategy = st.builds(
    coursePages::CourseWork,
)
coursePages::CourseWorkObject_strategy = st.builds(
    coursePages::CourseWorkObject,
    courseWorkType=
        safe_text,
    end=
        st.dates(),
    start=
        st.dates(),
    room=
        safe_text,
    day=
        safe_text
)
coursePages::Department_strategy = st.builds(
    coursePages::Department,
    phoneNummber=
        safe_text,
    departmentName=
        safe_text,
    email=
        safe_text
)
coursePages::Course_strategy = st.builds(
    coursePages::Course,
    courseCredits=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    courseContent=
        safe_text,
    courseName=
        safe_text,
    courseCode=
        safe_text
)
coursePages::StudyPrograms_strategy = st.builds(
    coursePages::StudyPrograms,
    studyProgramName=
        safe_text,
    studyProgramCode=
        safe_text
)
Person_strategy = st.builds(
    Person,
)
coursePages::Employee_strategy = st.builds(
    coursePages::Employee,
    position=
        safe_text
)
coursePages::Student_strategy = st.builds(
    coursePages::Student,
    studentID=
        safe_text
)
coursePages::Evaluations_strategy = st.builds(
    coursePages::Evaluations,
)
coursePages::EvaluationObject_strategy = st.builds(
    coursePages::EvaluationObject,
    evaluationsForm=
        safe_text,
    term=
        safe_text,
    credits=
        st.integers(),
    date=
        st.dates()
)
coursePages::Person_strategy = st.builds(
    coursePages::Person,
    surName=
        safe_text,
    phoneNummber=
        safe_text,
    email=
        safe_text,
    firstName=
        safe_text
)

@given(instance=coursePages::Reduction_strategy)
@settings(max_examples=50)
def test_coursepages::reduction_instantiation(instance):
    assert isinstance(instance, coursePages::Reduction)

@given(instance=coursePages::Reduction_strategy)
def test_coursepages::reduction_creditReduction_type(instance):
    assert isinstance(instance.creditReduction, float)


@given(instance=coursePages::Reduction_strategy)
def test_coursepages::reduction_creditReduction_setter(instance):
    original = instance.creditReduction
    instance.creditReduction = original
    assert instance.creditReduction == original

@given(instance=coursePages::Precondition_strategy)
@settings(max_examples=50)
def test_coursepages::precondition_instantiation(instance):
    assert isinstance(instance, coursePages::Precondition)

@given(instance=coursePages::Precondition_strategy)
def test_coursepages::precondition_preconditionStatus_type(instance):
    assert isinstance(instance.preconditionStatus, str)


@given(instance=coursePages::Precondition_strategy)
def test_coursepages::precondition_preconditionStatus_setter(instance):
    original = instance.preconditionStatus
    instance.preconditionStatus = original
    assert instance.preconditionStatus == original

@given(instance=coursePages::CourseWorker_strategy)
@settings(max_examples=50)
def test_coursepages::courseworker_instantiation(instance):
    assert isinstance(instance, coursePages::CourseWorker)

@given(instance=coursePages::CourseWorker_strategy)
def test_coursepages::courseworker_courseRole_type(instance):
    assert isinstance(instance.courseRole, str)


@given(instance=coursePages::CourseWorker_strategy)
def test_coursepages::courseworker_courseRole_setter(instance):
    original = instance.courseRole
    instance.courseRole = original
    assert instance.courseRole == original

@given(instance=coursePages::CourseInstance_strategy)
@settings(max_examples=50)
def test_coursepages::courseinstance_instantiation(instance):
    assert isinstance(instance, coursePages::CourseInstance)

@given(instance=coursePages::CourseInstance_strategy)
def test_coursepages::courseinstance_term_type(instance):
    assert isinstance(instance.term, str)


@given(instance=coursePages::CourseInstance_strategy)
def test_coursepages::courseinstance_term_setter(instance):
    original = instance.term
    instance.term = original
    assert instance.term == original

@given(instance=coursePages::CourseInstance_strategy)
def test_coursepages::courseinstance_courseYear_type(instance):
    assert isinstance(instance.courseYear, str)


@given(instance=coursePages::CourseInstance_strategy)
def test_coursepages::courseinstance_courseYear_setter(instance):
    original = instance.courseYear
    instance.courseYear = original
    assert instance.courseYear == original

@given(instance=coursePages::CourseWork_strategy)
@settings(max_examples=50)
def test_coursepages::coursework_instantiation(instance):
    assert isinstance(instance, coursePages::CourseWork)

@given(instance=coursePages::CourseWorkObject_strategy)
@settings(max_examples=50)
def test_coursepages::courseworkobject_instantiation(instance):
    assert isinstance(instance, coursePages::CourseWorkObject)

@given(instance=coursePages::CourseWorkObject_strategy)
def test_coursepages::courseworkobject_courseWorkType_type(instance):
    assert isinstance(instance.courseWorkType, str)


@given(instance=coursePages::CourseWorkObject_strategy)
def test_coursepages::courseworkobject_courseWorkType_setter(instance):
    original = instance.courseWorkType
    instance.courseWorkType = original
    assert instance.courseWorkType == original

@given(instance=coursePages::CourseWorkObject_strategy)
def test_coursepages::courseworkobject_end_type(instance):
    assert isinstance(instance.end, date)


@given(instance=coursePages::CourseWorkObject_strategy)
def test_coursepages::courseworkobject_end_setter(instance):
    original = instance.end
    instance.end = original
    assert instance.end == original

@given(instance=coursePages::CourseWorkObject_strategy)
def test_coursepages::courseworkobject_start_type(instance):
    assert isinstance(instance.start, date)


@given(instance=coursePages::CourseWorkObject_strategy)
def test_coursepages::courseworkobject_start_setter(instance):
    original = instance.start
    instance.start = original
    assert instance.start == original

@given(instance=coursePages::CourseWorkObject_strategy)
def test_coursepages::courseworkobject_room_type(instance):
    assert isinstance(instance.room, str)


@given(instance=coursePages::CourseWorkObject_strategy)
def test_coursepages::courseworkobject_room_setter(instance):
    original = instance.room
    instance.room = original
    assert instance.room == original

@given(instance=coursePages::CourseWorkObject_strategy)
def test_coursepages::courseworkobject_day_type(instance):
    assert isinstance(instance.day, str)


@given(instance=coursePages::CourseWorkObject_strategy)
def test_coursepages::courseworkobject_day_setter(instance):
    original = instance.day
    instance.day = original
    assert instance.day == original

@given(instance=coursePages::Department_strategy)
@settings(max_examples=50)
def test_coursepages::department_instantiation(instance):
    assert isinstance(instance, coursePages::Department)

@given(instance=coursePages::Department_strategy)
def test_coursepages::department_phoneNummber_type(instance):
    assert isinstance(instance.phoneNummber, str)


@given(instance=coursePages::Department_strategy)
def test_coursepages::department_phoneNummber_setter(instance):
    original = instance.phoneNummber
    instance.phoneNummber = original
    assert instance.phoneNummber == original

@given(instance=coursePages::Department_strategy)
def test_coursepages::department_departmentName_type(instance):
    assert isinstance(instance.departmentName, str)


@given(instance=coursePages::Department_strategy)
def test_coursepages::department_departmentName_setter(instance):
    original = instance.departmentName
    instance.departmentName = original
    assert instance.departmentName == original

@given(instance=coursePages::Department_strategy)
def test_coursepages::department_email_type(instance):
    assert isinstance(instance.email, str)


@given(instance=coursePages::Department_strategy)
def test_coursepages::department_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original

@given(instance=coursePages::Course_strategy)
@settings(max_examples=50)
def test_coursepages::course_instantiation(instance):
    assert isinstance(instance, coursePages::Course)

@given(instance=coursePages::Course_strategy)
def test_coursepages::course_courseCredits_type(instance):
    assert isinstance(instance.courseCredits, float)


@given(instance=coursePages::Course_strategy)
def test_coursepages::course_courseCredits_setter(instance):
    original = instance.courseCredits
    instance.courseCredits = original
    assert instance.courseCredits == original

@given(instance=coursePages::Course_strategy)
def test_coursepages::course_courseContent_type(instance):
    assert isinstance(instance.courseContent, str)


@given(instance=coursePages::Course_strategy)
def test_coursepages::course_courseContent_setter(instance):
    original = instance.courseContent
    instance.courseContent = original
    assert instance.courseContent == original

@given(instance=coursePages::Course_strategy)
def test_coursepages::course_courseName_type(instance):
    assert isinstance(instance.courseName, str)


@given(instance=coursePages::Course_strategy)
def test_coursepages::course_courseName_setter(instance):
    original = instance.courseName
    instance.courseName = original
    assert instance.courseName == original

@given(instance=coursePages::Course_strategy)
def test_coursepages::course_courseCode_type(instance):
    assert isinstance(instance.courseCode, str)


@given(instance=coursePages::Course_strategy)
def test_coursepages::course_courseCode_setter(instance):
    original = instance.courseCode
    instance.courseCode = original
    assert instance.courseCode == original

@given(instance=coursePages::StudyPrograms_strategy)
@settings(max_examples=50)
def test_coursepages::studyprograms_instantiation(instance):
    assert isinstance(instance, coursePages::StudyPrograms)

@given(instance=coursePages::StudyPrograms_strategy)
def test_coursepages::studyprograms_studyProgramName_type(instance):
    assert isinstance(instance.studyProgramName, str)


@given(instance=coursePages::StudyPrograms_strategy)
def test_coursepages::studyprograms_studyProgramName_setter(instance):
    original = instance.studyProgramName
    instance.studyProgramName = original
    assert instance.studyProgramName == original

@given(instance=coursePages::StudyPrograms_strategy)
def test_coursepages::studyprograms_studyProgramCode_type(instance):
    assert isinstance(instance.studyProgramCode, str)


@given(instance=coursePages::StudyPrograms_strategy)
def test_coursepages::studyprograms_studyProgramCode_setter(instance):
    original = instance.studyProgramCode
    instance.studyProgramCode = original
    assert instance.studyProgramCode == original

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)

@given(instance=coursePages::Employee_strategy)
@settings(max_examples=50)
def test_coursepages::employee_instantiation(instance):
    assert isinstance(instance, coursePages::Employee)

@given(instance=coursePages::Employee_strategy)
def test_coursepages::employee_position_type(instance):
    assert isinstance(instance.position, str)


@given(instance=coursePages::Employee_strategy)
def test_coursepages::employee_position_setter(instance):
    original = instance.position
    instance.position = original
    assert instance.position == original

@given(instance=coursePages::Student_strategy)
@settings(max_examples=50)
def test_coursepages::student_instantiation(instance):
    assert isinstance(instance, coursePages::Student)

@given(instance=coursePages::Student_strategy)
def test_coursepages::student_studentID_type(instance):
    assert isinstance(instance.studentID, str)


@given(instance=coursePages::Student_strategy)
def test_coursepages::student_studentID_setter(instance):
    original = instance.studentID
    instance.studentID = original
    assert instance.studentID == original

@given(instance=coursePages::Evaluations_strategy)
@settings(max_examples=50)
def test_coursepages::evaluations_instantiation(instance):
    assert isinstance(instance, coursePages::Evaluations)

@given(instance=coursePages::EvaluationObject_strategy)
@settings(max_examples=50)
def test_coursepages::evaluationobject_instantiation(instance):
    assert isinstance(instance, coursePages::EvaluationObject)

@given(instance=coursePages::EvaluationObject_strategy)
def test_coursepages::evaluationobject_evaluationsForm_type(instance):
    assert isinstance(instance.evaluationsForm, str)


@given(instance=coursePages::EvaluationObject_strategy)
def test_coursepages::evaluationobject_evaluationsForm_setter(instance):
    original = instance.evaluationsForm
    instance.evaluationsForm = original
    assert instance.evaluationsForm == original

@given(instance=coursePages::EvaluationObject_strategy)
def test_coursepages::evaluationobject_term_type(instance):
    assert isinstance(instance.term, str)


@given(instance=coursePages::EvaluationObject_strategy)
def test_coursepages::evaluationobject_term_setter(instance):
    original = instance.term
    instance.term = original
    assert instance.term == original

@given(instance=coursePages::EvaluationObject_strategy)
def test_coursepages::evaluationobject_credits_type(instance):
    assert isinstance(instance.credits, int)


@given(instance=coursePages::EvaluationObject_strategy)
def test_coursepages::evaluationobject_credits_setter(instance):
    original = instance.credits
    instance.credits = original
    assert instance.credits == original

@given(instance=coursePages::EvaluationObject_strategy)
def test_coursepages::evaluationobject_date_type(instance):
    assert isinstance(instance.date, date)


@given(instance=coursePages::EvaluationObject_strategy)
def test_coursepages::evaluationobject_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original

@given(instance=coursePages::Person_strategy)
@settings(max_examples=50)
def test_coursepages::person_instantiation(instance):
    assert isinstance(instance, coursePages::Person)

@given(instance=coursePages::Person_strategy)
def test_coursepages::person_surName_type(instance):
    assert isinstance(instance.surName, str)


@given(instance=coursePages::Person_strategy)
def test_coursepages::person_surName_setter(instance):
    original = instance.surName
    instance.surName = original
    assert instance.surName == original

@given(instance=coursePages::Person_strategy)
def test_coursepages::person_phoneNummber_type(instance):
    assert isinstance(instance.phoneNummber, str)


@given(instance=coursePages::Person_strategy)
def test_coursepages::person_phoneNummber_setter(instance):
    original = instance.phoneNummber
    instance.phoneNummber = original
    assert instance.phoneNummber == original

@given(instance=coursePages::Person_strategy)
def test_coursepages::person_email_type(instance):
    assert isinstance(instance.email, str)


@given(instance=coursePages::Person_strategy)
def test_coursepages::person_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original

@given(instance=coursePages::Person_strategy)
def test_coursepages::person_firstName_type(instance):
    assert isinstance(instance.firstName, str)


@given(instance=coursePages::Person_strategy)
def test_coursepages::person_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original
