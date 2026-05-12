import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    DiscardPile,
    Deck,
    DealDeck,
    Column,
    ChangeOptions,
    ChangeAppearance,
    CardStack,
    Card,
    AcePile,
    ActionEvent,
    Graphics,
    WinScreen,
    SolitairePanel,
    SolitaireLayout,
    SolitaireBoard,
    SingleCell,
    FourRowSolitaire,
    FireworksDisplay,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_discardpile_is_not_abstract():
    assert not inspect.isabstract(DiscardPile)


def test_discardpile_constructor_exists():
    assert callable(DiscardPile.__init__)


def test_discardpile_constructor_args():
    sig = inspect.signature(DiscardPile.__init__)
    params = list(sig.parameters.keys())
    assert "cardsLeftFromDraw" in params, "Missing parameter 'cardsLeftFromDraw'"
    assert "drawCount" in params, "Missing parameter 'drawCount'"

def test_discardpile_has_cardsLeftFromDraw():
    assert hasattr(DiscardPile, "cardsLeftFromDraw")
    descriptor = None
    for klass in DiscardPile.__mro__:
        if "cardsLeftFromDraw" in klass.__dict__:
            descriptor = klass.__dict__["cardsLeftFromDraw"]
            break
    assert isinstance(descriptor, property)

def test_discardpile_has_drawCount():
    assert hasattr(DiscardPile, "drawCount")
    descriptor = None
    for klass in DiscardPile.__mro__:
        if "drawCount" in klass.__dict__:
            descriptor = klass.__dict__["drawCount"]
            break
    assert isinstance(descriptor, property)



def test_deck_is_not_abstract():
    assert not inspect.isabstract(Deck)


def test_deck_constructor_exists():
    assert callable(Deck.__init__)


def test_deck_constructor_args():
    sig = inspect.signature(Deck.__init__)
    params = list(sig.parameters.keys())
    assert "deckNumber" in params, "Missing parameter 'deckNumber'"

def test_deck_has_deckNumber():
    assert hasattr(Deck, "deckNumber")
    descriptor = None
    for klass in Deck.__mro__:
        if "deckNumber" in klass.__dict__:
            descriptor = klass.__dict__["deckNumber"]
            break
    assert isinstance(descriptor, property)



def test_dealdeck_is_not_abstract():
    assert not inspect.isabstract(DealDeck)


def test_dealdeck_constructor_exists():
    assert callable(DealDeck.__init__)


def test_dealdeck_constructor_args():
    sig = inspect.signature(DealDeck.__init__)
    params = list(sig.parameters.keys())
    assert "MEDIUM_THROUGH_LIMIT" in params, "Missing parameter 'MEDIUM_THROUGH_LIMIT'"
    assert "redealable" in params, "Missing parameter 'redealable'"
    assert "difficulty" in params, "Missing parameter 'difficulty'"
    assert "numTimesThroughDeck" in params, "Missing parameter 'numTimesThroughDeck'"
    assert "EASY_THROUGH_LIMIT" in params, "Missing parameter 'EASY_THROUGH_LIMIT'"
    assert "drawCount" in params, "Missing parameter 'drawCount'"
    assert "deckThroughLimit" in params, "Missing parameter 'deckThroughLimit'"
    assert "DRAW_THREE_THROUGH_LIMIT" in params, "Missing parameter 'DRAW_THREE_THROUGH_LIMIT'"
    assert "HARD_THROUGH_LIMIT" in params, "Missing parameter 'HARD_THROUGH_LIMIT'"
    assert "DRAW_ONE_THROUGH_LIMIT" in params, "Missing parameter 'DRAW_ONE_THROUGH_LIMIT'"

def test_dealdeck_has_MEDIUM_THROUGH_LIMIT():
    assert hasattr(DealDeck, "MEDIUM_THROUGH_LIMIT")
    descriptor = None
    for klass in DealDeck.__mro__:
        if "MEDIUM_THROUGH_LIMIT" in klass.__dict__:
            descriptor = klass.__dict__["MEDIUM_THROUGH_LIMIT"]
            break
    assert isinstance(descriptor, property)

def test_dealdeck_has_redealable():
    assert hasattr(DealDeck, "redealable")
    descriptor = None
    for klass in DealDeck.__mro__:
        if "redealable" in klass.__dict__:
            descriptor = klass.__dict__["redealable"]
            break
    assert isinstance(descriptor, property)

def test_dealdeck_has_difficulty():
    assert hasattr(DealDeck, "difficulty")
    descriptor = None
    for klass in DealDeck.__mro__:
        if "difficulty" in klass.__dict__:
            descriptor = klass.__dict__["difficulty"]
            break
    assert isinstance(descriptor, property)

def test_dealdeck_has_numTimesThroughDeck():
    assert hasattr(DealDeck, "numTimesThroughDeck")
    descriptor = None
    for klass in DealDeck.__mro__:
        if "numTimesThroughDeck" in klass.__dict__:
            descriptor = klass.__dict__["numTimesThroughDeck"]
            break
    assert isinstance(descriptor, property)

def test_dealdeck_has_EASY_THROUGH_LIMIT():
    assert hasattr(DealDeck, "EASY_THROUGH_LIMIT")
    descriptor = None
    for klass in DealDeck.__mro__:
        if "EASY_THROUGH_LIMIT" in klass.__dict__:
            descriptor = klass.__dict__["EASY_THROUGH_LIMIT"]
            break
    assert isinstance(descriptor, property)

def test_dealdeck_has_drawCount():
    assert hasattr(DealDeck, "drawCount")
    descriptor = None
    for klass in DealDeck.__mro__:
        if "drawCount" in klass.__dict__:
            descriptor = klass.__dict__["drawCount"]
            break
    assert isinstance(descriptor, property)

def test_dealdeck_has_deckThroughLimit():
    assert hasattr(DealDeck, "deckThroughLimit")
    descriptor = None
    for klass in DealDeck.__mro__:
        if "deckThroughLimit" in klass.__dict__:
            descriptor = klass.__dict__["deckThroughLimit"]
            break
    assert isinstance(descriptor, property)

def test_dealdeck_has_DRAW_THREE_THROUGH_LIMIT():
    assert hasattr(DealDeck, "DRAW_THREE_THROUGH_LIMIT")
    descriptor = None
    for klass in DealDeck.__mro__:
        if "DRAW_THREE_THROUGH_LIMIT" in klass.__dict__:
            descriptor = klass.__dict__["DRAW_THREE_THROUGH_LIMIT"]
            break
    assert isinstance(descriptor, property)

def test_dealdeck_has_HARD_THROUGH_LIMIT():
    assert hasattr(DealDeck, "HARD_THROUGH_LIMIT")
    descriptor = None
    for klass in DealDeck.__mro__:
        if "HARD_THROUGH_LIMIT" in klass.__dict__:
            descriptor = klass.__dict__["HARD_THROUGH_LIMIT"]
            break
    assert isinstance(descriptor, property)

def test_dealdeck_has_DRAW_ONE_THROUGH_LIMIT():
    assert hasattr(DealDeck, "DRAW_ONE_THROUGH_LIMIT")
    descriptor = None
    for klass in DealDeck.__mro__:
        if "DRAW_ONE_THROUGH_LIMIT" in klass.__dict__:
            descriptor = klass.__dict__["DRAW_ONE_THROUGH_LIMIT"]
            break
    assert isinstance(descriptor, property)



def test_column_is_not_abstract():
    assert not inspect.isabstract(Column)


def test_column_constructor_exists():
    assert callable(Column.__init__)


def test_column_constructor_args():
    sig = inspect.signature(Column.__init__)
    params = list(sig.parameters.keys())



def test_changeoptions_is_not_abstract():
    assert not inspect.isabstract(ChangeOptions)


def test_changeoptions_constructor_exists():
    assert callable(ChangeOptions.__init__)


def test_changeoptions_constructor_args():
    sig = inspect.signature(ChangeOptions.__init__)
    params = list(sig.parameters.keys())
    assert "winSoundsCheck" in params, "Missing parameter 'winSoundsCheck'"
    assert "winAnimationCheck" in params, "Missing parameter 'winAnimationCheck'"
    assert "ok" in params, "Missing parameter 'ok'"
    assert "drawOne" in params, "Missing parameter 'drawOne'"
    assert "medium" in params, "Missing parameter 'medium'"
    assert "easy" in params, "Missing parameter 'easy'"
    assert "drawCount" in params, "Missing parameter 'drawCount'"
    assert "animation" in params, "Missing parameter 'animation'"
    assert "hard" in params, "Missing parameter 'hard'"
    assert "difficulty" in params, "Missing parameter 'difficulty'"
    assert "timerCheck" in params, "Missing parameter 'timerCheck'"
    assert "timer" in params, "Missing parameter 'timer'"
    assert "drawThree" in params, "Missing parameter 'drawThree'"
    assert "sounds" in params, "Missing parameter 'sounds'"
    assert "exited" in params, "Missing parameter 'exited'"

def test_changeoptions_has_winSoundsCheck():
    assert hasattr(ChangeOptions, "winSoundsCheck")
    descriptor = None
    for klass in ChangeOptions.__mro__:
        if "winSoundsCheck" in klass.__dict__:
            descriptor = klass.__dict__["winSoundsCheck"]
            break
    assert isinstance(descriptor, property)

def test_changeoptions_has_winAnimationCheck():
    assert hasattr(ChangeOptions, "winAnimationCheck")
    descriptor = None
    for klass in ChangeOptions.__mro__:
        if "winAnimationCheck" in klass.__dict__:
            descriptor = klass.__dict__["winAnimationCheck"]
            break
    assert isinstance(descriptor, property)

def test_changeoptions_has_ok():
    assert hasattr(ChangeOptions, "ok")
    descriptor = None
    for klass in ChangeOptions.__mro__:
        if "ok" in klass.__dict__:
            descriptor = klass.__dict__["ok"]
            break
    assert isinstance(descriptor, property)

def test_changeoptions_has_drawOne():
    assert hasattr(ChangeOptions, "drawOne")
    descriptor = None
    for klass in ChangeOptions.__mro__:
        if "drawOne" in klass.__dict__:
            descriptor = klass.__dict__["drawOne"]
            break
    assert isinstance(descriptor, property)

def test_changeoptions_has_medium():
    assert hasattr(ChangeOptions, "medium")
    descriptor = None
    for klass in ChangeOptions.__mro__:
        if "medium" in klass.__dict__:
            descriptor = klass.__dict__["medium"]
            break
    assert isinstance(descriptor, property)

def test_changeoptions_has_easy():
    assert hasattr(ChangeOptions, "easy")
    descriptor = None
    for klass in ChangeOptions.__mro__:
        if "easy" in klass.__dict__:
            descriptor = klass.__dict__["easy"]
            break
    assert isinstance(descriptor, property)

def test_changeoptions_has_drawCount():
    assert hasattr(ChangeOptions, "drawCount")
    descriptor = None
    for klass in ChangeOptions.__mro__:
        if "drawCount" in klass.__dict__:
            descriptor = klass.__dict__["drawCount"]
            break
    assert isinstance(descriptor, property)

def test_changeoptions_has_animation():
    assert hasattr(ChangeOptions, "animation")
    descriptor = None
    for klass in ChangeOptions.__mro__:
        if "animation" in klass.__dict__:
            descriptor = klass.__dict__["animation"]
            break
    assert isinstance(descriptor, property)

def test_changeoptions_has_hard():
    assert hasattr(ChangeOptions, "hard")
    descriptor = None
    for klass in ChangeOptions.__mro__:
        if "hard" in klass.__dict__:
            descriptor = klass.__dict__["hard"]
            break
    assert isinstance(descriptor, property)

def test_changeoptions_has_difficulty():
    assert hasattr(ChangeOptions, "difficulty")
    descriptor = None
    for klass in ChangeOptions.__mro__:
        if "difficulty" in klass.__dict__:
            descriptor = klass.__dict__["difficulty"]
            break
    assert isinstance(descriptor, property)

def test_changeoptions_has_timerCheck():
    assert hasattr(ChangeOptions, "timerCheck")
    descriptor = None
    for klass in ChangeOptions.__mro__:
        if "timerCheck" in klass.__dict__:
            descriptor = klass.__dict__["timerCheck"]
            break
    assert isinstance(descriptor, property)

def test_changeoptions_has_timer():
    assert hasattr(ChangeOptions, "timer")
    descriptor = None
    for klass in ChangeOptions.__mro__:
        if "timer" in klass.__dict__:
            descriptor = klass.__dict__["timer"]
            break
    assert isinstance(descriptor, property)

def test_changeoptions_has_drawThree():
    assert hasattr(ChangeOptions, "drawThree")
    descriptor = None
    for klass in ChangeOptions.__mro__:
        if "drawThree" in klass.__dict__:
            descriptor = klass.__dict__["drawThree"]
            break
    assert isinstance(descriptor, property)

def test_changeoptions_has_sounds():
    assert hasattr(ChangeOptions, "sounds")
    descriptor = None
    for klass in ChangeOptions.__mro__:
        if "sounds" in klass.__dict__:
            descriptor = klass.__dict__["sounds"]
            break
    assert isinstance(descriptor, property)

