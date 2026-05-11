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
gast_statements_ExceptionHandler = Class(name="gast_statements_ExceptionHandler")
Statement = Class(name="Statement")
CatchBlock = Class(name="CatchBlock")
BlockStatement = Class(name="BlockStatement")
gast_statements_Statement = Class(name="gast_statements_Statement", is_abstract=True)
SourceEntity = Class(name="SourceEntity")
BaseAccess = Class(name="BaseAccess")
CloneInstance = Class(name="CloneInstance")
gast_statements_LoopStatement = Class(name="gast_statements_LoopStatement")
Branch = Class(name="Branch")
LoopStatement = Class(name="LoopStatement")
gast_statements_BlockStatement = Class(name="gast_statements_BlockStatement")
Function = Class(name="Function")
gast_statements_Branch = Class(name="gast_statements_Branch")
GASTExpression = Class(name="GASTExpression")
BranchStatement = Class(name="BranchStatement")
gast_statements_GASTExpression = Class(name="gast_statements_GASTExpression", is_abstract=True)
gast_statements_BranchStatement = Class(name="gast_statements_BranchStatement")
gast_statements_GASTBehaviour = Class(name="gast_statements_GASTBehaviour")
gast_statements_Methods = Class(name="gast_statements_Methods")
Exit = Class(name="Exit")
gast_statements_Exit = Class(name="gast_statements_Exit")
gast_core_BasePath = Class(name="gast_core_BasePath")
ModelElement = Class(name="ModelElement")
Root = Class(name="Root")
Directory = Class(name="Directory")
gast_core_ModelElement = Class(name="gast_core_ModelElement", is_abstract=True)
Identifier = Class(name="Identifier")
gast_statements_CatchBlock = Class(name="gast_statements_CatchBlock")
ModelAnnotation = Class(name="ModelAnnotation")
CatchParameter = Class(name="CatchParameter")
gast_statements_JumpStatement = Class(name="gast_statements_JumpStatement")
gast_core_Identifier = Class(name="gast_core_Identifier", is_abstract=True)
gast_statements_SimpleStatement = Class(name="gast_statements_SimpleStatement")
gast_core_NamedModelElement = Class(name="gast_core_NamedModelElement", is_abstract=True)
gast_core_Package = Class(name="gast_core_Package")
NamedModelElement = Class(name="NamedModelElement")
GASTClass = Class(name="GASTClass")
Access = Class(name="Access")
Delegate = Class(name="Delegate")
GlobalFunction = Class(name="GlobalFunction")
GlobalVariable = Class(name="GlobalVariable")
TypeAlias = Class(name="TypeAlias")
gast_core_GenericEntity = Class(name="gast_core_GenericEntity", is_abstract=True)
TypeParameterClass = Class(name="TypeParameterClass")
gast_core_Root = Class(name="gast_core_Root")
Package = Class(name="Package")
Clone = Class(name="Clone")
StructuralAbstraction = Class(name="StructuralAbstraction")
GASTType = Class(name="GASTType")
BasePath = Class(name="BasePath")
gast_core_Directory = Class(name="gast_core_Directory")
File = Class(name="File")
gast_core_File = Class(name="gast_core_File")
gast_core_Position = Class(name="gast_core_Position")
gast_core_PackageAlias = Class(name="gast_core_PackageAlias")
gast_core_SourceEntity = Class(name="gast_core_SourceEntity", is_abstract=True)
Position = Class(name="Position")
gast_annotations_Attribute = Class(name="gast_annotations_Attribute")
types_GASTClass = Class(name="types_GASTClass")
annotations_ModelAnnotation = Class(name="annotations_ModelAnnotation")
gast_annotations_Clone = Class(name="gast_annotations_Clone")
core_ModelElement = Class(name="core_ModelElement")
gast_annotations_CloneInstance = Class(name="gast_annotations_CloneInstance")
gast_annotations_StructuralAbstraction = Class(name="gast_annotations_StructuralAbstraction", is_abstract=True)
core_NamedModelElement = Class(name="core_NamedModelElement")
gast_annotations_Comment = Class(name="gast_annotations_Comment")
core_SourceEntity = Class(name="core_SourceEntity")
gast_annotations_Subsystem = Class(name="gast_annotations_Subsystem")
gast_annotations_Layer = Class(name="gast_annotations_Layer")
gast_annotations_ModelAnnotation = Class(name="gast_annotations_ModelAnnotation", is_abstract=True)
gast_types_Reference = Class(name="gast_types_Reference")
TypeDecorator = Class(name="TypeDecorator")
gast_types_TypeDecorator = Class(name="gast_types_TypeDecorator", is_abstract=True)
gast_types_GASTType = Class(name="gast_types_GASTType", is_abstract=True)
gast_types_GASTArray = Class(name="gast_types_GASTArray")
gast_types_TypeAlias = Class(name="gast_types_TypeAlias")
types_Member = Class(name="types_Member")
types_TypeDecorator = Class(name="types_TypeDecorator")
gast_types_Member = Class(name="gast_types_Member", is_abstract=True)
Member = Class(name="Member")
gast_types_TypeParameterClass = Class(name="gast_types_TypeParameterClass")
gast_types_GenericClass = Class(name="gast_types_GenericClass")
core_GenericEntity = Class(name="core_GenericEntity")
gast_types_GASTEnumeration = Class(name="gast_types_GASTEnumeration")
gast_types_GASTStruct = Class(name="gast_types_GASTStruct")
gast_types_GASTUnion = Class(name="gast_types_GASTUnion")
gast_types_GASTClass = Class(name="gast_types_GASTClass")
types_GASTType = Class(name="types_GASTType")
Constructor = Class(name="Constructor")
Destructor = Class(name="Destructor")
Field = Class(name="Field")
Method_ = Class(name="Method")
Property_ = Class(name="Property")
gast_accesses_ParameterInstantiationTypeAccess = Class(name="gast_accesses_ParameterInstantiationTypeAccess")
TypeAccess = Class(name="TypeAccess")
gast_accesses_TypeAccess = Class(name="gast_accesses_TypeAccess", is_abstract=True)
gast_accesses_CastTypeAccess = Class(name="gast_accesses_CastTypeAccess")
gast_accesses_CompositeAccess = Class(name="gast_accesses_CompositeAccess")
InheritanceTypeAccess = Class(name="InheritanceTypeAccess")
gast_accesses_BaseAccess = Class(name="gast_accesses_BaseAccess", is_abstract=True)
CompositeAccess = Class(name="CompositeAccess")
gast_accesses_DeclarationTypeAccess = Class(name="gast_accesses_DeclarationTypeAccess")
Variable = Class(name="Variable")
gast_accesses_ThrowTypeAccess = Class(name="gast_accesses_ThrowTypeAccess")
gast_accesses_DelegateAccess = Class(name="gast_accesses_DelegateAccess")
FunctionAccess = Class(name="FunctionAccess")
gast_accesses_InheritanceTypeAccess = Class(name="gast_accesses_InheritanceTypeAccess")
gast_accesses_VariableAccess = Class(name="gast_accesses_VariableAccess")
gast_accesses_RunTimeTypeAccess = Class(name="gast_accesses_RunTimeTypeAccess")
gast_accesses_SelfAccess = Class(name="gast_accesses_SelfAccess")
VariableAccess = Class(name="VariableAccess")
gast_accesses_StaticTypeAccess = Class(name="gast_accesses_StaticTypeAccess")
gast_accesses_FunctionAccess = Class(name="gast_accesses_FunctionAccess")
gast_functions_Delegate = Class(name="gast_functions_Delegate")
functions_Function = Class(name="functions_Function")
gast_functions_Constructor = Class(name="gast_functions_Constructor")
gast_accesses_PropertyAccess = Class(name="gast_accesses_PropertyAccess")
gast_accesses_Access = Class(name="gast_accesses_Access", is_abstract=True)
gast_functions_Destructor = Class(name="gast_functions_Destructor")
gast_functions_GenericFunction = Class(name="gast_functions_GenericFunction")
functions_GlobalFunction = Class(name="functions_GlobalFunction")
gast_functions_GlobalFunction = Class(name="gast_functions_GlobalFunction")
gast_functions_Method = Class(name="gast_functions_Method")
gast_functions_GenericMethod = Class(name="gast_functions_GenericMethod")
functions_Method = Class(name="functions_Method")
gast_functions_GenericConstructor = Class(name="gast_functions_GenericConstructor")
functions_Constructor = Class(name="functions_Constructor")
gast_functions_Function = Class(name="gast_functions_Function", is_abstract=True)
DeclarationTypeAccess = Class(name="DeclarationTypeAccess")
LocalVariable = Class(name="LocalVariable")
ThrowTypeAccess = Class(name="ThrowTypeAccess")
FormalParameter = Class(name="FormalParameter")
gast_variables_Variable = Class(name="gast_variables_Variable", is_abstract=True)
gast_variables_CatchParameter = Class(name="gast_variables_CatchParameter")
gast_variables_Field = Class(name="gast_variables_Field")
variables_Variable = Class(name="variables_Variable")
gast_variables_LocalVariable = Class(name="gast_variables_LocalVariable")
gast_variables_Property = Class(name="gast_variables_Property")
variables_Field = Class(name="variables_Field")
gast_variables_FormalParameter = Class(name="gast_variables_FormalParameter")
gast_variables_GlobalVariable = Class(name="gast_variables_GlobalVariable")

