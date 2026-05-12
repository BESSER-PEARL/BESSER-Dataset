import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    research18_Action,
    StateMachineObject,
    research18_Transition,
    research18_StateMachineObject,
    research18_StateMachineVariable,
    research18_Labelled,
    research18_Counted,
    research18_Named,
    research18_PublicationStatus,
    Counted,
    research18_State,
    research18_PaperKeyword,
    Labelled,
    research18_Write,
    research18_Researcher,
    research18_Phase,
    research18_Progress,
    research18_Collaboration,
    research18_Skill,
    research18_Review,
    Named,
    research18_ReviewNote,
    research18_PublicationSystem,
    research18_KnowledgeManager,
    research18_PublicationStructure,
    research18_Position,
    research18_Paragraph,
    research18_Keyword,
    research18_Paper,
    research18_PublicationProcess,
    StateType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_research18_action_is_not_abstract():
    assert not inspect.isabstract(research18_Action)


def test_research18_action_constructor_exists():
    assert callable(research18_Action.__init__)


def test_research18_action_constructor_args():
    sig = inspect.signature(research18_Action.__init__)
    params = list(sig.parameters.keys())
    assert "actionLabel" in params, "Missing parameter 'actionLabel'"
    assert "actionStatement" in params, "Missing parameter 'actionStatement'"

def test_research18_action_has_actionLabel():
    assert hasattr(research18_Action, "actionLabel")
    descriptor = None
    for klass in research18_Action.__mro__:
        if "actionLabel" in klass.__dict__:
            descriptor = klass.__dict__["actionLabel"]
            break
    assert isinstance(descriptor, property)

def test_research18_action_has_actionStatement():
    assert hasattr(research18_Action, "actionStatement")
    descriptor = None
    for klass in research18_Action.__mro__:
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



def test_research18_transition_is_not_abstract():
    assert not inspect.isabstract(research18_Transition)


def test_research18_transition_constructor_exists():
    assert callable(research18_Transition.__init__)


