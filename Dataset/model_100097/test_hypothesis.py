import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    SubjectArea,
    Meta_Reviewer,
    ProgramCommittee,
    Conference,
    Person,
    cmt::User,
    cmt::ConferenceMember,
    Co_author,
    Decision,
    cmt::Rejection,
    cmt::Acceptance,
    cmt::ExternalReviewer,
    cmt::SubjectArea,
    Author,
    cmt::Co_author,
    cmt::AuthorNotReviewer,
    cmt::Bid,
    ProgramCommitteeMember,
    cmt::ProgramCommittee,
    cmt::Preference,
    cmt::Document,
    Chairman,
    cmt::ProgramCommitteeChair,
    Thing,
    cmt::Conference,
    Document,
    cmt::Paper,
    cmt::Review,
    cmt::Person,
    cmt::Decision,
    ExternalReviewer,
    Review,
    cmt::Meta-Review,
    Paper,
    cmt::PaperFullVersion,
    cmt::PaperAbstract,
    Bid,
    Administrator,
    User,
    cmt::Administrator,
    ConferenceMember,
    cmt::ProgramCommitteeMember,
    cmt::AssociatedChair,
    cmt::Chairman,
    cmt::Author,
    cmt::ConferenceChair,
    cmt::Reviewer,
    Reviewer,
    cmt::Meta-Reviewer,
    cmt::Thing,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_subjectarea_is_not_abstract():
    assert not inspect.isabstract(SubjectArea)


def test_subjectarea_constructor_exists():
    assert callable(SubjectArea.__init__)


def test_subjectarea_constructor_args():
    sig = inspect.signature(SubjectArea.__init__)
    params = list(sig.parameters.keys())



def test_meta_reviewer_is_not_abstract():
    assert not inspect.isabstract(Meta_Reviewer)


def test_meta_reviewer_constructor_exists():
    assert callable(Meta_Reviewer.__init__)


def test_meta_reviewer_constructor_args():
    sig = inspect.signature(Meta_Reviewer.__init__)
    params = list(sig.parameters.keys())



def test_programcommittee_is_not_abstract():
    assert not inspect.isabstract(ProgramCommittee)


def test_programcommittee_constructor_exists():
    assert callable(ProgramCommittee.__init__)


def test_programcommittee_constructor_args():
    sig = inspect.signature(ProgramCommittee.__init__)
    params = list(sig.parameters.keys())



def test_conference_is_not_abstract():
    assert not inspect.isabstract(Conference)


def test_conference_constructor_exists():
    assert callable(Conference.__init__)


def test_conference_constructor_args():
    sig = inspect.signature(Conference.__init__)
    params = list(sig.parameters.keys())



def test_person_is_not_abstract():
    assert not inspect.isabstract(Person)


def test_person_constructor_exists():
    assert callable(Person.__init__)


def test_person_constructor_args():
    sig = inspect.signature(Person.__init__)
    params = list(sig.parameters.keys())



def test_cmt::user_is_not_abstract():
    assert not inspect.isabstract(cmt::User)


def test_cmt::user_constructor_exists():
    assert callable(cmt::User.__init__)


def test_cmt::user_constructor_args():
    sig = inspect.signature(cmt::User.__init__)
    params = list(sig.parameters.keys())



def test_cmt::conferencemember_is_not_abstract():
    assert not inspect.isabstract(cmt::ConferenceMember)


def test_cmt::conferencemember_constructor_exists():
    assert callable(cmt::ConferenceMember.__init__)


def test_cmt::conferencemember_constructor_args():
    sig = inspect.signature(cmt::ConferenceMember.__init__)
    params = list(sig.parameters.keys())



def test_co_author_is_not_abstract():
    assert not inspect.isabstract(Co_author)


def test_co_author_constructor_exists():
    assert callable(Co_author.__init__)


def test_co_author_constructor_args():
    sig = inspect.signature(Co_author.__init__)
    params = list(sig.parameters.keys())



def test_decision_is_not_abstract():
    assert not inspect.isabstract(Decision)


def test_decision_constructor_exists():
    assert callable(Decision.__init__)


def test_decision_constructor_args():
    sig = inspect.signature(Decision.__init__)
    params = list(sig.parameters.keys())



def test_cmt::rejection_is_not_abstract():
    assert not inspect.isabstract(cmt::Rejection)


def test_cmt::rejection_constructor_exists():
    assert callable(cmt::Rejection.__init__)


def test_cmt::rejection_constructor_args():
    sig = inspect.signature(cmt::Rejection.__init__)
    params = list(sig.parameters.keys())



def test_cmt::acceptance_is_not_abstract():
    assert not inspect.isabstract(cmt::Acceptance)


