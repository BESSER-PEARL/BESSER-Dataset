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

# Classes
ast_EJBase = Class(name="ast::EJBase", is_abstract=True)
EJElement = Class(name="EJElement")
ast_DocumentationLine = Class(name="ast::DocumentationLine")
ast_Expression = Class(name="ast::Expression", is_abstract=True)
Feature = Class(name="Feature")
ast_AttributeSet = Class(name="ast::AttributeSet")
ast_Parameter = Class(name="ast::Parameter")
NamedElement = Class(name="NamedElement")
ast_Modifier = Class(name="ast::Modifier")
ast_Variable = Class(name="ast::Variable")
ast_TemplateParameter = Class(name="ast::TemplateParameter")
ast_EJElement = Class(name="ast::EJElement", is_abstract=True)
ast_BehaviorFeature = Class(name="ast::BehaviorFeature")
ast_Identifier = Class(name="ast::Identifier")
ast_ClassBlock = Class(name="ast::ClassBlock")
EJBase = Class(name="EJBase")
ast_ClassifierMemberStatement = Class(name="ast::ClassifierMemberStatement", is_abstract=True)
ast_ConstructorStatement = Class(name="ast::ConstructorStatement")
BehaviorFeature = Class(name="BehaviorFeature")
ast_MethodBlock = Class(name="ast::MethodBlock")
ast_EnumLiteral = Class(name="ast::EnumLiteral")
ClassifierMemberStatement = Class(name="ClassifierMemberStatement")
ast_Feature = Class(name="ast::Feature", is_abstract=True)
ast_FieldStatement = Class(name="ast::FieldStatement")
ast_InitStatement = Class(name="ast::InitStatement", is_abstract=True)
ast_InnerClassifier = Class(name="ast::InnerClassifier")
ast_ClassifierStatement = Class(name="ast::ClassifierStatement", is_abstract=True)
ast_InstanceInitStatement = Class(name="ast::InstanceInitStatement")
InitStatement = Class(name="InitStatement")
ast_MethodStatement = Class(name="ast::MethodStatement")
ast_StaticInitStatement = Class(name="ast::StaticInitStatement")
ast_ClassStatement = Class(name="ast::ClassStatement")
ImplemenationClassifierStatement = Class(name="ImplemenationClassifierStatement")
ast_EnumStatement = Class(name="ast::EnumStatement")
ast_ImplemenationClassifierStatement = Class(name="ast::ImplemenationClassifierStatement", is_abstract=True)
ClassifierStatement = Class(name="ClassifierStatement")
ast_InterfaceStatement = Class(name="ast::InterfaceStatement")
ast_ImportStatement = Class(name="ast::ImportStatement")
TopLevelStatement = Class(name="TopLevelStatement")
ast_PackageStatement = Class(name="ast::PackageStatement")
ast_TopLevelClassifier = Class(name="ast::TopLevelClassifier")
ast_TopLevelStatement = Class(name="ast::TopLevelStatement", is_abstract=True)
ast_BreakStatement = Class(name="ast::BreakStatement")
JumpStatement = Class(name="JumpStatement")
ast_CatchPart = Class(name="ast::CatchPart")
ast_ConditionalLoop = Class(name="ast::ConditionalLoop", is_abstract=True)
LoopStatement = Class(name="LoopStatement")
ast_ContinueStatement = Class(name="ast::ContinueStatement")
ast_SwitchDefaultPartRef = Class(name="ast::SwitchDefaultPartRef")
ast_DoWhileStatement = Class(name="ast::DoWhileStatement")
ConditionalLoop = Class(name="ConditionalLoop")
ast_ExpressionStatement = Class(name="ast::ExpressionStatement")
MethodContentStatement = Class(name="MethodContentStatement")
ast_ForeachStatement = Class(name="ast::ForeachStatement")
ast_ForStatement = Class(name="ast::ForStatement")
ast_LocalVarStatement = Class(name="ast::LocalVarStatement")
ast_IfStatement = Class(name="ast::IfStatement")
ast_IfThenPart = Class(name="ast::IfThenPart")
ast_JumpStatement = Class(name="ast::JumpStatement", is_abstract=True)
ast_Label = Class(name="ast::Label")
ast_LabeledStatement = Class(name="ast::LabeledStatement", is_abstract=True)
ast_LoopStatement = Class(name="ast::LoopStatement", is_abstract=True)
LabeledStatement = Class(name="LabeledStatement")
ast_MethodContentStatement = Class(name="ast::MethodContentStatement", is_abstract=True)
ast_MethodClassifier = Class(name="ast::MethodClassifier")
ast_ScopeStatement = Class(name="ast::ScopeStatement", is_abstract=True)
ast_SwitchDefaultPart = Class(name="ast::SwitchDefaultPart")
ast_SwitchPart = Class(name="ast::SwitchPart", is_abstract=True)
ast_SwitchStatement = Class(name="ast::SwitchStatement")
ast_SynchronizedStatement = Class(name="ast::SynchronizedStatement")
ScopeStatement = Class(name="ScopeStatement")
ast_ThrowStatement = Class(name="ast::ThrowStatement")
ast_TryStatement = Class(name="ast::TryStatement")
ast_WhileStatement = Class(name="ast::WhileStatement")
ast_AccessOp = Class(name="ast::AccessOp")
Expression = Class(name="Expression")
ast_SwitchCasePart = Class(name="ast::SwitchCasePart")
SwitchPart = Class(name="SwitchPart")
ast_ApplySquareOp = Class(name="ast::ApplySquareOp")
ast_ArrayConstructor = Class(name="ast::ArrayConstructor")
ast_AssignmentOp = Class(name="ast::AssignmentOp")
AssignmentOperation = Class(name="AssignmentOperation")
ast_AssignmentOperation = Class(name="ast::AssignmentOperation", is_abstract=True)
ast_BinaryOp = Class(name="ast::BinaryOp", is_abstract=True)
ast_ApplyRoundOp = Class(name="ast::ApplyRoundOp")
ast_BitwiseAndOp = Class(name="ast::BitwiseAndOp")
BinaryOp = Class(name="BinaryOp")
ast_BitwiseComplementOp = Class(name="ast::BitwiseComplementOp")
UnaryOp = Class(name="UnaryOp")
ast_BitwiseOrAssignmentOp = Class(name="ast::BitwiseOrAssignmentOp")
ast_BitwiseOrOp = Class(name="ast::BitwiseOrOp")
ast_BitwiseXorAssignmentOp = Class(name="ast::BitwiseXorAssignmentOp")
ast_BitwiseXorOp = Class(name="ast::BitwiseXorOp")
ast_BooleanLiteral = Class(name="ast::BooleanLiteral")
Literal = Class(name="Literal")
ast_CastOp = Class(name="ast::CastOp")
ClassifierOp = Class(name="ClassifierOp")
ast_CharacterLiteral = Class(name="ast::CharacterLiteral")
ast_ClassifierOp = Class(name="ast::ClassifierOp")
ast_BitwiseAndAssignmentOp = Class(name="ast::BitwiseAndAssignmentOp")
ast_ConditionalAndOp = Class(name="ast::ConditionalAndOp")
ast_ConditionalOp = Class(name="ast::ConditionalOp")
ast_ConditionalOrOp = Class(name="ast::ConditionalOrOp")
ast_DivideAssignmentOp = Class(name="ast::DivideAssignmentOp")
ast_DivideOp = Class(name="ast::DivideOp")
DivisionOp = Class(name="DivisionOp")
ast_DivisionOp = Class(name="ast::DivisionOp", is_abstract=True)
ast_DoubleLiteral = Class(name="ast::DoubleLiteral")
ast_EqualOp = Class(name="ast::EqualOp")
ast_FloatLiteral = Class(name="ast::FloatLiteral")
ast_GreaterOrEqualOp = Class(name="ast::GreaterOrEqualOp")
ast_GreaterThenOp = Class(name="ast::GreaterThenOp")
ast_IdentityOp = Class(name="ast::IdentityOp")
ast_IntegerLiteral = Class(name="ast::IntegerLiteral")
ast_InstanceOfOp = Class(name="ast::InstanceOfOp")
ast_LeftShiftAssignmentOp = Class(name="ast::LeftShiftAssignmentOp")
ast_LeftShiftOp = Class(name="ast::LeftShiftOp")
ShiftOp = Class(name="ShiftOp")
ast_LessOrEqualOp = Class(name="ast::LessOrEqualOp")
ast_LessThenOp = Class(name="ast::LessThenOp")
ast_Literal = Class(name="ast::Literal", is_abstract=True)
ast_LogicalComplementOp = Class(name="ast::LogicalComplementOp")
ast_LongIntegerLiteral = Class(name="ast::LongIntegerLiteral")
ast_MinusAssignmentOp = Class(name="ast::MinusAssignmentOp")
ast_MinusOp = Class(name="ast::MinusOp")
ast_MultiplyOp = Class(name="ast::MultiplyOp")
ast_NotEqualOp = Class(name="ast::NotEqualOp")
ast_NullReference = Class(name="ast::NullReference")
ast_PlusAssignmentOp = Class(name="ast::PlusAssignmentOp")
ast_PlusOp = Class(name="ast::PlusOp")
ast_PostfixDecrementOp = Class(name="ast::PostfixDecrementOp")
ast_PostfixIncrementOp = Class(name="ast::PostfixIncrementOp")
ast_PrefixDecrementOp = Class(name="ast::PrefixDecrementOp")
ast_PrefixIncrementOp = Class(name="ast::PrefixIncrementOp")
ast_PrimitiveType = Class(name="ast::PrimitiveType")
ast_RemainderAssignmentOp = Class(name="ast::RemainderAssignmentOp")
ast_RemainderOp = Class(name="ast::RemainderOp")
ast_ReturnStatement = Class(name="ast::ReturnStatement")
ast_MultiplyAssignmentOp = Class(name="ast::MultiplyAssignmentOp")
ast_NewOp = Class(name="ast::NewOp")
ast_RightShiftOp = Class(name="ast::RightShiftOp")
ast_ShiftOp = Class(name="ast::ShiftOp", is_abstract=True)
ast_StringLiteral = Class(name="ast::StringLiteral")
ast_SuperReference = Class(name="ast::SuperReference")
ast_ThisReference = Class(name="ast::ThisReference")
ast_UnaryMinusOp = Class(name="ast::UnaryMinusOp")
ast_UnaryOp = Class(name="ast::UnaryOp", is_abstract=True)
ast_UnaryPlusOp = Class(name="ast::UnaryPlusOp")
ast_ZeroExtensionRightShiftAssignmentOp = Class(name="ast::ZeroExtensionRightShiftAssignmentOp")
ast_ZeroExtensionRightShiftOp = Class(name="ast::ZeroExtensionRightShiftOp")
ast_NamedElement = Class(name="ast::NamedElement", is_abstract=True)
ast_RightShiftAssignmentOp = Class(name="ast::RightShiftAssignmentOp")
ast_WildcardType = Class(name="ast::WildcardType")
ast_AssertStatement = Class(name="ast::AssertStatement")
ast_EmptyStatement = Class(name="ast::EmptyStatement")
ast_RangeExpression = Class(name="ast::RangeExpression")
ast_AttributeDefinition = Class(name="ast::AttributeDefinition")

