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
            EnumerationLiteral(name="VISIBILITYPRIVAT"),
			EnumerationLiteral(name="VISIBILITYSTRICTPROTECTED"),
			EnumerationLiteral(name="VISIBILITYPUBLIC"),
			EnumerationLiteral(name="VISIBILITYPACKAGE"),
			EnumerationLiteral(name="VISIBILITYPROTECTED")
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
gast_statements_ExceptionHandler = Class(name="gast::statements::ExceptionHandler")
Statement = Class(name="Statement")
CatchBlock = Class(name="CatchBlock")
BlockStatement = Class(name="BlockStatement")
gast_statements_Statement = Class(name="gast::statements::Statement", is_abstract=True)
SourceEntity = Class(name="SourceEntity")
BaseAccess = Class(name="BaseAccess")
CloneInstance = Class(name="CloneInstance")
Function = Class(name="Function")
gast_statements_Branch = Class(name="gast::statements::Branch")
GASTExpression = Class(name="GASTExpression")
BranchStatement = Class(name="BranchStatement")
gast_statements_GASTExpression = Class(name="gast::statements::GASTExpression", is_abstract=True)
gast_statements_BranchStatement = Class(name="gast::statements::BranchStatement")
Branch = Class(name="Branch")
LoopStatement = Class(name="LoopStatement")
gast_statements_BlockStatement = Class(name="gast::statements::BlockStatement")
gast_statements_CatchBlock = Class(name="gast::statements::CatchBlock")
CatchParameter = Class(name="CatchParameter")
gast_statements_LoopStatement = Class(name="gast::statements::LoopStatement")
gast_statements_GASTBehaviour = Class(name="gast::statements::GASTBehaviour")
gast_statements_Methods = Class(name="gast::statements::Methods")
Exit = Class(name="Exit")
gast_statements_Exit = Class(name="gast::statements::Exit")
gast_core_BasePath = Class(name="gast::core::BasePath")
ModelElement = Class(name="ModelElement")
Root = Class(name="Root")
gast_statements_JumpStatement = Class(name="gast::statements::JumpStatement")
gast_statements_SimpleStatement = Class(name="gast::statements::SimpleStatement")
gast_core_NamedModelElement = Class(name="gast::core::NamedModelElement", is_abstract=True)
gast_core_Package = Class(name="gast::core::Package")
NamedModelElement = Class(name="NamedModelElement")
GASTClass = Class(name="GASTClass")
Directory = Class(name="Directory")
gast_core_ModelElement = Class(name="gast::core::ModelElement", is_abstract=True)
Identifier = Class(name="Identifier")
ModelAnnotation = Class(name="ModelAnnotation")
gast_core_Identifier = Class(name="gast::core::Identifier", is_abstract=True)
GlobalFunction = Class(name="GlobalFunction")
GlobalVariable = Class(name="GlobalVariable")
Access = Class(name="Access")
Delegate = Class(name="Delegate")
TypeAlias = Class(name="TypeAlias")
gast_core_GenericEntity = Class(name="gast::core::GenericEntity", is_abstract=True)
TypeParameterClass = Class(name="TypeParameterClass")
gast_core_Root = Class(name="gast::core::Root")
Package = Class(name="Package")
Clone = Class(name="Clone")
StructuralAbstraction = Class(name="StructuralAbstraction")
GASTType = Class(name="GASTType")
BasePath = Class(name="BasePath")
File = Class(name="File")
gast_core_File = Class(name="gast::core::File")
gast_core_Directory = Class(name="gast::core::Directory")
gast_core_PackageAlias = Class(name="gast::core::PackageAlias")
gast_core_SourceEntity = Class(name="gast::core::SourceEntity", is_abstract=True)
Position = Class(name="Position")
gast_core_Position = Class(name="gast::core::Position")
gast_annotations_StructuralAbstraction = Class(name="gast::annotations::StructuralAbstraction", is_abstract=True)
core_NamedModelElement = Class(name="core::NamedModelElement")
gast_annotations_Comment = Class(name="gast::annotations::Comment")
core_SourceEntity = Class(name="core::SourceEntity")
gast_annotations_Attribute = Class(name="gast::annotations::Attribute")
types_GASTClass = Class(name="types::GASTClass")
annotations_ModelAnnotation = Class(name="annotations::ModelAnnotation")
gast_annotations_Clone = Class(name="gast::annotations::Clone")
core_ModelElement = Class(name="core::ModelElement")
gast_annotations_CloneInstance = Class(name="gast::annotations::CloneInstance")
gast_types_TypeDecorator = Class(name="gast::types::TypeDecorator", is_abstract=True)
gast_types_GASTType = Class(name="gast::types::GASTType", is_abstract=True)
gast_types_GASTArray = Class(name="gast::types::GASTArray")
gast_annotations_Subsystem = Class(name="gast::annotations::Subsystem")
gast_annotations_Layer = Class(name="gast::annotations::Layer")
gast_annotations_ModelAnnotation = Class(name="gast::annotations::ModelAnnotation", is_abstract=True)
gast_types_Reference = Class(name="gast::types::Reference")
TypeDecorator = Class(name="TypeDecorator")
gast_types_Member = Class(name="gast::types::Member", is_abstract=True)
Member = Class(name="Member")
gast_types_TypeAlias = Class(name="gast::types::TypeAlias")
types_Member = Class(name="types::Member")
types_TypeDecorator = Class(name="types::TypeDecorator")
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
Property_ = Class(name="Property")
gast_accesses_ParameterInstantiationTypeAccess = Class(name="gast::accesses::ParameterInstantiationTypeAccess")
TypeAccess = Class(name="TypeAccess")
InheritanceTypeAccess = Class(name="InheritanceTypeAccess")
CompositeAccess = Class(name="CompositeAccess")
gast_accesses_TypeAccess = Class(name="gast::accesses::TypeAccess", is_abstract=True)
gast_accesses_DeclarationTypeAccess = Class(name="gast::accesses::DeclarationTypeAccess")
gast_accesses_CastTypeAccess = Class(name="gast::accesses::CastTypeAccess")
gast_accesses_CompositeAccess = Class(name="gast::accesses::CompositeAccess")
gast_accesses_BaseAccess = Class(name="gast::accesses::BaseAccess", is_abstract=True)
gast_accesses_DelegateAccess = Class(name="gast::accesses::DelegateAccess")
FunctionAccess = Class(name="FunctionAccess")
gast_accesses_FunctionAccess = Class(name="gast::accesses::FunctionAccess")
Variable = Class(name="Variable")
gast_accesses_ThrowTypeAccess = Class(name="gast::accesses::ThrowTypeAccess")
gast_accesses_InheritanceTypeAccess = Class(name="gast::accesses::InheritanceTypeAccess")
gast_accesses_VariableAccess = Class(name="gast::accesses::VariableAccess")
gast_accesses_RunTimeTypeAccess = Class(name="gast::accesses::RunTimeTypeAccess")
gast_accesses_SelfAccess = Class(name="gast::accesses::SelfAccess")
VariableAccess = Class(name="VariableAccess")
gast_functions_Delegate = Class(name="gast::functions::Delegate")
functions_Function = Class(name="functions::Function")
gast_accesses_StaticTypeAccess = Class(name="gast::accesses::StaticTypeAccess")
gast_accesses_PropertyAccess = Class(name="gast::accesses::PropertyAccess")
gast_accesses_Access = Class(name="gast::accesses::Access", is_abstract=True)
gast_functions_Constructor = Class(name="gast::functions::Constructor")
gast_functions_Destructor = Class(name="gast::functions::Destructor")
gast_functions_Method = Class(name="gast::functions::Method")
gast_functions_GenericFunction = Class(name="gast::functions::GenericFunction")
functions_GlobalFunction = Class(name="functions::GlobalFunction")
gast_functions_GlobalFunction = Class(name="gast::functions::GlobalFunction")
LocalVariable = Class(name="LocalVariable")
ThrowTypeAccess = Class(name="ThrowTypeAccess")
gast_functions_GenericMethod = Class(name="gast::functions::GenericMethod")
functions_Method = Class(name="functions::Method")
gast_functions_GenericConstructor = Class(name="gast::functions::GenericConstructor")
functions_Constructor = Class(name="functions::Constructor")
gast_functions_Function = Class(name="gast::functions::Function", is_abstract=True)
DeclarationTypeAccess = Class(name="DeclarationTypeAccess")
FormalParameter = Class(name="FormalParameter")
gast_variables_CatchParameter = Class(name="gast::variables::CatchParameter")
gast_variables_Field = Class(name="gast::variables::Field")
variables_Variable = Class(name="variables::Variable")
gast_variables_LocalVariable = Class(name="gast::variables::LocalVariable")
gast_variables_FormalParameter = Class(name="gast::variables::FormalParameter")
gast_variables_Variable = Class(name="gast::variables::Variable", is_abstract=True)
gast_variables_Property = Class(name="gast::variables::Property")
variables_Field = Class(name="variables::Field")
gast_variables_GlobalVariable = Class(name="gast::variables::GlobalVariable")

# gast_statements_ExceptionHandler class attributes and methods

# Statement class attributes and methods

# CatchBlock class attributes and methods

# BlockStatement class attributes and methods

