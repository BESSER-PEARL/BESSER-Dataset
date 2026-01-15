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
PinNature: Enumeration = Enumeration(
    name="PinNature",
    literals={
            EnumerationLiteral(name="Digital"),
			EnumerationLiteral(name="Analog"),
			EnumerationLiteral(name="Mixed")
    }
)

SpeedUnit: Enumeration = Enumeration(
    name="SpeedUnit",
    literals={
            EnumerationLiteral(name="Hz"),
			EnumerationLiteral(name="Mhz"),
			EnumerationLiteral(name="GHz"),
			EnumerationLiteral(name="MIPS")
    }
)

MemoryUnit: Enumeration = Enumeration(
    name="MemoryUnit",
    literals={
            EnumerationLiteral(name="Mo"),
			EnumerationLiteral(name="Go"),
			EnumerationLiteral(name="Ko")
    }
)

WordSize: Enumeration = Enumeration(
    name="WordSize",
    literals={
            EnumerationLiteral(name="wd_8bits"),
			EnumerationLiteral(name="wd_16bits"),
			EnumerationLiteral(name="wd_24bits"),
			EnumerationLiteral(name="wd_32bits"),
			EnumerationLiteral(name="wd_48bits"),
			EnumerationLiteral(name="wd_64bits")
    }
)

OperationName: Enumeration = Enumeration(
    name="OperationName",
    literals={
            EnumerationLiteral(name="digitalPinRead"),
			EnumerationLiteral(name="digitalPinWrite"),
			EnumerationLiteral(name="analogPinRead"),
			EnumerationLiteral(name="analogPinWrite"),
			EnumerationLiteral(name="pinConfigMode")
    }
)

TimerOp: Enumeration = Enumeration(
    name="TimerOp",
    literals={
            EnumerationLiteral(name="initializeTimer")
    }
)

RegType: Enumeration = Enumeration(
    name="RegType",
    literals={
            EnumerationLiteral(name="accumulator"),
			EnumerationLiteral(name="general"),
			EnumerationLiteral(name="PCounter"),
			EnumerationLiteral(name="Stack"),
			EnumerationLiteral(name="CCR"),
			EnumerationLiteral(name="ICR"),
			EnumerationLiteral(name="IR")
    }
)

PinModes: Enumeration = Enumeration(
    name="PinModes",
    literals={
            EnumerationLiteral(name="Input"),
			EnumerationLiteral(name="Output")
    }
)

# Classes
MicrocontrollerModeling_Microcontroller = Class(name="MicrocontrollerModeling::Microcontroller")
MicrocontrollerModeling_Pin = Class(name="MicrocontrollerModeling::Pin")
MicrocontrollerModeling_CLanguage = Class(name="MicrocontrollerModeling::CLanguage")
MicrocontrollerModeling_Processor = Class(name="MicrocontrollerModeling::Processor")
MicrocontrollerModeling_ROM = Class(name="MicrocontrollerModeling::ROM")
MicrocontrollerModeling_RAM = Class(name="MicrocontrollerModeling::RAM")
MicrocontrollerModeling_Register = Class(name="MicrocontrollerModeling::Register")
MicrocontrollerModeling_Library = Class(name="MicrocontrollerModeling::Library")
MicrocontrollerModeling_Flash = Class(name="MicrocontrollerModeling::Flash")
MicrocontrollerModeling_PinOperation = Class(name="MicrocontrollerModeling::PinOperation")
MicrocontrollerModeling_Function = Class(name="MicrocontrollerModeling::Function")
MicrocontrollerModeling_Parameter = Class(name="MicrocontrollerModeling::Parameter")
MicrocontrollerModeling_Instruction = Class(name="MicrocontrollerModeling::Instruction")
Function = Class(name="Function")
MicrocontrollerModeling_TimerConfig = Class(name="MicrocontrollerModeling::TimerConfig")
MicrocontrollerModeling_PinMode = Class(name="MicrocontrollerModeling::PinMode")
Memory = Class(name="Memory")
MicrocontrollerModeling_EEPROM = Class(name="MicrocontrollerModeling::EEPROM")
ROM = Class(name="ROM")
EEPROM = Class(name="EEPROM")
MicrocontrollerModeling_Memory = Class(name="MicrocontrollerModeling::Memory", is_abstract=True)

