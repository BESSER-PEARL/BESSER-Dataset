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
RobotWork_Instruction = Class(name="RobotWork::Instruction", is_abstract=True)
RobotWork_Action = Class(name="RobotWork::Action", is_abstract=True)
Instruction = Class(name="Instruction")
RobotWork_Chrography = Class(name="RobotWork::Chrography")
RobotWork_Grab = Class(name="RobotWork::Grab")
Action = Class(name="Action")
RobotWork_Release = Class(name="RobotWork::Release")
RobotWork_Rotate = Class(name="RobotWork::Rotate")
RobotWork_GoForward = Class(name="RobotWork::GoForward")

# RobotWork_Instruction class attributes and methods

# RobotWork_Action class attributes and methods

# Instruction class attributes and methods

# RobotWork_Chrography class attributes and methods
RobotWork_Chrography_name: Property = Property(name="name", type=StringType)
RobotWork_Chrography.attributes={RobotWork_Chrography_name}

# RobotWork_Grab class attributes and methods

# Action class attributes and methods

# RobotWork_Release class attributes and methods

# RobotWork_Rotate class attributes and methods
RobotWork_Rotate_degrees: Property = Property(name="degrees", type=IntegerType)
RobotWork_Rotate_random: Property = Property(name="random", type=BooleanType)
RobotWork_Rotate.attributes={RobotWork_Rotate_random, RobotWork_Rotate_degrees}

# RobotWork_GoForward class attributes and methods
RobotWork_GoForward_cm: Property = Property(name="cm", type=IntegerType)
RobotWork_GoForward.attributes={RobotWork_GoForward_cm}

# Relationships
instructions0: BinaryAssociation = BinaryAssociation(
    name="instructions0",
    ends={
        Property(name="RobotWork_Instruction", type=RobotWork_Chrography, multiplicity=Multiplicity(1, 1)),
        Property(name="RobotWork_Chrography", type=RobotWork_Instruction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_RobotWork_Action_Instruction = Generalization(general=Instruction, specific=RobotWork_Action)
gen_RobotWork_Chrography_Instruction = Generalization(general=Instruction, specific=RobotWork_Chrography)
gen_RobotWork_Grab_Action = Generalization(general=Action, specific=RobotWork_Grab)
gen_RobotWork_Release_Action = Generalization(general=Action, specific=RobotWork_Release)
gen_RobotWork_Rotate_Action = Generalization(general=Action, specific=RobotWork_Rotate)
gen_RobotWork_GoForward_Action = Generalization(general=Action, specific=RobotWork_GoForward)

# Domain Model
domain_model = DomainModel(
    name="RobotWork",
    types={RobotWork_Instruction, RobotWork_Action, Instruction, RobotWork_Chrography, RobotWork_Grab, Action, RobotWork_Release, RobotWork_Rotate, RobotWork_GoForward},
    associations={instructions0},
    generalizations={gen_RobotWork_Action_Instruction, gen_RobotWork_Chrography_Instruction, gen_RobotWork_Grab_Action, gen_RobotWork_Release_Action, gen_RobotWork_Rotate_Action, gen_RobotWork_GoForward_Action},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)