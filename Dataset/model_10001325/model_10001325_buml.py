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
bytecode_ArgsByteCode = Class(name="bytecode_ArgsByteCode")
bytecode_BopByteCode = Class(name="bytecode_BopByteCode")
bytecode_ByteCode = Class(name="bytecode_ByteCode", is_abstract=True)
bytecode_CallByteCode = Class(name="bytecode_CallByteCode")
bytecode_DumpByteCode = Class(name="bytecode_DumpByteCode")
bytecode_FalseBranchByteCode = Class(name="bytecode_FalseBranchByteCode")
bytecode_GoToByteCode = Class(name="bytecode_GoToByteCode")
bytecode_HaltByteCode = Class(name="bytecode_HaltByteCode")
bytecode_LabelByteCode = Class(name="bytecode_LabelByteCode")
bytecode_LitByteCode = Class(name="bytecode_LitByteCode")
bytecode_LoadByteCode = Class(name="bytecode_LoadByteCode")
bytecode_PopByteCode = Class(name="bytecode_PopByteCode")
bytecode_ReadByteCode = Class(name="bytecode_ReadByteCode")
bytecode_ReturnByteCode = Class(name="bytecode_ReturnByteCode")
bytecode_StoreByteCode = Class(name="bytecode_StoreByteCode")
bytecode_WriteByteCode = Class(name="bytecode_WriteByteCode")
interpreter_ByteCodeLoader = Class(name="interpreter_ByteCodeLoader")
interpreter_CodeTable = Class(name="interpreter_CodeTable")
interpreter_Interpreter = Class(name="interpreter_Interpreter")
interpreter_Program = Class(name="interpreter_Program")
interpreter_RunTimeStack = Class(name="interpreter_RunTimeStack")
interpreter_VirtualMachine = Class(name="interpreter_VirtualMachine")
genmymodelreverse_java_util_Scanner = Class(name="genmymodelreverse_java_util_Scanner")
genmymodelreverse_java_io_IOException = Class(name="genmymodelreverse_java_io_IOException")
genmymodelreverse_java_util_HashMap = Class(name="genmymodelreverse_java_util_HashMap")
genmymodelreverse_C1 = Class(name="genmymodelreverse_C1")
genmymodelreverse_C2 = Class(name="genmymodelreverse_C2")
genmymodelreverse_java_util_Vector = Class(name="genmymodelreverse_java_util_Vector")
genmymodelreverse_C11 = Class(name="genmymodelreverse_C11")
genmymodelreverse_java_util_Map_Interface = Class(name="genmymodelreverse_java_util_Map_Interface", is_abstract=True)
genmymodelreverse_C12 = Class(name="genmymodelreverse_C12")
genmymodelreverse_C21 = Class(name="genmymodelreverse_C21")

# bytecode_ArgsByteCode class attributes and methods
bytecode_ArgsByteCode_argCount: Property = Property(name="argCount", type=IntegerType)
bytecode_ArgsByteCode_byteCode: Property = Property(name="byteCode", type=StringType)
bytecode_ArgsByteCode.attributes={bytecode_ArgsByteCode_argCount, bytecode_ArgsByteCode_byteCode}

# bytecode_BopByteCode class attributes and methods
bytecode_BopByteCode_byteCode: Property = Property(name="byteCode", type=StringType)
bytecode_BopByteCode_theOperator: Property = Property(name="theOperator", type=StringType)
bytecode_BopByteCode.attributes={bytecode_BopByteCode_byteCode, bytecode_BopByteCode_theOperator}

# bytecode_ByteCode class attributes and methods

# bytecode_CallByteCode class attributes and methods
bytecode_CallByteCode_byteCode: Property = Property(name="byteCode", type=StringType)
bytecode_CallByteCode_theArg: Property = Property(name="theArg", type=StringType)
bytecode_CallByteCode_lineNO: Property = Property(name="lineNO", type=IntegerType)
bytecode_CallByteCode.attributes={bytecode_CallByteCode_byteCode, bytecode_CallByteCode_lineNO, bytecode_CallByteCode_theArg}

# bytecode_DumpByteCode class attributes and methods
bytecode_DumpByteCode_byteCode: Property = Property(name="byteCode", type=StringType)
bytecode_DumpByteCode_theArg: Property = Property(name="theArg", type=StringType)
bytecode_DumpByteCode.attributes={bytecode_DumpByteCode_byteCode, bytecode_DumpByteCode_theArg}

# bytecode_FalseBranchByteCode class attributes and methods
bytecode_FalseBranchByteCode_byteCode: Property = Property(name="byteCode", type=StringType)
bytecode_FalseBranchByteCode_theArg: Property = Property(name="theArg", type=StringType)
bytecode_FalseBranchByteCode_lineNO: Property = Property(name="lineNO", type=IntegerType)
bytecode_FalseBranchByteCode.attributes={bytecode_FalseBranchByteCode_theArg, bytecode_FalseBranchByteCode_lineNO, bytecode_FalseBranchByteCode_byteCode}

