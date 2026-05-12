import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Transakcija,
    Kupac,
    Osiguranje,
    Aran_man,
    Agent,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_transakcija_is_not_abstract():
    assert not inspect.isabstract(Transakcija)


def test_transakcija_constructor_exists():
    assert callable(Transakcija.__init__)


def test_transakcija_constructor_args():
    sig = inspect.signature(Transakcija.__init__)
    params = list(sig.parameters.keys())
    assert "datum_trans" in params, "Missing parameter 'datum_trans'"
    assert "suma" in params, "Missing parameter 'suma'"
    assert "Trans_ID" in params, "Missing parameter 'Trans_ID'"
    assert "tip" in params, "Missing parameter 'tip'"

def test_transakcija_has_datum_trans():
    assert hasattr(Transakcija, "datum_trans")
    descriptor = None
    for klass in Transakcija.__mro__:
        if "datum_trans" in klass.__dict__:
            descriptor = klass.__dict__["datum_trans"]
            break
    assert isinstance(descriptor, property)

def test_transakcija_has_suma():
    assert hasattr(Transakcija, "suma")
    descriptor = None
    for klass in Transakcija.__mro__:
        if "suma" in klass.__dict__:
            descriptor = klass.__dict__["suma"]
            break
    assert isinstance(descriptor, property)

def test_transakcija_has_Trans_ID():
    assert hasattr(Transakcija, "Trans_ID")
    descriptor = None
    for klass in Transakcija.__mro__:
        if "Trans_ID" in klass.__dict__:
            descriptor = klass.__dict__["Trans_ID"]
            break
    assert isinstance(descriptor, property)

def test_transakcija_has_tip():
    assert hasattr(Transakcija, "tip")
    descriptor = None
    for klass in Transakcija.__mro__:
        if "tip" in klass.__dict__:
            descriptor = klass.__dict__["tip"]
            break
    assert isinstance(descriptor, property)



def test_kupac_is_not_abstract():
    assert not inspect.isabstract(Kupac)


def test_kupac_constructor_exists():
    assert callable(Kupac.__init__)


def test_kupac_constructor_args():
    sig = inspect.signature(Kupac.__init__)
    params = list(sig.parameters.keys())
    assert "Mobilni" in params, "Missing parameter 'Mobilni'"
    assert "BrojPasosa" in params, "Missing parameter 'BrojPasosa'"
    assert "Grad" in params, "Missing parameter 'Grad'"
    assert "Ime" in params, "Missing parameter 'Ime'"
    assert "Kupac_ID" in params, "Missing parameter 'Kupac_ID'"
    assert "Prezime" in params, "Missing parameter 'Prezime'"
    assert "JMBG" in params, "Missing parameter 'JMBG'"

def test_kupac_has_Mobilni():
    assert hasattr(Kupac, "Mobilni")
    descriptor = None
    for klass in Kupac.__mro__:
        if "Mobilni" in klass.__dict__:
            descriptor = klass.__dict__["Mobilni"]
            break
    assert isinstance(descriptor, property)

def test_kupac_has_BrojPasosa():
    assert hasattr(Kupac, "BrojPasosa")
    descriptor = None
    for klass in Kupac.__mro__:
        if "BrojPasosa" in klass.__dict__:
            descriptor = klass.__dict__["BrojPasosa"]
            break
    assert isinstance(descriptor, property)

def test_kupac_has_Grad():
    assert hasattr(Kupac, "Grad")
    descriptor = None
    for klass in Kupac.__mro__:
        if "Grad" in klass.__dict__:
            descriptor = klass.__dict__["Grad"]
            break
    assert isinstance(descriptor, property)

def test_kupac_has_Ime():
    assert hasattr(Kupac, "Ime")
    descriptor = None
    for klass in Kupac.__mro__:
        if "Ime" in klass.__dict__:
            descriptor = klass.__dict__["Ime"]
            break
    assert isinstance(descriptor, property)

