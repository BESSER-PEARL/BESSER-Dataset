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
ParamDirection: Enumeration = Enumeration(
    name="ParamDirection",
    literals={
            EnumerationLiteral(name="In"),
			EnumerationLiteral(name="Out"),
			EnumerationLiteral(name="InOut")
    }
)

# Classes
ComponentExport = Class(name="ComponentExport")
idl_Preproc_Include = Class(name="idl::Preproc::Include")
Preproc = Class(name="Preproc")
idl_FileName = Class(name="idl::FileName")
idl_Preproc_Ifdef = Class(name="idl::Preproc::Ifdef")
idl_Preproc_Ifndef = Class(name="idl::Preproc::Ifndef")
idl_Preproc_Undef = Class(name="idl::Preproc::Undef")
idl_Preproc_If = Class(name="idl::Preproc::If")
idl_Preproc_If_Compare = Class(name="idl::Preproc::If::Compare")
idl_Preproc_If_Val = Class(name="idl::Preproc::If::Val")
idl_ConstExp = Class(name="idl::ConstExp")
idl_Preproc_Else = Class(name="idl::Preproc::Else")
idl_Preproc_Error = Class(name="idl::Preproc::Error")
idl_Specification = Class(name="idl::Specification")
idl_Import_decl = Class(name="idl::Import::decl")
idl_Definition = Class(name="idl::Definition")
idl_Preproc = Class(name="idl::Preproc")
Definition = Class(name="Definition")
Export = Class(name="Export")
idl_Preproc_Pragma_Prefix = Class(name="idl::Preproc::Pragma::Prefix")
Preproc_Pragma = Class(name="Preproc::Pragma")
idl_Preproc_Pragma_Ciao_Lem = Class(name="idl::Preproc::Pragma::Ciao::Lem")
idl_Preproc_Pragma_Ciao_Ami4ccm_Interface = Class(name="idl::Preproc::Pragma::Ciao::Ami4ccm::Interface")
idl_Preproc_Pragma_Ciao_Ami4ccm_Receptacle = Class(name="idl::Preproc::Pragma::Ciao::Ami4ccm::Receptacle")
idl_Preproc_Pragma_Ciao_Ami4ccm_Idl = Class(name="idl::Preproc::Pragma::Ciao::Ami4ccm::Idl")
idl_Preproc_Pragma_Ndds = Class(name="idl::Preproc::Pragma::Ndds")
idl_Preproc_Pragma_Component = Class(name="idl::Preproc::Pragma::Component")
idl_Preproc_Pragma_Home = Class(name="idl::Preproc::Pragma::Home")
idl_Preproc_Pragma_DDS4CCM_Impl = Class(name="idl::Preproc::Pragma::DDS4CCM::Impl")
idl_Preproc_Define = Class(name="idl::Preproc::Define")
idl_Preproc_Endif = Class(name="idl::Preproc::Endif")
idl_Preproc_Pragma = Class(name="idl::Preproc::Pragma")
idl_IDLComment = Class(name="idl::IDLComment")
idl_Interface_or_Forward_Decl = Class(name="idl::Interface::or::Forward::Decl")
idl_Interface_decl = Class(name="idl::Interface::decl")
Interface_or_Forward_Decl = Class(name="Interface::or::Forward::Decl")
TemplateDefinition = Class(name="TemplateDefinition")
FixedDefinition = Class(name="FixedDefinition")
idl_Interface_header = Class(name="idl::Interface::header")
idl_InterfaceBody = Class(name="idl::InterfaceBody")
idl_Forward_decl = Class(name="idl::Forward::decl")
idl_ScopedName = Class(name="idl::ScopedName")
idl_Export = Class(name="idl::Export")
HomeExport = Class(name="HomeExport")
idl_AttrDecl = Class(name="idl::AttrDecl")
PortExport = Class(name="PortExport")
ConnectorExport = Class(name="ConnectorExport")
idl_ParamTypeSpec = Class(name="idl::ParamTypeSpec")
idl_AttrSpec = Class(name="idl::AttrSpec")
AttrDecl = Class(name="AttrDecl")
idl_AttrRaisesExpr = Class(name="idl::AttrRaisesExpr")
idl_ReadOnlyAttrSpec = Class(name="idl::ReadOnlyAttrSpec")
idl_Preproc_Pragma_Misc = Class(name="idl::Preproc::Pragma::Misc")
idl_File_Marker = Class(name="idl::File::Marker")
idl_Excluded_File_Marker = Class(name="idl::Excluded::File::Marker")
idl_Module = Class(name="idl::Module")
idl_OpDecl = Class(name="idl::OpDecl")
idl_OpTypeDecl = Class(name="idl::OpTypeDecl")
idl_ParameterDecls = Class(name="idl::ParameterDecls")
idl_ContextExpr = Class(name="idl::ContextExpr")
idl_ParamDcl = Class(name="idl::ParamDcl")
idl_ExceptionList = Class(name="idl::ExceptionList")
idl_DoubleType = Class(name="idl::DoubleType")
idl_LongDoubleType = Class(name="idl::LongDoubleType")
idl_IntegerType = Class(name="idl::IntegerType")
idl_SignedInt = Class(name="idl::SignedInt")
IntegerType = Class(name="IntegerType")
idl_SignedShortInt = Class(name="idl::SignedShortInt")
SignedInt = Class(name="SignedInt")
idl_SignedLongInt = Class(name="idl::SignedLongInt")
idl_SignedLongLongInt = Class(name="idl::SignedLongLongInt")
idl_UnsignedInt = Class(name="idl::UnsignedInt")
idl_UnsignedShortInt = Class(name="idl::UnsignedShortInt")
UnsignedInt = Class(name="UnsignedInt")
idl_UnsignedLongInt = Class(name="idl::UnsignedLongInt")
idl_UnsignedLongLongInt = Class(name="idl::UnsignedLongLongInt")
idl_CharType = Class(name="idl::CharType")
idl_WideCharType = Class(name="idl::WideCharType")
idl_BooleanType = Class(name="idl::BooleanType")
OpTypeDecl = Class(name="OpTypeDecl")
ParamTypeSpec = Class(name="ParamTypeSpec")
SimpleTypeSpec = Class(name="SimpleTypeSpec")
SwitchTypeSpec = Class(name="SwitchTypeSpec")
ConstType = Class(name="ConstType")
PrimaryExpr = Class(name="PrimaryExpr")
idl_BaseTypeSpec = Class(name="idl::BaseTypeSpec")
idl_FloatingPtType = Class(name="idl::FloatingPtType")
BaseTypeSpec = Class(name="BaseTypeSpec")
idl_FloatType = Class(name="idl::FloatType")
FloatingPtType = Class(name="FloatingPtType")
idl_Member = Class(name="idl::Member")
idl_TypeSpec = Class(name="idl::TypeSpec")
idl_Declarator = Class(name="idl::Declarator")
idl_SimpleDeclarator = Class(name="idl::SimpleDeclarator")
Declarator = Class(name="Declarator")
idl_ComplexDeclarator = Class(name="idl::ComplexDeclarator")
idl_ArrayDeclarator = Class(name="idl::ArrayDeclarator")
ComplexDeclarator = Class(name="ComplexDeclarator")
idl_StructType = Class(name="idl::StructType")
TypeDecl = Class(name="TypeDecl")
ConstrTypeSpec = Class(name="ConstrTypeSpec")
idl_TypeDecl = Class(name="idl::TypeDecl")
idl_TypeDeclarator = Class(name="idl::TypeDeclarator")
idl_OctetType = Class(name="idl::OctetType")
idl_AnyType = Class(name="idl::AnyType")
idl_ObjectType = Class(name="idl::ObjectType")
idl_ValueBaseType = Class(name="idl::ValueBaseType")
idl_StringType = Class(name="idl::StringType")
TemplateTypeSpec = Class(name="TemplateTypeSpec")
idl_PositiveIntConst = Class(name="idl::PositiveIntConst")
idl_WideStringType = Class(name="idl::WideStringType")
idl_ExceptDecl = Class(name="idl::ExceptDecl")
idl_UnionType = Class(name="idl::UnionType")
idl_SwitchTypeSpec = Class(name="idl::SwitchTypeSpec")
idl_SwitchBody = Class(name="idl::SwitchBody")
idl_Case = Class(name="idl::Case")
idl_CaseLabel = Class(name="idl::CaseLabel")
idl_ElementSpec = Class(name="idl::ElementSpec")
idl_EnumType = Class(name="idl::EnumType")
ActualParameter = Class(name="ActualParameter")
idl_SimpleTypeSpec = Class(name="idl::SimpleTypeSpec")
TypeSpec = Class(name="TypeSpec")
idl_TemplateTypeSpec = Class(name="idl::TemplateTypeSpec")
idl_ConstrTypeSpec = Class(name="idl::ConstrTypeSpec")
idl_FixedPtType = Class(name="idl::FixedPtType")
idl_ConstrForwardDecl = Class(name="idl::ConstrForwardDecl")
idl_StructForwardDecl = Class(name="idl::StructForwardDecl")
ConstrForwardDecl = Class(name="ConstrForwardDecl")
idl_UnionForwardDecl = Class(name="idl::UnionForwardDecl")
idl_ConstDecl = Class(name="idl::ConstDecl")
idl_ConstType = Class(name="idl::ConstType")
ConstParamType = Class(name="ConstParamType")
idl_FixedPtConstType = Class(name="idl::FixedPtConstType")
idl_OrExpr = Class(name="idl::OrExpr")
ConstExp = Class(name="ConstExp")
idl_XOrExpr = Class(name="idl::XOrExpr")
idl_SequenceType = Class(name="idl::SequenceType")
FormalParameterType = Class(name="FormalParameterType")
idl_NativeType = Class(name="idl::NativeType")
idl_AddExpr = Class(name="idl::AddExpr")
idl_MultExpr = Class(name="idl::MultExpr")
idl_UnaryExpr = Class(name="idl::UnaryExpr")
idl_PrimaryExpr = Class(name="idl::PrimaryExpr")
idl_Literal = Class(name="idl::Literal")
idl_ComponentDecl = Class(name="idl::ComponentDecl")
idl_AndExpr = Class(name="idl::AndExpr")
idl_ShiftExpr = Class(name="idl::ShiftExpr")
idl_UsesDcl = Class(name="idl::UsesDcl")
idl_PublishesDcl = Class(name="idl::PublishesDcl")
idl_EmitDcl = Class(name="idl::EmitDcl")
idl_ConsumesDcl = Class(name="idl::ConsumesDcl")
idl_ComponentForwardDecl = Class(name="idl::ComponentForwardDecl")
idl_ComponentExport = Class(name="idl::ComponentExport")
idl_ProvidesDcl = Class(name="idl::ProvidesDcl")
idl_PrimaryKeySpec = Class(name="idl::PrimaryKeySpec")
idl_HomeExport = Class(name="idl::HomeExport")
idl_FactoryDcl = Class(name="idl::FactoryDcl")
idl_FinderDcl = Class(name="idl::FinderDcl")
idl_Event = Class(name="idl::Event")
idl_EventDcl = Class(name="idl::EventDcl")
Event = Class(name="Event")
idl_HomeDecl = Class(name="idl::HomeDecl")
idl_EventForwardDcl = Class(name="idl::EventForwardDcl")
idl_PortTypeDecl = Class(name="idl::PortTypeDecl")
idl_PortExport = Class(name="idl::PortExport")
idl_PortDecl = Class(name="idl::PortDecl")
idl_Connector = Class(name="idl::Connector")
idl_ConnectorHeader = Class(name="idl::ConnectorHeader")
idl_ConnectorExport = Class(name="idl::ConnectorExport")
idl_StateMember = Class(name="idl::StateMember")
idl_TypenameParamType = Class(name="idl::TypenameParamType")
idl_InterfaceParamType = Class(name="idl::InterfaceParamType")
idl_ValuetypeParamType = Class(name="idl::ValuetypeParamType")
idl_EventParamType = Class(name="idl::EventParamType")
idl_StructParamType = Class(name="idl::StructParamType")
idl_UnionParamType = Class(name="idl::UnionParamType")
idl_ExceptionParamType = Class(name="idl::ExceptionParamType")
idl_EnumParamType = Class(name="idl::EnumParamType")
idl_SequenceParamType = Class(name="idl::SequenceParamType")
idl_ConstParamType = Class(name="idl::ConstParamType")
idl_FixedModule = Class(name="idl::FixedModule")
idl_FixedDefinition = Class(name="idl::FixedDefinition")
idl_TemplateModuleInst = Class(name="idl::TemplateModuleInst")
idl_ActualParameter = Class(name="idl::ActualParameter")
idl_TemplateModuleRef = Class(name="idl::TemplateModuleRef")
idl_TemplateModule = Class(name="idl::TemplateModule")
idl_FormalParameter = Class(name="idl::FormalParameter")
idl_TemplateDefinition = Class(name="idl::TemplateDefinition")
idl_FormalParameterType = Class(name="idl::FormalParameterType")

