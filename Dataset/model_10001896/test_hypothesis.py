import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    UseCase_UseCase,
    Actor_Actor,
    WIS_HiTierImport,
    WIS_WeideBemerkung,
    WIS_Tier,
    WIS_Herde,
    WIS_Weidegang,
    WIS_Weide,
    WIS_Weidefl_che,
    Weidegang2,
    Benutzer,
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



def test_wis_hitierimport_is_not_abstract():
    assert not inspect.isabstract(WIS_HiTierImport)


def test_wis_hitierimport_constructor_exists():
    assert callable(WIS_HiTierImport.__init__)


def test_wis_hitierimport_constructor_args():
    sig = inspect.signature(WIS_HiTierImport.__init__)
    params = list(sig.parameters.keys())
    assert "datum" in params, "Missing parameter 'datum'"

def test_wis_hitierimport_has_datum():
    assert hasattr(WIS_HiTierImport, "datum")
    descriptor = None
    for klass in WIS_HiTierImport.__mro__:
        if "datum" in klass.__dict__:
            descriptor = klass.__dict__["datum"]
            break
    assert isinstance(descriptor, property)



def test_wis_weidebemerkung_is_not_abstract():
    assert not inspect.isabstract(WIS_WeideBemerkung)


def test_wis_weidebemerkung_constructor_exists():
    assert callable(WIS_WeideBemerkung.__init__)


def test_wis_weidebemerkung_constructor_args():
    sig = inspect.signature(WIS_WeideBemerkung.__init__)
    params = list(sig.parameters.keys())
    assert "weideFACTCode" in params, "Missing parameter 'weideFACTCode'"
    assert "weideName" in params, "Missing parameter 'weideName'"
    assert "bemerkung" in params, "Missing parameter 'bemerkung'"
    assert "weideSchlagnummer" in params, "Missing parameter 'weideSchlagnummer'"
    assert "datum" in params, "Missing parameter 'datum'"

def test_wis_weidebemerkung_has_weideFACTCode():
    assert hasattr(WIS_WeideBemerkung, "weideFACTCode")
    descriptor = None
    for klass in WIS_WeideBemerkung.__mro__:
        if "weideFACTCode" in klass.__dict__:
            descriptor = klass.__dict__["weideFACTCode"]
            break
    assert isinstance(descriptor, property)

def test_wis_weidebemerkung_has_weideName():
    assert hasattr(WIS_WeideBemerkung, "weideName")
    descriptor = None
    for klass in WIS_WeideBemerkung.__mro__:
        if "weideName" in klass.__dict__:
            descriptor = klass.__dict__["weideName"]
            break
    assert isinstance(descriptor, property)

def test_wis_weidebemerkung_has_bemerkung():
    assert hasattr(WIS_WeideBemerkung, "bemerkung")
    descriptor = None
    for klass in WIS_WeideBemerkung.__mro__:
        if "bemerkung" in klass.__dict__:
            descriptor = klass.__dict__["bemerkung"]
            break
    assert isinstance(descriptor, property)

def test_wis_weidebemerkung_has_weideSchlagnummer():
    assert hasattr(WIS_WeideBemerkung, "weideSchlagnummer")
    descriptor = None
    for klass in WIS_WeideBemerkung.__mro__:
        if "weideSchlagnummer" in klass.__dict__:
            descriptor = klass.__dict__["weideSchlagnummer"]
            break
    assert isinstance(descriptor, property)

def test_wis_weidebemerkung_has_datum():
    assert hasattr(WIS_WeideBemerkung, "datum")
    descriptor = None
    for klass in WIS_WeideBemerkung.__mro__:
        if "datum" in klass.__dict__:
            descriptor = klass.__dict__["datum"]
            break
    assert isinstance(descriptor, property)



def test_wis_tier_is_not_abstract():
    assert not inspect.isabstract(WIS_Tier)


def test_wis_tier_constructor_exists():
    assert callable(WIS_Tier.__init__)


def test_wis_tier_constructor_args():
    sig = inspect.signature(WIS_Tier.__init__)
    params = list(sig.parameters.keys())
    assert "istAktiv" in params, "Missing parameter 'istAktiv'"
    assert "BTV4" in params, "Missing parameter 'BTV4'"
    assert "eigeneAngaben" in params, "Missing parameter 'eigeneAngaben'"
    assert "name" in params, "Missing parameter 'name'"
    assert "transponderNummer" in params, "Missing parameter 'transponderNummer'"
    assert "UDNummer" in params, "Missing parameter 'UDNummer'"
    assert "LOM" in params, "Missing parameter 'LOM'"
    assert "BTV8" in params, "Missing parameter 'BTV8'"
    assert "letzteKalbung" in params, "Missing parameter 'letzteKalbung'"
    assert "istWeiblich" in params, "Missing parameter 'istWeiblich'"
    assert "geburtsdatum" in params, "Missing parameter 'geburtsdatum'"

