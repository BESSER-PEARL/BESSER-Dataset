import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Reservierung,
    Entlehnausweis,
    Kunde,
    Entlehnung,
    Exemplar,
    Entleihungsgegenstand,
    Zeitschrift,
    Videos_DVDS,
    Buch,
    ExemplarStatus,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_reservierung_is_not_abstract():
    assert not inspect.isabstract(Reservierung)


def test_reservierung_constructor_exists():
    assert callable(Reservierung.__init__)


def test_reservierung_constructor_args():
    sig = inspect.signature(Reservierung.__init__)
    params = list(sig.parameters.keys())
    assert "reservierungsEnde" in params, "Missing parameter 'reservierungsEnde'"
    assert "reservierungsDatum" in params, "Missing parameter 'reservierungsDatum'"

def test_reservierung_has_reservierungsEnde():
    assert hasattr(Reservierung, "reservierungsEnde")
    descriptor = None
    for klass in Reservierung.__mro__:
        if "reservierungsEnde" in klass.__dict__:
            descriptor = klass.__dict__["reservierungsEnde"]
            break
    assert isinstance(descriptor, property)

def test_reservierung_has_reservierungsDatum():
    assert hasattr(Reservierung, "reservierungsDatum")
    descriptor = None
    for klass in Reservierung.__mro__:
        if "reservierungsDatum" in klass.__dict__:
            descriptor = klass.__dict__["reservierungsDatum"]
            break
    assert isinstance(descriptor, property)



def test_entlehnausweis_is_not_abstract():
    assert not inspect.isabstract(Entlehnausweis)


def test_entlehnausweis_constructor_exists():
    assert callable(Entlehnausweis.__init__)


def test_entlehnausweis_constructor_args():
    sig = inspect.signature(Entlehnausweis.__init__)
    params = list(sig.parameters.keys())
    assert "g_ltigKeitsDatum" in params, "Missing parameter 'g_ltigKeitsDatum'"
    assert "id" in params, "Missing parameter 'id'"

def test_entlehnausweis_has_g_ltigKeitsDatum():
    assert hasattr(Entlehnausweis, "g_ltigKeitsDatum")
    descriptor = None
    for klass in Entlehnausweis.__mro__:
        if "g_ltigKeitsDatum" in klass.__dict__:
            descriptor = klass.__dict__["g_ltigKeitsDatum"]
            break
    assert isinstance(descriptor, property)

def test_entlehnausweis_has_id():
    assert hasattr(Entlehnausweis, "id")
    descriptor = None
    for klass in Entlehnausweis.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_kunde_is_not_abstract():
    assert not inspect.isabstract(Kunde)


def test_kunde_constructor_exists():
    assert callable(Kunde.__init__)


