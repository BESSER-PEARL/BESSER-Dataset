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
            EnumerationLiteral(name="Unspecified"),
			EnumerationLiteral(name="F"),
			EnumerationLiteral(name="M"),
			EnumerationLiteral(name="C"),
			EnumerationLiteral(name="S")
    }
)

SheepBreed: Enumeration = Enumeration(
    name="SheepBreed",
    literals={
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
			EnumerationLiteral(name="DL"),
			EnumerationLiteral(name="ER"),
			EnumerationLiteral(name="FN"),
			EnumerationLiteral(name="HS"),
			EnumerationLiteral(name="HY"),
			EnumerationLiteral(name="SR"),
			EnumerationLiteral(name="IL"),
			EnumerationLiteral(name="ST"),
			EnumerationLiteral(name="KK"),
			EnumerationLiteral(name="SU"),
			EnumerationLiteral(name="KA"),
			EnumerationLiteral(name="TA"),
			EnumerationLiteral(name="KH"),
			EnumerationLiteral(name="TX"),
			EnumerationLiteral(name="BL"),
			EnumerationLiteral(name="TU"),
			EnumerationLiteral(name="LE"),
			EnumerationLiteral(name="XL"),
			EnumerationLiteral(name="HL"),
			EnumerationLiteral(name="XM"),
			EnumerationLiteral(name="LI"),
			EnumerationLiteral(name="MM"),
			EnumerationLiteral(name="ZS"),
			EnumerationLiteral(name="MP"),
			EnumerationLiteral(name="Unspecified"),
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
			EnumerationLiteral(name="SL")
    }
)

BisonBreed: Enumeration = Enumeration(
    name="BisonBreed",
    literals={
            EnumerationLiteral(name="PB"),
			EnumerationLiteral(name="Unspecified"),
			EnumerationLiteral(name="WO")
    }
)

BeefBreed: Enumeration = Enumeration(
    name="BeefBreed",
    literals={
            EnumerationLiteral(name="AN"),
			EnumerationLiteral(name="AB"),
			EnumerationLiteral(name="AF"),
			EnumerationLiteral(name="AL"),
			EnumerationLiteral(name="CB"),
			EnumerationLiteral(name="AE"),
			EnumerationLiteral(name="CH"),
			EnumerationLiteral(name="AM"),
			EnumerationLiteral(name="CG"),
			EnumerationLiteral(name="AK"),
			EnumerationLiteral(name="CM"),
			EnumerationLiteral(name="AW"),
			EnumerationLiteral(name="CA"),
			EnumerationLiteral(name="AU"),
			EnumerationLiteral(name="BA"),
			EnumerationLiteral(name="XX"),
			EnumerationLiteral(name="BF"),
			EnumerationLiteral(name="XT"),
			EnumerationLiteral(name="BE"),
			EnumerationLiteral(name="CU"),
			EnumerationLiteral(name="BM"),
			EnumerationLiteral(name="DB"),
			EnumerationLiteral(name="BB"),
			EnumerationLiteral(name="DJ"),
			EnumerationLiteral(name="BG"),
			EnumerationLiteral(name="RW"),
			EnumerationLiteral(name="BD"),
			EnumerationLiteral(name="DE"),
			EnumerationLiteral(name="NS"),
			EnumerationLiteral(name="BO"),
			EnumerationLiteral(name="DR"),
			EnumerationLiteral(name="BR"),
			EnumerationLiteral(name="DL"),
			EnumerationLiteral(name="BH"),
			EnumerationLiteral(name="FP"),
			EnumerationLiteral(name="BI"),
			EnumerationLiteral(name="ER"),
			EnumerationLiteral(name="BL"),
			EnumerationLiteral(name="BN"),
			EnumerationLiteral(name="FA"),
			EnumerationLiteral(name="BU"),
			EnumerationLiteral(name="FL"),
			EnumerationLiteral(name="BW"),
			EnumerationLiteral(name="FC"),
			EnumerationLiteral(name="SB"),
			EnumerationLiteral(name="FR"),
			EnumerationLiteral(name="BQ"),
			EnumerationLiteral(name="FB"),
			EnumerationLiteral(name="CP"),
			EnumerationLiteral(name="DF"),
			EnumerationLiteral(name="CN"),
			EnumerationLiteral(name="GA"),
			EnumerationLiteral(name="ML"),
			EnumerationLiteral(name="GS"),
			EnumerationLiteral(name="MR"),
			EnumerationLiteral(name="GE"),
			EnumerationLiteral(name="ME"),
			EnumerationLiteral(name="GV"),
			EnumerationLiteral(name="MI"),
			EnumerationLiteral(name="GI"),
			EnumerationLiteral(name="MC"),
			EnumerationLiteral(name="GR"),
			EnumerationLiteral(name="MO"),
			EnumerationLiteral(name="GZ"),
			EnumerationLiteral(name="GY"),
			EnumerationLiteral(name="MU"),
			EnumerationLiteral(name="HC"),
			EnumerationLiteral(name="MG"),
			EnumerationLiteral(name="HB"),
			EnumerationLiteral(name="NE"),
			EnumerationLiteral(name="HH"),
			EnumerationLiteral(name="NM"),
			EnumerationLiteral(name="HP"),
			EnumerationLiteral(name="NR"),
			EnumerationLiteral(name="SH"),
			EnumerationLiteral(name="HY"),
			EnumerationLiteral(name="PA"),
			EnumerationLiteral(name="IB"),
			EnumerationLiteral(name="PR"),
			EnumerationLiteral(name="KY"),
			EnumerationLiteral(name="PI"),
			EnumerationLiteral(name="KB"),
			EnumerationLiteral(name="PZ"),
			EnumerationLiteral(name="LM"),
			EnumerationLiteral(name="RA"),
			EnumerationLiteral(name="LR"),
			EnumerationLiteral(name="AR"),
			EnumerationLiteral(name="LO"),
			EnumerationLiteral(name="RR"),
			EnumerationLiteral(name="LU"),
			EnumerationLiteral(name="RB"),
			EnumerationLiteral(name="MA"),
			EnumerationLiteral(name="RD"),
			EnumerationLiteral(name="MH"),
			EnumerationLiteral(name="RP"),
			EnumerationLiteral(name="RN"),
			EnumerationLiteral(name="TL"),
			EnumerationLiteral(name="TI"),
			EnumerationLiteral(name="WB"),
			EnumerationLiteral(name="WF"),
			EnumerationLiteral(name="RS"),
			EnumerationLiteral(name="RO"),
			EnumerationLiteral(name="DN"),
			EnumerationLiteral(name="SW"),
			EnumerationLiteral(name="SA"),
			EnumerationLiteral(name="SG"),
			EnumerationLiteral(name="WP"),
			EnumerationLiteral(name="SL"),
			EnumerationLiteral(name="YA"),
			EnumerationLiteral(name="SE"),
			EnumerationLiteral(name="Unspecified"),
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
			EnumerationLiteral(name="TN")
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
			EnumerationLiteral(name="TM"),
			EnumerationLiteral(name="WS"),
			EnumerationLiteral(name="YO"),
			EnumerationLiteral(name="Unspecified")
    }
)