def test_kupac_has_Kupac_ID():
    assert hasattr(Kupac, "Kupac_ID")
    descriptor = None
    for klass in Kupac.__mro__:
        if "Kupac_ID" in klass.__dict__:
            descriptor = klass.__dict__["Kupac_ID"]
            break
    assert isinstance(descriptor, property)

def test_kupac_has_Prezime():
    assert hasattr(Kupac, "Prezime")
    descriptor = None
    for klass in Kupac.__mro__:
        if "Prezime" in klass.__dict__:
            descriptor = klass.__dict__["Prezime"]
            break
    assert isinstance(descriptor, property)

def test_kupac_has_JMBG():
    assert hasattr(Kupac, "JMBG")
    descriptor = None
    for klass in Kupac.__mro__:
        if "JMBG" in klass.__dict__:
            descriptor = klass.__dict__["JMBG"]
            break
    assert isinstance(descriptor, property)



def test_osiguranje_is_not_abstract():
    assert not inspect.isabstract(Osiguranje)


def test_osiguranje_constructor_exists():
    assert callable(Osiguranje.__init__)


def test_osiguranje_constructor_args():
    sig = inspect.signature(Osiguranje.__init__)
    params = list(sig.parameters.keys())
    assert "BrojPolise" in params, "Missing parameter 'BrojPolise'"
    assert "Cena" in params, "Missing parameter 'Cena'"
    assert "OsigKuca" in params, "Missing parameter 'OsigKuca'"
    assert "PaketPokri_a" in params, "Missing parameter 'PaketPokri_a'"
    assert "Osiguranje_ID" in params, "Missing parameter 'Osiguranje_ID'"

def test_osiguranje_has_BrojPolise():
    assert hasattr(Osiguranje, "BrojPolise")
    descriptor = None
    for klass in Osiguranje.__mro__:
        if "BrojPolise" in klass.__dict__:
            descriptor = klass.__dict__["BrojPolise"]
            break
    assert isinstance(descriptor, property)

def test_osiguranje_has_Cena():
    assert hasattr(Osiguranje, "Cena")
    descriptor = None
    for klass in Osiguranje.__mro__:
        if "Cena" in klass.__dict__:
            descriptor = klass.__dict__["Cena"]
            break
    assert isinstance(descriptor, property)

def test_osiguranje_has_OsigKuca():
    assert hasattr(Osiguranje, "OsigKuca")
    descriptor = None
    for klass in Osiguranje.__mro__:
        if "OsigKuca" in klass.__dict__:
            descriptor = klass.__dict__["OsigKuca"]
            break
    assert isinstance(descriptor, property)

def test_osiguranje_has_PaketPokri_a():
    assert hasattr(Osiguranje, "PaketPokri_a")
    descriptor = None
    for klass in Osiguranje.__mro__:
        if "PaketPokri_a" in klass.__dict__:
            descriptor = klass.__dict__["PaketPokri_a"]
            break
    assert isinstance(descriptor, property)

def test_osiguranje_has_Osiguranje_ID():
    assert hasattr(Osiguranje, "Osiguranje_ID")
    descriptor = None
    for klass in Osiguranje.__mro__:
        if "Osiguranje_ID" in klass.__dict__:
            descriptor = klass.__dict__["Osiguranje_ID"]
            break
    assert isinstance(descriptor, property)



def test_aran_man_is_not_abstract():
    assert not inspect.isabstract(Aran_man)


def test_aran_man_constructor_exists():
    assert callable(Aran_man.__init__)


def test_aran_man_constructor_args():
    sig = inspect.signature(Aran_man.__init__)
    params = list(sig.parameters.keys())
    assert "NazivAran_" in params, "Missing parameter 'NazivAran_'"
    assert "DatumPolaska" in params, "Missing parameter 'DatumPolaska'"
    assert "DatumPovratka" in params, "Missing parameter 'DatumPovratka'"
    assert "Cena" in params, "Missing parameter 'Cena'"
    assert "Aranzman_ID" in params, "Missing parameter 'Aranzman_ID'"
    assert "SlobMesto" in params, "Missing parameter 'SlobMesto'"

