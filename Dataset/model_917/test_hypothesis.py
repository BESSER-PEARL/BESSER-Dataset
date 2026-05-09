import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Counted,
    publication2014::Researcher,
    publication2014::Sequence,
    publication2014::Rule,
    publication2014::PublicationPhase,
    Named,
    publication2014::Paragraph,
    publication2014::ReviewNote,
    publication2014::Paper,
    publication2014::PublicationProcess,
    publication2014::PublicationStructure,
    publication2014::PlaceHolder,
    PlaceHolder,
    publication2014::PlaceHolderRs,
    publication2014::PlaceHolderPP,
    publication2014::Labelled,
    publication2014::Counted,
    publication2014::Named,
    publication2014::PublicationSystem,
    publication2014::PlaceHolderRule,
    Labelled,
    publication2014::Progress,
    publication2014::Write,
    publication2014::Review,
    publication2014::PlaceHolderRn,
    SequenceType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_counted_is_not_abstract():
    assert not inspect.isabstract(Counted)


def test_counted_constructor_exists():
    assert callable(Counted.__init__)


def test_counted_constructor_args():
    sig = inspect.signature(Counted.__init__)
    params = list(sig.parameters.keys())



def test_publication2014::researcher_is_not_abstract():
    assert not inspect.isabstract(publication2014::Researcher)


def test_publication2014::researcher_constructor_exists():
    assert callable(publication2014::Researcher.__init__)


def test_publication2014::researcher_constructor_args():
    sig = inspect.signature(publication2014::Researcher.__init__)
    params = list(sig.parameters.keys())
    assert "position" in params, "Missing parameter 'position'"
    assert "name" in params, "Missing parameter 'name'"
    assert "forName" in params, "Missing parameter 'forName'"

def test_publication2014::researcher_has_position():
    assert hasattr(publication2014::Researcher, "position")
    descriptor = None
    for klass in publication2014::Researcher.__mro__:
        if "position" in klass.__dict__:
            descriptor = klass.__dict__["position"]
            break
    assert isinstance(descriptor, property)

def test_publication2014::researcher_has_name():
    assert hasattr(publication2014::Researcher, "name")
    descriptor = None
    for klass in publication2014::Researcher.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_publication2014::researcher_has_forName():
    assert hasattr(publication2014::Researcher, "forName")
    descriptor = None
    for klass in publication2014::Researcher.__mro__:
        if "forName" in klass.__dict__:
            descriptor = klass.__dict__["forName"]
            break
    assert isinstance(descriptor, property)



def test_publication2014::sequence_is_not_abstract():
    assert not inspect.isabstract(publication2014::Sequence)


def test_publication2014::sequence_constructor_exists():
    assert callable(publication2014::Sequence.__init__)


def test_publication2014::sequence_constructor_args():
    sig = inspect.signature(publication2014::Sequence.__init__)
    params = list(sig.parameters.keys())
    assert "sequenceType" in params, "Missing parameter 'sequenceType'"

def test_publication2014::sequence_has_sequenceType():
    assert hasattr(publication2014::Sequence, "sequenceType")
    descriptor = None
    for klass in publication2014::Sequence.__mro__:
        if "sequenceType" in klass.__dict__:
            descriptor = klass.__dict__["sequenceType"]
            break
    assert isinstance(descriptor, property)



def test_publication2014::rule_is_not_abstract():
    assert not inspect.isabstract(publication2014::Rule)


def test_publication2014::rule_constructor_exists():
    assert callable(publication2014::Rule.__init__)