# gast_statements_ExceptionHandler class attributes and methods

# Statement class attributes and methods

# CatchBlock class attributes and methods

# BlockStatement class attributes and methods

# gast_statements_Statement class attributes and methods
gast_statements_Statement_numberOfComments: Property = Property(name="numberOfComments", type=IntegerType)
gast_statements_Statement_linesOfCode: Property = Property(name="linesOfCode", type=IntegerType)
gast_statements_Statement_numberOfEdgesInCFG: Property = Property(name="numberOfEdgesInCFG", type=IntegerType)
gast_statements_Statement_numberOfStatements: Property = Property(name="numberOfStatements", type=IntegerType)
gast_statements_Statement_maximumNestingLevel: Property = Property(name="maximumNestingLevel", type=IntegerType)
gast_statements_Statement_numberOfNodesInCFG: Property = Property(name="numberOfNodesInCFG", type=IntegerType)
gast_statements_Statement.attributes={gast_statements_Statement_numberOfNodesInCFG, gast_statements_Statement_numberOfComments, gast_statements_Statement_numberOfEdgesInCFG, gast_statements_Statement_maximumNestingLevel, gast_statements_Statement_numberOfStatements, gast_statements_Statement_linesOfCode}

# SourceEntity class attributes and methods

# BaseAccess class attributes and methods

# CloneInstance class attributes and methods

# gast_statements_LoopStatement class attributes and methods
gast_statements_LoopStatement_kind: Property = Property(name="kind", type=StringType)
gast_statements_LoopStatement.attributes={gast_statements_LoopStatement_kind}

# Branch class attributes and methods

# LoopStatement class attributes and methods

# gast_statements_BlockStatement class attributes and methods
gast_statements_BlockStatement_synchronized: Property = Property(name="synchronized", type=BooleanType)
gast_statements_BlockStatement.attributes={gast_statements_BlockStatement_synchronized}

# Function class attributes and methods

# gast_statements_Branch class attributes and methods

# GASTExpression class attributes and methods

# BranchStatement class attributes and methods

# gast_statements_GASTExpression class attributes and methods

# gast_statements_BranchStatement class attributes and methods

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

# Directory class attributes and methods

# gast_core_ModelElement class attributes and methods
gast_core_ModelElement_status: Property = Property(name="status", type=StringType)
gast_core_ModelElement_sissyId: Property = Property(name="sissyId", type=IntegerType)
gast_core_ModelElement.attributes={gast_core_ModelElement_sissyId, gast_core_ModelElement_status}

# Identifier class attributes and methods

# gast_statements_CatchBlock class attributes and methods

# ModelAnnotation class attributes and methods

# CatchParameter class attributes and methods

# gast_statements_JumpStatement class attributes and methods
gast_statements_JumpStatement_kind: Property = Property(name="kind", type=StringType)
gast_statements_JumpStatement.attributes={gast_statements_JumpStatement_kind}

# gast_core_Identifier class attributes and methods
gast_core_Identifier_id: Property = Property(name="id", type=StringType)
gast_core_Identifier_m_idHasToBeUnique: Method = Method(name="idHasToBeUnique", parameters={Parameter(name='gast_diagnostics', type=StringType), Parameter(name='gast_context', type=StringType)}, type=BooleanType)
gast_core_Identifier.attributes={gast_core_Identifier_id}
gast_core_Identifier.methods={gast_core_Identifier_m_idHasToBeUnique}

# gast_statements_SimpleStatement class attributes and methods

# gast_core_NamedModelElement class attributes and methods
gast_core_NamedModelElement_simpleName: Property = Property(name="simpleName", type=StringType)
gast_core_NamedModelElement.attributes={gast_core_NamedModelElement_simpleName}

# gast_core_Package class attributes and methods
gast_core_Package_linesOfComments: Property = Property(name="linesOfComments", type=IntegerType)
gast_core_Package_linesOfCode: Property = Property(name="linesOfCode", type=IntegerType)
gast_core_Package_qualifiedName: Property = Property(name="qualifiedName", type=StringType)
gast_core_Package.attributes={gast_core_Package_qualifiedName, gast_core_Package_linesOfComments, gast_core_Package_linesOfCode}

# NamedModelElement class attributes and methods

# GASTClass class attributes and methods

# Access class attributes and methods

# Delegate class attributes and methods

# GlobalFunction class attributes and methods

# GlobalVariable class attributes and methods

# TypeAlias class attributes and methods

# gast_core_GenericEntity class attributes and methods

# TypeParameterClass class attributes and methods

# gast_core_Root class attributes and methods
gast_core_Root_linesOfComments: Property = Property(name="linesOfComments", type=IntegerType)
gast_core_Root_linesOfCode: Property = Property(name="linesOfCode", type=IntegerType)
gast_core_Root_m_getPackageByName: Method = Method(name="getPackageByName", parameters={Parameter(name='gast_name', type=StringType)}, type=StringType)
gast_core_Root_m_getPackageByQualifiedName: Method = Method(name="getPackageByQualifiedName", parameters={Parameter(name='gast_qualifiedName', type=StringType)}, type=StringType)
gast_core_Root.attributes={gast_core_Root_linesOfComments, gast_core_Root_linesOfCode}
gast_core_Root.methods={gast_core_Root_m_getPackageByName, gast_core_Root_m_getPackageByQualifiedName}

# Package class attributes and methods

# Clone class attributes and methods

# StructuralAbstraction class attributes and methods

# GASTType class attributes and methods

# BasePath class attributes and methods

# gast_core_Directory class attributes and methods
gast_core_Directory_fullQualifiedPath: Property = Property(name="fullQualifiedPath", type=StringType)
gast_core_Directory_fileSystemPath: Property = Property(name="fileSystemPath", type=StringType)
gast_core_Directory.attributes={gast_core_Directory_fileSystemPath, gast_core_Directory_fullQualifiedPath}

# File class attributes and methods

# gast_core_File class attributes and methods
gast_core_File_sourceFile: Property = Property(name="sourceFile", type=BooleanType)
gast_core_File_assemblyFile: Property = Property(name="assemblyFile", type=BooleanType)
gast_core_File_linesOfCode: Property = Property(name="linesOfCode", type=IntegerType)
gast_core_File_size: Property = Property(name="size", type=StringType)
gast_core_File_fullQualifiedPath: Property = Property(name="fullQualifiedPath", type=StringType)
gast_core_File_fileSystemPath: Property = Property(name="fileSystemPath", type=StringType)
gast_core_File.attributes={gast_core_File_fullQualifiedPath, gast_core_File_assemblyFile, gast_core_File_linesOfCode, gast_core_File_sourceFile, gast_core_File_fileSystemPath, gast_core_File_size}

# gast_core_Position class attributes and methods
gast_core_Position_endColumn: Property = Property(name="endColumn", type=IntegerType)
gast_core_Position_endLine: Property = Property(name="endLine", type=IntegerType)
gast_core_Position_startLine: Property = Property(name="startLine", type=IntegerType)
gast_core_Position_startColumn: Property = Property(name="startColumn", type=IntegerType)
gast_core_Position_m_EitherAssemblyFileOrSourceFileSet: Method = Method(name="EitherAssemblyFileOrSourceFileSet", parameters={Parameter(name='gast_diagnostics', type=StringType), Parameter(name='gast_context', type=StringType)}, type=BooleanType)
gast_core_Position.attributes={gast_core_Position_startLine, gast_core_Position_endLine, gast_core_Position_endColumn, gast_core_Position_startColumn}
gast_core_Position.methods={gast_core_Position_m_EitherAssemblyFileOrSourceFileSet}

# gast_core_PackageAlias class attributes and methods

# gast_core_SourceEntity class attributes and methods

# Position class attributes and methods

# gast_annotations_Attribute class attributes and methods

# types_GASTClass class attributes and methods

# annotations_ModelAnnotation class attributes and methods

# gast_annotations_Clone class attributes and methods

# core_ModelElement class attributes and methods

# gast_annotations_CloneInstance class attributes and methods

# gast_annotations_StructuralAbstraction class attributes and methods

# core_NamedModelElement class attributes and methods

# gast_annotations_Comment class attributes and methods
gast_annotations_Comment_todo: Property = Property(name="todo", type=BooleanType)
gast_annotations_Comment_formal: Property = Property(name="formal", type=BooleanType)
gast_annotations_Comment_todoCount: Property = Property(name="todoCount", type=IntegerType)
gast_annotations_Comment_texts: Property = Property(name="texts", type=StringType)
gast_annotations_Comment_m_OCLtodo: Method = Method(name="OCLtodo", parameters={Parameter(name='gast_diagnostics', type=StringType), Parameter(name='gast_context', type=StringType)}, type=BooleanType)
gast_annotations_Comment.attributes={gast_annotations_Comment_todoCount, gast_annotations_Comment_todo, gast_annotations_Comment_formal, gast_annotations_Comment_texts}
gast_annotations_Comment.methods={gast_annotations_Comment_m_OCLtodo}