def test_changeoptions_has_exited():
    assert hasattr(ChangeOptions, "exited")
    descriptor = None
    for klass in ChangeOptions.__mro__:
        if "exited" in klass.__dict__:
            descriptor = klass.__dict__["exited"]
            break
    assert isinstance(descriptor, property)



def test_changeappearance_is_not_abstract():
    assert not inspect.isabstract(ChangeAppearance)


def test_changeappearance_constructor_exists():
    assert callable(ChangeAppearance.__init__)


def test_changeappearance_constructor_args():
    sig = inspect.signature(ChangeAppearance.__init__)
    params = list(sig.parameters.keys())
    assert "backgrounds" in params, "Missing parameter 'backgrounds'"
    assert "exited" in params, "Missing parameter 'exited'"
    assert "backgroundNumber" in params, "Missing parameter 'backgroundNumber'"
    assert "ok" in params, "Missing parameter 'ok'"
    assert "FRS_BACKGROUND" in params, "Missing parameter 'FRS_BACKGROUND'"
    assert "deckNumber" in params, "Missing parameter 'deckNumber'"
    assert "decks" in params, "Missing parameter 'decks'"
    assert "cardBackLabel" in params, "Missing parameter 'cardBackLabel'"
    assert "backgroundLabel" in params, "Missing parameter 'backgroundLabel'"
    assert "FRS_DECK" in params, "Missing parameter 'FRS_DECK'"
    assert "NUM_BACKGROUNDS" in params, "Missing parameter 'NUM_BACKGROUNDS'"
    assert "NUM_DECKS" in params, "Missing parameter 'NUM_DECKS'"

def test_changeappearance_has_backgrounds():
    assert hasattr(ChangeAppearance, "backgrounds")
    descriptor = None
    for klass in ChangeAppearance.__mro__:
        if "backgrounds" in klass.__dict__:
            descriptor = klass.__dict__["backgrounds"]
            break
    assert isinstance(descriptor, property)

def test_changeappearance_has_exited():
    assert hasattr(ChangeAppearance, "exited")
    descriptor = None
    for klass in ChangeAppearance.__mro__:
        if "exited" in klass.__dict__:
            descriptor = klass.__dict__["exited"]
            break
    assert isinstance(descriptor, property)

def test_changeappearance_has_backgroundNumber():
    assert hasattr(ChangeAppearance, "backgroundNumber")
    descriptor = None
    for klass in ChangeAppearance.__mro__:
        if "backgroundNumber" in klass.__dict__:
            descriptor = klass.__dict__["backgroundNumber"]
            break
    assert isinstance(descriptor, property)

def test_changeappearance_has_ok():
    assert hasattr(ChangeAppearance, "ok")
    descriptor = None
    for klass in ChangeAppearance.__mro__:
        if "ok" in klass.__dict__:
            descriptor = klass.__dict__["ok"]
            break
    assert isinstance(descriptor, property)

def test_changeappearance_has_FRS_BACKGROUND():
    assert hasattr(ChangeAppearance, "FRS_BACKGROUND")
    descriptor = None
    for klass in ChangeAppearance.__mro__:
        if "FRS_BACKGROUND" in klass.__dict__:
            descriptor = klass.__dict__["FRS_BACKGROUND"]
            break
    assert isinstance(descriptor, property)

def test_changeappearance_has_deckNumber():
    assert hasattr(ChangeAppearance, "deckNumber")
    descriptor = None
    for klass in ChangeAppearance.__mro__:
        if "deckNumber" in klass.__dict__:
            descriptor = klass.__dict__["deckNumber"]
            break
    assert isinstance(descriptor, property)

def test_changeappearance_has_decks():
    assert hasattr(ChangeAppearance, "decks")
    descriptor = None
    for klass in ChangeAppearance.__mro__:
        if "decks" in klass.__dict__:
            descriptor = klass.__dict__["decks"]
            break
    assert isinstance(descriptor, property)

def test_changeappearance_has_cardBackLabel():
    assert hasattr(ChangeAppearance, "cardBackLabel")
    descriptor = None
    for klass in ChangeAppearance.__mro__:
        if "cardBackLabel" in klass.__dict__:
            descriptor = klass.__dict__["cardBackLabel"]
            break
    assert isinstance(descriptor, property)

def test_changeappearance_has_backgroundLabel():
    assert hasattr(ChangeAppearance, "backgroundLabel")
    descriptor = None
    for klass in ChangeAppearance.__mro__:
        if "backgroundLabel" in klass.__dict__:
            descriptor = klass.__dict__["backgroundLabel"]
            break
    assert isinstance(descriptor, property)

def test_changeappearance_has_FRS_DECK():
    assert hasattr(ChangeAppearance, "FRS_DECK")
    descriptor = None
    for klass in ChangeAppearance.__mro__:
        if "FRS_DECK" in klass.__dict__:
            descriptor = klass.__dict__["FRS_DECK"]
            break
    assert isinstance(descriptor, property)

def test_changeappearance_has_NUM_BACKGROUNDS():
    assert hasattr(ChangeAppearance, "NUM_BACKGROUNDS")
    descriptor = None
    for klass in ChangeAppearance.__mro__:
        if "NUM_BACKGROUNDS" in klass.__dict__:
            descriptor = klass.__dict__["NUM_BACKGROUNDS"]
            break
    assert isinstance(descriptor, property)

def test_changeappearance_has_NUM_DECKS():
    assert hasattr(ChangeAppearance, "NUM_DECKS")
    descriptor = None
    for klass in ChangeAppearance.__mro__:
        if "NUM_DECKS" in klass.__dict__:
            descriptor = klass.__dict__["NUM_DECKS"]
            break
    assert isinstance(descriptor, property)



def test_cardstack_is_not_abstract():
    assert not inspect.isabstract(CardStack)


def test_cardstack_constructor_exists():
    assert callable(CardStack.__init__)


def test_cardstack_constructor_args():
    sig = inspect.signature(CardStack.__init__)
    params = list(sig.parameters.keys())



def test_card_is_not_abstract():
    assert not inspect.isabstract(Card)


def test_card_constructor_exists():
    assert callable(Card.__init__)


def test_card_constructor_args():
    sig = inspect.signature(Card.__init__)
    params = list(sig.parameters.keys())
    assert "SIX" in params, "Missing parameter 'SIX'"
    assert "HEARTS_SUIT" in params, "Missing parameter 'HEARTS_SUIT'"
    assert "CLUBS_SUIT" in params, "Missing parameter 'CLUBS_SUIT'"
    assert "NINE" in params, "Missing parameter 'NINE'"
    assert "TEN" in params, "Missing parameter 'TEN'"
    assert "image" in params, "Missing parameter 'image'"
    assert "QUEEN" in params, "Missing parameter 'QUEEN'"
    assert "fullCardNumber" in params, "Missing parameter 'fullCardNumber'"
    assert "faceUp" in params, "Missing parameter 'faceUp'"
    assert "highlighted" in params, "Missing parameter 'highlighted'"
    assert "DIAMONDS_SUIT" in params, "Missing parameter 'DIAMONDS_SUIT'"
    assert "INVALID_SUIT" in params, "Missing parameter 'INVALID_SUIT'"
    assert "FOUR" in params, "Missing parameter 'FOUR'"
    assert "cardImageString" in params, "Missing parameter 'cardImageString'"
    assert "cardHighlighted" in params, "Missing parameter 'cardHighlighted'"
    assert "INVALID_NUMBER" in params, "Missing parameter 'INVALID_NUMBER'"
    assert "ACE" in params, "Missing parameter 'ACE'"
    assert "SPADES_SUIT" in params, "Missing parameter 'SPADES_SUIT'"
    assert "TWO" in params, "Missing parameter 'TWO'"
    assert "cardSuit" in params, "Missing parameter 'cardSuit'"
    assert "cardColor" in params, "Missing parameter 'cardColor'"
    assert "cardNumber" in params, "Missing parameter 'cardNumber'"
    assert "cardBack" in params, "Missing parameter 'cardBack'"
    assert "THREE" in params, "Missing parameter 'THREE'"
    assert "EIGHT" in params, "Missing parameter 'EIGHT'"
    assert "location" in params, "Missing parameter 'location'"
    assert "deckNumber" in params, "Missing parameter 'deckNumber'"
    assert "KING" in params, "Missing parameter 'KING'"
    assert "FIVE" in params, "Missing parameter 'FIVE'"
    assert "SEVEN" in params, "Missing parameter 'SEVEN'"
    assert "JACK" in params, "Missing parameter 'JACK'"

def test_card_has_SIX():
    assert hasattr(Card, "SIX")
    descriptor = None
    for klass in Card.__mro__:
        if "SIX" in klass.__dict__:
            descriptor = klass.__dict__["SIX"]
            break
    assert isinstance(descriptor, property)

def test_card_has_HEARTS_SUIT():
    assert hasattr(Card, "HEARTS_SUIT")
    descriptor = None
    for klass in Card.__mro__:
        if "HEARTS_SUIT" in klass.__dict__:
            descriptor = klass.__dict__["HEARTS_SUIT"]
            break
    assert isinstance(descriptor, property)

def test_card_has_CLUBS_SUIT():
    assert hasattr(Card, "CLUBS_SUIT")
    descriptor = None
    for klass in Card.__mro__:
        if "CLUBS_SUIT" in klass.__dict__:
            descriptor = klass.__dict__["CLUBS_SUIT"]
            break
    assert isinstance(descriptor, property)

def test_card_has_NINE():
    assert hasattr(Card, "NINE")
    descriptor = None
    for klass in Card.__mro__:
        if "NINE" in klass.__dict__:
            descriptor = klass.__dict__["NINE"]
            break
    assert isinstance(descriptor, property)

def test_card_has_TEN():
    assert hasattr(Card, "TEN")
    descriptor = None
    for klass in Card.__mro__:
        if "TEN" in klass.__dict__:
            descriptor = klass.__dict__["TEN"]
            break
    assert isinstance(descriptor, property)

def test_card_has_image():
    assert hasattr(Card, "image")
    descriptor = None
    for klass in Card.__mro__:
        if "image" in klass.__dict__:
            descriptor = klass.__dict__["image"]
            break
    assert isinstance(descriptor, property)

def test_card_has_QUEEN():
    assert hasattr(Card, "QUEEN")
    descriptor = None
    for klass in Card.__mro__:
        if "QUEEN" in klass.__dict__:
            descriptor = klass.__dict__["QUEEN"]
            break
    assert isinstance(descriptor, property)

def test_card_has_fullCardNumber():
    assert hasattr(Card, "fullCardNumber")
    descriptor = None
    for klass in Card.__mro__:
        if "fullCardNumber" in klass.__dict__:
            descriptor = klass.__dict__["fullCardNumber"]
            break
    assert isinstance(descriptor, property)

def test_card_has_faceUp():
    assert hasattr(Card, "faceUp")
    descriptor = None
    for klass in Card.__mro__:
        if "faceUp" in klass.__dict__:
            descriptor = klass.__dict__["faceUp"]
            break
    assert isinstance(descriptor, property)

def test_card_has_highlighted():
    assert hasattr(Card, "highlighted")
    descriptor = None
    for klass in Card.__mro__:
        if "highlighted" in klass.__dict__:
            descriptor = klass.__dict__["highlighted"]
            break
    assert isinstance(descriptor, property)

def test_card_has_DIAMONDS_SUIT():
    assert hasattr(Card, "DIAMONDS_SUIT")
    descriptor = None
    for klass in Card.__mro__:
        if "DIAMONDS_SUIT" in klass.__dict__:
            descriptor = klass.__dict__["DIAMONDS_SUIT"]
            break
    assert isinstance(descriptor, property)

def test_card_has_INVALID_SUIT():
    assert hasattr(Card, "INVALID_SUIT")
    descriptor = None
    for klass in Card.__mro__:
        if "INVALID_SUIT" in klass.__dict__:
            descriptor = klass.__dict__["INVALID_SUIT"]
            break
    assert isinstance(descriptor, property)

def test_card_has_FOUR():
    assert hasattr(Card, "FOUR")
    descriptor = None
    for klass in Card.__mro__:
        if "FOUR" in klass.__dict__:
            descriptor = klass.__dict__["FOUR"]
            break
    assert isinstance(descriptor, property)

def test_card_has_cardImageString():
    assert hasattr(Card, "cardImageString")
    descriptor = None
    for klass in Card.__mro__:
        if "cardImageString" in klass.__dict__:
            descriptor = klass.__dict__["cardImageString"]
            break
    assert isinstance(descriptor, property)

def test_card_has_cardHighlighted():
    assert hasattr(Card, "cardHighlighted")
    descriptor = None
    for klass in Card.__mro__:
        if "cardHighlighted" in klass.__dict__:
            descriptor = klass.__dict__["cardHighlighted"]
            break
    assert isinstance(descriptor, property)

def test_card_has_INVALID_NUMBER():
    assert hasattr(Card, "INVALID_NUMBER")
    descriptor = None
    for klass in Card.__mro__:
        if "INVALID_NUMBER" in klass.__dict__:
            descriptor = klass.__dict__["INVALID_NUMBER"]
            break
    assert isinstance(descriptor, property)

