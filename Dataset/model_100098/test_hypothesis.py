import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Meta_Reviewer,
    SubjectArea,
    Cocus::Activity,
    Cocus::Description,
    URL,
    Cocus::Event::URL,
    Cocus::Event::Setup,
    Help::Request,
    Cocus::Assistance,
    Cocus::Feature::Request,
    Cocus::Misc,
    Review::Form,
    Cocus::Review::Form::Setup,
    Cocus::Preview,
    Email,
    Cocus::Group::Email,
    Cocus::Rejection::Email,
    Cocus::Approval::Email,
    Cocus::Notification::Email,
    Cocus::URL,
    Account,
    Activity,
    Cocus::Event::Creation,
    Cocus::Request,
    Cocus::Registration,
    Cocus::Event::Approval,
    Cocus::Inforamtion,
    Cocus::Account,
    Event::Setup,
    Cocus::Event::Tracks,
    Cocus::Paper::Typologies,
    Cocus::Review::Form,
    Cocus::Email::Template,
    Cocus::Submission::Template,
    Cocus::Research::Topic,
    Approval::Email,
    Inforamtion,
    Request,
    Cocus::Help::Request,
    Role,
    Cocus::Committe::Role,
    Cocus::Head::Role,
    Cocus::Admin::Role,
    Cocus::Reviewer::Role,
    Cocus::Author::Role,
    Event::Tracks,
    Cocus::SubjectArea,
    Author,
    Cocus::Corresponding::Author,
    Cocus::Co_author,
    Cocus::AuthorNotReviewer,
    ProgramCommittee,
    Co_author,
    Document,
    Cocus::Submission,
    Cocus::Email,
    Cocus::Paper,
    Cocus::Template,
    Cocus::Review,
    Decision,
    Cocus::Rejection,
    Cocus::Acceptance,
    Event,
    Cocus::Symposium,
    Cocus::Workshop,
    Thing,
    Cocus::Person,
    Cocus::Event,
    Cocus::Detail,
    Cocus::Role,
    Cocus::Document,
    Cocus::Conference,
    Conference,
    Person,
    Cocus::User,
    Cocus::ExternalReviewer,
    Cocus::ConferenceMember,
    Chairman,
    Administrator,
    User,
    Cocus::Administrator,
    Cocus::Committee,
    ConferenceMember,
    Cocus::ProgramCommitteeMember,
    Cocus::AssociatedChair,
    Cocus::ConferenceChair,
    Cocus::Author,
    Cocus::Chairman,
    Cocus::Reviewer,
    Reviewer,
    Cocus::Meta_Reviewer,
    Cocus::Thing,
    Cocus::Bid,
    ProgramCommitteeMember,
    Cocus::ProgramCommitteeChair,
    Cocus::ProgramCommittee,
    Cocus::Preference,
    Cocus::Decision,
    ExternalReviewer,
    Review,
    Cocus::Meta-Review,
    Paper,
    Cocus::Short::Paper,
    Cocus::Full::Paper,
    Cocus::PaperFullVersion,
    Cocus::Abstract,
    Cocus::PaperAbstract,
    Cocus::Invited::Paper,
    Bid,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_meta_reviewer_is_not_abstract():
    assert not inspect.isabstract(Meta_Reviewer)


def test_meta_reviewer_constructor_exists():
    assert callable(Meta_Reviewer.__init__)


def test_meta_reviewer_constructor_args():
    sig = inspect.signature(Meta_Reviewer.__init__)
    params = list(sig.parameters.keys())



def test_subjectarea_is_not_abstract():
    assert not inspect.isabstract(SubjectArea)


def test_subjectarea_constructor_exists():
    assert callable(SubjectArea.__init__)


def test_subjectarea_constructor_args():
    sig = inspect.signature(SubjectArea.__init__)
    params = list(sig.parameters.keys())



def test_cocus::activity_is_not_abstract():
    assert not inspect.isabstract(Cocus::Activity)


def test_cocus::activity_constructor_exists():
    assert callable(Cocus::Activity.__init__)


def test_cocus::activity_constructor_args():
    sig = inspect.signature(Cocus::Activity.__init__)
    params = list(sig.parameters.keys())



def test_cocus::description_is_not_abstract():
    assert not inspect.isabstract(Cocus::Description)


def test_cocus::description_constructor_exists():
    assert callable(Cocus::Description.__init__)


def test_cocus::description_constructor_args():
    sig = inspect.signature(Cocus::Description.__init__)
    params = list(sig.parameters.keys())



def test_url_is_not_abstract():
    assert not inspect.isabstract(URL)


def test_url_constructor_exists():
    assert callable(URL.__init__)


def test_url_constructor_args():
    sig = inspect.signature(URL.__init__)
    params = list(sig.parameters.keys())



def test_cocus::event::url_is_not_abstract():
    assert not inspect.isabstract(Cocus::Event::URL)


def test_cocus::event::url_constructor_exists():
    assert callable(Cocus::Event::URL.__init__)


def test_cocus::event::url_constructor_args():
    sig = inspect.signature(Cocus::Event::URL.__init__)
    params = list(sig.parameters.keys())



def test_cocus::event::setup_is_not_abstract():
    assert not inspect.isabstract(Cocus::Event::Setup)


def test_cocus::event::setup_constructor_exists():
    assert callable(Cocus::Event::Setup.__init__)


def test_cocus::event::setup_constructor_args():
    sig = inspect.signature(Cocus::Event::Setup.__init__)
    params = list(sig.parameters.keys())



def test_help::request_is_not_abstract():
    assert not inspect.isabstract(Help::Request)


def test_help::request_constructor_exists():
    assert callable(Help::Request.__init__)


def test_help::request_constructor_args():
    sig = inspect.signature(Help::Request.__init__)
    params = list(sig.parameters.keys())



def test_cocus::assistance_is_not_abstract():
    assert not inspect.isabstract(Cocus::Assistance)


def test_cocus::assistance_constructor_exists():
    assert callable(Cocus::Assistance.__init__)


def test_cocus::assistance_constructor_args():
    sig = inspect.signature(Cocus::Assistance.__init__)
    params = list(sig.parameters.keys())



def test_cocus::feature::request_is_not_abstract():
    assert not inspect.isabstract(Cocus::Feature::Request)


def test_cocus::feature::request_constructor_exists():
    assert callable(Cocus::Feature::Request.__init__)


def test_cocus::feature::request_constructor_args():
    sig = inspect.signature(Cocus::Feature::Request.__init__)
    params = list(sig.parameters.keys())



def test_cocus::misc_is_not_abstract():
    assert not inspect.isabstract(Cocus::Misc)


def test_cocus::misc_constructor_exists():
    assert callable(Cocus::Misc.__init__)


def test_cocus::misc_constructor_args():
    sig = inspect.signature(Cocus::Misc.__init__)
    params = list(sig.parameters.keys())



def test_review::form_is_not_abstract():
    assert not inspect.isabstract(Review::Form)


def test_review::form_constructor_exists():
    assert callable(Review::Form.__init__)


def test_review::form_constructor_args():
    sig = inspect.signature(Review::Form.__init__)
    params = list(sig.parameters.keys())



def test_cocus::review::form::setup_is_not_abstract():
    assert not inspect.isabstract(Cocus::Review::Form::Setup)


def test_cocus::review::form::setup_constructor_exists():
    assert callable(Cocus::Review::Form::Setup.__init__)


def test_cocus::review::form::setup_constructor_args():
    sig = inspect.signature(Cocus::Review::Form::Setup.__init__)
    params = list(sig.parameters.keys())



def test_cocus::preview_is_not_abstract():
    assert not inspect.isabstract(Cocus::Preview)


def test_cocus::preview_constructor_exists():
    assert callable(Cocus::Preview.__init__)


def test_cocus::preview_constructor_args():
    sig = inspect.signature(Cocus::Preview.__init__)
    params = list(sig.parameters.keys())



def test_email_is_not_abstract():
    assert not inspect.isabstract(Email)


def test_email_constructor_exists():
    assert callable(Email.__init__)


def test_email_constructor_args():
    sig = inspect.signature(Email.__init__)
    params = list(sig.parameters.keys())



def test_cocus::group::email_is_not_abstract():
    assert not inspect.isabstract(Cocus::Group::Email)


def test_cocus::group::email_constructor_exists():
    assert callable(Cocus::Group::Email.__init__)


def test_cocus::group::email_constructor_args():
    sig = inspect.signature(Cocus::Group::Email.__init__)
    params = list(sig.parameters.keys())



def test_cocus::rejection::email_is_not_abstract():
    assert not inspect.isabstract(Cocus::Rejection::Email)


def test_cocus::rejection::email_constructor_exists():
    assert callable(Cocus::Rejection::Email.__init__)


def test_cocus::rejection::email_constructor_args():
    sig = inspect.signature(Cocus::Rejection::Email.__init__)
    params = list(sig.parameters.keys())



def test_cocus::approval::email_is_not_abstract():
    assert not inspect.isabstract(Cocus::Approval::Email)


def test_cocus::approval::email_constructor_exists():
    assert callable(Cocus::Approval::Email.__init__)


