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
Operator: Enumeration = Enumeration(
    name="Operator",
    literals={
            EnumerationLiteral(name="equals"),
			EnumerationLiteral(name="different"),
			EnumerationLiteral(name="in"),
			EnumerationLiteral(name="is"),
			EnumerationLiteral(name="not"),
			EnumerationLiteral(name="gt"),
			EnumerationLiteral(name="gte"),
			EnumerationLiteral(name="lt"),
			EnumerationLiteral(name="lte")
    }
)

Repeat: Enumeration = Enumeration(
    name="Repeat",
    literals={
            EnumerationLiteral(name="yes"),
			EnumerationLiteral(name="no")
    }
)

LogicOperator: Enumeration = Enumeration(
    name="LogicOperator",
    literals={
            EnumerationLiteral(name="and"),
			EnumerationLiteral(name="or")
    }
)

ArithmeticOperator: Enumeration = Enumeration(
    name="ArithmeticOperator",
    literals={
            EnumerationLiteral(name="module"),
			EnumerationLiteral(name="add"),
			EnumerationLiteral(name="subtract"),
			EnumerationLiteral(name="multiply"),
			EnumerationLiteral(name="divide")
    }
)

SampleClause: Enumeration = Enumeration(
    name="SampleClause",
    literals={
            EnumerationLiteral(name="equals"),
			EnumerationLiteral(name="distinct")
    }
)

# Classes
mutatorenvironment_MutatorEnvironment = Class(name="mutatorenvironment::MutatorEnvironment")
mutatorenvironment_Definition = Class(name="mutatorenvironment::Definition", is_abstract=True)
mutatorenvironment_Mutator = Class(name="mutatorenvironment::Mutator", is_abstract=True)
mutatorenvironment_Load = Class(name="mutatorenvironment::Load")
mutatorenvironment_Block = Class(name="mutatorenvironment::Block")
mutatorenvironment_Constraint = Class(name="mutatorenvironment::Constraint")
mutatorenvironment_Library = Class(name="mutatorenvironment::Library")
Definition = Class(name="Definition")
mutatorenvironment_Program = Class(name="mutatorenvironment::Program")
mutatorenvironment_Resource = Class(name="mutatorenvironment::Resource")
mutatorenvironment_ObjectEmitter = Class(name="mutatorenvironment::ObjectEmitter", is_abstract=True)
mutatorenvironment_EClass = Class(name="mutatorenvironment::EClass")
ObjectEmitter = Class(name="ObjectEmitter")
mutatorenvironment_CompositeMutator = Class(name="mutatorenvironment::CompositeMutator")
Mutator = Class(name="Mutator")
mutatorenvironment_CreateObjectMutator = Class(name="mutatorenvironment::CreateObjectMutator")
mutatorenvironment_ObSelectionStrategy = Class(name="mutatorenvironment::ObSelectionStrategy", is_abstract=True)
mutatorenvironment_AttributeSet = Class(name="mutatorenvironment::AttributeSet")
mutatorenvironment_ReferenceSet = Class(name="mutatorenvironment::ReferenceSet")
mutatorenvironment_EReference = Class(name="mutatorenvironment::EReference")
mutatorenvironment_Expression = Class(name="mutatorenvironment::Expression")
mutatorenvironment_Source = Class(name="mutatorenvironment::Source")
mutatorenvironment_SpecificObjectSelection = Class(name="mutatorenvironment::SpecificObjectSelection")
SpecificSelection = Class(name="SpecificSelection")
mutatorenvironment_AttributeScalar = Class(name="mutatorenvironment::AttributeScalar")
AttributeSet = Class(name="AttributeSet")
mutatorenvironment_AttributeType = Class(name="mutatorenvironment::AttributeType", is_abstract=True)
AttributeEvaluationType = Class(name="AttributeEvaluationType")
mutatorenvironment_BooleanType = Class(name="mutatorenvironment::BooleanType", is_abstract=True)
AttributeType = Class(name="AttributeType")
mutatorenvironment_SpecificBooleanType = Class(name="mutatorenvironment::SpecificBooleanType")
BooleanType = Class(name="BooleanType")
mutatorenvironment_RandomBooleanType = Class(name="mutatorenvironment::RandomBooleanType")
mutatorenvironment_StringType = Class(name="mutatorenvironment::StringType", is_abstract=True)
mutatorenvironment_SpecificStringType = Class(name="mutatorenvironment::SpecificStringType")
StringType = Class(name="StringType")
mutatorenvironment_RandomStringType = Class(name="mutatorenvironment::RandomStringType")
mutatorenvironment_IntegerType = Class(name="mutatorenvironment::IntegerType", is_abstract=True)
NumberType = Class(name="NumberType")
mutatorenvironment_SpecificIntegerType = Class(name="mutatorenvironment::SpecificIntegerType")
IntegerType = Class(name="IntegerType")
mutatorenvironment_RandomIntegerType = Class(name="mutatorenvironment::RandomIntegerType")
mutatorenvironment_RandomSelection = Class(name="mutatorenvironment::RandomSelection", is_abstract=True)
ObSelectionStrategy = Class(name="ObSelectionStrategy")
mutatorenvironment_RandomTypeSelection = Class(name="mutatorenvironment::RandomTypeSelection")
RandomSelection = Class(name="RandomSelection")
mutatorenvironment_ModifySourceReferenceMutator = Class(name="mutatorenvironment::ModifySourceReferenceMutator")
mutatorenvironment_SpecificSelection = Class(name="mutatorenvironment::SpecificSelection", is_abstract=True)
mutatorenvironment_SpecificReferenceSelection = Class(name="mutatorenvironment::SpecificReferenceSelection")
mutatorenvironment_ModifyTargetReferenceMutator = Class(name="mutatorenvironment::ModifyTargetReferenceMutator")
mutatorenvironment_CreateReferenceMutator = Class(name="mutatorenvironment::CreateReferenceMutator")
mutatorenvironment_RemoveObjectMutator = Class(name="mutatorenvironment::RemoveObjectMutator")
mutatorenvironment_DoubleType = Class(name="mutatorenvironment::DoubleType", is_abstract=True)
mutatorenvironment_SpecificDoubleType = Class(name="mutatorenvironment::SpecificDoubleType")
DoubleType = Class(name="DoubleType")
mutatorenvironment_RandomDoubleType = Class(name="mutatorenvironment::RandomDoubleType")
mutatorenvironment_ModifyInformationMutator = Class(name="mutatorenvironment::ModifyInformationMutator")
mutatorenvironment_UpperStringType = Class(name="mutatorenvironment::UpperStringType")
mutatorenvironment_LowerStringType = Class(name="mutatorenvironment::LowerStringType")
mutatorenvironment_ListStringType = Class(name="mutatorenvironment::ListStringType")
mutatorenvironment_CatStartStringType = Class(name="mutatorenvironment::CatStartStringType")
mutatorenvironment_CatEndStringType = Class(name="mutatorenvironment::CatEndStringType")
mutatorenvironment_AttributeUnset = Class(name="mutatorenvironment::AttributeUnset")
mutatorenvironment_EAttribute = Class(name="mutatorenvironment::EAttribute")
mutatorenvironment_AttributeSwap = Class(name="mutatorenvironment::AttributeSwap")
mutatorenvironment_RemoveReferenceMutator = Class(name="mutatorenvironment::RemoveReferenceMutator", is_abstract=True)
mutatorenvironment_AttributeCopy = Class(name="mutatorenvironment::AttributeCopy")
mutatorenvironment_RemoveRandomReferenceMutator = Class(name="mutatorenvironment::RemoveRandomReferenceMutator")
RemoveReferenceMutator = Class(name="RemoveReferenceMutator")
mutatorenvironment_RemoveSpecificReferenceMutator = Class(name="mutatorenvironment::RemoveSpecificReferenceMutator")
mutatorenvironment_CompleteSelection = Class(name="mutatorenvironment::CompleteSelection")
mutatorenvironment_CompleteTypeSelection = Class(name="mutatorenvironment::CompleteTypeSelection")
CompleteSelection = Class(name="CompleteSelection")
mutatorenvironment_RemoveCompleteReferenceMutator = Class(name="mutatorenvironment::RemoveCompleteReferenceMutator")
mutatorenvironment_ReplaceStringType = Class(name="mutatorenvironment::ReplaceStringType")
OtherSelection = Class(name="OtherSelection")
mutatorenvironment_SelectObjectMutator = Class(name="mutatorenvironment::SelectObjectMutator")
mutatorenvironment_AttributeEvaluation = Class(name="mutatorenvironment::AttributeEvaluation")
Evaluation = Class(name="Evaluation")
mutatorenvironment_AttributeEvaluationType = Class(name="mutatorenvironment::AttributeEvaluationType", is_abstract=True)
mutatorenvironment_AttributeReverse = Class(name="mutatorenvironment::AttributeReverse")
mutatorenvironment_OtherSelection = Class(name="mutatorenvironment::OtherSelection")
mutatorenvironment_OtherTypeSelection = Class(name="mutatorenvironment::OtherTypeSelection")
mutatorenvironment_ReferenceEvaluation = Class(name="mutatorenvironment::ReferenceEvaluation")
mutatorenvironment_Evaluation = Class(name="mutatorenvironment::Evaluation", is_abstract=True)
mutatorenvironment_BinaryOperator = Class(name="mutatorenvironment::BinaryOperator")
mutatorenvironment_ReferenceInit = Class(name="mutatorenvironment::ReferenceInit")
ReferenceSet = Class(name="ReferenceSet")
mutatorenvironment_ReferenceAtt = Class(name="mutatorenvironment::ReferenceAtt")
InvariantCS = Class(name="InvariantCS")
mutatorenvironment_RandomType = Class(name="mutatorenvironment::RandomType")
mutatorenvironment_ReferenceSwap = Class(name="mutatorenvironment::ReferenceSwap")
mutatorenvironment_ListType = Class(name="mutatorenvironment::ListType")
mutatorenvironment_EObject = Class(name="mutatorenvironment::EObject")
mutatorenvironment_ObjectAttributeType = Class(name="mutatorenvironment::ObjectAttributeType")
mutatorenvironment_MinValueType = Class(name="mutatorenvironment::MinValueType")
mutatorenvironment_MaxValueType = Class(name="mutatorenvironment::MaxValueType")
mutatorenvironment_NumberType = Class(name="mutatorenvironment::NumberType", is_abstract=True)
mutatorenvironment_AttributeOperation = Class(name="mutatorenvironment::AttributeOperation")
mutatorenvironment_CloneObjectMutator = Class(name="mutatorenvironment::CloneObjectMutator")
mutatorenvironment_RandomNumberType = Class(name="mutatorenvironment::RandomNumberType", is_abstract=True)
mutatorenvironment_RandomDoubleNumberType = Class(name="mutatorenvironment::RandomDoubleNumberType")
RandomNumberType = Class(name="RandomNumberType")
mutatorenvironment_RandomIntegerNumberType = Class(name="mutatorenvironment::RandomIntegerNumberType")
mutatorenvironment_SpecificClosureSelection = Class(name="mutatorenvironment::SpecificClosureSelection")
mutatorenvironment_SelectSampleMutator = Class(name="mutatorenvironment::SelectSampleMutator")
mutatorenvironment_EStructuralFeature = Class(name="mutatorenvironment::EStructuralFeature")
mutatorenvironment_ReferenceAdd = Class(name="mutatorenvironment::ReferenceAdd")
mutatorenvironment_ReferenceRemove = Class(name="mutatorenvironment::ReferenceRemove")
mutatorenvironment_RetypeObjectMutator = Class(name="mutatorenvironment::RetypeObjectMutator")
mutatorenvironment_TypedSelection = Class(name="mutatorenvironment::TypedSelection")
mutatorenvironment_RandomStringNumberType = Class(name="mutatorenvironment::RandomStringNumberType")
mutatorenvironment_miniOCL_RootCS = Class(name="mutatorenvironment::miniOCL::RootCS")
PackageCS = Class(name="PackageCS")
ConstraintCS = Class(name="ConstraintCS")
mutatorenvironment_miniOCL_PackageCS = Class(name="mutatorenvironment::miniOCL::PackageCS")
ClassCS = Class(name="ClassCS")
mutatorenvironment_miniOCL_ClassCS = Class(name="mutatorenvironment::miniOCL::ClassCS")
PathNameCS = Class(name="PathNameCS")
PropertyCS = Class(name="PropertyCS")
mutatorenvironment_miniOCL_PropertyCS = Class(name="mutatorenvironment::miniOCL::PropertyCS")
CallExpCS = Class(name="CallExpCS")
mutatorenvironment_miniOCL_CallExpCS = Class(name="mutatorenvironment::miniOCL::CallExpCS")
mutatorenvironment_miniOCL_OperationCS = Class(name="mutatorenvironment::miniOCL::OperationCS")
ParameterCS = Class(name="ParameterCS")
NavigationExpCS = Class(name="NavigationExpCS")
mutatorenvironment_miniOCL_PrimaryExpCS = Class(name="mutatorenvironment::miniOCL::PrimaryExpCS")
mutatorenvironment_miniOCL_NavigationExpCS = Class(name="mutatorenvironment::miniOCL::NavigationExpCS")
PrimaryExpCS = Class(name="PrimaryExpCS")
ExpCS = Class(name="ExpCS")
mutatorenvironment_miniOCL_NameExpCS = Class(name="mutatorenvironment::miniOCL::NameExpCS")
mutatorenvironment_miniOCL_ParameterCS = Class(name="mutatorenvironment::miniOCL::ParameterCS")
RoundedBracketClauseCS = Class(name="RoundedBracketClauseCS")
mutatorenvironment_miniOCL_ConstraintCS = Class(name="mutatorenvironment::miniOCL::ConstraintCS")
mutatorenvironment_miniOCL_InvariantCS = Class(name="mutatorenvironment::miniOCL::InvariantCS")
mutatorenvironment_miniOCL_ExpCS = Class(name="mutatorenvironment::miniOCL::ExpCS")
mutatorenvironment_miniOCL_LogicExpCS = Class(name="mutatorenvironment::miniOCL::LogicExpCS")
LogicExpCS = Class(name="LogicExpCS")
OperationCS = Class(name="OperationCS")
mutatorenvironment_miniOCL_RoundedBracketClauseCS = Class(name="mutatorenvironment::miniOCL::RoundedBracketClauseCS")
mutatorenvironment_miniOCL_LiteralExpCS = Class(name="mutatorenvironment::miniOCL::LiteralExpCS")
mutatorenvironment_miniOCL_IntLiteralExpCS = Class(name="mutatorenvironment::miniOCL::IntLiteralExpCS")
LiteralExpCS = Class(name="LiteralExpCS")
mutatorenvironment_miniOCL_StringLiteralExpCS = Class(name="mutatorenvironment::miniOCL::StringLiteralExpCS")
mutatorenvironment_miniOCL_BooleanLiteralExpCS = Class(name="mutatorenvironment::miniOCL::BooleanLiteralExpCS")
mutatorenvironment_miniOCL_PathNameCS = Class(name="mutatorenvironment::miniOCL::PathNameCS")
PathCS = Class(name="PathCS")
mutatorenvironment_miniOCL_PathCS = Class(name="mutatorenvironment::miniOCL::PathCS")
mutatorenvironment_miniOCL_PathVariableCS = Class(name="mutatorenvironment::miniOCL::PathVariableCS")
mutatorenvironment_miniOCL_LoopExpCS = Class(name="mutatorenvironment::miniOCL::LoopExpCS")
IteratorVarCS = Class(name="IteratorVarCS")
mutatorenvironment_miniOCL_CollectExpCS = Class(name="mutatorenvironment::miniOCL::CollectExpCS")
LoopExpCS = Class(name="LoopExpCS")
mutatorenvironment_miniOCL_IteratorVarCS = Class(name="mutatorenvironment::miniOCL::IteratorVarCS")
mutatorenvironment_miniOCL_IterateExpCS = Class(name="mutatorenvironment::miniOCL::IterateExpCS")
AccVarCS = Class(name="AccVarCS")
mutatorenvironment_miniOCL_AccVarCS = Class(name="mutatorenvironment::miniOCL::AccVarCS")
mutatorenvironment_miniOCL_NavigationNameExpCS = Class(name="mutatorenvironment::miniOCL::NavigationNameExpCS")
NavigationPathNameCS = Class(name="NavigationPathNameCS")
mutatorenvironment_miniOCL_NavigationPathNameCS = Class(name="mutatorenvironment::miniOCL::NavigationPathNameCS")
NavigationPathCS = Class(name="NavigationPathCS")
mutatorenvironment_miniOCL_NavigationPathCS = Class(name="mutatorenvironment::miniOCL::NavigationPathCS")
mutatorenvironment_miniOCL_NavigationPathVariableCS = Class(name="mutatorenvironment::miniOCL::NavigationPathVariableCS")
mutatorenvironment_miniOCL_NavigationPathElementCS = Class(name="mutatorenvironment::miniOCL::NavigationPathElementCS")
mutatorenvironment_miniOCL_ForAllExpCS = Class(name="mutatorenvironment::miniOCL::ForAllExpCS")
mutatorenvironment_miniOCL_PathElementCS = Class(name="mutatorenvironment::miniOCL::PathElementCS")
miniOCL_mutatorenvironment_EStructuralFeature = Class(name="miniOCL::mutatorenvironment::EStructuralFeature")
mutatorenvironment_miniOCL_BooleanExpCS = Class(name="mutatorenvironment::miniOCL::BooleanExpCS")
BooleanLiteralExpCS = Class(name="BooleanLiteralExpCS")
mutatorenvironment_miniOCL_ExistsExpCS = Class(name="mutatorenvironment::miniOCL::ExistsExpCS")

