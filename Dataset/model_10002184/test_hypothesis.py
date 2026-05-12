import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Drzava,
    Grad,
    Hotel,
    Vodic,
    Aranzman,
    Uplata,
    Korisnik,
    Putnik,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_drzava_is_not_abstract():
    assert not inspect.isabstract(Drzava)


def test_drzava_constructor_exists():
    assert callable(Drzava.__init__)


def test_drzava_constructor_args():
    sig = inspect.signature(Drzava.__init__)
    params = list(sig.parameters.keys())
    assert "DrzavaID" in params, "Missing parameter 'DrzavaID'"
    assert "NazivDrzave" in params, "Missing parameter 'NazivDrzave'"

def test_drzava_has_DrzavaID():
    assert hasattr(Drzava, "DrzavaID")
    descriptor = None
    for klass in Drzava.__mro__:
        if "DrzavaID" in klass.__dict__:
            descriptor = klass.__dict__["DrzavaID"]
            break
    assert isinstance(descriptor, property)

def test_drzava_has_NazivDrzave():
    assert hasattr(Drzava, "NazivDrzave")
    descriptor = None
    for klass in Drzava.__mro__:
        if "NazivDrzave" in klass.__dict__:
            descriptor = klass.__dict__["NazivDrzave"]
            break
    assert isinstance(descriptor, property)



def test_grad_is_not_abstract():
    assert not inspect.isabstract(Grad)


def test_grad_constructor_exists():
    assert callable(Grad.__init__)


def test_grad_constructor_args():
    sig = inspect.signature(Grad.__init__)
    params = list(sig.parameters.keys())
    assert "NazivGrada" in params, "Missing parameter 'NazivGrada'"
    assert "GradID" in params, "Missing parameter 'GradID'"
    assert "DrzavaID" in params, "Missing parameter 'DrzavaID'"

def test_grad_has_NazivGrada():
    assert hasattr(Grad, "NazivGrada")
    descriptor = None
    for klass in Grad.__mro__:
        if "NazivGrada" in klass.__dict__:
            descriptor = klass.__dict__["NazivGrada"]
            break
    assert isinstance(descriptor, property)

def test_grad_has_GradID():
    assert hasattr(Grad, "GradID")
    descriptor = None
    for klass in Grad.__mro__:
        if "GradID" in klass.__dict__:
            descriptor = klass.__dict__["GradID"]
            break
    assert isinstance(descriptor, property)

def test_grad_has_DrzavaID():
    assert hasattr(Grad, "DrzavaID")
    descriptor = None
    for klass in Grad.__mro__:
        if "DrzavaID" in klass.__dict__:
            descriptor = klass.__dict__["DrzavaID"]
            break
    assert isinstance(descriptor, property)



def test_hotel_is_not_abstract():
    assert not inspect.isabstract(Hotel)


def test_hotel_constructor_exists():
    assert callable(Hotel.__init__)


def test_hotel_constructor_args():
    sig = inspect.signature(Hotel.__init__)
    params = list(sig.parameters.keys())
    assert "AdresaHotela" in params, "Missing parameter 'AdresaHotela'"
    assert "KontaktHotela" in params, "Missing parameter 'KontaktHotela'"
    assert "HotelID" in params, "Missing parameter 'HotelID'"
    assert "NazivHotela" in params, "Missing parameter 'NazivHotela'"
    assert "GradID" in params, "Missing parameter 'GradID'"

def test_hotel_has_AdresaHotela():
    assert hasattr(Hotel, "AdresaHotela")
    descriptor = None
    for klass in Hotel.__mro__:
        if "AdresaHotela" in klass.__dict__:
            descriptor = klass.__dict__["AdresaHotela"]
            break
    assert isinstance(descriptor, property)

def test_hotel_has_KontaktHotela():
    assert hasattr(Hotel, "KontaktHotela")
    descriptor = None
    for klass in Hotel.__mro__:
        if "KontaktHotela" in klass.__dict__:
            descriptor = klass.__dict__["KontaktHotela"]
            break
    assert isinstance(descriptor, property)

def test_hotel_has_HotelID():
    assert hasattr(Hotel, "HotelID")
    descriptor = None
    for klass in Hotel.__mro__:
        if "HotelID" in klass.__dict__:
            descriptor = klass.__dict__["HotelID"]
            break
    assert isinstance(descriptor, property)