def test_cocus::approval::email_constructor_args():
    sig = inspect.signature(Cocus::Approval::Email.__init__)
    params = list(sig.parameters.keys())



def test_cocus::notification::email_is_not_abstract():
    assert not inspect.isabstract(Cocus::Notification::Email)


def test_cocus::notification::email_constructor_exists():
    assert callable(Cocus::Notification::Email.__init__)


def test_cocus::notification::email_constructor_args():
    sig = inspect.signature(Cocus::Notification::Email.__init__)
    params = list(sig.parameters.keys())



def test_cocus::url_is_not_abstract():
    assert not inspect.isabstract(Cocus::URL)


def test_cocus::url_constructor_exists():
    assert callable(Cocus::URL.__init__)


def test_cocus::url_constructor_args():
    sig = inspect.signature(Cocus::URL.__init__)
    params = list(sig.parameters.keys())



def test_account_is_not_abstract():
    assert not inspect.isabstract(Account)


def test_account_constructor_exists():
    assert callable(Account.__init__)


def test_account_constructor_args():
    sig = inspect.signature(Account.__init__)
    params = list(sig.parameters.keys())



def test_activity_is_not_abstract():
    assert not inspect.isabstract(Activity)


def test_activity_constructor_exists():
    assert callable(Activity.__init__)


def test_activity_constructor_args():
    sig = inspect.signature(Activity.__init__)
    params = list(sig.parameters.keys())



def test_cocus::event::creation_is_not_abstract():
    assert not inspect.isabstract(Cocus::Event::Creation)


def test_cocus::event::creation_constructor_exists():
    assert callable(Cocus::Event::Creation.__init__)


def test_cocus::event::creation_constructor_args():
    sig = inspect.signature(Cocus::Event::Creation.__init__)
    params = list(sig.parameters.keys())



def test_cocus::request_is_not_abstract():
    assert not inspect.isabstract(Cocus::Request)


def test_cocus::request_constructor_exists():
    assert callable(Cocus::Request.__init__)


def test_cocus::request_constructor_args():
    sig = inspect.signature(Cocus::Request.__init__)
    params = list(sig.parameters.keys())



def test_cocus::registration_is_not_abstract():
    assert not inspect.isabstract(Cocus::Registration)


def test_cocus::registration_constructor_exists():
    assert callable(Cocus::Registration.__init__)


def test_cocus::registration_constructor_args():
    sig = inspect.signature(Cocus::Registration.__init__)
    params = list(sig.parameters.keys())



def test_cocus::event::approval_is_not_abstract():
    assert not inspect.isabstract(Cocus::Event::Approval)


def test_cocus::event::approval_constructor_exists():
    assert callable(Cocus::Event::Approval.__init__)


def test_cocus::event::approval_constructor_args():
    sig = inspect.signature(Cocus::Event::Approval.__init__)
    params = list(sig.parameters.keys())



def test_cocus::inforamtion_is_not_abstract():
    assert not inspect.isabstract(Cocus::Inforamtion)


def test_cocus::inforamtion_constructor_exists():
    assert callable(Cocus::Inforamtion.__init__)


def test_cocus::inforamtion_constructor_args():
    sig = inspect.signature(Cocus::Inforamtion.__init__)
    params = list(sig.parameters.keys())



def test_cocus::account_is_not_abstract():
    assert not inspect.isabstract(Cocus::Account)


def test_cocus::account_constructor_exists():
    assert callable(Cocus::Account.__init__)


def test_cocus::account_constructor_args():
    sig = inspect.signature(Cocus::Account.__init__)
    params = list(sig.parameters.keys())



def test_event::setup_is_not_abstract():
    assert not inspect.isabstract(Event::Setup)


def test_event::setup_constructor_exists():
    assert callable(Event::Setup.__init__)


def test_event::setup_constructor_args():
    sig = inspect.signature(Event::Setup.__init__)
    params = list(sig.parameters.keys())



def test_cocus::event::tracks_is_not_abstract():
    assert not inspect.isabstract(Cocus::Event::Tracks)


def test_cocus::event::tracks_constructor_exists():
    assert callable(Cocus::Event::Tracks.__init__)


def test_cocus::event::tracks_constructor_args():
    sig = inspect.signature(Cocus::Event::Tracks.__init__)
    params = list(sig.parameters.keys())



def test_cocus::paper::typologies_is_not_abstract():
    assert not inspect.isabstract(Cocus::Paper::Typologies)


def test_cocus::paper::typologies_constructor_exists():
    assert callable(Cocus::Paper::Typologies.__init__)


def test_cocus::paper::typologies_constructor_args():
    sig = inspect.signature(Cocus::Paper::Typologies.__init__)
    params = list(sig.parameters.keys())



def test_cocus::review::form_is_not_abstract():
    assert not inspect.isabstract(Cocus::Review::Form)


def test_cocus::review::form_constructor_exists():
    assert callable(Cocus::Review::Form.__init__)


def test_cocus::review::form_constructor_args():
    sig = inspect.signature(Cocus::Review::Form.__init__)
    params = list(sig.parameters.keys())



def test_cocus::email::template_is_not_abstract():
    assert not inspect.isabstract(Cocus::Email::Template)


def test_cocus::email::template_constructor_exists():
    assert callable(Cocus::Email::Template.__init__)


def test_cocus::email::template_constructor_args():
    sig = inspect.signature(Cocus::Email::Template.__init__)
    params = list(sig.parameters.keys())



def test_cocus::submission::template_is_not_abstract():
    assert not inspect.isabstract(Cocus::Submission::Template)


def test_cocus::submission::template_constructor_exists():
    assert callable(Cocus::Submission::Template.__init__)


def test_cocus::submission::template_constructor_args():
    sig = inspect.signature(Cocus::Submission::Template.__init__)
    params = list(sig.parameters.keys())



def test_cocus::research::topic_is_not_abstract():
    assert not inspect.isabstract(Cocus::Research::Topic)


def test_cocus::research::topic_constructor_exists():
    assert callable(Cocus::Research::Topic.__init__)


def test_cocus::research::topic_constructor_args():
    sig = inspect.signature(Cocus::Research::Topic.__init__)
    params = list(sig.parameters.keys())



def test_approval::email_is_not_abstract():
    assert not inspect.isabstract(Approval::Email)


def test_approval::email_constructor_exists():
    assert callable(Approval::Email.__init__)


def test_approval::email_constructor_args():
    sig = inspect.signature(Approval::Email.__init__)
    params = list(sig.parameters.keys())



def test_inforamtion_is_not_abstract():
    assert not inspect.isabstract(Inforamtion)


def test_inforamtion_constructor_exists():
    assert callable(Inforamtion.__init__)


def test_inforamtion_constructor_args():
    sig = inspect.signature(Inforamtion.__init__)
    params = list(sig.parameters.keys())



def test_request_is_not_abstract():
    assert not inspect.isabstract(Request)


def test_request_constructor_exists():
    assert callable(Request.__init__)


def test_request_constructor_args():
    sig = inspect.signature(Request.__init__)
    params = list(sig.parameters.keys())



def test_cocus::help::request_is_not_abstract():
    assert not inspect.isabstract(Cocus::Help::Request)


def test_cocus::help::request_constructor_exists():
    assert callable(Cocus::Help::Request.__init__)


def test_cocus::help::request_constructor_args():
    sig = inspect.signature(Cocus::Help::Request.__init__)
    params = list(sig.parameters.keys())



def test_role_is_not_abstract():
    assert not inspect.isabstract(Role)


def test_role_constructor_exists():
    assert callable(Role.__init__)


def test_role_constructor_args():
    sig = inspect.signature(Role.__init__)
    params = list(sig.parameters.keys())



def test_cocus::committe::role_is_not_abstract():
    assert not inspect.isabstract(Cocus::Committe::Role)


def test_cocus::committe::role_constructor_exists():
    assert callable(Cocus::Committe::Role.__init__)


def test_cocus::committe::role_constructor_args():
    sig = inspect.signature(Cocus::Committe::Role.__init__)
    params = list(sig.parameters.keys())



def test_cocus::head::role_is_not_abstract():
    assert not inspect.isabstract(Cocus::Head::Role)


def test_cocus::head::role_constructor_exists():
    assert callable(Cocus::Head::Role.__init__)


def test_cocus::head::role_constructor_args():
    sig = inspect.signature(Cocus::Head::Role.__init__)
    params = list(sig.parameters.keys())



def test_cocus::admin::role_is_not_abstract():
    assert not inspect.isabstract(Cocus::Admin::Role)


def test_cocus::admin::role_constructor_exists():
    assert callable(Cocus::Admin::Role.__init__)


def test_cocus::admin::role_constructor_args():
    sig = inspect.signature(Cocus::Admin::Role.__init__)
    params = list(sig.parameters.keys())



def test_cocus::reviewer::role_is_not_abstract():
    assert not inspect.isabstract(Cocus::Reviewer::Role)


def test_cocus::reviewer::role_constructor_exists():
    assert callable(Cocus::Reviewer::Role.__init__)


def test_cocus::reviewer::role_constructor_args():
    sig = inspect.signature(Cocus::Reviewer::Role.__init__)
    params = list(sig.parameters.keys())



