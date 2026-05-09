import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    research20::Labelled,
    StateMachineObject,
    research20::Transition,
    research20::StateMachineObject,
    research20::StateMachineVariable,
    research20::Counted,
    research20::Named,
    research20::PublicationStatus,
    research20::PaperKeyword,
    Labelled,
    research20::Progress,
    Counted,
    research20::State,
    research20::Collaboration,
    research20::Skill,
    research20::Review,
    research20::Write,
    research20::Researcher,
    research20::Phase,
    Named,
    research20::Paragraph,
    research20::PublicationStructure,
    research20::PublicationSystem,
    research20::ReviewNote,
    research20::KnowledgeManager,
    research20::Paper,
    research20::Position,
    research20::Keyword,
    research20::PublicationProcess,
    research20::Action,
    StateType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_research20::labelled_is_not_abstract():
    assert not inspect.isabstract(research20::Labelled)


def test_research20::labelled_constructor_exists():
    assert callable(research20::Labelled.__init__)


def test_research20::labelled_constructor_args():
    sig = inspect.signature(research20::Labelled.__init__)
    params = list(sig.parameters.keys())
    assert "lname" in params, "Missing parameter 'lname'"

def test_research20::labelled_has_lname():
    assert hasattr(research20::Labelled, "lname")
    descriptor = None
    for klass in research20::Labelled.__mro__:
        if "lname" in klass.__dict__:
            descriptor = klass.__dict__["lname"]
            break
    assert isinstance(descriptor, property)



def test_statemachineobject_is_not_abstract():
    assert not inspect.isabstract(StateMachineObject)


def test_statemachineobject_constructor_exists():
    assert callable(StateMachineObject.__init__)


def test_statemachineobject_constructor_args():
    sig = inspect.signature(StateMachineObject.__init__)
    params = list(sig.parameters.keys())



def test_research20::transition_is_not_abstract():
    assert not inspect.isabstract(research20::Transition)


def test_research20::transition_constructor_exists():
    assert callable(research20::Transition.__init__)


