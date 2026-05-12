import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    SubjectArea,
    Meta_Reviewer,
    ProgramCommittee,
    Conference,
    Person,
    cmt_User,
    cmt_ConferenceMember,
    Co_author,
    Decision,
    cmt_Rejection,
    cmt_Acceptance,
    cmt_ExternalReviewer,
    cmt_SubjectArea,
    Author,
    cmt_Co_author,
    cmt_AuthorNotReviewer,
    cmt_Bid,
    ProgramCommitteeMember,
    cmt_ProgramCommittee,
    cmt_Preference,
    cmt_Document,
    Chairman,
    cmt_ProgramCommitteeChair,
    Thing,
    cmt_Conference,
    Document,
    cmt_Paper,
    cmt_Review,
    cmt_Person,
    cmt_Decision,
    ExternalReviewer,
    Review,
    cmt_Meta-Review,
    Paper,
    cmt_PaperFullVersion,
    cmt_PaperAbstract,
    Bid,
    Administrator,
    User,
    cmt_Administrator,
    ConferenceMember,
    cmt_Chairman,
    cmt_ProgramCommitteeMember,
    cmt_AssociatedChair,
    cmt_ConferenceChair,
    cmt_Author,
    cmt_Reviewer,
    Reviewer,
    cmt_Meta-Reviewer,
    cmt_Thing,
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



def test_cmt_user_is_not_abstract():
    assert not inspect.isabstract(cmt_User)


def test_cmt_user_constructor_exists():
    assert callable(cmt_User.__init__)


def test_cmt_user_constructor_args():
    sig = inspect.signature(cmt_User.__init__)
    params = list(sig.parameters.keys())



def test_cmt_conferencemember_is_not_abstract():
    assert not inspect.isabstract(cmt_ConferenceMember)


def test_cmt_conferencemember_constructor_exists():
    assert callable(cmt_ConferenceMember.__init__)


def test_cmt_conferencemember_constructor_args():
    sig = inspect.signature(cmt_ConferenceMember.__init__)
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



def test_cmt_rejection_is_not_abstract():
    assert not inspect.isabstract(cmt_Rejection)


def test_cmt_rejection_constructor_exists():
    assert callable(cmt_Rejection.__init__)


def test_cmt_rejection_constructor_args():
    sig = inspect.signature(cmt_Rejection.__init__)
    params = list(sig.parameters.keys())



def test_cmt_acceptance_is_not_abstract():
    assert not inspect.isabstract(cmt_Acceptance)


def test_cmt_acceptance_constructor_exists():
    assert callable(cmt_Acceptance.__init__)


def test_cmt_acceptance_constructor_args():
    sig = inspect.signature(cmt_Acceptance.__init__)
    params = list(sig.parameters.keys())



def test_cmt_externalreviewer_is_not_abstract():
    assert not inspect.isabstract(cmt_ExternalReviewer)


def test_cmt_externalreviewer_constructor_exists():
    assert callable(cmt_ExternalReviewer.__init__)


def test_cmt_externalreviewer_constructor_args():
    sig = inspect.signature(cmt_ExternalReviewer.__init__)
    params = list(sig.parameters.keys())



def test_cmt_subjectarea_is_not_abstract():
    assert not inspect.isabstract(cmt_SubjectArea)


def test_cmt_subjectarea_constructor_exists():
    assert callable(cmt_SubjectArea.__init__)


def test_cmt_subjectarea_constructor_args():
    sig = inspect.signature(cmt_SubjectArea.__init__)
    params = list(sig.parameters.keys())



def test_author_is_not_abstract():
    assert not inspect.isabstract(Author)


def test_author_constructor_exists():
    assert callable(Author.__init__)


def test_author_constructor_args():
    sig = inspect.signature(Author.__init__)
    params = list(sig.parameters.keys())



def test_cmt_co_author_is_not_abstract():
    assert not inspect.isabstract(cmt_Co_author)


def test_cmt_co_author_constructor_exists():
    assert callable(cmt_Co_author.__init__)


def test_cmt_co_author_constructor_args():
    sig = inspect.signature(cmt_Co_author.__init__)
    params = list(sig.parameters.keys())



def test_cmt_authornotreviewer_is_not_abstract():
    assert not inspect.isabstract(cmt_AuthorNotReviewer)


def test_cmt_authornotreviewer_constructor_exists():
    assert callable(cmt_AuthorNotReviewer.__init__)


