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
DirectionKindEnum: Enumeration = Enumeration(
    name="DirectionKindEnum",
    literals={
            EnumerationLiteral(name="DEFAULT"),
			EnumerationLiteral(name="in"),
			EnumerationLiteral(name="out"),
			EnumerationLiteral(name="inout")
    }
)

ModuleKindEnum: Enumeration = Enumeration(
    name="ModuleKindEnum",
    literals={
            EnumerationLiteral(name="transformation"),
			EnumerationLiteral(name="library")
    }
)

ImportKindEnum: Enumeration = Enumeration(
    name="ImportKindEnum",
    literals={
            EnumerationLiteral(name="extension"),
			EnumerationLiteral(name="access")
    }
)

MappingExtensionKindCS: Enumeration = Enumeration(
    name="MappingExtensionKindCS",
    literals={
            EnumerationLiteral(name="disjuncts"),
			EnumerationLiteral(name="merges"),
			EnumerationLiteral(name="inherits")
    }
)

QualifierKindCS: Enumeration = Enumeration(
    name="QualifierKindCS",
    literals={
            EnumerationLiteral(name="abstract"),
			EnumerationLiteral(name="blackbox"),
			EnumerationLiteral(name="static")
    }
)

# Classes
RenameCS = Class(name="RenameCS")
ModulePropertyCS = Class(name="ModulePropertyCS")
MappingMethodCS = Class(name="MappingMethodCS")
ClassifierDefCS = Class(name="ClassifierDefCS")
TagCS = Class(name="TagCS")
qvtoperational_cst_LibraryCS = Class(name="qvtoperational::cst::LibraryCS")
MappingModuleCS = Class(name="MappingModuleCS")
qvtoperational_cst_ImportCS = Class(name="qvtoperational::cst::ImportCS")
PathNameCS = Class(name="PathNameCS")
qvtoperational_cst_LibraryImportCS = Class(name="qvtoperational::cst::LibraryImportCS")
qvtoperational_cst_RenameCS = Class(name="qvtoperational::cst::RenameCS")
qvtoperational_cst_MappingModuleCS = Class(name="qvtoperational::cst::MappingModuleCS")
CSTNode = Class(name="CSTNode")
TransformationHeaderCS = Class(name="TransformationHeaderCS")
ImportCS = Class(name="ImportCS")
ModelTypeCS = Class(name="ModelTypeCS")
qvtoperational_cst_ConfigPropertyCS = Class(name="qvtoperational::cst::ConfigPropertyCS")
qvtoperational_cst_LocalPropertyCS = Class(name="qvtoperational::cst::LocalPropertyCS")
OCLExpressionCS = Class(name="OCLExpressionCS")
qvtoperational_cst_ContextualPropertyCS = Class(name="qvtoperational::cst::ContextualPropertyCS")
ScopedNameCS = Class(name="ScopedNameCS")
qvtoperational_cst_ClassifierDefCS = Class(name="qvtoperational::cst::ClassifierDefCS")
TypeCS = Class(name="TypeCS")
SimpleNameCS = Class(name="SimpleNameCS")
StringLiteralExpCS = Class(name="StringLiteralExpCS")
qvtoperational_cst_ModulePropertyCS = Class(name="qvtoperational::cst::ModulePropertyCS", is_abstract=True)
MultiplicityDefCS = Class(name="MultiplicityDefCS")
OppositePropertyCS = Class(name="OppositePropertyCS")
qvtoperational_cst_IntermediateClassDefCS = Class(name="qvtoperational::cst::IntermediateClassDefCS")
qvtoperational_cst_ExceptionDefCS = Class(name="qvtoperational::cst::ExceptionDefCS")
qvtoperational_cst_OppositePropertyCS = Class(name="qvtoperational::cst::OppositePropertyCS")
qvtoperational_cst_MultiplicityDefCS = Class(name="qvtoperational::cst::MultiplicityDefCS")
PrimitiveLiteralExpCS = Class(name="PrimitiveLiteralExpCS")
qvtoperational_cst_MappingDeclarationCS = Class(name="qvtoperational::cst::MappingDeclarationCS")
ClassifierPropertyCS = Class(name="ClassifierPropertyCS")
qvtoperational_cst_ClassifierPropertyCS = Class(name="qvtoperational::cst::ClassifierPropertyCS")
LocalPropertyCS = Class(name="LocalPropertyCS")
qvtoperational_cst_ParameterDeclarationCS = Class(name="qvtoperational::cst::ParameterDeclarationCS")
TypeSpecCS = Class(name="TypeSpecCS")
qvtoperational_cst_SimpleSignatureCS = Class(name="qvtoperational::cst::SimpleSignatureCS")
qvtoperational_cst_CompleteSignatureCS = Class(name="qvtoperational::cst::CompleteSignatureCS")
SimpleSignatureCS = Class(name="SimpleSignatureCS")
qvtoperational_cst_MappingMethodCS = Class(name="qvtoperational::cst::MappingMethodCS", is_abstract=True)
ParameterDeclarationCS = Class(name="ParameterDeclarationCS")
DirectionKindCS = Class(name="DirectionKindCS")
MappingExtensionCS = Class(name="MappingExtensionCS")
qvtoperational_cst_MappingQueryCS = Class(name="qvtoperational::cst::MappingQueryCS")
BlockExpCS = Class(name="BlockExpCS")
qvtoperational_cst_ConstructorCS = Class(name="qvtoperational::cst::ConstructorCS")
qvtoperational_cst_MappingSectionCS = Class(name="qvtoperational::cst::MappingSectionCS", is_abstract=True)
cst_CSTNode = Class(name="cst::CSTNode")
cst_ElementWithBody = Class(name="cst::ElementWithBody")
MappingRuleCS = Class(name="MappingRuleCS")
qvtoperational_cst_MappingInitCS = Class(name="qvtoperational::cst::MappingInitCS")
MappingSectionCS = Class(name="MappingSectionCS")
qvtoperational_cst_MappingEndCS = Class(name="qvtoperational::cst::MappingEndCS")
qvtoperational_cst_MappingSectionsCS = Class(name="qvtoperational::cst::MappingSectionsCS")
MappingInitCS = Class(name="MappingInitCS")
MappingBodyCS = Class(name="MappingBodyCS")
MappingEndCS = Class(name="MappingEndCS")
MappingDeclarationCS = Class(name="MappingDeclarationCS")
qvtoperational_cst_MappingRuleCS = Class(name="qvtoperational::cst::MappingRuleCS")
MappingSectionsCS = Class(name="MappingSectionsCS")
VariableCS = Class(name="VariableCS")
qvtoperational_cst_WhileExpCS = Class(name="qvtoperational::cst::WhileExpCS")
qvtoperational_cst_ImperativeLoopExpCS = Class(name="qvtoperational::cst::ImperativeLoopExpCS")
cst_LoopExpCS = Class(name="cst::LoopExpCS")
cst_StatementCS = Class(name="cst::StatementCS")
qvtoperational_cst_ForExpCS = Class(name="qvtoperational::cst::ForExpCS")
ImperativeLoopExpCS = Class(name="ImperativeLoopExpCS")
qvtoperational_cst_ImperativeIterateExpCS = Class(name="qvtoperational::cst::ImperativeIterateExpCS")
qvtoperational_cst_SwitchExpCS = Class(name="qvtoperational::cst::SwitchExpCS")
SwitchAltExpCS = Class(name="SwitchAltExpCS")
qvtoperational_cst_StatementCS = Class(name="qvtoperational::cst::StatementCS", is_abstract=True)
qvtoperational_cst_BlockExpCS = Class(name="qvtoperational::cst::BlockExpCS")
StatementCS = Class(name="StatementCS")
qvtoperational_cst_ComputeExpCS = Class(name="qvtoperational::cst::ComputeExpCS")
qvtoperational_cst_AssignStatementCS = Class(name="qvtoperational::cst::AssignStatementCS")
qvtoperational_cst_BreakExpCS = Class(name="qvtoperational::cst::BreakExpCS")
qvtoperational_cst_ContinueExpCS = Class(name="qvtoperational::cst::ContinueExpCS")
qvtoperational_cst_ExpressionStatementCS = Class(name="qvtoperational::cst::ExpressionStatementCS")
qvtoperational_cst_MappingBodyCS = Class(name="qvtoperational::cst::MappingBodyCS")
qvtoperational_cst_ObjectExpCS = Class(name="qvtoperational::cst::ObjectExpCS")
qvtoperational_cst_SwitchAltExpCS = Class(name="qvtoperational::cst::SwitchAltExpCS")
qvtoperational_cst_VariableInitializationCS = Class(name="qvtoperational::cst::VariableInitializationCS")
OperationCallExpCS = Class(name="OperationCallExpCS")
qvtoperational_cst_DirectionKindCS = Class(name="qvtoperational::cst::DirectionKindCS")
qvtoperational_cst_ElementWithBody = Class(name="qvtoperational::cst::ElementWithBody", is_abstract=True)
qvtoperational_cst_ResolveExpCS = Class(name="qvtoperational::cst::ResolveExpCS")
CallExpCS = Class(name="CallExpCS")
qvtoperational_cst_ResolveInExpCS = Class(name="qvtoperational::cst::ResolveInExpCS")
ResolveExpCS = Class(name="ResolveExpCS")
cst_InstantiationExpCS = Class(name="cst::InstantiationExpCS")
qvtoperational_cst_MappingCallExpCS = Class(name="qvtoperational::cst::MappingCallExpCS")
ImperativeOperationCallExpCS = Class(name="ImperativeOperationCallExpCS")
qvtoperational_cst_ImperativeOperationCallExpCS = Class(name="qvtoperational::cst::ImperativeOperationCallExpCS")
qvtoperational_cst_PackageRefCS = Class(name="qvtoperational::cst::PackageRefCS")
qvtoperational_cst_TransformationHeaderCS = Class(name="qvtoperational::cst::TransformationHeaderCS")
ModuleUsageCS = Class(name="ModuleUsageCS")
TransformationRefineCS = Class(name="TransformationRefineCS")
qvtoperational_cst_ModelTypeCS = Class(name="qvtoperational::cst::ModelTypeCS")
PackageRefCS = Class(name="PackageRefCS")
qvtoperational_cst_ModuleUsageCS = Class(name="qvtoperational::cst::ModuleUsageCS")
ModuleKindCS = Class(name="ModuleKindCS")
ModuleRefCS = Class(name="ModuleRefCS")
qvtoperational_cst_TransformationRefineCS = Class(name="qvtoperational::cst::TransformationRefineCS")
qvtoperational_cst_TypeSpecCS = Class(name="qvtoperational::cst::TypeSpecCS")
qvtoperational_cst_LogExpCS = Class(name="qvtoperational::cst::LogExpCS")
qvtoperational_cst_ModuleKindCS = Class(name="qvtoperational::cst::ModuleKindCS")
qvtoperational_cst_ModuleRefCS = Class(name="qvtoperational::cst::ModuleRefCS")
qvtoperational_cst_MappingExtensionCS = Class(name="qvtoperational::cst::MappingExtensionCS")
qvtoperational_cst_DictLiteralExpCS = Class(name="qvtoperational::cst::DictLiteralExpCS")
qvtoperational_cst_InstantiationExpCS = Class(name="qvtoperational::cst::InstantiationExpCS")
qvtoperational_cst_ListTypeCS = Class(name="qvtoperational::cst::ListTypeCS")
qvtoperational_cst_ListLiteralExpCS = Class(name="qvtoperational::cst::ListLiteralExpCS")
qvtoperational_cst_AssertExpCS = Class(name="qvtoperational::cst::AssertExpCS")
LiteralExpCS = Class(name="LiteralExpCS")
CollectionLiteralPartCS = Class(name="CollectionLiteralPartCS")
qvtoperational_cst_DictionaryTypeCS = Class(name="qvtoperational::cst::DictionaryTypeCS")
LogExpCS = Class(name="LogExpCS")
qvtoperational_cst_ReturnExpCS = Class(name="qvtoperational::cst::ReturnExpCS")
qvtoperational_cst_UnitCS = Class(name="qvtoperational::cst::UnitCS")
DictLiteralPartCS = Class(name="DictLiteralPartCS")
qvtoperational_cst_DictLiteralPartCS = Class(name="qvtoperational::cst::DictLiteralPartCS")
qvtoperational_cst_TagCS = Class(name="qvtoperational::cst::TagCS")
qvtoperational_cst_TryExpCS = Class(name="qvtoperational::cst::TryExpCS")
CatchExpCS = Class(name="CatchExpCS")
qvtoperational_cst_CatchExpCS = Class(name="qvtoperational::cst::CatchExpCS")
qvtoperational_cst_RaiseExpCS = Class(name="qvtoperational::cst::RaiseExpCS")
qvtoperational_cst_ResolveOpArgsExpCS = Class(name="qvtoperational::cst::ResolveOpArgsExpCS")
qvtoperational_cst_ScopedNameCS = Class(name="qvtoperational::cst::ScopedNameCS")

