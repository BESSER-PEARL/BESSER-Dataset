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
LoopStatementKind: Enumeration = Enumeration(
    name="LoopStatementKind",
    literals={
            EnumerationLiteral(name="FOREACH"),
			EnumerationLiteral(name="WHILE"),
			EnumerationLiteral(name="DOWHILE"),
			EnumerationLiteral(name="FOR")
    }
)

JumpStatementKind: Enumeration = Enumeration(
    name="JumpStatementKind",
    literals={
            EnumerationLiteral(name="JUMP"),
			EnumerationLiteral(name="RETURN"),
			EnumerationLiteral(name="THROW")
    }
)

Status: Enumeration = Enumeration(
    name="Status",
    literals={
            EnumerationLiteral(name="NORMAL"),
			EnumerationLiteral(name="LIBRARY"),
			EnumerationLiteral(name="IMPLICIT"),
			EnumerationLiteral(name="FAILEDDEP")
    }
)

Visibilities: Enumeration = Enumeration(
    name="Visibilities",
    literals={
            EnumerationLiteral(name="VISIBILITYSTRICTPROTECTED"),
			EnumerationLiteral(name="VISIBILITYPUBLIC"),
			EnumerationLiteral(name="VISIBILITYPACKAGE"),
			EnumerationLiteral(name="VISIBILITYPROTECTED"),
			EnumerationLiteral(name="VISIBILITYPRIVAT")
    }
)

GlobalFunctionKind: Enumeration = Enumeration(
    name="GlobalFunctionKind",
    literals={
            EnumerationLiteral(name="NORMAL"),
			EnumerationLiteral(name="UNITINITIALIZER"),
			EnumerationLiteral(name="UNITFINALIZER")
    }
)

# Classes
BaseAccess = Class(name="BaseAccess")
CloneInstance = Class(name="CloneInstance")
gast_statements_ExceptionHandler = Class(name="gast::statements::ExceptionHandler")
Statement = Class(name="Statement")
CatchBlock = Class(name="CatchBlock")
BlockStatement = Class(name="BlockStatement")
gast_statements_Statement = Class(name="gast::statements::Statement", is_abstract=True)
SourceEntity = Class(name="SourceEntity")
Branch = Class(name="Branch")
LoopStatement = Class(name="LoopStatement")
gast_statements_Branch = Class(name="gast::statements::Branch")
GASTExpression = Class(name="GASTExpression")
gast_statements_BlockStatement = Class(name="gast::statements::BlockStatement")
Function = Class(name="Function")
BranchStatement = Class(name="BranchStatement")
gast_statements_GASTExpression = Class(name="gast::statements::GASTExpression", is_abstract=True)
gast_statements_BranchStatement = Class(name="gast::statements::BranchStatement")
gast_statements_LoopStatement = Class(name="gast::statements::LoopStatement")
gast_statements_CatchBlock = Class(name="gast::statements::CatchBlock")
CatchParameter = Class(name="CatchParameter")
gast_statements_SimpleStatement = Class(name="gast::statements::SimpleStatement")
gast_statements_JumpStatement = Class(name="gast::statements::JumpStatement")
statements_Statement = Class(name="statements::Statement")
statements_FlowInstr = Class(name="statements::FlowInstr")
gast_statements_GASTBehaviour = Class(name="gast::statements::GASTBehaviour")
gast_statements_Methods = Class(name="gast::statements::Methods")
statements_BlockStatement = Class(name="statements::BlockStatement")
Exit = Class(name="Exit")
gast_statements_Exit = Class(name="gast::statements::Exit")
FlowInstr = Class(name="FlowInstr")
gast_statements_FlowInstr = Class(name="gast::statements::FlowInstr")
Var = Class(name="Var")
gast_statements_Var = Class(name="gast::statements::Var")
gast_statements_Param = Class(name="gast::statements::Param")
gast_core_BasePath = Class(name="gast::core::BasePath")
ModelElement = Class(name="ModelElement")
Root = Class(name="Root")
Directory = Class(name="Directory")
gast_core_Identifier = Class(name="gast::core::Identifier", is_abstract=True)
gast_core_NamedModelElement = Class(name="gast::core::NamedModelElement", is_abstract=True)
gast_core_ModelElement = Class(name="gast::core::ModelElement", is_abstract=True)
Identifier = Class(name="Identifier")
ModelAnnotation = Class(name="ModelAnnotation")
gast_core_Package = Class(name="gast::core::Package")
NamedModelElement = Class(name="NamedModelElement")
GASTClass = Class(name="GASTClass")
Access = Class(name="Access")
Delegate = Class(name="Delegate")
GlobalFunction = Class(name="GlobalFunction")
GlobalVariable = Class(name="GlobalVariable")
Package = Class(name="Package")
TypeAlias = Class(name="TypeAlias")
gast_core_GenericEntity = Class(name="gast::core::GenericEntity", is_abstract=True)
TypeParameterClass = Class(name="TypeParameterClass")
gast_core_Root = Class(name="gast::core::Root")
Clone = Class(name="Clone")
StructuralAbstraction = Class(name="StructuralAbstraction")
BasePath = Class(name="BasePath")
gast_core_Directory = Class(name="gast::core::Directory")
GASTType = Class(name="GASTType")
File = Class(name="File")
gast_core_File = Class(name="gast::core::File")
gast_core_PackageAlias = Class(name="gast::core::PackageAlias")
gast_core_Position = Class(name="gast::core::Position")
gast_core_SourceEntity = Class(name="gast::core::SourceEntity", is_abstract=True)
Position = Class(name="Position")
gast_annotations_Attribute = Class(name="gast::annotations::Attribute")
types_GASTClass = Class(name="types::GASTClass")
annotations_ModelAnnotation = Class(name="annotations::ModelAnnotation")
gast_annotations_Clone = Class(name="gast::annotations::Clone")
core_ModelElement = Class(name="core::ModelElement")
gast_annotations_StructuralAbstraction = Class(name="gast::annotations::StructuralAbstraction", is_abstract=True)
core_NamedModelElement = Class(name="core::NamedModelElement")
gast_annotations_Comment = Class(name="gast::annotations::Comment")
core_SourceEntity = Class(name="core::SourceEntity")
gast_annotations_CloneInstance = Class(name="gast::annotations::CloneInstance")
gast_annotations_Subsystem = Class(name="gast::annotations::Subsystem")
gast_annotations_Layer = Class(name="gast::annotations::Layer")
gast_annotations_ModelAnnotation = Class(name="gast::annotations::ModelAnnotation", is_abstract=True)
gast_types_Reference = Class(name="gast::types::Reference")
TypeDecorator = Class(name="TypeDecorator")
gast_types_TypeDecorator = Class(name="gast::types::TypeDecorator", is_abstract=True)
gast_types_GASTType = Class(name="gast::types::GASTType", is_abstract=True)
gast_types_GASTArray = Class(name="gast::types::GASTArray")
gast_types_TypeAlias = Class(name="gast::types::TypeAlias")
types_Member = Class(name="types::Member")
types_TypeDecorator = Class(name="types::TypeDecorator")
gast_types_Member = Class(name="gast::types::Member", is_abstract=True)
Member = Class(name="Member")
gast_types_TypeParameterClass = Class(name="gast::types::TypeParameterClass")
gast_types_GenericClass = Class(name="gast::types::GenericClass")
core_GenericEntity = Class(name="core::GenericEntity")
gast_types_GASTEnumeration = Class(name="gast::types::GASTEnumeration")
gast_types_GASTStruct = Class(name="gast::types::GASTStruct")
gast_types_GASTUnion = Class(name="gast::types::GASTUnion")
gast_types_GASTClass = Class(name="gast::types::GASTClass")
types_GASTType = Class(name="types::GASTType")
Constructor = Class(name="Constructor")
Destructor = Class(name="Destructor")
Field = Class(name="Field")
Method_ = Class(name="Method")
InheritanceTypeAccess = Class(name="InheritanceTypeAccess")
Property_ = Class(name="Property")
gast_accesses_ParameterInstantiationTypeAccess = Class(name="gast::accesses::ParameterInstantiationTypeAccess")
TypeAccess = Class(name="TypeAccess")
gast_accesses_TypeAccess = Class(name="gast::accesses::TypeAccess", is_abstract=True)
gast_accesses_CastTypeAccess = Class(name="gast::accesses::CastTypeAccess")
gast_accesses_BaseAccess = Class(name="gast::accesses::BaseAccess", is_abstract=True)
gast_accesses_CompositeAccess = Class(name="gast::accesses::CompositeAccess")
CompositeAccess = Class(name="CompositeAccess")
gast_accesses_DeclarationTypeAccess = Class(name="gast::accesses::DeclarationTypeAccess")
Variable = Class(name="Variable")
gast_accesses_ThrowTypeAccess = Class(name="gast::accesses::ThrowTypeAccess")
gast_accesses_FunctionAccess = Class(name="gast::accesses::FunctionAccess")
gast_accesses_DelegateAccess = Class(name="gast::accesses::DelegateAccess")
FunctionAccess = Class(name="FunctionAccess")
gast_accesses_RunTimeTypeAccess = Class(name="gast::accesses::RunTimeTypeAccess")
gast_accesses_SelfAccess = Class(name="gast::accesses::SelfAccess")
VariableAccess = Class(name="VariableAccess")
gast_accesses_StaticTypeAccess = Class(name="gast::accesses::StaticTypeAccess")
gast_accesses_PropertyAccess = Class(name="gast::accesses::PropertyAccess")
gast_accesses_Access = Class(name="gast::accesses::Access", is_abstract=True)
gast_accesses_InheritanceTypeAccess = Class(name="gast::accesses::InheritanceTypeAccess")
gast_accesses_VariableAccess = Class(name="gast::accesses::VariableAccess")
gast_functions_Delegate = Class(name="gast::functions::Delegate")
functions_Function = Class(name="functions::Function")
gast_functions_Constructor = Class(name="gast::functions::Constructor")
gast_functions_GenericFunction = Class(name="gast::functions::GenericFunction")
functions_GlobalFunction = Class(name="functions::GlobalFunction")
gast_functions_GlobalFunction = Class(name="gast::functions::GlobalFunction")
gast_functions_Method = Class(name="gast::functions::Method")
gast_functions_Destructor = Class(name="gast::functions::Destructor")
gast_functions_GenericMethod = Class(name="gast::functions::GenericMethod")
functions_Method = Class(name="functions::Method")
gast_functions_GenericConstructor = Class(name="gast::functions::GenericConstructor")
functions_Constructor = Class(name="functions::Constructor")
gast_functions_Function = Class(name="gast::functions::Function", is_abstract=True)
DeclarationTypeAccess = Class(name="DeclarationTypeAccess")
FormalParameter = Class(name="FormalParameter")
LocalVariable = Class(name="LocalVariable")
ThrowTypeAccess = Class(name="ThrowTypeAccess")
gast_variables_FormalParameter = Class(name="gast::variables::FormalParameter")
gast_variables_Variable = Class(name="gast::variables::Variable", is_abstract=True)
gast_variables_CatchParameter = Class(name="gast::variables::CatchParameter")
gast_variables_Field = Class(name="gast::variables::Field")
variables_Variable = Class(name="variables::Variable")
gast_variables_LocalVariable = Class(name="gast::variables::LocalVariable")
gast_variables_Property = Class(name="gast::variables::Property")
variables_Field = Class(name="variables::Field")
gast_variables_GlobalVariable = Class(name="gast::variables::GlobalVariable")

# BaseAccess class attributes and methods

# CloneInstance class attributes and methods