def test_publication2014::rule_constructor_args():
    sig = inspect.signature(publication2014::Rule.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"
    assert "text" in params, "Missing parameter 'text'"

def test_publication2014::rule_has_key():
    assert hasattr(publication2014::Rule, "key")
    descriptor = None
    for klass in publication2014::Rule.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_publication2014::rule_has_text():
    assert hasattr(publication2014::Rule, "text")
    descriptor = None
    for klass in publication2014::Rule.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_publication2014::publicationphase_is_not_abstract():
    assert not inspect.isabstract(publication2014::PublicationPhase)


def test_publication2014::publicationphase_constructor_exists():
    assert callable(publication2014::PublicationPhase.__init__)


def test_publication2014::publicationphase_constructor_args():
    sig = inspect.signature(publication2014::PublicationPhase.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "minTime" in params, "Missing parameter 'minTime'"
    assert "maxTime" in params, "Missing parameter 'maxTime'"

def test_publication2014::publicationphase_has_name():
    assert hasattr(publication2014::PublicationPhase, "name")
    descriptor = None
    for klass in publication2014::PublicationPhase.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_publication2014::publicationphase_has_minTime():
    assert hasattr(publication2014::PublicationPhase, "minTime")
    descriptor = None
    for klass in publication2014::PublicationPhase.__mro__:
        if "minTime" in klass.__dict__:
            descriptor = klass.__dict__["minTime"]
            break
    assert isinstance(descriptor, property)

def test_publication2014::publicationphase_has_maxTime():
    assert hasattr(publication2014::PublicationPhase, "maxTime")
    descriptor = None
    for klass in publication2014::PublicationPhase.__mro__:
        if "maxTime" in klass.__dict__:
            descriptor = klass.__dict__["maxTime"]
            break
    assert isinstance(descriptor, property)



def test_named_is_not_abstract():
    assert not inspect.isabstract(Named)


def test_named_constructor_exists():
    assert callable(Named.__init__)


def test_named_constructor_args():
    sig = inspect.signature(Named.__init__)
    params = list(sig.parameters.keys())



def test_publication2014::paragraph_is_not_abstract():
    assert not inspect.isabstract(publication2014::Paragraph)


def test_publication2014::paragraph_constructor_exists():
    assert callable(publication2014::Paragraph.__init__)


def test_publication2014::paragraph_constructor_args():
    sig = inspect.signature(publication2014::Paragraph.__init__)
    params = list(sig.parameters.keys())
    assert "content" in params, "Missing parameter 'content'"

def test_publication2014::paragraph_has_content():
    assert hasattr(publication2014::Paragraph, "content")
    descriptor = None
    for klass in publication2014::Paragraph.__mro__:
        if "content" in klass.__dict__:
            descriptor = klass.__dict__["content"]
            break
    assert isinstance(descriptor, property)



def test_publication2014::reviewnote_is_not_abstract():
    assert not inspect.isabstract(publication2014::ReviewNote)


def test_publication2014::reviewnote_constructor_exists():
    assert callable(publication2014::ReviewNote.__init__)


def test_publication2014::reviewnote_constructor_args():
    sig = inspect.signature(publication2014::ReviewNote.__init__)
    params = list(sig.parameters.keys())
    assert "content" in params, "Missing parameter 'content'"

def test_publication2014::reviewnote_has_content():
    assert hasattr(publication2014::ReviewNote, "content")
    descriptor = None
    for klass in publication2014::ReviewNote.__mro__:
        if "content" in klass.__dict__:
            descriptor = klass.__dict__["content"]
            break
    assert isinstance(descriptor, property)



def test_publication2014::paper_is_not_abstract():
    assert not inspect.isabstract(publication2014::Paper)


def test_publication2014::paper_constructor_exists():
    assert callable(publication2014::Paper.__init__)


def test_publication2014::paper_constructor_args():
    sig = inspect.signature(publication2014::Paper.__init__)
    params = list(sig.parameters.keys())



def test_publication2014::publicationprocess_is_not_abstract():
    assert not inspect.isabstract(publication2014::PublicationProcess)


def test_publication2014::publicationprocess_constructor_exists():
    assert callable(publication2014::PublicationProcess.__init__)


def test_publication2014::publicationprocess_constructor_args():
    sig = inspect.signature(publication2014::PublicationProcess.__init__)
    params = list(sig.parameters.keys())
    assert "minTime" in params, "Missing parameter 'minTime'"
    assert "maxTime" in params, "Missing parameter 'maxTime'"

def test_publication2014::publicationprocess_has_minTime():
    assert hasattr(publication2014::PublicationProcess, "minTime")
    descriptor = None
    for klass in publication2014::PublicationProcess.__mro__:
        if "minTime" in klass.__dict__:
            descriptor = klass.__dict__["minTime"]
            break
    assert isinstance(descriptor, property)

def test_publication2014::publicationprocess_has_maxTime():
    assert hasattr(publication2014::PublicationProcess, "maxTime")
    descriptor = None
    for klass in publication2014::PublicationProcess.__mro__:
        if "maxTime" in klass.__dict__:
            descriptor = klass.__dict__["maxTime"]
            break
    assert isinstance(descriptor, property)



def test_publication2014::publicationstructure_is_not_abstract():
    assert not inspect.isabstract(publication2014::PublicationStructure)


def test_publication2014::publicationstructure_constructor_exists():
    assert callable(publication2014::PublicationStructure.__init__)


def test_publication2014::publicationstructure_constructor_args():
    sig = inspect.signature(publication2014::PublicationStructure.__init__)
    params = list(sig.parameters.keys())



def test_publication2014::placeholder_is_not_abstract():
    assert not inspect.isabstract(publication2014::PlaceHolder)


def test_publication2014::placeholder_constructor_exists():
    assert callable(publication2014::PlaceHolder.__init__)


def test_publication2014::placeholder_constructor_args():
    sig = inspect.signature(publication2014::PlaceHolder.__init__)
    params = list(sig.parameters.keys())



def test_placeholder_is_not_abstract():
    assert not inspect.isabstract(PlaceHolder)


def test_placeholder_constructor_exists():
    assert callable(PlaceHolder.__init__)


def test_placeholder_constructor_args():
    sig = inspect.signature(PlaceHolder.__init__)
    params = list(sig.parameters.keys())



def test_publication2014::placeholderrs_is_not_abstract():
    assert not inspect.isabstract(publication2014::PlaceHolderRs)


def test_publication2014::placeholderrs_constructor_exists():
    assert callable(publication2014::PlaceHolderRs.__init__)


def test_publication2014::placeholderrs_constructor_args():
    sig = inspect.signature(publication2014::PlaceHolderRs.__init__)
    params = list(sig.parameters.keys())



def test_publication2014::placeholderpp_is_not_abstract():
    assert not inspect.isabstract(publication2014::PlaceHolderPP)


def test_publication2014::placeholderpp_constructor_exists():
    assert callable(publication2014::PlaceHolderPP.__init__)


def test_publication2014::placeholderpp_constructor_args():
    sig = inspect.signature(publication2014::PlaceHolderPP.__init__)
    params = list(sig.parameters.keys())



def test_publication2014::labelled_is_not_abstract():
    assert not inspect.isabstract(publication2014::Labelled)


def test_publication2014::labelled_constructor_exists():
    assert callable(publication2014::Labelled.__init__)


def test_publication2014::labelled_constructor_args():
    sig = inspect.signature(publication2014::Labelled.__init__)
    params = list(sig.parameters.keys())
    assert "lname" in params, "Missing parameter 'lname'"

def test_publication2014::labelled_has_lname():
    assert hasattr(publication2014::Labelled, "lname")
    descriptor = None
    for klass in publication2014::Labelled.__mro__:
        if "lname" in klass.__dict__:
            descriptor = klass.__dict__["lname"]
            break
    assert isinstance(descriptor, property)



def test_publication2014::counted_is_not_abstract():
    assert not inspect.isabstract(publication2014::Counted)


def test_publication2014::counted_constructor_exists():
    assert callable(publication2014::Counted.__init__)


def test_publication2014::counted_constructor_args():
    sig = inspect.signature(publication2014::Counted.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_publication2014::counted_has_id():
    assert hasattr(publication2014::Counted, "id")
    descriptor = None
    for klass in publication2014::Counted.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_publication2014::named_is_not_abstract():
    assert not inspect.isabstract(publication2014::Named)


def test_publication2014::named_constructor_exists():
    assert callable(publication2014::Named.__init__)


def test_publication2014::named_constructor_args():
    sig = inspect.signature(publication2014::Named.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_publication2014::named_has_name():
    assert hasattr(publication2014::Named, "name")
    descriptor = None
    for klass in publication2014::Named.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_publication2014::publicationsystem_is_not_abstract():
    assert not inspect.isabstract(publication2014::PublicationSystem)


def test_publication2014::publicationsystem_constructor_exists():
    assert callable(publication2014::PublicationSystem.__init__)


def test_publication2014::publicationsystem_constructor_args():
    sig = inspect.signature(publication2014::PublicationSystem.__init__)
    params = list(sig.parameters.keys())



def test_publication2014::placeholderrule_is_not_abstract():
    assert not inspect.isabstract(publication2014::PlaceHolderRule)


def test_publication2014::placeholderrule_constructor_exists():
    assert callable(publication2014::PlaceHolderRule.__init__)


def test_publication2014::placeholderrule_constructor_args():
    sig = inspect.signature(publication2014::PlaceHolderRule.__init__)
    params = list(sig.parameters.keys())



def test_labelled_is_not_abstract():
    assert not inspect.isabstract(Labelled)


def test_labelled_constructor_exists():
    assert callable(Labelled.__init__)


def test_labelled_constructor_args():
    sig = inspect.signature(Labelled.__init__)
    params = list(sig.parameters.keys())



def test_publication2014::progress_is_not_abstract():
    assert not inspect.isabstract(publication2014::Progress)


def test_publication2014::progress_constructor_exists():
    assert callable(publication2014::Progress.__init__)


def test_publication2014::progress_constructor_args():
    sig = inspect.signature(publication2014::Progress.__init__)
    params = list(sig.parameters.keys())
    assert "time" in params, "Missing parameter 'time'"
    assert "percent" in params, "Missing parameter 'percent'"

def test_publication2014::progress_has_time():
    assert hasattr(publication2014::Progress, "time")
    descriptor = None
    for klass in publication2014::Progress.__mro__:
        if "time" in klass.__dict__:
            descriptor = klass.__dict__["time"]
            break
    assert isinstance(descriptor, property)

def test_publication2014::progress_has_percent():
    assert hasattr(publication2014::Progress, "percent")
    descriptor = None
    for klass in publication2014::Progress.__mro__:
        if "percent" in klass.__dict__:
            descriptor = klass.__dict__["percent"]
            break
    assert isinstance(descriptor, property)



def test_publication2014::write_is_not_abstract():
    assert not inspect.isabstract(publication2014::Write)


def test_publication2014::write_constructor_exists():
    assert callable(publication2014::Write.__init__)


def test_publication2014::write_constructor_args():
    sig = inspect.signature(publication2014::Write.__init__)
    params = list(sig.parameters.keys())



def test_publication2014::review_is_not_abstract():
    assert not inspect.isabstract(publication2014::Review)


def test_publication2014::review_constructor_exists():
    assert callable(publication2014::Review.__init__)


def test_publication2014::review_constructor_args():
    sig = inspect.signature(publication2014::Review.__init__)
    params = list(sig.parameters.keys())



def test_publication2014::placeholderrn_is_not_abstract():
    assert not inspect.isabstract(publication2014::PlaceHolderRn)


def test_publication2014::placeholderrn_constructor_exists():
    assert callable(publication2014::PlaceHolderRn.__init__)


def test_publication2014::placeholderrn_constructor_args():
    sig = inspect.signature(publication2014::PlaceHolderRn.__init__)
    params = list(sig.parameters.keys())

def test_sequencetype_exists():
    # Check that the Enumeration exists
    assert SequenceType is not None

def test_sequencetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SequenceType]
    expected_literals = [
        "finishToFinish",
        "finishToStart",
        "startToFinish",
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
Counted_strategy = st.builds(
    Counted,
)
publication2014::Researcher_strategy = st.builds(
    publication2014::Researcher,
    position=
        safe_text,
    name=
        safe_text,
    forName=
        safe_text
)
publication2014::Sequence_strategy = st.builds(
    publication2014::Sequence,
    sequenceType=
        safe_text
)
publication2014::Rule_strategy = st.builds(
    publication2014::Rule,
    key=
        safe_text,
    text=
        safe_text
)
publication2014::PublicationPhase_strategy = st.builds(
    publication2014::PublicationPhase,
    name=
        safe_text,
    minTime=
        st.integers(),
    maxTime=
        st.integers()
)
Named_strategy = st.builds(
    Named,
)
publication2014::Paragraph_strategy = st.builds(
    publication2014::Paragraph,
    content=
        safe_text
)
publication2014::ReviewNote_strategy = st.builds(
    publication2014::ReviewNote,
    content=
        safe_text
)
publication2014::Paper_strategy = st.builds(
    publication2014::Paper,
)
publication2014::PublicationProcess_strategy = st.builds(
    publication2014::PublicationProcess,
    minTime=
        st.integers(),
    maxTime=
        st.integers()
)
publication2014::PublicationStructure_strategy = st.builds(
    publication2014::PublicationStructure,
)
publication2014::PlaceHolder_strategy = st.builds(
    publication2014::PlaceHolder,
)
PlaceHolder_strategy = st.builds(
    PlaceHolder,
)
publication2014::PlaceHolderRs_strategy = st.builds(
    publication2014::PlaceHolderRs,
)
publication2014::PlaceHolderPP_strategy = st.builds(
    publication2014::PlaceHolderPP,
)
publication2014::Labelled_strategy = st.builds(
    publication2014::Labelled,
    lname=
        safe_text
)
publication2014::Counted_strategy = st.builds(
    publication2014::Counted,
    id=
        st.integers()
)
publication2014::Named_strategy = st.builds(
    publication2014::Named,
    name=
        safe_text
)
publication2014::PublicationSystem_strategy = st.builds(
    publication2014::PublicationSystem,
)
publication2014::PlaceHolderRule_strategy = st.builds(
    publication2014::PlaceHolderRule,
)
Labelled_strategy = st.builds(
    Labelled,
)
publication2014::Progress_strategy = st.builds(
    publication2014::Progress,
    time=
        st.integers(),
    percent=
        st.integers()
)
publication2014::Write_strategy = st.builds(
    publication2014::Write,
)
publication2014::Review_strategy = st.builds(
    publication2014::Review,
)
publication2014::PlaceHolderRn_strategy = st.builds(
    publication2014::PlaceHolderRn,
)

@given(instance=Counted_strategy)
@settings(max_examples=50)
def test_counted_instantiation(instance):
    assert isinstance(instance, Counted)

@given(instance=publication2014::Researcher_strategy)
@settings(max_examples=50)
def test_publication2014::researcher_instantiation(instance):
    assert isinstance(instance, publication2014::Researcher)

@given(instance=publication2014::Researcher_strategy)
def test_publication2014::researcher_position_type(instance):
    assert isinstance(instance.position, str)


@given(instance=publication2014::Researcher_strategy)
def test_publication2014::researcher_position_setter(instance):
    original = instance.position
    instance.position = original
    assert instance.position == original

@given(instance=publication2014::Researcher_strategy)
def test_publication2014::researcher_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=publication2014::Researcher_strategy)
def test_publication2014::researcher_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=publication2014::Researcher_strategy)
def test_publication2014::researcher_forName_type(instance):
    assert isinstance(instance.forName, str)


@given(instance=publication2014::Researcher_strategy)
def test_publication2014::researcher_forName_setter(instance):
    original = instance.forName
    instance.forName = original
    assert instance.forName == original

@given(instance=publication2014::Sequence_strategy)
@settings(max_examples=50)
def test_publication2014::sequence_instantiation(instance):
    assert isinstance(instance, publication2014::Sequence)

@given(instance=publication2014::Sequence_strategy)
def test_publication2014::sequence_sequenceType_type(instance):
    assert isinstance(instance.sequenceType, str)


@given(instance=publication2014::Sequence_strategy)
def test_publication2014::sequence_sequenceType_setter(instance):
    original = instance.sequenceType
    instance.sequenceType = original
    assert instance.sequenceType == original

@given(instance=publication2014::Rule_strategy)
@settings(max_examples=50)
def test_publication2014::rule_instantiation(instance):
    assert isinstance(instance, publication2014::Rule)

@given(instance=publication2014::Rule_strategy)
def test_publication2014::rule_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=publication2014::Rule_strategy)
def test_publication2014::rule_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=publication2014::Rule_strategy)
def test_publication2014::rule_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=publication2014::Rule_strategy)
def test_publication2014::rule_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=publication2014::PublicationPhase_strategy)
@settings(max_examples=50)
def test_publication2014::publicationphase_instantiation(instance):
    assert isinstance(instance, publication2014::PublicationPhase)

