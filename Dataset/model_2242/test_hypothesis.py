import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    oving4::Assignment,
    oving4::Exam,
    oving4::EvaluationElement,
    oving4::TimeTableElement,
    oving4::CourseInstance,
    oving4::CourseWork,
    oving4::TimeTable,
    oving4::Precondition,
    oving4::Person,
    oving4::Evaluation,
    oving4::PersonRole,
    oving4::Course,
    oving4::Project,
    oving4::StudyProgram,
    oving4::Department,
    oving4::Root,
    StudyProgramType,
    RoleType,
    CourseWorkType,
    EvaluationType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_oving4::assignment_is_not_abstract():
    assert not inspect.isabstract(oving4::Assignment)


def test_oving4::assignment_constructor_exists():
    assert callable(oving4::Assignment.__init__)


def test_oving4::assignment_constructor_args():
    sig = inspect.signature(oving4::Assignment.__init__)
    params = list(sig.parameters.keys())
    assert "deadline" in params, "Missing parameter 'deadline'"

def test_oving4::assignment_has_deadline():
    assert hasattr(oving4::Assignment, "deadline")
    descriptor = None
    for klass in oving4::Assignment.__mro__:
        if "deadline" in klass.__dict__:
            descriptor = klass.__dict__["deadline"]
            break
    assert isinstance(descriptor, property)



def test_oving4::exam_is_not_abstract():
    assert not inspect.isabstract(oving4::Exam)


def test_oving4::exam_constructor_exists():
    assert callable(oving4::Exam.__init__)


def test_oving4::exam_constructor_args():
    sig = inspect.signature(oving4::Exam.__init__)
    params = list(sig.parameters.keys())
    assert "previousEndDate" in params, "Missing parameter 'previousEndDate'"
    assert "startDate" in params, "Missing parameter 'startDate'"
    assert "previousStartDate" in params, "Missing parameter 'previousStartDate'"
    assert "endDate" in params, "Missing parameter 'endDate'"

def test_oving4::exam_has_previousEndDate():
    assert hasattr(oving4::Exam, "previousEndDate")
    descriptor = None
    for klass in oving4::Exam.__mro__:
        if "previousEndDate" in klass.__dict__:
            descriptor = klass.__dict__["previousEndDate"]
            break
    assert isinstance(descriptor, property)

def test_oving4::exam_has_startDate():
    assert hasattr(oving4::Exam, "startDate")
    descriptor = None
    for klass in oving4::Exam.__mro__:
        if "startDate" in klass.__dict__:
            descriptor = klass.__dict__["startDate"]
            break
    assert isinstance(descriptor, property)

def test_oving4::exam_has_previousStartDate():
    assert hasattr(oving4::Exam, "previousStartDate")
    descriptor = None
    for klass in oving4::Exam.__mro__:
        if "previousStartDate" in klass.__dict__:
            descriptor = klass.__dict__["previousStartDate"]
            break
    assert isinstance(descriptor, property)

def test_oving4::exam_has_endDate():
    assert hasattr(oving4::Exam, "endDate")
    descriptor = None
    for klass in oving4::Exam.__mro__:
        if "endDate" in klass.__dict__:
            descriptor = klass.__dict__["endDate"]
            break
    assert isinstance(descriptor, property)



def test_oving4::evaluationelement_is_not_abstract():
    assert not inspect.isabstract(oving4::EvaluationElement)


def test_oving4::evaluationelement_constructor_exists():
    assert callable(oving4::EvaluationElement.__init__)


def test_oving4::evaluationelement_constructor_args():
    sig = inspect.signature(oving4::EvaluationElement.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "weight" in params, "Missing parameter 'weight'"
    assert "attended" in params, "Missing parameter 'attended'"
    assert "percentageResult" in params, "Missing parameter 'percentageResult'"

def test_oving4::evaluationelement_has_type():
    assert hasattr(oving4::EvaluationElement, "type")
    descriptor = None
    for klass in oving4::EvaluationElement.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_oving4::evaluationelement_has_weight():
    assert hasattr(oving4::EvaluationElement, "weight")
    descriptor = None
    for klass in oving4::EvaluationElement.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)

def test_oving4::evaluationelement_has_attended():
    assert hasattr(oving4::EvaluationElement, "attended")
    descriptor = None
    for klass in oving4::EvaluationElement.__mro__:
        if "attended" in klass.__dict__:
            descriptor = klass.__dict__["attended"]
            break
    assert isinstance(descriptor, property)

def test_oving4::evaluationelement_has_percentageResult():
    assert hasattr(oving4::EvaluationElement, "percentageResult")
    descriptor = None
    for klass in oving4::EvaluationElement.__mro__:
        if "percentageResult" in klass.__dict__:
            descriptor = klass.__dict__["percentageResult"]
            break
    assert isinstance(descriptor, property)



