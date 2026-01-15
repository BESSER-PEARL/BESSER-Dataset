####################
# STRUCTURAL MODEL #
####################

from besser.BUML.metamodel.structural import (
    Class, Property, Method, Parameter,
    BinaryAssociation, Generalization, DomainModel,
    Enumeration, EnumerationLiteral, Multiplicity,
    StringType, IntegerType, FloatType, BooleanType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    AnyType, Constraint, AssociationClass, Metadata
)

# Enumerations
FeuerModus: Enumeration = Enumeration(
    name="FeuerModus",
    literals={
            EnumerationLiteral(name="EM"),
			EnumerationLiteral(name="HM"),
			EnumerationLiteral(name="SM"),
			EnumerationLiteral(name="AM")
    }
)

ZauberArt: Enumeration = Enumeration(
    name="ZauberArt",
    literals={
            EnumerationLiteral(name="Mana"),
			EnumerationLiteral(name="Physisch")
    }
)

ZauberReichweite: Enumeration = Enumeration(
    name="ZauberReichweite",
    literals={
            EnumerationLiteral(name="Blickfeld"),
			EnumerationLiteral(name="Begrenzt"),
			EnumerationLiteral(name="Selbst"),
			EnumerationLiteral(name="Beruehrung")
    }
)

ZauberDauer: Enumeration = Enumeration(
    name="ZauberDauer",
    literals={
            EnumerationLiteral(name="Sofort"),
			EnumerationLiteral(name="Aufrechterhalten"),
			EnumerationLiteral(name="Permanent")
    }
)

Koerperteil: Enumeration = Enumeration(
    name="Koerperteil",
    literals={
            EnumerationLiteral(name="Rumpf"),
			EnumerationLiteral(name="Kopf"),
			EnumerationLiteral(name="Arme"),
			EnumerationLiteral(name="Beine")
    }
)

MagazinTyp: Enumeration = Enumeration(
    name="MagazinTyp",
    literals={
            EnumerationLiteral(name="Streifen"),
			EnumerationLiteral(name="Clip"),
			EnumerationLiteral(name="Trommel"),
			EnumerationLiteral(name="Gurt")
    }
)

ModifikatorType: Enumeration = Enumeration(
    name="ModifikatorType",
    literals={
            EnumerationLiteral(name="Natural"),
			EnumerationLiteral(name="Cyber"),
			EnumerationLiteral(name="Bio")
    }
)

SmartgunType: Enumeration = Enumeration(
    name="SmartgunType",
    literals={
            EnumerationLiteral(name="SmartBrille"),
			EnumerationLiteral(name="SmartGun"),
			EnumerationLiteral(name="SmatgunII")
    }
)

SchadensTyp: Enumeration = Enumeration(
    name="SchadensTyp",
    literals={
            EnumerationLiteral(name="koerperlich"),
			EnumerationLiteral(name="geistig"),
			EnumerationLiteral(name="speziell")
    }
)

Tragbar: Enumeration = Enumeration(
    name="Tragbar",
    literals={
            EnumerationLiteral(name="einhaendig"),
			EnumerationLiteral(name="zweihaendig")
    }
)

# Classes
shadowrun_AbstaktFernKampfwaffe = Class(name="shadowrun::AbstaktFernKampfwaffe", is_abstract=True)
AbstaktWaffe = Class(name="AbstaktWaffe")
shadowrun_AbstaktPersona = Class(name="shadowrun::AbstaktPersona", is_abstract=True)
Essenz = Class(name="Essenz")
BodyIndex = Class(name="BodyIndex")
KoerperlicheAtribute = Class(name="KoerperlicheAtribute")
BerechneteAttribute = Class(name="BerechneteAttribute")
GeistigeAttribute = Class(name="GeistigeAttribute")
shadowrun_PersonaFertigkeit = Class(name="shadowrun::PersonaFertigkeit")
shadowrun_Cyberware = Class(name="shadowrun::Cyberware")
shadowrun_Reichweite = Class(name="shadowrun::Reichweite")
shadowrun_AbstaktGegenstand = Class(name="shadowrun::AbstaktGegenstand", is_abstract=True)
FK = Class(name="FK")
GeldWert = Class(name="GeldWert")
Beschreibbar = Class(name="Beschreibbar")
Legalitaet = Class(name="Legalitaet")
Bemerkbar = Class(name="Bemerkbar")
Quelle = Class(name="Quelle")
Modifizierbar = Class(name="Modifizierbar")
shadowrun_Spezies = Class(name="shadowrun::Spezies")
shadowrun_AbstaktWaffe = Class(name="shadowrun::AbstaktWaffe", is_abstract=True)
AbstaktGegenstand = Class(name="AbstaktGegenstand")
shadowrun_Fertigkeit = Class(name="shadowrun::Fertigkeit")
shadowrun_BioWare = Class(name="shadowrun::BioWare")
shadowrun_AbstraktKleidung = Class(name="shadowrun::AbstraktKleidung", is_abstract=True)
shadowrun_Konzentration = Class(name="shadowrun::Konzentration")
shadowrun_Spezialisierung = Class(name="shadowrun::Spezialisierung")
shadowrun_AbstrakRaumKoerper = Class(name="shadowrun::AbstrakRaumKoerper", is_abstract=True)
shadowrun_RaumKoordinate = Class(name="shadowrun::RaumKoordinate")
shadowrun_Feuerwaffe = Class(name="shadowrun::Feuerwaffe")
AbstaktFernKampfwaffe = Class(name="AbstaktFernKampfwaffe")
shadowrun_MunitionsBehealter = Class(name="shadowrun::MunitionsBehealter")
shadowrun_Gegenstand = Class(name="shadowrun::Gegenstand")
shadowrun_Kleidung = Class(name="shadowrun::Kleidung")
shadowrun_Persona = Class(name="shadowrun::Persona")
AbstaktPersona = Class(name="AbstaktPersona")
shadowrun_PersonaGruppe = Class(name="shadowrun::PersonaGruppe")
shadowrun_PersonaKoerper = Class(name="shadowrun::PersonaKoerper")
shadowrun_Placement = Class(name="shadowrun::Placement")
shadowrun_Projektilwaffe = Class(name="shadowrun::Projektilwaffe")
shadowrun_AbstrakteRuestung = Class(name="shadowrun::AbstrakteRuestung", is_abstract=True)
AbstraktKleidung = Class(name="AbstraktKleidung")
shadowrun_Ruestung = Class(name="shadowrun::Ruestung")
AbstrakteRuestung = Class(name="AbstrakteRuestung")
shadowrun_Script = Class(name="shadowrun::Script")
shadowrun_AbstraktModifikatoren = Class(name="shadowrun::AbstraktModifikatoren", is_abstract=True)
shadowrun_AbstraktNahkampfwaffe = Class(name="shadowrun::AbstraktNahkampfwaffe", is_abstract=True)
NahkampfReichweite = Class(name="NahkampfReichweite")
shadowrun_Behaelter = Class(name="shadowrun::Behaelter")
Gegenstand = Class(name="Gegenstand")
shadowrun_FK = Class(name="shadowrun::FK")
koerpermods = Class(name="koerpermods")
shadowrun_GeldWert = Class(name="shadowrun::GeldWert", is_abstract=True)
shadowrun_BasicList = Class(name="shadowrun::BasicList")
shadowrun_AttributModifikatorWert = Class(name="shadowrun::AttributModifikatorWert")
shadowrun_EAttribute = Class(name="shadowrun::EAttribute")
shadowrun_Modifizierbar = Class(name="shadowrun::Modifizierbar", is_abstract=True)
shadowrun_KiKraft = Class(name="shadowrun::KiKraft")
MagischeMods = Class(name="MagischeMods")
shadowrun_KiAdept = Class(name="shadowrun::KiAdept")
shadowrun_AbstraktFertigkeit = Class(name="shadowrun::AbstraktFertigkeit", is_abstract=True)
AbstraktFertigkeit = Class(name="AbstraktFertigkeit")
shadowrun_FertigkeitsGruppe = Class(name="shadowrun::FertigkeitsGruppe")
shadowrun_Wurfwaffe = Class(name="shadowrun::Wurfwaffe")
shadowrun_ModifikatorList = Class(name="shadowrun::ModifikatorList")
shadowrun_koerpermods = Class(name="shadowrun::koerpermods", is_abstract=True)
AbstraktModifikatoren = Class(name="AbstraktModifikatoren")
shadowrun_MagischeMods = Class(name="shadowrun::MagischeMods", is_abstract=True)
shadowrun_BaseMagischePersona = Class(name="shadowrun::BaseMagischePersona", is_abstract=True)
shadowrun_AbstractMagischePaersona = Class(name="shadowrun::AbstractMagischePaersona", is_abstract=True)
BaseMagischePersona = Class(name="BaseMagischePersona")
AbstractMagischePaersona = Class(name="AbstractMagischePaersona")
shadowrun_GengenstandListe = Class(name="shadowrun::GengenstandListe")
shadowrun_Beschreibbar = Class(name="shadowrun::Beschreibbar", is_abstract=True)
shadowrun_Reichweiten = Class(name="shadowrun::Reichweiten")
shadowrun_Legalitaet = Class(name="shadowrun::Legalitaet", is_abstract=True)
shadowrun_AbstractMagier = Class(name="shadowrun::AbstractMagier", is_abstract=True)
shadowrun_MagiePersona = Class(name="shadowrun::MagiePersona")
AbstractMagier = Class(name="AbstractMagier")
shadowrun_PersonaZauber = Class(name="shadowrun::PersonaZauber")
shadowrun_Zauber = Class(name="shadowrun::Zauber")
shadowrun_Sichtverhaeltnisse = Class(name="shadowrun::Sichtverhaeltnisse", is_abstract=True)
shadowrun_WarenListe = Class(name="shadowrun::WarenListe")
shadowrun_Quelle = Class(name="shadowrun::Quelle", is_abstract=True)
shadowrun_SourceBook = Class(name="shadowrun::SourceBook")
shadowrun_KoerperlicheAtribute = Class(name="shadowrun::KoerperlicheAtribute", is_abstract=True)
Schadenswiederstand = Class(name="Schadenswiederstand")
shadowrun_BerechneteAttribute = Class(name="shadowrun::BerechneteAttribute", is_abstract=True)
shadowrun_Nahkampfwaffe = Class(name="shadowrun::Nahkampfwaffe")
AbstraktNahkampfwaffe = Class(name="AbstraktNahkampfwaffe")
shadowrun_Bemerkbar = Class(name="shadowrun::Bemerkbar", is_abstract=True)
shadowrun_ShrList = Class(name="shadowrun::ShrList")
shadowrun_EObject = Class(name="shadowrun::EObject")
shadowrun_FernkampfwaffenModifikatoren = Class(name="shadowrun::FernkampfwaffenModifikatoren", is_abstract=True)
shadowrun_NahkampfReichweite = Class(name="shadowrun::NahkampfReichweite", is_abstract=True)
shadowrun_Shamane = Class(name="shadowrun::Shamane")
MagiePersona = Class(name="MagiePersona")
shadowrun_Totem = Class(name="shadowrun::Totem")
shadowrun_GeistigeAttribute = Class(name="shadowrun::GeistigeAttribute", is_abstract=True)
shadowrun_Essenz = Class(name="shadowrun::Essenz", is_abstract=True)
shadowrun_BodyIndex = Class(name="shadowrun::BodyIndex", is_abstract=True)
shadowrun_GegenstandStufen = Class(name="shadowrun::GegenstandStufen", is_abstract=True)
shadowrun_Schadenswiederstand = Class(name="shadowrun::Schadenswiederstand", is_abstract=True)
shadowrun_Granate = Class(name="shadowrun::Granate")
shadowrun_Munition = Class(name="shadowrun::Munition")

