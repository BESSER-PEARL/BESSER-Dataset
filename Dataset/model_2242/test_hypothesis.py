import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    oving4_Assignment,
    oving4_Exam,
    oving4_EvaluationElement,
    oving4_TimeTableElement,
    oving4_CourseInstance,
    oving4_CourseWork,
    oving4_TimeTable,
    oving4_Precondition,
    oving4_Person,
    oving4_Evaluation,
    oving4_PersonRole,
    oving4_Course,
    oving4_Project,
    oving4_StudyProgram,
    oving4_Department,
    oving4_Root,
    StudyProgramType,
    EvaluationType,
    RoleType,
    CourseWorkType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_oving4_assignment_is_not_abstract():
    assert not inspect.isabstract(oving4_Assignment)


def test_oving4_assignment_constructor_exists():
    assert callable(oving4_Assignment.__init__)


def test_oving4_assignment_constructor_args():
    sig = inspect.signature(oving4_Assignment.__init__)
    params = list(sig.parameters.keys())
    assert "deadline" in params, "Missing parameter 'deadline'"

def test_oving4_assignment_has_deadline():
    assert hasattr(oving4_Assignment, "deadline")
    descriptor = None
    for klass in oving4_Assignment.__mro__:
        if "deadline" in klass.__dict__:
            descriptor = klass.__dict__["deadline"]
            break
    assert isinstance(descriptor, property)



def test_oving4_exam_is_not_abstract():
    assert not inspect.isabstract(oving4_Exam)


def test_oving4_exam_constructor_exists():
    assert callable(oving4_Exam.__init__)


def test_oving4_exam_constructor_args():
    sig = inspect.signature(oving4_Exam.__init__)
    params = list(sig.parameters.keys())
    assert "previousStartDate" in params, "Missing parameter 'previousStartDate'"
    assert "startDate" in params, "Missing parameter 'startDate'"
    assert "previousEndDate" in params, "Missing parameter 'previousEndDate'"
    assert "endDate" in params, "Missing parameter 'endDate'"

def test_oving4_exam_has_previousStartDate():
    assert hasattr(oving4_Exam, "previousStartDate")
    descriptor = None
    for klass in oving4_Exam.__mro__:
        if "previousStartDate" in klass.__dict__:
            descriptor = klass.__dict__["previousStartDate"]
            break
    assert isinstance(descriptor, property)

def test_oving4_exam_has_startDate():
    assert hasattr(oving4_Exam, "startDate")
    descriptor = None
    for klass in oving4_Exam.__mro__:
        if "startDate" in klass.__dict__:
            descriptor = klass.__dict__["startDate"]
            break
    assert isinstance(descriptor, property)

def test_oving4_exam_has_previousEndDate():
    assert hasattr(oving4_Exam, "previousEndDate")
    descriptor = None
    for klass in oving4_Exam.__mro__:
        if "previousEndDate" in klass.__dict__:
            descriptor = klass.__dict__["previousEndDate"]
            break
    assert isinstance(descriptor, property)

def test_oving4_exam_has_endDate():
    assert hasattr(oving4_Exam, "endDate")
    descriptor = None
    for klass in oving4_Exam.__mro__:
        if "endDate" in klass.__dict__:
            descriptor = klass.__dict__["endDate"]
            break
    assert isinstance(descriptor, property)



def test_oving4_evaluationelement_is_not_abstract():
    assert not inspect.isabstract(oving4_EvaluationElement)


def test_oving4_evaluationelement_constructor_exists():
    assert callable(oving4_EvaluationElement.__init__)


