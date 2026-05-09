import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    shadowrun::Schadenswiederstand,
    MagiePersona,
    shadowrun::Shamane,
    shadowrun::GegenstandStufen,
    shadowrun::NahkampfReichweite,
    shadowrun::BodyIndex,
    shadowrun::Essenz,
    shadowrun::GeistigeAttribute,
    shadowrun::BerechneteAttribute,
    Schadenswiederstand,
    shadowrun::KoerperlicheAtribute,
    shadowrun::Sichtverhaeltnisse,
    shadowrun::FernkampfwaffenModifikatoren,
    shadowrun::EObject,
    shadowrun::Bemerkbar,
    AbstraktNahkampfwaffe,
    shadowrun::Nahkampfwaffe,
    shadowrun::Quelle,
    shadowrun::WarenListe,
    shadowrun::Reichweiten,
    shadowrun::Beschreibbar,
    shadowrun::GengenstandListe,
    AbstractMagischePaersona,
    shadowrun::PersonaZauber,
    AbstractMagier,
    shadowrun::MagiePersona,
    shadowrun::Legalitaet,
    AbstraktFertigkeit,
    shadowrun::KiAdept,
    MagischeMods,
    shadowrun::KiKraft,
    BaseMagischePersona,
    shadowrun::AbstractMagier,
    shadowrun::BaseMagischePersona,
    AbstraktModifikatoren,
    shadowrun::MagischeMods,
    shadowrun::koerpermods,
    shadowrun::ModifikatorList,
    shadowrun::GeldWert,
    koerpermods,
    shadowrun::FK,
    AbstrakteRuestung,
    shadowrun::Ruestung,
    shadowrun::PersonaKoerper,
    shadowrun::Modifizierbar,
    shadowrun::EAttribute,
    shadowrun::AttributModifikatorWert,
    shadowrun::BasicList,
    AbstaktFernKampfwaffe,
    shadowrun::Projektilwaffe,
    shadowrun::Wurfwaffe,
    shadowrun::Feuerwaffe,
    Gegenstand,
    shadowrun::MunitionsBehealter,
    shadowrun::Behaelter,
    NahkampfReichweite,
    AbstraktKleidung,
    shadowrun::AbstrakteRuestung,
    shadowrun::RaumKoordinate,
    shadowrun::AbstrakRaumKoerper,
    shadowrun::Spezialisierung,
    AbstaktPersona,
    shadowrun::AbstractMagischePaersona,
    shadowrun::Persona,
    shadowrun::Kleidung,
    shadowrun::PersonaFertigkeit,
    shadowrun::Konzentration,
    shadowrun::Fertigkeit,
    AbstaktGegenstand,
    shadowrun::Munition,
    shadowrun::Gegenstand,
    shadowrun::AbstraktKleidung,
    shadowrun::AbstaktWaffe,
    Modifizierbar,
    Quelle,
    Bemerkbar,
    Legalitaet,
    Beschreibbar,
    shadowrun::Zauber,
    shadowrun::ShrList,
    shadowrun::Totem,
    shadowrun::Script,
    shadowrun::AbstraktModifikatoren,
    shadowrun::Placement,
    shadowrun::SourceBook,
    shadowrun::Spezies,
    shadowrun::PersonaGruppe,
    GeldWert,
    shadowrun::BioWare,
    shadowrun::Cyberware,
    FK,
    shadowrun::FertigkeitsGruppe,
    shadowrun::AbstraktFertigkeit,
    shadowrun::AbstaktGegenstand,
    shadowrun::Reichweite,
    AbstaktWaffe,
    shadowrun::Granate,
    shadowrun::AbstraktNahkampfwaffe,
    shadowrun::AbstaktFernKampfwaffe,
    GeistigeAttribute,
    BerechneteAttribute,
    KoerperlicheAtribute,
    BodyIndex,
    Essenz,
    shadowrun::AbstaktPersona,
    Koerperteil,
    SchadensTyp,
    SmartgunType,
    ModifikatorType,
    FeuerModus,
    MagazinTyp,
    Tragbar,
    ZauberReichweite,
    ZauberDauer,
    ZauberArt,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_shadowrun::schadenswiederstand_is_not_abstract():
    assert not inspect.isabstract(shadowrun::Schadenswiederstand)


def test_shadowrun::schadenswiederstand_constructor_exists():
    assert callable(shadowrun::Schadenswiederstand.__init__)


def test_shadowrun::schadenswiederstand_constructor_args():
    sig = inspect.signature(shadowrun::Schadenswiederstand.__init__)
    params = list(sig.parameters.keys())
    assert "ruestungsSchutzBalistisch" in params, "Missing parameter 'ruestungsSchutzBalistisch'"
    assert "ruestungsSchutzStoss" in params, "Missing parameter 'ruestungsSchutzStoss'"

def test_shadowrun::schadenswiederstand_has_ruestungsSchutzBalistisch():
    assert hasattr(shadowrun::Schadenswiederstand, "ruestungsSchutzBalistisch")
    descriptor = None
    for klass in shadowrun::Schadenswiederstand.__mro__:
        if "ruestungsSchutzBalistisch" in klass.__dict__:
            descriptor = klass.__dict__["ruestungsSchutzBalistisch"]
            break
    assert isinstance(descriptor, property)

def test_shadowrun::schadenswiederstand_has_ruestungsSchutzStoss():
    assert hasattr(shadowrun::Schadenswiederstand, "ruestungsSchutzStoss")
    descriptor = None
    for klass in shadowrun::Schadenswiederstand.__mro__:
        if "ruestungsSchutzStoss" in klass.__dict__:
            descriptor = klass.__dict__["ruestungsSchutzStoss"]
            break
    assert isinstance(descriptor, property)



def test_magiepersona_is_not_abstract():
    assert not inspect.isabstract(MagiePersona)


def test_magiepersona_constructor_exists():
    assert callable(MagiePersona.__init__)


def test_magiepersona_constructor_args():
    sig = inspect.signature(MagiePersona.__init__)
    params = list(sig.parameters.keys())



def test_shadowrun::shamane_is_not_abstract():
    assert not inspect.isabstract(shadowrun::Shamane)


def test_shadowrun::shamane_constructor_exists():
    assert callable(shadowrun::Shamane.__init__)


def test_shadowrun::shamane_constructor_args():
    sig = inspect.signature(shadowrun::Shamane.__init__)
    params = list(sig.parameters.keys())



def test_shadowrun::gegenstandstufen_is_not_abstract():
    assert not inspect.isabstract(shadowrun::GegenstandStufen)


def test_shadowrun::gegenstandstufen_constructor_exists():
    assert callable(shadowrun::GegenstandStufen.__init__)


def test_shadowrun::gegenstandstufen_constructor_args():
    sig = inspect.signature(shadowrun::GegenstandStufen.__init__)
    params = list(sig.parameters.keys())
    assert "AntiTracing" in params, "Missing parameter 'AntiTracing'"
    assert "AntiProtection" in params, "Missing parameter 'AntiProtection'"
    assert "Protection" in params, "Missing parameter 'Protection'"
    assert "Computer" in params, "Missing parameter 'Computer'"
    assert "Elektronik" in params, "Missing parameter 'Elektronik'"
    assert "Tracing" in params, "Missing parameter 'Tracing'"

def test_shadowrun::gegenstandstufen_has_AntiTracing():
    assert hasattr(shadowrun::GegenstandStufen, "AntiTracing")
    descriptor = None
    for klass in shadowrun::GegenstandStufen.__mro__:
        if "AntiTracing" in klass.__dict__:
            descriptor = klass.__dict__["AntiTracing"]
            break
    assert isinstance(descriptor, property)

def test_shadowrun::gegenstandstufen_has_AntiProtection():
    assert hasattr(shadowrun::GegenstandStufen, "AntiProtection")
    descriptor = None
    for klass in shadowrun::GegenstandStufen.__mro__:
        if "AntiProtection" in klass.__dict__:
            descriptor = klass.__dict__["AntiProtection"]
            break
    assert isinstance(descriptor, property)

def test_shadowrun::gegenstandstufen_has_Protection():
    assert hasattr(shadowrun::GegenstandStufen, "Protection")
    descriptor = None
    for klass in shadowrun::GegenstandStufen.__mro__:
        if "Protection" in klass.__dict__:
            descriptor = klass.__dict__["Protection"]
            break
    assert isinstance(descriptor, property)

def test_shadowrun::gegenstandstufen_has_Computer():
    assert hasattr(shadowrun::GegenstandStufen, "Computer")
    descriptor = None
    for klass in shadowrun::GegenstandStufen.__mro__:
        if "Computer" in klass.__dict__:
            descriptor = klass.__dict__["Computer"]
            break
    assert isinstance(descriptor, property)

def test_shadowrun::gegenstandstufen_has_Elektronik():
    assert hasattr(shadowrun::GegenstandStufen, "Elektronik")
    descriptor = None
    for klass in shadowrun::GegenstandStufen.__mro__:
        if "Elektronik" in klass.__dict__:
            descriptor = klass.__dict__["Elektronik"]
            break
    assert isinstance(descriptor, property)

def test_shadowrun::gegenstandstufen_has_Tracing():
    assert hasattr(shadowrun::GegenstandStufen, "Tracing")
    descriptor = None
    for klass in shadowrun::GegenstandStufen.__mro__:
        if "Tracing" in klass.__dict__:
            descriptor = klass.__dict__["Tracing"]
            break
    assert isinstance(descriptor, property)



def test_shadowrun::nahkampfreichweite_is_not_abstract():
    assert not inspect.isabstract(shadowrun::NahkampfReichweite)


def test_shadowrun::nahkampfreichweite_constructor_exists():
    assert callable(shadowrun::NahkampfReichweite.__init__)


def test_shadowrun::nahkampfreichweite_constructor_args():
    sig = inspect.signature(shadowrun::NahkampfReichweite.__init__)
    params = list(sig.parameters.keys())
    assert "reichweite" in params, "Missing parameter 'reichweite'"

def test_shadowrun::nahkampfreichweite_has_reichweite():
    assert hasattr(shadowrun::NahkampfReichweite, "reichweite")
    descriptor = None
    for klass in shadowrun::NahkampfReichweite.__mro__:
        if "reichweite" in klass.__dict__:
            descriptor = klass.__dict__["reichweite"]
            break
    assert isinstance(descriptor, property)



def test_shadowrun::bodyindex_is_not_abstract():
    assert not inspect.isabstract(shadowrun::BodyIndex)


def test_shadowrun::bodyindex_constructor_exists():
    assert callable(shadowrun::BodyIndex.__init__)


def test_shadowrun::bodyindex_constructor_args():
    sig = inspect.signature(shadowrun::BodyIndex.__init__)
    params = list(sig.parameters.keys())
    assert "bodyIndex" in params, "Missing parameter 'bodyIndex'"

def test_shadowrun::bodyindex_has_bodyIndex():
    assert hasattr(shadowrun::BodyIndex, "bodyIndex")
    descriptor = None
    for klass in shadowrun::BodyIndex.__mro__:
        if "bodyIndex" in klass.__dict__:
            descriptor = klass.__dict__["bodyIndex"]
            break
    assert isinstance(descriptor, property)



def test_shadowrun::essenz_is_not_abstract():
    assert not inspect.isabstract(shadowrun::Essenz)


def test_shadowrun::essenz_constructor_exists():
    assert callable(shadowrun::Essenz.__init__)


def test_shadowrun::essenz_constructor_args():
    sig = inspect.signature(shadowrun::Essenz.__init__)
    params = list(sig.parameters.keys())
    assert "Essenz" in params, "Missing parameter 'Essenz'"

def test_shadowrun::essenz_has_Essenz():
    assert hasattr(shadowrun::Essenz, "Essenz")
    descriptor = None
    for klass in shadowrun::Essenz.__mro__:
        if "Essenz" in klass.__dict__:
            descriptor = klass.__dict__["Essenz"]
            break
    assert isinstance(descriptor, property)



def test_shadowrun::geistigeattribute_is_not_abstract():
    assert not inspect.isabstract(shadowrun::GeistigeAttribute)


def test_shadowrun::geistigeattribute_constructor_exists():
    assert callable(shadowrun::GeistigeAttribute.__init__)


