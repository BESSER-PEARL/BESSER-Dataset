import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    research16::Phase,
    Named,
    research16::PublicationProcess,
    research16::Action,
    StateMachineObject,
    research16::Transition,
    research16::StateMachineObject,
    research16::StateMachineVariable,
    research16::Keyword,
    research16::Labelled,
    research16::Counted,
    research16::Named,
    research16::PublicationStatus,
    research16::PublicationSystem,
    research16::KnowledgeManager,
    research16::PublicationStructure,
    Labelled,
    research16::ReviewNote,
    Counted,
    research16::State,
    research16::PaperKeyword,
    research16::Progress,
    research16::Paragraph,
    research16::Collaboration,
    research16::Position,
    research16::Skill,
    research16::Paper,
    research16::Review,
    research16::Write,
    research16::Researcher,
    StateType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_research16::phase_is_not_abstract():
    assert not inspect.isabstract(research16::Phase)


def test_research16::phase_constructor_exists():
    assert callable(research16::Phase.__init__)


def test_research16::phase_constructor_args():
    sig = inspect.signature(research16::Phase.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_research16::phase_has_name():
    assert hasattr(research16::Phase, "name")
    descriptor = None
    for klass in research16::Phase.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_named_is_not_abstract():
    assert not inspect.isabstract(Named)


def test_named_constructor_exists():
    assert callable(Named.__init__)


def test_named_constructor_args():
    sig = inspect.signature(Named.__init__)
    params = list(sig.parameters.keys())



def test_research16::publicationprocess_is_not_abstract():
    assert not inspect.isabstract(research16::PublicationProcess)


def test_research16::publicationprocess_constructor_exists():
    assert callable(research16::PublicationProcess.__init__)


def test_research16::publicationprocess_constructor_args():
    sig = inspect.signature(research16::PublicationProcess.__init__)
    params = list(sig.parameters.keys())
    assert "minTime" in params, "Missing parameter 'minTime'"
    assert "maxTime" in params, "Missing parameter 'maxTime'"

def test_research16::publicationprocess_has_minTime():
    assert hasattr(research16::PublicationProcess, "minTime")
    descriptor = None
    for klass in research16::PublicationProcess.__mro__:
        if "minTime" in klass.__dict__:
            descriptor = klass.__dict__["minTime"]
            break
    assert isinstance(descriptor, property)

def test_research16::publicationprocess_has_maxTime():
    assert hasattr(research16::PublicationProcess, "maxTime")
    descriptor = None
    for klass in research16::PublicationProcess.__mro__:
        if "maxTime" in klass.__dict__:
            descriptor = klass.__dict__["maxTime"]
            break
    assert isinstance(descriptor, property)



def test_research16::action_is_not_abstract():
    assert not inspect.isabstract(research16::Action)


def test_research16::action_constructor_exists():
    assert callable(research16::Action.__init__)


def test_research16::action_constructor_args():
    sig = inspect.signature(research16::Action.__init__)
    params = list(sig.parameters.keys())
    assert "actionStatement" in params, "Missing parameter 'actionStatement'"
    assert "actionLabel" in params, "Missing parameter 'actionLabel'"

def test_research16::action_has_actionStatement():
    assert hasattr(research16::Action, "actionStatement")
    descriptor = None
    for klass in research16::Action.__mro__:
        if "actionStatement" in klass.__dict__:
            descriptor = klass.__dict__["actionStatement"]
            break
    assert isinstance(descriptor, property)

def test_research16::action_has_actionLabel():
    assert hasattr(research16::Action, "actionLabel")
    descriptor = None
    for klass in research16::Action.__mro__:
        if "actionLabel" in klass.__dict__:
            descriptor = klass.__dict__["actionLabel"]
            break
    assert isinstance(descriptor, property)



def test_statemachineobject_is_not_abstract():
    assert not inspect.isabstract(StateMachineObject)


def test_statemachineobject_constructor_exists():
    assert callable(StateMachineObject.__init__)


def test_statemachineobject_constructor_args():
    sig = inspect.signature(StateMachineObject.__init__)
    params = list(sig.parameters.keys())



def test_research16::transition_is_not_abstract():
    assert not inspect.isabstract(research16::Transition)


def test_research16::transition_constructor_exists():
    assert callable(research16::Transition.__init__)


def test_research16::transition_constructor_args():
    sig = inspect.signature(research16::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "guardLabel" in params, "Missing parameter 'guardLabel'"
    assert "guardExpression" in params, "Missing parameter 'guardExpression'"

def test_research16::transition_has_guardLabel():
    assert hasattr(research16::Transition, "guardLabel")
    descriptor = None
    for klass in research16::Transition.__mro__:
        if "guardLabel" in klass.__dict__:
            descriptor = klass.__dict__["guardLabel"]
            break
    assert isinstance(descriptor, property)

def test_research16::transition_has_guardExpression():
    assert hasattr(research16::Transition, "guardExpression")
    descriptor = None
    for klass in research16::Transition.__mro__:
        if "guardExpression" in klass.__dict__:
            descriptor = klass.__dict__["guardExpression"]
            break
    assert isinstance(descriptor, property)



def test_research16::statemachineobject_is_not_abstract():
    assert not inspect.isabstract(research16::StateMachineObject)


def test_research16::statemachineobject_constructor_exists():
    assert callable(research16::StateMachineObject.__init__)


def test_research16::statemachineobject_constructor_args():
    sig = inspect.signature(research16::StateMachineObject.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_research16::statemachineobject_has_label():
    assert hasattr(research16::StateMachineObject, "label")
    descriptor = None
    for klass in research16::StateMachineObject.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_research16::statemachinevariable_is_not_abstract():
    assert not inspect.isabstract(research16::StateMachineVariable)


def test_research16::statemachinevariable_constructor_exists():
    assert callable(research16::StateMachineVariable.__init__)


def test_research16::statemachinevariable_constructor_args():
    sig = inspect.signature(research16::StateMachineVariable.__init__)
    params = list(sig.parameters.keys())



def test_research16::keyword_is_not_abstract():
    assert not inspect.isabstract(research16::Keyword)


def test_research16::keyword_constructor_exists():
    assert callable(research16::Keyword.__init__)


def test_research16::keyword_constructor_args():
    sig = inspect.signature(research16::Keyword.__init__)
    params = list(sig.parameters.keys())
    assert "word" in params, "Missing parameter 'word'"

def test_research16::keyword_has_word():
    assert hasattr(research16::Keyword, "word")
    descriptor = None
    for klass in research16::Keyword.__mro__:
        if "word" in klass.__dict__:
            descriptor = klass.__dict__["word"]
            break
    assert isinstance(descriptor, property)



def test_research16::labelled_is_not_abstract():
    assert not inspect.isabstract(research16::Labelled)


def test_research16::labelled_constructor_exists():
    assert callable(research16::Labelled.__init__)


def test_research16::labelled_constructor_args():
    sig = inspect.signature(research16::Labelled.__init__)
    params = list(sig.parameters.keys())
    assert "lname" in params, "Missing parameter 'lname'"

def test_research16::labelled_has_lname():
    assert hasattr(research16::Labelled, "lname")
    descriptor = None
    for klass in research16::Labelled.__mro__:
        if "lname" in klass.__dict__:
            descriptor = klass.__dict__["lname"]
            break
    assert isinstance(descriptor, property)



def test_research16::counted_is_not_abstract():
    assert not inspect.isabstract(research16::Counted)


def test_research16::counted_constructor_exists():
    assert callable(research16::Counted.__init__)


def test_research16::counted_constructor_args():
    sig = inspect.signature(research16::Counted.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_research16::counted_has_id():
    assert hasattr(research16::Counted, "id")
    descriptor = None
    for klass in research16::Counted.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_research16::named_is_not_abstract():
    assert not inspect.isabstract(research16::Named)


def test_research16::named_constructor_exists():
    assert callable(research16::Named.__init__)


def test_research16::named_constructor_args():
    sig = inspect.signature(research16::Named.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_research16::named_has_name():
    assert hasattr(research16::Named, "name")
    descriptor = None
    for klass in research16::Named.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_research16::publicationstatus_is_not_abstract():
    assert not inspect.isabstract(research16::PublicationStatus)


def test_research16::publicationstatus_constructor_exists():
    assert callable(research16::PublicationStatus.__init__)


def test_research16::publicationstatus_constructor_args():
    sig = inspect.signature(research16::PublicationStatus.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_research16::publicationstatus_has_label():
    assert hasattr(research16::PublicationStatus, "label")
    descriptor = None
    for klass in research16::PublicationStatus.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_research16::publicationsystem_is_not_abstract():
    assert not inspect.isabstract(research16::PublicationSystem)


def test_research16::publicationsystem_constructor_exists():
    assert callable(research16::PublicationSystem.__init__)


def test_research16::publicationsystem_constructor_args():
    sig = inspect.signature(research16::PublicationSystem.__init__)
    params = list(sig.parameters.keys())



def test_research16::knowledgemanager_is_not_abstract():
    assert not inspect.isabstract(research16::KnowledgeManager)


def test_research16::knowledgemanager_constructor_exists():
    assert callable(research16::KnowledgeManager.__init__)


def test_research16::knowledgemanager_constructor_args():
    sig = inspect.signature(research16::KnowledgeManager.__init__)
    params = list(sig.parameters.keys())



def test_research16::publicationstructure_is_not_abstract():
    assert not inspect.isabstract(research16::PublicationStructure)


def test_research16::publicationstructure_constructor_exists():
    assert callable(research16::PublicationStructure.__init__)


def test_research16::publicationstructure_constructor_args():
    sig = inspect.signature(research16::PublicationStructure.__init__)
    params = list(sig.parameters.keys())



def test_labelled_is_not_abstract():
    assert not inspect.isabstract(Labelled)


def test_labelled_constructor_exists():
    assert callable(Labelled.__init__)


def test_labelled_constructor_args():
    sig = inspect.signature(Labelled.__init__)
    params = list(sig.parameters.keys())



def test_research16::reviewnote_is_not_abstract():
    assert not inspect.isabstract(research16::ReviewNote)


def test_research16::reviewnote_constructor_exists():
    assert callable(research16::ReviewNote.__init__)


def test_research16::reviewnote_constructor_args():
    sig = inspect.signature(research16::ReviewNote.__init__)
    params = list(sig.parameters.keys())
    assert "content" in params, "Missing parameter 'content'"

def test_research16::reviewnote_has_content():
    assert hasattr(research16::ReviewNote, "content")
    descriptor = None
    for klass in research16::ReviewNote.__mro__:
        if "content" in klass.__dict__:
            descriptor = klass.__dict__["content"]
            break
    assert isinstance(descriptor, property)



def test_counted_is_not_abstract():
    assert not inspect.isabstract(Counted)


def test_counted_constructor_exists():
    assert callable(Counted.__init__)


def test_counted_constructor_args():
    sig = inspect.signature(Counted.__init__)
    params = list(sig.parameters.keys())



def test_research16::state_is_not_abstract():
    assert not inspect.isabstract(research16::State)


def test_research16::state_constructor_exists():
    assert callable(research16::State.__init__)


def test_research16::state_constructor_args():
    sig = inspect.signature(research16::State.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"

def test_research16::state_has_kind():
    assert hasattr(research16::State, "kind")
    descriptor = None
    for klass in research16::State.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)

def test_research16::state_has_name():
    assert hasattr(research16::State, "name")
    descriptor = None
    for klass in research16::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_research16::state_has_id():
    assert hasattr(research16::State, "id")
    descriptor = None
    for klass in research16::State.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_research16::paperkeyword_is_not_abstract():
    assert not inspect.isabstract(research16::PaperKeyword)


def test_research16::paperkeyword_constructor_exists():
    assert callable(research16::PaperKeyword.__init__)


def test_research16::paperkeyword_constructor_args():
    sig = inspect.signature(research16::PaperKeyword.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"

def test_research16::paperkeyword_has_weight():
    assert hasattr(research16::PaperKeyword, "weight")
    descriptor = None
    for klass in research16::PaperKeyword.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)



def test_research16::progress_is_not_abstract():
    assert not inspect.isabstract(research16::Progress)


def test_research16::progress_constructor_exists():
    assert callable(research16::Progress.__init__)


def test_research16::progress_constructor_args():
    sig = inspect.signature(research16::Progress.__init__)
    params = list(sig.parameters.keys())
    assert "percent" in params, "Missing parameter 'percent'"

def test_research16::progress_has_percent():
    assert hasattr(research16::Progress, "percent")
    descriptor = None
    for klass in research16::Progress.__mro__:
        if "percent" in klass.__dict__:
            descriptor = klass.__dict__["percent"]
            break
    assert isinstance(descriptor, property)



def test_research16::paragraph_is_not_abstract():
    assert not inspect.isabstract(research16::Paragraph)


def test_research16::paragraph_constructor_exists():
    assert callable(research16::Paragraph.__init__)


def test_research16::paragraph_constructor_args():
    sig = inspect.signature(research16::Paragraph.__init__)
    params = list(sig.parameters.keys())
    assert "content" in params, "Missing parameter 'content'"

def test_research16::paragraph_has_content():
    assert hasattr(research16::Paragraph, "content")
    descriptor = None
    for klass in research16::Paragraph.__mro__:
        if "content" in klass.__dict__:
            descriptor = klass.__dict__["content"]
            break
    assert isinstance(descriptor, property)



def test_research16::collaboration_is_not_abstract():
    assert not inspect.isabstract(research16::Collaboration)


def test_research16::collaboration_constructor_exists():
    assert callable(research16::Collaboration.__init__)


def test_research16::collaboration_constructor_args():
    sig = inspect.signature(research16::Collaboration.__init__)
    params = list(sig.parameters.keys())
    assert "ratio" in params, "Missing parameter 'ratio'"

def test_research16::collaboration_has_ratio():
    assert hasattr(research16::Collaboration, "ratio")
    descriptor = None
    for klass in research16::Collaboration.__mro__:
        if "ratio" in klass.__dict__:
            descriptor = klass.__dict__["ratio"]
            break
    assert isinstance(descriptor, property)



def test_research16::position_is_not_abstract():
    assert not inspect.isabstract(research16::Position)


def test_research16::position_constructor_exists():
    assert callable(research16::Position.__init__)


def test_research16::position_constructor_args():
    sig = inspect.signature(research16::Position.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"

def test_research16::position_has_description():
    assert hasattr(research16::Position, "description")
    descriptor = None
    for klass in research16::Position.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_research16::skill_is_not_abstract():
    assert not inspect.isabstract(research16::Skill)


def test_research16::skill_constructor_exists():
    assert callable(research16::Skill.__init__)


def test_research16::skill_constructor_args():
    sig = inspect.signature(research16::Skill.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"

def test_research16::skill_has_description():
    assert hasattr(research16::Skill, "description")
    descriptor = None
    for klass in research16::Skill.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_research16::paper_is_not_abstract():
    assert not inspect.isabstract(research16::Paper)


def test_research16::paper_constructor_exists():
    assert callable(research16::Paper.__init__)


def test_research16::paper_constructor_args():
    sig = inspect.signature(research16::Paper.__init__)
    params = list(sig.parameters.keys())



def test_research16::review_is_not_abstract():
    assert not inspect.isabstract(research16::Review)


def test_research16::review_constructor_exists():
    assert callable(research16::Review.__init__)


def test_research16::review_constructor_args():
    sig = inspect.signature(research16::Review.__init__)
    params = list(sig.parameters.keys())
    assert "date" in params, "Missing parameter 'date'"

def test_research16::review_has_date():
    assert hasattr(research16::Review, "date")
    descriptor = None
    for klass in research16::Review.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)



def test_research16::write_is_not_abstract():
    assert not inspect.isabstract(research16::Write)


def test_research16::write_constructor_exists():
    assert callable(research16::Write.__init__)


def test_research16::write_constructor_args():
    sig = inspect.signature(research16::Write.__init__)
    params = list(sig.parameters.keys())
    assert "timeSpent" in params, "Missing parameter 'timeSpent'"

def test_research16::write_has_timeSpent():
    assert hasattr(research16::Write, "timeSpent")
    descriptor = None
    for klass in research16::Write.__mro__:
        if "timeSpent" in klass.__dict__:
            descriptor = klass.__dict__["timeSpent"]
            break
    assert isinstance(descriptor, property)



def test_research16::researcher_is_not_abstract():
    assert not inspect.isabstract(research16::Researcher)


def test_research16::researcher_constructor_exists():
    assert callable(research16::Researcher.__init__)


def test_research16::researcher_constructor_args():
    sig = inspect.signature(research16::Researcher.__init__)
    params = list(sig.parameters.keys())
    assert "forName" in params, "Missing parameter 'forName'"
    assert "name" in params, "Missing parameter 'name'"

def test_research16::researcher_has_forName():
    assert hasattr(research16::Researcher, "forName")
    descriptor = None
    for klass in research16::Researcher.__mro__:
        if "forName" in klass.__dict__:
            descriptor = klass.__dict__["forName"]
            break
    assert isinstance(descriptor, property)

def test_research16::researcher_has_name():
    assert hasattr(research16::Researcher, "name")
    descriptor = None
    for klass in research16::Researcher.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_statetype_exists():
    # Check that the Enumeration exists
    assert StateType is not None

def test_statetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in StateType]
    expected_literals = [
        "ongoing",
        "initial",
        "final",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in StateType"


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
research16::Phase_strategy = st.builds(
    research16::Phase,
    name=
        safe_text
)
Named_strategy = st.builds(
    Named,
)
research16::PublicationProcess_strategy = st.builds(
    research16::PublicationProcess,
    minTime=
        st.integers(),
    maxTime=
        st.integers()
)
research16::Action_strategy = st.builds(
    research16::Action,
    actionStatement=
        safe_text,
    actionLabel=
        safe_text
)
StateMachineObject_strategy = st.builds(
    StateMachineObject,
)
research16::Transition_strategy = st.builds(
    research16::Transition,
    guardLabel=
        safe_text,
    guardExpression=
        safe_text
)
research16::StateMachineObject_strategy = st.builds(
    research16::StateMachineObject,
    label=
        safe_text
)
research16::StateMachineVariable_strategy = st.builds(
    research16::StateMachineVariable,
)
research16::Keyword_strategy = st.builds(
    research16::Keyword,
    word=
        safe_text
)
research16::Labelled_strategy = st.builds(
    research16::Labelled,
    lname=
        safe_text
)
research16::Counted_strategy = st.builds(
    research16::Counted,
    id=
        st.integers()
)
research16::Named_strategy = st.builds(
    research16::Named,
    name=
        safe_text
)
research16::PublicationStatus_strategy = st.builds(
    research16::PublicationStatus,
    label=
        safe_text
)
research16::PublicationSystem_strategy = st.builds(
    research16::PublicationSystem,
)
research16::KnowledgeManager_strategy = st.builds(
    research16::KnowledgeManager,
)
research16::PublicationStructure_strategy = st.builds(
    research16::PublicationStructure,
)
Labelled_strategy = st.builds(
    Labelled,
)
research16::ReviewNote_strategy = st.builds(
    research16::ReviewNote,
    content=
        safe_text
)
Counted_strategy = st.builds(
    Counted,
)
research16::State_strategy = st.builds(
    research16::State,
    kind=
        safe_text,
    name=
        safe_text,
    id=
        st.integers()
)
research16::PaperKeyword_strategy = st.builds(
    research16::PaperKeyword,
    weight=
        st.integers()
)
research16::Progress_strategy = st.builds(
    research16::Progress,
    percent=
        st.integers()
)
research16::Paragraph_strategy = st.builds(
    research16::Paragraph,
    content=
        safe_text
)
research16::Collaboration_strategy = st.builds(
    research16::Collaboration,
    ratio=
        st.integers()
)
research16::Position_strategy = st.builds(
    research16::Position,
    description=
        safe_text
)
research16::Skill_strategy = st.builds(
    research16::Skill,
    description=
        safe_text
)
research16::Paper_strategy = st.builds(
    research16::Paper,
)
research16::Review_strategy = st.builds(
    research16::Review,
    date=
        st.dates()
)
research16::Write_strategy = st.builds(
    research16::Write,
    timeSpent=
        st.integers()
)
research16::Researcher_strategy = st.builds(
    research16::Researcher,
    forName=
        safe_text,
    name=
        safe_text
)

@given(instance=research16::Phase_strategy)
@settings(max_examples=50)
def test_research16::phase_instantiation(instance):
    assert isinstance(instance, research16::Phase)

@given(instance=research16::Phase_strategy)
def test_research16::phase_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=research16::Phase_strategy)
def test_research16::phase_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Named_strategy)
@settings(max_examples=50)
def test_named_instantiation(instance):
    assert isinstance(instance, Named)

@given(instance=research16::PublicationProcess_strategy)
@settings(max_examples=50)
def test_research16::publicationprocess_instantiation(instance):
    assert isinstance(instance, research16::PublicationProcess)

@given(instance=research16::PublicationProcess_strategy)
def test_research16::publicationprocess_minTime_type(instance):
    assert isinstance(instance.minTime, int)


@given(instance=research16::PublicationProcess_strategy)
def test_research16::publicationprocess_minTime_setter(instance):
    original = instance.minTime
    instance.minTime = original
    assert instance.minTime == original

@given(instance=research16::PublicationProcess_strategy)
def test_research16::publicationprocess_maxTime_type(instance):
    assert isinstance(instance.maxTime, int)


@given(instance=research16::PublicationProcess_strategy)
def test_research16::publicationprocess_maxTime_setter(instance):
    original = instance.maxTime
    instance.maxTime = original
    assert instance.maxTime == original

@given(instance=research16::Action_strategy)
@settings(max_examples=50)
def test_research16::action_instantiation(instance):
    assert isinstance(instance, research16::Action)

@given(instance=research16::Action_strategy)
def test_research16::action_actionStatement_type(instance):
    assert isinstance(instance.actionStatement, str)


@given(instance=research16::Action_strategy)
def test_research16::action_actionStatement_setter(instance):
    original = instance.actionStatement
    instance.actionStatement = original
    assert instance.actionStatement == original

@given(instance=research16::Action_strategy)
def test_research16::action_actionLabel_type(instance):
    assert isinstance(instance.actionLabel, str)


@given(instance=research16::Action_strategy)
def test_research16::action_actionLabel_setter(instance):
    original = instance.actionLabel
    instance.actionLabel = original
    assert instance.actionLabel == original

@given(instance=StateMachineObject_strategy)
@settings(max_examples=50)
def test_statemachineobject_instantiation(instance):
    assert isinstance(instance, StateMachineObject)

@given(instance=research16::Transition_strategy)
@settings(max_examples=50)
def test_research16::transition_instantiation(instance):
    assert isinstance(instance, research16::Transition)

@given(instance=research16::Transition_strategy)
def test_research16::transition_guardLabel_type(instance):
    assert isinstance(instance.guardLabel, str)


@given(instance=research16::Transition_strategy)
def test_research16::transition_guardLabel_setter(instance):
    original = instance.guardLabel
    instance.guardLabel = original
    assert instance.guardLabel == original

@given(instance=research16::Transition_strategy)
def test_research16::transition_guardExpression_type(instance):
    assert isinstance(instance.guardExpression, str)


@given(instance=research16::Transition_strategy)
def test_research16::transition_guardExpression_setter(instance):
    original = instance.guardExpression
    instance.guardExpression = original
    assert instance.guardExpression == original

@given(instance=research16::StateMachineObject_strategy)
@settings(max_examples=50)
def test_research16::statemachineobject_instantiation(instance):
    assert isinstance(instance, research16::StateMachineObject)

@given(instance=research16::StateMachineObject_strategy)
def test_research16::statemachineobject_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=research16::StateMachineObject_strategy)
def test_research16::statemachineobject_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=research16::StateMachineVariable_strategy)
@settings(max_examples=50)
def test_research16::statemachinevariable_instantiation(instance):
    assert isinstance(instance, research16::StateMachineVariable)

@given(instance=research16::Keyword_strategy)
@settings(max_examples=50)
def test_research16::keyword_instantiation(instance):
    assert isinstance(instance, research16::Keyword)

@given(instance=research16::Keyword_strategy)
def test_research16::keyword_word_type(instance):
    assert isinstance(instance.word, str)


@given(instance=research16::Keyword_strategy)
def test_research16::keyword_word_setter(instance):
    original = instance.word
    instance.word = original
    assert instance.word == original

@given(instance=research16::Labelled_strategy)
@settings(max_examples=50)
def test_research16::labelled_instantiation(instance):
    assert isinstance(instance, research16::Labelled)

@given(instance=research16::Labelled_strategy)
def test_research16::labelled_lname_type(instance):
    assert isinstance(instance.lname, str)


@given(instance=research16::Labelled_strategy)
def test_research16::labelled_lname_setter(instance):
    original = instance.lname
    instance.lname = original
    assert instance.lname == original

@given(instance=research16::Counted_strategy)
@settings(max_examples=50)
def test_research16::counted_instantiation(instance):
    assert isinstance(instance, research16::Counted)

@given(instance=research16::Counted_strategy)
def test_research16::counted_id_type(instance):
    assert isinstance(instance.id, int)


@given(instance=research16::Counted_strategy)
def test_research16::counted_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=research16::Named_strategy)
@settings(max_examples=50)
def test_research16::named_instantiation(instance):
    assert isinstance(instance, research16::Named)

@given(instance=research16::Named_strategy)
def test_research16::named_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=research16::Named_strategy)
def test_research16::named_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=research16::PublicationStatus_strategy)
@settings(max_examples=50)
def test_research16::publicationstatus_instantiation(instance):
    assert isinstance(instance, research16::PublicationStatus)

