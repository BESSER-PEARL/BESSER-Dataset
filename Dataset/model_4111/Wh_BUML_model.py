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
wh_Input = Class(name="wh::Input")
wh_Commands = Class(name="wh::Commands")
wh_Output = Class(name="wh::Output")
wh_Command = Class(name="wh::Command")
wh_EObject = Class(name="wh::EObject")
wh_Nop = Class(name="wh::Nop")
wh_Affect = Class(name="wh::Affect")
wh_Definition = Class(name="wh::Definition")

# wh_Wh class attributes and methods

# wh_Program class attributes and methods
wh_Program_name: Property = Property(name="name", type=StringType)
wh_Program.attributes={wh_Program_name}

# wh_Input class attributes and methods
wh_Input_vars: Property = Property(name="vars", type=StringType)
wh_Input.attributes={wh_Input_vars}

# wh_Commands class attributes and methods

# wh_Output class attributes and methods
wh_Output_vars: Property = Property(name="vars", type=StringType)
wh_Output.attributes={wh_Output_vars}

# wh_Command class attributes and methods

# wh_EObject class attributes and methods

# wh_Nop class attributes and methods
wh_Nop_nop: Property = Property(name="nop", type=StringType)
wh_Nop.attributes={wh_Nop_nop}

# wh_Affect class attributes and methods
wh_Affect_vars: Property = Property(name="vars", type=StringType)
wh_Affect_exprs: Property = Property(name="exprs", type=StringType)
wh_Affect.attributes={wh_Affect_vars, wh_Affect_exprs}

# wh_Definition class attributes and methods

# Relationships
input3: BinaryAssociation = BinaryAssociation(
    name="input3",
    ends={
        Property(name="wh_Input", type=wh_Definition, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_Definition4", type=wh_Input, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
command5: BinaryAssociation = BinaryAssociation(
    name="command5",
    ends={
        Property(name="wh_Commands", type=wh_Definition, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_Definition6", type=wh_Commands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
output7: BinaryAssociation = BinaryAssociation(
    name="output7",
    ends={
        Property(name="wh_Output", type=wh_Definition, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_Definition8", type=wh_Output, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
commands9: BinaryAssociation = BinaryAssociation(
    name="commands9",
    ends={
        Property(name="wh_Command", type=wh_Commands, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_Commands10", type=wh_Command, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cmd11: BinaryAssociation = BinaryAssociation(
    name="cmd11",
    ends={
        Property(name="wh_EObject", type=wh_Command, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_Command12", type=wh_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
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

# Domain Model
domain_model = DomainModel(
    name="wh",
    types={wh_Wh, wh_Program, wh_Input, wh_Commands, wh_Output, wh_Command, wh_EObject, wh_Nop, wh_Affect, wh_Definition},
    associations={input3, command5, output7, commands9, cmd11, elements0, definition1},
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