# gast_statements_Statement class attributes and methods
gast_statements_Statement_numberOfStatements: Property = Property(name="numberOfStatements", type=IntegerType)
gast_statements_Statement_maximumNestingLevel: Property = Property(name="maximumNestingLevel", type=IntegerType)
gast_statements_Statement_numberOfComments: Property = Property(name="numberOfComments", type=IntegerType)
gast_statements_Statement_linesOfCode: Property = Property(name="linesOfCode", type=IntegerType)
gast_statements_Statement_numberOfEdgesInCFG: Property = Property(name="numberOfEdgesInCFG", type=IntegerType)
gast_statements_Statement_numberOfNodesInCFG: Property = Property(name="numberOfNodesInCFG", type=IntegerType)
gast_statements_Statement.attributes={gast_statements_Statement_numberOfComments, gast_statements_Statement_linesOfCode, gast_statements_Statement_numberOfEdgesInCFG, gast_statements_Statement_numberOfNodesInCFG, gast_statements_Statement_maximumNestingLevel, gast_statements_Statement_numberOfStatements}

# SourceEntity class attributes and methods

# BaseAccess class attributes and methods

# CloneInstance class attributes and methods

# Function class attributes and methods

# gast_statements_Branch class attributes and methods

# GASTExpression class attributes and methods

# BranchStatement class attributes and methods

# gast_statements_GASTExpression class attributes and methods

# gast_statements_BranchStatement class attributes and methods

# Branch class attributes and methods

# LoopStatement class attributes and methods

# gast_statements_BlockStatement class attributes and methods
gast_statements_BlockStatement_synchronized: Property = Property(name="synchronized", type=BooleanType)
gast_statements_BlockStatement.attributes={gast_statements_BlockStatement_synchronized}

# gast_statements_CatchBlock class attributes and methods

# CatchParameter class attributes and methods

# gast_statements_LoopStatement class attributes and methods
gast_statements_LoopStatement_kind: Property = Property(name="kind", type=StringType)
gast_statements_LoopStatement.attributes={gast_statements_LoopStatement_kind}

# gast_statements_GASTBehaviour class attributes and methods

# gast_statements_Methods class attributes and methods
gast_statements_Methods_methodName: Property = Property(name="methodName", type=StringType)
gast_statements_Methods.attributes={gast_statements_Methods_methodName}

# Exit class attributes and methods

# gast_statements_Exit class attributes and methods
gast_statements_Exit_name: Property = Property(name="name", type=StringType)
gast_statements_Exit.attributes={gast_statements_Exit_name}

# gast_core_BasePath class attributes and methods
gast_core_BasePath_path: Property = Property(name="path", type=StringType)
gast_core_BasePath.attributes={gast_core_BasePath_path}

# ModelElement class attributes and methods

# Root class attributes and methods

# gast_statements_JumpStatement class attributes and methods
gast_statements_JumpStatement_kind: Property = Property(name="kind", type=StringType)
gast_statements_JumpStatement.attributes={gast_statements_JumpStatement_kind}

# gast_statements_SimpleStatement class attributes and methods

# gast_core_NamedModelElement class attributes and methods
gast_core_NamedModelElement_simpleName: Property = Property(name="simpleName", type=StringType)
gast_core_NamedModelElement.attributes={gast_core_NamedModelElement_simpleName}

# gast_core_Package class attributes and methods
gast_core_Package_linesOfComments: Property = Property(name="linesOfComments", type=IntegerType)
gast_core_Package_linesOfCode: Property = Property(name="linesOfCode", type=IntegerType)
gast_core_Package_qualifiedName: Property = Property(name="qualifiedName", type=StringType)
gast_core_Package.attributes={gast_core_Package_qualifiedName, gast_core_Package_linesOfCode, gast_core_Package_linesOfComments}

# NamedModelElement class attributes and methods

# GASTClass class attributes and methods

# Directory class attributes and methods

# gast_core_ModelElement class attributes and methods
gast_core_ModelElement_status: Property = Property(name="status", type=StringType)
gast_core_ModelElement_sissyId: Property = Property(name="sissyId", type=IntegerType)
gast_core_ModelElement.attributes={gast_core_ModelElement_status, gast_core_ModelElement_sissyId}

# Identifier class attributes and methods

# ModelAnnotation class attributes and methods