def test_aran_man_has_NazivAran_():
    assert hasattr(Aran_man, "NazivAran_")
    descriptor = None
    for klass in Aran_man.__mro__:
        if "NazivAran_" in klass.__dict__:
            descriptor = klass.__dict__["NazivAran_"]
            break
    assert isinstance(descriptor, property)

def test_aran_man_has_DatumPolaska():
    assert hasattr(Aran_man, "DatumPolaska")
    descriptor = None
    for klass in Aran_man.__mro__:
        if "DatumPolaska" in klass.__dict__:
            descriptor = klass.__dict__["DatumPolaska"]
            break
    assert isinstance(descriptor, property)

def test_aran_man_has_DatumPovratka():
    assert hasattr(Aran_man, "DatumPovratka")
    descriptor = None
    for klass in Aran_man.__mro__:
        if "DatumPovratka" in klass.__dict__:
            descriptor = klass.__dict__["DatumPovratka"]
            break
    assert isinstance(descriptor, property)

def test_aran_man_has_Cena():
    assert hasattr(Aran_man, "Cena")
    descriptor = None
    for klass in Aran_man.__mro__:
        if "Cena" in klass.__dict__:
            descriptor = klass.__dict__["Cena"]
            break
    assert isinstance(descriptor, property)

def test_aran_man_has_Aranzman_ID():
    assert hasattr(Aran_man, "Aranzman_ID")
    descriptor = None
    for klass in Aran_man.__mro__:
        if "Aranzman_ID" in klass.__dict__:
            descriptor = klass.__dict__["Aranzman_ID"]
            break
    assert isinstance(descriptor, property)

def test_aran_man_has_SlobMesto():
    assert hasattr(Aran_man, "SlobMesto")
    descriptor = None
    for klass in Aran_man.__mro__:
        if "SlobMesto" in klass.__dict__:
            descriptor = klass.__dict__["SlobMesto"]
            break
    assert isinstance(descriptor, property)



def test_agent_is_not_abstract():
    assert not inspect.isabstract(Agent)


def test_agent_constructor_exists():
    assert callable(Agent.__init__)


def test_agent_constructor_args():
    sig = inspect.signature(Agent.__init__)
    params = list(sig.parameters.keys())
    assert "Ime" in params, "Missing parameter 'Ime'"
    assert "Agent_ID" in params, "Missing parameter 'Agent_ID'"
    assert "JMBG" in params, "Missing parameter 'JMBG'"
    assert "BrojAgenta" in params, "Missing parameter 'BrojAgenta'"
    assert "Prezime" in params, "Missing parameter 'Prezime'"

def test_agent_has_Ime():
    assert hasattr(Agent, "Ime")
    descriptor = None
    for klass in Agent.__mro__:
        if "Ime" in klass.__dict__:
            descriptor = klass.__dict__["Ime"]
            break
    assert isinstance(descriptor, property)

def test_agent_has_Agent_ID():
    assert hasattr(Agent, "Agent_ID")
    descriptor = None
    for klass in Agent.__mro__:
        if "Agent_ID" in klass.__dict__:
            descriptor = klass.__dict__["Agent_ID"]
            break
    assert isinstance(descriptor, property)

def test_agent_has_JMBG():
    assert hasattr(Agent, "JMBG")
    descriptor = None
    for klass in Agent.__mro__:
        if "JMBG" in klass.__dict__:
            descriptor = klass.__dict__["JMBG"]
            break
    assert isinstance(descriptor, property)

