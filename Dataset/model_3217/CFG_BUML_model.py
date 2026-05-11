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
			EnumerationLiteral(name="FAILEDDEP"),
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
gast_statements_ExceptionHandler = Class(name="gast_statements_ExceptionHandler")
Statement = Class(name="Statement")
CatchBlock = Class(name="CatchBlock")
BlockStatement = Class(name="BlockStatement")
gast_statements_Statement = Class(name="gast_statements_Statement", is_abstract=True)
SourceEntity = Class(name="SourceEntity")
BaseAccess = Class(name="BaseAccess")
CloneInstance = Class(name="CloneInstance")
Branch = Class(name="Branch")
LoopStatement = Class(name="LoopStatement")
gast_statements_BlockStatement = Class(name="gast_statements_BlockStatement")
Function = Class(name="Function")
gast_statements_Branch = Class(name="gast_statements_Branch")
GASTExpression = Class(name="GASTExpression")
gast_statements_GASTExpression = Class(name="gast_statements_GASTExpression", is_abstract=True)
gast_statements_BranchStatement = Class(name="gast_statements_BranchStatement")
gast_statements_LoopStatement = Class(name="gast_statements_LoopStatement")
gast_statements_CatchBlock = Class(name="gast_statements_CatchBlock")
CatchParameter = Class(name="CatchParameter")
BranchStatement = Class(name="BranchStatement")
gast_statements_SimpleStatement = Class(name="gast_statements_SimpleStatement")
gast_statements_GASTBehaviour = Class(name="gast_statements_GASTBehaviour")
gast_statements_Methods = Class(name="gast_statements_Methods")
statements_BlockStatement = Class(name="statements_BlockStatement")
Exit = Class(name="Exit")
gast_statements_Exit = Class(name="gast_statements_Exit")
FlowInstr = Class(name="FlowInstr")
gast_statements_FlowInstr = Class(name="gast_statements_FlowInstr")
Var = Class(name="Var")
gast_statements_JumpStatement = Class(name="gast_statements_JumpStatement")
statements_Statement = Class(name="statements_Statement")
statements_FlowInstr = Class(name="statements_FlowInstr")
gast_core_BasePath = Class(name="gast_core_BasePath")
ModelElement = Class(name="ModelElement")
Root = Class(name="Root")
Directory = Class(name="Directory")
gast_core_ModelElement = Class(name="gast_core_ModelElement", is_abstract=True)
Identifier = Class(name="Identifier")
ModelAnnotation = Class(name="ModelAnnotation")
gast_core_Identifier = Class(name="gast_core_Identifier", is_abstract=True)
gast_core_NamedModelElement = Class(name="gast_core_NamedModelElement", is_abstract=True)
gast_core_Package = Class(name="gast_core_Package")
NamedModelElement = Class(name="NamedModelElement")
gast_statements_Var = Class(name="gast_statements_Var")
gast_statements_Param = Class(name="gast_statements_Param")
Access = Class(name="Access")
Delegate = Class(name="Delegate")
GlobalFunction = Class(name="GlobalFunction")
GlobalVariable = Class(name="GlobalVariable")
Package = Class(name="Package")
GASTClass = Class(name="GASTClass")
TypeAlias = Class(name="TypeAlias")
gast_core_GenericEntity = Class(name="gast_core_GenericEntity", is_abstract=True)
TypeParameterClass = Class(name="TypeParameterClass")
gast_core_Root = Class(name="gast_core_Root")
Clone = Class(name="Clone")
StructuralAbstraction = Class(name="StructuralAbstraction")
GASTType = Class(name="GASTType")
BasePath = Class(name="BasePath")
gast_core_Directory = Class(name="gast_core_Directory")
File = Class(name="File")
gast_core_File = Class(name="gast_core_File")
gast_core_Position = Class(name="gast_core_Position")
gast_core_PackageAlias = Class(name="gast_core_PackageAlias")
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
gast_core_SourceEntity = Class(name="gast_core_SourceEntity", is_abstract=True)
gast_annotations_Subsystem = Class(name="gast_annotations_Subsystem")
gast_annotations_Layer = Class(name="gast_annotations_Layer")
gast_annotations_ModelAnnotation = Class(name="gast_annotations_ModelAnnotation", is_abstract=True)
gast_types_Reference = Class(name="gast_types_Reference")
TypeDecorator = Class(name="TypeDecorator")
gast_types_TypeDecorator = Class(name="gast_types_TypeDecorator", is_abstract=True)
gast_types_GASTType = Class(name="gast_types_GASTType", is_abstract=True)
gast_types_TypeAlias = Class(name="gast_types_TypeAlias")
types_Member = Class(name="types_Member")
types_TypeDecorator = Class(name="types_TypeDecorator")
gast_types_Member = Class(name="gast_types_Member", is_abstract=True)
Member = Class(name="Member")
gast_types_GASTArray = Class(name="gast_types_GASTArray")
gast_types_TypeParameterClass = Class(name="gast_types_TypeParameterClass")
gast_types_GenericClass = Class(name="gast_types_GenericClass")
core_GenericEntity = Class(name="core_GenericEntity")
gast_types_GASTEnumeration = Class(name="gast_types_GASTEnumeration")
gast_types_GASTStruct = Class(name="gast_types_GASTStruct")
gast_types_GASTUnion = Class(name="gast_types_GASTUnion")
Constructor = Class(name="Constructor")
Destructor = Class(name="Destructor")
Field = Class(name="Field")
Method_ = Class(name="Method")
gast_types_GASTClass = Class(name="gast_types_GASTClass")
types_GASTType = Class(name="types_GASTType")
InheritanceTypeAccess = Class(name="InheritanceTypeAccess")
Property_ = Class(name="Property")
gast_accesses_ParameterInstantiationTypeAccess = Class(name="gast_accesses_ParameterInstantiationTypeAccess")
TypeAccess = Class(name="TypeAccess")
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
gast_accesses_StaticTypeAccess = Class(name="gast_accesses_StaticTypeAccess")
gast_accesses_PropertyAccess = Class(name="gast_accesses_PropertyAccess")
gast_accesses_Access = Class(name="gast_accesses_Access", is_abstract=True)
gast_functions_Delegate = Class(name="gast_functions_Delegate")
functions_Function = Class(name="functions_Function")
gast_functions_Constructor = Class(name="gast_functions_Constructor")
gast_functions_Destructor = Class(name="gast_functions_Destructor")
gast_functions_GenericFunction = Class(name="gast_functions_GenericFunction")
functions_GlobalFunction = Class(name="functions_GlobalFunction")
gast_functions_GlobalFunction = Class(name="gast_functions_GlobalFunction")
gast_functions_Method = Class(name="gast_functions_Method")
gast_functions_GenericMethod = Class(name="gast_functions_GenericMethod")
functions_Method = Class(name="functions_Method")
gast_functions_GenericConstructor = Class(name="gast_functions_GenericConstructor")
functions_Constructor = Class(name="functions_Constructor")
DeclarationTypeAccess = Class(name="DeclarationTypeAccess")
FormalParameter = Class(name="FormalParameter")
LocalVariable = Class(name="LocalVariable")
ThrowTypeAccess = Class(name="ThrowTypeAccess")
gast_functions_Function = Class(name="gast_functions_Function", is_abstract=True)
gast_variables_FormalParameter = Class(name="gast_variables_FormalParameter")
gast_variables_Variable = Class(name="gast_variables_Variable", is_abstract=True)
gast_variables_CatchParameter = Class(name="gast_variables_CatchParameter")
gast_variables_Field = Class(name="gast_variables_Field")
variables_Variable = Class(name="variables_Variable")
gast_variables_Property = Class(name="gast_variables_Property")
variables_Field = Class(name="variables_Field")
gast_variables_GlobalVariable = Class(name="gast_variables_GlobalVariable")
gast_variables_LocalVariable = Class(name="gast_variables_LocalVariable")

# gast_statements_ExceptionHandler class attributes and methods

# Statement class attributes and methods

# CatchBlock class attributes and methods

# BlockStatement class attributes and methods