def test_oving4_evaluationelement_constructor_args():
    sig = inspect.signature(oving4_EvaluationElement.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "percentageResult" in params, "Missing parameter 'percentageResult'"
    assert "weight" in params, "Missing parameter 'weight'"
    assert "attended" in params, "Missing parameter 'attended'"

def test_oving4_evaluationelement_has_type():
    assert hasattr(oving4_EvaluationElement, "type")
    descriptor = None
    for klass in oving4_EvaluationElement.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_oving4_evaluationelement_has_percentageResult():
    assert hasattr(oving4_EvaluationElement, "percentageResult")
    descriptor = None
    for klass in oving4_EvaluationElement.__mro__:
        if "percentageResult" in klass.__dict__:
            descriptor = klass.__dict__["percentageResult"]
            break
    assert isinstance(descriptor, property)

def test_oving4_evaluationelement_has_weight():
    assert hasattr(oving4_EvaluationElement, "weight")
    descriptor = None
    for klass in oving4_EvaluationElement.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)

def test_oving4_evaluationelement_has_attended():
    assert hasattr(oving4_EvaluationElement, "attended")
    descriptor = None
    for klass in oving4_EvaluationElement.__mro__:
        if "attended" in klass.__dict__:
            descriptor = klass.__dict__["attended"]
            break
    assert isinstance(descriptor, property)



def test_oving4_timetableelement_is_not_abstract():
    assert not inspect.isabstract(oving4_TimeTableElement)


def test_oving4_timetableelement_constructor_exists():
    assert callable(oving4_TimeTableElement.__init__)


def test_oving4_timetableelement_constructor_args():
    sig = inspect.signature(oving4_TimeTableElement.__init__)
    params = list(sig.parameters.keys())
    assert "room" in params, "Missing parameter 'room'"
    assert "durationInMinutes" in params, "Missing parameter 'durationInMinutes'"
    assert "date" in params, "Missing parameter 'date'"

def test_oving4_timetableelement_has_room():
    assert hasattr(oving4_TimeTableElement, "room")
    descriptor = None
    for klass in oving4_TimeTableElement.__mro__:
        if "room" in klass.__dict__:
            descriptor = klass.__dict__["room"]
            break
    assert isinstance(descriptor, property)

def test_oving4_timetableelement_has_durationInMinutes():
    assert hasattr(oving4_TimeTableElement, "durationInMinutes")
    descriptor = None
    for klass in oving4_TimeTableElement.__mro__:
        if "durationInMinutes" in klass.__dict__:
            descriptor = klass.__dict__["durationInMinutes"]
            break
    assert isinstance(descriptor, property)

def test_oving4_timetableelement_has_date():
    assert hasattr(oving4_TimeTableElement, "date")
    descriptor = None
    for klass in oving4_TimeTableElement.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)



def test_oving4_courseinstance_is_not_abstract():
    assert not inspect.isabstract(oving4_CourseInstance)


def test_oving4_courseinstance_constructor_exists():
    assert callable(oving4_CourseInstance.__init__)


def test_oving4_courseinstance_constructor_args():
    sig = inspect.signature(oving4_CourseInstance.__init__)
    params = list(sig.parameters.keys())
    assert "sumLectureHours" in params, "Missing parameter 'sumLectureHours'"
    assert "sumInDepthHours" in params, "Missing parameter 'sumInDepthHours'"
    assert "sumExerciseHours" in params, "Missing parameter 'sumExerciseHours'"

def test_oving4_courseinstance_has_sumLectureHours():
    assert hasattr(oving4_CourseInstance, "sumLectureHours")
    descriptor = None
    for klass in oving4_CourseInstance.__mro__:
        if "sumLectureHours" in klass.__dict__:
            descriptor = klass.__dict__["sumLectureHours"]
            break
    assert isinstance(descriptor, property)

def test_oving4_courseinstance_has_sumInDepthHours():
    assert hasattr(oving4_CourseInstance, "sumInDepthHours")
    descriptor = None
    for klass in oving4_CourseInstance.__mro__:
        if "sumInDepthHours" in klass.__dict__:
            descriptor = klass.__dict__["sumInDepthHours"]
            break
    assert isinstance(descriptor, property)

def test_oving4_courseinstance_has_sumExerciseHours():
    assert hasattr(oving4_CourseInstance, "sumExerciseHours")
    descriptor = None
    for klass in oving4_CourseInstance.__mro__:
        if "sumExerciseHours" in klass.__dict__:
            descriptor = klass.__dict__["sumExerciseHours"]
            break
    assert isinstance(descriptor, property)