def test_card_has_ACE():
    assert hasattr(Card, "ACE")
    descriptor = None
    for klass in Card.__mro__:
        if "ACE" in klass.__dict__:
            descriptor = klass.__dict__["ACE"]
            break
    assert isinstance(descriptor, property)

def test_card_has_SPADES_SUIT():
    assert hasattr(Card, "SPADES_SUIT")
    descriptor = None
    for klass in Card.__mro__:
        if "SPADES_SUIT" in klass.__dict__:
            descriptor = klass.__dict__["SPADES_SUIT"]
            break
    assert isinstance(descriptor, property)

def test_card_has_TWO():
    assert hasattr(Card, "TWO")
    descriptor = None
    for klass in Card.__mro__:
        if "TWO" in klass.__dict__:
            descriptor = klass.__dict__["TWO"]
            break
    assert isinstance(descriptor, property)

def test_card_has_cardSuit():
    assert hasattr(Card, "cardSuit")
    descriptor = None
    for klass in Card.__mro__:
        if "cardSuit" in klass.__dict__:
            descriptor = klass.__dict__["cardSuit"]
            break
    assert isinstance(descriptor, property)

def test_card_has_cardColor():
    assert hasattr(Card, "cardColor")
    descriptor = None
    for klass in Card.__mro__:
        if "cardColor" in klass.__dict__:
            descriptor = klass.__dict__["cardColor"]
            break
    assert isinstance(descriptor, property)

def test_card_has_cardNumber():
    assert hasattr(Card, "cardNumber")
    descriptor = None
    for klass in Card.__mro__:
        if "cardNumber" in klass.__dict__:
            descriptor = klass.__dict__["cardNumber"]
            break
    assert isinstance(descriptor, property)

def test_card_has_cardBack():
    assert hasattr(Card, "cardBack")
    descriptor = None
    for klass in Card.__mro__:
        if "cardBack" in klass.__dict__:
            descriptor = klass.__dict__["cardBack"]
            break
    assert isinstance(descriptor, property)

def test_card_has_THREE():
    assert hasattr(Card, "THREE")
    descriptor = None
    for klass in Card.__mro__:
        if "THREE" in klass.__dict__:
            descriptor = klass.__dict__["THREE"]
            break
    assert isinstance(descriptor, property)

def test_card_has_EIGHT():
    assert hasattr(Card, "EIGHT")
    descriptor = None
    for klass in Card.__mro__:
        if "EIGHT" in klass.__dict__:
            descriptor = klass.__dict__["EIGHT"]
            break
    assert isinstance(descriptor, property)

def test_card_has_location():
    assert hasattr(Card, "location")
    descriptor = None
    for klass in Card.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)

def test_card_has_deckNumber():
    assert hasattr(Card, "deckNumber")
    descriptor = None
    for klass in Card.__mro__:
        if "deckNumber" in klass.__dict__:
            descriptor = klass.__dict__["deckNumber"]
            break
    assert isinstance(descriptor, property)

def test_card_has_KING():
    assert hasattr(Card, "KING")
    descriptor = None
    for klass in Card.__mro__:
        if "KING" in klass.__dict__:
            descriptor = klass.__dict__["KING"]
            break
    assert isinstance(descriptor, property)

def test_card_has_FIVE():
    assert hasattr(Card, "FIVE")
    descriptor = None
    for klass in Card.__mro__:
        if "FIVE" in klass.__dict__:
            descriptor = klass.__dict__["FIVE"]
            break
    assert isinstance(descriptor, property)

def test_card_has_SEVEN():
    assert hasattr(Card, "SEVEN")
    descriptor = None
    for klass in Card.__mro__:
        if "SEVEN" in klass.__dict__:
            descriptor = klass.__dict__["SEVEN"]
            break
    assert isinstance(descriptor, property)

def test_card_has_JACK():
    assert hasattr(Card, "JACK")
    descriptor = None
    for klass in Card.__mro__:
        if "JACK" in klass.__dict__:
            descriptor = klass.__dict__["JACK"]
            break
    assert isinstance(descriptor, property)



def test_acepile_is_not_abstract():
    assert not inspect.isabstract(AcePile)


def test_acepile_constructor_exists():
    assert callable(AcePile.__init__)


def test_acepile_constructor_args():
    sig = inspect.signature(AcePile.__init__)
    params = list(sig.parameters.keys())
    assert "suit" in params, "Missing parameter 'suit'"

def test_acepile_has_suit():
    assert hasattr(AcePile, "suit")
    descriptor = None
    for klass in AcePile.__mro__:
        if "suit" in klass.__dict__:
            descriptor = klass.__dict__["suit"]
            break
    assert isinstance(descriptor, property)



def test_actionevent_is_not_abstract():
    assert not inspect.isabstract(ActionEvent)


def test_actionevent_constructor_exists():
    assert callable(ActionEvent.__init__)


def test_actionevent_constructor_args():
    sig = inspect.signature(ActionEvent.__init__)
    params = list(sig.parameters.keys())



def test_graphics_is_not_abstract():
    assert not inspect.isabstract(Graphics)


def test_graphics_constructor_exists():
    assert callable(Graphics.__init__)


def test_graphics_constructor_args():
    sig = inspect.signature(Graphics.__init__)
    params = list(sig.parameters.keys())



def test_winscreen_is_not_abstract():
    assert not inspect.isabstract(WinScreen)


def test_winscreen_constructor_exists():
    assert callable(WinScreen.__init__)


def test_winscreen_constructor_args():
    sig = inspect.signature(WinScreen.__init__)
    params = list(sig.parameters.keys())



def test_solitairepanel_is_not_abstract():
    assert not inspect.isabstract(SolitairePanel)


def test_solitairepanel_constructor_exists():
    assert callable(SolitairePanel.__init__)


def test_solitairepanel_constructor_args():
    sig = inspect.signature(SolitairePanel.__init__)
    params = list(sig.parameters.keys())
    assert "background" in params, "Missing parameter 'background'"
    assert "backgroundNumber" in params, "Missing parameter 'backgroundNumber'"

def test_solitairepanel_has_background():
    assert hasattr(SolitairePanel, "background")
    descriptor = None
    for klass in SolitairePanel.__mro__:
        if "background" in klass.__dict__:
            descriptor = klass.__dict__["background"]
            break
    assert isinstance(descriptor, property)

def test_solitairepanel_has_backgroundNumber():
    assert hasattr(SolitairePanel, "backgroundNumber")
    descriptor = None
    for klass in SolitairePanel.__mro__:
        if "backgroundNumber" in klass.__dict__:
            descriptor = klass.__dict__["backgroundNumber"]
            break
    assert isinstance(descriptor, property)



def test_solitairelayout_is_not_abstract():
    assert not inspect.isabstract(SolitaireLayout)


def test_solitairelayout_constructor_exists():
    assert callable(SolitaireLayout.__init__)


def test_solitairelayout_constructor_args():
    sig = inspect.signature(SolitaireLayout.__init__)
    params = list(sig.parameters.keys())
    assert "COLUMN_TWO" in params, "Missing parameter 'COLUMN_TWO'"
    assert "COLUMN_THREE" in params, "Missing parameter 'COLUMN_THREE'"
    assert "CELL_THREE" in params, "Missing parameter 'CELL_THREE'"
    assert "colTwo" in params, "Missing parameter 'colTwo'"
    assert "colOne" in params, "Missing parameter 'colOne'"
    assert "aceClubs" in params, "Missing parameter 'aceClubs'"
    assert "COLUMEN_ONE" in params, "Missing parameter 'COLUMEN_ONE'"
    assert "aceHearts" in params, "Missing parameter 'aceHearts'"
    assert "cellThree" in params, "Missing parameter 'cellThree'"
    assert "cellOne" in params, "Missing parameter 'cellOne'"
    assert "HEARTS_ACE_PILE" in params, "Missing parameter 'HEARTS_ACE_PILE'"
    assert "DIAMONDS_ACE_PILE" in params, "Missing parameter 'DIAMONDS_ACE_PILE'"
    assert "CELL_ONE" in params, "Missing parameter 'CELL_ONE'"
    assert "cellFour" in params, "Missing parameter 'cellFour'"
    assert "DECK" in params, "Missing parameter 'DECK'"
    assert "colFour" in params, "Missing parameter 'colFour'"
    assert "CELL_FOUR" in params, "Missing parameter 'CELL_FOUR'"
    assert "discardPile" in params, "Missing parameter 'discardPile'"
    assert "COLUMN_FOUR" in params, "Missing parameter 'COLUMN_FOUR'"
    assert "deck" in params, "Missing parameter 'deck'"
    assert "CLUBS_ACE_PILE" in params, "Missing parameter 'CLUBS_ACE_PILE'"
    assert "colThree" in params, "Missing parameter 'colThree'"
    assert "DISCARD_PILE" in params, "Missing parameter 'DISCARD_PILE'"
    assert "aceSpades" in params, "Missing parameter 'aceSpades'"
    assert "CELL_TWO" in params, "Missing parameter 'CELL_TWO'"
    assert "aceDiamonds" in params, "Missing parameter 'aceDiamonds'"
    assert "cellTwo" in params, "Missing parameter 'cellTwo'"
    assert "SPADES_ACE_PILE" in params, "Missing parameter 'SPADES_ACE_PILE'"

def test_solitairelayout_has_COLUMN_TWO():
    assert hasattr(SolitaireLayout, "COLUMN_TWO")
    descriptor = None
    for klass in SolitaireLayout.__mro__:
        if "COLUMN_TWO" in klass.__dict__:
            descriptor = klass.__dict__["COLUMN_TWO"]
            break
    assert isinstance(descriptor, property)

def test_solitairelayout_has_COLUMN_THREE():
    assert hasattr(SolitaireLayout, "COLUMN_THREE")
    descriptor = None
    for klass in SolitaireLayout.__mro__:
        if "COLUMN_THREE" in klass.__dict__:
            descriptor = klass.__dict__["COLUMN_THREE"]
            break
    assert isinstance(descriptor, property)

def test_solitairelayout_has_CELL_THREE():
    assert hasattr(SolitaireLayout, "CELL_THREE")
    descriptor = None
    for klass in SolitaireLayout.__mro__:
        if "CELL_THREE" in klass.__dict__:
            descriptor = klass.__dict__["CELL_THREE"]
            break
    assert isinstance(descriptor, property)

def test_solitairelayout_has_colTwo():
    assert hasattr(SolitaireLayout, "colTwo")
    descriptor = None
    for klass in SolitaireLayout.__mro__:
        if "colTwo" in klass.__dict__:
            descriptor = klass.__dict__["colTwo"]
            break
    assert isinstance(descriptor, property)

def test_solitairelayout_has_colOne():
    assert hasattr(SolitaireLayout, "colOne")
    descriptor = None
    for klass in SolitaireLayout.__mro__:
        if "colOne" in klass.__dict__:
            descriptor = klass.__dict__["colOne"]
            break
    assert isinstance(descriptor, property)

def test_solitairelayout_has_aceClubs():
    assert hasattr(SolitaireLayout, "aceClubs")
    descriptor = None
    for klass in SolitaireLayout.__mro__:
        if "aceClubs" in klass.__dict__:
            descriptor = klass.__dict__["aceClubs"]
            break
    assert isinstance(descriptor, property)

def test_solitairelayout_has_COLUMEN_ONE():
    assert hasattr(SolitaireLayout, "COLUMEN_ONE")
    descriptor = None
    for klass in SolitaireLayout.__mro__:
        if "COLUMEN_ONE" in klass.__dict__:
            descriptor = klass.__dict__["COLUMEN_ONE"]
            break
    assert isinstance(descriptor, property)

def test_solitairelayout_has_aceHearts():
    assert hasattr(SolitaireLayout, "aceHearts")
    descriptor = None
    for klass in SolitaireLayout.__mro__:
        if "aceHearts" in klass.__dict__:
            descriptor = klass.__dict__["aceHearts"]
            break
    assert isinstance(descriptor, property)

def test_solitairelayout_has_cellThree():
    assert hasattr(SolitaireLayout, "cellThree")
    descriptor = None
    for klass in SolitaireLayout.__mro__:
        if "cellThree" in klass.__dict__:
            descriptor = klass.__dict__["cellThree"]
            break
    assert isinstance(descriptor, property)

def test_solitairelayout_has_cellOne():
    assert hasattr(SolitaireLayout, "cellOne")
    descriptor = None
    for klass in SolitaireLayout.__mro__:
        if "cellOne" in klass.__dict__:
            descriptor = klass.__dict__["cellOne"]
            break
    assert isinstance(descriptor, property)

def test_solitairelayout_has_HEARTS_ACE_PILE():
    assert hasattr(SolitaireLayout, "HEARTS_ACE_PILE")
    descriptor = None
    for klass in SolitaireLayout.__mro__:
        if "HEARTS_ACE_PILE" in klass.__dict__:
            descriptor = klass.__dict__["HEARTS_ACE_PILE"]
            break
    assert isinstance(descriptor, property)

