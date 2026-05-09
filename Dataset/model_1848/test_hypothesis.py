import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    timetrack::TimeEntry,
    timetrack::Project,
    timetrack::Library,
    timetrack::User,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_timetrack::timeentry_is_not_abstract():
    assert not inspect.isabstract(timetrack::TimeEntry)


def test_timetrack::timeentry_constructor_exists():
    assert callable(timetrack::TimeEntry.__init__)


def test_timetrack::timeentry_constructor_args():
    sig = inspect.signature(timetrack::TimeEntry.__init__)
    params = list(sig.parameters.keys())
    assert "till" in params, "Missing parameter 'till'"
    assert "sync_date" in params, "Missing parameter 'sync_date'"
    assert "from_" in params, "Missing parameter 'from_'"
    assert "notes" in params, "Missing parameter 'notes'"
    assert "duration" in params, "Missing parameter 'duration'"
    assert "day" in params, "Missing parameter 'day'"
    assert "factured" in params, "Missing parameter 'factured'"

def test_timetrack::timeentry_has_till():
    assert hasattr(timetrack::TimeEntry, "till")
    descriptor = None
    for klass in timetrack::TimeEntry.__mro__:
        if "till" in klass.__dict__:
            descriptor = klass.__dict__["till"]
            break
    assert isinstance(descriptor, property)

def test_timetrack::timeentry_has_sync_date():
    assert hasattr(timetrack::TimeEntry, "sync_date")
    descriptor = None
    for klass in timetrack::TimeEntry.__mro__:
        if "sync_date" in klass.__dict__:
            descriptor = klass.__dict__["sync_date"]
            break
    assert isinstance(descriptor, property)

def test_timetrack::timeentry_has_from_():
    assert hasattr(timetrack::TimeEntry, "from_")
    descriptor = None
    for klass in timetrack::TimeEntry.__mro__:
        if "from_" in klass.__dict__:
            descriptor = klass.__dict__["from_"]
            break
    assert isinstance(descriptor, property)

def test_timetrack::timeentry_has_notes():
    assert hasattr(timetrack::TimeEntry, "notes")
    descriptor = None
    for klass in timetrack::TimeEntry.__mro__:
        if "notes" in klass.__dict__:
            descriptor = klass.__dict__["notes"]
            break
    assert isinstance(descriptor, property)

def test_timetrack::timeentry_has_duration():
    assert hasattr(timetrack::TimeEntry, "duration")
    descriptor = None
    for klass in timetrack::TimeEntry.__mro__:
        if "duration" in klass.__dict__:
            descriptor = klass.__dict__["duration"]
            break
    assert isinstance(descriptor, property)

def test_timetrack::timeentry_has_day():
    assert hasattr(timetrack::TimeEntry, "day")
    descriptor = None
    for klass in timetrack::TimeEntry.__mro__:
        if "day" in klass.__dict__:
            descriptor = klass.__dict__["day"]
            break
    assert isinstance(descriptor, property)

def test_timetrack::timeentry_has_factured():
    assert hasattr(timetrack::TimeEntry, "factured")
    descriptor = None
    for klass in timetrack::TimeEntry.__mro__:
        if "factured" in klass.__dict__:
            descriptor = klass.__dict__["factured"]
            break
    assert isinstance(descriptor, property)



def test_timetrack::project_is_not_abstract():
    assert not inspect.isabstract(timetrack::Project)


def test_timetrack::project_constructor_exists():
    assert callable(timetrack::Project.__init__)


def test_timetrack::project_constructor_args():
    sig = inspect.signature(timetrack::Project.__init__)
    params = list(sig.parameters.keys())
    assert "number" in params, "Missing parameter 'number'"
    assert "name" in params, "Missing parameter 'name'"

def test_timetrack::project_has_number():
    assert hasattr(timetrack::Project, "number")
    descriptor = None
    for klass in timetrack::Project.__mro__:
        if "number" in klass.__dict__:
            descriptor = klass.__dict__["number"]
            break
    assert isinstance(descriptor, property)

def test_timetrack::project_has_name():
    assert hasattr(timetrack::Project, "name")
    descriptor = None
    for klass in timetrack::Project.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_timetrack::library_is_not_abstract():
    assert not inspect.isabstract(timetrack::Library)


def test_timetrack::library_constructor_exists():
    assert callable(timetrack::Library.__init__)


def test_timetrack::library_constructor_args():
    sig = inspect.signature(timetrack::Library.__init__)
    params = list(sig.parameters.keys())



def test_timetrack::user_is_not_abstract():
    assert not inspect.isabstract(timetrack::User)


def test_timetrack::user_constructor_exists():
    assert callable(timetrack::User.__init__)


def test_timetrack::user_constructor_args():
    sig = inspect.signature(timetrack::User.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "password" in params, "Missing parameter 'password'"
    assert "sap_password" in params, "Missing parameter 'sap_password'"
    assert "sap_name" in params, "Missing parameter 'sap_name'"

def test_timetrack::user_has_name():
    assert hasattr(timetrack::User, "name")
    descriptor = None
    for klass in timetrack::User.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_timetrack::user_has_password():
    assert hasattr(timetrack::User, "password")
    descriptor = None
    for klass in timetrack::User.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)

def test_timetrack::user_has_sap_password():
    assert hasattr(timetrack::User, "sap_password")
    descriptor = None
    for klass in timetrack::User.__mro__:
        if "sap_password" in klass.__dict__:
            descriptor = klass.__dict__["sap_password"]
            break
    assert isinstance(descriptor, property)

