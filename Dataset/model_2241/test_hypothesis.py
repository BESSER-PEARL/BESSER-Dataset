import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    coursePages_Reduction,
    coursePages_Precondition,
    coursePages_CourseWorker,
    coursePages_CourseInstance,
    coursePages_CourseWork,
    coursePages_CourseWorkObject,
    coursePages_Department,
    coursePages_Course,
    coursePages_StudyPrograms,
    Person,
    coursePages_Employee,
    coursePages_Student,
    coursePages_Evaluations,
    coursePages_EvaluationObject,
    coursePages_Person,
    PrecondistionType,
    personRoleType,
    CourseWorkType,
    EvaluationType,
    TermType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_coursepages_reduction_is_not_abstract():
    assert not inspect.isabstract(coursePages_Reduction)


def test_coursepages_reduction_constructor_exists():
    assert callable(coursePages_Reduction.__init__)


def test_coursepages_reduction_constructor_args():
    sig = inspect.signature(coursePages_Reduction.__init__)
    params = list(sig.parameters.keys())
    assert "creditReduction" in params, "Missing parameter 'creditReduction'"

def test_coursepages_reduction_has_creditReduction():
    assert hasattr(coursePages_Reduction, "creditReduction")
    descriptor = None
    for klass in coursePages_Reduction.__mro__:
        if "creditReduction" in klass.__dict__:
            descriptor = klass.__dict__["creditReduction"]
            break
    assert isinstance(descriptor, property)



def test_coursepages_precondition_is_not_abstract():
    assert not inspect.isabstract(coursePages_Precondition)


def test_coursepages_precondition_constructor_exists():
    assert callable(coursePages_Precondition.__init__)


def test_coursepages_precondition_constructor_args():
    sig = inspect.signature(coursePages_Precondition.__init__)
    params = list(sig.parameters.keys())
    assert "preconditionStatus" in params, "Missing parameter 'preconditionStatus'"

def test_coursepages_precondition_has_preconditionStatus():
    assert hasattr(coursePages_Precondition, "preconditionStatus")
    descriptor = None
    for klass in coursePages_Precondition.__mro__:
        if "preconditionStatus" in klass.__dict__:
            descriptor = klass.__dict__["preconditionStatus"]
            break
    assert isinstance(descriptor, property)



def test_coursepages_courseworker_is_not_abstract():
    assert not inspect.isabstract(coursePages_CourseWorker)


def test_coursepages_courseworker_constructor_exists():
    assert callable(coursePages_CourseWorker.__init__)


def test_coursepages_courseworker_constructor_args():
    sig = inspect.signature(coursePages_CourseWorker.__init__)
    params = list(sig.parameters.keys())
    assert "courseRole" in params, "Missing parameter 'courseRole'"

def test_coursepages_courseworker_has_courseRole():
    assert hasattr(coursePages_CourseWorker, "courseRole")
    descriptor = None
    for klass in coursePages_CourseWorker.__mro__:
        if "courseRole" in klass.__dict__:
            descriptor = klass.__dict__["courseRole"]
            break
    assert isinstance(descriptor, property)



def test_coursepages_courseinstance_is_not_abstract():
    assert not inspect.isabstract(coursePages_CourseInstance)


def test_coursepages_courseinstance_constructor_exists():
    assert callable(coursePages_CourseInstance.__init__)


def test_coursepages_courseinstance_constructor_args():
    sig = inspect.signature(coursePages_CourseInstance.__init__)
    params = list(sig.parameters.keys())
    assert "courseYear" in params, "Missing parameter 'courseYear'"
    assert "term" in params, "Missing parameter 'term'"

def test_coursepages_courseinstance_has_courseYear():
    assert hasattr(coursePages_CourseInstance, "courseYear")
    descriptor = None
    for klass in coursePages_CourseInstance.__mro__:
        if "courseYear" in klass.__dict__:
            descriptor = klass.__dict__["courseYear"]
            break
    assert isinstance(descriptor, property)