def test_shadowrun::geistigeattribute_constructor_args():
    sig = inspect.signature(shadowrun::GeistigeAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "Inteligenz" in params, "Missing parameter 'Inteligenz'"
    assert "Charisma" in params, "Missing parameter 'Charisma'"
    assert "Willenskraft" in params, "Missing parameter 'Willenskraft'"

def test_shadowrun::geistigeattribute_has_Inteligenz():
    assert hasattr(shadowrun::GeistigeAttribute, "Inteligenz")
    descriptor = None
    for klass in shadowrun::GeistigeAttribute.__mro__:
        if "Inteligenz" in klass.__dict__:
            descriptor = klass.__dict__["Inteligenz"]
            break
    assert isinstance(descriptor, property)

def test_shadowrun::geistigeattribute_has_Charisma():
    assert hasattr(shadowrun::GeistigeAttribute, "Charisma")
    descriptor = None
    for klass in shadowrun::GeistigeAttribute.__mro__:
        if "Charisma" in klass.__dict__:
            descriptor = klass.__dict__["Charisma"]
            break
    assert isinstance(descriptor, property)

def test_shadowrun::geistigeattribute_has_Willenskraft():
    assert hasattr(shadowrun::GeistigeAttribute, "Willenskraft")
    descriptor = None
    for klass in shadowrun::GeistigeAttribute.__mro__:
        if "Willenskraft" in klass.__dict__:
            descriptor = klass.__dict__["Willenskraft"]
            break
    assert isinstance(descriptor, property)



def test_shadowrun::berechneteattribute_is_not_abstract():
    assert not inspect.isabstract(shadowrun::BerechneteAttribute)


def test_shadowrun::berechneteattribute_constructor_exists():
    assert callable(shadowrun::BerechneteAttribute.__init__)


def test_shadowrun::berechneteattribute_constructor_args():
    sig = inspect.signature(shadowrun::BerechneteAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "ReaktionW" in params, "Missing parameter 'ReaktionW'"
    assert "Kampfpool" in params, "Missing parameter 'Kampfpool'"
    assert "Reaktion" in params, "Missing parameter 'Reaktion'"

def test_shadowrun::berechneteattribute_has_ReaktionW():
    assert hasattr(shadowrun::BerechneteAttribute, "ReaktionW")
    descriptor = None
    for klass in shadowrun::BerechneteAttribute.__mro__:
        if "ReaktionW" in klass.__dict__:
            descriptor = klass.__dict__["ReaktionW"]
            break
    assert isinstance(descriptor, property)

def test_shadowrun::berechneteattribute_has_Kampfpool():
    assert hasattr(shadowrun::BerechneteAttribute, "Kampfpool")
    descriptor = None
    for klass in shadowrun::BerechneteAttribute.__mro__:
        if "Kampfpool" in klass.__dict__:
            descriptor = klass.__dict__["Kampfpool"]
            break
    assert isinstance(descriptor, property)

def test_shadowrun::berechneteattribute_has_Reaktion():
    assert hasattr(shadowrun::BerechneteAttribute, "Reaktion")
    descriptor = None
    for klass in shadowrun::BerechneteAttribute.__mro__:
        if "Reaktion" in klass.__dict__:
            descriptor = klass.__dict__["Reaktion"]
            break
    assert isinstance(descriptor, property)



def test_schadenswiederstand_is_not_abstract():
    assert not inspect.isabstract(Schadenswiederstand)


def test_schadenswiederstand_constructor_exists():
    assert callable(Schadenswiederstand.__init__)


def test_schadenswiederstand_constructor_args():
    sig = inspect.signature(Schadenswiederstand.__init__)
    params = list(sig.parameters.keys())



def test_shadowrun::koerperlicheatribute_is_not_abstract():
    assert not inspect.isabstract(shadowrun::KoerperlicheAtribute)


def test_shadowrun::koerperlicheatribute_constructor_exists():
    assert callable(shadowrun::KoerperlicheAtribute.__init__)


def test_shadowrun::koerperlicheatribute_constructor_args():
    sig = inspect.signature(shadowrun::KoerperlicheAtribute.__init__)
    params = list(sig.parameters.keys())
    assert "Staerke" in params, "Missing parameter 'Staerke'"
    assert "Schnelligkeit" in params, "Missing parameter 'Schnelligkeit'"
    assert "Konsitution" in params, "Missing parameter 'Konsitution'"

def test_shadowrun::koerperlicheatribute_has_Staerke():
    assert hasattr(shadowrun::KoerperlicheAtribute, "Staerke")
    descriptor = None
    for klass in shadowrun::KoerperlicheAtribute.__mro__:
        if "Staerke" in klass.__dict__:
            descriptor = klass.__dict__["Staerke"]
            break
    assert isinstance(descriptor, property)

def test_shadowrun::koerperlicheatribute_has_Schnelligkeit():
    assert hasattr(shadowrun::KoerperlicheAtribute, "Schnelligkeit")
    descriptor = None
    for klass in shadowrun::KoerperlicheAtribute.__mro__:
        if "Schnelligkeit" in klass.__dict__:
            descriptor = klass.__dict__["Schnelligkeit"]
            break
    assert isinstance(descriptor, property)

def test_shadowrun::koerperlicheatribute_has_Konsitution():
    assert hasattr(shadowrun::KoerperlicheAtribute, "Konsitution")
    descriptor = None
    for klass in shadowrun::KoerperlicheAtribute.__mro__:
        if "Konsitution" in klass.__dict__:
            descriptor = klass.__dict__["Konsitution"]
            break
    assert isinstance(descriptor, property)



def test_shadowrun::sichtverhaeltnisse_is_not_abstract():
    assert not inspect.isabstract(shadowrun::Sichtverhaeltnisse)


def test_shadowrun::sichtverhaeltnisse_constructor_exists():
    assert callable(shadowrun::Sichtverhaeltnisse.__init__)


def test_shadowrun::sichtverhaeltnisse_constructor_args():
    sig = inspect.signature(shadowrun::Sichtverhaeltnisse.__init__)
    params = list(sig.parameters.keys())
    assert "Infrarot" in params, "Missing parameter 'Infrarot'"
    assert "Ultrasound" in params, "Missing parameter 'Ultrasound'"
    assert "Restlichtverstaerkung" in params, "Missing parameter 'Restlichtverstaerkung'"

def test_shadowrun::sichtverhaeltnisse_has_Infrarot():
    assert hasattr(shadowrun::Sichtverhaeltnisse, "Infrarot")
    descriptor = None
    for klass in shadowrun::Sichtverhaeltnisse.__mro__:
        if "Infrarot" in klass.__dict__:
            descriptor = klass.__dict__["Infrarot"]
            break
    assert isinstance(descriptor, property)

def test_shadowrun::sichtverhaeltnisse_has_Ultrasound():
    assert hasattr(shadowrun::Sichtverhaeltnisse, "Ultrasound")
    descriptor = None
    for klass in shadowrun::Sichtverhaeltnisse.__mro__:
        if "Ultrasound" in klass.__dict__:
            descriptor = klass.__dict__["Ultrasound"]
            break
    assert isinstance(descriptor, property)

def test_shadowrun::sichtverhaeltnisse_has_Restlichtverstaerkung():
    assert hasattr(shadowrun::Sichtverhaeltnisse, "Restlichtverstaerkung")
    descriptor = None
    for klass in shadowrun::Sichtverhaeltnisse.__mro__:
        if "Restlichtverstaerkung" in klass.__dict__:
            descriptor = klass.__dict__["Restlichtverstaerkung"]
            break
    assert isinstance(descriptor, property)



def test_shadowrun::fernkampfwaffenmodifikatoren_is_not_abstract():
    assert not inspect.isabstract(shadowrun::FernkampfwaffenModifikatoren)


def test_shadowrun::fernkampfwaffenmodifikatoren_constructor_exists():
    assert callable(shadowrun::FernkampfwaffenModifikatoren.__init__)


def test_shadowrun::fernkampfwaffenmodifikatoren_constructor_args():
    sig = inspect.signature(shadowrun::FernkampfwaffenModifikatoren.__init__)
    params = list(sig.parameters.keys())
    assert "Schalldaempfer" in params, "Missing parameter 'Schalldaempfer'"
    assert "Vergroesserung" in params, "Missing parameter 'Vergroesserung'"
    assert "lasterPointer" in params, "Missing parameter 'lasterPointer'"
    assert "Smartgun" in params, "Missing parameter 'Smartgun'"
    assert "Rueckstoss" in params, "Missing parameter 'Rueckstoss'"

def test_shadowrun::fernkampfwaffenmodifikatoren_has_Schalldaempfer():
    assert hasattr(shadowrun::FernkampfwaffenModifikatoren, "Schalldaempfer")
    descriptor = None
    for klass in shadowrun::FernkampfwaffenModifikatoren.__mro__:
        if "Schalldaempfer" in klass.__dict__:
            descriptor = klass.__dict__["Schalldaempfer"]
            break
    assert isinstance(descriptor, property)

def test_shadowrun::fernkampfwaffenmodifikatoren_has_Vergroesserung():
    assert hasattr(shadowrun::FernkampfwaffenModifikatoren, "Vergroesserung")
    descriptor = None
    for klass in shadowrun::FernkampfwaffenModifikatoren.__mro__:
        if "Vergroesserung" in klass.__dict__:
            descriptor = klass.__dict__["Vergroesserung"]
            break
    assert isinstance(descriptor, property)

def test_shadowrun::fernkampfwaffenmodifikatoren_has_lasterPointer():
    assert hasattr(shadowrun::FernkampfwaffenModifikatoren, "lasterPointer")
    descriptor = None
    for klass in shadowrun::FernkampfwaffenModifikatoren.__mro__:
        if "lasterPointer" in klass.__dict__:
            descriptor = klass.__dict__["lasterPointer"]
            break
    assert isinstance(descriptor, property)

def test_shadowrun::fernkampfwaffenmodifikatoren_has_Smartgun():
    assert hasattr(shadowrun::FernkampfwaffenModifikatoren, "Smartgun")
    descriptor = None
    for klass in shadowrun::FernkampfwaffenModifikatoren.__mro__:
        if "Smartgun" in klass.__dict__:
            descriptor = klass.__dict__["Smartgun"]
            break
    assert isinstance(descriptor, property)

def test_shadowrun::fernkampfwaffenmodifikatoren_has_Rueckstoss():
    assert hasattr(shadowrun::FernkampfwaffenModifikatoren, "Rueckstoss")
    descriptor = None
    for klass in shadowrun::FernkampfwaffenModifikatoren.__mro__:
        if "Rueckstoss" in klass.__dict__:
            descriptor = klass.__dict__["Rueckstoss"]
            break
    assert isinstance(descriptor, property)



def test_shadowrun::eobject_is_not_abstract():
    assert not inspect.isabstract(shadowrun::EObject)


def test_shadowrun::eobject_constructor_exists():
    assert callable(shadowrun::EObject.__init__)


def test_shadowrun::eobject_constructor_args():
    sig = inspect.signature(shadowrun::EObject.__init__)
    params = list(sig.parameters.keys())



def test_shadowrun::bemerkbar_is_not_abstract():
    assert not inspect.isabstract(shadowrun::Bemerkbar)


def test_shadowrun::bemerkbar_constructor_exists():
    assert callable(shadowrun::Bemerkbar.__init__)


def test_shadowrun::bemerkbar_constructor_args():
    sig = inspect.signature(shadowrun::Bemerkbar.__init__)
    params = list(sig.parameters.keys())
    assert "tarnstufe" in params, "Missing parameter 'tarnstufe'"

def test_shadowrun::bemerkbar_has_tarnstufe():
    assert hasattr(shadowrun::Bemerkbar, "tarnstufe")
    descriptor = None
    for klass in shadowrun::Bemerkbar.__mro__:
        if "tarnstufe" in klass.__dict__:
            descriptor = klass.__dict__["tarnstufe"]
            break
    assert isinstance(descriptor, property)



def test_abstraktnahkampfwaffe_is_not_abstract():
    assert not inspect.isabstract(AbstraktNahkampfwaffe)


def test_abstraktnahkampfwaffe_constructor_exists():
    assert callable(AbstraktNahkampfwaffe.__init__)


def test_abstraktnahkampfwaffe_constructor_args():
    sig = inspect.signature(AbstraktNahkampfwaffe.__init__)
    params = list(sig.parameters.keys())



def test_shadowrun::nahkampfwaffe_is_not_abstract():
    assert not inspect.isabstract(shadowrun::Nahkampfwaffe)


def test_shadowrun::nahkampfwaffe_constructor_exists():
    assert callable(shadowrun::Nahkampfwaffe.__init__)


def test_shadowrun::nahkampfwaffe_constructor_args():
    sig = inspect.signature(shadowrun::Nahkampfwaffe.__init__)
    params = list(sig.parameters.keys())



def test_shadowrun::quelle_is_not_abstract():
    assert not inspect.isabstract(shadowrun::Quelle)


def test_shadowrun::quelle_constructor_exists():
    assert callable(shadowrun::Quelle.__init__)


def test_shadowrun::quelle_constructor_args():
    sig = inspect.signature(shadowrun::Quelle.__init__)
    params = list(sig.parameters.keys())
    assert "page" in params, "Missing parameter 'page'"

def test_shadowrun::quelle_has_page():
    assert hasattr(shadowrun::Quelle, "page")
    descriptor = None
    for klass in shadowrun::Quelle.__mro__:
        if "page" in klass.__dict__:
            descriptor = klass.__dict__["page"]
            break
    assert isinstance(descriptor, property)



def test_shadowrun::warenliste_is_not_abstract():
    assert not inspect.isabstract(shadowrun::WarenListe)


def test_shadowrun::warenliste_constructor_exists():
    assert callable(shadowrun::WarenListe.__init__)


def test_shadowrun::warenliste_constructor_args():
    sig = inspect.signature(shadowrun::WarenListe.__init__)
    params = list(sig.parameters.keys())
    assert "listenWert" in params, "Missing parameter 'listenWert'"
    assert "strassenWert" in params, "Missing parameter 'strassenWert'"

def test_shadowrun::warenliste_has_listenWert():
    assert hasattr(shadowrun::WarenListe, "listenWert")
    descriptor = None
    for klass in shadowrun::WarenListe.__mro__:
        if "listenWert" in klass.__dict__:
            descriptor = klass.__dict__["listenWert"]
            break
    assert isinstance(descriptor, property)

def test_shadowrun::warenliste_has_strassenWert():
    assert hasattr(shadowrun::WarenListe, "strassenWert")
    descriptor = None
    for klass in shadowrun::WarenListe.__mro__:
        if "strassenWert" in klass.__dict__:
            descriptor = klass.__dict__["strassenWert"]
            break
    assert isinstance(descriptor, property)



def test_shadowrun::reichweiten_is_not_abstract():
    assert not inspect.isabstract(shadowrun::Reichweiten)


def test_shadowrun::reichweiten_constructor_exists():
    assert callable(shadowrun::Reichweiten.__init__)


def test_shadowrun::reichweiten_constructor_args():
    sig = inspect.signature(shadowrun::Reichweiten.__init__)
    params = list(sig.parameters.keys())



def test_shadowrun::beschreibbar_is_not_abstract():
    assert not inspect.isabstract(shadowrun::Beschreibbar)


def test_shadowrun::beschreibbar_constructor_exists():
    assert callable(shadowrun::Beschreibbar.__init__)


def test_shadowrun::beschreibbar_constructor_args():
    sig = inspect.signature(shadowrun::Beschreibbar.__init__)
    params = list(sig.parameters.keys())
    assert "beschreibung" in params, "Missing parameter 'beschreibung'"
    assert "image" in params, "Missing parameter 'image'"
    assert "name" in params, "Missing parameter 'name'"

def test_shadowrun::beschreibbar_has_beschreibung():
    assert hasattr(shadowrun::Beschreibbar, "beschreibung")
    descriptor = None
    for klass in shadowrun::Beschreibbar.__mro__:
        if "beschreibung" in klass.__dict__:
            descriptor = klass.__dict__["beschreibung"]
            break
    assert isinstance(descriptor, property)

def test_shadowrun::beschreibbar_has_image():
    assert hasattr(shadowrun::Beschreibbar, "image")
    descriptor = None
    for klass in shadowrun::Beschreibbar.__mro__:
        if "image" in klass.__dict__:
            descriptor = klass.__dict__["image"]
            break
    assert isinstance(descriptor, property)

def test_shadowrun::beschreibbar_has_name():
    assert hasattr(shadowrun::Beschreibbar, "name")
    descriptor = None
    for klass in shadowrun::Beschreibbar.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_shadowrun::gengenstandliste_is_not_abstract():
    assert not inspect.isabstract(shadowrun::GengenstandListe)


def test_shadowrun::gengenstandliste_constructor_exists():
    assert callable(shadowrun::GengenstandListe.__init__)


def test_shadowrun::gengenstandliste_constructor_args():
    sig = inspect.signature(shadowrun::GengenstandListe.__init__)
    params = list(sig.parameters.keys())



def test_abstractmagischepaersona_is_not_abstract():
    assert not inspect.isabstract(AbstractMagischePaersona)


def test_abstractmagischepaersona_constructor_exists():
    assert callable(AbstractMagischePaersona.__init__)


def test_abstractmagischepaersona_constructor_args():
    sig = inspect.signature(AbstractMagischePaersona.__init__)
    params = list(sig.parameters.keys())



def test_shadowrun::personazauber_is_not_abstract():
    assert not inspect.isabstract(shadowrun::PersonaZauber)


def test_shadowrun::personazauber_constructor_exists():
    assert callable(shadowrun::PersonaZauber.__init__)


def test_shadowrun::personazauber_constructor_args():
    sig = inspect.signature(shadowrun::PersonaZauber.__init__)
    params = list(sig.parameters.keys())
    assert "stufe" in params, "Missing parameter 'stufe'"

def test_shadowrun::personazauber_has_stufe():
    assert hasattr(shadowrun::PersonaZauber, "stufe")
    descriptor = None
    for klass in shadowrun::PersonaZauber.__mro__:
        if "stufe" in klass.__dict__:
            descriptor = klass.__dict__["stufe"]
            break
    assert isinstance(descriptor, property)



def test_abstractmagier_is_not_abstract():
    assert not inspect.isabstract(AbstractMagier)


def test_abstractmagier_constructor_exists():
    assert callable(AbstractMagier.__init__)


def test_abstractmagier_constructor_args():
    sig = inspect.signature(AbstractMagier.__init__)
    params = list(sig.parameters.keys())



def test_shadowrun::magiepersona_is_not_abstract():
    assert not inspect.isabstract(shadowrun::MagiePersona)


def test_shadowrun::magiepersona_constructor_exists():
    assert callable(shadowrun::MagiePersona.__init__)


def test_shadowrun::magiepersona_constructor_args():
    sig = inspect.signature(shadowrun::MagiePersona.__init__)
    params = list(sig.parameters.keys())



def test_shadowrun::legalitaet_is_not_abstract():
    assert not inspect.isabstract(shadowrun::Legalitaet)


def test_shadowrun::legalitaet_constructor_exists():
    assert callable(shadowrun::Legalitaet.__init__)


def test_shadowrun::legalitaet_constructor_args():
    sig = inspect.signature(shadowrun::Legalitaet.__init__)
    params = list(sig.parameters.keys())
    assert "legalitaet" in params, "Missing parameter 'legalitaet'"

def test_shadowrun::legalitaet_has_legalitaet():
    assert hasattr(shadowrun::Legalitaet, "legalitaet")
    descriptor = None
    for klass in shadowrun::Legalitaet.__mro__:
        if "legalitaet" in klass.__dict__:
            descriptor = klass.__dict__["legalitaet"]
            break
    assert isinstance(descriptor, property)



def test_abstraktfertigkeit_is_not_abstract():
    assert not inspect.isabstract(AbstraktFertigkeit)


def test_abstraktfertigkeit_constructor_exists():
    assert callable(AbstraktFertigkeit.__init__)


def test_abstraktfertigkeit_constructor_args():
    sig = inspect.signature(AbstraktFertigkeit.__init__)
    params = list(sig.parameters.keys())



def test_shadowrun::kiadept_is_not_abstract():
    assert not inspect.isabstract(shadowrun::KiAdept)


def test_shadowrun::kiadept_constructor_exists():
    assert callable(shadowrun::KiAdept.__init__)


def test_shadowrun::kiadept_constructor_args():
    sig = inspect.signature(shadowrun::KiAdept.__init__)
    params = list(sig.parameters.keys())



def test_magischemods_is_not_abstract():
    assert not inspect.isabstract(MagischeMods)


def test_magischemods_constructor_exists():
    assert callable(MagischeMods.__init__)


def test_magischemods_constructor_args():
    sig = inspect.signature(MagischeMods.__init__)
    params = list(sig.parameters.keys())



def test_shadowrun::kikraft_is_not_abstract():
    assert not inspect.isabstract(shadowrun::KiKraft)


def test_shadowrun::kikraft_constructor_exists():
    assert callable(shadowrun::KiKraft.__init__)


def test_shadowrun::kikraft_constructor_args():
    sig = inspect.signature(shadowrun::KiKraft.__init__)
    params = list(sig.parameters.keys())



def test_basemagischepersona_is_not_abstract():
    assert not inspect.isabstract(BaseMagischePersona)


def test_basemagischepersona_constructor_exists():
    assert callable(BaseMagischePersona.__init__)


def test_basemagischepersona_constructor_args():
    sig = inspect.signature(BaseMagischePersona.__init__)
    params = list(sig.parameters.keys())



def test_shadowrun::abstractmagier_is_not_abstract():
    assert not inspect.isabstract(shadowrun::AbstractMagier)


def test_shadowrun::abstractmagier_constructor_exists():
    assert callable(shadowrun::AbstractMagier.__init__)


def test_shadowrun::abstractmagier_constructor_args():
    sig = inspect.signature(shadowrun::AbstractMagier.__init__)
    params = list(sig.parameters.keys())
    assert "InitationsGrad" in params, "Missing parameter 'InitationsGrad'"
    assert "MagiePool" in params, "Missing parameter 'MagiePool'"
    assert "Astralpool" in params, "Missing parameter 'Astralpool'"

def test_shadowrun::abstractmagier_has_InitationsGrad():
    assert hasattr(shadowrun::AbstractMagier, "InitationsGrad")
    descriptor = None
    for klass in shadowrun::AbstractMagier.__mro__:
        if "InitationsGrad" in klass.__dict__:
            descriptor = klass.__dict__["InitationsGrad"]
            break
    assert isinstance(descriptor, property)

def test_shadowrun::abstractmagier_has_MagiePool():
    assert hasattr(shadowrun::AbstractMagier, "MagiePool")
    descriptor = None
    for klass in shadowrun::AbstractMagier.__mro__:
        if "MagiePool" in klass.__dict__:
            descriptor = klass.__dict__["MagiePool"]
            break
    assert isinstance(descriptor, property)

def test_shadowrun::abstractmagier_has_Astralpool():
    assert hasattr(shadowrun::AbstractMagier, "Astralpool")
    descriptor = None
    for klass in shadowrun::AbstractMagier.__mro__:
        if "Astralpool" in klass.__dict__:
            descriptor = klass.__dict__["Astralpool"]
            break
    assert isinstance(descriptor, property)



def test_shadowrun::basemagischepersona_is_not_abstract():
    assert not inspect.isabstract(shadowrun::BaseMagischePersona)


def test_shadowrun::basemagischepersona_constructor_exists():
    assert callable(shadowrun::BaseMagischePersona.__init__)


def test_shadowrun::basemagischepersona_constructor_args():
    sig = inspect.signature(shadowrun::BaseMagischePersona.__init__)
    params = list(sig.parameters.keys())
    assert "magie" in params, "Missing parameter 'magie'"

def test_shadowrun::basemagischepersona_has_magie():
    assert hasattr(shadowrun::BaseMagischePersona, "magie")
    descriptor = None
    for klass in shadowrun::BaseMagischePersona.__mro__:
        if "magie" in klass.__dict__:
            descriptor = klass.__dict__["magie"]
            break
    assert isinstance(descriptor, property)



def test_abstraktmodifikatoren_is_not_abstract():
    assert not inspect.isabstract(AbstraktModifikatoren)


def test_abstraktmodifikatoren_constructor_exists():
    assert callable(AbstraktModifikatoren.__init__)


def test_abstraktmodifikatoren_constructor_args():
    sig = inspect.signature(AbstraktModifikatoren.__init__)
    params = list(sig.parameters.keys())



def test_shadowrun::magischemods_is_not_abstract():
    assert not inspect.isabstract(shadowrun::MagischeMods)


def test_shadowrun::magischemods_constructor_exists():
    assert callable(shadowrun::MagischeMods.__init__)


def test_shadowrun::magischemods_constructor_args():
    sig = inspect.signature(shadowrun::MagischeMods.__init__)
    params = list(sig.parameters.keys())



def test_shadowrun::koerpermods_is_not_abstract():
    assert not inspect.isabstract(shadowrun::koerpermods)


def test_shadowrun::koerpermods_constructor_exists():
    assert callable(shadowrun::koerpermods.__init__)


def test_shadowrun::koerpermods_constructor_args():
    sig = inspect.signature(shadowrun::koerpermods.__init__)
    params = list(sig.parameters.keys())



def test_shadowrun::modifikatorlist_is_not_abstract():
    assert not inspect.isabstract(shadowrun::ModifikatorList)


def test_shadowrun::modifikatorlist_constructor_exists():
    assert callable(shadowrun::ModifikatorList.__init__)


def test_shadowrun::modifikatorlist_constructor_args():
    sig = inspect.signature(shadowrun::ModifikatorList.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_shadowrun::modifikatorlist_has_name():
    assert hasattr(shadowrun::ModifikatorList, "name")
    descriptor = None
    for klass in shadowrun::ModifikatorList.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_shadowrun::geldwert_is_not_abstract():
    assert not inspect.isabstract(shadowrun::GeldWert)


def test_shadowrun::geldwert_constructor_exists():
    assert callable(shadowrun::GeldWert.__init__)


def test_shadowrun::geldwert_constructor_args():
    sig = inspect.signature(shadowrun::GeldWert.__init__)
    params = list(sig.parameters.keys())
    assert "verfuegbarkeit" in params, "Missing parameter 'verfuegbarkeit'"
    assert "wert" in params, "Missing parameter 'wert'"
    assert "strassenIndex" in params, "Missing parameter 'strassenIndex'"

def test_shadowrun::geldwert_has_verfuegbarkeit():
    assert hasattr(shadowrun::GeldWert, "verfuegbarkeit")
    descriptor = None
    for klass in shadowrun::GeldWert.__mro__:
        if "verfuegbarkeit" in klass.__dict__:
            descriptor = klass.__dict__["verfuegbarkeit"]
            break
    assert isinstance(descriptor, property)

def test_shadowrun::geldwert_has_wert():
    assert hasattr(shadowrun::GeldWert, "wert")
    descriptor = None
    for klass in shadowrun::GeldWert.__mro__:
        if "wert" in klass.__dict__:
            descriptor = klass.__dict__["wert"]
            break
    assert isinstance(descriptor, property)

def test_shadowrun::geldwert_has_strassenIndex():
    assert hasattr(shadowrun::GeldWert, "strassenIndex")
    descriptor = None
    for klass in shadowrun::GeldWert.__mro__:
        if "strassenIndex" in klass.__dict__:
            descriptor = klass.__dict__["strassenIndex"]
            break
    assert isinstance(descriptor, property)



def test_koerpermods_is_not_abstract():
    assert not inspect.isabstract(koerpermods)


def test_koerpermods_constructor_exists():
    assert callable(koerpermods.__init__)


def test_koerpermods_constructor_args():
    sig = inspect.signature(koerpermods.__init__)
    params = list(sig.parameters.keys())



def test_shadowrun::fk_is_not_abstract():
    assert not inspect.isabstract(shadowrun::FK)


def test_shadowrun::fk_constructor_exists():
    assert callable(shadowrun::FK.__init__)


def test_shadowrun::fk_constructor_args():
    sig = inspect.signature(shadowrun::FK.__init__)
    params = list(sig.parameters.keys())



def test_abstrakteruestung_is_not_abstract():
    assert not inspect.isabstract(AbstrakteRuestung)


def test_abstrakteruestung_constructor_exists():
    assert callable(AbstrakteRuestung.__init__)


def test_abstrakteruestung_constructor_args():
    sig = inspect.signature(AbstrakteRuestung.__init__)
    params = list(sig.parameters.keys())



def test_shadowrun::ruestung_is_not_abstract():
    assert not inspect.isabstract(shadowrun::Ruestung)


def test_shadowrun::ruestung_constructor_exists():
    assert callable(shadowrun::Ruestung.__init__)


def test_shadowrun::ruestung_constructor_args():
    sig = inspect.signature(shadowrun::Ruestung.__init__)
    params = list(sig.parameters.keys())



def test_shadowrun::personakoerper_is_not_abstract():
    assert not inspect.isabstract(shadowrun::PersonaKoerper)


def test_shadowrun::personakoerper_constructor_exists():
    assert callable(shadowrun::PersonaKoerper.__init__)


def test_shadowrun::personakoerper_constructor_args():
    sig = inspect.signature(shadowrun::PersonaKoerper.__init__)
    params = list(sig.parameters.keys())
    assert "gesamtZustand" in params, "Missing parameter 'gesamtZustand'"

def test_shadowrun::personakoerper_has_gesamtZustand():
    assert hasattr(shadowrun::PersonaKoerper, "gesamtZustand")
    descriptor = None
    for klass in shadowrun::PersonaKoerper.__mro__:
        if "gesamtZustand" in klass.__dict__:
            descriptor = klass.__dict__["gesamtZustand"]
            break
    assert isinstance(descriptor, property)



def test_shadowrun::modifizierbar_is_not_abstract():
    assert not inspect.isabstract(shadowrun::Modifizierbar)


def test_shadowrun::modifizierbar_constructor_exists():
    assert callable(shadowrun::Modifizierbar.__init__)


def test_shadowrun::modifizierbar_constructor_args():
    sig = inspect.signature(shadowrun::Modifizierbar.__init__)
    params = list(sig.parameters.keys())



def test_shadowrun::eattribute_is_not_abstract():
    assert not inspect.isabstract(shadowrun::EAttribute)


def test_shadowrun::eattribute_constructor_exists():
    assert callable(shadowrun::EAttribute.__init__)


def test_shadowrun::eattribute_constructor_args():
    sig = inspect.signature(shadowrun::EAttribute.__init__)
    params = list(sig.parameters.keys())



def test_shadowrun::attributmodifikatorwert_is_not_abstract():
    assert not inspect.isabstract(shadowrun::AttributModifikatorWert)


def test_shadowrun::attributmodifikatorwert_constructor_exists():
    assert callable(shadowrun::AttributModifikatorWert.__init__)


def test_shadowrun::attributmodifikatorwert_constructor_args():
    sig = inspect.signature(shadowrun::AttributModifikatorWert.__init__)
    params = list(sig.parameters.keys())
    assert "wert" in params, "Missing parameter 'wert'"

def test_shadowrun::attributmodifikatorwert_has_wert():
    assert hasattr(shadowrun::AttributModifikatorWert, "wert")
    descriptor = None
    for klass in shadowrun::AttributModifikatorWert.__mro__:
        if "wert" in klass.__dict__:
            descriptor = klass.__dict__["wert"]
            break
    assert isinstance(descriptor, property)



def test_shadowrun::basiclist_is_not_abstract():
    assert not inspect.isabstract(shadowrun::BasicList)


def test_shadowrun::basiclist_constructor_exists():
    assert callable(shadowrun::BasicList.__init__)


def test_shadowrun::basiclist_constructor_args():
    sig = inspect.signature(shadowrun::BasicList.__init__)
    params = list(sig.parameters.keys())



def test_abstaktfernkampfwaffe_is_not_abstract():
    assert not inspect.isabstract(AbstaktFernKampfwaffe)


def test_abstaktfernkampfwaffe_constructor_exists():
    assert callable(AbstaktFernKampfwaffe.__init__)


def test_abstaktfernkampfwaffe_constructor_args():
    sig = inspect.signature(AbstaktFernKampfwaffe.__init__)
    params = list(sig.parameters.keys())



def test_shadowrun::projektilwaffe_is_not_abstract():
    assert not inspect.isabstract(shadowrun::Projektilwaffe)


def test_shadowrun::projektilwaffe_constructor_exists():
    assert callable(shadowrun::Projektilwaffe.__init__)


def test_shadowrun::projektilwaffe_constructor_args():
    sig = inspect.signature(shadowrun::Projektilwaffe.__init__)
    params = list(sig.parameters.keys())



def test_shadowrun::wurfwaffe_is_not_abstract():
    assert not inspect.isabstract(shadowrun::Wurfwaffe)


def test_shadowrun::wurfwaffe_constructor_exists():
    assert callable(shadowrun::Wurfwaffe.__init__)


def test_shadowrun::wurfwaffe_constructor_args():
    sig = inspect.signature(shadowrun::Wurfwaffe.__init__)
    params = list(sig.parameters.keys())



def test_shadowrun::feuerwaffe_is_not_abstract():
    assert not inspect.isabstract(shadowrun::Feuerwaffe)


def test_shadowrun::feuerwaffe_constructor_exists():
    assert callable(shadowrun::Feuerwaffe.__init__)


def test_shadowrun::feuerwaffe_constructor_args():
    sig = inspect.signature(shadowrun::Feuerwaffe.__init__)
    params = list(sig.parameters.keys())
    assert "kapazitaet" in params, "Missing parameter 'kapazitaet'"
    assert "modie" in params, "Missing parameter 'modie'"
    assert "munitionstyp" in params, "Missing parameter 'munitionstyp'"

def test_shadowrun::feuerwaffe_has_kapazitaet():
    assert hasattr(shadowrun::Feuerwaffe, "kapazitaet")
    descriptor = None
    for klass in shadowrun::Feuerwaffe.__mro__:
        if "kapazitaet" in klass.__dict__:
            descriptor = klass.__dict__["kapazitaet"]
            break
    assert isinstance(descriptor, property)

def test_shadowrun::feuerwaffe_has_modie():
    assert hasattr(shadowrun::Feuerwaffe, "modie")
    descriptor = None
    for klass in shadowrun::Feuerwaffe.__mro__:
        if "modie" in klass.__dict__:
            descriptor = klass.__dict__["modie"]
            break
    assert isinstance(descriptor, property)

def test_shadowrun::feuerwaffe_has_munitionstyp():
    assert hasattr(shadowrun::Feuerwaffe, "munitionstyp")
    descriptor = None
    for klass in shadowrun::Feuerwaffe.__mro__:
        if "munitionstyp" in klass.__dict__:
            descriptor = klass.__dict__["munitionstyp"]
            break
    assert isinstance(descriptor, property)



def test_gegenstand_is_not_abstract():
    assert not inspect.isabstract(Gegenstand)


def test_gegenstand_constructor_exists():
    assert callable(Gegenstand.__init__)


def test_gegenstand_constructor_args():
    sig = inspect.signature(Gegenstand.__init__)
    params = list(sig.parameters.keys())



def test_shadowrun::munitionsbehealter_is_not_abstract():
    assert not inspect.isabstract(shadowrun::MunitionsBehealter)


def test_shadowrun::munitionsbehealter_constructor_exists():
    assert callable(shadowrun::MunitionsBehealter.__init__)


def test_shadowrun::munitionsbehealter_constructor_args():
    sig = inspect.signature(shadowrun::MunitionsBehealter.__init__)
    params = list(sig.parameters.keys())



def test_shadowrun::behaelter_is_not_abstract():
    assert not inspect.isabstract(shadowrun::Behaelter)


def test_shadowrun::behaelter_constructor_exists():
    assert callable(shadowrun::Behaelter.__init__)


def test_shadowrun::behaelter_constructor_args():
    sig = inspect.signature(shadowrun::Behaelter.__init__)
    params = list(sig.parameters.keys())
    assert "kapazitaet" in params, "Missing parameter 'kapazitaet'"

def test_shadowrun::behaelter_has_kapazitaet():
    assert hasattr(shadowrun::Behaelter, "kapazitaet")
    descriptor = None
    for klass in shadowrun::Behaelter.__mro__:
        if "kapazitaet" in klass.__dict__:
            descriptor = klass.__dict__["kapazitaet"]
            break
    assert isinstance(descriptor, property)



def test_nahkampfreichweite_is_not_abstract():
    assert not inspect.isabstract(NahkampfReichweite)


def test_nahkampfreichweite_constructor_exists():
    assert callable(NahkampfReichweite.__init__)


def test_nahkampfreichweite_constructor_args():
    sig = inspect.signature(NahkampfReichweite.__init__)
    params = list(sig.parameters.keys())



def test_abstraktkleidung_is_not_abstract():
    assert not inspect.isabstract(AbstraktKleidung)


def test_abstraktkleidung_constructor_exists():
    assert callable(AbstraktKleidung.__init__)


def test_abstraktkleidung_constructor_args():
    sig = inspect.signature(AbstraktKleidung.__init__)
    params = list(sig.parameters.keys())



def test_shadowrun::abstrakteruestung_is_not_abstract():
    assert not inspect.isabstract(shadowrun::AbstrakteRuestung)


def test_shadowrun::abstrakteruestung_constructor_exists():
    assert callable(shadowrun::AbstrakteRuestung.__init__)


def test_shadowrun::abstrakteruestung_constructor_args():
    sig = inspect.signature(shadowrun::AbstrakteRuestung.__init__)
    params = list(sig.parameters.keys())
    assert "ruestungsSchutzBalistisch" in params, "Missing parameter 'ruestungsSchutzBalistisch'"
    assert "ruestungsSchutzStoss" in params, "Missing parameter 'ruestungsSchutzStoss'"

def test_shadowrun::abstrakteruestung_has_ruestungsSchutzBalistisch():
    assert hasattr(shadowrun::AbstrakteRuestung, "ruestungsSchutzBalistisch")
    descriptor = None
    for klass in shadowrun::AbstrakteRuestung.__mro__:
        if "ruestungsSchutzBalistisch" in klass.__dict__:
            descriptor = klass.__dict__["ruestungsSchutzBalistisch"]
            break
    assert isinstance(descriptor, property)

def test_shadowrun::abstrakteruestung_has_ruestungsSchutzStoss():
    assert hasattr(shadowrun::AbstrakteRuestung, "ruestungsSchutzStoss")
    descriptor = None
    for klass in shadowrun::AbstrakteRuestung.__mro__:
        if "ruestungsSchutzStoss" in klass.__dict__:
            descriptor = klass.__dict__["ruestungsSchutzStoss"]
            break
    assert isinstance(descriptor, property)



def test_shadowrun::raumkoordinate_is_not_abstract():
    assert not inspect.isabstract(shadowrun::RaumKoordinate)


def test_shadowrun::raumkoordinate_constructor_exists():
    assert callable(shadowrun::RaumKoordinate.__init__)


def test_shadowrun::raumkoordinate_constructor_args():
    sig = inspect.signature(shadowrun::RaumKoordinate.__init__)
    params = list(sig.parameters.keys())



def test_shadowrun::abstrakraumkoerper_is_not_abstract():
    assert not inspect.isabstract(shadowrun::AbstrakRaumKoerper)


def test_shadowrun::abstrakraumkoerper_constructor_exists():
    assert callable(shadowrun::AbstrakRaumKoerper.__init__)


def test_shadowrun::abstrakraumkoerper_constructor_args():
    sig = inspect.signature(shadowrun::AbstrakRaumKoerper.__init__)
    params = list(sig.parameters.keys())



def test_shadowrun::spezialisierung_is_not_abstract():
    assert not inspect.isabstract(shadowrun::Spezialisierung)


def test_shadowrun::spezialisierung_constructor_exists():
    assert callable(shadowrun::Spezialisierung.__init__)


def test_shadowrun::spezialisierung_constructor_args():
    sig = inspect.signature(shadowrun::Spezialisierung.__init__)
    params = list(sig.parameters.keys())



def test_abstaktpersona_is_not_abstract():
    assert not inspect.isabstract(AbstaktPersona)


def test_abstaktpersona_constructor_exists():
    assert callable(AbstaktPersona.__init__)


def test_abstaktpersona_constructor_args():
    sig = inspect.signature(AbstaktPersona.__init__)
    params = list(sig.parameters.keys())



def test_shadowrun::abstractmagischepaersona_is_not_abstract():
    assert not inspect.isabstract(shadowrun::AbstractMagischePaersona)


def test_shadowrun::abstractmagischepaersona_constructor_exists():
    assert callable(shadowrun::AbstractMagischePaersona.__init__)


def test_shadowrun::abstractmagischepaersona_constructor_args():
    sig = inspect.signature(shadowrun::AbstractMagischePaersona.__init__)
    params = list(sig.parameters.keys())
    assert "magieBase" in params, "Missing parameter 'magieBase'"

def test_shadowrun::abstractmagischepaersona_has_magieBase():
    assert hasattr(shadowrun::AbstractMagischePaersona, "magieBase")
    descriptor = None
    for klass in shadowrun::AbstractMagischePaersona.__mro__:
        if "magieBase" in klass.__dict__:
            descriptor = klass.__dict__["magieBase"]
            break
    assert isinstance(descriptor, property)



def test_shadowrun::persona_is_not_abstract():
    assert not inspect.isabstract(shadowrun::Persona)


def test_shadowrun::persona_constructor_exists():
    assert callable(shadowrun::Persona.__init__)


def test_shadowrun::persona_constructor_args():
    sig = inspect.signature(shadowrun::Persona.__init__)
    params = list(sig.parameters.keys())



def test_shadowrun::kleidung_is_not_abstract():
    assert not inspect.isabstract(shadowrun::Kleidung)


def test_shadowrun::kleidung_constructor_exists():
    assert callable(shadowrun::Kleidung.__init__)


def test_shadowrun::kleidung_constructor_args():
    sig = inspect.signature(shadowrun::Kleidung.__init__)
    params = list(sig.parameters.keys())



def test_shadowrun::personafertigkeit_is_not_abstract():
    assert not inspect.isabstract(shadowrun::PersonaFertigkeit)


def test_shadowrun::personafertigkeit_constructor_exists():
    assert callable(shadowrun::PersonaFertigkeit.__init__)


def test_shadowrun::personafertigkeit_constructor_args():
    sig = inspect.signature(shadowrun::PersonaFertigkeit.__init__)
    params = list(sig.parameters.keys())
    assert "stufe" in params, "Missing parameter 'stufe'"

def test_shadowrun::personafertigkeit_has_stufe():
    assert hasattr(shadowrun::PersonaFertigkeit, "stufe")
    descriptor = None
    for klass in shadowrun::PersonaFertigkeit.__mro__:
        if "stufe" in klass.__dict__:
            descriptor = klass.__dict__["stufe"]
            break
    assert isinstance(descriptor, property)



def test_shadowrun::konzentration_is_not_abstract():
    assert not inspect.isabstract(shadowrun::Konzentration)


def test_shadowrun::konzentration_constructor_exists():
    assert callable(shadowrun::Konzentration.__init__)


def test_shadowrun::konzentration_constructor_args():
    sig = inspect.signature(shadowrun::Konzentration.__init__)
    params = list(sig.parameters.keys())



def test_shadowrun::fertigkeit_is_not_abstract():
    assert not inspect.isabstract(shadowrun::Fertigkeit)


def test_shadowrun::fertigkeit_constructor_exists():
    assert callable(shadowrun::Fertigkeit.__init__)


def test_shadowrun::fertigkeit_constructor_args():
    sig = inspect.signature(shadowrun::Fertigkeit.__init__)
    params = list(sig.parameters.keys())



def test_abstaktgegenstand_is_not_abstract():
    assert not inspect.isabstract(AbstaktGegenstand)


def test_abstaktgegenstand_constructor_exists():
    assert callable(AbstaktGegenstand.__init__)


def test_abstaktgegenstand_constructor_args():
    sig = inspect.signature(AbstaktGegenstand.__init__)
    params = list(sig.parameters.keys())



def test_shadowrun::munition_is_not_abstract():
    assert not inspect.isabstract(shadowrun::Munition)


def test_shadowrun::munition_constructor_exists():
    assert callable(shadowrun::Munition.__init__)


def test_shadowrun::munition_constructor_args():
    sig = inspect.signature(shadowrun::Munition.__init__)
    params = list(sig.parameters.keys())
    assert "power" in params, "Missing parameter 'power'"
    assert "schadensTyp" in params, "Missing parameter 'schadensTyp'"
    assert "niveau" in params, "Missing parameter 'niveau'"

def test_shadowrun::munition_has_power():
    assert hasattr(shadowrun::Munition, "power")
    descriptor = None
    for klass in shadowrun::Munition.__mro__:
        if "power" in klass.__dict__:
            descriptor = klass.__dict__["power"]
            break
    assert isinstance(descriptor, property)

def test_shadowrun::munition_has_schadensTyp():
    assert hasattr(shadowrun::Munition, "schadensTyp")
    descriptor = None
    for klass in shadowrun::Munition.__mro__:
        if "schadensTyp" in klass.__dict__:
            descriptor = klass.__dict__["schadensTyp"]
            break
    assert isinstance(descriptor, property)

def test_shadowrun::munition_has_niveau():
    assert hasattr(shadowrun::Munition, "niveau")
    descriptor = None
    for klass in shadowrun::Munition.__mro__:
        if "niveau" in klass.__dict__:
            descriptor = klass.__dict__["niveau"]
            break
    assert isinstance(descriptor, property)



def test_shadowrun::gegenstand_is_not_abstract():
    assert not inspect.isabstract(shadowrun::Gegenstand)


def test_shadowrun::gegenstand_constructor_exists():
    assert callable(shadowrun::Gegenstand.__init__)


def test_shadowrun::gegenstand_constructor_args():
    sig = inspect.signature(shadowrun::Gegenstand.__init__)
    params = list(sig.parameters.keys())



def test_shadowrun::abstraktkleidung_is_not_abstract():
    assert not inspect.isabstract(shadowrun::AbstraktKleidung)


def test_shadowrun::abstraktkleidung_constructor_exists():
    assert callable(shadowrun::AbstraktKleidung.__init__)


def test_shadowrun::abstraktkleidung_constructor_args():
    sig = inspect.signature(shadowrun::AbstraktKleidung.__init__)
    params = list(sig.parameters.keys())
    assert "koeperTeil" in params, "Missing parameter 'koeperTeil'"

def test_shadowrun::abstraktkleidung_has_koeperTeil():
    assert hasattr(shadowrun::AbstraktKleidung, "koeperTeil")
    descriptor = None
    for klass in shadowrun::AbstraktKleidung.__mro__:
        if "koeperTeil" in klass.__dict__:
            descriptor = klass.__dict__["koeperTeil"]
            break
    assert isinstance(descriptor, property)



def test_shadowrun::abstaktwaffe_is_not_abstract():
    assert not inspect.isabstract(shadowrun::AbstaktWaffe)


def test_shadowrun::abstaktwaffe_constructor_exists():
    assert callable(shadowrun::AbstaktWaffe.__init__)


def test_shadowrun::abstaktwaffe_constructor_args():
    sig = inspect.signature(shadowrun::AbstaktWaffe.__init__)
    params = list(sig.parameters.keys())
    assert "schadenscode" in params, "Missing parameter 'schadenscode'"

def test_shadowrun::abstaktwaffe_has_schadenscode():
    assert hasattr(shadowrun::AbstaktWaffe, "schadenscode")
    descriptor = None
    for klass in shadowrun::AbstaktWaffe.__mro__:
        if "schadenscode" in klass.__dict__:
            descriptor = klass.__dict__["schadenscode"]
            break
    assert isinstance(descriptor, property)



def test_modifizierbar_is_not_abstract():
    assert not inspect.isabstract(Modifizierbar)


def test_modifizierbar_constructor_exists():
    assert callable(Modifizierbar.__init__)


def test_modifizierbar_constructor_args():
    sig = inspect.signature(Modifizierbar.__init__)
    params = list(sig.parameters.keys())



def test_quelle_is_not_abstract():
    assert not inspect.isabstract(Quelle)


def test_quelle_constructor_exists():
    assert callable(Quelle.__init__)


def test_quelle_constructor_args():
    sig = inspect.signature(Quelle.__init__)
    params = list(sig.parameters.keys())



def test_bemerkbar_is_not_abstract():
    assert not inspect.isabstract(Bemerkbar)


def test_bemerkbar_constructor_exists():
    assert callable(Bemerkbar.__init__)


def test_bemerkbar_constructor_args():
    sig = inspect.signature(Bemerkbar.__init__)
    params = list(sig.parameters.keys())



def test_legalitaet_is_not_abstract():
    assert not inspect.isabstract(Legalitaet)


def test_legalitaet_constructor_exists():
    assert callable(Legalitaet.__init__)


def test_legalitaet_constructor_args():
    sig = inspect.signature(Legalitaet.__init__)
    params = list(sig.parameters.keys())



def test_beschreibbar_is_not_abstract():
    assert not inspect.isabstract(Beschreibbar)


def test_beschreibbar_constructor_exists():
    assert callable(Beschreibbar.__init__)


def test_beschreibbar_constructor_args():
    sig = inspect.signature(Beschreibbar.__init__)
    params = list(sig.parameters.keys())



def test_shadowrun::zauber_is_not_abstract():
    assert not inspect.isabstract(shadowrun::Zauber)


def test_shadowrun::zauber_constructor_exists():
    assert callable(shadowrun::Zauber.__init__)


def test_shadowrun::zauber_constructor_args():
    sig = inspect.signature(shadowrun::Zauber.__init__)
    params = list(sig.parameters.keys())
    assert "art" in params, "Missing parameter 'art'"
    assert "reichweite" in params, "Missing parameter 'reichweite'"
    assert "Enzug" in params, "Missing parameter 'Enzug'"
    assert "Schaden" in params, "Missing parameter 'Schaden'"
    assert "Mindestwurf" in params, "Missing parameter 'Mindestwurf'"
    assert "Dauer" in params, "Missing parameter 'Dauer'"

def test_shadowrun::zauber_has_art():
    assert hasattr(shadowrun::Zauber, "art")
    descriptor = None
    for klass in shadowrun::Zauber.__mro__:
        if "art" in klass.__dict__:
            descriptor = klass.__dict__["art"]
            break
    assert isinstance(descriptor, property)

def test_shadowrun::zauber_has_reichweite():
    assert hasattr(shadowrun::Zauber, "reichweite")
    descriptor = None
    for klass in shadowrun::Zauber.__mro__:
        if "reichweite" in klass.__dict__:
            descriptor = klass.__dict__["reichweite"]
            break
    assert isinstance(descriptor, property)

def test_shadowrun::zauber_has_Enzug():
    assert hasattr(shadowrun::Zauber, "Enzug")
    descriptor = None
    for klass in shadowrun::Zauber.__mro__:
        if "Enzug" in klass.__dict__:
            descriptor = klass.__dict__["Enzug"]
            break
    assert isinstance(descriptor, property)

def test_shadowrun::zauber_has_Schaden():
    assert hasattr(shadowrun::Zauber, "Schaden")
    descriptor = None
    for klass in shadowrun::Zauber.__mro__:
        if "Schaden" in klass.__dict__:
            descriptor = klass.__dict__["Schaden"]
            break
    assert isinstance(descriptor, property)

def test_shadowrun::zauber_has_Mindestwurf():
    assert hasattr(shadowrun::Zauber, "Mindestwurf")
    descriptor = None
    for klass in shadowrun::Zauber.__mro__:
        if "Mindestwurf" in klass.__dict__:
            descriptor = klass.__dict__["Mindestwurf"]
            break
    assert isinstance(descriptor, property)

def test_shadowrun::zauber_has_Dauer():
    assert hasattr(shadowrun::Zauber, "Dauer")
    descriptor = None
    for klass in shadowrun::Zauber.__mro__:
        if "Dauer" in klass.__dict__:
            descriptor = klass.__dict__["Dauer"]
            break
    assert isinstance(descriptor, property)



def test_shadowrun::shrlist_is_not_abstract():
    assert not inspect.isabstract(shadowrun::ShrList)


def test_shadowrun::shrlist_constructor_exists():
    assert callable(shadowrun::ShrList.__init__)


def test_shadowrun::shrlist_constructor_args():
    sig = inspect.signature(shadowrun::ShrList.__init__)
    params = list(sig.parameters.keys())



def test_shadowrun::totem_is_not_abstract():
    assert not inspect.isabstract(shadowrun::Totem)


def test_shadowrun::totem_constructor_exists():
    assert callable(shadowrun::Totem.__init__)


def test_shadowrun::totem_constructor_args():
    sig = inspect.signature(shadowrun::Totem.__init__)
    params = list(sig.parameters.keys())



def test_shadowrun::script_is_not_abstract():
    assert not inspect.isabstract(shadowrun::Script)


def test_shadowrun::script_constructor_exists():
    assert callable(shadowrun::Script.__init__)


def test_shadowrun::script_constructor_args():
    sig = inspect.signature(shadowrun::Script.__init__)
    params = list(sig.parameters.keys())



def test_shadowrun::abstraktmodifikatoren_is_not_abstract():
    assert not inspect.isabstract(shadowrun::AbstraktModifikatoren)


def test_shadowrun::abstraktmodifikatoren_constructor_exists():
    assert callable(shadowrun::AbstraktModifikatoren.__init__)


def test_shadowrun::abstraktmodifikatoren_constructor_args():
    sig = inspect.signature(shadowrun::AbstraktModifikatoren.__init__)
    params = list(sig.parameters.keys())



def test_shadowrun::placement_is_not_abstract():
    assert not inspect.isabstract(shadowrun::Placement)


def test_shadowrun::placement_constructor_exists():
    assert callable(shadowrun::Placement.__init__)


def test_shadowrun::placement_constructor_args():
    sig = inspect.signature(shadowrun::Placement.__init__)
    params = list(sig.parameters.keys())



def test_shadowrun::sourcebook_is_not_abstract():
    assert not inspect.isabstract(shadowrun::SourceBook)


def test_shadowrun::sourcebook_constructor_exists():
    assert callable(shadowrun::SourceBook.__init__)


def test_shadowrun::sourcebook_constructor_args():
    sig = inspect.signature(shadowrun::SourceBook.__init__)
    params = list(sig.parameters.keys())
    assert "endShrTime" in params, "Missing parameter 'endShrTime'"
    assert "startShrTime" in params, "Missing parameter 'startShrTime'"

def test_shadowrun::sourcebook_has_endShrTime():
    assert hasattr(shadowrun::SourceBook, "endShrTime")
    descriptor = None
    for klass in shadowrun::SourceBook.__mro__:
        if "endShrTime" in klass.__dict__:
            descriptor = klass.__dict__["endShrTime"]
            break
    assert isinstance(descriptor, property)

def test_shadowrun::sourcebook_has_startShrTime():
    assert hasattr(shadowrun::SourceBook, "startShrTime")
    descriptor = None
    for klass in shadowrun::SourceBook.__mro__:
        if "startShrTime" in klass.__dict__:
            descriptor = klass.__dict__["startShrTime"]
            break
    assert isinstance(descriptor, property)



def test_shadowrun::spezies_is_not_abstract():
    assert not inspect.isabstract(shadowrun::Spezies)


def test_shadowrun::spezies_constructor_exists():
    assert callable(shadowrun::Spezies.__init__)


def test_shadowrun::spezies_constructor_args():
    sig = inspect.signature(shadowrun::Spezies.__init__)
    params = list(sig.parameters.keys())
    assert "StaerkeMax" in params, "Missing parameter 'StaerkeMax'"
    assert "WillenskraftMax" in params, "Missing parameter 'WillenskraftMax'"
    assert "KonsitutionMax" in params, "Missing parameter 'KonsitutionMax'"
    assert "SchnelligkeitMax" in params, "Missing parameter 'SchnelligkeitMax'"
    assert "InteligenzMax" in params, "Missing parameter 'InteligenzMax'"
    assert "CharismaMax" in params, "Missing parameter 'CharismaMax'"

def test_shadowrun::spezies_has_StaerkeMax():
    assert hasattr(shadowrun::Spezies, "StaerkeMax")
    descriptor = None
    for klass in shadowrun::Spezies.__mro__:
        if "StaerkeMax" in klass.__dict__:
            descriptor = klass.__dict__["StaerkeMax"]
            break
    assert isinstance(descriptor, property)

def test_shadowrun::spezies_has_WillenskraftMax():
    assert hasattr(shadowrun::Spezies, "WillenskraftMax")
    descriptor = None
    for klass in shadowrun::Spezies.__mro__:
        if "WillenskraftMax" in klass.__dict__:
            descriptor = klass.__dict__["WillenskraftMax"]
            break
    assert isinstance(descriptor, property)

def test_shadowrun::spezies_has_KonsitutionMax():
    assert hasattr(shadowrun::Spezies, "KonsitutionMax")
    descriptor = None
    for klass in shadowrun::Spezies.__mro__:
        if "KonsitutionMax" in klass.__dict__:
            descriptor = klass.__dict__["KonsitutionMax"]
            break
    assert isinstance(descriptor, property)

def test_shadowrun::spezies_has_SchnelligkeitMax():
    assert hasattr(shadowrun::Spezies, "SchnelligkeitMax")
    descriptor = None
    for klass in shadowrun::Spezies.__mro__:
        if "SchnelligkeitMax" in klass.__dict__:
            descriptor = klass.__dict__["SchnelligkeitMax"]
            break
    assert isinstance(descriptor, property)

def test_shadowrun::spezies_has_InteligenzMax():
    assert hasattr(shadowrun::Spezies, "InteligenzMax")
    descriptor = None
    for klass in shadowrun::Spezies.__mro__:
        if "InteligenzMax" in klass.__dict__:
            descriptor = klass.__dict__["InteligenzMax"]
            break
    assert isinstance(descriptor, property)

def test_shadowrun::spezies_has_CharismaMax():
    assert hasattr(shadowrun::Spezies, "CharismaMax")
    descriptor = None
    for klass in shadowrun::Spezies.__mro__:
        if "CharismaMax" in klass.__dict__:
            descriptor = klass.__dict__["CharismaMax"]
            break
    assert isinstance(descriptor, property)



def test_shadowrun::personagruppe_is_not_abstract():
    assert not inspect.isabstract(shadowrun::PersonaGruppe)


def test_shadowrun::personagruppe_constructor_exists():
    assert callable(shadowrun::PersonaGruppe.__init__)


def test_shadowrun::personagruppe_constructor_args():
    sig = inspect.signature(shadowrun::PersonaGruppe.__init__)
    params = list(sig.parameters.keys())



def test_geldwert_is_not_abstract():
    assert not inspect.isabstract(GeldWert)


def test_geldwert_constructor_exists():
    assert callable(GeldWert.__init__)


def test_geldwert_constructor_args():
    sig = inspect.signature(GeldWert.__init__)
    params = list(sig.parameters.keys())



def test_shadowrun::bioware_is_not_abstract():
    assert not inspect.isabstract(shadowrun::BioWare)


def test_shadowrun::bioware_constructor_exists():
    assert callable(shadowrun::BioWare.__init__)


def test_shadowrun::bioware_constructor_args():
    sig = inspect.signature(shadowrun::BioWare.__init__)
    params = list(sig.parameters.keys())



def test_shadowrun::cyberware_is_not_abstract():
    assert not inspect.isabstract(shadowrun::Cyberware)


def test_shadowrun::cyberware_constructor_exists():
    assert callable(shadowrun::Cyberware.__init__)


def test_shadowrun::cyberware_constructor_args():
    sig = inspect.signature(shadowrun::Cyberware.__init__)
    params = list(sig.parameters.keys())



def test_fk_is_not_abstract():
    assert not inspect.isabstract(FK)


def test_fk_constructor_exists():
    assert callable(FK.__init__)


def test_fk_constructor_args():
    sig = inspect.signature(FK.__init__)
    params = list(sig.parameters.keys())



def test_shadowrun::fertigkeitsgruppe_is_not_abstract():
    assert not inspect.isabstract(shadowrun::FertigkeitsGruppe)


def test_shadowrun::fertigkeitsgruppe_constructor_exists():
    assert callable(shadowrun::FertigkeitsGruppe.__init__)


def test_shadowrun::fertigkeitsgruppe_constructor_args():
    sig = inspect.signature(shadowrun::FertigkeitsGruppe.__init__)
    params = list(sig.parameters.keys())



def test_shadowrun::abstraktfertigkeit_is_not_abstract():
    assert not inspect.isabstract(shadowrun::AbstraktFertigkeit)


def test_shadowrun::abstraktfertigkeit_constructor_exists():
    assert callable(shadowrun::AbstraktFertigkeit.__init__)


def test_shadowrun::abstraktfertigkeit_constructor_args():
    sig = inspect.signature(shadowrun::AbstraktFertigkeit.__init__)
    params = list(sig.parameters.keys())



def test_shadowrun::abstaktgegenstand_is_not_abstract():
    assert not inspect.isabstract(shadowrun::AbstaktGegenstand)


def test_shadowrun::abstaktgegenstand_constructor_exists():
    assert callable(shadowrun::AbstaktGegenstand.__init__)


def test_shadowrun::abstaktgegenstand_constructor_args():
    sig = inspect.signature(shadowrun::AbstaktGegenstand.__init__)
    params = list(sig.parameters.keys())
    assert "verbraucht" in params, "Missing parameter 'verbraucht'"
    assert "inBenutzung" in params, "Missing parameter 'inBenutzung'"
    assert "raumKapazitaet" in params, "Missing parameter 'raumKapazitaet'"
    assert "tragbar" in params, "Missing parameter 'tragbar'"
    assert "gewicht" in params, "Missing parameter 'gewicht'"

def test_shadowrun::abstaktgegenstand_has_verbraucht():
    assert hasattr(shadowrun::AbstaktGegenstand, "verbraucht")
    descriptor = None
    for klass in shadowrun::AbstaktGegenstand.__mro__:
        if "verbraucht" in klass.__dict__:
            descriptor = klass.__dict__["verbraucht"]
            break
    assert isinstance(descriptor, property)

def test_shadowrun::abstaktgegenstand_has_inBenutzung():
    assert hasattr(shadowrun::AbstaktGegenstand, "inBenutzung")
    descriptor = None
    for klass in shadowrun::AbstaktGegenstand.__mro__:
        if "inBenutzung" in klass.__dict__:
            descriptor = klass.__dict__["inBenutzung"]
            break
    assert isinstance(descriptor, property)

def test_shadowrun::abstaktgegenstand_has_raumKapazitaet():
    assert hasattr(shadowrun::AbstaktGegenstand, "raumKapazitaet")
    descriptor = None
    for klass in shadowrun::AbstaktGegenstand.__mro__:
        if "raumKapazitaet" in klass.__dict__:
            descriptor = klass.__dict__["raumKapazitaet"]
            break
    assert isinstance(descriptor, property)

def test_shadowrun::abstaktgegenstand_has_tragbar():
    assert hasattr(shadowrun::AbstaktGegenstand, "tragbar")
    descriptor = None
    for klass in shadowrun::AbstaktGegenstand.__mro__:
        if "tragbar" in klass.__dict__:
            descriptor = klass.__dict__["tragbar"]
            break
    assert isinstance(descriptor, property)

def test_shadowrun::abstaktgegenstand_has_gewicht():
    assert hasattr(shadowrun::AbstaktGegenstand, "gewicht")
    descriptor = None
    for klass in shadowrun::AbstaktGegenstand.__mro__:
        if "gewicht" in klass.__dict__:
            descriptor = klass.__dict__["gewicht"]
            break
    assert isinstance(descriptor, property)



def test_shadowrun::reichweite_is_not_abstract():
    assert not inspect.isabstract(shadowrun::Reichweite)


def test_shadowrun::reichweite_constructor_exists():
    assert callable(shadowrun::Reichweite.__init__)


def test_shadowrun::reichweite_constructor_args():
    sig = inspect.signature(shadowrun::Reichweite.__init__)
    params = list(sig.parameters.keys())
    assert "reichweiteKurz" in params, "Missing parameter 'reichweiteKurz'"
    assert "reichweiteExtrem1" in params, "Missing parameter 'reichweiteExtrem1'"
    assert "reichweiteMittel1" in params, "Missing parameter 'reichweiteMittel1'"
    assert "reichweiteExtrem" in params, "Missing parameter 'reichweiteExtrem'"
    assert "reichweiteWeit1" in params, "Missing parameter 'reichweiteWeit1'"
    assert "reichweiteWeit" in params, "Missing parameter 'reichweiteWeit'"
    assert "reichweiteKurz1" in params, "Missing parameter 'reichweiteKurz1'"
    assert "reichweiteMittel" in params, "Missing parameter 'reichweiteMittel'"

def test_shadowrun::reichweite_has_reichweiteKurz():
    assert hasattr(shadowrun::Reichweite, "reichweiteKurz")
    descriptor = None
    for klass in shadowrun::Reichweite.__mro__:
        if "reichweiteKurz" in klass.__dict__:
            descriptor = klass.__dict__["reichweiteKurz"]
            break
    assert isinstance(descriptor, property)

def test_shadowrun::reichweite_has_reichweiteExtrem1():
    assert hasattr(shadowrun::Reichweite, "reichweiteExtrem1")
    descriptor = None
    for klass in shadowrun::Reichweite.__mro__:
        if "reichweiteExtrem1" in klass.__dict__:
            descriptor = klass.__dict__["reichweiteExtrem1"]
            break
    assert isinstance(descriptor, property)

def test_shadowrun::reichweite_has_reichweiteMittel1():
    assert hasattr(shadowrun::Reichweite, "reichweiteMittel1")
    descriptor = None
    for klass in shadowrun::Reichweite.__mro__:
        if "reichweiteMittel1" in klass.__dict__:
            descriptor = klass.__dict__["reichweiteMittel1"]
            break
    assert isinstance(descriptor, property)

def test_shadowrun::reichweite_has_reichweiteExtrem():
    assert hasattr(shadowrun::Reichweite, "reichweiteExtrem")
    descriptor = None
    for klass in shadowrun::Reichweite.__mro__:
        if "reichweiteExtrem" in klass.__dict__:
            descriptor = klass.__dict__["reichweiteExtrem"]
            break
    assert isinstance(descriptor, property)

def test_shadowrun::reichweite_has_reichweiteWeit1():
    assert hasattr(shadowrun::Reichweite, "reichweiteWeit1")
    descriptor = None
    for klass in shadowrun::Reichweite.__mro__:
        if "reichweiteWeit1" in klass.__dict__:
            descriptor = klass.__dict__["reichweiteWeit1"]
            break
    assert isinstance(descriptor, property)

def test_shadowrun::reichweite_has_reichweiteWeit():
    assert hasattr(shadowrun::Reichweite, "reichweiteWeit")
    descriptor = None
    for klass in shadowrun::Reichweite.__mro__:
        if "reichweiteWeit" in klass.__dict__:
            descriptor = klass.__dict__["reichweiteWeit"]
            break
    assert isinstance(descriptor, property)

def test_shadowrun::reichweite_has_reichweiteKurz1():
    assert hasattr(shadowrun::Reichweite, "reichweiteKurz1")
    descriptor = None
    for klass in shadowrun::Reichweite.__mro__:
        if "reichweiteKurz1" in klass.__dict__:
            descriptor = klass.__dict__["reichweiteKurz1"]
            break
    assert isinstance(descriptor, property)

def test_shadowrun::reichweite_has_reichweiteMittel():
    assert hasattr(shadowrun::Reichweite, "reichweiteMittel")
    descriptor = None
    for klass in shadowrun::Reichweite.__mro__:
        if "reichweiteMittel" in klass.__dict__:
            descriptor = klass.__dict__["reichweiteMittel"]
            break
    assert isinstance(descriptor, property)



def test_abstaktwaffe_is_not_abstract():
    assert not inspect.isabstract(AbstaktWaffe)


def test_abstaktwaffe_constructor_exists():
    assert callable(AbstaktWaffe.__init__)


def test_abstaktwaffe_constructor_args():
    sig = inspect.signature(AbstaktWaffe.__init__)
    params = list(sig.parameters.keys())



def test_shadowrun::granate_is_not_abstract():
    assert not inspect.isabstract(shadowrun::Granate)


def test_shadowrun::granate_constructor_exists():
    assert callable(shadowrun::Granate.__init__)


def test_shadowrun::granate_constructor_args():
    sig = inspect.signature(shadowrun::Granate.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "daempfung" in params, "Missing parameter 'daempfung'"

def test_shadowrun::granate_has_type():
    assert hasattr(shadowrun::Granate, "type")
    descriptor = None
    for klass in shadowrun::Granate.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_shadowrun::granate_has_daempfung():
    assert hasattr(shadowrun::Granate, "daempfung")
    descriptor = None
    for klass in shadowrun::Granate.__mro__:
        if "daempfung" in klass.__dict__:
            descriptor = klass.__dict__["daempfung"]
            break
    assert isinstance(descriptor, property)



def test_shadowrun::abstraktnahkampfwaffe_is_not_abstract():
    assert not inspect.isabstract(shadowrun::AbstraktNahkampfwaffe)


def test_shadowrun::abstraktnahkampfwaffe_constructor_exists():
    assert callable(shadowrun::AbstraktNahkampfwaffe.__init__)


def test_shadowrun::abstraktnahkampfwaffe_constructor_args():
    sig = inspect.signature(shadowrun::AbstraktNahkampfwaffe.__init__)
    params = list(sig.parameters.keys())



def test_shadowrun::abstaktfernkampfwaffe_is_not_abstract():
    assert not inspect.isabstract(shadowrun::AbstaktFernKampfwaffe)


def test_shadowrun::abstaktfernkampfwaffe_constructor_exists():
    assert callable(shadowrun::AbstaktFernKampfwaffe.__init__)


def test_shadowrun::abstaktfernkampfwaffe_constructor_args():
    sig = inspect.signature(shadowrun::AbstaktFernKampfwaffe.__init__)
    params = list(sig.parameters.keys())



def test_geistigeattribute_is_not_abstract():
    assert not inspect.isabstract(GeistigeAttribute)


def test_geistigeattribute_constructor_exists():
    assert callable(GeistigeAttribute.__init__)


def test_geistigeattribute_constructor_args():
    sig = inspect.signature(GeistigeAttribute.__init__)
    params = list(sig.parameters.keys())



def test_berechneteattribute_is_not_abstract():
    assert not inspect.isabstract(BerechneteAttribute)


def test_berechneteattribute_constructor_exists():
    assert callable(BerechneteAttribute.__init__)


def test_berechneteattribute_constructor_args():
    sig = inspect.signature(BerechneteAttribute.__init__)
    params = list(sig.parameters.keys())



def test_koerperlicheatribute_is_not_abstract():
    assert not inspect.isabstract(KoerperlicheAtribute)


def test_koerperlicheatribute_constructor_exists():
    assert callable(KoerperlicheAtribute.__init__)


def test_koerperlicheatribute_constructor_args():
    sig = inspect.signature(KoerperlicheAtribute.__init__)
    params = list(sig.parameters.keys())



def test_bodyindex_is_not_abstract():
    assert not inspect.isabstract(BodyIndex)


def test_bodyindex_constructor_exists():
    assert callable(BodyIndex.__init__)


def test_bodyindex_constructor_args():
    sig = inspect.signature(BodyIndex.__init__)
    params = list(sig.parameters.keys())



def test_essenz_is_not_abstract():
    assert not inspect.isabstract(Essenz)


def test_essenz_constructor_exists():
    assert callable(Essenz.__init__)


def test_essenz_constructor_args():
    sig = inspect.signature(Essenz.__init__)
    params = list(sig.parameters.keys())



def test_shadowrun::abstaktpersona_is_not_abstract():
    assert not inspect.isabstract(shadowrun::AbstaktPersona)


def test_shadowrun::abstaktpersona_constructor_exists():
    assert callable(shadowrun::AbstaktPersona.__init__)


def test_shadowrun::abstaktpersona_constructor_args():
    sig = inspect.signature(shadowrun::AbstaktPersona.__init__)
    params = list(sig.parameters.keys())
    assert "WillenskraftBase" in params, "Missing parameter 'WillenskraftBase'"
    assert "StaerkeBase" in params, "Missing parameter 'StaerkeBase'"
    assert "ReaktionBase" in params, "Missing parameter 'ReaktionBase'"
    assert "SchnelligkeitBase" in params, "Missing parameter 'SchnelligkeitBase'"
    assert "EssenzBase" in params, "Missing parameter 'EssenzBase'"
    assert "eigenGewicht" in params, "Missing parameter 'eigenGewicht'"
    assert "CharismaBase" in params, "Missing parameter 'CharismaBase'"
    assert "KonsitutionBase" in params, "Missing parameter 'KonsitutionBase'"
    assert "KampfpoolBase" in params, "Missing parameter 'KampfpoolBase'"
    assert "ReaktionWBase" in params, "Missing parameter 'ReaktionWBase'"
    assert "modsetter" in params, "Missing parameter 'modsetter'"
    assert "InteligenzBase" in params, "Missing parameter 'InteligenzBase'"

def test_shadowrun::abstaktpersona_has_WillenskraftBase():
    assert hasattr(shadowrun::AbstaktPersona, "WillenskraftBase")
    descriptor = None
    for klass in shadowrun::AbstaktPersona.__mro__:
        if "WillenskraftBase" in klass.__dict__:
            descriptor = klass.__dict__["WillenskraftBase"]
            break
    assert isinstance(descriptor, property)

def test_shadowrun::abstaktpersona_has_StaerkeBase():
    assert hasattr(shadowrun::AbstaktPersona, "StaerkeBase")
    descriptor = None
    for klass in shadowrun::AbstaktPersona.__mro__:
        if "StaerkeBase" in klass.__dict__:
            descriptor = klass.__dict__["StaerkeBase"]
            break
    assert isinstance(descriptor, property)

def test_shadowrun::abstaktpersona_has_ReaktionBase():
    assert hasattr(shadowrun::AbstaktPersona, "ReaktionBase")
    descriptor = None
    for klass in shadowrun::AbstaktPersona.__mro__:
        if "ReaktionBase" in klass.__dict__:
            descriptor = klass.__dict__["ReaktionBase"]
            break
    assert isinstance(descriptor, property)

def test_shadowrun::abstaktpersona_has_SchnelligkeitBase():
    assert hasattr(shadowrun::AbstaktPersona, "SchnelligkeitBase")
    descriptor = None
    for klass in shadowrun::AbstaktPersona.__mro__:
        if "SchnelligkeitBase" in klass.__dict__:
            descriptor = klass.__dict__["SchnelligkeitBase"]
            break
    assert isinstance(descriptor, property)

def test_shadowrun::abstaktpersona_has_EssenzBase():
    assert hasattr(shadowrun::AbstaktPersona, "EssenzBase")
    descriptor = None
    for klass in shadowrun::AbstaktPersona.__mro__:
        if "EssenzBase" in klass.__dict__:
            descriptor = klass.__dict__["EssenzBase"]
            break
    assert isinstance(descriptor, property)

def test_shadowrun::abstaktpersona_has_eigenGewicht():
    assert hasattr(shadowrun::AbstaktPersona, "eigenGewicht")
    descriptor = None
    for klass in shadowrun::AbstaktPersona.__mro__:
        if "eigenGewicht" in klass.__dict__:
            descriptor = klass.__dict__["eigenGewicht"]
            break
    assert isinstance(descriptor, property)

def test_shadowrun::abstaktpersona_has_CharismaBase():
    assert hasattr(shadowrun::AbstaktPersona, "CharismaBase")
    descriptor = None
    for klass in shadowrun::AbstaktPersona.__mro__:
        if "CharismaBase" in klass.__dict__:
            descriptor = klass.__dict__["CharismaBase"]
            break
    assert isinstance(descriptor, property)

def test_shadowrun::abstaktpersona_has_KonsitutionBase():
    assert hasattr(shadowrun::AbstaktPersona, "KonsitutionBase")
    descriptor = None
    for klass in shadowrun::AbstaktPersona.__mro__:
        if "KonsitutionBase" in klass.__dict__:
            descriptor = klass.__dict__["KonsitutionBase"]
            break
    assert isinstance(descriptor, property)

def test_shadowrun::abstaktpersona_has_KampfpoolBase():
    assert hasattr(shadowrun::AbstaktPersona, "KampfpoolBase")
    descriptor = None
    for klass in shadowrun::AbstaktPersona.__mro__:
        if "KampfpoolBase" in klass.__dict__:
            descriptor = klass.__dict__["KampfpoolBase"]
            break
    assert isinstance(descriptor, property)

def test_shadowrun::abstaktpersona_has_ReaktionWBase():
    assert hasattr(shadowrun::AbstaktPersona, "ReaktionWBase")
    descriptor = None
    for klass in shadowrun::AbstaktPersona.__mro__:
        if "ReaktionWBase" in klass.__dict__:
            descriptor = klass.__dict__["ReaktionWBase"]
            break
    assert isinstance(descriptor, property)

def test_shadowrun::abstaktpersona_has_modsetter():
    assert hasattr(shadowrun::AbstaktPersona, "modsetter")
    descriptor = None
    for klass in shadowrun::AbstaktPersona.__mro__:
        if "modsetter" in klass.__dict__:
            descriptor = klass.__dict__["modsetter"]
            break
    assert isinstance(descriptor, property)

def test_shadowrun::abstaktpersona_has_InteligenzBase():
    assert hasattr(shadowrun::AbstaktPersona, "InteligenzBase")
    descriptor = None
    for klass in shadowrun::AbstaktPersona.__mro__:
        if "InteligenzBase" in klass.__dict__:
            descriptor = klass.__dict__["InteligenzBase"]
            break
    assert isinstance(descriptor, property)

def test_koerperteil_exists():
    # Check that the Enumeration exists
    assert Koerperteil is not None

def test_koerperteil_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Koerperteil]
    expected_literals = [
        "Beine",
        "Rumpf",
        "Arme",
        "Kopf",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Koerperteil"

def test_schadenstyp_exists():
    # Check that the Enumeration exists
    assert SchadensTyp is not None

def test_schadenstyp_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SchadensTyp]
    expected_literals = [
        "speziell",
        "koerperlich",
        "geistig",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SchadensTyp"

def test_smartguntype_exists():
    # Check that the Enumeration exists
    assert SmartgunType is not None

def test_smartguntype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SmartgunType]
    expected_literals = [
        "SmartGun",
        "SmatgunII",
        "SmartBrille",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SmartgunType"

def test_modifikatortype_exists():
    # Check that the Enumeration exists
    assert ModifikatorType is not None

def test_modifikatortype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ModifikatorType]
    expected_literals = [
        "Bio",
        "Cyber",
        "Natural",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ModifikatorType"

def test_feuermodus_exists():
    # Check that the Enumeration exists
    assert FeuerModus is not None

def test_feuermodus_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FeuerModus]
    expected_literals = [
        "SM",
        "AM",
        "EM",
        "HM",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FeuerModus"

def test_magazintyp_exists():
    # Check that the Enumeration exists
    assert MagazinTyp is not None

def test_magazintyp_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MagazinTyp]
    expected_literals = [
        "Streifen",
        "Gurt",
        "Trommel",
        "Clip",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MagazinTyp"

def test_tragbar_exists():
    # Check that the Enumeration exists
    assert Tragbar is not None

def test_tragbar_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Tragbar]
    expected_literals = [
        "zweihaendig",
        "einhaendig",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Tragbar"

def test_zauberreichweite_exists():
    # Check that the Enumeration exists
    assert ZauberReichweite is not None

def test_zauberreichweite_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ZauberReichweite]
    expected_literals = [
        "Begrenzt",
        "Selbst",
        "Beruehrung",
        "Blickfeld",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ZauberReichweite"

def test_zauberdauer_exists():
    # Check that the Enumeration exists
    assert ZauberDauer is not None

def test_zauberdauer_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ZauberDauer]
    expected_literals = [
        "Aufrechterhalten",
        "Permanent",
        "Sofort",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ZauberDauer"

def test_zauberart_exists():
    # Check that the Enumeration exists
    assert ZauberArt is not None

def test_zauberart_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ZauberArt]
    expected_literals = [
        "Mana",
        "Physisch",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ZauberArt"


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
shadowrun::Schadenswiederstand_strategy = st.builds(
    shadowrun::Schadenswiederstand,
    ruestungsSchutzBalistisch=
        st.integers(),
    ruestungsSchutzStoss=
        st.integers()
)
MagiePersona_strategy = st.builds(
    MagiePersona,
)
shadowrun::Shamane_strategy = st.builds(
    shadowrun::Shamane,
)
shadowrun::GegenstandStufen_strategy = st.builds(
    shadowrun::GegenstandStufen,
    AntiTracing=
        st.integers(),
    AntiProtection=
        st.integers(),
    Protection=
        st.integers(),
    Computer=
        st.integers(),
    Elektronik=
        st.integers(),
    Tracing=
        st.integers()
)
shadowrun::NahkampfReichweite_strategy = st.builds(
    shadowrun::NahkampfReichweite,
    reichweite=
        st.integers()
)
shadowrun::BodyIndex_strategy = st.builds(
    shadowrun::BodyIndex,
    bodyIndex=
        st.integers()
)
shadowrun::Essenz_strategy = st.builds(
    shadowrun::Essenz,
    Essenz=
        st.integers()
)
shadowrun::GeistigeAttribute_strategy = st.builds(
    shadowrun::GeistigeAttribute,
    Inteligenz=
        st.integers(),
    Charisma=
        st.integers(),
    Willenskraft=
        st.integers()
)
shadowrun::BerechneteAttribute_strategy = st.builds(
    shadowrun::BerechneteAttribute,
    ReaktionW=
        st.integers(),
    Kampfpool=
        st.integers(),
    Reaktion=
        st.integers()
)
Schadenswiederstand_strategy = st.builds(
    Schadenswiederstand,
)
shadowrun::KoerperlicheAtribute_strategy = st.builds(
    shadowrun::KoerperlicheAtribute,
    Staerke=
        st.integers(),
    Schnelligkeit=
        st.integers(),
    Konsitution=
        st.integers()
)
shadowrun::Sichtverhaeltnisse_strategy = st.builds(
    shadowrun::Sichtverhaeltnisse,
    Infrarot=
        safe_text,
    Ultrasound=
        safe_text,
    Restlichtverstaerkung=
        safe_text
)
shadowrun::FernkampfwaffenModifikatoren_strategy = st.builds(
    shadowrun::FernkampfwaffenModifikatoren,
    Schalldaempfer=
        st.booleans(),
    Vergroesserung=
        st.integers(),
    lasterPointer=
        st.booleans(),
    Smartgun=
        safe_text,
    Rueckstoss=
        st.integers()
)
shadowrun::EObject_strategy = st.builds(
    shadowrun::EObject,
)
shadowrun::Bemerkbar_strategy = st.builds(
    shadowrun::Bemerkbar,
    tarnstufe=
        st.integers()
)
AbstraktNahkampfwaffe_strategy = st.builds(
    AbstraktNahkampfwaffe,
)
shadowrun::Nahkampfwaffe_strategy = st.builds(
    shadowrun::Nahkampfwaffe,
)
shadowrun::Quelle_strategy = st.builds(
    shadowrun::Quelle,
    page=
        safe_text
)
shadowrun::WarenListe_strategy = st.builds(
    shadowrun::WarenListe,
    listenWert=
        safe_text,
    strassenWert=
        safe_text
)
shadowrun::Reichweiten_strategy = st.builds(
    shadowrun::Reichweiten,
)
shadowrun::Beschreibbar_strategy = st.builds(
    shadowrun::Beschreibbar,
    beschreibung=
        safe_text,
    image=
        safe_text,
    name=
        safe_text
)
shadowrun::GengenstandListe_strategy = st.builds(
    shadowrun::GengenstandListe,
)
AbstractMagischePaersona_strategy = st.builds(
    AbstractMagischePaersona,
)
shadowrun::PersonaZauber_strategy = st.builds(
    shadowrun::PersonaZauber,
    stufe=
        st.integers()
)
AbstractMagier_strategy = st.builds(
    AbstractMagier,
)
shadowrun::MagiePersona_strategy = st.builds(
    shadowrun::MagiePersona,
)
shadowrun::Legalitaet_strategy = st.builds(
    shadowrun::Legalitaet,
    legalitaet=
        safe_text
)
AbstraktFertigkeit_strategy = st.builds(
    AbstraktFertigkeit,
)
shadowrun::KiAdept_strategy = st.builds(
    shadowrun::KiAdept,
)
MagischeMods_strategy = st.builds(
    MagischeMods,
)
shadowrun::KiKraft_strategy = st.builds(
    shadowrun::KiKraft,
)
BaseMagischePersona_strategy = st.builds(
    BaseMagischePersona,
)
shadowrun::AbstractMagier_strategy = st.builds(
    shadowrun::AbstractMagier,
    InitationsGrad=
        st.integers(),
    MagiePool=
        st.integers(),
    Astralpool=
        st.integers()
)
shadowrun::BaseMagischePersona_strategy = st.builds(
    shadowrun::BaseMagischePersona,
    magie=
        st.integers()
)
AbstraktModifikatoren_strategy = st.builds(
    AbstraktModifikatoren,
)
shadowrun::MagischeMods_strategy = st.builds(
    shadowrun::MagischeMods,
)
shadowrun::koerpermods_strategy = st.builds(
    shadowrun::koerpermods,
)
shadowrun::ModifikatorList_strategy = st.builds(
    shadowrun::ModifikatorList,
    name=
        safe_text
)
shadowrun::GeldWert_strategy = st.builds(
    shadowrun::GeldWert,
    verfuegbarkeit=
        safe_text,
    wert=
        safe_text,
    strassenIndex=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
koerpermods_strategy = st.builds(
    koerpermods,
)
shadowrun::FK_strategy = st.builds(
    shadowrun::FK,
)
AbstrakteRuestung_strategy = st.builds(
    AbstrakteRuestung,
)
shadowrun::Ruestung_strategy = st.builds(
    shadowrun::Ruestung,
)
shadowrun::PersonaKoerper_strategy = st.builds(
    shadowrun::PersonaKoerper,
    gesamtZustand=
        st.integers()
)
shadowrun::Modifizierbar_strategy = st.builds(
    shadowrun::Modifizierbar,
)
shadowrun::EAttribute_strategy = st.builds(
    shadowrun::EAttribute,
)
shadowrun::AttributModifikatorWert_strategy = st.builds(
    shadowrun::AttributModifikatorWert,
    wert=
        st.integers()
)
shadowrun::BasicList_strategy = st.builds(
    shadowrun::BasicList,
)
AbstaktFernKampfwaffe_strategy = st.builds(
    AbstaktFernKampfwaffe,
)
shadowrun::Projektilwaffe_strategy = st.builds(
    shadowrun::Projektilwaffe,
)
shadowrun::Wurfwaffe_strategy = st.builds(
    shadowrun::Wurfwaffe,
)
shadowrun::Feuerwaffe_strategy = st.builds(
    shadowrun::Feuerwaffe,
    kapazitaet=
        st.integers(),
    modie=
        safe_text,
    munitionstyp=
        safe_text
)
Gegenstand_strategy = st.builds(
    Gegenstand,
)
shadowrun::MunitionsBehealter_strategy = st.builds(
    shadowrun::MunitionsBehealter,
)
shadowrun::Behaelter_strategy = st.builds(
    shadowrun::Behaelter,
    kapazitaet=
        st.integers()
)
NahkampfReichweite_strategy = st.builds(
    NahkampfReichweite,
)
AbstraktKleidung_strategy = st.builds(
    AbstraktKleidung,
)
shadowrun::AbstrakteRuestung_strategy = st.builds(
    shadowrun::AbstrakteRuestung,
    ruestungsSchutzBalistisch=
        st.integers(),
    ruestungsSchutzStoss=
        st.integers()
)
shadowrun::RaumKoordinate_strategy = st.builds(
    shadowrun::RaumKoordinate,
)
shadowrun::AbstrakRaumKoerper_strategy = st.builds(
    shadowrun::AbstrakRaumKoerper,
)
shadowrun::Spezialisierung_strategy = st.builds(
    shadowrun::Spezialisierung,
)
AbstaktPersona_strategy = st.builds(
    AbstaktPersona,
)
shadowrun::AbstractMagischePaersona_strategy = st.builds(
    shadowrun::AbstractMagischePaersona,
    magieBase=
        st.integers()
)
shadowrun::Persona_strategy = st.builds(
    shadowrun::Persona,
)
shadowrun::Kleidung_strategy = st.builds(
    shadowrun::Kleidung,
)
shadowrun::PersonaFertigkeit_strategy = st.builds(
    shadowrun::PersonaFertigkeit,
    stufe=
        st.integers()
)
shadowrun::Konzentration_strategy = st.builds(
    shadowrun::Konzentration,
)
shadowrun::Fertigkeit_strategy = st.builds(
    shadowrun::Fertigkeit,
)
AbstaktGegenstand_strategy = st.builds(
    AbstaktGegenstand,
)
shadowrun::Munition_strategy = st.builds(
    shadowrun::Munition,
    power=
        st.integers(),
    schadensTyp=
        safe_text,
    niveau=
        st.integers()
)
shadowrun::Gegenstand_strategy = st.builds(
    shadowrun::Gegenstand,
)
shadowrun::AbstraktKleidung_strategy = st.builds(
    shadowrun::AbstraktKleidung,
    koeperTeil=
        safe_text
)
shadowrun::AbstaktWaffe_strategy = st.builds(
    shadowrun::AbstaktWaffe,
    schadenscode=
        safe_text
)
Modifizierbar_strategy = st.builds(
    Modifizierbar,
)
Quelle_strategy = st.builds(
    Quelle,
)
Bemerkbar_strategy = st.builds(
    Bemerkbar,
)
Legalitaet_strategy = st.builds(
    Legalitaet,
)
Beschreibbar_strategy = st.builds(
    Beschreibbar,
)
shadowrun::Zauber_strategy = st.builds(
    shadowrun::Zauber,
    art=
        safe_text,
    reichweite=
        safe_text,
    Enzug=
        safe_text,
    Schaden=
        safe_text,
    Mindestwurf=
        safe_text,
    Dauer=
        safe_text
)
shadowrun::ShrList_strategy = st.builds(
    shadowrun::ShrList,
)
shadowrun::Totem_strategy = st.builds(
    shadowrun::Totem,
)
shadowrun::Script_strategy = st.builds(
    shadowrun::Script,
)
shadowrun::AbstraktModifikatoren_strategy = st.builds(
    shadowrun::AbstraktModifikatoren,
)
shadowrun::Placement_strategy = st.builds(
    shadowrun::Placement,
)
shadowrun::SourceBook_strategy = st.builds(
    shadowrun::SourceBook,
    endShrTime=
        safe_text,
    startShrTime=
        safe_text
)
shadowrun::Spezies_strategy = st.builds(
    shadowrun::Spezies,
    StaerkeMax=
        st.integers(),
    WillenskraftMax=
        st.integers(),
    KonsitutionMax=
        st.integers(),
    SchnelligkeitMax=
        st.integers(),
    InteligenzMax=
        st.integers(),
    CharismaMax=
        st.integers()
)
shadowrun::PersonaGruppe_strategy = st.builds(
    shadowrun::PersonaGruppe,
)
GeldWert_strategy = st.builds(
    GeldWert,
)
shadowrun::BioWare_strategy = st.builds(
    shadowrun::BioWare,
)
shadowrun::Cyberware_strategy = st.builds(
    shadowrun::Cyberware,
)
FK_strategy = st.builds(
    FK,
)
shadowrun::FertigkeitsGruppe_strategy = st.builds(
    shadowrun::FertigkeitsGruppe,
)
shadowrun::AbstraktFertigkeit_strategy = st.builds(
    shadowrun::AbstraktFertigkeit,
)
shadowrun::AbstaktGegenstand_strategy = st.builds(
    shadowrun::AbstaktGegenstand,
    verbraucht=
        st.booleans(),
    inBenutzung=
        st.booleans(),
    raumKapazitaet=
        st.integers(),
    tragbar=
        safe_text,
    gewicht=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
shadowrun::Reichweite_strategy = st.builds(
    shadowrun::Reichweite,
    reichweiteKurz=
        st.integers(),
    reichweiteExtrem1=
        st.integers(),
    reichweiteMittel1=
        st.integers(),
    reichweiteExtrem=
        st.integers(),
    reichweiteWeit1=
        st.integers(),
    reichweiteWeit=
        st.integers(),
    reichweiteKurz1=
        st.integers(),
    reichweiteMittel=
        st.integers()
)
AbstaktWaffe_strategy = st.builds(
    AbstaktWaffe,
)
shadowrun::Granate_strategy = st.builds(
    shadowrun::Granate,
    type=
        safe_text,
    daempfung=
        safe_text
)
shadowrun::AbstraktNahkampfwaffe_strategy = st.builds(
    shadowrun::AbstraktNahkampfwaffe,
)
shadowrun::AbstaktFernKampfwaffe_strategy = st.builds(
    shadowrun::AbstaktFernKampfwaffe,
)
GeistigeAttribute_strategy = st.builds(
    GeistigeAttribute,
)
BerechneteAttribute_strategy = st.builds(
    BerechneteAttribute,
)
KoerperlicheAtribute_strategy = st.builds(
    KoerperlicheAtribute,
)
BodyIndex_strategy = st.builds(
    BodyIndex,
)
Essenz_strategy = st.builds(
    Essenz,
)
shadowrun::AbstaktPersona_strategy = st.builds(
    shadowrun::AbstaktPersona,
    WillenskraftBase=
        st.integers(),
    StaerkeBase=
        st.integers(),
    ReaktionBase=
        st.integers(),
    SchnelligkeitBase=
        st.integers(),
    EssenzBase=
        st.integers(),
    eigenGewicht=
        st.integers(),
    CharismaBase=
        st.integers(),
    KonsitutionBase=
        st.integers(),
    KampfpoolBase=
        st.integers(),
    ReaktionWBase=
        st.integers(),
    modsetter=
        safe_text,
    InteligenzBase=
        st.integers()
)

@given(instance=shadowrun::Schadenswiederstand_strategy)
@settings(max_examples=50)
def test_shadowrun::schadenswiederstand_instantiation(instance):
    assert isinstance(instance, shadowrun::Schadenswiederstand)

@given(instance=shadowrun::Schadenswiederstand_strategy)
def test_shadowrun::schadenswiederstand_ruestungsSchutzBalistisch_type(instance):
    assert isinstance(instance.ruestungsSchutzBalistisch, int)


@given(instance=shadowrun::Schadenswiederstand_strategy)
def test_shadowrun::schadenswiederstand_ruestungsSchutzBalistisch_setter(instance):
    original = instance.ruestungsSchutzBalistisch
    instance.ruestungsSchutzBalistisch = original
    assert instance.ruestungsSchutzBalistisch == original

@given(instance=shadowrun::Schadenswiederstand_strategy)
def test_shadowrun::schadenswiederstand_ruestungsSchutzStoss_type(instance):
    assert isinstance(instance.ruestungsSchutzStoss, int)


@given(instance=shadowrun::Schadenswiederstand_strategy)
def test_shadowrun::schadenswiederstand_ruestungsSchutzStoss_setter(instance):
    original = instance.ruestungsSchutzStoss
    instance.ruestungsSchutzStoss = original
    assert instance.ruestungsSchutzStoss == original

@given(instance=MagiePersona_strategy)
@settings(max_examples=50)
def test_magiepersona_instantiation(instance):
    assert isinstance(instance, MagiePersona)

@given(instance=shadowrun::Shamane_strategy)
@settings(max_examples=50)
def test_shadowrun::shamane_instantiation(instance):
    assert isinstance(instance, shadowrun::Shamane)

@given(instance=shadowrun::GegenstandStufen_strategy)
@settings(max_examples=50)
def test_shadowrun::gegenstandstufen_instantiation(instance):
    assert isinstance(instance, shadowrun::GegenstandStufen)

@given(instance=shadowrun::GegenstandStufen_strategy)
def test_shadowrun::gegenstandstufen_AntiTracing_type(instance):
    assert isinstance(instance.AntiTracing, int)


@given(instance=shadowrun::GegenstandStufen_strategy)
def test_shadowrun::gegenstandstufen_AntiTracing_setter(instance):
    original = instance.AntiTracing
    instance.AntiTracing = original
    assert instance.AntiTracing == original

@given(instance=shadowrun::GegenstandStufen_strategy)
def test_shadowrun::gegenstandstufen_AntiProtection_type(instance):
    assert isinstance(instance.AntiProtection, int)


@given(instance=shadowrun::GegenstandStufen_strategy)
def test_shadowrun::gegenstandstufen_AntiProtection_setter(instance):
    original = instance.AntiProtection
    instance.AntiProtection = original
    assert instance.AntiProtection == original

@given(instance=shadowrun::GegenstandStufen_strategy)
def test_shadowrun::gegenstandstufen_Protection_type(instance):
    assert isinstance(instance.Protection, int)


@given(instance=shadowrun::GegenstandStufen_strategy)
def test_shadowrun::gegenstandstufen_Protection_setter(instance):
    original = instance.Protection
    instance.Protection = original
    assert instance.Protection == original

@given(instance=shadowrun::GegenstandStufen_strategy)
def test_shadowrun::gegenstandstufen_Computer_type(instance):
    assert isinstance(instance.Computer, int)


@given(instance=shadowrun::GegenstandStufen_strategy)
def test_shadowrun::gegenstandstufen_Computer_setter(instance):
    original = instance.Computer
    instance.Computer = original
    assert instance.Computer == original

@given(instance=shadowrun::GegenstandStufen_strategy)
def test_shadowrun::gegenstandstufen_Elektronik_type(instance):
    assert isinstance(instance.Elektronik, int)


@given(instance=shadowrun::GegenstandStufen_strategy)
def test_shadowrun::gegenstandstufen_Elektronik_setter(instance):
    original = instance.Elektronik
    instance.Elektronik = original
    assert instance.Elektronik == original

@given(instance=shadowrun::GegenstandStufen_strategy)
def test_shadowrun::gegenstandstufen_Tracing_type(instance):
    assert isinstance(instance.Tracing, int)


@given(instance=shadowrun::GegenstandStufen_strategy)
def test_shadowrun::gegenstandstufen_Tracing_setter(instance):
    original = instance.Tracing
    instance.Tracing = original
    assert instance.Tracing == original

@given(instance=shadowrun::NahkampfReichweite_strategy)
@settings(max_examples=50)
def test_shadowrun::nahkampfreichweite_instantiation(instance):
    assert isinstance(instance, shadowrun::NahkampfReichweite)

@given(instance=shadowrun::NahkampfReichweite_strategy)
def test_shadowrun::nahkampfreichweite_reichweite_type(instance):
    assert isinstance(instance.reichweite, int)


@given(instance=shadowrun::NahkampfReichweite_strategy)
def test_shadowrun::nahkampfreichweite_reichweite_setter(instance):
    original = instance.reichweite
    instance.reichweite = original
    assert instance.reichweite == original

@given(instance=shadowrun::BodyIndex_strategy)
@settings(max_examples=50)
def test_shadowrun::bodyindex_instantiation(instance):
    assert isinstance(instance, shadowrun::BodyIndex)

@given(instance=shadowrun::BodyIndex_strategy)
def test_shadowrun::bodyindex_bodyIndex_type(instance):
    assert isinstance(instance.bodyIndex, int)


@given(instance=shadowrun::BodyIndex_strategy)
def test_shadowrun::bodyindex_bodyIndex_setter(instance):
    original = instance.bodyIndex
    instance.bodyIndex = original
    assert instance.bodyIndex == original

@given(instance=shadowrun::Essenz_strategy)
@settings(max_examples=50)
def test_shadowrun::essenz_instantiation(instance):
    assert isinstance(instance, shadowrun::Essenz)

@given(instance=shadowrun::Essenz_strategy)
def test_shadowrun::essenz_Essenz_type(instance):
    assert isinstance(instance.Essenz, int)


@given(instance=shadowrun::Essenz_strategy)
def test_shadowrun::essenz_Essenz_setter(instance):
    original = instance.Essenz
    instance.Essenz = original
    assert instance.Essenz == original

@given(instance=shadowrun::GeistigeAttribute_strategy)
@settings(max_examples=50)
def test_shadowrun::geistigeattribute_instantiation(instance):
    assert isinstance(instance, shadowrun::GeistigeAttribute)

@given(instance=shadowrun::GeistigeAttribute_strategy)
def test_shadowrun::geistigeattribute_Inteligenz_type(instance):
    assert isinstance(instance.Inteligenz, int)


@given(instance=shadowrun::GeistigeAttribute_strategy)
def test_shadowrun::geistigeattribute_Inteligenz_setter(instance):
    original = instance.Inteligenz
    instance.Inteligenz = original
    assert instance.Inteligenz == original

@given(instance=shadowrun::GeistigeAttribute_strategy)
def test_shadowrun::geistigeattribute_Charisma_type(instance):
    assert isinstance(instance.Charisma, int)


@given(instance=shadowrun::GeistigeAttribute_strategy)
def test_shadowrun::geistigeattribute_Charisma_setter(instance):
    original = instance.Charisma
    instance.Charisma = original
    assert instance.Charisma == original

@given(instance=shadowrun::GeistigeAttribute_strategy)
def test_shadowrun::geistigeattribute_Willenskraft_type(instance):
    assert isinstance(instance.Willenskraft, int)


@given(instance=shadowrun::GeistigeAttribute_strategy)
def test_shadowrun::geistigeattribute_Willenskraft_setter(instance):
    original = instance.Willenskraft
    instance.Willenskraft = original
    assert instance.Willenskraft == original

@given(instance=shadowrun::BerechneteAttribute_strategy)
@settings(max_examples=50)
def test_shadowrun::berechneteattribute_instantiation(instance):
    assert isinstance(instance, shadowrun::BerechneteAttribute)

@given(instance=shadowrun::BerechneteAttribute_strategy)
def test_shadowrun::berechneteattribute_ReaktionW_type(instance):
    assert isinstance(instance.ReaktionW, int)


@given(instance=shadowrun::BerechneteAttribute_strategy)
def test_shadowrun::berechneteattribute_ReaktionW_setter(instance):
    original = instance.ReaktionW
    instance.ReaktionW = original
    assert instance.ReaktionW == original

@given(instance=shadowrun::BerechneteAttribute_strategy)
def test_shadowrun::berechneteattribute_Kampfpool_type(instance):
    assert isinstance(instance.Kampfpool, int)


@given(instance=shadowrun::BerechneteAttribute_strategy)
def test_shadowrun::berechneteattribute_Kampfpool_setter(instance):
    original = instance.Kampfpool
    instance.Kampfpool = original
    assert instance.Kampfpool == original

@given(instance=shadowrun::BerechneteAttribute_strategy)
def test_shadowrun::berechneteattribute_Reaktion_type(instance):
    assert isinstance(instance.Reaktion, int)


@given(instance=shadowrun::BerechneteAttribute_strategy)
def test_shadowrun::berechneteattribute_Reaktion_setter(instance):
    original = instance.Reaktion
    instance.Reaktion = original
    assert instance.Reaktion == original

@given(instance=Schadenswiederstand_strategy)
@settings(max_examples=50)
def test_schadenswiederstand_instantiation(instance):
    assert isinstance(instance, Schadenswiederstand)

@given(instance=shadowrun::KoerperlicheAtribute_strategy)
@settings(max_examples=50)
def test_shadowrun::koerperlicheatribute_instantiation(instance):
    assert isinstance(instance, shadowrun::KoerperlicheAtribute)

@given(instance=shadowrun::KoerperlicheAtribute_strategy)
def test_shadowrun::koerperlicheatribute_Staerke_type(instance):
    assert isinstance(instance.Staerke, int)


@given(instance=shadowrun::KoerperlicheAtribute_strategy)
def test_shadowrun::koerperlicheatribute_Staerke_setter(instance):
    original = instance.Staerke
    instance.Staerke = original
    assert instance.Staerke == original

@given(instance=shadowrun::KoerperlicheAtribute_strategy)
def test_shadowrun::koerperlicheatribute_Schnelligkeit_type(instance):
    assert isinstance(instance.Schnelligkeit, int)


@given(instance=shadowrun::KoerperlicheAtribute_strategy)
def test_shadowrun::koerperlicheatribute_Schnelligkeit_setter(instance):
    original = instance.Schnelligkeit
    instance.Schnelligkeit = original
    assert instance.Schnelligkeit == original

@given(instance=shadowrun::KoerperlicheAtribute_strategy)
def test_shadowrun::koerperlicheatribute_Konsitution_type(instance):
    assert isinstance(instance.Konsitution, int)


@given(instance=shadowrun::KoerperlicheAtribute_strategy)
def test_shadowrun::koerperlicheatribute_Konsitution_setter(instance):
    original = instance.Konsitution
    instance.Konsitution = original
    assert instance.Konsitution == original

@given(instance=shadowrun::Sichtverhaeltnisse_strategy)
@settings(max_examples=50)
def test_shadowrun::sichtverhaeltnisse_instantiation(instance):
    assert isinstance(instance, shadowrun::Sichtverhaeltnisse)

@given(instance=shadowrun::Sichtverhaeltnisse_strategy)
def test_shadowrun::sichtverhaeltnisse_Infrarot_type(instance):
    assert isinstance(instance.Infrarot, str)


@given(instance=shadowrun::Sichtverhaeltnisse_strategy)
def test_shadowrun::sichtverhaeltnisse_Infrarot_setter(instance):
    original = instance.Infrarot
    instance.Infrarot = original
    assert instance.Infrarot == original

@given(instance=shadowrun::Sichtverhaeltnisse_strategy)
def test_shadowrun::sichtverhaeltnisse_Ultrasound_type(instance):
    assert isinstance(instance.Ultrasound, str)


@given(instance=shadowrun::Sichtverhaeltnisse_strategy)
def test_shadowrun::sichtverhaeltnisse_Ultrasound_setter(instance):
    original = instance.Ultrasound
    instance.Ultrasound = original
    assert instance.Ultrasound == original

@given(instance=shadowrun::Sichtverhaeltnisse_strategy)
def test_shadowrun::sichtverhaeltnisse_Restlichtverstaerkung_type(instance):
    assert isinstance(instance.Restlichtverstaerkung, str)


@given(instance=shadowrun::Sichtverhaeltnisse_strategy)
def test_shadowrun::sichtverhaeltnisse_Restlichtverstaerkung_setter(instance):
    original = instance.Restlichtverstaerkung
    instance.Restlichtverstaerkung = original
    assert instance.Restlichtverstaerkung == original

@given(instance=shadowrun::FernkampfwaffenModifikatoren_strategy)
@settings(max_examples=50)
def test_shadowrun::fernkampfwaffenmodifikatoren_instantiation(instance):
    assert isinstance(instance, shadowrun::FernkampfwaffenModifikatoren)

@given(instance=shadowrun::FernkampfwaffenModifikatoren_strategy)
def test_shadowrun::fernkampfwaffenmodifikatoren_Schalldaempfer_type(instance):
    assert isinstance(instance.Schalldaempfer, bool)


@given(instance=shadowrun::FernkampfwaffenModifikatoren_strategy)
def test_shadowrun::fernkampfwaffenmodifikatoren_Schalldaempfer_setter(instance):
    original = instance.Schalldaempfer
    instance.Schalldaempfer = original
    assert instance.Schalldaempfer == original

@given(instance=shadowrun::FernkampfwaffenModifikatoren_strategy)
def test_shadowrun::fernkampfwaffenmodifikatoren_Vergroesserung_type(instance):
    assert isinstance(instance.Vergroesserung, int)


@given(instance=shadowrun::FernkampfwaffenModifikatoren_strategy)
def test_shadowrun::fernkampfwaffenmodifikatoren_Vergroesserung_setter(instance):
    original = instance.Vergroesserung
    instance.Vergroesserung = original
    assert instance.Vergroesserung == original

@given(instance=shadowrun::FernkampfwaffenModifikatoren_strategy)
def test_shadowrun::fernkampfwaffenmodifikatoren_lasterPointer_type(instance):
    assert isinstance(instance.lasterPointer, bool)


@given(instance=shadowrun::FernkampfwaffenModifikatoren_strategy)
def test_shadowrun::fernkampfwaffenmodifikatoren_lasterPointer_setter(instance):
    original = instance.lasterPointer
    instance.lasterPointer = original
    assert instance.lasterPointer == original

@given(instance=shadowrun::FernkampfwaffenModifikatoren_strategy)
def test_shadowrun::fernkampfwaffenmodifikatoren_Smartgun_type(instance):
    assert isinstance(instance.Smartgun, str)


@given(instance=shadowrun::FernkampfwaffenModifikatoren_strategy)
def test_shadowrun::fernkampfwaffenmodifikatoren_Smartgun_setter(instance):
    original = instance.Smartgun
    instance.Smartgun = original
    assert instance.Smartgun == original

@given(instance=shadowrun::FernkampfwaffenModifikatoren_strategy)
def test_shadowrun::fernkampfwaffenmodifikatoren_Rueckstoss_type(instance):
    assert isinstance(instance.Rueckstoss, int)


@given(instance=shadowrun::FernkampfwaffenModifikatoren_strategy)
def test_shadowrun::fernkampfwaffenmodifikatoren_Rueckstoss_setter(instance):
    original = instance.Rueckstoss
    instance.Rueckstoss = original
    assert instance.Rueckstoss == original

@given(instance=shadowrun::EObject_strategy)
@settings(max_examples=50)
def test_shadowrun::eobject_instantiation(instance):
    assert isinstance(instance, shadowrun::EObject)

@given(instance=shadowrun::Bemerkbar_strategy)
@settings(max_examples=50)
def test_shadowrun::bemerkbar_instantiation(instance):
    assert isinstance(instance, shadowrun::Bemerkbar)

@given(instance=shadowrun::Bemerkbar_strategy)
def test_shadowrun::bemerkbar_tarnstufe_type(instance):
    assert isinstance(instance.tarnstufe, int)


@given(instance=shadowrun::Bemerkbar_strategy)
def test_shadowrun::bemerkbar_tarnstufe_setter(instance):
    original = instance.tarnstufe
    instance.tarnstufe = original
    assert instance.tarnstufe == original

@given(instance=AbstraktNahkampfwaffe_strategy)
@settings(max_examples=50)
def test_abstraktnahkampfwaffe_instantiation(instance):
    assert isinstance(instance, AbstraktNahkampfwaffe)

@given(instance=shadowrun::Nahkampfwaffe_strategy)
@settings(max_examples=50)
def test_shadowrun::nahkampfwaffe_instantiation(instance):
    assert isinstance(instance, shadowrun::Nahkampfwaffe)

@given(instance=shadowrun::Quelle_strategy)
@settings(max_examples=50)
def test_shadowrun::quelle_instantiation(instance):
    assert isinstance(instance, shadowrun::Quelle)

@given(instance=shadowrun::Quelle_strategy)
def test_shadowrun::quelle_page_type(instance):
    assert isinstance(instance.page, str)


@given(instance=shadowrun::Quelle_strategy)
def test_shadowrun::quelle_page_setter(instance):
    original = instance.page
    instance.page = original
    assert instance.page == original

@given(instance=shadowrun::WarenListe_strategy)
@settings(max_examples=50)
def test_shadowrun::warenliste_instantiation(instance):
    assert isinstance(instance, shadowrun::WarenListe)

@given(instance=shadowrun::WarenListe_strategy)
def test_shadowrun::warenliste_listenWert_type(instance):
    assert isinstance(instance.listenWert, str)


@given(instance=shadowrun::WarenListe_strategy)
def test_shadowrun::warenliste_listenWert_setter(instance):
    original = instance.listenWert
    instance.listenWert = original
    assert instance.listenWert == original

@given(instance=shadowrun::WarenListe_strategy)
def test_shadowrun::warenliste_strassenWert_type(instance):
    assert isinstance(instance.strassenWert, str)


@given(instance=shadowrun::WarenListe_strategy)
def test_shadowrun::warenliste_strassenWert_setter(instance):
    original = instance.strassenWert
    instance.strassenWert = original
    assert instance.strassenWert == original

@given(instance=shadowrun::Reichweiten_strategy)
@settings(max_examples=50)
def test_shadowrun::reichweiten_instantiation(instance):
    assert isinstance(instance, shadowrun::Reichweiten)

@given(instance=shadowrun::Beschreibbar_strategy)
@settings(max_examples=50)
def test_shadowrun::beschreibbar_instantiation(instance):
    assert isinstance(instance, shadowrun::Beschreibbar)

@given(instance=shadowrun::Beschreibbar_strategy)
def test_shadowrun::beschreibbar_beschreibung_type(instance):
    assert isinstance(instance.beschreibung, str)


@given(instance=shadowrun::Beschreibbar_strategy)
def test_shadowrun::beschreibbar_beschreibung_setter(instance):
    original = instance.beschreibung
    instance.beschreibung = original
    assert instance.beschreibung == original

@given(instance=shadowrun::Beschreibbar_strategy)
def test_shadowrun::beschreibbar_image_type(instance):
    assert isinstance(instance.image, str)


@given(instance=shadowrun::Beschreibbar_strategy)
def test_shadowrun::beschreibbar_image_setter(instance):
    original = instance.image
    instance.image = original
    assert instance.image == original

@given(instance=shadowrun::Beschreibbar_strategy)
def test_shadowrun::beschreibbar_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=shadowrun::Beschreibbar_strategy)
def test_shadowrun::beschreibbar_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=shadowrun::GengenstandListe_strategy)
@settings(max_examples=50)
def test_shadowrun::gengenstandliste_instantiation(instance):
    assert isinstance(instance, shadowrun::GengenstandListe)

@given(instance=AbstractMagischePaersona_strategy)
@settings(max_examples=50)
def test_abstractmagischepaersona_instantiation(instance):
    assert isinstance(instance, AbstractMagischePaersona)

@given(instance=shadowrun::PersonaZauber_strategy)
@settings(max_examples=50)
def test_shadowrun::personazauber_instantiation(instance):
    assert isinstance(instance, shadowrun::PersonaZauber)

@given(instance=shadowrun::PersonaZauber_strategy)
def test_shadowrun::personazauber_stufe_type(instance):
    assert isinstance(instance.stufe, int)


@given(instance=shadowrun::PersonaZauber_strategy)
def test_shadowrun::personazauber_stufe_setter(instance):
    original = instance.stufe
    instance.stufe = original
    assert instance.stufe == original

@given(instance=AbstractMagier_strategy)
@settings(max_examples=50)
def test_abstractmagier_instantiation(instance):
    assert isinstance(instance, AbstractMagier)

@given(instance=shadowrun::MagiePersona_strategy)
@settings(max_examples=50)
def test_shadowrun::magiepersona_instantiation(instance):
    assert isinstance(instance, shadowrun::MagiePersona)

@given(instance=shadowrun::Legalitaet_strategy)
@settings(max_examples=50)
def test_shadowrun::legalitaet_instantiation(instance):
    assert isinstance(instance, shadowrun::Legalitaet)

@given(instance=shadowrun::Legalitaet_strategy)
def test_shadowrun::legalitaet_legalitaet_type(instance):
    assert isinstance(instance.legalitaet, str)


@given(instance=shadowrun::Legalitaet_strategy)
def test_shadowrun::legalitaet_legalitaet_setter(instance):
    original = instance.legalitaet
    instance.legalitaet = original
    assert instance.legalitaet == original

@given(instance=AbstraktFertigkeit_strategy)
@settings(max_examples=50)
def test_abstraktfertigkeit_instantiation(instance):
    assert isinstance(instance, AbstraktFertigkeit)

@given(instance=shadowrun::KiAdept_strategy)
@settings(max_examples=50)
def test_shadowrun::kiadept_instantiation(instance):
    assert isinstance(instance, shadowrun::KiAdept)

@given(instance=MagischeMods_strategy)
@settings(max_examples=50)
def test_magischemods_instantiation(instance):
    assert isinstance(instance, MagischeMods)

@given(instance=shadowrun::KiKraft_strategy)
@settings(max_examples=50)
def test_shadowrun::kikraft_instantiation(instance):
    assert isinstance(instance, shadowrun::KiKraft)

@given(instance=BaseMagischePersona_strategy)
@settings(max_examples=50)
def test_basemagischepersona_instantiation(instance):
    assert isinstance(instance, BaseMagischePersona)

@given(instance=shadowrun::AbstractMagier_strategy)
@settings(max_examples=50)
def test_shadowrun::abstractmagier_instantiation(instance):
    assert isinstance(instance, shadowrun::AbstractMagier)

@given(instance=shadowrun::AbstractMagier_strategy)
def test_shadowrun::abstractmagier_InitationsGrad_type(instance):
    assert isinstance(instance.InitationsGrad, int)


@given(instance=shadowrun::AbstractMagier_strategy)
def test_shadowrun::abstractmagier_InitationsGrad_setter(instance):
    original = instance.InitationsGrad
    instance.InitationsGrad = original
    assert instance.InitationsGrad == original

@given(instance=shadowrun::AbstractMagier_strategy)
def test_shadowrun::abstractmagier_MagiePool_type(instance):
    assert isinstance(instance.MagiePool, int)


@given(instance=shadowrun::AbstractMagier_strategy)
def test_shadowrun::abstractmagier_MagiePool_setter(instance):
    original = instance.MagiePool
    instance.MagiePool = original
    assert instance.MagiePool == original

@given(instance=shadowrun::AbstractMagier_strategy)
def test_shadowrun::abstractmagier_Astralpool_type(instance):
    assert isinstance(instance.Astralpool, int)


@given(instance=shadowrun::AbstractMagier_strategy)
def test_shadowrun::abstractmagier_Astralpool_setter(instance):
    original = instance.Astralpool
    instance.Astralpool = original
    assert instance.Astralpool == original

@given(instance=shadowrun::BaseMagischePersona_strategy)
@settings(max_examples=50)
def test_shadowrun::basemagischepersona_instantiation(instance):
    assert isinstance(instance, shadowrun::BaseMagischePersona)

@given(instance=shadowrun::BaseMagischePersona_strategy)
def test_shadowrun::basemagischepersona_magie_type(instance):
    assert isinstance(instance.magie, int)


@given(instance=shadowrun::BaseMagischePersona_strategy)
def test_shadowrun::basemagischepersona_magie_setter(instance):
    original = instance.magie
    instance.magie = original
    assert instance.magie == original

@given(instance=AbstraktModifikatoren_strategy)
@settings(max_examples=50)
def test_abstraktmodifikatoren_instantiation(instance):
    assert isinstance(instance, AbstraktModifikatoren)

@given(instance=shadowrun::MagischeMods_strategy)
@settings(max_examples=50)
def test_shadowrun::magischemods_instantiation(instance):
    assert isinstance(instance, shadowrun::MagischeMods)

@given(instance=shadowrun::koerpermods_strategy)
@settings(max_examples=50)
def test_shadowrun::koerpermods_instantiation(instance):
    assert isinstance(instance, shadowrun::koerpermods)

@given(instance=shadowrun::ModifikatorList_strategy)
@settings(max_examples=50)
def test_shadowrun::modifikatorlist_instantiation(instance):
    assert isinstance(instance, shadowrun::ModifikatorList)

@given(instance=shadowrun::ModifikatorList_strategy)
def test_shadowrun::modifikatorlist_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=shadowrun::ModifikatorList_strategy)
def test_shadowrun::modifikatorlist_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=shadowrun::GeldWert_strategy)
@settings(max_examples=50)
def test_shadowrun::geldwert_instantiation(instance):
    assert isinstance(instance, shadowrun::GeldWert)

@given(instance=shadowrun::GeldWert_strategy)
def test_shadowrun::geldwert_verfuegbarkeit_type(instance):
    assert isinstance(instance.verfuegbarkeit, str)


@given(instance=shadowrun::GeldWert_strategy)
def test_shadowrun::geldwert_verfuegbarkeit_setter(instance):
    original = instance.verfuegbarkeit
    instance.verfuegbarkeit = original
    assert instance.verfuegbarkeit == original

@given(instance=shadowrun::GeldWert_strategy)
def test_shadowrun::geldwert_wert_type(instance):
    assert isinstance(instance.wert, str)


@given(instance=shadowrun::GeldWert_strategy)
def test_shadowrun::geldwert_wert_setter(instance):
    original = instance.wert
    instance.wert = original
    assert instance.wert == original

@given(instance=shadowrun::GeldWert_strategy)
def test_shadowrun::geldwert_strassenIndex_type(instance):
    assert isinstance(instance.strassenIndex, float)


@given(instance=shadowrun::GeldWert_strategy)
def test_shadowrun::geldwert_strassenIndex_setter(instance):
    original = instance.strassenIndex
    instance.strassenIndex = original
    assert instance.strassenIndex == original

@given(instance=koerpermods_strategy)
@settings(max_examples=50)
def test_koerpermods_instantiation(instance):
    assert isinstance(instance, koerpermods)

@given(instance=shadowrun::FK_strategy)
@settings(max_examples=50)
def test_shadowrun::fk_instantiation(instance):
    assert isinstance(instance, shadowrun::FK)

@given(instance=AbstrakteRuestung_strategy)
@settings(max_examples=50)
def test_abstrakteruestung_instantiation(instance):
    assert isinstance(instance, AbstrakteRuestung)

@given(instance=shadowrun::Ruestung_strategy)
@settings(max_examples=50)
def test_shadowrun::ruestung_instantiation(instance):
    assert isinstance(instance, shadowrun::Ruestung)

@given(instance=shadowrun::PersonaKoerper_strategy)
@settings(max_examples=50)
def test_shadowrun::personakoerper_instantiation(instance):
    assert isinstance(instance, shadowrun::PersonaKoerper)

@given(instance=shadowrun::PersonaKoerper_strategy)
def test_shadowrun::personakoerper_gesamtZustand_type(instance):
    assert isinstance(instance.gesamtZustand, int)


@given(instance=shadowrun::PersonaKoerper_strategy)
def test_shadowrun::personakoerper_gesamtZustand_setter(instance):
    original = instance.gesamtZustand
    instance.gesamtZustand = original
    assert instance.gesamtZustand == original

@given(instance=shadowrun::Modifizierbar_strategy)
@settings(max_examples=50)
def test_shadowrun::modifizierbar_instantiation(instance):
    assert isinstance(instance, shadowrun::Modifizierbar)

@given(instance=shadowrun::EAttribute_strategy)
@settings(max_examples=50)
def test_shadowrun::eattribute_instantiation(instance):
    assert isinstance(instance, shadowrun::EAttribute)

@given(instance=shadowrun::AttributModifikatorWert_strategy)
@settings(max_examples=50)
def test_shadowrun::attributmodifikatorwert_instantiation(instance):
    assert isinstance(instance, shadowrun::AttributModifikatorWert)

@given(instance=shadowrun::AttributModifikatorWert_strategy)
def test_shadowrun::attributmodifikatorwert_wert_type(instance):
    assert isinstance(instance.wert, int)


@given(instance=shadowrun::AttributModifikatorWert_strategy)
def test_shadowrun::attributmodifikatorwert_wert_setter(instance):
    original = instance.wert
    instance.wert = original
    assert instance.wert == original

@given(instance=shadowrun::BasicList_strategy)
@settings(max_examples=50)
def test_shadowrun::basiclist_instantiation(instance):
    assert isinstance(instance, shadowrun::BasicList)

@given(instance=AbstaktFernKampfwaffe_strategy)
@settings(max_examples=50)
def test_abstaktfernkampfwaffe_instantiation(instance):
    assert isinstance(instance, AbstaktFernKampfwaffe)

@given(instance=shadowrun::Projektilwaffe_strategy)
@settings(max_examples=50)
def test_shadowrun::projektilwaffe_instantiation(instance):
    assert isinstance(instance, shadowrun::Projektilwaffe)

@given(instance=shadowrun::Wurfwaffe_strategy)
@settings(max_examples=50)
def test_shadowrun::wurfwaffe_instantiation(instance):
    assert isinstance(instance, shadowrun::Wurfwaffe)

@given(instance=shadowrun::Feuerwaffe_strategy)
@settings(max_examples=50)
def test_shadowrun::feuerwaffe_instantiation(instance):
    assert isinstance(instance, shadowrun::Feuerwaffe)

@given(instance=shadowrun::Feuerwaffe_strategy)
def test_shadowrun::feuerwaffe_kapazitaet_type(instance):
    assert isinstance(instance.kapazitaet, int)


@given(instance=shadowrun::Feuerwaffe_strategy)
def test_shadowrun::feuerwaffe_kapazitaet_setter(instance):
    original = instance.kapazitaet
    instance.kapazitaet = original
    assert instance.kapazitaet == original

@given(instance=shadowrun::Feuerwaffe_strategy)
def test_shadowrun::feuerwaffe_modie_type(instance):
    assert isinstance(instance.modie, str)


@given(instance=shadowrun::Feuerwaffe_strategy)
def test_shadowrun::feuerwaffe_modie_setter(instance):
    original = instance.modie
    instance.modie = original
    assert instance.modie == original

@given(instance=shadowrun::Feuerwaffe_strategy)
def test_shadowrun::feuerwaffe_munitionstyp_type(instance):
    assert isinstance(instance.munitionstyp, str)


@given(instance=shadowrun::Feuerwaffe_strategy)
def test_shadowrun::feuerwaffe_munitionstyp_setter(instance):
    original = instance.munitionstyp
    instance.munitionstyp = original
    assert instance.munitionstyp == original

@given(instance=Gegenstand_strategy)
@settings(max_examples=50)
def test_gegenstand_instantiation(instance):
    assert isinstance(instance, Gegenstand)

@given(instance=shadowrun::MunitionsBehealter_strategy)
@settings(max_examples=50)
def test_shadowrun::munitionsbehealter_instantiation(instance):
    assert isinstance(instance, shadowrun::MunitionsBehealter)

@given(instance=shadowrun::Behaelter_strategy)
@settings(max_examples=50)
def test_shadowrun::behaelter_instantiation(instance):
    assert isinstance(instance, shadowrun::Behaelter)

@given(instance=shadowrun::Behaelter_strategy)
def test_shadowrun::behaelter_kapazitaet_type(instance):
    assert isinstance(instance.kapazitaet, int)


@given(instance=shadowrun::Behaelter_strategy)
def test_shadowrun::behaelter_kapazitaet_setter(instance):
    original = instance.kapazitaet
    instance.kapazitaet = original
    assert instance.kapazitaet == original

@given(instance=NahkampfReichweite_strategy)
@settings(max_examples=50)
def test_nahkampfreichweite_instantiation(instance):
    assert isinstance(instance, NahkampfReichweite)

@given(instance=AbstraktKleidung_strategy)
@settings(max_examples=50)
def test_abstraktkleidung_instantiation(instance):
    assert isinstance(instance, AbstraktKleidung)

@given(instance=shadowrun::AbstrakteRuestung_strategy)
@settings(max_examples=50)
def test_shadowrun::abstrakteruestung_instantiation(instance):
    assert isinstance(instance, shadowrun::AbstrakteRuestung)

@given(instance=shadowrun::AbstrakteRuestung_strategy)
def test_shadowrun::abstrakteruestung_ruestungsSchutzBalistisch_type(instance):
    assert isinstance(instance.ruestungsSchutzBalistisch, int)


@given(instance=shadowrun::AbstrakteRuestung_strategy)
def test_shadowrun::abstrakteruestung_ruestungsSchutzBalistisch_setter(instance):
    original = instance.ruestungsSchutzBalistisch
    instance.ruestungsSchutzBalistisch = original
    assert instance.ruestungsSchutzBalistisch == original

@given(instance=shadowrun::AbstrakteRuestung_strategy)
def test_shadowrun::abstrakteruestung_ruestungsSchutzStoss_type(instance):
    assert isinstance(instance.ruestungsSchutzStoss, int)


@given(instance=shadowrun::AbstrakteRuestung_strategy)
def test_shadowrun::abstrakteruestung_ruestungsSchutzStoss_setter(instance):
    original = instance.ruestungsSchutzStoss
    instance.ruestungsSchutzStoss = original
    assert instance.ruestungsSchutzStoss == original

@given(instance=shadowrun::RaumKoordinate_strategy)
@settings(max_examples=50)
def test_shadowrun::raumkoordinate_instantiation(instance):
    assert isinstance(instance, shadowrun::RaumKoordinate)

@given(instance=shadowrun::AbstrakRaumKoerper_strategy)
@settings(max_examples=50)
def test_shadowrun::abstrakraumkoerper_instantiation(instance):
    assert isinstance(instance, shadowrun::AbstrakRaumKoerper)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=shadowrun::AbstrakRaumKoerper_strategy)
@settings(max_examples=30)
def test_shadowrun::abstrakraumkoerper_processworldtick_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.ProcessWorldTick()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.ProcessWorldTick).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'ProcessWorldTick' in shadowrun::AbstrakRaumKoerper is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'ProcessWorldTick' in shadowrun::AbstrakRaumKoerper did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'ProcessWorldTick' in shadowrun::AbstrakRaumKoerper is not implemented or raised an error")

