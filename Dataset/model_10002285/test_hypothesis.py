import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Kupac,
    Osiguranje,
    Sme_taj,
    Aran_man,
    Putovanje,
    Korisnik_IS,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_kupac_is_not_abstract():
    assert not inspect.isabstract(Kupac)


def test_kupac_constructor_exists():
    assert callable(Kupac.__init__)


def test_kupac_constructor_args():
    sig = inspect.signature(Kupac.__init__)
    params = list(sig.parameters.keys())
    assert "OsigID" in params, "Missing parameter 'OsigID'"
    assert "eMail" in params, "Missing parameter 'eMail'"
    assert "PrezimeKup" in params, "Missing parameter 'PrezimeKup'"
    assert "ImeKup" in params, "Missing parameter 'ImeKup'"
    assert "JMBG" in params, "Missing parameter 'JMBG'"
    assert "Grad" in params, "Missing parameter 'Grad'"
    assert "KupacID" in params, "Missing parameter 'KupacID'"
    assert "Adresa" in params, "Missing parameter 'Adresa'"
    assert "Mobilni" in params, "Missing parameter 'Mobilni'"

def test_kupac_has_OsigID():
    assert hasattr(Kupac, "OsigID")
    descriptor = None
    for klass in Kupac.__mro__:
        if "OsigID" in klass.__dict__:
            descriptor = klass.__dict__["OsigID"]
            break
    assert isinstance(descriptor, property)

def test_kupac_has_eMail():
    assert hasattr(Kupac, "eMail")
    descriptor = None
    for klass in Kupac.__mro__:
        if "eMail" in klass.__dict__:
            descriptor = klass.__dict__["eMail"]
            break
    assert isinstance(descriptor, property)

def test_kupac_has_PrezimeKup():
    assert hasattr(Kupac, "PrezimeKup")
    descriptor = None
    for klass in Kupac.__mro__:
        if "PrezimeKup" in klass.__dict__:
            descriptor = klass.__dict__["PrezimeKup"]
            break
    assert isinstance(descriptor, property)

def test_kupac_has_ImeKup():
    assert hasattr(Kupac, "ImeKup")
    descriptor = None
    for klass in Kupac.__mro__:
        if "ImeKup" in klass.__dict__:
            descriptor = klass.__dict__["ImeKup"]
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

def test_kupac_has_Grad():
    assert hasattr(Kupac, "Grad")
    descriptor = None
    for klass in Kupac.__mro__:
        if "Grad" in klass.__dict__:
            descriptor = klass.__dict__["Grad"]
            break
    assert isinstance(descriptor, property)

def test_kupac_has_KupacID():
    assert hasattr(Kupac, "KupacID")
    descriptor = None
    for klass in Kupac.__mro__:
        if "KupacID" in klass.__dict__:
            descriptor = klass.__dict__["KupacID"]
            break
    assert isinstance(descriptor, property)

def test_kupac_has_Adresa():
    assert hasattr(Kupac, "Adresa")
    descriptor = None
    for klass in Kupac.__mro__:
        if "Adresa" in klass.__dict__:
            descriptor = klass.__dict__["Adresa"]
            break
    assert isinstance(descriptor, property)

def test_kupac_has_Mobilni():
    assert hasattr(Kupac, "Mobilni")
    descriptor = None
    for klass in Kupac.__mro__:
        if "Mobilni" in klass.__dict__:
            descriptor = klass.__dict__["Mobilni"]
            break
    assert isinstance(descriptor, property)



def test_osiguranje_is_not_abstract():
    assert not inspect.isabstract(Osiguranje)


def test_osiguranje_constructor_exists():
    assert callable(Osiguranje.__init__)


def test_osiguranje_constructor_args():
    sig = inspect.signature(Osiguranje.__init__)
    params = list(sig.parameters.keys())
    assert "PaketPokri_a" in params, "Missing parameter 'PaketPokri_a'"
    assert "OsigID" in params, "Missing parameter 'OsigID'"
    assert "KucaOsiguranje" in params, "Missing parameter 'KucaOsiguranje'"