# RenameCS class attributes and methods

# ModulePropertyCS class attributes and methods

# MappingMethodCS class attributes and methods

# ClassifierDefCS class attributes and methods

# TagCS class attributes and methods

# qvtoperational_cst_LibraryCS class attributes and methods

# MappingModuleCS class attributes and methods

# qvtoperational_cst_ImportCS class attributes and methods

# PathNameCS class attributes and methods

# qvtoperational_cst_LibraryImportCS class attributes and methods

# qvtoperational_cst_RenameCS class attributes and methods

# qvtoperational_cst_MappingModuleCS class attributes and methods

# CSTNode class attributes and methods

# TransformationHeaderCS class attributes and methods

# ImportCS class attributes and methods

# ModelTypeCS class attributes and methods

# qvtoperational_cst_ConfigPropertyCS class attributes and methods

# qvtoperational_cst_LocalPropertyCS class attributes and methods

# OCLExpressionCS class attributes and methods

# qvtoperational_cst_ContextualPropertyCS class attributes and methods

# ScopedNameCS class attributes and methods

# qvtoperational_cst_ClassifierDefCS class attributes and methods

# TypeCS class attributes and methods

# SimpleNameCS class attributes and methods

# StringLiteralExpCS class attributes and methods

# qvtoperational_cst_ModulePropertyCS class attributes and methods

# MultiplicityDefCS class attributes and methods

# OppositePropertyCS class attributes and methods

# qvtoperational_cst_IntermediateClassDefCS class attributes and methods

# qvtoperational_cst_ExceptionDefCS class attributes and methods

# qvtoperational_cst_OppositePropertyCS class attributes and methods
qvtoperational_cst_OppositePropertyCS_isNavigable: Property = Property(name="isNavigable", type=BooleanType)
qvtoperational_cst_OppositePropertyCS.attributes={qvtoperational_cst_OppositePropertyCS_isNavigable}

# qvtoperational_cst_MultiplicityDefCS class attributes and methods

# PrimitiveLiteralExpCS class attributes and methods

# qvtoperational_cst_MappingDeclarationCS class attributes and methods
qvtoperational_cst_MappingDeclarationCS_qualifiers: Property = Property(name="qualifiers", type=StringType)
qvtoperational_cst_MappingDeclarationCS_isQuery: Property = Property(name="isQuery", type=BooleanType)
qvtoperational_cst_MappingDeclarationCS.attributes={qvtoperational_cst_MappingDeclarationCS_isQuery, qvtoperational_cst_MappingDeclarationCS_qualifiers}

# ClassifierPropertyCS class attributes and methods

# qvtoperational_cst_ClassifierPropertyCS class attributes and methods
qvtoperational_cst_ClassifierPropertyCS_isOrdered: Property = Property(name="isOrdered", type=BooleanType)
qvtoperational_cst_ClassifierPropertyCS.attributes={qvtoperational_cst_ClassifierPropertyCS_isOrdered}

# LocalPropertyCS class attributes and methods

# qvtoperational_cst_ParameterDeclarationCS class attributes and methods
qvtoperational_cst_ParameterDeclarationCS_directionKind: Property = Property(name="directionKind", type=StringType)
qvtoperational_cst_ParameterDeclarationCS.attributes={qvtoperational_cst_ParameterDeclarationCS_directionKind}

# TypeSpecCS class attributes and methods

# qvtoperational_cst_SimpleSignatureCS class attributes and methods

# qvtoperational_cst_CompleteSignatureCS class attributes and methods

# SimpleSignatureCS class attributes and methods

# qvtoperational_cst_MappingMethodCS class attributes and methods
qvtoperational_cst_MappingMethodCS_blackBox: Property = Property(name="blackBox", type=BooleanType)
qvtoperational_cst_MappingMethodCS.attributes={qvtoperational_cst_MappingMethodCS_blackBox}

# ParameterDeclarationCS class attributes and methods

# DirectionKindCS class attributes and methods

# MappingExtensionCS class attributes and methods

# qvtoperational_cst_MappingQueryCS class attributes and methods
qvtoperational_cst_MappingQueryCS_isSimpleDefinition: Property = Property(name="isSimpleDefinition", type=BooleanType)
qvtoperational_cst_MappingQueryCS.attributes={qvtoperational_cst_MappingQueryCS_isSimpleDefinition}

# BlockExpCS class attributes and methods

# qvtoperational_cst_ConstructorCS class attributes and methods

# qvtoperational_cst_MappingSectionCS class attributes and methods

# cst_CSTNode class attributes and methods

# cst_ElementWithBody class attributes and methods

# MappingRuleCS class attributes and methods

# qvtoperational_cst_MappingInitCS class attributes and methods

# MappingSectionCS class attributes and methods

# qvtoperational_cst_MappingEndCS class attributes and methods

# qvtoperational_cst_MappingSectionsCS class attributes and methods

# MappingInitCS class attributes and methods

# MappingBodyCS class attributes and methods

# MappingEndCS class attributes and methods

# MappingDeclarationCS class attributes and methods

# qvtoperational_cst_MappingRuleCS class attributes and methods

# MappingSectionsCS class attributes and methods

# VariableCS class attributes and methods

# qvtoperational_cst_WhileExpCS class attributes and methods

# qvtoperational_cst_ImperativeLoopExpCS class attributes and methods

# cst_LoopExpCS class attributes and methods

# cst_StatementCS class attributes and methods

# qvtoperational_cst_ForExpCS class attributes and methods

# ImperativeLoopExpCS class attributes and methods

# qvtoperational_cst_ImperativeIterateExpCS class attributes and methods

# qvtoperational_cst_SwitchExpCS class attributes and methods

# SwitchAltExpCS class attributes and methods

# qvtoperational_cst_StatementCS class attributes and methods

# qvtoperational_cst_BlockExpCS class attributes and methods

# StatementCS class attributes and methods

# qvtoperational_cst_ComputeExpCS class attributes and methods

# qvtoperational_cst_AssignStatementCS class attributes and methods
qvtoperational_cst_AssignStatementCS_incremental: Property = Property(name="incremental", type=BooleanType)
qvtoperational_cst_AssignStatementCS.attributes={qvtoperational_cst_AssignStatementCS_incremental}

# qvtoperational_cst_BreakExpCS class attributes and methods

# qvtoperational_cst_ContinueExpCS class attributes and methods

# qvtoperational_cst_ExpressionStatementCS class attributes and methods

# qvtoperational_cst_MappingBodyCS class attributes and methods
qvtoperational_cst_MappingBodyCS_hasPopulationKeyword: Property = Property(name="hasPopulationKeyword", type=BooleanType)
qvtoperational_cst_MappingBodyCS.attributes={qvtoperational_cst_MappingBodyCS_hasPopulationKeyword}

# qvtoperational_cst_ObjectExpCS class attributes and methods
qvtoperational_cst_ObjectExpCS_isImplicit: Property = Property(name="isImplicit", type=BooleanType)
qvtoperational_cst_ObjectExpCS.attributes={qvtoperational_cst_ObjectExpCS_isImplicit}

# qvtoperational_cst_SwitchAltExpCS class attributes and methods

# qvtoperational_cst_VariableInitializationCS class attributes and methods
qvtoperational_cst_VariableInitializationCS_withResult: Property = Property(name="withResult", type=BooleanType)
qvtoperational_cst_VariableInitializationCS.attributes={qvtoperational_cst_VariableInitializationCS_withResult}

# OperationCallExpCS class attributes and methods

# qvtoperational_cst_DirectionKindCS class attributes and methods
qvtoperational_cst_DirectionKindCS_directionKind: Property = Property(name="directionKind", type=StringType)
qvtoperational_cst_DirectionKindCS.attributes={qvtoperational_cst_DirectionKindCS_directionKind}

