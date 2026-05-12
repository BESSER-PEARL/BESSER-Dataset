import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    research18::Action,
    StateMachineObject,
    research18::Transition,
    research18::StateMachineObject,
    research18::StateMachineVariable,
    research18::Labelled,
    research18::Counted,
    research18::Named,
    research18::PublicationStatus,
    Counted,
    research18::State,
    research18::PaperKeyword,
    Labelled,
    research18::Write,
    research18::Researcher,
    research18::Phase,
    research18::Progress,
    research18::Collaboration,
    research18::Skill,
    research18::Review,
    Named,
    research18::Paragraph,
    research18::Keyword,
    research18::PublicationSystem,
    research18::PublicationStructure,
    research18::KnowledgeManager,
    research18::Paper,
    research18::Position,
    research18::ReviewNote,
    research18::PublicationProcess,
    StateType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_research18::action_is_not_abstract():
    assert not inspect.isabstract(research18::Action)


def test_research18::action_constructor_exists():
    assert callable(research18::Action.__init__)


def test_research18::action_constructor_args():
    sig = inspect.signature(research18::Action.__init__)
    params = list(sig.parameters.keys())
    assert "actionLabel" in params, "Missing parameter 'actionLabel'"
    assert "actionStatement" in params, "Missing parameter 'actionStatement'"

def test_research18::action_has_actionLabel():
    assert hasattr(research18::Action, "actionLabel")
    descriptor = None
    for klass in research18::Action.__mro__:
        if "actionLabel" in klass.__dict__:
            descriptor = klass.__dict__["actionLabel"]
            break
    assert isinstance(descriptor, property)

def test_research18::action_has_actionStatement():
    assert hasattr(research18::Action, "actionStatement")
    descriptor = None
    for klass in research18::Action.__mro__:
        if "actionStatement" in klass.__dict__:
            descriptor = klass.__dict__["actionStatement"]
            break
    assert isinstance(descriptor, property)



def test_statemachineobject_is_not_abstract():
    assert not inspect.isabstract(StateMachineObject)


def test_statemachineobject_constructor_exists():
    assert callable(StateMachineObject.__init__)


def test_statemachineobject_constructor_args():
    sig = inspect.signature(StateMachineObject.__init__)
    params = list(sig.parameters.keys())



def test_research18::transition_is_not_abstract():
    assert not inspect.isabstract(research18::Transition)


def test_research18::transition_constructor_exists():
    assert callable(research18::Transition.__init__)