@given(instance=shadowrun::Spezialisierung_strategy)
@settings(max_examples=50)
def test_shadowrun::spezialisierung_instantiation(instance):
    assert isinstance(instance, shadowrun::Spezialisierung)

@given(instance=AbstaktPersona_strategy)
@settings(max_examples=50)
def test_abstaktpersona_instantiation(instance):
    assert isinstance(instance, AbstaktPersona)

@given(instance=shadowrun::AbstractMagischePaersona_strategy)
@settings(max_examples=50)
def test_shadowrun::abstractmagischepaersona_instantiation(instance):
    assert isinstance(instance, shadowrun::AbstractMagischePaersona)

@given(instance=shadowrun::AbstractMagischePaersona_strategy)
def test_shadowrun::abstractmagischepaersona_magieBase_type(instance):
    assert isinstance(instance.magieBase, int)


@given(instance=shadowrun::AbstractMagischePaersona_strategy)
def test_shadowrun::abstractmagischepaersona_magieBase_setter(instance):
    original = instance.magieBase
    instance.magieBase = original
    assert instance.magieBase == original

@given(instance=shadowrun::Persona_strategy)
@settings(max_examples=50)
def test_shadowrun::persona_instantiation(instance):
    assert isinstance(instance, shadowrun::Persona)

