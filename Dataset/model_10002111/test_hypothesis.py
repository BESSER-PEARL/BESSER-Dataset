import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    User2_Interface,
    HashTags,
    Page,
    Post,
    User__,
    Group,
    User,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_user2_interface_is_not_abstract():
    assert not inspect.isabstract(User2_Interface)


def test_user2_interface_constructor_exists():
    assert callable(User2_Interface.__init__)


def test_user2_interface_constructor_args():
    sig = inspect.signature(User2_Interface.__init__)
    params = list(sig.parameters.keys())



def test_hashtags_is_not_abstract():
    assert not inspect.isabstract(HashTags)


def test_hashtags_constructor_exists():
    assert callable(HashTags.__init__)


def test_hashtags_constructor_args():
    sig = inspect.signature(HashTags.__init__)
    params = list(sig.parameters.keys())
    assert "allHashTags" in params, "Missing parameter 'allHashTags'"

def test_hashtags_has_allHashTags():
    assert hasattr(HashTags, "allHashTags")
    descriptor = None
    for klass in HashTags.__mro__:
        if "allHashTags" in klass.__dict__:
            descriptor = klass.__dict__["allHashTags"]
            break
    assert isinstance(descriptor, property)



def test_page_is_not_abstract():
    assert not inspect.isabstract(Page)


def test_page_constructor_exists():
    assert callable(Page.__init__)


