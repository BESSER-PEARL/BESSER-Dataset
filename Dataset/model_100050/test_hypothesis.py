import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    research23_Action,
    StateMachineObject,
    research23_Transition,
    research23_Labelled,
    research23_Counted,
    research23_Named,
    research23_PublicationStatus,
    Counted,
    research23_State,
    research23_PaperKeyword,
    Labelled,
    research23_Review,
    research23_Write,
    research23_Researcher,
    research23_Phase,
    research23_Progress,
    research23_Collaboration,
    research23_Skill,
    Named,
    research23_Position,
    research23_Paper,
    research23_KnowledgeManager,
    research23_ReviewNote,
    research23_PublicationStructure,
    research23_Paragraph,
    research23_PublicationSystem,
    research23_Keyword,
    research23_PublicationProcess,
    research23_StateMachineObject,
    research23_StateMachineVariable,
    StateType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_research23_action_is_not_abstract():
    assert not inspect.isabstract(research23_Action)


def test_research23_action_constructor_exists():
    assert callable(research23_Action.__init__)


def test_research23_action_constructor_args():
    sig = inspect.signature(research23_Action.__init__)
    params = list(sig.parameters.keys())
    assert "actionLabel" in params, "Missing parameter 'actionLabel'"
    assert "actionStatement" in params, "Missing parameter 'actionStatement'"

def test_research23_action_has_actionLabel():
    assert hasattr(research23_Action, "actionLabel")
    descriptor = None
    for klass in research23_Action.__mro__:
        if "actionLabel" in klass.__dict__:
            descriptor = klass.__dict__["actionLabel"]
            break
    assert isinstance(descriptor, property)

def test_research23_action_has_actionStatement():
    assert hasattr(research23_Action, "actionStatement")
    descriptor = None
    for klass in research23_Action.__mro__:
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



def test_research23_transition_is_not_abstract():
    assert not inspect.isabstract(research23_Transition)


def test_research23_transition_constructor_exists():
    assert callable(research23_Transition.__init__)