def test_cocus::author::role_is_not_abstract():
    assert not inspect.isabstract(Cocus::Author::Role)


def test_cocus::author::role_constructor_exists():
    assert callable(Cocus::Author::Role.__init__)


def test_cocus::author::role_constructor_args():
    sig = inspect.signature(Cocus::Author::Role.__init__)
    params = list(sig.parameters.keys())



def test_event::tracks_is_not_abstract():
    assert not inspect.isabstract(Event::Tracks)


def test_event::tracks_constructor_exists():
    assert callable(Event::Tracks.__init__)


def test_event::tracks_constructor_args():
    sig = inspect.signature(Event::Tracks.__init__)
    params = list(sig.parameters.keys())



def test_cocus::subjectarea_is_not_abstract():
    assert not inspect.isabstract(Cocus::SubjectArea)


def test_cocus::subjectarea_constructor_exists():
    assert callable(Cocus::SubjectArea.__init__)


def test_cocus::subjectarea_constructor_args():
    sig = inspect.signature(Cocus::SubjectArea.__init__)
    params = list(sig.parameters.keys())



def test_author_is_not_abstract():
    assert not inspect.isabstract(Author)


def test_author_constructor_exists():
    assert callable(Author.__init__)


def test_author_constructor_args():
    sig = inspect.signature(Author.__init__)
    params = list(sig.parameters.keys())



def test_cocus::corresponding::author_is_not_abstract():
    assert not inspect.isabstract(Cocus::Corresponding::Author)


def test_cocus::corresponding::author_constructor_exists():
    assert callable(Cocus::Corresponding::Author.__init__)


def test_cocus::corresponding::author_constructor_args():
    sig = inspect.signature(Cocus::Corresponding::Author.__init__)
    params = list(sig.parameters.keys())



def test_cocus::co_author_is_not_abstract():
    assert not inspect.isabstract(Cocus::Co_author)


def test_cocus::co_author_constructor_exists():
    assert callable(Cocus::Co_author.__init__)


def test_cocus::co_author_constructor_args():
    sig = inspect.signature(Cocus::Co_author.__init__)
    params = list(sig.parameters.keys())



def test_cocus::authornotreviewer_is_not_abstract():
    assert not inspect.isabstract(Cocus::AuthorNotReviewer)


def test_cocus::authornotreviewer_constructor_exists():
    assert callable(Cocus::AuthorNotReviewer.__init__)


def test_cocus::authornotreviewer_constructor_args():
    sig = inspect.signature(Cocus::AuthorNotReviewer.__init__)
    params = list(sig.parameters.keys())



def test_programcommittee_is_not_abstract():
    assert not inspect.isabstract(ProgramCommittee)


def test_programcommittee_constructor_exists():
    assert callable(ProgramCommittee.__init__)


def test_programcommittee_constructor_args():
    sig = inspect.signature(ProgramCommittee.__init__)
    params = list(sig.parameters.keys())



def test_co_author_is_not_abstract():
    assert not inspect.isabstract(Co_author)


def test_co_author_constructor_exists():
    assert callable(Co_author.__init__)


def test_co_author_constructor_args():
    sig = inspect.signature(Co_author.__init__)
    params = list(sig.parameters.keys())



def test_document_is_not_abstract():
    assert not inspect.isabstract(Document)


def test_document_constructor_exists():
    assert callable(Document.__init__)


def test_document_constructor_args():
    sig = inspect.signature(Document.__init__)
    params = list(sig.parameters.keys())



def test_cocus::submission_is_not_abstract():
    assert not inspect.isabstract(Cocus::Submission)


def test_cocus::submission_constructor_exists():
    assert callable(Cocus::Submission.__init__)


def test_cocus::submission_constructor_args():
    sig = inspect.signature(Cocus::Submission.__init__)
    params = list(sig.parameters.keys())



def test_cocus::email_is_not_abstract():
    assert not inspect.isabstract(Cocus::Email)


def test_cocus::email_constructor_exists():
    assert callable(Cocus::Email.__init__)


def test_cocus::email_constructor_args():
    sig = inspect.signature(Cocus::Email.__init__)
    params = list(sig.parameters.keys())



def test_cocus::paper_is_not_abstract():
    assert not inspect.isabstract(Cocus::Paper)


def test_cocus::paper_constructor_exists():
    assert callable(Cocus::Paper.__init__)


def test_cocus::paper_constructor_args():
    sig = inspect.signature(Cocus::Paper.__init__)
    params = list(sig.parameters.keys())
    assert "paperID" in params, "Missing parameter 'paperID'"
    assert "title" in params, "Missing parameter 'title'"

def test_cocus::paper_has_paperID():
    assert hasattr(Cocus::Paper, "paperID")
    descriptor = None
    for klass in Cocus::Paper.__mro__:
        if "paperID" in klass.__dict__:
            descriptor = klass.__dict__["paperID"]
            break
    assert isinstance(descriptor, property)

def test_cocus::paper_has_title():
    assert hasattr(Cocus::Paper, "title")
    descriptor = None
    for klass in Cocus::Paper.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_cocus::template_is_not_abstract():
    assert not inspect.isabstract(Cocus::Template)


def test_cocus::template_constructor_exists():
    assert callable(Cocus::Template.__init__)


def test_cocus::template_constructor_args():
    sig = inspect.signature(Cocus::Template.__init__)
    params = list(sig.parameters.keys())



def test_cocus::review_is_not_abstract():
    assert not inspect.isabstract(Cocus::Review)


def test_cocus::review_constructor_exists():
    assert callable(Cocus::Review.__init__)


def test_cocus::review_constructor_args():
    sig = inspect.signature(Cocus::Review.__init__)
    params = list(sig.parameters.keys())



def test_decision_is_not_abstract():
    assert not inspect.isabstract(Decision)


def test_decision_constructor_exists():
    assert callable(Decision.__init__)


def test_decision_constructor_args():
    sig = inspect.signature(Decision.__init__)
    params = list(sig.parameters.keys())



def test_cocus::rejection_is_not_abstract():
    assert not inspect.isabstract(Cocus::Rejection)


def test_cocus::rejection_constructor_exists():
    assert callable(Cocus::Rejection.__init__)


def test_cocus::rejection_constructor_args():
    sig = inspect.signature(Cocus::Rejection.__init__)
    params = list(sig.parameters.keys())



def test_cocus::acceptance_is_not_abstract():
    assert not inspect.isabstract(Cocus::Acceptance)


def test_cocus::acceptance_constructor_exists():
    assert callable(Cocus::Acceptance.__init__)


def test_cocus::acceptance_constructor_args():
    sig = inspect.signature(Cocus::Acceptance.__init__)
    params = list(sig.parameters.keys())



def test_event_is_not_abstract():
    assert not inspect.isabstract(Event)


def test_event_constructor_exists():
    assert callable(Event.__init__)


def test_event_constructor_args():
    sig = inspect.signature(Event.__init__)
    params = list(sig.parameters.keys())



def test_cocus::symposium_is_not_abstract():
    assert not inspect.isabstract(Cocus::Symposium)


def test_cocus::symposium_constructor_exists():
    assert callable(Cocus::Symposium.__init__)


def test_cocus::symposium_constructor_args():
    sig = inspect.signature(Cocus::Symposium.__init__)
    params = list(sig.parameters.keys())



def test_cocus::workshop_is_not_abstract():
    assert not inspect.isabstract(Cocus::Workshop)


def test_cocus::workshop_constructor_exists():
    assert callable(Cocus::Workshop.__init__)


def test_cocus::workshop_constructor_args():
    sig = inspect.signature(Cocus::Workshop.__init__)
    params = list(sig.parameters.keys())



def test_thing_is_not_abstract():
    assert not inspect.isabstract(Thing)


def test_thing_constructor_exists():
    assert callable(Thing.__init__)


def test_thing_constructor_args():
    sig = inspect.signature(Thing.__init__)
    params = list(sig.parameters.keys())



def test_cocus::person_is_not_abstract():
    assert not inspect.isabstract(Cocus::Person)


def test_cocus::person_constructor_exists():
    assert callable(Cocus::Person.__init__)


def test_cocus::person_constructor_args():
    sig = inspect.signature(Cocus::Person.__init__)
    params = list(sig.parameters.keys())
    assert "email" in params, "Missing parameter 'email'"

def test_cocus::person_has_email():
    assert hasattr(Cocus::Person, "email")
    descriptor = None
    for klass in Cocus::Person.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)



def test_cocus::event_is_not_abstract():
    assert not inspect.isabstract(Cocus::Event)


def test_cocus::event_constructor_exists():
    assert callable(Cocus::Event.__init__)


def test_cocus::event_constructor_args():
    sig = inspect.signature(Cocus::Event.__init__)
    params = list(sig.parameters.keys())



def test_cocus::detail_is_not_abstract():
    assert not inspect.isabstract(Cocus::Detail)


def test_cocus::detail_constructor_exists():
    assert callable(Cocus::Detail.__init__)


def test_cocus::detail_constructor_args():
    sig = inspect.signature(Cocus::Detail.__init__)
    params = list(sig.parameters.keys())



