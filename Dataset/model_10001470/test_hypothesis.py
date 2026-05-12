import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Putnik,
    string,
    Destinacija,
    Double,
    Date,
    Racun,
    Termin,
    Osiguranje,
    Aranzman,
    Agent,
    Rezervacija,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_putnik_is_not_abstract():
    assert not inspect.isabstract(Putnik)


def test_putnik_constructor_exists():
    assert callable(Putnik.__init__)


def test_putnik_constructor_args():
    sig = inspect.signature(Putnik.__init__)
    params = list(sig.parameters.keys())
    assert "Grad" in params, "Missing parameter 'Grad'"
    assert "PutnikID" in params, "Missing parameter 'PutnikID'"
    assert "Email" in params, "Missing parameter 'Email'"
    assert "ImePutnik" in params, "Missing parameter 'ImePutnik'"
    assert "BrojTel" in params, "Missing parameter 'BrojTel'"
    assert "JMBG" in params, "Missing parameter 'JMBG'"
    assert "OsiguranjeID" in params, "Missing parameter 'OsiguranjeID'"
    assert "PrezimePutnik" in params, "Missing parameter 'PrezimePutnik'"
    assert "Adresa" in params, "Missing parameter 'Adresa'"

def test_putnik_has_Grad():
    assert hasattr(Putnik, "Grad")
    descriptor = None
    for klass in Putnik.__mro__:
        if "Grad" in klass.__dict__:
            descriptor = klass.__dict__["Grad"]
            break
    assert isinstance(descriptor, property)

def test_putnik_has_PutnikID():
    assert hasattr(Putnik, "PutnikID")
    descriptor = None
    for klass in Putnik.__mro__:
        if "PutnikID" in klass.__dict__:
            descriptor = klass.__dict__["PutnikID"]
            break
    assert isinstance(descriptor, property)

def test_putnik_has_Email():
    assert hasattr(Putnik, "Email")
    descriptor = None
    for klass in Putnik.__mro__:
        if "Email" in klass.__dict__:
            descriptor = klass.__dict__["Email"]
            break
    assert isinstance(descriptor, property)

def test_putnik_has_ImePutnik():
    assert hasattr(Putnik, "ImePutnik")
    descriptor = None
    for klass in Putnik.__mro__:
        if "ImePutnik" in klass.__dict__:
            descriptor = klass.__dict__["ImePutnik"]
            break
    assert isinstance(descriptor, property)

def test_putnik_has_BrojTel():
    assert hasattr(Putnik, "BrojTel")
    descriptor = None
    for klass in Putnik.__mro__:
        if "BrojTel" in klass.__dict__:
            descriptor = klass.__dict__["BrojTel"]
            break
    assert isinstance(descriptor, property)

def test_putnik_has_JMBG():
    assert hasattr(Putnik, "JMBG")
    descriptor = None
    for klass in Putnik.__mro__:
        if "JMBG" in klass.__dict__:
            descriptor = klass.__dict__["JMBG"]
            break
    assert isinstance(descriptor, property)

def test_putnik_has_OsiguranjeID():
    assert hasattr(Putnik, "OsiguranjeID")
    descriptor = None
    for klass in Putnik.__mro__:
        if "OsiguranjeID" in klass.__dict__:
            descriptor = klass.__dict__["OsiguranjeID"]
            break
    assert isinstance(descriptor, property)

def test_putnik_has_PrezimePutnik():
    assert hasattr(Putnik, "PrezimePutnik")
    descriptor = None
    for klass in Putnik.__mro__:
        if "PrezimePutnik" in klass.__dict__:
            descriptor = klass.__dict__["PrezimePutnik"]
            break
    assert isinstance(descriptor, property)

def test_putnik_has_Adresa():
    assert hasattr(Putnik, "Adresa")
    descriptor = None
    for klass in Putnik.__mro__:
        if "Adresa" in klass.__dict__:
            descriptor = klass.__dict__["Adresa"]
            break
    assert isinstance(descriptor, property)



def test_string_is_not_abstract():
    assert not inspect.isabstract(string)


def test_string_constructor_exists():
    assert callable(string.__init__)


def test_string_constructor_args():
    sig = inspect.signature(string.__init__)
    params = list(sig.parameters.keys())



def test_destinacija_is_not_abstract():
    assert not inspect.isabstract(Destinacija)


def test_destinacija_constructor_exists():
    assert callable(Destinacija.__init__)


