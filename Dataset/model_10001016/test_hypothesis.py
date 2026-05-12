import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Korisnik_IS,
    Putnik,
    Osiguranje,
    Hotel,
    Rezervisanje,
    Destinacija,
    Karta,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_korisnik_is_is_not_abstract():
    assert not inspect.isabstract(Korisnik_IS)


def test_korisnik_is_constructor_exists():
    assert callable(Korisnik_IS.__init__)


def test_korisnik_is_constructor_args():
    sig = inspect.signature(Korisnik_IS.__init__)
    params = list(sig.parameters.keys())
    assert "KorisnikID" in params, "Missing parameter 'KorisnikID'"
    assert "PrezimeKorisnika" in params, "Missing parameter 'PrezimeKorisnika'"
    assert "ImeKorisnika" in params, "Missing parameter 'ImeKorisnika'"
    assert "Password" in params, "Missing parameter 'Password'"
    assert "UserName" in params, "Missing parameter 'UserName'"

def test_korisnik_is_has_KorisnikID():
    assert hasattr(Korisnik_IS, "KorisnikID")
    descriptor = None
    for klass in Korisnik_IS.__mro__:
        if "KorisnikID" in klass.__dict__:
            descriptor = klass.__dict__["KorisnikID"]
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

def test_korisnik_is_has_ImeKorisnika():
    assert hasattr(Korisnik_IS, "ImeKorisnika")
    descriptor = None
    for klass in Korisnik_IS.__mro__:
        if "ImeKorisnika" in klass.__dict__:
            descriptor = klass.__dict__["ImeKorisnika"]
            break
    assert isinstance(descriptor, property)

def test_korisnik_is_has_Password():
    assert hasattr(Korisnik_IS, "Password")
    descriptor = None
    for klass in Korisnik_IS.__mro__:
        if "Password" in klass.__dict__:
            descriptor = klass.__dict__["Password"]
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



def test_putnik_is_not_abstract():
    assert not inspect.isabstract(Putnik)


def test_putnik_constructor_exists():
    assert callable(Putnik.__init__)


def test_putnik_constructor_args():
    sig = inspect.signature(Putnik.__init__)
    params = list(sig.parameters.keys())
    assert "Adresa" in params, "Missing parameter 'Adresa'"
    assert "Mobilni" in params, "Missing parameter 'Mobilni'"
    assert "ImePut" in params, "Missing parameter 'ImePut'"
    assert "eMail" in params, "Missing parameter 'eMail'"
    assert "Grad" in params, "Missing parameter 'Grad'"
    assert "JMBG" in params, "Missing parameter 'JMBG'"
    assert "PrezimePut" in params, "Missing parameter 'PrezimePut'"
    assert "OsigID" in params, "Missing parameter 'OsigID'"
    assert "PutnikID" in params, "Missing parameter 'PutnikID'"

def test_putnik_has_Adresa():
    assert hasattr(Putnik, "Adresa")
    descriptor = None
    for klass in Putnik.__mro__:
        if "Adresa" in klass.__dict__:
            descriptor = klass.__dict__["Adresa"]
            break
    assert isinstance(descriptor, property)

def test_putnik_has_Mobilni():
    assert hasattr(Putnik, "Mobilni")
    descriptor = None
    for klass in Putnik.__mro__:
        if "Mobilni" in klass.__dict__:
            descriptor = klass.__dict__["Mobilni"]
            break
    assert isinstance(descriptor, property)

def test_putnik_has_ImePut():
    assert hasattr(Putnik, "ImePut")
    descriptor = None
    for klass in Putnik.__mro__:
        if "ImePut" in klass.__dict__:
            descriptor = klass.__dict__["ImePut"]
            break
    assert isinstance(descriptor, property)

def test_putnik_has_eMail():
    assert hasattr(Putnik, "eMail")
    descriptor = None
    for klass in Putnik.__mro__:
        if "eMail" in klass.__dict__:
            descriptor = klass.__dict__["eMail"]
            break
    assert isinstance(descriptor, property)