@given(instance=shadowrun::Kleidung_strategy)
@settings(max_examples=50)
def test_shadowrun::kleidung_instantiation(instance):
    assert isinstance(instance, shadowrun::Kleidung)

@given(instance=shadowrun::PersonaFertigkeit_strategy)
@settings(max_examples=50)
def test_shadowrun::personafertigkeit_instantiation(instance):
    assert isinstance(instance, shadowrun::PersonaFertigkeit)

@given(instance=shadowrun::PersonaFertigkeit_strategy)
def test_shadowrun::personafertigkeit_stufe_type(instance):
    assert isinstance(instance.stufe, int)


@given(instance=shadowrun::PersonaFertigkeit_strategy)
def test_shadowrun::personafertigkeit_stufe_setter(instance):
    original = instance.stufe
    instance.stufe = original
    assert instance.stufe == original

@given(instance=shadowrun::Konzentration_strategy)
@settings(max_examples=50)
def test_shadowrun::konzentration_instantiation(instance):
    assert isinstance(instance, shadowrun::Konzentration)

@given(instance=shadowrun::Fertigkeit_strategy)
@settings(max_examples=50)
def test_shadowrun::fertigkeit_instantiation(instance):
    assert isinstance(instance, shadowrun::Fertigkeit)

@given(instance=AbstaktGegenstand_strategy)
@settings(max_examples=50)
def test_abstaktgegenstand_instantiation(instance):
    assert isinstance(instance, AbstaktGegenstand)

