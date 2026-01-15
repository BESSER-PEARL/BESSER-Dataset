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
Sex: Enumeration = Enumeration(
    name="Sex",
    literals={
            EnumerationLiteral(name="F"),
			EnumerationLiteral(name="M"),
			EnumerationLiteral(name="C"),
			EnumerationLiteral(name="S"),
			EnumerationLiteral(name="Unspecified")
    }
)

BisonBreed: Enumeration = Enumeration(
    name="BisonBreed",
    literals={
            EnumerationLiteral(name="WO"),
			EnumerationLiteral(name="PB"),
			EnumerationLiteral(name="Unspecified")
    }
)

SheepBreed: Enumeration = Enumeration(
    name="SheepBreed",
    literals={
            EnumerationLiteral(name="DL"),
			EnumerationLiteral(name="ER"),
			EnumerationLiteral(name="CD"),
			EnumerationLiteral(name="OU"),
			EnumerationLiteral(name="RI"),
			EnumerationLiteral(name="LY"),
			EnumerationLiteral(name="FB"),
			EnumerationLiteral(name="BW"),
			EnumerationLiteral(name="BF"),
			EnumerationLiteral(name="BO"),
			EnumerationLiteral(name="BC"),
			EnumerationLiteral(name="CO"),
			EnumerationLiteral(name="CF"),
			EnumerationLiteral(name="CL"),
			EnumerationLiteral(name="CP"),
			EnumerationLiteral(name="CR"),
			EnumerationLiteral(name="DH"),
			EnumerationLiteral(name="DP"),
			EnumerationLiteral(name="ST"),
			EnumerationLiteral(name="SU"),
			EnumerationLiteral(name="FN"),
			EnumerationLiteral(name="HS"),
			EnumerationLiteral(name="HY"),
			EnumerationLiteral(name="IL"),
			EnumerationLiteral(name="KK"),
			EnumerationLiteral(name="KA"),
			EnumerationLiteral(name="KH"),
			EnumerationLiteral(name="BL"),
			EnumerationLiteral(name="LE"),
			EnumerationLiteral(name="HL"),
			EnumerationLiteral(name="LI"),
			EnumerationLiteral(name="MM"),
			EnumerationLiteral(name="MP"),
			EnumerationLiteral(name="MT"),
			EnumerationLiteral(name="NL"),
			EnumerationLiteral(name="NC"),
			EnumerationLiteral(name="OX"),
			EnumerationLiteral(name="PE"),
			EnumerationLiteral(name="PO"),
			EnumerationLiteral(name="RG"),
			EnumerationLiteral(name="RV"),
			EnumerationLiteral(name="RM"),
			EnumerationLiteral(name="RY"),
			EnumerationLiteral(name="SX"),
			EnumerationLiteral(name="SC"),
			EnumerationLiteral(name="SL"),
			EnumerationLiteral(name="SR"),
			EnumerationLiteral(name="TA"),
			EnumerationLiteral(name="TX"),
			EnumerationLiteral(name="TU"),
			EnumerationLiteral(name="XL"),
			EnumerationLiteral(name="XM"),
			EnumerationLiteral(name="ZS"),
			EnumerationLiteral(name="Unspecified")
    }
)