@given(instance=publication2014::PublicationPhase_strategy)
def test_publication2014::publicationphase_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=publication2014::PublicationPhase_strategy)
def test_publication2014::publicationphase_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=publication2014::PublicationPhase_strategy)
def test_publication2014::publicationphase_minTime_type(instance):
    assert isinstance(instance.minTime, int)


@given(instance=publication2014::PublicationPhase_strategy)
def test_publication2014::publicationphase_minTime_setter(instance):
    original = instance.minTime
    instance.minTime = original
    assert instance.minTime == original

@given(instance=publication2014::PublicationPhase_strategy)
def test_publication2014::publicationphase_maxTime_type(instance):
    assert isinstance(instance.maxTime, int)


@given(instance=publication2014::PublicationPhase_strategy)
def test_publication2014::publicationphase_maxTime_setter(instance):
    original = instance.maxTime
    instance.maxTime = original
    assert instance.maxTime == original

@given(instance=Named_strategy)
@settings(max_examples=50)
def test_named_instantiation(instance):
    assert isinstance(instance, Named)

@given(instance=publication2014::Paragraph_strategy)
@settings(max_examples=50)
def test_publication2014::paragraph_instantiation(instance):
    assert isinstance(instance, publication2014::Paragraph)

@given(instance=publication2014::Paragraph_strategy)
def test_publication2014::paragraph_content_type(instance):
    assert isinstance(instance.content, str)