def test_putnik_has_Grad():
    assert hasattr(Putnik, "Grad")
    descriptor = None
    for klass in Putnik.__mro__:
        if "Grad" in klass.__dict__:
            descriptor = klass.__dict__["Grad"]
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

def test_putnik_has_PrezimePut():
    assert hasattr(Putnik, "PrezimePut")
    descriptor = None
    for klass in Putnik.__mro__:
        if "PrezimePut" in klass.__dict__:
            descriptor = klass.__dict__["PrezimePut"]
            break
    assert isinstance(descriptor, property)

def test_putnik_has_OsigID():
    assert hasattr(Putnik, "OsigID")
    descriptor = None
    for klass in Putnik.__mro__:
        if "OsigID" in klass.__dict__:
            descriptor = klass.__dict__["OsigID"]
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



def test_osiguranje_is_not_abstract():
    assert not inspect.isabstract(Osiguranje)


def test_osiguranje_constructor_exists():
    assert callable(Osiguranje.__init__)


def test_osiguranje_constructor_args():
    sig = inspect.signature(Osiguranje.__init__)
    params = list(sig.parameters.keys())
    assert "OsigID" in params, "Missing parameter 'OsigID'"
    assert "KucaOsiguranje" in params, "Missing parameter 'KucaOsiguranje'"

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



def test_hotel_is_not_abstract():
    assert not inspect.isabstract(Hotel)


def test_hotel_constructor_exists():
    assert callable(Hotel.__init__)


def test_hotel_constructor_args():
    sig = inspect.signature(Hotel.__init__)
    params = list(sig.parameters.keys())
    assert "CenaSmestaja" in params, "Missing parameter 'CenaSmestaja'"
    assert "SobaHotela" in params, "Missing parameter 'SobaHotela'"
    assert "HotelID" in params, "Missing parameter 'HotelID'"
    assert "UslugaHotela" in params, "Missing parameter 'UslugaHotela'"
    assert "DestiID" in params, "Missing parameter 'DestiID'"
    assert "ImeHotela" in params, "Missing parameter 'ImeHotela'"
    assert "SpratHotela" in params, "Missing parameter 'SpratHotela'"
    assert "AdresaHotela" in params, "Missing parameter 'AdresaHotela'"
    assert "DuzinaBoravka" in params, "Missing parameter 'DuzinaBoravka'"

def test_hotel_has_CenaSmestaja():
    assert hasattr(Hotel, "CenaSmestaja")
    descriptor = None
    for klass in Hotel.__mro__:
        if "CenaSmestaja" in klass.__dict__:
            descriptor = klass.__dict__["CenaSmestaja"]
            break
    assert isinstance(descriptor, property)

def test_hotel_has_SobaHotela():
    assert hasattr(Hotel, "SobaHotela")
    descriptor = None
    for klass in Hotel.__mro__:
        if "SobaHotela" in klass.__dict__:
            descriptor = klass.__dict__["SobaHotela"]
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

def test_hotel_has_UslugaHotela():
    assert hasattr(Hotel, "UslugaHotela")
    descriptor = None
    for klass in Hotel.__mro__:
        if "UslugaHotela" in klass.__dict__:
            descriptor = klass.__dict__["UslugaHotela"]
            break
    assert isinstance(descriptor, property)

def test_hotel_has_DestiID():
    assert hasattr(Hotel, "DestiID")
    descriptor = None
    for klass in Hotel.__mro__:
        if "DestiID" in klass.__dict__:
            descriptor = klass.__dict__["DestiID"]
            break
    assert isinstance(descriptor, property)

def test_hotel_has_ImeHotela():
    assert hasattr(Hotel, "ImeHotela")
    descriptor = None
    for klass in Hotel.__mro__:
        if "ImeHotela" in klass.__dict__:
            descriptor = klass.__dict__["ImeHotela"]
            break
    assert isinstance(descriptor, property)

def test_hotel_has_SpratHotela():
    assert hasattr(Hotel, "SpratHotela")
    descriptor = None
    for klass in Hotel.__mro__:
        if "SpratHotela" in klass.__dict__:
            descriptor = klass.__dict__["SpratHotela"]
            break
    assert isinstance(descriptor, property)