BeefBreed: Enumeration = Enumeration(
    name="BeefBreed",
    literals={
            EnumerationLiteral(name="BM"),
			EnumerationLiteral(name="BB"),
			EnumerationLiteral(name="BG"),
			EnumerationLiteral(name="AN"),
			EnumerationLiteral(name="AB"),
			EnumerationLiteral(name="AF"),
			EnumerationLiteral(name="AL"),
			EnumerationLiteral(name="AE"),
			EnumerationLiteral(name="AM"),
			EnumerationLiteral(name="AK"),
			EnumerationLiteral(name="AW"),
			EnumerationLiteral(name="AU"),
			EnumerationLiteral(name="BA"),
			EnumerationLiteral(name="BF"),
			EnumerationLiteral(name="BE"),
			EnumerationLiteral(name="DR"),
			EnumerationLiteral(name="DL"),
			EnumerationLiteral(name="FP"),
			EnumerationLiteral(name="BD"),
			EnumerationLiteral(name="NS"),
			EnumerationLiteral(name="BO"),
			EnumerationLiteral(name="BR"),
			EnumerationLiteral(name="BH"),
			EnumerationLiteral(name="BI"),
			EnumerationLiteral(name="BL"),
			EnumerationLiteral(name="BN"),
			EnumerationLiteral(name="BU"),
			EnumerationLiteral(name="BW"),
			EnumerationLiteral(name="SB"),
			EnumerationLiteral(name="BQ"),
			EnumerationLiteral(name="CP"),
			EnumerationLiteral(name="CN"),
			EnumerationLiteral(name="CB"),
			EnumerationLiteral(name="CH"),
			EnumerationLiteral(name="CG"),
			EnumerationLiteral(name="CM"),
			EnumerationLiteral(name="CA"),
			EnumerationLiteral(name="XX"),
			EnumerationLiteral(name="XT"),
			EnumerationLiteral(name="CU"),
			EnumerationLiteral(name="DB"),
			EnumerationLiteral(name="DJ"),
			EnumerationLiteral(name="RW"),
			EnumerationLiteral(name="DE"),
			EnumerationLiteral(name="KB"),
			EnumerationLiteral(name="ER"),
			EnumerationLiteral(name="FA"),
			EnumerationLiteral(name="FL"),
			EnumerationLiteral(name="FC"),
			EnumerationLiteral(name="FR"),
			EnumerationLiteral(name="FB"),
			EnumerationLiteral(name="DF"),
			EnumerationLiteral(name="GA"),
			EnumerationLiteral(name="GS"),
			EnumerationLiteral(name="GE"),
			EnumerationLiteral(name="GV"),
			EnumerationLiteral(name="GI"),
			EnumerationLiteral(name="GR"),
			EnumerationLiteral(name="GZ"),
			EnumerationLiteral(name="GY"),
			EnumerationLiteral(name="HC"),
			EnumerationLiteral(name="HB"),
			EnumerationLiteral(name="HH"),
			EnumerationLiteral(name="HP"),
			EnumerationLiteral(name="SH"),
			EnumerationLiteral(name="HY"),
			EnumerationLiteral(name="IB"),
			EnumerationLiteral(name="KY"),
			EnumerationLiteral(name="RB"),
			EnumerationLiteral(name="LM"),
			EnumerationLiteral(name="RD"),
			EnumerationLiteral(name="LR"),
			EnumerationLiteral(name="RP"),
			EnumerationLiteral(name="LO"),
			EnumerationLiteral(name="RN"),
			EnumerationLiteral(name="LU"),
			EnumerationLiteral(name="MA"),
			EnumerationLiteral(name="MH"),
			EnumerationLiteral(name="ML"),
			EnumerationLiteral(name="MR"),
			EnumerationLiteral(name="ME"),
			EnumerationLiteral(name="MI"),
			EnumerationLiteral(name="MC"),
			EnumerationLiteral(name="MO"),
			EnumerationLiteral(name="MU"),
			EnumerationLiteral(name="MG"),
			EnumerationLiteral(name="NE"),
			EnumerationLiteral(name="NM"),
			EnumerationLiteral(name="NR"),
			EnumerationLiteral(name="PA"),
			EnumerationLiteral(name="PR"),
			EnumerationLiteral(name="PI"),
			EnumerationLiteral(name="PZ"),
			EnumerationLiteral(name="RA"),
			EnumerationLiteral(name="AR"),
			EnumerationLiteral(name="RR"),
			EnumerationLiteral(name="TN"),
			EnumerationLiteral(name="TL"),
			EnumerationLiteral(name="TI"),
			EnumerationLiteral(name="RS"),
			EnumerationLiteral(name="RO"),
			EnumerationLiteral(name="DN"),
			EnumerationLiteral(name="SW"),
			EnumerationLiteral(name="SA"),
			EnumerationLiteral(name="SG"),
			EnumerationLiteral(name="SL"),
			EnumerationLiteral(name="SE"),
			EnumerationLiteral(name="SV"),
			EnumerationLiteral(name="SS"),
			EnumerationLiteral(name="IS"),
			EnumerationLiteral(name="SP"),
			EnumerationLiteral(name="SI"),
			EnumerationLiteral(name="SM"),
			EnumerationLiteral(name="DS"),
			EnumerationLiteral(name="SX"),
			EnumerationLiteral(name="TP"),
			EnumerationLiteral(name="TA"),
			EnumerationLiteral(name="TG"),
			EnumerationLiteral(name="WB"),
			EnumerationLiteral(name="WF"),
			EnumerationLiteral(name="WP"),
			EnumerationLiteral(name="YA"),
			EnumerationLiteral(name="Unspecified")
    }
)