# shadowrun_AbstaktFernKampfwaffe class attributes and methods

# AbstaktWaffe class attributes and methods

# shadowrun_AbstaktPersona class attributes and methods
shadowrun_AbstaktPersona_KonsitutionBase: Property = Property(name="KonsitutionBase", type=IntegerType)
shadowrun_AbstaktPersona_StaerkeBase: Property = Property(name="StaerkeBase", type=IntegerType)
shadowrun_AbstaktPersona_SchnelligkeitBase: Property = Property(name="SchnelligkeitBase", type=IntegerType)
shadowrun_AbstaktPersona_InteligenzBase: Property = Property(name="InteligenzBase", type=IntegerType)
shadowrun_AbstaktPersona_CharismaBase: Property = Property(name="CharismaBase", type=IntegerType)
shadowrun_AbstaktPersona_WillenskraftBase: Property = Property(name="WillenskraftBase", type=IntegerType)
shadowrun_AbstaktPersona_ReaktionBase: Property = Property(name="ReaktionBase", type=IntegerType)
shadowrun_AbstaktPersona_ReaktionWBase: Property = Property(name="ReaktionWBase", type=IntegerType)
shadowrun_AbstaktPersona_KampfpoolBase: Property = Property(name="KampfpoolBase", type=IntegerType)
shadowrun_AbstaktPersona_EssenzBase: Property = Property(name="EssenzBase", type=IntegerType)
shadowrun_AbstaktPersona_eigenGewicht: Property = Property(name="eigenGewicht", type=IntegerType)
shadowrun_AbstaktPersona_modsetter: Property = Property(name="modsetter", type=StringType)
shadowrun_AbstaktPersona_m_getGesamtGewicht: Method = Method(name="getGesamtGewicht", parameters={}, type=IntegerType)
shadowrun_AbstaktPersona.attributes={shadowrun_AbstaktPersona_KonsitutionBase, shadowrun_AbstaktPersona_WillenskraftBase, shadowrun_AbstaktPersona_EssenzBase, shadowrun_AbstaktPersona_StaerkeBase, shadowrun_AbstaktPersona_CharismaBase, shadowrun_AbstaktPersona_ReaktionBase, shadowrun_AbstaktPersona_KampfpoolBase, shadowrun_AbstaktPersona_eigenGewicht, shadowrun_AbstaktPersona_modsetter, shadowrun_AbstaktPersona_SchnelligkeitBase, shadowrun_AbstaktPersona_InteligenzBase, shadowrun_AbstaktPersona_ReaktionWBase}
shadowrun_AbstaktPersona.methods={shadowrun_AbstaktPersona_m_getGesamtGewicht}

# Essenz class attributes and methods

# BodyIndex class attributes and methods

# KoerperlicheAtribute class attributes and methods

# BerechneteAttribute class attributes and methods

# GeistigeAttribute class attributes and methods

# shadowrun_PersonaFertigkeit class attributes and methods
shadowrun_PersonaFertigkeit_stufe: Property = Property(name="stufe", type=IntegerType)
shadowrun_PersonaFertigkeit.attributes={shadowrun_PersonaFertigkeit_stufe}

# shadowrun_Cyberware class attributes and methods

# shadowrun_Reichweite class attributes and methods
shadowrun_Reichweite_reichweiteExtrem: Property = Property(name="reichweiteExtrem", type=IntegerType)
shadowrun_Reichweite_reichweiteExtrem1: Property = Property(name="reichweiteExtrem1", type=IntegerType)
shadowrun_Reichweite_reichweiteKurz: Property = Property(name="reichweiteKurz", type=IntegerType)
shadowrun_Reichweite_reichweiteKurz1: Property = Property(name="reichweiteKurz1", type=IntegerType)
shadowrun_Reichweite_reichweiteMittel: Property = Property(name="reichweiteMittel", type=IntegerType)
shadowrun_Reichweite_reichweiteMittel1: Property = Property(name="reichweiteMittel1", type=IntegerType)
shadowrun_Reichweite_reichweiteWeit: Property = Property(name="reichweiteWeit", type=IntegerType)
shadowrun_Reichweite_reichweiteWeit1: Property = Property(name="reichweiteWeit1", type=IntegerType)
shadowrun_Reichweite.attributes={shadowrun_Reichweite_reichweiteKurz1, shadowrun_Reichweite_reichweiteExtrem1, shadowrun_Reichweite_reichweiteWeit, shadowrun_Reichweite_reichweiteMittel1, shadowrun_Reichweite_reichweiteMittel, shadowrun_Reichweite_reichweiteExtrem, shadowrun_Reichweite_reichweiteWeit1, shadowrun_Reichweite_reichweiteKurz}

# shadowrun_AbstaktGegenstand class attributes and methods
shadowrun_AbstaktGegenstand_tragbar: Property = Property(name="tragbar", type=StringType)
shadowrun_AbstaktGegenstand_gewicht: Property = Property(name="gewicht", type=FloatType)
shadowrun_AbstaktGegenstand_raumKapazitaet: Property = Property(name="raumKapazitaet", type=IntegerType)
shadowrun_AbstaktGegenstand_verbraucht: Property = Property(name="verbraucht", type=BooleanType)
shadowrun_AbstaktGegenstand_inBenutzung: Property = Property(name="inBenutzung", type=BooleanType)
shadowrun_AbstaktGegenstand_m_Benutze: Method = Method(name="Benutze", parameters={})
shadowrun_AbstaktGegenstand_m_ErzeugePersonaHandlung: Method = Method(name="ErzeugePersonaHandlung", parameters={})
shadowrun_AbstaktGegenstand.attributes={shadowrun_AbstaktGegenstand_tragbar, shadowrun_AbstaktGegenstand_gewicht, shadowrun_AbstaktGegenstand_raumKapazitaet, shadowrun_AbstaktGegenstand_inBenutzung, shadowrun_AbstaktGegenstand_verbraucht}
shadowrun_AbstaktGegenstand.methods={shadowrun_AbstaktGegenstand_m_Benutze, shadowrun_AbstaktGegenstand_m_ErzeugePersonaHandlung}

# FK class attributes and methods

# GeldWert class attributes and methods

# Beschreibbar class attributes and methods

# Legalitaet class attributes and methods

# Bemerkbar class attributes and methods