def test_research18::transition_constructor_args():
    sig = inspect.signature(research18::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "guardExpression" in params, "Missing parameter 'guardExpression'"
    assert "guardLabel" in params, "Missing parameter 'guardLabel'"

def test_research18::transition_has_guardExpression():
    assert hasattr(research18::Transition, "guardExpression")
    descriptor = None
    for klass in research18::Transition.__mro__:
        if "guardExpression" in klass.__dict__:
            descriptor = klass.__dict__["guardExpression"]
            break
    assert isinstance(descriptor, property)

def test_research18::transition_has_guardLabel():
    assert hasattr(research18::Transition, "guardLabel")
    descriptor = None
    for klass in research18::Transition.__mro__:
        if "guardLabel" in klass.__dict__:
            descriptor = klass.__dict__["guardLabel"]
            break
    assert isinstance(descriptor, property)



def test_research18::statemachineobject_is_not_abstract():
    assert not inspect.isabstract(research18::StateMachineObject)


def test_research18::statemachineobject_constructor_exists():
    assert callable(research18::StateMachineObject.__init__)


def test_research18::statemachineobject_constructor_args():
    sig = inspect.signature(research18::StateMachineObject.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_research18::statemachineobject_has_label():
    assert hasattr(research18::StateMachineObject, "label")
    descriptor = None
    for klass in research18::StateMachineObject.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_research18::statemachinevariable_is_not_abstract():
    assert not inspect.isabstract(research18::StateMachineVariable)


def test_research18::statemachinevariable_constructor_exists():
    assert callable(research18::StateMachineVariable.__init__)


def test_research18::statemachinevariable_constructor_args():
    sig = inspect.signature(research18::StateMachineVariable.__init__)
    params = list(sig.parameters.keys())



def test_research18::labelled_is_not_abstract():
    assert not inspect.isabstract(research18::Labelled)


def test_research18::labelled_constructor_exists():
    assert callable(research18::Labelled.__init__)


def test_research18::labelled_constructor_args():
    sig = inspect.signature(research18::Labelled.__init__)
    params = list(sig.parameters.keys())
    assert "lname" in params, "Missing parameter 'lname'"

def test_research18::labelled_has_lname():
    assert hasattr(research18::Labelled, "lname")
    descriptor = None
    for klass in research18::Labelled.__mro__:
        if "lname" in klass.__dict__:
            descriptor = klass.__dict__["lname"]
            break
    assert isinstance(descriptor, property)



def test_research18::counted_is_not_abstract():
    assert not inspect.isabstract(research18::Counted)


def test_research18::counted_constructor_exists():
    assert callable(research18::Counted.__init__)


def test_research18::counted_constructor_args():
    sig = inspect.signature(research18::Counted.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_research18::counted_has_id():
    assert hasattr(research18::Counted, "id")
    descriptor = None
    for klass in research18::Counted.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_research18::named_is_not_abstract():
    assert not inspect.isabstract(research18::Named)


def test_research18::named_constructor_exists():
    assert callable(research18::Named.__init__)


def test_research18::named_constructor_args():
    sig = inspect.signature(research18::Named.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_research18::named_has_name():
    assert hasattr(research18::Named, "name")
    descriptor = None
    for klass in research18::Named.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_research18::publicationstatus_is_not_abstract():
    assert not inspect.isabstract(research18::PublicationStatus)


def test_research18::publicationstatus_constructor_exists():
    assert callable(research18::PublicationStatus.__init__)


def test_research18::publicationstatus_constructor_args():
    sig = inspect.signature(research18::PublicationStatus.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_research18::publicationstatus_has_label():
    assert hasattr(research18::PublicationStatus, "label")
    descriptor = None
    for klass in research18::PublicationStatus.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_counted_is_not_abstract():
    assert not inspect.isabstract(Counted)


def test_counted_constructor_exists():
    assert callable(Counted.__init__)


def test_counted_constructor_args():
    sig = inspect.signature(Counted.__init__)
    params = list(sig.parameters.keys())



def test_research18::state_is_not_abstract():
    assert not inspect.isabstract(research18::State)


def test_research18::state_constructor_exists():
    assert callable(research18::State.__init__)


def test_research18::state_constructor_args():
    sig = inspect.signature(research18::State.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"

def test_research18::state_has_kind():
    assert hasattr(research18::State, "kind")
    descriptor = None
    for klass in research18::State.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)

def test_research18::state_has_id():
    assert hasattr(research18::State, "id")
    descriptor = None
    for klass in research18::State.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_research18::state_has_name():
    assert hasattr(research18::State, "name")
    descriptor = None
    for klass in research18::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_research18::paperkeyword_is_not_abstract():
    assert not inspect.isabstract(research18::PaperKeyword)


def test_research18::paperkeyword_constructor_exists():
    assert callable(research18::PaperKeyword.__init__)


def test_research18::paperkeyword_constructor_args():
    sig = inspect.signature(research18::PaperKeyword.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"

def test_research18::paperkeyword_has_weight():
    assert hasattr(research18::PaperKeyword, "weight")
    descriptor = None
    for klass in research18::PaperKeyword.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)



def test_labelled_is_not_abstract():
    assert not inspect.isabstract(Labelled)


def test_labelled_constructor_exists():
    assert callable(Labelled.__init__)


def test_labelled_constructor_args():
    sig = inspect.signature(Labelled.__init__)
    params = list(sig.parameters.keys())



def test_research18::write_is_not_abstract():
    assert not inspect.isabstract(research18::Write)


def test_research18::write_constructor_exists():
    assert callable(research18::Write.__init__)


def test_research18::write_constructor_args():
    sig = inspect.signature(research18::Write.__init__)
    params = list(sig.parameters.keys())
    assert "timeSpent" in params, "Missing parameter 'timeSpent'"

def test_research18::write_has_timeSpent():
    assert hasattr(research18::Write, "timeSpent")
    descriptor = None
    for klass in research18::Write.__mro__:
        if "timeSpent" in klass.__dict__:
            descriptor = klass.__dict__["timeSpent"]
            break
    assert isinstance(descriptor, property)



def test_research18::researcher_is_not_abstract():
    assert not inspect.isabstract(research18::Researcher)


def test_research18::researcher_constructor_exists():
    assert callable(research18::Researcher.__init__)


def test_research18::researcher_constructor_args():
    sig = inspect.signature(research18::Researcher.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "forName" in params, "Missing parameter 'forName'"

def test_research18::researcher_has_name():
    assert hasattr(research18::Researcher, "name")
    descriptor = None
    for klass in research18::Researcher.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_research18::researcher_has_forName():
    assert hasattr(research18::Researcher, "forName")
    descriptor = None
    for klass in research18::Researcher.__mro__:
        if "forName" in klass.__dict__:
            descriptor = klass.__dict__["forName"]
            break
    assert isinstance(descriptor, property)



def test_research18::phase_is_not_abstract():
    assert not inspect.isabstract(research18::Phase)


def test_research18::phase_constructor_exists():
    assert callable(research18::Phase.__init__)


def test_research18::phase_constructor_args():
    sig = inspect.signature(research18::Phase.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_research18::phase_has_name():
    assert hasattr(research18::Phase, "name")
    descriptor = None
    for klass in research18::Phase.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_research18::progress_is_not_abstract():
    assert not inspect.isabstract(research18::Progress)


def test_research18::progress_constructor_exists():
    assert callable(research18::Progress.__init__)


def test_research18::progress_constructor_args():
    sig = inspect.signature(research18::Progress.__init__)
    params = list(sig.parameters.keys())
    assert "percent" in params, "Missing parameter 'percent'"

def test_research18::progress_has_percent():
    assert hasattr(research18::Progress, "percent")
    descriptor = None
    for klass in research18::Progress.__mro__:
        if "percent" in klass.__dict__:
            descriptor = klass.__dict__["percent"]
            break
    assert isinstance(descriptor, property)



def test_research18::collaboration_is_not_abstract():
    assert not inspect.isabstract(research18::Collaboration)


def test_research18::collaboration_constructor_exists():
    assert callable(research18::Collaboration.__init__)


def test_research18::collaboration_constructor_args():
    sig = inspect.signature(research18::Collaboration.__init__)
    params = list(sig.parameters.keys())
    assert "ratio" in params, "Missing parameter 'ratio'"

def test_research18::collaboration_has_ratio():
    assert hasattr(research18::Collaboration, "ratio")
    descriptor = None
    for klass in research18::Collaboration.__mro__:
        if "ratio" in klass.__dict__:
            descriptor = klass.__dict__["ratio"]
            break
    assert isinstance(descriptor, property)



def test_research18::skill_is_not_abstract():
    assert not inspect.isabstract(research18::Skill)


def test_research18::skill_constructor_exists():
    assert callable(research18::Skill.__init__)


def test_research18::skill_constructor_args():
    sig = inspect.signature(research18::Skill.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"

def test_research18::skill_has_description():
    assert hasattr(research18::Skill, "description")
    descriptor = None
    for klass in research18::Skill.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_research18::review_is_not_abstract():
    assert not inspect.isabstract(research18::Review)


def test_research18::review_constructor_exists():
    assert callable(research18::Review.__init__)


def test_research18::review_constructor_args():
    sig = inspect.signature(research18::Review.__init__)
    params = list(sig.parameters.keys())
    assert "date" in params, "Missing parameter 'date'"

def test_research18::review_has_date():
    assert hasattr(research18::Review, "date")
    descriptor = None
    for klass in research18::Review.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)



def test_named_is_not_abstract():
    assert not inspect.isabstract(Named)


def test_named_constructor_exists():
    assert callable(Named.__init__)


def test_named_constructor_args():
    sig = inspect.signature(Named.__init__)
    params = list(sig.parameters.keys())



def test_research18::paragraph_is_not_abstract():
    assert not inspect.isabstract(research18::Paragraph)


def test_research18::paragraph_constructor_exists():
    assert callable(research18::Paragraph.__init__)


def test_research18::paragraph_constructor_args():
    sig = inspect.signature(research18::Paragraph.__init__)
    params = list(sig.parameters.keys())
    assert "content" in params, "Missing parameter 'content'"

def test_research18::paragraph_has_content():
    assert hasattr(research18::Paragraph, "content")
    descriptor = None
    for klass in research18::Paragraph.__mro__:
        if "content" in klass.__dict__:
            descriptor = klass.__dict__["content"]
            break
    assert isinstance(descriptor, property)



def test_research18::keyword_is_not_abstract():
    assert not inspect.isabstract(research18::Keyword)


def test_research18::keyword_constructor_exists():
    assert callable(research18::Keyword.__init__)


def test_research18::keyword_constructor_args():
    sig = inspect.signature(research18::Keyword.__init__)
    params = list(sig.parameters.keys())
    assert "word" in params, "Missing parameter 'word'"

def test_research18::keyword_has_word():
    assert hasattr(research18::Keyword, "word")
    descriptor = None
    for klass in research18::Keyword.__mro__:
        if "word" in klass.__dict__:
            descriptor = klass.__dict__["word"]
            break
    assert isinstance(descriptor, property)



def test_research18::publicationsystem_is_not_abstract():
    assert not inspect.isabstract(research18::PublicationSystem)


def test_research18::publicationsystem_constructor_exists():
    assert callable(research18::PublicationSystem.__init__)


def test_research18::publicationsystem_constructor_args():
    sig = inspect.signature(research18::PublicationSystem.__init__)
    params = list(sig.parameters.keys())



def test_research18::publicationstructure_is_not_abstract():
    assert not inspect.isabstract(research18::PublicationStructure)


def test_research18::publicationstructure_constructor_exists():
    assert callable(research18::PublicationStructure.__init__)


def test_research18::publicationstructure_constructor_args():
    sig = inspect.signature(research18::PublicationStructure.__init__)
    params = list(sig.parameters.keys())



def test_research18::knowledgemanager_is_not_abstract():
    assert not inspect.isabstract(research18::KnowledgeManager)


def test_research18::knowledgemanager_constructor_exists():
    assert callable(research18::KnowledgeManager.__init__)


def test_research18::knowledgemanager_constructor_args():
    sig = inspect.signature(research18::KnowledgeManager.__init__)
    params = list(sig.parameters.keys())



def test_research18::paper_is_not_abstract():
    assert not inspect.isabstract(research18::Paper)


def test_research18::paper_constructor_exists():
    assert callable(research18::Paper.__init__)


def test_research18::paper_constructor_args():
    sig = inspect.signature(research18::Paper.__init__)
    params = list(sig.parameters.keys())



def test_research18::position_is_not_abstract():
    assert not inspect.isabstract(research18::Position)


def test_research18::position_constructor_exists():
    assert callable(research18::Position.__init__)


def test_research18::position_constructor_args():
    sig = inspect.signature(research18::Position.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"

def test_research18::position_has_description():
    assert hasattr(research18::Position, "description")
    descriptor = None
    for klass in research18::Position.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_research18::reviewnote_is_not_abstract():
    assert not inspect.isabstract(research18::ReviewNote)


def test_research18::reviewnote_constructor_exists():
    assert callable(research18::ReviewNote.__init__)


def test_research18::reviewnote_constructor_args():
    sig = inspect.signature(research18::ReviewNote.__init__)
    params = list(sig.parameters.keys())
    assert "content" in params, "Missing parameter 'content'"

def test_research18::reviewnote_has_content():
    assert hasattr(research18::ReviewNote, "content")
    descriptor = None
    for klass in research18::ReviewNote.__mro__:
        if "content" in klass.__dict__:
            descriptor = klass.__dict__["content"]
            break
    assert isinstance(descriptor, property)



def test_research18::publicationprocess_is_not_abstract():
    assert not inspect.isabstract(research18::PublicationProcess)


def test_research18::publicationprocess_constructor_exists():
    assert callable(research18::PublicationProcess.__init__)


def test_research18::publicationprocess_constructor_args():
    sig = inspect.signature(research18::PublicationProcess.__init__)
    params = list(sig.parameters.keys())
    assert "minTime" in params, "Missing parameter 'minTime'"
    assert "maxTime" in params, "Missing parameter 'maxTime'"

def test_research18::publicationprocess_has_minTime():
    assert hasattr(research18::PublicationProcess, "minTime")
    descriptor = None
    for klass in research18::PublicationProcess.__mro__:
        if "minTime" in klass.__dict__:
            descriptor = klass.__dict__["minTime"]
            break
    assert isinstance(descriptor, property)

def test_research18::publicationprocess_has_maxTime():
    assert hasattr(research18::PublicationProcess, "maxTime")
    descriptor = None
    for klass in research18::PublicationProcess.__mro__:
        if "maxTime" in klass.__dict__:
            descriptor = klass.__dict__["maxTime"]
            break
    assert isinstance(descriptor, property)

def test_statetype_exists():
    # Check that the Enumeration exists
    assert StateType is not None

def test_statetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in StateType]
    expected_literals = [
        "final",
        "initial",
        "ongoing",
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
research18::Action_strategy = st.builds(
    research18::Action,
    actionLabel=
        safe_text,
    actionStatement=
        safe_text
)
StateMachineObject_strategy = st.builds(
    StateMachineObject,
)
research18::Transition_strategy = st.builds(
    research18::Transition,
    guardExpression=
        safe_text,
    guardLabel=
        safe_text
)
research18::StateMachineObject_strategy = st.builds(
    research18::StateMachineObject,
    label=
        safe_text
)
research18::StateMachineVariable_strategy = st.builds(
    research18::StateMachineVariable,
)
research18::Labelled_strategy = st.builds(
    research18::Labelled,
    lname=
        safe_text
)
research18::Counted_strategy = st.builds(
    research18::Counted,
    id=
        st.integers()
)
research18::Named_strategy = st.builds(
    research18::Named,
    name=
        safe_text
)
research18::PublicationStatus_strategy = st.builds(
    research18::PublicationStatus,
    label=
        safe_text
)
Counted_strategy = st.builds(
    Counted,
)
research18::State_strategy = st.builds(
    research18::State,
    kind=
        safe_text,
    id=
        st.integers(),
    name=
        safe_text
)
research18::PaperKeyword_strategy = st.builds(
    research18::PaperKeyword,
    weight=
        st.integers()
)
Labelled_strategy = st.builds(
    Labelled,
)
research18::Write_strategy = st.builds(
    research18::Write,
    timeSpent=
        st.integers()
)
research18::Researcher_strategy = st.builds(
    research18::Researcher,
    name=
        safe_text,
    forName=
        safe_text
)
research18::Phase_strategy = st.builds(
    research18::Phase,
    name=
        safe_text
)
research18::Progress_strategy = st.builds(
    research18::Progress,
    percent=
        st.integers()
)
research18::Collaboration_strategy = st.builds(
    research18::Collaboration,
    ratio=
        st.integers()
)
research18::Skill_strategy = st.builds(
    research18::Skill,
    description=
        safe_text
)
research18::Review_strategy = st.builds(
    research18::Review,
    date=
        st.dates()
)
Named_strategy = st.builds(
    Named,
)
research18::Paragraph_strategy = st.builds(
    research18::Paragraph,
    content=
        safe_text
)
research18::Keyword_strategy = st.builds(
    research18::Keyword,
    word=
        safe_text
)
research18::PublicationSystem_strategy = st.builds(
    research18::PublicationSystem,
)
research18::PublicationStructure_strategy = st.builds(
    research18::PublicationStructure,
)
research18::KnowledgeManager_strategy = st.builds(
    research18::KnowledgeManager,
)
research18::Paper_strategy = st.builds(
    research18::Paper,
)
research18::Position_strategy = st.builds(
    research18::Position,
    description=
        safe_text
)
research18::ReviewNote_strategy = st.builds(
    research18::ReviewNote,
    content=
        safe_text
)
research18::PublicationProcess_strategy = st.builds(
    research18::PublicationProcess,
    minTime=
        st.integers(),
    maxTime=
        st.integers()
)

@given(instance=research18::Action_strategy)
@settings(max_examples=50)
def test_research18::action_instantiation(instance):
    assert isinstance(instance, research18::Action)

@given(instance=research18::Action_strategy)
def test_research18::action_actionLabel_type(instance):
    assert isinstance(instance.actionLabel, str)


@given(instance=research18::Action_strategy)
def test_research18::action_actionLabel_setter(instance):
    original = instance.actionLabel
    instance.actionLabel = original
    assert instance.actionLabel == original

@given(instance=research18::Action_strategy)
def test_research18::action_actionStatement_type(instance):
    assert isinstance(instance.actionStatement, str)


@given(instance=research18::Action_strategy)
def test_research18::action_actionStatement_setter(instance):
    original = instance.actionStatement
    instance.actionStatement = original
    assert instance.actionStatement == original

@given(instance=StateMachineObject_strategy)
@settings(max_examples=50)
def test_statemachineobject_instantiation(instance):
    assert isinstance(instance, StateMachineObject)

@given(instance=research18::Transition_strategy)
@settings(max_examples=50)
def test_research18::transition_instantiation(instance):
    assert isinstance(instance, research18::Transition)

@given(instance=research18::Transition_strategy)
def test_research18::transition_guardExpression_type(instance):
    assert isinstance(instance.guardExpression, str)


@given(instance=research18::Transition_strategy)
def test_research18::transition_guardExpression_setter(instance):
    original = instance.guardExpression
    instance.guardExpression = original
    assert instance.guardExpression == original

@given(instance=research18::Transition_strategy)
def test_research18::transition_guardLabel_type(instance):
    assert isinstance(instance.guardLabel, str)


@given(instance=research18::Transition_strategy)
def test_research18::transition_guardLabel_setter(instance):
    original = instance.guardLabel
    instance.guardLabel = original
    assert instance.guardLabel == original

@given(instance=research18::StateMachineObject_strategy)
@settings(max_examples=50)
def test_research18::statemachineobject_instantiation(instance):
    assert isinstance(instance, research18::StateMachineObject)

@given(instance=research18::StateMachineObject_strategy)
def test_research18::statemachineobject_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=research18::StateMachineObject_strategy)
def test_research18::statemachineobject_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=research18::StateMachineVariable_strategy)
@settings(max_examples=50)
def test_research18::statemachinevariable_instantiation(instance):
    assert isinstance(instance, research18::StateMachineVariable)

@given(instance=research18::Labelled_strategy)
@settings(max_examples=50)
def test_research18::labelled_instantiation(instance):
    assert isinstance(instance, research18::Labelled)

@given(instance=research18::Labelled_strategy)
def test_research18::labelled_lname_type(instance):
    assert isinstance(instance.lname, str)


@given(instance=research18::Labelled_strategy)
def test_research18::labelled_lname_setter(instance):
    original = instance.lname
    instance.lname = original
    assert instance.lname == original

@given(instance=research18::Counted_strategy)
@settings(max_examples=50)
def test_research18::counted_instantiation(instance):
    assert isinstance(instance, research18::Counted)

@given(instance=research18::Counted_strategy)
def test_research18::counted_id_type(instance):
    assert isinstance(instance.id, int)


@given(instance=research18::Counted_strategy)
def test_research18::counted_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=research18::Named_strategy)
@settings(max_examples=50)
def test_research18::named_instantiation(instance):
    assert isinstance(instance, research18::Named)

@given(instance=research18::Named_strategy)
def test_research18::named_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=research18::Named_strategy)
def test_research18::named_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=research18::PublicationStatus_strategy)
@settings(max_examples=50)
def test_research18::publicationstatus_instantiation(instance):
    assert isinstance(instance, research18::PublicationStatus)

@given(instance=research18::PublicationStatus_strategy)
def test_research18::publicationstatus_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=research18::PublicationStatus_strategy)
def test_research18::publicationstatus_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=Counted_strategy)
@settings(max_examples=50)
def test_counted_instantiation(instance):
    assert isinstance(instance, Counted)

@given(instance=research18::State_strategy)
@settings(max_examples=50)
def test_research18::state_instantiation(instance):
    assert isinstance(instance, research18::State)

@given(instance=research18::State_strategy)
def test_research18::state_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=research18::State_strategy)
def test_research18::state_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=research18::State_strategy)
def test_research18::state_id_type(instance):
    assert isinstance(instance.id, int)


