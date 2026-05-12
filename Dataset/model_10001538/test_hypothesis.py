import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    zutaten,
    ea_helfer,
    backstrasse,
    auftrag,
    zutat,
    plaetzchen,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_zutaten_is_not_abstract():
    assert not inspect.isabstract(zutaten)


def test_zutaten_constructor_exists():
    assert callable(zutaten.__init__)


def test_zutaten_constructor_args():
    sig = inspect.signature(zutaten.__init__)
    params = list(sig.parameters.keys())
    assert "zutatenListe" in params, "Missing parameter 'zutatenListe'"

def test_zutaten_has_zutatenListe():
    assert hasattr(zutaten, "zutatenListe")
    descriptor = None
    for klass in zutaten.__mro__:
        if "zutatenListe" in klass.__dict__:
            descriptor = klass.__dict__["zutatenListe"]
            break
    assert isinstance(descriptor, property)



def test_ea_helfer_is_not_abstract():
    assert not inspect.isabstract(ea_helfer)


def test_ea_helfer_constructor_exists():
    assert callable(ea_helfer.__init__)


def test_ea_helfer_constructor_args():
    sig = inspect.signature(ea_helfer.__init__)
    params = list(sig.parameters.keys())



def test_backstrasse_is_not_abstract():
    assert not inspect.isabstract(backstrasse)


def test_backstrasse_constructor_exists():
    assert callable(backstrasse.__init__)


def test_backstrasse_constructor_args():
    sig = inspect.signature(backstrasse.__init__)
    params = list(sig.parameters.keys())
    assert "zutatenVorrat" in params, "Missing parameter 'zutatenVorrat'"
    assert "temperatur" in params, "Missing parameter 'temperatur'"
    assert "backAuftrag" in params, "Missing parameter 'backAuftrag'"
    assert "gestoppt" in params, "Missing parameter 'gestoppt'"
    assert "ofenlaenge" in params, "Missing parameter 'ofenlaenge'"
    assert "BLECHBREITE" in params, "Missing parameter 'BLECHBREITE'"
    assert "BLECHLAENGE" in params, "Missing parameter 'BLECHLAENGE'"
    assert "eingabeAusgabe" in params, "Missing parameter 'eingabeAusgabe'"
    assert "geschwindigkeit" in params, "Missing parameter 'geschwindigkeit'"

def test_backstrasse_has_zutatenVorrat():
    assert hasattr(backstrasse, "zutatenVorrat")
    descriptor = None
    for klass in backstrasse.__mro__:
        if "zutatenVorrat" in klass.__dict__:
            descriptor = klass.__dict__["zutatenVorrat"]
            break
    assert isinstance(descriptor, property)

def test_backstrasse_has_temperatur():
    assert hasattr(backstrasse, "temperatur")
    descriptor = None
    for klass in backstrasse.__mro__:
        if "temperatur" in klass.__dict__:
            descriptor = klass.__dict__["temperatur"]
            break
    assert isinstance(descriptor, property)

def test_backstrasse_has_backAuftrag():
    assert hasattr(backstrasse, "backAuftrag")
    descriptor = None
    for klass in backstrasse.__mro__:
        if "backAuftrag" in klass.__dict__:
            descriptor = klass.__dict__["backAuftrag"]
            break
    assert isinstance(descriptor, property)

def test_backstrasse_has_gestoppt():
    assert hasattr(backstrasse, "gestoppt")
    descriptor = None
    for klass in backstrasse.__mro__:
        if "gestoppt" in klass.__dict__:
            descriptor = klass.__dict__["gestoppt"]
            break
    assert isinstance(descriptor, property)

def test_backstrasse_has_ofenlaenge():
    assert hasattr(backstrasse, "ofenlaenge")
    descriptor = None
    for klass in backstrasse.__mro__:
        if "ofenlaenge" in klass.__dict__:
            descriptor = klass.__dict__["ofenlaenge"]
            break
    assert isinstance(descriptor, property)

def test_backstrasse_has_BLECHBREITE():
    assert hasattr(backstrasse, "BLECHBREITE")
    descriptor = None
    for klass in backstrasse.__mro__:
        if "BLECHBREITE" in klass.__dict__:
            descriptor = klass.__dict__["BLECHBREITE"]
            break
    assert isinstance(descriptor, property)

