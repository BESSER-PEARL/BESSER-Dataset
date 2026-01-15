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
vmLogo_Turtle = Class(name="vmLogo::Turtle")
vmLogo_Point = Class(name="vmLogo::Point")
vmLogo_Segment = Class(name="vmLogo::Segment")

# vmLogo_Turtle class attributes and methods
vmLogo_Turtle_heading: Property = Property(name="heading", type=StringType)
vmLogo_Turtle_penUp: Property = Property(name="penUp", type=StringType)
vmLogo_Turtle.attributes={vmLogo_Turtle_heading, vmLogo_Turtle_penUp}

# vmLogo_Point class attributes and methods
vmLogo_Point_x: Property = Property(name="x", type=StringType)
vmLogo_Point_y: Property = Property(name="y", type=StringType)
vmLogo_Point.attributes={vmLogo_Point_y, vmLogo_Point_x}

# vmLogo_Segment class attributes and methods

# Relationships
origin6: BinaryAssociation = BinaryAssociation(
    name="origin6",
    ends={
        Property(name="vmLogo_Point8", type=vmLogo_Segment, multiplicity=Multiplicity(1, 1)),
        Property(name="vmLogo_Segment7", type=vmLogo_Point, multiplicity=Multiplicity(1, 1))
    }
)
destination9: BinaryAssociation = BinaryAssociation(
    name="destination9",
    ends={
        Property(name="vmLogo_Point11", type=vmLogo_Segment, multiplicity=Multiplicity(1, 1)),
        Property(name="vmLogo_Segment10", type=vmLogo_Point, multiplicity=Multiplicity(1, 1))
    }
)
position0: BinaryAssociation = BinaryAssociation(
    name="position0",
    ends={
        Property(name="vmLogo_Point", type=vmLogo_Turtle, multiplicity=Multiplicity(1, 1)),
        Property(name="vmLogo_Turtle", type=vmLogo_Point, multiplicity=Multiplicity(0, 1))
    }
)
drawings1: BinaryAssociation = BinaryAssociation(
    name="drawings1",
    ends={
        Property(name="vmLogo_Segment", type=vmLogo_Turtle, multiplicity=Multiplicity(1, 1)),
        Property(name="vmLogo_Turtle2", type=vmLogo_Segment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
points3: BinaryAssociation = BinaryAssociation(
    name="points3",
    ends={
        Property(name="vmLogo_Point5", type=vmLogo_Turtle, multiplicity=Multiplicity(1, 1)),
        Property(name="vmLogo_Turtle4", type=vmLogo_Point, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="vmLogo",
    types={vmLogo_Turtle, vmLogo_Point, vmLogo_Segment},
    associations={origin6, destination9, position0, drawings1, points3},
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