# gast_statements_Statement class attributes and methods
gast_statements_Statement_numberOfStatements: Property = Property(name="numberOfStatements", type=IntegerType)
gast_statements_Statement_linesOfCode: Property = Property(name="linesOfCode", type=IntegerType)
gast_statements_Statement_numberOfEdgesInCFG: Property = Property(name="numberOfEdgesInCFG", type=IntegerType)
gast_statements_Statement_numberOfNodesInCFG: Property = Property(name="numberOfNodesInCFG", type=IntegerType)
gast_statements_Statement_maximumNestingLevel: Property = Property(name="maximumNestingLevel", type=IntegerType)
gast_statements_Statement_numberOfComments: Property = Property(name="numberOfComments", type=IntegerType)
gast_statements_Statement.attributes={gast_statements_Statement_numberOfStatements, gast_statements_Statement_numberOfNodesInCFG, gast_statements_Statement_linesOfCode, gast_statements_Statement_numberOfComments, gast_statements_Statement_maximumNestingLevel, gast_statements_Statement_numberOfEdgesInCFG}

# SourceEntity class attributes and methods

# BaseAccess class attributes and methods

# CloneInstance class attributes and methods

# Branch class attributes and methods

# LoopStatement class attributes and methods

# gast_statements_BlockStatement class attributes and methods
gast_statements_BlockStatement_synchronized: Property = Property(name="synchronized", type=BooleanType)
gast_statements_BlockStatement.attributes={gast_statements_BlockStatement_synchronized}

# Function class attributes and methods

# gast_statements_Branch class attributes and methods

# GASTExpression class attributes and methods

# gast_statements_GASTExpression class attributes and methods

# gast_statements_BranchStatement class attributes and methods

# gast_statements_LoopStatement class attributes and methods
gast_statements_LoopStatement_kind: Property = Property(name="kind", type=StringType)
gast_statements_LoopStatement.attributes={gast_statements_LoopStatement_kind}

# gast_statements_CatchBlock class attributes and methods

# CatchParameter class attributes and methods

# BranchStatement class attributes and methods

# gast_statements_SimpleStatement class attributes and methods

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

# gast_statements_JumpStatement class attributes and methods
gast_statements_JumpStatement_kind: Property = Property(name="kind", type=StringType)
gast_statements_JumpStatement.attributes={gast_statements_JumpStatement_kind}

# statements_Statement class attributes and methods

# statements_FlowInstr class attributes and methods

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

# gast_core_NamedModelElement class attributes and methods
gast_core_NamedModelElement_simpleName: Property = Property(name="simpleName", type=StringType)
gast_core_NamedModelElement.attributes={gast_core_NamedModelElement_simpleName}

# gast_core_Package class attributes and methods
gast_core_Package_linesOfComments: Property = Property(name="linesOfComments", type=IntegerType)
gast_core_Package_linesOfCode: Property = Property(name="linesOfCode", type=IntegerType)
gast_core_Package_qualifiedName: Property = Property(name="qualifiedName", type=StringType)
gast_core_Package.attributes={gast_core_Package_linesOfComments, gast_core_Package_linesOfCode, gast_core_Package_qualifiedName}

# NamedModelElement class attributes and methods

# gast_statements_Var class attributes and methods
gast_statements_Var_name: Property = Property(name="name", type=StringType)
gast_statements_Var.attributes={gast_statements_Var_name}

# gast_statements_Param class attributes and methods

# Access class attributes and methods

# Delegate class attributes and methods

# GlobalFunction class attributes and methods

# GlobalVariable class attributes and methods

# Package class attributes and methods

# GASTClass class attributes and methods

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

# Clone class attributes and methods

# StructuralAbstraction class attributes and methods

# GASTType class attributes and methods

# BasePath class attributes and methods

# gast_core_Directory class attributes and methods
gast_core_Directory_fullQualifiedPath: Property = Property(name="fullQualifiedPath", type=StringType)
gast_core_Directory_fileSystemPath: Property = Property(name="fileSystemPath", type=StringType)
gast_core_Directory.attributes={gast_core_Directory_fullQualifiedPath, gast_core_Directory_fileSystemPath}

# File class attributes and methods

# gast_core_File class attributes and methods
gast_core_File_sourceFile: Property = Property(name="sourceFile", type=BooleanType)
gast_core_File_linesOfCode: Property = Property(name="linesOfCode", type=IntegerType)
gast_core_File_size: Property = Property(name="size", type=StringType)
gast_core_File_fullQualifiedPath: Property = Property(name="fullQualifiedPath", type=StringType)
gast_core_File_assemblyFile: Property = Property(name="assemblyFile", type=BooleanType)
gast_core_File_fileSystemPath: Property = Property(name="fileSystemPath", type=StringType)
gast_core_File.attributes={gast_core_File_sourceFile, gast_core_File_fileSystemPath, gast_core_File_assemblyFile, gast_core_File_size, gast_core_File_fullQualifiedPath, gast_core_File_linesOfCode}

# gast_core_Position class attributes and methods
gast_core_Position_endColumn: Property = Property(name="endColumn", type=IntegerType)
gast_core_Position_startColumn: Property = Property(name="startColumn", type=IntegerType)
gast_core_Position_endLine: Property = Property(name="endLine", type=IntegerType)
gast_core_Position_startLine: Property = Property(name="startLine", type=IntegerType)
gast_core_Position_m_EitherAssemblyFileOrSourceFileSet: Method = Method(name="EitherAssemblyFileOrSourceFileSet", parameters={Parameter(name='gast_diagnostics', type=StringType), Parameter(name='gast_context', type=StringType)}, type=BooleanType)
gast_core_Position.attributes={gast_core_Position_startColumn, gast_core_Position_startLine, gast_core_Position_endLine, gast_core_Position_endColumn}
gast_core_Position.methods={gast_core_Position_m_EitherAssemblyFileOrSourceFileSet}

# gast_core_PackageAlias class attributes and methods

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
gast_annotations_Comment_formal: Property = Property(name="formal", type=BooleanType)
gast_annotations_Comment_todoCount: Property = Property(name="todoCount", type=IntegerType)
gast_annotations_Comment_texts: Property = Property(name="texts", type=StringType)
gast_annotations_Comment_todo: Property = Property(name="todo", type=BooleanType)
gast_annotations_Comment_m_OCLtodo: Method = Method(name="OCLtodo", parameters={Parameter(name='gast_context', type=StringType), Parameter(name='gast_diagnostics', type=StringType)}, type=BooleanType)
gast_annotations_Comment.attributes={gast_annotations_Comment_todoCount, gast_annotations_Comment_texts, gast_annotations_Comment_formal, gast_annotations_Comment_todo}
gast_annotations_Comment.methods={gast_annotations_Comment_m_OCLtodo}

# core_SourceEntity class attributes and methods

# gast_core_SourceEntity class attributes and methods

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
gast_types_Member_typeParameterClassMember: Property = Property(name="typeParameterClassMember", type=BooleanType)
gast_types_Member_virtual: Property = Property(name="virtual", type=BooleanType)
gast_types_Member_override: Property = Property(name="override", type=BooleanType)
gast_types_Member_static: Property = Property(name="static", type=BooleanType)
gast_types_Member_m_getSurroundingClass: Method = Method(name="getSurroundingClass", parameters={}, type=StringType)
gast_types_Member.attributes={gast_types_Member_static, gast_types_Member_visibility, gast_types_Member_typeParameterClassMember, gast_types_Member_internal, gast_types_Member_override, gast_types_Member_final, gast_types_Member_extern, gast_types_Member_introspectable, gast_types_Member_abstract, gast_types_Member_virtual}
gast_types_Member.methods={gast_types_Member_m_getSurroundingClass}

# Member class attributes and methods

# gast_types_GASTArray class attributes and methods
gast_types_GASTArray_dimensions: Property = Property(name="dimensions", type=IntegerType)
gast_types_GASTArray.attributes={gast_types_GASTArray_dimensions}

# gast_types_TypeParameterClass class attributes and methods

# gast_types_GenericClass class attributes and methods

# core_GenericEntity class attributes and methods

# gast_types_GASTEnumeration class attributes and methods

# gast_types_GASTStruct class attributes and methods

# gast_types_GASTUnion class attributes and methods

# Constructor class attributes and methods

# Destructor class attributes and methods

# Field class attributes and methods

# Method class attributes and methods

# gast_types_GASTClass class attributes and methods
gast_types_GASTClass_local: Property = Property(name="local", type=BooleanType)
gast_types_GASTClass_primitive: Property = Property(name="primitive", type=BooleanType)
gast_types_GASTClass_interface: Property = Property(name="interface", type=BooleanType)
gast_types_GASTClass_anonymous: Property = Property(name="anonymous", type=BooleanType)
gast_types_GASTClass_linesOfComments: Property = Property(name="linesOfComments", type=IntegerType)
gast_types_GASTClass_inner: Property = Property(name="inner", type=BooleanType)
gast_types_GASTClass.attributes={gast_types_GASTClass_local, gast_types_GASTClass_inner, gast_types_GASTClass_primitive, gast_types_GASTClass_interface, gast_types_GASTClass_anonymous, gast_types_GASTClass_linesOfComments}