def test_wis_tier_has_istAktiv():
    assert hasattr(WIS_Tier, "istAktiv")
    descriptor = None
    for klass in WIS_Tier.__mro__:
        if "istAktiv" in klass.__dict__:
            descriptor = klass.__dict__["istAktiv"]
            break
    assert isinstance(descriptor, property)

def test_wis_tier_has_BTV4():
    assert hasattr(WIS_Tier, "BTV4")
    descriptor = None
    for klass in WIS_Tier.__mro__:
        if "BTV4" in klass.__dict__:
            descriptor = klass.__dict__["BTV4"]
            break
    assert isinstance(descriptor, property)

def test_wis_tier_has_eigeneAngaben():
    assert hasattr(WIS_Tier, "eigeneAngaben")
    descriptor = None
    for klass in WIS_Tier.__mro__:
        if "eigeneAngaben" in klass.__dict__:
            descriptor = klass.__dict__["eigeneAngaben"]
            break
    assert isinstance(descriptor, property)

def test_wis_tier_has_name():
    assert hasattr(WIS_Tier, "name")
    descriptor = None
    for klass in WIS_Tier.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_wis_tier_has_transponderNummer():
    assert hasattr(WIS_Tier, "transponderNummer")
    descriptor = None
    for klass in WIS_Tier.__mro__:
        if "transponderNummer" in klass.__dict__:
            descriptor = klass.__dict__["transponderNummer"]
            break
    assert isinstance(descriptor, property)

def test_wis_tier_has_UDNummer():
    assert hasattr(WIS_Tier, "UDNummer")
    descriptor = None
    for klass in WIS_Tier.__mro__:
        if "UDNummer" in klass.__dict__:
            descriptor = klass.__dict__["UDNummer"]
            break
    assert isinstance(descriptor, property)

def test_wis_tier_has_LOM():
    assert hasattr(WIS_Tier, "LOM")
    descriptor = None
    for klass in WIS_Tier.__mro__:
        if "LOM" in klass.__dict__:
            descriptor = klass.__dict__["LOM"]
            break
    assert isinstance(descriptor, property)

def test_wis_tier_has_BTV8():
    assert hasattr(WIS_Tier, "BTV8")
    descriptor = None
    for klass in WIS_Tier.__mro__:
        if "BTV8" in klass.__dict__:
            descriptor = klass.__dict__["BTV8"]
            break
    assert isinstance(descriptor, property)

def test_wis_tier_has_letzteKalbung():
    assert hasattr(WIS_Tier, "letzteKalbung")
    descriptor = None
    for klass in WIS_Tier.__mro__:
        if "letzteKalbung" in klass.__dict__:
            descriptor = klass.__dict__["letzteKalbung"]
            break
    assert isinstance(descriptor, property)

def test_wis_tier_has_istWeiblich():
    assert hasattr(WIS_Tier, "istWeiblich")
    descriptor = None
    for klass in WIS_Tier.__mro__:
        if "istWeiblich" in klass.__dict__:
            descriptor = klass.__dict__["istWeiblich"]
            break
    assert isinstance(descriptor, property)

def test_wis_tier_has_geburtsdatum():
    assert hasattr(WIS_Tier, "geburtsdatum")
    descriptor = None
    for klass in WIS_Tier.__mro__:
        if "geburtsdatum" in klass.__dict__:
            descriptor = klass.__dict__["geburtsdatum"]
            break
    assert isinstance(descriptor, property)



def test_wis_herde_is_not_abstract():
    assert not inspect.isabstract(WIS_Herde)


def test_wis_herde_constructor_exists():
    assert callable(WIS_Herde.__init__)