def test_hotel_has_AdresaHotela():
    assert hasattr(Hotel, "AdresaHotela")
    descriptor = None
    for klass in Hotel.__mro__:
        if "AdresaHotela" in klass.__dict__:
            descriptor = klass.__dict__["AdresaHotela"]
            break
    assert isinstance(descriptor, property)

def test_hotel_has_DuzinaBoravka():
    assert hasattr(Hotel, "DuzinaBoravka")
    descriptor = None
    for klass in Hotel.__mro__:
        if "DuzinaBoravka" in klass.__dict__:
            descriptor = klass.__dict__["DuzinaBoravka"]
            break
    assert isinstance(descriptor, property)



def test_rezervisanje_is_not_abstract():
    assert not inspect.isabstract(Rezervisanje)


def test_rezervisanje_constructor_exists():
    assert callable(Rezervisanje.__init__)


def test_rezervisanje_constructor_args():
    sig = inspect.signature(Rezervisanje.__init__)
    params = list(sig.parameters.keys())
    assert "Cena" in params, "Missing parameter 'Cena'"
    assert "KorisnikID" in params, "Missing parameter 'KorisnikID'"
    assert "DatumPolaska" in params, "Missing parameter 'DatumPolaska'"
    assert "SlobMesto" in params, "Missing parameter 'SlobMesto'"
    assert "RezerID" in params, "Missing parameter 'RezerID'"
    assert "DatumDolaska" in params, "Missing parameter 'DatumDolaska'"
    assert "DestiID" in params, "Missing parameter 'DestiID'"
    assert "PutnikID" in params, "Missing parameter 'PutnikID'"

def test_rezervisanje_has_Cena():
    assert hasattr(Rezervisanje, "Cena")
    descriptor = None
    for klass in Rezervisanje.__mro__:
        if "Cena" in klass.__dict__:
            descriptor = klass.__dict__["Cena"]
            break
    assert isinstance(descriptor, property)

def test_rezervisanje_has_KorisnikID():
    assert hasattr(Rezervisanje, "KorisnikID")
    descriptor = None
    for klass in Rezervisanje.__mro__:
        if "KorisnikID" in klass.__dict__:
            descriptor = klass.__dict__["KorisnikID"]
            break
    assert isinstance(descriptor, property)

def test_rezervisanje_has_DatumPolaska():
    assert hasattr(Rezervisanje, "DatumPolaska")
    descriptor = None
    for klass in Rezervisanje.__mro__:
        if "DatumPolaska" in klass.__dict__:
            descriptor = klass.__dict__["DatumPolaska"]
            break
    assert isinstance(descriptor, property)

def test_rezervisanje_has_SlobMesto():
    assert hasattr(Rezervisanje, "SlobMesto")
    descriptor = None
    for klass in Rezervisanje.__mro__:
        if "SlobMesto" in klass.__dict__:
            descriptor = klass.__dict__["SlobMesto"]
            break
    assert isinstance(descriptor, property)

def test_rezervisanje_has_RezerID():
    assert hasattr(Rezervisanje, "RezerID")
    descriptor = None
    for klass in Rezervisanje.__mro__:
        if "RezerID" in klass.__dict__:
            descriptor = klass.__dict__["RezerID"]
            break
    assert isinstance(descriptor, property)

def test_rezervisanje_has_DatumDolaska():
    assert hasattr(Rezervisanje, "DatumDolaska")
    descriptor = None
    for klass in Rezervisanje.__mro__:
        if "DatumDolaska" in klass.__dict__:
            descriptor = klass.__dict__["DatumDolaska"]
            break
    assert isinstance(descriptor, property)

def test_rezervisanje_has_DestiID():
    assert hasattr(Rezervisanje, "DestiID")
    descriptor = None
    for klass in Rezervisanje.__mro__:
        if "DestiID" in klass.__dict__:
            descriptor = klass.__dict__["DestiID"]
            break
    assert isinstance(descriptor, property)