def test_hotel_has_NazivHotela():
    assert hasattr(Hotel, "NazivHotela")
    descriptor = None
    for klass in Hotel.__mro__:
        if "NazivHotela" in klass.__dict__:
            descriptor = klass.__dict__["NazivHotela"]
            break
    assert isinstance(descriptor, property)

def test_hotel_has_GradID():
    assert hasattr(Hotel, "GradID")
    descriptor = None
    for klass in Hotel.__mro__:
        if "GradID" in klass.__dict__:
            descriptor = klass.__dict__["GradID"]
            break
    assert isinstance(descriptor, property)



def test_vodic_is_not_abstract():
    assert not inspect.isabstract(Vodic)


def test_vodic_constructor_exists():
    assert callable(Vodic.__init__)


def test_vodic_constructor_args():
    sig = inspect.signature(Vodic.__init__)
    params = list(sig.parameters.keys())
    assert "GradVodica" in params, "Missing parameter 'GradVodica'"
    assert "KontaktVodica" in params, "Missing parameter 'KontaktVodica'"
    assert "PrezimeVodica" in params, "Missing parameter 'PrezimeVodica'"
    assert "ImeVodica" in params, "Missing parameter 'ImeVodica'"
    assert "JMBG" in params, "Missing parameter 'JMBG'"
    assert "AdresaVodica" in params, "Missing parameter 'AdresaVodica'"
    assert "VodicID" in params, "Missing parameter 'VodicID'"

def test_vodic_has_GradVodica():
    assert hasattr(Vodic, "GradVodica")
    descriptor = None
    for klass in Vodic.__mro__:
        if "GradVodica" in klass.__dict__:
            descriptor = klass.__dict__["GradVodica"]
            break
    assert isinstance(descriptor, property)

def test_vodic_has_KontaktVodica():
    assert hasattr(Vodic, "KontaktVodica")
    descriptor = None
    for klass in Vodic.__mro__:
        if "KontaktVodica" in klass.__dict__:
            descriptor = klass.__dict__["KontaktVodica"]
            break
    assert isinstance(descriptor, property)

def test_vodic_has_PrezimeVodica():
    assert hasattr(Vodic, "PrezimeVodica")
    descriptor = None
    for klass in Vodic.__mro__:
        if "PrezimeVodica" in klass.__dict__:
            descriptor = klass.__dict__["PrezimeVodica"]
            break
    assert isinstance(descriptor, property)

def test_vodic_has_ImeVodica():
    assert hasattr(Vodic, "ImeVodica")
    descriptor = None
    for klass in Vodic.__mro__:
        if "ImeVodica" in klass.__dict__:
            descriptor = klass.__dict__["ImeVodica"]
            break
    assert isinstance(descriptor, property)

def test_vodic_has_JMBG():
    assert hasattr(Vodic, "JMBG")
    descriptor = None
    for klass in Vodic.__mro__:
        if "JMBG" in klass.__dict__:
            descriptor = klass.__dict__["JMBG"]
            break
    assert isinstance(descriptor, property)

def test_vodic_has_AdresaVodica():
    assert hasattr(Vodic, "AdresaVodica")
    descriptor = None
    for klass in Vodic.__mro__:
        if "AdresaVodica" in klass.__dict__:
            descriptor = klass.__dict__["AdresaVodica"]
            break
    assert isinstance(descriptor, property)

def test_vodic_has_VodicID():
    assert hasattr(Vodic, "VodicID")
    descriptor = None
    for klass in Vodic.__mro__:
        if "VodicID" in klass.__dict__:
            descriptor = klass.__dict__["VodicID"]
            break
    assert isinstance(descriptor, property)



def test_aranzman_is_not_abstract():
    assert not inspect.isabstract(Aranzman)


def test_aranzman_constructor_exists():
    assert callable(Aranzman.__init__)


