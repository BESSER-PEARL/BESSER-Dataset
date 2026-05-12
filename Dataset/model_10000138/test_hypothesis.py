import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Class,
    Another_Login,
    Comment,
    Cryptostream,
    Following_Hashtag,
    Message,
    Mention,
    Like,
    Hashtag,
    Key,
    N_Disturb_User,
    Post,
    Sender,
    Principal,
    Reciever,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_class_constructor_exists():
    assert callable(Class.__init__)


def test_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_another_login_is_not_abstract():
    assert not inspect.isabstract(Another_Login)


def test_another_login_constructor_exists():
    assert callable(Another_Login.__init__)


def test_another_login_constructor_args():
    sig = inspect.signature(Another_Login.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "facebook_id" in params, "Missing parameter 'facebook_id'"
    assert "user_id" in params, "Missing parameter 'user_id'"

def test_another_login_has_id():
    assert hasattr(Another_Login, "id")
    descriptor = None
    for klass in Another_Login.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_another_login_has_facebook_id():
    assert hasattr(Another_Login, "facebook_id")
    descriptor = None
    for klass in Another_Login.__mro__:
        if "facebook_id" in klass.__dict__:
            descriptor = klass.__dict__["facebook_id"]
            break
    assert isinstance(descriptor, property)

def test_another_login_has_user_id():
    assert hasattr(Another_Login, "user_id")
    descriptor = None
    for klass in Another_Login.__mro__:
        if "user_id" in klass.__dict__:
            descriptor = klass.__dict__["user_id"]
            break
    assert isinstance(descriptor, property)



def test_comment_is_not_abstract():
    assert not inspect.isabstract(Comment)


def test_comment_constructor_exists():
    assert callable(Comment.__init__)


def test_comment_constructor_args():
    sig = inspect.signature(Comment.__init__)
    params = list(sig.parameters.keys())
    assert "post_id" in params, "Missing parameter 'post_id'"
    assert "comment_id" in params, "Missing parameter 'comment_id'"
    assert "creation_date" in params, "Missing parameter 'creation_date'"
    assert "content" in params, "Missing parameter 'content'"
    assert "user_id" in params, "Missing parameter 'user_id'"
    assert "id" in params, "Missing parameter 'id'"

def test_comment_has_post_id():
    assert hasattr(Comment, "post_id")
    descriptor = None
    for klass in Comment.__mro__:
        if "post_id" in klass.__dict__:
            descriptor = klass.__dict__["post_id"]
            break
    assert isinstance(descriptor, property)

def test_comment_has_comment_id():
    assert hasattr(Comment, "comment_id")
    descriptor = None
    for klass in Comment.__mro__:
        if "comment_id" in klass.__dict__:
            descriptor = klass.__dict__["comment_id"]
            break
    assert isinstance(descriptor, property)

def test_comment_has_creation_date():
    assert hasattr(Comment, "creation_date")
    descriptor = None
    for klass in Comment.__mro__:
        if "creation_date" in klass.__dict__:
            descriptor = klass.__dict__["creation_date"]
            break
    assert isinstance(descriptor, property)

def test_comment_has_content():
    assert hasattr(Comment, "content")
    descriptor = None
    for klass in Comment.__mro__:
        if "content" in klass.__dict__:
            descriptor = klass.__dict__["content"]
            break
    assert isinstance(descriptor, property)

def test_comment_has_user_id():
    assert hasattr(Comment, "user_id")
    descriptor = None
    for klass in Comment.__mro__:
        if "user_id" in klass.__dict__:
            descriptor = klass.__dict__["user_id"]
            break
    assert isinstance(descriptor, property)

def test_comment_has_id():
    assert hasattr(Comment, "id")
    descriptor = None
    for klass in Comment.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_cryptostream_is_not_abstract():
    assert not inspect.isabstract(Cryptostream)


def test_cryptostream_constructor_exists():
    assert callable(Cryptostream.__init__)


def test_cryptostream_constructor_args():
    sig = inspect.signature(Cryptostream.__init__)
    params = list(sig.parameters.keys())
    assert "user_id" in params, "Missing parameter 'user_id'"
    assert "blocked_user_id" in params, "Missing parameter 'blocked_user_id'"
    assert "id" in params, "Missing parameter 'id'"

def test_cryptostream_has_user_id():
    assert hasattr(Cryptostream, "user_id")
    descriptor = None
    for klass in Cryptostream.__mro__:
        if "user_id" in klass.__dict__:
            descriptor = klass.__dict__["user_id"]
            break
    assert isinstance(descriptor, property)

def test_cryptostream_has_blocked_user_id():
    assert hasattr(Cryptostream, "blocked_user_id")
    descriptor = None
    for klass in Cryptostream.__mro__:
        if "blocked_user_id" in klass.__dict__:
            descriptor = klass.__dict__["blocked_user_id"]
            break
    assert isinstance(descriptor, property)

def test_cryptostream_has_id():
    assert hasattr(Cryptostream, "id")
    descriptor = None
    for klass in Cryptostream.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_following_hashtag_is_not_abstract():
    assert not inspect.isabstract(Following_Hashtag)


def test_following_hashtag_constructor_exists():
    assert callable(Following_Hashtag.__init__)


def test_following_hashtag_constructor_args():
    sig = inspect.signature(Following_Hashtag.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "user_id" in params, "Missing parameter 'user_id'"
    assert "hashtag_id" in params, "Missing parameter 'hashtag_id'"

def test_following_hashtag_has_id():
    assert hasattr(Following_Hashtag, "id")
    descriptor = None
    for klass in Following_Hashtag.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_following_hashtag_has_user_id():
    assert hasattr(Following_Hashtag, "user_id")
    descriptor = None
    for klass in Following_Hashtag.__mro__:
        if "user_id" in klass.__dict__:
            descriptor = klass.__dict__["user_id"]
            break
    assert isinstance(descriptor, property)

def test_following_hashtag_has_hashtag_id():
    assert hasattr(Following_Hashtag, "hashtag_id")
    descriptor = None
    for klass in Following_Hashtag.__mro__:
        if "hashtag_id" in klass.__dict__:
            descriptor = klass.__dict__["hashtag_id"]
            break
    assert isinstance(descriptor, property)



def test_message_is_not_abstract():
    assert not inspect.isabstract(Message)


def test_message_constructor_exists():
    assert callable(Message.__init__)


def test_message_constructor_args():
    sig = inspect.signature(Message.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "message" in params, "Missing parameter 'message'"
    assert "receiver_id" in params, "Missing parameter 'receiver_id'"
    assert "is_deleted" in params, "Missing parameter 'is_deleted'"
    assert "creation_date" in params, "Missing parameter 'creation_date'"
    assert "date_seen" in params, "Missing parameter 'date_seen'"
    assert "sender_id" in params, "Missing parameter 'sender_id'"

def test_message_has_id():
    assert hasattr(Message, "id")
    descriptor = None
    for klass in Message.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_message_has_message():
    assert hasattr(Message, "message")
    descriptor = None
    for klass in Message.__mro__:
        if "message" in klass.__dict__:
            descriptor = klass.__dict__["message"]
            break
    assert isinstance(descriptor, property)

def test_message_has_receiver_id():
    assert hasattr(Message, "receiver_id")
    descriptor = None
    for klass in Message.__mro__:
        if "receiver_id" in klass.__dict__:
            descriptor = klass.__dict__["receiver_id"]
            break
    assert isinstance(descriptor, property)

def test_message_has_is_deleted():
    assert hasattr(Message, "is_deleted")
    descriptor = None
    for klass in Message.__mro__:
        if "is_deleted" in klass.__dict__:
            descriptor = klass.__dict__["is_deleted"]
            break
    assert isinstance(descriptor, property)

def test_message_has_creation_date():
    assert hasattr(Message, "creation_date")
    descriptor = None
    for klass in Message.__mro__:
        if "creation_date" in klass.__dict__:
            descriptor = klass.__dict__["creation_date"]
            break
    assert isinstance(descriptor, property)

def test_message_has_date_seen():
    assert hasattr(Message, "date_seen")
    descriptor = None
    for klass in Message.__mro__:
        if "date_seen" in klass.__dict__:
            descriptor = klass.__dict__["date_seen"]
            break
    assert isinstance(descriptor, property)

def test_message_has_sender_id():
    assert hasattr(Message, "sender_id")
    descriptor = None
    for klass in Message.__mro__:
        if "sender_id" in klass.__dict__:
            descriptor = klass.__dict__["sender_id"]
            break
    assert isinstance(descriptor, property)



def test_mention_is_not_abstract():
    assert not inspect.isabstract(Mention)


def test_mention_constructor_exists():
    assert callable(Mention.__init__)


def test_mention_constructor_args():
    sig = inspect.signature(Mention.__init__)
    params = list(sig.parameters.keys())
    assert "post_id" in params, "Missing parameter 'post_id'"
    assert "user_id" in params, "Missing parameter 'user_id'"
    assert "id" in params, "Missing parameter 'id'"

def test_mention_has_post_id():
    assert hasattr(Mention, "post_id")
    descriptor = None
    for klass in Mention.__mro__:
        if "post_id" in klass.__dict__:
            descriptor = klass.__dict__["post_id"]
            break
    assert isinstance(descriptor, property)

def test_mention_has_user_id():
    assert hasattr(Mention, "user_id")
    descriptor = None
    for klass in Mention.__mro__:
        if "user_id" in klass.__dict__:
            descriptor = klass.__dict__["user_id"]
            break
    assert isinstance(descriptor, property)

def test_mention_has_id():
    assert hasattr(Mention, "id")
    descriptor = None
    for klass in Mention.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_like_is_not_abstract():
    assert not inspect.isabstract(Like)


def test_like_constructor_exists():
    assert callable(Like.__init__)


def test_like_constructor_args():
    sig = inspect.signature(Like.__init__)
    params = list(sig.parameters.keys())
    assert "post_id" in params, "Missing parameter 'post_id'"
    assert "date_sent" in params, "Missing parameter 'date_sent'"
    assert "user_id" in params, "Missing parameter 'user_id'"
    assert "id" in params, "Missing parameter 'id'"

def test_like_has_post_id():
    assert hasattr(Like, "post_id")
    descriptor = None
    for klass in Like.__mro__:
        if "post_id" in klass.__dict__:
            descriptor = klass.__dict__["post_id"]
            break
    assert isinstance(descriptor, property)

def test_like_has_date_sent():
    assert hasattr(Like, "date_sent")
    descriptor = None
    for klass in Like.__mro__:
        if "date_sent" in klass.__dict__:
            descriptor = klass.__dict__["date_sent"]
            break
    assert isinstance(descriptor, property)

def test_like_has_user_id():
    assert hasattr(Like, "user_id")
    descriptor = None
    for klass in Like.__mro__:
        if "user_id" in klass.__dict__:
            descriptor = klass.__dict__["user_id"]
            break
    assert isinstance(descriptor, property)

def test_like_has_id():
    assert hasattr(Like, "id")
    descriptor = None
    for klass in Like.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_hashtag_is_not_abstract():
    assert not inspect.isabstract(Hashtag)


def test_hashtag_constructor_exists():
    assert callable(Hashtag.__init__)


def test_hashtag_constructor_args():
    sig = inspect.signature(Hashtag.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "tag" in params, "Missing parameter 'tag'"

def test_hashtag_has_id():
    assert hasattr(Hashtag, "id")
    descriptor = None
    for klass in Hashtag.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_hashtag_has_tag():
    assert hasattr(Hashtag, "tag")
    descriptor = None
    for klass in Hashtag.__mro__:
        if "tag" in klass.__dict__:
            descriptor = klass.__dict__["tag"]
            break
    assert isinstance(descriptor, property)



def test_key_is_not_abstract():
    assert not inspect.isabstract(Key)


def test_key_constructor_exists():
    assert callable(Key.__init__)


def test_key_constructor_args():
    sig = inspect.signature(Key.__init__)
    params = list(sig.parameters.keys())
    assert "Value" in params, "Missing parameter 'Value'"
    assert "coordinat_y" in params, "Missing parameter 'coordinat_y'"
    assert "id" in params, "Missing parameter 'id'"
    assert "Length" in params, "Missing parameter 'Length'"

def test_key_has_Value():
    assert hasattr(Key, "Value")
    descriptor = None
    for klass in Key.__mro__:
        if "Value" in klass.__dict__:
            descriptor = klass.__dict__["Value"]
            break
    assert isinstance(descriptor, property)

def test_key_has_coordinat_y():
    assert hasattr(Key, "coordinat_y")
    descriptor = None
    for klass in Key.__mro__:
        if "coordinat_y" in klass.__dict__:
            descriptor = klass.__dict__["coordinat_y"]
            break
    assert isinstance(descriptor, property)

def test_key_has_id():
    assert hasattr(Key, "id")
    descriptor = None
    for klass in Key.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_key_has_Length():
    assert hasattr(Key, "Length")
    descriptor = None
    for klass in Key.__mro__:
        if "Length" in klass.__dict__:
            descriptor = klass.__dict__["Length"]
            break
    assert isinstance(descriptor, property)



def test_n_disturb_user_is_not_abstract():
    assert not inspect.isabstract(N_Disturb_User)


def test_n_disturb_user_constructor_exists():
    assert callable(N_Disturb_User.__init__)


def test_n_disturb_user_constructor_args():
    sig = inspect.signature(N_Disturb_User.__init__)
    params = list(sig.parameters.keys())
    assert "user_id" in params, "Missing parameter 'user_id'"
    assert "id" in params, "Missing parameter 'id'"
    assert "disturb_user_id" in params, "Missing parameter 'disturb_user_id'"

def test_n_disturb_user_has_user_id():
    assert hasattr(N_Disturb_User, "user_id")
    descriptor = None
    for klass in N_Disturb_User.__mro__:
        if "user_id" in klass.__dict__:
            descriptor = klass.__dict__["user_id"]
            break
    assert isinstance(descriptor, property)

def test_n_disturb_user_has_id():
    assert hasattr(N_Disturb_User, "id")
    descriptor = None
    for klass in N_Disturb_User.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_n_disturb_user_has_disturb_user_id():
    assert hasattr(N_Disturb_User, "disturb_user_id")
    descriptor = None
    for klass in N_Disturb_User.__mro__:
        if "disturb_user_id" in klass.__dict__:
            descriptor = klass.__dict__["disturb_user_id"]
            break
    assert isinstance(descriptor, property)



def test_post_is_not_abstract():
    assert not inspect.isabstract(Post)


def test_post_constructor_exists():
    assert callable(Post.__init__)


def test_post_constructor_args():
    sig = inspect.signature(Post.__init__)
    params = list(sig.parameters.keys())
    assert "date_update" in params, "Missing parameter 'date_update'"
    assert "id" in params, "Missing parameter 'id'"
    assert "text" in params, "Missing parameter 'text'"
    assert "total_like" in params, "Missing parameter 'total_like'"
    assert "hashtag_id" in params, "Missing parameter 'hashtag_id'"
    assert "status" in params, "Missing parameter 'status'"
    assert "creation_date" in params, "Missing parameter 'creation_date'"
    assert "location_id" in params, "Missing parameter 'location_id'"

def test_post_has_date_update():
    assert hasattr(Post, "date_update")
    descriptor = None
    for klass in Post.__mro__:
        if "date_update" in klass.__dict__:
            descriptor = klass.__dict__["date_update"]
            break
    assert isinstance(descriptor, property)

def test_post_has_id():
    assert hasattr(Post, "id")
    descriptor = None
    for klass in Post.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_post_has_text():
    assert hasattr(Post, "text")
    descriptor = None
    for klass in Post.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)

def test_post_has_total_like():
    assert hasattr(Post, "total_like")
    descriptor = None
    for klass in Post.__mro__:
        if "total_like" in klass.__dict__:
            descriptor = klass.__dict__["total_like"]
            break
    assert isinstance(descriptor, property)

def test_post_has_hashtag_id():
    assert hasattr(Post, "hashtag_id")
    descriptor = None
    for klass in Post.__mro__:
        if "hashtag_id" in klass.__dict__:
            descriptor = klass.__dict__["hashtag_id"]
            break
    assert isinstance(descriptor, property)

def test_post_has_status():
    assert hasattr(Post, "status")
    descriptor = None
    for klass in Post.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)

def test_post_has_creation_date():
    assert hasattr(Post, "creation_date")
    descriptor = None
    for klass in Post.__mro__:
        if "creation_date" in klass.__dict__:
            descriptor = klass.__dict__["creation_date"]
            break
    assert isinstance(descriptor, property)

def test_post_has_location_id():
    assert hasattr(Post, "location_id")
    descriptor = None
    for klass in Post.__mro__:
        if "location_id" in klass.__dict__:
            descriptor = klass.__dict__["location_id"]
            break
    assert isinstance(descriptor, property)



def test_sender_is_not_abstract():
    assert not inspect.isabstract(Sender)


def test_sender_constructor_exists():
    assert callable(Sender.__init__)


def test_sender_constructor_args():
    sig = inspect.signature(Sender.__init__)
    params = list(sig.parameters.keys())
    assert "status" in params, "Missing parameter 'status'"
    assert "following_id" in params, "Missing parameter 'following_id'"
    assert "user_id" in params, "Missing parameter 'user_id'"
    assert "creation_date" in params, "Missing parameter 'creation_date'"
    assert "id" in params, "Missing parameter 'id'"

def test_sender_has_status():
    assert hasattr(Sender, "status")
    descriptor = None
    for klass in Sender.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)

def test_sender_has_following_id():
    assert hasattr(Sender, "following_id")
    descriptor = None
    for klass in Sender.__mro__:
        if "following_id" in klass.__dict__:
            descriptor = klass.__dict__["following_id"]
            break
    assert isinstance(descriptor, property)

def test_sender_has_user_id():
    assert hasattr(Sender, "user_id")
    descriptor = None
    for klass in Sender.__mro__:
        if "user_id" in klass.__dict__:
            descriptor = klass.__dict__["user_id"]
            break
    assert isinstance(descriptor, property)

def test_sender_has_creation_date():
    assert hasattr(Sender, "creation_date")
    descriptor = None
    for klass in Sender.__mro__:
        if "creation_date" in klass.__dict__:
            descriptor = klass.__dict__["creation_date"]
            break
    assert isinstance(descriptor, property)

def test_sender_has_id():
    assert hasattr(Sender, "id")
    descriptor = None
    for klass in Sender.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_principal_is_not_abstract():
    assert not inspect.isabstract(Principal)


def test_principal_constructor_exists():
    assert callable(Principal.__init__)


def test_principal_constructor_args():
    sig = inspect.signature(Principal.__init__)
    params = list(sig.parameters.keys())
    assert "creation_date" in params, "Missing parameter 'creation_date'"
    assert "id" in params, "Missing parameter 'id'"
    assert "user_id" in params, "Missing parameter 'user_id'"
    assert "followers_id" in params, "Missing parameter 'followers_id'"
    assert "status" in params, "Missing parameter 'status'"

def test_principal_has_creation_date():
    assert hasattr(Principal, "creation_date")
    descriptor = None
    for klass in Principal.__mro__:
        if "creation_date" in klass.__dict__:
            descriptor = klass.__dict__["creation_date"]
            break
    assert isinstance(descriptor, property)

def test_principal_has_id():
    assert hasattr(Principal, "id")
    descriptor = None
    for klass in Principal.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_principal_has_user_id():
    assert hasattr(Principal, "user_id")
    descriptor = None
    for klass in Principal.__mro__:
        if "user_id" in klass.__dict__:
            descriptor = klass.__dict__["user_id"]
            break
    assert isinstance(descriptor, property)

def test_principal_has_followers_id():
    assert hasattr(Principal, "followers_id")
    descriptor = None
    for klass in Principal.__mro__:
        if "followers_id" in klass.__dict__:
            descriptor = klass.__dict__["followers_id"]
            break
    assert isinstance(descriptor, property)

def test_principal_has_status():
    assert hasattr(Principal, "status")
    descriptor = None
    for klass in Principal.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)



