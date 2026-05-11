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
EqualityOpEnum: Enumeration = Enumeration(
    name="EqualityOpEnum",
    literals={
            EnumerationLiteral(name="EQ"),
			EnumerationLiteral(name="NOTEQ")
    }
)

ComparisonOpEnum: Enumeration = Enumeration(
    name="ComparisonOpEnum",
    literals={
            EnumerationLiteral(name="LT"),
			EnumerationLiteral(name="GT"),
			EnumerationLiteral(name="LTE"),
			EnumerationLiteral(name="GTE"),
			EnumerationLiteral(name="IN")
    }
)

ShiftOpEnum: Enumeration = Enumeration(
    name="ShiftOpEnum",
    literals={
            EnumerationLiteral(name="LEFT_SHIFT"),
			EnumerationLiteral(name="RIGHT_SHIFT"),
			EnumerationLiteral(name="ARITHMETIC_RIGHT_SHIFT")
    }
)

AdditionOpEnum: Enumeration = Enumeration(
    name="AdditionOpEnum",
    literals={
            EnumerationLiteral(name="ADD"),
			EnumerationLiteral(name="SUB")
    }
)

AssignmentOpEnum: Enumeration = Enumeration(
    name="AssignmentOpEnum",
    literals={
            EnumerationLiteral(name="ASSIGN_XOR"),
			EnumerationLiteral(name="ASSIGN_AND"),
			EnumerationLiteral(name="ASSIGN_SHIFT_LEFT"),
			EnumerationLiteral(name="ASSIGN_SHIFT_RIGHT"),
			EnumerationLiteral(name="ASSIGN_SHIFT_RIGHT_ARIMETIC"),
			EnumerationLiteral(name="ASSIGN_ADD"),
			EnumerationLiteral(name="ASSIGN_SUB"),
			EnumerationLiteral(name="ASSIGN_MULT"),
			EnumerationLiteral(name="ASSIGN_DIV"),
			EnumerationLiteral(name="ASSIGN_MOD"),
			EnumerationLiteral(name="ASSIGN"),
			EnumerationLiteral(name="ASSIGN_OR")
    }
)

MulDivModOpEnum: Enumeration = Enumeration(
    name="MulDivModOpEnum",
    literals={
            EnumerationLiteral(name="MULT"),
			EnumerationLiteral(name="DIV"),
			EnumerationLiteral(name="MOD")
    }
)

IncDecOpEnum: Enumeration = Enumeration(
    name="IncDecOpEnum",
    literals={
            EnumerationLiteral(name="INC"),
			EnumerationLiteral(name="DEC")
    }
)

SpecialExpressionTypeEnum: Enumeration = Enumeration(
    name="SpecialExpressionTypeEnum",
    literals={
            EnumerationLiteral(name="SUPER"),
			EnumerationLiteral(name="THIS")
    }
)

ReservedWordsEnum: Enumeration = Enumeration(
    name="ReservedWordsEnum",
    literals={
            EnumerationLiteral(name="AS"),
			EnumerationLiteral(name="CASE"),
			EnumerationLiteral(name="CATCH"),
			EnumerationLiteral(name="FINAL"),
			EnumerationLiteral(name="LET"),
			EnumerationLiteral(name="MATCH"),
			EnumerationLiteral(name="OF"),
			EnumerationLiteral(name="RELOCATABLE"),
			EnumerationLiteral(name="SWITCH"),
			EnumerationLiteral(name="TRY"),
			EnumerationLiteral(name="TYPE"),
			EnumerationLiteral(name="TYPEOF"),
			EnumerationLiteral(name="USING"),
			EnumerationLiteral(name="ILLEGAL")
    }
)

# Classes
optGrammar_Model = Class(name="optGrammar_Model")
optGrammar_PragmaDirective = Class(name="optGrammar_PragmaDirective")
optGrammar_DefinitionBody = Class(name="optGrammar_DefinitionBody")
optGrammar_ConstructorDefinition = Class(name="optGrammar_ConstructorDefinition")
DefinitionBody = Class(name="DefinitionBody")
optGrammar_ParameterList = Class(name="optGrammar_ParameterList")
optGrammar_StateMutability = Class(name="optGrammar_StateMutability")
optGrammar_Const = Class(name="optGrammar_Const")
optGrammar_ModifierInvocation = Class(name="optGrammar_ModifierInvocation")
optGrammar_ImportDirective = Class(name="optGrammar_ImportDirective")
optGrammar_Contract = Class(name="optGrammar_Contract")
optGrammar_versionOperator = Class(name="optGrammar_versionOperator")
optGrammar_SymbolAlias = Class(name="optGrammar_SymbolAlias")
optGrammar_InheritanceSpecifier = Class(name="optGrammar_InheritanceSpecifier")
optGrammar_FunctionDefinition = Class(name="optGrammar_FunctionDefinition")
optGrammar_VisibilityLiteral = Class(name="optGrammar_VisibilityLiteral")
optGrammar_Body = Class(name="optGrammar_Body")
optGrammar_FunctionCallListArguments = Class(name="optGrammar_FunctionCallListArguments")
FunctionCallArguments = Class(name="FunctionCallArguments")
optGrammar_Expression = Class(name="optGrammar_Expression")
optGrammar_FunctionCallArguments = Class(name="optGrammar_FunctionCallArguments")
optGrammar_FunctionCallArg = Class(name="optGrammar_FunctionCallArg")
optGrammar_PrimaryTypeDeclaration = Class(name="optGrammar_PrimaryTypeDeclaration")
PrimaryTypeDefinitionDeclaration = Class(name="PrimaryTypeDefinitionDeclaration")
optGrammar_NonArrayableDeclaration = Class(name="optGrammar_NonArrayableDeclaration")
PrimaryTypeDeclaration = Class(name="PrimaryTypeDeclaration")
optGrammar_LocationLiteral = Class(name="optGrammar_LocationLiteral")
optGrammar_SimpleTypeDeclaration = Class(name="optGrammar_SimpleTypeDeclaration")
optGrammar_ArrayableDeclaration = Class(name="optGrammar_ArrayableDeclaration")
optGrammar_SizedDeclaration = Class(name="optGrammar_SizedDeclaration")
optGrammar_ReturnsParameterList = Class(name="optGrammar_ReturnsParameterList")
optGrammar_StructDefinition = Class(name="optGrammar_StructDefinition")
optGrammar_PrimaryTypeDefinitionDeclaration = Class(name="optGrammar_PrimaryTypeDefinitionDeclaration")
optGrammar_EnumDefinition = Class(name="optGrammar_EnumDefinition")
optGrammar_EnumValue = Class(name="optGrammar_EnumValue")
optGrammar_Variable = Class(name="optGrammar_Variable")
optGrammar_Mapping = Class(name="optGrammar_Mapping")
optGrammar_Tuple = Class(name="optGrammar_Tuple")
Expression = Class(name="Expression")
optGrammar_TupleSeparator = Class(name="optGrammar_TupleSeparator")
optGrammar_SimpleStatement = Class(name="optGrammar_SimpleStatement")
Statement = Class(name="Statement")
optGrammar_SimpleStatement2 = Class(name="optGrammar_SimpleStatement2")
optGrammar_ExpressionStatement = Class(name="optGrammar_ExpressionStatement")
optGrammar_VariableDeclarationOptionalElement = Class(name="optGrammar_VariableDeclarationOptionalElement")
optGrammar_VisibilitySpecifier = Class(name="optGrammar_VisibilitySpecifier")
VariableDeclarationOptionalElement = Class(name="VariableDeclarationOptionalElement")
optGrammar_IndexedSpecifer = Class(name="optGrammar_IndexedSpecifer")
optGrammar_ConstantSpecifier = Class(name="optGrammar_ConstantSpecifier")
optGrammar_LocationSpecifier = Class(name="optGrammar_LocationSpecifier")
optGrammar_Type = Class(name="optGrammar_Type")
optGrammar_NamedType = Class(name="optGrammar_NamedType")
StandardType = Class(name="StandardType")
StandardTypeWithoutQualifiedIdentifier = Class(name="StandardTypeWithoutQualifiedIdentifier")
optGrammar_ArrayType = Class(name="optGrammar_ArrayType")
optGrammar_StandardType = Class(name="optGrammar_StandardType")
Type = Class(name="Type")
optGrammar_StandardTypeWithoutQualifiedIdentifier = Class(name="optGrammar_StandardTypeWithoutQualifiedIdentifier")
SimpleStatement = Class(name="SimpleStatement")
SimpleStatement2 = Class(name="SimpleStatement2")
optGrammar_Event = Class(name="optGrammar_Event")
optGrammar_ReturnParameterDeclaration = Class(name="optGrammar_ReturnParameterDeclaration")
optGrammar_QualifiedIdentifier = Class(name="optGrammar_QualifiedIdentifier")
optGrammar_Qualifier = Class(name="optGrammar_Qualifier")
optGrammar_Field = Class(name="optGrammar_Field")
Qualifier = Class(name="Qualifier")
optGrammar_Index = Class(name="optGrammar_Index")
optGrammar_Arguments = Class(name="optGrammar_Arguments")
optGrammar_Modifier = Class(name="optGrammar_Modifier")
optGrammar_WhileStatement = Class(name="optGrammar_WhileStatement")
optGrammar_ForStatement = Class(name="optGrammar_ForStatement")
optGrammar_LoopStructures = Class(name="optGrammar_LoopStructures")
optGrammar_Statement = Class(name="optGrammar_Statement")
optGrammar_DoWhileStatement = Class(name="optGrammar_DoWhileStatement")
optGrammar_EmitStatement = Class(name="optGrammar_EmitStatement")
optGrammar_FunctionCall = Class(name="optGrammar_FunctionCall")
optGrammar_DeleteStatement = Class(name="optGrammar_DeleteStatement")
optGrammar_IfStatement = Class(name="optGrammar_IfStatement")
LoopStructures = Class(name="LoopStructures")
optGrammar_NotExpression = Class(name="optGrammar_NotExpression")
optGrammar_PreIncExpression = Class(name="optGrammar_PreIncExpression")
optGrammar_PreDecExpression = Class(name="optGrammar_PreDecExpression")
optGrammar_ContinueStatement = Class(name="optGrammar_ContinueStatement")
optGrammar_BreakStatement = Class(name="optGrammar_BreakStatement")
optGrammar_ReturnStatement = Class(name="optGrammar_ReturnStatement")
optGrammar_ThrowStatement = Class(name="optGrammar_ThrowStatement")
optGrammar_PlaceHolderStatement = Class(name="optGrammar_PlaceHolderStatement")
PrimaryArithmetic = Class(name="PrimaryArithmetic")
optGrammar_SpecialExpression = Class(name="optGrammar_SpecialExpression")
optGrammar_BlockhashFunction = Class(name="optGrammar_BlockhashFunction")
Literal = Class(name="Literal")
optGrammar_IntParameter = Class(name="optGrammar_IntParameter")
optGrammar_GasleftFunction = Class(name="optGrammar_GasleftFunction")
optGrammar_BinaryNotExpression = Class(name="optGrammar_BinaryNotExpression")
optGrammar_SignExpression = Class(name="optGrammar_SignExpression")
optGrammar_NewExpression = Class(name="optGrammar_NewExpression")
optGrammar_Literal = Class(name="optGrammar_Literal")
optGrammar_ArithmeticOperations = Class(name="optGrammar_ArithmeticOperations")
optGrammar_PrimaryArithmetic = Class(name="optGrammar_PrimaryArithmetic")
optGrammar_SecondOperators = Class(name="optGrammar_SecondOperators")
optGrammar_HexLiteral = Class(name="optGrammar_HexLiteral")
optGrammar_DecimalLiteral = Class(name="optGrammar_DecimalLiteral")
optGrammar_UnitTypes = Class(name="optGrammar_UnitTypes")
optGrammar_StringLiteral = Class(name="optGrammar_StringLiteral")
optGrammar_TypeCast = Class(name="optGrammar_TypeCast")
optGrammar_MathematicalFunction = Class(name="optGrammar_MathematicalFunction")
optGrammar_HashFunction = Class(name="optGrammar_HashFunction")
optGrammar_EcrecoverFunction = Class(name="optGrammar_EcrecoverFunction")
optGrammar_BooleanLiteral = Class(name="optGrammar_BooleanLiteral")
optGrammar_NumericLiteral = Class(name="optGrammar_NumericLiteral")
optGrammar_IntLiteral = Class(name="optGrammar_IntLiteral")
optGrammar_TimeUnitsLiteral = Class(name="optGrammar_TimeUnitsLiteral")
optGrammar_UnitsLiteral = Class(name="optGrammar_UnitsLiteral")
optGrammar_SpecialLiteral = Class(name="optGrammar_SpecialLiteral")
NamedType = Class(name="NamedType")
optGrammar_StandardVariableDeclaration = Class(name="optGrammar_StandardVariableDeclaration")
optGrammar_Continue = Class(name="optGrammar_Continue")
ContinueStatement = Class(name="ContinueStatement")
optGrammar_Assignment = Class(name="optGrammar_Assignment")
optGrammar_VariableDeclarationExpression = Class(name="optGrammar_VariableDeclarationExpression")
optGrammar_VarVariableTypeDeclaration = Class(name="optGrammar_VarVariableTypeDeclaration")
optGrammar_VarVariableTupleVariableDeclaration = Class(name="optGrammar_VarVariableTupleVariableDeclaration")
optGrammar_Equality = Class(name="optGrammar_Equality")
optGrammar_Or = Class(name="optGrammar_Or")
optGrammar_And = Class(name="optGrammar_And")
optGrammar_BitAnd = Class(name="optGrammar_BitAnd")
optGrammar_Shift = Class(name="optGrammar_Shift")
optGrammar_Comparison = Class(name="optGrammar_Comparison")
optGrammar_BitOr = Class(name="optGrammar_BitOr")
optGrammar_BitXor = Class(name="optGrammar_BitXor")
optGrammar_Exponent = Class(name="optGrammar_Exponent")
optGrammar_PostIncDecExpression = Class(name="optGrammar_PostIncDecExpression")
optGrammar_AddSub = Class(name="optGrammar_AddSub")
optGrammar_MulDivMod = Class(name="optGrammar_MulDivMod")