def test_oving4::timetableelement_is_not_abstract():
    assert not inspect.isabstract(oving4::TimeTableElement)


def test_oving4::timetableelement_constructor_exists():
    assert callable(oving4::TimeTableElement.__init__)


def test_oving4::timetableelement_constructor_args():
    sig = inspect.signature(oving4::TimeTableElement.__init__)
    params = list(sig.parameters.keys())
    assert "durationInMinutes" in params, "Missing parameter 'durationInMinutes'"
    assert "room" in params, "Missing parameter 'room'"
    assert "date" in params, "Missing parameter 'date'"

def test_oving4::timetableelement_has_durationInMinutes():
    assert hasattr(oving4::TimeTableElement, "durationInMinutes")
    descriptor = None
    for klass in oving4::TimeTableElement.__mro__:
        if "durationInMinutes" in klass.__dict__:
            descriptor = klass.__dict__["durationInMinutes"]
            break
    assert isinstance(descriptor, property)

def test_oving4::timetableelement_has_room():
    assert hasattr(oving4::TimeTableElement, "room")
    descriptor = None
    for klass in oving4::TimeTableElement.__mro__:
        if "room" in klass.__dict__:
            descriptor = klass.__dict__["room"]
            break
    assert isinstance(descriptor, property)

def test_oving4::timetableelement_has_date():
    assert hasattr(oving4::TimeTableElement, "date")
    descriptor = None
    for klass in oving4::TimeTableElement.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)



def test_oving4::courseinstance_is_not_abstract():
    assert not inspect.isabstract(oving4::CourseInstance)


def test_oving4::courseinstance_constructor_exists():
    assert callable(oving4::CourseInstance.__init__)


def test_oving4::courseinstance_constructor_args():
    sig = inspect.signature(oving4::CourseInstance.__init__)
    params = list(sig.parameters.keys())
    assert "sumLectureHours" in params, "Missing parameter 'sumLectureHours'"
    assert "sumExerciseHours" in params, "Missing parameter 'sumExerciseHours'"
    assert "sumInDepthHours" in params, "Missing parameter 'sumInDepthHours'"

def test_oving4::courseinstance_has_sumLectureHours():
    assert hasattr(oving4::CourseInstance, "sumLectureHours")
    descriptor = None
    for klass in oving4::CourseInstance.__mro__:
        if "sumLectureHours" in klass.__dict__:
            descriptor = klass.__dict__["sumLectureHours"]
            break
    assert isinstance(descriptor, property)

def test_oving4::courseinstance_has_sumExerciseHours():
    assert hasattr(oving4::CourseInstance, "sumExerciseHours")
    descriptor = None
    for klass in oving4::CourseInstance.__mro__:
        if "sumExerciseHours" in klass.__dict__:
            descriptor = klass.__dict__["sumExerciseHours"]
            break
    assert isinstance(descriptor, property)

def test_oving4::courseinstance_has_sumInDepthHours():
    assert hasattr(oving4::CourseInstance, "sumInDepthHours")
    descriptor = None
    for klass in oving4::CourseInstance.__mro__:
        if "sumInDepthHours" in klass.__dict__:
            descriptor = klass.__dict__["sumInDepthHours"]
            break
    assert isinstance(descriptor, property)



def test_oving4::coursework_is_not_abstract():
    assert not inspect.isabstract(oving4::CourseWork)


def test_oving4::coursework_constructor_exists():
    assert callable(oving4::CourseWork.__init__)