def test_cmt::acceptance_constructor_exists():
    assert callable(cmt::Acceptance.__init__)


def test_cmt::acceptance_constructor_args():
    sig = inspect.signature(cmt::Acceptance.__init__)
    params = list(sig.parameters.keys())



def test_cmt::externalreviewer_is_not_abstract():
    assert not inspect.isabstract(cmt::ExternalReviewer)


def test_cmt::externalreviewer_constructor_exists():
    assert callable(cmt::ExternalReviewer.__init__)


def test_cmt::externalreviewer_constructor_args():
    sig = inspect.signature(cmt::ExternalReviewer.__init__)
    params = list(sig.parameters.keys())



def test_cmt::subjectarea_is_not_abstract():
    assert not inspect.isabstract(cmt::SubjectArea)


def test_cmt::subjectarea_constructor_exists():
    assert callable(cmt::SubjectArea.__init__)


def test_cmt::subjectarea_constructor_args():
    sig = inspect.signature(cmt::SubjectArea.__init__)
    params = list(sig.parameters.keys())



def test_author_is_not_abstract():
    assert not inspect.isabstract(Author)


def test_author_constructor_exists():
    assert callable(Author.__init__)


def test_author_constructor_args():
    sig = inspect.signature(Author.__init__)
    params = list(sig.parameters.keys())



def test_cmt::co_author_is_not_abstract():
    assert not inspect.isabstract(cmt::Co_author)


def test_cmt::co_author_constructor_exists():
    assert callable(cmt::Co_author.__init__)


def test_cmt::co_author_constructor_args():
    sig = inspect.signature(cmt::Co_author.__init__)
    params = list(sig.parameters.keys())



def test_cmt::authornotreviewer_is_not_abstract():
    assert not inspect.isabstract(cmt::AuthorNotReviewer)


def test_cmt::authornotreviewer_constructor_exists():
    assert callable(cmt::AuthorNotReviewer.__init__)


def test_cmt::authornotreviewer_constructor_args():
    sig = inspect.signature(cmt::AuthorNotReviewer.__init__)
    params = list(sig.parameters.keys())



def test_cmt::bid_is_not_abstract():
    assert not inspect.isabstract(cmt::Bid)


def test_cmt::bid_constructor_exists():
    assert callable(cmt::Bid.__init__)


def test_cmt::bid_constructor_args():
    sig = inspect.signature(cmt::Bid.__init__)
    params = list(sig.parameters.keys())



def test_programcommitteemember_is_not_abstract():
    assert not inspect.isabstract(ProgramCommitteeMember)


def test_programcommitteemember_constructor_exists():
    assert callable(ProgramCommitteeMember.__init__)


def test_programcommitteemember_constructor_args():
    sig = inspect.signature(ProgramCommitteeMember.__init__)
    params = list(sig.parameters.keys())



def test_cmt::programcommittee_is_not_abstract():
    assert not inspect.isabstract(cmt::ProgramCommittee)


def test_cmt::programcommittee_constructor_exists():
    assert callable(cmt::ProgramCommittee.__init__)


def test_cmt::programcommittee_constructor_args():
    sig = inspect.signature(cmt::ProgramCommittee.__init__)
    params = list(sig.parameters.keys())



def test_cmt::preference_is_not_abstract():
    assert not inspect.isabstract(cmt::Preference)


def test_cmt::preference_constructor_exists():
    assert callable(cmt::Preference.__init__)


def test_cmt::preference_constructor_args():
    sig = inspect.signature(cmt::Preference.__init__)
    params = list(sig.parameters.keys())



def test_cmt::document_is_not_abstract():
    assert not inspect.isabstract(cmt::Document)


def test_cmt::document_constructor_exists():
    assert callable(cmt::Document.__init__)


def test_cmt::document_constructor_args():
    sig = inspect.signature(cmt::Document.__init__)
    params = list(sig.parameters.keys())



def test_chairman_is_not_abstract():
    assert not inspect.isabstract(Chairman)


def test_chairman_constructor_exists():
    assert callable(Chairman.__init__)


def test_chairman_constructor_args():
    sig = inspect.signature(Chairman.__init__)
    params = list(sig.parameters.keys())



def test_cmt::programcommitteechair_is_not_abstract():
    assert not inspect.isabstract(cmt::ProgramCommitteeChair)


def test_cmt::programcommitteechair_constructor_exists():
    assert callable(cmt::ProgramCommitteeChair.__init__)


def test_cmt::programcommitteechair_constructor_args():
    sig = inspect.signature(cmt::ProgramCommitteeChair.__init__)
    params = list(sig.parameters.keys())