@given(instance=research18::State_strategy)
def test_research18::state_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=research18::State_strategy)
def test_research18::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=research18::State_strategy)
def test_research18::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=research18::PaperKeyword_strategy)
@settings(max_examples=50)
def test_research18::paperkeyword_instantiation(instance):
    assert isinstance(instance, research18::PaperKeyword)

@given(instance=research18::PaperKeyword_strategy)
def test_research18::paperkeyword_weight_type(instance):
    assert isinstance(instance.weight, int)


@given(instance=research18::PaperKeyword_strategy)
def test_research18::paperkeyword_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=Labelled_strategy)
@settings(max_examples=50)
def test_labelled_instantiation(instance):
    assert isinstance(instance, Labelled)

@given(instance=research18::Write_strategy)
@settings(max_examples=50)
def test_research18::write_instantiation(instance):
    assert isinstance(instance, research18::Write)

@given(instance=research18::Write_strategy)
def test_research18::write_timeSpent_type(instance):
    assert isinstance(instance.timeSpent, int)


@given(instance=research18::Write_strategy)
def test_research18::write_timeSpent_setter(instance):
    original = instance.timeSpent
    instance.timeSpent = original
    assert instance.timeSpent == original

@given(instance=research18::Researcher_strategy)
@settings(max_examples=50)
def test_research18::researcher_instantiation(instance):
    assert isinstance(instance, research18::Researcher)