# core_SourceEntity class attributes and methods

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
gast_types_GASTType.attributes={gast_types_GASTType_qualifiedName, gast_types_GASTType_referenceType}

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
gast_types_Member_introspectable: Property = Property(name="introspectable", type=BooleanType)
gast_types_Member_override: Property = Property(name="override", type=BooleanType)
gast_types_Member_static: Property = Property(name="static", type=BooleanType)
gast_types_Member_typeParameterClassMember: Property = Property(name="typeParameterClassMember", type=BooleanType)
gast_types_Member_virtual: Property = Property(name="virtual", type=BooleanType)
gast_types_Member_final: Property = Property(name="final", type=BooleanType)
gast_types_Member_internal: Property = Property(name="internal", type=BooleanType)
gast_types_Member_m_getSurroundingClass: Method = Method(name="getSurroundingClass", parameters={}, type=StringType)
gast_types_Member.attributes={gast_types_Member_virtual, gast_types_Member_introspectable, gast_types_Member_override, gast_types_Member_abstract, gast_types_Member_typeParameterClassMember, gast_types_Member_final, gast_types_Member_static, gast_types_Member_extern, gast_types_Member_visibility, gast_types_Member_internal}
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
gast_types_GASTClass.attributes={gast_types_GASTClass_local, gast_types_GASTClass_inner, gast_types_GASTClass_primitive, gast_types_GASTClass_anonymous, gast_types_GASTClass_interface, gast_types_GASTClass_linesOfComments}

# types_GASTType class attributes and methods

# Constructor class attributes and methods

# Destructor class attributes and methods

# Field class attributes and methods

# Method class attributes and methods

# Property class attributes and methods

# gast_accesses_ParameterInstantiationTypeAccess class attributes and methods

# TypeAccess class attributes and methods

# gast_accesses_TypeAccess class attributes and methods

# gast_accesses_CastTypeAccess class attributes and methods

# gast_accesses_CompositeAccess class attributes and methods

# InheritanceTypeAccess class attributes and methods

# gast_accesses_BaseAccess class attributes and methods

# CompositeAccess class attributes and methods

# gast_accesses_DeclarationTypeAccess class attributes and methods

# Variable class attributes and methods

# gast_accesses_ThrowTypeAccess class attributes and methods
gast_accesses_ThrowTypeAccess_declared: Property = Property(name="declared", type=BooleanType)
gast_accesses_ThrowTypeAccess.attributes={gast_accesses_ThrowTypeAccess_declared}

# gast_accesses_DelegateAccess class attributes and methods

# FunctionAccess class attributes and methods

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

# gast_accesses_StaticTypeAccess class attributes and methods

# gast_accesses_FunctionAccess class attributes and methods

# gast_functions_Delegate class attributes and methods
gast_functions_Delegate_innerDelegate: Property = Property(name="innerDelegate", type=BooleanType)
gast_functions_Delegate.attributes={gast_functions_Delegate_innerDelegate}

# functions_Function class attributes and methods

# gast_functions_Constructor class attributes and methods
gast_functions_Constructor_initializer: Property = Property(name="initializer", type=BooleanType)
gast_functions_Constructor.attributes={gast_functions_Constructor_initializer}

# gast_accesses_PropertyAccess class attributes and methods

# gast_accesses_Access class attributes and methods

# gast_functions_Destructor class attributes and methods

# gast_functions_GenericFunction class attributes and methods

# functions_GlobalFunction class attributes and methods

# gast_functions_GlobalFunction class attributes and methods
gast_functions_GlobalFunction_kind: Property = Property(name="kind", type=StringType)
gast_functions_GlobalFunction.attributes={gast_functions_GlobalFunction_kind}

# gast_functions_Method class attributes and methods
gast_functions_Method_propertyMethod: Property = Property(name="propertyMethod", type=BooleanType)
gast_functions_Method.attributes={gast_functions_Method_propertyMethod}

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
gast_functions_Function.attributes={gast_functions_Function_operator, gast_functions_Function_linesOfComments, gast_functions_Function_numberOfNodesInCFG, gast_functions_Function_linesOfCode, gast_functions_Function_maximumNestingLevel, gast_functions_Function_numberOfEdgesInCFG, gast_functions_Function_numberOfStatements}

# DeclarationTypeAccess class attributes and methods

# LocalVariable class attributes and methods

# ThrowTypeAccess class attributes and methods

# FormalParameter class attributes and methods

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