def test_aranzman_constructor_args():
    sig = inspect.signature(Aranzman.__init__)
    params = list(sig.parameters.keys())
    assert "AranzmanID" in params, "Missing parameter 'AranzmanID'"
    assert "HotelID" in params, "Missing parameter 'HotelID'"
    assert "DatumAranzmana" in params, "Missing parameter 'DatumAranzmana'"
    assert "KorisnikID" in params, "Missing parameter 'KorisnikID'"
    assert "VodicID" in params, "Missing parameter 'VodicID'"
    assert "OpisAranzmana" in params, "Missing parameter 'OpisAranzmana'"
    assert "CenaAranzmana" in params, "Missing parameter 'CenaAranzmana'"
    assert "NazivAranzmana" in params, "Missing parameter 'NazivAranzmana'"

def test_aranzman_has_AranzmanID():
    assert hasattr(Aranzman, "AranzmanID")
    descriptor = None
    for klass in Aranzman.__mro__:
        if "AranzmanID" in klass.__dict__:
            descriptor = klass.__dict__["AranzmanID"]
            break
    assert isinstance(descriptor, property)

def test_aranzman_has_HotelID():
    assert hasattr(Aranzman, "HotelID")
    descriptor = None
    for klass in Aranzman.__mro__:
        if "HotelID" in klass.__dict__:
            descriptor = klass.__dict__["HotelID"]
            break
    assert isinstance(descriptor, property)

def test_aranzman_has_DatumAranzmana():
    assert hasattr(Aranzman, "DatumAranzmana")
    descriptor = None
    for klass in Aranzman.__mro__:
        if "DatumAranzmana" in klass.__dict__:
            descriptor = klass.__dict__["DatumAranzmana"]
            break
    assert isinstance(descriptor, property)

def test_aranzman_has_KorisnikID():
    assert hasattr(Aranzman, "KorisnikID")
    descriptor = None
    for klass in Aranzman.__mro__:
        if "KorisnikID" in klass.__dict__:
            descriptor = klass.__dict__["KorisnikID"]
            break
    assert isinstance(descriptor, property)

def test_aranzman_has_VodicID():
    assert hasattr(Aranzman, "VodicID")
    descriptor = None
    for klass in Aranzman.__mro__:
        if "VodicID" in klass.__dict__:
            descriptor = klass.__dict__["VodicID"]
            break
    assert isinstance(descriptor, property)

def test_aranzman_has_OpisAranzmana():
    assert hasattr(Aranzman, "OpisAranzmana")
    descriptor = None
    for klass in Aranzman.__mro__:
        if "OpisAranzmana" in klass.__dict__:
            descriptor = klass.__dict__["OpisAranzmana"]
            break
    assert isinstance(descriptor, property)

def test_aranzman_has_CenaAranzmana():
    assert hasattr(Aranzman, "CenaAranzmana")
    descriptor = None
    for klass in Aranzman.__mro__:
        if "CenaAranzmana" in klass.__dict__:
            descriptor = klass.__dict__["CenaAranzmana"]
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



def test_uplata_is_not_abstract():
    assert not inspect.isabstract(Uplata)


def test_uplata_constructor_exists():
    assert callable(Uplata.__init__)


def test_uplata_constructor_args():
    sig = inspect.signature(Uplata.__init__)
    params = list(sig.parameters.keys())
    assert "DatumUplate" in params, "Missing parameter 'DatumUplate'"
    assert "Iznos" in params, "Missing parameter 'Iznos'"
    assert "NazivUplate" in params, "Missing parameter 'NazivUplate'"
    assert "UplataID" in params, "Missing parameter 'UplataID'"
    assert "PutnikID" in params, "Missing parameter 'PutnikID'"

def test_uplata_has_DatumUplate():
    assert hasattr(Uplata, "DatumUplate")
    descriptor = None
    for klass in Uplata.__mro__:
        if "DatumUplate" in klass.__dict__:
            descriptor = klass.__dict__["DatumUplate"]
            break
    assert isinstance(descriptor, property)

def test_uplata_has_Iznos():
    assert hasattr(Uplata, "Iznos")
    descriptor = None
    for klass in Uplata.__mro__:
        if "Iznos" in klass.__dict__:
            descriptor = klass.__dict__["Iznos"]
            break
    assert isinstance(descriptor, property)

def test_uplata_has_NazivUplate():
    assert hasattr(Uplata, "NazivUplate")
    descriptor = None
    for klass in Uplata.__mro__:
        if "NazivUplate" in klass.__dict__:
            descriptor = klass.__dict__["NazivUplate"]
            break
    assert isinstance(descriptor, property)

