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
PrimitiveType: Enumeration = Enumeration(
    name="PrimitiveType",
    literals={
            EnumerationLiteral(name="Int"),
			EnumerationLiteral(name="Real"),
			EnumerationLiteral(name="Bool")
    }
)

# Classes
ir_IrAnnotable = Class(name="ir::IrAnnotable", is_abstract=True)
ir_IrAnnotation = Class(name="ir::IrAnnotation")
ir_EStringToStringMapEntry = Class(name="ir::EStringToStringMapEntry")
ir_JobContainer = Class(name="ir::JobContainer", is_abstract=True)
IrAnnotable = Class(name="IrAnnotable")
ir_Job = Class(name="ir::Job", is_abstract=True)
ir_IrModule = Class(name="ir::IrModule")
JobContainer = Class(name="JobContainer")
ir_Import = Class(name="ir::Import")
ir_ItemType = Class(name="ir::ItemType")
ir_Function = Class(name="ir::Function")
ir_Connectivity = Class(name="ir::Connectivity")
ir_SimpleVariable = Class(name="ir::SimpleVariable")
ir_Variable = Class(name="ir::Variable", is_abstract=True)
ir_ConnectivityVariable = Class(name="ir::ConnectivityVariable")
Variable = Class(name="Variable")
ir_TimeLoop = Class(name="ir::TimeLoop")
ir_PostProcessingInfo = Class(name="ir::PostProcessingInfo")
ir_TimeLoopVariable = Class(name="ir::TimeLoopVariable")
ir_Expression = Class(name="ir::Expression", is_abstract=True)
ir_TimeLoopJob = Class(name="ir::TimeLoopJob")
ir_ArgOrVar = Class(name="ir::ArgOrVar", is_abstract=True)
ir_Arg = Class(name="ir::Arg")
ArgOrVar = Class(name="ArgOrVar")
ir_BaseType = Class(name="ir::BaseType")
ir_TimeLoopCopyJob = Class(name="ir::TimeLoopCopyJob", is_abstract=True)
ir_ConnectivityType = Class(name="ir::ConnectivityType")
ir_ArgOrVarRef = Class(name="ir::ArgOrVarRef")
ir_Instruction = Class(name="ir::Instruction", is_abstract=True)
ir_InstructionJob = Class(name="ir::InstructionJob")
Job = Class(name="Job")
TimeLoopCopyJob = Class(name="TimeLoopCopyJob")
ir_Loop = Class(name="ir::Loop")
ir_TimeLoopCopy = Class(name="ir::TimeLoopCopy")
ir_BeforeTimeLoopJob = Class(name="ir::BeforeTimeLoopJob")
ir_AfterTimeLoopJob = Class(name="ir::AfterTimeLoopJob")
ir_InstructionBlock = Class(name="ir::InstructionBlock")
Instruction = Class(name="Instruction")
ir_VariableDefinition = Class(name="ir::VariableDefinition")
ir_Affectation = Class(name="ir::Affectation")
ir_IterableInstruction = Class(name="ir::IterableInstruction", is_abstract=True)
ir_IterationBlock = Class(name="ir::IterationBlock", is_abstract=True)
ir_ReductionInstruction = Class(name="ir::ReductionInstruction")
IterableInstruction = Class(name="IterableInstruction")
ir_ItemIndexDefinition = Class(name="ir::ItemIndexDefinition")
ir_ItemIndex = Class(name="ir::ItemIndex")
ir_ItemIndexValue = Class(name="ir::ItemIndexValue")
ir_ItemIdDefinition = Class(name="ir::ItemIdDefinition")
ir_ItemId = Class(name="ir::ItemId")
ir_ItemIdValue = Class(name="ir::ItemIdValue", is_abstract=True)
ir_SetDefinition = Class(name="ir::SetDefinition")
ir_ConnectivityCall = Class(name="ir::ConnectivityCall")
ir_If = Class(name="ir::If")
ir_Return = Class(name="ir::Return")
ir_Exit = Class(name="ir::Exit")
ir_Iterator = Class(name="ir::Iterator")
IterationBlock = Class(name="IterationBlock")
ir_Container = Class(name="ir::Container", is_abstract=True)
ir_MaxConstant = Class(name="ir::MaxConstant")
ir_FunctionCall = Class(name="ir::FunctionCall")
ir_Interval = Class(name="ir::Interval")
ir_IrType = Class(name="ir::IrType")
ir_ContractedIf = Class(name="ir::ContractedIf")
Expression = Class(name="Expression")
ir_BinaryExpression = Class(name="ir::BinaryExpression")
ir_UnaryExpression = Class(name="ir::UnaryExpression")
ir_Parenthesis = Class(name="ir::Parenthesis")
ir_IntConstant = Class(name="ir::IntConstant")
ir_RealConstant = Class(name="ir::RealConstant")
ir_BoolConstant = Class(name="ir::BoolConstant")
ir_MinConstant = Class(name="ir::MinConstant")
ir_BaseTypeConstant = Class(name="ir::BaseTypeConstant")
ir_VectorConstant = Class(name="ir::VectorConstant")
IrType = Class(name="IrType")
ir_Cardinality = Class(name="ir::Cardinality")
Container = Class(name="Container")
ir_SetRef = Class(name="ir::SetRef")
ir_ItemIdValueIterator = Class(name="ir::ItemIdValueIterator")
ItemIdValue = Class(name="ItemIdValue")
ir_ItemIdValueCall = Class(name="ir::ItemIdValueCall")

# ir_IrAnnotable class attributes and methods

# ir_IrAnnotation class attributes and methods
ir_IrAnnotation_source: Property = Property(name="source", type=StringType)
ir_IrAnnotation.attributes={ir_IrAnnotation_source}

# ir_EStringToStringMapEntry class attributes and methods

# ir_JobContainer class attributes and methods

# IrAnnotable class attributes and methods

# ir_Job class attributes and methods
ir_Job_name: Property = Property(name="name", type=StringType)
ir_Job_at: Property = Property(name="at", type=FloatType)
ir_Job_onCycle: Property = Property(name="onCycle", type=BooleanType)
ir_Job.attributes={ir_Job_at, ir_Job_onCycle, ir_Job_name}