# mutatorenvironment_MutatorEnvironment class attributes and methods

# mutatorenvironment_Definition class attributes and methods
mutatorenvironment_Definition_metamodel: Property = Property(name="metamodel", type=StringType)
mutatorenvironment_Definition.attributes={mutatorenvironment_Definition_metamodel}

# mutatorenvironment_Mutator class attributes and methods
mutatorenvironment_Mutator_min: Property = Property(name="min", type=IntegerType)
mutatorenvironment_Mutator_max: Property = Property(name="max", type=IntegerType)
mutatorenvironment_Mutator_fixed: Property = Property(name="fixed", type=IntegerType)
mutatorenvironment_Mutator.attributes={mutatorenvironment_Mutator_max, mutatorenvironment_Mutator_fixed, mutatorenvironment_Mutator_min}

# mutatorenvironment_Load class attributes and methods
mutatorenvironment_Load_file: Property = Property(name="file", type=StringType)
mutatorenvironment_Load.attributes={mutatorenvironment_Load_file}

# mutatorenvironment_Block class attributes and methods
mutatorenvironment_Block_name: Property = Property(name="name", type=StringType)
mutatorenvironment_Block_repeat: Property = Property(name="repeat", type=StringType)
mutatorenvironment_Block_min: Property = Property(name="min", type=IntegerType)
mutatorenvironment_Block_max: Property = Property(name="max", type=IntegerType)
mutatorenvironment_Block_fixed: Property = Property(name="fixed", type=IntegerType)
mutatorenvironment_Block_description: Property = Property(name="description", type=StringType)
mutatorenvironment_Block.attributes={mutatorenvironment_Block_max, mutatorenvironment_Block_fixed, mutatorenvironment_Block_description, mutatorenvironment_Block_min, mutatorenvironment_Block_repeat, mutatorenvironment_Block_name}

# mutatorenvironment_Constraint class attributes and methods
mutatorenvironment_Constraint_id: Property = Property(name="id", type=StringType)
mutatorenvironment_Constraint_rules: Property = Property(name="rules", type=StringType)
mutatorenvironment_Constraint.attributes={mutatorenvironment_Constraint_rules, mutatorenvironment_Constraint_id}

# mutatorenvironment_Library class attributes and methods

# Definition class attributes and methods

# mutatorenvironment_Program class attributes and methods
mutatorenvironment_Program_output: Property = Property(name="output", type=StringType)
mutatorenvironment_Program_num: Property = Property(name="num", type=IntegerType)
mutatorenvironment_Program_description: Property = Property(name="description", type=StringType)
mutatorenvironment_Program_exhaustive: Property = Property(name="exhaustive", type=BooleanType)
mutatorenvironment_Program.attributes={mutatorenvironment_Program_num, mutatorenvironment_Program_exhaustive, mutatorenvironment_Program_output, mutatorenvironment_Program_description}

# mutatorenvironment_Resource class attributes and methods
mutatorenvironment_Resource_name: Property = Property(name="name", type=StringType)
mutatorenvironment_Resource.attributes={mutatorenvironment_Resource_name}

# mutatorenvironment_ObjectEmitter class attributes and methods
mutatorenvironment_ObjectEmitter_name: Property = Property(name="name", type=StringType)
mutatorenvironment_ObjectEmitter.attributes={mutatorenvironment_ObjectEmitter_name}

# mutatorenvironment_EClass class attributes and methods

# ObjectEmitter class attributes and methods

# mutatorenvironment_CompositeMutator class attributes and methods

# Mutator class attributes and methods

# mutatorenvironment_CreateObjectMutator class attributes and methods

# mutatorenvironment_ObSelectionStrategy class attributes and methods
mutatorenvironment_ObSelectionStrategy_resource: Property = Property(name="resource", type=StringType)
mutatorenvironment_ObSelectionStrategy.attributes={mutatorenvironment_ObSelectionStrategy_resource}

# mutatorenvironment_AttributeSet class attributes and methods

# mutatorenvironment_ReferenceSet class attributes and methods

# mutatorenvironment_EReference class attributes and methods

# mutatorenvironment_Expression class attributes and methods

# mutatorenvironment_Source class attributes and methods
mutatorenvironment_Source_path: Property = Property(name="path", type=StringType)
mutatorenvironment_Source.attributes={mutatorenvironment_Source_path}

# mutatorenvironment_SpecificObjectSelection class attributes and methods

# SpecificSelection class attributes and methods

# mutatorenvironment_AttributeScalar class attributes and methods

# AttributeSet class attributes and methods

# mutatorenvironment_AttributeType class attributes and methods
mutatorenvironment_AttributeType_operator: Property = Property(name="operator", type=StringType)
mutatorenvironment_AttributeType.attributes={mutatorenvironment_AttributeType_operator}

# AttributeEvaluationType class attributes and methods

# mutatorenvironment_BooleanType class attributes and methods

# AttributeType class attributes and methods

# mutatorenvironment_SpecificBooleanType class attributes and methods
mutatorenvironment_SpecificBooleanType_value: Property = Property(name="value", type=BooleanType)
mutatorenvironment_SpecificBooleanType.attributes={mutatorenvironment_SpecificBooleanType_value}

# BooleanType class attributes and methods

# mutatorenvironment_RandomBooleanType class attributes and methods
mutatorenvironment_RandomBooleanType_allowsNull: Property = Property(name="allowsNull", type=BooleanType)
mutatorenvironment_RandomBooleanType.attributes={mutatorenvironment_RandomBooleanType_allowsNull}

# mutatorenvironment_StringType class attributes and methods

# mutatorenvironment_SpecificStringType class attributes and methods
mutatorenvironment_SpecificStringType_value: Property = Property(name="value", type=StringType)
mutatorenvironment_SpecificStringType.attributes={mutatorenvironment_SpecificStringType_value}

# StringType class attributes and methods

# mutatorenvironment_RandomStringType class attributes and methods
mutatorenvironment_RandomStringType_min: Property = Property(name="min", type=IntegerType)
mutatorenvironment_RandomStringType_max: Property = Property(name="max", type=IntegerType)
mutatorenvironment_RandomStringType_allowsNull: Property = Property(name="allowsNull", type=BooleanType)
mutatorenvironment_RandomStringType.attributes={mutatorenvironment_RandomStringType_max, mutatorenvironment_RandomStringType_allowsNull, mutatorenvironment_RandomStringType_min}

# mutatorenvironment_IntegerType class attributes and methods

# NumberType class attributes and methods

# mutatorenvironment_SpecificIntegerType class attributes and methods
mutatorenvironment_SpecificIntegerType_value: Property = Property(name="value", type=IntegerType)
mutatorenvironment_SpecificIntegerType.attributes={mutatorenvironment_SpecificIntegerType_value}

# IntegerType class attributes and methods

# mutatorenvironment_RandomIntegerType class attributes and methods
mutatorenvironment_RandomIntegerType_min: Property = Property(name="min", type=IntegerType)
mutatorenvironment_RandomIntegerType_max: Property = Property(name="max", type=IntegerType)
mutatorenvironment_RandomIntegerType_allowsNull: Property = Property(name="allowsNull", type=BooleanType)
mutatorenvironment_RandomIntegerType.attributes={mutatorenvironment_RandomIntegerType_min, mutatorenvironment_RandomIntegerType_allowsNull, mutatorenvironment_RandomIntegerType_max}

# mutatorenvironment_RandomSelection class attributes and methods

# ObSelectionStrategy class attributes and methods

# mutatorenvironment_RandomTypeSelection class attributes and methods

# RandomSelection class attributes and methods

# mutatorenvironment_ModifySourceReferenceMutator class attributes and methods

# mutatorenvironment_SpecificSelection class attributes and methods

# mutatorenvironment_SpecificReferenceSelection class attributes and methods

# mutatorenvironment_ModifyTargetReferenceMutator class attributes and methods

# mutatorenvironment_CreateReferenceMutator class attributes and methods

# mutatorenvironment_RemoveObjectMutator class attributes and methods

# mutatorenvironment_DoubleType class attributes and methods

# mutatorenvironment_SpecificDoubleType class attributes and methods
mutatorenvironment_SpecificDoubleType_value: Property = Property(name="value", type=FloatType)
mutatorenvironment_SpecificDoubleType.attributes={mutatorenvironment_SpecificDoubleType_value}

# DoubleType class attributes and methods

# mutatorenvironment_RandomDoubleType class attributes and methods
mutatorenvironment_RandomDoubleType_max: Property = Property(name="max", type=FloatType)
mutatorenvironment_RandomDoubleType_allowsNull: Property = Property(name="allowsNull", type=BooleanType)
mutatorenvironment_RandomDoubleType_min: Property = Property(name="min", type=FloatType)
mutatorenvironment_RandomDoubleType.attributes={mutatorenvironment_RandomDoubleType_allowsNull, mutatorenvironment_RandomDoubleType_max, mutatorenvironment_RandomDoubleType_min}