def test_uplata_has_UplataID():
    assert hasattr(Uplata, "UplataID")
    descriptor = None
    for klass in Uplata.__mro__:
        if "UplataID" in klass.__dict__:
            descriptor = klass.__dict__["UplataID"]
            break
    assert isinstance(descriptor, property)

def test_uplata_has_PutnikID():
    assert hasattr(Uplata, "PutnikID")
    descriptor = None
    for klass in Uplata.__mro__:
        if "PutnikID" in klass.__dict__:
            descriptor = klass.__dict__["PutnikID"]
            break
    assert isinstance(descriptor, property)



def test_korisnik_is_not_abstract():
    assert not inspect.isabstract(Korisnik)


def test_korisnik_constructor_exists():
    assert callable(Korisnik.__init__)


def test_korisnik_constructor_args():
    sig = inspect.signature(Korisnik.__init__)
    params = list(sig.parameters.keys())
    assert "KontaktKorisnika" in params, "Missing parameter 'KontaktKorisnika'"
    assert "KorisnikID" in params, "Missing parameter 'KorisnikID'"
    assert "JMBG" in params, "Missing parameter 'JMBG'"
    assert "Password" in params, "Missing parameter 'Password'"
    assert "PrezimeKorisnika" in params, "Missing parameter 'PrezimeKorisnika'"
    assert "ImeKorisnika" in params, "Missing parameter 'ImeKorisnika'"
    assert "AdresaKorisnika" in params, "Missing parameter 'AdresaKorisnika'"
    assert "GradKorisnika" in params, "Missing parameter 'GradKorisnika'"
    assert "Username" in params, "Missing parameter 'Username'"

def test_korisnik_has_KontaktKorisnika():
    assert hasattr(Korisnik, "KontaktKorisnika")
    descriptor = None
    for klass in Korisnik.__mro__:
        if "KontaktKorisnika" in klass.__dict__:
            descriptor = klass.__dict__["KontaktKorisnika"]
            break
    assert isinstance(descriptor, property)

def test_korisnik_has_KorisnikID():
    assert hasattr(Korisnik, "KorisnikID")
    descriptor = None
    for klass in Korisnik.__mro__:
        if "KorisnikID" in klass.__dict__:
            descriptor = klass.__dict__["KorisnikID"]
            break
    assert isinstance(descriptor, property)

def test_korisnik_has_JMBG():
    assert hasattr(Korisnik, "JMBG")
    descriptor = None
    for klass in Korisnik.__mro__:
        if "JMBG" in klass.__dict__:
            descriptor = klass.__dict__["JMBG"]
            break
    assert isinstance(descriptor, property)

def test_korisnik_has_Password():
    assert hasattr(Korisnik, "Password")
    descriptor = None
    for klass in Korisnik.__mro__:
        if "Password" in klass.__dict__:
            descriptor = klass.__dict__["Password"]
            break
    assert isinstance(descriptor, property)

def test_korisnik_has_PrezimeKorisnika():
    assert hasattr(Korisnik, "PrezimeKorisnika")
    descriptor = None
    for klass in Korisnik.__mro__:
        if "PrezimeKorisnika" in klass.__dict__:
            descriptor = klass.__dict__["PrezimeKorisnika"]
            break
    assert isinstance(descriptor, property)

def test_korisnik_has_ImeKorisnika():
    assert hasattr(Korisnik, "ImeKorisnika")
    descriptor = None
    for klass in Korisnik.__mro__:
        if "ImeKorisnika" in klass.__dict__:
            descriptor = klass.__dict__["ImeKorisnika"]
            break
    assert isinstance(descriptor, property)

def test_korisnik_has_AdresaKorisnika():
    assert hasattr(Korisnik, "AdresaKorisnika")
    descriptor = None
    for klass in Korisnik.__mro__:
        if "AdresaKorisnika" in klass.__dict__:
            descriptor = klass.__dict__["AdresaKorisnika"]
            break
    assert isinstance(descriptor, property)