def test_cocus::role_is_not_abstract():
    assert not inspect.isabstract(Cocus::Role)


def test_cocus::role_constructor_exists():
    assert callable(Cocus::Role.__init__)


def test_cocus::role_constructor_args():
    sig = inspect.signature(Cocus::Role.__init__)
    params = list(sig.parameters.keys())



def test_cocus::document_is_not_abstract():
    assert not inspect.isabstract(Cocus::Document)


def test_cocus::document_constructor_exists():
    assert callable(Cocus::Document.__init__)


def test_cocus::document_constructor_args():
    sig = inspect.signature(Cocus::Document.__init__)
    params = list(sig.parameters.keys())



def test_cocus::conference_is_not_abstract():
    assert not inspect.isabstract(Cocus::Conference)


def test_cocus::conference_constructor_exists():
    assert callable(Cocus::Conference.__init__)


def test_cocus::conference_constructor_args():
    sig = inspect.signature(Cocus::Conference.__init__)
    params = list(sig.parameters.keys())
    assert "reviewsPerPaper" in params, "Missing parameter 'reviewsPerPaper'"
    assert "siteURL" in params, "Missing parameter 'siteURL'"
    assert "logoURL" in params, "Missing parameter 'logoURL'"
    assert "date" in params, "Missing parameter 'date'"
    assert "acceptsHardcopySubmissions" in params, "Missing parameter 'acceptsHardcopySubmissions'"

def test_cocus::conference_has_reviewsPerPaper():
    assert hasattr(Cocus::Conference, "reviewsPerPaper")
    descriptor = None
    for klass in Cocus::Conference.__mro__:
        if "reviewsPerPaper" in klass.__dict__:
            descriptor = klass.__dict__["reviewsPerPaper"]
            break
    assert isinstance(descriptor, property)

def test_cocus::conference_has_siteURL():
    assert hasattr(Cocus::Conference, "siteURL")
    descriptor = None
    for klass in Cocus::Conference.__mro__:
        if "siteURL" in klass.__dict__:
            descriptor = klass.__dict__["siteURL"]
            break
    assert isinstance(descriptor, property)

def test_cocus::conference_has_logoURL():
    assert hasattr(Cocus::Conference, "logoURL")
    descriptor = None
    for klass in Cocus::Conference.__mro__:
        if "logoURL" in klass.__dict__:
            descriptor = klass.__dict__["logoURL"]
            break
    assert isinstance(descriptor, property)

def test_cocus::conference_has_date():
    assert hasattr(Cocus::Conference, "date")
    descriptor = None
    for klass in Cocus::Conference.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)

def test_cocus::conference_has_acceptsHardcopySubmissions():
    assert hasattr(Cocus::Conference, "acceptsHardcopySubmissions")
    descriptor = None
    for klass in Cocus::Conference.__mro__:
        if "acceptsHardcopySubmissions" in klass.__dict__:
            descriptor = klass.__dict__["acceptsHardcopySubmissions"]
            break
    assert isinstance(descriptor, property)



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



def test_cocus::user_is_not_abstract():
    assert not inspect.isabstract(Cocus::User)


def test_cocus::user_constructor_exists():
    assert callable(Cocus::User.__init__)


def test_cocus::user_constructor_args():
    sig = inspect.signature(Cocus::User.__init__)
    params = list(sig.parameters.keys())



def test_cocus::externalreviewer_is_not_abstract():
    assert not inspect.isabstract(Cocus::ExternalReviewer)


def test_cocus::externalreviewer_constructor_exists():
    assert callable(Cocus::ExternalReviewer.__init__)


def test_cocus::externalreviewer_constructor_args():
    sig = inspect.signature(Cocus::ExternalReviewer.__init__)
    params = list(sig.parameters.keys())



def test_cocus::conferencemember_is_not_abstract():
    assert not inspect.isabstract(Cocus::ConferenceMember)


def test_cocus::conferencemember_constructor_exists():
    assert callable(Cocus::ConferenceMember.__init__)


def test_cocus::conferencemember_constructor_args():
    sig = inspect.signature(Cocus::ConferenceMember.__init__)
    params = list(sig.parameters.keys())



def test_chairman_is_not_abstract():
    assert not inspect.isabstract(Chairman)


def test_chairman_constructor_exists():
    assert callable(Chairman.__init__)


def test_chairman_constructor_args():
    sig = inspect.signature(Chairman.__init__)
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



def test_cocus::administrator_is_not_abstract():
    assert not inspect.isabstract(Cocus::Administrator)


def test_cocus::administrator_constructor_exists():
    assert callable(Cocus::Administrator.__init__)


def test_cocus::administrator_constructor_args():
    sig = inspect.signature(Cocus::Administrator.__init__)
    params = list(sig.parameters.keys())



def test_cocus::committee_is_not_abstract():
    assert not inspect.isabstract(Cocus::Committee)


def test_cocus::committee_constructor_exists():
    assert callable(Cocus::Committee.__init__)


def test_cocus::committee_constructor_args():
    sig = inspect.signature(Cocus::Committee.__init__)
    params = list(sig.parameters.keys())



def test_conferencemember_is_not_abstract():
    assert not inspect.isabstract(ConferenceMember)


def test_conferencemember_constructor_exists():
    assert callable(ConferenceMember.__init__)


def test_conferencemember_constructor_args():
    sig = inspect.signature(ConferenceMember.__init__)
    params = list(sig.parameters.keys())



def test_cocus::programcommitteemember_is_not_abstract():
    assert not inspect.isabstract(Cocus::ProgramCommitteeMember)


def test_cocus::programcommitteemember_constructor_exists():
    assert callable(Cocus::ProgramCommitteeMember.__init__)


def test_cocus::programcommitteemember_constructor_args():
    sig = inspect.signature(Cocus::ProgramCommitteeMember.__init__)
    params = list(sig.parameters.keys())
    assert "maxPapers" in params, "Missing parameter 'maxPapers'"

def test_cocus::programcommitteemember_has_maxPapers():
    assert hasattr(Cocus::ProgramCommitteeMember, "maxPapers")
    descriptor = None
    for klass in Cocus::ProgramCommitteeMember.__mro__:
        if "maxPapers" in klass.__dict__:
            descriptor = klass.__dict__["maxPapers"]
            break
    assert isinstance(descriptor, property)



def test_cocus::associatedchair_is_not_abstract():
    assert not inspect.isabstract(Cocus::AssociatedChair)


def test_cocus::associatedchair_constructor_exists():
    assert callable(Cocus::AssociatedChair.__init__)


def test_cocus::associatedchair_constructor_args():
    sig = inspect.signature(Cocus::AssociatedChair.__init__)
    params = list(sig.parameters.keys())



def test_cocus::conferencechair_is_not_abstract():
    assert not inspect.isabstract(Cocus::ConferenceChair)


def test_cocus::conferencechair_constructor_exists():
    assert callable(Cocus::ConferenceChair.__init__)


def test_cocus::conferencechair_constructor_args():
    sig = inspect.signature(Cocus::ConferenceChair.__init__)
    params = list(sig.parameters.keys())



def test_cocus::author_is_not_abstract():
    assert not inspect.isabstract(Cocus::Author)


def test_cocus::author_constructor_exists():
    assert callable(Cocus::Author.__init__)


def test_cocus::author_constructor_args():
    sig = inspect.signature(Cocus::Author.__init__)
    params = list(sig.parameters.keys())



def test_cocus::chairman_is_not_abstract():
    assert not inspect.isabstract(Cocus::Chairman)


def test_cocus::chairman_constructor_exists():
    assert callable(Cocus::Chairman.__init__)


def test_cocus::chairman_constructor_args():
    sig = inspect.signature(Cocus::Chairman.__init__)
    params = list(sig.parameters.keys())



def test_cocus::reviewer_is_not_abstract():
    assert not inspect.isabstract(Cocus::Reviewer)


def test_cocus::reviewer_constructor_exists():
    assert callable(Cocus::Reviewer.__init__)


def test_cocus::reviewer_constructor_args():
    sig = inspect.signature(Cocus::Reviewer.__init__)
    params = list(sig.parameters.keys())



def test_reviewer_is_not_abstract():
    assert not inspect.isabstract(Reviewer)


def test_reviewer_constructor_exists():
    assert callable(Reviewer.__init__)


def test_reviewer_constructor_args():
    sig = inspect.signature(Reviewer.__init__)
    params = list(sig.parameters.keys())



def test_cocus::meta_reviewer_is_not_abstract():
    assert not inspect.isabstract(Cocus::Meta_Reviewer)


def test_cocus::meta_reviewer_constructor_exists():
    assert callable(Cocus::Meta_Reviewer.__init__)


def test_cocus::meta_reviewer_constructor_args():
    sig = inspect.signature(Cocus::Meta_Reviewer.__init__)
    params = list(sig.parameters.keys())



def test_cocus::thing_is_not_abstract():
    assert not inspect.isabstract(Cocus::Thing)


def test_cocus::thing_constructor_exists():
    assert callable(Cocus::Thing.__init__)


def test_cocus::thing_constructor_args():
    sig = inspect.signature(Cocus::Thing.__init__)
    params = list(sig.parameters.keys())