# gast_statements_ExceptionHandler class attributes and methods

# Statement class attributes and methods

# CatchBlock class attributes and methods

# BlockStatement class attributes and methods

# gast_statements_Statement class attributes and methods
gast_statements_Statement_numberOfNodesInCFG: Property = Property(name="numberOfNodesInCFG", type=IntegerType)
gast_statements_Statement_numberOfStatements: Property = Property(name="numberOfStatements", type=IntegerType)
gast_statements_Statement_maximumNestingLevel: Property = Property(name="maximumNestingLevel", type=IntegerType)
gast_statements_Statement_numberOfComments: Property = Property(name="numberOfComments", type=IntegerType)
gast_statements_Statement_linesOfCode: Property = Property(name="linesOfCode", type=IntegerType)
gast_statements_Statement_numberOfEdgesInCFG: Property = Property(name="numberOfEdgesInCFG", type=IntegerType)
gast_statements_Statement.attributes={gast_statements_Statement_linesOfCode, gast_statements_Statement_numberOfEdgesInCFG, gast_statements_Statement_maximumNestingLevel, gast_statements_Statement_numberOfComments, gast_statements_Statement_numberOfNodesInCFG, gast_statements_Statement_numberOfStatements}

# SourceEntity class attributes and methods

# Branch class attributes and methods

# LoopStatement class attributes and methods

# gast_statements_Branch class attributes and methods

# GASTExpression class attributes and methods

# gast_statements_BlockStatement class attributes and methods
gast_statements_BlockStatement_synchronized: Property = Property(name="synchronized", type=BooleanType)
gast_statements_BlockStatement.attributes={gast_statements_BlockStatement_synchronized}

# Function class attributes and methods

# BranchStatement class attributes and methods

# gast_statements_GASTExpression class attributes and methods

# gast_statements_BranchStatement class attributes and methods

# gast_statements_LoopStatement class attributes and methods
gast_statements_LoopStatement_kind: Property = Property(name="kind", type=StringType)
gast_statements_LoopStatement.attributes={gast_statements_LoopStatement_kind}

# gast_statements_CatchBlock class attributes and methods

# CatchParameter class attributes and methods

# gast_statements_SimpleStatement class attributes and methods

# gast_statements_JumpStatement class attributes and methods
gast_statements_JumpStatement_kind: Property = Property(name="kind", type=StringType)
gast_statements_JumpStatement.attributes={gast_statements_JumpStatement_kind}

# statements_Statement class attributes and methods

# statements_FlowInstr class attributes and methods

# gast_statements_GASTBehaviour class attributes and methods

# gast_statements_Methods class attributes and methods
gast_statements_Methods_methodName: Property = Property(name="methodName", type=StringType)
gast_statements_Methods.attributes={gast_statements_Methods_methodName}

# statements_BlockStatement class attributes and methods

# Exit class attributes and methods

# gast_statements_Exit class attributes and methods
gast_statements_Exit_name: Property = Property(name="name", type=StringType)
gast_statements_Exit.attributes={gast_statements_Exit_name}

# FlowInstr class attributes and methods

# gast_statements_FlowInstr class attributes and methods
gast_statements_FlowInstr_txt: Property = Property(name="txt", type=StringType)
gast_statements_FlowInstr.attributes={gast_statements_FlowInstr_txt}

# Var class attributes and methods

# gast_statements_Var class attributes and methods
gast_statements_Var_name: Property = Property(name="name", type=StringType)
gast_statements_Var.attributes={gast_statements_Var_name}

# gast_statements_Param class attributes and methods

# gast_core_BasePath class attributes and methods
gast_core_BasePath_path: Property = Property(name="path", type=StringType)
gast_core_BasePath.attributes={gast_core_BasePath_path}

# ModelElement class attributes and methods

# Root class attributes and methods

# Directory class attributes and methods