HorseBreed: Enumeration = Enumeration(
    name="HorseBreed",
    literals={
            EnumerationLiteral(name="BW"),
			EnumerationLiteral(name="BY"),
			EnumerationLiteral(name="BU"),
			EnumerationLiteral(name="CI"),
			EnumerationLiteral(name="FC"),
			EnumerationLiteral(name="CV"),
			EnumerationLiteral(name="CY"),
			EnumerationLiteral(name="CM"),
			EnumerationLiteral(name="DT"),
			EnumerationLiteral(name="DW"),
			EnumerationLiteral(name="EX"),
			EnumerationLiteral(name="AC"),
			EnumerationLiteral(name="AS"),
			EnumerationLiteral(name="AA"),
			EnumerationLiteral(name="AO"),
			EnumerationLiteral(name="NO"),
			EnumerationLiteral(name="AP"),
			EnumerationLiteral(name="AD"),
			EnumerationLiteral(name="TH"),
			EnumerationLiteral(name="TR"),
			EnumerationLiteral(name="TF"),
			EnumerationLiteral(name="VK"),
			EnumerationLiteral(name="WE"),
			EnumerationLiteral(name="FE"),
			EnumerationLiteral(name="FJ"),
			EnumerationLiteral(name="FH"),
			EnumerationLiteral(name="FR"),
			EnumerationLiteral(name="GL"),
			EnumerationLiteral(name="WG"),
			EnumerationLiteral(name="HN"),
			EnumerationLiteral(name="HK"),
			EnumerationLiteral(name="HF"),
			EnumerationLiteral(name="HV"),
			EnumerationLiteral(name="HG"),
			EnumerationLiteral(name="HT"),
			EnumerationLiteral(name="HW"),
			EnumerationLiteral(name="HU"),
			EnumerationLiteral(name="IC"),
			EnumerationLiteral(name="LZ"),
			EnumerationLiteral(name="MU"),
			EnumerationLiteral(name="MF"),
			EnumerationLiteral(name="MN"),
			EnumerationLiteral(name="NF"),
			EnumerationLiteral(name="NK"),
			EnumerationLiteral(name="OB"),
			EnumerationLiteral(name="PT"),
			EnumerationLiteral(name="PL"),
			EnumerationLiteral(name="PF"),
			EnumerationLiteral(name="PH"),
			EnumerationLiteral(name="PV"),
			EnumerationLiteral(name="PN"),
			EnumerationLiteral(name="PW"),
			EnumerationLiteral(name="OL"),
			EnumerationLiteral(name="QH"),
			EnumerationLiteral(name="RH"),
			EnumerationLiteral(name="RU"),
			EnumerationLiteral(name="SE"),
			EnumerationLiteral(name="SY"),
			EnumerationLiteral(name="SN"),
			EnumerationLiteral(name="SF"),
			EnumerationLiteral(name="WW"),
			EnumerationLiteral(name="WI"),
			EnumerationLiteral(name="TP"),
			EnumerationLiteral(name="TW"),
			EnumerationLiteral(name="WF"),
			EnumerationLiteral(name="WU"),
			EnumerationLiteral(name="Unspecified")
    }
)

