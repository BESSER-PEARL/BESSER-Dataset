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
Branch = Class(name="Branch")
gast_statements_ExceptionHandler = Class(name="gast_statements_ExceptionHandler")
Statement = Class(name="Statement")
CatchBlock = Class(name="CatchBlock")
BlockStatement = Class(name="BlockStatement")
gast_statements_Statement = Class(name="gast_statements_Statement", is_abstract=True)
SourceEntity = Class(name="SourceEntity")
BaseAccess = Class(name="BaseAccess")
CloneInstance = Class(name="CloneInstance")
LoopStatement = Class(name="LoopStatement")
gast_statements_BlockStatement = Class(name="gast_statements_BlockStatement")
Function = Class(name="Function")
gast_statements_Branch = Class(name="gast_statements_Branch")
GASTExpression = Class(name="GASTExpression")
BranchStatement = Class(name="BranchStatement")
gast_statements_GASTExpression = Class(name="gast_statements_GASTExpression", is_abstract=True)
gast_statements_BranchStatement = Class(name="gast_statements_BranchStatement")
gast_statements_LoopStatement = Class(name="gast_statements_LoopStatement")
gast_statements_CatchBlock = Class(name="gast_statements_CatchBlock")
CatchParameter = Class(name="CatchParameter")
gast_statements_JumpStatement = Class(name="gast_statements_JumpStatement")
gast_statements_SimpleStatement = Class(name="gast_statements_SimpleStatement")
gast_statements_GASTBehaviour = Class(name="gast_statements_GASTBehaviour")
gast_core_BasePath = Class(name="gast_core_BasePath")
ModelElement = Class(name="ModelElement")
Root = Class(name="Root")
Directory = Class(name="Directory")
gast_core_ModelElement = Class(name="gast_core_ModelElement", is_abstract=True)
Identifier = Class(name="Identifier")
ModelAnnotation = Class(name="ModelAnnotation")
gast_core_Identifier = Class(name="gast_core_Identifier", is_abstract=True)
GlobalFunction = Class(name="GlobalFunction")
gast_core_NamedModelElement = Class(name="gast_core_NamedModelElement", is_abstract=True)
gast_core_Package = Class(name="gast_core_Package")
NamedModelElement = Class(name="NamedModelElement")
GASTClass = Class(name="GASTClass")
Access = Class(name="Access")
Delegate = Class(name="Delegate")
GlobalVariable = Class(name="GlobalVariable")
Package = Class(name="Package")
TypeAlias = Class(name="TypeAlias")
gast_core_GenericEntity = Class(name="gast_core_GenericEntity", is_abstract=True)
TypeParameterClass = Class(name="TypeParameterClass")
gast_core_Root = Class(name="gast_core_Root")
GASTType = Class(name="GASTType")
Clone = Class(name="Clone")
StructuralAbstraction = Class(name="StructuralAbstraction")
BasePath = Class(name="BasePath")
gast_core_Directory = Class(name="gast_core_Directory")
File = Class(name="File")
gast_core_File = Class(name="gast_core_File")
gast_annotations_Clone = Class(name="gast_annotations_Clone")
core_ModelElement = Class(name="core_ModelElement")
gast_core_Position = Class(name="gast_core_Position")
gast_core_PackageAlias = Class(name="gast_core_PackageAlias")
gast_core_SourceEntity = Class(name="gast_core_SourceEntity", is_abstract=True)
Position = Class(name="Position")
gast_annotations_Attribute = Class(name="gast_annotations_Attribute")
types_GASTClass = Class(name="types_GASTClass")
annotations_ModelAnnotation = Class(name="annotations_ModelAnnotation")
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
TypeAccess = Class(name="TypeAccess")
InheritanceTypeAccess = Class(name="InheritanceTypeAccess")
Property_ = Class(name="Property")
gast_accesses_ParameterInstantiationTypeAccess = Class(name="gast_accesses_ParameterInstantiationTypeAccess")
gast_accesses_TypeAccess = Class(name="gast_accesses_TypeAccess", is_abstract=True)
gast_accesses_CastTypeAccess = Class(name="gast_accesses_CastTypeAccess")
gast_accesses_CompositeAccess = Class(name="gast_accesses_CompositeAccess")
gast_accesses_BaseAccess = Class(name="gast_accesses_BaseAccess", is_abstract=True)
CompositeAccess = Class(name="CompositeAccess")
gast_accesses_DeclarationTypeAccess = Class(name="gast_accesses_DeclarationTypeAccess")
Variable = Class(name="Variable")
gast_accesses_ThrowTypeAccess = Class(name="gast_accesses_ThrowTypeAccess")
gast_accesses_DelegateAccess = Class(name="gast_accesses_DelegateAccess")
FunctionAccess = Class(name="FunctionAccess")
gast_accesses_FunctionAccess = Class(name="gast_accesses_FunctionAccess")
gast_accesses_InheritanceTypeAccess = Class(name="gast_accesses_InheritanceTypeAccess")
gast_accesses_VariableAccess = Class(name="gast_accesses_VariableAccess")
gast_accesses_RunTimeTypeAccess = Class(name="gast_accesses_RunTimeTypeAccess")
gast_accesses_SelfAccess = Class(name="gast_accesses_SelfAccess")
VariableAccess = Class(name="VariableAccess")
gast_functions_Constructor = Class(name="gast_functions_Constructor")
gast_accesses_StaticTypeAccess = Class(name="gast_accesses_StaticTypeAccess")
gast_accesses_PropertyAccess = Class(name="gast_accesses_PropertyAccess")
gast_accesses_Access = Class(name="gast_accesses_Access", is_abstract=True)
gast_functions_Delegate = Class(name="gast_functions_Delegate")
functions_Function = Class(name="functions_Function")
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
FormalParameter = Class(name="FormalParameter")
LocalVariable = Class(name="LocalVariable")
ThrowTypeAccess = Class(name="ThrowTypeAccess")
gast_variables_Property = Class(name="gast_variables_Property")
variables_Field = Class(name="variables_Field")
gast_variables_FormalParameter = Class(name="gast_variables_FormalParameter")
gast_variables_Variable = Class(name="gast_variables_Variable", is_abstract=True)
gast_variables_CatchParameter = Class(name="gast_variables_CatchParameter")
gast_variables_Field = Class(name="gast_variables_Field")
variables_Variable = Class(name="variables_Variable")
gast_variables_LocalVariable = Class(name="gast_variables_LocalVariable")
gast_variables_GlobalVariable = Class(name="gast_variables_GlobalVariable")

# Branch class attributes and methods

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
gast_statements_Statement.attributes={gast_statements_Statement_maximumNestingLevel, gast_statements_Statement_numberOfEdgesInCFG, gast_statements_Statement_numberOfComments, gast_statements_Statement_linesOfCode, gast_statements_Statement_numberOfStatements, gast_statements_Statement_numberOfNodesInCFG}

# SourceEntity class attributes and methods

# BaseAccess class attributes and methods

# CloneInstance class attributes and methods

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

# Directory class attributes and methods

# gast_core_ModelElement class attributes and methods
gast_core_ModelElement_status: Property = Property(name="status", type=StringType)
gast_core_ModelElement_sissyId: Property = Property(name="sissyId", type=IntegerType)
gast_core_ModelElement.attributes={gast_core_ModelElement_status, gast_core_ModelElement_sissyId}

# Identifier class attributes and methods

# ModelAnnotation class attributes and methods

# gast_core_Identifier class attributes and methods
gast_core_Identifier_id: Property = Property(name="id", type=StringType)
gast_core_Identifier_m_idHasToBeUnique: Method = Method(name="idHasToBeUnique", parameters={Parameter(name='gast_diagnostics', type=StringType), Parameter(name='gast_context', type=StringType)}, type=BooleanType)
gast_core_Identifier.attributes={gast_core_Identifier_id}
gast_core_Identifier.methods={gast_core_Identifier_m_idHasToBeUnique}

# GlobalFunction class attributes and methods

# gast_core_NamedModelElement class attributes and methods
gast_core_NamedModelElement_simpleName: Property = Property(name="simpleName", type=StringType)
gast_core_NamedModelElement.attributes={gast_core_NamedModelElement_simpleName}

