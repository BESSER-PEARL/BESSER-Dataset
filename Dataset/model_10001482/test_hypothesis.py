import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    BenannteEinrichtung,
    Deck,
    Kabine,
    Antrieb,
    TurboliftSchacht,
    Steuerung,
    TurboliftSystem,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_benannteeinrichtung_is_not_abstract():
    assert not inspect.isabstract(BenannteEinrichtung)


def test_benannteeinrichtung_constructor_exists():
    assert callable(BenannteEinrichtung.__init__)


def test_benannteeinrichtung_constructor_args():
    sig = inspect.signature(BenannteEinrichtung.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_benannteeinrichtung_has_name():
    assert hasattr(BenannteEinrichtung, "name")
    descriptor = None
    for klass in BenannteEinrichtung.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_deck_is_not_abstract():
    assert not inspect.isabstract(Deck)


def test_deck_constructor_exists():
    assert callable(Deck.__init__)


def test_deck_constructor_args():
    sig = inspect.signature(Deck.__init__)
    params = list(sig.parameters.keys())
    assert "sektion" in params, "Missing parameter 'sektion'"
    assert "fahrtWunsch" in params, "Missing parameter 'fahrtWunsch'"

def test_deck_has_sektion():
    assert hasattr(Deck, "sektion")
    descriptor = None
    for klass in Deck.__mro__:
        if "sektion" in klass.__dict__:
            descriptor = klass.__dict__["sektion"]
            break
    assert isinstance(descriptor, property)

def test_deck_has_fahrtWunsch():
    assert hasattr(Deck, "fahrtWunsch")
    descriptor = None
    for klass in Deck.__mro__:
        if "fahrtWunsch" in klass.__dict__:
            descriptor = klass.__dict__["fahrtWunsch"]
            break
    assert isinstance(descriptor, property)



def test_kabine_is_not_abstract():
    assert not inspect.isabstract(Kabine)


def test_kabine_constructor_exists():
    assert callable(Kabine.__init__)


def test_kabine_constructor_args():
    sig = inspect.signature(Kabine.__init__)
    params = list(sig.parameters.keys())
    assert "tuerZustand" in params, "Missing parameter 'tuerZustand'"

def test_kabine_has_tuerZustand():
    assert hasattr(Kabine, "tuerZustand")
    descriptor = None
    for klass in Kabine.__mro__:
        if "tuerZustand" in klass.__dict__:
            descriptor = klass.__dict__["tuerZustand"]
            break
    assert isinstance(descriptor, property)



def test_antrieb_is_not_abstract():
    assert not inspect.isabstract(Antrieb)


def test_antrieb_constructor_exists():
    assert callable(Antrieb.__init__)


def test_antrieb_constructor_args():
    sig = inspect.signature(Antrieb.__init__)
    params = list(sig.parameters.keys())
    assert "aNTRIEBSART" in params, "Missing parameter 'aNTRIEBSART'"

def test_antrieb_has_aNTRIEBSART():
    assert hasattr(Antrieb, "aNTRIEBSART")
    descriptor = None
    for klass in Antrieb.__mro__:
        if "aNTRIEBSART" in klass.__dict__:
            descriptor = klass.__dict__["aNTRIEBSART"]
            break
    assert isinstance(descriptor, property)



def test_turboliftschacht_is_not_abstract():
    assert not inspect.isabstract(TurboliftSchacht)


def test_turboliftschacht_constructor_exists():
    assert callable(TurboliftSchacht.__init__)


def test_turboliftschacht_constructor_args():
    sig = inspect.signature(TurboliftSchacht.__init__)
    params = list(sig.parameters.keys())
    assert "vertikal" in params, "Missing parameter 'vertikal'"

def test_turboliftschacht_has_vertikal():
    assert hasattr(TurboliftSchacht, "vertikal")
    descriptor = None
    for klass in TurboliftSchacht.__mro__:
        if "vertikal" in klass.__dict__:
            descriptor = klass.__dict__["vertikal"]
            break
    assert isinstance(descriptor, property)



def test_steuerung_is_not_abstract():
    assert not inspect.isabstract(Steuerung)


def test_steuerung_constructor_exists():
    assert callable(Steuerung.__init__)


def test_steuerung_constructor_args():
    sig = inspect.signature(Steuerung.__init__)
    params = list(sig.parameters.keys())



def test_turboliftsystem_is_not_abstract():
    assert not inspect.isabstract(TurboliftSystem)


def test_turboliftsystem_constructor_exists():
    assert callable(TurboliftSystem.__init__)


def test_turboliftsystem_constructor_args():
    sig = inspect.signature(TurboliftSystem.__init__)
    params = list(sig.parameters.keys())
    assert "alarmStufe" in params, "Missing parameter 'alarmStufe'"

def test_turboliftsystem_has_alarmStufe():
    assert hasattr(TurboliftSystem, "alarmStufe")
    descriptor = None
    for klass in TurboliftSystem.__mro__:
        if "alarmStufe" in klass.__dict__:
            descriptor = klass.__dict__["alarmStufe"]
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
BenannteEinrichtung_strategy = st.builds(
    BenannteEinrichtung,
    name=
        safe_text
)
Deck_strategy = st.builds(
    Deck,
    sektion=
        safe_text,
    fahrtWunsch=
        st.booleans()
)
Kabine_strategy = st.builds(
    Kabine,
    tuerZustand=
        st.booleans()
)
Antrieb_strategy = st.builds(
    Antrieb,
    aNTRIEBSART=
        safe_text
)
TurboliftSchacht_strategy = st.builds(
    TurboliftSchacht,
    vertikal=
        st.booleans()
)
Steuerung_strategy = st.builds(
    Steuerung,
)
TurboliftSystem_strategy = st.builds(
    TurboliftSystem,
    alarmStufe=
        st.integers()
)

@given(instance=BenannteEinrichtung_strategy)
@settings(max_examples=50)
def test_benannteeinrichtung_instantiation(instance):
    assert isinstance(instance, BenannteEinrichtung)



@given(instance=BenannteEinrichtung_strategy)
def test_benannteeinrichtung_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Deck_strategy)
@settings(max_examples=50)
def test_deck_instantiation(instance):
    assert isinstance(instance, Deck)