# optGrammar_Model class attributes and methods

# optGrammar_PragmaDirective class attributes and methods

# optGrammar_DefinitionBody class attributes and methods

# optGrammar_ConstructorDefinition class attributes and methods
optGrammar_ConstructorDefinition_name: Property = Property(name="name", type=StringType)
optGrammar_ConstructorDefinition.attributes={optGrammar_ConstructorDefinition_name}

# DefinitionBody class attributes and methods

# optGrammar_ParameterList class attributes and methods

# optGrammar_StateMutability class attributes and methods
optGrammar_StateMutability_type: Property = Property(name="type", type=StringType)
optGrammar_StateMutability.attributes={optGrammar_StateMutability_type}

# optGrammar_Const class attributes and methods

# optGrammar_ModifierInvocation class attributes and methods

# optGrammar_ImportDirective class attributes and methods
optGrammar_ImportDirective_importURI: Property = Property(name="importURI", type=StringType)
optGrammar_ImportDirective_unitAlias: Property = Property(name="unitAlias", type=StringType)
optGrammar_ImportDirective.attributes={optGrammar_ImportDirective_unitAlias, optGrammar_ImportDirective_importURI}

# optGrammar_Contract class attributes and methods
optGrammar_Contract_name: Property = Property(name="name", type=StringType)
optGrammar_Contract.attributes={optGrammar_Contract_name}

# optGrammar_versionOperator class attributes and methods
optGrammar_versionOperator_value: Property = Property(name="value", type=StringType)
optGrammar_versionOperator.attributes={optGrammar_versionOperator_value}

# optGrammar_SymbolAlias class attributes and methods
optGrammar_SymbolAlias_symbol: Property = Property(name="symbol", type=StringType)
optGrammar_SymbolAlias_alias: Property = Property(name="alias", type=StringType)
optGrammar_SymbolAlias.attributes={optGrammar_SymbolAlias_alias, optGrammar_SymbolAlias_symbol}

# optGrammar_InheritanceSpecifier class attributes and methods

# optGrammar_FunctionDefinition class attributes and methods
optGrammar_FunctionDefinition_name: Property = Property(name="name", type=StringType)
optGrammar_FunctionDefinition.attributes={optGrammar_FunctionDefinition_name}

# optGrammar_VisibilityLiteral class attributes and methods
optGrammar_VisibilityLiteral_type: Property = Property(name="type", type=StringType)
optGrammar_VisibilityLiteral.attributes={optGrammar_VisibilityLiteral_type}

# optGrammar_Body class attributes and methods

# optGrammar_FunctionCallListArguments class attributes and methods

# FunctionCallArguments class attributes and methods

# optGrammar_Expression class attributes and methods

# optGrammar_FunctionCallArguments class attributes and methods

# optGrammar_FunctionCallArg class attributes and methods
optGrammar_FunctionCallArg_name: Property = Property(name="name", type=StringType)
optGrammar_FunctionCallArg.attributes={optGrammar_FunctionCallArg_name}

# optGrammar_PrimaryTypeDeclaration class attributes and methods
optGrammar_PrimaryTypeDeclaration_constant: Property = Property(name="constant", type=BooleanType)
optGrammar_PrimaryTypeDeclaration_name: Property = Property(name="name", type=StringType)
optGrammar_PrimaryTypeDeclaration.attributes={optGrammar_PrimaryTypeDeclaration_name, optGrammar_PrimaryTypeDeclaration_constant}

# PrimaryTypeDefinitionDeclaration class attributes and methods

# optGrammar_NonArrayableDeclaration class attributes and methods

# PrimaryTypeDeclaration class attributes and methods

# optGrammar_LocationLiteral class attributes and methods
optGrammar_LocationLiteral_type: Property = Property(name="type", type=StringType)
optGrammar_LocationLiteral.attributes={optGrammar_LocationLiteral_type}

# optGrammar_SimpleTypeDeclaration class attributes and methods

# optGrammar_ArrayableDeclaration class attributes and methods

# optGrammar_SizedDeclaration class attributes and methods

# optGrammar_ReturnsParameterList class attributes and methods

# optGrammar_StructDefinition class attributes and methods
optGrammar_StructDefinition_name: Property = Property(name="name", type=StringType)
optGrammar_StructDefinition.attributes={optGrammar_StructDefinition_name}

# optGrammar_PrimaryTypeDefinitionDeclaration class attributes and methods

# optGrammar_EnumDefinition class attributes and methods
optGrammar_EnumDefinition_name: Property = Property(name="name", type=StringType)
optGrammar_EnumDefinition.attributes={optGrammar_EnumDefinition_name}

# optGrammar_EnumValue class attributes and methods
optGrammar_EnumValue_name: Property = Property(name="name", type=StringType)
optGrammar_EnumValue.attributes={optGrammar_EnumValue_name}

# optGrammar_Variable class attributes and methods
optGrammar_Variable_name: Property = Property(name="name", type=StringType)
optGrammar_Variable.attributes={optGrammar_Variable_name}

# optGrammar_Mapping class attributes and methods

# optGrammar_Tuple class attributes and methods

# Expression class attributes and methods

# optGrammar_TupleSeparator class attributes and methods

# optGrammar_SimpleStatement class attributes and methods

# Statement class attributes and methods

# optGrammar_SimpleStatement2 class attributes and methods

# optGrammar_ExpressionStatement class attributes and methods
optGrammar_ExpressionStatement_semicolon: Property = Property(name="semicolon", type=BooleanType)
optGrammar_ExpressionStatement.attributes={optGrammar_ExpressionStatement_semicolon}

# optGrammar_VariableDeclarationOptionalElement class attributes and methods

# optGrammar_VisibilitySpecifier class attributes and methods

# VariableDeclarationOptionalElement class attributes and methods

# optGrammar_IndexedSpecifer class attributes and methods

# optGrammar_ConstantSpecifier class attributes and methods

# optGrammar_LocationSpecifier class attributes and methods

# optGrammar_Type class attributes and methods
optGrammar_Type_isVarType: Property = Property(name="isVarType", type=BooleanType)
optGrammar_Type.attributes={optGrammar_Type_isVarType}

# optGrammar_NamedType class attributes and methods
optGrammar_NamedType_type: Property = Property(name="type", type=StringType)
optGrammar_NamedType.attributes={optGrammar_NamedType_type}

# StandardType class attributes and methods

# StandardTypeWithoutQualifiedIdentifier class attributes and methods

# optGrammar_ArrayType class attributes and methods

# optGrammar_StandardType class attributes and methods

# Type class attributes and methods

# optGrammar_StandardTypeWithoutQualifiedIdentifier class attributes and methods

# SimpleStatement class attributes and methods

# SimpleStatement2 class attributes and methods