DairyBreed: Enumeration = Enumeration(
    name="DairyBreed",
    literals={
            EnumerationLiteral(name="LD"),
			EnumerationLiteral(name="AY"),
			EnumerationLiteral(name="BS"),
			EnumerationLiteral(name="GD"),
			EnumerationLiteral(name="GU"),
			EnumerationLiteral(name="HO"),
			EnumerationLiteral(name="JE"),
			EnumerationLiteral(name="WW"),
			EnumerationLiteral(name="FM"),
			EnumerationLiteral(name="MS"),
			EnumerationLiteral(name="Unspecified")
    }
)

SwineBreed: Enumeration = Enumeration(
    name="SwineBreed",
    literals={
            EnumerationLiteral(name="WS"),
			EnumerationLiteral(name="YO"),
			EnumerationLiteral(name="Unspecified"),
			EnumerationLiteral(name="BK"),
			EnumerationLiteral(name="CW"),
			EnumerationLiteral(name="DU"),
			EnumerationLiteral(name="HA"),
			EnumerationLiteral(name="LC"),
			EnumerationLiteral(name="LA"),
			EnumerationLiteral(name="LB"),
			EnumerationLiteral(name="LW"),
			EnumerationLiteral(name="PE"),
			EnumerationLiteral(name="PC"),
			EnumerationLiteral(name="RW"),
			EnumerationLiteral(name="SO"),
			EnumerationLiteral(name="TM")
    }
)

# Classes
tracker_AnimalId = Class(name="tracker::AnimalId")
tracker_Animal = Class(name="tracker::Animal", is_abstract=True)
tracker_Bovine = Class(name="tracker::Bovine", is_abstract=True)
Animal = Class(name="Animal")
tracker_Event = Class(name="tracker::Event", is_abstract=True)
tracker_TagAllocated = Class(name="tracker::TagAllocated")
Event = Class(name="Event")
tracker_Premises = Class(name="tracker::Premises")
tracker_Animals = Class(name="tracker::Animals")
tracker_EventHistory = Class(name="tracker::EventHistory")
tracker_UnAppliedTags = Class(name="tracker::UnAppliedTags")
tracker_BovineBeef = Class(name="tracker::BovineBeef")
Bovine = Class(name="Bovine")
tracker_Ovine = Class(name="tracker::Ovine")
tracker_BovineBison = Class(name="tracker::BovineBison")
tracker_BovineDairy = Class(name="tracker::BovineDairy", is_abstract=True)
tracker_FairRegistration = Class(name="tracker::FairRegistration")
tracker_TagApplied = Class(name="tracker::TagApplied")
tracker_MovedIn = Class(name="tracker::MovedIn")
tracker_MovedOut = Class(name="tracker::MovedOut")
tracker_LostTag = Class(name="tracker::LostTag")
tracker_ReplacedTag = Class(name="tracker::ReplacedTag")
tracker_Imported = Class(name="tracker::Imported")
tracker_Exported = Class(name="tracker::Exported")
tracker_Sighting = Class(name="tracker::Sighting")
tracker_Slaughtered = Class(name="tracker::Slaughtered")
tracker_Died = Class(name="tracker::Died")
tracker_TagRetired = Class(name="tracker::TagRetired")
tracker_AnimalMissing = Class(name="tracker::AnimalMissing")
tracker_ICVI = Class(name="tracker::ICVI")
tracker_Swine = Class(name="tracker::Swine")
tracker_WeighIn = Class(name="tracker::WeighIn")

