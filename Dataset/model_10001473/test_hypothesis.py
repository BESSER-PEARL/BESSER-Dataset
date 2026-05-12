import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Invitation,
    Tag,
    CommentTopic,
    Topic,
    Group,
    Message,
    Vote,
    Comment,
    Post,
    Rol,
    User,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_invitation_is_not_abstract():
    assert not inspect.isabstract(Invitation)


def test_invitation_constructor_exists():
    assert callable(Invitation.__init__)


def test_invitation_constructor_args():
    sig = inspect.signature(Invitation.__init__)
    params = list(sig.parameters.keys())



def test_tag_is_not_abstract():
    assert not inspect.isabstract(Tag)


def test_tag_constructor_exists():
    assert callable(Tag.__init__)


def test_tag_constructor_args():
    sig = inspect.signature(Tag.__init__)
    params = list(sig.parameters.keys())



def test_commenttopic_is_not_abstract():
    assert not inspect.isabstract(CommentTopic)


def test_commenttopic_constructor_exists():
    assert callable(CommentTopic.__init__)


def test_commenttopic_constructor_args():
    sig = inspect.signature(CommentTopic.__init__)
    params = list(sig.parameters.keys())



def test_topic_is_not_abstract():
    assert not inspect.isabstract(Topic)


def test_topic_constructor_exists():
    assert callable(Topic.__init__)


def test_topic_constructor_args():
    sig = inspect.signature(Topic.__init__)
    params = list(sig.parameters.keys())



def test_group_is_not_abstract():
    assert not inspect.isabstract(Group)


def test_group_constructor_exists():
    assert callable(Group.__init__)


def test_group_constructor_args():
    sig = inspect.signature(Group.__init__)
    params = list(sig.parameters.keys())



def test_message_is_not_abstract():
    assert not inspect.isabstract(Message)


def test_message_constructor_exists():
    assert callable(Message.__init__)


def test_message_constructor_args():
    sig = inspect.signature(Message.__init__)
    params = list(sig.parameters.keys())



def test_vote_is_not_abstract():
    assert not inspect.isabstract(Vote)


def test_vote_constructor_exists():
    assert callable(Vote.__init__)


def test_vote_constructor_args():
    sig = inspect.signature(Vote.__init__)
    params = list(sig.parameters.keys())
    assert "tipo" in params, "Missing parameter 'tipo'"

def test_vote_has_tipo():
    assert hasattr(Vote, "tipo")
    descriptor = None
    for klass in Vote.__mro__:
        if "tipo" in klass.__dict__:
            descriptor = klass.__dict__["tipo"]
            break
    assert isinstance(descriptor, property)



def test_comment_is_not_abstract():
    assert not inspect.isabstract(Comment)


def test_comment_constructor_exists():
    assert callable(Comment.__init__)


def test_comment_constructor_args():
    sig = inspect.signature(Comment.__init__)
    params = list(sig.parameters.keys())
    assert "date" in params, "Missing parameter 'date'"
    assert "userName" in params, "Missing parameter 'userName'"
    assert "comment" in params, "Missing parameter 'comment'"

def test_comment_has_date():
    assert hasattr(Comment, "date")
    descriptor = None
    for klass in Comment.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)

def test_comment_has_userName():
    assert hasattr(Comment, "userName")
    descriptor = None
    for klass in Comment.__mro__:
        if "userName" in klass.__dict__:
            descriptor = klass.__dict__["userName"]
            break
    assert isinstance(descriptor, property)

def test_comment_has_comment():
    assert hasattr(Comment, "comment")
    descriptor = None
    for klass in Comment.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_post_is_not_abstract():
    assert not inspect.isabstract(Post)


def test_post_constructor_exists():
    assert callable(Post.__init__)


def test_post_constructor_args():
    sig = inspect.signature(Post.__init__)
    params = list(sig.parameters.keys())
    assert "content" in params, "Missing parameter 'content'"
    assert "userName" in params, "Missing parameter 'userName'"
    assert "Date" in params, "Missing parameter 'Date'"

def test_post_has_content():
    assert hasattr(Post, "content")
    descriptor = None
    for klass in Post.__mro__:
        if "content" in klass.__dict__:
            descriptor = klass.__dict__["content"]
            break
    assert isinstance(descriptor, property)

def test_post_has_userName():
    assert hasattr(Post, "userName")
    descriptor = None
    for klass in Post.__mro__:
        if "userName" in klass.__dict__:
            descriptor = klass.__dict__["userName"]
            break
    assert isinstance(descriptor, property)

def test_post_has_Date():
    assert hasattr(Post, "Date")
    descriptor = None
    for klass in Post.__mro__:
        if "Date" in klass.__dict__:
            descriptor = klass.__dict__["Date"]
            break
    assert isinstance(descriptor, property)



def test_rol_is_not_abstract():
    assert not inspect.isabstract(Rol)


def test_rol_constructor_exists():
    assert callable(Rol.__init__)


