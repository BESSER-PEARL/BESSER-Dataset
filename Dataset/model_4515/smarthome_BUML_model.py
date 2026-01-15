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
Activity: Enumeration = Enumeration(
    name="Activity",
    literals={
            EnumerationLiteral(name="standing"),
			EnumerationLiteral(name="laying"),
			EnumerationLiteral(name="sitting")
    }
)

Operator: Enumeration = Enumeration(
    name="Operator",
    literals={
            EnumerationLiteral(name="superior"),
			EnumerationLiteral(name="inferior"),
			EnumerationLiteral(name="equal")
    }
)

Precision: Enumeration = Enumeration(
    name="Precision",
    literals={
            EnumerationLiteral(name="ms"),
			EnumerationLiteral(name="s"),
			EnumerationLiteral(name="m")
    }
)

# Classes
smarthome_Person = Class(name="smarthome::Person")
smarthome_Pattern = Class(name="smarthome::Pattern")
smarthome_NamedEntity = Class(name="smarthome::NamedEntity", is_abstract=True)
smarthome_Sensor = Class(name="smarthome::Sensor", is_abstract=True)
NamedEntity = Class(name="NamedEntity")
smarthome_Home = Class(name="smarthome::Home")
smarthome_Room = Class(name="smarthome::Room")
smarthome_SensorPredicate = Class(name="smarthome::SensorPredicate")
Predicate = Class(name="Predicate")
smarthome_PersonPredicate = Class(name="smarthome::PersonPredicate")
smarthome_AnalogSensor = Class(name="smarthome::AnalogSensor")
Sensor = Class(name="Sensor")
smarthome_DigitalSensor = Class(name="smarthome::DigitalSensor")
smarthome_CSVSensor = Class(name="smarthome::CSVSensor")
smarthome_Tag = Class(name="smarthome::Tag")
smarthome_Rule = Class(name="smarthome::Rule")
smarthome_Predicate = Class(name="smarthome::Predicate", is_abstract=True)
smarthome_Duration = Class(name="smarthome::Duration")
smarthome_Mode = Class(name="smarthome::Mode")

# smarthome_Person class attributes and methods

# smarthome_Pattern class attributes and methods

# smarthome_NamedEntity class attributes and methods
smarthome_NamedEntity_name: Property = Property(name="name", type=StringType)
smarthome_NamedEntity.attributes={smarthome_NamedEntity_name}

# smarthome_Sensor class attributes and methods

# NamedEntity class attributes and methods

# smarthome_Home class attributes and methods
smarthome_Home_fileEvents: Property = Property(name="fileEvents", type=StringType)
smarthome_Home.attributes={smarthome_Home_fileEvents}

# smarthome_Room class attributes and methods

# smarthome_SensorPredicate class attributes and methods
smarthome_SensorPredicate_operator: Property = Property(name="operator", type=StringType)
smarthome_SensorPredicate_value: Property = Property(name="value", type=FloatType)
smarthome_SensorPredicate.attributes={smarthome_SensorPredicate_operator, smarthome_SensorPredicate_value}

# Predicate class attributes and methods

# smarthome_PersonPredicate class attributes and methods
smarthome_PersonPredicate_activity: Property = Property(name="activity", type=StringType)
smarthome_PersonPredicate.attributes={smarthome_PersonPredicate_activity}

# smarthome_AnalogSensor class attributes and methods

# Sensor class attributes and methods

# smarthome_DigitalSensor class attributes and methods

# smarthome_CSVSensor class attributes and methods
smarthome_CSVSensor_file: Property = Property(name="file", type=StringType)
smarthome_CSVSensor.attributes={smarthome_CSVSensor_file}

# smarthome_Tag class attributes and methods

# smarthome_Rule class attributes and methods

# smarthome_Predicate class attributes and methods

# smarthome_Duration class attributes and methods
smarthome_Duration_time: Property = Property(name="time", type=IntegerType)
smarthome_Duration_precision: Property = Property(name="precision", type=StringType)
smarthome_Duration.attributes={smarthome_Duration_time, smarthome_Duration_precision}

# smarthome_Mode class attributes and methods

