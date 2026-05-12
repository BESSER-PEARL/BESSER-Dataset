import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    publication2014a_Counted,
    publication2014a_Named,
    publication2014a_PublicationSystem,
    publication2014a_Labelled,
    Counted,
    Labelled,
    publication2014a_Progress,
    publication2014a_Researcher,
    publication2014a_Sequence,
    publication2014a_Rule,
    publication2014a_Review,
    publication2014a_Write,
    publication2014a_PublicationPhase,
    Named,
    publication2014a_Paragraph,
    publication2014a_Paper,
    publication2014a_PublicationStructure,
    publication2014a_ReviewNote,
    publication2014a_PublicationProcess,
    SequenceType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_publication2014a_counted_is_not_abstract():
    assert not inspect.isabstract(publication2014a_Counted)


def test_publication2014a_counted_constructor_exists():
    assert callable(publication2014a_Counted.__init__)


def test_publication2014a_counted_constructor_args():
    sig = inspect.signature(publication2014a_Counted.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_publication2014a_counted_has_id():
    assert hasattr(publication2014a_Counted, "id")
    descriptor = None
    for klass in publication2014a_Counted.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_publication2014a_named_is_not_abstract():
    assert not inspect.isabstract(publication2014a_Named)


def test_publication2014a_named_constructor_exists():
    assert callable(publication2014a_Named.__init__)


def test_publication2014a_named_constructor_args():
    sig = inspect.signature(publication2014a_Named.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_publication2014a_named_has_name():
    assert hasattr(publication2014a_Named, "name")
    descriptor = None
    for klass in publication2014a_Named.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_publication2014a_publicationsystem_is_not_abstract():
    assert not inspect.isabstract(publication2014a_PublicationSystem)


def test_publication2014a_publicationsystem_constructor_exists():
    assert callable(publication2014a_PublicationSystem.__init__)


def test_publication2014a_publicationsystem_constructor_args():
    sig = inspect.signature(publication2014a_PublicationSystem.__init__)
    params = list(sig.parameters.keys())



def test_publication2014a_labelled_is_not_abstract():
    assert not inspect.isabstract(publication2014a_Labelled)


def test_publication2014a_labelled_constructor_exists():
    assert callable(publication2014a_Labelled.__init__)


def test_publication2014a_labelled_constructor_args():
    sig = inspect.signature(publication2014a_Labelled.__init__)
    params = list(sig.parameters.keys())
    assert "lname" in params, "Missing parameter 'lname'"

def test_publication2014a_labelled_has_lname():
    assert hasattr(publication2014a_Labelled, "lname")
    descriptor = None
    for klass in publication2014a_Labelled.__mro__:
        if "lname" in klass.__dict__:
            descriptor = klass.__dict__["lname"]
            break
    assert isinstance(descriptor, property)



def test_counted_is_not_abstract():
    assert not inspect.isabstract(Counted)


def test_counted_constructor_exists():
    assert callable(Counted.__init__)


def test_counted_constructor_args():
    sig = inspect.signature(Counted.__init__)
    params = list(sig.parameters.keys())



def test_labelled_is_not_abstract():
    assert not inspect.isabstract(Labelled)


def test_labelled_constructor_exists():
    assert callable(Labelled.__init__)


def test_labelled_constructor_args():
    sig = inspect.signature(Labelled.__init__)
    params = list(sig.parameters.keys())



def test_publication2014a_progress_is_not_abstract():
    assert not inspect.isabstract(publication2014a_Progress)


def test_publication2014a_progress_constructor_exists():
    assert callable(publication2014a_Progress.__init__)


def test_publication2014a_progress_constructor_args():
    sig = inspect.signature(publication2014a_Progress.__init__)
    params = list(sig.parameters.keys())
    assert "time" in params, "Missing parameter 'time'"
    assert "percent" in params, "Missing parameter 'percent'"

def test_publication2014a_progress_has_time():
    assert hasattr(publication2014a_Progress, "time")
    descriptor = None
    for klass in publication2014a_Progress.__mro__:
        if "time" in klass.__dict__:
            descriptor = klass.__dict__["time"]
            break
    assert isinstance(descriptor, property)

def test_publication2014a_progress_has_percent():
    assert hasattr(publication2014a_Progress, "percent")
    descriptor = None
    for klass in publication2014a_Progress.__mro__:
        if "percent" in klass.__dict__:
            descriptor = klass.__dict__["percent"]
            break
    assert isinstance(descriptor, property)



def test_publication2014a_researcher_is_not_abstract():
    assert not inspect.isabstract(publication2014a_Researcher)


def test_publication2014a_researcher_constructor_exists():
    assert callable(publication2014a_Researcher.__init__)


def test_publication2014a_researcher_constructor_args():
    sig = inspect.signature(publication2014a_Researcher.__init__)
    params = list(sig.parameters.keys())
    assert "position" in params, "Missing parameter 'position'"
    assert "forName" in params, "Missing parameter 'forName'"
    assert "name" in params, "Missing parameter 'name'"

def test_publication2014a_researcher_has_position():
    assert hasattr(publication2014a_Researcher, "position")
    descriptor = None
    for klass in publication2014a_Researcher.__mro__:
        if "position" in klass.__dict__:
            descriptor = klass.__dict__["position"]
            break
    assert isinstance(descriptor, property)

def test_publication2014a_researcher_has_forName():
    assert hasattr(publication2014a_Researcher, "forName")
    descriptor = None
    for klass in publication2014a_Researcher.__mro__:
        if "forName" in klass.__dict__:
            descriptor = klass.__dict__["forName"]
            break
    assert isinstance(descriptor, property)

def test_publication2014a_researcher_has_name():
    assert hasattr(publication2014a_Researcher, "name")
    descriptor = None
    for klass in publication2014a_Researcher.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_publication2014a_sequence_is_not_abstract():
    assert not inspect.isabstract(publication2014a_Sequence)


def test_publication2014a_sequence_constructor_exists():
    assert callable(publication2014a_Sequence.__init__)


def test_publication2014a_sequence_constructor_args():
    sig = inspect.signature(publication2014a_Sequence.__init__)
    params = list(sig.parameters.keys())
    assert "sequenceType" in params, "Missing parameter 'sequenceType'"

def test_publication2014a_sequence_has_sequenceType():
    assert hasattr(publication2014a_Sequence, "sequenceType")
    descriptor = None
    for klass in publication2014a_Sequence.__mro__:
        if "sequenceType" in klass.__dict__:
            descriptor = klass.__dict__["sequenceType"]
            break
    assert isinstance(descriptor, property)



def test_publication2014a_rule_is_not_abstract():
    assert not inspect.isabstract(publication2014a_Rule)


def test_publication2014a_rule_constructor_exists():
    assert callable(publication2014a_Rule.__init__)


def test_publication2014a_rule_constructor_args():
    sig = inspect.signature(publication2014a_Rule.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"
    assert "text" in params, "Missing parameter 'text'"

def test_publication2014a_rule_has_key():
    assert hasattr(publication2014a_Rule, "key")
    descriptor = None
    for klass in publication2014a_Rule.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_publication2014a_rule_has_text():
    assert hasattr(publication2014a_Rule, "text")
    descriptor = None
    for klass in publication2014a_Rule.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_publication2014a_review_is_not_abstract():
    assert not inspect.isabstract(publication2014a_Review)


def test_publication2014a_review_constructor_exists():
    assert callable(publication2014a_Review.__init__)


def test_publication2014a_review_constructor_args():
    sig = inspect.signature(publication2014a_Review.__init__)
    params = list(sig.parameters.keys())



def test_publication2014a_write_is_not_abstract():
    assert not inspect.isabstract(publication2014a_Write)


def test_publication2014a_write_constructor_exists():
    assert callable(publication2014a_Write.__init__)


def test_publication2014a_write_constructor_args():
    sig = inspect.signature(publication2014a_Write.__init__)
    params = list(sig.parameters.keys())



def test_publication2014a_publicationphase_is_not_abstract():
    assert not inspect.isabstract(publication2014a_PublicationPhase)


def test_publication2014a_publicationphase_constructor_exists():
    assert callable(publication2014a_PublicationPhase.__init__)


def test_publication2014a_publicationphase_constructor_args():
    sig = inspect.signature(publication2014a_PublicationPhase.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "maxTime" in params, "Missing parameter 'maxTime'"
    assert "minTime" in params, "Missing parameter 'minTime'"

def test_publication2014a_publicationphase_has_name():
    assert hasattr(publication2014a_PublicationPhase, "name")
    descriptor = None
    for klass in publication2014a_PublicationPhase.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_publication2014a_publicationphase_has_maxTime():
    assert hasattr(publication2014a_PublicationPhase, "maxTime")
    descriptor = None
    for klass in publication2014a_PublicationPhase.__mro__:
        if "maxTime" in klass.__dict__:
            descriptor = klass.__dict__["maxTime"]
            break
    assert isinstance(descriptor, property)

def test_publication2014a_publicationphase_has_minTime():
    assert hasattr(publication2014a_PublicationPhase, "minTime")
    descriptor = None
    for klass in publication2014a_PublicationPhase.__mro__:
        if "minTime" in klass.__dict__:
            descriptor = klass.__dict__["minTime"]
            break
    assert isinstance(descriptor, property)



def test_named_is_not_abstract():
    assert not inspect.isabstract(Named)


def test_named_constructor_exists():
    assert callable(Named.__init__)


def test_named_constructor_args():
    sig = inspect.signature(Named.__init__)
    params = list(sig.parameters.keys())



def test_publication2014a_paragraph_is_not_abstract():
    assert not inspect.isabstract(publication2014a_Paragraph)


def test_publication2014a_paragraph_constructor_exists():
    assert callable(publication2014a_Paragraph.__init__)


def test_publication2014a_paragraph_constructor_args():
    sig = inspect.signature(publication2014a_Paragraph.__init__)
    params = list(sig.parameters.keys())
    assert "content" in params, "Missing parameter 'content'"

def test_publication2014a_paragraph_has_content():
    assert hasattr(publication2014a_Paragraph, "content")
    descriptor = None
    for klass in publication2014a_Paragraph.__mro__:
        if "content" in klass.__dict__:
            descriptor = klass.__dict__["content"]
            break
    assert isinstance(descriptor, property)



def test_publication2014a_paper_is_not_abstract():
    assert not inspect.isabstract(publication2014a_Paper)


def test_publication2014a_paper_constructor_exists():
    assert callable(publication2014a_Paper.__init__)


def test_publication2014a_paper_constructor_args():
    sig = inspect.signature(publication2014a_Paper.__init__)
    params = list(sig.parameters.keys())



def test_publication2014a_publicationstructure_is_not_abstract():
    assert not inspect.isabstract(publication2014a_PublicationStructure)


def test_publication2014a_publicationstructure_constructor_exists():
    assert callable(publication2014a_PublicationStructure.__init__)


def test_publication2014a_publicationstructure_constructor_args():
    sig = inspect.signature(publication2014a_PublicationStructure.__init__)
    params = list(sig.parameters.keys())



def test_publication2014a_reviewnote_is_not_abstract():
    assert not inspect.isabstract(publication2014a_ReviewNote)


def test_publication2014a_reviewnote_constructor_exists():
    assert callable(publication2014a_ReviewNote.__init__)


def test_publication2014a_reviewnote_constructor_args():
    sig = inspect.signature(publication2014a_ReviewNote.__init__)
    params = list(sig.parameters.keys())
    assert "content" in params, "Missing parameter 'content'"

def test_publication2014a_reviewnote_has_content():
    assert hasattr(publication2014a_ReviewNote, "content")
    descriptor = None
    for klass in publication2014a_ReviewNote.__mro__:
        if "content" in klass.__dict__:
            descriptor = klass.__dict__["content"]
            break
    assert isinstance(descriptor, property)



def test_publication2014a_publicationprocess_is_not_abstract():
    assert not inspect.isabstract(publication2014a_PublicationProcess)


def test_publication2014a_publicationprocess_constructor_exists():
    assert callable(publication2014a_PublicationProcess.__init__)


def test_publication2014a_publicationprocess_constructor_args():
    sig = inspect.signature(publication2014a_PublicationProcess.__init__)
    params = list(sig.parameters.keys())
    assert "minTime" in params, "Missing parameter 'minTime'"
    assert "maxTime" in params, "Missing parameter 'maxTime'"

def test_publication2014a_publicationprocess_has_minTime():
    assert hasattr(publication2014a_PublicationProcess, "minTime")
    descriptor = None
    for klass in publication2014a_PublicationProcess.__mro__:
        if "minTime" in klass.__dict__:
            descriptor = klass.__dict__["minTime"]
            break
    assert isinstance(descriptor, property)

def test_publication2014a_publicationprocess_has_maxTime():
    assert hasattr(publication2014a_PublicationProcess, "maxTime")
    descriptor = None
    for klass in publication2014a_PublicationProcess.__mro__:
        if "maxTime" in klass.__dict__:
            descriptor = klass.__dict__["maxTime"]
            break
    assert isinstance(descriptor, property)

def test_sequencetype_exists():
    # Check that the Enumeration exists
    assert SequenceType is not None

def test_sequencetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SequenceType]
    expected_literals = [
        "startToFinish",
        "finishToStart",
        "finishToFinish",
        "startToStart",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SequenceType"


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
publication2014a_Counted_strategy = st.builds(
    publication2014a_Counted,
    id=
        st.integers()
)
publication2014a_Named_strategy = st.builds(
    publication2014a_Named,
    name=
        safe_text
)
publication2014a_PublicationSystem_strategy = st.builds(
    publication2014a_PublicationSystem,
)
publication2014a_Labelled_strategy = st.builds(
    publication2014a_Labelled,
    lname=
        safe_text
)
Counted_strategy = st.builds(
    Counted,
)
Labelled_strategy = st.builds(
    Labelled,
)
publication2014a_Progress_strategy = st.builds(
    publication2014a_Progress,
    time=
        st.integers(),
    percent=
        st.integers()
)
publication2014a_Researcher_strategy = st.builds(
    publication2014a_Researcher,
    position=
        safe_text,
    forName=
        safe_text,
    name=
        safe_text
)
publication2014a_Sequence_strategy = st.builds(
    publication2014a_Sequence,
    sequenceType=
        safe_text
)
publication2014a_Rule_strategy = st.builds(
    publication2014a_Rule,
    key=
        safe_text,
    text=
        safe_text
)
publication2014a_Review_strategy = st.builds(
    publication2014a_Review,
)
publication2014a_Write_strategy = st.builds(
    publication2014a_Write,
)
publication2014a_PublicationPhase_strategy = st.builds(
    publication2014a_PublicationPhase,
    name=
        safe_text,
    maxTime=
        st.integers(),
    minTime=
        st.integers()
)
Named_strategy = st.builds(
    Named,
)
publication2014a_Paragraph_strategy = st.builds(
    publication2014a_Paragraph,
    content=
        safe_text
)
publication2014a_Paper_strategy = st.builds(
    publication2014a_Paper,
)
publication2014a_PublicationStructure_strategy = st.builds(
    publication2014a_PublicationStructure,
)
publication2014a_ReviewNote_strategy = st.builds(
    publication2014a_ReviewNote,
    content=
        safe_text
)
publication2014a_PublicationProcess_strategy = st.builds(
    publication2014a_PublicationProcess,
    minTime=
        st.integers(),
    maxTime=
        st.integers()
)

@given(instance=publication2014a_Counted_strategy)
@settings(max_examples=50)
def test_publication2014a_counted_instantiation(instance):
    assert isinstance(instance, publication2014a_Counted)



@given(instance=publication2014a_Counted_strategy)
def test_publication2014a_counted_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=publication2014a_Named_strategy)
@settings(max_examples=50)
def test_publication2014a_named_instantiation(instance):
    assert isinstance(instance, publication2014a_Named)



@given(instance=publication2014a_Named_strategy)
def test_publication2014a_named_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=publication2014a_PublicationSystem_strategy)
@settings(max_examples=50)
def test_publication2014a_publicationsystem_instantiation(instance):
    assert isinstance(instance, publication2014a_PublicationSystem)

@given(instance=publication2014a_Labelled_strategy)
@settings(max_examples=50)
def test_publication2014a_labelled_instantiation(instance):
    assert isinstance(instance, publication2014a_Labelled)



@given(instance=publication2014a_Labelled_strategy)
def test_publication2014a_labelled_lname_setter(instance):
    original = instance.lname
    instance.lname = original
    assert instance.lname == original

@given(instance=Counted_strategy)
@settings(max_examples=50)
def test_counted_instantiation(instance):
    assert isinstance(instance, Counted)

@given(instance=Labelled_strategy)
@settings(max_examples=50)
def test_labelled_instantiation(instance):
    assert isinstance(instance, Labelled)

@given(instance=publication2014a_Progress_strategy)
@settings(max_examples=50)
def test_publication2014a_progress_instantiation(instance):
    assert isinstance(instance, publication2014a_Progress)



@given(instance=publication2014a_Progress_strategy)
def test_publication2014a_progress_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original



@given(instance=publication2014a_Progress_strategy)
def test_publication2014a_progress_percent_setter(instance):
    original = instance.percent
    instance.percent = original
    assert instance.percent == original

@given(instance=publication2014a_Researcher_strategy)
@settings(max_examples=50)
def test_publication2014a_researcher_instantiation(instance):
    assert isinstance(instance, publication2014a_Researcher)



@given(instance=publication2014a_Researcher_strategy)
def test_publication2014a_researcher_position_setter(instance):
    original = instance.position
    instance.position = original
    assert instance.position == original



@given(instance=publication2014a_Researcher_strategy)
def test_publication2014a_researcher_forName_setter(instance):
    original = instance.forName
    instance.forName = original
    assert instance.forName == original



@given(instance=publication2014a_Researcher_strategy)
def test_publication2014a_researcher_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=publication2014a_Sequence_strategy)
@settings(max_examples=50)
def test_publication2014a_sequence_instantiation(instance):
    assert isinstance(instance, publication2014a_Sequence)



@given(instance=publication2014a_Sequence_strategy)
def test_publication2014a_sequence_sequenceType_setter(instance):
    original = instance.sequenceType
    instance.sequenceType = original
    assert instance.sequenceType == original

@given(instance=publication2014a_Rule_strategy)
@settings(max_examples=50)
def test_publication2014a_rule_instantiation(instance):
    assert isinstance(instance, publication2014a_Rule)



@given(instance=publication2014a_Rule_strategy)
def test_publication2014a_rule_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original



@given(instance=publication2014a_Rule_strategy)
def test_publication2014a_rule_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=publication2014a_Review_strategy)
@settings(max_examples=50)
def test_publication2014a_review_instantiation(instance):
    assert isinstance(instance, publication2014a_Review)

