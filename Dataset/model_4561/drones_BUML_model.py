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
ActionKind: Enumeration = Enumeration(
    name="ActionKind",
    literals={
            EnumerationLiteral(name="SET"),
			EnumerationLiteral(name="ADD"),
			EnumerationLiteral(name="SUBTRACT")
    }
)

# Classes
drones_FieldObject = Class(name="drones::FieldObject", is_abstract=True)
NamedElement = Class(name="NamedElement")
SizedElement = Class(name="SizedElement")
drones_Parameter = Class(name="drones::Parameter")
drones_Drone = Class(name="drones::Drone")
drones_Battery = Class(name="drones::Battery")
drones_ChargeStation = Class(name="drones::ChargeStation")
drones_Action = Class(name="drones::Action")
TemporalContainmentProxy = Class(name="TemporalContainmentProxy")
drones_NamedElement = Class(name="drones::NamedElement", is_abstract=True)
drones_MovableObject = Class(name="drones::MovableObject")
FieldObject = Class(name="FieldObject")
drones_SizedElement = Class(name="drones::SizedElement", is_abstract=True)
drones_ImmovableObject = Class(name="drones::ImmovableObject")
ImmovableObject = Class(name="ImmovableObject")
drones_Mission = Class(name="drones::Mission")
drones_TemporalContainmentProxy = Class(name="drones::TemporalContainmentProxy", is_abstract=True)

# drones_FieldObject class attributes and methods

# NamedElement class attributes and methods

# SizedElement class attributes and methods

# drones_Parameter class attributes and methods
drones_Parameter_key: Property = Property(name="key", type=StringType)
drones_Parameter_value: Property = Property(name="value", type=StringType)
drones_Parameter.attributes={drones_Parameter_value, drones_Parameter_key}

# drones_Drone class attributes and methods
drones_Drone_cpuFrequency: Property = Property(name="cpuFrequency", type=IntegerType)
drones_Drone_memory: Property = Property(name="memory", type=IntegerType)
drones_Drone_maxPayload: Property = Property(name="maxPayload", type=FloatType)
drones_Drone_communicationRange: Property = Property(name="communicationRange", type=FloatType)
drones_Drone_minSpeed: Property = Property(name="minSpeed", type=FloatType)
drones_Drone_maxSpeed: Property = Property(name="maxSpeed", type=FloatType)
drones_Drone.attributes={drones_Drone_maxPayload, drones_Drone_communicationRange, drones_Drone_maxSpeed, drones_Drone_memory, drones_Drone_cpuFrequency, drones_Drone_minSpeed}

# drones_Battery class attributes and methods
drones_Battery_lifeTime: Property = Property(name="lifeTime", type=FloatType)
drones_Battery_rechargeRate: Property = Property(name="rechargeRate", type=FloatType)
drones_Battery_charge: Property = Property(name="charge", type=FloatType)
drones_Battery_remainingLifeTime: Property = Property(name="remainingLifeTime", type=FloatType)
drones_Battery.attributes={drones_Battery_lifeTime, drones_Battery_rechargeRate, drones_Battery_remainingLifeTime, drones_Battery_charge}

# drones_ChargeStation class attributes and methods

# drones_Action class attributes and methods
drones_Action_operation: Property = Property(name="operation", type=StringType)
drones_Action_key: Property = Property(name="key", type=StringType)
drones_Action_value: Property = Property(name="value", type=StringType)
drones_Action_range: Property = Property(name="range", type=FloatType)
drones_Action.attributes={drones_Action_key, drones_Action_range, drones_Action_operation, drones_Action_value}

# TemporalContainmentProxy class attributes and methods

# drones_NamedElement class attributes and methods
drones_NamedElement_name: Property = Property(name="name", type=StringType)
drones_NamedElement.attributes={drones_NamedElement_name}

# drones_MovableObject class attributes and methods
drones_MovableObject_weight: Property = Property(name="weight", type=FloatType)
drones_MovableObject.attributes={drones_MovableObject_weight}

# FieldObject class attributes and methods

# drones_SizedElement class attributes and methods
drones_SizedElement_length: Property = Property(name="length", type=FloatType)
drones_SizedElement_height: Property = Property(name="height", type=FloatType)
drones_SizedElement_width: Property = Property(name="width", type=FloatType)
drones_SizedElement_x: Property = Property(name="x", type=FloatType)
drones_SizedElement_y: Property = Property(name="y", type=FloatType)
drones_SizedElement_z: Property = Property(name="z", type=FloatType)
drones_SizedElement.attributes={drones_SizedElement_length, drones_SizedElement_x, drones_SizedElement_z, drones_SizedElement_height, drones_SizedElement_y, drones_SizedElement_width}

# drones_ImmovableObject class attributes and methods

# ImmovableObject class attributes and methods

# drones_Mission class attributes and methods

# drones_TemporalContainmentProxy class attributes and methods