def test_destinacija_constructor_args():
    sig = inspect.signature(Destinacija.__init__)
    params = list(sig.parameters.keys())
    assert "Drzava" in params, "Missing parameter 'Drzava'"
    assert "Grad" in params, "Missing parameter 'Grad'"
    assert "Hotel" in params, "Missing parameter 'Hotel'"
    assert "DestinacijaID" in params, "Missing parameter 'DestinacijaID'"

def test_destinacija_has_Drzava():
    assert hasattr(Destinacija, "Drzava")
    descriptor = None
    for klass in Destinacija.__mro__:
        if "Drzava" in klass.__dict__:
            descriptor = klass.__dict__["Drzava"]
            break
    assert isinstance(descriptor, property)

def test_destinacija_has_Grad():
    assert hasattr(Destinacija, "Grad")
    descriptor = None
    for klass in Destinacija.__mro__:
        if "Grad" in klass.__dict__:
            descriptor = klass.__dict__["Grad"]
            break
    assert isinstance(descriptor, property)

def test_destinacija_has_Hotel():
    assert hasattr(Destinacija, "Hotel")
    descriptor = None
    for klass in Destinacija.__mro__:
        if "Hotel" in klass.__dict__:
            descriptor = klass.__dict__["Hotel"]
            break
    assert isinstance(descriptor, property)

def test_destinacija_has_DestinacijaID():
    assert hasattr(Destinacija, "DestinacijaID")
    descriptor = None
    for klass in Destinacija.__mro__:
        if "DestinacijaID" in klass.__dict__:
            descriptor = klass.__dict__["DestinacijaID"]
            break
    assert isinstance(descriptor, property)



def test_double_is_not_abstract():
    assert not inspect.isabstract(Double)


def test_double_constructor_exists():
    assert callable(Double.__init__)


def test_double_constructor_args():
    sig = inspect.signature(Double.__init__)
    params = list(sig.parameters.keys())



def test_date_is_not_abstract():
    assert not inspect.isabstract(Date)


def test_date_constructor_exists():
    assert callable(Date.__init__)


def test_date_constructor_args():
    sig = inspect.signature(Date.__init__)
    params = list(sig.parameters.keys())



def test_racun_is_not_abstract():
    assert not inspect.isabstract(Racun)


def test_racun_constructor_exists():
    assert callable(Racun.__init__)


def test_racun_constructor_args():
    sig = inspect.signature(Racun.__init__)
    params = list(sig.parameters.keys())
    assert "Placeno" in params, "Missing parameter 'Placeno'"
    assert "Iznos" in params, "Missing parameter 'Iznos'"
    assert "RacunID" in params, "Missing parameter 'RacunID'"

def test_racun_has_Placeno():
    assert hasattr(Racun, "Placeno")
    descriptor = None
    for klass in Racun.__mro__:
        if "Placeno" in klass.__dict__:
            descriptor = klass.__dict__["Placeno"]
            break
    assert isinstance(descriptor, property)

def test_racun_has_Iznos():
    assert hasattr(Racun, "Iznos")
    descriptor = None
    for klass in Racun.__mro__:
        if "Iznos" in klass.__dict__:
            descriptor = klass.__dict__["Iznos"]
            break
    assert isinstance(descriptor, property)

def test_racun_has_RacunID():
    assert hasattr(Racun, "RacunID")
    descriptor = None
    for klass in Racun.__mro__:
        if "RacunID" in klass.__dict__:
            descriptor = klass.__dict__["RacunID"]
            break
    assert isinstance(descriptor, property)



def test_termin_is_not_abstract():
    assert not inspect.isabstract(Termin)


def test_termin_constructor_exists():
    assert callable(Termin.__init__)


def test_termin_constructor_args():
    sig = inspect.signature(Termin.__init__)
    params = list(sig.parameters.keys())
    assert "DatumPovratka" in params, "Missing parameter 'DatumPovratka'"
    assert "DatumPolaska" in params, "Missing parameter 'DatumPolaska'"
    assert "TerminID" in params, "Missing parameter 'TerminID'"

def test_termin_has_DatumPovratka():
    assert hasattr(Termin, "DatumPovratka")
    descriptor = None
    for klass in Termin.__mro__:
        if "DatumPovratka" in klass.__dict__:
            descriptor = klass.__dict__["DatumPovratka"]
            break
    assert isinstance(descriptor, property)