def test_kunde_constructor_args():
    sig = inspect.signature(Kunde.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Anschrift" in params, "Missing parameter 'Anschrift'"

def test_kunde_has_Name():
    assert hasattr(Kunde, "Name")
    descriptor = None
    for klass in Kunde.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_kunde_has_Anschrift():
    assert hasattr(Kunde, "Anschrift")
    descriptor = None
    for klass in Kunde.__mro__:
        if "Anschrift" in klass.__dict__:
            descriptor = klass.__dict__["Anschrift"]
            break
    assert isinstance(descriptor, property)



def test_entlehnung_is_not_abstract():
    assert not inspect.isabstract(Entlehnung)


def test_entlehnung_constructor_exists():
    assert callable(Entlehnung.__init__)


def test_entlehnung_constructor_args():
    sig = inspect.signature(Entlehnung.__init__)
    params = list(sig.parameters.keys())
    assert "ausLeihDatun" in params, "Missing parameter 'ausLeihDatun'"
    assert "rueckGDatum" in params, "Missing parameter 'rueckGDatum'"
    assert "ausLeihFrist" in params, "Missing parameter 'ausLeihFrist'"
    assert "maxAnzahlFristTage" in params, "Missing parameter 'maxAnzahlFristTage'"

def test_entlehnung_has_ausLeihDatun():
    assert hasattr(Entlehnung, "ausLeihDatun")
    descriptor = None
    for klass in Entlehnung.__mro__:
        if "ausLeihDatun" in klass.__dict__:
            descriptor = klass.__dict__["ausLeihDatun"]
            break
    assert isinstance(descriptor, property)

def test_entlehnung_has_rueckGDatum():
    assert hasattr(Entlehnung, "rueckGDatum")
    descriptor = None
    for klass in Entlehnung.__mro__:
        if "rueckGDatum" in klass.__dict__:
            descriptor = klass.__dict__["rueckGDatum"]
            break
    assert isinstance(descriptor, property)

def test_entlehnung_has_ausLeihFrist():
    assert hasattr(Entlehnung, "ausLeihFrist")
    descriptor = None
    for klass in Entlehnung.__mro__:
        if "ausLeihFrist" in klass.__dict__:
            descriptor = klass.__dict__["ausLeihFrist"]
            break
    assert isinstance(descriptor, property)

def test_entlehnung_has_maxAnzahlFristTage():
    assert hasattr(Entlehnung, "maxAnzahlFristTage")
    descriptor = None
    for klass in Entlehnung.__mro__:
        if "maxAnzahlFristTage" in klass.__dict__:
            descriptor = klass.__dict__["maxAnzahlFristTage"]
            break
    assert isinstance(descriptor, property)



def test_exemplar_is_not_abstract():
    assert not inspect.isabstract(Exemplar)


def test_exemplar_constructor_exists():
    assert callable(Exemplar.__init__)


def test_exemplar_constructor_args():
    sig = inspect.signature(Exemplar.__init__)
    params = list(sig.parameters.keys())
    assert "exemplarNummer" in params, "Missing parameter 'exemplarNummer'"

def test_exemplar_has_exemplarNummer():
    assert hasattr(Exemplar, "exemplarNummer")
    descriptor = None
    for klass in Exemplar.__mro__:
        if "exemplarNummer" in klass.__dict__:
            descriptor = klass.__dict__["exemplarNummer"]
            break
    assert isinstance(descriptor, property)



def test_entleihungsgegenstand_is_not_abstract():
    assert not inspect.isabstract(Entleihungsgegenstand)


def test_entleihungsgegenstand_constructor_exists():
    assert callable(Entleihungsgegenstand.__init__)


def test_entleihungsgegenstand_constructor_args():
    sig = inspect.signature(Entleihungsgegenstand.__init__)
    params = list(sig.parameters.keys())
    assert "einkaufspreis" in params, "Missing parameter 'einkaufspreis'"
    assert "kurzbeschreibung" in params, "Missing parameter 'kurzbeschreibung'"
    assert "titel" in params, "Missing parameter 'titel'"

def test_entleihungsgegenstand_has_einkaufspreis():
    assert hasattr(Entleihungsgegenstand, "einkaufspreis")
    descriptor = None
    for klass in Entleihungsgegenstand.__mro__:
        if "einkaufspreis" in klass.__dict__:
            descriptor = klass.__dict__["einkaufspreis"]
            break
    assert isinstance(descriptor, property)

def test_entleihungsgegenstand_has_kurzbeschreibung():
    assert hasattr(Entleihungsgegenstand, "kurzbeschreibung")
    descriptor = None
    for klass in Entleihungsgegenstand.__mro__:
        if "kurzbeschreibung" in klass.__dict__:
            descriptor = klass.__dict__["kurzbeschreibung"]
            break
    assert isinstance(descriptor, property)

def test_entleihungsgegenstand_has_titel():
    assert hasattr(Entleihungsgegenstand, "titel")
    descriptor = None
    for klass in Entleihungsgegenstand.__mro__:
        if "titel" in klass.__dict__:
            descriptor = klass.__dict__["titel"]
            break
    assert isinstance(descriptor, property)



def test_zeitschrift_is_not_abstract():
    assert not inspect.isabstract(Zeitschrift)


def test_zeitschrift_constructor_exists():
    assert callable(Zeitschrift.__init__)


def test_zeitschrift_constructor_args():
    sig = inspect.signature(Zeitschrift.__init__)
    params = list(sig.parameters.keys())
    assert "Jahrgang" in params, "Missing parameter 'Jahrgang'"
    assert "Ausgabe" in params, "Missing parameter 'Ausgabe'"

def test_zeitschrift_has_Jahrgang():
    assert hasattr(Zeitschrift, "Jahrgang")
    descriptor = None
    for klass in Zeitschrift.__mro__:
        if "Jahrgang" in klass.__dict__:
            descriptor = klass.__dict__["Jahrgang"]
            break
    assert isinstance(descriptor, property)

def test_zeitschrift_has_Ausgabe():
    assert hasattr(Zeitschrift, "Ausgabe")
    descriptor = None
    for klass in Zeitschrift.__mro__:
        if "Ausgabe" in klass.__dict__:
            descriptor = klass.__dict__["Ausgabe"]
            break
    assert isinstance(descriptor, property)



def test_videos_dvds_is_not_abstract():
    assert not inspect.isabstract(Videos_DVDS)


def test_videos_dvds_constructor_exists():
    assert callable(Videos_DVDS.__init__)


def test_videos_dvds_constructor_args():
    sig = inspect.signature(Videos_DVDS.__init__)
    params = list(sig.parameters.keys())
    assert "entLeihungsGeb_hr" in params, "Missing parameter 'entLeihungsGeb_hr'"
    assert "AnzahlEntlehnungen" in params, "Missing parameter 'AnzahlEntlehnungen'"
    assert "Regisseur" in params, "Missing parameter 'Regisseur'"
    assert "Laufzeit" in params, "Missing parameter 'Laufzeit'"

def test_videos_dvds_has_entLeihungsGeb_hr():
    assert hasattr(Videos_DVDS, "entLeihungsGeb_hr")
    descriptor = None
    for klass in Videos_DVDS.__mro__:
        if "entLeihungsGeb_hr" in klass.__dict__:
            descriptor = klass.__dict__["entLeihungsGeb_hr"]
            break
    assert isinstance(descriptor, property)

def test_videos_dvds_has_AnzahlEntlehnungen():
    assert hasattr(Videos_DVDS, "AnzahlEntlehnungen")
    descriptor = None
    for klass in Videos_DVDS.__mro__:
        if "AnzahlEntlehnungen" in klass.__dict__:
            descriptor = klass.__dict__["AnzahlEntlehnungen"]
            break
    assert isinstance(descriptor, property)

def test_videos_dvds_has_Regisseur():
    assert hasattr(Videos_DVDS, "Regisseur")
    descriptor = None
    for klass in Videos_DVDS.__mro__:
        if "Regisseur" in klass.__dict__:
            descriptor = klass.__dict__["Regisseur"]
            break
    assert isinstance(descriptor, property)

def test_videos_dvds_has_Laufzeit():
    assert hasattr(Videos_DVDS, "Laufzeit")
    descriptor = None
    for klass in Videos_DVDS.__mro__:
        if "Laufzeit" in klass.__dict__:
            descriptor = klass.__dict__["Laufzeit"]
            break
    assert isinstance(descriptor, property)



def test_buch_is_not_abstract():
    assert not inspect.isabstract(Buch)


def test_buch_constructor_exists():
    assert callable(Buch.__init__)


def test_buch_constructor_args():
    sig = inspect.signature(Buch.__init__)
    params = list(sig.parameters.keys())
    assert "ISBN" in params, "Missing parameter 'ISBN'"
    assert "Autor" in params, "Missing parameter 'Autor'"

def test_buch_has_ISBN():
    assert hasattr(Buch, "ISBN")
    descriptor = None
    for klass in Buch.__mro__:
        if "ISBN" in klass.__dict__:
            descriptor = klass.__dict__["ISBN"]
            break
    assert isinstance(descriptor, property)

def test_buch_has_Autor():
    assert hasattr(Buch, "Autor")
    descriptor = None
    for klass in Buch.__mro__:
        if "Autor" in klass.__dict__:
            descriptor = klass.__dict__["Autor"]
            break
    assert isinstance(descriptor, property)

def test_exemplarstatus_exists():
    # Check that the Enumeration exists
    assert ExemplarStatus is not None

def test_exemplarstatus_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ExemplarStatus]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ExemplarStatus"


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
Reservierung_strategy = st.builds(
    Reservierung,
    reservierungsEnde=
        safe_text,
    reservierungsDatum=
        safe_text
)
Entlehnausweis_strategy = st.builds(
    Entlehnausweis,
    g_ltigKeitsDatum=
        safe_text,
    id=
        st.integers()
)
Kunde_strategy = st.builds(
    Kunde,
    Name=
        safe_text,
    Anschrift=
        safe_text
)
Entlehnung_strategy = st.builds(
    Entlehnung,
    ausLeihDatun=
        safe_text,
    rueckGDatum=
        safe_text,
    ausLeihFrist=
        safe_text,
    maxAnzahlFristTage=
        st.integers()
)
Exemplar_strategy = st.builds(
    Exemplar,
    exemplarNummer=
        safe_text
)
Entleihungsgegenstand_strategy = st.builds(
    Entleihungsgegenstand,
    einkaufspreis=
        safe_text,
    kurzbeschreibung=
        safe_text,
    titel=
        safe_text
)
Zeitschrift_strategy = st.builds(
    Zeitschrift,
    Jahrgang=
        st.integers(),
    Ausgabe=
        safe_text
)
Videos_DVDS_strategy = st.builds(
    Videos_DVDS,
    entLeihungsGeb_hr=
        safe_text,
    AnzahlEntlehnungen=
        st.integers(),
    Regisseur=
        safe_text,
    Laufzeit=
        st.integers()
)
Buch_strategy = st.builds(
    Buch,
    ISBN=
        safe_text,
    Autor=
        safe_text
)