def test_research20::transition_constructor_args():
    sig = inspect.signature(research20::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "guardLabel" in params, "Missing parameter 'guardLabel'"
    assert "guardExpression" in params, "Missing parameter 'guardExpression'"

def test_research20::transition_has_guardLabel():
    assert hasattr(research20::Transition, "guardLabel")
    descriptor = None
    for klass in research20::Transition.__mro__:
        if "guardLabel" in klass.__dict__:
            descriptor = klass.__dict__["guardLabel"]
            break
    assert isinstance(descriptor, property)

def test_research20::transition_has_guardExpression():
    assert hasattr(research20::Transition, "guardExpression")
    descriptor = None
    for klass in research20::Transition.__mro__:
        if "guardExpression" in klass.__dict__:
            descriptor = klass.__dict__["guardExpression"]
            break
    assert isinstance(descriptor, property)



def test_research20::statemachineobject_is_not_abstract():
    assert not inspect.isabstract(research20::StateMachineObject)


def test_research20::statemachineobject_constructor_exists():
    assert callable(research20::StateMachineObject.__init__)


def test_research20::statemachineobject_constructor_args():
    sig = inspect.signature(research20::StateMachineObject.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_research20::statemachineobject_has_label():
    assert hasattr(research20::StateMachineObject, "label")
    descriptor = None
    for klass in research20::StateMachineObject.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_research20::statemachinevariable_is_not_abstract():
    assert not inspect.isabstract(research20::StateMachineVariable)


def test_research20::statemachinevariable_constructor_exists():
    assert callable(research20::StateMachineVariable.__init__)


def test_research20::statemachinevariable_constructor_args():
    sig = inspect.signature(research20::StateMachineVariable.__init__)
    params = list(sig.parameters.keys())



def test_research20::counted_is_not_abstract():
    assert not inspect.isabstract(research20::Counted)


def test_research20::counted_constructor_exists():
    assert callable(research20::Counted.__init__)


def test_research20::counted_constructor_args():
    sig = inspect.signature(research20::Counted.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_research20::counted_has_id():
    assert hasattr(research20::Counted, "id")
    descriptor = None
    for klass in research20::Counted.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_research20::named_is_not_abstract():
    assert not inspect.isabstract(research20::Named)


def test_research20::named_constructor_exists():
    assert callable(research20::Named.__init__)


def test_research20::named_constructor_args():
    sig = inspect.signature(research20::Named.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_research20::named_has_name():
    assert hasattr(research20::Named, "name")
    descriptor = None
    for klass in research20::Named.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_research20::publicationstatus_is_not_abstract():
    assert not inspect.isabstract(research20::PublicationStatus)


def test_research20::publicationstatus_constructor_exists():
    assert callable(research20::PublicationStatus.__init__)


def test_research20::publicationstatus_constructor_args():
    sig = inspect.signature(research20::PublicationStatus.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_research20::publicationstatus_has_label():
    assert hasattr(research20::PublicationStatus, "label")
    descriptor = None
    for klass in research20::PublicationStatus.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_research20::paperkeyword_is_not_abstract():
    assert not inspect.isabstract(research20::PaperKeyword)


def test_research20::paperkeyword_constructor_exists():
    assert callable(research20::PaperKeyword.__init__)


def test_research20::paperkeyword_constructor_args():
    sig = inspect.signature(research20::PaperKeyword.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"

def test_research20::paperkeyword_has_weight():
    assert hasattr(research20::PaperKeyword, "weight")
    descriptor = None
    for klass in research20::PaperKeyword.__mro__:
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



def test_research20::progress_is_not_abstract():
    assert not inspect.isabstract(research20::Progress)


def test_research20::progress_constructor_exists():
    assert callable(research20::Progress.__init__)


def test_research20::progress_constructor_args():
    sig = inspect.signature(research20::Progress.__init__)
    params = list(sig.parameters.keys())
    assert "percent" in params, "Missing parameter 'percent'"

def test_research20::progress_has_percent():
    assert hasattr(research20::Progress, "percent")
    descriptor = None
    for klass in research20::Progress.__mro__:
        if "percent" in klass.__dict__:
            descriptor = klass.__dict__["percent"]
            break
    assert isinstance(descriptor, property)



def test_counted_is_not_abstract():
    assert not inspect.isabstract(Counted)


def test_counted_constructor_exists():
    assert callable(Counted.__init__)


def test_counted_constructor_args():
    sig = inspect.signature(Counted.__init__)
    params = list(sig.parameters.keys())



def test_research20::state_is_not_abstract():
    assert not inspect.isabstract(research20::State)


def test_research20::state_constructor_exists():
    assert callable(research20::State.__init__)


def test_research20::state_constructor_args():
    sig = inspect.signature(research20::State.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"

def test_research20::state_has_kind():
    assert hasattr(research20::State, "kind")
    descriptor = None
    for klass in research20::State.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)

def test_research20::state_has_id():
    assert hasattr(research20::State, "id")
    descriptor = None
    for klass in research20::State.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_research20::state_has_name():
    assert hasattr(research20::State, "name")
    descriptor = None
    for klass in research20::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_research20::collaboration_is_not_abstract():
    assert not inspect.isabstract(research20::Collaboration)


def test_research20::collaboration_constructor_exists():
    assert callable(research20::Collaboration.__init__)


def test_research20::collaboration_constructor_args():
    sig = inspect.signature(research20::Collaboration.__init__)
    params = list(sig.parameters.keys())
    assert "ratio" in params, "Missing parameter 'ratio'"

def test_research20::collaboration_has_ratio():
    assert hasattr(research20::Collaboration, "ratio")
    descriptor = None
    for klass in research20::Collaboration.__mro__:
        if "ratio" in klass.__dict__:
            descriptor = klass.__dict__["ratio"]
            break
    assert isinstance(descriptor, property)



def test_research20::skill_is_not_abstract():
    assert not inspect.isabstract(research20::Skill)


def test_research20::skill_constructor_exists():
    assert callable(research20::Skill.__init__)


def test_research20::skill_constructor_args():
    sig = inspect.signature(research20::Skill.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"

def test_research20::skill_has_description():
    assert hasattr(research20::Skill, "description")
    descriptor = None
    for klass in research20::Skill.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_research20::review_is_not_abstract():
    assert not inspect.isabstract(research20::Review)


def test_research20::review_constructor_exists():
    assert callable(research20::Review.__init__)


def test_research20::review_constructor_args():
    sig = inspect.signature(research20::Review.__init__)
    params = list(sig.parameters.keys())
    assert "date" in params, "Missing parameter 'date'"

def test_research20::review_has_date():
    assert hasattr(research20::Review, "date")
    descriptor = None
    for klass in research20::Review.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)



def test_research20::write_is_not_abstract():
    assert not inspect.isabstract(research20::Write)


def test_research20::write_constructor_exists():
    assert callable(research20::Write.__init__)


def test_research20::write_constructor_args():
    sig = inspect.signature(research20::Write.__init__)
    params = list(sig.parameters.keys())
    assert "timeSpent" in params, "Missing parameter 'timeSpent'"

def test_research20::write_has_timeSpent():
    assert hasattr(research20::Write, "timeSpent")
    descriptor = None
    for klass in research20::Write.__mro__:
        if "timeSpent" in klass.__dict__:
            descriptor = klass.__dict__["timeSpent"]
            break
    assert isinstance(descriptor, property)



def test_research20::researcher_is_not_abstract():
    assert not inspect.isabstract(research20::Researcher)


def test_research20::researcher_constructor_exists():
    assert callable(research20::Researcher.__init__)


def test_research20::researcher_constructor_args():
    sig = inspect.signature(research20::Researcher.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "forName" in params, "Missing parameter 'forName'"

def test_research20::researcher_has_name():
    assert hasattr(research20::Researcher, "name")
    descriptor = None
    for klass in research20::Researcher.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_research20::researcher_has_forName():
    assert hasattr(research20::Researcher, "forName")
    descriptor = None
    for klass in research20::Researcher.__mro__:
        if "forName" in klass.__dict__:
            descriptor = klass.__dict__["forName"]
            break
    assert isinstance(descriptor, property)



def test_research20::phase_is_not_abstract():
    assert not inspect.isabstract(research20::Phase)


def test_research20::phase_constructor_exists():
    assert callable(research20::Phase.__init__)


def test_research20::phase_constructor_args():
    sig = inspect.signature(research20::Phase.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_research20::phase_has_name():
    assert hasattr(research20::Phase, "name")
    descriptor = None
    for klass in research20::Phase.__mro__:
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



def test_research20::paragraph_is_not_abstract():
    assert not inspect.isabstract(research20::Paragraph)


def test_research20::paragraph_constructor_exists():
    assert callable(research20::Paragraph.__init__)


def test_research20::paragraph_constructor_args():
    sig = inspect.signature(research20::Paragraph.__init__)
    params = list(sig.parameters.keys())
    assert "content" in params, "Missing parameter 'content'"

def test_research20::paragraph_has_content():
    assert hasattr(research20::Paragraph, "content")
    descriptor = None
    for klass in research20::Paragraph.__mro__:
        if "content" in klass.__dict__:
            descriptor = klass.__dict__["content"]
            break
    assert isinstance(descriptor, property)



def test_research20::publicationstructure_is_not_abstract():
    assert not inspect.isabstract(research20::PublicationStructure)


def test_research20::publicationstructure_constructor_exists():
    assert callable(research20::PublicationStructure.__init__)


def test_research20::publicationstructure_constructor_args():
    sig = inspect.signature(research20::PublicationStructure.__init__)
    params = list(sig.parameters.keys())



def test_research20::publicationsystem_is_not_abstract():
    assert not inspect.isabstract(research20::PublicationSystem)


def test_research20::publicationsystem_constructor_exists():
    assert callable(research20::PublicationSystem.__init__)


def test_research20::publicationsystem_constructor_args():
    sig = inspect.signature(research20::PublicationSystem.__init__)
    params = list(sig.parameters.keys())



def test_research20::reviewnote_is_not_abstract():
    assert not inspect.isabstract(research20::ReviewNote)


def test_research20::reviewnote_constructor_exists():
    assert callable(research20::ReviewNote.__init__)


def test_research20::reviewnote_constructor_args():
    sig = inspect.signature(research20::ReviewNote.__init__)
    params = list(sig.parameters.keys())
    assert "content" in params, "Missing parameter 'content'"

def test_research20::reviewnote_has_content():
    assert hasattr(research20::ReviewNote, "content")
    descriptor = None
    for klass in research20::ReviewNote.__mro__:
        if "content" in klass.__dict__:
            descriptor = klass.__dict__["content"]
            break
    assert isinstance(descriptor, property)



def test_research20::knowledgemanager_is_not_abstract():
    assert not inspect.isabstract(research20::KnowledgeManager)


def test_research20::knowledgemanager_constructor_exists():
    assert callable(research20::KnowledgeManager.__init__)


def test_research20::knowledgemanager_constructor_args():
    sig = inspect.signature(research20::KnowledgeManager.__init__)
    params = list(sig.parameters.keys())



def test_research20::paper_is_not_abstract():
    assert not inspect.isabstract(research20::Paper)


def test_research20::paper_constructor_exists():
    assert callable(research20::Paper.__init__)


def test_research20::paper_constructor_args():
    sig = inspect.signature(research20::Paper.__init__)
    params = list(sig.parameters.keys())



def test_research20::position_is_not_abstract():
    assert not inspect.isabstract(research20::Position)


def test_research20::position_constructor_exists():
    assert callable(research20::Position.__init__)


def test_research20::position_constructor_args():
    sig = inspect.signature(research20::Position.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"

def test_research20::position_has_description():
    assert hasattr(research20::Position, "description")
    descriptor = None
    for klass in research20::Position.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_research20::keyword_is_not_abstract():
    assert not inspect.isabstract(research20::Keyword)


def test_research20::keyword_constructor_exists():
    assert callable(research20::Keyword.__init__)


def test_research20::keyword_constructor_args():
    sig = inspect.signature(research20::Keyword.__init__)
    params = list(sig.parameters.keys())
    assert "word" in params, "Missing parameter 'word'"

def test_research20::keyword_has_word():
    assert hasattr(research20::Keyword, "word")
    descriptor = None
    for klass in research20::Keyword.__mro__:
        if "word" in klass.__dict__:
            descriptor = klass.__dict__["word"]
            break
    assert isinstance(descriptor, property)



def test_research20::publicationprocess_is_not_abstract():
    assert not inspect.isabstract(research20::PublicationProcess)


def test_research20::publicationprocess_constructor_exists():
    assert callable(research20::PublicationProcess.__init__)


def test_research20::publicationprocess_constructor_args():
    sig = inspect.signature(research20::PublicationProcess.__init__)
    params = list(sig.parameters.keys())
    assert "minTime" in params, "Missing parameter 'minTime'"
    assert "maxTime" in params, "Missing parameter 'maxTime'"

def test_research20::publicationprocess_has_minTime():
    assert hasattr(research20::PublicationProcess, "minTime")
    descriptor = None
    for klass in research20::PublicationProcess.__mro__:
        if "minTime" in klass.__dict__:
            descriptor = klass.__dict__["minTime"]
            break
    assert isinstance(descriptor, property)

def test_research20::publicationprocess_has_maxTime():
    assert hasattr(research20::PublicationProcess, "maxTime")
    descriptor = None
    for klass in research20::PublicationProcess.__mro__:
        if "maxTime" in klass.__dict__:
            descriptor = klass.__dict__["maxTime"]
            break
    assert isinstance(descriptor, property)



def test_research20::action_is_not_abstract():
    assert not inspect.isabstract(research20::Action)


def test_research20::action_constructor_exists():
    assert callable(research20::Action.__init__)


def test_research20::action_constructor_args():
    sig = inspect.signature(research20::Action.__init__)
    params = list(sig.parameters.keys())
    assert "actionLabel" in params, "Missing parameter 'actionLabel'"
    assert "actionStatement" in params, "Missing parameter 'actionStatement'"

def test_research20::action_has_actionLabel():
    assert hasattr(research20::Action, "actionLabel")
    descriptor = None
    for klass in research20::Action.__mro__:
        if "actionLabel" in klass.__dict__:
            descriptor = klass.__dict__["actionLabel"]
            break
    assert isinstance(descriptor, property)

def test_research20::action_has_actionStatement():
    assert hasattr(research20::Action, "actionStatement")
    descriptor = None
    for klass in research20::Action.__mro__:
        if "actionStatement" in klass.__dict__:
            descriptor = klass.__dict__["actionStatement"]
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
research20::Labelled_strategy = st.builds(
    research20::Labelled,
    lname=
        safe_text
)
StateMachineObject_strategy = st.builds(
    StateMachineObject,
)
research20::Transition_strategy = st.builds(
    research20::Transition,
    guardLabel=
        safe_text,
    guardExpression=
        safe_text
)
research20::StateMachineObject_strategy = st.builds(
    research20::StateMachineObject,
    label=
        safe_text
)
research20::StateMachineVariable_strategy = st.builds(
    research20::StateMachineVariable,
)
research20::Counted_strategy = st.builds(
    research20::Counted,
    id=
        st.integers()
)
research20::Named_strategy = st.builds(
    research20::Named,
    name=
        safe_text
)
research20::PublicationStatus_strategy = st.builds(
    research20::PublicationStatus,
    label=
        safe_text
)
research20::PaperKeyword_strategy = st.builds(
    research20::PaperKeyword,
    weight=
        st.integers()
)
Labelled_strategy = st.builds(
    Labelled,
)
research20::Progress_strategy = st.builds(
    research20::Progress,
    percent=
        st.integers()
)
Counted_strategy = st.builds(
    Counted,
)
research20::State_strategy = st.builds(
    research20::State,
    kind=
        safe_text,
    id=
        st.integers(),
    name=
        safe_text
)
research20::Collaboration_strategy = st.builds(
    research20::Collaboration,
    ratio=
        st.integers()
)
research20::Skill_strategy = st.builds(
    research20::Skill,
    description=
        safe_text
)
research20::Review_strategy = st.builds(
    research20::Review,
    date=
        st.dates()
)
research20::Write_strategy = st.builds(
    research20::Write,
    timeSpent=
        st.integers()
)
research20::Researcher_strategy = st.builds(
    research20::Researcher,
    name=
        safe_text,
    forName=
        safe_text
)
research20::Phase_strategy = st.builds(
    research20::Phase,
    name=
        safe_text
)
Named_strategy = st.builds(
    Named,
)
research20::Paragraph_strategy = st.builds(
    research20::Paragraph,
    content=
        safe_text
)
research20::PublicationStructure_strategy = st.builds(
    research20::PublicationStructure,
)
research20::PublicationSystem_strategy = st.builds(
    research20::PublicationSystem,
)
research20::ReviewNote_strategy = st.builds(
    research20::ReviewNote,
    content=
        safe_text
)
research20::KnowledgeManager_strategy = st.builds(
    research20::KnowledgeManager,
)
research20::Paper_strategy = st.builds(
    research20::Paper,
)
research20::Position_strategy = st.builds(
    research20::Position,
    description=
        safe_text
)
research20::Keyword_strategy = st.builds(
    research20::Keyword,
    word=
        safe_text
)
research20::PublicationProcess_strategy = st.builds(
    research20::PublicationProcess,
    minTime=
        st.integers(),
    maxTime=
        st.integers()
)
research20::Action_strategy = st.builds(
    research20::Action,
    actionLabel=
        safe_text,
    actionStatement=
        safe_text
)

@given(instance=research20::Labelled_strategy)
@settings(max_examples=50)
def test_research20::labelled_instantiation(instance):
    assert isinstance(instance, research20::Labelled)

@given(instance=research20::Labelled_strategy)
def test_research20::labelled_lname_type(instance):
    assert isinstance(instance.lname, str)


@given(instance=research20::Labelled_strategy)
def test_research20::labelled_lname_setter(instance):
    original = instance.lname
    instance.lname = original
    assert instance.lname == original

@given(instance=StateMachineObject_strategy)
@settings(max_examples=50)
def test_statemachineobject_instantiation(instance):
    assert isinstance(instance, StateMachineObject)

@given(instance=research20::Transition_strategy)
@settings(max_examples=50)
def test_research20::transition_instantiation(instance):
    assert isinstance(instance, research20::Transition)

@given(instance=research20::Transition_strategy)
def test_research20::transition_guardLabel_type(instance):
    assert isinstance(instance.guardLabel, str)


@given(instance=research20::Transition_strategy)
def test_research20::transition_guardLabel_setter(instance):
    original = instance.guardLabel
    instance.guardLabel = original
    assert instance.guardLabel == original

@given(instance=research20::Transition_strategy)
def test_research20::transition_guardExpression_type(instance):
    assert isinstance(instance.guardExpression, str)


@given(instance=research20::Transition_strategy)
def test_research20::transition_guardExpression_setter(instance):
    original = instance.guardExpression
    instance.guardExpression = original
    assert instance.guardExpression == original

@given(instance=research20::StateMachineObject_strategy)
@settings(max_examples=50)
def test_research20::statemachineobject_instantiation(instance):
    assert isinstance(instance, research20::StateMachineObject)

@given(instance=research20::StateMachineObject_strategy)
def test_research20::statemachineobject_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=research20::StateMachineObject_strategy)
def test_research20::statemachineobject_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=research20::StateMachineVariable_strategy)
@settings(max_examples=50)
def test_research20::statemachinevariable_instantiation(instance):
    assert isinstance(instance, research20::StateMachineVariable)

@given(instance=research20::Counted_strategy)
@settings(max_examples=50)
def test_research20::counted_instantiation(instance):
    assert isinstance(instance, research20::Counted)

@given(instance=research20::Counted_strategy)
def test_research20::counted_id_type(instance):
    assert isinstance(instance.id, int)


@given(instance=research20::Counted_strategy)
def test_research20::counted_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=research20::Named_strategy)
@settings(max_examples=50)
def test_research20::named_instantiation(instance):
    assert isinstance(instance, research20::Named)

@given(instance=research20::Named_strategy)
def test_research20::named_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=research20::Named_strategy)
def test_research20::named_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=research20::PublicationStatus_strategy)
@settings(max_examples=50)
def test_research20::publicationstatus_instantiation(instance):
    assert isinstance(instance, research20::PublicationStatus)

@given(instance=research20::PublicationStatus_strategy)
def test_research20::publicationstatus_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=research20::PublicationStatus_strategy)
def test_research20::publicationstatus_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=research20::PaperKeyword_strategy)
@settings(max_examples=50)
def test_research20::paperkeyword_instantiation(instance):
    assert isinstance(instance, research20::PaperKeyword)

@given(instance=research20::PaperKeyword_strategy)
def test_research20::paperkeyword_weight_type(instance):
    assert isinstance(instance.weight, int)


@given(instance=research20::PaperKeyword_strategy)
def test_research20::paperkeyword_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=Labelled_strategy)
@settings(max_examples=50)
def test_labelled_instantiation(instance):
    assert isinstance(instance, Labelled)

@given(instance=research20::Progress_strategy)
@settings(max_examples=50)
def test_research20::progress_instantiation(instance):
    assert isinstance(instance, research20::Progress)

@given(instance=research20::Progress_strategy)
def test_research20::progress_percent_type(instance):
    assert isinstance(instance.percent, int)


@given(instance=research20::Progress_strategy)
def test_research20::progress_percent_setter(instance):
    original = instance.percent
    instance.percent = original
    assert instance.percent == original

@given(instance=Counted_strategy)
@settings(max_examples=50)
def test_counted_instantiation(instance):
    assert isinstance(instance, Counted)

@given(instance=research20::State_strategy)
@settings(max_examples=50)
def test_research20::state_instantiation(instance):
    assert isinstance(instance, research20::State)

@given(instance=research20::State_strategy)
def test_research20::state_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=research20::State_strategy)
def test_research20::state_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=research20::State_strategy)
def test_research20::state_id_type(instance):
    assert isinstance(instance.id, int)


