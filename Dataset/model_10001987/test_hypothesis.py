import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Admin,
    Election,
    Post,
    BallotInformation,
    Voter,
    Candidate,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_admin_is_not_abstract():
    assert not inspect.isabstract(Admin)


def test_admin_constructor_exists():
    assert callable(Admin.__init__)


def test_admin_constructor_args():
    sig = inspect.signature(Admin.__init__)
    params = list(sig.parameters.keys())
    assert "AdminID" in params, "Missing parameter 'AdminID'"
    assert "AminName" in params, "Missing parameter 'AminName'"
    assert "UserLogin" in params, "Missing parameter 'UserLogin'"

def test_admin_has_AdminID():
    assert hasattr(Admin, "AdminID")
    descriptor = None
    for klass in Admin.__mro__:
        if "AdminID" in klass.__dict__:
            descriptor = klass.__dict__["AdminID"]
            break
    assert isinstance(descriptor, property)

def test_admin_has_AminName():
    assert hasattr(Admin, "AminName")
    descriptor = None
    for klass in Admin.__mro__:
        if "AminName" in klass.__dict__:
            descriptor = klass.__dict__["AminName"]
            break
    assert isinstance(descriptor, property)

def test_admin_has_UserLogin():
    assert hasattr(Admin, "UserLogin")
    descriptor = None
    for klass in Admin.__mro__:
        if "UserLogin" in klass.__dict__:
            descriptor = klass.__dict__["UserLogin"]
            break
    assert isinstance(descriptor, property)



def test_election_is_not_abstract():
    assert not inspect.isabstract(Election)


def test_election_constructor_exists():
    assert callable(Election.__init__)


def test_election_constructor_args():
    sig = inspect.signature(Election.__init__)
    params = list(sig.parameters.keys())
    assert "ElectionDate" in params, "Missing parameter 'ElectionDate'"
    assert "ElectionCriteria" in params, "Missing parameter 'ElectionCriteria'"
    assert "ElectionName" in params, "Missing parameter 'ElectionName'"
    assert "ElectionID" in params, "Missing parameter 'ElectionID'"

def test_election_has_ElectionDate():
    assert hasattr(Election, "ElectionDate")
    descriptor = None
    for klass in Election.__mro__:
        if "ElectionDate" in klass.__dict__:
            descriptor = klass.__dict__["ElectionDate"]
            break
    assert isinstance(descriptor, property)

def test_election_has_ElectionCriteria():
    assert hasattr(Election, "ElectionCriteria")
    descriptor = None
    for klass in Election.__mro__:
        if "ElectionCriteria" in klass.__dict__:
            descriptor = klass.__dict__["ElectionCriteria"]
            break
    assert isinstance(descriptor, property)

def test_election_has_ElectionName():
    assert hasattr(Election, "ElectionName")
    descriptor = None
    for klass in Election.__mro__:
        if "ElectionName" in klass.__dict__:
            descriptor = klass.__dict__["ElectionName"]
            break
    assert isinstance(descriptor, property)

def test_election_has_ElectionID():
    assert hasattr(Election, "ElectionID")
    descriptor = None
    for klass in Election.__mro__:
        if "ElectionID" in klass.__dict__:
            descriptor = klass.__dict__["ElectionID"]
            break
    assert isinstance(descriptor, property)



def test_post_is_not_abstract():
    assert not inspect.isabstract(Post)


def test_post_constructor_exists():
    assert callable(Post.__init__)


def test_post_constructor_args():
    sig = inspect.signature(Post.__init__)
    params = list(sig.parameters.keys())
    assert "PostDesc" in params, "Missing parameter 'PostDesc'"
    assert "PostId" in params, "Missing parameter 'PostId'"
    assert "PostElectionId" in params, "Missing parameter 'PostElectionId'"

def test_post_has_PostDesc():
    assert hasattr(Post, "PostDesc")
    descriptor = None
    for klass in Post.__mro__:
        if "PostDesc" in klass.__dict__:
            descriptor = klass.__dict__["PostDesc"]
            break
    assert isinstance(descriptor, property)

def test_post_has_PostId():
    assert hasattr(Post, "PostId")
    descriptor = None
    for klass in Post.__mro__:
        if "PostId" in klass.__dict__:
            descriptor = klass.__dict__["PostId"]
            break
    assert isinstance(descriptor, property)

def test_post_has_PostElectionId():
    assert hasattr(Post, "PostElectionId")
    descriptor = None
    for klass in Post.__mro__:
        if "PostElectionId" in klass.__dict__:
            descriptor = klass.__dict__["PostElectionId"]
            break
    assert isinstance(descriptor, property)