def test_rezervisanje_has_PutnikID():
    assert hasattr(Rezervisanje, "PutnikID")
    descriptor = None
    for klass in Rezervisanje.__mro__:
        if "PutnikID" in klass.__dict__:
            descriptor = klass.__dict__["PutnikID"]
            break
    assert isinstance(descriptor, property)



def test_destinacija_is_not_abstract():
    assert not inspect.isabstract(Destinacija)


def test_destinacija_constructor_exists():
    assert callable(Destinacija.__init__)


def test_destinacija_constructor_args():
    sig = inspect.signature(Destinacija.__init__)
    params = list(sig.parameters.keys())
    assert "DesGrad" in params, "Missing parameter 'DesGrad'"
    assert "DesDrzava" in params, "Missing parameter 'DesDrzava'"
    assert "DestiID" in params, "Missing parameter 'DestiID'"

def test_destinacija_has_DesGrad():
    assert hasattr(Destinacija, "DesGrad")
    descriptor = None
    for klass in Destinacija.__mro__:
        if "DesGrad" in klass.__dict__:
            descriptor = klass.__dict__["DesGrad"]
            break
    assert isinstance(descriptor, property)

def test_destinacija_has_DesDrzava():
    assert hasattr(Destinacija, "DesDrzava")
    descriptor = None
    for klass in Destinacija.__mro__:
        if "DesDrzava" in klass.__dict__:
            descriptor = klass.__dict__["DesDrzava"]
            break
    assert isinstance(descriptor, property)

def test_destinacija_has_DestiID():
    assert hasattr(Destinacija, "DestiID")
    descriptor = None
    for klass in Destinacija.__mro__:
        if "DestiID" in klass.__dict__:
            descriptor = klass.__dict__["DestiID"]
            break
    assert isinstance(descriptor, property)



def test_karta_is_not_abstract():
    assert not inspect.isabstract(Karta)


def test_karta_constructor_exists():
    assert callable(Karta.__init__)


def test_karta_constructor_args():
    sig = inspect.signature(Karta.__init__)
    params = list(sig.parameters.keys())
    assert "VremeOdlaska" in params, "Missing parameter 'VremeOdlaska'"
    assert "RezerID" in params, "Missing parameter 'RezerID'"
    assert "PovratakKarta" in params, "Missing parameter 'PovratakKarta'"
    assert "KartaID" in params, "Missing parameter 'KartaID'"
    assert "CenaKarte" in params, "Missing parameter 'CenaKarte'"
    assert "VremePovratka" in params, "Missing parameter 'VremePovratka'"
    assert "OdlazakKarta" in params, "Missing parameter 'OdlazakKarta'"

def test_karta_has_VremeOdlaska():
    assert hasattr(Karta, "VremeOdlaska")
    descriptor = None
    for klass in Karta.__mro__:
        if "VremeOdlaska" in klass.__dict__:
            descriptor = klass.__dict__["VremeOdlaska"]
            break
    assert isinstance(descriptor, property)

def test_karta_has_RezerID():
    assert hasattr(Karta, "RezerID")
    descriptor = None
    for klass in Karta.__mro__:
        if "RezerID" in klass.__dict__:
            descriptor = klass.__dict__["RezerID"]
            break
    assert isinstance(descriptor, property)

def test_karta_has_PovratakKarta():
    assert hasattr(Karta, "PovratakKarta")
    descriptor = None
    for klass in Karta.__mro__:
        if "PovratakKarta" in klass.__dict__:
            descriptor = klass.__dict__["PovratakKarta"]
            break
    assert isinstance(descriptor, property)

def test_karta_has_KartaID():
    assert hasattr(Karta, "KartaID")
    descriptor = None
    for klass in Karta.__mro__:
        if "KartaID" in klass.__dict__:
            descriptor = klass.__dict__["KartaID"]
            break
    assert isinstance(descriptor, property)