Treatment: Enumeration = Enumeration(
    name="Treatment",
    literals={
            EnumerationLiteral(name="Unspecified"),
			EnumerationLiteral(name="Vaccination"),
			EnumerationLiteral(name="Vitamin"),
			EnumerationLiteral(name="Hormone"),
			EnumerationLiteral(name="Prevention")
    }
)

TreatmentMethod: Enumeration = Enumeration(
    name="TreatmentMethod",
    literals={
            EnumerationLiteral(name="Unspecified"),
			EnumerationLiteral(name="Intramuscular"),
			EnumerationLiteral(name="Nasal"),
			EnumerationLiteral(name="Salve")
    }
)

GoatBreed: Enumeration = Enumeration(
    name="GoatBreed",
    literals={
            EnumerationLiteral(name="AI"),
			EnumerationLiteral(name="AG"),
			EnumerationLiteral(name="BZ"),
			EnumerationLiteral(name="CS"),
			EnumerationLiteral(name="LN"),
			EnumerationLiteral(name="ND"),
			EnumerationLiteral(name="NU"),
			EnumerationLiteral(name="OH"),
			EnumerationLiteral(name="PY"),
			EnumerationLiteral(name="EN"),
			EnumerationLiteral(name="TO"),
			EnumerationLiteral(name="Unspecified")
    }
)

OneToTen: Enumeration = Enumeration(
    name="OneToTen",
    literals={
            EnumerationLiteral(name="Unspecified"),
			EnumerationLiteral(name="One"),
			EnumerationLiteral(name="Two"),
			EnumerationLiteral(name="Three"),
			EnumerationLiteral(name="Four"),
			EnumerationLiteral(name="Five"),
			EnumerationLiteral(name="Six"),
			EnumerationLiteral(name="Seven"),
			EnumerationLiteral(name="Eight"),
			EnumerationLiteral(name="Nine"),
			EnumerationLiteral(name="Ten")
    }
)

AnimalType: Enumeration = Enumeration(
    name="AnimalType",
    literals={
            EnumerationLiteral(name="Unspecified"),
			EnumerationLiteral(name="Swine"),
			EnumerationLiteral(name="Equine"),
			EnumerationLiteral(name="Caprine"),
			EnumerationLiteral(name="Ovine"),
			EnumerationLiteral(name="BovineBeef"),
			EnumerationLiteral(name="BovineDairy"),
			EnumerationLiteral(name="BovineBison")
    }
)

EventDataType: Enumeration = Enumeration(
    name="EventDataType",
    literals={
            EnumerationLiteral(name="String"),
			EnumerationLiteral(name="Integer"),
			EnumerationLiteral(name="Boolean")
    }
)

# Classes
tracker_Animal = Class(name="tracker::Animal", is_abstract=True)
tracker_Tag = Class(name="tracker::Tag")
tracker_Event = Class(name="tracker::Event", is_abstract=True)
tracker_Bovine = Class(name="tracker::Bovine", is_abstract=True)
Animal = Class(name="Animal")
tracker_TagAllocated = Class(name="tracker::TagAllocated")
Event = Class(name="Event")
tracker_Premises = Class(name="tracker::Premises")
tracker_Location = Class(name="tracker::Location")
tracker_Schema = Class(name="tracker::Schema")
tracker_BovineBeef = Class(name="tracker::BovineBeef")
Bovine = Class(name="Bovine")
tracker_Ovine = Class(name="tracker::Ovine")
tracker_Slaughtered = Class(name="tracker::Slaughtered")
tracker_Died = Class(name="tracker::Died")
tracker_TagRetired = Class(name="tracker::TagRetired")
tracker_AnimalMissing = Class(name="tracker::AnimalMissing")
tracker_BovineBison = Class(name="tracker::BovineBison")
tracker_BovineDairy = Class(name="tracker::BovineDairy")
tracker_TagApplied = Class(name="tracker::TagApplied")
tracker_MovedIn = Class(name="tracker::MovedIn")
tracker_MovedOut = Class(name="tracker::MovedOut")
tracker_LostTag = Class(name="tracker::LostTag")
tracker_ReplacedTag = Class(name="tracker::ReplacedTag")
tracker_Imported = Class(name="tracker::Imported")
tracker_Exported = Class(name="tracker::Exported")
tracker_Sighting = Class(name="tracker::Sighting")
tracker_ICVI = Class(name="tracker::ICVI")
tracker_WeighIn = Class(name="tracker::WeighIn")
tracker_Swine = Class(name="tracker::Swine")
tracker_Equine = Class(name="tracker::Equine")
tracker_Birthing = Class(name="tracker::Birthing")
tracker_Caprine = Class(name="tracker::Caprine")
tracker_Calving = Class(name="tracker::Calving")
Birthing = Class(name="Birthing")
tracker_BirthDefect = Class(name="tracker::BirthDefect")
tracker_MedicalCondition = Class(name="tracker::MedicalCondition")
tracker_MedicalTreatment = Class(name="tracker::MedicalTreatment")
tracker_EventAttribute = Class(name="tracker::EventAttribute")
tracker_EventSchema = Class(name="tracker::EventSchema")
tracker_EventAttributeSchema = Class(name="tracker::EventAttributeSchema")
tracker_Mastitis = Class(name="tracker::Mastitis")
MedicalCondition = Class(name="MedicalCondition")
tracker_MilkTest = Class(name="tracker::MilkTest")
tracker_HerdTest = Class(name="tracker::HerdTest")
tracker_GenericEvent = Class(name="tracker::GenericEvent")