# gast_core_Identifier class attributes and methods
gast_core_Identifier_id: Property = Property(name="id", type=StringType)
gast_core_Identifier_m_idHasToBeUnique: Method = Method(name="idHasToBeUnique", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
gast_core_Identifier.attributes={gast_core_Identifier_id}
gast_core_Identifier.methods={gast_core_Identifier_m_idHasToBeUnique}

# GlobalFunction class attributes and methods

# GlobalVariable class attributes and methods

# Access class attributes and methods

# Delegate class attributes and methods

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

# Package class attributes and methods

# Clone class attributes and methods

# StructuralAbstraction class attributes and methods

# GASTType class attributes and methods

# BasePath class attributes and methods

# File class attributes and methods

# gast_core_File class attributes and methods
gast_core_File_sourceFile: Property = Property(name="sourceFile", type=BooleanType)
gast_core_File_linesOfCode: Property = Property(name="linesOfCode", type=IntegerType)
gast_core_File_size: Property = Property(name="size", type=StringType)
gast_core_File_fullQualifiedPath: Property = Property(name="fullQualifiedPath", type=StringType)
gast_core_File_fileSystemPath: Property = Property(name="fileSystemPath", type=StringType)
gast_core_File_assemblyFile: Property = Property(name="assemblyFile", type=BooleanType)
gast_core_File.attributes={gast_core_File_sourceFile, gast_core_File_assemblyFile, gast_core_File_size, gast_core_File_linesOfCode, gast_core_File_fullQualifiedPath, gast_core_File_fileSystemPath}

# gast_core_Directory class attributes and methods
gast_core_Directory_fileSystemPath: Property = Property(name="fileSystemPath", type=StringType)
gast_core_Directory_fullQualifiedPath: Property = Property(name="fullQualifiedPath", type=StringType)
gast_core_Directory.attributes={gast_core_Directory_fileSystemPath, gast_core_Directory_fullQualifiedPath}

# gast_core_PackageAlias class attributes and methods

# gast_core_SourceEntity class attributes and methods

# Position class attributes and methods

# gast_core_Position class attributes and methods
gast_core_Position_endLine: Property = Property(name="endLine", type=IntegerType)
gast_core_Position_startLine: Property = Property(name="startLine", type=IntegerType)
gast_core_Position_endColumn: Property = Property(name="endColumn", type=IntegerType)
gast_core_Position_startColumn: Property = Property(name="startColumn", type=IntegerType)
gast_core_Position_m_EitherAssemblyFileOrSourceFileSet: Method = Method(name="EitherAssemblyFileOrSourceFileSet", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
gast_core_Position.attributes={gast_core_Position_startColumn, gast_core_Position_endColumn, gast_core_Position_endLine, gast_core_Position_startLine}
gast_core_Position.methods={gast_core_Position_m_EitherAssemblyFileOrSourceFileSet}

# gast_annotations_StructuralAbstraction class attributes and methods

# core_NamedModelElement class attributes and methods

# gast_annotations_Comment class attributes and methods
gast_annotations_Comment_todo: Property = Property(name="todo", type=BooleanType)
gast_annotations_Comment_formal: Property = Property(name="formal", type=BooleanType)
gast_annotations_Comment_todoCount: Property = Property(name="todoCount", type=IntegerType)
gast_annotations_Comment_texts: Property = Property(name="texts", type=StringType)
gast_annotations_Comment_m_OCLtodo: Method = Method(name="OCLtodo", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
gast_annotations_Comment.attributes={gast_annotations_Comment_todoCount, gast_annotations_Comment_texts, gast_annotations_Comment_todo, gast_annotations_Comment_formal}
gast_annotations_Comment.methods={gast_annotations_Comment_m_OCLtodo}

# core_SourceEntity class attributes and methods

# gast_annotations_Attribute class attributes and methods

# types_GASTClass class attributes and methods

# annotations_ModelAnnotation class attributes and methods

# gast_annotations_Clone class attributes and methods

# core_ModelElement class attributes and methods

# gast_annotations_CloneInstance class attributes and methods

# gast_types_TypeDecorator class attributes and methods

# gast_types_GASTType class attributes and methods
gast_types_GASTType_qualifiedName: Property = Property(name="qualifiedName", type=StringType)
gast_types_GASTType_referenceType: Property = Property(name="referenceType", type=BooleanType)
gast_types_GASTType.attributes={gast_types_GASTType_referenceType, gast_types_GASTType_qualifiedName}

# gast_types_GASTArray class attributes and methods
gast_types_GASTArray_dimensions: Property = Property(name="dimensions", type=IntegerType)
gast_types_GASTArray.attributes={gast_types_GASTArray_dimensions}

# gast_annotations_Subsystem class attributes and methods

# gast_annotations_Layer class attributes and methods

# gast_annotations_ModelAnnotation class attributes and methods

# gast_types_Reference class attributes and methods
gast_types_Reference_explicit: Property = Property(name="explicit", type=BooleanType)
gast_types_Reference.attributes={gast_types_Reference_explicit}

# TypeDecorator class attributes and methods

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
gast_types_Member.attributes={gast_types_Member_virtual, gast_types_Member_final, gast_types_Member_abstract, gast_types_Member_internal, gast_types_Member_static, gast_types_Member_extern, gast_types_Member_override, gast_types_Member_introspectable, gast_types_Member_visibility, gast_types_Member_typeParameterClassMember}
gast_types_Member.methods={gast_types_Member_m_getSurroundingClass}

# Member class attributes and methods

# gast_types_TypeAlias class attributes and methods
gast_types_TypeAlias_innerTypeAlias: Property = Property(name="innerTypeAlias", type=BooleanType)
gast_types_TypeAlias.attributes={gast_types_TypeAlias_innerTypeAlias}

# types_Member class attributes and methods

# types_TypeDecorator class attributes and methods

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
gast_types_GASTClass.attributes={gast_types_GASTClass_anonymous, gast_types_GASTClass_local, gast_types_GASTClass_primitive, gast_types_GASTClass_interface, gast_types_GASTClass_inner, gast_types_GASTClass_linesOfComments}

# types_GASTType class attributes and methods

# Constructor class attributes and methods

# Destructor class attributes and methods

# Field class attributes and methods

# Method class attributes and methods

# Property class attributes and methods

# gast_accesses_ParameterInstantiationTypeAccess class attributes and methods

# TypeAccess class attributes and methods

# InheritanceTypeAccess class attributes and methods

# CompositeAccess class attributes and methods

# gast_accesses_TypeAccess class attributes and methods

# gast_accesses_DeclarationTypeAccess class attributes and methods

# gast_accesses_CastTypeAccess class attributes and methods

# gast_accesses_CompositeAccess class attributes and methods

# gast_accesses_BaseAccess class attributes and methods

# gast_accesses_DelegateAccess class attributes and methods

# FunctionAccess class attributes and methods

# gast_accesses_FunctionAccess class attributes and methods

# Variable class attributes and methods

# gast_accesses_ThrowTypeAccess class attributes and methods
gast_accesses_ThrowTypeAccess_declared: Property = Property(name="declared", type=BooleanType)
gast_accesses_ThrowTypeAccess.attributes={gast_accesses_ThrowTypeAccess_declared}

# gast_accesses_InheritanceTypeAccess class attributes and methods
gast_accesses_InheritanceTypeAccess_implementationInheritance: Property = Property(name="implementationInheritance", type=BooleanType)
gast_accesses_InheritanceTypeAccess.attributes={gast_accesses_InheritanceTypeAccess_implementationInheritance}

# gast_accesses_VariableAccess class attributes and methods
gast_accesses_VariableAccess_write: Property = Property(name="write", type=BooleanType)
gast_accesses_VariableAccess.attributes={gast_accesses_VariableAccess_write}

# gast_accesses_RunTimeTypeAccess class attributes and methods

# gast_accesses_SelfAccess class attributes and methods
gast_accesses_SelfAccess_super: Property = Property(name="super", type=BooleanType)
gast_accesses_SelfAccess.attributes={gast_accesses_SelfAccess_super}

# VariableAccess class attributes and methods

# gast_functions_Delegate class attributes and methods
gast_functions_Delegate_innerDelegate: Property = Property(name="innerDelegate", type=BooleanType)
gast_functions_Delegate.attributes={gast_functions_Delegate_innerDelegate}

# functions_Function class attributes and methods

# gast_accesses_StaticTypeAccess class attributes and methods

# gast_accesses_PropertyAccess class attributes and methods

# gast_accesses_Access class attributes and methods

# gast_functions_Constructor class attributes and methods
gast_functions_Constructor_initializer: Property = Property(name="initializer", type=BooleanType)
gast_functions_Constructor.attributes={gast_functions_Constructor_initializer}

# gast_functions_Destructor class attributes and methods

# gast_functions_Method class attributes and methods
gast_functions_Method_propertyMethod: Property = Property(name="propertyMethod", type=BooleanType)
gast_functions_Method.attributes={gast_functions_Method_propertyMethod}

# gast_functions_GenericFunction class attributes and methods

# functions_GlobalFunction class attributes and methods

# gast_functions_GlobalFunction class attributes and methods
gast_functions_GlobalFunction_kind: Property = Property(name="kind", type=StringType)
gast_functions_GlobalFunction.attributes={gast_functions_GlobalFunction_kind}

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
gast_functions_Function.attributes={gast_functions_Function_numberOfNodesInCFG, gast_functions_Function_operator, gast_functions_Function_numberOfStatements, gast_functions_Function_maximumNestingLevel, gast_functions_Function_linesOfComments, gast_functions_Function_numberOfEdgesInCFG, gast_functions_Function_linesOfCode}

# DeclarationTypeAccess class attributes and methods

# FormalParameter class attributes and methods

# gast_variables_CatchParameter class attributes and methods
gast_variables_CatchParameter_rethrown: Property = Property(name="rethrown", type=BooleanType)
gast_variables_CatchParameter.attributes={gast_variables_CatchParameter_rethrown}

# gast_variables_Field class attributes and methods
gast_variables_Field_propertyField: Property = Property(name="propertyField", type=BooleanType)
gast_variables_Field.attributes={gast_variables_Field_propertyField}

# variables_Variable class attributes and methods

# gast_variables_LocalVariable class attributes and methods

# gast_variables_FormalParameter class attributes and methods
gast_variables_FormalParameter_passedByReference: Property = Property(name="passedByReference", type=BooleanType)
gast_variables_FormalParameter.attributes={gast_variables_FormalParameter_passedByReference}

# gast_variables_Variable class attributes and methods
gast_variables_Variable_const: Property = Property(name="const", type=BooleanType)
gast_variables_Variable.attributes={gast_variables_Variable_const}

# gast_variables_Property class attributes and methods

# variables_Field class attributes and methods

# gast_variables_GlobalVariable class attributes and methods

# Relationships
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
conditionExpression25: BinaryAssociation = BinaryAssociation(
    name="conditionExpression25",
    ends={
        Property(name="GASTExpression", type=gast_statements_Branch, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_statements_Branch", type=GASTExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
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
catchParameter45: BinaryAssociation = BinaryAssociation(
    name="catchParameter45",
    ends={
        Property(name="CatchParameter", type=gast_statements_CatchBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_statements_CatchBlock", type=CatchParameter, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
breakConditionExpression34: BinaryAssociation = BinaryAssociation(
    name="breakConditionExpression34",
    ends={
        Property(name="GASTExpression35", type=gast_statements_LoopStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_statements_LoopStatement", type=GASTExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
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
expression48: BinaryAssociation = BinaryAssociation(
    name="expression48",
    ends={
        Property(name="GASTExpression49", type=gast_statements_SimpleStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_statements_SimpleStatement", type=GASTExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body42: BinaryAssociation = BinaryAssociation(
    name="body42",
    ends={
        Property(name="statements44", type=gast_statements_LoopStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="Statement43", type=Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
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
root53: BinaryAssociation = BinaryAssociation(
    name="root53",
    ends={
        Property(name="core", type=gast_core_BasePath, multiplicity=Multiplicity(1, 1)),
        Property(name="Root", type=Root, multiplicity=Multiplicity(1, 1))
    }
)
expression46: BinaryAssociation = BinaryAssociation(
    name="expression46",
    ends={
        Property(name="GASTExpression47", type=gast_statements_JumpStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_statements_JumpStatement", type=GASTExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
allLocalClasses57: BinaryAssociation = BinaryAssociation(
    name="allLocalClasses57",
    ends={
        Property(name="GASTClass", type=gast_core_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_Package", type=GASTClass, multiplicity=Multiplicity(0, 9999))
    }
)
allInnerClasses58: BinaryAssociation = BinaryAssociation(
    name="allInnerClasses58",
    ends={
        Property(name="GASTClass60", type=gast_core_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_Package59", type=GASTClass, multiplicity=Multiplicity(0, 9999))
    }
)
directories54: BinaryAssociation = BinaryAssociation(
    name="directories54",
    ends={
        Property(name="core55", type=gast_core_BasePath, multiplicity=Multiplicity(1, 1)),
        Property(name="Directory", type=Directory, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotations56: BinaryAssociation = BinaryAssociation(
    name="annotations56",
    ends={
        Property(name="ModelAnnotation", type=gast_core_ModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_ModelElement", type=ModelAnnotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
globalFunctions71: BinaryAssociation = BinaryAssociation(
    name="globalFunctions71",
    ends={
        Property(name="functions72", type=gast_core_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="GlobalFunction", type=GlobalFunction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
globalVariables73: BinaryAssociation = BinaryAssociation(
    name="globalVariables73",
    ends={
        Property(name="variables", type=gast_core_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="GlobalVariable", type=GlobalVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
root74: BinaryAssociation = BinaryAssociation(
    name="root74",
    ends={
        Property(name="core76", type=gast_core_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="Root75", type=Root, multiplicity=Multiplicity(0, 1))
    }
)
allNormalClasses61: BinaryAssociation = BinaryAssociation(
    name="allNormalClasses61",
    ends={
        Property(name="GASTClass63", type=gast_core_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_Package62", type=GASTClass, multiplicity=Multiplicity(0, 9999))
    }
)
allInterfaces64: BinaryAssociation = BinaryAssociation(
    name="allInterfaces64",
    ends={
        Property(name="GASTClass66", type=gast_core_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_Package65", type=GASTClass, multiplicity=Multiplicity(0, 9999))
    }
)
allAccesses67: BinaryAssociation = BinaryAssociation(
    name="allAccesses67",
    ends={
        Property(name="Access", type=gast_core_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_Package68", type=Access, multiplicity=Multiplicity(0, 9999))
    }
)
delegates69: BinaryAssociation = BinaryAssociation(
    name="delegates69",
    ends={
        Property(name="functions70", type=gast_core_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="Delegate", type=Delegate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
allAccessedPackages84: BinaryAssociation = BinaryAssociation(
    name="allAccessedPackages84",
    ends={
        Property(name="Package86", type=gast_core_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_Package85", type=Package, multiplicity=Multiplicity(0, 9999))
    }
)
typeAliases87: BinaryAssociation = BinaryAssociation(
    name="typeAliases87",
    ends={
        Property(name="types88", type=gast_core_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="TypeAlias", type=TypeAlias, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeParameters89: BinaryAssociation = BinaryAssociation(
    name="typeParameters89",
    ends={
        Property(name="TypeParameterClass", type=gast_core_GenericEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_GenericEntity", type=TypeParameterClass, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
allAccesses90: BinaryAssociation = BinaryAssociation(
    name="allAccesses90",
    ends={
        Property(name="Access91", type=gast_core_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_Root", type=Access, multiplicity=Multiplicity(0, 9999))
    }
)
allInnerClasses92: BinaryAssociation = BinaryAssociation(
    name="allInnerClasses92",
    ends={
        Property(name="GASTClass94", type=gast_core_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_Root93", type=GASTClass, multiplicity=Multiplicity(0, 9999))
    }
)
classes77: BinaryAssociation = BinaryAssociation(
    name="classes77",
    ends={
        Property(name="types", type=gast_core_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="GASTClass78", type=GASTClass, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subPackages79: BinaryAssociation = BinaryAssociation(
    name="subPackages79",
    ends={
        Property(name="core80", type=gast_core_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="Package", type=Package, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
surroundingPackage81: BinaryAssociation = BinaryAssociation(
    name="surroundingPackage81",
    ends={
        Property(name="core83", type=gast_core_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="Package82", type=Package, multiplicity=Multiplicity(0, 1))
    }
)
globalVariables106: BinaryAssociation = BinaryAssociation(
    name="globalVariables106",
    ends={
        Property(name="GlobalVariable108", type=gast_core_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_Root107", type=GlobalVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
packages109: BinaryAssociation = BinaryAssociation(
    name="packages109",
    ends={
        Property(name="core111", type=gast_core_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="Package110", type=Package, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
clones112: BinaryAssociation = BinaryAssociation(
    name="clones112",
    ends={
        Property(name="annotations113", type=gast_core_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="Clone", type=Clone, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
structuralAbstractions114: BinaryAssociation = BinaryAssociation(
    name="structuralAbstractions114",
    ends={
        Property(name="StructuralAbstraction", type=gast_core_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_Root115", type=StructuralAbstraction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
types116: BinaryAssociation = BinaryAssociation(
    name="types116",
    ends={
        Property(name="GASTType", type=gast_core_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_Root117", type=GASTType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
danglingModelElements118: BinaryAssociation = BinaryAssociation(
    name="danglingModelElements118",
    ends={
        Property(name="ModelElement120", type=gast_core_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_Root119", type=ModelElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
basePaths121: BinaryAssociation = BinaryAssociation(
    name="basePaths121",
    ends={
        Property(name="core122", type=gast_core_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="BasePath", type=BasePath, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
allInterfaces95: BinaryAssociation = BinaryAssociation(
    name="allInterfaces95",
    ends={
        Property(name="GASTClass97", type=gast_core_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_Root96", type=GASTClass, multiplicity=Multiplicity(0, 9999))
    }
)
allLocalClasses98: BinaryAssociation = BinaryAssociation(
    name="allLocalClasses98",
    ends={
        Property(name="GASTClass100", type=gast_core_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_Root99", type=GASTClass, multiplicity=Multiplicity(0, 9999))
    }
)
allNormalClasses101: BinaryAssociation = BinaryAssociation(
    name="allNormalClasses101",
    ends={
        Property(name="GASTClass103", type=gast_core_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_Root102", type=GASTClass, multiplicity=Multiplicity(0, 9999))
    }
)
allModelElements104: BinaryAssociation = BinaryAssociation(
    name="allModelElements104",
    ends={
        Property(name="ModelElement", type=gast_core_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_Root105", type=ModelElement, multiplicity=Multiplicity(0, 9999))
    }
)
subDirectory126: BinaryAssociation = BinaryAssociation(
    name="subDirectory126",
    ends={
        Property(name="core128", type=gast_core_Directory, multiplicity=Multiplicity(1, 1)),
        Property(name="Directory127", type=Directory, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentDirectory129: BinaryAssociation = BinaryAssociation(
    name="parentDirectory129",
    ends={
        Property(name="core131", type=gast_core_Directory, multiplicity=Multiplicity(1, 1)),
        Property(name="Directory130", type=Directory, multiplicity=Multiplicity(0, 1))
    }
)
files132: BinaryAssociation = BinaryAssociation(
    name="files132",
    ends={
        Property(name="core133", type=gast_core_Directory, multiplicity=Multiplicity(1, 1)),
        Property(name="File", type=File, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
basePath134: BinaryAssociation = BinaryAssociation(
    name="basePath134",
    ends={
        Property(name="core136", type=gast_core_Directory, multiplicity=Multiplicity(1, 1)),
        Property(name="BasePath135", type=BasePath, multiplicity=Multiplicity(0, 1))
    }
)
root137: BinaryAssociation = BinaryAssociation(
    name="root137",
    ends={
        Property(name="Root138", type=gast_core_File, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_File", type=Root, multiplicity=Multiplicity(1, 1))
    }
)
globalFunctions123: BinaryAssociation = BinaryAssociation(
    name="globalFunctions123",
    ends={
        Property(name="functions125", type=gast_core_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="GlobalFunction124", type=GlobalFunction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
importedGlobalFunctions151: BinaryAssociation = BinaryAssociation(
    name="importedGlobalFunctions151",
    ends={
        Property(name="GlobalFunction153", type=gast_core_File, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_File152", type=GlobalFunction, multiplicity=Multiplicity(0, 9999))
    }
)
importedGlobalVariables154: BinaryAssociation = BinaryAssociation(
    name="importedGlobalVariables154",
    ends={
        Property(name="GlobalVariable156", type=gast_core_File, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_File155", type=GlobalVariable, multiplicity=Multiplicity(0, 9999))
    }
)
importedPackages157: BinaryAssociation = BinaryAssociation(
    name="importedPackages157",
    ends={
        Property(name="Package159", type=gast_core_File, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_File158", type=Package, multiplicity=Multiplicity(0, 9999))
    }
)
includedFiles160: BinaryAssociation = BinaryAssociation(
    name="includedFiles160",
    ends={
        Property(name="File162", type=gast_core_File, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_File161", type=File, multiplicity=Multiplicity(0, 9999))
    }
)
importedTypes139: BinaryAssociation = BinaryAssociation(
    name="importedTypes139",
    ends={
        Property(name="GASTType141", type=gast_core_File, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_File140", type=GASTType, multiplicity=Multiplicity(0, 9999))
    }
)
types142: BinaryAssociation = BinaryAssociation(
    name="types142",
    ends={
        Property(name="GASTType144", type=gast_core_File, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_File143", type=GASTType, multiplicity=Multiplicity(0, 9999))
    }
)
globalVariables145: BinaryAssociation = BinaryAssociation(
    name="globalVariables145",
    ends={
        Property(name="GlobalVariable147", type=gast_core_File, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_File146", type=GlobalVariable, multiplicity=Multiplicity(0, 9999))
    }
)
globalFunctions148: BinaryAssociation = BinaryAssociation(
    name="globalFunctions148",
    ends={
        Property(name="GlobalFunction150", type=gast_core_File, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_File149", type=GlobalFunction, multiplicity=Multiplicity(0, 9999))
    }
)
sourceFile166: BinaryAssociation = BinaryAssociation(
    name="sourceFile166",
    ends={
        Property(name="File167", type=gast_core_Position, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_Position", type=File, multiplicity=Multiplicity(0, 1))
    }
)
assembly168: BinaryAssociation = BinaryAssociation(
    name="assembly168",
    ends={
        Property(name="File170", type=gast_core_Position, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_Position169", type=File, multiplicity=Multiplicity(0, 1))
    }
)
sourceentity171: BinaryAssociation = BinaryAssociation(
    name="sourceentity171",
    ends={
        Property(name="core172", type=gast_core_Position, multiplicity=Multiplicity(1, 1)),
        Property(name="SourceEntity", type=SourceEntity, multiplicity=Multiplicity(1, 1))
    }
)
aliasedPackage173: BinaryAssociation = BinaryAssociation(
    name="aliasedPackage173",
    ends={
        Property(name="Package174", type=gast_core_PackageAlias, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_PackageAlias", type=Package, multiplicity=Multiplicity(1, 1))
    }
)
position175: BinaryAssociation = BinaryAssociation(
    name="position175",
    ends={
        Property(name="core176", type=gast_core_SourceEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="Position", type=Position, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
directory163: BinaryAssociation = BinaryAssociation(
    name="directory163",
    ends={
        Property(name="core165", type=gast_core_File, multiplicity=Multiplicity(1, 1)),
        Property(name="Directory164", type=Directory, multiplicity=Multiplicity(1, 1))
    }
)
statements183: BinaryAssociation = BinaryAssociation(
    name="statements183",
    ends={
        Property(name="statements185", type=gast_annotations_CloneInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="Statement184", type=Statement, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
clone186: BinaryAssociation = BinaryAssociation(
    name="clone186",
    ends={
        Property(name="annotations188", type=gast_annotations_CloneInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="Clone187", type=Clone, multiplicity=Multiplicity(1, 1))
    }
)
cloneInstances177: BinaryAssociation = BinaryAssociation(
    name="cloneInstances177",
    ends={
        Property(name="annotations179", type=gast_annotations_Clone, multiplicity=Multiplicity(1, 1)),
        Property(name="CloneInstance178", type=CloneInstance, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
root180: BinaryAssociation = BinaryAssociation(
    name="root180",
    ends={
        Property(name="core182", type=gast_annotations_Clone, multiplicity=Multiplicity(1, 1)),
        Property(name="Root181", type=Root, multiplicity=Multiplicity(1, 1))
    }
)
decoratedType191: BinaryAssociation = BinaryAssociation(
    name="decoratedType191",
    ends={
        Property(name="GASTType192", type=gast_types_TypeDecorator, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_types_TypeDecorator", type=GASTType, multiplicity=Multiplicity(1, 1))
    }
)
undecoratedType193: BinaryAssociation = BinaryAssociation(
    name="undecoratedType193",
    ends={
        Property(name="GASTType195", type=gast_types_TypeDecorator, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_types_TypeDecorator194", type=GASTType, multiplicity=Multiplicity(1, 1))
    }
)
referencedType189: BinaryAssociation = BinaryAssociation(
    name="referencedType189",
    ends={
        Property(name="GASTType190", type=gast_types_Reference, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_types_Reference", type=GASTType, multiplicity=Multiplicity(1, 1))
    }
)
surroundingClass200: BinaryAssociation = BinaryAssociation(
    name="surroundingClass200",
    ends={
        Property(name="types202", type=gast_types_TypeAlias, multiplicity=Multiplicity(1, 1)),
        Property(name="GASTClass201", type=GASTClass, multiplicity=Multiplicity(0, 1))
    }
)
surroundingPackage203: BinaryAssociation = BinaryAssociation(
    name="surroundingPackage203",
    ends={
        Property(name="core205", type=gast_types_TypeAlias, multiplicity=Multiplicity(1, 1)),
        Property(name="Package204", type=Package, multiplicity=Multiplicity(0, 1))
    }
)
overriddenMember206: BinaryAssociation = BinaryAssociation(
    name="overriddenMember206",
    ends={
        Property(name="Member", type=gast_types_Member, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_types_Member", type=Member, multiplicity=Multiplicity(0, 1))
    }
)
baseType196: BinaryAssociation = BinaryAssociation(
    name="baseType196",
    ends={
        Property(name="GASTType197", type=gast_types_GASTArray, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_types_GASTArray", type=GASTType, multiplicity=Multiplicity(1, 1))
    }
)
aliasedType198: BinaryAssociation = BinaryAssociation(
    name="aliasedType198",
    ends={
        Property(name="GASTType199", type=gast_types_TypeAlias, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_types_TypeAlias", type=GASTType, multiplicity=Multiplicity(1, 1))
    }
)
typeBounds207: BinaryAssociation = BinaryAssociation(
    name="typeBounds207",
    ends={
        Property(name="GASTType208", type=gast_types_TypeParameterClass, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_types_TypeParameterClass", type=GASTType, multiplicity=Multiplicity(0, 9999))
    }
)
innerTypeAliases209: BinaryAssociation = BinaryAssociation(
    name="innerTypeAliases209",
    ends={
        Property(name="types211", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="TypeAlias210", type=TypeAlias, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
surroundingFunction223: BinaryAssociation = BinaryAssociation(
    name="surroundingFunction223",
    ends={
        Property(name="functions225", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="Function224", type=Function, multiplicity=Multiplicity(0, 1))
    }
)
surroundingPackage226: BinaryAssociation = BinaryAssociation(
    name="surroundingPackage226",
    ends={
        Property(name="core228", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="Package227", type=Package, multiplicity=Multiplicity(0, 1))
    }
)
superTypes229: BinaryAssociation = BinaryAssociation(
    name="superTypes229",
    ends={
        Property(name="GASTClass230", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_types_GASTClass", type=GASTClass, multiplicity=Multiplicity(0, 9999))
    }
)
innerClasses231: BinaryAssociation = BinaryAssociation(
    name="innerClasses231",
    ends={
        Property(name="types233", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="GASTClass232", type=GASTClass, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
innerDelegates212: BinaryAssociation = BinaryAssociation(
    name="innerDelegates212",
    ends={
        Property(name="functions214", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="Delegate213", type=Delegate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
constructors215: BinaryAssociation = BinaryAssociation(
    name="constructors215",
    ends={
        Property(name="functions216", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="Constructor", type=Constructor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
destructors217: BinaryAssociation = BinaryAssociation(
    name="destructors217",
    ends={
        Property(name="functions218", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="Destructor", type=Destructor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fields219: BinaryAssociation = BinaryAssociation(
    name="fields219",
    ends={
        Property(name="variables220", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="Field", type=Field, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
methods221: BinaryAssociation = BinaryAssociation(
    name="methods221",
    ends={
        Property(name="functions222", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="Method", type=Method_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
friendFunctions248: BinaryAssociation = BinaryAssociation(
    name="friendFunctions248",
    ends={
        Property(name="Function250", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_types_GASTClass249", type=Function, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
property251: BinaryAssociation = BinaryAssociation(
    name="property251",
    ends={
        Property(name="Property", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_types_GASTClass252", type=Property_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
allAccesses253: BinaryAssociation = BinaryAssociation(
    name="allAccesses253",
    ends={
        Property(name="Access255", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_types_GASTClass254", type=Access, multiplicity=Multiplicity(0, 9999))
    }
)
allAccessedClasses256: BinaryAssociation = BinaryAssociation(
    name="allAccessedClasses256",
    ends={
        Property(name="GASTClass258", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_types_GASTClass257", type=GASTClass, multiplicity=Multiplicity(0, 9999))
    }
)
surroundingClass234: BinaryAssociation = BinaryAssociation(
    name="surroundingClass234",
    ends={
        Property(name="types236", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="GASTClass235", type=GASTClass, multiplicity=Multiplicity(0, 1))
    }
)
inheritanceTypeAccesses237: BinaryAssociation = BinaryAssociation(
    name="inheritanceTypeAccesses237",
    ends={
        Property(name="InheritanceTypeAccess", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_types_GASTClass238", type=InheritanceTypeAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
self239: BinaryAssociation = BinaryAssociation(
    name="self239",
    ends={
        Property(name="Field241", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_types_GASTClass240", type=Field, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
friendClasses242: BinaryAssociation = BinaryAssociation(
    name="friendClasses242",
    ends={
        Property(name="types244", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="GASTClass243", type=GASTClass, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
surroundingStatement270: BinaryAssociation = BinaryAssociation(
    name="surroundingStatement270",
    ends={
        Property(name="Statement271", type=gast_accesses_BaseAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_accesses_BaseAccess", type=Statement, multiplicity=Multiplicity(0, 1))
    }
)
gastClass245: BinaryAssociation = BinaryAssociation(
    name="gastClass245",
    ends={
        Property(name="types247", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="GASTClass246", type=GASTClass, multiplicity=Multiplicity(0, 1))
    }
)
surroundingClass272: BinaryAssociation = BinaryAssociation(
    name="surroundingClass272",
    ends={
        Property(name="GASTClass274", type=gast_accesses_BaseAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_accesses_BaseAccess273", type=GASTClass, multiplicity=Multiplicity(1, 1))
    }
)
surroundingFunction275: BinaryAssociation = BinaryAssociation(
    name="surroundingFunction275",
    ends={
        Property(name="Function277", type=gast_accesses_BaseAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_accesses_BaseAccess276", type=Function, multiplicity=Multiplicity(0, 1))
    }
)
surroundingCompositeAccess278: BinaryAssociation = BinaryAssociation(
    name="surroundingCompositeAccess278",
    ends={
        Property(name="accesses279", type=gast_accesses_BaseAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="CompositeAccess", type=CompositeAccess, multiplicity=Multiplicity(0, 1))
    }
)
targetType259: BinaryAssociation = BinaryAssociation(
    name="targetType259",
    ends={
        Property(name="GASTType260", type=gast_accesses_TypeAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_accesses_TypeAccess", type=GASTType, multiplicity=Multiplicity(1, 1))
    }
)
typeArguments261: BinaryAssociation = BinaryAssociation(
    name="typeArguments261",
    ends={
        Property(name="GASTType263", type=gast_accesses_TypeAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_accesses_TypeAccess262", type=GASTType, multiplicity=Multiplicity(0, 9999))
    }
)
accesses264: BinaryAssociation = BinaryAssociation(
    name="accesses264",
    ends={
        Property(name="accesses266", type=gast_accesses_CompositeAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="BaseAccess265", type=BaseAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentStatement267: BinaryAssociation = BinaryAssociation(
    name="parentStatement267",
    ends={
        Property(name="statements269", type=gast_accesses_BaseAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="Statement268", type=Statement, multiplicity=Multiplicity(0, 1))
    }
)
accessedFunctions285: BinaryAssociation = BinaryAssociation(
    name="accessedFunctions285",
    ends={
        Property(name="Function286", type=gast_accesses_DelegateAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_accesses_DelegateAccess", type=Function, multiplicity=Multiplicity(0, 9999))
    }
)
accessedDelegate287: BinaryAssociation = BinaryAssociation(
    name="accessedDelegate287",
    ends={
        Property(name="Delegate289", type=gast_accesses_DelegateAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_accesses_DelegateAccess288", type=Delegate, multiplicity=Multiplicity(1, 1))
    }
)
typeArguments290: BinaryAssociation = BinaryAssociation(
    name="typeArguments290",
    ends={
        Property(name="GASTType291", type=gast_accesses_FunctionAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_accesses_FunctionAccess", type=GASTType, multiplicity=Multiplicity(0, 9999))
    }
)
function280: BinaryAssociation = BinaryAssociation(
    name="function280",
    ends={
        Property(name="functions282", type=gast_accesses_DeclarationTypeAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="Function281", type=Function, multiplicity=Multiplicity(0, 1))
    }
)
surroundingVariable283: BinaryAssociation = BinaryAssociation(
    name="surroundingVariable283",
    ends={
        Property(name="variables284", type=gast_accesses_DeclarationTypeAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="Variable", type=Variable, multiplicity=Multiplicity(0, 1))
    }
)
targetVariable295: BinaryAssociation = BinaryAssociation(
    name="targetVariable295",
    ends={
        Property(name="Variable296", type=gast_accesses_VariableAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_accesses_VariableAccess", type=Variable, multiplicity=Multiplicity(1, 1))
    }
)
targetFunction292: BinaryAssociation = BinaryAssociation(
    name="targetFunction292",
    ends={
        Property(name="Function294", type=gast_accesses_FunctionAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_accesses_FunctionAccess293", type=Function, multiplicity=Multiplicity(1, 1))
    }
)
accessedTarget299: BinaryAssociation = BinaryAssociation(
    name="accessedTarget299",
    ends={
        Property(name="ModelElement301", type=gast_accesses_Access, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_accesses_Access300", type=ModelElement, multiplicity=Multiplicity(1, 1))
    }
)
accessedClass297: BinaryAssociation = BinaryAssociation(
    name="accessedClass297",
    ends={
        Property(name="GASTClass298", type=gast_accesses_Access, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_accesses_Access", type=GASTClass, multiplicity=Multiplicity(1, 1))
    }
)
surroundingPackage310: BinaryAssociation = BinaryAssociation(
    name="surroundingPackage310",
    ends={
        Property(name="core312", type=gast_functions_Delegate, multiplicity=Multiplicity(1, 1)),
        Property(name="Package311", type=Package, multiplicity=Multiplicity(0, 1))
    }
)
surroundingClass313: BinaryAssociation = BinaryAssociation(
    name="surroundingClass313",
    ends={
        Property(name="types315", type=gast_functions_Constructor, multiplicity=Multiplicity(1, 1)),
        Property(name="GASTClass314", type=GASTClass, multiplicity=Multiplicity(1, 1))
    }
)
surroundingClass316: BinaryAssociation = BinaryAssociation(
    name="surroundingClass316",
    ends={
        Property(name="types318", type=gast_functions_Destructor, multiplicity=Multiplicity(1, 1)),
        Property(name="GASTClass317", type=GASTClass, multiplicity=Multiplicity(1, 1))
    }
)
superClass302: BinaryAssociation = BinaryAssociation(
    name="superClass302",
    ends={
        Property(name="GASTClass303", type=gast_functions_Delegate, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_functions_Delegate", type=GASTClass, multiplicity=Multiplicity(0, 1))
    }
)
invocations304: BinaryAssociation = BinaryAssociation(
    name="invocations304",
    ends={
        Property(name="Function306", type=gast_functions_Delegate, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_functions_Delegate305", type=Function, multiplicity=Multiplicity(0, 9999))
    }
)
root322: BinaryAssociation = BinaryAssociation(
    name="root322",
    ends={
        Property(name="core324", type=gast_functions_GlobalFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="Root323", type=Root, multiplicity=Multiplicity(0, 1))
    }
)
surroundingClass307: BinaryAssociation = BinaryAssociation(
    name="surroundingClass307",
    ends={
        Property(name="types309", type=gast_functions_Delegate, multiplicity=Multiplicity(1, 1)),
        Property(name="GASTClass308", type=GASTClass, multiplicity=Multiplicity(0, 1))
    }
)
surroundingProperty325: BinaryAssociation = BinaryAssociation(
    name="surroundingProperty325",
    ends={
        Property(name="Property326", type=gast_functions_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_functions_Method", type=Property_, multiplicity=Multiplicity(0, 1))
    }
)
surroundingPackage319: BinaryAssociation = BinaryAssociation(
    name="surroundingPackage319",
    ends={
        Property(name="core321", type=gast_functions_GlobalFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="Package320", type=Package, multiplicity=Multiplicity(0, 1))
    }
)
localVariables334: BinaryAssociation = BinaryAssociation(
    name="localVariables334",
    ends={
        Property(name="variables335", type=gast_functions_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="LocalVariable", type=LocalVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
allStatements336: BinaryAssociation = BinaryAssociation(
    name="allStatements336",
    ends={
        Property(name="Statement337", type=gast_functions_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_functions_Function", type=Statement, multiplicity=Multiplicity(0, 9999))
    }
)
throwTypeAccesses338: BinaryAssociation = BinaryAssociation(
    name="throwTypeAccesses338",
    ends={
        Property(name="ThrowTypeAccess", type=gast_functions_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_functions_Function339", type=ThrowTypeAccess, multiplicity=Multiplicity(0, 9999))
    }
)
accesses340: BinaryAssociation = BinaryAssociation(
    name="accesses340",
    ends={
        Property(name="Access342", type=gast_functions_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_functions_Function341", type=Access, multiplicity=Multiplicity(0, 9999))
    }
)
surroundingClass327: BinaryAssociation = BinaryAssociation(
    name="surroundingClass327",
    ends={
        Property(name="types329", type=gast_functions_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="GASTClass328", type=GASTClass, multiplicity=Multiplicity(1, 1))
    }
)
returnTypeDeclaration330: BinaryAssociation = BinaryAssociation(
    name="returnTypeDeclaration330",
    ends={
        Property(name="accesses331", type=gast_functions_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="DeclarationTypeAccess", type=DeclarationTypeAccess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
formalParameters332: BinaryAssociation = BinaryAssociation(
    name="formalParameters332",
    ends={
        Property(name="variables333", type=gast_functions_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="FormalParameter", type=FormalParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type352: BinaryAssociation = BinaryAssociation(
    name="type352",
    ends={
        Property(name="GASTType353", type=gast_variables_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_variables_Variable", type=GASTType, multiplicity=Multiplicity(1, 1))
    }
)
typeDeclaration354: BinaryAssociation = BinaryAssociation(
    name="typeDeclaration354",
    ends={
        Property(name="accesses356", type=gast_variables_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="DeclarationTypeAccess355", type=DeclarationTypeAccess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
surroundingClass357: BinaryAssociation = BinaryAssociation(
    name="surroundingClass357",
    ends={
        Property(name="types359", type=gast_variables_Field, multiplicity=Multiplicity(1, 1)),
        Property(name="GASTClass358", type=GASTClass, multiplicity=Multiplicity(0, 1))
    }
)
surroundingFunction360: BinaryAssociation = BinaryAssociation(
    name="surroundingFunction360",
    ends={
        Property(name="functions362", type=gast_variables_LocalVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="Function361", type=Function, multiplicity=Multiplicity(1, 1))
    }
)
body343: BinaryAssociation = BinaryAssociation(
    name="body343",
    ends={
        Property(name="statements345", type=gast_functions_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="BlockStatement344", type=BlockStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
localClasses346: BinaryAssociation = BinaryAssociation(
    name="localClasses346",
    ends={
        Property(name="types348", type=gast_functions_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="GASTClass347", type=GASTClass, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
surroundingFunction349: BinaryAssociation = BinaryAssociation(
    name="surroundingFunction349",
    ends={
        Property(name="functions351", type=gast_variables_FormalParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="Function350", type=Function, multiplicity=Multiplicity(1, 1))
    }
)
setter363: BinaryAssociation = BinaryAssociation(
    name="setter363",
    ends={
        Property(name="Method364", type=gast_variables_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_variables_Property", type=Method_, multiplicity=Multiplicity(0, 1))
    }
)
getter365: BinaryAssociation = BinaryAssociation(
    name="getter365",
    ends={
        Property(name="Method367", type=gast_variables_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_variables_Property366", type=Method_, multiplicity=Multiplicity(0, 1))
    }
)
surroundingPackage368: BinaryAssociation = BinaryAssociation(
    name="surroundingPackage368",
    ends={
        Property(name="core370", type=gast_variables_GlobalVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="Package369", type=Package, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_gast_statements_ExceptionHandler_Statement = Generalization(general=Statement, specific=gast_statements_ExceptionHandler)
gen_gast_statements_Statement_SourceEntity = Generalization(general=SourceEntity, specific=gast_statements_Statement)
gen_gast_statements_Branch_SourceEntity = Generalization(general=SourceEntity, specific=gast_statements_Branch)
gen_gast_statements_GASTExpression_SourceEntity = Generalization(general=SourceEntity, specific=gast_statements_GASTExpression)
gen_gast_statements_BranchStatement_Statement = Generalization(general=Statement, specific=gast_statements_BranchStatement)
gen_gast_statements_BlockStatement_Statement = Generalization(general=Statement, specific=gast_statements_BlockStatement)
gen_gast_statements_CatchBlock_BlockStatement = Generalization(general=BlockStatement, specific=gast_statements_CatchBlock)
gen_gast_statements_LoopStatement_Statement = Generalization(general=Statement, specific=gast_statements_LoopStatement)
gen_gast_statements_Methods_BlockStatement = Generalization(general=BlockStatement, specific=gast_statements_Methods)
gen_gast_core_BasePath_ModelElement = Generalization(general=ModelElement, specific=gast_core_BasePath)
gen_gast_statements_JumpStatement_Statement = Generalization(general=Statement, specific=gast_statements_JumpStatement)
gen_gast_statements_SimpleStatement_Statement = Generalization(general=Statement, specific=gast_statements_SimpleStatement)
gen_gast_core_NamedModelElement_ModelElement = Generalization(general=ModelElement, specific=gast_core_NamedModelElement)
gen_gast_core_Package_NamedModelElement = Generalization(general=NamedModelElement, specific=gast_core_Package)
gen_gast_core_ModelElement_Identifier = Generalization(general=Identifier, specific=gast_core_ModelElement)
gen_gast_core_GenericEntity_ModelElement = Generalization(general=ModelElement, specific=gast_core_GenericEntity)
gen_gast_core_Root_ModelElement = Generalization(general=ModelElement, specific=gast_core_Root)
gen_gast_core_File_NamedModelElement = Generalization(general=NamedModelElement, specific=gast_core_File)
gen_gast_core_Directory_NamedModelElement = Generalization(general=NamedModelElement, specific=gast_core_Directory)
gen_gast_core_PackageAlias_Package = Generalization(general=Package, specific=gast_core_PackageAlias)
gen_gast_core_SourceEntity_ModelElement = Generalization(general=ModelElement, specific=gast_core_SourceEntity)
gen_gast_annotations_StructuralAbstraction_core_NamedModelElement = Generalization(general=core_NamedModelElement, specific=gast_annotations_StructuralAbstraction)
gen_gast_annotations_StructuralAbstraction_annotations_ModelAnnotation = Generalization(general=annotations_ModelAnnotation, specific=gast_annotations_StructuralAbstraction)
gen_gast_annotations_Comment_core_SourceEntity = Generalization(general=core_SourceEntity, specific=gast_annotations_Comment)
gen_gast_annotations_Comment_annotations_ModelAnnotation = Generalization(general=annotations_ModelAnnotation, specific=gast_annotations_Comment)
gen_gast_annotations_Attribute_types_GASTClass = Generalization(general=types_GASTClass, specific=gast_annotations_Attribute)
gen_gast_annotations_Attribute_annotations_ModelAnnotation = Generalization(general=annotations_ModelAnnotation, specific=gast_annotations_Attribute)
gen_gast_annotations_Clone_core_ModelElement = Generalization(general=core_ModelElement, specific=gast_annotations_Clone)
gen_gast_annotations_Clone_annotations_ModelAnnotation = Generalization(general=annotations_ModelAnnotation, specific=gast_annotations_Clone)
gen_gast_annotations_CloneInstance_core_ModelElement = Generalization(general=core_ModelElement, specific=gast_annotations_CloneInstance)
gen_gast_annotations_CloneInstance_annotations_ModelAnnotation = Generalization(general=annotations_ModelAnnotation, specific=gast_annotations_CloneInstance)
gen_gast_types_TypeDecorator_GASTType = Generalization(general=GASTType, specific=gast_types_TypeDecorator)
gen_gast_types_GASTType_NamedModelElement = Generalization(general=NamedModelElement, specific=gast_types_GASTType)
gen_gast_types_GASTArray_TypeDecorator = Generalization(general=TypeDecorator, specific=gast_types_GASTArray)
gen_gast_annotations_Subsystem_StructuralAbstraction = Generalization(general=StructuralAbstraction, specific=gast_annotations_Subsystem)
gen_gast_annotations_Layer_StructuralAbstraction = Generalization(general=StructuralAbstraction, specific=gast_annotations_Layer)
gen_gast_types_Reference_TypeDecorator = Generalization(general=TypeDecorator, specific=gast_types_Reference)
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
gen_gast_accesses_DeclarationTypeAccess_TypeAccess = Generalization(general=TypeAccess, specific=gast_accesses_DeclarationTypeAccess)
gen_gast_accesses_CastTypeAccess_TypeAccess = Generalization(general=TypeAccess, specific=gast_accesses_CastTypeAccess)
gen_gast_accesses_CompositeAccess_BaseAccess = Generalization(general=BaseAccess, specific=gast_accesses_CompositeAccess)
gen_gast_accesses_BaseAccess_SourceEntity = Generalization(general=SourceEntity, specific=gast_accesses_BaseAccess)
gen_gast_accesses_DelegateAccess_FunctionAccess = Generalization(general=FunctionAccess, specific=gast_accesses_DelegateAccess)
gen_gast_accesses_FunctionAccess_Access = Generalization(general=Access, specific=gast_accesses_FunctionAccess)
gen_gast_accesses_ThrowTypeAccess_TypeAccess = Generalization(general=TypeAccess, specific=gast_accesses_ThrowTypeAccess)
gen_gast_accesses_InheritanceTypeAccess_TypeAccess = Generalization(general=TypeAccess, specific=gast_accesses_InheritanceTypeAccess)
gen_gast_accesses_VariableAccess_Access = Generalization(general=Access, specific=gast_accesses_VariableAccess)
gen_gast_accesses_RunTimeTypeAccess_TypeAccess = Generalization(general=TypeAccess, specific=gast_accesses_RunTimeTypeAccess)
gen_gast_accesses_SelfAccess_VariableAccess = Generalization(general=VariableAccess, specific=gast_accesses_SelfAccess)
gen_gast_functions_Delegate_functions_Function = Generalization(general=functions_Function, specific=gast_functions_Delegate)
gen_gast_functions_Delegate_types_Member = Generalization(general=types_Member, specific=gast_functions_Delegate)
gen_gast_functions_Delegate_types_GASTType = Generalization(general=types_GASTType, specific=gast_functions_Delegate)
gen_gast_accesses_StaticTypeAccess_TypeAccess = Generalization(general=TypeAccess, specific=gast_accesses_StaticTypeAccess)
gen_gast_accesses_PropertyAccess_VariableAccess = Generalization(general=VariableAccess, specific=gast_accesses_PropertyAccess)
gen_gast_accesses_Access_BaseAccess = Generalization(general=BaseAccess, specific=gast_accesses_Access)
gen_gast_functions_Constructor_functions_Function = Generalization(general=functions_Function, specific=gast_functions_Constructor)
gen_gast_functions_Constructor_types_Member = Generalization(general=types_Member, specific=gast_functions_Constructor)
gen_gast_functions_Destructor_functions_Function = Generalization(general=functions_Function, specific=gast_functions_Destructor)
gen_gast_functions_Destructor_types_Member = Generalization(general=types_Member, specific=gast_functions_Destructor)
gen_gast_functions_Method_functions_Function = Generalization(general=functions_Function, specific=gast_functions_Method)
gen_gast_functions_Method_types_Member = Generalization(general=types_Member, specific=gast_functions_Method)
gen_gast_functions_GenericFunction_functions_GlobalFunction = Generalization(general=functions_GlobalFunction, specific=gast_functions_GenericFunction)
gen_gast_functions_GenericFunction_core_GenericEntity = Generalization(general=core_GenericEntity, specific=gast_functions_GenericFunction)
gen_gast_functions_GlobalFunction_Function = Generalization(general=Function, specific=gast_functions_GlobalFunction)
gen_gast_functions_GenericMethod_functions_Method = Generalization(general=functions_Method, specific=gast_functions_GenericMethod)
gen_gast_functions_GenericMethod_core_GenericEntity = Generalization(general=core_GenericEntity, specific=gast_functions_GenericMethod)
gen_gast_functions_GenericConstructor_functions_Constructor = Generalization(general=functions_Constructor, specific=gast_functions_GenericConstructor)
gen_gast_functions_GenericConstructor_core_GenericEntity = Generalization(general=core_GenericEntity, specific=gast_functions_GenericConstructor)
gen_gast_functions_Function_core_NamedModelElement = Generalization(general=core_NamedModelElement, specific=gast_functions_Function)
gen_gast_functions_Function_core_SourceEntity = Generalization(general=core_SourceEntity, specific=gast_functions_Function)
gen_gast_variables_CatchParameter_Variable = Generalization(general=Variable, specific=gast_variables_CatchParameter)
gen_gast_variables_Field_types_Member = Generalization(general=types_Member, specific=gast_variables_Field)
gen_gast_variables_Field_variables_Variable = Generalization(general=variables_Variable, specific=gast_variables_Field)
gen_gast_variables_LocalVariable_Variable = Generalization(general=Variable, specific=gast_variables_LocalVariable)
gen_gast_variables_FormalParameter_Variable = Generalization(general=Variable, specific=gast_variables_FormalParameter)
gen_gast_variables_Variable_core_NamedModelElement = Generalization(general=core_NamedModelElement, specific=gast_variables_Variable)
gen_gast_variables_Variable_core_SourceEntity = Generalization(general=core_SourceEntity, specific=gast_variables_Variable)
gen_gast_variables_Property_variables_Field = Generalization(general=variables_Field, specific=gast_variables_Property)
gen_gast_variables_Property_types_Member = Generalization(general=types_Member, specific=gast_variables_Property)
gen_gast_variables_GlobalVariable_Variable = Generalization(general=Variable, specific=gast_variables_GlobalVariable)

# Domain Model
domain_model = DomainModel(
    name="gast",
    types={gast_statements_ExceptionHandler, Statement, CatchBlock, BlockStatement, gast_statements_Statement, SourceEntity, BaseAccess, CloneInstance, Function, gast_statements_Branch, GASTExpression, BranchStatement, gast_statements_GASTExpression, gast_statements_BranchStatement, Branch, LoopStatement, gast_statements_BlockStatement, gast_statements_CatchBlock, CatchParameter, gast_statements_LoopStatement, gast_statements_GASTBehaviour, gast_statements_Methods, Exit, gast_statements_Exit, gast_core_BasePath, ModelElement, Root, gast_statements_JumpStatement, gast_statements_SimpleStatement, gast_core_NamedModelElement, gast_core_Package, NamedModelElement, GASTClass, Directory, gast_core_ModelElement, Identifier, ModelAnnotation, gast_core_Identifier, GlobalFunction, GlobalVariable, Access, Delegate, TypeAlias, gast_core_GenericEntity, TypeParameterClass, gast_core_Root, Package, Clone, StructuralAbstraction, GASTType, BasePath, File, gast_core_File, gast_core_Directory, gast_core_PackageAlias, gast_core_SourceEntity, Position, gast_core_Position, gast_annotations_StructuralAbstraction, core_NamedModelElement, gast_annotations_Comment, core_SourceEntity, gast_annotations_Attribute, types_GASTClass, annotations_ModelAnnotation, gast_annotations_Clone, core_ModelElement, gast_annotations_CloneInstance, gast_types_TypeDecorator, gast_types_GASTType, gast_types_GASTArray, gast_annotations_Subsystem, gast_annotations_Layer, gast_annotations_ModelAnnotation, gast_types_Reference, TypeDecorator, gast_types_Member, Member, gast_types_TypeAlias, types_Member, types_TypeDecorator, gast_types_TypeParameterClass, gast_types_GenericClass, core_GenericEntity, gast_types_GASTEnumeration, gast_types_GASTStruct, gast_types_GASTUnion, gast_types_GASTClass, types_GASTType, Constructor, Destructor, Field, Method_, Property_, gast_accesses_ParameterInstantiationTypeAccess, TypeAccess, InheritanceTypeAccess, CompositeAccess, gast_accesses_TypeAccess, gast_accesses_DeclarationTypeAccess, gast_accesses_CastTypeAccess, gast_accesses_CompositeAccess, gast_accesses_BaseAccess, gast_accesses_DelegateAccess, FunctionAccess, gast_accesses_FunctionAccess, Variable, gast_accesses_ThrowTypeAccess, gast_accesses_InheritanceTypeAccess, gast_accesses_VariableAccess, gast_accesses_RunTimeTypeAccess, gast_accesses_SelfAccess, VariableAccess, gast_functions_Delegate, functions_Function, gast_accesses_StaticTypeAccess, gast_accesses_PropertyAccess, gast_accesses_Access, gast_functions_Constructor, gast_functions_Destructor, gast_functions_Method, gast_functions_GenericFunction, functions_GlobalFunction, gast_functions_GlobalFunction, LocalVariable, ThrowTypeAccess, gast_functions_GenericMethod, functions_Method, gast_functions_GenericConstructor, functions_Constructor, gast_functions_Function, DeclarationTypeAccess, FormalParameter, gast_variables_CatchParameter, gast_variables_Field, variables_Variable, gast_variables_LocalVariable, gast_variables_FormalParameter, gast_variables_Variable, gast_variables_Property, variables_Field, gast_variables_GlobalVariable, LoopStatementKind, JumpStatementKind, Status, Visibilities, GlobalFunctionKind},
    associations={catchBlocks0, finallyBlock1, guardedBlock3, accesses6, cloneInstance7, blockstatement8, surroundingStatement10, statements21, surroundingFunction24, conditionExpression25, branchstatement26, statement28, branches31, branch11, loopstatement13, cfPre15, cfNext18, catchParameter45, breakConditionExpression34, initExpression36, incrementExpression39, expression48, body42, blockstatement50, exit52, root53, expression46, allLocalClasses57, allInnerClasses58, directories54, annotations56, globalFunctions71, globalVariables73, root74, allNormalClasses61, allInterfaces64, allAccesses67, delegates69, allAccessedPackages84, typeAliases87, typeParameters89, allAccesses90, allInnerClasses92, classes77, subPackages79, surroundingPackage81, globalVariables106, packages109, clones112, structuralAbstractions114, types116, danglingModelElements118, basePaths121, allInterfaces95, allLocalClasses98, allNormalClasses101, allModelElements104, subDirectory126, parentDirectory129, files132, basePath134, root137, globalFunctions123, importedGlobalFunctions151, importedGlobalVariables154, importedPackages157, includedFiles160, importedTypes139, types142, globalVariables145, globalFunctions148, sourceFile166, assembly168, sourceentity171, aliasedPackage173, position175, directory163, statements183, clone186, cloneInstances177, root180, decoratedType191, undecoratedType193, referencedType189, surroundingClass200, surroundingPackage203, overriddenMember206, baseType196, aliasedType198, typeBounds207, innerTypeAliases209, surroundingFunction223, surroundingPackage226, superTypes229, innerClasses231, innerDelegates212, constructors215, destructors217, fields219, methods221, friendFunctions248, property251, allAccesses253, allAccessedClasses256, surroundingClass234, inheritanceTypeAccesses237, self239, friendClasses242, surroundingStatement270, gastClass245, surroundingClass272, surroundingFunction275, surroundingCompositeAccess278, targetType259, typeArguments261, accesses264, parentStatement267, accessedFunctions285, accessedDelegate287, typeArguments290, function280, surroundingVariable283, targetVariable295, targetFunction292, accessedTarget299, accessedClass297, surroundingPackage310, surroundingClass313, surroundingClass316, superClass302, invocations304, root322, surroundingClass307, surroundingProperty325, surroundingPackage319, localVariables334, allStatements336, throwTypeAccesses338, accesses340, surroundingClass327, returnTypeDeclaration330, formalParameters332, type352, typeDeclaration354, surroundingClass357, surroundingFunction360, body343, localClasses346, surroundingFunction349, setter363, getter365, surroundingPackage368},
    generalizations={gen_gast_statements_ExceptionHandler_Statement, gen_gast_statements_Statement_SourceEntity, gen_gast_statements_Branch_SourceEntity, gen_gast_statements_GASTExpression_SourceEntity, gen_gast_statements_BranchStatement_Statement, gen_gast_statements_BlockStatement_Statement, gen_gast_statements_CatchBlock_BlockStatement, gen_gast_statements_LoopStatement_Statement, gen_gast_statements_Methods_BlockStatement, gen_gast_core_BasePath_ModelElement, gen_gast_statements_JumpStatement_Statement, gen_gast_statements_SimpleStatement_Statement, gen_gast_core_NamedModelElement_ModelElement, gen_gast_core_Package_NamedModelElement, gen_gast_core_ModelElement_Identifier, gen_gast_core_GenericEntity_ModelElement, gen_gast_core_Root_ModelElement, gen_gast_core_File_NamedModelElement, gen_gast_core_Directory_NamedModelElement, gen_gast_core_PackageAlias_Package, gen_gast_core_SourceEntity_ModelElement, gen_gast_annotations_StructuralAbstraction_core_NamedModelElement, gen_gast_annotations_StructuralAbstraction_annotations_ModelAnnotation, gen_gast_annotations_Comment_core_SourceEntity, gen_gast_annotations_Comment_annotations_ModelAnnotation, gen_gast_annotations_Attribute_types_GASTClass, gen_gast_annotations_Attribute_annotations_ModelAnnotation, gen_gast_annotations_Clone_core_ModelElement, gen_gast_annotations_Clone_annotations_ModelAnnotation, gen_gast_annotations_CloneInstance_core_ModelElement, gen_gast_annotations_CloneInstance_annotations_ModelAnnotation, gen_gast_types_TypeDecorator_GASTType, gen_gast_types_GASTType_NamedModelElement, gen_gast_types_GASTArray_TypeDecorator, gen_gast_annotations_Subsystem_StructuralAbstraction, gen_gast_annotations_Layer_StructuralAbstraction, gen_gast_types_Reference_TypeDecorator, gen_gast_types_Member_SourceEntity, gen_gast_types_TypeAlias_types_Member, gen_gast_types_TypeAlias_types_TypeDecorator, gen_gast_types_TypeParameterClass_GASTClass, gen_gast_types_GenericClass_types_GASTClass, gen_gast_types_GenericClass_core_GenericEntity, gen_gast_types_GASTEnumeration_GASTClass, gen_gast_types_GASTStruct_GASTClass, gen_gast_types_GASTUnion_GASTClass, gen_gast_types_GASTClass_types_Member, gen_gast_types_GASTClass_types_GASTType, gen_gast_accesses_ParameterInstantiationTypeAccess_TypeAccess, gen_gast_accesses_TypeAccess_Access, gen_gast_accesses_DeclarationTypeAccess_TypeAccess, gen_gast_accesses_CastTypeAccess_TypeAccess, gen_gast_accesses_CompositeAccess_BaseAccess, gen_gast_accesses_BaseAccess_SourceEntity, gen_gast_accesses_DelegateAccess_FunctionAccess, gen_gast_accesses_FunctionAccess_Access, gen_gast_accesses_ThrowTypeAccess_TypeAccess, gen_gast_accesses_InheritanceTypeAccess_TypeAccess, gen_gast_accesses_VariableAccess_Access, gen_gast_accesses_RunTimeTypeAccess_TypeAccess, gen_gast_accesses_SelfAccess_VariableAccess, gen_gast_functions_Delegate_functions_Function, gen_gast_functions_Delegate_types_Member, gen_gast_functions_Delegate_types_GASTType, gen_gast_accesses_StaticTypeAccess_TypeAccess, gen_gast_accesses_PropertyAccess_VariableAccess, gen_gast_accesses_Access_BaseAccess, gen_gast_functions_Constructor_functions_Function, gen_gast_functions_Constructor_types_Member, gen_gast_functions_Destructor_functions_Function, gen_gast_functions_Destructor_types_Member, gen_gast_functions_Method_functions_Function, gen_gast_functions_Method_types_Member, gen_gast_functions_GenericFunction_functions_GlobalFunction, gen_gast_functions_GenericFunction_core_GenericEntity, gen_gast_functions_GlobalFunction_Function, gen_gast_functions_GenericMethod_functions_Method, gen_gast_functions_GenericMethod_core_GenericEntity, gen_gast_functions_GenericConstructor_functions_Constructor, gen_gast_functions_GenericConstructor_core_GenericEntity, gen_gast_functions_Function_core_NamedModelElement, gen_gast_functions_Function_core_SourceEntity, gen_gast_variables_CatchParameter_Variable, gen_gast_variables_Field_types_Member, gen_gast_variables_Field_variables_Variable, gen_gast_variables_LocalVariable_Variable, gen_gast_variables_FormalParameter_Variable, gen_gast_variables_Variable_core_NamedModelElement, gen_gast_variables_Variable_core_SourceEntity, gen_gast_variables_Property_variables_Field, gen_gast_variables_Property_types_Member, gen_gast_variables_GlobalVariable_Variable},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)