def test_osiguranje_has_PaketPokri_a():
    assert hasattr(Osiguranje, "PaketPokri_a")
    descriptor = None
    for klass in Osiguranje.__mro__:
        if "PaketPokri_a" in klass.__dict__:
            descriptor = klass.__dict__["PaketPokri_a"]
            break
    assert isinstance(descriptor, property)

def test_osiguranje_has_OsigID():
    assert hasattr(Osiguranje, "OsigID")
    descriptor = None
    for klass in Osiguranje.__mro__:
        if "OsigID" in klass.__dict__:
            descriptor = klass.__dict__["OsigID"]
            break
    assert isinstance(descriptor, property)

def test_osiguranje_has_KucaOsiguranje():
    assert hasattr(Osiguranje, "KucaOsiguranje")
    descriptor = None
    for klass in Osiguranje.__mro__:
        if "KucaOsiguranje" in klass.__dict__:
            descriptor = klass.__dict__["KucaOsiguranje"]
            break
    assert isinstance(descriptor, property)



def test_sme_taj_is_not_abstract():
    assert not inspect.isabstract(Sme_taj)


def test_sme_taj_constructor_exists():
    assert callable(Sme_taj.__init__)


def test_sme_taj_constructor_args():
    sig = inspect.signature(Sme_taj.__init__)
    params = list(sig.parameters.keys())
    assert "LokacijaSme_taja" in params, "Missing parameter 'LokacijaSme_taja'"
    assert "PutovID" in params, "Missing parameter 'PutovID'"
    assert "CenaSmestaja" in params, "Missing parameter 'CenaSmestaja'"
    assert "UslugaSme_taja" in params, "Missing parameter 'UslugaSme_taja'"
    assert "DuzinaBoravka" in params, "Missing parameter 'DuzinaBoravka'"
    assert "ImeSme_taja" in params, "Missing parameter 'ImeSme_taja'"
    assert "Sme_tajID" in params, "Missing parameter 'Sme_tajID'"

def test_sme_taj_has_LokacijaSme_taja():
    assert hasattr(Sme_taj, "LokacijaSme_taja")
    descriptor = None
    for klass in Sme_taj.__mro__:
        if "LokacijaSme_taja" in klass.__dict__:
            descriptor = klass.__dict__["LokacijaSme_taja"]
            break
    assert isinstance(descriptor, property)

def test_sme_taj_has_PutovID():
    assert hasattr(Sme_taj, "PutovID")
    descriptor = None
    for klass in Sme_taj.__mro__:
        if "PutovID" in klass.__dict__:
            descriptor = klass.__dict__["PutovID"]
            break
    assert isinstance(descriptor, property)

def test_sme_taj_has_CenaSmestaja():
    assert hasattr(Sme_taj, "CenaSmestaja")
    descriptor = None
    for klass in Sme_taj.__mro__:
        if "CenaSmestaja" in klass.__dict__:
            descriptor = klass.__dict__["CenaSmestaja"]
            break
    assert isinstance(descriptor, property)

def test_sme_taj_has_UslugaSme_taja():
    assert hasattr(Sme_taj, "UslugaSme_taja")
    descriptor = None
    for klass in Sme_taj.__mro__:
        if "UslugaSme_taja" in klass.__dict__:
            descriptor = klass.__dict__["UslugaSme_taja"]
            break
    assert isinstance(descriptor, property)

def test_sme_taj_has_DuzinaBoravka():
    assert hasattr(Sme_taj, "DuzinaBoravka")
    descriptor = None
    for klass in Sme_taj.__mro__:
        if "DuzinaBoravka" in klass.__dict__:
            descriptor = klass.__dict__["DuzinaBoravka"]
            break
    assert isinstance(descriptor, property)

def test_sme_taj_has_ImeSme_taja():
    assert hasattr(Sme_taj, "ImeSme_taja")
    descriptor = None
    for klass in Sme_taj.__mro__:
        if "ImeSme_taja" in klass.__dict__:
            descriptor = klass.__dict__["ImeSme_taja"]
            break
    assert isinstance(descriptor, property)

