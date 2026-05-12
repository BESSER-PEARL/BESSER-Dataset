import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    UseCase_UseCase,
    Actor_Actor,
    Repeat_Non_UseCase,
    Shuflfe_play_UseCase,
    Stop_UseCase,
    Pause_UseCase,
    Favorite_UseCase,
    Search_UseCase,
    Create_playlist_UseCase,
    Play_UseCase,
    Download_UseCase,
    User_Actor,
    TopMostPlayed,
    Recently_Played,
    Downloads,
    Favourites,
    Playlist_Song,
    Playlist,
    Song,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_usecase_usecase_is_not_abstract():
    assert not inspect.isabstract(UseCase_UseCase)


def test_usecase_usecase_constructor_exists():
    assert callable(UseCase_UseCase.__init__)


def test_usecase_usecase_constructor_args():
    sig = inspect.signature(UseCase_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_actor_actor_is_not_abstract():
    assert not inspect.isabstract(Actor_Actor)


def test_actor_actor_constructor_exists():
    assert callable(Actor_Actor.__init__)


def test_actor_actor_constructor_args():
    sig = inspect.signature(Actor_Actor.__init__)
    params = list(sig.parameters.keys())



def test_repeat_non_usecase_is_not_abstract():
    assert not inspect.isabstract(Repeat_Non_UseCase)


def test_repeat_non_usecase_constructor_exists():
    assert callable(Repeat_Non_UseCase.__init__)


def test_repeat_non_usecase_constructor_args():
    sig = inspect.signature(Repeat_Non_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_shuflfe_play_usecase_is_not_abstract():
    assert not inspect.isabstract(Shuflfe_play_UseCase)


def test_shuflfe_play_usecase_constructor_exists():
    assert callable(Shuflfe_play_UseCase.__init__)


def test_shuflfe_play_usecase_constructor_args():
    sig = inspect.signature(Shuflfe_play_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_stop_usecase_is_not_abstract():
    assert not inspect.isabstract(Stop_UseCase)


def test_stop_usecase_constructor_exists():
    assert callable(Stop_UseCase.__init__)


def test_stop_usecase_constructor_args():
    sig = inspect.signature(Stop_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_pause_usecase_is_not_abstract():
    assert not inspect.isabstract(Pause_UseCase)


def test_pause_usecase_constructor_exists():
    assert callable(Pause_UseCase.__init__)


def test_pause_usecase_constructor_args():
    sig = inspect.signature(Pause_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_favorite_usecase_is_not_abstract():
    assert not inspect.isabstract(Favorite_UseCase)


def test_favorite_usecase_constructor_exists():
    assert callable(Favorite_UseCase.__init__)


def test_favorite_usecase_constructor_args():
    sig = inspect.signature(Favorite_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_search_usecase_is_not_abstract():
    assert not inspect.isabstract(Search_UseCase)


def test_search_usecase_constructor_exists():
    assert callable(Search_UseCase.__init__)


def test_search_usecase_constructor_args():
    sig = inspect.signature(Search_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_create_playlist_usecase_is_not_abstract():
    assert not inspect.isabstract(Create_playlist_UseCase)


def test_create_playlist_usecase_constructor_exists():
    assert callable(Create_playlist_UseCase.__init__)


def test_create_playlist_usecase_constructor_args():
    sig = inspect.signature(Create_playlist_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_play_usecase_is_not_abstract():
    assert not inspect.isabstract(Play_UseCase)


def test_play_usecase_constructor_exists():
    assert callable(Play_UseCase.__init__)


def test_play_usecase_constructor_args():
    sig = inspect.signature(Play_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_download_usecase_is_not_abstract():
    assert not inspect.isabstract(Download_UseCase)


def test_download_usecase_constructor_exists():
    assert callable(Download_UseCase.__init__)


def test_download_usecase_constructor_args():
    sig = inspect.signature(Download_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_user_actor_is_not_abstract():
    assert not inspect.isabstract(User_Actor)


def test_user_actor_constructor_exists():
    assert callable(User_Actor.__init__)


def test_user_actor_constructor_args():
    sig = inspect.signature(User_Actor.__init__)
    params = list(sig.parameters.keys())



def test_topmostplayed_is_not_abstract():
    assert not inspect.isabstract(TopMostPlayed)


def test_topmostplayed_constructor_exists():
    assert callable(TopMostPlayed.__init__)


def test_topmostplayed_constructor_args():
    sig = inspect.signature(TopMostPlayed.__init__)
    params = list(sig.parameters.keys())
    assert "sID" in params, "Missing parameter 'sID'"
    assert "mpID" in params, "Missing parameter 'mpID'"

def test_topmostplayed_has_sID():
    assert hasattr(TopMostPlayed, "sID")
    descriptor = None
    for klass in TopMostPlayed.__mro__:
        if "sID" in klass.__dict__:
            descriptor = klass.__dict__["sID"]
            break
    assert isinstance(descriptor, property)

def test_topmostplayed_has_mpID():
    assert hasattr(TopMostPlayed, "mpID")
    descriptor = None
    for klass in TopMostPlayed.__mro__:
        if "mpID" in klass.__dict__:
            descriptor = klass.__dict__["mpID"]
            break
    assert isinstance(descriptor, property)



def test_recently_played_is_not_abstract():
    assert not inspect.isabstract(Recently_Played)


def test_recently_played_constructor_exists():
    assert callable(Recently_Played.__init__)


def test_recently_played_constructor_args():
    sig = inspect.signature(Recently_Played.__init__)
    params = list(sig.parameters.keys())
    assert "rpID" in params, "Missing parameter 'rpID'"
    assert "sID" in params, "Missing parameter 'sID'"

def test_recently_played_has_rpID():
    assert hasattr(Recently_Played, "rpID")
    descriptor = None
    for klass in Recently_Played.__mro__:
        if "rpID" in klass.__dict__:
            descriptor = klass.__dict__["rpID"]
            break
    assert isinstance(descriptor, property)

def test_recently_played_has_sID():
    assert hasattr(Recently_Played, "sID")
    descriptor = None
    for klass in Recently_Played.__mro__:
        if "sID" in klass.__dict__:
            descriptor = klass.__dict__["sID"]
            break
    assert isinstance(descriptor, property)



def test_downloads_is_not_abstract():
    assert not inspect.isabstract(Downloads)


def test_downloads_constructor_exists():
    assert callable(Downloads.__init__)


def test_downloads_constructor_args():
    sig = inspect.signature(Downloads.__init__)
    params = list(sig.parameters.keys())
    assert "sID" in params, "Missing parameter 'sID'"
    assert "dID" in params, "Missing parameter 'dID'"

def test_downloads_has_sID():
    assert hasattr(Downloads, "sID")
    descriptor = None
    for klass in Downloads.__mro__:
        if "sID" in klass.__dict__:
            descriptor = klass.__dict__["sID"]
            break
    assert isinstance(descriptor, property)

def test_downloads_has_dID():
    assert hasattr(Downloads, "dID")
    descriptor = None
    for klass in Downloads.__mro__:
        if "dID" in klass.__dict__:
            descriptor = klass.__dict__["dID"]
            break
    assert isinstance(descriptor, property)



def test_favourites_is_not_abstract():
    assert not inspect.isabstract(Favourites)


def test_favourites_constructor_exists():
    assert callable(Favourites.__init__)


def test_favourites_constructor_args():
    sig = inspect.signature(Favourites.__init__)
    params = list(sig.parameters.keys())
    assert "sID" in params, "Missing parameter 'sID'"
    assert "fID" in params, "Missing parameter 'fID'"

def test_favourites_has_sID():
    assert hasattr(Favourites, "sID")
    descriptor = None
    for klass in Favourites.__mro__:
        if "sID" in klass.__dict__:
            descriptor = klass.__dict__["sID"]
            break
    assert isinstance(descriptor, property)

def test_favourites_has_fID():
    assert hasattr(Favourites, "fID")
    descriptor = None
    for klass in Favourites.__mro__:
        if "fID" in klass.__dict__:
            descriptor = klass.__dict__["fID"]
            break
    assert isinstance(descriptor, property)



def test_playlist_song_is_not_abstract():
    assert not inspect.isabstract(Playlist_Song)


def test_playlist_song_constructor_exists():
    assert callable(Playlist_Song.__init__)


def test_playlist_song_constructor_args():
    sig = inspect.signature(Playlist_Song.__init__)
    params = list(sig.parameters.keys())
    assert "pID" in params, "Missing parameter 'pID'"
    assert "sID" in params, "Missing parameter 'sID'"

def test_playlist_song_has_pID():
    assert hasattr(Playlist_Song, "pID")
    descriptor = None
    for klass in Playlist_Song.__mro__:
        if "pID" in klass.__dict__:
            descriptor = klass.__dict__["pID"]
            break
    assert isinstance(descriptor, property)

def test_playlist_song_has_sID():
    assert hasattr(Playlist_Song, "sID")
    descriptor = None
    for klass in Playlist_Song.__mro__:
        if "sID" in klass.__dict__:
            descriptor = klass.__dict__["sID"]
            break
    assert isinstance(descriptor, property)



def test_playlist_is_not_abstract():
    assert not inspect.isabstract(Playlist)


def test_playlist_constructor_exists():
    assert callable(Playlist.__init__)


def test_playlist_constructor_args():
    sig = inspect.signature(Playlist.__init__)
    params = list(sig.parameters.keys())
    assert "pID" in params, "Missing parameter 'pID'"
    assert "pName" in params, "Missing parameter 'pName'"
    assert "pDate" in params, "Missing parameter 'pDate'"

def test_playlist_has_pID():
    assert hasattr(Playlist, "pID")
    descriptor = None
    for klass in Playlist.__mro__:
        if "pID" in klass.__dict__:
            descriptor = klass.__dict__["pID"]
            break
    assert isinstance(descriptor, property)

def test_playlist_has_pName():
    assert hasattr(Playlist, "pName")
    descriptor = None
    for klass in Playlist.__mro__:
        if "pName" in klass.__dict__:
            descriptor = klass.__dict__["pName"]
            break
    assert isinstance(descriptor, property)

def test_playlist_has_pDate():
    assert hasattr(Playlist, "pDate")
    descriptor = None
    for klass in Playlist.__mro__:
        if "pDate" in klass.__dict__:
            descriptor = klass.__dict__["pDate"]
            break
    assert isinstance(descriptor, property)



def test_song_is_not_abstract():
    assert not inspect.isabstract(Song)


def test_song_constructor_exists():
    assert callable(Song.__init__)


def test_song_constructor_args():
    sig = inspect.signature(Song.__init__)
    params = list(sig.parameters.keys())
    assert "sIMG_url" in params, "Missing parameter 'sIMG_url'"
    assert "sName" in params, "Missing parameter 'sName'"
    assert "sCateg" in params, "Missing parameter 'sCateg'"
    assert "sDate" in params, "Missing parameter 'sDate'"
    assert "sArtist" in params, "Missing parameter 'sArtist'"
    assert "sID" in params, "Missing parameter 'sID'"

def test_song_has_sIMG_url():
    assert hasattr(Song, "sIMG_url")
    descriptor = None
    for klass in Song.__mro__:
        if "sIMG_url" in klass.__dict__:
            descriptor = klass.__dict__["sIMG_url"]
            break
    assert isinstance(descriptor, property)

def test_song_has_sName():
    assert hasattr(Song, "sName")
    descriptor = None
    for klass in Song.__mro__:
        if "sName" in klass.__dict__:
            descriptor = klass.__dict__["sName"]
            break
    assert isinstance(descriptor, property)

def test_song_has_sCateg():
    assert hasattr(Song, "sCateg")
    descriptor = None
    for klass in Song.__mro__:
        if "sCateg" in klass.__dict__:
            descriptor = klass.__dict__["sCateg"]
            break
    assert isinstance(descriptor, property)

def test_song_has_sDate():
    assert hasattr(Song, "sDate")
    descriptor = None
    for klass in Song.__mro__:
        if "sDate" in klass.__dict__:
            descriptor = klass.__dict__["sDate"]
            break
    assert isinstance(descriptor, property)

def test_song_has_sArtist():
    assert hasattr(Song, "sArtist")
    descriptor = None
    for klass in Song.__mro__:
        if "sArtist" in klass.__dict__:
            descriptor = klass.__dict__["sArtist"]
            break
    assert isinstance(descriptor, property)

def test_song_has_sID():
    assert hasattr(Song, "sID")
    descriptor = None
    for klass in Song.__mro__:
        if "sID" in klass.__dict__:
            descriptor = klass.__dict__["sID"]
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
UseCase_UseCase_strategy = st.builds(
    UseCase_UseCase,
)
Actor_Actor_strategy = st.builds(
    Actor_Actor,
)
Repeat_Non_UseCase_strategy = st.builds(
    Repeat_Non_UseCase,
)
Shuflfe_play_UseCase_strategy = st.builds(
    Shuflfe_play_UseCase,
)
Stop_UseCase_strategy = st.builds(
    Stop_UseCase,
)
Pause_UseCase_strategy = st.builds(
    Pause_UseCase,
)
Favorite_UseCase_strategy = st.builds(
    Favorite_UseCase,
)
Search_UseCase_strategy = st.builds(
    Search_UseCase,
)
Create_playlist_UseCase_strategy = st.builds(
    Create_playlist_UseCase,
)
Play_UseCase_strategy = st.builds(
    Play_UseCase,
)
Download_UseCase_strategy = st.builds(
    Download_UseCase,
)
User_Actor_strategy = st.builds(
    User_Actor,
)
TopMostPlayed_strategy = st.builds(
    TopMostPlayed,
    sID=
        st.integers(),
    mpID=
        st.integers()
)
Recently_Played_strategy = st.builds(
    Recently_Played,
    rpID=
        st.integers(),
    sID=
        st.integers()
)
Downloads_strategy = st.builds(
    Downloads,
    sID=
        st.integers(),
    dID=
        st.integers()
)
Favourites_strategy = st.builds(
    Favourites,
    sID=
        st.integers(),
    fID=
        st.integers()
)
Playlist_Song_strategy = st.builds(
    Playlist_Song,
    pID=
        st.integers(),
    sID=
        st.integers()
)
Playlist_strategy = st.builds(
    Playlist,
    pID=
        st.integers(),
    pName=
        safe_text,
    pDate=
        safe_text
)
Song_strategy = st.builds(
    Song,
    sIMG_url=
        safe_text,
    sName=
        safe_text,
    sCateg=
        safe_text,
    sDate=
        safe_text,
    sArtist=
        safe_text,
    sID=
        st.integers()
)

@given(instance=UseCase_UseCase_strategy)
@settings(max_examples=50)
def test_usecase_usecase_instantiation(instance):
    assert isinstance(instance, UseCase_UseCase)

@given(instance=Actor_Actor_strategy)
@settings(max_examples=50)
def test_actor_actor_instantiation(instance):
    assert isinstance(instance, Actor_Actor)

@given(instance=Repeat_Non_UseCase_strategy)
@settings(max_examples=50)
def test_repeat_non_usecase_instantiation(instance):
    assert isinstance(instance, Repeat_Non_UseCase)

@given(instance=Shuflfe_play_UseCase_strategy)
@settings(max_examples=50)
def test_shuflfe_play_usecase_instantiation(instance):
    assert isinstance(instance, Shuflfe_play_UseCase)

@given(instance=Stop_UseCase_strategy)
@settings(max_examples=50)
def test_stop_usecase_instantiation(instance):
    assert isinstance(instance, Stop_UseCase)

@given(instance=Pause_UseCase_strategy)
@settings(max_examples=50)
def test_pause_usecase_instantiation(instance):
    assert isinstance(instance, Pause_UseCase)

@given(instance=Favorite_UseCase_strategy)
@settings(max_examples=50)
def test_favorite_usecase_instantiation(instance):
    assert isinstance(instance, Favorite_UseCase)

@given(instance=Search_UseCase_strategy)
@settings(max_examples=50)
def test_search_usecase_instantiation(instance):
    assert isinstance(instance, Search_UseCase)

@given(instance=Create_playlist_UseCase_strategy)
@settings(max_examples=50)
def test_create_playlist_usecase_instantiation(instance):
    assert isinstance(instance, Create_playlist_UseCase)

@given(instance=Play_UseCase_strategy)
@settings(max_examples=50)
def test_play_usecase_instantiation(instance):
    assert isinstance(instance, Play_UseCase)

@given(instance=Download_UseCase_strategy)
@settings(max_examples=50)
def test_download_usecase_instantiation(instance):
    assert isinstance(instance, Download_UseCase)

@given(instance=User_Actor_strategy)
@settings(max_examples=50)
def test_user_actor_instantiation(instance):
    assert isinstance(instance, User_Actor)

@given(instance=TopMostPlayed_strategy)
@settings(max_examples=50)
def test_topmostplayed_instantiation(instance):
    assert isinstance(instance, TopMostPlayed)



@given(instance=TopMostPlayed_strategy)
def test_topmostplayed_sID_setter(instance):
    original = instance.sID
    instance.sID = original
    assert instance.sID == original



@given(instance=TopMostPlayed_strategy)
def test_topmostplayed_mpID_setter(instance):
    original = instance.mpID
    instance.mpID = original
    assert instance.mpID == original

@given(instance=Recently_Played_strategy)
@settings(max_examples=50)
def test_recently_played_instantiation(instance):
    assert isinstance(instance, Recently_Played)



@given(instance=Recently_Played_strategy)
def test_recently_played_rpID_setter(instance):
    original = instance.rpID
    instance.rpID = original
    assert instance.rpID == original



@given(instance=Recently_Played_strategy)
def test_recently_played_sID_setter(instance):
    original = instance.sID
    instance.sID = original
    assert instance.sID == original

@given(instance=Downloads_strategy)
@settings(max_examples=50)
def test_downloads_instantiation(instance):
    assert isinstance(instance, Downloads)



@given(instance=Downloads_strategy)
def test_downloads_sID_setter(instance):
    original = instance.sID
    instance.sID = original
    assert instance.sID == original



@given(instance=Downloads_strategy)
def test_downloads_dID_setter(instance):
    original = instance.dID
    instance.dID = original
    assert instance.dID == original

@given(instance=Favourites_strategy)
@settings(max_examples=50)
def test_favourites_instantiation(instance):
    assert isinstance(instance, Favourites)



@given(instance=Favourites_strategy)
def test_favourites_sID_setter(instance):
    original = instance.sID
    instance.sID = original
    assert instance.sID == original



@given(instance=Favourites_strategy)
def test_favourites_fID_setter(instance):
    original = instance.fID
    instance.fID = original
    assert instance.fID == original

@given(instance=Playlist_Song_strategy)
@settings(max_examples=50)
def test_playlist_song_instantiation(instance):
    assert isinstance(instance, Playlist_Song)



@given(instance=Playlist_Song_strategy)
def test_playlist_song_pID_setter(instance):
    original = instance.pID
    instance.pID = original
    assert instance.pID == original



@given(instance=Playlist_Song_strategy)
def test_playlist_song_sID_setter(instance):
    original = instance.sID
    instance.sID = original
    assert instance.sID == original

@given(instance=Playlist_strategy)
@settings(max_examples=50)
def test_playlist_instantiation(instance):
    assert isinstance(instance, Playlist)



@given(instance=Playlist_strategy)
def test_playlist_pID_setter(instance):
    original = instance.pID
    instance.pID = original
    assert instance.pID == original



@given(instance=Playlist_strategy)
def test_playlist_pName_setter(instance):
    original = instance.pName
    instance.pName = original
    assert instance.pName == original



@given(instance=Playlist_strategy)
def test_playlist_pDate_setter(instance):
    original = instance.pDate
    instance.pDate = original
    assert instance.pDate == original

@given(instance=Song_strategy)
@settings(max_examples=50)
def test_song_instantiation(instance):
    assert isinstance(instance, Song)



@given(instance=Song_strategy)
def test_song_sIMG_url_setter(instance):
    original = instance.sIMG_url
    instance.sIMG_url = original
    assert instance.sIMG_url == original



@given(instance=Song_strategy)
def test_song_sName_setter(instance):
    original = instance.sName
    instance.sName = original
    assert instance.sName == original



@given(instance=Song_strategy)
def test_song_sCateg_setter(instance):
    original = instance.sCateg
    instance.sCateg = original
    assert instance.sCateg == original



@given(instance=Song_strategy)
def test_song_sDate_setter(instance):
    original = instance.sDate
    instance.sDate = original
    assert instance.sDate == original



@given(instance=Song_strategy)
def test_song_sArtist_setter(instance):
    original = instance.sArtist
    instance.sArtist = original
    assert instance.sArtist == original



@given(instance=Song_strategy)
def test_song_sID_setter(instance):
    original = instance.sID
    instance.sID = original
    assert instance.sID == original