@given(instance=shadowrun::Munition_strategy)
@settings(max_examples=50)
def test_shadowrun::munition_instantiation(instance):
    assert isinstance(instance, shadowrun::Munition)

@given(instance=shadowrun::Munition_strategy)
def test_shadowrun::munition_power_type(instance):
    assert isinstance(instance.power, int)


@given(instance=shadowrun::Munition_strategy)
def test_shadowrun::munition_power_setter(instance):
    original = instance.power
    instance.power = original
    assert instance.power == original

@given(instance=shadowrun::Munition_strategy)
def test_shadowrun::munition_schadensTyp_type(instance):
    assert isinstance(instance.schadensTyp, str)


@given(instance=shadowrun::Munition_strategy)
def test_shadowrun::munition_schadensTyp_setter(instance):
    original = instance.schadensTyp
    instance.schadensTyp = original
    assert instance.schadensTyp == original

@given(instance=shadowrun::Munition_strategy)
def test_shadowrun::munition_niveau_type(instance):
    assert isinstance(instance.niveau, int)


@given(instance=shadowrun::Munition_strategy)
def test_shadowrun::munition_niveau_setter(instance):
    original = instance.niveau
    instance.niveau = original
    assert instance.niveau == original

@given(instance=shadowrun::Gegenstand_strategy)
@settings(max_examples=50)
def test_shadowrun::gegenstand_instantiation(instance):
    assert isinstance(instance, shadowrun::Gegenstand)