def test_thing_is_not_abstract():
    assert not inspect.isabstract(Thing)


def test_thing_constructor_exists():
    assert callable(Thing.__init__)


def test_thing_constructor_args():
    sig = inspect.signature(Thing.__init__)
    params = list(sig.parameters.keys())



def test_cmt::conference_is_not_abstract():
    assert not inspect.isabstract(cmt::Conference)


def test_cmt::conference_constructor_exists():
    assert callable(cmt::Conference.__init__)


def test_cmt::conference_constructor_args():
    sig = inspect.signature(cmt::Conference.__init__)
    params = list(sig.parameters.keys())
    assert "reviewsPerPaper" in params, "Missing parameter 'reviewsPerPaper'"
    assert "siteURL" in params, "Missing parameter 'siteURL'"
    assert "logoURL" in params, "Missing parameter 'logoURL'"
    assert "date" in params, "Missing parameter 'date'"
    assert "acceptsHardcopySubmissions" in params, "Missing parameter 'acceptsHardcopySubmissions'"

def test_cmt::conference_has_reviewsPerPaper():
    assert hasattr(cmt::Conference, "reviewsPerPaper")
    descriptor = None
    for klass in cmt::Conference.__mro__:
        if "reviewsPerPaper" in klass.__dict__:
            descriptor = klass.__dict__["reviewsPerPaper"]
            break
    assert isinstance(descriptor, property)

def test_cmt::conference_has_siteURL():
    assert hasattr(cmt::Conference, "siteURL")
    descriptor = None
    for klass in cmt::Conference.__mro__:
        if "siteURL" in klass.__dict__:
            descriptor = klass.__dict__["siteURL"]
            break
    assert isinstance(descriptor, property)

def test_cmt::conference_has_logoURL():
    assert hasattr(cmt::Conference, "logoURL")
    descriptor = None
    for klass in cmt::Conference.__mro__:
        if "logoURL" in klass.__dict__:
            descriptor = klass.__dict__["logoURL"]
            break
    assert isinstance(descriptor, property)

def test_cmt::conference_has_date():
    assert hasattr(cmt::Conference, "date")
    descriptor = None
    for klass in cmt::Conference.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)

def test_cmt::conference_has_acceptsHardcopySubmissions():
    assert hasattr(cmt::Conference, "acceptsHardcopySubmissions")
    descriptor = None
    for klass in cmt::Conference.__mro__:
        if "acceptsHardcopySubmissions" in klass.__dict__:
            descriptor = klass.__dict__["acceptsHardcopySubmissions"]
            break
    assert isinstance(descriptor, property)



def test_document_is_not_abstract():
    assert not inspect.isabstract(Document)


def test_document_constructor_exists():
    assert callable(Document.__init__)


def test_document_constructor_args():
    sig = inspect.signature(Document.__init__)
    params = list(sig.parameters.keys())



def test_cmt::paper_is_not_abstract():
    assert not inspect.isabstract(cmt::Paper)


def test_cmt::paper_constructor_exists():
    assert callable(cmt::Paper.__init__)


def test_cmt::paper_constructor_args():
    sig = inspect.signature(cmt::Paper.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "paperID" in params, "Missing parameter 'paperID'"

def test_cmt::paper_has_title():
    assert hasattr(cmt::Paper, "title")
    descriptor = None
    for klass in cmt::Paper.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_cmt::paper_has_paperID():
    assert hasattr(cmt::Paper, "paperID")
    descriptor = None
    for klass in cmt::Paper.__mro__:
        if "paperID" in klass.__dict__:
            descriptor = klass.__dict__["paperID"]
            break
    assert isinstance(descriptor, property)



def test_cmt::review_is_not_abstract():
    assert not inspect.isabstract(cmt::Review)


def test_cmt::review_constructor_exists():
    assert callable(cmt::Review.__init__)


def test_cmt::review_constructor_args():
    sig = inspect.signature(cmt::Review.__init__)
    params = list(sig.parameters.keys())



def test_cmt::person_is_not_abstract():
    assert not inspect.isabstract(cmt::Person)


def test_cmt::person_constructor_exists():
    assert callable(cmt::Person.__init__)


def test_cmt::person_constructor_args():
    sig = inspect.signature(cmt::Person.__init__)
    params = list(sig.parameters.keys())
    assert "email" in params, "Missing parameter 'email'"

def test_cmt::person_has_email():
    assert hasattr(cmt::Person, "email")
    descriptor = None
    for klass in cmt::Person.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)



def test_cmt::decision_is_not_abstract():
    assert not inspect.isabstract(cmt::Decision)


def test_cmt::decision_constructor_exists():
    assert callable(cmt::Decision.__init__)