def test_reciever_is_not_abstract():
    assert not inspect.isabstract(Reciever)


def test_reciever_constructor_exists():
    assert callable(Reciever.__init__)


def test_reciever_constructor_args():
    sig = inspect.signature(Reciever.__init__)
    params = list(sig.parameters.keys())
    assert "is_active" in params, "Missing parameter 'is_active'"
    assert "is_admin" in params, "Missing parameter 'is_admin'"
    assert "name" in params, "Missing parameter 'name'"
    assert "password" in params, "Missing parameter 'password'"
    assert "phone" in params, "Missing parameter 'phone'"
    assert "username" in params, "Missing parameter 'username'"
    assert "id" in params, "Missing parameter 'id'"
    assert "is_private" in params, "Missing parameter 'is_private'"
    assert "surname" in params, "Missing parameter 'surname'"
    assert "mail" in params, "Missing parameter 'mail'"
    assert "user_id" in params, "Missing parameter 'user_id'"

def test_reciever_has_is_active():
    assert hasattr(Reciever, "is_active")
    descriptor = None
    for klass in Reciever.__mro__:
        if "is_active" in klass.__dict__:
            descriptor = klass.__dict__["is_active"]
            break
    assert isinstance(descriptor, property)

def test_reciever_has_is_admin():
    assert hasattr(Reciever, "is_admin")
    descriptor = None
    for klass in Reciever.__mro__:
        if "is_admin" in klass.__dict__:
            descriptor = klass.__dict__["is_admin"]
            break
    assert isinstance(descriptor, property)

