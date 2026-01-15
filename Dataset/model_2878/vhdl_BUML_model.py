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
UnaryOperator: Enumeration = Enumeration(
    name="UnaryOperator",
    literals={
            EnumerationLiteral(name="ABS"),
			EnumerationLiteral(name="NOT")
    }
)

RelationalOperator: Enumeration = Enumeration(
    name="RelationalOperator",
    literals={
            EnumerationLiteral(name="EQ"),
			EnumerationLiteral(name="NEQ"),
			EnumerationLiteral(name="LOWERTHAN"),
			EnumerationLiteral(name="LE"),
			EnumerationLiteral(name="GREATERTHAN"),
			EnumerationLiteral(name="GE")
    }
)

LogicalOperator: Enumeration = Enumeration(
    name="LogicalOperator",
    literals={
            EnumerationLiteral(name="AND"),
			EnumerationLiteral(name="OR"),
			EnumerationLiteral(name="NAND"),
			EnumerationLiteral(name="NOR"),
			EnumerationLiteral(name="XOR"),
			EnumerationLiteral(name="XNOR")
    }
)

AddingOperator: Enumeration = Enumeration(
    name="AddingOperator",
    literals={
            EnumerationLiteral(name="PLUS"),
			EnumerationLiteral(name="MINUS"),
			EnumerationLiteral(name="AMPERSAND")
    }
)

Sign: Enumeration = Enumeration(
    name="Sign",
    literals={
            EnumerationLiteral(name="PLUS"),
			EnumerationLiteral(name="MINUS")
    }
)

MultiplyingOperator: Enumeration = Enumeration(
    name="MultiplyingOperator",
    literals={
            EnumerationLiteral(name="MUL"),
			EnumerationLiteral(name="DIV"),
			EnumerationLiteral(name="MOD"),
			EnumerationLiteral(name="REM")
    }
)

ShiftOperator: Enumeration = Enumeration(
    name="ShiftOperator",
    literals={
            EnumerationLiteral(name="SLL"),
			EnumerationLiteral(name="SRL"),
			EnumerationLiteral(name="SLA"),
			EnumerationLiteral(name="SRA"),
			EnumerationLiteral(name="ROL"),
			EnumerationLiteral(name="ROR")
    }
)

RangeDirection: Enumeration = Enumeration(
    name="RangeDirection",
    literals={
            EnumerationLiteral(name="TO"),
			EnumerationLiteral(name="DOWNTO")
    }
)

SignalKind: Enumeration = Enumeration(
    name="SignalKind",
    literals={
            EnumerationLiteral(name="REGISTER"),
			EnumerationLiteral(name="BUS")
    }
)

Mode: Enumeration = Enumeration(
    name="Mode",
    literals={
            EnumerationLiteral(name="IN"),
			EnumerationLiteral(name="OUT"),
			EnumerationLiteral(name="INOUT"),
			EnumerationLiteral(name="BUFFER"),
			EnumerationLiteral(name="LINKAGE")
    }
)

EntityClass: Enumeration = Enumeration(
    name="EntityClass",
    literals={
            EnumerationLiteral(name="ENTITY"),
			EnumerationLiteral(name="ARCHITECTURE"),
			EnumerationLiteral(name="CONFIGURATION"),
			EnumerationLiteral(name="PROCEDURE"),
			EnumerationLiteral(name="FUNCTION"),
			EnumerationLiteral(name="PACKAGE"),
			EnumerationLiteral(name="TYPE"),
			EnumerationLiteral(name="SUBTYPE"),
			EnumerationLiteral(name="CONSTANT"),
			EnumerationLiteral(name="SIGNAL"),
			EnumerationLiteral(name="VARIABLE"),
			EnumerationLiteral(name="COMPONENT"),
			EnumerationLiteral(name="LABEL"),
			EnumerationLiteral(name="LITERAL"),
			EnumerationLiteral(name="UNITS"),
			EnumerationLiteral(name="GROUP"),
			EnumerationLiteral(name="FILE"),
			EnumerationLiteral(name="NATURE"),
			EnumerationLiteral(name="SUBNATURE"),
			EnumerationLiteral(name="QUANTITY"),
			EnumerationLiteral(name="TERMINAL")
    }
)

Purity: Enumeration = Enumeration(
    name="Purity",
    literals={
            EnumerationLiteral(name="IMPURE"),
			EnumerationLiteral(name="PURE")
    }
)

# Classes
vhdl_Architecture = Class(name="vhdl::Architecture")
Module = Class(name="Module")
Named = Class(name="Named")
vhdl_EntityReference = Class(name="vhdl::EntityReference", is_abstract=True)
Statement = Class(name="Statement")
vhdl_Component = Class(name="vhdl::Component")
declaration_Declaration = Class(name="declaration::Declaration")
vhdl_Generics = Class(name="vhdl::Generics")
vhdl_Ports = Class(name="vhdl::Ports")
vhdl_DesignUnit = Class(name="vhdl::DesignUnit")
VhdlObject = Class(name="VhdlObject")
vhdl_Name = Class(name="vhdl::Name", is_abstract=True)
vhdl_Module = Class(name="vhdl::Module", is_abstract=True)
Declaration = Class(name="Declaration")
vhdl_Entity = Class(name="vhdl::Entity")
vhdl_Model = Class(name="vhdl::Model")
vhdl_Package = Class(name="vhdl::Package")
vhdl_PackageBody = Class(name="vhdl::PackageBody")
vhdl_PackageReference = Class(name="vhdl::PackageReference", is_abstract=True)
vhdl_GenericMaps = Class(name="vhdl::GenericMaps")
Expression = Class(name="Expression")
vhdl_PortMaps = Class(name="vhdl::PortMaps")
vhdl_Signature = Class(name="vhdl::Signature")
TypeReference = Class(name="TypeReference")
vhdl_Named = Class(name="vhdl::Named", is_abstract=True)
vhdl_MultiNamed = Class(name="vhdl::MultiNamed")
vhdl_MultiName = Class(name="vhdl::MultiName", is_abstract=True)
vhdl_VhdlObject = Class(name="vhdl::VhdlObject", is_abstract=True)
MultiName = Class(name="MultiName")
type_TypeReference = Class(name="type::TypeReference")
nature_NatureReference = Class(name="nature::NatureReference")
EntityReference = Class(name="EntityReference")
PackageReference = Class(name="PackageReference")
ComponentReference = Class(name="ComponentReference")
configuration_ConfigurationReference = Class(name="configuration::ConfigurationReference")
CallReference = Class(name="CallReference")
vhdl_NameList = Class(name="vhdl::NameList")
vhdl_EntityResolvedReference = Class(name="vhdl::EntityResolvedReference")
vhdl_PackageResolvedReference = Class(name="vhdl::PackageResolvedReference")
vhdl_CallReference = Class(name="vhdl::CallReference", is_abstract=True)
vhdl_CallResolvedReference = Class(name="vhdl::CallResolvedReference")
SubprogramDeclaration = Class(name="SubprogramDeclaration")
vhdl_statement_ReportStatement = Class(name="vhdl::statement::ReportStatement")
vhdl_statement_ReturnStatement = Class(name="vhdl::statement::ReturnStatement")
ExpressionStatement = Class(name="ExpressionStatement")
vhdl_statement_ConditionalSignalAssignmentStatement = Class(name="vhdl::statement::ConditionalSignalAssignmentStatement")
SignalAssignmentStatement = Class(name="SignalAssignmentStatement")
vhdl_statement_SelectedSignalAssignmentStatement = Class(name="vhdl::statement::SelectedSignalAssignmentStatement")
ConditionalSignalAssignmentStatement = Class(name="ConditionalSignalAssignmentStatement")
vhdl_statement_SequentialSignalAssignmentStatement = Class(name="vhdl::statement::SequentialSignalAssignmentStatement")
vhdl_statement_SignalAssignmentStatement = Class(name="vhdl::statement::SignalAssignmentStatement", is_abstract=True)
DelayMechanism = Class(name="DelayMechanism")
vhdl_statement_WaitStatement = Class(name="vhdl::statement::WaitStatement")
statement_vhdl_MultiName = Class(name="statement::vhdl::MultiName")
vhdl_ComponentReference = Class(name="vhdl::ComponentReference", is_abstract=True)
vhdl_ComponentResolvedReference = Class(name="vhdl::ComponentResolvedReference")
vhdl_statement_VariableAssignmentStatement = Class(name="vhdl::statement::VariableAssignmentStatement")
vhdl_statement_SimultaneousCaseStatement = Class(name="vhdl::statement::SimultaneousCaseStatement")
CaseStatement = Class(name="CaseStatement")
vhdl_statement_CaseStatement = Class(name="vhdl::statement::CaseStatement")
CaseAlternative = Class(name="CaseAlternative")
vhdl_statement_CaseAlternative = Class(name="vhdl::statement::CaseAlternative")
vhdl_statement_SimultaneousIfStatement = Class(name="vhdl::statement::SimultaneousIfStatement")
IfStatement = Class(name="IfStatement")
vhdl_statement_IfStatement = Class(name="vhdl::statement::IfStatement")
IfStatementTest = Class(name="IfStatementTest")
vhdl_statement_ProcedureCallStatement = Class(name="vhdl::statement::ProcedureCallStatement")
statement_vhdl_CallReference = Class(name="statement::vhdl::CallReference")
vhdl_statement_SimultaneousProceduralStatement = Class(name="vhdl::statement::SimultaneousProceduralStatement")
vhdl_statement_ProcessStatement = Class(name="vhdl::statement::ProcessStatement")
vhdl_statement_IfStatementTest = Class(name="vhdl::statement::IfStatementTest")
vhdl_statement_AssertionStatement = Class(name="vhdl::statement::AssertionStatement")
vhdl_statement_BlockStatement = Class(name="vhdl::statement::BlockStatement")
statement_vhdl_Generics = Class(name="statement::vhdl::Generics")
statement_vhdl_GenericMaps = Class(name="statement::vhdl::GenericMaps")
statement_vhdl_Ports = Class(name="statement::vhdl::Ports")
statement_vhdl_PortMaps = Class(name="statement::vhdl::PortMaps")
vhdl_statement_BreakStatement = Class(name="vhdl::statement::BreakStatement")
BreakStatementItem = Class(name="BreakStatementItem")
vhdl_statement_BreakStatementItem = Class(name="vhdl::statement::BreakStatementItem")
statement_vhdl_Name = Class(name="statement::vhdl::Name")
vhdl_statement_ComponentInstantiationStatement = Class(name="vhdl::statement::ComponentInstantiationStatement")
InstantiationStatement = Class(name="InstantiationStatement")
statement_vhdl_ComponentReference = Class(name="statement::vhdl::ComponentReference")
vhdl_statement_EntityInstantiationStatement = Class(name="vhdl::statement::EntityInstantiationStatement")
statement_vhdl_EntityReference = Class(name="statement::vhdl::EntityReference")
vhdl_statement_ConfigurationInstantiationStatement = Class(name="vhdl::statement::ConfigurationInstantiationStatement")
ConfigurationReference = Class(name="ConfigurationReference")
vhdl_statement_SimpleSimultaneousStatement = Class(name="vhdl::statement::SimpleSimultaneousStatement")
vhdl_statement_InstantiationStatement = Class(name="vhdl::statement::InstantiationStatement")
vhdl_statement_GenerateStatement = Class(name="vhdl::statement::GenerateStatement")
GenerationScheme = Class(name="GenerationScheme")
vhdl_statement_LoopStatement = Class(name="vhdl::statement::LoopStatement")
IterationScheme = Class(name="IterationScheme")
vhdl_statement_ExitStatement = Class(name="vhdl::statement::ExitStatement")
vhdl_statement_Statement = Class(name="vhdl::statement::Statement", is_abstract=True)
vhdl_statement_IterationScheme = Class(name="vhdl::statement::IterationScheme")
vhdl_statement_WhileIterationScheme = Class(name="vhdl::statement::WhileIterationScheme")
vhdl_statement_DelayMechanism = Class(name="vhdl::statement::DelayMechanism", is_abstract=True)
vhdl_statement_ExpressionStatement = Class(name="vhdl::statement::ExpressionStatement")
vhdl_statement_ForGenerationScheme = Class(name="vhdl::statement::ForGenerationScheme")
vhdl_statement_NextStatement = Class(name="vhdl::statement::NextStatement")
vhdl_statement_GenerationScheme = Class(name="vhdl::statement::GenerationScheme", is_abstract=True)
vhdl_statement_IfGenerationScheme = Class(name="vhdl::statement::IfGenerationScheme")
vhdl_statement_RejectMechanism = Class(name="vhdl::statement::RejectMechanism")
vhdl_statement_TransportMechanism = Class(name="vhdl::statement::TransportMechanism")
vhdl_expression_AddingExpression = Class(name="vhdl::expression::AddingExpression")
BinaryExpression = Class(name="BinaryExpression")
vhdl_expression_AggregateExpression = Class(name="vhdl::expression::AggregateExpression")
expression_MultiExpression = Class(name="expression::MultiExpression")
Name = Class(name="Name")
vhdl_statement_ForIterationScheme = Class(name="vhdl::statement::ForIterationScheme")
vhdl_expression_AttributeExpression = Class(name="vhdl::expression::AttributeExpression")
expression_ValueExpression = Class(name="expression::ValueExpression")
expression_vhdl_Signature = Class(name="expression::vhdl::Signature")
vhdl_expression_BinaryExpression = Class(name="vhdl::expression::BinaryExpression", is_abstract=True)
vhdl_expression_AllExpression = Class(name="vhdl::expression::AllExpression")
expression_Expression = Class(name="expression::Expression")
vhdl_expression_AllocatorExpression = Class(name="vhdl::expression::AllocatorExpression")
type_Typed = Class(name="type::Typed")
vhdl_expression_AssociationExpression = Class(name="vhdl::expression::AssociationExpression")
vhdl_expression_IndicationExpression = Class(name="vhdl::expression::IndicationExpression", is_abstract=True)
vhdl_expression_SubtypeIndicationExpression = Class(name="vhdl::expression::SubtypeIndicationExpression")
expression_IndicationExpression = Class(name="expression::IndicationExpression")
vhdl_expression_SubnatureIndicationExpression = Class(name="vhdl::expression::SubnatureIndicationExpression")
vhdl_expression_BitStringExpression = Class(name="vhdl::expression::BitStringExpression")
ValueExpression = Class(name="ValueExpression")
vhdl_expression_Expression = Class(name="vhdl::expression::Expression", is_abstract=True)
vhdl_expression_NameExpression = Class(name="vhdl::expression::NameExpression")
expression_vhdl_Name = Class(name="expression::vhdl::Name")
vhdl_expression_NullExpression = Class(name="vhdl::expression::NullExpression")
vhdl_expression_MultiplyingExpression = Class(name="vhdl::expression::MultiplyingExpression")
vhdl_expression_PowerExpression = Class(name="vhdl::expression::PowerExpression")
vhdl_expression_RelationalExpression = Class(name="vhdl::expression::RelationalExpression")
vhdl_expression_ShiftExpression = Class(name="vhdl::expression::ShiftExpression")
vhdl_expression_SignatureExpression = Class(name="vhdl::expression::SignatureExpression")
NatureReference = Class(name="NatureReference")
vhdl_expression_LogicalExpression = Class(name="vhdl::expression::LogicalExpression")
vhdl_expression_UnaryExpression = Class(name="vhdl::expression::UnaryExpression")
vhdl_expression_OpenExpression = Class(name="vhdl::expression::OpenExpression")
vhdl_expression_OthersExpression = Class(name="vhdl::expression::OthersExpression")
vhdl_expression_RangeExpression = Class(name="vhdl::expression::RangeExpression")
expression_BinaryExpression = Class(name="expression::BinaryExpression")
vhdl_expression_SignExpression = Class(name="vhdl::expression::SignExpression")
vhdl_expression_CharacterExpression = Class(name="vhdl::expression::CharacterExpression")
type_EnumerationLiteral = Class(name="type::EnumerationLiteral")
vhdl_expression_IdentifierExpression = Class(name="vhdl::expression::IdentifierExpression")
vhdl_expression_UnitValueExpression = Class(name="vhdl::expression::UnitValueExpression")
vhdl_expression_UnaffectedExpression = Class(name="vhdl::expression::UnaffectedExpression")
vhdl_expression_ValueExpression = Class(name="vhdl::expression::ValueExpression")
vhdl_expression_WaveformExpression = Class(name="vhdl::expression::WaveformExpression")
vhdl_expression_StringExpression = Class(name="vhdl::expression::StringExpression")
vhdl_expression_MultiExpression = Class(name="vhdl::expression::MultiExpression")
vhdl_expression_ConditionalWaveformExpression = Class(name="vhdl::expression::ConditionalWaveformExpression")
AssociationExpression = Class(name="AssociationExpression")
vhdl_expression_TypeQualificationExpression = Class(name="vhdl::expression::TypeQualificationExpression")
vhdl_declaration_AliasDeclaration = Class(name="vhdl::declaration::AliasDeclaration")
declaration_vhdl_Name = Class(name="declaration::vhdl::Name")
vhdl_declaration_AttributeDeclaration = Class(name="vhdl::declaration::AttributeDeclaration")
vhdl_declaration_AttributeSpecification = Class(name="vhdl::declaration::AttributeSpecification")
declaration_vhdl_MultiName = Class(name="declaration::vhdl::MultiName")
vhdl_declaration_BranchQuantityDeclaration = Class(name="vhdl::declaration::BranchQuantityDeclaration")
QuantityDeclaration = Class(name="QuantityDeclaration")
vhdl_declaration_FreeQuantityDeclaration = Class(name="vhdl::declaration::FreeQuantityDeclaration")
declaration_QuantityDeclaration = Class(name="declaration::QuantityDeclaration")
MultiNamed = Class(name="MultiNamed")
vhdl_declaration_LimitDeclaration = Class(name="vhdl::declaration::LimitDeclaration")
vhdl_declaration_QuantityDeclaration = Class(name="vhdl::declaration::QuantityDeclaration", is_abstract=True)
QuantityAspect = Class(name="QuantityAspect")
vhdl_declaration_SubnatureDeclaration = Class(name="vhdl::declaration::SubnatureDeclaration")
nature_Natured = Class(name="nature::Natured")
vhdl_declaration_SubprogramDeclaration = Class(name="vhdl::declaration::SubprogramDeclaration", is_abstract=True)
SubprogramBody = Class(name="SubprogramBody")
vhdl_declaration_ProcedureDeclaration = Class(name="vhdl::declaration::ProcedureDeclaration")
vhdl_declaration_FunctionDeclaration = Class(name="vhdl::declaration::FunctionDeclaration")
declaration_SubprogramDeclaration = Class(name="declaration::SubprogramDeclaration")
vhdl_declaration_SubprogramBody = Class(name="vhdl::declaration::SubprogramBody")
vhdl_declaration_SourceQuantityDeclaration = Class(name="vhdl::declaration::SourceQuantityDeclaration")
SourceAspect = Class(name="SourceAspect")
declaration_vhdl_ComponentReference = Class(name="declaration::vhdl::ComponentReference")
declaration_vhdl_EntityReference = Class(name="declaration::vhdl::EntityReference")
declaration_vhdl_GenericMaps = Class(name="declaration::vhdl::GenericMaps")
declaration_vhdl_PortMaps = Class(name="declaration::vhdl::PortMaps")
vhdl_declaration_Declaration = Class(name="vhdl::declaration::Declaration", is_abstract=True)
vhdl_declaration_DisconnectionSpecification = Class(name="vhdl::declaration::DisconnectionSpecification")
vhdl_declaration_FileDeclaration = Class(name="vhdl::declaration::FileDeclaration")
vhdl_declaration_TerminalDeclaration = Class(name="vhdl::declaration::TerminalDeclaration")
vhdl_declaration_TypeDeclaration = Class(name="vhdl::declaration::TypeDeclaration")
TypeDefinition = Class(name="TypeDefinition")
vhdl_declaration_ConstantDeclaration = Class(name="vhdl::declaration::ConstantDeclaration")
ValueDeclaration = Class(name="ValueDeclaration")
vhdl_declaration_GroupDeclaration = Class(name="vhdl::declaration::GroupDeclaration")
vhdl_declaration_SubtypeDeclaration = Class(name="vhdl::declaration::SubtypeDeclaration")
vhdl_declaration_ConfigurationSpecification = Class(name="vhdl::declaration::ConfigurationSpecification")
vhdl_declaration_NatureDeclaration = Class(name="vhdl::declaration::NatureDeclaration")
NatureDefinition = Class(name="NatureDefinition")
vhdl_declaration_SignalDeclaration = Class(name="vhdl::declaration::SignalDeclaration")
vhdl_declaration_UseClauseDeclaration = Class(name="vhdl::declaration::UseClauseDeclaration")
vhdl_declaration_VariableDeclaration = Class(name="vhdl::declaration::VariableDeclaration")
vhdl_declaration_ValueDeclaration = Class(name="vhdl::declaration::ValueDeclaration", is_abstract=True)
vhdl_declaration_GroupTemplateDeclaration = Class(name="vhdl::declaration::GroupTemplateDeclaration")
vhdl_type_AccessTypeDefinition = Class(name="vhdl::type::AccessTypeDefinition")
type_TypeDefinition = Class(name="type::TypeDefinition")
vhdl_type_CompositeTypeDefinition = Class(name="vhdl::type::CompositeTypeDefinition", is_abstract=True)
vhdl_type_RecordTypeDefinition = Class(name="vhdl::type::RecordTypeDefinition")
CompositeTypeDefinition = Class(name="CompositeTypeDefinition")
RecordTypeElement = Class(name="RecordTypeElement")
vhdl_type_ArrayTypeDefinition = Class(name="vhdl::type::ArrayTypeDefinition")
type_CompositeTypeDefinition = Class(name="type::CompositeTypeDefinition")
vhdl_type_ConstrainedArrayTypeDefinition = Class(name="vhdl::type::ConstrainedArrayTypeDefinition")
ArrayTypeDefinition = Class(name="ArrayTypeDefinition")
vhdl_type_UnconstrainedArrayTypeDefinition = Class(name="vhdl::type::UnconstrainedArrayTypeDefinition")
vhdl_type_EnumerationLiteral = Class(name="vhdl::type::EnumerationLiteral", is_abstract=True)
vhdl_type_EnumerationTypeDefinition = Class(name="vhdl::type::EnumerationTypeDefinition")
EnumerationLiteral = Class(name="EnumerationLiteral")
vhdl_type_FileTypeDefinition = Class(name="vhdl::type::FileTypeDefinition")
vhdl_type_PhysicalTypeDefinition = Class(name="vhdl::type::PhysicalTypeDefinition")
PhysicalTypeDefinitionSecondary = Class(name="PhysicalTypeDefinitionSecondary")
type_vhdl_Name = Class(name="type::vhdl::Name")
vhdl_type_RangeTypeDefinition = Class(name="vhdl::type::RangeTypeDefinition")
vhdl_type_RecordTypeElement = Class(name="vhdl::type::RecordTypeElement")
vhdl_type_Typed = Class(name="vhdl::type::Typed", is_abstract=True)
vhdl_type_TypeDefinition = Class(name="vhdl::type::TypeDefinition", is_abstract=True)
vhdl_type_TypeReference = Class(name="vhdl::type::TypeReference", is_abstract=True)
vhdl_nature_ArrayNatureDefinition = Class(name="vhdl::nature::ArrayNatureDefinition")
nature_CompositeNatureDefinition = Class(name="nature::CompositeNatureDefinition")
vhdl_nature_CompositeNatureDefinition = Class(name="vhdl::nature::CompositeNatureDefinition")
vhdl_nature_ConstrainedArrayNatureDefinition = Class(name="vhdl::nature::ConstrainedArrayNatureDefinition")
ArrayNatureDefinition = Class(name="ArrayNatureDefinition")
vhdl_nature_NatureDefinition = Class(name="vhdl::nature::NatureDefinition")
vhdl_nature_RecordNatureDefinition = Class(name="vhdl::nature::RecordNatureDefinition")
CompositeNatureDefinition = Class(name="CompositeNatureDefinition")
RecordNatureElement = Class(name="RecordNatureElement")
vhdl_nature_RecordNatureElement = Class(name="vhdl::nature::RecordNatureElement")
vhdl_type_PhysicalTypeDefinitionSecondary = Class(name="vhdl::type::PhysicalTypeDefinitionSecondary")
vhdl_nature_UnconstrainedArrayNatureDefinition = Class(name="vhdl::nature::UnconstrainedArrayNatureDefinition")
vhdl_nature_NatureReference = Class(name="vhdl::nature::NatureReference", is_abstract=True)
vhdl_nature_Natured = Class(name="vhdl::nature::Natured", is_abstract=True)
vhdl_ams_QuantityAspect = Class(name="vhdl::ams::QuantityAspect")
vhdl_ams_SourceAspect = Class(name="vhdl::ams::SourceAspect")
vhdl_ams_Spectrum = Class(name="vhdl::ams::Spectrum")
vhdl_ams_Noise = Class(name="vhdl::ams::Noise")
vhdl_nature_ScalarNatureDefinition = Class(name="vhdl::nature::ScalarNatureDefinition")
nature_vhdl_Name = Class(name="nature::vhdl::Name")
vhdl_configuration_BlockConfiguration = Class(name="vhdl::configuration::BlockConfiguration")
configuration_ConfigurationItem = Class(name="configuration::ConfigurationItem")
configuration_vhdl_Name = Class(name="configuration::vhdl::Name")
ConfigurationItem = Class(name="ConfigurationItem")
vhdl_configuration_ComponentConfiguration = Class(name="vhdl::configuration::ComponentConfiguration")
configuration_vhdl_MultiName = Class(name="configuration::vhdl::MultiName")
configuration_vhdl_GenericMaps = Class(name="configuration::vhdl::GenericMaps")
configuration_vhdl_PortMaps = Class(name="configuration::vhdl::PortMaps")
BlockConfiguration = Class(name="BlockConfiguration")
vhdl_configuration_Configuration = Class(name="vhdl::configuration::Configuration")
configuration_vhdl_EntityReference = Class(name="configuration::vhdl::EntityReference")
vhdl_configuration_ConfigurationReference = Class(name="vhdl::configuration::ConfigurationReference", is_abstract=True)
vhdl_configuration_ConfigurationResolvedReference = Class(name="vhdl::configuration::ConfigurationResolvedReference")
Configuration = Class(name="Configuration")
vhdl_configuration_ConfigurationItem = Class(name="vhdl::configuration::ConfigurationItem")

