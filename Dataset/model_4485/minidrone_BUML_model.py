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

# Enumerations
JumpType: Enumeration = Enumeration(
    name="JumpType",
    literals={
            EnumerationLiteral(name="JUMP_LONG"),
			EnumerationLiteral(name="JUMP_HIGH"),
			EnumerationLiteral(name="JUMP_MAX")
    }
)

# Classes
minidrone_MiniDroneProgram = Class(name="minidrone::MiniDroneProgram")
minidrone_Instruction = Class(name="minidrone::Instruction", is_abstract=True)
minidrone_Go = Class(name="minidrone::Go")
Instruction = Class(name="Instruction")
minidrone_Turn = Class(name="minidrone::Turn")
minidrone_Jump = Class(name="minidrone::Jump")

# minidrone_MiniDroneProgram class attributes and methods
minidrone_MiniDroneProgram_name: Property = Property(name="name", type=StringType)
minidrone_MiniDroneProgram.attributes={minidrone_MiniDroneProgram_name}

# minidrone_Instruction class attributes and methods

# minidrone_Go class attributes and methods
minidrone_Go_distance: Property = Property(name="distance", type=IntegerType)
minidrone_Go.attributes={minidrone_Go_distance}

# Instruction class attributes and methods

# minidrone_Turn class attributes and methods
minidrone_Turn_angle: Property = Property(name="angle", type=IntegerType)
minidrone_Turn.attributes={minidrone_Turn_angle}

# minidrone_Jump class attributes and methods
minidrone_Jump_jumpType: Property = Property(name="jumpType", type=StringType)
minidrone_Jump.attributes={minidrone_Jump_jumpType}

# Relationships
instructions0: BinaryAssociation = BinaryAssociation(
    name="instructions0",
    ends={
        Property(name="minidrone_Instruction", type=minidrone_MiniDroneProgram, multiplicity=Multiplicity(1, 1)),
        Property(name="minidrone_MiniDroneProgram", type=minidrone_Instruction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_minidrone_Go_Instruction = Generalization(general=Instruction, specific=minidrone_Go)
gen_minidrone_Turn_Instruction = Generalization(general=Instruction, specific=minidrone_Turn)
gen_minidrone_Jump_Instruction = Generalization(general=Instruction, specific=minidrone_Jump)

# Domain Model
domain_model = DomainModel(
    name="minidrone",
    types={minidrone_MiniDroneProgram, minidrone_Instruction, minidrone_Go, Instruction, minidrone_Turn, minidrone_Jump, JumpType},
    associations={instructions0},
    generalizations={gen_minidrone_Go_Instruction, gen_minidrone_Turn_Instruction, gen_minidrone_Jump_Instruction},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)