def test_agent_has_BrojAgenta():
    assert hasattr(Agent, "BrojAgenta")
    descriptor = None
    for klass in Agent.__mro__:
        if "BrojAgenta" in klass.__dict__:
            descriptor = klass.__dict__["BrojAgenta"]
            break
    assert isinstance(descriptor, property)

def test_agent_has_Prezime():
    assert hasattr(Agent, "Prezime")
    descriptor = None
    for klass in Agent.__mro__:
        if "Prezime" in klass.__dict__:
            descriptor = klass.__dict__["Prezime"]
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
Transakcija_strategy = st.builds(
    Transakcija,
    datum_trans=
        safe_text,
    suma=
        safe_text,
    Trans_ID=
        safe_text,
    tip=
        safe_text
)
Kupac_strategy = st.builds(
    Kupac,
    Mobilni=
        st.integers(),
    BrojPasosa=
        st.integers(),
    Grad=
        safe_text,
    Ime=
        safe_text,
    Kupac_ID=
        safe_text,
    Prezime=
        safe_text,
    JMBG=
        st.integers()
)
Osiguranje_strategy = st.builds(
    Osiguranje,
    BrojPolise=
        st.integers(),
    Cena=
        safe_text,
    OsigKuca=
        safe_text,
    PaketPokri_a=
        safe_text,
    Osiguranje_ID=
        safe_text
)
Aran_man_strategy = st.builds(
    Aran_man,
    NazivAran_=
        safe_text,
    DatumPolaska=
        safe_text,
    DatumPovratka=
        safe_text,
    Cena=
        safe_text,
    Aranzman_ID=
        safe_text,
    SlobMesto=
        st.booleans()
)
Agent_strategy = st.builds(
    Agent,
    Ime=
        safe_text,
    Agent_ID=
        safe_text,
    JMBG=
        st.integers(),
    BrojAgenta=
        st.integers(),
    Prezime=
        safe_text
)

@given(instance=Transakcija_strategy)
@settings(max_examples=50)
def test_transakcija_instantiation(instance):
    assert isinstance(instance, Transakcija)



@given(instance=Transakcija_strategy)
def test_transakcija_datum_trans_setter(instance):
    original = instance.datum_trans
    instance.datum_trans = original
    assert instance.datum_trans == original



@given(instance=Transakcija_strategy)
def test_transakcija_suma_setter(instance):
    original = instance.suma
    instance.suma = original
    assert instance.suma == original



@given(instance=Transakcija_strategy)
def test_transakcija_Trans_ID_setter(instance):
    original = instance.Trans_ID
    instance.Trans_ID = original
    assert instance.Trans_ID == original



@given(instance=Transakcija_strategy)
def test_transakcija_tip_setter(instance):
    original = instance.tip
    instance.tip = original
    assert instance.tip == original

@given(instance=Kupac_strategy)
@settings(max_examples=50)
def test_kupac_instantiation(instance):
    assert isinstance(instance, Kupac)



@given(instance=Kupac_strategy)
def test_kupac_Mobilni_setter(instance):
    original = instance.Mobilni
    instance.Mobilni = original
    assert instance.Mobilni == original



@given(instance=Kupac_strategy)
def test_kupac_BrojPasosa_setter(instance):
    original = instance.BrojPasosa
    instance.BrojPasosa = original
    assert instance.BrojPasosa == original



@given(instance=Kupac_strategy)
def test_kupac_Grad_setter(instance):
    original = instance.Grad
    instance.Grad = original
    assert instance.Grad == original



@given(instance=Kupac_strategy)
def test_kupac_Ime_setter(instance):
    original = instance.Ime
    instance.Ime = original
    assert instance.Ime == original



@given(instance=Kupac_strategy)
def test_kupac_Kupac_ID_setter(instance):
    original = instance.Kupac_ID
    instance.Kupac_ID = original
    assert instance.Kupac_ID == original



@given(instance=Kupac_strategy)
def test_kupac_Prezime_setter(instance):
    original = instance.Prezime
    instance.Prezime = original
    assert instance.Prezime == original