@given(instance=research20::State_strategy)
def test_research20::state_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=research20::State_strategy)
def test_research20::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=research20::State_strategy)
def test_research20::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=research20::Collaboration_strategy)
@settings(max_examples=50)
def test_research20::collaboration_instantiation(instance):
    assert isinstance(instance, research20::Collaboration)

@given(instance=research20::Collaboration_strategy)
def test_research20::collaboration_ratio_type(instance):
    assert isinstance(instance.ratio, int)


@given(instance=research20::Collaboration_strategy)
def test_research20::collaboration_ratio_setter(instance):
    original = instance.ratio
    instance.ratio = original
    assert instance.ratio == original

@given(instance=research20::Skill_strategy)
@settings(max_examples=50)
def test_research20::skill_instantiation(instance):
    assert isinstance(instance, research20::Skill)

@given(instance=research20::Skill_strategy)
def test_research20::skill_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=research20::Skill_strategy)
def test_research20::skill_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=research20::Review_strategy)
@settings(max_examples=50)
def test_research20::review_instantiation(instance):
    assert isinstance(instance, research20::Review)

@given(instance=research20::Review_strategy)
def test_research20::review_date_type(instance):
    assert isinstance(instance.date, date)


@given(instance=research20::Review_strategy)
def test_research20::review_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original