# Quelle class attributes and methods

# Modifizierbar class attributes and methods

# shadowrun_Spezies class attributes and methods
shadowrun_Spezies_KonsitutionMax: Property = Property(name="KonsitutionMax", type=IntegerType)
shadowrun_Spezies_StaerkeMax: Property = Property(name="StaerkeMax", type=IntegerType)
shadowrun_Spezies_SchnelligkeitMax: Property = Property(name="SchnelligkeitMax", type=IntegerType)
shadowrun_Spezies_InteligenzMax: Property = Property(name="InteligenzMax", type=IntegerType)
shadowrun_Spezies_CharismaMax: Property = Property(name="CharismaMax", type=IntegerType)
shadowrun_Spezies_WillenskraftMax: Property = Property(name="WillenskraftMax", type=IntegerType)
shadowrun_Spezies.attributes={shadowrun_Spezies_KonsitutionMax, shadowrun_Spezies_WillenskraftMax, shadowrun_Spezies_InteligenzMax, shadowrun_Spezies_SchnelligkeitMax, shadowrun_Spezies_CharismaMax, shadowrun_Spezies_StaerkeMax}

# shadowrun_AbstaktWaffe class attributes and methods
shadowrun_AbstaktWaffe_schadenscode: Property = Property(name="schadenscode", type=StringType)
shadowrun_AbstaktWaffe.attributes={shadowrun_AbstaktWaffe_schadenscode}

# AbstaktGegenstand class attributes and methods

# shadowrun_Fertigkeit class attributes and methods

# shadowrun_BioWare class attributes and methods

# shadowrun_AbstraktKleidung class attributes and methods
shadowrun_AbstraktKleidung_koeperTeil: Property = Property(name="koeperTeil", type=StringType)
shadowrun_AbstraktKleidung.attributes={shadowrun_AbstraktKleidung_koeperTeil}

# shadowrun_Konzentration class attributes and methods

# shadowrun_Spezialisierung class attributes and methods

# shadowrun_AbstrakRaumKoerper class attributes and methods
shadowrun_AbstrakRaumKoerper_m_ProcessWorldTick: Method = Method(name="ProcessWorldTick", parameters={})
shadowrun_AbstrakRaumKoerper.methods={shadowrun_AbstrakRaumKoerper_m_ProcessWorldTick}

# shadowrun_RaumKoordinate class attributes and methods

# shadowrun_Feuerwaffe class attributes and methods
shadowrun_Feuerwaffe_munitionstyp: Property = Property(name="munitionstyp", type=StringType)
shadowrun_Feuerwaffe_modie: Property = Property(name="modie", type=StringType)
shadowrun_Feuerwaffe_kapazitaet: Property = Property(name="kapazitaet", type=IntegerType)
shadowrun_Feuerwaffe.attributes={shadowrun_Feuerwaffe_modie, shadowrun_Feuerwaffe_munitionstyp, shadowrun_Feuerwaffe_kapazitaet}

# AbstaktFernKampfwaffe class attributes and methods

# shadowrun_MunitionsBehealter class attributes and methods

# shadowrun_Gegenstand class attributes and methods

# shadowrun_Kleidung class attributes and methods

# shadowrun_Persona class attributes and methods

# AbstaktPersona class attributes and methods

# shadowrun_PersonaGruppe class attributes and methods
shadowrun_PersonaGruppe_m_getPersonaByName: Method = Method(name="getPersonaByName", parameters={Parameter(name='ItemName')})
shadowrun_PersonaGruppe_m_getPersonaCount: Method = Method(name="getPersonaCount", parameters={}, type=IntegerType)
shadowrun_PersonaGruppe_m_getPersonas: Method = Method(name="getPersonas", parameters={Parameter(name='Index')})
shadowrun_PersonaGruppe.methods={shadowrun_PersonaGruppe_m_getPersonaByName, shadowrun_PersonaGruppe_m_getPersonaCount, shadowrun_PersonaGruppe_m_getPersonas}

# shadowrun_PersonaKoerper class attributes and methods
shadowrun_PersonaKoerper_gesamtZustand: Property = Property(name="gesamtZustand", type=IntegerType)
shadowrun_PersonaKoerper.attributes={shadowrun_PersonaKoerper_gesamtZustand}

# shadowrun_Placement class attributes and methods
shadowrun_Placement_m_getGruppeByName: Method = Method(name="getGruppeByName", parameters={Parameter(name='ItemName')})
shadowrun_Placement.methods={shadowrun_Placement_m_getGruppeByName}

# shadowrun_Projektilwaffe class attributes and methods

# shadowrun_AbstrakteRuestung class attributes and methods
shadowrun_AbstrakteRuestung_ruestungsSchutzBalistisch: Property = Property(name="ruestungsSchutzBalistisch", type=IntegerType)
shadowrun_AbstrakteRuestung_ruestungsSchutzStoss: Property = Property(name="ruestungsSchutzStoss", type=IntegerType)
shadowrun_AbstrakteRuestung.attributes={shadowrun_AbstrakteRuestung_ruestungsSchutzBalistisch, shadowrun_AbstrakteRuestung_ruestungsSchutzStoss}

# AbstraktKleidung class attributes and methods

# shadowrun_Ruestung class attributes and methods

# AbstrakteRuestung class attributes and methods

# shadowrun_Script class attributes and methods
shadowrun_Script_m_getPlacementByName: Method = Method(name="getPlacementByName", parameters={Parameter(name='ItemName')})
shadowrun_Script_m_getPlacementCount: Method = Method(name="getPlacementCount", parameters={}, type=IntegerType)
shadowrun_Script_m_getPlacements: Method = Method(name="getPlacements", parameters={Parameter(name='Index')})
shadowrun_Script.methods={shadowrun_Script_m_getPlacementCount, shadowrun_Script_m_getPlacements, shadowrun_Script_m_getPlacementByName}

# shadowrun_AbstraktModifikatoren class attributes and methods

# shadowrun_AbstraktNahkampfwaffe class attributes and methods

# NahkampfReichweite class attributes and methods

# shadowrun_Behaelter class attributes and methods
shadowrun_Behaelter_kapazitaet: Property = Property(name="kapazitaet", type=IntegerType)
shadowrun_Behaelter.attributes={shadowrun_Behaelter_kapazitaet}

# Gegenstand class attributes and methods

# shadowrun_FK class attributes and methods

# koerpermods class attributes and methods

# shadowrun_GeldWert class attributes and methods
shadowrun_GeldWert_wert: Property = Property(name="wert", type=StringType)
shadowrun_GeldWert_strassenIndex: Property = Property(name="strassenIndex", type=FloatType)
shadowrun_GeldWert_verfuegbarkeit: Property = Property(name="verfuegbarkeit", type=StringType)
shadowrun_GeldWert.attributes={shadowrun_GeldWert_wert, shadowrun_GeldWert_verfuegbarkeit, shadowrun_GeldWert_strassenIndex}

# shadowrun_BasicList class attributes and methods

# shadowrun_AttributModifikatorWert class attributes and methods
shadowrun_AttributModifikatorWert_wert: Property = Property(name="wert", type=IntegerType)
shadowrun_AttributModifikatorWert.attributes={shadowrun_AttributModifikatorWert_wert}

# shadowrun_EAttribute class attributes and methods

# shadowrun_Modifizierbar class attributes and methods

# shadowrun_KiKraft class attributes and methods

# MagischeMods class attributes and methods

# shadowrun_KiAdept class attributes and methods

# shadowrun_AbstraktFertigkeit class attributes and methods

# AbstraktFertigkeit class attributes and methods

# shadowrun_FertigkeitsGruppe class attributes and methods

# shadowrun_Wurfwaffe class attributes and methods

# shadowrun_ModifikatorList class attributes and methods
shadowrun_ModifikatorList_name: Property = Property(name="name", type=StringType)
shadowrun_ModifikatorList.attributes={shadowrun_ModifikatorList_name}

# shadowrun_koerpermods class attributes and methods

# AbstraktModifikatoren class attributes and methods

# shadowrun_MagischeMods class attributes and methods

# shadowrun_BaseMagischePersona class attributes and methods
shadowrun_BaseMagischePersona_magie: Property = Property(name="magie", type=IntegerType)
shadowrun_BaseMagischePersona.attributes={shadowrun_BaseMagischePersona_magie}

# shadowrun_AbstractMagischePaersona class attributes and methods
shadowrun_AbstractMagischePaersona_magieBase: Property = Property(name="magieBase", type=IntegerType)
shadowrun_AbstractMagischePaersona.attributes={shadowrun_AbstractMagischePaersona_magieBase}

# BaseMagischePersona class attributes and methods

# AbstractMagischePaersona class attributes and methods

# shadowrun_GengenstandListe class attributes and methods

# shadowrun_Beschreibbar class attributes and methods
shadowrun_Beschreibbar_name: Property = Property(name="name", type=StringType)
shadowrun_Beschreibbar_beschreibung: Property = Property(name="beschreibung", type=StringType)
shadowrun_Beschreibbar_image: Property = Property(name="image", type=StringType)
shadowrun_Beschreibbar.attributes={shadowrun_Beschreibbar_name, shadowrun_Beschreibbar_beschreibung, shadowrun_Beschreibbar_image}