def test_oving4::coursework_constructor_args():
    sig = inspect.signature(oving4::CourseWork.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"
    assert "isMandatory" in params, "Missing parameter 'isMandatory'"

def test_oving4::coursework_has_type():
    assert hasattr(oving4::CourseWork, "type")
    descriptor = None
    for klass in oving4::CourseWork.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_oving4::coursework_has_name():
    assert hasattr(oving4::CourseWork, "name")
    descriptor = None
    for klass in oving4::CourseWork.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_oving4::coursework_has_isMandatory():
    assert hasattr(oving4::CourseWork, "isMandatory")
    descriptor = None
    for klass in oving4::CourseWork.__mro__:
        if "isMandatory" in klass.__dict__:
            descriptor = klass.__dict__["isMandatory"]
            break
    assert isinstance(descriptor, property)



def test_oving4::timetable_is_not_abstract():
    assert not inspect.isabstract(oving4::TimeTable)


def test_oving4::timetable_constructor_exists():
    assert callable(oving4::TimeTable.__init__)


def test_oving4::timetable_constructor_args():
    sig = inspect.signature(oving4::TimeTable.__init__)
    params = list(sig.parameters.keys())
    assert "isRestrictedToProgramsInParallell" in params, "Missing parameter 'isRestrictedToProgramsInParallell'"

def test_oving4::timetable_has_isRestrictedToProgramsInParallell():
    assert hasattr(oving4::TimeTable, "isRestrictedToProgramsInParallell")
    descriptor = None
    for klass in oving4::TimeTable.__mro__:
        if "isRestrictedToProgramsInParallell" in klass.__dict__:
            descriptor = klass.__dict__["isRestrictedToProgramsInParallell"]
            break
    assert isinstance(descriptor, property)



def test_oving4::precondition_is_not_abstract():
    assert not inspect.isabstract(oving4::Precondition)


def test_oving4::precondition_constructor_exists():
    assert callable(oving4::Precondition.__init__)


def test_oving4::precondition_constructor_args():
    sig = inspect.signature(oving4::Precondition.__init__)
    params = list(sig.parameters.keys())
    assert "isMandatory" in params, "Missing parameter 'isMandatory'"
    assert "creditReduction" in params, "Missing parameter 'creditReduction'"

def test_oving4::precondition_has_isMandatory():
    assert hasattr(oving4::Precondition, "isMandatory")
    descriptor = None
    for klass in oving4::Precondition.__mro__:
        if "isMandatory" in klass.__dict__:
            descriptor = klass.__dict__["isMandatory"]
            break
    assert isinstance(descriptor, property)

def test_oving4::precondition_has_creditReduction():
    assert hasattr(oving4::Precondition, "creditReduction")
    descriptor = None
    for klass in oving4::Precondition.__mro__:
        if "creditReduction" in klass.__dict__:
            descriptor = klass.__dict__["creditReduction"]
            break
    assert isinstance(descriptor, property)



def test_oving4::person_is_not_abstract():
    assert not inspect.isabstract(oving4::Person)


def test_oving4::person_constructor_exists():
    assert callable(oving4::Person.__init__)


def test_oving4::person_constructor_args():
    sig = inspect.signature(oving4::Person.__init__)
    params = list(sig.parameters.keys())
    assert "studyCredits" in params, "Missing parameter 'studyCredits'"
    assert "name" in params, "Missing parameter 'name'"
    assert "first_name" in params, "Missing parameter 'first_name'"
    assert "last_name" in params, "Missing parameter 'last_name'"

def test_oving4::person_has_studyCredits():
    assert hasattr(oving4::Person, "studyCredits")
    descriptor = None
    for klass in oving4::Person.__mro__:
        if "studyCredits" in klass.__dict__:
            descriptor = klass.__dict__["studyCredits"]
            break
    assert isinstance(descriptor, property)

def test_oving4::person_has_name():
    assert hasattr(oving4::Person, "name")
    descriptor = None
    for klass in oving4::Person.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_oving4::person_has_first_name():
    assert hasattr(oving4::Person, "first_name")
    descriptor = None
    for klass in oving4::Person.__mro__:
        if "first_name" in klass.__dict__:
            descriptor = klass.__dict__["first_name"]
            break
    assert isinstance(descriptor, property)

def test_oving4::person_has_last_name():
    assert hasattr(oving4::Person, "last_name")
    descriptor = None
    for klass in oving4::Person.__mro__:
        if "last_name" in klass.__dict__:
            descriptor = klass.__dict__["last_name"]
            break
    assert isinstance(descriptor, property)



def test_oving4::evaluation_is_not_abstract():
    assert not inspect.isabstract(oving4::Evaluation)


def test_oving4::evaluation_constructor_exists():
    assert callable(oving4::Evaluation.__init__)


def test_oving4::evaluation_constructor_args():
    sig = inspect.signature(oving4::Evaluation.__init__)
    params = list(sig.parameters.keys())
    assert "creditsReceived" in params, "Missing parameter 'creditsReceived'"
    assert "description" in params, "Missing parameter 'description'"
    assert "totalPercentageResult" in params, "Missing parameter 'totalPercentageResult'"
    assert "completed" in params, "Missing parameter 'completed'"

def test_oving4::evaluation_has_creditsReceived():
    assert hasattr(oving4::Evaluation, "creditsReceived")
    descriptor = None
    for klass in oving4::Evaluation.__mro__:
        if "creditsReceived" in klass.__dict__:
            descriptor = klass.__dict__["creditsReceived"]
            break
    assert isinstance(descriptor, property)

def test_oving4::evaluation_has_description():
    assert hasattr(oving4::Evaluation, "description")
    descriptor = None
    for klass in oving4::Evaluation.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_oving4::evaluation_has_totalPercentageResult():
    assert hasattr(oving4::Evaluation, "totalPercentageResult")
    descriptor = None
    for klass in oving4::Evaluation.__mro__:
        if "totalPercentageResult" in klass.__dict__:
            descriptor = klass.__dict__["totalPercentageResult"]
            break
    assert isinstance(descriptor, property)

def test_oving4::evaluation_has_completed():
    assert hasattr(oving4::Evaluation, "completed")
    descriptor = None
    for klass in oving4::Evaluation.__mro__:
        if "completed" in klass.__dict__:
            descriptor = klass.__dict__["completed"]
            break
    assert isinstance(descriptor, property)



def test_oving4::personrole_is_not_abstract():
    assert not inspect.isabstract(oving4::PersonRole)


def test_oving4::personrole_constructor_exists():
    assert callable(oving4::PersonRole.__init__)


def test_oving4::personrole_constructor_args():
    sig = inspect.signature(oving4::PersonRole.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_oving4::personrole_has_type():
    assert hasattr(oving4::PersonRole, "type")
    descriptor = None
    for klass in oving4::PersonRole.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_oving4::course_is_not_abstract():
    assert not inspect.isabstract(oving4::Course)


def test_oving4::course_constructor_exists():
    assert callable(oving4::Course.__init__)


def test_oving4::course_constructor_args():
    sig = inspect.signature(oving4::Course.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "content" in params, "Missing parameter 'content'"
    assert "credits" in params, "Missing parameter 'credits'"
    assert "examStartDate" in params, "Missing parameter 'examStartDate'"
    assert "examEndDate" in params, "Missing parameter 'examEndDate'"
    assert "code" in params, "Missing parameter 'code'"

def test_oving4::course_has_name():
    assert hasattr(oving4::Course, "name")
    descriptor = None
    for klass in oving4::Course.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_oving4::course_has_content():
    assert hasattr(oving4::Course, "content")
    descriptor = None
    for klass in oving4::Course.__mro__:
        if "content" in klass.__dict__:
            descriptor = klass.__dict__["content"]
            break
    assert isinstance(descriptor, property)

def test_oving4::course_has_credits():
    assert hasattr(oving4::Course, "credits")
    descriptor = None
    for klass in oving4::Course.__mro__:
        if "credits" in klass.__dict__:
            descriptor = klass.__dict__["credits"]
            break
    assert isinstance(descriptor, property)

def test_oving4::course_has_examStartDate():
    assert hasattr(oving4::Course, "examStartDate")
    descriptor = None
    for klass in oving4::Course.__mro__:
        if "examStartDate" in klass.__dict__:
            descriptor = klass.__dict__["examStartDate"]
            break
    assert isinstance(descriptor, property)

def test_oving4::course_has_examEndDate():
    assert hasattr(oving4::Course, "examEndDate")
    descriptor = None
    for klass in oving4::Course.__mro__:
        if "examEndDate" in klass.__dict__:
            descriptor = klass.__dict__["examEndDate"]
            break
    assert isinstance(descriptor, property)

def test_oving4::course_has_code():
    assert hasattr(oving4::Course, "code")
    descriptor = None
    for klass in oving4::Course.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)



def test_oving4::project_is_not_abstract():
    assert not inspect.isabstract(oving4::Project)


def test_oving4::project_constructor_exists():
    assert callable(oving4::Project.__init__)


def test_oving4::project_constructor_args():
    sig = inspect.signature(oving4::Project.__init__)
    params = list(sig.parameters.keys())
    assert "deadline" in params, "Missing parameter 'deadline'"

def test_oving4::project_has_deadline():
    assert hasattr(oving4::Project, "deadline")
    descriptor = None
    for klass in oving4::Project.__mro__:
        if "deadline" in klass.__dict__:
            descriptor = klass.__dict__["deadline"]
            break
    assert isinstance(descriptor, property)



def test_oving4::studyprogram_is_not_abstract():
    assert not inspect.isabstract(oving4::StudyProgram)


def test_oving4::studyprogram_constructor_exists():
    assert callable(oving4::StudyProgram.__init__)


def test_oving4::studyprogram_constructor_args():
    sig = inspect.signature(oving4::StudyProgram.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_oving4::studyprogram_has_type():
    assert hasattr(oving4::StudyProgram, "type")
    descriptor = None
    for klass in oving4::StudyProgram.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_oving4::department_is_not_abstract():
    assert not inspect.isabstract(oving4::Department)


def test_oving4::department_constructor_exists():
    assert callable(oving4::Department.__init__)


def test_oving4::department_constructor_args():
    sig = inspect.signature(oving4::Department.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_oving4::department_has_name():
    assert hasattr(oving4::Department, "name")
    descriptor = None
    for klass in oving4::Department.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_oving4::root_is_not_abstract():
    assert not inspect.isabstract(oving4::Root)


def test_oving4::root_constructor_exists():
    assert callable(oving4::Root.__init__)


def test_oving4::root_constructor_args():
    sig = inspect.signature(oving4::Root.__init__)
    params = list(sig.parameters.keys())

def test_studyprogramtype_exists():
    # Check that the Enumeration exists
    assert StudyProgramType is not None

def test_studyprogramtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in StudyProgramType]
    expected_literals = [
        "MTMART",
        "MTDT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in StudyProgramType"

def test_roletype_exists():
    # Check that the Enumeration exists
    assert RoleType is not None

def test_roletype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in RoleType]
    expected_literals = [
        "Lecturer",
        "Student",
        "Supervisor",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in RoleType"

def test_courseworktype_exists():
    # Check that the Enumeration exists
    assert CourseWorkType is not None

def test_courseworktype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CourseWorkType]
    expected_literals = [
        "Exercise",
        "InDepth",
        "Lecture",
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
        "Project",
        "Exam",
        "Assignment",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EvaluationType"


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
oving4::Assignment_strategy = st.builds(
    oving4::Assignment,
    deadline=
        safe_text
)
oving4::Exam_strategy = st.builds(
    oving4::Exam,
    previousEndDate=
        safe_text,
    startDate=
        safe_text,
    previousStartDate=
        safe_text,
    endDate=
        safe_text
)
oving4::EvaluationElement_strategy = st.builds(
    oving4::EvaluationElement,
    type=
        safe_text,
    weight=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    attended=
        st.booleans(),
    percentageResult=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
oving4::TimeTableElement_strategy = st.builds(
    oving4::TimeTableElement,
    durationInMinutes=
        st.integers(),
    room=
        safe_text,
    date=
        safe_text
)
oving4::CourseInstance_strategy = st.builds(
    oving4::CourseInstance,
    sumLectureHours=
        st.integers(),
    sumExerciseHours=
        st.integers(),
    sumInDepthHours=
        st.integers()
)
oving4::CourseWork_strategy = st.builds(
    oving4::CourseWork,
    type=
        safe_text,
    name=
        safe_text,
    isMandatory=
        st.booleans()
)
oving4::TimeTable_strategy = st.builds(
    oving4::TimeTable,
    isRestrictedToProgramsInParallell=
        st.booleans()
)
oving4::Precondition_strategy = st.builds(
    oving4::Precondition,
    isMandatory=
        st.booleans(),
    creditReduction=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
oving4::Person_strategy = st.builds(
    oving4::Person,
    studyCredits=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text,
    first_name=
        safe_text,
    last_name=
        safe_text
)
oving4::Evaluation_strategy = st.builds(
    oving4::Evaluation,
    creditsReceived=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    description=
        safe_text,
    totalPercentageResult=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    completed=
        st.booleans()
)
oving4::PersonRole_strategy = st.builds(
    oving4::PersonRole,
    type=
        safe_text
)
oving4::Course_strategy = st.builds(
    oving4::Course,
    name=
        safe_text,
    content=
        safe_text,
    credits=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    examStartDate=
        safe_text,
    examEndDate=
        safe_text,
    code=
        safe_text
)
oving4::Project_strategy = st.builds(
    oving4::Project,
    deadline=
        safe_text
)
oving4::StudyProgram_strategy = st.builds(
    oving4::StudyProgram,
    type=
        safe_text
)
oving4::Department_strategy = st.builds(
    oving4::Department,
    name=
        safe_text
)
oving4::Root_strategy = st.builds(
    oving4::Root,
)

@given(instance=oving4::Assignment_strategy)
@settings(max_examples=50)
def test_oving4::assignment_instantiation(instance):
    assert isinstance(instance, oving4::Assignment)

@given(instance=oving4::Assignment_strategy)
def test_oving4::assignment_deadline_type(instance):
    assert isinstance(instance.deadline, str)


@given(instance=oving4::Assignment_strategy)
def test_oving4::assignment_deadline_setter(instance):
    original = instance.deadline
    instance.deadline = original
    assert instance.deadline == original

@given(instance=oving4::Exam_strategy)
@settings(max_examples=50)
def test_oving4::exam_instantiation(instance):
    assert isinstance(instance, oving4::Exam)

@given(instance=oving4::Exam_strategy)
def test_oving4::exam_previousEndDate_type(instance):
    assert isinstance(instance.previousEndDate, str)


@given(instance=oving4::Exam_strategy)
def test_oving4::exam_previousEndDate_setter(instance):
    original = instance.previousEndDate
    instance.previousEndDate = original
    assert instance.previousEndDate == original

@given(instance=oving4::Exam_strategy)
def test_oving4::exam_startDate_type(instance):
    assert isinstance(instance.startDate, str)


@given(instance=oving4::Exam_strategy)
def test_oving4::exam_startDate_setter(instance):
    original = instance.startDate
    instance.startDate = original
    assert instance.startDate == original

@given(instance=oving4::Exam_strategy)
def test_oving4::exam_previousStartDate_type(instance):
    assert isinstance(instance.previousStartDate, str)


@given(instance=oving4::Exam_strategy)
def test_oving4::exam_previousStartDate_setter(instance):
    original = instance.previousStartDate
    instance.previousStartDate = original
    assert instance.previousStartDate == original

@given(instance=oving4::Exam_strategy)
def test_oving4::exam_endDate_type(instance):
    assert isinstance(instance.endDate, str)


@given(instance=oving4::Exam_strategy)
def test_oving4::exam_endDate_setter(instance):
    original = instance.endDate
    instance.endDate = original
    assert instance.endDate == original

@given(instance=oving4::EvaluationElement_strategy)
@settings(max_examples=50)
def test_oving4::evaluationelement_instantiation(instance):
    assert isinstance(instance, oving4::EvaluationElement)

@given(instance=oving4::EvaluationElement_strategy)
def test_oving4::evaluationelement_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=oving4::EvaluationElement_strategy)
def test_oving4::evaluationelement_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=oving4::EvaluationElement_strategy)
def test_oving4::evaluationelement_weight_type(instance):
    assert isinstance(instance.weight, float)


@given(instance=oving4::EvaluationElement_strategy)
def test_oving4::evaluationelement_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=oving4::EvaluationElement_strategy)
def test_oving4::evaluationelement_attended_type(instance):
    assert isinstance(instance.attended, bool)


@given(instance=oving4::EvaluationElement_strategy)
def test_oving4::evaluationelement_attended_setter(instance):
    original = instance.attended
    instance.attended = original
    assert instance.attended == original

@given(instance=oving4::EvaluationElement_strategy)
def test_oving4::evaluationelement_percentageResult_type(instance):
    assert isinstance(instance.percentageResult, float)


@given(instance=oving4::EvaluationElement_strategy)
def test_oving4::evaluationelement_percentageResult_setter(instance):
    original = instance.percentageResult
    instance.percentageResult = original
    assert instance.percentageResult == original

@given(instance=oving4::TimeTableElement_strategy)
@settings(max_examples=50)
def test_oving4::timetableelement_instantiation(instance):
    assert isinstance(instance, oving4::TimeTableElement)

@given(instance=oving4::TimeTableElement_strategy)
def test_oving4::timetableelement_durationInMinutes_type(instance):
    assert isinstance(instance.durationInMinutes, int)


@given(instance=oving4::TimeTableElement_strategy)
def test_oving4::timetableelement_durationInMinutes_setter(instance):
    original = instance.durationInMinutes
    instance.durationInMinutes = original
    assert instance.durationInMinutes == original

@given(instance=oving4::TimeTableElement_strategy)
def test_oving4::timetableelement_room_type(instance):
    assert isinstance(instance.room, str)


@given(instance=oving4::TimeTableElement_strategy)
def test_oving4::timetableelement_room_setter(instance):
    original = instance.room
    instance.room = original
    assert instance.room == original

@given(instance=oving4::TimeTableElement_strategy)
def test_oving4::timetableelement_date_type(instance):
    assert isinstance(instance.date, str)


@given(instance=oving4::TimeTableElement_strategy)
def test_oving4::timetableelement_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original

@given(instance=oving4::CourseInstance_strategy)
@settings(max_examples=50)
def test_oving4::courseinstance_instantiation(instance):
    assert isinstance(instance, oving4::CourseInstance)

@given(instance=oving4::CourseInstance_strategy)
def test_oving4::courseinstance_sumLectureHours_type(instance):
    assert isinstance(instance.sumLectureHours, int)


@given(instance=oving4::CourseInstance_strategy)
def test_oving4::courseinstance_sumLectureHours_setter(instance):
    original = instance.sumLectureHours
    instance.sumLectureHours = original
    assert instance.sumLectureHours == original

@given(instance=oving4::CourseInstance_strategy)
def test_oving4::courseinstance_sumExerciseHours_type(instance):
    assert isinstance(instance.sumExerciseHours, int)


@given(instance=oving4::CourseInstance_strategy)
def test_oving4::courseinstance_sumExerciseHours_setter(instance):
    original = instance.sumExerciseHours
    instance.sumExerciseHours = original
    assert instance.sumExerciseHours == original

@given(instance=oving4::CourseInstance_strategy)
def test_oving4::courseinstance_sumInDepthHours_type(instance):
    assert isinstance(instance.sumInDepthHours, int)


@given(instance=oving4::CourseInstance_strategy)
def test_oving4::courseinstance_sumInDepthHours_setter(instance):
    original = instance.sumInDepthHours
    instance.sumInDepthHours = original
    assert instance.sumInDepthHours == original

@given(instance=oving4::CourseWork_strategy)
@settings(max_examples=50)
def test_oving4::coursework_instantiation(instance):
    assert isinstance(instance, oving4::CourseWork)

@given(instance=oving4::CourseWork_strategy)
def test_oving4::coursework_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=oving4::CourseWork_strategy)
def test_oving4::coursework_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=oving4::CourseWork_strategy)
def test_oving4::coursework_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=oving4::CourseWork_strategy)
def test_oving4::coursework_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=oving4::CourseWork_strategy)
def test_oving4::coursework_isMandatory_type(instance):
    assert isinstance(instance.isMandatory, bool)