@given(instance=research18::Researcher_strategy)
def test_research18::researcher_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=research18::Researcher_strategy)
def test_research18::researcher_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=research18::Researcher_strategy)
def test_research18::researcher_forName_type(instance):
    assert isinstance(instance.forName, str)


@given(instance=research18::Researcher_strategy)
def test_research18::researcher_forName_setter(instance):
    original = instance.forName
    instance.forName = original
    assert instance.forName == original

@given(instance=research18::Phase_strategy)
@settings(max_examples=50)
def test_research18::phase_instantiation(instance):
    assert isinstance(instance, research18::Phase)

@given(instance=research18::Phase_strategy)
def test_research18::phase_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=research18::Phase_strategy)
def test_research18::phase_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=research18::Progress_strategy)
@settings(max_examples=50)
def test_research18::progress_instantiation(instance):
    assert isinstance(instance, research18::Progress)

@given(instance=research18::Progress_strategy)
def test_research18::progress_percent_type(instance):
    assert isinstance(instance.percent, int)


@given(instance=research18::Progress_strategy)
def test_research18::progress_percent_setter(instance):
    original = instance.percent
    instance.percent = original
    assert instance.percent == original

@given(instance=research18::Collaboration_strategy)
@settings(max_examples=50)
def test_research18::collaboration_instantiation(instance):
    assert isinstance(instance, research18::Collaboration)

