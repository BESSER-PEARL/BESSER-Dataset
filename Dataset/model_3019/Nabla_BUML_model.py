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
nabla_NablaModule = Class(name="nabla::NablaModule")
nabla_SimpleVarDefinition = Class(name="nabla::SimpleVarDefinition")
nabla_VarGroupDeclaration = Class(name="nabla::VarGroupDeclaration")
nabla_TimeIteratorDefinition = Class(name="nabla::TimeIteratorDefinition")
nabla_Import = Class(name="nabla::Import")
nabla_ItemType = Class(name="nabla::ItemType")
nabla_Connectivity = Class(name="nabla::Connectivity")
nabla_Reduction = Class(name="nabla::Reduction")
nabla_Function = Class(name="nabla::Function")
nabla_OptDefinition = Class(name="nabla::OptDefinition")
nabla_SimpleVar = Class(name="nabla::SimpleVar")
nabla_Expression = Class(name="nabla::Expression")
nabla_Job = Class(name="nabla::Job")
nabla_SingleConnectivity = Class(name="nabla::SingleConnectivity")
nabla_MultipleConnectivity = Class(name="nabla::MultipleConnectivity")
Connectivity = Class(name="Connectivity")
nabla_Instruction = Class(name="nabla::Instruction")
nabla_Iterable = Class(name="nabla::Iterable")
nabla_IterationBlock = Class(name="nabla::IterationBlock")
Instruction = Class(name="Instruction")
nabla_Affectation = Class(name="nabla::Affectation")
nabla_ArgOrVarRef = Class(name="nabla::ArgOrVarRef")
nabla_BaseType = Class(name="nabla::BaseType")
nabla_Var = Class(name="nabla::Var")
nabla_InstructionBlock = Class(name="nabla::InstructionBlock")
nabla_Loop = Class(name="nabla::Loop")
Iterable = Class(name="Iterable")
nabla_ItemDefinition = Class(name="nabla::ItemDefinition")
nabla_Item = Class(name="nabla::Item")
nabla_If = Class(name="nabla::If")
nabla_Exit = Class(name="nabla::Exit")
nabla_Container = Class(name="nabla::Container")
nabla_SingleConnectivityCall = Class(name="nabla::SingleConnectivityCall")
nabla_SetDefinition = Class(name="nabla::SetDefinition")
nabla_MultipleConnectivityCall = Class(name="nabla::MultipleConnectivityCall")
nabla_Return = Class(name="nabla::Return")
nabla_SingletonDefinition = Class(name="nabla::SingletonDefinition")
nabla_SetRef = Class(name="nabla::SetRef")
Container = Class(name="Container")
nabla_SpaceIterator = Class(name="nabla::SpaceIterator")
IterationBlock = Class(name="IterationBlock")
nabla_Interval = Class(name="nabla::Interval")
nabla_ConnectivityCall = Class(name="nabla::ConnectivityCall")
nabla_ItemRef = Class(name="nabla::ItemRef")
ConnectivityCall = Class(name="ConnectivityCall")
nabla_TimeIteratorRef = Class(name="nabla::TimeIteratorRef")
nabla_TimeIterator = Class(name="nabla::TimeIterator")
ArgOrVar = Class(name="ArgOrVar")
nabla_ArgOrVar = Class(name="nabla::ArgOrVar")
nabla_CurrentTimeIteratorRef = Class(name="nabla::CurrentTimeIteratorRef")
TimeIteratorRef = Class(name="TimeIteratorRef")
nabla_InitTimeIteratorRef = Class(name="nabla::InitTimeIteratorRef")
nabla_NextTimeIteratorRef = Class(name="nabla::NextTimeIteratorRef")
Var = Class(name="Var")
nabla_ConnectivityVar = Class(name="nabla::ConnectivityVar")
nabla_FunctionOrReduction = Class(name="nabla::FunctionOrReduction")
nabla_Arg = Class(name="nabla::Arg")
FunctionOrReduction = Class(name="FunctionOrReduction")
nabla_IntConstant = Class(name="nabla::IntConstant")
Expression = Class(name="Expression")
nabla_ReductionCall = Class(name="nabla::ReductionCall")
nabla_ContractedIf = Class(name="nabla::ContractedIf")
nabla_And = Class(name="nabla::And")
nabla_Or = Class(name="nabla::Or")
nabla_Comparison = Class(name="nabla::Comparison")
nabla_Equality = Class(name="nabla::Equality")
nabla_Minus = Class(name="nabla::Minus")
nabla_Plus = Class(name="nabla::Plus")
nabla_Mul = Class(name="nabla::Mul")
nabla_Div = Class(name="nabla::Div")
nabla_UnaryMinus = Class(name="nabla::UnaryMinus")
nabla_Modulo = Class(name="nabla::Modulo")
nabla_Parenthesis = Class(name="nabla::Parenthesis")
nabla_MaxConstant = Class(name="nabla::MaxConstant")
nabla_Not = Class(name="nabla::Not")
nabla_RealConstant = Class(name="nabla::RealConstant")
nabla_BoolConstant = Class(name="nabla::BoolConstant")
nabla_MinConstant = Class(name="nabla::MinConstant")
nabla_VectorConstant = Class(name="nabla::VectorConstant")
nabla_FunctionCall = Class(name="nabla::FunctionCall")
nabla_BaseTypeConstant = Class(name="nabla::BaseTypeConstant")
nabla_Cardinality = Class(name="nabla::Cardinality")

# nabla_NablaModule class attributes and methods
nabla_NablaModule_name: Property = Property(name="name", type=StringType)
nabla_NablaModule.attributes={nabla_NablaModule_name}

# nabla_SimpleVarDefinition class attributes and methods

# nabla_VarGroupDeclaration class attributes and methods

# nabla_TimeIteratorDefinition class attributes and methods

# nabla_Import class attributes and methods
nabla_Import_importedNamespace: Property = Property(name="importedNamespace", type=StringType)
nabla_Import.attributes={nabla_Import_importedNamespace}

# nabla_ItemType class attributes and methods
nabla_ItemType_name: Property = Property(name="name", type=StringType)
nabla_ItemType.attributes={nabla_ItemType_name}

# nabla_Connectivity class attributes and methods
nabla_Connectivity_name: Property = Property(name="name", type=StringType)
nabla_Connectivity.attributes={nabla_Connectivity_name}