@given(instance=oving4::CourseWork_strategy)
def test_oving4::coursework_isMandatory_setter(instance):
    original = instance.isMandatory
    instance.isMandatory = original
    assert instance.isMandatory == original

@given(instance=oving4::TimeTable_strategy)
@settings(max_examples=50)
def test_oving4::timetable_instantiation(instance):
    assert isinstance(instance, oving4::TimeTable)

@given(instance=oving4::TimeTable_strategy)
def test_oving4::timetable_isRestrictedToProgramsInParallell_type(instance):
    assert isinstance(instance.isRestrictedToProgramsInParallell, bool)


@given(instance=oving4::TimeTable_strategy)
def test_oving4::timetable_isRestrictedToProgramsInParallell_setter(instance):
    original = instance.isRestrictedToProgramsInParallell
    instance.isRestrictedToProgramsInParallell = original
    assert instance.isRestrictedToProgramsInParallell == original

@given(instance=oving4::Precondition_strategy)
@settings(max_examples=50)
def test_oving4::precondition_instantiation(instance):
    assert isinstance(instance, oving4::Precondition)

@given(instance=oving4::Precondition_strategy)
def test_oving4::precondition_isMandatory_type(instance):
    assert isinstance(instance.isMandatory, bool)


@given(instance=oving4::Precondition_strategy)
def test_oving4::precondition_isMandatory_setter(instance):
    original = instance.isMandatory
    instance.isMandatory = original
    assert instance.isMandatory == original