def test_rol_constructor_args():
    sig = inspect.signature(Rol.__init__)
    params = list(sig.parameters.keys())
    assert "nombre" in params, "Missing parameter 'nombre'"

def test_rol_has_nombre():
    assert hasattr(Rol, "nombre")
    descriptor = None
    for klass in Rol.__mro__:
        if "nombre" in klass.__dict__:
            descriptor = klass.__dict__["nombre"]
            break
    assert isinstance(descriptor, property)



def test_user_is_not_abstract():
    assert not inspect.isabstract(User)


def test_user_constructor_exists():
    assert callable(User.__init__)


def test_user_constructor_args():
    sig = inspect.signature(User.__init__)
    params = list(sig.parameters.keys())
    assert "password" in params, "Missing parameter 'password'"
    assert "userName" in params, "Missing parameter 'userName'"
    assert "email" in params, "Missing parameter 'email'"

def test_user_has_password():
    assert hasattr(User, "password")
    descriptor = None
    for klass in User.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)

def test_user_has_userName():
    assert hasattr(User, "userName")
    descriptor = None
    for klass in User.__mro__:
        if "userName" in klass.__dict__:
            descriptor = klass.__dict__["userName"]
            break
    assert isinstance(descriptor, property)

def test_user_has_email():
    assert hasattr(User, "email")
    descriptor = None
    for klass in User.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
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
Invitation_strategy = st.builds(
    Invitation,
)
Tag_strategy = st.builds(
    Tag,
)
CommentTopic_strategy = st.builds(
    CommentTopic,
)
Topic_strategy = st.builds(
    Topic,
)
Group_strategy = st.builds(
    Group,
)
Message_strategy = st.builds(
    Message,
)
Vote_strategy = st.builds(
    Vote,
    tipo=
        st.booleans()
)
Comment_strategy = st.builds(
    Comment,
    date=
        safe_text,
    userName=
        safe_text,
    comment=
        safe_text
)
Post_strategy = st.builds(
    Post,
    content=
        safe_text,
    userName=
        safe_text,
    Date=
        safe_text
)
Rol_strategy = st.builds(
    Rol,
    nombre=
        safe_text
)
User_strategy = st.builds(
    User,
    password=
        safe_text,
    userName=
        safe_text,
    email=
        safe_text
)

@given(instance=Invitation_strategy)
@settings(max_examples=50)
def test_invitation_instantiation(instance):
    assert isinstance(instance, Invitation)

@given(instance=Tag_strategy)
@settings(max_examples=50)
def test_tag_instantiation(instance):
    assert isinstance(instance, Tag)

@given(instance=CommentTopic_strategy)
@settings(max_examples=50)
def test_commenttopic_instantiation(instance):
    assert isinstance(instance, CommentTopic)

@given(instance=Topic_strategy)
@settings(max_examples=50)
def test_topic_instantiation(instance):
    assert isinstance(instance, Topic)

@given(instance=Group_strategy)
@settings(max_examples=50)
def test_group_instantiation(instance):
    assert isinstance(instance, Group)

@given(instance=Message_strategy)
@settings(max_examples=50)
def test_message_instantiation(instance):
    assert isinstance(instance, Message)

@given(instance=Vote_strategy)
@settings(max_examples=50)
def test_vote_instantiation(instance):
    assert isinstance(instance, Vote)



@given(instance=Vote_strategy)
def test_vote_tipo_setter(instance):
    original = instance.tipo
    instance.tipo = original
    assert instance.tipo == original

@given(instance=Comment_strategy)
@settings(max_examples=50)
def test_comment_instantiation(instance):
    assert isinstance(instance, Comment)



@given(instance=Comment_strategy)
def test_comment_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original



@given(instance=Comment_strategy)
def test_comment_userName_setter(instance):
    original = instance.userName
    instance.userName = original
    assert instance.userName == original



@given(instance=Comment_strategy)
def test_comment_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=Post_strategy)
@settings(max_examples=50)
def test_post_instantiation(instance):
    assert isinstance(instance, Post)



@given(instance=Post_strategy)
def test_post_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original



@given(instance=Post_strategy)
def test_post_userName_setter(instance):
    original = instance.userName
    instance.userName = original
    assert instance.userName == original



@given(instance=Post_strategy)
def test_post_Date_setter(instance):
    original = instance.Date
    instance.Date = original
    assert instance.Date == original

@given(instance=Rol_strategy)
@settings(max_examples=50)
def test_rol_instantiation(instance):
    assert isinstance(instance, Rol)



@given(instance=Rol_strategy)
def test_rol_nombre_setter(instance):
    original = instance.nombre
    instance.nombre = original
    assert instance.nombre == original

@given(instance=User_strategy)
@settings(max_examples=50)
def test_user_instantiation(instance):
    assert isinstance(instance, User)



@given(instance=User_strategy)
def test_user_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=User_strategy)
def test_user_userName_setter(instance):
    original = instance.userName
    instance.userName = original
    assert instance.userName == original



@given(instance=User_strategy)
def test_user_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original