def test_timetrack::user_has_sap_name():
    assert hasattr(timetrack::User, "sap_name")
    descriptor = None
    for klass in timetrack::User.__mro__:
        if "sap_name" in klass.__dict__:
            descriptor = klass.__dict__["sap_name"]
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
timetrack::TimeEntry_strategy = st.builds(
    timetrack::TimeEntry,
    till=
        st.dates(),
    sync_date=
        st.dates(),
    from_=
        st.dates(),
    notes=
        safe_text,
    duration=
        st.dates(),
    day=
        st.dates(),
    factured=
        st.booleans()
)
timetrack::Project_strategy = st.builds(
    timetrack::Project,
    number=
        safe_text,
    name=
        safe_text
)
timetrack::Library_strategy = st.builds(
    timetrack::Library,
)
timetrack::User_strategy = st.builds(
    timetrack::User,
    name=
        safe_text,
    password=
        safe_text,
    sap_password=
        safe_text,
    sap_name=
        safe_text
)

@given(instance=timetrack::TimeEntry_strategy)
@settings(max_examples=50)
def test_timetrack::timeentry_instantiation(instance):
    assert isinstance(instance, timetrack::TimeEntry)

@given(instance=timetrack::TimeEntry_strategy)
def test_timetrack::timeentry_till_type(instance):
    assert isinstance(instance.till, date)


@given(instance=timetrack::TimeEntry_strategy)
def test_timetrack::timeentry_till_setter(instance):
    original = instance.till
    instance.till = original
    assert instance.till == original

@given(instance=timetrack::TimeEntry_strategy)
def test_timetrack::timeentry_sync_date_type(instance):
    assert isinstance(instance.sync_date, date)


@given(instance=timetrack::TimeEntry_strategy)
def test_timetrack::timeentry_sync_date_setter(instance):
    original = instance.sync_date
    instance.sync_date = original
    assert instance.sync_date == original

@given(instance=timetrack::TimeEntry_strategy)
def test_timetrack::timeentry_from__type(instance):
    assert isinstance(instance.from_, date)


@given(instance=timetrack::TimeEntry_strategy)
def test_timetrack::timeentry_from__setter(instance):
    original = instance.from_
    instance.from_ = original
    assert instance.from_ == original

@given(instance=timetrack::TimeEntry_strategy)
def test_timetrack::timeentry_notes_type(instance):
    assert isinstance(instance.notes, str)


@given(instance=timetrack::TimeEntry_strategy)
def test_timetrack::timeentry_notes_setter(instance):
    original = instance.notes
    instance.notes = original
    assert instance.notes == original

@given(instance=timetrack::TimeEntry_strategy)
def test_timetrack::timeentry_duration_type(instance):
    assert isinstance(instance.duration, date)


@given(instance=timetrack::TimeEntry_strategy)
def test_timetrack::timeentry_duration_setter(instance):
    original = instance.duration
    instance.duration = original
    assert instance.duration == original

@given(instance=timetrack::TimeEntry_strategy)
def test_timetrack::timeentry_day_type(instance):
    assert isinstance(instance.day, date)


@given(instance=timetrack::TimeEntry_strategy)
def test_timetrack::timeentry_day_setter(instance):
    original = instance.day
    instance.day = original
    assert instance.day == original

@given(instance=timetrack::TimeEntry_strategy)
def test_timetrack::timeentry_factured_type(instance):
    assert isinstance(instance.factured, bool)


@given(instance=timetrack::TimeEntry_strategy)
def test_timetrack::timeentry_factured_setter(instance):
    original = instance.factured
    instance.factured = original
    assert instance.factured == original

@given(instance=timetrack::Project_strategy)
@settings(max_examples=50)
def test_timetrack::project_instantiation(instance):
    assert isinstance(instance, timetrack::Project)

@given(instance=timetrack::Project_strategy)
def test_timetrack::project_number_type(instance):
    assert isinstance(instance.number, str)


@given(instance=timetrack::Project_strategy)
def test_timetrack::project_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original

@given(instance=timetrack::Project_strategy)
def test_timetrack::project_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=timetrack::Project_strategy)
def test_timetrack::project_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=timetrack::Library_strategy)
@settings(max_examples=50)
def test_timetrack::library_instantiation(instance):
    assert isinstance(instance, timetrack::Library)

@given(instance=timetrack::User_strategy)
@settings(max_examples=50)
def test_timetrack::user_instantiation(instance):
    assert isinstance(instance, timetrack::User)

@given(instance=timetrack::User_strategy)
def test_timetrack::user_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=timetrack::User_strategy)
def test_timetrack::user_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=timetrack::User_strategy)
def test_timetrack::user_password_type(instance):
    assert isinstance(instance.password, str)


@given(instance=timetrack::User_strategy)
def test_timetrack::user_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original

@given(instance=timetrack::User_strategy)
def test_timetrack::user_sap_password_type(instance):
    assert isinstance(instance.sap_password, str)


@given(instance=timetrack::User_strategy)
def test_timetrack::user_sap_password_setter(instance):
    original = instance.sap_password
    instance.sap_password = original
    assert instance.sap_password == original

@given(instance=timetrack::User_strategy)
def test_timetrack::user_sap_name_type(instance):
    assert isinstance(instance.sap_name, str)


@given(instance=timetrack::User_strategy)
def test_timetrack::user_sap_name_setter(instance):
    original = instance.sap_name
    instance.sap_name = original
    assert instance.sap_name == original
