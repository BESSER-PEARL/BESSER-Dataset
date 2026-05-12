import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    grudi_TeamLine,
    grudi_Team,
    grudi_PersonInfo,
    grudi_Person,
    Gender,
    TeamPersonKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_grudi_teamline_is_not_abstract():
    assert not inspect.isabstract(grudi_TeamLine)


def test_grudi_teamline_constructor_exists():
    assert callable(grudi_TeamLine.__init__)


def test_grudi_teamline_constructor_args():
    sig = inspect.signature(grudi_TeamLine.__init__)
    params = list(sig.parameters.keys())
    assert "versionNumber" in params, "Missing parameter 'versionNumber'"
    assert "kind" in params, "Missing parameter 'kind'"
    assert "id" in params, "Missing parameter 'id'"

def test_grudi_teamline_has_versionNumber():
    assert hasattr(grudi_TeamLine, "versionNumber")
    descriptor = None
    for klass in grudi_TeamLine.__mro__:
        if "versionNumber" in klass.__dict__:
            descriptor = klass.__dict__["versionNumber"]
            break
    assert isinstance(descriptor, property)

def test_grudi_teamline_has_kind():
    assert hasattr(grudi_TeamLine, "kind")
    descriptor = None
    for klass in grudi_TeamLine.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)

def test_grudi_teamline_has_id():
    assert hasattr(grudi_TeamLine, "id")
    descriptor = None
    for klass in grudi_TeamLine.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_grudi_team_is_not_abstract():
    assert not inspect.isabstract(grudi_Team)


def test_grudi_team_constructor_exists():
    assert callable(grudi_Team.__init__)


def test_grudi_team_constructor_args():
    sig = inspect.signature(grudi_Team.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "versionNumber" in params, "Missing parameter 'versionNumber'"
    assert "id" in params, "Missing parameter 'id'"

def test_grudi_team_has_name():
    assert hasattr(grudi_Team, "name")
    descriptor = None
    for klass in grudi_Team.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_grudi_team_has_versionNumber():
    assert hasattr(grudi_Team, "versionNumber")
    descriptor = None
    for klass in grudi_Team.__mro__:
        if "versionNumber" in klass.__dict__:
            descriptor = klass.__dict__["versionNumber"]
            break
    assert isinstance(descriptor, property)

def test_grudi_team_has_id():
    assert hasattr(grudi_Team, "id")
    descriptor = None
    for klass in grudi_Team.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_grudi_personinfo_is_not_abstract():
    assert not inspect.isabstract(grudi_PersonInfo)


def test_grudi_personinfo_constructor_exists():
    assert callable(grudi_PersonInfo.__init__)


def test_grudi_personinfo_constructor_args():
    sig = inspect.signature(grudi_PersonInfo.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "userName" in params, "Missing parameter 'userName'"
    assert "name" in params, "Missing parameter 'name'"
    assert "phoneNumber" in params, "Missing parameter 'phoneNumber'"
    assert "gender" in params, "Missing parameter 'gender'"

def test_grudi_personinfo_has_id():
    assert hasattr(grudi_PersonInfo, "id")
    descriptor = None
    for klass in grudi_PersonInfo.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_grudi_personinfo_has_userName():
    assert hasattr(grudi_PersonInfo, "userName")
    descriptor = None
    for klass in grudi_PersonInfo.__mro__:
        if "userName" in klass.__dict__:
            descriptor = klass.__dict__["userName"]
            break
    assert isinstance(descriptor, property)

def test_grudi_personinfo_has_name():
    assert hasattr(grudi_PersonInfo, "name")
    descriptor = None
    for klass in grudi_PersonInfo.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_grudi_personinfo_has_phoneNumber():
    assert hasattr(grudi_PersonInfo, "phoneNumber")
    descriptor = None
    for klass in grudi_PersonInfo.__mro__:
        if "phoneNumber" in klass.__dict__:
            descriptor = klass.__dict__["phoneNumber"]
            break
    assert isinstance(descriptor, property)

def test_grudi_personinfo_has_gender():
    assert hasattr(grudi_PersonInfo, "gender")
    descriptor = None
    for klass in grudi_PersonInfo.__mro__:
        if "gender" in klass.__dict__:
            descriptor = klass.__dict__["gender"]
            break
    assert isinstance(descriptor, property)



def test_grudi_person_is_not_abstract():
    assert not inspect.isabstract(grudi_Person)


def test_grudi_person_constructor_exists():
    assert callable(grudi_Person.__init__)


def test_grudi_person_constructor_args():
    sig = inspect.signature(grudi_Person.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "username" in params, "Missing parameter 'username'"
    assert "versionNumber" in params, "Missing parameter 'versionNumber'"
    assert "password" in params, "Missing parameter 'password'"
    assert "gender" in params, "Missing parameter 'gender'"
    assert "email" in params, "Missing parameter 'email'"
    assert "name" in params, "Missing parameter 'name'"
    assert "phoneNumber" in params, "Missing parameter 'phoneNumber'"
    assert "address" in params, "Missing parameter 'address'"

def test_grudi_person_has_id():
    assert hasattr(grudi_Person, "id")
    descriptor = None
    for klass in grudi_Person.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_grudi_person_has_username():
    assert hasattr(grudi_Person, "username")
    descriptor = None
    for klass in grudi_Person.__mro__:
        if "username" in klass.__dict__:
            descriptor = klass.__dict__["username"]
            break
    assert isinstance(descriptor, property)

def test_grudi_person_has_versionNumber():
    assert hasattr(grudi_Person, "versionNumber")
    descriptor = None
    for klass in grudi_Person.__mro__:
        if "versionNumber" in klass.__dict__:
            descriptor = klass.__dict__["versionNumber"]
            break
    assert isinstance(descriptor, property)

def test_grudi_person_has_password():
    assert hasattr(grudi_Person, "password")
    descriptor = None
    for klass in grudi_Person.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)

def test_grudi_person_has_gender():
    assert hasattr(grudi_Person, "gender")
    descriptor = None
    for klass in grudi_Person.__mro__:
        if "gender" in klass.__dict__:
            descriptor = klass.__dict__["gender"]
            break
    assert isinstance(descriptor, property)

def test_grudi_person_has_email():
    assert hasattr(grudi_Person, "email")
    descriptor = None
    for klass in grudi_Person.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)

def test_grudi_person_has_name():
    assert hasattr(grudi_Person, "name")
    descriptor = None
    for klass in grudi_Person.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_grudi_person_has_phoneNumber():
    assert hasattr(grudi_Person, "phoneNumber")
    descriptor = None
    for klass in grudi_Person.__mro__:
        if "phoneNumber" in klass.__dict__:
            descriptor = klass.__dict__["phoneNumber"]
            break
    assert isinstance(descriptor, property)

def test_grudi_person_has_address():
    assert hasattr(grudi_Person, "address")
    descriptor = None
    for klass in grudi_Person.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)