def test_termin_has_DatumPolaska():
    assert hasattr(Termin, "DatumPolaska")
    descriptor = None
    for klass in Termin.__mro__:
        if "DatumPolaska" in klass.__dict__:
            descriptor = klass.__dict__["DatumPolaska"]
            break
    assert isinstance(descriptor, property)

def test_termin_has_TerminID():
    assert hasattr(Termin, "TerminID")
    descriptor = None
    for klass in Termin.__mro__:
        if "TerminID" in klass.__dict__:
            descriptor = klass.__dict__["TerminID"]
            break
    assert isinstance(descriptor, property)



def test_osiguranje_is_not_abstract():
    assert not inspect.isabstract(Osiguranje)


def test_osiguranje_constructor_exists():
    assert callable(Osiguranje.__init__)


def test_osiguranje_constructor_args():
    sig = inspect.signature(Osiguranje.__init__)
    params = list(sig.parameters.keys())
    assert "OsiguranjeID" in params, "Missing parameter 'OsiguranjeID'"
    assert "OsigurKuca" in params, "Missing parameter 'OsigurKuca'"

def test_osiguranje_has_OsiguranjeID():
    assert hasattr(Osiguranje, "OsiguranjeID")
    descriptor = None
    for klass in Osiguranje.__mro__:
        if "OsiguranjeID" in klass.__dict__:
            descriptor = klass.__dict__["OsiguranjeID"]
            break
    assert isinstance(descriptor, property)

def test_osiguranje_has_OsigurKuca():
    assert hasattr(Osiguranje, "OsigurKuca")
    descriptor = None
    for klass in Osiguranje.__mro__:
        if "OsigurKuca" in klass.__dict__:
            descriptor = klass.__dict__["OsigurKuca"]
            break
    assert isinstance(descriptor, property)



def test_aranzman_is_not_abstract():
    assert not inspect.isabstract(Aranzman)


def test_aranzman_constructor_exists():
    assert callable(Aranzman.__init__)


def test_aranzman_constructor_args():
    sig = inspect.signature(Aranzman.__init__)
    params = list(sig.parameters.keys())
    assert "TerminID" in params, "Missing parameter 'TerminID'"
    assert "Popunjeno" in params, "Missing parameter 'Popunjeno'"
    assert "DestinacijaID" in params, "Missing parameter 'DestinacijaID'"
    assert "AranzmanID" in params, "Missing parameter 'AranzmanID'"
    assert "BrojMesta" in params, "Missing parameter 'BrojMesta'"
    assert "NazivAranzmana" in params, "Missing parameter 'NazivAranzmana'"
    assert "Cena" in params, "Missing parameter 'Cena'"

def test_aranzman_has_TerminID():
    assert hasattr(Aranzman, "TerminID")
    descriptor = None
    for klass in Aranzman.__mro__:
        if "TerminID" in klass.__dict__:
            descriptor = klass.__dict__["TerminID"]
            break
    assert isinstance(descriptor, property)

def test_aranzman_has_Popunjeno():
    assert hasattr(Aranzman, "Popunjeno")
    descriptor = None
    for klass in Aranzman.__mro__:
        if "Popunjeno" in klass.__dict__:
            descriptor = klass.__dict__["Popunjeno"]
            break
    assert isinstance(descriptor, property)

def test_aranzman_has_DestinacijaID():
    assert hasattr(Aranzman, "DestinacijaID")
    descriptor = None
    for klass in Aranzman.__mro__:
        if "DestinacijaID" in klass.__dict__:
            descriptor = klass.__dict__["DestinacijaID"]
            break
    assert isinstance(descriptor, property)

def test_aranzman_has_AranzmanID():
    assert hasattr(Aranzman, "AranzmanID")
    descriptor = None
    for klass in Aranzman.__mro__:
        if "AranzmanID" in klass.__dict__:
            descriptor = klass.__dict__["AranzmanID"]
            break
    assert isinstance(descriptor, property)

def test_aranzman_has_BrojMesta():
    assert hasattr(Aranzman, "BrojMesta")
    descriptor = None
    for klass in Aranzman.__mro__:
        if "BrojMesta" in klass.__dict__:
            descriptor = klass.__dict__["BrojMesta"]
            break
    assert isinstance(descriptor, property)

def test_aranzman_has_NazivAranzmana():
    assert hasattr(Aranzman, "NazivAranzmana")
    descriptor = None
    for klass in Aranzman.__mro__:
        if "NazivAranzmana" in klass.__dict__:
            descriptor = klass.__dict__["NazivAranzmana"]
            break
    assert isinstance(descriptor, property)