def test_korisnik_has_GradKorisnika():
    assert hasattr(Korisnik, "GradKorisnika")
    descriptor = None
    for klass in Korisnik.__mro__:
        if "GradKorisnika" in klass.__dict__:
            descriptor = klass.__dict__["GradKorisnika"]
            break
    assert isinstance(descriptor, property)

def test_korisnik_has_Username():
    assert hasattr(Korisnik, "Username")
    descriptor = None
    for klass in Korisnik.__mro__:
        if "Username" in klass.__dict__:
            descriptor = klass.__dict__["Username"]
            break
    assert isinstance(descriptor, property)



def test_putnik_is_not_abstract():
    assert not inspect.isabstract(Putnik)


def test_putnik_constructor_exists():
    assert callable(Putnik.__init__)


def test_putnik_constructor_args():
    sig = inspect.signature(Putnik.__init__)
    params = list(sig.parameters.keys())
    assert "BrojPasosa" in params, "Missing parameter 'BrojPasosa'"
    assert "AranzmanID" in params, "Missing parameter 'AranzmanID'"
    assert "JMBG" in params, "Missing parameter 'JMBG'"
    assert "ImePutnika" in params, "Missing parameter 'ImePutnika'"
    assert "AdresaPutnika" in params, "Missing parameter 'AdresaPutnika'"
    assert "PrezimePutnika" in params, "Missing parameter 'PrezimePutnika'"
    assert "PutnikID" in params, "Missing parameter 'PutnikID'"
    assert "KontaktPutnika" in params, "Missing parameter 'KontaktPutnika'"
    assert "GradPutnika" in params, "Missing parameter 'GradPutnika'"

def test_putnik_has_BrojPasosa():
    assert hasattr(Putnik, "BrojPasosa")
    descriptor = None
    for klass in Putnik.__mro__:
        if "BrojPasosa" in klass.__dict__:
            descriptor = klass.__dict__["BrojPasosa"]
            break
    assert isinstance(descriptor, property)

def test_putnik_has_AranzmanID():
    assert hasattr(Putnik, "AranzmanID")
    descriptor = None
    for klass in Putnik.__mro__:
        if "AranzmanID" in klass.__dict__:
            descriptor = klass.__dict__["AranzmanID"]
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

def test_putnik_has_ImePutnika():
    assert hasattr(Putnik, "ImePutnika")
    descriptor = None
    for klass in Putnik.__mro__:
        if "ImePutnika" in klass.__dict__:
            descriptor = klass.__dict__["ImePutnika"]
            break
    assert isinstance(descriptor, property)

def test_putnik_has_AdresaPutnika():
    assert hasattr(Putnik, "AdresaPutnika")
    descriptor = None
    for klass in Putnik.__mro__:
        if "AdresaPutnika" in klass.__dict__:
            descriptor = klass.__dict__["AdresaPutnika"]
            break
    assert isinstance(descriptor, property)

def test_putnik_has_PrezimePutnika():
    assert hasattr(Putnik, "PrezimePutnika")
    descriptor = None
    for klass in Putnik.__mro__:
        if "PrezimePutnika" in klass.__dict__:
            descriptor = klass.__dict__["PrezimePutnika"]
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

def test_putnik_has_KontaktPutnika():
    assert hasattr(Putnik, "KontaktPutnika")
    descriptor = None
    for klass in Putnik.__mro__:
        if "KontaktPutnika" in klass.__dict__:
            descriptor = klass.__dict__["KontaktPutnika"]
            break
    assert isinstance(descriptor, property)

