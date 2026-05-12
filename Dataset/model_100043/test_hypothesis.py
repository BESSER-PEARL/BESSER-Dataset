import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    research13::Labelled,
    research13::Counted,
    research13::Named,
    research13::PaperKeyword,
    research13::Collaboration,
    Labelled,
    research13::Progress,
    Counted,
    Named,
    research13::ReviewNote,
    research13::PublicationSystem,
    research13::PublicationStructure,
    research13::KnowledgeManager,
    research13::Paragraph,
    research13::Keyword,
    research13::Position,
    research13::PublicationProcess,
    research13::Skill,
    research13::Paper,
    research13::Review,
    research13::Write,
    research13::Researcher,
    research13::Phase,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_research13::labelled_is_not_abstract():
    assert not inspect.isabstract(research13::Labelled)


def test_research13::labelled_constructor_exists():
    assert callable(research13::Labelled.__init__)


def test_research13::labelled_constructor_args():
    sig = inspect.signature(research13::Labelled.__init__)
    params = list(sig.parameters.keys())
    assert "lname" in params, "Missing parameter 'lname'"

def test_research13::labelled_has_lname():
    assert hasattr(research13::Labelled, "lname")
    descriptor = None
    for klass in research13::Labelled.__mro__:
        if "lname" in klass.__dict__:
            descriptor = klass.__dict__["lname"]
            break
    assert isinstance(descriptor, property)



def test_research13::counted_is_not_abstract():
    assert not inspect.isabstract(research13::Counted)


def test_research13::counted_constructor_exists():
    assert callable(research13::Counted.__init__)