@given(instance=publication2014::Paragraph_strategy)
def test_publication2014::paragraph_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original

@given(instance=publication2014::ReviewNote_strategy)
@settings(max_examples=50)
def test_publication2014::reviewnote_instantiation(instance):
    assert isinstance(instance, publication2014::ReviewNote)

@given(instance=publication2014::ReviewNote_strategy)
def test_publication2014::reviewnote_content_type(instance):
    assert isinstance(instance.content, str)


@given(instance=publication2014::ReviewNote_strategy)
def test_publication2014::reviewnote_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original

@given(instance=publication2014::Paper_strategy)
@settings(max_examples=50)
def test_publication2014::paper_instantiation(instance):
    assert isinstance(instance, publication2014::Paper)

@given(instance=publication2014::PublicationProcess_strategy)
@settings(max_examples=50)
def test_publication2014::publicationprocess_instantiation(instance):
    assert isinstance(instance, publication2014::PublicationProcess)

@given(instance=publication2014::PublicationProcess_strategy)
def test_publication2014::publicationprocess_minTime_type(instance):
    assert isinstance(instance.minTime, int)


@given(instance=publication2014::PublicationProcess_strategy)
def test_publication2014::publicationprocess_minTime_setter(instance):
    original = instance.minTime
    instance.minTime = original
    assert instance.minTime == original