def test_wis_herde_constructor_args():
    sig = inspect.signature(WIS_Herde.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_wis_herde_has_name():
    assert hasattr(WIS_Herde, "name")
    descriptor = None
    for klass in WIS_Herde.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_wis_weidegang_is_not_abstract():
    assert not inspect.isabstract(WIS_Weidegang)


def test_wis_weidegang_constructor_exists():
    assert callable(WIS_Weidegang.__init__)


def test_wis_weidegang_constructor_args():
    sig = inspect.signature(WIS_Weidegang.__init__)
    params = list(sig.parameters.keys())
    assert "weideFACTCode" in params, "Missing parameter 'weideFACTCode'"
    assert "tierLOM" in params, "Missing parameter 'tierLOM'"
    assert "weideSchlagnummer" in params, "Missing parameter 'weideSchlagnummer'"
    assert "ausfallgrund" in params, "Missing parameter 'ausfallgrund'"
    assert "datum" in params, "Missing parameter 'datum'"
    assert "herdeName" in params, "Missing parameter 'herdeName'"
    assert "herdeFarbe" in params, "Missing parameter 'herdeFarbe'"
    assert "istAusgefallen" in params, "Missing parameter 'istAusgefallen'"
    assert "weideName" in params, "Missing parameter 'weideName'"
    assert "tierName" in params, "Missing parameter 'tierName'"

def test_wis_weidegang_has_weideFACTCode():
    assert hasattr(WIS_Weidegang, "weideFACTCode")
    descriptor = None
    for klass in WIS_Weidegang.__mro__:
        if "weideFACTCode" in klass.__dict__:
            descriptor = klass.__dict__["weideFACTCode"]
            break
    assert isinstance(descriptor, property)

def test_wis_weidegang_has_tierLOM():
    assert hasattr(WIS_Weidegang, "tierLOM")
    descriptor = None
    for klass in WIS_Weidegang.__mro__:
        if "tierLOM" in klass.__dict__:
            descriptor = klass.__dict__["tierLOM"]
            break
    assert isinstance(descriptor, property)

def test_wis_weidegang_has_weideSchlagnummer():
    assert hasattr(WIS_Weidegang, "weideSchlagnummer")
    descriptor = None
    for klass in WIS_Weidegang.__mro__:
        if "weideSchlagnummer" in klass.__dict__:
            descriptor = klass.__dict__["weideSchlagnummer"]
            break
    assert isinstance(descriptor, property)

def test_wis_weidegang_has_ausfallgrund():
    assert hasattr(WIS_Weidegang, "ausfallgrund")
    descriptor = None
    for klass in WIS_Weidegang.__mro__:
        if "ausfallgrund" in klass.__dict__:
            descriptor = klass.__dict__["ausfallgrund"]
            break
    assert isinstance(descriptor, property)

def test_wis_weidegang_has_datum():
    assert hasattr(WIS_Weidegang, "datum")
    descriptor = None
    for klass in WIS_Weidegang.__mro__:
        if "datum" in klass.__dict__:
            descriptor = klass.__dict__["datum"]
            break
    assert isinstance(descriptor, property)

def test_wis_weidegang_has_herdeName():
    assert hasattr(WIS_Weidegang, "herdeName")
    descriptor = None
    for klass in WIS_Weidegang.__mro__:
        if "herdeName" in klass.__dict__:
            descriptor = klass.__dict__["herdeName"]
            break
    assert isinstance(descriptor, property)

def test_wis_weidegang_has_herdeFarbe():
    assert hasattr(WIS_Weidegang, "herdeFarbe")
    descriptor = None
    for klass in WIS_Weidegang.__mro__:
        if "herdeFarbe" in klass.__dict__:
            descriptor = klass.__dict__["herdeFarbe"]
            break
    assert isinstance(descriptor, property)

def test_wis_weidegang_has_istAusgefallen():
    assert hasattr(WIS_Weidegang, "istAusgefallen")
    descriptor = None
    for klass in WIS_Weidegang.__mro__:
        if "istAusgefallen" in klass.__dict__:
            descriptor = klass.__dict__["istAusgefallen"]
            break
    assert isinstance(descriptor, property)

def test_wis_weidegang_has_weideName():
    assert hasattr(WIS_Weidegang, "weideName")
    descriptor = None
    for klass in WIS_Weidegang.__mro__:
        if "weideName" in klass.__dict__:
            descriptor = klass.__dict__["weideName"]
            break
    assert isinstance(descriptor, property)

def test_wis_weidegang_has_tierName():
    assert hasattr(WIS_Weidegang, "tierName")
    descriptor = None
    for klass in WIS_Weidegang.__mro__:
        if "tierName" in klass.__dict__:
            descriptor = klass.__dict__["tierName"]
            break
    assert isinstance(descriptor, property)



def test_wis_weide_is_not_abstract():
    assert not inspect.isabstract(WIS_Weide)


def test_wis_weide_constructor_exists():
    assert callable(WIS_Weide.__init__)


def test_wis_weide_constructor_args():
    sig = inspect.signature(WIS_Weide.__init__)
    params = list(sig.parameters.keys())
    assert "bemerkung" in params, "Missing parameter 'bemerkung'"
    assert "LPRVertrag" in params, "Missing parameter 'LPRVertrag'"
    assert "groesse" in params, "Missing parameter 'groesse'"
    assert "FACTCode" in params, "Missing parameter 'FACTCode'"
    assert "istAktiv" in params, "Missing parameter 'istAktiv'"
    assert "istBetriebsfremdeFlaeche" in params, "Missing parameter 'istBetriebsfremdeFlaeche'"
    assert "farbe" in params, "Missing parameter 'farbe'"
    assert "name" in params, "Missing parameter 'name'"
    assert "schlagnummer" in params, "Missing parameter 'schlagnummer'"

def test_wis_weide_has_bemerkung():
    assert hasattr(WIS_Weide, "bemerkung")
    descriptor = None
    for klass in WIS_Weide.__mro__:
        if "bemerkung" in klass.__dict__:
            descriptor = klass.__dict__["bemerkung"]
            break
    assert isinstance(descriptor, property)

def test_wis_weide_has_LPRVertrag():
    assert hasattr(WIS_Weide, "LPRVertrag")
    descriptor = None
    for klass in WIS_Weide.__mro__:
        if "LPRVertrag" in klass.__dict__:
            descriptor = klass.__dict__["LPRVertrag"]
            break
    assert isinstance(descriptor, property)

def test_wis_weide_has_groesse():
    assert hasattr(WIS_Weide, "groesse")
    descriptor = None
    for klass in WIS_Weide.__mro__:
        if "groesse" in klass.__dict__:
            descriptor = klass.__dict__["groesse"]
            break
    assert isinstance(descriptor, property)

def test_wis_weide_has_FACTCode():
    assert hasattr(WIS_Weide, "FACTCode")
    descriptor = None
    for klass in WIS_Weide.__mro__:
        if "FACTCode" in klass.__dict__:
            descriptor = klass.__dict__["FACTCode"]
            break
    assert isinstance(descriptor, property)

def test_wis_weide_has_istAktiv():
    assert hasattr(WIS_Weide, "istAktiv")
    descriptor = None
    for klass in WIS_Weide.__mro__:
        if "istAktiv" in klass.__dict__:
            descriptor = klass.__dict__["istAktiv"]
            break
    assert isinstance(descriptor, property)

def test_wis_weide_has_istBetriebsfremdeFlaeche():
    assert hasattr(WIS_Weide, "istBetriebsfremdeFlaeche")
    descriptor = None
    for klass in WIS_Weide.__mro__:
        if "istBetriebsfremdeFlaeche" in klass.__dict__:
            descriptor = klass.__dict__["istBetriebsfremdeFlaeche"]
            break
    assert isinstance(descriptor, property)

def test_wis_weide_has_farbe():
    assert hasattr(WIS_Weide, "farbe")
    descriptor = None
    for klass in WIS_Weide.__mro__:
        if "farbe" in klass.__dict__:
            descriptor = klass.__dict__["farbe"]
            break
    assert isinstance(descriptor, property)

def test_wis_weide_has_name():
    assert hasattr(WIS_Weide, "name")
    descriptor = None
    for klass in WIS_Weide.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_wis_weide_has_schlagnummer():
    assert hasattr(WIS_Weide, "schlagnummer")
    descriptor = None
    for klass in WIS_Weide.__mro__:
        if "schlagnummer" in klass.__dict__:
            descriptor = klass.__dict__["schlagnummer"]
            break
    assert isinstance(descriptor, property)



def test_wis_weidefl_che_is_not_abstract():
    assert not inspect.isabstract(WIS_Weidefl_che)


def test_wis_weidefl_che_constructor_exists():
    assert callable(WIS_Weidefl_che.__init__)


def test_wis_weidefl_che_constructor_args():
    sig = inspect.signature(WIS_Weidefl_che.__init__)
    params = list(sig.parameters.keys())
    assert "schlagnummer" in params, "Missing parameter 'schlagnummer'"
    assert "groesse" in params, "Missing parameter 'groesse'"
    assert "farbe" in params, "Missing parameter 'farbe'"
    assert "name" in params, "Missing parameter 'name'"

def test_wis_weidefl_che_has_schlagnummer():
    assert hasattr(WIS_Weidefl_che, "schlagnummer")
    descriptor = None
    for klass in WIS_Weidefl_che.__mro__:
        if "schlagnummer" in klass.__dict__:
            descriptor = klass.__dict__["schlagnummer"]
            break
    assert isinstance(descriptor, property)

def test_wis_weidefl_che_has_groesse():
    assert hasattr(WIS_Weidefl_che, "groesse")
    descriptor = None
    for klass in WIS_Weidefl_che.__mro__:
        if "groesse" in klass.__dict__:
            descriptor = klass.__dict__["groesse"]
            break
    assert isinstance(descriptor, property)

def test_wis_weidefl_che_has_farbe():
    assert hasattr(WIS_Weidefl_che, "farbe")
    descriptor = None
    for klass in WIS_Weidefl_che.__mro__:
        if "farbe" in klass.__dict__:
            descriptor = klass.__dict__["farbe"]
            break
    assert isinstance(descriptor, property)

def test_wis_weidefl_che_has_name():
    assert hasattr(WIS_Weidefl_che, "name")
    descriptor = None
    for klass in WIS_Weidefl_che.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_weidegang2_is_not_abstract():
    assert not inspect.isabstract(Weidegang2)


def test_weidegang2_constructor_exists():
    assert callable(Weidegang2.__init__)


def test_weidegang2_constructor_args():
    sig = inspect.signature(Weidegang2.__init__)
    params = list(sig.parameters.keys())
    assert "tierName" in params, "Missing parameter 'tierName'"
    assert "datum" in params, "Missing parameter 'datum'"
    assert "herdeFarbe" in params, "Missing parameter 'herdeFarbe'"
    assert "weideSchlagnummer" in params, "Missing parameter 'weideSchlagnummer'"
    assert "weideFACTCode" in params, "Missing parameter 'weideFACTCode'"
    assert "herdeName" in params, "Missing parameter 'herdeName'"
    assert "istAusgefallen" in params, "Missing parameter 'istAusgefallen'"
    assert "weideName" in params, "Missing parameter 'weideName'"
    assert "ausfallgrund" in params, "Missing parameter 'ausfallgrund'"

def test_weidegang2_has_tierName():
    assert hasattr(Weidegang2, "tierName")
    descriptor = None
    for klass in Weidegang2.__mro__:
        if "tierName" in klass.__dict__:
            descriptor = klass.__dict__["tierName"]
            break
    assert isinstance(descriptor, property)

def test_weidegang2_has_datum():
    assert hasattr(Weidegang2, "datum")
    descriptor = None
    for klass in Weidegang2.__mro__:
        if "datum" in klass.__dict__:
            descriptor = klass.__dict__["datum"]
            break
    assert isinstance(descriptor, property)

def test_weidegang2_has_herdeFarbe():
    assert hasattr(Weidegang2, "herdeFarbe")
    descriptor = None
    for klass in Weidegang2.__mro__:
        if "herdeFarbe" in klass.__dict__:
            descriptor = klass.__dict__["herdeFarbe"]
            break
    assert isinstance(descriptor, property)

def test_weidegang2_has_weideSchlagnummer():
    assert hasattr(Weidegang2, "weideSchlagnummer")
    descriptor = None
    for klass in Weidegang2.__mro__:
        if "weideSchlagnummer" in klass.__dict__:
            descriptor = klass.__dict__["weideSchlagnummer"]
            break
    assert isinstance(descriptor, property)

def test_weidegang2_has_weideFACTCode():
    assert hasattr(Weidegang2, "weideFACTCode")
    descriptor = None
    for klass in Weidegang2.__mro__:
        if "weideFACTCode" in klass.__dict__:
            descriptor = klass.__dict__["weideFACTCode"]
            break
    assert isinstance(descriptor, property)

def test_weidegang2_has_herdeName():
    assert hasattr(Weidegang2, "herdeName")
    descriptor = None
    for klass in Weidegang2.__mro__:
        if "herdeName" in klass.__dict__:
            descriptor = klass.__dict__["herdeName"]
            break
    assert isinstance(descriptor, property)

def test_weidegang2_has_istAusgefallen():
    assert hasattr(Weidegang2, "istAusgefallen")
    descriptor = None
    for klass in Weidegang2.__mro__:
        if "istAusgefallen" in klass.__dict__:
            descriptor = klass.__dict__["istAusgefallen"]
            break
    assert isinstance(descriptor, property)

def test_weidegang2_has_weideName():
    assert hasattr(Weidegang2, "weideName")
    descriptor = None
    for klass in Weidegang2.__mro__:
        if "weideName" in klass.__dict__:
            descriptor = klass.__dict__["weideName"]
            break
    assert isinstance(descriptor, property)

def test_weidegang2_has_ausfallgrund():
    assert hasattr(Weidegang2, "ausfallgrund")
    descriptor = None
    for klass in Weidegang2.__mro__:
        if "ausfallgrund" in klass.__dict__:
            descriptor = klass.__dict__["ausfallgrund"]
            break
    assert isinstance(descriptor, property)



def test_benutzer_is_not_abstract():
    assert not inspect.isabstract(Benutzer)


def test_benutzer_constructor_exists():
    assert callable(Benutzer.__init__)


def test_benutzer_constructor_args():
    sig = inspect.signature(Benutzer.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "passwortHash" in params, "Missing parameter 'passwortHash'"

def test_benutzer_has_name():
    assert hasattr(Benutzer, "name")
    descriptor = None
    for klass in Benutzer.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_benutzer_has_passwortHash():
    assert hasattr(Benutzer, "passwortHash")
    descriptor = None
    for klass in Benutzer.__mro__:
        if "passwortHash" in klass.__dict__:
            descriptor = klass.__dict__["passwortHash"]
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
WIS_HiTierImport_strategy = st.builds(
    WIS_HiTierImport,
    datum=
        safe_text
)
WIS_WeideBemerkung_strategy = st.builds(
    WIS_WeideBemerkung,
    weideFACTCode=
        safe_text,
    weideName=
        safe_text,
    bemerkung=
        safe_text,
    weideSchlagnummer=
        safe_text,
    datum=
        safe_text
)
WIS_Tier_strategy = st.builds(
    WIS_Tier,
    istAktiv=
        st.booleans(),
    BTV4=
        safe_text,
    eigeneAngaben=
        safe_text,
    name=
        safe_text,
    transponderNummer=
        safe_text,
    UDNummer=
        safe_text,
    LOM=
        st.integers(),
    BTV8=
        safe_text,
    letzteKalbung=
        safe_text,
    istWeiblich=
        st.booleans(),
    geburtsdatum=
        safe_text
)
WIS_Herde_strategy = st.builds(
    WIS_Herde,
    name=
        safe_text
)
WIS_Weidegang_strategy = st.builds(
    WIS_Weidegang,
    weideFACTCode=
        safe_text,
    tierLOM=
        safe_text,
    weideSchlagnummer=
        safe_text,
    ausfallgrund=
        safe_text,
    datum=
        safe_text,
    herdeName=
        safe_text,
    herdeFarbe=
        safe_text,
    istAusgefallen=
        st.booleans(),
    weideName=
        safe_text,
    tierName=
        safe_text
)
WIS_Weide_strategy = st.builds(
    WIS_Weide,
    bemerkung=
        safe_text,
    LPRVertrag=
        safe_text,
    groesse=
        st.integers(),
    FACTCode=
        st.integers(),
    istAktiv=
        st.booleans(),
    istBetriebsfremdeFlaeche=
        st.booleans(),
    farbe=
        safe_text,
    name=
        safe_text,
    schlagnummer=
        st.integers()
)
WIS_Weidefl_che_strategy = st.builds(
    WIS_Weidefl_che,
    schlagnummer=
        safe_text,
    groesse=
        st.integers(),
    farbe=
        safe_text,
    name=
        safe_text
)
Weidegang2_strategy = st.builds(
    Weidegang2,
    tierName=
        safe_text,
    datum=
        safe_text,
    herdeFarbe=
        safe_text,
    weideSchlagnummer=
        safe_text,
    weideFACTCode=
        safe_text,
    herdeName=
        safe_text,
    istAusgefallen=
        st.booleans(),
    weideName=
        safe_text,
    ausfallgrund=
        safe_text
)
Benutzer_strategy = st.builds(
    Benutzer,
    name=
        safe_text,
    passwortHash=
        safe_text
)

@given(instance=UseCase_UseCase_strategy)
@settings(max_examples=50)
def test_usecase_usecase_instantiation(instance):
    assert isinstance(instance, UseCase_UseCase)

@given(instance=Actor_Actor_strategy)
@settings(max_examples=50)
def test_actor_actor_instantiation(instance):
    assert isinstance(instance, Actor_Actor)

@given(instance=WIS_HiTierImport_strategy)
@settings(max_examples=50)
def test_wis_hitierimport_instantiation(instance):
    assert isinstance(instance, WIS_HiTierImport)



@given(instance=WIS_HiTierImport_strategy)
def test_wis_hitierimport_datum_setter(instance):
    original = instance.datum
    instance.datum = original
    assert instance.datum == original

@given(instance=WIS_WeideBemerkung_strategy)
@settings(max_examples=50)
def test_wis_weidebemerkung_instantiation(instance):
    assert isinstance(instance, WIS_WeideBemerkung)



@given(instance=WIS_WeideBemerkung_strategy)
def test_wis_weidebemerkung_weideFACTCode_setter(instance):
    original = instance.weideFACTCode
    instance.weideFACTCode = original
    assert instance.weideFACTCode == original



@given(instance=WIS_WeideBemerkung_strategy)
def test_wis_weidebemerkung_weideName_setter(instance):
    original = instance.weideName
    instance.weideName = original
    assert instance.weideName == original



@given(instance=WIS_WeideBemerkung_strategy)
def test_wis_weidebemerkung_bemerkung_setter(instance):
    original = instance.bemerkung
    instance.bemerkung = original
    assert instance.bemerkung == original



@given(instance=WIS_WeideBemerkung_strategy)
def test_wis_weidebemerkung_weideSchlagnummer_setter(instance):
    original = instance.weideSchlagnummer
    instance.weideSchlagnummer = original
    assert instance.weideSchlagnummer == original



@given(instance=WIS_WeideBemerkung_strategy)
def test_wis_weidebemerkung_datum_setter(instance):
    original = instance.datum
    instance.datum = original
    assert instance.datum == original

@given(instance=WIS_Tier_strategy)
@settings(max_examples=50)
def test_wis_tier_instantiation(instance):
    assert isinstance(instance, WIS_Tier)



@given(instance=WIS_Tier_strategy)
def test_wis_tier_istAktiv_setter(instance):
    original = instance.istAktiv
    instance.istAktiv = original
    assert instance.istAktiv == original



@given(instance=WIS_Tier_strategy)
def test_wis_tier_BTV4_setter(instance):
    original = instance.BTV4
    instance.BTV4 = original
    assert instance.BTV4 == original



@given(instance=WIS_Tier_strategy)
def test_wis_tier_eigeneAngaben_setter(instance):
    original = instance.eigeneAngaben
    instance.eigeneAngaben = original
    assert instance.eigeneAngaben == original



@given(instance=WIS_Tier_strategy)
def test_wis_tier_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=WIS_Tier_strategy)
def test_wis_tier_transponderNummer_setter(instance):
    original = instance.transponderNummer
    instance.transponderNummer = original
    assert instance.transponderNummer == original



@given(instance=WIS_Tier_strategy)
def test_wis_tier_UDNummer_setter(instance):
    original = instance.UDNummer
    instance.UDNummer = original
    assert instance.UDNummer == original



@given(instance=WIS_Tier_strategy)
def test_wis_tier_LOM_setter(instance):
    original = instance.LOM
    instance.LOM = original
    assert instance.LOM == original



@given(instance=WIS_Tier_strategy)
def test_wis_tier_BTV8_setter(instance):
    original = instance.BTV8
    instance.BTV8 = original
    assert instance.BTV8 == original



@given(instance=WIS_Tier_strategy)
def test_wis_tier_letzteKalbung_setter(instance):
    original = instance.letzteKalbung
    instance.letzteKalbung = original
    assert instance.letzteKalbung == original



@given(instance=WIS_Tier_strategy)
def test_wis_tier_istWeiblich_setter(instance):
    original = instance.istWeiblich
    instance.istWeiblich = original
    assert instance.istWeiblich == original



@given(instance=WIS_Tier_strategy)
def test_wis_tier_geburtsdatum_setter(instance):
    original = instance.geburtsdatum
    instance.geburtsdatum = original
    assert instance.geburtsdatum == original

@given(instance=WIS_Herde_strategy)
@settings(max_examples=50)
def test_wis_herde_instantiation(instance):
    assert isinstance(instance, WIS_Herde)



@given(instance=WIS_Herde_strategy)
def test_wis_herde_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=WIS_Weidegang_strategy)
@settings(max_examples=50)
def test_wis_weidegang_instantiation(instance):
    assert isinstance(instance, WIS_Weidegang)