# MicrocontrollerModeling_Microcontroller class attributes and methods
MicrocontrollerModeling_Microcontroller_name: Property = Property(name="name", type=StringType)
MicrocontrollerModeling_Microcontroller_family: Property = Property(name="family", type=StringType)
MicrocontrollerModeling_Microcontroller_manufacturer: Property = Property(name="manufacturer", type=StringType)
MicrocontrollerModeling_Microcontroller_wordMemory: Property = Property(name="wordMemory", type=StringType)
MicrocontrollerModeling_Microcontroller.attributes={MicrocontrollerModeling_Microcontroller_name, MicrocontrollerModeling_Microcontroller_wordMemory, MicrocontrollerModeling_Microcontroller_manufacturer, MicrocontrollerModeling_Microcontroller_family}

# MicrocontrollerModeling_Pin class attributes and methods
MicrocontrollerModeling_Pin_name: Property = Property(name="name", type=StringType)
MicrocontrollerModeling_Pin_nature: Property = Property(name="nature", type=StringType)
MicrocontrollerModeling_Pin_number: Property = Property(name="number", type=IntegerType)
MicrocontrollerModeling_Pin.attributes={MicrocontrollerModeling_Pin_name, MicrocontrollerModeling_Pin_nature, MicrocontrollerModeling_Pin_number}

# MicrocontrollerModeling_CLanguage class attributes and methods
MicrocontrollerModeling_CLanguage_name: Property = Property(name="name", type=StringType)
MicrocontrollerModeling_CLanguage_hasMain: Property = Property(name="hasMain", type=BooleanType)
MicrocontrollerModeling_CLanguage_filesExtension: Property = Property(name="filesExtension", type=StringType)
MicrocontrollerModeling_CLanguage.attributes={MicrocontrollerModeling_CLanguage_hasMain, MicrocontrollerModeling_CLanguage_filesExtension, MicrocontrollerModeling_CLanguage_name}

# MicrocontrollerModeling_Processor class attributes and methods
MicrocontrollerModeling_Processor_unit: Property = Property(name="unit", type=StringType)
MicrocontrollerModeling_Processor_speed: Property = Property(name="speed", type=IntegerType)
MicrocontrollerModeling_Processor.attributes={MicrocontrollerModeling_Processor_speed, MicrocontrollerModeling_Processor_unit}

# MicrocontrollerModeling_ROM class attributes and methods

# MicrocontrollerModeling_RAM class attributes and methods

# MicrocontrollerModeling_Register class attributes and methods
MicrocontrollerModeling_Register_name: Property = Property(name="name", type=StringType)
MicrocontrollerModeling_Register_type: Property = Property(name="type", type=StringType)
MicrocontrollerModeling_Register.attributes={MicrocontrollerModeling_Register_type, MicrocontrollerModeling_Register_name}

# MicrocontrollerModeling_Library class attributes and methods
MicrocontrollerModeling_Library_name: Property = Property(name="name", type=StringType)
MicrocontrollerModeling_Library.attributes={MicrocontrollerModeling_Library_name}

# MicrocontrollerModeling_Flash class attributes and methods

# MicrocontrollerModeling_PinOperation class attributes and methods
MicrocontrollerModeling_PinOperation_name: Property = Property(name="name", type=StringType)
MicrocontrollerModeling_PinOperation.attributes={MicrocontrollerModeling_PinOperation_name}

# MicrocontrollerModeling_Function class attributes and methods
MicrocontrollerModeling_Function_type: Property = Property(name="type", type=StringType)
MicrocontrollerModeling_Function.attributes={MicrocontrollerModeling_Function_type}

# MicrocontrollerModeling_Parameter class attributes and methods
MicrocontrollerModeling_Parameter_name: Property = Property(name="name", type=StringType)
MicrocontrollerModeling_Parameter_type: Property = Property(name="type", type=StringType)
MicrocontrollerModeling_Parameter.attributes={MicrocontrollerModeling_Parameter_name, MicrocontrollerModeling_Parameter_type}

# MicrocontrollerModeling_Instruction class attributes and methods
MicrocontrollerModeling_Instruction_value: Property = Property(name="value", type=StringType)
MicrocontrollerModeling_Instruction.attributes={MicrocontrollerModeling_Instruction_value}

# Function class attributes and methods