def test_coursepages_courseinstance_has_term():
    assert hasattr(coursePages_CourseInstance, "term")
    descriptor = None
    for klass in coursePages_CourseInstance.__mro__:
        if "term" in klass.__dict__:
            descriptor = klass.__dict__["term"]
            break
    assert isinstance(descriptor, property)



def test_coursepages_coursework_is_not_abstract():
    assert not inspect.isabstract(coursePages_CourseWork)


def test_coursepages_coursework_constructor_exists():
    assert callable(coursePages_CourseWork.__init__)


def test_coursepages_coursework_constructor_args():
    sig = inspect.signature(coursePages_CourseWork.__init__)
    params = list(sig.parameters.keys())



def test_coursepages_courseworkobject_is_not_abstract():
    assert not inspect.isabstract(coursePages_CourseWorkObject)


def test_coursepages_courseworkobject_constructor_exists():
    assert callable(coursePages_CourseWorkObject.__init__)


def test_coursepages_courseworkobject_constructor_args():
    sig = inspect.signature(coursePages_CourseWorkObject.__init__)
    params = list(sig.parameters.keys())
    assert "end" in params, "Missing parameter 'end'"
    assert "start" in params, "Missing parameter 'start'"
    assert "day" in params, "Missing parameter 'day'"
    assert "courseWorkType" in params, "Missing parameter 'courseWorkType'"
    assert "room" in params, "Missing parameter 'room'"

def test_coursepages_courseworkobject_has_end():
    assert hasattr(coursePages_CourseWorkObject, "end")
    descriptor = None
    for klass in coursePages_CourseWorkObject.__mro__:
        if "end" in klass.__dict__:
            descriptor = klass.__dict__["end"]
            break
    assert isinstance(descriptor, property)

def test_coursepages_courseworkobject_has_start():
    assert hasattr(coursePages_CourseWorkObject, "start")
    descriptor = None
    for klass in coursePages_CourseWorkObject.__mro__:
        if "start" in klass.__dict__:
            descriptor = klass.__dict__["start"]
            break
    assert isinstance(descriptor, property)

def test_coursepages_courseworkobject_has_day():
    assert hasattr(coursePages_CourseWorkObject, "day")
    descriptor = None
    for klass in coursePages_CourseWorkObject.__mro__:
        if "day" in klass.__dict__:
            descriptor = klass.__dict__["day"]
            break
    assert isinstance(descriptor, property)

def test_coursepages_courseworkobject_has_courseWorkType():
    assert hasattr(coursePages_CourseWorkObject, "courseWorkType")
    descriptor = None
    for klass in coursePages_CourseWorkObject.__mro__:
        if "courseWorkType" in klass.__dict__:
            descriptor = klass.__dict__["courseWorkType"]
            break
    assert isinstance(descriptor, property)

def test_coursepages_courseworkobject_has_room():
    assert hasattr(coursePages_CourseWorkObject, "room")
    descriptor = None
    for klass in coursePages_CourseWorkObject.__mro__:
        if "room" in klass.__dict__:
            descriptor = klass.__dict__["room"]
            break
    assert isinstance(descriptor, property)



def test_coursepages_department_is_not_abstract():
    assert not inspect.isabstract(coursePages_Department)


def test_coursepages_department_constructor_exists():
    assert callable(coursePages_Department.__init__)


def test_coursepages_department_constructor_args():
    sig = inspect.signature(coursePages_Department.__init__)
    params = list(sig.parameters.keys())
    assert "phoneNummber" in params, "Missing parameter 'phoneNummber'"
    assert "email" in params, "Missing parameter 'email'"
    assert "departmentName" in params, "Missing parameter 'departmentName'"

def test_coursepages_department_has_phoneNummber():
    assert hasattr(coursePages_Department, "phoneNummber")
    descriptor = None
    for klass in coursePages_Department.__mro__:
        if "phoneNummber" in klass.__dict__:
            descriptor = klass.__dict__["phoneNummber"]
            break
    assert isinstance(descriptor, property)

def test_coursepages_department_has_email():
    assert hasattr(coursePages_Department, "email")
    descriptor = None
    for klass in coursePages_Department.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)