# types_GASTType class attributes and methods

# InheritanceTypeAccess class attributes and methods

# Property class attributes and methods

# gast_accesses_ParameterInstantiationTypeAccess class attributes and methods

# TypeAccess class attributes and methods

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

# gast_accesses_StaticTypeAccess class attributes and methods

# gast_accesses_PropertyAccess class attributes and methods

# gast_accesses_Access class attributes and methods

# gast_functions_Delegate class attributes and methods
gast_functions_Delegate_innerDelegate: Property = Property(name="innerDelegate", type=BooleanType)
gast_functions_Delegate.attributes={gast_functions_Delegate_innerDelegate}

# functions_Function class attributes and methods

# gast_functions_Constructor class attributes and methods
gast_functions_Constructor_initializer: Property = Property(name="initializer", type=BooleanType)
gast_functions_Constructor.attributes={gast_functions_Constructor_initializer}

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

# DeclarationTypeAccess class attributes and methods

# FormalParameter class attributes and methods

# LocalVariable class attributes and methods

# ThrowTypeAccess class attributes and methods

# gast_functions_Function class attributes and methods
gast_functions_Function_numberOfStatements: Property = Property(name="numberOfStatements", type=IntegerType)
gast_functions_Function_maximumNestingLevel: Property = Property(name="maximumNestingLevel", type=IntegerType)
gast_functions_Function_linesOfComments: Property = Property(name="linesOfComments", type=IntegerType)
gast_functions_Function_linesOfCode: Property = Property(name="linesOfCode", type=IntegerType)
gast_functions_Function_numberOfEdgesInCFG: Property = Property(name="numberOfEdgesInCFG", type=IntegerType)
gast_functions_Function_numberOfNodesInCFG: Property = Property(name="numberOfNodesInCFG", type=IntegerType)
gast_functions_Function_operator: Property = Property(name="operator", type=BooleanType)
gast_functions_Function.attributes={gast_functions_Function_linesOfComments, gast_functions_Function_numberOfNodesInCFG, gast_functions_Function_linesOfCode, gast_functions_Function_numberOfEdgesInCFG, gast_functions_Function_maximumNestingLevel, gast_functions_Function_numberOfStatements, gast_functions_Function_operator}

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

# gast_variables_Property class attributes and methods

# variables_Field class attributes and methods

# gast_variables_GlobalVariable class attributes and methods