@given(instance=publication2014a_Write_strategy)
@settings(max_examples=50)
def test_publication2014a_write_instantiation(instance):
    assert isinstance(instance, publication2014a_Write)

@given(instance=publication2014a_PublicationPhase_strategy)
@settings(max_examples=50)
def test_publication2014a_publicationphase_instantiation(instance):
    assert isinstance(instance, publication2014a_PublicationPhase)



@given(instance=publication2014a_PublicationPhase_strategy)
def test_publication2014a_publicationphase_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=publication2014a_PublicationPhase_strategy)
def test_publication2014a_publicationphase_maxTime_setter(instance):
    original = instance.maxTime
    instance.maxTime = original
    assert instance.maxTime == original



@given(instance=publication2014a_PublicationPhase_strategy)
def test_publication2014a_publicationphase_minTime_setter(instance):
    original = instance.minTime
    instance.minTime = original
    assert instance.minTime == original

@given(instance=Named_strategy)
@settings(max_examples=50)
def test_named_instantiation(instance):
    assert isinstance(instance, Named)

@given(instance=publication2014a_Paragraph_strategy)
@settings(max_examples=50)
def test_publication2014a_paragraph_instantiation(instance):
    assert isinstance(instance, publication2014a_Paragraph)



@given(instance=publication2014a_Paragraph_strategy)
def test_publication2014a_paragraph_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original

