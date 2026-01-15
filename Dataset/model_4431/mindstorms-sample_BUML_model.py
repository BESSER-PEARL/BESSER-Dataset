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
mindstorms_Instruction = Class(name="mindstorms::Instruction", is_abstract=True)
NamedElement = Class(name="NamedElement")
mindstorms_Begin = Class(name="mindstorms::Begin")
mindstorms_Rotate = Class(name="mindstorms::Rotate")
mindstorms_Release = Class(name="mindstorms::Release")
mindstorms_Action = Class(name="mindstorms::Action", is_abstract=True)
Block = Class(name="Block")
mindstorms_Block = Class(name="mindstorms::Block", is_abstract=True)
Instruction = Class(name="Instruction")
mindstorms_End = Class(name="mindstorms::End")
mindstorms_Choreography = Class(name="mindstorms::Choreography")
mindstorms_NamedElement = Class(name="mindstorms::NamedElement", is_abstract=True)
mindstorms_GoForward = Class(name="mindstorms::GoForward")
Action = Class(name="Action")
mindstorms_GoBackward = Class(name="mindstorms::GoBackward")
mindstorms_EdgeInstruction = Class(name="mindstorms::EdgeInstruction")
mindstorms_Grab = Class(name="mindstorms::Grab")

# mindstorms_Instruction class attributes and methods

# NamedElement class attributes and methods

# mindstorms_Begin class attributes and methods

# mindstorms_Rotate class attributes and methods
mindstorms_Rotate_degrees: Property = Property(name="degrees", type=IntegerType)
mindstorms_Rotate_random: Property = Property(name="random", type=BooleanType)
mindstorms_Rotate.attributes={mindstorms_Rotate_degrees, mindstorms_Rotate_random}

# mindstorms_Release class attributes and methods

# mindstorms_Action class attributes and methods

# Block class attributes and methods

# mindstorms_Block class attributes and methods

# Instruction class attributes and methods

# mindstorms_End class attributes and methods

# mindstorms_Choreography class attributes and methods

# mindstorms_NamedElement class attributes and methods
mindstorms_NamedElement_name: Property = Property(name="name", type=StringType)
mindstorms_NamedElement.attributes={mindstorms_NamedElement_name}

# mindstorms_GoForward class attributes and methods
mindstorms_GoForward_cm: Property = Property(name="cm", type=IntegerType)
mindstorms_GoForward_infinite: Property = Property(name="infinite", type=BooleanType)
mindstorms_GoForward.attributes={mindstorms_GoForward_infinite, mindstorms_GoForward_cm}

# Action class attributes and methods

# mindstorms_GoBackward class attributes and methods
mindstorms_GoBackward_infinite: Property = Property(name="infinite", type=BooleanType)
mindstorms_GoBackward_cm: Property = Property(name="cm", type=IntegerType)
mindstorms_GoBackward.attributes={mindstorms_GoBackward_infinite, mindstorms_GoBackward_cm}

# mindstorms_EdgeInstruction class attributes and methods

# mindstorms_Grab class attributes and methods

# Relationships
instructions0: BinaryAssociation = BinaryAssociation(
    name="instructions0",
    ends={
        Property(name="mindstorms_Instruction", type=mindstorms_Choreography, multiplicity=Multiplicity(1, 1)),
        Property(name="mindstorms_Choreography", type=mindstorms_Instruction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edgeInstructions1: BinaryAssociation = BinaryAssociation(
    name="edgeInstructions1",
    ends={
        Property(name="mindstorms_EdgeInstruction", type=mindstorms_Choreography, multiplicity=Multiplicity(1, 1)),
        Property(name="mindstorms_Choreography2", type=mindstorms_EdgeInstruction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source3: BinaryAssociation = BinaryAssociation(
    name="source3",
    ends={
        Property(name="mindstorms_Instruction5", type=mindstorms_EdgeInstruction, multiplicity=Multiplicity(1, 1)),
        Property(name="mindstorms_EdgeInstruction4", type=mindstorms_Instruction, multiplicity=Multiplicity(0, 1))
    }
)
target6: BinaryAssociation = BinaryAssociation(
    name="target6",
    ends={
        Property(name="mindstorms_Instruction8", type=mindstorms_EdgeInstruction, multiplicity=Multiplicity(1, 1)),
        Property(name="mindstorms_EdgeInstruction7", type=mindstorms_Instruction, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_mindstorms_Begin_Action = Generalization(general=Action, specific=mindstorms_Begin)
gen_mindstorms_Rotate_Action = Generalization(general=Action, specific=mindstorms_Rotate)
gen_mindstorms_Release_Action = Generalization(general=Action, specific=mindstorms_Release)
gen_mindstorms_Action_Block = Generalization(general=Block, specific=mindstorms_Action)
gen_mindstorms_Block_Instruction = Generalization(general=Instruction, specific=mindstorms_Block)
gen_mindstorms_End_Action = Generalization(general=Action, specific=mindstorms_End)
gen_mindstorms_Choreography_Instruction = Generalization(general=Instruction, specific=mindstorms_Choreography)
gen_mindstorms_Instruction_NamedElement = Generalization(general=NamedElement, specific=mindstorms_Instruction)
gen_mindstorms_GoForward_Action = Generalization(general=Action, specific=mindstorms_GoForward)
gen_mindstorms_GoBackward_Action = Generalization(general=Action, specific=mindstorms_GoBackward)
gen_mindstorms_Grab_Action = Generalization(general=Action, specific=mindstorms_Grab)

# Domain Model
domain_model = DomainModel(
    name="mindstorms",
    types={mindstorms_Instruction, NamedElement, mindstorms_Begin, mindstorms_Rotate, mindstorms_Release, mindstorms_Action, Block, mindstorms_Block, Instruction, mindstorms_End, mindstorms_Choreography, mindstorms_NamedElement, mindstorms_GoForward, Action, mindstorms_GoBackward, mindstorms_EdgeInstruction, mindstorms_Grab},
    associations={instructions0, edgeInstructions1, source3, target6},
    generalizations={gen_mindstorms_Begin_Action, gen_mindstorms_Rotate_Action, gen_mindstorms_Release_Action, gen_mindstorms_Action_Block, gen_mindstorms_Block_Instruction, gen_mindstorms_End_Action, gen_mindstorms_Choreography_Instruction, gen_mindstorms_Instruction_NamedElement, gen_mindstorms_GoForward_Action, gen_mindstorms_GoBackward_Action, gen_mindstorms_Grab_Action},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)