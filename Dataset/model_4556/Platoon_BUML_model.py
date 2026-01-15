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
platoon_World = Class(name="platoon::World")
platoon_Platoon = Class(name="platoon::Platoon")
platoon_Route = Class(name="platoon::Route")
platoon_Constraints = Class(name="platoon::Constraints")
platoon_LeadVehicle = Class(name="platoon::LeadVehicle")
platoon_TurnRight = Class(name="platoon::TurnRight")
platoon_Constraint = Class(name="platoon::Constraint", is_abstract=True)
platoon_headway = Class(name="platoon::headway")
Constraint = Class(name="Constraint")
platoon_FollowVehicle = Class(name="platoon::FollowVehicle")
platoon_Vehicle = Class(name="platoon::Vehicle", is_abstract=True)
Vehicle = Class(name="Vehicle")
platoon_Step = Class(name="platoon::Step", is_abstract=True)
platoon_Forward = Class(name="platoon::Forward")
Step = Class(name="Step")
platoon_Turn = Class(name="platoon::Turn", is_abstract=True)
platoon_TurnLeft = Class(name="platoon::TurnLeft")
Turn = Class(name="Turn")

# platoon_World class attributes and methods

# platoon_Platoon class attributes and methods

# platoon_Route class attributes and methods
platoon_Route_name: Property = Property(name="name", type=StringType)
platoon_Route.attributes={platoon_Route_name}

# platoon_Constraints class attributes and methods

# platoon_LeadVehicle class attributes and methods

# platoon_TurnRight class attributes and methods

# platoon_Constraint class attributes and methods

# platoon_headway class attributes and methods
platoon_headway_lowbound: Property = Property(name="lowbound", type=IntegerType)
platoon_headway_upbound: Property = Property(name="upbound", type=IntegerType)
platoon_headway.attributes={platoon_headway_upbound, platoon_headway_lowbound}

# Constraint class attributes and methods

# platoon_FollowVehicle class attributes and methods

# platoon_Vehicle class attributes and methods
platoon_Vehicle_name: Property = Property(name="name", type=StringType)
platoon_Vehicle.attributes={platoon_Vehicle_name}

# Vehicle class attributes and methods

# platoon_Step class attributes and methods

# platoon_Forward class attributes and methods
platoon_Forward_distance: Property = Property(name="distance", type=IntegerType)
platoon_Forward.attributes={platoon_Forward_distance}

# Step class attributes and methods

# platoon_Turn class attributes and methods

# platoon_TurnLeft class attributes and methods

# Turn class attributes and methods

# Relationships
platoon0: BinaryAssociation = BinaryAssociation(
    name="platoon0",
    ends={
        Property(name="platoon_Platoon", type=platoon_World, multiplicity=Multiplicity(1, 1)),
        Property(name="platoon_World", type=platoon_Platoon, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
routes1: BinaryAssociation = BinaryAssociation(
    name="routes1",
    ends={
        Property(name="platoon_Route", type=platoon_World, multiplicity=Multiplicity(1, 1)),
        Property(name="platoon_World2", type=platoon_Route, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
constraints3: BinaryAssociation = BinaryAssociation(
    name="constraints3",
    ends={
        Property(name="platoon_Constraints", type=platoon_World, multiplicity=Multiplicity(1, 1)),
        Property(name="platoon_World4", type=platoon_Constraints, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
leader5: BinaryAssociation = BinaryAssociation(
    name="leader5",
    ends={
        Property(name="platoon_LeadVehicle", type=platoon_Platoon, multiplicity=Multiplicity(1, 1)),
        Property(name="platoon_Platoon6", type=platoon_LeadVehicle, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
list16: BinaryAssociation = BinaryAssociation(
    name="list16",
    ends={
        Property(name="platoon_Constraint", type=platoon_Constraints, multiplicity=Multiplicity(1, 1)),
        Property(name="platoon_Constraints17", type=platoon_Constraint, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
followers7: BinaryAssociation = BinaryAssociation(
    name="followers7",
    ends={
        Property(name="platoon_FollowVehicle", type=platoon_Platoon, multiplicity=Multiplicity(1, 1)),
        Property(name="platoon_Platoon8", type=platoon_FollowVehicle, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
route9: BinaryAssociation = BinaryAssociation(
    name="route9",
    ends={
        Property(name="platoon_Route11", type=platoon_LeadVehicle, multiplicity=Multiplicity(1, 1)),
        Property(name="platoon_LeadVehicle10", type=platoon_Route, multiplicity=Multiplicity(1, 1))
    }
)
frontrunner12: BinaryAssociation = BinaryAssociation(
    name="frontrunner12",
    ends={
        Property(name="platoon_Vehicle", type=platoon_FollowVehicle, multiplicity=Multiplicity(1, 1)),
        Property(name="platoon_FollowVehicle13", type=platoon_Vehicle, multiplicity=Multiplicity(1, 1))
    }
)
steps14: BinaryAssociation = BinaryAssociation(
    name="steps14",
    ends={
        Property(name="platoon_Step", type=platoon_Route, multiplicity=Multiplicity(1, 1)),
        Property(name="platoon_Route15", type=platoon_Step, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)

# Generalizations
gen_platoon_TurnRight_Turn = Generalization(general=Turn, specific=platoon_TurnRight)
gen_platoon_headway_Constraint = Generalization(general=Constraint, specific=platoon_headway)
gen_platoon_LeadVehicle_Vehicle = Generalization(general=Vehicle, specific=platoon_LeadVehicle)
gen_platoon_FollowVehicle_Vehicle = Generalization(general=Vehicle, specific=platoon_FollowVehicle)
gen_platoon_Forward_Step = Generalization(general=Step, specific=platoon_Forward)
gen_platoon_Turn_Step = Generalization(general=Step, specific=platoon_Turn)
gen_platoon_TurnLeft_Turn = Generalization(general=Turn, specific=platoon_TurnLeft)

# Domain Model
domain_model = DomainModel(
    name="platoon",
    types={platoon_World, platoon_Platoon, platoon_Route, platoon_Constraints, platoon_LeadVehicle, platoon_TurnRight, platoon_Constraint, platoon_headway, Constraint, platoon_FollowVehicle, platoon_Vehicle, Vehicle, platoon_Step, platoon_Forward, Step, platoon_Turn, platoon_TurnLeft, Turn},
    associations={platoon0, routes1, constraints3, leader5, list16, followers7, route9, frontrunner12, steps14},
    generalizations={gen_platoon_TurnRight_Turn, gen_platoon_headway_Constraint, gen_platoon_LeadVehicle_Vehicle, gen_platoon_FollowVehicle_Vehicle, gen_platoon_Forward_Step, gen_platoon_Turn_Step, gen_platoon_TurnLeft_Turn},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)