def test_karta_has_CenaKarte():
    assert hasattr(Karta, "CenaKarte")
    descriptor = None
    for klass in Karta.__mro__:
        if "CenaKarte" in klass.__dict__:
            descriptor = klass.__dict__["CenaKarte"]
            break
    assert isinstance(descriptor, property)

def test_karta_has_VremePovratka():
    assert hasattr(Karta, "VremePovratka")
    descriptor = None
    for klass in Karta.__mro__:
        if "VremePovratka" in klass.__dict__:
            descriptor = klass.__dict__["VremePovratka"]
            break
    assert isinstance(descriptor, property)

def test_karta_has_OdlazakKarta():
    assert hasattr(Karta, "OdlazakKarta")
    descriptor = None
    for klass in Karta.__mro__:
        if "OdlazakKarta" in klass.__dict__:
            descriptor = klass.__dict__["OdlazakKarta"]
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
Korisnik_IS_strategy = st.builds(
    Korisnik_IS,
    KorisnikID=
        st.integers(),
    PrezimeKorisnika=
        safe_text,
    ImeKorisnika=
        safe_text,
    Password=
        safe_text,
    UserName=
        safe_text
)
Putnik_strategy = st.builds(
    Putnik,
    Adresa=
        safe_text,
    Mobilni=
        st.integers(),
    ImePut=
        safe_text,
    eMail=
        safe_text,
    Grad=
        safe_text,
    JMBG=
        safe_text,
    PrezimePut=
        safe_text,
    OsigID=
        st.integers(),
    PutnikID=
        st.integers()
)
Osiguranje_strategy = st.builds(
    Osiguranje,
    OsigID=
        st.integers(),
    KucaOsiguranje=
        safe_text
)
Hotel_strategy = st.builds(
    Hotel,
    CenaSmestaja=
        safe_text,
    SobaHotela=
        st.integers(),
    HotelID=
        st.integers(),
    UslugaHotela=
        safe_text,
    DestiID=
        st.integers(),
    ImeHotela=
        safe_text,
    SpratHotela=
        st.integers(),
    AdresaHotela=
        safe_text,
    DuzinaBoravka=
        st.integers()
)
Rezervisanje_strategy = st.builds(
    Rezervisanje,
    Cena=
        safe_text,
    KorisnikID=
        st.integers(),
    DatumPolaska=
        safe_text,
    SlobMesto=
        st.booleans(),
    RezerID=
        st.integers(),
    DatumDolaska=
        safe_text,
    DestiID=
        st.integers(),
    PutnikID=
        st.integers()
)
Destinacija_strategy = st.builds(
    Destinacija,
    DesGrad=
        safe_text,
    DesDrzava=
        safe_text,
    DestiID=
        st.integers()
)
Karta_strategy = st.builds(
    Karta,
    VremeOdlaska=
        safe_text,
    RezerID=
        st.integers(),
    PovratakKarta=
        safe_text,
    KartaID=
        st.integers(),
    CenaKarte=
        safe_text,
    VremePovratka=
        safe_text,
    OdlazakKarta=
        safe_text
)

@given(instance=Korisnik_IS_strategy)
@settings(max_examples=50)
def test_korisnik_is_instantiation(instance):
    assert isinstance(instance, Korisnik_IS)



@given(instance=Korisnik_IS_strategy)
def test_korisnik_is_KorisnikID_setter(instance):
    original = instance.KorisnikID
    instance.KorisnikID = original
    assert instance.KorisnikID == original



@given(instance=Korisnik_IS_strategy)
def test_korisnik_is_PrezimeKorisnika_setter(instance):
    original = instance.PrezimeKorisnika
    instance.PrezimeKorisnika = original
    assert instance.PrezimeKorisnika == original



@given(instance=Korisnik_IS_strategy)
def test_korisnik_is_ImeKorisnika_setter(instance):
    original = instance.ImeKorisnika
    instance.ImeKorisnika = original
    assert instance.ImeKorisnika == original



@given(instance=Korisnik_IS_strategy)
def test_korisnik_is_Password_setter(instance):
    original = instance.Password
    instance.Password = original
    assert instance.Password == original