# tracker_AnimalId class attributes and methods
tracker_AnimalId_idNumber: Property = Property(name="idNumber", type=StringType)
tracker_AnimalId_usainNumberUsed: Property = Property(name="usainNumberUsed", type=BooleanType)
tracker_AnimalId.attributes={tracker_AnimalId_usainNumberUsed, tracker_AnimalId_idNumber}

# tracker_Animal class attributes and methods
tracker_Animal_birthDate: Property = Property(name="birthDate", type=StringType)
tracker_Animal_sex: Property = Property(name="sex", type=StringType)
tracker_Animal_species: Property = Property(name="species", type=StringType)
tracker_Animal_idNumber: Property = Property(name="idNumber", type=StringType)
tracker_Animal_breed: Property = Property(name="breed", type=StringType)
tracker_Animal_age: Property = Property(name="age", type=StringType)
tracker_Animal_sexCode: Property = Property(name="sexCode", type=StringType)
tracker_Animal_speciesCode: Property = Property(name="speciesCode", type=StringType)
tracker_Animal.attributes={tracker_Animal_idNumber, tracker_Animal_species, tracker_Animal_sex, tracker_Animal_age, tracker_Animal_breed, tracker_Animal_sexCode, tracker_Animal_birthDate, tracker_Animal_speciesCode}

# tracker_Bovine class attributes and methods

# Animal class attributes and methods

# tracker_Event class attributes and methods
tracker_Event_dateTime: Property = Property(name="dateTime", type=StringType)
tracker_Event_eventCode: Property = Property(name="eventCode", type=IntegerType)
tracker_Event_electronicallyRead: Property = Property(name="electronicallyRead", type=BooleanType)
tracker_Event_correction: Property = Property(name="correction", type=BooleanType)
tracker_Event_comments: Property = Property(name="comments", type=StringType)
tracker_Event_id: Property = Property(name="id", type=StringType)
tracker_Event.attributes={tracker_Event_correction, tracker_Event_id, tracker_Event_dateTime, tracker_Event_eventCode, tracker_Event_comments, tracker_Event_electronicallyRead}

# tracker_TagAllocated class attributes and methods

# Event class attributes and methods

# tracker_Premises class attributes and methods
tracker_Premises_premisesId: Property = Property(name="premisesId", type=StringType)
tracker_Premises_emailContact: Property = Property(name="emailContact", type=StringType)
tracker_Premises.attributes={tracker_Premises_premisesId, tracker_Premises_emailContact}

# tracker_Animals class attributes and methods

# tracker_EventHistory class attributes and methods

# tracker_UnAppliedTags class attributes and methods

# tracker_BovineBeef class attributes and methods
tracker_BovineBeef_beefBreed: Property = Property(name="beefBreed", type=StringType)
tracker_BovineBeef.attributes={tracker_BovineBeef_beefBreed}

# Bovine class attributes and methods

# tracker_Ovine class attributes and methods
tracker_Ovine_sheepBreed: Property = Property(name="sheepBreed", type=StringType)
tracker_Ovine.attributes={tracker_Ovine_sheepBreed}

# tracker_BovineBison class attributes and methods
tracker_BovineBison_buffaloBreed: Property = Property(name="buffaloBreed", type=StringType)
tracker_BovineBison.attributes={tracker_BovineBison_buffaloBreed}

# tracker_BovineDairy class attributes and methods
tracker_BovineDairy_dairyBreed: Property = Property(name="dairyBreed", type=StringType)
tracker_BovineDairy.attributes={tracker_BovineDairy_dairyBreed}

# tracker_FairRegistration class attributes and methods
tracker_FairRegistration_participant: Property = Property(name="participant", type=StringType)
tracker_FairRegistration_address: Property = Property(name="address", type=StringType)
tracker_FairRegistration_phone: Property = Property(name="phone", type=StringType)
tracker_FairRegistration_parent: Property = Property(name="parent", type=StringType)
tracker_FairRegistration_club: Property = Property(name="club", type=StringType)
tracker_FairRegistration.attributes={tracker_FairRegistration_club, tracker_FairRegistration_participant, tracker_FairRegistration_phone, tracker_FairRegistration_parent, tracker_FairRegistration_address}