def test_backstrasse_has_BLECHLAENGE():
    assert hasattr(backstrasse, "BLECHLAENGE")
    descriptor = None
    for klass in backstrasse.__mro__:
        if "BLECHLAENGE" in klass.__dict__:
            descriptor = klass.__dict__["BLECHLAENGE"]
            break
    assert isinstance(descriptor, property)

def test_backstrasse_has_eingabeAusgabe():
    assert hasattr(backstrasse, "eingabeAusgabe")
    descriptor = None
    for klass in backstrasse.__mro__:
        if "eingabeAusgabe" in klass.__dict__:
            descriptor = klass.__dict__["eingabeAusgabe"]
            break
    assert isinstance(descriptor, property)

def test_backstrasse_has_geschwindigkeit():
    assert hasattr(backstrasse, "geschwindigkeit")
    descriptor = None
    for klass in backstrasse.__mro__:
        if "geschwindigkeit" in klass.__dict__:
            descriptor = klass.__dict__["geschwindigkeit"]
            break
    assert isinstance(descriptor, property)



def test_auftrag_is_not_abstract():
    assert not inspect.isabstract(auftrag)


def test_auftrag_constructor_exists():
    assert callable(auftrag.__init__)


def test_auftrag_constructor_args():
    sig = inspect.signature(auftrag.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "anzahl" in params, "Missing parameter 'anzahl'"
    assert "auftragsPlaetzchen" in params, "Missing parameter 'auftragsPlaetzchen'"

def test_auftrag_has_name():
    assert hasattr(auftrag, "name")
    descriptor = None
    for klass in auftrag.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_auftrag_has_anzahl():
    assert hasattr(auftrag, "anzahl")
    descriptor = None
    for klass in auftrag.__mro__:
        if "anzahl" in klass.__dict__:
            descriptor = klass.__dict__["anzahl"]
            break
    assert isinstance(descriptor, property)

def test_auftrag_has_auftragsPlaetzchen():
    assert hasattr(auftrag, "auftragsPlaetzchen")
    descriptor = None
    for klass in auftrag.__mro__:
        if "auftragsPlaetzchen" in klass.__dict__:
            descriptor = klass.__dict__["auftragsPlaetzchen"]
            break
    assert isinstance(descriptor, property)



def test_zutat_is_not_abstract():
    assert not inspect.isabstract(zutat)


def test_zutat_constructor_exists():
    assert callable(zutat.__init__)


def test_zutat_constructor_args():
    sig = inspect.signature(zutat.__init__)
    params = list(sig.parameters.keys())
    assert "einheit" in params, "Missing parameter 'einheit'"
    assert "name" in params, "Missing parameter 'name'"
    assert "menge" in params, "Missing parameter 'menge'"

def test_zutat_has_einheit():
    assert hasattr(zutat, "einheit")
    descriptor = None
    for klass in zutat.__mro__:
        if "einheit" in klass.__dict__:
            descriptor = klass.__dict__["einheit"]
            break
    assert isinstance(descriptor, property)

def test_zutat_has_name():
    assert hasattr(zutat, "name")
    descriptor = None
    for klass in zutat.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_zutat_has_menge():
    assert hasattr(zutat, "menge")
    descriptor = None
    for klass in zutat.__mro__:
        if "menge" in klass.__dict__:
            descriptor = klass.__dict__["menge"]
            break
    assert isinstance(descriptor, property)



def test_plaetzchen_is_not_abstract():
    assert not inspect.isabstract(plaetzchen)


def test_plaetzchen_constructor_exists():
    assert callable(plaetzchen.__init__)


def test_plaetzchen_constructor_args():
    sig = inspect.signature(plaetzchen.__init__)
    params = list(sig.parameters.keys())
    assert "breite" in params, "Missing parameter 'breite'"
    assert "form" in params, "Missing parameter 'form'"
    assert "temperatur" in params, "Missing parameter 'temperatur'"
    assert "laenge" in params, "Missing parameter 'laenge'"
    assert "belag" in params, "Missing parameter 'belag'"
    assert "teig" in params, "Missing parameter 'teig'"
    assert "backzeit" in params, "Missing parameter 'backzeit'"

def test_plaetzchen_has_breite():
    assert hasattr(plaetzchen, "breite")
    descriptor = None
    for klass in plaetzchen.__mro__:
        if "breite" in klass.__dict__:
            descriptor = klass.__dict__["breite"]
            break
    assert isinstance(descriptor, property)

def test_plaetzchen_has_form():
    assert hasattr(plaetzchen, "form")
    descriptor = None
    for klass in plaetzchen.__mro__:
        if "form" in klass.__dict__:
            descriptor = klass.__dict__["form"]
            break
    assert isinstance(descriptor, property)

def test_plaetzchen_has_temperatur():
    assert hasattr(plaetzchen, "temperatur")
    descriptor = None
    for klass in plaetzchen.__mro__:
        if "temperatur" in klass.__dict__:
            descriptor = klass.__dict__["temperatur"]
            break
    assert isinstance(descriptor, property)

def test_plaetzchen_has_laenge():
    assert hasattr(plaetzchen, "laenge")
    descriptor = None
    for klass in plaetzchen.__mro__:
        if "laenge" in klass.__dict__:
            descriptor = klass.__dict__["laenge"]
            break
    assert isinstance(descriptor, property)

def test_plaetzchen_has_belag():
    assert hasattr(plaetzchen, "belag")
    descriptor = None
    for klass in plaetzchen.__mro__:
        if "belag" in klass.__dict__:
            descriptor = klass.__dict__["belag"]
            break
    assert isinstance(descriptor, property)

def test_plaetzchen_has_teig():
    assert hasattr(plaetzchen, "teig")
    descriptor = None
    for klass in plaetzchen.__mro__:
        if "teig" in klass.__dict__:
            descriptor = klass.__dict__["teig"]
            break
    assert isinstance(descriptor, property)

def test_plaetzchen_has_backzeit():
    assert hasattr(plaetzchen, "backzeit")
    descriptor = None
    for klass in plaetzchen.__mro__:
        if "backzeit" in klass.__dict__:
            descriptor = klass.__dict__["backzeit"]
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
zutaten_strategy = st.builds(
    zutaten,
    zutatenListe=
        safe_text
)
ea_helfer_strategy = st.builds(
    ea_helfer,
)
backstrasse_strategy = st.builds(
    backstrasse,
    zutatenVorrat=
        safe_text,
    temperatur=
        safe_text,
    backAuftrag=
        safe_text,
    gestoppt=
        safe_text,
    ofenlaenge=
        safe_text,
    BLECHBREITE=
        safe_text,
    BLECHLAENGE=
        safe_text,
    eingabeAusgabe=
        safe_text,
    geschwindigkeit=
        safe_text
)
auftrag_strategy = st.builds(
    auftrag,
    name=
        safe_text,
    anzahl=
        safe_text,
    auftragsPlaetzchen=
        safe_text
)
zutat_strategy = st.builds(
    zutat,
    einheit=
        safe_text,
    name=
        safe_text,
    menge=
        safe_text
)
plaetzchen_strategy = st.builds(
    plaetzchen,
    breite=
        safe_text,
    form=
        safe_text,
    temperatur=
        safe_text,
    laenge=
        safe_text,
    belag=
        safe_text,
    teig=
        safe_text,
    backzeit=
        safe_text
)

@given(instance=zutaten_strategy)
@settings(max_examples=50)
def test_zutaten_instantiation(instance):
    assert isinstance(instance, zutaten)



@given(instance=zutaten_strategy)
def test_zutaten_zutatenListe_setter(instance):
    original = instance.zutatenListe
    instance.zutatenListe = original
    assert instance.zutatenListe == original

@given(instance=ea_helfer_strategy)
@settings(max_examples=50)
def test_ea_helfer_instantiation(instance):
    assert isinstance(instance, ea_helfer)

@given(instance=backstrasse_strategy)
@settings(max_examples=50)
def test_backstrasse_instantiation(instance):
    assert isinstance(instance, backstrasse)



@given(instance=backstrasse_strategy)
def test_backstrasse_zutatenVorrat_setter(instance):
    original = instance.zutatenVorrat
    instance.zutatenVorrat = original
    assert instance.zutatenVorrat == original



@given(instance=backstrasse_strategy)
def test_backstrasse_temperatur_setter(instance):
    original = instance.temperatur
    instance.temperatur = original
    assert instance.temperatur == original



@given(instance=backstrasse_strategy)
def test_backstrasse_backAuftrag_setter(instance):
    original = instance.backAuftrag
    instance.backAuftrag = original
    assert instance.backAuftrag == original



@given(instance=backstrasse_strategy)
def test_backstrasse_gestoppt_setter(instance):
    original = instance.gestoppt
    instance.gestoppt = original
    assert instance.gestoppt == original



@given(instance=backstrasse_strategy)
def test_backstrasse_ofenlaenge_setter(instance):
    original = instance.ofenlaenge
    instance.ofenlaenge = original
    assert instance.ofenlaenge == original



@given(instance=backstrasse_strategy)
def test_backstrasse_BLECHBREITE_setter(instance):
    original = instance.BLECHBREITE
    instance.BLECHBREITE = original
    assert instance.BLECHBREITE == original



@given(instance=backstrasse_strategy)
def test_backstrasse_BLECHLAENGE_setter(instance):
    original = instance.BLECHLAENGE
    instance.BLECHLAENGE = original
    assert instance.BLECHLAENGE == original



@given(instance=backstrasse_strategy)
def test_backstrasse_eingabeAusgabe_setter(instance):
    original = instance.eingabeAusgabe
    instance.eingabeAusgabe = original
    assert instance.eingabeAusgabe == original



@given(instance=backstrasse_strategy)
def test_backstrasse_geschwindigkeit_setter(instance):
    original = instance.geschwindigkeit
    instance.geschwindigkeit = original
    assert instance.geschwindigkeit == original

@given(instance=auftrag_strategy)
@settings(max_examples=50)
def test_auftrag_instantiation(instance):
    assert isinstance(instance, auftrag)



@given(instance=auftrag_strategy)
def test_auftrag_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=auftrag_strategy)
def test_auftrag_anzahl_setter(instance):
    original = instance.anzahl
    instance.anzahl = original
    assert instance.anzahl == original