def test_aranzman_has_Cena():
    assert hasattr(Aranzman, "Cena")
    descriptor = None
    for klass in Aranzman.__mro__:
        if "Cena" in klass.__dict__:
            descriptor = klass.__dict__["Cena"]
            break
    assert isinstance(descriptor, property)



def test_agent_is_not_abstract():
    assert not inspect.isabstract(Agent)


def test_agent_constructor_exists():
    assert callable(Agent.__init__)


def test_agent_constructor_args():
    sig = inspect.signature(Agent.__init__)
    params = list(sig.parameters.keys())
    assert "ImeAgent" in params, "Missing parameter 'ImeAgent'"
    assert "BrojTele" in params, "Missing parameter 'BrojTele'"
    assert "PrezimeAgent" in params, "Missing parameter 'PrezimeAgent'"
    assert "Password" in params, "Missing parameter 'Password'"
    assert "Username" in params, "Missing parameter 'Username'"
    assert "Email" in params, "Missing parameter 'Email'"
    assert "AgentID" in params, "Missing parameter 'AgentID'"

def test_agent_has_ImeAgent():
    assert hasattr(Agent, "ImeAgent")
    descriptor = None
    for klass in Agent.__mro__:
        if "ImeAgent" in klass.__dict__:
            descriptor = klass.__dict__["ImeAgent"]
            break
    assert isinstance(descriptor, property)

def test_agent_has_BrojTele():
    assert hasattr(Agent, "BrojTele")
    descriptor = None
    for klass in Agent.__mro__:
        if "BrojTele" in klass.__dict__:
            descriptor = klass.__dict__["BrojTele"]
            break
    assert isinstance(descriptor, property)

def test_agent_has_PrezimeAgent():
    assert hasattr(Agent, "PrezimeAgent")
    descriptor = None
    for klass in Agent.__mro__:
        if "PrezimeAgent" in klass.__dict__:
            descriptor = klass.__dict__["PrezimeAgent"]
            break
    assert isinstance(descriptor, property)

def test_agent_has_Password():
    assert hasattr(Agent, "Password")
    descriptor = None
    for klass in Agent.__mro__:
        if "Password" in klass.__dict__:
            descriptor = klass.__dict__["Password"]
            break
    assert isinstance(descriptor, property)

def test_agent_has_Username():
    assert hasattr(Agent, "Username")
    descriptor = None
    for klass in Agent.__mro__:
        if "Username" in klass.__dict__:
            descriptor = klass.__dict__["Username"]
            break
    assert isinstance(descriptor, property)

def test_agent_has_Email():
    assert hasattr(Agent, "Email")
    descriptor = None
    for klass in Agent.__mro__:
        if "Email" in klass.__dict__:
            descriptor = klass.__dict__["Email"]
            break
    assert isinstance(descriptor, property)

def test_agent_has_AgentID():
    assert hasattr(Agent, "AgentID")
    descriptor = None
    for klass in Agent.__mro__:
        if "AgentID" in klass.__dict__:
            descriptor = klass.__dict__["AgentID"]
            break
    assert isinstance(descriptor, property)



def test_rezervacija_is_not_abstract():
    assert not inspect.isabstract(Rezervacija)


def test_rezervacija_constructor_exists():
    assert callable(Rezervacija.__init__)


def test_rezervacija_constructor_args():
    sig = inspect.signature(Rezervacija.__init__)
    params = list(sig.parameters.keys())
    assert "PutnikID" in params, "Missing parameter 'PutnikID'"
    assert "ReyervacijaID" in params, "Missing parameter 'ReyervacijaID'"
    assert "DatumKreiranja" in params, "Missing parameter 'DatumKreiranja'"
    assert "AranzmanID" in params, "Missing parameter 'AranzmanID'"
    assert "RacunID" in params, "Missing parameter 'RacunID'"
    assert "AgentID" in params, "Missing parameter 'AgentID'"

def test_rezervacija_has_PutnikID():
    assert hasattr(Rezervacija, "PutnikID")
    descriptor = None
    for klass in Rezervacija.__mro__:
        if "PutnikID" in klass.__dict__:
            descriptor = klass.__dict__["PutnikID"]
            break
    assert isinstance(descriptor, property)