def test_solitairelayout_has_DIAMONDS_ACE_PILE():
    assert hasattr(SolitaireLayout, "DIAMONDS_ACE_PILE")
    descriptor = None
    for klass in SolitaireLayout.__mro__:
        if "DIAMONDS_ACE_PILE" in klass.__dict__:
            descriptor = klass.__dict__["DIAMONDS_ACE_PILE"]
            break
    assert isinstance(descriptor, property)

def test_solitairelayout_has_CELL_ONE():
    assert hasattr(SolitaireLayout, "CELL_ONE")
    descriptor = None
    for klass in SolitaireLayout.__mro__:
        if "CELL_ONE" in klass.__dict__:
            descriptor = klass.__dict__["CELL_ONE"]
            break
    assert isinstance(descriptor, property)

def test_solitairelayout_has_cellFour():
    assert hasattr(SolitaireLayout, "cellFour")
    descriptor = None
    for klass in SolitaireLayout.__mro__:
        if "cellFour" in klass.__dict__:
            descriptor = klass.__dict__["cellFour"]
            break
    assert isinstance(descriptor, property)

def test_solitairelayout_has_DECK():
    assert hasattr(SolitaireLayout, "DECK")
    descriptor = None
    for klass in SolitaireLayout.__mro__:
        if "DECK" in klass.__dict__:
            descriptor = klass.__dict__["DECK"]
            break
    assert isinstance(descriptor, property)

def test_solitairelayout_has_colFour():
    assert hasattr(SolitaireLayout, "colFour")
    descriptor = None
    for klass in SolitaireLayout.__mro__:
        if "colFour" in klass.__dict__:
            descriptor = klass.__dict__["colFour"]
            break
    assert isinstance(descriptor, property)

def test_solitairelayout_has_CELL_FOUR():
    assert hasattr(SolitaireLayout, "CELL_FOUR")
    descriptor = None
    for klass in SolitaireLayout.__mro__:
        if "CELL_FOUR" in klass.__dict__:
            descriptor = klass.__dict__["CELL_FOUR"]
            break
    assert isinstance(descriptor, property)

def test_solitairelayout_has_discardPile():
    assert hasattr(SolitaireLayout, "discardPile")
    descriptor = None
    for klass in SolitaireLayout.__mro__:
        if "discardPile" in klass.__dict__:
            descriptor = klass.__dict__["discardPile"]
            break
    assert isinstance(descriptor, property)

def test_solitairelayout_has_COLUMN_FOUR():
    assert hasattr(SolitaireLayout, "COLUMN_FOUR")
    descriptor = None
    for klass in SolitaireLayout.__mro__:
        if "COLUMN_FOUR" in klass.__dict__:
            descriptor = klass.__dict__["COLUMN_FOUR"]
            break
    assert isinstance(descriptor, property)

def test_solitairelayout_has_deck():
    assert hasattr(SolitaireLayout, "deck")
    descriptor = None
    for klass in SolitaireLayout.__mro__:
        if "deck" in klass.__dict__:
            descriptor = klass.__dict__["deck"]
            break
    assert isinstance(descriptor, property)

def test_solitairelayout_has_CLUBS_ACE_PILE():
    assert hasattr(SolitaireLayout, "CLUBS_ACE_PILE")
    descriptor = None
    for klass in SolitaireLayout.__mro__:
        if "CLUBS_ACE_PILE" in klass.__dict__:
            descriptor = klass.__dict__["CLUBS_ACE_PILE"]
            break
    assert isinstance(descriptor, property)

def test_solitairelayout_has_colThree():
    assert hasattr(SolitaireLayout, "colThree")
    descriptor = None
    for klass in SolitaireLayout.__mro__:
        if "colThree" in klass.__dict__:
            descriptor = klass.__dict__["colThree"]
            break
    assert isinstance(descriptor, property)

def test_solitairelayout_has_DISCARD_PILE():
    assert hasattr(SolitaireLayout, "DISCARD_PILE")
    descriptor = None
    for klass in SolitaireLayout.__mro__:
        if "DISCARD_PILE" in klass.__dict__:
            descriptor = klass.__dict__["DISCARD_PILE"]
            break
    assert isinstance(descriptor, property)

def test_solitairelayout_has_aceSpades():
    assert hasattr(SolitaireLayout, "aceSpades")
    descriptor = None
    for klass in SolitaireLayout.__mro__:
        if "aceSpades" in klass.__dict__:
            descriptor = klass.__dict__["aceSpades"]
            break
    assert isinstance(descriptor, property)

def test_solitairelayout_has_CELL_TWO():
    assert hasattr(SolitaireLayout, "CELL_TWO")
    descriptor = None
    for klass in SolitaireLayout.__mro__:
        if "CELL_TWO" in klass.__dict__:
            descriptor = klass.__dict__["CELL_TWO"]
            break
    assert isinstance(descriptor, property)

def test_solitairelayout_has_aceDiamonds():
    assert hasattr(SolitaireLayout, "aceDiamonds")
    descriptor = None
    for klass in SolitaireLayout.__mro__:
        if "aceDiamonds" in klass.__dict__:
            descriptor = klass.__dict__["aceDiamonds"]
            break
    assert isinstance(descriptor, property)

def test_solitairelayout_has_cellTwo():
    assert hasattr(SolitaireLayout, "cellTwo")
    descriptor = None
    for klass in SolitaireLayout.__mro__:
        if "cellTwo" in klass.__dict__:
            descriptor = klass.__dict__["cellTwo"]
            break
    assert isinstance(descriptor, property)

def test_solitairelayout_has_SPADES_ACE_PILE():
    assert hasattr(SolitaireLayout, "SPADES_ACE_PILE")
    descriptor = None
    for klass in SolitaireLayout.__mro__:
        if "SPADES_ACE_PILE" in klass.__dict__:
            descriptor = klass.__dict__["SPADES_ACE_PILE"]
            break
    assert isinstance(descriptor, property)



def test_solitaireboard_is_not_abstract():
    assert not inspect.isabstract(SolitaireBoard)


def test_solitaireboard_constructor_exists():
    assert callable(SolitaireBoard.__init__)


def test_solitaireboard_constructor_args():
    sig = inspect.signature(SolitaireBoard.__init__)
    params = list(sig.parameters.keys())
    assert "GAME_WON" in params, "Missing parameter 'GAME_WON'"
    assert "timer" in params, "Missing parameter 'timer'"
    assert "numCards" in params, "Missing parameter 'numCards'"
    assert "timerCount" in params, "Missing parameter 'timerCount'"
    assert "timerLabel" in params, "Missing parameter 'timerLabel'"
    assert "newDrawCount" in params, "Missing parameter 'newDrawCount'"
    assert "RESET_STATS" in params, "Missing parameter 'RESET_STATS'"
    assert "drawCount" in params, "Missing parameter 'drawCount'"
    assert "newDifficulty" in params, "Missing parameter 'newDifficulty'"
    assert "timerToRun" in params, "Missing parameter 'timerToRun'"
    assert "numCardsInDiscardView" in params, "Missing parameter 'numCardsInDiscardView'"
    assert "statusBar" in params, "Missing parameter 'statusBar'"
    assert "GAME_SAVED" in params, "Missing parameter 'GAME_SAVED'"
    assert "winAnimationStatus" in params, "Missing parameter 'winAnimationStatus'"
    assert "timerToRunNextGame" in params, "Missing parameter 'timerToRunNextGame'"
    assert "DO_NOTHING" in params, "Missing parameter 'DO_NOTHING'"
    assert "deckNumber" in params, "Missing parameter 'deckNumber'"
    assert "difficulty" in params, "Missing parameter 'difficulty'"
    assert "GAME_LOST" in params, "Missing parameter 'GAME_LOST'"
    assert "winSoundsStatus" in params, "Missing parameter 'winSoundsStatus'"
    assert "backgroundNumber" in params, "Missing parameter 'backgroundNumber'"

def test_solitaireboard_has_GAME_WON():
    assert hasattr(SolitaireBoard, "GAME_WON")
    descriptor = None
    for klass in SolitaireBoard.__mro__:
        if "GAME_WON" in klass.__dict__:
            descriptor = klass.__dict__["GAME_WON"]
            break
    assert isinstance(descriptor, property)

def test_solitaireboard_has_timer():
    assert hasattr(SolitaireBoard, "timer")
    descriptor = None
    for klass in SolitaireBoard.__mro__:
        if "timer" in klass.__dict__:
            descriptor = klass.__dict__["timer"]
            break
    assert isinstance(descriptor, property)

def test_solitaireboard_has_numCards():
    assert hasattr(SolitaireBoard, "numCards")
    descriptor = None
    for klass in SolitaireBoard.__mro__:
        if "numCards" in klass.__dict__:
            descriptor = klass.__dict__["numCards"]
            break
    assert isinstance(descriptor, property)

def test_solitaireboard_has_timerCount():
    assert hasattr(SolitaireBoard, "timerCount")
    descriptor = None
    for klass in SolitaireBoard.__mro__:
        if "timerCount" in klass.__dict__:
            descriptor = klass.__dict__["timerCount"]
            break
    assert isinstance(descriptor, property)

def test_solitaireboard_has_timerLabel():
    assert hasattr(SolitaireBoard, "timerLabel")
    descriptor = None
    for klass in SolitaireBoard.__mro__:
        if "timerLabel" in klass.__dict__:
            descriptor = klass.__dict__["timerLabel"]
            break
    assert isinstance(descriptor, property)

def test_solitaireboard_has_newDrawCount():
    assert hasattr(SolitaireBoard, "newDrawCount")
    descriptor = None
    for klass in SolitaireBoard.__mro__:
        if "newDrawCount" in klass.__dict__:
            descriptor = klass.__dict__["newDrawCount"]
            break
    assert isinstance(descriptor, property)

def test_solitaireboard_has_RESET_STATS():
    assert hasattr(SolitaireBoard, "RESET_STATS")
    descriptor = None
    for klass in SolitaireBoard.__mro__:
        if "RESET_STATS" in klass.__dict__:
            descriptor = klass.__dict__["RESET_STATS"]
            break
    assert isinstance(descriptor, property)

def test_solitaireboard_has_drawCount():
    assert hasattr(SolitaireBoard, "drawCount")
    descriptor = None
    for klass in SolitaireBoard.__mro__:
        if "drawCount" in klass.__dict__:
            descriptor = klass.__dict__["drawCount"]
            break
    assert isinstance(descriptor, property)

def test_solitaireboard_has_newDifficulty():
    assert hasattr(SolitaireBoard, "newDifficulty")
    descriptor = None
    for klass in SolitaireBoard.__mro__:
        if "newDifficulty" in klass.__dict__:
            descriptor = klass.__dict__["newDifficulty"]
            break
    assert isinstance(descriptor, property)

def test_solitaireboard_has_timerToRun():
    assert hasattr(SolitaireBoard, "timerToRun")
    descriptor = None
    for klass in SolitaireBoard.__mro__:
        if "timerToRun" in klass.__dict__:
            descriptor = klass.__dict__["timerToRun"]
            break
    assert isinstance(descriptor, property)

def test_solitaireboard_has_numCardsInDiscardView():
    assert hasattr(SolitaireBoard, "numCardsInDiscardView")
    descriptor = None
    for klass in SolitaireBoard.__mro__:
        if "numCardsInDiscardView" in klass.__dict__:
            descriptor = klass.__dict__["numCardsInDiscardView"]
            break
    assert isinstance(descriptor, property)

def test_solitaireboard_has_statusBar():
    assert hasattr(SolitaireBoard, "statusBar")
    descriptor = None
    for klass in SolitaireBoard.__mro__:
        if "statusBar" in klass.__dict__:
            descriptor = klass.__dict__["statusBar"]
            break
    assert isinstance(descriptor, property)

def test_solitaireboard_has_GAME_SAVED():
    assert hasattr(SolitaireBoard, "GAME_SAVED")
    descriptor = None
    for klass in SolitaireBoard.__mro__:
        if "GAME_SAVED" in klass.__dict__:
            descriptor = klass.__dict__["GAME_SAVED"]
            break
    assert isinstance(descriptor, property)

def test_solitaireboard_has_winAnimationStatus():
    assert hasattr(SolitaireBoard, "winAnimationStatus")
    descriptor = None
    for klass in SolitaireBoard.__mro__:
        if "winAnimationStatus" in klass.__dict__:
            descriptor = klass.__dict__["winAnimationStatus"]
            break
    assert isinstance(descriptor, property)

def test_solitaireboard_has_timerToRunNextGame():
    assert hasattr(SolitaireBoard, "timerToRunNextGame")
    descriptor = None
    for klass in SolitaireBoard.__mro__:
        if "timerToRunNextGame" in klass.__dict__:
            descriptor = klass.__dict__["timerToRunNextGame"]
            break
    assert isinstance(descriptor, property)

def test_solitaireboard_has_DO_NOTHING():
    assert hasattr(SolitaireBoard, "DO_NOTHING")
    descriptor = None
    for klass in SolitaireBoard.__mro__:
        if "DO_NOTHING" in klass.__dict__:
            descriptor = klass.__dict__["DO_NOTHING"]
            break
    assert isinstance(descriptor, property)

