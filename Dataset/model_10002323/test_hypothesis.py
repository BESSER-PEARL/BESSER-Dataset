import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    UserService,
    CredentialsProvider,
    CredentialsAuthController,
    ApplicationController,
    Actor_Actor,
    PrescriberController,
    Environment_User__CookieAuthenticator_,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_userservice_is_not_abstract():
    assert not inspect.isabstract(UserService)


def test_userservice_constructor_exists():
    assert callable(UserService.__init__)


def test_userservice_constructor_args():
    sig = inspect.signature(UserService.__init__)
    params = list(sig.parameters.keys())



def test_credentialsprovider_is_not_abstract():
    assert not inspect.isabstract(CredentialsProvider)


def test_credentialsprovider_constructor_exists():
    assert callable(CredentialsProvider.__init__)


def test_credentialsprovider_constructor_args():
    sig = inspect.signature(CredentialsProvider.__init__)
    params = list(sig.parameters.keys())



def test_credentialsauthcontroller_is_not_abstract():
    assert not inspect.isabstract(CredentialsAuthController)


def test_credentialsauthcontroller_constructor_exists():
    assert callable(CredentialsAuthController.__init__)


def test_credentialsauthcontroller_constructor_args():
    sig = inspect.signature(CredentialsAuthController.__init__)
    params = list(sig.parameters.keys())



def test_applicationcontroller_is_not_abstract():
    assert not inspect.isabstract(ApplicationController)


def test_applicationcontroller_constructor_exists():
    assert callable(ApplicationController.__init__)


def test_applicationcontroller_constructor_args():
    sig = inspect.signature(ApplicationController.__init__)
    params = list(sig.parameters.keys())



def test_actor_actor_is_not_abstract():
    assert not inspect.isabstract(Actor_Actor)


def test_actor_actor_constructor_exists():
    assert callable(Actor_Actor.__init__)


def test_actor_actor_constructor_args():
    sig = inspect.signature(Actor_Actor.__init__)
    params = list(sig.parameters.keys())



def test_prescribercontroller_is_not_abstract():
    assert not inspect.isabstract(PrescriberController)


def test_prescribercontroller_constructor_exists():
    assert callable(PrescriberController.__init__)


def test_prescribercontroller_constructor_args():
    sig = inspect.signature(PrescriberController.__init__)
    params = list(sig.parameters.keys())



def test_environment_user__cookieauthenticator__is_not_abstract():
    assert not inspect.isabstract(Environment_User__CookieAuthenticator_)


def test_environment_user__cookieauthenticator__constructor_exists():
    assert callable(Environment_User__CookieAuthenticator_.__init__)


def test_environment_user__cookieauthenticator__constructor_args():
    sig = inspect.signature(Environment_User__CookieAuthenticator_.__init__)
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
UserService_strategy = st.builds(
    UserService,
)
CredentialsProvider_strategy = st.builds(
    CredentialsProvider,
)
CredentialsAuthController_strategy = st.builds(
    CredentialsAuthController,
)
ApplicationController_strategy = st.builds(
    ApplicationController,
)
Actor_Actor_strategy = st.builds(
    Actor_Actor,
)
PrescriberController_strategy = st.builds(
    PrescriberController,
)
Environment_User__CookieAuthenticator__strategy = st.builds(
    Environment_User__CookieAuthenticator_,
)

@given(instance=UserService_strategy)
@settings(max_examples=50)
def test_userservice_instantiation(instance):
    assert isinstance(instance, UserService)

@given(instance=CredentialsProvider_strategy)
@settings(max_examples=50)
def test_credentialsprovider_instantiation(instance):
    assert isinstance(instance, CredentialsProvider)

@given(instance=CredentialsAuthController_strategy)
@settings(max_examples=50)
def test_credentialsauthcontroller_instantiation(instance):
    assert isinstance(instance, CredentialsAuthController)

@given(instance=ApplicationController_strategy)
@settings(max_examples=50)
def test_applicationcontroller_instantiation(instance):
    assert isinstance(instance, ApplicationController)

@given(instance=Actor_Actor_strategy)
@settings(max_examples=50)
def test_actor_actor_instantiation(instance):
    assert isinstance(instance, Actor_Actor)

@given(instance=PrescriberController_strategy)
@settings(max_examples=50)
def test_prescribercontroller_instantiation(instance):
    assert isinstance(instance, PrescriberController)

@given(instance=Environment_User__CookieAuthenticator__strategy)
@settings(max_examples=50)
def test_environment_user__cookieauthenticator__instantiation(instance):
    assert isinstance(instance, Environment_User__CookieAuthenticator_)