# mutatorenvironment_ModifyInformationMutator class attributes and methods

# mutatorenvironment_UpperStringType class attributes and methods
mutatorenvironment_UpperStringType_value: Property = Property(name="value", type=StringType)
mutatorenvironment_UpperStringType.attributes={mutatorenvironment_UpperStringType_value}

# mutatorenvironment_LowerStringType class attributes and methods
mutatorenvironment_LowerStringType_value: Property = Property(name="value", type=StringType)
mutatorenvironment_LowerStringType.attributes={mutatorenvironment_LowerStringType_value}

# mutatorenvironment_ListStringType class attributes and methods
mutatorenvironment_ListStringType_value: Property = Property(name="value", type=StringType)
mutatorenvironment_ListStringType.attributes={mutatorenvironment_ListStringType_value}

# mutatorenvironment_CatStartStringType class attributes and methods
mutatorenvironment_CatStartStringType_value: Property = Property(name="value", type=StringType)
mutatorenvironment_CatStartStringType.attributes={mutatorenvironment_CatStartStringType_value}

# mutatorenvironment_CatEndStringType class attributes and methods
mutatorenvironment_CatEndStringType_value: Property = Property(name="value", type=StringType)
mutatorenvironment_CatEndStringType.attributes={mutatorenvironment_CatEndStringType_value}

# mutatorenvironment_AttributeUnset class attributes and methods

# mutatorenvironment_EAttribute class attributes and methods

# mutatorenvironment_AttributeSwap class attributes and methods

# mutatorenvironment_RemoveReferenceMutator class attributes and methods

# mutatorenvironment_AttributeCopy class attributes and methods

# mutatorenvironment_RemoveRandomReferenceMutator class attributes and methods

# RemoveReferenceMutator class attributes and methods

# mutatorenvironment_RemoveSpecificReferenceMutator class attributes and methods

# mutatorenvironment_CompleteSelection class attributes and methods

# mutatorenvironment_CompleteTypeSelection class attributes and methods

# CompleteSelection class attributes and methods

# mutatorenvironment_RemoveCompleteReferenceMutator class attributes and methods

# mutatorenvironment_ReplaceStringType class attributes and methods
mutatorenvironment_ReplaceStringType_newstring: Property = Property(name="newstring", type=StringType)
mutatorenvironment_ReplaceStringType_oldstring: Property = Property(name="oldstring", type=StringType)
mutatorenvironment_ReplaceStringType.attributes={mutatorenvironment_ReplaceStringType_newstring, mutatorenvironment_ReplaceStringType_oldstring}

# OtherSelection class attributes and methods

# mutatorenvironment_SelectObjectMutator class attributes and methods

# mutatorenvironment_AttributeEvaluation class attributes and methods

# Evaluation class attributes and methods

# mutatorenvironment_AttributeEvaluationType class attributes and methods

# mutatorenvironment_AttributeReverse class attributes and methods

# mutatorenvironment_OtherSelection class attributes and methods

# mutatorenvironment_OtherTypeSelection class attributes and methods

# mutatorenvironment_ReferenceEvaluation class attributes and methods
mutatorenvironment_ReferenceEvaluation_operator: Property = Property(name="operator", type=StringType)
mutatorenvironment_ReferenceEvaluation_container: Property = Property(name="container", type=BooleanType)
mutatorenvironment_ReferenceEvaluation.attributes={mutatorenvironment_ReferenceEvaluation_operator, mutatorenvironment_ReferenceEvaluation_container}

# mutatorenvironment_Evaluation class attributes and methods

# mutatorenvironment_BinaryOperator class attributes and methods
mutatorenvironment_BinaryOperator_type: Property = Property(name="type", type=StringType)
mutatorenvironment_BinaryOperator.attributes={mutatorenvironment_BinaryOperator_type}

# mutatorenvironment_ReferenceInit class attributes and methods

# ReferenceSet class attributes and methods

# mutatorenvironment_ReferenceAtt class attributes and methods

# InvariantCS class attributes and methods

# mutatorenvironment_RandomType class attributes and methods

# mutatorenvironment_ReferenceSwap class attributes and methods

# mutatorenvironment_ListType class attributes and methods

# mutatorenvironment_EObject class attributes and methods

# mutatorenvironment_ObjectAttributeType class attributes and methods
mutatorenvironment_ObjectAttributeType_operator: Property = Property(name="operator", type=StringType)
mutatorenvironment_ObjectAttributeType.attributes={mutatorenvironment_ObjectAttributeType_operator}

# mutatorenvironment_MinValueType class attributes and methods

# mutatorenvironment_MaxValueType class attributes and methods

# mutatorenvironment_NumberType class attributes and methods

# mutatorenvironment_AttributeOperation class attributes and methods
mutatorenvironment_AttributeOperation_operator: Property = Property(name="operator", type=StringType)
mutatorenvironment_AttributeOperation.attributes={mutatorenvironment_AttributeOperation_operator}

# mutatorenvironment_CloneObjectMutator class attributes and methods
mutatorenvironment_CloneObjectMutator_contents: Property = Property(name="contents", type=BooleanType)
mutatorenvironment_CloneObjectMutator.attributes={mutatorenvironment_CloneObjectMutator_contents}

# mutatorenvironment_RandomNumberType class attributes and methods

# mutatorenvironment_RandomDoubleNumberType class attributes and methods
mutatorenvironment_RandomDoubleNumberType_min: Property = Property(name="min", type=FloatType)
mutatorenvironment_RandomDoubleNumberType.attributes={mutatorenvironment_RandomDoubleNumberType_min}

# RandomNumberType class attributes and methods

# mutatorenvironment_RandomIntegerNumberType class attributes and methods
mutatorenvironment_RandomIntegerNumberType_min: Property = Property(name="min", type=IntegerType)
mutatorenvironment_RandomIntegerNumberType.attributes={mutatorenvironment_RandomIntegerNumberType_min}

# mutatorenvironment_SpecificClosureSelection class attributes and methods

# mutatorenvironment_SelectSampleMutator class attributes and methods
mutatorenvironment_SelectSampleMutator_clause: Property = Property(name="clause", type=StringType)
mutatorenvironment_SelectSampleMutator.attributes={mutatorenvironment_SelectSampleMutator_clause}

# mutatorenvironment_EStructuralFeature class attributes and methods

# mutatorenvironment_ReferenceAdd class attributes and methods

# mutatorenvironment_ReferenceRemove class attributes and methods

# mutatorenvironment_RetypeObjectMutator class attributes and methods

# mutatorenvironment_TypedSelection class attributes and methods

# mutatorenvironment_RandomStringNumberType class attributes and methods
mutatorenvironment_RandomStringNumberType_min: Property = Property(name="min", type=IntegerType)
mutatorenvironment_RandomStringNumberType_max: Property = Property(name="max", type=IntegerType)
mutatorenvironment_RandomStringNumberType_allowsNull: Property = Property(name="allowsNull", type=BooleanType)
mutatorenvironment_RandomStringNumberType.attributes={mutatorenvironment_RandomStringNumberType_allowsNull, mutatorenvironment_RandomStringNumberType_min, mutatorenvironment_RandomStringNumberType_max}

# mutatorenvironment_miniOCL_RootCS class attributes and methods

# PackageCS class attributes and methods

# ConstraintCS class attributes and methods

# mutatorenvironment_miniOCL_PackageCS class attributes and methods
mutatorenvironment_miniOCL_PackageCS_name: Property = Property(name="name", type=StringType)
mutatorenvironment_miniOCL_PackageCS.attributes={mutatorenvironment_miniOCL_PackageCS_name}

# ClassCS class attributes and methods

# mutatorenvironment_miniOCL_ClassCS class attributes and methods
mutatorenvironment_miniOCL_ClassCS_name: Property = Property(name="name", type=StringType)
mutatorenvironment_miniOCL_ClassCS.attributes={mutatorenvironment_miniOCL_ClassCS_name}

# PathNameCS class attributes and methods

# PropertyCS class attributes and methods

# mutatorenvironment_miniOCL_PropertyCS class attributes and methods
mutatorenvironment_miniOCL_PropertyCS_name: Property = Property(name="name", type=StringType)
mutatorenvironment_miniOCL_PropertyCS.attributes={mutatorenvironment_miniOCL_PropertyCS_name}

# CallExpCS class attributes and methods

# mutatorenvironment_miniOCL_CallExpCS class attributes and methods

# mutatorenvironment_miniOCL_OperationCS class attributes and methods
mutatorenvironment_miniOCL_OperationCS_name: Property = Property(name="name", type=StringType)
mutatorenvironment_miniOCL_OperationCS.attributes={mutatorenvironment_miniOCL_OperationCS_name}

# ParameterCS class attributes and methods

# NavigationExpCS class attributes and methods

# mutatorenvironment_miniOCL_PrimaryExpCS class attributes and methods

# mutatorenvironment_miniOCL_NavigationExpCS class attributes and methods

# PrimaryExpCS class attributes and methods

# ExpCS class attributes and methods

# mutatorenvironment_miniOCL_NameExpCS class attributes and methods

# mutatorenvironment_miniOCL_ParameterCS class attributes and methods
mutatorenvironment_miniOCL_ParameterCS_name: Property = Property(name="name", type=StringType)
mutatorenvironment_miniOCL_ParameterCS.attributes={mutatorenvironment_miniOCL_ParameterCS_name}

# RoundedBracketClauseCS class attributes and methods

# mutatorenvironment_miniOCL_ConstraintCS class attributes and methods

# mutatorenvironment_miniOCL_InvariantCS class attributes and methods

# mutatorenvironment_miniOCL_ExpCS class attributes and methods

# mutatorenvironment_miniOCL_LogicExpCS class attributes and methods
mutatorenvironment_miniOCL_LogicExpCS_op: Property = Property(name="op", type=StringType)
mutatorenvironment_miniOCL_LogicExpCS.attributes={mutatorenvironment_miniOCL_LogicExpCS_op}

# LogicExpCS class attributes and methods

# OperationCS class attributes and methods

# mutatorenvironment_miniOCL_RoundedBracketClauseCS class attributes and methods

# mutatorenvironment_miniOCL_LiteralExpCS class attributes and methods

# mutatorenvironment_miniOCL_IntLiteralExpCS class attributes and methods
mutatorenvironment_miniOCL_IntLiteralExpCS_intSymbol: Property = Property(name="intSymbol", type=IntegerType)
mutatorenvironment_miniOCL_IntLiteralExpCS.attributes={mutatorenvironment_miniOCL_IntLiteralExpCS_intSymbol}

# LiteralExpCS class attributes and methods

# mutatorenvironment_miniOCL_StringLiteralExpCS class attributes and methods
mutatorenvironment_miniOCL_StringLiteralExpCS_stringSymbol: Property = Property(name="stringSymbol", type=StringType)
mutatorenvironment_miniOCL_StringLiteralExpCS.attributes={mutatorenvironment_miniOCL_StringLiteralExpCS_stringSymbol}

# mutatorenvironment_miniOCL_BooleanLiteralExpCS class attributes and methods

# mutatorenvironment_miniOCL_PathNameCS class attributes and methods

# PathCS class attributes and methods

# mutatorenvironment_miniOCL_PathCS class attributes and methods

# mutatorenvironment_miniOCL_PathVariableCS class attributes and methods
mutatorenvironment_miniOCL_PathVariableCS_varName: Property = Property(name="varName", type=StringType)
mutatorenvironment_miniOCL_PathVariableCS.attributes={mutatorenvironment_miniOCL_PathVariableCS_varName}

# mutatorenvironment_miniOCL_LoopExpCS class attributes and methods
mutatorenvironment_miniOCL_LoopExpCS_logicOp: Property = Property(name="logicOp", type=StringType)
mutatorenvironment_miniOCL_LoopExpCS.attributes={mutatorenvironment_miniOCL_LoopExpCS_logicOp}

# IteratorVarCS class attributes and methods

# mutatorenvironment_miniOCL_CollectExpCS class attributes and methods

# LoopExpCS class attributes and methods

# mutatorenvironment_miniOCL_IteratorVarCS class attributes and methods
mutatorenvironment_miniOCL_IteratorVarCS_itName: Property = Property(name="itName", type=StringType)
mutatorenvironment_miniOCL_IteratorVarCS.attributes={mutatorenvironment_miniOCL_IteratorVarCS_itName}

# mutatorenvironment_miniOCL_IterateExpCS class attributes and methods

# AccVarCS class attributes and methods

# mutatorenvironment_miniOCL_AccVarCS class attributes and methods
mutatorenvironment_miniOCL_AccVarCS_accVarName: Property = Property(name="accVarName", type=StringType)
mutatorenvironment_miniOCL_AccVarCS.attributes={mutatorenvironment_miniOCL_AccVarCS_accVarName}

# mutatorenvironment_miniOCL_NavigationNameExpCS class attributes and methods

# NavigationPathNameCS class attributes and methods

# mutatorenvironment_miniOCL_NavigationPathNameCS class attributes and methods