# bytecode_GoToByteCode class attributes and methods
bytecode_GoToByteCode_byteCode: Property = Property(name="byteCode", type=StringType)
bytecode_GoToByteCode_theArg: Property = Property(name="theArg", type=StringType)
bytecode_GoToByteCode_lineNO: Property = Property(name="lineNO", type=IntegerType)
bytecode_GoToByteCode.attributes={bytecode_GoToByteCode_byteCode, bytecode_GoToByteCode_theArg, bytecode_GoToByteCode_lineNO}

# bytecode_HaltByteCode class attributes and methods
bytecode_HaltByteCode_byteCode: Property = Property(name="byteCode", type=StringType)
bytecode_HaltByteCode.attributes={bytecode_HaltByteCode_byteCode}

# bytecode_LabelByteCode class attributes and methods
bytecode_LabelByteCode_lineNO: Property = Property(name="lineNO", type=IntegerType)
bytecode_LabelByteCode_byteCode: Property = Property(name="byteCode", type=StringType)
bytecode_LabelByteCode_theArg: Property = Property(name="theArg", type=StringType)
bytecode_LabelByteCode.attributes={bytecode_LabelByteCode_lineNO, bytecode_LabelByteCode_byteCode, bytecode_LabelByteCode_theArg}

# bytecode_LitByteCode class attributes and methods
bytecode_LitByteCode_byteCode: Property = Property(name="byteCode", type=StringType)
bytecode_LitByteCode_litValue: Property = Property(name="litValue", type=IntegerType)
bytecode_LitByteCode_litID: Property = Property(name="litID", type=StringType)
bytecode_LitByteCode.attributes={bytecode_LitByteCode_litID, bytecode_LitByteCode_litValue, bytecode_LitByteCode_byteCode}

# bytecode_LoadByteCode class attributes and methods
bytecode_LoadByteCode_byteCode: Property = Property(name="byteCode", type=StringType)
bytecode_LoadByteCode_loadOffset: Property = Property(name="loadOffset", type=IntegerType)
bytecode_LoadByteCode_loadID: Property = Property(name="loadID", type=StringType)
bytecode_LoadByteCode.attributes={bytecode_LoadByteCode_loadID, bytecode_LoadByteCode_byteCode, bytecode_LoadByteCode_loadOffset}

# bytecode_PopByteCode class attributes and methods
bytecode_PopByteCode_byteCode: Property = Property(name="byteCode", type=StringType)
bytecode_PopByteCode_theArg: Property = Property(name="theArg", type=StringType)
bytecode_PopByteCode_count: Property = Property(name="count", type=IntegerType)
bytecode_PopByteCode.attributes={bytecode_PopByteCode_byteCode, bytecode_PopByteCode_theArg, bytecode_PopByteCode_count}

# bytecode_ReadByteCode class attributes and methods
bytecode_ReadByteCode_byteCode: Property = Property(name="byteCode", type=StringType)
bytecode_ReadByteCode.attributes={bytecode_ReadByteCode_byteCode}

# bytecode_ReturnByteCode class attributes and methods
bytecode_ReturnByteCode_byteCode: Property = Property(name="byteCode", type=StringType)
bytecode_ReturnByteCode.attributes={bytecode_ReturnByteCode_byteCode}

# bytecode_StoreByteCode class attributes and methods
bytecode_StoreByteCode_byteCode: Property = Property(name="byteCode", type=StringType)
bytecode_StoreByteCode_theArg: Property = Property(name="theArg", type=StringType)
bytecode_StoreByteCode_storeValue: Property = Property(name="storeValue", type=IntegerType)
bytecode_StoreByteCode_storeID: Property = Property(name="storeID", type=StringType)
bytecode_StoreByteCode.attributes={bytecode_StoreByteCode_byteCode, bytecode_StoreByteCode_storeValue, bytecode_StoreByteCode_theArg, bytecode_StoreByteCode_storeID}

# bytecode_WriteByteCode class attributes and methods
bytecode_WriteByteCode_byteCode: Property = Property(name="byteCode", type=StringType)
bytecode_WriteByteCode.attributes={bytecode_WriteByteCode_byteCode}

# interpreter_ByteCodeLoader class attributes and methods
interpreter_ByteCodeLoader_input: Property = Property(name="input", type=genmymodelreverse_java_util_Scanner)
interpreter_ByteCodeLoader_programMap: Property = Property(name="programMap", type=StringType)
interpreter_ByteCodeLoader_lineCount: Property = Property(name="lineCount", type=IntegerType)
interpreter_ByteCodeLoader.attributes={interpreter_ByteCodeLoader_input, interpreter_ByteCodeLoader_programMap, interpreter_ByteCodeLoader_lineCount}

