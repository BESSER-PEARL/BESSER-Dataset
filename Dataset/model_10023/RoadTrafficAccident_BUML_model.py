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
EA_Model_RoadwayWithAccident = Class(name="EA_Model_RoadwayWithAccident")
EA_Model_CrashedVehicle = Class(name="EA_Model_CrashedVehicle")
TravelingVehicle = Class(name="TravelingVehicle")
EA_Model_RoadTrafficAccident = Class(name="EA_Model_RoadTrafficAccident")
EA_Model_DeceasedPerson = Class(name="EA_Model_DeceasedPerson")
Person = Class(name="Person")
EA_Model_Driver = Class(name="EA_Model_Driver")
Traveler = Class(name="Traveler")
EA_Model_LivingPerson = Class(name="EA_Model_LivingPerson")
EA_Model_Passenger = Class(name="EA_Model_Passenger")
EA_Model_Person = Class(name="EA_Model_Person")
EA_Model_RearEndCollision = Class(name="EA_Model_RearEndCollision")
RoadTrafficAccident = Class(name="RoadTrafficAccident")
EA_Model_Victim = Class(name="EA_Model_Victim")
EA_Model_Roadway = Class(name="EA_Model_Roadway")
Roadway = Class(name="Roadway")
EA_Model_Travel = Class(name="EA_Model_Travel")
EA_Model_Traveler = Class(name="EA_Model_Traveler")
EA_Model_TravelingVehicle = Class(name="EA_Model_TravelingVehicle")
Vehicle = Class(name="Vehicle")
EA_Model_Vehicle = Class(name="EA_Model_Vehicle")

# EA_Model_RoadwayWithAccident class attributes and methods

# EA_Model_CrashedVehicle class attributes and methods

# TravelingVehicle class attributes and methods

# EA_Model_RoadTrafficAccident class attributes and methods
EA_Model_RoadTrafficAccident_fatalvictims: Property = Property(name="fatalvictims", type=IntegerType)
EA_Model_RoadTrafficAccident.attributes={EA_Model_RoadTrafficAccident_fatalvictims}

# EA_Model_DeceasedPerson class attributes and methods

# Person class attributes and methods

# EA_Model_Driver class attributes and methods

# Traveler class attributes and methods

# EA_Model_LivingPerson class attributes and methods

# EA_Model_Passenger class attributes and methods

# EA_Model_Person class attributes and methods

# EA_Model_RearEndCollision class attributes and methods

# RoadTrafficAccident class attributes and methods

# EA_Model_Victim class attributes and methods

# EA_Model_Roadway class attributes and methods

# Roadway class attributes and methods

# EA_Model_Travel class attributes and methods

# EA_Model_Traveler class attributes and methods

# EA_Model_TravelingVehicle class attributes and methods

# Vehicle class attributes and methods

# EA_Model_Vehicle class attributes and methods