@given(instance=research20::Write_strategy)
@settings(max_examples=50)
def test_research20::write_instantiation(instance):
    assert isinstance(instance, research20::Write)

@given(instance=research20::Write_strategy)
def test_research20::write_timeSpent_type(instance):
    assert isinstance(instance.timeSpent, int)


@given(instance=research20::Write_strategy)
def test_research20::write_timeSpent_setter(instance):
    original = instance.timeSpent
    instance.timeSpent = original
    assert instance.timeSpent == original

@given(instance=research20::Researcher_strategy)
@settings(max_examples=50)
def test_research20::researcher_instantiation(instance):
    assert isinstance(instance, research20::Researcher)

@given(instance=research20::Researcher_strategy)
def test_research20::researcher_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=research20::Researcher_strategy)
def test_research20::researcher_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=research20::Researcher_strategy)
def test_research20::researcher_forName_type(instance):
    assert isinstance(instance.forName, str)


@given(instance=research20::Researcher_strategy)
def test_research20::researcher_forName_setter(instance):
    original = instance.forName
    instance.forName = original
    assert instance.forName == original

@given(instance=research20::Phase_strategy)
@settings(max_examples=50)
def test_research20::phase_instantiation(instance):
    assert isinstance(instance, research20::Phase)

@given(instance=research20::Phase_strategy)
def test_research20::phase_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=research20::Phase_strategy)
def test_research20::phase_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Named_strategy)
@settings(max_examples=50)
def test_named_instantiation(instance):
    assert isinstance(instance, Named)