def test_sme_taj_has_Sme_tajID():
    assert hasattr(Sme_taj, "Sme_tajID")
    descriptor = None
    for klass in Sme_taj.__mro__:
        if "Sme_tajID" in klass.__dict__:
            descriptor = klass.__dict__["Sme_tajID"]
            break
    assert isinstance(descriptor, property)



def test_aran_man_is_not_abstract():
    assert not inspect.isabstract(Aran_man)


def test_aran_man_constructor_exists():
    assert callable(Aran_man.__init__)


def test_aran_man_constructor_args():
    sig = inspect.signature(Aran_man.__init__)
    params = list(sig.parameters.keys())
    assert "KorisnikID" in params, "Missing parameter 'KorisnikID'"
    assert "Aran_manID" in params, "Missing parameter 'Aran_manID'"
    assert "DatumPolaska" in params, "Missing parameter 'DatumPolaska'"
    assert "KupacID" in params, "Missing parameter 'KupacID'"
    assert "DatumDolaska" in params, "Missing parameter 'DatumDolaska'"
    assert "SlobMesto" in params, "Missing parameter 'SlobMesto'"
    assert "PutovID" in params, "Missing parameter 'PutovID'"
    assert "Cena" in params, "Missing parameter 'Cena'"

def test_aran_man_has_KorisnikID():
    assert hasattr(Aran_man, "KorisnikID")
    descriptor = None
    for klass in Aran_man.__mro__:
        if "KorisnikID" in klass.__dict__:
            descriptor = klass.__dict__["KorisnikID"]
            break
    assert isinstance(descriptor, property)

def test_aran_man_has_Aran_manID():
    assert hasattr(Aran_man, "Aran_manID")
    descriptor = None
    for klass in Aran_man.__mro__:
        if "Aran_manID" in klass.__dict__:
            descriptor = klass.__dict__["Aran_manID"]
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

def test_aran_man_has_KupacID():
    assert hasattr(Aran_man, "KupacID")
    descriptor = None
    for klass in Aran_man.__mro__:
        if "KupacID" in klass.__dict__:
            descriptor = klass.__dict__["KupacID"]
            break
    assert isinstance(descriptor, property)

def test_aran_man_has_DatumDolaska():
    assert hasattr(Aran_man, "DatumDolaska")
    descriptor = None
    for klass in Aran_man.__mro__:
        if "DatumDolaska" in klass.__dict__:
            descriptor = klass.__dict__["DatumDolaska"]
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

def test_aran_man_has_PutovID():
    assert hasattr(Aran_man, "PutovID")
    descriptor = None
    for klass in Aran_man.__mro__:
        if "PutovID" in klass.__dict__:
            descriptor = klass.__dict__["PutovID"]
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



def test_putovanje_is_not_abstract():
    assert not inspect.isabstract(Putovanje)


def test_putovanje_constructor_exists():
    assert callable(Putovanje.__init__)


def test_putovanje_constructor_args():
    sig = inspect.signature(Putovanje.__init__)
    params = list(sig.parameters.keys())
    assert "Dr_ava" in params, "Missing parameter 'Dr_ava'"
    assert "PutovID" in params, "Missing parameter 'PutovID'"
    assert "Grad" in params, "Missing parameter 'Grad'"

def test_putovanje_has_Dr_ava():
    assert hasattr(Putovanje, "Dr_ava")
    descriptor = None
    for klass in Putovanje.__mro__:
        if "Dr_ava" in klass.__dict__:
            descriptor = klass.__dict__["Dr_ava"]
            break
    assert isinstance(descriptor, property)

def test_putovanje_has_PutovID():
    assert hasattr(Putovanje, "PutovID")
    descriptor = None
    for klass in Putovanje.__mro__:
        if "PutovID" in klass.__dict__:
            descriptor = klass.__dict__["PutovID"]
            break
    assert isinstance(descriptor, property)

def test_putovanje_has_Grad():
    assert hasattr(Putovanje, "Grad")
    descriptor = None
    for klass in Putovanje.__mro__:
        if "Grad" in klass.__dict__:
            descriptor = klass.__dict__["Grad"]
            break
    assert isinstance(descriptor, property)