def test_cocus::bid_is_not_abstract():
    assert not inspect.isabstract(Cocus::Bid)


def test_cocus::bid_constructor_exists():
    assert callable(Cocus::Bid.__init__)


def test_cocus::bid_constructor_args():
    sig = inspect.signature(Cocus::Bid.__init__)
    params = list(sig.parameters.keys())



def test_programcommitteemember_is_not_abstract():
    assert not inspect.isabstract(ProgramCommitteeMember)


def test_programcommitteemember_constructor_exists():
    assert callable(ProgramCommitteeMember.__init__)


def test_programcommitteemember_constructor_args():
    sig = inspect.signature(ProgramCommitteeMember.__init__)
    params = list(sig.parameters.keys())



def test_cocus::programcommitteechair_is_not_abstract():
    assert not inspect.isabstract(Cocus::ProgramCommitteeChair)


def test_cocus::programcommitteechair_constructor_exists():
    assert callable(Cocus::ProgramCommitteeChair.__init__)


def test_cocus::programcommitteechair_constructor_args():
    sig = inspect.signature(Cocus::ProgramCommitteeChair.__init__)
    params = list(sig.parameters.keys())



def test_cocus::programcommittee_is_not_abstract():
    assert not inspect.isabstract(Cocus::ProgramCommittee)


def test_cocus::programcommittee_constructor_exists():
    assert callable(Cocus::ProgramCommittee.__init__)


def test_cocus::programcommittee_constructor_args():
    sig = inspect.signature(Cocus::ProgramCommittee.__init__)
    params = list(sig.parameters.keys())



def test_cocus::preference_is_not_abstract():
    assert not inspect.isabstract(Cocus::Preference)


def test_cocus::preference_constructor_exists():
    assert callable(Cocus::Preference.__init__)


def test_cocus::preference_constructor_args():
    sig = inspect.signature(Cocus::Preference.__init__)
    params = list(sig.parameters.keys())



def test_cocus::decision_is_not_abstract():
    assert not inspect.isabstract(Cocus::Decision)


def test_cocus::decision_constructor_exists():
    assert callable(Cocus::Decision.__init__)


def test_cocus::decision_constructor_args():
    sig = inspect.signature(Cocus::Decision.__init__)
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



def test_cocus::meta-review_is_not_abstract():
    assert not inspect.isabstract(Cocus::Meta-Review)


def test_cocus::meta-review_constructor_exists():
    assert callable(Cocus::Meta-Review.__init__)


def test_cocus::meta-review_constructor_args():
    sig = inspect.signature(Cocus::Meta-Review.__init__)
    params = list(sig.parameters.keys())



def test_paper_is_not_abstract():
    assert not inspect.isabstract(Paper)


def test_paper_constructor_exists():
    assert callable(Paper.__init__)


def test_paper_constructor_args():
    sig = inspect.signature(Paper.__init__)
    params = list(sig.parameters.keys())



def test_cocus::short::paper_is_not_abstract():
    assert not inspect.isabstract(Cocus::Short::Paper)


def test_cocus::short::paper_constructor_exists():
    assert callable(Cocus::Short::Paper.__init__)


def test_cocus::short::paper_constructor_args():
    sig = inspect.signature(Cocus::Short::Paper.__init__)
    params = list(sig.parameters.keys())



def test_cocus::full::paper_is_not_abstract():
    assert not inspect.isabstract(Cocus::Full::Paper)


def test_cocus::full::paper_constructor_exists():
    assert callable(Cocus::Full::Paper.__init__)


def test_cocus::full::paper_constructor_args():
    sig = inspect.signature(Cocus::Full::Paper.__init__)
    params = list(sig.parameters.keys())



def test_cocus::paperfullversion_is_not_abstract():
    assert not inspect.isabstract(Cocus::PaperFullVersion)


def test_cocus::paperfullversion_constructor_exists():
    assert callable(Cocus::PaperFullVersion.__init__)


def test_cocus::paperfullversion_constructor_args():
    sig = inspect.signature(Cocus::PaperFullVersion.__init__)
    params = list(sig.parameters.keys())



def test_cocus::abstract_is_not_abstract():
    assert not inspect.isabstract(Cocus::Abstract)


def test_cocus::abstract_constructor_exists():
    assert callable(Cocus::Abstract.__init__)


def test_cocus::abstract_constructor_args():
    sig = inspect.signature(Cocus::Abstract.__init__)
    params = list(sig.parameters.keys())



def test_cocus::paperabstract_is_not_abstract():
    assert not inspect.isabstract(Cocus::PaperAbstract)


def test_cocus::paperabstract_constructor_exists():
    assert callable(Cocus::PaperAbstract.__init__)


def test_cocus::paperabstract_constructor_args():
    sig = inspect.signature(Cocus::PaperAbstract.__init__)
    params = list(sig.parameters.keys())



def test_cocus::invited::paper_is_not_abstract():
    assert not inspect.isabstract(Cocus::Invited::Paper)


def test_cocus::invited::paper_constructor_exists():
    assert callable(Cocus::Invited::Paper.__init__)


def test_cocus::invited::paper_constructor_args():
    sig = inspect.signature(Cocus::Invited::Paper.__init__)
    params = list(sig.parameters.keys())



def test_bid_is_not_abstract():
    assert not inspect.isabstract(Bid)


def test_bid_constructor_exists():
    assert callable(Bid.__init__)