@given(instance=research18::Collaboration_strategy)
def test_research18::collaboration_ratio_type(instance):
    assert isinstance(instance.ratio, int)


@given(instance=research18::Collaboration_strategy)
def test_research18::collaboration_ratio_setter(instance):
    original = instance.ratio
    instance.ratio = original
    assert instance.ratio == original

@given(instance=research18::Skill_strategy)
@settings(max_examples=50)
def test_research18::skill_instantiation(instance):
    assert isinstance(instance, research18::Skill)

@given(instance=research18::Skill_strategy)
def test_research18::skill_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=research18::Skill_strategy)
def test_research18::skill_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=research18::Review_strategy)
@settings(max_examples=50)
def test_research18::review_instantiation(instance):
    assert isinstance(instance, research18::Review)

@given(instance=research18::Review_strategy)
def test_research18::review_date_type(instance):
    assert isinstance(instance.date, date)


@given(instance=research18::Review_strategy)
def test_research18::review_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original

@given(instance=Named_strategy)
@settings(max_examples=50)
def test_named_instantiation(instance):
    assert isinstance(instance, Named)

@given(instance=research18::Paragraph_strategy)
@settings(max_examples=50)
def test_research18::paragraph_instantiation(instance):
    assert isinstance(instance, research18::Paragraph)