# gast_variables_FormalParameter class attributes and methods
gast_variables_FormalParameter_passedByReference: Property = Property(name="passedByReference", type=BooleanType)
gast_variables_FormalParameter.attributes={gast_variables_FormalParameter_passedByReference}

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
        Property(name="BaseAccess", type=gast_statements_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="parentStatement", type=BaseAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cloneInstance7: BinaryAssociation = BinaryAssociation(
    name="cloneInstance7",
    ends={
        Property(name="CloneInstance", type=gast_statements_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="statements", type=CloneInstance, multiplicity=Multiplicity(0, 1))
    }
)
blockstatement8: BinaryAssociation = BinaryAssociation(
    name="blockstatement8",
    ends={
        Property(name="BlockStatement10", type=gast_statements_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="statements9", type=BlockStatement, multiplicity=Multiplicity(0, 1))
    }
)
surroundingStatement11: BinaryAssociation = BinaryAssociation(
    name="surroundingStatement11",
    ends={
        Property(name="Statement", type=gast_statements_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_statements_Statement", type=Statement, multiplicity=Multiplicity(0, 1))
    }
)
breakConditionExpression30: BinaryAssociation = BinaryAssociation(
    name="breakConditionExpression30",
    ends={
        Property(name="GASTExpression31", type=gast_statements_LoopStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_statements_LoopStatement", type=GASTExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initExpression32: BinaryAssociation = BinaryAssociation(
    name="initExpression32",
    ends={
        Property(name="GASTExpression34", type=gast_statements_LoopStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_statements_LoopStatement33", type=GASTExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
branch12: BinaryAssociation = BinaryAssociation(
    name="branch12",
    ends={
        Property(name="Branch", type=gast_statements_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="statement", type=Branch, multiplicity=Multiplicity(0, 1))
    }
)
loopstatement13: BinaryAssociation = BinaryAssociation(
    name="loopstatement13",
    ends={
        Property(name="LoopStatement", type=gast_statements_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="body", type=LoopStatement, multiplicity=Multiplicity(0, 1))
    }
)
cfPre14: BinaryAssociation = BinaryAssociation(
    name="cfPre14",
    ends={
        Property(name="Statement16", type=gast_statements_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_statements_Statement15", type=Statement, multiplicity=Multiplicity(0, 9999))
    }
)
cfNext17: BinaryAssociation = BinaryAssociation(
    name="cfNext17",
    ends={
        Property(name="Statement19", type=gast_statements_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_statements_Statement18", type=Statement, multiplicity=Multiplicity(0, 9999))
    }
)
statements20: BinaryAssociation = BinaryAssociation(
    name="statements20",
    ends={
        Property(name="Statement21", type=gast_statements_BlockStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="blockstatement", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
surroundingFunction22: BinaryAssociation = BinaryAssociation(
    name="surroundingFunction22",
    ends={
        Property(name="Function", type=gast_statements_BlockStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="body23", type=Function, multiplicity=Multiplicity(0, 1))
    }
)
conditionExpression24: BinaryAssociation = BinaryAssociation(
    name="conditionExpression24",
    ends={
        Property(name="GASTExpression", type=gast_statements_Branch, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_statements_Branch", type=GASTExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
branchstatement25: BinaryAssociation = BinaryAssociation(
    name="branchstatement25",
    ends={
        Property(name="BranchStatement", type=gast_statements_Branch, multiplicity=Multiplicity(1, 1)),
        Property(name="branches", type=BranchStatement, multiplicity=Multiplicity(1, 1))
    }
)
statement26: BinaryAssociation = BinaryAssociation(
    name="statement26",
    ends={
        Property(name="Statement27", type=gast_statements_Branch, multiplicity=Multiplicity(1, 1)),
        Property(name="branch", type=Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
branches28: BinaryAssociation = BinaryAssociation(
    name="branches28",
    ends={
        Property(name="Branch29", type=gast_statements_BranchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="branchstatement", type=Branch, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
expression43: BinaryAssociation = BinaryAssociation(
    name="expression43",
    ends={
        Property(name="GASTExpression44", type=gast_statements_SimpleStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_statements_SimpleStatement", type=GASTExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
blockstatement45: BinaryAssociation = BinaryAssociation(
    name="blockstatement45",
    ends={
        Property(name="BlockStatement46", type=gast_statements_GASTBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_statements_GASTBehaviour", type=BlockStatement, multiplicity=Multiplicity(1, 1))
    }
)
incrementExpression35: BinaryAssociation = BinaryAssociation(
    name="incrementExpression35",
    ends={
        Property(name="GASTExpression37", type=gast_statements_LoopStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_statements_LoopStatement36", type=GASTExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exit47: BinaryAssociation = BinaryAssociation(
    name="exit47",
    ends={
        Property(name="Exit", type=gast_statements_Methods, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_statements_Methods", type=Exit, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body38: BinaryAssociation = BinaryAssociation(
    name="body38",
    ends={
        Property(name="Statement39", type=gast_statements_LoopStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="loopstatement", type=Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
root48: BinaryAssociation = BinaryAssociation(
    name="root48",
    ends={
        Property(name="Root", type=gast_core_BasePath, multiplicity=Multiplicity(1, 1)),
        Property(name="basePaths", type=Root, multiplicity=Multiplicity(1, 1))
    }
)
directories49: BinaryAssociation = BinaryAssociation(
    name="directories49",
    ends={
        Property(name="Directory", type=gast_core_BasePath, multiplicity=Multiplicity(1, 1)),
        Property(name="basePath", type=Directory, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotations50: BinaryAssociation = BinaryAssociation(
    name="annotations50",
    ends={
        Property(name="ModelAnnotation", type=gast_core_ModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_ModelElement", type=ModelAnnotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
catchParameter40: BinaryAssociation = BinaryAssociation(
    name="catchParameter40",
    ends={
        Property(name="CatchParameter", type=gast_statements_CatchBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_statements_CatchBlock", type=CatchParameter, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression41: BinaryAssociation = BinaryAssociation(
    name="expression41",
    ends={
        Property(name="GASTExpression42", type=gast_statements_JumpStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_statements_JumpStatement", type=GASTExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
allLocalClasses51: BinaryAssociation = BinaryAssociation(
    name="allLocalClasses51",
    ends={
        Property(name="GASTClass", type=gast_core_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_Package", type=GASTClass, multiplicity=Multiplicity(0, 9999))
    }
)
allInnerClasses52: BinaryAssociation = BinaryAssociation(
    name="allInnerClasses52",
    ends={
        Property(name="GASTClass54", type=gast_core_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_Package53", type=GASTClass, multiplicity=Multiplicity(0, 9999))
    }
)
allNormalClasses55: BinaryAssociation = BinaryAssociation(
    name="allNormalClasses55",
    ends={
        Property(name="GASTClass57", type=gast_core_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_Package56", type=GASTClass, multiplicity=Multiplicity(0, 9999))
    }
)
allInterfaces58: BinaryAssociation = BinaryAssociation(
    name="allInterfaces58",
    ends={
        Property(name="GASTClass60", type=gast_core_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_Package59", type=GASTClass, multiplicity=Multiplicity(0, 9999))
    }
)
allAccesses61: BinaryAssociation = BinaryAssociation(
    name="allAccesses61",
    ends={
        Property(name="Access", type=gast_core_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_Package62", type=Access, multiplicity=Multiplicity(0, 9999))
    }
)
delegates63: BinaryAssociation = BinaryAssociation(
    name="delegates63",
    ends={
        Property(name="Delegate", type=gast_core_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="surroundingPackage", type=Delegate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
globalFunctions64: BinaryAssociation = BinaryAssociation(
    name="globalFunctions64",
    ends={
        Property(name="GlobalFunction", type=gast_core_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="surroundingPackage65", type=GlobalFunction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
globalVariables66: BinaryAssociation = BinaryAssociation(
    name="globalVariables66",
    ends={
        Property(name="GlobalVariable", type=gast_core_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="surroundingPackage67", type=GlobalVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
root68: BinaryAssociation = BinaryAssociation(
    name="root68",
    ends={
        Property(name="Root69", type=gast_core_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="packages", type=Root, multiplicity=Multiplicity(0, 1))
    }
)
classes70: BinaryAssociation = BinaryAssociation(
    name="classes70",
    ends={
        Property(name="GASTClass72", type=gast_core_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="surroundingPackage71", type=GASTClass, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
surroundingPackage75: BinaryAssociation = BinaryAssociation(
    name="surroundingPackage75",
    ends={
        Property(name="Package76", type=gast_core_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="subPackages", type=Package, multiplicity=Multiplicity(0, 1))
    }
)
allAccessedPackages77: BinaryAssociation = BinaryAssociation(
    name="allAccessedPackages77",
    ends={
        Property(name="Package79", type=gast_core_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_Package78", type=Package, multiplicity=Multiplicity(0, 9999))
    }
)
typeAliases80: BinaryAssociation = BinaryAssociation(
    name="typeAliases80",
    ends={
        Property(name="TypeAlias", type=gast_core_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="surroundingPackage81", type=TypeAlias, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeParameters82: BinaryAssociation = BinaryAssociation(
    name="typeParameters82",
    ends={
        Property(name="TypeParameterClass", type=gast_core_GenericEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_GenericEntity", type=TypeParameterClass, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
subPackages73: BinaryAssociation = BinaryAssociation(
    name="subPackages73",
    ends={
        Property(name="Package", type=gast_core_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="surroundingPackage74", type=Package, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
        Property(name="Package103", type=gast_core_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="root", type=Package, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
clones104: BinaryAssociation = BinaryAssociation(
    name="clones104",
    ends={
        Property(name="Clone", type=gast_core_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="root105", type=Clone, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
structuralAbstractions106: BinaryAssociation = BinaryAssociation(
    name="structuralAbstractions106",
    ends={
        Property(name="StructuralAbstraction", type=gast_core_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_Root107", type=StructuralAbstraction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
types108: BinaryAssociation = BinaryAssociation(
    name="types108",
    ends={
        Property(name="GASTType", type=gast_core_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_Root109", type=GASTType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
danglingModelElements110: BinaryAssociation = BinaryAssociation(
    name="danglingModelElements110",
    ends={
        Property(name="ModelElement112", type=gast_core_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_Root111", type=ModelElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
basePaths113: BinaryAssociation = BinaryAssociation(
    name="basePaths113",
    ends={
        Property(name="BasePath", type=gast_core_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="root114", type=BasePath, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
allModelElements97: BinaryAssociation = BinaryAssociation(
    name="allModelElements97",
    ends={
        Property(name="ModelElement", type=gast_core_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_Root98", type=ModelElement, multiplicity=Multiplicity(0, 9999))
    }
)
subDirectory118: BinaryAssociation = BinaryAssociation(
    name="subDirectory118",
    ends={
        Property(name="Directory119", type=gast_core_Directory, multiplicity=Multiplicity(1, 1)),
        Property(name="parentDirectory", type=Directory, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentDirectory120: BinaryAssociation = BinaryAssociation(
    name="parentDirectory120",
    ends={
        Property(name="Directory121", type=gast_core_Directory, multiplicity=Multiplicity(1, 1)),
        Property(name="subDirectory", type=Directory, multiplicity=Multiplicity(0, 1))
    }
)
files122: BinaryAssociation = BinaryAssociation(
    name="files122",
    ends={
        Property(name="File", type=gast_core_Directory, multiplicity=Multiplicity(1, 1)),
        Property(name="directory", type=File, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
basePath123: BinaryAssociation = BinaryAssociation(
    name="basePath123",
    ends={
        Property(name="BasePath124", type=gast_core_Directory, multiplicity=Multiplicity(1, 1)),
        Property(name="directories", type=BasePath, multiplicity=Multiplicity(0, 1))
    }
)
root125: BinaryAssociation = BinaryAssociation(
    name="root125",
    ends={
        Property(name="Root126", type=gast_core_File, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_File", type=Root, multiplicity=Multiplicity(1, 1))
    }
)
importedTypes127: BinaryAssociation = BinaryAssociation(
    name="importedTypes127",
    ends={
        Property(name="GASTType129", type=gast_core_File, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_File128", type=GASTType, multiplicity=Multiplicity(0, 9999))
    }
)
globalFunctions115: BinaryAssociation = BinaryAssociation(
    name="globalFunctions115",
    ends={
        Property(name="GlobalFunction117", type=gast_core_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="root116", type=GlobalFunction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
globalVariables133: BinaryAssociation = BinaryAssociation(
    name="globalVariables133",
    ends={
        Property(name="GlobalVariable135", type=gast_core_File, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_File134", type=GlobalVariable, multiplicity=Multiplicity(0, 9999))
    }
)
globalFunctions136: BinaryAssociation = BinaryAssociation(
    name="globalFunctions136",
    ends={
        Property(name="GlobalFunction138", type=gast_core_File, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_File137", type=GlobalFunction, multiplicity=Multiplicity(0, 9999))
    }
)
importedGlobalFunctions139: BinaryAssociation = BinaryAssociation(
    name="importedGlobalFunctions139",
    ends={
        Property(name="GlobalFunction141", type=gast_core_File, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_File140", type=GlobalFunction, multiplicity=Multiplicity(0, 9999))
    }
)
importedGlobalVariables142: BinaryAssociation = BinaryAssociation(
    name="importedGlobalVariables142",
    ends={
        Property(name="GlobalVariable144", type=gast_core_File, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_File143", type=GlobalVariable, multiplicity=Multiplicity(0, 9999))
    }
)
importedPackages145: BinaryAssociation = BinaryAssociation(
    name="importedPackages145",
    ends={
        Property(name="Package147", type=gast_core_File, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_File146", type=Package, multiplicity=Multiplicity(0, 9999))
    }
)
includedFiles148: BinaryAssociation = BinaryAssociation(
    name="includedFiles148",
    ends={
        Property(name="File150", type=gast_core_File, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_File149", type=File, multiplicity=Multiplicity(0, 9999))
    }
)
directory151: BinaryAssociation = BinaryAssociation(
    name="directory151",
    ends={
        Property(name="Directory152", type=gast_core_File, multiplicity=Multiplicity(1, 1)),
        Property(name="files", type=Directory, multiplicity=Multiplicity(1, 1))
    }
)
types130: BinaryAssociation = BinaryAssociation(
    name="types130",
    ends={
        Property(name="GASTType132", type=gast_core_File, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_File131", type=GASTType, multiplicity=Multiplicity(0, 9999))
    }
)
sourceFile153: BinaryAssociation = BinaryAssociation(
    name="sourceFile153",
    ends={
        Property(name="File154", type=gast_core_Position, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_Position", type=File, multiplicity=Multiplicity(0, 1))
    }
)
assembly155: BinaryAssociation = BinaryAssociation(
    name="assembly155",
    ends={
        Property(name="File157", type=gast_core_Position, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_Position156", type=File, multiplicity=Multiplicity(0, 1))
    }
)
sourceentity158: BinaryAssociation = BinaryAssociation(
    name="sourceentity158",
    ends={
        Property(name="SourceEntity", type=gast_core_Position, multiplicity=Multiplicity(1, 1)),
        Property(name="position", type=SourceEntity, multiplicity=Multiplicity(1, 1))
    }
)
aliasedPackage159: BinaryAssociation = BinaryAssociation(
    name="aliasedPackage159",
    ends={
        Property(name="Package160", type=gast_core_PackageAlias, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_PackageAlias", type=Package, multiplicity=Multiplicity(1, 1))
    }
)
position161: BinaryAssociation = BinaryAssociation(
    name="position161",
    ends={
        Property(name="Position", type=gast_core_SourceEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="sourceentity", type=Position, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cloneInstances162: BinaryAssociation = BinaryAssociation(
    name="cloneInstances162",
    ends={
        Property(name="CloneInstance163", type=gast_annotations_Clone, multiplicity=Multiplicity(1, 1)),
        Property(name="clone", type=CloneInstance, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
root164: BinaryAssociation = BinaryAssociation(
    name="root164",
    ends={
        Property(name="Root165", type=gast_annotations_Clone, multiplicity=Multiplicity(1, 1)),
        Property(name="clones", type=Root, multiplicity=Multiplicity(1, 1))
    }
)
statements166: BinaryAssociation = BinaryAssociation(
    name="statements166",
    ends={
        Property(name="Statement167", type=gast_annotations_CloneInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="cloneInstance", type=Statement, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
referencedType170: BinaryAssociation = BinaryAssociation(
    name="referencedType170",
    ends={
        Property(name="GASTType171", type=gast_types_Reference, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_types_Reference", type=GASTType, multiplicity=Multiplicity(1, 1))
    }
)
decoratedType172: BinaryAssociation = BinaryAssociation(
    name="decoratedType172",
    ends={
        Property(name="GASTType173", type=gast_types_TypeDecorator, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_types_TypeDecorator", type=GASTType, multiplicity=Multiplicity(1, 1))
    }
)
undecoratedType174: BinaryAssociation = BinaryAssociation(
    name="undecoratedType174",
    ends={
        Property(name="GASTType176", type=gast_types_TypeDecorator, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_types_TypeDecorator175", type=GASTType, multiplicity=Multiplicity(1, 1))
    }
)
clone168: BinaryAssociation = BinaryAssociation(
    name="clone168",
    ends={
        Property(name="Clone169", type=gast_annotations_CloneInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="cloneInstances", type=Clone, multiplicity=Multiplicity(1, 1))
    }
)
baseType177: BinaryAssociation = BinaryAssociation(
    name="baseType177",
    ends={
        Property(name="GASTType178", type=gast_types_GASTArray, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_types_GASTArray", type=GASTType, multiplicity=Multiplicity(1, 1))
    }
)
aliasedType179: BinaryAssociation = BinaryAssociation(
    name="aliasedType179",
    ends={
        Property(name="GASTType180", type=gast_types_TypeAlias, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_types_TypeAlias", type=GASTType, multiplicity=Multiplicity(1, 1))
    }
)
surroundingClass181: BinaryAssociation = BinaryAssociation(
    name="surroundingClass181",
    ends={
        Property(name="GASTClass182", type=gast_types_TypeAlias, multiplicity=Multiplicity(1, 1)),
        Property(name="innerTypeAliases", type=GASTClass, multiplicity=Multiplicity(0, 1))
    }
)
surroundingPackage183: BinaryAssociation = BinaryAssociation(
    name="surroundingPackage183",
    ends={
        Property(name="Package184", type=gast_types_TypeAlias, multiplicity=Multiplicity(1, 1)),
        Property(name="typeAliases", type=Package, multiplicity=Multiplicity(0, 1))
    }
)
overriddenMember185: BinaryAssociation = BinaryAssociation(
    name="overriddenMember185",
    ends={
        Property(name="Member", type=gast_types_Member, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_types_Member", type=Member, multiplicity=Multiplicity(0, 1))
    }
)
typeBounds186: BinaryAssociation = BinaryAssociation(
    name="typeBounds186",
    ends={
        Property(name="GASTType187", type=gast_types_TypeParameterClass, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_types_TypeParameterClass", type=GASTType, multiplicity=Multiplicity(0, 9999))
    }
)
innerTypeAliases188: BinaryAssociation = BinaryAssociation(
    name="innerTypeAliases188",
    ends={
        Property(name="TypeAlias189", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="surroundingClass", type=TypeAlias, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
constructors193: BinaryAssociation = BinaryAssociation(
    name="constructors193",
    ends={
        Property(name="Constructor", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="surroundingClass194", type=Constructor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
destructors195: BinaryAssociation = BinaryAssociation(
    name="destructors195",
    ends={
        Property(name="Destructor", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="surroundingClass196", type=Destructor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fields197: BinaryAssociation = BinaryAssociation(
    name="fields197",
    ends={
        Property(name="Field", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="surroundingClass198", type=Field, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
methods199: BinaryAssociation = BinaryAssociation(
    name="methods199",
    ends={
        Property(name="Method", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="surroundingClass200", type=Method_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
surroundingFunction201: BinaryAssociation = BinaryAssociation(
    name="surroundingFunction201",
    ends={
        Property(name="Function202", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="localClasses", type=Function, multiplicity=Multiplicity(0, 1))
    }
)
surroundingPackage203: BinaryAssociation = BinaryAssociation(
    name="surroundingPackage203",
    ends={
        Property(name="Package204", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="classes", type=Package, multiplicity=Multiplicity(0, 1))
    }
)
superTypes205: BinaryAssociation = BinaryAssociation(
    name="superTypes205",
    ends={
        Property(name="GASTClass206", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_types_GASTClass", type=GASTClass, multiplicity=Multiplicity(0, 9999))
    }
)
innerClasses207: BinaryAssociation = BinaryAssociation(
    name="innerClasses207",
    ends={
        Property(name="GASTClass209", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="surroundingClass208", type=GASTClass, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
surroundingClass210: BinaryAssociation = BinaryAssociation(
    name="surroundingClass210",
    ends={
        Property(name="GASTClass211", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="innerClasses", type=GASTClass, multiplicity=Multiplicity(0, 1))
    }
)
innerDelegates190: BinaryAssociation = BinaryAssociation(
    name="innerDelegates190",
    ends={
        Property(name="Delegate192", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="surroundingClass191", type=Delegate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
self214: BinaryAssociation = BinaryAssociation(
    name="self214",
    ends={
        Property(name="Field216", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_types_GASTClass215", type=Field, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
friendClasses217: BinaryAssociation = BinaryAssociation(
    name="friendClasses217",
    ends={
        Property(name="GASTClass218", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="gastClass", type=GASTClass, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
gastClass219: BinaryAssociation = BinaryAssociation(
    name="gastClass219",
    ends={
        Property(name="GASTClass220", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="friendClasses", type=GASTClass, multiplicity=Multiplicity(0, 1))
    }
)
friendFunctions221: BinaryAssociation = BinaryAssociation(
    name="friendFunctions221",
    ends={
        Property(name="Function223", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_types_GASTClass222", type=Function, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
property224: BinaryAssociation = BinaryAssociation(
    name="property224",
    ends={
        Property(name="Property", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_types_GASTClass225", type=Property_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
allAccesses226: BinaryAssociation = BinaryAssociation(
    name="allAccesses226",
    ends={
        Property(name="Access228", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_types_GASTClass227", type=Access, multiplicity=Multiplicity(0, 9999))
    }
)
allAccessedClasses229: BinaryAssociation = BinaryAssociation(
    name="allAccessedClasses229",
    ends={
        Property(name="GASTClass231", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_types_GASTClass230", type=GASTClass, multiplicity=Multiplicity(0, 9999))
    }
)
targetType232: BinaryAssociation = BinaryAssociation(
    name="targetType232",
    ends={
        Property(name="GASTType233", type=gast_accesses_TypeAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_accesses_TypeAccess", type=GASTType, multiplicity=Multiplicity(1, 1))
    }
)
typeArguments234: BinaryAssociation = BinaryAssociation(
    name="typeArguments234",
    ends={
        Property(name="GASTType236", type=gast_accesses_TypeAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_accesses_TypeAccess235", type=GASTType, multiplicity=Multiplicity(0, 9999))
    }
)
inheritanceTypeAccesses212: BinaryAssociation = BinaryAssociation(
    name="inheritanceTypeAccesses212",
    ends={
        Property(name="InheritanceTypeAccess", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_types_GASTClass213", type=InheritanceTypeAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentStatement239: BinaryAssociation = BinaryAssociation(
    name="parentStatement239",
    ends={
        Property(name="Statement240", type=gast_accesses_BaseAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="accesses", type=Statement, multiplicity=Multiplicity(0, 1))
    }
)
surroundingStatement241: BinaryAssociation = BinaryAssociation(
    name="surroundingStatement241",
    ends={
        Property(name="Statement242", type=gast_accesses_BaseAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_accesses_BaseAccess", type=Statement, multiplicity=Multiplicity(0, 1))
    }
)
surroundingClass243: BinaryAssociation = BinaryAssociation(
    name="surroundingClass243",
    ends={
        Property(name="GASTClass245", type=gast_accesses_BaseAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_accesses_BaseAccess244", type=GASTClass, multiplicity=Multiplicity(1, 1))
    }
)
surroundingFunction246: BinaryAssociation = BinaryAssociation(
    name="surroundingFunction246",
    ends={
        Property(name="Function248", type=gast_accesses_BaseAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_accesses_BaseAccess247", type=Function, multiplicity=Multiplicity(0, 1))
    }
)
surroundingCompositeAccess249: BinaryAssociation = BinaryAssociation(
    name="surroundingCompositeAccess249",
    ends={
        Property(name="CompositeAccess", type=gast_accesses_BaseAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="accesses250", type=CompositeAccess, multiplicity=Multiplicity(0, 1))
    }
)
function251: BinaryAssociation = BinaryAssociation(
    name="function251",
    ends={
        Property(name="Function252", type=gast_accesses_DeclarationTypeAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="returnTypeDeclaration", type=Function, multiplicity=Multiplicity(0, 1))
    }
)
surroundingVariable253: BinaryAssociation = BinaryAssociation(
    name="surroundingVariable253",
    ends={
        Property(name="Variable", type=gast_accesses_DeclarationTypeAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="typeDeclaration", type=Variable, multiplicity=Multiplicity(0, 1))
    }
)
accessedFunctions254: BinaryAssociation = BinaryAssociation(
    name="accessedFunctions254",
    ends={
        Property(name="Function255", type=gast_accesses_DelegateAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_accesses_DelegateAccess", type=Function, multiplicity=Multiplicity(0, 9999))
    }
)
accessedDelegate256: BinaryAssociation = BinaryAssociation(
    name="accessedDelegate256",
    ends={
        Property(name="Delegate258", type=gast_accesses_DelegateAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_accesses_DelegateAccess257", type=Delegate, multiplicity=Multiplicity(1, 1))
    }
)
accesses237: BinaryAssociation = BinaryAssociation(
    name="accesses237",
    ends={
        Property(name="BaseAccess238", type=gast_accesses_CompositeAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="surroundingCompositeAccess", type=BaseAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeArguments259: BinaryAssociation = BinaryAssociation(
    name="typeArguments259",
    ends={
        Property(name="GASTType260", type=gast_accesses_FunctionAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_accesses_FunctionAccess", type=GASTType, multiplicity=Multiplicity(0, 9999))
    }
)
targetFunction261: BinaryAssociation = BinaryAssociation(
    name="targetFunction261",
    ends={
        Property(name="Function263", type=gast_accesses_FunctionAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_accesses_FunctionAccess262", type=Function, multiplicity=Multiplicity(1, 1))
    }
)
targetVariable264: BinaryAssociation = BinaryAssociation(
    name="targetVariable264",
    ends={
        Property(name="Variable265", type=gast_accesses_VariableAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_accesses_VariableAccess", type=Variable, multiplicity=Multiplicity(1, 1))
    }
)
accessedClass266: BinaryAssociation = BinaryAssociation(
    name="accessedClass266",
    ends={
        Property(name="GASTClass267", type=gast_accesses_Access, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_accesses_Access", type=GASTClass, multiplicity=Multiplicity(1, 1))
    }
)
accessedTarget268: BinaryAssociation = BinaryAssociation(
    name="accessedTarget268",
    ends={
        Property(name="ModelElement270", type=gast_accesses_Access, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_accesses_Access269", type=ModelElement, multiplicity=Multiplicity(1, 1))
    }
)
superClass271: BinaryAssociation = BinaryAssociation(
    name="superClass271",
    ends={
        Property(name="GASTClass272", type=gast_functions_Delegate, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_functions_Delegate", type=GASTClass, multiplicity=Multiplicity(0, 1))
    }
)
invocations273: BinaryAssociation = BinaryAssociation(
    name="invocations273",
    ends={
        Property(name="Function275", type=gast_functions_Delegate, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_functions_Delegate274", type=Function, multiplicity=Multiplicity(0, 9999))
    }
)
surroundingClass276: BinaryAssociation = BinaryAssociation(
    name="surroundingClass276",
    ends={
        Property(name="GASTClass277", type=gast_functions_Delegate, multiplicity=Multiplicity(1, 1)),
        Property(name="innerDelegates", type=GASTClass, multiplicity=Multiplicity(0, 1))
    }
)
surroundingPackage278: BinaryAssociation = BinaryAssociation(
    name="surroundingPackage278",
    ends={
        Property(name="Package279", type=gast_functions_Delegate, multiplicity=Multiplicity(1, 1)),
        Property(name="delegates", type=Package, multiplicity=Multiplicity(0, 1))
    }
)
surroundingClass280: BinaryAssociation = BinaryAssociation(
    name="surroundingClass280",
    ends={
        Property(name="constructors", type=GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="GASTClass281", type=gast_functions_Constructor, multiplicity=Multiplicity(1, 1))
    }
)
surroundingClass282: BinaryAssociation = BinaryAssociation(
    name="surroundingClass282",
    ends={
        Property(name="GASTClass283", type=gast_functions_Destructor, multiplicity=Multiplicity(1, 1)),
        Property(name="destructors", type=GASTClass, multiplicity=Multiplicity(1, 1))
    }
)
surroundingPackage284: BinaryAssociation = BinaryAssociation(
    name="surroundingPackage284",
    ends={
        Property(name="Package285", type=gast_functions_GlobalFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="globalFunctions", type=Package, multiplicity=Multiplicity(0, 1))
    }
)
root286: BinaryAssociation = BinaryAssociation(
    name="root286",
    ends={
        Property(name="Root288", type=gast_functions_GlobalFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="globalFunctions287", type=Root, multiplicity=Multiplicity(0, 1))
    }
)
surroundingProperty289: BinaryAssociation = BinaryAssociation(
    name="surroundingProperty289",
    ends={
        Property(name="Property290", type=gast_functions_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_functions_Method", type=Property_, multiplicity=Multiplicity(0, 1))
    }
)
surroundingClass291: BinaryAssociation = BinaryAssociation(
    name="surroundingClass291",
    ends={
        Property(name="GASTClass292", type=gast_functions_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="methods", type=GASTClass, multiplicity=Multiplicity(1, 1))
    }
)
returnTypeDeclaration293: BinaryAssociation = BinaryAssociation(
    name="returnTypeDeclaration293",
    ends={
        Property(name="DeclarationTypeAccess", type=gast_functions_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="function", type=DeclarationTypeAccess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
localVariables295: BinaryAssociation = BinaryAssociation(
    name="localVariables295",
    ends={
        Property(name="LocalVariable", type=gast_functions_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="surroundingFunction296", type=LocalVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
allStatements297: BinaryAssociation = BinaryAssociation(
    name="allStatements297",
    ends={
        Property(name="Statement298", type=gast_functions_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_functions_Function", type=Statement, multiplicity=Multiplicity(0, 9999))
    }
)
throwTypeAccesses299: BinaryAssociation = BinaryAssociation(
    name="throwTypeAccesses299",
    ends={
        Property(name="ThrowTypeAccess", type=gast_functions_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_functions_Function300", type=ThrowTypeAccess, multiplicity=Multiplicity(0, 9999))
    }
)
accesses301: BinaryAssociation = BinaryAssociation(
    name="accesses301",
    ends={
        Property(name="Access303", type=gast_functions_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_functions_Function302", type=Access, multiplicity=Multiplicity(0, 9999))
    }
)
body304: BinaryAssociation = BinaryAssociation(
    name="body304",
    ends={
        Property(name="BlockStatement306", type=gast_functions_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="surroundingFunction305", type=BlockStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
localClasses307: BinaryAssociation = BinaryAssociation(
    name="localClasses307",
    ends={
        Property(name="GASTClass309", type=gast_functions_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="surroundingFunction308", type=GASTClass, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
surroundingFunction310: BinaryAssociation = BinaryAssociation(
    name="surroundingFunction310",
    ends={
        Property(name="Function311", type=gast_variables_FormalParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="formalParameters", type=Function, multiplicity=Multiplicity(1, 1))
    }
)
formalParameters294: BinaryAssociation = BinaryAssociation(
    name="formalParameters294",
    ends={
        Property(name="FormalParameter", type=gast_functions_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="surroundingFunction", type=FormalParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type312: BinaryAssociation = BinaryAssociation(
    name="type312",
    ends={
        Property(name="GASTType313", type=gast_variables_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_variables_Variable", type=GASTType, multiplicity=Multiplicity(1, 1))
    }
)
typeDeclaration314: BinaryAssociation = BinaryAssociation(
    name="typeDeclaration314",
    ends={
        Property(name="DeclarationTypeAccess315", type=gast_variables_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="surroundingVariable", type=DeclarationTypeAccess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
surroundingClass316: BinaryAssociation = BinaryAssociation(
    name="surroundingClass316",
    ends={
        Property(name="GASTClass317", type=gast_variables_Field, multiplicity=Multiplicity(1, 1)),
        Property(name="fields", type=GASTClass, multiplicity=Multiplicity(0, 1))
    }
)
surroundingFunction318: BinaryAssociation = BinaryAssociation(
    name="surroundingFunction318",
    ends={
        Property(name="Function319", type=gast_variables_LocalVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="localVariables", type=Function, multiplicity=Multiplicity(1, 1))
    }
)
setter320: BinaryAssociation = BinaryAssociation(
    name="setter320",
    ends={
        Property(name="Method321", type=gast_variables_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_variables_Property", type=Method_, multiplicity=Multiplicity(0, 1))
    }
)
getter322: BinaryAssociation = BinaryAssociation(
    name="getter322",
    ends={
        Property(name="Method324", type=gast_variables_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_variables_Property323", type=Method_, multiplicity=Multiplicity(0, 1))
    }
)
surroundingPackage325: BinaryAssociation = BinaryAssociation(
    name="surroundingPackage325",
    ends={
        Property(name="Package326", type=gast_variables_GlobalVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="globalVariables", type=Package, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_gast_statements_ExceptionHandler_Statement = Generalization(general=Statement, specific=gast_statements_ExceptionHandler)
gen_gast_statements_Statement_SourceEntity = Generalization(general=SourceEntity, specific=gast_statements_Statement)
gen_gast_statements_LoopStatement_Statement = Generalization(general=Statement, specific=gast_statements_LoopStatement)
gen_gast_statements_BlockStatement_Statement = Generalization(general=Statement, specific=gast_statements_BlockStatement)
gen_gast_statements_Branch_SourceEntity = Generalization(general=SourceEntity, specific=gast_statements_Branch)
gen_gast_statements_GASTExpression_SourceEntity = Generalization(general=SourceEntity, specific=gast_statements_GASTExpression)
gen_gast_statements_BranchStatement_Statement = Generalization(general=Statement, specific=gast_statements_BranchStatement)
gen_gast_statements_Methods_BlockStatement = Generalization(general=BlockStatement, specific=gast_statements_Methods)
gen_gast_core_BasePath_ModelElement = Generalization(general=ModelElement, specific=gast_core_BasePath)
gen_gast_core_ModelElement_Identifier = Generalization(general=Identifier, specific=gast_core_ModelElement)
gen_gast_statements_CatchBlock_BlockStatement = Generalization(general=BlockStatement, specific=gast_statements_CatchBlock)
gen_gast_statements_JumpStatement_Statement = Generalization(general=Statement, specific=gast_statements_JumpStatement)
gen_gast_statements_SimpleStatement_Statement = Generalization(general=Statement, specific=gast_statements_SimpleStatement)
gen_gast_core_NamedModelElement_ModelElement = Generalization(general=ModelElement, specific=gast_core_NamedModelElement)
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
gen_gast_accesses_CompositeAccess_BaseAccess = Generalization(general=BaseAccess, specific=gast_accesses_CompositeAccess)
gen_gast_accesses_BaseAccess_SourceEntity = Generalization(general=SourceEntity, specific=gast_accesses_BaseAccess)
gen_gast_accesses_DeclarationTypeAccess_TypeAccess = Generalization(general=TypeAccess, specific=gast_accesses_DeclarationTypeAccess)
gen_gast_accesses_ThrowTypeAccess_TypeAccess = Generalization(general=TypeAccess, specific=gast_accesses_ThrowTypeAccess)
gen_gast_accesses_DelegateAccess_FunctionAccess = Generalization(general=FunctionAccess, specific=gast_accesses_DelegateAccess)
gen_gast_accesses_InheritanceTypeAccess_TypeAccess = Generalization(general=TypeAccess, specific=gast_accesses_InheritanceTypeAccess)
gen_gast_accesses_VariableAccess_Access = Generalization(general=Access, specific=gast_accesses_VariableAccess)
gen_gast_accesses_RunTimeTypeAccess_TypeAccess = Generalization(general=TypeAccess, specific=gast_accesses_RunTimeTypeAccess)
gen_gast_accesses_SelfAccess_VariableAccess = Generalization(general=VariableAccess, specific=gast_accesses_SelfAccess)
gen_gast_accesses_StaticTypeAccess_TypeAccess = Generalization(general=TypeAccess, specific=gast_accesses_StaticTypeAccess)
gen_gast_accesses_FunctionAccess_Access = Generalization(general=Access, specific=gast_accesses_FunctionAccess)
gen_gast_functions_Delegate_functions_Function = Generalization(general=functions_Function, specific=gast_functions_Delegate)
gen_gast_functions_Delegate_types_Member = Generalization(general=types_Member, specific=gast_functions_Delegate)
gen_gast_functions_Delegate_types_GASTType = Generalization(general=types_GASTType, specific=gast_functions_Delegate)
gen_gast_functions_Constructor_functions_Function = Generalization(general=functions_Function, specific=gast_functions_Constructor)
gen_gast_functions_Constructor_types_Member = Generalization(general=types_Member, specific=gast_functions_Constructor)
gen_gast_accesses_PropertyAccess_VariableAccess = Generalization(general=VariableAccess, specific=gast_accesses_PropertyAccess)
gen_gast_accesses_Access_BaseAccess = Generalization(general=BaseAccess, specific=gast_accesses_Access)
gen_gast_functions_Destructor_functions_Function = Generalization(general=functions_Function, specific=gast_functions_Destructor)
gen_gast_functions_Destructor_types_Member = Generalization(general=types_Member, specific=gast_functions_Destructor)
gen_gast_functions_GenericFunction_functions_GlobalFunction = Generalization(general=functions_GlobalFunction, specific=gast_functions_GenericFunction)
gen_gast_functions_GenericFunction_core_GenericEntity = Generalization(general=core_GenericEntity, specific=gast_functions_GenericFunction)
gen_gast_functions_GlobalFunction_Function = Generalization(general=Function, specific=gast_functions_GlobalFunction)
gen_gast_functions_Method_functions_Function = Generalization(general=functions_Function, specific=gast_functions_Method)
gen_gast_functions_Method_types_Member = Generalization(general=types_Member, specific=gast_functions_Method)
gen_gast_functions_GenericMethod_functions_Method = Generalization(general=functions_Method, specific=gast_functions_GenericMethod)
gen_gast_functions_GenericMethod_core_GenericEntity = Generalization(general=core_GenericEntity, specific=gast_functions_GenericMethod)
gen_gast_functions_GenericConstructor_functions_Constructor = Generalization(general=functions_Constructor, specific=gast_functions_GenericConstructor)
gen_gast_functions_GenericConstructor_core_GenericEntity = Generalization(general=core_GenericEntity, specific=gast_functions_GenericConstructor)
gen_gast_functions_Function_core_NamedModelElement = Generalization(general=core_NamedModelElement, specific=gast_functions_Function)
gen_gast_functions_Function_core_SourceEntity = Generalization(general=core_SourceEntity, specific=gast_functions_Function)
gen_gast_variables_Variable_core_NamedModelElement = Generalization(general=core_NamedModelElement, specific=gast_variables_Variable)
gen_gast_variables_Variable_core_SourceEntity = Generalization(general=core_SourceEntity, specific=gast_variables_Variable)
gen_gast_variables_CatchParameter_Variable = Generalization(general=Variable, specific=gast_variables_CatchParameter)
gen_gast_variables_Field_types_Member = Generalization(general=types_Member, specific=gast_variables_Field)
gen_gast_variables_Field_variables_Variable = Generalization(general=variables_Variable, specific=gast_variables_Field)
gen_gast_variables_LocalVariable_Variable = Generalization(general=Variable, specific=gast_variables_LocalVariable)
gen_gast_variables_Property_variables_Field = Generalization(general=variables_Field, specific=gast_variables_Property)
gen_gast_variables_Property_types_Member = Generalization(general=types_Member, specific=gast_variables_Property)
gen_gast_variables_FormalParameter_Variable = Generalization(general=Variable, specific=gast_variables_FormalParameter)
gen_gast_variables_GlobalVariable_Variable = Generalization(general=Variable, specific=gast_variables_GlobalVariable)

# Domain Model
domain_model = DomainModel(
    name="gast",
    types={gast_statements_ExceptionHandler, Statement, CatchBlock, BlockStatement, gast_statements_Statement, SourceEntity, BaseAccess, CloneInstance, gast_statements_LoopStatement, Branch, LoopStatement, gast_statements_BlockStatement, Function, gast_statements_Branch, GASTExpression, BranchStatement, gast_statements_GASTExpression, gast_statements_BranchStatement, gast_statements_GASTBehaviour, gast_statements_Methods, Exit, gast_statements_Exit, gast_core_BasePath, ModelElement, Root, Directory, gast_core_ModelElement, Identifier, gast_statements_CatchBlock, ModelAnnotation, CatchParameter, gast_statements_JumpStatement, gast_core_Identifier, gast_statements_SimpleStatement, gast_core_NamedModelElement, gast_core_Package, NamedModelElement, GASTClass, Access, Delegate, GlobalFunction, GlobalVariable, TypeAlias, gast_core_GenericEntity, TypeParameterClass, gast_core_Root, Package, Clone, StructuralAbstraction, GASTType, BasePath, gast_core_Directory, File, gast_core_File, gast_core_Position, gast_core_PackageAlias, gast_core_SourceEntity, Position, gast_annotations_Attribute, types_GASTClass, annotations_ModelAnnotation, gast_annotations_Clone, core_ModelElement, gast_annotations_CloneInstance, gast_annotations_StructuralAbstraction, core_NamedModelElement, gast_annotations_Comment, core_SourceEntity, gast_annotations_Subsystem, gast_annotations_Layer, gast_annotations_ModelAnnotation, gast_types_Reference, TypeDecorator, gast_types_TypeDecorator, gast_types_GASTType, gast_types_GASTArray, gast_types_TypeAlias, types_Member, types_TypeDecorator, gast_types_Member, Member, gast_types_TypeParameterClass, gast_types_GenericClass, core_GenericEntity, gast_types_GASTEnumeration, gast_types_GASTStruct, gast_types_GASTUnion, gast_types_GASTClass, types_GASTType, Constructor, Destructor, Field, Method_, Property_, gast_accesses_ParameterInstantiationTypeAccess, TypeAccess, gast_accesses_TypeAccess, gast_accesses_CastTypeAccess, gast_accesses_CompositeAccess, InheritanceTypeAccess, gast_accesses_BaseAccess, CompositeAccess, gast_accesses_DeclarationTypeAccess, Variable, gast_accesses_ThrowTypeAccess, gast_accesses_DelegateAccess, FunctionAccess, gast_accesses_InheritanceTypeAccess, gast_accesses_VariableAccess, gast_accesses_RunTimeTypeAccess, gast_accesses_SelfAccess, VariableAccess, gast_accesses_StaticTypeAccess, gast_accesses_FunctionAccess, gast_functions_Delegate, functions_Function, gast_functions_Constructor, gast_accesses_PropertyAccess, gast_accesses_Access, gast_functions_Destructor, gast_functions_GenericFunction, functions_GlobalFunction, gast_functions_GlobalFunction, gast_functions_Method, gast_functions_GenericMethod, functions_Method, gast_functions_GenericConstructor, functions_Constructor, gast_functions_Function, DeclarationTypeAccess, LocalVariable, ThrowTypeAccess, FormalParameter, gast_variables_Variable, gast_variables_CatchParameter, gast_variables_Field, variables_Variable, gast_variables_LocalVariable, gast_variables_Property, variables_Field, gast_variables_FormalParameter, gast_variables_GlobalVariable, LoopStatementKind, JumpStatementKind, Status, Visibilities, GlobalFunctionKind},
    associations={catchBlocks0, finallyBlock1, guardedBlock3, accesses6, cloneInstance7, blockstatement8, surroundingStatement11, breakConditionExpression30, initExpression32, branch12, loopstatement13, cfPre14, cfNext17, statements20, surroundingFunction22, conditionExpression24, branchstatement25, statement26, branches28, expression43, blockstatement45, incrementExpression35, exit47, body38, root48, directories49, annotations50, catchParameter40, expression41, allLocalClasses51, allInnerClasses52, allNormalClasses55, allInterfaces58, allAccesses61, delegates63, globalFunctions64, globalVariables66, root68, classes70, surroundingPackage75, allAccessedPackages77, typeAliases80, typeParameters82, allAccesses83, allInnerClasses85, allInterfaces88, allLocalClasses91, allNormalClasses94, subPackages73, globalVariables99, packages102, clones104, structuralAbstractions106, types108, danglingModelElements110, basePaths113, allModelElements97, subDirectory118, parentDirectory120, files122, basePath123, root125, importedTypes127, globalFunctions115, globalVariables133, globalFunctions136, importedGlobalFunctions139, importedGlobalVariables142, importedPackages145, includedFiles148, directory151, types130, sourceFile153, assembly155, sourceentity158, aliasedPackage159, position161, cloneInstances162, root164, statements166, referencedType170, decoratedType172, undecoratedType174, clone168, baseType177, aliasedType179, surroundingClass181, surroundingPackage183, overriddenMember185, typeBounds186, innerTypeAliases188, constructors193, destructors195, fields197, methods199, surroundingFunction201, surroundingPackage203, superTypes205, innerClasses207, surroundingClass210, innerDelegates190, self214, friendClasses217, gastClass219, friendFunctions221, property224, allAccesses226, allAccessedClasses229, targetType232, typeArguments234, inheritanceTypeAccesses212, parentStatement239, surroundingStatement241, surroundingClass243, surroundingFunction246, surroundingCompositeAccess249, function251, surroundingVariable253, accessedFunctions254, accessedDelegate256, accesses237, typeArguments259, targetFunction261, targetVariable264, accessedClass266, accessedTarget268, superClass271, invocations273, surroundingClass276, surroundingPackage278, surroundingClass280, surroundingClass282, surroundingPackage284, root286, surroundingProperty289, surroundingClass291, returnTypeDeclaration293, localVariables295, allStatements297, throwTypeAccesses299, accesses301, body304, localClasses307, surroundingFunction310, formalParameters294, type312, typeDeclaration314, surroundingClass316, surroundingFunction318, setter320, getter322, surroundingPackage325},
    generalizations={gen_gast_statements_ExceptionHandler_Statement, gen_gast_statements_Statement_SourceEntity, gen_gast_statements_LoopStatement_Statement, gen_gast_statements_BlockStatement_Statement, gen_gast_statements_Branch_SourceEntity, gen_gast_statements_GASTExpression_SourceEntity, gen_gast_statements_BranchStatement_Statement, gen_gast_statements_Methods_BlockStatement, gen_gast_core_BasePath_ModelElement, gen_gast_core_ModelElement_Identifier, gen_gast_statements_CatchBlock_BlockStatement, gen_gast_statements_JumpStatement_Statement, gen_gast_statements_SimpleStatement_Statement, gen_gast_core_NamedModelElement_ModelElement, gen_gast_core_Package_NamedModelElement, gen_gast_core_GenericEntity_ModelElement, gen_gast_core_Root_ModelElement, gen_gast_core_Directory_NamedModelElement, gen_gast_core_File_NamedModelElement, gen_gast_core_PackageAlias_Package, gen_gast_core_SourceEntity_ModelElement, gen_gast_annotations_Attribute_types_GASTClass, gen_gast_annotations_Attribute_annotations_ModelAnnotation, gen_gast_annotations_Clone_core_ModelElement, gen_gast_annotations_Clone_annotations_ModelAnnotation, gen_gast_annotations_CloneInstance_core_ModelElement, gen_gast_annotations_CloneInstance_annotations_ModelAnnotation, gen_gast_annotations_StructuralAbstraction_core_NamedModelElement, gen_gast_annotations_StructuralAbstraction_annotations_ModelAnnotation, gen_gast_annotations_Comment_core_SourceEntity, gen_gast_annotations_Comment_annotations_ModelAnnotation, gen_gast_annotations_Subsystem_StructuralAbstraction, gen_gast_annotations_Layer_StructuralAbstraction, gen_gast_types_Reference_TypeDecorator, gen_gast_types_TypeDecorator_GASTType, gen_gast_types_GASTType_NamedModelElement, gen_gast_types_GASTArray_TypeDecorator, gen_gast_types_TypeAlias_types_Member, gen_gast_types_TypeAlias_types_TypeDecorator, gen_gast_types_Member_SourceEntity, gen_gast_types_TypeParameterClass_GASTClass, gen_gast_types_GenericClass_types_GASTClass, gen_gast_types_GenericClass_core_GenericEntity, gen_gast_types_GASTEnumeration_GASTClass, gen_gast_types_GASTStruct_GASTClass, gen_gast_types_GASTUnion_GASTClass, gen_gast_types_GASTClass_types_Member, gen_gast_types_GASTClass_types_GASTType, gen_gast_accesses_ParameterInstantiationTypeAccess_TypeAccess, gen_gast_accesses_TypeAccess_Access, gen_gast_accesses_CastTypeAccess_TypeAccess, gen_gast_accesses_CompositeAccess_BaseAccess, gen_gast_accesses_BaseAccess_SourceEntity, gen_gast_accesses_DeclarationTypeAccess_TypeAccess, gen_gast_accesses_ThrowTypeAccess_TypeAccess, gen_gast_accesses_DelegateAccess_FunctionAccess, gen_gast_accesses_InheritanceTypeAccess_TypeAccess, gen_gast_accesses_VariableAccess_Access, gen_gast_accesses_RunTimeTypeAccess_TypeAccess, gen_gast_accesses_SelfAccess_VariableAccess, gen_gast_accesses_StaticTypeAccess_TypeAccess, gen_gast_accesses_FunctionAccess_Access, gen_gast_functions_Delegate_functions_Function, gen_gast_functions_Delegate_types_Member, gen_gast_functions_Delegate_types_GASTType, gen_gast_functions_Constructor_functions_Function, gen_gast_functions_Constructor_types_Member, gen_gast_accesses_PropertyAccess_VariableAccess, gen_gast_accesses_Access_BaseAccess, gen_gast_functions_Destructor_functions_Function, gen_gast_functions_Destructor_types_Member, gen_gast_functions_GenericFunction_functions_GlobalFunction, gen_gast_functions_GenericFunction_core_GenericEntity, gen_gast_functions_GlobalFunction_Function, gen_gast_functions_Method_functions_Function, gen_gast_functions_Method_types_Member, gen_gast_functions_GenericMethod_functions_Method, gen_gast_functions_GenericMethod_core_GenericEntity, gen_gast_functions_GenericConstructor_functions_Constructor, gen_gast_functions_GenericConstructor_core_GenericEntity, gen_gast_functions_Function_core_NamedModelElement, gen_gast_functions_Function_core_SourceEntity, gen_gast_variables_Variable_core_NamedModelElement, gen_gast_variables_Variable_core_SourceEntity, gen_gast_variables_CatchParameter_Variable, gen_gast_variables_Field_types_Member, gen_gast_variables_Field_variables_Variable, gen_gast_variables_LocalVariable_Variable, gen_gast_variables_Property_variables_Field, gen_gast_variables_Property_types_Member, gen_gast_variables_FormalParameter_Variable, gen_gast_variables_GlobalVariable_Variable},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)