def test_coursepages_department_has_departmentName():
    assert hasattr(coursePages_Department, "departmentName")
    descriptor = None
    for klass in coursePages_Department.__mro__:
        if "departmentName" in klass.__dict__:
            descriptor = klass.__dict__["departmentName"]
            break
    assert isinstance(descriptor, property)



def test_coursepages_course_is_not_abstract():
    assert not inspect.isabstract(coursePages_Course)


def test_coursepages_course_constructor_exists():
    assert callable(coursePages_Course.__init__)


def test_coursepages_course_constructor_args():
    sig = inspect.signature(coursePages_Course.__init__)
    params = list(sig.parameters.keys())
    assert "courseCredits" in params, "Missing parameter 'courseCredits'"
    assert "courseContent" in params, "Missing parameter 'courseContent'"
    assert "courseCode" in params, "Missing parameter 'courseCode'"
    assert "courseName" in params, "Missing parameter 'courseName'"

def test_coursepages_course_has_courseCredits():
    assert hasattr(coursePages_Course, "courseCredits")
    descriptor = None
    for klass in coursePages_Course.__mro__:
        if "courseCredits" in klass.__dict__:
            descriptor = klass.__dict__["courseCredits"]
            break
    assert isinstance(descriptor, property)

def test_coursepages_course_has_courseContent():
    assert hasattr(coursePages_Course, "courseContent")
    descriptor = None
    for klass in coursePages_Course.__mro__:
        if "courseContent" in klass.__dict__:
            descriptor = klass.__dict__["courseContent"]
            break
    assert isinstance(descriptor, property)

def test_coursepages_course_has_courseCode():
    assert hasattr(coursePages_Course, "courseCode")
    descriptor = None
    for klass in coursePages_Course.__mro__:
        if "courseCode" in klass.__dict__:
            descriptor = klass.__dict__["courseCode"]
            break
    assert isinstance(descriptor, property)

def test_coursepages_course_has_courseName():
    assert hasattr(coursePages_Course, "courseName")
    descriptor = None
    for klass in coursePages_Course.__mro__:
        if "courseName" in klass.__dict__:
            descriptor = klass.__dict__["courseName"]
            break
    assert isinstance(descriptor, property)



def test_coursepages_studyprograms_is_not_abstract():
    assert not inspect.isabstract(coursePages_StudyPrograms)


def test_coursepages_studyprograms_constructor_exists():
    assert callable(coursePages_StudyPrograms.__init__)


def test_coursepages_studyprograms_constructor_args():
    sig = inspect.signature(coursePages_StudyPrograms.__init__)
    params = list(sig.parameters.keys())
    assert "studyProgramCode" in params, "Missing parameter 'studyProgramCode'"
    assert "studyProgramName" in params, "Missing parameter 'studyProgramName'"

def test_coursepages_studyprograms_has_studyProgramCode():
    assert hasattr(coursePages_StudyPrograms, "studyProgramCode")
    descriptor = None
    for klass in coursePages_StudyPrograms.__mro__:
        if "studyProgramCode" in klass.__dict__:
            descriptor = klass.__dict__["studyProgramCode"]
            break
    assert isinstance(descriptor, property)

def test_coursepages_studyprograms_has_studyProgramName():
    assert hasattr(coursePages_StudyPrograms, "studyProgramName")
    descriptor = None
    for klass in coursePages_StudyPrograms.__mro__:
        if "studyProgramName" in klass.__dict__:
            descriptor = klass.__dict__["studyProgramName"]
            break
    assert isinstance(descriptor, property)



def test_person_is_not_abstract():
    assert not inspect.isabstract(Person)


def test_person_constructor_exists():
    assert callable(Person.__init__)


def test_person_constructor_args():
    sig = inspect.signature(Person.__init__)
    params = list(sig.parameters.keys())



def test_coursepages_employee_is_not_abstract():
    assert not inspect.isabstract(coursePages_Employee)


def test_coursepages_employee_constructor_exists():
    assert callable(coursePages_Employee.__init__)