def test_research13::counted_constructor_args():
    sig = inspect.signature(research13::Counted.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_research13::counted_has_id():
    assert hasattr(research13::Counted, "id")
    descriptor = None
    for klass in research13::Counted.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_research13::named_is_not_abstract():
    assert not inspect.isabstract(research13::Named)


def test_research13::named_constructor_exists():
    assert callable(research13::Named.__init__)


def test_research13::named_constructor_args():
    sig = inspect.signature(research13::Named.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_research13::named_has_name():
    assert hasattr(research13::Named, "name")
    descriptor = None
    for klass in research13::Named.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_research13::paperkeyword_is_not_abstract():
    assert not inspect.isabstract(research13::PaperKeyword)


def test_research13::paperkeyword_constructor_exists():
    assert callable(research13::PaperKeyword.__init__)


def test_research13::paperkeyword_constructor_args():
    sig = inspect.signature(research13::PaperKeyword.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"

def test_research13::paperkeyword_has_weight():
    assert hasattr(research13::PaperKeyword, "weight")
    descriptor = None
    for klass in research13::PaperKeyword.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)



def test_research13::collaboration_is_not_abstract():
    assert not inspect.isabstract(research13::Collaboration)


def test_research13::collaboration_constructor_exists():
    assert callable(research13::Collaboration.__init__)


def test_research13::collaboration_constructor_args():
    sig = inspect.signature(research13::Collaboration.__init__)
    params = list(sig.parameters.keys())
    assert "ratio" in params, "Missing parameter 'ratio'"

def test_research13::collaboration_has_ratio():
    assert hasattr(research13::Collaboration, "ratio")
    descriptor = None
    for klass in research13::Collaboration.__mro__:
        if "ratio" in klass.__dict__:
            descriptor = klass.__dict__["ratio"]
            break
    assert isinstance(descriptor, property)



def test_labelled_is_not_abstract():
    assert not inspect.isabstract(Labelled)


def test_labelled_constructor_exists():
    assert callable(Labelled.__init__)


def test_labelled_constructor_args():
    sig = inspect.signature(Labelled.__init__)
    params = list(sig.parameters.keys())



def test_research13::progress_is_not_abstract():
    assert not inspect.isabstract(research13::Progress)


def test_research13::progress_constructor_exists():
    assert callable(research13::Progress.__init__)


def test_research13::progress_constructor_args():
    sig = inspect.signature(research13::Progress.__init__)
    params = list(sig.parameters.keys())
    assert "percent" in params, "Missing parameter 'percent'"

def test_research13::progress_has_percent():
    assert hasattr(research13::Progress, "percent")
    descriptor = None
    for klass in research13::Progress.__mro__:
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



def test_named_is_not_abstract():
    assert not inspect.isabstract(Named)


def test_named_constructor_exists():
    assert callable(Named.__init__)


def test_named_constructor_args():
    sig = inspect.signature(Named.__init__)
    params = list(sig.parameters.keys())



def test_research13::reviewnote_is_not_abstract():
    assert not inspect.isabstract(research13::ReviewNote)


def test_research13::reviewnote_constructor_exists():
    assert callable(research13::ReviewNote.__init__)


def test_research13::reviewnote_constructor_args():
    sig = inspect.signature(research13::ReviewNote.__init__)
    params = list(sig.parameters.keys())
    assert "content" in params, "Missing parameter 'content'"

def test_research13::reviewnote_has_content():
    assert hasattr(research13::ReviewNote, "content")
    descriptor = None
    for klass in research13::ReviewNote.__mro__:
        if "content" in klass.__dict__:
            descriptor = klass.__dict__["content"]
            break
    assert isinstance(descriptor, property)



def test_research13::publicationsystem_is_not_abstract():
    assert not inspect.isabstract(research13::PublicationSystem)


def test_research13::publicationsystem_constructor_exists():
    assert callable(research13::PublicationSystem.__init__)


def test_research13::publicationsystem_constructor_args():
    sig = inspect.signature(research13::PublicationSystem.__init__)
    params = list(sig.parameters.keys())



def test_research13::publicationstructure_is_not_abstract():
    assert not inspect.isabstract(research13::PublicationStructure)


def test_research13::publicationstructure_constructor_exists():
    assert callable(research13::PublicationStructure.__init__)


def test_research13::publicationstructure_constructor_args():
    sig = inspect.signature(research13::PublicationStructure.__init__)
    params = list(sig.parameters.keys())



def test_research13::knowledgemanager_is_not_abstract():
    assert not inspect.isabstract(research13::KnowledgeManager)


def test_research13::knowledgemanager_constructor_exists():
    assert callable(research13::KnowledgeManager.__init__)


def test_research13::knowledgemanager_constructor_args():
    sig = inspect.signature(research13::KnowledgeManager.__init__)
    params = list(sig.parameters.keys())



def test_research13::paragraph_is_not_abstract():
    assert not inspect.isabstract(research13::Paragraph)


def test_research13::paragraph_constructor_exists():
    assert callable(research13::Paragraph.__init__)


def test_research13::paragraph_constructor_args():
    sig = inspect.signature(research13::Paragraph.__init__)
    params = list(sig.parameters.keys())
    assert "content" in params, "Missing parameter 'content'"

def test_research13::paragraph_has_content():
    assert hasattr(research13::Paragraph, "content")
    descriptor = None
    for klass in research13::Paragraph.__mro__:
        if "content" in klass.__dict__:
            descriptor = klass.__dict__["content"]
            break
    assert isinstance(descriptor, property)



def test_research13::keyword_is_not_abstract():
    assert not inspect.isabstract(research13::Keyword)


def test_research13::keyword_constructor_exists():
    assert callable(research13::Keyword.__init__)


def test_research13::keyword_constructor_args():
    sig = inspect.signature(research13::Keyword.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"

def test_research13::keyword_has_description():
    assert hasattr(research13::Keyword, "description")
    descriptor = None
    for klass in research13::Keyword.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_research13::position_is_not_abstract():
    assert not inspect.isabstract(research13::Position)


def test_research13::position_constructor_exists():
    assert callable(research13::Position.__init__)


def test_research13::position_constructor_args():
    sig = inspect.signature(research13::Position.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"

def test_research13::position_has_description():
    assert hasattr(research13::Position, "description")
    descriptor = None
    for klass in research13::Position.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_research13::publicationprocess_is_not_abstract():
    assert not inspect.isabstract(research13::PublicationProcess)


def test_research13::publicationprocess_constructor_exists():
    assert callable(research13::PublicationProcess.__init__)


def test_research13::publicationprocess_constructor_args():
    sig = inspect.signature(research13::PublicationProcess.__init__)
    params = list(sig.parameters.keys())
    assert "minTime" in params, "Missing parameter 'minTime'"
    assert "maxTime" in params, "Missing parameter 'maxTime'"

def test_research13::publicationprocess_has_minTime():
    assert hasattr(research13::PublicationProcess, "minTime")
    descriptor = None
    for klass in research13::PublicationProcess.__mro__:
        if "minTime" in klass.__dict__:
            descriptor = klass.__dict__["minTime"]
            break
    assert isinstance(descriptor, property)

def test_research13::publicationprocess_has_maxTime():
    assert hasattr(research13::PublicationProcess, "maxTime")
    descriptor = None
    for klass in research13::PublicationProcess.__mro__:
        if "maxTime" in klass.__dict__:
            descriptor = klass.__dict__["maxTime"]
            break
    assert isinstance(descriptor, property)



def test_research13::skill_is_not_abstract():
    assert not inspect.isabstract(research13::Skill)


def test_research13::skill_constructor_exists():
    assert callable(research13::Skill.__init__)


def test_research13::skill_constructor_args():
    sig = inspect.signature(research13::Skill.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"

def test_research13::skill_has_description():
    assert hasattr(research13::Skill, "description")
    descriptor = None
    for klass in research13::Skill.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_research13::paper_is_not_abstract():
    assert not inspect.isabstract(research13::Paper)


def test_research13::paper_constructor_exists():
    assert callable(research13::Paper.__init__)


def test_research13::paper_constructor_args():
    sig = inspect.signature(research13::Paper.__init__)
    params = list(sig.parameters.keys())



def test_research13::review_is_not_abstract():
    assert not inspect.isabstract(research13::Review)


def test_research13::review_constructor_exists():
    assert callable(research13::Review.__init__)


def test_research13::review_constructor_args():
    sig = inspect.signature(research13::Review.__init__)
    params = list(sig.parameters.keys())
    assert "date" in params, "Missing parameter 'date'"

def test_research13::review_has_date():
    assert hasattr(research13::Review, "date")
    descriptor = None
    for klass in research13::Review.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)



def test_research13::write_is_not_abstract():
    assert not inspect.isabstract(research13::Write)


def test_research13::write_constructor_exists():
    assert callable(research13::Write.__init__)


def test_research13::write_constructor_args():
    sig = inspect.signature(research13::Write.__init__)
    params = list(sig.parameters.keys())
    assert "timeSpent" in params, "Missing parameter 'timeSpent'"

def test_research13::write_has_timeSpent():
    assert hasattr(research13::Write, "timeSpent")
    descriptor = None
    for klass in research13::Write.__mro__:
        if "timeSpent" in klass.__dict__:
            descriptor = klass.__dict__["timeSpent"]
            break
    assert isinstance(descriptor, property)



def test_research13::researcher_is_not_abstract():
    assert not inspect.isabstract(research13::Researcher)


def test_research13::researcher_constructor_exists():
    assert callable(research13::Researcher.__init__)


def test_research13::researcher_constructor_args():
    sig = inspect.signature(research13::Researcher.__init__)
    params = list(sig.parameters.keys())
    assert "forName" in params, "Missing parameter 'forName'"
    assert "name" in params, "Missing parameter 'name'"

def test_research13::researcher_has_forName():
    assert hasattr(research13::Researcher, "forName")
    descriptor = None
    for klass in research13::Researcher.__mro__:
        if "forName" in klass.__dict__:
            descriptor = klass.__dict__["forName"]
            break
    assert isinstance(descriptor, property)

def test_research13::researcher_has_name():
    assert hasattr(research13::Researcher, "name")
    descriptor = None
    for klass in research13::Researcher.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_research13::phase_is_not_abstract():
    assert not inspect.isabstract(research13::Phase)


def test_research13::phase_constructor_exists():
    assert callable(research13::Phase.__init__)


def test_research13::phase_constructor_args():
    sig = inspect.signature(research13::Phase.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_research13::phase_has_name():
    assert hasattr(research13::Phase, "name")
    descriptor = None
    for klass in research13::Phase.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)


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
research13::Labelled_strategy = st.builds(
    research13::Labelled,
    lname=
        safe_text
)
research13::Counted_strategy = st.builds(
    research13::Counted,
    id=
        st.integers()
)
research13::Named_strategy = st.builds(
    research13::Named,
    name=
        safe_text
)
research13::PaperKeyword_strategy = st.builds(
    research13::PaperKeyword,
    weight=
        st.integers()
)
research13::Collaboration_strategy = st.builds(
    research13::Collaboration,
    ratio=
        st.integers()
)
Labelled_strategy = st.builds(
    Labelled,
)
research13::Progress_strategy = st.builds(
    research13::Progress,
    percent=
        st.integers()
)
Counted_strategy = st.builds(
    Counted,
)
Named_strategy = st.builds(
    Named,
)
research13::ReviewNote_strategy = st.builds(
    research13::ReviewNote,
    content=
        safe_text
)
research13::PublicationSystem_strategy = st.builds(
    research13::PublicationSystem,
)
research13::PublicationStructure_strategy = st.builds(
    research13::PublicationStructure,
)
research13::KnowledgeManager_strategy = st.builds(
    research13::KnowledgeManager,
)
research13::Paragraph_strategy = st.builds(
    research13::Paragraph,
    content=
        safe_text
)
research13::Keyword_strategy = st.builds(
    research13::Keyword,
    description=
        safe_text
)
research13::Position_strategy = st.builds(
    research13::Position,
    description=
        safe_text
)
research13::PublicationProcess_strategy = st.builds(
    research13::PublicationProcess,
    minTime=
        st.integers(),
    maxTime=
        st.integers()
)
research13::Skill_strategy = st.builds(
    research13::Skill,
    description=
        safe_text
)
research13::Paper_strategy = st.builds(
    research13::Paper,
)
research13::Review_strategy = st.builds(
    research13::Review,
    date=
        st.dates()
)
research13::Write_strategy = st.builds(
    research13::Write,
    timeSpent=
        st.integers()
)
research13::Researcher_strategy = st.builds(
    research13::Researcher,
    forName=
        safe_text,
    name=
        safe_text
)
research13::Phase_strategy = st.builds(
    research13::Phase,
    name=
        safe_text
)

@given(instance=research13::Labelled_strategy)
@settings(max_examples=50)
def test_research13::labelled_instantiation(instance):
    assert isinstance(instance, research13::Labelled)

@given(instance=research13::Labelled_strategy)
def test_research13::labelled_lname_type(instance):
    assert isinstance(instance.lname, str)


@given(instance=research13::Labelled_strategy)
def test_research13::labelled_lname_setter(instance):
    original = instance.lname
    instance.lname = original
    assert instance.lname == original

@given(instance=research13::Counted_strategy)
@settings(max_examples=50)
def test_research13::counted_instantiation(instance):
    assert isinstance(instance, research13::Counted)

@given(instance=research13::Counted_strategy)
def test_research13::counted_id_type(instance):
    assert isinstance(instance.id, int)


@given(instance=research13::Counted_strategy)
def test_research13::counted_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=research13::Named_strategy)
@settings(max_examples=50)
def test_research13::named_instantiation(instance):
    assert isinstance(instance, research13::Named)

@given(instance=research13::Named_strategy)
def test_research13::named_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=research13::Named_strategy)
def test_research13::named_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=research13::PaperKeyword_strategy)
@settings(max_examples=50)
def test_research13::paperkeyword_instantiation(instance):
    assert isinstance(instance, research13::PaperKeyword)

@given(instance=research13::PaperKeyword_strategy)
def test_research13::paperkeyword_weight_type(instance):
    assert isinstance(instance.weight, int)


@given(instance=research13::PaperKeyword_strategy)
def test_research13::paperkeyword_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=research13::Collaboration_strategy)
@settings(max_examples=50)
def test_research13::collaboration_instantiation(instance):
    assert isinstance(instance, research13::Collaboration)