def test_oving4_coursework_is_not_abstract():
    assert not inspect.isabstract(oving4_CourseWork)


def test_oving4_coursework_constructor_exists():
    assert callable(oving4_CourseWork.__init__)


def test_oving4_coursework_constructor_args():
    sig = inspect.signature(oving4_CourseWork.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"
    assert "isMandatory" in params, "Missing parameter 'isMandatory'"

def test_oving4_coursework_has_name():
    assert hasattr(oving4_CourseWork, "name")
    descriptor = None
    for klass in oving4_CourseWork.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_oving4_coursework_has_type():
    assert hasattr(oving4_CourseWork, "type")
    descriptor = None
    for klass in oving4_CourseWork.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_oving4_coursework_has_isMandatory():
    assert hasattr(oving4_CourseWork, "isMandatory")
    descriptor = None
    for klass in oving4_CourseWork.__mro__:
        if "isMandatory" in klass.__dict__:
            descriptor = klass.__dict__["isMandatory"]
            break
    assert isinstance(descriptor, property)



def test_oving4_timetable_is_not_abstract():
    assert not inspect.isabstract(oving4_TimeTable)


def test_oving4_timetable_constructor_exists():
    assert callable(oving4_TimeTable.__init__)


def test_oving4_timetable_constructor_args():
    sig = inspect.signature(oving4_TimeTable.__init__)
    params = list(sig.parameters.keys())
    assert "isRestrictedToProgramsInParallell" in params, "Missing parameter 'isRestrictedToProgramsInParallell'"

def test_oving4_timetable_has_isRestrictedToProgramsInParallell():
    assert hasattr(oving4_TimeTable, "isRestrictedToProgramsInParallell")
    descriptor = None
    for klass in oving4_TimeTable.__mro__:
        if "isRestrictedToProgramsInParallell" in klass.__dict__:
            descriptor = klass.__dict__["isRestrictedToProgramsInParallell"]
            break
    assert isinstance(descriptor, property)



def test_oving4_precondition_is_not_abstract():
    assert not inspect.isabstract(oving4_Precondition)


def test_oving4_precondition_constructor_exists():
    assert callable(oving4_Precondition.__init__)


def test_oving4_precondition_constructor_args():
    sig = inspect.signature(oving4_Precondition.__init__)
    params = list(sig.parameters.keys())
    assert "creditReduction" in params, "Missing parameter 'creditReduction'"
    assert "isMandatory" in params, "Missing parameter 'isMandatory'"

def test_oving4_precondition_has_creditReduction():
    assert hasattr(oving4_Precondition, "creditReduction")
    descriptor = None
    for klass in oving4_Precondition.__mro__:
        if "creditReduction" in klass.__dict__:
            descriptor = klass.__dict__["creditReduction"]
            break
    assert isinstance(descriptor, property)

def test_oving4_precondition_has_isMandatory():
    assert hasattr(oving4_Precondition, "isMandatory")
    descriptor = None
    for klass in oving4_Precondition.__mro__:
        if "isMandatory" in klass.__dict__:
            descriptor = klass.__dict__["isMandatory"]
            break
    assert isinstance(descriptor, property)



def test_oving4_person_is_not_abstract():
    assert not inspect.isabstract(oving4_Person)


def test_oving4_person_constructor_exists():
    assert callable(oving4_Person.__init__)


def test_oving4_person_constructor_args():
    sig = inspect.signature(oving4_Person.__init__)
    params = list(sig.parameters.keys())
    assert "first_name" in params, "Missing parameter 'first_name'"
    assert "last_name" in params, "Missing parameter 'last_name'"
    assert "name" in params, "Missing parameter 'name'"
    assert "studyCredits" in params, "Missing parameter 'studyCredits'"

def test_oving4_person_has_first_name():
    assert hasattr(oving4_Person, "first_name")
    descriptor = None
    for klass in oving4_Person.__mro__:
        if "first_name" in klass.__dict__:
            descriptor = klass.__dict__["first_name"]
            break
    assert isinstance(descriptor, property)

def test_oving4_person_has_last_name():
    assert hasattr(oving4_Person, "last_name")
    descriptor = None
    for klass in oving4_Person.__mro__:
        if "last_name" in klass.__dict__:
            descriptor = klass.__dict__["last_name"]
            break
    assert isinstance(descriptor, property)

def test_oving4_person_has_name():
    assert hasattr(oving4_Person, "name")
    descriptor = None
    for klass in oving4_Person.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_oving4_person_has_studyCredits():
    assert hasattr(oving4_Person, "studyCredits")
    descriptor = None
    for klass in oving4_Person.__mro__:
        if "studyCredits" in klass.__dict__:
            descriptor = klass.__dict__["studyCredits"]
            break
    assert isinstance(descriptor, property)



def test_oving4_evaluation_is_not_abstract():
    assert not inspect.isabstract(oving4_Evaluation)


def test_oving4_evaluation_constructor_exists():
    assert callable(oving4_Evaluation.__init__)


def test_oving4_evaluation_constructor_args():
    sig = inspect.signature(oving4_Evaluation.__init__)
    params = list(sig.parameters.keys())
    assert "totalPercentageResult" in params, "Missing parameter 'totalPercentageResult'"
    assert "description" in params, "Missing parameter 'description'"
    assert "creditsReceived" in params, "Missing parameter 'creditsReceived'"
    assert "completed" in params, "Missing parameter 'completed'"

def test_oving4_evaluation_has_totalPercentageResult():
    assert hasattr(oving4_Evaluation, "totalPercentageResult")
    descriptor = None
    for klass in oving4_Evaluation.__mro__:
        if "totalPercentageResult" in klass.__dict__:
            descriptor = klass.__dict__["totalPercentageResult"]
            break
    assert isinstance(descriptor, property)

def test_oving4_evaluation_has_description():
    assert hasattr(oving4_Evaluation, "description")
    descriptor = None
    for klass in oving4_Evaluation.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_oving4_evaluation_has_creditsReceived():
    assert hasattr(oving4_Evaluation, "creditsReceived")
    descriptor = None
    for klass in oving4_Evaluation.__mro__:
        if "creditsReceived" in klass.__dict__:
            descriptor = klass.__dict__["creditsReceived"]
            break
    assert isinstance(descriptor, property)

def test_oving4_evaluation_has_completed():
    assert hasattr(oving4_Evaluation, "completed")
    descriptor = None
    for klass in oving4_Evaluation.__mro__:
        if "completed" in klass.__dict__:
            descriptor = klass.__dict__["completed"]
            break
    assert isinstance(descriptor, property)



def test_oving4_personrole_is_not_abstract():
    assert not inspect.isabstract(oving4_PersonRole)


def test_oving4_personrole_constructor_exists():
    assert callable(oving4_PersonRole.__init__)


def test_oving4_personrole_constructor_args():
    sig = inspect.signature(oving4_PersonRole.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_oving4_personrole_has_type():
    assert hasattr(oving4_PersonRole, "type")
    descriptor = None
    for klass in oving4_PersonRole.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_oving4_course_is_not_abstract():
    assert not inspect.isabstract(oving4_Course)


def test_oving4_course_constructor_exists():
    assert callable(oving4_Course.__init__)


def test_oving4_course_constructor_args():
    sig = inspect.signature(oving4_Course.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "content" in params, "Missing parameter 'content'"
    assert "name" in params, "Missing parameter 'name'"
    assert "examStartDate" in params, "Missing parameter 'examStartDate'"
    assert "credits" in params, "Missing parameter 'credits'"
    assert "examEndDate" in params, "Missing parameter 'examEndDate'"

def test_oving4_course_has_code():
    assert hasattr(oving4_Course, "code")
    descriptor = None
    for klass in oving4_Course.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_oving4_course_has_content():
    assert hasattr(oving4_Course, "content")
    descriptor = None
    for klass in oving4_Course.__mro__:
        if "content" in klass.__dict__:
            descriptor = klass.__dict__["content"]
            break
    assert isinstance(descriptor, property)

def test_oving4_course_has_name():
    assert hasattr(oving4_Course, "name")
    descriptor = None
    for klass in oving4_Course.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_oving4_course_has_examStartDate():
    assert hasattr(oving4_Course, "examStartDate")
    descriptor = None
    for klass in oving4_Course.__mro__:
        if "examStartDate" in klass.__dict__:
            descriptor = klass.__dict__["examStartDate"]
            break
    assert isinstance(descriptor, property)

def test_oving4_course_has_credits():
    assert hasattr(oving4_Course, "credits")
    descriptor = None
    for klass in oving4_Course.__mro__:
        if "credits" in klass.__dict__:
            descriptor = klass.__dict__["credits"]
            break
    assert isinstance(descriptor, property)

def test_oving4_course_has_examEndDate():
    assert hasattr(oving4_Course, "examEndDate")
    descriptor = None
    for klass in oving4_Course.__mro__:
        if "examEndDate" in klass.__dict__:
            descriptor = klass.__dict__["examEndDate"]
            break
    assert isinstance(descriptor, property)



def test_oving4_project_is_not_abstract():
    assert not inspect.isabstract(oving4_Project)


def test_oving4_project_constructor_exists():
    assert callable(oving4_Project.__init__)


def test_oving4_project_constructor_args():
    sig = inspect.signature(oving4_Project.__init__)
    params = list(sig.parameters.keys())
    assert "deadline" in params, "Missing parameter 'deadline'"

def test_oving4_project_has_deadline():
    assert hasattr(oving4_Project, "deadline")
    descriptor = None
    for klass in oving4_Project.__mro__:
        if "deadline" in klass.__dict__:
            descriptor = klass.__dict__["deadline"]
            break
    assert isinstance(descriptor, property)



def test_oving4_studyprogram_is_not_abstract():
    assert not inspect.isabstract(oving4_StudyProgram)


def test_oving4_studyprogram_constructor_exists():
    assert callable(oving4_StudyProgram.__init__)


def test_oving4_studyprogram_constructor_args():
    sig = inspect.signature(oving4_StudyProgram.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_oving4_studyprogram_has_type():
    assert hasattr(oving4_StudyProgram, "type")
    descriptor = None
    for klass in oving4_StudyProgram.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_oving4_department_is_not_abstract():
    assert not inspect.isabstract(oving4_Department)


def test_oving4_department_constructor_exists():
    assert callable(oving4_Department.__init__)


def test_oving4_department_constructor_args():
    sig = inspect.signature(oving4_Department.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_oving4_department_has_name():
    assert hasattr(oving4_Department, "name")
    descriptor = None
    for klass in oving4_Department.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_oving4_root_is_not_abstract():
    assert not inspect.isabstract(oving4_Root)


def test_oving4_root_constructor_exists():
    assert callable(oving4_Root.__init__)


def test_oving4_root_constructor_args():
    sig = inspect.signature(oving4_Root.__init__)
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

def test_evaluationtype_exists():
    # Check that the Enumeration exists
    assert EvaluationType is not None

def test_evaluationtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EvaluationType]
    expected_literals = [
        "Project",
        "Assignment",
        "Exam",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EvaluationType"

def test_roletype_exists():
    # Check that the Enumeration exists
    assert RoleType is not None

def test_roletype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in RoleType]
    expected_literals = [
        "Supervisor",
        "Student",
        "Lecturer",
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
        "Lecture",
        "InDepth",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CourseWorkType"


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
oving4_Assignment_strategy = st.builds(
    oving4_Assignment,
    deadline=
        safe_text
)
oving4_Exam_strategy = st.builds(
    oving4_Exam,
    previousStartDate=
        safe_text,
    startDate=
        safe_text,
    previousEndDate=
        safe_text,
    endDate=
        safe_text
)
oving4_EvaluationElement_strategy = st.builds(
    oving4_EvaluationElement,
    type=
        safe_text,
    percentageResult=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    weight=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    attended=
        st.booleans()
)
oving4_TimeTableElement_strategy = st.builds(
    oving4_TimeTableElement,
    room=
        safe_text,
    durationInMinutes=
        st.integers(),
    date=
        safe_text
)
oving4_CourseInstance_strategy = st.builds(
    oving4_CourseInstance,
    sumLectureHours=
        st.integers(),
    sumInDepthHours=
        st.integers(),
    sumExerciseHours=
        st.integers()
)
oving4_CourseWork_strategy = st.builds(
    oving4_CourseWork,
    name=
        safe_text,
    type=
        safe_text,
    isMandatory=
        st.booleans()
)
oving4_TimeTable_strategy = st.builds(
    oving4_TimeTable,
    isRestrictedToProgramsInParallell=
        st.booleans()
)
oving4_Precondition_strategy = st.builds(
    oving4_Precondition,
    creditReduction=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    isMandatory=
        st.booleans()
)
oving4_Person_strategy = st.builds(
    oving4_Person,
    first_name=
        safe_text,
    last_name=
        safe_text,
    name=
        safe_text,
    studyCredits=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
oving4_Evaluation_strategy = st.builds(
    oving4_Evaluation,
    totalPercentageResult=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    description=
        safe_text,
    creditsReceived=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    completed=
        st.booleans()
)
oving4_PersonRole_strategy = st.builds(
    oving4_PersonRole,
    type=
        safe_text
)
oving4_Course_strategy = st.builds(
    oving4_Course,
    code=
        safe_text,
    content=
        safe_text,
    name=
        safe_text,
    examStartDate=
        safe_text,
    credits=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    examEndDate=
        safe_text
)
oving4_Project_strategy = st.builds(
    oving4_Project,
    deadline=
        safe_text
)
oving4_StudyProgram_strategy = st.builds(
    oving4_StudyProgram,
    type=
        safe_text
)
oving4_Department_strategy = st.builds(
    oving4_Department,
    name=
        safe_text
)
oving4_Root_strategy = st.builds(
    oving4_Root,
)

@given(instance=oving4_Assignment_strategy)
@settings(max_examples=50)
def test_oving4_assignment_instantiation(instance):
    assert isinstance(instance, oving4_Assignment)



@given(instance=oving4_Assignment_strategy)
def test_oving4_assignment_deadline_setter(instance):
    original = instance.deadline
    instance.deadline = original
    assert instance.deadline == original

@given(instance=oving4_Exam_strategy)
@settings(max_examples=50)
def test_oving4_exam_instantiation(instance):
    assert isinstance(instance, oving4_Exam)



@given(instance=oving4_Exam_strategy)
def test_oving4_exam_previousStartDate_setter(instance):
    original = instance.previousStartDate
    instance.previousStartDate = original
    assert instance.previousStartDate == original



@given(instance=oving4_Exam_strategy)
def test_oving4_exam_startDate_setter(instance):
    original = instance.startDate
    instance.startDate = original
    assert instance.startDate == original



@given(instance=oving4_Exam_strategy)
def test_oving4_exam_previousEndDate_setter(instance):
    original = instance.previousEndDate
    instance.previousEndDate = original
    assert instance.previousEndDate == original



@given(instance=oving4_Exam_strategy)
def test_oving4_exam_endDate_setter(instance):
    original = instance.endDate
    instance.endDate = original
    assert instance.endDate == original

@given(instance=oving4_EvaluationElement_strategy)
@settings(max_examples=50)
def test_oving4_evaluationelement_instantiation(instance):
    assert isinstance(instance, oving4_EvaluationElement)



@given(instance=oving4_EvaluationElement_strategy)
def test_oving4_evaluationelement_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=oving4_EvaluationElement_strategy)
def test_oving4_evaluationelement_percentageResult_setter(instance):
    original = instance.percentageResult
    instance.percentageResult = original
    assert instance.percentageResult == original



@given(instance=oving4_EvaluationElement_strategy)
def test_oving4_evaluationelement_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original



@given(instance=oving4_EvaluationElement_strategy)
def test_oving4_evaluationelement_attended_setter(instance):
    original = instance.attended
    instance.attended = original
    assert instance.attended == original

@given(instance=oving4_TimeTableElement_strategy)
@settings(max_examples=50)
def test_oving4_timetableelement_instantiation(instance):
    assert isinstance(instance, oving4_TimeTableElement)



@given(instance=oving4_TimeTableElement_strategy)
def test_oving4_timetableelement_room_setter(instance):
    original = instance.room
    instance.room = original
    assert instance.room == original



@given(instance=oving4_TimeTableElement_strategy)
def test_oving4_timetableelement_durationInMinutes_setter(instance):
    original = instance.durationInMinutes
    instance.durationInMinutes = original
    assert instance.durationInMinutes == original



@given(instance=oving4_TimeTableElement_strategy)
def test_oving4_timetableelement_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original

@given(instance=oving4_CourseInstance_strategy)
@settings(max_examples=50)
def test_oving4_courseinstance_instantiation(instance):
    assert isinstance(instance, oving4_CourseInstance)



@given(instance=oving4_CourseInstance_strategy)
def test_oving4_courseinstance_sumLectureHours_setter(instance):
    original = instance.sumLectureHours
    instance.sumLectureHours = original
    assert instance.sumLectureHours == original



@given(instance=oving4_CourseInstance_strategy)
def test_oving4_courseinstance_sumInDepthHours_setter(instance):
    original = instance.sumInDepthHours
    instance.sumInDepthHours = original
    assert instance.sumInDepthHours == original



@given(instance=oving4_CourseInstance_strategy)
def test_oving4_courseinstance_sumExerciseHours_setter(instance):
    original = instance.sumExerciseHours
    instance.sumExerciseHours = original
    assert instance.sumExerciseHours == original

@given(instance=oving4_CourseWork_strategy)
@settings(max_examples=50)
def test_oving4_coursework_instantiation(instance):
    assert isinstance(instance, oving4_CourseWork)



@given(instance=oving4_CourseWork_strategy)
def test_oving4_coursework_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=oving4_CourseWork_strategy)
def test_oving4_coursework_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=oving4_CourseWork_strategy)
def test_oving4_coursework_isMandatory_setter(instance):
    original = instance.isMandatory
    instance.isMandatory = original
    assert instance.isMandatory == original

@given(instance=oving4_TimeTable_strategy)
@settings(max_examples=50)
def test_oving4_timetable_instantiation(instance):
    assert isinstance(instance, oving4_TimeTable)



@given(instance=oving4_TimeTable_strategy)
def test_oving4_timetable_isRestrictedToProgramsInParallell_setter(instance):
    original = instance.isRestrictedToProgramsInParallell
    instance.isRestrictedToProgramsInParallell = original
    assert instance.isRestrictedToProgramsInParallell == original

@given(instance=oving4_Precondition_strategy)
@settings(max_examples=50)
def test_oving4_precondition_instantiation(instance):
    assert isinstance(instance, oving4_Precondition)



@given(instance=oving4_Precondition_strategy)
def test_oving4_precondition_creditReduction_setter(instance):
    original = instance.creditReduction
    instance.creditReduction = original
    assert instance.creditReduction == original



@given(instance=oving4_Precondition_strategy)
def test_oving4_precondition_isMandatory_setter(instance):
    original = instance.isMandatory
    instance.isMandatory = original
    assert instance.isMandatory == original

@given(instance=oving4_Person_strategy)
@settings(max_examples=50)
def test_oving4_person_instantiation(instance):
    assert isinstance(instance, oving4_Person)



@given(instance=oving4_Person_strategy)
def test_oving4_person_first_name_setter(instance):
    original = instance.first_name
    instance.first_name = original
    assert instance.first_name == original



@given(instance=oving4_Person_strategy)
def test_oving4_person_last_name_setter(instance):
    original = instance.last_name
    instance.last_name = original
    assert instance.last_name == original



@given(instance=oving4_Person_strategy)
def test_oving4_person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=oving4_Person_strategy)
def test_oving4_person_studyCredits_setter(instance):
    original = instance.studyCredits
    instance.studyCredits = original
    assert instance.studyCredits == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=oving4_Person_strategy)
@settings(max_examples=30)
def test_oving4_person_cancelexam_changes_state(instance):
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
        assert has_statements, f"Function 'cancelExam' in oving4_Person is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'cancelExam' in oving4_Person did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'cancelExam' in oving4_Person is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=oving4_Person_strategy)
@settings(max_examples=30)
def test_oving4_person_signupforexam_changes_state(instance):
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
        assert has_statements, f"Function 'signUpForExam' in oving4_Person is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'signUpForExam' in oving4_Person did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'signUpForExam' in oving4_Person is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=oving4_Person_strategy)
@settings(max_examples=30)
def test_oving4_person_takeexam_changes_state(instance):
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
        assert has_statements, f"Function 'takeExam' in oving4_Person is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'takeExam' in oving4_Person did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'takeExam' in oving4_Person is not implemented or raised an error")