# Relationships
parameters0: BinaryAssociation = BinaryAssociation(
    name="parameters0",
    ends={
        Property(name="drones_Parameter", type=drones_FieldObject, multiplicity=Multiplicity(1, 1)),
        Property(name="drones_FieldObject", type=drones_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
battery1: BinaryAssociation = BinaryAssociation(
    name="battery1",
    ends={
        Property(name="drones_Battery", type=drones_Drone, multiplicity=Multiplicity(1, 1)),
        Property(name="drones_Drone", type=drones_Battery, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
chargeStation2: BinaryAssociation = BinaryAssociation(
    name="chargeStation2",
    ends={
        Property(name="drones_ChargeStation", type=drones_Drone, multiplicity=Multiplicity(1, 1)),
        Property(name="drones_Drone3", type=drones_ChargeStation, multiplicity=Multiplicity(1, 1))
    }
)
supportedActions4: BinaryAssociation = BinaryAssociation(
    name="supportedActions4",
    ends={
        Property(name="drones_Action", type=drones_Drone, multiplicity=Multiplicity(1, 1)),
        Property(name="drones_Drone5", type=drones_Action, multiplicity=Multiplicity(0, 9999))
    }
)
fieldObjects6: BinaryAssociation = BinaryAssociation(
    name="fieldObjects6",
    ends={
        Property(name="drones_FieldObject7", type=drones_Mission, multiplicity=Multiplicity(1, 1)),
        Property(name="drones_Mission", type=drones_FieldObject, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
drones8: BinaryAssociation = BinaryAssociation(
    name="drones8",
    ends={
        Property(name="drones_Drone10", type=drones_Mission, multiplicity=Multiplicity(1, 1)),
        Property(name="drones_Mission9", type=drones_Drone, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
temporalObjects11: BinaryAssociation = BinaryAssociation(
    name="temporalObjects11",
    ends={
        Property(name="drones_TemporalContainmentProxy", type=drones_Mission, multiplicity=Multiplicity(1, 1)),
        Property(name="drones_Mission12", type=drones_TemporalContainmentProxy, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actions13: BinaryAssociation = BinaryAssociation(
    name="actions13",
    ends={
        Property(name="drones_Action15", type=drones_Mission, multiplicity=Multiplicity(1, 1)),
        Property(name="drones_Mission14", type=drones_Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_drones_FieldObject_NamedElement = Generalization(general=NamedElement, specific=drones_FieldObject)
gen_drones_FieldObject_SizedElement = Generalization(general=SizedElement, specific=drones_FieldObject)
gen_drones_Drone_NamedElement = Generalization(general=NamedElement, specific=drones_Drone)
gen_drones_Drone_SizedElement = Generalization(general=SizedElement, specific=drones_Drone)
gen_drones_Battery_TemporalContainmentProxy = Generalization(general=TemporalContainmentProxy, specific=drones_Battery)
gen_drones_Parameter_TemporalContainmentProxy = Generalization(general=TemporalContainmentProxy, specific=drones_Parameter)
gen_drones_Action_TemporalContainmentProxy = Generalization(general=TemporalContainmentProxy, specific=drones_Action)
gen_drones_Action_NamedElement = Generalization(general=NamedElement, specific=drones_Action)
gen_drones_MovableObject_FieldObject = Generalization(general=FieldObject, specific=drones_MovableObject)
gen_drones_ImmovableObject_FieldObject = Generalization(general=FieldObject, specific=drones_ImmovableObject)
gen_drones_ChargeStation_ImmovableObject = Generalization(general=ImmovableObject, specific=drones_ChargeStation)
gen_drones_Mission_NamedElement = Generalization(general=NamedElement, specific=drones_Mission)

# Domain Model
domain_model = DomainModel(
    name="drones",
    types={drones_FieldObject, NamedElement, SizedElement, drones_Parameter, drones_Drone, drones_Battery, drones_ChargeStation, drones_Action, TemporalContainmentProxy, drones_NamedElement, drones_MovableObject, FieldObject, drones_SizedElement, drones_ImmovableObject, ImmovableObject, drones_Mission, drones_TemporalContainmentProxy, ActionKind},
    associations={parameters0, battery1, chargeStation2, supportedActions4, fieldObjects6, drones8, temporalObjects11, actions13},
    generalizations={gen_drones_FieldObject_NamedElement, gen_drones_FieldObject_SizedElement, gen_drones_Drone_NamedElement, gen_drones_Drone_SizedElement, gen_drones_Battery_TemporalContainmentProxy, gen_drones_Parameter_TemporalContainmentProxy, gen_drones_Action_TemporalContainmentProxy, gen_drones_Action_NamedElement, gen_drones_MovableObject_FieldObject, gen_drones_ImmovableObject_FieldObject, gen_drones_ChargeStation_ImmovableObject, gen_drones_Mission_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)