def test_research23_transition_constructor_args():
    sig = inspect.signature(research23_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "guardLabel" in params, "Missing parameter 'guardLabel'"
    assert "guardExpression" in params, "Missing parameter 'guardExpression'"

def test_research23_transition_has_guardLabel():
    assert hasattr(research23_Transition, "guardLabel")
    descriptor = None
    for klass in research23_Transition.__mro__:
        if "guardLabel" in klass.__dict__:
            descriptor = klass.__dict__["guardLabel"]
            break
    assert isinstance(descriptor, property)

def test_research23_transition_has_guardExpression():
    assert hasattr(research23_Transition, "guardExpression")
    descriptor = None
    for klass in research23_Transition.__mro__:
        if "guardExpression" in klass.__dict__:
            descriptor = klass.__dict__["guardExpression"]
            break
    assert isinstance(descriptor, property)



def test_research23_labelled_is_not_abstract():
    assert not inspect.isabstract(research23_Labelled)


def test_research23_labelled_constructor_exists():
    assert callable(research23_Labelled.__init__)


def test_research23_labelled_constructor_args():
    sig = inspect.signature(research23_Labelled.__init__)
    params = list(sig.parameters.keys())
    assert "lname" in params, "Missing parameter 'lname'"

def test_research23_labelled_has_lname():
    assert hasattr(research23_Labelled, "lname")
    descriptor = None
    for klass in research23_Labelled.__mro__:
        if "lname" in klass.__dict__:
            descriptor = klass.__dict__["lname"]
            break
    assert isinstance(descriptor, property)



def test_research23_counted_is_not_abstract():
    assert not inspect.isabstract(research23_Counted)


def test_research23_counted_constructor_exists():
    assert callable(research23_Counted.__init__)


def test_research23_counted_constructor_args():
    sig = inspect.signature(research23_Counted.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_research23_counted_has_id():
    assert hasattr(research23_Counted, "id")
    descriptor = None
    for klass in research23_Counted.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_research23_named_is_not_abstract():
    assert not inspect.isabstract(research23_Named)


def test_research23_named_constructor_exists():
    assert callable(research23_Named.__init__)


def test_research23_named_constructor_args():
    sig = inspect.signature(research23_Named.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_research23_named_has_name():
    assert hasattr(research23_Named, "name")
    descriptor = None
    for klass in research23_Named.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_research23_publicationstatus_is_not_abstract():
    assert not inspect.isabstract(research23_PublicationStatus)


def test_research23_publicationstatus_constructor_exists():
    assert callable(research23_PublicationStatus.__init__)


def test_research23_publicationstatus_constructor_args():
    sig = inspect.signature(research23_PublicationStatus.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_research23_publicationstatus_has_label():
    assert hasattr(research23_PublicationStatus, "label")
    descriptor = None
    for klass in research23_PublicationStatus.__mro__:
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



def test_research23_state_is_not_abstract():
    assert not inspect.isabstract(research23_State)


def test_research23_state_constructor_exists():
    assert callable(research23_State.__init__)


def test_research23_state_constructor_args():
    sig = inspect.signature(research23_State.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "kind" in params, "Missing parameter 'kind'"
    assert "name" in params, "Missing parameter 'name'"

def test_research23_state_has_id():
    assert hasattr(research23_State, "id")
    descriptor = None
    for klass in research23_State.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_research23_state_has_kind():
    assert hasattr(research23_State, "kind")
    descriptor = None
    for klass in research23_State.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)

def test_research23_state_has_name():
    assert hasattr(research23_State, "name")
    descriptor = None
    for klass in research23_State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_research23_paperkeyword_is_not_abstract():
    assert not inspect.isabstract(research23_PaperKeyword)


def test_research23_paperkeyword_constructor_exists():
    assert callable(research23_PaperKeyword.__init__)


def test_research23_paperkeyword_constructor_args():
    sig = inspect.signature(research23_PaperKeyword.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"

def test_research23_paperkeyword_has_weight():
    assert hasattr(research23_PaperKeyword, "weight")
    descriptor = None
    for klass in research23_PaperKeyword.__mro__:
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



def test_research23_review_is_not_abstract():
    assert not inspect.isabstract(research23_Review)


def test_research23_review_constructor_exists():
    assert callable(research23_Review.__init__)


def test_research23_review_constructor_args():
    sig = inspect.signature(research23_Review.__init__)
    params = list(sig.parameters.keys())
    assert "date" in params, "Missing parameter 'date'"

def test_research23_review_has_date():
    assert hasattr(research23_Review, "date")
    descriptor = None
    for klass in research23_Review.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)



def test_research23_write_is_not_abstract():
    assert not inspect.isabstract(research23_Write)


def test_research23_write_constructor_exists():
    assert callable(research23_Write.__init__)


def test_research23_write_constructor_args():
    sig = inspect.signature(research23_Write.__init__)
    params = list(sig.parameters.keys())
    assert "timeSpent" in params, "Missing parameter 'timeSpent'"

def test_research23_write_has_timeSpent():
    assert hasattr(research23_Write, "timeSpent")
    descriptor = None
    for klass in research23_Write.__mro__:
        if "timeSpent" in klass.__dict__:
            descriptor = klass.__dict__["timeSpent"]
            break
    assert isinstance(descriptor, property)



def test_research23_researcher_is_not_abstract():
    assert not inspect.isabstract(research23_Researcher)


def test_research23_researcher_constructor_exists():
    assert callable(research23_Researcher.__init__)


def test_research23_researcher_constructor_args():
    sig = inspect.signature(research23_Researcher.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "forName" in params, "Missing parameter 'forName'"

def test_research23_researcher_has_name():
    assert hasattr(research23_Researcher, "name")
    descriptor = None
    for klass in research23_Researcher.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_research23_researcher_has_forName():
    assert hasattr(research23_Researcher, "forName")
    descriptor = None
    for klass in research23_Researcher.__mro__:
        if "forName" in klass.__dict__:
            descriptor = klass.__dict__["forName"]
            break
    assert isinstance(descriptor, property)



def test_research23_phase_is_not_abstract():
    assert not inspect.isabstract(research23_Phase)


def test_research23_phase_constructor_exists():
    assert callable(research23_Phase.__init__)


def test_research23_phase_constructor_args():
    sig = inspect.signature(research23_Phase.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_research23_phase_has_name():
    assert hasattr(research23_Phase, "name")
    descriptor = None
    for klass in research23_Phase.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_research23_progress_is_not_abstract():
    assert not inspect.isabstract(research23_Progress)


def test_research23_progress_constructor_exists():
    assert callable(research23_Progress.__init__)


def test_research23_progress_constructor_args():
    sig = inspect.signature(research23_Progress.__init__)
    params = list(sig.parameters.keys())
    assert "percent" in params, "Missing parameter 'percent'"

def test_research23_progress_has_percent():
    assert hasattr(research23_Progress, "percent")
    descriptor = None
    for klass in research23_Progress.__mro__:
        if "percent" in klass.__dict__:
            descriptor = klass.__dict__["percent"]
            break
    assert isinstance(descriptor, property)



def test_research23_collaboration_is_not_abstract():
    assert not inspect.isabstract(research23_Collaboration)


def test_research23_collaboration_constructor_exists():
    assert callable(research23_Collaboration.__init__)


def test_research23_collaboration_constructor_args():
    sig = inspect.signature(research23_Collaboration.__init__)
    params = list(sig.parameters.keys())
    assert "ratio" in params, "Missing parameter 'ratio'"

def test_research23_collaboration_has_ratio():
    assert hasattr(research23_Collaboration, "ratio")
    descriptor = None
    for klass in research23_Collaboration.__mro__:
        if "ratio" in klass.__dict__:
            descriptor = klass.__dict__["ratio"]
            break
    assert isinstance(descriptor, property)



def test_research23_skill_is_not_abstract():
    assert not inspect.isabstract(research23_Skill)


def test_research23_skill_constructor_exists():
    assert callable(research23_Skill.__init__)


def test_research23_skill_constructor_args():
    sig = inspect.signature(research23_Skill.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"

def test_research23_skill_has_description():
    assert hasattr(research23_Skill, "description")
    descriptor = None
    for klass in research23_Skill.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_named_is_not_abstract():
    assert not inspect.isabstract(Named)


def test_named_constructor_exists():
    assert callable(Named.__init__)


def test_named_constructor_args():
    sig = inspect.signature(Named.__init__)
    params = list(sig.parameters.keys())



def test_research23_position_is_not_abstract():
    assert not inspect.isabstract(research23_Position)


def test_research23_position_constructor_exists():
    assert callable(research23_Position.__init__)


def test_research23_position_constructor_args():
    sig = inspect.signature(research23_Position.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"

def test_research23_position_has_description():
    assert hasattr(research23_Position, "description")
    descriptor = None
    for klass in research23_Position.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_research23_paper_is_not_abstract():
    assert not inspect.isabstract(research23_Paper)


def test_research23_paper_constructor_exists():
    assert callable(research23_Paper.__init__)


def test_research23_paper_constructor_args():
    sig = inspect.signature(research23_Paper.__init__)
    params = list(sig.parameters.keys())



def test_research23_knowledgemanager_is_not_abstract():
    assert not inspect.isabstract(research23_KnowledgeManager)


def test_research23_knowledgemanager_constructor_exists():
    assert callable(research23_KnowledgeManager.__init__)


def test_research23_knowledgemanager_constructor_args():
    sig = inspect.signature(research23_KnowledgeManager.__init__)
    params = list(sig.parameters.keys())



def test_research23_reviewnote_is_not_abstract():
    assert not inspect.isabstract(research23_ReviewNote)


def test_research23_reviewnote_constructor_exists():
    assert callable(research23_ReviewNote.__init__)


def test_research23_reviewnote_constructor_args():
    sig = inspect.signature(research23_ReviewNote.__init__)
    params = list(sig.parameters.keys())
    assert "content" in params, "Missing parameter 'content'"

def test_research23_reviewnote_has_content():
    assert hasattr(research23_ReviewNote, "content")
    descriptor = None
    for klass in research23_ReviewNote.__mro__:
        if "content" in klass.__dict__:
            descriptor = klass.__dict__["content"]
            break
    assert isinstance(descriptor, property)



def test_research23_publicationstructure_is_not_abstract():
    assert not inspect.isabstract(research23_PublicationStructure)


def test_research23_publicationstructure_constructor_exists():
    assert callable(research23_PublicationStructure.__init__)


def test_research23_publicationstructure_constructor_args():
    sig = inspect.signature(research23_PublicationStructure.__init__)
    params = list(sig.parameters.keys())



def test_research23_paragraph_is_not_abstract():
    assert not inspect.isabstract(research23_Paragraph)


def test_research23_paragraph_constructor_exists():
    assert callable(research23_Paragraph.__init__)


def test_research23_paragraph_constructor_args():
    sig = inspect.signature(research23_Paragraph.__init__)
    params = list(sig.parameters.keys())
    assert "content" in params, "Missing parameter 'content'"

def test_research23_paragraph_has_content():
    assert hasattr(research23_Paragraph, "content")
    descriptor = None
    for klass in research23_Paragraph.__mro__:
        if "content" in klass.__dict__:
            descriptor = klass.__dict__["content"]
            break
    assert isinstance(descriptor, property)



def test_research23_publicationsystem_is_not_abstract():
    assert not inspect.isabstract(research23_PublicationSystem)


def test_research23_publicationsystem_constructor_exists():
    assert callable(research23_PublicationSystem.__init__)


def test_research23_publicationsystem_constructor_args():
    sig = inspect.signature(research23_PublicationSystem.__init__)
    params = list(sig.parameters.keys())



def test_research23_keyword_is_not_abstract():
    assert not inspect.isabstract(research23_Keyword)


def test_research23_keyword_constructor_exists():
    assert callable(research23_Keyword.__init__)


def test_research23_keyword_constructor_args():
    sig = inspect.signature(research23_Keyword.__init__)
    params = list(sig.parameters.keys())
    assert "word" in params, "Missing parameter 'word'"

def test_research23_keyword_has_word():
    assert hasattr(research23_Keyword, "word")
    descriptor = None
    for klass in research23_Keyword.__mro__:
        if "word" in klass.__dict__:
            descriptor = klass.__dict__["word"]
            break
    assert isinstance(descriptor, property)



def test_research23_publicationprocess_is_not_abstract():
    assert not inspect.isabstract(research23_PublicationProcess)


def test_research23_publicationprocess_constructor_exists():
    assert callable(research23_PublicationProcess.__init__)


def test_research23_publicationprocess_constructor_args():
    sig = inspect.signature(research23_PublicationProcess.__init__)
    params = list(sig.parameters.keys())
    assert "maxTime" in params, "Missing parameter 'maxTime'"
    assert "minTime" in params, "Missing parameter 'minTime'"

def test_research23_publicationprocess_has_maxTime():
    assert hasattr(research23_PublicationProcess, "maxTime")
    descriptor = None
    for klass in research23_PublicationProcess.__mro__:
        if "maxTime" in klass.__dict__:
            descriptor = klass.__dict__["maxTime"]
            break
    assert isinstance(descriptor, property)

def test_research23_publicationprocess_has_minTime():
    assert hasattr(research23_PublicationProcess, "minTime")
    descriptor = None
    for klass in research23_PublicationProcess.__mro__:
        if "minTime" in klass.__dict__:
            descriptor = klass.__dict__["minTime"]
            break
    assert isinstance(descriptor, property)



def test_research23_statemachineobject_is_not_abstract():
    assert not inspect.isabstract(research23_StateMachineObject)


def test_research23_statemachineobject_constructor_exists():
    assert callable(research23_StateMachineObject.__init__)


def test_research23_statemachineobject_constructor_args():
    sig = inspect.signature(research23_StateMachineObject.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_research23_statemachineobject_has_label():
    assert hasattr(research23_StateMachineObject, "label")
    descriptor = None
    for klass in research23_StateMachineObject.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_research23_statemachinevariable_is_not_abstract():
    assert not inspect.isabstract(research23_StateMachineVariable)


def test_research23_statemachinevariable_constructor_exists():
    assert callable(research23_StateMachineVariable.__init__)


def test_research23_statemachinevariable_constructor_args():
    sig = inspect.signature(research23_StateMachineVariable.__init__)
    params = list(sig.parameters.keys())

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
research23_Action_strategy = st.builds(
    research23_Action,
    actionLabel=
        safe_text,
    actionStatement=
        safe_text
)
StateMachineObject_strategy = st.builds(
    StateMachineObject,
)
research23_Transition_strategy = st.builds(
    research23_Transition,
    guardLabel=
        safe_text,
    guardExpression=
        safe_text
)
research23_Labelled_strategy = st.builds(
    research23_Labelled,
    lname=
        safe_text
)
research23_Counted_strategy = st.builds(
    research23_Counted,
    id=
        st.integers()
)
research23_Named_strategy = st.builds(
    research23_Named,
    name=
        safe_text
)
research23_PublicationStatus_strategy = st.builds(
    research23_PublicationStatus,
    label=
        safe_text
)
Counted_strategy = st.builds(
    Counted,
)
research23_State_strategy = st.builds(
    research23_State,
    id=
        st.integers(),
    kind=
        safe_text,
    name=
        safe_text
)
research23_PaperKeyword_strategy = st.builds(
    research23_PaperKeyword,
    weight=
        st.integers()
)
Labelled_strategy = st.builds(
    Labelled,
)
research23_Review_strategy = st.builds(
    research23_Review,
    date=
        st.dates()
)
research23_Write_strategy = st.builds(
    research23_Write,
    timeSpent=
        st.integers()
)
research23_Researcher_strategy = st.builds(
    research23_Researcher,
    name=
        safe_text,
    forName=
        safe_text
)
research23_Phase_strategy = st.builds(
    research23_Phase,
    name=
        safe_text
)
research23_Progress_strategy = st.builds(
    research23_Progress,
    percent=
        st.integers()
)
research23_Collaboration_strategy = st.builds(
    research23_Collaboration,
    ratio=
        st.integers()
)
research23_Skill_strategy = st.builds(
    research23_Skill,
    description=
        safe_text
)
Named_strategy = st.builds(
    Named,
)
research23_Position_strategy = st.builds(
    research23_Position,
    description=
        safe_text
)
research23_Paper_strategy = st.builds(
    research23_Paper,
)
research23_KnowledgeManager_strategy = st.builds(
    research23_KnowledgeManager,
)
research23_ReviewNote_strategy = st.builds(
    research23_ReviewNote,
    content=
        safe_text
)
research23_PublicationStructure_strategy = st.builds(
    research23_PublicationStructure,
)
research23_Paragraph_strategy = st.builds(
    research23_Paragraph,
    content=
        safe_text
)
research23_PublicationSystem_strategy = st.builds(
    research23_PublicationSystem,
)
research23_Keyword_strategy = st.builds(
    research23_Keyword,
    word=
        safe_text
)
research23_PublicationProcess_strategy = st.builds(
    research23_PublicationProcess,
    maxTime=
        st.integers(),
    minTime=
        st.integers()
)
research23_StateMachineObject_strategy = st.builds(
    research23_StateMachineObject,
    label=
        safe_text
)
research23_StateMachineVariable_strategy = st.builds(
    research23_StateMachineVariable,
)

@given(instance=research23_Action_strategy)
@settings(max_examples=50)
def test_research23_action_instantiation(instance):
    assert isinstance(instance, research23_Action)



@given(instance=research23_Action_strategy)
def test_research23_action_actionLabel_setter(instance):
    original = instance.actionLabel
    instance.actionLabel = original
    assert instance.actionLabel == original



@given(instance=research23_Action_strategy)
def test_research23_action_actionStatement_setter(instance):
    original = instance.actionStatement
    instance.actionStatement = original
    assert instance.actionStatement == original

@given(instance=StateMachineObject_strategy)
@settings(max_examples=50)
def test_statemachineobject_instantiation(instance):
    assert isinstance(instance, StateMachineObject)

@given(instance=research23_Transition_strategy)
@settings(max_examples=50)
def test_research23_transition_instantiation(instance):
    assert isinstance(instance, research23_Transition)



@given(instance=research23_Transition_strategy)
def test_research23_transition_guardLabel_setter(instance):
    original = instance.guardLabel
    instance.guardLabel = original
    assert instance.guardLabel == original



@given(instance=research23_Transition_strategy)
def test_research23_transition_guardExpression_setter(instance):
    original = instance.guardExpression
    instance.guardExpression = original
    assert instance.guardExpression == original

@given(instance=research23_Labelled_strategy)
@settings(max_examples=50)
def test_research23_labelled_instantiation(instance):
    assert isinstance(instance, research23_Labelled)



@given(instance=research23_Labelled_strategy)
def test_research23_labelled_lname_setter(instance):
    original = instance.lname
    instance.lname = original
    assert instance.lname == original

@given(instance=research23_Counted_strategy)
@settings(max_examples=50)
def test_research23_counted_instantiation(instance):
    assert isinstance(instance, research23_Counted)



@given(instance=research23_Counted_strategy)
def test_research23_counted_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=research23_Named_strategy)
@settings(max_examples=50)
def test_research23_named_instantiation(instance):
    assert isinstance(instance, research23_Named)



@given(instance=research23_Named_strategy)
def test_research23_named_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=research23_PublicationStatus_strategy)
@settings(max_examples=50)
def test_research23_publicationstatus_instantiation(instance):
    assert isinstance(instance, research23_PublicationStatus)



@given(instance=research23_PublicationStatus_strategy)
def test_research23_publicationstatus_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=Counted_strategy)
@settings(max_examples=50)
def test_counted_instantiation(instance):
    assert isinstance(instance, Counted)

@given(instance=research23_State_strategy)
@settings(max_examples=50)
def test_research23_state_instantiation(instance):
    assert isinstance(instance, research23_State)



@given(instance=research23_State_strategy)
def test_research23_state_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=research23_State_strategy)
def test_research23_state_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original



@given(instance=research23_State_strategy)
def test_research23_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=research23_PaperKeyword_strategy)
@settings(max_examples=50)
def test_research23_paperkeyword_instantiation(instance):
    assert isinstance(instance, research23_PaperKeyword)



@given(instance=research23_PaperKeyword_strategy)
def test_research23_paperkeyword_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=Labelled_strategy)
@settings(max_examples=50)
def test_labelled_instantiation(instance):
    assert isinstance(instance, Labelled)

@given(instance=research23_Review_strategy)
@settings(max_examples=50)
def test_research23_review_instantiation(instance):
    assert isinstance(instance, research23_Review)



@given(instance=research23_Review_strategy)
def test_research23_review_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original

@given(instance=research23_Write_strategy)
@settings(max_examples=50)
def test_research23_write_instantiation(instance):
    assert isinstance(instance, research23_Write)



@given(instance=research23_Write_strategy)
def test_research23_write_timeSpent_setter(instance):
    original = instance.timeSpent
    instance.timeSpent = original
    assert instance.timeSpent == original

@given(instance=research23_Researcher_strategy)
@settings(max_examples=50)
def test_research23_researcher_instantiation(instance):
    assert isinstance(instance, research23_Researcher)



@given(instance=research23_Researcher_strategy)
def test_research23_researcher_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=research23_Researcher_strategy)
def test_research23_researcher_forName_setter(instance):
    original = instance.forName
    instance.forName = original
    assert instance.forName == original

@given(instance=research23_Phase_strategy)
@settings(max_examples=50)
def test_research23_phase_instantiation(instance):
    assert isinstance(instance, research23_Phase)



@given(instance=research23_Phase_strategy)
def test_research23_phase_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=research23_Progress_strategy)
@settings(max_examples=50)
def test_research23_progress_instantiation(instance):
    assert isinstance(instance, research23_Progress)



@given(instance=research23_Progress_strategy)
def test_research23_progress_percent_setter(instance):
    original = instance.percent
    instance.percent = original
    assert instance.percent == original

@given(instance=research23_Collaboration_strategy)
@settings(max_examples=50)
def test_research23_collaboration_instantiation(instance):
    assert isinstance(instance, research23_Collaboration)



@given(instance=research23_Collaboration_strategy)
def test_research23_collaboration_ratio_setter(instance):
    original = instance.ratio
    instance.ratio = original
    assert instance.ratio == original

@given(instance=research23_Skill_strategy)
@settings(max_examples=50)
def test_research23_skill_instantiation(instance):
    assert isinstance(instance, research23_Skill)



@given(instance=research23_Skill_strategy)
def test_research23_skill_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=Named_strategy)
@settings(max_examples=50)
def test_named_instantiation(instance):
    assert isinstance(instance, Named)