def test_solitaireboard_has_deckNumber():
    assert hasattr(SolitaireBoard, "deckNumber")
    descriptor = None
    for klass in SolitaireBoard.__mro__:
        if "deckNumber" in klass.__dict__:
            descriptor = klass.__dict__["deckNumber"]
            break
    assert isinstance(descriptor, property)

def test_solitaireboard_has_difficulty():
    assert hasattr(SolitaireBoard, "difficulty")
    descriptor = None
    for klass in SolitaireBoard.__mro__:
        if "difficulty" in klass.__dict__:
            descriptor = klass.__dict__["difficulty"]
            break
    assert isinstance(descriptor, property)

def test_solitaireboard_has_GAME_LOST():
    assert hasattr(SolitaireBoard, "GAME_LOST")
    descriptor = None
    for klass in SolitaireBoard.__mro__:
        if "GAME_LOST" in klass.__dict__:
            descriptor = klass.__dict__["GAME_LOST"]
            break
    assert isinstance(descriptor, property)

def test_solitaireboard_has_winSoundsStatus():
    assert hasattr(SolitaireBoard, "winSoundsStatus")
    descriptor = None
    for klass in SolitaireBoard.__mro__:
        if "winSoundsStatus" in klass.__dict__:
            descriptor = klass.__dict__["winSoundsStatus"]
            break
    assert isinstance(descriptor, property)

def test_solitaireboard_has_backgroundNumber():
    assert hasattr(SolitaireBoard, "backgroundNumber")
    descriptor = None
    for klass in SolitaireBoard.__mro__:
        if "backgroundNumber" in klass.__dict__:
            descriptor = klass.__dict__["backgroundNumber"]
            break
    assert isinstance(descriptor, property)



def test_singlecell_is_not_abstract():
    assert not inspect.isabstract(SingleCell)


def test_singlecell_constructor_exists():
    assert callable(SingleCell.__init__)


def test_singlecell_constructor_args():
    sig = inspect.signature(SingleCell.__init__)
    params = list(sig.parameters.keys())



def test_fourrowsolitaire_is_not_abstract():
    assert not inspect.isabstract(FourRowSolitaire)


def test_fourrowsolitaire_constructor_exists():
    assert callable(FourRowSolitaire.__init__)


def test_fourrowsolitaire_constructor_args():
    sig = inspect.signature(FourRowSolitaire.__init__)
    params = list(sig.parameters.keys())
    assert "appearance" in params, "Missing parameter 'appearance'"
    assert "helpMenu" in params, "Missing parameter 'helpMenu'"
    assert "checkUpdate" in params, "Missing parameter 'checkUpdate'"
    assert "exit" in params, "Missing parameter 'exit'"
    assert "undo" in params, "Missing parameter 'undo'"
    assert "game" in params, "Missing parameter 'game'"
    assert "statistics" in params, "Missing parameter 'statistics'"
    assert "version" in params, "Missing parameter 'version'"
    assert "newGame" in params, "Missing parameter 'newGame'"
    assert "menuBar" in params, "Missing parameter 'menuBar'"
    assert "options" in params, "Missing parameter 'options'"
    assert "hint" in params, "Missing parameter 'hint'"
    assert "help" in params, "Missing parameter 'help'"
    assert "about" in params, "Missing parameter 'about'"

def test_fourrowsolitaire_has_appearance():
    assert hasattr(FourRowSolitaire, "appearance")
    descriptor = None
    for klass in FourRowSolitaire.__mro__:
        if "appearance" in klass.__dict__:
            descriptor = klass.__dict__["appearance"]
            break
    assert isinstance(descriptor, property)

def test_fourrowsolitaire_has_helpMenu():
    assert hasattr(FourRowSolitaire, "helpMenu")
    descriptor = None
    for klass in FourRowSolitaire.__mro__:
        if "helpMenu" in klass.__dict__:
            descriptor = klass.__dict__["helpMenu"]
            break
    assert isinstance(descriptor, property)

def test_fourrowsolitaire_has_checkUpdate():
    assert hasattr(FourRowSolitaire, "checkUpdate")
    descriptor = None
    for klass in FourRowSolitaire.__mro__:
        if "checkUpdate" in klass.__dict__:
            descriptor = klass.__dict__["checkUpdate"]
            break
    assert isinstance(descriptor, property)

def test_fourrowsolitaire_has_exit():
    assert hasattr(FourRowSolitaire, "exit")
    descriptor = None
    for klass in FourRowSolitaire.__mro__:
        if "exit" in klass.__dict__:
            descriptor = klass.__dict__["exit"]
            break
    assert isinstance(descriptor, property)

def test_fourrowsolitaire_has_undo():
    assert hasattr(FourRowSolitaire, "undo")
    descriptor = None
    for klass in FourRowSolitaire.__mro__:
        if "undo" in klass.__dict__:
            descriptor = klass.__dict__["undo"]
            break
    assert isinstance(descriptor, property)

def test_fourrowsolitaire_has_game():
    assert hasattr(FourRowSolitaire, "game")
    descriptor = None
    for klass in FourRowSolitaire.__mro__:
        if "game" in klass.__dict__:
            descriptor = klass.__dict__["game"]
            break
    assert isinstance(descriptor, property)

def test_fourrowsolitaire_has_statistics():
    assert hasattr(FourRowSolitaire, "statistics")
    descriptor = None
    for klass in FourRowSolitaire.__mro__:
        if "statistics" in klass.__dict__:
            descriptor = klass.__dict__["statistics"]
            break
    assert isinstance(descriptor, property)

def test_fourrowsolitaire_has_version():
    assert hasattr(FourRowSolitaire, "version")
    descriptor = None
    for klass in FourRowSolitaire.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_fourrowsolitaire_has_newGame():
    assert hasattr(FourRowSolitaire, "newGame")
    descriptor = None
    for klass in FourRowSolitaire.__mro__:
        if "newGame" in klass.__dict__:
            descriptor = klass.__dict__["newGame"]
            break
    assert isinstance(descriptor, property)

def test_fourrowsolitaire_has_menuBar():
    assert hasattr(FourRowSolitaire, "menuBar")
    descriptor = None
    for klass in FourRowSolitaire.__mro__:
        if "menuBar" in klass.__dict__:
            descriptor = klass.__dict__["menuBar"]
            break
    assert isinstance(descriptor, property)

def test_fourrowsolitaire_has_options():
    assert hasattr(FourRowSolitaire, "options")
    descriptor = None
    for klass in FourRowSolitaire.__mro__:
        if "options" in klass.__dict__:
            descriptor = klass.__dict__["options"]
            break
    assert isinstance(descriptor, property)

def test_fourrowsolitaire_has_hint():
    assert hasattr(FourRowSolitaire, "hint")
    descriptor = None
    for klass in FourRowSolitaire.__mro__:
        if "hint" in klass.__dict__:
            descriptor = klass.__dict__["hint"]
            break
    assert isinstance(descriptor, property)

def test_fourrowsolitaire_has_help():
    assert hasattr(FourRowSolitaire, "help")
    descriptor = None
    for klass in FourRowSolitaire.__mro__:
        if "help" in klass.__dict__:
            descriptor = klass.__dict__["help"]
            break
    assert isinstance(descriptor, property)

def test_fourrowsolitaire_has_about():
    assert hasattr(FourRowSolitaire, "about")
    descriptor = None
    for klass in FourRowSolitaire.__mro__:
        if "about" in klass.__dict__:
            descriptor = klass.__dict__["about"]
            break
    assert isinstance(descriptor, property)



def test_fireworksdisplay_is_not_abstract():
    assert not inspect.isabstract(FireworksDisplay)


def test_fireworksdisplay_constructor_exists():
    assert callable(FireworksDisplay.__init__)


def test_fireworksdisplay_constructor_args():
    sig = inspect.signature(FireworksDisplay.__init__)
    params = list(sig.parameters.keys())
    assert "y" in params, "Missing parameter 'y'"
    assert "FIREWORKS_TIME" in params, "Missing parameter 'FIREWORKS_TIME'"
    assert "startValue" in params, "Missing parameter 'startValue'"
    assert "x" in params, "Missing parameter 'x'"
    assert "FIREWORKS_SIZE" in params, "Missing parameter 'FIREWORKS_SIZE'"
    assert "numSets" in params, "Missing parameter 'numSets'"
    assert "xx" in params, "Missing parameter 'xx'"
    assert "random" in params, "Missing parameter 'random'"
    assert "timer" in params, "Missing parameter 'timer'"
    assert "num" in params, "Missing parameter 'num'"
    assert "NUM_FIREWORKS" in params, "Missing parameter 'NUM_FIREWORKS'"
    assert "yy" in params, "Missing parameter 'yy'"
    assert "SET_DELAY" in params, "Missing parameter 'SET_DELAY'"
    assert "colors" in params, "Missing parameter 'colors'"

def test_fireworksdisplay_has_y():
    assert hasattr(FireworksDisplay, "y")
    descriptor = None
    for klass in FireworksDisplay.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_fireworksdisplay_has_FIREWORKS_TIME():
    assert hasattr(FireworksDisplay, "FIREWORKS_TIME")
    descriptor = None
    for klass in FireworksDisplay.__mro__:
        if "FIREWORKS_TIME" in klass.__dict__:
            descriptor = klass.__dict__["FIREWORKS_TIME"]
            break
    assert isinstance(descriptor, property)

def test_fireworksdisplay_has_startValue():
    assert hasattr(FireworksDisplay, "startValue")
    descriptor = None
    for klass in FireworksDisplay.__mro__:
        if "startValue" in klass.__dict__:
            descriptor = klass.__dict__["startValue"]
            break
    assert isinstance(descriptor, property)

def test_fireworksdisplay_has_x():
    assert hasattr(FireworksDisplay, "x")
    descriptor = None
    for klass in FireworksDisplay.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_fireworksdisplay_has_FIREWORKS_SIZE():
    assert hasattr(FireworksDisplay, "FIREWORKS_SIZE")
    descriptor = None
    for klass in FireworksDisplay.__mro__:
        if "FIREWORKS_SIZE" in klass.__dict__:
            descriptor = klass.__dict__["FIREWORKS_SIZE"]
            break
    assert isinstance(descriptor, property)

def test_fireworksdisplay_has_numSets():
    assert hasattr(FireworksDisplay, "numSets")
    descriptor = None
    for klass in FireworksDisplay.__mro__:
        if "numSets" in klass.__dict__:
            descriptor = klass.__dict__["numSets"]
            break
    assert isinstance(descriptor, property)

def test_fireworksdisplay_has_xx():
    assert hasattr(FireworksDisplay, "xx")
    descriptor = None
    for klass in FireworksDisplay.__mro__:
        if "xx" in klass.__dict__:
            descriptor = klass.__dict__["xx"]
            break
    assert isinstance(descriptor, property)

def test_fireworksdisplay_has_random():
    assert hasattr(FireworksDisplay, "random")
    descriptor = None
    for klass in FireworksDisplay.__mro__:
        if "random" in klass.__dict__:
            descriptor = klass.__dict__["random"]
            break
    assert isinstance(descriptor, property)

def test_fireworksdisplay_has_timer():
    assert hasattr(FireworksDisplay, "timer")
    descriptor = None
    for klass in FireworksDisplay.__mro__:
        if "timer" in klass.__dict__:
            descriptor = klass.__dict__["timer"]
            break
    assert isinstance(descriptor, property)

def test_fireworksdisplay_has_num():
    assert hasattr(FireworksDisplay, "num")
    descriptor = None
    for klass in FireworksDisplay.__mro__:
        if "num" in klass.__dict__:
            descriptor = klass.__dict__["num"]
            break
    assert isinstance(descriptor, property)

def test_fireworksdisplay_has_NUM_FIREWORKS():
    assert hasattr(FireworksDisplay, "NUM_FIREWORKS")
    descriptor = None
    for klass in FireworksDisplay.__mro__:
        if "NUM_FIREWORKS" in klass.__dict__:
            descriptor = klass.__dict__["NUM_FIREWORKS"]
            break
    assert isinstance(descriptor, property)

def test_fireworksdisplay_has_yy():
    assert hasattr(FireworksDisplay, "yy")
    descriptor = None
    for klass in FireworksDisplay.__mro__:
        if "yy" in klass.__dict__:
            descriptor = klass.__dict__["yy"]
            break
    assert isinstance(descriptor, property)

def test_fireworksdisplay_has_SET_DELAY():
    assert hasattr(FireworksDisplay, "SET_DELAY")
    descriptor = None
    for klass in FireworksDisplay.__mro__:
        if "SET_DELAY" in klass.__dict__:
            descriptor = klass.__dict__["SET_DELAY"]
            break
    assert isinstance(descriptor, property)

