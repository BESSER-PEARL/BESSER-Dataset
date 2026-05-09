import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    publication2014a::Labelled,
    publication2014a::Counted,
    publication2014a::Named,
    publication2014a::PublicationSystem,
    Labelled,
    Counted,
    publication2014a::Progress,
    publication2014a::Review,
    publication2014a::Write,
    publication2014a::Researcher,
    publication2014a::Sequence,
    Named,
    publication2014a::Paragraph,
    publication2014a::Paper,
    publication2014a::ReviewNote,
    publication2014a::PublicationStructure,
    publication2014a::PublicationProcess,
    publication2014a::Rule,
    publication2014a::PublicationPhase,
    SequenceType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_publication2014a::labelled_is_not_abstract():
    assert not inspect.isabstract(publication2014a::Labelled)


def test_publication2014a::labelled_constructor_exists():
    assert callable(publication2014a::Labelled.__init__)


def test_publication2014a::labelled_constructor_args():
    sig = inspect.signature(publication2014a::Labelled.__init__)
    params = list(sig.parameters.keys())
    assert "lname" in params, "Missing parameter 'lname'"

def test_publication2014a::labelled_has_lname():
    assert hasattr(publication2014a::Labelled, "lname")
    descriptor = None
    for klass in publication2014a::Labelled.__mro__:
        if "lname" in klass.__dict__:
            descriptor = klass.__dict__["lname"]
            break
    assert isinstance(descriptor, property)



def test_publication2014a::counted_is_not_abstract():
    assert not inspect.isabstract(publication2014a::Counted)


def test_publication2014a::counted_constructor_exists():
    assert callable(publication2014a::Counted.__init__)