@given(instance=research18::Paragraph_strategy)
def test_research18::paragraph_content_type(instance):
    assert isinstance(instance.content, str)


@given(instance=research18::Paragraph_strategy)
def test_research18::paragraph_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original

@given(instance=research18::Keyword_strategy)
@settings(max_examples=50)
def test_research18::keyword_instantiation(instance):
    assert isinstance(instance, research18::Keyword)

@given(instance=research18::Keyword_strategy)
def test_research18::keyword_word_type(instance):
    assert isinstance(instance.word, str)


@given(instance=research18::Keyword_strategy)
def test_research18::keyword_word_setter(instance):
    original = instance.word
    instance.word = original
    assert instance.word == original

@given(instance=research18::PublicationSystem_strategy)
@settings(max_examples=50)
def test_research18::publicationsystem_instantiation(instance):
    assert isinstance(instance, research18::PublicationSystem)

@given(instance=research18::PublicationStructure_strategy)
@settings(max_examples=50)
def test_research18::publicationstructure_instantiation(instance):
    assert isinstance(instance, research18::PublicationStructure)

@given(instance=research18::KnowledgeManager_strategy)
@settings(max_examples=50)
def test_research18::knowledgemanager_instantiation(instance):
    assert isinstance(instance, research18::KnowledgeManager)