# vhdl_Architecture class attributes and methods

# Module class attributes and methods

# Named class attributes and methods

# vhdl_EntityReference class attributes and methods

# Statement class attributes and methods

# vhdl_Component class attributes and methods

# declaration_Declaration class attributes and methods

# vhdl_Generics class attributes and methods

# vhdl_Ports class attributes and methods

# vhdl_DesignUnit class attributes and methods
vhdl_DesignUnit_library: Property = Property(name="library", type=StringType)
vhdl_DesignUnit.attributes={vhdl_DesignUnit_library}

# VhdlObject class attributes and methods

# vhdl_Name class attributes and methods

# vhdl_Module class attributes and methods

# Declaration class attributes and methods

# vhdl_Entity class attributes and methods

# vhdl_Model class attributes and methods

# vhdl_Package class attributes and methods

# vhdl_PackageBody class attributes and methods

# vhdl_PackageReference class attributes and methods

# vhdl_GenericMaps class attributes and methods

# Expression class attributes and methods

# vhdl_PortMaps class attributes and methods

# vhdl_Signature class attributes and methods

# TypeReference class attributes and methods

# vhdl_Named class attributes and methods

# vhdl_MultiNamed class attributes and methods

# vhdl_MultiName class attributes and methods

# vhdl_VhdlObject class attributes and methods
vhdl_VhdlObject_id: Property = Property(name="id", type=StringType)
vhdl_VhdlObject.attributes={vhdl_VhdlObject_id}

# MultiName class attributes and methods

# type_TypeReference class attributes and methods

# nature_NatureReference class attributes and methods

# EntityReference class attributes and methods

# PackageReference class attributes and methods

# ComponentReference class attributes and methods

# configuration_ConfigurationReference class attributes and methods

# CallReference class attributes and methods

# vhdl_NameList class attributes and methods

# vhdl_EntityResolvedReference class attributes and methods

# vhdl_PackageResolvedReference class attributes and methods

# vhdl_CallReference class attributes and methods

# vhdl_CallResolvedReference class attributes and methods

# SubprogramDeclaration class attributes and methods

# vhdl_statement_ReportStatement class attributes and methods

# vhdl_statement_ReturnStatement class attributes and methods

# ExpressionStatement class attributes and methods

# vhdl_statement_ConditionalSignalAssignmentStatement class attributes and methods

# SignalAssignmentStatement class attributes and methods

# vhdl_statement_SelectedSignalAssignmentStatement class attributes and methods

# ConditionalSignalAssignmentStatement class attributes and methods

# vhdl_statement_SequentialSignalAssignmentStatement class attributes and methods

# vhdl_statement_SignalAssignmentStatement class attributes and methods
vhdl_statement_SignalAssignmentStatement_postponed: Property = Property(name="postponed", type=BooleanType)
vhdl_statement_SignalAssignmentStatement_guarded: Property = Property(name="guarded", type=BooleanType)
vhdl_statement_SignalAssignmentStatement.attributes={vhdl_statement_SignalAssignmentStatement_postponed, vhdl_statement_SignalAssignmentStatement_guarded}

# DelayMechanism class attributes and methods

# vhdl_statement_WaitStatement class attributes and methods

# statement_vhdl_MultiName class attributes and methods

# vhdl_ComponentReference class attributes and methods

# vhdl_ComponentResolvedReference class attributes and methods

# vhdl_statement_VariableAssignmentStatement class attributes and methods

# vhdl_statement_SimultaneousCaseStatement class attributes and methods

# CaseStatement class attributes and methods

# vhdl_statement_CaseStatement class attributes and methods

# CaseAlternative class attributes and methods

# vhdl_statement_CaseAlternative class attributes and methods

# vhdl_statement_SimultaneousIfStatement class attributes and methods

# IfStatement class attributes and methods

# vhdl_statement_IfStatement class attributes and methods

# IfStatementTest class attributes and methods

# vhdl_statement_ProcedureCallStatement class attributes and methods
vhdl_statement_ProcedureCallStatement_postponed: Property = Property(name="postponed", type=BooleanType)
vhdl_statement_ProcedureCallStatement.attributes={vhdl_statement_ProcedureCallStatement_postponed}

# statement_vhdl_CallReference class attributes and methods

# vhdl_statement_SimultaneousProceduralStatement class attributes and methods

# vhdl_statement_ProcessStatement class attributes and methods
vhdl_statement_ProcessStatement_postponed: Property = Property(name="postponed", type=BooleanType)
vhdl_statement_ProcessStatement.attributes={vhdl_statement_ProcessStatement_postponed}

# vhdl_statement_IfStatementTest class attributes and methods

# vhdl_statement_AssertionStatement class attributes and methods
vhdl_statement_AssertionStatement_postponed: Property = Property(name="postponed", type=BooleanType)
vhdl_statement_AssertionStatement.attributes={vhdl_statement_AssertionStatement_postponed}

# vhdl_statement_BlockStatement class attributes and methods

# statement_vhdl_Generics class attributes and methods

# statement_vhdl_GenericMaps class attributes and methods

# statement_vhdl_Ports class attributes and methods

# statement_vhdl_PortMaps class attributes and methods

# vhdl_statement_BreakStatement class attributes and methods

# BreakStatementItem class attributes and methods

# vhdl_statement_BreakStatementItem class attributes and methods

# statement_vhdl_Name class attributes and methods

# vhdl_statement_ComponentInstantiationStatement class attributes and methods

# InstantiationStatement class attributes and methods

# statement_vhdl_ComponentReference class attributes and methods

# vhdl_statement_EntityInstantiationStatement class attributes and methods

# statement_vhdl_EntityReference class attributes and methods

# vhdl_statement_ConfigurationInstantiationStatement class attributes and methods

# ConfigurationReference class attributes and methods

# vhdl_statement_SimpleSimultaneousStatement class attributes and methods

# vhdl_statement_InstantiationStatement class attributes and methods

# vhdl_statement_GenerateStatement class attributes and methods

# GenerationScheme class attributes and methods

# vhdl_statement_LoopStatement class attributes and methods

# IterationScheme class attributes and methods

# vhdl_statement_ExitStatement class attributes and methods
vhdl_statement_ExitStatement_exit: Property = Property(name="exit", type=StringType)
vhdl_statement_ExitStatement.attributes={vhdl_statement_ExitStatement_exit}

# vhdl_statement_Statement class attributes and methods
vhdl_statement_Statement_label: Property = Property(name="label", type=StringType)
vhdl_statement_Statement.attributes={vhdl_statement_Statement_label}

# vhdl_statement_IterationScheme class attributes and methods

# vhdl_statement_WhileIterationScheme class attributes and methods

# vhdl_statement_DelayMechanism class attributes and methods

# vhdl_statement_ExpressionStatement class attributes and methods

# vhdl_statement_ForGenerationScheme class attributes and methods
vhdl_statement_ForGenerationScheme_variable: Property = Property(name="variable", type=StringType)
vhdl_statement_ForGenerationScheme.attributes={vhdl_statement_ForGenerationScheme_variable}

# vhdl_statement_NextStatement class attributes and methods
vhdl_statement_NextStatement_next: Property = Property(name="next", type=StringType)
vhdl_statement_NextStatement.attributes={vhdl_statement_NextStatement_next}

# vhdl_statement_GenerationScheme class attributes and methods

# vhdl_statement_IfGenerationScheme class attributes and methods

# vhdl_statement_RejectMechanism class attributes and methods

# vhdl_statement_TransportMechanism class attributes and methods

# vhdl_expression_AddingExpression class attributes and methods
vhdl_expression_AddingExpression_operator: Property = Property(name="operator", type=StringType)
vhdl_expression_AddingExpression.attributes={vhdl_expression_AddingExpression_operator}

# BinaryExpression class attributes and methods

# vhdl_expression_AggregateExpression class attributes and methods

# expression_MultiExpression class attributes and methods

# Name class attributes and methods

# vhdl_statement_ForIterationScheme class attributes and methods
vhdl_statement_ForIterationScheme_variable: Property = Property(name="variable", type=StringType)
vhdl_statement_ForIterationScheme.attributes={vhdl_statement_ForIterationScheme_variable}

# vhdl_expression_AttributeExpression class attributes and methods

# expression_ValueExpression class attributes and methods

# expression_vhdl_Signature class attributes and methods

# vhdl_expression_BinaryExpression class attributes and methods

# vhdl_expression_AllExpression class attributes and methods

# expression_Expression class attributes and methods

# vhdl_expression_AllocatorExpression class attributes and methods

# type_Typed class attributes and methods

# vhdl_expression_AssociationExpression class attributes and methods

# vhdl_expression_IndicationExpression class attributes and methods

# vhdl_expression_SubtypeIndicationExpression class attributes and methods

# expression_IndicationExpression class attributes and methods

# vhdl_expression_SubnatureIndicationExpression class attributes and methods

# vhdl_expression_BitStringExpression class attributes and methods

# ValueExpression class attributes and methods

# vhdl_expression_Expression class attributes and methods

# vhdl_expression_NameExpression class attributes and methods

# expression_vhdl_Name class attributes and methods

# vhdl_expression_NullExpression class attributes and methods

