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

SchadensTyp: Enumeration = Enumeration(
    name="SchadensTyp",
    literals={
            EnumerationLiteral(name="koerperlich"),
			EnumerationLiteral(name="geistig"),
			EnumerationLiteral(name="speziell")
    }
)

MagazinTyp: Enumeration = Enumeration(
    name="MagazinTyp",
    literals={
            EnumerationLiteral(name="Clip"),
			EnumerationLiteral(name="Trommel"),
			EnumerationLiteral(name="Gurt"),
			EnumerationLiteral(name="Streifen")
    }
)

FeuwerwaffenErweiterung: Enumeration = Enumeration(
    name="FeuwerwaffenErweiterung",
    literals={
            EnumerationLiteral(name="Lauf"),
			EnumerationLiteral(name="Unten"),
			EnumerationLiteral(name="Oben")
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

CritterHandlung: Enumeration = Enumeration(
    name="CritterHandlung",
    literals={
            EnumerationLiteral(name="komplex"),
			EnumerationLiteral(name="auto")
    }
)

CritterReichweite: Enumeration = Enumeration(
    name="CritterReichweite",
    literals={
            EnumerationLiteral(name="blickfeld"),
			EnumerationLiteral(name="beruehrung"),
			EnumerationLiteral(name="selbst"),
			EnumerationLiteral(name="speziell")
    }
)

CritterDauer: Enumeration = Enumeration(
    name="CritterDauer",
    literals={
            EnumerationLiteral(name="immer"),
			EnumerationLiteral(name="sofort"),
			EnumerationLiteral(name="aufrechterhalten"),
			EnumerationLiteral(name="permanent"),
			EnumerationLiteral(name="speziell")
    }
)

ResonanzZiel: Enumeration = Enumeration(
    name="ResonanzZiel",
    literals={
            EnumerationLiteral(name="datei"),
			EnumerationLiteral(name="geraet"),
			EnumerationLiteral(name="selbst"),
			EnumerationLiteral(name="persona"),
			EnumerationLiteral(name="sprite")
    }
)

InterfaceModus: Enumeration = Enumeration(
    name="InterfaceModus",
    literals={
            EnumerationLiteral(name="augmentedReality"),
			EnumerationLiteral(name="coldSim"),
			EnumerationLiteral(name="hotSim")
    }
)

ProgramType: Enumeration = Enumeration(
    name="ProgramType",
    literals={
            EnumerationLiteral(name="defaultSoft"),
			EnumerationLiteral(name="dataSoft"),
			EnumerationLiteral(name="shopSoft")
    }
)

MatrixProgramType: Enumeration = Enumeration(
    name="MatrixProgramType",
    literals={
            EnumerationLiteral(name="defaultProgram"),
			EnumerationLiteral(name="hackingProgram")
    }
)

SubstanceVector: Enumeration = Enumeration(
    name="SubstanceVector",
    literals={
            EnumerationLiteral(name="contact"),
			EnumerationLiteral(name="inhalation"),
			EnumerationLiteral(name="ingestion"),
			EnumerationLiteral(name="injection")
    }
)

SubstanceEffect: Enumeration = Enumeration(
    name="SubstanceEffect",
    literals={
            EnumerationLiteral(name="disorientation"),
			EnumerationLiteral(name="nausea"),
			EnumerationLiteral(name="paralysis"),
			EnumerationLiteral(name="stunDamage")
    }
)

AddictionType: Enumeration = Enumeration(
    name="AddictionType",
    literals={
            EnumerationLiteral(name="psychological"),
			EnumerationLiteral(name="physiological"),
			EnumerationLiteral(name="both")
    }
)

TimeUnits: Enumeration = Enumeration(
    name="TimeUnits",
    literals={
            EnumerationLiteral(name="sec"),
			EnumerationLiteral(name="min"),
			EnumerationLiteral(name="hour"),
			EnumerationLiteral(name="day"),
			EnumerationLiteral(name="week"),
			EnumerationLiteral(name="month"),
			EnumerationLiteral(name="year")
    }
)

Enzug: Enumeration = Enumeration(
    name="Enzug",
    literals={
            EnumerationLiteral(name="wil_log"),
			EnumerationLiteral(name="wil_cha"),
			EnumerationLiteral(name="wil_int")
    }
)

CyberwareType: Enumeration = Enumeration(
    name="CyberwareType",
    literals={
            EnumerationLiteral(name="cyberlimb"),
			EnumerationLiteral(name="earware"),
			EnumerationLiteral(name="eyeware"),
			EnumerationLiteral(name="headware"),
			EnumerationLiteral(name="bodyware")
    }
)

armorModificationType: Enumeration = Enumeration(
    name="armorModificationType",
    literals={
            EnumerationLiteral(name="ChemicalProtection"),
			EnumerationLiteral(name="ChemicalSeal"),
			EnumerationLiteral(name="FireResistance"),
			EnumerationLiteral(name="Insulation"),
			EnumerationLiteral(name="Nonconductivity"),
			EnumerationLiteral(name="ShockFrills"),
			EnumerationLiteral(name="ThermalDamping")
    }
)

# Classes
shr5_Beschreibbar = Class(name="shr5::Beschreibbar", is_abstract=True)
shr5_Quelle = Class(name="shr5::Quelle", is_abstract=True)
Identifiable = Class(name="Identifiable")
shr5_SourceBook = Class(name="shr5::SourceBook")
Beschreibbar = Class(name="Beschreibbar")
shr5_AbstraktPersona = Class(name="shr5::AbstraktPersona", is_abstract=True)
KoerperlicheAttribute = Class(name="KoerperlicheAttribute")
SpezielleAttribute = Class(name="SpezielleAttribute")
GeistigeAttribute = Class(name="GeistigeAttribute")
ChrakterLimits = Class(name="ChrakterLimits")
shr5_PersonaFertigkeit = Class(name="shr5::PersonaFertigkeit")
shr5_PersonaFertigkeitsGruppe = Class(name="shr5::PersonaFertigkeitsGruppe")
shr5_Spezies = Class(name="shr5::Spezies")
shr5_PersonaMartialartStyle = Class(name="shr5::PersonaMartialartStyle")
shr5_Gegenstand = Class(name="shr5::Gegenstand")
AbstraktGegenstand = Class(name="AbstraktGegenstand")
shr5_Reichweite = Class(name="shr5::Reichweite")
shr5_AttributModifikatorWert = Class(name="shr5::AttributModifikatorWert")
shr5_EAttribute = Class(name="shr5::EAttribute")
shr5_Modifizierbar = Class(name="shr5::Modifizierbar", is_abstract=True)
shr5_Modifyable = Class(name="shr5::Modifyable", is_abstract=True)
shr5_KoerperlicheAttribute = Class(name="shr5::KoerperlicheAttribute", is_abstract=True)
ModifikatorAttribute = Class(name="ModifikatorAttribute")
shr5_SpezielleAttribute = Class(name="shr5::SpezielleAttribute", is_abstract=True)
shr5_GeldWert = Class(name="shr5::GeldWert", is_abstract=True)
shr5_AbstraktGegenstand = Class(name="shr5::AbstraktGegenstand", is_abstract=True)
Quelle = Class(name="Quelle")
GeldWert = Class(name="GeldWert")
Modifizierbar = Class(name="Modifizierbar")
Anwendbar = Class(name="Anwendbar")
shr5_MatrixDevice = Class(name="shr5::MatrixDevice", is_abstract=True)
shr5_AbstaktFernKampfwaffe = Class(name="shr5::AbstaktFernKampfwaffe", is_abstract=True)
AbstaktWaffe = Class(name="AbstaktWaffe")
shr5_AbstaktWaffe = Class(name="shr5::AbstaktWaffe", is_abstract=True)
shr5_Nahkampfwaffe = Class(name="shr5::Nahkampfwaffe")
shr5_Feuerwaffe = Class(name="shr5::Feuerwaffe")
AbstaktFernKampfwaffe = Class(name="AbstaktFernKampfwaffe")
shr5_FernkampfwaffeModifikator = Class(name="shr5::FernkampfwaffeModifikator")
shr5_Magazin = Class(name="shr5::Magazin")
shr5_Wurfwaffe = Class(name="shr5::Wurfwaffe")
Menge = Class(name="Menge")
shr5_ShrList = Class(name="shr5::ShrList")
shr5_EObject = Class(name="shr5::EObject")
shr5_Projektilwaffe = Class(name="shr5::Projektilwaffe")
shr5_FertigkeitsGruppe = Class(name="shr5::FertigkeitsGruppe")
Modifyable = Class(name="Modifyable")
shr5_Fertigkeit = Class(name="shr5::Fertigkeit")
shr5_Spezialisierung = Class(name="shr5::Spezialisierung")
Steigerbar = Class(name="Steigerbar")
shr5_Cyberware = Class(name="shr5::Cyberware")
Koerpermods = Class(name="Koerpermods")
Capacity = Class(name="Capacity")
shr5_CyberwareEnhancement = Class(name="shr5::CyberwareEnhancement")
shr5_DefaultWifi = Class(name="shr5::DefaultWifi")
shr5_BioWare = Class(name="shr5::BioWare")
shr5_Koerpermods = Class(name="shr5::Koerpermods", is_abstract=True)
AbstraktModifikatoren = Class(name="AbstraktModifikatoren")
shr5_AbstraktModifikatoren = Class(name="shr5::AbstraktModifikatoren", is_abstract=True)
shr5_GeistigeAttribute = Class(name="shr5::GeistigeAttribute", is_abstract=True)
shr5_MudanPersona = Class(name="shr5::MudanPersona")
KoerperPersona = Class(name="KoerperPersona")
shr5_KoerperPersona = Class(name="shr5::KoerperPersona", is_abstract=True)
AbstraktPersona = Class(name="AbstraktPersona")
Panzerung = Class(name="Panzerung")
PersonaZustand = Class(name="PersonaZustand")
BerechneteAttribute = Class(name="BerechneteAttribute")
shr5_PersonaEigenschaft = Class(name="shr5::PersonaEigenschaft")
shr5_MagischeMods = Class(name="shr5::MagischeMods", is_abstract=True)
shr5_KiKraft = Class(name="shr5::KiKraft")
MagischeMods = Class(name="MagischeMods")
Erlernbar = Class(name="Erlernbar")
shr5_MagischePersona = Class(name="shr5::MagischePersona", is_abstract=True)
BaseMagischePersona = Class(name="BaseMagischePersona")
shr5_Schutzgeist = Class(name="shr5::Schutzgeist")
shr5_BaseMagischePersona = Class(name="shr5::BaseMagischePersona", is_abstract=True)
shr5_Initation = Class(name="shr5::Initation")
shr5_FokusBinding = Class(name="shr5::FokusBinding")
shr5_FernkampfwaffenModifikatoren = Class(name="shr5::FernkampfwaffenModifikatoren", is_abstract=True)
shr5_Sichtverhaeltnisse = Class(name="shr5::Sichtverhaeltnisse", is_abstract=True)
shr5_GegenstandStufen = Class(name="shr5::GegenstandStufen", is_abstract=True)
shr5_KiAdept = Class(name="shr5::KiAdept")
MagischePersona = Class(name="MagischePersona")
shr5_Kleidung = Class(name="shr5::Kleidung")
shr5_KleindungsModifikator = Class(name="shr5::KleindungsModifikator")
shr5_Anwendbar = Class(name="shr5::Anwendbar", is_abstract=True)
shr5_ProbenModifikatoren = Class(name="shr5::ProbenModifikatoren", is_abstract=True)
shr5_Magier = Class(name="shr5::Magier")
Zauberer = Class(name="Zauberer")
AstraleProjektion = Class(name="AstraleProjektion")
shr5_Zauberer = Class(name="shr5::Zauberer", is_abstract=True)
shr5_PersonaZauber = Class(name="shr5::PersonaZauber")
shr5_GebundenerGeist = Class(name="shr5::GebundenerGeist")
shr5_MagischeTradition = Class(name="shr5::MagischeTradition")
shr5_MysticAdept = Class(name="shr5::MysticAdept")
KiAdept = Class(name="KiAdept")
shr5_Zauber = Class(name="shr5::Zauber")
shr5_ChrakterLimits = Class(name="shr5::ChrakterLimits", is_abstract=True)
shr5_Panzerung = Class(name="shr5::Panzerung", is_abstract=True)
shr5_AspektMagier = Class(name="shr5::AspektMagier")
shr5_MetaMagie = Class(name="shr5::MetaMagie")
shr5_CritterKraft = Class(name="shr5::CritterKraft")
shr5_Fahrzeug = Class(name="shr5::Fahrzeug", is_abstract=True)
FahrzeugZustand = Class(name="FahrzeugZustand")
shr5_AstraleProjektion = Class(name="shr5::AstraleProjektion", is_abstract=True)
shr5_FahrzeugModifikation = Class(name="shr5::FahrzeugModifikation", is_abstract=True)
shr5_SensorArray = Class(name="shr5::SensorArray")
shr5_Bodenfahrzeug = Class(name="shr5::Bodenfahrzeug")
PassagierFahrzeug = Class(name="PassagierFahrzeug")
shr5_PassagierFahrzeug = Class(name="shr5::PassagierFahrzeug")
Fahrzeug = Class(name="Fahrzeug")
shr5_Drohne = Class(name="shr5::Drohne")
MatrixAttributes = Class(name="MatrixAttributes")
shr5_RiggerProgram = Class(name="shr5::RiggerProgram", is_abstract=True)
shr5_Technomancer = Class(name="shr5::Technomancer")
ResonanzPersona = Class(name="ResonanzPersona")
shr5_PersonaKomplexForm = Class(name="shr5::PersonaKomplexForm")
shr5_Echo = Class(name="shr5::Echo")
shr5_ResonanzPersona = Class(name="shr5::ResonanzPersona", is_abstract=True)
ActiveMatixDevice = Class(name="ActiveMatixDevice")
shr5_KomplexeForm = Class(name="shr5::KomplexeForm")
shr5_Sprite = Class(name="shr5::Sprite")
shr5_Vertrag = Class(name="shr5::Vertrag")
shr5_Lifestyle = Class(name="shr5::Lifestyle")
IntervallVertrag = Class(name="IntervallVertrag")
shr5_LifestyleOption = Class(name="shr5::LifestyleOption")
shr5_Wissensfertigkeit = Class(name="shr5::Wissensfertigkeit")
Fertigkeit = Class(name="Fertigkeit")
shr5_Sprachfertigkeit = Class(name="shr5::Sprachfertigkeit")
Wissensfertigkeit = Class(name="Wissensfertigkeit")
shr5_PersonaZustand = Class(name="shr5::PersonaZustand", is_abstract=True)
shr5_Critter = Class(name="shr5::Critter")
Spezies = Class(name="Spezies")
shr5_IntervallVertrag = Class(name="shr5::IntervallVertrag")
Vertrag = Class(name="Vertrag")
shr5_Sin = Class(name="shr5::Sin")
Fakeable = Class(name="Fakeable")
shr5_Lizenz = Class(name="shr5::Lizenz")
shr5_Fakeable = Class(name="shr5::Fakeable", is_abstract=True)
shr5_Steigerbar = Class(name="shr5::Steigerbar", is_abstract=True)
shr5_Erlernbar = Class(name="shr5::Erlernbar", is_abstract=True)
shr5_Credstick = Class(name="shr5::Credstick")
shr5_CredstickTransaction = Class(name="shr5::CredstickTransaction")
shr5_Menge = Class(name="shr5::Menge", is_abstract=True)
shr5_Munition = Class(name="shr5::Munition")
shr5_ModifikatorAttribute = Class(name="shr5::ModifikatorAttribute", is_abstract=True)
shr5_Geist = Class(name="shr5::Geist")
shr5_StufenPersona = Class(name="shr5::StufenPersona", is_abstract=True)
StufenPersona = Class(name="StufenPersona")
shr5_Identifiable = Class(name="shr5::Identifiable", is_abstract=True)
shr5_Localization = Class(name="shr5::Localization")
shr5_MatrixAttributes = Class(name="shr5::MatrixAttributes", is_abstract=True)
MatixConditionMonitor = Class(name="MatixConditionMonitor")
shr5_ActiveMatixDevice = Class(name="shr5::ActiveMatixDevice", is_abstract=True)
shr5_Commlink = Class(name="shr5::Commlink")
AbstractMatrixDevice = Class(name="AbstractMatrixDevice")
shr5_BasicProgram = Class(name="shr5::BasicProgram", is_abstract=True)
shr5_MatixConditionMonitor = Class(name="shr5::MatixConditionMonitor", is_abstract=True)
shr5_Cyberdeck = Class(name="shr5::Cyberdeck")
MatrixDevice = Class(name="MatrixDevice")
shr5_MatrixProgram = Class(name="shr5::MatrixProgram", is_abstract=True)
shr5_SoftwareAgent = Class(name="shr5::SoftwareAgent")
MatrixProgram = Class(name="MatrixProgram")
shr5_Host = Class(name="shr5::Host")
shr5_CyberwareModifikatioren = Class(name="shr5::CyberwareModifikatioren", is_abstract=True)
shr5_RiggerCommandConsole = Class(name="shr5::RiggerCommandConsole")
shr5_AutoSoft = Class(name="shr5::AutoSoft")
RiggerProgram = Class(name="RiggerProgram")
shr5_Software = Class(name="shr5::Software", is_abstract=True)
Software = Class(name="Software")
shr5_Tutorsoft = Class(name="shr5::Tutorsoft")
BasicProgram = Class(name="BasicProgram")
shr5_SkillSoft = Class(name="shr5::SkillSoft")
shr5_PersonalAreaNetwork = Class(name="shr5::PersonalAreaNetwork")
shr5_Datasoft = Class(name="shr5::Datasoft")
shr5_AbstractMatrixDevice = Class(name="shr5::AbstractMatrixDevice", is_abstract=True)
shr5_ConsumerSoft = Class(name="shr5::ConsumerSoft")
shr5_CommonProgram = Class(name="shr5::CommonProgram")
shr5_WeaponMount = Class(name="shr5::WeaponMount")
FahrzeugModifikation = Class(name="FahrzeugModifikation")
shr5_PercentLifestyleOption = Class(name="shr5::PercentLifestyleOption")
LifestyleOption = Class(name="LifestyleOption")
shr5_FahrzeugZustand = Class(name="shr5::FahrzeugZustand", is_abstract=True)
shr5_MagischeStufe = Class(name="shr5::MagischeStufe", is_abstract=True)
shr5_Fokus = Class(name="shr5::Fokus", is_abstract=True)
MagischeStufe = Class(name="MagischeStufe")
shr5_AbstraktFokus = Class(name="shr5::AbstraktFokus", is_abstract=True)
Fokus = Class(name="Fokus")
shr5_QiFokus = Class(name="shr5::QiFokus")
AbstraktFokus = Class(name="AbstraktFokus")
shr5_WaffenFokus = Class(name="shr5::WaffenFokus")
Nahkampfwaffe = Class(name="Nahkampfwaffe")
shr5_MagieFokus = Class(name="shr5::MagieFokus")
shr5_Substance = Class(name="shr5::Substance", is_abstract=True)
shr5_Toxin = Class(name="shr5::Toxin")
Substance = Class(name="Substance")
shr5_BerechneteAttribute = Class(name="shr5::BerechneteAttribute", is_abstract=True)
shr5_SubstanceContainer = Class(name="shr5::SubstanceContainer")
shr5_Capacity = Class(name="shr5::Capacity", is_abstract=True)
shr5_EReference = Class(name="shr5::EReference")
shr5_Drug = Class(name="shr5::Drug")
shr5_CyberImplantWeapon = Class(name="shr5::CyberImplantWeapon")
CyberwareEnhancement = Class(name="CyberwareEnhancement")
shr5_ShoppingTransaction = Class(name="shr5::ShoppingTransaction")
CredstickTransaction = Class(name="CredstickTransaction")
shr5_TransferAmount = Class(name="shr5::TransferAmount")
shr5_Sensor = Class(name="shr5::Sensor")
shr5_SensorFunction = Class(name="shr5::SensorFunction")
Sensor = Class(name="Sensor")
shr5_MartialartStyle = Class(name="shr5::MartialartStyle")
shr5_MartialartTechnique = Class(name="shr5::MartialartTechnique")
Spezialisierung = Class(name="Spezialisierung")
shr5_PersonaMartialartTechnique = Class(name="shr5::PersonaMartialartTechnique")
shr5_FahrzeugErweiterung = Class(name="shr5::FahrzeugErweiterung")
shr5_AbtraktGranate = Class(name="shr5::AbtraktGranate", is_abstract=True)
shr5_MiniGrenate = Class(name="shr5::MiniGrenate")
Munition = Class(name="Munition")
AbtraktGranate = Class(name="AbtraktGranate")
shr5_Granate = Class(name="shr5::Granate")
Wurfwaffe = Class(name="Wurfwaffe")
shr5_SourceLink = Class(name="shr5::SourceLink")

# shr5_Beschreibbar class attributes and methods
shr5_Beschreibbar_beschreibung: Property = Property(name="beschreibung", type=StringType)
shr5_Beschreibbar_name: Property = Property(name="name", type=StringType)
shr5_Beschreibbar_image: Property = Property(name="image", type=StringType)
shr5_Beschreibbar.attributes={shr5_Beschreibbar_name, shr5_Beschreibbar_beschreibung, shr5_Beschreibbar_image}

# shr5_Quelle class attributes and methods
shr5_Quelle_page: Property = Property(name="page", type=StringType)
shr5_Quelle.attributes={shr5_Quelle_page}

# Identifiable class attributes and methods

# shr5_SourceBook class attributes and methods
shr5_SourceBook_startShrTime: Property = Property(name="startShrTime", type=StringType)
shr5_SourceBook_endShrTime: Property = Property(name="endShrTime", type=StringType)
shr5_SourceBook_code: Property = Property(name="code", type=StringType)
shr5_SourceBook.attributes={shr5_SourceBook_code, shr5_SourceBook_startShrTime, shr5_SourceBook_endShrTime}

# Beschreibbar class attributes and methods

# shr5_AbstraktPersona class attributes and methods
shr5_AbstraktPersona_konstitutionBasis: Property = Property(name="konstitutionBasis", type=IntegerType)
shr5_AbstraktPersona_geschicklichkeitBasis: Property = Property(name="geschicklichkeitBasis", type=IntegerType)
shr5_AbstraktPersona_reaktionBasis: Property = Property(name="reaktionBasis", type=IntegerType)
shr5_AbstraktPersona_staerkeBasis: Property = Property(name="staerkeBasis", type=IntegerType)
shr5_AbstraktPersona_charismaBasis: Property = Property(name="charismaBasis", type=IntegerType)
shr5_AbstraktPersona_willenskraftBasis: Property = Property(name="willenskraftBasis", type=IntegerType)
shr5_AbstraktPersona_intuitionBasis: Property = Property(name="intuitionBasis", type=IntegerType)
shr5_AbstraktPersona_logikBasis: Property = Property(name="logikBasis", type=IntegerType)
shr5_AbstraktPersona_modManager: Property = Property(name="modManager", type=StringType)
shr5_AbstraktPersona.attributes={shr5_AbstraktPersona_geschicklichkeitBasis, shr5_AbstraktPersona_intuitionBasis, shr5_AbstraktPersona_reaktionBasis, shr5_AbstraktPersona_konstitutionBasis, shr5_AbstraktPersona_willenskraftBasis, shr5_AbstraktPersona_modManager, shr5_AbstraktPersona_charismaBasis, shr5_AbstraktPersona_staerkeBasis, shr5_AbstraktPersona_logikBasis}

# KoerperlicheAttribute class attributes and methods

# SpezielleAttribute class attributes and methods

# GeistigeAttribute class attributes and methods

# ChrakterLimits class attributes and methods

# shr5_PersonaFertigkeit class attributes and methods

# shr5_PersonaFertigkeitsGruppe class attributes and methods

# shr5_Spezies class attributes and methods
shr5_Spezies_konstitutionMin: Property = Property(name="konstitutionMin", type=IntegerType)
shr5_Spezies_geschicklichkeitMin: Property = Property(name="geschicklichkeitMin", type=IntegerType)
shr5_Spezies_reaktionMin: Property = Property(name="reaktionMin", type=IntegerType)
shr5_Spezies_staerkeMin: Property = Property(name="staerkeMin", type=IntegerType)
shr5_Spezies_charismaMin: Property = Property(name="charismaMin", type=IntegerType)
shr5_Spezies_willenskraftMin: Property = Property(name="willenskraftMin", type=IntegerType)
shr5_Spezies_intuitionMin: Property = Property(name="intuitionMin", type=IntegerType)
shr5_Spezies_logikMin: Property = Property(name="logikMin", type=IntegerType)
shr5_Spezies_edgeMin: Property = Property(name="edgeMin", type=IntegerType)
shr5_Spezies_magieMin: Property = Property(name="magieMin", type=IntegerType)
shr5_Spezies_resonanzMin: Property = Property(name="resonanzMin", type=IntegerType)
shr5_Spezies_essenzMin: Property = Property(name="essenzMin", type=IntegerType)
shr5_Spezies_konstitutionMax: Property = Property(name="konstitutionMax", type=IntegerType)
shr5_Spezies_geschicklichkeitMax: Property = Property(name="geschicklichkeitMax", type=IntegerType)
shr5_Spezies_reaktionMax: Property = Property(name="reaktionMax", type=IntegerType)
shr5_Spezies_staerkeMax: Property = Property(name="staerkeMax", type=IntegerType)
shr5_Spezies_charismaMax: Property = Property(name="charismaMax", type=IntegerType)
shr5_Spezies_willenskraftMax: Property = Property(name="willenskraftMax", type=IntegerType)
shr5_Spezies_intuitionMax: Property = Property(name="intuitionMax", type=IntegerType)
shr5_Spezies_logikMax: Property = Property(name="logikMax", type=IntegerType)
shr5_Spezies_edgeMax: Property = Property(name="edgeMax", type=IntegerType)
shr5_Spezies_magieMax: Property = Property(name="magieMax", type=IntegerType)
shr5_Spezies_resonanzMax: Property = Property(name="resonanzMax", type=IntegerType)
shr5_Spezies_essenzMax: Property = Property(name="essenzMax", type=IntegerType)
shr5_Spezies_laufen: Property = Property(name="laufen", type=IntegerType)
shr5_Spezies_rennen: Property = Property(name="rennen", type=IntegerType)
shr5_Spezies_sprinten: Property = Property(name="sprinten", type=IntegerType)
shr5_Spezies.attributes={shr5_Spezies_staerkeMin, shr5_Spezies_logikMax, shr5_Spezies_intuitionMin, shr5_Spezies_resonanzMin, shr5_Spezies_rennen, shr5_Spezies_sprinten, shr5_Spezies_willenskraftMin, shr5_Spezies_resonanzMax, shr5_Spezies_edgeMax, shr5_Spezies_reaktionMin, shr5_Spezies_intuitionMax, shr5_Spezies_charismaMin, shr5_Spezies_laufen, shr5_Spezies_geschicklichkeitMin, shr5_Spezies_staerkeMax, shr5_Spezies_essenzMax, shr5_Spezies_willenskraftMax, shr5_Spezies_essenzMin, shr5_Spezies_geschicklichkeitMax, shr5_Spezies_charismaMax, shr5_Spezies_edgeMin, shr5_Spezies_konstitutionMax, shr5_Spezies_konstitutionMin, shr5_Spezies_magieMax, shr5_Spezies_reaktionMax, shr5_Spezies_logikMin, shr5_Spezies_magieMin}

# shr5_PersonaMartialartStyle class attributes and methods

# shr5_Gegenstand class attributes and methods
shr5_Gegenstand_kategorie: Property = Property(name="kategorie", type=StringType)
shr5_Gegenstand_stufe: Property = Property(name="stufe", type=IntegerType)
shr5_Gegenstand.attributes={shr5_Gegenstand_kategorie, shr5_Gegenstand_stufe}

# AbstraktGegenstand class attributes and methods

# shr5_Reichweite class attributes and methods
shr5_Reichweite_min: Property = Property(name="min", type=IntegerType)
shr5_Reichweite_kurz: Property = Property(name="kurz", type=IntegerType)
shr5_Reichweite_mittel: Property = Property(name="mittel", type=IntegerType)
shr5_Reichweite_weit: Property = Property(name="weit", type=IntegerType)
shr5_Reichweite_extrem: Property = Property(name="extrem", type=IntegerType)
shr5_Reichweite.attributes={shr5_Reichweite_extrem, shr5_Reichweite_weit, shr5_Reichweite_kurz, shr5_Reichweite_mittel, shr5_Reichweite_min}

# shr5_AttributModifikatorWert class attributes and methods
shr5_AttributModifikatorWert_wert: Property = Property(name="wert", type=IntegerType)
shr5_AttributModifikatorWert.attributes={shr5_AttributModifikatorWert_wert}

# shr5_EAttribute class attributes and methods

# shr5_Modifizierbar class attributes and methods

# shr5_Modifyable class attributes and methods

# shr5_KoerperlicheAttribute class attributes and methods
shr5_KoerperlicheAttribute_konstitution: Property = Property(name="konstitution", type=IntegerType)
shr5_KoerperlicheAttribute_geschicklichkeit: Property = Property(name="geschicklichkeit", type=IntegerType)
shr5_KoerperlicheAttribute_reaktion: Property = Property(name="reaktion", type=IntegerType)
shr5_KoerperlicheAttribute_staerke: Property = Property(name="staerke", type=IntegerType)
shr5_KoerperlicheAttribute.attributes={shr5_KoerperlicheAttribute_geschicklichkeit, shr5_KoerperlicheAttribute_reaktion, shr5_KoerperlicheAttribute_staerke, shr5_KoerperlicheAttribute_konstitution}

# ModifikatorAttribute class attributes and methods

# shr5_SpezielleAttribute class attributes and methods
shr5_SpezielleAttribute_initative: Property = Property(name="initative", type=IntegerType)
shr5_SpezielleAttribute_initativWuerfel: Property = Property(name="initativWuerfel", type=IntegerType)
shr5_SpezielleAttribute_ausweichen: Property = Property(name="ausweichen", type=IntegerType)
shr5_SpezielleAttribute_essenz: Property = Property(name="essenz", type=IntegerType)
shr5_SpezielleAttribute_edgeBasis: Property = Property(name="edgeBasis", type=IntegerType)
shr5_SpezielleAttribute_edge: Property = Property(name="edge", type=IntegerType)
shr5_SpezielleAttribute.attributes={shr5_SpezielleAttribute_edgeBasis, shr5_SpezielleAttribute_initative, shr5_SpezielleAttribute_initativWuerfel, shr5_SpezielleAttribute_ausweichen, shr5_SpezielleAttribute_essenz, shr5_SpezielleAttribute_edge}

# shr5_GeldWert class attributes and methods
shr5_GeldWert_wert: Property = Property(name="wert", type=StringType)
shr5_GeldWert_verfuegbarkeit: Property = Property(name="verfuegbarkeit", type=StringType)
shr5_GeldWert_wertValue: Property = Property(name="wertValue", type=StringType)
shr5_GeldWert.attributes={shr5_GeldWert_wert, shr5_GeldWert_verfuegbarkeit, shr5_GeldWert_wertValue}

# shr5_AbstraktGegenstand class attributes and methods

# Quelle class attributes and methods

# GeldWert class attributes and methods

# Modifizierbar class attributes and methods

# Anwendbar class attributes and methods

# shr5_MatrixDevice class attributes and methods

# shr5_AbstaktFernKampfwaffe class attributes and methods

# AbstaktWaffe class attributes and methods

# shr5_AbstaktWaffe class attributes and methods
shr5_AbstaktWaffe_schadenscode: Property = Property(name="schadenscode", type=StringType)
shr5_AbstaktWaffe_schadesTyp: Property = Property(name="schadesTyp", type=StringType)
shr5_AbstaktWaffe_praezision: Property = Property(name="praezision", type=IntegerType)
shr5_AbstaktWaffe_durchschlagsKraft: Property = Property(name="durchschlagsKraft", type=IntegerType)
shr5_AbstaktWaffe.attributes={shr5_AbstaktWaffe_schadenscode, shr5_AbstaktWaffe_durchschlagsKraft, shr5_AbstaktWaffe_schadesTyp, shr5_AbstaktWaffe_praezision}

# shr5_Nahkampfwaffe class attributes and methods
shr5_Nahkampfwaffe_reichweite: Property = Property(name="reichweite", type=IntegerType)
shr5_Nahkampfwaffe.attributes={shr5_Nahkampfwaffe_reichweite}

# shr5_Feuerwaffe class attributes and methods
shr5_Feuerwaffe_munitionstyp: Property = Property(name="munitionstyp", type=StringType)
shr5_Feuerwaffe_modie: Property = Property(name="modie", type=StringType)
shr5_Feuerwaffe_kapazitaet: Property = Property(name="kapazitaet", type=IntegerType)
shr5_Feuerwaffe_erweiterung: Property = Property(name="erweiterung", type=StringType)
shr5_Feuerwaffe_rueckstoss: Property = Property(name="rueckstoss", type=IntegerType)
shr5_Feuerwaffe.attributes={shr5_Feuerwaffe_kapazitaet, shr5_Feuerwaffe_rueckstoss, shr5_Feuerwaffe_munitionstyp, shr5_Feuerwaffe_modie, shr5_Feuerwaffe_erweiterung}

# AbstaktFernKampfwaffe class attributes and methods

# shr5_FernkampfwaffeModifikator class attributes and methods
shr5_FernkampfwaffeModifikator_ep: Property = Property(name="ep", type=StringType)
shr5_FernkampfwaffeModifikator.attributes={shr5_FernkampfwaffeModifikator_ep}

# shr5_Magazin class attributes and methods

# shr5_Wurfwaffe class attributes and methods

# Menge class attributes and methods

# shr5_ShrList class attributes and methods

# shr5_EObject class attributes and methods

# shr5_Projektilwaffe class attributes and methods

# shr5_FertigkeitsGruppe class attributes and methods

# Modifyable class attributes and methods

# shr5_Fertigkeit class attributes and methods
shr5_Fertigkeit_kategorie: Property = Property(name="kategorie", type=StringType)
shr5_Fertigkeit_ausweichen: Property = Property(name="ausweichen", type=BooleanType)
shr5_Fertigkeit.attributes={shr5_Fertigkeit_kategorie, shr5_Fertigkeit_ausweichen}

# shr5_Spezialisierung class attributes and methods

# Steigerbar class attributes and methods

# shr5_Cyberware class attributes and methods
shr5_Cyberware_cyberwareCapacity: Property = Property(name="cyberwareCapacity", type=IntegerType)
shr5_Cyberware_type: Property = Property(name="type", type=StringType)
shr5_Cyberware.attributes={shr5_Cyberware_type, shr5_Cyberware_cyberwareCapacity}

# Koerpermods class attributes and methods

# Capacity class attributes and methods

# shr5_CyberwareEnhancement class attributes and methods
shr5_CyberwareEnhancement_capacityUse: Property = Property(name="capacityUse", type=IntegerType)
shr5_CyberwareEnhancement_type: Property = Property(name="type", type=StringType)
shr5_CyberwareEnhancement.attributes={shr5_CyberwareEnhancement_type, shr5_CyberwareEnhancement_capacityUse}

# shr5_DefaultWifi class attributes and methods

# shr5_BioWare class attributes and methods

# shr5_Koerpermods class attributes and methods

# AbstraktModifikatoren class attributes and methods

# shr5_AbstraktModifikatoren class attributes and methods

# shr5_GeistigeAttribute class attributes and methods
shr5_GeistigeAttribute_charisma: Property = Property(name="charisma", type=IntegerType)
shr5_GeistigeAttribute_willenskraft: Property = Property(name="willenskraft", type=IntegerType)
shr5_GeistigeAttribute_intuition: Property = Property(name="intuition", type=IntegerType)
shr5_GeistigeAttribute_logik: Property = Property(name="logik", type=IntegerType)
shr5_GeistigeAttribute.attributes={shr5_GeistigeAttribute_willenskraft, shr5_GeistigeAttribute_logik, shr5_GeistigeAttribute_charisma, shr5_GeistigeAttribute_intuition}

# shr5_MudanPersona class attributes and methods

# KoerperPersona class attributes and methods

# shr5_KoerperPersona class attributes and methods
shr5_KoerperPersona_zustandKoerperlich: Property = Property(name="zustandKoerperlich", type=IntegerType)
shr5_KoerperPersona_zustandGeistig: Property = Property(name="zustandGeistig", type=IntegerType)
shr5_KoerperPersona.attributes={shr5_KoerperPersona_zustandKoerperlich, shr5_KoerperPersona_zustandGeistig}

# AbstraktPersona class attributes and methods

# Panzerung class attributes and methods

# PersonaZustand class attributes and methods

# BerechneteAttribute class attributes and methods

# shr5_PersonaEigenschaft class attributes and methods
shr5_PersonaEigenschaft_karmaKosten: Property = Property(name="karmaKosten", type=IntegerType)
shr5_PersonaEigenschaft.attributes={shr5_PersonaEigenschaft_karmaKosten}

# shr5_MagischeMods class attributes and methods

# shr5_KiKraft class attributes and methods
shr5_KiKraft_kraftpunkte: Property = Property(name="kraftpunkte", type=IntegerType)
shr5_KiKraft.attributes={shr5_KiKraft_kraftpunkte}

# MagischeMods class attributes and methods

# Erlernbar class attributes and methods

# shr5_MagischePersona class attributes and methods

# BaseMagischePersona class attributes and methods

# shr5_Schutzgeist class attributes and methods
shr5_Schutzgeist_vorteile: Property = Property(name="vorteile", type=StringType)
shr5_Schutzgeist_nachteile: Property = Property(name="nachteile", type=StringType)
shr5_Schutzgeist.attributes={shr5_Schutzgeist_vorteile, shr5_Schutzgeist_nachteile}

# shr5_BaseMagischePersona class attributes and methods
shr5_BaseMagischePersona_magie: Property = Property(name="magie", type=IntegerType)
shr5_BaseMagischePersona_magieBasis: Property = Property(name="magieBasis", type=IntegerType)
shr5_BaseMagischePersona.attributes={shr5_BaseMagischePersona_magieBasis, shr5_BaseMagischePersona_magie}

# shr5_Initation class attributes and methods

# shr5_FokusBinding class attributes and methods
shr5_FokusBinding_active: Property = Property(name="active", type=BooleanType)
shr5_FokusBinding.attributes={shr5_FokusBinding_active}

# shr5_FernkampfwaffenModifikatoren class attributes and methods
shr5_FernkampfwaffenModifikatoren_rueckstoss: Property = Property(name="rueckstoss", type=IntegerType)
shr5_FernkampfwaffenModifikatoren_lasterPointer: Property = Property(name="lasterPointer", type=BooleanType)
shr5_FernkampfwaffenModifikatoren_schalldaempfer: Property = Property(name="schalldaempfer", type=BooleanType)
shr5_FernkampfwaffenModifikatoren_vergroesserung: Property = Property(name="vergroesserung", type=IntegerType)
shr5_FernkampfwaffenModifikatoren_sichtverbesserung: Property = Property(name="sichtverbesserung", type=IntegerType)
shr5_FernkampfwaffenModifikatoren_smartgun: Property = Property(name="smartgun", type=StringType)
shr5_FernkampfwaffenModifikatoren.attributes={shr5_FernkampfwaffenModifikatoren_schalldaempfer, shr5_FernkampfwaffenModifikatoren_rueckstoss, shr5_FernkampfwaffenModifikatoren_smartgun, shr5_FernkampfwaffenModifikatoren_sichtverbesserung, shr5_FernkampfwaffenModifikatoren_vergroesserung, shr5_FernkampfwaffenModifikatoren_lasterPointer}

# shr5_Sichtverhaeltnisse class attributes and methods
shr5_Sichtverhaeltnisse_restlichtverstaerkung: Property = Property(name="restlichtverstaerkung", type=StringType)
shr5_Sichtverhaeltnisse_infrarot: Property = Property(name="infrarot", type=StringType)
shr5_Sichtverhaeltnisse_ultrasound: Property = Property(name="ultrasound", type=StringType)
shr5_Sichtverhaeltnisse.attributes={shr5_Sichtverhaeltnisse_infrarot, shr5_Sichtverhaeltnisse_ultrasound, shr5_Sichtverhaeltnisse_restlichtverstaerkung}

# shr5_GegenstandStufen class attributes and methods
shr5_GegenstandStufen_computer: Property = Property(name="computer", type=IntegerType)
shr5_GegenstandStufen_elektronik: Property = Property(name="elektronik", type=IntegerType)
shr5_GegenstandStufen_tracing: Property = Property(name="tracing", type=IntegerType)
shr5_GegenstandStufen_antiTracing: Property = Property(name="antiTracing", type=IntegerType)
shr5_GegenstandStufen_protection: Property = Property(name="protection", type=IntegerType)
shr5_GegenstandStufen_antiProtection: Property = Property(name="antiProtection", type=IntegerType)
shr5_GegenstandStufen.attributes={shr5_GegenstandStufen_antiTracing, shr5_GegenstandStufen_tracing, shr5_GegenstandStufen_elektronik, shr5_GegenstandStufen_protection, shr5_GegenstandStufen_antiProtection, shr5_GegenstandStufen_computer}

# shr5_KiAdept class attributes and methods

# MagischePersona class attributes and methods

# shr5_Kleidung class attributes and methods
shr5_Kleidung_ruestung: Property = Property(name="ruestung", type=IntegerType)
shr5_Kleidung.attributes={shr5_Kleidung_ruestung}

# shr5_KleindungsModifikator class attributes and methods
shr5_KleindungsModifikator_rating: Property = Property(name="rating", type=IntegerType)
shr5_KleindungsModifikator_type: Property = Property(name="type", type=StringType)
shr5_KleindungsModifikator_capacity: Property = Property(name="capacity", type=IntegerType)
shr5_KleindungsModifikator.attributes={shr5_KleindungsModifikator_type, shr5_KleindungsModifikator_rating, shr5_KleindungsModifikator_capacity}

# shr5_Anwendbar class attributes and methods

# shr5_ProbenModifikatoren class attributes and methods
shr5_ProbenModifikatoren_schadenswiederstand: Property = Property(name="schadenswiederstand", type=IntegerType)
shr5_ProbenModifikatoren_heilung: Property = Property(name="heilung", type=IntegerType)
shr5_ProbenModifikatoren.attributes={shr5_ProbenModifikatoren_schadenswiederstand, shr5_ProbenModifikatoren_heilung}

# shr5_Magier class attributes and methods

# Zauberer class attributes and methods

# AstraleProjektion class attributes and methods

# shr5_Zauberer class attributes and methods
shr5_Zauberer_enzug: Property = Property(name="enzug", type=IntegerType)
shr5_Zauberer.attributes={shr5_Zauberer_enzug}

# shr5_PersonaZauber class attributes and methods
shr5_PersonaZauber_stufe: Property = Property(name="stufe", type=IntegerType)
shr5_PersonaZauber.attributes={shr5_PersonaZauber_stufe}

# shr5_GebundenerGeist class attributes and methods
shr5_GebundenerGeist_dienste: Property = Property(name="dienste", type=IntegerType)
shr5_GebundenerGeist.attributes={shr5_GebundenerGeist_dienste}

# shr5_MagischeTradition class attributes and methods
shr5_MagischeTradition_enzug: Property = Property(name="enzug", type=StringType)
shr5_MagischeTradition.attributes={shr5_MagischeTradition_enzug}

# shr5_MysticAdept class attributes and methods

# KiAdept class attributes and methods

# shr5_Zauber class attributes and methods
shr5_Zauber_art: Property = Property(name="art", type=StringType)
shr5_Zauber_reichweite: Property = Property(name="reichweite", type=StringType)
shr5_Zauber_schaden: Property = Property(name="schaden", type=StringType)
shr5_Zauber_dauer: Property = Property(name="dauer", type=StringType)
shr5_Zauber_entzug: Property = Property(name="entzug", type=StringType)
shr5_Zauber_kategorie: Property = Property(name="kategorie", type=StringType)
shr5_Zauber_merkmale: Property = Property(name="merkmale", type=StringType)
shr5_Zauber.attributes={shr5_Zauber_kategorie, shr5_Zauber_entzug, shr5_Zauber_merkmale, shr5_Zauber_dauer, shr5_Zauber_art, shr5_Zauber_reichweite, shr5_Zauber_schaden}

# shr5_ChrakterLimits class attributes and methods
shr5_ChrakterLimits_koerperlich: Property = Property(name="koerperlich", type=IntegerType)
shr5_ChrakterLimits_geistig: Property = Property(name="geistig", type=IntegerType)
shr5_ChrakterLimits_sozial: Property = Property(name="sozial", type=IntegerType)
shr5_ChrakterLimits.attributes={shr5_ChrakterLimits_geistig, shr5_ChrakterLimits_koerperlich, shr5_ChrakterLimits_sozial}

# shr5_Panzerung class attributes and methods
shr5_Panzerung_panzer: Property = Property(name="panzer", type=IntegerType)
shr5_Panzerung.attributes={shr5_Panzerung_panzer}

# shr5_AspektMagier class attributes and methods

# shr5_MetaMagie class attributes and methods

# shr5_CritterKraft class attributes and methods
shr5_CritterKraft_art: Property = Property(name="art", type=StringType)
shr5_CritterKraft_handlung: Property = Property(name="handlung", type=StringType)
shr5_CritterKraft_reichweite: Property = Property(name="reichweite", type=StringType)
shr5_CritterKraft_dauer: Property = Property(name="dauer", type=StringType)
shr5_CritterKraft.attributes={shr5_CritterKraft_handlung, shr5_CritterKraft_reichweite, shr5_CritterKraft_art, shr5_CritterKraft_dauer}

# shr5_Fahrzeug class attributes and methods
shr5_Fahrzeug_beschleunigung: Property = Property(name="beschleunigung", type=IntegerType)
shr5_Fahrzeug_rumpf: Property = Property(name="rumpf", type=IntegerType)
shr5_Fahrzeug_pilot: Property = Property(name="pilot", type=IntegerType)
shr5_Fahrzeug_sensor: Property = Property(name="sensor", type=IntegerType)
shr5_Fahrzeug_fahrzeugTyp: Property = Property(name="fahrzeugTyp", type=StringType)
shr5_Fahrzeug_panzer: Property = Property(name="panzer", type=IntegerType)
shr5_Fahrzeug_weaponMounts: Property = Property(name="weaponMounts", type=IntegerType)
shr5_Fahrzeug_handling: Property = Property(name="handling", type=IntegerType)
shr5_Fahrzeug_geschwindigkeit: Property = Property(name="geschwindigkeit", type=IntegerType)
shr5_Fahrzeug.attributes={shr5_Fahrzeug_sensor, shr5_Fahrzeug_fahrzeugTyp, shr5_Fahrzeug_geschwindigkeit, shr5_Fahrzeug_handling, shr5_Fahrzeug_panzer, shr5_Fahrzeug_weaponMounts, shr5_Fahrzeug_pilot, shr5_Fahrzeug_rumpf, shr5_Fahrzeug_beschleunigung}

# FahrzeugZustand class attributes and methods

# shr5_AstraleProjektion class attributes and methods
shr5_AstraleProjektion_astralesLimit: Property = Property(name="astralesLimit", type=IntegerType)
shr5_AstraleProjektion_astraleKonstitution: Property = Property(name="astraleKonstitution", type=IntegerType)
shr5_AstraleProjektion_astraleGeschicklichkeit: Property = Property(name="astraleGeschicklichkeit", type=IntegerType)
shr5_AstraleProjektion_astraleReaktion: Property = Property(name="astraleReaktion", type=IntegerType)
shr5_AstraleProjektion_astraleStaerke: Property = Property(name="astraleStaerke", type=IntegerType)
shr5_AstraleProjektion_astraleInitative: Property = Property(name="astraleInitative", type=IntegerType)
shr5_AstraleProjektion_astraleInitativWuerfel: Property = Property(name="astraleInitativWuerfel", type=IntegerType)
shr5_AstraleProjektion_astralePanzerung: Property = Property(name="astralePanzerung", type=IntegerType)
shr5_AstraleProjektion.attributes={shr5_AstraleProjektion_astraleInitative, shr5_AstraleProjektion_astraleStaerke, shr5_AstraleProjektion_astralePanzerung, shr5_AstraleProjektion_astraleKonstitution, shr5_AstraleProjektion_astraleInitativWuerfel, shr5_AstraleProjektion_astraleReaktion, shr5_AstraleProjektion_astraleGeschicklichkeit, shr5_AstraleProjektion_astralesLimit}

# shr5_FahrzeugModifikation class attributes and methods
shr5_FahrzeugModifikation_capacityUsed: Property = Property(name="capacityUsed", type=IntegerType)
shr5_FahrzeugModifikation.attributes={shr5_FahrzeugModifikation_capacityUsed}

# shr5_SensorArray class attributes and methods

# shr5_Bodenfahrzeug class attributes and methods
shr5_Bodenfahrzeug_handlingGelaende: Property = Property(name="handlingGelaende", type=IntegerType)
shr5_Bodenfahrzeug_geschwindigkeitGelaende: Property = Property(name="geschwindigkeitGelaende", type=IntegerType)
shr5_Bodenfahrzeug.attributes={shr5_Bodenfahrzeug_geschwindigkeitGelaende, shr5_Bodenfahrzeug_handlingGelaende}

# PassagierFahrzeug class attributes and methods

# shr5_PassagierFahrzeug class attributes and methods
shr5_PassagierFahrzeug_sitze: Property = Property(name="sitze", type=IntegerType)
shr5_PassagierFahrzeug.attributes={shr5_PassagierFahrzeug_sitze}

# Fahrzeug class attributes and methods

# shr5_Drohne class attributes and methods
shr5_Drohne_programSlotCount: Property = Property(name="programSlotCount", type=IntegerType)
shr5_Drohne.attributes={shr5_Drohne_programSlotCount}

# MatrixAttributes class attributes and methods

# shr5_RiggerProgram class attributes and methods

# shr5_Technomancer class attributes and methods

# ResonanzPersona class attributes and methods

# shr5_PersonaKomplexForm class attributes and methods
shr5_PersonaKomplexForm_stufe: Property = Property(name="stufe", type=IntegerType)
shr5_PersonaKomplexForm.attributes={shr5_PersonaKomplexForm_stufe}

# shr5_Echo class attributes and methods

# shr5_ResonanzPersona class attributes and methods
shr5_ResonanzPersona_resonanz: Property = Property(name="resonanz", type=IntegerType)
shr5_ResonanzPersona_resonanzBasis: Property = Property(name="resonanzBasis", type=IntegerType)
shr5_ResonanzPersona.attributes={shr5_ResonanzPersona_resonanzBasis, shr5_ResonanzPersona_resonanz}

# ActiveMatixDevice class attributes and methods

# shr5_KomplexeForm class attributes and methods
shr5_KomplexeForm_ziel: Property = Property(name="ziel", type=StringType)
shr5_KomplexeForm_dauer: Property = Property(name="dauer", type=StringType)
shr5_KomplexeForm_schwund: Property = Property(name="schwund", type=StringType)
shr5_KomplexeForm.attributes={shr5_KomplexeForm_dauer, shr5_KomplexeForm_schwund, shr5_KomplexeForm_ziel}

# shr5_Sprite class attributes and methods
shr5_Sprite_stufe: Property = Property(name="stufe", type=IntegerType)
shr5_Sprite_angriffMod: Property = Property(name="angriffMod", type=IntegerType)
shr5_Sprite_schleicherMod: Property = Property(name="schleicherMod", type=IntegerType)
shr5_Sprite_datenverarbeitungMod: Property = Property(name="datenverarbeitungMod", type=IntegerType)
shr5_Sprite_firewallMod: Property = Property(name="firewallMod", type=IntegerType)
shr5_Sprite_initativeMod: Property = Property(name="initativeMod", type=IntegerType)
shr5_Sprite.attributes={shr5_Sprite_firewallMod, shr5_Sprite_datenverarbeitungMod, shr5_Sprite_initativeMod, shr5_Sprite_schleicherMod, shr5_Sprite_angriffMod, shr5_Sprite_stufe}

# shr5_Vertrag class attributes and methods

# shr5_Lifestyle class attributes and methods
shr5_Lifestyle_owned: Property = Property(name="owned", type=BooleanType)
shr5_Lifestyle.attributes={shr5_Lifestyle_owned}

# IntervallVertrag class attributes and methods

# shr5_LifestyleOption class attributes and methods

# shr5_Wissensfertigkeit class attributes and methods

# Fertigkeit class attributes and methods

# shr5_Sprachfertigkeit class attributes and methods

# Wissensfertigkeit class attributes and methods

# shr5_PersonaZustand class attributes and methods
shr5_PersonaZustand_zustandKoerperlichMax: Property = Property(name="zustandKoerperlichMax", type=IntegerType)
shr5_PersonaZustand_zustandGeistigMax: Property = Property(name="zustandGeistigMax", type=IntegerType)
shr5_PersonaZustand_zustandGrenze: Property = Property(name="zustandGrenze", type=IntegerType)
shr5_PersonaZustand.attributes={shr5_PersonaZustand_zustandGrenze, shr5_PersonaZustand_zustandKoerperlichMax, shr5_PersonaZustand_zustandGeistigMax}

# shr5_Critter class attributes and methods

# Spezies class attributes and methods

# shr5_IntervallVertrag class attributes and methods
shr5_IntervallVertrag_unit: Property = Property(name="unit", type=StringType)
shr5_IntervallVertrag_begin: Property = Property(name="begin", type=StringType)
shr5_IntervallVertrag_faelligkeitsIntervall: Property = Property(name="faelligkeitsIntervall", type=IntegerType)
shr5_IntervallVertrag.attributes={shr5_IntervallVertrag_faelligkeitsIntervall, shr5_IntervallVertrag_unit, shr5_IntervallVertrag_begin}

# Vertrag class attributes and methods

# shr5_Sin class attributes and methods

# Fakeable class attributes and methods

# shr5_Lizenz class attributes and methods
shr5_Lizenz_lizenGegenstand: Property = Property(name="lizenGegenstand", type=StringType)
shr5_Lizenz.attributes={shr5_Lizenz_lizenGegenstand}

# shr5_Fakeable class attributes and methods
shr5_Fakeable_stufe: Property = Property(name="stufe", type=IntegerType)
shr5_Fakeable_gefaelscht: Property = Property(name="gefaelscht", type=BooleanType)
shr5_Fakeable.attributes={shr5_Fakeable_gefaelscht, shr5_Fakeable_stufe}

# shr5_Steigerbar class attributes and methods
shr5_Steigerbar_stufe: Property = Property(name="stufe", type=IntegerType)
shr5_Steigerbar.attributes={shr5_Steigerbar_stufe}

# shr5_Erlernbar class attributes and methods

# shr5_Credstick class attributes and methods
shr5_Credstick_maxValue: Property = Property(name="maxValue", type=IntegerType)
shr5_Credstick_currentValue: Property = Property(name="currentValue", type=StringType)
shr5_Credstick.attributes={shr5_Credstick_currentValue, shr5_Credstick_maxValue}

# shr5_CredstickTransaction class attributes and methods
shr5_CredstickTransaction_amount: Property = Property(name="amount", type=StringType)
shr5_CredstickTransaction_date: Property = Property(name="date", type=StringType)
shr5_CredstickTransaction_description: Property = Property(name="description", type=StringType)
shr5_CredstickTransaction.attributes={shr5_CredstickTransaction_date, shr5_CredstickTransaction_description, shr5_CredstickTransaction_amount}

# shr5_Menge class attributes and methods
shr5_Menge_anzahl: Property = Property(name="anzahl", type=IntegerType)
shr5_Menge_proAnzahl: Property = Property(name="proAnzahl", type=IntegerType)
shr5_Menge.attributes={shr5_Menge_proAnzahl, shr5_Menge_anzahl}

# shr5_Munition class attributes and methods
shr5_Munition_damageType: Property = Property(name="damageType", type=StringType)
shr5_Munition_damageMod: Property = Property(name="damageMod", type=IntegerType)
shr5_Munition_armorMod: Property = Property(name="armorMod", type=IntegerType)
shr5_Munition.attributes={shr5_Munition_damageMod, shr5_Munition_damageType, shr5_Munition_armorMod}

# shr5_ModifikatorAttribute class attributes and methods

# shr5_Geist class attributes and methods
shr5_Geist_intuitionBasis: Property = Property(name="intuitionBasis", type=IntegerType)
shr5_Geist_logikBasis: Property = Property(name="logikBasis", type=IntegerType)
shr5_Geist_konstitutionBasis: Property = Property(name="konstitutionBasis", type=IntegerType)
shr5_Geist_geschicklichkeitBasis: Property = Property(name="geschicklichkeitBasis", type=IntegerType)
shr5_Geist_reaktionBasis: Property = Property(name="reaktionBasis", type=IntegerType)
shr5_Geist_staerkeBasis: Property = Property(name="staerkeBasis", type=IntegerType)
shr5_Geist_charismaBasis: Property = Property(name="charismaBasis", type=IntegerType)
shr5_Geist_willenskraftBasis: Property = Property(name="willenskraftBasis", type=IntegerType)
shr5_Geist.attributes={shr5_Geist_intuitionBasis, shr5_Geist_willenskraftBasis, shr5_Geist_logikBasis, shr5_Geist_reaktionBasis, shr5_Geist_staerkeBasis, shr5_Geist_charismaBasis, shr5_Geist_konstitutionBasis, shr5_Geist_geschicklichkeitBasis}

# shr5_StufenPersona class attributes and methods
shr5_StufenPersona_stufe: Property = Property(name="stufe", type=IntegerType)
shr5_StufenPersona.attributes={shr5_StufenPersona_stufe}

# StufenPersona class attributes and methods

# shr5_Identifiable class attributes and methods
shr5_Identifiable_parentId: Property = Property(name="parentId", type=StringType)
shr5_Identifiable.attributes={shr5_Identifiable_parentId}

# shr5_Localization class attributes and methods
shr5_Localization_local: Property = Property(name="local", type=StringType)
shr5_Localization_name: Property = Property(name="name", type=StringType)
shr5_Localization_page: Property = Property(name="page", type=IntegerType)
shr5_Localization.attributes={shr5_Localization_name, shr5_Localization_page, shr5_Localization_local}

# shr5_MatrixAttributes class attributes and methods
shr5_MatrixAttributes_geraetestufe: Property = Property(name="geraetestufe", type=IntegerType)
shr5_MatrixAttributes_firewall: Property = Property(name="firewall", type=IntegerType)
shr5_MatrixAttributes_datenverarbeitung: Property = Property(name="datenverarbeitung", type=IntegerType)
shr5_MatrixAttributes_currentModus: Property = Property(name="currentModus", type=StringType)
shr5_MatrixAttributes.attributes={shr5_MatrixAttributes_firewall, shr5_MatrixAttributes_currentModus, shr5_MatrixAttributes_geraetestufe, shr5_MatrixAttributes_datenverarbeitung}

# MatixConditionMonitor class attributes and methods

# shr5_ActiveMatixDevice class attributes and methods
shr5_ActiveMatixDevice_angriff: Property = Property(name="angriff", type=IntegerType)
shr5_ActiveMatixDevice_schleicher: Property = Property(name="schleicher", type=IntegerType)
shr5_ActiveMatixDevice.attributes={shr5_ActiveMatixDevice_schleicher, shr5_ActiveMatixDevice_angriff}

# shr5_Commlink class attributes and methods

# AbstractMatrixDevice class attributes and methods

# shr5_BasicProgram class attributes and methods

# shr5_MatixConditionMonitor class attributes and methods
shr5_MatixConditionMonitor_matrixZustandMax: Property = Property(name="matrixZustandMax", type=IntegerType)
shr5_MatixConditionMonitor.attributes={shr5_MatixConditionMonitor_matrixZustandMax}

# shr5_Cyberdeck class attributes and methods
shr5_Cyberdeck_programSlots: Property = Property(name="programSlots", type=IntegerType)
shr5_Cyberdeck_attribute1: Property = Property(name="attribute1", type=IntegerType)
shr5_Cyberdeck_attribute2: Property = Property(name="attribute2", type=IntegerType)
shr5_Cyberdeck_attribute3: Property = Property(name="attribute3", type=IntegerType)
shr5_Cyberdeck_attribute4: Property = Property(name="attribute4", type=IntegerType)
shr5_Cyberdeck_modManager: Property = Property(name="modManager", type=StringType)
shr5_Cyberdeck.attributes={shr5_Cyberdeck_attribute1, shr5_Cyberdeck_modManager, shr5_Cyberdeck_programSlots, shr5_Cyberdeck_attribute2, shr5_Cyberdeck_attribute4, shr5_Cyberdeck_attribute3}

# MatrixDevice class attributes and methods

# shr5_MatrixProgram class attributes and methods

# shr5_SoftwareAgent class attributes and methods
shr5_SoftwareAgent_rating: Property = Property(name="rating", type=IntegerType)
shr5_SoftwareAgent.attributes={shr5_SoftwareAgent_rating}

# MatrixProgram class attributes and methods

# shr5_Host class attributes and methods
shr5_Host_hostRating: Property = Property(name="hostRating", type=IntegerType)
shr5_Host_baseFirewall: Property = Property(name="baseFirewall", type=IntegerType)
shr5_Host_baseDatenverarbeitung: Property = Property(name="baseDatenverarbeitung", type=IntegerType)
shr5_Host_baseAngriff: Property = Property(name="baseAngriff", type=IntegerType)
shr5_Host_baseSchleicher: Property = Property(name="baseSchleicher", type=IntegerType)
shr5_Host.attributes={shr5_Host_hostRating, shr5_Host_baseFirewall, shr5_Host_baseAngriff, shr5_Host_baseDatenverarbeitung, shr5_Host_baseSchleicher}

# shr5_CyberwareModifikatioren class attributes and methods
shr5_CyberwareModifikatioren_simRig: Property = Property(name="simRig", type=IntegerType)
shr5_CyberwareModifikatioren_riggerInterface: Property = Property(name="riggerInterface", type=BooleanType)
shr5_CyberwareModifikatioren_directNeuralInterface: Property = Property(name="directNeuralInterface", type=BooleanType)
shr5_CyberwareModifikatioren_universalDataConnector: Property = Property(name="universalDataConnector", type=BooleanType)
shr5_CyberwareModifikatioren_controlRig: Property = Property(name="controlRig", type=IntegerType)
shr5_CyberwareModifikatioren.attributes={shr5_CyberwareModifikatioren_riggerInterface, shr5_CyberwareModifikatioren_simRig, shr5_CyberwareModifikatioren_directNeuralInterface, shr5_CyberwareModifikatioren_controlRig, shr5_CyberwareModifikatioren_universalDataConnector}

# shr5_RiggerCommandConsole class attributes and methods
shr5_RiggerCommandConsole_rauschunterdrueckung: Property = Property(name="rauschunterdrueckung", type=IntegerType)
shr5_RiggerCommandConsole_zugriff: Property = Property(name="zugriff", type=IntegerType)
shr5_RiggerCommandConsole_datenverarbeitungBasis: Property = Property(name="datenverarbeitungBasis", type=IntegerType)
shr5_RiggerCommandConsole_firewallBasis: Property = Property(name="firewallBasis", type=IntegerType)
shr5_RiggerCommandConsole_zugriffBasis: Property = Property(name="zugriffBasis", type=IntegerType)
shr5_RiggerCommandConsole.attributes={shr5_RiggerCommandConsole_zugriff, shr5_RiggerCommandConsole_datenverarbeitungBasis, shr5_RiggerCommandConsole_rauschunterdrueckung, shr5_RiggerCommandConsole_zugriffBasis, shr5_RiggerCommandConsole_firewallBasis}

# shr5_AutoSoft class attributes and methods
shr5_AutoSoft_rating: Property = Property(name="rating", type=IntegerType)
shr5_AutoSoft.attributes={shr5_AutoSoft_rating}

# RiggerProgram class attributes and methods

# shr5_Software class attributes and methods

# Software class attributes and methods

# shr5_Tutorsoft class attributes and methods
shr5_Tutorsoft_rating: Property = Property(name="rating", type=IntegerType)
shr5_Tutorsoft.attributes={shr5_Tutorsoft_rating}

# BasicProgram class attributes and methods

# shr5_SkillSoft class attributes and methods
shr5_SkillSoft_rating: Property = Property(name="rating", type=IntegerType)
shr5_SkillSoft.attributes={shr5_SkillSoft_rating}

# shr5_PersonalAreaNetwork class attributes and methods
shr5_PersonalAreaNetwork_slaveMax: Property = Property(name="slaveMax", type=IntegerType)
shr5_PersonalAreaNetwork.attributes={shr5_PersonalAreaNetwork_slaveMax}

# shr5_Datasoft class attributes and methods

# shr5_AbstractMatrixDevice class attributes and methods
shr5_AbstractMatrixDevice_deviceRating: Property = Property(name="deviceRating", type=IntegerType)
shr5_AbstractMatrixDevice.attributes={shr5_AbstractMatrixDevice_deviceRating}

# shr5_ConsumerSoft class attributes and methods
shr5_ConsumerSoft_type: Property = Property(name="type", type=StringType)
shr5_ConsumerSoft.attributes={shr5_ConsumerSoft_type}

# shr5_CommonProgram class attributes and methods
shr5_CommonProgram_programType: Property = Property(name="programType", type=StringType)
shr5_CommonProgram.attributes={shr5_CommonProgram_programType}

# shr5_WeaponMount class attributes and methods

# FahrzeugModifikation class attributes and methods

# shr5_PercentLifestyleOption class attributes and methods

# LifestyleOption class attributes and methods

# shr5_FahrzeugZustand class attributes and methods
shr5_FahrzeugZustand_zustandMax: Property = Property(name="zustandMax", type=IntegerType)
shr5_FahrzeugZustand.attributes={shr5_FahrzeugZustand_zustandMax}

# shr5_MagischeStufe class attributes and methods
shr5_MagischeStufe_stufe: Property = Property(name="stufe", type=IntegerType)
shr5_MagischeStufe.attributes={shr5_MagischeStufe_stufe}

# shr5_Fokus class attributes and methods
shr5_Fokus_bindungskosten: Property = Property(name="bindungskosten", type=IntegerType)
shr5_Fokus.attributes={shr5_Fokus_bindungskosten}

# MagischeStufe class attributes and methods

# shr5_AbstraktFokus class attributes and methods

# Fokus class attributes and methods

# shr5_QiFokus class attributes and methods

# AbstraktFokus class attributes and methods

# shr5_WaffenFokus class attributes and methods

# Nahkampfwaffe class attributes and methods

# shr5_MagieFokus class attributes and methods
shr5_MagieFokus_bindungsFaktor: Property = Property(name="bindungsFaktor", type=IntegerType)
shr5_MagieFokus.attributes={shr5_MagieFokus_bindungsFaktor}

# shr5_Substance class attributes and methods
shr5_Substance_vector: Property = Property(name="vector", type=StringType)
shr5_Substance_speed: Property = Property(name="speed", type=StringType)
shr5_Substance.attributes={shr5_Substance_vector, shr5_Substance_speed}

# shr5_Toxin class attributes and methods
shr5_Toxin_power: Property = Property(name="power", type=IntegerType)
shr5_Toxin_penetration: Property = Property(name="penetration", type=IntegerType)
shr5_Toxin_effect: Property = Property(name="effect", type=StringType)
shr5_Toxin.attributes={shr5_Toxin_effect, shr5_Toxin_power, shr5_Toxin_penetration}

# Substance class attributes and methods

# shr5_BerechneteAttribute class attributes and methods
shr5_BerechneteAttribute_menschenkenntnis: Property = Property(name="menschenkenntnis", type=IntegerType)
shr5_BerechneteAttribute_selbstbeherrschung: Property = Property(name="selbstbeherrschung", type=IntegerType)
shr5_BerechneteAttribute_errinerungsvermoegen: Property = Property(name="errinerungsvermoegen", type=IntegerType)
shr5_BerechneteAttribute.attributes={shr5_BerechneteAttribute_menschenkenntnis, shr5_BerechneteAttribute_errinerungsvermoegen, shr5_BerechneteAttribute_selbstbeherrschung}

# shr5_SubstanceContainer class attributes and methods

# shr5_Capacity class attributes and methods
shr5_Capacity_capacity: Property = Property(name="capacity", type=IntegerType)
shr5_Capacity_capacityRemains: Property = Property(name="capacityRemains", type=IntegerType)
shr5_Capacity_m_canAdd: Method = Method(name="canAdd", parameters={Parameter(name='object')}, type=BooleanType)
shr5_Capacity.attributes={shr5_Capacity_capacityRemains, shr5_Capacity_capacity}
shr5_Capacity.methods={shr5_Capacity_m_canAdd}

# shr5_EReference class attributes and methods

# shr5_Drug class attributes and methods
shr5_Drug_addictionType: Property = Property(name="addictionType", type=StringType)
shr5_Drug_duration: Property = Property(name="duration", type=StringType)
shr5_Drug.attributes={shr5_Drug_duration, shr5_Drug_addictionType}

# shr5_CyberImplantWeapon class attributes and methods

# CyberwareEnhancement class attributes and methods

# shr5_ShoppingTransaction class attributes and methods
shr5_ShoppingTransaction_fee: Property = Property(name="fee", type=FloatType)
shr5_ShoppingTransaction_caculatedCosts: Property = Property(name="caculatedCosts", type=StringType)
shr5_ShoppingTransaction.attributes={shr5_ShoppingTransaction_caculatedCosts, shr5_ShoppingTransaction_fee}

# CredstickTransaction class attributes and methods

# shr5_TransferAmount class attributes and methods
shr5_TransferAmount_amountToTransfer: Property = Property(name="amountToTransfer", type=StringType)
shr5_TransferAmount.attributes={shr5_TransferAmount_amountToTransfer}

# shr5_Sensor class attributes and methods
shr5_Sensor_rating: Property = Property(name="rating", type=IntegerType)
shr5_Sensor_capacityValue: Property = Property(name="capacityValue", type=IntegerType)
shr5_Sensor.attributes={shr5_Sensor_rating, shr5_Sensor_capacityValue}

# shr5_SensorFunction class attributes and methods
shr5_SensorFunction_maxRange: Property = Property(name="maxRange", type=IntegerType)
shr5_SensorFunction.attributes={shr5_SensorFunction_maxRange}

# Sensor class attributes and methods

# shr5_MartialartStyle class attributes and methods

# shr5_MartialartTechnique class attributes and methods

# Spezialisierung class attributes and methods

# shr5_PersonaMartialartTechnique class attributes and methods

# shr5_FahrzeugErweiterung class attributes and methods

# shr5_AbtraktGranate class attributes and methods
shr5_AbtraktGranate_blast: Property = Property(name="blast", type=StringType)
shr5_AbtraktGranate.attributes={shr5_AbtraktGranate_blast}

# shr5_MiniGrenate class attributes and methods

# Munition class attributes and methods

# AbtraktGranate class attributes and methods

# shr5_Granate class attributes and methods

# Wurfwaffe class attributes and methods

# shr5_SourceLink class attributes and methods

# Relationships
srcBook0: BinaryAssociation = BinaryAssociation(
    name="srcBook0",
    ends={
        Property(name="shr5_SourceBook", type=shr5_Quelle, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5_Quelle", type=shr5_SourceBook, multiplicity=Multiplicity(0, 1))
    }
)
fertigkeiten1: BinaryAssociation = BinaryAssociation(
    name="fertigkeiten1",
    ends={
        Property(name="shr5_PersonaFertigkeit", type=shr5_AbstraktPersona, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5_AbstraktPersona", type=shr5_PersonaFertigkeit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fertigkeitsGruppen2: BinaryAssociation = BinaryAssociation(
    name="fertigkeitsGruppen2",
    ends={
        Property(name="shr5_PersonaFertigkeitsGruppe", type=shr5_AbstraktPersona, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5_AbstraktPersona3", type=shr5_PersonaFertigkeitsGruppe, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
spezies4: BinaryAssociation = BinaryAssociation(
    name="spezies4",
    ends={
        Property(name="shr5_Spezies", type=shr5_AbstraktPersona, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5_AbstraktPersona5", type=shr5_Spezies, multiplicity=Multiplicity(1, 1))
    }
)
martialartStyles6: BinaryAssociation = BinaryAssociation(
    name="martialartStyles6",
    ends={
        Property(name="shr5_PersonaMartialartStyle", type=shr5_AbstraktPersona, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5_AbstraktPersona7", type=shr5_PersonaMartialartStyle, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attribut8: BinaryAssociation = BinaryAssociation(
    name="attribut8",
    ends={
        Property(name="shr5_EAttribute", type=shr5_AttributModifikatorWert, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5_AttributModifikatorWert", type=shr5_EAttribute, multiplicity=Multiplicity(0, 1))
    }
)
modifiziertes9: BinaryAssociation = BinaryAssociation(
    name="modifiziertes9",
    ends={
        Property(name="Modifizierbar", type=shr5_AttributModifikatorWert, multiplicity=Multiplicity(1, 1)),
        Property(name="mods", type=shr5_Modifizierbar, multiplicity=Multiplicity(0, 1))
    }
)
modifyable10: BinaryAssociation = BinaryAssociation(
    name="modifyable10",
    ends={
        Property(name="shr5_Modifyable", type=shr5_AttributModifikatorWert, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5_AttributModifikatorWert11", type=shr5_Modifyable, multiplicity=Multiplicity(0, 1))
    }
)
mods12: BinaryAssociation = BinaryAssociation(
    name="mods12",
    ends={
        Property(name="AttributModifikatorWert", type=shr5_Modifizierbar, multiplicity=Multiplicity(1, 1)),
        Property(name="modifiziertes", type=shr5_AttributModifikatorWert, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
wifi13: BinaryAssociation = BinaryAssociation(
    name="wifi13",
    ends={
        Property(name="shr5_MatrixDevice", type=shr5_AbstraktGegenstand, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5_AbstraktGegenstand", type=shr5_MatrixDevice, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
reichweite14: BinaryAssociation = BinaryAssociation(
    name="reichweite14",
    ends={
        Property(name="shr5_Reichweite", type=shr5_AbstaktFernKampfwaffe, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5_AbstaktFernKampfwaffe", type=shr5_Reichweite, multiplicity=Multiplicity(1, 1))
    }
)
einbau15: BinaryAssociation = BinaryAssociation(
    name="einbau15",
    ends={
        Property(name="shr5_FernkampfwaffeModifikator", type=shr5_Feuerwaffe, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5_Feuerwaffe", type=shr5_FernkampfwaffeModifikator, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
magazin16: BinaryAssociation = BinaryAssociation(
    name="magazin16",
    ends={
        Property(name="shr5_Magazin", type=shr5_Feuerwaffe, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5_Feuerwaffe17", type=shr5_Magazin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entries18: BinaryAssociation = BinaryAssociation(
    name="entries18",
    ends={
        Property(name="shr5_EObject", type=shr5_ShrList, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5_ShrList", type=shr5_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fertigkeiten19: BinaryAssociation = BinaryAssociation(
    name="fertigkeiten19",
    ends={
        Property(name="shr5_Fertigkeit", type=shr5_FertigkeitsGruppe, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5_FertigkeitsGruppe", type=shr5_Fertigkeit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attribut20: BinaryAssociation = BinaryAssociation(
    name="attribut20",
    ends={
        Property(name="shr5_EAttribute22", type=shr5_Fertigkeit, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5_Fertigkeit21", type=shr5_EAttribute, multiplicity=Multiplicity(0, 1))
    }
)
spezialisierungen23: BinaryAssociation = BinaryAssociation(
    name="spezialisierungen23",
    ends={
        Property(name="Spezialisierung", type=shr5_Fertigkeit, multiplicity=Multiplicity(1, 1)),
        Property(name="fertigkeit", type=shr5_Spezialisierung, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fertigkeit24: BinaryAssociation = BinaryAssociation(
    name="fertigkeit24",
    ends={
        Property(name="shr5_Fertigkeit26", type=shr5_PersonaFertigkeit, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5_PersonaFertigkeit25", type=shr5_Fertigkeit, multiplicity=Multiplicity(0, 1))
    }
)
spezialisierungen27: BinaryAssociation = BinaryAssociation(
    name="spezialisierungen27",
    ends={
        Property(name="shr5_Spezialisierung", type=shr5_PersonaFertigkeit, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5_PersonaFertigkeit28", type=shr5_Spezialisierung, multiplicity=Multiplicity(0, 9999))
    }
)
gruppe29: BinaryAssociation = BinaryAssociation(
    name="gruppe29",
    ends={
        Property(name="shr5_FertigkeitsGruppe31", type=shr5_PersonaFertigkeitsGruppe, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5_PersonaFertigkeitsGruppe30", type=shr5_FertigkeitsGruppe, multiplicity=Multiplicity(0, 1))
    }
)
persona32: BinaryAssociation = BinaryAssociation(
    name="persona32",
    ends={
        Property(name="shr5_AbstraktPersona33", type=shr5_Cyberware, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5_Cyberware", type=shr5_AbstraktPersona, multiplicity=Multiplicity(0, 1))
    }
)
einbau34: BinaryAssociation = BinaryAssociation(
    name="einbau34",
    ends={
        Property(name="shr5_CyberwareEnhancement", type=shr5_Cyberware, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5_Cyberware35", type=shr5_CyberwareEnhancement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
wifi36: BinaryAssociation = BinaryAssociation(
    name="wifi36",
    ends={
        Property(name="shr5_DefaultWifi", type=shr5_Cyberware, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5_Cyberware37", type=shr5_DefaultWifi, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
koerperMods40: BinaryAssociation = BinaryAssociation(
    name="koerperMods40",
    ends={
        Property(name="shr5_Koerpermods", type=shr5_KoerperPersona, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5_KoerperPersona", type=shr5_Koerpermods, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eigenschaften41: BinaryAssociation = BinaryAssociation(
    name="eigenschaften41",
    ends={
        Property(name="shr5_PersonaEigenschaft", type=shr5_KoerperPersona, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5_KoerperPersona42", type=shr5_PersonaEigenschaft, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mentor43: BinaryAssociation = BinaryAssociation(
    name="mentor43",
    ends={
        Property(name="shr5_Schutzgeist", type=shr5_MagischePersona, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5_MagischePersona", type=shr5_Schutzgeist, multiplicity=Multiplicity(0, 1))
    }
)
initationen44: BinaryAssociation = BinaryAssociation(
    name="initationen44",
    ends={
        Property(name="shr5_Initation", type=shr5_BaseMagischePersona, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5_BaseMagischePersona", type=shr5_Initation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
boundFoki45: BinaryAssociation = BinaryAssociation(
    name="boundFoki45",
    ends={
        Property(name="shr5_FokusBinding", type=shr5_BaseMagischePersona, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5_BaseMagischePersona46", type=shr5_FokusBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
persona38: BinaryAssociation = BinaryAssociation(
    name="persona38",
    ends={
        Property(name="shr5_AbstraktPersona39", type=shr5_BioWare, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5_BioWare", type=shr5_AbstraktPersona, multiplicity=Multiplicity(0, 1))
    }
)
angriff47: BinaryAssociation = BinaryAssociation(
    name="angriff47",
    ends={
        Property(name="shr5_Nahkampfwaffe", type=shr5_Spezies, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5_Spezies48", type=shr5_Nahkampfwaffe, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
kikraft49: BinaryAssociation = BinaryAssociation(
    name="kikraft49",
    ends={
        Property(name="shr5_KiKraft", type=shr5_KiAdept, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5_KiAdept", type=shr5_KiKraft, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
kmods50: BinaryAssociation = BinaryAssociation(
    name="kmods50",
    ends={
        Property(name="shr5_KleindungsModifikator", type=shr5_Kleidung, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5_Kleidung", type=shr5_KleindungsModifikator, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fertigkeit51: BinaryAssociation = BinaryAssociation(
    name="fertigkeit51",
    ends={
        Property(name="shr5_Fertigkeit52", type=shr5_Anwendbar, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5_Anwendbar", type=shr5_Fertigkeit, multiplicity=Multiplicity(0, 1))
    }
)
spezialisierung53: BinaryAssociation = BinaryAssociation(
    name="spezialisierung53",
    ends={
        Property(name="shr5_Spezialisierung55", type=shr5_Anwendbar, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5_Anwendbar54", type=shr5_Spezialisierung, multiplicity=Multiplicity(0, 1))
    }
)
zauber56: BinaryAssociation = BinaryAssociation(
    name="zauber56",
    ends={
        Property(name="shr5_PersonaZauber", type=shr5_Zauberer, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5_Zauberer", type=shr5_PersonaZauber, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
gebundeneGeister57: BinaryAssociation = BinaryAssociation(
    name="gebundeneGeister57",
    ends={
        Property(name="shr5_GebundenerGeist", type=shr5_Zauberer, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5_Zauberer58", type=shr5_GebundenerGeist, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ungebundenerGeist59: BinaryAssociation = BinaryAssociation(
    name="ungebundenerGeist59",
    ends={
        Property(name="shr5_GebundenerGeist61", type=shr5_Zauberer, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5_Zauberer60", type=shr5_GebundenerGeist, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tradition62: BinaryAssociation = BinaryAssociation(
    name="tradition62",
    ends={
        Property(name="shr5_MagischeTradition", type=shr5_Zauberer, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5_Zauberer63", type=shr5_MagischeTradition, multiplicity=Multiplicity(1, 1))
    }
)
formel64: BinaryAssociation = BinaryAssociation(
    name="formel64",
    ends={
        Property(name="shr5_Zauber", type=shr5_PersonaZauber, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5_PersonaZauber65", type=shr5_Zauber, multiplicity=Multiplicity(1, 1))
    }
)
aspekt66: BinaryAssociation = BinaryAssociation(
    name="aspekt66",
    ends={
        Property(name="shr5_FertigkeitsGruppe67", type=shr5_AspektMagier, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5_AspektMagier", type=shr5_FertigkeitsGruppe, multiplicity=Multiplicity(1, 1))
    }
)
erlernt68: BinaryAssociation = BinaryAssociation(
    name="erlernt68",
    ends={
        Property(name="shr5_MetaMagie", type=shr5_Initation, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5_Initation69", type=shr5_MetaMagie, multiplicity=Multiplicity(0, 1))
    }
)
modifizierungen70: BinaryAssociation = BinaryAssociation(
    name="modifizierungen70",
    ends={
        Property(name="shr5_FahrzeugModifikation", type=shr5_Fahrzeug, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5_Fahrzeug", type=shr5_FahrzeugModifikation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sensorArray71: BinaryAssociation = BinaryAssociation(
    name="sensorArray71",
    ends={
        Property(name="shr5_SensorArray", type=shr5_Fahrzeug, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5_Fahrzeug72", type=shr5_SensorArray, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
runningPrograms73: BinaryAssociation = BinaryAssociation(
    name="runningPrograms73",
    ends={
        Property(name="shr5_RiggerProgram", type=shr5_Drohne, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5_Drohne", type=shr5_RiggerProgram, multiplicity=Multiplicity(0, 9999))
    }
)
storedPrograms74: BinaryAssociation = BinaryAssociation(
    name="storedPrograms74",
    ends={
        Property(name="shr5_RiggerProgram76", type=shr5_Drohne, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5_Drohne75", type=shr5_RiggerProgram, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
complexForms77: BinaryAssociation = BinaryAssociation(
    name="complexForms77",
    ends={
        Property(name="shr5_PersonaKomplexForm", type=shr5_Technomancer, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5_Technomancer", type=shr5_PersonaKomplexForm, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
echos78: BinaryAssociation = BinaryAssociation(
    name="echos78",
    ends={
        Property(name="shr5_Echo", type=shr5_Technomancer, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5_Technomancer79", type=shr5_Echo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
form80: BinaryAssociation = BinaryAssociation(
    name="form80",
    ends={
        Property(name="shr5_KomplexeForm", type=shr5_PersonaKomplexForm, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5_PersonaKomplexForm81", type=shr5_KomplexeForm, multiplicity=Multiplicity(1, 1))
    }
)
options82: BinaryAssociation = BinaryAssociation(
    name="options82",
    ends={
        Property(name="shr5_LifestyleOption", type=shr5_Lifestyle, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5_Lifestyle", type=shr5_LifestyleOption, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
powers83: BinaryAssociation = BinaryAssociation(
    name="powers83",
    ends={
        Property(name="shr5_CritterKraft", type=shr5_Critter, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5_Critter", type=shr5_CritterKraft, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
licences84: BinaryAssociation = BinaryAssociation(
    name="licences84",
    ends={
        Property(name="Lizenz", type=shr5_Sin, multiplicity=Multiplicity(1, 1)),
        Property(name="lizenzTraeger", type=shr5_Lizenz, multiplicity=Multiplicity(0, 9999))
    }
)
lizenzTraeger85: BinaryAssociation = BinaryAssociation(
    name="lizenzTraeger85",
    ends={
        Property(name="Sin", type=shr5_Lizenz, multiplicity=Multiplicity(1, 1)),
        Property(name="licences", type=shr5_Sin, multiplicity=Multiplicity(1, 1))
    }
)
transactionlog86: BinaryAssociation = BinaryAssociation(
    name="transactionlog86",
    ends={
        Property(name="shr5_CredstickTransaction", type=shr5_Credstick, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5_Credstick", type=shr5_CredstickTransaction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type87: BinaryAssociation = BinaryAssociation(
    name="type87",
    ends={
        Property(name="shr5_Reichweite88", type=shr5_Munition, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5_Munition", type=shr5_Reichweite, multiplicity=Multiplicity(1, 1))
    }
)
geist89: BinaryAssociation = BinaryAssociation(
    name="geist89",
    ends={
        Property(name="shr5_Geist", type=shr5_GebundenerGeist, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5_GebundenerGeist90", type=shr5_Geist, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
skillGroups91: BinaryAssociation = BinaryAssociation(
    name="skillGroups91",
    ends={
        Property(name="shr5_FertigkeitsGruppe92", type=shr5_StufenPersona, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5_StufenPersona", type=shr5_FertigkeitsGruppe, multiplicity=Multiplicity(0, 9999))
    }
)
skills93: BinaryAssociation = BinaryAssociation(
    name="skills93",
    ends={
        Property(name="shr5_Fertigkeit95", type=shr5_StufenPersona, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5_StufenPersona94", type=shr5_Fertigkeit, multiplicity=Multiplicity(0, 9999))
    }
)
powers96: BinaryAssociation = BinaryAssociation(
    name="powers96",
    ends={
        Property(name="shr5_CritterKraft98", type=shr5_Geist, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5_Geist97", type=shr5_CritterKraft, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
optionalPowers99: BinaryAssociation = BinaryAssociation(
    name="optionalPowers99",
    ends={
        Property(name="shr5_CritterKraft101", type=shr5_Geist, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5_Geist100", type=shr5_CritterKraft, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
localizations102: BinaryAssociation = BinaryAssociation(
    name="localizations102",
    ends={
        Property(name="shr5_Localization", type=shr5_Identifiable, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5_Identifiable", type=shr5_Localization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fertigkeit103: BinaryAssociation = BinaryAssociation(
    name="fertigkeit103",
    ends={
        Property(name="Fertigkeit", type=shr5_Spezialisierung, multiplicity=Multiplicity(1, 1)),
        Property(name="spezialisierungen", type=shr5_Fertigkeit, multiplicity=Multiplicity(0, 1))
    }
)
storedPrograms104: BinaryAssociation = BinaryAssociation(
    name="storedPrograms104",
    ends={
        Property(name="shr5_BasicProgram", type=shr5_Commlink, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5_Commlink", type=shr5_BasicProgram, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
configuration107: BinaryAssociation = BinaryAssociation(
    name="configuration107",
    ends={
        Property(name="shr5_EAttribute108", type=shr5_Cyberdeck, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5_Cyberdeck", type=shr5_EAttribute, multiplicity=Multiplicity(4, 4))
    }
)
storedPrograms109: BinaryAssociation = BinaryAssociation(
    name="storedPrograms109",
    ends={
        Property(name="shr5_MatrixProgram", type=shr5_Cyberdeck, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5_Cyberdeck110", type=shr5_MatrixProgram, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
runningPrograms111: BinaryAssociation = BinaryAssociation(
    name="runningPrograms111",
    ends={
        Property(name="shr5_MatrixProgram113", type=shr5_Cyberdeck, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5_Cyberdeck112", type=shr5_MatrixProgram, multiplicity=Multiplicity(0, 9999))
    }
)
storedSins105: BinaryAssociation = BinaryAssociation(
    name="storedSins105",
    ends={
        Property(name="shr5_Sin", type=shr5_Commlink, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5_Commlink106", type=shr5_Sin, multiplicity=Multiplicity(0, 9999))
    }
)
storedPrograms114: BinaryAssociation = BinaryAssociation(
    name="storedPrograms114",
    ends={
        Property(name="shr5_RiggerProgram115", type=shr5_RiggerCommandConsole, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5_RiggerCommandConsole", type=shr5_RiggerProgram, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
runningPrograms116: BinaryAssociation = BinaryAssociation(
    name="runningPrograms116",
    ends={
        Property(name="shr5_RiggerProgram118", type=shr5_RiggerCommandConsole, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5_RiggerCommandConsole117", type=shr5_RiggerProgram, multiplicity=Multiplicity(0, 9999))
    }
)
skill119: BinaryAssociation = BinaryAssociation(
    name="skill119",
    ends={
        Property(name="shr5_Fertigkeit120", type=shr5_AutoSoft, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5_AutoSoft", type=shr5_Fertigkeit, multiplicity=Multiplicity(0, 1))
    }
)
weapon121: BinaryAssociation = BinaryAssociation(
    name="weapon121",
    ends={
        Property(name="shr5_AbstaktWaffe", type=shr5_AutoSoft, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5_AutoSoft122", type=shr5_AbstaktWaffe, multiplicity=Multiplicity(0, 1))
    }
)
model123: BinaryAssociation = BinaryAssociation(
    name="model123",
    ends={
        Property(name="shr5_Drohne125", type=shr5_AutoSoft, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5_AutoSoft124", type=shr5_Drohne, multiplicity=Multiplicity(0, 1))
    }
)
skill126: BinaryAssociation = BinaryAssociation(
    name="skill126",
    ends={
        Property(name="shr5_Fertigkeit127", type=shr5_Tutorsoft, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5_Tutorsoft", type=shr5_Fertigkeit, multiplicity=Multiplicity(1, 1))
    }
)
slaves130: BinaryAssociation = BinaryAssociation(
    name="slaves130",
    ends={
        Property(name="shr5_MatrixDevice131", type=shr5_PersonalAreaNetwork, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5_PersonalAreaNetwork", type=shr5_MatrixDevice, multiplicity=Multiplicity(0, 9999))
    }
)
master132: BinaryAssociation = BinaryAssociation(
    name="master132",
    ends={
        Property(name="MatrixDevice", type=shr5_PersonalAreaNetwork, multiplicity=Multiplicity(1, 1)),
        Property(name="pan", type=shr5_MatrixDevice, multiplicity=Multiplicity(1, 1))
    }
)
skill133: BinaryAssociation = BinaryAssociation(
    name="skill133",
    ends={
        Property(name="shr5_Wissensfertigkeit", type=shr5_Datasoft, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5_Datasoft", type=shr5_Wissensfertigkeit, multiplicity=Multiplicity(1, 1))
    }
)
pan134: BinaryAssociation = BinaryAssociation(
    name="pan134",
    ends={
        Property(name="PersonalAreaNetwork", type=shr5_MatrixDevice, multiplicity=Multiplicity(1, 1)),
        Property(name="master", type=shr5_PersonalAreaNetwork, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
weapon135: BinaryAssociation = BinaryAssociation(
    name="weapon135",
    ends={
        Property(name="shr5_AbstaktWaffe136", type=shr5_WeaponMount, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5_WeaponMount", type=shr5_AbstaktWaffe, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
skill128: BinaryAssociation = BinaryAssociation(
    name="skill128",
    ends={
        Property(name="shr5_Fertigkeit129", type=shr5_SkillSoft, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5_SkillSoft", type=shr5_Fertigkeit, multiplicity=Multiplicity(1, 1))
    }
)
power137: BinaryAssociation = BinaryAssociation(
    name="power137",
    ends={
        Property(name="shr5_KiKraft138", type=shr5_QiFokus, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5_QiFokus", type=shr5_KiKraft, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
fokus139: BinaryAssociation = BinaryAssociation(
    name="fokus139",
    ends={
        Property(name="shr5_Fokus", type=shr5_FokusBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5_FokusBinding140", type=shr5_Fokus, multiplicity=Multiplicity(1, 1))
    }
)
type141: BinaryAssociation = BinaryAssociation(
    name="type141",
    ends={
        Property(name="shr5_Feuerwaffe143", type=shr5_Magazin, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5_Magazin142", type=shr5_Feuerwaffe, multiplicity=Multiplicity(1, 1))
    }
)
bullets144: BinaryAssociation = BinaryAssociation(
    name="bullets144",
    ends={
        Property(name="shr5_Munition146", type=shr5_Magazin, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5_Magazin145", type=shr5_Munition, multiplicity=Multiplicity(0, 9999))
    }
)
substance147: BinaryAssociation = BinaryAssociation(
    name="substance147",
    ends={
        Property(name="shr5_Substance", type=shr5_SubstanceContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5_SubstanceContainer", type=shr5_Substance, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
capacityFeature148: BinaryAssociation = BinaryAssociation(
    name="capacityFeature148",
    ends={
        Property(name="shr5_EReference", type=shr5_Capacity, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5_Capacity", type=shr5_EReference, multiplicity=Multiplicity(0, 1))
    }
)
weapon149: BinaryAssociation = BinaryAssociation(
    name="weapon149",
    ends={
        Property(name="shr5_AbstaktWaffe150", type=shr5_CyberImplantWeapon, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5_CyberImplantWeapon", type=shr5_AbstaktWaffe, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
beschwoerbar151: BinaryAssociation = BinaryAssociation(
    name="beschwoerbar151",
    ends={
        Property(name="shr5_Geist153", type=shr5_MagischeTradition, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5_MagischeTradition152", type=shr5_Geist, multiplicity=Multiplicity(0, 9999))
    }
)
items154: BinaryAssociation = BinaryAssociation(
    name="items154",
    ends={
        Property(name="shr5_GeldWert", type=shr5_ShoppingTransaction, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5_ShoppingTransaction", type=shr5_GeldWert, multiplicity=Multiplicity(0, 9999))
    }
)
source155: BinaryAssociation = BinaryAssociation(
    name="source155",
    ends={
        Property(name="shr5_Credstick156", type=shr5_TransferAmount, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5_TransferAmount", type=shr5_Credstick, multiplicity=Multiplicity(1, 1))
    }
)
dest157: BinaryAssociation = BinaryAssociation(
    name="dest157",
    ends={
        Property(name="shr5_Credstick159", type=shr5_TransferAmount, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5_TransferAmount158", type=shr5_Credstick, multiplicity=Multiplicity(1, 1))
    }
)
functions160: BinaryAssociation = BinaryAssociation(
    name="functions160",
    ends={
        Property(name="shr5_SensorFunction", type=shr5_Sensor, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5_Sensor", type=shr5_SensorFunction, multiplicity=Multiplicity(0, 9999))
    }
)
techniques161: BinaryAssociation = BinaryAssociation(
    name="techniques161",
    ends={
        Property(name="shr5_MartialartTechnique", type=shr5_MartialartStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5_MartialartStyle", type=shr5_MartialartTechnique, multiplicity=Multiplicity(0, 9999))
    }
)
usableWith162: BinaryAssociation = BinaryAssociation(
    name="usableWith162",
    ends={
        Property(name="shr5_Fertigkeit164", type=shr5_MartialartStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5_MartialartStyle163", type=shr5_Fertigkeit, multiplicity=Multiplicity(0, 9999))
    }
)
style165: BinaryAssociation = BinaryAssociation(
    name="style165",
    ends={
        Property(name="shr5_MartialartStyle167", type=shr5_PersonaMartialartStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5_PersonaMartialartStyle166", type=shr5_MartialartStyle, multiplicity=Multiplicity(1, 1))
    }
)
techniques168: BinaryAssociation = BinaryAssociation(
    name="techniques168",
    ends={
        Property(name="shr5_PersonaMartialartTechnique", type=shr5_PersonaMartialartStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5_PersonaMartialartStyle169", type=shr5_PersonaMartialartTechnique, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
technique170: BinaryAssociation = BinaryAssociation(
    name="technique170",
    ends={
        Property(name="shr5_MartialartTechnique172", type=shr5_PersonaMartialartTechnique, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5_PersonaMartialartTechnique171", type=shr5_MartialartTechnique, multiplicity=Multiplicity(1, 1))
    }
)
chemical173: BinaryAssociation = BinaryAssociation(
    name="chemical173",
    ends={
        Property(name="shr5_Substance174", type=shr5_AbtraktGranate, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5_AbtraktGranate", type=shr5_Substance, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
subLinks176: BinaryAssociation = BinaryAssociation(
    name="subLinks176",
    ends={
        Property(name="shr5_SourceLink", type=shr5_SourceLink, multiplicity=Multiplicity(1, 1)),
        Property(name="shr5_SourceLink175", type=shr5_SourceLink, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_shr5_Quelle_Identifiable = Generalization(general=Identifiable, specific=shr5_Quelle)
gen_shr5_SourceBook_Beschreibbar = Generalization(general=Beschreibbar, specific=shr5_SourceBook)
gen_shr5_SourceBook_Identifiable = Generalization(general=Identifiable, specific=shr5_SourceBook)
gen_shr5_AbstraktPersona_Beschreibbar = Generalization(general=Beschreibbar, specific=shr5_AbstraktPersona)
gen_shr5_AbstraktPersona_KoerperlicheAttribute = Generalization(general=KoerperlicheAttribute, specific=shr5_AbstraktPersona)
gen_shr5_AbstraktPersona_SpezielleAttribute = Generalization(general=SpezielleAttribute, specific=shr5_AbstraktPersona)
gen_shr5_AbstraktPersona_GeistigeAttribute = Generalization(general=GeistigeAttribute, specific=shr5_AbstraktPersona)
gen_shr5_AbstraktPersona_ChrakterLimits = Generalization(general=ChrakterLimits, specific=shr5_AbstraktPersona)
gen_shr5_Gegenstand_AbstraktGegenstand = Generalization(general=AbstraktGegenstand, specific=shr5_Gegenstand)
gen_shr5_Reichweite_Beschreibbar = Generalization(general=Beschreibbar, specific=shr5_Reichweite)
gen_shr5_Reichweite_Identifiable = Generalization(general=Identifiable, specific=shr5_Reichweite)
gen_shr5_KoerperlicheAttribute_ModifikatorAttribute = Generalization(general=ModifikatorAttribute, specific=shr5_KoerperlicheAttribute)
gen_shr5_SpezielleAttribute_ModifikatorAttribute = Generalization(general=ModifikatorAttribute, specific=shr5_SpezielleAttribute)
gen_shr5_AbstraktGegenstand_Quelle = Generalization(general=Quelle, specific=shr5_AbstraktGegenstand)
gen_shr5_AbstraktGegenstand_GeldWert = Generalization(general=GeldWert, specific=shr5_AbstraktGegenstand)
gen_shr5_AbstraktGegenstand_Beschreibbar = Generalization(general=Beschreibbar, specific=shr5_AbstraktGegenstand)
gen_shr5_AbstraktGegenstand_Modifizierbar = Generalization(general=Modifizierbar, specific=shr5_AbstraktGegenstand)
gen_shr5_AbstraktGegenstand_Anwendbar = Generalization(general=Anwendbar, specific=shr5_AbstraktGegenstand)
gen_shr5_AbstaktFernKampfwaffe_AbstaktWaffe = Generalization(general=AbstaktWaffe, specific=shr5_AbstaktFernKampfwaffe)
gen_shr5_AbstaktWaffe_AbstraktGegenstand = Generalization(general=AbstraktGegenstand, specific=shr5_AbstaktWaffe)
gen_shr5_Nahkampfwaffe_AbstaktWaffe = Generalization(general=AbstaktWaffe, specific=shr5_Nahkampfwaffe)
gen_shr5_Feuerwaffe_AbstaktFernKampfwaffe = Generalization(general=AbstaktFernKampfwaffe, specific=shr5_Feuerwaffe)
gen_shr5_Wurfwaffe_AbstaktFernKampfwaffe = Generalization(general=AbstaktFernKampfwaffe, specific=shr5_Wurfwaffe)
gen_shr5_Wurfwaffe_Menge = Generalization(general=Menge, specific=shr5_Wurfwaffe)
gen_shr5_ShrList_Beschreibbar = Generalization(general=Beschreibbar, specific=shr5_ShrList)
gen_shr5_ShrList_Identifiable = Generalization(general=Identifiable, specific=shr5_ShrList)
gen_shr5_Projektilwaffe_AbstaktFernKampfwaffe = Generalization(general=AbstaktFernKampfwaffe, specific=shr5_Projektilwaffe)
gen_shr5_FertigkeitsGruppe_Beschreibbar = Generalization(general=Beschreibbar, specific=shr5_FertigkeitsGruppe)
gen_shr5_FertigkeitsGruppe_Quelle = Generalization(general=Quelle, specific=shr5_FertigkeitsGruppe)
gen_shr5_FertigkeitsGruppe_Modifyable = Generalization(general=Modifyable, specific=shr5_FertigkeitsGruppe)
gen_shr5_Fertigkeit_Beschreibbar = Generalization(general=Beschreibbar, specific=shr5_Fertigkeit)
gen_shr5_Fertigkeit_Quelle = Generalization(general=Quelle, specific=shr5_Fertigkeit)
gen_shr5_Fertigkeit_Modifyable = Generalization(general=Modifyable, specific=shr5_Fertigkeit)
gen_shr5_PersonaFertigkeit_Steigerbar = Generalization(general=Steigerbar, specific=shr5_PersonaFertigkeit)
gen_shr5_PersonaFertigkeitsGruppe_Steigerbar = Generalization(general=Steigerbar, specific=shr5_PersonaFertigkeitsGruppe)
gen_shr5_Cyberware_Koerpermods = Generalization(general=Koerpermods, specific=shr5_Cyberware)
gen_shr5_Cyberware_GeldWert = Generalization(general=GeldWert, specific=shr5_Cyberware)
gen_shr5_Cyberware_Capacity = Generalization(general=Capacity, specific=shr5_Cyberware)
gen_shr5_BioWare_Koerpermods = Generalization(general=Koerpermods, specific=shr5_BioWare)
gen_shr5_BioWare_GeldWert = Generalization(general=GeldWert, specific=shr5_BioWare)
gen_shr5_Koerpermods_AbstraktModifikatoren = Generalization(general=AbstraktModifikatoren, specific=shr5_Koerpermods)
gen_shr5_AbstraktModifikatoren_Beschreibbar = Generalization(general=Beschreibbar, specific=shr5_AbstraktModifikatoren)
gen_shr5_AbstraktModifikatoren_Modifizierbar = Generalization(general=Modifizierbar, specific=shr5_AbstraktModifikatoren)
gen_shr5_AbstraktModifikatoren_Quelle = Generalization(general=Quelle, specific=shr5_AbstraktModifikatoren)
gen_shr5_GeistigeAttribute_ModifikatorAttribute = Generalization(general=ModifikatorAttribute, specific=shr5_GeistigeAttribute)
gen_shr5_MudanPersona_KoerperPersona = Generalization(general=KoerperPersona, specific=shr5_MudanPersona)
gen_shr5_KoerperPersona_AbstraktPersona = Generalization(general=AbstraktPersona, specific=shr5_KoerperPersona)
gen_shr5_KoerperPersona_Panzerung = Generalization(general=Panzerung, specific=shr5_KoerperPersona)
gen_shr5_KoerperPersona_PersonaZustand = Generalization(general=PersonaZustand, specific=shr5_KoerperPersona)
gen_shr5_KoerperPersona_BerechneteAttribute = Generalization(general=BerechneteAttribute, specific=shr5_KoerperPersona)
gen_shr5_MagischeMods_AbstraktModifikatoren = Generalization(general=AbstraktModifikatoren, specific=shr5_MagischeMods)
gen_shr5_KiKraft_MagischeMods = Generalization(general=MagischeMods, specific=shr5_KiKraft)
gen_shr5_KiKraft_Erlernbar = Generalization(general=Erlernbar, specific=shr5_KiKraft)
gen_shr5_MagischePersona_KoerperPersona = Generalization(general=KoerperPersona, specific=shr5_MagischePersona)
gen_shr5_MagischePersona_BaseMagischePersona = Generalization(general=BaseMagischePersona, specific=shr5_MagischePersona)
gen_shr5_FernkampfwaffenModifikatoren_ModifikatorAttribute = Generalization(general=ModifikatorAttribute, specific=shr5_FernkampfwaffenModifikatoren)
gen_shr5_Sichtverhaeltnisse_ModifikatorAttribute = Generalization(general=ModifikatorAttribute, specific=shr5_Sichtverhaeltnisse)
gen_shr5_Spezies_Beschreibbar = Generalization(general=Beschreibbar, specific=shr5_Spezies)
gen_shr5_Spezies_Modifizierbar = Generalization(general=Modifizierbar, specific=shr5_Spezies)
gen_shr5_Spezies_Quelle = Generalization(general=Quelle, specific=shr5_Spezies)
gen_shr5_GegenstandStufen_ModifikatorAttribute = Generalization(general=ModifikatorAttribute, specific=shr5_GegenstandStufen)
gen_shr5_KiAdept_MagischePersona = Generalization(general=MagischePersona, specific=shr5_KiAdept)
gen_shr5_Kleidung_AbstraktGegenstand = Generalization(general=AbstraktGegenstand, specific=shr5_Kleidung)
gen_shr5_Kleidung_Capacity = Generalization(general=Capacity, specific=shr5_Kleidung)
gen_shr5_FernkampfwaffeModifikator_AbstraktModifikatoren = Generalization(general=AbstraktModifikatoren, specific=shr5_FernkampfwaffeModifikator)
gen_shr5_FernkampfwaffeModifikator_GeldWert = Generalization(general=GeldWert, specific=shr5_FernkampfwaffeModifikator)
gen_shr5_PersonaEigenschaft_AbstraktModifikatoren = Generalization(general=AbstraktModifikatoren, specific=shr5_PersonaEigenschaft)
gen_shr5_PersonaEigenschaft_Erlernbar = Generalization(general=Erlernbar, specific=shr5_PersonaEigenschaft)
gen_shr5_ProbenModifikatoren_ModifikatorAttribute = Generalization(general=ModifikatorAttribute, specific=shr5_ProbenModifikatoren)
gen_shr5_Magier_MagischePersona = Generalization(general=MagischePersona, specific=shr5_Magier)
gen_shr5_Magier_Zauberer = Generalization(general=Zauberer, specific=shr5_Magier)
gen_shr5_Magier_AstraleProjektion = Generalization(general=AstraleProjektion, specific=shr5_Magier)
gen_shr5_MysticAdept_KiAdept = Generalization(general=KiAdept, specific=shr5_MysticAdept)
gen_shr5_MysticAdept_Zauberer = Generalization(general=Zauberer, specific=shr5_MysticAdept)
gen_shr5_PersonaZauber_Erlernbar = Generalization(general=Erlernbar, specific=shr5_PersonaZauber)
gen_shr5_Zauber_Beschreibbar = Generalization(general=Beschreibbar, specific=shr5_Zauber)
gen_shr5_Zauber_Quelle = Generalization(general=Quelle, specific=shr5_Zauber)
gen_shr5_AspektMagier_MagischePersona = Generalization(general=MagischePersona, specific=shr5_AspektMagier)
gen_shr5_AspektMagier_Zauberer = Generalization(general=Zauberer, specific=shr5_AspektMagier)
gen_shr5_Schutzgeist_MagischeMods = Generalization(general=MagischeMods, specific=shr5_Schutzgeist)
gen_shr5_Initation_Steigerbar = Generalization(general=Steigerbar, specific=shr5_Initation)
gen_shr5_MetaMagie_Beschreibbar = Generalization(general=Beschreibbar, specific=shr5_MetaMagie)
gen_shr5_MetaMagie_Quelle = Generalization(general=Quelle, specific=shr5_MetaMagie)
gen_shr5_CritterKraft_MagischeMods = Generalization(general=MagischeMods, specific=shr5_CritterKraft)
gen_shr5_Fahrzeug_Beschreibbar = Generalization(general=Beschreibbar, specific=shr5_Fahrzeug)
gen_shr5_Fahrzeug_Quelle = Generalization(general=Quelle, specific=shr5_Fahrzeug)
gen_shr5_Fahrzeug_GeldWert = Generalization(general=GeldWert, specific=shr5_Fahrzeug)
gen_shr5_Fahrzeug_Anwendbar = Generalization(general=Anwendbar, specific=shr5_Fahrzeug)
gen_shr5_Fahrzeug_Modifizierbar = Generalization(general=Modifizierbar, specific=shr5_Fahrzeug)
gen_shr5_Fahrzeug_FahrzeugZustand = Generalization(general=FahrzeugZustand, specific=shr5_Fahrzeug)
gen_shr5_Fahrzeug_Capacity = Generalization(general=Capacity, specific=shr5_Fahrzeug)
gen_shr5_Bodenfahrzeug_PassagierFahrzeug = Generalization(general=PassagierFahrzeug, specific=shr5_Bodenfahrzeug)
gen_shr5_PassagierFahrzeug_Fahrzeug = Generalization(general=Fahrzeug, specific=shr5_PassagierFahrzeug)
gen_shr5_Drohne_Fahrzeug = Generalization(general=Fahrzeug, specific=shr5_Drohne)
gen_shr5_Drohne_MatrixAttributes = Generalization(general=MatrixAttributes, specific=shr5_Drohne)
gen_shr5_FahrzeugModifikation_Beschreibbar = Generalization(general=Beschreibbar, specific=shr5_FahrzeugModifikation)
gen_shr5_FahrzeugModifikation_Quelle = Generalization(general=Quelle, specific=shr5_FahrzeugModifikation)
gen_shr5_FahrzeugModifikation_GeldWert = Generalization(general=GeldWert, specific=shr5_FahrzeugModifikation)
gen_shr5_Technomancer_KoerperPersona = Generalization(general=KoerperPersona, specific=shr5_Technomancer)
gen_shr5_Technomancer_ResonanzPersona = Generalization(general=ResonanzPersona, specific=shr5_Technomancer)
gen_shr5_ResonanzPersona_ActiveMatixDevice = Generalization(general=ActiveMatixDevice, specific=shr5_ResonanzPersona)
gen_shr5_PersonaKomplexForm_Erlernbar = Generalization(general=Erlernbar, specific=shr5_PersonaKomplexForm)
gen_shr5_Sprite_ResonanzPersona = Generalization(general=ResonanzPersona, specific=shr5_Sprite)
gen_shr5_Sprite_Beschreibbar = Generalization(general=Beschreibbar, specific=shr5_Sprite)
gen_shr5_Sprite_Quelle = Generalization(general=Quelle, specific=shr5_Sprite)
gen_shr5_Echo_AbstraktModifikatoren = Generalization(general=AbstraktModifikatoren, specific=shr5_Echo)
gen_shr5_Vertrag_Beschreibbar = Generalization(general=Beschreibbar, specific=shr5_Vertrag)
gen_shr5_Vertrag_Quelle = Generalization(general=Quelle, specific=shr5_Vertrag)
gen_shr5_Vertrag_GeldWert = Generalization(general=GeldWert, specific=shr5_Vertrag)
gen_shr5_Lifestyle_IntervallVertrag = Generalization(general=IntervallVertrag, specific=shr5_Lifestyle)
gen_shr5_Wissensfertigkeit_Fertigkeit = Generalization(general=Fertigkeit, specific=shr5_Wissensfertigkeit)
gen_shr5_Sprachfertigkeit_Wissensfertigkeit = Generalization(general=Wissensfertigkeit, specific=shr5_Sprachfertigkeit)
gen_shr5_Critter_Spezies = Generalization(general=Spezies, specific=shr5_Critter)
gen_shr5_IntervallVertrag_Vertrag = Generalization(general=Vertrag, specific=shr5_IntervallVertrag)
gen_shr5_KomplexeForm_Quelle = Generalization(general=Quelle, specific=shr5_KomplexeForm)
gen_shr5_KomplexeForm_Beschreibbar = Generalization(general=Beschreibbar, specific=shr5_KomplexeForm)
gen_shr5_Sin_Fakeable = Generalization(general=Fakeable, specific=shr5_Sin)
gen_shr5_Lizenz_Fakeable = Generalization(general=Fakeable, specific=shr5_Lizenz)
gen_shr5_Fakeable_Vertrag = Generalization(general=Vertrag, specific=shr5_Fakeable)
gen_shr5_Steigerbar_Erlernbar = Generalization(general=Erlernbar, specific=shr5_Steigerbar)
gen_shr5_Credstick_AbstraktGegenstand = Generalization(general=AbstraktGegenstand, specific=shr5_Credstick)
gen_shr5_Munition_AbstraktGegenstand = Generalization(general=AbstraktGegenstand, specific=shr5_Munition)
gen_shr5_Munition_Menge = Generalization(general=Menge, specific=shr5_Munition)
gen_shr5_StufenPersona_Quelle = Generalization(general=Quelle, specific=shr5_StufenPersona)
gen_shr5_StufenPersona_SpezielleAttribute = Generalization(general=SpezielleAttribute, specific=shr5_StufenPersona)
gen_shr5_StufenPersona_GeistigeAttribute = Generalization(general=GeistigeAttribute, specific=shr5_StufenPersona)
gen_shr5_StufenPersona_KoerperlicheAttribute = Generalization(general=KoerperlicheAttribute, specific=shr5_StufenPersona)
gen_shr5_StufenPersona_Beschreibbar = Generalization(general=Beschreibbar, specific=shr5_StufenPersona)
gen_shr5_StufenPersona_ChrakterLimits = Generalization(general=ChrakterLimits, specific=shr5_StufenPersona)
gen_shr5_StufenPersona_Panzerung = Generalization(general=Panzerung, specific=shr5_StufenPersona)
gen_shr5_Geist_StufenPersona = Generalization(general=StufenPersona, specific=shr5_Geist)
gen_shr5_Geist_AstraleProjektion = Generalization(general=AstraleProjektion, specific=shr5_Geist)
gen_shr5_Spezialisierung_Beschreibbar = Generalization(general=Beschreibbar, specific=shr5_Spezialisierung)
gen_shr5_Spezialisierung_Quelle = Generalization(general=Quelle, specific=shr5_Spezialisierung)
gen_shr5_Spezialisierung_Erlernbar = Generalization(general=Erlernbar, specific=shr5_Spezialisierung)
gen_shr5_Spezialisierung_Modifyable = Generalization(general=Modifyable, specific=shr5_Spezialisierung)
gen_shr5_MatrixAttributes_MatixConditionMonitor = Generalization(general=MatixConditionMonitor, specific=shr5_MatrixAttributes)
gen_shr5_ActiveMatixDevice_MatrixAttributes = Generalization(general=MatrixAttributes, specific=shr5_ActiveMatixDevice)
gen_shr5_Commlink_AbstractMatrixDevice = Generalization(general=AbstractMatrixDevice, specific=shr5_Commlink)
gen_shr5_Cyberdeck_AbstractMatrixDevice = Generalization(general=AbstractMatrixDevice, specific=shr5_Cyberdeck)
gen_shr5_Cyberdeck_MatrixDevice = Generalization(general=MatrixDevice, specific=shr5_Cyberdeck)
gen_shr5_Cyberdeck_ActiveMatixDevice = Generalization(general=ActiveMatixDevice, specific=shr5_Cyberdeck)
gen_shr5_Cyberdeck_Capacity = Generalization(general=Capacity, specific=shr5_Cyberdeck)
gen_shr5_SoftwareAgent_MatrixProgram = Generalization(general=MatrixProgram, specific=shr5_SoftwareAgent)
gen_shr5_Host_Beschreibbar = Generalization(general=Beschreibbar, specific=shr5_Host)
gen_shr5_Host_MatrixDevice = Generalization(general=MatrixDevice, specific=shr5_Host)
gen_shr5_Host_ActiveMatixDevice = Generalization(general=ActiveMatixDevice, specific=shr5_Host)
gen_shr5_CyberwareModifikatioren_ModifikatorAttribute = Generalization(general=ModifikatorAttribute, specific=shr5_CyberwareModifikatioren)
gen_shr5_RiggerCommandConsole_AbstractMatrixDevice = Generalization(general=AbstractMatrixDevice, specific=shr5_RiggerCommandConsole)
gen_shr5_AutoSoft_RiggerProgram = Generalization(general=RiggerProgram, specific=shr5_AutoSoft)
gen_shr5_Software_GeldWert = Generalization(general=GeldWert, specific=shr5_Software)
gen_shr5_Software_Beschreibbar = Generalization(general=Beschreibbar, specific=shr5_Software)
gen_shr5_Software_Quelle = Generalization(general=Quelle, specific=shr5_Software)
gen_shr5_MatrixProgram_Software = Generalization(general=Software, specific=shr5_MatrixProgram)
gen_shr5_MatrixProgram_Modifizierbar = Generalization(general=Modifizierbar, specific=shr5_MatrixProgram)
gen_shr5_Tutorsoft_BasicProgram = Generalization(general=BasicProgram, specific=shr5_Tutorsoft)
gen_shr5_SkillSoft_Software = Generalization(general=Software, specific=shr5_SkillSoft)
gen_shr5_BasicProgram_Software = Generalization(general=Software, specific=shr5_BasicProgram)
gen_shr5_Datasoft_BasicProgram = Generalization(general=BasicProgram, specific=shr5_Datasoft)
gen_shr5_AbstractMatrixDevice_AbstraktGegenstand = Generalization(general=AbstraktGegenstand, specific=shr5_AbstractMatrixDevice)
gen_shr5_AbstractMatrixDevice_MatrixDevice = Generalization(general=MatrixDevice, specific=shr5_AbstractMatrixDevice)
gen_shr5_ConsumerSoft_BasicProgram = Generalization(general=BasicProgram, specific=shr5_ConsumerSoft)
gen_shr5_RiggerProgram_Software = Generalization(general=Software, specific=shr5_RiggerProgram)
gen_shr5_MatrixDevice_MatrixAttributes = Generalization(general=MatrixAttributes, specific=shr5_MatrixDevice)
gen_shr5_CommonProgram_MatrixProgram = Generalization(general=MatrixProgram, specific=shr5_CommonProgram)
gen_shr5_CommonProgram_RiggerProgram = Generalization(general=RiggerProgram, specific=shr5_CommonProgram)
gen_shr5_WeaponMount_FahrzeugModifikation = Generalization(general=FahrzeugModifikation, specific=shr5_WeaponMount)
gen_shr5_LifestyleOption_Beschreibbar = Generalization(general=Beschreibbar, specific=shr5_LifestyleOption)
gen_shr5_LifestyleOption_Quelle = Generalization(general=Quelle, specific=shr5_LifestyleOption)
gen_shr5_LifestyleOption_GeldWert = Generalization(general=GeldWert, specific=shr5_LifestyleOption)
gen_shr5_PercentLifestyleOption_LifestyleOption = Generalization(general=LifestyleOption, specific=shr5_PercentLifestyleOption)
gen_shr5_Fokus_MagischeStufe = Generalization(general=MagischeStufe, specific=shr5_Fokus)
gen_shr5_Fokus_Erlernbar = Generalization(general=Erlernbar, specific=shr5_Fokus)
gen_shr5_AbstraktFokus_Fokus = Generalization(general=Fokus, specific=shr5_AbstraktFokus)
gen_shr5_AbstraktFokus_AbstraktGegenstand = Generalization(general=AbstraktGegenstand, specific=shr5_AbstraktFokus)
gen_shr5_QiFokus_AbstraktFokus = Generalization(general=AbstraktFokus, specific=shr5_QiFokus)
gen_shr5_WaffenFokus_Nahkampfwaffe = Generalization(general=Nahkampfwaffe, specific=shr5_WaffenFokus)
gen_shr5_WaffenFokus_Fokus = Generalization(general=Fokus, specific=shr5_WaffenFokus)
gen_shr5_MagieFokus_AbstraktFokus = Generalization(general=AbstraktFokus, specific=shr5_MagieFokus)
gen_shr5_Substance_Beschreibbar = Generalization(general=Beschreibbar, specific=shr5_Substance)
gen_shr5_Substance_Quelle = Generalization(general=Quelle, specific=shr5_Substance)
gen_shr5_Substance_GeldWert = Generalization(general=GeldWert, specific=shr5_Substance)
gen_shr5_Substance_Menge = Generalization(general=Menge, specific=shr5_Substance)
gen_shr5_Toxin_Substance = Generalization(general=Substance, specific=shr5_Toxin)
gen_shr5_Magazin_AbstraktGegenstand = Generalization(general=AbstraktGegenstand, specific=shr5_Magazin)
gen_shr5_Magazin_Capacity = Generalization(general=Capacity, specific=shr5_Magazin)
gen_shr5_DefaultWifi_AbstractMatrixDevice = Generalization(general=AbstractMatrixDevice, specific=shr5_DefaultWifi)
gen_shr5_SubstanceContainer_AbstraktGegenstand = Generalization(general=AbstraktGegenstand, specific=shr5_SubstanceContainer)
gen_shr5_Drug_Substance = Generalization(general=Substance, specific=shr5_Drug)
gen_shr5_Drug_Modifizierbar = Generalization(general=Modifizierbar, specific=shr5_Drug)
gen_shr5_CyberwareEnhancement_GeldWert = Generalization(general=GeldWert, specific=shr5_CyberwareEnhancement)
gen_shr5_CyberwareEnhancement_AbstraktModifikatoren = Generalization(general=AbstraktModifikatoren, specific=shr5_CyberwareEnhancement)
gen_shr5_CyberImplantWeapon_CyberwareEnhancement = Generalization(general=CyberwareEnhancement, specific=shr5_CyberImplantWeapon)
gen_shr5_MagischeTradition_Beschreibbar = Generalization(general=Beschreibbar, specific=shr5_MagischeTradition)
gen_shr5_MagischeTradition_Quelle = Generalization(general=Quelle, specific=shr5_MagischeTradition)
gen_shr5_ShoppingTransaction_CredstickTransaction = Generalization(general=CredstickTransaction, specific=shr5_ShoppingTransaction)
gen_shr5_TransferAmount_CredstickTransaction = Generalization(general=CredstickTransaction, specific=shr5_TransferAmount)
gen_shr5_KleindungsModifikator_Beschreibbar = Generalization(general=Beschreibbar, specific=shr5_KleindungsModifikator)
gen_shr5_KleindungsModifikator_Quelle = Generalization(general=Quelle, specific=shr5_KleindungsModifikator)
gen_shr5_KleindungsModifikator_GeldWert = Generalization(general=GeldWert, specific=shr5_KleindungsModifikator)
gen_shr5_Sensor_Capacity = Generalization(general=Capacity, specific=shr5_Sensor)
gen_shr5_Sensor_Beschreibbar = Generalization(general=Beschreibbar, specific=shr5_Sensor)
gen_shr5_Sensor_Quelle = Generalization(general=Quelle, specific=shr5_Sensor)
gen_shr5_Sensor_GeldWert = Generalization(general=GeldWert, specific=shr5_Sensor)
gen_shr5_SensorArray_Sensor = Generalization(general=Sensor, specific=shr5_SensorArray)
gen_shr5_SensorFunction_Beschreibbar = Generalization(general=Beschreibbar, specific=shr5_SensorFunction)
gen_shr5_SensorFunction_Quelle = Generalization(general=Quelle, specific=shr5_SensorFunction)
gen_shr5_MartialartStyle_Beschreibbar = Generalization(general=Beschreibbar, specific=shr5_MartialartStyle)
gen_shr5_MartialartStyle_Quelle = Generalization(general=Quelle, specific=shr5_MartialartStyle)
gen_shr5_MartialartTechnique_Beschreibbar = Generalization(general=Beschreibbar, specific=shr5_MartialartTechnique)
gen_shr5_MartialartTechnique_Quelle = Generalization(general=Quelle, specific=shr5_MartialartTechnique)
gen_shr5_PersonaMartialartStyle_Spezialisierung = Generalization(general=Spezialisierung, specific=shr5_PersonaMartialartStyle)
gen_shr5_PersonaMartialartTechnique_Erlernbar = Generalization(general=Erlernbar, specific=shr5_PersonaMartialartTechnique)
gen_shr5_FahrzeugErweiterung_FahrzeugModifikation = Generalization(general=FahrzeugModifikation, specific=shr5_FahrzeugErweiterung)
gen_shr5_MiniGrenate_Munition = Generalization(general=Munition, specific=shr5_MiniGrenate)
gen_shr5_MiniGrenate_AbtraktGranate = Generalization(general=AbtraktGranate, specific=shr5_MiniGrenate)
gen_shr5_Granate_Wurfwaffe = Generalization(general=Wurfwaffe, specific=shr5_Granate)
gen_shr5_Granate_AbtraktGranate = Generalization(general=AbtraktGranate, specific=shr5_Granate)
gen_shr5_SourceLink_Beschreibbar = Generalization(general=Beschreibbar, specific=shr5_SourceLink)
gen_shr5_SourceLink_Quelle = Generalization(general=Quelle, specific=shr5_SourceLink)

# Domain Model
domain_model = DomainModel(
    name="shr5",
    types={shr5_Beschreibbar, shr5_Quelle, Identifiable, shr5_SourceBook, Beschreibbar, shr5_AbstraktPersona, KoerperlicheAttribute, SpezielleAttribute, GeistigeAttribute, ChrakterLimits, shr5_PersonaFertigkeit, shr5_PersonaFertigkeitsGruppe, shr5_Spezies, shr5_PersonaMartialartStyle, shr5_Gegenstand, AbstraktGegenstand, shr5_Reichweite, shr5_AttributModifikatorWert, shr5_EAttribute, shr5_Modifizierbar, shr5_Modifyable, shr5_KoerperlicheAttribute, ModifikatorAttribute, shr5_SpezielleAttribute, shr5_GeldWert, shr5_AbstraktGegenstand, Quelle, GeldWert, Modifizierbar, Anwendbar, shr5_MatrixDevice, shr5_AbstaktFernKampfwaffe, AbstaktWaffe, shr5_AbstaktWaffe, shr5_Nahkampfwaffe, shr5_Feuerwaffe, AbstaktFernKampfwaffe, shr5_FernkampfwaffeModifikator, shr5_Magazin, shr5_Wurfwaffe, Menge, shr5_ShrList, shr5_EObject, shr5_Projektilwaffe, shr5_FertigkeitsGruppe, Modifyable, shr5_Fertigkeit, shr5_Spezialisierung, Steigerbar, shr5_Cyberware, Koerpermods, Capacity, shr5_CyberwareEnhancement, shr5_DefaultWifi, shr5_BioWare, shr5_Koerpermods, AbstraktModifikatoren, shr5_AbstraktModifikatoren, shr5_GeistigeAttribute, shr5_MudanPersona, KoerperPersona, shr5_KoerperPersona, AbstraktPersona, Panzerung, PersonaZustand, BerechneteAttribute, shr5_PersonaEigenschaft, shr5_MagischeMods, shr5_KiKraft, MagischeMods, Erlernbar, shr5_MagischePersona, BaseMagischePersona, shr5_Schutzgeist, shr5_BaseMagischePersona, shr5_Initation, shr5_FokusBinding, shr5_FernkampfwaffenModifikatoren, shr5_Sichtverhaeltnisse, shr5_GegenstandStufen, shr5_KiAdept, MagischePersona, shr5_Kleidung, shr5_KleindungsModifikator, shr5_Anwendbar, shr5_ProbenModifikatoren, shr5_Magier, Zauberer, AstraleProjektion, shr5_Zauberer, shr5_PersonaZauber, shr5_GebundenerGeist, shr5_MagischeTradition, shr5_MysticAdept, KiAdept, shr5_Zauber, shr5_ChrakterLimits, shr5_Panzerung, shr5_AspektMagier, shr5_MetaMagie, shr5_CritterKraft, shr5_Fahrzeug, FahrzeugZustand, shr5_AstraleProjektion, shr5_FahrzeugModifikation, shr5_SensorArray, shr5_Bodenfahrzeug, PassagierFahrzeug, shr5_PassagierFahrzeug, Fahrzeug, shr5_Drohne, MatrixAttributes, shr5_RiggerProgram, shr5_Technomancer, ResonanzPersona, shr5_PersonaKomplexForm, shr5_Echo, shr5_ResonanzPersona, ActiveMatixDevice, shr5_KomplexeForm, shr5_Sprite, shr5_Vertrag, shr5_Lifestyle, IntervallVertrag, shr5_LifestyleOption, shr5_Wissensfertigkeit, Fertigkeit, shr5_Sprachfertigkeit, Wissensfertigkeit, shr5_PersonaZustand, shr5_Critter, Spezies, shr5_IntervallVertrag, Vertrag, shr5_Sin, Fakeable, shr5_Lizenz, shr5_Fakeable, shr5_Steigerbar, shr5_Erlernbar, shr5_Credstick, shr5_CredstickTransaction, shr5_Menge, shr5_Munition, shr5_ModifikatorAttribute, shr5_Geist, shr5_StufenPersona, StufenPersona, shr5_Identifiable, shr5_Localization, shr5_MatrixAttributes, MatixConditionMonitor, shr5_ActiveMatixDevice, shr5_Commlink, AbstractMatrixDevice, shr5_BasicProgram, shr5_MatixConditionMonitor, shr5_Cyberdeck, MatrixDevice, shr5_MatrixProgram, shr5_SoftwareAgent, MatrixProgram, shr5_Host, shr5_CyberwareModifikatioren, shr5_RiggerCommandConsole, shr5_AutoSoft, RiggerProgram, shr5_Software, Software, shr5_Tutorsoft, BasicProgram, shr5_SkillSoft, shr5_PersonalAreaNetwork, shr5_Datasoft, shr5_AbstractMatrixDevice, shr5_ConsumerSoft, shr5_CommonProgram, shr5_WeaponMount, FahrzeugModifikation, shr5_PercentLifestyleOption, LifestyleOption, shr5_FahrzeugZustand, shr5_MagischeStufe, shr5_Fokus, MagischeStufe, shr5_AbstraktFokus, Fokus, shr5_QiFokus, AbstraktFokus, shr5_WaffenFokus, Nahkampfwaffe, shr5_MagieFokus, shr5_Substance, shr5_Toxin, Substance, shr5_BerechneteAttribute, shr5_SubstanceContainer, shr5_Capacity, shr5_EReference, shr5_Drug, shr5_CyberImplantWeapon, CyberwareEnhancement, shr5_ShoppingTransaction, CredstickTransaction, shr5_TransferAmount, shr5_Sensor, shr5_SensorFunction, Sensor, shr5_MartialartStyle, shr5_MartialartTechnique, Spezialisierung, shr5_PersonaMartialartTechnique, shr5_FahrzeugErweiterung, shr5_AbtraktGranate, shr5_MiniGrenate, Munition, AbtraktGranate, shr5_Granate, Wurfwaffe, shr5_SourceLink, FeuerModus, SchadensTyp, MagazinTyp, FeuwerwaffenErweiterung, ModifikatorType, SmartgunType, ZauberArt, ZauberReichweite, ZauberDauer, CritterHandlung, CritterReichweite, CritterDauer, ResonanzZiel, InterfaceModus, ProgramType, MatrixProgramType, SubstanceVector, SubstanceEffect, AddictionType, TimeUnits, Enzug, CyberwareType, armorModificationType},
    associations={srcBook0, fertigkeiten1, fertigkeitsGruppen2, spezies4, martialartStyles6, attribut8, modifiziertes9, modifyable10, mods12, wifi13, reichweite14, einbau15, magazin16, entries18, fertigkeiten19, attribut20, spezialisierungen23, fertigkeit24, spezialisierungen27, gruppe29, persona32, einbau34, wifi36, koerperMods40, eigenschaften41, mentor43, initationen44, boundFoki45, persona38, angriff47, kikraft49, kmods50, fertigkeit51, spezialisierung53, zauber56, gebundeneGeister57, ungebundenerGeist59, tradition62, formel64, aspekt66, erlernt68, modifizierungen70, sensorArray71, runningPrograms73, storedPrograms74, complexForms77, echos78, form80, options82, powers83, licences84, lizenzTraeger85, transactionlog86, type87, geist89, skillGroups91, skills93, powers96, optionalPowers99, localizations102, fertigkeit103, storedPrograms104, configuration107, storedPrograms109, runningPrograms111, storedSins105, storedPrograms114, runningPrograms116, skill119, weapon121, model123, skill126, slaves130, master132, skill133, pan134, weapon135, skill128, power137, fokus139, type141, bullets144, substance147, capacityFeature148, weapon149, beschwoerbar151, items154, source155, dest157, functions160, techniques161, usableWith162, style165, techniques168, technique170, chemical173, subLinks176},
    generalizations={gen_shr5_Quelle_Identifiable, gen_shr5_SourceBook_Beschreibbar, gen_shr5_SourceBook_Identifiable, gen_shr5_AbstraktPersona_Beschreibbar, gen_shr5_AbstraktPersona_KoerperlicheAttribute, gen_shr5_AbstraktPersona_SpezielleAttribute, gen_shr5_AbstraktPersona_GeistigeAttribute, gen_shr5_AbstraktPersona_ChrakterLimits, gen_shr5_Gegenstand_AbstraktGegenstand, gen_shr5_Reichweite_Beschreibbar, gen_shr5_Reichweite_Identifiable, gen_shr5_KoerperlicheAttribute_ModifikatorAttribute, gen_shr5_SpezielleAttribute_ModifikatorAttribute, gen_shr5_AbstraktGegenstand_Quelle, gen_shr5_AbstraktGegenstand_GeldWert, gen_shr5_AbstraktGegenstand_Beschreibbar, gen_shr5_AbstraktGegenstand_Modifizierbar, gen_shr5_AbstraktGegenstand_Anwendbar, gen_shr5_AbstaktFernKampfwaffe_AbstaktWaffe, gen_shr5_AbstaktWaffe_AbstraktGegenstand, gen_shr5_Nahkampfwaffe_AbstaktWaffe, gen_shr5_Feuerwaffe_AbstaktFernKampfwaffe, gen_shr5_Wurfwaffe_AbstaktFernKampfwaffe, gen_shr5_Wurfwaffe_Menge, gen_shr5_ShrList_Beschreibbar, gen_shr5_ShrList_Identifiable, gen_shr5_Projektilwaffe_AbstaktFernKampfwaffe, gen_shr5_FertigkeitsGruppe_Beschreibbar, gen_shr5_FertigkeitsGruppe_Quelle, gen_shr5_FertigkeitsGruppe_Modifyable, gen_shr5_Fertigkeit_Beschreibbar, gen_shr5_Fertigkeit_Quelle, gen_shr5_Fertigkeit_Modifyable, gen_shr5_PersonaFertigkeit_Steigerbar, gen_shr5_PersonaFertigkeitsGruppe_Steigerbar, gen_shr5_Cyberware_Koerpermods, gen_shr5_Cyberware_GeldWert, gen_shr5_Cyberware_Capacity, gen_shr5_BioWare_Koerpermods, gen_shr5_BioWare_GeldWert, gen_shr5_Koerpermods_AbstraktModifikatoren, gen_shr5_AbstraktModifikatoren_Beschreibbar, gen_shr5_AbstraktModifikatoren_Modifizierbar, gen_shr5_AbstraktModifikatoren_Quelle, gen_shr5_GeistigeAttribute_ModifikatorAttribute, gen_shr5_MudanPersona_KoerperPersona, gen_shr5_KoerperPersona_AbstraktPersona, gen_shr5_KoerperPersona_Panzerung, gen_shr5_KoerperPersona_PersonaZustand, gen_shr5_KoerperPersona_BerechneteAttribute, gen_shr5_MagischeMods_AbstraktModifikatoren, gen_shr5_KiKraft_MagischeMods, gen_shr5_KiKraft_Erlernbar, gen_shr5_MagischePersona_KoerperPersona, gen_shr5_MagischePersona_BaseMagischePersona, gen_shr5_FernkampfwaffenModifikatoren_ModifikatorAttribute, gen_shr5_Sichtverhaeltnisse_ModifikatorAttribute, gen_shr5_Spezies_Beschreibbar, gen_shr5_Spezies_Modifizierbar, gen_shr5_Spezies_Quelle, gen_shr5_GegenstandStufen_ModifikatorAttribute, gen_shr5_KiAdept_MagischePersona, gen_shr5_Kleidung_AbstraktGegenstand, gen_shr5_Kleidung_Capacity, gen_shr5_FernkampfwaffeModifikator_AbstraktModifikatoren, gen_shr5_FernkampfwaffeModifikator_GeldWert, gen_shr5_PersonaEigenschaft_AbstraktModifikatoren, gen_shr5_PersonaEigenschaft_Erlernbar, gen_shr5_ProbenModifikatoren_ModifikatorAttribute, gen_shr5_Magier_MagischePersona, gen_shr5_Magier_Zauberer, gen_shr5_Magier_AstraleProjektion, gen_shr5_MysticAdept_KiAdept, gen_shr5_MysticAdept_Zauberer, gen_shr5_PersonaZauber_Erlernbar, gen_shr5_Zauber_Beschreibbar, gen_shr5_Zauber_Quelle, gen_shr5_AspektMagier_MagischePersona, gen_shr5_AspektMagier_Zauberer, gen_shr5_Schutzgeist_MagischeMods, gen_shr5_Initation_Steigerbar, gen_shr5_MetaMagie_Beschreibbar, gen_shr5_MetaMagie_Quelle, gen_shr5_CritterKraft_MagischeMods, gen_shr5_Fahrzeug_Beschreibbar, gen_shr5_Fahrzeug_Quelle, gen_shr5_Fahrzeug_GeldWert, gen_shr5_Fahrzeug_Anwendbar, gen_shr5_Fahrzeug_Modifizierbar, gen_shr5_Fahrzeug_FahrzeugZustand, gen_shr5_Fahrzeug_Capacity, gen_shr5_Bodenfahrzeug_PassagierFahrzeug, gen_shr5_PassagierFahrzeug_Fahrzeug, gen_shr5_Drohne_Fahrzeug, gen_shr5_Drohne_MatrixAttributes, gen_shr5_FahrzeugModifikation_Beschreibbar, gen_shr5_FahrzeugModifikation_Quelle, gen_shr5_FahrzeugModifikation_GeldWert, gen_shr5_Technomancer_KoerperPersona, gen_shr5_Technomancer_ResonanzPersona, gen_shr5_ResonanzPersona_ActiveMatixDevice, gen_shr5_PersonaKomplexForm_Erlernbar, gen_shr5_Sprite_ResonanzPersona, gen_shr5_Sprite_Beschreibbar, gen_shr5_Sprite_Quelle, gen_shr5_Echo_AbstraktModifikatoren, gen_shr5_Vertrag_Beschreibbar, gen_shr5_Vertrag_Quelle, gen_shr5_Vertrag_GeldWert, gen_shr5_Lifestyle_IntervallVertrag, gen_shr5_Wissensfertigkeit_Fertigkeit, gen_shr5_Sprachfertigkeit_Wissensfertigkeit, gen_shr5_Critter_Spezies, gen_shr5_IntervallVertrag_Vertrag, gen_shr5_KomplexeForm_Quelle, gen_shr5_KomplexeForm_Beschreibbar, gen_shr5_Sin_Fakeable, gen_shr5_Lizenz_Fakeable, gen_shr5_Fakeable_Vertrag, gen_shr5_Steigerbar_Erlernbar, gen_shr5_Credstick_AbstraktGegenstand, gen_shr5_Munition_AbstraktGegenstand, gen_shr5_Munition_Menge, gen_shr5_StufenPersona_Quelle, gen_shr5_StufenPersona_SpezielleAttribute, gen_shr5_StufenPersona_GeistigeAttribute, gen_shr5_StufenPersona_KoerperlicheAttribute, gen_shr5_StufenPersona_Beschreibbar, gen_shr5_StufenPersona_ChrakterLimits, gen_shr5_StufenPersona_Panzerung, gen_shr5_Geist_StufenPersona, gen_shr5_Geist_AstraleProjektion, gen_shr5_Spezialisierung_Beschreibbar, gen_shr5_Spezialisierung_Quelle, gen_shr5_Spezialisierung_Erlernbar, gen_shr5_Spezialisierung_Modifyable, gen_shr5_MatrixAttributes_MatixConditionMonitor, gen_shr5_ActiveMatixDevice_MatrixAttributes, gen_shr5_Commlink_AbstractMatrixDevice, gen_shr5_Cyberdeck_AbstractMatrixDevice, gen_shr5_Cyberdeck_MatrixDevice, gen_shr5_Cyberdeck_ActiveMatixDevice, gen_shr5_Cyberdeck_Capacity, gen_shr5_SoftwareAgent_MatrixProgram, gen_shr5_Host_Beschreibbar, gen_shr5_Host_MatrixDevice, gen_shr5_Host_ActiveMatixDevice, gen_shr5_CyberwareModifikatioren_ModifikatorAttribute, gen_shr5_RiggerCommandConsole_AbstractMatrixDevice, gen_shr5_AutoSoft_RiggerProgram, gen_shr5_Software_GeldWert, gen_shr5_Software_Beschreibbar, gen_shr5_Software_Quelle, gen_shr5_MatrixProgram_Software, gen_shr5_MatrixProgram_Modifizierbar, gen_shr5_Tutorsoft_BasicProgram, gen_shr5_SkillSoft_Software, gen_shr5_BasicProgram_Software, gen_shr5_Datasoft_BasicProgram, gen_shr5_AbstractMatrixDevice_AbstraktGegenstand, gen_shr5_AbstractMatrixDevice_MatrixDevice, gen_shr5_ConsumerSoft_BasicProgram, gen_shr5_RiggerProgram_Software, gen_shr5_MatrixDevice_MatrixAttributes, gen_shr5_CommonProgram_MatrixProgram, gen_shr5_CommonProgram_RiggerProgram, gen_shr5_WeaponMount_FahrzeugModifikation, gen_shr5_LifestyleOption_Beschreibbar, gen_shr5_LifestyleOption_Quelle, gen_shr5_LifestyleOption_GeldWert, gen_shr5_PercentLifestyleOption_LifestyleOption, gen_shr5_Fokus_MagischeStufe, gen_shr5_Fokus_Erlernbar, gen_shr5_AbstraktFokus_Fokus, gen_shr5_AbstraktFokus_AbstraktGegenstand, gen_shr5_QiFokus_AbstraktFokus, gen_shr5_WaffenFokus_Nahkampfwaffe, gen_shr5_WaffenFokus_Fokus, gen_shr5_MagieFokus_AbstraktFokus, gen_shr5_Substance_Beschreibbar, gen_shr5_Substance_Quelle, gen_shr5_Substance_GeldWert, gen_shr5_Substance_Menge, gen_shr5_Toxin_Substance, gen_shr5_Magazin_AbstraktGegenstand, gen_shr5_Magazin_Capacity, gen_shr5_DefaultWifi_AbstractMatrixDevice, gen_shr5_SubstanceContainer_AbstraktGegenstand, gen_shr5_Drug_Substance, gen_shr5_Drug_Modifizierbar, gen_shr5_CyberwareEnhancement_GeldWert, gen_shr5_CyberwareEnhancement_AbstraktModifikatoren, gen_shr5_CyberImplantWeapon_CyberwareEnhancement, gen_shr5_MagischeTradition_Beschreibbar, gen_shr5_MagischeTradition_Quelle, gen_shr5_ShoppingTransaction_CredstickTransaction, gen_shr5_TransferAmount_CredstickTransaction, gen_shr5_KleindungsModifikator_Beschreibbar, gen_shr5_KleindungsModifikator_Quelle, gen_shr5_KleindungsModifikator_GeldWert, gen_shr5_Sensor_Capacity, gen_shr5_Sensor_Beschreibbar, gen_shr5_Sensor_Quelle, gen_shr5_Sensor_GeldWert, gen_shr5_SensorArray_Sensor, gen_shr5_SensorFunction_Beschreibbar, gen_shr5_SensorFunction_Quelle, gen_shr5_MartialartStyle_Beschreibbar, gen_shr5_MartialartStyle_Quelle, gen_shr5_MartialartTechnique_Beschreibbar, gen_shr5_MartialartTechnique_Quelle, gen_shr5_PersonaMartialartStyle_Spezialisierung, gen_shr5_PersonaMartialartTechnique_Erlernbar, gen_shr5_FahrzeugErweiterung_FahrzeugModifikation, gen_shr5_MiniGrenate_Munition, gen_shr5_MiniGrenate_AbtraktGranate, gen_shr5_Granate_Wurfwaffe, gen_shr5_Granate_AbtraktGranate, gen_shr5_SourceLink_Beschreibbar, gen_shr5_SourceLink_Quelle},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)