def test_putnik_has_GradPutnika():
    assert hasattr(Putnik, "GradPutnika")
    descriptor = None
    for klass in Putnik.__mro__:
        if "GradPutnika" in klass.__dict__:
            descriptor = klass.__dict__["GradPutnika"]
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
Drzava_strategy = st.builds(
    Drzava,
    DrzavaID=
        st.integers(),
    NazivDrzave=
        safe_text
)
Grad_strategy = st.builds(
    Grad,
    NazivGrada=
        safe_text,
    GradID=
        st.integers(),
    DrzavaID=
        st.integers()
)
Hotel_strategy = st.builds(
    Hotel,
    AdresaHotela=
        safe_text,
    KontaktHotela=
        safe_text,
    HotelID=
        st.integers(),
    NazivHotela=
        safe_text,
    GradID=
        st.integers()
)
Vodic_strategy = st.builds(
    Vodic,
    GradVodica=
        safe_text,
    KontaktVodica=
        safe_text,
    PrezimeVodica=
        safe_text,
    ImeVodica=
        safe_text,
    JMBG=
        safe_text,
    AdresaVodica=
        safe_text,
    VodicID=
        st.integers()
)
Aranzman_strategy = st.builds(
    Aranzman,
    AranzmanID=
        st.integers(),
    HotelID=
        st.integers(),
    DatumAranzmana=
        safe_text,
    KorisnikID=
        st.integers(),
    VodicID=
        st.integers(),
    OpisAranzmana=
        safe_text,
    CenaAranzmana=
        safe_text,
    NazivAranzmana=
        safe_text
)
Uplata_strategy = st.builds(
    Uplata,
    DatumUplate=
        safe_text,
    Iznos=
        safe_text,
    NazivUplate=
        safe_text,
    UplataID=
        st.integers(),
    PutnikID=
        st.integers()
)
Korisnik_strategy = st.builds(
    Korisnik,
    KontaktKorisnika=
        safe_text,
    KorisnikID=
        st.integers(),
    JMBG=
        safe_text,
    Password=
        safe_text,
    PrezimeKorisnika=
        safe_text,
    ImeKorisnika=
        safe_text,
    AdresaKorisnika=
        safe_text,
    GradKorisnika=
        safe_text,
    Username=
        safe_text
)
Putnik_strategy = st.builds(
    Putnik,
    BrojPasosa=
        st.integers(),
    AranzmanID=
        st.integers(),
    JMBG=
        safe_text,
    ImePutnika=
        safe_text,
    AdresaPutnika=
        safe_text,
    PrezimePutnika=
        safe_text,
    PutnikID=
        st.integers(),
    KontaktPutnika=
        safe_text,
    GradPutnika=
        safe_text
)

@given(instance=Drzava_strategy)
@settings(max_examples=50)
def test_drzava_instantiation(instance):
    assert isinstance(instance, Drzava)



@given(instance=Drzava_strategy)
def test_drzava_DrzavaID_setter(instance):
    original = instance.DrzavaID
    instance.DrzavaID = original
    assert instance.DrzavaID == original



@given(instance=Drzava_strategy)
def test_drzava_NazivDrzave_setter(instance):
    original = instance.NazivDrzave
    instance.NazivDrzave = original
    assert instance.NazivDrzave == original

@given(instance=Grad_strategy)
@settings(max_examples=50)
def test_grad_instantiation(instance):
    assert isinstance(instance, Grad)



@given(instance=Grad_strategy)
def test_grad_NazivGrada_setter(instance):
    original = instance.NazivGrada
    instance.NazivGrada = original
    assert instance.NazivGrada == original



@given(instance=Grad_strategy)
def test_grad_GradID_setter(instance):
    original = instance.GradID
    instance.GradID = original
    assert instance.GradID == original



@given(instance=Grad_strategy)
def test_grad_DrzavaID_setter(instance):
    original = instance.DrzavaID
    instance.DrzavaID = original
    assert instance.DrzavaID == original

@given(instance=Hotel_strategy)
@settings(max_examples=50)
def test_hotel_instantiation(instance):
    assert isinstance(instance, Hotel)



@given(instance=Hotel_strategy)
def test_hotel_AdresaHotela_setter(instance):
    original = instance.AdresaHotela
    instance.AdresaHotela = original
    assert instance.AdresaHotela == original



@given(instance=Hotel_strategy)
def test_hotel_KontaktHotela_setter(instance):
    original = instance.KontaktHotela
    instance.KontaktHotela = original
    assert instance.KontaktHotela == original



@given(instance=Hotel_strategy)
def test_hotel_HotelID_setter(instance):
    original = instance.HotelID
    instance.HotelID = original
    assert instance.HotelID == original



@given(instance=Hotel_strategy)
def test_hotel_NazivHotela_setter(instance):
    original = instance.NazivHotela
    instance.NazivHotela = original
    assert instance.NazivHotela == original



@given(instance=Hotel_strategy)
def test_hotel_GradID_setter(instance):
    original = instance.GradID
    instance.GradID = original
    assert instance.GradID == original

