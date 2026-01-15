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
Direction: Enumeration = Enumeration(
    name="Direction",
    literals={
            EnumerationLiteral(name="INPUT"),
			EnumerationLiteral(name="OUTPUT")
    }
)

DigitalPinNumber: Enumeration = Enumeration(
    name="DigitalPinNumber",
    literals={
            EnumerationLiteral(name="D0"),
			EnumerationLiteral(name="D1"),
			EnumerationLiteral(name="D2"),
			EnumerationLiteral(name="D4"),
			EnumerationLiteral(name="D5")
    }
)

# Classes
arduino_Project = Class(name="arduino::Project")
arduino_Sketch = Class(name="arduino::Sketch")
arduino_Setup = Class(name="arduino::Setup")
arduino_Loop = Class(name="arduino::Loop")
arduino_Read = Class(name="arduino::Read")
arduino_Pin = Class(name="arduino::Pin", is_abstract=True)
Pin = Class(name="Pin")
arduino_Function = Class(name="arduino::Function", is_abstract=True)
Instruction = Class(name="Instruction")
arduino_Instruction = Class(name="arduino::Instruction", is_abstract=True)
arduino_Write = Class(name="arduino::Write")
Function = Class(name="Function")
arduino_DigitalPin = Class(name="arduino::DigitalPin")

# arduino_Project class attributes and methods
arduino_Project_name: Property = Property(name="name", type=StringType)
arduino_Project.attributes={arduino_Project_name}

# arduino_Sketch class attributes and methods
arduino_Sketch_name: Property = Property(name="name", type=StringType)
arduino_Sketch.attributes={arduino_Sketch_name}

# arduino_Setup class attributes and methods
arduino_Setup_name: Property = Property(name="name", type=StringType)
arduino_Setup.attributes={arduino_Setup_name}

# arduino_Loop class attributes and methods
arduino_Loop_name: Property = Property(name="name", type=StringType)
arduino_Loop.attributes={arduino_Loop_name}

# arduino_Read class attributes and methods
arduino_Read_returnValue: Property = Property(name="returnValue", type=StringType)
arduino_Read_name: Property = Property(name="name", type=StringType)
arduino_Read.attributes={arduino_Read_name, arduino_Read_returnValue}

# arduino_Pin class attributes and methods
arduino_Pin_Direction: Property = Property(name="Direction", type=StringType)
arduino_Pin_name: Property = Property(name="name", type=StringType)
arduino_Pin.attributes={arduino_Pin_Direction, arduino_Pin_name}

# Pin class attributes and methods

# arduino_Function class attributes and methods

# Instruction class attributes and methods

# arduino_Instruction class attributes and methods

# arduino_Write class attributes and methods
arduino_Write_name: Property = Property(name="name", type=StringType)
arduino_Write.attributes={arduino_Write_name}

# Function class attributes and methods

# arduino_DigitalPin class attributes and methods
arduino_DigitalPin_number: Property = Property(name="number", type=StringType)
arduino_DigitalPin.attributes={arduino_DigitalPin_number}

# Relationships
sketch0: BinaryAssociation = BinaryAssociation(
    name="sketch0",
    ends={
        Property(name="arduino_Sketch", type=arduino_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_Project", type=arduino_Sketch, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
setup1: BinaryAssociation = BinaryAssociation(
    name="setup1",
    ends={
        Property(name="arduino_Setup", type=arduino_Sketch, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_Sketch2", type=arduino_Setup, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
loop3: BinaryAssociation = BinaryAssociation(
    name="loop3",
    ends={
        Property(name="arduino_Loop", type=arduino_Sketch, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_Sketch4", type=arduino_Loop, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
digitalpin11: BinaryAssociation = BinaryAssociation(
    name="digitalpin11",
    ends={
        Property(name="arduino_DigitalPin12", type=arduino_Read, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_Read", type=arduino_DigitalPin, multiplicity=Multiplicity(0, 1))
    }
)
digitalpin13: BinaryAssociation = BinaryAssociation(
    name="digitalpin13",
    ends={
        Property(name="arduino_DigitalPin15", type=arduino_Setup, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_Setup14", type=arduino_DigitalPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
instruction16: BinaryAssociation = BinaryAssociation(
    name="instruction16",
    ends={
        Property(name="arduino_Instruction18", type=arduino_Loop, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_Loop17", type=arduino_Instruction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
instruction5: BinaryAssociation = BinaryAssociation(
    name="instruction5",
    ends={
        Property(name="arduino_Instruction", type=arduino_Sketch, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_Sketch6", type=arduino_Instruction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
next8: BinaryAssociation = BinaryAssociation(
    name="next8",
    ends={
        Property(name="arduino_Instruction9", type=arduino_Instruction, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_Instruction7", type=arduino_Instruction, multiplicity=Multiplicity(0, 1))
    }
)
digitalpin10: BinaryAssociation = BinaryAssociation(
    name="digitalpin10",
    ends={
        Property(name="arduino_DigitalPin", type=arduino_Write, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_Write", type=arduino_DigitalPin, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_arduino_Read_Function = Generalization(general=Function, specific=arduino_Read)
gen_arduino_DigitalPin_Pin = Generalization(general=Pin, specific=arduino_DigitalPin)
gen_arduino_Function_Instruction = Generalization(general=Instruction, specific=arduino_Function)
gen_arduino_Write_Function = Generalization(general=Function, specific=arduino_Write)

# Domain Model
domain_model = DomainModel(
    name="arduino",
    types={arduino_Project, arduino_Sketch, arduino_Setup, arduino_Loop, arduino_Read, arduino_Pin, Pin, arduino_Function, Instruction, arduino_Instruction, arduino_Write, Function, arduino_DigitalPin, Direction, DigitalPinNumber},
    associations={sketch0, setup1, loop3, digitalpin11, digitalpin13, instruction16, instruction5, next8, digitalpin10},
    generalizations={gen_arduino_Read_Function, gen_arduino_DigitalPin_Pin, gen_arduino_Function_Instruction, gen_arduino_Write_Function},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)