# ast_EJBase class attributes and methods

# EJElement class attributes and methods

# ast_DocumentationLine class attributes and methods
ast_DocumentationLine_text: Property = Property(name="text", type=StringType)
ast_DocumentationLine.attributes={ast_DocumentationLine_text}

# ast_Expression class attributes and methods

# Feature class attributes and methods

# ast_AttributeSet class attributes and methods

# ast_Parameter class attributes and methods

# NamedElement class attributes and methods

# ast_Modifier class attributes and methods
ast_Modifier_value: Property = Property(name="value", type=StringType)
ast_Modifier.attributes={ast_Modifier_value}

# ast_Variable class attributes and methods

# ast_TemplateParameter class attributes and methods

# ast_EJElement class attributes and methods
ast_EJElement_startLine: Property = Property(name="startLine", type=IntegerType)
ast_EJElement_endLine: Property = Property(name="endLine", type=IntegerType)
ast_EJElement_startColumn: Property = Property(name="startColumn", type=IntegerType)
ast_EJElement_endColumn: Property = Property(name="endColumn", type=IntegerType)
ast_EJElement_startOffset: Property = Property(name="startOffset", type=StringType)
ast_EJElement_endOffset: Property = Property(name="endOffset", type=StringType)
ast_EJElement.attributes={ast_EJElement_endLine, ast_EJElement_endOffset, ast_EJElement_startOffset, ast_EJElement_startColumn, ast_EJElement_endColumn, ast_EJElement_startLine}

# ast_BehaviorFeature class attributes and methods

# ast_Identifier class attributes and methods
ast_Identifier_quotedValue: Property = Property(name="quotedValue", type=StringType)
ast_Identifier_value: Property = Property(name="value", type=StringType)
ast_Identifier_escapedValue: Property = Property(name="escapedValue", type=StringType)
ast_Identifier.attributes={ast_Identifier_quotedValue, ast_Identifier_escapedValue, ast_Identifier_value}

# ast_ClassBlock class attributes and methods

# EJBase class attributes and methods

# ast_ClassifierMemberStatement class attributes and methods

# ast_ConstructorStatement class attributes and methods

# BehaviorFeature class attributes and methods

# ast_MethodBlock class attributes and methods

# ast_EnumLiteral class attributes and methods

# ClassifierMemberStatement class attributes and methods

# ast_Feature class attributes and methods

# ast_FieldStatement class attributes and methods

# ast_InitStatement class attributes and methods

# ast_InnerClassifier class attributes and methods

# ast_ClassifierStatement class attributes and methods

# ast_InstanceInitStatement class attributes and methods

# InitStatement class attributes and methods

# ast_MethodStatement class attributes and methods

# ast_StaticInitStatement class attributes and methods

# ast_ClassStatement class attributes and methods

# ImplemenationClassifierStatement class attributes and methods

# ast_EnumStatement class attributes and methods

# ast_ImplemenationClassifierStatement class attributes and methods

# ClassifierStatement class attributes and methods

# ast_InterfaceStatement class attributes and methods

# ast_ImportStatement class attributes and methods

# TopLevelStatement class attributes and methods

# ast_PackageStatement class attributes and methods

# ast_TopLevelClassifier class attributes and methods

# ast_TopLevelStatement class attributes and methods

# ast_BreakStatement class attributes and methods

# JumpStatement class attributes and methods

# ast_CatchPart class attributes and methods

# ast_ConditionalLoop class attributes and methods

# LoopStatement class attributes and methods

# ast_ContinueStatement class attributes and methods

# ast_SwitchDefaultPartRef class attributes and methods

# ast_DoWhileStatement class attributes and methods

# ConditionalLoop class attributes and methods

# ast_ExpressionStatement class attributes and methods

# MethodContentStatement class attributes and methods

# ast_ForeachStatement class attributes and methods

# ast_ForStatement class attributes and methods

# ast_LocalVarStatement class attributes and methods

# ast_IfStatement class attributes and methods

# ast_IfThenPart class attributes and methods

# ast_JumpStatement class attributes and methods

# ast_Label class attributes and methods
ast_Label_name: Property = Property(name="name", type=StringType)
ast_Label.attributes={ast_Label_name}

# ast_LabeledStatement class attributes and methods

# ast_LoopStatement class attributes and methods

# LabeledStatement class attributes and methods

# ast_MethodContentStatement class attributes and methods

# ast_MethodClassifier class attributes and methods

# ast_ScopeStatement class attributes and methods

# ast_SwitchDefaultPart class attributes and methods

# ast_SwitchPart class attributes and methods

# ast_SwitchStatement class attributes and methods

# ast_SynchronizedStatement class attributes and methods

# ScopeStatement class attributes and methods

# ast_ThrowStatement class attributes and methods

# ast_TryStatement class attributes and methods

# ast_WhileStatement class attributes and methods

# ast_AccessOp class attributes and methods

# Expression class attributes and methods

# ast_SwitchCasePart class attributes and methods

# SwitchPart class attributes and methods

# ast_ApplySquareOp class attributes and methods

# ast_ArrayConstructor class attributes and methods

# ast_AssignmentOp class attributes and methods

# AssignmentOperation class attributes and methods

# ast_AssignmentOperation class attributes and methods

# ast_BinaryOp class attributes and methods

# ast_ApplyRoundOp class attributes and methods

# ast_BitwiseAndOp class attributes and methods

# BinaryOp class attributes and methods

# ast_BitwiseComplementOp class attributes and methods

# UnaryOp class attributes and methods

# ast_BitwiseOrAssignmentOp class attributes and methods

# ast_BitwiseOrOp class attributes and methods

# ast_BitwiseXorAssignmentOp class attributes and methods

# ast_BitwiseXorOp class attributes and methods

# ast_BooleanLiteral class attributes and methods

# Literal class attributes and methods

# ast_CastOp class attributes and methods

# ClassifierOp class attributes and methods

# ast_CharacterLiteral class attributes and methods

# ast_ClassifierOp class attributes and methods

# ast_BitwiseAndAssignmentOp class attributes and methods

# ast_ConditionalAndOp class attributes and methods

# ast_ConditionalOp class attributes and methods

# ast_ConditionalOrOp class attributes and methods

# ast_DivideAssignmentOp class attributes and methods

# ast_DivideOp class attributes and methods

# DivisionOp class attributes and methods

# ast_DivisionOp class attributes and methods

# ast_DoubleLiteral class attributes and methods

# ast_EqualOp class attributes and methods

# ast_FloatLiteral class attributes and methods

# ast_GreaterOrEqualOp class attributes and methods

# ast_GreaterThenOp class attributes and methods

# ast_IdentityOp class attributes and methods

# ast_IntegerLiteral class attributes and methods

# ast_InstanceOfOp class attributes and methods

# ast_LeftShiftAssignmentOp class attributes and methods

# ast_LeftShiftOp class attributes and methods

# ShiftOp class attributes and methods

# ast_LessOrEqualOp class attributes and methods

# ast_LessThenOp class attributes and methods

# ast_Literal class attributes and methods
ast_Literal_value: Property = Property(name="value", type=StringType)
ast_Literal.attributes={ast_Literal_value}

# ast_LogicalComplementOp class attributes and methods

# ast_LongIntegerLiteral class attributes and methods