@given(instance=research13::Collaboration_strategy)
def test_research13::collaboration_ratio_type(instance):
    assert isinstance(instance.ratio, int)


@given(instance=research13::Collaboration_strategy)
def test_research13::collaboration_ratio_setter(instance):
    original = instance.ratio
    instance.ratio = original
    assert instance.ratio == original

@given(instance=Labelled_strategy)
@settings(max_examples=50)
def test_labelled_instantiation(instance):
    assert isinstance(instance, Labelled)

@given(instance=research13::Progress_strategy)
@settings(max_examples=50)
def test_research13::progress_instantiation(instance):
    assert isinstance(instance, research13::Progress)

@given(instance=research13::Progress_strategy)
def test_research13::progress_percent_type(instance):
    assert isinstance(instance.percent, int)


@given(instance=research13::Progress_strategy)
def test_research13::progress_percent_setter(instance):
    original = instance.percent
    instance.percent = original
    assert instance.percent == original

@given(instance=Counted_strategy)
@settings(max_examples=50)
def test_counted_instantiation(instance):
    assert isinstance(instance, Counted)

@given(instance=Named_strategy)
@settings(max_examples=50)
def test_named_instantiation(instance):
    assert isinstance(instance, Named)

@given(instance=research13::ReviewNote_strategy)
@settings(max_examples=50)
def test_research13::reviewnote_instantiation(instance):
    assert isinstance(instance, research13::ReviewNote)