def test_rezervacija_has_ReyervacijaID():
    assert hasattr(Rezervacija, "ReyervacijaID")
    descriptor = None
    for klass in Rezervacija.__mro__:
        if "ReyervacijaID" in klass.__dict__:
            descriptor = klass.__dict__["ReyervacijaID"]
            break
    assert isinstance(descriptor, property)

def test_rezervacija_has_DatumKreiranja():
    assert hasattr(Rezervacija, "DatumKreiranja")
    descriptor = None
    for klass in Rezervacija.__mro__:
        if "DatumKreiranja" in klass.__dict__:
            descriptor = klass.__dict__["DatumKreiranja"]
            break
    assert isinstance(descriptor, property)

def test_rezervacija_has_AranzmanID():
    assert hasattr(Rezervacija, "AranzmanID")
    descriptor = None
    for klass in Rezervacija.__mro__:
        if "AranzmanID" in klass.__dict__:
            descriptor = klass.__dict__["AranzmanID"]
            break
    assert isinstance(descriptor, property)

def test_rezervacija_has_RacunID():
    assert hasattr(Rezervacija, "RacunID")
    descriptor = None
    for klass in Rezervacija.__mro__:
        if "RacunID" in klass.__dict__:
            descriptor = klass.__dict__["RacunID"]
            break
    assert isinstance(descriptor, property)

def test_rezervacija_has_AgentID():
    assert hasattr(Rezervacija, "AgentID")
    descriptor = None
    for klass in Rezervacija.__mro__:
        if "AgentID" in klass.__dict__:
            descriptor = klass.__dict__["AgentID"]
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
Putnik_strategy = st.builds(
    Putnik,
    Grad=
        safe_text,
    PutnikID=
        st.integers(),
    Email=
        safe_text,
    ImePutnik=
        safe_text,
    BrojTel=
        safe_text,
    JMBG=
        safe_text,
    OsiguranjeID=
        st.integers(),
    PrezimePutnik=
        safe_text,
    Adresa=
        safe_text
)
string_strategy = st.builds(
    string,
)
Destinacija_strategy = st.builds(
    Destinacija,
    Drzava=
        safe_text,
    Grad=
        safe_text,
    Hotel=
        safe_text,
    DestinacijaID=
        st.integers()
)
Double_strategy = st.builds(
    Double,
)
Date_strategy = st.builds(
    Date,
)
Racun_strategy = st.builds(
    Racun,
    Placeno=
        st.booleans(),
    Iznos=
        st.none(),
    RacunID=
        st.integers()
)
Termin_strategy = st.builds(
    Termin,
    DatumPovratka=
        st.dates(),
    DatumPolaska=
        st.dates(),
    TerminID=
        st.integers()
)
Osiguranje_strategy = st.builds(
    Osiguranje,
    OsiguranjeID=
        st.integers(),
    OsigurKuca=
        safe_text
)
Aranzman_strategy = st.builds(
    Aranzman,
    TerminID=
        st.integers(),
    Popunjeno=
        st.booleans(),
    DestinacijaID=
        st.integers(),
    AranzmanID=
        st.integers(),
    BrojMesta=
        st.integers(),
    NazivAranzmana=
        safe_text,
    Cena=
        st.none()
)
Agent_strategy = st.builds(
    Agent,
    ImeAgent=
        safe_text,
    BrojTele=
        safe_text,
    PrezimeAgent=
        safe_text,
    Password=
        safe_text,
    Username=
        safe_text,
    Email=
        safe_text,
    AgentID=
        st.integers()
)
Rezervacija_strategy = st.builds(
    Rezervacija,
    PutnikID=
        st.integers(),
    ReyervacijaID=
        st.integers(),
    DatumKreiranja=
        st.dates(),
    AranzmanID=
        st.integers(),
    RacunID=
        st.integers(),
    AgentID=
        st.integers()
)

@given(instance=Putnik_strategy)
@settings(max_examples=50)
def test_putnik_instantiation(instance):
    assert isinstance(instance, Putnik)



@given(instance=Putnik_strategy)
def test_putnik_Grad_setter(instance):
    original = instance.Grad
    instance.Grad = original
    assert instance.Grad == original



@given(instance=Putnik_strategy)
def test_putnik_PutnikID_setter(instance):
    original = instance.PutnikID
    instance.PutnikID = original
    assert instance.PutnikID == original



@given(instance=Putnik_strategy)
def test_putnik_Email_setter(instance):
    original = instance.Email
    instance.Email = original
    assert instance.Email == original