def test_bid_constructor_args():
    sig = inspect.signature(Bid.__init__)
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
Meta_Reviewer_strategy = st.builds(
    Meta_Reviewer,
)
SubjectArea_strategy = st.builds(
    SubjectArea,
)
Cocus::Activity_strategy = st.builds(
    Cocus::Activity,
)
Cocus::Description_strategy = st.builds(
    Cocus::Description,
)
URL_strategy = st.builds(
    URL,
)
Cocus::Event::URL_strategy = st.builds(
    Cocus::Event::URL,
)
Cocus::Event::Setup_strategy = st.builds(
    Cocus::Event::Setup,
)
Help::Request_strategy = st.builds(
    Help::Request,
)
Cocus::Assistance_strategy = st.builds(
    Cocus::Assistance,
)
Cocus::Feature::Request_strategy = st.builds(
    Cocus::Feature::Request,
)
Cocus::Misc_strategy = st.builds(
    Cocus::Misc,
)
Review::Form_strategy = st.builds(
    Review::Form,
)
Cocus::Review::Form::Setup_strategy = st.builds(
    Cocus::Review::Form::Setup,
)
Cocus::Preview_strategy = st.builds(
    Cocus::Preview,
)
Email_strategy = st.builds(
    Email,
)
Cocus::Group::Email_strategy = st.builds(
    Cocus::Group::Email,
)
Cocus::Rejection::Email_strategy = st.builds(
    Cocus::Rejection::Email,
)
Cocus::Approval::Email_strategy = st.builds(
    Cocus::Approval::Email,
)
Cocus::Notification::Email_strategy = st.builds(
    Cocus::Notification::Email,
)
Cocus::URL_strategy = st.builds(
    Cocus::URL,
)
Account_strategy = st.builds(
    Account,
)
Activity_strategy = st.builds(
    Activity,
)
Cocus::Event::Creation_strategy = st.builds(
    Cocus::Event::Creation,
)
Cocus::Request_strategy = st.builds(
    Cocus::Request,
)
Cocus::Registration_strategy = st.builds(
    Cocus::Registration,
)
Cocus::Event::Approval_strategy = st.builds(
    Cocus::Event::Approval,
)
Cocus::Inforamtion_strategy = st.builds(
    Cocus::Inforamtion,
)
Cocus::Account_strategy = st.builds(
    Cocus::Account,
)
Event::Setup_strategy = st.builds(
    Event::Setup,
)
Cocus::Event::Tracks_strategy = st.builds(
    Cocus::Event::Tracks,
)
Cocus::Paper::Typologies_strategy = st.builds(
    Cocus::Paper::Typologies,
)
Cocus::Review::Form_strategy = st.builds(
    Cocus::Review::Form,
)
Cocus::Email::Template_strategy = st.builds(
    Cocus::Email::Template,
)
Cocus::Submission::Template_strategy = st.builds(
    Cocus::Submission::Template,
)
Cocus::Research::Topic_strategy = st.builds(
    Cocus::Research::Topic,
)
Approval::Email_strategy = st.builds(
    Approval::Email,
)
Inforamtion_strategy = st.builds(
    Inforamtion,
)
Request_strategy = st.builds(
    Request,
)
Cocus::Help::Request_strategy = st.builds(
    Cocus::Help::Request,
)
Role_strategy = st.builds(
    Role,
)
Cocus::Committe::Role_strategy = st.builds(
    Cocus::Committe::Role,
)
Cocus::Head::Role_strategy = st.builds(
    Cocus::Head::Role,
)
Cocus::Admin::Role_strategy = st.builds(
    Cocus::Admin::Role,
)
Cocus::Reviewer::Role_strategy = st.builds(
    Cocus::Reviewer::Role,
)
Cocus::Author::Role_strategy = st.builds(
    Cocus::Author::Role,
)
Event::Tracks_strategy = st.builds(
    Event::Tracks,
)
Cocus::SubjectArea_strategy = st.builds(
    Cocus::SubjectArea,
)
Author_strategy = st.builds(
    Author,
)
Cocus::Corresponding::Author_strategy = st.builds(
    Cocus::Corresponding::Author,
)
Cocus::Co_author_strategy = st.builds(
    Cocus::Co_author,
)
Cocus::AuthorNotReviewer_strategy = st.builds(
    Cocus::AuthorNotReviewer,
)
ProgramCommittee_strategy = st.builds(
    ProgramCommittee,
)
Co_author_strategy = st.builds(
    Co_author,
)
Document_strategy = st.builds(
    Document,
)
Cocus::Submission_strategy = st.builds(
    Cocus::Submission,
)
Cocus::Email_strategy = st.builds(
    Cocus::Email,
)
Cocus::Paper_strategy = st.builds(
    Cocus::Paper,
    paperID=
        safe_text,
    title=
        safe_text
)
Cocus::Template_strategy = st.builds(
    Cocus::Template,
)
Cocus::Review_strategy = st.builds(
    Cocus::Review,
)
Decision_strategy = st.builds(
    Decision,
)
Cocus::Rejection_strategy = st.builds(
    Cocus::Rejection,
)
Cocus::Acceptance_strategy = st.builds(
    Cocus::Acceptance,
)
Event_strategy = st.builds(
    Event,
)
Cocus::Symposium_strategy = st.builds(
    Cocus::Symposium,
)
Cocus::Workshop_strategy = st.builds(
    Cocus::Workshop,
)
Thing_strategy = st.builds(
    Thing,
)
Cocus::Person_strategy = st.builds(
    Cocus::Person,
    email=
        safe_text
)
Cocus::Event_strategy = st.builds(
    Cocus::Event,
)
Cocus::Detail_strategy = st.builds(
    Cocus::Detail,
)
Cocus::Role_strategy = st.builds(
    Cocus::Role,
)
Cocus::Document_strategy = st.builds(
    Cocus::Document,
)
Cocus::Conference_strategy = st.builds(
    Cocus::Conference,
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
Conference_strategy = st.builds(
    Conference,
)
Person_strategy = st.builds(
    Person,
)
Cocus::User_strategy = st.builds(
    Cocus::User,
)
Cocus::ExternalReviewer_strategy = st.builds(
    Cocus::ExternalReviewer,
)
Cocus::ConferenceMember_strategy = st.builds(
    Cocus::ConferenceMember,
)
Chairman_strategy = st.builds(
    Chairman,
)
Administrator_strategy = st.builds(
    Administrator,
)
User_strategy = st.builds(
    User,
)
Cocus::Administrator_strategy = st.builds(
    Cocus::Administrator,
)
Cocus::Committee_strategy = st.builds(
    Cocus::Committee,
)
ConferenceMember_strategy = st.builds(
    ConferenceMember,
)
Cocus::ProgramCommitteeMember_strategy = st.builds(
    Cocus::ProgramCommitteeMember,
    maxPapers=
        safe_text
)
Cocus::AssociatedChair_strategy = st.builds(
    Cocus::AssociatedChair,
)
Cocus::ConferenceChair_strategy = st.builds(
    Cocus::ConferenceChair,
)
Cocus::Author_strategy = st.builds(
    Cocus::Author,
)
Cocus::Chairman_strategy = st.builds(
    Cocus::Chairman,
)
Cocus::Reviewer_strategy = st.builds(
    Cocus::Reviewer,
)
Reviewer_strategy = st.builds(
    Reviewer,
)
Cocus::Meta_Reviewer_strategy = st.builds(
    Cocus::Meta_Reviewer,
)
Cocus::Thing_strategy = st.builds(
    Cocus::Thing,
)
Cocus::Bid_strategy = st.builds(
    Cocus::Bid,
)
ProgramCommitteeMember_strategy = st.builds(
    ProgramCommitteeMember,
)
Cocus::ProgramCommitteeChair_strategy = st.builds(
    Cocus::ProgramCommitteeChair,
)
Cocus::ProgramCommittee_strategy = st.builds(
    Cocus::ProgramCommittee,
)
Cocus::Preference_strategy = st.builds(
    Cocus::Preference,
)
Cocus::Decision_strategy = st.builds(
    Cocus::Decision,
)
ExternalReviewer_strategy = st.builds(
    ExternalReviewer,
)
Review_strategy = st.builds(
    Review,
)
Cocus::Meta-Review_strategy = st.builds(
    Cocus::Meta-Review,
)
Paper_strategy = st.builds(
    Paper,
)
Cocus::Short::Paper_strategy = st.builds(
    Cocus::Short::Paper,
)
Cocus::Full::Paper_strategy = st.builds(
    Cocus::Full::Paper,
)
Cocus::PaperFullVersion_strategy = st.builds(
    Cocus::PaperFullVersion,
)
Cocus::Abstract_strategy = st.builds(
    Cocus::Abstract,
)
Cocus::PaperAbstract_strategy = st.builds(
    Cocus::PaperAbstract,
)
Cocus::Invited::Paper_strategy = st.builds(
    Cocus::Invited::Paper,
)
Bid_strategy = st.builds(
    Bid,
)

@given(instance=Meta_Reviewer_strategy)
@settings(max_examples=50)
def test_meta_reviewer_instantiation(instance):
    assert isinstance(instance, Meta_Reviewer)

@given(instance=SubjectArea_strategy)
@settings(max_examples=50)
def test_subjectarea_instantiation(instance):
    assert isinstance(instance, SubjectArea)

@given(instance=Cocus::Activity_strategy)
@settings(max_examples=50)
def test_cocus::activity_instantiation(instance):
    assert isinstance(instance, Cocus::Activity)

@given(instance=Cocus::Description_strategy)
@settings(max_examples=50)
def test_cocus::description_instantiation(instance):
    assert isinstance(instance, Cocus::Description)

@given(instance=URL_strategy)
@settings(max_examples=50)
def test_url_instantiation(instance):
    assert isinstance(instance, URL)

@given(instance=Cocus::Event::URL_strategy)
@settings(max_examples=50)
def test_cocus::event::url_instantiation(instance):
    assert isinstance(instance, Cocus::Event::URL)

@given(instance=Cocus::Event::Setup_strategy)
@settings(max_examples=50)
def test_cocus::event::setup_instantiation(instance):
    assert isinstance(instance, Cocus::Event::Setup)

@given(instance=Help::Request_strategy)
@settings(max_examples=50)
def test_help::request_instantiation(instance):
    assert isinstance(instance, Help::Request)

@given(instance=Cocus::Assistance_strategy)
@settings(max_examples=50)
def test_cocus::assistance_instantiation(instance):
    assert isinstance(instance, Cocus::Assistance)

@given(instance=Cocus::Feature::Request_strategy)
@settings(max_examples=50)
def test_cocus::feature::request_instantiation(instance):
    assert isinstance(instance, Cocus::Feature::Request)

@given(instance=Cocus::Misc_strategy)
@settings(max_examples=50)
def test_cocus::misc_instantiation(instance):
    assert isinstance(instance, Cocus::Misc)

@given(instance=Review::Form_strategy)
@settings(max_examples=50)
def test_review::form_instantiation(instance):
    assert isinstance(instance, Review::Form)

@given(instance=Cocus::Review::Form::Setup_strategy)
@settings(max_examples=50)
def test_cocus::review::form::setup_instantiation(instance):
    assert isinstance(instance, Cocus::Review::Form::Setup)

@given(instance=Cocus::Preview_strategy)
@settings(max_examples=50)
def test_cocus::preview_instantiation(instance):
    assert isinstance(instance, Cocus::Preview)

@given(instance=Email_strategy)
@settings(max_examples=50)
def test_email_instantiation(instance):
    assert isinstance(instance, Email)

@given(instance=Cocus::Group::Email_strategy)
@settings(max_examples=50)
def test_cocus::group::email_instantiation(instance):
    assert isinstance(instance, Cocus::Group::Email)

@given(instance=Cocus::Rejection::Email_strategy)
@settings(max_examples=50)
def test_cocus::rejection::email_instantiation(instance):
    assert isinstance(instance, Cocus::Rejection::Email)

@given(instance=Cocus::Approval::Email_strategy)
@settings(max_examples=50)
def test_cocus::approval::email_instantiation(instance):
    assert isinstance(instance, Cocus::Approval::Email)

@given(instance=Cocus::Notification::Email_strategy)
@settings(max_examples=50)
def test_cocus::notification::email_instantiation(instance):
    assert isinstance(instance, Cocus::Notification::Email)

@given(instance=Cocus::URL_strategy)
@settings(max_examples=50)
def test_cocus::url_instantiation(instance):
    assert isinstance(instance, Cocus::URL)

@given(instance=Account_strategy)
@settings(max_examples=50)
def test_account_instantiation(instance):
    assert isinstance(instance, Account)

@given(instance=Activity_strategy)
@settings(max_examples=50)
def test_activity_instantiation(instance):
    assert isinstance(instance, Activity)

@given(instance=Cocus::Event::Creation_strategy)
@settings(max_examples=50)
def test_cocus::event::creation_instantiation(instance):
    assert isinstance(instance, Cocus::Event::Creation)

@given(instance=Cocus::Request_strategy)
@settings(max_examples=50)
def test_cocus::request_instantiation(instance):
    assert isinstance(instance, Cocus::Request)

@given(instance=Cocus::Registration_strategy)
@settings(max_examples=50)
def test_cocus::registration_instantiation(instance):
    assert isinstance(instance, Cocus::Registration)

@given(instance=Cocus::Event::Approval_strategy)
@settings(max_examples=50)
def test_cocus::event::approval_instantiation(instance):
    assert isinstance(instance, Cocus::Event::Approval)

@given(instance=Cocus::Inforamtion_strategy)
@settings(max_examples=50)
def test_cocus::inforamtion_instantiation(instance):
    assert isinstance(instance, Cocus::Inforamtion)

@given(instance=Cocus::Account_strategy)
@settings(max_examples=50)
def test_cocus::account_instantiation(instance):
    assert isinstance(instance, Cocus::Account)

@given(instance=Event::Setup_strategy)
@settings(max_examples=50)
def test_event::setup_instantiation(instance):
    assert isinstance(instance, Event::Setup)

@given(instance=Cocus::Event::Tracks_strategy)
@settings(max_examples=50)
def test_cocus::event::tracks_instantiation(instance):
    assert isinstance(instance, Cocus::Event::Tracks)

@given(instance=Cocus::Paper::Typologies_strategy)
@settings(max_examples=50)
def test_cocus::paper::typologies_instantiation(instance):
    assert isinstance(instance, Cocus::Paper::Typologies)

@given(instance=Cocus::Review::Form_strategy)
@settings(max_examples=50)
def test_cocus::review::form_instantiation(instance):
    assert isinstance(instance, Cocus::Review::Form)

@given(instance=Cocus::Email::Template_strategy)
@settings(max_examples=50)
def test_cocus::email::template_instantiation(instance):
    assert isinstance(instance, Cocus::Email::Template)

@given(instance=Cocus::Submission::Template_strategy)
@settings(max_examples=50)
def test_cocus::submission::template_instantiation(instance):
    assert isinstance(instance, Cocus::Submission::Template)

@given(instance=Cocus::Research::Topic_strategy)
@settings(max_examples=50)
def test_cocus::research::topic_instantiation(instance):
    assert isinstance(instance, Cocus::Research::Topic)

@given(instance=Approval::Email_strategy)
@settings(max_examples=50)
def test_approval::email_instantiation(instance):
    assert isinstance(instance, Approval::Email)

@given(instance=Inforamtion_strategy)
@settings(max_examples=50)
def test_inforamtion_instantiation(instance):
    assert isinstance(instance, Inforamtion)

@given(instance=Request_strategy)
@settings(max_examples=50)
def test_request_instantiation(instance):
    assert isinstance(instance, Request)

@given(instance=Cocus::Help::Request_strategy)
@settings(max_examples=50)
def test_cocus::help::request_instantiation(instance):
    assert isinstance(instance, Cocus::Help::Request)

@given(instance=Role_strategy)
@settings(max_examples=50)
def test_role_instantiation(instance):
    assert isinstance(instance, Role)

@given(instance=Cocus::Committe::Role_strategy)
@settings(max_examples=50)
def test_cocus::committe::role_instantiation(instance):
    assert isinstance(instance, Cocus::Committe::Role)

@given(instance=Cocus::Head::Role_strategy)
@settings(max_examples=50)
def test_cocus::head::role_instantiation(instance):
    assert isinstance(instance, Cocus::Head::Role)

@given(instance=Cocus::Admin::Role_strategy)
@settings(max_examples=50)
def test_cocus::admin::role_instantiation(instance):
    assert isinstance(instance, Cocus::Admin::Role)

@given(instance=Cocus::Reviewer::Role_strategy)
@settings(max_examples=50)
def test_cocus::reviewer::role_instantiation(instance):
    assert isinstance(instance, Cocus::Reviewer::Role)

@given(instance=Cocus::Author::Role_strategy)
@settings(max_examples=50)
def test_cocus::author::role_instantiation(instance):
    assert isinstance(instance, Cocus::Author::Role)

@given(instance=Event::Tracks_strategy)
@settings(max_examples=50)
def test_event::tracks_instantiation(instance):
    assert isinstance(instance, Event::Tracks)

@given(instance=Cocus::SubjectArea_strategy)
@settings(max_examples=50)
def test_cocus::subjectarea_instantiation(instance):
    assert isinstance(instance, Cocus::SubjectArea)

@given(instance=Author_strategy)
@settings(max_examples=50)
def test_author_instantiation(instance):
    assert isinstance(instance, Author)

@given(instance=Cocus::Corresponding::Author_strategy)
@settings(max_examples=50)
def test_cocus::corresponding::author_instantiation(instance):
    assert isinstance(instance, Cocus::Corresponding::Author)

@given(instance=Cocus::Co_author_strategy)
@settings(max_examples=50)
def test_cocus::co_author_instantiation(instance):
    assert isinstance(instance, Cocus::Co_author)

@given(instance=Cocus::AuthorNotReviewer_strategy)
@settings(max_examples=50)
def test_cocus::authornotreviewer_instantiation(instance):
    assert isinstance(instance, Cocus::AuthorNotReviewer)

@given(instance=ProgramCommittee_strategy)
@settings(max_examples=50)
def test_programcommittee_instantiation(instance):
    assert isinstance(instance, ProgramCommittee)

@given(instance=Co_author_strategy)
@settings(max_examples=50)
def test_co_author_instantiation(instance):
    assert isinstance(instance, Co_author)

@given(instance=Document_strategy)
@settings(max_examples=50)
def test_document_instantiation(instance):
    assert isinstance(instance, Document)

@given(instance=Cocus::Submission_strategy)
@settings(max_examples=50)
def test_cocus::submission_instantiation(instance):
    assert isinstance(instance, Cocus::Submission)

@given(instance=Cocus::Email_strategy)
@settings(max_examples=50)
def test_cocus::email_instantiation(instance):
    assert isinstance(instance, Cocus::Email)

@given(instance=Cocus::Paper_strategy)
@settings(max_examples=50)
def test_cocus::paper_instantiation(instance):
    assert isinstance(instance, Cocus::Paper)

@given(instance=Cocus::Paper_strategy)
def test_cocus::paper_paperID_type(instance):
    assert isinstance(instance.paperID, str)


@given(instance=Cocus::Paper_strategy)
def test_cocus::paper_paperID_setter(instance):
    original = instance.paperID
    instance.paperID = original
    assert instance.paperID == original

@given(instance=Cocus::Paper_strategy)
def test_cocus::paper_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=Cocus::Paper_strategy)
def test_cocus::paper_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=Cocus::Template_strategy)
@settings(max_examples=50)
def test_cocus::template_instantiation(instance):
    assert isinstance(instance, Cocus::Template)