@given(instance=research16::PublicationStatus_strategy)
def test_research16::publicationstatus_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=research16::PublicationStatus_strategy)
def test_research16::publicationstatus_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=research16::PublicationSystem_strategy)
@settings(max_examples=50)
def test_research16::publicationsystem_instantiation(instance):
    assert isinstance(instance, research16::PublicationSystem)

@given(instance=research16::KnowledgeManager_strategy)
@settings(max_examples=50)
def test_research16::knowledgemanager_instantiation(instance):
    assert isinstance(instance, research16::KnowledgeManager)

@given(instance=research16::PublicationStructure_strategy)
@settings(max_examples=50)
def test_research16::publicationstructure_instantiation(instance):
    assert isinstance(instance, research16::PublicationStructure)

@given(instance=Labelled_strategy)
@settings(max_examples=50)
def test_labelled_instantiation(instance):
    assert isinstance(instance, Labelled)

@given(instance=research16::ReviewNote_strategy)
@settings(max_examples=50)
def test_research16::reviewnote_instantiation(instance):
    assert isinstance(instance, research16::ReviewNote)

@given(instance=research16::ReviewNote_strategy)
def test_research16::reviewnote_content_type(instance):
    assert isinstance(instance.content, str)


@given(instance=research16::ReviewNote_strategy)
def test_research16::reviewnote_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original