def test_publication2014a::counted_constructor_args():
    sig = inspect.signature(publication2014a::Counted.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_publication2014a::counted_has_id():
    assert hasattr(publication2014a::Counted, "id")
    descriptor = None
    for klass in publication2014a::Counted.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_publication2014a::named_is_not_abstract():
    assert not inspect.isabstract(publication2014a::Named)


def test_publication2014a::named_constructor_exists():
    assert callable(publication2014a::Named.__init__)


def test_publication2014a::named_constructor_args():
    sig = inspect.signature(publication2014a::Named.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_publication2014a::named_has_name():
    assert hasattr(publication2014a::Named, "name")
    descriptor = None
    for klass in publication2014a::Named.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_publication2014a::publicationsystem_is_not_abstract():
    assert not inspect.isabstract(publication2014a::PublicationSystem)


def test_publication2014a::publicationsystem_constructor_exists():
    assert callable(publication2014a::PublicationSystem.__init__)


def test_publication2014a::publicationsystem_constructor_args():
    sig = inspect.signature(publication2014a::PublicationSystem.__init__)
    params = list(sig.parameters.keys())



def test_labelled_is_not_abstract():
    assert not inspect.isabstract(Labelled)


def test_labelled_constructor_exists():
    assert callable(Labelled.__init__)


def test_labelled_constructor_args():
    sig = inspect.signature(Labelled.__init__)
    params = list(sig.parameters.keys())



def test_counted_is_not_abstract():
    assert not inspect.isabstract(Counted)


def test_counted_constructor_exists():
    assert callable(Counted.__init__)


def test_counted_constructor_args():
    sig = inspect.signature(Counted.__init__)
    params = list(sig.parameters.keys())



def test_publication2014a::progress_is_not_abstract():
    assert not inspect.isabstract(publication2014a::Progress)


def test_publication2014a::progress_constructor_exists():
    assert callable(publication2014a::Progress.__init__)


def test_publication2014a::progress_constructor_args():
    sig = inspect.signature(publication2014a::Progress.__init__)
    params = list(sig.parameters.keys())
    assert "percent" in params, "Missing parameter 'percent'"
    assert "time" in params, "Missing parameter 'time'"

def test_publication2014a::progress_has_percent():
    assert hasattr(publication2014a::Progress, "percent")
    descriptor = None
    for klass in publication2014a::Progress.__mro__:
        if "percent" in klass.__dict__:
            descriptor = klass.__dict__["percent"]
            break
    assert isinstance(descriptor, property)

def test_publication2014a::progress_has_time():
    assert hasattr(publication2014a::Progress, "time")
    descriptor = None
    for klass in publication2014a::Progress.__mro__:
        if "time" in klass.__dict__:
            descriptor = klass.__dict__["time"]
            break
    assert isinstance(descriptor, property)



def test_publication2014a::review_is_not_abstract():
    assert not inspect.isabstract(publication2014a::Review)


def test_publication2014a::review_constructor_exists():
    assert callable(publication2014a::Review.__init__)


def test_publication2014a::review_constructor_args():
    sig = inspect.signature(publication2014a::Review.__init__)
    params = list(sig.parameters.keys())



def test_publication2014a::write_is_not_abstract():
    assert not inspect.isabstract(publication2014a::Write)


def test_publication2014a::write_constructor_exists():
    assert callable(publication2014a::Write.__init__)


def test_publication2014a::write_constructor_args():
    sig = inspect.signature(publication2014a::Write.__init__)
    params = list(sig.parameters.keys())



def test_publication2014a::researcher_is_not_abstract():
    assert not inspect.isabstract(publication2014a::Researcher)


def test_publication2014a::researcher_constructor_exists():
    assert callable(publication2014a::Researcher.__init__)


def test_publication2014a::researcher_constructor_args():
    sig = inspect.signature(publication2014a::Researcher.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "position" in params, "Missing parameter 'position'"
    assert "forName" in params, "Missing parameter 'forName'"

def test_publication2014a::researcher_has_name():
    assert hasattr(publication2014a::Researcher, "name")
    descriptor = None
    for klass in publication2014a::Researcher.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_publication2014a::researcher_has_position():
    assert hasattr(publication2014a::Researcher, "position")
    descriptor = None
    for klass in publication2014a::Researcher.__mro__:
        if "position" in klass.__dict__:
            descriptor = klass.__dict__["position"]
            break
    assert isinstance(descriptor, property)

def test_publication2014a::researcher_has_forName():
    assert hasattr(publication2014a::Researcher, "forName")
    descriptor = None
    for klass in publication2014a::Researcher.__mro__:
        if "forName" in klass.__dict__:
            descriptor = klass.__dict__["forName"]
            break
    assert isinstance(descriptor, property)



def test_publication2014a::sequence_is_not_abstract():
    assert not inspect.isabstract(publication2014a::Sequence)


def test_publication2014a::sequence_constructor_exists():
    assert callable(publication2014a::Sequence.__init__)


def test_publication2014a::sequence_constructor_args():
    sig = inspect.signature(publication2014a::Sequence.__init__)
    params = list(sig.parameters.keys())
    assert "sequenceType" in params, "Missing parameter 'sequenceType'"

def test_publication2014a::sequence_has_sequenceType():
    assert hasattr(publication2014a::Sequence, "sequenceType")
    descriptor = None
    for klass in publication2014a::Sequence.__mro__:
        if "sequenceType" in klass.__dict__:
            descriptor = klass.__dict__["sequenceType"]
            break
    assert isinstance(descriptor, property)



def test_named_is_not_abstract():
    assert not inspect.isabstract(Named)


def test_named_constructor_exists():
    assert callable(Named.__init__)


def test_named_constructor_args():
    sig = inspect.signature(Named.__init__)
    params = list(sig.parameters.keys())



def test_publication2014a::paragraph_is_not_abstract():
    assert not inspect.isabstract(publication2014a::Paragraph)


def test_publication2014a::paragraph_constructor_exists():
    assert callable(publication2014a::Paragraph.__init__)


def test_publication2014a::paragraph_constructor_args():
    sig = inspect.signature(publication2014a::Paragraph.__init__)
    params = list(sig.parameters.keys())
    assert "content" in params, "Missing parameter 'content'"

def test_publication2014a::paragraph_has_content():
    assert hasattr(publication2014a::Paragraph, "content")
    descriptor = None
    for klass in publication2014a::Paragraph.__mro__:
        if "content" in klass.__dict__:
            descriptor = klass.__dict__["content"]
            break
    assert isinstance(descriptor, property)



def test_publication2014a::paper_is_not_abstract():
    assert not inspect.isabstract(publication2014a::Paper)


def test_publication2014a::paper_constructor_exists():
    assert callable(publication2014a::Paper.__init__)


def test_publication2014a::paper_constructor_args():
    sig = inspect.signature(publication2014a::Paper.__init__)
    params = list(sig.parameters.keys())



def test_publication2014a::reviewnote_is_not_abstract():
    assert not inspect.isabstract(publication2014a::ReviewNote)


def test_publication2014a::reviewnote_constructor_exists():
    assert callable(publication2014a::ReviewNote.__init__)


def test_publication2014a::reviewnote_constructor_args():
    sig = inspect.signature(publication2014a::ReviewNote.__init__)
    params = list(sig.parameters.keys())
    assert "content" in params, "Missing parameter 'content'"

def test_publication2014a::reviewnote_has_content():
    assert hasattr(publication2014a::ReviewNote, "content")
    descriptor = None
    for klass in publication2014a::ReviewNote.__mro__:
        if "content" in klass.__dict__:
            descriptor = klass.__dict__["content"]
            break
    assert isinstance(descriptor, property)



def test_publication2014a::publicationstructure_is_not_abstract():
    assert not inspect.isabstract(publication2014a::PublicationStructure)


def test_publication2014a::publicationstructure_constructor_exists():
    assert callable(publication2014a::PublicationStructure.__init__)


def test_publication2014a::publicationstructure_constructor_args():
    sig = inspect.signature(publication2014a::PublicationStructure.__init__)
    params = list(sig.parameters.keys())



def test_publication2014a::publicationprocess_is_not_abstract():
    assert not inspect.isabstract(publication2014a::PublicationProcess)


def test_publication2014a::publicationprocess_constructor_exists():
    assert callable(publication2014a::PublicationProcess.__init__)


def test_publication2014a::publicationprocess_constructor_args():
    sig = inspect.signature(publication2014a::PublicationProcess.__init__)
    params = list(sig.parameters.keys())
    assert "maxTime" in params, "Missing parameter 'maxTime'"
    assert "minTime" in params, "Missing parameter 'minTime'"

def test_publication2014a::publicationprocess_has_maxTime():
    assert hasattr(publication2014a::PublicationProcess, "maxTime")
    descriptor = None
    for klass in publication2014a::PublicationProcess.__mro__:
        if "maxTime" in klass.__dict__:
            descriptor = klass.__dict__["maxTime"]
            break
    assert isinstance(descriptor, property)

def test_publication2014a::publicationprocess_has_minTime():
    assert hasattr(publication2014a::PublicationProcess, "minTime")
    descriptor = None
    for klass in publication2014a::PublicationProcess.__mro__:
        if "minTime" in klass.__dict__:
            descriptor = klass.__dict__["minTime"]
            break
    assert isinstance(descriptor, property)



def test_publication2014a::rule_is_not_abstract():
    assert not inspect.isabstract(publication2014a::Rule)


def test_publication2014a::rule_constructor_exists():
    assert callable(publication2014a::Rule.__init__)


def test_publication2014a::rule_constructor_args():
    sig = inspect.signature(publication2014a::Rule.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"
    assert "text" in params, "Missing parameter 'text'"

def test_publication2014a::rule_has_key():
    assert hasattr(publication2014a::Rule, "key")
    descriptor = None
    for klass in publication2014a::Rule.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_publication2014a::rule_has_text():
    assert hasattr(publication2014a::Rule, "text")
    descriptor = None
    for klass in publication2014a::Rule.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_publication2014a::publicationphase_is_not_abstract():
    assert not inspect.isabstract(publication2014a::PublicationPhase)


def test_publication2014a::publicationphase_constructor_exists():
    assert callable(publication2014a::PublicationPhase.__init__)


def test_publication2014a::publicationphase_constructor_args():
    sig = inspect.signature(publication2014a::PublicationPhase.__init__)
    params = list(sig.parameters.keys())
    assert "minTime" in params, "Missing parameter 'minTime'"
    assert "name" in params, "Missing parameter 'name'"
    assert "maxTime" in params, "Missing parameter 'maxTime'"

def test_publication2014a::publicationphase_has_minTime():
    assert hasattr(publication2014a::PublicationPhase, "minTime")
    descriptor = None
    for klass in publication2014a::PublicationPhase.__mro__:
        if "minTime" in klass.__dict__:
            descriptor = klass.__dict__["minTime"]
            break
    assert isinstance(descriptor, property)

def test_publication2014a::publicationphase_has_name():
    assert hasattr(publication2014a::PublicationPhase, "name")
    descriptor = None
    for klass in publication2014a::PublicationPhase.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_publication2014a::publicationphase_has_maxTime():
    assert hasattr(publication2014a::PublicationPhase, "maxTime")
    descriptor = None
    for klass in publication2014a::PublicationPhase.__mro__:
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
        "finishToStart",
        "startToFinish",
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
publication2014a::Labelled_strategy = st.builds(
    publication2014a::Labelled,
    lname=
        safe_text
)
publication2014a::Counted_strategy = st.builds(
    publication2014a::Counted,
    id=
        st.integers()
)
publication2014a::Named_strategy = st.builds(
    publication2014a::Named,
    name=
        safe_text
)
publication2014a::PublicationSystem_strategy = st.builds(
    publication2014a::PublicationSystem,
)
Labelled_strategy = st.builds(
    Labelled,
)
Counted_strategy = st.builds(
    Counted,
)
publication2014a::Progress_strategy = st.builds(
    publication2014a::Progress,
    percent=
        st.integers(),
    time=
        st.integers()
)
publication2014a::Review_strategy = st.builds(
    publication2014a::Review,
)
publication2014a::Write_strategy = st.builds(
    publication2014a::Write,
)
publication2014a::Researcher_strategy = st.builds(
    publication2014a::Researcher,
    name=
        safe_text,
    position=
        safe_text,
    forName=
        safe_text
)
publication2014a::Sequence_strategy = st.builds(
    publication2014a::Sequence,
    sequenceType=
        safe_text
)
Named_strategy = st.builds(
    Named,
)
publication2014a::Paragraph_strategy = st.builds(
    publication2014a::Paragraph,
    content=
        safe_text
)
publication2014a::Paper_strategy = st.builds(
    publication2014a::Paper,
)
publication2014a::ReviewNote_strategy = st.builds(
    publication2014a::ReviewNote,
    content=
        safe_text
)
publication2014a::PublicationStructure_strategy = st.builds(
    publication2014a::PublicationStructure,
)
publication2014a::PublicationProcess_strategy = st.builds(
    publication2014a::PublicationProcess,
    maxTime=
        st.integers(),
    minTime=
        st.integers()
)
publication2014a::Rule_strategy = st.builds(
    publication2014a::Rule,
    key=
        safe_text,
    text=
        safe_text
)
publication2014a::PublicationPhase_strategy = st.builds(
    publication2014a::PublicationPhase,
    minTime=
        st.integers(),
    name=
        safe_text,
    maxTime=
        st.integers()
)

@given(instance=publication2014a::Labelled_strategy)
@settings(max_examples=50)
def test_publication2014a::labelled_instantiation(instance):
    assert isinstance(instance, publication2014a::Labelled)

@given(instance=publication2014a::Labelled_strategy)
def test_publication2014a::labelled_lname_type(instance):
    assert isinstance(instance.lname, str)


@given(instance=publication2014a::Labelled_strategy)
def test_publication2014a::labelled_lname_setter(instance):
    original = instance.lname
    instance.lname = original
    assert instance.lname == original

@given(instance=publication2014a::Counted_strategy)
@settings(max_examples=50)
def test_publication2014a::counted_instantiation(instance):
    assert isinstance(instance, publication2014a::Counted)

@given(instance=publication2014a::Counted_strategy)
def test_publication2014a::counted_id_type(instance):
    assert isinstance(instance.id, int)


@given(instance=publication2014a::Counted_strategy)
def test_publication2014a::counted_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=publication2014a::Named_strategy)
@settings(max_examples=50)
def test_publication2014a::named_instantiation(instance):
    assert isinstance(instance, publication2014a::Named)

@given(instance=publication2014a::Named_strategy)
def test_publication2014a::named_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=publication2014a::Named_strategy)
def test_publication2014a::named_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=publication2014a::PublicationSystem_strategy)
@settings(max_examples=50)
def test_publication2014a::publicationsystem_instantiation(instance):
    assert isinstance(instance, publication2014a::PublicationSystem)

@given(instance=Labelled_strategy)
@settings(max_examples=50)
def test_labelled_instantiation(instance):
    assert isinstance(instance, Labelled)

@given(instance=Counted_strategy)
@settings(max_examples=50)
def test_counted_instantiation(instance):
    assert isinstance(instance, Counted)

@given(instance=publication2014a::Progress_strategy)
@settings(max_examples=50)
def test_publication2014a::progress_instantiation(instance):
    assert isinstance(instance, publication2014a::Progress)

@given(instance=publication2014a::Progress_strategy)
def test_publication2014a::progress_percent_type(instance):
    assert isinstance(instance.percent, int)


@given(instance=publication2014a::Progress_strategy)
def test_publication2014a::progress_percent_setter(instance):
    original = instance.percent
    instance.percent = original
    assert instance.percent == original

@given(instance=publication2014a::Progress_strategy)
def test_publication2014a::progress_time_type(instance):
    assert isinstance(instance.time, int)


@given(instance=publication2014a::Progress_strategy)
def test_publication2014a::progress_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original

@given(instance=publication2014a::Review_strategy)
@settings(max_examples=50)
def test_publication2014a::review_instantiation(instance):
    assert isinstance(instance, publication2014a::Review)

@given(instance=publication2014a::Write_strategy)
@settings(max_examples=50)
def test_publication2014a::write_instantiation(instance):
    assert isinstance(instance, publication2014a::Write)

@given(instance=publication2014a::Researcher_strategy)
@settings(max_examples=50)
def test_publication2014a::researcher_instantiation(instance):
    assert isinstance(instance, publication2014a::Researcher)

@given(instance=publication2014a::Researcher_strategy)
def test_publication2014a::researcher_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=publication2014a::Researcher_strategy)
def test_publication2014a::researcher_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=publication2014a::Researcher_strategy)
def test_publication2014a::researcher_position_type(instance):
    assert isinstance(instance.position, str)