def test_reciever_has_name():
    assert hasattr(Reciever, "name")
    descriptor = None
    for klass in Reciever.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_reciever_has_password():
    assert hasattr(Reciever, "password")
    descriptor = None
    for klass in Reciever.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)

def test_reciever_has_phone():
    assert hasattr(Reciever, "phone")
    descriptor = None
    for klass in Reciever.__mro__:
        if "phone" in klass.__dict__:
            descriptor = klass.__dict__["phone"]
            break
    assert isinstance(descriptor, property)

def test_reciever_has_username():
    assert hasattr(Reciever, "username")
    descriptor = None
    for klass in Reciever.__mro__:
        if "username" in klass.__dict__:
            descriptor = klass.__dict__["username"]
            break
    assert isinstance(descriptor, property)

def test_reciever_has_id():
    assert hasattr(Reciever, "id")
    descriptor = None
    for klass in Reciever.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_reciever_has_is_private():
    assert hasattr(Reciever, "is_private")
    descriptor = None
    for klass in Reciever.__mro__:
        if "is_private" in klass.__dict__:
            descriptor = klass.__dict__["is_private"]
            break
    assert isinstance(descriptor, property)

def test_reciever_has_surname():
    assert hasattr(Reciever, "surname")
    descriptor = None
    for klass in Reciever.__mro__:
        if "surname" in klass.__dict__:
            descriptor = klass.__dict__["surname"]
            break
    assert isinstance(descriptor, property)

