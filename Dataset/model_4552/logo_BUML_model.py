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
logo_ProgramUnit = Class(name="logo::ProgramUnit")
logo_Command = Class(name="logo::Command", is_abstract=True)
logo_Turn = Class(name="logo::Turn")
logo_WhileNoObstacle = Class(name="logo::WhileNoObstacle")
logo_Move = Class(name="logo::Move")
Command = Class(name="Command")

# logo_ProgramUnit class attributes and methods

# logo_Command class attributes and methods

# logo_Turn class attributes and methods
logo_Turn_angle: Property = Property(name="angle", type=FloatType)
logo_Turn.attributes={logo_Turn_angle}

# logo_WhileNoObstacle class attributes and methods
logo_WhileNoObstacle_distance: Property = Property(name="distance", type=FloatType)
logo_WhileNoObstacle.attributes={logo_WhileNoObstacle_distance}

# logo_Move class attributes and methods
logo_Move_distance: Property = Property(name="distance", type=FloatType)
logo_Move.attributes={logo_Move_distance}

# Command class attributes and methods

# Relationships
commands0: BinaryAssociation = BinaryAssociation(
    name="commands0",
    ends={
        Property(name="logo_Command", type=logo_ProgramUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="logo_ProgramUnit", type=logo_Command, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
commands1: BinaryAssociation = BinaryAssociation(
    name="commands1",
    ends={
        Property(name="logo_Command2", type=logo_WhileNoObstacle, multiplicity=Multiplicity(1, 1)),
        Property(name="logo_WhileNoObstacle", type=logo_Command, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_logo_Move_Command = Generalization(general=Command, specific=logo_Move)
gen_logo_Turn_Command = Generalization(general=Command, specific=logo_Turn)
gen_logo_WhileNoObstacle_Command = Generalization(general=Command, specific=logo_WhileNoObstacle)

# Domain Model
domain_model = DomainModel(
    name="logo",
    types={logo_ProgramUnit, logo_Command, logo_Turn, logo_WhileNoObstacle, logo_Move, Command},
    associations={commands0, commands1},
    generalizations={gen_logo_Move_Command, gen_logo_Turn_Command, gen_logo_WhileNoObstacle_Command},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)