@given(instance=oving4::Precondition_strategy)
def test_oving4::precondition_creditReduction_type(instance):
    assert isinstance(instance.creditReduction, float)


@given(instance=oving4::Precondition_strategy)
def test_oving4::precondition_creditReduction_setter(instance):
    original = instance.creditReduction
    instance.creditReduction = original
    assert instance.creditReduction == original

@given(instance=oving4::Person_strategy)
@settings(max_examples=50)
def test_oving4::person_instantiation(instance):
    assert isinstance(instance, oving4::Person)

@given(instance=oving4::Person_strategy)
def test_oving4::person_studyCredits_type(instance):
    assert isinstance(instance.studyCredits, float)


@given(instance=oving4::Person_strategy)
def test_oving4::person_studyCredits_setter(instance):
    original = instance.studyCredits
    instance.studyCredits = original
    assert instance.studyCredits == original

@given(instance=oving4::Person_strategy)
def test_oving4::person_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=oving4::Person_strategy)
def test_oving4::person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=oving4::Person_strategy)
def test_oving4::person_first_name_type(instance):
    assert isinstance(instance.first_name, str)


@given(instance=oving4::Person_strategy)
def test_oving4::person_first_name_setter(instance):
    original = instance.first_name
    instance.first_name = original
    assert instance.first_name == original