def test_coursepages_employee_constructor_args():
    sig = inspect.signature(coursePages_Employee.__init__)
    params = list(sig.parameters.keys())
    assert "position" in params, "Missing parameter 'position'"

def test_coursepages_employee_has_position():
    assert hasattr(coursePages_Employee, "position")
    descriptor = None
    for klass in coursePages_Employee.__mro__:
        if "position" in klass.__dict__:
            descriptor = klass.__dict__["position"]
            break
    assert isinstance(descriptor, property)



def test_coursepages_student_is_not_abstract():
    assert not inspect.isabstract(coursePages_Student)


def test_coursepages_student_constructor_exists():
    assert callable(coursePages_Student.__init__)


def test_coursepages_student_constructor_args():
    sig = inspect.signature(coursePages_Student.__init__)
    params = list(sig.parameters.keys())
    assert "studentID" in params, "Missing parameter 'studentID'"

def test_coursepages_student_has_studentID():
    assert hasattr(coursePages_Student, "studentID")
    descriptor = None
    for klass in coursePages_Student.__mro__:
        if "studentID" in klass.__dict__:
            descriptor = klass.__dict__["studentID"]
            break
    assert isinstance(descriptor, property)



def test_coursepages_evaluations_is_not_abstract():
    assert not inspect.isabstract(coursePages_Evaluations)


def test_coursepages_evaluations_constructor_exists():
    assert callable(coursePages_Evaluations.__init__)


def test_coursepages_evaluations_constructor_args():
    sig = inspect.signature(coursePages_Evaluations.__init__)
    params = list(sig.parameters.keys())



def test_coursepages_evaluationobject_is_not_abstract():
    assert not inspect.isabstract(coursePages_EvaluationObject)


def test_coursepages_evaluationobject_constructor_exists():
    assert callable(coursePages_EvaluationObject.__init__)


def test_coursepages_evaluationobject_constructor_args():
    sig = inspect.signature(coursePages_EvaluationObject.__init__)
    params = list(sig.parameters.keys())
    assert "date" in params, "Missing parameter 'date'"
    assert "credits" in params, "Missing parameter 'credits'"
    assert "term" in params, "Missing parameter 'term'"
    assert "evaluationsForm" in params, "Missing parameter 'evaluationsForm'"

def test_coursepages_evaluationobject_has_date():
    assert hasattr(coursePages_EvaluationObject, "date")
    descriptor = None
    for klass in coursePages_EvaluationObject.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)

def test_coursepages_evaluationobject_has_credits():
    assert hasattr(coursePages_EvaluationObject, "credits")
    descriptor = None
    for klass in coursePages_EvaluationObject.__mro__:
        if "credits" in klass.__dict__:
            descriptor = klass.__dict__["credits"]
            break
    assert isinstance(descriptor, property)

def test_coursepages_evaluationobject_has_term():
    assert hasattr(coursePages_EvaluationObject, "term")
    descriptor = None
    for klass in coursePages_EvaluationObject.__mro__:
        if "term" in klass.__dict__:
            descriptor = klass.__dict__["term"]
            break
    assert isinstance(descriptor, property)

def test_coursepages_evaluationobject_has_evaluationsForm():
    assert hasattr(coursePages_EvaluationObject, "evaluationsForm")
    descriptor = None
    for klass in coursePages_EvaluationObject.__mro__:
        if "evaluationsForm" in klass.__dict__:
            descriptor = klass.__dict__["evaluationsForm"]
            break
    assert isinstance(descriptor, property)



def test_coursepages_person_is_not_abstract():
    assert not inspect.isabstract(coursePages_Person)


def test_coursepages_person_constructor_exists():
    assert callable(coursePages_Person.__init__)


def test_coursepages_person_constructor_args():
    sig = inspect.signature(coursePages_Person.__init__)
    params = list(sig.parameters.keys())
    assert "surName" in params, "Missing parameter 'surName'"
    assert "email" in params, "Missing parameter 'email'"
    assert "firstName" in params, "Missing parameter 'firstName'"
    assert "phoneNummber" in params, "Missing parameter 'phoneNummber'"