@given(instance=publication2014::PublicationProcess_strategy)
def test_publication2014::publicationprocess_maxTime_type(instance):
    assert isinstance(instance.maxTime, int)


@given(instance=publication2014::PublicationProcess_strategy)
def test_publication2014::publicationprocess_maxTime_setter(instance):
    original = instance.maxTime
    instance.maxTime = original
    assert instance.maxTime == original

@given(instance=publication2014::PublicationStructure_strategy)
@settings(max_examples=50)
def test_publication2014::publicationstructure_instantiation(instance):
    assert isinstance(instance, publication2014::PublicationStructure)

@given(instance=publication2014::PlaceHolder_strategy)
@settings(max_examples=50)
def test_publication2014::placeholder_instantiation(instance):
    assert isinstance(instance, publication2014::PlaceHolder)

@given(instance=PlaceHolder_strategy)
@settings(max_examples=50)
def test_placeholder_instantiation(instance):
    assert isinstance(instance, PlaceHolder)

@given(instance=publication2014::PlaceHolderRs_strategy)
@settings(max_examples=50)
def test_publication2014::placeholderrs_instantiation(instance):
    assert isinstance(instance, publication2014::PlaceHolderRs)

@given(instance=publication2014::PlaceHolderPP_strategy)
@settings(max_examples=50)
def test_publication2014::placeholderpp_instantiation(instance):
    assert isinstance(instance, publication2014::PlaceHolderPP)