@given(instance=Putnik_strategy)
def test_putnik_ImePutnik_setter(instance):
    original = instance.ImePutnik
    instance.ImePutnik = original
    assert instance.ImePutnik == original



@given(instance=Putnik_strategy)
def test_putnik_BrojTel_setter(instance):
    original = instance.BrojTel
    instance.BrojTel = original
    assert instance.BrojTel == original



@given(instance=Putnik_strategy)
def test_putnik_JMBG_setter(instance):
    original = instance.JMBG
    instance.JMBG = original
    assert instance.JMBG == original



@given(instance=Putnik_strategy)
def test_putnik_OsiguranjeID_setter(instance):
    original = instance.OsiguranjeID
    instance.OsiguranjeID = original
    assert instance.OsiguranjeID == original



@given(instance=Putnik_strategy)
def test_putnik_PrezimePutnik_setter(instance):
    original = instance.PrezimePutnik
    instance.PrezimePutnik = original
    assert instance.PrezimePutnik == original



@given(instance=Putnik_strategy)
def test_putnik_Adresa_setter(instance):
    original = instance.Adresa
    instance.Adresa = original
    assert instance.Adresa == original

@given(instance=string_strategy)
@settings(max_examples=50)
def test_string_instantiation(instance):
    assert isinstance(instance, string)

@given(instance=Destinacija_strategy)
@settings(max_examples=50)
def test_destinacija_instantiation(instance):
    assert isinstance(instance, Destinacija)



@given(instance=Destinacija_strategy)
def test_destinacija_Drzava_setter(instance):
    original = instance.Drzava
    instance.Drzava = original
    assert instance.Drzava == original



@given(instance=Destinacija_strategy)
def test_destinacija_Grad_setter(instance):
    original = instance.Grad
    instance.Grad = original
    assert instance.Grad == original



@given(instance=Destinacija_strategy)
def test_destinacija_Hotel_setter(instance):
    original = instance.Hotel
    instance.Hotel = original
    assert instance.Hotel == original



@given(instance=Destinacija_strategy)
def test_destinacija_DestinacijaID_setter(instance):
    original = instance.DestinacijaID
    instance.DestinacijaID = original
    assert instance.DestinacijaID == original

@given(instance=Double_strategy)
@settings(max_examples=50)
def test_double_instantiation(instance):
    assert isinstance(instance, Double)

@given(instance=Date_strategy)
@settings(max_examples=50)
def test_date_instantiation(instance):
    assert isinstance(instance, Date)

@given(instance=Racun_strategy)
@settings(max_examples=50)
def test_racun_instantiation(instance):
    assert isinstance(instance, Racun)



@given(instance=Racun_strategy)
def test_racun_Placeno_setter(instance):
    original = instance.Placeno
    instance.Placeno = original
    assert instance.Placeno == original



@given(instance=Racun_strategy)
def test_racun_Iznos_setter(instance):
    original = instance.Iznos
    instance.Iznos = original
    assert instance.Iznos == original



@given(instance=Racun_strategy)
def test_racun_RacunID_setter(instance):
    original = instance.RacunID
    instance.RacunID = original
    assert instance.RacunID == original

@given(instance=Termin_strategy)
@settings(max_examples=50)
def test_termin_instantiation(instance):
    assert isinstance(instance, Termin)



@given(instance=Termin_strategy)
def test_termin_DatumPovratka_setter(instance):
    original = instance.DatumPovratka
    instance.DatumPovratka = original
    assert instance.DatumPovratka == original



@given(instance=Termin_strategy)
def test_termin_DatumPolaska_setter(instance):
    original = instance.DatumPolaska
    instance.DatumPolaska = original
    assert instance.DatumPolaska == original



@given(instance=Termin_strategy)
def test_termin_TerminID_setter(instance):
    original = instance.TerminID
    instance.TerminID = original
    assert instance.TerminID == original

@given(instance=Osiguranje_strategy)
@settings(max_examples=50)
def test_osiguranje_instantiation(instance):
    assert isinstance(instance, Osiguranje)



@given(instance=Osiguranje_strategy)
def test_osiguranje_OsiguranjeID_setter(instance):
    original = instance.OsiguranjeID
    instance.OsiguranjeID = original
    assert instance.OsiguranjeID == original