@given(instance=WIS_Weidegang_strategy)
def test_wis_weidegang_weideFACTCode_setter(instance):
    original = instance.weideFACTCode
    instance.weideFACTCode = original
    assert instance.weideFACTCode == original



@given(instance=WIS_Weidegang_strategy)
def test_wis_weidegang_tierLOM_setter(instance):
    original = instance.tierLOM
    instance.tierLOM = original
    assert instance.tierLOM == original



@given(instance=WIS_Weidegang_strategy)
def test_wis_weidegang_weideSchlagnummer_setter(instance):
    original = instance.weideSchlagnummer
    instance.weideSchlagnummer = original
    assert instance.weideSchlagnummer == original



@given(instance=WIS_Weidegang_strategy)
def test_wis_weidegang_ausfallgrund_setter(instance):
    original = instance.ausfallgrund
    instance.ausfallgrund = original
    assert instance.ausfallgrund == original



@given(instance=WIS_Weidegang_strategy)
def test_wis_weidegang_datum_setter(instance):
    original = instance.datum
    instance.datum = original
    assert instance.datum == original



@given(instance=WIS_Weidegang_strategy)
def test_wis_weidegang_herdeName_setter(instance):
    original = instance.herdeName
    instance.herdeName = original
    assert instance.herdeName == original



