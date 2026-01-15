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

ImportKindEnum: Enumeration = Enumeration(
    name="ImportKindEnum",
    literals={
            EnumerationLiteral(name="extension"),
			EnumerationLiteral(name="access")
    }
)

ModuleKindEnum: Enumeration = Enumeration(
    name="ModuleKindEnum",
    literals={
            EnumerationLiteral(name="transformation"),
			EnumerationLiteral(name="library")
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
qvtoperational_cst_MappingModuleCS = Class(name="qvtoperational::cst::MappingModuleCS")
CSTNode = Class(name="CSTNode")
TransformationHeaderCS = Class(name="TransformationHeaderCS")
ImportCS = Class(name="ImportCS")
ModelTypeCS = Class(name="ModelTypeCS")
RenameCS = Class(name="RenameCS")
ModulePropertyCS = Class(name="ModulePropertyCS")
MappingMethodCS = Class(name="MappingMethodCS")
ClassifierDefCS = Class(name="ClassifierDefCS")
SimpleNameCS = Class(name="SimpleNameCS")
StringLiteralExpCS = Class(name="StringLiteralExpCS")
qvtoperational_cst_ModulePropertyCS = Class(name="qvtoperational::cst::ModulePropertyCS", is_abstract=True)
qvtoperational_cst_ConfigPropertyCS = Class(name="qvtoperational::cst::ConfigPropertyCS")
qvtoperational_cst_LocalPropertyCS = Class(name="qvtoperational::cst::LocalPropertyCS")
OCLExpressionCS = Class(name="OCLExpressionCS")
qvtoperational_cst_ContextualPropertyCS = Class(name="qvtoperational::cst::ContextualPropertyCS")
ScopedNameCS = Class(name="ScopedNameCS")
qvtoperational_cst_ClassifierDefCS = Class(name="qvtoperational::cst::ClassifierDefCS")
TagCS = Class(name="TagCS")
qvtoperational_cst_LibraryCS = Class(name="qvtoperational::cst::LibraryCS")
MappingModuleCS = Class(name="MappingModuleCS")
qvtoperational_cst_ImportCS = Class(name="qvtoperational::cst::ImportCS")
PathNameCS = Class(name="PathNameCS")
qvtoperational_cst_LibraryImportCS = Class(name="qvtoperational::cst::LibraryImportCS")
qvtoperational_cst_RenameCS = Class(name="qvtoperational::cst::RenameCS")
TypeCS = Class(name="TypeCS")
MultiplicityDefCS = Class(name="MultiplicityDefCS")
OppositePropertyCS = Class(name="OppositePropertyCS")
qvtoperational_cst_OppositePropertyCS = Class(name="qvtoperational::cst::OppositePropertyCS")
qvtoperational_cst_MultiplicityDefCS = Class(name="qvtoperational::cst::MultiplicityDefCS")
PrimitiveLiteralExpCS = Class(name="PrimitiveLiteralExpCS")
qvtoperational_cst_MappingDeclarationCS = Class(name="qvtoperational::cst::MappingDeclarationCS")
ClassifierPropertyCS = Class(name="ClassifierPropertyCS")
qvtoperational_cst_ClassifierPropertyCS = Class(name="qvtoperational::cst::ClassifierPropertyCS")
LocalPropertyCS = Class(name="LocalPropertyCS")
TypeSpecCS = Class(name="TypeSpecCS")
qvtoperational_cst_SimpleSignatureCS = Class(name="qvtoperational::cst::SimpleSignatureCS")
qvtoperational_cst_CompleteSignatureCS = Class(name="qvtoperational::cst::CompleteSignatureCS")
SimpleSignatureCS = Class(name="SimpleSignatureCS")
qvtoperational_cst_MappingMethodCS = Class(name="qvtoperational::cst::MappingMethodCS", is_abstract=True)
MappingDeclarationCS = Class(name="MappingDeclarationCS")
qvtoperational_cst_MappingRuleCS = Class(name="qvtoperational::cst::MappingRuleCS")
ParameterDeclarationCS = Class(name="ParameterDeclarationCS")
DirectionKindCS = Class(name="DirectionKindCS")
MappingExtensionCS = Class(name="MappingExtensionCS")
qvtoperational_cst_ParameterDeclarationCS = Class(name="qvtoperational::cst::ParameterDeclarationCS")
qvtoperational_cst_MappingSectionCS = Class(name="qvtoperational::cst::MappingSectionCS", is_abstract=True)
cst_CSTNode = Class(name="cst::CSTNode")
cst_ElementWithBody = Class(name="cst::ElementWithBody")
MappingRuleCS = Class(name="MappingRuleCS")
qvtoperational_cst_MappingInitCS = Class(name="qvtoperational::cst::MappingInitCS")
MappingSectionCS = Class(name="MappingSectionCS")
qvtoperational_cst_MappingEndCS = Class(name="qvtoperational::cst::MappingEndCS")
qvtoperational_cst_MappingSectionsCS = Class(name="qvtoperational::cst::MappingSectionsCS")
MappingInitCS = Class(name="MappingInitCS")
MappingSectionsCS = Class(name="MappingSectionsCS")
qvtoperational_cst_MappingQueryCS = Class(name="qvtoperational::cst::MappingQueryCS")
qvtoperational_cst_ConstructorCS = Class(name="qvtoperational::cst::ConstructorCS")
qvtoperational_cst_ComputeExpCS = Class(name="qvtoperational::cst::ComputeExpCS")
VariableCS = Class(name="VariableCS")
qvtoperational_cst_WhileExpCS = Class(name="qvtoperational::cst::WhileExpCS")
MappingBodyCS = Class(name="MappingBodyCS")
MappingEndCS = Class(name="MappingEndCS")
qvtoperational_cst_StatementCS = Class(name="qvtoperational::cst::StatementCS", is_abstract=True)
qvtoperational_cst_BlockExpCS = Class(name="qvtoperational::cst::BlockExpCS")
StatementCS = Class(name="StatementCS")
qvtoperational_cst_ForExpCS = Class(name="qvtoperational::cst::ForExpCS")
ImperativeLoopExpCS = Class(name="ImperativeLoopExpCS")
qvtoperational_cst_ImperativeIterateExpCS = Class(name="qvtoperational::cst::ImperativeIterateExpCS")
qvtoperational_cst_SwitchExpCS = Class(name="qvtoperational::cst::SwitchExpCS")
SwitchAltExpCS = Class(name="SwitchAltExpCS")
qvtoperational_cst_SwitchAltExpCS = Class(name="qvtoperational::cst::SwitchAltExpCS")
qvtoperational_cst_ImperativeLoopExpCS = Class(name="qvtoperational::cst::ImperativeLoopExpCS")
cst_LoopExpCS = Class(name="cst::LoopExpCS")
cst_StatementCS = Class(name="cst::StatementCS")
qvtoperational_cst_AssignStatementCS = Class(name="qvtoperational::cst::AssignStatementCS")
qvtoperational_cst_BreakExpCS = Class(name="qvtoperational::cst::BreakExpCS")
qvtoperational_cst_ContinueExpCS = Class(name="qvtoperational::cst::ContinueExpCS")
qvtoperational_cst_VariableInitializationCS = Class(name="qvtoperational::cst::VariableInitializationCS")
qvtoperational_cst_ObjectExpCS = Class(name="qvtoperational::cst::ObjectExpCS")
cst_InstantiationExpCS = Class(name="cst::InstantiationExpCS")
qvtoperational_cst_MappingCallExpCS = Class(name="qvtoperational::cst::MappingCallExpCS")
ImperativeOperationCallExpCS = Class(name="ImperativeOperationCallExpCS")
qvtoperational_cst_ImperativeOperationCallExpCS = Class(name="qvtoperational::cst::ImperativeOperationCallExpCS")
OperationCallExpCS = Class(name="OperationCallExpCS")
qvtoperational_cst_DirectionKindCS = Class(name="qvtoperational::cst::DirectionKindCS")
qvtoperational_cst_ExpressionStatementCS = Class(name="qvtoperational::cst::ExpressionStatementCS")
qvtoperational_cst_MappingBodyCS = Class(name="qvtoperational::cst::MappingBodyCS")
qvtoperational_cst_ResolveInExpCS = Class(name="qvtoperational::cst::ResolveInExpCS")
ResolveExpCS = Class(name="ResolveExpCS")
qvtoperational_cst_ModelTypeCS = Class(name="qvtoperational::cst::ModelTypeCS")
qvtoperational_cst_ElementWithBody = Class(name="qvtoperational::cst::ElementWithBody", is_abstract=True)
qvtoperational_cst_ResolveExpCS = Class(name="qvtoperational::cst::ResolveExpCS")
CallExpCS = Class(name="CallExpCS")
qvtoperational_cst_PackageRefCS = Class(name="qvtoperational::cst::PackageRefCS")
qvtoperational_cst_TransformationHeaderCS = Class(name="qvtoperational::cst::TransformationHeaderCS")
PackageRefCS = Class(name="PackageRefCS")
qvtoperational_cst_ModuleUsageCS = Class(name="qvtoperational::cst::ModuleUsageCS")
ModuleKindCS = Class(name="ModuleKindCS")
ModuleRefCS = Class(name="ModuleRefCS")
qvtoperational_cst_TransformationRefineCS = Class(name="qvtoperational::cst::TransformationRefineCS")
qvtoperational_cst_TypeSpecCS = Class(name="qvtoperational::cst::TypeSpecCS")
qvtoperational_cst_LogExpCS = Class(name="qvtoperational::cst::LogExpCS")
ModuleUsageCS = Class(name="ModuleUsageCS")
TransformationRefineCS = Class(name="TransformationRefineCS")
qvtoperational_cst_ModuleKindCS = Class(name="qvtoperational::cst::ModuleKindCS")
qvtoperational_cst_ModuleRefCS = Class(name="qvtoperational::cst::ModuleRefCS")
qvtoperational_cst_ReturnExpCS = Class(name="qvtoperational::cst::ReturnExpCS")
qvtoperational_cst_MappingExtensionCS = Class(name="qvtoperational::cst::MappingExtensionCS")
qvtoperational_cst_InstantiationExpCS = Class(name="qvtoperational::cst::InstantiationExpCS")
qvtoperational_cst_ListTypeCS = Class(name="qvtoperational::cst::ListTypeCS")
qvtoperational_cst_AssertExpCS = Class(name="qvtoperational::cst::AssertExpCS")
LogExpCS = Class(name="LogExpCS")
DictLiteralPartCS = Class(name="DictLiteralPartCS")
qvtoperational_cst_DictLiteralPartCS = Class(name="qvtoperational::cst::DictLiteralPartCS")
qvtoperational_cst_TagCS = Class(name="qvtoperational::cst::TagCS")
qvtoperational_cst_UnitCS = Class(name="qvtoperational::cst::UnitCS")
qvtoperational_cst_ListLiteralExpCS = Class(name="qvtoperational::cst::ListLiteralExpCS")
LiteralExpCS = Class(name="LiteralExpCS")
CollectionLiteralPartCS = Class(name="CollectionLiteralPartCS")
qvtoperational_cst_DictionaryTypeCS = Class(name="qvtoperational::cst::DictionaryTypeCS")
qvtoperational_cst_DictLiteralExpCS = Class(name="qvtoperational::cst::DictLiteralExpCS")
qvtoperational_cst_ScopedNameCS = Class(name="qvtoperational::cst::ScopedNameCS")
qvtoperational_cst_ResolveOpArgsExpCS = Class(name="qvtoperational::cst::ResolveOpArgsExpCS")

# qvtoperational_cst_MappingModuleCS class attributes and methods

# CSTNode class attributes and methods

# TransformationHeaderCS class attributes and methods

# ImportCS class attributes and methods

# ModelTypeCS class attributes and methods

# RenameCS class attributes and methods

# ModulePropertyCS class attributes and methods

# MappingMethodCS class attributes and methods

# ClassifierDefCS class attributes and methods

# SimpleNameCS class attributes and methods

# StringLiteralExpCS class attributes and methods

# qvtoperational_cst_ModulePropertyCS class attributes and methods

# qvtoperational_cst_ConfigPropertyCS class attributes and methods

# qvtoperational_cst_LocalPropertyCS class attributes and methods

# OCLExpressionCS class attributes and methods

# qvtoperational_cst_ContextualPropertyCS class attributes and methods

# ScopedNameCS class attributes and methods

# qvtoperational_cst_ClassifierDefCS class attributes and methods

# TagCS class attributes and methods

# qvtoperational_cst_LibraryCS class attributes and methods

# MappingModuleCS class attributes and methods

# qvtoperational_cst_ImportCS class attributes and methods

# PathNameCS class attributes and methods

# qvtoperational_cst_LibraryImportCS class attributes and methods

# qvtoperational_cst_RenameCS class attributes and methods

# TypeCS class attributes and methods

# MultiplicityDefCS class attributes and methods

# OppositePropertyCS class attributes and methods

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

# TypeSpecCS class attributes and methods

# qvtoperational_cst_SimpleSignatureCS class attributes and methods

# qvtoperational_cst_CompleteSignatureCS class attributes and methods

# SimpleSignatureCS class attributes and methods

# qvtoperational_cst_MappingMethodCS class attributes and methods
qvtoperational_cst_MappingMethodCS_blackBox: Property = Property(name="blackBox", type=BooleanType)
qvtoperational_cst_MappingMethodCS.attributes={qvtoperational_cst_MappingMethodCS_blackBox}

# MappingDeclarationCS class attributes and methods

# qvtoperational_cst_MappingRuleCS class attributes and methods

# ParameterDeclarationCS class attributes and methods

# DirectionKindCS class attributes and methods

# MappingExtensionCS class attributes and methods

# qvtoperational_cst_ParameterDeclarationCS class attributes and methods
qvtoperational_cst_ParameterDeclarationCS_directionKind: Property = Property(name="directionKind", type=StringType)
qvtoperational_cst_ParameterDeclarationCS.attributes={qvtoperational_cst_ParameterDeclarationCS_directionKind}

# qvtoperational_cst_MappingSectionCS class attributes and methods

# cst_CSTNode class attributes and methods

# cst_ElementWithBody class attributes and methods

# MappingRuleCS class attributes and methods

# qvtoperational_cst_MappingInitCS class attributes and methods

# MappingSectionCS class attributes and methods

# qvtoperational_cst_MappingEndCS class attributes and methods

# qvtoperational_cst_MappingSectionsCS class attributes and methods

# MappingInitCS class attributes and methods

# MappingSectionsCS class attributes and methods

# qvtoperational_cst_MappingQueryCS class attributes and methods
qvtoperational_cst_MappingQueryCS_isSimpleDefinition: Property = Property(name="isSimpleDefinition", type=BooleanType)
qvtoperational_cst_MappingQueryCS.attributes={qvtoperational_cst_MappingQueryCS_isSimpleDefinition}

# qvtoperational_cst_ConstructorCS class attributes and methods

# qvtoperational_cst_ComputeExpCS class attributes and methods

# VariableCS class attributes and methods

# qvtoperational_cst_WhileExpCS class attributes and methods

# MappingBodyCS class attributes and methods

# MappingEndCS class attributes and methods

# qvtoperational_cst_StatementCS class attributes and methods

# qvtoperational_cst_BlockExpCS class attributes and methods

# StatementCS class attributes and methods

# qvtoperational_cst_ForExpCS class attributes and methods

# ImperativeLoopExpCS class attributes and methods

# qvtoperational_cst_ImperativeIterateExpCS class attributes and methods

# qvtoperational_cst_SwitchExpCS class attributes and methods

# SwitchAltExpCS class attributes and methods

# qvtoperational_cst_SwitchAltExpCS class attributes and methods

# qvtoperational_cst_ImperativeLoopExpCS class attributes and methods

# cst_LoopExpCS class attributes and methods

# cst_StatementCS class attributes and methods

# qvtoperational_cst_AssignStatementCS class attributes and methods
qvtoperational_cst_AssignStatementCS_incremental: Property = Property(name="incremental", type=BooleanType)
qvtoperational_cst_AssignStatementCS.attributes={qvtoperational_cst_AssignStatementCS_incremental}

# qvtoperational_cst_BreakExpCS class attributes and methods

# qvtoperational_cst_ContinueExpCS class attributes and methods

# qvtoperational_cst_VariableInitializationCS class attributes and methods
qvtoperational_cst_VariableInitializationCS_withResult: Property = Property(name="withResult", type=BooleanType)
qvtoperational_cst_VariableInitializationCS.attributes={qvtoperational_cst_VariableInitializationCS_withResult}

# qvtoperational_cst_ObjectExpCS class attributes and methods
qvtoperational_cst_ObjectExpCS_isImplicit: Property = Property(name="isImplicit", type=BooleanType)
qvtoperational_cst_ObjectExpCS.attributes={qvtoperational_cst_ObjectExpCS_isImplicit}

# cst_InstantiationExpCS class attributes and methods

# qvtoperational_cst_MappingCallExpCS class attributes and methods
qvtoperational_cst_MappingCallExpCS_strict: Property = Property(name="strict", type=BooleanType)
qvtoperational_cst_MappingCallExpCS.attributes={qvtoperational_cst_MappingCallExpCS_strict}

# ImperativeOperationCallExpCS class attributes and methods

# qvtoperational_cst_ImperativeOperationCallExpCS class attributes and methods

# OperationCallExpCS class attributes and methods

# qvtoperational_cst_DirectionKindCS class attributes and methods
qvtoperational_cst_DirectionKindCS_directionKind: Property = Property(name="directionKind", type=StringType)
qvtoperational_cst_DirectionKindCS.attributes={qvtoperational_cst_DirectionKindCS_directionKind}

# qvtoperational_cst_ExpressionStatementCS class attributes and methods

# qvtoperational_cst_MappingBodyCS class attributes and methods
qvtoperational_cst_MappingBodyCS_hasPopulationKeyword: Property = Property(name="hasPopulationKeyword", type=BooleanType)
qvtoperational_cst_MappingBodyCS.attributes={qvtoperational_cst_MappingBodyCS_hasPopulationKeyword}

# qvtoperational_cst_ResolveInExpCS class attributes and methods

# ResolveExpCS class attributes and methods

# qvtoperational_cst_ModelTypeCS class attributes and methods

# qvtoperational_cst_ElementWithBody class attributes and methods
qvtoperational_cst_ElementWithBody_bodyStartLocation: Property = Property(name="bodyStartLocation", type=IntegerType)
qvtoperational_cst_ElementWithBody_bodyEndLocation: Property = Property(name="bodyEndLocation", type=IntegerType)
qvtoperational_cst_ElementWithBody.attributes={qvtoperational_cst_ElementWithBody_bodyStartLocation, qvtoperational_cst_ElementWithBody_bodyEndLocation}

# qvtoperational_cst_ResolveExpCS class attributes and methods
qvtoperational_cst_ResolveExpCS_isInverse: Property = Property(name="isInverse", type=BooleanType)
qvtoperational_cst_ResolveExpCS_isDeferred: Property = Property(name="isDeferred", type=BooleanType)
qvtoperational_cst_ResolveExpCS_one: Property = Property(name="one", type=BooleanType)
qvtoperational_cst_ResolveExpCS.attributes={qvtoperational_cst_ResolveExpCS_isInverse, qvtoperational_cst_ResolveExpCS_isDeferred, qvtoperational_cst_ResolveExpCS_one}

# CallExpCS class attributes and methods

# qvtoperational_cst_PackageRefCS class attributes and methods

# qvtoperational_cst_TransformationHeaderCS class attributes and methods

# PackageRefCS class attributes and methods

# qvtoperational_cst_ModuleUsageCS class attributes and methods
qvtoperational_cst_ModuleUsageCS_importKind: Property = Property(name="importKind", type=StringType)
qvtoperational_cst_ModuleUsageCS.attributes={qvtoperational_cst_ModuleUsageCS_importKind}

# ModuleKindCS class attributes and methods

# ModuleRefCS class attributes and methods

# qvtoperational_cst_TransformationRefineCS class attributes and methods

# qvtoperational_cst_TypeSpecCS class attributes and methods

# qvtoperational_cst_LogExpCS class attributes and methods

# ModuleUsageCS class attributes and methods

# TransformationRefineCS class attributes and methods

# qvtoperational_cst_ModuleKindCS class attributes and methods
qvtoperational_cst_ModuleKindCS_moduleKind: Property = Property(name="moduleKind", type=StringType)
qvtoperational_cst_ModuleKindCS.attributes={qvtoperational_cst_ModuleKindCS_moduleKind}

# qvtoperational_cst_ModuleRefCS class attributes and methods

# qvtoperational_cst_ReturnExpCS class attributes and methods

# qvtoperational_cst_MappingExtensionCS class attributes and methods
qvtoperational_cst_MappingExtensionCS_kind: Property = Property(name="kind", type=StringType)
qvtoperational_cst_MappingExtensionCS.attributes={qvtoperational_cst_MappingExtensionCS_kind}

# qvtoperational_cst_InstantiationExpCS class attributes and methods

# qvtoperational_cst_ListTypeCS class attributes and methods

# qvtoperational_cst_AssertExpCS class attributes and methods

# LogExpCS class attributes and methods

# DictLiteralPartCS class attributes and methods

# qvtoperational_cst_DictLiteralPartCS class attributes and methods

# qvtoperational_cst_TagCS class attributes and methods

# qvtoperational_cst_UnitCS class attributes and methods

# qvtoperational_cst_ListLiteralExpCS class attributes and methods

# LiteralExpCS class attributes and methods

# CollectionLiteralPartCS class attributes and methods

# qvtoperational_cst_DictionaryTypeCS class attributes and methods

# qvtoperational_cst_DictLiteralExpCS class attributes and methods

# qvtoperational_cst_ScopedNameCS class attributes and methods
qvtoperational_cst_ScopedNameCS_name: Property = Property(name="name", type=StringType)
qvtoperational_cst_ScopedNameCS.attributes={qvtoperational_cst_ScopedNameCS_name}

# qvtoperational_cst_ResolveOpArgsExpCS class attributes and methods

# Relationships
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
typeCS16: BinaryAssociation = BinaryAssociation(
    name="typeCS16",
    ends={
        Property(name="TypeCS", type=qvtoperational_cst_RenameCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_RenameCS", type=TypeCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
stereotypeQualifiers46: BinaryAssociation = BinaryAssociation(
    name="stereotypeQualifiers46",
    ends={
        Property(name="qvtoperational_cst_ClassifierPropertyCS", type=SimpleNameCS, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="SimpleNameCS47", type=qvtoperational_cst_ClassifierPropertyCS, multiplicity=Multiplicity(1, 1))
    }
)
featureKeys48: BinaryAssociation = BinaryAssociation(
    name="featureKeys48",
    ends={
        Property(name="SimpleNameCS50", type=qvtoperational_cst_ClassifierPropertyCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_ClassifierPropertyCS49", type=SimpleNameCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
mappingDeclarationCS88: BinaryAssociation = BinaryAssociation(
    name="mappingDeclarationCS88",
    ends={
        Property(name="MappingDeclarationCS", type=qvtoperational_cst_MappingMethodCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_MappingMethodCS", type=MappingDeclarationCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
guard89: BinaryAssociation = BinaryAssociation(
    name="guard89",
    ends={
        Property(name="OCLExpressionCS90", type=qvtoperational_cst_MappingRuleCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_MappingRuleCS", type=OCLExpressionCS, multiplicity=Multiplicity(0, 1), is_composite=True)
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
expressions95: BinaryAssociation = BinaryAssociation(
    name="expressions95",
    ends={
        Property(name="OCLExpressionCS96", type=qvtoperational_cst_ConstructorCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_ConstructorCS", type=OCLExpressionCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statements97: BinaryAssociation = BinaryAssociation(
    name="statements97",
    ends={
        Property(name="OCLExpressionCS98", type=qvtoperational_cst_MappingSectionCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_MappingSectionCS", type=OCLExpressionCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mappingRuleCS99: BinaryAssociation = BinaryAssociation(
    name="mappingRuleCS99",
    ends={
        Property(name="MappingRuleCS", type=qvtoperational_cst_MappingSectionCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_MappingSectionCS100", type=MappingRuleCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
mappingInitCS101: BinaryAssociation = BinaryAssociation(
    name="mappingInitCS101",
    ends={
        Property(name="MappingInitCS", type=qvtoperational_cst_MappingSectionsCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_MappingSectionsCS", type=MappingInitCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
mappingBody91: BinaryAssociation = BinaryAssociation(
    name="mappingBody91",
    ends={
        Property(name="MappingSectionsCS", type=qvtoperational_cst_MappingRuleCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_MappingRuleCS92", type=MappingSectionsCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expressions93: BinaryAssociation = BinaryAssociation(
    name="expressions93",
    ends={
        Property(name="OCLExpressionCS94", type=qvtoperational_cst_MappingQueryCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_MappingQueryCS", type=OCLExpressionCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bodyExpressions106: BinaryAssociation = BinaryAssociation(
    name="bodyExpressions106",
    ends={
        Property(name="OCLExpressionCS107", type=qvtoperational_cst_BlockExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_BlockExpCS", type=OCLExpressionCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returnedElement108: BinaryAssociation = BinaryAssociation(
    name="returnedElement108",
    ends={
        Property(name="VariableCS", type=qvtoperational_cst_ComputeExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_ComputeExpCS", type=VariableCS, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body109: BinaryAssociation = BinaryAssociation(
    name="body109",
    ends={
        Property(name="OCLExpressionCS111", type=qvtoperational_cst_ComputeExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_ComputeExpCS110", type=OCLExpressionCS, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body112: BinaryAssociation = BinaryAssociation(
    name="body112",
    ends={
        Property(name="OCLExpressionCS113", type=qvtoperational_cst_WhileExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_WhileExpCS", type=OCLExpressionCS, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition114: BinaryAssociation = BinaryAssociation(
    name="condition114",
    ends={
        Property(name="OCLExpressionCS116", type=qvtoperational_cst_WhileExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_WhileExpCS115", type=OCLExpressionCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
mappingBodyCS102: BinaryAssociation = BinaryAssociation(
    name="mappingBodyCS102",
    ends={
        Property(name="MappingBodyCS", type=qvtoperational_cst_MappingSectionsCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_MappingSectionsCS103", type=MappingBodyCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
mappingEndCS104: BinaryAssociation = BinaryAssociation(
    name="mappingEndCS104",
    ends={
        Property(name="MappingEndCS", type=qvtoperational_cst_MappingSectionsCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_MappingSectionsCS105", type=MappingEndCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target122: BinaryAssociation = BinaryAssociation(
    name="target122",
    ends={
        Property(name="VariableCS123", type=qvtoperational_cst_ImperativeIterateExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_ImperativeIterateExpCS", type=VariableCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
alternativePart124: BinaryAssociation = BinaryAssociation(
    name="alternativePart124",
    ends={
        Property(name="SwitchAltExpCS", type=qvtoperational_cst_SwitchExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_SwitchExpCS", type=SwitchAltExpCS, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
elsePart125: BinaryAssociation = BinaryAssociation(
    name="elsePart125",
    ends={
        Property(name="OCLExpressionCS127", type=qvtoperational_cst_SwitchExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_SwitchExpCS126", type=OCLExpressionCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition128: BinaryAssociation = BinaryAssociation(
    name="condition128",
    ends={
        Property(name="OCLExpressionCS129", type=qvtoperational_cst_SwitchAltExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_SwitchAltExpCS", type=OCLExpressionCS, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body130: BinaryAssociation = BinaryAssociation(
    name="body130",
    ends={
        Property(name="OCLExpressionCS132", type=qvtoperational_cst_SwitchAltExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_SwitchAltExpCS131", type=OCLExpressionCS, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
resultVar117: BinaryAssociation = BinaryAssociation(
    name="resultVar117",
    ends={
        Property(name="VariableCS119", type=qvtoperational_cst_WhileExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_WhileExpCS118", type=VariableCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition120: BinaryAssociation = BinaryAssociation(
    name="condition120",
    ends={
        Property(name="OCLExpressionCS121", type=qvtoperational_cst_ImperativeLoopExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_ImperativeLoopExpCS", type=OCLExpressionCS, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
simpleNameCS135: BinaryAssociation = BinaryAssociation(
    name="simpleNameCS135",
    ends={
        Property(name="SimpleNameCS137", type=qvtoperational_cst_VariableInitializationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_VariableInitializationCS136", type=SimpleNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeCS138: BinaryAssociation = BinaryAssociation(
    name="typeCS138",
    ends={
        Property(name="TypeCS140", type=qvtoperational_cst_VariableInitializationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_VariableInitializationCS139", type=TypeCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lValueCS141: BinaryAssociation = BinaryAssociation(
    name="lValueCS141",
    ends={
        Property(name="OCLExpressionCS142", type=qvtoperational_cst_AssignStatementCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_AssignStatementCS", type=OCLExpressionCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
oclExpressionCS143: BinaryAssociation = BinaryAssociation(
    name="oclExpressionCS143",
    ends={
        Property(name="OCLExpressionCS145", type=qvtoperational_cst_AssignStatementCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_AssignStatementCS144", type=OCLExpressionCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
oclExpressionCS133: BinaryAssociation = BinaryAssociation(
    name="oclExpressionCS133",
    ends={
        Property(name="OCLExpressionCS134", type=qvtoperational_cst_VariableInitializationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_VariableInitializationCS", type=OCLExpressionCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
simpleNameCS148: BinaryAssociation = BinaryAssociation(
    name="simpleNameCS148",
    ends={
        Property(name="SimpleNameCS149", type=qvtoperational_cst_ObjectExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_ObjectExpCS", type=SimpleNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expressions150: BinaryAssociation = BinaryAssociation(
    name="expressions150",
    ends={
        Property(name="OCLExpressionCS152", type=qvtoperational_cst_ObjectExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_ObjectExpCS151", type=OCLExpressionCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
module153: BinaryAssociation = BinaryAssociation(
    name="module153",
    ends={
        Property(name="SimpleNameCS154", type=qvtoperational_cst_ImperativeOperationCallExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_ImperativeOperationCallExpCS", type=SimpleNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
oclExpressionCS146: BinaryAssociation = BinaryAssociation(
    name="oclExpressionCS146",
    ends={
        Property(name="OCLExpressionCS147", type=qvtoperational_cst_ExpressionStatementCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_ExpressionStatementCS", type=OCLExpressionCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target155: BinaryAssociation = BinaryAssociation(
    name="target155",
    ends={
        Property(name="VariableCS156", type=qvtoperational_cst_ResolveExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_ResolveExpCS", type=VariableCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition157: BinaryAssociation = BinaryAssociation(
    name="condition157",
    ends={
        Property(name="OCLExpressionCS159", type=qvtoperational_cst_ResolveExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_ResolveExpCS158", type=OCLExpressionCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
inMappingType160: BinaryAssociation = BinaryAssociation(
    name="inMappingType160",
    ends={
        Property(name="TypeCS161", type=qvtoperational_cst_ResolveInExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_ResolveInExpCS", type=TypeCS, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
inMappingName162: BinaryAssociation = BinaryAssociation(
    name="inMappingName162",
    ends={
        Property(name="SimpleNameCS164", type=qvtoperational_cst_ResolveInExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_ResolveInExpCS163", type=SimpleNameCS, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
whereStatements172: BinaryAssociation = BinaryAssociation(
    name="whereStatements172",
    ends={
        Property(name="OCLExpressionCS174", type=qvtoperational_cst_ModelTypeCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_ModelTypeCS173", type=OCLExpressionCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pathNameCS175: BinaryAssociation = BinaryAssociation(
    name="pathNameCS175",
    ends={
        Property(name="PathNameCS176", type=qvtoperational_cst_PackageRefCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_PackageRefCS", type=PathNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
uriCS177: BinaryAssociation = BinaryAssociation(
    name="uriCS177",
    ends={
        Property(name="StringLiteralExpCS179", type=qvtoperational_cst_PackageRefCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_PackageRefCS178", type=StringLiteralExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
qualifiers180: BinaryAssociation = BinaryAssociation(
    name="qualifiers180",
    ends={
        Property(name="StringLiteralExpCS181", type=qvtoperational_cst_TransformationHeaderCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_TransformationHeaderCS", type=StringLiteralExpCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pathNameCS182: BinaryAssociation = BinaryAssociation(
    name="pathNameCS182",
    ends={
        Property(name="PathNameCS184", type=qvtoperational_cst_TransformationHeaderCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_TransformationHeaderCS183", type=PathNameCS, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameters185: BinaryAssociation = BinaryAssociation(
    name="parameters185",
    ends={
        Property(name="ParameterDeclarationCS187", type=qvtoperational_cst_TransformationHeaderCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_TransformationHeaderCS186", type=ParameterDeclarationCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
identifierCS165: BinaryAssociation = BinaryAssociation(
    name="identifierCS165",
    ends={
        Property(name="SimpleNameCS166", type=qvtoperational_cst_ModelTypeCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_ModelTypeCS", type=SimpleNameCS, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
complianceKindCS167: BinaryAssociation = BinaryAssociation(
    name="complianceKindCS167",
    ends={
        Property(name="StringLiteralExpCS169", type=qvtoperational_cst_ModelTypeCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_ModelTypeCS168", type=StringLiteralExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
packageRefs170: BinaryAssociation = BinaryAssociation(
    name="packageRefs170",
    ends={
        Property(name="PackageRefCS", type=qvtoperational_cst_ModelTypeCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_ModelTypeCS171", type=PackageRefCS, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
pathNameCS192: BinaryAssociation = BinaryAssociation(
    name="pathNameCS192",
    ends={
        Property(name="PathNameCS193", type=qvtoperational_cst_ModuleRefCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_ModuleRefCS", type=PathNameCS, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameters194: BinaryAssociation = BinaryAssociation(
    name="parameters194",
    ends={
        Property(name="ParameterDeclarationCS196", type=qvtoperational_cst_ModuleRefCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_ModuleRefCS195", type=ParameterDeclarationCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
moduleKindCS197: BinaryAssociation = BinaryAssociation(
    name="moduleKindCS197",
    ends={
        Property(name="ModuleKindCS", type=qvtoperational_cst_ModuleUsageCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_ModuleUsageCS", type=ModuleKindCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
moduleRefs198: BinaryAssociation = BinaryAssociation(
    name="moduleRefs198",
    ends={
        Property(name="ModuleRefCS", type=qvtoperational_cst_ModuleUsageCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_ModuleUsageCS199", type=ModuleRefCS, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
moduleRefCS200: BinaryAssociation = BinaryAssociation(
    name="moduleRefCS200",
    ends={
        Property(name="ModuleRefCS201", type=qvtoperational_cst_TransformationRefineCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_TransformationRefineCS", type=ModuleRefCS, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
simpleNameCS202: BinaryAssociation = BinaryAssociation(
    name="simpleNameCS202",
    ends={
        Property(name="SimpleNameCS204", type=qvtoperational_cst_TransformationRefineCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_TransformationRefineCS203", type=SimpleNameCS, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
typeCS205: BinaryAssociation = BinaryAssociation(
    name="typeCS205",
    ends={
        Property(name="TypeCS206", type=qvtoperational_cst_TypeSpecCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_TypeSpecCS", type=TypeCS, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
simpleNameCS207: BinaryAssociation = BinaryAssociation(
    name="simpleNameCS207",
    ends={
        Property(name="SimpleNameCS209", type=qvtoperational_cst_TypeSpecCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_TypeSpecCS208", type=SimpleNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
moduleUsages188: BinaryAssociation = BinaryAssociation(
    name="moduleUsages188",
    ends={
        Property(name="ModuleUsageCS", type=qvtoperational_cst_TransformationHeaderCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_TransformationHeaderCS189", type=ModuleUsageCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transformationRefineCS190: BinaryAssociation = BinaryAssociation(
    name="transformationRefineCS190",
    ends={
        Property(name="TransformationRefineCS", type=qvtoperational_cst_TransformationHeaderCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_TransformationHeaderCS191", type=TransformationRefineCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value219: BinaryAssociation = BinaryAssociation(
    name="value219",
    ends={
        Property(name="OCLExpressionCS220", type=qvtoperational_cst_ReturnExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_ReturnExpCS", type=OCLExpressionCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
mappingIdentifiers221: BinaryAssociation = BinaryAssociation(
    name="mappingIdentifiers221",
    ends={
        Property(name="ScopedNameCS222", type=qvtoperational_cst_MappingExtensionCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_MappingExtensionCS", type=ScopedNameCS, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
typeSpecCS223: BinaryAssociation = BinaryAssociation(
    name="typeSpecCS223",
    ends={
        Property(name="TypeSpecCS224", type=qvtoperational_cst_InstantiationExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_InstantiationExpCS", type=TypeSpecCS, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
arguments225: BinaryAssociation = BinaryAssociation(
    name="arguments225",
    ends={
        Property(name="OCLExpressionCS227", type=qvtoperational_cst_InstantiationExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_InstantiationExpCS226", type=OCLExpressionCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeCS228: BinaryAssociation = BinaryAssociation(
    name="typeCS228",
    ends={
        Property(name="TypeCS229", type=qvtoperational_cst_ListTypeCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_ListTypeCS", type=TypeCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition210: BinaryAssociation = BinaryAssociation(
    name="condition210",
    ends={
        Property(name="OCLExpressionCS211", type=qvtoperational_cst_LogExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_LogExpCS", type=OCLExpressionCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assertion212: BinaryAssociation = BinaryAssociation(
    name="assertion212",
    ends={
        Property(name="OCLExpressionCS213", type=qvtoperational_cst_AssertExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_AssertExpCS", type=OCLExpressionCS, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
log214: BinaryAssociation = BinaryAssociation(
    name="log214",
    ends={
        Property(name="LogExpCS", type=qvtoperational_cst_AssertExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_AssertExpCS215", type=LogExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
severity216: BinaryAssociation = BinaryAssociation(
    name="severity216",
    ends={
        Property(name="SimpleNameCS218", type=qvtoperational_cst_AssertExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_AssertExpCS217", type=SimpleNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parts236: BinaryAssociation = BinaryAssociation(
    name="parts236",
    ends={
        Property(name="DictLiteralPartCS", type=qvtoperational_cst_DictLiteralExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_DictLiteralExpCS", type=DictLiteralPartCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
key237: BinaryAssociation = BinaryAssociation(
    name="key237",
    ends={
        Property(name="LiteralExpCS", type=qvtoperational_cst_DictLiteralPartCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_DictLiteralPartCS", type=LiteralExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value238: BinaryAssociation = BinaryAssociation(
    name="value238",
    ends={
        Property(name="OCLExpressionCS240", type=qvtoperational_cst_DictLiteralPartCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_DictLiteralPartCS239", type=OCLExpressionCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name241: BinaryAssociation = BinaryAssociation(
    name="name241",
    ends={
        Property(name="StringLiteralExpCS242", type=qvtoperational_cst_TagCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_TagCS", type=StringLiteralExpCS, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
scopedNameCS243: BinaryAssociation = BinaryAssociation(
    name="scopedNameCS243",
    ends={
        Property(name="ScopedNameCS245", type=qvtoperational_cst_TagCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_TagCS244", type=ScopedNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
oclExpressionCS246: BinaryAssociation = BinaryAssociation(
    name="oclExpressionCS246",
    ends={
        Property(name="OCLExpressionCS248", type=qvtoperational_cst_TagCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_TagCS247", type=OCLExpressionCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
topLevelElements249: BinaryAssociation = BinaryAssociation(
    name="topLevelElements249",
    ends={
        Property(name="CSTNode", type=qvtoperational_cst_UnitCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_UnitCS", type=CSTNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
modules250: BinaryAssociation = BinaryAssociation(
    name="modules250",
    ends={
        Property(name="MappingModuleCS", type=qvtoperational_cst_UnitCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_UnitCS251", type=MappingModuleCS, multiplicity=Multiplicity(0, 9999))
    }
)
collectionLiteralParts230: BinaryAssociation = BinaryAssociation(
    name="collectionLiteralParts230",
    ends={
        Property(name="CollectionLiteralPartCS", type=qvtoperational_cst_ListLiteralExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_ListLiteralExpCS", type=CollectionLiteralPartCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
key231: BinaryAssociation = BinaryAssociation(
    name="key231",
    ends={
        Property(name="TypeCS232", type=qvtoperational_cst_DictionaryTypeCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_DictionaryTypeCS", type=TypeCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value233: BinaryAssociation = BinaryAssociation(
    name="value233",
    ends={
        Property(name="TypeCS235", type=qvtoperational_cst_DictionaryTypeCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_DictionaryTypeCS234", type=TypeCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeCS263: BinaryAssociation = BinaryAssociation(
    name="typeCS263",
    ends={
        Property(name="TypeCS264", type=qvtoperational_cst_ScopedNameCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_ScopedNameCS", type=TypeCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
modelTypes252: BinaryAssociation = BinaryAssociation(
    name="modelTypes252",
    ends={
        Property(name="ModelTypeCS254", type=qvtoperational_cst_UnitCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_UnitCS253", type=ModelTypeCS, multiplicity=Multiplicity(0, 9999))
    }
)
imports255: BinaryAssociation = BinaryAssociation(
    name="imports255",
    ends={
        Property(name="ImportCS257", type=qvtoperational_cst_UnitCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_UnitCS256", type=ImportCS, multiplicity=Multiplicity(0, 9999))
    }
)
target258: BinaryAssociation = BinaryAssociation(
    name="target258",
    ends={
        Property(name="VariableCS259", type=qvtoperational_cst_ResolveOpArgsExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_ResolveOpArgsExpCS", type=VariableCS, multiplicity=Multiplicity(0, 1))
    }
)
condition260: BinaryAssociation = BinaryAssociation(
    name="condition260",
    ends={
        Property(name="OCLExpressionCS262", type=qvtoperational_cst_ResolveOpArgsExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_cst_ResolveOpArgsExpCS261", type=OCLExpressionCS, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_qvtoperational_cst_MappingModuleCS_CSTNode = Generalization(general=CSTNode, specific=qvtoperational_cst_MappingModuleCS)
gen_qvtoperational_cst_ModulePropertyCS_CSTNode = Generalization(general=CSTNode, specific=qvtoperational_cst_ModulePropertyCS)
gen_qvtoperational_cst_ConfigPropertyCS_ModulePropertyCS = Generalization(general=ModulePropertyCS, specific=qvtoperational_cst_ConfigPropertyCS)
gen_qvtoperational_cst_LocalPropertyCS_ModulePropertyCS = Generalization(general=ModulePropertyCS, specific=qvtoperational_cst_LocalPropertyCS)
gen_qvtoperational_cst_ContextualPropertyCS_ModulePropertyCS = Generalization(general=ModulePropertyCS, specific=qvtoperational_cst_ContextualPropertyCS)
gen_qvtoperational_cst_LibraryCS_MappingModuleCS = Generalization(general=MappingModuleCS, specific=qvtoperational_cst_LibraryCS)
gen_qvtoperational_cst_ImportCS_CSTNode = Generalization(general=CSTNode, specific=qvtoperational_cst_ImportCS)
gen_qvtoperational_cst_LibraryImportCS_ImportCS = Generalization(general=ImportCS, specific=qvtoperational_cst_LibraryImportCS)
gen_qvtoperational_cst_RenameCS_CSTNode = Generalization(general=CSTNode, specific=qvtoperational_cst_RenameCS)
gen_qvtoperational_cst_OppositePropertyCS_CSTNode = Generalization(general=CSTNode, specific=qvtoperational_cst_OppositePropertyCS)
gen_qvtoperational_cst_MultiplicityDefCS_CSTNode = Generalization(general=CSTNode, specific=qvtoperational_cst_MultiplicityDefCS)
gen_qvtoperational_cst_MappingDeclarationCS_CSTNode = Generalization(general=CSTNode, specific=qvtoperational_cst_MappingDeclarationCS)
gen_qvtoperational_cst_ClassifierDefCS_CSTNode = Generalization(general=CSTNode, specific=qvtoperational_cst_ClassifierDefCS)
gen_qvtoperational_cst_ClassifierPropertyCS_LocalPropertyCS = Generalization(general=LocalPropertyCS, specific=qvtoperational_cst_ClassifierPropertyCS)
gen_qvtoperational_cst_SimpleSignatureCS_CSTNode = Generalization(general=CSTNode, specific=qvtoperational_cst_SimpleSignatureCS)
gen_qvtoperational_cst_CompleteSignatureCS_CSTNode = Generalization(general=CSTNode, specific=qvtoperational_cst_CompleteSignatureCS)
gen_qvtoperational_cst_MappingMethodCS_CSTNode = Generalization(general=CSTNode, specific=qvtoperational_cst_MappingMethodCS)
gen_qvtoperational_cst_MappingRuleCS_MappingMethodCS = Generalization(general=MappingMethodCS, specific=qvtoperational_cst_MappingRuleCS)
gen_qvtoperational_cst_ParameterDeclarationCS_CSTNode = Generalization(general=CSTNode, specific=qvtoperational_cst_ParameterDeclarationCS)
gen_qvtoperational_cst_MappingSectionCS_cst_CSTNode = Generalization(general=cst_CSTNode, specific=qvtoperational_cst_MappingSectionCS)
gen_qvtoperational_cst_MappingSectionCS_cst_ElementWithBody = Generalization(general=cst_ElementWithBody, specific=qvtoperational_cst_MappingSectionCS)
gen_qvtoperational_cst_MappingInitCS_MappingSectionCS = Generalization(general=MappingSectionCS, specific=qvtoperational_cst_MappingInitCS)
gen_qvtoperational_cst_MappingEndCS_MappingSectionCS = Generalization(general=MappingSectionCS, specific=qvtoperational_cst_MappingEndCS)
gen_qvtoperational_cst_MappingSectionsCS_CSTNode = Generalization(general=CSTNode, specific=qvtoperational_cst_MappingSectionsCS)
gen_qvtoperational_cst_MappingQueryCS_MappingMethodCS = Generalization(general=MappingMethodCS, specific=qvtoperational_cst_MappingQueryCS)
gen_qvtoperational_cst_ConstructorCS_MappingMethodCS = Generalization(general=MappingMethodCS, specific=qvtoperational_cst_ConstructorCS)
gen_qvtoperational_cst_ComputeExpCS_StatementCS = Generalization(general=StatementCS, specific=qvtoperational_cst_ComputeExpCS)
gen_qvtoperational_cst_WhileExpCS_StatementCS = Generalization(general=StatementCS, specific=qvtoperational_cst_WhileExpCS)
gen_qvtoperational_cst_StatementCS_OCLExpressionCS = Generalization(general=OCLExpressionCS, specific=qvtoperational_cst_StatementCS)
gen_qvtoperational_cst_BlockExpCS_StatementCS = Generalization(general=StatementCS, specific=qvtoperational_cst_BlockExpCS)
gen_qvtoperational_cst_ForExpCS_ImperativeLoopExpCS = Generalization(general=ImperativeLoopExpCS, specific=qvtoperational_cst_ForExpCS)
gen_qvtoperational_cst_ImperativeIterateExpCS_ImperativeLoopExpCS = Generalization(general=ImperativeLoopExpCS, specific=qvtoperational_cst_ImperativeIterateExpCS)
gen_qvtoperational_cst_SwitchExpCS_StatementCS = Generalization(general=StatementCS, specific=qvtoperational_cst_SwitchExpCS)
gen_qvtoperational_cst_SwitchAltExpCS_StatementCS = Generalization(general=StatementCS, specific=qvtoperational_cst_SwitchAltExpCS)
gen_qvtoperational_cst_ImperativeLoopExpCS_cst_LoopExpCS = Generalization(general=cst_LoopExpCS, specific=qvtoperational_cst_ImperativeLoopExpCS)
gen_qvtoperational_cst_ImperativeLoopExpCS_cst_StatementCS = Generalization(general=cst_StatementCS, specific=qvtoperational_cst_ImperativeLoopExpCS)
gen_qvtoperational_cst_AssignStatementCS_StatementCS = Generalization(general=StatementCS, specific=qvtoperational_cst_AssignStatementCS)
gen_qvtoperational_cst_BreakExpCS_StatementCS = Generalization(general=StatementCS, specific=qvtoperational_cst_BreakExpCS)
gen_qvtoperational_cst_ContinueExpCS_StatementCS = Generalization(general=StatementCS, specific=qvtoperational_cst_ContinueExpCS)
gen_qvtoperational_cst_VariableInitializationCS_StatementCS = Generalization(general=StatementCS, specific=qvtoperational_cst_VariableInitializationCS)
gen_qvtoperational_cst_ObjectExpCS_cst_InstantiationExpCS = Generalization(general=cst_InstantiationExpCS, specific=qvtoperational_cst_ObjectExpCS)
gen_qvtoperational_cst_ObjectExpCS_cst_ElementWithBody = Generalization(general=cst_ElementWithBody, specific=qvtoperational_cst_ObjectExpCS)
gen_qvtoperational_cst_MappingCallExpCS_ImperativeOperationCallExpCS = Generalization(general=ImperativeOperationCallExpCS, specific=qvtoperational_cst_MappingCallExpCS)
gen_qvtoperational_cst_ImperativeOperationCallExpCS_OperationCallExpCS = Generalization(general=OperationCallExpCS, specific=qvtoperational_cst_ImperativeOperationCallExpCS)
gen_qvtoperational_cst_DirectionKindCS_CSTNode = Generalization(general=CSTNode, specific=qvtoperational_cst_DirectionKindCS)
gen_qvtoperational_cst_ExpressionStatementCS_StatementCS = Generalization(general=StatementCS, specific=qvtoperational_cst_ExpressionStatementCS)
gen_qvtoperational_cst_MappingBodyCS_MappingSectionCS = Generalization(general=MappingSectionCS, specific=qvtoperational_cst_MappingBodyCS)
gen_qvtoperational_cst_ResolveInExpCS_ResolveExpCS = Generalization(general=ResolveExpCS, specific=qvtoperational_cst_ResolveInExpCS)
gen_qvtoperational_cst_ModelTypeCS_cst_CSTNode = Generalization(general=cst_CSTNode, specific=qvtoperational_cst_ModelTypeCS)
gen_qvtoperational_cst_ModelTypeCS_cst_ElementWithBody = Generalization(general=cst_ElementWithBody, specific=qvtoperational_cst_ModelTypeCS)
gen_qvtoperational_cst_ResolveExpCS_CallExpCS = Generalization(general=CallExpCS, specific=qvtoperational_cst_ResolveExpCS)
gen_qvtoperational_cst_PackageRefCS_CSTNode = Generalization(general=CSTNode, specific=qvtoperational_cst_PackageRefCS)
gen_qvtoperational_cst_TransformationHeaderCS_CSTNode = Generalization(general=CSTNode, specific=qvtoperational_cst_TransformationHeaderCS)
gen_qvtoperational_cst_ModuleUsageCS_CSTNode = Generalization(general=CSTNode, specific=qvtoperational_cst_ModuleUsageCS)
gen_qvtoperational_cst_TransformationRefineCS_CSTNode = Generalization(general=CSTNode, specific=qvtoperational_cst_TransformationRefineCS)
gen_qvtoperational_cst_TypeSpecCS_CSTNode = Generalization(general=CSTNode, specific=qvtoperational_cst_TypeSpecCS)
gen_qvtoperational_cst_LogExpCS_OperationCallExpCS = Generalization(general=OperationCallExpCS, specific=qvtoperational_cst_LogExpCS)
gen_qvtoperational_cst_ModuleKindCS_CSTNode = Generalization(general=CSTNode, specific=qvtoperational_cst_ModuleKindCS)
gen_qvtoperational_cst_ModuleRefCS_CSTNode = Generalization(general=CSTNode, specific=qvtoperational_cst_ModuleRefCS)
gen_qvtoperational_cst_ReturnExpCS_StatementCS = Generalization(general=StatementCS, specific=qvtoperational_cst_ReturnExpCS)
gen_qvtoperational_cst_MappingExtensionCS_CSTNode = Generalization(general=CSTNode, specific=qvtoperational_cst_MappingExtensionCS)
gen_qvtoperational_cst_InstantiationExpCS_StatementCS = Generalization(general=StatementCS, specific=qvtoperational_cst_InstantiationExpCS)
gen_qvtoperational_cst_ListTypeCS_TypeCS = Generalization(general=TypeCS, specific=qvtoperational_cst_ListTypeCS)
gen_qvtoperational_cst_AssertExpCS_StatementCS = Generalization(general=StatementCS, specific=qvtoperational_cst_AssertExpCS)
gen_qvtoperational_cst_DictLiteralPartCS_CSTNode = Generalization(general=CSTNode, specific=qvtoperational_cst_DictLiteralPartCS)
gen_qvtoperational_cst_TagCS_CSTNode = Generalization(general=CSTNode, specific=qvtoperational_cst_TagCS)
gen_qvtoperational_cst_UnitCS_CSTNode = Generalization(general=CSTNode, specific=qvtoperational_cst_UnitCS)
gen_qvtoperational_cst_ListLiteralExpCS_LiteralExpCS = Generalization(general=LiteralExpCS, specific=qvtoperational_cst_ListLiteralExpCS)
gen_qvtoperational_cst_DictionaryTypeCS_TypeCS = Generalization(general=TypeCS, specific=qvtoperational_cst_DictionaryTypeCS)
gen_qvtoperational_cst_DictLiteralExpCS_LiteralExpCS = Generalization(general=LiteralExpCS, specific=qvtoperational_cst_DictLiteralExpCS)
gen_qvtoperational_cst_ScopedNameCS_CSTNode = Generalization(general=CSTNode, specific=qvtoperational_cst_ScopedNameCS)
gen_qvtoperational_cst_ResolveOpArgsExpCS_CSTNode = Generalization(general=CSTNode, specific=qvtoperational_cst_ResolveOpArgsExpCS)

# Domain Model
domain_model = DomainModel(
    name="qvtoperational",
    types={qvtoperational_cst_MappingModuleCS, CSTNode, TransformationHeaderCS, ImportCS, ModelTypeCS, RenameCS, ModulePropertyCS, MappingMethodCS, ClassifierDefCS, SimpleNameCS, StringLiteralExpCS, qvtoperational_cst_ModulePropertyCS, qvtoperational_cst_ConfigPropertyCS, qvtoperational_cst_LocalPropertyCS, OCLExpressionCS, qvtoperational_cst_ContextualPropertyCS, ScopedNameCS, qvtoperational_cst_ClassifierDefCS, TagCS, qvtoperational_cst_LibraryCS, MappingModuleCS, qvtoperational_cst_ImportCS, PathNameCS, qvtoperational_cst_LibraryImportCS, qvtoperational_cst_RenameCS, TypeCS, MultiplicityDefCS, OppositePropertyCS, qvtoperational_cst_OppositePropertyCS, qvtoperational_cst_MultiplicityDefCS, PrimitiveLiteralExpCS, qvtoperational_cst_MappingDeclarationCS, ClassifierPropertyCS, qvtoperational_cst_ClassifierPropertyCS, LocalPropertyCS, TypeSpecCS, qvtoperational_cst_SimpleSignatureCS, qvtoperational_cst_CompleteSignatureCS, SimpleSignatureCS, qvtoperational_cst_MappingMethodCS, MappingDeclarationCS, qvtoperational_cst_MappingRuleCS, ParameterDeclarationCS, DirectionKindCS, MappingExtensionCS, qvtoperational_cst_ParameterDeclarationCS, qvtoperational_cst_MappingSectionCS, cst_CSTNode, cst_ElementWithBody, MappingRuleCS, qvtoperational_cst_MappingInitCS, MappingSectionCS, qvtoperational_cst_MappingEndCS, qvtoperational_cst_MappingSectionsCS, MappingInitCS, MappingSectionsCS, qvtoperational_cst_MappingQueryCS, qvtoperational_cst_ConstructorCS, qvtoperational_cst_ComputeExpCS, VariableCS, qvtoperational_cst_WhileExpCS, MappingBodyCS, MappingEndCS, qvtoperational_cst_StatementCS, qvtoperational_cst_BlockExpCS, StatementCS, qvtoperational_cst_ForExpCS, ImperativeLoopExpCS, qvtoperational_cst_ImperativeIterateExpCS, qvtoperational_cst_SwitchExpCS, SwitchAltExpCS, qvtoperational_cst_SwitchAltExpCS, qvtoperational_cst_ImperativeLoopExpCS, cst_LoopExpCS, cst_StatementCS, qvtoperational_cst_AssignStatementCS, qvtoperational_cst_BreakExpCS, qvtoperational_cst_ContinueExpCS, qvtoperational_cst_VariableInitializationCS, qvtoperational_cst_ObjectExpCS, cst_InstantiationExpCS, qvtoperational_cst_MappingCallExpCS, ImperativeOperationCallExpCS, qvtoperational_cst_ImperativeOperationCallExpCS, OperationCallExpCS, qvtoperational_cst_DirectionKindCS, qvtoperational_cst_ExpressionStatementCS, qvtoperational_cst_MappingBodyCS, qvtoperational_cst_ResolveInExpCS, ResolveExpCS, qvtoperational_cst_ModelTypeCS, qvtoperational_cst_ElementWithBody, qvtoperational_cst_ResolveExpCS, CallExpCS, qvtoperational_cst_PackageRefCS, qvtoperational_cst_TransformationHeaderCS, PackageRefCS, qvtoperational_cst_ModuleUsageCS, ModuleKindCS, ModuleRefCS, qvtoperational_cst_TransformationRefineCS, qvtoperational_cst_TypeSpecCS, qvtoperational_cst_LogExpCS, ModuleUsageCS, TransformationRefineCS, qvtoperational_cst_ModuleKindCS, qvtoperational_cst_ModuleRefCS, qvtoperational_cst_ReturnExpCS, qvtoperational_cst_MappingExtensionCS, qvtoperational_cst_InstantiationExpCS, qvtoperational_cst_ListTypeCS, qvtoperational_cst_AssertExpCS, LogExpCS, DictLiteralPartCS, qvtoperational_cst_DictLiteralPartCS, qvtoperational_cst_TagCS, qvtoperational_cst_UnitCS, qvtoperational_cst_ListLiteralExpCS, LiteralExpCS, CollectionLiteralPartCS, qvtoperational_cst_DictionaryTypeCS, qvtoperational_cst_DictLiteralExpCS, qvtoperational_cst_ScopedNameCS, qvtoperational_cst_ResolveOpArgsExpCS, DirectionKindEnum, ImportKindEnum, ModuleKindEnum, MappingExtensionKindCS, QualifierKindCS},
    associations={headerCS0, imports1, metamodels3, renamings5, properties7, methods9, classifierDefCS11, simpleNameCS17, originalName19, simpleNameCS21, typeCS23, typeCS25, oclExpressionCS27, scopedNameCS29, typeCS30, oclExpressionCS33, tags13, pathNameCS15, typeCS16, stereotypeQualifiers46, featureKeys48, multiplicity51, opposite53, simpleNameCS55, multiplicity57, lowerBound60, upperBound61, simpleNameCS64, simpleNameCS36, extends38, properties41, tags43, simpleNameCS78, typeSpecCS80, params82, simpleSignature84, resultParams85, mappingDeclarationCS88, guard89, contextType66, parameters69, result71, directionKindCS74, mappingExtension76, expressions95, statements97, mappingRuleCS99, mappingInitCS101, mappingBody91, expressions93, bodyExpressions106, returnedElement108, body109, body112, condition114, mappingBodyCS102, mappingEndCS104, target122, alternativePart124, elsePart125, condition128, body130, resultVar117, condition120, simpleNameCS135, typeCS138, lValueCS141, oclExpressionCS143, oclExpressionCS133, simpleNameCS148, expressions150, module153, oclExpressionCS146, target155, condition157, inMappingType160, inMappingName162, whereStatements172, pathNameCS175, uriCS177, qualifiers180, pathNameCS182, parameters185, identifierCS165, complianceKindCS167, packageRefs170, pathNameCS192, parameters194, moduleKindCS197, moduleRefs198, moduleRefCS200, simpleNameCS202, typeCS205, simpleNameCS207, moduleUsages188, transformationRefineCS190, value219, mappingIdentifiers221, typeSpecCS223, arguments225, typeCS228, condition210, assertion212, log214, severity216, parts236, key237, value238, name241, scopedNameCS243, oclExpressionCS246, topLevelElements249, modules250, collectionLiteralParts230, key231, value233, typeCS263, modelTypes252, imports255, target258, condition260},
    generalizations={gen_qvtoperational_cst_MappingModuleCS_CSTNode, gen_qvtoperational_cst_ModulePropertyCS_CSTNode, gen_qvtoperational_cst_ConfigPropertyCS_ModulePropertyCS, gen_qvtoperational_cst_LocalPropertyCS_ModulePropertyCS, gen_qvtoperational_cst_ContextualPropertyCS_ModulePropertyCS, gen_qvtoperational_cst_LibraryCS_MappingModuleCS, gen_qvtoperational_cst_ImportCS_CSTNode, gen_qvtoperational_cst_LibraryImportCS_ImportCS, gen_qvtoperational_cst_RenameCS_CSTNode, gen_qvtoperational_cst_OppositePropertyCS_CSTNode, gen_qvtoperational_cst_MultiplicityDefCS_CSTNode, gen_qvtoperational_cst_MappingDeclarationCS_CSTNode, gen_qvtoperational_cst_ClassifierDefCS_CSTNode, gen_qvtoperational_cst_ClassifierPropertyCS_LocalPropertyCS, gen_qvtoperational_cst_SimpleSignatureCS_CSTNode, gen_qvtoperational_cst_CompleteSignatureCS_CSTNode, gen_qvtoperational_cst_MappingMethodCS_CSTNode, gen_qvtoperational_cst_MappingRuleCS_MappingMethodCS, gen_qvtoperational_cst_ParameterDeclarationCS_CSTNode, gen_qvtoperational_cst_MappingSectionCS_cst_CSTNode, gen_qvtoperational_cst_MappingSectionCS_cst_ElementWithBody, gen_qvtoperational_cst_MappingInitCS_MappingSectionCS, gen_qvtoperational_cst_MappingEndCS_MappingSectionCS, gen_qvtoperational_cst_MappingSectionsCS_CSTNode, gen_qvtoperational_cst_MappingQueryCS_MappingMethodCS, gen_qvtoperational_cst_ConstructorCS_MappingMethodCS, gen_qvtoperational_cst_ComputeExpCS_StatementCS, gen_qvtoperational_cst_WhileExpCS_StatementCS, gen_qvtoperational_cst_StatementCS_OCLExpressionCS, gen_qvtoperational_cst_BlockExpCS_StatementCS, gen_qvtoperational_cst_ForExpCS_ImperativeLoopExpCS, gen_qvtoperational_cst_ImperativeIterateExpCS_ImperativeLoopExpCS, gen_qvtoperational_cst_SwitchExpCS_StatementCS, gen_qvtoperational_cst_SwitchAltExpCS_StatementCS, gen_qvtoperational_cst_ImperativeLoopExpCS_cst_LoopExpCS, gen_qvtoperational_cst_ImperativeLoopExpCS_cst_StatementCS, gen_qvtoperational_cst_AssignStatementCS_StatementCS, gen_qvtoperational_cst_BreakExpCS_StatementCS, gen_qvtoperational_cst_ContinueExpCS_StatementCS, gen_qvtoperational_cst_VariableInitializationCS_StatementCS, gen_qvtoperational_cst_ObjectExpCS_cst_InstantiationExpCS, gen_qvtoperational_cst_ObjectExpCS_cst_ElementWithBody, gen_qvtoperational_cst_MappingCallExpCS_ImperativeOperationCallExpCS, gen_qvtoperational_cst_ImperativeOperationCallExpCS_OperationCallExpCS, gen_qvtoperational_cst_DirectionKindCS_CSTNode, gen_qvtoperational_cst_ExpressionStatementCS_StatementCS, gen_qvtoperational_cst_MappingBodyCS_MappingSectionCS, gen_qvtoperational_cst_ResolveInExpCS_ResolveExpCS, gen_qvtoperational_cst_ModelTypeCS_cst_CSTNode, gen_qvtoperational_cst_ModelTypeCS_cst_ElementWithBody, gen_qvtoperational_cst_ResolveExpCS_CallExpCS, gen_qvtoperational_cst_PackageRefCS_CSTNode, gen_qvtoperational_cst_TransformationHeaderCS_CSTNode, gen_qvtoperational_cst_ModuleUsageCS_CSTNode, gen_qvtoperational_cst_TransformationRefineCS_CSTNode, gen_qvtoperational_cst_TypeSpecCS_CSTNode, gen_qvtoperational_cst_LogExpCS_OperationCallExpCS, gen_qvtoperational_cst_ModuleKindCS_CSTNode, gen_qvtoperational_cst_ModuleRefCS_CSTNode, gen_qvtoperational_cst_ReturnExpCS_StatementCS, gen_qvtoperational_cst_MappingExtensionCS_CSTNode, gen_qvtoperational_cst_InstantiationExpCS_StatementCS, gen_qvtoperational_cst_ListTypeCS_TypeCS, gen_qvtoperational_cst_AssertExpCS_StatementCS, gen_qvtoperational_cst_DictLiteralPartCS_CSTNode, gen_qvtoperational_cst_TagCS_CSTNode, gen_qvtoperational_cst_UnitCS_CSTNode, gen_qvtoperational_cst_ListLiteralExpCS_LiteralExpCS, gen_qvtoperational_cst_DictionaryTypeCS_TypeCS, gen_qvtoperational_cst_DictLiteralExpCS_LiteralExpCS, gen_qvtoperational_cst_ScopedNameCS_CSTNode, gen_qvtoperational_cst_ResolveOpArgsExpCS_CSTNode},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)