# ir_IrModule class attributes and methods
ir_IrModule_name: Property = Property(name="name", type=StringType)
ir_IrModule.attributes={ir_IrModule_name}

# JobContainer class attributes and methods

# ir_Import class attributes and methods
ir_Import_importedNamespace: Property = Property(name="importedNamespace", type=StringType)
ir_Import.attributes={ir_Import_importedNamespace}

# ir_ItemType class attributes and methods
ir_ItemType_name: Property = Property(name="name", type=StringType)
ir_ItemType.attributes={ir_ItemType_name}

# ir_Function class attributes and methods
ir_Function_provider: Property = Property(name="provider", type=StringType)
ir_Function_name: Property = Property(name="name", type=StringType)
ir_Function.attributes={ir_Function_provider, ir_Function_name}

# ir_Connectivity class attributes and methods
ir_Connectivity_name: Property = Property(name="name", type=StringType)
ir_Connectivity_indexEqualId: Property = Property(name="indexEqualId", type=BooleanType)
ir_Connectivity_multiple: Property = Property(name="multiple", type=BooleanType)
ir_Connectivity.attributes={ir_Connectivity_multiple, ir_Connectivity_name, ir_Connectivity_indexEqualId}

# ir_SimpleVariable class attributes and methods

# ir_Variable class attributes and methods
ir_Variable_persistenceName: Property = Property(name="persistenceName", type=StringType)
ir_Variable_const: Property = Property(name="const", type=BooleanType)
ir_Variable.attributes={ir_Variable_const, ir_Variable_persistenceName}

# ir_ConnectivityVariable class attributes and methods

# Variable class attributes and methods

# ir_TimeLoop class attributes and methods
ir_TimeLoop_name: Property = Property(name="name", type=StringType)
ir_TimeLoop.attributes={ir_TimeLoop_name}

# ir_PostProcessingInfo class attributes and methods
ir_PostProcessingInfo_periodValue: Property = Property(name="periodValue", type=FloatType)
ir_PostProcessingInfo.attributes={ir_PostProcessingInfo_periodValue}

# ir_TimeLoopVariable class attributes and methods
ir_TimeLoopVariable_name: Property = Property(name="name", type=StringType)
ir_TimeLoopVariable.attributes={ir_TimeLoopVariable_name}

# ir_Expression class attributes and methods

# ir_TimeLoopJob class attributes and methods

# ir_ArgOrVar class attributes and methods
ir_ArgOrVar_name: Property = Property(name="name", type=StringType)
ir_ArgOrVar.attributes={ir_ArgOrVar_name}

# ir_Arg class attributes and methods

# ArgOrVar class attributes and methods

# ir_BaseType class attributes and methods
ir_BaseType_primitive: Property = Property(name="primitive", type=StringType)
ir_BaseType.attributes={ir_BaseType_primitive}

# ir_TimeLoopCopyJob class attributes and methods

# ir_ConnectivityType class attributes and methods

# ir_ArgOrVarRef class attributes and methods

# ir_Instruction class attributes and methods

# ir_InstructionJob class attributes and methods

# Job class attributes and methods

# TimeLoopCopyJob class attributes and methods

# ir_Loop class attributes and methods
ir_Loop_multithreadable: Property = Property(name="multithreadable", type=BooleanType)
ir_Loop.attributes={ir_Loop_multithreadable}

# ir_TimeLoopCopy class attributes and methods

# ir_BeforeTimeLoopJob class attributes and methods

# ir_AfterTimeLoopJob class attributes and methods

# ir_InstructionBlock class attributes and methods

# Instruction class attributes and methods

# ir_VariableDefinition class attributes and methods

# ir_Affectation class attributes and methods

# ir_IterableInstruction class attributes and methods

# ir_IterationBlock class attributes and methods

# ir_ReductionInstruction class attributes and methods

# IterableInstruction class attributes and methods

# ir_ItemIndexDefinition class attributes and methods

# ir_ItemIndex class attributes and methods
ir_ItemIndex_name: Property = Property(name="name", type=StringType)
ir_ItemIndex_itemName: Property = Property(name="itemName", type=StringType)
ir_ItemIndex.attributes={ir_ItemIndex_itemName, ir_ItemIndex_name}

# ir_ItemIndexValue class attributes and methods

# ir_ItemIdDefinition class attributes and methods

# ir_ItemId class attributes and methods
ir_ItemId_name: Property = Property(name="name", type=StringType)
ir_ItemId_itemName: Property = Property(name="itemName", type=StringType)
ir_ItemId.attributes={ir_ItemId_name, ir_ItemId_itemName}

# ir_ItemIdValue class attributes and methods

# ir_SetDefinition class attributes and methods
ir_SetDefinition_name: Property = Property(name="name", type=StringType)
ir_SetDefinition.attributes={ir_SetDefinition_name}

# ir_ConnectivityCall class attributes and methods

# ir_If class attributes and methods

# ir_Return class attributes and methods

# ir_Exit class attributes and methods
ir_Exit_message: Property = Property(name="message", type=StringType)
ir_Exit.attributes={ir_Exit_message}

# ir_Iterator class attributes and methods

# IterationBlock class attributes and methods

# ir_Container class attributes and methods

# ir_MaxConstant class attributes and methods

# ir_FunctionCall class attributes and methods

# ir_Interval class attributes and methods

# ir_IrType class attributes and methods

# ir_ContractedIf class attributes and methods

# Expression class attributes and methods

# ir_BinaryExpression class attributes and methods
ir_BinaryExpression_operator: Property = Property(name="operator", type=StringType)
ir_BinaryExpression.attributes={ir_BinaryExpression_operator}

# ir_UnaryExpression class attributes and methods
ir_UnaryExpression_operator: Property = Property(name="operator", type=StringType)
ir_UnaryExpression.attributes={ir_UnaryExpression_operator}

# ir_Parenthesis class attributes and methods

# ir_IntConstant class attributes and methods
ir_IntConstant_value: Property = Property(name="value", type=IntegerType)
ir_IntConstant.attributes={ir_IntConstant_value}

# ir_RealConstant class attributes and methods
ir_RealConstant_value: Property = Property(name="value", type=FloatType)
ir_RealConstant.attributes={ir_RealConstant_value}