def test_cmt::decision_constructor_args():
    sig = inspect.signature(cmt::Decision.__init__)
    params = list(sig.parameters.keys())



def test_externalreviewer_is_not_abstract():
    assert not inspect.isabstract(ExternalReviewer)


def test_externalreviewer_constructor_exists():
    assert callable(ExternalReviewer.__init__)


def test_externalreviewer_constructor_args():
    sig = inspect.signature(ExternalReviewer.__init__)
    params = list(sig.parameters.keys())



def test_review_is_not_abstract():
    assert not inspect.isabstract(Review)


def test_review_constructor_exists():
    assert callable(Review.__init__)


def test_review_constructor_args():
    sig = inspect.signature(Review.__init__)
    params = list(sig.parameters.keys())



def test_cmt::meta-review_is_not_abstract():
    assert not inspect.isabstract(cmt::Meta-Review)


def test_cmt::meta-review_constructor_exists():
    assert callable(cmt::Meta-Review.__init__)


def test_cmt::meta-review_constructor_args():
    sig = inspect.signature(cmt::Meta-Review.__init__)
    params = list(sig.parameters.keys())



def test_paper_is_not_abstract():
    assert not inspect.isabstract(Paper)


def test_paper_constructor_exists():
    assert callable(Paper.__init__)


def test_paper_constructor_args():
    sig = inspect.signature(Paper.__init__)
    params = list(sig.parameters.keys())



def test_cmt::paperfullversion_is_not_abstract():
    assert not inspect.isabstract(cmt::PaperFullVersion)


def test_cmt::paperfullversion_constructor_exists():
    assert callable(cmt::PaperFullVersion.__init__)


def test_cmt::paperfullversion_constructor_args():
    sig = inspect.signature(cmt::PaperFullVersion.__init__)
    params = list(sig.parameters.keys())



def test_cmt::paperabstract_is_not_abstract():
    assert not inspect.isabstract(cmt::PaperAbstract)


def test_cmt::paperabstract_constructor_exists():
    assert callable(cmt::PaperAbstract.__init__)


def test_cmt::paperabstract_constructor_args():
    sig = inspect.signature(cmt::PaperAbstract.__init__)
    params = list(sig.parameters.keys())



def test_bid_is_not_abstract():
    assert not inspect.isabstract(Bid)


def test_bid_constructor_exists():
    assert callable(Bid.__init__)


def test_bid_constructor_args():
    sig = inspect.signature(Bid.__init__)
    params = list(sig.parameters.keys())



def test_administrator_is_not_abstract():
    assert not inspect.isabstract(Administrator)


def test_administrator_constructor_exists():
    assert callable(Administrator.__init__)


def test_administrator_constructor_args():
    sig = inspect.signature(Administrator.__init__)
    params = list(sig.parameters.keys())



def test_user_is_not_abstract():
    assert not inspect.isabstract(User)


def test_user_constructor_exists():
    assert callable(User.__init__)


def test_user_constructor_args():
    sig = inspect.signature(User.__init__)
    params = list(sig.parameters.keys())



def test_cmt::administrator_is_not_abstract():
    assert not inspect.isabstract(cmt::Administrator)


def test_cmt::administrator_constructor_exists():
    assert callable(cmt::Administrator.__init__)


def test_cmt::administrator_constructor_args():
    sig = inspect.signature(cmt::Administrator.__init__)
    params = list(sig.parameters.keys())



def test_conferencemember_is_not_abstract():
    assert not inspect.isabstract(ConferenceMember)


def test_conferencemember_constructor_exists():
    assert callable(ConferenceMember.__init__)


def test_conferencemember_constructor_args():
    sig = inspect.signature(ConferenceMember.__init__)
    params = list(sig.parameters.keys())



def test_cmt::programcommitteemember_is_not_abstract():
    assert not inspect.isabstract(cmt::ProgramCommitteeMember)


def test_cmt::programcommitteemember_constructor_exists():
    assert callable(cmt::ProgramCommitteeMember.__init__)


def test_cmt::programcommitteemember_constructor_args():
    sig = inspect.signature(cmt::ProgramCommitteeMember.__init__)
    params = list(sig.parameters.keys())
    assert "maxPapers" in params, "Missing parameter 'maxPapers'"

def test_cmt::programcommitteemember_has_maxPapers():
    assert hasattr(cmt::ProgramCommitteeMember, "maxPapers")
    descriptor = None
    for klass in cmt::ProgramCommitteeMember.__mro__:
        if "maxPapers" in klass.__dict__:
            descriptor = klass.__dict__["maxPapers"]
            break
    assert isinstance(descriptor, property)



