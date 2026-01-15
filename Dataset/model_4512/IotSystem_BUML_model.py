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
EnvironmentConditions: Enumeration = Enumeration(
    name="EnvironmentConditions",
    literals={
            EnumerationLiteral(name="TEMPERATURE"),
			EnumerationLiteral(name="SOUND"),
			EnumerationLiteral(name="LIGHT")
    }
)

Actions: Enumeration = Enumeration(
    name="Actions",
    literals={
            EnumerationLiteral(name="SMS"),
			EnumerationLiteral(name="EMAIL")
    }
)

RelationalOperator: Enumeration = Enumeration(
    name="RelationalOperator",
    literals={
            EnumerationLiteral(name="MINOR"),
			EnumerationLiteral(name="MINOREQUAL"),
			EnumerationLiteral(name="EQUAL"),
			EnumerationLiteral(name="DIFFERENT"),
			EnumerationLiteral(name="MAJOR"),
			EnumerationLiteral(name="MAJOREQUAL")
    }
)

# Classes
Device = Class(name="Device")
iotsystem_Device = Class(name="iotsystem::Device", is_abstract=True)
NamedElement = Class(name="NamedElement")
iotsystem_Resource = Class(name="iotsystem::Resource")
iotsystem_DigitalArtifact = Class(name="iotsystem::DigitalArtifact")
iotsystem_Rule = Class(name="iotsystem::Rule")
iotsystem_Actuator = Class(name="iotsystem::Actuator")
iotsystem_Action = Class(name="iotsystem::Action")
iotsystem_Condition = Class(name="iotsystem::Condition")
iotsystem_Parameter = Class(name="iotsystem::Parameter")
iotsystem_PhysicalEntity = Class(name="iotsystem::PhysicalEntity")
iotsystem_IotSystem = Class(name="iotsystem::IotSystem")
iotsystem_Sensor = Class(name="iotsystem::Sensor")
iotsystem_NamedElement = Class(name="iotsystem::NamedElement")

# Device class attributes and methods

# iotsystem_Device class attributes and methods

# NamedElement class attributes and methods

# iotsystem_Resource class attributes and methods
iotsystem_Resource_url: Property = Property(name="url", type=StringType)
iotsystem_Resource_measurement: Property = Property(name="measurement", type=StringType)
iotsystem_Resource.attributes={iotsystem_Resource_url, iotsystem_Resource_measurement}

# iotsystem_DigitalArtifact class attributes and methods

# iotsystem_Rule class attributes and methods

# iotsystem_Actuator class attributes and methods

# iotsystem_Action class attributes and methods
iotsystem_Action_action: Property = Property(name="action", type=StringType)
iotsystem_Action.attributes={iotsystem_Action_action}

# iotsystem_Condition class attributes and methods
iotsystem_Condition_expectedValue: Property = Property(name="expectedValue", type=FloatType)
iotsystem_Condition_relationalOperator: Property = Property(name="relationalOperator", type=StringType)
iotsystem_Condition.attributes={iotsystem_Condition_expectedValue, iotsystem_Condition_relationalOperator}

# iotsystem_Parameter class attributes and methods
iotsystem_Parameter_name: Property = Property(name="name", type=StringType)
iotsystem_Parameter_value: Property = Property(name="value", type=StringType)
iotsystem_Parameter.attributes={iotsystem_Parameter_name, iotsystem_Parameter_value}

# iotsystem_PhysicalEntity class attributes and methods

# iotsystem_IotSystem class attributes and methods

# iotsystem_Sensor class attributes and methods

# iotsystem_NamedElement class attributes and methods
iotsystem_NamedElement_name: Property = Property(name="name", type=StringType)
iotsystem_NamedElement.attributes={iotsystem_NamedElement_name}