@given(instance=research18::Paper_strategy)
@settings(max_examples=50)
def test_research18::paper_instantiation(instance):
    assert isinstance(instance, research18::Paper)

@given(instance=research18::Position_strategy)
@settings(max_examples=50)
def test_research18::position_instantiation(instance):
    assert isinstance(instance, research18::Position)

@given(instance=research18::Position_strategy)
def test_research18::position_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=research18::Position_strategy)
def test_research18::position_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=research18::ReviewNote_strategy)
@settings(max_examples=50)
def test_research18::reviewnote_instantiation(instance):
    assert isinstance(instance, research18::ReviewNote)

@given(instance=research18::ReviewNote_strategy)
def test_research18::reviewnote_content_type(instance):
    assert isinstance(instance.content, str)


@given(instance=research18::ReviewNote_strategy)
def test_research18::reviewnote_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original

@given(instance=research18::PublicationProcess_strategy)
@settings(max_examples=50)
def test_research18::publicationprocess_instantiation(instance):
    assert isinstance(instance, research18::PublicationProcess)

@given(instance=research18::PublicationProcess_strategy)
def test_research18::publicationprocess_minTime_type(instance):
    assert isinstance(instance.minTime, int)


@given(instance=research18::PublicationProcess_strategy)
def test_research18::publicationprocess_minTime_setter(instance):
    original = instance.minTime
    instance.minTime = original
    assert instance.minTime == original

@given(instance=research18::PublicationProcess_strategy)
def test_research18::publicationprocess_maxTime_type(instance):
    assert isinstance(instance.maxTime, int)


@given(instance=research18::PublicationProcess_strategy)
def test_research18::publicationprocess_maxTime_setter(instance):
    original = instance.maxTime
    instance.maxTime = original
    assert instance.maxTime == original