def test_research18_transition_constructor_args():
    sig = inspect.signature(research18_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "guardExpression" in params, "Missing parameter 'guardExpression'"
    assert "guardLabel" in params, "Missing parameter 'guardLabel'"

def test_research18_transition_has_guardExpression():
    assert hasattr(research18_Transition, "guardExpression")
    descriptor = None
    for klass in research18_Transition.__mro__:
        if "guardExpression" in klass.__dict__:
            descriptor = klass.__dict__["guardExpression"]
            break
    assert isinstance(descriptor, property)

def test_research18_transition_has_guardLabel():
    assert hasattr(research18_Transition, "guardLabel")
    descriptor = None
    for klass in research18_Transition.__mro__:
        if "guardLabel" in klass.__dict__:
            descriptor = klass.__dict__["guardLabel"]
            break
    assert isinstance(descriptor, property)



def test_research18_statemachineobject_is_not_abstract():
    assert not inspect.isabstract(research18_StateMachineObject)


def test_research18_statemachineobject_constructor_exists():
    assert callable(research18_StateMachineObject.__init__)


def test_research18_statemachineobject_constructor_args():
    sig = inspect.signature(research18_StateMachineObject.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_research18_statemachineobject_has_label():
    assert hasattr(research18_StateMachineObject, "label")
    descriptor = None
    for klass in research18_StateMachineObject.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_research18_statemachinevariable_is_not_abstract():
    assert not inspect.isabstract(research18_StateMachineVariable)


def test_research18_statemachinevariable_constructor_exists():
    assert callable(research18_StateMachineVariable.__init__)


def test_research18_statemachinevariable_constructor_args():
    sig = inspect.signature(research18_StateMachineVariable.__init__)
    params = list(sig.parameters.keys())



def test_research18_labelled_is_not_abstract():
    assert not inspect.isabstract(research18_Labelled)


def test_research18_labelled_constructor_exists():
    assert callable(research18_Labelled.__init__)


def test_research18_labelled_constructor_args():
    sig = inspect.signature(research18_Labelled.__init__)
    params = list(sig.parameters.keys())
    assert "lname" in params, "Missing parameter 'lname'"

def test_research18_labelled_has_lname():
    assert hasattr(research18_Labelled, "lname")
    descriptor = None
    for klass in research18_Labelled.__mro__:
        if "lname" in klass.__dict__:
            descriptor = klass.__dict__["lname"]
            break
    assert isinstance(descriptor, property)



def test_research18_counted_is_not_abstract():
    assert not inspect.isabstract(research18_Counted)


def test_research18_counted_constructor_exists():
    assert callable(research18_Counted.__init__)


def test_research18_counted_constructor_args():
    sig = inspect.signature(research18_Counted.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_research18_counted_has_id():
    assert hasattr(research18_Counted, "id")
    descriptor = None
    for klass in research18_Counted.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_research18_named_is_not_abstract():
    assert not inspect.isabstract(research18_Named)


def test_research18_named_constructor_exists():
    assert callable(research18_Named.__init__)


def test_research18_named_constructor_args():
    sig = inspect.signature(research18_Named.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_research18_named_has_name():
    assert hasattr(research18_Named, "name")
    descriptor = None
    for klass in research18_Named.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_research18_publicationstatus_is_not_abstract():
    assert not inspect.isabstract(research18_PublicationStatus)


def test_research18_publicationstatus_constructor_exists():
    assert callable(research18_PublicationStatus.__init__)


def test_research18_publicationstatus_constructor_args():
    sig = inspect.signature(research18_PublicationStatus.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_research18_publicationstatus_has_label():
    assert hasattr(research18_PublicationStatus, "label")
    descriptor = None
    for klass in research18_PublicationStatus.__mro__:
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



def test_research18_state_is_not_abstract():
    assert not inspect.isabstract(research18_State)


def test_research18_state_constructor_exists():
    assert callable(research18_State.__init__)


def test_research18_state_constructor_args():
    sig = inspect.signature(research18_State.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"

def test_research18_state_has_kind():
    assert hasattr(research18_State, "kind")
    descriptor = None
    for klass in research18_State.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)

def test_research18_state_has_id():
    assert hasattr(research18_State, "id")
    descriptor = None
    for klass in research18_State.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_research18_state_has_name():
    assert hasattr(research18_State, "name")
    descriptor = None
    for klass in research18_State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_research18_paperkeyword_is_not_abstract():
    assert not inspect.isabstract(research18_PaperKeyword)


def test_research18_paperkeyword_constructor_exists():
    assert callable(research18_PaperKeyword.__init__)


def test_research18_paperkeyword_constructor_args():
    sig = inspect.signature(research18_PaperKeyword.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"

def test_research18_paperkeyword_has_weight():
    assert hasattr(research18_PaperKeyword, "weight")
    descriptor = None
    for klass in research18_PaperKeyword.__mro__:
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



def test_research18_write_is_not_abstract():
    assert not inspect.isabstract(research18_Write)


def test_research18_write_constructor_exists():
    assert callable(research18_Write.__init__)


def test_research18_write_constructor_args():
    sig = inspect.signature(research18_Write.__init__)
    params = list(sig.parameters.keys())
    assert "timeSpent" in params, "Missing parameter 'timeSpent'"

def test_research18_write_has_timeSpent():
    assert hasattr(research18_Write, "timeSpent")
    descriptor = None
    for klass in research18_Write.__mro__:
        if "timeSpent" in klass.__dict__:
            descriptor = klass.__dict__["timeSpent"]
            break
    assert isinstance(descriptor, property)



def test_research18_researcher_is_not_abstract():
    assert not inspect.isabstract(research18_Researcher)


def test_research18_researcher_constructor_exists():
    assert callable(research18_Researcher.__init__)


def test_research18_researcher_constructor_args():
    sig = inspect.signature(research18_Researcher.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "forName" in params, "Missing parameter 'forName'"

def test_research18_researcher_has_name():
    assert hasattr(research18_Researcher, "name")
    descriptor = None
    for klass in research18_Researcher.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_research18_researcher_has_forName():
    assert hasattr(research18_Researcher, "forName")
    descriptor = None
    for klass in research18_Researcher.__mro__:
        if "forName" in klass.__dict__:
            descriptor = klass.__dict__["forName"]
            break
    assert isinstance(descriptor, property)



def test_research18_phase_is_not_abstract():
    assert not inspect.isabstract(research18_Phase)


def test_research18_phase_constructor_exists():
    assert callable(research18_Phase.__init__)


def test_research18_phase_constructor_args():
    sig = inspect.signature(research18_Phase.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_research18_phase_has_name():
    assert hasattr(research18_Phase, "name")
    descriptor = None
    for klass in research18_Phase.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_research18_progress_is_not_abstract():
    assert not inspect.isabstract(research18_Progress)


def test_research18_progress_constructor_exists():
    assert callable(research18_Progress.__init__)


def test_research18_progress_constructor_args():
    sig = inspect.signature(research18_Progress.__init__)
    params = list(sig.parameters.keys())
    assert "percent" in params, "Missing parameter 'percent'"

def test_research18_progress_has_percent():
    assert hasattr(research18_Progress, "percent")
    descriptor = None
    for klass in research18_Progress.__mro__:
        if "percent" in klass.__dict__:
            descriptor = klass.__dict__["percent"]
            break
    assert isinstance(descriptor, property)



def test_research18_collaboration_is_not_abstract():
    assert not inspect.isabstract(research18_Collaboration)


def test_research18_collaboration_constructor_exists():
    assert callable(research18_Collaboration.__init__)


def test_research18_collaboration_constructor_args():
    sig = inspect.signature(research18_Collaboration.__init__)
    params = list(sig.parameters.keys())
    assert "ratio" in params, "Missing parameter 'ratio'"

def test_research18_collaboration_has_ratio():
    assert hasattr(research18_Collaboration, "ratio")
    descriptor = None
    for klass in research18_Collaboration.__mro__:
        if "ratio" in klass.__dict__:
            descriptor = klass.__dict__["ratio"]
            break
    assert isinstance(descriptor, property)



def test_research18_skill_is_not_abstract():
    assert not inspect.isabstract(research18_Skill)


def test_research18_skill_constructor_exists():
    assert callable(research18_Skill.__init__)


def test_research18_skill_constructor_args():
    sig = inspect.signature(research18_Skill.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"

def test_research18_skill_has_description():
    assert hasattr(research18_Skill, "description")
    descriptor = None
    for klass in research18_Skill.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_research18_review_is_not_abstract():
    assert not inspect.isabstract(research18_Review)


def test_research18_review_constructor_exists():
    assert callable(research18_Review.__init__)


def test_research18_review_constructor_args():
    sig = inspect.signature(research18_Review.__init__)
    params = list(sig.parameters.keys())
    assert "date" in params, "Missing parameter 'date'"

def test_research18_review_has_date():
    assert hasattr(research18_Review, "date")
    descriptor = None
    for klass in research18_Review.__mro__:
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



def test_research18_reviewnote_is_not_abstract():
    assert not inspect.isabstract(research18_ReviewNote)


def test_research18_reviewnote_constructor_exists():
    assert callable(research18_ReviewNote.__init__)


def test_research18_reviewnote_constructor_args():
    sig = inspect.signature(research18_ReviewNote.__init__)
    params = list(sig.parameters.keys())
    assert "content" in params, "Missing parameter 'content'"

def test_research18_reviewnote_has_content():
    assert hasattr(research18_ReviewNote, "content")
    descriptor = None
    for klass in research18_ReviewNote.__mro__:
        if "content" in klass.__dict__:
            descriptor = klass.__dict__["content"]
            break
    assert isinstance(descriptor, property)



def test_research18_publicationsystem_is_not_abstract():
    assert not inspect.isabstract(research18_PublicationSystem)


def test_research18_publicationsystem_constructor_exists():
    assert callable(research18_PublicationSystem.__init__)


def test_research18_publicationsystem_constructor_args():
    sig = inspect.signature(research18_PublicationSystem.__init__)
    params = list(sig.parameters.keys())



def test_research18_knowledgemanager_is_not_abstract():
    assert not inspect.isabstract(research18_KnowledgeManager)


def test_research18_knowledgemanager_constructor_exists():
    assert callable(research18_KnowledgeManager.__init__)


def test_research18_knowledgemanager_constructor_args():
    sig = inspect.signature(research18_KnowledgeManager.__init__)
    params = list(sig.parameters.keys())



def test_research18_publicationstructure_is_not_abstract():
    assert not inspect.isabstract(research18_PublicationStructure)


def test_research18_publicationstructure_constructor_exists():
    assert callable(research18_PublicationStructure.__init__)


def test_research18_publicationstructure_constructor_args():
    sig = inspect.signature(research18_PublicationStructure.__init__)
    params = list(sig.parameters.keys())



def test_research18_position_is_not_abstract():
    assert not inspect.isabstract(research18_Position)


def test_research18_position_constructor_exists():
    assert callable(research18_Position.__init__)


def test_research18_position_constructor_args():
    sig = inspect.signature(research18_Position.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"

def test_research18_position_has_description():
    assert hasattr(research18_Position, "description")
    descriptor = None
    for klass in research18_Position.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_research18_paragraph_is_not_abstract():
    assert not inspect.isabstract(research18_Paragraph)


def test_research18_paragraph_constructor_exists():
    assert callable(research18_Paragraph.__init__)


def test_research18_paragraph_constructor_args():
    sig = inspect.signature(research18_Paragraph.__init__)
    params = list(sig.parameters.keys())
    assert "content" in params, "Missing parameter 'content'"

def test_research18_paragraph_has_content():
    assert hasattr(research18_Paragraph, "content")
    descriptor = None
    for klass in research18_Paragraph.__mro__:
        if "content" in klass.__dict__:
            descriptor = klass.__dict__["content"]
            break
    assert isinstance(descriptor, property)



def test_research18_keyword_is_not_abstract():
    assert not inspect.isabstract(research18_Keyword)


def test_research18_keyword_constructor_exists():
    assert callable(research18_Keyword.__init__)


def test_research18_keyword_constructor_args():
    sig = inspect.signature(research18_Keyword.__init__)
    params = list(sig.parameters.keys())
    assert "word" in params, "Missing parameter 'word'"

def test_research18_keyword_has_word():
    assert hasattr(research18_Keyword, "word")
    descriptor = None
    for klass in research18_Keyword.__mro__:
        if "word" in klass.__dict__:
            descriptor = klass.__dict__["word"]
            break
    assert isinstance(descriptor, property)



def test_research18_paper_is_not_abstract():
    assert not inspect.isabstract(research18_Paper)


def test_research18_paper_constructor_exists():
    assert callable(research18_Paper.__init__)


def test_research18_paper_constructor_args():
    sig = inspect.signature(research18_Paper.__init__)
    params = list(sig.parameters.keys())



def test_research18_publicationprocess_is_not_abstract():
    assert not inspect.isabstract(research18_PublicationProcess)


def test_research18_publicationprocess_constructor_exists():
    assert callable(research18_PublicationProcess.__init__)


def test_research18_publicationprocess_constructor_args():
    sig = inspect.signature(research18_PublicationProcess.__init__)
    params = list(sig.parameters.keys())
    assert "minTime" in params, "Missing parameter 'minTime'"
    assert "maxTime" in params, "Missing parameter 'maxTime'"

def test_research18_publicationprocess_has_minTime():
    assert hasattr(research18_PublicationProcess, "minTime")
    descriptor = None
    for klass in research18_PublicationProcess.__mro__:
        if "minTime" in klass.__dict__:
            descriptor = klass.__dict__["minTime"]
            break
    assert isinstance(descriptor, property)

def test_research18_publicationprocess_has_maxTime():
    assert hasattr(research18_PublicationProcess, "maxTime")
    descriptor = None
    for klass in research18_PublicationProcess.__mro__:
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
        "initial",
        "final",
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
research18_Action_strategy = st.builds(
    research18_Action,
    actionLabel=
        safe_text,
    actionStatement=
        safe_text
)
StateMachineObject_strategy = st.builds(
    StateMachineObject,
)
research18_Transition_strategy = st.builds(
    research18_Transition,
    guardExpression=
        safe_text,
    guardLabel=
        safe_text
)
research18_StateMachineObject_strategy = st.builds(
    research18_StateMachineObject,
    label=
        safe_text
)
research18_StateMachineVariable_strategy = st.builds(
    research18_StateMachineVariable,
)
research18_Labelled_strategy = st.builds(
    research18_Labelled,
    lname=
        safe_text
)
research18_Counted_strategy = st.builds(
    research18_Counted,
    id=
        st.integers()
)
research18_Named_strategy = st.builds(
    research18_Named,
    name=
        safe_text
)
research18_PublicationStatus_strategy = st.builds(
    research18_PublicationStatus,
    label=
        safe_text
)
Counted_strategy = st.builds(
    Counted,
)
research18_State_strategy = st.builds(
    research18_State,
    kind=
        safe_text,
    id=
        st.integers(),
    name=
        safe_text
)
research18_PaperKeyword_strategy = st.builds(
    research18_PaperKeyword,
    weight=
        st.integers()
)
Labelled_strategy = st.builds(
    Labelled,
)
research18_Write_strategy = st.builds(
    research18_Write,
    timeSpent=
        st.integers()
)
research18_Researcher_strategy = st.builds(
    research18_Researcher,
    name=
        safe_text,
    forName=
        safe_text
)
research18_Phase_strategy = st.builds(
    research18_Phase,
    name=
        safe_text
)
research18_Progress_strategy = st.builds(
    research18_Progress,
    percent=
        st.integers()
)
research18_Collaboration_strategy = st.builds(
    research18_Collaboration,
    ratio=
        st.integers()
)
research18_Skill_strategy = st.builds(
    research18_Skill,
    description=
        safe_text
)
research18_Review_strategy = st.builds(
    research18_Review,
    date=
        st.dates()
)
Named_strategy = st.builds(
    Named,
)
research18_ReviewNote_strategy = st.builds(
    research18_ReviewNote,
    content=
        safe_text
)
research18_PublicationSystem_strategy = st.builds(
    research18_PublicationSystem,
)
research18_KnowledgeManager_strategy = st.builds(
    research18_KnowledgeManager,
)
research18_PublicationStructure_strategy = st.builds(
    research18_PublicationStructure,
)
research18_Position_strategy = st.builds(
    research18_Position,
    description=
        safe_text
)
research18_Paragraph_strategy = st.builds(
    research18_Paragraph,
    content=
        safe_text
)
research18_Keyword_strategy = st.builds(
    research18_Keyword,
    word=
        safe_text
)
research18_Paper_strategy = st.builds(
    research18_Paper,
)
research18_PublicationProcess_strategy = st.builds(
    research18_PublicationProcess,
    minTime=
        st.integers(),
    maxTime=
        st.integers()
)

@given(instance=research18_Action_strategy)
@settings(max_examples=50)
def test_research18_action_instantiation(instance):
    assert isinstance(instance, research18_Action)



@given(instance=research18_Action_strategy)
def test_research18_action_actionLabel_setter(instance):
    original = instance.actionLabel
    instance.actionLabel = original
    assert instance.actionLabel == original



@given(instance=research18_Action_strategy)
def test_research18_action_actionStatement_setter(instance):
    original = instance.actionStatement
    instance.actionStatement = original
    assert instance.actionStatement == original

@given(instance=StateMachineObject_strategy)
@settings(max_examples=50)
def test_statemachineobject_instantiation(instance):
    assert isinstance(instance, StateMachineObject)

@given(instance=research18_Transition_strategy)
@settings(max_examples=50)
def test_research18_transition_instantiation(instance):
    assert isinstance(instance, research18_Transition)



@given(instance=research18_Transition_strategy)
def test_research18_transition_guardExpression_setter(instance):
    original = instance.guardExpression
    instance.guardExpression = original
    assert instance.guardExpression == original



@given(instance=research18_Transition_strategy)
def test_research18_transition_guardLabel_setter(instance):
    original = instance.guardLabel
    instance.guardLabel = original
    assert instance.guardLabel == original

@given(instance=research18_StateMachineObject_strategy)
@settings(max_examples=50)
def test_research18_statemachineobject_instantiation(instance):
    assert isinstance(instance, research18_StateMachineObject)



@given(instance=research18_StateMachineObject_strategy)
def test_research18_statemachineobject_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=research18_StateMachineVariable_strategy)
@settings(max_examples=50)
def test_research18_statemachinevariable_instantiation(instance):
    assert isinstance(instance, research18_StateMachineVariable)

@given(instance=research18_Labelled_strategy)
@settings(max_examples=50)
def test_research18_labelled_instantiation(instance):
    assert isinstance(instance, research18_Labelled)



@given(instance=research18_Labelled_strategy)
def test_research18_labelled_lname_setter(instance):
    original = instance.lname
    instance.lname = original
    assert instance.lname == original

@given(instance=research18_Counted_strategy)
@settings(max_examples=50)
def test_research18_counted_instantiation(instance):
    assert isinstance(instance, research18_Counted)



@given(instance=research18_Counted_strategy)
def test_research18_counted_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=research18_Named_strategy)
@settings(max_examples=50)
def test_research18_named_instantiation(instance):
    assert isinstance(instance, research18_Named)



@given(instance=research18_Named_strategy)
def test_research18_named_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=research18_PublicationStatus_strategy)
@settings(max_examples=50)
def test_research18_publicationstatus_instantiation(instance):
    assert isinstance(instance, research18_PublicationStatus)



@given(instance=research18_PublicationStatus_strategy)
def test_research18_publicationstatus_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=Counted_strategy)
@settings(max_examples=50)
def test_counted_instantiation(instance):
    assert isinstance(instance, Counted)

@given(instance=research18_State_strategy)
@settings(max_examples=50)
def test_research18_state_instantiation(instance):
    assert isinstance(instance, research18_State)



@given(instance=research18_State_strategy)
def test_research18_state_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original



@given(instance=research18_State_strategy)
def test_research18_state_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=research18_State_strategy)
def test_research18_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=research18_PaperKeyword_strategy)
@settings(max_examples=50)
def test_research18_paperkeyword_instantiation(instance):
    assert isinstance(instance, research18_PaperKeyword)



@given(instance=research18_PaperKeyword_strategy)
def test_research18_paperkeyword_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=Labelled_strategy)
@settings(max_examples=50)
def test_labelled_instantiation(instance):
    assert isinstance(instance, Labelled)

@given(instance=research18_Write_strategy)
@settings(max_examples=50)
def test_research18_write_instantiation(instance):
    assert isinstance(instance, research18_Write)



@given(instance=research18_Write_strategy)
def test_research18_write_timeSpent_setter(instance):
    original = instance.timeSpent
    instance.timeSpent = original
    assert instance.timeSpent == original

@given(instance=research18_Researcher_strategy)
@settings(max_examples=50)
def test_research18_researcher_instantiation(instance):
    assert isinstance(instance, research18_Researcher)



@given(instance=research18_Researcher_strategy)
def test_research18_researcher_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=research18_Researcher_strategy)
def test_research18_researcher_forName_setter(instance):
    original = instance.forName
    instance.forName = original
    assert instance.forName == original

@given(instance=research18_Phase_strategy)
@settings(max_examples=50)
def test_research18_phase_instantiation(instance):
    assert isinstance(instance, research18_Phase)



@given(instance=research18_Phase_strategy)
def test_research18_phase_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=research18_Progress_strategy)
@settings(max_examples=50)
def test_research18_progress_instantiation(instance):
    assert isinstance(instance, research18_Progress)



@given(instance=research18_Progress_strategy)
def test_research18_progress_percent_setter(instance):
    original = instance.percent
    instance.percent = original
    assert instance.percent == original

@given(instance=research18_Collaboration_strategy)
@settings(max_examples=50)
def test_research18_collaboration_instantiation(instance):
    assert isinstance(instance, research18_Collaboration)



@given(instance=research18_Collaboration_strategy)
def test_research18_collaboration_ratio_setter(instance):
    original = instance.ratio
    instance.ratio = original
    assert instance.ratio == original

@given(instance=research18_Skill_strategy)
@settings(max_examples=50)
def test_research18_skill_instantiation(instance):
    assert isinstance(instance, research18_Skill)



@given(instance=research18_Skill_strategy)
def test_research18_skill_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=research18_Review_strategy)
@settings(max_examples=50)
def test_research18_review_instantiation(instance):
    assert isinstance(instance, research18_Review)