# Relationships
consumes0: BinaryAssociation = BinaryAssociation(
    name="consumes0",
    ends={
        Property(name="iotsystem_Resource", type=iotsystem_Device, multiplicity=Multiplicity(1, 1)),
        Property(name="iotsystem_Device", type=iotsystem_Resource, multiplicity=Multiplicity(1, 9999))
    }
)
resources1: BinaryAssociation = BinaryAssociation(
    name="resources1",
    ends={
        Property(name="iotsystem_Resource2", type=iotsystem_DigitalArtifact, multiplicity=Multiplicity(1, 1)),
        Property(name="iotsystem_DigitalArtifact", type=iotsystem_Resource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rules3: BinaryAssociation = BinaryAssociation(
    name="rules3",
    ends={
        Property(name="iotsystem_Rule", type=iotsystem_DigitalArtifact, multiplicity=Multiplicity(1, 1)),
        Property(name="iotsystem_DigitalArtifact4", type=iotsystem_Rule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actions5: BinaryAssociation = BinaryAssociation(
    name="actions5",
    ends={
        Property(name="iotsystem_Action", type=iotsystem_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="iotsystem_Rule6", type=iotsystem_Action, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
condition7: BinaryAssociation = BinaryAssociation(
    name="condition7",
    ends={
        Property(name="iotsystem_Condition", type=iotsystem_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="iotsystem_Rule8", type=iotsystem_Condition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameters9: BinaryAssociation = BinaryAssociation(
    name="parameters9",
    ends={
        Property(name="iotsystem_Parameter", type=iotsystem_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="iotsystem_Action10", type=iotsystem_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
devices11: BinaryAssociation = BinaryAssociation(
    name="devices11",
    ends={
        Property(name="iotsystem_Device12", type=iotsystem_PhysicalEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="iotsystem_PhysicalEntity", type=iotsystem_Device, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
physicalEntities13: BinaryAssociation = BinaryAssociation(
    name="physicalEntities13",
    ends={
        Property(name="iotsystem_PhysicalEntity14", type=iotsystem_IotSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="iotsystem_IotSystem", type=iotsystem_PhysicalEntity, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
variable18: BinaryAssociation = BinaryAssociation(
    name="variable18",
    ends={
        Property(name="iotsystem_Sensor", type=iotsystem_Condition, multiplicity=Multiplicity(1, 1)),
        Property(name="iotsystem_Condition19", type=iotsystem_Sensor, multiplicity=Multiplicity(1, 1))
    }
)
digitalArtifacts15: BinaryAssociation = BinaryAssociation(
    name="digitalArtifacts15",
    ends={
        Property(name="iotsystem_DigitalArtifact17", type=iotsystem_IotSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="iotsystem_IotSystem16", type=iotsystem_DigitalArtifact, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)

# Generalizations
gen_iotsystem_Sensor_Device = Generalization(general=Device, specific=iotsystem_Sensor)
gen_iotsystem_Device_NamedElement = Generalization(general=NamedElement, specific=iotsystem_Device)
gen_iotsystem_DigitalArtifact_NamedElement = Generalization(general=NamedElement, specific=iotsystem_DigitalArtifact)
gen_iotsystem_Actuator_Device = Generalization(general=Device, specific=iotsystem_Actuator)
gen_iotsystem_Rule_NamedElement = Generalization(general=NamedElement, specific=iotsystem_Rule)
gen_iotsystem_PhysicalEntity_NamedElement = Generalization(general=NamedElement, specific=iotsystem_PhysicalEntity)
gen_iotsystem_IotSystem_NamedElement = Generalization(general=NamedElement, specific=iotsystem_IotSystem)

# Domain Model
domain_model = DomainModel(
    name="iotsystem",
    types={Device, iotsystem_Device, NamedElement, iotsystem_Resource, iotsystem_DigitalArtifact, iotsystem_Rule, iotsystem_Actuator, iotsystem_Action, iotsystem_Condition, iotsystem_Parameter, iotsystem_PhysicalEntity, iotsystem_IotSystem, iotsystem_Sensor, iotsystem_NamedElement, EnvironmentConditions, Actions, RelationalOperator},
    associations={consumes0, resources1, rules3, actions5, condition7, parameters9, devices11, physicalEntities13, variable18, digitalArtifacts15},
    generalizations={gen_iotsystem_Sensor_Device, gen_iotsystem_Device_NamedElement, gen_iotsystem_DigitalArtifact_NamedElement, gen_iotsystem_Actuator_Device, gen_iotsystem_Rule_NamedElement, gen_iotsystem_PhysicalEntity_NamedElement, gen_iotsystem_IotSystem_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)