# tracker_Animal class attributes and methods
tracker_Animal_birthDate: Property = Property(name="birthDate", type=DateType)
tracker_Animal_sex: Property = Property(name="sex", type=StringType)
tracker_Animal_species: Property = Property(name="species", type=StringType)
tracker_Animal_breed: Property = Property(name="breed", type=StringType)
tracker_Animal_age: Property = Property(name="age", type=StringType)
tracker_Animal_comments: Property = Property(name="comments", type=StringType)
tracker_Animal_sexCode: Property = Property(name="sexCode", type=StringType)
tracker_Animal_speciesCode: Property = Property(name="speciesCode", type=StringType)
tracker_Animal_lastEventDateTime: Property = Property(name="lastEventDateTime", type=DateType)
tracker_Animal_id: Property = Property(name="id", type=StringType)
tracker_Animal_weight: Property = Property(name="weight", type=StringType)
tracker_Animal_weightGainPerDay: Property = Property(name="weightGainPerDay", type=StringType)
tracker_Animal_m_allEvents: Method = Method(name="allEvents", parameters={}, type=StringType)
tracker_Animal_m_addTemplate: Method = Method(name="addTemplate", parameters={Parameter(name='eventTemplate')})
tracker_Animal_m_activeTag: Method = Method(name="activeTag", parameters={}, type=StringType)
tracker_Animal_m_eventHistory: Method = Method(name="eventHistory", parameters={}, type=StringType)
tracker_Animal_m_lastWeighIn: Method = Method(name="lastWeighIn", parameters={}, type=StringType)
tracker_Animal.attributes={tracker_Animal_comments, tracker_Animal_id, tracker_Animal_breed, tracker_Animal_species, tracker_Animal_lastEventDateTime, tracker_Animal_birthDate, tracker_Animal_sexCode, tracker_Animal_sex, tracker_Animal_age, tracker_Animal_weight, tracker_Animal_weightGainPerDay, tracker_Animal_speciesCode}
tracker_Animal.methods={tracker_Animal_m_activeTag, tracker_Animal_m_addTemplate, tracker_Animal_m_allEvents, tracker_Animal_m_eventHistory, tracker_Animal_m_lastWeighIn}

# tracker_Tag class attributes and methods
tracker_Tag_usainNumberUsed: Property = Property(name="usainNumberUsed", type=BooleanType)
tracker_Tag_id: Property = Property(name="id", type=StringType)
tracker_Tag.attributes={tracker_Tag_id, tracker_Tag_usainNumberUsed}

# tracker_Event class attributes and methods
tracker_Event_dateTime: Property = Property(name="dateTime", type=DateType)
tracker_Event_eventCode: Property = Property(name="eventCode", type=IntegerType)
tracker_Event_electronicallyRead: Property = Property(name="electronicallyRead", type=BooleanType)
tracker_Event_correction: Property = Property(name="correction", type=BooleanType)
tracker_Event_comments: Property = Property(name="comments", type=StringType)
tracker_Event_id: Property = Property(name="id", type=StringType)
tracker_Event.attributes={tracker_Event_correction, tracker_Event_dateTime, tracker_Event_eventCode, tracker_Event_comments, tracker_Event_id, tracker_Event_electronicallyRead}

# tracker_Bovine class attributes and methods

# Animal class attributes and methods

# tracker_TagAllocated class attributes and methods

# Event class attributes and methods

# tracker_Premises class attributes and methods
tracker_Premises_emailContact: Property = Property(name="emailContact", type=StringType)
tracker_Premises_premisesId: Property = Property(name="premisesId", type=StringType)
tracker_Premises_uri: Property = Property(name="uri", type=StringType)
tracker_Premises_name: Property = Property(name="name", type=StringType)
tracker_Premises_m_eventHistory: Method = Method(name="eventHistory", parameters={}, type=Event)
tracker_Premises_m_findAnimal: Method = Method(name="findAnimal", parameters={Parameter(name='id')}, type=Animal)
tracker_Premises_m_addTemplate: Method = Method(name="addTemplate", parameters={Parameter(name='ains'), Parameter(name='animalTemplate')})
tracker_Premises.attributes={tracker_Premises_name, tracker_Premises_uri, tracker_Premises_emailContact, tracker_Premises_premisesId}
tracker_Premises.methods={tracker_Premises_m_addTemplate, tracker_Premises_m_eventHistory, tracker_Premises_m_findAnimal}