# ComponentExport class attributes and methods

# idl_Preproc_Include class attributes and methods
idl_Preproc_Include_strValue: Property = Property(name="strValue", type=StringType)
idl_Preproc_Include.attributes={idl_Preproc_Include_strValue}

# Preproc class attributes and methods

# idl_FileName class attributes and methods
idl_FileName_name: Property = Property(name="name", type=StringType)
idl_FileName.attributes={idl_FileName_name}

# idl_Preproc_Ifdef class attributes and methods
idl_Preproc_Ifdef_value: Property = Property(name="value", type=StringType)
idl_Preproc_Ifdef.attributes={idl_Preproc_Ifdef_value}

# idl_Preproc_Ifndef class attributes and methods
idl_Preproc_Ifndef_value: Property = Property(name="value", type=StringType)
idl_Preproc_Ifndef.attributes={idl_Preproc_Ifndef_value}

# idl_Preproc_Undef class attributes and methods
idl_Preproc_Undef_value: Property = Property(name="value", type=StringType)
idl_Preproc_Undef.attributes={idl_Preproc_Undef_value}

# idl_Preproc_If class attributes and methods
idl_Preproc_If_negation: Property = Property(name="negation", type=BooleanType)
idl_Preproc_If.attributes={idl_Preproc_If_negation}

# idl_Preproc_If_Compare class attributes and methods
idl_Preproc_If_Compare_op: Property = Property(name="op", type=StringType)
idl_Preproc_If_Compare.attributes={idl_Preproc_If_Compare_op}

# idl_Preproc_If_Val class attributes and methods

# idl_ConstExp class attributes and methods

# idl_Preproc_Else class attributes and methods

# idl_Preproc_Error class attributes and methods
idl_Preproc_Error_value: Property = Property(name="value", type=StringType)
idl_Preproc_Error.attributes={idl_Preproc_Error_value}

# idl_Specification class attributes and methods

# idl_Import_decl class attributes and methods
idl_Import_decl_imported_scope: Property = Property(name="imported_scope", type=StringType)
idl_Import_decl.attributes={idl_Import_decl_imported_scope}

# idl_Definition class attributes and methods

# idl_Preproc class attributes and methods

# Definition class attributes and methods

# Export class attributes and methods

# idl_Preproc_Pragma_Prefix class attributes and methods
idl_Preproc_Pragma_Prefix_value: Property = Property(name="value", type=StringType)
idl_Preproc_Pragma_Prefix.attributes={idl_Preproc_Pragma_Prefix_value}

# Preproc_Pragma class attributes and methods

# idl_Preproc_Pragma_Ciao_Lem class attributes and methods
idl_Preproc_Pragma_Ciao_Lem_value: Property = Property(name="value", type=StringType)
idl_Preproc_Pragma_Ciao_Lem.attributes={idl_Preproc_Pragma_Ciao_Lem_value}

# idl_Preproc_Pragma_Ciao_Ami4ccm_Interface class attributes and methods
idl_Preproc_Pragma_Ciao_Ami4ccm_Interface_value: Property = Property(name="value", type=StringType)
idl_Preproc_Pragma_Ciao_Ami4ccm_Interface.attributes={idl_Preproc_Pragma_Ciao_Ami4ccm_Interface_value}

# idl_Preproc_Pragma_Ciao_Ami4ccm_Receptacle class attributes and methods
idl_Preproc_Pragma_Ciao_Ami4ccm_Receptacle_value: Property = Property(name="value", type=StringType)
idl_Preproc_Pragma_Ciao_Ami4ccm_Receptacle.attributes={idl_Preproc_Pragma_Ciao_Ami4ccm_Receptacle_value}

# idl_Preproc_Pragma_Ciao_Ami4ccm_Idl class attributes and methods
idl_Preproc_Pragma_Ciao_Ami4ccm_Idl_value: Property = Property(name="value", type=StringType)
idl_Preproc_Pragma_Ciao_Ami4ccm_Idl.attributes={idl_Preproc_Pragma_Ciao_Ami4ccm_Idl_value}

# idl_Preproc_Pragma_Ndds class attributes and methods
idl_Preproc_Pragma_Ndds_value: Property = Property(name="value", type=StringType)
idl_Preproc_Pragma_Ndds.attributes={idl_Preproc_Pragma_Ndds_value}

# idl_Preproc_Pragma_Component class attributes and methods
idl_Preproc_Pragma_Component_value: Property = Property(name="value", type=StringType)
idl_Preproc_Pragma_Component.attributes={idl_Preproc_Pragma_Component_value}

# idl_Preproc_Pragma_Home class attributes and methods
idl_Preproc_Pragma_Home_value: Property = Property(name="value", type=StringType)
idl_Preproc_Pragma_Home.attributes={idl_Preproc_Pragma_Home_value}

# idl_Preproc_Pragma_DDS4CCM_Impl class attributes and methods
idl_Preproc_Pragma_DDS4CCM_Impl_value: Property = Property(name="value", type=StringType)
idl_Preproc_Pragma_DDS4CCM_Impl.attributes={idl_Preproc_Pragma_DDS4CCM_Impl_value}

# idl_Preproc_Define class attributes and methods
idl_Preproc_Define_value: Property = Property(name="value", type=StringType)
idl_Preproc_Define.attributes={idl_Preproc_Define_value}

# idl_Preproc_Endif class attributes and methods

# idl_Preproc_Pragma class attributes and methods

# idl_IDLComment class attributes and methods
idl_IDLComment_body: Property = Property(name="body", type=StringType)
idl_IDLComment.attributes={idl_IDLComment_body}

# idl_Interface_or_Forward_Decl class attributes and methods

# idl_Interface_decl class attributes and methods

# Interface_or_Forward_Decl class attributes and methods

# TemplateDefinition class attributes and methods

# FixedDefinition class attributes and methods

# idl_Interface_header class attributes and methods
idl_Interface_header_isAbstract: Property = Property(name="isAbstract", type=BooleanType)
idl_Interface_header_isLocal: Property = Property(name="isLocal", type=BooleanType)
idl_Interface_header_name: Property = Property(name="name", type=StringType)
idl_Interface_header.attributes={idl_Interface_header_isAbstract, idl_Interface_header_isLocal, idl_Interface_header_name}

# idl_InterfaceBody class attributes and methods

# idl_Forward_decl class attributes and methods
idl_Forward_decl_name: Property = Property(name="name", type=StringType)
idl_Forward_decl.attributes={idl_Forward_decl_name}

# idl_ScopedName class attributes and methods
idl_ScopedName_name: Property = Property(name="name", type=StringType)
idl_ScopedName.attributes={idl_ScopedName_name}

# idl_Export class attributes and methods

# HomeExport class attributes and methods

# idl_AttrDecl class attributes and methods
idl_AttrDecl_names: Property = Property(name="names", type=StringType)
idl_AttrDecl.attributes={idl_AttrDecl_names}

# PortExport class attributes and methods

# ConnectorExport class attributes and methods

# idl_ParamTypeSpec class attributes and methods

# idl_AttrSpec class attributes and methods

# AttrDecl class attributes and methods

# idl_AttrRaisesExpr class attributes and methods

# idl_ReadOnlyAttrSpec class attributes and methods

# idl_Preproc_Pragma_Misc class attributes and methods

# idl_File_Marker class attributes and methods
idl_File_Marker_file: Property = Property(name="file", type=StringType)
idl_File_Marker.attributes={idl_File_Marker_file}

# idl_Excluded_File_Marker class attributes and methods
idl_Excluded_File_Marker_file: Property = Property(name="file", type=StringType)
idl_Excluded_File_Marker.attributes={idl_Excluded_File_Marker_file}

# idl_Module class attributes and methods
idl_Module_name: Property = Property(name="name", type=StringType)
idl_Module.attributes={idl_Module_name}

# idl_OpDecl class attributes and methods
idl_OpDecl_isOneway: Property = Property(name="isOneway", type=BooleanType)
idl_OpDecl_name: Property = Property(name="name", type=StringType)
idl_OpDecl.attributes={idl_OpDecl_name, idl_OpDecl_isOneway}

# idl_OpTypeDecl class attributes and methods

# idl_ParameterDecls class attributes and methods

# idl_ContextExpr class attributes and methods
idl_ContextExpr_literal: Property = Property(name="literal", type=StringType)
idl_ContextExpr.attributes={idl_ContextExpr_literal}

# idl_ParamDcl class attributes and methods
idl_ParamDcl_direction: Property = Property(name="direction", type=StringType)
idl_ParamDcl_name: Property = Property(name="name", type=StringType)
idl_ParamDcl.attributes={idl_ParamDcl_name, idl_ParamDcl_direction}

# idl_ExceptionList class attributes and methods

# idl_DoubleType class attributes and methods

# idl_LongDoubleType class attributes and methods

# idl_IntegerType class attributes and methods

# idl_SignedInt class attributes and methods

# IntegerType class attributes and methods

# idl_SignedShortInt class attributes and methods

# SignedInt class attributes and methods

# idl_SignedLongInt class attributes and methods

# idl_SignedLongLongInt class attributes and methods

# idl_UnsignedInt class attributes and methods

# idl_UnsignedShortInt class attributes and methods

# UnsignedInt class attributes and methods

# idl_UnsignedLongInt class attributes and methods

# idl_UnsignedLongLongInt class attributes and methods

# idl_CharType class attributes and methods

# idl_WideCharType class attributes and methods

# idl_BooleanType class attributes and methods

# OpTypeDecl class attributes and methods

# ParamTypeSpec class attributes and methods

# SimpleTypeSpec class attributes and methods

# SwitchTypeSpec class attributes and methods

# ConstType class attributes and methods

# PrimaryExpr class attributes and methods

# idl_BaseTypeSpec class attributes and methods

# idl_FloatingPtType class attributes and methods

# BaseTypeSpec class attributes and methods

# idl_FloatType class attributes and methods

# FloatingPtType class attributes and methods

# idl_Member class attributes and methods

# idl_TypeSpec class attributes and methods

# idl_Declarator class attributes and methods
idl_Declarator_id: Property = Property(name="id", type=StringType)
idl_Declarator.attributes={idl_Declarator_id}

# idl_SimpleDeclarator class attributes and methods

# Declarator class attributes and methods

# idl_ComplexDeclarator class attributes and methods

# idl_ArrayDeclarator class attributes and methods

# ComplexDeclarator class attributes and methods

# idl_StructType class attributes and methods
idl_StructType_name: Property = Property(name="name", type=StringType)
idl_StructType.attributes={idl_StructType_name}

# TypeDecl class attributes and methods

# ConstrTypeSpec class attributes and methods

# idl_TypeDecl class attributes and methods

# idl_TypeDeclarator class attributes and methods

# idl_OctetType class attributes and methods

# idl_AnyType class attributes and methods

# idl_ObjectType class attributes and methods

# idl_ValueBaseType class attributes and methods

# idl_StringType class attributes and methods

# TemplateTypeSpec class attributes and methods

# idl_PositiveIntConst class attributes and methods

# idl_WideStringType class attributes and methods

# idl_ExceptDecl class attributes and methods
idl_ExceptDecl_name: Property = Property(name="name", type=StringType)
idl_ExceptDecl.attributes={idl_ExceptDecl_name}