def test_page_constructor_args():
    sig = inspect.signature(Page.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "posts" in params, "Missing parameter 'posts'"
    assert "admin" in params, "Missing parameter 'admin'"
    assert "nFans" in params, "Missing parameter 'nFans'"
    assert "fans" in params, "Missing parameter 'fans'"
    assert "name" in params, "Missing parameter 'name'"

def test_page_has_description():
    assert hasattr(Page, "description")
    descriptor = None
    for klass in Page.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_page_has_posts():
    assert hasattr(Page, "posts")
    descriptor = None
    for klass in Page.__mro__:
        if "posts" in klass.__dict__:
            descriptor = klass.__dict__["posts"]
            break
    assert isinstance(descriptor, property)

def test_page_has_admin():
    assert hasattr(Page, "admin")
    descriptor = None
    for klass in Page.__mro__:
        if "admin" in klass.__dict__:
            descriptor = klass.__dict__["admin"]
            break
    assert isinstance(descriptor, property)

def test_page_has_nFans():
    assert hasattr(Page, "nFans")
    descriptor = None
    for klass in Page.__mro__:
        if "nFans" in klass.__dict__:
            descriptor = klass.__dict__["nFans"]
            break
    assert isinstance(descriptor, property)

def test_page_has_fans():
    assert hasattr(Page, "fans")
    descriptor = None
    for klass in Page.__mro__:
        if "fans" in klass.__dict__:
            descriptor = klass.__dict__["fans"]
            break
    assert isinstance(descriptor, property)

def test_page_has_name():
    assert hasattr(Page, "name")
    descriptor = None
    for klass in Page.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_post_is_not_abstract():
    assert not inspect.isabstract(Post)


def test_post_constructor_exists():
    assert callable(Post.__init__)


def test_post_constructor_args():
    sig = inspect.signature(Post.__init__)
    params = list(sig.parameters.keys())
    assert "nComments" in params, "Missing parameter 'nComments'"
    assert "nShares" in params, "Missing parameter 'nShares'"
    assert "owner" in params, "Missing parameter 'owner'"
    assert "nLikes" in params, "Missing parameter 'nLikes'"
    assert "privateMode" in params, "Missing parameter 'privateMode'"

def test_post_has_nComments():
    assert hasattr(Post, "nComments")
    descriptor = None
    for klass in Post.__mro__:
        if "nComments" in klass.__dict__:
            descriptor = klass.__dict__["nComments"]
            break
    assert isinstance(descriptor, property)

def test_post_has_nShares():
    assert hasattr(Post, "nShares")
    descriptor = None
    for klass in Post.__mro__:
        if "nShares" in klass.__dict__:
            descriptor = klass.__dict__["nShares"]
            break
    assert isinstance(descriptor, property)

def test_post_has_owner():
    assert hasattr(Post, "owner")
    descriptor = None
    for klass in Post.__mro__:
        if "owner" in klass.__dict__:
            descriptor = klass.__dict__["owner"]
            break
    assert isinstance(descriptor, property)

def test_post_has_nLikes():
    assert hasattr(Post, "nLikes")
    descriptor = None
    for klass in Post.__mro__:
        if "nLikes" in klass.__dict__:
            descriptor = klass.__dict__["nLikes"]
            break
    assert isinstance(descriptor, property)

def test_post_has_privateMode():
    assert hasattr(Post, "privateMode")
    descriptor = None
    for klass in Post.__mro__:
        if "privateMode" in klass.__dict__:
            descriptor = klass.__dict__["privateMode"]
            break
    assert isinstance(descriptor, property)



def test_user___is_not_abstract():
    assert not inspect.isabstract(User__)


def test_user___constructor_exists():
    assert callable(User__.__init__)


def test_user___constructor_args():
    sig = inspect.signature(User__.__init__)
    params = list(sig.parameters.keys())



def test_group_is_not_abstract():
    assert not inspect.isabstract(Group)


def test_group_constructor_exists():
    assert callable(Group.__init__)


def test_group_constructor_args():
    sig = inspect.signature(Group.__init__)
    params = list(sig.parameters.keys())
    assert "admins" in params, "Missing parameter 'admins'"
    assert "nMembers" in params, "Missing parameter 'nMembers'"
    assert "description" in params, "Missing parameter 'description'"
    assert "members" in params, "Missing parameter 'members'"
    assert "name" in params, "Missing parameter 'name'"
    assert "posts" in params, "Missing parameter 'posts'"

def test_group_has_admins():
    assert hasattr(Group, "admins")
    descriptor = None
    for klass in Group.__mro__:
        if "admins" in klass.__dict__:
            descriptor = klass.__dict__["admins"]
            break
    assert isinstance(descriptor, property)

def test_group_has_nMembers():
    assert hasattr(Group, "nMembers")
    descriptor = None
    for klass in Group.__mro__:
        if "nMembers" in klass.__dict__:
            descriptor = klass.__dict__["nMembers"]
            break
    assert isinstance(descriptor, property)

def test_group_has_description():
    assert hasattr(Group, "description")
    descriptor = None
    for klass in Group.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_group_has_members():
    assert hasattr(Group, "members")
    descriptor = None
    for klass in Group.__mro__:
        if "members" in klass.__dict__:
            descriptor = klass.__dict__["members"]
            break
    assert isinstance(descriptor, property)

def test_group_has_name():
    assert hasattr(Group, "name")
    descriptor = None
    for klass in Group.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_group_has_posts():
    assert hasattr(Group, "posts")
    descriptor = None
    for klass in Group.__mro__:
        if "posts" in klass.__dict__:
            descriptor = klass.__dict__["posts"]
            break
    assert isinstance(descriptor, property)



def test_user_is_not_abstract():
    assert not inspect.isabstract(User)


def test_user_constructor_exists():
    assert callable(User.__init__)


def test_user_constructor_args():
    sig = inspect.signature(User.__init__)
    params = list(sig.parameters.keys())
    assert "pages" in params, "Missing parameter 'pages'"
    assert "gender" in params, "Missing parameter 'gender'"
    assert "username" in params, "Missing parameter 'username'"
    assert "groups" in params, "Missing parameter 'groups'"
    assert "name" in params, "Missing parameter 'name'"
    assert "password" in params, "Missing parameter 'password'"
    assert "email" in params, "Missing parameter 'email'"

def test_user_has_pages():
    assert hasattr(User, "pages")
    descriptor = None
    for klass in User.__mro__:
        if "pages" in klass.__dict__:
            descriptor = klass.__dict__["pages"]
            break
    assert isinstance(descriptor, property)

def test_user_has_gender():
    assert hasattr(User, "gender")
    descriptor = None
    for klass in User.__mro__:
        if "gender" in klass.__dict__:
            descriptor = klass.__dict__["gender"]
            break
    assert isinstance(descriptor, property)

def test_user_has_username():
    assert hasattr(User, "username")
    descriptor = None
    for klass in User.__mro__:
        if "username" in klass.__dict__:
            descriptor = klass.__dict__["username"]
            break
    assert isinstance(descriptor, property)

def test_user_has_groups():
    assert hasattr(User, "groups")
    descriptor = None
    for klass in User.__mro__:
        if "groups" in klass.__dict__:
            descriptor = klass.__dict__["groups"]
            break
    assert isinstance(descriptor, property)

def test_user_has_name():
    assert hasattr(User, "name")
    descriptor = None
    for klass in User.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_user_has_password():
    assert hasattr(User, "password")
    descriptor = None
    for klass in User.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
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
User2_Interface_strategy = st.builds(
    User2_Interface,
)
HashTags_strategy = st.builds(
    HashTags,
    allHashTags=
        safe_text
)
Page_strategy = st.builds(
    Page,
    description=
        safe_text,
    posts=
        safe_text,
    admin=
        st.none(),
    nFans=
        st.integers(),
    fans=
        st.none(),
    name=
        safe_text
)
Post_strategy = st.builds(
    Post,
    nComments=
        st.integers(),
    nShares=
        st.integers(),
    owner=
        st.none(),
    nLikes=
        st.integers(),
    privateMode=
        st.booleans()
)
User___strategy = st.builds(
    User__,
)
Group_strategy = st.builds(
    Group,
    admins=
        st.none(),
    nMembers=
        st.integers(),
    description=
        safe_text,
    members=
        st.none(),
    name=
        safe_text,
    posts=
        safe_text
)
User_strategy = st.builds(
    User,
    pages=
        safe_text,
    gender=
        safe_text,
    username=
        safe_text,
    groups=
        safe_text,
    name=
        safe_text,
    password=
        safe_text,
    email=
        safe_text
)

@given(instance=User2_Interface_strategy)
@settings(max_examples=50)
def test_user2_interface_instantiation(instance):
    assert isinstance(instance, User2_Interface)

@given(instance=HashTags_strategy)
@settings(max_examples=50)
def test_hashtags_instantiation(instance):
    assert isinstance(instance, HashTags)



@given(instance=HashTags_strategy)
def test_hashtags_allHashTags_setter(instance):
    original = instance.allHashTags
    instance.allHashTags = original
    assert instance.allHashTags == original

@given(instance=Page_strategy)
@settings(max_examples=50)
def test_page_instantiation(instance):
    assert isinstance(instance, Page)



@given(instance=Page_strategy)
def test_page_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=Page_strategy)
def test_page_posts_setter(instance):
    original = instance.posts
    instance.posts = original
    assert instance.posts == original



