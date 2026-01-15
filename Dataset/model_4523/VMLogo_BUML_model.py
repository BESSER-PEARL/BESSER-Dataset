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
vmlogo_Turtle = Class(name="vmlogo::Turtle")
vmlogo_Point = Class(name="vmlogo::Point")
vmlogo_Segment = Class(name="vmlogo::Segment")
vmlogo_CallStack = Class(name="vmlogo::CallStack")
vmlogo_StackFrame = Class(name="vmlogo::StackFrame")
vmlogo_Variable = Class(name="vmlogo::Variable")

# vmlogo_Turtle class attributes and methods
vmlogo_Turtle_heading: Property = Property(name="heading", type=FloatType)
vmlogo_Turtle_penUp: Property = Property(name="penUp", type=BooleanType)
vmlogo_Turtle.attributes={vmlogo_Turtle_heading, vmlogo_Turtle_penUp}

# vmlogo_Point class attributes and methods
vmlogo_Point_x: Property = Property(name="x", type=FloatType)
vmlogo_Point_y: Property = Property(name="y", type=FloatType)
vmlogo_Point.attributes={vmlogo_Point_x, vmlogo_Point_y}

# vmlogo_Segment class attributes and methods

# vmlogo_CallStack class attributes and methods

# vmlogo_StackFrame class attributes and methods

# vmlogo_Variable class attributes and methods
vmlogo_Variable_name: Property = Property(name="name", type=StringType)
vmlogo_Variable_value: Property = Property(name="value", type=FloatType)
vmlogo_Variable.attributes={vmlogo_Variable_value, vmlogo_Variable_name}

# Relationships
position0: BinaryAssociation = BinaryAssociation(
    name="position0",
    ends={
        Property(name="vmlogo_Point", type=vmlogo_Turtle, multiplicity=Multiplicity(1, 1)),
        Property(name="vmlogo_Turtle", type=vmlogo_Point, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
drawings1: BinaryAssociation = BinaryAssociation(
    name="drawings1",
    ends={
        Property(name="vmlogo_Segment", type=vmlogo_Turtle, multiplicity=Multiplicity(1, 1)),
        Property(name="vmlogo_Turtle2", type=vmlogo_Segment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
callStack3: BinaryAssociation = BinaryAssociation(
    name="callStack3",
    ends={
        Property(name="vmlogo_CallStack", type=vmlogo_Turtle, multiplicity=Multiplicity(1, 1)),
        Property(name="vmlogo_Turtle4", type=vmlogo_CallStack, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
begin5: BinaryAssociation = BinaryAssociation(
    name="begin5",
    ends={
        Property(name="vmlogo_Point7", type=vmlogo_Segment, multiplicity=Multiplicity(1, 1)),
        Property(name="vmlogo_Segment6", type=vmlogo_Point, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
end8: BinaryAssociation = BinaryAssociation(
    name="end8",
    ends={
        Property(name="vmlogo_Point10", type=vmlogo_Segment, multiplicity=Multiplicity(1, 1)),
        Property(name="vmlogo_Segment9", type=vmlogo_Point, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
frames11: BinaryAssociation = BinaryAssociation(
    name="frames11",
    ends={
        Property(name="vmlogo_StackFrame", type=vmlogo_CallStack, multiplicity=Multiplicity(1, 1)),
        Property(name="vmlogo_CallStack12", type=vmlogo_StackFrame, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variables13: BinaryAssociation = BinaryAssociation(
    name="variables13",
    ends={
        Property(name="vmlogo_Variable", type=vmlogo_StackFrame, multiplicity=Multiplicity(1, 1)),
        Property(name="vmlogo_StackFrame14", type=vmlogo_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="vmlogo",
    types={vmlogo_Turtle, vmlogo_Point, vmlogo_Segment, vmlogo_CallStack, vmlogo_StackFrame, vmlogo_Variable},
    associations={position0, drawings1, callStack3, begin5, end8, frames11, variables13},
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