def test_reciever_has_mail():
    assert hasattr(Reciever, "mail")
    descriptor = None
    for klass in Reciever.__mro__:
        if "mail" in klass.__dict__:
            descriptor = klass.__dict__["mail"]
            break
    assert isinstance(descriptor, property)

def test_reciever_has_user_id():
    assert hasattr(Reciever, "user_id")
    descriptor = None
    for klass in Reciever.__mro__:
        if "user_id" in klass.__dict__:
            descriptor = klass.__dict__["user_id"]
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
Class_strategy = st.builds(
    Class,
)
Another_Login_strategy = st.builds(
    Another_Login,
    id=
        st.integers(),
    facebook_id=
        st.integers(),
    user_id=
        st.integers()
)
Comment_strategy = st.builds(
    Comment,
    post_id=
        st.integers(),
    comment_id=
        st.integers(),
    creation_date=
        safe_text,
    content=
        st.integers(),
    user_id=
        st.integers(),
    id=
        st.integers()
)
Cryptostream_strategy = st.builds(
    Cryptostream,
    user_id=
        st.integers(),
    blocked_user_id=
        st.integers(),
    id=
        st.integers()
)
Following_Hashtag_strategy = st.builds(
    Following_Hashtag,
    id=
        st.integers(),
    user_id=
        st.integers(),
    hashtag_id=
        st.integers()
)
Message_strategy = st.builds(
    Message,
    id=
        st.integers(),
    message=
        safe_text,
    receiver_id=
        st.integers(),
    is_deleted=
        st.booleans(),
    creation_date=
        safe_text,
    date_seen=
        safe_text,
    sender_id=
        st.integers()
)
Mention_strategy = st.builds(
    Mention,
    post_id=
        st.integers(),
    user_id=
        st.integers(),
    id=
        st.integers()
)
Like_strategy = st.builds(
    Like,
    post_id=
        st.integers(),
    date_sent=
        safe_text,
    user_id=
        st.integers(),
    id=
        st.integers()
)
Hashtag_strategy = st.builds(
    Hashtag,
    id=
        st.integers(),
    tag=
        safe_text
)
Key_strategy = st.builds(
    Key,
    Value=
        safe_text,
    coordinat_y=
        st.integers(),
    id=
        st.integers(),
    Length=
        safe_text
)
N_Disturb_User_strategy = st.builds(
    N_Disturb_User,
    user_id=
        st.integers(),
    id=
        st.integers(),
    disturb_user_id=
        st.integers()
)
Post_strategy = st.builds(
    Post,
    date_update=
        safe_text,
    id=
        st.integers(),
    text=
        safe_text,
    total_like=
        st.integers(),
    hashtag_id=
        st.integers(),
    status=
        safe_text,
    creation_date=
        safe_text,
    location_id=
        st.integers()
)
Sender_strategy = st.builds(
    Sender,
    status=
        safe_text,
    following_id=
        st.integers(),
    user_id=
        st.integers(),
    creation_date=
        safe_text,
    id=
        st.integers()
)
Principal_strategy = st.builds(
    Principal,
    creation_date=
        safe_text,
    id=
        st.integers(),
    user_id=
        st.integers(),
    followers_id=
        st.integers(),
    status=
        safe_text
)
Reciever_strategy = st.builds(
    Reciever,
    is_active=
        st.booleans(),
    is_admin=
        st.booleans(),
    name=
        safe_text,
    password=
        safe_text,
    phone=
        safe_text,
    username=
        safe_text,
    id=
        st.integers(),
    is_private=
        st.booleans(),
    surname=
        safe_text,
    mail=
        safe_text,
    user_id=
        st.integers()
)