@given(instance=Cocus::Review_strategy)
@settings(max_examples=50)
def test_cocus::review_instantiation(instance):
    assert isinstance(instance, Cocus::Review)

@given(instance=Decision_strategy)
@settings(max_examples=50)
def test_decision_instantiation(instance):
    assert isinstance(instance, Decision)

@given(instance=Cocus::Rejection_strategy)
@settings(max_examples=50)
def test_cocus::rejection_instantiation(instance):
    assert isinstance(instance, Cocus::Rejection)

@given(instance=Cocus::Acceptance_strategy)
@settings(max_examples=50)
def test_cocus::acceptance_instantiation(instance):
    assert isinstance(instance, Cocus::Acceptance)

@given(instance=Event_strategy)
@settings(max_examples=50)
def test_event_instantiation(instance):
    assert isinstance(instance, Event)

@given(instance=Cocus::Symposium_strategy)
@settings(max_examples=50)
def test_cocus::symposium_instantiation(instance):
    assert isinstance(instance, Cocus::Symposium)

@given(instance=Cocus::Workshop_strategy)
@settings(max_examples=50)
def test_cocus::workshop_instantiation(instance):
    assert isinstance(instance, Cocus::Workshop)

@given(instance=Thing_strategy)
@settings(max_examples=50)
def test_thing_instantiation(instance):
    assert isinstance(instance, Thing)

@given(instance=Cocus::Person_strategy)
@settings(max_examples=50)
def test_cocus::person_instantiation(instance):
    assert isinstance(instance, Cocus::Person)

@given(instance=Cocus::Person_strategy)
def test_cocus::person_email_type(instance):
    assert isinstance(instance.email, str)


@given(instance=Cocus::Person_strategy)
def test_cocus::person_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original

@given(instance=Cocus::Event_strategy)
@settings(max_examples=50)
def test_cocus::event_instantiation(instance):
    assert isinstance(instance, Cocus::Event)

@given(instance=Cocus::Detail_strategy)
@settings(max_examples=50)
def test_cocus::detail_instantiation(instance):
    assert isinstance(instance, Cocus::Detail)

@given(instance=Cocus::Role_strategy)
@settings(max_examples=50)
def test_cocus::role_instantiation(instance):
    assert isinstance(instance, Cocus::Role)