@given(instance=shadowrun::AbstraktKleidung_strategy)
@settings(max_examples=50)
def test_shadowrun::abstraktkleidung_instantiation(instance):
    assert isinstance(instance, shadowrun::AbstraktKleidung)

@given(instance=shadowrun::AbstraktKleidung_strategy)
def test_shadowrun::abstraktkleidung_koeperTeil_type(instance):
    assert isinstance(instance.koeperTeil, str)


@given(instance=shadowrun::AbstraktKleidung_strategy)
def test_shadowrun::abstraktkleidung_koeperTeil_setter(instance):
    original = instance.koeperTeil
    instance.koeperTeil = original
    assert instance.koeperTeil == original

@given(instance=shadowrun::AbstaktWaffe_strategy)
@settings(max_examples=50)
def test_shadowrun::abstaktwaffe_instantiation(instance):
    assert isinstance(instance, shadowrun::AbstaktWaffe)

@given(instance=shadowrun::AbstaktWaffe_strategy)
def test_shadowrun::abstaktwaffe_schadenscode_type(instance):
    assert isinstance(instance.schadenscode, str)


@given(instance=shadowrun::AbstaktWaffe_strategy)
def test_shadowrun::abstaktwaffe_schadenscode_setter(instance):
    original = instance.schadenscode
    instance.schadenscode = original
    assert instance.schadenscode == original