# idl_UnionType class attributes and methods
idl_UnionType_name: Property = Property(name="name", type=StringType)
idl_UnionType.attributes={idl_UnionType_name}

# idl_SwitchTypeSpec class attributes and methods

# idl_SwitchBody class attributes and methods

# idl_Case class attributes and methods

# idl_CaseLabel class attributes and methods
idl_CaseLabel_isCase: Property = Property(name="isCase", type=BooleanType)
idl_CaseLabel_isDefault: Property = Property(name="isDefault", type=BooleanType)
idl_CaseLabel.attributes={idl_CaseLabel_isCase, idl_CaseLabel_isDefault}

# idl_ElementSpec class attributes and methods

# idl_EnumType class attributes and methods
idl_EnumType_name: Property = Property(name="name", type=StringType)
idl_EnumType_literal: Property = Property(name="literal", type=StringType)
idl_EnumType.attributes={idl_EnumType_name, idl_EnumType_literal}

# ActualParameter class attributes and methods

# idl_SimpleTypeSpec class attributes and methods

# TypeSpec class attributes and methods

# idl_TemplateTypeSpec class attributes and methods

# idl_ConstrTypeSpec class attributes and methods

# idl_FixedPtType class attributes and methods

# idl_ConstrForwardDecl class attributes and methods
idl_ConstrForwardDecl_name: Property = Property(name="name", type=StringType)
idl_ConstrForwardDecl.attributes={idl_ConstrForwardDecl_name}

# idl_StructForwardDecl class attributes and methods

# ConstrForwardDecl class attributes and methods

# idl_UnionForwardDecl class attributes and methods

# idl_ConstDecl class attributes and methods
idl_ConstDecl_name: Property = Property(name="name", type=StringType)
idl_ConstDecl.attributes={idl_ConstDecl_name}

# idl_ConstType class attributes and methods

# ConstParamType class attributes and methods

# idl_FixedPtConstType class attributes and methods

# idl_OrExpr class attributes and methods
idl_OrExpr_op: Property = Property(name="op", type=StringType)
idl_OrExpr.attributes={idl_OrExpr_op}

# ConstExp class attributes and methods

# idl_XOrExpr class attributes and methods
idl_XOrExpr_op: Property = Property(name="op", type=StringType)
idl_XOrExpr.attributes={idl_XOrExpr_op}

# idl_SequenceType class attributes and methods

# FormalParameterType class attributes and methods

# idl_NativeType class attributes and methods
idl_NativeType_name: Property = Property(name="name", type=StringType)
idl_NativeType.attributes={idl_NativeType_name}

# idl_AddExpr class attributes and methods
idl_AddExpr_op: Property = Property(name="op", type=StringType)
idl_AddExpr.attributes={idl_AddExpr_op}

# idl_MultExpr class attributes and methods
idl_MultExpr_op: Property = Property(name="op", type=StringType)
idl_MultExpr.attributes={idl_MultExpr_op}

# idl_UnaryExpr class attributes and methods
idl_UnaryExpr_op: Property = Property(name="op", type=StringType)
idl_UnaryExpr.attributes={idl_UnaryExpr_op}

# idl_PrimaryExpr class attributes and methods

# idl_Literal class attributes and methods
idl_Literal_value: Property = Property(name="value", type=StringType)
idl_Literal.attributes={idl_Literal_value}

# idl_ComponentDecl class attributes and methods
idl_ComponentDecl_name: Property = Property(name="name", type=StringType)
idl_ComponentDecl.attributes={idl_ComponentDecl_name}

# idl_AndExpr class attributes and methods
idl_AndExpr_op: Property = Property(name="op", type=StringType)
idl_AndExpr.attributes={idl_AndExpr_op}

# idl_ShiftExpr class attributes and methods
idl_ShiftExpr_op: Property = Property(name="op", type=StringType)
idl_ShiftExpr.attributes={idl_ShiftExpr_op}

# idl_UsesDcl class attributes and methods
idl_UsesDcl_isMultiple: Property = Property(name="isMultiple", type=BooleanType)
idl_UsesDcl_name: Property = Property(name="name", type=StringType)
idl_UsesDcl.attributes={idl_UsesDcl_isMultiple, idl_UsesDcl_name}

# idl_PublishesDcl class attributes and methods
idl_PublishesDcl_name: Property = Property(name="name", type=StringType)
idl_PublishesDcl.attributes={idl_PublishesDcl_name}

# idl_EmitDcl class attributes and methods
idl_EmitDcl_name: Property = Property(name="name", type=StringType)
idl_EmitDcl.attributes={idl_EmitDcl_name}

# idl_ConsumesDcl class attributes and methods
idl_ConsumesDcl_name: Property = Property(name="name", type=StringType)
idl_ConsumesDcl.attributes={idl_ConsumesDcl_name}

# idl_ComponentForwardDecl class attributes and methods
idl_ComponentForwardDecl_name: Property = Property(name="name", type=StringType)
idl_ComponentForwardDecl.attributes={idl_ComponentForwardDecl_name}

# idl_ComponentExport class attributes and methods

# idl_ProvidesDcl class attributes and methods
idl_ProvidesDcl_name: Property = Property(name="name", type=StringType)
idl_ProvidesDcl.attributes={idl_ProvidesDcl_name}

# idl_PrimaryKeySpec class attributes and methods

# idl_HomeExport class attributes and methods

# idl_FactoryDcl class attributes and methods
idl_FactoryDcl_name: Property = Property(name="name", type=StringType)
idl_FactoryDcl.attributes={idl_FactoryDcl_name}

# idl_FinderDcl class attributes and methods
idl_FinderDcl_name: Property = Property(name="name", type=StringType)
idl_FinderDcl.attributes={idl_FinderDcl_name}

# idl_Event class attributes and methods
idl_Event_isAbstract: Property = Property(name="isAbstract", type=BooleanType)
idl_Event_name: Property = Property(name="name", type=StringType)
idl_Event.attributes={idl_Event_name, idl_Event_isAbstract}

# idl_EventDcl class attributes and methods
idl_EventDcl_isCustom: Property = Property(name="isCustom", type=BooleanType)
idl_EventDcl_isTruncatable: Property = Property(name="isTruncatable", type=BooleanType)
idl_EventDcl.attributes={idl_EventDcl_isCustom, idl_EventDcl_isTruncatable}

# Event class attributes and methods

# idl_HomeDecl class attributes and methods
idl_HomeDecl_name: Property = Property(name="name", type=StringType)
idl_HomeDecl.attributes={idl_HomeDecl_name}

# idl_EventForwardDcl class attributes and methods

# idl_PortTypeDecl class attributes and methods
idl_PortTypeDecl_name: Property = Property(name="name", type=StringType)
idl_PortTypeDecl.attributes={idl_PortTypeDecl_name}

# idl_PortExport class attributes and methods

# idl_PortDecl class attributes and methods
idl_PortDecl_isMirror: Property = Property(name="isMirror", type=BooleanType)
idl_PortDecl_name: Property = Property(name="name", type=StringType)
idl_PortDecl.attributes={idl_PortDecl_isMirror, idl_PortDecl_name}

# idl_Connector class attributes and methods

# idl_ConnectorHeader class attributes and methods
idl_ConnectorHeader_name: Property = Property(name="name", type=StringType)
idl_ConnectorHeader.attributes={idl_ConnectorHeader_name}

# idl_ConnectorExport class attributes and methods

# idl_StateMember class attributes and methods
idl_StateMember_isPublic: Property = Property(name="isPublic", type=BooleanType)
idl_StateMember_names: Property = Property(name="names", type=StringType)
idl_StateMember.attributes={idl_StateMember_isPublic, idl_StateMember_names}

# idl_TypenameParamType class attributes and methods

# idl_InterfaceParamType class attributes and methods

# idl_ValuetypeParamType class attributes and methods

# idl_EventParamType class attributes and methods

# idl_StructParamType class attributes and methods

# idl_UnionParamType class attributes and methods

# idl_ExceptionParamType class attributes and methods

# idl_EnumParamType class attributes and methods

# idl_SequenceParamType class attributes and methods

# idl_ConstParamType class attributes and methods

# idl_FixedModule class attributes and methods
idl_FixedModule_name: Property = Property(name="name", type=StringType)
idl_FixedModule.attributes={idl_FixedModule_name}

# idl_FixedDefinition class attributes and methods

# idl_TemplateModuleInst class attributes and methods
idl_TemplateModuleInst_name: Property = Property(name="name", type=StringType)
idl_TemplateModuleInst.attributes={idl_TemplateModuleInst_name}

# idl_ActualParameter class attributes and methods

# idl_TemplateModuleRef class attributes and methods
idl_TemplateModuleRef_id: Property = Property(name="id", type=StringType)
idl_TemplateModuleRef_name: Property = Property(name="name", type=StringType)
idl_TemplateModuleRef.attributes={idl_TemplateModuleRef_name, idl_TemplateModuleRef_id}

# idl_TemplateModule class attributes and methods
idl_TemplateModule_name: Property = Property(name="name", type=StringType)
idl_TemplateModule.attributes={idl_TemplateModule_name}

# idl_FormalParameter class attributes and methods
idl_FormalParameter_name: Property = Property(name="name", type=StringType)
idl_FormalParameter.attributes={idl_FormalParameter_name}

# idl_TemplateDefinition class attributes and methods

# idl_FormalParameterType class attributes and methods