# gast_core_Identifier class attributes and methods
gast_core_Identifier_id: Property = Property(name="id", type=StringType)
gast_core_Identifier_m_idHasToBeUnique: Method = Method(name="idHasToBeUnique", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
gast_core_Identifier.attributes={gast_core_Identifier_id}
gast_core_Identifier.methods={gast_core_Identifier_m_idHasToBeUnique}

# gast_core_NamedModelElement class attributes and methods
gast_core_NamedModelElement_simpleName: Property = Property(name="simpleName", type=StringType)
gast_core_NamedModelElement.attributes={gast_core_NamedModelElement_simpleName}

# gast_core_ModelElement class attributes and methods
gast_core_ModelElement_status: Property = Property(name="status", type=StringType)
gast_core_ModelElement_sissyId: Property = Property(name="sissyId", type=IntegerType)
gast_core_ModelElement.attributes={gast_core_ModelElement_status, gast_core_ModelElement_sissyId}

# Identifier class attributes and methods

# ModelAnnotation class attributes and methods

# gast_core_Package class attributes and methods
gast_core_Package_linesOfComments: Property = Property(name="linesOfComments", type=IntegerType)
gast_core_Package_linesOfCode: Property = Property(name="linesOfCode", type=IntegerType)
gast_core_Package_qualifiedName: Property = Property(name="qualifiedName", type=StringType)
gast_core_Package.attributes={gast_core_Package_linesOfComments, gast_core_Package_linesOfCode, gast_core_Package_qualifiedName}

# NamedModelElement class attributes and methods

# GASTClass class attributes and methods

# Access class attributes and methods

# Delegate class attributes and methods

# GlobalFunction class attributes and methods

# GlobalVariable class attributes and methods

# Package class attributes and methods

# TypeAlias class attributes and methods

# gast_core_GenericEntity class attributes and methods

# TypeParameterClass class attributes and methods

# gast_core_Root class attributes and methods
gast_core_Root_linesOfComments: Property = Property(name="linesOfComments", type=IntegerType)
gast_core_Root_linesOfCode: Property = Property(name="linesOfCode", type=IntegerType)
gast_core_Root_m_getPackageByName: Method = Method(name="getPackageByName", parameters={Parameter(name='name')}, type=StringType)
gast_core_Root_m_getPackageByQualifiedName: Method = Method(name="getPackageByQualifiedName", parameters={Parameter(name='qualifiedName')}, type=StringType)
gast_core_Root.attributes={gast_core_Root_linesOfComments, gast_core_Root_linesOfCode}
gast_core_Root.methods={gast_core_Root_m_getPackageByName, gast_core_Root_m_getPackageByQualifiedName}

# Clone class attributes and methods

# StructuralAbstraction class attributes and methods

# BasePath class attributes and methods

# gast_core_Directory class attributes and methods
gast_core_Directory_fullQualifiedPath: Property = Property(name="fullQualifiedPath", type=StringType)
gast_core_Directory_fileSystemPath: Property = Property(name="fileSystemPath", type=StringType)
gast_core_Directory.attributes={gast_core_Directory_fullQualifiedPath, gast_core_Directory_fileSystemPath}

# GASTType class attributes and methods

# File class attributes and methods

# gast_core_File class attributes and methods
gast_core_File_sourceFile: Property = Property(name="sourceFile", type=BooleanType)
gast_core_File_assemblyFile: Property = Property(name="assemblyFile", type=BooleanType)
gast_core_File_size: Property = Property(name="size", type=StringType)
gast_core_File_fullQualifiedPath: Property = Property(name="fullQualifiedPath", type=StringType)
gast_core_File_fileSystemPath: Property = Property(name="fileSystemPath", type=StringType)
gast_core_File_linesOfCode: Property = Property(name="linesOfCode", type=IntegerType)
gast_core_File.attributes={gast_core_File_sourceFile, gast_core_File_assemblyFile, gast_core_File_fullQualifiedPath, gast_core_File_size, gast_core_File_linesOfCode, gast_core_File_fileSystemPath}

# gast_core_PackageAlias class attributes and methods

# gast_core_Position class attributes and methods
gast_core_Position_endColumn: Property = Property(name="endColumn", type=IntegerType)
gast_core_Position_startColumn: Property = Property(name="startColumn", type=IntegerType)
gast_core_Position_endLine: Property = Property(name="endLine", type=IntegerType)
gast_core_Position_startLine: Property = Property(name="startLine", type=IntegerType)
gast_core_Position_m_EitherAssemblyFileOrSourceFileSet: Method = Method(name="EitherAssemblyFileOrSourceFileSet", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
gast_core_Position.attributes={gast_core_Position_startLine, gast_core_Position_endLine, gast_core_Position_startColumn, gast_core_Position_endColumn}
gast_core_Position.methods={gast_core_Position_m_EitherAssemblyFileOrSourceFileSet}

# gast_core_SourceEntity class attributes and methods

# Position class attributes and methods

# gast_annotations_Attribute class attributes and methods

# types_GASTClass class attributes and methods

# annotations_ModelAnnotation class attributes and methods

# gast_annotations_Clone class attributes and methods

# core_ModelElement class attributes and methods

# gast_annotations_StructuralAbstraction class attributes and methods

# core_NamedModelElement class attributes and methods

# gast_annotations_Comment class attributes and methods
gast_annotations_Comment_todo: Property = Property(name="todo", type=BooleanType)
gast_annotations_Comment_formal: Property = Property(name="formal", type=BooleanType)
gast_annotations_Comment_todoCount: Property = Property(name="todoCount", type=IntegerType)
gast_annotations_Comment_texts: Property = Property(name="texts", type=StringType)
gast_annotations_Comment_m_OCLtodo: Method = Method(name="OCLtodo", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
gast_annotations_Comment.attributes={gast_annotations_Comment_formal, gast_annotations_Comment_texts, gast_annotations_Comment_todo, gast_annotations_Comment_todoCount}
gast_annotations_Comment.methods={gast_annotations_Comment_m_OCLtodo}

# core_SourceEntity class attributes and methods

# gast_annotations_CloneInstance class attributes and methods

# gast_annotations_Subsystem class attributes and methods

# gast_annotations_Layer class attributes and methods

# gast_annotations_ModelAnnotation class attributes and methods

# gast_types_Reference class attributes and methods
gast_types_Reference_explicit: Property = Property(name="explicit", type=BooleanType)
gast_types_Reference.attributes={gast_types_Reference_explicit}

# TypeDecorator class attributes and methods

# gast_types_TypeDecorator class attributes and methods

# gast_types_GASTType class attributes and methods
gast_types_GASTType_qualifiedName: Property = Property(name="qualifiedName", type=StringType)
gast_types_GASTType_referenceType: Property = Property(name="referenceType", type=BooleanType)
gast_types_GASTType.attributes={gast_types_GASTType_referenceType, gast_types_GASTType_qualifiedName}

# gast_types_GASTArray class attributes and methods
gast_types_GASTArray_dimensions: Property = Property(name="dimensions", type=IntegerType)
gast_types_GASTArray.attributes={gast_types_GASTArray_dimensions}

# gast_types_TypeAlias class attributes and methods
gast_types_TypeAlias_innerTypeAlias: Property = Property(name="innerTypeAlias", type=BooleanType)
gast_types_TypeAlias.attributes={gast_types_TypeAlias_innerTypeAlias}

# types_Member class attributes and methods

# types_TypeDecorator class attributes and methods

# gast_types_Member class attributes and methods
gast_types_Member_visibility: Property = Property(name="visibility", type=StringType)
gast_types_Member_abstract: Property = Property(name="abstract", type=BooleanType)
gast_types_Member_extern: Property = Property(name="extern", type=BooleanType)
gast_types_Member_final: Property = Property(name="final", type=BooleanType)
gast_types_Member_internal: Property = Property(name="internal", type=BooleanType)
gast_types_Member_introspectable: Property = Property(name="introspectable", type=BooleanType)
gast_types_Member_override: Property = Property(name="override", type=BooleanType)
gast_types_Member_static: Property = Property(name="static", type=BooleanType)
gast_types_Member_typeParameterClassMember: Property = Property(name="typeParameterClassMember", type=BooleanType)
gast_types_Member_virtual: Property = Property(name="virtual", type=BooleanType)
gast_types_Member_m_getSurroundingClass: Method = Method(name="getSurroundingClass", parameters={}, type=StringType)
gast_types_Member.attributes={gast_types_Member_virtual, gast_types_Member_internal, gast_types_Member_typeParameterClassMember, gast_types_Member_introspectable, gast_types_Member_final, gast_types_Member_visibility, gast_types_Member_static, gast_types_Member_override, gast_types_Member_extern, gast_types_Member_abstract}
gast_types_Member.methods={gast_types_Member_m_getSurroundingClass}

# Member class attributes and methods

# gast_types_TypeParameterClass class attributes and methods

# gast_types_GenericClass class attributes and methods

# core_GenericEntity class attributes and methods

# gast_types_GASTEnumeration class attributes and methods

# gast_types_GASTStruct class attributes and methods

# gast_types_GASTUnion class attributes and methods

# gast_types_GASTClass class attributes and methods
gast_types_GASTClass_linesOfComments: Property = Property(name="linesOfComments", type=IntegerType)
gast_types_GASTClass_local: Property = Property(name="local", type=BooleanType)
gast_types_GASTClass_primitive: Property = Property(name="primitive", type=BooleanType)
gast_types_GASTClass_interface: Property = Property(name="interface", type=BooleanType)
gast_types_GASTClass_anonymous: Property = Property(name="anonymous", type=BooleanType)
gast_types_GASTClass_inner: Property = Property(name="inner", type=BooleanType)
gast_types_GASTClass.attributes={gast_types_GASTClass_linesOfComments, gast_types_GASTClass_inner, gast_types_GASTClass_interface, gast_types_GASTClass_local, gast_types_GASTClass_anonymous, gast_types_GASTClass_primitive}

# types_GASTType class attributes and methods

# Constructor class attributes and methods

# Destructor class attributes and methods

# Field class attributes and methods

# Method class attributes and methods

# InheritanceTypeAccess class attributes and methods

# Property class attributes and methods

# gast_accesses_ParameterInstantiationTypeAccess class attributes and methods

# TypeAccess class attributes and methods

# gast_accesses_TypeAccess class attributes and methods

# gast_accesses_CastTypeAccess class attributes and methods

# gast_accesses_BaseAccess class attributes and methods

# gast_accesses_CompositeAccess class attributes and methods

# CompositeAccess class attributes and methods

# gast_accesses_DeclarationTypeAccess class attributes and methods

# Variable class attributes and methods

# gast_accesses_ThrowTypeAccess class attributes and methods
gast_accesses_ThrowTypeAccess_declared: Property = Property(name="declared", type=BooleanType)
gast_accesses_ThrowTypeAccess.attributes={gast_accesses_ThrowTypeAccess_declared}

# gast_accesses_FunctionAccess class attributes and methods

# gast_accesses_DelegateAccess class attributes and methods

# FunctionAccess class attributes and methods

# gast_accesses_RunTimeTypeAccess class attributes and methods

# gast_accesses_SelfAccess class attributes and methods
gast_accesses_SelfAccess_super: Property = Property(name="super", type=BooleanType)
gast_accesses_SelfAccess.attributes={gast_accesses_SelfAccess_super}

# VariableAccess class attributes and methods

# gast_accesses_StaticTypeAccess class attributes and methods

# gast_accesses_PropertyAccess class attributes and methods

# gast_accesses_Access class attributes and methods

# gast_accesses_InheritanceTypeAccess class attributes and methods
gast_accesses_InheritanceTypeAccess_implementationInheritance: Property = Property(name="implementationInheritance", type=BooleanType)
gast_accesses_InheritanceTypeAccess.attributes={gast_accesses_InheritanceTypeAccess_implementationInheritance}

# gast_accesses_VariableAccess class attributes and methods
gast_accesses_VariableAccess_write: Property = Property(name="write", type=BooleanType)
gast_accesses_VariableAccess.attributes={gast_accesses_VariableAccess_write}

# gast_functions_Delegate class attributes and methods
gast_functions_Delegate_innerDelegate: Property = Property(name="innerDelegate", type=BooleanType)
gast_functions_Delegate.attributes={gast_functions_Delegate_innerDelegate}

# functions_Function class attributes and methods

# gast_functions_Constructor class attributes and methods
gast_functions_Constructor_initializer: Property = Property(name="initializer", type=BooleanType)
gast_functions_Constructor.attributes={gast_functions_Constructor_initializer}

# gast_functions_GenericFunction class attributes and methods

# functions_GlobalFunction class attributes and methods

# gast_functions_GlobalFunction class attributes and methods
gast_functions_GlobalFunction_kind: Property = Property(name="kind", type=StringType)
gast_functions_GlobalFunction.attributes={gast_functions_GlobalFunction_kind}

# gast_functions_Method class attributes and methods
gast_functions_Method_propertyMethod: Property = Property(name="propertyMethod", type=BooleanType)
gast_functions_Method.attributes={gast_functions_Method_propertyMethod}

# gast_functions_Destructor class attributes and methods

# gast_functions_GenericMethod class attributes and methods

# functions_Method class attributes and methods

# gast_functions_GenericConstructor class attributes and methods

# functions_Constructor class attributes and methods

# gast_functions_Function class attributes and methods
gast_functions_Function_numberOfStatements: Property = Property(name="numberOfStatements", type=IntegerType)
gast_functions_Function_maximumNestingLevel: Property = Property(name="maximumNestingLevel", type=IntegerType)
gast_functions_Function_linesOfComments: Property = Property(name="linesOfComments", type=IntegerType)
gast_functions_Function_numberOfEdgesInCFG: Property = Property(name="numberOfEdgesInCFG", type=IntegerType)
gast_functions_Function_numberOfNodesInCFG: Property = Property(name="numberOfNodesInCFG", type=IntegerType)
gast_functions_Function_operator: Property = Property(name="operator", type=BooleanType)
gast_functions_Function_linesOfCode: Property = Property(name="linesOfCode", type=IntegerType)
gast_functions_Function.attributes={gast_functions_Function_numberOfStatements, gast_functions_Function_numberOfEdgesInCFG, gast_functions_Function_linesOfComments, gast_functions_Function_linesOfCode, gast_functions_Function_maximumNestingLevel, gast_functions_Function_operator, gast_functions_Function_numberOfNodesInCFG}

# DeclarationTypeAccess class attributes and methods

# FormalParameter class attributes and methods

# LocalVariable class attributes and methods

# ThrowTypeAccess class attributes and methods

# gast_variables_FormalParameter class attributes and methods
gast_variables_FormalParameter_passedByReference: Property = Property(name="passedByReference", type=BooleanType)
gast_variables_FormalParameter.attributes={gast_variables_FormalParameter_passedByReference}

# gast_variables_Variable class attributes and methods
gast_variables_Variable_const: Property = Property(name="const", type=BooleanType)
gast_variables_Variable.attributes={gast_variables_Variable_const}

# gast_variables_CatchParameter class attributes and methods
gast_variables_CatchParameter_rethrown: Property = Property(name="rethrown", type=BooleanType)
gast_variables_CatchParameter.attributes={gast_variables_CatchParameter_rethrown}

# gast_variables_Field class attributes and methods
gast_variables_Field_propertyField: Property = Property(name="propertyField", type=BooleanType)
gast_variables_Field.attributes={gast_variables_Field_propertyField}

# variables_Variable class attributes and methods

# gast_variables_LocalVariable class attributes and methods

# gast_variables_Property class attributes and methods

# variables_Field class attributes and methods

# gast_variables_GlobalVariable class attributes and methods

# Relationships
accesses6: BinaryAssociation = BinaryAssociation(
    name="accesses6",
    ends={
        Property(name="accesses", type=gast_statements_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="BaseAccess", type=BaseAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cloneInstance7: BinaryAssociation = BinaryAssociation(
    name="cloneInstance7",
    ends={
        Property(name="annotations", type=gast_statements_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="CloneInstance", type=CloneInstance, multiplicity=Multiplicity(0, 1))
    }
)
catchBlocks0: BinaryAssociation = BinaryAssociation(
    name="catchBlocks0",
    ends={
        Property(name="CatchBlock", type=gast_statements_ExceptionHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_statements_ExceptionHandler", type=CatchBlock, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
finallyBlock1: BinaryAssociation = BinaryAssociation(
    name="finallyBlock1",
    ends={
        Property(name="BlockStatement", type=gast_statements_ExceptionHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_statements_ExceptionHandler2", type=BlockStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
guardedBlock3: BinaryAssociation = BinaryAssociation(
    name="guardedBlock3",
    ends={
        Property(name="BlockStatement5", type=gast_statements_ExceptionHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_statements_ExceptionHandler4", type=BlockStatement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
branch11: BinaryAssociation = BinaryAssociation(
    name="branch11",
    ends={
        Property(name="statements12", type=gast_statements_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="Branch", type=Branch, multiplicity=Multiplicity(0, 1))
    }
)
blockstatement8: BinaryAssociation = BinaryAssociation(
    name="blockstatement8",
    ends={
        Property(name="statements", type=gast_statements_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="BlockStatement9", type=BlockStatement, multiplicity=Multiplicity(0, 1))
    }
)
surroundingStatement10: BinaryAssociation = BinaryAssociation(
    name="surroundingStatement10",
    ends={
        Property(name="Statement", type=gast_statements_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_statements_Statement", type=Statement, multiplicity=Multiplicity(0, 1))
    }
)
conditionExpression25: BinaryAssociation = BinaryAssociation(
    name="conditionExpression25",
    ends={
        Property(name="GASTExpression", type=gast_statements_Branch, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_statements_Branch", type=GASTExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
loopstatement13: BinaryAssociation = BinaryAssociation(
    name="loopstatement13",
    ends={
        Property(name="statements14", type=gast_statements_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="LoopStatement", type=LoopStatement, multiplicity=Multiplicity(0, 1))
    }
)
cfPre15: BinaryAssociation = BinaryAssociation(
    name="cfPre15",
    ends={
        Property(name="Statement17", type=gast_statements_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_statements_Statement16", type=Statement, multiplicity=Multiplicity(0, 9999))
    }
)
cfNext18: BinaryAssociation = BinaryAssociation(
    name="cfNext18",
    ends={
        Property(name="Statement20", type=gast_statements_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_statements_Statement19", type=Statement, multiplicity=Multiplicity(0, 9999))
    }
)
statements21: BinaryAssociation = BinaryAssociation(
    name="statements21",
    ends={
        Property(name="statements23", type=gast_statements_BlockStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="Statement22", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
surroundingFunction24: BinaryAssociation = BinaryAssociation(
    name="surroundingFunction24",
    ends={
        Property(name="functions", type=gast_statements_BlockStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="Function", type=Function, multiplicity=Multiplicity(0, 1))
    }
)
breakConditionExpression34: BinaryAssociation = BinaryAssociation(
    name="breakConditionExpression34",
    ends={
        Property(name="GASTExpression35", type=gast_statements_LoopStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_statements_LoopStatement", type=GASTExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
branchstatement26: BinaryAssociation = BinaryAssociation(
    name="branchstatement26",
    ends={
        Property(name="statements27", type=gast_statements_Branch, multiplicity=Multiplicity(1, 1)),
        Property(name="BranchStatement", type=BranchStatement, multiplicity=Multiplicity(1, 1))
    }
)
statement28: BinaryAssociation = BinaryAssociation(
    name="statement28",
    ends={
        Property(name="statements30", type=gast_statements_Branch, multiplicity=Multiplicity(1, 1)),
        Property(name="Statement29", type=Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
branches31: BinaryAssociation = BinaryAssociation(
    name="branches31",
    ends={
        Property(name="statements33", type=gast_statements_BranchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="Branch32", type=Branch, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
catchParameter45: BinaryAssociation = BinaryAssociation(
    name="catchParameter45",
    ends={
        Property(name="CatchParameter", type=gast_statements_CatchBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_statements_CatchBlock", type=CatchParameter, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initExpression36: BinaryAssociation = BinaryAssociation(
    name="initExpression36",
    ends={
        Property(name="GASTExpression38", type=gast_statements_LoopStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_statements_LoopStatement37", type=GASTExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
incrementExpression39: BinaryAssociation = BinaryAssociation(
    name="incrementExpression39",
    ends={
        Property(name="GASTExpression41", type=gast_statements_LoopStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_statements_LoopStatement40", type=GASTExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body42: BinaryAssociation = BinaryAssociation(
    name="body42",
    ends={
        Property(name="statements44", type=gast_statements_LoopStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="Statement43", type=Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression48: BinaryAssociation = BinaryAssociation(
    name="expression48",
    ends={
        Property(name="GASTExpression49", type=gast_statements_SimpleStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_statements_SimpleStatement", type=GASTExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression46: BinaryAssociation = BinaryAssociation(
    name="expression46",
    ends={
        Property(name="GASTExpression47", type=gast_statements_JumpStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_statements_JumpStatement", type=GASTExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cfnext57: BinaryAssociation = BinaryAssociation(
    name="cfnext57",
    ends={
        Property(name="statements58", type=gast_statements_FlowInstr, multiplicity=Multiplicity(1, 1)),
        Property(name="FlowInstr", type=FlowInstr, multiplicity=Multiplicity(0, 9999))
    }
)
cfPrev59: BinaryAssociation = BinaryAssociation(
    name="cfPrev59",
    ends={
        Property(name="statements61", type=gast_statements_FlowInstr, multiplicity=Multiplicity(1, 1)),
        Property(name="FlowInstr60", type=FlowInstr, multiplicity=Multiplicity(0, 9999))
    }
)
blockstatement50: BinaryAssociation = BinaryAssociation(
    name="blockstatement50",
    ends={
        Property(name="BlockStatement51", type=gast_statements_GASTBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_statements_GASTBehaviour", type=BlockStatement, multiplicity=Multiplicity(1, 1))
    }
)
exit52: BinaryAssociation = BinaryAssociation(
    name="exit52",
    ends={
        Property(name="Exit", type=gast_statements_Methods, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_statements_Methods", type=Exit, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
use53: BinaryAssociation = BinaryAssociation(
    name="use53",
    ends={
        Property(name="Var", type=gast_statements_FlowInstr, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_statements_FlowInstr", type=Var, multiplicity=Multiplicity(0, 9999))
    }
)
def54: BinaryAssociation = BinaryAssociation(
    name="def54",
    ends={
        Property(name="Var56", type=gast_statements_FlowInstr, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_statements_FlowInstr55", type=Var, multiplicity=Multiplicity(0, 9999))
    }
)
root62: BinaryAssociation = BinaryAssociation(
    name="root62",
    ends={
        Property(name="core", type=gast_core_BasePath, multiplicity=Multiplicity(1, 1)),
        Property(name="Root", type=Root, multiplicity=Multiplicity(1, 1))
    }
)
directories63: BinaryAssociation = BinaryAssociation(
    name="directories63",
    ends={
        Property(name="core64", type=gast_core_BasePath, multiplicity=Multiplicity(1, 1)),
        Property(name="Directory", type=Directory, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotations65: BinaryAssociation = BinaryAssociation(
    name="annotations65",
    ends={
        Property(name="ModelAnnotation", type=gast_core_ModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_ModelElement", type=ModelAnnotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
allLocalClasses66: BinaryAssociation = BinaryAssociation(
    name="allLocalClasses66",
    ends={
        Property(name="GASTClass", type=gast_core_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_Package", type=GASTClass, multiplicity=Multiplicity(0, 9999))
    }
)
allInnerClasses67: BinaryAssociation = BinaryAssociation(
    name="allInnerClasses67",
    ends={
        Property(name="GASTClass69", type=gast_core_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_Package68", type=GASTClass, multiplicity=Multiplicity(0, 9999))
    }
)
allNormalClasses70: BinaryAssociation = BinaryAssociation(
    name="allNormalClasses70",
    ends={
        Property(name="GASTClass72", type=gast_core_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_Package71", type=GASTClass, multiplicity=Multiplicity(0, 9999))
    }
)
allInterfaces73: BinaryAssociation = BinaryAssociation(
    name="allInterfaces73",
    ends={
        Property(name="GASTClass75", type=gast_core_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_Package74", type=GASTClass, multiplicity=Multiplicity(0, 9999))
    }
)
allAccesses76: BinaryAssociation = BinaryAssociation(
    name="allAccesses76",
    ends={
        Property(name="Access", type=gast_core_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_Package77", type=Access, multiplicity=Multiplicity(0, 9999))
    }
)
delegates78: BinaryAssociation = BinaryAssociation(
    name="delegates78",
    ends={
        Property(name="functions79", type=gast_core_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="Delegate", type=Delegate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
globalFunctions80: BinaryAssociation = BinaryAssociation(
    name="globalFunctions80",
    ends={
        Property(name="functions81", type=gast_core_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="GlobalFunction", type=GlobalFunction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
globalVariables82: BinaryAssociation = BinaryAssociation(
    name="globalVariables82",
    ends={
        Property(name="variables", type=gast_core_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="GlobalVariable", type=GlobalVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
root83: BinaryAssociation = BinaryAssociation(
    name="root83",
    ends={
        Property(name="core85", type=gast_core_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="Root84", type=Root, multiplicity=Multiplicity(0, 1))
    }
)
classes86: BinaryAssociation = BinaryAssociation(
    name="classes86",
    ends={
        Property(name="types", type=gast_core_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="GASTClass87", type=GASTClass, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
surroundingPackage90: BinaryAssociation = BinaryAssociation(
    name="surroundingPackage90",
    ends={
        Property(name="core92", type=gast_core_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="Package91", type=Package, multiplicity=Multiplicity(0, 1))
    }
)
allAccessedPackages93: BinaryAssociation = BinaryAssociation(
    name="allAccessedPackages93",
    ends={
        Property(name="Package95", type=gast_core_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_Package94", type=Package, multiplicity=Multiplicity(0, 9999))
    }
)
typeAliases96: BinaryAssociation = BinaryAssociation(
    name="typeAliases96",
    ends={
        Property(name="types97", type=gast_core_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="TypeAlias", type=TypeAlias, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeParameters98: BinaryAssociation = BinaryAssociation(
    name="typeParameters98",
    ends={
        Property(name="TypeParameterClass", type=gast_core_GenericEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_GenericEntity", type=TypeParameterClass, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subPackages88: BinaryAssociation = BinaryAssociation(
    name="subPackages88",
    ends={
        Property(name="core89", type=gast_core_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="Package", type=Package, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
allAccesses99: BinaryAssociation = BinaryAssociation(
    name="allAccesses99",
    ends={
        Property(name="Access100", type=gast_core_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_Root", type=Access, multiplicity=Multiplicity(0, 9999))
    }
)
allInnerClasses101: BinaryAssociation = BinaryAssociation(
    name="allInnerClasses101",
    ends={
        Property(name="GASTClass103", type=gast_core_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_Root102", type=GASTClass, multiplicity=Multiplicity(0, 9999))
    }
)
allInterfaces104: BinaryAssociation = BinaryAssociation(
    name="allInterfaces104",
    ends={
        Property(name="GASTClass106", type=gast_core_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_Root105", type=GASTClass, multiplicity=Multiplicity(0, 9999))
    }
)
allLocalClasses107: BinaryAssociation = BinaryAssociation(
    name="allLocalClasses107",
    ends={
        Property(name="GASTClass109", type=gast_core_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_Root108", type=GASTClass, multiplicity=Multiplicity(0, 9999))
    }
)
allNormalClasses110: BinaryAssociation = BinaryAssociation(
    name="allNormalClasses110",
    ends={
        Property(name="GASTClass112", type=gast_core_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_Root111", type=GASTClass, multiplicity=Multiplicity(0, 9999))
    }
)
allModelElements113: BinaryAssociation = BinaryAssociation(
    name="allModelElements113",
    ends={
        Property(name="ModelElement", type=gast_core_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_Root114", type=ModelElement, multiplicity=Multiplicity(0, 9999))
    }
)
globalVariables115: BinaryAssociation = BinaryAssociation(
    name="globalVariables115",
    ends={
        Property(name="GlobalVariable117", type=gast_core_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_Root116", type=GlobalVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
packages118: BinaryAssociation = BinaryAssociation(
    name="packages118",
    ends={
        Property(name="core120", type=gast_core_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="Package119", type=Package, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
clones121: BinaryAssociation = BinaryAssociation(
    name="clones121",
    ends={
        Property(name="annotations122", type=gast_core_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="Clone", type=Clone, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
structuralAbstractions123: BinaryAssociation = BinaryAssociation(
    name="structuralAbstractions123",
    ends={
        Property(name="StructuralAbstraction", type=gast_core_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_Root124", type=StructuralAbstraction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
danglingModelElements127: BinaryAssociation = BinaryAssociation(
    name="danglingModelElements127",
    ends={
        Property(name="ModelElement129", type=gast_core_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_Root128", type=ModelElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
basePaths130: BinaryAssociation = BinaryAssociation(
    name="basePaths130",
    ends={
        Property(name="core131", type=gast_core_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="BasePath", type=BasePath, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
globalFunctions132: BinaryAssociation = BinaryAssociation(
    name="globalFunctions132",
    ends={
        Property(name="functions134", type=gast_core_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="GlobalFunction133", type=GlobalFunction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
types125: BinaryAssociation = BinaryAssociation(
    name="types125",
    ends={
        Property(name="GASTType", type=gast_core_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_Root126", type=GASTType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subDirectory135: BinaryAssociation = BinaryAssociation(
    name="subDirectory135",
    ends={
        Property(name="core137", type=gast_core_Directory, multiplicity=Multiplicity(1, 1)),
        Property(name="Directory136", type=Directory, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentDirectory138: BinaryAssociation = BinaryAssociation(
    name="parentDirectory138",
    ends={
        Property(name="core140", type=gast_core_Directory, multiplicity=Multiplicity(1, 1)),
        Property(name="Directory139", type=Directory, multiplicity=Multiplicity(0, 1))
    }
)
files141: BinaryAssociation = BinaryAssociation(
    name="files141",
    ends={
        Property(name="core142", type=gast_core_Directory, multiplicity=Multiplicity(1, 1)),
        Property(name="File", type=File, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
basePath143: BinaryAssociation = BinaryAssociation(
    name="basePath143",
    ends={
        Property(name="core145", type=gast_core_Directory, multiplicity=Multiplicity(1, 1)),
        Property(name="BasePath144", type=BasePath, multiplicity=Multiplicity(0, 1))
    }
)
importedTypes148: BinaryAssociation = BinaryAssociation(
    name="importedTypes148",
    ends={
        Property(name="GASTType150", type=gast_core_File, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_File149", type=GASTType, multiplicity=Multiplicity(0, 9999))
    }
)
types151: BinaryAssociation = BinaryAssociation(
    name="types151",
    ends={
        Property(name="GASTType153", type=gast_core_File, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_File152", type=GASTType, multiplicity=Multiplicity(0, 9999))
    }
)
globalVariables154: BinaryAssociation = BinaryAssociation(
    name="globalVariables154",
    ends={
        Property(name="GlobalVariable156", type=gast_core_File, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_File155", type=GlobalVariable, multiplicity=Multiplicity(0, 9999))
    }
)
globalFunctions157: BinaryAssociation = BinaryAssociation(
    name="globalFunctions157",
    ends={
        Property(name="GlobalFunction159", type=gast_core_File, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_File158", type=GlobalFunction, multiplicity=Multiplicity(0, 9999))
    }
)
root146: BinaryAssociation = BinaryAssociation(
    name="root146",
    ends={
        Property(name="Root147", type=gast_core_File, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_File", type=Root, multiplicity=Multiplicity(1, 1))
    }
)
importedGlobalFunctions160: BinaryAssociation = BinaryAssociation(
    name="importedGlobalFunctions160",
    ends={
        Property(name="GlobalFunction162", type=gast_core_File, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_File161", type=GlobalFunction, multiplicity=Multiplicity(0, 9999))
    }
)
importedGlobalVariables163: BinaryAssociation = BinaryAssociation(
    name="importedGlobalVariables163",
    ends={
        Property(name="GlobalVariable165", type=gast_core_File, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_File164", type=GlobalVariable, multiplicity=Multiplicity(0, 9999))
    }
)
importedPackages166: BinaryAssociation = BinaryAssociation(
    name="importedPackages166",
    ends={
        Property(name="Package168", type=gast_core_File, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_File167", type=Package, multiplicity=Multiplicity(0, 9999))
    }
)
includedFiles169: BinaryAssociation = BinaryAssociation(
    name="includedFiles169",
    ends={
        Property(name="File171", type=gast_core_File, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_File170", type=File, multiplicity=Multiplicity(0, 9999))
    }
)
directory172: BinaryAssociation = BinaryAssociation(
    name="directory172",
    ends={
        Property(name="core174", type=gast_core_File, multiplicity=Multiplicity(1, 1)),
        Property(name="Directory173", type=Directory, multiplicity=Multiplicity(1, 1))
    }
)
sourceFile175: BinaryAssociation = BinaryAssociation(
    name="sourceFile175",
    ends={
        Property(name="File176", type=gast_core_Position, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_Position", type=File, multiplicity=Multiplicity(0, 1))
    }
)
assembly177: BinaryAssociation = BinaryAssociation(
    name="assembly177",
    ends={
        Property(name="File179", type=gast_core_Position, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_Position178", type=File, multiplicity=Multiplicity(0, 1))
    }
)
sourceentity180: BinaryAssociation = BinaryAssociation(
    name="sourceentity180",
    ends={
        Property(name="core181", type=gast_core_Position, multiplicity=Multiplicity(1, 1)),
        Property(name="SourceEntity", type=SourceEntity, multiplicity=Multiplicity(1, 1))
    }
)
aliasedPackage182: BinaryAssociation = BinaryAssociation(
    name="aliasedPackage182",
    ends={
        Property(name="Package183", type=gast_core_PackageAlias, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_PackageAlias", type=Package, multiplicity=Multiplicity(1, 1))
    }
)
position184: BinaryAssociation = BinaryAssociation(
    name="position184",
    ends={
        Property(name="core185", type=gast_core_SourceEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="Position", type=Position, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cloneInstances186: BinaryAssociation = BinaryAssociation(
    name="cloneInstances186",
    ends={
        Property(name="annotations188", type=gast_annotations_Clone, multiplicity=Multiplicity(1, 1)),
        Property(name="CloneInstance187", type=CloneInstance, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
root189: BinaryAssociation = BinaryAssociation(
    name="root189",
    ends={
        Property(name="core191", type=gast_annotations_Clone, multiplicity=Multiplicity(1, 1)),
        Property(name="Root190", type=Root, multiplicity=Multiplicity(1, 1))
    }
)
statements192: BinaryAssociation = BinaryAssociation(
    name="statements192",
    ends={
        Property(name="statements194", type=gast_annotations_CloneInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="Statement193", type=Statement, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
clone195: BinaryAssociation = BinaryAssociation(
    name="clone195",
    ends={
        Property(name="annotations197", type=gast_annotations_CloneInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="Clone196", type=Clone, multiplicity=Multiplicity(1, 1))
    }
)
referencedType198: BinaryAssociation = BinaryAssociation(
    name="referencedType198",
    ends={
        Property(name="gast_types_Reference", type=GASTType, multiplicity=Multiplicity(1, 1)),
        Property(name="GASTType199", type=gast_types_Reference, multiplicity=Multiplicity(1, 1))
    }
)
decoratedType200: BinaryAssociation = BinaryAssociation(
    name="decoratedType200",
    ends={
        Property(name="GASTType201", type=gast_types_TypeDecorator, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_types_TypeDecorator", type=GASTType, multiplicity=Multiplicity(1, 1))
    }
)
undecoratedType202: BinaryAssociation = BinaryAssociation(
    name="undecoratedType202",
    ends={
        Property(name="GASTType204", type=gast_types_TypeDecorator, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_types_TypeDecorator203", type=GASTType, multiplicity=Multiplicity(1, 1))
    }
)
baseType205: BinaryAssociation = BinaryAssociation(
    name="baseType205",
    ends={
        Property(name="GASTType206", type=gast_types_GASTArray, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_types_GASTArray", type=GASTType, multiplicity=Multiplicity(1, 1))
    }
)
aliasedType207: BinaryAssociation = BinaryAssociation(
    name="aliasedType207",
    ends={
        Property(name="GASTType208", type=gast_types_TypeAlias, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_types_TypeAlias", type=GASTType, multiplicity=Multiplicity(1, 1))
    }
)
surroundingClass209: BinaryAssociation = BinaryAssociation(
    name="surroundingClass209",
    ends={
        Property(name="types211", type=gast_types_TypeAlias, multiplicity=Multiplicity(1, 1)),
        Property(name="GASTClass210", type=GASTClass, multiplicity=Multiplicity(0, 1))
    }
)
surroundingPackage212: BinaryAssociation = BinaryAssociation(
    name="surroundingPackage212",
    ends={
        Property(name="core214", type=gast_types_TypeAlias, multiplicity=Multiplicity(1, 1)),
        Property(name="Package213", type=Package, multiplicity=Multiplicity(0, 1))
    }
)
overriddenMember215: BinaryAssociation = BinaryAssociation(
    name="overriddenMember215",
    ends={
        Property(name="Member", type=gast_types_Member, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_types_Member", type=Member, multiplicity=Multiplicity(0, 1))
    }
)
typeBounds216: BinaryAssociation = BinaryAssociation(
    name="typeBounds216",
    ends={
        Property(name="GASTType217", type=gast_types_TypeParameterClass, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_types_TypeParameterClass", type=GASTType, multiplicity=Multiplicity(0, 9999))
    }
)
innerTypeAliases218: BinaryAssociation = BinaryAssociation(
    name="innerTypeAliases218",
    ends={
        Property(name="types220", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="TypeAlias219", type=TypeAlias, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
innerDelegates221: BinaryAssociation = BinaryAssociation(
    name="innerDelegates221",
    ends={
        Property(name="functions223", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="Delegate222", type=Delegate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
constructors224: BinaryAssociation = BinaryAssociation(
    name="constructors224",
    ends={
        Property(name="functions225", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="Constructor", type=Constructor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
destructors226: BinaryAssociation = BinaryAssociation(
    name="destructors226",
    ends={
        Property(name="functions227", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="Destructor", type=Destructor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fields228: BinaryAssociation = BinaryAssociation(
    name="fields228",
    ends={
        Property(name="variables229", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="Field", type=Field, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
methods230: BinaryAssociation = BinaryAssociation(
    name="methods230",
    ends={
        Property(name="functions231", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="Method", type=Method_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
surroundingFunction232: BinaryAssociation = BinaryAssociation(
    name="surroundingFunction232",
    ends={
        Property(name="functions234", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="Function233", type=Function, multiplicity=Multiplicity(0, 1))
    }
)
surroundingPackage235: BinaryAssociation = BinaryAssociation(
    name="surroundingPackage235",
    ends={
        Property(name="core237", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="Package236", type=Package, multiplicity=Multiplicity(0, 1))
    }
)
innerClasses240: BinaryAssociation = BinaryAssociation(
    name="innerClasses240",
    ends={
        Property(name="types242", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="GASTClass241", type=GASTClass, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
surroundingClass243: BinaryAssociation = BinaryAssociation(
    name="surroundingClass243",
    ends={
        Property(name="types245", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="GASTClass244", type=GASTClass, multiplicity=Multiplicity(0, 1))
    }
)
superTypes238: BinaryAssociation = BinaryAssociation(
    name="superTypes238",
    ends={
        Property(name="GASTClass239", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_types_GASTClass", type=GASTClass, multiplicity=Multiplicity(0, 9999))
    }
)
self248: BinaryAssociation = BinaryAssociation(
    name="self248",
    ends={
        Property(name="Field250", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_types_GASTClass249", type=Field, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
friendClasses251: BinaryAssociation = BinaryAssociation(
    name="friendClasses251",
    ends={
        Property(name="types253", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="GASTClass252", type=GASTClass, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
gastClass254: BinaryAssociation = BinaryAssociation(
    name="gastClass254",
    ends={
        Property(name="types256", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="GASTClass255", type=GASTClass, multiplicity=Multiplicity(0, 1))
    }
)
friendFunctions257: BinaryAssociation = BinaryAssociation(
    name="friendFunctions257",
    ends={
        Property(name="Function259", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_types_GASTClass258", type=Function, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
property260: BinaryAssociation = BinaryAssociation(
    name="property260",
    ends={
        Property(name="Property", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_types_GASTClass261", type=Property_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
allAccesses262: BinaryAssociation = BinaryAssociation(
    name="allAccesses262",
    ends={
        Property(name="Access264", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_types_GASTClass263", type=Access, multiplicity=Multiplicity(0, 9999))
    }
)
inheritanceTypeAccesses246: BinaryAssociation = BinaryAssociation(
    name="inheritanceTypeAccesses246",
    ends={
        Property(name="InheritanceTypeAccess", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_types_GASTClass247", type=InheritanceTypeAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
allAccessedClasses265: BinaryAssociation = BinaryAssociation(
    name="allAccessedClasses265",
    ends={
        Property(name="gast_types_GASTClass266", type=GASTClass, multiplicity=Multiplicity(0, 9999)),
        Property(name="GASTClass267", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1))
    }
)
targetType268: BinaryAssociation = BinaryAssociation(
    name="targetType268",
    ends={
        Property(name="GASTType269", type=gast_accesses_TypeAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_accesses_TypeAccess", type=GASTType, multiplicity=Multiplicity(1, 1))
    }
)
typeArguments270: BinaryAssociation = BinaryAssociation(
    name="typeArguments270",
    ends={
        Property(name="GASTType272", type=gast_accesses_TypeAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_accesses_TypeAccess271", type=GASTType, multiplicity=Multiplicity(0, 9999))
    }
)
accesses273: BinaryAssociation = BinaryAssociation(
    name="accesses273",
    ends={
        Property(name="accesses275", type=gast_accesses_CompositeAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="BaseAccess274", type=BaseAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentStatement276: BinaryAssociation = BinaryAssociation(
    name="parentStatement276",
    ends={
        Property(name="statements278", type=gast_accesses_BaseAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="Statement277", type=Statement, multiplicity=Multiplicity(0, 1))
    }
)
surroundingStatement279: BinaryAssociation = BinaryAssociation(
    name="surroundingStatement279",
    ends={
        Property(name="Statement280", type=gast_accesses_BaseAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_accesses_BaseAccess", type=Statement, multiplicity=Multiplicity(0, 1))
    }
)
surroundingClass281: BinaryAssociation = BinaryAssociation(
    name="surroundingClass281",
    ends={
        Property(name="GASTClass283", type=gast_accesses_BaseAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_accesses_BaseAccess282", type=GASTClass, multiplicity=Multiplicity(1, 1))
    }
)
surroundingFunction284: BinaryAssociation = BinaryAssociation(
    name="surroundingFunction284",
    ends={
        Property(name="Function286", type=gast_accesses_BaseAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_accesses_BaseAccess285", type=Function, multiplicity=Multiplicity(0, 1))
    }
)
surroundingCompositeAccess287: BinaryAssociation = BinaryAssociation(
    name="surroundingCompositeAccess287",
    ends={
        Property(name="accesses288", type=gast_accesses_BaseAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="CompositeAccess", type=CompositeAccess, multiplicity=Multiplicity(0, 1))
    }
)
function289: BinaryAssociation = BinaryAssociation(
    name="function289",
    ends={
        Property(name="functions291", type=gast_accesses_DeclarationTypeAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="Function290", type=Function, multiplicity=Multiplicity(0, 1))
    }
)
surroundingVariable292: BinaryAssociation = BinaryAssociation(
    name="surroundingVariable292",
    ends={
        Property(name="variables293", type=gast_accesses_DeclarationTypeAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="Variable", type=Variable, multiplicity=Multiplicity(0, 1))
    }
)
accessedFunctions294: BinaryAssociation = BinaryAssociation(
    name="accessedFunctions294",
    ends={
        Property(name="Function295", type=gast_accesses_DelegateAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_accesses_DelegateAccess", type=Function, multiplicity=Multiplicity(0, 9999))
    }
)
accessedDelegate296: BinaryAssociation = BinaryAssociation(
    name="accessedDelegate296",
    ends={
        Property(name="Delegate298", type=gast_accesses_DelegateAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_accesses_DelegateAccess297", type=Delegate, multiplicity=Multiplicity(1, 1))
    }
)
typeArguments299: BinaryAssociation = BinaryAssociation(
    name="typeArguments299",
    ends={
        Property(name="GASTType300", type=gast_accesses_FunctionAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_accesses_FunctionAccess", type=GASTType, multiplicity=Multiplicity(0, 9999))
    }
)
targetFunction301: BinaryAssociation = BinaryAssociation(
    name="targetFunction301",
    ends={
        Property(name="Function303", type=gast_accesses_FunctionAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_accesses_FunctionAccess302", type=Function, multiplicity=Multiplicity(1, 1))
    }
)
targetVariable304: BinaryAssociation = BinaryAssociation(
    name="targetVariable304",
    ends={
        Property(name="Variable305", type=gast_accesses_VariableAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_accesses_VariableAccess", type=Variable, multiplicity=Multiplicity(1, 1))
    }
)
accessedTarget308: BinaryAssociation = BinaryAssociation(
    name="accessedTarget308",
    ends={
        Property(name="ModelElement310", type=gast_accesses_Access, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_accesses_Access309", type=ModelElement, multiplicity=Multiplicity(1, 1))
    }
)
accessedClass306: BinaryAssociation = BinaryAssociation(
    name="accessedClass306",
    ends={
        Property(name="GASTClass307", type=gast_accesses_Access, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_accesses_Access", type=GASTClass, multiplicity=Multiplicity(1, 1))
    }
)
invocations313: BinaryAssociation = BinaryAssociation(
    name="invocations313",
    ends={
        Property(name="Function315", type=gast_functions_Delegate, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_functions_Delegate314", type=Function, multiplicity=Multiplicity(0, 9999))
    }
)
surroundingClass316: BinaryAssociation = BinaryAssociation(
    name="surroundingClass316",
    ends={
        Property(name="types318", type=gast_functions_Delegate, multiplicity=Multiplicity(1, 1)),
        Property(name="GASTClass317", type=GASTClass, multiplicity=Multiplicity(0, 1))
    }
)
surroundingPackage319: BinaryAssociation = BinaryAssociation(
    name="surroundingPackage319",
    ends={
        Property(name="core321", type=gast_functions_Delegate, multiplicity=Multiplicity(1, 1)),
        Property(name="Package320", type=Package, multiplicity=Multiplicity(0, 1))
    }
)
surroundingClass322: BinaryAssociation = BinaryAssociation(
    name="surroundingClass322",
    ends={
        Property(name="types324", type=gast_functions_Constructor, multiplicity=Multiplicity(1, 1)),
        Property(name="GASTClass323", type=GASTClass, multiplicity=Multiplicity(1, 1))
    }
)
superClass311: BinaryAssociation = BinaryAssociation(
    name="superClass311",
    ends={
        Property(name="GASTClass312", type=gast_functions_Delegate, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_functions_Delegate", type=GASTClass, multiplicity=Multiplicity(0, 1))
    }
)
surroundingClass325: BinaryAssociation = BinaryAssociation(
    name="surroundingClass325",
    ends={
        Property(name="GASTClass326", type=GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="types327", type=gast_functions_Destructor, multiplicity=Multiplicity(1, 1))
    }
)
surroundingPackage328: BinaryAssociation = BinaryAssociation(
    name="surroundingPackage328",
    ends={
        Property(name="core330", type=gast_functions_GlobalFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="Package329", type=Package, multiplicity=Multiplicity(0, 1))
    }
)
root331: BinaryAssociation = BinaryAssociation(
    name="root331",
    ends={
        Property(name="core333", type=gast_functions_GlobalFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="Root332", type=Root, multiplicity=Multiplicity(0, 1))
    }
)
surroundingProperty334: BinaryAssociation = BinaryAssociation(
    name="surroundingProperty334",
    ends={
        Property(name="Property335", type=gast_functions_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_functions_Method", type=Property_, multiplicity=Multiplicity(0, 1))
    }
)
surroundingClass336: BinaryAssociation = BinaryAssociation(
    name="surroundingClass336",
    ends={
        Property(name="types338", type=gast_functions_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="GASTClass337", type=GASTClass, multiplicity=Multiplicity(1, 1))
    }
)
returnTypeDeclaration339: BinaryAssociation = BinaryAssociation(
    name="returnTypeDeclaration339",
    ends={
        Property(name="accesses340", type=gast_functions_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="DeclarationTypeAccess", type=DeclarationTypeAccess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
formalParameters341: BinaryAssociation = BinaryAssociation(
    name="formalParameters341",
    ends={
        Property(name="variables342", type=gast_functions_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="FormalParameter", type=FormalParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
localVariables343: BinaryAssociation = BinaryAssociation(
    name="localVariables343",
    ends={
        Property(name="variables344", type=gast_functions_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="LocalVariable", type=LocalVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
allStatements345: BinaryAssociation = BinaryAssociation(
    name="allStatements345",
    ends={
        Property(name="Statement346", type=gast_functions_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_functions_Function", type=Statement, multiplicity=Multiplicity(0, 9999))
    }
)
throwTypeAccesses347: BinaryAssociation = BinaryAssociation(
    name="throwTypeAccesses347",
    ends={
        Property(name="ThrowTypeAccess", type=gast_functions_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_functions_Function348", type=ThrowTypeAccess, multiplicity=Multiplicity(0, 9999))
    }
)
accesses349: BinaryAssociation = BinaryAssociation(
    name="accesses349",
    ends={
        Property(name="Access351", type=gast_functions_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_functions_Function350", type=Access, multiplicity=Multiplicity(0, 9999))
    }
)
body352: BinaryAssociation = BinaryAssociation(
    name="body352",
    ends={
        Property(name="statements354", type=gast_functions_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="BlockStatement353", type=BlockStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
localClasses355: BinaryAssociation = BinaryAssociation(
    name="localClasses355",
    ends={
        Property(name="types357", type=gast_functions_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="GASTClass356", type=GASTClass, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
surroundingFunction358: BinaryAssociation = BinaryAssociation(
    name="surroundingFunction358",
    ends={
        Property(name="functions360", type=gast_variables_FormalParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="Function359", type=Function, multiplicity=Multiplicity(1, 1))
    }
)
type361: BinaryAssociation = BinaryAssociation(
    name="type361",
    ends={
        Property(name="GASTType362", type=gast_variables_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_variables_Variable", type=GASTType, multiplicity=Multiplicity(1, 1))
    }
)
typeDeclaration363: BinaryAssociation = BinaryAssociation(
    name="typeDeclaration363",
    ends={
        Property(name="accesses365", type=gast_variables_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="DeclarationTypeAccess364", type=DeclarationTypeAccess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
surroundingClass366: BinaryAssociation = BinaryAssociation(
    name="surroundingClass366",
    ends={
        Property(name="types368", type=gast_variables_Field, multiplicity=Multiplicity(1, 1)),
        Property(name="GASTClass367", type=GASTClass, multiplicity=Multiplicity(0, 1))
    }
)
surroundingFunction369: BinaryAssociation = BinaryAssociation(
    name="surroundingFunction369",
    ends={
        Property(name="functions371", type=gast_variables_LocalVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="Function370", type=Function, multiplicity=Multiplicity(1, 1))
    }
)
setter372: BinaryAssociation = BinaryAssociation(
    name="setter372",
    ends={
        Property(name="Method373", type=gast_variables_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_variables_Property", type=Method_, multiplicity=Multiplicity(0, 1))
    }
)
getter374: BinaryAssociation = BinaryAssociation(
    name="getter374",
    ends={
        Property(name="Method376", type=gast_variables_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_variables_Property375", type=Method_, multiplicity=Multiplicity(0, 1))
    }
)
surroundingPackage377: BinaryAssociation = BinaryAssociation(
    name="surroundingPackage377",
    ends={
        Property(name="core379", type=gast_variables_GlobalVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="Package378", type=Package, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_gast_statements_ExceptionHandler_Statement = Generalization(general=Statement, specific=gast_statements_ExceptionHandler)
gen_gast_statements_Statement_SourceEntity = Generalization(general=SourceEntity, specific=gast_statements_Statement)
gen_gast_statements_Branch_SourceEntity = Generalization(general=SourceEntity, specific=gast_statements_Branch)
gen_gast_statements_BlockStatement_Statement = Generalization(general=Statement, specific=gast_statements_BlockStatement)
gen_gast_statements_GASTExpression_SourceEntity = Generalization(general=SourceEntity, specific=gast_statements_GASTExpression)
gen_gast_statements_BranchStatement_Statement = Generalization(general=Statement, specific=gast_statements_BranchStatement)
gen_gast_statements_LoopStatement_Statement = Generalization(general=Statement, specific=gast_statements_LoopStatement)
gen_gast_statements_CatchBlock_BlockStatement = Generalization(general=BlockStatement, specific=gast_statements_CatchBlock)
gen_gast_statements_SimpleStatement_statements_Statement = Generalization(general=statements_Statement, specific=gast_statements_SimpleStatement)
gen_gast_statements_SimpleStatement_statements_FlowInstr = Generalization(general=statements_FlowInstr, specific=gast_statements_SimpleStatement)
gen_gast_statements_JumpStatement_statements_Statement = Generalization(general=statements_Statement, specific=gast_statements_JumpStatement)
gen_gast_statements_JumpStatement_statements_FlowInstr = Generalization(general=statements_FlowInstr, specific=gast_statements_JumpStatement)
gen_gast_statements_Methods_statements_BlockStatement = Generalization(general=statements_BlockStatement, specific=gast_statements_Methods)
gen_gast_statements_Methods_statements_FlowInstr = Generalization(general=statements_FlowInstr, specific=gast_statements_Methods)
gen_gast_statements_Exit_FlowInstr = Generalization(general=FlowInstr, specific=gast_statements_Exit)
gen_gast_statements_Param_Var = Generalization(general=Var, specific=gast_statements_Param)
gen_gast_core_BasePath_ModelElement = Generalization(general=ModelElement, specific=gast_core_BasePath)
gen_gast_core_NamedModelElement_ModelElement = Generalization(general=ModelElement, specific=gast_core_NamedModelElement)
gen_gast_core_ModelElement_Identifier = Generalization(general=Identifier, specific=gast_core_ModelElement)
gen_gast_core_Package_NamedModelElement = Generalization(general=NamedModelElement, specific=gast_core_Package)
gen_gast_core_GenericEntity_ModelElement = Generalization(general=ModelElement, specific=gast_core_GenericEntity)
gen_gast_core_Root_ModelElement = Generalization(general=ModelElement, specific=gast_core_Root)
gen_gast_core_Directory_NamedModelElement = Generalization(general=NamedModelElement, specific=gast_core_Directory)
gen_gast_core_File_NamedModelElement = Generalization(general=NamedModelElement, specific=gast_core_File)
gen_gast_core_PackageAlias_Package = Generalization(general=Package, specific=gast_core_PackageAlias)
gen_gast_core_SourceEntity_ModelElement = Generalization(general=ModelElement, specific=gast_core_SourceEntity)
gen_gast_annotations_Attribute_types_GASTClass = Generalization(general=types_GASTClass, specific=gast_annotations_Attribute)
gen_gast_annotations_Attribute_annotations_ModelAnnotation = Generalization(general=annotations_ModelAnnotation, specific=gast_annotations_Attribute)
gen_gast_annotations_Clone_core_ModelElement = Generalization(general=core_ModelElement, specific=gast_annotations_Clone)
gen_gast_annotations_Clone_annotations_ModelAnnotation = Generalization(general=annotations_ModelAnnotation, specific=gast_annotations_Clone)
gen_gast_annotations_CloneInstance_core_ModelElement = Generalization(general=core_ModelElement, specific=gast_annotations_CloneInstance)
gen_gast_annotations_CloneInstance_annotations_ModelAnnotation = Generalization(general=annotations_ModelAnnotation, specific=gast_annotations_CloneInstance)
gen_gast_annotations_StructuralAbstraction_core_NamedModelElement = Generalization(general=core_NamedModelElement, specific=gast_annotations_StructuralAbstraction)
gen_gast_annotations_StructuralAbstraction_annotations_ModelAnnotation = Generalization(general=annotations_ModelAnnotation, specific=gast_annotations_StructuralAbstraction)
gen_gast_annotations_Comment_core_SourceEntity = Generalization(general=core_SourceEntity, specific=gast_annotations_Comment)
gen_gast_annotations_Comment_annotations_ModelAnnotation = Generalization(general=annotations_ModelAnnotation, specific=gast_annotations_Comment)
gen_gast_annotations_Subsystem_StructuralAbstraction = Generalization(general=StructuralAbstraction, specific=gast_annotations_Subsystem)
gen_gast_annotations_Layer_StructuralAbstraction = Generalization(general=StructuralAbstraction, specific=gast_annotations_Layer)
gen_gast_types_Reference_TypeDecorator = Generalization(general=TypeDecorator, specific=gast_types_Reference)
gen_gast_types_TypeDecorator_GASTType = Generalization(general=GASTType, specific=gast_types_TypeDecorator)
gen_gast_types_GASTType_NamedModelElement = Generalization(general=NamedModelElement, specific=gast_types_GASTType)
gen_gast_types_GASTArray_TypeDecorator = Generalization(general=TypeDecorator, specific=gast_types_GASTArray)
gen_gast_types_TypeAlias_types_Member = Generalization(general=types_Member, specific=gast_types_TypeAlias)
gen_gast_types_TypeAlias_types_TypeDecorator = Generalization(general=types_TypeDecorator, specific=gast_types_TypeAlias)
gen_gast_types_Member_SourceEntity = Generalization(general=SourceEntity, specific=gast_types_Member)
gen_gast_types_TypeParameterClass_GASTClass = Generalization(general=GASTClass, specific=gast_types_TypeParameterClass)
gen_gast_types_GenericClass_types_GASTClass = Generalization(general=types_GASTClass, specific=gast_types_GenericClass)
gen_gast_types_GenericClass_core_GenericEntity = Generalization(general=core_GenericEntity, specific=gast_types_GenericClass)
gen_gast_types_GASTEnumeration_GASTClass = Generalization(general=GASTClass, specific=gast_types_GASTEnumeration)
gen_gast_types_GASTStruct_GASTClass = Generalization(general=GASTClass, specific=gast_types_GASTStruct)
gen_gast_types_GASTUnion_GASTClass = Generalization(general=GASTClass, specific=gast_types_GASTUnion)
gen_gast_types_GASTClass_types_Member = Generalization(general=types_Member, specific=gast_types_GASTClass)
gen_gast_types_GASTClass_types_GASTType = Generalization(general=types_GASTType, specific=gast_types_GASTClass)
gen_gast_accesses_ParameterInstantiationTypeAccess_TypeAccess = Generalization(general=TypeAccess, specific=gast_accesses_ParameterInstantiationTypeAccess)
gen_gast_accesses_TypeAccess_Access = Generalization(general=Access, specific=gast_accesses_TypeAccess)
gen_gast_accesses_CastTypeAccess_TypeAccess = Generalization(general=TypeAccess, specific=gast_accesses_CastTypeAccess)
gen_gast_accesses_BaseAccess_SourceEntity = Generalization(general=SourceEntity, specific=gast_accesses_BaseAccess)
gen_gast_accesses_CompositeAccess_BaseAccess = Generalization(general=BaseAccess, specific=gast_accesses_CompositeAccess)
gen_gast_accesses_DeclarationTypeAccess_TypeAccess = Generalization(general=TypeAccess, specific=gast_accesses_DeclarationTypeAccess)
gen_gast_accesses_ThrowTypeAccess_TypeAccess = Generalization(general=TypeAccess, specific=gast_accesses_ThrowTypeAccess)
gen_gast_accesses_FunctionAccess_Access = Generalization(general=Access, specific=gast_accesses_FunctionAccess)
gen_gast_accesses_DelegateAccess_FunctionAccess = Generalization(general=FunctionAccess, specific=gast_accesses_DelegateAccess)
gen_gast_accesses_VariableAccess_Access = Generalization(general=Access, specific=gast_accesses_VariableAccess)
gen_gast_accesses_RunTimeTypeAccess_TypeAccess = Generalization(general=TypeAccess, specific=gast_accesses_RunTimeTypeAccess)
gen_gast_accesses_SelfAccess_VariableAccess = Generalization(general=VariableAccess, specific=gast_accesses_SelfAccess)
gen_gast_accesses_StaticTypeAccess_TypeAccess = Generalization(general=TypeAccess, specific=gast_accesses_StaticTypeAccess)
gen_gast_accesses_PropertyAccess_VariableAccess = Generalization(general=VariableAccess, specific=gast_accesses_PropertyAccess)
gen_gast_accesses_Access_BaseAccess = Generalization(general=BaseAccess, specific=gast_accesses_Access)
gen_gast_accesses_InheritanceTypeAccess_TypeAccess = Generalization(general=TypeAccess, specific=gast_accesses_InheritanceTypeAccess)
gen_gast_functions_Delegate_functions_Function = Generalization(general=functions_Function, specific=gast_functions_Delegate)
gen_gast_functions_Delegate_types_Member = Generalization(general=types_Member, specific=gast_functions_Delegate)
gen_gast_functions_Delegate_types_GASTType = Generalization(general=types_GASTType, specific=gast_functions_Delegate)
gen_gast_functions_Constructor_functions_Function = Generalization(general=functions_Function, specific=gast_functions_Constructor)
gen_gast_functions_Constructor_types_Member = Generalization(general=types_Member, specific=gast_functions_Constructor)
gen_gast_functions_GenericFunction_functions_GlobalFunction = Generalization(general=functions_GlobalFunction, specific=gast_functions_GenericFunction)
gen_gast_functions_GenericFunction_core_GenericEntity = Generalization(general=core_GenericEntity, specific=gast_functions_GenericFunction)
gen_gast_functions_GlobalFunction_Function = Generalization(general=Function, specific=gast_functions_GlobalFunction)
gen_gast_functions_Method_functions_Function = Generalization(general=functions_Function, specific=gast_functions_Method)
gen_gast_functions_Method_types_Member = Generalization(general=types_Member, specific=gast_functions_Method)
gen_gast_functions_Destructor_functions_Function = Generalization(general=functions_Function, specific=gast_functions_Destructor)
gen_gast_functions_Destructor_types_Member = Generalization(general=types_Member, specific=gast_functions_Destructor)
gen_gast_functions_GenericMethod_functions_Method = Generalization(general=functions_Method, specific=gast_functions_GenericMethod)
gen_gast_functions_GenericMethod_core_GenericEntity = Generalization(general=core_GenericEntity, specific=gast_functions_GenericMethod)
gen_gast_functions_GenericConstructor_functions_Constructor = Generalization(general=functions_Constructor, specific=gast_functions_GenericConstructor)
gen_gast_functions_GenericConstructor_core_GenericEntity = Generalization(general=core_GenericEntity, specific=gast_functions_GenericConstructor)
gen_gast_functions_Function_core_NamedModelElement = Generalization(general=core_NamedModelElement, specific=gast_functions_Function)
gen_gast_functions_Function_core_SourceEntity = Generalization(general=core_SourceEntity, specific=gast_functions_Function)
gen_gast_variables_FormalParameter_Variable = Generalization(general=Variable, specific=gast_variables_FormalParameter)
gen_gast_variables_Variable_core_NamedModelElement = Generalization(general=core_NamedModelElement, specific=gast_variables_Variable)
gen_gast_variables_Variable_core_SourceEntity = Generalization(general=core_SourceEntity, specific=gast_variables_Variable)
gen_gast_variables_CatchParameter_Variable = Generalization(general=Variable, specific=gast_variables_CatchParameter)
gen_gast_variables_Field_types_Member = Generalization(general=types_Member, specific=gast_variables_Field)
gen_gast_variables_Field_variables_Variable = Generalization(general=variables_Variable, specific=gast_variables_Field)
gen_gast_variables_LocalVariable_Variable = Generalization(general=Variable, specific=gast_variables_LocalVariable)
gen_gast_variables_Property_variables_Field = Generalization(general=variables_Field, specific=gast_variables_Property)
gen_gast_variables_Property_types_Member = Generalization(general=types_Member, specific=gast_variables_Property)
gen_gast_variables_GlobalVariable_Variable = Generalization(general=Variable, specific=gast_variables_GlobalVariable)

# Domain Model
domain_model = DomainModel(
    name="gast",
    types={BaseAccess, CloneInstance, gast_statements_ExceptionHandler, Statement, CatchBlock, BlockStatement, gast_statements_Statement, SourceEntity, Branch, LoopStatement, gast_statements_Branch, GASTExpression, gast_statements_BlockStatement, Function, BranchStatement, gast_statements_GASTExpression, gast_statements_BranchStatement, gast_statements_LoopStatement, gast_statements_CatchBlock, CatchParameter, gast_statements_SimpleStatement, gast_statements_JumpStatement, statements_Statement, statements_FlowInstr, gast_statements_GASTBehaviour, gast_statements_Methods, statements_BlockStatement, Exit, gast_statements_Exit, FlowInstr, gast_statements_FlowInstr, Var, gast_statements_Var, gast_statements_Param, gast_core_BasePath, ModelElement, Root, Directory, gast_core_Identifier, gast_core_NamedModelElement, gast_core_ModelElement, Identifier, ModelAnnotation, gast_core_Package, NamedModelElement, GASTClass, Access, Delegate, GlobalFunction, GlobalVariable, Package, TypeAlias, gast_core_GenericEntity, TypeParameterClass, gast_core_Root, Clone, StructuralAbstraction, BasePath, gast_core_Directory, GASTType, File, gast_core_File, gast_core_PackageAlias, gast_core_Position, gast_core_SourceEntity, Position, gast_annotations_Attribute, types_GASTClass, annotations_ModelAnnotation, gast_annotations_Clone, core_ModelElement, gast_annotations_StructuralAbstraction, core_NamedModelElement, gast_annotations_Comment, core_SourceEntity, gast_annotations_CloneInstance, gast_annotations_Subsystem, gast_annotations_Layer, gast_annotations_ModelAnnotation, gast_types_Reference, TypeDecorator, gast_types_TypeDecorator, gast_types_GASTType, gast_types_GASTArray, gast_types_TypeAlias, types_Member, types_TypeDecorator, gast_types_Member, Member, gast_types_TypeParameterClass, gast_types_GenericClass, core_GenericEntity, gast_types_GASTEnumeration, gast_types_GASTStruct, gast_types_GASTUnion, gast_types_GASTClass, types_GASTType, Constructor, Destructor, Field, Method_, InheritanceTypeAccess, Property_, gast_accesses_ParameterInstantiationTypeAccess, TypeAccess, gast_accesses_TypeAccess, gast_accesses_CastTypeAccess, gast_accesses_BaseAccess, gast_accesses_CompositeAccess, CompositeAccess, gast_accesses_DeclarationTypeAccess, Variable, gast_accesses_ThrowTypeAccess, gast_accesses_FunctionAccess, gast_accesses_DelegateAccess, FunctionAccess, gast_accesses_RunTimeTypeAccess, gast_accesses_SelfAccess, VariableAccess, gast_accesses_StaticTypeAccess, gast_accesses_PropertyAccess, gast_accesses_Access, gast_accesses_InheritanceTypeAccess, gast_accesses_VariableAccess, gast_functions_Delegate, functions_Function, gast_functions_Constructor, gast_functions_GenericFunction, functions_GlobalFunction, gast_functions_GlobalFunction, gast_functions_Method, gast_functions_Destructor, gast_functions_GenericMethod, functions_Method, gast_functions_GenericConstructor, functions_Constructor, gast_functions_Function, DeclarationTypeAccess, FormalParameter, LocalVariable, ThrowTypeAccess, gast_variables_FormalParameter, gast_variables_Variable, gast_variables_CatchParameter, gast_variables_Field, variables_Variable, gast_variables_LocalVariable, gast_variables_Property, variables_Field, gast_variables_GlobalVariable, LoopStatementKind, JumpStatementKind, Status, Visibilities, GlobalFunctionKind},
    associations={accesses6, cloneInstance7, catchBlocks0, finallyBlock1, guardedBlock3, branch11, blockstatement8, surroundingStatement10, conditionExpression25, loopstatement13, cfPre15, cfNext18, statements21, surroundingFunction24, breakConditionExpression34, branchstatement26, statement28, branches31, catchParameter45, initExpression36, incrementExpression39, body42, expression48, expression46, cfnext57, cfPrev59, blockstatement50, exit52, use53, def54, root62, directories63, annotations65, allLocalClasses66, allInnerClasses67, allNormalClasses70, allInterfaces73, allAccesses76, delegates78, globalFunctions80, globalVariables82, root83, classes86, surroundingPackage90, allAccessedPackages93, typeAliases96, typeParameters98, subPackages88, allAccesses99, allInnerClasses101, allInterfaces104, allLocalClasses107, allNormalClasses110, allModelElements113, globalVariables115, packages118, clones121, structuralAbstractions123, danglingModelElements127, basePaths130, globalFunctions132, types125, subDirectory135, parentDirectory138, files141, basePath143, importedTypes148, types151, globalVariables154, globalFunctions157, root146, importedGlobalFunctions160, importedGlobalVariables163, importedPackages166, includedFiles169, directory172, sourceFile175, assembly177, sourceentity180, aliasedPackage182, position184, cloneInstances186, root189, statements192, clone195, referencedType198, decoratedType200, undecoratedType202, baseType205, aliasedType207, surroundingClass209, surroundingPackage212, overriddenMember215, typeBounds216, innerTypeAliases218, innerDelegates221, constructors224, destructors226, fields228, methods230, surroundingFunction232, surroundingPackage235, innerClasses240, surroundingClass243, superTypes238, self248, friendClasses251, gastClass254, friendFunctions257, property260, allAccesses262, inheritanceTypeAccesses246, allAccessedClasses265, targetType268, typeArguments270, accesses273, parentStatement276, surroundingStatement279, surroundingClass281, surroundingFunction284, surroundingCompositeAccess287, function289, surroundingVariable292, accessedFunctions294, accessedDelegate296, typeArguments299, targetFunction301, targetVariable304, accessedTarget308, accessedClass306, invocations313, surroundingClass316, surroundingPackage319, surroundingClass322, superClass311, surroundingClass325, surroundingPackage328, root331, surroundingProperty334, surroundingClass336, returnTypeDeclaration339, formalParameters341, localVariables343, allStatements345, throwTypeAccesses347, accesses349, body352, localClasses355, surroundingFunction358, type361, typeDeclaration363, surroundingClass366, surroundingFunction369, setter372, getter374, surroundingPackage377},
    generalizations={gen_gast_statements_ExceptionHandler_Statement, gen_gast_statements_Statement_SourceEntity, gen_gast_statements_Branch_SourceEntity, gen_gast_statements_BlockStatement_Statement, gen_gast_statements_GASTExpression_SourceEntity, gen_gast_statements_BranchStatement_Statement, gen_gast_statements_LoopStatement_Statement, gen_gast_statements_CatchBlock_BlockStatement, gen_gast_statements_SimpleStatement_statements_Statement, gen_gast_statements_SimpleStatement_statements_FlowInstr, gen_gast_statements_JumpStatement_statements_Statement, gen_gast_statements_JumpStatement_statements_FlowInstr, gen_gast_statements_Methods_statements_BlockStatement, gen_gast_statements_Methods_statements_FlowInstr, gen_gast_statements_Exit_FlowInstr, gen_gast_statements_Param_Var, gen_gast_core_BasePath_ModelElement, gen_gast_core_NamedModelElement_ModelElement, gen_gast_core_ModelElement_Identifier, gen_gast_core_Package_NamedModelElement, gen_gast_core_GenericEntity_ModelElement, gen_gast_core_Root_ModelElement, gen_gast_core_Directory_NamedModelElement, gen_gast_core_File_NamedModelElement, gen_gast_core_PackageAlias_Package, gen_gast_core_SourceEntity_ModelElement, gen_gast_annotations_Attribute_types_GASTClass, gen_gast_annotations_Attribute_annotations_ModelAnnotation, gen_gast_annotations_Clone_core_ModelElement, gen_gast_annotations_Clone_annotations_ModelAnnotation, gen_gast_annotations_CloneInstance_core_ModelElement, gen_gast_annotations_CloneInstance_annotations_ModelAnnotation, gen_gast_annotations_StructuralAbstraction_core_NamedModelElement, gen_gast_annotations_StructuralAbstraction_annotations_ModelAnnotation, gen_gast_annotations_Comment_core_SourceEntity, gen_gast_annotations_Comment_annotations_ModelAnnotation, gen_gast_annotations_Subsystem_StructuralAbstraction, gen_gast_annotations_Layer_StructuralAbstraction, gen_gast_types_Reference_TypeDecorator, gen_gast_types_TypeDecorator_GASTType, gen_gast_types_GASTType_NamedModelElement, gen_gast_types_GASTArray_TypeDecorator, gen_gast_types_TypeAlias_types_Member, gen_gast_types_TypeAlias_types_TypeDecorator, gen_gast_types_Member_SourceEntity, gen_gast_types_TypeParameterClass_GASTClass, gen_gast_types_GenericClass_types_GASTClass, gen_gast_types_GenericClass_core_GenericEntity, gen_gast_types_GASTEnumeration_GASTClass, gen_gast_types_GASTStruct_GASTClass, gen_gast_types_GASTUnion_GASTClass, gen_gast_types_GASTClass_types_Member, gen_gast_types_GASTClass_types_GASTType, gen_gast_accesses_ParameterInstantiationTypeAccess_TypeAccess, gen_gast_accesses_TypeAccess_Access, gen_gast_accesses_CastTypeAccess_TypeAccess, gen_gast_accesses_BaseAccess_SourceEntity, gen_gast_accesses_CompositeAccess_BaseAccess, gen_gast_accesses_DeclarationTypeAccess_TypeAccess, gen_gast_accesses_ThrowTypeAccess_TypeAccess, gen_gast_accesses_FunctionAccess_Access, gen_gast_accesses_DelegateAccess_FunctionAccess, gen_gast_accesses_VariableAccess_Access, gen_gast_accesses_RunTimeTypeAccess_TypeAccess, gen_gast_accesses_SelfAccess_VariableAccess, gen_gast_accesses_StaticTypeAccess_TypeAccess, gen_gast_accesses_PropertyAccess_VariableAccess, gen_gast_accesses_Access_BaseAccess, gen_gast_accesses_InheritanceTypeAccess_TypeAccess, gen_gast_functions_Delegate_functions_Function, gen_gast_functions_Delegate_types_Member, gen_gast_functions_Delegate_types_GASTType, gen_gast_functions_Constructor_functions_Function, gen_gast_functions_Constructor_types_Member, gen_gast_functions_GenericFunction_functions_GlobalFunction, gen_gast_functions_GenericFunction_core_GenericEntity, gen_gast_functions_GlobalFunction_Function, gen_gast_functions_Method_functions_Function, gen_gast_functions_Method_types_Member, gen_gast_functions_Destructor_functions_Function, gen_gast_functions_Destructor_types_Member, gen_gast_functions_GenericMethod_functions_Method, gen_gast_functions_GenericMethod_core_GenericEntity, gen_gast_functions_GenericConstructor_functions_Constructor, gen_gast_functions_GenericConstructor_core_GenericEntity, gen_gast_functions_Function_core_NamedModelElement, gen_gast_functions_Function_core_SourceEntity, gen_gast_variables_FormalParameter_Variable, gen_gast_variables_Variable_core_NamedModelElement, gen_gast_variables_Variable_core_SourceEntity, gen_gast_variables_CatchParameter_Variable, gen_gast_variables_Field_types_Member, gen_gast_variables_Field_variables_Variable, gen_gast_variables_LocalVariable_Variable, gen_gast_variables_Property_variables_Field, gen_gast_variables_Property_types_Member, gen_gast_variables_GlobalVariable_Variable},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)