# tracker_TagApplied class attributes and methods

# tracker_MovedIn class attributes and methods
tracker_MovedIn_sourcePin: Property = Property(name="sourcePin", type=StringType)
tracker_MovedIn.attributes={tracker_MovedIn_sourcePin}

# tracker_MovedOut class attributes and methods
tracker_MovedOut_destinationPin: Property = Property(name="destinationPin", type=StringType)
tracker_MovedOut.attributes={tracker_MovedOut_destinationPin}

# tracker_LostTag class attributes and methods

# tracker_ReplacedTag class attributes and methods
tracker_ReplacedTag_oldAin: Property = Property(name="oldAin", type=StringType)
tracker_ReplacedTag.attributes={tracker_ReplacedTag_oldAin}

# tracker_Imported class attributes and methods

# tracker_Exported class attributes and methods

# tracker_Sighting class attributes and methods

# tracker_Slaughtered class attributes and methods

# tracker_Died class attributes and methods

# tracker_TagRetired class attributes and methods

# tracker_AnimalMissing class attributes and methods

# tracker_ICVI class attributes and methods

# tracker_Swine class attributes and methods
tracker_Swine_swineBreed: Property = Property(name="swineBreed", type=StringType)
tracker_Swine.attributes={tracker_Swine_swineBreed}

# tracker_WeighIn class attributes and methods
tracker_WeighIn_weight: Property = Property(name="weight", type=IntegerType)
tracker_WeighIn.attributes={tracker_WeighIn_weight}