def test_korisnik_is_is_not_abstract():
    assert not inspect.isabstract(Korisnik_IS)


def test_korisnik_is_constructor_exists():
    assert callable(Korisnik_IS.__init__)


def test_korisnik_is_constructor_args():
    sig = inspect.signature(Korisnik_IS.__init__)
    params = list(sig.parameters.keys())
    assert "Password" in params, "Missing parameter 'Password'"
    assert "ImeKorisnika" in params, "Missing parameter 'ImeKorisnika'"
    assert "PrezimeKorisnika" in params, "Missing parameter 'PrezimeKorisnika'"
    assert "UserName" in params, "Missing parameter 'UserName'"
    assert "KorisnikID" in params, "Missing parameter 'KorisnikID'"

def test_korisnik_is_has_Password():
    assert hasattr(Korisnik_IS, "Password")
    descriptor = None
    for klass in Korisnik_IS.__mro__:
        if "Password" in klass.__dict__:
            descriptor = klass.__dict__["Password"]
            break
    assert isinstance(descriptor, property)

def test_korisnik_is_has_ImeKorisnika():
    assert hasattr(Korisnik_IS, "ImeKorisnika")
    descriptor = None
    for klass in Korisnik_IS.__mro__:
        if "ImeKorisnika" in klass.__dict__:
            descriptor = klass.__dict__["ImeKorisnika"]
            break
    assert isinstance(descriptor, property)

def test_korisnik_is_has_PrezimeKorisnika():
    assert hasattr(Korisnik_IS, "PrezimeKorisnika")
    descriptor = None
    for klass in Korisnik_IS.__mro__:
        if "PrezimeKorisnika" in klass.__dict__:
            descriptor = klass.__dict__["PrezimeKorisnika"]
            break
    assert isinstance(descriptor, property)

def test_korisnik_is_has_UserName():
    assert hasattr(Korisnik_IS, "UserName")
    descriptor = None
    for klass in Korisnik_IS.__mro__:
        if "UserName" in klass.__dict__:
            descriptor = klass.__dict__["UserName"]
            break
    assert isinstance(descriptor, property)

def test_korisnik_is_has_KorisnikID():
    assert hasattr(Korisnik_IS, "KorisnikID")
    descriptor = None
    for klass in Korisnik_IS.__mro__:
        if "KorisnikID" in klass.__dict__:
            descriptor = klass.__dict__["KorisnikID"]
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
Kupac_strategy = st.builds(
    Kupac,
    OsigID=
        st.integers(),
    eMail=
        safe_text,
    PrezimeKup=
        safe_text,
    ImeKup=
        safe_text,
    JMBG=
        safe_text,
    Grad=
        safe_text,
    KupacID=
        st.integers(),
    Adresa=
        safe_text,
    Mobilni=
        st.integers()
)
Osiguranje_strategy = st.builds(
    Osiguranje,
    PaketPokri_a=
        safe_text,
    OsigID=
        st.integers(),
    KucaOsiguranje=
        safe_text
)
Sme_taj_strategy = st.builds(
    Sme_taj,
    LokacijaSme_taja=
        safe_text,
    PutovID=
        st.integers(),
    CenaSmestaja=
        safe_text,
    UslugaSme_taja=
        safe_text,
    DuzinaBoravka=
        st.integers(),
    ImeSme_taja=
        safe_text,
    Sme_tajID=
        st.integers()
)
Aran_man_strategy = st.builds(
    Aran_man,
    KorisnikID=
        st.integers(),
    Aran_manID=
        st.integers(),
    DatumPolaska=
        safe_text,
    KupacID=
        st.integers(),
    DatumDolaska=
        safe_text,
    SlobMesto=
        st.booleans(),
    PutovID=
        st.integers(),
    Cena=
        safe_text
)
Putovanje_strategy = st.builds(
    Putovanje,
    Dr_ava=
        safe_text,
    PutovID=
        st.integers(),
    Grad=
        safe_text
)
Korisnik_IS_strategy = st.builds(
    Korisnik_IS,
    Password=
        safe_text,
    ImeKorisnika=
        safe_text,
    PrezimeKorisnika=
        safe_text,
    UserName=
        safe_text,
    KorisnikID=
        st.integers()
)