def test_cmt_authornotreviewer_constructor_args():
    sig = inspect.signature(cmt_AuthorNotReviewer.__init__)
    params = list(sig.parameters.keys())



def test_cmt_bid_is_not_abstract():
    assert not inspect.isabstract(cmt_Bid)


def test_cmt_bid_constructor_exists():
    assert callable(cmt_Bid.__init__)


def test_cmt_bid_constructor_args():
    sig = inspect.signature(cmt_Bid.__init__)
    params = list(sig.parameters.keys())



def test_programcommitteemember_is_not_abstract():
    assert not inspect.isabstract(ProgramCommitteeMember)


def test_programcommitteemember_constructor_exists():
    assert callable(ProgramCommitteeMember.__init__)


def test_programcommitteemember_constructor_args():
    sig = inspect.signature(ProgramCommitteeMember.__init__)
    params = list(sig.parameters.keys())



def test_cmt_programcommittee_is_not_abstract():
    assert not inspect.isabstract(cmt_ProgramCommittee)


def test_cmt_programcommittee_constructor_exists():
    assert callable(cmt_ProgramCommittee.__init__)


def test_cmt_programcommittee_constructor_args():
    sig = inspect.signature(cmt_ProgramCommittee.__init__)
    params = list(sig.parameters.keys())



def test_cmt_preference_is_not_abstract():
    assert not inspect.isabstract(cmt_Preference)


def test_cmt_preference_constructor_exists():
    assert callable(cmt_Preference.__init__)


def test_cmt_preference_constructor_args():
    sig = inspect.signature(cmt_Preference.__init__)
    params = list(sig.parameters.keys())



def test_cmt_document_is_not_abstract():
    assert not inspect.isabstract(cmt_Document)


def test_cmt_document_constructor_exists():
    assert callable(cmt_Document.__init__)


def test_cmt_document_constructor_args():
    sig = inspect.signature(cmt_Document.__init__)
    params = list(sig.parameters.keys())



def test_chairman_is_not_abstract():
    assert not inspect.isabstract(Chairman)


def test_chairman_constructor_exists():
    assert callable(Chairman.__init__)


def test_chairman_constructor_args():
    sig = inspect.signature(Chairman.__init__)
    params = list(sig.parameters.keys())



def test_cmt_programcommitteechair_is_not_abstract():
    assert not inspect.isabstract(cmt_ProgramCommitteeChair)


def test_cmt_programcommitteechair_constructor_exists():
    assert callable(cmt_ProgramCommitteeChair.__init__)


def test_cmt_programcommitteechair_constructor_args():
    sig = inspect.signature(cmt_ProgramCommitteeChair.__init__)
    params = list(sig.parameters.keys())



def test_thing_is_not_abstract():
    assert not inspect.isabstract(Thing)


def test_thing_constructor_exists():
    assert callable(Thing.__init__)


def test_thing_constructor_args():
    sig = inspect.signature(Thing.__init__)
    params = list(sig.parameters.keys())



def test_cmt_conference_is_not_abstract():
    assert not inspect.isabstract(cmt_Conference)


def test_cmt_conference_constructor_exists():
    assert callable(cmt_Conference.__init__)


def test_cmt_conference_constructor_args():
    sig = inspect.signature(cmt_Conference.__init__)
    params = list(sig.parameters.keys())
    assert "date" in params, "Missing parameter 'date'"
    assert "reviewsPerPaper" in params, "Missing parameter 'reviewsPerPaper'"
    assert "logoURL" in params, "Missing parameter 'logoURL'"
    assert "acceptsHardcopySubmissions" in params, "Missing parameter 'acceptsHardcopySubmissions'"
    assert "siteURL" in params, "Missing parameter 'siteURL'"

def test_cmt_conference_has_date():
    assert hasattr(cmt_Conference, "date")
    descriptor = None
    for klass in cmt_Conference.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)

def test_cmt_conference_has_reviewsPerPaper():
    assert hasattr(cmt_Conference, "reviewsPerPaper")
    descriptor = None
    for klass in cmt_Conference.__mro__:
        if "reviewsPerPaper" in klass.__dict__:
            descriptor = klass.__dict__["reviewsPerPaper"]
            break
    assert isinstance(descriptor, property)