@given(instance=publication2014a::Researcher_strategy)
def test_publication2014a::researcher_position_setter(instance):
    original = instance.position
    instance.position = original
    assert instance.position == original

@given(instance=publication2014a::Researcher_strategy)
def test_publication2014a::researcher_forName_type(instance):
    assert isinstance(instance.forName, str)


@given(instance=publication2014a::Researcher_strategy)
def test_publication2014a::researcher_forName_setter(instance):
    original = instance.forName
    instance.forName = original
    assert instance.forName == original

@given(instance=publication2014a::Sequence_strategy)
@settings(max_examples=50)
def test_publication2014a::sequence_instantiation(instance):
    assert isinstance(instance, publication2014a::Sequence)

@given(instance=publication2014a::Sequence_strategy)
def test_publication2014a::sequence_sequenceType_type(instance):
    assert isinstance(instance.sequenceType, str)


@given(instance=publication2014a::Sequence_strategy)
def test_publication2014a::sequence_sequenceType_setter(instance):
    original = instance.sequenceType
    instance.sequenceType = original
    assert instance.sequenceType == original

@given(instance=Named_strategy)
@settings(max_examples=50)
def test_named_instantiation(instance):
    assert isinstance(instance, Named)

@given(instance=publication2014a::Paragraph_strategy)
@settings(max_examples=50)
def test_publication2014a::paragraph_instantiation(instance):
    assert isinstance(instance, publication2014a::Paragraph)