def test_coursepages_person_has_surName():
    assert hasattr(coursePages_Person, "surName")
    descriptor = None
    for klass in coursePages_Person.__mro__:
        if "surName" in klass.__dict__:
            descriptor = klass.__dict__["surName"]
            break
    assert isinstance(descriptor, property)

def test_coursepages_person_has_email():
    assert hasattr(coursePages_Person, "email")
    descriptor = None
    for klass in coursePages_Person.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)

def test_coursepages_person_has_firstName():
    assert hasattr(coursePages_Person, "firstName")
    descriptor = None
    for klass in coursePages_Person.__mro__:
        if "firstName" in klass.__dict__:
            descriptor = klass.__dict__["firstName"]
            break
    assert isinstance(descriptor, property)

def test_coursepages_person_has_phoneNummber():
    assert hasattr(coursePages_Person, "phoneNummber")
    descriptor = None
    for klass in coursePages_Person.__mro__:
        if "phoneNummber" in klass.__dict__:
            descriptor = klass.__dict__["phoneNummber"]
            break
    assert isinstance(descriptor, property)

def test_precondistiontype_exists():
    # Check that the Enumeration exists
    assert PrecondistionType is not None

def test_precondistiontype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PrecondistionType]
    expected_literals = [
        "Required",
        "Recommended",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PrecondistionType"

def test_personroletype_exists():
    # Check that the Enumeration exists
    assert personRoleType is not None

def test_personroletype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in personRoleType]
    expected_literals = [
        "Lecture",
        "CourseCordinator",
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
        "Lab",
        "Lecture",
        "Exercise",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CourseWorkType"

def test_evaluationtype_exists():
    # Check that the Enumeration exists
    assert EvaluationType is not None

def test_evaluationtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EvaluationType]
    expected_literals = [
        "WrittenExam",
        "Assignments",
        "PracticalExam",
        "OralExam",
        "Participated",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EvaluationType"

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
coursePages_Reduction_strategy = st.builds(
    coursePages_Reduction,
    creditReduction=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
coursePages_Precondition_strategy = st.builds(
    coursePages_Precondition,
    preconditionStatus=
        safe_text
)
coursePages_CourseWorker_strategy = st.builds(
    coursePages_CourseWorker,
    courseRole=
        safe_text
)
coursePages_CourseInstance_strategy = st.builds(
    coursePages_CourseInstance,
    courseYear=
        safe_text,
    term=
        safe_text
)
coursePages_CourseWork_strategy = st.builds(
    coursePages_CourseWork,
)
coursePages_CourseWorkObject_strategy = st.builds(
    coursePages_CourseWorkObject,
    end=
        st.dates(),
    start=
        st.dates(),
    day=
        safe_text,
    courseWorkType=
        safe_text,
    room=
        safe_text
)
coursePages_Department_strategy = st.builds(
    coursePages_Department,
    phoneNummber=
        safe_text,
    email=
        safe_text,
    departmentName=
        safe_text
)
coursePages_Course_strategy = st.builds(
    coursePages_Course,
    courseCredits=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    courseContent=
        safe_text,
    courseCode=
        safe_text,
    courseName=
        safe_text
)
coursePages_StudyPrograms_strategy = st.builds(
    coursePages_StudyPrograms,
    studyProgramCode=
        safe_text,
    studyProgramName=
        safe_text
)
Person_strategy = st.builds(
    Person,
)
coursePages_Employee_strategy = st.builds(
    coursePages_Employee,
    position=
        safe_text
)
coursePages_Student_strategy = st.builds(
    coursePages_Student,
    studentID=
        safe_text
)
coursePages_Evaluations_strategy = st.builds(
    coursePages_Evaluations,
)
coursePages_EvaluationObject_strategy = st.builds(
    coursePages_EvaluationObject,
    date=
        st.dates(),
    credits=
        st.integers(),
    term=
        safe_text,
    evaluationsForm=
        safe_text
)
coursePages_Person_strategy = st.builds(
    coursePages_Person,
    surName=
        safe_text,
    email=
        safe_text,
    firstName=
        safe_text,
    phoneNummber=
        safe_text
)

@given(instance=coursePages_Reduction_strategy)
@settings(max_examples=50)
def test_coursepages_reduction_instantiation(instance):
    assert isinstance(instance, coursePages_Reduction)



@given(instance=coursePages_Reduction_strategy)
def test_coursepages_reduction_creditReduction_setter(instance):
    original = instance.creditReduction
    instance.creditReduction = original
    assert instance.creditReduction == original

@given(instance=coursePages_Precondition_strategy)
@settings(max_examples=50)
def test_coursepages_precondition_instantiation(instance):
    assert isinstance(instance, coursePages_Precondition)



@given(instance=coursePages_Precondition_strategy)
def test_coursepages_precondition_preconditionStatus_setter(instance):
    original = instance.preconditionStatus
    instance.preconditionStatus = original
    assert instance.preconditionStatus == original

@given(instance=coursePages_CourseWorker_strategy)
@settings(max_examples=50)
def test_coursepages_courseworker_instantiation(instance):
    assert isinstance(instance, coursePages_CourseWorker)



@given(instance=coursePages_CourseWorker_strategy)
def test_coursepages_courseworker_courseRole_setter(instance):
    original = instance.courseRole
    instance.courseRole = original
    assert instance.courseRole == original

@given(instance=coursePages_CourseInstance_strategy)
@settings(max_examples=50)
def test_coursepages_courseinstance_instantiation(instance):
    assert isinstance(instance, coursePages_CourseInstance)



@given(instance=coursePages_CourseInstance_strategy)
def test_coursepages_courseinstance_courseYear_setter(instance):
    original = instance.courseYear
    instance.courseYear = original
    assert instance.courseYear == original



@given(instance=coursePages_CourseInstance_strategy)
def test_coursepages_courseinstance_term_setter(instance):
    original = instance.term
    instance.term = original
    assert instance.term == original

@given(instance=coursePages_CourseWork_strategy)
@settings(max_examples=50)
def test_coursepages_coursework_instantiation(instance):
    assert isinstance(instance, coursePages_CourseWork)

@given(instance=coursePages_CourseWorkObject_strategy)
@settings(max_examples=50)
def test_coursepages_courseworkobject_instantiation(instance):
    assert isinstance(instance, coursePages_CourseWorkObject)



@given(instance=coursePages_CourseWorkObject_strategy)
def test_coursepages_courseworkobject_end_setter(instance):
    original = instance.end
    instance.end = original
    assert instance.end == original



@given(instance=coursePages_CourseWorkObject_strategy)
def test_coursepages_courseworkobject_start_setter(instance):
    original = instance.start
    instance.start = original
    assert instance.start == original



@given(instance=coursePages_CourseWorkObject_strategy)
def test_coursepages_courseworkobject_day_setter(instance):
    original = instance.day
    instance.day = original
    assert instance.day == original



@given(instance=coursePages_CourseWorkObject_strategy)
def test_coursepages_courseworkobject_courseWorkType_setter(instance):
    original = instance.courseWorkType
    instance.courseWorkType = original
    assert instance.courseWorkType == original



@given(instance=coursePages_CourseWorkObject_strategy)
def test_coursepages_courseworkobject_room_setter(instance):
    original = instance.room
    instance.room = original
    assert instance.room == original

@given(instance=coursePages_Department_strategy)
@settings(max_examples=50)
def test_coursepages_department_instantiation(instance):
    assert isinstance(instance, coursePages_Department)



@given(instance=coursePages_Department_strategy)
def test_coursepages_department_phoneNummber_setter(instance):
    original = instance.phoneNummber
    instance.phoneNummber = original
    assert instance.phoneNummber == original



@given(instance=coursePages_Department_strategy)
def test_coursepages_department_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=coursePages_Department_strategy)
def test_coursepages_department_departmentName_setter(instance):
    original = instance.departmentName
    instance.departmentName = original
    assert instance.departmentName == original

@given(instance=coursePages_Course_strategy)
@settings(max_examples=50)
def test_coursepages_course_instantiation(instance):
    assert isinstance(instance, coursePages_Course)



@given(instance=coursePages_Course_strategy)
def test_coursepages_course_courseCredits_setter(instance):
    original = instance.courseCredits
    instance.courseCredits = original
    assert instance.courseCredits == original



@given(instance=coursePages_Course_strategy)
def test_coursepages_course_courseContent_setter(instance):
    original = instance.courseContent
    instance.courseContent = original
    assert instance.courseContent == original



@given(instance=coursePages_Course_strategy)
def test_coursepages_course_courseCode_setter(instance):
    original = instance.courseCode
    instance.courseCode = original
    assert instance.courseCode == original



@given(instance=coursePages_Course_strategy)
def test_coursepages_course_courseName_setter(instance):
    original = instance.courseName
    instance.courseName = original
    assert instance.courseName == original

@given(instance=coursePages_StudyPrograms_strategy)
@settings(max_examples=50)
def test_coursepages_studyprograms_instantiation(instance):
    assert isinstance(instance, coursePages_StudyPrograms)



@given(instance=coursePages_StudyPrograms_strategy)
def test_coursepages_studyprograms_studyProgramCode_setter(instance):
    original = instance.studyProgramCode
    instance.studyProgramCode = original
    assert instance.studyProgramCode == original



@given(instance=coursePages_StudyPrograms_strategy)
def test_coursepages_studyprograms_studyProgramName_setter(instance):
    original = instance.studyProgramName
    instance.studyProgramName = original
    assert instance.studyProgramName == original

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)