@given(instance=Vodic_strategy)
@settings(max_examples=50)
def test_vodic_instantiation(instance):
    assert isinstance(instance, Vodic)



@given(instance=Vodic_strategy)
def test_vodic_GradVodica_setter(instance):
    original = instance.GradVodica
    instance.GradVodica = original
    assert instance.GradVodica == original



@given(instance=Vodic_strategy)
def test_vodic_KontaktVodica_setter(instance):
    original = instance.KontaktVodica
    instance.KontaktVodica = original
    assert instance.KontaktVodica == original



@given(instance=Vodic_strategy)
def test_vodic_PrezimeVodica_setter(instance):
    original = instance.PrezimeVodica
    instance.PrezimeVodica = original
    assert instance.PrezimeVodica == original



@given(instance=Vodic_strategy)
def test_vodic_ImeVodica_setter(instance):
    original = instance.ImeVodica
    instance.ImeVodica = original
    assert instance.ImeVodica == original



@given(instance=Vodic_strategy)
def test_vodic_JMBG_setter(instance):
    original = instance.JMBG
    instance.JMBG = original
    assert instance.JMBG == original



@given(instance=Vodic_strategy)
def test_vodic_AdresaVodica_setter(instance):
    original = instance.AdresaVodica
    instance.AdresaVodica = original
    assert instance.AdresaVodica == original



@given(instance=Vodic_strategy)
def test_vodic_VodicID_setter(instance):
    original = instance.VodicID
    instance.VodicID = original
    assert instance.VodicID == original

@given(instance=Aranzman_strategy)
@settings(max_examples=50)
def test_aranzman_instantiation(instance):
    assert isinstance(instance, Aranzman)



@given(instance=Aranzman_strategy)
def test_aranzman_AranzmanID_setter(instance):
    original = instance.AranzmanID
    instance.AranzmanID = original
    assert instance.AranzmanID == original



@given(instance=Aranzman_strategy)
def test_aranzman_HotelID_setter(instance):
    original = instance.HotelID
    instance.HotelID = original
    assert instance.HotelID == original



@given(instance=Aranzman_strategy)
def test_aranzman_DatumAranzmana_setter(instance):
    original = instance.DatumAranzmana
    instance.DatumAranzmana = original
    assert instance.DatumAranzmana == original



@given(instance=Aranzman_strategy)
def test_aranzman_KorisnikID_setter(instance):
    original = instance.KorisnikID
    instance.KorisnikID = original
    assert instance.KorisnikID == original



@given(instance=Aranzman_strategy)
def test_aranzman_VodicID_setter(instance):
    original = instance.VodicID
    instance.VodicID = original
    assert instance.VodicID == original



@given(instance=Aranzman_strategy)
def test_aranzman_OpisAranzmana_setter(instance):
    original = instance.OpisAranzmana
    instance.OpisAranzmana = original
    assert instance.OpisAranzmana == original



@given(instance=Aranzman_strategy)
def test_aranzman_CenaAranzmana_setter(instance):
    original = instance.CenaAranzmana
    instance.CenaAranzmana = original
    assert instance.CenaAranzmana == original



@given(instance=Aranzman_strategy)
def test_aranzman_NazivAranzmana_setter(instance):
    original = instance.NazivAranzmana
    instance.NazivAranzmana = original
    assert instance.NazivAranzmana == original

@given(instance=Uplata_strategy)
@settings(max_examples=50)
def test_uplata_instantiation(instance):
    assert isinstance(instance, Uplata)



@given(instance=Uplata_strategy)
def test_uplata_DatumUplate_setter(instance):
    original = instance.DatumUplate
    instance.DatumUplate = original
    assert instance.DatumUplate == original



@given(instance=Uplata_strategy)
def test_uplata_Iznos_setter(instance):
    original = instance.Iznos
    instance.Iznos = original
    assert instance.Iznos == original



@given(instance=Uplata_strategy)
def test_uplata_NazivUplate_setter(instance):
    original = instance.NazivUplate
    instance.NazivUplate = original
    assert instance.NazivUplate == original



@given(instance=Uplata_strategy)
def test_uplata_UplataID_setter(instance):
    original = instance.UplataID
    instance.UplataID = original
    assert instance.UplataID == original



