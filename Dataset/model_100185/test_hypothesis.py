import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Provides,
    sql::SqlProvides,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_provides_is_not_abstract():
    assert not inspect.isabstract(Provides)


def test_provides_constructor_exists():
    assert callable(Provides.__init__)


def test_provides_constructor_args():
    sig = inspect.signature(Provides.__init__)
    params = list(sig.parameters.keys())



def test_sql::sqlprovides_is_not_abstract():
    assert not inspect.isabstract(sql::SqlProvides)


def test_sql::sqlprovides_constructor_exists():
    assert callable(sql::SqlProvides.__init__)


def test_sql::sqlprovides_constructor_args():
    sig = inspect.signature(sql::SqlProvides.__init__)
    params = list(sig.parameters.keys())
    assert "minIdle" in params, "Missing parameter 'minIdle'"
    assert "timeBetweenEvictionRunsMillis" in params, "Missing parameter 'timeBetweenEvictionRunsMillis'"
    assert "maxIdle" in params, "Missing parameter 'maxIdle'"
    assert "storedProcedure" in params, "Missing parameter 'storedProcedure'"
    assert "url" in params, "Missing parameter 'url'"
    assert "metadata" in params, "Missing parameter 'metadata'"
    assert "user" in params, "Missing parameter 'user'"
    assert "driver" in params, "Missing parameter 'driver'"
    assert "maxWait" in params, "Missing parameter 'maxWait'"
    assert "password" in params, "Missing parameter 'password'"
    assert "maxActive" in params, "Missing parameter 'maxActive'"

def test_sql::sqlprovides_has_minIdle():
    assert hasattr(sql::SqlProvides, "minIdle")
    descriptor = None
    for klass in sql::SqlProvides.__mro__:
        if "minIdle" in klass.__dict__:
            descriptor = klass.__dict__["minIdle"]
            break
    assert isinstance(descriptor, property)

def test_sql::sqlprovides_has_timeBetweenEvictionRunsMillis():
    assert hasattr(sql::SqlProvides, "timeBetweenEvictionRunsMillis")
    descriptor = None
    for klass in sql::SqlProvides.__mro__:
        if "timeBetweenEvictionRunsMillis" in klass.__dict__:
            descriptor = klass.__dict__["timeBetweenEvictionRunsMillis"]
            break
    assert isinstance(descriptor, property)

def test_sql::sqlprovides_has_maxIdle():
    assert hasattr(sql::SqlProvides, "maxIdle")
    descriptor = None
    for klass in sql::SqlProvides.__mro__:
        if "maxIdle" in klass.__dict__:
            descriptor = klass.__dict__["maxIdle"]
            break
    assert isinstance(descriptor, property)

def test_sql::sqlprovides_has_storedProcedure():
    assert hasattr(sql::SqlProvides, "storedProcedure")
    descriptor = None
    for klass in sql::SqlProvides.__mro__:
        if "storedProcedure" in klass.__dict__:
            descriptor = klass.__dict__["storedProcedure"]
            break
    assert isinstance(descriptor, property)

def test_sql::sqlprovides_has_url():
    assert hasattr(sql::SqlProvides, "url")
    descriptor = None
    for klass in sql::SqlProvides.__mro__:
        if "url" in klass.__dict__:
            descriptor = klass.__dict__["url"]
            break
    assert isinstance(descriptor, property)

def test_sql::sqlprovides_has_metadata():
    assert hasattr(sql::SqlProvides, "metadata")
    descriptor = None
    for klass in sql::SqlProvides.__mro__:
        if "metadata" in klass.__dict__:
            descriptor = klass.__dict__["metadata"]
            break
    assert isinstance(descriptor, property)

def test_sql::sqlprovides_has_user():
    assert hasattr(sql::SqlProvides, "user")
    descriptor = None
    for klass in sql::SqlProvides.__mro__:
        if "user" in klass.__dict__:
            descriptor = klass.__dict__["user"]
            break
    assert isinstance(descriptor, property)

def test_sql::sqlprovides_has_driver():
    assert hasattr(sql::SqlProvides, "driver")
    descriptor = None
    for klass in sql::SqlProvides.__mro__:
        if "driver" in klass.__dict__:
            descriptor = klass.__dict__["driver"]
            break
    assert isinstance(descriptor, property)

def test_sql::sqlprovides_has_maxWait():
    assert hasattr(sql::SqlProvides, "maxWait")
    descriptor = None
    for klass in sql::SqlProvides.__mro__:
        if "maxWait" in klass.__dict__:
            descriptor = klass.__dict__["maxWait"]
            break
    assert isinstance(descriptor, property)

def test_sql::sqlprovides_has_password():
    assert hasattr(sql::SqlProvides, "password")
    descriptor = None
    for klass in sql::SqlProvides.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)