# NavigationPathCS class attributes and methods

# mutatorenvironment_miniOCL_NavigationPathCS class attributes and methods

# mutatorenvironment_miniOCL_NavigationPathVariableCS class attributes and methods
mutatorenvironment_miniOCL_NavigationPathVariableCS_varName: Property = Property(name="varName", type=StringType)
mutatorenvironment_miniOCL_NavigationPathVariableCS.attributes={mutatorenvironment_miniOCL_NavigationPathVariableCS_varName}

# mutatorenvironment_miniOCL_NavigationPathElementCS class attributes and methods

# mutatorenvironment_miniOCL_ForAllExpCS class attributes and methods

# mutatorenvironment_miniOCL_PathElementCS class attributes and methods

# miniOCL_mutatorenvironment_EStructuralFeature class attributes and methods

# mutatorenvironment_miniOCL_BooleanExpCS class attributes and methods
mutatorenvironment_miniOCL_BooleanExpCS_boolSymbol: Property = Property(name="boolSymbol", type=BooleanType)
mutatorenvironment_miniOCL_BooleanExpCS.attributes={mutatorenvironment_miniOCL_BooleanExpCS_boolSymbol}

# BooleanLiteralExpCS class attributes and methods

# mutatorenvironment_miniOCL_ExistsExpCS class attributes and methods