@given(instance=publication2014a_Paper_strategy)
@settings(max_examples=50)
def test_publication2014a_paper_instantiation(instance):
    assert isinstance(instance, publication2014a_Paper)

@given(instance=publication2014a_PublicationStructure_strategy)
@settings(max_examples=50)
def test_publication2014a_publicationstructure_instantiation(instance):
    assert isinstance(instance, publication2014a_PublicationStructure)

@given(instance=publication2014a_ReviewNote_strategy)
@settings(max_examples=50)
def test_publication2014a_reviewnote_instantiation(instance):
    assert isinstance(instance, publication2014a_ReviewNote)



@given(instance=publication2014a_ReviewNote_strategy)
def test_publication2014a_reviewnote_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original

@given(instance=publication2014a_PublicationProcess_strategy)
@settings(max_examples=50)
def test_publication2014a_publicationprocess_instantiation(instance):
    assert isinstance(instance, publication2014a_PublicationProcess)



@given(instance=publication2014a_PublicationProcess_strategy)
def test_publication2014a_publicationprocess_minTime_setter(instance):
    original = instance.minTime
    instance.minTime = original
    assert instance.minTime == original



@given(instance=publication2014a_PublicationProcess_strategy)
def test_publication2014a_publicationprocess_maxTime_setter(instance):
    original = instance.maxTime
    instance.maxTime = original
    assert instance.maxTime == original