@given(instance=Osiguranje_strategy)
def test_osiguranje_OsigurKuca_setter(instance):
    original = instance.OsigurKuca
    instance.OsigurKuca = original
    assert instance.OsigurKuca == original

@given(instance=Aranzman_strategy)
@settings(max_examples=50)
def test_aranzman_instantiation(instance):
    assert isinstance(instance, Aranzman)



@given(instance=Aranzman_strategy)
def test_aranzman_TerminID_setter(instance):
    original = instance.TerminID
    instance.TerminID = original
    assert instance.TerminID == original



@given(instance=Aranzman_strategy)
def test_aranzman_Popunjeno_setter(instance):
    original = instance.Popunjeno
    instance.Popunjeno = original
    assert instance.Popunjeno == original



@given(instance=Aranzman_strategy)
def test_aranzman_DestinacijaID_setter(instance):
    original = instance.DestinacijaID
    instance.DestinacijaID = original
    assert instance.DestinacijaID == original



@given(instance=Aranzman_strategy)
def test_aranzman_AranzmanID_setter(instance):
    original = instance.AranzmanID
    instance.AranzmanID = original
    assert instance.AranzmanID == original



@given(instance=Aranzman_strategy)
def test_aranzman_BrojMesta_setter(instance):
    original = instance.BrojMesta
    instance.BrojMesta = original
    assert instance.BrojMesta == original



@given(instance=Aranzman_strategy)
def test_aranzman_NazivAranzmana_setter(instance):
    original = instance.NazivAranzmana
    instance.NazivAranzmana = original
    assert instance.NazivAranzmana == original



@given(instance=Aranzman_strategy)
def test_aranzman_Cena_setter(instance):
    original = instance.Cena
    instance.Cena = original
    assert instance.Cena == original

@given(instance=Agent_strategy)
@settings(max_examples=50)
def test_agent_instantiation(instance):
    assert isinstance(instance, Agent)



@given(instance=Agent_strategy)
def test_agent_ImeAgent_setter(instance):
    original = instance.ImeAgent
    instance.ImeAgent = original
    assert instance.ImeAgent == original



@given(instance=Agent_strategy)
def test_agent_BrojTele_setter(instance):
    original = instance.BrojTele
    instance.BrojTele = original
    assert instance.BrojTele == original



@given(instance=Agent_strategy)
def test_agent_PrezimeAgent_setter(instance):
    original = instance.PrezimeAgent
    instance.PrezimeAgent = original
    assert instance.PrezimeAgent == original



@given(instance=Agent_strategy)
def test_agent_Password_setter(instance):
    original = instance.Password
    instance.Password = original
    assert instance.Password == original



@given(instance=Agent_strategy)
def test_agent_Username_setter(instance):
    original = instance.Username
    instance.Username = original
    assert instance.Username == original



@given(instance=Agent_strategy)
def test_agent_Email_setter(instance):
    original = instance.Email
    instance.Email = original
    assert instance.Email == original



@given(instance=Agent_strategy)
def test_agent_AgentID_setter(instance):
    original = instance.AgentID
    instance.AgentID = original
    assert instance.AgentID == original

@given(instance=Rezervacija_strategy)
@settings(max_examples=50)
def test_rezervacija_instantiation(instance):
    assert isinstance(instance, Rezervacija)



@given(instance=Rezervacija_strategy)
def test_rezervacija_PutnikID_setter(instance):
    original = instance.PutnikID
    instance.PutnikID = original
    assert instance.PutnikID == original



@given(instance=Rezervacija_strategy)
def test_rezervacija_ReyervacijaID_setter(instance):
    original = instance.ReyervacijaID
    instance.ReyervacijaID = original
    assert instance.ReyervacijaID == original



@given(instance=Rezervacija_strategy)
def test_rezervacija_DatumKreiranja_setter(instance):
    original = instance.DatumKreiranja
    instance.DatumKreiranja = original
    assert instance.DatumKreiranja == original



@given(instance=Rezervacija_strategy)
def test_rezervacija_AranzmanID_setter(instance):
    original = instance.AranzmanID
    instance.AranzmanID = original
    assert instance.AranzmanID == original



@given(instance=Rezervacija_strategy)
def test_rezervacija_RacunID_setter(instance):
    original = instance.RacunID
    instance.RacunID = original
    assert instance.RacunID == original



@given(instance=Rezervacija_strategy)
def test_rezervacija_AgentID_setter(instance):
    original = instance.AgentID
    instance.AgentID = original
    assert instance.AgentID == original