@given(instance=WIS_Weidegang_strategy)
def test_wis_weidegang_herdeFarbe_setter(instance):
    original = instance.herdeFarbe
    instance.herdeFarbe = original
    assert instance.herdeFarbe == original



@given(instance=WIS_Weidegang_strategy)
def test_wis_weidegang_istAusgefallen_setter(instance):
    original = instance.istAusgefallen
    instance.istAusgefallen = original
    assert instance.istAusgefallen == original



@given(instance=WIS_Weidegang_strategy)
def test_wis_weidegang_weideName_setter(instance):
    original = instance.weideName
    instance.weideName = original
    assert instance.weideName == original



@given(instance=WIS_Weidegang_strategy)
def test_wis_weidegang_tierName_setter(instance):
    original = instance.tierName
    instance.tierName = original
    assert instance.tierName == original

@given(instance=WIS_Weide_strategy)
@settings(max_examples=50)
def test_wis_weide_instantiation(instance):
    assert isinstance(instance, WIS_Weide)



@given(instance=WIS_Weide_strategy)
def test_wis_weide_bemerkung_setter(instance):
    original = instance.bemerkung
    instance.bemerkung = original
    assert instance.bemerkung == original



@given(instance=WIS_Weide_strategy)
def test_wis_weide_LPRVertrag_setter(instance):
    original = instance.LPRVertrag
    instance.LPRVertrag = original
    assert instance.LPRVertrag == original