# MicrocontrollerModeling_TimerConfig class attributes and methods
MicrocontrollerModeling_TimerConfig_name: Property = Property(name="name", type=StringType)
MicrocontrollerModeling_TimerConfig_period: Property = Property(name="period", type=IntegerType)
MicrocontrollerModeling_TimerConfig.attributes={MicrocontrollerModeling_TimerConfig_period, MicrocontrollerModeling_TimerConfig_name}

# MicrocontrollerModeling_PinMode class attributes and methods
MicrocontrollerModeling_PinMode_name: Property = Property(name="name", type=StringType)
MicrocontrollerModeling_PinMode_value: Property = Property(name="value", type=StringType)
MicrocontrollerModeling_PinMode.attributes={MicrocontrollerModeling_PinMode_name, MicrocontrollerModeling_PinMode_value}

# Memory class attributes and methods

# MicrocontrollerModeling_EEPROM class attributes and methods

# ROM class attributes and methods

# EEPROM class attributes and methods

# MicrocontrollerModeling_Memory class attributes and methods
MicrocontrollerModeling_Memory_unit: Property = Property(name="unit", type=StringType)
MicrocontrollerModeling_Memory_size: Property = Property(name="size", type=IntegerType)
MicrocontrollerModeling_Memory.attributes={MicrocontrollerModeling_Memory_size, MicrocontrollerModeling_Memory_unit}