@given(instance=Deck_strategy)
def test_deck_sektion_setter(instance):
    original = instance.sektion
    instance.sektion = original
    assert instance.sektion == original



@given(instance=Deck_strategy)
def test_deck_fahrtWunsch_setter(instance):
    original = instance.fahrtWunsch
    instance.fahrtWunsch = original
    assert instance.fahrtWunsch == original

@given(instance=Kabine_strategy)
@settings(max_examples=50)
def test_kabine_instantiation(instance):
    assert isinstance(instance, Kabine)



@given(instance=Kabine_strategy)
def test_kabine_tuerZustand_setter(instance):
    original = instance.tuerZustand
    instance.tuerZustand = original
    assert instance.tuerZustand == original

@given(instance=Antrieb_strategy)
@settings(max_examples=50)
def test_antrieb_instantiation(instance):
    assert isinstance(instance, Antrieb)



@given(instance=Antrieb_strategy)
def test_antrieb_aNTRIEBSART_setter(instance):
    original = instance.aNTRIEBSART
    instance.aNTRIEBSART = original
    assert instance.aNTRIEBSART == original

@given(instance=TurboliftSchacht_strategy)
@settings(max_examples=50)
def test_turboliftschacht_instantiation(instance):
    assert isinstance(instance, TurboliftSchacht)



@given(instance=TurboliftSchacht_strategy)
def test_turboliftschacht_vertikal_setter(instance):
    original = instance.vertikal
    instance.vertikal = original
    assert instance.vertikal == original

@given(instance=Steuerung_strategy)
@settings(max_examples=50)
def test_steuerung_instantiation(instance):
    assert isinstance(instance, Steuerung)

@given(instance=TurboliftSystem_strategy)
@settings(max_examples=50)
def test_turboliftsystem_instantiation(instance):
    assert isinstance(instance, TurboliftSystem)



@given(instance=TurboliftSystem_strategy)
def test_turboliftsystem_alarmStufe_setter(instance):
    original = instance.alarmStufe
    instance.alarmStufe = original
    assert instance.alarmStufe == original