@given(instance=Kupac_strategy)
@settings(max_examples=50)
def test_kupac_instantiation(instance):
    assert isinstance(instance, Kupac)



@given(instance=Kupac_strategy)
def test_kupac_OsigID_setter(instance):
    original = instance.OsigID
    instance.OsigID = original
    assert instance.OsigID == original



@given(instance=Kupac_strategy)
def test_kupac_eMail_setter(instance):
    original = instance.eMail
    instance.eMail = original
    assert instance.eMail == original



@given(instance=Kupac_strategy)
def test_kupac_PrezimeKup_setter(instance):
    original = instance.PrezimeKup
    instance.PrezimeKup = original
    assert instance.PrezimeKup == original



@given(instance=Kupac_strategy)
def test_kupac_ImeKup_setter(instance):
    original = instance.ImeKup
    instance.ImeKup = original
    assert instance.ImeKup == original



@given(instance=Kupac_strategy)
def test_kupac_JMBG_setter(instance):
    original = instance.JMBG
    instance.JMBG = original
    assert instance.JMBG == original



@given(instance=Kupac_strategy)
def test_kupac_Grad_setter(instance):
    original = instance.Grad
    instance.Grad = original
    assert instance.Grad == original



@given(instance=Kupac_strategy)
def test_kupac_KupacID_setter(instance):
    original = instance.KupacID
    instance.KupacID = original
    assert instance.KupacID == original



@given(instance=Kupac_strategy)
def test_kupac_Adresa_setter(instance):
    original = instance.Adresa
    instance.Adresa = original
    assert instance.Adresa == original



@given(instance=Kupac_strategy)
def test_kupac_Mobilni_setter(instance):
    original = instance.Mobilni
    instance.Mobilni = original
    assert instance.Mobilni == original

@given(instance=Osiguranje_strategy)
@settings(max_examples=50)
def test_osiguranje_instantiation(instance):
    assert isinstance(instance, Osiguranje)



@given(instance=Osiguranje_strategy)
def test_osiguranje_PaketPokri_a_setter(instance):
    original = instance.PaketPokri_a
    instance.PaketPokri_a = original
    assert instance.PaketPokri_a == original



@given(instance=Osiguranje_strategy)
def test_osiguranje_OsigID_setter(instance):
    original = instance.OsigID
    instance.OsigID = original
    assert instance.OsigID == original



@given(instance=Osiguranje_strategy)
def test_osiguranje_KucaOsiguranje_setter(instance):
    original = instance.KucaOsiguranje
    instance.KucaOsiguranje = original
    assert instance.KucaOsiguranje == original

@given(instance=Sme_taj_strategy)
@settings(max_examples=50)
def test_sme_taj_instantiation(instance):
    assert isinstance(instance, Sme_taj)



@given(instance=Sme_taj_strategy)
def test_sme_taj_LokacijaSme_taja_setter(instance):
    original = instance.LokacijaSme_taja
    instance.LokacijaSme_taja = original
    assert instance.LokacijaSme_taja == original



@given(instance=Sme_taj_strategy)
def test_sme_taj_PutovID_setter(instance):
    original = instance.PutovID
    instance.PutovID = original
    assert instance.PutovID == original



@given(instance=Sme_taj_strategy)
def test_sme_taj_CenaSmestaja_setter(instance):
    original = instance.CenaSmestaja
    instance.CenaSmestaja = original
    assert instance.CenaSmestaja == original



@given(instance=Sme_taj_strategy)
def test_sme_taj_UslugaSme_taja_setter(instance):
    original = instance.UslugaSme_taja
    instance.UslugaSme_taja = original
    assert instance.UslugaSme_taja == original



@given(instance=Sme_taj_strategy)
def test_sme_taj_DuzinaBoravka_setter(instance):
    original = instance.DuzinaBoravka
    instance.DuzinaBoravka = original
    assert instance.DuzinaBoravka == original