@given(instance=Kupac_strategy)
def test_kupac_JMBG_setter(instance):
    original = instance.JMBG
    instance.JMBG = original
    assert instance.JMBG == original

@given(instance=Osiguranje_strategy)
@settings(max_examples=50)
def test_osiguranje_instantiation(instance):
    assert isinstance(instance, Osiguranje)



@given(instance=Osiguranje_strategy)
def test_osiguranje_BrojPolise_setter(instance):
    original = instance.BrojPolise
    instance.BrojPolise = original
    assert instance.BrojPolise == original



@given(instance=Osiguranje_strategy)
def test_osiguranje_Cena_setter(instance):
    original = instance.Cena
    instance.Cena = original
    assert instance.Cena == original



@given(instance=Osiguranje_strategy)
def test_osiguranje_OsigKuca_setter(instance):
    original = instance.OsigKuca
    instance.OsigKuca = original
    assert instance.OsigKuca == original



@given(instance=Osiguranje_strategy)
def test_osiguranje_PaketPokri_a_setter(instance):
    original = instance.PaketPokri_a
    instance.PaketPokri_a = original
    assert instance.PaketPokri_a == original



@given(instance=Osiguranje_strategy)
def test_osiguranje_Osiguranje_ID_setter(instance):
    original = instance.Osiguranje_ID
    instance.Osiguranje_ID = original
    assert instance.Osiguranje_ID == original

@given(instance=Aran_man_strategy)
@settings(max_examples=50)
def test_aran_man_instantiation(instance):
    assert isinstance(instance, Aran_man)



@given(instance=Aran_man_strategy)
def test_aran_man_NazivAran__setter(instance):
    original = instance.NazivAran_
    instance.NazivAran_ = original
    assert instance.NazivAran_ == original



@given(instance=Aran_man_strategy)
def test_aran_man_DatumPolaska_setter(instance):
    original = instance.DatumPolaska
    instance.DatumPolaska = original
    assert instance.DatumPolaska == original



@given(instance=Aran_man_strategy)
def test_aran_man_DatumPovratka_setter(instance):
    original = instance.DatumPovratka
    instance.DatumPovratka = original
    assert instance.DatumPovratka == original



@given(instance=Aran_man_strategy)
def test_aran_man_Cena_setter(instance):
    original = instance.Cena
    instance.Cena = original
    assert instance.Cena == original



@given(instance=Aran_man_strategy)
def test_aran_man_Aranzman_ID_setter(instance):
    original = instance.Aranzman_ID
    instance.Aranzman_ID = original
    assert instance.Aranzman_ID == original



@given(instance=Aran_man_strategy)
def test_aran_man_SlobMesto_setter(instance):
    original = instance.SlobMesto
    instance.SlobMesto = original
    assert instance.SlobMesto == original

@given(instance=Agent_strategy)
@settings(max_examples=50)
def test_agent_instantiation(instance):
    assert isinstance(instance, Agent)



@given(instance=Agent_strategy)
def test_agent_Ime_setter(instance):
    original = instance.Ime
    instance.Ime = original
    assert instance.Ime == original



@given(instance=Agent_strategy)
def test_agent_Agent_ID_setter(instance):
    original = instance.Agent_ID
    instance.Agent_ID = original
    assert instance.Agent_ID == original



@given(instance=Agent_strategy)
def test_agent_JMBG_setter(instance):
    original = instance.JMBG
    instance.JMBG = original
    assert instance.JMBG == original



@given(instance=Agent_strategy)
def test_agent_BrojAgenta_setter(instance):
    original = instance.BrojAgenta
    instance.BrojAgenta = original
    assert instance.BrojAgenta == original



@given(instance=Agent_strategy)
def test_agent_Prezime_setter(instance):
    original = instance.Prezime
    instance.Prezime = original
    assert instance.Prezime == original