@given(instance=WIS_Weide_strategy)
def test_wis_weide_groesse_setter(instance):
    original = instance.groesse
    instance.groesse = original
    assert instance.groesse == original



@given(instance=WIS_Weide_strategy)
def test_wis_weide_FACTCode_setter(instance):
    original = instance.FACTCode
    instance.FACTCode = original
    assert instance.FACTCode == original



@given(instance=WIS_Weide_strategy)
def test_wis_weide_istAktiv_setter(instance):
    original = instance.istAktiv
    instance.istAktiv = original
    assert instance.istAktiv == original



@given(instance=WIS_Weide_strategy)
def test_wis_weide_istBetriebsfremdeFlaeche_setter(instance):
    original = instance.istBetriebsfremdeFlaeche
    instance.istBetriebsfremdeFlaeche = original
    assert instance.istBetriebsfremdeFlaeche == original



@given(instance=WIS_Weide_strategy)
def test_wis_weide_farbe_setter(instance):
    original = instance.farbe
    instance.farbe = original
    assert instance.farbe == original



@given(instance=WIS_Weide_strategy)
def test_wis_weide_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=WIS_Weide_strategy)
def test_wis_weide_schlagnummer_setter(instance):
    original = instance.schlagnummer
    instance.schlagnummer = original
    assert instance.schlagnummer == original