def test_cmt::associatedchair_is_not_abstract():
    assert not inspect.isabstract(cmt::AssociatedChair)


def test_cmt::associatedchair_constructor_exists():
    assert callable(cmt::AssociatedChair.__init__)


def test_cmt::associatedchair_constructor_args():
    sig = inspect.signature(cmt::AssociatedChair.__init__)
    params = list(sig.parameters.keys())



def test_cmt::chairman_is_not_abstract():
    assert not inspect.isabstract(cmt::Chairman)


def test_cmt::chairman_constructor_exists():
    assert callable(cmt::Chairman.__init__)


def test_cmt::chairman_constructor_args():
    sig = inspect.signature(cmt::Chairman.__init__)
    params = list(sig.parameters.keys())



def test_cmt::author_is_not_abstract():
    assert not inspect.isabstract(cmt::Author)


def test_cmt::author_constructor_exists():
    assert callable(cmt::Author.__init__)


def test_cmt::author_constructor_args():
    sig = inspect.signature(cmt::Author.__init__)
    params = list(sig.parameters.keys())



def test_cmt::conferencechair_is_not_abstract():
    assert not inspect.isabstract(cmt::ConferenceChair)


def test_cmt::conferencechair_constructor_exists():
    assert callable(cmt::ConferenceChair.__init__)


def test_cmt::conferencechair_constructor_args():
    sig = inspect.signature(cmt::ConferenceChair.__init__)
    params = list(sig.parameters.keys())



def test_cmt::reviewer_is_not_abstract():
    assert not inspect.isabstract(cmt::Reviewer)


def test_cmt::reviewer_constructor_exists():
    assert callable(cmt::Reviewer.__init__)


def test_cmt::reviewer_constructor_args():
    sig = inspect.signature(cmt::Reviewer.__init__)
    params = list(sig.parameters.keys())



def test_reviewer_is_not_abstract():
    assert not inspect.isabstract(Reviewer)


def test_reviewer_constructor_exists():
    assert callable(Reviewer.__init__)


def test_reviewer_constructor_args():
    sig = inspect.signature(Reviewer.__init__)
    params = list(sig.parameters.keys())



def test_cmt::meta-reviewer_is_not_abstract():
    assert not inspect.isabstract(cmt::Meta-Reviewer)


def test_cmt::meta-reviewer_constructor_exists():
    assert callable(cmt::Meta-Reviewer.__init__)


def test_cmt::meta-reviewer_constructor_args():
    sig = inspect.signature(cmt::Meta-Reviewer.__init__)
    params = list(sig.parameters.keys())



def test_cmt::thing_is_not_abstract():
    assert not inspect.isabstract(cmt::Thing)


def test_cmt::thing_constructor_exists():
    assert callable(cmt::Thing.__init__)