# Relationships
pins0: BinaryAssociation = BinaryAssociation(
    name="pins0",
    ends={
        Property(name="MicrocontrollerModeling_Pin", type=MicrocontrollerModeling_Microcontroller, multiplicity=Multiplicity(1, 1)),
        Property(name="MicrocontrollerModeling_Microcontroller", type=MicrocontrollerModeling_Pin, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
clanguage1: BinaryAssociation = BinaryAssociation(
    name="clanguage1",
    ends={
        Property(name="MicrocontrollerModeling_CLanguage", type=MicrocontrollerModeling_Microcontroller, multiplicity=Multiplicity(1, 1)),
        Property(name="MicrocontrollerModeling_Microcontroller2", type=MicrocontrollerModeling_CLanguage, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
processor3: BinaryAssociation = BinaryAssociation(
    name="processor3",
    ends={
        Property(name="MicrocontrollerModeling_Processor", type=MicrocontrollerModeling_Microcontroller, multiplicity=Multiplicity(1, 1)),
        Property(name="MicrocontrollerModeling_Microcontroller4", type=MicrocontrollerModeling_Processor, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
rom5: BinaryAssociation = BinaryAssociation(
    name="rom5",
    ends={
        Property(name="MicrocontrollerModeling_ROM", type=MicrocontrollerModeling_Microcontroller, multiplicity=Multiplicity(1, 1)),
        Property(name="MicrocontrollerModeling_Microcontroller6", type=MicrocontrollerModeling_ROM, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ram9: BinaryAssociation = BinaryAssociation(
    name="ram9",
    ends={
        Property(name="MicrocontrollerModeling_RAM", type=MicrocontrollerModeling_Microcontroller, multiplicity=Multiplicity(1, 1)),
        Property(name="MicrocontrollerModeling_Microcontroller10", type=MicrocontrollerModeling_RAM, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
registers11: BinaryAssociation = BinaryAssociation(
    name="registers11",
    ends={
        Property(name="MicrocontrollerModeling_Register", type=MicrocontrollerModeling_Microcontroller, multiplicity=Multiplicity(1, 1)),
        Property(name="MicrocontrollerModeling_Microcontroller12", type=MicrocontrollerModeling_Register, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pinmodes17: BinaryAssociation = BinaryAssociation(
    name="pinmodes17",
    ends={
        Property(name="MicrocontrollerModeling_PinMode", type=MicrocontrollerModeling_CLanguage, multiplicity=Multiplicity(1, 1)),
        Property(name="MicrocontrollerModeling_CLanguage18", type=MicrocontrollerModeling_PinMode, multiplicity=Multiplicity(1, 2), is_composite=True)
    }
)
flash7: BinaryAssociation = BinaryAssociation(
    name="flash7",
    ends={
        Property(name="MicrocontrollerModeling_Flash", type=MicrocontrollerModeling_Microcontroller, multiplicity=Multiplicity(1, 1)),
        Property(name="MicrocontrollerModeling_Microcontroller8", type=MicrocontrollerModeling_Flash, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pinoperation19: BinaryAssociation = BinaryAssociation(
    name="pinoperation19",
    ends={
        Property(name="MicrocontrollerModeling_PinOperation", type=MicrocontrollerModeling_CLanguage, multiplicity=Multiplicity(1, 1)),
        Property(name="MicrocontrollerModeling_CLanguage20", type=MicrocontrollerModeling_PinOperation, multiplicity=Multiplicity(1, 5), is_composite=True)
    }
)
parameters21: BinaryAssociation = BinaryAssociation(
    name="parameters21",
    ends={
        Property(name="MicrocontrollerModeling_Parameter", type=MicrocontrollerModeling_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="MicrocontrollerModeling_Function", type=MicrocontrollerModeling_Parameter, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
instructions22: BinaryAssociation = BinaryAssociation(
    name="instructions22",
    ends={
        Property(name="MicrocontrollerModeling_Instruction", type=MicrocontrollerModeling_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="MicrocontrollerModeling_Function23", type=MicrocontrollerModeling_Instruction, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
libraries13: BinaryAssociation = BinaryAssociation(
    name="libraries13",
    ends={
        Property(name="MicrocontrollerModeling_Library", type=MicrocontrollerModeling_CLanguage, multiplicity=Multiplicity(1, 1)),
        Property(name="MicrocontrollerModeling_CLanguage14", type=MicrocontrollerModeling_Library, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
timerconfig15: BinaryAssociation = BinaryAssociation(
    name="timerconfig15",
    ends={
        Property(name="MicrocontrollerModeling_TimerConfig", type=MicrocontrollerModeling_CLanguage, multiplicity=Multiplicity(1, 1)),
        Property(name="MicrocontrollerModeling_CLanguage16", type=MicrocontrollerModeling_TimerConfig, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_MicrocontrollerModeling_TimerConfig_Function = Generalization(general=Function, specific=MicrocontrollerModeling_TimerConfig)
gen_MicrocontrollerModeling_ROM_Memory = Generalization(general=Memory, specific=MicrocontrollerModeling_ROM)
gen_MicrocontrollerModeling_EEPROM_ROM = Generalization(general=ROM, specific=MicrocontrollerModeling_EEPROM)
gen_MicrocontrollerModeling_Flash_EEPROM = Generalization(general=EEPROM, specific=MicrocontrollerModeling_Flash)
gen_MicrocontrollerModeling_PinOperation_Function = Generalization(general=Function, specific=MicrocontrollerModeling_PinOperation)
gen_MicrocontrollerModeling_RAM_Memory = Generalization(general=Memory, specific=MicrocontrollerModeling_RAM)

# Domain Model
domain_model = DomainModel(
    name="MicrocontrollerModeling",
    types={MicrocontrollerModeling_Microcontroller, MicrocontrollerModeling_Pin, MicrocontrollerModeling_CLanguage, MicrocontrollerModeling_Processor, MicrocontrollerModeling_ROM, MicrocontrollerModeling_RAM, MicrocontrollerModeling_Register, MicrocontrollerModeling_Library, MicrocontrollerModeling_Flash, MicrocontrollerModeling_PinOperation, MicrocontrollerModeling_Function, MicrocontrollerModeling_Parameter, MicrocontrollerModeling_Instruction, Function, MicrocontrollerModeling_TimerConfig, MicrocontrollerModeling_PinMode, Memory, MicrocontrollerModeling_EEPROM, ROM, EEPROM, MicrocontrollerModeling_Memory, PinNature, SpeedUnit, MemoryUnit, WordSize, OperationName, TimerOp, RegType, PinModes},
    associations={pins0, clanguage1, processor3, rom5, ram9, registers11, pinmodes17, flash7, pinoperation19, parameters21, instructions22, libraries13, timerconfig15},
    generalizations={gen_MicrocontrollerModeling_TimerConfig_Function, gen_MicrocontrollerModeling_ROM_Memory, gen_MicrocontrollerModeling_EEPROM_ROM, gen_MicrocontrollerModeling_Flash_EEPROM, gen_MicrocontrollerModeling_PinOperation_Function, gen_MicrocontrollerModeling_RAM_Memory},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)