@given(instance=WIS_Weidefl_che_strategy)
@settings(max_examples=50)
def test_wis_weidefl_che_instantiation(instance):
    assert isinstance(instance, WIS_Weidefl_che)



@given(instance=WIS_Weidefl_che_strategy)
def test_wis_weidefl_che_schlagnummer_setter(instance):
    original = instance.schlagnummer
    instance.schlagnummer = original
    assert instance.schlagnummer == original



@given(instance=WIS_Weidefl_che_strategy)
def test_wis_weidefl_che_groesse_setter(instance):
    original = instance.groesse
    instance.groesse = original
    assert instance.groesse == original



@given(instance=WIS_Weidefl_che_strategy)
def test_wis_weidefl_che_farbe_setter(instance):
    original = instance.farbe
    instance.farbe = original
    assert instance.farbe == original



@given(instance=WIS_Weidefl_che_strategy)
def test_wis_weidefl_che_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Weidegang2_strategy)
@settings(max_examples=50)
def test_weidegang2_instantiation(instance):
    assert isinstance(instance, Weidegang2)



@given(instance=Weidegang2_strategy)
def test_weidegang2_tierName_setter(instance):
    original = instance.tierName
    instance.tierName = original
    assert instance.tierName == original



@given(instance=Weidegang2_strategy)
def test_weidegang2_datum_setter(instance):
    original = instance.datum
    instance.datum = original
    assert instance.datum == original