@given(instance=research23_Position_strategy)
@settings(max_examples=50)
def test_research23_position_instantiation(instance):
    assert isinstance(instance, research23_Position)



@given(instance=research23_Position_strategy)
def test_research23_position_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=research23_Paper_strategy)
@settings(max_examples=50)
def test_research23_paper_instantiation(instance):
    assert isinstance(instance, research23_Paper)

@given(instance=research23_KnowledgeManager_strategy)
@settings(max_examples=50)
def test_research23_knowledgemanager_instantiation(instance):
    assert isinstance(instance, research23_KnowledgeManager)

@given(instance=research23_ReviewNote_strategy)
@settings(max_examples=50)
def test_research23_reviewnote_instantiation(instance):
    assert isinstance(instance, research23_ReviewNote)



@given(instance=research23_ReviewNote_strategy)
def test_research23_reviewnote_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original

@given(instance=research23_PublicationStructure_strategy)
@settings(max_examples=50)
def test_research23_publicationstructure_instantiation(instance):
    assert isinstance(instance, research23_PublicationStructure)

@given(instance=research23_Paragraph_strategy)
@settings(max_examples=50)
def test_research23_paragraph_instantiation(instance):
    assert isinstance(instance, research23_Paragraph)



@given(instance=research23_Paragraph_strategy)
def test_research23_paragraph_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original