@given(instance=Counted_strategy)
@settings(max_examples=50)
def test_counted_instantiation(instance):
    assert isinstance(instance, Counted)

@given(instance=research16::State_strategy)
@settings(max_examples=50)
def test_research16::state_instantiation(instance):
    assert isinstance(instance, research16::State)

@given(instance=research16::State_strategy)
def test_research16::state_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=research16::State_strategy)
def test_research16::state_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=research16::State_strategy)
def test_research16::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=research16::State_strategy)
def test_research16::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=research16::State_strategy)
def test_research16::state_id_type(instance):
    assert isinstance(instance.id, int)


@given(instance=research16::State_strategy)
def test_research16::state_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=research16::PaperKeyword_strategy)
@settings(max_examples=50)
def test_research16::paperkeyword_instantiation(instance):
    assert isinstance(instance, research16::PaperKeyword)

@given(instance=research16::PaperKeyword_strategy)
def test_research16::paperkeyword_weight_type(instance):
    assert isinstance(instance.weight, int)


@given(instance=research16::PaperKeyword_strategy)
def test_research16::paperkeyword_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=research16::Progress_strategy)
@settings(max_examples=50)
def test_research16::progress_instantiation(instance):
    assert isinstance(instance, research16::Progress)

@given(instance=research16::Progress_strategy)
def test_research16::progress_percent_type(instance):
    assert isinstance(instance.percent, int)