def test_sql::sqlprovides_has_maxActive():
    assert hasattr(sql::SqlProvides, "maxActive")
    descriptor = None
    for klass in sql::SqlProvides.__mro__:
        if "maxActive" in klass.__dict__:
            descriptor = klass.__dict__["maxActive"]
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
Provides_strategy = st.builds(
    Provides,
)
sql::SqlProvides_strategy = st.builds(
    sql::SqlProvides,
    minIdle=
        safe_text,
    timeBetweenEvictionRunsMillis=
        safe_text,
    maxIdle=
        safe_text,
    storedProcedure=
        safe_text,
    url=
        safe_text,
    metadata=
        safe_text,
    user=
        safe_text,
    driver=
        safe_text,
    maxWait=
        safe_text,
    password=
        safe_text,
    maxActive=
        safe_text
)

@given(instance=Provides_strategy)
@settings(max_examples=50)
def test_provides_instantiation(instance):
    assert isinstance(instance, Provides)

@given(instance=sql::SqlProvides_strategy)
@settings(max_examples=50)
def test_sql::sqlprovides_instantiation(instance):
    assert isinstance(instance, sql::SqlProvides)

@given(instance=sql::SqlProvides_strategy)
def test_sql::sqlprovides_minIdle_type(instance):
    assert isinstance(instance.minIdle, str)


@given(instance=sql::SqlProvides_strategy)
def test_sql::sqlprovides_minIdle_setter(instance):
    original = instance.minIdle
    instance.minIdle = original
    assert instance.minIdle == original

@given(instance=sql::SqlProvides_strategy)
def test_sql::sqlprovides_timeBetweenEvictionRunsMillis_type(instance):
    assert isinstance(instance.timeBetweenEvictionRunsMillis, str)


@given(instance=sql::SqlProvides_strategy)
def test_sql::sqlprovides_timeBetweenEvictionRunsMillis_setter(instance):
    original = instance.timeBetweenEvictionRunsMillis
    instance.timeBetweenEvictionRunsMillis = original
    assert instance.timeBetweenEvictionRunsMillis == original

@given(instance=sql::SqlProvides_strategy)
def test_sql::sqlprovides_maxIdle_type(instance):
    assert isinstance(instance.maxIdle, str)


@given(instance=sql::SqlProvides_strategy)
def test_sql::sqlprovides_maxIdle_setter(instance):
    original = instance.maxIdle
    instance.maxIdle = original
    assert instance.maxIdle == original

@given(instance=sql::SqlProvides_strategy)
def test_sql::sqlprovides_storedProcedure_type(instance):
    assert isinstance(instance.storedProcedure, str)


@given(instance=sql::SqlProvides_strategy)
def test_sql::sqlprovides_storedProcedure_setter(instance):
    original = instance.storedProcedure
    instance.storedProcedure = original
    assert instance.storedProcedure == original

@given(instance=sql::SqlProvides_strategy)
def test_sql::sqlprovides_url_type(instance):
    assert isinstance(instance.url, str)


@given(instance=sql::SqlProvides_strategy)
def test_sql::sqlprovides_url_setter(instance):
    original = instance.url
    instance.url = original
    assert instance.url == original

@given(instance=sql::SqlProvides_strategy)
def test_sql::sqlprovides_metadata_type(instance):
    assert isinstance(instance.metadata, str)


@given(instance=sql::SqlProvides_strategy)
def test_sql::sqlprovides_metadata_setter(instance):
    original = instance.metadata
    instance.metadata = original
    assert instance.metadata == original

@given(instance=sql::SqlProvides_strategy)
def test_sql::sqlprovides_user_type(instance):
    assert isinstance(instance.user, str)


@given(instance=sql::SqlProvides_strategy)
def test_sql::sqlprovides_user_setter(instance):
    original = instance.user
    instance.user = original
    assert instance.user == original

@given(instance=sql::SqlProvides_strategy)
def test_sql::sqlprovides_driver_type(instance):
    assert isinstance(instance.driver, str)


@given(instance=sql::SqlProvides_strategy)
def test_sql::sqlprovides_driver_setter(instance):
    original = instance.driver
    instance.driver = original
    assert instance.driver == original

@given(instance=sql::SqlProvides_strategy)
def test_sql::sqlprovides_maxWait_type(instance):
    assert isinstance(instance.maxWait, str)


@given(instance=sql::SqlProvides_strategy)
def test_sql::sqlprovides_maxWait_setter(instance):
    original = instance.maxWait
    instance.maxWait = original
    assert instance.maxWait == original

@given(instance=sql::SqlProvides_strategy)
def test_sql::sqlprovides_password_type(instance):
    assert isinstance(instance.password, str)


@given(instance=sql::SqlProvides_strategy)
def test_sql::sqlprovides_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original

@given(instance=sql::SqlProvides_strategy)
def test_sql::sqlprovides_maxActive_type(instance):
    assert isinstance(instance.maxActive, str)


@given(instance=sql::SqlProvides_strategy)
def test_sql::sqlprovides_maxActive_setter(instance):
    original = instance.maxActive
    instance.maxActive = original
    assert instance.maxActive == original