def test_fireworksdisplay_has_colors():
    assert hasattr(FireworksDisplay, "colors")
    descriptor = None
    for klass in FireworksDisplay.__mro__:
        if "colors" in klass.__dict__:
            descriptor = klass.__dict__["colors"]
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
DiscardPile_strategy = st.builds(
    DiscardPile,
    cardsLeftFromDraw=
        st.integers(),
    drawCount=
        st.integers()
)
Deck_strategy = st.builds(
    Deck,
    deckNumber=
        st.integers()
)
DealDeck_strategy = st.builds(
    DealDeck,
    MEDIUM_THROUGH_LIMIT=
        st.integers(),
    redealable=
        st.booleans(),
    difficulty=
        st.integers(),
    numTimesThroughDeck=
        st.integers(),
    EASY_THROUGH_LIMIT=
        st.integers(),
    drawCount=
        st.integers(),
    deckThroughLimit=
        st.integers(),
    DRAW_THREE_THROUGH_LIMIT=
        st.integers(),
    HARD_THROUGH_LIMIT=
        st.integers(),
    DRAW_ONE_THROUGH_LIMIT=
        st.integers()
)
Column_strategy = st.builds(
    Column,
)
ChangeOptions_strategy = st.builds(
    ChangeOptions,
    winSoundsCheck=
        safe_text,
    winAnimationCheck=
        safe_text,
    ok=
        safe_text,
    drawOne=
        safe_text,
    medium=
        safe_text,
    easy=
        safe_text,
    drawCount=
        st.integers(),
    animation=
        st.integers(),
    hard=
        safe_text,
    difficulty=
        st.integers(),
    timerCheck=
        safe_text,
    timer=
        st.integers(),
    drawThree=
        safe_text,
    sounds=
        st.integers(),
    exited=
        st.booleans()
)
ChangeAppearance_strategy = st.builds(
    ChangeAppearance,
    backgrounds=
        safe_text,
    exited=
        st.booleans(),
    backgroundNumber=
        st.integers(),
    ok=
        safe_text,
    FRS_BACKGROUND=
        st.integers(),
    deckNumber=
        st.integers(),
    decks=
        safe_text,
    cardBackLabel=
        safe_text,
    backgroundLabel=
        safe_text,
    FRS_DECK=
        st.integers(),
    NUM_BACKGROUNDS=
        st.integers(),
    NUM_DECKS=
        st.integers()
)
CardStack_strategy = st.builds(
    CardStack,
)
Card_strategy = st.builds(
    Card,
    SIX=
        st.integers(),
    HEARTS_SUIT=
        safe_text,
    CLUBS_SUIT=
        safe_text,
    NINE=
        st.integers(),
    TEN=
        st.integers(),
    image=
        safe_text,
    QUEEN=
        st.integers(),
    fullCardNumber=
        st.integers(),
    faceUp=
        st.booleans(),
    highlighted=
        st.booleans(),
    DIAMONDS_SUIT=
        safe_text,
    INVALID_SUIT=
        safe_text,
    FOUR=
        st.integers(),
    cardImageString=
        safe_text,
    cardHighlighted=
        safe_text,
    INVALID_NUMBER=
        st.integers(),
    ACE=
        st.integers(),
    SPADES_SUIT=
        safe_text,
    TWO=
        st.integers(),
    cardSuit=
        safe_text,
    cardColor=
        st.integers(),
    cardNumber=
        st.integers(),
    cardBack=
        safe_text,
    THREE=
        st.integers(),
    EIGHT=
        st.integers(),
    location=
        safe_text,
    deckNumber=
        st.integers(),
    KING=
        st.integers(),
    FIVE=
        st.integers(),
    SEVEN=
        st.integers(),
    JACK=
        st.integers()
)
AcePile_strategy = st.builds(
    AcePile,
    suit=
        safe_text
)
ActionEvent_strategy = st.builds(
    ActionEvent,
)
Graphics_strategy = st.builds(
    Graphics,
)
WinScreen_strategy = st.builds(
    WinScreen,
)
SolitairePanel_strategy = st.builds(
    SolitairePanel,
    background=
        safe_text,
    backgroundNumber=
        st.integers()
)
SolitaireLayout_strategy = st.builds(
    SolitaireLayout,
    COLUMN_TWO=
        safe_text,
    COLUMN_THREE=
        safe_text,
    CELL_THREE=
        safe_text,
    colTwo=
        safe_text,
    colOne=
        safe_text,
    aceClubs=
        safe_text,
    COLUMEN_ONE=
        safe_text,
    aceHearts=
        safe_text,
    cellThree=
        safe_text,
    cellOne=
        safe_text,
    HEARTS_ACE_PILE=
        safe_text,
    DIAMONDS_ACE_PILE=
        safe_text,
    CELL_ONE=
        safe_text,
    cellFour=
        safe_text,
    DECK=
        safe_text,
    colFour=
        safe_text,
    CELL_FOUR=
        safe_text,
    discardPile=
        safe_text,
    COLUMN_FOUR=
        safe_text,
    deck=
        safe_text,
    CLUBS_ACE_PILE=
        safe_text,
    colThree=
        safe_text,
    DISCARD_PILE=
        safe_text,
    aceSpades=
        safe_text,
    CELL_TWO=
        safe_text,
    aceDiamonds=
        safe_text,
    cellTwo=
        safe_text,
    SPADES_ACE_PILE=
        safe_text
)
SolitaireBoard_strategy = st.builds(
    SolitaireBoard,
    GAME_WON=
        st.integers(),
    timer=
        safe_text,
    numCards=
        safe_text,
    timerCount=
        st.integers(),
    timerLabel=
        safe_text,
    newDrawCount=
        st.integers(),
    RESET_STATS=
        st.integers(),
    drawCount=
        st.integers(),
    newDifficulty=
        st.integers(),
    timerToRun=
        st.booleans(),
    numCardsInDiscardView=
        safe_text,
    statusBar=
        safe_text,
    GAME_SAVED=
        st.integers(),
    winAnimationStatus=
        st.integers(),
    timerToRunNextGame=
        st.integers(),
    DO_NOTHING=
        st.integers(),
    deckNumber=
        st.integers(),
    difficulty=
        st.integers(),
    GAME_LOST=
        st.integers(),
    winSoundsStatus=
        st.integers(),
    backgroundNumber=
        st.integers()
)
SingleCell_strategy = st.builds(
    SingleCell,
)
FourRowSolitaire_strategy = st.builds(
    FourRowSolitaire,
    appearance=
        safe_text,
    helpMenu=
        safe_text,
    checkUpdate=
        safe_text,
    exit=
        safe_text,
    undo=
        safe_text,
    game=
        safe_text,
    statistics=
        safe_text,
    version=
        st.none(),
    newGame=
        safe_text,
    menuBar=
        safe_text,
    options=
        safe_text,
    hint=
        safe_text,
    help=
        safe_text,
    about=
        safe_text
)
FireworksDisplay_strategy = st.builds(
    FireworksDisplay,
    y=
        safe_text,
    FIREWORKS_TIME=
        st.integers(),
    startValue=
        st.integers(),
    x=
        safe_text,
    FIREWORKS_SIZE=
        st.integers(),
    numSets=
        st.integers(),
    xx=
        safe_text,
    random=
        safe_text,
    timer=
        safe_text,
    num=
        st.integers(),
    NUM_FIREWORKS=
        st.integers(),
    yy=
        safe_text,
    SET_DELAY=
        st.integers(),
    colors=
        safe_text
)

@given(instance=DiscardPile_strategy)
@settings(max_examples=50)
def test_discardpile_instantiation(instance):
    assert isinstance(instance, DiscardPile)



@given(instance=DiscardPile_strategy)
def test_discardpile_cardsLeftFromDraw_setter(instance):
    original = instance.cardsLeftFromDraw
    instance.cardsLeftFromDraw = original
    assert instance.cardsLeftFromDraw == original



@given(instance=DiscardPile_strategy)
def test_discardpile_drawCount_setter(instance):
    original = instance.drawCount
    instance.drawCount = original
    assert instance.drawCount == original

@given(instance=Deck_strategy)
@settings(max_examples=50)
def test_deck_instantiation(instance):
    assert isinstance(instance, Deck)



@given(instance=Deck_strategy)
def test_deck_deckNumber_setter(instance):
    original = instance.deckNumber
    instance.deckNumber = original
    assert instance.deckNumber == original

@given(instance=DealDeck_strategy)
@settings(max_examples=50)
def test_dealdeck_instantiation(instance):
    assert isinstance(instance, DealDeck)



@given(instance=DealDeck_strategy)
def test_dealdeck_MEDIUM_THROUGH_LIMIT_setter(instance):
    original = instance.MEDIUM_THROUGH_LIMIT
    instance.MEDIUM_THROUGH_LIMIT = original
    assert instance.MEDIUM_THROUGH_LIMIT == original



@given(instance=DealDeck_strategy)
def test_dealdeck_redealable_setter(instance):
    original = instance.redealable
    instance.redealable = original
    assert instance.redealable == original



@given(instance=DealDeck_strategy)
def test_dealdeck_difficulty_setter(instance):
    original = instance.difficulty
    instance.difficulty = original
    assert instance.difficulty == original



@given(instance=DealDeck_strategy)
def test_dealdeck_numTimesThroughDeck_setter(instance):
    original = instance.numTimesThroughDeck
    instance.numTimesThroughDeck = original
    assert instance.numTimesThroughDeck == original



@given(instance=DealDeck_strategy)
def test_dealdeck_EASY_THROUGH_LIMIT_setter(instance):
    original = instance.EASY_THROUGH_LIMIT
    instance.EASY_THROUGH_LIMIT = original
    assert instance.EASY_THROUGH_LIMIT == original



@given(instance=DealDeck_strategy)
def test_dealdeck_drawCount_setter(instance):
    original = instance.drawCount
    instance.drawCount = original
    assert instance.drawCount == original



@given(instance=DealDeck_strategy)
def test_dealdeck_deckThroughLimit_setter(instance):
    original = instance.deckThroughLimit
    instance.deckThroughLimit = original
    assert instance.deckThroughLimit == original



@given(instance=DealDeck_strategy)
def test_dealdeck_DRAW_THREE_THROUGH_LIMIT_setter(instance):
    original = instance.DRAW_THREE_THROUGH_LIMIT
    instance.DRAW_THREE_THROUGH_LIMIT = original
    assert instance.DRAW_THREE_THROUGH_LIMIT == original



@given(instance=DealDeck_strategy)
def test_dealdeck_HARD_THROUGH_LIMIT_setter(instance):
    original = instance.HARD_THROUGH_LIMIT
    instance.HARD_THROUGH_LIMIT = original
    assert instance.HARD_THROUGH_LIMIT == original



@given(instance=DealDeck_strategy)
def test_dealdeck_DRAW_ONE_THROUGH_LIMIT_setter(instance):
    original = instance.DRAW_ONE_THROUGH_LIMIT
    instance.DRAW_ONE_THROUGH_LIMIT = original
    assert instance.DRAW_ONE_THROUGH_LIMIT == original

@given(instance=Column_strategy)
@settings(max_examples=50)
def test_column_instantiation(instance):
    assert isinstance(instance, Column)

@given(instance=ChangeOptions_strategy)
@settings(max_examples=50)
def test_changeoptions_instantiation(instance):
    assert isinstance(instance, ChangeOptions)



@given(instance=ChangeOptions_strategy)
def test_changeoptions_winSoundsCheck_setter(instance):
    original = instance.winSoundsCheck
    instance.winSoundsCheck = original
    assert instance.winSoundsCheck == original



@given(instance=ChangeOptions_strategy)
def test_changeoptions_winAnimationCheck_setter(instance):
    original = instance.winAnimationCheck
    instance.winAnimationCheck = original
    assert instance.winAnimationCheck == original



@given(instance=ChangeOptions_strategy)
def test_changeoptions_ok_setter(instance):
    original = instance.ok
    instance.ok = original
    assert instance.ok == original



@given(instance=ChangeOptions_strategy)
def test_changeoptions_drawOne_setter(instance):
    original = instance.drawOne
    instance.drawOne = original
    assert instance.drawOne == original



@given(instance=ChangeOptions_strategy)
def test_changeoptions_medium_setter(instance):
    original = instance.medium
    instance.medium = original
    assert instance.medium == original



@given(instance=ChangeOptions_strategy)
def test_changeoptions_easy_setter(instance):
    original = instance.easy
    instance.easy = original
    assert instance.easy == original



@given(instance=ChangeOptions_strategy)
def test_changeoptions_drawCount_setter(instance):
    original = instance.drawCount
    instance.drawCount = original
    assert instance.drawCount == original



@given(instance=ChangeOptions_strategy)
def test_changeoptions_animation_setter(instance):
    original = instance.animation
    instance.animation = original
    assert instance.animation == original



@given(instance=ChangeOptions_strategy)
def test_changeoptions_hard_setter(instance):
    original = instance.hard
    instance.hard = original
    assert instance.hard == original



@given(instance=ChangeOptions_strategy)
def test_changeoptions_difficulty_setter(instance):
    original = instance.difficulty
    instance.difficulty = original
    assert instance.difficulty == original



@given(instance=ChangeOptions_strategy)
def test_changeoptions_timerCheck_setter(instance):
    original = instance.timerCheck
    instance.timerCheck = original
    assert instance.timerCheck == original



@given(instance=ChangeOptions_strategy)
def test_changeoptions_timer_setter(instance):
    original = instance.timer
    instance.timer = original
    assert instance.timer == original



@given(instance=ChangeOptions_strategy)
def test_changeoptions_drawThree_setter(instance):
    original = instance.drawThree
    instance.drawThree = original
    assert instance.drawThree == original