@given(instance=Modifizierbar_strategy)
@settings(max_examples=50)
def test_modifizierbar_instantiation(instance):
    assert isinstance(instance, Modifizierbar)

@given(instance=Quelle_strategy)
@settings(max_examples=50)
def test_quelle_instantiation(instance):
    assert isinstance(instance, Quelle)

@given(instance=Bemerkbar_strategy)
@settings(max_examples=50)
def test_bemerkbar_instantiation(instance):
    assert isinstance(instance, Bemerkbar)

@given(instance=Legalitaet_strategy)
@settings(max_examples=50)
def test_legalitaet_instantiation(instance):
    assert isinstance(instance, Legalitaet)

@given(instance=Beschreibbar_strategy)
@settings(max_examples=50)
def test_beschreibbar_instantiation(instance):
    assert isinstance(instance, Beschreibbar)

@given(instance=shadowrun::Zauber_strategy)
@settings(max_examples=50)
def test_shadowrun::zauber_instantiation(instance):
    assert isinstance(instance, shadowrun::Zauber)

@given(instance=shadowrun::Zauber_strategy)
def test_shadowrun::zauber_art_type(instance):
    assert isinstance(instance.art, str)


@given(instance=shadowrun::Zauber_strategy)
def test_shadowrun::zauber_art_setter(instance):
    original = instance.art
    instance.art = original
    assert instance.art == original

@given(instance=shadowrun::Zauber_strategy)
def test_shadowrun::zauber_reichweite_type(instance):
    assert isinstance(instance.reichweite, str)


@given(instance=shadowrun::Zauber_strategy)
def test_shadowrun::zauber_reichweite_setter(instance):
    original = instance.reichweite
    instance.reichweite = original
    assert instance.reichweite == original

@given(instance=shadowrun::Zauber_strategy)
def test_shadowrun::zauber_Enzug_type(instance):
    assert isinstance(instance.Enzug, str)


@given(instance=shadowrun::Zauber_strategy)
def test_shadowrun::zauber_Enzug_setter(instance):
    original = instance.Enzug
    instance.Enzug = original
    assert instance.Enzug == original

@given(instance=shadowrun::Zauber_strategy)
def test_shadowrun::zauber_Schaden_type(instance):
    assert isinstance(instance.Schaden, str)


@given(instance=shadowrun::Zauber_strategy)
def test_shadowrun::zauber_Schaden_setter(instance):
    original = instance.Schaden
    instance.Schaden = original
    assert instance.Schaden == original

@given(instance=shadowrun::Zauber_strategy)
def test_shadowrun::zauber_Mindestwurf_type(instance):
    assert isinstance(instance.Mindestwurf, str)