@given(instance=auftrag_strategy)
def test_auftrag_auftragsPlaetzchen_setter(instance):
    original = instance.auftragsPlaetzchen
    instance.auftragsPlaetzchen = original
    assert instance.auftragsPlaetzchen == original

@given(instance=zutat_strategy)
@settings(max_examples=50)
def test_zutat_instantiation(instance):
    assert isinstance(instance, zutat)



@given(instance=zutat_strategy)
def test_zutat_einheit_setter(instance):
    original = instance.einheit
    instance.einheit = original
    assert instance.einheit == original



@given(instance=zutat_strategy)
def test_zutat_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=zutat_strategy)
def test_zutat_menge_setter(instance):
    original = instance.menge
    instance.menge = original
    assert instance.menge == original

@given(instance=plaetzchen_strategy)
@settings(max_examples=50)
def test_plaetzchen_instantiation(instance):
    assert isinstance(instance, plaetzchen)



@given(instance=plaetzchen_strategy)
def test_plaetzchen_breite_setter(instance):
    original = instance.breite
    instance.breite = original
    assert instance.breite == original



@given(instance=plaetzchen_strategy)
def test_plaetzchen_form_setter(instance):
    original = instance.form
    instance.form = original
    assert instance.form == original



@given(instance=plaetzchen_strategy)
def test_plaetzchen_temperatur_setter(instance):
    original = instance.temperatur
    instance.temperatur = original
    assert instance.temperatur == original



@given(instance=plaetzchen_strategy)
def test_plaetzchen_laenge_setter(instance):
    original = instance.laenge
    instance.laenge = original
    assert instance.laenge == original



@given(instance=plaetzchen_strategy)
def test_plaetzchen_belag_setter(instance):
    original = instance.belag
    instance.belag = original
    assert instance.belag == original



@given(instance=plaetzchen_strategy)
def test_plaetzchen_teig_setter(instance):
    original = instance.teig
    instance.teig = original
    assert instance.teig == original



@given(instance=plaetzchen_strategy)
def test_plaetzchen_backzeit_setter(instance):
    original = instance.backzeit
    instance.backzeit = original
    assert instance.backzeit == original