# optGrammar_Event class attributes and methods
optGrammar_Event_name: Property = Property(name="name", type=StringType)
optGrammar_Event_isAnonymous: Property = Property(name="isAnonymous", type=BooleanType)
optGrammar_Event.attributes={optGrammar_Event_isAnonymous, optGrammar_Event_name}

# optGrammar_ReturnParameterDeclaration class attributes and methods

# optGrammar_QualifiedIdentifier class attributes and methods
optGrammar_QualifiedIdentifier_identifier: Property = Property(name="identifier", type=StringType)
optGrammar_QualifiedIdentifier.attributes={optGrammar_QualifiedIdentifier_identifier}

# optGrammar_Qualifier class attributes and methods

# optGrammar_Field class attributes and methods
optGrammar_Field_field: Property = Property(name="field", type=StringType)
optGrammar_Field.attributes={optGrammar_Field_field}

# Qualifier class attributes and methods

# optGrammar_Index class attributes and methods

# optGrammar_Arguments class attributes and methods

# optGrammar_Modifier class attributes and methods
optGrammar_Modifier_name: Property = Property(name="name", type=StringType)
optGrammar_Modifier.attributes={optGrammar_Modifier_name}

# optGrammar_WhileStatement class attributes and methods

# optGrammar_ForStatement class attributes and methods

# optGrammar_LoopStructures class attributes and methods
optGrammar_LoopStructures_type: Property = Property(name="type", type=StringType)
optGrammar_LoopStructures.attributes={optGrammar_LoopStructures_type}

# optGrammar_Statement class attributes and methods

# optGrammar_DoWhileStatement class attributes and methods

# optGrammar_EmitStatement class attributes and methods

# optGrammar_FunctionCall class attributes and methods

# optGrammar_DeleteStatement class attributes and methods

# optGrammar_IfStatement class attributes and methods

# LoopStructures class attributes and methods

# optGrammar_NotExpression class attributes and methods

# optGrammar_PreIncExpression class attributes and methods

# optGrammar_PreDecExpression class attributes and methods

# optGrammar_ContinueStatement class attributes and methods

# optGrammar_BreakStatement class attributes and methods

# optGrammar_ReturnStatement class attributes and methods

# optGrammar_ThrowStatement class attributes and methods

# optGrammar_PlaceHolderStatement class attributes and methods

# PrimaryArithmetic class attributes and methods

# optGrammar_SpecialExpression class attributes and methods
optGrammar_SpecialExpression_type: Property = Property(name="type", type=StringType)
optGrammar_SpecialExpression.attributes={optGrammar_SpecialExpression_type}

# optGrammar_BlockhashFunction class attributes and methods

# Literal class attributes and methods

# optGrammar_IntParameter class attributes and methods

# optGrammar_GasleftFunction class attributes and methods
optGrammar_GasleftFunction_name: Property = Property(name="name", type=StringType)
optGrammar_GasleftFunction.attributes={optGrammar_GasleftFunction_name}

# optGrammar_BinaryNotExpression class attributes and methods

# optGrammar_SignExpression class attributes and methods
optGrammar_SignExpression_signOp: Property = Property(name="signOp", type=StringType)
optGrammar_SignExpression.attributes={optGrammar_SignExpression_signOp}

# optGrammar_NewExpression class attributes and methods

# optGrammar_Literal class attributes and methods

# optGrammar_ArithmeticOperations class attributes and methods

# optGrammar_PrimaryArithmetic class attributes and methods

# optGrammar_SecondOperators class attributes and methods
optGrammar_SecondOperators_operator: Property = Property(name="operator", type=StringType)
optGrammar_SecondOperators.attributes={optGrammar_SecondOperators_operator}

# optGrammar_HexLiteral class attributes and methods
optGrammar_HexLiteral_value: Property = Property(name="value", type=StringType)
optGrammar_HexLiteral.attributes={optGrammar_HexLiteral_value}

# optGrammar_DecimalLiteral class attributes and methods
optGrammar_DecimalLiteral_value: Property = Property(name="value", type=FloatType)
optGrammar_DecimalLiteral.attributes={optGrammar_DecimalLiteral_value}

# optGrammar_UnitTypes class attributes and methods

# optGrammar_StringLiteral class attributes and methods
optGrammar_StringLiteral_value: Property = Property(name="value", type=StringType)
optGrammar_StringLiteral.attributes={optGrammar_StringLiteral_value}

# optGrammar_TypeCast class attributes and methods

# optGrammar_MathematicalFunction class attributes and methods
optGrammar_MathematicalFunction_function: Property = Property(name="function", type=StringType)
optGrammar_MathematicalFunction.attributes={optGrammar_MathematicalFunction_function}

# optGrammar_HashFunction class attributes and methods
optGrammar_HashFunction_name: Property = Property(name="name", type=StringType)
optGrammar_HashFunction.attributes={optGrammar_HashFunction_name}

# optGrammar_EcrecoverFunction class attributes and methods
optGrammar_EcrecoverFunction_function: Property = Property(name="function", type=StringType)
optGrammar_EcrecoverFunction.attributes={optGrammar_EcrecoverFunction_function}

# optGrammar_BooleanLiteral class attributes and methods
optGrammar_BooleanLiteral_value: Property = Property(name="value", type=StringType)
optGrammar_BooleanLiteral.attributes={optGrammar_BooleanLiteral_value}

# optGrammar_NumericLiteral class attributes and methods

# optGrammar_IntLiteral class attributes and methods
optGrammar_IntLiteral_value: Property = Property(name="value", type=IntegerType)
optGrammar_IntLiteral.attributes={optGrammar_IntLiteral_value}

# optGrammar_TimeUnitsLiteral class attributes and methods
optGrammar_TimeUnitsLiteral_value: Property = Property(name="value", type=StringType)
optGrammar_TimeUnitsLiteral.attributes={optGrammar_TimeUnitsLiteral_value}

# optGrammar_UnitsLiteral class attributes and methods
optGrammar_UnitsLiteral_value: Property = Property(name="value", type=StringType)
optGrammar_UnitsLiteral.attributes={optGrammar_UnitsLiteral_value}

# optGrammar_SpecialLiteral class attributes and methods
optGrammar_SpecialLiteral_name: Property = Property(name="name", type=StringType)
optGrammar_SpecialLiteral.attributes={optGrammar_SpecialLiteral_name}

# NamedType class attributes and methods

# optGrammar_StandardVariableDeclaration class attributes and methods
optGrammar_StandardVariableDeclaration_semicolon: Property = Property(name="semicolon", type=BooleanType)
optGrammar_StandardVariableDeclaration.attributes={optGrammar_StandardVariableDeclaration_semicolon}

# optGrammar_Continue class attributes and methods

# ContinueStatement class attributes and methods

# optGrammar_Assignment class attributes and methods
optGrammar_Assignment_assignmentOp: Property = Property(name="assignmentOp", type=StringType)
optGrammar_Assignment.attributes={optGrammar_Assignment_assignmentOp}

# optGrammar_VariableDeclarationExpression class attributes and methods

# optGrammar_VarVariableTypeDeclaration class attributes and methods
optGrammar_VarVariableTypeDeclaration_semicolon: Property = Property(name="semicolon", type=BooleanType)
optGrammar_VarVariableTypeDeclaration.attributes={optGrammar_VarVariableTypeDeclaration_semicolon}

# optGrammar_VarVariableTupleVariableDeclaration class attributes and methods
optGrammar_VarVariableTupleVariableDeclaration_semicolon: Property = Property(name="semicolon", type=BooleanType)
optGrammar_VarVariableTupleVariableDeclaration.attributes={optGrammar_VarVariableTupleVariableDeclaration_semicolon}

# optGrammar_Equality class attributes and methods
optGrammar_Equality_equalityOp: Property = Property(name="equalityOp", type=StringType)
optGrammar_Equality.attributes={optGrammar_Equality_equalityOp}

# optGrammar_Or class attributes and methods

# optGrammar_And class attributes and methods

# optGrammar_BitAnd class attributes and methods

# optGrammar_Shift class attributes and methods
optGrammar_Shift_shiftOp: Property = Property(name="shiftOp", type=StringType)
optGrammar_Shift.attributes={optGrammar_Shift_shiftOp}

# optGrammar_Comparison class attributes and methods
optGrammar_Comparison_comparisonOp: Property = Property(name="comparisonOp", type=StringType)
optGrammar_Comparison.attributes={optGrammar_Comparison_comparisonOp}

# optGrammar_BitOr class attributes and methods

# optGrammar_BitXor class attributes and methods

# optGrammar_Exponent class attributes and methods

# optGrammar_PostIncDecExpression class attributes and methods
optGrammar_PostIncDecExpression_postOp: Property = Property(name="postOp", type=StringType)
optGrammar_PostIncDecExpression.attributes={optGrammar_PostIncDecExpression_postOp}

# optGrammar_AddSub class attributes and methods
optGrammar_AddSub_additionOp: Property = Property(name="additionOp", type=StringType)
optGrammar_AddSub.attributes={optGrammar_AddSub_additionOp}

# optGrammar_MulDivMod class attributes and methods
optGrammar_MulDivMod_multipliciativeOp: Property = Property(name="multipliciativeOp", type=StringType)
optGrammar_MulDivMod.attributes={optGrammar_MulDivMod_multipliciativeOp}