# gast_variables_LocalVariable class attributes and methods

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
branches28: BinaryAssociation = BinaryAssociation(
    name="branches28",
    ends={
        Property(name="Branch29", type=gast_statements_BranchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="branchstatement", type=Branch, multiplicity=Multiplicity(1, 9999), is_composite=True)
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
incrementExpression35: BinaryAssociation = BinaryAssociation(
    name="incrementExpression35",
    ends={
        Property(name="GASTExpression37", type=gast_statements_LoopStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_statements_LoopStatement36", type=GASTExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body38: BinaryAssociation = BinaryAssociation(
    name="body38",
    ends={
        Property(name="Statement39", type=gast_statements_LoopStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="loopstatement", type=Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
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
expression41: BinaryAssociation = BinaryAssociation(
    name="expression41",
    ends={
        Property(name="GASTExpression42", type=gast_statements_JumpStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_statements_JumpStatement", type=GASTExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
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
exit47: BinaryAssociation = BinaryAssociation(
    name="exit47",
    ends={
        Property(name="Exit", type=gast_statements_Methods, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_statements_Methods", type=Exit, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
use48: BinaryAssociation = BinaryAssociation(
    name="use48",
    ends={
        Property(name="Var", type=gast_statements_FlowInstr, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_statements_FlowInstr", type=Var, multiplicity=Multiplicity(0, 9999))
    }
)
def_49: BinaryAssociation = BinaryAssociation(
    name="def_49",
    ends={
        Property(name="Var51", type=gast_statements_FlowInstr, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_statements_FlowInstr50", type=Var, multiplicity=Multiplicity(0, 9999))
    }
)
cfnext52: BinaryAssociation = BinaryAssociation(
    name="cfnext52",
    ends={
        Property(name="FlowInstr", type=gast_statements_FlowInstr, multiplicity=Multiplicity(1, 1)),
        Property(name="cfPrev", type=FlowInstr, multiplicity=Multiplicity(0, 9999))
    }
)
cfPrev53: BinaryAssociation = BinaryAssociation(
    name="cfPrev53",
    ends={
        Property(name="FlowInstr54", type=gast_statements_FlowInstr, multiplicity=Multiplicity(1, 1)),
        Property(name="cfnext", type=FlowInstr, multiplicity=Multiplicity(0, 9999))
    }
)
catchParameter40: BinaryAssociation = BinaryAssociation(
    name="catchParameter40",
    ends={
        Property(name="CatchParameter", type=gast_statements_CatchBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_statements_CatchBlock", type=CatchParameter, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
root55: BinaryAssociation = BinaryAssociation(
    name="root55",
    ends={
        Property(name="Root", type=gast_core_BasePath, multiplicity=Multiplicity(1, 1)),
        Property(name="basePaths", type=Root, multiplicity=Multiplicity(1, 1))
    }
)
directories56: BinaryAssociation = BinaryAssociation(
    name="directories56",
    ends={
        Property(name="Directory", type=gast_core_BasePath, multiplicity=Multiplicity(1, 1)),
        Property(name="basePath", type=Directory, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotations57: BinaryAssociation = BinaryAssociation(
    name="annotations57",
    ends={
        Property(name="ModelAnnotation", type=gast_core_ModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_ModelElement", type=ModelAnnotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
allInnerClasses59: BinaryAssociation = BinaryAssociation(
    name="allInnerClasses59",
    ends={
        Property(name="GASTClass61", type=gast_core_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_Package60", type=GASTClass, multiplicity=Multiplicity(0, 9999))
    }
)
allNormalClasses62: BinaryAssociation = BinaryAssociation(
    name="allNormalClasses62",
    ends={
        Property(name="GASTClass64", type=gast_core_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_Package63", type=GASTClass, multiplicity=Multiplicity(0, 9999))
    }
)
allInterfaces65: BinaryAssociation = BinaryAssociation(
    name="allInterfaces65",
    ends={
        Property(name="GASTClass67", type=gast_core_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_Package66", type=GASTClass, multiplicity=Multiplicity(0, 9999))
    }
)
allAccesses68: BinaryAssociation = BinaryAssociation(
    name="allAccesses68",
    ends={
        Property(name="Access", type=gast_core_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_Package69", type=Access, multiplicity=Multiplicity(0, 9999))
    }
)
delegates70: BinaryAssociation = BinaryAssociation(
    name="delegates70",
    ends={
        Property(name="Delegate", type=gast_core_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="surroundingPackage", type=Delegate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
globalFunctions71: BinaryAssociation = BinaryAssociation(
    name="globalFunctions71",
    ends={
        Property(name="GlobalFunction", type=gast_core_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="surroundingPackage72", type=GlobalFunction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
globalVariables73: BinaryAssociation = BinaryAssociation(
    name="globalVariables73",
    ends={
        Property(name="GlobalVariable", type=gast_core_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="surroundingPackage74", type=GlobalVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
root75: BinaryAssociation = BinaryAssociation(
    name="root75",
    ends={
        Property(name="Root76", type=gast_core_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="packages", type=Root, multiplicity=Multiplicity(0, 1))
    }
)
classes77: BinaryAssociation = BinaryAssociation(
    name="classes77",
    ends={
        Property(name="GASTClass79", type=gast_core_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="surroundingPackage78", type=GASTClass, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subPackages80: BinaryAssociation = BinaryAssociation(
    name="subPackages80",
    ends={
        Property(name="Package", type=gast_core_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="surroundingPackage81", type=Package, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
allLocalClasses58: BinaryAssociation = BinaryAssociation(
    name="allLocalClasses58",
    ends={
        Property(name="GASTClass", type=gast_core_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_Package", type=GASTClass, multiplicity=Multiplicity(0, 9999))
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
        Property(name="TypeAlias", type=gast_core_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="surroundingPackage88", type=TypeAlias, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
surroundingPackage82: BinaryAssociation = BinaryAssociation(
    name="surroundingPackage82",
    ends={
        Property(name="Package83", type=gast_core_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="subPackages", type=Package, multiplicity=Multiplicity(0, 1))
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
        Property(name="Package110", type=gast_core_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="root", type=Package, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
clones111: BinaryAssociation = BinaryAssociation(
    name="clones111",
    ends={
        Property(name="Clone", type=gast_core_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="root112", type=Clone, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
structuralAbstractions113: BinaryAssociation = BinaryAssociation(
    name="structuralAbstractions113",
    ends={
        Property(name="StructuralAbstraction", type=gast_core_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_Root114", type=StructuralAbstraction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
types115: BinaryAssociation = BinaryAssociation(
    name="types115",
    ends={
        Property(name="GASTType", type=gast_core_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_Root116", type=GASTType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
danglingModelElements117: BinaryAssociation = BinaryAssociation(
    name="danglingModelElements117",
    ends={
        Property(name="ModelElement119", type=gast_core_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_Root118", type=ModelElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
basePaths120: BinaryAssociation = BinaryAssociation(
    name="basePaths120",
    ends={
        Property(name="BasePath", type=gast_core_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="root121", type=BasePath, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
globalFunctions122: BinaryAssociation = BinaryAssociation(
    name="globalFunctions122",
    ends={
        Property(name="GlobalFunction124", type=gast_core_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="root123", type=GlobalFunction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
allModelElements104: BinaryAssociation = BinaryAssociation(
    name="allModelElements104",
    ends={
        Property(name="ModelElement", type=gast_core_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_Root105", type=ModelElement, multiplicity=Multiplicity(0, 9999))
    }
)
subDirectory125: BinaryAssociation = BinaryAssociation(
    name="subDirectory125",
    ends={
        Property(name="Directory126", type=gast_core_Directory, multiplicity=Multiplicity(1, 1)),
        Property(name="parentDirectory", type=Directory, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentDirectory127: BinaryAssociation = BinaryAssociation(
    name="parentDirectory127",
    ends={
        Property(name="Directory128", type=gast_core_Directory, multiplicity=Multiplicity(1, 1)),
        Property(name="subDirectory", type=Directory, multiplicity=Multiplicity(0, 1))
    }
)
files129: BinaryAssociation = BinaryAssociation(
    name="files129",
    ends={
        Property(name="File", type=gast_core_Directory, multiplicity=Multiplicity(1, 1)),
        Property(name="directory", type=File, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
basePath130: BinaryAssociation = BinaryAssociation(
    name="basePath130",
    ends={
        Property(name="BasePath131", type=gast_core_Directory, multiplicity=Multiplicity(1, 1)),
        Property(name="directories", type=BasePath, multiplicity=Multiplicity(0, 1))
    }
)
root132: BinaryAssociation = BinaryAssociation(
    name="root132",
    ends={
        Property(name="Root133", type=gast_core_File, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_File", type=Root, multiplicity=Multiplicity(1, 1))
    }
)
importedTypes134: BinaryAssociation = BinaryAssociation(
    name="importedTypes134",
    ends={
        Property(name="GASTType136", type=gast_core_File, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_File135", type=GASTType, multiplicity=Multiplicity(0, 9999))
    }
)
types137: BinaryAssociation = BinaryAssociation(
    name="types137",
    ends={
        Property(name="GASTType139", type=gast_core_File, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_File138", type=GASTType, multiplicity=Multiplicity(0, 9999))
    }
)
globalVariables140: BinaryAssociation = BinaryAssociation(
    name="globalVariables140",
    ends={
        Property(name="GlobalVariable142", type=gast_core_File, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_File141", type=GlobalVariable, multiplicity=Multiplicity(0, 9999))
    }
)
globalFunctions143: BinaryAssociation = BinaryAssociation(
    name="globalFunctions143",
    ends={
        Property(name="GlobalFunction145", type=gast_core_File, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_File144", type=GlobalFunction, multiplicity=Multiplicity(0, 9999))
    }
)
importedGlobalFunctions146: BinaryAssociation = BinaryAssociation(
    name="importedGlobalFunctions146",
    ends={
        Property(name="GlobalFunction148", type=gast_core_File, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_File147", type=GlobalFunction, multiplicity=Multiplicity(0, 9999))
    }
)
importedGlobalVariables149: BinaryAssociation = BinaryAssociation(
    name="importedGlobalVariables149",
    ends={
        Property(name="GlobalVariable151", type=gast_core_File, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_File150", type=GlobalVariable, multiplicity=Multiplicity(0, 9999))
    }
)
importedPackages152: BinaryAssociation = BinaryAssociation(
    name="importedPackages152",
    ends={
        Property(name="Package154", type=gast_core_File, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_File153", type=Package, multiplicity=Multiplicity(0, 9999))
    }
)
includedFiles155: BinaryAssociation = BinaryAssociation(
    name="includedFiles155",
    ends={
        Property(name="File157", type=gast_core_File, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_File156", type=File, multiplicity=Multiplicity(0, 9999))
    }
)
directory158: BinaryAssociation = BinaryAssociation(
    name="directory158",
    ends={
        Property(name="Directory159", type=gast_core_File, multiplicity=Multiplicity(1, 1)),
        Property(name="files", type=Directory, multiplicity=Multiplicity(1, 1))
    }
)
sourceFile160: BinaryAssociation = BinaryAssociation(
    name="sourceFile160",
    ends={
        Property(name="File161", type=gast_core_Position, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_Position", type=File, multiplicity=Multiplicity(0, 1))
    }
)
assembly162: BinaryAssociation = BinaryAssociation(
    name="assembly162",
    ends={
        Property(name="File164", type=gast_core_Position, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_core_Position163", type=File, multiplicity=Multiplicity(0, 1))
    }
)
sourceentity165: BinaryAssociation = BinaryAssociation(
    name="sourceentity165",
    ends={
        Property(name="SourceEntity", type=gast_core_Position, multiplicity=Multiplicity(1, 1)),
        Property(name="position", type=SourceEntity, multiplicity=Multiplicity(1, 1))
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
        Property(name="Position", type=gast_core_SourceEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="sourceentity", type=Position, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cloneInstances169: BinaryAssociation = BinaryAssociation(
    name="cloneInstances169",
    ends={
        Property(name="CloneInstance170", type=gast_annotations_Clone, multiplicity=Multiplicity(1, 1)),
        Property(name="clone", type=CloneInstance, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
root171: BinaryAssociation = BinaryAssociation(
    name="root171",
    ends={
        Property(name="Root172", type=gast_annotations_Clone, multiplicity=Multiplicity(1, 1)),
        Property(name="clones", type=Root, multiplicity=Multiplicity(1, 1))
    }
)
statements173: BinaryAssociation = BinaryAssociation(
    name="statements173",
    ends={
        Property(name="Statement174", type=gast_annotations_CloneInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="cloneInstance", type=Statement, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
clone175: BinaryAssociation = BinaryAssociation(
    name="clone175",
    ends={
        Property(name="Clone176", type=gast_annotations_CloneInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="cloneInstances", type=Clone, multiplicity=Multiplicity(1, 1))
    }
)
referencedType177: BinaryAssociation = BinaryAssociation(
    name="referencedType177",
    ends={
        Property(name="GASTType178", type=gast_types_Reference, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_types_Reference", type=GASTType, multiplicity=Multiplicity(1, 1))
    }
)
decoratedType179: BinaryAssociation = BinaryAssociation(
    name="decoratedType179",
    ends={
        Property(name="GASTType180", type=gast_types_TypeDecorator, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_types_TypeDecorator", type=GASTType, multiplicity=Multiplicity(1, 1))
    }
)
undecoratedType181: BinaryAssociation = BinaryAssociation(
    name="undecoratedType181",
    ends={
        Property(name="GASTType183", type=gast_types_TypeDecorator, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_types_TypeDecorator182", type=GASTType, multiplicity=Multiplicity(1, 1))
    }
)
baseType184: BinaryAssociation = BinaryAssociation(
    name="baseType184",
    ends={
        Property(name="GASTType185", type=gast_types_GASTArray, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_types_GASTArray", type=GASTType, multiplicity=Multiplicity(1, 1))
    }
)
aliasedType186: BinaryAssociation = BinaryAssociation(
    name="aliasedType186",
    ends={
        Property(name="GASTType187", type=gast_types_TypeAlias, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_types_TypeAlias", type=GASTType, multiplicity=Multiplicity(1, 1))
    }
)
surroundingClass188: BinaryAssociation = BinaryAssociation(
    name="surroundingClass188",
    ends={
        Property(name="GASTClass189", type=gast_types_TypeAlias, multiplicity=Multiplicity(1, 1)),
        Property(name="innerTypeAliases", type=GASTClass, multiplicity=Multiplicity(0, 1))
    }
)
surroundingPackage190: BinaryAssociation = BinaryAssociation(
    name="surroundingPackage190",
    ends={
        Property(name="Package191", type=gast_types_TypeAlias, multiplicity=Multiplicity(1, 1)),
        Property(name="typeAliases", type=Package, multiplicity=Multiplicity(0, 1))
    }
)
overriddenMember192: BinaryAssociation = BinaryAssociation(
    name="overriddenMember192",
    ends={
        Property(name="Member", type=gast_types_Member, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_types_Member", type=Member, multiplicity=Multiplicity(0, 1))
    }
)
typeBounds193: BinaryAssociation = BinaryAssociation(
    name="typeBounds193",
    ends={
        Property(name="GASTType194", type=gast_types_TypeParameterClass, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_types_TypeParameterClass", type=GASTType, multiplicity=Multiplicity(0, 9999))
    }
)
innerTypeAliases195: BinaryAssociation = BinaryAssociation(
    name="innerTypeAliases195",
    ends={
        Property(name="TypeAlias196", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="surroundingClass", type=TypeAlias, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
innerDelegates197: BinaryAssociation = BinaryAssociation(
    name="innerDelegates197",
    ends={
        Property(name="Delegate199", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="surroundingClass198", type=Delegate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
constructors200: BinaryAssociation = BinaryAssociation(
    name="constructors200",
    ends={
        Property(name="Constructor", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="surroundingClass201", type=Constructor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
destructors202: BinaryAssociation = BinaryAssociation(
    name="destructors202",
    ends={
        Property(name="Destructor", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="surroundingClass203", type=Destructor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fields204: BinaryAssociation = BinaryAssociation(
    name="fields204",
    ends={
        Property(name="Field", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="surroundingClass205", type=Field, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
methods206: BinaryAssociation = BinaryAssociation(
    name="methods206",
    ends={
        Property(name="Method", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="surroundingClass207", type=Method_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
surroundingFunction208: BinaryAssociation = BinaryAssociation(
    name="surroundingFunction208",
    ends={
        Property(name="Function209", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="localClasses", type=Function, multiplicity=Multiplicity(0, 1))
    }
)
surroundingPackage210: BinaryAssociation = BinaryAssociation(
    name="surroundingPackage210",
    ends={
        Property(name="Package211", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="classes", type=Package, multiplicity=Multiplicity(0, 1))
    }
)
superTypes212: BinaryAssociation = BinaryAssociation(
    name="superTypes212",
    ends={
        Property(name="GASTClass213", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_types_GASTClass", type=GASTClass, multiplicity=Multiplicity(0, 9999))
    }
)
innerClasses214: BinaryAssociation = BinaryAssociation(
    name="innerClasses214",
    ends={
        Property(name="GASTClass216", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="surroundingClass215", type=GASTClass, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
surroundingClass217: BinaryAssociation = BinaryAssociation(
    name="surroundingClass217",
    ends={
        Property(name="GASTClass218", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="innerClasses", type=GASTClass, multiplicity=Multiplicity(0, 1))
    }
)
inheritanceTypeAccesses219: BinaryAssociation = BinaryAssociation(
    name="inheritanceTypeAccesses219",
    ends={
        Property(name="InheritanceTypeAccess", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_types_GASTClass220", type=InheritanceTypeAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
self221: BinaryAssociation = BinaryAssociation(
    name="self221",
    ends={
        Property(name="Field223", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_types_GASTClass222", type=Field, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
friendClasses224: BinaryAssociation = BinaryAssociation(
    name="friendClasses224",
    ends={
        Property(name="GASTClass225", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="gastClass", type=GASTClass, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
gastClass226: BinaryAssociation = BinaryAssociation(
    name="gastClass226",
    ends={
        Property(name="GASTClass227", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="friendClasses", type=GASTClass, multiplicity=Multiplicity(0, 1))
    }
)
property231: BinaryAssociation = BinaryAssociation(
    name="property231",
    ends={
        Property(name="Property", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_types_GASTClass232", type=Property_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
allAccesses233: BinaryAssociation = BinaryAssociation(
    name="allAccesses233",
    ends={
        Property(name="Access235", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_types_GASTClass234", type=Access, multiplicity=Multiplicity(0, 9999))
    }
)
allAccessedClasses236: BinaryAssociation = BinaryAssociation(
    name="allAccessedClasses236",
    ends={
        Property(name="GASTClass238", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_types_GASTClass237", type=GASTClass, multiplicity=Multiplicity(0, 9999))
    }
)
targetType239: BinaryAssociation = BinaryAssociation(
    name="targetType239",
    ends={
        Property(name="GASTType240", type=gast_accesses_TypeAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_accesses_TypeAccess", type=GASTType, multiplicity=Multiplicity(1, 1))
    }
)
typeArguments241: BinaryAssociation = BinaryAssociation(
    name="typeArguments241",
    ends={
        Property(name="GASTType243", type=gast_accesses_TypeAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_accesses_TypeAccess242", type=GASTType, multiplicity=Multiplicity(0, 9999))
    }
)
accesses244: BinaryAssociation = BinaryAssociation(
    name="accesses244",
    ends={
        Property(name="BaseAccess245", type=gast_accesses_CompositeAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="surroundingCompositeAccess", type=BaseAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
friendFunctions228: BinaryAssociation = BinaryAssociation(
    name="friendFunctions228",
    ends={
        Property(name="Function230", type=gast_types_GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_types_GASTClass229", type=Function, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
surroundingStatement248: BinaryAssociation = BinaryAssociation(
    name="surroundingStatement248",
    ends={
        Property(name="Statement249", type=gast_accesses_BaseAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_accesses_BaseAccess", type=Statement, multiplicity=Multiplicity(0, 1))
    }
)
surroundingClass250: BinaryAssociation = BinaryAssociation(
    name="surroundingClass250",
    ends={
        Property(name="GASTClass252", type=gast_accesses_BaseAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_accesses_BaseAccess251", type=GASTClass, multiplicity=Multiplicity(1, 1))
    }
)
surroundingFunction253: BinaryAssociation = BinaryAssociation(
    name="surroundingFunction253",
    ends={
        Property(name="Function255", type=gast_accesses_BaseAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_accesses_BaseAccess254", type=Function, multiplicity=Multiplicity(0, 1))
    }
)
surroundingCompositeAccess256: BinaryAssociation = BinaryAssociation(
    name="surroundingCompositeAccess256",
    ends={
        Property(name="CompositeAccess", type=gast_accesses_BaseAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="accesses257", type=CompositeAccess, multiplicity=Multiplicity(0, 1))
    }
)
function258: BinaryAssociation = BinaryAssociation(
    name="function258",
    ends={
        Property(name="Function259", type=gast_accesses_DeclarationTypeAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="returnTypeDeclaration", type=Function, multiplicity=Multiplicity(0, 1))
    }
)
surroundingVariable260: BinaryAssociation = BinaryAssociation(
    name="surroundingVariable260",
    ends={
        Property(name="Variable", type=gast_accesses_DeclarationTypeAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="typeDeclaration", type=Variable, multiplicity=Multiplicity(0, 1))
    }
)
accessedFunctions261: BinaryAssociation = BinaryAssociation(
    name="accessedFunctions261",
    ends={
        Property(name="Function262", type=gast_accesses_DelegateAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_accesses_DelegateAccess", type=Function, multiplicity=Multiplicity(0, 9999))
    }
)
parentStatement246: BinaryAssociation = BinaryAssociation(
    name="parentStatement246",
    ends={
        Property(name="Statement247", type=gast_accesses_BaseAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="accesses", type=Statement, multiplicity=Multiplicity(0, 1))
    }
)
typeArguments266: BinaryAssociation = BinaryAssociation(
    name="typeArguments266",
    ends={
        Property(name="GASTType267", type=gast_accesses_FunctionAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_accesses_FunctionAccess", type=GASTType, multiplicity=Multiplicity(0, 9999))
    }
)
targetFunction268: BinaryAssociation = BinaryAssociation(
    name="targetFunction268",
    ends={
        Property(name="Function270", type=gast_accesses_FunctionAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_accesses_FunctionAccess269", type=Function, multiplicity=Multiplicity(1, 1))
    }
)
targetVariable271: BinaryAssociation = BinaryAssociation(
    name="targetVariable271",
    ends={
        Property(name="Variable272", type=gast_accesses_VariableAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_accesses_VariableAccess", type=Variable, multiplicity=Multiplicity(1, 1))
    }
)
accessedDelegate263: BinaryAssociation = BinaryAssociation(
    name="accessedDelegate263",
    ends={
        Property(name="Delegate265", type=gast_accesses_DelegateAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_accesses_DelegateAccess264", type=Delegate, multiplicity=Multiplicity(1, 1))
    }
)
accessedClass273: BinaryAssociation = BinaryAssociation(
    name="accessedClass273",
    ends={
        Property(name="gast_accesses_Access", type=GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="GASTClass274", type=gast_accesses_Access, multiplicity=Multiplicity(1, 1))
    }
)
accessedTarget275: BinaryAssociation = BinaryAssociation(
    name="accessedTarget275",
    ends={
        Property(name="ModelElement277", type=gast_accesses_Access, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_accesses_Access276", type=ModelElement, multiplicity=Multiplicity(1, 1))
    }
)
superClass278: BinaryAssociation = BinaryAssociation(
    name="superClass278",
    ends={
        Property(name="GASTClass279", type=gast_functions_Delegate, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_functions_Delegate", type=GASTClass, multiplicity=Multiplicity(0, 1))
    }
)
invocations280: BinaryAssociation = BinaryAssociation(
    name="invocations280",
    ends={
        Property(name="Function282", type=gast_functions_Delegate, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_functions_Delegate281", type=Function, multiplicity=Multiplicity(0, 9999))
    }
)
surroundingClass283: BinaryAssociation = BinaryAssociation(
    name="surroundingClass283",
    ends={
        Property(name="GASTClass284", type=gast_functions_Delegate, multiplicity=Multiplicity(1, 1)),
        Property(name="innerDelegates", type=GASTClass, multiplicity=Multiplicity(0, 1))
    }
)
surroundingPackage285: BinaryAssociation = BinaryAssociation(
    name="surroundingPackage285",
    ends={
        Property(name="Package286", type=gast_functions_Delegate, multiplicity=Multiplicity(1, 1)),
        Property(name="delegates", type=Package, multiplicity=Multiplicity(0, 1))
    }
)
surroundingClass287: BinaryAssociation = BinaryAssociation(
    name="surroundingClass287",
    ends={
        Property(name="constructors", type=GASTClass, multiplicity=Multiplicity(1, 1)),
        Property(name="GASTClass288", type=gast_functions_Constructor, multiplicity=Multiplicity(1, 1))
    }
)
surroundingClass289: BinaryAssociation = BinaryAssociation(
    name="surroundingClass289",
    ends={
        Property(name="GASTClass290", type=gast_functions_Destructor, multiplicity=Multiplicity(1, 1)),
        Property(name="destructors", type=GASTClass, multiplicity=Multiplicity(1, 1))
    }
)
surroundingPackage291: BinaryAssociation = BinaryAssociation(
    name="surroundingPackage291",
    ends={
        Property(name="Package292", type=gast_functions_GlobalFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="globalFunctions", type=Package, multiplicity=Multiplicity(0, 1))
    }
)
root293: BinaryAssociation = BinaryAssociation(
    name="root293",
    ends={
        Property(name="Root295", type=gast_functions_GlobalFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="globalFunctions294", type=Root, multiplicity=Multiplicity(0, 1))
    }
)
surroundingProperty296: BinaryAssociation = BinaryAssociation(
    name="surroundingProperty296",
    ends={
        Property(name="Property297", type=gast_functions_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_functions_Method", type=Property_, multiplicity=Multiplicity(0, 1))
    }
)
surroundingClass298: BinaryAssociation = BinaryAssociation(
    name="surroundingClass298",
    ends={
        Property(name="GASTClass299", type=gast_functions_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="methods", type=GASTClass, multiplicity=Multiplicity(1, 1))
    }
)
returnTypeDeclaration300: BinaryAssociation = BinaryAssociation(
    name="returnTypeDeclaration300",
    ends={
        Property(name="DeclarationTypeAccess", type=gast_functions_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="function", type=DeclarationTypeAccess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
formalParameters301: BinaryAssociation = BinaryAssociation(
    name="formalParameters301",
    ends={
        Property(name="FormalParameter", type=gast_functions_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="surroundingFunction", type=FormalParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
localVariables302: BinaryAssociation = BinaryAssociation(
    name="localVariables302",
    ends={
        Property(name="LocalVariable", type=gast_functions_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="surroundingFunction303", type=LocalVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
allStatements304: BinaryAssociation = BinaryAssociation(
    name="allStatements304",
    ends={
        Property(name="Statement305", type=gast_functions_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_functions_Function", type=Statement, multiplicity=Multiplicity(0, 9999))
    }
)
throwTypeAccesses306: BinaryAssociation = BinaryAssociation(
    name="throwTypeAccesses306",
    ends={
        Property(name="ThrowTypeAccess", type=gast_functions_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_functions_Function307", type=ThrowTypeAccess, multiplicity=Multiplicity(0, 9999))
    }
)
accesses308: BinaryAssociation = BinaryAssociation(
    name="accesses308",
    ends={
        Property(name="Access310", type=gast_functions_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_functions_Function309", type=Access, multiplicity=Multiplicity(0, 9999))
    }
)
localClasses314: BinaryAssociation = BinaryAssociation(
    name="localClasses314",
    ends={
        Property(name="GASTClass316", type=gast_functions_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="surroundingFunction315", type=GASTClass, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
surroundingFunction317: BinaryAssociation = BinaryAssociation(
    name="surroundingFunction317",
    ends={
        Property(name="Function318", type=gast_variables_FormalParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="formalParameters", type=Function, multiplicity=Multiplicity(1, 1))
    }
)
type319: BinaryAssociation = BinaryAssociation(
    name="type319",
    ends={
        Property(name="GASTType320", type=gast_variables_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_variables_Variable", type=GASTType, multiplicity=Multiplicity(1, 1))
    }
)
typeDeclaration321: BinaryAssociation = BinaryAssociation(
    name="typeDeclaration321",
    ends={
        Property(name="DeclarationTypeAccess322", type=gast_variables_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="surroundingVariable", type=DeclarationTypeAccess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
surroundingClass323: BinaryAssociation = BinaryAssociation(
    name="surroundingClass323",
    ends={
        Property(name="GASTClass324", type=gast_variables_Field, multiplicity=Multiplicity(1, 1)),
        Property(name="fields", type=GASTClass, multiplicity=Multiplicity(0, 1))
    }
)
body311: BinaryAssociation = BinaryAssociation(
    name="body311",
    ends={
        Property(name="BlockStatement313", type=gast_functions_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="surroundingFunction312", type=BlockStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
surroundingFunction325: BinaryAssociation = BinaryAssociation(
    name="surroundingFunction325",
    ends={
        Property(name="Function326", type=gast_variables_LocalVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="localVariables", type=Function, multiplicity=Multiplicity(1, 1))
    }
)
setter327: BinaryAssociation = BinaryAssociation(
    name="setter327",
    ends={
        Property(name="Method328", type=gast_variables_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_variables_Property", type=Method_, multiplicity=Multiplicity(0, 1))
    }
)
getter329: BinaryAssociation = BinaryAssociation(
    name="getter329",
    ends={
        Property(name="Method331", type=gast_variables_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="gast_variables_Property330", type=Method_, multiplicity=Multiplicity(0, 1))
    }
)
surroundingPackage332: BinaryAssociation = BinaryAssociation(
    name="surroundingPackage332",
    ends={
        Property(name="Package333", type=gast_variables_GlobalVariable, multiplicity=Multiplicity(1, 1)),
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
gen_gast_statements_SimpleStatement_statements_Statement = Generalization(general=statements_Statement, specific=gast_statements_SimpleStatement)
gen_gast_statements_SimpleStatement_statements_FlowInstr = Generalization(general=statements_FlowInstr, specific=gast_statements_SimpleStatement)
gen_gast_statements_Methods_statements_BlockStatement = Generalization(general=statements_BlockStatement, specific=gast_statements_Methods)
gen_gast_statements_Methods_statements_FlowInstr = Generalization(general=statements_FlowInstr, specific=gast_statements_Methods)
gen_gast_statements_Exit_FlowInstr = Generalization(general=FlowInstr, specific=gast_statements_Exit)
gen_gast_statements_JumpStatement_statements_Statement = Generalization(general=statements_Statement, specific=gast_statements_JumpStatement)
gen_gast_statements_JumpStatement_statements_FlowInstr = Generalization(general=statements_FlowInstr, specific=gast_statements_JumpStatement)
gen_gast_statements_Param_Var = Generalization(general=Var, specific=gast_statements_Param)
gen_gast_core_BasePath_ModelElement = Generalization(general=ModelElement, specific=gast_core_BasePath)
gen_gast_core_ModelElement_Identifier = Generalization(general=Identifier, specific=gast_core_ModelElement)
gen_gast_core_NamedModelElement_ModelElement = Generalization(general=ModelElement, specific=gast_core_NamedModelElement)
gen_gast_core_Package_NamedModelElement = Generalization(general=NamedModelElement, specific=gast_core_Package)
gen_gast_core_GenericEntity_ModelElement = Generalization(general=ModelElement, specific=gast_core_GenericEntity)
gen_gast_core_Root_ModelElement = Generalization(general=ModelElement, specific=gast_core_Root)
gen_gast_core_Directory_NamedModelElement = Generalization(general=NamedModelElement, specific=gast_core_Directory)
gen_gast_core_File_NamedModelElement = Generalization(general=NamedModelElement, specific=gast_core_File)
gen_gast_core_PackageAlias_Package = Generalization(general=Package, specific=gast_core_PackageAlias)
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
gen_gast_core_SourceEntity_ModelElement = Generalization(general=ModelElement, specific=gast_core_SourceEntity)
gen_gast_annotations_Subsystem_StructuralAbstraction = Generalization(general=StructuralAbstraction, specific=gast_annotations_Subsystem)
gen_gast_annotations_Layer_StructuralAbstraction = Generalization(general=StructuralAbstraction, specific=gast_annotations_Layer)
gen_gast_types_Reference_TypeDecorator = Generalization(general=TypeDecorator, specific=gast_types_Reference)
gen_gast_types_TypeDecorator_GASTType = Generalization(general=GASTType, specific=gast_types_TypeDecorator)
gen_gast_types_GASTType_NamedModelElement = Generalization(general=NamedModelElement, specific=gast_types_GASTType)
gen_gast_types_TypeAlias_types_Member = Generalization(general=types_Member, specific=gast_types_TypeAlias)
gen_gast_types_TypeAlias_types_TypeDecorator = Generalization(general=types_TypeDecorator, specific=gast_types_TypeAlias)
gen_gast_types_Member_SourceEntity = Generalization(general=SourceEntity, specific=gast_types_Member)
gen_gast_types_GASTArray_TypeDecorator = Generalization(general=TypeDecorator, specific=gast_types_GASTArray)
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
gen_gast_accesses_StaticTypeAccess_TypeAccess = Generalization(general=TypeAccess, specific=gast_accesses_StaticTypeAccess)
gen_gast_accesses_PropertyAccess_VariableAccess = Generalization(general=VariableAccess, specific=gast_accesses_PropertyAccess)
gen_gast_accesses_Access_BaseAccess = Generalization(general=BaseAccess, specific=gast_accesses_Access)
gen_gast_functions_Delegate_functions_Function = Generalization(general=functions_Function, specific=gast_functions_Delegate)
gen_gast_functions_Delegate_types_Member = Generalization(general=types_Member, specific=gast_functions_Delegate)
gen_gast_functions_Delegate_types_GASTType = Generalization(general=types_GASTType, specific=gast_functions_Delegate)
gen_gast_functions_Constructor_functions_Function = Generalization(general=functions_Function, specific=gast_functions_Constructor)
gen_gast_functions_Constructor_types_Member = Generalization(general=types_Member, specific=gast_functions_Constructor)
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
gen_gast_variables_FormalParameter_Variable = Generalization(general=Variable, specific=gast_variables_FormalParameter)
gen_gast_variables_Variable_core_NamedModelElement = Generalization(general=core_NamedModelElement, specific=gast_variables_Variable)
gen_gast_variables_Variable_core_SourceEntity = Generalization(general=core_SourceEntity, specific=gast_variables_Variable)
gen_gast_variables_CatchParameter_Variable = Generalization(general=Variable, specific=gast_variables_CatchParameter)
gen_gast_variables_Field_types_Member = Generalization(general=types_Member, specific=gast_variables_Field)
gen_gast_variables_Field_variables_Variable = Generalization(general=variables_Variable, specific=gast_variables_Field)
gen_gast_variables_Property_variables_Field = Generalization(general=variables_Field, specific=gast_variables_Property)
gen_gast_variables_Property_types_Member = Generalization(general=types_Member, specific=gast_variables_Property)
gen_gast_variables_GlobalVariable_Variable = Generalization(general=Variable, specific=gast_variables_GlobalVariable)
gen_gast_variables_LocalVariable_Variable = Generalization(general=Variable, specific=gast_variables_LocalVariable)

# Domain Model
domain_model = DomainModel(
    name="gast",
    types={gast_statements_ExceptionHandler, Statement, CatchBlock, BlockStatement, gast_statements_Statement, SourceEntity, BaseAccess, CloneInstance, Branch, LoopStatement, gast_statements_BlockStatement, Function, gast_statements_Branch, GASTExpression, gast_statements_GASTExpression, gast_statements_BranchStatement, gast_statements_LoopStatement, gast_statements_CatchBlock, CatchParameter, BranchStatement, gast_statements_SimpleStatement, gast_statements_GASTBehaviour, gast_statements_Methods, statements_BlockStatement, Exit, gast_statements_Exit, FlowInstr, gast_statements_FlowInstr, Var, gast_statements_JumpStatement, statements_Statement, statements_FlowInstr, gast_core_BasePath, ModelElement, Root, Directory, gast_core_ModelElement, Identifier, ModelAnnotation, gast_core_Identifier, gast_core_NamedModelElement, gast_core_Package, NamedModelElement, gast_statements_Var, gast_statements_Param, Access, Delegate, GlobalFunction, GlobalVariable, Package, GASTClass, TypeAlias, gast_core_GenericEntity, TypeParameterClass, gast_core_Root, Clone, StructuralAbstraction, GASTType, BasePath, gast_core_Directory, File, gast_core_File, gast_core_Position, gast_core_PackageAlias, Position, gast_annotations_Attribute, types_GASTClass, annotations_ModelAnnotation, gast_annotations_Clone, core_ModelElement, gast_annotations_CloneInstance, gast_annotations_StructuralAbstraction, core_NamedModelElement, gast_annotations_Comment, core_SourceEntity, gast_core_SourceEntity, gast_annotations_Subsystem, gast_annotations_Layer, gast_annotations_ModelAnnotation, gast_types_Reference, TypeDecorator, gast_types_TypeDecorator, gast_types_GASTType, gast_types_TypeAlias, types_Member, types_TypeDecorator, gast_types_Member, Member, gast_types_GASTArray, gast_types_TypeParameterClass, gast_types_GenericClass, core_GenericEntity, gast_types_GASTEnumeration, gast_types_GASTStruct, gast_types_GASTUnion, Constructor, Destructor, Field, Method_, gast_types_GASTClass, types_GASTType, InheritanceTypeAccess, Property_, gast_accesses_ParameterInstantiationTypeAccess, TypeAccess, gast_accesses_TypeAccess, gast_accesses_CastTypeAccess, gast_accesses_CompositeAccess, gast_accesses_BaseAccess, CompositeAccess, gast_accesses_DeclarationTypeAccess, Variable, gast_accesses_ThrowTypeAccess, gast_accesses_DelegateAccess, FunctionAccess, gast_accesses_FunctionAccess, gast_accesses_InheritanceTypeAccess, gast_accesses_VariableAccess, gast_accesses_RunTimeTypeAccess, gast_accesses_SelfAccess, VariableAccess, gast_accesses_StaticTypeAccess, gast_accesses_PropertyAccess, gast_accesses_Access, gast_functions_Delegate, functions_Function, gast_functions_Constructor, gast_functions_Destructor, gast_functions_GenericFunction, functions_GlobalFunction, gast_functions_GlobalFunction, gast_functions_Method, gast_functions_GenericMethod, functions_Method, gast_functions_GenericConstructor, functions_Constructor, DeclarationTypeAccess, FormalParameter, LocalVariable, ThrowTypeAccess, gast_functions_Function, gast_variables_FormalParameter, gast_variables_Variable, gast_variables_CatchParameter, gast_variables_Field, variables_Variable, gast_variables_Property, variables_Field, gast_variables_GlobalVariable, gast_variables_LocalVariable, LoopStatementKind, JumpStatementKind, Status, Visibilities, GlobalFunctionKind},
    associations={catchBlocks0, finallyBlock1, guardedBlock3, accesses6, cloneInstance7, blockstatement8, surroundingStatement11, branch12, loopstatement13, cfPre14, cfNext17, statements20, surroundingFunction22, conditionExpression24, branches28, breakConditionExpression30, initExpression32, incrementExpression35, body38, branchstatement25, statement26, expression41, expression43, blockstatement45, exit47, use48, def_49, cfnext52, cfPrev53, catchParameter40, root55, directories56, annotations57, allInnerClasses59, allNormalClasses62, allInterfaces65, allAccesses68, delegates70, globalFunctions71, globalVariables73, root75, classes77, subPackages80, allLocalClasses58, allAccessedPackages84, typeAliases87, typeParameters89, allAccesses90, allInnerClasses92, allInterfaces95, allLocalClasses98, allNormalClasses101, surroundingPackage82, globalVariables106, packages109, clones111, structuralAbstractions113, types115, danglingModelElements117, basePaths120, globalFunctions122, allModelElements104, subDirectory125, parentDirectory127, files129, basePath130, root132, importedTypes134, types137, globalVariables140, globalFunctions143, importedGlobalFunctions146, importedGlobalVariables149, importedPackages152, includedFiles155, directory158, sourceFile160, assembly162, sourceentity165, aliasedPackage166, position168, cloneInstances169, root171, statements173, clone175, referencedType177, decoratedType179, undecoratedType181, baseType184, aliasedType186, surroundingClass188, surroundingPackage190, overriddenMember192, typeBounds193, innerTypeAliases195, innerDelegates197, constructors200, destructors202, fields204, methods206, surroundingFunction208, surroundingPackage210, superTypes212, innerClasses214, surroundingClass217, inheritanceTypeAccesses219, self221, friendClasses224, gastClass226, property231, allAccesses233, allAccessedClasses236, targetType239, typeArguments241, accesses244, friendFunctions228, surroundingStatement248, surroundingClass250, surroundingFunction253, surroundingCompositeAccess256, function258, surroundingVariable260, accessedFunctions261, parentStatement246, typeArguments266, targetFunction268, targetVariable271, accessedDelegate263, accessedClass273, accessedTarget275, superClass278, invocations280, surroundingClass283, surroundingPackage285, surroundingClass287, surroundingClass289, surroundingPackage291, root293, surroundingProperty296, surroundingClass298, returnTypeDeclaration300, formalParameters301, localVariables302, allStatements304, throwTypeAccesses306, accesses308, localClasses314, surroundingFunction317, type319, typeDeclaration321, surroundingClass323, body311, surroundingFunction325, setter327, getter329, surroundingPackage332},
    generalizations={gen_gast_statements_ExceptionHandler_Statement, gen_gast_statements_Statement_SourceEntity, gen_gast_statements_BlockStatement_Statement, gen_gast_statements_Branch_SourceEntity, gen_gast_statements_GASTExpression_SourceEntity, gen_gast_statements_BranchStatement_Statement, gen_gast_statements_LoopStatement_Statement, gen_gast_statements_CatchBlock_BlockStatement, gen_gast_statements_SimpleStatement_statements_Statement, gen_gast_statements_SimpleStatement_statements_FlowInstr, gen_gast_statements_Methods_statements_BlockStatement, gen_gast_statements_Methods_statements_FlowInstr, gen_gast_statements_Exit_FlowInstr, gen_gast_statements_JumpStatement_statements_Statement, gen_gast_statements_JumpStatement_statements_FlowInstr, gen_gast_statements_Param_Var, gen_gast_core_BasePath_ModelElement, gen_gast_core_ModelElement_Identifier, gen_gast_core_NamedModelElement_ModelElement, gen_gast_core_Package_NamedModelElement, gen_gast_core_GenericEntity_ModelElement, gen_gast_core_Root_ModelElement, gen_gast_core_Directory_NamedModelElement, gen_gast_core_File_NamedModelElement, gen_gast_core_PackageAlias_Package, gen_gast_annotations_Attribute_types_GASTClass, gen_gast_annotations_Attribute_annotations_ModelAnnotation, gen_gast_annotations_Clone_core_ModelElement, gen_gast_annotations_Clone_annotations_ModelAnnotation, gen_gast_annotations_CloneInstance_core_ModelElement, gen_gast_annotations_CloneInstance_annotations_ModelAnnotation, gen_gast_annotations_StructuralAbstraction_core_NamedModelElement, gen_gast_annotations_StructuralAbstraction_annotations_ModelAnnotation, gen_gast_annotations_Comment_core_SourceEntity, gen_gast_annotations_Comment_annotations_ModelAnnotation, gen_gast_core_SourceEntity_ModelElement, gen_gast_annotations_Subsystem_StructuralAbstraction, gen_gast_annotations_Layer_StructuralAbstraction, gen_gast_types_Reference_TypeDecorator, gen_gast_types_TypeDecorator_GASTType, gen_gast_types_GASTType_NamedModelElement, gen_gast_types_TypeAlias_types_Member, gen_gast_types_TypeAlias_types_TypeDecorator, gen_gast_types_Member_SourceEntity, gen_gast_types_GASTArray_TypeDecorator, gen_gast_types_TypeParameterClass_GASTClass, gen_gast_types_GenericClass_types_GASTClass, gen_gast_types_GenericClass_core_GenericEntity, gen_gast_types_GASTEnumeration_GASTClass, gen_gast_types_GASTStruct_GASTClass, gen_gast_types_GASTUnion_GASTClass, gen_gast_types_GASTClass_types_Member, gen_gast_types_GASTClass_types_GASTType, gen_gast_accesses_ParameterInstantiationTypeAccess_TypeAccess, gen_gast_accesses_TypeAccess_Access, gen_gast_accesses_CastTypeAccess_TypeAccess, gen_gast_accesses_CompositeAccess_BaseAccess, gen_gast_accesses_BaseAccess_SourceEntity, gen_gast_accesses_DeclarationTypeAccess_TypeAccess, gen_gast_accesses_ThrowTypeAccess_TypeAccess, gen_gast_accesses_DelegateAccess_FunctionAccess, gen_gast_accesses_FunctionAccess_Access, gen_gast_accesses_InheritanceTypeAccess_TypeAccess, gen_gast_accesses_VariableAccess_Access, gen_gast_accesses_RunTimeTypeAccess_TypeAccess, gen_gast_accesses_SelfAccess_VariableAccess, gen_gast_accesses_StaticTypeAccess_TypeAccess, gen_gast_accesses_PropertyAccess_VariableAccess, gen_gast_accesses_Access_BaseAccess, gen_gast_functions_Delegate_functions_Function, gen_gast_functions_Delegate_types_Member, gen_gast_functions_Delegate_types_GASTType, gen_gast_functions_Constructor_functions_Function, gen_gast_functions_Constructor_types_Member, gen_gast_functions_Destructor_functions_Function, gen_gast_functions_Destructor_types_Member, gen_gast_functions_GenericFunction_functions_GlobalFunction, gen_gast_functions_GenericFunction_core_GenericEntity, gen_gast_functions_GlobalFunction_Function, gen_gast_functions_Method_functions_Function, gen_gast_functions_Method_types_Member, gen_gast_functions_GenericMethod_functions_Method, gen_gast_functions_GenericMethod_core_GenericEntity, gen_gast_functions_GenericConstructor_functions_Constructor, gen_gast_functions_GenericConstructor_core_GenericEntity, gen_gast_functions_Function_core_NamedModelElement, gen_gast_functions_Function_core_SourceEntity, gen_gast_variables_FormalParameter_Variable, gen_gast_variables_Variable_core_NamedModelElement, gen_gast_variables_Variable_core_SourceEntity, gen_gast_variables_CatchParameter_Variable, gen_gast_variables_Field_types_Member, gen_gast_variables_Field_variables_Variable, gen_gast_variables_Property_variables_Field, gen_gast_variables_Property_types_Member, gen_gast_variables_GlobalVariable_Variable, gen_gast_variables_LocalVariable_Variable},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)