@given(instance=publication2014a::Paragraph_strategy)
def test_publication2014a::paragraph_content_type(instance):
    assert isinstance(instance.content, str)


@given(instance=publication2014a::Paragraph_strategy)
def test_publication2014a::paragraph_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original

@given(instance=publication2014a::Paper_strategy)
@settings(max_examples=50)
def test_publication2014a::paper_instantiation(instance):
    assert isinstance(instance, publication2014a::Paper)

@given(instance=publication2014a::ReviewNote_strategy)
@settings(max_examples=50)
def test_publication2014a::reviewnote_instantiation(instance):
    assert isinstance(instance, publication2014a::ReviewNote)

@given(instance=publication2014a::ReviewNote_strategy)
def test_publication2014a::reviewnote_content_type(instance):
    assert isinstance(instance.content, str)


@given(instance=publication2014a::ReviewNote_strategy)
def test_publication2014a::reviewnote_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original

@given(instance=publication2014a::PublicationStructure_strategy)
@settings(max_examples=50)
def test_publication2014a::publicationstructure_instantiation(instance):
    assert isinstance(instance, publication2014a::PublicationStructure)

@given(instance=publication2014a::PublicationProcess_strategy)
@settings(max_examples=50)
def test_publication2014a::publicationprocess_instantiation(instance):
    assert isinstance(instance, publication2014a::PublicationProcess)

