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
kmLogo_VM_Turtle = Class(name="kmLogo::VM::Turtle")
Point = Class(name="Point")
Segment = Class(name="Segment")
kmLogo_VM_Point = Class(name="kmLogo::VM::Point")
kmLogo_VM_Segment = Class(name="kmLogo::VM::Segment")

# kmLogo_VM_Turtle class attributes and methods
kmLogo_VM_Turtle_heading: Property = Property(name="heading", type=StringType)
kmLogo_VM_Turtle_penUp: Property = Property(name="penUp", type=StringType)
kmLogo_VM_Turtle.attributes={kmLogo_VM_Turtle_penUp, kmLogo_VM_Turtle_heading}

# Point class attributes and methods

# Segment class attributes and methods

# kmLogo_VM_Point class attributes and methods
kmLogo_VM_Point_x: Property = Property(name="x", type=StringType)
kmLogo_VM_Point_y: Property = Property(name="y", type=StringType)
kmLogo_VM_Point.attributes={kmLogo_VM_Point_x, kmLogo_VM_Point_y}

# kmLogo_VM_Segment class attributes and methods

# Relationships
position0: BinaryAssociation = BinaryAssociation(
    name="position0",
    ends={
        Property(name="Point", type=kmLogo_VM_Turtle, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_VM_Turtle", type=Point, multiplicity=Multiplicity(0, 1))
    }
)
drawings1: BinaryAssociation = BinaryAssociation(
    name="drawings1",
    ends={
        Property(name="Segment", type=kmLogo_VM_Turtle, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_VM_Turtle2", type=Segment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
points3: BinaryAssociation = BinaryAssociation(
    name="points3",
    ends={
        Property(name="Point5", type=kmLogo_VM_Turtle, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_VM_Turtle4", type=Point, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
origin6: BinaryAssociation = BinaryAssociation(
    name="origin6",
    ends={
        Property(name="Point7", type=kmLogo_VM_Segment, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_VM_Segment", type=Point, multiplicity=Multiplicity(1, 1))
    }
)
destination8: BinaryAssociation = BinaryAssociation(
    name="destination8",
    ends={
        Property(name="Point10", type=kmLogo_VM_Segment, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_VM_Segment9", type=Point, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="kmLogo",
    types={kmLogo_VM_Turtle, Point, Segment, kmLogo_VM_Point, kmLogo_VM_Segment},
    associations={position0, drawings1, points3, origin6, destination8},
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