def test_cmt::thing_constructor_args():
    sig = inspect.signature(cmt::Thing.__init__)
    params = list(sig.parameters.keys())


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
SubjectArea_strategy = st.builds(
    SubjectArea,
)
Meta_Reviewer_strategy = st.builds(
    Meta_Reviewer,
)
ProgramCommittee_strategy = st.builds(
    ProgramCommittee,
)
Conference_strategy = st.builds(
    Conference,
)
Person_strategy = st.builds(
    Person,
)
cmt::User_strategy = st.builds(
    cmt::User,
)
cmt::ConferenceMember_strategy = st.builds(
    cmt::ConferenceMember,
)
Co_author_strategy = st.builds(
    Co_author,
)
Decision_strategy = st.builds(
    Decision,
)
cmt::Rejection_strategy = st.builds(
    cmt::Rejection,
)
cmt::Acceptance_strategy = st.builds(
    cmt::Acceptance,
)
cmt::ExternalReviewer_strategy = st.builds(
    cmt::ExternalReviewer,
)
cmt::SubjectArea_strategy = st.builds(
    cmt::SubjectArea,
)
Author_strategy = st.builds(
    Author,
)
cmt::Co_author_strategy = st.builds(
    cmt::Co_author,
)
cmt::AuthorNotReviewer_strategy = st.builds(
    cmt::AuthorNotReviewer,
)
cmt::Bid_strategy = st.builds(
    cmt::Bid,
)
ProgramCommitteeMember_strategy = st.builds(
    ProgramCommitteeMember,
)
cmt::ProgramCommittee_strategy = st.builds(
    cmt::ProgramCommittee,
)
cmt::Preference_strategy = st.builds(
    cmt::Preference,
)
cmt::Document_strategy = st.builds(
    cmt::Document,
)
Chairman_strategy = st.builds(
    Chairman,
)
cmt::ProgramCommitteeChair_strategy = st.builds(
    cmt::ProgramCommitteeChair,
)
Thing_strategy = st.builds(
    Thing,
)
cmt::Conference_strategy = st.builds(
    cmt::Conference,
    reviewsPerPaper=
        safe_text,
    siteURL=
        safe_text,
    logoURL=
        safe_text,
    date=
        safe_text,
    acceptsHardcopySubmissions=
        safe_text
)
Document_strategy = st.builds(
    Document,
)
cmt::Paper_strategy = st.builds(
    cmt::Paper,
    title=
        safe_text,
    paperID=
        safe_text
)
cmt::Review_strategy = st.builds(
    cmt::Review,
)
cmt::Person_strategy = st.builds(
    cmt::Person,
    email=
        safe_text
)
cmt::Decision_strategy = st.builds(
    cmt::Decision,
)
ExternalReviewer_strategy = st.builds(
    ExternalReviewer,
)
Review_strategy = st.builds(
    Review,
)
cmt::Meta-Review_strategy = st.builds(
    cmt::Meta-Review,
)
Paper_strategy = st.builds(
    Paper,
)
cmt::PaperFullVersion_strategy = st.builds(
    cmt::PaperFullVersion,
)
cmt::PaperAbstract_strategy = st.builds(
    cmt::PaperAbstract,
)
Bid_strategy = st.builds(
    Bid,
)
Administrator_strategy = st.builds(
    Administrator,
)
User_strategy = st.builds(
    User,
)
cmt::Administrator_strategy = st.builds(
    cmt::Administrator,
)
ConferenceMember_strategy = st.builds(
    ConferenceMember,
)
cmt::ProgramCommitteeMember_strategy = st.builds(
    cmt::ProgramCommitteeMember,
    maxPapers=
        safe_text
)
cmt::AssociatedChair_strategy = st.builds(
    cmt::AssociatedChair,
)
cmt::Chairman_strategy = st.builds(
    cmt::Chairman,
)
cmt::Author_strategy = st.builds(
    cmt::Author,
)
cmt::ConferenceChair_strategy = st.builds(
    cmt::ConferenceChair,
)
cmt::Reviewer_strategy = st.builds(
    cmt::Reviewer,
)
Reviewer_strategy = st.builds(
    Reviewer,
)
cmt::Meta-Reviewer_strategy = st.builds(
    cmt::Meta-Reviewer,
)
cmt::Thing_strategy = st.builds(
    cmt::Thing,
)

@given(instance=SubjectArea_strategy)
@settings(max_examples=50)
def test_subjectarea_instantiation(instance):
    assert isinstance(instance, SubjectArea)

@given(instance=Meta_Reviewer_strategy)
@settings(max_examples=50)
def test_meta_reviewer_instantiation(instance):
    assert isinstance(instance, Meta_Reviewer)

@given(instance=ProgramCommittee_strategy)
@settings(max_examples=50)
def test_programcommittee_instantiation(instance):
    assert isinstance(instance, ProgramCommittee)

@given(instance=Conference_strategy)
@settings(max_examples=50)
def test_conference_instantiation(instance):
    assert isinstance(instance, Conference)

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)

@given(instance=cmt::User_strategy)
@settings(max_examples=50)
def test_cmt::user_instantiation(instance):
    assert isinstance(instance, cmt::User)

@given(instance=cmt::ConferenceMember_strategy)
@settings(max_examples=50)
def test_cmt::conferencemember_instantiation(instance):
    assert isinstance(instance, cmt::ConferenceMember)

@given(instance=Co_author_strategy)
@settings(max_examples=50)
def test_co_author_instantiation(instance):
    assert isinstance(instance, Co_author)

@given(instance=Decision_strategy)
@settings(max_examples=50)
def test_decision_instantiation(instance):
    assert isinstance(instance, Decision)

@given(instance=cmt::Rejection_strategy)
@settings(max_examples=50)
def test_cmt::rejection_instantiation(instance):
    assert isinstance(instance, cmt::Rejection)

@given(instance=cmt::Acceptance_strategy)
@settings(max_examples=50)
def test_cmt::acceptance_instantiation(instance):
    assert isinstance(instance, cmt::Acceptance)

@given(instance=cmt::ExternalReviewer_strategy)
@settings(max_examples=50)
def test_cmt::externalreviewer_instantiation(instance):
    assert isinstance(instance, cmt::ExternalReviewer)

@given(instance=cmt::SubjectArea_strategy)
@settings(max_examples=50)
def test_cmt::subjectarea_instantiation(instance):
    assert isinstance(instance, cmt::SubjectArea)

@given(instance=Author_strategy)
@settings(max_examples=50)
def test_author_instantiation(instance):
    assert isinstance(instance, Author)