def test_ballotinformation_is_not_abstract():
    assert not inspect.isabstract(BallotInformation)


def test_ballotinformation_constructor_exists():
    assert callable(BallotInformation.__init__)


def test_ballotinformation_constructor_args():
    sig = inspect.signature(BallotInformation.__init__)
    params = list(sig.parameters.keys())
    assert "BallotPropID" in params, "Missing parameter 'BallotPropID'"
    assert "BallotPropResults" in params, "Missing parameter 'BallotPropResults'"
    assert "BallotVotersID" in params, "Missing parameter 'BallotVotersID'"
    assert "BallotID" in params, "Missing parameter 'BallotID'"
    assert "BallotElectionID" in params, "Missing parameter 'BallotElectionID'"
    assert "BallotPropBallotID" in params, "Missing parameter 'BallotPropBallotID'"

def test_ballotinformation_has_BallotPropID():
    assert hasattr(BallotInformation, "BallotPropID")
    descriptor = None
    for klass in BallotInformation.__mro__:
        if "BallotPropID" in klass.__dict__:
            descriptor = klass.__dict__["BallotPropID"]
            break
    assert isinstance(descriptor, property)

def test_ballotinformation_has_BallotPropResults():
    assert hasattr(BallotInformation, "BallotPropResults")
    descriptor = None
    for klass in BallotInformation.__mro__:
        if "BallotPropResults" in klass.__dict__:
            descriptor = klass.__dict__["BallotPropResults"]
            break
    assert isinstance(descriptor, property)

def test_ballotinformation_has_BallotVotersID():
    assert hasattr(BallotInformation, "BallotVotersID")
    descriptor = None
    for klass in BallotInformation.__mro__:
        if "BallotVotersID" in klass.__dict__:
            descriptor = klass.__dict__["BallotVotersID"]
            break
    assert isinstance(descriptor, property)

def test_ballotinformation_has_BallotID():
    assert hasattr(BallotInformation, "BallotID")
    descriptor = None
    for klass in BallotInformation.__mro__:
        if "BallotID" in klass.__dict__:
            descriptor = klass.__dict__["BallotID"]
            break
    assert isinstance(descriptor, property)

def test_ballotinformation_has_BallotElectionID():
    assert hasattr(BallotInformation, "BallotElectionID")
    descriptor = None
    for klass in BallotInformation.__mro__:
        if "BallotElectionID" in klass.__dict__:
            descriptor = klass.__dict__["BallotElectionID"]
            break
    assert isinstance(descriptor, property)

def test_ballotinformation_has_BallotPropBallotID():
    assert hasattr(BallotInformation, "BallotPropBallotID")
    descriptor = None
    for klass in BallotInformation.__mro__:
        if "BallotPropBallotID" in klass.__dict__:
            descriptor = klass.__dict__["BallotPropBallotID"]
            break
    assert isinstance(descriptor, property)



def test_voter_is_not_abstract():
    assert not inspect.isabstract(Voter)


def test_voter_constructor_exists():
    assert callable(Voter.__init__)


def test_voter_constructor_args():
    sig = inspect.signature(Voter.__init__)
    params = list(sig.parameters.keys())
    assert "student_faculty_ID" in params, "Missing parameter 'student_faculty_ID'"
    assert "Address" in params, "Missing parameter 'Address'"
    assert "Eligibilty" in params, "Missing parameter 'Eligibilty'"
    assert "Age" in params, "Missing parameter 'Age'"
    assert "Name" in params, "Missing parameter 'Name'"

def test_voter_has_student_faculty_ID():
    assert hasattr(Voter, "student_faculty_ID")
    descriptor = None
    for klass in Voter.__mro__:
        if "student_faculty_ID" in klass.__dict__:
            descriptor = klass.__dict__["student_faculty_ID"]
            break
    assert isinstance(descriptor, property)

def test_voter_has_Address():
    assert hasattr(Voter, "Address")
    descriptor = None
    for klass in Voter.__mro__:
        if "Address" in klass.__dict__:
            descriptor = klass.__dict__["Address"]
            break
    assert isinstance(descriptor, property)

def test_voter_has_Eligibilty():
    assert hasattr(Voter, "Eligibilty")
    descriptor = None
    for klass in Voter.__mro__:
        if "Eligibilty" in klass.__dict__:
            descriptor = klass.__dict__["Eligibilty"]
            break
    assert isinstance(descriptor, property)