@given(instance=research16::Progress_strategy)
def test_research16::progress_percent_setter(instance):
    original = instance.percent
    instance.percent = original
    assert instance.percent == original

@given(instance=research16::Paragraph_strategy)
@settings(max_examples=50)
def test_research16::paragraph_instantiation(instance):
    assert isinstance(instance, research16::Paragraph)

@given(instance=research16::Paragraph_strategy)
def test_research16::paragraph_content_type(instance):
    assert isinstance(instance.content, str)


@given(instance=research16::Paragraph_strategy)
def test_research16::paragraph_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original

@given(instance=research16::Collaboration_strategy)
@settings(max_examples=50)
def test_research16::collaboration_instantiation(instance):
    assert isinstance(instance, research16::Collaboration)

@given(instance=research16::Collaboration_strategy)
def test_research16::collaboration_ratio_type(instance):
    assert isinstance(instance.ratio, int)


@given(instance=research16::Collaboration_strategy)
def test_research16::collaboration_ratio_setter(instance):
    original = instance.ratio
    instance.ratio = original
    assert instance.ratio == original

@given(instance=research16::Position_strategy)
@settings(max_examples=50)
def test_research16::position_instantiation(instance):
    assert isinstance(instance, research16::Position)

@given(instance=research16::Position_strategy)
def test_research16::position_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=research16::Position_strategy)
def test_research16::position_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=research16::Skill_strategy)
@settings(max_examples=50)
def test_research16::skill_instantiation(instance):
    assert isinstance(instance, research16::Skill)