@given(instance=Class_strategy)
@settings(max_examples=50)
def test_class_instantiation(instance):
    assert isinstance(instance, Class)

@given(instance=Another_Login_strategy)
@settings(max_examples=50)
def test_another_login_instantiation(instance):
    assert isinstance(instance, Another_Login)



@given(instance=Another_Login_strategy)
def test_another_login_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Another_Login_strategy)
def test_another_login_facebook_id_setter(instance):
    original = instance.facebook_id
    instance.facebook_id = original
    assert instance.facebook_id == original



@given(instance=Another_Login_strategy)
def test_another_login_user_id_setter(instance):
    original = instance.user_id
    instance.user_id = original
    assert instance.user_id == original

@given(instance=Comment_strategy)
@settings(max_examples=50)
def test_comment_instantiation(instance):
    assert isinstance(instance, Comment)



@given(instance=Comment_strategy)
def test_comment_post_id_setter(instance):
    original = instance.post_id
    instance.post_id = original
    assert instance.post_id == original



@given(instance=Comment_strategy)
def test_comment_comment_id_setter(instance):
    original = instance.comment_id
    instance.comment_id = original
    assert instance.comment_id == original



@given(instance=Comment_strategy)
def test_comment_creation_date_setter(instance):
    original = instance.creation_date
    instance.creation_date = original
    assert instance.creation_date == original