@given(instance=Cocus::Document_strategy)
@settings(max_examples=50)
def test_cocus::document_instantiation(instance):
    assert isinstance(instance, Cocus::Document)

@given(instance=Cocus::Conference_strategy)
@settings(max_examples=50)
def test_cocus::conference_instantiation(instance):
    assert isinstance(instance, Cocus::Conference)

@given(instance=Cocus::Conference_strategy)
def test_cocus::conference_reviewsPerPaper_type(instance):
    assert isinstance(instance.reviewsPerPaper, str)


@given(instance=Cocus::Conference_strategy)
def test_cocus::conference_reviewsPerPaper_setter(instance):
    original = instance.reviewsPerPaper
    instance.reviewsPerPaper = original
    assert instance.reviewsPerPaper == original

@given(instance=Cocus::Conference_strategy)
def test_cocus::conference_siteURL_type(instance):
    assert isinstance(instance.siteURL, str)


@given(instance=Cocus::Conference_strategy)
def test_cocus::conference_siteURL_setter(instance):
    original = instance.siteURL
    instance.siteURL = original
    assert instance.siteURL == original

@given(instance=Cocus::Conference_strategy)
def test_cocus::conference_logoURL_type(instance):
    assert isinstance(instance.logoURL, str)


@given(instance=Cocus::Conference_strategy)
def test_cocus::conference_logoURL_setter(instance):
    original = instance.logoURL
    instance.logoURL = original
    assert instance.logoURL == original

@given(instance=Cocus::Conference_strategy)
def test_cocus::conference_date_type(instance):
    assert isinstance(instance.date, str)


@given(instance=Cocus::Conference_strategy)
def test_cocus::conference_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original

@given(instance=Cocus::Conference_strategy)
def test_cocus::conference_acceptsHardcopySubmissions_type(instance):
    assert isinstance(instance.acceptsHardcopySubmissions, str)


@given(instance=Cocus::Conference_strategy)
def test_cocus::conference_acceptsHardcopySubmissions_setter(instance):
    original = instance.acceptsHardcopySubmissions
    instance.acceptsHardcopySubmissions = original
    assert instance.acceptsHardcopySubmissions == original

@given(instance=Conference_strategy)
@settings(max_examples=50)
def test_conference_instantiation(instance):
    assert isinstance(instance, Conference)

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)

@given(instance=Cocus::User_strategy)
@settings(max_examples=50)
def test_cocus::user_instantiation(instance):
    assert isinstance(instance, Cocus::User)

@given(instance=Cocus::ExternalReviewer_strategy)
@settings(max_examples=50)
def test_cocus::externalreviewer_instantiation(instance):
    assert isinstance(instance, Cocus::ExternalReviewer)

@given(instance=Cocus::ConferenceMember_strategy)
@settings(max_examples=50)
def test_cocus::conferencemember_instantiation(instance):
    assert isinstance(instance, Cocus::ConferenceMember)

@given(instance=Chairman_strategy)
@settings(max_examples=50)
def test_chairman_instantiation(instance):
    assert isinstance(instance, Chairman)

@given(instance=Administrator_strategy)
@settings(max_examples=50)
def test_administrator_instantiation(instance):
    assert isinstance(instance, Administrator)

@given(instance=User_strategy)
@settings(max_examples=50)
def test_user_instantiation(instance):
    assert isinstance(instance, User)

@given(instance=Cocus::Administrator_strategy)
@settings(max_examples=50)
def test_cocus::administrator_instantiation(instance):
    assert isinstance(instance, Cocus::Administrator)

@given(instance=Cocus::Committee_strategy)
@settings(max_examples=50)
def test_cocus::committee_instantiation(instance):
    assert isinstance(instance, Cocus::Committee)

@given(instance=ConferenceMember_strategy)
@settings(max_examples=50)
def test_conferencemember_instantiation(instance):
    assert isinstance(instance, ConferenceMember)

@given(instance=Cocus::ProgramCommitteeMember_strategy)
@settings(max_examples=50)
def test_cocus::programcommitteemember_instantiation(instance):
    assert isinstance(instance, Cocus::ProgramCommitteeMember)

@given(instance=Cocus::ProgramCommitteeMember_strategy)
def test_cocus::programcommitteemember_maxPapers_type(instance):
    assert isinstance(instance.maxPapers, str)


@given(instance=Cocus::ProgramCommitteeMember_strategy)
def test_cocus::programcommitteemember_maxPapers_setter(instance):
    original = instance.maxPapers
    instance.maxPapers = original
    assert instance.maxPapers == original

@given(instance=Cocus::AssociatedChair_strategy)
@settings(max_examples=50)
def test_cocus::associatedchair_instantiation(instance):
    assert isinstance(instance, Cocus::AssociatedChair)

@given(instance=Cocus::ConferenceChair_strategy)
@settings(max_examples=50)
def test_cocus::conferencechair_instantiation(instance):
    assert isinstance(instance, Cocus::ConferenceChair)

@given(instance=Cocus::Author_strategy)
@settings(max_examples=50)
def test_cocus::author_instantiation(instance):
    assert isinstance(instance, Cocus::Author)

@given(instance=Cocus::Chairman_strategy)
@settings(max_examples=50)
def test_cocus::chairman_instantiation(instance):
    assert isinstance(instance, Cocus::Chairman)

@given(instance=Cocus::Reviewer_strategy)
@settings(max_examples=50)
def test_cocus::reviewer_instantiation(instance):
    assert isinstance(instance, Cocus::Reviewer)

@given(instance=Reviewer_strategy)
@settings(max_examples=50)
def test_reviewer_instantiation(instance):
    assert isinstance(instance, Reviewer)

@given(instance=Cocus::Meta_Reviewer_strategy)
@settings(max_examples=50)
def test_cocus::meta_reviewer_instantiation(instance):
    assert isinstance(instance, Cocus::Meta_Reviewer)

@given(instance=Cocus::Thing_strategy)
@settings(max_examples=50)
def test_cocus::thing_instantiation(instance):
    assert isinstance(instance, Cocus::Thing)

@given(instance=Cocus::Bid_strategy)
@settings(max_examples=50)
def test_cocus::bid_instantiation(instance):
    assert isinstance(instance, Cocus::Bid)

@given(instance=ProgramCommitteeMember_strategy)
@settings(max_examples=50)
def test_programcommitteemember_instantiation(instance):
    assert isinstance(instance, ProgramCommitteeMember)

@given(instance=Cocus::ProgramCommitteeChair_strategy)
@settings(max_examples=50)
def test_cocus::programcommitteechair_instantiation(instance):
    assert isinstance(instance, Cocus::ProgramCommitteeChair)

@given(instance=Cocus::ProgramCommittee_strategy)
@settings(max_examples=50)
def test_cocus::programcommittee_instantiation(instance):
    assert isinstance(instance, Cocus::ProgramCommittee)

@given(instance=Cocus::Preference_strategy)
@settings(max_examples=50)
def test_cocus::preference_instantiation(instance):
    assert isinstance(instance, Cocus::Preference)

@given(instance=Cocus::Decision_strategy)
@settings(max_examples=50)
def test_cocus::decision_instantiation(instance):
    assert isinstance(instance, Cocus::Decision)

@given(instance=ExternalReviewer_strategy)
@settings(max_examples=50)
def test_externalreviewer_instantiation(instance):
    assert isinstance(instance, ExternalReviewer)

@given(instance=Review_strategy)
@settings(max_examples=50)
def test_review_instantiation(instance):
    assert isinstance(instance, Review)

@given(instance=Cocus::Meta-Review_strategy)
@settings(max_examples=50)
def test_cocus::meta-review_instantiation(instance):
    assert isinstance(instance, Cocus::Meta-Review)

@given(instance=Paper_strategy)
@settings(max_examples=50)
def test_paper_instantiation(instance):
    assert isinstance(instance, Paper)

@given(instance=Cocus::Short::Paper_strategy)
@settings(max_examples=50)
def test_cocus::short::paper_instantiation(instance):
    assert isinstance(instance, Cocus::Short::Paper)

@given(instance=Cocus::Full::Paper_strategy)
@settings(max_examples=50)
def test_cocus::full::paper_instantiation(instance):
    assert isinstance(instance, Cocus::Full::Paper)

@given(instance=Cocus::PaperFullVersion_strategy)
@settings(max_examples=50)
def test_cocus::paperfullversion_instantiation(instance):
    assert isinstance(instance, Cocus::PaperFullVersion)

@given(instance=Cocus::Abstract_strategy)
@settings(max_examples=50)
def test_cocus::abstract_instantiation(instance):
    assert isinstance(instance, Cocus::Abstract)

@given(instance=Cocus::PaperAbstract_strategy)
@settings(max_examples=50)
def test_cocus::paperabstract_instantiation(instance):
    assert isinstance(instance, Cocus::PaperAbstract)

@given(instance=Cocus::Invited::Paper_strategy)
@settings(max_examples=50)
def test_cocus::invited::paper_instantiation(instance):
    assert isinstance(instance, Cocus::Invited::Paper)

@given(instance=Bid_strategy)
@settings(max_examples=50)
def test_bid_instantiation(instance):
    assert isinstance(instance, Bid)