# Relationships
ain0: BinaryAssociation = BinaryAssociation(
    name="ain0",
    ends={
        Property(name="tracker_AnimalId", type=tracker_Animal, multiplicity=Multiplicity(1, 1)),
        Property(name="tracker_Animal", type=tracker_AnimalId, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ain1: BinaryAssociation = BinaryAssociation(
    name="ain1",
    ends={
        Property(name="tracker_AnimalId2", type=tracker_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="tracker_Event", type=tracker_AnimalId, multiplicity=Multiplicity(1, 1))
    }
)
animals3: BinaryAssociation = BinaryAssociation(
    name="animals3",
    ends={
        Property(name="tracker_Animals", type=tracker_Premises, multiplicity=Multiplicity(1, 1)),
        Property(name="tracker_Premises", type=tracker_Animals, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
eventHistory4: BinaryAssociation = BinaryAssociation(
    name="eventHistory4",
    ends={
        Property(name="tracker_EventHistory", type=tracker_Premises, multiplicity=Multiplicity(1, 1)),
        Property(name="tracker_Premises5", type=tracker_EventHistory, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
unAppliedTags6: BinaryAssociation = BinaryAssociation(
    name="unAppliedTags6",
    ends={
        Property(name="tracker_UnAppliedTags", type=tracker_Premises, multiplicity=Multiplicity(1, 1)),
        Property(name="tracker_Premises7", type=tracker_UnAppliedTags, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
events8: BinaryAssociation = BinaryAssociation(
    name="events8",
    ends={
        Property(name="tracker_Event10", type=tracker_EventHistory, multiplicity=Multiplicity(1, 1)),
        Property(name="tracker_EventHistory9", type=tracker_Event, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
animal11: BinaryAssociation = BinaryAssociation(
    name="animal11",
    ends={
        Property(name="tracker_Animal13", type=tracker_Animals, multiplicity=Multiplicity(1, 1)),
        Property(name="tracker_Animals12", type=tracker_Animal, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
ain14: BinaryAssociation = BinaryAssociation(
    name="ain14",
    ends={
        Property(name="tracker_AnimalId16", type=tracker_UnAppliedTags, multiplicity=Multiplicity(1, 1)),
        Property(name="tracker_UnAppliedTags15", type=tracker_AnimalId, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_tracker_Bovine_Animal = Generalization(general=Animal, specific=tracker_Bovine)
gen_tracker_TagAllocated_Event = Generalization(general=Event, specific=tracker_TagAllocated)
gen_tracker_BovineBeef_Bovine = Generalization(general=Bovine, specific=tracker_BovineBeef)
gen_tracker_Ovine_Animal = Generalization(general=Animal, specific=tracker_Ovine)
gen_tracker_BovineBison_Bovine = Generalization(general=Bovine, specific=tracker_BovineBison)
gen_tracker_BovineDairy_Bovine = Generalization(general=Bovine, specific=tracker_BovineDairy)
gen_tracker_FairRegistration_Event = Generalization(general=Event, specific=tracker_FairRegistration)
gen_tracker_TagApplied_Event = Generalization(general=Event, specific=tracker_TagApplied)
gen_tracker_MovedIn_Event = Generalization(general=Event, specific=tracker_MovedIn)
gen_tracker_MovedOut_Event = Generalization(general=Event, specific=tracker_MovedOut)
gen_tracker_LostTag_Event = Generalization(general=Event, specific=tracker_LostTag)
gen_tracker_ReplacedTag_Event = Generalization(general=Event, specific=tracker_ReplacedTag)
gen_tracker_Imported_Event = Generalization(general=Event, specific=tracker_Imported)
gen_tracker_Exported_Event = Generalization(general=Event, specific=tracker_Exported)
gen_tracker_Sighting_Event = Generalization(general=Event, specific=tracker_Sighting)
gen_tracker_Slaughtered_Event = Generalization(general=Event, specific=tracker_Slaughtered)
gen_tracker_Died_Event = Generalization(general=Event, specific=tracker_Died)
gen_tracker_TagRetired_Event = Generalization(general=Event, specific=tracker_TagRetired)
gen_tracker_AnimalMissing_Event = Generalization(general=Event, specific=tracker_AnimalMissing)
gen_tracker_ICVI_Event = Generalization(general=Event, specific=tracker_ICVI)
gen_tracker_Swine_Animal = Generalization(general=Animal, specific=tracker_Swine)
gen_tracker_WeighIn_Event = Generalization(general=Event, specific=tracker_WeighIn)

# Domain Model
domain_model = DomainModel(
    name="tracker",
    types={tracker_AnimalId, tracker_Animal, tracker_Bovine, Animal, tracker_Event, tracker_TagAllocated, Event, tracker_Premises, tracker_Animals, tracker_EventHistory, tracker_UnAppliedTags, tracker_BovineBeef, Bovine, tracker_Ovine, tracker_BovineBison, tracker_BovineDairy, tracker_FairRegistration, tracker_TagApplied, tracker_MovedIn, tracker_MovedOut, tracker_LostTag, tracker_ReplacedTag, tracker_Imported, tracker_Exported, tracker_Sighting, tracker_Slaughtered, tracker_Died, tracker_TagRetired, tracker_AnimalMissing, tracker_ICVI, tracker_Swine, tracker_WeighIn, Sex, BisonBreed, SheepBreed, BeefBreed, DairyBreed, SwineBreed},
    associations={ain0, ain1, animals3, eventHistory4, unAppliedTags6, events8, animal11, ain14},
    generalizations={gen_tracker_Bovine_Animal, gen_tracker_TagAllocated_Event, gen_tracker_BovineBeef_Bovine, gen_tracker_Ovine_Animal, gen_tracker_BovineBison_Bovine, gen_tracker_BovineDairy_Bovine, gen_tracker_FairRegistration_Event, gen_tracker_TagApplied_Event, gen_tracker_MovedIn_Event, gen_tracker_MovedOut_Event, gen_tracker_LostTag_Event, gen_tracker_ReplacedTag_Event, gen_tracker_Imported_Event, gen_tracker_Exported_Event, gen_tracker_Sighting_Event, gen_tracker_Slaughtered_Event, gen_tracker_Died_Event, gen_tracker_TagRetired_Event, gen_tracker_AnimalMissing_Event, gen_tracker_ICVI_Event, gen_tracker_Swine_Animal, gen_tracker_WeighIn_Event},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)