# qvtoperational_cst_ElementWithBody class attributes and methods
qvtoperational_cst_ElementWithBody_bodyStartLocation: Property = Property(name="bodyStartLocation", type=IntegerType)
qvtoperational_cst_ElementWithBody_bodyEndLocation: Property = Property(name="bodyEndLocation", type=IntegerType)
qvtoperational_cst_ElementWithBody.attributes={qvtoperational_cst_ElementWithBody_bodyStartLocation, qvtoperational_cst_ElementWithBody_bodyEndLocation}

# qvtoperational_cst_ResolveExpCS class attributes and methods
qvtoperational_cst_ResolveExpCS_one: Property = Property(name="one", type=BooleanType)
qvtoperational_cst_ResolveExpCS_isInverse: Property = Property(name="isInverse", type=BooleanType)
qvtoperational_cst_ResolveExpCS_isDeferred: Property = Property(name="isDeferred", type=BooleanType)
qvtoperational_cst_ResolveExpCS.attributes={qvtoperational_cst_ResolveExpCS_one, qvtoperational_cst_ResolveExpCS_isInverse, qvtoperational_cst_ResolveExpCS_isDeferred}

# CallExpCS class attributes and methods

# qvtoperational_cst_ResolveInExpCS class attributes and methods

# ResolveExpCS class attributes and methods

# cst_InstantiationExpCS class attributes and methods

# qvtoperational_cst_MappingCallExpCS class attributes and methods
qvtoperational_cst_MappingCallExpCS_strict: Property = Property(name="strict", type=BooleanType)
qvtoperational_cst_MappingCallExpCS.attributes={qvtoperational_cst_MappingCallExpCS_strict}

# ImperativeOperationCallExpCS class attributes and methods

# qvtoperational_cst_ImperativeOperationCallExpCS class attributes and methods

# qvtoperational_cst_PackageRefCS class attributes and methods

# qvtoperational_cst_TransformationHeaderCS class attributes and methods
qvtoperational_cst_TransformationHeaderCS_qualifiers: Property = Property(name="qualifiers", type=StringType)
qvtoperational_cst_TransformationHeaderCS.attributes={qvtoperational_cst_TransformationHeaderCS_qualifiers}

# ModuleUsageCS class attributes and methods

# TransformationRefineCS class attributes and methods

# qvtoperational_cst_ModelTypeCS class attributes and methods

# PackageRefCS class attributes and methods

# qvtoperational_cst_ModuleUsageCS class attributes and methods
qvtoperational_cst_ModuleUsageCS_importKind: Property = Property(name="importKind", type=StringType)
qvtoperational_cst_ModuleUsageCS.attributes={qvtoperational_cst_ModuleUsageCS_importKind}

# ModuleKindCS class attributes and methods

# ModuleRefCS class attributes and methods

# qvtoperational_cst_TransformationRefineCS class attributes and methods

# qvtoperational_cst_TypeSpecCS class attributes and methods

# qvtoperational_cst_LogExpCS class attributes and methods

# qvtoperational_cst_ModuleKindCS class attributes and methods
qvtoperational_cst_ModuleKindCS_moduleKind: Property = Property(name="moduleKind", type=StringType)
qvtoperational_cst_ModuleKindCS.attributes={qvtoperational_cst_ModuleKindCS_moduleKind}

# qvtoperational_cst_ModuleRefCS class attributes and methods

# qvtoperational_cst_MappingExtensionCS class attributes and methods
qvtoperational_cst_MappingExtensionCS_kind: Property = Property(name="kind", type=StringType)
qvtoperational_cst_MappingExtensionCS.attributes={qvtoperational_cst_MappingExtensionCS_kind}

# qvtoperational_cst_DictLiteralExpCS class attributes and methods

# qvtoperational_cst_InstantiationExpCS class attributes and methods

# qvtoperational_cst_ListTypeCS class attributes and methods

# qvtoperational_cst_ListLiteralExpCS class attributes and methods

# qvtoperational_cst_AssertExpCS class attributes and methods

# LiteralExpCS class attributes and methods

# CollectionLiteralPartCS class attributes and methods

# qvtoperational_cst_DictionaryTypeCS class attributes and methods

# LogExpCS class attributes and methods

# qvtoperational_cst_ReturnExpCS class attributes and methods

# qvtoperational_cst_UnitCS class attributes and methods

# DictLiteralPartCS class attributes and methods

# qvtoperational_cst_DictLiteralPartCS class attributes and methods

# qvtoperational_cst_TagCS class attributes and methods

# qvtoperational_cst_TryExpCS class attributes and methods

# CatchExpCS class attributes and methods

# qvtoperational_cst_CatchExpCS class attributes and methods

# qvtoperational_cst_RaiseExpCS class attributes and methods

# qvtoperational_cst_ResolveOpArgsExpCS class attributes and methods

# qvtoperational_cst_ScopedNameCS class attributes and methods
qvtoperational_cst_ScopedNameCS_name: Property = Property(name="name", type=StringType)
qvtoperational_cst_ScopedNameCS.attributes={qvtoperational_cst_ScopedNameCS_name}