@given(instance=ChangeOptions_strategy)
def test_changeoptions_sounds_setter(instance):
    original = instance.sounds
    instance.sounds = original
    assert instance.sounds == original



@given(instance=ChangeOptions_strategy)
def test_changeoptions_exited_setter(instance):
    original = instance.exited
    instance.exited = original
    assert instance.exited == original

@given(instance=ChangeAppearance_strategy)
@settings(max_examples=50)
def test_changeappearance_instantiation(instance):
    assert isinstance(instance, ChangeAppearance)



@given(instance=ChangeAppearance_strategy)
def test_changeappearance_backgrounds_setter(instance):
    original = instance.backgrounds
    instance.backgrounds = original
    assert instance.backgrounds == original



@given(instance=ChangeAppearance_strategy)
def test_changeappearance_exited_setter(instance):
    original = instance.exited
    instance.exited = original
    assert instance.exited == original



@given(instance=ChangeAppearance_strategy)
def test_changeappearance_backgroundNumber_setter(instance):
    original = instance.backgroundNumber
    instance.backgroundNumber = original
    assert instance.backgroundNumber == original



@given(instance=ChangeAppearance_strategy)
def test_changeappearance_ok_setter(instance):
    original = instance.ok
    instance.ok = original
    assert instance.ok == original



@given(instance=ChangeAppearance_strategy)
def test_changeappearance_FRS_BACKGROUND_setter(instance):
    original = instance.FRS_BACKGROUND
    instance.FRS_BACKGROUND = original
    assert instance.FRS_BACKGROUND == original



@given(instance=ChangeAppearance_strategy)
def test_changeappearance_deckNumber_setter(instance):
    original = instance.deckNumber
    instance.deckNumber = original
    assert instance.deckNumber == original



@given(instance=ChangeAppearance_strategy)
def test_changeappearance_decks_setter(instance):
    original = instance.decks
    instance.decks = original
    assert instance.decks == original



@given(instance=ChangeAppearance_strategy)
def test_changeappearance_cardBackLabel_setter(instance):
    original = instance.cardBackLabel
    instance.cardBackLabel = original
    assert instance.cardBackLabel == original



@given(instance=ChangeAppearance_strategy)
def test_changeappearance_backgroundLabel_setter(instance):
    original = instance.backgroundLabel
    instance.backgroundLabel = original
    assert instance.backgroundLabel == original



@given(instance=ChangeAppearance_strategy)
def test_changeappearance_FRS_DECK_setter(instance):
    original = instance.FRS_DECK
    instance.FRS_DECK = original
    assert instance.FRS_DECK == original



@given(instance=ChangeAppearance_strategy)
def test_changeappearance_NUM_BACKGROUNDS_setter(instance):
    original = instance.NUM_BACKGROUNDS
    instance.NUM_BACKGROUNDS = original
    assert instance.NUM_BACKGROUNDS == original



@given(instance=ChangeAppearance_strategy)
def test_changeappearance_NUM_DECKS_setter(instance):
    original = instance.NUM_DECKS
    instance.NUM_DECKS = original
    assert instance.NUM_DECKS == original

@given(instance=CardStack_strategy)
@settings(max_examples=50)
def test_cardstack_instantiation(instance):
    assert isinstance(instance, CardStack)

@given(instance=Card_strategy)
@settings(max_examples=50)
def test_card_instantiation(instance):
    assert isinstance(instance, Card)



@given(instance=Card_strategy)
def test_card_SIX_setter(instance):
    original = instance.SIX
    instance.SIX = original
    assert instance.SIX == original



@given(instance=Card_strategy)
def test_card_HEARTS_SUIT_setter(instance):
    original = instance.HEARTS_SUIT
    instance.HEARTS_SUIT = original
    assert instance.HEARTS_SUIT == original



@given(instance=Card_strategy)
def test_card_CLUBS_SUIT_setter(instance):
    original = instance.CLUBS_SUIT
    instance.CLUBS_SUIT = original
    assert instance.CLUBS_SUIT == original



@given(instance=Card_strategy)
def test_card_NINE_setter(instance):
    original = instance.NINE
    instance.NINE = original
    assert instance.NINE == original



@given(instance=Card_strategy)
def test_card_TEN_setter(instance):
    original = instance.TEN
    instance.TEN = original
    assert instance.TEN == original



@given(instance=Card_strategy)
def test_card_image_setter(instance):
    original = instance.image
    instance.image = original
    assert instance.image == original



@given(instance=Card_strategy)
def test_card_QUEEN_setter(instance):
    original = instance.QUEEN
    instance.QUEEN = original
    assert instance.QUEEN == original



@given(instance=Card_strategy)
def test_card_fullCardNumber_setter(instance):
    original = instance.fullCardNumber
    instance.fullCardNumber = original
    assert instance.fullCardNumber == original



@given(instance=Card_strategy)
def test_card_faceUp_setter(instance):
    original = instance.faceUp
    instance.faceUp = original
    assert instance.faceUp == original



@given(instance=Card_strategy)
def test_card_highlighted_setter(instance):
    original = instance.highlighted
    instance.highlighted = original
    assert instance.highlighted == original



@given(instance=Card_strategy)
def test_card_DIAMONDS_SUIT_setter(instance):
    original = instance.DIAMONDS_SUIT
    instance.DIAMONDS_SUIT = original
    assert instance.DIAMONDS_SUIT == original



@given(instance=Card_strategy)
def test_card_INVALID_SUIT_setter(instance):
    original = instance.INVALID_SUIT
    instance.INVALID_SUIT = original
    assert instance.INVALID_SUIT == original



@given(instance=Card_strategy)
def test_card_FOUR_setter(instance):
    original = instance.FOUR
    instance.FOUR = original
    assert instance.FOUR == original



@given(instance=Card_strategy)
def test_card_cardImageString_setter(instance):
    original = instance.cardImageString
    instance.cardImageString = original
    assert instance.cardImageString == original



@given(instance=Card_strategy)
def test_card_cardHighlighted_setter(instance):
    original = instance.cardHighlighted
    instance.cardHighlighted = original
    assert instance.cardHighlighted == original



@given(instance=Card_strategy)
def test_card_INVALID_NUMBER_setter(instance):
    original = instance.INVALID_NUMBER
    instance.INVALID_NUMBER = original
    assert instance.INVALID_NUMBER == original



@given(instance=Card_strategy)
def test_card_ACE_setter(instance):
    original = instance.ACE
    instance.ACE = original
    assert instance.ACE == original



@given(instance=Card_strategy)
def test_card_SPADES_SUIT_setter(instance):
    original = instance.SPADES_SUIT
    instance.SPADES_SUIT = original
    assert instance.SPADES_SUIT == original



@given(instance=Card_strategy)
def test_card_TWO_setter(instance):
    original = instance.TWO
    instance.TWO = original
    assert instance.TWO == original



@given(instance=Card_strategy)
def test_card_cardSuit_setter(instance):
    original = instance.cardSuit
    instance.cardSuit = original
    assert instance.cardSuit == original



@given(instance=Card_strategy)
def test_card_cardColor_setter(instance):
    original = instance.cardColor
    instance.cardColor = original
    assert instance.cardColor == original



@given(instance=Card_strategy)
def test_card_cardNumber_setter(instance):
    original = instance.cardNumber
    instance.cardNumber = original
    assert instance.cardNumber == original



@given(instance=Card_strategy)
def test_card_cardBack_setter(instance):
    original = instance.cardBack
    instance.cardBack = original
    assert instance.cardBack == original



@given(instance=Card_strategy)
def test_card_THREE_setter(instance):
    original = instance.THREE
    instance.THREE = original
    assert instance.THREE == original



@given(instance=Card_strategy)
def test_card_EIGHT_setter(instance):
    original = instance.EIGHT
    instance.EIGHT = original
    assert instance.EIGHT == original



@given(instance=Card_strategy)
def test_card_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original



@given(instance=Card_strategy)
def test_card_deckNumber_setter(instance):
    original = instance.deckNumber
    instance.deckNumber = original
    assert instance.deckNumber == original



@given(instance=Card_strategy)
def test_card_KING_setter(instance):
    original = instance.KING
    instance.KING = original
    assert instance.KING == original



@given(instance=Card_strategy)
def test_card_FIVE_setter(instance):
    original = instance.FIVE
    instance.FIVE = original
    assert instance.FIVE == original



@given(instance=Card_strategy)
def test_card_SEVEN_setter(instance):
    original = instance.SEVEN
    instance.SEVEN = original
    assert instance.SEVEN == original



@given(instance=Card_strategy)
def test_card_JACK_setter(instance):
    original = instance.JACK
    instance.JACK = original
    assert instance.JACK == original

@given(instance=AcePile_strategy)
@settings(max_examples=50)
def test_acepile_instantiation(instance):
    assert isinstance(instance, AcePile)



@given(instance=AcePile_strategy)
def test_acepile_suit_setter(instance):
    original = instance.suit
    instance.suit = original
    assert instance.suit == original

@given(instance=ActionEvent_strategy)
@settings(max_examples=50)
def test_actionevent_instantiation(instance):
    assert isinstance(instance, ActionEvent)

@given(instance=Graphics_strategy)
@settings(max_examples=50)
def test_graphics_instantiation(instance):
    assert isinstance(instance, Graphics)

@given(instance=WinScreen_strategy)
@settings(max_examples=50)
def test_winscreen_instantiation(instance):
    assert isinstance(instance, WinScreen)

@given(instance=SolitairePanel_strategy)
@settings(max_examples=50)
def test_solitairepanel_instantiation(instance):
    assert isinstance(instance, SolitairePanel)



@given(instance=SolitairePanel_strategy)
def test_solitairepanel_background_setter(instance):
    original = instance.background
    instance.background = original
    assert instance.background == original



@given(instance=SolitairePanel_strategy)
def test_solitairepanel_backgroundNumber_setter(instance):
    original = instance.backgroundNumber
    instance.backgroundNumber = original
    assert instance.backgroundNumber == original

@given(instance=SolitaireLayout_strategy)
@settings(max_examples=50)
def test_solitairelayout_instantiation(instance):
    assert isinstance(instance, SolitaireLayout)



@given(instance=SolitaireLayout_strategy)
def test_solitairelayout_COLUMN_TWO_setter(instance):
    original = instance.COLUMN_TWO
    instance.COLUMN_TWO = original
    assert instance.COLUMN_TWO == original



@given(instance=SolitaireLayout_strategy)
def test_solitairelayout_COLUMN_THREE_setter(instance):
    original = instance.COLUMN_THREE
    instance.COLUMN_THREE = original
    assert instance.COLUMN_THREE == original



@given(instance=SolitaireLayout_strategy)
def test_solitairelayout_CELL_THREE_setter(instance):
    original = instance.CELL_THREE
    instance.CELL_THREE = original
    assert instance.CELL_THREE == original



@given(instance=SolitaireLayout_strategy)
def test_solitairelayout_colTwo_setter(instance):
    original = instance.colTwo
    instance.colTwo = original
    assert instance.colTwo == original



@given(instance=SolitaireLayout_strategy)
def test_solitairelayout_colOne_setter(instance):
    original = instance.colOne
    instance.colOne = original
    assert instance.colOne == original



@given(instance=SolitaireLayout_strategy)
def test_solitairelayout_aceClubs_setter(instance):
    original = instance.aceClubs
    instance.aceClubs = original
    assert instance.aceClubs == original



@given(instance=SolitaireLayout_strategy)
def test_solitairelayout_COLUMEN_ONE_setter(instance):
    original = instance.COLUMEN_ONE
    instance.COLUMEN_ONE = original
    assert instance.COLUMEN_ONE == original



@given(instance=SolitaireLayout_strategy)
def test_solitairelayout_aceHearts_setter(instance):
    original = instance.aceHearts
    instance.aceHearts = original
    assert instance.aceHearts == original



@given(instance=SolitaireLayout_strategy)
def test_solitairelayout_cellThree_setter(instance):
    original = instance.cellThree
    instance.cellThree = original
    assert instance.cellThree == original



@given(instance=SolitaireLayout_strategy)
def test_solitairelayout_cellOne_setter(instance):
    original = instance.cellOne
    instance.cellOne = original
    assert instance.cellOne == original



@given(instance=SolitaireLayout_strategy)
def test_solitairelayout_HEARTS_ACE_PILE_setter(instance):
    original = instance.HEARTS_ACE_PILE
    instance.HEARTS_ACE_PILE = original
    assert instance.HEARTS_ACE_PILE == original



@given(instance=SolitaireLayout_strategy)
def test_solitairelayout_DIAMONDS_ACE_PILE_setter(instance):
    original = instance.DIAMONDS_ACE_PILE
    instance.DIAMONDS_ACE_PILE = original
    assert instance.DIAMONDS_ACE_PILE == original



@given(instance=SolitaireLayout_strategy)
def test_solitairelayout_CELL_ONE_setter(instance):
    original = instance.CELL_ONE
    instance.CELL_ONE = original
    assert instance.CELL_ONE == original



@given(instance=SolitaireLayout_strategy)
def test_solitairelayout_cellFour_setter(instance):
    original = instance.cellFour
    instance.cellFour = original
    assert instance.cellFour == original