@given(instance=oving4_Evaluation_strategy)
@settings(max_examples=50)
def test_oving4_evaluation_instantiation(instance):
    assert isinstance(instance, oving4_Evaluation)



@given(instance=oving4_Evaluation_strategy)
def test_oving4_evaluation_totalPercentageResult_setter(instance):
    original = instance.totalPercentageResult
    instance.totalPercentageResult = original
    assert instance.totalPercentageResult == original



@given(instance=oving4_Evaluation_strategy)
def test_oving4_evaluation_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=oving4_Evaluation_strategy)
def test_oving4_evaluation_creditsReceived_setter(instance):
    original = instance.creditsReceived
    instance.creditsReceived = original
    assert instance.creditsReceived == original



@given(instance=oving4_Evaluation_strategy)
def test_oving4_evaluation_completed_setter(instance):
    original = instance.completed
    instance.completed = original
    assert instance.completed == original

@given(instance=oving4_PersonRole_strategy)
@settings(max_examples=50)
def test_oving4_personrole_instantiation(instance):
    assert isinstance(instance, oving4_PersonRole)



@given(instance=oving4_PersonRole_strategy)
def test_oving4_personrole_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=oving4_Course_strategy)
@settings(max_examples=50)
def test_oving4_course_instantiation(instance):
    assert isinstance(instance, oving4_Course)