# nabla_Reduction class attributes and methods

# nabla_Function class attributes and methods
nabla_Function_external: Property = Property(name="external", type=BooleanType)
nabla_Function.attributes={nabla_Function_external}

# nabla_OptDefinition class attributes and methods

# nabla_SimpleVar class attributes and methods

# nabla_Expression class attributes and methods

# nabla_Job class attributes and methods
nabla_Job_name: Property = Property(name="name", type=StringType)
nabla_Job.attributes={nabla_Job_name}

# nabla_SingleConnectivity class attributes and methods

# nabla_MultipleConnectivity class attributes and methods

# Connectivity class attributes and methods

# nabla_Instruction class attributes and methods

# nabla_Iterable class attributes and methods

# nabla_IterationBlock class attributes and methods

# Instruction class attributes and methods

# nabla_Affectation class attributes and methods

# nabla_ArgOrVarRef class attributes and methods

# nabla_BaseType class attributes and methods
nabla_BaseType_primitive: Property = Property(name="primitive", type=StringType)
nabla_BaseType.attributes={nabla_BaseType_primitive}

# nabla_Var class attributes and methods

# nabla_InstructionBlock class attributes and methods

# nabla_Loop class attributes and methods

# Iterable class attributes and methods

# nabla_ItemDefinition class attributes and methods

# nabla_Item class attributes and methods
nabla_Item_name: Property = Property(name="name", type=StringType)
nabla_Item.attributes={nabla_Item_name}

# nabla_If class attributes and methods

# nabla_Exit class attributes and methods
nabla_Exit_message: Property = Property(name="message", type=StringType)
nabla_Exit.attributes={nabla_Exit_message}

# nabla_Container class attributes and methods

# nabla_SingleConnectivityCall class attributes and methods

# nabla_SetDefinition class attributes and methods
nabla_SetDefinition_name: Property = Property(name="name", type=StringType)
nabla_SetDefinition.attributes={nabla_SetDefinition_name}

# nabla_MultipleConnectivityCall class attributes and methods

# nabla_Return class attributes and methods

# nabla_SingletonDefinition class attributes and methods

# nabla_SetRef class attributes and methods

# Container class attributes and methods

# nabla_SpaceIterator class attributes and methods

# IterationBlock class attributes and methods

# nabla_Interval class attributes and methods
nabla_Interval_from: Property = Property(name="from", type=IntegerType)
nabla_Interval.attributes={nabla_Interval_from}

# nabla_ConnectivityCall class attributes and methods

# nabla_ItemRef class attributes and methods
nabla_ItemRef_inc: Property = Property(name="inc", type=IntegerType)
nabla_ItemRef_dec: Property = Property(name="dec", type=IntegerType)
nabla_ItemRef.attributes={nabla_ItemRef_dec, nabla_ItemRef_inc}

# ConnectivityCall class attributes and methods

# nabla_TimeIteratorRef class attributes and methods

# nabla_TimeIterator class attributes and methods

# ArgOrVar class attributes and methods

# nabla_ArgOrVar class attributes and methods
nabla_ArgOrVar_name: Property = Property(name="name", type=StringType)
nabla_ArgOrVar.attributes={nabla_ArgOrVar_name}

# nabla_CurrentTimeIteratorRef class attributes and methods

# TimeIteratorRef class attributes and methods

# nabla_InitTimeIteratorRef class attributes and methods
nabla_InitTimeIteratorRef_value: Property = Property(name="value", type=IntegerType)
nabla_InitTimeIteratorRef.attributes={nabla_InitTimeIteratorRef_value}

# nabla_NextTimeIteratorRef class attributes and methods
nabla_NextTimeIteratorRef_value: Property = Property(name="value", type=IntegerType)
nabla_NextTimeIteratorRef.attributes={nabla_NextTimeIteratorRef_value}

# Var class attributes and methods

# nabla_ConnectivityVar class attributes and methods

# nabla_FunctionOrReduction class attributes and methods
nabla_FunctionOrReduction_name: Property = Property(name="name", type=StringType)
nabla_FunctionOrReduction.attributes={nabla_FunctionOrReduction_name}

# nabla_Arg class attributes and methods

# FunctionOrReduction class attributes and methods

# nabla_IntConstant class attributes and methods
nabla_IntConstant_value: Property = Property(name="value", type=IntegerType)
nabla_IntConstant.attributes={nabla_IntConstant_value}

# Expression class attributes and methods

# nabla_ReductionCall class attributes and methods

# nabla_ContractedIf class attributes and methods

# nabla_And class attributes and methods
nabla_And_op: Property = Property(name="op", type=StringType)
nabla_And.attributes={nabla_And_op}

# nabla_Or class attributes and methods
nabla_Or_op: Property = Property(name="op", type=StringType)
nabla_Or.attributes={nabla_Or_op}

# nabla_Comparison class attributes and methods
nabla_Comparison_op: Property = Property(name="op", type=StringType)
nabla_Comparison.attributes={nabla_Comparison_op}

# nabla_Equality class attributes and methods
nabla_Equality_op: Property = Property(name="op", type=StringType)
nabla_Equality.attributes={nabla_Equality_op}

# nabla_Minus class attributes and methods
nabla_Minus_op: Property = Property(name="op", type=StringType)
nabla_Minus.attributes={nabla_Minus_op}

# nabla_Plus class attributes and methods
nabla_Plus_op: Property = Property(name="op", type=StringType)
nabla_Plus.attributes={nabla_Plus_op}

# nabla_Mul class attributes and methods
nabla_Mul_op: Property = Property(name="op", type=StringType)
nabla_Mul.attributes={nabla_Mul_op}

# nabla_Div class attributes and methods
nabla_Div_op: Property = Property(name="op", type=StringType)
nabla_Div.attributes={nabla_Div_op}

# nabla_UnaryMinus class attributes and methods

# nabla_Modulo class attributes and methods
nabla_Modulo_op: Property = Property(name="op", type=StringType)
nabla_Modulo.attributes={nabla_Modulo_op}

# nabla_Parenthesis class attributes and methods

# nabla_MaxConstant class attributes and methods
nabla_MaxConstant_type: Property = Property(name="type", type=StringType)
nabla_MaxConstant.attributes={nabla_MaxConstant_type}

# nabla_Not class attributes and methods