# ir_BoolConstant class attributes and methods
ir_BoolConstant_value: Property = Property(name="value", type=BooleanType)
ir_BoolConstant.attributes={ir_BoolConstant_value}

# ir_MinConstant class attributes and methods

# ir_BaseTypeConstant class attributes and methods

# ir_VectorConstant class attributes and methods

# IrType class attributes and methods

# ir_Cardinality class attributes and methods

# Container class attributes and methods

# ir_SetRef class attributes and methods

# ir_ItemIdValueIterator class attributes and methods
ir_ItemIdValueIterator_shift: Property = Property(name="shift", type=IntegerType)
ir_ItemIdValueIterator.attributes={ir_ItemIdValueIterator_shift}

# ItemIdValue class attributes and methods

# ir_ItemIdValueCall class attributes and methods

# Relationships
deltatVariable23: BinaryAssociation = BinaryAssociation(
    name="deltatVariable23",
    ends={
        Property(name="ir_SimpleVariable25", type=ir_IrModule, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_IrModule24", type=ir_SimpleVariable, multiplicity=Multiplicity(1, 1))
    }
)
jobs26: BinaryAssociation = BinaryAssociation(
    name="jobs26",
    ends={
        Property(name="ir_Job", type=ir_IrModule, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_IrModule27", type=ir_Job, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotations0: BinaryAssociation = BinaryAssociation(
    name="annotations0",
    ends={
        Property(name="ir_IrAnnotation", type=ir_IrAnnotable, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_IrAnnotable", type=ir_IrAnnotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
details1: BinaryAssociation = BinaryAssociation(
    name="details1",
    ends={
        Property(name="ir_EStringToStringMapEntry", type=ir_IrAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_IrAnnotation2", type=ir_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
innerJobs3: BinaryAssociation = BinaryAssociation(
    name="innerJobs3",
    ends={
        Property(name="Job", type=ir_JobContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="jobContainer", type=ir_Job, multiplicity=Multiplicity(0, 9999))
    }
)
imports4: BinaryAssociation = BinaryAssociation(
    name="imports4",
    ends={
        Property(name="ir_Import", type=ir_IrModule, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_IrModule", type=ir_Import, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
itemTypes5: BinaryAssociation = BinaryAssociation(
    name="itemTypes5",
    ends={
        Property(name="ir_ItemType", type=ir_IrModule, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_IrModule6", type=ir_ItemType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
functions7: BinaryAssociation = BinaryAssociation(
    name="functions7",
    ends={
        Property(name="ir_Function", type=ir_IrModule, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_IrModule8", type=ir_Function, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
connectivities9: BinaryAssociation = BinaryAssociation(
    name="connectivities9",
    ends={
        Property(name="ir_Connectivity", type=ir_IrModule, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_IrModule10", type=ir_Connectivity, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
options11: BinaryAssociation = BinaryAssociation(
    name="options11",
    ends={
        Property(name="ir_SimpleVariable", type=ir_IrModule, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_IrModule12", type=ir_SimpleVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variables13: BinaryAssociation = BinaryAssociation(
    name="variables13",
    ends={
        Property(name="ir_Variable", type=ir_IrModule, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_IrModule14", type=ir_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initNodeCoordVariable15: BinaryAssociation = BinaryAssociation(
    name="initNodeCoordVariable15",
    ends={
        Property(name="ir_ConnectivityVariable", type=ir_IrModule, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_IrModule16", type=ir_ConnectivityVariable, multiplicity=Multiplicity(1, 1))
    }
)
nodeCoordVariable17: BinaryAssociation = BinaryAssociation(
    name="nodeCoordVariable17",
    ends={
        Property(name="ir_ConnectivityVariable19", type=ir_IrModule, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_IrModule18", type=ir_ConnectivityVariable, multiplicity=Multiplicity(1, 1))
    }
)
timeVariable20: BinaryAssociation = BinaryAssociation(
    name="timeVariable20",
    ends={
        Property(name="ir_SimpleVariable22", type=ir_IrModule, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_IrModule21", type=ir_SimpleVariable, multiplicity=Multiplicity(1, 1))
    }
)
mainTimeLoop28: BinaryAssociation = BinaryAssociation(
    name="mainTimeLoop28",
    ends={
        Property(name="ir_TimeLoop", type=ir_IrModule, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_IrModule29", type=ir_TimeLoop, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
postProcessingInfo30: BinaryAssociation = BinaryAssociation(
    name="postProcessingInfo30",
    ends={
        Property(name="ir_PostProcessingInfo", type=ir_IrModule, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_IrModule31", type=ir_PostProcessingInfo, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
postProcessedVariables32: BinaryAssociation = BinaryAssociation(
    name="postProcessedVariables32",
    ends={
        Property(name="ir_Variable34", type=ir_PostProcessingInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_PostProcessingInfo33", type=ir_Variable, multiplicity=Multiplicity(0, 9999))
    }
)
periodVariable35: BinaryAssociation = BinaryAssociation(
    name="periodVariable35",
    ends={
        Property(name="ir_SimpleVariable37", type=ir_PostProcessingInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_PostProcessingInfo36", type=ir_SimpleVariable, multiplicity=Multiplicity(1, 1))
    }
)
lastDumpVariable38: BinaryAssociation = BinaryAssociation(
    name="lastDumpVariable38",
    ends={
        Property(name="ir_SimpleVariable40", type=ir_PostProcessingInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_PostProcessingInfo39", type=ir_SimpleVariable, multiplicity=Multiplicity(1, 1))
    }
)
innerTimeLoop42: BinaryAssociation = BinaryAssociation(
    name="innerTimeLoop42",
    ends={
        Property(name="TimeLoop", type=ir_TimeLoop, multiplicity=Multiplicity(1, 1)),
        Property(name="outerTimeLoop", type=ir_TimeLoop, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
outerTimeLoop44: BinaryAssociation = BinaryAssociation(
    name="outerTimeLoop44",
    ends={
        Property(name="TimeLoop45", type=ir_TimeLoop, multiplicity=Multiplicity(1, 1)),
        Property(name="innerTimeLoop", type=ir_TimeLoop, multiplicity=Multiplicity(0, 1))
    }
)
variables46: BinaryAssociation = BinaryAssociation(
    name="variables46",
    ends={
        Property(name="ir_TimeLoopVariable", type=ir_TimeLoop, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_TimeLoop47", type=ir_TimeLoopVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
whileCondition48: BinaryAssociation = BinaryAssociation(
    name="whileCondition48",
    ends={
        Property(name="ir_Expression", type=ir_TimeLoop, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_TimeLoop49", type=ir_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
associatedJob50: BinaryAssociation = BinaryAssociation(
    name="associatedJob50",
    ends={
        Property(name="ir_TimeLoopJob", type=ir_TimeLoop, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_TimeLoop51", type=ir_TimeLoopJob, multiplicity=Multiplicity(1, 1))
    }
)
iterationCounter52: BinaryAssociation = BinaryAssociation(
    name="iterationCounter52",
    ends={
        Property(name="ir_SimpleVariable54", type=ir_TimeLoop, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_TimeLoop53", type=ir_SimpleVariable, multiplicity=Multiplicity(1, 1))
    }
)
type55: BinaryAssociation = BinaryAssociation(
    name="type55",
    ends={
        Property(name="ir_BaseType", type=ir_Arg, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_Arg", type=ir_BaseType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type56: BinaryAssociation = BinaryAssociation(
    name="type56",
    ends={
        Property(name="ir_BaseType58", type=ir_SimpleVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_SimpleVariable57", type=ir_BaseType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
defaultValue59: BinaryAssociation = BinaryAssociation(
    name="defaultValue59",
    ends={
        Property(name="ir_Expression61", type=ir_SimpleVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_SimpleVariable60", type=ir_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type62: BinaryAssociation = BinaryAssociation(
    name="type62",
    ends={
        Property(name="ir_ConnectivityType", type=ir_ConnectivityVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_ConnectivityVariable63", type=ir_ConnectivityType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
defaultValue64: BinaryAssociation = BinaryAssociation(
    name="defaultValue64",
    ends={
        Property(name="ir_ArgOrVarRef", type=ir_ConnectivityVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_ConnectivityVariable65", type=ir_ArgOrVarRef, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
returnType66: BinaryAssociation = BinaryAssociation(
    name="returnType66",
    ends={
        Property(name="ir_BaseType68", type=ir_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_Function67", type=ir_BaseType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variables69: BinaryAssociation = BinaryAssociation(
    name="variables69",
    ends={
        Property(name="ir_SimpleVariable71", type=ir_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_Function70", type=ir_SimpleVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inArgs72: BinaryAssociation = BinaryAssociation(
    name="inArgs72",
    ends={
        Property(name="ir_Arg74", type=ir_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_Function73", type=ir_Arg, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body75: BinaryAssociation = BinaryAssociation(
    name="body75",
    ends={
        Property(name="ir_Instruction", type=ir_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_Function76", type=ir_Instruction, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
inTypes77: BinaryAssociation = BinaryAssociation(
    name="inTypes77",
    ends={
        Property(name="ir_ItemType79", type=ir_Connectivity, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_Connectivity78", type=ir_ItemType, multiplicity=Multiplicity(0, 9999))
    }
)
returnType80: BinaryAssociation = BinaryAssociation(
    name="returnType80",
    ends={
        Property(name="ir_ItemType82", type=ir_Connectivity, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_Connectivity81", type=ir_ItemType, multiplicity=Multiplicity(0, 1))
    }
)
jobContainer83: BinaryAssociation = BinaryAssociation(
    name="jobContainer83",
    ends={
        Property(name="JobContainer", type=ir_Job, multiplicity=Multiplicity(1, 1)),
        Property(name="innerJobs", type=ir_JobContainer, multiplicity=Multiplicity(1, 1))
    }
)
instruction84: BinaryAssociation = BinaryAssociation(
    name="instruction84",
    ends={
        Property(name="ir_Instruction85", type=ir_InstructionJob, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_InstructionJob", type=ir_Instruction, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
copies86: BinaryAssociation = BinaryAssociation(
    name="copies86",
    ends={
        Property(name="ir_TimeLoopCopy", type=ir_TimeLoopCopyJob, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_TimeLoopCopyJob", type=ir_TimeLoopCopy, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
timeLoop87: BinaryAssociation = BinaryAssociation(
    name="timeLoop87",
    ends={
        Property(name="ir_TimeLoop89", type=ir_TimeLoopCopyJob, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_TimeLoopCopyJob88", type=ir_TimeLoop, multiplicity=Multiplicity(1, 1))
    }
)
destination90: BinaryAssociation = BinaryAssociation(
    name="destination90",
    ends={
        Property(name="ir_Variable92", type=ir_TimeLoopCopy, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_TimeLoopCopy91", type=ir_Variable, multiplicity=Multiplicity(1, 1))
    }
)
source93: BinaryAssociation = BinaryAssociation(
    name="source93",
    ends={
        Property(name="ir_Variable95", type=ir_TimeLoopCopy, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_TimeLoopCopy94", type=ir_Variable, multiplicity=Multiplicity(1, 1))
    }
)
variables96: BinaryAssociation = BinaryAssociation(
    name="variables96",
    ends={
        Property(name="ir_Variable97", type=ir_InstructionBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_InstructionBlock", type=ir_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
instructions98: BinaryAssociation = BinaryAssociation(
    name="instructions98",
    ends={
        Property(name="ir_Instruction100", type=ir_InstructionBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_InstructionBlock99", type=ir_Instruction, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
variable101: BinaryAssociation = BinaryAssociation(
    name="variable101",
    ends={
        Property(name="ir_Variable102", type=ir_VariableDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_VariableDefinition", type=ir_Variable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
left103: BinaryAssociation = BinaryAssociation(
    name="left103",
    ends={
        Property(name="ir_ArgOrVarRef104", type=ir_Affectation, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_Affectation", type=ir_ArgOrVarRef, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
right105: BinaryAssociation = BinaryAssociation(
    name="right105",
    ends={
        Property(name="ir_Expression107", type=ir_Affectation, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_Affectation106", type=ir_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
iterationBlock108: BinaryAssociation = BinaryAssociation(
    name="iterationBlock108",
    ends={
        Property(name="ir_IterationBlock", type=ir_IterableInstruction, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_IterableInstruction", type=ir_IterationBlock, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
innerInstructions109: BinaryAssociation = BinaryAssociation(
    name="innerInstructions109",
    ends={
        Property(name="ir_Instruction110", type=ir_ReductionInstruction, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_ReductionInstruction", type=ir_Instruction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
binaryFunction111: BinaryAssociation = BinaryAssociation(
    name="binaryFunction111",
    ends={
        Property(name="ir_Function113", type=ir_ReductionInstruction, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_ReductionInstruction112", type=ir_Function, multiplicity=Multiplicity(1, 1))
    }
)
lambda114: BinaryAssociation = BinaryAssociation(
    name="lambda114",
    ends={
        Property(name="ir_Expression116", type=ir_ReductionInstruction, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_ReductionInstruction115", type=ir_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result117: BinaryAssociation = BinaryAssociation(
    name="result117",
    ends={
        Property(name="ir_SimpleVariable119", type=ir_ReductionInstruction, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_ReductionInstruction118", type=ir_SimpleVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
counter143: BinaryAssociation = BinaryAssociation(
    name="counter143",
    ends={
        Property(name="ir_SimpleVariable145", type=ir_Iterator, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_Iterator144", type=ir_SimpleVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body120: BinaryAssociation = BinaryAssociation(
    name="body120",
    ends={
        Property(name="ir_Instruction121", type=ir_Loop, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_Loop", type=ir_Instruction, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
index122: BinaryAssociation = BinaryAssociation(
    name="index122",
    ends={
        Property(name="ir_ItemIndex", type=ir_ItemIndexDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_ItemIndexDefinition", type=ir_ItemIndex, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value123: BinaryAssociation = BinaryAssociation(
    name="value123",
    ends={
        Property(name="ir_ItemIndexValue", type=ir_ItemIndexDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_ItemIndexDefinition124", type=ir_ItemIndexValue, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
id125: BinaryAssociation = BinaryAssociation(
    name="id125",
    ends={
        Property(name="ir_ItemId", type=ir_ItemIdDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_ItemIdDefinition", type=ir_ItemId, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value126: BinaryAssociation = BinaryAssociation(
    name="value126",
    ends={
        Property(name="ir_ItemIdValue", type=ir_ItemIdDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_ItemIdDefinition127", type=ir_ItemIdValue, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value128: BinaryAssociation = BinaryAssociation(
    name="value128",
    ends={
        Property(name="ir_ConnectivityCall", type=ir_SetDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_SetDefinition", type=ir_ConnectivityCall, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition129: BinaryAssociation = BinaryAssociation(
    name="condition129",
    ends={
        Property(name="ir_Expression130", type=ir_If, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_If", type=ir_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thenInstruction131: BinaryAssociation = BinaryAssociation(
    name="thenInstruction131",
    ends={
        Property(name="ir_Instruction133", type=ir_If, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_If132", type=ir_Instruction, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elseInstruction134: BinaryAssociation = BinaryAssociation(
    name="elseInstruction134",
    ends={
        Property(name="ir_Instruction136", type=ir_If, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_If135", type=ir_Instruction, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression137: BinaryAssociation = BinaryAssociation(
    name="expression137",
    ends={
        Property(name="ir_Expression138", type=ir_Return, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_Return", type=ir_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
index139: BinaryAssociation = BinaryAssociation(
    name="index139",
    ends={
        Property(name="ir_ItemIndex140", type=ir_Iterator, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_Iterator", type=ir_ItemIndex, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
container141: BinaryAssociation = BinaryAssociation(
    name="container141",
    ends={
        Property(name="ir_Container", type=ir_Iterator, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_Iterator142", type=ir_Container, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
index146: BinaryAssociation = BinaryAssociation(
    name="index146",
    ends={
        Property(name="ir_SimpleVariable147", type=ir_Interval, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_Interval", type=ir_SimpleVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
nbElems148: BinaryAssociation = BinaryAssociation(
    name="nbElems148",
    ends={
        Property(name="ir_Expression150", type=ir_Interval, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_Interval149", type=ir_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type151: BinaryAssociation = BinaryAssociation(
    name="type151",
    ends={
        Property(name="ir_IrType", type=ir_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_Expression152", type=ir_IrType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition153: BinaryAssociation = BinaryAssociation(
    name="condition153",
    ends={
        Property(name="ir_Expression154", type=ir_ContractedIf, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_ContractedIf", type=ir_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thenExpression155: BinaryAssociation = BinaryAssociation(
    name="thenExpression155",
    ends={
        Property(name="ir_Expression157", type=ir_ContractedIf, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_ContractedIf156", type=ir_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elseExpression158: BinaryAssociation = BinaryAssociation(
    name="elseExpression158",
    ends={
        Property(name="ir_Expression160", type=ir_ContractedIf, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_ContractedIf159", type=ir_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
left161: BinaryAssociation = BinaryAssociation(
    name="left161",
    ends={
        Property(name="ir_Expression162", type=ir_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_BinaryExpression", type=ir_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
right163: BinaryAssociation = BinaryAssociation(
    name="right163",
    ends={
        Property(name="ir_Expression165", type=ir_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_BinaryExpression164", type=ir_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression166: BinaryAssociation = BinaryAssociation(
    name="expression166",
    ends={
        Property(name="ir_Expression167", type=ir_UnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_UnaryExpression", type=ir_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression168: BinaryAssociation = BinaryAssociation(
    name="expression168",
    ends={
        Property(name="ir_Expression169", type=ir_Parenthesis, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_Parenthesis", type=ir_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
function170: BinaryAssociation = BinaryAssociation(
    name="function170",
    ends={
        Property(name="ir_Function171", type=ir_FunctionCall, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_FunctionCall", type=ir_Function, multiplicity=Multiplicity(1, 1))
    }
)
args172: BinaryAssociation = BinaryAssociation(
    name="args172",
    ends={
        Property(name="ir_Expression174", type=ir_FunctionCall, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_FunctionCall173", type=ir_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value175: BinaryAssociation = BinaryAssociation(
    name="value175",
    ends={
        Property(name="ir_Expression176", type=ir_BaseTypeConstant, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_BaseTypeConstant", type=ir_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
values177: BinaryAssociation = BinaryAssociation(
    name="values177",
    ends={
        Property(name="ir_Expression178", type=ir_VectorConstant, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_VectorConstant", type=ir_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
container179: BinaryAssociation = BinaryAssociation(
    name="container179",
    ends={
        Property(name="ir_Container180", type=ir_Cardinality, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_Cardinality", type=ir_Container, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
target181: BinaryAssociation = BinaryAssociation(
    name="target181",
    ends={
        Property(name="ir_ArgOrVar", type=ir_ArgOrVarRef, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_ArgOrVarRef182", type=ir_ArgOrVar, multiplicity=Multiplicity(1, 1))
    }
)
iterators183: BinaryAssociation = BinaryAssociation(
    name="iterators183",
    ends={
        Property(name="ir_ItemIndex185", type=ir_ArgOrVarRef, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_ArgOrVarRef184", type=ir_ItemIndex, multiplicity=Multiplicity(0, 9999))
    }
)
indices186: BinaryAssociation = BinaryAssociation(
    name="indices186",
    ends={
        Property(name="ir_Expression188", type=ir_ArgOrVarRef, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_ArgOrVarRef187", type=ir_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sizes189: BinaryAssociation = BinaryAssociation(
    name="sizes189",
    ends={
        Property(name="ir_Expression191", type=ir_BaseType, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_BaseType190", type=ir_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
connectivities192: BinaryAssociation = BinaryAssociation(
    name="connectivities192",
    ends={
        Property(name="ir_Connectivity194", type=ir_ConnectivityType, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_ConnectivityType193", type=ir_Connectivity, multiplicity=Multiplicity(0, 9999))
    }
)
base195: BinaryAssociation = BinaryAssociation(
    name="base195",
    ends={
        Property(name="ir_BaseType197", type=ir_ConnectivityType, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_ConnectivityType196", type=ir_BaseType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
init198: BinaryAssociation = BinaryAssociation(
    name="init198",
    ends={
        Property(name="ir_Variable200", type=ir_TimeLoopVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_TimeLoopVariable199", type=ir_Variable, multiplicity=Multiplicity(0, 1))
    }
)
current201: BinaryAssociation = BinaryAssociation(
    name="current201",
    ends={
        Property(name="ir_Variable203", type=ir_TimeLoopVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_TimeLoopVariable202", type=ir_Variable, multiplicity=Multiplicity(1, 1))
    }
)
next204: BinaryAssociation = BinaryAssociation(
    name="next204",
    ends={
        Property(name="ir_Variable206", type=ir_TimeLoopVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_TimeLoopVariable205", type=ir_Variable, multiplicity=Multiplicity(1, 1))
    }
)
connectivity207: BinaryAssociation = BinaryAssociation(
    name="connectivity207",
    ends={
        Property(name="ir_Connectivity209", type=ir_ConnectivityCall, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_ConnectivityCall208", type=ir_Connectivity, multiplicity=Multiplicity(1, 1))
    }
)
args210: BinaryAssociation = BinaryAssociation(
    name="args210",
    ends={
        Property(name="ir_ItemId212", type=ir_ConnectivityCall, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_ConnectivityCall211", type=ir_ItemId, multiplicity=Multiplicity(0, 9999))
    }
)
iterator215: BinaryAssociation = BinaryAssociation(
    name="iterator215",
    ends={
        Property(name="ir_Iterator216", type=ir_ItemIdValueIterator, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_ItemIdValueIterator", type=ir_Iterator, multiplicity=Multiplicity(1, 1))
    }
)
call217: BinaryAssociation = BinaryAssociation(
    name="call217",
    ends={
        Property(name="ir_ConnectivityCall218", type=ir_ItemIdValueCall, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_ItemIdValueCall", type=ir_ConnectivityCall, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
id219: BinaryAssociation = BinaryAssociation(
    name="id219",
    ends={
        Property(name="ir_ItemId221", type=ir_ItemIndexValue, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_ItemIndexValue220", type=ir_ItemId, multiplicity=Multiplicity(1, 1))
    }
)
container222: BinaryAssociation = BinaryAssociation(
    name="container222",
    ends={
        Property(name="ir_ConnectivityCall224", type=ir_ItemIndexValue, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_ItemIndexValue223", type=ir_ConnectivityCall, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
target213: BinaryAssociation = BinaryAssociation(
    name="target213",
    ends={
        Property(name="ir_SetDefinition214", type=ir_SetRef, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_SetRef", type=ir_SetDefinition, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_ir_JobContainer_IrAnnotable = Generalization(general=IrAnnotable, specific=ir_JobContainer)
gen_ir_IrModule_JobContainer = Generalization(general=JobContainer, specific=ir_IrModule)
gen_ir_SimpleVariable_Variable = Generalization(general=Variable, specific=ir_SimpleVariable)
gen_ir_Import_IrAnnotable = Generalization(general=IrAnnotable, specific=ir_Import)
gen_ir_PostProcessingInfo_IrAnnotable = Generalization(general=IrAnnotable, specific=ir_PostProcessingInfo)
gen_ir_TimeLoop_IrAnnotable = Generalization(general=IrAnnotable, specific=ir_TimeLoop)
gen_ir_ArgOrVar_IrAnnotable = Generalization(general=IrAnnotable, specific=ir_ArgOrVar)
gen_ir_Arg_ArgOrVar = Generalization(general=ArgOrVar, specific=ir_Arg)
gen_ir_Variable_ArgOrVar = Generalization(general=ArgOrVar, specific=ir_Variable)
gen_ir_TimeLoopCopyJob_Job = Generalization(general=Job, specific=ir_TimeLoopCopyJob)
gen_ir_ConnectivityVariable_Variable = Generalization(general=Variable, specific=ir_ConnectivityVariable)
gen_ir_Function_IrAnnotable = Generalization(general=IrAnnotable, specific=ir_Function)
gen_ir_Connectivity_IrAnnotable = Generalization(general=IrAnnotable, specific=ir_Connectivity)
gen_ir_Job_IrAnnotable = Generalization(general=IrAnnotable, specific=ir_Job)
gen_ir_InstructionJob_Job = Generalization(general=Job, specific=ir_InstructionJob)
gen_ir_TimeLoopJob_TimeLoopCopyJob = Generalization(general=TimeLoopCopyJob, specific=ir_TimeLoopJob)
gen_ir_TimeLoopJob_JobContainer = Generalization(general=JobContainer, specific=ir_TimeLoopJob)
gen_ir_Loop_IterableInstruction = Generalization(general=IterableInstruction, specific=ir_Loop)
gen_ir_BeforeTimeLoopJob_TimeLoopCopyJob = Generalization(general=TimeLoopCopyJob, specific=ir_BeforeTimeLoopJob)
gen_ir_AfterTimeLoopJob_TimeLoopCopyJob = Generalization(general=TimeLoopCopyJob, specific=ir_AfterTimeLoopJob)
gen_ir_TimeLoopCopy_IrAnnotable = Generalization(general=IrAnnotable, specific=ir_TimeLoopCopy)
gen_ir_Instruction_IrAnnotable = Generalization(general=IrAnnotable, specific=ir_Instruction)
gen_ir_InstructionBlock_Instruction = Generalization(general=Instruction, specific=ir_InstructionBlock)
gen_ir_VariableDefinition_Instruction = Generalization(general=Instruction, specific=ir_VariableDefinition)
gen_ir_Affectation_Instruction = Generalization(general=Instruction, specific=ir_Affectation)
gen_ir_IterableInstruction_Instruction = Generalization(general=Instruction, specific=ir_IterableInstruction)
gen_ir_ReductionInstruction_IterableInstruction = Generalization(general=IterableInstruction, specific=ir_ReductionInstruction)
gen_ir_ItemIndexDefinition_Instruction = Generalization(general=Instruction, specific=ir_ItemIndexDefinition)
gen_ir_ItemIdDefinition_Instruction = Generalization(general=Instruction, specific=ir_ItemIdDefinition)
gen_ir_SetDefinition_Instruction = Generalization(general=Instruction, specific=ir_SetDefinition)
gen_ir_If_Instruction = Generalization(general=Instruction, specific=ir_If)
gen_ir_Return_Instruction = Generalization(general=Instruction, specific=ir_Return)
gen_ir_Exit_Instruction = Generalization(general=Instruction, specific=ir_Exit)
gen_ir_IterationBlock_IrAnnotable = Generalization(general=IrAnnotable, specific=ir_IterationBlock)
gen_ir_Iterator_IterationBlock = Generalization(general=IterationBlock, specific=ir_Iterator)
gen_ir_MaxConstant_Expression = Generalization(general=Expression, specific=ir_MaxConstant)
gen_ir_Interval_IterationBlock = Generalization(general=IterationBlock, specific=ir_Interval)
gen_ir_Expression_IrAnnotable = Generalization(general=IrAnnotable, specific=ir_Expression)
gen_ir_ContractedIf_Expression = Generalization(general=Expression, specific=ir_ContractedIf)
gen_ir_BinaryExpression_Expression = Generalization(general=Expression, specific=ir_BinaryExpression)
gen_ir_UnaryExpression_Expression = Generalization(general=Expression, specific=ir_UnaryExpression)
gen_ir_Parenthesis_Expression = Generalization(general=Expression, specific=ir_Parenthesis)
gen_ir_IntConstant_Expression = Generalization(general=Expression, specific=ir_IntConstant)
gen_ir_RealConstant_Expression = Generalization(general=Expression, specific=ir_RealConstant)
gen_ir_BoolConstant_Expression = Generalization(general=Expression, specific=ir_BoolConstant)
gen_ir_MinConstant_Expression = Generalization(general=Expression, specific=ir_MinConstant)
gen_ir_FunctionCall_Expression = Generalization(general=Expression, specific=ir_FunctionCall)
gen_ir_BaseTypeConstant_Expression = Generalization(general=Expression, specific=ir_BaseTypeConstant)
gen_ir_VectorConstant_Expression = Generalization(general=Expression, specific=ir_VectorConstant)
gen_ir_ArgOrVarRef_Expression = Generalization(general=Expression, specific=ir_ArgOrVarRef)
gen_ir_ItemType_IrAnnotable = Generalization(general=IrAnnotable, specific=ir_ItemType)
gen_ir_IrType_IrAnnotable = Generalization(general=IrAnnotable, specific=ir_IrType)
gen_ir_BaseType_IrType = Generalization(general=IrType, specific=ir_BaseType)
gen_ir_Cardinality_Expression = Generalization(general=Expression, specific=ir_Cardinality)
gen_ir_ConnectivityType_IrType = Generalization(general=IrType, specific=ir_ConnectivityType)
gen_ir_TimeLoopVariable_IrAnnotable = Generalization(general=IrAnnotable, specific=ir_TimeLoopVariable)
gen_ir_Container_IrAnnotable = Generalization(general=IrAnnotable, specific=ir_Container)
gen_ir_ConnectivityCall_Container = Generalization(general=Container, specific=ir_ConnectivityCall)
gen_ir_SetRef_Container = Generalization(general=Container, specific=ir_SetRef)
gen_ir_ItemId_IrAnnotable = Generalization(general=IrAnnotable, specific=ir_ItemId)
gen_ir_ItemIdValue_IrAnnotable = Generalization(general=IrAnnotable, specific=ir_ItemIdValue)
gen_ir_ItemIdValueIterator_ItemIdValue = Generalization(general=ItemIdValue, specific=ir_ItemIdValueIterator)
gen_ir_ItemIdValueCall_ItemIdValue = Generalization(general=ItemIdValue, specific=ir_ItemIdValueCall)
gen_ir_ItemIndex_IrAnnotable = Generalization(general=IrAnnotable, specific=ir_ItemIndex)
gen_ir_ItemIndexValue_IrAnnotable = Generalization(general=IrAnnotable, specific=ir_ItemIndexValue)

# Domain Model
domain_model = DomainModel(
    name="ir",
    types={ir_IrAnnotable, ir_IrAnnotation, ir_EStringToStringMapEntry, ir_JobContainer, IrAnnotable, ir_Job, ir_IrModule, JobContainer, ir_Import, ir_ItemType, ir_Function, ir_Connectivity, ir_SimpleVariable, ir_Variable, ir_ConnectivityVariable, Variable, ir_TimeLoop, ir_PostProcessingInfo, ir_TimeLoopVariable, ir_Expression, ir_TimeLoopJob, ir_ArgOrVar, ir_Arg, ArgOrVar, ir_BaseType, ir_TimeLoopCopyJob, ir_ConnectivityType, ir_ArgOrVarRef, ir_Instruction, ir_InstructionJob, Job, TimeLoopCopyJob, ir_Loop, ir_TimeLoopCopy, ir_BeforeTimeLoopJob, ir_AfterTimeLoopJob, ir_InstructionBlock, Instruction, ir_VariableDefinition, ir_Affectation, ir_IterableInstruction, ir_IterationBlock, ir_ReductionInstruction, IterableInstruction, ir_ItemIndexDefinition, ir_ItemIndex, ir_ItemIndexValue, ir_ItemIdDefinition, ir_ItemId, ir_ItemIdValue, ir_SetDefinition, ir_ConnectivityCall, ir_If, ir_Return, ir_Exit, ir_Iterator, IterationBlock, ir_Container, ir_MaxConstant, ir_FunctionCall, ir_Interval, ir_IrType, ir_ContractedIf, Expression, ir_BinaryExpression, ir_UnaryExpression, ir_Parenthesis, ir_IntConstant, ir_RealConstant, ir_BoolConstant, ir_MinConstant, ir_BaseTypeConstant, ir_VectorConstant, IrType, ir_Cardinality, Container, ir_SetRef, ir_ItemIdValueIterator, ItemIdValue, ir_ItemIdValueCall, PrimitiveType},
    associations={deltatVariable23, jobs26, annotations0, details1, innerJobs3, imports4, itemTypes5, functions7, connectivities9, options11, variables13, initNodeCoordVariable15, nodeCoordVariable17, timeVariable20, mainTimeLoop28, postProcessingInfo30, postProcessedVariables32, periodVariable35, lastDumpVariable38, innerTimeLoop42, outerTimeLoop44, variables46, whileCondition48, associatedJob50, iterationCounter52, type55, type56, defaultValue59, type62, defaultValue64, returnType66, variables69, inArgs72, body75, inTypes77, returnType80, jobContainer83, instruction84, copies86, timeLoop87, destination90, source93, variables96, instructions98, variable101, left103, right105, iterationBlock108, innerInstructions109, binaryFunction111, lambda114, result117, counter143, body120, index122, value123, id125, value126, value128, condition129, thenInstruction131, elseInstruction134, expression137, index139, container141, index146, nbElems148, type151, condition153, thenExpression155, elseExpression158, left161, right163, expression166, expression168, function170, args172, value175, values177, container179, target181, iterators183, indices186, sizes189, connectivities192, base195, init198, current201, next204, connectivity207, args210, iterator215, call217, id219, container222, target213},
    generalizations={gen_ir_JobContainer_IrAnnotable, gen_ir_IrModule_JobContainer, gen_ir_SimpleVariable_Variable, gen_ir_Import_IrAnnotable, gen_ir_PostProcessingInfo_IrAnnotable, gen_ir_TimeLoop_IrAnnotable, gen_ir_ArgOrVar_IrAnnotable, gen_ir_Arg_ArgOrVar, gen_ir_Variable_ArgOrVar, gen_ir_TimeLoopCopyJob_Job, gen_ir_ConnectivityVariable_Variable, gen_ir_Function_IrAnnotable, gen_ir_Connectivity_IrAnnotable, gen_ir_Job_IrAnnotable, gen_ir_InstructionJob_Job, gen_ir_TimeLoopJob_TimeLoopCopyJob, gen_ir_TimeLoopJob_JobContainer, gen_ir_Loop_IterableInstruction, gen_ir_BeforeTimeLoopJob_TimeLoopCopyJob, gen_ir_AfterTimeLoopJob_TimeLoopCopyJob, gen_ir_TimeLoopCopy_IrAnnotable, gen_ir_Instruction_IrAnnotable, gen_ir_InstructionBlock_Instruction, gen_ir_VariableDefinition_Instruction, gen_ir_Affectation_Instruction, gen_ir_IterableInstruction_Instruction, gen_ir_ReductionInstruction_IterableInstruction, gen_ir_ItemIndexDefinition_Instruction, gen_ir_ItemIdDefinition_Instruction, gen_ir_SetDefinition_Instruction, gen_ir_If_Instruction, gen_ir_Return_Instruction, gen_ir_Exit_Instruction, gen_ir_IterationBlock_IrAnnotable, gen_ir_Iterator_IterationBlock, gen_ir_MaxConstant_Expression, gen_ir_Interval_IterationBlock, gen_ir_Expression_IrAnnotable, gen_ir_ContractedIf_Expression, gen_ir_BinaryExpression_Expression, gen_ir_UnaryExpression_Expression, gen_ir_Parenthesis_Expression, gen_ir_IntConstant_Expression, gen_ir_RealConstant_Expression, gen_ir_BoolConstant_Expression, gen_ir_MinConstant_Expression, gen_ir_FunctionCall_Expression, gen_ir_BaseTypeConstant_Expression, gen_ir_VectorConstant_Expression, gen_ir_ArgOrVarRef_Expression, gen_ir_ItemType_IrAnnotable, gen_ir_IrType_IrAnnotable, gen_ir_BaseType_IrType, gen_ir_Cardinality_Expression, gen_ir_ConnectivityType_IrType, gen_ir_TimeLoopVariable_IrAnnotable, gen_ir_Container_IrAnnotable, gen_ir_ConnectivityCall_Container, gen_ir_SetRef_Container, gen_ir_ItemId_IrAnnotable, gen_ir_ItemIdValue_IrAnnotable, gen_ir_ItemIdValueIterator_ItemIdValue, gen_ir_ItemIdValueCall_ItemIdValue, gen_ir_ItemIndex_IrAnnotable, gen_ir_ItemIndexValue_IrAnnotable},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)