@given(instance=Weidegang2_strategy)
def test_weidegang2_herdeFarbe_setter(instance):
    original = instance.herdeFarbe
    instance.herdeFarbe = original
    assert instance.herdeFarbe == original



@given(instance=Weidegang2_strategy)
def test_weidegang2_weideSchlagnummer_setter(instance):
    original = instance.weideSchlagnummer
    instance.weideSchlagnummer = original
    assert instance.weideSchlagnummer == original



@given(instance=Weidegang2_strategy)
def test_weidegang2_weideFACTCode_setter(instance):
    original = instance.weideFACTCode
    instance.weideFACTCode = original
    assert instance.weideFACTCode == original



@given(instance=Weidegang2_strategy)
def test_weidegang2_herdeName_setter(instance):
    original = instance.herdeName
    instance.herdeName = original
    assert instance.herdeName == original



@given(instance=Weidegang2_strategy)
def test_weidegang2_istAusgefallen_setter(instance):
    original = instance.istAusgefallen
    instance.istAusgefallen = original
    assert instance.istAusgefallen == original



@given(instance=Weidegang2_strategy)
def test_weidegang2_weideName_setter(instance):
    original = instance.weideName
    instance.weideName = original
    assert instance.weideName == original



@given(instance=Weidegang2_strategy)
def test_weidegang2_ausfallgrund_setter(instance):
    original = instance.ausfallgrund
    instance.ausfallgrund = original
    assert instance.ausfallgrund == original

@given(instance=Benutzer_strategy)
@settings(max_examples=50)
def test_benutzer_instantiation(instance):
    assert isinstance(instance, Benutzer)



@given(instance=Benutzer_strategy)
def test_benutzer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Benutzer_strategy)
def test_benutzer_passwortHash_setter(instance):
    original = instance.passwortHash
    instance.passwortHash = original
    assert instance.passwortHash == original