# tracker_Location class attributes and methods
tracker_Location_name: Property = Property(name="name", type=StringType)
tracker_Location.attributes={tracker_Location_name}

# tracker_Schema class attributes and methods

# tracker_BovineBeef class attributes and methods
tracker_BovineBeef_beefBreed: Property = Property(name="beefBreed", type=StringType)
tracker_BovineBeef.attributes={tracker_BovineBeef_beefBreed}

# Bovine class attributes and methods

# tracker_Ovine class attributes and methods
tracker_Ovine_sheepBreed: Property = Property(name="sheepBreed", type=StringType)
tracker_Ovine_scrapieTag: Property = Property(name="scrapieTag", type=StringType)
tracker_Ovine.attributes={tracker_Ovine_sheepBreed, tracker_Ovine_scrapieTag}

# tracker_Slaughtered class attributes and methods

# tracker_Died class attributes and methods

# tracker_TagRetired class attributes and methods

# tracker_AnimalMissing class attributes and methods

# tracker_BovineBison class attributes and methods
tracker_BovineBison_buffaloBreed: Property = Property(name="buffaloBreed", type=StringType)
tracker_BovineBison.attributes={tracker_BovineBison_buffaloBreed}

# tracker_BovineDairy class attributes and methods
tracker_BovineDairy_dairyBreed: Property = Property(name="dairyBreed", type=StringType)
tracker_BovineDairy.attributes={tracker_BovineDairy_dairyBreed}

# tracker_TagApplied class attributes and methods

# tracker_MovedIn class attributes and methods
tracker_MovedIn_sourcePin: Property = Property(name="sourcePin", type=StringType)
tracker_MovedIn.attributes={tracker_MovedIn_sourcePin}

# tracker_MovedOut class attributes and methods
tracker_MovedOut_destinationPin: Property = Property(name="destinationPin", type=StringType)
tracker_MovedOut.attributes={tracker_MovedOut_destinationPin}

# tracker_LostTag class attributes and methods

# tracker_ReplacedTag class attributes and methods
tracker_ReplacedTag_oldId: Property = Property(name="oldId", type=StringType)
tracker_ReplacedTag_usainNumberUsedForOldId: Property = Property(name="usainNumberUsedForOldId", type=BooleanType)
tracker_ReplacedTag.attributes={tracker_ReplacedTag_oldId, tracker_ReplacedTag_usainNumberUsedForOldId}

# tracker_Imported class attributes and methods

# tracker_Exported class attributes and methods

# tracker_Sighting class attributes and methods

# tracker_ICVI class attributes and methods

# tracker_WeighIn class attributes and methods
tracker_WeighIn_weight: Property = Property(name="weight", type=StringType)
tracker_WeighIn_weightGainPerDay: Property = Property(name="weightGainPerDay", type=StringType)
tracker_WeighIn_m_previousWeighIn: Method = Method(name="previousWeighIn", parameters={}, type=StringType)
tracker_WeighIn.attributes={tracker_WeighIn_weightGainPerDay, tracker_WeighIn_weight}
tracker_WeighIn.methods={tracker_WeighIn_m_previousWeighIn}

# tracker_Swine class attributes and methods
tracker_Swine_swineBreed: Property = Property(name="swineBreed", type=StringType)
tracker_Swine_rightEarNotching: Property = Property(name="rightEarNotching", type=IntegerType)
tracker_Swine_leftEarNotching: Property = Property(name="leftEarNotching", type=IntegerType)
tracker_Swine.attributes={tracker_Swine_rightEarNotching, tracker_Swine_leftEarNotching, tracker_Swine_swineBreed}

# tracker_Equine class attributes and methods
tracker_Equine_horseBreed: Property = Property(name="horseBreed", type=StringType)
tracker_Equine.attributes={tracker_Equine_horseBreed}

# tracker_Birthing class attributes and methods
tracker_Birthing_viability: Property = Property(name="viability", type=BooleanType)
tracker_Birthing_assisted: Property = Property(name="assisted", type=BooleanType)
tracker_Birthing_difficulty: Property = Property(name="difficulty", type=StringType)
tracker_Birthing.attributes={tracker_Birthing_assisted, tracker_Birthing_difficulty, tracker_Birthing_viability}

# tracker_Caprine class attributes and methods
tracker_Caprine_goatBreed: Property = Property(name="goatBreed", type=StringType)
tracker_Caprine.attributes={tracker_Caprine_goatBreed}

# tracker_Calving class attributes and methods