def test_cmt_conference_has_logoURL():
    assert hasattr(cmt_Conference, "logoURL")
    descriptor = None
    for klass in cmt_Conference.__mro__:
        if "logoURL" in klass.__dict__:
            descriptor = klass.__dict__["logoURL"]
            break
    assert isinstance(descriptor, property)

def test_cmt_conference_has_acceptsHardcopySubmissions():
    assert hasattr(cmt_Conference, "acceptsHardcopySubmissions")
    descriptor = None
    for klass in cmt_Conference.__mro__:
        if "acceptsHardcopySubmissions" in klass.__dict__:
            descriptor = klass.__dict__["acceptsHardcopySubmissions"]
            break
    assert isinstance(descriptor, property)

def test_cmt_conference_has_siteURL():
    assert hasattr(cmt_Conference, "siteURL")
    descriptor = None
    for klass in cmt_Conference.__mro__:
        if "siteURL" in klass.__dict__:
            descriptor = klass.__dict__["siteURL"]
            break
    assert isinstance(descriptor, property)



def test_document_is_not_abstract():
    assert not inspect.isabstract(Document)


def test_document_constructor_exists():
    assert callable(Document.__init__)


def test_document_constructor_args():
    sig = inspect.signature(Document.__init__)
    params = list(sig.parameters.keys())



def test_cmt_paper_is_not_abstract():
    assert not inspect.isabstract(cmt_Paper)


def test_cmt_paper_constructor_exists():
    assert callable(cmt_Paper.__init__)


def test_cmt_paper_constructor_args():
    sig = inspect.signature(cmt_Paper.__init__)
    params = list(sig.parameters.keys())
    assert "paperID" in params, "Missing parameter 'paperID'"
    assert "title" in params, "Missing parameter 'title'"

def test_cmt_paper_has_paperID():
    assert hasattr(cmt_Paper, "paperID")
    descriptor = None
    for klass in cmt_Paper.__mro__:
        if "paperID" in klass.__dict__:
            descriptor = klass.__dict__["paperID"]
            break
    assert isinstance(descriptor, property)

def test_cmt_paper_has_title():
    assert hasattr(cmt_Paper, "title")
    descriptor = None
    for klass in cmt_Paper.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_cmt_review_is_not_abstract():
    assert not inspect.isabstract(cmt_Review)


def test_cmt_review_constructor_exists():
    assert callable(cmt_Review.__init__)


def test_cmt_review_constructor_args():
    sig = inspect.signature(cmt_Review.__init__)
    params = list(sig.parameters.keys())



def test_cmt_person_is_not_abstract():
    assert not inspect.isabstract(cmt_Person)


def test_cmt_person_constructor_exists():
    assert callable(cmt_Person.__init__)


def test_cmt_person_constructor_args():
    sig = inspect.signature(cmt_Person.__init__)
    params = list(sig.parameters.keys())
    assert "email" in params, "Missing parameter 'email'"

def test_cmt_person_has_email():
    assert hasattr(cmt_Person, "email")
    descriptor = None
    for klass in cmt_Person.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)



def test_cmt_decision_is_not_abstract():
    assert not inspect.isabstract(cmt_Decision)


def test_cmt_decision_constructor_exists():
    assert callable(cmt_Decision.__init__)


def test_cmt_decision_constructor_args():
    sig = inspect.signature(cmt_Decision.__init__)
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



def test_cmt_meta-review_is_not_abstract():
    assert not inspect.isabstract(cmt_Meta-Review)


def test_cmt_meta-review_constructor_exists():
    assert callable(cmt_Meta-Review.__init__)


def test_cmt_meta-review_constructor_args():
    sig = inspect.signature(cmt_Meta-Review.__init__)
    params = list(sig.parameters.keys())



def test_paper_is_not_abstract():
    assert not inspect.isabstract(Paper)


def test_paper_constructor_exists():
    assert callable(Paper.__init__)


def test_paper_constructor_args():
    sig = inspect.signature(Paper.__init__)
    params = list(sig.parameters.keys())



def test_cmt_paperfullversion_is_not_abstract():
    assert not inspect.isabstract(cmt_PaperFullVersion)


def test_cmt_paperfullversion_constructor_exists():
    assert callable(cmt_PaperFullVersion.__init__)


def test_cmt_paperfullversion_constructor_args():
    sig = inspect.signature(cmt_PaperFullVersion.__init__)
    params = list(sig.parameters.keys())



def test_cmt_paperabstract_is_not_abstract():
    assert not inspect.isabstract(cmt_PaperAbstract)