# Relationships
value3: BinaryAssociation = BinaryAssociation(
    name="value3",
    ends={
        Property(name="idl_FileName", type=idl_Preproc_Include, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_Preproc_Include", type=idl_FileName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value4: BinaryAssociation = BinaryAssociation(
    name="value4",
    ends={
        Property(name="idl_Preproc_If_Compare", type=idl_Preproc_If, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_Preproc_If", type=idl_Preproc_If_Compare, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
lhs5: BinaryAssociation = BinaryAssociation(
    name="lhs5",
    ends={
        Property(name="idl_Preproc_If_Val", type=idl_Preproc_If_Compare, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_Preproc_If_Compare6", type=idl_Preproc_If_Val, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rhs7: BinaryAssociation = BinaryAssociation(
    name="rhs7",
    ends={
        Property(name="idl_Preproc_If_Val9", type=idl_Preproc_If_Compare, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_Preproc_If_Compare8", type=idl_Preproc_If_Val, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value10: BinaryAssociation = BinaryAssociation(
    name="value10",
    ends={
        Property(name="idl_ConstExp", type=idl_Preproc_If_Val, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_Preproc_If_Val11", type=idl_ConstExp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
imports0: BinaryAssociation = BinaryAssociation(
    name="imports0",
    ends={
        Property(name="idl_Import_decl", type=idl_Specification, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_Specification", type=idl_Import_decl, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
definitions1: BinaryAssociation = BinaryAssociation(
    name="definitions1",
    ends={
        Property(name="idl_Definition", type=idl_Specification, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_Specification2", type=idl_Definition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exp12: BinaryAssociation = BinaryAssociation(
    name="exp12",
    ends={
        Property(name="idl_ConstExp13", type=idl_Preproc_Define, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_Preproc_Define", type=idl_ConstExp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
comments14: BinaryAssociation = BinaryAssociation(
    name="comments14",
    ends={
        Property(name="idl_IDLComment", type=idl_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_Module", type=idl_IDLComment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
definitions15: BinaryAssociation = BinaryAssociation(
    name="definitions15",
    ends={
        Property(name="idl_Definition17", type=idl_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_Module16", type=idl_Definition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
header18: BinaryAssociation = BinaryAssociation(
    name="header18",
    ends={
        Property(name="idl_Interface_header", type=idl_Interface_decl, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_Interface_decl", type=idl_Interface_header, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
interfaceBody19: BinaryAssociation = BinaryAssociation(
    name="interfaceBody19",
    ends={
        Property(name="idl_InterfaceBody", type=idl_Interface_decl, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_Interface_decl20", type=idl_InterfaceBody, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
specializes21: BinaryAssociation = BinaryAssociation(
    name="specializes21",
    ends={
        Property(name="idl_ScopedName", type=idl_Interface_header, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_Interface_header22", type=idl_ScopedName, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
comments23: BinaryAssociation = BinaryAssociation(
    name="comments23",
    ends={
        Property(name="idl_IDLComment25", type=idl_Interface_header, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_Interface_header24", type=idl_IDLComment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
export26: BinaryAssociation = BinaryAssociation(
    name="export26",
    ends={
        Property(name="idl_Export", type=idl_InterfaceBody, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_InterfaceBody27", type=idl_Export, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
comments28: BinaryAssociation = BinaryAssociation(
    name="comments28",
    ends={
        Property(name="idl_IDLComment29", type=idl_AttrDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_AttrDecl", type=idl_IDLComment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type30: BinaryAssociation = BinaryAssociation(
    name="type30",
    ends={
        Property(name="idl_ParamTypeSpec", type=idl_AttrDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_AttrDecl31", type=idl_ParamTypeSpec, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
getRaises32: BinaryAssociation = BinaryAssociation(
    name="getRaises32",
    ends={
        Property(name="idl_AttrRaisesExpr", type=idl_AttrSpec, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_AttrSpec", type=idl_AttrRaisesExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
setRaises33: BinaryAssociation = BinaryAssociation(
    name="setRaises33",
    ends={
        Property(name="idl_AttrRaisesExpr35", type=idl_AttrSpec, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_AttrSpec34", type=idl_AttrRaisesExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
raises36: BinaryAssociation = BinaryAssociation(
    name="raises36",
    ends={
        Property(name="idl_AttrRaisesExpr37", type=idl_ReadOnlyAttrSpec, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_ReadOnlyAttrSpec", type=idl_AttrRaisesExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exception40: BinaryAssociation = BinaryAssociation(
    name="exception40",
    ends={
        Property(name="idl_ScopedName42", type=idl_ExceptionList, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_ExceptionList41", type=idl_ScopedName, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
comments43: BinaryAssociation = BinaryAssociation(
    name="comments43",
    ends={
        Property(name="idl_IDLComment44", type=idl_OpDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_OpDecl", type=idl_IDLComment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type45: BinaryAssociation = BinaryAssociation(
    name="type45",
    ends={
        Property(name="idl_OpTypeDecl", type=idl_OpDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_OpDecl46", type=idl_OpTypeDecl, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
params47: BinaryAssociation = BinaryAssociation(
    name="params47",
    ends={
        Property(name="idl_ParameterDecls", type=idl_OpDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_OpDecl48", type=idl_ParameterDecls, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
raises49: BinaryAssociation = BinaryAssociation(
    name="raises49",
    ends={
        Property(name="idl_ExceptionList51", type=idl_OpDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_OpDecl50", type=idl_ExceptionList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
context52: BinaryAssociation = BinaryAssociation(
    name="context52",
    ends={
        Property(name="idl_ContextExpr", type=idl_OpDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_OpDecl53", type=idl_ContextExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
comments54: BinaryAssociation = BinaryAssociation(
    name="comments54",
    ends={
        Property(name="idl_IDLComment56", type=idl_ParameterDecls, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_ParameterDecls55", type=idl_IDLComment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
decls57: BinaryAssociation = BinaryAssociation(
    name="decls57",
    ends={
        Property(name="idl_ParamDcl", type=idl_ParameterDecls, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_ParameterDecls58", type=idl_ParamDcl, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type59: BinaryAssociation = BinaryAssociation(
    name="type59",
    ends={
        Property(name="idl_ParamTypeSpec61", type=idl_ParamDcl, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_ParamDcl60", type=idl_ParamTypeSpec, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exceptions38: BinaryAssociation = BinaryAssociation(
    name="exceptions38",
    ends={
        Property(name="idl_ExceptionList", type=idl_AttrRaisesExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_AttrRaisesExpr39", type=idl_ExceptionList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
comments65: BinaryAssociation = BinaryAssociation(
    name="comments65",
    ends={
        Property(name="idl_IDLComment66", type=idl_ExceptDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_ExceptDecl", type=idl_IDLComment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
members67: BinaryAssociation = BinaryAssociation(
    name="members67",
    ends={
        Property(name="idl_Member", type=idl_ExceptDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_ExceptDecl68", type=idl_Member, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type69: BinaryAssociation = BinaryAssociation(
    name="type69",
    ends={
        Property(name="idl_TypeSpec", type=idl_Member, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_Member70", type=idl_TypeSpec, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
decl71: BinaryAssociation = BinaryAssociation(
    name="decl71",
    ends={
        Property(name="idl_Declarator", type=idl_Member, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_Member72", type=idl_Declarator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
comment73: BinaryAssociation = BinaryAssociation(
    name="comment73",
    ends={
        Property(name="idl_IDLComment75", type=idl_Member, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_Member74", type=idl_IDLComment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
size76: BinaryAssociation = BinaryAssociation(
    name="size76",
    ends={
        Property(name="idl_ConstExp77", type=idl_ArrayDeclarator, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_ArrayDeclarator", type=idl_ConstExp, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
comments78: BinaryAssociation = BinaryAssociation(
    name="comments78",
    ends={
        Property(name="idl_IDLComment79", type=idl_StructType, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_StructType", type=idl_IDLComment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
members80: BinaryAssociation = BinaryAssociation(
    name="members80",
    ends={
        Property(name="idl_Member82", type=idl_StructType, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_StructType81", type=idl_Member, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
size62: BinaryAssociation = BinaryAssociation(
    name="size62",
    ends={
        Property(name="idl_PositiveIntConst", type=idl_StringType, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_StringType", type=idl_PositiveIntConst, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
size63: BinaryAssociation = BinaryAssociation(
    name="size63",
    ends={
        Property(name="idl_PositiveIntConst64", type=idl_WideStringType, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_WideStringType", type=idl_PositiveIntConst, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
comments91: BinaryAssociation = BinaryAssociation(
    name="comments91",
    ends={
        Property(name="idl_IDLComment92", type=idl_UnionType, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_UnionType", type=idl_IDLComment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
switch93: BinaryAssociation = BinaryAssociation(
    name="switch93",
    ends={
        Property(name="idl_SwitchTypeSpec", type=idl_UnionType, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_UnionType94", type=idl_SwitchTypeSpec, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body95: BinaryAssociation = BinaryAssociation(
    name="body95",
    ends={
        Property(name="idl_SwitchBody", type=idl_UnionType, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_UnionType96", type=idl_SwitchBody, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
case97: BinaryAssociation = BinaryAssociation(
    name="case97",
    ends={
        Property(name="idl_Case", type=idl_SwitchBody, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_SwitchBody98", type=idl_Case, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
comments99: BinaryAssociation = BinaryAssociation(
    name="comments99",
    ends={
        Property(name="idl_IDLComment101", type=idl_Case, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_Case100", type=idl_IDLComment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
label102: BinaryAssociation = BinaryAssociation(
    name="label102",
    ends={
        Property(name="idl_CaseLabel", type=idl_Case, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_Case103", type=idl_CaseLabel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
spec104: BinaryAssociation = BinaryAssociation(
    name="spec104",
    ends={
        Property(name="idl_ElementSpec", type=idl_Case, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_Case105", type=idl_ElementSpec, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constExp106: BinaryAssociation = BinaryAssociation(
    name="constExp106",
    ends={
        Property(name="idl_ConstExp108", type=idl_CaseLabel, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_CaseLabel107", type=idl_ConstExp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type109: BinaryAssociation = BinaryAssociation(
    name="type109",
    ends={
        Property(name="idl_TypeSpec111", type=idl_ElementSpec, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_ElementSpec110", type=idl_TypeSpec, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declarator112: BinaryAssociation = BinaryAssociation(
    name="declarator112",
    ends={
        Property(name="idl_Declarator114", type=idl_ElementSpec, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_ElementSpec113", type=idl_Declarator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
comments83: BinaryAssociation = BinaryAssociation(
    name="comments83",
    ends={
        Property(name="idl_IDLComment84", type=idl_TypeDeclarator, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_TypeDeclarator", type=idl_IDLComment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type85: BinaryAssociation = BinaryAssociation(
    name="type85",
    ends={
        Property(name="idl_TypeSpec87", type=idl_TypeDeclarator, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_TypeDeclarator86", type=idl_TypeSpec, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declarators88: BinaryAssociation = BinaryAssociation(
    name="declarators88",
    ends={
        Property(name="idl_Declarator90", type=idl_TypeDeclarator, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_TypeDeclarator89", type=idl_Declarator, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
lower121: BinaryAssociation = BinaryAssociation(
    name="lower121",
    ends={
        Property(name="idl_PositiveIntConst122", type=idl_FixedPtType, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_FixedPtType", type=idl_PositiveIntConst, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
upper123: BinaryAssociation = BinaryAssociation(
    name="upper123",
    ends={
        Property(name="idl_PositiveIntConst125", type=idl_FixedPtType, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_FixedPtType124", type=idl_PositiveIntConst, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp126: BinaryAssociation = BinaryAssociation(
    name="exp126",
    ends={
        Property(name="idl_ConstExp128", type=idl_PositiveIntConst, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_PositiveIntConst127", type=idl_ConstExp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type129: BinaryAssociation = BinaryAssociation(
    name="type129",
    ends={
        Property(name="idl_ConstType", type=idl_ConstDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_ConstDecl", type=idl_ConstType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value130: BinaryAssociation = BinaryAssociation(
    name="value130",
    ends={
        Property(name="idl_ConstExp132", type=idl_ConstDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_ConstDecl131", type=idl_ConstExp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
comments133: BinaryAssociation = BinaryAssociation(
    name="comments133",
    ends={
        Property(name="idl_IDLComment135", type=idl_ConstDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_ConstDecl134", type=idl_IDLComment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
lhs136: BinaryAssociation = BinaryAssociation(
    name="lhs136",
    ends={
        Property(name="idl_XOrExpr", type=idl_OrExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_OrExpr", type=idl_XOrExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rhs138: BinaryAssociation = BinaryAssociation(
    name="rhs138",
    ends={
        Property(name="idl_OrExpr139", type=idl_OrExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_OrExpr137", type=idl_OrExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
comments115: BinaryAssociation = BinaryAssociation(
    name="comments115",
    ends={
        Property(name="idl_IDLComment116", type=idl_EnumType, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_EnumType", type=idl_IDLComment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type117: BinaryAssociation = BinaryAssociation(
    name="type117",
    ends={
        Property(name="idl_SimpleTypeSpec", type=idl_SequenceType, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_SequenceType", type=idl_SimpleTypeSpec, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
size118: BinaryAssociation = BinaryAssociation(
    name="size118",
    ends={
        Property(name="idl_PositiveIntConst120", type=idl_SequenceType, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_SequenceType119", type=idl_PositiveIntConst, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lhs150: BinaryAssociation = BinaryAssociation(
    name="lhs150",
    ends={
        Property(name="idl_AddExpr", type=idl_ShiftExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_ShiftExpr151", type=idl_AddExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rhs153: BinaryAssociation = BinaryAssociation(
    name="rhs153",
    ends={
        Property(name="idl_ShiftExpr154", type=idl_ShiftExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_ShiftExpr152", type=idl_ShiftExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lhs155: BinaryAssociation = BinaryAssociation(
    name="lhs155",
    ends={
        Property(name="idl_MultExpr", type=idl_AddExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_AddExpr156", type=idl_MultExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rhs158: BinaryAssociation = BinaryAssociation(
    name="rhs158",
    ends={
        Property(name="idl_AddExpr159", type=idl_AddExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_AddExpr157", type=idl_AddExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lhs160: BinaryAssociation = BinaryAssociation(
    name="lhs160",
    ends={
        Property(name="idl_UnaryExpr", type=idl_MultExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_MultExpr161", type=idl_UnaryExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rhs163: BinaryAssociation = BinaryAssociation(
    name="rhs163",
    ends={
        Property(name="idl_MultExpr164", type=idl_MultExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_MultExpr162", type=idl_MultExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr165: BinaryAssociation = BinaryAssociation(
    name="expr165",
    ends={
        Property(name="idl_PrimaryExpr", type=idl_UnaryExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_UnaryExpr166", type=idl_PrimaryExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
comments167: BinaryAssociation = BinaryAssociation(
    name="comments167",
    ends={
        Property(name="idl_IDLComment168", type=idl_ComponentDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_ComponentDecl", type=idl_IDLComment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
base169: BinaryAssociation = BinaryAssociation(
    name="base169",
    ends={
        Property(name="idl_ScopedName171", type=idl_ComponentDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_ComponentDecl170", type=idl_ScopedName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lhs140: BinaryAssociation = BinaryAssociation(
    name="lhs140",
    ends={
        Property(name="idl_AndExpr", type=idl_XOrExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_XOrExpr141", type=idl_AndExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rhs143: BinaryAssociation = BinaryAssociation(
    name="rhs143",
    ends={
        Property(name="idl_XOrExpr144", type=idl_XOrExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_XOrExpr142", type=idl_XOrExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lhs145: BinaryAssociation = BinaryAssociation(
    name="lhs145",
    ends={
        Property(name="idl_ShiftExpr", type=idl_AndExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_AndExpr146", type=idl_ShiftExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rhs148: BinaryAssociation = BinaryAssociation(
    name="rhs148",
    ends={
        Property(name="idl_AndExpr149", type=idl_AndExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_AndExpr147", type=idl_AndExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type182: BinaryAssociation = BinaryAssociation(
    name="type182",
    ends={
        Property(name="idl_ScopedName183", type=idl_UsesDcl, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_UsesDcl", type=idl_ScopedName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
comments184: BinaryAssociation = BinaryAssociation(
    name="comments184",
    ends={
        Property(name="idl_IDLComment186", type=idl_UsesDcl, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_UsesDcl185", type=idl_IDLComment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type187: BinaryAssociation = BinaryAssociation(
    name="type187",
    ends={
        Property(name="idl_ScopedName188", type=idl_PublishesDcl, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_PublishesDcl", type=idl_ScopedName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
comments189: BinaryAssociation = BinaryAssociation(
    name="comments189",
    ends={
        Property(name="idl_IDLComment191", type=idl_PublishesDcl, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_PublishesDcl190", type=idl_IDLComment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type192: BinaryAssociation = BinaryAssociation(
    name="type192",
    ends={
        Property(name="idl_ScopedName193", type=idl_EmitDcl, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_EmitDcl", type=idl_ScopedName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
comments194: BinaryAssociation = BinaryAssociation(
    name="comments194",
    ends={
        Property(name="idl_IDLComment196", type=idl_EmitDcl, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_EmitDcl195", type=idl_IDLComment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type197: BinaryAssociation = BinaryAssociation(
    name="type197",
    ends={
        Property(name="idl_ScopedName198", type=idl_ConsumesDcl, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_ConsumesDcl", type=idl_ScopedName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
comments199: BinaryAssociation = BinaryAssociation(
    name="comments199",
    ends={
        Property(name="idl_IDLComment201", type=idl_ConsumesDcl, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_ConsumesDcl200", type=idl_IDLComment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
supports172: BinaryAssociation = BinaryAssociation(
    name="supports172",
    ends={
        Property(name="idl_ScopedName174", type=idl_ComponentDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_ComponentDecl173", type=idl_ScopedName, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
export175: BinaryAssociation = BinaryAssociation(
    name="export175",
    ends={
        Property(name="idl_ComponentExport", type=idl_ComponentDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_ComponentDecl176", type=idl_ComponentExport, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type177: BinaryAssociation = BinaryAssociation(
    name="type177",
    ends={
        Property(name="idl_ScopedName178", type=idl_ProvidesDcl, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_ProvidesDcl", type=idl_ScopedName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
comments179: BinaryAssociation = BinaryAssociation(
    name="comments179",
    ends={
        Property(name="idl_IDLComment181", type=idl_ProvidesDcl, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_ProvidesDcl180", type=idl_IDLComment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
manages210: BinaryAssociation = BinaryAssociation(
    name="manages210",
    ends={
        Property(name="idl_ScopedName212", type=idl_HomeDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_HomeDecl211", type=idl_ScopedName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
primary_key213: BinaryAssociation = BinaryAssociation(
    name="primary_key213",
    ends={
        Property(name="idl_PrimaryKeySpec", type=idl_HomeDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_HomeDecl214", type=idl_PrimaryKeySpec, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
export215: BinaryAssociation = BinaryAssociation(
    name="export215",
    ends={
        Property(name="idl_HomeExport", type=idl_HomeDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_HomeDecl216", type=idl_HomeExport, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
key217: BinaryAssociation = BinaryAssociation(
    name="key217",
    ends={
        Property(name="idl_ScopedName219", type=idl_PrimaryKeySpec, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_PrimaryKeySpec218", type=idl_ScopedName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
comments220: BinaryAssociation = BinaryAssociation(
    name="comments220",
    ends={
        Property(name="idl_IDLComment221", type=idl_FactoryDcl, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_FactoryDcl", type=idl_IDLComment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
params222: BinaryAssociation = BinaryAssociation(
    name="params222",
    ends={
        Property(name="idl_ParameterDecls224", type=idl_FactoryDcl, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_FactoryDcl223", type=idl_ParameterDecls, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
raises225: BinaryAssociation = BinaryAssociation(
    name="raises225",
    ends={
        Property(name="idl_ExceptionList227", type=idl_FactoryDcl, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_FactoryDcl226", type=idl_ExceptionList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
comments228: BinaryAssociation = BinaryAssociation(
    name="comments228",
    ends={
        Property(name="idl_IDLComment229", type=idl_FinderDcl, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_FinderDcl", type=idl_IDLComment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
params230: BinaryAssociation = BinaryAssociation(
    name="params230",
    ends={
        Property(name="idl_ParameterDecls232", type=idl_FinderDcl, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_FinderDcl231", type=idl_ParameterDecls, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
raises233: BinaryAssociation = BinaryAssociation(
    name="raises233",
    ends={
        Property(name="idl_ExceptionList235", type=idl_FinderDcl, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_FinderDcl234", type=idl_ExceptionList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
comments202: BinaryAssociation = BinaryAssociation(
    name="comments202",
    ends={
        Property(name="idl_IDLComment203", type=idl_HomeDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_HomeDecl", type=idl_IDLComment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
base204: BinaryAssociation = BinaryAssociation(
    name="base204",
    ends={
        Property(name="idl_ScopedName206", type=idl_HomeDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_HomeDecl205", type=idl_ScopedName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
supports207: BinaryAssociation = BinaryAssociation(
    name="supports207",
    ends={
        Property(name="idl_ScopedName209", type=idl_HomeDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_HomeDecl208", type=idl_ScopedName, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type246: BinaryAssociation = BinaryAssociation(
    name="type246",
    ends={
        Property(name="idl_ParamTypeSpec248", type=idl_StateMember, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_StateMember247", type=idl_ParamTypeSpec, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
comments249: BinaryAssociation = BinaryAssociation(
    name="comments249",
    ends={
        Property(name="idl_IDLComment250", type=idl_PortTypeDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_PortTypeDecl", type=idl_IDLComment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exports251: BinaryAssociation = BinaryAssociation(
    name="exports251",
    ends={
        Property(name="idl_PortExport", type=idl_PortTypeDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_PortTypeDecl252", type=idl_PortExport, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type253: BinaryAssociation = BinaryAssociation(
    name="type253",
    ends={
        Property(name="idl_ScopedName254", type=idl_PortDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_PortDecl", type=idl_ScopedName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
comments255: BinaryAssociation = BinaryAssociation(
    name="comments255",
    ends={
        Property(name="idl_IDLComment257", type=idl_PortDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_PortDecl256", type=idl_IDLComment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
header258: BinaryAssociation = BinaryAssociation(
    name="header258",
    ends={
        Property(name="idl_ConnectorHeader", type=idl_Connector, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_Connector", type=idl_ConnectorHeader, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exports259: BinaryAssociation = BinaryAssociation(
    name="exports259",
    ends={
        Property(name="idl_ConnectorExport", type=idl_Connector, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_Connector260", type=idl_ConnectorExport, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
base236: BinaryAssociation = BinaryAssociation(
    name="base236",
    ends={
        Property(name="idl_ScopedName237", type=idl_EventDcl, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_EventDcl", type=idl_ScopedName, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
supports238: BinaryAssociation = BinaryAssociation(
    name="supports238",
    ends={
        Property(name="idl_ScopedName240", type=idl_EventDcl, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_EventDcl239", type=idl_ScopedName, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
export241: BinaryAssociation = BinaryAssociation(
    name="export241",
    ends={
        Property(name="idl_Export243", type=idl_EventDcl, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_EventDcl242", type=idl_Export, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
member244: BinaryAssociation = BinaryAssociation(
    name="member244",
    ends={
        Property(name="idl_StateMember", type=idl_EventDcl, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_EventDcl245", type=idl_StateMember, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
definitions269: BinaryAssociation = BinaryAssociation(
    name="definitions269",
    ends={
        Property(name="idl_FixedDefinition", type=idl_FixedModule, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_FixedModule", type=idl_FixedDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type270: BinaryAssociation = BinaryAssociation(
    name="type270",
    ends={
        Property(name="idl_ScopedName271", type=idl_TemplateModuleInst, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_TemplateModuleInst", type=idl_ScopedName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameter272: BinaryAssociation = BinaryAssociation(
    name="parameter272",
    ends={
        Property(name="idl_ActualParameter", type=idl_TemplateModuleInst, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_TemplateModuleInst273", type=idl_ActualParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
comments274: BinaryAssociation = BinaryAssociation(
    name="comments274",
    ends={
        Property(name="idl_IDLComment276", type=idl_TemplateModuleInst, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_TemplateModuleInst275", type=idl_IDLComment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type277: BinaryAssociation = BinaryAssociation(
    name="type277",
    ends={
        Property(name="idl_ScopedName278", type=idl_TemplateModuleRef, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_TemplateModuleRef", type=idl_ScopedName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
base261: BinaryAssociation = BinaryAssociation(
    name="base261",
    ends={
        Property(name="idl_ScopedName263", type=idl_ConnectorHeader, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_ConnectorHeader262", type=idl_ScopedName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters264: BinaryAssociation = BinaryAssociation(
    name="parameters264",
    ends={
        Property(name="idl_FormalParameter", type=idl_TemplateModule, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_TemplateModule", type=idl_FormalParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
definitions265: BinaryAssociation = BinaryAssociation(
    name="definitions265",
    ends={
        Property(name="idl_TemplateDefinition", type=idl_TemplateModule, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_TemplateModule266", type=idl_TemplateDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type267: BinaryAssociation = BinaryAssociation(
    name="type267",
    ends={
        Property(name="idl_FormalParameterType", type=idl_FormalParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="idl_FormalParameter268", type=idl_FormalParameterType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_idl_Preproc_ComponentExport = Generalization(general=ComponentExport, specific=idl_Preproc)
gen_idl_Preproc_Include_Preproc = Generalization(general=Preproc, specific=idl_Preproc_Include)
gen_idl_Preproc_Ifdef_Preproc = Generalization(general=Preproc, specific=idl_Preproc_Ifdef)
gen_idl_Preproc_Ifndef_Preproc = Generalization(general=Preproc, specific=idl_Preproc_Ifndef)
gen_idl_Preproc_Undef_Preproc = Generalization(general=Preproc, specific=idl_Preproc_Undef)
gen_idl_Preproc_If_Preproc = Generalization(general=Preproc, specific=idl_Preproc_If)
gen_idl_Preproc_Else_Preproc = Generalization(general=Preproc, specific=idl_Preproc_Else)
gen_idl_Preproc_Error_Preproc = Generalization(general=Preproc, specific=idl_Preproc_Error)
gen_idl_Preproc_Definition = Generalization(general=Definition, specific=idl_Preproc)
gen_idl_Preproc_Export = Generalization(general=Export, specific=idl_Preproc)
gen_idl_Preproc_Pragma_Prefix_Preproc_Pragma = Generalization(general=Preproc_Pragma, specific=idl_Preproc_Pragma_Prefix)
gen_idl_Preproc_Pragma_Ciao_Lem_Preproc_Pragma = Generalization(general=Preproc_Pragma, specific=idl_Preproc_Pragma_Ciao_Lem)
gen_idl_Preproc_Pragma_Ciao_Ami4ccm_Interface_Preproc_Pragma = Generalization(general=Preproc_Pragma, specific=idl_Preproc_Pragma_Ciao_Ami4ccm_Interface)
gen_idl_Preproc_Pragma_Ciao_Ami4ccm_Receptacle_Preproc_Pragma = Generalization(general=Preproc_Pragma, specific=idl_Preproc_Pragma_Ciao_Ami4ccm_Receptacle)
gen_idl_Preproc_Pragma_Ciao_Ami4ccm_Idl_Preproc_Pragma = Generalization(general=Preproc_Pragma, specific=idl_Preproc_Pragma_Ciao_Ami4ccm_Idl)
gen_idl_Preproc_Pragma_Ndds_Preproc_Pragma = Generalization(general=Preproc_Pragma, specific=idl_Preproc_Pragma_Ndds)
gen_idl_Preproc_Pragma_Component_Preproc_Pragma = Generalization(general=Preproc_Pragma, specific=idl_Preproc_Pragma_Component)
gen_idl_Preproc_Pragma_Home_Preproc_Pragma = Generalization(general=Preproc_Pragma, specific=idl_Preproc_Pragma_Home)
gen_idl_Preproc_Pragma_DDS4CCM_Impl_Preproc_Pragma = Generalization(general=Preproc_Pragma, specific=idl_Preproc_Pragma_DDS4CCM_Impl)
gen_idl_Preproc_Define_Preproc = Generalization(general=Preproc, specific=idl_Preproc_Define)
gen_idl_Preproc_Endif_Preproc = Generalization(general=Preproc, specific=idl_Preproc_Endif)
gen_idl_Preproc_Pragma_Preproc = Generalization(general=Preproc, specific=idl_Preproc_Pragma)
gen_idl_Interface_or_Forward_Decl_Definition = Generalization(general=Definition, specific=idl_Interface_or_Forward_Decl)
gen_idl_Interface_decl_Interface_or_Forward_Decl = Generalization(general=Interface_or_Forward_Decl, specific=idl_Interface_decl)
gen_idl_Interface_decl_TemplateDefinition = Generalization(general=TemplateDefinition, specific=idl_Interface_decl)
gen_idl_Interface_decl_FixedDefinition = Generalization(general=FixedDefinition, specific=idl_Interface_decl)
gen_idl_Forward_decl_Interface_or_Forward_Decl = Generalization(general=Interface_or_Forward_Decl, specific=idl_Forward_decl)
gen_idl_Export_HomeExport = Generalization(general=HomeExport, specific=idl_Export)
gen_idl_AttrDecl_Export = Generalization(general=Export, specific=idl_AttrDecl)
gen_idl_AttrDecl_ComponentExport = Generalization(general=ComponentExport, specific=idl_AttrDecl)
gen_idl_AttrDecl_PortExport = Generalization(general=PortExport, specific=idl_AttrDecl)
gen_idl_AttrDecl_ConnectorExport = Generalization(general=ConnectorExport, specific=idl_AttrDecl)
gen_idl_AttrSpec_AttrDecl = Generalization(general=AttrDecl, specific=idl_AttrSpec)
gen_idl_ReadOnlyAttrSpec_AttrDecl = Generalization(general=AttrDecl, specific=idl_ReadOnlyAttrSpec)
gen_idl_Preproc_Pragma_Misc_Preproc_Pragma = Generalization(general=Preproc_Pragma, specific=idl_Preproc_Pragma_Misc)
gen_idl_File_Marker_Preproc = Generalization(general=Preproc, specific=idl_File_Marker)
gen_idl_Excluded_File_Marker_Preproc = Generalization(general=Preproc, specific=idl_Excluded_File_Marker)
gen_idl_Module_Definition = Generalization(general=Definition, specific=idl_Module)
gen_idl_OpDecl_Export = Generalization(general=Export, specific=idl_OpDecl)
gen_idl_FloatType_FloatingPtType = Generalization(general=FloatingPtType, specific=idl_FloatType)
gen_idl_DoubleType_FloatingPtType = Generalization(general=FloatingPtType, specific=idl_DoubleType)
gen_idl_LongDoubleType_FloatingPtType = Generalization(general=FloatingPtType, specific=idl_LongDoubleType)
gen_idl_IntegerType_BaseTypeSpec = Generalization(general=BaseTypeSpec, specific=idl_IntegerType)
gen_idl_IntegerType_SwitchTypeSpec = Generalization(general=SwitchTypeSpec, specific=idl_IntegerType)
gen_idl_IntegerType_ConstType = Generalization(general=ConstType, specific=idl_IntegerType)
gen_idl_SignedInt_IntegerType = Generalization(general=IntegerType, specific=idl_SignedInt)
gen_idl_SignedShortInt_SignedInt = Generalization(general=SignedInt, specific=idl_SignedShortInt)
gen_idl_SignedLongInt_SignedInt = Generalization(general=SignedInt, specific=idl_SignedLongInt)
gen_idl_SignedLongLongInt_SignedInt = Generalization(general=SignedInt, specific=idl_SignedLongLongInt)
gen_idl_UnsignedInt_IntegerType = Generalization(general=IntegerType, specific=idl_UnsignedInt)
gen_idl_UnsignedShortInt_UnsignedInt = Generalization(general=UnsignedInt, specific=idl_UnsignedShortInt)
gen_idl_UnsignedLongInt_UnsignedInt = Generalization(general=UnsignedInt, specific=idl_UnsignedLongInt)
gen_idl_UnsignedLongLongInt_UnsignedInt = Generalization(general=UnsignedInt, specific=idl_UnsignedLongLongInt)
gen_idl_CharType_BaseTypeSpec = Generalization(general=BaseTypeSpec, specific=idl_CharType)
gen_idl_CharType_SwitchTypeSpec = Generalization(general=SwitchTypeSpec, specific=idl_CharType)
gen_idl_CharType_ConstType = Generalization(general=ConstType, specific=idl_CharType)
gen_idl_WideCharType_BaseTypeSpec = Generalization(general=BaseTypeSpec, specific=idl_WideCharType)
gen_idl_WideCharType_ConstType = Generalization(general=ConstType, specific=idl_WideCharType)
gen_idl_BooleanType_BaseTypeSpec = Generalization(general=BaseTypeSpec, specific=idl_BooleanType)
gen_idl_BooleanType_SwitchTypeSpec = Generalization(general=SwitchTypeSpec, specific=idl_BooleanType)
gen_idl_BooleanType_ConstType = Generalization(general=ConstType, specific=idl_BooleanType)
gen_idl_ParamTypeSpec_OpTypeDecl = Generalization(general=OpTypeDecl, specific=idl_ParamTypeSpec)
gen_idl_ScopedName_ParamTypeSpec = Generalization(general=ParamTypeSpec, specific=idl_ScopedName)
gen_idl_ScopedName_SimpleTypeSpec = Generalization(general=SimpleTypeSpec, specific=idl_ScopedName)
gen_idl_ScopedName_SwitchTypeSpec = Generalization(general=SwitchTypeSpec, specific=idl_ScopedName)
gen_idl_ScopedName_ConstType = Generalization(general=ConstType, specific=idl_ScopedName)
gen_idl_ScopedName_PrimaryExpr = Generalization(general=PrimaryExpr, specific=idl_ScopedName)
gen_idl_BaseTypeSpec_ParamTypeSpec = Generalization(general=ParamTypeSpec, specific=idl_BaseTypeSpec)
gen_idl_BaseTypeSpec_SimpleTypeSpec = Generalization(general=SimpleTypeSpec, specific=idl_BaseTypeSpec)
gen_idl_FloatingPtType_BaseTypeSpec = Generalization(general=BaseTypeSpec, specific=idl_FloatingPtType)
gen_idl_FloatingPtType_ConstType = Generalization(general=ConstType, specific=idl_FloatingPtType)
gen_idl_ExceptDecl_Export = Generalization(general=Export, specific=idl_ExceptDecl)
gen_idl_ExceptDecl_TemplateDefinition = Generalization(general=TemplateDefinition, specific=idl_ExceptDecl)
gen_idl_ExceptDecl_FixedDefinition = Generalization(general=FixedDefinition, specific=idl_ExceptDecl)
gen_idl_SimpleDeclarator_Declarator = Generalization(general=Declarator, specific=idl_SimpleDeclarator)
gen_idl_ArrayDeclarator_Declarator = Generalization(general=Declarator, specific=idl_ArrayDeclarator)
gen_idl_ArrayDeclarator_ComplexDeclarator = Generalization(general=ComplexDeclarator, specific=idl_ArrayDeclarator)
gen_idl_StructType_Definition = Generalization(general=Definition, specific=idl_StructType)
gen_idl_StructType_TypeDecl = Generalization(general=TypeDecl, specific=idl_StructType)
gen_idl_StructType_ConstrTypeSpec = Generalization(general=ConstrTypeSpec, specific=idl_StructType)
gen_idl_TypeDecl_Definition = Generalization(general=Definition, specific=idl_TypeDecl)
gen_idl_TypeDecl_Export = Generalization(general=Export, specific=idl_TypeDecl)
gen_idl_TypeDecl_TemplateDefinition = Generalization(general=TemplateDefinition, specific=idl_TypeDecl)
gen_idl_TypeDecl_FixedDefinition = Generalization(general=FixedDefinition, specific=idl_TypeDecl)
gen_idl_TypeDeclarator_TypeDecl = Generalization(general=TypeDecl, specific=idl_TypeDeclarator)
gen_idl_OctetType_BaseTypeSpec = Generalization(general=BaseTypeSpec, specific=idl_OctetType)
gen_idl_OctetType_ConstType = Generalization(general=ConstType, specific=idl_OctetType)
gen_idl_AnyType_BaseTypeSpec = Generalization(general=BaseTypeSpec, specific=idl_AnyType)
gen_idl_ObjectType_BaseTypeSpec = Generalization(general=BaseTypeSpec, specific=idl_ObjectType)
gen_idl_ValueBaseType_BaseTypeSpec = Generalization(general=BaseTypeSpec, specific=idl_ValueBaseType)
gen_idl_StringType_ParamTypeSpec = Generalization(general=ParamTypeSpec, specific=idl_StringType)
gen_idl_StringType_TemplateTypeSpec = Generalization(general=TemplateTypeSpec, specific=idl_StringType)
gen_idl_StringType_ConstType = Generalization(general=ConstType, specific=idl_StringType)
gen_idl_WideStringType_ParamTypeSpec = Generalization(general=ParamTypeSpec, specific=idl_WideStringType)
gen_idl_WideStringType_TemplateTypeSpec = Generalization(general=TemplateTypeSpec, specific=idl_WideStringType)
gen_idl_WideStringType_ConstType = Generalization(general=ConstType, specific=idl_WideStringType)
gen_idl_ExceptDecl_Definition = Generalization(general=Definition, specific=idl_ExceptDecl)
gen_idl_UnionType_TypeDecl = Generalization(general=TypeDecl, specific=idl_UnionType)
gen_idl_UnionType_ConstrTypeSpec = Generalization(general=ConstrTypeSpec, specific=idl_UnionType)
gen_idl_EnumType_TypeDecl = Generalization(general=TypeDecl, specific=idl_EnumType)
gen_idl_EnumType_ConstrTypeSpec = Generalization(general=ConstrTypeSpec, specific=idl_EnumType)
gen_idl_EnumType_SwitchTypeSpec = Generalization(general=SwitchTypeSpec, specific=idl_EnumType)
gen_idl_TypeSpec_ActualParameter = Generalization(general=ActualParameter, specific=idl_TypeSpec)
gen_idl_SimpleTypeSpec_TypeSpec = Generalization(general=TypeSpec, specific=idl_SimpleTypeSpec)
gen_idl_TemplateTypeSpec_SimpleTypeSpec = Generalization(general=SimpleTypeSpec, specific=idl_TemplateTypeSpec)
gen_idl_ConstrTypeSpec_TypeSpec = Generalization(general=TypeSpec, specific=idl_ConstrTypeSpec)
gen_idl_FixedPtType_TemplateTypeSpec = Generalization(general=TemplateTypeSpec, specific=idl_FixedPtType)
gen_idl_ConstrForwardDecl_TypeDecl = Generalization(general=TypeDecl, specific=idl_ConstrForwardDecl)
gen_idl_StructForwardDecl_ConstrForwardDecl = Generalization(general=ConstrForwardDecl, specific=idl_StructForwardDecl)
gen_idl_UnionForwardDecl_ConstrForwardDecl = Generalization(general=ConstrForwardDecl, specific=idl_UnionForwardDecl)
gen_idl_ConstDecl_Definition = Generalization(general=Definition, specific=idl_ConstDecl)
gen_idl_ConstDecl_Export = Generalization(general=Export, specific=idl_ConstDecl)
gen_idl_ConstDecl_TemplateDefinition = Generalization(general=TemplateDefinition, specific=idl_ConstDecl)
gen_idl_ConstDecl_FixedDefinition = Generalization(general=FixedDefinition, specific=idl_ConstDecl)
gen_idl_ConstType_ConstParamType = Generalization(general=ConstParamType, specific=idl_ConstType)
gen_idl_FixedPtConstType_ConstType = Generalization(general=ConstType, specific=idl_FixedPtConstType)
gen_idl_ConstExp_PrimaryExpr = Generalization(general=PrimaryExpr, specific=idl_ConstExp)
gen_idl_ConstExp_ActualParameter = Generalization(general=ActualParameter, specific=idl_ConstExp)
gen_idl_OrExpr_ConstExp = Generalization(general=ConstExp, specific=idl_OrExpr)
gen_idl_SequenceType_TemplateTypeSpec = Generalization(general=TemplateTypeSpec, specific=idl_SequenceType)
gen_idl_SequenceType_FormalParameterType = Generalization(general=FormalParameterType, specific=idl_SequenceType)
gen_idl_NativeType_Definition = Generalization(general=Definition, specific=idl_NativeType)
gen_idl_NativeType_TemplateDefinition = Generalization(general=TemplateDefinition, specific=idl_NativeType)
gen_idl_NativeType_FixedDefinition = Generalization(general=FixedDefinition, specific=idl_NativeType)
gen_idl_Literal_PrimaryExpr = Generalization(general=PrimaryExpr, specific=idl_Literal)
gen_idl_ComponentDecl_Definition = Generalization(general=Definition, specific=idl_ComponentDecl)
gen_idl_ComponentDecl_TemplateDefinition = Generalization(general=TemplateDefinition, specific=idl_ComponentDecl)
gen_idl_ComponentDecl_FixedDefinition = Generalization(general=FixedDefinition, specific=idl_ComponentDecl)
gen_idl_UsesDcl_ComponentExport = Generalization(general=ComponentExport, specific=idl_UsesDcl)
gen_idl_UsesDcl_PortExport = Generalization(general=PortExport, specific=idl_UsesDcl)
gen_idl_UsesDcl_ConnectorExport = Generalization(general=ConnectorExport, specific=idl_UsesDcl)
gen_idl_PublishesDcl_ComponentExport = Generalization(general=ComponentExport, specific=idl_PublishesDcl)
gen_idl_EmitDcl_ComponentExport = Generalization(general=ComponentExport, specific=idl_EmitDcl)
gen_idl_ConsumesDcl_ComponentExport = Generalization(general=ComponentExport, specific=idl_ConsumesDcl)
gen_idl_ComponentForwardDecl_Definition = Generalization(general=Definition, specific=idl_ComponentForwardDecl)
gen_idl_ProvidesDcl_ComponentExport = Generalization(general=ComponentExport, specific=idl_ProvidesDcl)
gen_idl_ProvidesDcl_PortExport = Generalization(general=PortExport, specific=idl_ProvidesDcl)
gen_idl_ProvidesDcl_ConnectorExport = Generalization(general=ConnectorExport, specific=idl_ProvidesDcl)
gen_idl_FactoryDcl_HomeExport = Generalization(general=HomeExport, specific=idl_FactoryDcl)
gen_idl_FinderDcl_HomeExport = Generalization(general=HomeExport, specific=idl_FinderDcl)
gen_idl_Event_Definition = Generalization(general=Definition, specific=idl_Event)
gen_idl_Event_TemplateDefinition = Generalization(general=TemplateDefinition, specific=idl_Event)
gen_idl_Event_FixedDefinition = Generalization(general=FixedDefinition, specific=idl_Event)
gen_idl_HomeDecl_Definition = Generalization(general=Definition, specific=idl_HomeDecl)
gen_idl_HomeDecl_TemplateDefinition = Generalization(general=TemplateDefinition, specific=idl_HomeDecl)
gen_idl_HomeDecl_FixedDefinition = Generalization(general=FixedDefinition, specific=idl_HomeDecl)
gen_idl_EventForwardDcl_Event = Generalization(general=Event, specific=idl_EventForwardDcl)
gen_idl_PortTypeDecl_Definition = Generalization(general=Definition, specific=idl_PortTypeDecl)
gen_idl_PortTypeDecl_TemplateDefinition = Generalization(general=TemplateDefinition, specific=idl_PortTypeDecl)
gen_idl_PortTypeDecl_FixedDefinition = Generalization(general=FixedDefinition, specific=idl_PortTypeDecl)
gen_idl_PortDecl_ComponentExport = Generalization(general=ComponentExport, specific=idl_PortDecl)
gen_idl_PortDecl_ConnectorExport = Generalization(general=ConnectorExport, specific=idl_PortDecl)
gen_idl_Connector_Definition = Generalization(general=Definition, specific=idl_Connector)
gen_idl_Connector_TemplateDefinition = Generalization(general=TemplateDefinition, specific=idl_Connector)
gen_idl_Connector_FixedDefinition = Generalization(general=FixedDefinition, specific=idl_Connector)
gen_idl_EventDcl_Event = Generalization(general=Event, specific=idl_EventDcl)
gen_idl_TypenameParamType_FormalParameterType = Generalization(general=FormalParameterType, specific=idl_TypenameParamType)
gen_idl_InterfaceParamType_FormalParameterType = Generalization(general=FormalParameterType, specific=idl_InterfaceParamType)
gen_idl_ValuetypeParamType_FormalParameterType = Generalization(general=FormalParameterType, specific=idl_ValuetypeParamType)
gen_idl_EventParamType_FormalParameterType = Generalization(general=FormalParameterType, specific=idl_EventParamType)
gen_idl_StructParamType_FormalParameterType = Generalization(general=FormalParameterType, specific=idl_StructParamType)
gen_idl_UnionParamType_FormalParameterType = Generalization(general=FormalParameterType, specific=idl_UnionParamType)
gen_idl_ExceptionParamType_FormalParameterType = Generalization(general=FormalParameterType, specific=idl_ExceptionParamType)
gen_idl_EnumParamType_FormalParameterType = Generalization(general=FormalParameterType, specific=idl_EnumParamType)
gen_idl_SequenceParamType_FormalParameterType = Generalization(general=FormalParameterType, specific=idl_SequenceParamType)
gen_idl_ConstParamType_FormalParameterType = Generalization(general=FormalParameterType, specific=idl_ConstParamType)
gen_idl_FixedModule_TemplateDefinition = Generalization(general=TemplateDefinition, specific=idl_FixedModule)
gen_idl_FixedModule_FixedDefinition = Generalization(general=FixedDefinition, specific=idl_FixedModule)
gen_idl_TemplateModuleInst_Definition = Generalization(general=Definition, specific=idl_TemplateModuleInst)
gen_idl_TemplateModuleRef_TemplateDefinition = Generalization(general=TemplateDefinition, specific=idl_TemplateModuleRef)
gen_idl_TemplateModule_Definition = Generalization(general=Definition, specific=idl_TemplateModule)
gen_idl_IDLComment_Definition = Generalization(general=Definition, specific=idl_IDLComment)
gen_idl_IDLComment_Export = Generalization(general=Export, specific=idl_IDLComment)
gen_idl_IDLComment_ComponentExport = Generalization(general=ComponentExport, specific=idl_IDLComment)
gen_idl_IDLComment_PortExport = Generalization(general=PortExport, specific=idl_IDLComment)
gen_idl_IDLComment_ConnectorExport = Generalization(general=ConnectorExport, specific=idl_IDLComment)
gen_idl_IDLComment_TemplateDefinition = Generalization(general=TemplateDefinition, specific=idl_IDLComment)
gen_idl_IDLComment_FixedDefinition = Generalization(general=FixedDefinition, specific=idl_IDLComment)

# Domain Model
domain_model = DomainModel(
    name="idl",
    types={ComponentExport, idl_Preproc_Include, Preproc, idl_FileName, idl_Preproc_Ifdef, idl_Preproc_Ifndef, idl_Preproc_Undef, idl_Preproc_If, idl_Preproc_If_Compare, idl_Preproc_If_Val, idl_ConstExp, idl_Preproc_Else, idl_Preproc_Error, idl_Specification, idl_Import_decl, idl_Definition, idl_Preproc, Definition, Export, idl_Preproc_Pragma_Prefix, Preproc_Pragma, idl_Preproc_Pragma_Ciao_Lem, idl_Preproc_Pragma_Ciao_Ami4ccm_Interface, idl_Preproc_Pragma_Ciao_Ami4ccm_Receptacle, idl_Preproc_Pragma_Ciao_Ami4ccm_Idl, idl_Preproc_Pragma_Ndds, idl_Preproc_Pragma_Component, idl_Preproc_Pragma_Home, idl_Preproc_Pragma_DDS4CCM_Impl, idl_Preproc_Define, idl_Preproc_Endif, idl_Preproc_Pragma, idl_IDLComment, idl_Interface_or_Forward_Decl, idl_Interface_decl, Interface_or_Forward_Decl, TemplateDefinition, FixedDefinition, idl_Interface_header, idl_InterfaceBody, idl_Forward_decl, idl_ScopedName, idl_Export, HomeExport, idl_AttrDecl, PortExport, ConnectorExport, idl_ParamTypeSpec, idl_AttrSpec, AttrDecl, idl_AttrRaisesExpr, idl_ReadOnlyAttrSpec, idl_Preproc_Pragma_Misc, idl_File_Marker, idl_Excluded_File_Marker, idl_Module, idl_OpDecl, idl_OpTypeDecl, idl_ParameterDecls, idl_ContextExpr, idl_ParamDcl, idl_ExceptionList, idl_DoubleType, idl_LongDoubleType, idl_IntegerType, idl_SignedInt, IntegerType, idl_SignedShortInt, SignedInt, idl_SignedLongInt, idl_SignedLongLongInt, idl_UnsignedInt, idl_UnsignedShortInt, UnsignedInt, idl_UnsignedLongInt, idl_UnsignedLongLongInt, idl_CharType, idl_WideCharType, idl_BooleanType, OpTypeDecl, ParamTypeSpec, SimpleTypeSpec, SwitchTypeSpec, ConstType, PrimaryExpr, idl_BaseTypeSpec, idl_FloatingPtType, BaseTypeSpec, idl_FloatType, FloatingPtType, idl_Member, idl_TypeSpec, idl_Declarator, idl_SimpleDeclarator, Declarator, idl_ComplexDeclarator, idl_ArrayDeclarator, ComplexDeclarator, idl_StructType, TypeDecl, ConstrTypeSpec, idl_TypeDecl, idl_TypeDeclarator, idl_OctetType, idl_AnyType, idl_ObjectType, idl_ValueBaseType, idl_StringType, TemplateTypeSpec, idl_PositiveIntConst, idl_WideStringType, idl_ExceptDecl, idl_UnionType, idl_SwitchTypeSpec, idl_SwitchBody, idl_Case, idl_CaseLabel, idl_ElementSpec, idl_EnumType, ActualParameter, idl_SimpleTypeSpec, TypeSpec, idl_TemplateTypeSpec, idl_ConstrTypeSpec, idl_FixedPtType, idl_ConstrForwardDecl, idl_StructForwardDecl, ConstrForwardDecl, idl_UnionForwardDecl, idl_ConstDecl, idl_ConstType, ConstParamType, idl_FixedPtConstType, idl_OrExpr, ConstExp, idl_XOrExpr, idl_SequenceType, FormalParameterType, idl_NativeType, idl_AddExpr, idl_MultExpr, idl_UnaryExpr, idl_PrimaryExpr, idl_Literal, idl_ComponentDecl, idl_AndExpr, idl_ShiftExpr, idl_UsesDcl, idl_PublishesDcl, idl_EmitDcl, idl_ConsumesDcl, idl_ComponentForwardDecl, idl_ComponentExport, idl_ProvidesDcl, idl_PrimaryKeySpec, idl_HomeExport, idl_FactoryDcl, idl_FinderDcl, idl_Event, idl_EventDcl, Event, idl_HomeDecl, idl_EventForwardDcl, idl_PortTypeDecl, idl_PortExport, idl_PortDecl, idl_Connector, idl_ConnectorHeader, idl_ConnectorExport, idl_StateMember, idl_TypenameParamType, idl_InterfaceParamType, idl_ValuetypeParamType, idl_EventParamType, idl_StructParamType, idl_UnionParamType, idl_ExceptionParamType, idl_EnumParamType, idl_SequenceParamType, idl_ConstParamType, idl_FixedModule, idl_FixedDefinition, idl_TemplateModuleInst, idl_ActualParameter, idl_TemplateModuleRef, idl_TemplateModule, idl_FormalParameter, idl_TemplateDefinition, idl_FormalParameterType, ParamDirection},
    associations={value3, value4, lhs5, rhs7, value10, imports0, definitions1, exp12, comments14, definitions15, header18, interfaceBody19, specializes21, comments23, export26, comments28, type30, getRaises32, setRaises33, raises36, exception40, comments43, type45, params47, raises49, context52, comments54, decls57, type59, exceptions38, comments65, members67, type69, decl71, comment73, size76, comments78, members80, size62, size63, comments91, switch93, body95, case97, comments99, label102, spec104, constExp106, type109, declarator112, comments83, type85, declarators88, lower121, upper123, exp126, type129, value130, comments133, lhs136, rhs138, comments115, type117, size118, lhs150, rhs153, lhs155, rhs158, lhs160, rhs163, expr165, comments167, base169, lhs140, rhs143, lhs145, rhs148, type182, comments184, type187, comments189, type192, comments194, type197, comments199, supports172, export175, type177, comments179, manages210, primary_key213, export215, key217, comments220, params222, raises225, comments228, params230, raises233, comments202, base204, supports207, type246, comments249, exports251, type253, comments255, header258, exports259, base236, supports238, export241, member244, definitions269, type270, parameter272, comments274, type277, base261, parameters264, definitions265, type267},
    generalizations={gen_idl_Preproc_ComponentExport, gen_idl_Preproc_Include_Preproc, gen_idl_Preproc_Ifdef_Preproc, gen_idl_Preproc_Ifndef_Preproc, gen_idl_Preproc_Undef_Preproc, gen_idl_Preproc_If_Preproc, gen_idl_Preproc_Else_Preproc, gen_idl_Preproc_Error_Preproc, gen_idl_Preproc_Definition, gen_idl_Preproc_Export, gen_idl_Preproc_Pragma_Prefix_Preproc_Pragma, gen_idl_Preproc_Pragma_Ciao_Lem_Preproc_Pragma, gen_idl_Preproc_Pragma_Ciao_Ami4ccm_Interface_Preproc_Pragma, gen_idl_Preproc_Pragma_Ciao_Ami4ccm_Receptacle_Preproc_Pragma, gen_idl_Preproc_Pragma_Ciao_Ami4ccm_Idl_Preproc_Pragma, gen_idl_Preproc_Pragma_Ndds_Preproc_Pragma, gen_idl_Preproc_Pragma_Component_Preproc_Pragma, gen_idl_Preproc_Pragma_Home_Preproc_Pragma, gen_idl_Preproc_Pragma_DDS4CCM_Impl_Preproc_Pragma, gen_idl_Preproc_Define_Preproc, gen_idl_Preproc_Endif_Preproc, gen_idl_Preproc_Pragma_Preproc, gen_idl_Interface_or_Forward_Decl_Definition, gen_idl_Interface_decl_Interface_or_Forward_Decl, gen_idl_Interface_decl_TemplateDefinition, gen_idl_Interface_decl_FixedDefinition, gen_idl_Forward_decl_Interface_or_Forward_Decl, gen_idl_Export_HomeExport, gen_idl_AttrDecl_Export, gen_idl_AttrDecl_ComponentExport, gen_idl_AttrDecl_PortExport, gen_idl_AttrDecl_ConnectorExport, gen_idl_AttrSpec_AttrDecl, gen_idl_ReadOnlyAttrSpec_AttrDecl, gen_idl_Preproc_Pragma_Misc_Preproc_Pragma, gen_idl_File_Marker_Preproc, gen_idl_Excluded_File_Marker_Preproc, gen_idl_Module_Definition, gen_idl_OpDecl_Export, gen_idl_FloatType_FloatingPtType, gen_idl_DoubleType_FloatingPtType, gen_idl_LongDoubleType_FloatingPtType, gen_idl_IntegerType_BaseTypeSpec, gen_idl_IntegerType_SwitchTypeSpec, gen_idl_IntegerType_ConstType, gen_idl_SignedInt_IntegerType, gen_idl_SignedShortInt_SignedInt, gen_idl_SignedLongInt_SignedInt, gen_idl_SignedLongLongInt_SignedInt, gen_idl_UnsignedInt_IntegerType, gen_idl_UnsignedShortInt_UnsignedInt, gen_idl_UnsignedLongInt_UnsignedInt, gen_idl_UnsignedLongLongInt_UnsignedInt, gen_idl_CharType_BaseTypeSpec, gen_idl_CharType_SwitchTypeSpec, gen_idl_CharType_ConstType, gen_idl_WideCharType_BaseTypeSpec, gen_idl_WideCharType_ConstType, gen_idl_BooleanType_BaseTypeSpec, gen_idl_BooleanType_SwitchTypeSpec, gen_idl_BooleanType_ConstType, gen_idl_ParamTypeSpec_OpTypeDecl, gen_idl_ScopedName_ParamTypeSpec, gen_idl_ScopedName_SimpleTypeSpec, gen_idl_ScopedName_SwitchTypeSpec, gen_idl_ScopedName_ConstType, gen_idl_ScopedName_PrimaryExpr, gen_idl_BaseTypeSpec_ParamTypeSpec, gen_idl_BaseTypeSpec_SimpleTypeSpec, gen_idl_FloatingPtType_BaseTypeSpec, gen_idl_FloatingPtType_ConstType, gen_idl_ExceptDecl_Export, gen_idl_ExceptDecl_TemplateDefinition, gen_idl_ExceptDecl_FixedDefinition, gen_idl_SimpleDeclarator_Declarator, gen_idl_ArrayDeclarator_Declarator, gen_idl_ArrayDeclarator_ComplexDeclarator, gen_idl_StructType_Definition, gen_idl_StructType_TypeDecl, gen_idl_StructType_ConstrTypeSpec, gen_idl_TypeDecl_Definition, gen_idl_TypeDecl_Export, gen_idl_TypeDecl_TemplateDefinition, gen_idl_TypeDecl_FixedDefinition, gen_idl_TypeDeclarator_TypeDecl, gen_idl_OctetType_BaseTypeSpec, gen_idl_OctetType_ConstType, gen_idl_AnyType_BaseTypeSpec, gen_idl_ObjectType_BaseTypeSpec, gen_idl_ValueBaseType_BaseTypeSpec, gen_idl_StringType_ParamTypeSpec, gen_idl_StringType_TemplateTypeSpec, gen_idl_StringType_ConstType, gen_idl_WideStringType_ParamTypeSpec, gen_idl_WideStringType_TemplateTypeSpec, gen_idl_WideStringType_ConstType, gen_idl_ExceptDecl_Definition, gen_idl_UnionType_TypeDecl, gen_idl_UnionType_ConstrTypeSpec, gen_idl_EnumType_TypeDecl, gen_idl_EnumType_ConstrTypeSpec, gen_idl_EnumType_SwitchTypeSpec, gen_idl_TypeSpec_ActualParameter, gen_idl_SimpleTypeSpec_TypeSpec, gen_idl_TemplateTypeSpec_SimpleTypeSpec, gen_idl_ConstrTypeSpec_TypeSpec, gen_idl_FixedPtType_TemplateTypeSpec, gen_idl_ConstrForwardDecl_TypeDecl, gen_idl_StructForwardDecl_ConstrForwardDecl, gen_idl_UnionForwardDecl_ConstrForwardDecl, gen_idl_ConstDecl_Definition, gen_idl_ConstDecl_Export, gen_idl_ConstDecl_TemplateDefinition, gen_idl_ConstDecl_FixedDefinition, gen_idl_ConstType_ConstParamType, gen_idl_FixedPtConstType_ConstType, gen_idl_ConstExp_PrimaryExpr, gen_idl_ConstExp_ActualParameter, gen_idl_OrExpr_ConstExp, gen_idl_SequenceType_TemplateTypeSpec, gen_idl_SequenceType_FormalParameterType, gen_idl_NativeType_Definition, gen_idl_NativeType_TemplateDefinition, gen_idl_NativeType_FixedDefinition, gen_idl_Literal_PrimaryExpr, gen_idl_ComponentDecl_Definition, gen_idl_ComponentDecl_TemplateDefinition, gen_idl_ComponentDecl_FixedDefinition, gen_idl_UsesDcl_ComponentExport, gen_idl_UsesDcl_PortExport, gen_idl_UsesDcl_ConnectorExport, gen_idl_PublishesDcl_ComponentExport, gen_idl_EmitDcl_ComponentExport, gen_idl_ConsumesDcl_ComponentExport, gen_idl_ComponentForwardDecl_Definition, gen_idl_ProvidesDcl_ComponentExport, gen_idl_ProvidesDcl_PortExport, gen_idl_ProvidesDcl_ConnectorExport, gen_idl_FactoryDcl_HomeExport, gen_idl_FinderDcl_HomeExport, gen_idl_Event_Definition, gen_idl_Event_TemplateDefinition, gen_idl_Event_FixedDefinition, gen_idl_HomeDecl_Definition, gen_idl_HomeDecl_TemplateDefinition, gen_idl_HomeDecl_FixedDefinition, gen_idl_EventForwardDcl_Event, gen_idl_PortTypeDecl_Definition, gen_idl_PortTypeDecl_TemplateDefinition, gen_idl_PortTypeDecl_FixedDefinition, gen_idl_PortDecl_ComponentExport, gen_idl_PortDecl_ConnectorExport, gen_idl_Connector_Definition, gen_idl_Connector_TemplateDefinition, gen_idl_Connector_FixedDefinition, gen_idl_EventDcl_Event, gen_idl_TypenameParamType_FormalParameterType, gen_idl_InterfaceParamType_FormalParameterType, gen_idl_ValuetypeParamType_FormalParameterType, gen_idl_EventParamType_FormalParameterType, gen_idl_StructParamType_FormalParameterType, gen_idl_UnionParamType_FormalParameterType, gen_idl_ExceptionParamType_FormalParameterType, gen_idl_EnumParamType_FormalParameterType, gen_idl_SequenceParamType_FormalParameterType, gen_idl_ConstParamType_FormalParameterType, gen_idl_FixedModule_TemplateDefinition, gen_idl_FixedModule_FixedDefinition, gen_idl_TemplateModuleInst_Definition, gen_idl_TemplateModuleRef_TemplateDefinition, gen_idl_TemplateModule_Definition, gen_idl_IDLComment_Definition, gen_idl_IDLComment_Export, gen_idl_IDLComment_ComponentExport, gen_idl_IDLComment_PortExport, gen_idl_IDLComment_ConnectorExport, gen_idl_IDLComment_TemplateDefinition, gen_idl_IDLComment_FixedDefinition},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)