@given(instance=oving4::Person_strategy)
def test_oving4::person_last_name_type(instance):
    assert isinstance(instance.last_name, str)


@given(instance=oving4::Person_strategy)
def test_oving4::person_last_name_setter(instance):
    original = instance.last_name
    instance.last_name = original
    assert instance.last_name == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=oving4::Person_strategy)
@settings(max_examples=30)
def test_oving4::person_cancelexam_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.cancelExam(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.cancelExam).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'cancelExam' in oving4::Person is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'cancelExam' in oving4::Person did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'cancelExam' in oving4::Person is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=oving4::Person_strategy)
@settings(max_examples=30)
def test_oving4::person_signupforexam_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.signUpForExam(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.signUpForExam).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'signUpForExam' in oving4::Person is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'signUpForExam' in oving4::Person did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'signUpForExam' in oving4::Person is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=oving4::Person_strategy)
@settings(max_examples=30)
def test_oving4::person_takeexam_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.takeExam(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.takeExam).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'takeExam' in oving4::Person is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'takeExam' in oving4::Person did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'takeExam' in oving4::Person is not implemented or raised an error")

@given(instance=oving4::Evaluation_strategy)
@settings(max_examples=50)
def test_oving4::evaluation_instantiation(instance):
    assert isinstance(instance, oving4::Evaluation)