# Birthing class attributes and methods

# tracker_BirthDefect class attributes and methods
tracker_BirthDefect_freemartin: Property = Property(name="freemartin", type=BooleanType)
tracker_BirthDefect.attributes={tracker_BirthDefect_freemartin}

# tracker_MedicalCondition class attributes and methods

# tracker_MedicalTreatment class attributes and methods
tracker_MedicalTreatment_method: Property = Property(name="method", type=StringType)
tracker_MedicalTreatment_name: Property = Property(name="name", type=StringType)
tracker_MedicalTreatment_product: Property = Property(name="product", type=StringType)
tracker_MedicalTreatment_manufacturer: Property = Property(name="manufacturer", type=StringType)
tracker_MedicalTreatment_lot: Property = Property(name="lot", type=StringType)
tracker_MedicalTreatment_quantity: Property = Property(name="quantity", type=StringType)
tracker_MedicalTreatment_treatment: Property = Property(name="treatment", type=StringType)
tracker_MedicalTreatment.attributes={tracker_MedicalTreatment_manufacturer, tracker_MedicalTreatment_product, tracker_MedicalTreatment_name, tracker_MedicalTreatment_method, tracker_MedicalTreatment_treatment, tracker_MedicalTreatment_quantity, tracker_MedicalTreatment_lot}

# tracker_EventAttribute class attributes and methods
tracker_EventAttribute_key: Property = Property(name="key", type=StringType)
tracker_EventAttribute_value: Property = Property(name="value", type=StringType)
tracker_EventAttribute.attributes={tracker_EventAttribute_value, tracker_EventAttribute_key}

# tracker_EventSchema class attributes and methods
tracker_EventSchema_name: Property = Property(name="name", type=StringType)
tracker_EventSchema_description: Property = Property(name="description", type=StringType)
tracker_EventSchema_animalType: Property = Property(name="animalType", type=StringType)
tracker_EventSchema.attributes={tracker_EventSchema_animalType, tracker_EventSchema_description, tracker_EventSchema_name}

# tracker_EventAttributeSchema class attributes and methods
tracker_EventAttributeSchema_name: Property = Property(name="name", type=StringType)
tracker_EventAttributeSchema_dataType: Property = Property(name="dataType", type=StringType)
tracker_EventAttributeSchema_description: Property = Property(name="description", type=StringType)
tracker_EventAttributeSchema.attributes={tracker_EventAttributeSchema_description, tracker_EventAttributeSchema_name, tracker_EventAttributeSchema_dataType}

# tracker_Mastitis class attributes and methods
tracker_Mastitis_location: Property = Property(name="location", type=StringType)
tracker_Mastitis_origin: Property = Property(name="origin", type=StringType)
tracker_Mastitis.attributes={tracker_Mastitis_location, tracker_Mastitis_origin}

# MedicalCondition class attributes and methods

# tracker_MilkTest class attributes and methods
tracker_MilkTest_poundsProduced: Property = Property(name="poundsProduced", type=FloatType)
tracker_MilkTest_percentButterFat: Property = Property(name="percentButterFat", type=FloatType)
tracker_MilkTest_percentProtein: Property = Property(name="percentProtein", type=FloatType)
tracker_MilkTest_somaticCellCounts: Property = Property(name="somaticCellCounts", type=IntegerType)
tracker_MilkTest_otherSolids: Property = Property(name="otherSolids", type=FloatType)
tracker_MilkTest.attributes={tracker_MilkTest_percentButterFat, tracker_MilkTest_somaticCellCounts, tracker_MilkTest_percentProtein, tracker_MilkTest_otherSolids, tracker_MilkTest_poundsProduced}

# tracker_HerdTest class attributes and methods
tracker_HerdTest_pregnant: Property = Property(name="pregnant", type=BooleanType)
tracker_HerdTest_daysSinceBredEstimate: Property = Property(name="daysSinceBredEstimate", type=IntegerType)
tracker_HerdTest_bredDateEstimate: Property = Property(name="bredDateEstimate", type=DateType)
tracker_HerdTest.attributes={tracker_HerdTest_bredDateEstimate, tracker_HerdTest_pregnant, tracker_HerdTest_daysSinceBredEstimate}

# tracker_GenericEvent class attributes and methods
tracker_GenericEvent_m_findSchema: Method = Method(name="findSchema", parameters={Parameter(name='eventAttribute')}, type=StringType)
tracker_GenericEvent.methods={tracker_GenericEvent_m_findSchema}