def test_voter_has_Age():
    assert hasattr(Voter, "Age")
    descriptor = None
    for klass in Voter.__mro__:
        if "Age" in klass.__dict__:
            descriptor = klass.__dict__["Age"]
            break
    assert isinstance(descriptor, property)

def test_voter_has_Name():
    assert hasattr(Voter, "Name")
    descriptor = None
    for klass in Voter.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_candidate_is_not_abstract():
    assert not inspect.isabstract(Candidate)


def test_candidate_constructor_exists():
    assert callable(Candidate.__init__)


def test_candidate_constructor_args():
    sig = inspect.signature(Candidate.__init__)
    params = list(sig.parameters.keys())
    assert "Candidate_Name" in params, "Missing parameter 'Candidate_Name'"
    assert "candidate_ID" in params, "Missing parameter 'candidate_ID'"
    assert "Candidate_PostID" in params, "Missing parameter 'Candidate_PostID'"
    assert "CandidatePartyName" in params, "Missing parameter 'CandidatePartyName'"

def test_candidate_has_Candidate_Name():
    assert hasattr(Candidate, "Candidate_Name")
    descriptor = None
    for klass in Candidate.__mro__:
        if "Candidate_Name" in klass.__dict__:
            descriptor = klass.__dict__["Candidate_Name"]
            break
    assert isinstance(descriptor, property)

def test_candidate_has_candidate_ID():
    assert hasattr(Candidate, "candidate_ID")
    descriptor = None
    for klass in Candidate.__mro__:
        if "candidate_ID" in klass.__dict__:
            descriptor = klass.__dict__["candidate_ID"]
            break
    assert isinstance(descriptor, property)

def test_candidate_has_Candidate_PostID():
    assert hasattr(Candidate, "Candidate_PostID")
    descriptor = None
    for klass in Candidate.__mro__:
        if "Candidate_PostID" in klass.__dict__:
            descriptor = klass.__dict__["Candidate_PostID"]
            break
    assert isinstance(descriptor, property)

def test_candidate_has_CandidatePartyName():
    assert hasattr(Candidate, "CandidatePartyName")
    descriptor = None
    for klass in Candidate.__mro__:
        if "CandidatePartyName" in klass.__dict__:
            descriptor = klass.__dict__["CandidatePartyName"]
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
Admin_strategy = st.builds(
    Admin,
    AdminID=
        st.integers(),
    AminName=
        safe_text,
    UserLogin=
        st.integers()
)
Election_strategy = st.builds(
    Election,
    ElectionDate=
        safe_text,
    ElectionCriteria=
        safe_text,
    ElectionName=
        safe_text,
    ElectionID=
        st.integers()
)
Post_strategy = st.builds(
    Post,
    PostDesc=
        safe_text,
    PostId=
        st.integers(),
    PostElectionId=
        st.integers()
)
BallotInformation_strategy = st.builds(
    BallotInformation,
    BallotPropID=
        st.integers(),
    BallotPropResults=
        st.integers(),
    BallotVotersID=
        st.integers(),
    BallotID=
        st.integers(),
    BallotElectionID=
        st.integers(),
    BallotPropBallotID=
        st.integers()
)
Voter_strategy = st.builds(
    Voter,
    student_faculty_ID=
        st.integers(),
    Address=
        safe_text,
    Eligibilty=
        st.booleans(),
    Age=
        st.integers(),
    Name=
        safe_text
)
Candidate_strategy = st.builds(
    Candidate,
    Candidate_Name=
        safe_text,
    candidate_ID=
        st.integers(),
    Candidate_PostID=
        st.integers(),
    CandidatePartyName=
        safe_text
)

@given(instance=Admin_strategy)
@settings(max_examples=50)
def test_admin_instantiation(instance):
    assert isinstance(instance, Admin)



@given(instance=Admin_strategy)
def test_admin_AdminID_setter(instance):
    original = instance.AdminID
    instance.AdminID = original
    assert instance.AdminID == original



@given(instance=Admin_strategy)
def test_admin_AminName_setter(instance):
    original = instance.AminName
    instance.AminName = original
    assert instance.AminName == original



@given(instance=Admin_strategy)
def test_admin_UserLogin_setter(instance):
    original = instance.UserLogin
    instance.UserLogin = original
    assert instance.UserLogin == original

@given(instance=Election_strategy)
@settings(max_examples=50)
def test_election_instantiation(instance):
    assert isinstance(instance, Election)



@given(instance=Election_strategy)
def test_election_ElectionDate_setter(instance):
    original = instance.ElectionDate
    instance.ElectionDate = original
    assert instance.ElectionDate == original



