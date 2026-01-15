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
vmlogo_Context = Class(name="vmlogo::Context")
vmlogo_Turtle = Class(name="vmlogo::Turtle")
vmlogo_CallStack = Class(name="vmlogo::CallStack")
vmlogo_Point = Class(name="vmlogo::Point")
vmlogo_Segment = Class(name="vmlogo::Segment")
vmlogo_StackFrame = Class(name="vmlogo::StackFrame")

# vmlogo_Context class attributes and methods

# vmlogo_Turtle class attributes and methods
vmlogo_Turtle_heading: Property = Property(name="heading", type=FloatType)
vmlogo_Turtle_penUp: Property = Property(name="penUp", type=BooleanType)
vmlogo_Turtle.attributes={vmlogo_Turtle_penUp, vmlogo_Turtle_heading}

# vmlogo_CallStack class attributes and methods

# vmlogo_Point class attributes and methods
vmlogo_Point_x: Property = Property(name="x", type=FloatType)
vmlogo_Point_y: Property = Property(name="y", type=FloatType)
vmlogo_Point.attributes={vmlogo_Point_x, vmlogo_Point_y}

# vmlogo_Segment class attributes and methods

# vmlogo_StackFrame class attributes and methods
vmlogo_StackFrame_variables: Property = Property(name="variables", type=StringType)
vmlogo_StackFrame.attributes={vmlogo_StackFrame_variables}

# Relationships
turtle0: BinaryAssociation = BinaryAssociation(
    name="turtle0",
    ends={
        Property(name="vmlogo_Turtle", type=vmlogo_Context, multiplicity=Multiplicity(1, 1)),
        Property(name="vmlogo_Context", type=vmlogo_Turtle, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
callStack1: BinaryAssociation = BinaryAssociation(
    name="callStack1",
    ends={
        Property(name="vmlogo_CallStack", type=vmlogo_Context, multiplicity=Multiplicity(1, 1)),
        Property(name="vmlogo_Context2", type=vmlogo_CallStack, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
position3: BinaryAssociation = BinaryAssociation(
    name="position3",
    ends={
        Property(name="vmlogo_Point", type=vmlogo_Turtle, multiplicity=Multiplicity(1, 1)),
        Property(name="vmlogo_Turtle4", type=vmlogo_Point, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
drawings5: BinaryAssociation = BinaryAssociation(
    name="drawings5",
    ends={
        Property(name="vmlogo_Segment", type=vmlogo_Turtle, multiplicity=Multiplicity(1, 1)),
        Property(name="vmlogo_Turtle6", type=vmlogo_Segment, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
begin7: BinaryAssociation = BinaryAssociation(
    name="begin7",
    ends={
        Property(name="vmlogo_Point9", type=vmlogo_Segment, multiplicity=Multiplicity(1, 1)),
        Property(name="vmlogo_Segment8", type=vmlogo_Point, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
end10: BinaryAssociation = BinaryAssociation(
    name="end10",
    ends={
        Property(name="vmlogo_Point12", type=vmlogo_Segment, multiplicity=Multiplicity(1, 1)),
        Property(name="vmlogo_Segment11", type=vmlogo_Point, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
frames13: BinaryAssociation = BinaryAssociation(
    name="frames13",
    ends={
        Property(name="vmlogo_StackFrame", type=vmlogo_CallStack, multiplicity=Multiplicity(1, 1)),
        Property(name="vmlogo_CallStack14", type=vmlogo_StackFrame, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="vmlogo",
    types={vmlogo_Context, vmlogo_Turtle, vmlogo_CallStack, vmlogo_Point, vmlogo_Segment, vmlogo_StackFrame},
    associations={turtle0, callStack1, position3, drawings5, begin7, end10, frames13},
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