@given(instance=coursePages_Employee_strategy)
@settings(max_examples=50)
def test_coursepages_employee_instantiation(instance):
    assert isinstance(instance, coursePages_Employee)



@given(instance=coursePages_Employee_strategy)
def test_coursepages_employee_position_setter(instance):
    original = instance.position
    instance.position = original
    assert instance.position == original

@given(instance=coursePages_Student_strategy)
@settings(max_examples=50)
def test_coursepages_student_instantiation(instance):
    assert isinstance(instance, coursePages_Student)



@given(instance=coursePages_Student_strategy)
def test_coursepages_student_studentID_setter(instance):
    original = instance.studentID
    instance.studentID = original
    assert instance.studentID == original

@given(instance=coursePages_Evaluations_strategy)
@settings(max_examples=50)
def test_coursepages_evaluations_instantiation(instance):
    assert isinstance(instance, coursePages_Evaluations)

@given(instance=coursePages_EvaluationObject_strategy)
@settings(max_examples=50)
def test_coursepages_evaluationobject_instantiation(instance):
    assert isinstance(instance, coursePages_EvaluationObject)



@given(instance=coursePages_EvaluationObject_strategy)
def test_coursepages_evaluationobject_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original



@given(instance=coursePages_EvaluationObject_strategy)
def test_coursepages_evaluationobject_credits_setter(instance):
    original = instance.credits
    instance.credits = original
    assert instance.credits == original



@given(instance=coursePages_EvaluationObject_strategy)
def test_coursepages_evaluationobject_term_setter(instance):
    original = instance.term
    instance.term = original
    assert instance.term == original



@given(instance=coursePages_EvaluationObject_strategy)
def test_coursepages_evaluationobject_evaluationsForm_setter(instance):
    original = instance.evaluationsForm
    instance.evaluationsForm = original
    assert instance.evaluationsForm == original

@given(instance=coursePages_Person_strategy)
@settings(max_examples=50)
def test_coursepages_person_instantiation(instance):
    assert isinstance(instance, coursePages_Person)



@given(instance=coursePages_Person_strategy)
def test_coursepages_person_surName_setter(instance):
    original = instance.surName
    instance.surName = original
    assert instance.surName == original



@given(instance=coursePages_Person_strategy)
def test_coursepages_person_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=coursePages_Person_strategy)
def test_coursepages_person_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original



@given(instance=coursePages_Person_strategy)
def test_coursepages_person_phoneNummber_setter(instance):
    original = instance.phoneNummber
    instance.phoneNummber = original
    assert instance.phoneNummber == original