@given(instance=Page_strategy)
def test_page_admin_setter(instance):
    original = instance.admin
    instance.admin = original
    assert instance.admin == original



@given(instance=Page_strategy)
def test_page_nFans_setter(instance):
    original = instance.nFans
    instance.nFans = original
    assert instance.nFans == original



@given(instance=Page_strategy)
def test_page_fans_setter(instance):
    original = instance.fans
    instance.fans = original
    assert instance.fans == original



@given(instance=Page_strategy)
def test_page_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Post_strategy)
@settings(max_examples=50)
def test_post_instantiation(instance):
    assert isinstance(instance, Post)



@given(instance=Post_strategy)
def test_post_nComments_setter(instance):
    original = instance.nComments
    instance.nComments = original
    assert instance.nComments == original



@given(instance=Post_strategy)
def test_post_nShares_setter(instance):
    original = instance.nShares
    instance.nShares = original
    assert instance.nShares == original



@given(instance=Post_strategy)
def test_post_owner_setter(instance):
    original = instance.owner
    instance.owner = original
    assert instance.owner == original



@given(instance=Post_strategy)
def test_post_nLikes_setter(instance):
    original = instance.nLikes
    instance.nLikes = original
    assert instance.nLikes == original



@given(instance=Post_strategy)
def test_post_privateMode_setter(instance):
    original = instance.privateMode
    instance.privateMode = original
    assert instance.privateMode == original

@given(instance=User___strategy)
@settings(max_examples=50)
def test_user___instantiation(instance):
    assert isinstance(instance, User__)

@given(instance=Group_strategy)
@settings(max_examples=50)
def test_group_instantiation(instance):
    assert isinstance(instance, Group)



@given(instance=Group_strategy)
def test_group_admins_setter(instance):
    original = instance.admins
    instance.admins = original
    assert instance.admins == original



@given(instance=Group_strategy)
def test_group_nMembers_setter(instance):
    original = instance.nMembers
    instance.nMembers = original
    assert instance.nMembers == original



@given(instance=Group_strategy)
def test_group_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=Group_strategy)
def test_group_members_setter(instance):
    original = instance.members
    instance.members = original
    assert instance.members == original



@given(instance=Group_strategy)
def test_group_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Group_strategy)
def test_group_posts_setter(instance):
    original = instance.posts
    instance.posts = original
    assert instance.posts == original

@given(instance=User_strategy)
@settings(max_examples=50)
def test_user_instantiation(instance):
    assert isinstance(instance, User)



@given(instance=User_strategy)
def test_user_pages_setter(instance):
    original = instance.pages
    instance.pages = original
    assert instance.pages == original



@given(instance=User_strategy)
def test_user_gender_setter(instance):
    original = instance.gender
    instance.gender = original
    assert instance.gender == original



@given(instance=User_strategy)
def test_user_username_setter(instance):
    original = instance.username
    instance.username = original
    assert instance.username == original



@given(instance=User_strategy)
def test_user_groups_setter(instance):
    original = instance.groups
    instance.groups = original
    assert instance.groups == original



@given(instance=User_strategy)
def test_user_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=User_strategy)
def test_user_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=User_strategy)
def test_user_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original