@given(instance=research23_PublicationSystem_strategy)
@settings(max_examples=50)
def test_research23_publicationsystem_instantiation(instance):
    assert isinstance(instance, research23_PublicationSystem)

@given(instance=research23_Keyword_strategy)
@settings(max_examples=50)
def test_research23_keyword_instantiation(instance):
    assert isinstance(instance, research23_Keyword)



@given(instance=research23_Keyword_strategy)
def test_research23_keyword_word_setter(instance):
    original = instance.word
    instance.word = original
    assert instance.word == original

@given(instance=research23_PublicationProcess_strategy)
@settings(max_examples=50)
def test_research23_publicationprocess_instantiation(instance):
    assert isinstance(instance, research23_PublicationProcess)



@given(instance=research23_PublicationProcess_strategy)
def test_research23_publicationprocess_maxTime_setter(instance):
    original = instance.maxTime
    instance.maxTime = original
    assert instance.maxTime == original



@given(instance=research23_PublicationProcess_strategy)
def test_research23_publicationprocess_minTime_setter(instance):
    original = instance.minTime
    instance.minTime = original
    assert instance.minTime == original

@given(instance=research23_StateMachineObject_strategy)
@settings(max_examples=50)
def test_research23_statemachineobject_instantiation(instance):
    assert isinstance(instance, research23_StateMachineObject)



@given(instance=research23_StateMachineObject_strategy)
def test_research23_statemachineobject_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=research23_StateMachineVariable_strategy)
@settings(max_examples=50)
def test_research23_statemachinevariable_instantiation(instance):
    assert isinstance(instance, research23_StateMachineVariable)
