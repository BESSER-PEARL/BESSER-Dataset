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
wh_Model = Class(name="wh::Model")
wh_Program = Class(name="wh::Program")
wh_Function = Class(name="wh::Function")
wh_Definition = Class(name="wh::Definition")
wh_Input = Class(name="wh::Input")
wh_Commands = Class(name="wh::Commands")
wh_Output = Class(name="wh::Output")

# wh_Model class attributes and methods

# wh_Program class attributes and methods

# wh_Function class attributes and methods
wh_Function_name: Property = Property(name="name", type=StringType)
wh_Function.attributes={wh_Function_name}

# wh_Definition class attributes and methods

# wh_Input class attributes and methods
wh_Input_variable: Property = Property(name="variable", type=StringType)
wh_Input.attributes={wh_Input_variable}

# wh_Commands class attributes and methods
wh_Commands_command: Property = Property(name="command", type=StringType)
wh_Commands.attributes={wh_Commands_command}

# wh_Output class attributes and methods
wh_Output_variable: Property = Property(name="variable", type=StringType)
wh_Output.attributes={wh_Output_variable}

# Relationships
program0: BinaryAssociation = BinaryAssociation(
    name="program0",
    ends={
        Property(name="wh_Program", type=wh_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_Model", type=wh_Program, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
function1: BinaryAssociation = BinaryAssociation(
    name="function1",
    ends={
        Property(name="wh_Function", type=wh_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_Program2", type=wh_Function, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
program4: BinaryAssociation = BinaryAssociation(
    name="program4",
    ends={
        Property(name="wh_Program5", type=wh_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_Program3", type=wh_Program, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
definition6: BinaryAssociation = BinaryAssociation(
    name="definition6",
    ends={
        Property(name="wh_Definition", type=wh_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_Function7", type=wh_Definition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
input8: BinaryAssociation = BinaryAssociation(
    name="input8",
    ends={
        Property(name="wh_Input", type=wh_Definition, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_Definition9", type=wh_Input, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
commands10: BinaryAssociation = BinaryAssociation(
    name="commands10",
    ends={
        Property(name="wh_Commands", type=wh_Definition, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_Definition11", type=wh_Commands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
output12: BinaryAssociation = BinaryAssociation(
    name="output12",
    ends={
        Property(name="wh_Output", type=wh_Definition, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_Definition13", type=wh_Output, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
input15: BinaryAssociation = BinaryAssociation(
    name="input15",
    ends={
        Property(name="wh_Input16", type=wh_Input, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_Input14", type=wh_Input, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
output18: BinaryAssociation = BinaryAssociation(
    name="output18",
    ends={
        Property(name="wh_Output19", type=wh_Output, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_Output17", type=wh_Output, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
commands21: BinaryAssociation = BinaryAssociation(
    name="commands21",
    ends={
        Property(name="wh_Commands22", type=wh_Commands, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_Commands20", type=wh_Commands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="wh",
    types={wh_Model, wh_Program, wh_Function, wh_Definition, wh_Input, wh_Commands, wh_Output},
    associations={program0, function1, program4, definition6, input8, commands10, output12, input15, output18, commands21},
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