@given(instance=research13::ReviewNote_strategy)
def test_research13::reviewnote_content_type(instance):
    assert isinstance(instance.content, str)


@given(instance=research13::ReviewNote_strategy)
def test_research13::reviewnote_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original

@given(instance=research13::PublicationSystem_strategy)
@settings(max_examples=50)
def test_research13::publicationsystem_instantiation(instance):
    assert isinstance(instance, research13::PublicationSystem)

@given(instance=research13::PublicationStructure_strategy)
@settings(max_examples=50)
def test_research13::publicationstructure_instantiation(instance):
    assert isinstance(instance, research13::PublicationStructure)

@given(instance=research13::KnowledgeManager_strategy)
@settings(max_examples=50)
def test_research13::knowledgemanager_instantiation(instance):
    assert isinstance(instance, research13::KnowledgeManager)

@given(instance=research13::Paragraph_strategy)
@settings(max_examples=50)
def test_research13::paragraph_instantiation(instance):
    assert isinstance(instance, research13::Paragraph)

@given(instance=research13::Paragraph_strategy)
def test_research13::paragraph_content_type(instance):
    assert isinstance(instance.content, str)


@given(instance=research13::Paragraph_strategy)
def test_research13::paragraph_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original

@given(instance=research13::Keyword_strategy)
@settings(max_examples=50)
def test_research13::keyword_instantiation(instance):
    assert isinstance(instance, research13::Keyword)