# gast_core_Package class attributes and methods
gast_core_Package_linesOfComments: Property = Property(name="linesOfComments", type=IntegerType)
gast_core_Package_linesOfCode: Property = Property(name="linesOfCode", type=IntegerType)
gast_core_Package_qualifiedName: Property = Property(name="qualifiedName", type=StringType)
gast_core_Package.attributes={gast_core_Package_linesOfCode, gast_core_Package_linesOfComments, gast_core_Package_qualifiedName}

# NamedModelElement class attributes and methods

# GASTClass class attributes and methods

# Access class attributes and methods

# Delegate class attributes and methods

# GlobalVariable class attributes and methods

# Package class attributes and methods

# TypeAlias class attributes and methods

# gast_core_GenericEntity class attributes and methods

# TypeParameterClass class attributes and methods

# gast_core_Root class attributes and methods
gast_core_Root_linesOfComments: Property = Property(name="linesOfComments", type=IntegerType)
gast_core_Root_linesOfCode: Property = Property(name="linesOfCode", type=IntegerType)
gast_core_Root_m_getPackageByName: Method = Method(name="getPackageByName", parameters={Parameter(name='gast_name', type=StringType)}, type=StringType)
gast_core_Root_m_getPackageByQualifiedName: Method = Method(name="getPackageByQualifiedName", parameters={Parameter(name='gast_qualifiedName', type=StringType)}, type=StringType)
gast_core_Root.attributes={gast_core_Root_linesOfComments, gast_core_Root_linesOfCode}
gast_core_Root.methods={gast_core_Root_m_getPackageByQualifiedName, gast_core_Root_m_getPackageByName}

# GASTType class attributes and methods

# Clone class attributes and methods

# StructuralAbstraction class attributes and methods

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
gast_core_File.attributes={gast_core_File_fileSystemPath, gast_core_File_sourceFile, gast_core_File_linesOfCode, gast_core_File_fullQualifiedPath, gast_core_File_size, gast_core_File_assemblyFile}

# gast_annotations_Clone class attributes and methods

# core_ModelElement class attributes and methods

# gast_core_Position class attributes and methods
gast_core_Position_endColumn: Property = Property(name="endColumn", type=IntegerType)
gast_core_Position_startColumn: Property = Property(name="startColumn", type=IntegerType)
gast_core_Position_endLine: Property = Property(name="endLine", type=IntegerType)
gast_core_Position_startLine: Property = Property(name="startLine", type=IntegerType)
gast_core_Position_m_EitherAssemblyFileOrSourceFileSet: Method = Method(name="EitherAssemblyFileOrSourceFileSet", parameters={Parameter(name='gast_diagnostics', type=StringType), Parameter(name='gast_context', type=StringType)}, type=BooleanType)
gast_core_Position.attributes={gast_core_Position_startColumn, gast_core_Position_endColumn, gast_core_Position_startLine, gast_core_Position_endLine}
gast_core_Position.methods={gast_core_Position_m_EitherAssemblyFileOrSourceFileSet}

# gast_core_PackageAlias class attributes and methods

# gast_core_SourceEntity class attributes and methods

# Position class attributes and methods

# gast_annotations_Attribute class attributes and methods

# types_GASTClass class attributes and methods

# annotations_ModelAnnotation class attributes and methods

# gast_annotations_CloneInstance class attributes and methods

# gast_annotations_StructuralAbstraction class attributes and methods

# core_NamedModelElement class attributes and methods

# gast_annotations_Comment class attributes and methods
gast_annotations_Comment_todo: Property = Property(name="todo", type=BooleanType)
gast_annotations_Comment_formal: Property = Property(name="formal", type=BooleanType)
gast_annotations_Comment_todoCount: Property = Property(name="todoCount", type=IntegerType)
gast_annotations_Comment_texts: Property = Property(name="texts", type=StringType)
gast_annotations_Comment_m_OCLtodo: Method = Method(name="OCLtodo", parameters={Parameter(name='gast_context', type=StringType), Parameter(name='gast_diagnostics', type=StringType)}, type=BooleanType)
gast_annotations_Comment.attributes={gast_annotations_Comment_formal, gast_annotations_Comment_texts, gast_annotations_Comment_todoCount, gast_annotations_Comment_todo}
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
gast_types_Member.attributes={gast_types_Member_visibility, gast_types_Member_abstract, gast_types_Member_typeParameterClassMember, gast_types_Member_introspectable, gast_types_Member_static, gast_types_Member_virtual, gast_types_Member_internal, gast_types_Member_final, gast_types_Member_override, gast_types_Member_extern}
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
gast_types_GASTClass.attributes={gast_types_GASTClass_local, gast_types_GASTClass_primitive, gast_types_GASTClass_linesOfComments, gast_types_GASTClass_anonymous, gast_types_GASTClass_interface, gast_types_GASTClass_inner}

# types_GASTType class attributes and methods

# Constructor class attributes and methods

# Destructor class attributes and methods

# Field class attributes and methods

# Method class attributes and methods

# TypeAccess class attributes and methods

# InheritanceTypeAccess class attributes and methods

# Property class attributes and methods

# gast_accesses_ParameterInstantiationTypeAccess class attributes and methods

# gast_accesses_TypeAccess class attributes and methods

# gast_accesses_CastTypeAccess class attributes and methods

# gast_accesses_CompositeAccess class attributes and methods

# gast_accesses_BaseAccess class attributes and methods

# CompositeAccess class attributes and methods

# gast_accesses_DeclarationTypeAccess class attributes and methods

# Variable class attributes and methods

# gast_accesses_ThrowTypeAccess class attributes and methods
gast_accesses_ThrowTypeAccess_declared: Property = Property(name="declared", type=BooleanType)
gast_accesses_ThrowTypeAccess.attributes={gast_accesses_ThrowTypeAccess_declared}

# gast_accesses_DelegateAccess class attributes and methods

# FunctionAccess class attributes and methods

# gast_accesses_FunctionAccess class attributes and methods

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

# gast_functions_Constructor class attributes and methods
gast_functions_Constructor_initializer: Property = Property(name="initializer", type=BooleanType)
gast_functions_Constructor.attributes={gast_functions_Constructor_initializer}

# gast_accesses_StaticTypeAccess class attributes and methods

# gast_accesses_PropertyAccess class attributes and methods

# gast_accesses_Access class attributes and methods

# gast_functions_Delegate class attributes and methods
gast_functions_Delegate_innerDelegate: Property = Property(name="innerDelegate", type=BooleanType)
gast_functions_Delegate.attributes={gast_functions_Delegate_innerDelegate}

# functions_Function class attributes and methods

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
gast_functions_Function.attributes={gast_functions_Function_numberOfNodesInCFG, gast_functions_Function_linesOfCode, gast_functions_Function_numberOfEdgesInCFG, gast_functions_Function_maximumNestingLevel, gast_functions_Function_numberOfStatements, gast_functions_Function_linesOfComments, gast_functions_Function_operator}

# DeclarationTypeAccess class attributes and methods

# FormalParameter class attributes and methods

# LocalVariable class attributes and methods

# ThrowTypeAccess class attributes and methods

# gast_variables_Property class attributes and methods