# Relationships
pragmaDirective0: BinaryAssociation = BinaryAssociation(
    name="pragmaDirective0",
    ends={
        Property(name="optGrammar_PragmaDirective", type=optGrammar_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_Model", type=optGrammar_PragmaDirective, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body11: BinaryAssociation = BinaryAssociation(
    name="body11",
    ends={
        Property(name="optGrammar_DefinitionBody", type=optGrammar_Contract, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_Contract12", type=optGrammar_DefinitionBody, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters13: BinaryAssociation = BinaryAssociation(
    name="parameters13",
    ends={
        Property(name="optGrammar_ParameterList", type=optGrammar_ConstructorDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_ConstructorDefinition", type=optGrammar_ParameterList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
state14: BinaryAssociation = BinaryAssociation(
    name="state14",
    ends={
        Property(name="optGrammar_StateMutability", type=optGrammar_ConstructorDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_ConstructorDefinition15", type=optGrammar_StateMutability, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
const16: BinaryAssociation = BinaryAssociation(
    name="const16",
    ends={
        Property(name="optGrammar_Const", type=optGrammar_ConstructorDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_ConstructorDefinition17", type=optGrammar_Const, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
modifier18: BinaryAssociation = BinaryAssociation(
    name="modifier18",
    ends={
        Property(name="optGrammar_ModifierInvocation", type=optGrammar_ConstructorDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_ConstructorDefinition19", type=optGrammar_ModifierInvocation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
importDirective1: BinaryAssociation = BinaryAssociation(
    name="importDirective1",
    ends={
        Property(name="optGrammar_ImportDirective", type=optGrammar_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_Model2", type=optGrammar_ImportDirective, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
contract3: BinaryAssociation = BinaryAssociation(
    name="contract3",
    ends={
        Property(name="optGrammar_Contract", type=optGrammar_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_Model4", type=optGrammar_Contract, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
version5: BinaryAssociation = BinaryAssociation(
    name="version5",
    ends={
        Property(name="optGrammar_versionOperator", type=optGrammar_PragmaDirective, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_PragmaDirective6", type=optGrammar_versionOperator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
symbolAliases7: BinaryAssociation = BinaryAssociation(
    name="symbolAliases7",
    ends={
        Property(name="optGrammar_SymbolAlias", type=optGrammar_ImportDirective, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_ImportDirective8", type=optGrammar_SymbolAlias, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inheritanceSpecifiers9: BinaryAssociation = BinaryAssociation(
    name="inheritanceSpecifiers9",
    ends={
        Property(name="optGrammar_InheritanceSpecifier", type=optGrammar_Contract, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_Contract10", type=optGrammar_InheritanceSpecifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
args31: BinaryAssociation = BinaryAssociation(
    name="args31",
    ends={
        Property(name="optGrammar_FunctionCallArguments", type=optGrammar_FunctionCallArg, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="optGrammar_FunctionCallArg", type=optGrammar_FunctionCallArguments, multiplicity=Multiplicity(1, 1))
    }
)
expr32: BinaryAssociation = BinaryAssociation(
    name="expr32",
    ends={
        Property(name="optGrammar_Expression34", type=optGrammar_FunctionCallArg, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_FunctionCallArg33", type=optGrammar_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters35: BinaryAssociation = BinaryAssociation(
    name="parameters35",
    ends={
        Property(name="optGrammar_ParameterList36", type=optGrammar_FunctionDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_FunctionDefinition", type=optGrammar_ParameterList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
state37: BinaryAssociation = BinaryAssociation(
    name="state37",
    ends={
        Property(name="optGrammar_StateMutability39", type=optGrammar_FunctionDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_FunctionDefinition38", type=optGrammar_StateMutability, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
const40: BinaryAssociation = BinaryAssociation(
    name="const40",
    ends={
        Property(name="optGrammar_Const42", type=optGrammar_FunctionDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_FunctionDefinition41", type=optGrammar_Const, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
modifier43: BinaryAssociation = BinaryAssociation(
    name="modifier43",
    ends={
        Property(name="optGrammar_ModifierInvocation45", type=optGrammar_FunctionDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_FunctionDefinition44", type=optGrammar_ModifierInvocation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
visibility20: BinaryAssociation = BinaryAssociation(
    name="visibility20",
    ends={
        Property(name="optGrammar_VisibilityLiteral", type=optGrammar_ConstructorDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_ConstructorDefinition21", type=optGrammar_VisibilityLiteral, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
block22: BinaryAssociation = BinaryAssociation(
    name="block22",
    ends={
        Property(name="optGrammar_Body", type=optGrammar_ConstructorDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_ConstructorDefinition23", type=optGrammar_Body, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
superType24: BinaryAssociation = BinaryAssociation(
    name="superType24",
    ends={
        Property(name="optGrammar_Contract26", type=optGrammar_InheritanceSpecifier, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_InheritanceSpecifier25", type=optGrammar_Contract, multiplicity=Multiplicity(0, 1))
    }
)
args27: BinaryAssociation = BinaryAssociation(
    name="args27",
    ends={
        Property(name="optGrammar_FunctionCallListArguments", type=optGrammar_InheritanceSpecifier, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_InheritanceSpecifier28", type=optGrammar_FunctionCallListArguments, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arguments29: BinaryAssociation = BinaryAssociation(
    name="arguments29",
    ends={
        Property(name="optGrammar_Expression", type=optGrammar_FunctionCallListArguments, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_FunctionCallListArguments30", type=optGrammar_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ref56: BinaryAssociation = BinaryAssociation(
    name="ref56",
    ends={
        Property(name="optGrammar_PrimaryTypeDeclaration", type=optGrammar_PrimaryTypeDefinitionDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_PrimaryTypeDefinitionDeclaration57", type=optGrammar_PrimaryTypeDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
value58: BinaryAssociation = BinaryAssociation(
    name="value58",
    ends={
        Property(name="optGrammar_Expression60", type=optGrammar_PrimaryTypeDefinitionDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_PrimaryTypeDefinitionDeclaration59", type=optGrammar_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
visibility61: BinaryAssociation = BinaryAssociation(
    name="visibility61",
    ends={
        Property(name="optGrammar_VisibilityLiteral63", type=optGrammar_PrimaryTypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_PrimaryTypeDeclaration62", type=optGrammar_VisibilityLiteral, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
location64: BinaryAssociation = BinaryAssociation(
    name="location64",
    ends={
        Property(name="optGrammar_LocationLiteral", type=optGrammar_NonArrayableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_NonArrayableDeclaration", type=optGrammar_LocationLiteral, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type65: BinaryAssociation = BinaryAssociation(
    name="type65",
    ends={
        Property(name="optGrammar_SimpleTypeDeclaration", type=optGrammar_NonArrayableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_NonArrayableDeclaration66", type=optGrammar_SimpleTypeDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type67: BinaryAssociation = BinaryAssociation(
    name="type67",
    ends={
        Property(name="optGrammar_SizedDeclaration", type=optGrammar_ArrayableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_ArrayableDeclaration", type=optGrammar_SizedDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
visibility46: BinaryAssociation = BinaryAssociation(
    name="visibility46",
    ends={
        Property(name="optGrammar_VisibilityLiteral48", type=optGrammar_FunctionDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_FunctionDefinition47", type=optGrammar_VisibilityLiteral, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returnParameters49: BinaryAssociation = BinaryAssociation(
    name="returnParameters49",
    ends={
        Property(name="optGrammar_ReturnsParameterList", type=optGrammar_FunctionDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_FunctionDefinition50", type=optGrammar_ReturnsParameterList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block51: BinaryAssociation = BinaryAssociation(
    name="block51",
    ends={
        Property(name="optGrammar_Body53", type=optGrammar_FunctionDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_FunctionDefinition52", type=optGrammar_Body, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
members54: BinaryAssociation = BinaryAssociation(
    name="members54",
    ends={
        Property(name="optGrammar_PrimaryTypeDefinitionDeclaration", type=optGrammar_StructDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_StructDefinition", type=optGrammar_PrimaryTypeDefinitionDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
members55: BinaryAssociation = BinaryAssociation(
    name="members55",
    ends={
        Property(name="optGrammar_EnumValue", type=optGrammar_EnumDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_EnumDefinition", type=optGrammar_EnumValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value73: BinaryAssociation = BinaryAssociation(
    name="value73",
    ends={
        Property(name="optGrammar_Expression75", type=optGrammar_ArrayType, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_ArrayType74", type=optGrammar_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
keyType76: BinaryAssociation = BinaryAssociation(
    name="keyType76",
    ends={
        Property(name="optGrammar_SizedDeclaration77", type=optGrammar_Mapping, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_Mapping", type=optGrammar_SizedDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
valueType78: BinaryAssociation = BinaryAssociation(
    name="valueType78",
    ends={
        Property(name="optGrammar_Type", type=optGrammar_Mapping, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_Mapping79", type=optGrammar_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
members80: BinaryAssociation = BinaryAssociation(
    name="members80",
    ends={
        Property(name="optGrammar_Expression81", type=optGrammar_Tuple, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_Tuple", type=optGrammar_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression82: BinaryAssociation = BinaryAssociation(
    name="expression82",
    ends={
        Property(name="optGrammar_Expression83", type=optGrammar_ExpressionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_ExpressionStatement", type=optGrammar_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
visibility68: BinaryAssociation = BinaryAssociation(
    name="visibility68",
    ends={
        Property(name="optGrammar_VisibilityLiteral69", type=optGrammar_VisibilitySpecifier, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_VisibilitySpecifier", type=optGrammar_VisibilityLiteral, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
location70: BinaryAssociation = BinaryAssociation(
    name="location70",
    ends={
        Property(name="optGrammar_LocationLiteral71", type=optGrammar_LocationSpecifier, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_LocationSpecifier", type=optGrammar_LocationLiteral, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dimension72: BinaryAssociation = BinaryAssociation(
    name="dimension72",
    ends={
        Property(name="optGrammar_ArrayType", type=optGrammar_NamedType, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_NamedType", type=optGrammar_ArrayType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters94: BinaryAssociation = BinaryAssociation(
    name="parameters94",
    ends={
        Property(name="optGrammar_ParameterList95", type=optGrammar_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_Event", type=optGrammar_ParameterList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name96: BinaryAssociation = BinaryAssociation(
    name="name96",
    ends={
        Property(name="optGrammar_Modifier98", type=optGrammar_ModifierInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_ModifierInvocation97", type=optGrammar_Modifier, multiplicity=Multiplicity(0, 1))
    }
)
args99: BinaryAssociation = BinaryAssociation(
    name="args99",
    ends={
        Property(name="optGrammar_FunctionCallListArguments101", type=optGrammar_ModifierInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_ModifierInvocation100", type=optGrammar_FunctionCallListArguments, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters102: BinaryAssociation = BinaryAssociation(
    name="parameters102",
    ends={
        Property(name="optGrammar_PrimaryTypeDefinitionDeclaration104", type=optGrammar_ParameterList, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_ParameterList103", type=optGrammar_PrimaryTypeDefinitionDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters105: BinaryAssociation = BinaryAssociation(
    name="parameters105",
    ends={
        Property(name="optGrammar_ReturnParameterDeclaration", type=optGrammar_ReturnsParameterList, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_ReturnsParameterList106", type=optGrammar_ReturnParameterDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeRef107: BinaryAssociation = BinaryAssociation(
    name="typeRef107",
    ends={
        Property(name="optGrammar_Type109", type=optGrammar_ReturnParameterDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_ReturnParameterDeclaration108", type=optGrammar_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
qualifiers84: BinaryAssociation = BinaryAssociation(
    name="qualifiers84",
    ends={
        Property(name="optGrammar_Qualifier", type=optGrammar_QualifiedIdentifier, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_QualifiedIdentifier", type=optGrammar_Qualifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value85: BinaryAssociation = BinaryAssociation(
    name="value85",
    ends={
        Property(name="optGrammar_Expression86", type=optGrammar_Index, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_Index", type=optGrammar_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arguments87: BinaryAssociation = BinaryAssociation(
    name="arguments87",
    ends={
        Property(name="optGrammar_FunctionCallArguments88", type=optGrammar_Arguments, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_Arguments", type=optGrammar_FunctionCallArguments, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters89: BinaryAssociation = BinaryAssociation(
    name="parameters89",
    ends={
        Property(name="optGrammar_ParameterList90", type=optGrammar_Modifier, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_Modifier", type=optGrammar_ParameterList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block91: BinaryAssociation = BinaryAssociation(
    name="block91",
    ends={
        Property(name="optGrammar_Body93", type=optGrammar_Modifier, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_Modifier92", type=optGrammar_Body, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
falseBody124: BinaryAssociation = BinaryAssociation(
    name="falseBody124",
    ends={
        Property(name="optGrammar_Statement126", type=optGrammar_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_IfStatement125", type=optGrammar_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition127: BinaryAssociation = BinaryAssociation(
    name="condition127",
    ends={
        Property(name="optGrammar_Expression128", type=optGrammar_WhileStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_WhileStatement", type=optGrammar_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body129: BinaryAssociation = BinaryAssociation(
    name="body129",
    ends={
        Property(name="optGrammar_Statement131", type=optGrammar_WhileStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_WhileStatement130", type=optGrammar_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initExpression132: BinaryAssociation = BinaryAssociation(
    name="initExpression132",
    ends={
        Property(name="optGrammar_SimpleStatement2", type=optGrammar_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_ForStatement", type=optGrammar_SimpleStatement2, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
conditionExpression133: BinaryAssociation = BinaryAssociation(
    name="conditionExpression133",
    ends={
        Property(name="optGrammar_Expression135", type=optGrammar_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_ForStatement134", type=optGrammar_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
loopExpression136: BinaryAssociation = BinaryAssociation(
    name="loopExpression136",
    ends={
        Property(name="optGrammar_ExpressionStatement138", type=optGrammar_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_ForStatement137", type=optGrammar_ExpressionStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body139: BinaryAssociation = BinaryAssociation(
    name="body139",
    ends={
        Property(name="optGrammar_Statement141", type=optGrammar_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_ForStatement140", type=optGrammar_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable110: BinaryAssociation = BinaryAssociation(
    name="variable110",
    ends={
        Property(name="optGrammar_Variable", type=optGrammar_ReturnParameterDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_ReturnParameterDeclaration111", type=optGrammar_Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body112: BinaryAssociation = BinaryAssociation(
    name="body112",
    ends={
        Property(name="optGrammar_Statement", type=optGrammar_DoWhileStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_DoWhileStatement", type=optGrammar_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition113: BinaryAssociation = BinaryAssociation(
    name="condition113",
    ends={
        Property(name="optGrammar_Expression115", type=optGrammar_DoWhileStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_DoWhileStatement114", type=optGrammar_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
call116: BinaryAssociation = BinaryAssociation(
    name="call116",
    ends={
        Property(name="optGrammar_FunctionCall", type=optGrammar_EmitStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_EmitStatement", type=optGrammar_FunctionCall, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable117: BinaryAssociation = BinaryAssociation(
    name="variable117",
    ends={
        Property(name="optGrammar_QualifiedIdentifier118", type=optGrammar_DeleteStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_DeleteStatement", type=optGrammar_QualifiedIdentifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition119: BinaryAssociation = BinaryAssociation(
    name="condition119",
    ends={
        Property(name="optGrammar_Expression120", type=optGrammar_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_IfStatement", type=optGrammar_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
trueBody121: BinaryAssociation = BinaryAssociation(
    name="trueBody121",
    ends={
        Property(name="optGrammar_Statement123", type=optGrammar_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_IfStatement122", type=optGrammar_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fieldOrMethod147: BinaryAssociation = BinaryAssociation(
    name="fieldOrMethod147",
    ends={
        Property(name="optGrammar_Field", type=optGrammar_SpecialExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_SpecialExpression", type=optGrammar_Field, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
qualifiers148: BinaryAssociation = BinaryAssociation(
    name="qualifiers148",
    ends={
        Property(name="optGrammar_Qualifier150", type=optGrammar_SpecialExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_SpecialExpression149", type=optGrammar_Qualifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression151: BinaryAssociation = BinaryAssociation(
    name="expression151",
    ends={
        Property(name="optGrammar_Expression152", type=optGrammar_NotExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_NotExpression", type=optGrammar_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression153: BinaryAssociation = BinaryAssociation(
    name="expression153",
    ends={
        Property(name="optGrammar_Expression154", type=optGrammar_PreIncExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_PreIncExpression", type=optGrammar_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression155: BinaryAssociation = BinaryAssociation(
    name="expression155",
    ends={
        Property(name="optGrammar_Expression156", type=optGrammar_PreDecExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_PreDecExpression", type=optGrammar_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statements142: BinaryAssociation = BinaryAssociation(
    name="statements142",
    ends={
        Property(name="optGrammar_Statement144", type=optGrammar_Body, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_Body143", type=optGrammar_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression145: BinaryAssociation = BinaryAssociation(
    name="expression145",
    ends={
        Property(name="optGrammar_Expression146", type=optGrammar_ReturnStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_ReturnStatement", type=optGrammar_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value169: BinaryAssociation = BinaryAssociation(
    name="value169",
    ends={
        Property(name="optGrammar_PrimaryArithmetic171", type=optGrammar_SecondOperators, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_SecondOperators170", type=optGrammar_PrimaryArithmetic, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name172: BinaryAssociation = BinaryAssociation(
    name="name172",
    ends={
        Property(name="optGrammar_FunctionDefinition174", type=optGrammar_FunctionCall, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_FunctionCall173", type=optGrammar_FunctionDefinition, multiplicity=Multiplicity(0, 1))
    }
)
parameters175: BinaryAssociation = BinaryAssociation(
    name="parameters175",
    ends={
        Property(name="optGrammar_Expression177", type=optGrammar_FunctionCall, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_FunctionCall176", type=optGrammar_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameter178: BinaryAssociation = BinaryAssociation(
    name="parameter178",
    ends={
        Property(name="optGrammar_IntParameter", type=optGrammar_BlockhashFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_BlockhashFunction", type=optGrammar_IntParameter, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
param179: BinaryAssociation = BinaryAssociation(
    name="param179",
    ends={
        Property(name="optGrammar_ArithmeticOperations181", type=optGrammar_IntParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_IntParameter180", type=optGrammar_ArithmeticOperations, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression157: BinaryAssociation = BinaryAssociation(
    name="expression157",
    ends={
        Property(name="optGrammar_Expression158", type=optGrammar_BinaryNotExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_BinaryNotExpression", type=optGrammar_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression159: BinaryAssociation = BinaryAssociation(
    name="expression159",
    ends={
        Property(name="optGrammar_Expression160", type=optGrammar_SignExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_SignExpression", type=optGrammar_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
contract161: BinaryAssociation = BinaryAssociation(
    name="contract161",
    ends={
        Property(name="optGrammar_Contract162", type=optGrammar_NewExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_NewExpression", type=optGrammar_Contract, multiplicity=Multiplicity(0, 1))
    }
)
args163: BinaryAssociation = BinaryAssociation(
    name="args163",
    ends={
        Property(name="optGrammar_FunctionCallListArguments165", type=optGrammar_NewExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_NewExpression164", type=optGrammar_FunctionCallListArguments, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
first166: BinaryAssociation = BinaryAssociation(
    name="first166",
    ends={
        Property(name="optGrammar_PrimaryArithmetic", type=optGrammar_ArithmeticOperations, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_ArithmeticOperations", type=optGrammar_PrimaryArithmetic, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
seconds167: BinaryAssociation = BinaryAssociation(
    name="seconds167",
    ends={
        Property(name="optGrammar_SecondOperators", type=optGrammar_ArithmeticOperations, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_ArithmeticOperations168", type=optGrammar_SecondOperators, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
hexValue192: BinaryAssociation = BinaryAssociation(
    name="hexValue192",
    ends={
        Property(name="optGrammar_HexLiteral", type=optGrammar_NumericLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_NumericLiteral193", type=optGrammar_HexLiteral, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
decimalValue194: BinaryAssociation = BinaryAssociation(
    name="decimalValue194",
    ends={
        Property(name="optGrammar_DecimalLiteral", type=optGrammar_NumericLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_NumericLiteral195", type=optGrammar_DecimalLiteral, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
etherUnit196: BinaryAssociation = BinaryAssociation(
    name="etherUnit196",
    ends={
        Property(name="optGrammar_UnitTypes", type=optGrammar_NumericLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_NumericLiteral197", type=optGrammar_UnitTypes, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value198: BinaryAssociation = BinaryAssociation(
    name="value198",
    ends={
        Property(name="optGrammar_SizedDeclaration199", type=optGrammar_TypeCast, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_TypeCast", type=optGrammar_SizedDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression200: BinaryAssociation = BinaryAssociation(
    name="expression200",
    ends={
        Property(name="optGrammar_Expression202", type=optGrammar_TypeCast, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_TypeCast201", type=optGrammar_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fun182: BinaryAssociation = BinaryAssociation(
    name="fun182",
    ends={
        Property(name="optGrammar_FunctionCall184", type=optGrammar_IntParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_IntParameter183", type=optGrammar_FunctionCall, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters185: BinaryAssociation = BinaryAssociation(
    name="parameters185",
    ends={
        Property(name="optGrammar_IntParameter186", type=optGrammar_MathematicalFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_MathematicalFunction", type=optGrammar_IntParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters187: BinaryAssociation = BinaryAssociation(
    name="parameters187",
    ends={
        Property(name="optGrammar_IntParameter188", type=optGrammar_HashFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_HashFunction", type=optGrammar_IntParameter, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters189: BinaryAssociation = BinaryAssociation(
    name="parameters189",
    ends={
        Property(name="optGrammar_IntParameter190", type=optGrammar_EcrecoverFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_EcrecoverFunction", type=optGrammar_IntParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
intValue191: BinaryAssociation = BinaryAssociation(
    name="intValue191",
    ends={
        Property(name="optGrammar_IntLiteral", type=optGrammar_NumericLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_NumericLiteral", type=optGrammar_IntLiteral, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
time203: BinaryAssociation = BinaryAssociation(
    name="time203",
    ends={
        Property(name="optGrammar_TimeUnitsLiteral", type=optGrammar_UnitTypes, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_UnitTypes204", type=optGrammar_TimeUnitsLiteral, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
units205: BinaryAssociation = BinaryAssociation(
    name="units205",
    ends={
        Property(name="optGrammar_UnitsLiteral", type=optGrammar_UnitTypes, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_UnitTypes206", type=optGrammar_UnitsLiteral, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression223: BinaryAssociation = BinaryAssociation(
    name="expression223",
    ends={
        Property(name="optGrammar_Expression225", type=optGrammar_VarVariableTupleVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_VarVariableTupleVariableDeclaration224", type=optGrammar_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left226: BinaryAssociation = BinaryAssociation(
    name="left226",
    ends={
        Property(name="optGrammar_Expression227", type=optGrammar_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_Assignment", type=optGrammar_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression228: BinaryAssociation = BinaryAssociation(
    name="expression228",
    ends={
        Property(name="optGrammar_Expression230", type=optGrammar_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_Assignment229", type=optGrammar_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type231: BinaryAssociation = BinaryAssociation(
    name="type231",
    ends={
        Property(name="optGrammar_Expression232", type=optGrammar_VariableDeclarationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_VariableDeclarationExpression", type=optGrammar_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type207: BinaryAssociation = BinaryAssociation(
    name="type207",
    ends={
        Property(name="optGrammar_StandardTypeWithoutQualifiedIdentifier", type=optGrammar_StandardVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_StandardVariableDeclaration", type=optGrammar_StandardTypeWithoutQualifiedIdentifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
optionalElements208: BinaryAssociation = BinaryAssociation(
    name="optionalElements208",
    ends={
        Property(name="optGrammar_VariableDeclarationOptionalElement", type=optGrammar_StandardVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_StandardVariableDeclaration209", type=optGrammar_VariableDeclarationOptionalElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variable210: BinaryAssociation = BinaryAssociation(
    name="variable210",
    ends={
        Property(name="optGrammar_Variable212", type=optGrammar_StandardVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_StandardVariableDeclaration211", type=optGrammar_Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression213: BinaryAssociation = BinaryAssociation(
    name="expression213",
    ends={
        Property(name="optGrammar_Expression215", type=optGrammar_StandardVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_StandardVariableDeclaration214", type=optGrammar_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable216: BinaryAssociation = BinaryAssociation(
    name="variable216",
    ends={
        Property(name="optGrammar_Variable217", type=optGrammar_VarVariableTypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_VarVariableTypeDeclaration", type=optGrammar_Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression218: BinaryAssociation = BinaryAssociation(
    name="expression218",
    ends={
        Property(name="optGrammar_Expression220", type=optGrammar_VarVariableTypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_VarVariableTypeDeclaration219", type=optGrammar_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tuple221: BinaryAssociation = BinaryAssociation(
    name="tuple221",
    ends={
        Property(name="optGrammar_Tuple222", type=optGrammar_VarVariableTupleVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_VarVariableTupleVariableDeclaration", type=optGrammar_Tuple, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right246: BinaryAssociation = BinaryAssociation(
    name="right246",
    ends={
        Property(name="optGrammar_Expression248", type=optGrammar_And, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_And247", type=optGrammar_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left249: BinaryAssociation = BinaryAssociation(
    name="left249",
    ends={
        Property(name="optGrammar_Expression250", type=optGrammar_Equality, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_Equality", type=optGrammar_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right251: BinaryAssociation = BinaryAssociation(
    name="right251",
    ends={
        Property(name="optGrammar_Expression253", type=optGrammar_Equality, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_Equality252", type=optGrammar_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable233: BinaryAssociation = BinaryAssociation(
    name="variable233",
    ends={
        Property(name="optGrammar_Variable235", type=optGrammar_VariableDeclarationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_VariableDeclarationExpression234", type=optGrammar_Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression236: BinaryAssociation = BinaryAssociation(
    name="expression236",
    ends={
        Property(name="optGrammar_Expression238", type=optGrammar_VariableDeclarationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_VariableDeclarationExpression237", type=optGrammar_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left239: BinaryAssociation = BinaryAssociation(
    name="left239",
    ends={
        Property(name="optGrammar_Expression240", type=optGrammar_Or, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_Or", type=optGrammar_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right241: BinaryAssociation = BinaryAssociation(
    name="right241",
    ends={
        Property(name="optGrammar_Expression243", type=optGrammar_Or, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_Or242", type=optGrammar_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left244: BinaryAssociation = BinaryAssociation(
    name="left244",
    ends={
        Property(name="optGrammar_Expression245", type=optGrammar_And, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_And", type=optGrammar_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right266: BinaryAssociation = BinaryAssociation(
    name="right266",
    ends={
        Property(name="optGrammar_Expression268", type=optGrammar_BitXor, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_BitXor267", type=optGrammar_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left269: BinaryAssociation = BinaryAssociation(
    name="left269",
    ends={
        Property(name="optGrammar_Expression270", type=optGrammar_BitAnd, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_BitAnd", type=optGrammar_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right271: BinaryAssociation = BinaryAssociation(
    name="right271",
    ends={
        Property(name="optGrammar_Expression273", type=optGrammar_BitAnd, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_BitAnd272", type=optGrammar_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left274: BinaryAssociation = BinaryAssociation(
    name="left274",
    ends={
        Property(name="optGrammar_Expression275", type=optGrammar_Shift, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_Shift", type=optGrammar_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right276: BinaryAssociation = BinaryAssociation(
    name="right276",
    ends={
        Property(name="optGrammar_Expression278", type=optGrammar_Shift, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_Shift277", type=optGrammar_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left254: BinaryAssociation = BinaryAssociation(
    name="left254",
    ends={
        Property(name="optGrammar_Expression255", type=optGrammar_Comparison, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_Comparison", type=optGrammar_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right256: BinaryAssociation = BinaryAssociation(
    name="right256",
    ends={
        Property(name="optGrammar_Expression258", type=optGrammar_Comparison, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_Comparison257", type=optGrammar_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left259: BinaryAssociation = BinaryAssociation(
    name="left259",
    ends={
        Property(name="optGrammar_Expression260", type=optGrammar_BitOr, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_BitOr", type=optGrammar_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right261: BinaryAssociation = BinaryAssociation(
    name="right261",
    ends={
        Property(name="optGrammar_Expression263", type=optGrammar_BitOr, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_BitOr262", type=optGrammar_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left264: BinaryAssociation = BinaryAssociation(
    name="left264",
    ends={
        Property(name="optGrammar_Expression265", type=optGrammar_BitXor, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_BitXor", type=optGrammar_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right286: BinaryAssociation = BinaryAssociation(
    name="right286",
    ends={
        Property(name="optGrammar_MulDivMod287", type=optGrammar_Expression, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="optGrammar_Expression288", type=optGrammar_MulDivMod, multiplicity=Multiplicity(1, 1))
    }
)
left289: BinaryAssociation = BinaryAssociation(
    name="left289",
    ends={
        Property(name="optGrammar_Expression290", type=optGrammar_Exponent, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_Exponent", type=optGrammar_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right291: BinaryAssociation = BinaryAssociation(
    name="right291",
    ends={
        Property(name="optGrammar_Expression293", type=optGrammar_Exponent, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_Exponent292", type=optGrammar_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression294: BinaryAssociation = BinaryAssociation(
    name="expression294",
    ends={
        Property(name="optGrammar_Expression295", type=optGrammar_PostIncDecExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_PostIncDecExpression", type=optGrammar_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left279: BinaryAssociation = BinaryAssociation(
    name="left279",
    ends={
        Property(name="optGrammar_Expression280", type=optGrammar_AddSub, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_AddSub", type=optGrammar_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right281: BinaryAssociation = BinaryAssociation(
    name="right281",
    ends={
        Property(name="optGrammar_Expression283", type=optGrammar_AddSub, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_AddSub282", type=optGrammar_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left284: BinaryAssociation = BinaryAssociation(
    name="left284",
    ends={
        Property(name="optGrammar_Expression285", type=optGrammar_MulDivMod, multiplicity=Multiplicity(1, 1)),
        Property(name="optGrammar_MulDivMod", type=optGrammar_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_optGrammar_ConstructorDefinition_DefinitionBody = Generalization(general=DefinitionBody, specific=optGrammar_ConstructorDefinition)
gen_optGrammar_FunctionDefinition_DefinitionBody = Generalization(general=DefinitionBody, specific=optGrammar_FunctionDefinition)
gen_optGrammar_FunctionCallListArguments_FunctionCallArguments = Generalization(general=FunctionCallArguments, specific=optGrammar_FunctionCallListArguments)
gen_optGrammar_PrimaryTypeDefinitionDeclaration_DefinitionBody = Generalization(general=DefinitionBody, specific=optGrammar_PrimaryTypeDefinitionDeclaration)
gen_optGrammar_PrimaryTypeDeclaration_PrimaryTypeDefinitionDeclaration = Generalization(general=PrimaryTypeDefinitionDeclaration, specific=optGrammar_PrimaryTypeDeclaration)
gen_optGrammar_NonArrayableDeclaration_PrimaryTypeDeclaration = Generalization(general=PrimaryTypeDeclaration, specific=optGrammar_NonArrayableDeclaration)
gen_optGrammar_ArrayableDeclaration_PrimaryTypeDeclaration = Generalization(general=PrimaryTypeDeclaration, specific=optGrammar_ArrayableDeclaration)
gen_optGrammar_StructDefinition_DefinitionBody = Generalization(general=DefinitionBody, specific=optGrammar_StructDefinition)
gen_optGrammar_EnumDefinition_DefinitionBody = Generalization(general=DefinitionBody, specific=optGrammar_EnumDefinition)
gen_optGrammar_Mapping_StandardType = Generalization(general=StandardType, specific=optGrammar_Mapping)
gen_optGrammar_Mapping_StandardTypeWithoutQualifiedIdentifier = Generalization(general=StandardTypeWithoutQualifiedIdentifier, specific=optGrammar_Mapping)
gen_optGrammar_Tuple_Expression = Generalization(general=Expression, specific=optGrammar_Tuple)
gen_optGrammar_TupleSeparator_Expression = Generalization(general=Expression, specific=optGrammar_TupleSeparator)
gen_optGrammar_SimpleStatement_Statement = Generalization(general=Statement, specific=optGrammar_SimpleStatement)
gen_optGrammar_ExpressionStatement_SimpleStatement = Generalization(general=SimpleStatement, specific=optGrammar_ExpressionStatement)
gen_optGrammar_ExpressionStatement_SimpleStatement2 = Generalization(general=SimpleStatement2, specific=optGrammar_ExpressionStatement)
gen_optGrammar_VisibilitySpecifier_VariableDeclarationOptionalElement = Generalization(general=VariableDeclarationOptionalElement, specific=optGrammar_VisibilitySpecifier)
gen_optGrammar_IndexedSpecifer_VariableDeclarationOptionalElement = Generalization(general=VariableDeclarationOptionalElement, specific=optGrammar_IndexedSpecifer)
gen_optGrammar_ConstantSpecifier_VariableDeclarationOptionalElement = Generalization(general=VariableDeclarationOptionalElement, specific=optGrammar_ConstantSpecifier)
gen_optGrammar_LocationSpecifier_VariableDeclarationOptionalElement = Generalization(general=VariableDeclarationOptionalElement, specific=optGrammar_LocationSpecifier)
gen_optGrammar_NamedType_StandardType = Generalization(general=StandardType, specific=optGrammar_NamedType)
gen_optGrammar_NamedType_StandardTypeWithoutQualifiedIdentifier = Generalization(general=StandardTypeWithoutQualifiedIdentifier, specific=optGrammar_NamedType)
gen_optGrammar_StandardType_Type = Generalization(general=Type, specific=optGrammar_StandardType)
gen_optGrammar_StandardTypeWithoutQualifiedIdentifier_SimpleStatement = Generalization(general=SimpleStatement, specific=optGrammar_StandardTypeWithoutQualifiedIdentifier)
gen_optGrammar_StandardTypeWithoutQualifiedIdentifier_SimpleStatement2 = Generalization(general=SimpleStatement2, specific=optGrammar_StandardTypeWithoutQualifiedIdentifier)
gen_optGrammar_Event_DefinitionBody = Generalization(general=DefinitionBody, specific=optGrammar_Event)
gen_optGrammar_QualifiedIdentifier_StandardType = Generalization(general=StandardType, specific=optGrammar_QualifiedIdentifier)
gen_optGrammar_QualifiedIdentifier_Expression = Generalization(general=Expression, specific=optGrammar_QualifiedIdentifier)
gen_optGrammar_Field_Qualifier = Generalization(general=Qualifier, specific=optGrammar_Field)
gen_optGrammar_Index_Qualifier = Generalization(general=Qualifier, specific=optGrammar_Index)
gen_optGrammar_Arguments_Qualifier = Generalization(general=Qualifier, specific=optGrammar_Arguments)
gen_optGrammar_Modifier_DefinitionBody = Generalization(general=DefinitionBody, specific=optGrammar_Modifier)
gen_optGrammar_WhileStatement_LoopStructures = Generalization(general=LoopStructures, specific=optGrammar_WhileStatement)
gen_optGrammar_ForStatement_LoopStructures = Generalization(general=LoopStructures, specific=optGrammar_ForStatement)
gen_optGrammar_LoopStructures_Statement = Generalization(general=Statement, specific=optGrammar_LoopStructures)
gen_optGrammar_DoWhileStatement_Statement = Generalization(general=Statement, specific=optGrammar_DoWhileStatement)
gen_optGrammar_EmitStatement_Statement = Generalization(general=Statement, specific=optGrammar_EmitStatement)
gen_optGrammar_DeleteStatement_Statement = Generalization(general=Statement, specific=optGrammar_DeleteStatement)
gen_optGrammar_IfStatement_LoopStructures = Generalization(general=LoopStructures, specific=optGrammar_IfStatement)
gen_optGrammar_NotExpression_Expression = Generalization(general=Expression, specific=optGrammar_NotExpression)
gen_optGrammar_PreIncExpression_Expression = Generalization(general=Expression, specific=optGrammar_PreIncExpression)
gen_optGrammar_PreDecExpression_Expression = Generalization(general=Expression, specific=optGrammar_PreDecExpression)
gen_optGrammar_Body_Statement = Generalization(general=Statement, specific=optGrammar_Body)
gen_optGrammar_ContinueStatement_Statement = Generalization(general=Statement, specific=optGrammar_ContinueStatement)
gen_optGrammar_BreakStatement_Statement = Generalization(general=Statement, specific=optGrammar_BreakStatement)
gen_optGrammar_ReturnStatement_Statement = Generalization(general=Statement, specific=optGrammar_ReturnStatement)
gen_optGrammar_ThrowStatement_Statement = Generalization(general=Statement, specific=optGrammar_ThrowStatement)
gen_optGrammar_PlaceHolderStatement_Statement = Generalization(general=Statement, specific=optGrammar_PlaceHolderStatement)
gen_optGrammar_Expression_PrimaryArithmetic = Generalization(general=PrimaryArithmetic, specific=optGrammar_Expression)
gen_optGrammar_SpecialExpression_Expression = Generalization(general=Expression, specific=optGrammar_SpecialExpression)
gen_optGrammar_BlockhashFunction_Literal = Generalization(general=Literal, specific=optGrammar_BlockhashFunction)
gen_optGrammar_GasleftFunction_Literal = Generalization(general=Literal, specific=optGrammar_GasleftFunction)
gen_optGrammar_BinaryNotExpression_Expression = Generalization(general=Expression, specific=optGrammar_BinaryNotExpression)
gen_optGrammar_SignExpression_Expression = Generalization(general=Expression, specific=optGrammar_SignExpression)
gen_optGrammar_NewExpression_Expression = Generalization(general=Expression, specific=optGrammar_NewExpression)
gen_optGrammar_Literal_Expression = Generalization(general=Expression, specific=optGrammar_Literal)
gen_optGrammar_StringLiteral_Literal = Generalization(general=Literal, specific=optGrammar_StringLiteral)
gen_optGrammar_TypeCast_Expression = Generalization(general=Expression, specific=optGrammar_TypeCast)
gen_optGrammar_MathematicalFunction_Literal = Generalization(general=Literal, specific=optGrammar_MathematicalFunction)
gen_optGrammar_HashFunction_Literal = Generalization(general=Literal, specific=optGrammar_HashFunction)
gen_optGrammar_EcrecoverFunction_Literal = Generalization(general=Literal, specific=optGrammar_EcrecoverFunction)
gen_optGrammar_BooleanLiteral_Literal = Generalization(general=Literal, specific=optGrammar_BooleanLiteral)
gen_optGrammar_NumericLiteral_Literal = Generalization(general=Literal, specific=optGrammar_NumericLiteral)
gen_optGrammar_NumericLiteral_PrimaryArithmetic = Generalization(general=PrimaryArithmetic, specific=optGrammar_NumericLiteral)
gen_optGrammar_SpecialLiteral_Literal = Generalization(general=Literal, specific=optGrammar_SpecialLiteral)
gen_optGrammar_SizedDeclaration_NamedType = Generalization(general=NamedType, specific=optGrammar_SizedDeclaration)
gen_optGrammar_SimpleTypeDeclaration_NamedType = Generalization(general=NamedType, specific=optGrammar_SimpleTypeDeclaration)
gen_optGrammar_StandardVariableDeclaration_SimpleStatement = Generalization(general=SimpleStatement, specific=optGrammar_StandardVariableDeclaration)
gen_optGrammar_StandardVariableDeclaration_SimpleStatement2 = Generalization(general=SimpleStatement2, specific=optGrammar_StandardVariableDeclaration)
gen_optGrammar_Continue_ContinueStatement = Generalization(general=ContinueStatement, specific=optGrammar_Continue)
gen_optGrammar_Assignment_Expression = Generalization(general=Expression, specific=optGrammar_Assignment)
gen_optGrammar_VariableDeclarationExpression_Expression = Generalization(general=Expression, specific=optGrammar_VariableDeclarationExpression)
gen_optGrammar_VarVariableTypeDeclaration_SimpleStatement = Generalization(general=SimpleStatement, specific=optGrammar_VarVariableTypeDeclaration)
gen_optGrammar_VarVariableTypeDeclaration_SimpleStatement2 = Generalization(general=SimpleStatement2, specific=optGrammar_VarVariableTypeDeclaration)
gen_optGrammar_VarVariableTupleVariableDeclaration_SimpleStatement = Generalization(general=SimpleStatement, specific=optGrammar_VarVariableTupleVariableDeclaration)
gen_optGrammar_VarVariableTupleVariableDeclaration_SimpleStatement2 = Generalization(general=SimpleStatement2, specific=optGrammar_VarVariableTupleVariableDeclaration)
gen_optGrammar_Equality_Expression = Generalization(general=Expression, specific=optGrammar_Equality)
gen_optGrammar_Or_Expression = Generalization(general=Expression, specific=optGrammar_Or)
gen_optGrammar_And_Expression = Generalization(general=Expression, specific=optGrammar_And)
gen_optGrammar_BitAnd_Expression = Generalization(general=Expression, specific=optGrammar_BitAnd)
gen_optGrammar_Shift_Expression = Generalization(general=Expression, specific=optGrammar_Shift)
gen_optGrammar_Comparison_Expression = Generalization(general=Expression, specific=optGrammar_Comparison)
gen_optGrammar_BitOr_Expression = Generalization(general=Expression, specific=optGrammar_BitOr)
gen_optGrammar_BitXor_Expression = Generalization(general=Expression, specific=optGrammar_BitXor)
gen_optGrammar_Exponent_Expression = Generalization(general=Expression, specific=optGrammar_Exponent)
gen_optGrammar_PostIncDecExpression_Expression = Generalization(general=Expression, specific=optGrammar_PostIncDecExpression)
gen_optGrammar_AddSub_Expression = Generalization(general=Expression, specific=optGrammar_AddSub)
gen_optGrammar_MulDivMod_Expression = Generalization(general=Expression, specific=optGrammar_MulDivMod)

# Domain Model
domain_model = DomainModel(
    name="optGrammar",
    types={optGrammar_Model, optGrammar_PragmaDirective, optGrammar_DefinitionBody, optGrammar_ConstructorDefinition, DefinitionBody, optGrammar_ParameterList, optGrammar_StateMutability, optGrammar_Const, optGrammar_ModifierInvocation, optGrammar_ImportDirective, optGrammar_Contract, optGrammar_versionOperator, optGrammar_SymbolAlias, optGrammar_InheritanceSpecifier, optGrammar_FunctionDefinition, optGrammar_VisibilityLiteral, optGrammar_Body, optGrammar_FunctionCallListArguments, FunctionCallArguments, optGrammar_Expression, optGrammar_FunctionCallArguments, optGrammar_FunctionCallArg, optGrammar_PrimaryTypeDeclaration, PrimaryTypeDefinitionDeclaration, optGrammar_NonArrayableDeclaration, PrimaryTypeDeclaration, optGrammar_LocationLiteral, optGrammar_SimpleTypeDeclaration, optGrammar_ArrayableDeclaration, optGrammar_SizedDeclaration, optGrammar_ReturnsParameterList, optGrammar_StructDefinition, optGrammar_PrimaryTypeDefinitionDeclaration, optGrammar_EnumDefinition, optGrammar_EnumValue, optGrammar_Variable, optGrammar_Mapping, optGrammar_Tuple, Expression, optGrammar_TupleSeparator, optGrammar_SimpleStatement, Statement, optGrammar_SimpleStatement2, optGrammar_ExpressionStatement, optGrammar_VariableDeclarationOptionalElement, optGrammar_VisibilitySpecifier, VariableDeclarationOptionalElement, optGrammar_IndexedSpecifer, optGrammar_ConstantSpecifier, optGrammar_LocationSpecifier, optGrammar_Type, optGrammar_NamedType, StandardType, StandardTypeWithoutQualifiedIdentifier, optGrammar_ArrayType, optGrammar_StandardType, Type, optGrammar_StandardTypeWithoutQualifiedIdentifier, SimpleStatement, SimpleStatement2, optGrammar_Event, optGrammar_ReturnParameterDeclaration, optGrammar_QualifiedIdentifier, optGrammar_Qualifier, optGrammar_Field, Qualifier, optGrammar_Index, optGrammar_Arguments, optGrammar_Modifier, optGrammar_WhileStatement, optGrammar_ForStatement, optGrammar_LoopStructures, optGrammar_Statement, optGrammar_DoWhileStatement, optGrammar_EmitStatement, optGrammar_FunctionCall, optGrammar_DeleteStatement, optGrammar_IfStatement, LoopStructures, optGrammar_NotExpression, optGrammar_PreIncExpression, optGrammar_PreDecExpression, optGrammar_ContinueStatement, optGrammar_BreakStatement, optGrammar_ReturnStatement, optGrammar_ThrowStatement, optGrammar_PlaceHolderStatement, PrimaryArithmetic, optGrammar_SpecialExpression, optGrammar_BlockhashFunction, Literal, optGrammar_IntParameter, optGrammar_GasleftFunction, optGrammar_BinaryNotExpression, optGrammar_SignExpression, optGrammar_NewExpression, optGrammar_Literal, optGrammar_ArithmeticOperations, optGrammar_PrimaryArithmetic, optGrammar_SecondOperators, optGrammar_HexLiteral, optGrammar_DecimalLiteral, optGrammar_UnitTypes, optGrammar_StringLiteral, optGrammar_TypeCast, optGrammar_MathematicalFunction, optGrammar_HashFunction, optGrammar_EcrecoverFunction, optGrammar_BooleanLiteral, optGrammar_NumericLiteral, optGrammar_IntLiteral, optGrammar_TimeUnitsLiteral, optGrammar_UnitsLiteral, optGrammar_SpecialLiteral, NamedType, optGrammar_StandardVariableDeclaration, optGrammar_Continue, ContinueStatement, optGrammar_Assignment, optGrammar_VariableDeclarationExpression, optGrammar_VarVariableTypeDeclaration, optGrammar_VarVariableTupleVariableDeclaration, optGrammar_Equality, optGrammar_Or, optGrammar_And, optGrammar_BitAnd, optGrammar_Shift, optGrammar_Comparison, optGrammar_BitOr, optGrammar_BitXor, optGrammar_Exponent, optGrammar_PostIncDecExpression, optGrammar_AddSub, optGrammar_MulDivMod, EqualityOpEnum, ComparisonOpEnum, ShiftOpEnum, AdditionOpEnum, AssignmentOpEnum, MulDivModOpEnum, IncDecOpEnum, SpecialExpressionTypeEnum, ReservedWordsEnum},
    associations={pragmaDirective0, body11, parameters13, state14, const16, modifier18, importDirective1, contract3, version5, symbolAliases7, inheritanceSpecifiers9, args31, expr32, parameters35, state37, const40, modifier43, visibility20, block22, superType24, args27, arguments29, ref56, value58, visibility61, location64, type65, type67, visibility46, returnParameters49, block51, members54, members55, value73, keyType76, valueType78, members80, expression82, visibility68, location70, dimension72, parameters94, name96, args99, parameters102, parameters105, typeRef107, qualifiers84, value85, arguments87, parameters89, block91, falseBody124, condition127, body129, initExpression132, conditionExpression133, loopExpression136, body139, variable110, body112, condition113, call116, variable117, condition119, trueBody121, fieldOrMethod147, qualifiers148, expression151, expression153, expression155, statements142, expression145, value169, name172, parameters175, parameter178, param179, expression157, expression159, contract161, args163, first166, seconds167, hexValue192, decimalValue194, etherUnit196, value198, expression200, fun182, parameters185, parameters187, parameters189, intValue191, time203, units205, expression223, left226, expression228, type231, type207, optionalElements208, variable210, expression213, variable216, expression218, tuple221, right246, left249, right251, variable233, expression236, left239, right241, left244, right266, left269, right271, left274, right276, left254, right256, left259, right261, left264, right286, left289, right291, expression294, left279, right281, left284},
    generalizations={gen_optGrammar_ConstructorDefinition_DefinitionBody, gen_optGrammar_FunctionDefinition_DefinitionBody, gen_optGrammar_FunctionCallListArguments_FunctionCallArguments, gen_optGrammar_PrimaryTypeDefinitionDeclaration_DefinitionBody, gen_optGrammar_PrimaryTypeDeclaration_PrimaryTypeDefinitionDeclaration, gen_optGrammar_NonArrayableDeclaration_PrimaryTypeDeclaration, gen_optGrammar_ArrayableDeclaration_PrimaryTypeDeclaration, gen_optGrammar_StructDefinition_DefinitionBody, gen_optGrammar_EnumDefinition_DefinitionBody, gen_optGrammar_Mapping_StandardType, gen_optGrammar_Mapping_StandardTypeWithoutQualifiedIdentifier, gen_optGrammar_Tuple_Expression, gen_optGrammar_TupleSeparator_Expression, gen_optGrammar_SimpleStatement_Statement, gen_optGrammar_ExpressionStatement_SimpleStatement, gen_optGrammar_ExpressionStatement_SimpleStatement2, gen_optGrammar_VisibilitySpecifier_VariableDeclarationOptionalElement, gen_optGrammar_IndexedSpecifer_VariableDeclarationOptionalElement, gen_optGrammar_ConstantSpecifier_VariableDeclarationOptionalElement, gen_optGrammar_LocationSpecifier_VariableDeclarationOptionalElement, gen_optGrammar_NamedType_StandardType, gen_optGrammar_NamedType_StandardTypeWithoutQualifiedIdentifier, gen_optGrammar_StandardType_Type, gen_optGrammar_StandardTypeWithoutQualifiedIdentifier_SimpleStatement, gen_optGrammar_StandardTypeWithoutQualifiedIdentifier_SimpleStatement2, gen_optGrammar_Event_DefinitionBody, gen_optGrammar_QualifiedIdentifier_StandardType, gen_optGrammar_QualifiedIdentifier_Expression, gen_optGrammar_Field_Qualifier, gen_optGrammar_Index_Qualifier, gen_optGrammar_Arguments_Qualifier, gen_optGrammar_Modifier_DefinitionBody, gen_optGrammar_WhileStatement_LoopStructures, gen_optGrammar_ForStatement_LoopStructures, gen_optGrammar_LoopStructures_Statement, gen_optGrammar_DoWhileStatement_Statement, gen_optGrammar_EmitStatement_Statement, gen_optGrammar_DeleteStatement_Statement, gen_optGrammar_IfStatement_LoopStructures, gen_optGrammar_NotExpression_Expression, gen_optGrammar_PreIncExpression_Expression, gen_optGrammar_PreDecExpression_Expression, gen_optGrammar_Body_Statement, gen_optGrammar_ContinueStatement_Statement, gen_optGrammar_BreakStatement_Statement, gen_optGrammar_ReturnStatement_Statement, gen_optGrammar_ThrowStatement_Statement, gen_optGrammar_PlaceHolderStatement_Statement, gen_optGrammar_Expression_PrimaryArithmetic, gen_optGrammar_SpecialExpression_Expression, gen_optGrammar_BlockhashFunction_Literal, gen_optGrammar_GasleftFunction_Literal, gen_optGrammar_BinaryNotExpression_Expression, gen_optGrammar_SignExpression_Expression, gen_optGrammar_NewExpression_Expression, gen_optGrammar_Literal_Expression, gen_optGrammar_StringLiteral_Literal, gen_optGrammar_TypeCast_Expression, gen_optGrammar_MathematicalFunction_Literal, gen_optGrammar_HashFunction_Literal, gen_optGrammar_EcrecoverFunction_Literal, gen_optGrammar_BooleanLiteral_Literal, gen_optGrammar_NumericLiteral_Literal, gen_optGrammar_NumericLiteral_PrimaryArithmetic, gen_optGrammar_SpecialLiteral_Literal, gen_optGrammar_SizedDeclaration_NamedType, gen_optGrammar_SimpleTypeDeclaration_NamedType, gen_optGrammar_StandardVariableDeclaration_SimpleStatement, gen_optGrammar_StandardVariableDeclaration_SimpleStatement2, gen_optGrammar_Continue_ContinueStatement, gen_optGrammar_Assignment_Expression, gen_optGrammar_VariableDeclarationExpression_Expression, gen_optGrammar_VarVariableTypeDeclaration_SimpleStatement, gen_optGrammar_VarVariableTypeDeclaration_SimpleStatement2, gen_optGrammar_VarVariableTupleVariableDeclaration_SimpleStatement, gen_optGrammar_VarVariableTupleVariableDeclaration_SimpleStatement2, gen_optGrammar_Equality_Expression, gen_optGrammar_Or_Expression, gen_optGrammar_And_Expression, gen_optGrammar_BitAnd_Expression, gen_optGrammar_Shift_Expression, gen_optGrammar_Comparison_Expression, gen_optGrammar_BitOr_Expression, gen_optGrammar_BitXor_Expression, gen_optGrammar_Exponent_Expression, gen_optGrammar_PostIncDecExpression_Expression, gen_optGrammar_AddSub_Expression, gen_optGrammar_MulDivMod_Expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)