@given(instance=Comment_strategy)
def test_comment_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original



@given(instance=Comment_strategy)
def test_comment_user_id_setter(instance):
    original = instance.user_id
    instance.user_id = original
    assert instance.user_id == original



@given(instance=Comment_strategy)
def test_comment_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Cryptostream_strategy)
@settings(max_examples=50)
def test_cryptostream_instantiation(instance):
    assert isinstance(instance, Cryptostream)



@given(instance=Cryptostream_strategy)
def test_cryptostream_user_id_setter(instance):
    original = instance.user_id
    instance.user_id = original
    assert instance.user_id == original



@given(instance=Cryptostream_strategy)
def test_cryptostream_blocked_user_id_setter(instance):
    original = instance.blocked_user_id
    instance.blocked_user_id = original
    assert instance.blocked_user_id == original



@given(instance=Cryptostream_strategy)
def test_cryptostream_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Following_Hashtag_strategy)
@settings(max_examples=50)
def test_following_hashtag_instantiation(instance):
    assert isinstance(instance, Following_Hashtag)



@given(instance=Following_Hashtag_strategy)
def test_following_hashtag_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Following_Hashtag_strategy)
def test_following_hashtag_user_id_setter(instance):
    original = instance.user_id
    instance.user_id = original
    assert instance.user_id == original



