import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Inbox,
    Hashtag,
    Comment,
    Page,
    Group,
    Post,
    Share,
    Message,
    User,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_inbox_is_not_abstract():
    assert not inspect.isabstract(Inbox)


def test_inbox_constructor_exists():
    assert callable(Inbox.__init__)


def test_inbox_constructor_args():
    sig = inspect.signature(Inbox.__init__)
    params = list(sig.parameters.keys())



def test_hashtag_is_not_abstract():
    assert not inspect.isabstract(Hashtag)


def test_hashtag_constructor_exists():
    assert callable(Hashtag.__init__)


def test_hashtag_constructor_args():
    sig = inspect.signature(Hashtag.__init__)
    params = list(sig.parameters.keys())



def test_comment_is_not_abstract():
    assert not inspect.isabstract(Comment)


def test_comment_constructor_exists():
    assert callable(Comment.__init__)


def test_comment_constructor_args():
    sig = inspect.signature(Comment.__init__)
    params = list(sig.parameters.keys())



def test_page_is_not_abstract():
    assert not inspect.isabstract(Page)


def test_page_constructor_exists():
    assert callable(Page.__init__)


def test_page_constructor_args():
    sig = inspect.signature(Page.__init__)
    params = list(sig.parameters.keys())



def test_group_is_not_abstract():
    assert not inspect.isabstract(Group)


def test_group_constructor_exists():
    assert callable(Group.__init__)


def test_group_constructor_args():
    sig = inspect.signature(Group.__init__)
    params = list(sig.parameters.keys())



def test_post_is_not_abstract():
    assert not inspect.isabstract(Post)


def test_post_constructor_exists():
    assert callable(Post.__init__)


def test_post_constructor_args():
    sig = inspect.signature(Post.__init__)
    params = list(sig.parameters.keys())



def test_share_is_not_abstract():
    assert not inspect.isabstract(Share)


def test_share_constructor_exists():
    assert callable(Share.__init__)


def test_share_constructor_args():
    sig = inspect.signature(Share.__init__)
    params = list(sig.parameters.keys())



def test_message_is_not_abstract():
    assert not inspect.isabstract(Message)


def test_message_constructor_exists():
    assert callable(Message.__init__)


def test_message_constructor_args():
    sig = inspect.signature(Message.__init__)
    params = list(sig.parameters.keys())



def test_user_is_not_abstract():
    assert not inspect.isabstract(User)


def test_user_constructor_exists():
    assert callable(User.__init__)


def test_user_constructor_args():
    sig = inspect.signature(User.__init__)
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
Inbox_strategy = st.builds(
    Inbox,
)
Hashtag_strategy = st.builds(
    Hashtag,
)
Comment_strategy = st.builds(
    Comment,
)
Page_strategy = st.builds(
    Page,
)
Group_strategy = st.builds(
    Group,
)
Post_strategy = st.builds(
    Post,
)
Share_strategy = st.builds(
    Share,
)
Message_strategy = st.builds(
    Message,
)
User_strategy = st.builds(
    User,
)

@given(instance=Inbox_strategy)
@settings(max_examples=50)
def test_inbox_instantiation(instance):
    assert isinstance(instance, Inbox)

@given(instance=Hashtag_strategy)
@settings(max_examples=50)
def test_hashtag_instantiation(instance):
    assert isinstance(instance, Hashtag)

@given(instance=Comment_strategy)
@settings(max_examples=50)
def test_comment_instantiation(instance):
    assert isinstance(instance, Comment)

@given(instance=Page_strategy)
@settings(max_examples=50)
def test_page_instantiation(instance):
    assert isinstance(instance, Page)

@given(instance=Group_strategy)
@settings(max_examples=50)
def test_group_instantiation(instance):
    assert isinstance(instance, Group)

@given(instance=Post_strategy)
@settings(max_examples=50)
def test_post_instantiation(instance):
    assert isinstance(instance, Post)

@given(instance=Share_strategy)
@settings(max_examples=50)
def test_share_instantiation(instance):
    assert isinstance(instance, Share)

@given(instance=Message_strategy)
@settings(max_examples=50)
def test_message_instantiation(instance):
    assert isinstance(instance, Message)

@given(instance=User_strategy)
@settings(max_examples=50)
def test_user_instantiation(instance):
    assert isinstance(instance, User)