# Relationships
accident0: BinaryAssociation = BinaryAssociation(
    name="accident0",
    ends={
        Property(name="RoadTrafficAccident", type=EA_Model_CrashedVehicle, multiplicity=Multiplicity(1, 1)),
        Property(name="vehicles", type=EA_Model_RoadTrafficAccident, multiplicity=Multiplicity(1, 1))
    }
)
roadtrafficaccident7: BinaryAssociation = BinaryAssociation(
    name="roadtrafficaccident7",
    ends={
        Property(name="RoadTrafficAccident8", type=EA_Model_RoadwayWithAccident, multiplicity=Multiplicity(1, 1)),
        Property(name="roadwaywithaccident", type=EA_Model_RoadTrafficAccident, multiplicity=Multiplicity(1, 9999))
    }
)
roadwaywithaccident1: BinaryAssociation = BinaryAssociation(
    name="roadwaywithaccident1",
    ends={
        Property(name="RoadwayWithAccident", type=EA_Model_CrashedVehicle, multiplicity=Multiplicity(1, 1)),
        Property(name="crashedvehicle", type=EA_Model_RoadwayWithAccident, multiplicity=Multiplicity(1, 1))
    }
)
vehicles2: BinaryAssociation = BinaryAssociation(
    name="vehicles2",
    ends={
        Property(name="CrashedVehicle", type=EA_Model_RoadTrafficAccident, multiplicity=Multiplicity(1, 1)),
        Property(name="accident", type=EA_Model_CrashedVehicle, multiplicity=Multiplicity(1, 9999))
    }
)
victims3: BinaryAssociation = BinaryAssociation(
    name="victims3",
    ends={
        Property(name="Victim", type=EA_Model_RoadTrafficAccident, multiplicity=Multiplicity(1, 1)),
        Property(name="accident4", type=EA_Model_Victim, multiplicity=Multiplicity(1, 9999))
    }
)
roadwaywithaccident5: BinaryAssociation = BinaryAssociation(
    name="roadwaywithaccident5",
    ends={
        Property(name="RoadwayWithAccident6", type=EA_Model_RoadTrafficAccident, multiplicity=Multiplicity(1, 1)),
        Property(name="roadtrafficaccident", type=EA_Model_RoadwayWithAccident, multiplicity=Multiplicity(1, 1))
    }
)
crashedvehicle9: BinaryAssociation = BinaryAssociation(
    name="crashedvehicle9",
    ends={
        Property(name="CrashedVehicle11", type=EA_Model_RoadwayWithAccident, multiplicity=Multiplicity(1, 1)),
        Property(name="roadwaywithaccident10", type=EA_Model_CrashedVehicle, multiplicity=Multiplicity(1, 9999))
    }
)
travelers12: BinaryAssociation = BinaryAssociation(
    name="travelers12",
    ends={
        Property(name="Traveler", type=EA_Model_Travel, multiplicity=Multiplicity(1, 1)),
        Property(name="travel", type=EA_Model_Traveler, multiplicity=Multiplicity(1, 9999))
    }
)
vehicle13: BinaryAssociation = BinaryAssociation(
    name="vehicle13",
    ends={
        Property(name="TravelingVehicle", type=EA_Model_Travel, multiplicity=Multiplicity(1, 1)),
        Property(name="travel14", type=EA_Model_TravelingVehicle, multiplicity=Multiplicity(1, 1))
    }
)
travel15: BinaryAssociation = BinaryAssociation(
    name="travel15",
    ends={
        Property(name="Travel", type=EA_Model_Traveler, multiplicity=Multiplicity(1, 1)),
        Property(name="travelers", type=EA_Model_Travel, multiplicity=Multiplicity(1, 1))
    }
)
travel16: BinaryAssociation = BinaryAssociation(
    name="travel16",
    ends={
        Property(name="Travel17", type=EA_Model_TravelingVehicle, multiplicity=Multiplicity(1, 1)),
        Property(name="vehicle", type=EA_Model_Travel, multiplicity=Multiplicity(1, 1))
    }
)
accident18: BinaryAssociation = BinaryAssociation(
    name="accident18",
    ends={
        Property(name="RoadTrafficAccident19", type=EA_Model_Victim, multiplicity=Multiplicity(1, 1)),
        Property(name="victims", type=EA_Model_RoadTrafficAccident, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_EA_Model_CrashedVehicle_TravelingVehicle = Generalization(general=TravelingVehicle, specific=EA_Model_CrashedVehicle)
gen_EA_Model_DeceasedPerson_Person = Generalization(general=Person, specific=EA_Model_DeceasedPerson)
gen_EA_Model_Driver_Traveler = Generalization(general=Traveler, specific=EA_Model_Driver)
gen_EA_Model_LivingPerson_Person = Generalization(general=Person, specific=EA_Model_LivingPerson)
gen_EA_Model_Passenger_Traveler = Generalization(general=Traveler, specific=EA_Model_Passenger)
gen_EA_Model_RearEndCollision_RoadTrafficAccident = Generalization(general=RoadTrafficAccident, specific=EA_Model_RearEndCollision)
gen_EA_Model_RoadwayWithAccident_Roadway = Generalization(general=Roadway, specific=EA_Model_RoadwayWithAccident)
gen_EA_Model_Traveler_Person = Generalization(general=Person, specific=EA_Model_Traveler)
gen_EA_Model_TravelingVehicle_Vehicle = Generalization(general=Vehicle, specific=EA_Model_TravelingVehicle)
gen_EA_Model_Victim_Traveler = Generalization(general=Traveler, specific=EA_Model_Victim)


# OCL Constraints
Unnamed: Constraint = Constraint(
    name="Unnamed",
    context=EA_Model_RearEndCollision,
    expression="context RearEndCollision inv: self.vehicles->size()=2",
    language="OCL"
)
Unnamed1: Constraint = Constraint(
    name="Unnamed1",
    context=EA_Model_TravelingVehicle,
    expression="context TravelingVehicle inv: self.travel.travelers->one(v|v.oclIsKindOf(Driver))",
    language="OCL"
)
one_vehicle: Constraint = Constraint(
    name="one_vehicle",
    context=EA_Model_RoadTrafficAccident,
    expression="context RoadTrafficAccident inv: self.vehicles->size()=1",
    language="OCL"
)
travelers_are_victims_in_accident: Constraint = Constraint(
    name="travelers_are_victims_in_accident",
    context=EA_Model_CrashedVehicle,
    expression="context CrashedVehicle inv: self.travel.travelers->forAll(t|t.oclIsKindOf(Victim) andt.oclAsType(Victim).accident = self.accident)",
    language="OCL"
)

# Domain Model
domain_model = DomainModel(
    name="EA_Model",
    types={EA_Model_RoadwayWithAccident, EA_Model_CrashedVehicle, TravelingVehicle, EA_Model_RoadTrafficAccident, EA_Model_DeceasedPerson, Person, EA_Model_Driver, Traveler, EA_Model_LivingPerson, EA_Model_Passenger, EA_Model_Person, EA_Model_RearEndCollision, RoadTrafficAccident, EA_Model_Victim, EA_Model_Roadway, Roadway, EA_Model_Travel, EA_Model_Traveler, EA_Model_TravelingVehicle, Vehicle, EA_Model_Vehicle},
    associations={accident0, roadtrafficaccident7, roadwaywithaccident1, vehicles2, victims3, roadwaywithaccident5, crashedvehicle9, travelers12, vehicle13, travel15, travel16, accident18},
    constraints={Unnamed, Unnamed1, one_vehicle, travelers_are_victims_in_accident},
    generalizations={gen_EA_Model_CrashedVehicle_TravelingVehicle, gen_EA_Model_DeceasedPerson_Person, gen_EA_Model_Driver_Traveler, gen_EA_Model_LivingPerson_Person, gen_EA_Model_Passenger_Traveler, gen_EA_Model_RearEndCollision_RoadTrafficAccident, gen_EA_Model_RoadwayWithAccident_Roadway, gen_EA_Model_Traveler_Person, gen_EA_Model_TravelingVehicle_Vehicle, gen_EA_Model_Victim_Traveler},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)