def test_gender_exists():
    # Check that the Enumeration exists
    assert Gender is not None

def test_gender_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Gender]
    expected_literals = [
        "unknown",
        "male",
        "female",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Gender"

def test_teampersonkind_exists():
    # Check that the Enumeration exists
    assert TeamPersonKind is not None

def test_teampersonkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TeamPersonKind]
    expected_literals = [
        "captain",
        "member",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TeamPersonKind"


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
grudi_TeamLine_strategy = st.builds(
    grudi_TeamLine,
    versionNumber=
        safe_text,
    kind=
        safe_text,
    id=
        safe_text
)
grudi_Team_strategy = st.builds(
    grudi_Team,
    name=
        safe_text,
    versionNumber=
        safe_text,
    id=
        safe_text
)
grudi_PersonInfo_strategy = st.builds(
    grudi_PersonInfo,
    id=
        safe_text,
    userName=
        safe_text,
    name=
        safe_text,
    phoneNumber=
        safe_text,
    gender=
        safe_text
)
grudi_Person_strategy = st.builds(
    grudi_Person,
    id=
        safe_text,
    username=
        safe_text,
    versionNumber=
        safe_text,
    password=
        safe_text,
    gender=
        safe_text,
    email=
        safe_text,
    name=
        safe_text,
    phoneNumber=
        safe_text,
    address=
        safe_text
)

@given(instance=grudi_TeamLine_strategy)
@settings(max_examples=50)
def test_grudi_teamline_instantiation(instance):
    assert isinstance(instance, grudi_TeamLine)



@given(instance=grudi_TeamLine_strategy)
def test_grudi_teamline_versionNumber_setter(instance):
    original = instance.versionNumber
    instance.versionNumber = original
    assert instance.versionNumber == original



@given(instance=grudi_TeamLine_strategy)
def test_grudi_teamline_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original



@given(instance=grudi_TeamLine_strategy)
def test_grudi_teamline_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=grudi_Team_strategy)
@settings(max_examples=50)
def test_grudi_team_instantiation(instance):
    assert isinstance(instance, grudi_Team)



@given(instance=grudi_Team_strategy)
def test_grudi_team_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=grudi_Team_strategy)
def test_grudi_team_versionNumber_setter(instance):
    original = instance.versionNumber
    instance.versionNumber = original
    assert instance.versionNumber == original



@given(instance=grudi_Team_strategy)
def test_grudi_team_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=grudi_PersonInfo_strategy)
@settings(max_examples=50)
def test_grudi_personinfo_instantiation(instance):
    assert isinstance(instance, grudi_PersonInfo)



@given(instance=grudi_PersonInfo_strategy)
def test_grudi_personinfo_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=grudi_PersonInfo_strategy)
def test_grudi_personinfo_userName_setter(instance):
    original = instance.userName
    instance.userName = original
    assert instance.userName == original



@given(instance=grudi_PersonInfo_strategy)
def test_grudi_personinfo_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=grudi_PersonInfo_strategy)
def test_grudi_personinfo_phoneNumber_setter(instance):
    original = instance.phoneNumber
    instance.phoneNumber = original
    assert instance.phoneNumber == original



@given(instance=grudi_PersonInfo_strategy)
def test_grudi_personinfo_gender_setter(instance):
    original = instance.gender
    instance.gender = original
    assert instance.gender == original

@given(instance=grudi_Person_strategy)
@settings(max_examples=50)
def test_grudi_person_instantiation(instance):
    assert isinstance(instance, grudi_Person)



@given(instance=grudi_Person_strategy)
def test_grudi_person_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=grudi_Person_strategy)
def test_grudi_person_username_setter(instance):
    original = instance.username
    instance.username = original
    assert instance.username == original



@given(instance=grudi_Person_strategy)
def test_grudi_person_versionNumber_setter(instance):
    original = instance.versionNumber
    instance.versionNumber = original
    assert instance.versionNumber == original



@given(instance=grudi_Person_strategy)
def test_grudi_person_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=grudi_Person_strategy)
def test_grudi_person_gender_setter(instance):
    original = instance.gender
    instance.gender = original
    assert instance.gender == original



@given(instance=grudi_Person_strategy)
def test_grudi_person_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=grudi_Person_strategy)
def test_grudi_person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=grudi_Person_strategy)
def test_grudi_person_phoneNumber_setter(instance):
    original = instance.phoneNumber
    instance.phoneNumber = original
    assert instance.phoneNumber == original



@given(instance=grudi_Person_strategy)
def test_grudi_person_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original