# ast_MinusAssignmentOp class attributes and methods

# ast_MinusOp class attributes and methods

# ast_MultiplyOp class attributes and methods

# ast_NotEqualOp class attributes and methods

# ast_NullReference class attributes and methods

# ast_PlusAssignmentOp class attributes and methods

# ast_PlusOp class attributes and methods

# ast_PostfixDecrementOp class attributes and methods

# ast_PostfixIncrementOp class attributes and methods

# ast_PrefixDecrementOp class attributes and methods

# ast_PrefixIncrementOp class attributes and methods

# ast_PrimitiveType class attributes and methods
ast_PrimitiveType_name: Property = Property(name="name", type=StringType)
ast_PrimitiveType.attributes={ast_PrimitiveType_name}

# ast_RemainderAssignmentOp class attributes and methods

# ast_RemainderOp class attributes and methods

# ast_ReturnStatement class attributes and methods

# ast_MultiplyAssignmentOp class attributes and methods

# ast_NewOp class attributes and methods

# ast_RightShiftOp class attributes and methods

# ast_ShiftOp class attributes and methods

# ast_StringLiteral class attributes and methods

# ast_SuperReference class attributes and methods
ast_SuperReference_name: Property = Property(name="name", type=StringType)
ast_SuperReference.attributes={ast_SuperReference_name}

# ast_ThisReference class attributes and methods
ast_ThisReference_name: Property = Property(name="name", type=StringType)
ast_ThisReference.attributes={ast_ThisReference_name}

# ast_UnaryMinusOp class attributes and methods

# ast_UnaryOp class attributes and methods

# ast_UnaryPlusOp class attributes and methods

# ast_ZeroExtensionRightShiftAssignmentOp class attributes and methods

# ast_ZeroExtensionRightShiftOp class attributes and methods

# ast_NamedElement class attributes and methods

# ast_RightShiftAssignmentOp class attributes and methods

# ast_WildcardType class attributes and methods

# ast_AssertStatement class attributes and methods

# ast_EmptyStatement class attributes and methods

# ast_RangeExpression class attributes and methods

# ast_AttributeDefinition class attributes and methods