# Relationships
definition0: BinaryAssociation = BinaryAssociation(
    name="definition0",
    ends={
        Property(name="mutatorenvironment_Definition", type=mutatorenvironment_MutatorEnvironment, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_MutatorEnvironment", type=mutatorenvironment_Definition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
commands1: BinaryAssociation = BinaryAssociation(
    name="commands1",
    ends={
        Property(name="mutatorenvironment_Mutator", type=mutatorenvironment_MutatorEnvironment, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_MutatorEnvironment2", type=mutatorenvironment_Mutator, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
load3: BinaryAssociation = BinaryAssociation(
    name="load3",
    ends={
        Property(name="mutatorenvironment_Load", type=mutatorenvironment_MutatorEnvironment, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_MutatorEnvironment4", type=mutatorenvironment_Load, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
blocks5: BinaryAssociation = BinaryAssociation(
    name="blocks5",
    ends={
        Property(name="mutatorenvironment_Block", type=mutatorenvironment_MutatorEnvironment, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_MutatorEnvironment6", type=mutatorenvironment_Block, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
constraints7: BinaryAssociation = BinaryAssociation(
    name="constraints7",
    ends={
        Property(name="mutatorenvironment_Constraint", type=mutatorenvironment_MutatorEnvironment, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_MutatorEnvironment8", type=mutatorenvironment_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resources10: BinaryAssociation = BinaryAssociation(
    name="resources10",
    ends={
        Property(name="mutatorenvironment_Resource", type=mutatorenvironment_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_Program11", type=mutatorenvironment_Resource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type12: BinaryAssociation = BinaryAssociation(
    name="type12",
    ends={
        Property(name="mutatorenvironment_EClass", type=mutatorenvironment_ObjectEmitter, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_ObjectEmitter", type=mutatorenvironment_EClass, multiplicity=Multiplicity(0, 1))
    }
)
types13: BinaryAssociation = BinaryAssociation(
    name="types13",
    ends={
        Property(name="mutatorenvironment_EClass15", type=mutatorenvironment_ObjectEmitter, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_ObjectEmitter14", type=mutatorenvironment_EClass, multiplicity=Multiplicity(0, 9999))
    }
)
commands16: BinaryAssociation = BinaryAssociation(
    name="commands16",
    ends={
        Property(name="mutatorenvironment_Mutator17", type=mutatorenvironment_CompositeMutator, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_CompositeMutator", type=mutatorenvironment_Mutator, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
container18: BinaryAssociation = BinaryAssociation(
    name="container18",
    ends={
        Property(name="mutatorenvironment_ObSelectionStrategy", type=mutatorenvironment_CreateObjectMutator, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_CreateObjectMutator", type=mutatorenvironment_ObSelectionStrategy, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
attributes19: BinaryAssociation = BinaryAssociation(
    name="attributes19",
    ends={
        Property(name="mutatorenvironment_AttributeSet", type=mutatorenvironment_CreateObjectMutator, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_CreateObjectMutator20", type=mutatorenvironment_AttributeSet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
references21: BinaryAssociation = BinaryAssociation(
    name="references21",
    ends={
        Property(name="mutatorenvironment_ReferenceSet", type=mutatorenvironment_CreateObjectMutator, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_CreateObjectMutator22", type=mutatorenvironment_ReferenceSet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
refType23: BinaryAssociation = BinaryAssociation(
    name="refType23",
    ends={
        Property(name="mutatorenvironment_EReference", type=mutatorenvironment_ObSelectionStrategy, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_ObSelectionStrategy24", type=mutatorenvironment_EReference, multiplicity=Multiplicity(0, 1))
    }
)
expression25: BinaryAssociation = BinaryAssociation(
    name="expression25",
    ends={
        Property(name="mutatorenvironment_Expression", type=mutatorenvironment_ObSelectionStrategy, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_ObSelectionStrategy26", type=mutatorenvironment_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
source9: BinaryAssociation = BinaryAssociation(
    name="source9",
    ends={
        Property(name="mutatorenvironment_Source", type=mutatorenvironment_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_Program", type=mutatorenvironment_Source, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
objSel33: BinaryAssociation = BinaryAssociation(
    name="objSel33",
    ends={
        Property(name="mutatorenvironment_ObjectEmitter34", type=mutatorenvironment_SpecificObjectSelection, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_SpecificObjectSelection", type=mutatorenvironment_ObjectEmitter, multiplicity=Multiplicity(1, 1))
    }
)
value35: BinaryAssociation = BinaryAssociation(
    name="value35",
    ends={
        Property(name="mutatorenvironment_AttributeType", type=mutatorenvironment_AttributeScalar, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_AttributeScalar", type=mutatorenvironment_AttributeType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
refRefType27: BinaryAssociation = BinaryAssociation(
    name="refRefType27",
    ends={
        Property(name="mutatorenvironment_EReference29", type=mutatorenvironment_ObSelectionStrategy, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_ObSelectionStrategy28", type=mutatorenvironment_EReference, multiplicity=Multiplicity(0, 1))
    }
)
refRefRefType30: BinaryAssociation = BinaryAssociation(
    name="refRefRefType30",
    ends={
        Property(name="mutatorenvironment_EReference32", type=mutatorenvironment_ObSelectionStrategy, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_ObSelectionStrategy31", type=mutatorenvironment_EReference, multiplicity=Multiplicity(0, 1))
    }
)
refType36: BinaryAssociation = BinaryAssociation(
    name="refType36",
    ends={
        Property(name="mutatorenvironment_EReference37", type=mutatorenvironment_ModifySourceReferenceMutator, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_ModifySourceReferenceMutator", type=mutatorenvironment_EReference, multiplicity=Multiplicity(0, 1))
    }
)
source38: BinaryAssociation = BinaryAssociation(
    name="source38",
    ends={
        Property(name="mutatorenvironment_ObSelectionStrategy40", type=mutatorenvironment_ModifySourceReferenceMutator, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_ModifySourceReferenceMutator39", type=mutatorenvironment_ObSelectionStrategy, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
newSource41: BinaryAssociation = BinaryAssociation(
    name="newSource41",
    ends={
        Property(name="mutatorenvironment_ObSelectionStrategy43", type=mutatorenvironment_ModifySourceReferenceMutator, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_ModifySourceReferenceMutator42", type=mutatorenvironment_ObSelectionStrategy, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
objSel44: BinaryAssociation = BinaryAssociation(
    name="objSel44",
    ends={
        Property(name="mutatorenvironment_ObjectEmitter45", type=mutatorenvironment_SpecificReferenceSelection, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_SpecificReferenceSelection", type=mutatorenvironment_ObjectEmitter, multiplicity=Multiplicity(1, 1))
    }
)
refType46: BinaryAssociation = BinaryAssociation(
    name="refType46",
    ends={
        Property(name="mutatorenvironment_EReference47", type=mutatorenvironment_ModifyTargetReferenceMutator, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_ModifyTargetReferenceMutator", type=mutatorenvironment_EReference, multiplicity=Multiplicity(0, 1))
    }
)
source48: BinaryAssociation = BinaryAssociation(
    name="source48",
    ends={
        Property(name="mutatorenvironment_ObSelectionStrategy50", type=mutatorenvironment_ModifyTargetReferenceMutator, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_ModifyTargetReferenceMutator49", type=mutatorenvironment_ObSelectionStrategy, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
newTarget51: BinaryAssociation = BinaryAssociation(
    name="newTarget51",
    ends={
        Property(name="mutatorenvironment_ObSelectionStrategy53", type=mutatorenvironment_ModifyTargetReferenceMutator, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_ModifyTargetReferenceMutator52", type=mutatorenvironment_ObSelectionStrategy, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
source54: BinaryAssociation = BinaryAssociation(
    name="source54",
    ends={
        Property(name="mutatorenvironment_ObSelectionStrategy55", type=mutatorenvironment_CreateReferenceMutator, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_CreateReferenceMutator", type=mutatorenvironment_ObSelectionStrategy, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target56: BinaryAssociation = BinaryAssociation(
    name="target56",
    ends={
        Property(name="mutatorenvironment_ObSelectionStrategy58", type=mutatorenvironment_CreateReferenceMutator, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_CreateReferenceMutator57", type=mutatorenvironment_ObSelectionStrategy, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
refType59: BinaryAssociation = BinaryAssociation(
    name="refType59",
    ends={
        Property(name="mutatorenvironment_EReference61", type=mutatorenvironment_CreateReferenceMutator, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_CreateReferenceMutator60", type=mutatorenvironment_EReference, multiplicity=Multiplicity(0, 1))
    }
)
object67: BinaryAssociation = BinaryAssociation(
    name="object67",
    ends={
        Property(name="mutatorenvironment_ObSelectionStrategy68", type=mutatorenvironment_ModifyInformationMutator, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_ModifyInformationMutator", type=mutatorenvironment_ObSelectionStrategy, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
attributes69: BinaryAssociation = BinaryAssociation(
    name="attributes69",
    ends={
        Property(name="mutatorenvironment_AttributeSet71", type=mutatorenvironment_ModifyInformationMutator, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_ModifyInformationMutator70", type=mutatorenvironment_AttributeSet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
references72: BinaryAssociation = BinaryAssociation(
    name="references72",
    ends={
        Property(name="mutatorenvironment_ReferenceSet74", type=mutatorenvironment_ModifyInformationMutator, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_ModifyInformationMutator73", type=mutatorenvironment_ReferenceSet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attribute75: BinaryAssociation = BinaryAssociation(
    name="attribute75",
    ends={
        Property(name="mutatorenvironment_EAttribute", type=mutatorenvironment_AttributeSet, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_AttributeSet76", type=mutatorenvironment_EAttribute, multiplicity=Multiplicity(0, 9999))
    }
)
object77: BinaryAssociation = BinaryAssociation(
    name="object77",
    ends={
        Property(name="mutatorenvironment_ObSelectionStrategy78", type=mutatorenvironment_AttributeSwap, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_AttributeSwap", type=mutatorenvironment_ObSelectionStrategy, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
object62: BinaryAssociation = BinaryAssociation(
    name="object62",
    ends={
        Property(name="mutatorenvironment_ObSelectionStrategy63", type=mutatorenvironment_RemoveObjectMutator, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_RemoveObjectMutator", type=mutatorenvironment_ObSelectionStrategy, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
container64: BinaryAssociation = BinaryAssociation(
    name="container64",
    ends={
        Property(name="mutatorenvironment_ObSelectionStrategy66", type=mutatorenvironment_RemoveObjectMutator, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_RemoveObjectMutator65", type=mutatorenvironment_ObSelectionStrategy, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
object79: BinaryAssociation = BinaryAssociation(
    name="object79",
    ends={
        Property(name="mutatorenvironment_ObSelectionStrategy80", type=mutatorenvironment_AttributeCopy, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_AttributeCopy", type=mutatorenvironment_ObSelectionStrategy, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
refType81: BinaryAssociation = BinaryAssociation(
    name="refType81",
    ends={
        Property(name="mutatorenvironment_EReference82", type=mutatorenvironment_RemoveRandomReferenceMutator, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_RemoveRandomReferenceMutator", type=mutatorenvironment_EReference, multiplicity=Multiplicity(0, 1))
    }
)
refType83: BinaryAssociation = BinaryAssociation(
    name="refType83",
    ends={
        Property(name="mutatorenvironment_EReference84", type=mutatorenvironment_RemoveSpecificReferenceMutator, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_RemoveSpecificReferenceMutator", type=mutatorenvironment_EReference, multiplicity=Multiplicity(0, 1))
    }
)
container85: BinaryAssociation = BinaryAssociation(
    name="container85",
    ends={
        Property(name="mutatorenvironment_ObSelectionStrategy87", type=mutatorenvironment_RemoveSpecificReferenceMutator, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_RemoveSpecificReferenceMutator86", type=mutatorenvironment_ObSelectionStrategy, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
refType88: BinaryAssociation = BinaryAssociation(
    name="refType88",
    ends={
        Property(name="mutatorenvironment_EReference89", type=mutatorenvironment_RemoveCompleteReferenceMutator, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_RemoveCompleteReferenceMutator", type=mutatorenvironment_EReference, multiplicity=Multiplicity(0, 1))
    }
)
container90: BinaryAssociation = BinaryAssociation(
    name="container90",
    ends={
        Property(name="mutatorenvironment_ObSelectionStrategy91", type=mutatorenvironment_SelectObjectMutator, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_SelectObjectMutator", type=mutatorenvironment_ObSelectionStrategy, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
object92: BinaryAssociation = BinaryAssociation(
    name="object92",
    ends={
        Property(name="mutatorenvironment_ObSelectionStrategy94", type=mutatorenvironment_SelectObjectMutator, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_SelectObjectMutator93", type=mutatorenvironment_ObSelectionStrategy, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name95: BinaryAssociation = BinaryAssociation(
    name="name95",
    ends={
        Property(name="mutatorenvironment_EAttribute96", type=mutatorenvironment_AttributeEvaluation, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_AttributeEvaluation", type=mutatorenvironment_EAttribute, multiplicity=Multiplicity(1, 1))
    }
)
value97: BinaryAssociation = BinaryAssociation(
    name="value97",
    ends={
        Property(name="mutatorenvironment_AttributeEvaluationType", type=mutatorenvironment_AttributeEvaluation, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_AttributeEvaluation98", type=mutatorenvironment_AttributeEvaluationType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
reference99: BinaryAssociation = BinaryAssociation(
    name="reference99",
    ends={
        Property(name="mutatorenvironment_EReference101", type=mutatorenvironment_ReferenceSet, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_ReferenceSet100", type=mutatorenvironment_EReference, multiplicity=Multiplicity(0, 9999))
    }
)
object102: BinaryAssociation = BinaryAssociation(
    name="object102",
    ends={
        Property(name="mutatorenvironment_ObSelectionStrategy104", type=mutatorenvironment_ReferenceSet, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_ReferenceSet103", type=mutatorenvironment_ObSelectionStrategy, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value107: BinaryAssociation = BinaryAssociation(
    name="value107",
    ends={
        Property(name="mutatorenvironment_AttributeType109", type=mutatorenvironment_ReferenceAtt, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_ReferenceAtt108", type=mutatorenvironment_AttributeType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
name110: BinaryAssociation = BinaryAssociation(
    name="name110",
    ends={
        Property(name="mutatorenvironment_EReference111", type=mutatorenvironment_ReferenceEvaluation, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_ReferenceEvaluation", type=mutatorenvironment_EReference, multiplicity=Multiplicity(0, 1))
    }
)
refName112: BinaryAssociation = BinaryAssociation(
    name="refName112",
    ends={
        Property(name="mutatorenvironment_EReference114", type=mutatorenvironment_ReferenceEvaluation, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_ReferenceEvaluation113", type=mutatorenvironment_EReference, multiplicity=Multiplicity(0, 1))
    }
)
refRefName115: BinaryAssociation = BinaryAssociation(
    name="refRefName115",
    ends={
        Property(name="mutatorenvironment_EReference117", type=mutatorenvironment_ReferenceEvaluation, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_ReferenceEvaluation116", type=mutatorenvironment_EReference, multiplicity=Multiplicity(0, 1))
    }
)
value118: BinaryAssociation = BinaryAssociation(
    name="value118",
    ends={
        Property(name="mutatorenvironment_ObSelectionStrategy120", type=mutatorenvironment_ReferenceEvaluation, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_ReferenceEvaluation119", type=mutatorenvironment_ObSelectionStrategy, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
refType121: BinaryAssociation = BinaryAssociation(
    name="refType121",
    ends={
        Property(name="mutatorenvironment_EReference123", type=mutatorenvironment_ReferenceEvaluation, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_ReferenceEvaluation122", type=mutatorenvironment_EReference, multiplicity=Multiplicity(0, 1))
    }
)
attName124: BinaryAssociation = BinaryAssociation(
    name="attName124",
    ends={
        Property(name="mutatorenvironment_EAttribute126", type=mutatorenvironment_ReferenceEvaluation, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_ReferenceEvaluation125", type=mutatorenvironment_EAttribute, multiplicity=Multiplicity(0, 1))
    }
)
attValue127: BinaryAssociation = BinaryAssociation(
    name="attValue127",
    ends={
        Property(name="mutatorenvironment_AttributeEvaluationType129", type=mutatorenvironment_ReferenceEvaluation, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_ReferenceEvaluation128", type=mutatorenvironment_AttributeEvaluationType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
first130: BinaryAssociation = BinaryAssociation(
    name="first130",
    ends={
        Property(name="mutatorenvironment_Evaluation", type=mutatorenvironment_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_Expression131", type=mutatorenvironment_Evaluation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
operator132: BinaryAssociation = BinaryAssociation(
    name="operator132",
    ends={
        Property(name="mutatorenvironment_BinaryOperator", type=mutatorenvironment_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_Expression133", type=mutatorenvironment_BinaryOperator, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attribute105: BinaryAssociation = BinaryAssociation(
    name="attribute105",
    ends={
        Property(name="mutatorenvironment_EAttribute106", type=mutatorenvironment_ReferenceAtt, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_ReferenceAtt", type=mutatorenvironment_EAttribute, multiplicity=Multiplicity(1, 1))
    }
)
commands137: BinaryAssociation = BinaryAssociation(
    name="commands137",
    ends={
        Property(name="mutatorenvironment_Mutator139", type=mutatorenvironment_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_Block138", type=mutatorenvironment_Mutator, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
from141: BinaryAssociation = BinaryAssociation(
    name="from141",
    ends={
        Property(name="mutatorenvironment_Block142", type=mutatorenvironment_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_Block140", type=mutatorenvironment_Block, multiplicity=Multiplicity(0, 9999))
    }
)
type143: BinaryAssociation = BinaryAssociation(
    name="type143",
    ends={
        Property(name="mutatorenvironment_EClass145", type=mutatorenvironment_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_Constraint144", type=mutatorenvironment_EClass, multiplicity=Multiplicity(1, 1))
    }
)
expressions146: BinaryAssociation = BinaryAssociation(
    name="expressions146",
    ends={
        Property(name="InvariantCS", type=mutatorenvironment_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_Constraint147", type=InvariantCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
second134: BinaryAssociation = BinaryAssociation(
    name="second134",
    ends={
        Property(name="mutatorenvironment_Evaluation136", type=mutatorenvironment_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_Expression135", type=mutatorenvironment_Evaluation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
object148: BinaryAssociation = BinaryAssociation(
    name="object148",
    ends={
        Property(name="mutatorenvironment_ObSelectionStrategy149", type=mutatorenvironment_CloneObjectMutator, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_CloneObjectMutator", type=mutatorenvironment_ObSelectionStrategy, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
container150: BinaryAssociation = BinaryAssociation(
    name="container150",
    ends={
        Property(name="mutatorenvironment_ObSelectionStrategy152", type=mutatorenvironment_CloneObjectMutator, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_CloneObjectMutator151", type=mutatorenvironment_ObSelectionStrategy, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
refType153: BinaryAssociation = BinaryAssociation(
    name="refType153",
    ends={
        Property(name="mutatorenvironment_EReference155", type=mutatorenvironment_CloneObjectMutator, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_CloneObjectMutator154", type=mutatorenvironment_EReference, multiplicity=Multiplicity(0, 1))
    }
)
attributes156: BinaryAssociation = BinaryAssociation(
    name="attributes156",
    ends={
        Property(name="mutatorenvironment_AttributeSet158", type=mutatorenvironment_CloneObjectMutator, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_CloneObjectMutator157", type=mutatorenvironment_AttributeSet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
references159: BinaryAssociation = BinaryAssociation(
    name="references159",
    ends={
        Property(name="mutatorenvironment_ReferenceSet161", type=mutatorenvironment_CloneObjectMutator, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_CloneObjectMutator160", type=mutatorenvironment_ReferenceSet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value162: BinaryAssociation = BinaryAssociation(
    name="value162",
    ends={
        Property(name="mutatorenvironment_EObject", type=mutatorenvironment_ListType, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_ListType", type=mutatorenvironment_EObject, multiplicity=Multiplicity(0, 9999))
    }
)
objSel163: BinaryAssociation = BinaryAssociation(
    name="objSel163",
    ends={
        Property(name="mutatorenvironment_ObjectEmitter164", type=mutatorenvironment_ObjectAttributeType, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_ObjectAttributeType", type=mutatorenvironment_ObjectEmitter, multiplicity=Multiplicity(1, 1))
    }
)
attribute165: BinaryAssociation = BinaryAssociation(
    name="attribute165",
    ends={
        Property(name="mutatorenvironment_EAttribute167", type=mutatorenvironment_ObjectAttributeType, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_ObjectAttributeType166", type=mutatorenvironment_EAttribute, multiplicity=Multiplicity(1, 1))
    }
)
attribute168: BinaryAssociation = BinaryAssociation(
    name="attribute168",
    ends={
        Property(name="mutatorenvironment_EAttribute169", type=mutatorenvironment_MinValueType, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_MinValueType", type=mutatorenvironment_EAttribute, multiplicity=Multiplicity(1, 1))
    }
)
attribute170: BinaryAssociation = BinaryAssociation(
    name="attribute170",
    ends={
        Property(name="mutatorenvironment_EAttribute171", type=mutatorenvironment_MaxValueType, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_MaxValueType", type=mutatorenvironment_EAttribute, multiplicity=Multiplicity(1, 1))
    }
)
value172: BinaryAssociation = BinaryAssociation(
    name="value172",
    ends={
        Property(name="mutatorenvironment_AttributeEvaluationType173", type=mutatorenvironment_AttributeOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_AttributeOperation", type=mutatorenvironment_AttributeEvaluationType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
object174: BinaryAssociation = BinaryAssociation(
    name="object174",
    ends={
        Property(name="mutatorenvironment_ObSelectionStrategy175", type=mutatorenvironment_RandomNumberType, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_RandomNumberType", type=mutatorenvironment_ObSelectionStrategy, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
max176: BinaryAssociation = BinaryAssociation(
    name="max176",
    ends={
        Property(name="mutatorenvironment_EAttribute178", type=mutatorenvironment_RandomNumberType, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_RandomNumberType177", type=mutatorenvironment_EAttribute, multiplicity=Multiplicity(1, 1))
    }
)
objSel179: BinaryAssociation = BinaryAssociation(
    name="objSel179",
    ends={
        Property(name="mutatorenvironment_ObjectEmitter180", type=mutatorenvironment_SpecificClosureSelection, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_SpecificClosureSelection", type=mutatorenvironment_ObjectEmitter, multiplicity=Multiplicity(1, 1))
    }
)
object181: BinaryAssociation = BinaryAssociation(
    name="object181",
    ends={
        Property(name="mutatorenvironment_ObSelectionStrategy182", type=mutatorenvironment_SelectSampleMutator, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_SelectSampleMutator", type=mutatorenvironment_ObSelectionStrategy, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
features183: BinaryAssociation = BinaryAssociation(
    name="features183",
    ends={
        Property(name="mutatorenvironment_EStructuralFeature", type=mutatorenvironment_SelectSampleMutator, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_SelectSampleMutator184", type=mutatorenvironment_EStructuralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
object185: BinaryAssociation = BinaryAssociation(
    name="object185",
    ends={
        Property(name="mutatorenvironment_ObSelectionStrategy186", type=mutatorenvironment_RetypeObjectMutator, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_RetypeObjectMutator", type=mutatorenvironment_ObSelectionStrategy, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
container187: BinaryAssociation = BinaryAssociation(
    name="container187",
    ends={
        Property(name="mutatorenvironment_ObSelectionStrategy189", type=mutatorenvironment_RetypeObjectMutator, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_RetypeObjectMutator188", type=mutatorenvironment_ObSelectionStrategy, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
attributes193: BinaryAssociation = BinaryAssociation(
    name="attributes193",
    ends={
        Property(name="mutatorenvironment_AttributeSet195", type=mutatorenvironment_RetypeObjectMutator, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_RetypeObjectMutator194", type=mutatorenvironment_AttributeSet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
references196: BinaryAssociation = BinaryAssociation(
    name="references196",
    ends={
        Property(name="mutatorenvironment_ReferenceSet198", type=mutatorenvironment_RetypeObjectMutator, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_RetypeObjectMutator197", type=mutatorenvironment_ReferenceSet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
path199: BinaryAssociation = BinaryAssociation(
    name="path199",
    ends={
        Property(name="mutatorenvironment_Source201", type=mutatorenvironment_Resource, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_Resource200", type=mutatorenvironment_Source, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
packages202: BinaryAssociation = BinaryAssociation(
    name="packages202",
    ends={
        Property(name="PackageCS", type=mutatorenvironment_miniOCL_RootCS, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_miniOCL_RootCS", type=PackageCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
contraints203: BinaryAssociation = BinaryAssociation(
    name="contraints203",
    ends={
        Property(name="ConstraintCS", type=mutatorenvironment_miniOCL_RootCS, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_miniOCL_RootCS204", type=ConstraintCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
packages205: BinaryAssociation = BinaryAssociation(
    name="packages205",
    ends={
        Property(name="PackageCS206", type=mutatorenvironment_miniOCL_PackageCS, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_miniOCL_PackageCS", type=PackageCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
classes207: BinaryAssociation = BinaryAssociation(
    name="classes207",
    ends={
        Property(name="ClassCS", type=mutatorenvironment_miniOCL_PackageCS, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_miniOCL_PackageCS208", type=ClassCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extends209: BinaryAssociation = BinaryAssociation(
    name="extends209",
    ends={
        Property(name="PathNameCS", type=mutatorenvironment_miniOCL_ClassCS, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_miniOCL_ClassCS", type=PathNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
properties210: BinaryAssociation = BinaryAssociation(
    name="properties210",
    ends={
        Property(name="PropertyCS", type=mutatorenvironment_miniOCL_ClassCS, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_miniOCL_ClassCS211", type=PropertyCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
refType190: BinaryAssociation = BinaryAssociation(
    name="refType190",
    ends={
        Property(name="mutatorenvironment_EReference192", type=mutatorenvironment_RetypeObjectMutator, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_RetypeObjectMutator191", type=mutatorenvironment_EReference, multiplicity=Multiplicity(0, 1))
    }
)
operations212: BinaryAssociation = BinaryAssociation(
    name="operations212",
    ends={
        Property(name="mutatorenvironment_miniOCL_ClassCS213", type=OperationCS, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="OperationCS", type=mutatorenvironment_miniOCL_ClassCS, multiplicity=Multiplicity(1, 1))
    }
)
right232: BinaryAssociation = BinaryAssociation(
    name="right232",
    ends={
        Property(name="CallExpCS", type=mutatorenvironment_miniOCL_LogicExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_miniOCL_LogicExpCS233", type=CallExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeRef214: BinaryAssociation = BinaryAssociation(
    name="typeRef214",
    ends={
        Property(name="PathNameCS215", type=mutatorenvironment_miniOCL_PropertyCS, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_miniOCL_PropertyCS", type=PathNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
source234: BinaryAssociation = BinaryAssociation(
    name="source234",
    ends={
        Property(name="CallExpCS235", type=mutatorenvironment_miniOCL_CallExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_miniOCL_CallExpCS", type=CallExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
params216: BinaryAssociation = BinaryAssociation(
    name="params216",
    ends={
        Property(name="ParameterCS", type=mutatorenvironment_miniOCL_OperationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_miniOCL_OperationCS", type=ParameterCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
navExp236: BinaryAssociation = BinaryAssociation(
    name="navExp236",
    ends={
        Property(name="NavigationExpCS", type=mutatorenvironment_miniOCL_CallExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_miniOCL_CallExpCS237", type=NavigationExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resultRef217: BinaryAssociation = BinaryAssociation(
    name="resultRef217",
    ends={
        Property(name="PathNameCS219", type=mutatorenvironment_miniOCL_OperationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_miniOCL_OperationCS218", type=PathNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body220: BinaryAssociation = BinaryAssociation(
    name="body220",
    ends={
        Property(name="ExpCS", type=mutatorenvironment_miniOCL_OperationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_miniOCL_OperationCS221", type=ExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expName238: BinaryAssociation = BinaryAssociation(
    name="expName238",
    ends={
        Property(name="PathNameCS239", type=mutatorenvironment_miniOCL_NameExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_miniOCL_NameExpCS", type=PathNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeRef222: BinaryAssociation = BinaryAssociation(
    name="typeRef222",
    ends={
        Property(name="PathNameCS223", type=mutatorenvironment_miniOCL_ParameterCS, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_miniOCL_ParameterCS", type=PathNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
roundedBrackets240: BinaryAssociation = BinaryAssociation(
    name="roundedBrackets240",
    ends={
        Property(name="RoundedBracketClauseCS", type=mutatorenvironment_miniOCL_NameExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_miniOCL_NameExpCS241", type=RoundedBracketClauseCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeRef224: BinaryAssociation = BinaryAssociation(
    name="typeRef224",
    ends={
        Property(name="PathNameCS225", type=mutatorenvironment_miniOCL_ConstraintCS, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_miniOCL_ConstraintCS", type=PathNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
invariants226: BinaryAssociation = BinaryAssociation(
    name="invariants226",
    ends={
        Property(name="InvariantCS228", type=mutatorenvironment_miniOCL_ConstraintCS, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_miniOCL_ConstraintCS227", type=InvariantCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exp229: BinaryAssociation = BinaryAssociation(
    name="exp229",
    ends={
        Property(name="ExpCS230", type=mutatorenvironment_miniOCL_InvariantCS, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_miniOCL_InvariantCS", type=ExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left231: BinaryAssociation = BinaryAssociation(
    name="left231",
    ends={
        Property(name="LogicExpCS", type=mutatorenvironment_miniOCL_LogicExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_miniOCL_LogicExpCS", type=LogicExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
accType252: BinaryAssociation = BinaryAssociation(
    name="accType252",
    ends={
        Property(name="PathNameCS253", type=mutatorenvironment_miniOCL_AccVarCS, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_miniOCL_AccVarCS", type=PathNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
accInitExp254: BinaryAssociation = BinaryAssociation(
    name="accInitExp254",
    ends={
        Property(name="ExpCS256", type=mutatorenvironment_miniOCL_AccVarCS, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_miniOCL_AccVarCS255", type=ExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
args257: BinaryAssociation = BinaryAssociation(
    name="args257",
    ends={
        Property(name="ExpCS258", type=mutatorenvironment_miniOCL_RoundedBracketClauseCS, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_miniOCL_RoundedBracketClauseCS", type=ExpCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
path259: BinaryAssociation = BinaryAssociation(
    name="path259",
    ends={
        Property(name="PathCS", type=mutatorenvironment_miniOCL_PathNameCS, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_miniOCL_PathNameCS", type=PathCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
callExp242: BinaryAssociation = BinaryAssociation(
    name="callExp242",
    ends={
        Property(name="CallExpCS244", type=mutatorenvironment_miniOCL_NameExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_miniOCL_NameExpCS243", type=CallExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
itVar245: BinaryAssociation = BinaryAssociation(
    name="itVar245",
    ends={
        Property(name="IteratorVarCS", type=mutatorenvironment_miniOCL_LoopExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_miniOCL_LoopExpCS", type=IteratorVarCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp246: BinaryAssociation = BinaryAssociation(
    name="exp246",
    ends={
        Property(name="ExpCS248", type=mutatorenvironment_miniOCL_LoopExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_miniOCL_LoopExpCS247", type=ExpCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
itType249: BinaryAssociation = BinaryAssociation(
    name="itType249",
    ends={
        Property(name="PathNameCS250", type=mutatorenvironment_miniOCL_IteratorVarCS, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_miniOCL_IteratorVarCS", type=PathNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
accVar251: BinaryAssociation = BinaryAssociation(
    name="accVar251",
    ends={
        Property(name="AccVarCS", type=mutatorenvironment_miniOCL_IterateExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_miniOCL_IterateExpCS", type=AccVarCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expName263: BinaryAssociation = BinaryAssociation(
    name="expName263",
    ends={
        Property(name="NavigationPathNameCS", type=mutatorenvironment_miniOCL_NavigationNameExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_miniOCL_NavigationNameExpCS", type=NavigationPathNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
roundedBrackets264: BinaryAssociation = BinaryAssociation(
    name="roundedBrackets264",
    ends={
        Property(name="RoundedBracketClauseCS266", type=mutatorenvironment_miniOCL_NavigationNameExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_miniOCL_NavigationNameExpCS265", type=RoundedBracketClauseCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
callExp267: BinaryAssociation = BinaryAssociation(
    name="callExp267",
    ends={
        Property(name="CallExpCS269", type=mutatorenvironment_miniOCL_NavigationNameExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_miniOCL_NavigationNameExpCS268", type=CallExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
path270: BinaryAssociation = BinaryAssociation(
    name="path270",
    ends={
        Property(name="NavigationPathCS", type=mutatorenvironment_miniOCL_NavigationPathNameCS, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_miniOCL_NavigationPathNameCS", type=NavigationPathCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pathName271: BinaryAssociation = BinaryAssociation(
    name="pathName271",
    ends={
        Property(name="miniOCL_mutatorenvironment_EStructuralFeature272", type=mutatorenvironment_miniOCL_NavigationPathElementCS, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_miniOCL_NavigationPathElementCS", type=miniOCL_mutatorenvironment_EStructuralFeature, multiplicity=Multiplicity(0, 1))
    }
)
pathName260: BinaryAssociation = BinaryAssociation(
    name="pathName260",
    ends={
        Property(name="miniOCL_mutatorenvironment_EStructuralFeature", type=mutatorenvironment_miniOCL_PathElementCS, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_miniOCL_PathElementCS", type=miniOCL_mutatorenvironment_EStructuralFeature, multiplicity=Multiplicity(0, 1))
    }
)
accVars261: BinaryAssociation = BinaryAssociation(
    name="accVars261",
    ends={
        Property(name="AccVarCS262", type=mutatorenvironment_miniOCL_ExistsExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_miniOCL_ExistsExpCS", type=AccVarCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
accVars273: BinaryAssociation = BinaryAssociation(
    name="accVars273",
    ends={
        Property(name="AccVarCS274", type=mutatorenvironment_miniOCL_ForAllExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="mutatorenvironment_miniOCL_ForAllExpCS", type=AccVarCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_mutatorenvironment_Library_Definition = Generalization(general=Definition, specific=mutatorenvironment_Library)
gen_mutatorenvironment_Program_Definition = Generalization(general=Definition, specific=mutatorenvironment_Program)
gen_mutatorenvironment_Mutator_ObjectEmitter = Generalization(general=ObjectEmitter, specific=mutatorenvironment_Mutator)
gen_mutatorenvironment_CompositeMutator_Mutator = Generalization(general=Mutator, specific=mutatorenvironment_CompositeMutator)
gen_mutatorenvironment_CreateObjectMutator_Mutator = Generalization(general=Mutator, specific=mutatorenvironment_CreateObjectMutator)
gen_mutatorenvironment_ObSelectionStrategy_ObjectEmitter = Generalization(general=ObjectEmitter, specific=mutatorenvironment_ObSelectionStrategy)
gen_mutatorenvironment_SpecificObjectSelection_SpecificSelection = Generalization(general=SpecificSelection, specific=mutatorenvironment_SpecificObjectSelection)
gen_mutatorenvironment_AttributeScalar_AttributeSet = Generalization(general=AttributeSet, specific=mutatorenvironment_AttributeScalar)
gen_mutatorenvironment_AttributeType_AttributeEvaluationType = Generalization(general=AttributeEvaluationType, specific=mutatorenvironment_AttributeType)
gen_mutatorenvironment_BooleanType_AttributeType = Generalization(general=AttributeType, specific=mutatorenvironment_BooleanType)
gen_mutatorenvironment_SpecificBooleanType_BooleanType = Generalization(general=BooleanType, specific=mutatorenvironment_SpecificBooleanType)
gen_mutatorenvironment_RandomBooleanType_BooleanType = Generalization(general=BooleanType, specific=mutatorenvironment_RandomBooleanType)
gen_mutatorenvironment_StringType_AttributeType = Generalization(general=AttributeType, specific=mutatorenvironment_StringType)
gen_mutatorenvironment_SpecificStringType_StringType = Generalization(general=StringType, specific=mutatorenvironment_SpecificStringType)
gen_mutatorenvironment_RandomStringType_StringType = Generalization(general=StringType, specific=mutatorenvironment_RandomStringType)
gen_mutatorenvironment_IntegerType_NumberType = Generalization(general=NumberType, specific=mutatorenvironment_IntegerType)
gen_mutatorenvironment_SpecificIntegerType_IntegerType = Generalization(general=IntegerType, specific=mutatorenvironment_SpecificIntegerType)
gen_mutatorenvironment_RandomIntegerType_IntegerType = Generalization(general=IntegerType, specific=mutatorenvironment_RandomIntegerType)
gen_mutatorenvironment_RandomSelection_ObSelectionStrategy = Generalization(general=ObSelectionStrategy, specific=mutatorenvironment_RandomSelection)
gen_mutatorenvironment_RandomTypeSelection_RandomSelection = Generalization(general=RandomSelection, specific=mutatorenvironment_RandomTypeSelection)
gen_mutatorenvironment_ModifySourceReferenceMutator_Mutator = Generalization(general=Mutator, specific=mutatorenvironment_ModifySourceReferenceMutator)
gen_mutatorenvironment_SpecificSelection_ObSelectionStrategy = Generalization(general=ObSelectionStrategy, specific=mutatorenvironment_SpecificSelection)
gen_mutatorenvironment_SpecificReferenceSelection_SpecificSelection = Generalization(general=SpecificSelection, specific=mutatorenvironment_SpecificReferenceSelection)
gen_mutatorenvironment_ModifyTargetReferenceMutator_Mutator = Generalization(general=Mutator, specific=mutatorenvironment_ModifyTargetReferenceMutator)
gen_mutatorenvironment_CreateReferenceMutator_Mutator = Generalization(general=Mutator, specific=mutatorenvironment_CreateReferenceMutator)
gen_mutatorenvironment_RemoveObjectMutator_Mutator = Generalization(general=Mutator, specific=mutatorenvironment_RemoveObjectMutator)
gen_mutatorenvironment_DoubleType_NumberType = Generalization(general=NumberType, specific=mutatorenvironment_DoubleType)
gen_mutatorenvironment_SpecificDoubleType_DoubleType = Generalization(general=DoubleType, specific=mutatorenvironment_SpecificDoubleType)
gen_mutatorenvironment_RandomDoubleType_DoubleType = Generalization(general=DoubleType, specific=mutatorenvironment_RandomDoubleType)
gen_mutatorenvironment_ModifyInformationMutator_Mutator = Generalization(general=Mutator, specific=mutatorenvironment_ModifyInformationMutator)
gen_mutatorenvironment_UpperStringType_StringType = Generalization(general=StringType, specific=mutatorenvironment_UpperStringType)
gen_mutatorenvironment_LowerStringType_StringType = Generalization(general=StringType, specific=mutatorenvironment_LowerStringType)
gen_mutatorenvironment_ListStringType_AttributeType = Generalization(general=AttributeType, specific=mutatorenvironment_ListStringType)
gen_mutatorenvironment_CatStartStringType_StringType = Generalization(general=StringType, specific=mutatorenvironment_CatStartStringType)
gen_mutatorenvironment_CatEndStringType_StringType = Generalization(general=StringType, specific=mutatorenvironment_CatEndStringType)
gen_mutatorenvironment_AttributeUnset_AttributeSet = Generalization(general=AttributeSet, specific=mutatorenvironment_AttributeUnset)
gen_mutatorenvironment_AttributeSwap_AttributeSet = Generalization(general=AttributeSet, specific=mutatorenvironment_AttributeSwap)
gen_mutatorenvironment_RemoveReferenceMutator_Mutator = Generalization(general=Mutator, specific=mutatorenvironment_RemoveReferenceMutator)
gen_mutatorenvironment_AttributeCopy_AttributeSet = Generalization(general=AttributeSet, specific=mutatorenvironment_AttributeCopy)
gen_mutatorenvironment_RemoveRandomReferenceMutator_RemoveReferenceMutator = Generalization(general=RemoveReferenceMutator, specific=mutatorenvironment_RemoveRandomReferenceMutator)
gen_mutatorenvironment_RemoveSpecificReferenceMutator_RemoveReferenceMutator = Generalization(general=RemoveReferenceMutator, specific=mutatorenvironment_RemoveSpecificReferenceMutator)
gen_mutatorenvironment_CompleteSelection_ObSelectionStrategy = Generalization(general=ObSelectionStrategy, specific=mutatorenvironment_CompleteSelection)
gen_mutatorenvironment_CompleteTypeSelection_CompleteSelection = Generalization(general=CompleteSelection, specific=mutatorenvironment_CompleteTypeSelection)
gen_mutatorenvironment_RemoveCompleteReferenceMutator_RemoveReferenceMutator = Generalization(general=RemoveReferenceMutator, specific=mutatorenvironment_RemoveCompleteReferenceMutator)
gen_mutatorenvironment_ReplaceStringType_StringType = Generalization(general=StringType, specific=mutatorenvironment_ReplaceStringType)
gen_mutatorenvironment_OtherTypeSelection_OtherSelection = Generalization(general=OtherSelection, specific=mutatorenvironment_OtherTypeSelection)
gen_mutatorenvironment_SelectObjectMutator_Mutator = Generalization(general=Mutator, specific=mutatorenvironment_SelectObjectMutator)
gen_mutatorenvironment_AttributeEvaluation_Evaluation = Generalization(general=Evaluation, specific=mutatorenvironment_AttributeEvaluation)
gen_mutatorenvironment_AttributeReverse_AttributeSet = Generalization(general=AttributeSet, specific=mutatorenvironment_AttributeReverse)
gen_mutatorenvironment_OtherSelection_ObSelectionStrategy = Generalization(general=ObSelectionStrategy, specific=mutatorenvironment_OtherSelection)
gen_mutatorenvironment_ReferenceEvaluation_Evaluation = Generalization(general=Evaluation, specific=mutatorenvironment_ReferenceEvaluation)
gen_mutatorenvironment_ReferenceInit_ReferenceSet = Generalization(general=ReferenceSet, specific=mutatorenvironment_ReferenceInit)
gen_mutatorenvironment_ReferenceAtt_ReferenceSet = Generalization(general=ReferenceSet, specific=mutatorenvironment_ReferenceAtt)
gen_mutatorenvironment_RandomType_AttributeType = Generalization(general=AttributeType, specific=mutatorenvironment_RandomType)
gen_mutatorenvironment_ReferenceSwap_ReferenceSet = Generalization(general=ReferenceSet, specific=mutatorenvironment_ReferenceSwap)
gen_mutatorenvironment_ListType_AttributeType = Generalization(general=AttributeType, specific=mutatorenvironment_ListType)
gen_mutatorenvironment_ObjectAttributeType_AttributeEvaluationType = Generalization(general=AttributeEvaluationType, specific=mutatorenvironment_ObjectAttributeType)
gen_mutatorenvironment_MinValueType_NumberType = Generalization(general=NumberType, specific=mutatorenvironment_MinValueType)
gen_mutatorenvironment_MaxValueType_NumberType = Generalization(general=NumberType, specific=mutatorenvironment_MaxValueType)
gen_mutatorenvironment_NumberType_AttributeType = Generalization(general=AttributeType, specific=mutatorenvironment_NumberType)
gen_mutatorenvironment_AttributeOperation_AttributeSet = Generalization(general=AttributeSet, specific=mutatorenvironment_AttributeOperation)
gen_mutatorenvironment_CloneObjectMutator_Mutator = Generalization(general=Mutator, specific=mutatorenvironment_CloneObjectMutator)
gen_mutatorenvironment_RandomNumberType_NumberType = Generalization(general=NumberType, specific=mutatorenvironment_RandomNumberType)
gen_mutatorenvironment_RandomDoubleNumberType_RandomNumberType = Generalization(general=RandomNumberType, specific=mutatorenvironment_RandomDoubleNumberType)
gen_mutatorenvironment_RandomIntegerNumberType_RandomNumberType = Generalization(general=RandomNumberType, specific=mutatorenvironment_RandomIntegerNumberType)
gen_mutatorenvironment_SpecificClosureSelection_SpecificSelection = Generalization(general=SpecificSelection, specific=mutatorenvironment_SpecificClosureSelection)
gen_mutatorenvironment_SelectSampleMutator_Mutator = Generalization(general=Mutator, specific=mutatorenvironment_SelectSampleMutator)
gen_mutatorenvironment_ReferenceAdd_ReferenceSet = Generalization(general=ReferenceSet, specific=mutatorenvironment_ReferenceAdd)
gen_mutatorenvironment_ReferenceRemove_ReferenceSet = Generalization(general=ReferenceSet, specific=mutatorenvironment_ReferenceRemove)
gen_mutatorenvironment_RetypeObjectMutator_Mutator = Generalization(general=Mutator, specific=mutatorenvironment_RetypeObjectMutator)
gen_mutatorenvironment_TypedSelection_ObSelectionStrategy = Generalization(general=ObSelectionStrategy, specific=mutatorenvironment_TypedSelection)
gen_mutatorenvironment_RandomStringNumberType_StringType = Generalization(general=StringType, specific=mutatorenvironment_RandomStringNumberType)
gen_mutatorenvironment_Resource_Definition = Generalization(general=Definition, specific=mutatorenvironment_Resource)
gen_mutatorenvironment_miniOCL_CallExpCS_LogicExpCS = Generalization(general=LogicExpCS, specific=mutatorenvironment_miniOCL_CallExpCS)
gen_mutatorenvironment_miniOCL_PrimaryExpCS_CallExpCS = Generalization(general=CallExpCS, specific=mutatorenvironment_miniOCL_PrimaryExpCS)
gen_mutatorenvironment_miniOCL_NavigationExpCS_PrimaryExpCS = Generalization(general=PrimaryExpCS, specific=mutatorenvironment_miniOCL_NavigationExpCS)
gen_mutatorenvironment_miniOCL_NameExpCS_NavigationExpCS = Generalization(general=NavigationExpCS, specific=mutatorenvironment_miniOCL_NameExpCS)
gen_mutatorenvironment_miniOCL_LogicExpCS_ExpCS = Generalization(general=ExpCS, specific=mutatorenvironment_miniOCL_LogicExpCS)
gen_mutatorenvironment_miniOCL_LiteralExpCS_PrimaryExpCS = Generalization(general=PrimaryExpCS, specific=mutatorenvironment_miniOCL_LiteralExpCS)
gen_mutatorenvironment_miniOCL_IntLiteralExpCS_LiteralExpCS = Generalization(general=LiteralExpCS, specific=mutatorenvironment_miniOCL_IntLiteralExpCS)
gen_mutatorenvironment_miniOCL_StringLiteralExpCS_LiteralExpCS = Generalization(general=LiteralExpCS, specific=mutatorenvironment_miniOCL_StringLiteralExpCS)
gen_mutatorenvironment_miniOCL_BooleanLiteralExpCS_LiteralExpCS = Generalization(general=LiteralExpCS, specific=mutatorenvironment_miniOCL_BooleanLiteralExpCS)
gen_mutatorenvironment_miniOCL_PathVariableCS_PathCS = Generalization(general=PathCS, specific=mutatorenvironment_miniOCL_PathVariableCS)
gen_mutatorenvironment_miniOCL_LoopExpCS_NavigationExpCS = Generalization(general=NavigationExpCS, specific=mutatorenvironment_miniOCL_LoopExpCS)
gen_mutatorenvironment_miniOCL_CollectExpCS_LoopExpCS = Generalization(general=LoopExpCS, specific=mutatorenvironment_miniOCL_CollectExpCS)
gen_mutatorenvironment_miniOCL_IterateExpCS_LoopExpCS = Generalization(general=LoopExpCS, specific=mutatorenvironment_miniOCL_IterateExpCS)
gen_mutatorenvironment_miniOCL_NavigationNameExpCS_NavigationExpCS = Generalization(general=NavigationExpCS, specific=mutatorenvironment_miniOCL_NavigationNameExpCS)
gen_mutatorenvironment_miniOCL_NavigationPathVariableCS_NavigationPathCS = Generalization(general=NavigationPathCS, specific=mutatorenvironment_miniOCL_NavigationPathVariableCS)
gen_mutatorenvironment_miniOCL_NavigationPathElementCS_NavigationPathCS = Generalization(general=NavigationPathCS, specific=mutatorenvironment_miniOCL_NavigationPathElementCS)
gen_mutatorenvironment_miniOCL_ForAllExpCS_LoopExpCS = Generalization(general=LoopExpCS, specific=mutatorenvironment_miniOCL_ForAllExpCS)
gen_mutatorenvironment_miniOCL_PathElementCS_PathCS = Generalization(general=PathCS, specific=mutatorenvironment_miniOCL_PathElementCS)
gen_mutatorenvironment_miniOCL_BooleanExpCS_BooleanLiteralExpCS = Generalization(general=BooleanLiteralExpCS, specific=mutatorenvironment_miniOCL_BooleanExpCS)
gen_mutatorenvironment_miniOCL_ExistsExpCS_LoopExpCS = Generalization(general=LoopExpCS, specific=mutatorenvironment_miniOCL_ExistsExpCS)

# Domain Model
domain_model = DomainModel(
    name="mutatorenvironment",
    types={mutatorenvironment_MutatorEnvironment, mutatorenvironment_Definition, mutatorenvironment_Mutator, mutatorenvironment_Load, mutatorenvironment_Block, mutatorenvironment_Constraint, mutatorenvironment_Library, Definition, mutatorenvironment_Program, mutatorenvironment_Resource, mutatorenvironment_ObjectEmitter, mutatorenvironment_EClass, ObjectEmitter, mutatorenvironment_CompositeMutator, Mutator, mutatorenvironment_CreateObjectMutator, mutatorenvironment_ObSelectionStrategy, mutatorenvironment_AttributeSet, mutatorenvironment_ReferenceSet, mutatorenvironment_EReference, mutatorenvironment_Expression, mutatorenvironment_Source, mutatorenvironment_SpecificObjectSelection, SpecificSelection, mutatorenvironment_AttributeScalar, AttributeSet, mutatorenvironment_AttributeType, AttributeEvaluationType, mutatorenvironment_BooleanType, AttributeType, mutatorenvironment_SpecificBooleanType, BooleanType, mutatorenvironment_RandomBooleanType, mutatorenvironment_StringType, mutatorenvironment_SpecificStringType, StringType, mutatorenvironment_RandomStringType, mutatorenvironment_IntegerType, NumberType, mutatorenvironment_SpecificIntegerType, IntegerType, mutatorenvironment_RandomIntegerType, mutatorenvironment_RandomSelection, ObSelectionStrategy, mutatorenvironment_RandomTypeSelection, RandomSelection, mutatorenvironment_ModifySourceReferenceMutator, mutatorenvironment_SpecificSelection, mutatorenvironment_SpecificReferenceSelection, mutatorenvironment_ModifyTargetReferenceMutator, mutatorenvironment_CreateReferenceMutator, mutatorenvironment_RemoveObjectMutator, mutatorenvironment_DoubleType, mutatorenvironment_SpecificDoubleType, DoubleType, mutatorenvironment_RandomDoubleType, mutatorenvironment_ModifyInformationMutator, mutatorenvironment_UpperStringType, mutatorenvironment_LowerStringType, mutatorenvironment_ListStringType, mutatorenvironment_CatStartStringType, mutatorenvironment_CatEndStringType, mutatorenvironment_AttributeUnset, mutatorenvironment_EAttribute, mutatorenvironment_AttributeSwap, mutatorenvironment_RemoveReferenceMutator, mutatorenvironment_AttributeCopy, mutatorenvironment_RemoveRandomReferenceMutator, RemoveReferenceMutator, mutatorenvironment_RemoveSpecificReferenceMutator, mutatorenvironment_CompleteSelection, mutatorenvironment_CompleteTypeSelection, CompleteSelection, mutatorenvironment_RemoveCompleteReferenceMutator, mutatorenvironment_ReplaceStringType, OtherSelection, mutatorenvironment_SelectObjectMutator, mutatorenvironment_AttributeEvaluation, Evaluation, mutatorenvironment_AttributeEvaluationType, mutatorenvironment_AttributeReverse, mutatorenvironment_OtherSelection, mutatorenvironment_OtherTypeSelection, mutatorenvironment_ReferenceEvaluation, mutatorenvironment_Evaluation, mutatorenvironment_BinaryOperator, mutatorenvironment_ReferenceInit, ReferenceSet, mutatorenvironment_ReferenceAtt, InvariantCS, mutatorenvironment_RandomType, mutatorenvironment_ReferenceSwap, mutatorenvironment_ListType, mutatorenvironment_EObject, mutatorenvironment_ObjectAttributeType, mutatorenvironment_MinValueType, mutatorenvironment_MaxValueType, mutatorenvironment_NumberType, mutatorenvironment_AttributeOperation, mutatorenvironment_CloneObjectMutator, mutatorenvironment_RandomNumberType, mutatorenvironment_RandomDoubleNumberType, RandomNumberType, mutatorenvironment_RandomIntegerNumberType, mutatorenvironment_SpecificClosureSelection, mutatorenvironment_SelectSampleMutator, mutatorenvironment_EStructuralFeature, mutatorenvironment_ReferenceAdd, mutatorenvironment_ReferenceRemove, mutatorenvironment_RetypeObjectMutator, mutatorenvironment_TypedSelection, mutatorenvironment_RandomStringNumberType, mutatorenvironment_miniOCL_RootCS, PackageCS, ConstraintCS, mutatorenvironment_miniOCL_PackageCS, ClassCS, mutatorenvironment_miniOCL_ClassCS, PathNameCS, PropertyCS, mutatorenvironment_miniOCL_PropertyCS, CallExpCS, mutatorenvironment_miniOCL_CallExpCS, mutatorenvironment_miniOCL_OperationCS, ParameterCS, NavigationExpCS, mutatorenvironment_miniOCL_PrimaryExpCS, mutatorenvironment_miniOCL_NavigationExpCS, PrimaryExpCS, ExpCS, mutatorenvironment_miniOCL_NameExpCS, mutatorenvironment_miniOCL_ParameterCS, RoundedBracketClauseCS, mutatorenvironment_miniOCL_ConstraintCS, mutatorenvironment_miniOCL_InvariantCS, mutatorenvironment_miniOCL_ExpCS, mutatorenvironment_miniOCL_LogicExpCS, LogicExpCS, OperationCS, mutatorenvironment_miniOCL_RoundedBracketClauseCS, mutatorenvironment_miniOCL_LiteralExpCS, mutatorenvironment_miniOCL_IntLiteralExpCS, LiteralExpCS, mutatorenvironment_miniOCL_StringLiteralExpCS, mutatorenvironment_miniOCL_BooleanLiteralExpCS, mutatorenvironment_miniOCL_PathNameCS, PathCS, mutatorenvironment_miniOCL_PathCS, mutatorenvironment_miniOCL_PathVariableCS, mutatorenvironment_miniOCL_LoopExpCS, IteratorVarCS, mutatorenvironment_miniOCL_CollectExpCS, LoopExpCS, mutatorenvironment_miniOCL_IteratorVarCS, mutatorenvironment_miniOCL_IterateExpCS, AccVarCS, mutatorenvironment_miniOCL_AccVarCS, mutatorenvironment_miniOCL_NavigationNameExpCS, NavigationPathNameCS, mutatorenvironment_miniOCL_NavigationPathNameCS, NavigationPathCS, mutatorenvironment_miniOCL_NavigationPathCS, mutatorenvironment_miniOCL_NavigationPathVariableCS, mutatorenvironment_miniOCL_NavigationPathElementCS, mutatorenvironment_miniOCL_ForAllExpCS, mutatorenvironment_miniOCL_PathElementCS, miniOCL_mutatorenvironment_EStructuralFeature, mutatorenvironment_miniOCL_BooleanExpCS, BooleanLiteralExpCS, mutatorenvironment_miniOCL_ExistsExpCS, Operator, Repeat, LogicOperator, ArithmeticOperator, SampleClause},
    associations={definition0, commands1, load3, blocks5, constraints7, resources10, type12, types13, commands16, container18, attributes19, references21, refType23, expression25, source9, objSel33, value35, refRefType27, refRefRefType30, refType36, source38, newSource41, objSel44, refType46, source48, newTarget51, source54, target56, refType59, object67, attributes69, references72, attribute75, object77, object62, container64, object79, refType81, refType83, container85, refType88, container90, object92, name95, value97, reference99, object102, value107, name110, refName112, refRefName115, value118, refType121, attName124, attValue127, first130, operator132, attribute105, commands137, from141, type143, expressions146, second134, object148, container150, refType153, attributes156, references159, value162, objSel163, attribute165, attribute168, attribute170, value172, object174, max176, objSel179, object181, features183, object185, container187, attributes193, references196, path199, packages202, contraints203, packages205, classes207, extends209, properties210, refType190, operations212, right232, typeRef214, source234, params216, navExp236, resultRef217, body220, expName238, typeRef222, roundedBrackets240, typeRef224, invariants226, exp229, left231, accType252, accInitExp254, args257, path259, callExp242, itVar245, exp246, itType249, accVar251, expName263, roundedBrackets264, callExp267, path270, pathName271, pathName260, accVars261, accVars273},
    generalizations={gen_mutatorenvironment_Library_Definition, gen_mutatorenvironment_Program_Definition, gen_mutatorenvironment_Mutator_ObjectEmitter, gen_mutatorenvironment_CompositeMutator_Mutator, gen_mutatorenvironment_CreateObjectMutator_Mutator, gen_mutatorenvironment_ObSelectionStrategy_ObjectEmitter, gen_mutatorenvironment_SpecificObjectSelection_SpecificSelection, gen_mutatorenvironment_AttributeScalar_AttributeSet, gen_mutatorenvironment_AttributeType_AttributeEvaluationType, gen_mutatorenvironment_BooleanType_AttributeType, gen_mutatorenvironment_SpecificBooleanType_BooleanType, gen_mutatorenvironment_RandomBooleanType_BooleanType, gen_mutatorenvironment_StringType_AttributeType, gen_mutatorenvironment_SpecificStringType_StringType, gen_mutatorenvironment_RandomStringType_StringType, gen_mutatorenvironment_IntegerType_NumberType, gen_mutatorenvironment_SpecificIntegerType_IntegerType, gen_mutatorenvironment_RandomIntegerType_IntegerType, gen_mutatorenvironment_RandomSelection_ObSelectionStrategy, gen_mutatorenvironment_RandomTypeSelection_RandomSelection, gen_mutatorenvironment_ModifySourceReferenceMutator_Mutator, gen_mutatorenvironment_SpecificSelection_ObSelectionStrategy, gen_mutatorenvironment_SpecificReferenceSelection_SpecificSelection, gen_mutatorenvironment_ModifyTargetReferenceMutator_Mutator, gen_mutatorenvironment_CreateReferenceMutator_Mutator, gen_mutatorenvironment_RemoveObjectMutator_Mutator, gen_mutatorenvironment_DoubleType_NumberType, gen_mutatorenvironment_SpecificDoubleType_DoubleType, gen_mutatorenvironment_RandomDoubleType_DoubleType, gen_mutatorenvironment_ModifyInformationMutator_Mutator, gen_mutatorenvironment_UpperStringType_StringType, gen_mutatorenvironment_LowerStringType_StringType, gen_mutatorenvironment_ListStringType_AttributeType, gen_mutatorenvironment_CatStartStringType_StringType, gen_mutatorenvironment_CatEndStringType_StringType, gen_mutatorenvironment_AttributeUnset_AttributeSet, gen_mutatorenvironment_AttributeSwap_AttributeSet, gen_mutatorenvironment_RemoveReferenceMutator_Mutator, gen_mutatorenvironment_AttributeCopy_AttributeSet, gen_mutatorenvironment_RemoveRandomReferenceMutator_RemoveReferenceMutator, gen_mutatorenvironment_RemoveSpecificReferenceMutator_RemoveReferenceMutator, gen_mutatorenvironment_CompleteSelection_ObSelectionStrategy, gen_mutatorenvironment_CompleteTypeSelection_CompleteSelection, gen_mutatorenvironment_RemoveCompleteReferenceMutator_RemoveReferenceMutator, gen_mutatorenvironment_ReplaceStringType_StringType, gen_mutatorenvironment_OtherTypeSelection_OtherSelection, gen_mutatorenvironment_SelectObjectMutator_Mutator, gen_mutatorenvironment_AttributeEvaluation_Evaluation, gen_mutatorenvironment_AttributeReverse_AttributeSet, gen_mutatorenvironment_OtherSelection_ObSelectionStrategy, gen_mutatorenvironment_ReferenceEvaluation_Evaluation, gen_mutatorenvironment_ReferenceInit_ReferenceSet, gen_mutatorenvironment_ReferenceAtt_ReferenceSet, gen_mutatorenvironment_RandomType_AttributeType, gen_mutatorenvironment_ReferenceSwap_ReferenceSet, gen_mutatorenvironment_ListType_AttributeType, gen_mutatorenvironment_ObjectAttributeType_AttributeEvaluationType, gen_mutatorenvironment_MinValueType_NumberType, gen_mutatorenvironment_MaxValueType_NumberType, gen_mutatorenvironment_NumberType_AttributeType, gen_mutatorenvironment_AttributeOperation_AttributeSet, gen_mutatorenvironment_CloneObjectMutator_Mutator, gen_mutatorenvironment_RandomNumberType_NumberType, gen_mutatorenvironment_RandomDoubleNumberType_RandomNumberType, gen_mutatorenvironment_RandomIntegerNumberType_RandomNumberType, gen_mutatorenvironment_SpecificClosureSelection_SpecificSelection, gen_mutatorenvironment_SelectSampleMutator_Mutator, gen_mutatorenvironment_ReferenceAdd_ReferenceSet, gen_mutatorenvironment_ReferenceRemove_ReferenceSet, gen_mutatorenvironment_RetypeObjectMutator_Mutator, gen_mutatorenvironment_TypedSelection_ObSelectionStrategy, gen_mutatorenvironment_RandomStringNumberType_StringType, gen_mutatorenvironment_Resource_Definition, gen_mutatorenvironment_miniOCL_CallExpCS_LogicExpCS, gen_mutatorenvironment_miniOCL_PrimaryExpCS_CallExpCS, gen_mutatorenvironment_miniOCL_NavigationExpCS_PrimaryExpCS, gen_mutatorenvironment_miniOCL_NameExpCS_NavigationExpCS, gen_mutatorenvironment_miniOCL_LogicExpCS_ExpCS, gen_mutatorenvironment_miniOCL_LiteralExpCS_PrimaryExpCS, gen_mutatorenvironment_miniOCL_IntLiteralExpCS_LiteralExpCS, gen_mutatorenvironment_miniOCL_StringLiteralExpCS_LiteralExpCS, gen_mutatorenvironment_miniOCL_BooleanLiteralExpCS_LiteralExpCS, gen_mutatorenvironment_miniOCL_PathVariableCS_PathCS, gen_mutatorenvironment_miniOCL_LoopExpCS_NavigationExpCS, gen_mutatorenvironment_miniOCL_CollectExpCS_LoopExpCS, gen_mutatorenvironment_miniOCL_IterateExpCS_LoopExpCS, gen_mutatorenvironment_miniOCL_NavigationNameExpCS_NavigationExpCS, gen_mutatorenvironment_miniOCL_NavigationPathVariableCS_NavigationPathCS, gen_mutatorenvironment_miniOCL_NavigationPathElementCS_NavigationPathCS, gen_mutatorenvironment_miniOCL_ForAllExpCS_LoopExpCS, gen_mutatorenvironment_miniOCL_PathElementCS_PathCS, gen_mutatorenvironment_miniOCL_BooleanExpCS_BooleanLiteralExpCS, gen_mutatorenvironment_miniOCL_ExistsExpCS_LoopExpCS},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)