@given(instance=research20::Paragraph_strategy)
@settings(max_examples=50)
def test_research20::paragraph_instantiation(instance):
    assert isinstance(instance, research20::Paragraph)

@given(instance=research20::Paragraph_strategy)
def test_research20::paragraph_content_type(instance):
    assert isinstance(instance.content, str)


@given(instance=research20::Paragraph_strategy)
def test_research20::paragraph_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original

@given(instance=research20::PublicationStructure_strategy)
@settings(max_examples=50)
def test_research20::publicationstructure_instantiation(instance):
    assert isinstance(instance, research20::PublicationStructure)

@given(instance=research20::PublicationSystem_strategy)
@settings(max_examples=50)
def test_research20::publicationsystem_instantiation(instance):
    assert isinstance(instance, research20::PublicationSystem)

@given(instance=research20::ReviewNote_strategy)
@settings(max_examples=50)
def test_research20::reviewnote_instantiation(instance):
    assert isinstance(instance, research20::ReviewNote)

@given(instance=research20::ReviewNote_strategy)
def test_research20::reviewnote_content_type(instance):
    assert isinstance(instance.content, str)


@given(instance=research20::ReviewNote_strategy)
def test_research20::reviewnote_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original

@given(instance=research20::KnowledgeManager_strategy)
@settings(max_examples=50)
def test_research20::knowledgemanager_instantiation(instance):
    assert isinstance(instance, research20::KnowledgeManager)