@given(instance=Korisnik_IS_strategy)
def test_korisnik_is_UserName_setter(instance):
    original = instance.UserName
    instance.UserName = original
    assert instance.UserName == original

@given(instance=Putnik_strategy)
@settings(max_examples=50)
def test_putnik_instantiation(instance):
    assert isinstance(instance, Putnik)



@given(instance=Putnik_strategy)
def test_putnik_Adresa_setter(instance):
    original = instance.Adresa
    instance.Adresa = original
    assert instance.Adresa == original



@given(instance=Putnik_strategy)
def test_putnik_Mobilni_setter(instance):
    original = instance.Mobilni
    instance.Mobilni = original
    assert instance.Mobilni == original



@given(instance=Putnik_strategy)
def test_putnik_ImePut_setter(instance):
    original = instance.ImePut
    instance.ImePut = original
    assert instance.ImePut == original



@given(instance=Putnik_strategy)
def test_putnik_eMail_setter(instance):
    original = instance.eMail
    instance.eMail = original
    assert instance.eMail == original



@given(instance=Putnik_strategy)
def test_putnik_Grad_setter(instance):
    original = instance.Grad
    instance.Grad = original
    assert instance.Grad == original



@given(instance=Putnik_strategy)
def test_putnik_JMBG_setter(instance):
    original = instance.JMBG
    instance.JMBG = original
    assert instance.JMBG == original



@given(instance=Putnik_strategy)
def test_putnik_PrezimePut_setter(instance):
    original = instance.PrezimePut
    instance.PrezimePut = original
    assert instance.PrezimePut == original



@given(instance=Putnik_strategy)
def test_putnik_OsigID_setter(instance):
    original = instance.OsigID
    instance.OsigID = original
    assert instance.OsigID == original



@given(instance=Putnik_strategy)
def test_putnik_PutnikID_setter(instance):
    original = instance.PutnikID
    instance.PutnikID = original
    assert instance.PutnikID == original

@given(instance=Osiguranje_strategy)
@settings(max_examples=50)
def test_osiguranje_instantiation(instance):
    assert isinstance(instance, Osiguranje)



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

@given(instance=Hotel_strategy)
@settings(max_examples=50)
def test_hotel_instantiation(instance):
    assert isinstance(instance, Hotel)



@given(instance=Hotel_strategy)
def test_hotel_CenaSmestaja_setter(instance):
    original = instance.CenaSmestaja
    instance.CenaSmestaja = original
    assert instance.CenaSmestaja == original



@given(instance=Hotel_strategy)
def test_hotel_SobaHotela_setter(instance):
    original = instance.SobaHotela
    instance.SobaHotela = original
    assert instance.SobaHotela == original



@given(instance=Hotel_strategy)
def test_hotel_HotelID_setter(instance):
    original = instance.HotelID
    instance.HotelID = original
    assert instance.HotelID == original



@given(instance=Hotel_strategy)
def test_hotel_UslugaHotela_setter(instance):
    original = instance.UslugaHotela
    instance.UslugaHotela = original
    assert instance.UslugaHotela == original



@given(instance=Hotel_strategy)
def test_hotel_DestiID_setter(instance):
    original = instance.DestiID
    instance.DestiID = original
    assert instance.DestiID == original



@given(instance=Hotel_strategy)
def test_hotel_ImeHotela_setter(instance):
    original = instance.ImeHotela
    instance.ImeHotela = original
    assert instance.ImeHotela == original



@given(instance=Hotel_strategy)
def test_hotel_SpratHotela_setter(instance):
    original = instance.SpratHotela
    instance.SpratHotela = original
    assert instance.SpratHotela == original



@given(instance=Hotel_strategy)
def test_hotel_AdresaHotela_setter(instance):
    original = instance.AdresaHotela
    instance.AdresaHotela = original
    assert instance.AdresaHotela == original



@given(instance=Hotel_strategy)
def test_hotel_DuzinaBoravka_setter(instance):
    original = instance.DuzinaBoravka
    instance.DuzinaBoravka = original
    assert instance.DuzinaBoravka == original