# shadowrun_Reichweiten class attributes and methods

# shadowrun_Legalitaet class attributes and methods
shadowrun_Legalitaet_legalitaet: Property = Property(name="legalitaet", type=StringType)
shadowrun_Legalitaet.attributes={shadowrun_Legalitaet_legalitaet}

# shadowrun_AbstractMagier class attributes and methods
shadowrun_AbstractMagier_Astralpool: Property = Property(name="Astralpool", type=IntegerType)
shadowrun_AbstractMagier_MagiePool: Property = Property(name="MagiePool", type=IntegerType)
shadowrun_AbstractMagier_InitationsGrad: Property = Property(name="InitationsGrad", type=IntegerType)
shadowrun_AbstractMagier.attributes={shadowrun_AbstractMagier_Astralpool, shadowrun_AbstractMagier_MagiePool, shadowrun_AbstractMagier_InitationsGrad}

# shadowrun_MagiePersona class attributes and methods

# AbstractMagier class attributes and methods

# shadowrun_PersonaZauber class attributes and methods
shadowrun_PersonaZauber_stufe: Property = Property(name="stufe", type=IntegerType)
shadowrun_PersonaZauber.attributes={shadowrun_PersonaZauber_stufe}

# shadowrun_Zauber class attributes and methods
shadowrun_Zauber_art: Property = Property(name="art", type=StringType)
shadowrun_Zauber_reichweite: Property = Property(name="reichweite", type=StringType)
shadowrun_Zauber_Mindestwurf: Property = Property(name="Mindestwurf", type=StringType)
shadowrun_Zauber_Schaden: Property = Property(name="Schaden", type=StringType)
shadowrun_Zauber_Dauer: Property = Property(name="Dauer", type=StringType)
shadowrun_Zauber_Enzug: Property = Property(name="Enzug", type=StringType)
shadowrun_Zauber.attributes={shadowrun_Zauber_art, shadowrun_Zauber_Schaden, shadowrun_Zauber_Enzug, shadowrun_Zauber_reichweite, shadowrun_Zauber_Mindestwurf, shadowrun_Zauber_Dauer}

# shadowrun_Sichtverhaeltnisse class attributes and methods
shadowrun_Sichtverhaeltnisse_Restlichtverstaerkung: Property = Property(name="Restlichtverstaerkung", type=StringType)
shadowrun_Sichtverhaeltnisse_Infrarot: Property = Property(name="Infrarot", type=StringType)
shadowrun_Sichtverhaeltnisse_Ultrasound: Property = Property(name="Ultrasound", type=StringType)
shadowrun_Sichtverhaeltnisse.attributes={shadowrun_Sichtverhaeltnisse_Ultrasound, shadowrun_Sichtverhaeltnisse_Restlichtverstaerkung, shadowrun_Sichtverhaeltnisse_Infrarot}

# shadowrun_WarenListe class attributes and methods
shadowrun_WarenListe_listenWert: Property = Property(name="listenWert", type=StringType)
shadowrun_WarenListe_strassenWert: Property = Property(name="strassenWert", type=StringType)
shadowrun_WarenListe.attributes={shadowrun_WarenListe_strassenWert, shadowrun_WarenListe_listenWert}

# shadowrun_Quelle class attributes and methods
shadowrun_Quelle_page: Property = Property(name="page", type=StringType)
shadowrun_Quelle.attributes={shadowrun_Quelle_page}

# shadowrun_SourceBook class attributes and methods
shadowrun_SourceBook_startShrTime: Property = Property(name="startShrTime", type=StringType)
shadowrun_SourceBook_endShrTime: Property = Property(name="endShrTime", type=StringType)
shadowrun_SourceBook.attributes={shadowrun_SourceBook_endShrTime, shadowrun_SourceBook_startShrTime}

# shadowrun_KoerperlicheAtribute class attributes and methods
shadowrun_KoerperlicheAtribute_Konsitution: Property = Property(name="Konsitution", type=IntegerType)
shadowrun_KoerperlicheAtribute_Staerke: Property = Property(name="Staerke", type=IntegerType)
shadowrun_KoerperlicheAtribute_Schnelligkeit: Property = Property(name="Schnelligkeit", type=IntegerType)
shadowrun_KoerperlicheAtribute.attributes={shadowrun_KoerperlicheAtribute_Konsitution, shadowrun_KoerperlicheAtribute_Schnelligkeit, shadowrun_KoerperlicheAtribute_Staerke}

# Schadenswiederstand class attributes and methods

# shadowrun_BerechneteAttribute class attributes and methods
shadowrun_BerechneteAttribute_Reaktion: Property = Property(name="Reaktion", type=IntegerType)
shadowrun_BerechneteAttribute_ReaktionW: Property = Property(name="ReaktionW", type=IntegerType)
shadowrun_BerechneteAttribute_Kampfpool: Property = Property(name="Kampfpool", type=IntegerType)
shadowrun_BerechneteAttribute.attributes={shadowrun_BerechneteAttribute_Reaktion, shadowrun_BerechneteAttribute_ReaktionW, shadowrun_BerechneteAttribute_Kampfpool}

# shadowrun_Nahkampfwaffe class attributes and methods

# AbstraktNahkampfwaffe class attributes and methods

# shadowrun_Bemerkbar class attributes and methods
shadowrun_Bemerkbar_tarnstufe: Property = Property(name="tarnstufe", type=IntegerType)
shadowrun_Bemerkbar.attributes={shadowrun_Bemerkbar_tarnstufe}

# shadowrun_ShrList class attributes and methods

# shadowrun_EObject class attributes and methods

# shadowrun_FernkampfwaffenModifikatoren class attributes and methods
shadowrun_FernkampfwaffenModifikatoren_Rueckstoss: Property = Property(name="Rueckstoss", type=IntegerType)
shadowrun_FernkampfwaffenModifikatoren_lasterPointer: Property = Property(name="lasterPointer", type=BooleanType)
shadowrun_FernkampfwaffenModifikatoren_Schalldaempfer: Property = Property(name="Schalldaempfer", type=BooleanType)
shadowrun_FernkampfwaffenModifikatoren_Vergroesserung: Property = Property(name="Vergroesserung", type=IntegerType)
shadowrun_FernkampfwaffenModifikatoren_Smartgun: Property = Property(name="Smartgun", type=StringType)
shadowrun_FernkampfwaffenModifikatoren.attributes={shadowrun_FernkampfwaffenModifikatoren_lasterPointer, shadowrun_FernkampfwaffenModifikatoren_Vergroesserung, shadowrun_FernkampfwaffenModifikatoren_Schalldaempfer, shadowrun_FernkampfwaffenModifikatoren_Smartgun, shadowrun_FernkampfwaffenModifikatoren_Rueckstoss}

# shadowrun_NahkampfReichweite class attributes and methods
shadowrun_NahkampfReichweite_reichweite: Property = Property(name="reichweite", type=IntegerType)
shadowrun_NahkampfReichweite.attributes={shadowrun_NahkampfReichweite_reichweite}

# shadowrun_Shamane class attributes and methods

# MagiePersona class attributes and methods

# shadowrun_Totem class attributes and methods

# shadowrun_GeistigeAttribute class attributes and methods
shadowrun_GeistigeAttribute_Inteligenz: Property = Property(name="Inteligenz", type=IntegerType)
shadowrun_GeistigeAttribute_Charisma: Property = Property(name="Charisma", type=IntegerType)
shadowrun_GeistigeAttribute_Willenskraft: Property = Property(name="Willenskraft", type=IntegerType)
shadowrun_GeistigeAttribute.attributes={shadowrun_GeistigeAttribute_Charisma, shadowrun_GeistigeAttribute_Inteligenz, shadowrun_GeistigeAttribute_Willenskraft}

# shadowrun_Essenz class attributes and methods
shadowrun_Essenz_Essenz: Property = Property(name="Essenz", type=IntegerType)
shadowrun_Essenz.attributes={shadowrun_Essenz_Essenz}

# shadowrun_BodyIndex class attributes and methods
shadowrun_BodyIndex_bodyIndex: Property = Property(name="bodyIndex", type=IntegerType)
shadowrun_BodyIndex.attributes={shadowrun_BodyIndex_bodyIndex}

# shadowrun_GegenstandStufen class attributes and methods
shadowrun_GegenstandStufen_Computer: Property = Property(name="Computer", type=IntegerType)
shadowrun_GegenstandStufen_Elektronik: Property = Property(name="Elektronik", type=IntegerType)
shadowrun_GegenstandStufen_Tracing: Property = Property(name="Tracing", type=IntegerType)
shadowrun_GegenstandStufen_AntiTracing: Property = Property(name="AntiTracing", type=IntegerType)
shadowrun_GegenstandStufen_Protection: Property = Property(name="Protection", type=IntegerType)
shadowrun_GegenstandStufen_AntiProtection: Property = Property(name="AntiProtection", type=IntegerType)
shadowrun_GegenstandStufen.attributes={shadowrun_GegenstandStufen_Protection, shadowrun_GegenstandStufen_Elektronik, shadowrun_GegenstandStufen_AntiProtection, shadowrun_GegenstandStufen_Tracing, shadowrun_GegenstandStufen_AntiTracing, shadowrun_GegenstandStufen_Computer}

