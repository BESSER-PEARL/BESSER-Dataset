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
platoon_Root = Class(name="platoon::Root")
platoon_Platoon = Class(name="platoon::Platoon")
platoon_Route = Class(name="platoon::Route")
platoon_Constraints = Class(name="platoon::Constraints")
platoon_routeCommand = Class(name="platoon::routeCommand", is_abstract=True)
platoon_LeaderVehicle = Class(name="platoon::LeaderVehicle")
platoon_FollowingVehicle = Class(name="platoon::FollowingVehicle")
platoon_Forward = Class(name="platoon::Forward")
routeCommand = Class(name="routeCommand")
platoon_TurnLeft = Class(name="platoon::TurnLeft")
platoon_TurnRight = Class(name="platoon::TurnRight")
platoon_Vehicle = Class(name="platoon::Vehicle", is_abstract=True)
Vehicle = Class(name="Vehicle")

# platoon_Root class attributes and methods

# platoon_Platoon class attributes and methods

# platoon_Route class attributes and methods
platoon_Route_name: Property = Property(name="name", type=StringType)
platoon_Route.attributes={platoon_Route_name}

# platoon_Constraints class attributes and methods
platoon_Constraints_lbound: Property = Property(name="lbound", type=IntegerType)
platoon_Constraints_ubound: Property = Property(name="ubound", type=IntegerType)
platoon_Constraints.attributes={platoon_Constraints_lbound, platoon_Constraints_ubound}

# platoon_routeCommand class attributes and methods

# platoon_LeaderVehicle class attributes and methods

# platoon_FollowingVehicle class attributes and methods

# platoon_Forward class attributes and methods
platoon_Forward_distance: Property = Property(name="distance", type=IntegerType)
platoon_Forward.attributes={platoon_Forward_distance}

# routeCommand class attributes and methods

# platoon_TurnLeft class attributes and methods

# platoon_TurnRight class attributes and methods

# platoon_Vehicle class attributes and methods
platoon_Vehicle_name: Property = Property(name="name", type=StringType)
platoon_Vehicle.attributes={platoon_Vehicle_name}

# Vehicle class attributes and methods

# Relationships
platoon0: BinaryAssociation = BinaryAssociation(
    name="platoon0",
    ends={
        Property(name="platoon_Platoon", type=platoon_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="platoon_Root", type=platoon_Platoon, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
route1: BinaryAssociation = BinaryAssociation(
    name="route1",
    ends={
        Property(name="platoon_Route", type=platoon_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="platoon_Root2", type=platoon_Route, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
constraints3: BinaryAssociation = BinaryAssociation(
    name="constraints3",
    ends={
        Property(name="platoon_Constraints", type=platoon_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="platoon_Root4", type=platoon_Constraints, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
routeCommands5: BinaryAssociation = BinaryAssociation(
    name="routeCommands5",
    ends={
        Property(name="platoon_routeCommand", type=platoon_Route, multiplicity=Multiplicity(1, 1)),
        Property(name="platoon_Route6", type=platoon_routeCommand, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
leaderVehicle7: BinaryAssociation = BinaryAssociation(
    name="leaderVehicle7",
    ends={
        Property(name="platoon_LeaderVehicle", type=platoon_Platoon, multiplicity=Multiplicity(1, 1)),
        Property(name="platoon_Platoon8", type=platoon_LeaderVehicle, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
followingVehicle9: BinaryAssociation = BinaryAssociation(
    name="followingVehicle9",
    ends={
        Property(name="platoon_FollowingVehicle", type=platoon_Platoon, multiplicity=Multiplicity(1, 1)),
        Property(name="platoon_Platoon10", type=platoon_FollowingVehicle, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
following11: BinaryAssociation = BinaryAssociation(
    name="following11",
    ends={
        Property(name="platoon_Vehicle", type=platoon_FollowingVehicle, multiplicity=Multiplicity(1, 1)),
        Property(name="platoon_FollowingVehicle12", type=platoon_Vehicle, multiplicity=Multiplicity(1, 1))
    }
)
route13: BinaryAssociation = BinaryAssociation(
    name="route13",
    ends={
        Property(name="platoon_Route15", type=platoon_LeaderVehicle, multiplicity=Multiplicity(1, 1)),
        Property(name="platoon_LeaderVehicle14", type=platoon_Route, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_platoon_Forward_routeCommand = Generalization(general=routeCommand, specific=platoon_Forward)
gen_platoon_TurnLeft_routeCommand = Generalization(general=routeCommand, specific=platoon_TurnLeft)
gen_platoon_TurnRight_routeCommand = Generalization(general=routeCommand, specific=platoon_TurnRight)
gen_platoon_LeaderVehicle_Vehicle = Generalization(general=Vehicle, specific=platoon_LeaderVehicle)
gen_platoon_FollowingVehicle_Vehicle = Generalization(general=Vehicle, specific=platoon_FollowingVehicle)

# Domain Model
domain_model = DomainModel(
    name="platoon",
    types={platoon_Root, platoon_Platoon, platoon_Route, platoon_Constraints, platoon_routeCommand, platoon_LeaderVehicle, platoon_FollowingVehicle, platoon_Forward, routeCommand, platoon_TurnLeft, platoon_TurnRight, platoon_Vehicle, Vehicle},
    associations={platoon0, route1, constraints3, routeCommands5, leaderVehicle7, followingVehicle9, following11, route13},
    generalizations={gen_platoon_Forward_routeCommand, gen_platoon_TurnLeft_routeCommand, gen_platoon_TurnRight_routeCommand, gen_platoon_LeaderVehicle_Vehicle, gen_platoon_FollowingVehicle_Vehicle},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)