@given(instance=Election_strategy)
def test_election_ElectionCriteria_setter(instance):
    original = instance.ElectionCriteria
    instance.ElectionCriteria = original
    assert instance.ElectionCriteria == original



@given(instance=Election_strategy)
def test_election_ElectionName_setter(instance):
    original = instance.ElectionName
    instance.ElectionName = original
    assert instance.ElectionName == original



@given(instance=Election_strategy)
def test_election_ElectionID_setter(instance):
    original = instance.ElectionID
    instance.ElectionID = original
    assert instance.ElectionID == original

@given(instance=Post_strategy)
@settings(max_examples=50)
def test_post_instantiation(instance):
    assert isinstance(instance, Post)



@given(instance=Post_strategy)
def test_post_PostDesc_setter(instance):
    original = instance.PostDesc
    instance.PostDesc = original
    assert instance.PostDesc == original



@given(instance=Post_strategy)
def test_post_PostId_setter(instance):
    original = instance.PostId
    instance.PostId = original
    assert instance.PostId == original



@given(instance=Post_strategy)
def test_post_PostElectionId_setter(instance):
    original = instance.PostElectionId
    instance.PostElectionId = original
    assert instance.PostElectionId == original

@given(instance=BallotInformation_strategy)
@settings(max_examples=50)
def test_ballotinformation_instantiation(instance):
    assert isinstance(instance, BallotInformation)



@given(instance=BallotInformation_strategy)
def test_ballotinformation_BallotPropID_setter(instance):
    original = instance.BallotPropID
    instance.BallotPropID = original
    assert instance.BallotPropID == original



@given(instance=BallotInformation_strategy)
def test_ballotinformation_BallotPropResults_setter(instance):
    original = instance.BallotPropResults
    instance.BallotPropResults = original
    assert instance.BallotPropResults == original



@given(instance=BallotInformation_strategy)
def test_ballotinformation_BallotVotersID_setter(instance):
    original = instance.BallotVotersID
    instance.BallotVotersID = original
    assert instance.BallotVotersID == original



@given(instance=BallotInformation_strategy)
def test_ballotinformation_BallotID_setter(instance):
    original = instance.BallotID
    instance.BallotID = original
    assert instance.BallotID == original



@given(instance=BallotInformation_strategy)
def test_ballotinformation_BallotElectionID_setter(instance):
    original = instance.BallotElectionID
    instance.BallotElectionID = original
    assert instance.BallotElectionID == original



@given(instance=BallotInformation_strategy)
def test_ballotinformation_BallotPropBallotID_setter(instance):
    original = instance.BallotPropBallotID
    instance.BallotPropBallotID = original
    assert instance.BallotPropBallotID == original

@given(instance=Voter_strategy)
@settings(max_examples=50)
def test_voter_instantiation(instance):
    assert isinstance(instance, Voter)



@given(instance=Voter_strategy)
def test_voter_student_faculty_ID_setter(instance):
    original = instance.student_faculty_ID
    instance.student_faculty_ID = original
    assert instance.student_faculty_ID == original



@given(instance=Voter_strategy)
def test_voter_Address_setter(instance):
    original = instance.Address
    instance.Address = original
    assert instance.Address == original



@given(instance=Voter_strategy)
def test_voter_Eligibilty_setter(instance):
    original = instance.Eligibilty
    instance.Eligibilty = original
    assert instance.Eligibilty == original



@given(instance=Voter_strategy)
def test_voter_Age_setter(instance):
    original = instance.Age
    instance.Age = original
    assert instance.Age == original



@given(instance=Voter_strategy)
def test_voter_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=Candidate_strategy)
@settings(max_examples=50)
def test_candidate_instantiation(instance):
    assert isinstance(instance, Candidate)



@given(instance=Candidate_strategy)
def test_candidate_Candidate_Name_setter(instance):
    original = instance.Candidate_Name
    instance.Candidate_Name = original
    assert instance.Candidate_Name == original



@given(instance=Candidate_strategy)
def test_candidate_candidate_ID_setter(instance):
    original = instance.candidate_ID
    instance.candidate_ID = original
    assert instance.candidate_ID == original



@given(instance=Candidate_strategy)
def test_candidate_Candidate_PostID_setter(instance):
    original = instance.Candidate_PostID
    instance.Candidate_PostID = original
    assert instance.Candidate_PostID == original



@given(instance=Candidate_strategy)
def test_candidate_CandidatePartyName_setter(instance):
    original = instance.CandidatePartyName
    instance.CandidatePartyName = original
    assert instance.CandidatePartyName == original