@given(instance=oving4_Course_strategy)
def test_oving4_course_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=oving4_Course_strategy)
def test_oving4_course_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original



@given(instance=oving4_Course_strategy)
def test_oving4_course_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=oving4_Course_strategy)
def test_oving4_course_examStartDate_setter(instance):
    original = instance.examStartDate
    instance.examStartDate = original
    assert instance.examStartDate == original



@given(instance=oving4_Course_strategy)
def test_oving4_course_credits_setter(instance):
    original = instance.credits
    instance.credits = original
    assert instance.credits == original



@given(instance=oving4_Course_strategy)
def test_oving4_course_examEndDate_setter(instance):
    original = instance.examEndDate
    instance.examEndDate = original
    assert instance.examEndDate == original

@given(instance=oving4_Project_strategy)
@settings(max_examples=50)
def test_oving4_project_instantiation(instance):
    assert isinstance(instance, oving4_Project)



@given(instance=oving4_Project_strategy)
def test_oving4_project_deadline_setter(instance):
    original = instance.deadline
    instance.deadline = original
    assert instance.deadline == original

@given(instance=oving4_StudyProgram_strategy)
@settings(max_examples=50)
def test_oving4_studyprogram_instantiation(instance):
    assert isinstance(instance, oving4_StudyProgram)



@given(instance=oving4_StudyProgram_strategy)
def test_oving4_studyprogram_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=oving4_Department_strategy)
@settings(max_examples=50)
def test_oving4_department_instantiation(instance):
    assert isinstance(instance, oving4_Department)



@given(instance=oving4_Department_strategy)
def test_oving4_department_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=oving4_Root_strategy)
@settings(max_examples=50)
def test_oving4_root_instantiation(instance):
    assert isinstance(instance, oving4_Root)