@given(instance=publication2014::Labelled_strategy)
@settings(max_examples=50)
def test_publication2014::labelled_instantiation(instance):
    assert isinstance(instance, publication2014::Labelled)

@given(instance=publication2014::Labelled_strategy)
def test_publication2014::labelled_lname_type(instance):
    assert isinstance(instance.lname, str)


@given(instance=publication2014::Labelled_strategy)
def test_publication2014::labelled_lname_setter(instance):
    original = instance.lname
    instance.lname = original
    assert instance.lname == original

@given(instance=publication2014::Counted_strategy)
@settings(max_examples=50)
def test_publication2014::counted_instantiation(instance):
    assert isinstance(instance, publication2014::Counted)

@given(instance=publication2014::Counted_strategy)
def test_publication2014::counted_id_type(instance):
    assert isinstance(instance.id, int)


@given(instance=publication2014::Counted_strategy)
def test_publication2014::counted_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=publication2014::Named_strategy)
@settings(max_examples=50)
def test_publication2014::named_instantiation(instance):
    assert isinstance(instance, publication2014::Named)

@given(instance=publication2014::Named_strategy)
def test_publication2014::named_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=publication2014::Named_strategy)
def test_publication2014::named_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=publication2014::PublicationSystem_strategy)
@settings(max_examples=50)
def test_publication2014::publicationsystem_instantiation(instance):
    assert isinstance(instance, publication2014::PublicationSystem)