@given(instance=SolitaireLayout_strategy)
def test_solitairelayout_DECK_setter(instance):
    original = instance.DECK
    instance.DECK = original
    assert instance.DECK == original



@given(instance=SolitaireLayout_strategy)
def test_solitairelayout_colFour_setter(instance):
    original = instance.colFour
    instance.colFour = original
    assert instance.colFour == original



@given(instance=SolitaireLayout_strategy)
def test_solitairelayout_CELL_FOUR_setter(instance):
    original = instance.CELL_FOUR
    instance.CELL_FOUR = original
    assert instance.CELL_FOUR == original



@given(instance=SolitaireLayout_strategy)
def test_solitairelayout_discardPile_setter(instance):
    original = instance.discardPile
    instance.discardPile = original
    assert instance.discardPile == original



@given(instance=SolitaireLayout_strategy)
def test_solitairelayout_COLUMN_FOUR_setter(instance):
    original = instance.COLUMN_FOUR
    instance.COLUMN_FOUR = original
    assert instance.COLUMN_FOUR == original



@given(instance=SolitaireLayout_strategy)
def test_solitairelayout_deck_setter(instance):
    original = instance.deck
    instance.deck = original
    assert instance.deck == original



@given(instance=SolitaireLayout_strategy)
def test_solitairelayout_CLUBS_ACE_PILE_setter(instance):
    original = instance.CLUBS_ACE_PILE
    instance.CLUBS_ACE_PILE = original
    assert instance.CLUBS_ACE_PILE == original



@given(instance=SolitaireLayout_strategy)
def test_solitairelayout_colThree_setter(instance):
    original = instance.colThree
    instance.colThree = original
    assert instance.colThree == original



@given(instance=SolitaireLayout_strategy)
def test_solitairelayout_DISCARD_PILE_setter(instance):
    original = instance.DISCARD_PILE
    instance.DISCARD_PILE = original
    assert instance.DISCARD_PILE == original



@given(instance=SolitaireLayout_strategy)
def test_solitairelayout_aceSpades_setter(instance):
    original = instance.aceSpades
    instance.aceSpades = original
    assert instance.aceSpades == original



@given(instance=SolitaireLayout_strategy)
def test_solitairelayout_CELL_TWO_setter(instance):
    original = instance.CELL_TWO
    instance.CELL_TWO = original
    assert instance.CELL_TWO == original



@given(instance=SolitaireLayout_strategy)
def test_solitairelayout_aceDiamonds_setter(instance):
    original = instance.aceDiamonds
    instance.aceDiamonds = original
    assert instance.aceDiamonds == original



@given(instance=SolitaireLayout_strategy)
def test_solitairelayout_cellTwo_setter(instance):
    original = instance.cellTwo
    instance.cellTwo = original
    assert instance.cellTwo == original



@given(instance=SolitaireLayout_strategy)
def test_solitairelayout_SPADES_ACE_PILE_setter(instance):
    original = instance.SPADES_ACE_PILE
    instance.SPADES_ACE_PILE = original
    assert instance.SPADES_ACE_PILE == original

@given(instance=SolitaireBoard_strategy)
@settings(max_examples=50)
def test_solitaireboard_instantiation(instance):
    assert isinstance(instance, SolitaireBoard)



@given(instance=SolitaireBoard_strategy)
def test_solitaireboard_GAME_WON_setter(instance):
    original = instance.GAME_WON
    instance.GAME_WON = original
    assert instance.GAME_WON == original



@given(instance=SolitaireBoard_strategy)
def test_solitaireboard_timer_setter(instance):
    original = instance.timer
    instance.timer = original
    assert instance.timer == original



@given(instance=SolitaireBoard_strategy)
def test_solitaireboard_numCards_setter(instance):
    original = instance.numCards
    instance.numCards = original
    assert instance.numCards == original



@given(instance=SolitaireBoard_strategy)
def test_solitaireboard_timerCount_setter(instance):
    original = instance.timerCount
    instance.timerCount = original
    assert instance.timerCount == original



@given(instance=SolitaireBoard_strategy)
def test_solitaireboard_timerLabel_setter(instance):
    original = instance.timerLabel
    instance.timerLabel = original
    assert instance.timerLabel == original



@given(instance=SolitaireBoard_strategy)
def test_solitaireboard_newDrawCount_setter(instance):
    original = instance.newDrawCount
    instance.newDrawCount = original
    assert instance.newDrawCount == original



@given(instance=SolitaireBoard_strategy)
def test_solitaireboard_RESET_STATS_setter(instance):
    original = instance.RESET_STATS
    instance.RESET_STATS = original
    assert instance.RESET_STATS == original



@given(instance=SolitaireBoard_strategy)
def test_solitaireboard_drawCount_setter(instance):
    original = instance.drawCount
    instance.drawCount = original
    assert instance.drawCount == original



@given(instance=SolitaireBoard_strategy)
def test_solitaireboard_newDifficulty_setter(instance):
    original = instance.newDifficulty
    instance.newDifficulty = original
    assert instance.newDifficulty == original



@given(instance=SolitaireBoard_strategy)
def test_solitaireboard_timerToRun_setter(instance):
    original = instance.timerToRun
    instance.timerToRun = original
    assert instance.timerToRun == original



@given(instance=SolitaireBoard_strategy)
def test_solitaireboard_numCardsInDiscardView_setter(instance):
    original = instance.numCardsInDiscardView
    instance.numCardsInDiscardView = original
    assert instance.numCardsInDiscardView == original



@given(instance=SolitaireBoard_strategy)
def test_solitaireboard_statusBar_setter(instance):
    original = instance.statusBar
    instance.statusBar = original
    assert instance.statusBar == original



@given(instance=SolitaireBoard_strategy)
def test_solitaireboard_GAME_SAVED_setter(instance):
    original = instance.GAME_SAVED
    instance.GAME_SAVED = original
    assert instance.GAME_SAVED == original



@given(instance=SolitaireBoard_strategy)
def test_solitaireboard_winAnimationStatus_setter(instance):
    original = instance.winAnimationStatus
    instance.winAnimationStatus = original
    assert instance.winAnimationStatus == original



@given(instance=SolitaireBoard_strategy)
def test_solitaireboard_timerToRunNextGame_setter(instance):
    original = instance.timerToRunNextGame
    instance.timerToRunNextGame = original
    assert instance.timerToRunNextGame == original



@given(instance=SolitaireBoard_strategy)
def test_solitaireboard_DO_NOTHING_setter(instance):
    original = instance.DO_NOTHING
    instance.DO_NOTHING = original
    assert instance.DO_NOTHING == original



@given(instance=SolitaireBoard_strategy)
def test_solitaireboard_deckNumber_setter(instance):
    original = instance.deckNumber
    instance.deckNumber = original
    assert instance.deckNumber == original



@given(instance=SolitaireBoard_strategy)
def test_solitaireboard_difficulty_setter(instance):
    original = instance.difficulty
    instance.difficulty = original
    assert instance.difficulty == original



@given(instance=SolitaireBoard_strategy)
def test_solitaireboard_GAME_LOST_setter(instance):
    original = instance.GAME_LOST
    instance.GAME_LOST = original
    assert instance.GAME_LOST == original



@given(instance=SolitaireBoard_strategy)
def test_solitaireboard_winSoundsStatus_setter(instance):
    original = instance.winSoundsStatus
    instance.winSoundsStatus = original
    assert instance.winSoundsStatus == original



@given(instance=SolitaireBoard_strategy)
def test_solitaireboard_backgroundNumber_setter(instance):
    original = instance.backgroundNumber
    instance.backgroundNumber = original
    assert instance.backgroundNumber == original

@given(instance=SingleCell_strategy)
@settings(max_examples=50)
def test_singlecell_instantiation(instance):
    assert isinstance(instance, SingleCell)

@given(instance=FourRowSolitaire_strategy)
@settings(max_examples=50)
def test_fourrowsolitaire_instantiation(instance):
    assert isinstance(instance, FourRowSolitaire)



@given(instance=FourRowSolitaire_strategy)
def test_fourrowsolitaire_appearance_setter(instance):
    original = instance.appearance
    instance.appearance = original
    assert instance.appearance == original



@given(instance=FourRowSolitaire_strategy)
def test_fourrowsolitaire_helpMenu_setter(instance):
    original = instance.helpMenu
    instance.helpMenu = original
    assert instance.helpMenu == original



@given(instance=FourRowSolitaire_strategy)
def test_fourrowsolitaire_checkUpdate_setter(instance):
    original = instance.checkUpdate
    instance.checkUpdate = original
    assert instance.checkUpdate == original



@given(instance=FourRowSolitaire_strategy)
def test_fourrowsolitaire_exit_setter(instance):
    original = instance.exit
    instance.exit = original
    assert instance.exit == original



@given(instance=FourRowSolitaire_strategy)
def test_fourrowsolitaire_undo_setter(instance):
    original = instance.undo
    instance.undo = original
    assert instance.undo == original



@given(instance=FourRowSolitaire_strategy)
def test_fourrowsolitaire_game_setter(instance):
    original = instance.game
    instance.game = original
    assert instance.game == original



@given(instance=FourRowSolitaire_strategy)
def test_fourrowsolitaire_statistics_setter(instance):
    original = instance.statistics
    instance.statistics = original
    assert instance.statistics == original



@given(instance=FourRowSolitaire_strategy)
def test_fourrowsolitaire_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original



@given(instance=FourRowSolitaire_strategy)
def test_fourrowsolitaire_newGame_setter(instance):
    original = instance.newGame
    instance.newGame = original
    assert instance.newGame == original



@given(instance=FourRowSolitaire_strategy)
def test_fourrowsolitaire_menuBar_setter(instance):
    original = instance.menuBar
    instance.menuBar = original
    assert instance.menuBar == original



@given(instance=FourRowSolitaire_strategy)
def test_fourrowsolitaire_options_setter(instance):
    original = instance.options
    instance.options = original
    assert instance.options == original



@given(instance=FourRowSolitaire_strategy)
def test_fourrowsolitaire_hint_setter(instance):
    original = instance.hint
    instance.hint = original
    assert instance.hint == original



@given(instance=FourRowSolitaire_strategy)
def test_fourrowsolitaire_help_setter(instance):
    original = instance.help
    instance.help = original
    assert instance.help == original



@given(instance=FourRowSolitaire_strategy)
def test_fourrowsolitaire_about_setter(instance):
    original = instance.about
    instance.about = original
    assert instance.about == original

@given(instance=FireworksDisplay_strategy)
@settings(max_examples=50)
def test_fireworksdisplay_instantiation(instance):
    assert isinstance(instance, FireworksDisplay)



@given(instance=FireworksDisplay_strategy)
def test_fireworksdisplay_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original



@given(instance=FireworksDisplay_strategy)
def test_fireworksdisplay_FIREWORKS_TIME_setter(instance):
    original = instance.FIREWORKS_TIME
    instance.FIREWORKS_TIME = original
    assert instance.FIREWORKS_TIME == original



@given(instance=FireworksDisplay_strategy)
def test_fireworksdisplay_startValue_setter(instance):
    original = instance.startValue
    instance.startValue = original
    assert instance.startValue == original



@given(instance=FireworksDisplay_strategy)
def test_fireworksdisplay_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=FireworksDisplay_strategy)
def test_fireworksdisplay_FIREWORKS_SIZE_setter(instance):
    original = instance.FIREWORKS_SIZE
    instance.FIREWORKS_SIZE = original
    assert instance.FIREWORKS_SIZE == original



@given(instance=FireworksDisplay_strategy)
def test_fireworksdisplay_numSets_setter(instance):
    original = instance.numSets
    instance.numSets = original
    assert instance.numSets == original



@given(instance=FireworksDisplay_strategy)
def test_fireworksdisplay_xx_setter(instance):
    original = instance.xx
    instance.xx = original
    assert instance.xx == original



@given(instance=FireworksDisplay_strategy)
def test_fireworksdisplay_random_setter(instance):
    original = instance.random
    instance.random = original
    assert instance.random == original



@given(instance=FireworksDisplay_strategy)
def test_fireworksdisplay_timer_setter(instance):
    original = instance.timer
    instance.timer = original
    assert instance.timer == original



@given(instance=FireworksDisplay_strategy)
def test_fireworksdisplay_num_setter(instance):
    original = instance.num
    instance.num = original
    assert instance.num == original



@given(instance=FireworksDisplay_strategy)
def test_fireworksdisplay_NUM_FIREWORKS_setter(instance):
    original = instance.NUM_FIREWORKS
    instance.NUM_FIREWORKS = original
    assert instance.NUM_FIREWORKS == original



@given(instance=FireworksDisplay_strategy)
def test_fireworksdisplay_yy_setter(instance):
    original = instance.yy
    instance.yy = original
    assert instance.yy == original



@given(instance=FireworksDisplay_strategy)
def test_fireworksdisplay_SET_DELAY_setter(instance):
    original = instance.SET_DELAY
    instance.SET_DELAY = original
    assert instance.SET_DELAY == original



@given(instance=FireworksDisplay_strategy)
def test_fireworksdisplay_colors_setter(instance):
    original = instance.colors
    instance.colors = original
    assert instance.colors == original