def test_cmt_paperabstract_constructor_exists():
    assert callable(cmt_PaperAbstract.__init__)


def test_cmt_paperabstract_constructor_args():
    sig = inspect.signature(cmt_PaperAbstract.__init__)
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



def test_cmt_administrator_is_not_abstract():
    assert not inspect.isabstract(cmt_Administrator)


def test_cmt_administrator_constructor_exists():
    assert callable(cmt_Administrator.__init__)


def test_cmt_administrator_constructor_args():
    sig = inspect.signature(cmt_Administrator.__init__)
    params = list(sig.parameters.keys())



def test_conferencemember_is_not_abstract():
    assert not inspect.isabstract(ConferenceMember)


def test_conferencemember_constructor_exists():
    assert callable(ConferenceMember.__init__)


def test_conferencemember_constructor_args():
    sig = inspect.signature(ConferenceMember.__init__)
    params = list(sig.parameters.keys())



def test_cmt_chairman_is_not_abstract():
    assert not inspect.isabstract(cmt_Chairman)


def test_cmt_chairman_constructor_exists():
    assert callable(cmt_Chairman.__init__)


def test_cmt_chairman_constructor_args():
    sig = inspect.signature(cmt_Chairman.__init__)
    params = list(sig.parameters.keys())



def test_cmt_programcommitteemember_is_not_abstract():
    assert not inspect.isabstract(cmt_ProgramCommitteeMember)


def test_cmt_programcommitteemember_constructor_exists():
    assert callable(cmt_ProgramCommitteeMember.__init__)


def test_cmt_programcommitteemember_constructor_args():
    sig = inspect.signature(cmt_ProgramCommitteeMember.__init__)
    params = list(sig.parameters.keys())
    assert "maxPapers" in params, "Missing parameter 'maxPapers'"

def test_cmt_programcommitteemember_has_maxPapers():
    assert hasattr(cmt_ProgramCommitteeMember, "maxPapers")
    descriptor = None
    for klass in cmt_ProgramCommitteeMember.__mro__:
        if "maxPapers" in klass.__dict__:
            descriptor = klass.__dict__["maxPapers"]
            break
    assert isinstance(descriptor, property)



def test_cmt_associatedchair_is_not_abstract():
    assert not inspect.isabstract(cmt_AssociatedChair)


def test_cmt_associatedchair_constructor_exists():
    assert callable(cmt_AssociatedChair.__init__)


def test_cmt_associatedchair_constructor_args():
    sig = inspect.signature(cmt_AssociatedChair.__init__)
    params = list(sig.parameters.keys())



def test_cmt_conferencechair_is_not_abstract():
    assert not inspect.isabstract(cmt_ConferenceChair)


def test_cmt_conferencechair_constructor_exists():
    assert callable(cmt_ConferenceChair.__init__)


def test_cmt_conferencechair_constructor_args():
    sig = inspect.signature(cmt_ConferenceChair.__init__)
    params = list(sig.parameters.keys())



def test_cmt_author_is_not_abstract():
    assert not inspect.isabstract(cmt_Author)


def test_cmt_author_constructor_exists():
    assert callable(cmt_Author.__init__)


def test_cmt_author_constructor_args():
    sig = inspect.signature(cmt_Author.__init__)
    params = list(sig.parameters.keys())



def test_cmt_reviewer_is_not_abstract():
    assert not inspect.isabstract(cmt_Reviewer)


def test_cmt_reviewer_constructor_exists():
    assert callable(cmt_Reviewer.__init__)


def test_cmt_reviewer_constructor_args():
    sig = inspect.signature(cmt_Reviewer.__init__)
    params = list(sig.parameters.keys())



def test_reviewer_is_not_abstract():
    assert not inspect.isabstract(Reviewer)


def test_reviewer_constructor_exists():
    assert callable(Reviewer.__init__)


def test_reviewer_constructor_args():
    sig = inspect.signature(Reviewer.__init__)
    params = list(sig.parameters.keys())



def test_cmt_meta-reviewer_is_not_abstract():
    assert not inspect.isabstract(cmt_Meta-Reviewer)


def test_cmt_meta-reviewer_constructor_exists():
    assert callable(cmt_Meta-Reviewer.__init__)


def test_cmt_meta-reviewer_constructor_args():
    sig = inspect.signature(cmt_Meta-Reviewer.__init__)
    params = list(sig.parameters.keys())