@given(instance=research20::Paper_strategy)
@settings(max_examples=50)
def test_research20::paper_instantiation(instance):
    assert isinstance(instance, research20::Paper)

@given(instance=research20::Position_strategy)
@settings(max_examples=50)
def test_research20::position_instantiation(instance):
    assert isinstance(instance, research20::Position)

@given(instance=research20::Position_strategy)
def test_research20::position_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=research20::Position_strategy)
def test_research20::position_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=research20::Keyword_strategy)
@settings(max_examples=50)
def test_research20::keyword_instantiation(instance):
    assert isinstance(instance, research20::Keyword)

@given(instance=research20::Keyword_strategy)
def test_research20::keyword_word_type(instance):
    assert isinstance(instance.word, str)


@given(instance=research20::Keyword_strategy)
def test_research20::keyword_word_setter(instance):
    original = instance.word
    instance.word = original
    assert instance.word == original

@given(instance=research20::PublicationProcess_strategy)
@settings(max_examples=50)
def test_research20::publicationprocess_instantiation(instance):
    assert isinstance(instance, research20::PublicationProcess)

@given(instance=research20::PublicationProcess_strategy)
def test_research20::publicationprocess_minTime_type(instance):
    assert isinstance(instance.minTime, int)


@given(instance=research20::PublicationProcess_strategy)
def test_research20::publicationprocess_minTime_setter(instance):
    original = instance.minTime
    instance.minTime = original
    assert instance.minTime == original

@given(instance=research20::PublicationProcess_strategy)
def test_research20::publicationprocess_maxTime_type(instance):
    assert isinstance(instance.maxTime, int)


@given(instance=research20::PublicationProcess_strategy)
def test_research20::publicationprocess_maxTime_setter(instance):
    original = instance.maxTime
    instance.maxTime = original
    assert instance.maxTime == original

@given(instance=research20::Action_strategy)
@settings(max_examples=50)
def test_research20::action_instantiation(instance):
    assert isinstance(instance, research20::Action)

@given(instance=research20::Action_strategy)
def test_research20::action_actionLabel_type(instance):
    assert isinstance(instance.actionLabel, str)


@given(instance=research20::Action_strategy)
def test_research20::action_actionLabel_setter(instance):
    original = instance.actionLabel
    instance.actionLabel = original
    assert instance.actionLabel == original

@given(instance=research20::Action_strategy)
def test_research20::action_actionStatement_type(instance):
    assert isinstance(instance.actionStatement, str)


@given(instance=research20::Action_strategy)
def test_research20::action_actionStatement_setter(instance):
    original = instance.actionStatement
    instance.actionStatement = original
    assert instance.actionStatement == original