# Relationships
metamodels3: BinaryAssociation = BinaryAssociation(
    name="metamodels3",
    ends={
        Property(name="ModelTypeCS", type=qvtoperational_cst_MappingModuleCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_MappingModuleCS4", type=ModelTypeCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
renamings5: BinaryAssociation = BinaryAssociation(
    name="renamings5",
    ends={
        Property(name="RenameCS", type=qvtoperational_cst_MappingModuleCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_MappingModuleCS6", type=RenameCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
properties7: BinaryAssociation = BinaryAssociation(
    name="properties7",
    ends={
        Property(name="ModulePropertyCS", type=qvtoperational_cst_MappingModuleCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_MappingModuleCS8", type=ModulePropertyCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
methods9: BinaryAssociation = BinaryAssociation(
    name="methods9",
    ends={
        Property(name="MappingMethodCS", type=qvtoperational_cst_MappingModuleCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_MappingModuleCS10", type=MappingMethodCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
classifierDefCS11: BinaryAssociation = BinaryAssociation(
    name="classifierDefCS11",
    ends={
        Property(name="ClassifierDefCS", type=qvtoperational_cst_MappingModuleCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_MappingModuleCS12", type=ClassifierDefCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tags13: BinaryAssociation = BinaryAssociation(
    name="tags13",
    ends={
        Property(name="TagCS", type=qvtoperational_cst_MappingModuleCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_MappingModuleCS14", type=TagCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pathNameCS15: BinaryAssociation = BinaryAssociation(
    name="pathNameCS15",
    ends={
        Property(name="PathNameCS", type=qvtoperational_cst_ImportCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_ImportCS", type=PathNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
headerCS0: BinaryAssociation = BinaryAssociation(
    name="headerCS0",
    ends={
        Property(name="TransformationHeaderCS", type=qvtoperational_cst_MappingModuleCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_MappingModuleCS", type=TransformationHeaderCS, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
imports1: BinaryAssociation = BinaryAssociation(
    name="imports1",
    ends={
        Property(name="ImportCS", type=qvtoperational_cst_MappingModuleCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_MappingModuleCS2", type=ImportCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeCS23: BinaryAssociation = BinaryAssociation(
    name="typeCS23",
    ends={
        Property(name="TypeCS24", type=qvtoperational_cst_ConfigPropertyCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_ConfigPropertyCS", type=TypeCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeCS25: BinaryAssociation = BinaryAssociation(
    name="typeCS25",
    ends={
        Property(name="TypeCS26", type=qvtoperational_cst_LocalPropertyCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_LocalPropertyCS", type=TypeCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
oclExpressionCS27: BinaryAssociation = BinaryAssociation(
    name="oclExpressionCS27",
    ends={
        Property(name="OCLExpressionCS", type=qvtoperational_cst_LocalPropertyCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_LocalPropertyCS28", type=OCLExpressionCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
scopedNameCS29: BinaryAssociation = BinaryAssociation(
    name="scopedNameCS29",
    ends={
        Property(name="ScopedNameCS", type=qvtoperational_cst_ContextualPropertyCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_ContextualPropertyCS", type=ScopedNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeCS30: BinaryAssociation = BinaryAssociation(
    name="typeCS30",
    ends={
        Property(name="TypeCS32", type=qvtoperational_cst_ContextualPropertyCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_ContextualPropertyCS31", type=TypeCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
oclExpressionCS33: BinaryAssociation = BinaryAssociation(
    name="oclExpressionCS33",
    ends={
        Property(name="OCLExpressionCS35", type=qvtoperational_cst_ContextualPropertyCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_ContextualPropertyCS34", type=OCLExpressionCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
simpleNameCS36: BinaryAssociation = BinaryAssociation(
    name="simpleNameCS36",
    ends={
        Property(name="SimpleNameCS37", type=qvtoperational_cst_ClassifierDefCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_ClassifierDefCS", type=SimpleNameCS, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
extends38: BinaryAssociation = BinaryAssociation(
    name="extends38",
    ends={
        Property(name="TypeCS40", type=qvtoperational_cst_ClassifierDefCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_ClassifierDefCS39", type=TypeCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeCS16: BinaryAssociation = BinaryAssociation(
    name="typeCS16",
    ends={
        Property(name="TypeCS", type=qvtoperational_cst_RenameCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_RenameCS", type=TypeCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
simpleNameCS17: BinaryAssociation = BinaryAssociation(
    name="simpleNameCS17",
    ends={
        Property(name="SimpleNameCS", type=qvtoperational_cst_RenameCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_RenameCS18", type=SimpleNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
originalName19: BinaryAssociation = BinaryAssociation(
    name="originalName19",
    ends={
        Property(name="StringLiteralExpCS", type=qvtoperational_cst_RenameCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_RenameCS20", type=StringLiteralExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
simpleNameCS21: BinaryAssociation = BinaryAssociation(
    name="simpleNameCS21",
    ends={
        Property(name="SimpleNameCS22", type=qvtoperational_cst_ModulePropertyCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_ModulePropertyCS", type=SimpleNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
multiplicity51: BinaryAssociation = BinaryAssociation(
    name="multiplicity51",
    ends={
        Property(name="MultiplicityDefCS", type=qvtoperational_cst_ClassifierPropertyCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_ClassifierPropertyCS52", type=MultiplicityDefCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
opposite53: BinaryAssociation = BinaryAssociation(
    name="opposite53",
    ends={
        Property(name="OppositePropertyCS", type=qvtoperational_cst_ClassifierPropertyCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_ClassifierPropertyCS54", type=OppositePropertyCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
simpleNameCS55: BinaryAssociation = BinaryAssociation(
    name="simpleNameCS55",
    ends={
        Property(name="SimpleNameCS56", type=qvtoperational_cst_OppositePropertyCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_OppositePropertyCS", type=SimpleNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
multiplicity57: BinaryAssociation = BinaryAssociation(
    name="multiplicity57",
    ends={
        Property(name="MultiplicityDefCS59", type=qvtoperational_cst_OppositePropertyCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_OppositePropertyCS58", type=MultiplicityDefCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lowerBound60: BinaryAssociation = BinaryAssociation(
    name="lowerBound60",
    ends={
        Property(name="PrimitiveLiteralExpCS", type=qvtoperational_cst_MultiplicityDefCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_MultiplicityDefCS", type=PrimitiveLiteralExpCS, multiplicity=Multiplicity(1, 1))
    }
)
upperBound61: BinaryAssociation = BinaryAssociation(
    name="upperBound61",
    ends={
        Property(name="PrimitiveLiteralExpCS63", type=qvtoperational_cst_MultiplicityDefCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_MultiplicityDefCS62", type=PrimitiveLiteralExpCS, multiplicity=Multiplicity(1, 1))
    }
)
simpleNameCS64: BinaryAssociation = BinaryAssociation(
    name="simpleNameCS64",
    ends={
        Property(name="SimpleNameCS65", type=qvtoperational_cst_MappingDeclarationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_MappingDeclarationCS", type=SimpleNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
properties41: BinaryAssociation = BinaryAssociation(
    name="properties41",
    ends={
        Property(name="ClassifierPropertyCS", type=qvtoperational_cst_ClassifierDefCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_ClassifierDefCS42", type=ClassifierPropertyCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tags43: BinaryAssociation = BinaryAssociation(
    name="tags43",
    ends={
        Property(name="TagCS45", type=qvtoperational_cst_ClassifierDefCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_ClassifierDefCS44", type=TagCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
stereotypeQualifiers46: BinaryAssociation = BinaryAssociation(
    name="stereotypeQualifiers46",
    ends={
        Property(name="SimpleNameCS47", type=qvtoperational_cst_ClassifierPropertyCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_ClassifierPropertyCS", type=SimpleNameCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
featureKeys48: BinaryAssociation = BinaryAssociation(
    name="featureKeys48",
    ends={
        Property(name="SimpleNameCS50", type=qvtoperational_cst_ClassifierPropertyCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_ClassifierPropertyCS49", type=SimpleNameCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
simpleNameCS78: BinaryAssociation = BinaryAssociation(
    name="simpleNameCS78",
    ends={
        Property(name="SimpleNameCS79", type=qvtoperational_cst_ParameterDeclarationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_ParameterDeclarationCS", type=SimpleNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeSpecCS80: BinaryAssociation = BinaryAssociation(
    name="typeSpecCS80",
    ends={
        Property(name="TypeSpecCS", type=qvtoperational_cst_ParameterDeclarationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_ParameterDeclarationCS81", type=TypeSpecCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
params82: BinaryAssociation = BinaryAssociation(
    name="params82",
    ends={
        Property(name="ParameterDeclarationCS83", type=qvtoperational_cst_SimpleSignatureCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_SimpleSignatureCS", type=ParameterDeclarationCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
simpleSignature84: BinaryAssociation = BinaryAssociation(
    name="simpleSignature84",
    ends={
        Property(name="SimpleSignatureCS", type=qvtoperational_cst_CompleteSignatureCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_CompleteSignatureCS", type=SimpleSignatureCS, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
resultParams85: BinaryAssociation = BinaryAssociation(
    name="resultParams85",
    ends={
        Property(name="ParameterDeclarationCS87", type=qvtoperational_cst_CompleteSignatureCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_CompleteSignatureCS86", type=ParameterDeclarationCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
contextType66: BinaryAssociation = BinaryAssociation(
    name="contextType66",
    ends={
        Property(name="TypeCS68", type=qvtoperational_cst_MappingDeclarationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_MappingDeclarationCS67", type=TypeCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters69: BinaryAssociation = BinaryAssociation(
    name="parameters69",
    ends={
        Property(name="ParameterDeclarationCS", type=qvtoperational_cst_MappingDeclarationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_MappingDeclarationCS70", type=ParameterDeclarationCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
result71: BinaryAssociation = BinaryAssociation(
    name="result71",
    ends={
        Property(name="ParameterDeclarationCS73", type=qvtoperational_cst_MappingDeclarationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_MappingDeclarationCS72", type=ParameterDeclarationCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
directionKindCS74: BinaryAssociation = BinaryAssociation(
    name="directionKindCS74",
    ends={
        Property(name="DirectionKindCS", type=qvtoperational_cst_MappingDeclarationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_MappingDeclarationCS75", type=DirectionKindCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
mappingExtension76: BinaryAssociation = BinaryAssociation(
    name="mappingExtension76",
    ends={
        Property(name="MappingExtensionCS", type=qvtoperational_cst_MappingDeclarationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_MappingDeclarationCS77", type=MappingExtensionCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body96: BinaryAssociation = BinaryAssociation(
    name="body96",
    ends={
        Property(name="BlockExpCS", type=qvtoperational_cst_MappingQueryCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_MappingQueryCS", type=BlockExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body97: BinaryAssociation = BinaryAssociation(
    name="body97",
    ends={
        Property(name="BlockExpCS98", type=qvtoperational_cst_ConstructorCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_ConstructorCS", type=BlockExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statements99: BinaryAssociation = BinaryAssociation(
    name="statements99",
    ends={
        Property(name="OCLExpressionCS100", type=qvtoperational_cst_MappingSectionCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_MappingSectionCS", type=OCLExpressionCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mappingRuleCS101: BinaryAssociation = BinaryAssociation(
    name="mappingRuleCS101",
    ends={
        Property(name="MappingRuleCS", type=qvtoperational_cst_MappingSectionCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_MappingSectionCS102", type=MappingRuleCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
mappingInitCS103: BinaryAssociation = BinaryAssociation(
    name="mappingInitCS103",
    ends={
        Property(name="MappingInitCS", type=qvtoperational_cst_MappingSectionsCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_MappingSectionsCS", type=MappingInitCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
mappingBodyCS104: BinaryAssociation = BinaryAssociation(
    name="mappingBodyCS104",
    ends={
        Property(name="MappingBodyCS", type=qvtoperational_cst_MappingSectionsCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_MappingSectionsCS105", type=MappingBodyCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
mappingEndCS106: BinaryAssociation = BinaryAssociation(
    name="mappingEndCS106",
    ends={
        Property(name="MappingEndCS", type=qvtoperational_cst_MappingSectionsCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_MappingSectionsCS107", type=MappingEndCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
mappingDeclarationCS88: BinaryAssociation = BinaryAssociation(
    name="mappingDeclarationCS88",
    ends={
        Property(name="MappingDeclarationCS", type=qvtoperational_cst_MappingMethodCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_MappingMethodCS", type=MappingDeclarationCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
guards89: BinaryAssociation = BinaryAssociation(
    name="guards89",
    ends={
        Property(name="OCLExpressionCS90", type=qvtoperational_cst_MappingRuleCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_MappingRuleCS", type=OCLExpressionCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
posts91: BinaryAssociation = BinaryAssociation(
    name="posts91",
    ends={
        Property(name="OCLExpressionCS93", type=qvtoperational_cst_MappingRuleCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_MappingRuleCS92", type=OCLExpressionCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mappingBody94: BinaryAssociation = BinaryAssociation(
    name="mappingBody94",
    ends={
        Property(name="MappingSectionsCS", type=qvtoperational_cst_MappingRuleCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_MappingRuleCS95", type=MappingSectionsCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
returnedElement110: BinaryAssociation = BinaryAssociation(
    name="returnedElement110",
    ends={
        Property(name="VariableCS", type=qvtoperational_cst_ComputeExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_ComputeExpCS", type=VariableCS, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body111: BinaryAssociation = BinaryAssociation(
    name="body111",
    ends={
        Property(name="OCLExpressionCS113", type=qvtoperational_cst_ComputeExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_ComputeExpCS112", type=OCLExpressionCS, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body114: BinaryAssociation = BinaryAssociation(
    name="body114",
    ends={
        Property(name="OCLExpressionCS115", type=qvtoperational_cst_WhileExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_WhileExpCS", type=OCLExpressionCS, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition116: BinaryAssociation = BinaryAssociation(
    name="condition116",
    ends={
        Property(name="OCLExpressionCS118", type=qvtoperational_cst_WhileExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_WhileExpCS117", type=OCLExpressionCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resultVar119: BinaryAssociation = BinaryAssociation(
    name="resultVar119",
    ends={
        Property(name="VariableCS121", type=qvtoperational_cst_WhileExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_WhileExpCS120", type=VariableCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition122: BinaryAssociation = BinaryAssociation(
    name="condition122",
    ends={
        Property(name="OCLExpressionCS123", type=qvtoperational_cst_ImperativeLoopExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_ImperativeLoopExpCS", type=OCLExpressionCS, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
target124: BinaryAssociation = BinaryAssociation(
    name="target124",
    ends={
        Property(name="VariableCS125", type=qvtoperational_cst_ImperativeIterateExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_ImperativeIterateExpCS", type=VariableCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
bodyExpressions108: BinaryAssociation = BinaryAssociation(
    name="bodyExpressions108",
    ends={
        Property(name="OCLExpressionCS109", type=qvtoperational_cst_BlockExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_BlockExpCS", type=OCLExpressionCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
oclExpressionCS135: BinaryAssociation = BinaryAssociation(
    name="oclExpressionCS135",
    ends={
        Property(name="OCLExpressionCS136", type=qvtoperational_cst_VariableInitializationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_VariableInitializationCS", type=OCLExpressionCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
simpleNameCS137: BinaryAssociation = BinaryAssociation(
    name="simpleNameCS137",
    ends={
        Property(name="SimpleNameCS139", type=qvtoperational_cst_VariableInitializationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_VariableInitializationCS138", type=SimpleNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeCS140: BinaryAssociation = BinaryAssociation(
    name="typeCS140",
    ends={
        Property(name="TypeCS142", type=qvtoperational_cst_VariableInitializationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_VariableInitializationCS141", type=TypeCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lValueCS143: BinaryAssociation = BinaryAssociation(
    name="lValueCS143",
    ends={
        Property(name="OCLExpressionCS144", type=qvtoperational_cst_AssignStatementCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_AssignStatementCS", type=OCLExpressionCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
oclExpressionCS145: BinaryAssociation = BinaryAssociation(
    name="oclExpressionCS145",
    ends={
        Property(name="OCLExpressionCS147", type=qvtoperational_cst_AssignStatementCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_AssignStatementCS146", type=OCLExpressionCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
oclExpressionCS148: BinaryAssociation = BinaryAssociation(
    name="oclExpressionCS148",
    ends={
        Property(name="OCLExpressionCS149", type=qvtoperational_cst_ExpressionStatementCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_ExpressionStatementCS", type=OCLExpressionCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
alternativePart126: BinaryAssociation = BinaryAssociation(
    name="alternativePart126",
    ends={
        Property(name="SwitchAltExpCS", type=qvtoperational_cst_SwitchExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_SwitchExpCS", type=SwitchAltExpCS, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
elsePart127: BinaryAssociation = BinaryAssociation(
    name="elsePart127",
    ends={
        Property(name="OCLExpressionCS129", type=qvtoperational_cst_SwitchExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_SwitchExpCS128", type=OCLExpressionCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition130: BinaryAssociation = BinaryAssociation(
    name="condition130",
    ends={
        Property(name="OCLExpressionCS131", type=qvtoperational_cst_SwitchAltExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_SwitchAltExpCS", type=OCLExpressionCS, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body132: BinaryAssociation = BinaryAssociation(
    name="body132",
    ends={
        Property(name="OCLExpressionCS134", type=qvtoperational_cst_SwitchAltExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_SwitchAltExpCS133", type=OCLExpressionCS, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
module155: BinaryAssociation = BinaryAssociation(
    name="module155",
    ends={
        Property(name="SimpleNameCS156", type=qvtoperational_cst_ImperativeOperationCallExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_ImperativeOperationCallExpCS", type=SimpleNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target157: BinaryAssociation = BinaryAssociation(
    name="target157",
    ends={
        Property(name="VariableCS158", type=qvtoperational_cst_ResolveExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_ResolveExpCS", type=VariableCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition159: BinaryAssociation = BinaryAssociation(
    name="condition159",
    ends={
        Property(name="OCLExpressionCS161", type=qvtoperational_cst_ResolveExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_ResolveExpCS160", type=OCLExpressionCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
inMappingType162: BinaryAssociation = BinaryAssociation(
    name="inMappingType162",
    ends={
        Property(name="TypeCS163", type=qvtoperational_cst_ResolveInExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_ResolveInExpCS", type=TypeCS, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
inMappingName164: BinaryAssociation = BinaryAssociation(
    name="inMappingName164",
    ends={
        Property(name="SimpleNameCS166", type=qvtoperational_cst_ResolveInExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_ResolveInExpCS165", type=SimpleNameCS, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
simpleNameCS150: BinaryAssociation = BinaryAssociation(
    name="simpleNameCS150",
    ends={
        Property(name="SimpleNameCS151", type=qvtoperational_cst_ObjectExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_ObjectExpCS", type=SimpleNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expressions152: BinaryAssociation = BinaryAssociation(
    name="expressions152",
    ends={
        Property(name="OCLExpressionCS154", type=qvtoperational_cst_ObjectExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_ObjectExpCS153", type=OCLExpressionCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
whereStatements174: BinaryAssociation = BinaryAssociation(
    name="whereStatements174",
    ends={
        Property(name="qvtoperational_cst_ModelTypeCS175", type=OCLExpressionCS, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="OCLExpressionCS176", type=qvtoperational_cst_ModelTypeCS, multiplicity=Multiplicity(1, 1))
    }
)
pathNameCS177: BinaryAssociation = BinaryAssociation(
    name="pathNameCS177",
    ends={
        Property(name="PathNameCS178", type=qvtoperational_cst_PackageRefCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_PackageRefCS", type=PathNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
uriCS179: BinaryAssociation = BinaryAssociation(
    name="uriCS179",
    ends={
        Property(name="StringLiteralExpCS181", type=qvtoperational_cst_PackageRefCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_PackageRefCS180", type=StringLiteralExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pathNameCS182: BinaryAssociation = BinaryAssociation(
    name="pathNameCS182",
    ends={
        Property(name="PathNameCS183", type=qvtoperational_cst_TransformationHeaderCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_TransformationHeaderCS", type=PathNameCS, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameters184: BinaryAssociation = BinaryAssociation(
    name="parameters184",
    ends={
        Property(name="ParameterDeclarationCS186", type=qvtoperational_cst_TransformationHeaderCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_TransformationHeaderCS185", type=ParameterDeclarationCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
moduleUsages187: BinaryAssociation = BinaryAssociation(
    name="moduleUsages187",
    ends={
        Property(name="ModuleUsageCS", type=qvtoperational_cst_TransformationHeaderCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_TransformationHeaderCS188", type=ModuleUsageCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transformationRefineCS189: BinaryAssociation = BinaryAssociation(
    name="transformationRefineCS189",
    ends={
        Property(name="TransformationRefineCS", type=qvtoperational_cst_TransformationHeaderCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_TransformationHeaderCS190", type=TransformationRefineCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
identifierCS167: BinaryAssociation = BinaryAssociation(
    name="identifierCS167",
    ends={
        Property(name="SimpleNameCS168", type=qvtoperational_cst_ModelTypeCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_ModelTypeCS", type=SimpleNameCS, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
complianceKindCS169: BinaryAssociation = BinaryAssociation(
    name="complianceKindCS169",
    ends={
        Property(name="StringLiteralExpCS171", type=qvtoperational_cst_ModelTypeCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_ModelTypeCS170", type=StringLiteralExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
packageRefs172: BinaryAssociation = BinaryAssociation(
    name="packageRefs172",
    ends={
        Property(name="PackageRefCS", type=qvtoperational_cst_ModelTypeCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_ModelTypeCS173", type=PackageRefCS, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
moduleKindCS196: BinaryAssociation = BinaryAssociation(
    name="moduleKindCS196",
    ends={
        Property(name="ModuleKindCS", type=qvtoperational_cst_ModuleUsageCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_ModuleUsageCS", type=ModuleKindCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
moduleRefs197: BinaryAssociation = BinaryAssociation(
    name="moduleRefs197",
    ends={
        Property(name="ModuleRefCS", type=qvtoperational_cst_ModuleUsageCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_ModuleUsageCS198", type=ModuleRefCS, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
moduleRefCS199: BinaryAssociation = BinaryAssociation(
    name="moduleRefCS199",
    ends={
        Property(name="ModuleRefCS200", type=qvtoperational_cst_TransformationRefineCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_TransformationRefineCS", type=ModuleRefCS, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
simpleNameCS201: BinaryAssociation = BinaryAssociation(
    name="simpleNameCS201",
    ends={
        Property(name="SimpleNameCS203", type=qvtoperational_cst_TransformationRefineCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_TransformationRefineCS202", type=SimpleNameCS, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
typeCS204: BinaryAssociation = BinaryAssociation(
    name="typeCS204",
    ends={
        Property(name="TypeCS205", type=qvtoperational_cst_TypeSpecCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_TypeSpecCS", type=TypeCS, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
simpleNameCS206: BinaryAssociation = BinaryAssociation(
    name="simpleNameCS206",
    ends={
        Property(name="SimpleNameCS208", type=qvtoperational_cst_TypeSpecCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_TypeSpecCS207", type=SimpleNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition209: BinaryAssociation = BinaryAssociation(
    name="condition209",
    ends={
        Property(name="OCLExpressionCS210", type=qvtoperational_cst_LogExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_LogExpCS", type=OCLExpressionCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pathNameCS191: BinaryAssociation = BinaryAssociation(
    name="pathNameCS191",
    ends={
        Property(name="PathNameCS192", type=qvtoperational_cst_ModuleRefCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_ModuleRefCS", type=PathNameCS, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameters193: BinaryAssociation = BinaryAssociation(
    name="parameters193",
    ends={
        Property(name="ParameterDeclarationCS195", type=qvtoperational_cst_ModuleRefCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_ModuleRefCS194", type=ParameterDeclarationCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value218: BinaryAssociation = BinaryAssociation(
    name="value218",
    ends={
        Property(name="OCLExpressionCS219", type=qvtoperational_cst_ReturnExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_ReturnExpCS", type=OCLExpressionCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value232: BinaryAssociation = BinaryAssociation(
    name="value232",
    ends={
        Property(name="TypeCS234", type=qvtoperational_cst_DictionaryTypeCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_DictionaryTypeCS233", type=TypeCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
mappingIdentifiers220: BinaryAssociation = BinaryAssociation(
    name="mappingIdentifiers220",
    ends={
        Property(name="ScopedNameCS221", type=qvtoperational_cst_MappingExtensionCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_MappingExtensionCS", type=ScopedNameCS, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
typeSpecCS222: BinaryAssociation = BinaryAssociation(
    name="typeSpecCS222",
    ends={
        Property(name="TypeSpecCS223", type=qvtoperational_cst_InstantiationExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_InstantiationExpCS", type=TypeSpecCS, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
arguments224: BinaryAssociation = BinaryAssociation(
    name="arguments224",
    ends={
        Property(name="OCLExpressionCS226", type=qvtoperational_cst_InstantiationExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_InstantiationExpCS225", type=OCLExpressionCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeCS227: BinaryAssociation = BinaryAssociation(
    name="typeCS227",
    ends={
        Property(name="TypeCS228", type=qvtoperational_cst_ListTypeCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_ListTypeCS", type=TypeCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assertion211: BinaryAssociation = BinaryAssociation(
    name="assertion211",
    ends={
        Property(name="OCLExpressionCS212", type=qvtoperational_cst_AssertExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_AssertExpCS", type=OCLExpressionCS, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
collectionLiteralParts229: BinaryAssociation = BinaryAssociation(
    name="collectionLiteralParts229",
    ends={
        Property(name="CollectionLiteralPartCS", type=qvtoperational_cst_ListLiteralExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_ListLiteralExpCS", type=CollectionLiteralPartCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
log213: BinaryAssociation = BinaryAssociation(
    name="log213",
    ends={
        Property(name="LogExpCS", type=qvtoperational_cst_AssertExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_AssertExpCS214", type=LogExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
key230: BinaryAssociation = BinaryAssociation(
    name="key230",
    ends={
        Property(name="TypeCS231", type=qvtoperational_cst_DictionaryTypeCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_DictionaryTypeCS", type=TypeCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
severity215: BinaryAssociation = BinaryAssociation(
    name="severity215",
    ends={
        Property(name="SimpleNameCS217", type=qvtoperational_cst_AssertExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_AssertExpCS216", type=SimpleNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parts235: BinaryAssociation = BinaryAssociation(
    name="parts235",
    ends={
        Property(name="DictLiteralPartCS", type=qvtoperational_cst_DictLiteralExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_DictLiteralExpCS", type=DictLiteralPartCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
topLevelElements248: BinaryAssociation = BinaryAssociation(
    name="topLevelElements248",
    ends={
        Property(name="CSTNode", type=qvtoperational_cst_UnitCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_UnitCS", type=CSTNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
key236: BinaryAssociation = BinaryAssociation(
    name="key236",
    ends={
        Property(name="LiteralExpCS", type=qvtoperational_cst_DictLiteralPartCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_DictLiteralPartCS", type=LiteralExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
modules249: BinaryAssociation = BinaryAssociation(
    name="modules249",
    ends={
        Property(name="MappingModuleCS", type=qvtoperational_cst_UnitCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_UnitCS250", type=MappingModuleCS, multiplicity=Multiplicity(0, 9999))
    }
)
modelTypes251: BinaryAssociation = BinaryAssociation(
    name="modelTypes251",
    ends={
        Property(name="ModelTypeCS253", type=qvtoperational_cst_UnitCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_UnitCS252", type=ModelTypeCS, multiplicity=Multiplicity(0, 9999))
    }
)
value237: BinaryAssociation = BinaryAssociation(
    name="value237",
    ends={
        Property(name="OCLExpressionCS239", type=qvtoperational_cst_DictLiteralPartCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_DictLiteralPartCS238", type=OCLExpressionCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name240: BinaryAssociation = BinaryAssociation(
    name="name240",
    ends={
        Property(name="StringLiteralExpCS241", type=qvtoperational_cst_TagCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_TagCS", type=StringLiteralExpCS, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
scopedNameCS242: BinaryAssociation = BinaryAssociation(
    name="scopedNameCS242",
    ends={
        Property(name="ScopedNameCS244", type=qvtoperational_cst_TagCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_TagCS243", type=ScopedNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
oclExpressionCS245: BinaryAssociation = BinaryAssociation(
    name="oclExpressionCS245",
    ends={
        Property(name="OCLExpressionCS247", type=qvtoperational_cst_TagCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_TagCS246", type=OCLExpressionCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tryBody264: BinaryAssociation = BinaryAssociation(
    name="tryBody264",
    ends={
        Property(name="BlockExpCS265", type=qvtoperational_cst_TryExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_TryExpCS", type=BlockExpCS, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
exceptClauses266: BinaryAssociation = BinaryAssociation(
    name="exceptClauses266",
    ends={
        Property(name="CatchExpCS", type=qvtoperational_cst_TryExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_TryExpCS267", type=CatchExpCS, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
body268: BinaryAssociation = BinaryAssociation(
    name="body268",
    ends={
        Property(name="BlockExpCS269", type=qvtoperational_cst_CatchExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_CatchExpCS", type=BlockExpCS, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
exceptions270: BinaryAssociation = BinaryAssociation(
    name="exceptions270",
    ends={
        Property(name="TypeCS272", type=qvtoperational_cst_CatchExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_CatchExpCS271", type=TypeCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
simpleNameCS273: BinaryAssociation = BinaryAssociation(
    name="simpleNameCS273",
    ends={
        Property(name="SimpleNameCS275", type=qvtoperational_cst_CatchExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_CatchExpCS274", type=SimpleNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exception276: BinaryAssociation = BinaryAssociation(
    name="exception276",
    ends={
        Property(name="TypeCS277", type=qvtoperational_cst_RaiseExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_RaiseExpCS", type=TypeCS, multiplicity=Multiplicity(1, 1))
    }
)
imports254: BinaryAssociation = BinaryAssociation(
    name="imports254",
    ends={
        Property(name="ImportCS256", type=qvtoperational_cst_UnitCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_UnitCS255", type=ImportCS, multiplicity=Multiplicity(0, 9999))
    }
)
target257: BinaryAssociation = BinaryAssociation(
    name="target257",
    ends={
        Property(name="VariableCS258", type=qvtoperational_cst_ResolveOpArgsExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_ResolveOpArgsExpCS", type=VariableCS, multiplicity=Multiplicity(0, 1))
    }
)
condition259: BinaryAssociation = BinaryAssociation(
    name="condition259",
    ends={
        Property(name="OCLExpressionCS261", type=qvtoperational_cst_ResolveOpArgsExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_ResolveOpArgsExpCS260", type=OCLExpressionCS, multiplicity=Multiplicity(0, 1))
    }
)
typeCS262: BinaryAssociation = BinaryAssociation(
    name="typeCS262",
    ends={
        Property(name="TypeCS263", type=qvtoperational_cst_ScopedNameCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_ScopedNameCS", type=TypeCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
argument278: BinaryAssociation = BinaryAssociation(
    name="argument278",
    ends={
        Property(name="OCLExpressionCS280", type=qvtoperational_cst_RaiseExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_RaiseExpCS279", type=OCLExpressionCS, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_qvtoperational_cst_LibraryCS_MappingModuleCS = Generalization(general=MappingModuleCS, specific=qvtoperational_cst_LibraryCS)
gen_qvtoperational_cst_ImportCS_CSTNode = Generalization(general=CSTNode, specific=qvtoperational_cst_ImportCS)
gen_qvtoperational_cst_LibraryImportCS_ImportCS = Generalization(general=ImportCS, specific=qvtoperational_cst_LibraryImportCS)
gen_qvtoperational_cst_RenameCS_CSTNode = Generalization(general=CSTNode, specific=qvtoperational_cst_RenameCS)
gen_qvtoperational_cst_MappingModuleCS_CSTNode = Generalization(general=CSTNode, specific=qvtoperational_cst_MappingModuleCS)
gen_qvtoperational_cst_ConfigPropertyCS_ModulePropertyCS = Generalization(general=ModulePropertyCS, specific=qvtoperational_cst_ConfigPropertyCS)
gen_qvtoperational_cst_LocalPropertyCS_ModulePropertyCS = Generalization(general=ModulePropertyCS, specific=qvtoperational_cst_LocalPropertyCS)
gen_qvtoperational_cst_ContextualPropertyCS_ModulePropertyCS = Generalization(general=ModulePropertyCS, specific=qvtoperational_cst_ContextualPropertyCS)
gen_qvtoperational_cst_ClassifierDefCS_CSTNode = Generalization(general=CSTNode, specific=qvtoperational_cst_ClassifierDefCS)
gen_qvtoperational_cst_ModulePropertyCS_CSTNode = Generalization(general=CSTNode, specific=qvtoperational_cst_ModulePropertyCS)
gen_qvtoperational_cst_IntermediateClassDefCS_ClassifierDefCS = Generalization(general=ClassifierDefCS, specific=qvtoperational_cst_IntermediateClassDefCS)
gen_qvtoperational_cst_ExceptionDefCS_ClassifierDefCS = Generalization(general=ClassifierDefCS, specific=qvtoperational_cst_ExceptionDefCS)
gen_qvtoperational_cst_OppositePropertyCS_CSTNode = Generalization(general=CSTNode, specific=qvtoperational_cst_OppositePropertyCS)
gen_qvtoperational_cst_MultiplicityDefCS_CSTNode = Generalization(general=CSTNode, specific=qvtoperational_cst_MultiplicityDefCS)
gen_qvtoperational_cst_MappingDeclarationCS_CSTNode = Generalization(general=CSTNode, specific=qvtoperational_cst_MappingDeclarationCS)
gen_qvtoperational_cst_ClassifierPropertyCS_LocalPropertyCS = Generalization(general=LocalPropertyCS, specific=qvtoperational_cst_ClassifierPropertyCS)
gen_qvtoperational_cst_ParameterDeclarationCS_CSTNode = Generalization(general=CSTNode, specific=qvtoperational_cst_ParameterDeclarationCS)
gen_qvtoperational_cst_SimpleSignatureCS_CSTNode = Generalization(general=CSTNode, specific=qvtoperational_cst_SimpleSignatureCS)
gen_qvtoperational_cst_CompleteSignatureCS_CSTNode = Generalization(general=CSTNode, specific=qvtoperational_cst_CompleteSignatureCS)
gen_qvtoperational_cst_MappingMethodCS_CSTNode = Generalization(general=CSTNode, specific=qvtoperational_cst_MappingMethodCS)
gen_qvtoperational_cst_MappingQueryCS_MappingMethodCS = Generalization(general=MappingMethodCS, specific=qvtoperational_cst_MappingQueryCS)
gen_qvtoperational_cst_ConstructorCS_MappingMethodCS = Generalization(general=MappingMethodCS, specific=qvtoperational_cst_ConstructorCS)
gen_qvtoperational_cst_MappingSectionCS_cst_CSTNode = Generalization(general=cst_CSTNode, specific=qvtoperational_cst_MappingSectionCS)
gen_qvtoperational_cst_MappingSectionCS_cst_ElementWithBody = Generalization(general=cst_ElementWithBody, specific=qvtoperational_cst_MappingSectionCS)
gen_qvtoperational_cst_MappingInitCS_MappingSectionCS = Generalization(general=MappingSectionCS, specific=qvtoperational_cst_MappingInitCS)
gen_qvtoperational_cst_MappingEndCS_MappingSectionCS = Generalization(general=MappingSectionCS, specific=qvtoperational_cst_MappingEndCS)
gen_qvtoperational_cst_MappingSectionsCS_CSTNode = Generalization(general=CSTNode, specific=qvtoperational_cst_MappingSectionsCS)
gen_qvtoperational_cst_MappingRuleCS_MappingMethodCS = Generalization(general=MappingMethodCS, specific=qvtoperational_cst_MappingRuleCS)
gen_qvtoperational_cst_WhileExpCS_StatementCS = Generalization(general=StatementCS, specific=qvtoperational_cst_WhileExpCS)
gen_qvtoperational_cst_ImperativeLoopExpCS_cst_LoopExpCS = Generalization(general=cst_LoopExpCS, specific=qvtoperational_cst_ImperativeLoopExpCS)
gen_qvtoperational_cst_ImperativeLoopExpCS_cst_StatementCS = Generalization(general=cst_StatementCS, specific=qvtoperational_cst_ImperativeLoopExpCS)
gen_qvtoperational_cst_ForExpCS_ImperativeLoopExpCS = Generalization(general=ImperativeLoopExpCS, specific=qvtoperational_cst_ForExpCS)
gen_qvtoperational_cst_ImperativeIterateExpCS_ImperativeLoopExpCS = Generalization(general=ImperativeLoopExpCS, specific=qvtoperational_cst_ImperativeIterateExpCS)
gen_qvtoperational_cst_SwitchExpCS_StatementCS = Generalization(general=StatementCS, specific=qvtoperational_cst_SwitchExpCS)
gen_qvtoperational_cst_StatementCS_OCLExpressionCS = Generalization(general=OCLExpressionCS, specific=qvtoperational_cst_StatementCS)
gen_qvtoperational_cst_BlockExpCS_StatementCS = Generalization(general=StatementCS, specific=qvtoperational_cst_BlockExpCS)
gen_qvtoperational_cst_ComputeExpCS_StatementCS = Generalization(general=StatementCS, specific=qvtoperational_cst_ComputeExpCS)
gen_qvtoperational_cst_VariableInitializationCS_StatementCS = Generalization(general=StatementCS, specific=qvtoperational_cst_VariableInitializationCS)
gen_qvtoperational_cst_AssignStatementCS_StatementCS = Generalization(general=StatementCS, specific=qvtoperational_cst_AssignStatementCS)
gen_qvtoperational_cst_BreakExpCS_StatementCS = Generalization(general=StatementCS, specific=qvtoperational_cst_BreakExpCS)
gen_qvtoperational_cst_ContinueExpCS_StatementCS = Generalization(general=StatementCS, specific=qvtoperational_cst_ContinueExpCS)
gen_qvtoperational_cst_ExpressionStatementCS_StatementCS = Generalization(general=StatementCS, specific=qvtoperational_cst_ExpressionStatementCS)
gen_qvtoperational_cst_MappingBodyCS_MappingSectionCS = Generalization(general=MappingSectionCS, specific=qvtoperational_cst_MappingBodyCS)
gen_qvtoperational_cst_SwitchAltExpCS_StatementCS = Generalization(general=StatementCS, specific=qvtoperational_cst_SwitchAltExpCS)
gen_qvtoperational_cst_ImperativeOperationCallExpCS_OperationCallExpCS = Generalization(general=OperationCallExpCS, specific=qvtoperational_cst_ImperativeOperationCallExpCS)
gen_qvtoperational_cst_DirectionKindCS_CSTNode = Generalization(general=CSTNode, specific=qvtoperational_cst_DirectionKindCS)
gen_qvtoperational_cst_ResolveExpCS_CallExpCS = Generalization(general=CallExpCS, specific=qvtoperational_cst_ResolveExpCS)
gen_qvtoperational_cst_ResolveInExpCS_ResolveExpCS = Generalization(general=ResolveExpCS, specific=qvtoperational_cst_ResolveInExpCS)
gen_qvtoperational_cst_ObjectExpCS_cst_InstantiationExpCS = Generalization(general=cst_InstantiationExpCS, specific=qvtoperational_cst_ObjectExpCS)
gen_qvtoperational_cst_ObjectExpCS_cst_ElementWithBody = Generalization(general=cst_ElementWithBody, specific=qvtoperational_cst_ObjectExpCS)
gen_qvtoperational_cst_MappingCallExpCS_ImperativeOperationCallExpCS = Generalization(general=ImperativeOperationCallExpCS, specific=qvtoperational_cst_MappingCallExpCS)
gen_qvtoperational_cst_PackageRefCS_CSTNode = Generalization(general=CSTNode, specific=qvtoperational_cst_PackageRefCS)
gen_qvtoperational_cst_TransformationHeaderCS_CSTNode = Generalization(general=CSTNode, specific=qvtoperational_cst_TransformationHeaderCS)
gen_qvtoperational_cst_ModelTypeCS_cst_CSTNode = Generalization(general=cst_CSTNode, specific=qvtoperational_cst_ModelTypeCS)
gen_qvtoperational_cst_ModelTypeCS_cst_ElementWithBody = Generalization(general=cst_ElementWithBody, specific=qvtoperational_cst_ModelTypeCS)
gen_qvtoperational_cst_ModuleUsageCS_CSTNode = Generalization(general=CSTNode, specific=qvtoperational_cst_ModuleUsageCS)
gen_qvtoperational_cst_TransformationRefineCS_CSTNode = Generalization(general=CSTNode, specific=qvtoperational_cst_TransformationRefineCS)
gen_qvtoperational_cst_TypeSpecCS_CSTNode = Generalization(general=CSTNode, specific=qvtoperational_cst_TypeSpecCS)
gen_qvtoperational_cst_LogExpCS_OperationCallExpCS = Generalization(general=OperationCallExpCS, specific=qvtoperational_cst_LogExpCS)
gen_qvtoperational_cst_ModuleKindCS_CSTNode = Generalization(general=CSTNode, specific=qvtoperational_cst_ModuleKindCS)
gen_qvtoperational_cst_ModuleRefCS_CSTNode = Generalization(general=CSTNode, specific=qvtoperational_cst_ModuleRefCS)
gen_qvtoperational_cst_MappingExtensionCS_CSTNode = Generalization(general=CSTNode, specific=qvtoperational_cst_MappingExtensionCS)
gen_qvtoperational_cst_InstantiationExpCS_StatementCS = Generalization(general=StatementCS, specific=qvtoperational_cst_InstantiationExpCS)
gen_qvtoperational_cst_ListTypeCS_TypeCS = Generalization(general=TypeCS, specific=qvtoperational_cst_ListTypeCS)
gen_qvtoperational_cst_AssertExpCS_StatementCS = Generalization(general=StatementCS, specific=qvtoperational_cst_AssertExpCS)
gen_qvtoperational_cst_ListLiteralExpCS_LiteralExpCS = Generalization(general=LiteralExpCS, specific=qvtoperational_cst_ListLiteralExpCS)
gen_qvtoperational_cst_DictionaryTypeCS_TypeCS = Generalization(general=TypeCS, specific=qvtoperational_cst_DictionaryTypeCS)
gen_qvtoperational_cst_ReturnExpCS_StatementCS = Generalization(general=StatementCS, specific=qvtoperational_cst_ReturnExpCS)
gen_qvtoperational_cst_UnitCS_CSTNode = Generalization(general=CSTNode, specific=qvtoperational_cst_UnitCS)
gen_qvtoperational_cst_DictLiteralExpCS_LiteralExpCS = Generalization(general=LiteralExpCS, specific=qvtoperational_cst_DictLiteralExpCS)
gen_qvtoperational_cst_DictLiteralPartCS_CSTNode = Generalization(general=CSTNode, specific=qvtoperational_cst_DictLiteralPartCS)
gen_qvtoperational_cst_TagCS_CSTNode = Generalization(general=CSTNode, specific=qvtoperational_cst_TagCS)
gen_qvtoperational_cst_TryExpCS_StatementCS = Generalization(general=StatementCS, specific=qvtoperational_cst_TryExpCS)
gen_qvtoperational_cst_CatchExpCS_CSTNode = Generalization(general=CSTNode, specific=qvtoperational_cst_CatchExpCS)
gen_qvtoperational_cst_RaiseExpCS_StatementCS = Generalization(general=StatementCS, specific=qvtoperational_cst_RaiseExpCS)
gen_qvtoperational_cst_ResolveOpArgsExpCS_CSTNode = Generalization(general=CSTNode, specific=qvtoperational_cst_ResolveOpArgsExpCS)
gen_qvtoperational_cst_ScopedNameCS_CSTNode = Generalization(general=CSTNode, specific=qvtoperational_cst_ScopedNameCS)

# Domain Model
domain_model = DomainModel(
    name="qvtoperational",
    types={RenameCS, ModulePropertyCS, MappingMethodCS, ClassifierDefCS, TagCS, qvtoperational_cst_LibraryCS, MappingModuleCS, qvtoperational_cst_ImportCS, PathNameCS, qvtoperational_cst_LibraryImportCS, qvtoperational_cst_RenameCS, qvtoperational_cst_MappingModuleCS, CSTNode, TransformationHeaderCS, ImportCS, ModelTypeCS, qvtoperational_cst_ConfigPropertyCS, qvtoperational_cst_LocalPropertyCS, OCLExpressionCS, qvtoperational_cst_ContextualPropertyCS, ScopedNameCS, qvtoperational_cst_ClassifierDefCS, TypeCS, SimpleNameCS, StringLiteralExpCS, qvtoperational_cst_ModulePropertyCS, MultiplicityDefCS, OppositePropertyCS, qvtoperational_cst_IntermediateClassDefCS, qvtoperational_cst_ExceptionDefCS, qvtoperational_cst_OppositePropertyCS, qvtoperational_cst_MultiplicityDefCS, PrimitiveLiteralExpCS, qvtoperational_cst_MappingDeclarationCS, ClassifierPropertyCS, qvtoperational_cst_ClassifierPropertyCS, LocalPropertyCS, qvtoperational_cst_ParameterDeclarationCS, TypeSpecCS, qvtoperational_cst_SimpleSignatureCS, qvtoperational_cst_CompleteSignatureCS, SimpleSignatureCS, qvtoperational_cst_MappingMethodCS, ParameterDeclarationCS, DirectionKindCS, MappingExtensionCS, qvtoperational_cst_MappingQueryCS, BlockExpCS, qvtoperational_cst_ConstructorCS, qvtoperational_cst_MappingSectionCS, cst_CSTNode, cst_ElementWithBody, MappingRuleCS, qvtoperational_cst_MappingInitCS, MappingSectionCS, qvtoperational_cst_MappingEndCS, qvtoperational_cst_MappingSectionsCS, MappingInitCS, MappingBodyCS, MappingEndCS, MappingDeclarationCS, qvtoperational_cst_MappingRuleCS, MappingSectionsCS, VariableCS, qvtoperational_cst_WhileExpCS, qvtoperational_cst_ImperativeLoopExpCS, cst_LoopExpCS, cst_StatementCS, qvtoperational_cst_ForExpCS, ImperativeLoopExpCS, qvtoperational_cst_ImperativeIterateExpCS, qvtoperational_cst_SwitchExpCS, SwitchAltExpCS, qvtoperational_cst_StatementCS, qvtoperational_cst_BlockExpCS, StatementCS, qvtoperational_cst_ComputeExpCS, qvtoperational_cst_AssignStatementCS, qvtoperational_cst_BreakExpCS, qvtoperational_cst_ContinueExpCS, qvtoperational_cst_ExpressionStatementCS, qvtoperational_cst_MappingBodyCS, qvtoperational_cst_ObjectExpCS, qvtoperational_cst_SwitchAltExpCS, qvtoperational_cst_VariableInitializationCS, OperationCallExpCS, qvtoperational_cst_DirectionKindCS, qvtoperational_cst_ElementWithBody, qvtoperational_cst_ResolveExpCS, CallExpCS, qvtoperational_cst_ResolveInExpCS, ResolveExpCS, cst_InstantiationExpCS, qvtoperational_cst_MappingCallExpCS, ImperativeOperationCallExpCS, qvtoperational_cst_ImperativeOperationCallExpCS, qvtoperational_cst_PackageRefCS, qvtoperational_cst_TransformationHeaderCS, ModuleUsageCS, TransformationRefineCS, qvtoperational_cst_ModelTypeCS, PackageRefCS, qvtoperational_cst_ModuleUsageCS, ModuleKindCS, ModuleRefCS, qvtoperational_cst_TransformationRefineCS, qvtoperational_cst_TypeSpecCS, qvtoperational_cst_LogExpCS, qvtoperational_cst_ModuleKindCS, qvtoperational_cst_ModuleRefCS, qvtoperational_cst_MappingExtensionCS, qvtoperational_cst_DictLiteralExpCS, qvtoperational_cst_InstantiationExpCS, qvtoperational_cst_ListTypeCS, qvtoperational_cst_ListLiteralExpCS, qvtoperational_cst_AssertExpCS, LiteralExpCS, CollectionLiteralPartCS, qvtoperational_cst_DictionaryTypeCS, LogExpCS, qvtoperational_cst_ReturnExpCS, qvtoperational_cst_UnitCS, DictLiteralPartCS, qvtoperational_cst_DictLiteralPartCS, qvtoperational_cst_TagCS, qvtoperational_cst_TryExpCS, CatchExpCS, qvtoperational_cst_CatchExpCS, qvtoperational_cst_RaiseExpCS, qvtoperational_cst_ResolveOpArgsExpCS, qvtoperational_cst_ScopedNameCS, DirectionKindEnum, ModuleKindEnum, ImportKindEnum, MappingExtensionKindCS, QualifierKindCS},
    associations={metamodels3, renamings5, properties7, methods9, classifierDefCS11, tags13, pathNameCS15, headerCS0, imports1, typeCS23, typeCS25, oclExpressionCS27, scopedNameCS29, typeCS30, oclExpressionCS33, simpleNameCS36, extends38, typeCS16, simpleNameCS17, originalName19, simpleNameCS21, multiplicity51, opposite53, simpleNameCS55, multiplicity57, lowerBound60, upperBound61, simpleNameCS64, properties41, tags43, stereotypeQualifiers46, featureKeys48, simpleNameCS78, typeSpecCS80, params82, simpleSignature84, resultParams85, contextType66, parameters69, result71, directionKindCS74, mappingExtension76, body96, body97, statements99, mappingRuleCS101, mappingInitCS103, mappingBodyCS104, mappingEndCS106, mappingDeclarationCS88, guards89, posts91, mappingBody94, returnedElement110, body111, body114, condition116, resultVar119, condition122, target124, bodyExpressions108, oclExpressionCS135, simpleNameCS137, typeCS140, lValueCS143, oclExpressionCS145, oclExpressionCS148, alternativePart126, elsePart127, condition130, body132, module155, target157, condition159, inMappingType162, inMappingName164, simpleNameCS150, expressions152, whereStatements174, pathNameCS177, uriCS179, pathNameCS182, parameters184, moduleUsages187, transformationRefineCS189, identifierCS167, complianceKindCS169, packageRefs172, moduleKindCS196, moduleRefs197, moduleRefCS199, simpleNameCS201, typeCS204, simpleNameCS206, condition209, pathNameCS191, parameters193, value218, value232, mappingIdentifiers220, typeSpecCS222, arguments224, typeCS227, assertion211, collectionLiteralParts229, log213, key230, severity215, parts235, topLevelElements248, key236, modules249, modelTypes251, value237, name240, scopedNameCS242, oclExpressionCS245, tryBody264, exceptClauses266, body268, exceptions270, simpleNameCS273, exception276, imports254, target257, condition259, typeCS262, argument278},
    generalizations={gen_qvtoperational_cst_LibraryCS_MappingModuleCS, gen_qvtoperational_cst_ImportCS_CSTNode, gen_qvtoperational_cst_LibraryImportCS_ImportCS, gen_qvtoperational_cst_RenameCS_CSTNode, gen_qvtoperational_cst_MappingModuleCS_CSTNode, gen_qvtoperational_cst_ConfigPropertyCS_ModulePropertyCS, gen_qvtoperational_cst_LocalPropertyCS_ModulePropertyCS, gen_qvtoperational_cst_ContextualPropertyCS_ModulePropertyCS, gen_qvtoperational_cst_ClassifierDefCS_CSTNode, gen_qvtoperational_cst_ModulePropertyCS_CSTNode, gen_qvtoperational_cst_IntermediateClassDefCS_ClassifierDefCS, gen_qvtoperational_cst_ExceptionDefCS_ClassifierDefCS, gen_qvtoperational_cst_OppositePropertyCS_CSTNode, gen_qvtoperational_cst_MultiplicityDefCS_CSTNode, gen_qvtoperational_cst_MappingDeclarationCS_CSTNode, gen_qvtoperational_cst_ClassifierPropertyCS_LocalPropertyCS, gen_qvtoperational_cst_ParameterDeclarationCS_CSTNode, gen_qvtoperational_cst_SimpleSignatureCS_CSTNode, gen_qvtoperational_cst_CompleteSignatureCS_CSTNode, gen_qvtoperational_cst_MappingMethodCS_CSTNode, gen_qvtoperational_cst_MappingQueryCS_MappingMethodCS, gen_qvtoperational_cst_ConstructorCS_MappingMethodCS, gen_qvtoperational_cst_MappingSectionCS_cst_CSTNode, gen_qvtoperational_cst_MappingSectionCS_cst_ElementWithBody, gen_qvtoperational_cst_MappingInitCS_MappingSectionCS, gen_qvtoperational_cst_MappingEndCS_MappingSectionCS, gen_qvtoperational_cst_MappingSectionsCS_CSTNode, gen_qvtoperational_cst_MappingRuleCS_MappingMethodCS, gen_qvtoperational_cst_WhileExpCS_StatementCS, gen_qvtoperational_cst_ImperativeLoopExpCS_cst_LoopExpCS, gen_qvtoperational_cst_ImperativeLoopExpCS_cst_StatementCS, gen_qvtoperational_cst_ForExpCS_ImperativeLoopExpCS, gen_qvtoperational_cst_ImperativeIterateExpCS_ImperativeLoopExpCS, gen_qvtoperational_cst_SwitchExpCS_StatementCS, gen_qvtoperational_cst_StatementCS_OCLExpressionCS, gen_qvtoperational_cst_BlockExpCS_StatementCS, gen_qvtoperational_cst_ComputeExpCS_StatementCS, gen_qvtoperational_cst_VariableInitializationCS_StatementCS, gen_qvtoperational_cst_AssignStatementCS_StatementCS, gen_qvtoperational_cst_BreakExpCS_StatementCS, gen_qvtoperational_cst_ContinueExpCS_StatementCS, gen_qvtoperational_cst_ExpressionStatementCS_StatementCS, gen_qvtoperational_cst_MappingBodyCS_MappingSectionCS, gen_qvtoperational_cst_SwitchAltExpCS_StatementCS, gen_qvtoperational_cst_ImperativeOperationCallExpCS_OperationCallExpCS, gen_qvtoperational_cst_DirectionKindCS_CSTNode, gen_qvtoperational_cst_ResolveExpCS_CallExpCS, gen_qvtoperational_cst_ResolveInExpCS_ResolveExpCS, gen_qvtoperational_cst_ObjectExpCS_cst_InstantiationExpCS, gen_qvtoperational_cst_ObjectExpCS_cst_ElementWithBody, gen_qvtoperational_cst_MappingCallExpCS_ImperativeOperationCallExpCS, gen_qvtoperational_cst_PackageRefCS_CSTNode, gen_qvtoperational_cst_TransformationHeaderCS_CSTNode, gen_qvtoperational_cst_ModelTypeCS_cst_CSTNode, gen_qvtoperational_cst_ModelTypeCS_cst_ElementWithBody, gen_qvtoperational_cst_ModuleUsageCS_CSTNode, gen_qvtoperational_cst_TransformationRefineCS_CSTNode, gen_qvtoperational_cst_TypeSpecCS_CSTNode, gen_qvtoperational_cst_LogExpCS_OperationCallExpCS, gen_qvtoperational_cst_ModuleKindCS_CSTNode, gen_qvtoperational_cst_ModuleRefCS_CSTNode, gen_qvtoperational_cst_MappingExtensionCS_CSTNode, gen_qvtoperational_cst_InstantiationExpCS_StatementCS, gen_qvtoperational_cst_ListTypeCS_TypeCS, gen_qvtoperational_cst_AssertExpCS_StatementCS, gen_qvtoperational_cst_ListLiteralExpCS_LiteralExpCS, gen_qvtoperational_cst_DictionaryTypeCS_TypeCS, gen_qvtoperational_cst_ReturnExpCS_StatementCS, gen_qvtoperational_cst_UnitCS_CSTNode, gen_qvtoperational_cst_DictLiteralExpCS_LiteralExpCS, gen_qvtoperational_cst_DictLiteralPartCS_CSTNode, gen_qvtoperational_cst_TagCS_CSTNode, gen_qvtoperational_cst_TryExpCS_StatementCS, gen_qvtoperational_cst_CatchExpCS_CSTNode, gen_qvtoperational_cst_RaiseExpCS_StatementCS, gen_qvtoperational_cst_ResolveOpArgsExpCS_CSTNode, gen_qvtoperational_cst_ScopedNameCS_CSTNode},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)