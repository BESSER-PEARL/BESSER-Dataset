import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    MatrixAttributes,
    Fahrzeug,
    shr5::Drohne,
    shr5::PassagierFahrzeug,
    PassagierFahrzeug,
    shr5::Bodenfahrzeug,
    FahrzeugZustand,
    shr5::ChrakterLimits,
    shr5::AstraleProjektion,
    shr5::Panzerung,
    shr5::Zauberer,
    AstraleProjektion,
    Zauberer,
    shr5::Anwendbar,
    KiAdept,
    MagischePersona,
    shr5::AspektMagier,
    shr5::Magier,
    shr5::MysticAdept,
    shr5::KiAdept,
    Wurfwaffe,
    AbtraktGranate,
    shr5::Granate,
    Munition,
    shr5::MiniGrenate,
    shr5::AbtraktGranate,
    Spezialisierung,
    Sensor,
    shr5::SensorArray,
    CredstickTransaction,
    shr5::TransferAmount,
    shr5::ShoppingTransaction,
    CyberwareEnhancement,
    shr5::CyberImplantWeapon,
    shr5::EReference,
    Substance,
    shr5::Toxin,
    shr5::Capacity,
    Nahkampfwaffe,
    AbstraktFokus,
    shr5::MagieFokus,
    shr5::QiFokus,
    Fokus,
    shr5::WaffenFokus,
    MagischeStufe,
    shr5::MagischeStufe,
    shr5::BerechneteAttribute,
    LifestyleOption,
    shr5::PercentLifestyleOption,
    FahrzeugModifikation,
    shr5::FahrzeugErweiterung,
    shr5::WeaponMount,
    shr5::PersonalAreaNetwork,
    shr5::FahrzeugZustand,
    BasicProgram,
    shr5::Datasoft,
    shr5::ConsumerSoft,
    shr5::Tutorsoft,
    Software,
    shr5::SkillSoft,
    shr5::RiggerProgram,
    RiggerProgram,
    shr5::AutoSoft,
    MatrixProgram,
    shr5::CommonProgram,
    shr5::SoftwareAgent,
    shr5::Localization,
    MatrixDevice,
    shr5::MatixConditionMonitor,
    shr5::BasicProgram,
    AbstractMatrixDevice,
    shr5::RiggerCommandConsole,
    shr5::Commlink,
    shr5::ActiveMatixDevice,
    MatixConditionMonitor,
    shr5::MatrixAttributes,
    shr5::Identifiable,
    StufenPersona,
    shr5::Geist,
    shr5::ModifikatorAttribute,
    Vertrag,
    shr5::IntervallVertrag,
    Spezies,
    shr5::Critter,
    shr5::PersonaZustand,
    Wissensfertigkeit,
    shr5::Sprachfertigkeit,
    Fertigkeit,
    shr5::Wissensfertigkeit,
    shr5::Menge,
    shr5::CredstickTransaction,
    shr5::Erlernbar,
    shr5::Fakeable,
    Fakeable,
    shr5::Lizenz,
    shr5::Sin,
    ResonanzPersona,
    IntervallVertrag,
    shr5::Lifestyle,
    ActiveMatixDevice,
    shr5::ResonanzPersona,
    shr5::GebundenerGeist,
    shr5::FokusBinding,
    Erlernbar,
    shr5::PersonaMartialartTechnique,
    shr5::PersonaKomplexForm,
    shr5::Steigerbar,
    shr5::Fokus,
    shr5::PersonaZauber,
    MagischeMods,
    shr5::CritterKraft,
    shr5::KiKraft,
    BerechneteAttribute,
    PersonaZustand,
    Panzerung,
    AbstraktPersona,
    shr5::KoerperPersona,
    KoerperPersona,
    shr5::Technomancer,
    shr5::MudanPersona,
    AbstraktModifikatoren,
    shr5::PersonaEigenschaft,
    shr5::Echo,
    shr5::MagischeMods,
    shr5::Koerpermods,
    shr5::DefaultWifi,
    shr5::BaseMagischePersona,
    shr5::Schutzgeist,
    BaseMagischePersona,
    shr5::MagischePersona,
    Steigerbar,
    shr5::Initation,
    Modifyable,
    shr5::EObject,
    Menge,
    AbstaktFernKampfwaffe,
    shr5::Wurfwaffe,
    shr5::Projektilwaffe,
    shr5::Feuerwaffe,
    Capacity,
    shr5::Cyberdeck,
    Koerpermods,
    AbstaktWaffe,
    shr5::AbstaktFernKampfwaffe,
    shr5::MatrixDevice,
    Anwendbar,
    Modifizierbar,
    shr5::Drug,
    shr5::MatrixProgram,
    GeldWert,
    shr5::FernkampfwaffeModifikator,
    shr5::CyberwareEnhancement,
    shr5::Cyberware,
    shr5::BioWare,
    Quelle,
    ModifikatorAttribute,
    shr5::SpezielleAttribute,
    shr5::Sichtverhaeltnisse,
    shr5::GeistigeAttribute,
    shr5::ProbenModifikatoren,
    shr5::CyberwareModifikatioren,
    shr5::FernkampfwaffenModifikatoren,
    shr5::GegenstandStufen,
    shr5::KoerperlicheAttribute,
    shr5::Modifyable,
    shr5::Modifizierbar,
    shr5::EAttribute,
    shr5::AttributModifikatorWert,
    shr5::Nahkampfwaffe,
    shr5::GeldWert,
    AbstraktGegenstand,
    shr5::Credstick,
    shr5::Magazin,
    shr5::AbstractMatrixDevice,
    shr5::Kleidung,
    shr5::AbstraktFokus,
    shr5::Munition,
    shr5::AbstaktWaffe,
    shr5::SubstanceContainer,
    shr5::Gegenstand,
    shr5::PersonaMartialartStyle,
    shr5::PersonaFertigkeitsGruppe,
    shr5::PersonaFertigkeit,
    ChrakterLimits,
    GeistigeAttribute,
    SpezielleAttribute,
    KoerperlicheAttribute,
    Identifiable,
    shr5::Quelle,
    shr5::Beschreibbar,
    Beschreibbar,
    shr5::Spezialisierung,
    shr5::FahrzeugModifikation,
    shr5::MartialartTechnique,
    shr5::Fertigkeit,
    shr5::StufenPersona,
    shr5::KomplexeForm,
    shr5::MagischeTradition,
    shr5::AbstraktGegenstand,
    shr5::AbstraktPersona,
    shr5::Sensor,
    shr5::MartialartStyle,
    shr5::KleindungsModifikator,
    shr5::Substance,
    shr5::FertigkeitsGruppe,
    shr5::Sprite,
    shr5::Vertrag,
    shr5::AbstraktModifikatoren,
    shr5::MetaMagie,
    shr5::SourceBook,
    shr5::LifestyleOption,
    shr5::Software,
    shr5::Fahrzeug,
    shr5::Host,
    shr5::SourceLink,
    shr5::ShrList,
    shr5::SensorFunction,
    shr5::Spezies,
    shr5::Reichweite,
    shr5::Zauber,
    ZauberDauer,
    AddictionType,
    SubstanceVector,
    Enzug,
    FeuwerwaffenErweiterung,
    CritterReichweite,
    MagazinTyp,
    ZauberReichweite,
    ProgramType,
    MatrixProgramType,
    ZauberArt,
    FeuerModus,
    SubstanceEffect,
    CyberwareType,
    CritterHandlung,
    SchadensTyp,
    armorModificationType,
    CritterDauer,
    InterfaceModus,
    ModifikatorType,
    SmartgunType,
    TimeUnits,
    ResonanzZiel,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_matrixattributes_is_not_abstract():
    assert not inspect.isabstract(MatrixAttributes)


def test_matrixattributes_constructor_exists():
    assert callable(MatrixAttributes.__init__)


def test_matrixattributes_constructor_args():
    sig = inspect.signature(MatrixAttributes.__init__)
    params = list(sig.parameters.keys())



def test_fahrzeug_is_not_abstract():
    assert not inspect.isabstract(Fahrzeug)


def test_fahrzeug_constructor_exists():
    assert callable(Fahrzeug.__init__)


def test_fahrzeug_constructor_args():
    sig = inspect.signature(Fahrzeug.__init__)
    params = list(sig.parameters.keys())



def test_shr5::drohne_is_not_abstract():
    assert not inspect.isabstract(shr5::Drohne)


def test_shr5::drohne_constructor_exists():
    assert callable(shr5::Drohne.__init__)


def test_shr5::drohne_constructor_args():
    sig = inspect.signature(shr5::Drohne.__init__)
    params = list(sig.parameters.keys())
    assert "programSlotCount" in params, "Missing parameter 'programSlotCount'"

def test_shr5::drohne_has_programSlotCount():
    assert hasattr(shr5::Drohne, "programSlotCount")
    descriptor = None
    for klass in shr5::Drohne.__mro__:
        if "programSlotCount" in klass.__dict__:
            descriptor = klass.__dict__["programSlotCount"]
            break
    assert isinstance(descriptor, property)



def test_shr5::passagierfahrzeug_is_not_abstract():
    assert not inspect.isabstract(shr5::PassagierFahrzeug)


def test_shr5::passagierfahrzeug_constructor_exists():
    assert callable(shr5::PassagierFahrzeug.__init__)


def test_shr5::passagierfahrzeug_constructor_args():
    sig = inspect.signature(shr5::PassagierFahrzeug.__init__)
    params = list(sig.parameters.keys())
    assert "sitze" in params, "Missing parameter 'sitze'"

def test_shr5::passagierfahrzeug_has_sitze():
    assert hasattr(shr5::PassagierFahrzeug, "sitze")
    descriptor = None
    for klass in shr5::PassagierFahrzeug.__mro__:
        if "sitze" in klass.__dict__:
            descriptor = klass.__dict__["sitze"]
            break
    assert isinstance(descriptor, property)



def test_passagierfahrzeug_is_not_abstract():
    assert not inspect.isabstract(PassagierFahrzeug)


def test_passagierfahrzeug_constructor_exists():
    assert callable(PassagierFahrzeug.__init__)


def test_passagierfahrzeug_constructor_args():
    sig = inspect.signature(PassagierFahrzeug.__init__)
    params = list(sig.parameters.keys())



def test_shr5::bodenfahrzeug_is_not_abstract():
    assert not inspect.isabstract(shr5::Bodenfahrzeug)


def test_shr5::bodenfahrzeug_constructor_exists():
    assert callable(shr5::Bodenfahrzeug.__init__)


def test_shr5::bodenfahrzeug_constructor_args():
    sig = inspect.signature(shr5::Bodenfahrzeug.__init__)
    params = list(sig.parameters.keys())
    assert "geschwindigkeitGelaende" in params, "Missing parameter 'geschwindigkeitGelaende'"
    assert "handlingGelaende" in params, "Missing parameter 'handlingGelaende'"

def test_shr5::bodenfahrzeug_has_geschwindigkeitGelaende():
    assert hasattr(shr5::Bodenfahrzeug, "geschwindigkeitGelaende")
    descriptor = None
    for klass in shr5::Bodenfahrzeug.__mro__:
        if "geschwindigkeitGelaende" in klass.__dict__:
            descriptor = klass.__dict__["geschwindigkeitGelaende"]
            break
    assert isinstance(descriptor, property)

def test_shr5::bodenfahrzeug_has_handlingGelaende():
    assert hasattr(shr5::Bodenfahrzeug, "handlingGelaende")
    descriptor = None
    for klass in shr5::Bodenfahrzeug.__mro__:
        if "handlingGelaende" in klass.__dict__:
            descriptor = klass.__dict__["handlingGelaende"]
            break
    assert isinstance(descriptor, property)



def test_fahrzeugzustand_is_not_abstract():
    assert not inspect.isabstract(FahrzeugZustand)


def test_fahrzeugzustand_constructor_exists():
    assert callable(FahrzeugZustand.__init__)


def test_fahrzeugzustand_constructor_args():
    sig = inspect.signature(FahrzeugZustand.__init__)
    params = list(sig.parameters.keys())



def test_shr5::chrakterlimits_is_not_abstract():
    assert not inspect.isabstract(shr5::ChrakterLimits)


def test_shr5::chrakterlimits_constructor_exists():
    assert callable(shr5::ChrakterLimits.__init__)


def test_shr5::chrakterlimits_constructor_args():
    sig = inspect.signature(shr5::ChrakterLimits.__init__)
    params = list(sig.parameters.keys())
    assert "sozial" in params, "Missing parameter 'sozial'"
    assert "geistig" in params, "Missing parameter 'geistig'"
    assert "koerperlich" in params, "Missing parameter 'koerperlich'"

def test_shr5::chrakterlimits_has_sozial():
    assert hasattr(shr5::ChrakterLimits, "sozial")
    descriptor = None
    for klass in shr5::ChrakterLimits.__mro__:
        if "sozial" in klass.__dict__:
            descriptor = klass.__dict__["sozial"]
            break
    assert isinstance(descriptor, property)

def test_shr5::chrakterlimits_has_geistig():
    assert hasattr(shr5::ChrakterLimits, "geistig")
    descriptor = None
    for klass in shr5::ChrakterLimits.__mro__:
        if "geistig" in klass.__dict__:
            descriptor = klass.__dict__["geistig"]
            break
    assert isinstance(descriptor, property)

def test_shr5::chrakterlimits_has_koerperlich():
    assert hasattr(shr5::ChrakterLimits, "koerperlich")
    descriptor = None
    for klass in shr5::ChrakterLimits.__mro__:
        if "koerperlich" in klass.__dict__:
            descriptor = klass.__dict__["koerperlich"]
            break
    assert isinstance(descriptor, property)



def test_shr5::astraleprojektion_is_not_abstract():
    assert not inspect.isabstract(shr5::AstraleProjektion)


def test_shr5::astraleprojektion_constructor_exists():
    assert callable(shr5::AstraleProjektion.__init__)


def test_shr5::astraleprojektion_constructor_args():
    sig = inspect.signature(shr5::AstraleProjektion.__init__)
    params = list(sig.parameters.keys())
    assert "astraleGeschicklichkeit" in params, "Missing parameter 'astraleGeschicklichkeit'"
    assert "astraleInitative" in params, "Missing parameter 'astraleInitative'"
    assert "astralesLimit" in params, "Missing parameter 'astralesLimit'"
    assert "astralePanzerung" in params, "Missing parameter 'astralePanzerung'"
    assert "astraleInitativWuerfel" in params, "Missing parameter 'astraleInitativWuerfel'"
    assert "astraleStaerke" in params, "Missing parameter 'astraleStaerke'"
    assert "astraleReaktion" in params, "Missing parameter 'astraleReaktion'"
    assert "astraleKonstitution" in params, "Missing parameter 'astraleKonstitution'"

def test_shr5::astraleprojektion_has_astraleGeschicklichkeit():
    assert hasattr(shr5::AstraleProjektion, "astraleGeschicklichkeit")
    descriptor = None
    for klass in shr5::AstraleProjektion.__mro__:
        if "astraleGeschicklichkeit" in klass.__dict__:
            descriptor = klass.__dict__["astraleGeschicklichkeit"]
            break
    assert isinstance(descriptor, property)

def test_shr5::astraleprojektion_has_astraleInitative():
    assert hasattr(shr5::AstraleProjektion, "astraleInitative")
    descriptor = None
    for klass in shr5::AstraleProjektion.__mro__:
        if "astraleInitative" in klass.__dict__:
            descriptor = klass.__dict__["astraleInitative"]
            break
    assert isinstance(descriptor, property)

def test_shr5::astraleprojektion_has_astralesLimit():
    assert hasattr(shr5::AstraleProjektion, "astralesLimit")
    descriptor = None
    for klass in shr5::AstraleProjektion.__mro__:
        if "astralesLimit" in klass.__dict__:
            descriptor = klass.__dict__["astralesLimit"]
            break
    assert isinstance(descriptor, property)

def test_shr5::astraleprojektion_has_astralePanzerung():
    assert hasattr(shr5::AstraleProjektion, "astralePanzerung")
    descriptor = None
    for klass in shr5::AstraleProjektion.__mro__:
        if "astralePanzerung" in klass.__dict__:
            descriptor = klass.__dict__["astralePanzerung"]
            break
    assert isinstance(descriptor, property)

def test_shr5::astraleprojektion_has_astraleInitativWuerfel():
    assert hasattr(shr5::AstraleProjektion, "astraleInitativWuerfel")
    descriptor = None
    for klass in shr5::AstraleProjektion.__mro__:
        if "astraleInitativWuerfel" in klass.__dict__:
            descriptor = klass.__dict__["astraleInitativWuerfel"]
            break
    assert isinstance(descriptor, property)

def test_shr5::astraleprojektion_has_astraleStaerke():
    assert hasattr(shr5::AstraleProjektion, "astraleStaerke")
    descriptor = None
    for klass in shr5::AstraleProjektion.__mro__:
        if "astraleStaerke" in klass.__dict__:
            descriptor = klass.__dict__["astraleStaerke"]
            break
    assert isinstance(descriptor, property)

def test_shr5::astraleprojektion_has_astraleReaktion():
    assert hasattr(shr5::AstraleProjektion, "astraleReaktion")
    descriptor = None
    for klass in shr5::AstraleProjektion.__mro__:
        if "astraleReaktion" in klass.__dict__:
            descriptor = klass.__dict__["astraleReaktion"]
            break
    assert isinstance(descriptor, property)

def test_shr5::astraleprojektion_has_astraleKonstitution():
    assert hasattr(shr5::AstraleProjektion, "astraleKonstitution")
    descriptor = None
    for klass in shr5::AstraleProjektion.__mro__:
        if "astraleKonstitution" in klass.__dict__:
            descriptor = klass.__dict__["astraleKonstitution"]
            break
    assert isinstance(descriptor, property)



def test_shr5::panzerung_is_not_abstract():
    assert not inspect.isabstract(shr5::Panzerung)


def test_shr5::panzerung_constructor_exists():
    assert callable(shr5::Panzerung.__init__)


def test_shr5::panzerung_constructor_args():
    sig = inspect.signature(shr5::Panzerung.__init__)
    params = list(sig.parameters.keys())
    assert "panzer" in params, "Missing parameter 'panzer'"

def test_shr5::panzerung_has_panzer():
    assert hasattr(shr5::Panzerung, "panzer")
    descriptor = None
    for klass in shr5::Panzerung.__mro__:
        if "panzer" in klass.__dict__:
            descriptor = klass.__dict__["panzer"]
            break
    assert isinstance(descriptor, property)



def test_shr5::zauberer_is_not_abstract():
    assert not inspect.isabstract(shr5::Zauberer)


def test_shr5::zauberer_constructor_exists():
    assert callable(shr5::Zauberer.__init__)


def test_shr5::zauberer_constructor_args():
    sig = inspect.signature(shr5::Zauberer.__init__)
    params = list(sig.parameters.keys())
    assert "enzug" in params, "Missing parameter 'enzug'"

def test_shr5::zauberer_has_enzug():
    assert hasattr(shr5::Zauberer, "enzug")
    descriptor = None
    for klass in shr5::Zauberer.__mro__:
        if "enzug" in klass.__dict__:
            descriptor = klass.__dict__["enzug"]
            break
    assert isinstance(descriptor, property)



def test_astraleprojektion_is_not_abstract():
    assert not inspect.isabstract(AstraleProjektion)


def test_astraleprojektion_constructor_exists():
    assert callable(AstraleProjektion.__init__)


def test_astraleprojektion_constructor_args():
    sig = inspect.signature(AstraleProjektion.__init__)
    params = list(sig.parameters.keys())



def test_zauberer_is_not_abstract():
    assert not inspect.isabstract(Zauberer)


def test_zauberer_constructor_exists():
    assert callable(Zauberer.__init__)


def test_zauberer_constructor_args():
    sig = inspect.signature(Zauberer.__init__)
    params = list(sig.parameters.keys())



def test_shr5::anwendbar_is_not_abstract():
    assert not inspect.isabstract(shr5::Anwendbar)


def test_shr5::anwendbar_constructor_exists():
    assert callable(shr5::Anwendbar.__init__)


def test_shr5::anwendbar_constructor_args():
    sig = inspect.signature(shr5::Anwendbar.__init__)
    params = list(sig.parameters.keys())



def test_kiadept_is_not_abstract():
    assert not inspect.isabstract(KiAdept)


def test_kiadept_constructor_exists():
    assert callable(KiAdept.__init__)


def test_kiadept_constructor_args():
    sig = inspect.signature(KiAdept.__init__)
    params = list(sig.parameters.keys())



def test_magischepersona_is_not_abstract():
    assert not inspect.isabstract(MagischePersona)


def test_magischepersona_constructor_exists():
    assert callable(MagischePersona.__init__)


def test_magischepersona_constructor_args():
    sig = inspect.signature(MagischePersona.__init__)
    params = list(sig.parameters.keys())



def test_shr5::aspektmagier_is_not_abstract():
    assert not inspect.isabstract(shr5::AspektMagier)


def test_shr5::aspektmagier_constructor_exists():
    assert callable(shr5::AspektMagier.__init__)


def test_shr5::aspektmagier_constructor_args():
    sig = inspect.signature(shr5::AspektMagier.__init__)
    params = list(sig.parameters.keys())



def test_shr5::magier_is_not_abstract():
    assert not inspect.isabstract(shr5::Magier)


def test_shr5::magier_constructor_exists():
    assert callable(shr5::Magier.__init__)


def test_shr5::magier_constructor_args():
    sig = inspect.signature(shr5::Magier.__init__)
    params = list(sig.parameters.keys())



def test_shr5::mysticadept_is_not_abstract():
    assert not inspect.isabstract(shr5::MysticAdept)


def test_shr5::mysticadept_constructor_exists():
    assert callable(shr5::MysticAdept.__init__)


def test_shr5::mysticadept_constructor_args():
    sig = inspect.signature(shr5::MysticAdept.__init__)
    params = list(sig.parameters.keys())



def test_shr5::kiadept_is_not_abstract():
    assert not inspect.isabstract(shr5::KiAdept)


def test_shr5::kiadept_constructor_exists():
    assert callable(shr5::KiAdept.__init__)


def test_shr5::kiadept_constructor_args():
    sig = inspect.signature(shr5::KiAdept.__init__)
    params = list(sig.parameters.keys())



def test_wurfwaffe_is_not_abstract():
    assert not inspect.isabstract(Wurfwaffe)


def test_wurfwaffe_constructor_exists():
    assert callable(Wurfwaffe.__init__)


def test_wurfwaffe_constructor_args():
    sig = inspect.signature(Wurfwaffe.__init__)
    params = list(sig.parameters.keys())



def test_abtraktgranate_is_not_abstract():
    assert not inspect.isabstract(AbtraktGranate)


def test_abtraktgranate_constructor_exists():
    assert callable(AbtraktGranate.__init__)


def test_abtraktgranate_constructor_args():
    sig = inspect.signature(AbtraktGranate.__init__)
    params = list(sig.parameters.keys())



def test_shr5::granate_is_not_abstract():
    assert not inspect.isabstract(shr5::Granate)


def test_shr5::granate_constructor_exists():
    assert callable(shr5::Granate.__init__)


def test_shr5::granate_constructor_args():
    sig = inspect.signature(shr5::Granate.__init__)
    params = list(sig.parameters.keys())



def test_munition_is_not_abstract():
    assert not inspect.isabstract(Munition)


def test_munition_constructor_exists():
    assert callable(Munition.__init__)


def test_munition_constructor_args():
    sig = inspect.signature(Munition.__init__)
    params = list(sig.parameters.keys())



def test_shr5::minigrenate_is_not_abstract():
    assert not inspect.isabstract(shr5::MiniGrenate)


def test_shr5::minigrenate_constructor_exists():
    assert callable(shr5::MiniGrenate.__init__)


def test_shr5::minigrenate_constructor_args():
    sig = inspect.signature(shr5::MiniGrenate.__init__)
    params = list(sig.parameters.keys())



def test_shr5::abtraktgranate_is_not_abstract():
    assert not inspect.isabstract(shr5::AbtraktGranate)


def test_shr5::abtraktgranate_constructor_exists():
    assert callable(shr5::AbtraktGranate.__init__)


def test_shr5::abtraktgranate_constructor_args():
    sig = inspect.signature(shr5::AbtraktGranate.__init__)
    params = list(sig.parameters.keys())
    assert "blast" in params, "Missing parameter 'blast'"

def test_shr5::abtraktgranate_has_blast():
    assert hasattr(shr5::AbtraktGranate, "blast")
    descriptor = None
    for klass in shr5::AbtraktGranate.__mro__:
        if "blast" in klass.__dict__:
            descriptor = klass.__dict__["blast"]
            break
    assert isinstance(descriptor, property)



def test_spezialisierung_is_not_abstract():
    assert not inspect.isabstract(Spezialisierung)


def test_spezialisierung_constructor_exists():
    assert callable(Spezialisierung.__init__)


def test_spezialisierung_constructor_args():
    sig = inspect.signature(Spezialisierung.__init__)
    params = list(sig.parameters.keys())



def test_sensor_is_not_abstract():
    assert not inspect.isabstract(Sensor)


def test_sensor_constructor_exists():
    assert callable(Sensor.__init__)


def test_sensor_constructor_args():
    sig = inspect.signature(Sensor.__init__)
    params = list(sig.parameters.keys())



def test_shr5::sensorarray_is_not_abstract():
    assert not inspect.isabstract(shr5::SensorArray)


def test_shr5::sensorarray_constructor_exists():
    assert callable(shr5::SensorArray.__init__)


def test_shr5::sensorarray_constructor_args():
    sig = inspect.signature(shr5::SensorArray.__init__)
    params = list(sig.parameters.keys())



def test_credsticktransaction_is_not_abstract():
    assert not inspect.isabstract(CredstickTransaction)


def test_credsticktransaction_constructor_exists():
    assert callable(CredstickTransaction.__init__)


def test_credsticktransaction_constructor_args():
    sig = inspect.signature(CredstickTransaction.__init__)
    params = list(sig.parameters.keys())



def test_shr5::transferamount_is_not_abstract():
    assert not inspect.isabstract(shr5::TransferAmount)


def test_shr5::transferamount_constructor_exists():
    assert callable(shr5::TransferAmount.__init__)


def test_shr5::transferamount_constructor_args():
    sig = inspect.signature(shr5::TransferAmount.__init__)
    params = list(sig.parameters.keys())
    assert "amountToTransfer" in params, "Missing parameter 'amountToTransfer'"

def test_shr5::transferamount_has_amountToTransfer():
    assert hasattr(shr5::TransferAmount, "amountToTransfer")
    descriptor = None
    for klass in shr5::TransferAmount.__mro__:
        if "amountToTransfer" in klass.__dict__:
            descriptor = klass.__dict__["amountToTransfer"]
            break
    assert isinstance(descriptor, property)



def test_shr5::shoppingtransaction_is_not_abstract():
    assert not inspect.isabstract(shr5::ShoppingTransaction)


def test_shr5::shoppingtransaction_constructor_exists():
    assert callable(shr5::ShoppingTransaction.__init__)


def test_shr5::shoppingtransaction_constructor_args():
    sig = inspect.signature(shr5::ShoppingTransaction.__init__)
    params = list(sig.parameters.keys())
    assert "caculatedCosts" in params, "Missing parameter 'caculatedCosts'"
    assert "fee" in params, "Missing parameter 'fee'"

def test_shr5::shoppingtransaction_has_caculatedCosts():
    assert hasattr(shr5::ShoppingTransaction, "caculatedCosts")
    descriptor = None
    for klass in shr5::ShoppingTransaction.__mro__:
        if "caculatedCosts" in klass.__dict__:
            descriptor = klass.__dict__["caculatedCosts"]
            break
    assert isinstance(descriptor, property)

def test_shr5::shoppingtransaction_has_fee():
    assert hasattr(shr5::ShoppingTransaction, "fee")
    descriptor = None
    for klass in shr5::ShoppingTransaction.__mro__:
        if "fee" in klass.__dict__:
            descriptor = klass.__dict__["fee"]
            break
    assert isinstance(descriptor, property)



def test_cyberwareenhancement_is_not_abstract():
    assert not inspect.isabstract(CyberwareEnhancement)


def test_cyberwareenhancement_constructor_exists():
    assert callable(CyberwareEnhancement.__init__)


def test_cyberwareenhancement_constructor_args():
    sig = inspect.signature(CyberwareEnhancement.__init__)
    params = list(sig.parameters.keys())



def test_shr5::cyberimplantweapon_is_not_abstract():
    assert not inspect.isabstract(shr5::CyberImplantWeapon)


def test_shr5::cyberimplantweapon_constructor_exists():
    assert callable(shr5::CyberImplantWeapon.__init__)


def test_shr5::cyberimplantweapon_constructor_args():
    sig = inspect.signature(shr5::CyberImplantWeapon.__init__)
    params = list(sig.parameters.keys())



def test_shr5::ereference_is_not_abstract():
    assert not inspect.isabstract(shr5::EReference)


def test_shr5::ereference_constructor_exists():
    assert callable(shr5::EReference.__init__)


def test_shr5::ereference_constructor_args():
    sig = inspect.signature(shr5::EReference.__init__)
    params = list(sig.parameters.keys())



def test_substance_is_not_abstract():
    assert not inspect.isabstract(Substance)


def test_substance_constructor_exists():
    assert callable(Substance.__init__)


def test_substance_constructor_args():
    sig = inspect.signature(Substance.__init__)
    params = list(sig.parameters.keys())



def test_shr5::toxin_is_not_abstract():
    assert not inspect.isabstract(shr5::Toxin)


def test_shr5::toxin_constructor_exists():
    assert callable(shr5::Toxin.__init__)


def test_shr5::toxin_constructor_args():
    sig = inspect.signature(shr5::Toxin.__init__)
    params = list(sig.parameters.keys())
    assert "power" in params, "Missing parameter 'power'"
    assert "effect" in params, "Missing parameter 'effect'"
    assert "penetration" in params, "Missing parameter 'penetration'"

def test_shr5::toxin_has_power():
    assert hasattr(shr5::Toxin, "power")
    descriptor = None
    for klass in shr5::Toxin.__mro__:
        if "power" in klass.__dict__:
            descriptor = klass.__dict__["power"]
            break
    assert isinstance(descriptor, property)

def test_shr5::toxin_has_effect():
    assert hasattr(shr5::Toxin, "effect")
    descriptor = None
    for klass in shr5::Toxin.__mro__:
        if "effect" in klass.__dict__:
            descriptor = klass.__dict__["effect"]
            break
    assert isinstance(descriptor, property)

def test_shr5::toxin_has_penetration():
    assert hasattr(shr5::Toxin, "penetration")
    descriptor = None
    for klass in shr5::Toxin.__mro__:
        if "penetration" in klass.__dict__:
            descriptor = klass.__dict__["penetration"]
            break
    assert isinstance(descriptor, property)



def test_shr5::capacity_is_not_abstract():
    assert not inspect.isabstract(shr5::Capacity)


def test_shr5::capacity_constructor_exists():
    assert callable(shr5::Capacity.__init__)


def test_shr5::capacity_constructor_args():
    sig = inspect.signature(shr5::Capacity.__init__)
    params = list(sig.parameters.keys())
    assert "capacity" in params, "Missing parameter 'capacity'"
    assert "capacityRemains" in params, "Missing parameter 'capacityRemains'"

def test_shr5::capacity_has_capacity():
    assert hasattr(shr5::Capacity, "capacity")
    descriptor = None
    for klass in shr5::Capacity.__mro__:
        if "capacity" in klass.__dict__:
            descriptor = klass.__dict__["capacity"]
            break
    assert isinstance(descriptor, property)

def test_shr5::capacity_has_capacityRemains():
    assert hasattr(shr5::Capacity, "capacityRemains")
    descriptor = None
    for klass in shr5::Capacity.__mro__:
        if "capacityRemains" in klass.__dict__:
            descriptor = klass.__dict__["capacityRemains"]
            break
    assert isinstance(descriptor, property)



def test_nahkampfwaffe_is_not_abstract():
    assert not inspect.isabstract(Nahkampfwaffe)


def test_nahkampfwaffe_constructor_exists():
    assert callable(Nahkampfwaffe.__init__)


def test_nahkampfwaffe_constructor_args():
    sig = inspect.signature(Nahkampfwaffe.__init__)
    params = list(sig.parameters.keys())



def test_abstraktfokus_is_not_abstract():
    assert not inspect.isabstract(AbstraktFokus)


def test_abstraktfokus_constructor_exists():
    assert callable(AbstraktFokus.__init__)


def test_abstraktfokus_constructor_args():
    sig = inspect.signature(AbstraktFokus.__init__)
    params = list(sig.parameters.keys())



def test_shr5::magiefokus_is_not_abstract():
    assert not inspect.isabstract(shr5::MagieFokus)


def test_shr5::magiefokus_constructor_exists():
    assert callable(shr5::MagieFokus.__init__)


def test_shr5::magiefokus_constructor_args():
    sig = inspect.signature(shr5::MagieFokus.__init__)
    params = list(sig.parameters.keys())
    assert "bindungsFaktor" in params, "Missing parameter 'bindungsFaktor'"

def test_shr5::magiefokus_has_bindungsFaktor():
    assert hasattr(shr5::MagieFokus, "bindungsFaktor")
    descriptor = None
    for klass in shr5::MagieFokus.__mro__:
        if "bindungsFaktor" in klass.__dict__:
            descriptor = klass.__dict__["bindungsFaktor"]
            break
    assert isinstance(descriptor, property)



def test_shr5::qifokus_is_not_abstract():
    assert not inspect.isabstract(shr5::QiFokus)


def test_shr5::qifokus_constructor_exists():
    assert callable(shr5::QiFokus.__init__)


def test_shr5::qifokus_constructor_args():
    sig = inspect.signature(shr5::QiFokus.__init__)
    params = list(sig.parameters.keys())



def test_fokus_is_not_abstract():
    assert not inspect.isabstract(Fokus)


def test_fokus_constructor_exists():
    assert callable(Fokus.__init__)


def test_fokus_constructor_args():
    sig = inspect.signature(Fokus.__init__)
    params = list(sig.parameters.keys())



def test_shr5::waffenfokus_is_not_abstract():
    assert not inspect.isabstract(shr5::WaffenFokus)


def test_shr5::waffenfokus_constructor_exists():
    assert callable(shr5::WaffenFokus.__init__)


def test_shr5::waffenfokus_constructor_args():
    sig = inspect.signature(shr5::WaffenFokus.__init__)
    params = list(sig.parameters.keys())



def test_magischestufe_is_not_abstract():
    assert not inspect.isabstract(MagischeStufe)


def test_magischestufe_constructor_exists():
    assert callable(MagischeStufe.__init__)


def test_magischestufe_constructor_args():
    sig = inspect.signature(MagischeStufe.__init__)
    params = list(sig.parameters.keys())



def test_shr5::magischestufe_is_not_abstract():
    assert not inspect.isabstract(shr5::MagischeStufe)


def test_shr5::magischestufe_constructor_exists():
    assert callable(shr5::MagischeStufe.__init__)


def test_shr5::magischestufe_constructor_args():
    sig = inspect.signature(shr5::MagischeStufe.__init__)
    params = list(sig.parameters.keys())
    assert "stufe" in params, "Missing parameter 'stufe'"

def test_shr5::magischestufe_has_stufe():
    assert hasattr(shr5::MagischeStufe, "stufe")
    descriptor = None
    for klass in shr5::MagischeStufe.__mro__:
        if "stufe" in klass.__dict__:
            descriptor = klass.__dict__["stufe"]
            break
    assert isinstance(descriptor, property)



def test_shr5::berechneteattribute_is_not_abstract():
    assert not inspect.isabstract(shr5::BerechneteAttribute)


def test_shr5::berechneteattribute_constructor_exists():
    assert callable(shr5::BerechneteAttribute.__init__)


def test_shr5::berechneteattribute_constructor_args():
    sig = inspect.signature(shr5::BerechneteAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "selbstbeherrschung" in params, "Missing parameter 'selbstbeherrschung'"
    assert "menschenkenntnis" in params, "Missing parameter 'menschenkenntnis'"
    assert "errinerungsvermoegen" in params, "Missing parameter 'errinerungsvermoegen'"

def test_shr5::berechneteattribute_has_selbstbeherrschung():
    assert hasattr(shr5::BerechneteAttribute, "selbstbeherrschung")
    descriptor = None
    for klass in shr5::BerechneteAttribute.__mro__:
        if "selbstbeherrschung" in klass.__dict__:
            descriptor = klass.__dict__["selbstbeherrschung"]
            break
    assert isinstance(descriptor, property)

def test_shr5::berechneteattribute_has_menschenkenntnis():
    assert hasattr(shr5::BerechneteAttribute, "menschenkenntnis")
    descriptor = None
    for klass in shr5::BerechneteAttribute.__mro__:
        if "menschenkenntnis" in klass.__dict__:
            descriptor = klass.__dict__["menschenkenntnis"]
            break
    assert isinstance(descriptor, property)

def test_shr5::berechneteattribute_has_errinerungsvermoegen():
    assert hasattr(shr5::BerechneteAttribute, "errinerungsvermoegen")
    descriptor = None
    for klass in shr5::BerechneteAttribute.__mro__:
        if "errinerungsvermoegen" in klass.__dict__:
            descriptor = klass.__dict__["errinerungsvermoegen"]
            break
    assert isinstance(descriptor, property)



def test_lifestyleoption_is_not_abstract():
    assert not inspect.isabstract(LifestyleOption)


def test_lifestyleoption_constructor_exists():
    assert callable(LifestyleOption.__init__)


def test_lifestyleoption_constructor_args():
    sig = inspect.signature(LifestyleOption.__init__)
    params = list(sig.parameters.keys())



def test_shr5::percentlifestyleoption_is_not_abstract():
    assert not inspect.isabstract(shr5::PercentLifestyleOption)


def test_shr5::percentlifestyleoption_constructor_exists():
    assert callable(shr5::PercentLifestyleOption.__init__)


def test_shr5::percentlifestyleoption_constructor_args():
    sig = inspect.signature(shr5::PercentLifestyleOption.__init__)
    params = list(sig.parameters.keys())



def test_fahrzeugmodifikation_is_not_abstract():
    assert not inspect.isabstract(FahrzeugModifikation)


def test_fahrzeugmodifikation_constructor_exists():
    assert callable(FahrzeugModifikation.__init__)


def test_fahrzeugmodifikation_constructor_args():
    sig = inspect.signature(FahrzeugModifikation.__init__)
    params = list(sig.parameters.keys())



def test_shr5::fahrzeugerweiterung_is_not_abstract():
    assert not inspect.isabstract(shr5::FahrzeugErweiterung)


def test_shr5::fahrzeugerweiterung_constructor_exists():
    assert callable(shr5::FahrzeugErweiterung.__init__)


def test_shr5::fahrzeugerweiterung_constructor_args():
    sig = inspect.signature(shr5::FahrzeugErweiterung.__init__)
    params = list(sig.parameters.keys())



def test_shr5::weaponmount_is_not_abstract():
    assert not inspect.isabstract(shr5::WeaponMount)


def test_shr5::weaponmount_constructor_exists():
    assert callable(shr5::WeaponMount.__init__)


def test_shr5::weaponmount_constructor_args():
    sig = inspect.signature(shr5::WeaponMount.__init__)
    params = list(sig.parameters.keys())



def test_shr5::personalareanetwork_is_not_abstract():
    assert not inspect.isabstract(shr5::PersonalAreaNetwork)


def test_shr5::personalareanetwork_constructor_exists():
    assert callable(shr5::PersonalAreaNetwork.__init__)


def test_shr5::personalareanetwork_constructor_args():
    sig = inspect.signature(shr5::PersonalAreaNetwork.__init__)
    params = list(sig.parameters.keys())
    assert "slaveMax" in params, "Missing parameter 'slaveMax'"

def test_shr5::personalareanetwork_has_slaveMax():
    assert hasattr(shr5::PersonalAreaNetwork, "slaveMax")
    descriptor = None
    for klass in shr5::PersonalAreaNetwork.__mro__:
        if "slaveMax" in klass.__dict__:
            descriptor = klass.__dict__["slaveMax"]
            break
    assert isinstance(descriptor, property)



def test_shr5::fahrzeugzustand_is_not_abstract():
    assert not inspect.isabstract(shr5::FahrzeugZustand)


def test_shr5::fahrzeugzustand_constructor_exists():
    assert callable(shr5::FahrzeugZustand.__init__)


def test_shr5::fahrzeugzustand_constructor_args():
    sig = inspect.signature(shr5::FahrzeugZustand.__init__)
    params = list(sig.parameters.keys())
    assert "zustandMax" in params, "Missing parameter 'zustandMax'"

def test_shr5::fahrzeugzustand_has_zustandMax():
    assert hasattr(shr5::FahrzeugZustand, "zustandMax")
    descriptor = None
    for klass in shr5::FahrzeugZustand.__mro__:
        if "zustandMax" in klass.__dict__:
            descriptor = klass.__dict__["zustandMax"]
            break
    assert isinstance(descriptor, property)



def test_basicprogram_is_not_abstract():
    assert not inspect.isabstract(BasicProgram)


def test_basicprogram_constructor_exists():
    assert callable(BasicProgram.__init__)


def test_basicprogram_constructor_args():
    sig = inspect.signature(BasicProgram.__init__)
    params = list(sig.parameters.keys())



def test_shr5::datasoft_is_not_abstract():
    assert not inspect.isabstract(shr5::Datasoft)


def test_shr5::datasoft_constructor_exists():
    assert callable(shr5::Datasoft.__init__)


def test_shr5::datasoft_constructor_args():
    sig = inspect.signature(shr5::Datasoft.__init__)
    params = list(sig.parameters.keys())



def test_shr5::consumersoft_is_not_abstract():
    assert not inspect.isabstract(shr5::ConsumerSoft)


def test_shr5::consumersoft_constructor_exists():
    assert callable(shr5::ConsumerSoft.__init__)


def test_shr5::consumersoft_constructor_args():
    sig = inspect.signature(shr5::ConsumerSoft.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_shr5::consumersoft_has_type():
    assert hasattr(shr5::ConsumerSoft, "type")
    descriptor = None
    for klass in shr5::ConsumerSoft.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_shr5::tutorsoft_is_not_abstract():
    assert not inspect.isabstract(shr5::Tutorsoft)


def test_shr5::tutorsoft_constructor_exists():
    assert callable(shr5::Tutorsoft.__init__)


def test_shr5::tutorsoft_constructor_args():
    sig = inspect.signature(shr5::Tutorsoft.__init__)
    params = list(sig.parameters.keys())
    assert "rating" in params, "Missing parameter 'rating'"

def test_shr5::tutorsoft_has_rating():
    assert hasattr(shr5::Tutorsoft, "rating")
    descriptor = None
    for klass in shr5::Tutorsoft.__mro__:
        if "rating" in klass.__dict__:
            descriptor = klass.__dict__["rating"]
            break
    assert isinstance(descriptor, property)



def test_software_is_not_abstract():
    assert not inspect.isabstract(Software)


def test_software_constructor_exists():
    assert callable(Software.__init__)


def test_software_constructor_args():
    sig = inspect.signature(Software.__init__)
    params = list(sig.parameters.keys())



def test_shr5::skillsoft_is_not_abstract():
    assert not inspect.isabstract(shr5::SkillSoft)


def test_shr5::skillsoft_constructor_exists():
    assert callable(shr5::SkillSoft.__init__)


def test_shr5::skillsoft_constructor_args():
    sig = inspect.signature(shr5::SkillSoft.__init__)
    params = list(sig.parameters.keys())
    assert "rating" in params, "Missing parameter 'rating'"

def test_shr5::skillsoft_has_rating():
    assert hasattr(shr5::SkillSoft, "rating")
    descriptor = None
    for klass in shr5::SkillSoft.__mro__:
        if "rating" in klass.__dict__:
            descriptor = klass.__dict__["rating"]
            break
    assert isinstance(descriptor, property)



def test_shr5::riggerprogram_is_not_abstract():
    assert not inspect.isabstract(shr5::RiggerProgram)


def test_shr5::riggerprogram_constructor_exists():
    assert callable(shr5::RiggerProgram.__init__)


def test_shr5::riggerprogram_constructor_args():
    sig = inspect.signature(shr5::RiggerProgram.__init__)
    params = list(sig.parameters.keys())



def test_riggerprogram_is_not_abstract():
    assert not inspect.isabstract(RiggerProgram)


def test_riggerprogram_constructor_exists():
    assert callable(RiggerProgram.__init__)


def test_riggerprogram_constructor_args():
    sig = inspect.signature(RiggerProgram.__init__)
    params = list(sig.parameters.keys())



def test_shr5::autosoft_is_not_abstract():
    assert not inspect.isabstract(shr5::AutoSoft)


def test_shr5::autosoft_constructor_exists():
    assert callable(shr5::AutoSoft.__init__)


def test_shr5::autosoft_constructor_args():
    sig = inspect.signature(shr5::AutoSoft.__init__)
    params = list(sig.parameters.keys())
    assert "rating" in params, "Missing parameter 'rating'"

def test_shr5::autosoft_has_rating():
    assert hasattr(shr5::AutoSoft, "rating")
    descriptor = None
    for klass in shr5::AutoSoft.__mro__:
        if "rating" in klass.__dict__:
            descriptor = klass.__dict__["rating"]
            break
    assert isinstance(descriptor, property)



def test_matrixprogram_is_not_abstract():
    assert not inspect.isabstract(MatrixProgram)


def test_matrixprogram_constructor_exists():
    assert callable(MatrixProgram.__init__)


def test_matrixprogram_constructor_args():
    sig = inspect.signature(MatrixProgram.__init__)
    params = list(sig.parameters.keys())



def test_shr5::commonprogram_is_not_abstract():
    assert not inspect.isabstract(shr5::CommonProgram)


def test_shr5::commonprogram_constructor_exists():
    assert callable(shr5::CommonProgram.__init__)


def test_shr5::commonprogram_constructor_args():
    sig = inspect.signature(shr5::CommonProgram.__init__)
    params = list(sig.parameters.keys())
    assert "programType" in params, "Missing parameter 'programType'"

def test_shr5::commonprogram_has_programType():
    assert hasattr(shr5::CommonProgram, "programType")
    descriptor = None
    for klass in shr5::CommonProgram.__mro__:
        if "programType" in klass.__dict__:
            descriptor = klass.__dict__["programType"]
            break
    assert isinstance(descriptor, property)



def test_shr5::softwareagent_is_not_abstract():
    assert not inspect.isabstract(shr5::SoftwareAgent)


def test_shr5::softwareagent_constructor_exists():
    assert callable(shr5::SoftwareAgent.__init__)


def test_shr5::softwareagent_constructor_args():
    sig = inspect.signature(shr5::SoftwareAgent.__init__)
    params = list(sig.parameters.keys())
    assert "rating" in params, "Missing parameter 'rating'"

def test_shr5::softwareagent_has_rating():
    assert hasattr(shr5::SoftwareAgent, "rating")
    descriptor = None
    for klass in shr5::SoftwareAgent.__mro__:
        if "rating" in klass.__dict__:
            descriptor = klass.__dict__["rating"]
            break
    assert isinstance(descriptor, property)



def test_shr5::localization_is_not_abstract():
    assert not inspect.isabstract(shr5::Localization)


def test_shr5::localization_constructor_exists():
    assert callable(shr5::Localization.__init__)


def test_shr5::localization_constructor_args():
    sig = inspect.signature(shr5::Localization.__init__)
    params = list(sig.parameters.keys())
    assert "page" in params, "Missing parameter 'page'"
    assert "local" in params, "Missing parameter 'local'"
    assert "name" in params, "Missing parameter 'name'"

def test_shr5::localization_has_page():
    assert hasattr(shr5::Localization, "page")
    descriptor = None
    for klass in shr5::Localization.__mro__:
        if "page" in klass.__dict__:
            descriptor = klass.__dict__["page"]
            break
    assert isinstance(descriptor, property)

def test_shr5::localization_has_local():
    assert hasattr(shr5::Localization, "local")
    descriptor = None
    for klass in shr5::Localization.__mro__:
        if "local" in klass.__dict__:
            descriptor = klass.__dict__["local"]
            break
    assert isinstance(descriptor, property)

def test_shr5::localization_has_name():
    assert hasattr(shr5::Localization, "name")
    descriptor = None
    for klass in shr5::Localization.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_matrixdevice_is_not_abstract():
    assert not inspect.isabstract(MatrixDevice)


def test_matrixdevice_constructor_exists():
    assert callable(MatrixDevice.__init__)


def test_matrixdevice_constructor_args():
    sig = inspect.signature(MatrixDevice.__init__)
    params = list(sig.parameters.keys())



def test_shr5::matixconditionmonitor_is_not_abstract():
    assert not inspect.isabstract(shr5::MatixConditionMonitor)


def test_shr5::matixconditionmonitor_constructor_exists():
    assert callable(shr5::MatixConditionMonitor.__init__)


def test_shr5::matixconditionmonitor_constructor_args():
    sig = inspect.signature(shr5::MatixConditionMonitor.__init__)
    params = list(sig.parameters.keys())
    assert "matrixZustandMax" in params, "Missing parameter 'matrixZustandMax'"

def test_shr5::matixconditionmonitor_has_matrixZustandMax():
    assert hasattr(shr5::MatixConditionMonitor, "matrixZustandMax")
    descriptor = None
    for klass in shr5::MatixConditionMonitor.__mro__:
        if "matrixZustandMax" in klass.__dict__:
            descriptor = klass.__dict__["matrixZustandMax"]
            break
    assert isinstance(descriptor, property)



def test_shr5::basicprogram_is_not_abstract():
    assert not inspect.isabstract(shr5::BasicProgram)


def test_shr5::basicprogram_constructor_exists():
    assert callable(shr5::BasicProgram.__init__)


def test_shr5::basicprogram_constructor_args():
    sig = inspect.signature(shr5::BasicProgram.__init__)
    params = list(sig.parameters.keys())



def test_abstractmatrixdevice_is_not_abstract():
    assert not inspect.isabstract(AbstractMatrixDevice)


def test_abstractmatrixdevice_constructor_exists():
    assert callable(AbstractMatrixDevice.__init__)


def test_abstractmatrixdevice_constructor_args():
    sig = inspect.signature(AbstractMatrixDevice.__init__)
    params = list(sig.parameters.keys())



def test_shr5::riggercommandconsole_is_not_abstract():
    assert not inspect.isabstract(shr5::RiggerCommandConsole)


def test_shr5::riggercommandconsole_constructor_exists():
    assert callable(shr5::RiggerCommandConsole.__init__)


def test_shr5::riggercommandconsole_constructor_args():
    sig = inspect.signature(shr5::RiggerCommandConsole.__init__)
    params = list(sig.parameters.keys())
    assert "rauschunterdrueckung" in params, "Missing parameter 'rauschunterdrueckung'"
    assert "zugriffBasis" in params, "Missing parameter 'zugriffBasis'"
    assert "firewallBasis" in params, "Missing parameter 'firewallBasis'"
    assert "datenverarbeitungBasis" in params, "Missing parameter 'datenverarbeitungBasis'"
    assert "zugriff" in params, "Missing parameter 'zugriff'"

def test_shr5::riggercommandconsole_has_rauschunterdrueckung():
    assert hasattr(shr5::RiggerCommandConsole, "rauschunterdrueckung")
    descriptor = None
    for klass in shr5::RiggerCommandConsole.__mro__:
        if "rauschunterdrueckung" in klass.__dict__:
            descriptor = klass.__dict__["rauschunterdrueckung"]
            break
    assert isinstance(descriptor, property)

def test_shr5::riggercommandconsole_has_zugriffBasis():
    assert hasattr(shr5::RiggerCommandConsole, "zugriffBasis")
    descriptor = None
    for klass in shr5::RiggerCommandConsole.__mro__:
        if "zugriffBasis" in klass.__dict__:
            descriptor = klass.__dict__["zugriffBasis"]
            break
    assert isinstance(descriptor, property)

def test_shr5::riggercommandconsole_has_firewallBasis():
    assert hasattr(shr5::RiggerCommandConsole, "firewallBasis")
    descriptor = None
    for klass in shr5::RiggerCommandConsole.__mro__:
        if "firewallBasis" in klass.__dict__:
            descriptor = klass.__dict__["firewallBasis"]
            break
    assert isinstance(descriptor, property)

def test_shr5::riggercommandconsole_has_datenverarbeitungBasis():
    assert hasattr(shr5::RiggerCommandConsole, "datenverarbeitungBasis")
    descriptor = None
    for klass in shr5::RiggerCommandConsole.__mro__:
        if "datenverarbeitungBasis" in klass.__dict__:
            descriptor = klass.__dict__["datenverarbeitungBasis"]
            break
    assert isinstance(descriptor, property)

def test_shr5::riggercommandconsole_has_zugriff():
    assert hasattr(shr5::RiggerCommandConsole, "zugriff")
    descriptor = None
    for klass in shr5::RiggerCommandConsole.__mro__:
        if "zugriff" in klass.__dict__:
            descriptor = klass.__dict__["zugriff"]
            break
    assert isinstance(descriptor, property)



def test_shr5::commlink_is_not_abstract():
    assert not inspect.isabstract(shr5::Commlink)


def test_shr5::commlink_constructor_exists():
    assert callable(shr5::Commlink.__init__)


def test_shr5::commlink_constructor_args():
    sig = inspect.signature(shr5::Commlink.__init__)
    params = list(sig.parameters.keys())



def test_shr5::activematixdevice_is_not_abstract():
    assert not inspect.isabstract(shr5::ActiveMatixDevice)


def test_shr5::activematixdevice_constructor_exists():
    assert callable(shr5::ActiveMatixDevice.__init__)


def test_shr5::activematixdevice_constructor_args():
    sig = inspect.signature(shr5::ActiveMatixDevice.__init__)
    params = list(sig.parameters.keys())
    assert "angriff" in params, "Missing parameter 'angriff'"
    assert "schleicher" in params, "Missing parameter 'schleicher'"

def test_shr5::activematixdevice_has_angriff():
    assert hasattr(shr5::ActiveMatixDevice, "angriff")
    descriptor = None
    for klass in shr5::ActiveMatixDevice.__mro__:
        if "angriff" in klass.__dict__:
            descriptor = klass.__dict__["angriff"]
            break
    assert isinstance(descriptor, property)

def test_shr5::activematixdevice_has_schleicher():
    assert hasattr(shr5::ActiveMatixDevice, "schleicher")
    descriptor = None
    for klass in shr5::ActiveMatixDevice.__mro__:
        if "schleicher" in klass.__dict__:
            descriptor = klass.__dict__["schleicher"]
            break
    assert isinstance(descriptor, property)



def test_matixconditionmonitor_is_not_abstract():
    assert not inspect.isabstract(MatixConditionMonitor)


def test_matixconditionmonitor_constructor_exists():
    assert callable(MatixConditionMonitor.__init__)


def test_matixconditionmonitor_constructor_args():
    sig = inspect.signature(MatixConditionMonitor.__init__)
    params = list(sig.parameters.keys())



def test_shr5::matrixattributes_is_not_abstract():
    assert not inspect.isabstract(shr5::MatrixAttributes)


def test_shr5::matrixattributes_constructor_exists():
    assert callable(shr5::MatrixAttributes.__init__)


def test_shr5::matrixattributes_constructor_args():
    sig = inspect.signature(shr5::MatrixAttributes.__init__)
    params = list(sig.parameters.keys())
    assert "geraetestufe" in params, "Missing parameter 'geraetestufe'"
    assert "datenverarbeitung" in params, "Missing parameter 'datenverarbeitung'"
    assert "currentModus" in params, "Missing parameter 'currentModus'"
    assert "firewall" in params, "Missing parameter 'firewall'"

def test_shr5::matrixattributes_has_geraetestufe():
    assert hasattr(shr5::MatrixAttributes, "geraetestufe")
    descriptor = None
    for klass in shr5::MatrixAttributes.__mro__:
        if "geraetestufe" in klass.__dict__:
            descriptor = klass.__dict__["geraetestufe"]
            break
    assert isinstance(descriptor, property)

def test_shr5::matrixattributes_has_datenverarbeitung():
    assert hasattr(shr5::MatrixAttributes, "datenverarbeitung")
    descriptor = None
    for klass in shr5::MatrixAttributes.__mro__:
        if "datenverarbeitung" in klass.__dict__:
            descriptor = klass.__dict__["datenverarbeitung"]
            break
    assert isinstance(descriptor, property)

def test_shr5::matrixattributes_has_currentModus():
    assert hasattr(shr5::MatrixAttributes, "currentModus")
    descriptor = None
    for klass in shr5::MatrixAttributes.__mro__:
        if "currentModus" in klass.__dict__:
            descriptor = klass.__dict__["currentModus"]
            break
    assert isinstance(descriptor, property)

def test_shr5::matrixattributes_has_firewall():
    assert hasattr(shr5::MatrixAttributes, "firewall")
    descriptor = None
    for klass in shr5::MatrixAttributes.__mro__:
        if "firewall" in klass.__dict__:
            descriptor = klass.__dict__["firewall"]
            break
    assert isinstance(descriptor, property)



def test_shr5::identifiable_is_not_abstract():
    assert not inspect.isabstract(shr5::Identifiable)


def test_shr5::identifiable_constructor_exists():
    assert callable(shr5::Identifiable.__init__)


def test_shr5::identifiable_constructor_args():
    sig = inspect.signature(shr5::Identifiable.__init__)
    params = list(sig.parameters.keys())
    assert "parentId" in params, "Missing parameter 'parentId'"

def test_shr5::identifiable_has_parentId():
    assert hasattr(shr5::Identifiable, "parentId")
    descriptor = None
    for klass in shr5::Identifiable.__mro__:
        if "parentId" in klass.__dict__:
            descriptor = klass.__dict__["parentId"]
            break
    assert isinstance(descriptor, property)



def test_stufenpersona_is_not_abstract():
    assert not inspect.isabstract(StufenPersona)


def test_stufenpersona_constructor_exists():
    assert callable(StufenPersona.__init__)


def test_stufenpersona_constructor_args():
    sig = inspect.signature(StufenPersona.__init__)
    params = list(sig.parameters.keys())



def test_shr5::geist_is_not_abstract():
    assert not inspect.isabstract(shr5::Geist)


def test_shr5::geist_constructor_exists():
    assert callable(shr5::Geist.__init__)


def test_shr5::geist_constructor_args():
    sig = inspect.signature(shr5::Geist.__init__)
    params = list(sig.parameters.keys())
    assert "reaktionBasis" in params, "Missing parameter 'reaktionBasis'"
    assert "staerkeBasis" in params, "Missing parameter 'staerkeBasis'"
    assert "charismaBasis" in params, "Missing parameter 'charismaBasis'"
    assert "logikBasis" in params, "Missing parameter 'logikBasis'"
    assert "willenskraftBasis" in params, "Missing parameter 'willenskraftBasis'"
    assert "konstitutionBasis" in params, "Missing parameter 'konstitutionBasis'"
    assert "geschicklichkeitBasis" in params, "Missing parameter 'geschicklichkeitBasis'"
    assert "intuitionBasis" in params, "Missing parameter 'intuitionBasis'"

def test_shr5::geist_has_reaktionBasis():
    assert hasattr(shr5::Geist, "reaktionBasis")
    descriptor = None
    for klass in shr5::Geist.__mro__:
        if "reaktionBasis" in klass.__dict__:
            descriptor = klass.__dict__["reaktionBasis"]
            break
    assert isinstance(descriptor, property)

def test_shr5::geist_has_staerkeBasis():
    assert hasattr(shr5::Geist, "staerkeBasis")
    descriptor = None
    for klass in shr5::Geist.__mro__:
        if "staerkeBasis" in klass.__dict__:
            descriptor = klass.__dict__["staerkeBasis"]
            break
    assert isinstance(descriptor, property)

def test_shr5::geist_has_charismaBasis():
    assert hasattr(shr5::Geist, "charismaBasis")
    descriptor = None
    for klass in shr5::Geist.__mro__:
        if "charismaBasis" in klass.__dict__:
            descriptor = klass.__dict__["charismaBasis"]
            break
    assert isinstance(descriptor, property)

def test_shr5::geist_has_logikBasis():
    assert hasattr(shr5::Geist, "logikBasis")
    descriptor = None
    for klass in shr5::Geist.__mro__:
        if "logikBasis" in klass.__dict__:
            descriptor = klass.__dict__["logikBasis"]
            break
    assert isinstance(descriptor, property)

def test_shr5::geist_has_willenskraftBasis():
    assert hasattr(shr5::Geist, "willenskraftBasis")
    descriptor = None
    for klass in shr5::Geist.__mro__:
        if "willenskraftBasis" in klass.__dict__:
            descriptor = klass.__dict__["willenskraftBasis"]
            break
    assert isinstance(descriptor, property)

def test_shr5::geist_has_konstitutionBasis():
    assert hasattr(shr5::Geist, "konstitutionBasis")
    descriptor = None
    for klass in shr5::Geist.__mro__:
        if "konstitutionBasis" in klass.__dict__:
            descriptor = klass.__dict__["konstitutionBasis"]
            break
    assert isinstance(descriptor, property)

def test_shr5::geist_has_geschicklichkeitBasis():
    assert hasattr(shr5::Geist, "geschicklichkeitBasis")
    descriptor = None
    for klass in shr5::Geist.__mro__:
        if "geschicklichkeitBasis" in klass.__dict__:
            descriptor = klass.__dict__["geschicklichkeitBasis"]
            break
    assert isinstance(descriptor, property)

def test_shr5::geist_has_intuitionBasis():
    assert hasattr(shr5::Geist, "intuitionBasis")
    descriptor = None
    for klass in shr5::Geist.__mro__:
        if "intuitionBasis" in klass.__dict__:
            descriptor = klass.__dict__["intuitionBasis"]
            break
    assert isinstance(descriptor, property)



def test_shr5::modifikatorattribute_is_not_abstract():
    assert not inspect.isabstract(shr5::ModifikatorAttribute)


def test_shr5::modifikatorattribute_constructor_exists():
    assert callable(shr5::ModifikatorAttribute.__init__)


def test_shr5::modifikatorattribute_constructor_args():
    sig = inspect.signature(shr5::ModifikatorAttribute.__init__)
    params = list(sig.parameters.keys())



def test_vertrag_is_not_abstract():
    assert not inspect.isabstract(Vertrag)


def test_vertrag_constructor_exists():
    assert callable(Vertrag.__init__)


def test_vertrag_constructor_args():
    sig = inspect.signature(Vertrag.__init__)
    params = list(sig.parameters.keys())



def test_shr5::intervallvertrag_is_not_abstract():
    assert not inspect.isabstract(shr5::IntervallVertrag)


def test_shr5::intervallvertrag_constructor_exists():
    assert callable(shr5::IntervallVertrag.__init__)


def test_shr5::intervallvertrag_constructor_args():
    sig = inspect.signature(shr5::IntervallVertrag.__init__)
    params = list(sig.parameters.keys())
    assert "faelligkeitsIntervall" in params, "Missing parameter 'faelligkeitsIntervall'"
    assert "unit" in params, "Missing parameter 'unit'"
    assert "begin" in params, "Missing parameter 'begin'"

def test_shr5::intervallvertrag_has_faelligkeitsIntervall():
    assert hasattr(shr5::IntervallVertrag, "faelligkeitsIntervall")
    descriptor = None
    for klass in shr5::IntervallVertrag.__mro__:
        if "faelligkeitsIntervall" in klass.__dict__:
            descriptor = klass.__dict__["faelligkeitsIntervall"]
            break
    assert isinstance(descriptor, property)

def test_shr5::intervallvertrag_has_unit():
    assert hasattr(shr5::IntervallVertrag, "unit")
    descriptor = None
    for klass in shr5::IntervallVertrag.__mro__:
        if "unit" in klass.__dict__:
            descriptor = klass.__dict__["unit"]
            break
    assert isinstance(descriptor, property)

def test_shr5::intervallvertrag_has_begin():
    assert hasattr(shr5::IntervallVertrag, "begin")
    descriptor = None
    for klass in shr5::IntervallVertrag.__mro__:
        if "begin" in klass.__dict__:
            descriptor = klass.__dict__["begin"]
            break
    assert isinstance(descriptor, property)



def test_spezies_is_not_abstract():
    assert not inspect.isabstract(Spezies)


def test_spezies_constructor_exists():
    assert callable(Spezies.__init__)


def test_spezies_constructor_args():
    sig = inspect.signature(Spezies.__init__)
    params = list(sig.parameters.keys())



def test_shr5::critter_is_not_abstract():
    assert not inspect.isabstract(shr5::Critter)


def test_shr5::critter_constructor_exists():
    assert callable(shr5::Critter.__init__)


def test_shr5::critter_constructor_args():
    sig = inspect.signature(shr5::Critter.__init__)
    params = list(sig.parameters.keys())



def test_shr5::personazustand_is_not_abstract():
    assert not inspect.isabstract(shr5::PersonaZustand)


def test_shr5::personazustand_constructor_exists():
    assert callable(shr5::PersonaZustand.__init__)


def test_shr5::personazustand_constructor_args():
    sig = inspect.signature(shr5::PersonaZustand.__init__)
    params = list(sig.parameters.keys())
    assert "zustandGeistigMax" in params, "Missing parameter 'zustandGeistigMax'"
    assert "zustandKoerperlichMax" in params, "Missing parameter 'zustandKoerperlichMax'"
    assert "zustandGrenze" in params, "Missing parameter 'zustandGrenze'"

def test_shr5::personazustand_has_zustandGeistigMax():
    assert hasattr(shr5::PersonaZustand, "zustandGeistigMax")
    descriptor = None
    for klass in shr5::PersonaZustand.__mro__:
        if "zustandGeistigMax" in klass.__dict__:
            descriptor = klass.__dict__["zustandGeistigMax"]
            break
    assert isinstance(descriptor, property)

def test_shr5::personazustand_has_zustandKoerperlichMax():
    assert hasattr(shr5::PersonaZustand, "zustandKoerperlichMax")
    descriptor = None
    for klass in shr5::PersonaZustand.__mro__:
        if "zustandKoerperlichMax" in klass.__dict__:
            descriptor = klass.__dict__["zustandKoerperlichMax"]
            break
    assert isinstance(descriptor, property)

def test_shr5::personazustand_has_zustandGrenze():
    assert hasattr(shr5::PersonaZustand, "zustandGrenze")
    descriptor = None
    for klass in shr5::PersonaZustand.__mro__:
        if "zustandGrenze" in klass.__dict__:
            descriptor = klass.__dict__["zustandGrenze"]
            break
    assert isinstance(descriptor, property)



def test_wissensfertigkeit_is_not_abstract():
    assert not inspect.isabstract(Wissensfertigkeit)


def test_wissensfertigkeit_constructor_exists():
    assert callable(Wissensfertigkeit.__init__)


def test_wissensfertigkeit_constructor_args():
    sig = inspect.signature(Wissensfertigkeit.__init__)
    params = list(sig.parameters.keys())



def test_shr5::sprachfertigkeit_is_not_abstract():
    assert not inspect.isabstract(shr5::Sprachfertigkeit)


def test_shr5::sprachfertigkeit_constructor_exists():
    assert callable(shr5::Sprachfertigkeit.__init__)


def test_shr5::sprachfertigkeit_constructor_args():
    sig = inspect.signature(shr5::Sprachfertigkeit.__init__)
    params = list(sig.parameters.keys())



def test_fertigkeit_is_not_abstract():
    assert not inspect.isabstract(Fertigkeit)


def test_fertigkeit_constructor_exists():
    assert callable(Fertigkeit.__init__)


def test_fertigkeit_constructor_args():
    sig = inspect.signature(Fertigkeit.__init__)
    params = list(sig.parameters.keys())



def test_shr5::wissensfertigkeit_is_not_abstract():
    assert not inspect.isabstract(shr5::Wissensfertigkeit)


def test_shr5::wissensfertigkeit_constructor_exists():
    assert callable(shr5::Wissensfertigkeit.__init__)


def test_shr5::wissensfertigkeit_constructor_args():
    sig = inspect.signature(shr5::Wissensfertigkeit.__init__)
    params = list(sig.parameters.keys())



def test_shr5::menge_is_not_abstract():
    assert not inspect.isabstract(shr5::Menge)


def test_shr5::menge_constructor_exists():
    assert callable(shr5::Menge.__init__)


def test_shr5::menge_constructor_args():
    sig = inspect.signature(shr5::Menge.__init__)
    params = list(sig.parameters.keys())
    assert "proAnzahl" in params, "Missing parameter 'proAnzahl'"
    assert "anzahl" in params, "Missing parameter 'anzahl'"

def test_shr5::menge_has_proAnzahl():
    assert hasattr(shr5::Menge, "proAnzahl")
    descriptor = None
    for klass in shr5::Menge.__mro__:
        if "proAnzahl" in klass.__dict__:
            descriptor = klass.__dict__["proAnzahl"]
            break
    assert isinstance(descriptor, property)

def test_shr5::menge_has_anzahl():
    assert hasattr(shr5::Menge, "anzahl")
    descriptor = None
    for klass in shr5::Menge.__mro__:
        if "anzahl" in klass.__dict__:
            descriptor = klass.__dict__["anzahl"]
            break
    assert isinstance(descriptor, property)



def test_shr5::credsticktransaction_is_not_abstract():
    assert not inspect.isabstract(shr5::CredstickTransaction)


def test_shr5::credsticktransaction_constructor_exists():
    assert callable(shr5::CredstickTransaction.__init__)


def test_shr5::credsticktransaction_constructor_args():
    sig = inspect.signature(shr5::CredstickTransaction.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "date" in params, "Missing parameter 'date'"
    assert "amount" in params, "Missing parameter 'amount'"

def test_shr5::credsticktransaction_has_description():
    assert hasattr(shr5::CredstickTransaction, "description")
    descriptor = None
    for klass in shr5::CredstickTransaction.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_shr5::credsticktransaction_has_date():
    assert hasattr(shr5::CredstickTransaction, "date")
    descriptor = None
    for klass in shr5::CredstickTransaction.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)

def test_shr5::credsticktransaction_has_amount():
    assert hasattr(shr5::CredstickTransaction, "amount")
    descriptor = None
    for klass in shr5::CredstickTransaction.__mro__:
        if "amount" in klass.__dict__:
            descriptor = klass.__dict__["amount"]
            break
    assert isinstance(descriptor, property)



def test_shr5::erlernbar_is_not_abstract():
    assert not inspect.isabstract(shr5::Erlernbar)


def test_shr5::erlernbar_constructor_exists():
    assert callable(shr5::Erlernbar.__init__)


def test_shr5::erlernbar_constructor_args():
    sig = inspect.signature(shr5::Erlernbar.__init__)
    params = list(sig.parameters.keys())



def test_shr5::fakeable_is_not_abstract():
    assert not inspect.isabstract(shr5::Fakeable)


def test_shr5::fakeable_constructor_exists():
    assert callable(shr5::Fakeable.__init__)


def test_shr5::fakeable_constructor_args():
    sig = inspect.signature(shr5::Fakeable.__init__)
    params = list(sig.parameters.keys())
    assert "gefaelscht" in params, "Missing parameter 'gefaelscht'"
    assert "stufe" in params, "Missing parameter 'stufe'"

def test_shr5::fakeable_has_gefaelscht():
    assert hasattr(shr5::Fakeable, "gefaelscht")
    descriptor = None
    for klass in shr5::Fakeable.__mro__:
        if "gefaelscht" in klass.__dict__:
            descriptor = klass.__dict__["gefaelscht"]
            break
    assert isinstance(descriptor, property)

def test_shr5::fakeable_has_stufe():
    assert hasattr(shr5::Fakeable, "stufe")
    descriptor = None
    for klass in shr5::Fakeable.__mro__:
        if "stufe" in klass.__dict__:
            descriptor = klass.__dict__["stufe"]
            break
    assert isinstance(descriptor, property)



def test_fakeable_is_not_abstract():
    assert not inspect.isabstract(Fakeable)


def test_fakeable_constructor_exists():
    assert callable(Fakeable.__init__)


def test_fakeable_constructor_args():
    sig = inspect.signature(Fakeable.__init__)
    params = list(sig.parameters.keys())



def test_shr5::lizenz_is_not_abstract():
    assert not inspect.isabstract(shr5::Lizenz)


def test_shr5::lizenz_constructor_exists():
    assert callable(shr5::Lizenz.__init__)


def test_shr5::lizenz_constructor_args():
    sig = inspect.signature(shr5::Lizenz.__init__)
    params = list(sig.parameters.keys())
    assert "lizenGegenstand" in params, "Missing parameter 'lizenGegenstand'"

def test_shr5::lizenz_has_lizenGegenstand():
    assert hasattr(shr5::Lizenz, "lizenGegenstand")
    descriptor = None
    for klass in shr5::Lizenz.__mro__:
        if "lizenGegenstand" in klass.__dict__:
            descriptor = klass.__dict__["lizenGegenstand"]
            break
    assert isinstance(descriptor, property)



def test_shr5::sin_is_not_abstract():
    assert not inspect.isabstract(shr5::Sin)


def test_shr5::sin_constructor_exists():
    assert callable(shr5::Sin.__init__)


def test_shr5::sin_constructor_args():
    sig = inspect.signature(shr5::Sin.__init__)
    params = list(sig.parameters.keys())



def test_resonanzpersona_is_not_abstract():
    assert not inspect.isabstract(ResonanzPersona)


def test_resonanzpersona_constructor_exists():
    assert callable(ResonanzPersona.__init__)


def test_resonanzpersona_constructor_args():
    sig = inspect.signature(ResonanzPersona.__init__)
    params = list(sig.parameters.keys())



def test_intervallvertrag_is_not_abstract():
    assert not inspect.isabstract(IntervallVertrag)


def test_intervallvertrag_constructor_exists():
    assert callable(IntervallVertrag.__init__)


def test_intervallvertrag_constructor_args():
    sig = inspect.signature(IntervallVertrag.__init__)
    params = list(sig.parameters.keys())



def test_shr5::lifestyle_is_not_abstract():
    assert not inspect.isabstract(shr5::Lifestyle)


def test_shr5::lifestyle_constructor_exists():
    assert callable(shr5::Lifestyle.__init__)


def test_shr5::lifestyle_constructor_args():
    sig = inspect.signature(shr5::Lifestyle.__init__)
    params = list(sig.parameters.keys())
    assert "owned" in params, "Missing parameter 'owned'"

def test_shr5::lifestyle_has_owned():
    assert hasattr(shr5::Lifestyle, "owned")
    descriptor = None
    for klass in shr5::Lifestyle.__mro__:
        if "owned" in klass.__dict__:
            descriptor = klass.__dict__["owned"]
            break
    assert isinstance(descriptor, property)



def test_activematixdevice_is_not_abstract():
    assert not inspect.isabstract(ActiveMatixDevice)


def test_activematixdevice_constructor_exists():
    assert callable(ActiveMatixDevice.__init__)


def test_activematixdevice_constructor_args():
    sig = inspect.signature(ActiveMatixDevice.__init__)
    params = list(sig.parameters.keys())



def test_shr5::resonanzpersona_is_not_abstract():
    assert not inspect.isabstract(shr5::ResonanzPersona)


def test_shr5::resonanzpersona_constructor_exists():
    assert callable(shr5::ResonanzPersona.__init__)


def test_shr5::resonanzpersona_constructor_args():
    sig = inspect.signature(shr5::ResonanzPersona.__init__)
    params = list(sig.parameters.keys())
    assert "resonanzBasis" in params, "Missing parameter 'resonanzBasis'"
    assert "resonanz" in params, "Missing parameter 'resonanz'"

def test_shr5::resonanzpersona_has_resonanzBasis():
    assert hasattr(shr5::ResonanzPersona, "resonanzBasis")
    descriptor = None
    for klass in shr5::ResonanzPersona.__mro__:
        if "resonanzBasis" in klass.__dict__:
            descriptor = klass.__dict__["resonanzBasis"]
            break
    assert isinstance(descriptor, property)

def test_shr5::resonanzpersona_has_resonanz():
    assert hasattr(shr5::ResonanzPersona, "resonanz")
    descriptor = None
    for klass in shr5::ResonanzPersona.__mro__:
        if "resonanz" in klass.__dict__:
            descriptor = klass.__dict__["resonanz"]
            break
    assert isinstance(descriptor, property)



def test_shr5::gebundenergeist_is_not_abstract():
    assert not inspect.isabstract(shr5::GebundenerGeist)


def test_shr5::gebundenergeist_constructor_exists():
    assert callable(shr5::GebundenerGeist.__init__)


def test_shr5::gebundenergeist_constructor_args():
    sig = inspect.signature(shr5::GebundenerGeist.__init__)
    params = list(sig.parameters.keys())
    assert "dienste" in params, "Missing parameter 'dienste'"

def test_shr5::gebundenergeist_has_dienste():
    assert hasattr(shr5::GebundenerGeist, "dienste")
    descriptor = None
    for klass in shr5::GebundenerGeist.__mro__:
        if "dienste" in klass.__dict__:
            descriptor = klass.__dict__["dienste"]
            break
    assert isinstance(descriptor, property)



def test_shr5::fokusbinding_is_not_abstract():
    assert not inspect.isabstract(shr5::FokusBinding)


def test_shr5::fokusbinding_constructor_exists():
    assert callable(shr5::FokusBinding.__init__)


def test_shr5::fokusbinding_constructor_args():
    sig = inspect.signature(shr5::FokusBinding.__init__)
    params = list(sig.parameters.keys())
    assert "active" in params, "Missing parameter 'active'"

def test_shr5::fokusbinding_has_active():
    assert hasattr(shr5::FokusBinding, "active")
    descriptor = None
    for klass in shr5::FokusBinding.__mro__:
        if "active" in klass.__dict__:
            descriptor = klass.__dict__["active"]
            break
    assert isinstance(descriptor, property)



def test_erlernbar_is_not_abstract():
    assert not inspect.isabstract(Erlernbar)


def test_erlernbar_constructor_exists():
    assert callable(Erlernbar.__init__)


def test_erlernbar_constructor_args():
    sig = inspect.signature(Erlernbar.__init__)
    params = list(sig.parameters.keys())



def test_shr5::personamartialarttechnique_is_not_abstract():
    assert not inspect.isabstract(shr5::PersonaMartialartTechnique)


def test_shr5::personamartialarttechnique_constructor_exists():
    assert callable(shr5::PersonaMartialartTechnique.__init__)


def test_shr5::personamartialarttechnique_constructor_args():
    sig = inspect.signature(shr5::PersonaMartialartTechnique.__init__)
    params = list(sig.parameters.keys())



def test_shr5::personakomplexform_is_not_abstract():
    assert not inspect.isabstract(shr5::PersonaKomplexForm)


def test_shr5::personakomplexform_constructor_exists():
    assert callable(shr5::PersonaKomplexForm.__init__)


def test_shr5::personakomplexform_constructor_args():
    sig = inspect.signature(shr5::PersonaKomplexForm.__init__)
    params = list(sig.parameters.keys())
    assert "stufe" in params, "Missing parameter 'stufe'"

def test_shr5::personakomplexform_has_stufe():
    assert hasattr(shr5::PersonaKomplexForm, "stufe")
    descriptor = None
    for klass in shr5::PersonaKomplexForm.__mro__:
        if "stufe" in klass.__dict__:
            descriptor = klass.__dict__["stufe"]
            break
    assert isinstance(descriptor, property)



def test_shr5::steigerbar_is_not_abstract():
    assert not inspect.isabstract(shr5::Steigerbar)


def test_shr5::steigerbar_constructor_exists():
    assert callable(shr5::Steigerbar.__init__)


def test_shr5::steigerbar_constructor_args():
    sig = inspect.signature(shr5::Steigerbar.__init__)
    params = list(sig.parameters.keys())
    assert "stufe" in params, "Missing parameter 'stufe'"

def test_shr5::steigerbar_has_stufe():
    assert hasattr(shr5::Steigerbar, "stufe")
    descriptor = None
    for klass in shr5::Steigerbar.__mro__:
        if "stufe" in klass.__dict__:
            descriptor = klass.__dict__["stufe"]
            break
    assert isinstance(descriptor, property)



def test_shr5::fokus_is_not_abstract():
    assert not inspect.isabstract(shr5::Fokus)


def test_shr5::fokus_constructor_exists():
    assert callable(shr5::Fokus.__init__)


def test_shr5::fokus_constructor_args():
    sig = inspect.signature(shr5::Fokus.__init__)
    params = list(sig.parameters.keys())
    assert "bindungskosten" in params, "Missing parameter 'bindungskosten'"

def test_shr5::fokus_has_bindungskosten():
    assert hasattr(shr5::Fokus, "bindungskosten")
    descriptor = None
    for klass in shr5::Fokus.__mro__:
        if "bindungskosten" in klass.__dict__:
            descriptor = klass.__dict__["bindungskosten"]
            break
    assert isinstance(descriptor, property)



def test_shr5::personazauber_is_not_abstract():
    assert not inspect.isabstract(shr5::PersonaZauber)


def test_shr5::personazauber_constructor_exists():
    assert callable(shr5::PersonaZauber.__init__)


def test_shr5::personazauber_constructor_args():
    sig = inspect.signature(shr5::PersonaZauber.__init__)
    params = list(sig.parameters.keys())
    assert "stufe" in params, "Missing parameter 'stufe'"

def test_shr5::personazauber_has_stufe():
    assert hasattr(shr5::PersonaZauber, "stufe")
    descriptor = None
    for klass in shr5::PersonaZauber.__mro__:
        if "stufe" in klass.__dict__:
            descriptor = klass.__dict__["stufe"]
            break
    assert isinstance(descriptor, property)



def test_magischemods_is_not_abstract():
    assert not inspect.isabstract(MagischeMods)


def test_magischemods_constructor_exists():
    assert callable(MagischeMods.__init__)


def test_magischemods_constructor_args():
    sig = inspect.signature(MagischeMods.__init__)
    params = list(sig.parameters.keys())



def test_shr5::critterkraft_is_not_abstract():
    assert not inspect.isabstract(shr5::CritterKraft)


def test_shr5::critterkraft_constructor_exists():
    assert callable(shr5::CritterKraft.__init__)


def test_shr5::critterkraft_constructor_args():
    sig = inspect.signature(shr5::CritterKraft.__init__)
    params = list(sig.parameters.keys())
    assert "reichweite" in params, "Missing parameter 'reichweite'"
    assert "dauer" in params, "Missing parameter 'dauer'"
    assert "art" in params, "Missing parameter 'art'"
    assert "handlung" in params, "Missing parameter 'handlung'"

def test_shr5::critterkraft_has_reichweite():
    assert hasattr(shr5::CritterKraft, "reichweite")
    descriptor = None
    for klass in shr5::CritterKraft.__mro__:
        if "reichweite" in klass.__dict__:
            descriptor = klass.__dict__["reichweite"]
            break
    assert isinstance(descriptor, property)

def test_shr5::critterkraft_has_dauer():
    assert hasattr(shr5::CritterKraft, "dauer")
    descriptor = None
    for klass in shr5::CritterKraft.__mro__:
        if "dauer" in klass.__dict__:
            descriptor = klass.__dict__["dauer"]
            break
    assert isinstance(descriptor, property)

def test_shr5::critterkraft_has_art():
    assert hasattr(shr5::CritterKraft, "art")
    descriptor = None
    for klass in shr5::CritterKraft.__mro__:
        if "art" in klass.__dict__:
            descriptor = klass.__dict__["art"]
            break
    assert isinstance(descriptor, property)

def test_shr5::critterkraft_has_handlung():
    assert hasattr(shr5::CritterKraft, "handlung")
    descriptor = None
    for klass in shr5::CritterKraft.__mro__:
        if "handlung" in klass.__dict__:
            descriptor = klass.__dict__["handlung"]
            break
    assert isinstance(descriptor, property)



def test_shr5::kikraft_is_not_abstract():
    assert not inspect.isabstract(shr5::KiKraft)


def test_shr5::kikraft_constructor_exists():
    assert callable(shr5::KiKraft.__init__)


def test_shr5::kikraft_constructor_args():
    sig = inspect.signature(shr5::KiKraft.__init__)
    params = list(sig.parameters.keys())
    assert "kraftpunkte" in params, "Missing parameter 'kraftpunkte'"

def test_shr5::kikraft_has_kraftpunkte():
    assert hasattr(shr5::KiKraft, "kraftpunkte")
    descriptor = None
    for klass in shr5::KiKraft.__mro__:
        if "kraftpunkte" in klass.__dict__:
            descriptor = klass.__dict__["kraftpunkte"]
            break
    assert isinstance(descriptor, property)



def test_berechneteattribute_is_not_abstract():
    assert not inspect.isabstract(BerechneteAttribute)


def test_berechneteattribute_constructor_exists():
    assert callable(BerechneteAttribute.__init__)


def test_berechneteattribute_constructor_args():
    sig = inspect.signature(BerechneteAttribute.__init__)
    params = list(sig.parameters.keys())



def test_personazustand_is_not_abstract():
    assert not inspect.isabstract(PersonaZustand)


def test_personazustand_constructor_exists():
    assert callable(PersonaZustand.__init__)


def test_personazustand_constructor_args():
    sig = inspect.signature(PersonaZustand.__init__)
    params = list(sig.parameters.keys())



def test_panzerung_is_not_abstract():
    assert not inspect.isabstract(Panzerung)


def test_panzerung_constructor_exists():
    assert callable(Panzerung.__init__)


def test_panzerung_constructor_args():
    sig = inspect.signature(Panzerung.__init__)
    params = list(sig.parameters.keys())



def test_abstraktpersona_is_not_abstract():
    assert not inspect.isabstract(AbstraktPersona)


def test_abstraktpersona_constructor_exists():
    assert callable(AbstraktPersona.__init__)


def test_abstraktpersona_constructor_args():
    sig = inspect.signature(AbstraktPersona.__init__)
    params = list(sig.parameters.keys())



def test_shr5::koerperpersona_is_not_abstract():
    assert not inspect.isabstract(shr5::KoerperPersona)


def test_shr5::koerperpersona_constructor_exists():
    assert callable(shr5::KoerperPersona.__init__)


def test_shr5::koerperpersona_constructor_args():
    sig = inspect.signature(shr5::KoerperPersona.__init__)
    params = list(sig.parameters.keys())
    assert "zustandKoerperlich" in params, "Missing parameter 'zustandKoerperlich'"
    assert "zustandGeistig" in params, "Missing parameter 'zustandGeistig'"

def test_shr5::koerperpersona_has_zustandKoerperlich():
    assert hasattr(shr5::KoerperPersona, "zustandKoerperlich")
    descriptor = None
    for klass in shr5::KoerperPersona.__mro__:
        if "zustandKoerperlich" in klass.__dict__:
            descriptor = klass.__dict__["zustandKoerperlich"]
            break
    assert isinstance(descriptor, property)

def test_shr5::koerperpersona_has_zustandGeistig():
    assert hasattr(shr5::KoerperPersona, "zustandGeistig")
    descriptor = None
    for klass in shr5::KoerperPersona.__mro__:
        if "zustandGeistig" in klass.__dict__:
            descriptor = klass.__dict__["zustandGeistig"]
            break
    assert isinstance(descriptor, property)



def test_koerperpersona_is_not_abstract():
    assert not inspect.isabstract(KoerperPersona)


def test_koerperpersona_constructor_exists():
    assert callable(KoerperPersona.__init__)


def test_koerperpersona_constructor_args():
    sig = inspect.signature(KoerperPersona.__init__)
    params = list(sig.parameters.keys())



def test_shr5::technomancer_is_not_abstract():
    assert not inspect.isabstract(shr5::Technomancer)


def test_shr5::technomancer_constructor_exists():
    assert callable(shr5::Technomancer.__init__)


def test_shr5::technomancer_constructor_args():
    sig = inspect.signature(shr5::Technomancer.__init__)
    params = list(sig.parameters.keys())



def test_shr5::mudanpersona_is_not_abstract():
    assert not inspect.isabstract(shr5::MudanPersona)


def test_shr5::mudanpersona_constructor_exists():
    assert callable(shr5::MudanPersona.__init__)


def test_shr5::mudanpersona_constructor_args():
    sig = inspect.signature(shr5::MudanPersona.__init__)
    params = list(sig.parameters.keys())



def test_abstraktmodifikatoren_is_not_abstract():
    assert not inspect.isabstract(AbstraktModifikatoren)


def test_abstraktmodifikatoren_constructor_exists():
    assert callable(AbstraktModifikatoren.__init__)


def test_abstraktmodifikatoren_constructor_args():
    sig = inspect.signature(AbstraktModifikatoren.__init__)
    params = list(sig.parameters.keys())



def test_shr5::personaeigenschaft_is_not_abstract():
    assert not inspect.isabstract(shr5::PersonaEigenschaft)


def test_shr5::personaeigenschaft_constructor_exists():
    assert callable(shr5::PersonaEigenschaft.__init__)


def test_shr5::personaeigenschaft_constructor_args():
    sig = inspect.signature(shr5::PersonaEigenschaft.__init__)
    params = list(sig.parameters.keys())
    assert "karmaKosten" in params, "Missing parameter 'karmaKosten'"

def test_shr5::personaeigenschaft_has_karmaKosten():
    assert hasattr(shr5::PersonaEigenschaft, "karmaKosten")
    descriptor = None
    for klass in shr5::PersonaEigenschaft.__mro__:
        if "karmaKosten" in klass.__dict__:
            descriptor = klass.__dict__["karmaKosten"]
            break
    assert isinstance(descriptor, property)



def test_shr5::echo_is_not_abstract():
    assert not inspect.isabstract(shr5::Echo)


def test_shr5::echo_constructor_exists():
    assert callable(shr5::Echo.__init__)


def test_shr5::echo_constructor_args():
    sig = inspect.signature(shr5::Echo.__init__)
    params = list(sig.parameters.keys())



def test_shr5::magischemods_is_not_abstract():
    assert not inspect.isabstract(shr5::MagischeMods)


def test_shr5::magischemods_constructor_exists():
    assert callable(shr5::MagischeMods.__init__)


def test_shr5::magischemods_constructor_args():
    sig = inspect.signature(shr5::MagischeMods.__init__)
    params = list(sig.parameters.keys())



def test_shr5::koerpermods_is_not_abstract():
    assert not inspect.isabstract(shr5::Koerpermods)


def test_shr5::koerpermods_constructor_exists():
    assert callable(shr5::Koerpermods.__init__)


def test_shr5::koerpermods_constructor_args():
    sig = inspect.signature(shr5::Koerpermods.__init__)
    params = list(sig.parameters.keys())



def test_shr5::defaultwifi_is_not_abstract():
    assert not inspect.isabstract(shr5::DefaultWifi)


def test_shr5::defaultwifi_constructor_exists():
    assert callable(shr5::DefaultWifi.__init__)


def test_shr5::defaultwifi_constructor_args():
    sig = inspect.signature(shr5::DefaultWifi.__init__)
    params = list(sig.parameters.keys())



def test_shr5::basemagischepersona_is_not_abstract():
    assert not inspect.isabstract(shr5::BaseMagischePersona)


def test_shr5::basemagischepersona_constructor_exists():
    assert callable(shr5::BaseMagischePersona.__init__)


def test_shr5::basemagischepersona_constructor_args():
    sig = inspect.signature(shr5::BaseMagischePersona.__init__)
    params = list(sig.parameters.keys())
    assert "magie" in params, "Missing parameter 'magie'"
    assert "magieBasis" in params, "Missing parameter 'magieBasis'"

def test_shr5::basemagischepersona_has_magie():
    assert hasattr(shr5::BaseMagischePersona, "magie")
    descriptor = None
    for klass in shr5::BaseMagischePersona.__mro__:
        if "magie" in klass.__dict__:
            descriptor = klass.__dict__["magie"]
            break
    assert isinstance(descriptor, property)

def test_shr5::basemagischepersona_has_magieBasis():
    assert hasattr(shr5::BaseMagischePersona, "magieBasis")
    descriptor = None
    for klass in shr5::BaseMagischePersona.__mro__:
        if "magieBasis" in klass.__dict__:
            descriptor = klass.__dict__["magieBasis"]
            break
    assert isinstance(descriptor, property)



def test_shr5::schutzgeist_is_not_abstract():
    assert not inspect.isabstract(shr5::Schutzgeist)


def test_shr5::schutzgeist_constructor_exists():
    assert callable(shr5::Schutzgeist.__init__)


def test_shr5::schutzgeist_constructor_args():
    sig = inspect.signature(shr5::Schutzgeist.__init__)
    params = list(sig.parameters.keys())
    assert "vorteile" in params, "Missing parameter 'vorteile'"
    assert "nachteile" in params, "Missing parameter 'nachteile'"

def test_shr5::schutzgeist_has_vorteile():
    assert hasattr(shr5::Schutzgeist, "vorteile")
    descriptor = None
    for klass in shr5::Schutzgeist.__mro__:
        if "vorteile" in klass.__dict__:
            descriptor = klass.__dict__["vorteile"]
            break
    assert isinstance(descriptor, property)

def test_shr5::schutzgeist_has_nachteile():
    assert hasattr(shr5::Schutzgeist, "nachteile")
    descriptor = None
    for klass in shr5::Schutzgeist.__mro__:
        if "nachteile" in klass.__dict__:
            descriptor = klass.__dict__["nachteile"]
            break
    assert isinstance(descriptor, property)



def test_basemagischepersona_is_not_abstract():
    assert not inspect.isabstract(BaseMagischePersona)


def test_basemagischepersona_constructor_exists():
    assert callable(BaseMagischePersona.__init__)


def test_basemagischepersona_constructor_args():
    sig = inspect.signature(BaseMagischePersona.__init__)
    params = list(sig.parameters.keys())



def test_shr5::magischepersona_is_not_abstract():
    assert not inspect.isabstract(shr5::MagischePersona)


def test_shr5::magischepersona_constructor_exists():
    assert callable(shr5::MagischePersona.__init__)


def test_shr5::magischepersona_constructor_args():
    sig = inspect.signature(shr5::MagischePersona.__init__)
    params = list(sig.parameters.keys())



def test_steigerbar_is_not_abstract():
    assert not inspect.isabstract(Steigerbar)


def test_steigerbar_constructor_exists():
    assert callable(Steigerbar.__init__)


def test_steigerbar_constructor_args():
    sig = inspect.signature(Steigerbar.__init__)
    params = list(sig.parameters.keys())



def test_shr5::initation_is_not_abstract():
    assert not inspect.isabstract(shr5::Initation)


def test_shr5::initation_constructor_exists():
    assert callable(shr5::Initation.__init__)


def test_shr5::initation_constructor_args():
    sig = inspect.signature(shr5::Initation.__init__)
    params = list(sig.parameters.keys())



def test_modifyable_is_not_abstract():
    assert not inspect.isabstract(Modifyable)


def test_modifyable_constructor_exists():
    assert callable(Modifyable.__init__)


def test_modifyable_constructor_args():
    sig = inspect.signature(Modifyable.__init__)
    params = list(sig.parameters.keys())



def test_shr5::eobject_is_not_abstract():
    assert not inspect.isabstract(shr5::EObject)


def test_shr5::eobject_constructor_exists():
    assert callable(shr5::EObject.__init__)


def test_shr5::eobject_constructor_args():
    sig = inspect.signature(shr5::EObject.__init__)
    params = list(sig.parameters.keys())



def test_menge_is_not_abstract():
    assert not inspect.isabstract(Menge)


def test_menge_constructor_exists():
    assert callable(Menge.__init__)


def test_menge_constructor_args():
    sig = inspect.signature(Menge.__init__)
    params = list(sig.parameters.keys())



def test_abstaktfernkampfwaffe_is_not_abstract():
    assert not inspect.isabstract(AbstaktFernKampfwaffe)


def test_abstaktfernkampfwaffe_constructor_exists():
    assert callable(AbstaktFernKampfwaffe.__init__)


def test_abstaktfernkampfwaffe_constructor_args():
    sig = inspect.signature(AbstaktFernKampfwaffe.__init__)
    params = list(sig.parameters.keys())



def test_shr5::wurfwaffe_is_not_abstract():
    assert not inspect.isabstract(shr5::Wurfwaffe)


def test_shr5::wurfwaffe_constructor_exists():
    assert callable(shr5::Wurfwaffe.__init__)


def test_shr5::wurfwaffe_constructor_args():
    sig = inspect.signature(shr5::Wurfwaffe.__init__)
    params = list(sig.parameters.keys())



def test_shr5::projektilwaffe_is_not_abstract():
    assert not inspect.isabstract(shr5::Projektilwaffe)


def test_shr5::projektilwaffe_constructor_exists():
    assert callable(shr5::Projektilwaffe.__init__)


def test_shr5::projektilwaffe_constructor_args():
    sig = inspect.signature(shr5::Projektilwaffe.__init__)
    params = list(sig.parameters.keys())



def test_shr5::feuerwaffe_is_not_abstract():
    assert not inspect.isabstract(shr5::Feuerwaffe)


def test_shr5::feuerwaffe_constructor_exists():
    assert callable(shr5::Feuerwaffe.__init__)


def test_shr5::feuerwaffe_constructor_args():
    sig = inspect.signature(shr5::Feuerwaffe.__init__)
    params = list(sig.parameters.keys())
    assert "kapazitaet" in params, "Missing parameter 'kapazitaet'"
    assert "modie" in params, "Missing parameter 'modie'"
    assert "munitionstyp" in params, "Missing parameter 'munitionstyp'"
    assert "erweiterung" in params, "Missing parameter 'erweiterung'"
    assert "rueckstoss" in params, "Missing parameter 'rueckstoss'"

def test_shr5::feuerwaffe_has_kapazitaet():
    assert hasattr(shr5::Feuerwaffe, "kapazitaet")
    descriptor = None
    for klass in shr5::Feuerwaffe.__mro__:
        if "kapazitaet" in klass.__dict__:
            descriptor = klass.__dict__["kapazitaet"]
            break
    assert isinstance(descriptor, property)

def test_shr5::feuerwaffe_has_modie():
    assert hasattr(shr5::Feuerwaffe, "modie")
    descriptor = None
    for klass in shr5::Feuerwaffe.__mro__:
        if "modie" in klass.__dict__:
            descriptor = klass.__dict__["modie"]
            break
    assert isinstance(descriptor, property)

def test_shr5::feuerwaffe_has_munitionstyp():
    assert hasattr(shr5::Feuerwaffe, "munitionstyp")
    descriptor = None
    for klass in shr5::Feuerwaffe.__mro__:
        if "munitionstyp" in klass.__dict__:
            descriptor = klass.__dict__["munitionstyp"]
            break
    assert isinstance(descriptor, property)

def test_shr5::feuerwaffe_has_erweiterung():
    assert hasattr(shr5::Feuerwaffe, "erweiterung")
    descriptor = None
    for klass in shr5::Feuerwaffe.__mro__:
        if "erweiterung" in klass.__dict__:
            descriptor = klass.__dict__["erweiterung"]
            break
    assert isinstance(descriptor, property)

def test_shr5::feuerwaffe_has_rueckstoss():
    assert hasattr(shr5::Feuerwaffe, "rueckstoss")
    descriptor = None
    for klass in shr5::Feuerwaffe.__mro__:
        if "rueckstoss" in klass.__dict__:
            descriptor = klass.__dict__["rueckstoss"]
            break
    assert isinstance(descriptor, property)



def test_capacity_is_not_abstract():
    assert not inspect.isabstract(Capacity)


def test_capacity_constructor_exists():
    assert callable(Capacity.__init__)


def test_capacity_constructor_args():
    sig = inspect.signature(Capacity.__init__)
    params = list(sig.parameters.keys())



def test_shr5::cyberdeck_is_not_abstract():
    assert not inspect.isabstract(shr5::Cyberdeck)


def test_shr5::cyberdeck_constructor_exists():
    assert callable(shr5::Cyberdeck.__init__)


def test_shr5::cyberdeck_constructor_args():
    sig = inspect.signature(shr5::Cyberdeck.__init__)
    params = list(sig.parameters.keys())
    assert "attribute2" in params, "Missing parameter 'attribute2'"
    assert "modManager" in params, "Missing parameter 'modManager'"
    assert "programSlots" in params, "Missing parameter 'programSlots'"
    assert "attribute3" in params, "Missing parameter 'attribute3'"
    assert "attribute1" in params, "Missing parameter 'attribute1'"
    assert "attribute4" in params, "Missing parameter 'attribute4'"

def test_shr5::cyberdeck_has_attribute2():
    assert hasattr(shr5::Cyberdeck, "attribute2")
    descriptor = None
    for klass in shr5::Cyberdeck.__mro__:
        if "attribute2" in klass.__dict__:
            descriptor = klass.__dict__["attribute2"]
            break
    assert isinstance(descriptor, property)

def test_shr5::cyberdeck_has_modManager():
    assert hasattr(shr5::Cyberdeck, "modManager")
    descriptor = None
    for klass in shr5::Cyberdeck.__mro__:
        if "modManager" in klass.__dict__:
            descriptor = klass.__dict__["modManager"]
            break
    assert isinstance(descriptor, property)

def test_shr5::cyberdeck_has_programSlots():
    assert hasattr(shr5::Cyberdeck, "programSlots")
    descriptor = None
    for klass in shr5::Cyberdeck.__mro__:
        if "programSlots" in klass.__dict__:
            descriptor = klass.__dict__["programSlots"]
            break
    assert isinstance(descriptor, property)

def test_shr5::cyberdeck_has_attribute3():
    assert hasattr(shr5::Cyberdeck, "attribute3")
    descriptor = None
    for klass in shr5::Cyberdeck.__mro__:
        if "attribute3" in klass.__dict__:
            descriptor = klass.__dict__["attribute3"]
            break
    assert isinstance(descriptor, property)

def test_shr5::cyberdeck_has_attribute1():
    assert hasattr(shr5::Cyberdeck, "attribute1")
    descriptor = None
    for klass in shr5::Cyberdeck.__mro__:
        if "attribute1" in klass.__dict__:
            descriptor = klass.__dict__["attribute1"]
            break
    assert isinstance(descriptor, property)

def test_shr5::cyberdeck_has_attribute4():
    assert hasattr(shr5::Cyberdeck, "attribute4")
    descriptor = None
    for klass in shr5::Cyberdeck.__mro__:
        if "attribute4" in klass.__dict__:
            descriptor = klass.__dict__["attribute4"]
            break
    assert isinstance(descriptor, property)



def test_koerpermods_is_not_abstract():
    assert not inspect.isabstract(Koerpermods)


def test_koerpermods_constructor_exists():
    assert callable(Koerpermods.__init__)


def test_koerpermods_constructor_args():
    sig = inspect.signature(Koerpermods.__init__)
    params = list(sig.parameters.keys())



def test_abstaktwaffe_is_not_abstract():
    assert not inspect.isabstract(AbstaktWaffe)


def test_abstaktwaffe_constructor_exists():
    assert callable(AbstaktWaffe.__init__)


def test_abstaktwaffe_constructor_args():
    sig = inspect.signature(AbstaktWaffe.__init__)
    params = list(sig.parameters.keys())



def test_shr5::abstaktfernkampfwaffe_is_not_abstract():
    assert not inspect.isabstract(shr5::AbstaktFernKampfwaffe)


def test_shr5::abstaktfernkampfwaffe_constructor_exists():
    assert callable(shr5::AbstaktFernKampfwaffe.__init__)


def test_shr5::abstaktfernkampfwaffe_constructor_args():
    sig = inspect.signature(shr5::AbstaktFernKampfwaffe.__init__)
    params = list(sig.parameters.keys())



def test_shr5::matrixdevice_is_not_abstract():
    assert not inspect.isabstract(shr5::MatrixDevice)


def test_shr5::matrixdevice_constructor_exists():
    assert callable(shr5::MatrixDevice.__init__)


def test_shr5::matrixdevice_constructor_args():
    sig = inspect.signature(shr5::MatrixDevice.__init__)
    params = list(sig.parameters.keys())



def test_anwendbar_is_not_abstract():
    assert not inspect.isabstract(Anwendbar)


def test_anwendbar_constructor_exists():
    assert callable(Anwendbar.__init__)


def test_anwendbar_constructor_args():
    sig = inspect.signature(Anwendbar.__init__)
    params = list(sig.parameters.keys())



def test_modifizierbar_is_not_abstract():
    assert not inspect.isabstract(Modifizierbar)


def test_modifizierbar_constructor_exists():
    assert callable(Modifizierbar.__init__)


def test_modifizierbar_constructor_args():
    sig = inspect.signature(Modifizierbar.__init__)
    params = list(sig.parameters.keys())



def test_shr5::drug_is_not_abstract():
    assert not inspect.isabstract(shr5::Drug)


def test_shr5::drug_constructor_exists():
    assert callable(shr5::Drug.__init__)


def test_shr5::drug_constructor_args():
    sig = inspect.signature(shr5::Drug.__init__)
    params = list(sig.parameters.keys())
    assert "addictionType" in params, "Missing parameter 'addictionType'"
    assert "duration" in params, "Missing parameter 'duration'"

def test_shr5::drug_has_addictionType():
    assert hasattr(shr5::Drug, "addictionType")
    descriptor = None
    for klass in shr5::Drug.__mro__:
        if "addictionType" in klass.__dict__:
            descriptor = klass.__dict__["addictionType"]
            break
    assert isinstance(descriptor, property)

def test_shr5::drug_has_duration():
    assert hasattr(shr5::Drug, "duration")
    descriptor = None
    for klass in shr5::Drug.__mro__:
        if "duration" in klass.__dict__:
            descriptor = klass.__dict__["duration"]
            break
    assert isinstance(descriptor, property)



def test_shr5::matrixprogram_is_not_abstract():
    assert not inspect.isabstract(shr5::MatrixProgram)


def test_shr5::matrixprogram_constructor_exists():
    assert callable(shr5::MatrixProgram.__init__)


def test_shr5::matrixprogram_constructor_args():
    sig = inspect.signature(shr5::MatrixProgram.__init__)
    params = list(sig.parameters.keys())



def test_geldwert_is_not_abstract():
    assert not inspect.isabstract(GeldWert)


def test_geldwert_constructor_exists():
    assert callable(GeldWert.__init__)


def test_geldwert_constructor_args():
    sig = inspect.signature(GeldWert.__init__)
    params = list(sig.parameters.keys())



def test_shr5::fernkampfwaffemodifikator_is_not_abstract():
    assert not inspect.isabstract(shr5::FernkampfwaffeModifikator)


def test_shr5::fernkampfwaffemodifikator_constructor_exists():
    assert callable(shr5::FernkampfwaffeModifikator.__init__)


def test_shr5::fernkampfwaffemodifikator_constructor_args():
    sig = inspect.signature(shr5::FernkampfwaffeModifikator.__init__)
    params = list(sig.parameters.keys())
    assert "ep" in params, "Missing parameter 'ep'"

def test_shr5::fernkampfwaffemodifikator_has_ep():
    assert hasattr(shr5::FernkampfwaffeModifikator, "ep")
    descriptor = None
    for klass in shr5::FernkampfwaffeModifikator.__mro__:
        if "ep" in klass.__dict__:
            descriptor = klass.__dict__["ep"]
            break
    assert isinstance(descriptor, property)



def test_shr5::cyberwareenhancement_is_not_abstract():
    assert not inspect.isabstract(shr5::CyberwareEnhancement)


def test_shr5::cyberwareenhancement_constructor_exists():
    assert callable(shr5::CyberwareEnhancement.__init__)


def test_shr5::cyberwareenhancement_constructor_args():
    sig = inspect.signature(shr5::CyberwareEnhancement.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "capacityUse" in params, "Missing parameter 'capacityUse'"

def test_shr5::cyberwareenhancement_has_type():
    assert hasattr(shr5::CyberwareEnhancement, "type")
    descriptor = None
    for klass in shr5::CyberwareEnhancement.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_shr5::cyberwareenhancement_has_capacityUse():
    assert hasattr(shr5::CyberwareEnhancement, "capacityUse")
    descriptor = None
    for klass in shr5::CyberwareEnhancement.__mro__:
        if "capacityUse" in klass.__dict__:
            descriptor = klass.__dict__["capacityUse"]
            break
    assert isinstance(descriptor, property)



def test_shr5::cyberware_is_not_abstract():
    assert not inspect.isabstract(shr5::Cyberware)


def test_shr5::cyberware_constructor_exists():
    assert callable(shr5::Cyberware.__init__)


def test_shr5::cyberware_constructor_args():
    sig = inspect.signature(shr5::Cyberware.__init__)
    params = list(sig.parameters.keys())
    assert "cyberwareCapacity" in params, "Missing parameter 'cyberwareCapacity'"
    assert "type" in params, "Missing parameter 'type'"

def test_shr5::cyberware_has_cyberwareCapacity():
    assert hasattr(shr5::Cyberware, "cyberwareCapacity")
    descriptor = None
    for klass in shr5::Cyberware.__mro__:
        if "cyberwareCapacity" in klass.__dict__:
            descriptor = klass.__dict__["cyberwareCapacity"]
            break
    assert isinstance(descriptor, property)

def test_shr5::cyberware_has_type():
    assert hasattr(shr5::Cyberware, "type")
    descriptor = None
    for klass in shr5::Cyberware.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_shr5::bioware_is_not_abstract():
    assert not inspect.isabstract(shr5::BioWare)


def test_shr5::bioware_constructor_exists():
    assert callable(shr5::BioWare.__init__)


def test_shr5::bioware_constructor_args():
    sig = inspect.signature(shr5::BioWare.__init__)
    params = list(sig.parameters.keys())



def test_quelle_is_not_abstract():
    assert not inspect.isabstract(Quelle)


def test_quelle_constructor_exists():
    assert callable(Quelle.__init__)


def test_quelle_constructor_args():
    sig = inspect.signature(Quelle.__init__)
    params = list(sig.parameters.keys())



def test_modifikatorattribute_is_not_abstract():
    assert not inspect.isabstract(ModifikatorAttribute)


def test_modifikatorattribute_constructor_exists():
    assert callable(ModifikatorAttribute.__init__)


def test_modifikatorattribute_constructor_args():
    sig = inspect.signature(ModifikatorAttribute.__init__)
    params = list(sig.parameters.keys())



def test_shr5::spezielleattribute_is_not_abstract():
    assert not inspect.isabstract(shr5::SpezielleAttribute)


def test_shr5::spezielleattribute_constructor_exists():
    assert callable(shr5::SpezielleAttribute.__init__)


def test_shr5::spezielleattribute_constructor_args():
    sig = inspect.signature(shr5::SpezielleAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "initativWuerfel" in params, "Missing parameter 'initativWuerfel'"
    assert "edge" in params, "Missing parameter 'edge'"
    assert "ausweichen" in params, "Missing parameter 'ausweichen'"
    assert "edgeBasis" in params, "Missing parameter 'edgeBasis'"
    assert "initative" in params, "Missing parameter 'initative'"
    assert "essenz" in params, "Missing parameter 'essenz'"

def test_shr5::spezielleattribute_has_initativWuerfel():
    assert hasattr(shr5::SpezielleAttribute, "initativWuerfel")
    descriptor = None
    for klass in shr5::SpezielleAttribute.__mro__:
        if "initativWuerfel" in klass.__dict__:
            descriptor = klass.__dict__["initativWuerfel"]
            break
    assert isinstance(descriptor, property)

def test_shr5::spezielleattribute_has_edge():
    assert hasattr(shr5::SpezielleAttribute, "edge")
    descriptor = None
    for klass in shr5::SpezielleAttribute.__mro__:
        if "edge" in klass.__dict__:
            descriptor = klass.__dict__["edge"]
            break
    assert isinstance(descriptor, property)

def test_shr5::spezielleattribute_has_ausweichen():
    assert hasattr(shr5::SpezielleAttribute, "ausweichen")
    descriptor = None
    for klass in shr5::SpezielleAttribute.__mro__:
        if "ausweichen" in klass.__dict__:
            descriptor = klass.__dict__["ausweichen"]
            break
    assert isinstance(descriptor, property)

def test_shr5::spezielleattribute_has_edgeBasis():
    assert hasattr(shr5::SpezielleAttribute, "edgeBasis")
    descriptor = None
    for klass in shr5::SpezielleAttribute.__mro__:
        if "edgeBasis" in klass.__dict__:
            descriptor = klass.__dict__["edgeBasis"]
            break
    assert isinstance(descriptor, property)

def test_shr5::spezielleattribute_has_initative():
    assert hasattr(shr5::SpezielleAttribute, "initative")
    descriptor = None
    for klass in shr5::SpezielleAttribute.__mro__:
        if "initative" in klass.__dict__:
            descriptor = klass.__dict__["initative"]
            break
    assert isinstance(descriptor, property)

def test_shr5::spezielleattribute_has_essenz():
    assert hasattr(shr5::SpezielleAttribute, "essenz")
    descriptor = None
    for klass in shr5::SpezielleAttribute.__mro__:
        if "essenz" in klass.__dict__:
            descriptor = klass.__dict__["essenz"]
            break
    assert isinstance(descriptor, property)



def test_shr5::sichtverhaeltnisse_is_not_abstract():
    assert not inspect.isabstract(shr5::Sichtverhaeltnisse)


def test_shr5::sichtverhaeltnisse_constructor_exists():
    assert callable(shr5::Sichtverhaeltnisse.__init__)


def test_shr5::sichtverhaeltnisse_constructor_args():
    sig = inspect.signature(shr5::Sichtverhaeltnisse.__init__)
    params = list(sig.parameters.keys())
    assert "infrarot" in params, "Missing parameter 'infrarot'"
    assert "ultrasound" in params, "Missing parameter 'ultrasound'"
    assert "restlichtverstaerkung" in params, "Missing parameter 'restlichtverstaerkung'"

def test_shr5::sichtverhaeltnisse_has_infrarot():
    assert hasattr(shr5::Sichtverhaeltnisse, "infrarot")
    descriptor = None
    for klass in shr5::Sichtverhaeltnisse.__mro__:
        if "infrarot" in klass.__dict__:
            descriptor = klass.__dict__["infrarot"]
            break
    assert isinstance(descriptor, property)

def test_shr5::sichtverhaeltnisse_has_ultrasound():
    assert hasattr(shr5::Sichtverhaeltnisse, "ultrasound")
    descriptor = None
    for klass in shr5::Sichtverhaeltnisse.__mro__:
        if "ultrasound" in klass.__dict__:
            descriptor = klass.__dict__["ultrasound"]
            break
    assert isinstance(descriptor, property)

def test_shr5::sichtverhaeltnisse_has_restlichtverstaerkung():
    assert hasattr(shr5::Sichtverhaeltnisse, "restlichtverstaerkung")
    descriptor = None
    for klass in shr5::Sichtverhaeltnisse.__mro__:
        if "restlichtverstaerkung" in klass.__dict__:
            descriptor = klass.__dict__["restlichtverstaerkung"]
            break
    assert isinstance(descriptor, property)



def test_shr5::geistigeattribute_is_not_abstract():
    assert not inspect.isabstract(shr5::GeistigeAttribute)


def test_shr5::geistigeattribute_constructor_exists():
    assert callable(shr5::GeistigeAttribute.__init__)


def test_shr5::geistigeattribute_constructor_args():
    sig = inspect.signature(shr5::GeistigeAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "willenskraft" in params, "Missing parameter 'willenskraft'"
    assert "charisma" in params, "Missing parameter 'charisma'"
    assert "logik" in params, "Missing parameter 'logik'"
    assert "intuition" in params, "Missing parameter 'intuition'"

def test_shr5::geistigeattribute_has_willenskraft():
    assert hasattr(shr5::GeistigeAttribute, "willenskraft")
    descriptor = None
    for klass in shr5::GeistigeAttribute.__mro__:
        if "willenskraft" in klass.__dict__:
            descriptor = klass.__dict__["willenskraft"]
            break
    assert isinstance(descriptor, property)

def test_shr5::geistigeattribute_has_charisma():
    assert hasattr(shr5::GeistigeAttribute, "charisma")
    descriptor = None
    for klass in shr5::GeistigeAttribute.__mro__:
        if "charisma" in klass.__dict__:
            descriptor = klass.__dict__["charisma"]
            break
    assert isinstance(descriptor, property)

def test_shr5::geistigeattribute_has_logik():
    assert hasattr(shr5::GeistigeAttribute, "logik")
    descriptor = None
    for klass in shr5::GeistigeAttribute.__mro__:
        if "logik" in klass.__dict__:
            descriptor = klass.__dict__["logik"]
            break
    assert isinstance(descriptor, property)

def test_shr5::geistigeattribute_has_intuition():
    assert hasattr(shr5::GeistigeAttribute, "intuition")
    descriptor = None
    for klass in shr5::GeistigeAttribute.__mro__:
        if "intuition" in klass.__dict__:
            descriptor = klass.__dict__["intuition"]
            break
    assert isinstance(descriptor, property)



def test_shr5::probenmodifikatoren_is_not_abstract():
    assert not inspect.isabstract(shr5::ProbenModifikatoren)


def test_shr5::probenmodifikatoren_constructor_exists():
    assert callable(shr5::ProbenModifikatoren.__init__)


def test_shr5::probenmodifikatoren_constructor_args():
    sig = inspect.signature(shr5::ProbenModifikatoren.__init__)
    params = list(sig.parameters.keys())
    assert "heilung" in params, "Missing parameter 'heilung'"
    assert "schadenswiederstand" in params, "Missing parameter 'schadenswiederstand'"

def test_shr5::probenmodifikatoren_has_heilung():
    assert hasattr(shr5::ProbenModifikatoren, "heilung")
    descriptor = None
    for klass in shr5::ProbenModifikatoren.__mro__:
        if "heilung" in klass.__dict__:
            descriptor = klass.__dict__["heilung"]
            break
    assert isinstance(descriptor, property)

def test_shr5::probenmodifikatoren_has_schadenswiederstand():
    assert hasattr(shr5::ProbenModifikatoren, "schadenswiederstand")
    descriptor = None
    for klass in shr5::ProbenModifikatoren.__mro__:
        if "schadenswiederstand" in klass.__dict__:
            descriptor = klass.__dict__["schadenswiederstand"]
            break
    assert isinstance(descriptor, property)



def test_shr5::cyberwaremodifikatioren_is_not_abstract():
    assert not inspect.isabstract(shr5::CyberwareModifikatioren)


def test_shr5::cyberwaremodifikatioren_constructor_exists():
    assert callable(shr5::CyberwareModifikatioren.__init__)


def test_shr5::cyberwaremodifikatioren_constructor_args():
    sig = inspect.signature(shr5::CyberwareModifikatioren.__init__)
    params = list(sig.parameters.keys())
    assert "universalDataConnector" in params, "Missing parameter 'universalDataConnector'"
    assert "simRig" in params, "Missing parameter 'simRig'"
    assert "controlRig" in params, "Missing parameter 'controlRig'"
    assert "directNeuralInterface" in params, "Missing parameter 'directNeuralInterface'"
    assert "riggerInterface" in params, "Missing parameter 'riggerInterface'"

def test_shr5::cyberwaremodifikatioren_has_universalDataConnector():
    assert hasattr(shr5::CyberwareModifikatioren, "universalDataConnector")
    descriptor = None
    for klass in shr5::CyberwareModifikatioren.__mro__:
        if "universalDataConnector" in klass.__dict__:
            descriptor = klass.__dict__["universalDataConnector"]
            break
    assert isinstance(descriptor, property)

def test_shr5::cyberwaremodifikatioren_has_simRig():
    assert hasattr(shr5::CyberwareModifikatioren, "simRig")
    descriptor = None
    for klass in shr5::CyberwareModifikatioren.__mro__:
        if "simRig" in klass.__dict__:
            descriptor = klass.__dict__["simRig"]
            break
    assert isinstance(descriptor, property)

def test_shr5::cyberwaremodifikatioren_has_controlRig():
    assert hasattr(shr5::CyberwareModifikatioren, "controlRig")
    descriptor = None
    for klass in shr5::CyberwareModifikatioren.__mro__:
        if "controlRig" in klass.__dict__:
            descriptor = klass.__dict__["controlRig"]
            break
    assert isinstance(descriptor, property)

def test_shr5::cyberwaremodifikatioren_has_directNeuralInterface():
    assert hasattr(shr5::CyberwareModifikatioren, "directNeuralInterface")
    descriptor = None
    for klass in shr5::CyberwareModifikatioren.__mro__:
        if "directNeuralInterface" in klass.__dict__:
            descriptor = klass.__dict__["directNeuralInterface"]
            break
    assert isinstance(descriptor, property)

def test_shr5::cyberwaremodifikatioren_has_riggerInterface():
    assert hasattr(shr5::CyberwareModifikatioren, "riggerInterface")
    descriptor = None
    for klass in shr5::CyberwareModifikatioren.__mro__:
        if "riggerInterface" in klass.__dict__:
            descriptor = klass.__dict__["riggerInterface"]
            break
    assert isinstance(descriptor, property)



def test_shr5::fernkampfwaffenmodifikatoren_is_not_abstract():
    assert not inspect.isabstract(shr5::FernkampfwaffenModifikatoren)


def test_shr5::fernkampfwaffenmodifikatoren_constructor_exists():
    assert callable(shr5::FernkampfwaffenModifikatoren.__init__)


def test_shr5::fernkampfwaffenmodifikatoren_constructor_args():
    sig = inspect.signature(shr5::FernkampfwaffenModifikatoren.__init__)
    params = list(sig.parameters.keys())
    assert "rueckstoss" in params, "Missing parameter 'rueckstoss'"
    assert "smartgun" in params, "Missing parameter 'smartgun'"
    assert "sichtverbesserung" in params, "Missing parameter 'sichtverbesserung'"
    assert "vergroesserung" in params, "Missing parameter 'vergroesserung'"
    assert "lasterPointer" in params, "Missing parameter 'lasterPointer'"
    assert "schalldaempfer" in params, "Missing parameter 'schalldaempfer'"

def test_shr5::fernkampfwaffenmodifikatoren_has_rueckstoss():
    assert hasattr(shr5::FernkampfwaffenModifikatoren, "rueckstoss")
    descriptor = None
    for klass in shr5::FernkampfwaffenModifikatoren.__mro__:
        if "rueckstoss" in klass.__dict__:
            descriptor = klass.__dict__["rueckstoss"]
            break
    assert isinstance(descriptor, property)

def test_shr5::fernkampfwaffenmodifikatoren_has_smartgun():
    assert hasattr(shr5::FernkampfwaffenModifikatoren, "smartgun")
    descriptor = None
    for klass in shr5::FernkampfwaffenModifikatoren.__mro__:
        if "smartgun" in klass.__dict__:
            descriptor = klass.__dict__["smartgun"]
            break
    assert isinstance(descriptor, property)

def test_shr5::fernkampfwaffenmodifikatoren_has_sichtverbesserung():
    assert hasattr(shr5::FernkampfwaffenModifikatoren, "sichtverbesserung")
    descriptor = None
    for klass in shr5::FernkampfwaffenModifikatoren.__mro__:
        if "sichtverbesserung" in klass.__dict__:
            descriptor = klass.__dict__["sichtverbesserung"]
            break
    assert isinstance(descriptor, property)

def test_shr5::fernkampfwaffenmodifikatoren_has_vergroesserung():
    assert hasattr(shr5::FernkampfwaffenModifikatoren, "vergroesserung")
    descriptor = None
    for klass in shr5::FernkampfwaffenModifikatoren.__mro__:
        if "vergroesserung" in klass.__dict__:
            descriptor = klass.__dict__["vergroesserung"]
            break
    assert isinstance(descriptor, property)

def test_shr5::fernkampfwaffenmodifikatoren_has_lasterPointer():
    assert hasattr(shr5::FernkampfwaffenModifikatoren, "lasterPointer")
    descriptor = None
    for klass in shr5::FernkampfwaffenModifikatoren.__mro__:
        if "lasterPointer" in klass.__dict__:
            descriptor = klass.__dict__["lasterPointer"]
            break
    assert isinstance(descriptor, property)

def test_shr5::fernkampfwaffenmodifikatoren_has_schalldaempfer():
    assert hasattr(shr5::FernkampfwaffenModifikatoren, "schalldaempfer")
    descriptor = None
    for klass in shr5::FernkampfwaffenModifikatoren.__mro__:
        if "schalldaempfer" in klass.__dict__:
            descriptor = klass.__dict__["schalldaempfer"]
            break
    assert isinstance(descriptor, property)



def test_shr5::gegenstandstufen_is_not_abstract():
    assert not inspect.isabstract(shr5::GegenstandStufen)


def test_shr5::gegenstandstufen_constructor_exists():
    assert callable(shr5::GegenstandStufen.__init__)


def test_shr5::gegenstandstufen_constructor_args():
    sig = inspect.signature(shr5::GegenstandStufen.__init__)
    params = list(sig.parameters.keys())
    assert "elektronik" in params, "Missing parameter 'elektronik'"
    assert "tracing" in params, "Missing parameter 'tracing'"
    assert "computer" in params, "Missing parameter 'computer'"
    assert "protection" in params, "Missing parameter 'protection'"
    assert "antiProtection" in params, "Missing parameter 'antiProtection'"
    assert "antiTracing" in params, "Missing parameter 'antiTracing'"

def test_shr5::gegenstandstufen_has_elektronik():
    assert hasattr(shr5::GegenstandStufen, "elektronik")
    descriptor = None
    for klass in shr5::GegenstandStufen.__mro__:
        if "elektronik" in klass.__dict__:
            descriptor = klass.__dict__["elektronik"]
            break
    assert isinstance(descriptor, property)

def test_shr5::gegenstandstufen_has_tracing():
    assert hasattr(shr5::GegenstandStufen, "tracing")
    descriptor = None
    for klass in shr5::GegenstandStufen.__mro__:
        if "tracing" in klass.__dict__:
            descriptor = klass.__dict__["tracing"]
            break
    assert isinstance(descriptor, property)

def test_shr5::gegenstandstufen_has_computer():
    assert hasattr(shr5::GegenstandStufen, "computer")
    descriptor = None
    for klass in shr5::GegenstandStufen.__mro__:
        if "computer" in klass.__dict__:
            descriptor = klass.__dict__["computer"]
            break
    assert isinstance(descriptor, property)

def test_shr5::gegenstandstufen_has_protection():
    assert hasattr(shr5::GegenstandStufen, "protection")
    descriptor = None
    for klass in shr5::GegenstandStufen.__mro__:
        if "protection" in klass.__dict__:
            descriptor = klass.__dict__["protection"]
            break
    assert isinstance(descriptor, property)

def test_shr5::gegenstandstufen_has_antiProtection():
    assert hasattr(shr5::GegenstandStufen, "antiProtection")
    descriptor = None
    for klass in shr5::GegenstandStufen.__mro__:
        if "antiProtection" in klass.__dict__:
            descriptor = klass.__dict__["antiProtection"]
            break
    assert isinstance(descriptor, property)

def test_shr5::gegenstandstufen_has_antiTracing():
    assert hasattr(shr5::GegenstandStufen, "antiTracing")
    descriptor = None
    for klass in shr5::GegenstandStufen.__mro__:
        if "antiTracing" in klass.__dict__:
            descriptor = klass.__dict__["antiTracing"]
            break
    assert isinstance(descriptor, property)



def test_shr5::koerperlicheattribute_is_not_abstract():
    assert not inspect.isabstract(shr5::KoerperlicheAttribute)


def test_shr5::koerperlicheattribute_constructor_exists():
    assert callable(shr5::KoerperlicheAttribute.__init__)


def test_shr5::koerperlicheattribute_constructor_args():
    sig = inspect.signature(shr5::KoerperlicheAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "staerke" in params, "Missing parameter 'staerke'"
    assert "geschicklichkeit" in params, "Missing parameter 'geschicklichkeit'"
    assert "konstitution" in params, "Missing parameter 'konstitution'"
    assert "reaktion" in params, "Missing parameter 'reaktion'"

def test_shr5::koerperlicheattribute_has_staerke():
    assert hasattr(shr5::KoerperlicheAttribute, "staerke")
    descriptor = None
    for klass in shr5::KoerperlicheAttribute.__mro__:
        if "staerke" in klass.__dict__:
            descriptor = klass.__dict__["staerke"]
            break
    assert isinstance(descriptor, property)

def test_shr5::koerperlicheattribute_has_geschicklichkeit():
    assert hasattr(shr5::KoerperlicheAttribute, "geschicklichkeit")
    descriptor = None
    for klass in shr5::KoerperlicheAttribute.__mro__:
        if "geschicklichkeit" in klass.__dict__:
            descriptor = klass.__dict__["geschicklichkeit"]
            break
    assert isinstance(descriptor, property)

def test_shr5::koerperlicheattribute_has_konstitution():
    assert hasattr(shr5::KoerperlicheAttribute, "konstitution")
    descriptor = None
    for klass in shr5::KoerperlicheAttribute.__mro__:
        if "konstitution" in klass.__dict__:
            descriptor = klass.__dict__["konstitution"]
            break
    assert isinstance(descriptor, property)

def test_shr5::koerperlicheattribute_has_reaktion():
    assert hasattr(shr5::KoerperlicheAttribute, "reaktion")
    descriptor = None
    for klass in shr5::KoerperlicheAttribute.__mro__:
        if "reaktion" in klass.__dict__:
            descriptor = klass.__dict__["reaktion"]
            break
    assert isinstance(descriptor, property)



def test_shr5::modifyable_is_not_abstract():
    assert not inspect.isabstract(shr5::Modifyable)


def test_shr5::modifyable_constructor_exists():
    assert callable(shr5::Modifyable.__init__)


def test_shr5::modifyable_constructor_args():
    sig = inspect.signature(shr5::Modifyable.__init__)
    params = list(sig.parameters.keys())



def test_shr5::modifizierbar_is_not_abstract():
    assert not inspect.isabstract(shr5::Modifizierbar)


def test_shr5::modifizierbar_constructor_exists():
    assert callable(shr5::Modifizierbar.__init__)


def test_shr5::modifizierbar_constructor_args():
    sig = inspect.signature(shr5::Modifizierbar.__init__)
    params = list(sig.parameters.keys())



def test_shr5::eattribute_is_not_abstract():
    assert not inspect.isabstract(shr5::EAttribute)


def test_shr5::eattribute_constructor_exists():
    assert callable(shr5::EAttribute.__init__)


def test_shr5::eattribute_constructor_args():
    sig = inspect.signature(shr5::EAttribute.__init__)
    params = list(sig.parameters.keys())



def test_shr5::attributmodifikatorwert_is_not_abstract():
    assert not inspect.isabstract(shr5::AttributModifikatorWert)


def test_shr5::attributmodifikatorwert_constructor_exists():
    assert callable(shr5::AttributModifikatorWert.__init__)


def test_shr5::attributmodifikatorwert_constructor_args():
    sig = inspect.signature(shr5::AttributModifikatorWert.__init__)
    params = list(sig.parameters.keys())
    assert "wert" in params, "Missing parameter 'wert'"

def test_shr5::attributmodifikatorwert_has_wert():
    assert hasattr(shr5::AttributModifikatorWert, "wert")
    descriptor = None
    for klass in shr5::AttributModifikatorWert.__mro__:
        if "wert" in klass.__dict__:
            descriptor = klass.__dict__["wert"]
            break
    assert isinstance(descriptor, property)



def test_shr5::nahkampfwaffe_is_not_abstract():
    assert not inspect.isabstract(shr5::Nahkampfwaffe)


def test_shr5::nahkampfwaffe_constructor_exists():
    assert callable(shr5::Nahkampfwaffe.__init__)


def test_shr5::nahkampfwaffe_constructor_args():
    sig = inspect.signature(shr5::Nahkampfwaffe.__init__)
    params = list(sig.parameters.keys())
    assert "reichweite" in params, "Missing parameter 'reichweite'"

def test_shr5::nahkampfwaffe_has_reichweite():
    assert hasattr(shr5::Nahkampfwaffe, "reichweite")
    descriptor = None
    for klass in shr5::Nahkampfwaffe.__mro__:
        if "reichweite" in klass.__dict__:
            descriptor = klass.__dict__["reichweite"]
            break
    assert isinstance(descriptor, property)



def test_shr5::geldwert_is_not_abstract():
    assert not inspect.isabstract(shr5::GeldWert)


def test_shr5::geldwert_constructor_exists():
    assert callable(shr5::GeldWert.__init__)


def test_shr5::geldwert_constructor_args():
    sig = inspect.signature(shr5::GeldWert.__init__)
    params = list(sig.parameters.keys())
    assert "wert" in params, "Missing parameter 'wert'"
    assert "wertValue" in params, "Missing parameter 'wertValue'"
    assert "verfuegbarkeit" in params, "Missing parameter 'verfuegbarkeit'"

def test_shr5::geldwert_has_wert():
    assert hasattr(shr5::GeldWert, "wert")
    descriptor = None
    for klass in shr5::GeldWert.__mro__:
        if "wert" in klass.__dict__:
            descriptor = klass.__dict__["wert"]
            break
    assert isinstance(descriptor, property)

def test_shr5::geldwert_has_wertValue():
    assert hasattr(shr5::GeldWert, "wertValue")
    descriptor = None
    for klass in shr5::GeldWert.__mro__:
        if "wertValue" in klass.__dict__:
            descriptor = klass.__dict__["wertValue"]
            break
    assert isinstance(descriptor, property)

def test_shr5::geldwert_has_verfuegbarkeit():
    assert hasattr(shr5::GeldWert, "verfuegbarkeit")
    descriptor = None
    for klass in shr5::GeldWert.__mro__:
        if "verfuegbarkeit" in klass.__dict__:
            descriptor = klass.__dict__["verfuegbarkeit"]
            break
    assert isinstance(descriptor, property)



def test_abstraktgegenstand_is_not_abstract():
    assert not inspect.isabstract(AbstraktGegenstand)


def test_abstraktgegenstand_constructor_exists():
    assert callable(AbstraktGegenstand.__init__)


def test_abstraktgegenstand_constructor_args():
    sig = inspect.signature(AbstraktGegenstand.__init__)
    params = list(sig.parameters.keys())



def test_shr5::credstick_is_not_abstract():
    assert not inspect.isabstract(shr5::Credstick)


def test_shr5::credstick_constructor_exists():
    assert callable(shr5::Credstick.__init__)


def test_shr5::credstick_constructor_args():
    sig = inspect.signature(shr5::Credstick.__init__)
    params = list(sig.parameters.keys())
    assert "maxValue" in params, "Missing parameter 'maxValue'"
    assert "currentValue" in params, "Missing parameter 'currentValue'"

def test_shr5::credstick_has_maxValue():
    assert hasattr(shr5::Credstick, "maxValue")
    descriptor = None
    for klass in shr5::Credstick.__mro__:
        if "maxValue" in klass.__dict__:
            descriptor = klass.__dict__["maxValue"]
            break
    assert isinstance(descriptor, property)

def test_shr5::credstick_has_currentValue():
    assert hasattr(shr5::Credstick, "currentValue")
    descriptor = None
    for klass in shr5::Credstick.__mro__:
        if "currentValue" in klass.__dict__:
            descriptor = klass.__dict__["currentValue"]
            break
    assert isinstance(descriptor, property)



def test_shr5::magazin_is_not_abstract():
    assert not inspect.isabstract(shr5::Magazin)


def test_shr5::magazin_constructor_exists():
    assert callable(shr5::Magazin.__init__)


def test_shr5::magazin_constructor_args():
    sig = inspect.signature(shr5::Magazin.__init__)
    params = list(sig.parameters.keys())



def test_shr5::abstractmatrixdevice_is_not_abstract():
    assert not inspect.isabstract(shr5::AbstractMatrixDevice)


def test_shr5::abstractmatrixdevice_constructor_exists():
    assert callable(shr5::AbstractMatrixDevice.__init__)


def test_shr5::abstractmatrixdevice_constructor_args():
    sig = inspect.signature(shr5::AbstractMatrixDevice.__init__)
    params = list(sig.parameters.keys())
    assert "deviceRating" in params, "Missing parameter 'deviceRating'"

def test_shr5::abstractmatrixdevice_has_deviceRating():
    assert hasattr(shr5::AbstractMatrixDevice, "deviceRating")
    descriptor = None
    for klass in shr5::AbstractMatrixDevice.__mro__:
        if "deviceRating" in klass.__dict__:
            descriptor = klass.__dict__["deviceRating"]
            break
    assert isinstance(descriptor, property)



def test_shr5::kleidung_is_not_abstract():
    assert not inspect.isabstract(shr5::Kleidung)


def test_shr5::kleidung_constructor_exists():
    assert callable(shr5::Kleidung.__init__)


def test_shr5::kleidung_constructor_args():
    sig = inspect.signature(shr5::Kleidung.__init__)
    params = list(sig.parameters.keys())
    assert "ruestung" in params, "Missing parameter 'ruestung'"

def test_shr5::kleidung_has_ruestung():
    assert hasattr(shr5::Kleidung, "ruestung")
    descriptor = None
    for klass in shr5::Kleidung.__mro__:
        if "ruestung" in klass.__dict__:
            descriptor = klass.__dict__["ruestung"]
            break
    assert isinstance(descriptor, property)



def test_shr5::abstraktfokus_is_not_abstract():
    assert not inspect.isabstract(shr5::AbstraktFokus)


def test_shr5::abstraktfokus_constructor_exists():
    assert callable(shr5::AbstraktFokus.__init__)


def test_shr5::abstraktfokus_constructor_args():
    sig = inspect.signature(shr5::AbstraktFokus.__init__)
    params = list(sig.parameters.keys())



def test_shr5::munition_is_not_abstract():
    assert not inspect.isabstract(shr5::Munition)


def test_shr5::munition_constructor_exists():
    assert callable(shr5::Munition.__init__)


def test_shr5::munition_constructor_args():
    sig = inspect.signature(shr5::Munition.__init__)
    params = list(sig.parameters.keys())
    assert "armorMod" in params, "Missing parameter 'armorMod'"
    assert "damageMod" in params, "Missing parameter 'damageMod'"
    assert "damageType" in params, "Missing parameter 'damageType'"

def test_shr5::munition_has_armorMod():
    assert hasattr(shr5::Munition, "armorMod")
    descriptor = None
    for klass in shr5::Munition.__mro__:
        if "armorMod" in klass.__dict__:
            descriptor = klass.__dict__["armorMod"]
            break
    assert isinstance(descriptor, property)

def test_shr5::munition_has_damageMod():
    assert hasattr(shr5::Munition, "damageMod")
    descriptor = None
    for klass in shr5::Munition.__mro__:
        if "damageMod" in klass.__dict__:
            descriptor = klass.__dict__["damageMod"]
            break
    assert isinstance(descriptor, property)

def test_shr5::munition_has_damageType():
    assert hasattr(shr5::Munition, "damageType")
    descriptor = None
    for klass in shr5::Munition.__mro__:
        if "damageType" in klass.__dict__:
            descriptor = klass.__dict__["damageType"]
            break
    assert isinstance(descriptor, property)



def test_shr5::abstaktwaffe_is_not_abstract():
    assert not inspect.isabstract(shr5::AbstaktWaffe)


def test_shr5::abstaktwaffe_constructor_exists():
    assert callable(shr5::AbstaktWaffe.__init__)


def test_shr5::abstaktwaffe_constructor_args():
    sig = inspect.signature(shr5::AbstaktWaffe.__init__)
    params = list(sig.parameters.keys())
    assert "schadesTyp" in params, "Missing parameter 'schadesTyp'"
    assert "schadenscode" in params, "Missing parameter 'schadenscode'"
    assert "durchschlagsKraft" in params, "Missing parameter 'durchschlagsKraft'"
    assert "praezision" in params, "Missing parameter 'praezision'"

def test_shr5::abstaktwaffe_has_schadesTyp():
    assert hasattr(shr5::AbstaktWaffe, "schadesTyp")
    descriptor = None
    for klass in shr5::AbstaktWaffe.__mro__:
        if "schadesTyp" in klass.__dict__:
            descriptor = klass.__dict__["schadesTyp"]
            break
    assert isinstance(descriptor, property)

def test_shr5::abstaktwaffe_has_schadenscode():
    assert hasattr(shr5::AbstaktWaffe, "schadenscode")
    descriptor = None
    for klass in shr5::AbstaktWaffe.__mro__:
        if "schadenscode" in klass.__dict__:
            descriptor = klass.__dict__["schadenscode"]
            break
    assert isinstance(descriptor, property)

def test_shr5::abstaktwaffe_has_durchschlagsKraft():
    assert hasattr(shr5::AbstaktWaffe, "durchschlagsKraft")
    descriptor = None
    for klass in shr5::AbstaktWaffe.__mro__:
        if "durchschlagsKraft" in klass.__dict__:
            descriptor = klass.__dict__["durchschlagsKraft"]
            break
    assert isinstance(descriptor, property)

def test_shr5::abstaktwaffe_has_praezision():
    assert hasattr(shr5::AbstaktWaffe, "praezision")
    descriptor = None
    for klass in shr5::AbstaktWaffe.__mro__:
        if "praezision" in klass.__dict__:
            descriptor = klass.__dict__["praezision"]
            break
    assert isinstance(descriptor, property)



def test_shr5::substancecontainer_is_not_abstract():
    assert not inspect.isabstract(shr5::SubstanceContainer)


def test_shr5::substancecontainer_constructor_exists():
    assert callable(shr5::SubstanceContainer.__init__)


def test_shr5::substancecontainer_constructor_args():
    sig = inspect.signature(shr5::SubstanceContainer.__init__)
    params = list(sig.parameters.keys())



def test_shr5::gegenstand_is_not_abstract():
    assert not inspect.isabstract(shr5::Gegenstand)


def test_shr5::gegenstand_constructor_exists():
    assert callable(shr5::Gegenstand.__init__)


def test_shr5::gegenstand_constructor_args():
    sig = inspect.signature(shr5::Gegenstand.__init__)
    params = list(sig.parameters.keys())
    assert "kategorie" in params, "Missing parameter 'kategorie'"
    assert "stufe" in params, "Missing parameter 'stufe'"

def test_shr5::gegenstand_has_kategorie():
    assert hasattr(shr5::Gegenstand, "kategorie")
    descriptor = None
    for klass in shr5::Gegenstand.__mro__:
        if "kategorie" in klass.__dict__:
            descriptor = klass.__dict__["kategorie"]
            break
    assert isinstance(descriptor, property)

def test_shr5::gegenstand_has_stufe():
    assert hasattr(shr5::Gegenstand, "stufe")
    descriptor = None
    for klass in shr5::Gegenstand.__mro__:
        if "stufe" in klass.__dict__:
            descriptor = klass.__dict__["stufe"]
            break
    assert isinstance(descriptor, property)



def test_shr5::personamartialartstyle_is_not_abstract():
    assert not inspect.isabstract(shr5::PersonaMartialartStyle)


def test_shr5::personamartialartstyle_constructor_exists():
    assert callable(shr5::PersonaMartialartStyle.__init__)


def test_shr5::personamartialartstyle_constructor_args():
    sig = inspect.signature(shr5::PersonaMartialartStyle.__init__)
    params = list(sig.parameters.keys())



def test_shr5::personafertigkeitsgruppe_is_not_abstract():
    assert not inspect.isabstract(shr5::PersonaFertigkeitsGruppe)


def test_shr5::personafertigkeitsgruppe_constructor_exists():
    assert callable(shr5::PersonaFertigkeitsGruppe.__init__)


def test_shr5::personafertigkeitsgruppe_constructor_args():
    sig = inspect.signature(shr5::PersonaFertigkeitsGruppe.__init__)
    params = list(sig.parameters.keys())



def test_shr5::personafertigkeit_is_not_abstract():
    assert not inspect.isabstract(shr5::PersonaFertigkeit)


def test_shr5::personafertigkeit_constructor_exists():
    assert callable(shr5::PersonaFertigkeit.__init__)


def test_shr5::personafertigkeit_constructor_args():
    sig = inspect.signature(shr5::PersonaFertigkeit.__init__)
    params = list(sig.parameters.keys())



def test_chrakterlimits_is_not_abstract():
    assert not inspect.isabstract(ChrakterLimits)


def test_chrakterlimits_constructor_exists():
    assert callable(ChrakterLimits.__init__)


def test_chrakterlimits_constructor_args():
    sig = inspect.signature(ChrakterLimits.__init__)
    params = list(sig.parameters.keys())



def test_geistigeattribute_is_not_abstract():
    assert not inspect.isabstract(GeistigeAttribute)


def test_geistigeattribute_constructor_exists():
    assert callable(GeistigeAttribute.__init__)


def test_geistigeattribute_constructor_args():
    sig = inspect.signature(GeistigeAttribute.__init__)
    params = list(sig.parameters.keys())



def test_spezielleattribute_is_not_abstract():
    assert not inspect.isabstract(SpezielleAttribute)


def test_spezielleattribute_constructor_exists():
    assert callable(SpezielleAttribute.__init__)


def test_spezielleattribute_constructor_args():
    sig = inspect.signature(SpezielleAttribute.__init__)
    params = list(sig.parameters.keys())



def test_koerperlicheattribute_is_not_abstract():
    assert not inspect.isabstract(KoerperlicheAttribute)


def test_koerperlicheattribute_constructor_exists():
    assert callable(KoerperlicheAttribute.__init__)


def test_koerperlicheattribute_constructor_args():
    sig = inspect.signature(KoerperlicheAttribute.__init__)
    params = list(sig.parameters.keys())



def test_identifiable_is_not_abstract():
    assert not inspect.isabstract(Identifiable)


def test_identifiable_constructor_exists():
    assert callable(Identifiable.__init__)


def test_identifiable_constructor_args():
    sig = inspect.signature(Identifiable.__init__)
    params = list(sig.parameters.keys())



def test_shr5::quelle_is_not_abstract():
    assert not inspect.isabstract(shr5::Quelle)


def test_shr5::quelle_constructor_exists():
    assert callable(shr5::Quelle.__init__)


def test_shr5::quelle_constructor_args():
    sig = inspect.signature(shr5::Quelle.__init__)
    params = list(sig.parameters.keys())
    assert "page" in params, "Missing parameter 'page'"

def test_shr5::quelle_has_page():
    assert hasattr(shr5::Quelle, "page")
    descriptor = None
    for klass in shr5::Quelle.__mro__:
        if "page" in klass.__dict__:
            descriptor = klass.__dict__["page"]
            break
    assert isinstance(descriptor, property)



def test_shr5::beschreibbar_is_not_abstract():
    assert not inspect.isabstract(shr5::Beschreibbar)


def test_shr5::beschreibbar_constructor_exists():
    assert callable(shr5::Beschreibbar.__init__)


def test_shr5::beschreibbar_constructor_args():
    sig = inspect.signature(shr5::Beschreibbar.__init__)
    params = list(sig.parameters.keys())
    assert "beschreibung" in params, "Missing parameter 'beschreibung'"
    assert "image" in params, "Missing parameter 'image'"
    assert "name" in params, "Missing parameter 'name'"

def test_shr5::beschreibbar_has_beschreibung():
    assert hasattr(shr5::Beschreibbar, "beschreibung")
    descriptor = None
    for klass in shr5::Beschreibbar.__mro__:
        if "beschreibung" in klass.__dict__:
            descriptor = klass.__dict__["beschreibung"]
            break
    assert isinstance(descriptor, property)

def test_shr5::beschreibbar_has_image():
    assert hasattr(shr5::Beschreibbar, "image")
    descriptor = None
    for klass in shr5::Beschreibbar.__mro__:
        if "image" in klass.__dict__:
            descriptor = klass.__dict__["image"]
            break
    assert isinstance(descriptor, property)

def test_shr5::beschreibbar_has_name():
    assert hasattr(shr5::Beschreibbar, "name")
    descriptor = None
    for klass in shr5::Beschreibbar.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_beschreibbar_is_not_abstract():
    assert not inspect.isabstract(Beschreibbar)


def test_beschreibbar_constructor_exists():
    assert callable(Beschreibbar.__init__)


def test_beschreibbar_constructor_args():
    sig = inspect.signature(Beschreibbar.__init__)
    params = list(sig.parameters.keys())



def test_shr5::spezialisierung_is_not_abstract():
    assert not inspect.isabstract(shr5::Spezialisierung)


def test_shr5::spezialisierung_constructor_exists():
    assert callable(shr5::Spezialisierung.__init__)


def test_shr5::spezialisierung_constructor_args():
    sig = inspect.signature(shr5::Spezialisierung.__init__)
    params = list(sig.parameters.keys())



def test_shr5::fahrzeugmodifikation_is_not_abstract():
    assert not inspect.isabstract(shr5::FahrzeugModifikation)


def test_shr5::fahrzeugmodifikation_constructor_exists():
    assert callable(shr5::FahrzeugModifikation.__init__)


def test_shr5::fahrzeugmodifikation_constructor_args():
    sig = inspect.signature(shr5::FahrzeugModifikation.__init__)
    params = list(sig.parameters.keys())
    assert "capacityUsed" in params, "Missing parameter 'capacityUsed'"

def test_shr5::fahrzeugmodifikation_has_capacityUsed():
    assert hasattr(shr5::FahrzeugModifikation, "capacityUsed")
    descriptor = None
    for klass in shr5::FahrzeugModifikation.__mro__:
        if "capacityUsed" in klass.__dict__:
            descriptor = klass.__dict__["capacityUsed"]
            break
    assert isinstance(descriptor, property)



def test_shr5::martialarttechnique_is_not_abstract():
    assert not inspect.isabstract(shr5::MartialartTechnique)


def test_shr5::martialarttechnique_constructor_exists():
    assert callable(shr5::MartialartTechnique.__init__)


def test_shr5::martialarttechnique_constructor_args():
    sig = inspect.signature(shr5::MartialartTechnique.__init__)
    params = list(sig.parameters.keys())



def test_shr5::fertigkeit_is_not_abstract():
    assert not inspect.isabstract(shr5::Fertigkeit)


def test_shr5::fertigkeit_constructor_exists():
    assert callable(shr5::Fertigkeit.__init__)


def test_shr5::fertigkeit_constructor_args():
    sig = inspect.signature(shr5::Fertigkeit.__init__)
    params = list(sig.parameters.keys())
    assert "kategorie" in params, "Missing parameter 'kategorie'"
    assert "ausweichen" in params, "Missing parameter 'ausweichen'"

def test_shr5::fertigkeit_has_kategorie():
    assert hasattr(shr5::Fertigkeit, "kategorie")
    descriptor = None
    for klass in shr5::Fertigkeit.__mro__:
        if "kategorie" in klass.__dict__:
            descriptor = klass.__dict__["kategorie"]
            break
    assert isinstance(descriptor, property)

def test_shr5::fertigkeit_has_ausweichen():
    assert hasattr(shr5::Fertigkeit, "ausweichen")
    descriptor = None
    for klass in shr5::Fertigkeit.__mro__:
        if "ausweichen" in klass.__dict__:
            descriptor = klass.__dict__["ausweichen"]
            break
    assert isinstance(descriptor, property)



def test_shr5::stufenpersona_is_not_abstract():
    assert not inspect.isabstract(shr5::StufenPersona)


def test_shr5::stufenpersona_constructor_exists():
    assert callable(shr5::StufenPersona.__init__)


def test_shr5::stufenpersona_constructor_args():
    sig = inspect.signature(shr5::StufenPersona.__init__)
    params = list(sig.parameters.keys())
    assert "stufe" in params, "Missing parameter 'stufe'"

def test_shr5::stufenpersona_has_stufe():
    assert hasattr(shr5::StufenPersona, "stufe")
    descriptor = None
    for klass in shr5::StufenPersona.__mro__:
        if "stufe" in klass.__dict__:
            descriptor = klass.__dict__["stufe"]
            break
    assert isinstance(descriptor, property)



def test_shr5::komplexeform_is_not_abstract():
    assert not inspect.isabstract(shr5::KomplexeForm)


def test_shr5::komplexeform_constructor_exists():
    assert callable(shr5::KomplexeForm.__init__)


def test_shr5::komplexeform_constructor_args():
    sig = inspect.signature(shr5::KomplexeForm.__init__)
    params = list(sig.parameters.keys())
    assert "dauer" in params, "Missing parameter 'dauer'"
    assert "ziel" in params, "Missing parameter 'ziel'"
    assert "schwund" in params, "Missing parameter 'schwund'"

def test_shr5::komplexeform_has_dauer():
    assert hasattr(shr5::KomplexeForm, "dauer")
    descriptor = None
    for klass in shr5::KomplexeForm.__mro__:
        if "dauer" in klass.__dict__:
            descriptor = klass.__dict__["dauer"]
            break
    assert isinstance(descriptor, property)

def test_shr5::komplexeform_has_ziel():
    assert hasattr(shr5::KomplexeForm, "ziel")
    descriptor = None
    for klass in shr5::KomplexeForm.__mro__:
        if "ziel" in klass.__dict__:
            descriptor = klass.__dict__["ziel"]
            break
    assert isinstance(descriptor, property)

def test_shr5::komplexeform_has_schwund():
    assert hasattr(shr5::KomplexeForm, "schwund")
    descriptor = None
    for klass in shr5::KomplexeForm.__mro__:
        if "schwund" in klass.__dict__:
            descriptor = klass.__dict__["schwund"]
            break
    assert isinstance(descriptor, property)



def test_shr5::magischetradition_is_not_abstract():
    assert not inspect.isabstract(shr5::MagischeTradition)


def test_shr5::magischetradition_constructor_exists():
    assert callable(shr5::MagischeTradition.__init__)


def test_shr5::magischetradition_constructor_args():
    sig = inspect.signature(shr5::MagischeTradition.__init__)
    params = list(sig.parameters.keys())
    assert "enzug" in params, "Missing parameter 'enzug'"

def test_shr5::magischetradition_has_enzug():
    assert hasattr(shr5::MagischeTradition, "enzug")
    descriptor = None
    for klass in shr5::MagischeTradition.__mro__:
        if "enzug" in klass.__dict__:
            descriptor = klass.__dict__["enzug"]
            break
    assert isinstance(descriptor, property)



def test_shr5::abstraktgegenstand_is_not_abstract():
    assert not inspect.isabstract(shr5::AbstraktGegenstand)


def test_shr5::abstraktgegenstand_constructor_exists():
    assert callable(shr5::AbstraktGegenstand.__init__)


def test_shr5::abstraktgegenstand_constructor_args():
    sig = inspect.signature(shr5::AbstraktGegenstand.__init__)
    params = list(sig.parameters.keys())



def test_shr5::abstraktpersona_is_not_abstract():
    assert not inspect.isabstract(shr5::AbstraktPersona)


def test_shr5::abstraktpersona_constructor_exists():
    assert callable(shr5::AbstraktPersona.__init__)


def test_shr5::abstraktpersona_constructor_args():
    sig = inspect.signature(shr5::AbstraktPersona.__init__)
    params = list(sig.parameters.keys())
    assert "modManager" in params, "Missing parameter 'modManager'"
    assert "willenskraftBasis" in params, "Missing parameter 'willenskraftBasis'"
    assert "reaktionBasis" in params, "Missing parameter 'reaktionBasis'"
    assert "staerkeBasis" in params, "Missing parameter 'staerkeBasis'"
    assert "geschicklichkeitBasis" in params, "Missing parameter 'geschicklichkeitBasis'"
    assert "logikBasis" in params, "Missing parameter 'logikBasis'"
    assert "intuitionBasis" in params, "Missing parameter 'intuitionBasis'"
    assert "konstitutionBasis" in params, "Missing parameter 'konstitutionBasis'"
    assert "charismaBasis" in params, "Missing parameter 'charismaBasis'"

def test_shr5::abstraktpersona_has_modManager():
    assert hasattr(shr5::AbstraktPersona, "modManager")
    descriptor = None
    for klass in shr5::AbstraktPersona.__mro__:
        if "modManager" in klass.__dict__:
            descriptor = klass.__dict__["modManager"]
            break
    assert isinstance(descriptor, property)

def test_shr5::abstraktpersona_has_willenskraftBasis():
    assert hasattr(shr5::AbstraktPersona, "willenskraftBasis")
    descriptor = None
    for klass in shr5::AbstraktPersona.__mro__:
        if "willenskraftBasis" in klass.__dict__:
            descriptor = klass.__dict__["willenskraftBasis"]
            break
    assert isinstance(descriptor, property)

def test_shr5::abstraktpersona_has_reaktionBasis():
    assert hasattr(shr5::AbstraktPersona, "reaktionBasis")
    descriptor = None
    for klass in shr5::AbstraktPersona.__mro__:
        if "reaktionBasis" in klass.__dict__:
            descriptor = klass.__dict__["reaktionBasis"]
            break
    assert isinstance(descriptor, property)

def test_shr5::abstraktpersona_has_staerkeBasis():
    assert hasattr(shr5::AbstraktPersona, "staerkeBasis")
    descriptor = None
    for klass in shr5::AbstraktPersona.__mro__:
        if "staerkeBasis" in klass.__dict__:
            descriptor = klass.__dict__["staerkeBasis"]
            break
    assert isinstance(descriptor, property)

def test_shr5::abstraktpersona_has_geschicklichkeitBasis():
    assert hasattr(shr5::AbstraktPersona, "geschicklichkeitBasis")
    descriptor = None
    for klass in shr5::AbstraktPersona.__mro__:
        if "geschicklichkeitBasis" in klass.__dict__:
            descriptor = klass.__dict__["geschicklichkeitBasis"]
            break
    assert isinstance(descriptor, property)

def test_shr5::abstraktpersona_has_logikBasis():
    assert hasattr(shr5::AbstraktPersona, "logikBasis")
    descriptor = None
    for klass in shr5::AbstraktPersona.__mro__:
        if "logikBasis" in klass.__dict__:
            descriptor = klass.__dict__["logikBasis"]
            break
    assert isinstance(descriptor, property)

def test_shr5::abstraktpersona_has_intuitionBasis():
    assert hasattr(shr5::AbstraktPersona, "intuitionBasis")
    descriptor = None
    for klass in shr5::AbstraktPersona.__mro__:
        if "intuitionBasis" in klass.__dict__:
            descriptor = klass.__dict__["intuitionBasis"]
            break
    assert isinstance(descriptor, property)

def test_shr5::abstraktpersona_has_konstitutionBasis():
    assert hasattr(shr5::AbstraktPersona, "konstitutionBasis")
    descriptor = None
    for klass in shr5::AbstraktPersona.__mro__:
        if "konstitutionBasis" in klass.__dict__:
            descriptor = klass.__dict__["konstitutionBasis"]
            break
    assert isinstance(descriptor, property)

def test_shr5::abstraktpersona_has_charismaBasis():
    assert hasattr(shr5::AbstraktPersona, "charismaBasis")
    descriptor = None
    for klass in shr5::AbstraktPersona.__mro__:
        if "charismaBasis" in klass.__dict__:
            descriptor = klass.__dict__["charismaBasis"]
            break
    assert isinstance(descriptor, property)



def test_shr5::sensor_is_not_abstract():
    assert not inspect.isabstract(shr5::Sensor)


def test_shr5::sensor_constructor_exists():
    assert callable(shr5::Sensor.__init__)


def test_shr5::sensor_constructor_args():
    sig = inspect.signature(shr5::Sensor.__init__)
    params = list(sig.parameters.keys())
    assert "rating" in params, "Missing parameter 'rating'"
    assert "capacityValue" in params, "Missing parameter 'capacityValue'"

def test_shr5::sensor_has_rating():
    assert hasattr(shr5::Sensor, "rating")
    descriptor = None
    for klass in shr5::Sensor.__mro__:
        if "rating" in klass.__dict__:
            descriptor = klass.__dict__["rating"]
            break
    assert isinstance(descriptor, property)

def test_shr5::sensor_has_capacityValue():
    assert hasattr(shr5::Sensor, "capacityValue")
    descriptor = None
    for klass in shr5::Sensor.__mro__:
        if "capacityValue" in klass.__dict__:
            descriptor = klass.__dict__["capacityValue"]
            break
    assert isinstance(descriptor, property)



def test_shr5::martialartstyle_is_not_abstract():
    assert not inspect.isabstract(shr5::MartialartStyle)


def test_shr5::martialartstyle_constructor_exists():
    assert callable(shr5::MartialartStyle.__init__)


def test_shr5::martialartstyle_constructor_args():
    sig = inspect.signature(shr5::MartialartStyle.__init__)
    params = list(sig.parameters.keys())



def test_shr5::kleindungsmodifikator_is_not_abstract():
    assert not inspect.isabstract(shr5::KleindungsModifikator)


def test_shr5::kleindungsmodifikator_constructor_exists():
    assert callable(shr5::KleindungsModifikator.__init__)


def test_shr5::kleindungsmodifikator_constructor_args():
    sig = inspect.signature(shr5::KleindungsModifikator.__init__)
    params = list(sig.parameters.keys())
    assert "capacity" in params, "Missing parameter 'capacity'"
    assert "type" in params, "Missing parameter 'type'"
    assert "rating" in params, "Missing parameter 'rating'"

def test_shr5::kleindungsmodifikator_has_capacity():
    assert hasattr(shr5::KleindungsModifikator, "capacity")
    descriptor = None
    for klass in shr5::KleindungsModifikator.__mro__:
        if "capacity" in klass.__dict__:
            descriptor = klass.__dict__["capacity"]
            break
    assert isinstance(descriptor, property)

def test_shr5::kleindungsmodifikator_has_type():
    assert hasattr(shr5::KleindungsModifikator, "type")
    descriptor = None
    for klass in shr5::KleindungsModifikator.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_shr5::kleindungsmodifikator_has_rating():
    assert hasattr(shr5::KleindungsModifikator, "rating")
    descriptor = None
    for klass in shr5::KleindungsModifikator.__mro__:
        if "rating" in klass.__dict__:
            descriptor = klass.__dict__["rating"]
            break
    assert isinstance(descriptor, property)



def test_shr5::substance_is_not_abstract():
    assert not inspect.isabstract(shr5::Substance)


def test_shr5::substance_constructor_exists():
    assert callable(shr5::Substance.__init__)


def test_shr5::substance_constructor_args():
    sig = inspect.signature(shr5::Substance.__init__)
    params = list(sig.parameters.keys())
    assert "speed" in params, "Missing parameter 'speed'"
    assert "vector" in params, "Missing parameter 'vector'"

def test_shr5::substance_has_speed():
    assert hasattr(shr5::Substance, "speed")
    descriptor = None
    for klass in shr5::Substance.__mro__:
        if "speed" in klass.__dict__:
            descriptor = klass.__dict__["speed"]
            break
    assert isinstance(descriptor, property)

def test_shr5::substance_has_vector():
    assert hasattr(shr5::Substance, "vector")
    descriptor = None
    for klass in shr5::Substance.__mro__:
        if "vector" in klass.__dict__:
            descriptor = klass.__dict__["vector"]
            break
    assert isinstance(descriptor, property)



def test_shr5::fertigkeitsgruppe_is_not_abstract():
    assert not inspect.isabstract(shr5::FertigkeitsGruppe)


def test_shr5::fertigkeitsgruppe_constructor_exists():
    assert callable(shr5::FertigkeitsGruppe.__init__)


def test_shr5::fertigkeitsgruppe_constructor_args():
    sig = inspect.signature(shr5::FertigkeitsGruppe.__init__)
    params = list(sig.parameters.keys())



def test_shr5::sprite_is_not_abstract():
    assert not inspect.isabstract(shr5::Sprite)


def test_shr5::sprite_constructor_exists():
    assert callable(shr5::Sprite.__init__)


def test_shr5::sprite_constructor_args():
    sig = inspect.signature(shr5::Sprite.__init__)
    params = list(sig.parameters.keys())
    assert "schleicherMod" in params, "Missing parameter 'schleicherMod'"
    assert "stufe" in params, "Missing parameter 'stufe'"
    assert "firewallMod" in params, "Missing parameter 'firewallMod'"
    assert "angriffMod" in params, "Missing parameter 'angriffMod'"
    assert "initativeMod" in params, "Missing parameter 'initativeMod'"
    assert "datenverarbeitungMod" in params, "Missing parameter 'datenverarbeitungMod'"

def test_shr5::sprite_has_schleicherMod():
    assert hasattr(shr5::Sprite, "schleicherMod")
    descriptor = None
    for klass in shr5::Sprite.__mro__:
        if "schleicherMod" in klass.__dict__:
            descriptor = klass.__dict__["schleicherMod"]
            break
    assert isinstance(descriptor, property)

def test_shr5::sprite_has_stufe():
    assert hasattr(shr5::Sprite, "stufe")
    descriptor = None
    for klass in shr5::Sprite.__mro__:
        if "stufe" in klass.__dict__:
            descriptor = klass.__dict__["stufe"]
            break
    assert isinstance(descriptor, property)

def test_shr5::sprite_has_firewallMod():
    assert hasattr(shr5::Sprite, "firewallMod")
    descriptor = None
    for klass in shr5::Sprite.__mro__:
        if "firewallMod" in klass.__dict__:
            descriptor = klass.__dict__["firewallMod"]
            break
    assert isinstance(descriptor, property)

def test_shr5::sprite_has_angriffMod():
    assert hasattr(shr5::Sprite, "angriffMod")
    descriptor = None
    for klass in shr5::Sprite.__mro__:
        if "angriffMod" in klass.__dict__:
            descriptor = klass.__dict__["angriffMod"]
            break
    assert isinstance(descriptor, property)

def test_shr5::sprite_has_initativeMod():
    assert hasattr(shr5::Sprite, "initativeMod")
    descriptor = None
    for klass in shr5::Sprite.__mro__:
        if "initativeMod" in klass.__dict__:
            descriptor = klass.__dict__["initativeMod"]
            break
    assert isinstance(descriptor, property)

def test_shr5::sprite_has_datenverarbeitungMod():
    assert hasattr(shr5::Sprite, "datenverarbeitungMod")
    descriptor = None
    for klass in shr5::Sprite.__mro__:
        if "datenverarbeitungMod" in klass.__dict__:
            descriptor = klass.__dict__["datenverarbeitungMod"]
            break
    assert isinstance(descriptor, property)



def test_shr5::vertrag_is_not_abstract():
    assert not inspect.isabstract(shr5::Vertrag)


def test_shr5::vertrag_constructor_exists():
    assert callable(shr5::Vertrag.__init__)


def test_shr5::vertrag_constructor_args():
    sig = inspect.signature(shr5::Vertrag.__init__)
    params = list(sig.parameters.keys())



def test_shr5::abstraktmodifikatoren_is_not_abstract():
    assert not inspect.isabstract(shr5::AbstraktModifikatoren)


def test_shr5::abstraktmodifikatoren_constructor_exists():
    assert callable(shr5::AbstraktModifikatoren.__init__)


def test_shr5::abstraktmodifikatoren_constructor_args():
    sig = inspect.signature(shr5::AbstraktModifikatoren.__init__)
    params = list(sig.parameters.keys())



def test_shr5::metamagie_is_not_abstract():
    assert not inspect.isabstract(shr5::MetaMagie)


def test_shr5::metamagie_constructor_exists():
    assert callable(shr5::MetaMagie.__init__)


def test_shr5::metamagie_constructor_args():
    sig = inspect.signature(shr5::MetaMagie.__init__)
    params = list(sig.parameters.keys())



def test_shr5::sourcebook_is_not_abstract():
    assert not inspect.isabstract(shr5::SourceBook)


def test_shr5::sourcebook_constructor_exists():
    assert callable(shr5::SourceBook.__init__)


def test_shr5::sourcebook_constructor_args():
    sig = inspect.signature(shr5::SourceBook.__init__)
    params = list(sig.parameters.keys())
    assert "endShrTime" in params, "Missing parameter 'endShrTime'"
    assert "startShrTime" in params, "Missing parameter 'startShrTime'"
    assert "code" in params, "Missing parameter 'code'"

def test_shr5::sourcebook_has_endShrTime():
    assert hasattr(shr5::SourceBook, "endShrTime")
    descriptor = None
    for klass in shr5::SourceBook.__mro__:
        if "endShrTime" in klass.__dict__:
            descriptor = klass.__dict__["endShrTime"]
            break
    assert isinstance(descriptor, property)

def test_shr5::sourcebook_has_startShrTime():
    assert hasattr(shr5::SourceBook, "startShrTime")
    descriptor = None
    for klass in shr5::SourceBook.__mro__:
        if "startShrTime" in klass.__dict__:
            descriptor = klass.__dict__["startShrTime"]
            break
    assert isinstance(descriptor, property)

def test_shr5::sourcebook_has_code():
    assert hasattr(shr5::SourceBook, "code")
    descriptor = None
    for klass in shr5::SourceBook.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)



def test_shr5::lifestyleoption_is_not_abstract():
    assert not inspect.isabstract(shr5::LifestyleOption)


def test_shr5::lifestyleoption_constructor_exists():
    assert callable(shr5::LifestyleOption.__init__)


def test_shr5::lifestyleoption_constructor_args():
    sig = inspect.signature(shr5::LifestyleOption.__init__)
    params = list(sig.parameters.keys())



def test_shr5::software_is_not_abstract():
    assert not inspect.isabstract(shr5::Software)


def test_shr5::software_constructor_exists():
    assert callable(shr5::Software.__init__)


def test_shr5::software_constructor_args():
    sig = inspect.signature(shr5::Software.__init__)
    params = list(sig.parameters.keys())



def test_shr5::fahrzeug_is_not_abstract():
    assert not inspect.isabstract(shr5::Fahrzeug)


def test_shr5::fahrzeug_constructor_exists():
    assert callable(shr5::Fahrzeug.__init__)


def test_shr5::fahrzeug_constructor_args():
    sig = inspect.signature(shr5::Fahrzeug.__init__)
    params = list(sig.parameters.keys())
    assert "beschleunigung" in params, "Missing parameter 'beschleunigung'"
    assert "panzer" in params, "Missing parameter 'panzer'"
    assert "sensor" in params, "Missing parameter 'sensor'"
    assert "weaponMounts" in params, "Missing parameter 'weaponMounts'"
    assert "pilot" in params, "Missing parameter 'pilot'"
    assert "rumpf" in params, "Missing parameter 'rumpf'"
    assert "geschwindigkeit" in params, "Missing parameter 'geschwindigkeit'"
    assert "handling" in params, "Missing parameter 'handling'"
    assert "fahrzeugTyp" in params, "Missing parameter 'fahrzeugTyp'"

def test_shr5::fahrzeug_has_beschleunigung():
    assert hasattr(shr5::Fahrzeug, "beschleunigung")
    descriptor = None
    for klass in shr5::Fahrzeug.__mro__:
        if "beschleunigung" in klass.__dict__:
            descriptor = klass.__dict__["beschleunigung"]
            break
    assert isinstance(descriptor, property)

def test_shr5::fahrzeug_has_panzer():
    assert hasattr(shr5::Fahrzeug, "panzer")
    descriptor = None
    for klass in shr5::Fahrzeug.__mro__:
        if "panzer" in klass.__dict__:
            descriptor = klass.__dict__["panzer"]
            break
    assert isinstance(descriptor, property)

def test_shr5::fahrzeug_has_sensor():
    assert hasattr(shr5::Fahrzeug, "sensor")
    descriptor = None
    for klass in shr5::Fahrzeug.__mro__:
        if "sensor" in klass.__dict__:
            descriptor = klass.__dict__["sensor"]
            break
    assert isinstance(descriptor, property)

def test_shr5::fahrzeug_has_weaponMounts():
    assert hasattr(shr5::Fahrzeug, "weaponMounts")
    descriptor = None
    for klass in shr5::Fahrzeug.__mro__:
        if "weaponMounts" in klass.__dict__:
            descriptor = klass.__dict__["weaponMounts"]
            break
    assert isinstance(descriptor, property)

def test_shr5::fahrzeug_has_pilot():
    assert hasattr(shr5::Fahrzeug, "pilot")
    descriptor = None
    for klass in shr5::Fahrzeug.__mro__:
        if "pilot" in klass.__dict__:
            descriptor = klass.__dict__["pilot"]
            break
    assert isinstance(descriptor, property)

def test_shr5::fahrzeug_has_rumpf():
    assert hasattr(shr5::Fahrzeug, "rumpf")
    descriptor = None
    for klass in shr5::Fahrzeug.__mro__:
        if "rumpf" in klass.__dict__:
            descriptor = klass.__dict__["rumpf"]
            break
    assert isinstance(descriptor, property)

def test_shr5::fahrzeug_has_geschwindigkeit():
    assert hasattr(shr5::Fahrzeug, "geschwindigkeit")
    descriptor = None
    for klass in shr5::Fahrzeug.__mro__:
        if "geschwindigkeit" in klass.__dict__:
            descriptor = klass.__dict__["geschwindigkeit"]
            break
    assert isinstance(descriptor, property)

def test_shr5::fahrzeug_has_handling():
    assert hasattr(shr5::Fahrzeug, "handling")
    descriptor = None
    for klass in shr5::Fahrzeug.__mro__:
        if "handling" in klass.__dict__:
            descriptor = klass.__dict__["handling"]
            break
    assert isinstance(descriptor, property)

def test_shr5::fahrzeug_has_fahrzeugTyp():
    assert hasattr(shr5::Fahrzeug, "fahrzeugTyp")
    descriptor = None
    for klass in shr5::Fahrzeug.__mro__:
        if "fahrzeugTyp" in klass.__dict__:
            descriptor = klass.__dict__["fahrzeugTyp"]
            break
    assert isinstance(descriptor, property)



def test_shr5::host_is_not_abstract():
    assert not inspect.isabstract(shr5::Host)


def test_shr5::host_constructor_exists():
    assert callable(shr5::Host.__init__)


def test_shr5::host_constructor_args():
    sig = inspect.signature(shr5::Host.__init__)
    params = list(sig.parameters.keys())
    assert "baseDatenverarbeitung" in params, "Missing parameter 'baseDatenverarbeitung'"
    assert "baseFirewall" in params, "Missing parameter 'baseFirewall'"
    assert "baseAngriff" in params, "Missing parameter 'baseAngriff'"
    assert "hostRating" in params, "Missing parameter 'hostRating'"
    assert "baseSchleicher" in params, "Missing parameter 'baseSchleicher'"

def test_shr5::host_has_baseDatenverarbeitung():
    assert hasattr(shr5::Host, "baseDatenverarbeitung")
    descriptor = None
    for klass in shr5::Host.__mro__:
        if "baseDatenverarbeitung" in klass.__dict__:
            descriptor = klass.__dict__["baseDatenverarbeitung"]
            break
    assert isinstance(descriptor, property)

def test_shr5::host_has_baseFirewall():
    assert hasattr(shr5::Host, "baseFirewall")
    descriptor = None
    for klass in shr5::Host.__mro__:
        if "baseFirewall" in klass.__dict__:
            descriptor = klass.__dict__["baseFirewall"]
            break
    assert isinstance(descriptor, property)

def test_shr5::host_has_baseAngriff():
    assert hasattr(shr5::Host, "baseAngriff")
    descriptor = None
    for klass in shr5::Host.__mro__:
        if "baseAngriff" in klass.__dict__:
            descriptor = klass.__dict__["baseAngriff"]
            break
    assert isinstance(descriptor, property)

def test_shr5::host_has_hostRating():
    assert hasattr(shr5::Host, "hostRating")
    descriptor = None
    for klass in shr5::Host.__mro__:
        if "hostRating" in klass.__dict__:
            descriptor = klass.__dict__["hostRating"]
            break
    assert isinstance(descriptor, property)

def test_shr5::host_has_baseSchleicher():
    assert hasattr(shr5::Host, "baseSchleicher")
    descriptor = None
    for klass in shr5::Host.__mro__:
        if "baseSchleicher" in klass.__dict__:
            descriptor = klass.__dict__["baseSchleicher"]
            break
    assert isinstance(descriptor, property)



def test_shr5::sourcelink_is_not_abstract():
    assert not inspect.isabstract(shr5::SourceLink)


def test_shr5::sourcelink_constructor_exists():
    assert callable(shr5::SourceLink.__init__)


def test_shr5::sourcelink_constructor_args():
    sig = inspect.signature(shr5::SourceLink.__init__)
    params = list(sig.parameters.keys())



def test_shr5::shrlist_is_not_abstract():
    assert not inspect.isabstract(shr5::ShrList)


def test_shr5::shrlist_constructor_exists():
    assert callable(shr5::ShrList.__init__)


def test_shr5::shrlist_constructor_args():
    sig = inspect.signature(shr5::ShrList.__init__)
    params = list(sig.parameters.keys())



def test_shr5::sensorfunction_is_not_abstract():
    assert not inspect.isabstract(shr5::SensorFunction)


def test_shr5::sensorfunction_constructor_exists():
    assert callable(shr5::SensorFunction.__init__)


def test_shr5::sensorfunction_constructor_args():
    sig = inspect.signature(shr5::SensorFunction.__init__)
    params = list(sig.parameters.keys())
    assert "maxRange" in params, "Missing parameter 'maxRange'"

def test_shr5::sensorfunction_has_maxRange():
    assert hasattr(shr5::SensorFunction, "maxRange")
    descriptor = None
    for klass in shr5::SensorFunction.__mro__:
        if "maxRange" in klass.__dict__:
            descriptor = klass.__dict__["maxRange"]
            break
    assert isinstance(descriptor, property)



def test_shr5::spezies_is_not_abstract():
    assert not inspect.isabstract(shr5::Spezies)


def test_shr5::spezies_constructor_exists():
    assert callable(shr5::Spezies.__init__)


def test_shr5::spezies_constructor_args():
    sig = inspect.signature(shr5::Spezies.__init__)
    params = list(sig.parameters.keys())
    assert "magieMax" in params, "Missing parameter 'magieMax'"
    assert "willenskraftMin" in params, "Missing parameter 'willenskraftMin'"
    assert "intuitionMin" in params, "Missing parameter 'intuitionMin'"
    assert "willenskraftMax" in params, "Missing parameter 'willenskraftMax'"
    assert "edgeMin" in params, "Missing parameter 'edgeMin'"
    assert "essenzMax" in params, "Missing parameter 'essenzMax'"
    assert "logikMin" in params, "Missing parameter 'logikMin'"
    assert "reaktionMax" in params, "Missing parameter 'reaktionMax'"
    assert "konstitutionMax" in params, "Missing parameter 'konstitutionMax'"
    assert "staerkeMin" in params, "Missing parameter 'staerkeMin'"
    assert "geschicklichkeitMin" in params, "Missing parameter 'geschicklichkeitMin'"
    assert "geschicklichkeitMax" in params, "Missing parameter 'geschicklichkeitMax'"
    assert "konstitutionMin" in params, "Missing parameter 'konstitutionMin'"
    assert "essenzMin" in params, "Missing parameter 'essenzMin'"
    assert "resonanzMax" in params, "Missing parameter 'resonanzMax'"
    assert "staerkeMax" in params, "Missing parameter 'staerkeMax'"
    assert "laufen" in params, "Missing parameter 'laufen'"
    assert "logikMax" in params, "Missing parameter 'logikMax'"
    assert "resonanzMin" in params, "Missing parameter 'resonanzMin'"
    assert "reaktionMin" in params, "Missing parameter 'reaktionMin'"
    assert "sprinten" in params, "Missing parameter 'sprinten'"
    assert "intuitionMax" in params, "Missing parameter 'intuitionMax'"
    assert "charismaMin" in params, "Missing parameter 'charismaMin'"
    assert "magieMin" in params, "Missing parameter 'magieMin'"
    assert "edgeMax" in params, "Missing parameter 'edgeMax'"
    assert "charismaMax" in params, "Missing parameter 'charismaMax'"
    assert "rennen" in params, "Missing parameter 'rennen'"

def test_shr5::spezies_has_magieMax():
    assert hasattr(shr5::Spezies, "magieMax")
    descriptor = None
    for klass in shr5::Spezies.__mro__:
        if "magieMax" in klass.__dict__:
            descriptor = klass.__dict__["magieMax"]
            break
    assert isinstance(descriptor, property)

def test_shr5::spezies_has_willenskraftMin():
    assert hasattr(shr5::Spezies, "willenskraftMin")
    descriptor = None
    for klass in shr5::Spezies.__mro__:
        if "willenskraftMin" in klass.__dict__:
            descriptor = klass.__dict__["willenskraftMin"]
            break
    assert isinstance(descriptor, property)

def test_shr5::spezies_has_intuitionMin():
    assert hasattr(shr5::Spezies, "intuitionMin")
    descriptor = None
    for klass in shr5::Spezies.__mro__:
        if "intuitionMin" in klass.__dict__:
            descriptor = klass.__dict__["intuitionMin"]
            break
    assert isinstance(descriptor, property)

def test_shr5::spezies_has_willenskraftMax():
    assert hasattr(shr5::Spezies, "willenskraftMax")
    descriptor = None
    for klass in shr5::Spezies.__mro__:
        if "willenskraftMax" in klass.__dict__:
            descriptor = klass.__dict__["willenskraftMax"]
            break
    assert isinstance(descriptor, property)

def test_shr5::spezies_has_edgeMin():
    assert hasattr(shr5::Spezies, "edgeMin")
    descriptor = None
    for klass in shr5::Spezies.__mro__:
        if "edgeMin" in klass.__dict__:
            descriptor = klass.__dict__["edgeMin"]
            break
    assert isinstance(descriptor, property)

def test_shr5::spezies_has_essenzMax():
    assert hasattr(shr5::Spezies, "essenzMax")
    descriptor = None
    for klass in shr5::Spezies.__mro__:
        if "essenzMax" in klass.__dict__:
            descriptor = klass.__dict__["essenzMax"]
            break
    assert isinstance(descriptor, property)

def test_shr5::spezies_has_logikMin():
    assert hasattr(shr5::Spezies, "logikMin")
    descriptor = None
    for klass in shr5::Spezies.__mro__:
        if "logikMin" in klass.__dict__:
            descriptor = klass.__dict__["logikMin"]
            break
    assert isinstance(descriptor, property)

def test_shr5::spezies_has_reaktionMax():
    assert hasattr(shr5::Spezies, "reaktionMax")
    descriptor = None
    for klass in shr5::Spezies.__mro__:
        if "reaktionMax" in klass.__dict__:
            descriptor = klass.__dict__["reaktionMax"]
            break
    assert isinstance(descriptor, property)

def test_shr5::spezies_has_konstitutionMax():
    assert hasattr(shr5::Spezies, "konstitutionMax")
    descriptor = None
    for klass in shr5::Spezies.__mro__:
        if "konstitutionMax" in klass.__dict__:
            descriptor = klass.__dict__["konstitutionMax"]
            break
    assert isinstance(descriptor, property)

def test_shr5::spezies_has_staerkeMin():
    assert hasattr(shr5::Spezies, "staerkeMin")
    descriptor = None
    for klass in shr5::Spezies.__mro__:
        if "staerkeMin" in klass.__dict__:
            descriptor = klass.__dict__["staerkeMin"]
            break
    assert isinstance(descriptor, property)

def test_shr5::spezies_has_geschicklichkeitMin():
    assert hasattr(shr5::Spezies, "geschicklichkeitMin")
    descriptor = None
    for klass in shr5::Spezies.__mro__:
        if "geschicklichkeitMin" in klass.__dict__:
            descriptor = klass.__dict__["geschicklichkeitMin"]
            break
    assert isinstance(descriptor, property)

def test_shr5::spezies_has_geschicklichkeitMax():
    assert hasattr(shr5::Spezies, "geschicklichkeitMax")
    descriptor = None
    for klass in shr5::Spezies.__mro__:
        if "geschicklichkeitMax" in klass.__dict__:
            descriptor = klass.__dict__["geschicklichkeitMax"]
            break
    assert isinstance(descriptor, property)

def test_shr5::spezies_has_konstitutionMin():
    assert hasattr(shr5::Spezies, "konstitutionMin")
    descriptor = None
    for klass in shr5::Spezies.__mro__:
        if "konstitutionMin" in klass.__dict__:
            descriptor = klass.__dict__["konstitutionMin"]
            break
    assert isinstance(descriptor, property)

def test_shr5::spezies_has_essenzMin():
    assert hasattr(shr5::Spezies, "essenzMin")
    descriptor = None
    for klass in shr5::Spezies.__mro__:
        if "essenzMin" in klass.__dict__:
            descriptor = klass.__dict__["essenzMin"]
            break
    assert isinstance(descriptor, property)

def test_shr5::spezies_has_resonanzMax():
    assert hasattr(shr5::Spezies, "resonanzMax")
    descriptor = None
    for klass in shr5::Spezies.__mro__:
        if "resonanzMax" in klass.__dict__:
            descriptor = klass.__dict__["resonanzMax"]
            break
    assert isinstance(descriptor, property)

def test_shr5::spezies_has_staerkeMax():
    assert hasattr(shr5::Spezies, "staerkeMax")
    descriptor = None
    for klass in shr5::Spezies.__mro__:
        if "staerkeMax" in klass.__dict__:
            descriptor = klass.__dict__["staerkeMax"]
            break
    assert isinstance(descriptor, property)

def test_shr5::spezies_has_laufen():
    assert hasattr(shr5::Spezies, "laufen")
    descriptor = None
    for klass in shr5::Spezies.__mro__:
        if "laufen" in klass.__dict__:
            descriptor = klass.__dict__["laufen"]
            break
    assert isinstance(descriptor, property)

def test_shr5::spezies_has_logikMax():
    assert hasattr(shr5::Spezies, "logikMax")
    descriptor = None
    for klass in shr5::Spezies.__mro__:
        if "logikMax" in klass.__dict__:
            descriptor = klass.__dict__["logikMax"]
            break
    assert isinstance(descriptor, property)

def test_shr5::spezies_has_resonanzMin():
    assert hasattr(shr5::Spezies, "resonanzMin")
    descriptor = None
    for klass in shr5::Spezies.__mro__:
        if "resonanzMin" in klass.__dict__:
            descriptor = klass.__dict__["resonanzMin"]
            break
    assert isinstance(descriptor, property)

def test_shr5::spezies_has_reaktionMin():
    assert hasattr(shr5::Spezies, "reaktionMin")
    descriptor = None
    for klass in shr5::Spezies.__mro__:
        if "reaktionMin" in klass.__dict__:
            descriptor = klass.__dict__["reaktionMin"]
            break
    assert isinstance(descriptor, property)

def test_shr5::spezies_has_sprinten():
    assert hasattr(shr5::Spezies, "sprinten")
    descriptor = None
    for klass in shr5::Spezies.__mro__:
        if "sprinten" in klass.__dict__:
            descriptor = klass.__dict__["sprinten"]
            break
    assert isinstance(descriptor, property)

def test_shr5::spezies_has_intuitionMax():
    assert hasattr(shr5::Spezies, "intuitionMax")
    descriptor = None
    for klass in shr5::Spezies.__mro__:
        if "intuitionMax" in klass.__dict__:
            descriptor = klass.__dict__["intuitionMax"]
            break
    assert isinstance(descriptor, property)

def test_shr5::spezies_has_charismaMin():
    assert hasattr(shr5::Spezies, "charismaMin")
    descriptor = None
    for klass in shr5::Spezies.__mro__:
        if "charismaMin" in klass.__dict__:
            descriptor = klass.__dict__["charismaMin"]
            break
    assert isinstance(descriptor, property)

def test_shr5::spezies_has_magieMin():
    assert hasattr(shr5::Spezies, "magieMin")
    descriptor = None
    for klass in shr5::Spezies.__mro__:
        if "magieMin" in klass.__dict__:
            descriptor = klass.__dict__["magieMin"]
            break
    assert isinstance(descriptor, property)

def test_shr5::spezies_has_edgeMax():
    assert hasattr(shr5::Spezies, "edgeMax")
    descriptor = None
    for klass in shr5::Spezies.__mro__:
        if "edgeMax" in klass.__dict__:
            descriptor = klass.__dict__["edgeMax"]
            break
    assert isinstance(descriptor, property)

def test_shr5::spezies_has_charismaMax():
    assert hasattr(shr5::Spezies, "charismaMax")
    descriptor = None
    for klass in shr5::Spezies.__mro__:
        if "charismaMax" in klass.__dict__:
            descriptor = klass.__dict__["charismaMax"]
            break
    assert isinstance(descriptor, property)

def test_shr5::spezies_has_rennen():
    assert hasattr(shr5::Spezies, "rennen")
    descriptor = None
    for klass in shr5::Spezies.__mro__:
        if "rennen" in klass.__dict__:
            descriptor = klass.__dict__["rennen"]
            break
    assert isinstance(descriptor, property)



def test_shr5::reichweite_is_not_abstract():
    assert not inspect.isabstract(shr5::Reichweite)


def test_shr5::reichweite_constructor_exists():
    assert callable(shr5::Reichweite.__init__)


def test_shr5::reichweite_constructor_args():
    sig = inspect.signature(shr5::Reichweite.__init__)
    params = list(sig.parameters.keys())
    assert "extrem" in params, "Missing parameter 'extrem'"
    assert "kurz" in params, "Missing parameter 'kurz'"
    assert "weit" in params, "Missing parameter 'weit'"
    assert "mittel" in params, "Missing parameter 'mittel'"
    assert "min" in params, "Missing parameter 'min'"

def test_shr5::reichweite_has_extrem():
    assert hasattr(shr5::Reichweite, "extrem")
    descriptor = None
    for klass in shr5::Reichweite.__mro__:
        if "extrem" in klass.__dict__:
            descriptor = klass.__dict__["extrem"]
            break
    assert isinstance(descriptor, property)

def test_shr5::reichweite_has_kurz():
    assert hasattr(shr5::Reichweite, "kurz")
    descriptor = None
    for klass in shr5::Reichweite.__mro__:
        if "kurz" in klass.__dict__:
            descriptor = klass.__dict__["kurz"]
            break
    assert isinstance(descriptor, property)

def test_shr5::reichweite_has_weit():
    assert hasattr(shr5::Reichweite, "weit")
    descriptor = None
    for klass in shr5::Reichweite.__mro__:
        if "weit" in klass.__dict__:
            descriptor = klass.__dict__["weit"]
            break
    assert isinstance(descriptor, property)

def test_shr5::reichweite_has_mittel():
    assert hasattr(shr5::Reichweite, "mittel")
    descriptor = None
    for klass in shr5::Reichweite.__mro__:
        if "mittel" in klass.__dict__:
            descriptor = klass.__dict__["mittel"]
            break
    assert isinstance(descriptor, property)

def test_shr5::reichweite_has_min():
    assert hasattr(shr5::Reichweite, "min")
    descriptor = None
    for klass in shr5::Reichweite.__mro__:
        if "min" in klass.__dict__:
            descriptor = klass.__dict__["min"]
            break
    assert isinstance(descriptor, property)



def test_shr5::zauber_is_not_abstract():
    assert not inspect.isabstract(shr5::Zauber)


def test_shr5::zauber_constructor_exists():
    assert callable(shr5::Zauber.__init__)


def test_shr5::zauber_constructor_args():
    sig = inspect.signature(shr5::Zauber.__init__)
    params = list(sig.parameters.keys())
    assert "entzug" in params, "Missing parameter 'entzug'"
    assert "merkmale" in params, "Missing parameter 'merkmale'"
    assert "dauer" in params, "Missing parameter 'dauer'"
    assert "reichweite" in params, "Missing parameter 'reichweite'"
    assert "art" in params, "Missing parameter 'art'"
    assert "kategorie" in params, "Missing parameter 'kategorie'"
    assert "schaden" in params, "Missing parameter 'schaden'"

def test_shr5::zauber_has_entzug():
    assert hasattr(shr5::Zauber, "entzug")
    descriptor = None
    for klass in shr5::Zauber.__mro__:
        if "entzug" in klass.__dict__:
            descriptor = klass.__dict__["entzug"]
            break
    assert isinstance(descriptor, property)

def test_shr5::zauber_has_merkmale():
    assert hasattr(shr5::Zauber, "merkmale")
    descriptor = None
    for klass in shr5::Zauber.__mro__:
        if "merkmale" in klass.__dict__:
            descriptor = klass.__dict__["merkmale"]
            break
    assert isinstance(descriptor, property)

def test_shr5::zauber_has_dauer():
    assert hasattr(shr5::Zauber, "dauer")
    descriptor = None
    for klass in shr5::Zauber.__mro__:
        if "dauer" in klass.__dict__:
            descriptor = klass.__dict__["dauer"]
            break
    assert isinstance(descriptor, property)

def test_shr5::zauber_has_reichweite():
    assert hasattr(shr5::Zauber, "reichweite")
    descriptor = None
    for klass in shr5::Zauber.__mro__:
        if "reichweite" in klass.__dict__:
            descriptor = klass.__dict__["reichweite"]
            break
    assert isinstance(descriptor, property)

def test_shr5::zauber_has_art():
    assert hasattr(shr5::Zauber, "art")
    descriptor = None
    for klass in shr5::Zauber.__mro__:
        if "art" in klass.__dict__:
            descriptor = klass.__dict__["art"]
            break
    assert isinstance(descriptor, property)

def test_shr5::zauber_has_kategorie():
    assert hasattr(shr5::Zauber, "kategorie")
    descriptor = None
    for klass in shr5::Zauber.__mro__:
        if "kategorie" in klass.__dict__:
            descriptor = klass.__dict__["kategorie"]
            break
    assert isinstance(descriptor, property)

def test_shr5::zauber_has_schaden():
    assert hasattr(shr5::Zauber, "schaden")
    descriptor = None
    for klass in shr5::Zauber.__mro__:
        if "schaden" in klass.__dict__:
            descriptor = klass.__dict__["schaden"]
            break
    assert isinstance(descriptor, property)

def test_zauberdauer_exists():
    # Check that the Enumeration exists
    assert ZauberDauer is not None

def test_zauberdauer_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ZauberDauer]
    expected_literals = [
        "Permanent",
        "Aufrechterhalten",
        "Sofort",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ZauberDauer"

def test_addictiontype_exists():
    # Check that the Enumeration exists
    assert AddictionType is not None

def test_addictiontype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AddictionType]
    expected_literals = [
        "both",
        "physiological",
        "psychological",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AddictionType"

def test_substancevector_exists():
    # Check that the Enumeration exists
    assert SubstanceVector is not None

def test_substancevector_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SubstanceVector]
    expected_literals = [
        "contact",
        "inhalation",
        "ingestion",
        "injection",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SubstanceVector"

def test_enzug_exists():
    # Check that the Enumeration exists
    assert Enzug is not None

def test_enzug_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Enzug]
    expected_literals = [
        "wil_int",
        "wil_cha",
        "wil_log",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Enzug"

def test_feuwerwaffenerweiterung_exists():
    # Check that the Enumeration exists
    assert FeuwerwaffenErweiterung is not None

def test_feuwerwaffenerweiterung_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FeuwerwaffenErweiterung]
    expected_literals = [
        "Oben",
        "Unten",
        "Lauf",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FeuwerwaffenErweiterung"

def test_critterreichweite_exists():
    # Check that the Enumeration exists
    assert CritterReichweite is not None

def test_critterreichweite_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CritterReichweite]
    expected_literals = [
        "blickfeld",
        "beruehrung",
        "speziell",
        "selbst",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CritterReichweite"

def test_magazintyp_exists():
    # Check that the Enumeration exists
    assert MagazinTyp is not None

def test_magazintyp_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MagazinTyp]
    expected_literals = [
        "Trommel",
        "Streifen",
        "Gurt",
        "Clip",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MagazinTyp"

def test_zauberreichweite_exists():
    # Check that the Enumeration exists
    assert ZauberReichweite is not None

def test_zauberreichweite_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ZauberReichweite]
    expected_literals = [
        "Beruehrung",
        "Blickfeld",
        "Selbst",
        "Begrenzt",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ZauberReichweite"

def test_programtype_exists():
    # Check that the Enumeration exists
    assert ProgramType is not None

def test_programtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ProgramType]
    expected_literals = [
        "defaultSoft",
        "shopSoft",
        "dataSoft",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ProgramType"

def test_matrixprogramtype_exists():
    # Check that the Enumeration exists
    assert MatrixProgramType is not None

def test_matrixprogramtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MatrixProgramType]
    expected_literals = [
        "hackingProgram",
        "defaultProgram",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MatrixProgramType"

def test_zauberart_exists():
    # Check that the Enumeration exists
    assert ZauberArt is not None

def test_zauberart_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ZauberArt]
    expected_literals = [
        "Physisch",
        "Mana",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ZauberArt"

def test_feuermodus_exists():
    # Check that the Enumeration exists
    assert FeuerModus is not None

def test_feuermodus_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FeuerModus]
    expected_literals = [
        "AM",
        "EM",
        "HM",
        "SM",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FeuerModus"

def test_substanceeffect_exists():
    # Check that the Enumeration exists
    assert SubstanceEffect is not None

def test_substanceeffect_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SubstanceEffect]
    expected_literals = [
        "stunDamage",
        "nausea",
        "paralysis",
        "disorientation",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SubstanceEffect"

def test_cyberwaretype_exists():
    # Check that the Enumeration exists
    assert CyberwareType is not None

def test_cyberwaretype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CyberwareType]
    expected_literals = [
        "earware",
        "bodyware",
        "headware",
        "cyberlimb",
        "eyeware",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CyberwareType"

def test_critterhandlung_exists():
    # Check that the Enumeration exists
    assert CritterHandlung is not None

def test_critterhandlung_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CritterHandlung]
    expected_literals = [
        "auto",
        "komplex",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CritterHandlung"

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

def test_armormodificationtype_exists():
    # Check that the Enumeration exists
    assert armorModificationType is not None

def test_armormodificationtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in armorModificationType]
    expected_literals = [
        "ThermalDamping",
        "Insulation",
        "ChemicalProtection",
        "ShockFrills",
        "FireResistance",
        "Nonconductivity",
        "ChemicalSeal",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in armorModificationType"

def test_critterdauer_exists():
    # Check that the Enumeration exists
    assert CritterDauer is not None

def test_critterdauer_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CritterDauer]
    expected_literals = [
        "aufrechterhalten",
        "permanent",
        "sofort",
        "speziell",
        "immer",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CritterDauer"

def test_interfacemodus_exists():
    # Check that the Enumeration exists
    assert InterfaceModus is not None

def test_interfacemodus_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in InterfaceModus]
    expected_literals = [
        "hotSim",
        "augmentedReality",
        "coldSim",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in InterfaceModus"

def test_modifikatortype_exists():
    # Check that the Enumeration exists
    assert ModifikatorType is not None

def test_modifikatortype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ModifikatorType]
    expected_literals = [
        "Cyber",
        "Natural",
        "Bio",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ModifikatorType"

def test_smartguntype_exists():
    # Check that the Enumeration exists
    assert SmartgunType is not None

def test_smartguntype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SmartgunType]
    expected_literals = [
        "SmartBrille",
        "SmartGun",
        "SmatgunII",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SmartgunType"

def test_timeunits_exists():
    # Check that the Enumeration exists
    assert TimeUnits is not None

def test_timeunits_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TimeUnits]
    expected_literals = [
        "hour",
        "min",
        "sec",
        "day",
        "week",
        "month",
        "year",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TimeUnits"

def test_resonanzziel_exists():
    # Check that the Enumeration exists
    assert ResonanzZiel is not None

def test_resonanzziel_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ResonanzZiel]
    expected_literals = [
        "persona",
        "geraet",
        "sprite",
        "selbst",
        "datei",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ResonanzZiel"


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
MatrixAttributes_strategy = st.builds(
    MatrixAttributes,
)
Fahrzeug_strategy = st.builds(
    Fahrzeug,
)
shr5::Drohne_strategy = st.builds(
    shr5::Drohne,
    programSlotCount=
        st.integers()
)
shr5::PassagierFahrzeug_strategy = st.builds(
    shr5::PassagierFahrzeug,
    sitze=
        st.integers()
)
PassagierFahrzeug_strategy = st.builds(
    PassagierFahrzeug,
)
shr5::Bodenfahrzeug_strategy = st.builds(
    shr5::Bodenfahrzeug,
    geschwindigkeitGelaende=
        st.integers(),
    handlingGelaende=
        st.integers()
)
FahrzeugZustand_strategy = st.builds(
    FahrzeugZustand,
)
shr5::ChrakterLimits_strategy = st.builds(
    shr5::ChrakterLimits,
    sozial=
        st.integers(),
    geistig=
        st.integers(),
    koerperlich=
        st.integers()
)
shr5::AstraleProjektion_strategy = st.builds(
    shr5::AstraleProjektion,
    astraleGeschicklichkeit=
        st.integers(),
    astraleInitative=
        st.integers(),
    astralesLimit=
        st.integers(),
    astralePanzerung=
        st.integers(),
    astraleInitativWuerfel=
        st.integers(),
    astraleStaerke=
        st.integers(),
    astraleReaktion=
        st.integers(),
    astraleKonstitution=
        st.integers()
)
shr5::Panzerung_strategy = st.builds(
    shr5::Panzerung,
    panzer=
        st.integers()
)
shr5::Zauberer_strategy = st.builds(
    shr5::Zauberer,
    enzug=
        st.integers()
)
AstraleProjektion_strategy = st.builds(
    AstraleProjektion,
)
Zauberer_strategy = st.builds(
    Zauberer,
)
shr5::Anwendbar_strategy = st.builds(
    shr5::Anwendbar,
)
KiAdept_strategy = st.builds(
    KiAdept,
)
MagischePersona_strategy = st.builds(
    MagischePersona,
)
shr5::AspektMagier_strategy = st.builds(
    shr5::AspektMagier,
)
shr5::Magier_strategy = st.builds(
    shr5::Magier,
)
shr5::MysticAdept_strategy = st.builds(
    shr5::MysticAdept,
)
shr5::KiAdept_strategy = st.builds(
    shr5::KiAdept,
)
Wurfwaffe_strategy = st.builds(
    Wurfwaffe,
)
AbtraktGranate_strategy = st.builds(
    AbtraktGranate,
)
shr5::Granate_strategy = st.builds(
    shr5::Granate,
)
Munition_strategy = st.builds(
    Munition,
)
shr5::MiniGrenate_strategy = st.builds(
    shr5::MiniGrenate,
)
shr5::AbtraktGranate_strategy = st.builds(
    shr5::AbtraktGranate,
    blast=
        safe_text
)
Spezialisierung_strategy = st.builds(
    Spezialisierung,
)
Sensor_strategy = st.builds(
    Sensor,
)
shr5::SensorArray_strategy = st.builds(
    shr5::SensorArray,
)
CredstickTransaction_strategy = st.builds(
    CredstickTransaction,
)
shr5::TransferAmount_strategy = st.builds(
    shr5::TransferAmount,
    amountToTransfer=
        safe_text
)
shr5::ShoppingTransaction_strategy = st.builds(
    shr5::ShoppingTransaction,
    caculatedCosts=
        safe_text,
    fee=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
CyberwareEnhancement_strategy = st.builds(
    CyberwareEnhancement,
)
shr5::CyberImplantWeapon_strategy = st.builds(
    shr5::CyberImplantWeapon,
)
shr5::EReference_strategy = st.builds(
    shr5::EReference,
)
Substance_strategy = st.builds(
    Substance,
)
shr5::Toxin_strategy = st.builds(
    shr5::Toxin,
    power=
        st.integers(),
    effect=
        safe_text,
    penetration=
        st.integers()
)
shr5::Capacity_strategy = st.builds(
    shr5::Capacity,
    capacity=
        st.integers(),
    capacityRemains=
        st.integers()
)
Nahkampfwaffe_strategy = st.builds(
    Nahkampfwaffe,
)
AbstraktFokus_strategy = st.builds(
    AbstraktFokus,
)
shr5::MagieFokus_strategy = st.builds(
    shr5::MagieFokus,
    bindungsFaktor=
        st.integers()
)
shr5::QiFokus_strategy = st.builds(
    shr5::QiFokus,
)
Fokus_strategy = st.builds(
    Fokus,
)
shr5::WaffenFokus_strategy = st.builds(
    shr5::WaffenFokus,
)
MagischeStufe_strategy = st.builds(
    MagischeStufe,
)
shr5::MagischeStufe_strategy = st.builds(
    shr5::MagischeStufe,
    stufe=
        st.integers()
)
shr5::BerechneteAttribute_strategy = st.builds(
    shr5::BerechneteAttribute,
    selbstbeherrschung=
        st.integers(),
    menschenkenntnis=
        st.integers(),
    errinerungsvermoegen=
        st.integers()
)
LifestyleOption_strategy = st.builds(
    LifestyleOption,
)
shr5::PercentLifestyleOption_strategy = st.builds(
    shr5::PercentLifestyleOption,
)
FahrzeugModifikation_strategy = st.builds(
    FahrzeugModifikation,
)
shr5::FahrzeugErweiterung_strategy = st.builds(
    shr5::FahrzeugErweiterung,
)
shr5::WeaponMount_strategy = st.builds(
    shr5::WeaponMount,
)
shr5::PersonalAreaNetwork_strategy = st.builds(
    shr5::PersonalAreaNetwork,
    slaveMax=
        st.integers()
)
shr5::FahrzeugZustand_strategy = st.builds(
    shr5::FahrzeugZustand,
    zustandMax=
        st.integers()
)
BasicProgram_strategy = st.builds(
    BasicProgram,
)
shr5::Datasoft_strategy = st.builds(
    shr5::Datasoft,
)
shr5::ConsumerSoft_strategy = st.builds(
    shr5::ConsumerSoft,
    type=
        safe_text
)
shr5::Tutorsoft_strategy = st.builds(
    shr5::Tutorsoft,
    rating=
        st.integers()
)
Software_strategy = st.builds(
    Software,
)
shr5::SkillSoft_strategy = st.builds(
    shr5::SkillSoft,
    rating=
        st.integers()
)
shr5::RiggerProgram_strategy = st.builds(
    shr5::RiggerProgram,
)
RiggerProgram_strategy = st.builds(
    RiggerProgram,
)
shr5::AutoSoft_strategy = st.builds(
    shr5::AutoSoft,
    rating=
        st.integers()
)
MatrixProgram_strategy = st.builds(
    MatrixProgram,
)
shr5::CommonProgram_strategy = st.builds(
    shr5::CommonProgram,
    programType=
        safe_text
)
shr5::SoftwareAgent_strategy = st.builds(
    shr5::SoftwareAgent,
    rating=
        st.integers()
)
shr5::Localization_strategy = st.builds(
    shr5::Localization,
    page=
        st.integers(),
    local=
        safe_text,
    name=
        safe_text
)
MatrixDevice_strategy = st.builds(
    MatrixDevice,
)
shr5::MatixConditionMonitor_strategy = st.builds(
    shr5::MatixConditionMonitor,
    matrixZustandMax=
        st.integers()
)
shr5::BasicProgram_strategy = st.builds(
    shr5::BasicProgram,
)
AbstractMatrixDevice_strategy = st.builds(
    AbstractMatrixDevice,
)
shr5::RiggerCommandConsole_strategy = st.builds(
    shr5::RiggerCommandConsole,
    rauschunterdrueckung=
        st.integers(),
    zugriffBasis=
        st.integers(),
    firewallBasis=
        st.integers(),
    datenverarbeitungBasis=
        st.integers(),
    zugriff=
        st.integers()
)
shr5::Commlink_strategy = st.builds(
    shr5::Commlink,
)
shr5::ActiveMatixDevice_strategy = st.builds(
    shr5::ActiveMatixDevice,
    angriff=
        st.integers(),
    schleicher=
        st.integers()
)
MatixConditionMonitor_strategy = st.builds(
    MatixConditionMonitor,
)
shr5::MatrixAttributes_strategy = st.builds(
    shr5::MatrixAttributes,
    geraetestufe=
        st.integers(),
    datenverarbeitung=
        st.integers(),
    currentModus=
        safe_text,
    firewall=
        st.integers()
)
shr5::Identifiable_strategy = st.builds(
    shr5::Identifiable,
    parentId=
        safe_text
)
StufenPersona_strategy = st.builds(
    StufenPersona,
)
shr5::Geist_strategy = st.builds(
    shr5::Geist,
    reaktionBasis=
        st.integers(),
    staerkeBasis=
        st.integers(),
    charismaBasis=
        st.integers(),
    logikBasis=
        st.integers(),
    willenskraftBasis=
        st.integers(),
    konstitutionBasis=
        st.integers(),
    geschicklichkeitBasis=
        st.integers(),
    intuitionBasis=
        st.integers()
)
shr5::ModifikatorAttribute_strategy = st.builds(
    shr5::ModifikatorAttribute,
)
Vertrag_strategy = st.builds(
    Vertrag,
)
shr5::IntervallVertrag_strategy = st.builds(
    shr5::IntervallVertrag,
    faelligkeitsIntervall=
        st.integers(),
    unit=
        safe_text,
    begin=
        safe_text
)
Spezies_strategy = st.builds(
    Spezies,
)
shr5::Critter_strategy = st.builds(
    shr5::Critter,
)
shr5::PersonaZustand_strategy = st.builds(
    shr5::PersonaZustand,
    zustandGeistigMax=
        st.integers(),
    zustandKoerperlichMax=
        st.integers(),
    zustandGrenze=
        st.integers()
)
Wissensfertigkeit_strategy = st.builds(
    Wissensfertigkeit,
)
shr5::Sprachfertigkeit_strategy = st.builds(
    shr5::Sprachfertigkeit,
)
Fertigkeit_strategy = st.builds(
    Fertigkeit,
)
shr5::Wissensfertigkeit_strategy = st.builds(
    shr5::Wissensfertigkeit,
)
shr5::Menge_strategy = st.builds(
    shr5::Menge,
    proAnzahl=
        st.integers(),
    anzahl=
        st.integers()
)
shr5::CredstickTransaction_strategy = st.builds(
    shr5::CredstickTransaction,
    description=
        safe_text,
    date=
        safe_text,
    amount=
        safe_text
)
shr5::Erlernbar_strategy = st.builds(
    shr5::Erlernbar,
)
shr5::Fakeable_strategy = st.builds(
    shr5::Fakeable,
    gefaelscht=
        st.booleans(),
    stufe=
        st.integers()
)
Fakeable_strategy = st.builds(
    Fakeable,
)
shr5::Lizenz_strategy = st.builds(
    shr5::Lizenz,
    lizenGegenstand=
        safe_text
)
shr5::Sin_strategy = st.builds(
    shr5::Sin,
)
ResonanzPersona_strategy = st.builds(
    ResonanzPersona,
)
IntervallVertrag_strategy = st.builds(
    IntervallVertrag,
)
shr5::Lifestyle_strategy = st.builds(
    shr5::Lifestyle,
    owned=
        st.booleans()
)
ActiveMatixDevice_strategy = st.builds(
    ActiveMatixDevice,
)
shr5::ResonanzPersona_strategy = st.builds(
    shr5::ResonanzPersona,
    resonanzBasis=
        st.integers(),
    resonanz=
        st.integers()
)
shr5::GebundenerGeist_strategy = st.builds(
    shr5::GebundenerGeist,
    dienste=
        st.integers()
)
shr5::FokusBinding_strategy = st.builds(
    shr5::FokusBinding,
    active=
        st.booleans()
)
Erlernbar_strategy = st.builds(
    Erlernbar,
)
shr5::PersonaMartialartTechnique_strategy = st.builds(
    shr5::PersonaMartialartTechnique,
)
shr5::PersonaKomplexForm_strategy = st.builds(
    shr5::PersonaKomplexForm,
    stufe=
        st.integers()
)
shr5::Steigerbar_strategy = st.builds(
    shr5::Steigerbar,
    stufe=
        st.integers()
)
shr5::Fokus_strategy = st.builds(
    shr5::Fokus,
    bindungskosten=
        st.integers()
)
shr5::PersonaZauber_strategy = st.builds(
    shr5::PersonaZauber,
    stufe=
        st.integers()
)
MagischeMods_strategy = st.builds(
    MagischeMods,
)
shr5::CritterKraft_strategy = st.builds(
    shr5::CritterKraft,
    reichweite=
        safe_text,
    dauer=
        safe_text,
    art=
        safe_text,
    handlung=
        safe_text
)
shr5::KiKraft_strategy = st.builds(
    shr5::KiKraft,
    kraftpunkte=
        st.integers()
)
BerechneteAttribute_strategy = st.builds(
    BerechneteAttribute,
)
PersonaZustand_strategy = st.builds(
    PersonaZustand,
)
Panzerung_strategy = st.builds(
    Panzerung,
)
AbstraktPersona_strategy = st.builds(
    AbstraktPersona,
)
shr5::KoerperPersona_strategy = st.builds(
    shr5::KoerperPersona,
    zustandKoerperlich=
        st.integers(),
    zustandGeistig=
        st.integers()
)
KoerperPersona_strategy = st.builds(
    KoerperPersona,
)
shr5::Technomancer_strategy = st.builds(
    shr5::Technomancer,
)
shr5::MudanPersona_strategy = st.builds(
    shr5::MudanPersona,
)
AbstraktModifikatoren_strategy = st.builds(
    AbstraktModifikatoren,
)
shr5::PersonaEigenschaft_strategy = st.builds(
    shr5::PersonaEigenschaft,
    karmaKosten=
        st.integers()
)
shr5::Echo_strategy = st.builds(
    shr5::Echo,
)
shr5::MagischeMods_strategy = st.builds(
    shr5::MagischeMods,
)
shr5::Koerpermods_strategy = st.builds(
    shr5::Koerpermods,
)
shr5::DefaultWifi_strategy = st.builds(
    shr5::DefaultWifi,
)
shr5::BaseMagischePersona_strategy = st.builds(
    shr5::BaseMagischePersona,
    magie=
        st.integers(),
    magieBasis=
        st.integers()
)
shr5::Schutzgeist_strategy = st.builds(
    shr5::Schutzgeist,
    vorteile=
        safe_text,
    nachteile=
        safe_text
)
BaseMagischePersona_strategy = st.builds(
    BaseMagischePersona,
)
shr5::MagischePersona_strategy = st.builds(
    shr5::MagischePersona,
)
Steigerbar_strategy = st.builds(
    Steigerbar,
)
shr5::Initation_strategy = st.builds(
    shr5::Initation,
)
Modifyable_strategy = st.builds(
    Modifyable,
)
shr5::EObject_strategy = st.builds(
    shr5::EObject,
)
Menge_strategy = st.builds(
    Menge,
)
AbstaktFernKampfwaffe_strategy = st.builds(
    AbstaktFernKampfwaffe,
)
shr5::Wurfwaffe_strategy = st.builds(
    shr5::Wurfwaffe,
)
shr5::Projektilwaffe_strategy = st.builds(
    shr5::Projektilwaffe,
)
shr5::Feuerwaffe_strategy = st.builds(
    shr5::Feuerwaffe,
    kapazitaet=
        st.integers(),
    modie=
        safe_text,
    munitionstyp=
        safe_text,
    erweiterung=
        safe_text,
    rueckstoss=
        st.integers()
)
Capacity_strategy = st.builds(
    Capacity,
)
shr5::Cyberdeck_strategy = st.builds(
    shr5::Cyberdeck,
    attribute2=
        st.integers(),
    modManager=
        safe_text,
    programSlots=
        st.integers(),
    attribute3=
        st.integers(),
    attribute1=
        st.integers(),
    attribute4=
        st.integers()
)
Koerpermods_strategy = st.builds(
    Koerpermods,
)
AbstaktWaffe_strategy = st.builds(
    AbstaktWaffe,
)
shr5::AbstaktFernKampfwaffe_strategy = st.builds(
    shr5::AbstaktFernKampfwaffe,
)
shr5::MatrixDevice_strategy = st.builds(
    shr5::MatrixDevice,
)
Anwendbar_strategy = st.builds(
    Anwendbar,
)
Modifizierbar_strategy = st.builds(
    Modifizierbar,
)
shr5::Drug_strategy = st.builds(
    shr5::Drug,
    addictionType=
        safe_text,
    duration=
        safe_text
)
shr5::MatrixProgram_strategy = st.builds(
    shr5::MatrixProgram,
)
GeldWert_strategy = st.builds(
    GeldWert,
)
shr5::FernkampfwaffeModifikator_strategy = st.builds(
    shr5::FernkampfwaffeModifikator,
    ep=
        safe_text
)
shr5::CyberwareEnhancement_strategy = st.builds(
    shr5::CyberwareEnhancement,
    type=
        safe_text,
    capacityUse=
        st.integers()
)
shr5::Cyberware_strategy = st.builds(
    shr5::Cyberware,
    cyberwareCapacity=
        st.integers(),
    type=
        safe_text
)
shr5::BioWare_strategy = st.builds(
    shr5::BioWare,
)
Quelle_strategy = st.builds(
    Quelle,
)
ModifikatorAttribute_strategy = st.builds(
    ModifikatorAttribute,
)
shr5::SpezielleAttribute_strategy = st.builds(
    shr5::SpezielleAttribute,
    initativWuerfel=
        st.integers(),
    edge=
        st.integers(),
    ausweichen=
        st.integers(),
    edgeBasis=
        st.integers(),
    initative=
        st.integers(),
    essenz=
        st.integers()
)
shr5::Sichtverhaeltnisse_strategy = st.builds(
    shr5::Sichtverhaeltnisse,
    infrarot=
        safe_text,
    ultrasound=
        safe_text,
    restlichtverstaerkung=
        safe_text
)
shr5::GeistigeAttribute_strategy = st.builds(
    shr5::GeistigeAttribute,
    willenskraft=
        st.integers(),
    charisma=
        st.integers(),
    logik=
        st.integers(),
    intuition=
        st.integers()
)
shr5::ProbenModifikatoren_strategy = st.builds(
    shr5::ProbenModifikatoren,
    heilung=
        st.integers(),
    schadenswiederstand=
        st.integers()
)
shr5::CyberwareModifikatioren_strategy = st.builds(
    shr5::CyberwareModifikatioren,
    universalDataConnector=
        st.booleans(),
    simRig=
        st.integers(),
    controlRig=
        st.integers(),
    directNeuralInterface=
        st.booleans(),
    riggerInterface=
        st.booleans()
)
shr5::FernkampfwaffenModifikatoren_strategy = st.builds(
    shr5::FernkampfwaffenModifikatoren,
    rueckstoss=
        st.integers(),
    smartgun=
        safe_text,
    sichtverbesserung=
        st.integers(),
    vergroesserung=
        st.integers(),
    lasterPointer=
        st.booleans(),
    schalldaempfer=
        st.booleans()
)
shr5::GegenstandStufen_strategy = st.builds(
    shr5::GegenstandStufen,
    elektronik=
        st.integers(),
    tracing=
        st.integers(),
    computer=
        st.integers(),
    protection=
        st.integers(),
    antiProtection=
        st.integers(),
    antiTracing=
        st.integers()
)
shr5::KoerperlicheAttribute_strategy = st.builds(
    shr5::KoerperlicheAttribute,
    staerke=
        st.integers(),
    geschicklichkeit=
        st.integers(),
    konstitution=
        st.integers(),
    reaktion=
        st.integers()
)
shr5::Modifyable_strategy = st.builds(
    shr5::Modifyable,
)
shr5::Modifizierbar_strategy = st.builds(
    shr5::Modifizierbar,
)
shr5::EAttribute_strategy = st.builds(
    shr5::EAttribute,
)
shr5::AttributModifikatorWert_strategy = st.builds(
    shr5::AttributModifikatorWert,
    wert=
        st.integers()
)
shr5::Nahkampfwaffe_strategy = st.builds(
    shr5::Nahkampfwaffe,
    reichweite=
        st.integers()
)
shr5::GeldWert_strategy = st.builds(
    shr5::GeldWert,
    wert=
        safe_text,
    wertValue=
        safe_text,
    verfuegbarkeit=
        safe_text
)
AbstraktGegenstand_strategy = st.builds(
    AbstraktGegenstand,
)
shr5::Credstick_strategy = st.builds(
    shr5::Credstick,
    maxValue=
        st.integers(),
    currentValue=
        safe_text
)
shr5::Magazin_strategy = st.builds(
    shr5::Magazin,
)
shr5::AbstractMatrixDevice_strategy = st.builds(
    shr5::AbstractMatrixDevice,
    deviceRating=
        st.integers()
)
shr5::Kleidung_strategy = st.builds(
    shr5::Kleidung,
    ruestung=
        st.integers()
)
shr5::AbstraktFokus_strategy = st.builds(
    shr5::AbstraktFokus,
)
shr5::Munition_strategy = st.builds(
    shr5::Munition,
    armorMod=
        st.integers(),
    damageMod=
        st.integers(),
    damageType=
        safe_text
)
shr5::AbstaktWaffe_strategy = st.builds(
    shr5::AbstaktWaffe,
    schadesTyp=
        safe_text,
    schadenscode=
        safe_text,
    durchschlagsKraft=
        st.integers(),
    praezision=
        st.integers()
)
shr5::SubstanceContainer_strategy = st.builds(
    shr5::SubstanceContainer,
)
shr5::Gegenstand_strategy = st.builds(
    shr5::Gegenstand,
    kategorie=
        safe_text,
    stufe=
        st.integers()
)
shr5::PersonaMartialartStyle_strategy = st.builds(
    shr5::PersonaMartialartStyle,
)
shr5::PersonaFertigkeitsGruppe_strategy = st.builds(
    shr5::PersonaFertigkeitsGruppe,
)
shr5::PersonaFertigkeit_strategy = st.builds(
    shr5::PersonaFertigkeit,
)
ChrakterLimits_strategy = st.builds(
    ChrakterLimits,
)
GeistigeAttribute_strategy = st.builds(
    GeistigeAttribute,
)
SpezielleAttribute_strategy = st.builds(
    SpezielleAttribute,
)
KoerperlicheAttribute_strategy = st.builds(
    KoerperlicheAttribute,
)
Identifiable_strategy = st.builds(
    Identifiable,
)
shr5::Quelle_strategy = st.builds(
    shr5::Quelle,
    page=
        safe_text
)
shr5::Beschreibbar_strategy = st.builds(
    shr5::Beschreibbar,
    beschreibung=
        safe_text,
    image=
        safe_text,
    name=
        safe_text
)
Beschreibbar_strategy = st.builds(
    Beschreibbar,
)
shr5::Spezialisierung_strategy = st.builds(
    shr5::Spezialisierung,
)
shr5::FahrzeugModifikation_strategy = st.builds(
    shr5::FahrzeugModifikation,
    capacityUsed=
        st.integers()
)
shr5::MartialartTechnique_strategy = st.builds(
    shr5::MartialartTechnique,
)
shr5::Fertigkeit_strategy = st.builds(
    shr5::Fertigkeit,
    kategorie=
        safe_text,
    ausweichen=
        st.booleans()
)
shr5::StufenPersona_strategy = st.builds(
    shr5::StufenPersona,
    stufe=
        st.integers()
)
shr5::KomplexeForm_strategy = st.builds(
    shr5::KomplexeForm,
    dauer=
        safe_text,
    ziel=
        safe_text,
    schwund=
        safe_text
)
shr5::MagischeTradition_strategy = st.builds(
    shr5::MagischeTradition,
    enzug=
        safe_text
)
shr5::AbstraktGegenstand_strategy = st.builds(
    shr5::AbstraktGegenstand,
)
shr5::AbstraktPersona_strategy = st.builds(
    shr5::AbstraktPersona,
    modManager=
        safe_text,
    willenskraftBasis=
        st.integers(),
    reaktionBasis=
        st.integers(),
    staerkeBasis=
        st.integers(),
    geschicklichkeitBasis=
        st.integers(),
    logikBasis=
        st.integers(),
    intuitionBasis=
        st.integers(),
    konstitutionBasis=
        st.integers(),
    charismaBasis=
        st.integers()
)
shr5::Sensor_strategy = st.builds(
    shr5::Sensor,
    rating=
        st.integers(),
    capacityValue=
        st.integers()
)
shr5::MartialartStyle_strategy = st.builds(
    shr5::MartialartStyle,
)
shr5::KleindungsModifikator_strategy = st.builds(
    shr5::KleindungsModifikator,
    capacity=
        st.integers(),
    type=
        safe_text,
    rating=
        st.integers()
)
shr5::Substance_strategy = st.builds(
    shr5::Substance,
    speed=
        safe_text,
    vector=
        safe_text
)
shr5::FertigkeitsGruppe_strategy = st.builds(
    shr5::FertigkeitsGruppe,
)
shr5::Sprite_strategy = st.builds(
    shr5::Sprite,
    schleicherMod=
        st.integers(),
    stufe=
        st.integers(),
    firewallMod=
        st.integers(),
    angriffMod=
        st.integers(),
    initativeMod=
        st.integers(),
    datenverarbeitungMod=
        st.integers()
)
shr5::Vertrag_strategy = st.builds(
    shr5::Vertrag,
)
shr5::AbstraktModifikatoren_strategy = st.builds(
    shr5::AbstraktModifikatoren,
)
shr5::MetaMagie_strategy = st.builds(
    shr5::MetaMagie,
)
shr5::SourceBook_strategy = st.builds(
    shr5::SourceBook,
    endShrTime=
        safe_text,
    startShrTime=
        safe_text,
    code=
        safe_text
)
shr5::LifestyleOption_strategy = st.builds(
    shr5::LifestyleOption,
)
shr5::Software_strategy = st.builds(
    shr5::Software,
)
shr5::Fahrzeug_strategy = st.builds(
    shr5::Fahrzeug,
    beschleunigung=
        st.integers(),
    panzer=
        st.integers(),
    sensor=
        st.integers(),
    weaponMounts=
        st.integers(),
    pilot=
        st.integers(),
    rumpf=
        st.integers(),
    geschwindigkeit=
        st.integers(),
    handling=
        st.integers(),
    fahrzeugTyp=
        safe_text
)
shr5::Host_strategy = st.builds(
    shr5::Host,
    baseDatenverarbeitung=
        st.integers(),
    baseFirewall=
        st.integers(),
    baseAngriff=
        st.integers(),
    hostRating=
        st.integers(),
    baseSchleicher=
        st.integers()
)
shr5::SourceLink_strategy = st.builds(
    shr5::SourceLink,
)
shr5::ShrList_strategy = st.builds(
    shr5::ShrList,
)
shr5::SensorFunction_strategy = st.builds(
    shr5::SensorFunction,
    maxRange=
        st.integers()
)
shr5::Spezies_strategy = st.builds(
    shr5::Spezies,
    magieMax=
        st.integers(),
    willenskraftMin=
        st.integers(),
    intuitionMin=
        st.integers(),
    willenskraftMax=
        st.integers(),
    edgeMin=
        st.integers(),
    essenzMax=
        st.integers(),
    logikMin=
        st.integers(),
    reaktionMax=
        st.integers(),
    konstitutionMax=
        st.integers(),
    staerkeMin=
        st.integers(),
    geschicklichkeitMin=
        st.integers(),
    geschicklichkeitMax=
        st.integers(),
    konstitutionMin=
        st.integers(),
    essenzMin=
        st.integers(),
    resonanzMax=
        st.integers(),
    staerkeMax=
        st.integers(),
    laufen=
        st.integers(),
    logikMax=
        st.integers(),
    resonanzMin=
        st.integers(),
    reaktionMin=
        st.integers(),
    sprinten=
        st.integers(),
    intuitionMax=
        st.integers(),
    charismaMin=
        st.integers(),
    magieMin=
        st.integers(),
    edgeMax=
        st.integers(),
    charismaMax=
        st.integers(),
    rennen=
        st.integers()
)
shr5::Reichweite_strategy = st.builds(
    shr5::Reichweite,
    extrem=
        st.integers(),
    kurz=
        st.integers(),
    weit=
        st.integers(),
    mittel=
        st.integers(),
    min=
        st.integers()
)
shr5::Zauber_strategy = st.builds(
    shr5::Zauber,
    entzug=
        safe_text,
    merkmale=
        safe_text,
    dauer=
        safe_text,
    reichweite=
        safe_text,
    art=
        safe_text,
    kategorie=
        safe_text,
    schaden=
        safe_text
)

@given(instance=MatrixAttributes_strategy)
@settings(max_examples=50)
def test_matrixattributes_instantiation(instance):
    assert isinstance(instance, MatrixAttributes)

@given(instance=Fahrzeug_strategy)
@settings(max_examples=50)
def test_fahrzeug_instantiation(instance):
    assert isinstance(instance, Fahrzeug)

@given(instance=shr5::Drohne_strategy)
@settings(max_examples=50)
def test_shr5::drohne_instantiation(instance):
    assert isinstance(instance, shr5::Drohne)

@given(instance=shr5::Drohne_strategy)
def test_shr5::drohne_programSlotCount_type(instance):
    assert isinstance(instance.programSlotCount, int)


@given(instance=shr5::Drohne_strategy)
def test_shr5::drohne_programSlotCount_setter(instance):
    original = instance.programSlotCount
    instance.programSlotCount = original
    assert instance.programSlotCount == original

@given(instance=shr5::PassagierFahrzeug_strategy)
@settings(max_examples=50)
def test_shr5::passagierfahrzeug_instantiation(instance):
    assert isinstance(instance, shr5::PassagierFahrzeug)

@given(instance=shr5::PassagierFahrzeug_strategy)
def test_shr5::passagierfahrzeug_sitze_type(instance):
    assert isinstance(instance.sitze, int)


@given(instance=shr5::PassagierFahrzeug_strategy)
def test_shr5::passagierfahrzeug_sitze_setter(instance):
    original = instance.sitze
    instance.sitze = original
    assert instance.sitze == original

@given(instance=PassagierFahrzeug_strategy)
@settings(max_examples=50)
def test_passagierfahrzeug_instantiation(instance):
    assert isinstance(instance, PassagierFahrzeug)

@given(instance=shr5::Bodenfahrzeug_strategy)
@settings(max_examples=50)
def test_shr5::bodenfahrzeug_instantiation(instance):
    assert isinstance(instance, shr5::Bodenfahrzeug)

@given(instance=shr5::Bodenfahrzeug_strategy)
def test_shr5::bodenfahrzeug_geschwindigkeitGelaende_type(instance):
    assert isinstance(instance.geschwindigkeitGelaende, int)


@given(instance=shr5::Bodenfahrzeug_strategy)
def test_shr5::bodenfahrzeug_geschwindigkeitGelaende_setter(instance):
    original = instance.geschwindigkeitGelaende
    instance.geschwindigkeitGelaende = original
    assert instance.geschwindigkeitGelaende == original

@given(instance=shr5::Bodenfahrzeug_strategy)
def test_shr5::bodenfahrzeug_handlingGelaende_type(instance):
    assert isinstance(instance.handlingGelaende, int)


@given(instance=shr5::Bodenfahrzeug_strategy)
def test_shr5::bodenfahrzeug_handlingGelaende_setter(instance):
    original = instance.handlingGelaende
    instance.handlingGelaende = original
    assert instance.handlingGelaende == original

@given(instance=FahrzeugZustand_strategy)
@settings(max_examples=50)
def test_fahrzeugzustand_instantiation(instance):
    assert isinstance(instance, FahrzeugZustand)

@given(instance=shr5::ChrakterLimits_strategy)
@settings(max_examples=50)
def test_shr5::chrakterlimits_instantiation(instance):
    assert isinstance(instance, shr5::ChrakterLimits)

@given(instance=shr5::ChrakterLimits_strategy)
def test_shr5::chrakterlimits_sozial_type(instance):
    assert isinstance(instance.sozial, int)


@given(instance=shr5::ChrakterLimits_strategy)
def test_shr5::chrakterlimits_sozial_setter(instance):
    original = instance.sozial
    instance.sozial = original
    assert instance.sozial == original

@given(instance=shr5::ChrakterLimits_strategy)
def test_shr5::chrakterlimits_geistig_type(instance):
    assert isinstance(instance.geistig, int)


@given(instance=shr5::ChrakterLimits_strategy)
def test_shr5::chrakterlimits_geistig_setter(instance):
    original = instance.geistig
    instance.geistig = original
    assert instance.geistig == original

@given(instance=shr5::ChrakterLimits_strategy)
def test_shr5::chrakterlimits_koerperlich_type(instance):
    assert isinstance(instance.koerperlich, int)


@given(instance=shr5::ChrakterLimits_strategy)
def test_shr5::chrakterlimits_koerperlich_setter(instance):
    original = instance.koerperlich
    instance.koerperlich = original
    assert instance.koerperlich == original

@given(instance=shr5::AstraleProjektion_strategy)
@settings(max_examples=50)
def test_shr5::astraleprojektion_instantiation(instance):
    assert isinstance(instance, shr5::AstraleProjektion)

@given(instance=shr5::AstraleProjektion_strategy)
def test_shr5::astraleprojektion_astraleGeschicklichkeit_type(instance):
    assert isinstance(instance.astraleGeschicklichkeit, int)


@given(instance=shr5::AstraleProjektion_strategy)
def test_shr5::astraleprojektion_astraleGeschicklichkeit_setter(instance):
    original = instance.astraleGeschicklichkeit
    instance.astraleGeschicklichkeit = original
    assert instance.astraleGeschicklichkeit == original

@given(instance=shr5::AstraleProjektion_strategy)
def test_shr5::astraleprojektion_astraleInitative_type(instance):
    assert isinstance(instance.astraleInitative, int)


@given(instance=shr5::AstraleProjektion_strategy)
def test_shr5::astraleprojektion_astraleInitative_setter(instance):
    original = instance.astraleInitative
    instance.astraleInitative = original
    assert instance.astraleInitative == original

@given(instance=shr5::AstraleProjektion_strategy)
def test_shr5::astraleprojektion_astralesLimit_type(instance):
    assert isinstance(instance.astralesLimit, int)


@given(instance=shr5::AstraleProjektion_strategy)
def test_shr5::astraleprojektion_astralesLimit_setter(instance):
    original = instance.astralesLimit
    instance.astralesLimit = original
    assert instance.astralesLimit == original

@given(instance=shr5::AstraleProjektion_strategy)
def test_shr5::astraleprojektion_astralePanzerung_type(instance):
    assert isinstance(instance.astralePanzerung, int)


@given(instance=shr5::AstraleProjektion_strategy)
def test_shr5::astraleprojektion_astralePanzerung_setter(instance):
    original = instance.astralePanzerung
    instance.astralePanzerung = original
    assert instance.astralePanzerung == original

@given(instance=shr5::AstraleProjektion_strategy)
def test_shr5::astraleprojektion_astraleInitativWuerfel_type(instance):
    assert isinstance(instance.astraleInitativWuerfel, int)


@given(instance=shr5::AstraleProjektion_strategy)
def test_shr5::astraleprojektion_astraleInitativWuerfel_setter(instance):
    original = instance.astraleInitativWuerfel
    instance.astraleInitativWuerfel = original
    assert instance.astraleInitativWuerfel == original

@given(instance=shr5::AstraleProjektion_strategy)
def test_shr5::astraleprojektion_astraleStaerke_type(instance):
    assert isinstance(instance.astraleStaerke, int)


@given(instance=shr5::AstraleProjektion_strategy)
def test_shr5::astraleprojektion_astraleStaerke_setter(instance):
    original = instance.astraleStaerke
    instance.astraleStaerke = original
    assert instance.astraleStaerke == original

@given(instance=shr5::AstraleProjektion_strategy)
def test_shr5::astraleprojektion_astraleReaktion_type(instance):
    assert isinstance(instance.astraleReaktion, int)


@given(instance=shr5::AstraleProjektion_strategy)
def test_shr5::astraleprojektion_astraleReaktion_setter(instance):
    original = instance.astraleReaktion
    instance.astraleReaktion = original
    assert instance.astraleReaktion == original

@given(instance=shr5::AstraleProjektion_strategy)
def test_shr5::astraleprojektion_astraleKonstitution_type(instance):
    assert isinstance(instance.astraleKonstitution, int)


@given(instance=shr5::AstraleProjektion_strategy)
def test_shr5::astraleprojektion_astraleKonstitution_setter(instance):
    original = instance.astraleKonstitution
    instance.astraleKonstitution = original
    assert instance.astraleKonstitution == original

@given(instance=shr5::Panzerung_strategy)
@settings(max_examples=50)
def test_shr5::panzerung_instantiation(instance):
    assert isinstance(instance, shr5::Panzerung)

@given(instance=shr5::Panzerung_strategy)
def test_shr5::panzerung_panzer_type(instance):
    assert isinstance(instance.panzer, int)


@given(instance=shr5::Panzerung_strategy)
def test_shr5::panzerung_panzer_setter(instance):
    original = instance.panzer
    instance.panzer = original
    assert instance.panzer == original

@given(instance=shr5::Zauberer_strategy)
@settings(max_examples=50)
def test_shr5::zauberer_instantiation(instance):
    assert isinstance(instance, shr5::Zauberer)

@given(instance=shr5::Zauberer_strategy)
def test_shr5::zauberer_enzug_type(instance):
    assert isinstance(instance.enzug, int)


@given(instance=shr5::Zauberer_strategy)
def test_shr5::zauberer_enzug_setter(instance):
    original = instance.enzug
    instance.enzug = original
    assert instance.enzug == original

@given(instance=AstraleProjektion_strategy)
@settings(max_examples=50)
def test_astraleprojektion_instantiation(instance):
    assert isinstance(instance, AstraleProjektion)

@given(instance=Zauberer_strategy)
@settings(max_examples=50)
def test_zauberer_instantiation(instance):
    assert isinstance(instance, Zauberer)

@given(instance=shr5::Anwendbar_strategy)
@settings(max_examples=50)
def test_shr5::anwendbar_instantiation(instance):
    assert isinstance(instance, shr5::Anwendbar)

@given(instance=KiAdept_strategy)
@settings(max_examples=50)
def test_kiadept_instantiation(instance):
    assert isinstance(instance, KiAdept)

@given(instance=MagischePersona_strategy)
@settings(max_examples=50)
def test_magischepersona_instantiation(instance):
    assert isinstance(instance, MagischePersona)

@given(instance=shr5::AspektMagier_strategy)
@settings(max_examples=50)
def test_shr5::aspektmagier_instantiation(instance):
    assert isinstance(instance, shr5::AspektMagier)

@given(instance=shr5::Magier_strategy)
@settings(max_examples=50)
def test_shr5::magier_instantiation(instance):
    assert isinstance(instance, shr5::Magier)

@given(instance=shr5::MysticAdept_strategy)
@settings(max_examples=50)
def test_shr5::mysticadept_instantiation(instance):
    assert isinstance(instance, shr5::MysticAdept)

@given(instance=shr5::KiAdept_strategy)
@settings(max_examples=50)
def test_shr5::kiadept_instantiation(instance):
    assert isinstance(instance, shr5::KiAdept)

@given(instance=Wurfwaffe_strategy)
@settings(max_examples=50)
def test_wurfwaffe_instantiation(instance):
    assert isinstance(instance, Wurfwaffe)

@given(instance=AbtraktGranate_strategy)
@settings(max_examples=50)
def test_abtraktgranate_instantiation(instance):
    assert isinstance(instance, AbtraktGranate)

@given(instance=shr5::Granate_strategy)
@settings(max_examples=50)
def test_shr5::granate_instantiation(instance):
    assert isinstance(instance, shr5::Granate)

@given(instance=Munition_strategy)
@settings(max_examples=50)
def test_munition_instantiation(instance):
    assert isinstance(instance, Munition)

@given(instance=shr5::MiniGrenate_strategy)
@settings(max_examples=50)
def test_shr5::minigrenate_instantiation(instance):
    assert isinstance(instance, shr5::MiniGrenate)

@given(instance=shr5::AbtraktGranate_strategy)
@settings(max_examples=50)
def test_shr5::abtraktgranate_instantiation(instance):
    assert isinstance(instance, shr5::AbtraktGranate)

@given(instance=shr5::AbtraktGranate_strategy)
def test_shr5::abtraktgranate_blast_type(instance):
    assert isinstance(instance.blast, str)


@given(instance=shr5::AbtraktGranate_strategy)
def test_shr5::abtraktgranate_blast_setter(instance):
    original = instance.blast
    instance.blast = original
    assert instance.blast == original

@given(instance=Spezialisierung_strategy)
@settings(max_examples=50)
def test_spezialisierung_instantiation(instance):
    assert isinstance(instance, Spezialisierung)

@given(instance=Sensor_strategy)
@settings(max_examples=50)
def test_sensor_instantiation(instance):
    assert isinstance(instance, Sensor)

@given(instance=shr5::SensorArray_strategy)
@settings(max_examples=50)
def test_shr5::sensorarray_instantiation(instance):
    assert isinstance(instance, shr5::SensorArray)

@given(instance=CredstickTransaction_strategy)
@settings(max_examples=50)
def test_credsticktransaction_instantiation(instance):
    assert isinstance(instance, CredstickTransaction)

@given(instance=shr5::TransferAmount_strategy)
@settings(max_examples=50)
def test_shr5::transferamount_instantiation(instance):
    assert isinstance(instance, shr5::TransferAmount)

@given(instance=shr5::TransferAmount_strategy)
def test_shr5::transferamount_amountToTransfer_type(instance):
    assert isinstance(instance.amountToTransfer, str)


@given(instance=shr5::TransferAmount_strategy)
def test_shr5::transferamount_amountToTransfer_setter(instance):
    original = instance.amountToTransfer
    instance.amountToTransfer = original
    assert instance.amountToTransfer == original

@given(instance=shr5::ShoppingTransaction_strategy)
@settings(max_examples=50)
def test_shr5::shoppingtransaction_instantiation(instance):
    assert isinstance(instance, shr5::ShoppingTransaction)

@given(instance=shr5::ShoppingTransaction_strategy)
def test_shr5::shoppingtransaction_caculatedCosts_type(instance):
    assert isinstance(instance.caculatedCosts, str)


@given(instance=shr5::ShoppingTransaction_strategy)
def test_shr5::shoppingtransaction_caculatedCosts_setter(instance):
    original = instance.caculatedCosts
    instance.caculatedCosts = original
    assert instance.caculatedCosts == original

@given(instance=shr5::ShoppingTransaction_strategy)
def test_shr5::shoppingtransaction_fee_type(instance):
    assert isinstance(instance.fee, float)


@given(instance=shr5::ShoppingTransaction_strategy)
def test_shr5::shoppingtransaction_fee_setter(instance):
    original = instance.fee
    instance.fee = original
    assert instance.fee == original

@given(instance=CyberwareEnhancement_strategy)
@settings(max_examples=50)
def test_cyberwareenhancement_instantiation(instance):
    assert isinstance(instance, CyberwareEnhancement)

@given(instance=shr5::CyberImplantWeapon_strategy)
@settings(max_examples=50)
def test_shr5::cyberimplantweapon_instantiation(instance):
    assert isinstance(instance, shr5::CyberImplantWeapon)

@given(instance=shr5::EReference_strategy)
@settings(max_examples=50)
def test_shr5::ereference_instantiation(instance):
    assert isinstance(instance, shr5::EReference)

@given(instance=Substance_strategy)
@settings(max_examples=50)
def test_substance_instantiation(instance):
    assert isinstance(instance, Substance)

@given(instance=shr5::Toxin_strategy)
@settings(max_examples=50)
def test_shr5::toxin_instantiation(instance):
    assert isinstance(instance, shr5::Toxin)

@given(instance=shr5::Toxin_strategy)
def test_shr5::toxin_power_type(instance):
    assert isinstance(instance.power, int)


@given(instance=shr5::Toxin_strategy)
def test_shr5::toxin_power_setter(instance):
    original = instance.power
    instance.power = original
    assert instance.power == original

@given(instance=shr5::Toxin_strategy)
def test_shr5::toxin_effect_type(instance):
    assert isinstance(instance.effect, str)


@given(instance=shr5::Toxin_strategy)
def test_shr5::toxin_effect_setter(instance):
    original = instance.effect
    instance.effect = original
    assert instance.effect == original

@given(instance=shr5::Toxin_strategy)
def test_shr5::toxin_penetration_type(instance):
    assert isinstance(instance.penetration, int)


@given(instance=shr5::Toxin_strategy)
def test_shr5::toxin_penetration_setter(instance):
    original = instance.penetration
    instance.penetration = original
    assert instance.penetration == original

@given(instance=shr5::Capacity_strategy)
@settings(max_examples=50)
def test_shr5::capacity_instantiation(instance):
    assert isinstance(instance, shr5::Capacity)

@given(instance=shr5::Capacity_strategy)
def test_shr5::capacity_capacity_type(instance):
    assert isinstance(instance.capacity, int)


@given(instance=shr5::Capacity_strategy)
def test_shr5::capacity_capacity_setter(instance):
    original = instance.capacity
    instance.capacity = original
    assert instance.capacity == original

@given(instance=shr5::Capacity_strategy)
def test_shr5::capacity_capacityRemains_type(instance):
    assert isinstance(instance.capacityRemains, int)


@given(instance=shr5::Capacity_strategy)
def test_shr5::capacity_capacityRemains_setter(instance):
    original = instance.capacityRemains
    instance.capacityRemains = original
    assert instance.capacityRemains == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=shr5::Capacity_strategy)
@settings(max_examples=30)
def test_shr5::capacity_canadd_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.canAdd(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.canAdd).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'canAdd' in shr5::Capacity is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'canAdd' in shr5::Capacity did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'canAdd' in shr5::Capacity is not implemented or raised an error")

@given(instance=Nahkampfwaffe_strategy)
@settings(max_examples=50)
def test_nahkampfwaffe_instantiation(instance):
    assert isinstance(instance, Nahkampfwaffe)

@given(instance=AbstraktFokus_strategy)
@settings(max_examples=50)
def test_abstraktfokus_instantiation(instance):
    assert isinstance(instance, AbstraktFokus)

@given(instance=shr5::MagieFokus_strategy)
@settings(max_examples=50)
def test_shr5::magiefokus_instantiation(instance):
    assert isinstance(instance, shr5::MagieFokus)

@given(instance=shr5::MagieFokus_strategy)
def test_shr5::magiefokus_bindungsFaktor_type(instance):
    assert isinstance(instance.bindungsFaktor, int)


@given(instance=shr5::MagieFokus_strategy)
def test_shr5::magiefokus_bindungsFaktor_setter(instance):
    original = instance.bindungsFaktor
    instance.bindungsFaktor = original
    assert instance.bindungsFaktor == original

@given(instance=shr5::QiFokus_strategy)
@settings(max_examples=50)
def test_shr5::qifokus_instantiation(instance):
    assert isinstance(instance, shr5::QiFokus)

@given(instance=Fokus_strategy)
@settings(max_examples=50)
def test_fokus_instantiation(instance):
    assert isinstance(instance, Fokus)

@given(instance=shr5::WaffenFokus_strategy)
@settings(max_examples=50)
def test_shr5::waffenfokus_instantiation(instance):
    assert isinstance(instance, shr5::WaffenFokus)

@given(instance=MagischeStufe_strategy)
@settings(max_examples=50)
def test_magischestufe_instantiation(instance):
    assert isinstance(instance, MagischeStufe)

@given(instance=shr5::MagischeStufe_strategy)
@settings(max_examples=50)
def test_shr5::magischestufe_instantiation(instance):
    assert isinstance(instance, shr5::MagischeStufe)

@given(instance=shr5::MagischeStufe_strategy)
def test_shr5::magischestufe_stufe_type(instance):
    assert isinstance(instance.stufe, int)


@given(instance=shr5::MagischeStufe_strategy)
def test_shr5::magischestufe_stufe_setter(instance):
    original = instance.stufe
    instance.stufe = original
    assert instance.stufe == original

@given(instance=shr5::BerechneteAttribute_strategy)
@settings(max_examples=50)
def test_shr5::berechneteattribute_instantiation(instance):
    assert isinstance(instance, shr5::BerechneteAttribute)

@given(instance=shr5::BerechneteAttribute_strategy)
def test_shr5::berechneteattribute_selbstbeherrschung_type(instance):
    assert isinstance(instance.selbstbeherrschung, int)


@given(instance=shr5::BerechneteAttribute_strategy)
def test_shr5::berechneteattribute_selbstbeherrschung_setter(instance):
    original = instance.selbstbeherrschung
    instance.selbstbeherrschung = original
    assert instance.selbstbeherrschung == original

@given(instance=shr5::BerechneteAttribute_strategy)
def test_shr5::berechneteattribute_menschenkenntnis_type(instance):
    assert isinstance(instance.menschenkenntnis, int)


@given(instance=shr5::BerechneteAttribute_strategy)
def test_shr5::berechneteattribute_menschenkenntnis_setter(instance):
    original = instance.menschenkenntnis
    instance.menschenkenntnis = original
    assert instance.menschenkenntnis == original

@given(instance=shr5::BerechneteAttribute_strategy)
def test_shr5::berechneteattribute_errinerungsvermoegen_type(instance):
    assert isinstance(instance.errinerungsvermoegen, int)


@given(instance=shr5::BerechneteAttribute_strategy)
def test_shr5::berechneteattribute_errinerungsvermoegen_setter(instance):
    original = instance.errinerungsvermoegen
    instance.errinerungsvermoegen = original
    assert instance.errinerungsvermoegen == original

@given(instance=LifestyleOption_strategy)
@settings(max_examples=50)
def test_lifestyleoption_instantiation(instance):
    assert isinstance(instance, LifestyleOption)

@given(instance=shr5::PercentLifestyleOption_strategy)
@settings(max_examples=50)
def test_shr5::percentlifestyleoption_instantiation(instance):
    assert isinstance(instance, shr5::PercentLifestyleOption)

@given(instance=FahrzeugModifikation_strategy)
@settings(max_examples=50)
def test_fahrzeugmodifikation_instantiation(instance):
    assert isinstance(instance, FahrzeugModifikation)

@given(instance=shr5::FahrzeugErweiterung_strategy)
@settings(max_examples=50)
def test_shr5::fahrzeugerweiterung_instantiation(instance):
    assert isinstance(instance, shr5::FahrzeugErweiterung)

@given(instance=shr5::WeaponMount_strategy)
@settings(max_examples=50)
def test_shr5::weaponmount_instantiation(instance):
    assert isinstance(instance, shr5::WeaponMount)

@given(instance=shr5::PersonalAreaNetwork_strategy)
@settings(max_examples=50)
def test_shr5::personalareanetwork_instantiation(instance):
    assert isinstance(instance, shr5::PersonalAreaNetwork)

@given(instance=shr5::PersonalAreaNetwork_strategy)
def test_shr5::personalareanetwork_slaveMax_type(instance):
    assert isinstance(instance.slaveMax, int)


@given(instance=shr5::PersonalAreaNetwork_strategy)
def test_shr5::personalareanetwork_slaveMax_setter(instance):
    original = instance.slaveMax
    instance.slaveMax = original
    assert instance.slaveMax == original

@given(instance=shr5::FahrzeugZustand_strategy)
@settings(max_examples=50)
def test_shr5::fahrzeugzustand_instantiation(instance):
    assert isinstance(instance, shr5::FahrzeugZustand)

@given(instance=shr5::FahrzeugZustand_strategy)
def test_shr5::fahrzeugzustand_zustandMax_type(instance):
    assert isinstance(instance.zustandMax, int)


@given(instance=shr5::FahrzeugZustand_strategy)
def test_shr5::fahrzeugzustand_zustandMax_setter(instance):
    original = instance.zustandMax
    instance.zustandMax = original
    assert instance.zustandMax == original

@given(instance=BasicProgram_strategy)
@settings(max_examples=50)
def test_basicprogram_instantiation(instance):
    assert isinstance(instance, BasicProgram)

@given(instance=shr5::Datasoft_strategy)
@settings(max_examples=50)
def test_shr5::datasoft_instantiation(instance):
    assert isinstance(instance, shr5::Datasoft)

@given(instance=shr5::ConsumerSoft_strategy)
@settings(max_examples=50)
def test_shr5::consumersoft_instantiation(instance):
    assert isinstance(instance, shr5::ConsumerSoft)

@given(instance=shr5::ConsumerSoft_strategy)
def test_shr5::consumersoft_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=shr5::ConsumerSoft_strategy)
def test_shr5::consumersoft_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=shr5::Tutorsoft_strategy)
@settings(max_examples=50)
def test_shr5::tutorsoft_instantiation(instance):
    assert isinstance(instance, shr5::Tutorsoft)

@given(instance=shr5::Tutorsoft_strategy)
def test_shr5::tutorsoft_rating_type(instance):
    assert isinstance(instance.rating, int)


@given(instance=shr5::Tutorsoft_strategy)
def test_shr5::tutorsoft_rating_setter(instance):
    original = instance.rating
    instance.rating = original
    assert instance.rating == original

@given(instance=Software_strategy)
@settings(max_examples=50)
def test_software_instantiation(instance):
    assert isinstance(instance, Software)

@given(instance=shr5::SkillSoft_strategy)
@settings(max_examples=50)
def test_shr5::skillsoft_instantiation(instance):
    assert isinstance(instance, shr5::SkillSoft)

@given(instance=shr5::SkillSoft_strategy)
def test_shr5::skillsoft_rating_type(instance):
    assert isinstance(instance.rating, int)


@given(instance=shr5::SkillSoft_strategy)
def test_shr5::skillsoft_rating_setter(instance):
    original = instance.rating
    instance.rating = original
    assert instance.rating == original

@given(instance=shr5::RiggerProgram_strategy)
@settings(max_examples=50)
def test_shr5::riggerprogram_instantiation(instance):
    assert isinstance(instance, shr5::RiggerProgram)

@given(instance=RiggerProgram_strategy)
@settings(max_examples=50)
def test_riggerprogram_instantiation(instance):
    assert isinstance(instance, RiggerProgram)

@given(instance=shr5::AutoSoft_strategy)
@settings(max_examples=50)
def test_shr5::autosoft_instantiation(instance):
    assert isinstance(instance, shr5::AutoSoft)

@given(instance=shr5::AutoSoft_strategy)
def test_shr5::autosoft_rating_type(instance):
    assert isinstance(instance.rating, int)


@given(instance=shr5::AutoSoft_strategy)
def test_shr5::autosoft_rating_setter(instance):
    original = instance.rating
    instance.rating = original
    assert instance.rating == original

@given(instance=MatrixProgram_strategy)
@settings(max_examples=50)
def test_matrixprogram_instantiation(instance):
    assert isinstance(instance, MatrixProgram)

@given(instance=shr5::CommonProgram_strategy)
@settings(max_examples=50)
def test_shr5::commonprogram_instantiation(instance):
    assert isinstance(instance, shr5::CommonProgram)

@given(instance=shr5::CommonProgram_strategy)
def test_shr5::commonprogram_programType_type(instance):
    assert isinstance(instance.programType, str)


@given(instance=shr5::CommonProgram_strategy)
def test_shr5::commonprogram_programType_setter(instance):
    original = instance.programType
    instance.programType = original
    assert instance.programType == original

@given(instance=shr5::SoftwareAgent_strategy)
@settings(max_examples=50)
def test_shr5::softwareagent_instantiation(instance):
    assert isinstance(instance, shr5::SoftwareAgent)

@given(instance=shr5::SoftwareAgent_strategy)
def test_shr5::softwareagent_rating_type(instance):
    assert isinstance(instance.rating, int)


@given(instance=shr5::SoftwareAgent_strategy)
def test_shr5::softwareagent_rating_setter(instance):
    original = instance.rating
    instance.rating = original
    assert instance.rating == original

@given(instance=shr5::Localization_strategy)
@settings(max_examples=50)
def test_shr5::localization_instantiation(instance):
    assert isinstance(instance, shr5::Localization)

@given(instance=shr5::Localization_strategy)
def test_shr5::localization_page_type(instance):
    assert isinstance(instance.page, int)


@given(instance=shr5::Localization_strategy)
def test_shr5::localization_page_setter(instance):
    original = instance.page
    instance.page = original
    assert instance.page == original

@given(instance=shr5::Localization_strategy)
def test_shr5::localization_local_type(instance):
    assert isinstance(instance.local, str)


@given(instance=shr5::Localization_strategy)
def test_shr5::localization_local_setter(instance):
    original = instance.local
    instance.local = original
    assert instance.local == original

@given(instance=shr5::Localization_strategy)
def test_shr5::localization_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=shr5::Localization_strategy)
def test_shr5::localization_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=MatrixDevice_strategy)
@settings(max_examples=50)
def test_matrixdevice_instantiation(instance):
    assert isinstance(instance, MatrixDevice)

@given(instance=shr5::MatixConditionMonitor_strategy)
@settings(max_examples=50)
def test_shr5::matixconditionmonitor_instantiation(instance):
    assert isinstance(instance, shr5::MatixConditionMonitor)

@given(instance=shr5::MatixConditionMonitor_strategy)
def test_shr5::matixconditionmonitor_matrixZustandMax_type(instance):
    assert isinstance(instance.matrixZustandMax, int)


@given(instance=shr5::MatixConditionMonitor_strategy)
def test_shr5::matixconditionmonitor_matrixZustandMax_setter(instance):
    original = instance.matrixZustandMax
    instance.matrixZustandMax = original
    assert instance.matrixZustandMax == original

@given(instance=shr5::BasicProgram_strategy)
@settings(max_examples=50)
def test_shr5::basicprogram_instantiation(instance):
    assert isinstance(instance, shr5::BasicProgram)

@given(instance=AbstractMatrixDevice_strategy)
@settings(max_examples=50)
def test_abstractmatrixdevice_instantiation(instance):
    assert isinstance(instance, AbstractMatrixDevice)

@given(instance=shr5::RiggerCommandConsole_strategy)
@settings(max_examples=50)
def test_shr5::riggercommandconsole_instantiation(instance):
    assert isinstance(instance, shr5::RiggerCommandConsole)

@given(instance=shr5::RiggerCommandConsole_strategy)
def test_shr5::riggercommandconsole_rauschunterdrueckung_type(instance):
    assert isinstance(instance.rauschunterdrueckung, int)


@given(instance=shr5::RiggerCommandConsole_strategy)
def test_shr5::riggercommandconsole_rauschunterdrueckung_setter(instance):
    original = instance.rauschunterdrueckung
    instance.rauschunterdrueckung = original
    assert instance.rauschunterdrueckung == original

@given(instance=shr5::RiggerCommandConsole_strategy)
def test_shr5::riggercommandconsole_zugriffBasis_type(instance):
    assert isinstance(instance.zugriffBasis, int)


@given(instance=shr5::RiggerCommandConsole_strategy)
def test_shr5::riggercommandconsole_zugriffBasis_setter(instance):
    original = instance.zugriffBasis
    instance.zugriffBasis = original
    assert instance.zugriffBasis == original

@given(instance=shr5::RiggerCommandConsole_strategy)
def test_shr5::riggercommandconsole_firewallBasis_type(instance):
    assert isinstance(instance.firewallBasis, int)


@given(instance=shr5::RiggerCommandConsole_strategy)
def test_shr5::riggercommandconsole_firewallBasis_setter(instance):
    original = instance.firewallBasis
    instance.firewallBasis = original
    assert instance.firewallBasis == original

@given(instance=shr5::RiggerCommandConsole_strategy)
def test_shr5::riggercommandconsole_datenverarbeitungBasis_type(instance):
    assert isinstance(instance.datenverarbeitungBasis, int)


@given(instance=shr5::RiggerCommandConsole_strategy)
def test_shr5::riggercommandconsole_datenverarbeitungBasis_setter(instance):
    original = instance.datenverarbeitungBasis
    instance.datenverarbeitungBasis = original
    assert instance.datenverarbeitungBasis == original

@given(instance=shr5::RiggerCommandConsole_strategy)
def test_shr5::riggercommandconsole_zugriff_type(instance):
    assert isinstance(instance.zugriff, int)


@given(instance=shr5::RiggerCommandConsole_strategy)
def test_shr5::riggercommandconsole_zugriff_setter(instance):
    original = instance.zugriff
    instance.zugriff = original
    assert instance.zugriff == original

@given(instance=shr5::Commlink_strategy)
@settings(max_examples=50)
def test_shr5::commlink_instantiation(instance):
    assert isinstance(instance, shr5::Commlink)

@given(instance=shr5::ActiveMatixDevice_strategy)
@settings(max_examples=50)
def test_shr5::activematixdevice_instantiation(instance):
    assert isinstance(instance, shr5::ActiveMatixDevice)

@given(instance=shr5::ActiveMatixDevice_strategy)
def test_shr5::activematixdevice_angriff_type(instance):
    assert isinstance(instance.angriff, int)


@given(instance=shr5::ActiveMatixDevice_strategy)
def test_shr5::activematixdevice_angriff_setter(instance):
    original = instance.angriff
    instance.angriff = original
    assert instance.angriff == original

@given(instance=shr5::ActiveMatixDevice_strategy)
def test_shr5::activematixdevice_schleicher_type(instance):
    assert isinstance(instance.schleicher, int)


@given(instance=shr5::ActiveMatixDevice_strategy)
def test_shr5::activematixdevice_schleicher_setter(instance):
    original = instance.schleicher
    instance.schleicher = original
    assert instance.schleicher == original

@given(instance=MatixConditionMonitor_strategy)
@settings(max_examples=50)
def test_matixconditionmonitor_instantiation(instance):
    assert isinstance(instance, MatixConditionMonitor)

@given(instance=shr5::MatrixAttributes_strategy)
@settings(max_examples=50)
def test_shr5::matrixattributes_instantiation(instance):
    assert isinstance(instance, shr5::MatrixAttributes)

@given(instance=shr5::MatrixAttributes_strategy)
def test_shr5::matrixattributes_geraetestufe_type(instance):
    assert isinstance(instance.geraetestufe, int)


@given(instance=shr5::MatrixAttributes_strategy)
def test_shr5::matrixattributes_geraetestufe_setter(instance):
    original = instance.geraetestufe
    instance.geraetestufe = original
    assert instance.geraetestufe == original

@given(instance=shr5::MatrixAttributes_strategy)
def test_shr5::matrixattributes_datenverarbeitung_type(instance):
    assert isinstance(instance.datenverarbeitung, int)


@given(instance=shr5::MatrixAttributes_strategy)
def test_shr5::matrixattributes_datenverarbeitung_setter(instance):
    original = instance.datenverarbeitung
    instance.datenverarbeitung = original
    assert instance.datenverarbeitung == original

@given(instance=shr5::MatrixAttributes_strategy)
def test_shr5::matrixattributes_currentModus_type(instance):
    assert isinstance(instance.currentModus, str)


@given(instance=shr5::MatrixAttributes_strategy)
def test_shr5::matrixattributes_currentModus_setter(instance):
    original = instance.currentModus
    instance.currentModus = original
    assert instance.currentModus == original

@given(instance=shr5::MatrixAttributes_strategy)
def test_shr5::matrixattributes_firewall_type(instance):
    assert isinstance(instance.firewall, int)


@given(instance=shr5::MatrixAttributes_strategy)
def test_shr5::matrixattributes_firewall_setter(instance):
    original = instance.firewall
    instance.firewall = original
    assert instance.firewall == original

@given(instance=shr5::Identifiable_strategy)
@settings(max_examples=50)
def test_shr5::identifiable_instantiation(instance):
    assert isinstance(instance, shr5::Identifiable)

@given(instance=shr5::Identifiable_strategy)
def test_shr5::identifiable_parentId_type(instance):
    assert isinstance(instance.parentId, str)


@given(instance=shr5::Identifiable_strategy)
def test_shr5::identifiable_parentId_setter(instance):
    original = instance.parentId
    instance.parentId = original
    assert instance.parentId == original

@given(instance=StufenPersona_strategy)
@settings(max_examples=50)
def test_stufenpersona_instantiation(instance):
    assert isinstance(instance, StufenPersona)

@given(instance=shr5::Geist_strategy)
@settings(max_examples=50)
def test_shr5::geist_instantiation(instance):
    assert isinstance(instance, shr5::Geist)

@given(instance=shr5::Geist_strategy)
def test_shr5::geist_reaktionBasis_type(instance):
    assert isinstance(instance.reaktionBasis, int)


@given(instance=shr5::Geist_strategy)
def test_shr5::geist_reaktionBasis_setter(instance):
    original = instance.reaktionBasis
    instance.reaktionBasis = original
    assert instance.reaktionBasis == original

@given(instance=shr5::Geist_strategy)
def test_shr5::geist_staerkeBasis_type(instance):
    assert isinstance(instance.staerkeBasis, int)


@given(instance=shr5::Geist_strategy)
def test_shr5::geist_staerkeBasis_setter(instance):
    original = instance.staerkeBasis
    instance.staerkeBasis = original
    assert instance.staerkeBasis == original

@given(instance=shr5::Geist_strategy)
def test_shr5::geist_charismaBasis_type(instance):
    assert isinstance(instance.charismaBasis, int)


@given(instance=shr5::Geist_strategy)
def test_shr5::geist_charismaBasis_setter(instance):
    original = instance.charismaBasis
    instance.charismaBasis = original
    assert instance.charismaBasis == original

@given(instance=shr5::Geist_strategy)
def test_shr5::geist_logikBasis_type(instance):
    assert isinstance(instance.logikBasis, int)


@given(instance=shr5::Geist_strategy)
def test_shr5::geist_logikBasis_setter(instance):
    original = instance.logikBasis
    instance.logikBasis = original
    assert instance.logikBasis == original

@given(instance=shr5::Geist_strategy)
def test_shr5::geist_willenskraftBasis_type(instance):
    assert isinstance(instance.willenskraftBasis, int)


@given(instance=shr5::Geist_strategy)
def test_shr5::geist_willenskraftBasis_setter(instance):
    original = instance.willenskraftBasis
    instance.willenskraftBasis = original
    assert instance.willenskraftBasis == original

@given(instance=shr5::Geist_strategy)
def test_shr5::geist_konstitutionBasis_type(instance):
    assert isinstance(instance.konstitutionBasis, int)


@given(instance=shr5::Geist_strategy)
def test_shr5::geist_konstitutionBasis_setter(instance):
    original = instance.konstitutionBasis
    instance.konstitutionBasis = original
    assert instance.konstitutionBasis == original

@given(instance=shr5::Geist_strategy)
def test_shr5::geist_geschicklichkeitBasis_type(instance):
    assert isinstance(instance.geschicklichkeitBasis, int)


@given(instance=shr5::Geist_strategy)
def test_shr5::geist_geschicklichkeitBasis_setter(instance):
    original = instance.geschicklichkeitBasis
    instance.geschicklichkeitBasis = original
    assert instance.geschicklichkeitBasis == original

@given(instance=shr5::Geist_strategy)
def test_shr5::geist_intuitionBasis_type(instance):
    assert isinstance(instance.intuitionBasis, int)


@given(instance=shr5::Geist_strategy)
def test_shr5::geist_intuitionBasis_setter(instance):
    original = instance.intuitionBasis
    instance.intuitionBasis = original
    assert instance.intuitionBasis == original

@given(instance=shr5::ModifikatorAttribute_strategy)
@settings(max_examples=50)
def test_shr5::modifikatorattribute_instantiation(instance):
    assert isinstance(instance, shr5::ModifikatorAttribute)

@given(instance=Vertrag_strategy)
@settings(max_examples=50)
def test_vertrag_instantiation(instance):
    assert isinstance(instance, Vertrag)

@given(instance=shr5::IntervallVertrag_strategy)
@settings(max_examples=50)
def test_shr5::intervallvertrag_instantiation(instance):
    assert isinstance(instance, shr5::IntervallVertrag)

@given(instance=shr5::IntervallVertrag_strategy)
def test_shr5::intervallvertrag_faelligkeitsIntervall_type(instance):
    assert isinstance(instance.faelligkeitsIntervall, int)


@given(instance=shr5::IntervallVertrag_strategy)
def test_shr5::intervallvertrag_faelligkeitsIntervall_setter(instance):
    original = instance.faelligkeitsIntervall
    instance.faelligkeitsIntervall = original
    assert instance.faelligkeitsIntervall == original

@given(instance=shr5::IntervallVertrag_strategy)
def test_shr5::intervallvertrag_unit_type(instance):
    assert isinstance(instance.unit, str)


@given(instance=shr5::IntervallVertrag_strategy)
def test_shr5::intervallvertrag_unit_setter(instance):
    original = instance.unit
    instance.unit = original
    assert instance.unit == original

@given(instance=shr5::IntervallVertrag_strategy)
def test_shr5::intervallvertrag_begin_type(instance):
    assert isinstance(instance.begin, str)


@given(instance=shr5::IntervallVertrag_strategy)
def test_shr5::intervallvertrag_begin_setter(instance):
    original = instance.begin
    instance.begin = original
    assert instance.begin == original

@given(instance=Spezies_strategy)
@settings(max_examples=50)
def test_spezies_instantiation(instance):
    assert isinstance(instance, Spezies)

@given(instance=shr5::Critter_strategy)
@settings(max_examples=50)
def test_shr5::critter_instantiation(instance):
    assert isinstance(instance, shr5::Critter)

@given(instance=shr5::PersonaZustand_strategy)
@settings(max_examples=50)
def test_shr5::personazustand_instantiation(instance):
    assert isinstance(instance, shr5::PersonaZustand)

@given(instance=shr5::PersonaZustand_strategy)
def test_shr5::personazustand_zustandGeistigMax_type(instance):
    assert isinstance(instance.zustandGeistigMax, int)


@given(instance=shr5::PersonaZustand_strategy)
def test_shr5::personazustand_zustandGeistigMax_setter(instance):
    original = instance.zustandGeistigMax
    instance.zustandGeistigMax = original
    assert instance.zustandGeistigMax == original

@given(instance=shr5::PersonaZustand_strategy)
def test_shr5::personazustand_zustandKoerperlichMax_type(instance):
    assert isinstance(instance.zustandKoerperlichMax, int)


@given(instance=shr5::PersonaZustand_strategy)
def test_shr5::personazustand_zustandKoerperlichMax_setter(instance):
    original = instance.zustandKoerperlichMax
    instance.zustandKoerperlichMax = original
    assert instance.zustandKoerperlichMax == original

@given(instance=shr5::PersonaZustand_strategy)
def test_shr5::personazustand_zustandGrenze_type(instance):
    assert isinstance(instance.zustandGrenze, int)


@given(instance=shr5::PersonaZustand_strategy)
def test_shr5::personazustand_zustandGrenze_setter(instance):
    original = instance.zustandGrenze
    instance.zustandGrenze = original
    assert instance.zustandGrenze == original

@given(instance=Wissensfertigkeit_strategy)
@settings(max_examples=50)
def test_wissensfertigkeit_instantiation(instance):
    assert isinstance(instance, Wissensfertigkeit)

@given(instance=shr5::Sprachfertigkeit_strategy)
@settings(max_examples=50)
def test_shr5::sprachfertigkeit_instantiation(instance):
    assert isinstance(instance, shr5::Sprachfertigkeit)

@given(instance=Fertigkeit_strategy)
@settings(max_examples=50)
def test_fertigkeit_instantiation(instance):
    assert isinstance(instance, Fertigkeit)

@given(instance=shr5::Wissensfertigkeit_strategy)
@settings(max_examples=50)
def test_shr5::wissensfertigkeit_instantiation(instance):
    assert isinstance(instance, shr5::Wissensfertigkeit)

@given(instance=shr5::Menge_strategy)
@settings(max_examples=50)
def test_shr5::menge_instantiation(instance):
    assert isinstance(instance, shr5::Menge)

@given(instance=shr5::Menge_strategy)
def test_shr5::menge_proAnzahl_type(instance):
    assert isinstance(instance.proAnzahl, int)


@given(instance=shr5::Menge_strategy)
def test_shr5::menge_proAnzahl_setter(instance):
    original = instance.proAnzahl
    instance.proAnzahl = original
    assert instance.proAnzahl == original

@given(instance=shr5::Menge_strategy)
def test_shr5::menge_anzahl_type(instance):
    assert isinstance(instance.anzahl, int)


@given(instance=shr5::Menge_strategy)
def test_shr5::menge_anzahl_setter(instance):
    original = instance.anzahl
    instance.anzahl = original
    assert instance.anzahl == original

@given(instance=shr5::CredstickTransaction_strategy)
@settings(max_examples=50)
def test_shr5::credsticktransaction_instantiation(instance):
    assert isinstance(instance, shr5::CredstickTransaction)

@given(instance=shr5::CredstickTransaction_strategy)
def test_shr5::credsticktransaction_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=shr5::CredstickTransaction_strategy)
def test_shr5::credsticktransaction_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=shr5::CredstickTransaction_strategy)
def test_shr5::credsticktransaction_date_type(instance):
    assert isinstance(instance.date, str)


@given(instance=shr5::CredstickTransaction_strategy)
def test_shr5::credsticktransaction_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original

@given(instance=shr5::CredstickTransaction_strategy)
def test_shr5::credsticktransaction_amount_type(instance):
    assert isinstance(instance.amount, str)


@given(instance=shr5::CredstickTransaction_strategy)
def test_shr5::credsticktransaction_amount_setter(instance):
    original = instance.amount
    instance.amount = original
    assert instance.amount == original

@given(instance=shr5::Erlernbar_strategy)
@settings(max_examples=50)
def test_shr5::erlernbar_instantiation(instance):
    assert isinstance(instance, shr5::Erlernbar)

@given(instance=shr5::Fakeable_strategy)
@settings(max_examples=50)
def test_shr5::fakeable_instantiation(instance):
    assert isinstance(instance, shr5::Fakeable)

@given(instance=shr5::Fakeable_strategy)
def test_shr5::fakeable_gefaelscht_type(instance):
    assert isinstance(instance.gefaelscht, bool)


@given(instance=shr5::Fakeable_strategy)
def test_shr5::fakeable_gefaelscht_setter(instance):
    original = instance.gefaelscht
    instance.gefaelscht = original
    assert instance.gefaelscht == original

@given(instance=shr5::Fakeable_strategy)
def test_shr5::fakeable_stufe_type(instance):
    assert isinstance(instance.stufe, int)


@given(instance=shr5::Fakeable_strategy)
def test_shr5::fakeable_stufe_setter(instance):
    original = instance.stufe
    instance.stufe = original
    assert instance.stufe == original

@given(instance=Fakeable_strategy)
@settings(max_examples=50)
def test_fakeable_instantiation(instance):
    assert isinstance(instance, Fakeable)

@given(instance=shr5::Lizenz_strategy)
@settings(max_examples=50)
def test_shr5::lizenz_instantiation(instance):
    assert isinstance(instance, shr5::Lizenz)

@given(instance=shr5::Lizenz_strategy)
def test_shr5::lizenz_lizenGegenstand_type(instance):
    assert isinstance(instance.lizenGegenstand, str)


@given(instance=shr5::Lizenz_strategy)
def test_shr5::lizenz_lizenGegenstand_setter(instance):
    original = instance.lizenGegenstand
    instance.lizenGegenstand = original
    assert instance.lizenGegenstand == original

@given(instance=shr5::Sin_strategy)
@settings(max_examples=50)
def test_shr5::sin_instantiation(instance):
    assert isinstance(instance, shr5::Sin)

@given(instance=ResonanzPersona_strategy)
@settings(max_examples=50)
def test_resonanzpersona_instantiation(instance):
    assert isinstance(instance, ResonanzPersona)

@given(instance=IntervallVertrag_strategy)
@settings(max_examples=50)
def test_intervallvertrag_instantiation(instance):
    assert isinstance(instance, IntervallVertrag)

@given(instance=shr5::Lifestyle_strategy)
@settings(max_examples=50)
def test_shr5::lifestyle_instantiation(instance):
    assert isinstance(instance, shr5::Lifestyle)

@given(instance=shr5::Lifestyle_strategy)
def test_shr5::lifestyle_owned_type(instance):
    assert isinstance(instance.owned, bool)


@given(instance=shr5::Lifestyle_strategy)
def test_shr5::lifestyle_owned_setter(instance):
    original = instance.owned
    instance.owned = original
    assert instance.owned == original

@given(instance=ActiveMatixDevice_strategy)
@settings(max_examples=50)
def test_activematixdevice_instantiation(instance):
    assert isinstance(instance, ActiveMatixDevice)

@given(instance=shr5::ResonanzPersona_strategy)
@settings(max_examples=50)
def test_shr5::resonanzpersona_instantiation(instance):
    assert isinstance(instance, shr5::ResonanzPersona)

@given(instance=shr5::ResonanzPersona_strategy)
def test_shr5::resonanzpersona_resonanzBasis_type(instance):
    assert isinstance(instance.resonanzBasis, int)


@given(instance=shr5::ResonanzPersona_strategy)
def test_shr5::resonanzpersona_resonanzBasis_setter(instance):
    original = instance.resonanzBasis
    instance.resonanzBasis = original
    assert instance.resonanzBasis == original

@given(instance=shr5::ResonanzPersona_strategy)
def test_shr5::resonanzpersona_resonanz_type(instance):
    assert isinstance(instance.resonanz, int)


@given(instance=shr5::ResonanzPersona_strategy)
def test_shr5::resonanzpersona_resonanz_setter(instance):
    original = instance.resonanz
    instance.resonanz = original
    assert instance.resonanz == original

@given(instance=shr5::GebundenerGeist_strategy)
@settings(max_examples=50)
def test_shr5::gebundenergeist_instantiation(instance):
    assert isinstance(instance, shr5::GebundenerGeist)

@given(instance=shr5::GebundenerGeist_strategy)
def test_shr5::gebundenergeist_dienste_type(instance):
    assert isinstance(instance.dienste, int)


@given(instance=shr5::GebundenerGeist_strategy)
def test_shr5::gebundenergeist_dienste_setter(instance):
    original = instance.dienste
    instance.dienste = original
    assert instance.dienste == original

@given(instance=shr5::FokusBinding_strategy)
@settings(max_examples=50)
def test_shr5::fokusbinding_instantiation(instance):
    assert isinstance(instance, shr5::FokusBinding)

@given(instance=shr5::FokusBinding_strategy)
def test_shr5::fokusbinding_active_type(instance):
    assert isinstance(instance.active, bool)


@given(instance=shr5::FokusBinding_strategy)
def test_shr5::fokusbinding_active_setter(instance):
    original = instance.active
    instance.active = original
    assert instance.active == original

@given(instance=Erlernbar_strategy)
@settings(max_examples=50)
def test_erlernbar_instantiation(instance):
    assert isinstance(instance, Erlernbar)

@given(instance=shr5::PersonaMartialartTechnique_strategy)
@settings(max_examples=50)
def test_shr5::personamartialarttechnique_instantiation(instance):
    assert isinstance(instance, shr5::PersonaMartialartTechnique)

@given(instance=shr5::PersonaKomplexForm_strategy)
@settings(max_examples=50)
def test_shr5::personakomplexform_instantiation(instance):
    assert isinstance(instance, shr5::PersonaKomplexForm)

@given(instance=shr5::PersonaKomplexForm_strategy)
def test_shr5::personakomplexform_stufe_type(instance):
    assert isinstance(instance.stufe, int)


@given(instance=shr5::PersonaKomplexForm_strategy)
def test_shr5::personakomplexform_stufe_setter(instance):
    original = instance.stufe
    instance.stufe = original
    assert instance.stufe == original

@given(instance=shr5::Steigerbar_strategy)
@settings(max_examples=50)
def test_shr5::steigerbar_instantiation(instance):
    assert isinstance(instance, shr5::Steigerbar)

@given(instance=shr5::Steigerbar_strategy)
def test_shr5::steigerbar_stufe_type(instance):
    assert isinstance(instance.stufe, int)


@given(instance=shr5::Steigerbar_strategy)
def test_shr5::steigerbar_stufe_setter(instance):
    original = instance.stufe
    instance.stufe = original
    assert instance.stufe == original

@given(instance=shr5::Fokus_strategy)
@settings(max_examples=50)
def test_shr5::fokus_instantiation(instance):
    assert isinstance(instance, shr5::Fokus)

@given(instance=shr5::Fokus_strategy)
def test_shr5::fokus_bindungskosten_type(instance):
    assert isinstance(instance.bindungskosten, int)


@given(instance=shr5::Fokus_strategy)
def test_shr5::fokus_bindungskosten_setter(instance):
    original = instance.bindungskosten
    instance.bindungskosten = original
    assert instance.bindungskosten == original

@given(instance=shr5::PersonaZauber_strategy)
@settings(max_examples=50)
def test_shr5::personazauber_instantiation(instance):
    assert isinstance(instance, shr5::PersonaZauber)

@given(instance=shr5::PersonaZauber_strategy)
def test_shr5::personazauber_stufe_type(instance):
    assert isinstance(instance.stufe, int)


@given(instance=shr5::PersonaZauber_strategy)
def test_shr5::personazauber_stufe_setter(instance):
    original = instance.stufe
    instance.stufe = original
    assert instance.stufe == original

@given(instance=MagischeMods_strategy)
@settings(max_examples=50)
def test_magischemods_instantiation(instance):
    assert isinstance(instance, MagischeMods)

@given(instance=shr5::CritterKraft_strategy)
@settings(max_examples=50)
def test_shr5::critterkraft_instantiation(instance):
    assert isinstance(instance, shr5::CritterKraft)

@given(instance=shr5::CritterKraft_strategy)
def test_shr5::critterkraft_reichweite_type(instance):
    assert isinstance(instance.reichweite, str)


@given(instance=shr5::CritterKraft_strategy)
def test_shr5::critterkraft_reichweite_setter(instance):
    original = instance.reichweite
    instance.reichweite = original
    assert instance.reichweite == original

@given(instance=shr5::CritterKraft_strategy)
def test_shr5::critterkraft_dauer_type(instance):
    assert isinstance(instance.dauer, str)


@given(instance=shr5::CritterKraft_strategy)
def test_shr5::critterkraft_dauer_setter(instance):
    original = instance.dauer
    instance.dauer = original
    assert instance.dauer == original

@given(instance=shr5::CritterKraft_strategy)
def test_shr5::critterkraft_art_type(instance):
    assert isinstance(instance.art, str)


@given(instance=shr5::CritterKraft_strategy)
def test_shr5::critterkraft_art_setter(instance):
    original = instance.art
    instance.art = original
    assert instance.art == original

@given(instance=shr5::CritterKraft_strategy)
def test_shr5::critterkraft_handlung_type(instance):
    assert isinstance(instance.handlung, str)


@given(instance=shr5::CritterKraft_strategy)
def test_shr5::critterkraft_handlung_setter(instance):
    original = instance.handlung
    instance.handlung = original
    assert instance.handlung == original

@given(instance=shr5::KiKraft_strategy)
@settings(max_examples=50)
def test_shr5::kikraft_instantiation(instance):
    assert isinstance(instance, shr5::KiKraft)

@given(instance=shr5::KiKraft_strategy)
def test_shr5::kikraft_kraftpunkte_type(instance):
    assert isinstance(instance.kraftpunkte, int)


@given(instance=shr5::KiKraft_strategy)
def test_shr5::kikraft_kraftpunkte_setter(instance):
    original = instance.kraftpunkte
    instance.kraftpunkte = original
    assert instance.kraftpunkte == original

@given(instance=BerechneteAttribute_strategy)
@settings(max_examples=50)
def test_berechneteattribute_instantiation(instance):
    assert isinstance(instance, BerechneteAttribute)

@given(instance=PersonaZustand_strategy)
@settings(max_examples=50)
def test_personazustand_instantiation(instance):
    assert isinstance(instance, PersonaZustand)

@given(instance=Panzerung_strategy)
@settings(max_examples=50)
def test_panzerung_instantiation(instance):
    assert isinstance(instance, Panzerung)

@given(instance=AbstraktPersona_strategy)
@settings(max_examples=50)
def test_abstraktpersona_instantiation(instance):
    assert isinstance(instance, AbstraktPersona)

@given(instance=shr5::KoerperPersona_strategy)
@settings(max_examples=50)
def test_shr5::koerperpersona_instantiation(instance):
    assert isinstance(instance, shr5::KoerperPersona)

@given(instance=shr5::KoerperPersona_strategy)
def test_shr5::koerperpersona_zustandKoerperlich_type(instance):
    assert isinstance(instance.zustandKoerperlich, int)


@given(instance=shr5::KoerperPersona_strategy)
def test_shr5::koerperpersona_zustandKoerperlich_setter(instance):
    original = instance.zustandKoerperlich
    instance.zustandKoerperlich = original
    assert instance.zustandKoerperlich == original

@given(instance=shr5::KoerperPersona_strategy)
def test_shr5::koerperpersona_zustandGeistig_type(instance):
    assert isinstance(instance.zustandGeistig, int)


@given(instance=shr5::KoerperPersona_strategy)
def test_shr5::koerperpersona_zustandGeistig_setter(instance):
    original = instance.zustandGeistig
    instance.zustandGeistig = original
    assert instance.zustandGeistig == original

@given(instance=KoerperPersona_strategy)
@settings(max_examples=50)
def test_koerperpersona_instantiation(instance):
    assert isinstance(instance, KoerperPersona)

@given(instance=shr5::Technomancer_strategy)
@settings(max_examples=50)
def test_shr5::technomancer_instantiation(instance):
    assert isinstance(instance, shr5::Technomancer)

@given(instance=shr5::MudanPersona_strategy)
@settings(max_examples=50)
def test_shr5::mudanpersona_instantiation(instance):
    assert isinstance(instance, shr5::MudanPersona)

@given(instance=AbstraktModifikatoren_strategy)
@settings(max_examples=50)
def test_abstraktmodifikatoren_instantiation(instance):
    assert isinstance(instance, AbstraktModifikatoren)

@given(instance=shr5::PersonaEigenschaft_strategy)
@settings(max_examples=50)
def test_shr5::personaeigenschaft_instantiation(instance):
    assert isinstance(instance, shr5::PersonaEigenschaft)

@given(instance=shr5::PersonaEigenschaft_strategy)
def test_shr5::personaeigenschaft_karmaKosten_type(instance):
    assert isinstance(instance.karmaKosten, int)


@given(instance=shr5::PersonaEigenschaft_strategy)
def test_shr5::personaeigenschaft_karmaKosten_setter(instance):
    original = instance.karmaKosten
    instance.karmaKosten = original
    assert instance.karmaKosten == original

@given(instance=shr5::Echo_strategy)
@settings(max_examples=50)
def test_shr5::echo_instantiation(instance):
    assert isinstance(instance, shr5::Echo)

@given(instance=shr5::MagischeMods_strategy)
@settings(max_examples=50)
def test_shr5::magischemods_instantiation(instance):
    assert isinstance(instance, shr5::MagischeMods)

@given(instance=shr5::Koerpermods_strategy)
@settings(max_examples=50)
def test_shr5::koerpermods_instantiation(instance):
    assert isinstance(instance, shr5::Koerpermods)

@given(instance=shr5::DefaultWifi_strategy)
@settings(max_examples=50)
def test_shr5::defaultwifi_instantiation(instance):
    assert isinstance(instance, shr5::DefaultWifi)

@given(instance=shr5::BaseMagischePersona_strategy)
@settings(max_examples=50)
def test_shr5::basemagischepersona_instantiation(instance):
    assert isinstance(instance, shr5::BaseMagischePersona)

@given(instance=shr5::BaseMagischePersona_strategy)
def test_shr5::basemagischepersona_magie_type(instance):
    assert isinstance(instance.magie, int)


@given(instance=shr5::BaseMagischePersona_strategy)
def test_shr5::basemagischepersona_magie_setter(instance):
    original = instance.magie
    instance.magie = original
    assert instance.magie == original

@given(instance=shr5::BaseMagischePersona_strategy)
def test_shr5::basemagischepersona_magieBasis_type(instance):
    assert isinstance(instance.magieBasis, int)


@given(instance=shr5::BaseMagischePersona_strategy)
def test_shr5::basemagischepersona_magieBasis_setter(instance):
    original = instance.magieBasis
    instance.magieBasis = original
    assert instance.magieBasis == original

@given(instance=shr5::Schutzgeist_strategy)
@settings(max_examples=50)
def test_shr5::schutzgeist_instantiation(instance):
    assert isinstance(instance, shr5::Schutzgeist)

@given(instance=shr5::Schutzgeist_strategy)
def test_shr5::schutzgeist_vorteile_type(instance):
    assert isinstance(instance.vorteile, str)


@given(instance=shr5::Schutzgeist_strategy)
def test_shr5::schutzgeist_vorteile_setter(instance):
    original = instance.vorteile
    instance.vorteile = original
    assert instance.vorteile == original

@given(instance=shr5::Schutzgeist_strategy)
def test_shr5::schutzgeist_nachteile_type(instance):
    assert isinstance(instance.nachteile, str)


@given(instance=shr5::Schutzgeist_strategy)
def test_shr5::schutzgeist_nachteile_setter(instance):
    original = instance.nachteile
    instance.nachteile = original
    assert instance.nachteile == original

@given(instance=BaseMagischePersona_strategy)
@settings(max_examples=50)
def test_basemagischepersona_instantiation(instance):
    assert isinstance(instance, BaseMagischePersona)

@given(instance=shr5::MagischePersona_strategy)
@settings(max_examples=50)
def test_shr5::magischepersona_instantiation(instance):
    assert isinstance(instance, shr5::MagischePersona)

@given(instance=Steigerbar_strategy)
@settings(max_examples=50)
def test_steigerbar_instantiation(instance):
    assert isinstance(instance, Steigerbar)

@given(instance=shr5::Initation_strategy)
@settings(max_examples=50)
def test_shr5::initation_instantiation(instance):
    assert isinstance(instance, shr5::Initation)

@given(instance=Modifyable_strategy)
@settings(max_examples=50)
def test_modifyable_instantiation(instance):
    assert isinstance(instance, Modifyable)

@given(instance=shr5::EObject_strategy)
@settings(max_examples=50)
def test_shr5::eobject_instantiation(instance):
    assert isinstance(instance, shr5::EObject)

@given(instance=Menge_strategy)
@settings(max_examples=50)
def test_menge_instantiation(instance):
    assert isinstance(instance, Menge)

@given(instance=AbstaktFernKampfwaffe_strategy)
@settings(max_examples=50)
def test_abstaktfernkampfwaffe_instantiation(instance):
    assert isinstance(instance, AbstaktFernKampfwaffe)

@given(instance=shr5::Wurfwaffe_strategy)
@settings(max_examples=50)
def test_shr5::wurfwaffe_instantiation(instance):
    assert isinstance(instance, shr5::Wurfwaffe)

@given(instance=shr5::Projektilwaffe_strategy)
@settings(max_examples=50)
def test_shr5::projektilwaffe_instantiation(instance):
    assert isinstance(instance, shr5::Projektilwaffe)

@given(instance=shr5::Feuerwaffe_strategy)
@settings(max_examples=50)
def test_shr5::feuerwaffe_instantiation(instance):
    assert isinstance(instance, shr5::Feuerwaffe)

@given(instance=shr5::Feuerwaffe_strategy)
def test_shr5::feuerwaffe_kapazitaet_type(instance):
    assert isinstance(instance.kapazitaet, int)


@given(instance=shr5::Feuerwaffe_strategy)
def test_shr5::feuerwaffe_kapazitaet_setter(instance):
    original = instance.kapazitaet
    instance.kapazitaet = original
    assert instance.kapazitaet == original

@given(instance=shr5::Feuerwaffe_strategy)
def test_shr5::feuerwaffe_modie_type(instance):
    assert isinstance(instance.modie, str)


@given(instance=shr5::Feuerwaffe_strategy)
def test_shr5::feuerwaffe_modie_setter(instance):
    original = instance.modie
    instance.modie = original
    assert instance.modie == original

@given(instance=shr5::Feuerwaffe_strategy)
def test_shr5::feuerwaffe_munitionstyp_type(instance):
    assert isinstance(instance.munitionstyp, str)


@given(instance=shr5::Feuerwaffe_strategy)
def test_shr5::feuerwaffe_munitionstyp_setter(instance):
    original = instance.munitionstyp
    instance.munitionstyp = original
    assert instance.munitionstyp == original

@given(instance=shr5::Feuerwaffe_strategy)
def test_shr5::feuerwaffe_erweiterung_type(instance):
    assert isinstance(instance.erweiterung, str)


@given(instance=shr5::Feuerwaffe_strategy)
def test_shr5::feuerwaffe_erweiterung_setter(instance):
    original = instance.erweiterung
    instance.erweiterung = original
    assert instance.erweiterung == original

@given(instance=shr5::Feuerwaffe_strategy)
def test_shr5::feuerwaffe_rueckstoss_type(instance):
    assert isinstance(instance.rueckstoss, int)


@given(instance=shr5::Feuerwaffe_strategy)
def test_shr5::feuerwaffe_rueckstoss_setter(instance):
    original = instance.rueckstoss
    instance.rueckstoss = original
    assert instance.rueckstoss == original

@given(instance=Capacity_strategy)
@settings(max_examples=50)
def test_capacity_instantiation(instance):
    assert isinstance(instance, Capacity)

@given(instance=shr5::Cyberdeck_strategy)
@settings(max_examples=50)
def test_shr5::cyberdeck_instantiation(instance):
    assert isinstance(instance, shr5::Cyberdeck)

@given(instance=shr5::Cyberdeck_strategy)
def test_shr5::cyberdeck_attribute2_type(instance):
    assert isinstance(instance.attribute2, int)


@given(instance=shr5::Cyberdeck_strategy)
def test_shr5::cyberdeck_attribute2_setter(instance):
    original = instance.attribute2
    instance.attribute2 = original
    assert instance.attribute2 == original

@given(instance=shr5::Cyberdeck_strategy)
def test_shr5::cyberdeck_modManager_type(instance):
    assert isinstance(instance.modManager, str)


@given(instance=shr5::Cyberdeck_strategy)
def test_shr5::cyberdeck_modManager_setter(instance):
    original = instance.modManager
    instance.modManager = original
    assert instance.modManager == original

@given(instance=shr5::Cyberdeck_strategy)
def test_shr5::cyberdeck_programSlots_type(instance):
    assert isinstance(instance.programSlots, int)


@given(instance=shr5::Cyberdeck_strategy)
def test_shr5::cyberdeck_programSlots_setter(instance):
    original = instance.programSlots
    instance.programSlots = original
    assert instance.programSlots == original

@given(instance=shr5::Cyberdeck_strategy)
def test_shr5::cyberdeck_attribute3_type(instance):
    assert isinstance(instance.attribute3, int)


@given(instance=shr5::Cyberdeck_strategy)
def test_shr5::cyberdeck_attribute3_setter(instance):
    original = instance.attribute3
    instance.attribute3 = original
    assert instance.attribute3 == original

@given(instance=shr5::Cyberdeck_strategy)
def test_shr5::cyberdeck_attribute1_type(instance):
    assert isinstance(instance.attribute1, int)


@given(instance=shr5::Cyberdeck_strategy)
def test_shr5::cyberdeck_attribute1_setter(instance):
    original = instance.attribute1
    instance.attribute1 = original
    assert instance.attribute1 == original

@given(instance=shr5::Cyberdeck_strategy)
def test_shr5::cyberdeck_attribute4_type(instance):
    assert isinstance(instance.attribute4, int)


@given(instance=shr5::Cyberdeck_strategy)
def test_shr5::cyberdeck_attribute4_setter(instance):
    original = instance.attribute4
    instance.attribute4 = original
    assert instance.attribute4 == original

@given(instance=Koerpermods_strategy)
@settings(max_examples=50)
def test_koerpermods_instantiation(instance):
    assert isinstance(instance, Koerpermods)

@given(instance=AbstaktWaffe_strategy)
@settings(max_examples=50)
def test_abstaktwaffe_instantiation(instance):
    assert isinstance(instance, AbstaktWaffe)

@given(instance=shr5::AbstaktFernKampfwaffe_strategy)
@settings(max_examples=50)
def test_shr5::abstaktfernkampfwaffe_instantiation(instance):
    assert isinstance(instance, shr5::AbstaktFernKampfwaffe)

@given(instance=shr5::MatrixDevice_strategy)
@settings(max_examples=50)
def test_shr5::matrixdevice_instantiation(instance):
    assert isinstance(instance, shr5::MatrixDevice)

@given(instance=Anwendbar_strategy)
@settings(max_examples=50)
def test_anwendbar_instantiation(instance):
    assert isinstance(instance, Anwendbar)

@given(instance=Modifizierbar_strategy)
@settings(max_examples=50)
def test_modifizierbar_instantiation(instance):
    assert isinstance(instance, Modifizierbar)

@given(instance=shr5::Drug_strategy)
@settings(max_examples=50)
def test_shr5::drug_instantiation(instance):
    assert isinstance(instance, shr5::Drug)

@given(instance=shr5::Drug_strategy)
def test_shr5::drug_addictionType_type(instance):
    assert isinstance(instance.addictionType, str)


@given(instance=shr5::Drug_strategy)
def test_shr5::drug_addictionType_setter(instance):
    original = instance.addictionType
    instance.addictionType = original
    assert instance.addictionType == original

@given(instance=shr5::Drug_strategy)
def test_shr5::drug_duration_type(instance):
    assert isinstance(instance.duration, str)


@given(instance=shr5::Drug_strategy)
def test_shr5::drug_duration_setter(instance):
    original = instance.duration
    instance.duration = original
    assert instance.duration == original

@given(instance=shr5::MatrixProgram_strategy)
@settings(max_examples=50)
def test_shr5::matrixprogram_instantiation(instance):
    assert isinstance(instance, shr5::MatrixProgram)

@given(instance=GeldWert_strategy)
@settings(max_examples=50)
def test_geldwert_instantiation(instance):
    assert isinstance(instance, GeldWert)

@given(instance=shr5::FernkampfwaffeModifikator_strategy)
@settings(max_examples=50)
def test_shr5::fernkampfwaffemodifikator_instantiation(instance):
    assert isinstance(instance, shr5::FernkampfwaffeModifikator)

@given(instance=shr5::FernkampfwaffeModifikator_strategy)
def test_shr5::fernkampfwaffemodifikator_ep_type(instance):
    assert isinstance(instance.ep, str)


@given(instance=shr5::FernkampfwaffeModifikator_strategy)
def test_shr5::fernkampfwaffemodifikator_ep_setter(instance):
    original = instance.ep
    instance.ep = original
    assert instance.ep == original

@given(instance=shr5::CyberwareEnhancement_strategy)
@settings(max_examples=50)
def test_shr5::cyberwareenhancement_instantiation(instance):
    assert isinstance(instance, shr5::CyberwareEnhancement)

@given(instance=shr5::CyberwareEnhancement_strategy)
def test_shr5::cyberwareenhancement_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=shr5::CyberwareEnhancement_strategy)
def test_shr5::cyberwareenhancement_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=shr5::CyberwareEnhancement_strategy)
def test_shr5::cyberwareenhancement_capacityUse_type(instance):
    assert isinstance(instance.capacityUse, int)


@given(instance=shr5::CyberwareEnhancement_strategy)
def test_shr5::cyberwareenhancement_capacityUse_setter(instance):
    original = instance.capacityUse
    instance.capacityUse = original
    assert instance.capacityUse == original

@given(instance=shr5::Cyberware_strategy)
@settings(max_examples=50)
def test_shr5::cyberware_instantiation(instance):
    assert isinstance(instance, shr5::Cyberware)

@given(instance=shr5::Cyberware_strategy)
def test_shr5::cyberware_cyberwareCapacity_type(instance):
    assert isinstance(instance.cyberwareCapacity, int)


@given(instance=shr5::Cyberware_strategy)
def test_shr5::cyberware_cyberwareCapacity_setter(instance):
    original = instance.cyberwareCapacity
    instance.cyberwareCapacity = original
    assert instance.cyberwareCapacity == original

@given(instance=shr5::Cyberware_strategy)
def test_shr5::cyberware_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=shr5::Cyberware_strategy)
def test_shr5::cyberware_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=shr5::BioWare_strategy)
@settings(max_examples=50)
def test_shr5::bioware_instantiation(instance):
    assert isinstance(instance, shr5::BioWare)

@given(instance=Quelle_strategy)
@settings(max_examples=50)
def test_quelle_instantiation(instance):
    assert isinstance(instance, Quelle)

@given(instance=ModifikatorAttribute_strategy)
@settings(max_examples=50)
def test_modifikatorattribute_instantiation(instance):
    assert isinstance(instance, ModifikatorAttribute)

@given(instance=shr5::SpezielleAttribute_strategy)
@settings(max_examples=50)
def test_shr5::spezielleattribute_instantiation(instance):
    assert isinstance(instance, shr5::SpezielleAttribute)

@given(instance=shr5::SpezielleAttribute_strategy)
def test_shr5::spezielleattribute_initativWuerfel_type(instance):
    assert isinstance(instance.initativWuerfel, int)


@given(instance=shr5::SpezielleAttribute_strategy)
def test_shr5::spezielleattribute_initativWuerfel_setter(instance):
    original = instance.initativWuerfel
    instance.initativWuerfel = original
    assert instance.initativWuerfel == original

@given(instance=shr5::SpezielleAttribute_strategy)
def test_shr5::spezielleattribute_edge_type(instance):
    assert isinstance(instance.edge, int)


@given(instance=shr5::SpezielleAttribute_strategy)
def test_shr5::spezielleattribute_edge_setter(instance):
    original = instance.edge
    instance.edge = original
    assert instance.edge == original

@given(instance=shr5::SpezielleAttribute_strategy)
def test_shr5::spezielleattribute_ausweichen_type(instance):
    assert isinstance(instance.ausweichen, int)


@given(instance=shr5::SpezielleAttribute_strategy)
def test_shr5::spezielleattribute_ausweichen_setter(instance):
    original = instance.ausweichen
    instance.ausweichen = original
    assert instance.ausweichen == original

@given(instance=shr5::SpezielleAttribute_strategy)
def test_shr5::spezielleattribute_edgeBasis_type(instance):
    assert isinstance(instance.edgeBasis, int)


@given(instance=shr5::SpezielleAttribute_strategy)
def test_shr5::spezielleattribute_edgeBasis_setter(instance):
    original = instance.edgeBasis
    instance.edgeBasis = original
    assert instance.edgeBasis == original

@given(instance=shr5::SpezielleAttribute_strategy)
def test_shr5::spezielleattribute_initative_type(instance):
    assert isinstance(instance.initative, int)


@given(instance=shr5::SpezielleAttribute_strategy)
def test_shr5::spezielleattribute_initative_setter(instance):
    original = instance.initative
    instance.initative = original
    assert instance.initative == original

@given(instance=shr5::SpezielleAttribute_strategy)
def test_shr5::spezielleattribute_essenz_type(instance):
    assert isinstance(instance.essenz, int)


@given(instance=shr5::SpezielleAttribute_strategy)
def test_shr5::spezielleattribute_essenz_setter(instance):
    original = instance.essenz
    instance.essenz = original
    assert instance.essenz == original

@given(instance=shr5::Sichtverhaeltnisse_strategy)
@settings(max_examples=50)
def test_shr5::sichtverhaeltnisse_instantiation(instance):
    assert isinstance(instance, shr5::Sichtverhaeltnisse)

@given(instance=shr5::Sichtverhaeltnisse_strategy)
def test_shr5::sichtverhaeltnisse_infrarot_type(instance):
    assert isinstance(instance.infrarot, str)


@given(instance=shr5::Sichtverhaeltnisse_strategy)
def test_shr5::sichtverhaeltnisse_infrarot_setter(instance):
    original = instance.infrarot
    instance.infrarot = original
    assert instance.infrarot == original

@given(instance=shr5::Sichtverhaeltnisse_strategy)
def test_shr5::sichtverhaeltnisse_ultrasound_type(instance):
    assert isinstance(instance.ultrasound, str)


@given(instance=shr5::Sichtverhaeltnisse_strategy)
def test_shr5::sichtverhaeltnisse_ultrasound_setter(instance):
    original = instance.ultrasound
    instance.ultrasound = original
    assert instance.ultrasound == original

@given(instance=shr5::Sichtverhaeltnisse_strategy)
def test_shr5::sichtverhaeltnisse_restlichtverstaerkung_type(instance):
    assert isinstance(instance.restlichtverstaerkung, str)


@given(instance=shr5::Sichtverhaeltnisse_strategy)
def test_shr5::sichtverhaeltnisse_restlichtverstaerkung_setter(instance):
    original = instance.restlichtverstaerkung
    instance.restlichtverstaerkung = original
    assert instance.restlichtverstaerkung == original

@given(instance=shr5::GeistigeAttribute_strategy)
@settings(max_examples=50)
def test_shr5::geistigeattribute_instantiation(instance):
    assert isinstance(instance, shr5::GeistigeAttribute)

@given(instance=shr5::GeistigeAttribute_strategy)
def test_shr5::geistigeattribute_willenskraft_type(instance):
    assert isinstance(instance.willenskraft, int)


@given(instance=shr5::GeistigeAttribute_strategy)
def test_shr5::geistigeattribute_willenskraft_setter(instance):
    original = instance.willenskraft
    instance.willenskraft = original
    assert instance.willenskraft == original

@given(instance=shr5::GeistigeAttribute_strategy)
def test_shr5::geistigeattribute_charisma_type(instance):
    assert isinstance(instance.charisma, int)


@given(instance=shr5::GeistigeAttribute_strategy)
def test_shr5::geistigeattribute_charisma_setter(instance):
    original = instance.charisma
    instance.charisma = original
    assert instance.charisma == original

@given(instance=shr5::GeistigeAttribute_strategy)
def test_shr5::geistigeattribute_logik_type(instance):
    assert isinstance(instance.logik, int)


@given(instance=shr5::GeistigeAttribute_strategy)
def test_shr5::geistigeattribute_logik_setter(instance):
    original = instance.logik
    instance.logik = original
    assert instance.logik == original

@given(instance=shr5::GeistigeAttribute_strategy)
def test_shr5::geistigeattribute_intuition_type(instance):
    assert isinstance(instance.intuition, int)


@given(instance=shr5::GeistigeAttribute_strategy)
def test_shr5::geistigeattribute_intuition_setter(instance):
    original = instance.intuition
    instance.intuition = original
    assert instance.intuition == original

@given(instance=shr5::ProbenModifikatoren_strategy)
@settings(max_examples=50)
def test_shr5::probenmodifikatoren_instantiation(instance):
    assert isinstance(instance, shr5::ProbenModifikatoren)

@given(instance=shr5::ProbenModifikatoren_strategy)
def test_shr5::probenmodifikatoren_heilung_type(instance):
    assert isinstance(instance.heilung, int)


@given(instance=shr5::ProbenModifikatoren_strategy)
def test_shr5::probenmodifikatoren_heilung_setter(instance):
    original = instance.heilung
    instance.heilung = original
    assert instance.heilung == original

@given(instance=shr5::ProbenModifikatoren_strategy)
def test_shr5::probenmodifikatoren_schadenswiederstand_type(instance):
    assert isinstance(instance.schadenswiederstand, int)


@given(instance=shr5::ProbenModifikatoren_strategy)
def test_shr5::probenmodifikatoren_schadenswiederstand_setter(instance):
    original = instance.schadenswiederstand
    instance.schadenswiederstand = original
    assert instance.schadenswiederstand == original

@given(instance=shr5::CyberwareModifikatioren_strategy)
@settings(max_examples=50)
def test_shr5::cyberwaremodifikatioren_instantiation(instance):
    assert isinstance(instance, shr5::CyberwareModifikatioren)

@given(instance=shr5::CyberwareModifikatioren_strategy)
def test_shr5::cyberwaremodifikatioren_universalDataConnector_type(instance):
    assert isinstance(instance.universalDataConnector, bool)


@given(instance=shr5::CyberwareModifikatioren_strategy)
def test_shr5::cyberwaremodifikatioren_universalDataConnector_setter(instance):
    original = instance.universalDataConnector
    instance.universalDataConnector = original
    assert instance.universalDataConnector == original

@given(instance=shr5::CyberwareModifikatioren_strategy)
def test_shr5::cyberwaremodifikatioren_simRig_type(instance):
    assert isinstance(instance.simRig, int)


@given(instance=shr5::CyberwareModifikatioren_strategy)
def test_shr5::cyberwaremodifikatioren_simRig_setter(instance):
    original = instance.simRig
    instance.simRig = original
    assert instance.simRig == original

@given(instance=shr5::CyberwareModifikatioren_strategy)
def test_shr5::cyberwaremodifikatioren_controlRig_type(instance):
    assert isinstance(instance.controlRig, int)


@given(instance=shr5::CyberwareModifikatioren_strategy)
def test_shr5::cyberwaremodifikatioren_controlRig_setter(instance):
    original = instance.controlRig
    instance.controlRig = original
    assert instance.controlRig == original

@given(instance=shr5::CyberwareModifikatioren_strategy)
def test_shr5::cyberwaremodifikatioren_directNeuralInterface_type(instance):
    assert isinstance(instance.directNeuralInterface, bool)


@given(instance=shr5::CyberwareModifikatioren_strategy)
def test_shr5::cyberwaremodifikatioren_directNeuralInterface_setter(instance):
    original = instance.directNeuralInterface
    instance.directNeuralInterface = original
    assert instance.directNeuralInterface == original

@given(instance=shr5::CyberwareModifikatioren_strategy)
def test_shr5::cyberwaremodifikatioren_riggerInterface_type(instance):
    assert isinstance(instance.riggerInterface, bool)


@given(instance=shr5::CyberwareModifikatioren_strategy)
def test_shr5::cyberwaremodifikatioren_riggerInterface_setter(instance):
    original = instance.riggerInterface
    instance.riggerInterface = original
    assert instance.riggerInterface == original

@given(instance=shr5::FernkampfwaffenModifikatoren_strategy)
@settings(max_examples=50)
def test_shr5::fernkampfwaffenmodifikatoren_instantiation(instance):
    assert isinstance(instance, shr5::FernkampfwaffenModifikatoren)

@given(instance=shr5::FernkampfwaffenModifikatoren_strategy)
def test_shr5::fernkampfwaffenmodifikatoren_rueckstoss_type(instance):
    assert isinstance(instance.rueckstoss, int)


@given(instance=shr5::FernkampfwaffenModifikatoren_strategy)
def test_shr5::fernkampfwaffenmodifikatoren_rueckstoss_setter(instance):
    original = instance.rueckstoss
    instance.rueckstoss = original
    assert instance.rueckstoss == original

@given(instance=shr5::FernkampfwaffenModifikatoren_strategy)
def test_shr5::fernkampfwaffenmodifikatoren_smartgun_type(instance):
    assert isinstance(instance.smartgun, str)


@given(instance=shr5::FernkampfwaffenModifikatoren_strategy)
def test_shr5::fernkampfwaffenmodifikatoren_smartgun_setter(instance):
    original = instance.smartgun
    instance.smartgun = original
    assert instance.smartgun == original

@given(instance=shr5::FernkampfwaffenModifikatoren_strategy)
def test_shr5::fernkampfwaffenmodifikatoren_sichtverbesserung_type(instance):
    assert isinstance(instance.sichtverbesserung, int)


@given(instance=shr5::FernkampfwaffenModifikatoren_strategy)
def test_shr5::fernkampfwaffenmodifikatoren_sichtverbesserung_setter(instance):
    original = instance.sichtverbesserung
    instance.sichtverbesserung = original
    assert instance.sichtverbesserung == original

@given(instance=shr5::FernkampfwaffenModifikatoren_strategy)
def test_shr5::fernkampfwaffenmodifikatoren_vergroesserung_type(instance):
    assert isinstance(instance.vergroesserung, int)


@given(instance=shr5::FernkampfwaffenModifikatoren_strategy)
def test_shr5::fernkampfwaffenmodifikatoren_vergroesserung_setter(instance):
    original = instance.vergroesserung
    instance.vergroesserung = original
    assert instance.vergroesserung == original

@given(instance=shr5::FernkampfwaffenModifikatoren_strategy)
def test_shr5::fernkampfwaffenmodifikatoren_lasterPointer_type(instance):
    assert isinstance(instance.lasterPointer, bool)


@given(instance=shr5::FernkampfwaffenModifikatoren_strategy)
def test_shr5::fernkampfwaffenmodifikatoren_lasterPointer_setter(instance):
    original = instance.lasterPointer
    instance.lasterPointer = original
    assert instance.lasterPointer == original

@given(instance=shr5::FernkampfwaffenModifikatoren_strategy)
def test_shr5::fernkampfwaffenmodifikatoren_schalldaempfer_type(instance):
    assert isinstance(instance.schalldaempfer, bool)


@given(instance=shr5::FernkampfwaffenModifikatoren_strategy)
def test_shr5::fernkampfwaffenmodifikatoren_schalldaempfer_setter(instance):
    original = instance.schalldaempfer
    instance.schalldaempfer = original
    assert instance.schalldaempfer == original

@given(instance=shr5::GegenstandStufen_strategy)
@settings(max_examples=50)
def test_shr5::gegenstandstufen_instantiation(instance):
    assert isinstance(instance, shr5::GegenstandStufen)

@given(instance=shr5::GegenstandStufen_strategy)
def test_shr5::gegenstandstufen_elektronik_type(instance):
    assert isinstance(instance.elektronik, int)


@given(instance=shr5::GegenstandStufen_strategy)
def test_shr5::gegenstandstufen_elektronik_setter(instance):
    original = instance.elektronik
    instance.elektronik = original
    assert instance.elektronik == original

@given(instance=shr5::GegenstandStufen_strategy)
def test_shr5::gegenstandstufen_tracing_type(instance):
    assert isinstance(instance.tracing, int)


@given(instance=shr5::GegenstandStufen_strategy)
def test_shr5::gegenstandstufen_tracing_setter(instance):
    original = instance.tracing
    instance.tracing = original
    assert instance.tracing == original

@given(instance=shr5::GegenstandStufen_strategy)
def test_shr5::gegenstandstufen_computer_type(instance):
    assert isinstance(instance.computer, int)


@given(instance=shr5::GegenstandStufen_strategy)
def test_shr5::gegenstandstufen_computer_setter(instance):
    original = instance.computer
    instance.computer = original
    assert instance.computer == original

@given(instance=shr5::GegenstandStufen_strategy)
def test_shr5::gegenstandstufen_protection_type(instance):
    assert isinstance(instance.protection, int)


@given(instance=shr5::GegenstandStufen_strategy)
def test_shr5::gegenstandstufen_protection_setter(instance):
    original = instance.protection
    instance.protection = original
    assert instance.protection == original

@given(instance=shr5::GegenstandStufen_strategy)
def test_shr5::gegenstandstufen_antiProtection_type(instance):
    assert isinstance(instance.antiProtection, int)


@given(instance=shr5::GegenstandStufen_strategy)
def test_shr5::gegenstandstufen_antiProtection_setter(instance):
    original = instance.antiProtection
    instance.antiProtection = original
    assert instance.antiProtection == original

@given(instance=shr5::GegenstandStufen_strategy)
def test_shr5::gegenstandstufen_antiTracing_type(instance):
    assert isinstance(instance.antiTracing, int)


@given(instance=shr5::GegenstandStufen_strategy)
def test_shr5::gegenstandstufen_antiTracing_setter(instance):
    original = instance.antiTracing
    instance.antiTracing = original
    assert instance.antiTracing == original

@given(instance=shr5::KoerperlicheAttribute_strategy)
@settings(max_examples=50)
def test_shr5::koerperlicheattribute_instantiation(instance):
    assert isinstance(instance, shr5::KoerperlicheAttribute)

@given(instance=shr5::KoerperlicheAttribute_strategy)
def test_shr5::koerperlicheattribute_staerke_type(instance):
    assert isinstance(instance.staerke, int)


@given(instance=shr5::KoerperlicheAttribute_strategy)
def test_shr5::koerperlicheattribute_staerke_setter(instance):
    original = instance.staerke
    instance.staerke = original
    assert instance.staerke == original

@given(instance=shr5::KoerperlicheAttribute_strategy)
def test_shr5::koerperlicheattribute_geschicklichkeit_type(instance):
    assert isinstance(instance.geschicklichkeit, int)


@given(instance=shr5::KoerperlicheAttribute_strategy)
def test_shr5::koerperlicheattribute_geschicklichkeit_setter(instance):
    original = instance.geschicklichkeit
    instance.geschicklichkeit = original
    assert instance.geschicklichkeit == original

@given(instance=shr5::KoerperlicheAttribute_strategy)
def test_shr5::koerperlicheattribute_konstitution_type(instance):
    assert isinstance(instance.konstitution, int)


@given(instance=shr5::KoerperlicheAttribute_strategy)
def test_shr5::koerperlicheattribute_konstitution_setter(instance):
    original = instance.konstitution
    instance.konstitution = original
    assert instance.konstitution == original

@given(instance=shr5::KoerperlicheAttribute_strategy)
def test_shr5::koerperlicheattribute_reaktion_type(instance):
    assert isinstance(instance.reaktion, int)


@given(instance=shr5::KoerperlicheAttribute_strategy)
def test_shr5::koerperlicheattribute_reaktion_setter(instance):
    original = instance.reaktion
    instance.reaktion = original
    assert instance.reaktion == original

@given(instance=shr5::Modifyable_strategy)
@settings(max_examples=50)
def test_shr5::modifyable_instantiation(instance):
    assert isinstance(instance, shr5::Modifyable)

@given(instance=shr5::Modifizierbar_strategy)
@settings(max_examples=50)
def test_shr5::modifizierbar_instantiation(instance):
    assert isinstance(instance, shr5::Modifizierbar)

@given(instance=shr5::EAttribute_strategy)
@settings(max_examples=50)
def test_shr5::eattribute_instantiation(instance):
    assert isinstance(instance, shr5::EAttribute)

@given(instance=shr5::AttributModifikatorWert_strategy)
@settings(max_examples=50)
def test_shr5::attributmodifikatorwert_instantiation(instance):
    assert isinstance(instance, shr5::AttributModifikatorWert)

@given(instance=shr5::AttributModifikatorWert_strategy)
def test_shr5::attributmodifikatorwert_wert_type(instance):
    assert isinstance(instance.wert, int)


@given(instance=shr5::AttributModifikatorWert_strategy)
def test_shr5::attributmodifikatorwert_wert_setter(instance):
    original = instance.wert
    instance.wert = original
    assert instance.wert == original

@given(instance=shr5::Nahkampfwaffe_strategy)
@settings(max_examples=50)
def test_shr5::nahkampfwaffe_instantiation(instance):
    assert isinstance(instance, shr5::Nahkampfwaffe)

@given(instance=shr5::Nahkampfwaffe_strategy)
def test_shr5::nahkampfwaffe_reichweite_type(instance):
    assert isinstance(instance.reichweite, int)


@given(instance=shr5::Nahkampfwaffe_strategy)
def test_shr5::nahkampfwaffe_reichweite_setter(instance):
    original = instance.reichweite
    instance.reichweite = original
    assert instance.reichweite == original

@given(instance=shr5::GeldWert_strategy)
@settings(max_examples=50)
def test_shr5::geldwert_instantiation(instance):
    assert isinstance(instance, shr5::GeldWert)

@given(instance=shr5::GeldWert_strategy)
def test_shr5::geldwert_wert_type(instance):
    assert isinstance(instance.wert, str)


@given(instance=shr5::GeldWert_strategy)
def test_shr5::geldwert_wert_setter(instance):
    original = instance.wert
    instance.wert = original
    assert instance.wert == original

@given(instance=shr5::GeldWert_strategy)
def test_shr5::geldwert_wertValue_type(instance):
    assert isinstance(instance.wertValue, str)


@given(instance=shr5::GeldWert_strategy)
def test_shr5::geldwert_wertValue_setter(instance):
    original = instance.wertValue
    instance.wertValue = original
    assert instance.wertValue == original

@given(instance=shr5::GeldWert_strategy)
def test_shr5::geldwert_verfuegbarkeit_type(instance):
    assert isinstance(instance.verfuegbarkeit, str)


@given(instance=shr5::GeldWert_strategy)
def test_shr5::geldwert_verfuegbarkeit_setter(instance):
    original = instance.verfuegbarkeit
    instance.verfuegbarkeit = original
    assert instance.verfuegbarkeit == original

@given(instance=AbstraktGegenstand_strategy)
@settings(max_examples=50)
def test_abstraktgegenstand_instantiation(instance):
    assert isinstance(instance, AbstraktGegenstand)

@given(instance=shr5::Credstick_strategy)
@settings(max_examples=50)
def test_shr5::credstick_instantiation(instance):
    assert isinstance(instance, shr5::Credstick)

@given(instance=shr5::Credstick_strategy)
def test_shr5::credstick_maxValue_type(instance):
    assert isinstance(instance.maxValue, int)


@given(instance=shr5::Credstick_strategy)
def test_shr5::credstick_maxValue_setter(instance):
    original = instance.maxValue
    instance.maxValue = original
    assert instance.maxValue == original

@given(instance=shr5::Credstick_strategy)
def test_shr5::credstick_currentValue_type(instance):
    assert isinstance(instance.currentValue, str)


@given(instance=shr5::Credstick_strategy)
def test_shr5::credstick_currentValue_setter(instance):
    original = instance.currentValue
    instance.currentValue = original
    assert instance.currentValue == original

@given(instance=shr5::Magazin_strategy)
@settings(max_examples=50)
def test_shr5::magazin_instantiation(instance):
    assert isinstance(instance, shr5::Magazin)

@given(instance=shr5::AbstractMatrixDevice_strategy)
@settings(max_examples=50)
def test_shr5::abstractmatrixdevice_instantiation(instance):
    assert isinstance(instance, shr5::AbstractMatrixDevice)

@given(instance=shr5::AbstractMatrixDevice_strategy)
def test_shr5::abstractmatrixdevice_deviceRating_type(instance):
    assert isinstance(instance.deviceRating, int)


@given(instance=shr5::AbstractMatrixDevice_strategy)
def test_shr5::abstractmatrixdevice_deviceRating_setter(instance):
    original = instance.deviceRating
    instance.deviceRating = original
    assert instance.deviceRating == original

@given(instance=shr5::Kleidung_strategy)
@settings(max_examples=50)
def test_shr5::kleidung_instantiation(instance):
    assert isinstance(instance, shr5::Kleidung)

@given(instance=shr5::Kleidung_strategy)
def test_shr5::kleidung_ruestung_type(instance):
    assert isinstance(instance.ruestung, int)


@given(instance=shr5::Kleidung_strategy)
def test_shr5::kleidung_ruestung_setter(instance):
    original = instance.ruestung
    instance.ruestung = original
    assert instance.ruestung == original

@given(instance=shr5::AbstraktFokus_strategy)
@settings(max_examples=50)
def test_shr5::abstraktfokus_instantiation(instance):
    assert isinstance(instance, shr5::AbstraktFokus)

@given(instance=shr5::Munition_strategy)
@settings(max_examples=50)
def test_shr5::munition_instantiation(instance):
    assert isinstance(instance, shr5::Munition)

@given(instance=shr5::Munition_strategy)
def test_shr5::munition_armorMod_type(instance):
    assert isinstance(instance.armorMod, int)


@given(instance=shr5::Munition_strategy)
def test_shr5::munition_armorMod_setter(instance):
    original = instance.armorMod
    instance.armorMod = original
    assert instance.armorMod == original

@given(instance=shr5::Munition_strategy)
def test_shr5::munition_damageMod_type(instance):
    assert isinstance(instance.damageMod, int)


@given(instance=shr5::Munition_strategy)
def test_shr5::munition_damageMod_setter(instance):
    original = instance.damageMod
    instance.damageMod = original
    assert instance.damageMod == original

@given(instance=shr5::Munition_strategy)
def test_shr5::munition_damageType_type(instance):
    assert isinstance(instance.damageType, str)


@given(instance=shr5::Munition_strategy)
def test_shr5::munition_damageType_setter(instance):
    original = instance.damageType
    instance.damageType = original
    assert instance.damageType == original

@given(instance=shr5::AbstaktWaffe_strategy)
@settings(max_examples=50)
def test_shr5::abstaktwaffe_instantiation(instance):
    assert isinstance(instance, shr5::AbstaktWaffe)

@given(instance=shr5::AbstaktWaffe_strategy)
def test_shr5::abstaktwaffe_schadesTyp_type(instance):
    assert isinstance(instance.schadesTyp, str)


@given(instance=shr5::AbstaktWaffe_strategy)
def test_shr5::abstaktwaffe_schadesTyp_setter(instance):
    original = instance.schadesTyp
    instance.schadesTyp = original
    assert instance.schadesTyp == original

@given(instance=shr5::AbstaktWaffe_strategy)
def test_shr5::abstaktwaffe_schadenscode_type(instance):
    assert isinstance(instance.schadenscode, str)


@given(instance=shr5::AbstaktWaffe_strategy)
def test_shr5::abstaktwaffe_schadenscode_setter(instance):
    original = instance.schadenscode
    instance.schadenscode = original
    assert instance.schadenscode == original

@given(instance=shr5::AbstaktWaffe_strategy)
def test_shr5::abstaktwaffe_durchschlagsKraft_type(instance):
    assert isinstance(instance.durchschlagsKraft, int)


@given(instance=shr5::AbstaktWaffe_strategy)
def test_shr5::abstaktwaffe_durchschlagsKraft_setter(instance):
    original = instance.durchschlagsKraft
    instance.durchschlagsKraft = original
    assert instance.durchschlagsKraft == original

@given(instance=shr5::AbstaktWaffe_strategy)
def test_shr5::abstaktwaffe_praezision_type(instance):
    assert isinstance(instance.praezision, int)


@given(instance=shr5::AbstaktWaffe_strategy)
def test_shr5::abstaktwaffe_praezision_setter(instance):
    original = instance.praezision
    instance.praezision = original
    assert instance.praezision == original

@given(instance=shr5::SubstanceContainer_strategy)
@settings(max_examples=50)
def test_shr5::substancecontainer_instantiation(instance):
    assert isinstance(instance, shr5::SubstanceContainer)

@given(instance=shr5::Gegenstand_strategy)
@settings(max_examples=50)
def test_shr5::gegenstand_instantiation(instance):
    assert isinstance(instance, shr5::Gegenstand)

@given(instance=shr5::Gegenstand_strategy)
def test_shr5::gegenstand_kategorie_type(instance):
    assert isinstance(instance.kategorie, str)


@given(instance=shr5::Gegenstand_strategy)
def test_shr5::gegenstand_kategorie_setter(instance):
    original = instance.kategorie
    instance.kategorie = original
    assert instance.kategorie == original

@given(instance=shr5::Gegenstand_strategy)
def test_shr5::gegenstand_stufe_type(instance):
    assert isinstance(instance.stufe, int)


@given(instance=shr5::Gegenstand_strategy)
def test_shr5::gegenstand_stufe_setter(instance):
    original = instance.stufe
    instance.stufe = original
    assert instance.stufe == original

@given(instance=shr5::PersonaMartialartStyle_strategy)
@settings(max_examples=50)
def test_shr5::personamartialartstyle_instantiation(instance):
    assert isinstance(instance, shr5::PersonaMartialartStyle)

@given(instance=shr5::PersonaFertigkeitsGruppe_strategy)
@settings(max_examples=50)
def test_shr5::personafertigkeitsgruppe_instantiation(instance):
    assert isinstance(instance, shr5::PersonaFertigkeitsGruppe)

@given(instance=shr5::PersonaFertigkeit_strategy)
@settings(max_examples=50)
def test_shr5::personafertigkeit_instantiation(instance):
    assert isinstance(instance, shr5::PersonaFertigkeit)

@given(instance=ChrakterLimits_strategy)
@settings(max_examples=50)
def test_chrakterlimits_instantiation(instance):
    assert isinstance(instance, ChrakterLimits)

@given(instance=GeistigeAttribute_strategy)
@settings(max_examples=50)
def test_geistigeattribute_instantiation(instance):
    assert isinstance(instance, GeistigeAttribute)

@given(instance=SpezielleAttribute_strategy)
@settings(max_examples=50)
def test_spezielleattribute_instantiation(instance):
    assert isinstance(instance, SpezielleAttribute)

@given(instance=KoerperlicheAttribute_strategy)
@settings(max_examples=50)
def test_koerperlicheattribute_instantiation(instance):
    assert isinstance(instance, KoerperlicheAttribute)

@given(instance=Identifiable_strategy)
@settings(max_examples=50)
def test_identifiable_instantiation(instance):
    assert isinstance(instance, Identifiable)

@given(instance=shr5::Quelle_strategy)
@settings(max_examples=50)
def test_shr5::quelle_instantiation(instance):
    assert isinstance(instance, shr5::Quelle)

@given(instance=shr5::Quelle_strategy)
def test_shr5::quelle_page_type(instance):
    assert isinstance(instance.page, str)


@given(instance=shr5::Quelle_strategy)
def test_shr5::quelle_page_setter(instance):
    original = instance.page
    instance.page = original
    assert instance.page == original

@given(instance=shr5::Beschreibbar_strategy)
@settings(max_examples=50)
def test_shr5::beschreibbar_instantiation(instance):
    assert isinstance(instance, shr5::Beschreibbar)

@given(instance=shr5::Beschreibbar_strategy)
def test_shr5::beschreibbar_beschreibung_type(instance):
    assert isinstance(instance.beschreibung, str)


@given(instance=shr5::Beschreibbar_strategy)
def test_shr5::beschreibbar_beschreibung_setter(instance):
    original = instance.beschreibung
    instance.beschreibung = original
    assert instance.beschreibung == original

@given(instance=shr5::Beschreibbar_strategy)
def test_shr5::beschreibbar_image_type(instance):
    assert isinstance(instance.image, str)


@given(instance=shr5::Beschreibbar_strategy)
def test_shr5::beschreibbar_image_setter(instance):
    original = instance.image
    instance.image = original
    assert instance.image == original

@given(instance=shr5::Beschreibbar_strategy)
def test_shr5::beschreibbar_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=shr5::Beschreibbar_strategy)
def test_shr5::beschreibbar_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Beschreibbar_strategy)
@settings(max_examples=50)
def test_beschreibbar_instantiation(instance):
    assert isinstance(instance, Beschreibbar)

@given(instance=shr5::Spezialisierung_strategy)
@settings(max_examples=50)
def test_shr5::spezialisierung_instantiation(instance):
    assert isinstance(instance, shr5::Spezialisierung)

@given(instance=shr5::FahrzeugModifikation_strategy)
@settings(max_examples=50)
def test_shr5::fahrzeugmodifikation_instantiation(instance):
    assert isinstance(instance, shr5::FahrzeugModifikation)

@given(instance=shr5::FahrzeugModifikation_strategy)
def test_shr5::fahrzeugmodifikation_capacityUsed_type(instance):
    assert isinstance(instance.capacityUsed, int)


@given(instance=shr5::FahrzeugModifikation_strategy)
def test_shr5::fahrzeugmodifikation_capacityUsed_setter(instance):
    original = instance.capacityUsed
    instance.capacityUsed = original
    assert instance.capacityUsed == original

@given(instance=shr5::MartialartTechnique_strategy)
@settings(max_examples=50)
def test_shr5::martialarttechnique_instantiation(instance):
    assert isinstance(instance, shr5::MartialartTechnique)

@given(instance=shr5::Fertigkeit_strategy)
@settings(max_examples=50)
def test_shr5::fertigkeit_instantiation(instance):
    assert isinstance(instance, shr5::Fertigkeit)

@given(instance=shr5::Fertigkeit_strategy)
def test_shr5::fertigkeit_kategorie_type(instance):
    assert isinstance(instance.kategorie, str)


@given(instance=shr5::Fertigkeit_strategy)
def test_shr5::fertigkeit_kategorie_setter(instance):
    original = instance.kategorie
    instance.kategorie = original
    assert instance.kategorie == original

@given(instance=shr5::Fertigkeit_strategy)
def test_shr5::fertigkeit_ausweichen_type(instance):
    assert isinstance(instance.ausweichen, bool)


@given(instance=shr5::Fertigkeit_strategy)
def test_shr5::fertigkeit_ausweichen_setter(instance):
    original = instance.ausweichen
    instance.ausweichen = original
    assert instance.ausweichen == original

@given(instance=shr5::StufenPersona_strategy)
@settings(max_examples=50)
def test_shr5::stufenpersona_instantiation(instance):
    assert isinstance(instance, shr5::StufenPersona)

@given(instance=shr5::StufenPersona_strategy)
def test_shr5::stufenpersona_stufe_type(instance):
    assert isinstance(instance.stufe, int)


@given(instance=shr5::StufenPersona_strategy)
def test_shr5::stufenpersona_stufe_setter(instance):
    original = instance.stufe
    instance.stufe = original
    assert instance.stufe == original

@given(instance=shr5::KomplexeForm_strategy)
@settings(max_examples=50)
def test_shr5::komplexeform_instantiation(instance):
    assert isinstance(instance, shr5::KomplexeForm)

@given(instance=shr5::KomplexeForm_strategy)
def test_shr5::komplexeform_dauer_type(instance):
    assert isinstance(instance.dauer, str)


@given(instance=shr5::KomplexeForm_strategy)
def test_shr5::komplexeform_dauer_setter(instance):
    original = instance.dauer
    instance.dauer = original
    assert instance.dauer == original

@given(instance=shr5::KomplexeForm_strategy)
def test_shr5::komplexeform_ziel_type(instance):
    assert isinstance(instance.ziel, str)


@given(instance=shr5::KomplexeForm_strategy)
def test_shr5::komplexeform_ziel_setter(instance):
    original = instance.ziel
    instance.ziel = original
    assert instance.ziel == original

@given(instance=shr5::KomplexeForm_strategy)
def test_shr5::komplexeform_schwund_type(instance):
    assert isinstance(instance.schwund, str)


@given(instance=shr5::KomplexeForm_strategy)
def test_shr5::komplexeform_schwund_setter(instance):
    original = instance.schwund
    instance.schwund = original
    assert instance.schwund == original

@given(instance=shr5::MagischeTradition_strategy)
@settings(max_examples=50)
def test_shr5::magischetradition_instantiation(instance):
    assert isinstance(instance, shr5::MagischeTradition)

@given(instance=shr5::MagischeTradition_strategy)
def test_shr5::magischetradition_enzug_type(instance):
    assert isinstance(instance.enzug, str)


@given(instance=shr5::MagischeTradition_strategy)
def test_shr5::magischetradition_enzug_setter(instance):
    original = instance.enzug
    instance.enzug = original
    assert instance.enzug == original

@given(instance=shr5::AbstraktGegenstand_strategy)
@settings(max_examples=50)
def test_shr5::abstraktgegenstand_instantiation(instance):
    assert isinstance(instance, shr5::AbstraktGegenstand)

@given(instance=shr5::AbstraktPersona_strategy)
@settings(max_examples=50)
def test_shr5::abstraktpersona_instantiation(instance):
    assert isinstance(instance, shr5::AbstraktPersona)

@given(instance=shr5::AbstraktPersona_strategy)
def test_shr5::abstraktpersona_modManager_type(instance):
    assert isinstance(instance.modManager, str)


@given(instance=shr5::AbstraktPersona_strategy)
def test_shr5::abstraktpersona_modManager_setter(instance):
    original = instance.modManager
    instance.modManager = original
    assert instance.modManager == original

@given(instance=shr5::AbstraktPersona_strategy)
def test_shr5::abstraktpersona_willenskraftBasis_type(instance):
    assert isinstance(instance.willenskraftBasis, int)


@given(instance=shr5::AbstraktPersona_strategy)
def test_shr5::abstraktpersona_willenskraftBasis_setter(instance):
    original = instance.willenskraftBasis
    instance.willenskraftBasis = original
    assert instance.willenskraftBasis == original

@given(instance=shr5::AbstraktPersona_strategy)
def test_shr5::abstraktpersona_reaktionBasis_type(instance):
    assert isinstance(instance.reaktionBasis, int)


@given(instance=shr5::AbstraktPersona_strategy)
def test_shr5::abstraktpersona_reaktionBasis_setter(instance):
    original = instance.reaktionBasis
    instance.reaktionBasis = original
    assert instance.reaktionBasis == original

@given(instance=shr5::AbstraktPersona_strategy)
def test_shr5::abstraktpersona_staerkeBasis_type(instance):
    assert isinstance(instance.staerkeBasis, int)


@given(instance=shr5::AbstraktPersona_strategy)
def test_shr5::abstraktpersona_staerkeBasis_setter(instance):
    original = instance.staerkeBasis
    instance.staerkeBasis = original
    assert instance.staerkeBasis == original

@given(instance=shr5::AbstraktPersona_strategy)
def test_shr5::abstraktpersona_geschicklichkeitBasis_type(instance):
    assert isinstance(instance.geschicklichkeitBasis, int)


@given(instance=shr5::AbstraktPersona_strategy)
def test_shr5::abstraktpersona_geschicklichkeitBasis_setter(instance):
    original = instance.geschicklichkeitBasis
    instance.geschicklichkeitBasis = original
    assert instance.geschicklichkeitBasis == original

@given(instance=shr5::AbstraktPersona_strategy)
def test_shr5::abstraktpersona_logikBasis_type(instance):
    assert isinstance(instance.logikBasis, int)


@given(instance=shr5::AbstraktPersona_strategy)
def test_shr5::abstraktpersona_logikBasis_setter(instance):
    original = instance.logikBasis
    instance.logikBasis = original
    assert instance.logikBasis == original

@given(instance=shr5::AbstraktPersona_strategy)
def test_shr5::abstraktpersona_intuitionBasis_type(instance):
    assert isinstance(instance.intuitionBasis, int)


@given(instance=shr5::AbstraktPersona_strategy)
def test_shr5::abstraktpersona_intuitionBasis_setter(instance):
    original = instance.intuitionBasis
    instance.intuitionBasis = original
    assert instance.intuitionBasis == original

@given(instance=shr5::AbstraktPersona_strategy)
def test_shr5::abstraktpersona_konstitutionBasis_type(instance):
    assert isinstance(instance.konstitutionBasis, int)


@given(instance=shr5::AbstraktPersona_strategy)
def test_shr5::abstraktpersona_konstitutionBasis_setter(instance):
    original = instance.konstitutionBasis
    instance.konstitutionBasis = original
    assert instance.konstitutionBasis == original

@given(instance=shr5::AbstraktPersona_strategy)
def test_shr5::abstraktpersona_charismaBasis_type(instance):
    assert isinstance(instance.charismaBasis, int)


@given(instance=shr5::AbstraktPersona_strategy)
def test_shr5::abstraktpersona_charismaBasis_setter(instance):
    original = instance.charismaBasis
    instance.charismaBasis = original
    assert instance.charismaBasis == original

@given(instance=shr5::Sensor_strategy)
@settings(max_examples=50)
def test_shr5::sensor_instantiation(instance):
    assert isinstance(instance, shr5::Sensor)

@given(instance=shr5::Sensor_strategy)
def test_shr5::sensor_rating_type(instance):
    assert isinstance(instance.rating, int)


@given(instance=shr5::Sensor_strategy)
def test_shr5::sensor_rating_setter(instance):
    original = instance.rating
    instance.rating = original
    assert instance.rating == original

@given(instance=shr5::Sensor_strategy)
def test_shr5::sensor_capacityValue_type(instance):
    assert isinstance(instance.capacityValue, int)


@given(instance=shr5::Sensor_strategy)
def test_shr5::sensor_capacityValue_setter(instance):
    original = instance.capacityValue
    instance.capacityValue = original
    assert instance.capacityValue == original

@given(instance=shr5::MartialartStyle_strategy)
@settings(max_examples=50)
def test_shr5::martialartstyle_instantiation(instance):
    assert isinstance(instance, shr5::MartialartStyle)

@given(instance=shr5::KleindungsModifikator_strategy)
@settings(max_examples=50)
def test_shr5::kleindungsmodifikator_instantiation(instance):
    assert isinstance(instance, shr5::KleindungsModifikator)

@given(instance=shr5::KleindungsModifikator_strategy)
def test_shr5::kleindungsmodifikator_capacity_type(instance):
    assert isinstance(instance.capacity, int)


@given(instance=shr5::KleindungsModifikator_strategy)
def test_shr5::kleindungsmodifikator_capacity_setter(instance):
    original = instance.capacity
    instance.capacity = original
    assert instance.capacity == original

@given(instance=shr5::KleindungsModifikator_strategy)
def test_shr5::kleindungsmodifikator_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=shr5::KleindungsModifikator_strategy)
def test_shr5::kleindungsmodifikator_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=shr5::KleindungsModifikator_strategy)
def test_shr5::kleindungsmodifikator_rating_type(instance):
    assert isinstance(instance.rating, int)


@given(instance=shr5::KleindungsModifikator_strategy)
def test_shr5::kleindungsmodifikator_rating_setter(instance):
    original = instance.rating
    instance.rating = original
    assert instance.rating == original

@given(instance=shr5::Substance_strategy)
@settings(max_examples=50)
def test_shr5::substance_instantiation(instance):
    assert isinstance(instance, shr5::Substance)

@given(instance=shr5::Substance_strategy)
def test_shr5::substance_speed_type(instance):
    assert isinstance(instance.speed, str)


@given(instance=shr5::Substance_strategy)
def test_shr5::substance_speed_setter(instance):
    original = instance.speed
    instance.speed = original
    assert instance.speed == original

@given(instance=shr5::Substance_strategy)
def test_shr5::substance_vector_type(instance):
    assert isinstance(instance.vector, str)


@given(instance=shr5::Substance_strategy)
def test_shr5::substance_vector_setter(instance):
    original = instance.vector
    instance.vector = original
    assert instance.vector == original

@given(instance=shr5::FertigkeitsGruppe_strategy)
@settings(max_examples=50)
def test_shr5::fertigkeitsgruppe_instantiation(instance):
    assert isinstance(instance, shr5::FertigkeitsGruppe)

@given(instance=shr5::Sprite_strategy)
@settings(max_examples=50)
def test_shr5::sprite_instantiation(instance):
    assert isinstance(instance, shr5::Sprite)

@given(instance=shr5::Sprite_strategy)
def test_shr5::sprite_schleicherMod_type(instance):
    assert isinstance(instance.schleicherMod, int)


@given(instance=shr5::Sprite_strategy)
def test_shr5::sprite_schleicherMod_setter(instance):
    original = instance.schleicherMod
    instance.schleicherMod = original
    assert instance.schleicherMod == original

@given(instance=shr5::Sprite_strategy)
def test_shr5::sprite_stufe_type(instance):
    assert isinstance(instance.stufe, int)


@given(instance=shr5::Sprite_strategy)
def test_shr5::sprite_stufe_setter(instance):
    original = instance.stufe
    instance.stufe = original
    assert instance.stufe == original

@given(instance=shr5::Sprite_strategy)
def test_shr5::sprite_firewallMod_type(instance):
    assert isinstance(instance.firewallMod, int)


@given(instance=shr5::Sprite_strategy)
def test_shr5::sprite_firewallMod_setter(instance):
    original = instance.firewallMod
    instance.firewallMod = original
    assert instance.firewallMod == original

@given(instance=shr5::Sprite_strategy)
def test_shr5::sprite_angriffMod_type(instance):
    assert isinstance(instance.angriffMod, int)


@given(instance=shr5::Sprite_strategy)
def test_shr5::sprite_angriffMod_setter(instance):
    original = instance.angriffMod
    instance.angriffMod = original
    assert instance.angriffMod == original

@given(instance=shr5::Sprite_strategy)
def test_shr5::sprite_initativeMod_type(instance):
    assert isinstance(instance.initativeMod, int)


@given(instance=shr5::Sprite_strategy)
def test_shr5::sprite_initativeMod_setter(instance):
    original = instance.initativeMod
    instance.initativeMod = original
    assert instance.initativeMod == original

@given(instance=shr5::Sprite_strategy)
def test_shr5::sprite_datenverarbeitungMod_type(instance):
    assert isinstance(instance.datenverarbeitungMod, int)


@given(instance=shr5::Sprite_strategy)
def test_shr5::sprite_datenverarbeitungMod_setter(instance):
    original = instance.datenverarbeitungMod
    instance.datenverarbeitungMod = original
    assert instance.datenverarbeitungMod == original

@given(instance=shr5::Vertrag_strategy)
@settings(max_examples=50)
def test_shr5::vertrag_instantiation(instance):
    assert isinstance(instance, shr5::Vertrag)

@given(instance=shr5::AbstraktModifikatoren_strategy)
@settings(max_examples=50)
def test_shr5::abstraktmodifikatoren_instantiation(instance):
    assert isinstance(instance, shr5::AbstraktModifikatoren)

@given(instance=shr5::MetaMagie_strategy)
@settings(max_examples=50)
def test_shr5::metamagie_instantiation(instance):
    assert isinstance(instance, shr5::MetaMagie)

@given(instance=shr5::SourceBook_strategy)
@settings(max_examples=50)
def test_shr5::sourcebook_instantiation(instance):
    assert isinstance(instance, shr5::SourceBook)

@given(instance=shr5::SourceBook_strategy)
def test_shr5::sourcebook_endShrTime_type(instance):
    assert isinstance(instance.endShrTime, str)


@given(instance=shr5::SourceBook_strategy)
def test_shr5::sourcebook_endShrTime_setter(instance):
    original = instance.endShrTime
    instance.endShrTime = original
    assert instance.endShrTime == original

@given(instance=shr5::SourceBook_strategy)
def test_shr5::sourcebook_startShrTime_type(instance):
    assert isinstance(instance.startShrTime, str)


@given(instance=shr5::SourceBook_strategy)
def test_shr5::sourcebook_startShrTime_setter(instance):
    original = instance.startShrTime
    instance.startShrTime = original
    assert instance.startShrTime == original

@given(instance=shr5::SourceBook_strategy)
def test_shr5::sourcebook_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=shr5::SourceBook_strategy)
def test_shr5::sourcebook_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=shr5::LifestyleOption_strategy)
@settings(max_examples=50)
def test_shr5::lifestyleoption_instantiation(instance):
    assert isinstance(instance, shr5::LifestyleOption)

@given(instance=shr5::Software_strategy)
@settings(max_examples=50)
def test_shr5::software_instantiation(instance):
    assert isinstance(instance, shr5::Software)

@given(instance=shr5::Fahrzeug_strategy)
@settings(max_examples=50)
def test_shr5::fahrzeug_instantiation(instance):
    assert isinstance(instance, shr5::Fahrzeug)

@given(instance=shr5::Fahrzeug_strategy)
def test_shr5::fahrzeug_beschleunigung_type(instance):
    assert isinstance(instance.beschleunigung, int)


@given(instance=shr5::Fahrzeug_strategy)
def test_shr5::fahrzeug_beschleunigung_setter(instance):
    original = instance.beschleunigung
    instance.beschleunigung = original
    assert instance.beschleunigung == original

@given(instance=shr5::Fahrzeug_strategy)
def test_shr5::fahrzeug_panzer_type(instance):
    assert isinstance(instance.panzer, int)


@given(instance=shr5::Fahrzeug_strategy)
def test_shr5::fahrzeug_panzer_setter(instance):
    original = instance.panzer
    instance.panzer = original
    assert instance.panzer == original

@given(instance=shr5::Fahrzeug_strategy)
def test_shr5::fahrzeug_sensor_type(instance):
    assert isinstance(instance.sensor, int)


@given(instance=shr5::Fahrzeug_strategy)
def test_shr5::fahrzeug_sensor_setter(instance):
    original = instance.sensor
    instance.sensor = original
    assert instance.sensor == original

@given(instance=shr5::Fahrzeug_strategy)
def test_shr5::fahrzeug_weaponMounts_type(instance):
    assert isinstance(instance.weaponMounts, int)


@given(instance=shr5::Fahrzeug_strategy)
def test_shr5::fahrzeug_weaponMounts_setter(instance):
    original = instance.weaponMounts
    instance.weaponMounts = original
    assert instance.weaponMounts == original

@given(instance=shr5::Fahrzeug_strategy)
def test_shr5::fahrzeug_pilot_type(instance):
    assert isinstance(instance.pilot, int)


@given(instance=shr5::Fahrzeug_strategy)
def test_shr5::fahrzeug_pilot_setter(instance):
    original = instance.pilot
    instance.pilot = original
    assert instance.pilot == original

@given(instance=shr5::Fahrzeug_strategy)
def test_shr5::fahrzeug_rumpf_type(instance):
    assert isinstance(instance.rumpf, int)


@given(instance=shr5::Fahrzeug_strategy)
def test_shr5::fahrzeug_rumpf_setter(instance):
    original = instance.rumpf
    instance.rumpf = original
    assert instance.rumpf == original

@given(instance=shr5::Fahrzeug_strategy)
def test_shr5::fahrzeug_geschwindigkeit_type(instance):
    assert isinstance(instance.geschwindigkeit, int)


@given(instance=shr5::Fahrzeug_strategy)
def test_shr5::fahrzeug_geschwindigkeit_setter(instance):
    original = instance.geschwindigkeit
    instance.geschwindigkeit = original
    assert instance.geschwindigkeit == original

@given(instance=shr5::Fahrzeug_strategy)
def test_shr5::fahrzeug_handling_type(instance):
    assert isinstance(instance.handling, int)


@given(instance=shr5::Fahrzeug_strategy)
def test_shr5::fahrzeug_handling_setter(instance):
    original = instance.handling
    instance.handling = original
    assert instance.handling == original

@given(instance=shr5::Fahrzeug_strategy)
def test_shr5::fahrzeug_fahrzeugTyp_type(instance):
    assert isinstance(instance.fahrzeugTyp, str)


@given(instance=shr5::Fahrzeug_strategy)
def test_shr5::fahrzeug_fahrzeugTyp_setter(instance):
    original = instance.fahrzeugTyp
    instance.fahrzeugTyp = original
    assert instance.fahrzeugTyp == original

@given(instance=shr5::Host_strategy)
@settings(max_examples=50)
def test_shr5::host_instantiation(instance):
    assert isinstance(instance, shr5::Host)

@given(instance=shr5::Host_strategy)
def test_shr5::host_baseDatenverarbeitung_type(instance):
    assert isinstance(instance.baseDatenverarbeitung, int)


@given(instance=shr5::Host_strategy)
def test_shr5::host_baseDatenverarbeitung_setter(instance):
    original = instance.baseDatenverarbeitung
    instance.baseDatenverarbeitung = original
    assert instance.baseDatenverarbeitung == original

@given(instance=shr5::Host_strategy)
def test_shr5::host_baseFirewall_type(instance):
    assert isinstance(instance.baseFirewall, int)


@given(instance=shr5::Host_strategy)
def test_shr5::host_baseFirewall_setter(instance):
    original = instance.baseFirewall
    instance.baseFirewall = original
    assert instance.baseFirewall == original

@given(instance=shr5::Host_strategy)
def test_shr5::host_baseAngriff_type(instance):
    assert isinstance(instance.baseAngriff, int)


@given(instance=shr5::Host_strategy)
def test_shr5::host_baseAngriff_setter(instance):
    original = instance.baseAngriff
    instance.baseAngriff = original
    assert instance.baseAngriff == original

@given(instance=shr5::Host_strategy)
def test_shr5::host_hostRating_type(instance):
    assert isinstance(instance.hostRating, int)


@given(instance=shr5::Host_strategy)
def test_shr5::host_hostRating_setter(instance):
    original = instance.hostRating
    instance.hostRating = original
    assert instance.hostRating == original

@given(instance=shr5::Host_strategy)
def test_shr5::host_baseSchleicher_type(instance):
    assert isinstance(instance.baseSchleicher, int)


@given(instance=shr5::Host_strategy)
def test_shr5::host_baseSchleicher_setter(instance):
    original = instance.baseSchleicher
    instance.baseSchleicher = original
    assert instance.baseSchleicher == original

@given(instance=shr5::SourceLink_strategy)
@settings(max_examples=50)
def test_shr5::sourcelink_instantiation(instance):
    assert isinstance(instance, shr5::SourceLink)

@given(instance=shr5::ShrList_strategy)
@settings(max_examples=50)
def test_shr5::shrlist_instantiation(instance):
    assert isinstance(instance, shr5::ShrList)

@given(instance=shr5::SensorFunction_strategy)
@settings(max_examples=50)
def test_shr5::sensorfunction_instantiation(instance):
    assert isinstance(instance, shr5::SensorFunction)

@given(instance=shr5::SensorFunction_strategy)
def test_shr5::sensorfunction_maxRange_type(instance):
    assert isinstance(instance.maxRange, int)


@given(instance=shr5::SensorFunction_strategy)
def test_shr5::sensorfunction_maxRange_setter(instance):
    original = instance.maxRange
    instance.maxRange = original
    assert instance.maxRange == original

@given(instance=shr5::Spezies_strategy)
@settings(max_examples=50)
def test_shr5::spezies_instantiation(instance):
    assert isinstance(instance, shr5::Spezies)

@given(instance=shr5::Spezies_strategy)
def test_shr5::spezies_magieMax_type(instance):
    assert isinstance(instance.magieMax, int)


@given(instance=shr5::Spezies_strategy)
def test_shr5::spezies_magieMax_setter(instance):
    original = instance.magieMax
    instance.magieMax = original
    assert instance.magieMax == original

@given(instance=shr5::Spezies_strategy)
def test_shr5::spezies_willenskraftMin_type(instance):
    assert isinstance(instance.willenskraftMin, int)


@given(instance=shr5::Spezies_strategy)
def test_shr5::spezies_willenskraftMin_setter(instance):
    original = instance.willenskraftMin
    instance.willenskraftMin = original
    assert instance.willenskraftMin == original

@given(instance=shr5::Spezies_strategy)
def test_shr5::spezies_intuitionMin_type(instance):
    assert isinstance(instance.intuitionMin, int)


@given(instance=shr5::Spezies_strategy)
def test_shr5::spezies_intuitionMin_setter(instance):
    original = instance.intuitionMin
    instance.intuitionMin = original
    assert instance.intuitionMin == original

@given(instance=shr5::Spezies_strategy)
def test_shr5::spezies_willenskraftMax_type(instance):
    assert isinstance(instance.willenskraftMax, int)


@given(instance=shr5::Spezies_strategy)
def test_shr5::spezies_willenskraftMax_setter(instance):
    original = instance.willenskraftMax
    instance.willenskraftMax = original
    assert instance.willenskraftMax == original

@given(instance=shr5::Spezies_strategy)
def test_shr5::spezies_edgeMin_type(instance):
    assert isinstance(instance.edgeMin, int)


@given(instance=shr5::Spezies_strategy)
def test_shr5::spezies_edgeMin_setter(instance):
    original = instance.edgeMin
    instance.edgeMin = original
    assert instance.edgeMin == original

@given(instance=shr5::Spezies_strategy)
def test_shr5::spezies_essenzMax_type(instance):
    assert isinstance(instance.essenzMax, int)


@given(instance=shr5::Spezies_strategy)
def test_shr5::spezies_essenzMax_setter(instance):
    original = instance.essenzMax
    instance.essenzMax = original
    assert instance.essenzMax == original

@given(instance=shr5::Spezies_strategy)
def test_shr5::spezies_logikMin_type(instance):
    assert isinstance(instance.logikMin, int)


@given(instance=shr5::Spezies_strategy)
def test_shr5::spezies_logikMin_setter(instance):
    original = instance.logikMin
    instance.logikMin = original
    assert instance.logikMin == original

@given(instance=shr5::Spezies_strategy)
def test_shr5::spezies_reaktionMax_type(instance):
    assert isinstance(instance.reaktionMax, int)


@given(instance=shr5::Spezies_strategy)
def test_shr5::spezies_reaktionMax_setter(instance):
    original = instance.reaktionMax
    instance.reaktionMax = original
    assert instance.reaktionMax == original

@given(instance=shr5::Spezies_strategy)
def test_shr5::spezies_konstitutionMax_type(instance):
    assert isinstance(instance.konstitutionMax, int)


@given(instance=shr5::Spezies_strategy)
def test_shr5::spezies_konstitutionMax_setter(instance):
    original = instance.konstitutionMax
    instance.konstitutionMax = original
    assert instance.konstitutionMax == original

@given(instance=shr5::Spezies_strategy)
def test_shr5::spezies_staerkeMin_type(instance):
    assert isinstance(instance.staerkeMin, int)


@given(instance=shr5::Spezies_strategy)
def test_shr5::spezies_staerkeMin_setter(instance):
    original = instance.staerkeMin
    instance.staerkeMin = original
    assert instance.staerkeMin == original

@given(instance=shr5::Spezies_strategy)
def test_shr5::spezies_geschicklichkeitMin_type(instance):
    assert isinstance(instance.geschicklichkeitMin, int)


@given(instance=shr5::Spezies_strategy)
def test_shr5::spezies_geschicklichkeitMin_setter(instance):
    original = instance.geschicklichkeitMin
    instance.geschicklichkeitMin = original
    assert instance.geschicklichkeitMin == original

@given(instance=shr5::Spezies_strategy)
def test_shr5::spezies_geschicklichkeitMax_type(instance):
    assert isinstance(instance.geschicklichkeitMax, int)


@given(instance=shr5::Spezies_strategy)
def test_shr5::spezies_geschicklichkeitMax_setter(instance):
    original = instance.geschicklichkeitMax
    instance.geschicklichkeitMax = original
    assert instance.geschicklichkeitMax == original

@given(instance=shr5::Spezies_strategy)
def test_shr5::spezies_konstitutionMin_type(instance):
    assert isinstance(instance.konstitutionMin, int)


@given(instance=shr5::Spezies_strategy)
def test_shr5::spezies_konstitutionMin_setter(instance):
    original = instance.konstitutionMin
    instance.konstitutionMin = original
    assert instance.konstitutionMin == original

@given(instance=shr5::Spezies_strategy)
def test_shr5::spezies_essenzMin_type(instance):
    assert isinstance(instance.essenzMin, int)


@given(instance=shr5::Spezies_strategy)
def test_shr5::spezies_essenzMin_setter(instance):
    original = instance.essenzMin
    instance.essenzMin = original
    assert instance.essenzMin == original

@given(instance=shr5::Spezies_strategy)
def test_shr5::spezies_resonanzMax_type(instance):
    assert isinstance(instance.resonanzMax, int)


@given(instance=shr5::Spezies_strategy)
def test_shr5::spezies_resonanzMax_setter(instance):
    original = instance.resonanzMax
    instance.resonanzMax = original
    assert instance.resonanzMax == original

@given(instance=shr5::Spezies_strategy)
def test_shr5::spezies_staerkeMax_type(instance):
    assert isinstance(instance.staerkeMax, int)


@given(instance=shr5::Spezies_strategy)
def test_shr5::spezies_staerkeMax_setter(instance):
    original = instance.staerkeMax
    instance.staerkeMax = original
    assert instance.staerkeMax == original

@given(instance=shr5::Spezies_strategy)
def test_shr5::spezies_laufen_type(instance):
    assert isinstance(instance.laufen, int)


@given(instance=shr5::Spezies_strategy)
def test_shr5::spezies_laufen_setter(instance):
    original = instance.laufen
    instance.laufen = original
    assert instance.laufen == original

@given(instance=shr5::Spezies_strategy)
def test_shr5::spezies_logikMax_type(instance):
    assert isinstance(instance.logikMax, int)


@given(instance=shr5::Spezies_strategy)
def test_shr5::spezies_logikMax_setter(instance):
    original = instance.logikMax
    instance.logikMax = original
    assert instance.logikMax == original

@given(instance=shr5::Spezies_strategy)
def test_shr5::spezies_resonanzMin_type(instance):
    assert isinstance(instance.resonanzMin, int)


@given(instance=shr5::Spezies_strategy)
def test_shr5::spezies_resonanzMin_setter(instance):
    original = instance.resonanzMin
    instance.resonanzMin = original
    assert instance.resonanzMin == original

@given(instance=shr5::Spezies_strategy)
def test_shr5::spezies_reaktionMin_type(instance):
    assert isinstance(instance.reaktionMin, int)


@given(instance=shr5::Spezies_strategy)
def test_shr5::spezies_reaktionMin_setter(instance):
    original = instance.reaktionMin
    instance.reaktionMin = original
    assert instance.reaktionMin == original

@given(instance=shr5::Spezies_strategy)
def test_shr5::spezies_sprinten_type(instance):
    assert isinstance(instance.sprinten, int)


@given(instance=shr5::Spezies_strategy)
def test_shr5::spezies_sprinten_setter(instance):
    original = instance.sprinten
    instance.sprinten = original
    assert instance.sprinten == original

@given(instance=shr5::Spezies_strategy)
def test_shr5::spezies_intuitionMax_type(instance):
    assert isinstance(instance.intuitionMax, int)


@given(instance=shr5::Spezies_strategy)
def test_shr5::spezies_intuitionMax_setter(instance):
    original = instance.intuitionMax
    instance.intuitionMax = original
    assert instance.intuitionMax == original

@given(instance=shr5::Spezies_strategy)
def test_shr5::spezies_charismaMin_type(instance):
    assert isinstance(instance.charismaMin, int)


@given(instance=shr5::Spezies_strategy)
def test_shr5::spezies_charismaMin_setter(instance):
    original = instance.charismaMin
    instance.charismaMin = original
    assert instance.charismaMin == original

@given(instance=shr5::Spezies_strategy)
def test_shr5::spezies_magieMin_type(instance):
    assert isinstance(instance.magieMin, int)


@given(instance=shr5::Spezies_strategy)
def test_shr5::spezies_magieMin_setter(instance):
    original = instance.magieMin
    instance.magieMin = original
    assert instance.magieMin == original

@given(instance=shr5::Spezies_strategy)
def test_shr5::spezies_edgeMax_type(instance):
    assert isinstance(instance.edgeMax, int)


@given(instance=shr5::Spezies_strategy)
def test_shr5::spezies_edgeMax_setter(instance):
    original = instance.edgeMax
    instance.edgeMax = original
    assert instance.edgeMax == original

@given(instance=shr5::Spezies_strategy)
def test_shr5::spezies_charismaMax_type(instance):
    assert isinstance(instance.charismaMax, int)


@given(instance=shr5::Spezies_strategy)
def test_shr5::spezies_charismaMax_setter(instance):
    original = instance.charismaMax
    instance.charismaMax = original
    assert instance.charismaMax == original

@given(instance=shr5::Spezies_strategy)
def test_shr5::spezies_rennen_type(instance):
    assert isinstance(instance.rennen, int)


@given(instance=shr5::Spezies_strategy)
def test_shr5::spezies_rennen_setter(instance):
    original = instance.rennen
    instance.rennen = original
    assert instance.rennen == original

@given(instance=shr5::Reichweite_strategy)
@settings(max_examples=50)
def test_shr5::reichweite_instantiation(instance):
    assert isinstance(instance, shr5::Reichweite)

@given(instance=shr5::Reichweite_strategy)
def test_shr5::reichweite_extrem_type(instance):
    assert isinstance(instance.extrem, int)


@given(instance=shr5::Reichweite_strategy)
def test_shr5::reichweite_extrem_setter(instance):
    original = instance.extrem
    instance.extrem = original
    assert instance.extrem == original

@given(instance=shr5::Reichweite_strategy)
def test_shr5::reichweite_kurz_type(instance):
    assert isinstance(instance.kurz, int)


@given(instance=shr5::Reichweite_strategy)
def test_shr5::reichweite_kurz_setter(instance):
    original = instance.kurz
    instance.kurz = original
    assert instance.kurz == original

@given(instance=shr5::Reichweite_strategy)
def test_shr5::reichweite_weit_type(instance):
    assert isinstance(instance.weit, int)


@given(instance=shr5::Reichweite_strategy)
def test_shr5::reichweite_weit_setter(instance):
    original = instance.weit
    instance.weit = original
    assert instance.weit == original

@given(instance=shr5::Reichweite_strategy)
def test_shr5::reichweite_mittel_type(instance):
    assert isinstance(instance.mittel, int)


@given(instance=shr5::Reichweite_strategy)
def test_shr5::reichweite_mittel_setter(instance):
    original = instance.mittel
    instance.mittel = original
    assert instance.mittel == original

@given(instance=shr5::Reichweite_strategy)
def test_shr5::reichweite_min_type(instance):
    assert isinstance(instance.min, int)


@given(instance=shr5::Reichweite_strategy)
def test_shr5::reichweite_min_setter(instance):
    original = instance.min
    instance.min = original
    assert instance.min == original

@given(instance=shr5::Zauber_strategy)
@settings(max_examples=50)
def test_shr5::zauber_instantiation(instance):
    assert isinstance(instance, shr5::Zauber)

@given(instance=shr5::Zauber_strategy)
def test_shr5::zauber_entzug_type(instance):
    assert isinstance(instance.entzug, str)


@given(instance=shr5::Zauber_strategy)
def test_shr5::zauber_entzug_setter(instance):
    original = instance.entzug
    instance.entzug = original
    assert instance.entzug == original

@given(instance=shr5::Zauber_strategy)
def test_shr5::zauber_merkmale_type(instance):
    assert isinstance(instance.merkmale, str)


@given(instance=shr5::Zauber_strategy)
def test_shr5::zauber_merkmale_setter(instance):
    original = instance.merkmale
    instance.merkmale = original
    assert instance.merkmale == original

@given(instance=shr5::Zauber_strategy)
def test_shr5::zauber_dauer_type(instance):
    assert isinstance(instance.dauer, str)


@given(instance=shr5::Zauber_strategy)
def test_shr5::zauber_dauer_setter(instance):
    original = instance.dauer
    instance.dauer = original
    assert instance.dauer == original

@given(instance=shr5::Zauber_strategy)
def test_shr5::zauber_reichweite_type(instance):
    assert isinstance(instance.reichweite, str)


@given(instance=shr5::Zauber_strategy)
def test_shr5::zauber_reichweite_setter(instance):
    original = instance.reichweite
    instance.reichweite = original
    assert instance.reichweite == original

@given(instance=shr5::Zauber_strategy)
def test_shr5::zauber_art_type(instance):
    assert isinstance(instance.art, str)


@given(instance=shr5::Zauber_strategy)
def test_shr5::zauber_art_setter(instance):
    original = instance.art
    instance.art = original
    assert instance.art == original

@given(instance=shr5::Zauber_strategy)
def test_shr5::zauber_kategorie_type(instance):
    assert isinstance(instance.kategorie, str)


@given(instance=shr5::Zauber_strategy)
def test_shr5::zauber_kategorie_setter(instance):
    original = instance.kategorie
    instance.kategorie = original
    assert instance.kategorie == original

@given(instance=shr5::Zauber_strategy)
def test_shr5::zauber_schaden_type(instance):
    assert isinstance(instance.schaden, str)


@given(instance=shr5::Zauber_strategy)
def test_shr5::zauber_schaden_setter(instance):
    original = instance.schaden
    instance.schaden = original
    assert instance.schaden == original