# vhdl_expression_MultiplyingExpression class attributes and methods
vhdl_expression_MultiplyingExpression_operator: Property = Property(name="operator", type=StringType)
vhdl_expression_MultiplyingExpression.attributes={vhdl_expression_MultiplyingExpression_operator}

# vhdl_expression_PowerExpression class attributes and methods

# vhdl_expression_RelationalExpression class attributes and methods
vhdl_expression_RelationalExpression_operator: Property = Property(name="operator", type=StringType)
vhdl_expression_RelationalExpression.attributes={vhdl_expression_RelationalExpression_operator}

# vhdl_expression_ShiftExpression class attributes and methods
vhdl_expression_ShiftExpression_operator: Property = Property(name="operator", type=StringType)
vhdl_expression_ShiftExpression.attributes={vhdl_expression_ShiftExpression_operator}

# vhdl_expression_SignatureExpression class attributes and methods

# NatureReference class attributes and methods

# vhdl_expression_LogicalExpression class attributes and methods
vhdl_expression_LogicalExpression_operator: Property = Property(name="operator", type=StringType)
vhdl_expression_LogicalExpression.attributes={vhdl_expression_LogicalExpression_operator}

# vhdl_expression_UnaryExpression class attributes and methods
vhdl_expression_UnaryExpression_operator: Property = Property(name="operator", type=StringType)
vhdl_expression_UnaryExpression.attributes={vhdl_expression_UnaryExpression_operator}

# vhdl_expression_OpenExpression class attributes and methods

# vhdl_expression_OthersExpression class attributes and methods

# vhdl_expression_RangeExpression class attributes and methods
vhdl_expression_RangeExpression_direction: Property = Property(name="direction", type=StringType)
vhdl_expression_RangeExpression.attributes={vhdl_expression_RangeExpression_direction}

# expression_BinaryExpression class attributes and methods

# vhdl_expression_SignExpression class attributes and methods
vhdl_expression_SignExpression_sign: Property = Property(name="sign", type=StringType)
vhdl_expression_SignExpression.attributes={vhdl_expression_SignExpression_sign}

# vhdl_expression_CharacterExpression class attributes and methods

# type_EnumerationLiteral class attributes and methods

# vhdl_expression_IdentifierExpression class attributes and methods

# vhdl_expression_UnitValueExpression class attributes and methods

# vhdl_expression_UnaffectedExpression class attributes and methods

# vhdl_expression_ValueExpression class attributes and methods
vhdl_expression_ValueExpression_value: Property = Property(name="value", type=StringType)
vhdl_expression_ValueExpression.attributes={vhdl_expression_ValueExpression_value}

# vhdl_expression_WaveformExpression class attributes and methods

# vhdl_expression_StringExpression class attributes and methods

# vhdl_expression_MultiExpression class attributes and methods

# vhdl_expression_ConditionalWaveformExpression class attributes and methods

# AssociationExpression class attributes and methods

# vhdl_expression_TypeQualificationExpression class attributes and methods

# vhdl_declaration_AliasDeclaration class attributes and methods

# declaration_vhdl_Name class attributes and methods

# vhdl_declaration_AttributeDeclaration class attributes and methods

# vhdl_declaration_AttributeSpecification class attributes and methods
vhdl_declaration_AttributeSpecification_class: Property = Property(name="class", type=StringType)
vhdl_declaration_AttributeSpecification.attributes={vhdl_declaration_AttributeSpecification_class}

# declaration_vhdl_MultiName class attributes and methods

# vhdl_declaration_BranchQuantityDeclaration class attributes and methods

# QuantityDeclaration class attributes and methods

# vhdl_declaration_FreeQuantityDeclaration class attributes and methods

# declaration_QuantityDeclaration class attributes and methods

# MultiNamed class attributes and methods

# vhdl_declaration_LimitDeclaration class attributes and methods

# vhdl_declaration_QuantityDeclaration class attributes and methods

# QuantityAspect class attributes and methods

# vhdl_declaration_SubnatureDeclaration class attributes and methods

# nature_Natured class attributes and methods

# vhdl_declaration_SubprogramDeclaration class attributes and methods

# SubprogramBody class attributes and methods

# vhdl_declaration_ProcedureDeclaration class attributes and methods

# vhdl_declaration_FunctionDeclaration class attributes and methods
vhdl_declaration_FunctionDeclaration_purity: Property = Property(name="purity", type=StringType)
vhdl_declaration_FunctionDeclaration.attributes={vhdl_declaration_FunctionDeclaration_purity}

# declaration_SubprogramDeclaration class attributes and methods

# vhdl_declaration_SubprogramBody class attributes and methods

# vhdl_declaration_SourceQuantityDeclaration class attributes and methods

# SourceAspect class attributes and methods

# declaration_vhdl_ComponentReference class attributes and methods

# declaration_vhdl_EntityReference class attributes and methods

# declaration_vhdl_GenericMaps class attributes and methods

# declaration_vhdl_PortMaps class attributes and methods

# vhdl_declaration_Declaration class attributes and methods

# vhdl_declaration_DisconnectionSpecification class attributes and methods

# vhdl_declaration_FileDeclaration class attributes and methods

# vhdl_declaration_TerminalDeclaration class attributes and methods

# vhdl_declaration_TypeDeclaration class attributes and methods

# TypeDefinition class attributes and methods

# vhdl_declaration_ConstantDeclaration class attributes and methods

# ValueDeclaration class attributes and methods

# vhdl_declaration_GroupDeclaration class attributes and methods

# vhdl_declaration_SubtypeDeclaration class attributes and methods

# vhdl_declaration_ConfigurationSpecification class attributes and methods

# vhdl_declaration_NatureDeclaration class attributes and methods

# NatureDefinition class attributes and methods

# vhdl_declaration_SignalDeclaration class attributes and methods
vhdl_declaration_SignalDeclaration_kind: Property = Property(name="kind", type=StringType)
vhdl_declaration_SignalDeclaration_mode: Property = Property(name="mode", type=StringType)
vhdl_declaration_SignalDeclaration.attributes={vhdl_declaration_SignalDeclaration_kind, vhdl_declaration_SignalDeclaration_mode}

# vhdl_declaration_UseClauseDeclaration class attributes and methods

# vhdl_declaration_VariableDeclaration class attributes and methods
vhdl_declaration_VariableDeclaration_shared: Property = Property(name="shared", type=BooleanType)
vhdl_declaration_VariableDeclaration_mode: Property = Property(name="mode", type=StringType)
vhdl_declaration_VariableDeclaration.attributes={vhdl_declaration_VariableDeclaration_mode, vhdl_declaration_VariableDeclaration_shared}

# vhdl_declaration_ValueDeclaration class attributes and methods

# vhdl_declaration_GroupTemplateDeclaration class attributes and methods
vhdl_declaration_GroupTemplateDeclaration_entry: Property = Property(name="entry", type=StringType)
vhdl_declaration_GroupTemplateDeclaration.attributes={vhdl_declaration_GroupTemplateDeclaration_entry}

# vhdl_type_AccessTypeDefinition class attributes and methods

# type_TypeDefinition class attributes and methods

# vhdl_type_CompositeTypeDefinition class attributes and methods

# vhdl_type_RecordTypeDefinition class attributes and methods

# CompositeTypeDefinition class attributes and methods

# RecordTypeElement class attributes and methods

# vhdl_type_ArrayTypeDefinition class attributes and methods

# type_CompositeTypeDefinition class attributes and methods

# vhdl_type_ConstrainedArrayTypeDefinition class attributes and methods

# ArrayTypeDefinition class attributes and methods

# vhdl_type_UnconstrainedArrayTypeDefinition class attributes and methods

# vhdl_type_EnumerationLiteral class attributes and methods

# vhdl_type_EnumerationTypeDefinition class attributes and methods

# EnumerationLiteral class attributes and methods

# vhdl_type_FileTypeDefinition class attributes and methods

# vhdl_type_PhysicalTypeDefinition class attributes and methods
vhdl_type_PhysicalTypeDefinition_primary: Property = Property(name="primary", type=StringType)
vhdl_type_PhysicalTypeDefinition.attributes={vhdl_type_PhysicalTypeDefinition_primary}

# PhysicalTypeDefinitionSecondary class attributes and methods

# type_vhdl_Name class attributes and methods

# vhdl_type_RangeTypeDefinition class attributes and methods
vhdl_type_RangeTypeDefinition_direction: Property = Property(name="direction", type=StringType)
vhdl_type_RangeTypeDefinition.attributes={vhdl_type_RangeTypeDefinition_direction}

# vhdl_type_RecordTypeElement class attributes and methods

# vhdl_type_Typed class attributes and methods

# vhdl_type_TypeDefinition class attributes and methods

# vhdl_type_TypeReference class attributes and methods

# vhdl_nature_ArrayNatureDefinition class attributes and methods

# nature_CompositeNatureDefinition class attributes and methods

# vhdl_nature_CompositeNatureDefinition class attributes and methods

# vhdl_nature_ConstrainedArrayNatureDefinition class attributes and methods

# ArrayNatureDefinition class attributes and methods

# vhdl_nature_NatureDefinition class attributes and methods

# vhdl_nature_RecordNatureDefinition class attributes and methods

# CompositeNatureDefinition class attributes and methods

# RecordNatureElement class attributes and methods

# vhdl_nature_RecordNatureElement class attributes and methods

# vhdl_type_PhysicalTypeDefinitionSecondary class attributes and methods
vhdl_type_PhysicalTypeDefinitionSecondary_number: Property = Property(name="number", type=StringType)
vhdl_type_PhysicalTypeDefinitionSecondary_name: Property = Property(name="name", type=StringType)
vhdl_type_PhysicalTypeDefinitionSecondary.attributes={vhdl_type_PhysicalTypeDefinitionSecondary_name, vhdl_type_PhysicalTypeDefinitionSecondary_number}

# vhdl_nature_UnconstrainedArrayNatureDefinition class attributes and methods

# vhdl_nature_NatureReference class attributes and methods

# vhdl_nature_Natured class attributes and methods

# vhdl_ams_QuantityAspect class attributes and methods

# vhdl_ams_SourceAspect class attributes and methods

# vhdl_ams_Spectrum class attributes and methods

# vhdl_ams_Noise class attributes and methods

# vhdl_nature_ScalarNatureDefinition class attributes and methods

# nature_vhdl_Name class attributes and methods

# vhdl_configuration_BlockConfiguration class attributes and methods

# configuration_ConfigurationItem class attributes and methods

# configuration_vhdl_Name class attributes and methods

# ConfigurationItem class attributes and methods

# vhdl_configuration_ComponentConfiguration class attributes and methods

# configuration_vhdl_MultiName class attributes and methods

# configuration_vhdl_GenericMaps class attributes and methods

# configuration_vhdl_PortMaps class attributes and methods

# BlockConfiguration class attributes and methods

# vhdl_configuration_Configuration class attributes and methods

# configuration_vhdl_EntityReference class attributes and methods

# vhdl_configuration_ConfigurationReference class attributes and methods

# vhdl_configuration_ConfigurationResolvedReference class attributes and methods

# Configuration class attributes and methods

# vhdl_configuration_ConfigurationItem class attributes and methods