@given(instance=research16::Skill_strategy)
def test_research16::skill_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=research16::Skill_strategy)
def test_research16::skill_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=research16::Paper_strategy)
@settings(max_examples=50)
def test_research16::paper_instantiation(instance):
    assert isinstance(instance, research16::Paper)

@given(instance=research16::Review_strategy)
@settings(max_examples=50)
def test_research16::review_instantiation(instance):
    assert isinstance(instance, research16::Review)

@given(instance=research16::Review_strategy)
def test_research16::review_date_type(instance):
    assert isinstance(instance.date, date)


@given(instance=research16::Review_strategy)
def test_research16::review_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original

@given(instance=research16::Write_strategy)
@settings(max_examples=50)
def test_research16::write_instantiation(instance):
    assert isinstance(instance, research16::Write)

@given(instance=research16::Write_strategy)
def test_research16::write_timeSpent_type(instance):
    assert isinstance(instance.timeSpent, int)


@given(instance=research16::Write_strategy)
def test_research16::write_timeSpent_setter(instance):
    original = instance.timeSpent
    instance.timeSpent = original
    assert instance.timeSpent == original

@given(instance=research16::Researcher_strategy)
@settings(max_examples=50)
def test_research16::researcher_instantiation(instance):
    assert isinstance(instance, research16::Researcher)

@given(instance=research16::Researcher_strategy)
def test_research16::researcher_forName_type(instance):
    assert isinstance(instance.forName, str)


@given(instance=research16::Researcher_strategy)
def test_research16::researcher_forName_setter(instance):
    original = instance.forName
    instance.forName = original
    assert instance.forName == original

@given(instance=research16::Researcher_strategy)
def test_research16::researcher_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=research16::Researcher_strategy)
def test_research16::researcher_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
