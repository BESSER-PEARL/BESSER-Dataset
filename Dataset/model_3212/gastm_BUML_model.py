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
            EnumerationLiteral(name="WHILE"),
			EnumerationLiteral(name="DOWHILE"),
			EnumerationLiteral(name="FOR"),
			EnumerationLiteral(name="FOREACH")
    }
)

JumpStatementKind: Enumeration = Enumeration(
    name="JumpStatementKind",
    literals={
            EnumerationLiteral(name="RETURN"),
			EnumerationLiteral(name="THROW"),
			EnumerationLiteral(name="JUMP")
    }
)

Status: Enumeration = Enumeration(
    name="Status",
    literals={
            EnumerationLiteral(name="FAILEDDEP"),
			EnumerationLiteral(name="NORMAL"),
			EnumerationLiteral(name="LIBRARY"),
			EnumerationLiteral(name="IMPLICIT")
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
gast_statements_Statement = Class(name="gast::statements::Statement", is_abstract=True)
SourceEntity = Class(name="SourceEntity")
BaseAccess = Class(name="BaseAccess")
CloneInstance = Class(name="CloneInstance")
gast_statements_ExceptionHandler = Class(name="gast::statements::ExceptionHandler")
Statement = Class(name="Statement")
CatchBlock = Class(name="CatchBlock")
BlockStatement = Class(name="BlockStatement")
Branch = Class(name="Branch")
LoopStatement = Class(name="LoopStatement")
gast_statements_BlockStatement = Class(name="gast::statements::BlockStatement")
gast_statements_Branch = Class(name="gast::statements::Branch")
GASTExpression = Class(name="GASTExpression")
BranchStatement = Class(name="BranchStatement")
gast_statements_GASTExpression = Class(name="gast::statements::GASTExpression", is_abstract=True)
gast_statements_BranchStatement = Class(name="gast::statements::BranchStatement")
Function = Class(name="Function")
gast_statements_LoopStatement = Class(name="gast::statements::LoopStatement")
gast_statements_CatchBlock = Class(name="gast::statements::CatchBlock")
CatchParameter = Class(name="CatchParameter")
gast_statements_JumpStatement = Class(name="gast::statements::JumpStatement")
gast_statements_SimpleStatement = Class(name="gast::statements::SimpleStatement")
gast_statements_GASTBehaviour = Class(name="gast::statements::GASTBehaviour")
gast_core_BasePath = Class(name="gast::core::BasePath")
ModelElement = Class(name="ModelElement")
Root = Class(name="Root")
ModelAnnotation = Class(name="ModelAnnotation")
gast_core_Identifier = Class(name="gast::core::Identifier", is_abstract=True)
gast_core_NamedModelElement = Class(name="gast::core::NamedModelElement", is_abstract=True)
Directory = Class(name="Directory")
gast_core_ModelElement = Class(name="gast::core::ModelElement", is_abstract=True)
Identifier = Class(name="Identifier")
GASTClass = Class(name="GASTClass")
Package = Class(name="Package")
gast_core_Package = Class(name="gast::core::Package")
NamedModelElement = Class(name="NamedModelElement")
Access = Class(name="Access")
Delegate = Class(name="Delegate")
GlobalFunction = Class(name="GlobalFunction")
GlobalVariable = Class(name="GlobalVariable")
gast_core_Root = Class(name="gast::core::Root")
TypeAlias = Class(name="TypeAlias")
gast_core_GenericEntity = Class(name="gast::core::GenericEntity", is_abstract=True)
TypeParameterClass = Class(name="TypeParameterClass")
StructuralAbstraction = Class(name="StructuralAbstraction")
GASTType = Class(name="GASTType")
BasePath = Class(name="BasePath")
Clone = Class(name="Clone")
gast_core_Directory = Class(name="gast::core::Directory")
File = Class(name="File")
gast_core_File = Class(name="gast::core::File")
gast_core_Position = Class(name="gast::core::Position")
gast_annotations_Attribute = Class(name="gast::annotations::Attribute")
types_GASTClass = Class(name="types::GASTClass")
annotations_ModelAnnotation = Class(name="annotations::ModelAnnotation")
gast_annotations_Clone = Class(name="gast::annotations::Clone")
core_ModelElement = Class(name="core::ModelElement")
gast_annotations_CloneInstance = Class(name="gast::annotations::CloneInstance")
gast_core_PackageAlias = Class(name="gast::core::PackageAlias")
gast_core_SourceEntity = Class(name="gast::core::SourceEntity", is_abstract=True)
Position = Class(name="Position")
gast_annotations_Comment = Class(name="gast::annotations::Comment")
core_SourceEntity = Class(name="core::SourceEntity")
gast_annotations_StructuralAbstraction = Class(name="gast::annotations::StructuralAbstraction", is_abstract=True)
core_NamedModelElement = Class(name="core::NamedModelElement")
gast_annotations_ModelAnnotation = Class(name="gast::annotations::ModelAnnotation", is_abstract=True)
gast_types_Reference = Class(name="gast::types::Reference")
TypeDecorator = Class(name="TypeDecorator")
gast_annotations_Subsystem = Class(name="gast::annotations::Subsystem")
gast_annotations_Layer = Class(name="gast::annotations::Layer")
gast_types_GASTType = Class(name="gast::types::GASTType", is_abstract=True)
gast_types_GASTArray = Class(name="gast::types::GASTArray")
gast_types_TypeDecorator = Class(name="gast::types::TypeDecorator", is_abstract=True)
gast_types_Member = Class(name="gast::types::Member", is_abstract=True)
Member = Class(name="Member")
gast_types_TypeAlias = Class(name="gast::types::TypeAlias")
types_Member = Class(name="types::Member")
types_TypeDecorator = Class(name="types::TypeDecorator")
gast_types_TypeParameterClass = Class(name="gast::types::TypeParameterClass")
Constructor = Class(name="Constructor")
Destructor = Class(name="Destructor")
Field = Class(name="Field")
Method_ = Class(name="Method")
gast_types_GenericClass = Class(name="gast::types::GenericClass")
core_GenericEntity = Class(name="core::GenericEntity")
gast_types_GASTEnumeration = Class(name="gast::types::GASTEnumeration")
gast_types_GASTStruct = Class(name="gast::types::GASTStruct")
gast_types_GASTUnion = Class(name="gast::types::GASTUnion")
gast_types_GASTClass = Class(name="gast::types::GASTClass")
types_GASTType = Class(name="types::GASTType")
InheritanceTypeAccess = Class(name="InheritanceTypeAccess")
gast_accesses_ParameterInstantiationTypeAccess = Class(name="gast::accesses::ParameterInstantiationTypeAccess")
TypeAccess = Class(name="TypeAccess")
gast_accesses_TypeAccess = Class(name="gast::accesses::TypeAccess", is_abstract=True)
gast_accesses_CastTypeAccess = Class(name="gast::accesses::CastTypeAccess")
gast_accesses_CompositeAccess = Class(name="gast::accesses::CompositeAccess")
Property_ = Class(name="Property")
gast_accesses_BaseAccess = Class(name="gast::accesses::BaseAccess", is_abstract=True)
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
gast_functions_Constructor = Class(name="gast::functions::Constructor")
gast_functions_Destructor = Class(name="gast::functions::Destructor")
gast_functions_GenericFunction = Class(name="gast::functions::GenericFunction")
functions_GlobalFunction = Class(name="functions::GlobalFunction")
gast_functions_Delegate = Class(name="gast::functions::Delegate")
functions_Function = Class(name="functions::Function")
gast_functions_Method = Class(name="gast::functions::Method")
gast_functions_GlobalFunction = Class(name="gast::functions::GlobalFunction")
DeclarationTypeAccess = Class(name="DeclarationTypeAccess")
FormalParameter = Class(name="FormalParameter")
LocalVariable = Class(name="LocalVariable")
ThrowTypeAccess = Class(name="ThrowTypeAccess")
gast_functions_GenericMethod = Class(name="gast::functions::GenericMethod")
functions_Method = Class(name="functions::Method")
gast_functions_GenericConstructor = Class(name="gast::functions::GenericConstructor")
functions_Constructor = Class(name="functions::Constructor")
gast_functions_Function = Class(name="gast::functions::Function", is_abstract=True)
gast_variables_FormalParameter = Class(name="gast::variables::FormalParameter")
gast_variables_Variable = Class(name="gast::variables::Variable", is_abstract=True)
gast_variables_CatchParameter = Class(name="gast::variables::CatchParameter")
gast_variables_GlobalVariable = Class(name="gast::variables::GlobalVariable")
gast_variables_Field = Class(name="gast::variables::Field")
variables_Variable = Class(name="variables::Variable")
gast_variables_LocalVariable = Class(name="gast::variables::LocalVariable")
gast_variables_Property = Class(name="gast::variables::Property")
variables_Field = Class(name="variables::Field")

# gast_statements_Statement class attributes and methods
gast_statements_Statement_numberOfStatements: Property = Property(name="numberOfStatements", type=IntegerType)
gast_statements_Statement_maximumNestingLevel: Property = Property(name="maximumNestingLevel", type=IntegerType)
gast_statements_Statement_numberOfEdgesInCFG: Property = Property(name="numberOfEdgesInCFG", type=IntegerType)
gast_statements_Statement_numberOfNodesInCFG: Property = Property(name="numberOfNodesInCFG", type=IntegerType)
gast_statements_Statement_numberOfComments: Property = Property(name="numberOfComments", type=IntegerType)
gast_statements_Statement_linesOfCode: Property = Property(name="linesOfCode", type=IntegerType)
gast_statements_Statement.attributes={gast_statements_Statement_maximumNestingLevel, gast_statements_Statement_numberOfComments, gast_statements_Statement_numberOfNodesInCFG, gast_statements_Statement_numberOfEdgesInCFG, gast_statements_Statement_linesOfCode, gast_statements_Statement_numberOfStatements}

# SourceEntity class attributes and methods

# BaseAccess class attributes and methods

# CloneInstance class attributes and methods

# gast_statements_ExceptionHandler class attributes and methods

# Statement class attributes and methods

# CatchBlock class attributes and methods

# BlockStatement class attributes and methods

# Branch class attributes and methods

# LoopStatement class attributes and methods

# gast_statements_BlockStatement class attributes and methods
gast_statements_BlockStatement_synchronized: Property = Property(name="synchronized", type=BooleanType)
gast_statements_BlockStatement.attributes={gast_statements_BlockStatement_synchronized}

# gast_statements_Branch class attributes and methods

# GASTExpression class attributes and methods

# BranchStatement class attributes and methods

# gast_statements_GASTExpression class attributes and methods

# gast_statements_BranchStatement class attributes and methods

# Function class attributes and methods

# gast_statements_LoopStatement class attributes and methods
gast_statements_LoopStatement_kind: Property = Property(name="kind", type=StringType)
gast_statements_LoopStatement.attributes={gast_statements_LoopStatement_kind}

# gast_statements_CatchBlock class attributes and methods

# CatchParameter class attributes and methods

# gast_statements_JumpStatement class attributes and methods
gast_statements_JumpStatement_kind: Property = Property(name="kind", type=StringType)
gast_statements_JumpStatement.attributes={gast_statements_JumpStatement_kind}

# gast_statements_SimpleStatement class attributes and methods

# gast_statements_GASTBehaviour class attributes and methods

# gast_core_BasePath class attributes and methods
gast_core_BasePath_path: Property = Property(name="path", type=StringType)
gast_core_BasePath.attributes={gast_core_BasePath_path}

# ModelElement class attributes and methods

# Root class attributes and methods

# ModelAnnotation class attributes and methods

# gast_core_Identifier class attributes and methods
gast_core_Identifier_id: Property = Property(name="id", type=StringType)
gast_core_Identifier_m_idHasToBeUnique: Method = Method(name="idHasToBeUnique", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
gast_core_Identifier.attributes={gast_core_Identifier_id}
gast_core_Identifier.methods={gast_core_Identifier_m_idHasToBeUnique}

# gast_core_NamedModelElement class attributes and methods
gast_core_NamedModelElement_simpleName: Property = Property(name="simpleName", type=StringType)
gast_core_NamedModelElement.attributes={gast_core_NamedModelElement_simpleName}

# Directory class attributes and methods

# gast_core_ModelElement class attributes and methods
gast_core_ModelElement_status: Property = Property(name="status", type=StringType)
gast_core_ModelElement_sissyId: Property = Property(name="sissyId", type=IntegerType)
gast_core_ModelElement.attributes={gast_core_ModelElement_sissyId, gast_core_ModelElement_status}

# Identifier class attributes and methods

# GASTClass class attributes and methods

# Package class attributes and methods

# gast_core_Package class attributes and methods
gast_core_Package_linesOfComments: Property = Property(name="linesOfComments", type=IntegerType)
gast_core_Package_linesOfCode: Property = Property(name="linesOfCode", type=IntegerType)
gast_core_Package_qualifiedName: Property = Property(name="qualifiedName", type=StringType)
gast_core_Package.attributes={gast_core_Package_qualifiedName, gast_core_Package_linesOfCode, gast_core_Package_linesOfComments}

# NamedModelElement class attributes and methods

# Access class attributes and methods

# Delegate class attributes and methods

# GlobalFunction class attributes and methods

# GlobalVariable class attributes and methods

# gast_core_Root class attributes and methods
gast_core_Root_linesOfComments: Property = Property(name="linesOfComments", type=IntegerType)
gast_core_Root_linesOfCode: Property = Property(name="linesOfCode", type=IntegerType)
gast_core_Root_m_getPackageByName: Method = Method(name="getPackageByName", parameters={Parameter(name='name')}, type=StringType)
gast_core_Root_m_getPackageByQualifiedName: Method = Method(name="getPackageByQualifiedName", parameters={Parameter(name='qualifiedName')}, type=StringType)
gast_core_Root.attributes={gast_core_Root_linesOfCode, gast_core_Root_linesOfComments}
gast_core_Root.methods={gast_core_Root_m_getPackageByQualifiedName, gast_core_Root_m_getPackageByName}

# TypeAlias class attributes and methods

# gast_core_GenericEntity class attributes and methods

# TypeParameterClass class attributes and methods

# StructuralAbstraction class attributes and methods

# GASTType class attributes and methods

# BasePath class attributes and methods

# Clone class attributes and methods

# gast_core_Directory class attributes and methods
gast_core_Directory_fullQualifiedPath: Property = Property(name="fullQualifiedPath", type=StringType)
gast_core_Directory_fileSystemPath: Property = Property(name="fileSystemPath", type=StringType)
gast_core_Directory.attributes={gast_core_Directory_fileSystemPath, gast_core_Directory_fullQualifiedPath}

# File class attributes and methods

# gast_core_File class attributes and methods
gast_core_File_assemblyFile: Property = Property(name="assemblyFile", type=BooleanType)
gast_core_File_fileSystemPath: Property = Property(name="fileSystemPath", type=StringType)
gast_core_File_sourceFile: Property = Property(name="sourceFile", type=BooleanType)
gast_core_File_linesOfCode: Property = Property(name="linesOfCode", type=IntegerType)
gast_core_File_size: Property = Property(name="size", type=StringType)
gast_core_File_fullQualifiedPath: Property = Property(name="fullQualifiedPath", type=StringType)
gast_core_File.attributes={gast_core_File_fullQualifiedPath, gast_core_File_linesOfCode, gast_core_File_sourceFile, gast_core_File_size, gast_core_File_fileSystemPath, gast_core_File_assemblyFile}

# gast_core_Position class attributes and methods
gast_core_Position_endColumn: Property = Property(name="endColumn", type=IntegerType)
gast_core_Position_startColumn: Property = Property(name="startColumn", type=IntegerType)
gast_core_Position_endLine: Property = Property(name="endLine", type=IntegerType)
gast_core_Position_startLine: Property = Property(name="startLine", type=IntegerType)
gast_core_Position_m_EitherAssemblyFileOrSourceFileSet: Method = Method(name="EitherAssemblyFileOrSourceFileSet", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
gast_core_Position.attributes={gast_core_Position_endColumn, gast_core_Position_startLine, gast_core_Position_endLine, gast_core_Position_startColumn}
gast_core_Position.methods={gast_core_Position_m_EitherAssemblyFileOrSourceFileSet}

# gast_annotations_Attribute class attributes and methods

# types_GASTClass class attributes and methods

# annotations_ModelAnnotation class attributes and methods

# gast_annotations_Clone class attributes and methods

# core_ModelElement class attributes and methods

# gast_annotations_CloneInstance class attributes and methods

# gast_core_PackageAlias class attributes and methods

# gast_core_SourceEntity class attributes and methods

# Position class attributes and methods

# gast_annotations_Comment class attributes and methods
gast_annotations_Comment_todo: Property = Property(name="todo", type=BooleanType)
gast_annotations_Comment_formal: Property = Property(name="formal", type=BooleanType)
gast_annotations_Comment_todoCount: Property = Property(name="todoCount", type=IntegerType)
gast_annotations_Comment_texts: Property = Property(name="texts", type=StringType)
gast_annotations_Comment_m_OCLtodo: Method = Method(name="OCLtodo", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
gast_annotations_Comment.attributes={gast_annotations_Comment_todo, gast_annotations_Comment_todoCount, gast_annotations_Comment_formal, gast_annotations_Comment_texts}
gast_annotations_Comment.methods={gast_annotations_Comment_m_OCLtodo}

# core_SourceEntity class attributes and methods

# gast_annotations_StructuralAbstraction class attributes and methods

# core_NamedModelElement class attributes and methods

# gast_annotations_ModelAnnotation class attributes and methods

# gast_types_Reference class attributes and methods
gast_types_Reference_explicit: Property = Property(name="explicit", type=BooleanType)
gast_types_Reference.attributes={gast_types_Reference_explicit}

# TypeDecorator class attributes and methods

# gast_annotations_Subsystem class attributes and methods

# gast_annotations_Layer class attributes and methods

# gast_types_GASTType class attributes and methods
gast_types_GASTType_qualifiedName: Property = Property(name="qualifiedName", type=StringType)
gast_types_GASTType_referenceType: Property = Property(name="referenceType", type=BooleanType)
gast_types_GASTType.attributes={gast_types_GASTType_qualifiedName, gast_types_GASTType_referenceType}

# gast_types_GASTArray class attributes and methods
gast_types_GASTArray_dimensions: Property = Property(name="dimensions", type=IntegerType)
gast_types_GASTArray.attributes={gast_types_GASTArray_dimensions}

# gast_types_TypeDecorator class attributes and methods

# gast_types_Member class attributes and methods
gast_types_Member_visibility: Property = Property(name="visibility", type=StringType)
gast_types_Member_abstract: Property = Property(name="abstract", type=BooleanType)
gast_types_Member_virtual: Property = Property(name="virtual", type=BooleanType)
gast_types_Member_extern: Property = Property(name="extern", type=BooleanType)
gast_types_Member_final: Property = Property(name="final", type=BooleanType)
gast_types_Member_internal: Property = Property(name="internal", type=BooleanType)
gast_types_Member_introspectable: Property = Property(name="introspectable", type=BooleanType)
gast_types_Member_override: Property = Property(name="override", type=BooleanType)
gast_types_Member_static: Property = Property(name="static", type=BooleanType)
gast_types_Member_typeParameterClassMember: Property = Property(name="typeParameterClassMember", type=BooleanType)
gast_types_Member_m_getSurroundingClass: Method = Method(name="getSurroundingClass", parameters={}, type=StringType)
gast_types_Member.attributes={gast_types_Member_static, gast_types_Member_extern, gast_types_Member_visibility, gast_types_Member_final, gast_types_Member_abstract, gast_types_Member_internal, gast_types_Member_introspectable, gast_types_Member_typeParameterClassMember, gast_types_Member_virtual, gast_types_Member_override}
gast_types_Member.methods={gast_types_Member_m_getSurroundingClass}

# Member class attributes and methods

# gast_types_TypeAlias class attributes and methods
gast_types_TypeAlias_innerTypeAlias: Property = Property(name="innerTypeAlias", type=BooleanType)
gast_types_TypeAlias.attributes={gast_types_TypeAlias_innerTypeAlias}

# types_Member class attributes and methods

# types_TypeDecorator class attributes and methods

# gast_types_TypeParameterClass class attributes and methods

# Constructor class attributes and methods

# Destructor class attributes and methods

# Field class attributes and methods

# Method class attributes and methods

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
gast_types_GASTClass.attributes={gast_types_GASTClass_anonymous, gast_types_GASTClass_inner, gast_types_GASTClass_interface, gast_types_GASTClass_linesOfComments, gast_types_GASTClass_local, gast_types_GASTClass_primitive}

# types_GASTType class attributes and methods

# InheritanceTypeAccess class attributes and methods

# gast_accesses_ParameterInstantiationTypeAccess class attributes and methods

# TypeAccess class attributes and methods

# gast_accesses_TypeAccess class attributes and methods

# gast_accesses_CastTypeAccess class attributes and methods

# gast_accesses_CompositeAccess class attributes and methods

# Property class attributes and methods

# gast_accesses_BaseAccess class attributes and methods

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

# gast_functions_Constructor class attributes and methods
gast_functions_Constructor_initializer: Property = Property(name="initializer", type=BooleanType)
gast_functions_Constructor.attributes={gast_functions_Constructor_initializer}

# gast_functions_Destructor class attributes and methods

# gast_functions_GenericFunction class attributes and methods

# functions_GlobalFunction class attributes and methods

# gast_functions_Delegate class attributes and methods
gast_functions_Delegate_innerDelegate: Property = Property(name="innerDelegate", type=BooleanType)
gast_functions_Delegate.attributes={gast_functions_Delegate_innerDelegate}

# functions_Function class attributes and methods

# gast_functions_Method class attributes and methods
gast_functions_Method_propertyMethod: Property = Property(name="propertyMethod", type=BooleanType)
gast_functions_Method.attributes={gast_functions_Method_propertyMethod}

# gast_functions_GlobalFunction class attributes and methods
gast_functions_GlobalFunction_kind: Property = Property(name="kind", type=StringType)
gast_functions_GlobalFunction.attributes={gast_functions_GlobalFunction_kind}

# DeclarationTypeAccess class attributes and methods

# FormalParameter class attributes and methods

# LocalVariable class attributes and methods

# ThrowTypeAccess class attributes and methods

# gast_functions_GenericMethod class attributes and methods

# functions_Method class attributes and methods

# gast_functions_GenericConstructor class attributes and methods

# functions_Constructor class attributes and methods

# gast_functions_Function class attributes and methods
gast_functions_Function_numberOfStatements: Property = Property(name="numberOfStatements", type=IntegerType)
gast_functions_Function_maximumNestingLevel: Property = Property(name="maximumNestingLevel", type=IntegerType)
gast_functions_Function_linesOfComments: Property = Property(name="linesOfComments", type=IntegerType)
gast_functions_Function_linesOfCode: Property = Property(name="linesOfCode", type=IntegerType)
gast_functions_Function_numberOfEdgesInCFG: Property = Property(name="numberOfEdgesInCFG", type=IntegerType)
gast_functions_Function_numberOfNodesInCFG: Property = Property(name="numberOfNodesInCFG", type=IntegerType)
gast_functions_Function_operator: Property = Property(name="operator", type=BooleanType)
gast_functions_Function.attributes={gast_functions_Function_numberOfNodesInCFG, gast_functions_Function_maximumNestingLevel, gast_functions_Function_linesOfComments, gast_functions_Function_numberOfStatements, gast_functions_Function_numberOfEdgesInCFG, gast_functions_Function_operator, gast_functions_Function_linesOfCode}

# gast_variables_FormalParameter class attributes and methods
gast_variables_FormalParameter_passedByReference: Property = Property(name="passedByReference", type=BooleanType)
gast_variables_FormalParameter.attributes={gast_variables_FormalParameter_passedByReference}

# gast_variables_Variable class attributes and methods
gast_variables_Variable_const: Property = Property(name="const", type=BooleanType)
gast_variables_Variable.attributes={gast_variables_Variable_const}

# gast_variables_CatchParameter class attributes and methods
gast_variables_CatchParameter_rethrown: Property = Property(name="rethrown", type=BooleanType)
gast_variables_CatchParameter.attributes={gast_variables_CatchParameter_rethrown}

# gast_variables_GlobalVariable class attributes and methods

# gast_variables_Field class attributes and methods
gast_variables_Field_propertyField: Property = Property(name="propertyField", type=BooleanType)
gast_variables_Field.attributes={gast_variables_Field_propertyField}

# variables_Variable class attributes and methods

# gast_variables_LocalVariable class attributes and methods

# gast_variables_Property class attributes and methods

# variables_Field class attributes and methods

# Relationships
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
catchBlocks0: BinaryAssociation = BinaryAssociation(
    name="catchBlocks0",
    ends={
        Property(name="CatchBlock", type=gast_statements_ExceptionHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_statements_ExceptionHandler", type=CatchBlock, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
branch11: BinaryAssociation = BinaryAssociation(
    name="branch11",
    ends={
        Property(name="statements12", type=gast_statements_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="Branch", type=Branch, multiplicity=Multiplicity(0, 1))
    }
)
loopstatement13: BinaryAssociation = BinaryAssociation(
    name="loopstatement13",
    ends={
        Property(name="statements14", type=gast_statements_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="LoopStatement", type=LoopStatement, multiplicity=Multiplicity(0, 1))
    }
)
statements15: BinaryAssociation = BinaryAssociation(
    name="statements15",
    ends={
        Property(name="statements17", type=gast_statements_BlockStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="Statement16", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
conditionExpression19: BinaryAssociation = BinaryAssociation(
    name="conditionExpression19",
    ends={
        Property(name="GASTExpression", type=gast_statements_Branch, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_statements_Branch", type=GASTExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
branchstatement20: BinaryAssociation = BinaryAssociation(
    name="branchstatement20",
    ends={
        Property(name="statements21", type=gast_statements_Branch, multiplicity=Multiplicity(1, 1)),
        Property(name="BranchStatement", type=BranchStatement, multiplicity=Multiplicity(1, 1))
    }
)
statement22: BinaryAssociation = BinaryAssociation(
    name="statement22",
    ends={
        Property(name="statements24", type=gast_statements_Branch, multiplicity=Multiplicity(1, 1)),
        Property(name="Statement23", type=Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
surroundingFunction18: BinaryAssociation = BinaryAssociation(
    name="surroundingFunction18",
    ends={
        Property(name="functions", type=gast_statements_BlockStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="Function", type=Function, multiplicity=Multiplicity(0, 1))
    }
)
breakConditionExpression28: BinaryAssociation = BinaryAssociation(
    name="breakConditionExpression28",
    ends={
        Property(name="GASTExpression29", type=gast_statements_LoopStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_statements_LoopStatement", type=GASTExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initExpression30: BinaryAssociation = BinaryAssociation(
    name="initExpression30",
    ends={
        Property(name="GASTExpression32", type=gast_statements_LoopStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_statements_LoopStatement31", type=GASTExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
incrementExpression33: BinaryAssociation = BinaryAssociation(
    name="incrementExpression33",
    ends={
        Property(name="GASTExpression35", type=gast_statements_LoopStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_statements_LoopStatement34", type=GASTExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body36: BinaryAssociation = BinaryAssociation(
    name="body36",
    ends={
        Property(name="statements38", type=gast_statements_LoopStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="Statement37", type=Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
branches25: BinaryAssociation = BinaryAssociation(
    name="branches25",
    ends={
        Property(name="statements27", type=gast_statements_BranchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="Branch26", type=Branch, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
catchParameter39: BinaryAssociation = BinaryAssociation(
    name="catchParameter39",
    ends={
        Property(name="CatchParameter", type=gast_statements_CatchBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_statements_CatchBlock", type=CatchParameter, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression40: BinaryAssociation = BinaryAssociation(
    name="expression40",
    ends={
        Property(name="GASTExpression41", type=gast_statements_JumpStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_statements_JumpStatement", type=GASTExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression42: BinaryAssociation = BinaryAssociation(
    name="expression42",
    ends={
        Property(name="GASTExpression43", type=gast_statements_SimpleStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_statements_SimpleStatement", type=GASTExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
blockstatement44: BinaryAssociation = BinaryAssociation(
    name="blockstatement44",
    ends={
        Property(name="BlockStatement45", type=gast_statements_GASTBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_statements_GASTBehaviour", type=BlockStatement, multiplicity=Multiplicity(1, 1))
    }
)
root46: BinaryAssociation = BinaryAssociation(
    name="root46",
    ends={
        Property(name="core", type=gast_core_BasePath, multiplicity=Multiplicity(1, 1)),
        Property(name="Root", type=Root, multiplicity=Multiplicity(1, 1))
    }
)
annotations49: BinaryAssociation = BinaryAssociation(
    name="annotations49",
    ends={
        Property(name="ModelAnnotation", type=gast_core_ModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_ModelElement", type=ModelAnnotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
directories47: BinaryAssociation = BinaryAssociation(
    name="directories47",
    ends={
        Property(name="core48", type=gast_core_BasePath, multiplicity=Multiplicity(1, 1)),
        Property(name="Directory", type=Directory, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
allLocalClasses50: BinaryAssociation = BinaryAssociation(
    name="allLocalClasses50",
    ends={
        Property(name="GASTClass", type=gast_core_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_Package", type=GASTClass, multiplicity=Multiplicity(0, 9999))
    }
)
allInnerClasses51: BinaryAssociation = BinaryAssociation(
    name="allInnerClasses51",
    ends={
        Property(name="GASTClass53", type=gast_core_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_Package52", type=GASTClass, multiplicity=Multiplicity(0, 9999))
    }
)
allNormalClasses54: BinaryAssociation = BinaryAssociation(
    name="allNormalClasses54",
    ends={
        Property(name="GASTClass56", type=gast_core_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_Package55", type=GASTClass, multiplicity=Multiplicity(0, 9999))
    }
)
allInterfaces57: BinaryAssociation = BinaryAssociation(
    name="allInterfaces57",
    ends={
        Property(name="GASTClass59", type=gast_core_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_Package58", type=GASTClass, multiplicity=Multiplicity(0, 9999))
    }
)
classes70: BinaryAssociation = BinaryAssociation(
    name="classes70",
    ends={
        Property(name="types", type=gast_core_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="GASTClass71", type=GASTClass, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subPackages72: BinaryAssociation = BinaryAssociation(
    name="subPackages72",
    ends={
        Property(name="core73", type=gast_core_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="Package", type=Package, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
surroundingPackage74: BinaryAssociation = BinaryAssociation(
    name="surroundingPackage74",
    ends={
        Property(name="core76", type=gast_core_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="Package75", type=Package, multiplicity=Multiplicity(0, 1))
    }
)
allAccesses60: BinaryAssociation = BinaryAssociation(
    name="allAccesses60",
    ends={
        Property(name="Access", type=gast_core_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_Package61", type=Access, multiplicity=Multiplicity(0, 9999))
    }
)
allAccessedPackages77: BinaryAssociation = BinaryAssociation(
    name="allAccessedPackages77",
    ends={
        Property(name="Package79", type=gast_core_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_Package78", type=Package, multiplicity=Multiplicity(0, 9999))
    }
)
delegates62: BinaryAssociation = BinaryAssociation(
    name="delegates62",
    ends={
        Property(name="functions63", type=gast_core_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="Delegate", type=Delegate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
globalFunctions64: BinaryAssociation = BinaryAssociation(
    name="globalFunctions64",
    ends={
        Property(name="functions65", type=gast_core_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="GlobalFunction", type=GlobalFunction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
globalVariables66: BinaryAssociation = BinaryAssociation(
    name="globalVariables66",
    ends={
        Property(name="variables", type=gast_core_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="GlobalVariable", type=GlobalVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
root67: BinaryAssociation = BinaryAssociation(
    name="root67",
    ends={
        Property(name="core69", type=gast_core_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="Root68", type=Root, multiplicity=Multiplicity(0, 1))
    }
)
typeAliases80: BinaryAssociation = BinaryAssociation(
    name="typeAliases80",
    ends={
        Property(name="types81", type=gast_core_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="TypeAlias", type=TypeAlias, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeParameters82: BinaryAssociation = BinaryAssociation(
    name="typeParameters82",
    ends={
        Property(name="TypeParameterClass", type=gast_core_GenericEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_GenericEntity", type=TypeParameterClass, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
allLocalClasses91: BinaryAssociation = BinaryAssociation(
    name="allLocalClasses91",
    ends={
        Property(name="GASTClass93", type=gast_core_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_Root92", type=GASTClass, multiplicity=Multiplicity(0, 9999))
    }
)
allNormalClasses94: BinaryAssociation = BinaryAssociation(
    name="allNormalClasses94",
    ends={
        Property(name="GASTClass96", type=gast_core_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_Root95", type=GASTClass, multiplicity=Multiplicity(0, 9999))
    }
)
allModelElements97: BinaryAssociation = BinaryAssociation(
    name="allModelElements97",
    ends={
        Property(name="ModelElement", type=gast_core_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_Root98", type=ModelElement, multiplicity=Multiplicity(0, 9999))
    }
)
allAccesses83: BinaryAssociation = BinaryAssociation(
    name="allAccesses83",
    ends={
        Property(name="Access84", type=gast_core_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_Root", type=Access, multiplicity=Multiplicity(0, 9999))
    }
)
allInnerClasses85: BinaryAssociation = BinaryAssociation(
    name="allInnerClasses85",
    ends={
        Property(name="GASTClass87", type=gast_core_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_Root86", type=GASTClass, multiplicity=Multiplicity(0, 9999))
    }
)
allInterfaces88: BinaryAssociation = BinaryAssociation(
    name="allInterfaces88",
    ends={
        Property(name="GASTClass90", type=gast_core_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_Root89", type=GASTClass, multiplicity=Multiplicity(0, 9999))
    }
)
structuralAbstractions107: BinaryAssociation = BinaryAssociation(
    name="structuralAbstractions107",
    ends={
        Property(name="StructuralAbstraction", type=gast_core_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_Root108", type=StructuralAbstraction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
types109: BinaryAssociation = BinaryAssociation(
    name="types109",
    ends={
        Property(name="GASTType", type=gast_core_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_Root110", type=GASTType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
danglingModelElements111: BinaryAssociation = BinaryAssociation(
    name="danglingModelElements111",
    ends={
        Property(name="ModelElement113", type=gast_core_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_Root112", type=ModelElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
basePaths114: BinaryAssociation = BinaryAssociation(
    name="basePaths114",
    ends={
        Property(name="core115", type=gast_core_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="BasePath", type=BasePath, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
globalFunctions116: BinaryAssociation = BinaryAssociation(
    name="globalFunctions116",
    ends={
        Property(name="functions118", type=gast_core_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="GlobalFunction117", type=GlobalFunction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
globalVariables99: BinaryAssociation = BinaryAssociation(
    name="globalVariables99",
    ends={
        Property(name="GlobalVariable101", type=gast_core_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_Root100", type=GlobalVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
packages102: BinaryAssociation = BinaryAssociation(
    name="packages102",
    ends={
        Property(name="core104", type=gast_core_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="Package103", type=Package, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
clones105: BinaryAssociation = BinaryAssociation(
    name="clones105",
    ends={
        Property(name="annotations106", type=gast_core_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="Clone", type=Clone, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subDirectory119: BinaryAssociation = BinaryAssociation(
    name="subDirectory119",
    ends={
        Property(name="core121", type=gast_core_Directory, multiplicity=Multiplicity(1, 1)),
        Property(name="Directory120", type=Directory, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
files125: BinaryAssociation = BinaryAssociation(
    name="files125",
    ends={
        Property(name="core126", type=gast_core_Directory, multiplicity=Multiplicity(1, 1)),
        Property(name="File", type=File, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
basePath127: BinaryAssociation = BinaryAssociation(
    name="basePath127",
    ends={
        Property(name="core129", type=gast_core_Directory, multiplicity=Multiplicity(1, 1)),
        Property(name="BasePath128", type=BasePath, multiplicity=Multiplicity(0, 1))
    }
)
parentDirectory122: BinaryAssociation = BinaryAssociation(
    name="parentDirectory122",
    ends={
        Property(name="core124", type=gast_core_Directory, multiplicity=Multiplicity(1, 1)),
        Property(name="Directory123", type=Directory, multiplicity=Multiplicity(0, 1))
    }
)
importedTypes132: BinaryAssociation = BinaryAssociation(
    name="importedTypes132",
    ends={
        Property(name="GASTType134", type=gast_core_File, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_File133", type=GASTType, multiplicity=Multiplicity(0, 9999))
    }
)
types135: BinaryAssociation = BinaryAssociation(
    name="types135",
    ends={
        Property(name="GASTType137", type=gast_core_File, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_File136", type=GASTType, multiplicity=Multiplicity(0, 9999))
    }
)
globalVariables138: BinaryAssociation = BinaryAssociation(
    name="globalVariables138",
    ends={
        Property(name="GlobalVariable140", type=gast_core_File, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_File139", type=GlobalVariable, multiplicity=Multiplicity(0, 9999))
    }
)
globalFunctions141: BinaryAssociation = BinaryAssociation(
    name="globalFunctions141",
    ends={
        Property(name="GlobalFunction143", type=gast_core_File, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_File142", type=GlobalFunction, multiplicity=Multiplicity(0, 9999))
    }
)
includedFiles153: BinaryAssociation = BinaryAssociation(
    name="includedFiles153",
    ends={
        Property(name="gast_core_File154", type=File, multiplicity=Multiplicity(0, 9999)),
        Property(name="File155", type=gast_core_File, multiplicity=Multiplicity(1, 1))
    }
)
root130: BinaryAssociation = BinaryAssociation(
    name="root130",
    ends={
        Property(name="Root131", type=gast_core_File, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_File", type=Root, multiplicity=Multiplicity(1, 1))
    }
)
directory156: BinaryAssociation = BinaryAssociation(
    name="directory156",
    ends={
        Property(name="core158", type=gast_core_File, multiplicity=Multiplicity(1, 1)),
        Property(name="Directory157", type=Directory, multiplicity=Multiplicity(1, 1))
    }
)
importedGlobalFunctions144: BinaryAssociation = BinaryAssociation(
    name="importedGlobalFunctions144",
    ends={
        Property(name="GlobalFunction146", type=gast_core_File, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_File145", type=GlobalFunction, multiplicity=Multiplicity(0, 9999))
    }
)
importedGlobalVariables147: BinaryAssociation = BinaryAssociation(
    name="importedGlobalVariables147",
    ends={
        Property(name="GlobalVariable149", type=gast_core_File, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_File148", type=GlobalVariable, multiplicity=Multiplicity(0, 9999))
    }
)
importedPackages150: BinaryAssociation = BinaryAssociation(
    name="importedPackages150",
    ends={
        Property(name="Package152", type=gast_core_File, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_File151", type=Package, multiplicity=Multiplicity(0, 9999))
    }
)
cloneInstances170: BinaryAssociation = BinaryAssociation(
    name="cloneInstances170",
    ends={
        Property(name="annotations172", type=gast_annotations_Clone, multiplicity=Multiplicity(1, 1)),
        Property(name="CloneInstance171", type=CloneInstance, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
root173: BinaryAssociation = BinaryAssociation(
    name="root173",
    ends={
        Property(name="core175", type=gast_annotations_Clone, multiplicity=Multiplicity(1, 1)),
        Property(name="Root174", type=Root, multiplicity=Multiplicity(1, 1))
    }
)
sourceFile159: BinaryAssociation = BinaryAssociation(
    name="sourceFile159",
    ends={
        Property(name="File160", type=gast_core_Position, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_Position", type=File, multiplicity=Multiplicity(0, 1))
    }
)
assembly161: BinaryAssociation = BinaryAssociation(
    name="assembly161",
    ends={
        Property(name="File163", type=gast_core_Position, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_Position162", type=File, multiplicity=Multiplicity(0, 1))
    }
)
sourceentity164: BinaryAssociation = BinaryAssociation(
    name="sourceentity164",
    ends={
        Property(name="core165", type=gast_core_Position, multiplicity=Multiplicity(1, 1)),
        Property(name="SourceEntity", type=SourceEntity, multiplicity=Multiplicity(1, 1))
    }
)
aliasedPackage166: BinaryAssociation = BinaryAssociation(
    name="aliasedPackage166",
    ends={
        Property(name="Package167", type=gast_core_PackageAlias, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_PackageAlias", type=Package, multiplicity=Multiplicity(1, 1))
    }
)
position168: BinaryAssociation = BinaryAssociation(
    name="position168",
    ends={
        Property(name="core169", type=gast_core_SourceEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="Position", type=Position, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statements176: BinaryAssociation = BinaryAssociation(
    name="statements176",
    ends={
        Property(name="statements178", type=gast_annotations_CloneInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="Statement177", type=Statement, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
clone179: BinaryAssociation = BinaryAssociation(
    name="clone179",
    ends={
        Property(name="annotations181", type=gast_annotations_CloneInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="Clone180", type=Clone, multiplicity=Multiplicity(1, 1))
    }
)
referencedType182: BinaryAssociation = BinaryAssociation(
    name="referencedType182",
    ends={
        Property(name="GASTType183", type=gast_types_Reference, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_types_Reference", type=GASTType, multiplicity=Multiplicity(1, 1))
    }
)
baseType189: BinaryAssociation = BinaryAssociation(
    name="baseType189",
    ends={
        Property(name="GASTType190", type=gast_types_GASTArray, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_types_GASTArray", type=GASTType, multiplicity=Multiplicity(1, 1))
    }
)
decoratedType184: BinaryAssociation = BinaryAssociation(
    name="decoratedType184",
    ends={
        Property(name="GASTType185", type=gast_types_TypeDecorator, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_types_TypeDecorator", type=GASTType, multiplicity=Multiplicity(1, 1))
    }
)
undecoratedType186: BinaryAssociation = BinaryAssociation(
    name="undecoratedType186",
    ends={
        Property(name="GASTType188", type=gast_types_TypeDecorator, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_types_TypeDecorator187", type=GASTType, multiplicity=Multiplicity(1, 1))
    }
)
surroundingClass193: BinaryAssociation = BinaryAssociation(
    name="surroundingClass193",
    ends={
        Property(name="types195", type=gast_types_TypeAlias, multiplicity=Multiplicity(1, 1)),
        Property(name="GASTClass194", type=GASTClass, multiplicity=Multiplicity(0, 1))
    }
)
surroundingPackage196: BinaryAssociation = BinaryAssociation(
    name="surroundingPackage196",
    ends={
        Property(name="core198", type=gast_types_TypeAlias, multiplicity=Multiplicity(1, 1)),
        Property(name="Package197", type=Package, multiplicity=Multiplicity(0, 1))
    }
)
overriddenMember199: BinaryAssociation = BinaryAssociation(
    name="overriddenMember199",
    ends={
        Property(name="Member", type=gast_types_Member, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_types_Member", type=Member, multiplicity=Multiplicity(0, 1))
    }
)
aliasedType191: BinaryAssociation = BinaryAssociation(
    name="aliasedType191",
    ends={
        Property(name="GASTType192", type=gast_types_TypeAlias, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_types_TypeAlias", type=GASTType, multiplicity=Multiplicity(1, 1))
    }
)
typeBounds200: BinaryAssociation = BinaryAssociation(
    name="typeBounds200",
    ends={
        Property(name="GASTType201", type=gast_types_TypeParameterClass, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_types_TypeParameterClass", type=GASTType, multiplicity=Multiplicity(0, 9999))
    }
)
innerDelegates205: BinaryAssociation = BinaryAssociation(
    name="innerDelegates205",
    ends={
        Property(name="functions207", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="Delegate206", type=Delegate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
constructors208: BinaryAssociation = BinaryAssociation(
    name="constructors208",
    ends={
        Property(name="functions209", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="Constructor", type=Constructor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
destructors210: BinaryAssociation = BinaryAssociation(
    name="destructors210",
    ends={
        Property(name="functions211", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="Destructor", type=Destructor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fields212: BinaryAssociation = BinaryAssociation(
    name="fields212",
    ends={
        Property(name="variables213", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="Field", type=Field, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
methods214: BinaryAssociation = BinaryAssociation(
    name="methods214",
    ends={
        Property(name="functions215", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="Method", type=Method_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
surroundingFunction216: BinaryAssociation = BinaryAssociation(
    name="surroundingFunction216",
    ends={
        Property(name="functions218", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="Function217", type=Function, multiplicity=Multiplicity(0, 1))
    }
)
innerTypeAliases202: BinaryAssociation = BinaryAssociation(
    name="innerTypeAliases202",
    ends={
        Property(name="types204", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="TypeAlias203", type=TypeAlias, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
innerClasses224: BinaryAssociation = BinaryAssociation(
    name="innerClasses224",
    ends={
        Property(name="types226", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="GASTClass225", type=GASTClass, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
surroundingClass227: BinaryAssociation = BinaryAssociation(
    name="surroundingClass227",
    ends={
        Property(name="types229", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="GASTClass228", type=GASTClass, multiplicity=Multiplicity(0, 1))
    }
)
inheritanceTypeAccesses230: BinaryAssociation = BinaryAssociation(
    name="inheritanceTypeAccesses230",
    ends={
        Property(name="InheritanceTypeAccess", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_types_GASTClass231", type=InheritanceTypeAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
self232: BinaryAssociation = BinaryAssociation(
    name="self232",
    ends={
        Property(name="Field234", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_types_GASTClass233", type=Field, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
friendClasses235: BinaryAssociation = BinaryAssociation(
    name="friendClasses235",
    ends={
        Property(name="types237", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="GASTClass236", type=GASTClass, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
surroundingPackage219: BinaryAssociation = BinaryAssociation(
    name="surroundingPackage219",
    ends={
        Property(name="core221", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="Package220", type=Package, multiplicity=Multiplicity(0, 1))
    }
)
superTypes222: BinaryAssociation = BinaryAssociation(
    name="superTypes222",
    ends={
        Property(name="GASTClass223", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_types_GASTClass", type=GASTClass, multiplicity=Multiplicity(0, 9999))
    }
)
targetType252: BinaryAssociation = BinaryAssociation(
    name="targetType252",
    ends={
        Property(name="GASTType253", type=gast_accesses_TypeAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_accesses_TypeAccess", type=GASTType, multiplicity=Multiplicity(1, 1))
    }
)
typeArguments254: BinaryAssociation = BinaryAssociation(
    name="typeArguments254",
    ends={
        Property(name="GASTType256", type=gast_accesses_TypeAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_accesses_TypeAccess255", type=GASTType, multiplicity=Multiplicity(0, 9999))
    }
)
accesses257: BinaryAssociation = BinaryAssociation(
    name="accesses257",
    ends={
        Property(name="accesses259", type=gast_accesses_CompositeAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="BaseAccess258", type=BaseAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
gastClass238: BinaryAssociation = BinaryAssociation(
    name="gastClass238",
    ends={
        Property(name="types240", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="GASTClass239", type=GASTClass, multiplicity=Multiplicity(0, 1))
    }
)
friendFunctions241: BinaryAssociation = BinaryAssociation(
    name="friendFunctions241",
    ends={
        Property(name="Function243", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_types_GASTClass242", type=Function, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
property244: BinaryAssociation = BinaryAssociation(
    name="property244",
    ends={
        Property(name="Property", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_types_GASTClass245", type=Property_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
allAccesses246: BinaryAssociation = BinaryAssociation(
    name="allAccesses246",
    ends={
        Property(name="Access248", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_types_GASTClass247", type=Access, multiplicity=Multiplicity(0, 9999))
    }
)
allAccessedClasses249: BinaryAssociation = BinaryAssociation(
    name="allAccessedClasses249",
    ends={
        Property(name="GASTClass251", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_types_GASTClass250", type=GASTClass, multiplicity=Multiplicity(0, 9999))
    }
)
parentStatement260: BinaryAssociation = BinaryAssociation(
    name="parentStatement260",
    ends={
        Property(name="statements262", type=gast_accesses_BaseAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="Statement261", type=Statement, multiplicity=Multiplicity(0, 1))
    }
)
surroundingStatement263: BinaryAssociation = BinaryAssociation(
    name="surroundingStatement263",
    ends={
        Property(name="Statement264", type=gast_accesses_BaseAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_accesses_BaseAccess", type=Statement, multiplicity=Multiplicity(0, 1))
    }
)
surroundingCompositeAccess271: BinaryAssociation = BinaryAssociation(
    name="surroundingCompositeAccess271",
    ends={
        Property(name="accesses272", type=gast_accesses_BaseAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="CompositeAccess", type=CompositeAccess, multiplicity=Multiplicity(0, 1))
    }
)
function273: BinaryAssociation = BinaryAssociation(
    name="function273",
    ends={
        Property(name="functions275", type=gast_accesses_DeclarationTypeAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="Function274", type=Function, multiplicity=Multiplicity(0, 1))
    }
)
surroundingVariable276: BinaryAssociation = BinaryAssociation(
    name="surroundingVariable276",
    ends={
        Property(name="variables277", type=gast_accesses_DeclarationTypeAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="Variable", type=Variable, multiplicity=Multiplicity(0, 1))
    }
)
surroundingClass265: BinaryAssociation = BinaryAssociation(
    name="surroundingClass265",
    ends={
        Property(name="GASTClass267", type=gast_accesses_BaseAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_accesses_BaseAccess266", type=GASTClass, multiplicity=Multiplicity(1, 1))
    }
)
surroundingFunction268: BinaryAssociation = BinaryAssociation(
    name="surroundingFunction268",
    ends={
        Property(name="Function270", type=gast_accesses_BaseAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_accesses_BaseAccess269", type=Function, multiplicity=Multiplicity(0, 1))
    }
)
accessedDelegate280: BinaryAssociation = BinaryAssociation(
    name="accessedDelegate280",
    ends={
        Property(name="Delegate282", type=gast_accesses_DelegateAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_accesses_DelegateAccess281", type=Delegate, multiplicity=Multiplicity(1, 1))
    }
)
typeArguments283: BinaryAssociation = BinaryAssociation(
    name="typeArguments283",
    ends={
        Property(name="GASTType284", type=gast_accesses_FunctionAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_accesses_FunctionAccess", type=GASTType, multiplicity=Multiplicity(0, 9999))
    }
)
targetFunction285: BinaryAssociation = BinaryAssociation(
    name="targetFunction285",
    ends={
        Property(name="Function287", type=gast_accesses_FunctionAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_accesses_FunctionAccess286", type=Function, multiplicity=Multiplicity(1, 1))
    }
)
accessedFunctions278: BinaryAssociation = BinaryAssociation(
    name="accessedFunctions278",
    ends={
        Property(name="Function279", type=gast_accesses_DelegateAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_accesses_DelegateAccess", type=Function, multiplicity=Multiplicity(0, 9999))
    }
)
accessedClass290: BinaryAssociation = BinaryAssociation(
    name="accessedClass290",
    ends={
        Property(name="GASTClass291", type=gast_accesses_Access, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_accesses_Access", type=GASTClass, multiplicity=Multiplicity(1, 1))
    }
)
accessedTarget292: BinaryAssociation = BinaryAssociation(
    name="accessedTarget292",
    ends={
        Property(name="ModelElement294", type=gast_accesses_Access, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_accesses_Access293", type=ModelElement, multiplicity=Multiplicity(1, 1))
    }
)
targetVariable288: BinaryAssociation = BinaryAssociation(
    name="targetVariable288",
    ends={
        Property(name="Variable289", type=gast_accesses_VariableAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_accesses_VariableAccess", type=Variable, multiplicity=Multiplicity(1, 1))
    }
)
invocations297: BinaryAssociation = BinaryAssociation(
    name="invocations297",
    ends={
        Property(name="Function299", type=gast_functions_Delegate, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_functions_Delegate298", type=Function, multiplicity=Multiplicity(0, 9999))
    }
)
surroundingClass300: BinaryAssociation = BinaryAssociation(
    name="surroundingClass300",
    ends={
        Property(name="types302", type=gast_functions_Delegate, multiplicity=Multiplicity(1, 1)),
        Property(name="GASTClass301", type=GASTClass, multiplicity=Multiplicity(0, 1))
    }
)
surroundingPackage303: BinaryAssociation = BinaryAssociation(
    name="surroundingPackage303",
    ends={
        Property(name="core305", type=gast_functions_Delegate, multiplicity=Multiplicity(1, 1)),
        Property(name="Package304", type=Package, multiplicity=Multiplicity(0, 1))
    }
)
surroundingClass306: BinaryAssociation = BinaryAssociation(
    name="surroundingClass306",
    ends={
        Property(name="types308", type=gast_functions_Constructor, multiplicity=Multiplicity(1, 1)),
        Property(name="GASTClass307", type=GASTClass, multiplicity=Multiplicity(1, 1))
    }
)
surroundingClass309: BinaryAssociation = BinaryAssociation(
    name="surroundingClass309",
    ends={
        Property(name="types311", type=gast_functions_Destructor, multiplicity=Multiplicity(1, 1)),
        Property(name="GASTClass310", type=GASTClass, multiplicity=Multiplicity(1, 1))
    }
)
superClass295: BinaryAssociation = BinaryAssociation(
    name="superClass295",
    ends={
        Property(name="GASTClass296", type=gast_functions_Delegate, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_functions_Delegate", type=GASTClass, multiplicity=Multiplicity(0, 1))
    }
)
surroundingProperty318: BinaryAssociation = BinaryAssociation(
    name="surroundingProperty318",
    ends={
        Property(name="Property319", type=gast_functions_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_functions_Method", type=Property_, multiplicity=Multiplicity(0, 1))
    }
)
surroundingClass320: BinaryAssociation = BinaryAssociation(
    name="surroundingClass320",
    ends={
        Property(name="types322", type=gast_functions_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="GASTClass321", type=GASTClass, multiplicity=Multiplicity(1, 1))
    }
)
surroundingPackage312: BinaryAssociation = BinaryAssociation(
    name="surroundingPackage312",
    ends={
        Property(name="core314", type=gast_functions_GlobalFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="Package313", type=Package, multiplicity=Multiplicity(0, 1))
    }
)
root315: BinaryAssociation = BinaryAssociation(
    name="root315",
    ends={
        Property(name="core317", type=gast_functions_GlobalFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="Root316", type=Root, multiplicity=Multiplicity(0, 1))
    }
)
returnTypeDeclaration323: BinaryAssociation = BinaryAssociation(
    name="returnTypeDeclaration323",
    ends={
        Property(name="accesses324", type=gast_functions_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="DeclarationTypeAccess", type=DeclarationTypeAccess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
formalParameters325: BinaryAssociation = BinaryAssociation(
    name="formalParameters325",
    ends={
        Property(name="variables326", type=gast_functions_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="FormalParameter", type=FormalParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
localVariables327: BinaryAssociation = BinaryAssociation(
    name="localVariables327",
    ends={
        Property(name="variables328", type=gast_functions_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="LocalVariable", type=LocalVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
allStatements329: BinaryAssociation = BinaryAssociation(
    name="allStatements329",
    ends={
        Property(name="Statement330", type=gast_functions_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_functions_Function", type=Statement, multiplicity=Multiplicity(0, 9999))
    }
)
throwTypeAccesses331: BinaryAssociation = BinaryAssociation(
    name="throwTypeAccesses331",
    ends={
        Property(name="ThrowTypeAccess", type=gast_functions_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_functions_Function332", type=ThrowTypeAccess, multiplicity=Multiplicity(0, 9999))
    }
)
accesses333: BinaryAssociation = BinaryAssociation(
    name="accesses333",
    ends={
        Property(name="Access335", type=gast_functions_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_functions_Function334", type=Access, multiplicity=Multiplicity(0, 9999))
    }
)
surroundingFunction342: BinaryAssociation = BinaryAssociation(
    name="surroundingFunction342",
    ends={
        Property(name="functions344", type=gast_variables_FormalParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="Function343", type=Function, multiplicity=Multiplicity(1, 1))
    }
)
type345: BinaryAssociation = BinaryAssociation(
    name="type345",
    ends={
        Property(name="GASTType346", type=gast_variables_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_variables_Variable", type=GASTType, multiplicity=Multiplicity(1, 1))
    }
)
typeDeclaration347: BinaryAssociation = BinaryAssociation(
    name="typeDeclaration347",
    ends={
        Property(name="accesses349", type=gast_variables_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="DeclarationTypeAccess348", type=DeclarationTypeAccess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body336: BinaryAssociation = BinaryAssociation(
    name="body336",
    ends={
        Property(name="statements338", type=gast_functions_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="BlockStatement337", type=BlockStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
localClasses339: BinaryAssociation = BinaryAssociation(
    name="localClasses339",
    ends={
        Property(name="types341", type=gast_functions_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="GASTClass340", type=GASTClass, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
getter358: BinaryAssociation = BinaryAssociation(
    name="getter358",
    ends={
        Property(name="Method360", type=gast_variables_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_variables_Property359", type=Method_, multiplicity=Multiplicity(0, 1))
    }
)
surroundingPackage361: BinaryAssociation = BinaryAssociation(
    name="surroundingPackage361",
    ends={
        Property(name="core363", type=gast_variables_GlobalVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="Package362", type=Package, multiplicity=Multiplicity(0, 1))
    }
)
surroundingClass350: BinaryAssociation = BinaryAssociation(
    name="surroundingClass350",
    ends={
        Property(name="types352", type=gast_variables_Field, multiplicity=Multiplicity(1, 1)),
        Property(name="GASTClass351", type=GASTClass, multiplicity=Multiplicity(0, 1))
    }
)
surroundingFunction353: BinaryAssociation = BinaryAssociation(
    name="surroundingFunction353",
    ends={
        Property(name="functions355", type=gast_variables_LocalVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="Function354", type=Function, multiplicity=Multiplicity(1, 1))
    }
)
setter356: BinaryAssociation = BinaryAssociation(
    name="setter356",
    ends={
        Property(name="Method357", type=gast_variables_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_variables_Property", type=Method_, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_gast_statements_Statement_SourceEntity = Generalization(general=SourceEntity, specific=gast_statements_Statement)
gen_gast_statements_ExceptionHandler_Statement = Generalization(general=Statement, specific=gast_statements_ExceptionHandler)
gen_gast_statements_BlockStatement_Statement = Generalization(general=Statement, specific=gast_statements_BlockStatement)
gen_gast_statements_Branch_SourceEntity = Generalization(general=SourceEntity, specific=gast_statements_Branch)
gen_gast_statements_GASTExpression_SourceEntity = Generalization(general=SourceEntity, specific=gast_statements_GASTExpression)
gen_gast_statements_BranchStatement_Statement = Generalization(general=Statement, specific=gast_statements_BranchStatement)
gen_gast_statements_LoopStatement_Statement = Generalization(general=Statement, specific=gast_statements_LoopStatement)
gen_gast_statements_CatchBlock_BlockStatement = Generalization(general=BlockStatement, specific=gast_statements_CatchBlock)
gen_gast_statements_JumpStatement_Statement = Generalization(general=Statement, specific=gast_statements_JumpStatement)
gen_gast_statements_SimpleStatement_Statement = Generalization(general=Statement, specific=gast_statements_SimpleStatement)
gen_gast_core_BasePath_ModelElement = Generalization(general=ModelElement, specific=gast_core_BasePath)
gen_gast_core_NamedModelElement_ModelElement = Generalization(general=ModelElement, specific=gast_core_NamedModelElement)
gen_gast_core_ModelElement_Identifier = Generalization(general=Identifier, specific=gast_core_ModelElement)
gen_gast_core_Package_NamedModelElement = Generalization(general=NamedModelElement, specific=gast_core_Package)
gen_gast_core_Root_ModelElement = Generalization(general=ModelElement, specific=gast_core_Root)
gen_gast_core_GenericEntity_ModelElement = Generalization(general=ModelElement, specific=gast_core_GenericEntity)
gen_gast_core_Directory_NamedModelElement = Generalization(general=NamedModelElement, specific=gast_core_Directory)
gen_gast_core_File_NamedModelElement = Generalization(general=NamedModelElement, specific=gast_core_File)
gen_gast_annotations_Attribute_types_GASTClass = Generalization(general=types_GASTClass, specific=gast_annotations_Attribute)
gen_gast_annotations_Attribute_annotations_ModelAnnotation = Generalization(general=annotations_ModelAnnotation, specific=gast_annotations_Attribute)
gen_gast_annotations_Clone_core_ModelElement = Generalization(general=core_ModelElement, specific=gast_annotations_Clone)
gen_gast_annotations_Clone_annotations_ModelAnnotation = Generalization(general=annotations_ModelAnnotation, specific=gast_annotations_Clone)
gen_gast_annotations_CloneInstance_core_ModelElement = Generalization(general=core_ModelElement, specific=gast_annotations_CloneInstance)
gen_gast_annotations_CloneInstance_annotations_ModelAnnotation = Generalization(general=annotations_ModelAnnotation, specific=gast_annotations_CloneInstance)
gen_gast_core_PackageAlias_Package = Generalization(general=Package, specific=gast_core_PackageAlias)
gen_gast_core_SourceEntity_ModelElement = Generalization(general=ModelElement, specific=gast_core_SourceEntity)
gen_gast_annotations_Comment_core_SourceEntity = Generalization(general=core_SourceEntity, specific=gast_annotations_Comment)
gen_gast_annotations_Comment_annotations_ModelAnnotation = Generalization(general=annotations_ModelAnnotation, specific=gast_annotations_Comment)
gen_gast_annotations_StructuralAbstraction_core_NamedModelElement = Generalization(general=core_NamedModelElement, specific=gast_annotations_StructuralAbstraction)
gen_gast_annotations_StructuralAbstraction_annotations_ModelAnnotation = Generalization(general=annotations_ModelAnnotation, specific=gast_annotations_StructuralAbstraction)
gen_gast_annotations_Layer_StructuralAbstraction = Generalization(general=StructuralAbstraction, specific=gast_annotations_Layer)
gen_gast_types_Reference_TypeDecorator = Generalization(general=TypeDecorator, specific=gast_types_Reference)
gen_gast_annotations_Subsystem_StructuralAbstraction = Generalization(general=StructuralAbstraction, specific=gast_annotations_Subsystem)
gen_gast_types_GASTType_NamedModelElement = Generalization(general=NamedModelElement, specific=gast_types_GASTType)
gen_gast_types_GASTArray_TypeDecorator = Generalization(general=TypeDecorator, specific=gast_types_GASTArray)
gen_gast_types_TypeDecorator_GASTType = Generalization(general=GASTType, specific=gast_types_TypeDecorator)
gen_gast_types_Member_SourceEntity = Generalization(general=SourceEntity, specific=gast_types_Member)
gen_gast_types_TypeAlias_types_Member = Generalization(general=types_Member, specific=gast_types_TypeAlias)
gen_gast_types_TypeAlias_types_TypeDecorator = Generalization(general=types_TypeDecorator, specific=gast_types_TypeAlias)
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
gen_gast_accesses_CompositeAccess_BaseAccess = Generalization(general=BaseAccess, specific=gast_accesses_CompositeAccess)
gen_gast_accesses_BaseAccess_SourceEntity = Generalization(general=SourceEntity, specific=gast_accesses_BaseAccess)
gen_gast_accesses_DeclarationTypeAccess_TypeAccess = Generalization(general=TypeAccess, specific=gast_accesses_DeclarationTypeAccess)
gen_gast_accesses_FunctionAccess_Access = Generalization(general=Access, specific=gast_accesses_FunctionAccess)
gen_gast_accesses_ThrowTypeAccess_TypeAccess = Generalization(general=TypeAccess, specific=gast_accesses_ThrowTypeAccess)
gen_gast_accesses_DelegateAccess_FunctionAccess = Generalization(general=FunctionAccess, specific=gast_accesses_DelegateAccess)
gen_gast_accesses_RunTimeTypeAccess_TypeAccess = Generalization(general=TypeAccess, specific=gast_accesses_RunTimeTypeAccess)
gen_gast_accesses_SelfAccess_VariableAccess = Generalization(general=VariableAccess, specific=gast_accesses_SelfAccess)
gen_gast_accesses_StaticTypeAccess_TypeAccess = Generalization(general=TypeAccess, specific=gast_accesses_StaticTypeAccess)
gen_gast_accesses_PropertyAccess_VariableAccess = Generalization(general=VariableAccess, specific=gast_accesses_PropertyAccess)
gen_gast_accesses_Access_BaseAccess = Generalization(general=BaseAccess, specific=gast_accesses_Access)
gen_gast_accesses_InheritanceTypeAccess_TypeAccess = Generalization(general=TypeAccess, specific=gast_accesses_InheritanceTypeAccess)
gen_gast_accesses_VariableAccess_Access = Generalization(general=Access, specific=gast_accesses_VariableAccess)
gen_gast_functions_Constructor_functions_Function = Generalization(general=functions_Function, specific=gast_functions_Constructor)
gen_gast_functions_Constructor_types_Member = Generalization(general=types_Member, specific=gast_functions_Constructor)
gen_gast_functions_Destructor_functions_Function = Generalization(general=functions_Function, specific=gast_functions_Destructor)
gen_gast_functions_Destructor_types_Member = Generalization(general=types_Member, specific=gast_functions_Destructor)
gen_gast_functions_GenericFunction_functions_GlobalFunction = Generalization(general=functions_GlobalFunction, specific=gast_functions_GenericFunction)
gen_gast_functions_GenericFunction_core_GenericEntity = Generalization(general=core_GenericEntity, specific=gast_functions_GenericFunction)
gen_gast_functions_Delegate_functions_Function = Generalization(general=functions_Function, specific=gast_functions_Delegate)
gen_gast_functions_Delegate_types_Member = Generalization(general=types_Member, specific=gast_functions_Delegate)
gen_gast_functions_Delegate_types_GASTType = Generalization(general=types_GASTType, specific=gast_functions_Delegate)
gen_gast_functions_Method_functions_Function = Generalization(general=functions_Function, specific=gast_functions_Method)
gen_gast_functions_Method_types_Member = Generalization(general=types_Member, specific=gast_functions_Method)
gen_gast_functions_GlobalFunction_Function = Generalization(general=Function, specific=gast_functions_GlobalFunction)
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
gen_gast_variables_GlobalVariable_Variable = Generalization(general=Variable, specific=gast_variables_GlobalVariable)
gen_gast_variables_Field_types_Member = Generalization(general=types_Member, specific=gast_variables_Field)
gen_gast_variables_Field_variables_Variable = Generalization(general=variables_Variable, specific=gast_variables_Field)
gen_gast_variables_LocalVariable_Variable = Generalization(general=Variable, specific=gast_variables_LocalVariable)
gen_gast_variables_Property_variables_Field = Generalization(general=variables_Field, specific=gast_variables_Property)
gen_gast_variables_Property_types_Member = Generalization(general=types_Member, specific=gast_variables_Property)

# Domain Model
domain_model = DomainModel(
    name="gast",
    types={gast_statements_Statement, SourceEntity, BaseAccess, CloneInstance, gast_statements_ExceptionHandler, Statement, CatchBlock, BlockStatement, Branch, LoopStatement, gast_statements_BlockStatement, gast_statements_Branch, GASTExpression, BranchStatement, gast_statements_GASTExpression, gast_statements_BranchStatement, Function, gast_statements_LoopStatement, gast_statements_CatchBlock, CatchParameter, gast_statements_JumpStatement, gast_statements_SimpleStatement, gast_statements_GASTBehaviour, gast_core_BasePath, ModelElement, Root, ModelAnnotation, gast_core_Identifier, gast_core_NamedModelElement, Directory, gast_core_ModelElement, Identifier, GASTClass, Package, gast_core_Package, NamedModelElement, Access, Delegate, GlobalFunction, GlobalVariable, gast_core_Root, TypeAlias, gast_core_GenericEntity, TypeParameterClass, StructuralAbstraction, GASTType, BasePath, Clone, gast_core_Directory, File, gast_core_File, gast_core_Position, gast_annotations_Attribute, types_GASTClass, annotations_ModelAnnotation, gast_annotations_Clone, core_ModelElement, gast_annotations_CloneInstance, gast_core_PackageAlias, gast_core_SourceEntity, Position, gast_annotations_Comment, core_SourceEntity, gast_annotations_StructuralAbstraction, core_NamedModelElement, gast_annotations_ModelAnnotation, gast_types_Reference, TypeDecorator, gast_annotations_Subsystem, gast_annotations_Layer, gast_types_GASTType, gast_types_GASTArray, gast_types_TypeDecorator, gast_types_Member, Member, gast_types_TypeAlias, types_Member, types_TypeDecorator, gast_types_TypeParameterClass, Constructor, Destructor, Field, Method_, gast_types_GenericClass, core_GenericEntity, gast_types_GASTEnumeration, gast_types_GASTStruct, gast_types_GASTUnion, gast_types_GASTClass, types_GASTType, InheritanceTypeAccess, gast_accesses_ParameterInstantiationTypeAccess, TypeAccess, gast_accesses_TypeAccess, gast_accesses_CastTypeAccess, gast_accesses_CompositeAccess, Property_, gast_accesses_BaseAccess, CompositeAccess, gast_accesses_DeclarationTypeAccess, Variable, gast_accesses_ThrowTypeAccess, gast_accesses_FunctionAccess, gast_accesses_DelegateAccess, FunctionAccess, gast_accesses_RunTimeTypeAccess, gast_accesses_SelfAccess, VariableAccess, gast_accesses_StaticTypeAccess, gast_accesses_PropertyAccess, gast_accesses_Access, gast_accesses_InheritanceTypeAccess, gast_accesses_VariableAccess, gast_functions_Constructor, gast_functions_Destructor, gast_functions_GenericFunction, functions_GlobalFunction, gast_functions_Delegate, functions_Function, gast_functions_Method, gast_functions_GlobalFunction, DeclarationTypeAccess, FormalParameter, LocalVariable, ThrowTypeAccess, gast_functions_GenericMethod, functions_Method, gast_functions_GenericConstructor, functions_Constructor, gast_functions_Function, gast_variables_FormalParameter, gast_variables_Variable, gast_variables_CatchParameter, gast_variables_GlobalVariable, gast_variables_Field, variables_Variable, gast_variables_LocalVariable, gast_variables_Property, variables_Field, LoopStatementKind, JumpStatementKind, Status, Visibilities, GlobalFunctionKind},
    associations={finallyBlock1, guardedBlock3, accesses6, cloneInstance7, blockstatement8, surroundingStatement10, catchBlocks0, branch11, loopstatement13, statements15, conditionExpression19, branchstatement20, statement22, surroundingFunction18, breakConditionExpression28, initExpression30, incrementExpression33, body36, branches25, catchParameter39, expression40, expression42, blockstatement44, root46, annotations49, directories47, allLocalClasses50, allInnerClasses51, allNormalClasses54, allInterfaces57, classes70, subPackages72, surroundingPackage74, allAccesses60, allAccessedPackages77, delegates62, globalFunctions64, globalVariables66, root67, typeAliases80, typeParameters82, allLocalClasses91, allNormalClasses94, allModelElements97, allAccesses83, allInnerClasses85, allInterfaces88, structuralAbstractions107, types109, danglingModelElements111, basePaths114, globalFunctions116, globalVariables99, packages102, clones105, subDirectory119, files125, basePath127, parentDirectory122, importedTypes132, types135, globalVariables138, globalFunctions141, includedFiles153, root130, directory156, importedGlobalFunctions144, importedGlobalVariables147, importedPackages150, cloneInstances170, root173, sourceFile159, assembly161, sourceentity164, aliasedPackage166, position168, statements176, clone179, referencedType182, baseType189, decoratedType184, undecoratedType186, surroundingClass193, surroundingPackage196, overriddenMember199, aliasedType191, typeBounds200, innerDelegates205, constructors208, destructors210, fields212, methods214, surroundingFunction216, innerTypeAliases202, innerClasses224, surroundingClass227, inheritanceTypeAccesses230, self232, friendClasses235, surroundingPackage219, superTypes222, targetType252, typeArguments254, accesses257, gastClass238, friendFunctions241, property244, allAccesses246, allAccessedClasses249, parentStatement260, surroundingStatement263, surroundingCompositeAccess271, function273, surroundingVariable276, surroundingClass265, surroundingFunction268, accessedDelegate280, typeArguments283, targetFunction285, accessedFunctions278, accessedClass290, accessedTarget292, targetVariable288, invocations297, surroundingClass300, surroundingPackage303, surroundingClass306, surroundingClass309, superClass295, surroundingProperty318, surroundingClass320, surroundingPackage312, root315, returnTypeDeclaration323, formalParameters325, localVariables327, allStatements329, throwTypeAccesses331, accesses333, surroundingFunction342, type345, typeDeclaration347, body336, localClasses339, getter358, surroundingPackage361, surroundingClass350, surroundingFunction353, setter356},
    generalizations={gen_gast_statements_Statement_SourceEntity, gen_gast_statements_ExceptionHandler_Statement, gen_gast_statements_BlockStatement_Statement, gen_gast_statements_Branch_SourceEntity, gen_gast_statements_GASTExpression_SourceEntity, gen_gast_statements_BranchStatement_Statement, gen_gast_statements_LoopStatement_Statement, gen_gast_statements_CatchBlock_BlockStatement, gen_gast_statements_JumpStatement_Statement, gen_gast_statements_SimpleStatement_Statement, gen_gast_core_BasePath_ModelElement, gen_gast_core_NamedModelElement_ModelElement, gen_gast_core_ModelElement_Identifier, gen_gast_core_Package_NamedModelElement, gen_gast_core_Root_ModelElement, gen_gast_core_GenericEntity_ModelElement, gen_gast_core_Directory_NamedModelElement, gen_gast_core_File_NamedModelElement, gen_gast_annotations_Attribute_types_GASTClass, gen_gast_annotations_Attribute_annotations_ModelAnnotation, gen_gast_annotations_Clone_core_ModelElement, gen_gast_annotations_Clone_annotations_ModelAnnotation, gen_gast_annotations_CloneInstance_core_ModelElement, gen_gast_annotations_CloneInstance_annotations_ModelAnnotation, gen_gast_core_PackageAlias_Package, gen_gast_core_SourceEntity_ModelElement, gen_gast_annotations_Comment_core_SourceEntity, gen_gast_annotations_Comment_annotations_ModelAnnotation, gen_gast_annotations_StructuralAbstraction_core_NamedModelElement, gen_gast_annotations_StructuralAbstraction_annotations_ModelAnnotation, gen_gast_annotations_Layer_StructuralAbstraction, gen_gast_types_Reference_TypeDecorator, gen_gast_annotations_Subsystem_StructuralAbstraction, gen_gast_types_GASTType_NamedModelElement, gen_gast_types_GASTArray_TypeDecorator, gen_gast_types_TypeDecorator_GASTType, gen_gast_types_Member_SourceEntity, gen_gast_types_TypeAlias_types_Member, gen_gast_types_TypeAlias_types_TypeDecorator, gen_gast_types_TypeParameterClass_GASTClass, gen_gast_types_GenericClass_types_GASTClass, gen_gast_types_GenericClass_core_GenericEntity, gen_gast_types_GASTEnumeration_GASTClass, gen_gast_types_GASTStruct_GASTClass, gen_gast_types_GASTUnion_GASTClass, gen_gast_types_GASTClass_types_Member, gen_gast_types_GASTClass_types_GASTType, gen_gast_accesses_ParameterInstantiationTypeAccess_TypeAccess, gen_gast_accesses_TypeAccess_Access, gen_gast_accesses_CastTypeAccess_TypeAccess, gen_gast_accesses_CompositeAccess_BaseAccess, gen_gast_accesses_BaseAccess_SourceEntity, gen_gast_accesses_DeclarationTypeAccess_TypeAccess, gen_gast_accesses_FunctionAccess_Access, gen_gast_accesses_ThrowTypeAccess_TypeAccess, gen_gast_accesses_DelegateAccess_FunctionAccess, gen_gast_accesses_RunTimeTypeAccess_TypeAccess, gen_gast_accesses_SelfAccess_VariableAccess, gen_gast_accesses_StaticTypeAccess_TypeAccess, gen_gast_accesses_PropertyAccess_VariableAccess, gen_gast_accesses_Access_BaseAccess, gen_gast_accesses_InheritanceTypeAccess_TypeAccess, gen_gast_accesses_VariableAccess_Access, gen_gast_functions_Constructor_functions_Function, gen_gast_functions_Constructor_types_Member, gen_gast_functions_Destructor_functions_Function, gen_gast_functions_Destructor_types_Member, gen_gast_functions_GenericFunction_functions_GlobalFunction, gen_gast_functions_GenericFunction_core_GenericEntity, gen_gast_functions_Delegate_functions_Function, gen_gast_functions_Delegate_types_Member, gen_gast_functions_Delegate_types_GASTType, gen_gast_functions_Method_functions_Function, gen_gast_functions_Method_types_Member, gen_gast_functions_GlobalFunction_Function, gen_gast_functions_GenericMethod_functions_Method, gen_gast_functions_GenericMethod_core_GenericEntity, gen_gast_functions_GenericConstructor_functions_Constructor, gen_gast_functions_GenericConstructor_core_GenericEntity, gen_gast_functions_Function_core_NamedModelElement, gen_gast_functions_Function_core_SourceEntity, gen_gast_variables_FormalParameter_Variable, gen_gast_variables_Variable_core_NamedModelElement, gen_gast_variables_Variable_core_SourceEntity, gen_gast_variables_CatchParameter_Variable, gen_gast_variables_GlobalVariable_Variable, gen_gast_variables_Field_types_Member, gen_gast_variables_Field_variables_Variable, gen_gast_variables_LocalVariable_Variable, gen_gast_variables_Property_variables_Field, gen_gast_variables_Property_types_Member},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)