def test_cmt_thing_is_not_abstract():
    assert not inspect.isabstract(cmt_Thing)


def test_cmt_thing_constructor_exists():
    assert callable(cmt_Thing.__init__)


def test_cmt_thing_constructor_args():
    sig = inspect.signature(cmt_Thing.__init__)
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
cmt_User_strategy = st.builds(
    cmt_User,
)
cmt_ConferenceMember_strategy = st.builds(
    cmt_ConferenceMember,
)
Co_author_strategy = st.builds(
    Co_author,
)
Decision_strategy = st.builds(
    Decision,
)
cmt_Rejection_strategy = st.builds(
    cmt_Rejection,
)
cmt_Acceptance_strategy = st.builds(
    cmt_Acceptance,
)
cmt_ExternalReviewer_strategy = st.builds(
    cmt_ExternalReviewer,
)
cmt_SubjectArea_strategy = st.builds(
    cmt_SubjectArea,
)
Author_strategy = st.builds(
    Author,
)
cmt_Co_author_strategy = st.builds(
    cmt_Co_author,
)
cmt_AuthorNotReviewer_strategy = st.builds(
    cmt_AuthorNotReviewer,
)
cmt_Bid_strategy = st.builds(
    cmt_Bid,
)
ProgramCommitteeMember_strategy = st.builds(
    ProgramCommitteeMember,
)
cmt_ProgramCommittee_strategy = st.builds(
    cmt_ProgramCommittee,
)
cmt_Preference_strategy = st.builds(
    cmt_Preference,
)
cmt_Document_strategy = st.builds(
    cmt_Document,
)
Chairman_strategy = st.builds(
    Chairman,
)
cmt_ProgramCommitteeChair_strategy = st.builds(
    cmt_ProgramCommitteeChair,
)
Thing_strategy = st.builds(
    Thing,
)
cmt_Conference_strategy = st.builds(
    cmt_Conference,
    date=
        safe_text,
    reviewsPerPaper=
        safe_text,
    logoURL=
        safe_text,
    acceptsHardcopySubmissions=
        safe_text,
    siteURL=
        safe_text
)
Document_strategy = st.builds(
    Document,
)
cmt_Paper_strategy = st.builds(
    cmt_Paper,
    paperID=
        safe_text,
    title=
        safe_text
)
cmt_Review_strategy = st.builds(
    cmt_Review,
)
cmt_Person_strategy = st.builds(
    cmt_Person,
    email=
        safe_text
)
cmt_Decision_strategy = st.builds(
    cmt_Decision,
)
ExternalReviewer_strategy = st.builds(
    ExternalReviewer,
)
Review_strategy = st.builds(
    Review,
)
cmt_Meta-Review_strategy = st.builds(
    cmt_Meta-Review,
)
Paper_strategy = st.builds(
    Paper,
)
cmt_PaperFullVersion_strategy = st.builds(
    cmt_PaperFullVersion,
)
cmt_PaperAbstract_strategy = st.builds(
    cmt_PaperAbstract,
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
cmt_Administrator_strategy = st.builds(
    cmt_Administrator,
)
ConferenceMember_strategy = st.builds(
    ConferenceMember,
)
cmt_Chairman_strategy = st.builds(
    cmt_Chairman,
)
cmt_ProgramCommitteeMember_strategy = st.builds(
    cmt_ProgramCommitteeMember,
    maxPapers=
        safe_text
)
cmt_AssociatedChair_strategy = st.builds(
    cmt_AssociatedChair,
)
cmt_ConferenceChair_strategy = st.builds(
    cmt_ConferenceChair,
)
cmt_Author_strategy = st.builds(
    cmt_Author,
)
cmt_Reviewer_strategy = st.builds(
    cmt_Reviewer,
)
Reviewer_strategy = st.builds(
    Reviewer,
)
cmt_Meta-Reviewer_strategy = st.builds(
    cmt_Meta-Reviewer,
)
cmt_Thing_strategy = st.builds(
    cmt_Thing,
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

@given(instance=cmt_User_strategy)
@settings(max_examples=50)
def test_cmt_user_instantiation(instance):
    assert isinstance(instance, cmt_User)

@given(instance=cmt_ConferenceMember_strategy)
@settings(max_examples=50)
def test_cmt_conferencemember_instantiation(instance):
    assert isinstance(instance, cmt_ConferenceMember)

@given(instance=Co_author_strategy)
@settings(max_examples=50)
def test_co_author_instantiation(instance):
    assert isinstance(instance, Co_author)

@given(instance=Decision_strategy)
@settings(max_examples=50)
def test_decision_instantiation(instance):
    assert isinstance(instance, Decision)

@given(instance=cmt_Rejection_strategy)
@settings(max_examples=50)
def test_cmt_rejection_instantiation(instance):
    assert isinstance(instance, cmt_Rejection)

@given(instance=cmt_Acceptance_strategy)
@settings(max_examples=50)
def test_cmt_acceptance_instantiation(instance):
    assert isinstance(instance, cmt_Acceptance)

@given(instance=cmt_ExternalReviewer_strategy)
@settings(max_examples=50)
def test_cmt_externalreviewer_instantiation(instance):
    assert isinstance(instance, cmt_ExternalReviewer)

@given(instance=cmt_SubjectArea_strategy)
@settings(max_examples=50)
def test_cmt_subjectarea_instantiation(instance):
    assert isinstance(instance, cmt_SubjectArea)

@given(instance=Author_strategy)
@settings(max_examples=50)
def test_author_instantiation(instance):
    assert isinstance(instance, Author)

@given(instance=cmt_Co_author_strategy)
@settings(max_examples=50)
def test_cmt_co_author_instantiation(instance):
    assert isinstance(instance, cmt_Co_author)

@given(instance=cmt_AuthorNotReviewer_strategy)
@settings(max_examples=50)
def test_cmt_authornotreviewer_instantiation(instance):
    assert isinstance(instance, cmt_AuthorNotReviewer)

@given(instance=cmt_Bid_strategy)
@settings(max_examples=50)
def test_cmt_bid_instantiation(instance):
    assert isinstance(instance, cmt_Bid)

@given(instance=ProgramCommitteeMember_strategy)
@settings(max_examples=50)
def test_programcommitteemember_instantiation(instance):
    assert isinstance(instance, ProgramCommitteeMember)

@given(instance=cmt_ProgramCommittee_strategy)
@settings(max_examples=50)
def test_cmt_programcommittee_instantiation(instance):
    assert isinstance(instance, cmt_ProgramCommittee)

@given(instance=cmt_Preference_strategy)
@settings(max_examples=50)
def test_cmt_preference_instantiation(instance):
    assert isinstance(instance, cmt_Preference)

@given(instance=cmt_Document_strategy)
@settings(max_examples=50)
def test_cmt_document_instantiation(instance):
    assert isinstance(instance, cmt_Document)

@given(instance=Chairman_strategy)
@settings(max_examples=50)
def test_chairman_instantiation(instance):
    assert isinstance(instance, Chairman)

@given(instance=cmt_ProgramCommitteeChair_strategy)
@settings(max_examples=50)
def test_cmt_programcommitteechair_instantiation(instance):
    assert isinstance(instance, cmt_ProgramCommitteeChair)

@given(instance=Thing_strategy)
@settings(max_examples=50)
def test_thing_instantiation(instance):
    assert isinstance(instance, Thing)

@given(instance=cmt_Conference_strategy)
@settings(max_examples=50)
def test_cmt_conference_instantiation(instance):
    assert isinstance(instance, cmt_Conference)



@given(instance=cmt_Conference_strategy)
def test_cmt_conference_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original



@given(instance=cmt_Conference_strategy)
def test_cmt_conference_reviewsPerPaper_setter(instance):
    original = instance.reviewsPerPaper
    instance.reviewsPerPaper = original
    assert instance.reviewsPerPaper == original



@given(instance=cmt_Conference_strategy)
def test_cmt_conference_logoURL_setter(instance):
    original = instance.logoURL
    instance.logoURL = original
    assert instance.logoURL == original



@given(instance=cmt_Conference_strategy)
def test_cmt_conference_acceptsHardcopySubmissions_setter(instance):
    original = instance.acceptsHardcopySubmissions
    instance.acceptsHardcopySubmissions = original
    assert instance.acceptsHardcopySubmissions == original



@given(instance=cmt_Conference_strategy)
def test_cmt_conference_siteURL_setter(instance):
    original = instance.siteURL
    instance.siteURL = original
    assert instance.siteURL == original

@given(instance=Document_strategy)
@settings(max_examples=50)
def test_document_instantiation(instance):
    assert isinstance(instance, Document)

@given(instance=cmt_Paper_strategy)
@settings(max_examples=50)
def test_cmt_paper_instantiation(instance):
    assert isinstance(instance, cmt_Paper)



@given(instance=cmt_Paper_strategy)
def test_cmt_paper_paperID_setter(instance):
    original = instance.paperID
    instance.paperID = original
    assert instance.paperID == original



@given(instance=cmt_Paper_strategy)
def test_cmt_paper_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=cmt_Review_strategy)
@settings(max_examples=50)
def test_cmt_review_instantiation(instance):
    assert isinstance(instance, cmt_Review)

@given(instance=cmt_Person_strategy)
@settings(max_examples=50)
def test_cmt_person_instantiation(instance):
    assert isinstance(instance, cmt_Person)



@given(instance=cmt_Person_strategy)
def test_cmt_person_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original

@given(instance=cmt_Decision_strategy)
@settings(max_examples=50)
def test_cmt_decision_instantiation(instance):
    assert isinstance(instance, cmt_Decision)

@given(instance=ExternalReviewer_strategy)
@settings(max_examples=50)
def test_externalreviewer_instantiation(instance):
    assert isinstance(instance, ExternalReviewer)

@given(instance=Review_strategy)
@settings(max_examples=50)
def test_review_instantiation(instance):
    assert isinstance(instance, Review)

@given(instance=cmt_Meta-Review_strategy)
@settings(max_examples=50)
def test_cmt_meta-review_instantiation(instance):
    assert isinstance(instance, cmt_Meta-Review)

@given(instance=Paper_strategy)
@settings(max_examples=50)
def test_paper_instantiation(instance):
    assert isinstance(instance, Paper)

@given(instance=cmt_PaperFullVersion_strategy)
@settings(max_examples=50)
def test_cmt_paperfullversion_instantiation(instance):
    assert isinstance(instance, cmt_PaperFullVersion)

@given(instance=cmt_PaperAbstract_strategy)
@settings(max_examples=50)
def test_cmt_paperabstract_instantiation(instance):
    assert isinstance(instance, cmt_PaperAbstract)

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

@given(instance=cmt_Administrator_strategy)
@settings(max_examples=50)
def test_cmt_administrator_instantiation(instance):
    assert isinstance(instance, cmt_Administrator)

@given(instance=ConferenceMember_strategy)
@settings(max_examples=50)
def test_conferencemember_instantiation(instance):
    assert isinstance(instance, ConferenceMember)

@given(instance=cmt_Chairman_strategy)
@settings(max_examples=50)
def test_cmt_chairman_instantiation(instance):
    assert isinstance(instance, cmt_Chairman)

@given(instance=cmt_ProgramCommitteeMember_strategy)
@settings(max_examples=50)
def test_cmt_programcommitteemember_instantiation(instance):
    assert isinstance(instance, cmt_ProgramCommitteeMember)



@given(instance=cmt_ProgramCommitteeMember_strategy)
def test_cmt_programcommitteemember_maxPapers_setter(instance):
    original = instance.maxPapers
    instance.maxPapers = original
    assert instance.maxPapers == original

@given(instance=cmt_AssociatedChair_strategy)
@settings(max_examples=50)
def test_cmt_associatedchair_instantiation(instance):
    assert isinstance(instance, cmt_AssociatedChair)

@given(instance=cmt_ConferenceChair_strategy)
@settings(max_examples=50)
def test_cmt_conferencechair_instantiation(instance):
    assert isinstance(instance, cmt_ConferenceChair)

@given(instance=cmt_Author_strategy)
@settings(max_examples=50)
def test_cmt_author_instantiation(instance):
    assert isinstance(instance, cmt_Author)

@given(instance=cmt_Reviewer_strategy)
@settings(max_examples=50)
def test_cmt_reviewer_instantiation(instance):
    assert isinstance(instance, cmt_Reviewer)

@given(instance=Reviewer_strategy)
@settings(max_examples=50)
def test_reviewer_instantiation(instance):
    assert isinstance(instance, Reviewer)

@given(instance=cmt_Meta-Reviewer_strategy)
@settings(max_examples=50)
def test_cmt_meta-reviewer_instantiation(instance):
    assert isinstance(instance, cmt_Meta-Reviewer)

@given(instance=cmt_Thing_strategy)
@settings(max_examples=50)
def test_cmt_thing_instantiation(instance):
    assert isinstance(instance, cmt_Thing)