# shadowrun_Schadenswiederstand class attributes and methods
shadowrun_Schadenswiederstand_ruestungsSchutzStoss: Property = Property(name="ruestungsSchutzStoss", type=IntegerType)
shadowrun_Schadenswiederstand_ruestungsSchutzBalistisch: Property = Property(name="ruestungsSchutzBalistisch", type=IntegerType)
shadowrun_Schadenswiederstand.attributes={shadowrun_Schadenswiederstand_ruestungsSchutzBalistisch, shadowrun_Schadenswiederstand_ruestungsSchutzStoss}

# shadowrun_Granate class attributes and methods
shadowrun_Granate_type: Property = Property(name="type", type=StringType)
shadowrun_Granate_daempfung: Property = Property(name="daempfung", type=StringType)
shadowrun_Granate.attributes={shadowrun_Granate_daempfung, shadowrun_Granate_type}

# shadowrun_Munition class attributes and methods
shadowrun_Munition_power: Property = Property(name="power", type=IntegerType)
shadowrun_Munition_niveau: Property = Property(name="niveau", type=IntegerType)
shadowrun_Munition_schadensTyp: Property = Property(name="schadensTyp", type=StringType)
shadowrun_Munition.attributes={shadowrun_Munition_niveau, shadowrun_Munition_schadensTyp, shadowrun_Munition_power}