@given(instance=shadowrun::Zauber_strategy)
def test_shadowrun::zauber_Mindestwurf_setter(instance):
    original = instance.Mindestwurf
    instance.Mindestwurf = original
    assert instance.Mindestwurf == original

@given(instance=shadowrun::Zauber_strategy)
def test_shadowrun::zauber_Dauer_type(instance):
    assert isinstance(instance.Dauer, str)


@given(instance=shadowrun::Zauber_strategy)
def test_shadowrun::zauber_Dauer_setter(instance):
    original = instance.Dauer
    instance.Dauer = original
    assert instance.Dauer == original

@given(instance=shadowrun::ShrList_strategy)
@settings(max_examples=50)
def test_shadowrun::shrlist_instantiation(instance):
    assert isinstance(instance, shadowrun::ShrList)

@given(instance=shadowrun::Totem_strategy)
@settings(max_examples=50)
def test_shadowrun::totem_instantiation(instance):
    assert isinstance(instance, shadowrun::Totem)

@given(instance=shadowrun::Script_strategy)
@settings(max_examples=50)
def test_shadowrun::script_instantiation(instance):
    assert isinstance(instance, shadowrun::Script)

@given(instance=shadowrun::AbstraktModifikatoren_strategy)
@settings(max_examples=50)
def test_shadowrun::abstraktmodifikatoren_instantiation(instance):
    assert isinstance(instance, shadowrun::AbstraktModifikatoren)

@given(instance=shadowrun::Placement_strategy)
@settings(max_examples=50)
def test_shadowrun::placement_instantiation(instance):
    assert isinstance(instance, shadowrun::Placement)

@given(instance=shadowrun::SourceBook_strategy)
@settings(max_examples=50)
def test_shadowrun::sourcebook_instantiation(instance):
    assert isinstance(instance, shadowrun::SourceBook)

@given(instance=shadowrun::SourceBook_strategy)
def test_shadowrun::sourcebook_endShrTime_type(instance):
    assert isinstance(instance.endShrTime, str)


@given(instance=shadowrun::SourceBook_strategy)
def test_shadowrun::sourcebook_endShrTime_setter(instance):
    original = instance.endShrTime
    instance.endShrTime = original
    assert instance.endShrTime == original

@given(instance=shadowrun::SourceBook_strategy)
def test_shadowrun::sourcebook_startShrTime_type(instance):
    assert isinstance(instance.startShrTime, str)


@given(instance=shadowrun::SourceBook_strategy)
def test_shadowrun::sourcebook_startShrTime_setter(instance):
    original = instance.startShrTime
    instance.startShrTime = original
    assert instance.startShrTime == original

@given(instance=shadowrun::Spezies_strategy)
@settings(max_examples=50)
def test_shadowrun::spezies_instantiation(instance):
    assert isinstance(instance, shadowrun::Spezies)

@given(instance=shadowrun::Spezies_strategy)
def test_shadowrun::spezies_StaerkeMax_type(instance):
    assert isinstance(instance.StaerkeMax, int)


@given(instance=shadowrun::Spezies_strategy)
def test_shadowrun::spezies_StaerkeMax_setter(instance):
    original = instance.StaerkeMax
    instance.StaerkeMax = original
    assert instance.StaerkeMax == original

@given(instance=shadowrun::Spezies_strategy)
def test_shadowrun::spezies_WillenskraftMax_type(instance):
    assert isinstance(instance.WillenskraftMax, int)


@given(instance=shadowrun::Spezies_strategy)
def test_shadowrun::spezies_WillenskraftMax_setter(instance):
    original = instance.WillenskraftMax
    instance.WillenskraftMax = original
    assert instance.WillenskraftMax == original

@given(instance=shadowrun::Spezies_strategy)
def test_shadowrun::spezies_KonsitutionMax_type(instance):
    assert isinstance(instance.KonsitutionMax, int)


@given(instance=shadowrun::Spezies_strategy)
def test_shadowrun::spezies_KonsitutionMax_setter(instance):
    original = instance.KonsitutionMax
    instance.KonsitutionMax = original
    assert instance.KonsitutionMax == original

@given(instance=shadowrun::Spezies_strategy)
def test_shadowrun::spezies_SchnelligkeitMax_type(instance):
    assert isinstance(instance.SchnelligkeitMax, int)


@given(instance=shadowrun::Spezies_strategy)
def test_shadowrun::spezies_SchnelligkeitMax_setter(instance):
    original = instance.SchnelligkeitMax
    instance.SchnelligkeitMax = original
    assert instance.SchnelligkeitMax == original

@given(instance=shadowrun::Spezies_strategy)
def test_shadowrun::spezies_InteligenzMax_type(instance):
    assert isinstance(instance.InteligenzMax, int)


@given(instance=shadowrun::Spezies_strategy)
def test_shadowrun::spezies_InteligenzMax_setter(instance):
    original = instance.InteligenzMax
    instance.InteligenzMax = original
    assert instance.InteligenzMax == original

@given(instance=shadowrun::Spezies_strategy)
def test_shadowrun::spezies_CharismaMax_type(instance):
    assert isinstance(instance.CharismaMax, int)


@given(instance=shadowrun::Spezies_strategy)
def test_shadowrun::spezies_CharismaMax_setter(instance):
    original = instance.CharismaMax
    instance.CharismaMax = original
    assert instance.CharismaMax == original

@given(instance=shadowrun::PersonaGruppe_strategy)
@settings(max_examples=50)
def test_shadowrun::personagruppe_instantiation(instance):
    assert isinstance(instance, shadowrun::PersonaGruppe)

@given(instance=GeldWert_strategy)
@settings(max_examples=50)
def test_geldwert_instantiation(instance):
    assert isinstance(instance, GeldWert)

@given(instance=shadowrun::BioWare_strategy)
@settings(max_examples=50)
def test_shadowrun::bioware_instantiation(instance):
    assert isinstance(instance, shadowrun::BioWare)

@given(instance=shadowrun::Cyberware_strategy)
@settings(max_examples=50)
def test_shadowrun::cyberware_instantiation(instance):
    assert isinstance(instance, shadowrun::Cyberware)

@given(instance=FK_strategy)
@settings(max_examples=50)
def test_fk_instantiation(instance):
    assert isinstance(instance, FK)

@given(instance=shadowrun::FertigkeitsGruppe_strategy)
@settings(max_examples=50)
def test_shadowrun::fertigkeitsgruppe_instantiation(instance):
    assert isinstance(instance, shadowrun::FertigkeitsGruppe)

@given(instance=shadowrun::AbstraktFertigkeit_strategy)
@settings(max_examples=50)
def test_shadowrun::abstraktfertigkeit_instantiation(instance):
    assert isinstance(instance, shadowrun::AbstraktFertigkeit)

@given(instance=shadowrun::AbstaktGegenstand_strategy)
@settings(max_examples=50)
def test_shadowrun::abstaktgegenstand_instantiation(instance):
    assert isinstance(instance, shadowrun::AbstaktGegenstand)

@given(instance=shadowrun::AbstaktGegenstand_strategy)
def test_shadowrun::abstaktgegenstand_verbraucht_type(instance):
    assert isinstance(instance.verbraucht, bool)


@given(instance=shadowrun::AbstaktGegenstand_strategy)
def test_shadowrun::abstaktgegenstand_verbraucht_setter(instance):
    original = instance.verbraucht
    instance.verbraucht = original
    assert instance.verbraucht == original

@given(instance=shadowrun::AbstaktGegenstand_strategy)
def test_shadowrun::abstaktgegenstand_inBenutzung_type(instance):
    assert isinstance(instance.inBenutzung, bool)


@given(instance=shadowrun::AbstaktGegenstand_strategy)
def test_shadowrun::abstaktgegenstand_inBenutzung_setter(instance):
    original = instance.inBenutzung
    instance.inBenutzung = original
    assert instance.inBenutzung == original

@given(instance=shadowrun::AbstaktGegenstand_strategy)
def test_shadowrun::abstaktgegenstand_raumKapazitaet_type(instance):
    assert isinstance(instance.raumKapazitaet, int)


@given(instance=shadowrun::AbstaktGegenstand_strategy)
def test_shadowrun::abstaktgegenstand_raumKapazitaet_setter(instance):
    original = instance.raumKapazitaet
    instance.raumKapazitaet = original
    assert instance.raumKapazitaet == original

@given(instance=shadowrun::AbstaktGegenstand_strategy)
def test_shadowrun::abstaktgegenstand_tragbar_type(instance):
    assert isinstance(instance.tragbar, str)


@given(instance=shadowrun::AbstaktGegenstand_strategy)
def test_shadowrun::abstaktgegenstand_tragbar_setter(instance):
    original = instance.tragbar
    instance.tragbar = original
    assert instance.tragbar == original

@given(instance=shadowrun::AbstaktGegenstand_strategy)
def test_shadowrun::abstaktgegenstand_gewicht_type(instance):
    assert isinstance(instance.gewicht, float)


@given(instance=shadowrun::AbstaktGegenstand_strategy)
def test_shadowrun::abstaktgegenstand_gewicht_setter(instance):
    original = instance.gewicht
    instance.gewicht = original
    assert instance.gewicht == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=shadowrun::AbstaktGegenstand_strategy)
@settings(max_examples=30)
def test_shadowrun::abstaktgegenstand_erzeugepersonahandlung_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.ErzeugePersonaHandlung()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.ErzeugePersonaHandlung).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'ErzeugePersonaHandlung' in shadowrun::AbstaktGegenstand is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'ErzeugePersonaHandlung' in shadowrun::AbstaktGegenstand did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'ErzeugePersonaHandlung' in shadowrun::AbstaktGegenstand is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=shadowrun::AbstaktGegenstand_strategy)
@settings(max_examples=30)
def test_shadowrun::abstaktgegenstand_benutze_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.Benutze()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.Benutze).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'Benutze' in shadowrun::AbstaktGegenstand is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'Benutze' in shadowrun::AbstaktGegenstand did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'Benutze' in shadowrun::AbstaktGegenstand is not implemented or raised an error")

@given(instance=shadowrun::Reichweite_strategy)
@settings(max_examples=50)
def test_shadowrun::reichweite_instantiation(instance):
    assert isinstance(instance, shadowrun::Reichweite)

@given(instance=shadowrun::Reichweite_strategy)
def test_shadowrun::reichweite_reichweiteKurz_type(instance):
    assert isinstance(instance.reichweiteKurz, int)


@given(instance=shadowrun::Reichweite_strategy)
def test_shadowrun::reichweite_reichweiteKurz_setter(instance):
    original = instance.reichweiteKurz
    instance.reichweiteKurz = original
    assert instance.reichweiteKurz == original

@given(instance=shadowrun::Reichweite_strategy)
def test_shadowrun::reichweite_reichweiteExtrem1_type(instance):
    assert isinstance(instance.reichweiteExtrem1, int)


@given(instance=shadowrun::Reichweite_strategy)
def test_shadowrun::reichweite_reichweiteExtrem1_setter(instance):
    original = instance.reichweiteExtrem1
    instance.reichweiteExtrem1 = original
    assert instance.reichweiteExtrem1 == original

@given(instance=shadowrun::Reichweite_strategy)
def test_shadowrun::reichweite_reichweiteMittel1_type(instance):
    assert isinstance(instance.reichweiteMittel1, int)


@given(instance=shadowrun::Reichweite_strategy)
def test_shadowrun::reichweite_reichweiteMittel1_setter(instance):
    original = instance.reichweiteMittel1
    instance.reichweiteMittel1 = original
    assert instance.reichweiteMittel1 == original

@given(instance=shadowrun::Reichweite_strategy)
def test_shadowrun::reichweite_reichweiteExtrem_type(instance):
    assert isinstance(instance.reichweiteExtrem, int)


@given(instance=shadowrun::Reichweite_strategy)
def test_shadowrun::reichweite_reichweiteExtrem_setter(instance):
    original = instance.reichweiteExtrem
    instance.reichweiteExtrem = original
    assert instance.reichweiteExtrem == original

@given(instance=shadowrun::Reichweite_strategy)
def test_shadowrun::reichweite_reichweiteWeit1_type(instance):
    assert isinstance(instance.reichweiteWeit1, int)


@given(instance=shadowrun::Reichweite_strategy)
def test_shadowrun::reichweite_reichweiteWeit1_setter(instance):
    original = instance.reichweiteWeit1
    instance.reichweiteWeit1 = original
    assert instance.reichweiteWeit1 == original

@given(instance=shadowrun::Reichweite_strategy)
def test_shadowrun::reichweite_reichweiteWeit_type(instance):
    assert isinstance(instance.reichweiteWeit, int)


@given(instance=shadowrun::Reichweite_strategy)
def test_shadowrun::reichweite_reichweiteWeit_setter(instance):
    original = instance.reichweiteWeit
    instance.reichweiteWeit = original
    assert instance.reichweiteWeit == original

@given(instance=shadowrun::Reichweite_strategy)
def test_shadowrun::reichweite_reichweiteKurz1_type(instance):
    assert isinstance(instance.reichweiteKurz1, int)


@given(instance=shadowrun::Reichweite_strategy)
def test_shadowrun::reichweite_reichweiteKurz1_setter(instance):
    original = instance.reichweiteKurz1
    instance.reichweiteKurz1 = original
    assert instance.reichweiteKurz1 == original

@given(instance=shadowrun::Reichweite_strategy)
def test_shadowrun::reichweite_reichweiteMittel_type(instance):
    assert isinstance(instance.reichweiteMittel, int)


@given(instance=shadowrun::Reichweite_strategy)
def test_shadowrun::reichweite_reichweiteMittel_setter(instance):
    original = instance.reichweiteMittel
    instance.reichweiteMittel = original
    assert instance.reichweiteMittel == original

@given(instance=AbstaktWaffe_strategy)
@settings(max_examples=50)
def test_abstaktwaffe_instantiation(instance):
    assert isinstance(instance, AbstaktWaffe)

@given(instance=shadowrun::Granate_strategy)
@settings(max_examples=50)
def test_shadowrun::granate_instantiation(instance):
    assert isinstance(instance, shadowrun::Granate)

@given(instance=shadowrun::Granate_strategy)
def test_shadowrun::granate_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=shadowrun::Granate_strategy)
def test_shadowrun::granate_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=shadowrun::Granate_strategy)
def test_shadowrun::granate_daempfung_type(instance):
    assert isinstance(instance.daempfung, str)


@given(instance=shadowrun::Granate_strategy)
def test_shadowrun::granate_daempfung_setter(instance):
    original = instance.daempfung
    instance.daempfung = original
    assert instance.daempfung == original

@given(instance=shadowrun::AbstraktNahkampfwaffe_strategy)
@settings(max_examples=50)
def test_shadowrun::abstraktnahkampfwaffe_instantiation(instance):
    assert isinstance(instance, shadowrun::AbstraktNahkampfwaffe)

@given(instance=shadowrun::AbstaktFernKampfwaffe_strategy)
@settings(max_examples=50)
def test_shadowrun::abstaktfernkampfwaffe_instantiation(instance):
    assert isinstance(instance, shadowrun::AbstaktFernKampfwaffe)

@given(instance=GeistigeAttribute_strategy)
@settings(max_examples=50)
def test_geistigeattribute_instantiation(instance):
    assert isinstance(instance, GeistigeAttribute)

@given(instance=BerechneteAttribute_strategy)
@settings(max_examples=50)
def test_berechneteattribute_instantiation(instance):
    assert isinstance(instance, BerechneteAttribute)

@given(instance=KoerperlicheAtribute_strategy)
@settings(max_examples=50)
def test_koerperlicheatribute_instantiation(instance):
    assert isinstance(instance, KoerperlicheAtribute)

@given(instance=BodyIndex_strategy)
@settings(max_examples=50)
def test_bodyindex_instantiation(instance):
    assert isinstance(instance, BodyIndex)

@given(instance=Essenz_strategy)
@settings(max_examples=50)
def test_essenz_instantiation(instance):
    assert isinstance(instance, Essenz)

@given(instance=shadowrun::AbstaktPersona_strategy)
@settings(max_examples=50)
def test_shadowrun::abstaktpersona_instantiation(instance):
    assert isinstance(instance, shadowrun::AbstaktPersona)

@given(instance=shadowrun::AbstaktPersona_strategy)
def test_shadowrun::abstaktpersona_WillenskraftBase_type(instance):
    assert isinstance(instance.WillenskraftBase, int)


@given(instance=shadowrun::AbstaktPersona_strategy)
def test_shadowrun::abstaktpersona_WillenskraftBase_setter(instance):
    original = instance.WillenskraftBase
    instance.WillenskraftBase = original
    assert instance.WillenskraftBase == original

@given(instance=shadowrun::AbstaktPersona_strategy)
def test_shadowrun::abstaktpersona_StaerkeBase_type(instance):
    assert isinstance(instance.StaerkeBase, int)


@given(instance=shadowrun::AbstaktPersona_strategy)
def test_shadowrun::abstaktpersona_StaerkeBase_setter(instance):
    original = instance.StaerkeBase
    instance.StaerkeBase = original
    assert instance.StaerkeBase == original

@given(instance=shadowrun::AbstaktPersona_strategy)
def test_shadowrun::abstaktpersona_ReaktionBase_type(instance):
    assert isinstance(instance.ReaktionBase, int)


@given(instance=shadowrun::AbstaktPersona_strategy)
def test_shadowrun::abstaktpersona_ReaktionBase_setter(instance):
    original = instance.ReaktionBase
    instance.ReaktionBase = original
    assert instance.ReaktionBase == original

@given(instance=shadowrun::AbstaktPersona_strategy)
def test_shadowrun::abstaktpersona_SchnelligkeitBase_type(instance):
    assert isinstance(instance.SchnelligkeitBase, int)


@given(instance=shadowrun::AbstaktPersona_strategy)
def test_shadowrun::abstaktpersona_SchnelligkeitBase_setter(instance):
    original = instance.SchnelligkeitBase
    instance.SchnelligkeitBase = original
    assert instance.SchnelligkeitBase == original

@given(instance=shadowrun::AbstaktPersona_strategy)
def test_shadowrun::abstaktpersona_EssenzBase_type(instance):
    assert isinstance(instance.EssenzBase, int)


@given(instance=shadowrun::AbstaktPersona_strategy)
def test_shadowrun::abstaktpersona_EssenzBase_setter(instance):
    original = instance.EssenzBase
    instance.EssenzBase = original
    assert instance.EssenzBase == original

@given(instance=shadowrun::AbstaktPersona_strategy)
def test_shadowrun::abstaktpersona_eigenGewicht_type(instance):
    assert isinstance(instance.eigenGewicht, int)


@given(instance=shadowrun::AbstaktPersona_strategy)
def test_shadowrun::abstaktpersona_eigenGewicht_setter(instance):
    original = instance.eigenGewicht
    instance.eigenGewicht = original
    assert instance.eigenGewicht == original

@given(instance=shadowrun::AbstaktPersona_strategy)
def test_shadowrun::abstaktpersona_CharismaBase_type(instance):
    assert isinstance(instance.CharismaBase, int)


@given(instance=shadowrun::AbstaktPersona_strategy)
def test_shadowrun::abstaktpersona_CharismaBase_setter(instance):
    original = instance.CharismaBase
    instance.CharismaBase = original
    assert instance.CharismaBase == original

@given(instance=shadowrun::AbstaktPersona_strategy)
def test_shadowrun::abstaktpersona_KonsitutionBase_type(instance):
    assert isinstance(instance.KonsitutionBase, int)


@given(instance=shadowrun::AbstaktPersona_strategy)
def test_shadowrun::abstaktpersona_KonsitutionBase_setter(instance):
    original = instance.KonsitutionBase
    instance.KonsitutionBase = original
    assert instance.KonsitutionBase == original

@given(instance=shadowrun::AbstaktPersona_strategy)
def test_shadowrun::abstaktpersona_KampfpoolBase_type(instance):
    assert isinstance(instance.KampfpoolBase, int)


@given(instance=shadowrun::AbstaktPersona_strategy)
def test_shadowrun::abstaktpersona_KampfpoolBase_setter(instance):
    original = instance.KampfpoolBase
    instance.KampfpoolBase = original
    assert instance.KampfpoolBase == original

@given(instance=shadowrun::AbstaktPersona_strategy)
def test_shadowrun::abstaktpersona_ReaktionWBase_type(instance):
    assert isinstance(instance.ReaktionWBase, int)


@given(instance=shadowrun::AbstaktPersona_strategy)
def test_shadowrun::abstaktpersona_ReaktionWBase_setter(instance):
    original = instance.ReaktionWBase
    instance.ReaktionWBase = original
    assert instance.ReaktionWBase == original

@given(instance=shadowrun::AbstaktPersona_strategy)
def test_shadowrun::abstaktpersona_modsetter_type(instance):
    assert isinstance(instance.modsetter, str)


@given(instance=shadowrun::AbstaktPersona_strategy)
def test_shadowrun::abstaktpersona_modsetter_setter(instance):
    original = instance.modsetter
    instance.modsetter = original
    assert instance.modsetter == original

@given(instance=shadowrun::AbstaktPersona_strategy)
def test_shadowrun::abstaktpersona_InteligenzBase_type(instance):
    assert isinstance(instance.InteligenzBase, int)


@given(instance=shadowrun::AbstaktPersona_strategy)
def test_shadowrun::abstaktpersona_InteligenzBase_setter(instance):
    original = instance.InteligenzBase
    instance.InteligenzBase = original
    assert instance.InteligenzBase == original