@given(instance=Sme_taj_strategy)
def test_sme_taj_ImeSme_taja_setter(instance):
    original = instance.ImeSme_taja
    instance.ImeSme_taja = original
    assert instance.ImeSme_taja == original



@given(instance=Sme_taj_strategy)
def test_sme_taj_Sme_tajID_setter(instance):
    original = instance.Sme_tajID
    instance.Sme_tajID = original
    assert instance.Sme_tajID == original

@given(instance=Aran_man_strategy)
@settings(max_examples=50)
def test_aran_man_instantiation(instance):
    assert isinstance(instance, Aran_man)



@given(instance=Aran_man_strategy)
def test_aran_man_KorisnikID_setter(instance):
    original = instance.KorisnikID
    instance.KorisnikID = original
    assert instance.KorisnikID == original



@given(instance=Aran_man_strategy)
def test_aran_man_Aran_manID_setter(instance):
    original = instance.Aran_manID
    instance.Aran_manID = original
    assert instance.Aran_manID == original



@given(instance=Aran_man_strategy)
def test_aran_man_DatumPolaska_setter(instance):
    original = instance.DatumPolaska
    instance.DatumPolaska = original
    assert instance.DatumPolaska == original



@given(instance=Aran_man_strategy)
def test_aran_man_KupacID_setter(instance):
    original = instance.KupacID
    instance.KupacID = original
    assert instance.KupacID == original



@given(instance=Aran_man_strategy)
def test_aran_man_DatumDolaska_setter(instance):
    original = instance.DatumDolaska
    instance.DatumDolaska = original
    assert instance.DatumDolaska == original



@given(instance=Aran_man_strategy)
def test_aran_man_SlobMesto_setter(instance):
    original = instance.SlobMesto
    instance.SlobMesto = original
    assert instance.SlobMesto == original



@given(instance=Aran_man_strategy)
def test_aran_man_PutovID_setter(instance):
    original = instance.PutovID
    instance.PutovID = original
    assert instance.PutovID == original



@given(instance=Aran_man_strategy)
def test_aran_man_Cena_setter(instance):
    original = instance.Cena
    instance.Cena = original
    assert instance.Cena == original

@given(instance=Putovanje_strategy)
@settings(max_examples=50)
def test_putovanje_instantiation(instance):
    assert isinstance(instance, Putovanje)



@given(instance=Putovanje_strategy)
def test_putovanje_Dr_ava_setter(instance):
    original = instance.Dr_ava
    instance.Dr_ava = original
    assert instance.Dr_ava == original



@given(instance=Putovanje_strategy)
def test_putovanje_PutovID_setter(instance):
    original = instance.PutovID
    instance.PutovID = original
    assert instance.PutovID == original



@given(instance=Putovanje_strategy)
def test_putovanje_Grad_setter(instance):
    original = instance.Grad
    instance.Grad = original
    assert instance.Grad == original

@given(instance=Korisnik_IS_strategy)
@settings(max_examples=50)
def test_korisnik_is_instantiation(instance):
    assert isinstance(instance, Korisnik_IS)



@given(instance=Korisnik_IS_strategy)
def test_korisnik_is_Password_setter(instance):
    original = instance.Password
    instance.Password = original
    assert instance.Password == original



@given(instance=Korisnik_IS_strategy)
def test_korisnik_is_ImeKorisnika_setter(instance):
    original = instance.ImeKorisnika
    instance.ImeKorisnika = original
    assert instance.ImeKorisnika == original



@given(instance=Korisnik_IS_strategy)
def test_korisnik_is_PrezimeKorisnika_setter(instance):
    original = instance.PrezimeKorisnika
    instance.PrezimeKorisnika = original
    assert instance.PrezimeKorisnika == original



@given(instance=Korisnik_IS_strategy)
def test_korisnik_is_UserName_setter(instance):
    original = instance.UserName
    instance.UserName = original
    assert instance.UserName == original



@given(instance=Korisnik_IS_strategy)
def test_korisnik_is_KorisnikID_setter(instance):
    original = instance.KorisnikID
    instance.KorisnikID = original
    assert instance.KorisnikID == original
