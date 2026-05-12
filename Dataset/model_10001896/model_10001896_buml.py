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

# Classes
Benutzer = Class(name="Benutzer")
Weidegang2 = Class(name="Weidegang2")
WIS_Weidefl_che = Class(name="WIS_Weidefl_che")
WIS_Weide = Class(name="WIS_Weide")
WIS_Weidegang = Class(name="WIS_Weidegang")
WIS_Herde = Class(name="WIS_Herde")
WIS_Tier = Class(name="WIS_Tier")
WIS_WeideBemerkung = Class(name="WIS_WeideBemerkung")
WIS_HiTierImport = Class(name="WIS_HiTierImport")
Actor_Actor = Class(name="Actor_Actor")
UseCase_UseCase = Class(name="UseCase_UseCase")

# Benutzer class attributes and methods
Benutzer_name: Property = Property(name="name", type=StringType)
Benutzer_passwortHash: Property = Property(name="passwortHash", type=StringType)
Benutzer.attributes={Benutzer_name, Benutzer_passwortHash}

# Weidegang2 class attributes and methods
Weidegang2_datum: Property = Property(name="datum", type=StringType)
Weidegang2_herdeName: Property = Property(name="herdeName", type=StringType)
Weidegang2_herdeFarbe: Property = Property(name="herdeFarbe", type=StringType)
Weidegang2_tierName: Property = Property(name="tierName", type=StringType)
Weidegang2_istAusgefallen: Property = Property(name="istAusgefallen", type=BooleanType)
Weidegang2_ausfallgrund: Property = Property(name="ausfallgrund", type=StringType)
Weidegang2_weideName: Property = Property(name="weideName", type=StringType)
Weidegang2_weideSchlagnummer: Property = Property(name="weideSchlagnummer", type=StringType)
Weidegang2_weideFACTCode: Property = Property(name="weideFACTCode", type=StringType)
Weidegang2.attributes={Weidegang2_weideSchlagnummer, Weidegang2_herdeFarbe, Weidegang2_weideName, Weidegang2_ausfallgrund, Weidegang2_datum, Weidegang2_tierName, Weidegang2_herdeName, Weidegang2_weideFACTCode, Weidegang2_istAusgefallen}

# WIS_Weidefl_che class attributes and methods
WIS_Weidefl_che_groesse: Property = Property(name="groesse", type=IntegerType)
WIS_Weidefl_che_farbe: Property = Property(name="farbe", type=StringType)
WIS_Weidefl_che_name: Property = Property(name="name", type=StringType)
WIS_Weidefl_che_schlagnummer: Property = Property(name="schlagnummer", type=StringType)
WIS_Weidefl_che.attributes={WIS_Weidefl_che_farbe, WIS_Weidefl_che_groesse, WIS_Weidefl_che_name, WIS_Weidefl_che_schlagnummer}

# WIS_Weide class attributes and methods
WIS_Weide_name: Property = Property(name="name", type=StringType)
WIS_Weide_schlagnummer: Property = Property(name="schlagnummer", type=IntegerType)
WIS_Weide_groesse: Property = Property(name="groesse", type=IntegerType)
WIS_Weide_FACTCode: Property = Property(name="FACTCode", type=IntegerType)
WIS_Weide_farbe: Property = Property(name="farbe", type=StringType)
WIS_Weide_istBetriebsfremdeFlaeche: Property = Property(name="istBetriebsfremdeFlaeche", type=BooleanType)
WIS_Weide_LPRVertrag: Property = Property(name="LPRVertrag", type=StringType)
WIS_Weide_istAktiv: Property = Property(name="istAktiv", type=BooleanType)
WIS_Weide_bemerkung: Property = Property(name="bemerkung", type=StringType)
WIS_Weide.attributes={WIS_Weide_LPRVertrag, WIS_Weide_schlagnummer, WIS_Weide_istBetriebsfremdeFlaeche, WIS_Weide_bemerkung, WIS_Weide_FACTCode, WIS_Weide_groesse, WIS_Weide_name, WIS_Weide_farbe, WIS_Weide_istAktiv}