# Relationships
fertigkeiten1: BinaryAssociation = BinaryAssociation(
    name="fertigkeiten1",
    ends={
        Property(name="shadowrun_PersonaFertigkeit", type=shadowrun_AbstaktPersona, multiplicity=Multiplicity(1, 1)),
        Property(name="shadowrun_AbstaktPersona", type=shadowrun_PersonaFertigkeit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cyberware2: BinaryAssociation = BinaryAssociation(
    name="cyberware2",
    ends={
        Property(name="Cyberware", type=shadowrun_AbstaktPersona, multiplicity=Multiplicity(1, 1)),
        Property(name="persona", type=shadowrun_Cyberware, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reichweite0: BinaryAssociation = BinaryAssociation(
    name="reichweite0",
    ends={
        Property(name="shadowrun_Reichweite", type=shadowrun_AbstaktFernKampfwaffe, multiplicity=Multiplicity(1, 1)),
        Property(name="shadowrun_AbstaktFernKampfwaffe", type=shadowrun_Reichweite, multiplicity=Multiplicity(1, 1))
    }
)
inBenutzung15: BinaryAssociation = BinaryAssociation(
    name="inBenutzung15",
    ends={
        Property(name="shadowrun_AbstaktGegenstand17", type=shadowrun_AbstaktPersona, multiplicity=Multiplicity(1, 1)),
        Property(name="shadowrun_AbstaktPersona16", type=shadowrun_AbstaktGegenstand, multiplicity=Multiplicity(0, 9999))
    }
)
spezies18: BinaryAssociation = BinaryAssociation(
    name="spezies18",
    ends={
        Property(name="shadowrun_Spezies", type=shadowrun_AbstaktPersona, multiplicity=Multiplicity(1, 1)),
        Property(name="shadowrun_AbstaktPersona19", type=shadowrun_Spezies, multiplicity=Multiplicity(0, 1))
    }
)
fertigkeit20: BinaryAssociation = BinaryAssociation(
    name="fertigkeit20",
    ends={
        Property(name="shadowrun_Fertigkeit", type=shadowrun_AbstaktWaffe, multiplicity=Multiplicity(1, 1)),
        Property(name="shadowrun_AbstaktWaffe", type=shadowrun_Fertigkeit, multiplicity=Multiplicity(1, 1))
    }
)
bioware3: BinaryAssociation = BinaryAssociation(
    name="bioware3",
    ends={
        Property(name="BioWare", type=shadowrun_AbstaktPersona, multiplicity=Multiplicity(1, 1)),
        Property(name="persona4", type=shadowrun_BioWare, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
gegenstaende5: BinaryAssociation = BinaryAssociation(
    name="gegenstaende5",
    ends={
        Property(name="shadowrun_AbstaktGegenstand", type=shadowrun_AbstaktPersona, multiplicity=Multiplicity(1, 1)),
        Property(name="shadowrun_AbstaktPersona6", type=shadowrun_AbstaktGegenstand, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
linkeHand7: BinaryAssociation = BinaryAssociation(
    name="linkeHand7",
    ends={
        Property(name="shadowrun_AbstaktGegenstand9", type=shadowrun_AbstaktPersona, multiplicity=Multiplicity(1, 1)),
        Property(name="shadowrun_AbstaktPersona8", type=shadowrun_AbstaktGegenstand, multiplicity=Multiplicity(0, 1))
    }
)
rechteHand10: BinaryAssociation = BinaryAssociation(
    name="rechteHand10",
    ends={
        Property(name="shadowrun_AbstaktGegenstand12", type=shadowrun_AbstaktPersona, multiplicity=Multiplicity(1, 1)),
        Property(name="shadowrun_AbstaktPersona11", type=shadowrun_AbstaktGegenstand, multiplicity=Multiplicity(0, 1))
    }
)
kleidung13: BinaryAssociation = BinaryAssociation(
    name="kleidung13",
    ends={
        Property(name="shadowrun_AbstraktKleidung", type=shadowrun_AbstaktPersona, multiplicity=Multiplicity(1, 1)),
        Property(name="shadowrun_AbstaktPersona14", type=shadowrun_AbstraktKleidung, multiplicity=Multiplicity(0, 9999))
    }
)
konzentration21: BinaryAssociation = BinaryAssociation(
    name="konzentration21",
    ends={
        Property(name="shadowrun_Konzentration", type=shadowrun_AbstaktWaffe, multiplicity=Multiplicity(1, 1)),
        Property(name="shadowrun_AbstaktWaffe22", type=shadowrun_Konzentration, multiplicity=Multiplicity(1, 1))
    }
)
spezialisierung23: BinaryAssociation = BinaryAssociation(
    name="spezialisierung23",
    ends={
        Property(name="shadowrun_Spezialisierung", type=shadowrun_AbstaktWaffe, multiplicity=Multiplicity(1, 1)),
        Property(name="shadowrun_AbstaktWaffe24", type=shadowrun_Spezialisierung, multiplicity=Multiplicity(1, 1))
    }
)
position25: BinaryAssociation = BinaryAssociation(
    name="position25",
    ends={
        Property(name="shadowrun_RaumKoordinate", type=shadowrun_AbstrakRaumKoerper, multiplicity=Multiplicity(1, 1)),
        Property(name="shadowrun_AbstrakRaumKoerper", type=shadowrun_RaumKoordinate, multiplicity=Multiplicity(0, 1))
    }
)
gegenstaendeList26: BinaryAssociation = BinaryAssociation(
    name="gegenstaendeList26",
    ends={
        Property(name="shadowrun_Behaelter", type=shadowrun_AbstaktGegenstand, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="shadowrun_AbstaktGegenstand27", type=shadowrun_Behaelter, multiplicity=Multiplicity(1, 1))
    }
)
munitionReservior28: BinaryAssociation = BinaryAssociation(
    name="munitionReservior28",
    ends={
        Property(name="shadowrun_MunitionsBehealter", type=shadowrun_Feuerwaffe, multiplicity=Multiplicity(1, 1)),
        Property(name="shadowrun_Feuerwaffe", type=shadowrun_MunitionsBehealter, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
personaList29: BinaryAssociation = BinaryAssociation(
    name="personaList29",
    ends={
        Property(name="shadowrun_AbstaktPersona30", type=shadowrun_PersonaGruppe, multiplicity=Multiplicity(1, 1)),
        Property(name="shadowrun_PersonaGruppe", type=shadowrun_AbstaktPersona, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
gruppen31: BinaryAssociation = BinaryAssociation(
    name="gruppen31",
    ends={
        Property(name="shadowrun_PersonaGruppe32", type=shadowrun_Placement, multiplicity=Multiplicity(1, 1)),
        Property(name="shadowrun_Placement", type=shadowrun_PersonaGruppe, multiplicity=Multiplicity(0, 9999))
    }
)
persona38: BinaryAssociation = BinaryAssociation(
    name="persona38",
    ends={
        Property(name="AbstaktPersona", type=shadowrun_Cyberware, multiplicity=Multiplicity(1, 1)),
        Property(name="cyberware", type=shadowrun_AbstaktPersona, multiplicity=Multiplicity(0, 1))
    }
)
entries39: BinaryAssociation = BinaryAssociation(
    name="entries39",
    ends={
        Property(name="shadowrun_FK", type=shadowrun_BasicList, multiplicity=Multiplicity(1, 1)),
        Property(name="shadowrun_BasicList", type=shadowrun_FK, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attribut40: BinaryAssociation = BinaryAssociation(
    name="attribut40",
    ends={
        Property(name="shadowrun_EAttribute", type=shadowrun_AttributModifikatorWert, multiplicity=Multiplicity(1, 1)),
        Property(name="shadowrun_AttributModifikatorWert", type=shadowrun_EAttribute, multiplicity=Multiplicity(0, 1))
    }
)
modifiziertes41: BinaryAssociation = BinaryAssociation(
    name="modifiziertes41",
    ends={
        Property(name="Modifizierbar", type=shadowrun_AttributModifikatorWert, multiplicity=Multiplicity(1, 1)),
        Property(name="mods", type=shadowrun_Modifizierbar, multiplicity=Multiplicity(0, 1))
    }
)
persona42: BinaryAssociation = BinaryAssociation(
    name="persona42",
    ends={
        Property(name="KiAdept", type=shadowrun_KiKraft, multiplicity=Multiplicity(1, 1)),
        Property(name="kikraft", type=shadowrun_KiAdept, multiplicity=Multiplicity(0, 1))
    }
)
konzentrationen43: BinaryAssociation = BinaryAssociation(
    name="konzentrationen43",
    ends={
        Property(name="Konzentration", type=shadowrun_Fertigkeit, multiplicity=Multiplicity(1, 1)),
        Property(name="fertigkeit", type=shadowrun_Konzentration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
gruppe44: BinaryAssociation = BinaryAssociation(
    name="gruppe44",
    ends={
        Property(name="FertigkeitsGruppe", type=shadowrun_Fertigkeit, multiplicity=Multiplicity(1, 1)),
        Property(name="fertigkeiten", type=shadowrun_FertigkeitsGruppe, multiplicity=Multiplicity(0, 1))
    }
)
placementList33: BinaryAssociation = BinaryAssociation(
    name="placementList33",
    ends={
        Property(name="shadowrun_Placement34", type=shadowrun_Script, multiplicity=Multiplicity(1, 1)),
        Property(name="shadowrun_Script", type=shadowrun_Placement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
persona51: BinaryAssociation = BinaryAssociation(
    name="persona51",
    ends={
        Property(name="AbstaktPersona52", type=shadowrun_BioWare, multiplicity=Multiplicity(1, 1)),
        Property(name="bioware", type=shadowrun_AbstaktPersona, multiplicity=Multiplicity(0, 1))
    }
)
spielerGruppe35: BinaryAssociation = BinaryAssociation(
    name="spielerGruppe35",
    ends={
        Property(name="shadowrun_PersonaGruppe37", type=shadowrun_Script, multiplicity=Multiplicity(1, 1)),
        Property(name="shadowrun_Script36", type=shadowrun_PersonaGruppe, multiplicity=Multiplicity(0, 1))
    }
)
entries53: BinaryAssociation = BinaryAssociation(
    name="entries53",
    ends={
        Property(name="shadowrun_AbstraktModifikatoren", type=shadowrun_ModifikatorList, multiplicity=Multiplicity(1, 1)),
        Property(name="shadowrun_ModifikatorList", type=shadowrun_AbstraktModifikatoren, multiplicity=Multiplicity(0, 9999))
    }
)
kikraft54: BinaryAssociation = BinaryAssociation(
    name="kikraft54",
    ends={
        Property(name="KiKraft", type=shadowrun_KiAdept, multiplicity=Multiplicity(1, 1)),
        Property(name="persona55", type=shadowrun_KiKraft, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entries56: BinaryAssociation = BinaryAssociation(
    name="entries56",
    ends={
        Property(name="shadowrun_AbstaktGegenstand57", type=shadowrun_GengenstandListe, multiplicity=Multiplicity(1, 1)),
        Property(name="shadowrun_GengenstandListe", type=shadowrun_AbstaktGegenstand, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
spezialisierungen45: BinaryAssociation = BinaryAssociation(
    name="spezialisierungen45",
    ends={
        Property(name="Spezialisierung", type=shadowrun_Konzentration, multiplicity=Multiplicity(1, 1)),
        Property(name="konzentration", type=shadowrun_Spezialisierung, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fertigkeit46: BinaryAssociation = BinaryAssociation(
    name="fertigkeit46",
    ends={
        Property(name="Fertigkeit", type=shadowrun_Konzentration, multiplicity=Multiplicity(1, 1)),
        Property(name="konzentrationen", type=shadowrun_Fertigkeit, multiplicity=Multiplicity(0, 1))
    }
)
konzentration47: BinaryAssociation = BinaryAssociation(
    name="konzentration47",
    ends={
        Property(name="Konzentration48", type=shadowrun_Spezialisierung, multiplicity=Multiplicity(1, 1)),
        Property(name="spezialisierungen", type=shadowrun_Konzentration, multiplicity=Multiplicity(0, 1))
    }
)
fertigkeit49: BinaryAssociation = BinaryAssociation(
    name="fertigkeit49",
    ends={
        Property(name="shadowrun_AbstraktFertigkeit", type=shadowrun_PersonaFertigkeit, multiplicity=Multiplicity(1, 1)),
        Property(name="shadowrun_PersonaFertigkeit50", type=shadowrun_AbstraktFertigkeit, multiplicity=Multiplicity(1, 1))
    }
)
entries58: BinaryAssociation = BinaryAssociation(
    name="entries58",
    ends={
        Property(name="shadowrun_Reichweite59", type=shadowrun_Reichweiten, multiplicity=Multiplicity(1, 1)),
        Property(name="shadowrun_Reichweiten", type=shadowrun_Reichweite, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
zauber60: BinaryAssociation = BinaryAssociation(
    name="zauber60",
    ends={
        Property(name="shadowrun_PersonaZauber", type=shadowrun_MagiePersona, multiplicity=Multiplicity(1, 1)),
        Property(name="shadowrun_MagiePersona", type=shadowrun_PersonaZauber, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
zauber61: BinaryAssociation = BinaryAssociation(
    name="zauber61",
    ends={
        Property(name="shadowrun_Zauber", type=shadowrun_PersonaZauber, multiplicity=Multiplicity(1, 1)),
        Property(name="shadowrun_PersonaZauber62", type=shadowrun_Zauber, multiplicity=Multiplicity(1, 1))
    }
)
entries66: BinaryAssociation = BinaryAssociation(
    name="entries66",
    ends={
        Property(name="shadowrun_AbstaktGegenstand67", type=shadowrun_WarenListe, multiplicity=Multiplicity(1, 1)),
        Property(name="shadowrun_WarenListe", type=shadowrun_AbstaktGegenstand, multiplicity=Multiplicity(0, 9999))
    }
)
srcBook68: BinaryAssociation = BinaryAssociation(
    name="srcBook68",
    ends={
        Property(name="shadowrun_SourceBook", type=shadowrun_Quelle, multiplicity=Multiplicity(1, 1)),
        Property(name="shadowrun_Quelle", type=shadowrun_SourceBook, multiplicity=Multiplicity(0, 1))
    }
)
mods69: BinaryAssociation = BinaryAssociation(
    name="mods69",
    ends={
        Property(name="AttributModifikatorWert", type=shadowrun_Modifizierbar, multiplicity=Multiplicity(1, 1)),
        Property(name="modifiziertes", type=shadowrun_AttributModifikatorWert, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fertigkeiten63: BinaryAssociation = BinaryAssociation(
    name="fertigkeiten63",
    ends={
        Property(name="Fertigkeit64", type=shadowrun_FertigkeitsGruppe, multiplicity=Multiplicity(1, 1)),
        Property(name="gruppe", type=shadowrun_Fertigkeit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entries65: BinaryAssociation = BinaryAssociation(
    name="entries65",
    ends={
        Property(name="shadowrun_EObject", type=shadowrun_ShrList, multiplicity=Multiplicity(1, 1)),
        Property(name="shadowrun_ShrList", type=shadowrun_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
totem70: BinaryAssociation = BinaryAssociation(
    name="totem70",
    ends={
        Property(name="shadowrun_Totem", type=shadowrun_Shamane, multiplicity=Multiplicity(1, 1)),
        Property(name="shadowrun_Shamane", type=shadowrun_Totem, multiplicity=Multiplicity(0, 1))
    }
)
typ71: BinaryAssociation = BinaryAssociation(
    name="typ71",
    ends={
        Property(name="shadowrun_Reichweite72", type=shadowrun_Munition, multiplicity=Multiplicity(1, 1)),
        Property(name="shadowrun_Munition", type=shadowrun_Reichweite, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_shadowrun_AbstaktFernKampfwaffe_AbstaktWaffe = Generalization(general=AbstaktWaffe, specific=shadowrun_AbstaktFernKampfwaffe)
gen_shadowrun_AbstaktPersona_Beschreibbar = Generalization(general=Beschreibbar, specific=shadowrun_AbstaktPersona)
gen_shadowrun_AbstaktPersona_Essenz = Generalization(general=Essenz, specific=shadowrun_AbstaktPersona)
gen_shadowrun_AbstaktPersona_BodyIndex = Generalization(general=BodyIndex, specific=shadowrun_AbstaktPersona)
gen_shadowrun_AbstaktPersona_KoerperlicheAtribute = Generalization(general=KoerperlicheAtribute, specific=shadowrun_AbstaktPersona)
gen_shadowrun_AbstaktPersona_BerechneteAttribute = Generalization(general=BerechneteAttribute, specific=shadowrun_AbstaktPersona)
gen_shadowrun_AbstaktPersona_GeistigeAttribute = Generalization(general=GeistigeAttribute, specific=shadowrun_AbstaktPersona)
gen_shadowrun_AbstaktGegenstand_FK = Generalization(general=FK, specific=shadowrun_AbstaktGegenstand)
gen_shadowrun_AbstaktGegenstand_GeldWert = Generalization(general=GeldWert, specific=shadowrun_AbstaktGegenstand)
gen_shadowrun_AbstaktGegenstand_Beschreibbar = Generalization(general=Beschreibbar, specific=shadowrun_AbstaktGegenstand)
gen_shadowrun_AbstaktGegenstand_Legalitaet = Generalization(general=Legalitaet, specific=shadowrun_AbstaktGegenstand)
gen_shadowrun_AbstaktGegenstand_Bemerkbar = Generalization(general=Bemerkbar, specific=shadowrun_AbstaktGegenstand)
gen_shadowrun_AbstaktGegenstand_Quelle = Generalization(general=Quelle, specific=shadowrun_AbstaktGegenstand)
gen_shadowrun_AbstaktGegenstand_Modifizierbar = Generalization(general=Modifizierbar, specific=shadowrun_AbstaktGegenstand)
gen_shadowrun_AbstaktWaffe_AbstaktGegenstand = Generalization(general=AbstaktGegenstand, specific=shadowrun_AbstaktWaffe)
gen_shadowrun_Feuerwaffe_AbstaktFernKampfwaffe = Generalization(general=AbstaktFernKampfwaffe, specific=shadowrun_Feuerwaffe)
gen_shadowrun_Gegenstand_AbstaktGegenstand = Generalization(general=AbstaktGegenstand, specific=shadowrun_Gegenstand)
gen_shadowrun_Kleidung_AbstraktKleidung = Generalization(general=AbstraktKleidung, specific=shadowrun_Kleidung)
gen_shadowrun_MunitionsBehealter_Gegenstand = Generalization(general=Gegenstand, specific=shadowrun_MunitionsBehealter)
gen_shadowrun_Persona_AbstaktPersona = Generalization(general=AbstaktPersona, specific=shadowrun_Persona)
gen_shadowrun_PersonaGruppe_Beschreibbar = Generalization(general=Beschreibbar, specific=shadowrun_PersonaGruppe)
gen_shadowrun_Placement_Beschreibbar = Generalization(general=Beschreibbar, specific=shadowrun_Placement)
gen_shadowrun_Projektilwaffe_AbstaktFernKampfwaffe = Generalization(general=AbstaktFernKampfwaffe, specific=shadowrun_Projektilwaffe)
gen_shadowrun_AbstrakteRuestung_AbstraktKleidung = Generalization(general=AbstraktKleidung, specific=shadowrun_AbstrakteRuestung)
gen_shadowrun_Ruestung_AbstrakteRuestung = Generalization(general=AbstrakteRuestung, specific=shadowrun_Ruestung)
gen_shadowrun_Script_Beschreibbar = Generalization(general=Beschreibbar, specific=shadowrun_Script)
gen_shadowrun_AbstraktKleidung_AbstaktGegenstand = Generalization(general=AbstaktGegenstand, specific=shadowrun_AbstraktKleidung)
gen_shadowrun_AbstraktModifikatoren_Beschreibbar = Generalization(general=Beschreibbar, specific=shadowrun_AbstraktModifikatoren)
gen_shadowrun_AbstraktModifikatoren_Modifizierbar = Generalization(general=Modifizierbar, specific=shadowrun_AbstraktModifikatoren)
gen_shadowrun_AbstraktModifikatoren_Quelle = Generalization(general=Quelle, specific=shadowrun_AbstraktModifikatoren)
gen_shadowrun_AbstraktNahkampfwaffe_AbstaktWaffe = Generalization(general=AbstaktWaffe, specific=shadowrun_AbstraktNahkampfwaffe)
gen_shadowrun_AbstraktNahkampfwaffe_NahkampfReichweite = Generalization(general=NahkampfReichweite, specific=shadowrun_AbstraktNahkampfwaffe)
gen_shadowrun_Behaelter_Gegenstand = Generalization(general=Gegenstand, specific=shadowrun_Behaelter)
gen_shadowrun_Cyberware_GeldWert = Generalization(general=GeldWert, specific=shadowrun_Cyberware)
gen_shadowrun_Cyberware_koerpermods = Generalization(general=koerpermods, specific=shadowrun_Cyberware)
gen_shadowrun_KiKraft_MagischeMods = Generalization(general=MagischeMods, specific=shadowrun_KiKraft)
gen_shadowrun_AbstraktFertigkeit_FK = Generalization(general=FK, specific=shadowrun_AbstraktFertigkeit)
gen_shadowrun_AbstraktFertigkeit_Beschreibbar = Generalization(general=Beschreibbar, specific=shadowrun_AbstraktFertigkeit)
gen_shadowrun_Fertigkeit_AbstraktFertigkeit = Generalization(general=AbstraktFertigkeit, specific=shadowrun_Fertigkeit)
gen_shadowrun_BioWare_GeldWert = Generalization(general=GeldWert, specific=shadowrun_BioWare)
gen_shadowrun_BioWare_koerpermods = Generalization(general=koerpermods, specific=shadowrun_BioWare)
gen_shadowrun_Wurfwaffe_AbstaktFernKampfwaffe = Generalization(general=AbstaktFernKampfwaffe, specific=shadowrun_Wurfwaffe)
gen_shadowrun_koerpermods_AbstraktModifikatoren = Generalization(general=AbstraktModifikatoren, specific=shadowrun_koerpermods)
gen_shadowrun_MagischeMods_AbstraktModifikatoren = Generalization(general=AbstraktModifikatoren, specific=shadowrun_MagischeMods)
gen_shadowrun_AbstractMagischePaersona_AbstaktPersona = Generalization(general=AbstaktPersona, specific=shadowrun_AbstractMagischePaersona)
gen_shadowrun_AbstractMagischePaersona_BaseMagischePersona = Generalization(general=BaseMagischePersona, specific=shadowrun_AbstractMagischePaersona)
gen_shadowrun_KiAdept_AbstractMagischePaersona = Generalization(general=AbstractMagischePaersona, specific=shadowrun_KiAdept)
gen_shadowrun_Konzentration_AbstraktFertigkeit = Generalization(general=AbstraktFertigkeit, specific=shadowrun_Konzentration)
gen_shadowrun_Spezialisierung_AbstraktFertigkeit = Generalization(general=AbstraktFertigkeit, specific=shadowrun_Spezialisierung)
gen_shadowrun_AbstractMagier_BaseMagischePersona = Generalization(general=BaseMagischePersona, specific=shadowrun_AbstractMagier)
gen_shadowrun_MagiePersona_AbstractMagischePaersona = Generalization(general=AbstractMagischePaersona, specific=shadowrun_MagiePersona)
gen_shadowrun_MagiePersona_AbstractMagier = Generalization(general=AbstractMagier, specific=shadowrun_MagiePersona)
gen_shadowrun_Zauber_Beschreibbar = Generalization(general=Beschreibbar, specific=shadowrun_Zauber)
gen_shadowrun_FertigkeitsGruppe_Beschreibbar = Generalization(general=Beschreibbar, specific=shadowrun_FertigkeitsGruppe)
gen_shadowrun_FertigkeitsGruppe_FK = Generalization(general=FK, specific=shadowrun_FertigkeitsGruppe)
gen_shadowrun_Reichweite_Beschreibbar = Generalization(general=Beschreibbar, specific=shadowrun_Reichweite)
gen_shadowrun_KoerperlicheAtribute_Schadenswiederstand = Generalization(general=Schadenswiederstand, specific=shadowrun_KoerperlicheAtribute)
gen_shadowrun_Nahkampfwaffe_AbstraktNahkampfwaffe = Generalization(general=AbstraktNahkampfwaffe, specific=shadowrun_Nahkampfwaffe)
gen_shadowrun_ShrList_Beschreibbar = Generalization(general=Beschreibbar, specific=shadowrun_ShrList)
gen_shadowrun_Spezies_Beschreibbar = Generalization(general=Beschreibbar, specific=shadowrun_Spezies)
gen_shadowrun_Spezies_Modifizierbar = Generalization(general=Modifizierbar, specific=shadowrun_Spezies)
gen_shadowrun_SourceBook_Beschreibbar = Generalization(general=Beschreibbar, specific=shadowrun_SourceBook)
gen_shadowrun_Shamane_MagiePersona = Generalization(general=MagiePersona, specific=shadowrun_Shamane)
gen_shadowrun_Totem_Beschreibbar = Generalization(general=Beschreibbar, specific=shadowrun_Totem)
gen_shadowrun_Granate_AbstaktWaffe = Generalization(general=AbstaktWaffe, specific=shadowrun_Granate)
gen_shadowrun_Munition_AbstaktGegenstand = Generalization(general=AbstaktGegenstand, specific=shadowrun_Munition)

# Domain Model
domain_model = DomainModel(
    name="shadowrun",
    types={shadowrun_AbstaktFernKampfwaffe, AbstaktWaffe, shadowrun_AbstaktPersona, Essenz, BodyIndex, KoerperlicheAtribute, BerechneteAttribute, GeistigeAttribute, shadowrun_PersonaFertigkeit, shadowrun_Cyberware, shadowrun_Reichweite, shadowrun_AbstaktGegenstand, FK, GeldWert, Beschreibbar, Legalitaet, Bemerkbar, Quelle, Modifizierbar, shadowrun_Spezies, shadowrun_AbstaktWaffe, AbstaktGegenstand, shadowrun_Fertigkeit, shadowrun_BioWare, shadowrun_AbstraktKleidung, shadowrun_Konzentration, shadowrun_Spezialisierung, shadowrun_AbstrakRaumKoerper, shadowrun_RaumKoordinate, shadowrun_Feuerwaffe, AbstaktFernKampfwaffe, shadowrun_MunitionsBehealter, shadowrun_Gegenstand, shadowrun_Kleidung, shadowrun_Persona, AbstaktPersona, shadowrun_PersonaGruppe, shadowrun_PersonaKoerper, shadowrun_Placement, shadowrun_Projektilwaffe, shadowrun_AbstrakteRuestung, AbstraktKleidung, shadowrun_Ruestung, AbstrakteRuestung, shadowrun_Script, shadowrun_AbstraktModifikatoren, shadowrun_AbstraktNahkampfwaffe, NahkampfReichweite, shadowrun_Behaelter, Gegenstand, shadowrun_FK, koerpermods, shadowrun_GeldWert, shadowrun_BasicList, shadowrun_AttributModifikatorWert, shadowrun_EAttribute, shadowrun_Modifizierbar, shadowrun_KiKraft, MagischeMods, shadowrun_KiAdept, shadowrun_AbstraktFertigkeit, AbstraktFertigkeit, shadowrun_FertigkeitsGruppe, shadowrun_Wurfwaffe, shadowrun_ModifikatorList, shadowrun_koerpermods, AbstraktModifikatoren, shadowrun_MagischeMods, shadowrun_BaseMagischePersona, shadowrun_AbstractMagischePaersona, BaseMagischePersona, AbstractMagischePaersona, shadowrun_GengenstandListe, shadowrun_Beschreibbar, shadowrun_Reichweiten, shadowrun_Legalitaet, shadowrun_AbstractMagier, shadowrun_MagiePersona, AbstractMagier, shadowrun_PersonaZauber, shadowrun_Zauber, shadowrun_Sichtverhaeltnisse, shadowrun_WarenListe, shadowrun_Quelle, shadowrun_SourceBook, shadowrun_KoerperlicheAtribute, Schadenswiederstand, shadowrun_BerechneteAttribute, shadowrun_Nahkampfwaffe, AbstraktNahkampfwaffe, shadowrun_Bemerkbar, shadowrun_ShrList, shadowrun_EObject, shadowrun_FernkampfwaffenModifikatoren, shadowrun_NahkampfReichweite, shadowrun_Shamane, MagiePersona, shadowrun_Totem, shadowrun_GeistigeAttribute, shadowrun_Essenz, shadowrun_BodyIndex, shadowrun_GegenstandStufen, shadowrun_Schadenswiederstand, shadowrun_Granate, shadowrun_Munition, FeuerModus, ZauberArt, ZauberReichweite, ZauberDauer, Koerperteil, MagazinTyp, ModifikatorType, SmartgunType, SchadensTyp, Tragbar},
    associations={fertigkeiten1, cyberware2, reichweite0, inBenutzung15, spezies18, fertigkeit20, bioware3, gegenstaende5, linkeHand7, rechteHand10, kleidung13, konzentration21, spezialisierung23, position25, gegenstaendeList26, munitionReservior28, personaList29, gruppen31, persona38, entries39, attribut40, modifiziertes41, persona42, konzentrationen43, gruppe44, placementList33, persona51, spielerGruppe35, entries53, kikraft54, entries56, spezialisierungen45, fertigkeit46, konzentration47, fertigkeit49, entries58, zauber60, zauber61, entries66, srcBook68, mods69, fertigkeiten63, entries65, totem70, typ71},
    generalizations={gen_shadowrun_AbstaktFernKampfwaffe_AbstaktWaffe, gen_shadowrun_AbstaktPersona_Beschreibbar, gen_shadowrun_AbstaktPersona_Essenz, gen_shadowrun_AbstaktPersona_BodyIndex, gen_shadowrun_AbstaktPersona_KoerperlicheAtribute, gen_shadowrun_AbstaktPersona_BerechneteAttribute, gen_shadowrun_AbstaktPersona_GeistigeAttribute, gen_shadowrun_AbstaktGegenstand_FK, gen_shadowrun_AbstaktGegenstand_GeldWert, gen_shadowrun_AbstaktGegenstand_Beschreibbar, gen_shadowrun_AbstaktGegenstand_Legalitaet, gen_shadowrun_AbstaktGegenstand_Bemerkbar, gen_shadowrun_AbstaktGegenstand_Quelle, gen_shadowrun_AbstaktGegenstand_Modifizierbar, gen_shadowrun_AbstaktWaffe_AbstaktGegenstand, gen_shadowrun_Feuerwaffe_AbstaktFernKampfwaffe, gen_shadowrun_Gegenstand_AbstaktGegenstand, gen_shadowrun_Kleidung_AbstraktKleidung, gen_shadowrun_MunitionsBehealter_Gegenstand, gen_shadowrun_Persona_AbstaktPersona, gen_shadowrun_PersonaGruppe_Beschreibbar, gen_shadowrun_Placement_Beschreibbar, gen_shadowrun_Projektilwaffe_AbstaktFernKampfwaffe, gen_shadowrun_AbstrakteRuestung_AbstraktKleidung, gen_shadowrun_Ruestung_AbstrakteRuestung, gen_shadowrun_Script_Beschreibbar, gen_shadowrun_AbstraktKleidung_AbstaktGegenstand, gen_shadowrun_AbstraktModifikatoren_Beschreibbar, gen_shadowrun_AbstraktModifikatoren_Modifizierbar, gen_shadowrun_AbstraktModifikatoren_Quelle, gen_shadowrun_AbstraktNahkampfwaffe_AbstaktWaffe, gen_shadowrun_AbstraktNahkampfwaffe_NahkampfReichweite, gen_shadowrun_Behaelter_Gegenstand, gen_shadowrun_Cyberware_GeldWert, gen_shadowrun_Cyberware_koerpermods, gen_shadowrun_KiKraft_MagischeMods, gen_shadowrun_AbstraktFertigkeit_FK, gen_shadowrun_AbstraktFertigkeit_Beschreibbar, gen_shadowrun_Fertigkeit_AbstraktFertigkeit, gen_shadowrun_BioWare_GeldWert, gen_shadowrun_BioWare_koerpermods, gen_shadowrun_Wurfwaffe_AbstaktFernKampfwaffe, gen_shadowrun_koerpermods_AbstraktModifikatoren, gen_shadowrun_MagischeMods_AbstraktModifikatoren, gen_shadowrun_AbstractMagischePaersona_AbstaktPersona, gen_shadowrun_AbstractMagischePaersona_BaseMagischePersona, gen_shadowrun_KiAdept_AbstractMagischePaersona, gen_shadowrun_Konzentration_AbstraktFertigkeit, gen_shadowrun_Spezialisierung_AbstraktFertigkeit, gen_shadowrun_AbstractMagier_BaseMagischePersona, gen_shadowrun_MagiePersona_AbstractMagischePaersona, gen_shadowrun_MagiePersona_AbstractMagier, gen_shadowrun_Zauber_Beschreibbar, gen_shadowrun_FertigkeitsGruppe_Beschreibbar, gen_shadowrun_FertigkeitsGruppe_FK, gen_shadowrun_Reichweite_Beschreibbar, gen_shadowrun_KoerperlicheAtribute_Schadenswiederstand, gen_shadowrun_Nahkampfwaffe_AbstraktNahkampfwaffe, gen_shadowrun_ShrList_Beschreibbar, gen_shadowrun_Spezies_Beschreibbar, gen_shadowrun_Spezies_Modifizierbar, gen_shadowrun_SourceBook_Beschreibbar, gen_shadowrun_Shamane_MagiePersona, gen_shadowrun_Totem_Beschreibbar, gen_shadowrun_Granate_AbstaktWaffe, gen_shadowrun_Munition_AbstaktGegenstand},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)