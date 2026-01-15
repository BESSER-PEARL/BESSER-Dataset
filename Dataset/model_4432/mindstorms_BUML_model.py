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
mindstorms_Choreography = Class(name="mindstorms::Choreography")
Instruction = Class(name="Instruction")
mindstorms_Action = Class(name="mindstorms::Action", is_abstract=True)
mindstorms_Grab = Class(name="mindstorms::Grab")
Action = Class(name="Action")
mindstorms_Release = Class(name="mindstorms::Release")
mindstorms_Rotate = Class(name="mindstorms::Rotate")
mindstorms_GoForward = Class(name="mindstorms::GoForward")
mindstorms_Instruction = Class(name="mindstorms::Instruction", is_abstract=True)

# mindstorms_Choreography class attributes and methods
mindstorms_Choreography_name: Property = Property(name="name", type=StringType)
mindstorms_Choreography.attributes={mindstorms_Choreography_name}

# Instruction class attributes and methods

# mindstorms_Action class attributes and methods

# mindstorms_Grab class attributes and methods

# Action class attributes and methods

# mindstorms_Release class attributes and methods

# mindstorms_Rotate class attributes and methods
mindstorms_Rotate_degrees: Property = Property(name="degrees", type=IntegerType)
mindstorms_Rotate_random: Property = Property(name="random", type=BooleanType)
mindstorms_Rotate.attributes={mindstorms_Rotate_degrees, mindstorms_Rotate_random}

# mindstorms_GoForward class attributes and methods
mindstorms_GoForward_cm: Property = Property(name="cm", type=IntegerType)
mindstorms_GoForward.attributes={mindstorms_GoForward_cm}

# mindstorms_Instruction class attributes and methods

# Relationships
instructions0: BinaryAssociation = BinaryAssociation(
    name="instructions0",
    ends={
        Property(name="mindstorms_Instruction", type=mindstorms_Choreography, multiplicity=Multiplicity(1, 1)),
        Property(name="mindstorms_Choreography", type=mindstorms_Instruction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_mindstorms_Choreography_Instruction = Generalization(general=Instruction, specific=mindstorms_Choreography)
gen_mindstorms_Action_Instruction = Generalization(general=Instruction, specific=mindstorms_Action)
gen_mindstorms_Grab_Action = Generalization(general=Action, specific=mindstorms_Grab)
gen_mindstorms_Release_Action = Generalization(general=Action, specific=mindstorms_Release)
gen_mindstorms_Rotate_Action = Generalization(general=Action, specific=mindstorms_Rotate)
gen_mindstorms_GoForward_Action = Generalization(general=Action, specific=mindstorms_GoForward)

# Domain Model
domain_model = DomainModel(
    name="mindstorms",
    types={mindstorms_Choreography, Instruction, mindstorms_Action, mindstorms_Grab, Action, mindstorms_Release, mindstorms_Rotate, mindstorms_GoForward, mindstorms_Instruction},
    associations={instructions0},
    generalizations={gen_mindstorms_Choreography_Instruction, gen_mindstorms_Action_Instruction, gen_mindstorms_Grab_Action, gen_mindstorms_Release_Action, gen_mindstorms_Rotate_Action, gen_mindstorms_GoForward_Action},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)