# Relationships
tags0: BinaryAssociation = BinaryAssociation(
    name="tags0",
    ends={
        Property(name="tracker_Tag", type=tracker_Animal, multiplicity=Multiplicity(1, 1)),
        Property(name="tracker_Animal", type=tracker_Tag, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
animals9: BinaryAssociation = BinaryAssociation(
    name="animals9",
    ends={
        Property(name="tracker_Animal10", type=tracker_Premises, multiplicity=Multiplicity(1, 1)),
        Property(name="tracker_Premises", type=tracker_Animal, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dam2: BinaryAssociation = BinaryAssociation(
    name="dam2",
    ends={
        Property(name="tracker_Animal3", type=tracker_Animal, multiplicity=Multiplicity(1, 1)),
        Property(name="tracker_Animal1", type=tracker_Animal, multiplicity=Multiplicity(0, 1))
    }
)
sire5: BinaryAssociation = BinaryAssociation(
    name="sire5",
    ends={
        Property(name="tracker_Animal6", type=tracker_Animal, multiplicity=Multiplicity(1, 1)),
        Property(name="tracker_Animal4", type=tracker_Animal, multiplicity=Multiplicity(0, 1))
    }
)
events7: BinaryAssociation = BinaryAssociation(
    name="events7",
    ends={
        Property(name="Event", type=tracker_Tag, multiplicity=Multiplicity(1, 1)),
        Property(name="tag", type=tracker_Event, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
tag8: BinaryAssociation = BinaryAssociation(
    name="tag8",
    ends={
        Property(name="Tag", type=tracker_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="events", type=tracker_Tag, multiplicity=Multiplicity(1, 1))
    }
)
unAppliedTags11: BinaryAssociation = BinaryAssociation(
    name="unAppliedTags11",
    ends={
        Property(name="tracker_Tag13", type=tracker_Premises, multiplicity=Multiplicity(1, 1)),
        Property(name="tracker_Premises12", type=tracker_Tag, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
locations14: BinaryAssociation = BinaryAssociation(
    name="locations14",
    ends={
        Property(name="tracker_Location", type=tracker_Premises, multiplicity=Multiplicity(1, 1)),
        Property(name="tracker_Premises15", type=tracker_Location, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
schema16: BinaryAssociation = BinaryAssociation(
    name="schema16",
    ends={
        Property(name="tracker_Schema", type=tracker_Premises, multiplicity=Multiplicity(1, 1)),
        Property(name="tracker_Premises17", type=tracker_Schema, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
oldTag18: BinaryAssociation = BinaryAssociation(
    name="oldTag18",
    ends={
        Property(name="tracker_Tag19", type=tracker_ReplacedTag, multiplicity=Multiplicity(1, 1)),
        Property(name="tracker_ReplacedTag", type=tracker_Tag, multiplicity=Multiplicity(1, 1))
    }
)
location20: BinaryAssociation = BinaryAssociation(
    name="location20",
    ends={
        Property(name="tracker_Location21", type=tracker_Sighting, multiplicity=Multiplicity(1, 1)),
        Property(name="tracker_Sighting", type=tracker_Location, multiplicity=Multiplicity(0, 1))
    }
)
eventAttributes22: BinaryAssociation = BinaryAssociation(
    name="eventAttributes22",
    ends={
        Property(name="tracker_EventAttribute", type=tracker_GenericEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="tracker_GenericEvent", type=tracker_EventAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eventSchema23: BinaryAssociation = BinaryAssociation(
    name="eventSchema23",
    ends={
        Property(name="tracker_EventSchema", type=tracker_GenericEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="tracker_GenericEvent24", type=tracker_EventSchema, multiplicity=Multiplicity(1, 1))
    }
)
eventAttributes25: BinaryAssociation = BinaryAssociation(
    name="eventAttributes25",
    ends={
        Property(name="tracker_EventAttributeSchema", type=tracker_EventSchema, multiplicity=Multiplicity(1, 1)),
        Property(name="tracker_EventSchema26", type=tracker_EventAttributeSchema, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
eventSchemas27: BinaryAssociation = BinaryAssociation(
    name="eventSchemas27",
    ends={
        Property(name="tracker_EventSchema29", type=tracker_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="tracker_Schema28", type=tracker_EventSchema, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_tracker_Bovine_Animal = Generalization(general=Animal, specific=tracker_Bovine)
gen_tracker_TagAllocated_Event = Generalization(general=Event, specific=tracker_TagAllocated)
gen_tracker_BovineBeef_Bovine = Generalization(general=Bovine, specific=tracker_BovineBeef)
gen_tracker_Ovine_Animal = Generalization(general=Animal, specific=tracker_Ovine)
gen_tracker_Slaughtered_Event = Generalization(general=Event, specific=tracker_Slaughtered)
gen_tracker_Died_Event = Generalization(general=Event, specific=tracker_Died)
gen_tracker_TagRetired_Event = Generalization(general=Event, specific=tracker_TagRetired)
gen_tracker_AnimalMissing_Event = Generalization(general=Event, specific=tracker_AnimalMissing)
gen_tracker_BovineBison_Bovine = Generalization(general=Bovine, specific=tracker_BovineBison)
gen_tracker_BovineDairy_Bovine = Generalization(general=Bovine, specific=tracker_BovineDairy)
gen_tracker_TagApplied_Event = Generalization(general=Event, specific=tracker_TagApplied)
gen_tracker_MovedIn_Event = Generalization(general=Event, specific=tracker_MovedIn)
gen_tracker_MovedOut_Event = Generalization(general=Event, specific=tracker_MovedOut)
gen_tracker_LostTag_Event = Generalization(general=Event, specific=tracker_LostTag)
gen_tracker_ReplacedTag_Event = Generalization(general=Event, specific=tracker_ReplacedTag)
gen_tracker_Imported_Event = Generalization(general=Event, specific=tracker_Imported)
gen_tracker_Exported_Event = Generalization(general=Event, specific=tracker_Exported)
gen_tracker_Sighting_Event = Generalization(general=Event, specific=tracker_Sighting)
gen_tracker_ICVI_Event = Generalization(general=Event, specific=tracker_ICVI)
gen_tracker_WeighIn_Event = Generalization(general=Event, specific=tracker_WeighIn)
gen_tracker_Swine_Animal = Generalization(general=Animal, specific=tracker_Swine)
gen_tracker_Equine_Animal = Generalization(general=Animal, specific=tracker_Equine)
gen_tracker_Birthing_Event = Generalization(general=Event, specific=tracker_Birthing)
gen_tracker_Caprine_Animal = Generalization(general=Animal, specific=tracker_Caprine)
gen_tracker_Calving_Birthing = Generalization(general=Birthing, specific=tracker_Calving)
gen_tracker_BirthDefect_Event = Generalization(general=Event, specific=tracker_BirthDefect)
gen_tracker_MedicalCondition_Event = Generalization(general=Event, specific=tracker_MedicalCondition)
gen_tracker_MedicalTreatment_Event = Generalization(general=Event, specific=tracker_MedicalTreatment)
gen_tracker_Mastitis_MedicalCondition = Generalization(general=MedicalCondition, specific=tracker_Mastitis)
gen_tracker_MilkTest_Event = Generalization(general=Event, specific=tracker_MilkTest)
gen_tracker_HerdTest_Event = Generalization(general=Event, specific=tracker_HerdTest)
gen_tracker_GenericEvent_Event = Generalization(general=Event, specific=tracker_GenericEvent)

# Domain Model
domain_model = DomainModel(
    name="tracker",
    types={tracker_Animal, tracker_Tag, tracker_Event, tracker_Bovine, Animal, tracker_TagAllocated, Event, tracker_Premises, tracker_Location, tracker_Schema, tracker_BovineBeef, Bovine, tracker_Ovine, tracker_Slaughtered, tracker_Died, tracker_TagRetired, tracker_AnimalMissing, tracker_BovineBison, tracker_BovineDairy, tracker_TagApplied, tracker_MovedIn, tracker_MovedOut, tracker_LostTag, tracker_ReplacedTag, tracker_Imported, tracker_Exported, tracker_Sighting, tracker_ICVI, tracker_WeighIn, tracker_Swine, tracker_Equine, tracker_Birthing, tracker_Caprine, tracker_Calving, Birthing, tracker_BirthDefect, tracker_MedicalCondition, tracker_MedicalTreatment, tracker_EventAttribute, tracker_EventSchema, tracker_EventAttributeSchema, tracker_Mastitis, MedicalCondition, tracker_MilkTest, tracker_HerdTest, tracker_GenericEvent, Sex, SheepBreed, BisonBreed, BeefBreed, DairyBreed, SwineBreed, HorseBreed, Treatment, TreatmentMethod, GoatBreed, OneToTen, AnimalType, EventDataType},
    associations={tags0, animals9, dam2, sire5, events7, tag8, unAppliedTags11, locations14, schema16, oldTag18, location20, eventAttributes22, eventSchema23, eventAttributes25, eventSchemas27},
    generalizations={gen_tracker_Bovine_Animal, gen_tracker_TagAllocated_Event, gen_tracker_BovineBeef_Bovine, gen_tracker_Ovine_Animal, gen_tracker_Slaughtered_Event, gen_tracker_Died_Event, gen_tracker_TagRetired_Event, gen_tracker_AnimalMissing_Event, gen_tracker_BovineBison_Bovine, gen_tracker_BovineDairy_Bovine, gen_tracker_TagApplied_Event, gen_tracker_MovedIn_Event, gen_tracker_MovedOut_Event, gen_tracker_LostTag_Event, gen_tracker_ReplacedTag_Event, gen_tracker_Imported_Event, gen_tracker_Exported_Event, gen_tracker_Sighting_Event, gen_tracker_ICVI_Event, gen_tracker_WeighIn_Event, gen_tracker_Swine_Animal, gen_tracker_Equine_Animal, gen_tracker_Birthing_Event, gen_tracker_Caprine_Animal, gen_tracker_Calving_Birthing, gen_tracker_BirthDefect_Event, gen_tracker_MedicalCondition_Event, gen_tracker_MedicalTreatment_Event, gen_tracker_Mastitis_MedicalCondition, gen_tracker_MilkTest_Event, gen_tracker_HerdTest_Event, gen_tracker_GenericEvent_Event},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)