# variables_Field class attributes and methods

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
initExpression26: BinaryAssociation = BinaryAssociation(
    name="initExpression26",
    ends={
        Property(name="GASTExpression28", type=gast_statements_LoopStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_statements_LoopStatement27", type=GASTExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
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
statements14: BinaryAssociation = BinaryAssociation(
    name="statements14",
    ends={
        Property(name="Statement15", type=gast_statements_BlockStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="blockstatement", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
surroundingFunction16: BinaryAssociation = BinaryAssociation(
    name="surroundingFunction16",
    ends={
        Property(name="Function", type=gast_statements_BlockStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="body17", type=Function, multiplicity=Multiplicity(0, 1))
    }
)
conditionExpression18: BinaryAssociation = BinaryAssociation(
    name="conditionExpression18",
    ends={
        Property(name="GASTExpression", type=gast_statements_Branch, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_statements_Branch", type=GASTExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
branchstatement19: BinaryAssociation = BinaryAssociation(
    name="branchstatement19",
    ends={
        Property(name="BranchStatement", type=gast_statements_Branch, multiplicity=Multiplicity(1, 1)),
        Property(name="branches", type=BranchStatement, multiplicity=Multiplicity(1, 1))
    }
)
statement20: BinaryAssociation = BinaryAssociation(
    name="statement20",
    ends={
        Property(name="Statement21", type=gast_statements_Branch, multiplicity=Multiplicity(1, 1)),
        Property(name="branch", type=Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
branches22: BinaryAssociation = BinaryAssociation(
    name="branches22",
    ends={
        Property(name="Branch23", type=gast_statements_BranchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="branchstatement", type=Branch, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
breakConditionExpression24: BinaryAssociation = BinaryAssociation(
    name="breakConditionExpression24",
    ends={
        Property(name="GASTExpression25", type=gast_statements_LoopStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_statements_LoopStatement", type=GASTExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
blockstatement39: BinaryAssociation = BinaryAssociation(
    name="blockstatement39",
    ends={
        Property(name="BlockStatement40", type=gast_statements_GASTBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_statements_GASTBehaviour", type=BlockStatement, multiplicity=Multiplicity(1, 1))
    }
)
incrementExpression29: BinaryAssociation = BinaryAssociation(
    name="incrementExpression29",
    ends={
        Property(name="GASTExpression31", type=gast_statements_LoopStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_statements_LoopStatement30", type=GASTExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body32: BinaryAssociation = BinaryAssociation(
    name="body32",
    ends={
        Property(name="Statement33", type=gast_statements_LoopStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="loopstatement", type=Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
catchParameter34: BinaryAssociation = BinaryAssociation(
    name="catchParameter34",
    ends={
        Property(name="CatchParameter", type=gast_statements_CatchBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_statements_CatchBlock", type=CatchParameter, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression35: BinaryAssociation = BinaryAssociation(
    name="expression35",
    ends={
        Property(name="GASTExpression36", type=gast_statements_JumpStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_statements_JumpStatement", type=GASTExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression37: BinaryAssociation = BinaryAssociation(
    name="expression37",
    ends={
        Property(name="GASTExpression38", type=gast_statements_SimpleStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_statements_SimpleStatement", type=GASTExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
root41: BinaryAssociation = BinaryAssociation(
    name="root41",
    ends={
        Property(name="Root", type=gast_core_BasePath, multiplicity=Multiplicity(1, 1)),
        Property(name="basePaths", type=Root, multiplicity=Multiplicity(1, 1))
    }
)
directories42: BinaryAssociation = BinaryAssociation(
    name="directories42",
    ends={
        Property(name="Directory", type=gast_core_BasePath, multiplicity=Multiplicity(1, 1)),
        Property(name="basePath", type=Directory, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotations43: BinaryAssociation = BinaryAssociation(
    name="annotations43",
    ends={
        Property(name="ModelAnnotation", type=gast_core_ModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_ModelElement", type=ModelAnnotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
allLocalClasses44: BinaryAssociation = BinaryAssociation(
    name="allLocalClasses44",
    ends={
        Property(name="GASTClass", type=gast_core_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_Package", type=GASTClass, multiplicity=Multiplicity(0, 9999))
    }
)
allInnerClasses45: BinaryAssociation = BinaryAssociation(
    name="allInnerClasses45",
    ends={
        Property(name="GASTClass47", type=gast_core_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_Package46", type=GASTClass, multiplicity=Multiplicity(0, 9999))
    }
)
allNormalClasses48: BinaryAssociation = BinaryAssociation(
    name="allNormalClasses48",
    ends={
        Property(name="GASTClass50", type=gast_core_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_Package49", type=GASTClass, multiplicity=Multiplicity(0, 9999))
    }
)
allInterfaces51: BinaryAssociation = BinaryAssociation(
    name="allInterfaces51",
    ends={
        Property(name="GASTClass53", type=gast_core_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_Package52", type=GASTClass, multiplicity=Multiplicity(0, 9999))
    }
)
allAccesses54: BinaryAssociation = BinaryAssociation(
    name="allAccesses54",
    ends={
        Property(name="Access", type=gast_core_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_Package55", type=Access, multiplicity=Multiplicity(0, 9999))
    }
)
delegates56: BinaryAssociation = BinaryAssociation(
    name="delegates56",
    ends={
        Property(name="Delegate", type=gast_core_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="surroundingPackage", type=Delegate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
globalFunctions57: BinaryAssociation = BinaryAssociation(
    name="globalFunctions57",
    ends={
        Property(name="GlobalFunction", type=gast_core_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="surroundingPackage58", type=GlobalFunction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
globalVariables59: BinaryAssociation = BinaryAssociation(
    name="globalVariables59",
    ends={
        Property(name="GlobalVariable", type=gast_core_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="surroundingPackage60", type=GlobalVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
root61: BinaryAssociation = BinaryAssociation(
    name="root61",
    ends={
        Property(name="Root62", type=gast_core_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="packages", type=Root, multiplicity=Multiplicity(0, 1))
    }
)
classes63: BinaryAssociation = BinaryAssociation(
    name="classes63",
    ends={
        Property(name="GASTClass65", type=gast_core_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="surroundingPackage64", type=GASTClass, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subPackages66: BinaryAssociation = BinaryAssociation(
    name="subPackages66",
    ends={
        Property(name="Package", type=gast_core_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="surroundingPackage67", type=Package, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
surroundingPackage68: BinaryAssociation = BinaryAssociation(
    name="surroundingPackage68",
    ends={
        Property(name="Package69", type=gast_core_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="subPackages", type=Package, multiplicity=Multiplicity(0, 1))
    }
)
allAccessedPackages70: BinaryAssociation = BinaryAssociation(
    name="allAccessedPackages70",
    ends={
        Property(name="Package72", type=gast_core_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_Package71", type=Package, multiplicity=Multiplicity(0, 9999))
    }
)
typeAliases73: BinaryAssociation = BinaryAssociation(
    name="typeAliases73",
    ends={
        Property(name="TypeAlias", type=gast_core_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="surroundingPackage74", type=TypeAlias, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeParameters75: BinaryAssociation = BinaryAssociation(
    name="typeParameters75",
    ends={
        Property(name="TypeParameterClass", type=gast_core_GenericEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_GenericEntity", type=TypeParameterClass, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
allAccesses76: BinaryAssociation = BinaryAssociation(
    name="allAccesses76",
    ends={
        Property(name="Access77", type=gast_core_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_Root", type=Access, multiplicity=Multiplicity(0, 9999))
    }
)
allInnerClasses78: BinaryAssociation = BinaryAssociation(
    name="allInnerClasses78",
    ends={
        Property(name="GASTClass80", type=gast_core_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_Root79", type=GASTClass, multiplicity=Multiplicity(0, 9999))
    }
)
allInterfaces81: BinaryAssociation = BinaryAssociation(
    name="allInterfaces81",
    ends={
        Property(name="GASTClass83", type=gast_core_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_Root82", type=GASTClass, multiplicity=Multiplicity(0, 9999))
    }
)
allLocalClasses84: BinaryAssociation = BinaryAssociation(
    name="allLocalClasses84",
    ends={
        Property(name="GASTClass86", type=gast_core_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_Root85", type=GASTClass, multiplicity=Multiplicity(0, 9999))
    }
)
allNormalClasses87: BinaryAssociation = BinaryAssociation(
    name="allNormalClasses87",
    ends={
        Property(name="GASTClass89", type=gast_core_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_Root88", type=GASTClass, multiplicity=Multiplicity(0, 9999))
    }
)
allModelElements90: BinaryAssociation = BinaryAssociation(
    name="allModelElements90",
    ends={
        Property(name="ModelElement", type=gast_core_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_Root91", type=ModelElement, multiplicity=Multiplicity(0, 9999))
    }
)
globalVariables92: BinaryAssociation = BinaryAssociation(
    name="globalVariables92",
    ends={
        Property(name="GlobalVariable94", type=gast_core_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_Root93", type=GlobalVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
packages95: BinaryAssociation = BinaryAssociation(
    name="packages95",
    ends={
        Property(name="Package96", type=gast_core_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="root", type=Package, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
clones97: BinaryAssociation = BinaryAssociation(
    name="clones97",
    ends={
        Property(name="Clone", type=gast_core_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="root98", type=Clone, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
structuralAbstractions99: BinaryAssociation = BinaryAssociation(
    name="structuralAbstractions99",
    ends={
        Property(name="StructuralAbstraction", type=gast_core_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_Root100", type=StructuralAbstraction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
types101: BinaryAssociation = BinaryAssociation(
    name="types101",
    ends={
        Property(name="GASTType", type=gast_core_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_Root102", type=GASTType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
danglingModelElements103: BinaryAssociation = BinaryAssociation(
    name="danglingModelElements103",
    ends={
        Property(name="ModelElement105", type=gast_core_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_Root104", type=ModelElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
basePaths106: BinaryAssociation = BinaryAssociation(
    name="basePaths106",
    ends={
        Property(name="BasePath", type=gast_core_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="root107", type=BasePath, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
globalFunctions108: BinaryAssociation = BinaryAssociation(
    name="globalFunctions108",
    ends={
        Property(name="GlobalFunction110", type=gast_core_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="root109", type=GlobalFunction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subDirectory111: BinaryAssociation = BinaryAssociation(
    name="subDirectory111",
    ends={
        Property(name="Directory112", type=gast_core_Directory, multiplicity=Multiplicity(1, 1)),
        Property(name="parentDirectory", type=Directory, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentDirectory113: BinaryAssociation = BinaryAssociation(
    name="parentDirectory113",
    ends={
        Property(name="Directory114", type=gast_core_Directory, multiplicity=Multiplicity(1, 1)),
        Property(name="subDirectory", type=Directory, multiplicity=Multiplicity(0, 1))
    }
)
files115: BinaryAssociation = BinaryAssociation(
    name="files115",
    ends={
        Property(name="File", type=gast_core_Directory, multiplicity=Multiplicity(1, 1)),
        Property(name="directory", type=File, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
basePath116: BinaryAssociation = BinaryAssociation(
    name="basePath116",
    ends={
        Property(name="BasePath117", type=gast_core_Directory, multiplicity=Multiplicity(1, 1)),
        Property(name="directories", type=BasePath, multiplicity=Multiplicity(0, 1))
    }
)
root118: BinaryAssociation = BinaryAssociation(
    name="root118",
    ends={
        Property(name="Root119", type=gast_core_File, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_File", type=Root, multiplicity=Multiplicity(1, 1))
    }
)
directory144: BinaryAssociation = BinaryAssociation(
    name="directory144",
    ends={
        Property(name="Directory145", type=gast_core_File, multiplicity=Multiplicity(1, 1)),
        Property(name="files", type=Directory, multiplicity=Multiplicity(1, 1))
    }
)
importedTypes120: BinaryAssociation = BinaryAssociation(
    name="importedTypes120",
    ends={
        Property(name="GASTType122", type=gast_core_File, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_File121", type=GASTType, multiplicity=Multiplicity(0, 9999))
    }
)
types123: BinaryAssociation = BinaryAssociation(
    name="types123",
    ends={
        Property(name="GASTType125", type=gast_core_File, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_File124", type=GASTType, multiplicity=Multiplicity(0, 9999))
    }
)
globalVariables126: BinaryAssociation = BinaryAssociation(
    name="globalVariables126",
    ends={
        Property(name="GlobalVariable128", type=gast_core_File, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_File127", type=GlobalVariable, multiplicity=Multiplicity(0, 9999))
    }
)
globalFunctions129: BinaryAssociation = BinaryAssociation(
    name="globalFunctions129",
    ends={
        Property(name="GlobalFunction131", type=gast_core_File, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_File130", type=GlobalFunction, multiplicity=Multiplicity(0, 9999))
    }
)
importedGlobalFunctions132: BinaryAssociation = BinaryAssociation(
    name="importedGlobalFunctions132",
    ends={
        Property(name="GlobalFunction134", type=gast_core_File, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_File133", type=GlobalFunction, multiplicity=Multiplicity(0, 9999))
    }
)
importedGlobalVariables135: BinaryAssociation = BinaryAssociation(
    name="importedGlobalVariables135",
    ends={
        Property(name="GlobalVariable137", type=gast_core_File, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_File136", type=GlobalVariable, multiplicity=Multiplicity(0, 9999))
    }
)
importedPackages138: BinaryAssociation = BinaryAssociation(
    name="importedPackages138",
    ends={
        Property(name="Package140", type=gast_core_File, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_File139", type=Package, multiplicity=Multiplicity(0, 9999))
    }
)
includedFiles141: BinaryAssociation = BinaryAssociation(
    name="includedFiles141",
    ends={
        Property(name="File143", type=gast_core_File, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_File142", type=File, multiplicity=Multiplicity(0, 9999))
    }
)
sourceFile146: BinaryAssociation = BinaryAssociation(
    name="sourceFile146",
    ends={
        Property(name="File147", type=gast_core_Position, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_Position", type=File, multiplicity=Multiplicity(0, 1))
    }
)
assembly148: BinaryAssociation = BinaryAssociation(
    name="assembly148",
    ends={
        Property(name="File150", type=gast_core_Position, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_Position149", type=File, multiplicity=Multiplicity(0, 1))
    }
)
sourceentity151: BinaryAssociation = BinaryAssociation(
    name="sourceentity151",
    ends={
        Property(name="SourceEntity", type=gast_core_Position, multiplicity=Multiplicity(1, 1)),
        Property(name="position", type=SourceEntity, multiplicity=Multiplicity(1, 1))
    }
)
aliasedPackage152: BinaryAssociation = BinaryAssociation(
    name="aliasedPackage152",
    ends={
        Property(name="Package153", type=gast_core_PackageAlias, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_PackageAlias", type=Package, multiplicity=Multiplicity(1, 1))
    }
)
position154: BinaryAssociation = BinaryAssociation(
    name="position154",
    ends={
        Property(name="Position", type=gast_core_SourceEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="sourceentity", type=Position, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cloneInstances155: BinaryAssociation = BinaryAssociation(
    name="cloneInstances155",
    ends={
        Property(name="CloneInstance156", type=gast_annotations_Clone, multiplicity=Multiplicity(1, 1)),
        Property(name="clone", type=CloneInstance, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
root157: BinaryAssociation = BinaryAssociation(
    name="root157",
    ends={
        Property(name="Root158", type=gast_annotations_Clone, multiplicity=Multiplicity(1, 1)),
        Property(name="clones", type=Root, multiplicity=Multiplicity(1, 1))
    }
)
statements159: BinaryAssociation = BinaryAssociation(
    name="statements159",
    ends={
        Property(name="Statement160", type=gast_annotations_CloneInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="cloneInstance", type=Statement, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
clone161: BinaryAssociation = BinaryAssociation(
    name="clone161",
    ends={
        Property(name="Clone162", type=gast_annotations_CloneInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="cloneInstances", type=Clone, multiplicity=Multiplicity(1, 1))
    }
)
referencedType163: BinaryAssociation = BinaryAssociation(
    name="referencedType163",
    ends={
        Property(name="GASTType164", type=gast_types_Reference, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_types_Reference", type=GASTType, multiplicity=Multiplicity(1, 1))
    }
)
decoratedType165: BinaryAssociation = BinaryAssociation(
    name="decoratedType165",
    ends={
        Property(name="GASTType166", type=gast_types_TypeDecorator, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_types_TypeDecorator", type=GASTType, multiplicity=Multiplicity(1, 1))
    }
)
undecoratedType167: BinaryAssociation = BinaryAssociation(
    name="undecoratedType167",
    ends={
        Property(name="GASTType169", type=gast_types_TypeDecorator, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_types_TypeDecorator168", type=GASTType, multiplicity=Multiplicity(1, 1))
    }
)
baseType170: BinaryAssociation = BinaryAssociation(
    name="baseType170",
    ends={
        Property(name="GASTType171", type=gast_types_GASTArray, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_types_GASTArray", type=GASTType, multiplicity=Multiplicity(1, 1))
    }
)
aliasedType172: BinaryAssociation = BinaryAssociation(
    name="aliasedType172",
    ends={
        Property(name="GASTType173", type=gast_types_TypeAlias, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_types_TypeAlias", type=GASTType, multiplicity=Multiplicity(1, 1))
    }
)
surroundingClass174: BinaryAssociation = BinaryAssociation(
    name="surroundingClass174",
    ends={
        Property(name="GASTClass175", type=gast_types_TypeAlias, multiplicity=Multiplicity(1, 1)),
        Property(name="innerTypeAliases", type=GASTClass, multiplicity=Multiplicity(0, 1))
    }
)
surroundingPackage176: BinaryAssociation = BinaryAssociation(
    name="surroundingPackage176",
    ends={
        Property(name="Package177", type=gast_types_TypeAlias, multiplicity=Multiplicity(1, 1)),
        Property(name="typeAliases", type=Package, multiplicity=Multiplicity(0, 1))
    }
)
overriddenMember178: BinaryAssociation = BinaryAssociation(
    name="overriddenMember178",
    ends={
        Property(name="Member", type=gast_types_Member, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_types_Member", type=Member, multiplicity=Multiplicity(0, 1))
    }
)
typeBounds179: BinaryAssociation = BinaryAssociation(
    name="typeBounds179",
    ends={
        Property(name="GASTType180", type=gast_types_TypeParameterClass, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_types_TypeParameterClass", type=GASTType, multiplicity=Multiplicity(0, 9999))
    }
)
innerTypeAliases181: BinaryAssociation = BinaryAssociation(
    name="innerTypeAliases181",
    ends={
        Property(name="TypeAlias182", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="surroundingClass", type=TypeAlias, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
innerDelegates183: BinaryAssociation = BinaryAssociation(
    name="innerDelegates183",
    ends={
        Property(name="Delegate185", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="surroundingClass184", type=Delegate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
constructors186: BinaryAssociation = BinaryAssociation(
    name="constructors186",
    ends={
        Property(name="Constructor", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="surroundingClass187", type=Constructor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
destructors188: BinaryAssociation = BinaryAssociation(
    name="destructors188",
    ends={
        Property(name="Destructor", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="surroundingClass189", type=Destructor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fields190: BinaryAssociation = BinaryAssociation(
    name="fields190",
    ends={
        Property(name="Field", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="surroundingClass191", type=Field, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
methods192: BinaryAssociation = BinaryAssociation(
    name="methods192",
    ends={
        Property(name="Method", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="surroundingClass193", type=Method_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
surroundingFunction194: BinaryAssociation = BinaryAssociation(
    name="surroundingFunction194",
    ends={
        Property(name="Function195", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="localClasses", type=Function, multiplicity=Multiplicity(0, 1))
    }
)
surroundingPackage196: BinaryAssociation = BinaryAssociation(
    name="surroundingPackage196",
    ends={
        Property(name="Package197", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="classes", type=Package, multiplicity=Multiplicity(0, 1))
    }
)
superTypes198: BinaryAssociation = BinaryAssociation(
    name="superTypes198",
    ends={
        Property(name="GASTClass199", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_types_GASTClass", type=GASTClass, multiplicity=Multiplicity(0, 9999))
    }
)
innerClasses200: BinaryAssociation = BinaryAssociation(
    name="innerClasses200",
    ends={
        Property(name="GASTClass202", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="surroundingClass201", type=GASTClass, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
surroundingClass203: BinaryAssociation = BinaryAssociation(
    name="surroundingClass203",
    ends={
        Property(name="GASTClass204", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="innerClasses", type=GASTClass, multiplicity=Multiplicity(0, 1))
    }
)
inheritanceTypeAccesses205: BinaryAssociation = BinaryAssociation(
    name="inheritanceTypeAccesses205",
    ends={
        Property(name="InheritanceTypeAccess", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_types_GASTClass206", type=InheritanceTypeAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
self207: BinaryAssociation = BinaryAssociation(
    name="self207",
    ends={
        Property(name="Field209", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_types_GASTClass208", type=Field, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
friendClasses210: BinaryAssociation = BinaryAssociation(
    name="friendClasses210",
    ends={
        Property(name="GASTClass211", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="gastClass", type=GASTClass, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
gastClass212: BinaryAssociation = BinaryAssociation(
    name="gastClass212",
    ends={
        Property(name="GASTClass213", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="friendClasses", type=GASTClass, multiplicity=Multiplicity(0, 1))
    }
)
friendFunctions214: BinaryAssociation = BinaryAssociation(
    name="friendFunctions214",
    ends={
        Property(name="Function216", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_types_GASTClass215", type=Function, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
property217: BinaryAssociation = BinaryAssociation(
    name="property217",
    ends={
        Property(name="Property", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_types_GASTClass218", type=Property_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
allAccesses219: BinaryAssociation = BinaryAssociation(
    name="allAccesses219",
    ends={
        Property(name="Access221", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_types_GASTClass220", type=Access, multiplicity=Multiplicity(0, 9999))
    }
)
allAccessedClasses222: BinaryAssociation = BinaryAssociation(
    name="allAccessedClasses222",
    ends={
        Property(name="GASTClass224", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_types_GASTClass223", type=GASTClass, multiplicity=Multiplicity(0, 9999))
    }
)
function244: BinaryAssociation = BinaryAssociation(
    name="function244",
    ends={
        Property(name="returnTypeDeclaration", type=Function, multiplicity=Multiplicity(0, 1)),
        Property(name="Function245", type=gast_accesses_DeclarationTypeAccess, multiplicity=Multiplicity(1, 1))
    }
)
targetType225: BinaryAssociation = BinaryAssociation(
    name="targetType225",
    ends={
        Property(name="GASTType226", type=gast_accesses_TypeAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_accesses_TypeAccess", type=GASTType, multiplicity=Multiplicity(1, 1))
    }
)
typeArguments227: BinaryAssociation = BinaryAssociation(
    name="typeArguments227",
    ends={
        Property(name="GASTType229", type=gast_accesses_TypeAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_accesses_TypeAccess228", type=GASTType, multiplicity=Multiplicity(0, 9999))
    }
)
accesses230: BinaryAssociation = BinaryAssociation(
    name="accesses230",
    ends={
        Property(name="BaseAccess231", type=gast_accesses_CompositeAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="surroundingCompositeAccess", type=BaseAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentStatement232: BinaryAssociation = BinaryAssociation(
    name="parentStatement232",
    ends={
        Property(name="Statement233", type=gast_accesses_BaseAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="accesses", type=Statement, multiplicity=Multiplicity(0, 1))
    }
)
surroundingStatement234: BinaryAssociation = BinaryAssociation(
    name="surroundingStatement234",
    ends={
        Property(name="Statement235", type=gast_accesses_BaseAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_accesses_BaseAccess", type=Statement, multiplicity=Multiplicity(0, 1))
    }
)
surroundingClass236: BinaryAssociation = BinaryAssociation(
    name="surroundingClass236",
    ends={
        Property(name="GASTClass238", type=gast_accesses_BaseAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_accesses_BaseAccess237", type=GASTClass, multiplicity=Multiplicity(1, 1))
    }
)
surroundingFunction239: BinaryAssociation = BinaryAssociation(
    name="surroundingFunction239",
    ends={
        Property(name="Function241", type=gast_accesses_BaseAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_accesses_BaseAccess240", type=Function, multiplicity=Multiplicity(0, 1))
    }
)
surroundingCompositeAccess242: BinaryAssociation = BinaryAssociation(
    name="surroundingCompositeAccess242",
    ends={
        Property(name="CompositeAccess", type=gast_accesses_BaseAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="accesses243", type=CompositeAccess, multiplicity=Multiplicity(0, 1))
    }
)
surroundingVariable246: BinaryAssociation = BinaryAssociation(
    name="surroundingVariable246",
    ends={
        Property(name="Variable", type=gast_accesses_DeclarationTypeAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="typeDeclaration", type=Variable, multiplicity=Multiplicity(0, 1))
    }
)
accessedFunctions247: BinaryAssociation = BinaryAssociation(
    name="accessedFunctions247",
    ends={
        Property(name="Function248", type=gast_accesses_DelegateAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_accesses_DelegateAccess", type=Function, multiplicity=Multiplicity(0, 9999))
    }
)
accessedDelegate249: BinaryAssociation = BinaryAssociation(
    name="accessedDelegate249",
    ends={
        Property(name="Delegate251", type=gast_accesses_DelegateAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_accesses_DelegateAccess250", type=Delegate, multiplicity=Multiplicity(1, 1))
    }
)
typeArguments252: BinaryAssociation = BinaryAssociation(
    name="typeArguments252",
    ends={
        Property(name="GASTType253", type=gast_accesses_FunctionAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_accesses_FunctionAccess", type=GASTType, multiplicity=Multiplicity(0, 9999))
    }
)
targetFunction254: BinaryAssociation = BinaryAssociation(
    name="targetFunction254",
    ends={
        Property(name="Function256", type=gast_accesses_FunctionAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_accesses_FunctionAccess255", type=Function, multiplicity=Multiplicity(1, 1))
    }
)
targetVariable257: BinaryAssociation = BinaryAssociation(
    name="targetVariable257",
    ends={
        Property(name="Variable258", type=gast_accesses_VariableAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_accesses_VariableAccess", type=Variable, multiplicity=Multiplicity(1, 1))
    }
)
accessedClass259: BinaryAssociation = BinaryAssociation(
    name="accessedClass259",
    ends={
        Property(name="GASTClass260", type=gast_accesses_Access, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_accesses_Access", type=GASTClass, multiplicity=Multiplicity(1, 1))
    }
)
accessedTarget261: BinaryAssociation = BinaryAssociation(
    name="accessedTarget261",
    ends={
        Property(name="ModelElement263", type=gast_accesses_Access, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_accesses_Access262", type=ModelElement, multiplicity=Multiplicity(1, 1))
    }
)
superClass264: BinaryAssociation = BinaryAssociation(
    name="superClass264",
    ends={
        Property(name="GASTClass265", type=gast_functions_Delegate, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_functions_Delegate", type=GASTClass, multiplicity=Multiplicity(0, 1))
    }
)
invocations266: BinaryAssociation = BinaryAssociation(
    name="invocations266",
    ends={
        Property(name="Function268", type=gast_functions_Delegate, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_functions_Delegate267", type=Function, multiplicity=Multiplicity(0, 9999))
    }
)
surroundingClass269: BinaryAssociation = BinaryAssociation(
    name="surroundingClass269",
    ends={
        Property(name="GASTClass270", type=gast_functions_Delegate, multiplicity=Multiplicity(1, 1)),
        Property(name="innerDelegates", type=GASTClass, multiplicity=Multiplicity(0, 1))
    }
)
surroundingPackage271: BinaryAssociation = BinaryAssociation(
    name="surroundingPackage271",
    ends={
        Property(name="Package272", type=gast_functions_Delegate, multiplicity=Multiplicity(1, 1)),
        Property(name="delegates", type=Package, multiplicity=Multiplicity(0, 1))
    }
)
surroundingClass273: BinaryAssociation = BinaryAssociation(
    name="surroundingClass273",
    ends={
        Property(name="GASTClass274", type=gast_functions_Constructor, multiplicity=Multiplicity(1, 1)),
        Property(name="constructors", type=GASTClass, multiplicity=Multiplicity(1, 1))
    }
)
surroundingClass275: BinaryAssociation = BinaryAssociation(
    name="surroundingClass275",
    ends={
        Property(name="GASTClass276", type=gast_functions_Destructor, multiplicity=Multiplicity(1, 1)),
        Property(name="destructors", type=GASTClass, multiplicity=Multiplicity(1, 1))
    }
)
surroundingPackage277: BinaryAssociation = BinaryAssociation(
    name="surroundingPackage277",
    ends={
        Property(name="Package278", type=gast_functions_GlobalFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="globalFunctions", type=Package, multiplicity=Multiplicity(0, 1))
    }
)
root279: BinaryAssociation = BinaryAssociation(
    name="root279",
    ends={
        Property(name="Root281", type=gast_functions_GlobalFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="globalFunctions280", type=Root, multiplicity=Multiplicity(0, 1))
    }
)
surroundingProperty282: BinaryAssociation = BinaryAssociation(
    name="surroundingProperty282",
    ends={
        Property(name="Property283", type=gast_functions_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_functions_Method", type=Property_, multiplicity=Multiplicity(0, 1))
    }
)
surroundingClass284: BinaryAssociation = BinaryAssociation(
    name="surroundingClass284",
    ends={
        Property(name="GASTClass285", type=gast_functions_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="methods", type=GASTClass, multiplicity=Multiplicity(1, 1))
    }
)
returnTypeDeclaration286: BinaryAssociation = BinaryAssociation(
    name="returnTypeDeclaration286",
    ends={
        Property(name="DeclarationTypeAccess", type=gast_functions_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="function", type=DeclarationTypeAccess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
formalParameters287: BinaryAssociation = BinaryAssociation(
    name="formalParameters287",
    ends={
        Property(name="FormalParameter", type=gast_functions_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="surroundingFunction", type=FormalParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
localVariables288: BinaryAssociation = BinaryAssociation(
    name="localVariables288",
    ends={
        Property(name="LocalVariable", type=gast_functions_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="surroundingFunction289", type=LocalVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
allStatements290: BinaryAssociation = BinaryAssociation(
    name="allStatements290",
    ends={
        Property(name="Statement291", type=gast_functions_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_functions_Function", type=Statement, multiplicity=Multiplicity(0, 9999))
    }
)
throwTypeAccesses292: BinaryAssociation = BinaryAssociation(
    name="throwTypeAccesses292",
    ends={
        Property(name="ThrowTypeAccess", type=gast_functions_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_functions_Function293", type=ThrowTypeAccess, multiplicity=Multiplicity(0, 9999))
    }
)
accesses294: BinaryAssociation = BinaryAssociation(
    name="accesses294",
    ends={
        Property(name="Access296", type=gast_functions_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_functions_Function295", type=Access, multiplicity=Multiplicity(0, 9999))
    }
)
body297: BinaryAssociation = BinaryAssociation(
    name="body297",
    ends={
        Property(name="BlockStatement299", type=gast_functions_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="surroundingFunction298", type=BlockStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
localClasses300: BinaryAssociation = BinaryAssociation(
    name="localClasses300",
    ends={
        Property(name="GASTClass302", type=gast_functions_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="surroundingFunction301", type=GASTClass, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
surroundingFunction303: BinaryAssociation = BinaryAssociation(
    name="surroundingFunction303",
    ends={
        Property(name="Function304", type=gast_variables_FormalParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="formalParameters", type=Function, multiplicity=Multiplicity(1, 1))
    }
)
type305: BinaryAssociation = BinaryAssociation(
    name="type305",
    ends={
        Property(name="GASTType306", type=gast_variables_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_variables_Variable", type=GASTType, multiplicity=Multiplicity(1, 1))
    }
)
typeDeclaration307: BinaryAssociation = BinaryAssociation(
    name="typeDeclaration307",
    ends={
        Property(name="DeclarationTypeAccess308", type=gast_variables_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="surroundingVariable", type=DeclarationTypeAccess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
surroundingClass309: BinaryAssociation = BinaryAssociation(
    name="surroundingClass309",
    ends={
        Property(name="GASTClass310", type=gast_variables_Field, multiplicity=Multiplicity(1, 1)),
        Property(name="fields", type=GASTClass, multiplicity=Multiplicity(0, 1))
    }
)
surroundingFunction311: BinaryAssociation = BinaryAssociation(
    name="surroundingFunction311",
    ends={
        Property(name="Function312", type=gast_variables_LocalVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="localVariables", type=Function, multiplicity=Multiplicity(1, 1))
    }
)
setter313: BinaryAssociation = BinaryAssociation(
    name="setter313",
    ends={
        Property(name="Method314", type=gast_variables_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_variables_Property", type=Method_, multiplicity=Multiplicity(0, 1))
    }
)
getter315: BinaryAssociation = BinaryAssociation(
    name="getter315",
    ends={
        Property(name="Method317", type=gast_variables_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_variables_Property316", type=Method_, multiplicity=Multiplicity(0, 1))
    }
)
surroundingPackage318: BinaryAssociation = BinaryAssociation(
    name="surroundingPackage318",
    ends={
        Property(name="Package319", type=gast_variables_GlobalVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="globalVariables", type=Package, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_gast_statements_ExceptionHandler_Statement = Generalization(general=Statement, specific=gast_statements_ExceptionHandler)
gen_gast_statements_Statement_SourceEntity = Generalization(general=SourceEntity, specific=gast_statements_Statement)
gen_gast_statements_BlockStatement_Statement = Generalization(general=Statement, specific=gast_statements_BlockStatement)
gen_gast_statements_Branch_SourceEntity = Generalization(general=SourceEntity, specific=gast_statements_Branch)
gen_gast_statements_GASTExpression_SourceEntity = Generalization(general=SourceEntity, specific=gast_statements_GASTExpression)
gen_gast_statements_BranchStatement_Statement = Generalization(general=Statement, specific=gast_statements_BranchStatement)
gen_gast_statements_LoopStatement_Statement = Generalization(general=Statement, specific=gast_statements_LoopStatement)
gen_gast_statements_CatchBlock_BlockStatement = Generalization(general=BlockStatement, specific=gast_statements_CatchBlock)
gen_gast_statements_JumpStatement_Statement = Generalization(general=Statement, specific=gast_statements_JumpStatement)
gen_gast_statements_SimpleStatement_Statement = Generalization(general=Statement, specific=gast_statements_SimpleStatement)
gen_gast_core_BasePath_ModelElement = Generalization(general=ModelElement, specific=gast_core_BasePath)
gen_gast_core_ModelElement_Identifier = Generalization(general=Identifier, specific=gast_core_ModelElement)
gen_gast_core_NamedModelElement_ModelElement = Generalization(general=ModelElement, specific=gast_core_NamedModelElement)
gen_gast_core_Package_NamedModelElement = Generalization(general=NamedModelElement, specific=gast_core_Package)
gen_gast_core_GenericEntity_ModelElement = Generalization(general=ModelElement, specific=gast_core_GenericEntity)
gen_gast_core_Root_ModelElement = Generalization(general=ModelElement, specific=gast_core_Root)
gen_gast_core_Directory_NamedModelElement = Generalization(general=NamedModelElement, specific=gast_core_Directory)
gen_gast_core_File_NamedModelElement = Generalization(general=NamedModelElement, specific=gast_core_File)
gen_gast_annotations_Clone_core_ModelElement = Generalization(general=core_ModelElement, specific=gast_annotations_Clone)
gen_gast_annotations_Clone_annotations_ModelAnnotation = Generalization(general=annotations_ModelAnnotation, specific=gast_annotations_Clone)
gen_gast_core_PackageAlias_Package = Generalization(general=Package, specific=gast_core_PackageAlias)
gen_gast_core_SourceEntity_ModelElement = Generalization(general=ModelElement, specific=gast_core_SourceEntity)
gen_gast_annotations_Attribute_types_GASTClass = Generalization(general=types_GASTClass, specific=gast_annotations_Attribute)
gen_gast_annotations_Attribute_annotations_ModelAnnotation = Generalization(general=annotations_ModelAnnotation, specific=gast_annotations_Attribute)
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
gen_gast_accesses_FunctionAccess_Access = Generalization(general=Access, specific=gast_accesses_FunctionAccess)
gen_gast_accesses_InheritanceTypeAccess_TypeAccess = Generalization(general=TypeAccess, specific=gast_accesses_InheritanceTypeAccess)
gen_gast_accesses_VariableAccess_Access = Generalization(general=Access, specific=gast_accesses_VariableAccess)
gen_gast_accesses_RunTimeTypeAccess_TypeAccess = Generalization(general=TypeAccess, specific=gast_accesses_RunTimeTypeAccess)
gen_gast_accesses_SelfAccess_VariableAccess = Generalization(general=VariableAccess, specific=gast_accesses_SelfAccess)
gen_gast_functions_Constructor_functions_Function = Generalization(general=functions_Function, specific=gast_functions_Constructor)
gen_gast_functions_Constructor_types_Member = Generalization(general=types_Member, specific=gast_functions_Constructor)
gen_gast_accesses_StaticTypeAccess_TypeAccess = Generalization(general=TypeAccess, specific=gast_accesses_StaticTypeAccess)
gen_gast_accesses_PropertyAccess_VariableAccess = Generalization(general=VariableAccess, specific=gast_accesses_PropertyAccess)
gen_gast_accesses_Access_BaseAccess = Generalization(general=BaseAccess, specific=gast_accesses_Access)
gen_gast_functions_Delegate_functions_Function = Generalization(general=functions_Function, specific=gast_functions_Delegate)
gen_gast_functions_Delegate_types_Member = Generalization(general=types_Member, specific=gast_functions_Delegate)
gen_gast_functions_Delegate_types_GASTType = Generalization(general=types_GASTType, specific=gast_functions_Delegate)
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
gen_gast_variables_Property_variables_Field = Generalization(general=variables_Field, specific=gast_variables_Property)
gen_gast_variables_Property_types_Member = Generalization(general=types_Member, specific=gast_variables_Property)
gen_gast_variables_FormalParameter_Variable = Generalization(general=Variable, specific=gast_variables_FormalParameter)
gen_gast_variables_Variable_core_NamedModelElement = Generalization(general=core_NamedModelElement, specific=gast_variables_Variable)
gen_gast_variables_Variable_core_SourceEntity = Generalization(general=core_SourceEntity, specific=gast_variables_Variable)
gen_gast_variables_CatchParameter_Variable = Generalization(general=Variable, specific=gast_variables_CatchParameter)
gen_gast_variables_Field_types_Member = Generalization(general=types_Member, specific=gast_variables_Field)
gen_gast_variables_Field_variables_Variable = Generalization(general=variables_Variable, specific=gast_variables_Field)
gen_gast_variables_LocalVariable_Variable = Generalization(general=Variable, specific=gast_variables_LocalVariable)
gen_gast_variables_GlobalVariable_Variable = Generalization(general=Variable, specific=gast_variables_GlobalVariable)

# Domain Model
domain_model = DomainModel(
    name="gast",
    types={Branch, gast_statements_ExceptionHandler, Statement, CatchBlock, BlockStatement, gast_statements_Statement, SourceEntity, BaseAccess, CloneInstance, LoopStatement, gast_statements_BlockStatement, Function, gast_statements_Branch, GASTExpression, BranchStatement, gast_statements_GASTExpression, gast_statements_BranchStatement, gast_statements_LoopStatement, gast_statements_CatchBlock, CatchParameter, gast_statements_JumpStatement, gast_statements_SimpleStatement, gast_statements_GASTBehaviour, gast_core_BasePath, ModelElement, Root, Directory, gast_core_ModelElement, Identifier, ModelAnnotation, gast_core_Identifier, GlobalFunction, gast_core_NamedModelElement, gast_core_Package, NamedModelElement, GASTClass, Access, Delegate, GlobalVariable, Package, TypeAlias, gast_core_GenericEntity, TypeParameterClass, gast_core_Root, GASTType, Clone, StructuralAbstraction, BasePath, gast_core_Directory, File, gast_core_File, gast_annotations_Clone, core_ModelElement, gast_core_Position, gast_core_PackageAlias, gast_core_SourceEntity, Position, gast_annotations_Attribute, types_GASTClass, annotations_ModelAnnotation, gast_annotations_CloneInstance, gast_annotations_StructuralAbstraction, core_NamedModelElement, gast_annotations_Comment, core_SourceEntity, gast_annotations_Subsystem, gast_annotations_Layer, gast_annotations_ModelAnnotation, gast_types_Reference, TypeDecorator, gast_types_TypeDecorator, gast_types_GASTType, gast_types_GASTArray, gast_types_TypeAlias, types_Member, types_TypeDecorator, gast_types_Member, Member, gast_types_TypeParameterClass, gast_types_GenericClass, core_GenericEntity, gast_types_GASTEnumeration, gast_types_GASTStruct, gast_types_GASTUnion, gast_types_GASTClass, types_GASTType, Constructor, Destructor, Field, Method_, TypeAccess, InheritanceTypeAccess, Property_, gast_accesses_ParameterInstantiationTypeAccess, gast_accesses_TypeAccess, gast_accesses_CastTypeAccess, gast_accesses_CompositeAccess, gast_accesses_BaseAccess, CompositeAccess, gast_accesses_DeclarationTypeAccess, Variable, gast_accesses_ThrowTypeAccess, gast_accesses_DelegateAccess, FunctionAccess, gast_accesses_FunctionAccess, gast_accesses_InheritanceTypeAccess, gast_accesses_VariableAccess, gast_accesses_RunTimeTypeAccess, gast_accesses_SelfAccess, VariableAccess, gast_functions_Constructor, gast_accesses_StaticTypeAccess, gast_accesses_PropertyAccess, gast_accesses_Access, gast_functions_Delegate, functions_Function, gast_functions_Destructor, gast_functions_GenericFunction, functions_GlobalFunction, gast_functions_GlobalFunction, gast_functions_Method, gast_functions_GenericMethod, functions_Method, gast_functions_GenericConstructor, functions_Constructor, gast_functions_Function, DeclarationTypeAccess, FormalParameter, LocalVariable, ThrowTypeAccess, gast_variables_Property, variables_Field, gast_variables_FormalParameter, gast_variables_Variable, gast_variables_CatchParameter, gast_variables_Field, variables_Variable, gast_variables_LocalVariable, gast_variables_GlobalVariable, LoopStatementKind, JumpStatementKind, Status, Visibilities, GlobalFunctionKind},
    associations={catchBlocks0, finallyBlock1, guardedBlock3, accesses6, cloneInstance7, blockstatement8, surroundingStatement11, initExpression26, branch12, loopstatement13, statements14, surroundingFunction16, conditionExpression18, branchstatement19, statement20, branches22, breakConditionExpression24, blockstatement39, incrementExpression29, body32, catchParameter34, expression35, expression37, root41, directories42, annotations43, allLocalClasses44, allInnerClasses45, allNormalClasses48, allInterfaces51, allAccesses54, delegates56, globalFunctions57, globalVariables59, root61, classes63, subPackages66, surroundingPackage68, allAccessedPackages70, typeAliases73, typeParameters75, allAccesses76, allInnerClasses78, allInterfaces81, allLocalClasses84, allNormalClasses87, allModelElements90, globalVariables92, packages95, clones97, structuralAbstractions99, types101, danglingModelElements103, basePaths106, globalFunctions108, subDirectory111, parentDirectory113, files115, basePath116, root118, directory144, importedTypes120, types123, globalVariables126, globalFunctions129, importedGlobalFunctions132, importedGlobalVariables135, importedPackages138, includedFiles141, sourceFile146, assembly148, sourceentity151, aliasedPackage152, position154, cloneInstances155, root157, statements159, clone161, referencedType163, decoratedType165, undecoratedType167, baseType170, aliasedType172, surroundingClass174, surroundingPackage176, overriddenMember178, typeBounds179, innerTypeAliases181, innerDelegates183, constructors186, destructors188, fields190, methods192, surroundingFunction194, surroundingPackage196, superTypes198, innerClasses200, surroundingClass203, inheritanceTypeAccesses205, self207, friendClasses210, gastClass212, friendFunctions214, property217, allAccesses219, allAccessedClasses222, function244, targetType225, typeArguments227, accesses230, parentStatement232, surroundingStatement234, surroundingClass236, surroundingFunction239, surroundingCompositeAccess242, surroundingVariable246, accessedFunctions247, accessedDelegate249, typeArguments252, targetFunction254, targetVariable257, accessedClass259, accessedTarget261, superClass264, invocations266, surroundingClass269, surroundingPackage271, surroundingClass273, surroundingClass275, surroundingPackage277, root279, surroundingProperty282, surroundingClass284, returnTypeDeclaration286, formalParameters287, localVariables288, allStatements290, throwTypeAccesses292, accesses294, body297, localClasses300, surroundingFunction303, type305, typeDeclaration307, surroundingClass309, surroundingFunction311, setter313, getter315, surroundingPackage318},
    generalizations={gen_gast_statements_ExceptionHandler_Statement, gen_gast_statements_Statement_SourceEntity, gen_gast_statements_BlockStatement_Statement, gen_gast_statements_Branch_SourceEntity, gen_gast_statements_GASTExpression_SourceEntity, gen_gast_statements_BranchStatement_Statement, gen_gast_statements_LoopStatement_Statement, gen_gast_statements_CatchBlock_BlockStatement, gen_gast_statements_JumpStatement_Statement, gen_gast_statements_SimpleStatement_Statement, gen_gast_core_BasePath_ModelElement, gen_gast_core_ModelElement_Identifier, gen_gast_core_NamedModelElement_ModelElement, gen_gast_core_Package_NamedModelElement, gen_gast_core_GenericEntity_ModelElement, gen_gast_core_Root_ModelElement, gen_gast_core_Directory_NamedModelElement, gen_gast_core_File_NamedModelElement, gen_gast_annotations_Clone_core_ModelElement, gen_gast_annotations_Clone_annotations_ModelAnnotation, gen_gast_core_PackageAlias_Package, gen_gast_core_SourceEntity_ModelElement, gen_gast_annotations_Attribute_types_GASTClass, gen_gast_annotations_Attribute_annotations_ModelAnnotation, gen_gast_annotations_CloneInstance_core_ModelElement, gen_gast_annotations_CloneInstance_annotations_ModelAnnotation, gen_gast_annotations_StructuralAbstraction_core_NamedModelElement, gen_gast_annotations_StructuralAbstraction_annotations_ModelAnnotation, gen_gast_annotations_Comment_core_SourceEntity, gen_gast_annotations_Comment_annotations_ModelAnnotation, gen_gast_annotations_Subsystem_StructuralAbstraction, gen_gast_annotations_Layer_StructuralAbstraction, gen_gast_types_Reference_TypeDecorator, gen_gast_types_TypeDecorator_GASTType, gen_gast_types_GASTType_NamedModelElement, gen_gast_types_GASTArray_TypeDecorator, gen_gast_types_TypeAlias_types_Member, gen_gast_types_TypeAlias_types_TypeDecorator, gen_gast_types_Member_SourceEntity, gen_gast_types_TypeParameterClass_GASTClass, gen_gast_types_GenericClass_types_GASTClass, gen_gast_types_GenericClass_core_GenericEntity, gen_gast_types_GASTEnumeration_GASTClass, gen_gast_types_GASTStruct_GASTClass, gen_gast_types_GASTUnion_GASTClass, gen_gast_types_GASTClass_types_Member, gen_gast_types_GASTClass_types_GASTType, gen_gast_accesses_ParameterInstantiationTypeAccess_TypeAccess, gen_gast_accesses_TypeAccess_Access, gen_gast_accesses_CastTypeAccess_TypeAccess, gen_gast_accesses_CompositeAccess_BaseAccess, gen_gast_accesses_BaseAccess_SourceEntity, gen_gast_accesses_DeclarationTypeAccess_TypeAccess, gen_gast_accesses_ThrowTypeAccess_TypeAccess, gen_gast_accesses_DelegateAccess_FunctionAccess, gen_gast_accesses_FunctionAccess_Access, gen_gast_accesses_InheritanceTypeAccess_TypeAccess, gen_gast_accesses_VariableAccess_Access, gen_gast_accesses_RunTimeTypeAccess_TypeAccess, gen_gast_accesses_SelfAccess_VariableAccess, gen_gast_functions_Constructor_functions_Function, gen_gast_functions_Constructor_types_Member, gen_gast_accesses_StaticTypeAccess_TypeAccess, gen_gast_accesses_PropertyAccess_VariableAccess, gen_gast_accesses_Access_BaseAccess, gen_gast_functions_Delegate_functions_Function, gen_gast_functions_Delegate_types_Member, gen_gast_functions_Delegate_types_GASTType, gen_gast_functions_Destructor_functions_Function, gen_gast_functions_Destructor_types_Member, gen_gast_functions_GenericFunction_functions_GlobalFunction, gen_gast_functions_GenericFunction_core_GenericEntity, gen_gast_functions_GlobalFunction_Function, gen_gast_functions_Method_functions_Function, gen_gast_functions_Method_types_Member, gen_gast_functions_GenericMethod_functions_Method, gen_gast_functions_GenericMethod_core_GenericEntity, gen_gast_functions_GenericConstructor_functions_Constructor, gen_gast_functions_GenericConstructor_core_GenericEntity, gen_gast_functions_Function_core_NamedModelElement, gen_gast_functions_Function_core_SourceEntity, gen_gast_variables_Property_variables_Field, gen_gast_variables_Property_types_Member, gen_gast_variables_FormalParameter_Variable, gen_gast_variables_Variable_core_NamedModelElement, gen_gast_variables_Variable_core_SourceEntity, gen_gast_variables_CatchParameter_Variable, gen_gast_variables_Field_types_Member, gen_gast_variables_Field_variables_Variable, gen_gast_variables_LocalVariable_Variable, gen_gast_variables_GlobalVariable_Variable},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)