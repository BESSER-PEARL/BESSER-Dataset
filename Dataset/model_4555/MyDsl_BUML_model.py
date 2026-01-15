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
myDsl_PROGRAM = Class(name="myDsl::PROGRAM")
myDsl_CMD = Class(name="myDsl::CMD")
myDsl_PAPER = Class(name="myDsl::PAPER")
CMD = Class(name="CMD")
myDsl_TURTLE = Class(name="myDsl::TURTLE")
myDsl_PENSTATE = Class(name="myDsl::PENSTATE")
myDsl_PENCOLOUR = Class(name="myDsl::PENCOLOUR")
myDsl_MOVE = Class(name="myDsl::MOVE")
myDsl_RIGHT = Class(name="myDsl::RIGHT")
myDsl_LEFT = Class(name="myDsl::LEFT")

# myDsl_PROGRAM class attributes and methods

# myDsl_CMD class attributes and methods

# myDsl_PAPER class attributes and methods
myDsl_PAPER_sizeX: Property = Property(name="sizeX", type=IntegerType)
myDsl_PAPER_sizeY: Property = Property(name="sizeY", type=IntegerType)
myDsl_PAPER_paperColour: Property = Property(name="paperColour", type=StringType)
myDsl_PAPER.attributes={myDsl_PAPER_sizeY, myDsl_PAPER_paperColour, myDsl_PAPER_sizeX}

# CMD class attributes and methods

# myDsl_TURTLE class attributes and methods
myDsl_TURTLE_startPosX: Property = Property(name="startPosX", type=IntegerType)
myDsl_TURTLE_startPosY: Property = Property(name="startPosY", type=IntegerType)
myDsl_TURTLE.attributes={myDsl_TURTLE_startPosX, myDsl_TURTLE_startPosY}

# myDsl_PENSTATE class attributes and methods
myDsl_PENSTATE_penState: Property = Property(name="penState", type=StringType)
myDsl_PENSTATE.attributes={myDsl_PENSTATE_penState}

# myDsl_PENCOLOUR class attributes and methods
myDsl_PENCOLOUR_colour: Property = Property(name="colour", type=StringType)
myDsl_PENCOLOUR.attributes={myDsl_PENCOLOUR_colour}

# myDsl_MOVE class attributes and methods
myDsl_MOVE_amount: Property = Property(name="amount", type=IntegerType)
myDsl_MOVE.attributes={myDsl_MOVE_amount}

# myDsl_RIGHT class attributes and methods
myDsl_RIGHT_amount: Property = Property(name="amount", type=IntegerType)
myDsl_RIGHT.attributes={myDsl_RIGHT_amount}

# myDsl_LEFT class attributes and methods
myDsl_LEFT_amount: Property = Property(name="amount", type=IntegerType)
myDsl_LEFT.attributes={myDsl_LEFT_amount}

# Relationships
commands0: BinaryAssociation = BinaryAssociation(
    name="commands0",
    ends={
        Property(name="myDsl_CMD", type=myDsl_PROGRAM, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_PROGRAM", type=myDsl_CMD, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_myDsl_PAPER_CMD = Generalization(general=CMD, specific=myDsl_PAPER)
gen_myDsl_TURTLE_CMD = Generalization(general=CMD, specific=myDsl_TURTLE)
gen_myDsl_PENSTATE_CMD = Generalization(general=CMD, specific=myDsl_PENSTATE)
gen_myDsl_PENCOLOUR_CMD = Generalization(general=CMD, specific=myDsl_PENCOLOUR)
gen_myDsl_MOVE_CMD = Generalization(general=CMD, specific=myDsl_MOVE)
gen_myDsl_RIGHT_CMD = Generalization(general=CMD, specific=myDsl_RIGHT)
gen_myDsl_LEFT_CMD = Generalization(general=CMD, specific=myDsl_LEFT)

# Domain Model
domain_model = DomainModel(
    name="myDsl",
    types={myDsl_PROGRAM, myDsl_CMD, myDsl_PAPER, CMD, myDsl_TURTLE, myDsl_PENSTATE, myDsl_PENCOLOUR, myDsl_MOVE, myDsl_RIGHT, myDsl_LEFT},
    associations={commands0},
    generalizations={gen_myDsl_PAPER_CMD, gen_myDsl_TURTLE_CMD, gen_myDsl_PENSTATE_CMD, gen_myDsl_PENCOLOUR_CMD, gen_myDsl_MOVE_CMD, gen_myDsl_RIGHT_CMD, gen_myDsl_LEFT_CMD},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)