@given(instance=Reservierung_strategy)
@settings(max_examples=50)
def test_reservierung_instantiation(instance):
    assert isinstance(instance, Reservierung)



@given(instance=Reservierung_strategy)
def test_reservierung_reservierungsEnde_setter(instance):
    original = instance.reservierungsEnde
    instance.reservierungsEnde = original
    assert instance.reservierungsEnde == original



@given(instance=Reservierung_strategy)
def test_reservierung_reservierungsDatum_setter(instance):
    original = instance.reservierungsDatum
    instance.reservierungsDatum = original
    assert instance.reservierungsDatum == original

@given(instance=Entlehnausweis_strategy)
@settings(max_examples=50)
def test_entlehnausweis_instantiation(instance):
    assert isinstance(instance, Entlehnausweis)



@given(instance=Entlehnausweis_strategy)
def test_entlehnausweis_g_ltigKeitsDatum_setter(instance):
    original = instance.g_ltigKeitsDatum
    instance.g_ltigKeitsDatum = original
    assert instance.g_ltigKeitsDatum == original



@given(instance=Entlehnausweis_strategy)
def test_entlehnausweis_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Kunde_strategy)
@settings(max_examples=50)
def test_kunde_instantiation(instance):
    assert isinstance(instance, Kunde)



@given(instance=Kunde_strategy)
def test_kunde_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=Kunde_strategy)
def test_kunde_Anschrift_setter(instance):
    original = instance.Anschrift
    instance.Anschrift = original
    assert instance.Anschrift == original