@given(instance=research13::Keyword_strategy)
def test_research13::keyword_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=research13::Keyword_strategy)
def test_research13::keyword_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=research13::Position_strategy)
@settings(max_examples=50)
def test_research13::position_instantiation(instance):
    assert isinstance(instance, research13::Position)

@given(instance=research13::Position_strategy)
def test_research13::position_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=research13::Position_strategy)
def test_research13::position_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=research13::PublicationProcess_strategy)
@settings(max_examples=50)
def test_research13::publicationprocess_instantiation(instance):
    assert isinstance(instance, research13::PublicationProcess)

@given(instance=research13::PublicationProcess_strategy)
def test_research13::publicationprocess_minTime_type(instance):
    assert isinstance(instance.minTime, int)


@given(instance=research13::PublicationProcess_strategy)
def test_research13::publicationprocess_minTime_setter(instance):
    original = instance.minTime
    instance.minTime = original
    assert instance.minTime == original

@given(instance=research13::PublicationProcess_strategy)
def test_research13::publicationprocess_maxTime_type(instance):
    assert isinstance(instance.maxTime, int)


@given(instance=research13::PublicationProcess_strategy)
def test_research13::publicationprocess_maxTime_setter(instance):
    original = instance.maxTime
    instance.maxTime = original
    assert instance.maxTime == original

@given(instance=research13::Skill_strategy)
@settings(max_examples=50)
def test_research13::skill_instantiation(instance):
    assert isinstance(instance, research13::Skill)

@given(instance=research13::Skill_strategy)
def test_research13::skill_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=research13::Skill_strategy)
def test_research13::skill_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=research13::Paper_strategy)
@settings(max_examples=50)
def test_research13::paper_instantiation(instance):
    assert isinstance(instance, research13::Paper)

@given(instance=research13::Review_strategy)
@settings(max_examples=50)
def test_research13::review_instantiation(instance):
    assert isinstance(instance, research13::Review)

@given(instance=research13::Review_strategy)
def test_research13::review_date_type(instance):
    assert isinstance(instance.date, date)


@given(instance=research13::Review_strategy)
def test_research13::review_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original

@given(instance=research13::Write_strategy)
@settings(max_examples=50)
def test_research13::write_instantiation(instance):
    assert isinstance(instance, research13::Write)

@given(instance=research13::Write_strategy)
def test_research13::write_timeSpent_type(instance):
    assert isinstance(instance.timeSpent, int)


@given(instance=research13::Write_strategy)
def test_research13::write_timeSpent_setter(instance):
    original = instance.timeSpent
    instance.timeSpent = original
    assert instance.timeSpent == original

@given(instance=research13::Researcher_strategy)
@settings(max_examples=50)
def test_research13::researcher_instantiation(instance):
    assert isinstance(instance, research13::Researcher)

@given(instance=research13::Researcher_strategy)
def test_research13::researcher_forName_type(instance):
    assert isinstance(instance.forName, str)


@given(instance=research13::Researcher_strategy)
def test_research13::researcher_forName_setter(instance):
    original = instance.forName
    instance.forName = original
    assert instance.forName == original

@given(instance=research13::Researcher_strategy)
def test_research13::researcher_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=research13::Researcher_strategy)
def test_research13::researcher_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=research13::Phase_strategy)
@settings(max_examples=50)
def test_research13::phase_instantiation(instance):
    assert isinstance(instance, research13::Phase)

@given(instance=research13::Phase_strategy)
def test_research13::phase_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=research13::Phase_strategy)
def test_research13::phase_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