# nabla_RealConstant class attributes and methods
nabla_RealConstant_value: Property = Property(name="value", type=FloatType)
nabla_RealConstant.attributes={nabla_RealConstant_value}

# nabla_BoolConstant class attributes and methods
nabla_BoolConstant_value: Property = Property(name="value", type=BooleanType)
nabla_BoolConstant.attributes={nabla_BoolConstant_value}

# nabla_MinConstant class attributes and methods
nabla_MinConstant_type: Property = Property(name="type", type=StringType)
nabla_MinConstant.attributes={nabla_MinConstant_type}

# nabla_VectorConstant class attributes and methods

# nabla_FunctionCall class attributes and methods

# nabla_BaseTypeConstant class attributes and methods

# nabla_Cardinality class attributes and methods

# Relationships
options9: BinaryAssociation = BinaryAssociation(
    name="options9",
    ends={
        Property(name="nabla_OptDefinition", type=nabla_NablaModule, multiplicity=Multiplicity(1, 1)),
        Property(name="nabla_NablaModule10", type=nabla_OptDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
definitions11: BinaryAssociation = BinaryAssociation(
    name="definitions11",
    ends={
        Property(name="nabla_SimpleVarDefinition", type=nabla_NablaModule, multiplicity=Multiplicity(1, 1)),
        Property(name="nabla_NablaModule12", type=nabla_SimpleVarDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
declarations13: BinaryAssociation = BinaryAssociation(
    name="declarations13",
    ends={
        Property(name="nabla_VarGroupDeclaration", type=nabla_NablaModule, multiplicity=Multiplicity(1, 1)),
        Property(name="nabla_NablaModule14", type=nabla_VarGroupDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
iteration15: BinaryAssociation = BinaryAssociation(
    name="iteration15",
    ends={
        Property(name="nabla_TimeIteratorDefinition", type=nabla_NablaModule, multiplicity=Multiplicity(1, 1)),
        Property(name="nabla_NablaModule16", type=nabla_TimeIteratorDefinition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
imports0: BinaryAssociation = BinaryAssociation(
    name="imports0",
    ends={
        Property(name="nabla_Import", type=nabla_NablaModule, multiplicity=Multiplicity(1, 1)),
        Property(name="nabla_NablaModule", type=nabla_Import, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
itemTypes1: BinaryAssociation = BinaryAssociation(
    name="itemTypes1",
    ends={
        Property(name="nabla_ItemType", type=nabla_NablaModule, multiplicity=Multiplicity(1, 1)),
        Property(name="nabla_NablaModule2", type=nabla_ItemType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
connectivities3: BinaryAssociation = BinaryAssociation(
    name="connectivities3",
    ends={
        Property(name="nabla_Connectivity", type=nabla_NablaModule, multiplicity=Multiplicity(1, 1)),
        Property(name="nabla_NablaModule4", type=nabla_Connectivity, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reductions5: BinaryAssociation = BinaryAssociation(
    name="reductions5",
    ends={
        Property(name="nabla_Reduction", type=nabla_NablaModule, multiplicity=Multiplicity(1, 1)),
        Property(name="nabla_NablaModule6", type=nabla_Reduction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
functions7: BinaryAssociation = BinaryAssociation(
    name="functions7",
    ends={
        Property(name="nabla_Function", type=nabla_NablaModule, multiplicity=Multiplicity(1, 1)),
        Property(name="nabla_NablaModule8", type=nabla_Function, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variable19: BinaryAssociation = BinaryAssociation(
    name="variable19",
    ends={
        Property(name="nabla_SimpleVar", type=nabla_OptDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="nabla_OptDefinition20", type=nabla_SimpleVar, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value21: BinaryAssociation = BinaryAssociation(
    name="value21",
    ends={
        Property(name="nabla_Expression", type=nabla_OptDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="nabla_OptDefinition22", type=nabla_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
jobs17: BinaryAssociation = BinaryAssociation(
    name="jobs17",
    ends={
        Property(name="nabla_Job", type=nabla_NablaModule, multiplicity=Multiplicity(1, 1)),
        Property(name="nabla_NablaModule18", type=nabla_Job, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inTypes23: BinaryAssociation = BinaryAssociation(
    name="inTypes23",
    ends={
        Property(name="nabla_ItemType25", type=nabla_Connectivity, multiplicity=Multiplicity(1, 1)),
        Property(name="nabla_Connectivity24", type=nabla_ItemType, multiplicity=Multiplicity(0, 9999))
    }
)
returnType26: BinaryAssociation = BinaryAssociation(
    name="returnType26",
    ends={
        Property(name="nabla_ItemType28", type=nabla_Connectivity, multiplicity=Multiplicity(1, 1)),
        Property(name="nabla_Connectivity27", type=nabla_ItemType, multiplicity=Multiplicity(0, 1))
    }
)
value35: BinaryAssociation = BinaryAssociation(
    name="value35",
    ends={
        Property(name="nabla_Expression37", type=nabla_SimpleVarDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="nabla_SimpleVarDefinition36", type=nabla_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
instruction29: BinaryAssociation = BinaryAssociation(
    name="instruction29",
    ends={
        Property(name="nabla_Instruction", type=nabla_Job, multiplicity=Multiplicity(1, 1)),
        Property(name="nabla_Job30", type=nabla_Instruction, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
iterationBlock31: BinaryAssociation = BinaryAssociation(
    name="iterationBlock31",
    ends={
        Property(name="nabla_IterationBlock", type=nabla_Iterable, multiplicity=Multiplicity(1, 1)),
        Property(name="nabla_Iterable", type=nabla_IterationBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable32: BinaryAssociation = BinaryAssociation(
    name="variable32",
    ends={
        Property(name="nabla_SimpleVar34", type=nabla_SimpleVarDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="nabla_SimpleVarDefinition33", type=nabla_SimpleVar, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body44: BinaryAssociation = BinaryAssociation(
    name="body44",
    ends={
        Property(name="nabla_Instruction45", type=nabla_Loop, multiplicity=Multiplicity(1, 1)),
        Property(name="nabla_Loop", type=nabla_Instruction, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type38: BinaryAssociation = BinaryAssociation(
    name="type38",
    ends={
        Property(name="nabla_BaseType", type=nabla_VarGroupDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="nabla_VarGroupDeclaration39", type=nabla_BaseType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variables40: BinaryAssociation = BinaryAssociation(
    name="variables40",
    ends={
        Property(name="nabla_Var", type=nabla_VarGroupDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="nabla_VarGroupDeclaration41", type=nabla_Var, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
instructions42: BinaryAssociation = BinaryAssociation(
    name="instructions42",
    ends={
        Property(name="nabla_Instruction43", type=nabla_InstructionBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="nabla_InstructionBlock", type=nabla_Instruction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
item58: BinaryAssociation = BinaryAssociation(
    name="item58",
    ends={
        Property(name="nabla_Item", type=nabla_ItemDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="nabla_ItemDefinition", type=nabla_Item, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left46: BinaryAssociation = BinaryAssociation(
    name="left46",
    ends={
        Property(name="nabla_ArgOrVarRef", type=nabla_Affectation, multiplicity=Multiplicity(1, 1)),
        Property(name="nabla_Affectation", type=nabla_ArgOrVarRef, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right47: BinaryAssociation = BinaryAssociation(
    name="right47",
    ends={
        Property(name="nabla_Expression49", type=nabla_Affectation, multiplicity=Multiplicity(1, 1)),
        Property(name="nabla_Affectation48", type=nabla_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition50: BinaryAssociation = BinaryAssociation(
    name="condition50",
    ends={
        Property(name="nabla_Expression51", type=nabla_If, multiplicity=Multiplicity(1, 1)),
        Property(name="nabla_If", type=nabla_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
then52: BinaryAssociation = BinaryAssociation(
    name="then52",
    ends={
        Property(name="nabla_Instruction54", type=nabla_If, multiplicity=Multiplicity(1, 1)),
        Property(name="nabla_If53", type=nabla_Instruction, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
else55: BinaryAssociation = BinaryAssociation(
    name="else55",
    ends={
        Property(name="nabla_Instruction57", type=nabla_If, multiplicity=Multiplicity(1, 1)),
        Property(name="nabla_If56", type=nabla_Instruction, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value59: BinaryAssociation = BinaryAssociation(
    name="value59",
    ends={
        Property(name="nabla_SingleConnectivityCall", type=nabla_ItemDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="nabla_ItemDefinition60", type=nabla_SingleConnectivityCall, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value61: BinaryAssociation = BinaryAssociation(
    name="value61",
    ends={
        Property(name="nabla_MultipleConnectivityCall", type=nabla_SetDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="nabla_SetDefinition", type=nabla_MultipleConnectivityCall, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression62: BinaryAssociation = BinaryAssociation(
    name="expression62",
    ends={
        Property(name="nabla_Expression63", type=nabla_Return, multiplicity=Multiplicity(1, 1)),
        Property(name="nabla_Return", type=nabla_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
container71: BinaryAssociation = BinaryAssociation(
    name="container71",
    ends={
        Property(name="nabla_Container", type=nabla_SpaceIterator, multiplicity=Multiplicity(1, 1)),
        Property(name="nabla_SpaceIterator72", type=nabla_Container, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
singletons73: BinaryAssociation = BinaryAssociation(
    name="singletons73",
    ends={
        Property(name="nabla_SingletonDefinition", type=nabla_SpaceIterator, multiplicity=Multiplicity(1, 1)),
        Property(name="nabla_SpaceIterator74", type=nabla_SingletonDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target64: BinaryAssociation = BinaryAssociation(
    name="target64",
    ends={
        Property(name="nabla_SetDefinition65", type=nabla_SetRef, multiplicity=Multiplicity(1, 1)),
        Property(name="nabla_SetRef", type=nabla_SetDefinition, multiplicity=Multiplicity(0, 1))
    }
)
item66: BinaryAssociation = BinaryAssociation(
    name="item66",
    ends={
        Property(name="nabla_Item67", type=nabla_SpaceIterator, multiplicity=Multiplicity(1, 1)),
        Property(name="nabla_SpaceIterator", type=nabla_Item, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
counter68: BinaryAssociation = BinaryAssociation(
    name="counter68",
    ends={
        Property(name="nabla_SimpleVar70", type=nabla_SpaceIterator, multiplicity=Multiplicity(1, 1)),
        Property(name="nabla_SpaceIterator69", type=nabla_SimpleVar, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
index81: BinaryAssociation = BinaryAssociation(
    name="index81",
    ends={
        Property(name="nabla_Interval", type=nabla_SimpleVar, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="nabla_SimpleVar82", type=nabla_Interval, multiplicity=Multiplicity(1, 1))
    }
)
nbElems83: BinaryAssociation = BinaryAssociation(
    name="nbElems83",
    ends={
        Property(name="nabla_Expression85", type=nabla_Interval, multiplicity=Multiplicity(1, 1)),
        Property(name="nabla_Interval84", type=nabla_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
item75: BinaryAssociation = BinaryAssociation(
    name="item75",
    ends={
        Property(name="nabla_Item77", type=nabla_SingletonDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="nabla_SingletonDefinition76", type=nabla_Item, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value78: BinaryAssociation = BinaryAssociation(
    name="value78",
    ends={
        Property(name="nabla_SingleConnectivityCall80", type=nabla_SingletonDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="nabla_SingletonDefinition79", type=nabla_SingleConnectivityCall, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
connectivity89: BinaryAssociation = BinaryAssociation(
    name="connectivity89",
    ends={
        Property(name="nabla_SingleConnectivity", type=nabla_SingleConnectivityCall, multiplicity=Multiplicity(1, 1)),
        Property(name="nabla_SingleConnectivityCall90", type=nabla_SingleConnectivity, multiplicity=Multiplicity(0, 1))
    }
)
args86: BinaryAssociation = BinaryAssociation(
    name="args86",
    ends={
        Property(name="nabla_ItemRef", type=nabla_ConnectivityCall, multiplicity=Multiplicity(1, 1)),
        Property(name="nabla_ConnectivityCall", type=nabla_ItemRef, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
connectivity87: BinaryAssociation = BinaryAssociation(
    name="connectivity87",
    ends={
        Property(name="nabla_MultipleConnectivity", type=nabla_MultipleConnectivityCall, multiplicity=Multiplicity(1, 1)),
        Property(name="nabla_MultipleConnectivityCall88", type=nabla_MultipleConnectivity, multiplicity=Multiplicity(0, 1))
    }
)
cond96: BinaryAssociation = BinaryAssociation(
    name="cond96",
    ends={
        Property(name="nabla_Expression98", type=nabla_TimeIterator, multiplicity=Multiplicity(1, 1)),
        Property(name="nabla_TimeIterator97", type=nabla_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target91: BinaryAssociation = BinaryAssociation(
    name="target91",
    ends={
        Property(name="nabla_Item93", type=nabla_ItemRef, multiplicity=Multiplicity(1, 1)),
        Property(name="nabla_ItemRef92", type=nabla_Item, multiplicity=Multiplicity(0, 1))
    }
)
iterators94: BinaryAssociation = BinaryAssociation(
    name="iterators94",
    ends={
        Property(name="nabla_TimeIterator", type=nabla_TimeIteratorDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="nabla_TimeIteratorDefinition95", type=nabla_TimeIterator, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target99: BinaryAssociation = BinaryAssociation(
    name="target99",
    ends={
        Property(name="nabla_TimeIterator100", type=nabla_TimeIteratorRef, multiplicity=Multiplicity(1, 1)),
        Property(name="nabla_TimeIteratorRef", type=nabla_TimeIterator, multiplicity=Multiplicity(0, 1))
    }
)
inArgs105: BinaryAssociation = BinaryAssociation(
    name="inArgs105",
    ends={
        Property(name="nabla_Arg", type=nabla_FunctionOrReduction, multiplicity=Multiplicity(1, 1)),
        Property(name="nabla_FunctionOrReduction106", type=nabla_Arg, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body107: BinaryAssociation = BinaryAssociation(
    name="body107",
    ends={
        Property(name="nabla_Instruction109", type=nabla_FunctionOrReduction, multiplicity=Multiplicity(1, 1)),
        Property(name="nabla_FunctionOrReduction108", type=nabla_Instruction, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
supports101: BinaryAssociation = BinaryAssociation(
    name="supports101",
    ends={
        Property(name="nabla_MultipleConnectivity102", type=nabla_ConnectivityVar, multiplicity=Multiplicity(1, 1)),
        Property(name="nabla_ConnectivityVar", type=nabla_MultipleConnectivity, multiplicity=Multiplicity(0, 9999))
    }
)
vars103: BinaryAssociation = BinaryAssociation(
    name="vars103",
    ends={
        Property(name="nabla_SimpleVar104", type=nabla_FunctionOrReduction, multiplicity=Multiplicity(1, 1)),
        Property(name="nabla_FunctionOrReduction", type=nabla_SimpleVar, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
seed116: BinaryAssociation = BinaryAssociation(
    name="seed116",
    ends={
        Property(name="nabla_Expression118", type=nabla_Reduction, multiplicity=Multiplicity(1, 1)),
        Property(name="nabla_Reduction117", type=nabla_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
inTypes110: BinaryAssociation = BinaryAssociation(
    name="inTypes110",
    ends={
        Property(name="nabla_BaseType112", type=nabla_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="nabla_Function111", type=nabla_BaseType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returnType113: BinaryAssociation = BinaryAssociation(
    name="returnType113",
    ends={
        Property(name="nabla_BaseType115", type=nabla_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="nabla_Function114", type=nabla_BaseType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arg124: BinaryAssociation = BinaryAssociation(
    name="arg124",
    ends={
        Property(name="nabla_Expression126", type=nabla_ReductionCall, multiplicity=Multiplicity(1, 1)),
        Property(name="nabla_ReductionCall125", type=nabla_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target127: BinaryAssociation = BinaryAssociation(
    name="target127",
    ends={
        Property(name="nabla_ArgOrVar", type=nabla_ArgOrVarRef, multiplicity=Multiplicity(1, 1)),
        Property(name="nabla_ArgOrVarRef128", type=nabla_ArgOrVar, multiplicity=Multiplicity(0, 1))
    }
)
type119: BinaryAssociation = BinaryAssociation(
    name="type119",
    ends={
        Property(name="nabla_BaseType121", type=nabla_Reduction, multiplicity=Multiplicity(1, 1)),
        Property(name="nabla_Reduction120", type=nabla_BaseType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
reduction122: BinaryAssociation = BinaryAssociation(
    name="reduction122",
    ends={
        Property(name="nabla_Reduction123", type=nabla_ReductionCall, multiplicity=Multiplicity(1, 1)),
        Property(name="nabla_ReductionCall", type=nabla_Reduction, multiplicity=Multiplicity(0, 1))
    }
)
sizes138: BinaryAssociation = BinaryAssociation(
    name="sizes138",
    ends={
        Property(name="nabla_Expression140", type=nabla_BaseType, multiplicity=Multiplicity(1, 1)),
        Property(name="nabla_BaseType139", type=nabla_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
timeIterators129: BinaryAssociation = BinaryAssociation(
    name="timeIterators129",
    ends={
        Property(name="nabla_TimeIteratorRef131", type=nabla_ArgOrVarRef, multiplicity=Multiplicity(1, 1)),
        Property(name="nabla_ArgOrVarRef130", type=nabla_TimeIteratorRef, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
spaceIterators132: BinaryAssociation = BinaryAssociation(
    name="spaceIterators132",
    ends={
        Property(name="nabla_ItemRef134", type=nabla_ArgOrVarRef, multiplicity=Multiplicity(1, 1)),
        Property(name="nabla_ArgOrVarRef133", type=nabla_ItemRef, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
indices135: BinaryAssociation = BinaryAssociation(
    name="indices135",
    ends={
        Property(name="nabla_Expression137", type=nabla_ArgOrVarRef, multiplicity=Multiplicity(1, 1)),
        Property(name="nabla_ArgOrVarRef136", type=nabla_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
right151: BinaryAssociation = BinaryAssociation(
    name="right151",
    ends={
        Property(name="nabla_Expression153", type=nabla_Or, multiplicity=Multiplicity(1, 1)),
        Property(name="nabla_Or152", type=nabla_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition141: BinaryAssociation = BinaryAssociation(
    name="condition141",
    ends={
        Property(name="nabla_Expression142", type=nabla_ContractedIf, multiplicity=Multiplicity(1, 1)),
        Property(name="nabla_ContractedIf", type=nabla_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
then143: BinaryAssociation = BinaryAssociation(
    name="then143",
    ends={
        Property(name="nabla_Expression145", type=nabla_ContractedIf, multiplicity=Multiplicity(1, 1)),
        Property(name="nabla_ContractedIf144", type=nabla_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
else146: BinaryAssociation = BinaryAssociation(
    name="else146",
    ends={
        Property(name="nabla_Expression148", type=nabla_ContractedIf, multiplicity=Multiplicity(1, 1)),
        Property(name="nabla_ContractedIf147", type=nabla_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left149: BinaryAssociation = BinaryAssociation(
    name="left149",
    ends={
        Property(name="nabla_Expression150", type=nabla_Or, multiplicity=Multiplicity(1, 1)),
        Property(name="nabla_Or", type=nabla_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right161: BinaryAssociation = BinaryAssociation(
    name="right161",
    ends={
        Property(name="nabla_Expression163", type=nabla_Equality, multiplicity=Multiplicity(1, 1)),
        Property(name="nabla_Equality162", type=nabla_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left164: BinaryAssociation = BinaryAssociation(
    name="left164",
    ends={
        Property(name="nabla_Expression165", type=nabla_Comparison, multiplicity=Multiplicity(1, 1)),
        Property(name="nabla_Comparison", type=nabla_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left154: BinaryAssociation = BinaryAssociation(
    name="left154",
    ends={
        Property(name="nabla_Expression155", type=nabla_And, multiplicity=Multiplicity(1, 1)),
        Property(name="nabla_And", type=nabla_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right156: BinaryAssociation = BinaryAssociation(
    name="right156",
    ends={
        Property(name="nabla_Expression158", type=nabla_And, multiplicity=Multiplicity(1, 1)),
        Property(name="nabla_And157", type=nabla_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left159: BinaryAssociation = BinaryAssociation(
    name="left159",
    ends={
        Property(name="nabla_Expression160", type=nabla_Equality, multiplicity=Multiplicity(1, 1)),
        Property(name="nabla_Equality", type=nabla_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left174: BinaryAssociation = BinaryAssociation(
    name="left174",
    ends={
        Property(name="nabla_Expression175", type=nabla_Minus, multiplicity=Multiplicity(1, 1)),
        Property(name="nabla_Minus", type=nabla_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right166: BinaryAssociation = BinaryAssociation(
    name="right166",
    ends={
        Property(name="nabla_Expression168", type=nabla_Comparison, multiplicity=Multiplicity(1, 1)),
        Property(name="nabla_Comparison167", type=nabla_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left169: BinaryAssociation = BinaryAssociation(
    name="left169",
    ends={
        Property(name="nabla_Expression170", type=nabla_Plus, multiplicity=Multiplicity(1, 1)),
        Property(name="nabla_Plus", type=nabla_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right171: BinaryAssociation = BinaryAssociation(
    name="right171",
    ends={
        Property(name="nabla_Expression173", type=nabla_Plus, multiplicity=Multiplicity(1, 1)),
        Property(name="nabla_Plus172", type=nabla_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Left184: BinaryAssociation = BinaryAssociation(
    name="Left184",
    ends={
        Property(name="nabla_Expression185", type=nabla_Div, multiplicity=Multiplicity(1, 1)),
        Property(name="nabla_Div", type=nabla_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right176: BinaryAssociation = BinaryAssociation(
    name="right176",
    ends={
        Property(name="nabla_Expression178", type=nabla_Minus, multiplicity=Multiplicity(1, 1)),
        Property(name="nabla_Minus177", type=nabla_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left179: BinaryAssociation = BinaryAssociation(
    name="left179",
    ends={
        Property(name="nabla_Expression180", type=nabla_Mul, multiplicity=Multiplicity(1, 1)),
        Property(name="nabla_Mul", type=nabla_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right181: BinaryAssociation = BinaryAssociation(
    name="right181",
    ends={
        Property(name="nabla_Expression183", type=nabla_Mul, multiplicity=Multiplicity(1, 1)),
        Property(name="nabla_Mul182", type=nabla_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression194: BinaryAssociation = BinaryAssociation(
    name="expression194",
    ends={
        Property(name="nabla_Expression195", type=nabla_Parenthesis, multiplicity=Multiplicity(1, 1)),
        Property(name="nabla_Parenthesis", type=nabla_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right186: BinaryAssociation = BinaryAssociation(
    name="right186",
    ends={
        Property(name="nabla_Expression188", type=nabla_Div, multiplicity=Multiplicity(1, 1)),
        Property(name="nabla_Div187", type=nabla_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left189: BinaryAssociation = BinaryAssociation(
    name="left189",
    ends={
        Property(name="nabla_Expression190", type=nabla_Modulo, multiplicity=Multiplicity(1, 1)),
        Property(name="nabla_Modulo", type=nabla_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right191: BinaryAssociation = BinaryAssociation(
    name="right191",
    ends={
        Property(name="nabla_Expression193", type=nabla_Modulo, multiplicity=Multiplicity(1, 1)),
        Property(name="nabla_Modulo192", type=nabla_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression196: BinaryAssociation = BinaryAssociation(
    name="expression196",
    ends={
        Property(name="nabla_Expression197", type=nabla_UnaryMinus, multiplicity=Multiplicity(1, 1)),
        Property(name="nabla_UnaryMinus", type=nabla_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression198: BinaryAssociation = BinaryAssociation(
    name="expression198",
    ends={
        Property(name="nabla_Expression199", type=nabla_Not, multiplicity=Multiplicity(1, 1)),
        Property(name="nabla_Not", type=nabla_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
values210: BinaryAssociation = BinaryAssociation(
    name="values210",
    ends={
        Property(name="nabla_Expression211", type=nabla_VectorConstant, multiplicity=Multiplicity(1, 1)),
        Property(name="nabla_VectorConstant", type=nabla_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
function200: BinaryAssociation = BinaryAssociation(
    name="function200",
    ends={
        Property(name="nabla_Function201", type=nabla_FunctionCall, multiplicity=Multiplicity(1, 1)),
        Property(name="nabla_FunctionCall", type=nabla_Function, multiplicity=Multiplicity(0, 1))
    }
)
args202: BinaryAssociation = BinaryAssociation(
    name="args202",
    ends={
        Property(name="nabla_Expression204", type=nabla_FunctionCall, multiplicity=Multiplicity(1, 1)),
        Property(name="nabla_FunctionCall203", type=nabla_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type205: BinaryAssociation = BinaryAssociation(
    name="type205",
    ends={
        Property(name="nabla_BaseType206", type=nabla_BaseTypeConstant, multiplicity=Multiplicity(1, 1)),
        Property(name="nabla_BaseTypeConstant", type=nabla_BaseType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value207: BinaryAssociation = BinaryAssociation(
    name="value207",
    ends={
        Property(name="nabla_Expression209", type=nabla_BaseTypeConstant, multiplicity=Multiplicity(1, 1)),
        Property(name="nabla_BaseTypeConstant208", type=nabla_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
container212: BinaryAssociation = BinaryAssociation(
    name="container212",
    ends={
        Property(name="nabla_Container213", type=nabla_Cardinality, multiplicity=Multiplicity(1, 1)),
        Property(name="nabla_Cardinality", type=nabla_Container, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_nabla_SingleConnectivity_Connectivity = Generalization(general=Connectivity, specific=nabla_SingleConnectivity)
gen_nabla_MultipleConnectivity_Connectivity = Generalization(general=Connectivity, specific=nabla_MultipleConnectivity)
gen_nabla_VarGroupDeclaration_Instruction = Generalization(general=Instruction, specific=nabla_VarGroupDeclaration)
gen_nabla_SimpleVarDefinition_Instruction = Generalization(general=Instruction, specific=nabla_SimpleVarDefinition)
gen_nabla_Affectation_Instruction = Generalization(general=Instruction, specific=nabla_Affectation)
gen_nabla_InstructionBlock_Instruction = Generalization(general=Instruction, specific=nabla_InstructionBlock)
gen_nabla_Loop_Iterable = Generalization(general=Iterable, specific=nabla_Loop)
gen_nabla_Loop_Instruction = Generalization(general=Instruction, specific=nabla_Loop)
gen_nabla_ItemDefinition_Instruction = Generalization(general=Instruction, specific=nabla_ItemDefinition)
gen_nabla_If_Instruction = Generalization(general=Instruction, specific=nabla_If)
gen_nabla_Exit_Instruction = Generalization(general=Instruction, specific=nabla_Exit)
gen_nabla_SetDefinition_Instruction = Generalization(general=Instruction, specific=nabla_SetDefinition)
gen_nabla_Return_Instruction = Generalization(general=Instruction, specific=nabla_Return)
gen_nabla_SetRef_Container = Generalization(general=Container, specific=nabla_SetRef)
gen_nabla_SpaceIterator_IterationBlock = Generalization(general=IterationBlock, specific=nabla_SpaceIterator)
gen_nabla_Interval_IterationBlock = Generalization(general=IterationBlock, specific=nabla_Interval)
gen_nabla_MultipleConnectivityCall_Container = Generalization(general=Container, specific=nabla_MultipleConnectivityCall)
gen_nabla_MultipleConnectivityCall_ConnectivityCall = Generalization(general=ConnectivityCall, specific=nabla_MultipleConnectivityCall)
gen_nabla_SingleConnectivityCall_ConnectivityCall = Generalization(general=ConnectivityCall, specific=nabla_SingleConnectivityCall)
gen_nabla_TimeIterator_ArgOrVar = Generalization(general=ArgOrVar, specific=nabla_TimeIterator)
gen_nabla_Var_ArgOrVar = Generalization(general=ArgOrVar, specific=nabla_Var)
gen_nabla_CurrentTimeIteratorRef_TimeIteratorRef = Generalization(general=TimeIteratorRef, specific=nabla_CurrentTimeIteratorRef)
gen_nabla_InitTimeIteratorRef_TimeIteratorRef = Generalization(general=TimeIteratorRef, specific=nabla_InitTimeIteratorRef)
gen_nabla_NextTimeIteratorRef_TimeIteratorRef = Generalization(general=TimeIteratorRef, specific=nabla_NextTimeIteratorRef)
gen_nabla_SimpleVar_Var = Generalization(general=Var, specific=nabla_SimpleVar)
gen_nabla_ConnectivityVar_Var = Generalization(general=Var, specific=nabla_ConnectivityVar)
gen_nabla_Reduction_FunctionOrReduction = Generalization(general=FunctionOrReduction, specific=nabla_Reduction)
gen_nabla_Function_FunctionOrReduction = Generalization(general=FunctionOrReduction, specific=nabla_Function)
gen_nabla_ArgOrVarRef_Expression = Generalization(general=Expression, specific=nabla_ArgOrVarRef)
gen_nabla_Arg_ArgOrVar = Generalization(general=ArgOrVar, specific=nabla_Arg)
gen_nabla_IntConstant_Expression = Generalization(general=Expression, specific=nabla_IntConstant)
gen_nabla_ReductionCall_Iterable = Generalization(general=Iterable, specific=nabla_ReductionCall)
gen_nabla_ReductionCall_Expression = Generalization(general=Expression, specific=nabla_ReductionCall)
gen_nabla_ContractedIf_Expression = Generalization(general=Expression, specific=nabla_ContractedIf)
gen_nabla_And_Expression = Generalization(general=Expression, specific=nabla_And)
gen_nabla_Or_Expression = Generalization(general=Expression, specific=nabla_Or)
gen_nabla_Comparison_Expression = Generalization(general=Expression, specific=nabla_Comparison)
gen_nabla_Equality_Expression = Generalization(general=Expression, specific=nabla_Equality)
gen_nabla_Minus_Expression = Generalization(general=Expression, specific=nabla_Minus)
gen_nabla_Plus_Expression = Generalization(general=Expression, specific=nabla_Plus)
gen_nabla_Mul_Expression = Generalization(general=Expression, specific=nabla_Mul)
gen_nabla_Div_Expression = Generalization(general=Expression, specific=nabla_Div)
gen_nabla_UnaryMinus_Expression = Generalization(general=Expression, specific=nabla_UnaryMinus)
gen_nabla_Modulo_Expression = Generalization(general=Expression, specific=nabla_Modulo)
gen_nabla_Parenthesis_Expression = Generalization(general=Expression, specific=nabla_Parenthesis)
gen_nabla_MinConstant_Expression = Generalization(general=Expression, specific=nabla_MinConstant)
gen_nabla_MaxConstant_Expression = Generalization(general=Expression, specific=nabla_MaxConstant)
gen_nabla_Not_Expression = Generalization(general=Expression, specific=nabla_Not)
gen_nabla_RealConstant_Expression = Generalization(general=Expression, specific=nabla_RealConstant)
gen_nabla_BoolConstant_Expression = Generalization(general=Expression, specific=nabla_BoolConstant)
gen_nabla_VectorConstant_Expression = Generalization(general=Expression, specific=nabla_VectorConstant)
gen_nabla_FunctionCall_Expression = Generalization(general=Expression, specific=nabla_FunctionCall)
gen_nabla_BaseTypeConstant_Expression = Generalization(general=Expression, specific=nabla_BaseTypeConstant)
gen_nabla_Cardinality_Expression = Generalization(general=Expression, specific=nabla_Cardinality)

# Domain Model
domain_model = DomainModel(
    name="nabla",
    types={nabla_NablaModule, nabla_SimpleVarDefinition, nabla_VarGroupDeclaration, nabla_TimeIteratorDefinition, nabla_Import, nabla_ItemType, nabla_Connectivity, nabla_Reduction, nabla_Function, nabla_OptDefinition, nabla_SimpleVar, nabla_Expression, nabla_Job, nabla_SingleConnectivity, nabla_MultipleConnectivity, Connectivity, nabla_Instruction, nabla_Iterable, nabla_IterationBlock, Instruction, nabla_Affectation, nabla_ArgOrVarRef, nabla_BaseType, nabla_Var, nabla_InstructionBlock, nabla_Loop, Iterable, nabla_ItemDefinition, nabla_Item, nabla_If, nabla_Exit, nabla_Container, nabla_SingleConnectivityCall, nabla_SetDefinition, nabla_MultipleConnectivityCall, nabla_Return, nabla_SingletonDefinition, nabla_SetRef, Container, nabla_SpaceIterator, IterationBlock, nabla_Interval, nabla_ConnectivityCall, nabla_ItemRef, ConnectivityCall, nabla_TimeIteratorRef, nabla_TimeIterator, ArgOrVar, nabla_ArgOrVar, nabla_CurrentTimeIteratorRef, TimeIteratorRef, nabla_InitTimeIteratorRef, nabla_NextTimeIteratorRef, Var, nabla_ConnectivityVar, nabla_FunctionOrReduction, nabla_Arg, FunctionOrReduction, nabla_IntConstant, Expression, nabla_ReductionCall, nabla_ContractedIf, nabla_And, nabla_Or, nabla_Comparison, nabla_Equality, nabla_Minus, nabla_Plus, nabla_Mul, nabla_Div, nabla_UnaryMinus, nabla_Modulo, nabla_Parenthesis, nabla_MaxConstant, nabla_Not, nabla_RealConstant, nabla_BoolConstant, nabla_MinConstant, nabla_VectorConstant, nabla_FunctionCall, nabla_BaseTypeConstant, nabla_Cardinality, PrimitiveType},
    associations={options9, definitions11, declarations13, iteration15, imports0, itemTypes1, connectivities3, reductions5, functions7, variable19, value21, jobs17, inTypes23, returnType26, value35, instruction29, iterationBlock31, variable32, body44, type38, variables40, instructions42, item58, left46, right47, condition50, then52, else55, value59, value61, expression62, container71, singletons73, target64, item66, counter68, index81, nbElems83, item75, value78, connectivity89, args86, connectivity87, cond96, target91, iterators94, target99, inArgs105, body107, supports101, vars103, seed116, inTypes110, returnType113, arg124, target127, type119, reduction122, sizes138, timeIterators129, spaceIterators132, indices135, right151, condition141, then143, else146, left149, right161, left164, left154, right156, left159, left174, right166, left169, right171, Left184, right176, left179, right181, expression194, right186, left189, right191, expression196, expression198, values210, function200, args202, type205, value207, container212},
    generalizations={gen_nabla_SingleConnectivity_Connectivity, gen_nabla_MultipleConnectivity_Connectivity, gen_nabla_VarGroupDeclaration_Instruction, gen_nabla_SimpleVarDefinition_Instruction, gen_nabla_Affectation_Instruction, gen_nabla_InstructionBlock_Instruction, gen_nabla_Loop_Iterable, gen_nabla_Loop_Instruction, gen_nabla_ItemDefinition_Instruction, gen_nabla_If_Instruction, gen_nabla_Exit_Instruction, gen_nabla_SetDefinition_Instruction, gen_nabla_Return_Instruction, gen_nabla_SetRef_Container, gen_nabla_SpaceIterator_IterationBlock, gen_nabla_Interval_IterationBlock, gen_nabla_MultipleConnectivityCall_Container, gen_nabla_MultipleConnectivityCall_ConnectivityCall, gen_nabla_SingleConnectivityCall_ConnectivityCall, gen_nabla_TimeIterator_ArgOrVar, gen_nabla_Var_ArgOrVar, gen_nabla_CurrentTimeIteratorRef_TimeIteratorRef, gen_nabla_InitTimeIteratorRef_TimeIteratorRef, gen_nabla_NextTimeIteratorRef_TimeIteratorRef, gen_nabla_SimpleVar_Var, gen_nabla_ConnectivityVar_Var, gen_nabla_Reduction_FunctionOrReduction, gen_nabla_Function_FunctionOrReduction, gen_nabla_ArgOrVarRef_Expression, gen_nabla_Arg_ArgOrVar, gen_nabla_IntConstant_Expression, gen_nabla_ReductionCall_Iterable, gen_nabla_ReductionCall_Expression, gen_nabla_ContractedIf_Expression, gen_nabla_And_Expression, gen_nabla_Or_Expression, gen_nabla_Comparison_Expression, gen_nabla_Equality_Expression, gen_nabla_Minus_Expression, gen_nabla_Plus_Expression, gen_nabla_Mul_Expression, gen_nabla_Div_Expression, gen_nabla_UnaryMinus_Expression, gen_nabla_Modulo_Expression, gen_nabla_Parenthesis_Expression, gen_nabla_MinConstant_Expression, gen_nabla_MaxConstant_Expression, gen_nabla_Not_Expression, gen_nabla_RealConstant_Expression, gen_nabla_BoolConstant_Expression, gen_nabla_VectorConstant_Expression, gen_nabla_FunctionCall_Expression, gen_nabla_BaseTypeConstant_Expression, gen_nabla_Cardinality_Expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)