@given(instance=Rezervisanje_strategy)
@settings(max_examples=50)
def test_rezervisanje_instantiation(instance):
    assert isinstance(instance, Rezervisanje)



@given(instance=Rezervisanje_strategy)
def test_rezervisanje_Cena_setter(instance):
    original = instance.Cena
    instance.Cena = original
    assert instance.Cena == original



@given(instance=Rezervisanje_strategy)
def test_rezervisanje_KorisnikID_setter(instance):
    original = instance.KorisnikID
    instance.KorisnikID = original
    assert instance.KorisnikID == original



@given(instance=Rezervisanje_strategy)
def test_rezervisanje_DatumPolaska_setter(instance):
    original = instance.DatumPolaska
    instance.DatumPolaska = original
    assert instance.DatumPolaska == original



@given(instance=Rezervisanje_strategy)
def test_rezervisanje_SlobMesto_setter(instance):
    original = instance.SlobMesto
    instance.SlobMesto = original
    assert instance.SlobMesto == original



@given(instance=Rezervisanje_strategy)
def test_rezervisanje_RezerID_setter(instance):
    original = instance.RezerID
    instance.RezerID = original
    assert instance.RezerID == original



@given(instance=Rezervisanje_strategy)
def test_rezervisanje_DatumDolaska_setter(instance):
    original = instance.DatumDolaska
    instance.DatumDolaska = original
    assert instance.DatumDolaska == original



@given(instance=Rezervisanje_strategy)
def test_rezervisanje_DestiID_setter(instance):
    original = instance.DestiID
    instance.DestiID = original
    assert instance.DestiID == original



@given(instance=Rezervisanje_strategy)
def test_rezervisanje_PutnikID_setter(instance):
    original = instance.PutnikID
    instance.PutnikID = original
    assert instance.PutnikID == original

@given(instance=Destinacija_strategy)
@settings(max_examples=50)
def test_destinacija_instantiation(instance):
    assert isinstance(instance, Destinacija)



@given(instance=Destinacija_strategy)
def test_destinacija_DesGrad_setter(instance):
    original = instance.DesGrad
    instance.DesGrad = original
    assert instance.DesGrad == original



@given(instance=Destinacija_strategy)
def test_destinacija_DesDrzava_setter(instance):
    original = instance.DesDrzava
    instance.DesDrzava = original
    assert instance.DesDrzava == original



@given(instance=Destinacija_strategy)
def test_destinacija_DestiID_setter(instance):
    original = instance.DestiID
    instance.DestiID = original
    assert instance.DestiID == original

@given(instance=Karta_strategy)
@settings(max_examples=50)
def test_karta_instantiation(instance):
    assert isinstance(instance, Karta)



@given(instance=Karta_strategy)
def test_karta_VremeOdlaska_setter(instance):
    original = instance.VremeOdlaska
    instance.VremeOdlaska = original
    assert instance.VremeOdlaska == original



@given(instance=Karta_strategy)
def test_karta_RezerID_setter(instance):
    original = instance.RezerID
    instance.RezerID = original
    assert instance.RezerID == original



@given(instance=Karta_strategy)
def test_karta_PovratakKarta_setter(instance):
    original = instance.PovratakKarta
    instance.PovratakKarta = original
    assert instance.PovratakKarta == original



@given(instance=Karta_strategy)
def test_karta_KartaID_setter(instance):
    original = instance.KartaID
    instance.KartaID = original
    assert instance.KartaID == original



@given(instance=Karta_strategy)
def test_karta_CenaKarte_setter(instance):
    original = instance.CenaKarte
    instance.CenaKarte = original
    assert instance.CenaKarte == original



@given(instance=Karta_strategy)
def test_karta_VremePovratka_setter(instance):
    original = instance.VremePovratka
    instance.VremePovratka = original
    assert instance.VremePovratka == original



@given(instance=Karta_strategy)
def test_karta_OdlazakKarta_setter(instance):
    original = instance.OdlazakKarta
    instance.OdlazakKarta = original
    assert instance.OdlazakKarta == original