@given(instance=Entlehnung_strategy)
@settings(max_examples=50)
def test_entlehnung_instantiation(instance):
    assert isinstance(instance, Entlehnung)



@given(instance=Entlehnung_strategy)
def test_entlehnung_ausLeihDatun_setter(instance):
    original = instance.ausLeihDatun
    instance.ausLeihDatun = original
    assert instance.ausLeihDatun == original



@given(instance=Entlehnung_strategy)
def test_entlehnung_rueckGDatum_setter(instance):
    original = instance.rueckGDatum
    instance.rueckGDatum = original
    assert instance.rueckGDatum == original



@given(instance=Entlehnung_strategy)
def test_entlehnung_ausLeihFrist_setter(instance):
    original = instance.ausLeihFrist
    instance.ausLeihFrist = original
    assert instance.ausLeihFrist == original



@given(instance=Entlehnung_strategy)
def test_entlehnung_maxAnzahlFristTage_setter(instance):
    original = instance.maxAnzahlFristTage
    instance.maxAnzahlFristTage = original
    assert instance.maxAnzahlFristTage == original

@given(instance=Exemplar_strategy)
@settings(max_examples=50)
def test_exemplar_instantiation(instance):
    assert isinstance(instance, Exemplar)



@given(instance=Exemplar_strategy)
def test_exemplar_exemplarNummer_setter(instance):
    original = instance.exemplarNummer
    instance.exemplarNummer = original
    assert instance.exemplarNummer == original