@given(instance=Following_Hashtag_strategy)
def test_following_hashtag_hashtag_id_setter(instance):
    original = instance.hashtag_id
    instance.hashtag_id = original
    assert instance.hashtag_id == original

@given(instance=Message_strategy)
@settings(max_examples=50)
def test_message_instantiation(instance):
    assert isinstance(instance, Message)



@given(instance=Message_strategy)
def test_message_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Message_strategy)
def test_message_message_setter(instance):
    original = instance.message
    instance.message = original
    assert instance.message == original



@given(instance=Message_strategy)
def test_message_receiver_id_setter(instance):
    original = instance.receiver_id
    instance.receiver_id = original
    assert instance.receiver_id == original



@given(instance=Message_strategy)
def test_message_is_deleted_setter(instance):
    original = instance.is_deleted
    instance.is_deleted = original
    assert instance.is_deleted == original



@given(instance=Message_strategy)
def test_message_creation_date_setter(instance):
    original = instance.creation_date
    instance.creation_date = original
    assert instance.creation_date == original



@given(instance=Message_strategy)
def test_message_date_seen_setter(instance):
    original = instance.date_seen
    instance.date_seen = original
    assert instance.date_seen == original



@given(instance=Message_strategy)
def test_message_sender_id_setter(instance):
    original = instance.sender_id
    instance.sender_id = original
    assert instance.sender_id == original

@given(instance=Mention_strategy)
@settings(max_examples=50)
def test_mention_instantiation(instance):
    assert isinstance(instance, Mention)



@given(instance=Mention_strategy)
def test_mention_post_id_setter(instance):
    original = instance.post_id
    instance.post_id = original
    assert instance.post_id == original



@given(instance=Mention_strategy)
def test_mention_user_id_setter(instance):
    original = instance.user_id
    instance.user_id = original
    assert instance.user_id == original



@given(instance=Mention_strategy)
def test_mention_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Like_strategy)
@settings(max_examples=50)
def test_like_instantiation(instance):
    assert isinstance(instance, Like)



@given(instance=Like_strategy)
def test_like_post_id_setter(instance):
    original = instance.post_id
    instance.post_id = original
    assert instance.post_id == original



@given(instance=Like_strategy)
def test_like_date_sent_setter(instance):
    original = instance.date_sent
    instance.date_sent = original
    assert instance.date_sent == original



@given(instance=Like_strategy)
def test_like_user_id_setter(instance):
    original = instance.user_id
    instance.user_id = original
    assert instance.user_id == original



@given(instance=Like_strategy)
def test_like_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Hashtag_strategy)
@settings(max_examples=50)
def test_hashtag_instantiation(instance):
    assert isinstance(instance, Hashtag)



@given(instance=Hashtag_strategy)
def test_hashtag_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Hashtag_strategy)
def test_hashtag_tag_setter(instance):
    original = instance.tag
    instance.tag = original
    assert instance.tag == original

@given(instance=Key_strategy)
@settings(max_examples=50)
def test_key_instantiation(instance):
    assert isinstance(instance, Key)



@given(instance=Key_strategy)
def test_key_Value_setter(instance):
    original = instance.Value
    instance.Value = original
    assert instance.Value == original



@given(instance=Key_strategy)
def test_key_coordinat_y_setter(instance):
    original = instance.coordinat_y
    instance.coordinat_y = original
    assert instance.coordinat_y == original



@given(instance=Key_strategy)
def test_key_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Key_strategy)
def test_key_Length_setter(instance):
    original = instance.Length
    instance.Length = original
    assert instance.Length == original