@given(instance=publication2014a::PublicationProcess_strategy)
def test_publication2014a::publicationprocess_maxTime_type(instance):
    assert isinstance(instance.maxTime, int)


@given(instance=publication2014a::PublicationProcess_strategy)
def test_publication2014a::publicationprocess_maxTime_setter(instance):
    original = instance.maxTime
    instance.maxTime = original
    assert instance.maxTime == original

@given(instance=publication2014a::PublicationProcess_strategy)
def test_publication2014a::publicationprocess_minTime_type(instance):
    assert isinstance(instance.minTime, int)


@given(instance=publication2014a::PublicationProcess_strategy)
def test_publication2014a::publicationprocess_minTime_setter(instance):
    original = instance.minTime
    instance.minTime = original
    assert instance.minTime == original

@given(instance=publication2014a::Rule_strategy)
@settings(max_examples=50)
def test_publication2014a::rule_instantiation(instance):
    assert isinstance(instance, publication2014a::Rule)

@given(instance=publication2014a::Rule_strategy)
def test_publication2014a::rule_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=publication2014a::Rule_strategy)
def test_publication2014a::rule_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=publication2014a::Rule_strategy)
def test_publication2014a::rule_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=publication2014a::Rule_strategy)
def test_publication2014a::rule_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=publication2014a::PublicationPhase_strategy)
@settings(max_examples=50)
def test_publication2014a::publicationphase_instantiation(instance):
    assert isinstance(instance, publication2014a::PublicationPhase)

@given(instance=publication2014a::PublicationPhase_strategy)
def test_publication2014a::publicationphase_minTime_type(instance):
    assert isinstance(instance.minTime, int)


@given(instance=publication2014a::PublicationPhase_strategy)
def test_publication2014a::publicationphase_minTime_setter(instance):
    original = instance.minTime
    instance.minTime = original
    assert instance.minTime == original

@given(instance=publication2014a::PublicationPhase_strategy)
def test_publication2014a::publicationphase_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=publication2014a::PublicationPhase_strategy)
def test_publication2014a::publicationphase_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=publication2014a::PublicationPhase_strategy)
def test_publication2014a::publicationphase_maxTime_type(instance):
    assert isinstance(instance.maxTime, int)


@given(instance=publication2014a::PublicationPhase_strategy)
def test_publication2014a::publicationphase_maxTime_setter(instance):
    original = instance.maxTime
    instance.maxTime = original
    assert instance.maxTime == original