@given(instance=publication2014::PlaceHolderRule_strategy)
@settings(max_examples=50)
def test_publication2014::placeholderrule_instantiation(instance):
    assert isinstance(instance, publication2014::PlaceHolderRule)

@given(instance=Labelled_strategy)
@settings(max_examples=50)
def test_labelled_instantiation(instance):
    assert isinstance(instance, Labelled)

@given(instance=publication2014::Progress_strategy)
@settings(max_examples=50)
def test_publication2014::progress_instantiation(instance):
    assert isinstance(instance, publication2014::Progress)

@given(instance=publication2014::Progress_strategy)
def test_publication2014::progress_time_type(instance):
    assert isinstance(instance.time, int)


@given(instance=publication2014::Progress_strategy)
def test_publication2014::progress_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original

@given(instance=publication2014::Progress_strategy)
def test_publication2014::progress_percent_type(instance):
    assert isinstance(instance.percent, int)


@given(instance=publication2014::Progress_strategy)
def test_publication2014::progress_percent_setter(instance):
    original = instance.percent
    instance.percent = original
    assert instance.percent == original

@given(instance=publication2014::Write_strategy)
@settings(max_examples=50)
def test_publication2014::write_instantiation(instance):
    assert isinstance(instance, publication2014::Write)

@given(instance=publication2014::Review_strategy)
@settings(max_examples=50)
def test_publication2014::review_instantiation(instance):
    assert isinstance(instance, publication2014::Review)

@given(instance=publication2014::PlaceHolderRn_strategy)
@settings(max_examples=50)
def test_publication2014::placeholderrn_instantiation(instance):
    assert isinstance(instance, publication2014::PlaceHolderRn)