@given(instance=cmt::Co_author_strategy)
@settings(max_examples=50)
def test_cmt::co_author_instantiation(instance):
    assert isinstance(instance, cmt::Co_author)

@given(instance=cmt::AuthorNotReviewer_strategy)
@settings(max_examples=50)
def test_cmt::authornotreviewer_instantiation(instance):
    assert isinstance(instance, cmt::AuthorNotReviewer)

@given(instance=cmt::Bid_strategy)
@settings(max_examples=50)
def test_cmt::bid_instantiation(instance):
    assert isinstance(instance, cmt::Bid)

@given(instance=ProgramCommitteeMember_strategy)
@settings(max_examples=50)
def test_programcommitteemember_instantiation(instance):
    assert isinstance(instance, ProgramCommitteeMember)

@given(instance=cmt::ProgramCommittee_strategy)
@settings(max_examples=50)
def test_cmt::programcommittee_instantiation(instance):
    assert isinstance(instance, cmt::ProgramCommittee)

@given(instance=cmt::Preference_strategy)
@settings(max_examples=50)
def test_cmt::preference_instantiation(instance):
    assert isinstance(instance, cmt::Preference)

@given(instance=cmt::Document_strategy)
@settings(max_examples=50)
def test_cmt::document_instantiation(instance):
    assert isinstance(instance, cmt::Document)

@given(instance=Chairman_strategy)
@settings(max_examples=50)
def test_chairman_instantiation(instance):
    assert isinstance(instance, Chairman)

@given(instance=cmt::ProgramCommitteeChair_strategy)
@settings(max_examples=50)
def test_cmt::programcommitteechair_instantiation(instance):
    assert isinstance(instance, cmt::ProgramCommitteeChair)

@given(instance=Thing_strategy)
@settings(max_examples=50)
def test_thing_instantiation(instance):
    assert isinstance(instance, Thing)

@given(instance=cmt::Conference_strategy)
@settings(max_examples=50)
def test_cmt::conference_instantiation(instance):
    assert isinstance(instance, cmt::Conference)

@given(instance=cmt::Conference_strategy)
def test_cmt::conference_reviewsPerPaper_type(instance):
    assert isinstance(instance.reviewsPerPaper, str)


@given(instance=cmt::Conference_strategy)
def test_cmt::conference_reviewsPerPaper_setter(instance):
    original = instance.reviewsPerPaper
    instance.reviewsPerPaper = original
    assert instance.reviewsPerPaper == original

@given(instance=cmt::Conference_strategy)
def test_cmt::conference_siteURL_type(instance):
    assert isinstance(instance.siteURL, str)


@given(instance=cmt::Conference_strategy)
def test_cmt::conference_siteURL_setter(instance):
    original = instance.siteURL
    instance.siteURL = original
    assert instance.siteURL == original

@given(instance=cmt::Conference_strategy)
def test_cmt::conference_logoURL_type(instance):
    assert isinstance(instance.logoURL, str)


@given(instance=cmt::Conference_strategy)
def test_cmt::conference_logoURL_setter(instance):
    original = instance.logoURL
    instance.logoURL = original
    assert instance.logoURL == original

@given(instance=cmt::Conference_strategy)
def test_cmt::conference_date_type(instance):
    assert isinstance(instance.date, str)


@given(instance=cmt::Conference_strategy)
def test_cmt::conference_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original

@given(instance=cmt::Conference_strategy)
def test_cmt::conference_acceptsHardcopySubmissions_type(instance):
    assert isinstance(instance.acceptsHardcopySubmissions, str)


@given(instance=cmt::Conference_strategy)
def test_cmt::conference_acceptsHardcopySubmissions_setter(instance):
    original = instance.acceptsHardcopySubmissions
    instance.acceptsHardcopySubmissions = original
    assert instance.acceptsHardcopySubmissions == original

@given(instance=Document_strategy)
@settings(max_examples=50)
def test_document_instantiation(instance):
    assert isinstance(instance, Document)

@given(instance=cmt::Paper_strategy)
@settings(max_examples=50)
def test_cmt::paper_instantiation(instance):
    assert isinstance(instance, cmt::Paper)

@given(instance=cmt::Paper_strategy)
def test_cmt::paper_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=cmt::Paper_strategy)
def test_cmt::paper_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=cmt::Paper_strategy)
def test_cmt::paper_paperID_type(instance):
    assert isinstance(instance.paperID, str)


@given(instance=cmt::Paper_strategy)
def test_cmt::paper_paperID_setter(instance):
    original = instance.paperID
    instance.paperID = original
    assert instance.paperID == original