# Relationships
persons1: BinaryAssociation = BinaryAssociation(
    name="persons1",
    ends={
        Property(name="smarthome_Person", type=smarthome_Home, multiplicity=Multiplicity(1, 1)),
        Property(name="smarthome_Home2", type=smarthome_Person, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
patterns3: BinaryAssociation = BinaryAssociation(
    name="patterns3",
    ends={
        Property(name="smarthome_Pattern", type=smarthome_Home, multiplicity=Multiplicity(1, 1)),
        Property(name="smarthome_Home4", type=smarthome_Pattern, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
monitoredEntities5: BinaryAssociation = BinaryAssociation(
    name="monitoredEntities5",
    ends={
        Property(name="smarthome_NamedEntity", type=smarthome_Home, multiplicity=Multiplicity(1, 1)),
        Property(name="smarthome_Home6", type=smarthome_NamedEntity, multiplicity=Multiplicity(0, 9999))
    }
)
rooms0: BinaryAssociation = BinaryAssociation(
    name="rooms0",
    ends={
        Property(name="smarthome_Room", type=smarthome_Home, multiplicity=Multiplicity(1, 1)),
        Property(name="smarthome_Home", type=smarthome_Room, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
chest23: BinaryAssociation = BinaryAssociation(
    name="chest23",
    ends={
        Property(name="smarthome_Tag25", type=smarthome_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="smarthome_Person24", type=smarthome_Tag, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sensor26: BinaryAssociation = BinaryAssociation(
    name="sensor26",
    ends={
        Property(name="smarthome_Sensor27", type=smarthome_SensorPredicate, multiplicity=Multiplicity(1, 1)),
        Property(name="smarthome_SensorPredicate", type=smarthome_Sensor, multiplicity=Multiplicity(0, 1))
    }
)
person28: BinaryAssociation = BinaryAssociation(
    name="person28",
    ends={
        Property(name="smarthome_Person29", type=smarthome_PersonPredicate, multiplicity=Multiplicity(1, 1)),
        Property(name="smarthome_PersonPredicate", type=smarthome_Person, multiplicity=Multiplicity(0, 1))
    }
)
sensors7: BinaryAssociation = BinaryAssociation(
    name="sensors7",
    ends={
        Property(name="smarthome_Sensor", type=smarthome_Room, multiplicity=Multiplicity(1, 1)),
        Property(name="smarthome_Room8", type=smarthome_Sensor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rules9: BinaryAssociation = BinaryAssociation(
    name="rules9",
    ends={
        Property(name="smarthome_Rule", type=smarthome_Pattern, multiplicity=Multiplicity(1, 1)),
        Property(name="smarthome_Pattern10", type=smarthome_Rule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
predicates11: BinaryAssociation = BinaryAssociation(
    name="predicates11",
    ends={
        Property(name="smarthome_Predicate", type=smarthome_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="smarthome_Rule12", type=smarthome_Predicate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
duration13: BinaryAssociation = BinaryAssociation(
    name="duration13",
    ends={
        Property(name="smarthome_Duration", type=smarthome_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="smarthome_Rule14", type=smarthome_Duration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ankleLeft15: BinaryAssociation = BinaryAssociation(
    name="ankleLeft15",
    ends={
        Property(name="smarthome_Tag", type=smarthome_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="smarthome_Person16", type=smarthome_Tag, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ankleRight17: BinaryAssociation = BinaryAssociation(
    name="ankleRight17",
    ends={
        Property(name="smarthome_Tag19", type=smarthome_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="smarthome_Person18", type=smarthome_Tag, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
belt20: BinaryAssociation = BinaryAssociation(
    name="belt20",
    ends={
        Property(name="smarthome_Tag22", type=smarthome_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="smarthome_Person21", type=smarthome_Tag, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_smarthome_Sensor_NamedEntity = Generalization(general=NamedEntity, specific=smarthome_Sensor)
gen_smarthome_SensorPredicate_Predicate = Generalization(general=Predicate, specific=smarthome_SensorPredicate)
gen_smarthome_PersonPredicate_Predicate = Generalization(general=Predicate, specific=smarthome_PersonPredicate)
gen_smarthome_AnalogSensor_Sensor = Generalization(general=Sensor, specific=smarthome_AnalogSensor)
gen_smarthome_DigitalSensor_Sensor = Generalization(general=Sensor, specific=smarthome_DigitalSensor)
gen_smarthome_Tag_NamedEntity = Generalization(general=NamedEntity, specific=smarthome_Tag)
gen_smarthome_Room_NamedEntity = Generalization(general=NamedEntity, specific=smarthome_Room)
gen_smarthome_Pattern_NamedEntity = Generalization(general=NamedEntity, specific=smarthome_Pattern)
gen_smarthome_Person_NamedEntity = Generalization(general=NamedEntity, specific=smarthome_Person)

# Domain Model
domain_model = DomainModel(
    name="smarthome",
    types={smarthome_Person, smarthome_Pattern, smarthome_NamedEntity, smarthome_Sensor, NamedEntity, smarthome_Home, smarthome_Room, smarthome_SensorPredicate, Predicate, smarthome_PersonPredicate, smarthome_AnalogSensor, Sensor, smarthome_DigitalSensor, smarthome_CSVSensor, smarthome_Tag, smarthome_Rule, smarthome_Predicate, smarthome_Duration, smarthome_Mode, Activity, Operator, Precision},
    associations={persons1, patterns3, monitoredEntities5, rooms0, chest23, sensor26, person28, sensors7, rules9, predicates11, duration13, ankleLeft15, ankleRight17, belt20},
    generalizations={gen_smarthome_Sensor_NamedEntity, gen_smarthome_SensorPredicate_Predicate, gen_smarthome_PersonPredicate_Predicate, gen_smarthome_AnalogSensor_Sensor, gen_smarthome_DigitalSensor_Sensor, gen_smarthome_Tag_NamedEntity, gen_smarthome_Room_NamedEntity, gen_smarthome_Pattern_NamedEntity, gen_smarthome_Person_NamedEntity},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)