# WIS_Weidegang class attributes and methods
WIS_Weidegang_datum: Property = Property(name="datum", type=StringType)
WIS_Weidegang_herdeName: Property = Property(name="herdeName", type=StringType)
WIS_Weidegang_herdeFarbe: Property = Property(name="herdeFarbe", type=StringType)
WIS_Weidegang_tierName: Property = Property(name="tierName", type=StringType)
WIS_Weidegang_istAusgefallen: Property = Property(name="istAusgefallen", type=BooleanType)
WIS_Weidegang_ausfallgrund: Property = Property(name="ausfallgrund", type=StringType)
WIS_Weidegang_weideName: Property = Property(name="weideName", type=StringType)
WIS_Weidegang_weideSchlagnummer: Property = Property(name="weideSchlagnummer", type=StringType)
WIS_Weidegang_weideFACTCode: Property = Property(name="weideFACTCode", type=StringType)
WIS_Weidegang_tierLOM: Property = Property(name="tierLOM", type=StringType)
WIS_Weidegang.attributes={WIS_Weidegang_datum, WIS_Weidegang_weideFACTCode, WIS_Weidegang_ausfallgrund, WIS_Weidegang_herdeName, WIS_Weidegang_weideSchlagnummer, WIS_Weidegang_tierLOM, WIS_Weidegang_tierName, WIS_Weidegang_istAusgefallen, WIS_Weidegang_weideName, WIS_Weidegang_herdeFarbe}

# WIS_Herde class attributes and methods
WIS_Herde_name: Property = Property(name="name", type=StringType)
WIS_Herde.attributes={WIS_Herde_name}

# WIS_Tier class attributes and methods
WIS_Tier_LOM: Property = Property(name="LOM", type=IntegerType)
WIS_Tier_name: Property = Property(name="name", type=StringType)
WIS_Tier_transponderNummer: Property = Property(name="transponderNummer", type=StringType)
WIS_Tier_geburtsdatum: Property = Property(name="geburtsdatum", type=StringType)
WIS_Tier_istWeiblich: Property = Property(name="istWeiblich", type=BooleanType)
WIS_Tier_eigeneAngaben: Property = Property(name="eigeneAngaben", type=StringType)
WIS_Tier_letzteKalbung: Property = Property(name="letzteKalbung", type=StringType)
WIS_Tier_istAktiv: Property = Property(name="istAktiv", type=BooleanType)
WIS_Tier_UDNummer: Property = Property(name="UDNummer", type=StringType)
WIS_Tier_BTV4: Property = Property(name="BTV4", type=StringType)
WIS_Tier_BTV8: Property = Property(name="BTV8", type=StringType)
WIS_Tier.attributes={WIS_Tier_BTV4, WIS_Tier_transponderNummer, WIS_Tier_eigeneAngaben, WIS_Tier_letzteKalbung, WIS_Tier_LOM, WIS_Tier_name, WIS_Tier_istWeiblich, WIS_Tier_BTV8, WIS_Tier_geburtsdatum, WIS_Tier_UDNummer, WIS_Tier_istAktiv}

# WIS_WeideBemerkung class attributes and methods
WIS_WeideBemerkung_datum: Property = Property(name="datum", type=StringType)
WIS_WeideBemerkung_bemerkung: Property = Property(name="bemerkung", type=StringType)
WIS_WeideBemerkung_weideFACTCode: Property = Property(name="weideFACTCode", type=StringType)
WIS_WeideBemerkung_weideSchlagnummer: Property = Property(name="weideSchlagnummer", type=StringType)
WIS_WeideBemerkung_weideName: Property = Property(name="weideName", type=StringType)
WIS_WeideBemerkung.attributes={WIS_WeideBemerkung_bemerkung, WIS_WeideBemerkung_weideName, WIS_WeideBemerkung_weideSchlagnummer, WIS_WeideBemerkung_weideFACTCode, WIS_WeideBemerkung_datum}

# WIS_HiTierImport class attributes and methods
WIS_HiTierImport_datum: Property = Property(name="datum", type=StringType)
WIS_HiTierImport.attributes={WIS_HiTierImport_datum}

# Actor_Actor class attributes and methods

# UseCase_UseCase class attributes and methods