# Relationships
of0: BinaryAssociation = BinaryAssociation(
    name="of0",
    ends={
        Property(name="vhdl_EntityReference", type=vhdl_Architecture, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_Architecture", type=vhdl_EntityReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statement1: BinaryAssociation = BinaryAssociation(
    name="statement1",
    ends={
        Property(name="Statement", type=vhdl_Architecture, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_Architecture2", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
generic3: BinaryAssociation = BinaryAssociation(
    name="generic3",
    ends={
        Property(name="vhdl_Generics", type=vhdl_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_Component", type=vhdl_Generics, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
port4: BinaryAssociation = BinaryAssociation(
    name="port4",
    ends={
        Property(name="vhdl_Ports", type=vhdl_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_Component5", type=vhdl_Ports, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
use6: BinaryAssociation = BinaryAssociation(
    name="use6",
    ends={
        Property(name="vhdl_Name", type=vhdl_DesignUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_DesignUnit", type=vhdl_Name, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
module7: BinaryAssociation = BinaryAssociation(
    name="module7",
    ends={
        Property(name="vhdl_Module", type=vhdl_DesignUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_DesignUnit8", type=vhdl_Module, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declaration9: BinaryAssociation = BinaryAssociation(
    name="declaration9",
    ends={
        Property(name="Declaration", type=vhdl_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_Module10", type=Declaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
generic11: BinaryAssociation = BinaryAssociation(
    name="generic11",
    ends={
        Property(name="vhdl_Generics12", type=vhdl_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_Entity", type=vhdl_Generics, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
port13: BinaryAssociation = BinaryAssociation(
    name="port13",
    ends={
        Property(name="vhdl_Ports15", type=vhdl_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_Entity14", type=vhdl_Ports, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declaration20: BinaryAssociation = BinaryAssociation(
    name="declaration20",
    ends={
        Property(name="Declaration22", type=vhdl_Generics, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_Generics21", type=Declaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
design23: BinaryAssociation = BinaryAssociation(
    name="design23",
    ends={
        Property(name="vhdl_DesignUnit24", type=vhdl_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_Model", type=vhdl_DesignUnit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statement16: BinaryAssociation = BinaryAssociation(
    name="statement16",
    ends={
        Property(name="Statement18", type=vhdl_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_Entity17", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
generic19: BinaryAssociation = BinaryAssociation(
    name="generic19",
    ends={
        Property(name="Expression", type=vhdl_GenericMaps, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_GenericMaps", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
port29: BinaryAssociation = BinaryAssociation(
    name="port29",
    ends={
        Property(name="Expression30", type=vhdl_PortMaps, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_PortMaps", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameter31: BinaryAssociation = BinaryAssociation(
    name="parameter31",
    ends={
        Property(name="TypeReference", type=vhdl_Signature, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_Signature", type=TypeReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
return32: BinaryAssociation = BinaryAssociation(
    name="return32",
    ends={
        Property(name="TypeReference34", type=vhdl_Signature, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_Signature33", type=TypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name35: BinaryAssociation = BinaryAssociation(
    name="name35",
    ends={
        Property(name="vhdl_Name36", type=vhdl_Named, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_Named", type=vhdl_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name37: BinaryAssociation = BinaryAssociation(
    name="name37",
    ends={
        Property(name="vhdl_MultiName", type=vhdl_MultiNamed, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_MultiNamed", type=vhdl_MultiName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name38: BinaryAssociation = BinaryAssociation(
    name="name38",
    ends={
        Property(name="vhdl_Name39", type=vhdl_NameList, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_NameList", type=vhdl_Name, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entity40: BinaryAssociation = BinaryAssociation(
    name="entity40",
    ends={
        Property(name="vhdl_Entity41", type=vhdl_EntityResolvedReference, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_EntityResolvedReference", type=vhdl_Entity, multiplicity=Multiplicity(0, 1))
    }
)
name25: BinaryAssociation = BinaryAssociation(
    name="name25",
    ends={
        Property(name="vhdl_PackageReference", type=vhdl_PackageBody, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_PackageBody", type=vhdl_PackageReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declaration26: BinaryAssociation = BinaryAssociation(
    name="declaration26",
    ends={
        Property(name="Declaration28", type=vhdl_Ports, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_Ports27", type=Declaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
component43: BinaryAssociation = BinaryAssociation(
    name="component43",
    ends={
        Property(name="vhdl_Component44", type=vhdl_ComponentResolvedReference, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_ComponentResolvedReference", type=vhdl_Component, multiplicity=Multiplicity(0, 1))
    }
)
call45: BinaryAssociation = BinaryAssociation(
    name="call45",
    ends={
        Property(name="SubprogramDeclaration", type=vhdl_CallResolvedReference, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_CallResolvedReference", type=SubprogramDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
report46: BinaryAssociation = BinaryAssociation(
    name="report46",
    ends={
        Property(name="Expression47", type=vhdl_statement_ReportStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_statement_ReportStatement", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
severity48: BinaryAssociation = BinaryAssociation(
    name="severity48",
    ends={
        Property(name="Expression50", type=vhdl_statement_ReportStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_statement_ReportStatement49", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
waveform51: BinaryAssociation = BinaryAssociation(
    name="waveform51",
    ends={
        Property(name="Expression52", type=vhdl_statement_ConditionalSignalAssignmentStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_statement_ConditionalSignalAssignmentStatement", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
selected53: BinaryAssociation = BinaryAssociation(
    name="selected53",
    ends={
        Property(name="Expression54", type=vhdl_statement_SelectedSignalAssignmentStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_statement_SelectedSignalAssignmentStatement", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
waveform55: BinaryAssociation = BinaryAssociation(
    name="waveform55",
    ends={
        Property(name="Expression56", type=vhdl_statement_SequentialSignalAssignmentStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_statement_SequentialSignalAssignmentStatement", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target57: BinaryAssociation = BinaryAssociation(
    name="target57",
    ends={
        Property(name="Expression58", type=vhdl_statement_SignalAssignmentStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_statement_SignalAssignmentStatement", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
delay59: BinaryAssociation = BinaryAssociation(
    name="delay59",
    ends={
        Property(name="DelayMechanism", type=vhdl_statement_SignalAssignmentStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_statement_SignalAssignmentStatement60", type=DelayMechanism, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sensitivity61: BinaryAssociation = BinaryAssociation(
    name="sensitivity61",
    ends={
        Property(name="statement_vhdl_MultiName", type=vhdl_statement_WaitStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_statement_WaitStatement", type=statement_vhdl_MultiName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
package42: BinaryAssociation = BinaryAssociation(
    name="package42",
    ends={
        Property(name="vhdl_Package", type=vhdl_PackageResolvedReference, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_PackageResolvedReference", type=vhdl_Package, multiplicity=Multiplicity(0, 1))
    }
)
target68: BinaryAssociation = BinaryAssociation(
    name="target68",
    ends={
        Property(name="Expression69", type=vhdl_statement_VariableAssignmentStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_statement_VariableAssignmentStatement", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initial70: BinaryAssociation = BinaryAssociation(
    name="initial70",
    ends={
        Property(name="Expression72", type=vhdl_statement_VariableAssignmentStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_statement_VariableAssignmentStatement71", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
case73: BinaryAssociation = BinaryAssociation(
    name="case73",
    ends={
        Property(name="Expression74", type=vhdl_statement_CaseStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_statement_CaseStatement", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
when75: BinaryAssociation = BinaryAssociation(
    name="when75",
    ends={
        Property(name="CaseAlternative", type=vhdl_statement_CaseStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_statement_CaseStatement76", type=CaseAlternative, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
choice77: BinaryAssociation = BinaryAssociation(
    name="choice77",
    ends={
        Property(name="Expression78", type=vhdl_statement_CaseAlternative, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_statement_CaseAlternative", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statement79: BinaryAssociation = BinaryAssociation(
    name="statement79",
    ends={
        Property(name="Statement81", type=vhdl_statement_CaseAlternative, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_statement_CaseAlternative80", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
until62: BinaryAssociation = BinaryAssociation(
    name="until62",
    ends={
        Property(name="Expression64", type=vhdl_statement_WaitStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_statement_WaitStatement63", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statement88: BinaryAssociation = BinaryAssociation(
    name="statement88",
    ends={
        Property(name="Statement90", type=vhdl_statement_IfStatementTest, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_statement_IfStatementTest89", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
time65: BinaryAssociation = BinaryAssociation(
    name="time65",
    ends={
        Property(name="Expression67", type=vhdl_statement_WaitStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_statement_WaitStatement66", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
procedure91: BinaryAssociation = BinaryAssociation(
    name="procedure91",
    ends={
        Property(name="statement_vhdl_CallReference", type=vhdl_statement_ProcedureCallStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_statement_ProcedureCallStatement", type=statement_vhdl_CallReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declaration92: BinaryAssociation = BinaryAssociation(
    name="declaration92",
    ends={
        Property(name="Declaration93", type=vhdl_statement_SimultaneousProceduralStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_statement_SimultaneousProceduralStatement", type=Declaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statement94: BinaryAssociation = BinaryAssociation(
    name="statement94",
    ends={
        Property(name="Statement96", type=vhdl_statement_SimultaneousProceduralStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_statement_SimultaneousProceduralStatement95", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
test82: BinaryAssociation = BinaryAssociation(
    name="test82",
    ends={
        Property(name="IfStatementTest", type=vhdl_statement_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_statement_IfStatement", type=IfStatementTest, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statement83: BinaryAssociation = BinaryAssociation(
    name="statement83",
    ends={
        Property(name="Statement85", type=vhdl_statement_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_statement_IfStatement84", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition86: BinaryAssociation = BinaryAssociation(
    name="condition86",
    ends={
        Property(name="Expression87", type=vhdl_statement_IfStatementTest, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_statement_IfStatementTest", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sensitivity102: BinaryAssociation = BinaryAssociation(
    name="sensitivity102",
    ends={
        Property(name="vhdl_statement_ProcessStatement103", type=statement_vhdl_MultiName, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="statement_vhdl_MultiName104", type=vhdl_statement_ProcessStatement, multiplicity=Multiplicity(1, 1))
    }
)
condition105: BinaryAssociation = BinaryAssociation(
    name="condition105",
    ends={
        Property(name="Expression106", type=vhdl_statement_AssertionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_statement_AssertionStatement", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
report107: BinaryAssociation = BinaryAssociation(
    name="report107",
    ends={
        Property(name="Expression109", type=vhdl_statement_AssertionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_statement_AssertionStatement108", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
severity110: BinaryAssociation = BinaryAssociation(
    name="severity110",
    ends={
        Property(name="Expression112", type=vhdl_statement_AssertionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_statement_AssertionStatement111", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
guard113: BinaryAssociation = BinaryAssociation(
    name="guard113",
    ends={
        Property(name="Expression114", type=vhdl_statement_BlockStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_statement_BlockStatement", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
generic115: BinaryAssociation = BinaryAssociation(
    name="generic115",
    ends={
        Property(name="statement_vhdl_Generics", type=vhdl_statement_BlockStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_statement_BlockStatement116", type=statement_vhdl_Generics, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
genericMap117: BinaryAssociation = BinaryAssociation(
    name="genericMap117",
    ends={
        Property(name="statement_vhdl_GenericMaps", type=vhdl_statement_BlockStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_statement_BlockStatement118", type=statement_vhdl_GenericMaps, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
port119: BinaryAssociation = BinaryAssociation(
    name="port119",
    ends={
        Property(name="statement_vhdl_Ports", type=vhdl_statement_BlockStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_statement_BlockStatement120", type=statement_vhdl_Ports, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declaration97: BinaryAssociation = BinaryAssociation(
    name="declaration97",
    ends={
        Property(name="Declaration98", type=vhdl_statement_ProcessStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_statement_ProcessStatement", type=Declaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
portMap121: BinaryAssociation = BinaryAssociation(
    name="portMap121",
    ends={
        Property(name="statement_vhdl_PortMaps", type=vhdl_statement_BlockStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_statement_BlockStatement122", type=statement_vhdl_PortMaps, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statement99: BinaryAssociation = BinaryAssociation(
    name="statement99",
    ends={
        Property(name="Statement101", type=vhdl_statement_ProcessStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_statement_ProcessStatement100", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statement126: BinaryAssociation = BinaryAssociation(
    name="statement126",
    ends={
        Property(name="vhdl_statement_BlockStatement127", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="Statement128", type=vhdl_statement_BlockStatement, multiplicity=Multiplicity(1, 1))
    }
)
break129: BinaryAssociation = BinaryAssociation(
    name="break129",
    ends={
        Property(name="BreakStatementItem", type=vhdl_statement_BreakStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_statement_BreakStatement", type=BreakStatementItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
when130: BinaryAssociation = BinaryAssociation(
    name="when130",
    ends={
        Property(name="Expression132", type=vhdl_statement_BreakStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_statement_BreakStatement131", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sensitivity133: BinaryAssociation = BinaryAssociation(
    name="sensitivity133",
    ends={
        Property(name="statement_vhdl_MultiName135", type=vhdl_statement_BreakStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_statement_BreakStatement134", type=statement_vhdl_MultiName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name136: BinaryAssociation = BinaryAssociation(
    name="name136",
    ends={
        Property(name="statement_vhdl_Name", type=vhdl_statement_BreakStatementItem, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_statement_BreakStatementItem", type=statement_vhdl_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
use137: BinaryAssociation = BinaryAssociation(
    name="use137",
    ends={
        Property(name="statement_vhdl_Name139", type=vhdl_statement_BreakStatementItem, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_statement_BreakStatementItem138", type=statement_vhdl_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arrow140: BinaryAssociation = BinaryAssociation(
    name="arrow140",
    ends={
        Property(name="Expression142", type=vhdl_statement_BreakStatementItem, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_statement_BreakStatementItem141", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name143: BinaryAssociation = BinaryAssociation(
    name="name143",
    ends={
        Property(name="statement_vhdl_ComponentReference", type=vhdl_statement_ComponentInstantiationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_statement_ComponentInstantiationStatement", type=statement_vhdl_ComponentReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declaration123: BinaryAssociation = BinaryAssociation(
    name="declaration123",
    ends={
        Property(name="Declaration125", type=vhdl_statement_BlockStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_statement_BlockStatement124", type=Declaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
genericMap144: BinaryAssociation = BinaryAssociation(
    name="genericMap144",
    ends={
        Property(name="statement_vhdl_GenericMaps145", type=vhdl_statement_InstantiationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_statement_InstantiationStatement", type=statement_vhdl_GenericMaps, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
portMap146: BinaryAssociation = BinaryAssociation(
    name="portMap146",
    ends={
        Property(name="statement_vhdl_PortMaps148", type=vhdl_statement_InstantiationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_statement_InstantiationStatement147", type=statement_vhdl_PortMaps, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name149: BinaryAssociation = BinaryAssociation(
    name="name149",
    ends={
        Property(name="statement_vhdl_EntityReference", type=vhdl_statement_EntityInstantiationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_statement_EntityInstantiationStatement", type=statement_vhdl_EntityReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name150: BinaryAssociation = BinaryAssociation(
    name="name150",
    ends={
        Property(name="ConfigurationReference", type=vhdl_statement_ConfigurationInstantiationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_statement_ConfigurationInstantiationStatement", type=ConfigurationReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left151: BinaryAssociation = BinaryAssociation(
    name="left151",
    ends={
        Property(name="Expression152", type=vhdl_statement_SimpleSimultaneousStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_statement_SimpleSimultaneousStatement", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right153: BinaryAssociation = BinaryAssociation(
    name="right153",
    ends={
        Property(name="Expression155", type=vhdl_statement_SimpleSimultaneousStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_statement_SimpleSimultaneousStatement154", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tolerance156: BinaryAssociation = BinaryAssociation(
    name="tolerance156",
    ends={
        Property(name="Expression158", type=vhdl_statement_SimpleSimultaneousStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_statement_SimpleSimultaneousStatement157", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
when159: BinaryAssociation = BinaryAssociation(
    name="when159",
    ends={
        Property(name="Expression160", type=vhdl_statement_ExitStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_statement_ExitStatement", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
scheme161: BinaryAssociation = BinaryAssociation(
    name="scheme161",
    ends={
        Property(name="GenerationScheme", type=vhdl_statement_GenerateStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_statement_GenerateStatement", type=GenerationScheme, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declaration162: BinaryAssociation = BinaryAssociation(
    name="declaration162",
    ends={
        Property(name="Declaration164", type=vhdl_statement_GenerateStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_statement_GenerateStatement163", type=Declaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statement165: BinaryAssociation = BinaryAssociation(
    name="statement165",
    ends={
        Property(name="Statement167", type=vhdl_statement_GenerateStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_statement_GenerateStatement166", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
iteration168: BinaryAssociation = BinaryAssociation(
    name="iteration168",
    ends={
        Property(name="IterationScheme", type=vhdl_statement_LoopStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_statement_LoopStatement", type=IterationScheme, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statement169: BinaryAssociation = BinaryAssociation(
    name="statement169",
    ends={
        Property(name="Statement171", type=vhdl_statement_LoopStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_statement_LoopStatement170", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
when172: BinaryAssociation = BinaryAssociation(
    name="when172",
    ends={
        Property(name="Expression173", type=vhdl_statement_NextStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_statement_NextStatement", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition174: BinaryAssociation = BinaryAssociation(
    name="condition174",
    ends={
        Property(name="Expression175", type=vhdl_statement_WhileIterationScheme, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_statement_WhileIterationScheme", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression176: BinaryAssociation = BinaryAssociation(
    name="expression176",
    ends={
        Property(name="Expression177", type=vhdl_statement_ExpressionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_statement_ExpressionStatement", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
in178: BinaryAssociation = BinaryAssociation(
    name="in178",
    ends={
        Property(name="Expression179", type=vhdl_statement_ForGenerationScheme, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_statement_ForGenerationScheme", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
in180: BinaryAssociation = BinaryAssociation(
    name="in180",
    ends={
        Property(name="Expression181", type=vhdl_statement_ForIterationScheme, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_statement_ForIterationScheme", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition182: BinaryAssociation = BinaryAssociation(
    name="condition182",
    ends={
        Property(name="Expression183", type=vhdl_statement_IfGenerationScheme, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_statement_IfGenerationScheme", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
reject184: BinaryAssociation = BinaryAssociation(
    name="reject184",
    ends={
        Property(name="Expression185", type=vhdl_statement_RejectMechanism, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_statement_RejectMechanism", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
choice186: BinaryAssociation = BinaryAssociation(
    name="choice186",
    ends={
        Property(name="Expression187", type=vhdl_expression_AssociationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_expression_AssociationExpression", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression188: BinaryAssociation = BinaryAssociation(
    name="expression188",
    ends={
        Property(name="Expression190", type=vhdl_expression_AssociationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_expression_AssociationExpression189", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
signature191: BinaryAssociation = BinaryAssociation(
    name="signature191",
    ends={
        Property(name="expression_vhdl_Signature", type=vhdl_expression_AttributeExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_expression_AttributeExpression", type=expression_vhdl_Signature, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left192: BinaryAssociation = BinaryAssociation(
    name="left192",
    ends={
        Property(name="Expression193", type=vhdl_expression_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_expression_BinaryExpression", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constraint197: BinaryAssociation = BinaryAssociation(
    name="constraint197",
    ends={
        Property(name="Expression198", type=vhdl_expression_IndicationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_expression_IndicationExpression", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tolerance199: BinaryAssociation = BinaryAssociation(
    name="tolerance199",
    ends={
        Property(name="Expression201", type=vhdl_expression_IndicationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_expression_IndicationExpression200", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
across202: BinaryAssociation = BinaryAssociation(
    name="across202",
    ends={
        Property(name="Expression204", type=vhdl_expression_IndicationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_expression_IndicationExpression203", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
mark205: BinaryAssociation = BinaryAssociation(
    name="mark205",
    ends={
        Property(name="TypeReference206", type=vhdl_expression_SubtypeIndicationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_expression_SubtypeIndicationExpression", type=TypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right194: BinaryAssociation = BinaryAssociation(
    name="right194",
    ends={
        Property(name="Expression196", type=vhdl_expression_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_expression_BinaryExpression195", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
element208: BinaryAssociation = BinaryAssociation(
    name="element208",
    ends={
        Property(name="expression_vhdl_Name", type=vhdl_expression_NameExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_expression_NameExpression", type=expression_vhdl_Name, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mark207: BinaryAssociation = BinaryAssociation(
    name="mark207",
    ends={
        Property(name="NatureReference", type=vhdl_expression_SubnatureIndicationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_expression_SubnatureIndicationExpression", type=NatureReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression214: BinaryAssociation = BinaryAssociation(
    name="expression214",
    ends={
        Property(name="Expression215", type=vhdl_expression_SignExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_expression_SignExpression", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression216: BinaryAssociation = BinaryAssociation(
    name="expression216",
    ends={
        Property(name="Expression217", type=vhdl_expression_UnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_expression_UnaryExpression", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
signature209: BinaryAssociation = BinaryAssociation(
    name="signature209",
    ends={
        Property(name="expression_vhdl_Signature210", type=vhdl_expression_SignatureExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_expression_SignatureExpression", type=expression_vhdl_Signature, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name211: BinaryAssociation = BinaryAssociation(
    name="name211",
    ends={
        Property(name="expression_vhdl_Name213", type=vhdl_expression_SignatureExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_expression_SignatureExpression212", type=expression_vhdl_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
unit218: BinaryAssociation = BinaryAssociation(
    name="unit218",
    ends={
        Property(name="expression_vhdl_Name219", type=vhdl_expression_UnitValueExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_expression_UnitValueExpression", type=expression_vhdl_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression220: BinaryAssociation = BinaryAssociation(
    name="expression220",
    ends={
        Property(name="Expression221", type=vhdl_expression_WaveformExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_expression_WaveformExpression", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression225: BinaryAssociation = BinaryAssociation(
    name="expression225",
    ends={
        Property(name="Expression226", type=vhdl_expression_MultiExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_expression_MultiExpression", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression227: BinaryAssociation = BinaryAssociation(
    name="expression227",
    ends={
        Property(name="Expression228", type=vhdl_expression_TypeQualificationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_expression_TypeQualificationExpression", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
after222: BinaryAssociation = BinaryAssociation(
    name="after222",
    ends={
        Property(name="Expression224", type=vhdl_expression_WaveformExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_expression_WaveformExpression223", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
alias229: BinaryAssociation = BinaryAssociation(
    name="alias229",
    ends={
        Property(name="TypeReference230", type=vhdl_declaration_AliasDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_declaration_AliasDeclaration", type=TypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
is231: BinaryAssociation = BinaryAssociation(
    name="is231",
    ends={
        Property(name="declaration_vhdl_Name", type=vhdl_declaration_AliasDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_declaration_AliasDeclaration232", type=declaration_vhdl_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entity233: BinaryAssociation = BinaryAssociation(
    name="entity233",
    ends={
        Property(name="declaration_vhdl_MultiName", type=vhdl_declaration_AttributeSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_declaration_AttributeSpecification", type=declaration_vhdl_MultiName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
is234: BinaryAssociation = BinaryAssociation(
    name="is234",
    ends={
        Property(name="Expression236", type=vhdl_declaration_AttributeSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_declaration_AttributeSpecification235", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left241: BinaryAssociation = BinaryAssociation(
    name="left241",
    ends={
        Property(name="declaration_vhdl_Name243", type=vhdl_declaration_BranchQuantityDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_declaration_BranchQuantityDeclaration242", type=declaration_vhdl_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right244: BinaryAssociation = BinaryAssociation(
    name="right244",
    ends={
        Property(name="declaration_vhdl_Name246", type=vhdl_declaration_BranchQuantityDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_declaration_BranchQuantityDeclaration245", type=declaration_vhdl_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
quantity247: BinaryAssociation = BinaryAssociation(
    name="quantity247",
    ends={
        Property(name="Expression248", type=vhdl_declaration_FreeQuantityDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_declaration_FreeQuantityDeclaration", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value249: BinaryAssociation = BinaryAssociation(
    name="value249",
    ends={
        Property(name="Expression250", type=vhdl_declaration_LimitDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_declaration_LimitDeclaration", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
across237: BinaryAssociation = BinaryAssociation(
    name="across237",
    ends={
        Property(name="QuantityAspect", type=vhdl_declaration_BranchQuantityDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_declaration_BranchQuantityDeclaration", type=QuantityAspect, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
through238: BinaryAssociation = BinaryAssociation(
    name="through238",
    ends={
        Property(name="QuantityAspect240", type=vhdl_declaration_BranchQuantityDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_declaration_BranchQuantityDeclaration239", type=QuantityAspect, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameter252: BinaryAssociation = BinaryAssociation(
    name="parameter252",
    ends={
        Property(name="Declaration253", type=vhdl_declaration_SubprogramDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_declaration_SubprogramDeclaration", type=Declaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body254: BinaryAssociation = BinaryAssociation(
    name="body254",
    ends={
        Property(name="SubprogramBody", type=vhdl_declaration_SubprogramDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_declaration_SubprogramDeclaration255", type=SubprogramBody, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declaration256: BinaryAssociation = BinaryAssociation(
    name="declaration256",
    ends={
        Property(name="Declaration257", type=vhdl_declaration_SubprogramBody, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_declaration_SubprogramBody", type=Declaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statement258: BinaryAssociation = BinaryAssociation(
    name="statement258",
    ends={
        Property(name="Statement260", type=vhdl_declaration_SubprogramBody, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_declaration_SubprogramBody259", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source251: BinaryAssociation = BinaryAssociation(
    name="source251",
    ends={
        Property(name="SourceAspect", type=vhdl_declaration_SourceQuantityDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_declaration_SourceQuantityDeclaration", type=SourceAspect, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
list261: BinaryAssociation = BinaryAssociation(
    name="list261",
    ends={
        Property(name="declaration_vhdl_MultiName262", type=vhdl_declaration_ConfigurationSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_declaration_ConfigurationSpecification", type=declaration_vhdl_MultiName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
component263: BinaryAssociation = BinaryAssociation(
    name="component263",
    ends={
        Property(name="declaration_vhdl_ComponentReference", type=vhdl_declaration_ConfigurationSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_declaration_ConfigurationSpecification264", type=declaration_vhdl_ComponentReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entity265: BinaryAssociation = BinaryAssociation(
    name="entity265",
    ends={
        Property(name="declaration_vhdl_EntityReference", type=vhdl_declaration_ConfigurationSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_declaration_ConfigurationSpecification266", type=declaration_vhdl_EntityReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
configuration267: BinaryAssociation = BinaryAssociation(
    name="configuration267",
    ends={
        Property(name="ConfigurationReference269", type=vhdl_declaration_ConfigurationSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_declaration_ConfigurationSpecification268", type=ConfigurationReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
genericMap270: BinaryAssociation = BinaryAssociation(
    name="genericMap270",
    ends={
        Property(name="declaration_vhdl_GenericMaps", type=vhdl_declaration_ConfigurationSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_declaration_ConfigurationSpecification271", type=declaration_vhdl_GenericMaps, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
portMap272: BinaryAssociation = BinaryAssociation(
    name="portMap272",
    ends={
        Property(name="declaration_vhdl_PortMaps", type=vhdl_declaration_ConfigurationSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_declaration_ConfigurationSpecification273", type=declaration_vhdl_PortMaps, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
disconnect274: BinaryAssociation = BinaryAssociation(
    name="disconnect274",
    ends={
        Property(name="declaration_vhdl_MultiName275", type=vhdl_declaration_DisconnectionSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_declaration_DisconnectionSpecification", type=declaration_vhdl_MultiName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
after276: BinaryAssociation = BinaryAssociation(
    name="after276",
    ends={
        Property(name="Expression278", type=vhdl_declaration_DisconnectionSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_declaration_DisconnectionSpecification277", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
open279: BinaryAssociation = BinaryAssociation(
    name="open279",
    ends={
        Property(name="Expression280", type=vhdl_declaration_FileDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_declaration_FileDeclaration", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
is281: BinaryAssociation = BinaryAssociation(
    name="is281",
    ends={
        Property(name="Expression283", type=vhdl_declaration_FileDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_declaration_FileDeclaration282", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
is284: BinaryAssociation = BinaryAssociation(
    name="is284",
    ends={
        Property(name="TypeDefinition", type=vhdl_declaration_TypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_declaration_TypeDeclaration", type=TypeDefinition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
is285: BinaryAssociation = BinaryAssociation(
    name="is285",
    ends={
        Property(name="declaration_vhdl_Name286", type=vhdl_declaration_GroupDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_declaration_GroupDeclaration", type=declaration_vhdl_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
is290: BinaryAssociation = BinaryAssociation(
    name="is290",
    ends={
        Property(name="NatureDefinition", type=vhdl_declaration_NatureDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_declaration_NatureDeclaration", type=NatureDefinition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
use291: BinaryAssociation = BinaryAssociation(
    name="use291",
    ends={
        Property(name="declaration_vhdl_MultiName292", type=vhdl_declaration_UseClauseDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_declaration_UseClauseDeclaration", type=declaration_vhdl_MultiName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initial293: BinaryAssociation = BinaryAssociation(
    name="initial293",
    ends={
        Property(name="Expression294", type=vhdl_declaration_ValueDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_declaration_ValueDeclaration", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
member287: BinaryAssociation = BinaryAssociation(
    name="member287",
    ends={
        Property(name="declaration_vhdl_MultiName289", type=vhdl_declaration_GroupDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_declaration_GroupDeclaration288", type=declaration_vhdl_MultiName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declaration295: BinaryAssociation = BinaryAssociation(
    name="declaration295",
    ends={
        Property(name="RecordTypeElement", type=vhdl_type_RecordTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_type_RecordTypeDefinition", type=RecordTypeElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
constraint296: BinaryAssociation = BinaryAssociation(
    name="constraint296",
    ends={
        Property(name="Expression297", type=vhdl_type_ConstrainedArrayTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_type_ConstrainedArrayTypeDefinition", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
index298: BinaryAssociation = BinaryAssociation(
    name="index298",
    ends={
        Property(name="TypeReference299", type=vhdl_type_UnconstrainedArrayTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_type_UnconstrainedArrayTypeDefinition", type=TypeReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
literal300: BinaryAssociation = BinaryAssociation(
    name="literal300",
    ends={
        Property(name="EnumerationLiteral", type=vhdl_type_EnumerationTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_type_EnumerationTypeDefinition", type=EnumerationLiteral, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
range301: BinaryAssociation = BinaryAssociation(
    name="range301",
    ends={
        Property(name="Expression302", type=vhdl_type_PhysicalTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_type_PhysicalTypeDefinition", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
of305: BinaryAssociation = BinaryAssociation(
    name="of305",
    ends={
        Property(name="type_vhdl_Name", type=vhdl_type_PhysicalTypeDefinitionSecondary, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_type_PhysicalTypeDefinitionSecondary", type=type_vhdl_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left306: BinaryAssociation = BinaryAssociation(
    name="left306",
    ends={
        Property(name="Expression307", type=vhdl_type_RangeTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_type_RangeTypeDefinition", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right308: BinaryAssociation = BinaryAssociation(
    name="right308",
    ends={
        Property(name="Expression310", type=vhdl_type_RangeTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_type_RangeTypeDefinition309", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type311: BinaryAssociation = BinaryAssociation(
    name="type311",
    ends={
        Property(name="TypeReference312", type=vhdl_type_Typed, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_type_Typed", type=TypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constraint313: BinaryAssociation = BinaryAssociation(
    name="constraint313",
    ends={
        Property(name="Expression314", type=vhdl_nature_ConstrainedArrayNatureDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_nature_ConstrainedArrayNatureDefinition", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
record315: BinaryAssociation = BinaryAssociation(
    name="record315",
    ends={
        Property(name="RecordNatureElement", type=vhdl_nature_RecordNatureDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_nature_RecordNatureDefinition", type=RecordNatureElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
secondary303: BinaryAssociation = BinaryAssociation(
    name="secondary303",
    ends={
        Property(name="PhysicalTypeDefinitionSecondary", type=vhdl_type_PhysicalTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_type_PhysicalTypeDefinition304", type=PhysicalTypeDefinitionSecondary, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
across317: BinaryAssociation = BinaryAssociation(
    name="across317",
    ends={
        Property(name="nature_vhdl_Name319", type=vhdl_nature_ScalarNatureDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_nature_ScalarNatureDefinition318", type=nature_vhdl_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
through320: BinaryAssociation = BinaryAssociation(
    name="through320",
    ends={
        Property(name="nature_vhdl_Name322", type=vhdl_nature_ScalarNatureDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_nature_ScalarNatureDefinition321", type=nature_vhdl_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
index323: BinaryAssociation = BinaryAssociation(
    name="index323",
    ends={
        Property(name="TypeReference324", type=vhdl_nature_UnconstrainedArrayNatureDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_nature_UnconstrainedArrayNatureDefinition", type=TypeReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nature325: BinaryAssociation = BinaryAssociation(
    name="nature325",
    ends={
        Property(name="NatureReference326", type=vhdl_nature_Natured, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_nature_Natured", type=NatureReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tolerance327: BinaryAssociation = BinaryAssociation(
    name="tolerance327",
    ends={
        Property(name="Expression328", type=vhdl_ams_QuantityAspect, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_ams_QuantityAspect", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression329: BinaryAssociation = BinaryAssociation(
    name="expression329",
    ends={
        Property(name="Expression331", type=vhdl_ams_QuantityAspect, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_ams_QuantityAspect330", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left332: BinaryAssociation = BinaryAssociation(
    name="left332",
    ends={
        Property(name="Expression333", type=vhdl_ams_Spectrum, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_ams_Spectrum", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right334: BinaryAssociation = BinaryAssociation(
    name="right334",
    ends={
        Property(name="Expression336", type=vhdl_ams_Spectrum, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_ams_Spectrum335", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
noise337: BinaryAssociation = BinaryAssociation(
    name="noise337",
    ends={
        Property(name="Expression338", type=vhdl_ams_Noise, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_ams_Noise", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name316: BinaryAssociation = BinaryAssociation(
    name="name316",
    ends={
        Property(name="nature_vhdl_Name", type=vhdl_nature_ScalarNatureDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_nature_ScalarNatureDefinition", type=nature_vhdl_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
use339: BinaryAssociation = BinaryAssociation(
    name="use339",
    ends={
        Property(name="configuration_vhdl_Name", type=vhdl_configuration_BlockConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_configuration_BlockConfiguration", type=configuration_vhdl_Name, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
item340: BinaryAssociation = BinaryAssociation(
    name="item340",
    ends={
        Property(name="ConfigurationItem", type=vhdl_configuration_BlockConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_configuration_BlockConfiguration341", type=ConfigurationItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
list342: BinaryAssociation = BinaryAssociation(
    name="list342",
    ends={
        Property(name="configuration_vhdl_MultiName", type=vhdl_configuration_ComponentConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_configuration_ComponentConfiguration", type=configuration_vhdl_MultiName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
component343: BinaryAssociation = BinaryAssociation(
    name="component343",
    ends={
        Property(name="configuration_vhdl_Name345", type=vhdl_configuration_ComponentConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_configuration_ComponentConfiguration344", type=configuration_vhdl_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entity346: BinaryAssociation = BinaryAssociation(
    name="entity346",
    ends={
        Property(name="configuration_vhdl_Name348", type=vhdl_configuration_ComponentConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_configuration_ComponentConfiguration347", type=configuration_vhdl_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
configuration349: BinaryAssociation = BinaryAssociation(
    name="configuration349",
    ends={
        Property(name="configuration_vhdl_Name351", type=vhdl_configuration_ComponentConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_configuration_ComponentConfiguration350", type=configuration_vhdl_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
genericMap352: BinaryAssociation = BinaryAssociation(
    name="genericMap352",
    ends={
        Property(name="configuration_vhdl_GenericMaps", type=vhdl_configuration_ComponentConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_configuration_ComponentConfiguration353", type=configuration_vhdl_GenericMaps, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
portMap354: BinaryAssociation = BinaryAssociation(
    name="portMap354",
    ends={
        Property(name="configuration_vhdl_PortMaps", type=vhdl_configuration_ComponentConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_configuration_ComponentConfiguration355", type=configuration_vhdl_PortMaps, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block356: BinaryAssociation = BinaryAssociation(
    name="block356",
    ends={
        Property(name="BlockConfiguration", type=vhdl_configuration_ComponentConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_configuration_ComponentConfiguration357", type=BlockConfiguration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
of358: BinaryAssociation = BinaryAssociation(
    name="of358",
    ends={
        Property(name="configuration_vhdl_EntityReference", type=vhdl_configuration_Configuration, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_configuration_Configuration", type=configuration_vhdl_EntityReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
configuration362: BinaryAssociation = BinaryAssociation(
    name="configuration362",
    ends={
        Property(name="Configuration", type=vhdl_configuration_ConfigurationResolvedReference, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_configuration_ConfigurationResolvedReference", type=Configuration, multiplicity=Multiplicity(0, 1))
    }
)
block359: BinaryAssociation = BinaryAssociation(
    name="block359",
    ends={
        Property(name="BlockConfiguration361", type=vhdl_configuration_Configuration, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_configuration_Configuration360", type=BlockConfiguration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_vhdl_Architecture_Module = Generalization(general=Module, specific=vhdl_Architecture)
gen_vhdl_Architecture_Named = Generalization(general=Named, specific=vhdl_Architecture)
gen_vhdl_Component_declaration_Declaration = Generalization(general=declaration_Declaration, specific=vhdl_Component)
gen_vhdl_Component_Named = Generalization(general=Named, specific=vhdl_Component)
gen_vhdl_DesignUnit_VhdlObject = Generalization(general=VhdlObject, specific=vhdl_DesignUnit)
gen_vhdl_Module_VhdlObject = Generalization(general=VhdlObject, specific=vhdl_Module)
gen_vhdl_Entity_Module = Generalization(general=Module, specific=vhdl_Entity)
gen_vhdl_Entity_Named = Generalization(general=Named, specific=vhdl_Entity)
gen_vhdl_Generics_VhdlObject = Generalization(general=VhdlObject, specific=vhdl_Generics)
gen_vhdl_Model_VhdlObject = Generalization(general=VhdlObject, specific=vhdl_Model)
gen_vhdl_Package_Module = Generalization(general=Module, specific=vhdl_Package)
gen_vhdl_Package_Named = Generalization(general=Named, specific=vhdl_Package)
gen_vhdl_PackageBody_Module = Generalization(general=Module, specific=vhdl_PackageBody)
gen_vhdl_GenericMaps_VhdlObject = Generalization(general=VhdlObject, specific=vhdl_GenericMaps)
gen_vhdl_PortMaps_VhdlObject = Generalization(general=VhdlObject, specific=vhdl_PortMaps)
gen_vhdl_Signature_VhdlObject = Generalization(general=VhdlObject, specific=vhdl_Signature)
gen_vhdl_Name_MultiName = Generalization(general=MultiName, specific=vhdl_Name)
gen_vhdl_Name_type_TypeReference = Generalization(general=type_TypeReference, specific=vhdl_Name)
gen_vhdl_Name_nature_NatureReference = Generalization(general=nature_NatureReference, specific=vhdl_Name)
gen_vhdl_Name_EntityReference = Generalization(general=EntityReference, specific=vhdl_Name)
gen_vhdl_Name_PackageReference = Generalization(general=PackageReference, specific=vhdl_Name)
gen_vhdl_Name_ComponentReference = Generalization(general=ComponentReference, specific=vhdl_Name)
gen_vhdl_Name_configuration_ConfigurationReference = Generalization(general=configuration_ConfigurationReference, specific=vhdl_Name)
gen_vhdl_Name_CallReference = Generalization(general=CallReference, specific=vhdl_Name)
gen_vhdl_NameList_VhdlObject = Generalization(general=VhdlObject, specific=vhdl_NameList)
gen_vhdl_NameList_MultiName = Generalization(general=MultiName, specific=vhdl_NameList)
gen_vhdl_EntityResolvedReference_VhdlObject = Generalization(general=VhdlObject, specific=vhdl_EntityResolvedReference)
gen_vhdl_EntityResolvedReference_EntityReference = Generalization(general=EntityReference, specific=vhdl_EntityResolvedReference)
gen_vhdl_PackageResolvedReference_VhdlObject = Generalization(general=VhdlObject, specific=vhdl_PackageResolvedReference)
gen_vhdl_PackageResolvedReference_PackageReference = Generalization(general=PackageReference, specific=vhdl_PackageResolvedReference)
gen_vhdl_Ports_VhdlObject = Generalization(general=VhdlObject, specific=vhdl_Ports)
gen_vhdl_CallResolvedReference_CallReference = Generalization(general=CallReference, specific=vhdl_CallResolvedReference)
gen_vhdl_statement_ReportStatement_Statement = Generalization(general=Statement, specific=vhdl_statement_ReportStatement)
gen_vhdl_statement_ReturnStatement_ExpressionStatement = Generalization(general=ExpressionStatement, specific=vhdl_statement_ReturnStatement)
gen_vhdl_statement_ConditionalSignalAssignmentStatement_SignalAssignmentStatement = Generalization(general=SignalAssignmentStatement, specific=vhdl_statement_ConditionalSignalAssignmentStatement)
gen_vhdl_statement_SelectedSignalAssignmentStatement_ConditionalSignalAssignmentStatement = Generalization(general=ConditionalSignalAssignmentStatement, specific=vhdl_statement_SelectedSignalAssignmentStatement)
gen_vhdl_statement_SequentialSignalAssignmentStatement_SignalAssignmentStatement = Generalization(general=SignalAssignmentStatement, specific=vhdl_statement_SequentialSignalAssignmentStatement)
gen_vhdl_statement_SignalAssignmentStatement_Statement = Generalization(general=Statement, specific=vhdl_statement_SignalAssignmentStatement)
gen_vhdl_statement_WaitStatement_Statement = Generalization(general=Statement, specific=vhdl_statement_WaitStatement)
gen_vhdl_ComponentResolvedReference_VhdlObject = Generalization(general=VhdlObject, specific=vhdl_ComponentResolvedReference)
gen_vhdl_ComponentResolvedReference_ComponentReference = Generalization(general=ComponentReference, specific=vhdl_ComponentResolvedReference)
gen_vhdl_statement_VariableAssignmentStatement_Statement = Generalization(general=Statement, specific=vhdl_statement_VariableAssignmentStatement)
gen_vhdl_statement_SimultaneousCaseStatement_CaseStatement = Generalization(general=CaseStatement, specific=vhdl_statement_SimultaneousCaseStatement)
gen_vhdl_statement_CaseStatement_Statement = Generalization(general=Statement, specific=vhdl_statement_CaseStatement)
gen_vhdl_statement_CaseAlternative_VhdlObject = Generalization(general=VhdlObject, specific=vhdl_statement_CaseAlternative)
gen_vhdl_statement_SimultaneousIfStatement_IfStatement = Generalization(general=IfStatement, specific=vhdl_statement_SimultaneousIfStatement)
gen_vhdl_statement_IfStatement_Statement = Generalization(general=Statement, specific=vhdl_statement_IfStatement)
gen_vhdl_statement_ProcedureCallStatement_Statement = Generalization(general=Statement, specific=vhdl_statement_ProcedureCallStatement)
gen_vhdl_statement_SimultaneousProceduralStatement_Statement = Generalization(general=Statement, specific=vhdl_statement_SimultaneousProceduralStatement)
gen_vhdl_statement_ProcessStatement_Statement = Generalization(general=Statement, specific=vhdl_statement_ProcessStatement)
gen_vhdl_statement_IfStatementTest_VhdlObject = Generalization(general=VhdlObject, specific=vhdl_statement_IfStatementTest)
gen_vhdl_statement_AssertionStatement_Statement = Generalization(general=Statement, specific=vhdl_statement_AssertionStatement)
gen_vhdl_statement_BlockStatement_Statement = Generalization(general=Statement, specific=vhdl_statement_BlockStatement)
gen_vhdl_statement_BreakStatement_Statement = Generalization(general=Statement, specific=vhdl_statement_BreakStatement)
gen_vhdl_statement_BreakStatementItem_VhdlObject = Generalization(general=VhdlObject, specific=vhdl_statement_BreakStatementItem)
gen_vhdl_statement_ComponentInstantiationStatement_InstantiationStatement = Generalization(general=InstantiationStatement, specific=vhdl_statement_ComponentInstantiationStatement)
gen_vhdl_statement_EntityInstantiationStatement_InstantiationStatement = Generalization(general=InstantiationStatement, specific=vhdl_statement_EntityInstantiationStatement)
gen_vhdl_statement_ConfigurationInstantiationStatement_InstantiationStatement = Generalization(general=InstantiationStatement, specific=vhdl_statement_ConfigurationInstantiationStatement)
gen_vhdl_statement_SimpleSimultaneousStatement_Statement = Generalization(general=Statement, specific=vhdl_statement_SimpleSimultaneousStatement)
gen_vhdl_statement_InstantiationStatement_Statement = Generalization(general=Statement, specific=vhdl_statement_InstantiationStatement)
gen_vhdl_statement_GenerateStatement_Statement = Generalization(general=Statement, specific=vhdl_statement_GenerateStatement)
gen_vhdl_statement_LoopStatement_Statement = Generalization(general=Statement, specific=vhdl_statement_LoopStatement)
gen_vhdl_statement_ExitStatement_Statement = Generalization(general=Statement, specific=vhdl_statement_ExitStatement)
gen_vhdl_statement_Statement_VhdlObject = Generalization(general=VhdlObject, specific=vhdl_statement_Statement)
gen_vhdl_statement_IterationScheme_VhdlObject = Generalization(general=VhdlObject, specific=vhdl_statement_IterationScheme)
gen_vhdl_statement_WhileIterationScheme_IterationScheme = Generalization(general=IterationScheme, specific=vhdl_statement_WhileIterationScheme)
gen_vhdl_statement_DelayMechanism_VhdlObject = Generalization(general=VhdlObject, specific=vhdl_statement_DelayMechanism)
gen_vhdl_statement_ExpressionStatement_Statement = Generalization(general=Statement, specific=vhdl_statement_ExpressionStatement)
gen_vhdl_statement_ForGenerationScheme_GenerationScheme = Generalization(general=GenerationScheme, specific=vhdl_statement_ForGenerationScheme)
gen_vhdl_statement_NextStatement_Statement = Generalization(general=Statement, specific=vhdl_statement_NextStatement)
gen_vhdl_statement_GenerationScheme_VhdlObject = Generalization(general=VhdlObject, specific=vhdl_statement_GenerationScheme)
gen_vhdl_statement_IfGenerationScheme_GenerationScheme = Generalization(general=GenerationScheme, specific=vhdl_statement_IfGenerationScheme)
gen_vhdl_statement_RejectMechanism_DelayMechanism = Generalization(general=DelayMechanism, specific=vhdl_statement_RejectMechanism)
gen_vhdl_statement_TransportMechanism_DelayMechanism = Generalization(general=DelayMechanism, specific=vhdl_statement_TransportMechanism)
gen_vhdl_expression_AddingExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=vhdl_expression_AddingExpression)
gen_vhdl_expression_AggregateExpression_expression_MultiExpression = Generalization(general=expression_MultiExpression, specific=vhdl_expression_AggregateExpression)
gen_vhdl_expression_AggregateExpression_Name = Generalization(general=Name, specific=vhdl_expression_AggregateExpression)
gen_vhdl_statement_ForIterationScheme_IterationScheme = Generalization(general=IterationScheme, specific=vhdl_statement_ForIterationScheme)
gen_vhdl_expression_AttributeExpression_expression_ValueExpression = Generalization(general=expression_ValueExpression, specific=vhdl_expression_AttributeExpression)
gen_vhdl_expression_AttributeExpression_Name = Generalization(general=Name, specific=vhdl_expression_AttributeExpression)
gen_vhdl_expression_BinaryExpression_Expression = Generalization(general=Expression, specific=vhdl_expression_BinaryExpression)
gen_vhdl_expression_AllExpression_expression_Expression = Generalization(general=expression_Expression, specific=vhdl_expression_AllExpression)
gen_vhdl_expression_AllExpression_Name = Generalization(general=Name, specific=vhdl_expression_AllExpression)
gen_vhdl_expression_AllocatorExpression_expression_Expression = Generalization(general=expression_Expression, specific=vhdl_expression_AllocatorExpression)
gen_vhdl_expression_AllocatorExpression_type_Typed = Generalization(general=type_Typed, specific=vhdl_expression_AllocatorExpression)
gen_vhdl_expression_AssociationExpression_Expression = Generalization(general=Expression, specific=vhdl_expression_AssociationExpression)
gen_vhdl_expression_Expression_VhdlObject = Generalization(general=VhdlObject, specific=vhdl_expression_Expression)
gen_vhdl_expression_IndicationExpression_Expression = Generalization(general=Expression, specific=vhdl_expression_IndicationExpression)
gen_vhdl_expression_SubtypeIndicationExpression_expression_IndicationExpression = Generalization(general=expression_IndicationExpression, specific=vhdl_expression_SubtypeIndicationExpression)
gen_vhdl_expression_SubtypeIndicationExpression_type_TypeReference = Generalization(general=type_TypeReference, specific=vhdl_expression_SubtypeIndicationExpression)
gen_vhdl_expression_SubtypeIndicationExpression_Named = Generalization(general=Named, specific=vhdl_expression_SubtypeIndicationExpression)
gen_vhdl_expression_BitStringExpression_ValueExpression = Generalization(general=ValueExpression, specific=vhdl_expression_BitStringExpression)
gen_vhdl_expression_NameExpression_expression_Expression = Generalization(general=expression_Expression, specific=vhdl_expression_NameExpression)
gen_vhdl_expression_NameExpression_Name = Generalization(general=Name, specific=vhdl_expression_NameExpression)
gen_vhdl_expression_NullExpression_Expression = Generalization(general=Expression, specific=vhdl_expression_NullExpression)
gen_vhdl_expression_MultiplyingExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=vhdl_expression_MultiplyingExpression)
gen_vhdl_expression_PowerExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=vhdl_expression_PowerExpression)
gen_vhdl_expression_RelationalExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=vhdl_expression_RelationalExpression)
gen_vhdl_expression_ShiftExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=vhdl_expression_ShiftExpression)
gen_vhdl_expression_SignatureExpression_expression_Expression = Generalization(general=expression_Expression, specific=vhdl_expression_SignatureExpression)
gen_vhdl_expression_SignatureExpression_Name = Generalization(general=Name, specific=vhdl_expression_SignatureExpression)
gen_vhdl_expression_SubnatureIndicationExpression_expression_IndicationExpression = Generalization(general=expression_IndicationExpression, specific=vhdl_expression_SubnatureIndicationExpression)
gen_vhdl_expression_SubnatureIndicationExpression_nature_NatureReference = Generalization(general=nature_NatureReference, specific=vhdl_expression_SubnatureIndicationExpression)
gen_vhdl_expression_LogicalExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=vhdl_expression_LogicalExpression)
gen_vhdl_expression_UnaryExpression_Expression = Generalization(general=Expression, specific=vhdl_expression_UnaryExpression)
gen_vhdl_expression_OpenExpression_Expression = Generalization(general=Expression, specific=vhdl_expression_OpenExpression)
gen_vhdl_expression_OthersExpression_expression_Expression = Generalization(general=expression_Expression, specific=vhdl_expression_OthersExpression)
gen_vhdl_expression_OthersExpression_Name = Generalization(general=Name, specific=vhdl_expression_OthersExpression)
gen_vhdl_expression_SignExpression_Expression = Generalization(general=Expression, specific=vhdl_expression_SignExpression)
gen_vhdl_expression_CharacterExpression_expression_ValueExpression = Generalization(general=expression_ValueExpression, specific=vhdl_expression_CharacterExpression)
gen_vhdl_expression_CharacterExpression_Name = Generalization(general=Name, specific=vhdl_expression_CharacterExpression)
gen_vhdl_expression_CharacterExpression_type_EnumerationLiteral = Generalization(general=type_EnumerationLiteral, specific=vhdl_expression_CharacterExpression)
gen_vhdl_expression_IdentifierExpression_expression_ValueExpression = Generalization(general=expression_ValueExpression, specific=vhdl_expression_IdentifierExpression)
gen_vhdl_expression_IdentifierExpression_Name = Generalization(general=Name, specific=vhdl_expression_IdentifierExpression)
gen_vhdl_expression_IdentifierExpression_type_EnumerationLiteral = Generalization(general=type_EnumerationLiteral, specific=vhdl_expression_IdentifierExpression)
gen_vhdl_expression_UnitValueExpression_ValueExpression = Generalization(general=ValueExpression, specific=vhdl_expression_UnitValueExpression)
gen_vhdl_expression_UnaffectedExpression_Expression = Generalization(general=Expression, specific=vhdl_expression_UnaffectedExpression)
gen_vhdl_expression_ValueExpression_Expression = Generalization(general=Expression, specific=vhdl_expression_ValueExpression)
gen_vhdl_expression_WaveformExpression_Expression = Generalization(general=Expression, specific=vhdl_expression_WaveformExpression)
gen_vhdl_expression_RangeExpression_expression_BinaryExpression = Generalization(general=expression_BinaryExpression, specific=vhdl_expression_RangeExpression)
gen_vhdl_expression_RangeExpression_Name = Generalization(general=Name, specific=vhdl_expression_RangeExpression)
gen_vhdl_expression_StringExpression_expression_ValueExpression = Generalization(general=expression_ValueExpression, specific=vhdl_expression_StringExpression)
gen_vhdl_expression_StringExpression_Name = Generalization(general=Name, specific=vhdl_expression_StringExpression)
gen_vhdl_expression_MultiExpression_Expression = Generalization(general=Expression, specific=vhdl_expression_MultiExpression)
gen_vhdl_expression_ConditionalWaveformExpression_AssociationExpression = Generalization(general=AssociationExpression, specific=vhdl_expression_ConditionalWaveformExpression)
gen_vhdl_expression_TypeQualificationExpression_expression_Expression = Generalization(general=expression_Expression, specific=vhdl_expression_TypeQualificationExpression)
gen_vhdl_expression_TypeQualificationExpression_Name = Generalization(general=Name, specific=vhdl_expression_TypeQualificationExpression)
gen_vhdl_declaration_AliasDeclaration_declaration_Declaration = Generalization(general=declaration_Declaration, specific=vhdl_declaration_AliasDeclaration)
gen_vhdl_declaration_AliasDeclaration_Named = Generalization(general=Named, specific=vhdl_declaration_AliasDeclaration)
gen_vhdl_declaration_AttributeDeclaration_declaration_Declaration = Generalization(general=declaration_Declaration, specific=vhdl_declaration_AttributeDeclaration)
gen_vhdl_declaration_AttributeDeclaration_Named = Generalization(general=Named, specific=vhdl_declaration_AttributeDeclaration)
gen_vhdl_declaration_AttributeDeclaration_type_Typed = Generalization(general=type_Typed, specific=vhdl_declaration_AttributeDeclaration)
gen_vhdl_declaration_AttributeSpecification_declaration_Declaration = Generalization(general=declaration_Declaration, specific=vhdl_declaration_AttributeSpecification)
gen_vhdl_declaration_AttributeSpecification_Named = Generalization(general=Named, specific=vhdl_declaration_AttributeSpecification)
gen_vhdl_declaration_BranchQuantityDeclaration_QuantityDeclaration = Generalization(general=QuantityDeclaration, specific=vhdl_declaration_BranchQuantityDeclaration)
gen_vhdl_declaration_FreeQuantityDeclaration_declaration_QuantityDeclaration = Generalization(general=declaration_QuantityDeclaration, specific=vhdl_declaration_FreeQuantityDeclaration)
gen_vhdl_declaration_FreeQuantityDeclaration_MultiNamed = Generalization(general=MultiNamed, specific=vhdl_declaration_FreeQuantityDeclaration)
gen_vhdl_declaration_FreeQuantityDeclaration_type_Typed = Generalization(general=type_Typed, specific=vhdl_declaration_FreeQuantityDeclaration)
gen_vhdl_declaration_LimitDeclaration_declaration_Declaration = Generalization(general=declaration_Declaration, specific=vhdl_declaration_LimitDeclaration)
gen_vhdl_declaration_LimitDeclaration_MultiNamed = Generalization(general=MultiNamed, specific=vhdl_declaration_LimitDeclaration)
gen_vhdl_declaration_LimitDeclaration_type_Typed = Generalization(general=type_Typed, specific=vhdl_declaration_LimitDeclaration)
gen_vhdl_declaration_QuantityDeclaration_Declaration = Generalization(general=Declaration, specific=vhdl_declaration_QuantityDeclaration)
gen_vhdl_declaration_SubnatureDeclaration_declaration_Declaration = Generalization(general=declaration_Declaration, specific=vhdl_declaration_SubnatureDeclaration)
gen_vhdl_declaration_SubnatureDeclaration_Named = Generalization(general=Named, specific=vhdl_declaration_SubnatureDeclaration)
gen_vhdl_declaration_SubnatureDeclaration_nature_Natured = Generalization(general=nature_Natured, specific=vhdl_declaration_SubnatureDeclaration)
gen_vhdl_declaration_SubprogramDeclaration_declaration_Declaration = Generalization(general=declaration_Declaration, specific=vhdl_declaration_SubprogramDeclaration)
gen_vhdl_declaration_SubprogramDeclaration_Named = Generalization(general=Named, specific=vhdl_declaration_SubprogramDeclaration)
gen_vhdl_declaration_ProcedureDeclaration_SubprogramDeclaration = Generalization(general=SubprogramDeclaration, specific=vhdl_declaration_ProcedureDeclaration)
gen_vhdl_declaration_FunctionDeclaration_declaration_SubprogramDeclaration = Generalization(general=declaration_SubprogramDeclaration, specific=vhdl_declaration_FunctionDeclaration)
gen_vhdl_declaration_FunctionDeclaration_type_Typed = Generalization(general=type_Typed, specific=vhdl_declaration_FunctionDeclaration)
gen_vhdl_declaration_SubprogramBody_VhdlObject = Generalization(general=VhdlObject, specific=vhdl_declaration_SubprogramBody)
gen_vhdl_declaration_SourceQuantityDeclaration_declaration_QuantityDeclaration = Generalization(general=declaration_QuantityDeclaration, specific=vhdl_declaration_SourceQuantityDeclaration)
gen_vhdl_declaration_SourceQuantityDeclaration_MultiNamed = Generalization(general=MultiNamed, specific=vhdl_declaration_SourceQuantityDeclaration)
gen_vhdl_declaration_SourceQuantityDeclaration_type_Typed = Generalization(general=type_Typed, specific=vhdl_declaration_SourceQuantityDeclaration)
gen_vhdl_declaration_Declaration_VhdlObject = Generalization(general=VhdlObject, specific=vhdl_declaration_Declaration)
gen_vhdl_declaration_DisconnectionSpecification_declaration_Declaration = Generalization(general=declaration_Declaration, specific=vhdl_declaration_DisconnectionSpecification)
gen_vhdl_declaration_DisconnectionSpecification_type_Typed = Generalization(general=type_Typed, specific=vhdl_declaration_DisconnectionSpecification)
gen_vhdl_declaration_FileDeclaration_declaration_Declaration = Generalization(general=declaration_Declaration, specific=vhdl_declaration_FileDeclaration)
gen_vhdl_declaration_FileDeclaration_MultiNamed = Generalization(general=MultiNamed, specific=vhdl_declaration_FileDeclaration)
gen_vhdl_declaration_FileDeclaration_type_Typed = Generalization(general=type_Typed, specific=vhdl_declaration_FileDeclaration)
gen_vhdl_declaration_TerminalDeclaration_declaration_Declaration = Generalization(general=declaration_Declaration, specific=vhdl_declaration_TerminalDeclaration)
gen_vhdl_declaration_TerminalDeclaration_MultiNamed = Generalization(general=MultiNamed, specific=vhdl_declaration_TerminalDeclaration)
gen_vhdl_declaration_TerminalDeclaration_nature_Natured = Generalization(general=nature_Natured, specific=vhdl_declaration_TerminalDeclaration)
gen_vhdl_declaration_TypeDeclaration_declaration_Declaration = Generalization(general=declaration_Declaration, specific=vhdl_declaration_TypeDeclaration)
gen_vhdl_declaration_TypeDeclaration_Named = Generalization(general=Named, specific=vhdl_declaration_TypeDeclaration)
gen_vhdl_declaration_ConstantDeclaration_ValueDeclaration = Generalization(general=ValueDeclaration, specific=vhdl_declaration_ConstantDeclaration)
gen_vhdl_declaration_GroupDeclaration_declaration_Declaration = Generalization(general=declaration_Declaration, specific=vhdl_declaration_GroupDeclaration)
gen_vhdl_declaration_GroupDeclaration_Named = Generalization(general=Named, specific=vhdl_declaration_GroupDeclaration)
gen_vhdl_declaration_SubtypeDeclaration_declaration_Declaration = Generalization(general=declaration_Declaration, specific=vhdl_declaration_SubtypeDeclaration)
gen_vhdl_declaration_SubtypeDeclaration_Named = Generalization(general=Named, specific=vhdl_declaration_SubtypeDeclaration)
gen_vhdl_declaration_SubtypeDeclaration_type_Typed = Generalization(general=type_Typed, specific=vhdl_declaration_SubtypeDeclaration)
gen_vhdl_declaration_ConfigurationSpecification_Declaration = Generalization(general=Declaration, specific=vhdl_declaration_ConfigurationSpecification)
gen_vhdl_declaration_NatureDeclaration_declaration_Declaration = Generalization(general=declaration_Declaration, specific=vhdl_declaration_NatureDeclaration)
gen_vhdl_declaration_NatureDeclaration_Named = Generalization(general=Named, specific=vhdl_declaration_NatureDeclaration)
gen_vhdl_declaration_SignalDeclaration_ValueDeclaration = Generalization(general=ValueDeclaration, specific=vhdl_declaration_SignalDeclaration)
gen_vhdl_declaration_UseClauseDeclaration_Declaration = Generalization(general=Declaration, specific=vhdl_declaration_UseClauseDeclaration)
gen_vhdl_declaration_VariableDeclaration_ValueDeclaration = Generalization(general=ValueDeclaration, specific=vhdl_declaration_VariableDeclaration)
gen_vhdl_declaration_ValueDeclaration_declaration_Declaration = Generalization(general=declaration_Declaration, specific=vhdl_declaration_ValueDeclaration)
gen_vhdl_declaration_ValueDeclaration_MultiNamed = Generalization(general=MultiNamed, specific=vhdl_declaration_ValueDeclaration)
gen_vhdl_declaration_ValueDeclaration_type_Typed = Generalization(general=type_Typed, specific=vhdl_declaration_ValueDeclaration)
gen_vhdl_declaration_GroupTemplateDeclaration_declaration_Declaration = Generalization(general=declaration_Declaration, specific=vhdl_declaration_GroupTemplateDeclaration)
gen_vhdl_declaration_GroupTemplateDeclaration_Named = Generalization(general=Named, specific=vhdl_declaration_GroupTemplateDeclaration)
gen_vhdl_type_AccessTypeDefinition_type_TypeDefinition = Generalization(general=type_TypeDefinition, specific=vhdl_type_AccessTypeDefinition)
gen_vhdl_type_AccessTypeDefinition_type_Typed = Generalization(general=type_Typed, specific=vhdl_type_AccessTypeDefinition)
gen_vhdl_type_CompositeTypeDefinition_TypeDefinition = Generalization(general=TypeDefinition, specific=vhdl_type_CompositeTypeDefinition)
gen_vhdl_type_RecordTypeDefinition_CompositeTypeDefinition = Generalization(general=CompositeTypeDefinition, specific=vhdl_type_RecordTypeDefinition)
gen_vhdl_type_ArrayTypeDefinition_type_CompositeTypeDefinition = Generalization(general=type_CompositeTypeDefinition, specific=vhdl_type_ArrayTypeDefinition)
gen_vhdl_type_ArrayTypeDefinition_type_Typed = Generalization(general=type_Typed, specific=vhdl_type_ArrayTypeDefinition)
gen_vhdl_type_ConstrainedArrayTypeDefinition_ArrayTypeDefinition = Generalization(general=ArrayTypeDefinition, specific=vhdl_type_ConstrainedArrayTypeDefinition)
gen_vhdl_type_UnconstrainedArrayTypeDefinition_ArrayTypeDefinition = Generalization(general=ArrayTypeDefinition, specific=vhdl_type_UnconstrainedArrayTypeDefinition)
gen_vhdl_type_EnumerationTypeDefinition_TypeDefinition = Generalization(general=TypeDefinition, specific=vhdl_type_EnumerationTypeDefinition)
gen_vhdl_type_FileTypeDefinition_type_TypeDefinition = Generalization(general=type_TypeDefinition, specific=vhdl_type_FileTypeDefinition)
gen_vhdl_type_FileTypeDefinition_type_Typed = Generalization(general=type_Typed, specific=vhdl_type_FileTypeDefinition)
gen_vhdl_type_PhysicalTypeDefinition_TypeDefinition = Generalization(general=TypeDefinition, specific=vhdl_type_PhysicalTypeDefinition)
gen_vhdl_type_RangeTypeDefinition_TypeDefinition = Generalization(general=TypeDefinition, specific=vhdl_type_RangeTypeDefinition)
gen_vhdl_type_RecordTypeElement_VhdlObject = Generalization(general=VhdlObject, specific=vhdl_type_RecordTypeElement)
gen_vhdl_type_RecordTypeElement_MultiNamed = Generalization(general=MultiNamed, specific=vhdl_type_RecordTypeElement)
gen_vhdl_type_RecordTypeElement_type_Typed = Generalization(general=type_Typed, specific=vhdl_type_RecordTypeElement)
gen_vhdl_type_TypeDefinition_VhdlObject = Generalization(general=VhdlObject, specific=vhdl_type_TypeDefinition)
gen_vhdl_nature_ArrayNatureDefinition_nature_CompositeNatureDefinition = Generalization(general=nature_CompositeNatureDefinition, specific=vhdl_nature_ArrayNatureDefinition)
gen_vhdl_nature_ArrayNatureDefinition_nature_Natured = Generalization(general=nature_Natured, specific=vhdl_nature_ArrayNatureDefinition)
gen_vhdl_nature_CompositeNatureDefinition_NatureDefinition = Generalization(general=NatureDefinition, specific=vhdl_nature_CompositeNatureDefinition)
gen_vhdl_nature_ConstrainedArrayNatureDefinition_ArrayNatureDefinition = Generalization(general=ArrayNatureDefinition, specific=vhdl_nature_ConstrainedArrayNatureDefinition)
gen_vhdl_nature_NatureDefinition_VhdlObject = Generalization(general=VhdlObject, specific=vhdl_nature_NatureDefinition)
gen_vhdl_nature_RecordNatureDefinition_CompositeNatureDefinition = Generalization(general=CompositeNatureDefinition, specific=vhdl_nature_RecordNatureDefinition)
gen_vhdl_nature_RecordNatureElement_VhdlObject = Generalization(general=VhdlObject, specific=vhdl_nature_RecordNatureElement)
gen_vhdl_nature_RecordNatureElement_MultiNamed = Generalization(general=MultiNamed, specific=vhdl_nature_RecordNatureElement)
gen_vhdl_nature_RecordNatureElement_nature_Natured = Generalization(general=nature_Natured, specific=vhdl_nature_RecordNatureElement)
gen_vhdl_nature_UnconstrainedArrayNatureDefinition_ArrayNatureDefinition = Generalization(general=ArrayNatureDefinition, specific=vhdl_nature_UnconstrainedArrayNatureDefinition)
gen_vhdl_ams_QuantityAspect_VhdlObject = Generalization(general=VhdlObject, specific=vhdl_ams_QuantityAspect)
gen_vhdl_ams_QuantityAspect_MultiNamed = Generalization(general=MultiNamed, specific=vhdl_ams_QuantityAspect)
gen_vhdl_ams_SourceAspect_VhdlObject = Generalization(general=VhdlObject, specific=vhdl_ams_SourceAspect)
gen_vhdl_ams_Spectrum_SourceAspect = Generalization(general=SourceAspect, specific=vhdl_ams_Spectrum)
gen_vhdl_ams_Noise_SourceAspect = Generalization(general=SourceAspect, specific=vhdl_ams_Noise)
gen_vhdl_nature_ScalarNatureDefinition_NatureDefinition = Generalization(general=NatureDefinition, specific=vhdl_nature_ScalarNatureDefinition)
gen_vhdl_configuration_BlockConfiguration_configuration_ConfigurationItem = Generalization(general=configuration_ConfigurationItem, specific=vhdl_configuration_BlockConfiguration)
gen_vhdl_configuration_BlockConfiguration_Named = Generalization(general=Named, specific=vhdl_configuration_BlockConfiguration)
gen_vhdl_configuration_ComponentConfiguration_ConfigurationItem = Generalization(general=ConfigurationItem, specific=vhdl_configuration_ComponentConfiguration)
gen_vhdl_configuration_Configuration_Module = Generalization(general=Module, specific=vhdl_configuration_Configuration)
gen_vhdl_configuration_Configuration_Named = Generalization(general=Named, specific=vhdl_configuration_Configuration)
gen_vhdl_configuration_ConfigurationResolvedReference_VhdlObject = Generalization(general=VhdlObject, specific=vhdl_configuration_ConfigurationResolvedReference)
gen_vhdl_configuration_ConfigurationResolvedReference_configuration_ConfigurationReference = Generalization(general=configuration_ConfigurationReference, specific=vhdl_configuration_ConfigurationResolvedReference)
gen_vhdl_configuration_ConfigurationItem_VhdlObject = Generalization(general=VhdlObject, specific=vhdl_configuration_ConfigurationItem)

# Domain Model
domain_model = DomainModel(
    name="vhdl",
    types={vhdl_Architecture, Module, Named, vhdl_EntityReference, Statement, vhdl_Component, declaration_Declaration, vhdl_Generics, vhdl_Ports, vhdl_DesignUnit, VhdlObject, vhdl_Name, vhdl_Module, Declaration, vhdl_Entity, vhdl_Model, vhdl_Package, vhdl_PackageBody, vhdl_PackageReference, vhdl_GenericMaps, Expression, vhdl_PortMaps, vhdl_Signature, TypeReference, vhdl_Named, vhdl_MultiNamed, vhdl_MultiName, vhdl_VhdlObject, MultiName, type_TypeReference, nature_NatureReference, EntityReference, PackageReference, ComponentReference, configuration_ConfigurationReference, CallReference, vhdl_NameList, vhdl_EntityResolvedReference, vhdl_PackageResolvedReference, vhdl_CallReference, vhdl_CallResolvedReference, SubprogramDeclaration, vhdl_statement_ReportStatement, vhdl_statement_ReturnStatement, ExpressionStatement, vhdl_statement_ConditionalSignalAssignmentStatement, SignalAssignmentStatement, vhdl_statement_SelectedSignalAssignmentStatement, ConditionalSignalAssignmentStatement, vhdl_statement_SequentialSignalAssignmentStatement, vhdl_statement_SignalAssignmentStatement, DelayMechanism, vhdl_statement_WaitStatement, statement_vhdl_MultiName, vhdl_ComponentReference, vhdl_ComponentResolvedReference, vhdl_statement_VariableAssignmentStatement, vhdl_statement_SimultaneousCaseStatement, CaseStatement, vhdl_statement_CaseStatement, CaseAlternative, vhdl_statement_CaseAlternative, vhdl_statement_SimultaneousIfStatement, IfStatement, vhdl_statement_IfStatement, IfStatementTest, vhdl_statement_ProcedureCallStatement, statement_vhdl_CallReference, vhdl_statement_SimultaneousProceduralStatement, vhdl_statement_ProcessStatement, vhdl_statement_IfStatementTest, vhdl_statement_AssertionStatement, vhdl_statement_BlockStatement, statement_vhdl_Generics, statement_vhdl_GenericMaps, statement_vhdl_Ports, statement_vhdl_PortMaps, vhdl_statement_BreakStatement, BreakStatementItem, vhdl_statement_BreakStatementItem, statement_vhdl_Name, vhdl_statement_ComponentInstantiationStatement, InstantiationStatement, statement_vhdl_ComponentReference, vhdl_statement_EntityInstantiationStatement, statement_vhdl_EntityReference, vhdl_statement_ConfigurationInstantiationStatement, ConfigurationReference, vhdl_statement_SimpleSimultaneousStatement, vhdl_statement_InstantiationStatement, vhdl_statement_GenerateStatement, GenerationScheme, vhdl_statement_LoopStatement, IterationScheme, vhdl_statement_ExitStatement, vhdl_statement_Statement, vhdl_statement_IterationScheme, vhdl_statement_WhileIterationScheme, vhdl_statement_DelayMechanism, vhdl_statement_ExpressionStatement, vhdl_statement_ForGenerationScheme, vhdl_statement_NextStatement, vhdl_statement_GenerationScheme, vhdl_statement_IfGenerationScheme, vhdl_statement_RejectMechanism, vhdl_statement_TransportMechanism, vhdl_expression_AddingExpression, BinaryExpression, vhdl_expression_AggregateExpression, expression_MultiExpression, Name, vhdl_statement_ForIterationScheme, vhdl_expression_AttributeExpression, expression_ValueExpression, expression_vhdl_Signature, vhdl_expression_BinaryExpression, vhdl_expression_AllExpression, expression_Expression, vhdl_expression_AllocatorExpression, type_Typed, vhdl_expression_AssociationExpression, vhdl_expression_IndicationExpression, vhdl_expression_SubtypeIndicationExpression, expression_IndicationExpression, vhdl_expression_SubnatureIndicationExpression, vhdl_expression_BitStringExpression, ValueExpression, vhdl_expression_Expression, vhdl_expression_NameExpression, expression_vhdl_Name, vhdl_expression_NullExpression, vhdl_expression_MultiplyingExpression, vhdl_expression_PowerExpression, vhdl_expression_RelationalExpression, vhdl_expression_ShiftExpression, vhdl_expression_SignatureExpression, NatureReference, vhdl_expression_LogicalExpression, vhdl_expression_UnaryExpression, vhdl_expression_OpenExpression, vhdl_expression_OthersExpression, vhdl_expression_RangeExpression, expression_BinaryExpression, vhdl_expression_SignExpression, vhdl_expression_CharacterExpression, type_EnumerationLiteral, vhdl_expression_IdentifierExpression, vhdl_expression_UnitValueExpression, vhdl_expression_UnaffectedExpression, vhdl_expression_ValueExpression, vhdl_expression_WaveformExpression, vhdl_expression_StringExpression, vhdl_expression_MultiExpression, vhdl_expression_ConditionalWaveformExpression, AssociationExpression, vhdl_expression_TypeQualificationExpression, vhdl_declaration_AliasDeclaration, declaration_vhdl_Name, vhdl_declaration_AttributeDeclaration, vhdl_declaration_AttributeSpecification, declaration_vhdl_MultiName, vhdl_declaration_BranchQuantityDeclaration, QuantityDeclaration, vhdl_declaration_FreeQuantityDeclaration, declaration_QuantityDeclaration, MultiNamed, vhdl_declaration_LimitDeclaration, vhdl_declaration_QuantityDeclaration, QuantityAspect, vhdl_declaration_SubnatureDeclaration, nature_Natured, vhdl_declaration_SubprogramDeclaration, SubprogramBody, vhdl_declaration_ProcedureDeclaration, vhdl_declaration_FunctionDeclaration, declaration_SubprogramDeclaration, vhdl_declaration_SubprogramBody, vhdl_declaration_SourceQuantityDeclaration, SourceAspect, declaration_vhdl_ComponentReference, declaration_vhdl_EntityReference, declaration_vhdl_GenericMaps, declaration_vhdl_PortMaps, vhdl_declaration_Declaration, vhdl_declaration_DisconnectionSpecification, vhdl_declaration_FileDeclaration, vhdl_declaration_TerminalDeclaration, vhdl_declaration_TypeDeclaration, TypeDefinition, vhdl_declaration_ConstantDeclaration, ValueDeclaration, vhdl_declaration_GroupDeclaration, vhdl_declaration_SubtypeDeclaration, vhdl_declaration_ConfigurationSpecification, vhdl_declaration_NatureDeclaration, NatureDefinition, vhdl_declaration_SignalDeclaration, vhdl_declaration_UseClauseDeclaration, vhdl_declaration_VariableDeclaration, vhdl_declaration_ValueDeclaration, vhdl_declaration_GroupTemplateDeclaration, vhdl_type_AccessTypeDefinition, type_TypeDefinition, vhdl_type_CompositeTypeDefinition, vhdl_type_RecordTypeDefinition, CompositeTypeDefinition, RecordTypeElement, vhdl_type_ArrayTypeDefinition, type_CompositeTypeDefinition, vhdl_type_ConstrainedArrayTypeDefinition, ArrayTypeDefinition, vhdl_type_UnconstrainedArrayTypeDefinition, vhdl_type_EnumerationLiteral, vhdl_type_EnumerationTypeDefinition, EnumerationLiteral, vhdl_type_FileTypeDefinition, vhdl_type_PhysicalTypeDefinition, PhysicalTypeDefinitionSecondary, type_vhdl_Name, vhdl_type_RangeTypeDefinition, vhdl_type_RecordTypeElement, vhdl_type_Typed, vhdl_type_TypeDefinition, vhdl_type_TypeReference, vhdl_nature_ArrayNatureDefinition, nature_CompositeNatureDefinition, vhdl_nature_CompositeNatureDefinition, vhdl_nature_ConstrainedArrayNatureDefinition, ArrayNatureDefinition, vhdl_nature_NatureDefinition, vhdl_nature_RecordNatureDefinition, CompositeNatureDefinition, RecordNatureElement, vhdl_nature_RecordNatureElement, vhdl_type_PhysicalTypeDefinitionSecondary, vhdl_nature_UnconstrainedArrayNatureDefinition, vhdl_nature_NatureReference, vhdl_nature_Natured, vhdl_ams_QuantityAspect, vhdl_ams_SourceAspect, vhdl_ams_Spectrum, vhdl_ams_Noise, vhdl_nature_ScalarNatureDefinition, nature_vhdl_Name, vhdl_configuration_BlockConfiguration, configuration_ConfigurationItem, configuration_vhdl_Name, ConfigurationItem, vhdl_configuration_ComponentConfiguration, configuration_vhdl_MultiName, configuration_vhdl_GenericMaps, configuration_vhdl_PortMaps, BlockConfiguration, vhdl_configuration_Configuration, configuration_vhdl_EntityReference, vhdl_configuration_ConfigurationReference, vhdl_configuration_ConfigurationResolvedReference, Configuration, vhdl_configuration_ConfigurationItem, UnaryOperator, RelationalOperator, LogicalOperator, AddingOperator, Sign, MultiplyingOperator, ShiftOperator, RangeDirection, SignalKind, Mode, EntityClass, Purity},
    associations={of0, statement1, generic3, port4, use6, module7, declaration9, generic11, port13, declaration20, design23, statement16, generic19, port29, parameter31, return32, name35, name37, name38, entity40, name25, declaration26, component43, call45, report46, severity48, waveform51, selected53, waveform55, target57, delay59, sensitivity61, package42, target68, initial70, case73, when75, choice77, statement79, until62, statement88, time65, procedure91, declaration92, statement94, test82, statement83, condition86, sensitivity102, condition105, report107, severity110, guard113, generic115, genericMap117, port119, declaration97, portMap121, statement99, statement126, break129, when130, sensitivity133, name136, use137, arrow140, name143, declaration123, genericMap144, portMap146, name149, name150, left151, right153, tolerance156, when159, scheme161, declaration162, statement165, iteration168, statement169, when172, condition174, expression176, in178, in180, condition182, reject184, choice186, expression188, signature191, left192, constraint197, tolerance199, across202, mark205, right194, element208, mark207, expression214, expression216, signature209, name211, unit218, expression220, expression225, expression227, after222, alias229, is231, entity233, is234, left241, right244, quantity247, value249, across237, through238, parameter252, body254, declaration256, statement258, source251, list261, component263, entity265, configuration267, genericMap270, portMap272, disconnect274, after276, open279, is281, is284, is285, is290, use291, initial293, member287, declaration295, constraint296, index298, literal300, range301, of305, left306, right308, type311, constraint313, record315, secondary303, across317, through320, index323, nature325, tolerance327, expression329, left332, right334, noise337, name316, use339, item340, list342, component343, entity346, configuration349, genericMap352, portMap354, block356, of358, configuration362, block359},
    generalizations={gen_vhdl_Architecture_Module, gen_vhdl_Architecture_Named, gen_vhdl_Component_declaration_Declaration, gen_vhdl_Component_Named, gen_vhdl_DesignUnit_VhdlObject, gen_vhdl_Module_VhdlObject, gen_vhdl_Entity_Module, gen_vhdl_Entity_Named, gen_vhdl_Generics_VhdlObject, gen_vhdl_Model_VhdlObject, gen_vhdl_Package_Module, gen_vhdl_Package_Named, gen_vhdl_PackageBody_Module, gen_vhdl_GenericMaps_VhdlObject, gen_vhdl_PortMaps_VhdlObject, gen_vhdl_Signature_VhdlObject, gen_vhdl_Name_MultiName, gen_vhdl_Name_type_TypeReference, gen_vhdl_Name_nature_NatureReference, gen_vhdl_Name_EntityReference, gen_vhdl_Name_PackageReference, gen_vhdl_Name_ComponentReference, gen_vhdl_Name_configuration_ConfigurationReference, gen_vhdl_Name_CallReference, gen_vhdl_NameList_VhdlObject, gen_vhdl_NameList_MultiName, gen_vhdl_EntityResolvedReference_VhdlObject, gen_vhdl_EntityResolvedReference_EntityReference, gen_vhdl_PackageResolvedReference_VhdlObject, gen_vhdl_PackageResolvedReference_PackageReference, gen_vhdl_Ports_VhdlObject, gen_vhdl_CallResolvedReference_CallReference, gen_vhdl_statement_ReportStatement_Statement, gen_vhdl_statement_ReturnStatement_ExpressionStatement, gen_vhdl_statement_ConditionalSignalAssignmentStatement_SignalAssignmentStatement, gen_vhdl_statement_SelectedSignalAssignmentStatement_ConditionalSignalAssignmentStatement, gen_vhdl_statement_SequentialSignalAssignmentStatement_SignalAssignmentStatement, gen_vhdl_statement_SignalAssignmentStatement_Statement, gen_vhdl_statement_WaitStatement_Statement, gen_vhdl_ComponentResolvedReference_VhdlObject, gen_vhdl_ComponentResolvedReference_ComponentReference, gen_vhdl_statement_VariableAssignmentStatement_Statement, gen_vhdl_statement_SimultaneousCaseStatement_CaseStatement, gen_vhdl_statement_CaseStatement_Statement, gen_vhdl_statement_CaseAlternative_VhdlObject, gen_vhdl_statement_SimultaneousIfStatement_IfStatement, gen_vhdl_statement_IfStatement_Statement, gen_vhdl_statement_ProcedureCallStatement_Statement, gen_vhdl_statement_SimultaneousProceduralStatement_Statement, gen_vhdl_statement_ProcessStatement_Statement, gen_vhdl_statement_IfStatementTest_VhdlObject, gen_vhdl_statement_AssertionStatement_Statement, gen_vhdl_statement_BlockStatement_Statement, gen_vhdl_statement_BreakStatement_Statement, gen_vhdl_statement_BreakStatementItem_VhdlObject, gen_vhdl_statement_ComponentInstantiationStatement_InstantiationStatement, gen_vhdl_statement_EntityInstantiationStatement_InstantiationStatement, gen_vhdl_statement_ConfigurationInstantiationStatement_InstantiationStatement, gen_vhdl_statement_SimpleSimultaneousStatement_Statement, gen_vhdl_statement_InstantiationStatement_Statement, gen_vhdl_statement_GenerateStatement_Statement, gen_vhdl_statement_LoopStatement_Statement, gen_vhdl_statement_ExitStatement_Statement, gen_vhdl_statement_Statement_VhdlObject, gen_vhdl_statement_IterationScheme_VhdlObject, gen_vhdl_statement_WhileIterationScheme_IterationScheme, gen_vhdl_statement_DelayMechanism_VhdlObject, gen_vhdl_statement_ExpressionStatement_Statement, gen_vhdl_statement_ForGenerationScheme_GenerationScheme, gen_vhdl_statement_NextStatement_Statement, gen_vhdl_statement_GenerationScheme_VhdlObject, gen_vhdl_statement_IfGenerationScheme_GenerationScheme, gen_vhdl_statement_RejectMechanism_DelayMechanism, gen_vhdl_statement_TransportMechanism_DelayMechanism, gen_vhdl_expression_AddingExpression_BinaryExpression, gen_vhdl_expression_AggregateExpression_expression_MultiExpression, gen_vhdl_expression_AggregateExpression_Name, gen_vhdl_statement_ForIterationScheme_IterationScheme, gen_vhdl_expression_AttributeExpression_expression_ValueExpression, gen_vhdl_expression_AttributeExpression_Name, gen_vhdl_expression_BinaryExpression_Expression, gen_vhdl_expression_AllExpression_expression_Expression, gen_vhdl_expression_AllExpression_Name, gen_vhdl_expression_AllocatorExpression_expression_Expression, gen_vhdl_expression_AllocatorExpression_type_Typed, gen_vhdl_expression_AssociationExpression_Expression, gen_vhdl_expression_Expression_VhdlObject, gen_vhdl_expression_IndicationExpression_Expression, gen_vhdl_expression_SubtypeIndicationExpression_expression_IndicationExpression, gen_vhdl_expression_SubtypeIndicationExpression_type_TypeReference, gen_vhdl_expression_SubtypeIndicationExpression_Named, gen_vhdl_expression_BitStringExpression_ValueExpression, gen_vhdl_expression_NameExpression_expression_Expression, gen_vhdl_expression_NameExpression_Name, gen_vhdl_expression_NullExpression_Expression, gen_vhdl_expression_MultiplyingExpression_BinaryExpression, gen_vhdl_expression_PowerExpression_BinaryExpression, gen_vhdl_expression_RelationalExpression_BinaryExpression, gen_vhdl_expression_ShiftExpression_BinaryExpression, gen_vhdl_expression_SignatureExpression_expression_Expression, gen_vhdl_expression_SignatureExpression_Name, gen_vhdl_expression_SubnatureIndicationExpression_expression_IndicationExpression, gen_vhdl_expression_SubnatureIndicationExpression_nature_NatureReference, gen_vhdl_expression_LogicalExpression_BinaryExpression, gen_vhdl_expression_UnaryExpression_Expression, gen_vhdl_expression_OpenExpression_Expression, gen_vhdl_expression_OthersExpression_expression_Expression, gen_vhdl_expression_OthersExpression_Name, gen_vhdl_expression_SignExpression_Expression, gen_vhdl_expression_CharacterExpression_expression_ValueExpression, gen_vhdl_expression_CharacterExpression_Name, gen_vhdl_expression_CharacterExpression_type_EnumerationLiteral, gen_vhdl_expression_IdentifierExpression_expression_ValueExpression, gen_vhdl_expression_IdentifierExpression_Name, gen_vhdl_expression_IdentifierExpression_type_EnumerationLiteral, gen_vhdl_expression_UnitValueExpression_ValueExpression, gen_vhdl_expression_UnaffectedExpression_Expression, gen_vhdl_expression_ValueExpression_Expression, gen_vhdl_expression_WaveformExpression_Expression, gen_vhdl_expression_RangeExpression_expression_BinaryExpression, gen_vhdl_expression_RangeExpression_Name, gen_vhdl_expression_StringExpression_expression_ValueExpression, gen_vhdl_expression_StringExpression_Name, gen_vhdl_expression_MultiExpression_Expression, gen_vhdl_expression_ConditionalWaveformExpression_AssociationExpression, gen_vhdl_expression_TypeQualificationExpression_expression_Expression, gen_vhdl_expression_TypeQualificationExpression_Name, gen_vhdl_declaration_AliasDeclaration_declaration_Declaration, gen_vhdl_declaration_AliasDeclaration_Named, gen_vhdl_declaration_AttributeDeclaration_declaration_Declaration, gen_vhdl_declaration_AttributeDeclaration_Named, gen_vhdl_declaration_AttributeDeclaration_type_Typed, gen_vhdl_declaration_AttributeSpecification_declaration_Declaration, gen_vhdl_declaration_AttributeSpecification_Named, gen_vhdl_declaration_BranchQuantityDeclaration_QuantityDeclaration, gen_vhdl_declaration_FreeQuantityDeclaration_declaration_QuantityDeclaration, gen_vhdl_declaration_FreeQuantityDeclaration_MultiNamed, gen_vhdl_declaration_FreeQuantityDeclaration_type_Typed, gen_vhdl_declaration_LimitDeclaration_declaration_Declaration, gen_vhdl_declaration_LimitDeclaration_MultiNamed, gen_vhdl_declaration_LimitDeclaration_type_Typed, gen_vhdl_declaration_QuantityDeclaration_Declaration, gen_vhdl_declaration_SubnatureDeclaration_declaration_Declaration, gen_vhdl_declaration_SubnatureDeclaration_Named, gen_vhdl_declaration_SubnatureDeclaration_nature_Natured, gen_vhdl_declaration_SubprogramDeclaration_declaration_Declaration, gen_vhdl_declaration_SubprogramDeclaration_Named, gen_vhdl_declaration_ProcedureDeclaration_SubprogramDeclaration, gen_vhdl_declaration_FunctionDeclaration_declaration_SubprogramDeclaration, gen_vhdl_declaration_FunctionDeclaration_type_Typed, gen_vhdl_declaration_SubprogramBody_VhdlObject, gen_vhdl_declaration_SourceQuantityDeclaration_declaration_QuantityDeclaration, gen_vhdl_declaration_SourceQuantityDeclaration_MultiNamed, gen_vhdl_declaration_SourceQuantityDeclaration_type_Typed, gen_vhdl_declaration_Declaration_VhdlObject, gen_vhdl_declaration_DisconnectionSpecification_declaration_Declaration, gen_vhdl_declaration_DisconnectionSpecification_type_Typed, gen_vhdl_declaration_FileDeclaration_declaration_Declaration, gen_vhdl_declaration_FileDeclaration_MultiNamed, gen_vhdl_declaration_FileDeclaration_type_Typed, gen_vhdl_declaration_TerminalDeclaration_declaration_Declaration, gen_vhdl_declaration_TerminalDeclaration_MultiNamed, gen_vhdl_declaration_TerminalDeclaration_nature_Natured, gen_vhdl_declaration_TypeDeclaration_declaration_Declaration, gen_vhdl_declaration_TypeDeclaration_Named, gen_vhdl_declaration_ConstantDeclaration_ValueDeclaration, gen_vhdl_declaration_GroupDeclaration_declaration_Declaration, gen_vhdl_declaration_GroupDeclaration_Named, gen_vhdl_declaration_SubtypeDeclaration_declaration_Declaration, gen_vhdl_declaration_SubtypeDeclaration_Named, gen_vhdl_declaration_SubtypeDeclaration_type_Typed, gen_vhdl_declaration_ConfigurationSpecification_Declaration, gen_vhdl_declaration_NatureDeclaration_declaration_Declaration, gen_vhdl_declaration_NatureDeclaration_Named, gen_vhdl_declaration_SignalDeclaration_ValueDeclaration, gen_vhdl_declaration_UseClauseDeclaration_Declaration, gen_vhdl_declaration_VariableDeclaration_ValueDeclaration, gen_vhdl_declaration_ValueDeclaration_declaration_Declaration, gen_vhdl_declaration_ValueDeclaration_MultiNamed, gen_vhdl_declaration_ValueDeclaration_type_Typed, gen_vhdl_declaration_GroupTemplateDeclaration_declaration_Declaration, gen_vhdl_declaration_GroupTemplateDeclaration_Named, gen_vhdl_type_AccessTypeDefinition_type_TypeDefinition, gen_vhdl_type_AccessTypeDefinition_type_Typed, gen_vhdl_type_CompositeTypeDefinition_TypeDefinition, gen_vhdl_type_RecordTypeDefinition_CompositeTypeDefinition, gen_vhdl_type_ArrayTypeDefinition_type_CompositeTypeDefinition, gen_vhdl_type_ArrayTypeDefinition_type_Typed, gen_vhdl_type_ConstrainedArrayTypeDefinition_ArrayTypeDefinition, gen_vhdl_type_UnconstrainedArrayTypeDefinition_ArrayTypeDefinition, gen_vhdl_type_EnumerationTypeDefinition_TypeDefinition, gen_vhdl_type_FileTypeDefinition_type_TypeDefinition, gen_vhdl_type_FileTypeDefinition_type_Typed, gen_vhdl_type_PhysicalTypeDefinition_TypeDefinition, gen_vhdl_type_RangeTypeDefinition_TypeDefinition, gen_vhdl_type_RecordTypeElement_VhdlObject, gen_vhdl_type_RecordTypeElement_MultiNamed, gen_vhdl_type_RecordTypeElement_type_Typed, gen_vhdl_type_TypeDefinition_VhdlObject, gen_vhdl_nature_ArrayNatureDefinition_nature_CompositeNatureDefinition, gen_vhdl_nature_ArrayNatureDefinition_nature_Natured, gen_vhdl_nature_CompositeNatureDefinition_NatureDefinition, gen_vhdl_nature_ConstrainedArrayNatureDefinition_ArrayNatureDefinition, gen_vhdl_nature_NatureDefinition_VhdlObject, gen_vhdl_nature_RecordNatureDefinition_CompositeNatureDefinition, gen_vhdl_nature_RecordNatureElement_VhdlObject, gen_vhdl_nature_RecordNatureElement_MultiNamed, gen_vhdl_nature_RecordNatureElement_nature_Natured, gen_vhdl_nature_UnconstrainedArrayNatureDefinition_ArrayNatureDefinition, gen_vhdl_ams_QuantityAspect_VhdlObject, gen_vhdl_ams_QuantityAspect_MultiNamed, gen_vhdl_ams_SourceAspect_VhdlObject, gen_vhdl_ams_Spectrum_SourceAspect, gen_vhdl_ams_Noise_SourceAspect, gen_vhdl_nature_ScalarNatureDefinition_NatureDefinition, gen_vhdl_configuration_BlockConfiguration_configuration_ConfigurationItem, gen_vhdl_configuration_BlockConfiguration_Named, gen_vhdl_configuration_ComponentConfiguration_ConfigurationItem, gen_vhdl_configuration_Configuration_Module, gen_vhdl_configuration_Configuration_Named, gen_vhdl_configuration_ConfigurationResolvedReference_VhdlObject, gen_vhdl_configuration_ConfigurationResolvedReference_configuration_ConfigurationReference, gen_vhdl_configuration_ConfigurationItem_VhdlObject},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)