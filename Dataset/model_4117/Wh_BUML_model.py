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
wh_Wh = Class(name="wh::Wh")
wh_Program = Class(name="wh::Program")
wh_Definition = Class(name="wh::Definition")
wh_Commands = Class(name="wh::Commands")
wh_Command = Class(name="wh::Command")

# wh_Wh class attributes and methods

# wh_Program class attributes and methods
wh_Program_name: Property = Property(name="name", type=StringType)
wh_Program.attributes={wh_Program_name}

# wh_Definition class attributes and methods
wh_Definition_input: Property = Property(name="input", type=StringType)
wh_Definition_output: Property = Property(name="output", type=StringType)
wh_Definition.attributes={wh_Definition_output, wh_Definition_input}

# wh_Commands class attributes and methods

# wh_Command class attributes and methods
wh_Command_cmd: Property = Property(name="cmd", type=StringType)
wh_Command.attributes={wh_Command_cmd}

# Relationships
elements0: BinaryAssociation = BinaryAssociation(
    name="elements0",
    ends={
        Property(name="wh_Program", type=wh_Wh, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_Wh", type=wh_Program, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
definition1: BinaryAssociation = BinaryAssociation(
    name="definition1",
    ends={
        Property(name="wh_Definition", type=wh_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_Program2", type=wh_Definition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
command3: BinaryAssociation = BinaryAssociation(
    name="command3",
    ends={
        Property(name="wh_Commands", type=wh_Definition, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_Definition4", type=wh_Commands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
commands5: BinaryAssociation = BinaryAssociation(
    name="commands5",
    ends={
        Property(name="wh_Command", type=wh_Commands, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_Commands6", type=wh_Command, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="wh",
    types={wh_Wh, wh_Program, wh_Definition, wh_Commands, wh_Command},
    associations={elements0, definition1, command3, commands5},
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