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
platoon_Vehicle = Class(name="platoon::Vehicle", is_abstract=True)
Vehicle = Class(name="Vehicle")
platoon_Platoon = Class(name="platoon::Platoon")
platoon_LeadingVehicle = Class(name="platoon::LeadingVehicle")
platoon_FollowVehicle = Class(name="platoon::FollowVehicle")
platoon_Route = Class(name="platoon::Route")
platoon_Command = Class(name="platoon::Command")
platoon_ForwardCommand = Class(name="platoon::ForwardCommand")
Command = Class(name="Command")
platoon_TurnCommand = Class(name="platoon::TurnCommand")
platoon_HeadwayConstraint = Class(name="platoon::HeadwayConstraint")
Constraint = Class(name="Constraint")
platoon_Constraint = Class(name="platoon::Constraint")
platoon_World = Class(name="platoon::World")
platoon_Constraints = Class(name="platoon::Constraints")

# platoon_Vehicle class attributes and methods
platoon_Vehicle_name: Property = Property(name="name", type=StringType)
platoon_Vehicle.attributes={platoon_Vehicle_name}

# Vehicle class attributes and methods

# platoon_Platoon class attributes and methods

# platoon_LeadingVehicle class attributes and methods

# platoon_FollowVehicle class attributes and methods

# platoon_Route class attributes and methods
platoon_Route_name: Property = Property(name="name", type=StringType)
platoon_Route.attributes={platoon_Route_name}

# platoon_Command class attributes and methods

# platoon_ForwardCommand class attributes and methods
platoon_ForwardCommand_distance: Property = Property(name="distance", type=IntegerType)
platoon_ForwardCommand.attributes={platoon_ForwardCommand_distance}

# Command class attributes and methods

# platoon_TurnCommand class attributes and methods
platoon_TurnCommand_direction: Property = Property(name="direction", type=StringType)
platoon_TurnCommand.attributes={platoon_TurnCommand_direction}

# platoon_HeadwayConstraint class attributes and methods
platoon_HeadwayConstraint_min: Property = Property(name="min", type=IntegerType)
platoon_HeadwayConstraint_max: Property = Property(name="max", type=IntegerType)
platoon_HeadwayConstraint.attributes={platoon_HeadwayConstraint_max, platoon_HeadwayConstraint_min}

# Constraint class attributes and methods

# platoon_Constraint class attributes and methods

# platoon_World class attributes and methods

# platoon_Constraints class attributes and methods

# Relationships
commands3: BinaryAssociation = BinaryAssociation(
    name="commands3",
    ends={
        Property(name="platoon_Command", type=platoon_Route, multiplicity=Multiplicity(1, 1)),
        Property(name="platoon_Route", type=platoon_Command, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
follows4: BinaryAssociation = BinaryAssociation(
    name="follows4",
    ends={
        Property(name="platoon_Vehicle", type=platoon_FollowVehicle, multiplicity=Multiplicity(1, 1)),
        Property(name="platoon_FollowVehicle5", type=platoon_Vehicle, multiplicity=Multiplicity(1, 1))
    }
)
LV0: BinaryAssociation = BinaryAssociation(
    name="LV0",
    ends={
        Property(name="platoon_LeadingVehicle", type=platoon_Platoon, multiplicity=Multiplicity(1, 1)),
        Property(name="platoon_Platoon", type=platoon_LeadingVehicle, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
FV1: BinaryAssociation = BinaryAssociation(
    name="FV1",
    ends={
        Property(name="platoon_FollowVehicle", type=platoon_Platoon, multiplicity=Multiplicity(1, 1)),
        Property(name="platoon_Platoon2", type=platoon_FollowVehicle, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
route6: BinaryAssociation = BinaryAssociation(
    name="route6",
    ends={
        Property(name="platoon_Route8", type=platoon_LeadingVehicle, multiplicity=Multiplicity(1, 1)),
        Property(name="platoon_LeadingVehicle7", type=platoon_Route, multiplicity=Multiplicity(1, 1))
    }
)
platoon9: BinaryAssociation = BinaryAssociation(
    name="platoon9",
    ends={
        Property(name="platoon_Platoon10", type=platoon_World, multiplicity=Multiplicity(1, 1)),
        Property(name="platoon_World", type=platoon_Platoon, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
route11: BinaryAssociation = BinaryAssociation(
    name="route11",
    ends={
        Property(name="platoon_Route13", type=platoon_World, multiplicity=Multiplicity(1, 1)),
        Property(name="platoon_World12", type=platoon_Route, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
constraints14: BinaryAssociation = BinaryAssociation(
    name="constraints14",
    ends={
        Property(name="platoon_Constraints", type=platoon_World, multiplicity=Multiplicity(1, 1)),
        Property(name="platoon_World15", type=platoon_Constraints, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constraints16: BinaryAssociation = BinaryAssociation(
    name="constraints16",
    ends={
        Property(name="platoon_Constraint", type=platoon_Constraints, multiplicity=Multiplicity(1, 1)),
        Property(name="platoon_Constraints17", type=platoon_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_platoon_FollowVehicle_Vehicle = Generalization(general=Vehicle, specific=platoon_FollowVehicle)
gen_platoon_LeadingVehicle_Vehicle = Generalization(general=Vehicle, specific=platoon_LeadingVehicle)
gen_platoon_ForwardCommand_Command = Generalization(general=Command, specific=platoon_ForwardCommand)
gen_platoon_TurnCommand_Command = Generalization(general=Command, specific=platoon_TurnCommand)
gen_platoon_HeadwayConstraint_Constraint = Generalization(general=Constraint, specific=platoon_HeadwayConstraint)

# Domain Model
domain_model = DomainModel(
    name="platoon",
    types={platoon_Vehicle, Vehicle, platoon_Platoon, platoon_LeadingVehicle, platoon_FollowVehicle, platoon_Route, platoon_Command, platoon_ForwardCommand, Command, platoon_TurnCommand, platoon_HeadwayConstraint, Constraint, platoon_Constraint, platoon_World, platoon_Constraints},
    associations={commands3, follows4, LV0, FV1, route6, platoon9, route11, constraints14, constraints16},
    generalizations={gen_platoon_FollowVehicle_Vehicle, gen_platoon_LeadingVehicle_Vehicle, gen_platoon_ForwardCommand_Command, gen_platoon_TurnCommand_Command, gen_platoon_HeadwayConstraint_Constraint},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)