# Relationships
Tier_Benutzer: BinaryAssociation = BinaryAssociation(
    name="Tier_Benutzer",
    ends={
        Property(name="benutzer0", type=Benutzer, multiplicity=Multiplicity(1, 1)),
        Property(name="tier1", type=WIS_Tier, multiplicity=Multiplicity(0, 9999))
    }
)
Weide_Weidefl_che: BinaryAssociation = BinaryAssociation(
    name="Weide_Weidefl_che",
    ends={
        Property(name="teilflaeche2", type=WIS_Weidefl_che, multiplicity=Multiplicity(0, 9999)),
        Property(name="weide3", type=WIS_Weide, multiplicity=Multiplicity(1, 1))
    }
)
Weidegang_Weide: BinaryAssociation = BinaryAssociation(
    name="Weidegang_Weide",
    ends={
        Property(name="weide4", type=WIS_Weide, multiplicity=Multiplicity(1, 1)),
        Property(name="weidegang5", type=WIS_Weidegang, multiplicity=Multiplicity(0, 9999))
    }
)
Weidegang_Herde: BinaryAssociation = BinaryAssociation(
    name="Weidegang_Herde",
    ends={
        Property(name="herde6", type=WIS_Herde, multiplicity=Multiplicity(1, 1)),
        Property(name="weidegang7", type=WIS_Weidegang, multiplicity=Multiplicity(0, 9999))
    }
)
Tier_Herde: BinaryAssociation = BinaryAssociation(
    name="Tier_Herde",
    ends={
        Property(name="herde8", type=WIS_Herde, multiplicity=Multiplicity(0, 1)),
        Property(name="tier9", type=WIS_Tier, multiplicity=Multiplicity(0, 9999))
    }
)
Weidegang_Tier: BinaryAssociation = BinaryAssociation(
    name="Weidegang_Tier",
    ends={
        Property(name="tier10", type=WIS_Tier, multiplicity=Multiplicity(1, 1)),
        Property(name="weidegang11", type=WIS_Weidegang, multiplicity=Multiplicity(0, 9999))
    }
)
Herde_Benutzer: BinaryAssociation = BinaryAssociation(
    name="Herde_Benutzer",
    ends={
        Property(name="benutzer12", type=Benutzer, multiplicity=Multiplicity(1, 1)),
        Property(name="herde13", type=WIS_Herde, multiplicity=Multiplicity(0, 9999))
    }
)
Weidegang_Benutzer: BinaryAssociation = BinaryAssociation(
    name="Weidegang_Benutzer",
    ends={
        Property(name="benutzer14", type=Benutzer, multiplicity=Multiplicity(1, 1)),
        Property(name="weidegang15", type=WIS_Weidegang, multiplicity=Multiplicity(0, 9999))
    }
)
Weide_Benutzer: BinaryAssociation = BinaryAssociation(
    name="Weide_Benutzer",
    ends={
        Property(name="benutzer16", type=Benutzer, multiplicity=Multiplicity(0, 1)),
        Property(name="weide17", type=WIS_Weide, multiplicity=Multiplicity(0, 1))
    }
)
HiTierImport_Benutzer: BinaryAssociation = BinaryAssociation(
    name="HiTierImport_Benutzer",
    ends={
        Property(name="benutzer18", type=Benutzer, multiplicity=Multiplicity(1, 1)),
        Property(name="hiTierImport19", type=WIS_HiTierImport, multiplicity=Multiplicity(0, 1))
    }
)
Tier_HiTierImport: BinaryAssociation = BinaryAssociation(
    name="Tier_HiTierImport",
    ends={
        Property(name="hiTierImport20", type=WIS_HiTierImport, multiplicity=Multiplicity(1, 1)),
        Property(name="tier21", type=WIS_Tier, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_c0wpEMGgEemphpAvuifT8g",
    types={Benutzer, Weidegang2, WIS_Weidefl_che, WIS_Weide, WIS_Weidegang, WIS_Herde, WIS_Tier, WIS_WeideBemerkung, WIS_HiTierImport, Actor_Actor, UseCase_UseCase},
    associations={Tier_Benutzer, Weide_Weidefl_che, Weidegang_Weide, Weidegang_Herde, Tier_Herde, Weidegang_Tier, Herde_Benutzer, Weidegang_Benutzer, Weide_Benutzer, HiTierImport_Benutzer, Tier_HiTierImport},
    generalizations={},
    metadata=None
)

###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)