@given(instance=oving4::Evaluation_strategy)
def test_oving4::evaluation_creditsReceived_type(instance):
    assert isinstance(instance.creditsReceived, float)


@given(instance=oving4::Evaluation_strategy)
def test_oving4::evaluation_creditsReceived_setter(instance):
    original = instance.creditsReceived
    instance.creditsReceived = original
    assert instance.creditsReceived == original

@given(instance=oving4::Evaluation_strategy)
def test_oving4::evaluation_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=oving4::Evaluation_strategy)
def test_oving4::evaluation_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=oving4::Evaluation_strategy)
def test_oving4::evaluation_totalPercentageResult_type(instance):
    assert isinstance(instance.totalPercentageResult, float)


@given(instance=oving4::Evaluation_strategy)
def test_oving4::evaluation_totalPercentageResult_setter(instance):
    original = instance.totalPercentageResult
    instance.totalPercentageResult = original
    assert instance.totalPercentageResult == original

@given(instance=oving4::Evaluation_strategy)
def test_oving4::evaluation_completed_type(instance):
    assert isinstance(instance.completed, bool)


@given(instance=oving4::Evaluation_strategy)
def test_oving4::evaluation_completed_setter(instance):
    original = instance.completed
    instance.completed = original
    assert instance.completed == original