@given(instance=Entleihungsgegenstand_strategy)
@settings(max_examples=50)
def test_entleihungsgegenstand_instantiation(instance):
    assert isinstance(instance, Entleihungsgegenstand)



@given(instance=Entleihungsgegenstand_strategy)
def test_entleihungsgegenstand_einkaufspreis_setter(instance):
    original = instance.einkaufspreis
    instance.einkaufspreis = original
    assert instance.einkaufspreis == original



@given(instance=Entleihungsgegenstand_strategy)
def test_entleihungsgegenstand_kurzbeschreibung_setter(instance):
    original = instance.kurzbeschreibung
    instance.kurzbeschreibung = original
    assert instance.kurzbeschreibung == original



@given(instance=Entleihungsgegenstand_strategy)
def test_entleihungsgegenstand_titel_setter(instance):
    original = instance.titel
    instance.titel = original
    assert instance.titel == original

@given(instance=Zeitschrift_strategy)
@settings(max_examples=50)
def test_zeitschrift_instantiation(instance):
    assert isinstance(instance, Zeitschrift)



@given(instance=Zeitschrift_strategy)
def test_zeitschrift_Jahrgang_setter(instance):
    original = instance.Jahrgang
    instance.Jahrgang = original
    assert instance.Jahrgang == original



@given(instance=Zeitschrift_strategy)
def test_zeitschrift_Ausgabe_setter(instance):
    original = instance.Ausgabe
    instance.Ausgabe = original
    assert instance.Ausgabe == original

@given(instance=Videos_DVDS_strategy)
@settings(max_examples=50)
def test_videos_dvds_instantiation(instance):
    assert isinstance(instance, Videos_DVDS)



@given(instance=Videos_DVDS_strategy)
def test_videos_dvds_entLeihungsGeb_hr_setter(instance):
    original = instance.entLeihungsGeb_hr
    instance.entLeihungsGeb_hr = original
    assert instance.entLeihungsGeb_hr == original



@given(instance=Videos_DVDS_strategy)
def test_videos_dvds_AnzahlEntlehnungen_setter(instance):
    original = instance.AnzahlEntlehnungen
    instance.AnzahlEntlehnungen = original
    assert instance.AnzahlEntlehnungen == original



@given(instance=Videos_DVDS_strategy)
def test_videos_dvds_Regisseur_setter(instance):
    original = instance.Regisseur
    instance.Regisseur = original
    assert instance.Regisseur == original



@given(instance=Videos_DVDS_strategy)
def test_videos_dvds_Laufzeit_setter(instance):
    original = instance.Laufzeit
    instance.Laufzeit = original
    assert instance.Laufzeit == original

@given(instance=Buch_strategy)
@settings(max_examples=50)
def test_buch_instantiation(instance):
    assert isinstance(instance, Buch)



@given(instance=Buch_strategy)
def test_buch_ISBN_setter(instance):
    original = instance.ISBN
    instance.ISBN = original
    assert instance.ISBN == original



@given(instance=Buch_strategy)
def test_buch_Autor_setter(instance):
    original = instance.Autor
    instance.Autor = original
    assert instance.Autor == original