# interpreter_CodeTable class attributes and methods
interpreter_CodeTable_codeMap: Property = Property(name="codeMap", type=StringType)
interpreter_CodeTable_byteCodesTXT: Property = Property(name="byteCodesTXT", type=StringType)
interpreter_CodeTable.attributes={interpreter_CodeTable_codeMap, interpreter_CodeTable_byteCodesTXT}

# interpreter_Interpreter class attributes and methods

# interpreter_Program class attributes and methods
interpreter_Program_programMap: Property = Property(name="programMap", type=StringType)
interpreter_Program_byteCodeVector: Property = Property(name="byteCodeVector", type=StringType)
interpreter_Program.attributes={interpreter_Program_byteCodeVector, interpreter_Program_programMap}

# interpreter_RunTimeStack class attributes and methods
interpreter_RunTimeStack_runStack: Property = Property(name="runStack", type=StringType)
interpreter_RunTimeStack_framePointers: Property = Property(name="framePointers", type=IntegerType)
interpreter_RunTimeStack.attributes={interpreter_RunTimeStack_framePointers, interpreter_RunTimeStack_runStack}

# interpreter_VirtualMachine class attributes and methods
interpreter_VirtualMachine_pc: Property = Property(name="pc", type=IntegerType)
interpreter_VirtualMachine_isRunning: Property = Property(name="isRunning", type=BooleanType)
interpreter_VirtualMachine_dumpState: Property = Property(name="dumpState", type=BooleanType)
interpreter_VirtualMachine_returnAddrs: Property = Property(name="returnAddrs", type=IntegerType)
interpreter_VirtualMachine.attributes={interpreter_VirtualMachine_pc, interpreter_VirtualMachine_dumpState, interpreter_VirtualMachine_returnAddrs, interpreter_VirtualMachine_isRunning}

# genmymodelreverse_java_util_Scanner class attributes and methods

# genmymodelreverse_java_io_IOException class attributes and methods

# genmymodelreverse_java_util_HashMap class attributes and methods

# genmymodelreverse_C1 class attributes and methods

# genmymodelreverse_C2 class attributes and methods

# genmymodelreverse_java_util_Vector class attributes and methods

# genmymodelreverse_C11 class attributes and methods

# genmymodelreverse_java_util_Map_Interface class attributes and methods

# genmymodelreverse_C12 class attributes and methods

# genmymodelreverse_C21 class attributes and methods

# Relationships
bcl_Interpreter_ByteCodeLoader_2: BinaryAssociation = BinaryAssociation(
    name="bcl_Interpreter_ByteCodeLoader_2",
    ends={
        Property(name="interpreter0", type=interpreter_Interpreter, multiplicity=Multiplicity(0, 1)),
        Property(name="bcl1", type=interpreter_ByteCodeLoader, multiplicity=Multiplicity(0, 1))
    }
)
newProgram_VirtualMachine_Program_1: BinaryAssociation = BinaryAssociation(
    name="newProgram_VirtualMachine_Program_1",
    ends={
        Property(name="virtualmachine2", type=interpreter_VirtualMachine, multiplicity=Multiplicity(0, 1)),
        Property(name="newProgram3", type=interpreter_Program, multiplicity=Multiplicity(0, 1))
    }
)
newRunStack_VirtualMachine_RunTimeStack_0: BinaryAssociation = BinaryAssociation(
    name="newRunStack_VirtualMachine_RunTimeStack_0",
    ends={
        Property(name="virtualmachine4", type=interpreter_VirtualMachine, multiplicity=Multiplicity(0, 1)),
        Property(name="newRunStack5", type=interpreter_RunTimeStack, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="__uD_0HFREemkSo3PkdMxbg",
    types={bytecode_ArgsByteCode, bytecode_BopByteCode, bytecode_ByteCode, bytecode_CallByteCode, bytecode_DumpByteCode, bytecode_FalseBranchByteCode, bytecode_GoToByteCode, bytecode_HaltByteCode, bytecode_LabelByteCode, bytecode_LitByteCode, bytecode_LoadByteCode, bytecode_PopByteCode, bytecode_ReadByteCode, bytecode_ReturnByteCode, bytecode_StoreByteCode, bytecode_WriteByteCode, interpreter_ByteCodeLoader, interpreter_CodeTable, interpreter_Interpreter, interpreter_Program, interpreter_RunTimeStack, interpreter_VirtualMachine, genmymodelreverse_java_util_Scanner, genmymodelreverse_java_io_IOException, genmymodelreverse_java_util_HashMap, genmymodelreverse_C1, genmymodelreverse_C2, genmymodelreverse_java_util_Vector, genmymodelreverse_C11, genmymodelreverse_java_util_Map_Interface, genmymodelreverse_C12, genmymodelreverse_C21},
    associations={bcl_Interpreter_ByteCodeLoader_2, newProgram_VirtualMachine_Program_1, newRunStack_VirtualMachine_RunTimeStack_0},
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