# Relationships
documentation0: BinaryAssociation = BinaryAssociation(
    name="documentation0",
    ends={
        Property(name="ast_DocumentationLine", type=ast_EJBase, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_EJBase", type=ast_DocumentationLine, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributeSets1: BinaryAssociation = BinaryAssociation(
    name="attributeSets1",
    ends={
        Property(name="ast_AttributeSet", type=ast_EJBase, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_EJBase2", type=ast_AttributeSet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributes3: BinaryAssociation = BinaryAssociation(
    name="attributes3",
    ends={
        Property(name="ast_Expression", type=ast_AttributeSet, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_AttributeSet4", type=ast_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
finalModifier5: BinaryAssociation = BinaryAssociation(
    name="finalModifier5",
    ends={
        Property(name="ast_Modifier", type=ast_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_Parameter", type=ast_Modifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
classifier6: BinaryAssociation = BinaryAssociation(
    name="classifier6",
    ends={
        Property(name="ast_Expression8", type=ast_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_Parameter7", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initialValue9: BinaryAssociation = BinaryAssociation(
    name="initialValue9",
    ends={
        Property(name="ast_Expression10", type=ast_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_Variable", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
extendedTypes11: BinaryAssociation = BinaryAssociation(
    name="extendedTypes11",
    ends={
        Property(name="ast_Expression12", type=ast_TemplateParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_TemplateParameter", type=ast_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superToTypes13: BinaryAssociation = BinaryAssociation(
    name="superToTypes13",
    ends={
        Property(name="ast_Expression15", type=ast_TemplateParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_TemplateParameter14", type=ast_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exceptions16: BinaryAssociation = BinaryAssociation(
    name="exceptions16",
    ends={
        Property(name="ast_Expression17", type=ast_BehaviorFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_BehaviorFeature", type=ast_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name18: BinaryAssociation = BinaryAssociation(
    name="name18",
    ends={
        Property(name="ast_Identifier", type=ast_BehaviorFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_BehaviorFeature19", type=ast_Identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters20: BinaryAssociation = BinaryAssociation(
    name="parameters20",
    ends={
        Property(name="ast_Parameter22", type=ast_BehaviorFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_BehaviorFeature21", type=ast_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
templateParameters23: BinaryAssociation = BinaryAssociation(
    name="templateParameters23",
    ends={
        Property(name="ast_TemplateParameter25", type=ast_BehaviorFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_BehaviorFeature24", type=ast_TemplateParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
content26: BinaryAssociation = BinaryAssociation(
    name="content26",
    ends={
        Property(name="ast_ClassifierMemberStatement", type=ast_ClassBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_ClassBlock", type=ast_ClassifierMemberStatement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body27: BinaryAssociation = BinaryAssociation(
    name="body27",
    ends={
        Property(name="ast_MethodBlock", type=ast_ConstructorStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_ConstructorStatement", type=ast_MethodBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
args28: BinaryAssociation = BinaryAssociation(
    name="args28",
    ends={
        Property(name="ast_Expression29", type=ast_EnumLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_EnumLiteral", type=ast_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name30: BinaryAssociation = BinaryAssociation(
    name="name30",
    ends={
        Property(name="ast_Identifier32", type=ast_EnumLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_EnumLiteral31", type=ast_Identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body33: BinaryAssociation = BinaryAssociation(
    name="body33",
    ends={
        Property(name="ast_ClassBlock35", type=ast_EnumLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_EnumLiteral34", type=ast_ClassBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
visibilityModifier36: BinaryAssociation = BinaryAssociation(
    name="visibilityModifier36",
    ends={
        Property(name="ast_Modifier37", type=ast_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_Feature", type=ast_Modifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
strictfpModifier72: BinaryAssociation = BinaryAssociation(
    name="strictfpModifier72",
    ends={
        Property(name="ast_Modifier74", type=ast_MethodStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_MethodStatement73", type=ast_Modifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
staticModifier38: BinaryAssociation = BinaryAssociation(
    name="staticModifier38",
    ends={
        Property(name="ast_Modifier40", type=ast_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_Feature39", type=ast_Modifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
finalModifier41: BinaryAssociation = BinaryAssociation(
    name="finalModifier41",
    ends={
        Property(name="ast_Modifier43", type=ast_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_Feature42", type=ast_Modifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
transientModifier44: BinaryAssociation = BinaryAssociation(
    name="transientModifier44",
    ends={
        Property(name="ast_Modifier45", type=ast_FieldStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_FieldStatement", type=ast_Modifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
volatileModifier46: BinaryAssociation = BinaryAssociation(
    name="volatileModifier46",
    ends={
        Property(name="ast_Modifier48", type=ast_FieldStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_FieldStatement47", type=ast_Modifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
classifier49: BinaryAssociation = BinaryAssociation(
    name="classifier49",
    ends={
        Property(name="ast_Expression51", type=ast_FieldStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_FieldStatement50", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variables52: BinaryAssociation = BinaryAssociation(
    name="variables52",
    ends={
        Property(name="ast_Variable54", type=ast_FieldStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_FieldStatement53", type=ast_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body55: BinaryAssociation = BinaryAssociation(
    name="body55",
    ends={
        Property(name="ast_MethodBlock56", type=ast_InitStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_InitStatement", type=ast_MethodBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
classifier57: BinaryAssociation = BinaryAssociation(
    name="classifier57",
    ends={
        Property(name="ast_ClassifierStatement", type=ast_InnerClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_InnerClassifier", type=ast_ClassifierStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body58: BinaryAssociation = BinaryAssociation(
    name="body58",
    ends={
        Property(name="ast_MethodBlock59", type=ast_MethodStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_MethodStatement", type=ast_MethodBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
returnType60: BinaryAssociation = BinaryAssociation(
    name="returnType60",
    ends={
        Property(name="ast_Expression62", type=ast_MethodStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_MethodStatement61", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
abstractModifier63: BinaryAssociation = BinaryAssociation(
    name="abstractModifier63",
    ends={
        Property(name="ast_Modifier65", type=ast_MethodStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_MethodStatement64", type=ast_Modifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
synchronizedModifier66: BinaryAssociation = BinaryAssociation(
    name="synchronizedModifier66",
    ends={
        Property(name="ast_Modifier68", type=ast_MethodStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_MethodStatement67", type=ast_Modifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nativeModifier69: BinaryAssociation = BinaryAssociation(
    name="nativeModifier69",
    ends={
        Property(name="ast_Modifier71", type=ast_MethodStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_MethodStatement70", type=ast_Modifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name75: BinaryAssociation = BinaryAssociation(
    name="name75",
    ends={
        Property(name="ast_Identifier77", type=ast_ClassifierStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_ClassifierStatement76", type=ast_Identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
visibilityModifier78: BinaryAssociation = BinaryAssociation(
    name="visibilityModifier78",
    ends={
        Property(name="ast_Modifier80", type=ast_ClassifierStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_ClassifierStatement79", type=ast_Modifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
templateParameters81: BinaryAssociation = BinaryAssociation(
    name="templateParameters81",
    ends={
        Property(name="ast_TemplateParameter83", type=ast_ClassifierStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_ClassifierStatement82", type=ast_TemplateParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
contents84: BinaryAssociation = BinaryAssociation(
    name="contents84",
    ends={
        Property(name="ast_ClassifierMemberStatement86", type=ast_ClassifierStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_ClassifierStatement85", type=ast_ClassifierMemberStatement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
staticModifier87: BinaryAssociation = BinaryAssociation(
    name="staticModifier87",
    ends={
        Property(name="ast_Modifier88", type=ast_ClassStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_ClassStatement", type=ast_Modifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
extendedType89: BinaryAssociation = BinaryAssociation(
    name="extendedType89",
    ends={
        Property(name="ast_Expression91", type=ast_ClassStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_ClassStatement90", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
implementedTypes92: BinaryAssociation = BinaryAssociation(
    name="implementedTypes92",
    ends={
        Property(name="ast_Expression94", type=ast_ClassStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_ClassStatement93", type=ast_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
strictfpModifier95: BinaryAssociation = BinaryAssociation(
    name="strictfpModifier95",
    ends={
        Property(name="ast_Modifier96", type=ast_ImplemenationClassifierStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_ImplemenationClassifierStatement", type=ast_Modifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
abstractModifier97: BinaryAssociation = BinaryAssociation(
    name="abstractModifier97",
    ends={
        Property(name="ast_Modifier99", type=ast_ImplemenationClassifierStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_ImplemenationClassifierStatement98", type=ast_Modifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
finalModifier100: BinaryAssociation = BinaryAssociation(
    name="finalModifier100",
    ends={
        Property(name="ast_Modifier102", type=ast_ImplemenationClassifierStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_ImplemenationClassifierStatement101", type=ast_Modifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
extendedTypes103: BinaryAssociation = BinaryAssociation(
    name="extendedTypes103",
    ends={
        Property(name="ast_Expression104", type=ast_InterfaceStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_InterfaceStatement", type=ast_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
staticModifier105: BinaryAssociation = BinaryAssociation(
    name="staticModifier105",
    ends={
        Property(name="ast_Modifier106", type=ast_ImportStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_ImportStatement", type=ast_Modifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
allModifier107: BinaryAssociation = BinaryAssociation(
    name="allModifier107",
    ends={
        Property(name="ast_Modifier109", type=ast_ImportStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_ImportStatement108", type=ast_Modifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
limit138: BinaryAssociation = BinaryAssociation(
    name="limit138",
    ends={
        Property(name="ast_Expression140", type=ast_ForeachStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_ForeachStatement139", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
importedPackage110: BinaryAssociation = BinaryAssociation(
    name="importedPackage110",
    ends={
        Property(name="ast_Expression112", type=ast_ImportStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_ImportStatement111", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name113: BinaryAssociation = BinaryAssociation(
    name="name113",
    ends={
        Property(name="ast_Expression114", type=ast_PackageStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_PackageStatement", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
classifier115: BinaryAssociation = BinaryAssociation(
    name="classifier115",
    ends={
        Property(name="ast_ClassifierStatement116", type=ast_TopLevelClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_TopLevelClassifier", type=ast_ClassifierStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
specification117: BinaryAssociation = BinaryAssociation(
    name="specification117",
    ends={
        Property(name="ast_Parameter118", type=ast_CatchPart, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_CatchPart", type=ast_Parameter, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body119: BinaryAssociation = BinaryAssociation(
    name="body119",
    ends={
        Property(name="ast_MethodBlock121", type=ast_CatchPart, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_CatchPart120", type=ast_MethodBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition122: BinaryAssociation = BinaryAssociation(
    name="condition122",
    ends={
        Property(name="ast_Expression123", type=ast_ConditionalLoop, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_ConditionalLoop", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
defaultLabel124: BinaryAssociation = BinaryAssociation(
    name="defaultLabel124",
    ends={
        Property(name="ast_SwitchDefaultPartRef", type=ast_ContinueStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_ContinueStatement", type=ast_SwitchDefaultPartRef, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
caseValue125: BinaryAssociation = BinaryAssociation(
    name="caseValue125",
    ends={
        Property(name="ast_Expression127", type=ast_ContinueStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_ContinueStatement126", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression128: BinaryAssociation = BinaryAssociation(
    name="expression128",
    ends={
        Property(name="ast_Expression129", type=ast_ExpressionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_ExpressionStatement", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameter130: BinaryAssociation = BinaryAssociation(
    name="parameter130",
    ends={
        Property(name="ast_Parameter131", type=ast_ForeachStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_ForeachStatement", type=ast_Parameter, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
collection132: BinaryAssociation = BinaryAssociation(
    name="collection132",
    ends={
        Property(name="ast_Expression134", type=ast_ForeachStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_ForeachStatement133", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initial135: BinaryAssociation = BinaryAssociation(
    name="initial135",
    ends={
        Property(name="ast_Expression137", type=ast_ForeachStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_ForeachStatement136", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initVariableDeclaration141: BinaryAssociation = BinaryAssociation(
    name="initVariableDeclaration141",
    ends={
        Property(name="ast_LocalVarStatement", type=ast_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_ForStatement", type=ast_LocalVarStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initExpressions142: BinaryAssociation = BinaryAssociation(
    name="initExpressions142",
    ends={
        Property(name="ast_Expression144", type=ast_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_ForStatement143", type=ast_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
updateExpressions145: BinaryAssociation = BinaryAssociation(
    name="updateExpressions145",
    ends={
        Property(name="ast_Expression147", type=ast_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_ForStatement146", type=ast_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ifThenPart148: BinaryAssociation = BinaryAssociation(
    name="ifThenPart148",
    ends={
        Property(name="ast_IfThenPart", type=ast_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_IfStatement", type=ast_IfThenPart, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
elsePart149: BinaryAssociation = BinaryAssociation(
    name="elsePart149",
    ends={
        Property(name="ast_MethodBlock151", type=ast_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_IfStatement150", type=ast_MethodBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition152: BinaryAssociation = BinaryAssociation(
    name="condition152",
    ends={
        Property(name="ast_Expression154", type=ast_IfThenPart, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_IfThenPart153", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body155: BinaryAssociation = BinaryAssociation(
    name="body155",
    ends={
        Property(name="ast_MethodBlock157", type=ast_IfThenPart, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_IfThenPart156", type=ast_MethodBlock, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
label158: BinaryAssociation = BinaryAssociation(
    name="label158",
    ends={
        Property(name="ast_Label", type=ast_JumpStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_JumpStatement", type=ast_Label, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
label159: BinaryAssociation = BinaryAssociation(
    name="label159",
    ends={
        Property(name="ast_Label160", type=ast_LabeledStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_LabeledStatement", type=ast_Label, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
finalModifier161: BinaryAssociation = BinaryAssociation(
    name="finalModifier161",
    ends={
        Property(name="ast_Modifier163", type=ast_LocalVarStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_LocalVarStatement162", type=ast_Modifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variables164: BinaryAssociation = BinaryAssociation(
    name="variables164",
    ends={
        Property(name="ast_Variable166", type=ast_LocalVarStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_LocalVarStatement165", type=ast_Variable, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
classifier167: BinaryAssociation = BinaryAssociation(
    name="classifier167",
    ends={
        Property(name="ast_Expression169", type=ast_LocalVarStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_LocalVarStatement168", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body170: BinaryAssociation = BinaryAssociation(
    name="body170",
    ends={
        Property(name="ast_MethodBlock171", type=ast_LoopStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_LoopStatement", type=ast_MethodBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
content172: BinaryAssociation = BinaryAssociation(
    name="content172",
    ends={
        Property(name="ast_MethodContentStatement", type=ast_MethodBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_MethodBlock173", type=ast_MethodContentStatement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
classifier174: BinaryAssociation = BinaryAssociation(
    name="classifier174",
    ends={
        Property(name="ast_ClassifierStatement175", type=ast_MethodClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_MethodClassifier", type=ast_ClassifierStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
values178: BinaryAssociation = BinaryAssociation(
    name="values178",
    ends={
        Property(name="ast_Expression179", type=ast_SwitchCasePart, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_SwitchCasePart", type=ast_Expression, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
body180: BinaryAssociation = BinaryAssociation(
    name="body180",
    ends={
        Property(name="ast_MethodBlock181", type=ast_SwitchPart, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_SwitchPart", type=ast_MethodBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value182: BinaryAssociation = BinaryAssociation(
    name="value182",
    ends={
        Property(name="ast_Expression183", type=ast_SwitchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_SwitchStatement", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parts184: BinaryAssociation = BinaryAssociation(
    name="parts184",
    ends={
        Property(name="ast_SwitchPart186", type=ast_SwitchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_SwitchStatement185", type=ast_SwitchPart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value187: BinaryAssociation = BinaryAssociation(
    name="value187",
    ends={
        Property(name="ast_Expression188", type=ast_SynchronizedStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_SynchronizedStatement", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exception189: BinaryAssociation = BinaryAssociation(
    name="exception189",
    ends={
        Property(name="ast_Expression190", type=ast_ThrowStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_ThrowStatement", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
finallyPart191: BinaryAssociation = BinaryAssociation(
    name="finallyPart191",
    ends={
        Property(name="ast_MethodBlock192", type=ast_TryStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_TryStatement", type=ast_MethodBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
catchPart193: BinaryAssociation = BinaryAssociation(
    name="catchPart193",
    ends={
        Property(name="ast_CatchPart195", type=ast_TryStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_TryStatement194", type=ast_CatchPart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
accessed196: BinaryAssociation = BinaryAssociation(
    name="accessed196",
    ends={
        Property(name="ast_Expression197", type=ast_AccessOp, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_AccessOp", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
feature198: BinaryAssociation = BinaryAssociation(
    name="feature198",
    ends={
        Property(name="ast_Expression200", type=ast_AccessOp, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_AccessOp199", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body176: BinaryAssociation = BinaryAssociation(
    name="body176",
    ends={
        Property(name="ast_MethodBlock177", type=ast_ScopeStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_ScopeStatement", type=ast_MethodBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
args203: BinaryAssociation = BinaryAssociation(
    name="args203",
    ends={
        Property(name="ast_Expression205", type=ast_ApplyRoundOp, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_ApplyRoundOp204", type=ast_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
functor206: BinaryAssociation = BinaryAssociation(
    name="functor206",
    ends={
        Property(name="ast_Expression207", type=ast_ApplySquareOp, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_ApplySquareOp", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
args208: BinaryAssociation = BinaryAssociation(
    name="args208",
    ends={
        Property(name="ast_Expression210", type=ast_ApplySquareOp, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_ApplySquareOp209", type=ast_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
values211: BinaryAssociation = BinaryAssociation(
    name="values211",
    ends={
        Property(name="ast_Expression212", type=ast_ArrayConstructor, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_ArrayConstructor", type=ast_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
leftHandSide213: BinaryAssociation = BinaryAssociation(
    name="leftHandSide213",
    ends={
        Property(name="ast_Expression214", type=ast_AssignmentOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_AssignmentOperation", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value215: BinaryAssociation = BinaryAssociation(
    name="value215",
    ends={
        Property(name="ast_Expression217", type=ast_AssignmentOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_AssignmentOperation216", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value1218: BinaryAssociation = BinaryAssociation(
    name="value1218",
    ends={
        Property(name="ast_Expression219", type=ast_BinaryOp, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_BinaryOp", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value2220: BinaryAssociation = BinaryAssociation(
    name="value2220",
    ends={
        Property(name="ast_Expression222", type=ast_BinaryOp, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_BinaryOp221", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
functor201: BinaryAssociation = BinaryAssociation(
    name="functor201",
    ends={
        Property(name="ast_Expression202", type=ast_ApplyRoundOp, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_ApplyRoundOp", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value223: BinaryAssociation = BinaryAssociation(
    name="value223",
    ends={
        Property(name="ast_Expression224", type=ast_ClassifierOp, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_ClassifierOp", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition228: BinaryAssociation = BinaryAssociation(
    name="condition228",
    ends={
        Property(name="ast_Expression229", type=ast_ConditionalOp, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_ConditionalOp", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
thenPart230: BinaryAssociation = BinaryAssociation(
    name="thenPart230",
    ends={
        Property(name="ast_Expression232", type=ast_ConditionalOp, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_ConditionalOp231", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elsePart233: BinaryAssociation = BinaryAssociation(
    name="elsePart233",
    ends={
        Property(name="ast_Expression235", type=ast_ConditionalOp, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_ConditionalOp234", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dividend236: BinaryAssociation = BinaryAssociation(
    name="dividend236",
    ends={
        Property(name="ast_Expression237", type=ast_DivisionOp, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_DivisionOp", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
divisor238: BinaryAssociation = BinaryAssociation(
    name="divisor238",
    ends={
        Property(name="ast_Expression240", type=ast_DivisionOp, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_DivisionOp239", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
classifier225: BinaryAssociation = BinaryAssociation(
    name="classifier225",
    ends={
        Property(name="ast_Expression227", type=ast_ClassifierOp, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_ClassifierOp226", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value241: BinaryAssociation = BinaryAssociation(
    name="value241",
    ends={
        Property(name="ast_Expression242", type=ast_IdentityOp, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_IdentityOp", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
minuend243: BinaryAssociation = BinaryAssociation(
    name="minuend243",
    ends={
        Property(name="ast_Expression244", type=ast_MinusOp, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_MinusOp", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
subtrahend245: BinaryAssociation = BinaryAssociation(
    name="subtrahend245",
    ends={
        Property(name="ast_Expression247", type=ast_MinusOp, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_MinusOp246", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
multipliers248: BinaryAssociation = BinaryAssociation(
    name="multipliers248",
    ends={
        Property(name="ast_Expression249", type=ast_MultiplyOp, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_MultiplyOp", type=ast_Expression, multiplicity=Multiplicity(2, 2), is_composite=True)
    }
)
classifier250: BinaryAssociation = BinaryAssociation(
    name="classifier250",
    ends={
        Property(name="ast_Expression251", type=ast_NewOp, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_NewOp", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
args252: BinaryAssociation = BinaryAssociation(
    name="args252",
    ends={
        Property(name="ast_Expression254", type=ast_NewOp, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_NewOp253", type=ast_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
classBody255: BinaryAssociation = BinaryAssociation(
    name="classBody255",
    ends={
        Property(name="ast_ClassBlock257", type=ast_NewOp, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_NewOp256", type=ast_ClassBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arrayConstructor258: BinaryAssociation = BinaryAssociation(
    name="arrayConstructor258",
    ends={
        Property(name="ast_ArrayConstructor260", type=ast_NewOp, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_NewOp259", type=ast_ArrayConstructor, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
summands261: BinaryAssociation = BinaryAssociation(
    name="summands261",
    ends={
        Property(name="ast_Expression262", type=ast_PlusOp, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_PlusOp", type=ast_Expression, multiplicity=Multiplicity(2, 2), is_composite=True)
    }
)
value263: BinaryAssociation = BinaryAssociation(
    name="value263",
    ends={
        Property(name="ast_Expression264", type=ast_ReturnStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_ReturnStatement", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value265: BinaryAssociation = BinaryAssociation(
    name="value265",
    ends={
        Property(name="ast_Expression266", type=ast_ShiftOp, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_ShiftOp", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
distance267: BinaryAssociation = BinaryAssociation(
    name="distance267",
    ends={
        Property(name="ast_Expression269", type=ast_ShiftOp, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_ShiftOp268", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value270: BinaryAssociation = BinaryAssociation(
    name="value270",
    ends={
        Property(name="ast_Expression271", type=ast_UnaryOp, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_UnaryOp", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name272: BinaryAssociation = BinaryAssociation(
    name="name272",
    ends={
        Property(name="ast_Identifier273", type=ast_NamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_NamedElement", type=ast_Identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
superToTypes284: BinaryAssociation = BinaryAssociation(
    name="superToTypes284",
    ends={
        Property(name="ast_Expression285", type=ast_WildcardType, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_WildcardType", type=ast_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extendedTypes286: BinaryAssociation = BinaryAssociation(
    name="extendedTypes286",
    ends={
        Property(name="ast_Expression288", type=ast_WildcardType, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_WildcardType287", type=ast_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
test274: BinaryAssociation = BinaryAssociation(
    name="test274",
    ends={
        Property(name="ast_Expression275", type=ast_AssertStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_AssertStatement", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
message276: BinaryAssociation = BinaryAssociation(
    name="message276",
    ends={
        Property(name="ast_Expression278", type=ast_AssertStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_AssertStatement277", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initial279: BinaryAssociation = BinaryAssociation(
    name="initial279",
    ends={
        Property(name="ast_Expression280", type=ast_RangeExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_RangeExpression", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
limit281: BinaryAssociation = BinaryAssociation(
    name="limit281",
    ends={
        Property(name="ast_Expression283", type=ast_RangeExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_RangeExpression282", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_ast_EJBase_EJElement = Generalization(general=EJElement, specific=ast_EJBase)
gen_ast_BehaviorFeature_Feature = Generalization(general=Feature, specific=ast_BehaviorFeature)
gen_ast_Parameter_NamedElement = Generalization(general=NamedElement, specific=ast_Parameter)
gen_ast_Variable_NamedElement = Generalization(general=NamedElement, specific=ast_Variable)
gen_ast_TemplateParameter_NamedElement = Generalization(general=NamedElement, specific=ast_TemplateParameter)
gen_ast_Modifier_EJElement = Generalization(general=EJElement, specific=ast_Modifier)
gen_ast_DocumentationLine_EJElement = Generalization(general=EJElement, specific=ast_DocumentationLine)
gen_ast_AttributeSet_EJElement = Generalization(general=EJElement, specific=ast_AttributeSet)
gen_ast_ClassBlock_EJBase = Generalization(general=EJBase, specific=ast_ClassBlock)
gen_ast_ClassifierMemberStatement_EJBase = Generalization(general=EJBase, specific=ast_ClassifierMemberStatement)
gen_ast_ConstructorStatement_BehaviorFeature = Generalization(general=BehaviorFeature, specific=ast_ConstructorStatement)
gen_ast_EnumLiteral_ClassifierMemberStatement = Generalization(general=ClassifierMemberStatement, specific=ast_EnumLiteral)
gen_ast_Feature_ClassifierMemberStatement = Generalization(general=ClassifierMemberStatement, specific=ast_Feature)
gen_ast_FieldStatement_Feature = Generalization(general=Feature, specific=ast_FieldStatement)
gen_ast_InitStatement_ClassifierMemberStatement = Generalization(general=ClassifierMemberStatement, specific=ast_InitStatement)
gen_ast_InnerClassifier_ClassifierMemberStatement = Generalization(general=ClassifierMemberStatement, specific=ast_InnerClassifier)
gen_ast_InstanceInitStatement_InitStatement = Generalization(general=InitStatement, specific=ast_InstanceInitStatement)
gen_ast_MethodStatement_BehaviorFeature = Generalization(general=BehaviorFeature, specific=ast_MethodStatement)
gen_ast_StaticInitStatement_InitStatement = Generalization(general=InitStatement, specific=ast_StaticInitStatement)
gen_ast_ClassifierStatement_EJBase = Generalization(general=EJBase, specific=ast_ClassifierStatement)
gen_ast_ClassStatement_ImplemenationClassifierStatement = Generalization(general=ImplemenationClassifierStatement, specific=ast_ClassStatement)
gen_ast_EnumStatement_ImplemenationClassifierStatement = Generalization(general=ImplemenationClassifierStatement, specific=ast_EnumStatement)
gen_ast_ImplemenationClassifierStatement_ClassifierStatement = Generalization(general=ClassifierStatement, specific=ast_ImplemenationClassifierStatement)
gen_ast_InterfaceStatement_ClassifierStatement = Generalization(general=ClassifierStatement, specific=ast_InterfaceStatement)
gen_ast_ImportStatement_TopLevelStatement = Generalization(general=TopLevelStatement, specific=ast_ImportStatement)
gen_ast_PackageStatement_TopLevelStatement = Generalization(general=TopLevelStatement, specific=ast_PackageStatement)
gen_ast_TopLevelClassifier_TopLevelStatement = Generalization(general=TopLevelStatement, specific=ast_TopLevelClassifier)
gen_ast_TopLevelStatement_EJBase = Generalization(general=EJBase, specific=ast_TopLevelStatement)
gen_ast_BreakStatement_JumpStatement = Generalization(general=JumpStatement, specific=ast_BreakStatement)
gen_ast_CatchPart_EJBase = Generalization(general=EJBase, specific=ast_CatchPart)
gen_ast_ConditionalLoop_LoopStatement = Generalization(general=LoopStatement, specific=ast_ConditionalLoop)
gen_ast_ContinueStatement_JumpStatement = Generalization(general=JumpStatement, specific=ast_ContinueStatement)
gen_ast_DoWhileStatement_ConditionalLoop = Generalization(general=ConditionalLoop, specific=ast_DoWhileStatement)
gen_ast_ExpressionStatement_MethodContentStatement = Generalization(general=MethodContentStatement, specific=ast_ExpressionStatement)
gen_ast_ForeachStatement_LoopStatement = Generalization(general=LoopStatement, specific=ast_ForeachStatement)
gen_ast_Label_EJElement = Generalization(general=EJElement, specific=ast_Label)
gen_ast_ForStatement_ConditionalLoop = Generalization(general=ConditionalLoop, specific=ast_ForStatement)
gen_ast_IfStatement_MethodContentStatement = Generalization(general=MethodContentStatement, specific=ast_IfStatement)
gen_ast_IfThenPart_EJBase = Generalization(general=EJBase, specific=ast_IfThenPart)
gen_ast_JumpStatement_MethodContentStatement = Generalization(general=MethodContentStatement, specific=ast_JumpStatement)
gen_ast_LabeledStatement_MethodContentStatement = Generalization(general=MethodContentStatement, specific=ast_LabeledStatement)
gen_ast_LocalVarStatement_MethodContentStatement = Generalization(general=MethodContentStatement, specific=ast_LocalVarStatement)
gen_ast_LoopStatement_LabeledStatement = Generalization(general=LabeledStatement, specific=ast_LoopStatement)
gen_ast_MethodBlock_MethodContentStatement = Generalization(general=MethodContentStatement, specific=ast_MethodBlock)
gen_ast_MethodClassifier_MethodContentStatement = Generalization(general=MethodContentStatement, specific=ast_MethodClassifier)
gen_ast_MethodContentStatement_EJBase = Generalization(general=EJBase, specific=ast_MethodContentStatement)
gen_ast_ScopeStatement_MethodContentStatement = Generalization(general=MethodContentStatement, specific=ast_ScopeStatement)
gen_ast_SwitchDefaultPart_SwitchPart = Generalization(general=SwitchPart, specific=ast_SwitchDefaultPart)
gen_ast_SwitchPart_EJBase = Generalization(general=EJBase, specific=ast_SwitchPart)
gen_ast_SwitchStatement_LabeledStatement = Generalization(general=LabeledStatement, specific=ast_SwitchStatement)
gen_ast_SynchronizedStatement_ScopeStatement = Generalization(general=ScopeStatement, specific=ast_SynchronizedStatement)
gen_ast_ThrowStatement_MethodContentStatement = Generalization(general=MethodContentStatement, specific=ast_ThrowStatement)
gen_ast_TryStatement_ScopeStatement = Generalization(general=ScopeStatement, specific=ast_TryStatement)
gen_ast_WhileStatement_ConditionalLoop = Generalization(general=ConditionalLoop, specific=ast_WhileStatement)
gen_ast_AccessOp_Expression = Generalization(general=Expression, specific=ast_AccessOp)
gen_ast_SwitchCasePart_SwitchPart = Generalization(general=SwitchPart, specific=ast_SwitchCasePart)
gen_ast_ApplySquareOp_Expression = Generalization(general=Expression, specific=ast_ApplySquareOp)
gen_ast_ArrayConstructor_Expression = Generalization(general=Expression, specific=ast_ArrayConstructor)
gen_ast_AssignmentOp_AssignmentOperation = Generalization(general=AssignmentOperation, specific=ast_AssignmentOp)
gen_ast_AssignmentOperation_Expression = Generalization(general=Expression, specific=ast_AssignmentOperation)
gen_ast_BinaryOp_Expression = Generalization(general=Expression, specific=ast_BinaryOp)
gen_ast_ApplyRoundOp_Expression = Generalization(general=Expression, specific=ast_ApplyRoundOp)
gen_ast_BitwiseAndOp_BinaryOp = Generalization(general=BinaryOp, specific=ast_BitwiseAndOp)
gen_ast_BitwiseComplementOp_UnaryOp = Generalization(general=UnaryOp, specific=ast_BitwiseComplementOp)
gen_ast_BitwiseOrAssignmentOp_AssignmentOperation = Generalization(general=AssignmentOperation, specific=ast_BitwiseOrAssignmentOp)
gen_ast_BitwiseOrOp_BinaryOp = Generalization(general=BinaryOp, specific=ast_BitwiseOrOp)
gen_ast_BitwiseXorAssignmentOp_AssignmentOperation = Generalization(general=AssignmentOperation, specific=ast_BitwiseXorAssignmentOp)
gen_ast_BitwiseXorOp_BinaryOp = Generalization(general=BinaryOp, specific=ast_BitwiseXorOp)
gen_ast_BooleanLiteral_Literal = Generalization(general=Literal, specific=ast_BooleanLiteral)
gen_ast_CastOp_ClassifierOp = Generalization(general=ClassifierOp, specific=ast_CastOp)
gen_ast_CharacterLiteral_Literal = Generalization(general=Literal, specific=ast_CharacterLiteral)
gen_ast_ClassifierOp_Expression = Generalization(general=Expression, specific=ast_ClassifierOp)
gen_ast_BitwiseAndAssignmentOp_AssignmentOperation = Generalization(general=AssignmentOperation, specific=ast_BitwiseAndAssignmentOp)
gen_ast_ConditionalAndOp_BinaryOp = Generalization(general=BinaryOp, specific=ast_ConditionalAndOp)
gen_ast_ConditionalOp_Expression = Generalization(general=Expression, specific=ast_ConditionalOp)
gen_ast_ConditionalOrOp_BinaryOp = Generalization(general=BinaryOp, specific=ast_ConditionalOrOp)
gen_ast_DivideAssignmentOp_AssignmentOperation = Generalization(general=AssignmentOperation, specific=ast_DivideAssignmentOp)
gen_ast_DivideOp_DivisionOp = Generalization(general=DivisionOp, specific=ast_DivideOp)
gen_ast_DivisionOp_Expression = Generalization(general=Expression, specific=ast_DivisionOp)
gen_ast_DoubleLiteral_Literal = Generalization(general=Literal, specific=ast_DoubleLiteral)
gen_ast_EqualOp_BinaryOp = Generalization(general=BinaryOp, specific=ast_EqualOp)
gen_ast_FloatLiteral_Literal = Generalization(general=Literal, specific=ast_FloatLiteral)
gen_ast_GreaterOrEqualOp_BinaryOp = Generalization(general=BinaryOp, specific=ast_GreaterOrEqualOp)
gen_ast_GreaterThenOp_BinaryOp = Generalization(general=BinaryOp, specific=ast_GreaterThenOp)
gen_ast_Identifier_Expression = Generalization(general=Expression, specific=ast_Identifier)
gen_ast_IdentityOp_Expression = Generalization(general=Expression, specific=ast_IdentityOp)
gen_ast_IntegerLiteral_Literal = Generalization(general=Literal, specific=ast_IntegerLiteral)
gen_ast_InstanceOfOp_ClassifierOp = Generalization(general=ClassifierOp, specific=ast_InstanceOfOp)
gen_ast_LeftShiftAssignmentOp_AssignmentOperation = Generalization(general=AssignmentOperation, specific=ast_LeftShiftAssignmentOp)
gen_ast_LeftShiftOp_ShiftOp = Generalization(general=ShiftOp, specific=ast_LeftShiftOp)
gen_ast_LessOrEqualOp_BinaryOp = Generalization(general=BinaryOp, specific=ast_LessOrEqualOp)
gen_ast_LessThenOp_BinaryOp = Generalization(general=BinaryOp, specific=ast_LessThenOp)
gen_ast_Literal_Expression = Generalization(general=Expression, specific=ast_Literal)
gen_ast_LogicalComplementOp_UnaryOp = Generalization(general=UnaryOp, specific=ast_LogicalComplementOp)
gen_ast_LongIntegerLiteral_Literal = Generalization(general=Literal, specific=ast_LongIntegerLiteral)
gen_ast_MinusAssignmentOp_AssignmentOperation = Generalization(general=AssignmentOperation, specific=ast_MinusAssignmentOp)
gen_ast_MinusOp_Expression = Generalization(general=Expression, specific=ast_MinusOp)
gen_ast_MultiplyOp_Expression = Generalization(general=Expression, specific=ast_MultiplyOp)
gen_ast_NotEqualOp_BinaryOp = Generalization(general=BinaryOp, specific=ast_NotEqualOp)
gen_ast_NullReference_Literal = Generalization(general=Literal, specific=ast_NullReference)
gen_ast_PlusAssignmentOp_AssignmentOperation = Generalization(general=AssignmentOperation, specific=ast_PlusAssignmentOp)
gen_ast_PlusOp_Expression = Generalization(general=Expression, specific=ast_PlusOp)
gen_ast_PostfixDecrementOp_UnaryOp = Generalization(general=UnaryOp, specific=ast_PostfixDecrementOp)
gen_ast_PostfixIncrementOp_UnaryOp = Generalization(general=UnaryOp, specific=ast_PostfixIncrementOp)
gen_ast_PrefixDecrementOp_UnaryOp = Generalization(general=UnaryOp, specific=ast_PrefixDecrementOp)
gen_ast_PrefixIncrementOp_UnaryOp = Generalization(general=UnaryOp, specific=ast_PrefixIncrementOp)
gen_ast_PrimitiveType_Expression = Generalization(general=Expression, specific=ast_PrimitiveType)
gen_ast_RemainderAssignmentOp_AssignmentOperation = Generalization(general=AssignmentOperation, specific=ast_RemainderAssignmentOp)
gen_ast_RemainderOp_DivisionOp = Generalization(general=DivisionOp, specific=ast_RemainderOp)
gen_ast_ReturnStatement_MethodContentStatement = Generalization(general=MethodContentStatement, specific=ast_ReturnStatement)
gen_ast_MultiplyAssignmentOp_AssignmentOperation = Generalization(general=AssignmentOperation, specific=ast_MultiplyAssignmentOp)
gen_ast_NewOp_Expression = Generalization(general=Expression, specific=ast_NewOp)
gen_ast_RightShiftOp_ShiftOp = Generalization(general=ShiftOp, specific=ast_RightShiftOp)
gen_ast_ShiftOp_Expression = Generalization(general=Expression, specific=ast_ShiftOp)
gen_ast_StringLiteral_Literal = Generalization(general=Literal, specific=ast_StringLiteral)
gen_ast_SuperReference_Expression = Generalization(general=Expression, specific=ast_SuperReference)
gen_ast_ThisReference_Expression = Generalization(general=Expression, specific=ast_ThisReference)
gen_ast_UnaryMinusOp_UnaryOp = Generalization(general=UnaryOp, specific=ast_UnaryMinusOp)
gen_ast_UnaryOp_Expression = Generalization(general=Expression, specific=ast_UnaryOp)
gen_ast_UnaryPlusOp_UnaryOp = Generalization(general=UnaryOp, specific=ast_UnaryPlusOp)
gen_ast_ZeroExtensionRightShiftAssignmentOp_AssignmentOperation = Generalization(general=AssignmentOperation, specific=ast_ZeroExtensionRightShiftAssignmentOp)
gen_ast_Expression_EJBase = Generalization(general=EJBase, specific=ast_Expression)
gen_ast_ZeroExtensionRightShiftOp_ShiftOp = Generalization(general=ShiftOp, specific=ast_ZeroExtensionRightShiftOp)
gen_ast_NamedElement_EJBase = Generalization(general=EJBase, specific=ast_NamedElement)
gen_ast_RightShiftAssignmentOp_AssignmentOperation = Generalization(general=AssignmentOperation, specific=ast_RightShiftAssignmentOp)
gen_ast_WildcardType_Expression = Generalization(general=Expression, specific=ast_WildcardType)
gen_ast_AssertStatement_MethodContentStatement = Generalization(general=MethodContentStatement, specific=ast_AssertStatement)
gen_ast_EmptyStatement_MethodContentStatement = Generalization(general=MethodContentStatement, specific=ast_EmptyStatement)
gen_ast_RangeExpression_Expression = Generalization(general=Expression, specific=ast_RangeExpression)
gen_ast_SwitchDefaultPartRef_EJElement = Generalization(general=EJElement, specific=ast_SwitchDefaultPartRef)
gen_ast_AttributeDefinition_ClassifierStatement = Generalization(general=ClassifierStatement, specific=ast_AttributeDefinition)

# Domain Model
domain_model = DomainModel(
    name="ast",
    types={ast_EJBase, EJElement, ast_DocumentationLine, ast_Expression, Feature, ast_AttributeSet, ast_Parameter, NamedElement, ast_Modifier, ast_Variable, ast_TemplateParameter, ast_EJElement, ast_BehaviorFeature, ast_Identifier, ast_ClassBlock, EJBase, ast_ClassifierMemberStatement, ast_ConstructorStatement, BehaviorFeature, ast_MethodBlock, ast_EnumLiteral, ClassifierMemberStatement, ast_Feature, ast_FieldStatement, ast_InitStatement, ast_InnerClassifier, ast_ClassifierStatement, ast_InstanceInitStatement, InitStatement, ast_MethodStatement, ast_StaticInitStatement, ast_ClassStatement, ImplemenationClassifierStatement, ast_EnumStatement, ast_ImplemenationClassifierStatement, ClassifierStatement, ast_InterfaceStatement, ast_ImportStatement, TopLevelStatement, ast_PackageStatement, ast_TopLevelClassifier, ast_TopLevelStatement, ast_BreakStatement, JumpStatement, ast_CatchPart, ast_ConditionalLoop, LoopStatement, ast_ContinueStatement, ast_SwitchDefaultPartRef, ast_DoWhileStatement, ConditionalLoop, ast_ExpressionStatement, MethodContentStatement, ast_ForeachStatement, ast_ForStatement, ast_LocalVarStatement, ast_IfStatement, ast_IfThenPart, ast_JumpStatement, ast_Label, ast_LabeledStatement, ast_LoopStatement, LabeledStatement, ast_MethodContentStatement, ast_MethodClassifier, ast_ScopeStatement, ast_SwitchDefaultPart, ast_SwitchPart, ast_SwitchStatement, ast_SynchronizedStatement, ScopeStatement, ast_ThrowStatement, ast_TryStatement, ast_WhileStatement, ast_AccessOp, Expression, ast_SwitchCasePart, SwitchPart, ast_ApplySquareOp, ast_ArrayConstructor, ast_AssignmentOp, AssignmentOperation, ast_AssignmentOperation, ast_BinaryOp, ast_ApplyRoundOp, ast_BitwiseAndOp, BinaryOp, ast_BitwiseComplementOp, UnaryOp, ast_BitwiseOrAssignmentOp, ast_BitwiseOrOp, ast_BitwiseXorAssignmentOp, ast_BitwiseXorOp, ast_BooleanLiteral, Literal, ast_CastOp, ClassifierOp, ast_CharacterLiteral, ast_ClassifierOp, ast_BitwiseAndAssignmentOp, ast_ConditionalAndOp, ast_ConditionalOp, ast_ConditionalOrOp, ast_DivideAssignmentOp, ast_DivideOp, DivisionOp, ast_DivisionOp, ast_DoubleLiteral, ast_EqualOp, ast_FloatLiteral, ast_GreaterOrEqualOp, ast_GreaterThenOp, ast_IdentityOp, ast_IntegerLiteral, ast_InstanceOfOp, ast_LeftShiftAssignmentOp, ast_LeftShiftOp, ShiftOp, ast_LessOrEqualOp, ast_LessThenOp, ast_Literal, ast_LogicalComplementOp, ast_LongIntegerLiteral, ast_MinusAssignmentOp, ast_MinusOp, ast_MultiplyOp, ast_NotEqualOp, ast_NullReference, ast_PlusAssignmentOp, ast_PlusOp, ast_PostfixDecrementOp, ast_PostfixIncrementOp, ast_PrefixDecrementOp, ast_PrefixIncrementOp, ast_PrimitiveType, ast_RemainderAssignmentOp, ast_RemainderOp, ast_ReturnStatement, ast_MultiplyAssignmentOp, ast_NewOp, ast_RightShiftOp, ast_ShiftOp, ast_StringLiteral, ast_SuperReference, ast_ThisReference, ast_UnaryMinusOp, ast_UnaryOp, ast_UnaryPlusOp, ast_ZeroExtensionRightShiftAssignmentOp, ast_ZeroExtensionRightShiftOp, ast_NamedElement, ast_RightShiftAssignmentOp, ast_WildcardType, ast_AssertStatement, ast_EmptyStatement, ast_RangeExpression, ast_AttributeDefinition},
    associations={documentation0, attributeSets1, attributes3, finalModifier5, classifier6, initialValue9, extendedTypes11, superToTypes13, exceptions16, name18, parameters20, templateParameters23, content26, body27, args28, name30, body33, visibilityModifier36, strictfpModifier72, staticModifier38, finalModifier41, transientModifier44, volatileModifier46, classifier49, variables52, body55, classifier57, body58, returnType60, abstractModifier63, synchronizedModifier66, nativeModifier69, name75, visibilityModifier78, templateParameters81, contents84, staticModifier87, extendedType89, implementedTypes92, strictfpModifier95, abstractModifier97, finalModifier100, extendedTypes103, staticModifier105, allModifier107, limit138, importedPackage110, name113, classifier115, specification117, body119, condition122, defaultLabel124, caseValue125, expression128, parameter130, collection132, initial135, initVariableDeclaration141, initExpressions142, updateExpressions145, ifThenPart148, elsePart149, condition152, body155, label158, label159, finalModifier161, variables164, classifier167, body170, content172, classifier174, values178, body180, value182, parts184, value187, exception189, finallyPart191, catchPart193, accessed196, feature198, body176, args203, functor206, args208, values211, leftHandSide213, value215, value1218, value2220, functor201, value223, condition228, thenPart230, elsePart233, dividend236, divisor238, classifier225, value241, minuend243, subtrahend245, multipliers248, classifier250, args252, classBody255, arrayConstructor258, summands261, value263, value265, distance267, value270, name272, superToTypes284, extendedTypes286, test274, message276, initial279, limit281},
    generalizations={gen_ast_EJBase_EJElement, gen_ast_BehaviorFeature_Feature, gen_ast_Parameter_NamedElement, gen_ast_Variable_NamedElement, gen_ast_TemplateParameter_NamedElement, gen_ast_Modifier_EJElement, gen_ast_DocumentationLine_EJElement, gen_ast_AttributeSet_EJElement, gen_ast_ClassBlock_EJBase, gen_ast_ClassifierMemberStatement_EJBase, gen_ast_ConstructorStatement_BehaviorFeature, gen_ast_EnumLiteral_ClassifierMemberStatement, gen_ast_Feature_ClassifierMemberStatement, gen_ast_FieldStatement_Feature, gen_ast_InitStatement_ClassifierMemberStatement, gen_ast_InnerClassifier_ClassifierMemberStatement, gen_ast_InstanceInitStatement_InitStatement, gen_ast_MethodStatement_BehaviorFeature, gen_ast_StaticInitStatement_InitStatement, gen_ast_ClassifierStatement_EJBase, gen_ast_ClassStatement_ImplemenationClassifierStatement, gen_ast_EnumStatement_ImplemenationClassifierStatement, gen_ast_ImplemenationClassifierStatement_ClassifierStatement, gen_ast_InterfaceStatement_ClassifierStatement, gen_ast_ImportStatement_TopLevelStatement, gen_ast_PackageStatement_TopLevelStatement, gen_ast_TopLevelClassifier_TopLevelStatement, gen_ast_TopLevelStatement_EJBase, gen_ast_BreakStatement_JumpStatement, gen_ast_CatchPart_EJBase, gen_ast_ConditionalLoop_LoopStatement, gen_ast_ContinueStatement_JumpStatement, gen_ast_DoWhileStatement_ConditionalLoop, gen_ast_ExpressionStatement_MethodContentStatement, gen_ast_ForeachStatement_LoopStatement, gen_ast_Label_EJElement, gen_ast_ForStatement_ConditionalLoop, gen_ast_IfStatement_MethodContentStatement, gen_ast_IfThenPart_EJBase, gen_ast_JumpStatement_MethodContentStatement, gen_ast_LabeledStatement_MethodContentStatement, gen_ast_LocalVarStatement_MethodContentStatement, gen_ast_LoopStatement_LabeledStatement, gen_ast_MethodBlock_MethodContentStatement, gen_ast_MethodClassifier_MethodContentStatement, gen_ast_MethodContentStatement_EJBase, gen_ast_ScopeStatement_MethodContentStatement, gen_ast_SwitchDefaultPart_SwitchPart, gen_ast_SwitchPart_EJBase, gen_ast_SwitchStatement_LabeledStatement, gen_ast_SynchronizedStatement_ScopeStatement, gen_ast_ThrowStatement_MethodContentStatement, gen_ast_TryStatement_ScopeStatement, gen_ast_WhileStatement_ConditionalLoop, gen_ast_AccessOp_Expression, gen_ast_SwitchCasePart_SwitchPart, gen_ast_ApplySquareOp_Expression, gen_ast_ArrayConstructor_Expression, gen_ast_AssignmentOp_AssignmentOperation, gen_ast_AssignmentOperation_Expression, gen_ast_BinaryOp_Expression, gen_ast_ApplyRoundOp_Expression, gen_ast_BitwiseAndOp_BinaryOp, gen_ast_BitwiseComplementOp_UnaryOp, gen_ast_BitwiseOrAssignmentOp_AssignmentOperation, gen_ast_BitwiseOrOp_BinaryOp, gen_ast_BitwiseXorAssignmentOp_AssignmentOperation, gen_ast_BitwiseXorOp_BinaryOp, gen_ast_BooleanLiteral_Literal, gen_ast_CastOp_ClassifierOp, gen_ast_CharacterLiteral_Literal, gen_ast_ClassifierOp_Expression, gen_ast_BitwiseAndAssignmentOp_AssignmentOperation, gen_ast_ConditionalAndOp_BinaryOp, gen_ast_ConditionalOp_Expression, gen_ast_ConditionalOrOp_BinaryOp, gen_ast_DivideAssignmentOp_AssignmentOperation, gen_ast_DivideOp_DivisionOp, gen_ast_DivisionOp_Expression, gen_ast_DoubleLiteral_Literal, gen_ast_EqualOp_BinaryOp, gen_ast_FloatLiteral_Literal, gen_ast_GreaterOrEqualOp_BinaryOp, gen_ast_GreaterThenOp_BinaryOp, gen_ast_Identifier_Expression, gen_ast_IdentityOp_Expression, gen_ast_IntegerLiteral_Literal, gen_ast_InstanceOfOp_ClassifierOp, gen_ast_LeftShiftAssignmentOp_AssignmentOperation, gen_ast_LeftShiftOp_ShiftOp, gen_ast_LessOrEqualOp_BinaryOp, gen_ast_LessThenOp_BinaryOp, gen_ast_Literal_Expression, gen_ast_LogicalComplementOp_UnaryOp, gen_ast_LongIntegerLiteral_Literal, gen_ast_MinusAssignmentOp_AssignmentOperation, gen_ast_MinusOp_Expression, gen_ast_MultiplyOp_Expression, gen_ast_NotEqualOp_BinaryOp, gen_ast_NullReference_Literal, gen_ast_PlusAssignmentOp_AssignmentOperation, gen_ast_PlusOp_Expression, gen_ast_PostfixDecrementOp_UnaryOp, gen_ast_PostfixIncrementOp_UnaryOp, gen_ast_PrefixDecrementOp_UnaryOp, gen_ast_PrefixIncrementOp_UnaryOp, gen_ast_PrimitiveType_Expression, gen_ast_RemainderAssignmentOp_AssignmentOperation, gen_ast_RemainderOp_DivisionOp, gen_ast_ReturnStatement_MethodContentStatement, gen_ast_MultiplyAssignmentOp_AssignmentOperation, gen_ast_NewOp_Expression, gen_ast_RightShiftOp_ShiftOp, gen_ast_ShiftOp_Expression, gen_ast_StringLiteral_Literal, gen_ast_SuperReference_Expression, gen_ast_ThisReference_Expression, gen_ast_UnaryMinusOp_UnaryOp, gen_ast_UnaryOp_Expression, gen_ast_UnaryPlusOp_UnaryOp, gen_ast_ZeroExtensionRightShiftAssignmentOp_AssignmentOperation, gen_ast_Expression_EJBase, gen_ast_ZeroExtensionRightShiftOp_ShiftOp, gen_ast_NamedElement_EJBase, gen_ast_RightShiftAssignmentOp_AssignmentOperation, gen_ast_WildcardType_Expression, gen_ast_AssertStatement_MethodContentStatement, gen_ast_EmptyStatement_MethodContentStatement, gen_ast_RangeExpression_Expression, gen_ast_SwitchDefaultPartRef_EJElement, gen_ast_AttributeDefinition_ClassifierStatement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)