@given(instance=Uplata_strategy)
def test_uplata_PutnikID_setter(instance):
    original = instance.PutnikID
    instance.PutnikID = original
    assert instance.PutnikID == original

@given(instance=Korisnik_strategy)
@settings(max_examples=50)
def test_korisnik_instantiation(instance):
    assert isinstance(instance, Korisnik)



@given(instance=Korisnik_strategy)
def test_korisnik_KontaktKorisnika_setter(instance):
    original = instance.KontaktKorisnika
    instance.KontaktKorisnika = original
    assert instance.KontaktKorisnika == original



@given(instance=Korisnik_strategy)
def test_korisnik_KorisnikID_setter(instance):
    original = instance.KorisnikID
    instance.KorisnikID = original
    assert instance.KorisnikID == original



@given(instance=Korisnik_strategy)
def test_korisnik_JMBG_setter(instance):
    original = instance.JMBG
    instance.JMBG = original
    assert instance.JMBG == original



@given(instance=Korisnik_strategy)
def test_korisnik_Password_setter(instance):
    original = instance.Password
    instance.Password = original
    assert instance.Password == original



@given(instance=Korisnik_strategy)
def test_korisnik_PrezimeKorisnika_setter(instance):
    original = instance.PrezimeKorisnika
    instance.PrezimeKorisnika = original
    assert instance.PrezimeKorisnika == original



@given(instance=Korisnik_strategy)
def test_korisnik_ImeKorisnika_setter(instance):
    original = instance.ImeKorisnika
    instance.ImeKorisnika = original
    assert instance.ImeKorisnika == original



@given(instance=Korisnik_strategy)
def test_korisnik_AdresaKorisnika_setter(instance):
    original = instance.AdresaKorisnika
    instance.AdresaKorisnika = original
    assert instance.AdresaKorisnika == original



@given(instance=Korisnik_strategy)
def test_korisnik_GradKorisnika_setter(instance):
    original = instance.GradKorisnika
    instance.GradKorisnika = original
    assert instance.GradKorisnika == original



@given(instance=Korisnik_strategy)
def test_korisnik_Username_setter(instance):
    original = instance.Username
    instance.Username = original
    assert instance.Username == original

@given(instance=Putnik_strategy)
@settings(max_examples=50)
def test_putnik_instantiation(instance):
    assert isinstance(instance, Putnik)



@given(instance=Putnik_strategy)
def test_putnik_BrojPasosa_setter(instance):
    original = instance.BrojPasosa
    instance.BrojPasosa = original
    assert instance.BrojPasosa == original



@given(instance=Putnik_strategy)
def test_putnik_AranzmanID_setter(instance):
    original = instance.AranzmanID
    instance.AranzmanID = original
    assert instance.AranzmanID == original



@given(instance=Putnik_strategy)
def test_putnik_JMBG_setter(instance):
    original = instance.JMBG
    instance.JMBG = original
    assert instance.JMBG == original



@given(instance=Putnik_strategy)
def test_putnik_ImePutnika_setter(instance):
    original = instance.ImePutnika
    instance.ImePutnika = original
    assert instance.ImePutnika == original



@given(instance=Putnik_strategy)
def test_putnik_AdresaPutnika_setter(instance):
    original = instance.AdresaPutnika
    instance.AdresaPutnika = original
    assert instance.AdresaPutnika == original



@given(instance=Putnik_strategy)
def test_putnik_PrezimePutnika_setter(instance):
    original = instance.PrezimePutnika
    instance.PrezimePutnika = original
    assert instance.PrezimePutnika == original



@given(instance=Putnik_strategy)
def test_putnik_PutnikID_setter(instance):
    original = instance.PutnikID
    instance.PutnikID = original
    assert instance.PutnikID == original



@given(instance=Putnik_strategy)
def test_putnik_KontaktPutnika_setter(instance):
    original = instance.KontaktPutnika
    instance.KontaktPutnika = original
    assert instance.KontaktPutnika == original



@given(instance=Putnik_strategy)
def test_putnik_GradPutnika_setter(instance):
    original = instance.GradPutnika
    instance.GradPutnika = original
    assert instance.GradPutnika == original