@given(instance=N_Disturb_User_strategy)
@settings(max_examples=50)
def test_n_disturb_user_instantiation(instance):
    assert isinstance(instance, N_Disturb_User)



@given(instance=N_Disturb_User_strategy)
def test_n_disturb_user_user_id_setter(instance):
    original = instance.user_id
    instance.user_id = original
    assert instance.user_id == original



@given(instance=N_Disturb_User_strategy)
def test_n_disturb_user_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=N_Disturb_User_strategy)
def test_n_disturb_user_disturb_user_id_setter(instance):
    original = instance.disturb_user_id
    instance.disturb_user_id = original
    assert instance.disturb_user_id == original

@given(instance=Post_strategy)
@settings(max_examples=50)
def test_post_instantiation(instance):
    assert isinstance(instance, Post)



@given(instance=Post_strategy)
def test_post_date_update_setter(instance):
    original = instance.date_update
    instance.date_update = original
    assert instance.date_update == original



@given(instance=Post_strategy)
def test_post_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Post_strategy)
def test_post_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original



@given(instance=Post_strategy)
def test_post_total_like_setter(instance):
    original = instance.total_like
    instance.total_like = original
    assert instance.total_like == original



@given(instance=Post_strategy)
def test_post_hashtag_id_setter(instance):
    original = instance.hashtag_id
    instance.hashtag_id = original
    assert instance.hashtag_id == original



@given(instance=Post_strategy)
def test_post_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original



@given(instance=Post_strategy)
def test_post_creation_date_setter(instance):
    original = instance.creation_date
    instance.creation_date = original
    assert instance.creation_date == original



@given(instance=Post_strategy)
def test_post_location_id_setter(instance):
    original = instance.location_id
    instance.location_id = original
    assert instance.location_id == original

@given(instance=Sender_strategy)
@settings(max_examples=50)
def test_sender_instantiation(instance):
    assert isinstance(instance, Sender)



@given(instance=Sender_strategy)
def test_sender_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original



@given(instance=Sender_strategy)
def test_sender_following_id_setter(instance):
    original = instance.following_id
    instance.following_id = original
    assert instance.following_id == original



@given(instance=Sender_strategy)
def test_sender_user_id_setter(instance):
    original = instance.user_id
    instance.user_id = original
    assert instance.user_id == original



@given(instance=Sender_strategy)
def test_sender_creation_date_setter(instance):
    original = instance.creation_date
    instance.creation_date = original
    assert instance.creation_date == original



@given(instance=Sender_strategy)
def test_sender_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Principal_strategy)
@settings(max_examples=50)
def test_principal_instantiation(instance):
    assert isinstance(instance, Principal)



@given(instance=Principal_strategy)
def test_principal_creation_date_setter(instance):
    original = instance.creation_date
    instance.creation_date = original
    assert instance.creation_date == original



@given(instance=Principal_strategy)
def test_principal_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Principal_strategy)
def test_principal_user_id_setter(instance):
    original = instance.user_id
    instance.user_id = original
    assert instance.user_id == original



@given(instance=Principal_strategy)
def test_principal_followers_id_setter(instance):
    original = instance.followers_id
    instance.followers_id = original
    assert instance.followers_id == original



@given(instance=Principal_strategy)
def test_principal_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original

@given(instance=Reciever_strategy)
@settings(max_examples=50)
def test_reciever_instantiation(instance):
    assert isinstance(instance, Reciever)



@given(instance=Reciever_strategy)
def test_reciever_is_active_setter(instance):
    original = instance.is_active
    instance.is_active = original
    assert instance.is_active == original



@given(instance=Reciever_strategy)
def test_reciever_is_admin_setter(instance):
    original = instance.is_admin
    instance.is_admin = original
    assert instance.is_admin == original



@given(instance=Reciever_strategy)
def test_reciever_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Reciever_strategy)
def test_reciever_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=Reciever_strategy)
def test_reciever_phone_setter(instance):
    original = instance.phone
    instance.phone = original
    assert instance.phone == original



@given(instance=Reciever_strategy)
def test_reciever_username_setter(instance):
    original = instance.username
    instance.username = original
    assert instance.username == original



@given(instance=Reciever_strategy)
def test_reciever_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Reciever_strategy)
def test_reciever_is_private_setter(instance):
    original = instance.is_private
    instance.is_private = original
    assert instance.is_private == original



@given(instance=Reciever_strategy)
def test_reciever_surname_setter(instance):
    original = instance.surname
    instance.surname = original
    assert instance.surname == original



@given(instance=Reciever_strategy)
def test_reciever_mail_setter(instance):
    original = instance.mail
    instance.mail = original
    assert instance.mail == original



@given(instance=Reciever_strategy)
def test_reciever_user_id_setter(instance):
    original = instance.user_id
    instance.user_id = original
    assert instance.user_id == original