@given(instance=cmt::Review_strategy)
@settings(max_examples=50)
def test_cmt::review_instantiation(instance):
    assert isinstance(instance, cmt::Review)

@given(instance=cmt::Person_strategy)
@settings(max_examples=50)
def test_cmt::person_instantiation(instance):
    assert isinstance(instance, cmt::Person)

@given(instance=cmt::Person_strategy)
def test_cmt::person_email_type(instance):
    assert isinstance(instance.email, str)


@given(instance=cmt::Person_strategy)
def test_cmt::person_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original

@given(instance=cmt::Decision_strategy)
@settings(max_examples=50)
def test_cmt::decision_instantiation(instance):
    assert isinstance(instance, cmt::Decision)

@given(instance=ExternalReviewer_strategy)
@settings(max_examples=50)
def test_externalreviewer_instantiation(instance):
    assert isinstance(instance, ExternalReviewer)

@given(instance=Review_strategy)
@settings(max_examples=50)
def test_review_instantiation(instance):
    assert isinstance(instance, Review)

@given(instance=cmt::Meta-Review_strategy)
@settings(max_examples=50)
def test_cmt::meta-review_instantiation(instance):
    assert isinstance(instance, cmt::Meta-Review)

@given(instance=Paper_strategy)
@settings(max_examples=50)
def test_paper_instantiation(instance):
    assert isinstance(instance, Paper)

@given(instance=cmt::PaperFullVersion_strategy)
@settings(max_examples=50)
def test_cmt::paperfullversion_instantiation(instance):
    assert isinstance(instance, cmt::PaperFullVersion)

@given(instance=cmt::PaperAbstract_strategy)
@settings(max_examples=50)
def test_cmt::paperabstract_instantiation(instance):
    assert isinstance(instance, cmt::PaperAbstract)

@given(instance=Bid_strategy)
@settings(max_examples=50)
def test_bid_instantiation(instance):
    assert isinstance(instance, Bid)

@given(instance=Administrator_strategy)
@settings(max_examples=50)
def test_administrator_instantiation(instance):
    assert isinstance(instance, Administrator)

@given(instance=User_strategy)
@settings(max_examples=50)
def test_user_instantiation(instance):
    assert isinstance(instance, User)

@given(instance=cmt::Administrator_strategy)
@settings(max_examples=50)
def test_cmt::administrator_instantiation(instance):
    assert isinstance(instance, cmt::Administrator)

@given(instance=ConferenceMember_strategy)
@settings(max_examples=50)
def test_conferencemember_instantiation(instance):
    assert isinstance(instance, ConferenceMember)

@given(instance=cmt::ProgramCommitteeMember_strategy)
@settings(max_examples=50)
def test_cmt::programcommitteemember_instantiation(instance):
    assert isinstance(instance, cmt::ProgramCommitteeMember)

@given(instance=cmt::ProgramCommitteeMember_strategy)
def test_cmt::programcommitteemember_maxPapers_type(instance):
    assert isinstance(instance.maxPapers, str)


@given(instance=cmt::ProgramCommitteeMember_strategy)
def test_cmt::programcommitteemember_maxPapers_setter(instance):
    original = instance.maxPapers
    instance.maxPapers = original
    assert instance.maxPapers == original

@given(instance=cmt::AssociatedChair_strategy)
@settings(max_examples=50)
def test_cmt::associatedchair_instantiation(instance):
    assert isinstance(instance, cmt::AssociatedChair)

@given(instance=cmt::Chairman_strategy)
@settings(max_examples=50)
def test_cmt::chairman_instantiation(instance):
    assert isinstance(instance, cmt::Chairman)

@given(instance=cmt::Author_strategy)
@settings(max_examples=50)
def test_cmt::author_instantiation(instance):
    assert isinstance(instance, cmt::Author)

@given(instance=cmt::ConferenceChair_strategy)
@settings(max_examples=50)
def test_cmt::conferencechair_instantiation(instance):
    assert isinstance(instance, cmt::ConferenceChair)

@given(instance=cmt::Reviewer_strategy)
@settings(max_examples=50)
def test_cmt::reviewer_instantiation(instance):
    assert isinstance(instance, cmt::Reviewer)

@given(instance=Reviewer_strategy)
@settings(max_examples=50)
def test_reviewer_instantiation(instance):
    assert isinstance(instance, Reviewer)

@given(instance=cmt::Meta-Reviewer_strategy)
@settings(max_examples=50)
def test_cmt::meta-reviewer_instantiation(instance):
    assert isinstance(instance, cmt::Meta-Reviewer)

@given(instance=cmt::Thing_strategy)
@settings(max_examples=50)
def test_cmt::thing_instantiation(instance):
    assert isinstance(instance, cmt::Thing)