@given(instance=research18_Review_strategy)
def test_research18_review_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original

@given(instance=Named_strategy)
@settings(max_examples=50)
def test_named_instantiation(instance):
    assert isinstance(instance, Named)

@given(instance=research18_ReviewNote_strategy)
@settings(max_examples=50)
def test_research18_reviewnote_instantiation(instance):
    assert isinstance(instance, research18_ReviewNote)



@given(instance=research18_ReviewNote_strategy)
def test_research18_reviewnote_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original

@given(instance=research18_PublicationSystem_strategy)
@settings(max_examples=50)
def test_research18_publicationsystem_instantiation(instance):
    assert isinstance(instance, research18_PublicationSystem)

@given(instance=research18_KnowledgeManager_strategy)
@settings(max_examples=50)
def test_research18_knowledgemanager_instantiation(instance):
    assert isinstance(instance, research18_KnowledgeManager)

@given(instance=research18_PublicationStructure_strategy)
@settings(max_examples=50)
def test_research18_publicationstructure_instantiation(instance):
    assert isinstance(instance, research18_PublicationStructure)

@given(instance=research18_Position_strategy)
@settings(max_examples=50)
def test_research18_position_instantiation(instance):
    assert isinstance(instance, research18_Position)



@given(instance=research18_Position_strategy)
def test_research18_position_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=research18_Paragraph_strategy)
@settings(max_examples=50)
def test_research18_paragraph_instantiation(instance):
    assert isinstance(instance, research18_Paragraph)



@given(instance=research18_Paragraph_strategy)
def test_research18_paragraph_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original

@given(instance=research18_Keyword_strategy)
@settings(max_examples=50)
def test_research18_keyword_instantiation(instance):
    assert isinstance(instance, research18_Keyword)



@given(instance=research18_Keyword_strategy)
def test_research18_keyword_word_setter(instance):
    original = instance.word
    instance.word = original
    assert instance.word == original

@given(instance=research18_Paper_strategy)
@settings(max_examples=50)
def test_research18_paper_instantiation(instance):
    assert isinstance(instance, research18_Paper)

@given(instance=research18_PublicationProcess_strategy)
@settings(max_examples=50)
def test_research18_publicationprocess_instantiation(instance):
    assert isinstance(instance, research18_PublicationProcess)



@given(instance=research18_PublicationProcess_strategy)
def test_research18_publicationprocess_minTime_setter(instance):
    original = instance.minTime
    instance.minTime = original
    assert instance.minTime == original



@given(instance=research18_PublicationProcess_strategy)
def test_research18_publicationprocess_maxTime_setter(instance):
    original = instance.maxTime
    instance.maxTime = original
    assert instance.maxTime == original