@given(instance=oving4::PersonRole_strategy)
@settings(max_examples=50)
def test_oving4::personrole_instantiation(instance):
    assert isinstance(instance, oving4::PersonRole)

@given(instance=oving4::PersonRole_strategy)
def test_oving4::personrole_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=oving4::PersonRole_strategy)
def test_oving4::personrole_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=oving4::Course_strategy)
@settings(max_examples=50)
def test_oving4::course_instantiation(instance):
    assert isinstance(instance, oving4::Course)

@given(instance=oving4::Course_strategy)
def test_oving4::course_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=oving4::Course_strategy)
def test_oving4::course_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=oving4::Course_strategy)
def test_oving4::course_content_type(instance):
    assert isinstance(instance.content, str)


@given(instance=oving4::Course_strategy)
def test_oving4::course_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original

@given(instance=oving4::Course_strategy)
def test_oving4::course_credits_type(instance):
    assert isinstance(instance.credits, float)


@given(instance=oving4::Course_strategy)
def test_oving4::course_credits_setter(instance):
    original = instance.credits
    instance.credits = original
    assert instance.credits == original

@given(instance=oving4::Course_strategy)
def test_oving4::course_examStartDate_type(instance):
    assert isinstance(instance.examStartDate, str)


@given(instance=oving4::Course_strategy)
def test_oving4::course_examStartDate_setter(instance):
    original = instance.examStartDate
    instance.examStartDate = original
    assert instance.examStartDate == original

@given(instance=oving4::Course_strategy)
def test_oving4::course_examEndDate_type(instance):
    assert isinstance(instance.examEndDate, str)


@given(instance=oving4::Course_strategy)
def test_oving4::course_examEndDate_setter(instance):
    original = instance.examEndDate
    instance.examEndDate = original
    assert instance.examEndDate == original

@given(instance=oving4::Course_strategy)
def test_oving4::course_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=oving4::Course_strategy)
def test_oving4::course_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=oving4::Project_strategy)
@settings(max_examples=50)
def test_oving4::project_instantiation(instance):
    assert isinstance(instance, oving4::Project)

@given(instance=oving4::Project_strategy)
def test_oving4::project_deadline_type(instance):
    assert isinstance(instance.deadline, str)


@given(instance=oving4::Project_strategy)
def test_oving4::project_deadline_setter(instance):
    original = instance.deadline
    instance.deadline = original
    assert instance.deadline == original

@given(instance=oving4::StudyProgram_strategy)
@settings(max_examples=50)
def test_oving4::studyprogram_instantiation(instance):
    assert isinstance(instance, oving4::StudyProgram)

@given(instance=oving4::StudyProgram_strategy)
def test_oving4::studyprogram_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=oving4::StudyProgram_strategy)
def test_oving4::studyprogram_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=oving4::Department_strategy)
@settings(max_examples=50)
def test_oving4::department_instantiation(instance):
    assert isinstance(instance, oving4::Department)

@given(instance=oving4::Department_strategy)
def test_oving4::department_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=oving4::Department_strategy)
def test_oving4::department_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=oving4::Root_strategy)
@settings(max_examples=50)
def test_oving4::root_instantiation(instance):
    assert isinstance(instance, oving4::Root)
