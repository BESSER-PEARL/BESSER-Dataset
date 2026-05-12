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
Interpreter_ByteCode_ByteCode = Class(name="Interpreter_ByteCode_ByteCode")
Interpreter_ByteCode_Args = Class(name="Interpreter_ByteCode_Args")
Interpreter_ByteCode_BOP = Class(name="Interpreter_ByteCode_BOP")
Interpreter_ByteCode_Call = Class(name="Interpreter_ByteCode_Call")
Interpreter_ByteCode_Dump = Class(name="Interpreter_ByteCode_Dump")
Interpreter_ByteCode_FalseBranch = Class(name="Interpreter_ByteCode_FalseBranch")
Interpreter_ByteCode_GoTo = Class(name="Interpreter_ByteCode_GoTo")
Interpreter_ByteCode_Halt = Class(name="Interpreter_ByteCode_Halt")
Interpreter_ByteCode_Label = Class(name="Interpreter_ByteCode_Label")
Interpreter_ByteCode_Lit = Class(name="Interpreter_ByteCode_Lit")
Interpreter_ByteCode_Load = Class(name="Interpreter_ByteCode_Load")
Interpreter_ByteCode_Pop = Class(name="Interpreter_ByteCode_Pop")
Interpreter_ByteCode_Read = Class(name="Interpreter_ByteCode_Read")
Interpreter_ByteCode_Return = Class(name="Interpreter_ByteCode_Return")
Interpreter_ByteCode_Store = Class(name="Interpreter_ByteCode_Store")
Interpreter_ByteCode_Write = Class(name="Interpreter_ByteCode_Write")
Interpreter_ByteCodeLoader = Class(name="Interpreter_ByteCodeLoader")

# Interpreter_ByteCode_ByteCode class attributes and methods

# Interpreter_ByteCode_Args class attributes and methods
Interpreter_ByteCode_Args_nArgs: Property = Property(name="nArgs", type=IntegerType)
Interpreter_ByteCode_Args.attributes={Interpreter_ByteCode_Args_nArgs}

# Interpreter_ByteCode_BOP class attributes and methods
Interpreter_ByteCode_BOP_binaryOp: Property = Property(name="binaryOp", type=StringType)
Interpreter_ByteCode_BOP.attributes={Interpreter_ByteCode_BOP_binaryOp}

# Interpreter_ByteCode_Call class attributes and methods
Interpreter_ByteCode_Call_funcname: Property = Property(name="funcname", type=StringType)
Interpreter_ByteCode_Call_address: Property = Property(name="address", type=IntegerType)
Interpreter_ByteCode_Call.attributes={Interpreter_ByteCode_Call_address, Interpreter_ByteCode_Call_funcname}

# Interpreter_ByteCode_Dump class attributes and methods
Interpreter_ByteCode_Dump_stats: Property = Property(name="stats", type=StringType)
Interpreter_ByteCode_Dump.attributes={Interpreter_ByteCode_Dump_stats}

# Interpreter_ByteCode_FalseBranch class attributes and methods
Interpreter_ByteCode_FalseBranch_address: Property = Property(name="address", type=IntegerType)
Interpreter_ByteCode_FalseBranch_label: Property = Property(name="label", type=StringType)
Interpreter_ByteCode_FalseBranch.attributes={Interpreter_ByteCode_FalseBranch_label, Interpreter_ByteCode_FalseBranch_address}

# Interpreter_ByteCode_GoTo class attributes and methods
Interpreter_ByteCode_GoTo_address: Property = Property(name="address", type=IntegerType)
Interpreter_ByteCode_GoTo_label: Property = Property(name="label", type=StringType)
Interpreter_ByteCode_GoTo.attributes={Interpreter_ByteCode_GoTo_label, Interpreter_ByteCode_GoTo_address}

# Interpreter_ByteCode_Halt class attributes and methods

# Interpreter_ByteCode_Label class attributes and methods
Interpreter_ByteCode_Label_label: Property = Property(name="label", type=StringType)
Interpreter_ByteCode_Label.attributes={Interpreter_ByteCode_Label_label}

# Interpreter_ByteCode_Lit class attributes and methods
Interpreter_ByteCode_Lit_var: Property = Property(name="var", type=StringType)
Interpreter_ByteCode_Lit_value: Property = Property(name="value", type=IntegerType)
Interpreter_ByteCode_Lit.attributes={Interpreter_ByteCode_Lit_value, Interpreter_ByteCode_Lit_var}

# Interpreter_ByteCode_Load class attributes and methods
Interpreter_ByteCode_Load_id: Property = Property(name="id", type=StringType)
Interpreter_ByteCode_Load_offset: Property = Property(name="offset", type=IntegerType)
Interpreter_ByteCode_Load.attributes={Interpreter_ByteCode_Load_offset, Interpreter_ByteCode_Load_id}

# Interpreter_ByteCode_Pop class attributes and methods
Interpreter_ByteCode_Pop_count: Property = Property(name="count", type=IntegerType)
Interpreter_ByteCode_Pop.attributes={Interpreter_ByteCode_Pop_count}

# Interpreter_ByteCode_Read class attributes and methods

# Interpreter_ByteCode_Return class attributes and methods
Interpreter_ByteCode_Return_funcname: Property = Property(name="funcname", type=StringType)
Interpreter_ByteCode_Return.attributes={Interpreter_ByteCode_Return_funcname}

# Interpreter_ByteCode_Store class attributes and methods
Interpreter_ByteCode_Store_id: Property = Property(name="id", type=StringType)
Interpreter_ByteCode_Store_offset: Property = Property(name="offset", type=IntegerType)
Interpreter_ByteCode_Store_value: Property = Property(name="value", type=IntegerType)
Interpreter_ByteCode_Store.attributes={Interpreter_ByteCode_Store_value, Interpreter_ByteCode_Store_id, Interpreter_ByteCode_Store_offset}

# Interpreter_ByteCode_Write class attributes and methods

# Interpreter_ByteCodeLoader class attributes and methods
Interpreter_ByteCodeLoader_byteSource: Property = Property(name="byteSource", type=StringType)
Interpreter_ByteCodeLoader_program: Property = Property(name="program", type=StringType)
Interpreter_ByteCodeLoader_byteCodeList: Property = Property(name="byteCodeList", type=StringType)
Interpreter_ByteCodeLoader.attributes={Interpreter_ByteCodeLoader_byteCodeList, Interpreter_ByteCodeLoader_program, Interpreter_ByteCodeLoader_byteSource}

# Domain Model
domain_model = DomainModel(
    name="_UeZYwHvzEeiF6cTK02sxJA",
    types={Interpreter_ByteCode_ByteCode, Interpreter_ByteCode_Args, Interpreter_ByteCode_BOP, Interpreter_ByteCode_Call, Interpreter_ByteCode_Dump, Interpreter_ByteCode_FalseBranch, Interpreter_ByteCode_GoTo, Interpreter_ByteCode_Halt, Interpreter_ByteCode_Label, Interpreter_ByteCode_Lit, Interpreter_ByteCode_Load, Interpreter_ByteCode_Pop, Interpreter_ByteCode_Read, Interpreter_ByteCode_Return, Interpreter_ByteCode_Store, Interpreter_ByteCode_Write, Interpreter_ByteCodeLoader},
    associations={},
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