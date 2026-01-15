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
ModifierKind: Enumeration = Enumeration(
    name="ModifierKind",
    literals={
            EnumerationLiteral(name="none"),
			EnumerationLiteral(name="static"),
			EnumerationLiteral(name="volatile"),
			EnumerationLiteral(name="register")
    }
)

UnaryOperatorKind: Enumeration = Enumeration(
    name="UnaryOperatorKind",
    literals={
            EnumerationLiteral(name="MINUS"),
			EnumerationLiteral(name="PLUS_PLUS"),
			EnumerationLiteral(name="MINUS_MINUS"),
			EnumerationLiteral(name="PLUS_EQUALS"),
			EnumerationLiteral(name="MINUS_EQUALS"),
			EnumerationLiteral(name="TIMES_EQUALS"),
			EnumerationLiteral(name="DIVIDED_BY_EQUALS")
    }
)

BinaryOperatorKind: Enumeration = Enumeration(
    name="BinaryOperatorKind",
    literals={
            EnumerationLiteral(name="PLUS"),
			EnumerationLiteral(name="MINUS"),
			EnumerationLiteral(name="TIMES"),
			EnumerationLiteral(name="DIVIDED_BY"),
			EnumerationLiteral(name="MODULE")
    }
)

DisplacementLogicOperatorKind: Enumeration = Enumeration(
    name="DisplacementLogicOperatorKind",
    literals={
            EnumerationLiteral(name="RIGHT_DISPLACEMENT"),
			EnumerationLiteral(name="LEFT_DISPLACEMENT")
    }
)

SimpleLogicOperatorKind: Enumeration = Enumeration(
    name="SimpleLogicOperatorKind",
    literals={
            EnumerationLiteral(name="AND"),
			EnumerationLiteral(name="OR"),
			EnumerationLiteral(name="XOR"),
			EnumerationLiteral(name="NOT")
    }
)

FunctionModifierKind: Enumeration = Enumeration(
    name="FunctionModifierKind",
    literals={
            EnumerationLiteral(name="none"),
			EnumerationLiteral(name="interrupt"),
			EnumerationLiteral(name="cdecl"),
			EnumerationLiteral(name="pascal")
    }
)

RelationalConectorKind: Enumeration = Enumeration(
    name="RelationalConectorKind",
    literals={
            EnumerationLiteral(name="none"),
			EnumerationLiteral(name="AND"),
			EnumerationLiteral(name="OR"),
			EnumerationLiteral(name="NOT")
    }
)

RelationalOperatorKind: Enumeration = Enumeration(
    name="RelationalOperatorKind",
    literals={
            EnumerationLiteral(name="LESS"),
			EnumerationLiteral(name="GREATER_EQUALS"),
			EnumerationLiteral(name="LESS_EQUALS"),
			EnumerationLiteral(name="NOT_EQUALS"),
			EnumerationLiteral(name="EQUALS"),
			EnumerationLiteral(name="none"),
			EnumerationLiteral(name="GREATER")
    }
)

# Classes
C_Types_Type = Class(name="C::Types::Type", is_abstract=True)
C_Types_Char = Class(name="C::Types::Char")
PrimitiveType = Class(name="PrimitiveType")
C_Types_Int = Class(name="C::Types::Int")
Types_PrimitiveType = Class(name="Types::PrimitiveType")
Types_Array = Class(name="Types::Array")
C_Types_Float = Class(name="C::Types::Float")
C_Types_Double = Class(name="C::Types::Double")
C_Types_Short = Class(name="C::Types::Short")
C_Types_Void = Class(name="C::Types::Void")
C_Types_Typedef = Class(name="C::Types::Typedef")
CompositeType = Class(name="CompositeType")
C_Types_Array = Class(name="C::Types::Array")
C_Types_Struct = Class(name="C::Types::Struct")
C_Types_PrimitiveType = Class(name="C::Types::PrimitiveType", is_abstract=True)
Type = Class(name="Type")
C_Types_CompositeType = Class(name="C::Types::CompositeType", is_abstract=True)
C_Types_Enum = Class(name="C::Types::Enum")
C_Types_FromHeader = Class(name="C::Types::FromHeader")
Types_Type = Class(name="Types::Type")
Abstractions_NamedElement = Class(name="Abstractions::NamedElement")
C_Abstractions_NamedElement = Class(name="C::Abstractions::NamedElement", is_abstract=True)
C_Abstractions_BlockedElement = Class(name="C::Abstractions::BlockedElement", is_abstract=True)
Main_Block = Class(name="Main::Block")
Main_Unit = Class(name="Main::Unit")
C_Main_Unit = Class(name="C::Main::Unit", is_abstract=True)
NamedElement = Class(name="NamedElement")
Main_Comment = Class(name="Main::Comment")
C_Main_C_Unit = Class(name="C::Main::C::Unit")
Unit = Class(name="Unit")
Main_Element = Class(name="Main::Element")
C_Main_Program = Class(name="C::Main::Program")
C_Main_Function = Class(name="C::Main::Function")
Element = Class(name="Element")
Declarations_Declaration = Class(name="Declarations::Declaration")
C_Main_H_Unit = Class(name="C::Main::H::Unit")
Main_DeclarationsBlock = Class(name="Main::DeclarationsBlock")
Abstractions_BlockedElement = Class(name="Abstractions::BlockedElement")
C_Main_Block = Class(name="C::Main::Block")
C_Main_Comment = Class(name="C::Main::Comment")
C_Main_Element = Class(name="C::Main::Element")
C_Main_DeclarationsBlock = Class(name="C::Main::DeclarationsBlock")
CompilationDirectiveDeclarations_CompilationDirectiveDeclaration = Class(name="CompilationDirectiveDeclarations::CompilationDirectiveDeclaration")
C_Main_FunctionsBlock = Class(name="C::Main::FunctionsBlock")
Main_Function = Class(name="Main::Function")
C_Declarations_Declaration = Class(name="C::Declarations::Declaration", is_abstract=True)
C_Declarations_ConstantDeclaration = Class(name="C::Declarations::ConstantDeclaration")
Declaration = Class(name="Declaration")
Expressions_Expression = Class(name="Expressions::Expression")
C_Declarations_SimpleVariableDeclaration = Class(name="C::Declarations::SimpleVariableDeclaration")
Declarations_VariableDeclaration = Class(name="Declarations::VariableDeclaration")
Declarations_FragmentVariableDeclaration = Class(name="Declarations::FragmentVariableDeclaration")
C_Declarations_PrototypeFunctionDeclaration = Class(name="C::Declarations::PrototypeFunctionDeclaration")
C_Declarations_VariableDeclaration = Class(name="C::Declarations::VariableDeclaration")
C_Declarations_FragmentVariableDeclaration = Class(name="C::Declarations::FragmentVariableDeclaration")
C_Declarations_CompositeVariableDeclaration = Class(name="C::Declarations::CompositeVariableDeclaration", is_abstract=True)
VariableDeclaration = Class(name="VariableDeclaration")
C_Declarations_EnumDeclaration = Class(name="C::Declarations::EnumDeclaration")
CompositeVariableDeclaration = Class(name="CompositeVariableDeclaration")
Expressions_Literal = Class(name="Expressions::Literal")
Declarations_CompositeVariableDeclaration = Class(name="Declarations::CompositeVariableDeclaration")
Expressions_Construction = Class(name="Expressions::Construction")
C_Declarations_StructDeclaration = Class(name="C::Declarations::StructDeclaration")
Declarations_SimpleVariableDeclaration = Class(name="Declarations::SimpleVariableDeclaration")
C_Declarations_TypeDefDeclaration = Class(name="C::Declarations::TypeDefDeclaration")
C_Declarations_ArrayDeclaration = Class(name="C::Declarations::ArrayDeclaration")
C_CompilationDirectiveDeclarations_SimpleDirectiveDeclaration = Class(name="C::CompilationDirectiveDeclarations::SimpleDirectiveDeclaration", is_abstract=True)
C_CompilationDirectiveDeclarations_ComplexDirectiveDeclaration = Class(name="C::CompilationDirectiveDeclarations::ComplexDirectiveDeclaration", is_abstract=True)
CompilationDirectiveDeclaration = Class(name="CompilationDirectiveDeclaration")
C_CompilationDirectiveDeclarations_Define = Class(name="C::CompilationDirectiveDeclarations::Define")
SimpleDirectiveDeclaration = Class(name="SimpleDirectiveDeclaration")
C_CompilationDirectiveDeclarations_Include = Class(name="C::CompilationDirectiveDeclarations::Include")
C_CompilationDirectiveDeclarations_Ifdef = Class(name="C::CompilationDirectiveDeclarations::Ifdef")
CompilationDirectiveDeclarations_ComplexDirectiveDeclaration = Class(name="CompilationDirectiveDeclarations::ComplexDirectiveDeclaration")
CompilationDirectiveDeclarations_Endif = Class(name="CompilationDirectiveDeclarations::Endif")
C_CompilationDirectiveDeclarations_Ifndef = Class(name="C::CompilationDirectiveDeclarations::Ifndef")
ComplexDirectiveDeclaration = Class(name="ComplexDirectiveDeclaration")
C_CompilationDirectiveDeclarations_CompilationDirectiveDeclaration = Class(name="C::CompilationDirectiveDeclarations::CompilationDirectiveDeclaration", is_abstract=True)
C_CompilationDirectiveDeclarations_IfDirective = Class(name="C::CompilationDirectiveDeclarations::IfDirective")
Expressions_ConstantExpression = Class(name="Expressions::ConstantExpression")
C_CompilationDirectiveDeclarations_Elif = Class(name="C::CompilationDirectiveDeclarations::Elif")
IfDirective = Class(name="IfDirective")
C_CompilationDirectiveDeclarations_Endif = Class(name="C::CompilationDirectiveDeclarations::Endif")
C_Commands_Command = Class(name="C::Commands::Command", is_abstract=True)
BlockedElement = Class(name="BlockedElement")
C_Commands_LabelCommand = Class(name="C::Commands::LabelCommand")
Commands_Command = Class(name="Commands::Command")
C_CompilationDirectiveDeclarations_ElseDirective = Class(name="C::CompilationDirectiveDeclarations::ElseDirective")
C_Commands_FlowControlCommand = Class(name="C::Commands::FlowControlCommand", is_abstract=True)
C_Commands_DecisionCommand = Class(name="C::Commands::DecisionCommand")
FlowControlCommand = Class(name="FlowControlCommand")
C_Commands_ReturnCommand = Class(name="C::Commands::ReturnCommand")
C_Commands_ExpressionCommand = Class(name="C::Commands::ExpressionCommand")
C_Commands_IfCommand = Class(name="C::Commands::IfCommand")
DecisionCommand = Class(name="DecisionCommand")
Expressions_ConditionalExpression = Class(name="Expressions::ConditionalExpression")
C_Commands_Assignment = Class(name="C::Commands::Assignment")
Command = Class(name="Command")
Expressions_Access = Class(name="Expressions::Access")
C_Commands_SwitchCommand = Class(name="C::Commands::SwitchCommand")
Expressions_VariableAccess = Class(name="Expressions::VariableAccess")
Commands_CaseOption = Class(name="Commands::CaseOption")
Commands_DefaultOption = Class(name="Commands::DefaultOption")
C_Commands_DefaultOption = Class(name="C::Commands::DefaultOption")
C_Commands_IterativeCommand = Class(name="C::Commands::IterativeCommand", is_abstract=True)
C_Commands_ForCommand = Class(name="C::Commands::ForCommand")
IterativeCommand = Class(name="IterativeCommand")
C_Commands_CaseOption = Class(name="C::Commands::CaseOption")
C_Commands_WhileCommand = Class(name="C::Commands::WhileCommand")
C_Expressions_Expression = Class(name="C::Expressions::Expression", is_abstract=True)
C_Expressions_Construction = Class(name="C::Expressions::Construction")
Expression = Class(name="Expression")
C_Expressions_FunctionCall = Class(name="C::Expressions::FunctionCall")
C_Expressions_ArithmeticExpression = Class(name="C::Expressions::ArithmeticExpression", is_abstract=True)
C_Expressions_UnaryArithmeticExpression = Class(name="C::Expressions::UnaryArithmeticExpression")
ArithmeticExpression = Class(name="ArithmeticExpression")
C_Expressions_BinaryArithmeticExpression = Class(name="C::Expressions::BinaryArithmeticExpression")
C_Expressions_CastExpression = Class(name="C::Expressions::CastExpression")
C_Expressions_AtomicConditionalExpression = Class(name="C::Expressions::AtomicConditionalExpression")
C_Expressions_ComposedConditionalExpression = Class(name="C::Expressions::ComposedConditionalExpression")
ConditionalExpression = Class(name="ConditionalExpression")
C_Expressions_LogicExpression = Class(name="C::Expressions::LogicExpression", is_abstract=True)
C_Expressions_DisplacementLogicExpression = Class(name="C::Expressions::DisplacementLogicExpression")
LogicExpression = Class(name="LogicExpression")
C_Expressions_ConditionalExpression = Class(name="C::Expressions::ConditionalExpression", is_abstract=True)
C_Expressions_SimpleLogicExpression = Class(name="C::Expressions::SimpleLogicExpression")
C_Expressions_Access = Class(name="C::Expressions::Access", is_abstract=True)
C_Expressions_ConstantAccess = Class(name="C::Expressions::ConstantAccess")
Access = Class(name="Access")
Declarations_ConstantDeclaration = Class(name="Declarations::ConstantDeclaration")
C_Expressions_VariableAccess = Class(name="C::Expressions::VariableAccess")
C_Expressions_PointerVariableAccess = Class(name="C::Expressions::PointerVariableAccess")
VariableAccess = Class(name="VariableAccess")
C_Expressions_PrototypeAccess = Class(name="C::Expressions::PrototypeAccess")
Declarations_PrototypeFunctionDeclaration = Class(name="Declarations::PrototypeFunctionDeclaration")
C_Expressions_Literal = Class(name="C::Expressions::Literal", is_abstract=True)
C_Expressions_CharLiteral = Class(name="C::Expressions::CharLiteral")
Literal = Class(name="Literal")
C_Expressions_ArrayAccess = Class(name="C::Expressions::ArrayAccess")
Declarations_ArrayDeclaration = Class(name="Declarations::ArrayDeclaration")
C_Expressions_DoubleLiteral = Class(name="C::Expressions::DoubleLiteral")
C_Expressions_StringLiteral = Class(name="C::Expressions::StringLiteral")
C_Expressions_ShortLiteral = Class(name="C::Expressions::ShortLiteral")
C_Expressions_ConstantExpression = Class(name="C::Expressions::ConstantExpression")
C_Sequencers_Sequencer = Class(name="C::Sequencers::Sequencer", is_abstract=True)
C_Sequencers_Goto = Class(name="C::Sequencers::Goto")
Sequencer = Class(name="Sequencer")
C_Expressions_IntLiteral = Class(name="C::Expressions::IntLiteral")
C_Expressions_FloatLiteral = Class(name="C::Expressions::FloatLiteral")
C_Sequencers_Break = Class(name="C::Sequencers::Break")
Commands_LabelCommand = Class(name="Commands::LabelCommand")

# C_Types_Type class attributes and methods

# C_Types_Char class attributes and methods

# PrimitiveType class attributes and methods

# C_Types_Int class attributes and methods

# Types_PrimitiveType class attributes and methods

# Types_Array class attributes and methods

# C_Types_Float class attributes and methods

# C_Types_Double class attributes and methods

# C_Types_Short class attributes and methods

# C_Types_Void class attributes and methods

# C_Types_Typedef class attributes and methods

# CompositeType class attributes and methods

# C_Types_Array class attributes and methods

# C_Types_Struct class attributes and methods

# C_Types_PrimitiveType class attributes and methods

# Type class attributes and methods

# C_Types_CompositeType class attributes and methods

# C_Types_Enum class attributes and methods

# C_Types_FromHeader class attributes and methods

# Types_Type class attributes and methods

# Abstractions_NamedElement class attributes and methods

# C_Abstractions_NamedElement class attributes and methods
C_Abstractions_NamedElement_name: Property = Property(name="name", type=StringType)
C_Abstractions_NamedElement.attributes={C_Abstractions_NamedElement_name}

# C_Abstractions_BlockedElement class attributes and methods

# Main_Block class attributes and methods

# Main_Unit class attributes and methods

# C_Main_Unit class attributes and methods

# NamedElement class attributes and methods

# Main_Comment class attributes and methods

# C_Main_C_Unit class attributes and methods

# Unit class attributes and methods

# Main_Element class attributes and methods

# C_Main_Program class attributes and methods
C_Main_Program_description: Property = Property(name="description", type=StringType)
C_Main_Program.attributes={C_Main_Program_description}

# C_Main_Function class attributes and methods
C_Main_Function_modifier: Property = Property(name="modifier", type=StringType)
C_Main_Function_functionModifier: Property = Property(name="functionModifier", type=StringType)
C_Main_Function.attributes={C_Main_Function_functionModifier, C_Main_Function_modifier}

# Element class attributes and methods

# Declarations_Declaration class attributes and methods

# C_Main_H_Unit class attributes and methods

# Main_DeclarationsBlock class attributes and methods

# Abstractions_BlockedElement class attributes and methods

# C_Main_Block class attributes and methods

# C_Main_Comment class attributes and methods

# C_Main_Element class attributes and methods

# C_Main_DeclarationsBlock class attributes and methods

# CompilationDirectiveDeclarations_CompilationDirectiveDeclaration class attributes and methods

# C_Main_FunctionsBlock class attributes and methods

# Main_Function class attributes and methods

# C_Declarations_Declaration class attributes and methods
C_Declarations_Declaration_modifier: Property = Property(name="modifier", type=StringType)
C_Declarations_Declaration.attributes={C_Declarations_Declaration_modifier}

# C_Declarations_ConstantDeclaration class attributes and methods

# Declaration class attributes and methods

# Expressions_Expression class attributes and methods

# C_Declarations_SimpleVariableDeclaration class attributes and methods

# Declarations_VariableDeclaration class attributes and methods

# Declarations_FragmentVariableDeclaration class attributes and methods

# C_Declarations_PrototypeFunctionDeclaration class attributes and methods
C_Declarations_PrototypeFunctionDeclaration_isAPointer: Property = Property(name="isAPointer", type=StringType)
C_Declarations_PrototypeFunctionDeclaration_functionModifier: Property = Property(name="functionModifier", type=StringType)
C_Declarations_PrototypeFunctionDeclaration.attributes={C_Declarations_PrototypeFunctionDeclaration_functionModifier, C_Declarations_PrototypeFunctionDeclaration_isAPointer}

# C_Declarations_VariableDeclaration class attributes and methods
C_Declarations_VariableDeclaration_isAPointer: Property = Property(name="isAPointer", type=StringType)
C_Declarations_VariableDeclaration_numberOfPointers: Property = Property(name="numberOfPointers", type=StringType)
C_Declarations_VariableDeclaration.attributes={C_Declarations_VariableDeclaration_numberOfPointers, C_Declarations_VariableDeclaration_isAPointer}

# C_Declarations_FragmentVariableDeclaration class attributes and methods

# C_Declarations_CompositeVariableDeclaration class attributes and methods

# VariableDeclaration class attributes and methods

# C_Declarations_EnumDeclaration class attributes and methods

# CompositeVariableDeclaration class attributes and methods

# Expressions_Literal class attributes and methods

# Declarations_CompositeVariableDeclaration class attributes and methods

# Expressions_Construction class attributes and methods

# C_Declarations_StructDeclaration class attributes and methods

# Declarations_SimpleVariableDeclaration class attributes and methods

# C_Declarations_TypeDefDeclaration class attributes and methods

# C_Declarations_ArrayDeclaration class attributes and methods
C_Declarations_ArrayDeclaration_dimensions: Property = Property(name="dimensions", type=StringType)
C_Declarations_ArrayDeclaration.attributes={C_Declarations_ArrayDeclaration_dimensions}

# C_CompilationDirectiveDeclarations_SimpleDirectiveDeclaration class attributes and methods

# C_CompilationDirectiveDeclarations_ComplexDirectiveDeclaration class attributes and methods

# CompilationDirectiveDeclaration class attributes and methods

# C_CompilationDirectiveDeclarations_Define class attributes and methods
C_CompilationDirectiveDeclarations_Define_value: Property = Property(name="value", type=StringType)
C_CompilationDirectiveDeclarations_Define.attributes={C_CompilationDirectiveDeclarations_Define_value}

# SimpleDirectiveDeclaration class attributes and methods

# C_CompilationDirectiveDeclarations_Include class attributes and methods

# C_CompilationDirectiveDeclarations_Ifdef class attributes and methods

# CompilationDirectiveDeclarations_ComplexDirectiveDeclaration class attributes and methods

# CompilationDirectiveDeclarations_Endif class attributes and methods

# C_CompilationDirectiveDeclarations_Ifndef class attributes and methods

# ComplexDirectiveDeclaration class attributes and methods

# C_CompilationDirectiveDeclarations_CompilationDirectiveDeclaration class attributes and methods

# C_CompilationDirectiveDeclarations_IfDirective class attributes and methods

# Expressions_ConstantExpression class attributes and methods

# C_CompilationDirectiveDeclarations_Elif class attributes and methods

# IfDirective class attributes and methods

# C_CompilationDirectiveDeclarations_Endif class attributes and methods

# C_Commands_Command class attributes and methods

# BlockedElement class attributes and methods

# C_Commands_LabelCommand class attributes and methods

# Commands_Command class attributes and methods

# C_CompilationDirectiveDeclarations_ElseDirective class attributes and methods

# C_Commands_FlowControlCommand class attributes and methods

# C_Commands_DecisionCommand class attributes and methods

# FlowControlCommand class attributes and methods

# C_Commands_ReturnCommand class attributes and methods

# C_Commands_ExpressionCommand class attributes and methods

# C_Commands_IfCommand class attributes and methods

# DecisionCommand class attributes and methods

# Expressions_ConditionalExpression class attributes and methods

# C_Commands_Assignment class attributes and methods

# Command class attributes and methods

# Expressions_Access class attributes and methods

# C_Commands_SwitchCommand class attributes and methods

# Expressions_VariableAccess class attributes and methods

# Commands_CaseOption class attributes and methods

# Commands_DefaultOption class attributes and methods

# C_Commands_DefaultOption class attributes and methods

# C_Commands_IterativeCommand class attributes and methods

# C_Commands_ForCommand class attributes and methods

# IterativeCommand class attributes and methods

# C_Commands_CaseOption class attributes and methods

# C_Commands_WhileCommand class attributes and methods

# C_Expressions_Expression class attributes and methods

# C_Expressions_Construction class attributes and methods

# Expression class attributes and methods

# C_Expressions_FunctionCall class attributes and methods

# C_Expressions_ArithmeticExpression class attributes and methods

# C_Expressions_UnaryArithmeticExpression class attributes and methods
C_Expressions_UnaryArithmeticExpression_operator: Property = Property(name="operator", type=StringType)
C_Expressions_UnaryArithmeticExpression.attributes={C_Expressions_UnaryArithmeticExpression_operator}

# ArithmeticExpression class attributes and methods

# C_Expressions_BinaryArithmeticExpression class attributes and methods
C_Expressions_BinaryArithmeticExpression_operator: Property = Property(name="operator", type=StringType)
C_Expressions_BinaryArithmeticExpression.attributes={C_Expressions_BinaryArithmeticExpression_operator}

# C_Expressions_CastExpression class attributes and methods

# C_Expressions_AtomicConditionalExpression class attributes and methods

# C_Expressions_ComposedConditionalExpression class attributes and methods
C_Expressions_ComposedConditionalExpression_operator: Property = Property(name="operator", type=StringType)
C_Expressions_ComposedConditionalExpression.attributes={C_Expressions_ComposedConditionalExpression_operator}

# ConditionalExpression class attributes and methods

# C_Expressions_LogicExpression class attributes and methods

# C_Expressions_DisplacementLogicExpression class attributes and methods
C_Expressions_DisplacementLogicExpression_operator: Property = Property(name="operator", type=StringType)
C_Expressions_DisplacementLogicExpression.attributes={C_Expressions_DisplacementLogicExpression_operator}

# LogicExpression class attributes and methods

# C_Expressions_ConditionalExpression class attributes and methods
C_Expressions_ConditionalExpression_conector: Property = Property(name="conector", type=StringType)
C_Expressions_ConditionalExpression.attributes={C_Expressions_ConditionalExpression_conector}

# C_Expressions_SimpleLogicExpression class attributes and methods
C_Expressions_SimpleLogicExpression_operator: Property = Property(name="operator", type=StringType)
C_Expressions_SimpleLogicExpression.attributes={C_Expressions_SimpleLogicExpression_operator}

# C_Expressions_Access class attributes and methods

# C_Expressions_ConstantAccess class attributes and methods

# Access class attributes and methods

# Declarations_ConstantDeclaration class attributes and methods

# C_Expressions_VariableAccess class attributes and methods

# C_Expressions_PointerVariableAccess class attributes and methods

# VariableAccess class attributes and methods

# C_Expressions_PrototypeAccess class attributes and methods

# Declarations_PrototypeFunctionDeclaration class attributes and methods

# C_Expressions_Literal class attributes and methods

# C_Expressions_CharLiteral class attributes and methods
C_Expressions_CharLiteral_value: Property = Property(name="value", type=StringType)
C_Expressions_CharLiteral.attributes={C_Expressions_CharLiteral_value}

# Literal class attributes and methods

# C_Expressions_ArrayAccess class attributes and methods

# Declarations_ArrayDeclaration class attributes and methods

# C_Expressions_DoubleLiteral class attributes and methods
C_Expressions_DoubleLiteral_value: Property = Property(name="value", type=FloatType)
C_Expressions_DoubleLiteral.attributes={C_Expressions_DoubleLiteral_value}

# C_Expressions_StringLiteral class attributes and methods
C_Expressions_StringLiteral_value: Property = Property(name="value", type=StringType)
C_Expressions_StringLiteral.attributes={C_Expressions_StringLiteral_value}

# C_Expressions_ShortLiteral class attributes and methods
C_Expressions_ShortLiteral_value: Property = Property(name="value", type=IntegerType)
C_Expressions_ShortLiteral.attributes={C_Expressions_ShortLiteral_value}

# C_Expressions_ConstantExpression class attributes and methods

# C_Sequencers_Sequencer class attributes and methods

# C_Sequencers_Goto class attributes and methods

# Sequencer class attributes and methods

# C_Expressions_IntLiteral class attributes and methods
C_Expressions_IntLiteral_value: Property = Property(name="value", type=StringType)
C_Expressions_IntLiteral.attributes={C_Expressions_IntLiteral_value}

# C_Expressions_FloatLiteral class attributes and methods
C_Expressions_FloatLiteral_value: Property = Property(name="value", type=FloatType)
C_Expressions_FloatLiteral.attributes={C_Expressions_FloatLiteral_value}

# C_Sequencers_Break class attributes and methods

# Commands_LabelCommand class attributes and methods

# Relationships
file1: BinaryAssociation = BinaryAssociation(
    name="file1",
    ends={
        Property(name="Main_Unit", type=C_Main_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="C_Main_Program", type=Main_Unit, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
comment2: BinaryAssociation = BinaryAssociation(
    name="comment2",
    ends={
        Property(name="Main_Comment", type=C_Main_Unit, multiplicity=Multiplicity(1, 1)),
        Property(name="C_Main_Unit", type=Main_Comment, multiplicity=Multiplicity(0, 9999))
    }
)
elements3: BinaryAssociation = BinaryAssociation(
    name="elements3",
    ends={
        Property(name="Main_Element", type=C_Main_C_Unit, multiplicity=Multiplicity(1, 1)),
        Property(name="C_Main_C_Unit", type=Main_Element, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
element0: BinaryAssociation = BinaryAssociation(
    name="element0",
    ends={
        Property(name="Main_Block", type=C_Abstractions_BlockedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="C_Abstractions_BlockedElement", type=Main_Block, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
declaration4: BinaryAssociation = BinaryAssociation(
    name="declaration4",
    ends={
        Property(name="C_Main_H_Unit", type=Main_DeclarationsBlock, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="Main_DeclarationsBlock", type=C_Main_H_Unit, multiplicity=Multiplicity(1, 1))
    }
)
return5: BinaryAssociation = BinaryAssociation(
    name="return5",
    ends={
        Property(name="Types_Type", type=C_Main_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="C_Main_Function", type=Types_Type, multiplicity=Multiplicity(0, 1))
    }
)
body6: BinaryAssociation = BinaryAssociation(
    name="body6",
    ends={
        Property(name="Main_Block8", type=C_Main_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="C_Main_Function7", type=Main_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedParameter9: BinaryAssociation = BinaryAssociation(
    name="ownedParameter9",
    ends={
        Property(name="Declarations_Declaration", type=C_Main_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="C_Main_Function10", type=Declarations_Declaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
element11: BinaryAssociation = BinaryAssociation(
    name="element11",
    ends={
        Property(name="Abstractions_BlockedElement", type=C_Main_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="C_Main_Block", type=Abstractions_BlockedElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
comment12: BinaryAssociation = BinaryAssociation(
    name="comment12",
    ends={
        Property(name="Main_Comment14", type=C_Main_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="C_Main_Block13", type=Main_Comment, multiplicity=Multiplicity(0, 9999))
    }
)
directive17: BinaryAssociation = BinaryAssociation(
    name="directive17",
    ends={
        Property(name="CompilationDirectiveDeclarations_CompilationDirectiveDeclaration", type=C_Main_DeclarationsBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="C_Main_DeclarationsBlock18", type=CompilationDirectiveDeclarations_CompilationDirectiveDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
declaration15: BinaryAssociation = BinaryAssociation(
    name="declaration15",
    ends={
        Property(name="Declarations_Declaration16", type=C_Main_DeclarationsBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="C_Main_DeclarationsBlock", type=Declarations_Declaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
function19: BinaryAssociation = BinaryAssociation(
    name="function19",
    ends={
        Property(name="Main_Function", type=C_Main_FunctionsBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="C_Main_FunctionsBlock", type=Main_Function, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initializer20: BinaryAssociation = BinaryAssociation(
    name="initializer20",
    ends={
        Property(name="Expressions_Expression", type=C_Declarations_ConstantDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="C_Declarations_ConstantDeclaration", type=Expressions_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type21: BinaryAssociation = BinaryAssociation(
    name="type21",
    ends={
        Property(name="Types_Type22", type=C_Declarations_SimpleVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="C_Declarations_SimpleVariableDeclaration", type=Types_Type, multiplicity=Multiplicity(0, 1))
    }
)
fragment23: BinaryAssociation = BinaryAssociation(
    name="fragment23",
    ends={
        Property(name="Declarations_FragmentVariableDeclaration", type=C_Declarations_SimpleVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="C_Declarations_SimpleVariableDeclaration24", type=Declarations_FragmentVariableDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initializer25: BinaryAssociation = BinaryAssociation(
    name="initializer25",
    ends={
        Property(name="Expressions_Expression27", type=C_Declarations_SimpleVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="C_Declarations_SimpleVariableDeclaration26", type=Expressions_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedParameter28: BinaryAssociation = BinaryAssociation(
    name="ownedParameter28",
    ends={
        Property(name="Declarations_VariableDeclaration", type=C_Declarations_PrototypeFunctionDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="C_Declarations_PrototypeFunctionDeclaration", type=Declarations_VariableDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type29: BinaryAssociation = BinaryAssociation(
    name="type29",
    ends={
        Property(name="C_Declarations_PrototypeFunctionDeclaration30", type=Types_Type, multiplicity=Multiplicity(0, 1)),
        Property(name="Types_Type31", type=C_Declarations_PrototypeFunctionDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
literal32: BinaryAssociation = BinaryAssociation(
    name="literal32",
    ends={
        Property(name="Expressions_Literal", type=C_Declarations_EnumDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="C_Declarations_EnumDeclaration", type=Expressions_Literal, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inicializer33: BinaryAssociation = BinaryAssociation(
    name="inicializer33",
    ends={
        Property(name="Expressions_Construction", type=C_Declarations_ArrayDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="C_Declarations_ArrayDeclaration", type=Expressions_Construction, multiplicity=Multiplicity(0, 1))
    }
)
elementType34: BinaryAssociation = BinaryAssociation(
    name="elementType34",
    ends={
        Property(name="Types_Type36", type=C_Declarations_ArrayDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="C_Declarations_ArrayDeclaration35", type=Types_Type, multiplicity=Multiplicity(0, 1))
    }
)
element37: BinaryAssociation = BinaryAssociation(
    name="element37",
    ends={
        Property(name="Declarations_SimpleVariableDeclaration", type=C_Declarations_StructDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="C_Declarations_StructDeclaration", type=Declarations_SimpleVariableDeclaration, multiplicity=Multiplicity(0, 9999))
    }
)
type38: BinaryAssociation = BinaryAssociation(
    name="type38",
    ends={
        Property(name="Types_Type39", type=C_Declarations_TypeDefDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="C_Declarations_TypeDefDeclaration", type=Types_Type, multiplicity=Multiplicity(0, 1))
    }
)
declaration40: BinaryAssociation = BinaryAssociation(
    name="declaration40",
    ends={
        Property(name="C_CompilationDirectiveDeclarations_CompilationDirectiveDeclaration", type=Declarations_Declaration, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="Declarations_Declaration41", type=C_CompilationDirectiveDeclarations_CompilationDirectiveDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
end42: BinaryAssociation = BinaryAssociation(
    name="end42",
    ends={
        Property(name="CompilationDirectiveDeclarations_Endif", type=C_CompilationDirectiveDeclarations_Ifdef, multiplicity=Multiplicity(1, 1)),
        Property(name="C_CompilationDirectiveDeclarations_Ifdef", type=CompilationDirectiveDeclarations_Endif, multiplicity=Multiplicity(0, 1))
    }
)
expression45: BinaryAssociation = BinaryAssociation(
    name="expression45",
    ends={
        Property(name="Expressions_ConstantExpression", type=C_CompilationDirectiveDeclarations_IfDirective, multiplicity=Multiplicity(1, 1)),
        Property(name="C_CompilationDirectiveDeclarations_IfDirective", type=Expressions_ConstantExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
refersTo46: BinaryAssociation = BinaryAssociation(
    name="refersTo46",
    ends={
        Property(name="Commands_Command", type=C_Commands_LabelCommand, multiplicity=Multiplicity(1, 1)),
        Property(name="C_Commands_LabelCommand", type=Commands_Command, multiplicity=Multiplicity(0, 1))
    }
)
end43: BinaryAssociation = BinaryAssociation(
    name="end43",
    ends={
        Property(name="CompilationDirectiveDeclarations_Endif44", type=C_CompilationDirectiveDeclarations_Ifndef, multiplicity=Multiplicity(1, 1)),
        Property(name="C_CompilationDirectiveDeclarations_Ifndef", type=CompilationDirectiveDeclarations_Endif, multiplicity=Multiplicity(0, 1))
    }
)
expression48: BinaryAssociation = BinaryAssociation(
    name="expression48",
    ends={
        Property(name="Expressions_Expression50", type=C_Commands_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="C_Commands_Assignment49", type=Expressions_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression51: BinaryAssociation = BinaryAssociation(
    name="expression51",
    ends={
        Property(name="Expressions_Expression52", type=C_Commands_ReturnCommand, multiplicity=Multiplicity(1, 1)),
        Property(name="C_Commands_ReturnCommand", type=Expressions_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression53: BinaryAssociation = BinaryAssociation(
    name="expression53",
    ends={
        Property(name="Expressions_Expression54", type=C_Commands_ExpressionCommand, multiplicity=Multiplicity(1, 1)),
        Property(name="C_Commands_ExpressionCommand", type=Expressions_Expression, multiplicity=Multiplicity(0, 1))
    }
)
condition55: BinaryAssociation = BinaryAssociation(
    name="condition55",
    ends={
        Property(name="Expressions_ConditionalExpression", type=C_Commands_IfCommand, multiplicity=Multiplicity(1, 1)),
        Property(name="C_Commands_IfCommand", type=Expressions_ConditionalExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
id47: BinaryAssociation = BinaryAssociation(
    name="id47",
    ends={
        Property(name="Expressions_Access", type=C_Commands_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="C_Commands_Assignment", type=Expressions_Access, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
thenBlock56: BinaryAssociation = BinaryAssociation(
    name="thenBlock56",
    ends={
        Property(name="Main_Block58", type=C_Commands_IfCommand, multiplicity=Multiplicity(1, 1)),
        Property(name="C_Commands_IfCommand57", type=Main_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elseBlock59: BinaryAssociation = BinaryAssociation(
    name="elseBlock59",
    ends={
        Property(name="Main_Block61", type=C_Commands_IfCommand, multiplicity=Multiplicity(1, 1)),
        Property(name="C_Commands_IfCommand60", type=Main_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable62: BinaryAssociation = BinaryAssociation(
    name="variable62",
    ends={
        Property(name="Expressions_VariableAccess", type=C_Commands_SwitchCommand, multiplicity=Multiplicity(1, 1)),
        Property(name="C_Commands_SwitchCommand", type=Expressions_VariableAccess, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
case63: BinaryAssociation = BinaryAssociation(
    name="case63",
    ends={
        Property(name="Commands_CaseOption", type=C_Commands_SwitchCommand, multiplicity=Multiplicity(1, 1)),
        Property(name="C_Commands_SwitchCommand64", type=Commands_CaseOption, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
default65: BinaryAssociation = BinaryAssociation(
    name="default65",
    ends={
        Property(name="Commands_DefaultOption", type=C_Commands_SwitchCommand, multiplicity=Multiplicity(1, 1)),
        Property(name="C_Commands_SwitchCommand66", type=Commands_DefaultOption, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body69: BinaryAssociation = BinaryAssociation(
    name="body69",
    ends={
        Property(name="Main_Block71", type=C_Commands_CaseOption, multiplicity=Multiplicity(1, 1)),
        Property(name="C_Commands_CaseOption70", type=Main_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body72: BinaryAssociation = BinaryAssociation(
    name="body72",
    ends={
        Property(name="Main_Block73", type=C_Commands_DefaultOption, multiplicity=Multiplicity(1, 1)),
        Property(name="C_Commands_DefaultOption", type=Main_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body74: BinaryAssociation = BinaryAssociation(
    name="body74",
    ends={
        Property(name="Main_Block75", type=C_Commands_IterativeCommand, multiplicity=Multiplicity(1, 1)),
        Property(name="C_Commands_IterativeCommand", type=Main_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
inicializer76: BinaryAssociation = BinaryAssociation(
    name="inicializer76",
    ends={
        Property(name="Expressions_Expression77", type=C_Commands_ForCommand, multiplicity=Multiplicity(1, 1)),
        Property(name="C_Commands_ForCommand", type=Expressions_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value67: BinaryAssociation = BinaryAssociation(
    name="value67",
    ends={
        Property(name="Expressions_Literal68", type=C_Commands_CaseOption, multiplicity=Multiplicity(1, 1)),
        Property(name="C_Commands_CaseOption", type=Expressions_Literal, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition84: BinaryAssociation = BinaryAssociation(
    name="condition84",
    ends={
        Property(name="Expressions_ConditionalExpression85", type=C_Commands_WhileCommand, multiplicity=Multiplicity(1, 1)),
        Property(name="C_Commands_WhileCommand", type=Expressions_ConditionalExpression, multiplicity=Multiplicity(0, 1))
    }
)
element86: BinaryAssociation = BinaryAssociation(
    name="element86",
    ends={
        Property(name="Expressions_Expression87", type=C_Expressions_Construction, multiplicity=Multiplicity(1, 1)),
        Property(name="C_Expressions_Construction", type=Expressions_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
argument88: BinaryAssociation = BinaryAssociation(
    name="argument88",
    ends={
        Property(name="Expressions_Expression89", type=C_Expressions_FunctionCall, multiplicity=Multiplicity(1, 1)),
        Property(name="C_Expressions_FunctionCall", type=Expressions_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression78: BinaryAssociation = BinaryAssociation(
    name="expression78",
    ends={
        Property(name="Expressions_Expression80", type=C_Commands_ForCommand, multiplicity=Multiplicity(1, 1)),
        Property(name="C_Commands_ForCommand79", type=Expressions_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
updater81: BinaryAssociation = BinaryAssociation(
    name="updater81",
    ends={
        Property(name="Expressions_Expression83", type=C_Commands_ForCommand, multiplicity=Multiplicity(1, 1)),
        Property(name="C_Commands_ForCommand82", type=Expressions_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression92: BinaryAssociation = BinaryAssociation(
    name="expression92",
    ends={
        Property(name="Expressions_Expression94", type=C_Expressions_CastExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="C_Expressions_CastExpression93", type=Expressions_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operand95: BinaryAssociation = BinaryAssociation(
    name="operand95",
    ends={
        Property(name="Expressions_Expression96", type=C_Expressions_ArithmeticExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="C_Expressions_ArithmeticExpression", type=Expressions_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
extraOperand97: BinaryAssociation = BinaryAssociation(
    name="extraOperand97",
    ends={
        Property(name="Expressions_Expression98", type=C_Expressions_BinaryArithmeticExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="C_Expressions_BinaryArithmeticExpression", type=Expressions_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type90: BinaryAssociation = BinaryAssociation(
    name="type90",
    ends={
        Property(name="Types_Type91", type=C_Expressions_CastExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="C_Expressions_CastExpression", type=Types_Type, multiplicity=Multiplicity(0, 1))
    }
)
term99: BinaryAssociation = BinaryAssociation(
    name="term99",
    ends={
        Property(name="Expressions_Expression100", type=C_Expressions_ComposedConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="C_Expressions_ComposedConditionalExpression", type=Expressions_Expression, multiplicity=Multiplicity(2, 2), is_composite=True)
    }
)
expression101: BinaryAssociation = BinaryAssociation(
    name="expression101",
    ends={
        Property(name="Expressions_Expression102", type=C_Expressions_LogicExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="C_Expressions_LogicExpression", type=Expressions_Expression, multiplicity=Multiplicity(0, 1))
    }
)
constant105: BinaryAssociation = BinaryAssociation(
    name="constant105",
    ends={
        Property(name="Declarations_ConstantDeclaration", type=C_Expressions_ConstantAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="C_Expressions_ConstantAccess", type=Declarations_ConstantDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
variable106: BinaryAssociation = BinaryAssociation(
    name="variable106",
    ends={
        Property(name="Declarations_VariableDeclaration107", type=C_Expressions_VariableAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="C_Expressions_VariableAccess", type=Declarations_VariableDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
numberOfDisplacement103: BinaryAssociation = BinaryAssociation(
    name="numberOfDisplacement103",
    ends={
        Property(name="Expressions_Expression104", type=C_Expressions_DisplacementLogicExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="C_Expressions_DisplacementLogicExpression", type=Expressions_Expression, multiplicity=Multiplicity(0, 1))
    }
)
index109: BinaryAssociation = BinaryAssociation(
    name="index109",
    ends={
        Property(name="Expressions_Expression111", type=C_Expressions_ArrayAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="C_Expressions_ArrayAccess110", type=Expressions_Expression, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
expression112: BinaryAssociation = BinaryAssociation(
    name="expression112",
    ends={
        Property(name="Expressions_Expression114", type=C_Expressions_ArrayAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="C_Expressions_ArrayAccess113", type=Expressions_Expression, multiplicity=Multiplicity(0, 1))
    }
)
prototype115: BinaryAssociation = BinaryAssociation(
    name="prototype115",
    ends={
        Property(name="Declarations_PrototypeFunctionDeclaration", type=C_Expressions_PrototypeAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="C_Expressions_PrototypeAccess", type=Declarations_PrototypeFunctionDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
array108: BinaryAssociation = BinaryAssociation(
    name="array108",
    ends={
        Property(name="Declarations_ArrayDeclaration", type=C_Expressions_ArrayAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="C_Expressions_ArrayAccess", type=Declarations_ArrayDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
refersTo116: BinaryAssociation = BinaryAssociation(
    name="refersTo116",
    ends={
        Property(name="Commands_LabelCommand", type=C_Sequencers_Goto, multiplicity=Multiplicity(1, 1)),
        Property(name="C_Sequencers_Goto", type=Commands_LabelCommand, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_C_Types_Char_PrimitiveType = Generalization(general=PrimitiveType, specific=C_Types_Char)
gen_C_Types_Int_Types_PrimitiveType = Generalization(general=Types_PrimitiveType, specific=C_Types_Int)
gen_C_Types_Int_Types_Array = Generalization(general=Types_Array, specific=C_Types_Int)
gen_C_Types_Float_PrimitiveType = Generalization(general=PrimitiveType, specific=C_Types_Float)
gen_C_Types_Double_PrimitiveType = Generalization(general=PrimitiveType, specific=C_Types_Double)
gen_C_Types_Short_PrimitiveType = Generalization(general=PrimitiveType, specific=C_Types_Short)
gen_C_Types_Void_PrimitiveType = Generalization(general=PrimitiveType, specific=C_Types_Void)
gen_C_Types_Typedef_CompositeType = Generalization(general=CompositeType, specific=C_Types_Typedef)
gen_C_Types_Array_CompositeType = Generalization(general=CompositeType, specific=C_Types_Array)
gen_C_Types_PrimitiveType_Type = Generalization(general=Type, specific=C_Types_PrimitiveType)
gen_C_Types_CompositeType_Type = Generalization(general=Type, specific=C_Types_CompositeType)
gen_C_Types_Enum_CompositeType = Generalization(general=CompositeType, specific=C_Types_Enum)
gen_C_Types_FromHeader_Types_Type = Generalization(general=Types_Type, specific=C_Types_FromHeader)
gen_C_Types_FromHeader_Abstractions_NamedElement = Generalization(general=Abstractions_NamedElement, specific=C_Types_FromHeader)
gen_C_Types_Struct_CompositeType = Generalization(general=CompositeType, specific=C_Types_Struct)
gen_C_Main_Unit_NamedElement = Generalization(general=NamedElement, specific=C_Main_Unit)
gen_C_Main_C_Unit_Unit = Generalization(general=Unit, specific=C_Main_C_Unit)
gen_C_Main_Function_Element = Generalization(general=Element, specific=C_Main_Function)
gen_C_Main_H_Unit_Unit = Generalization(general=Unit, specific=C_Main_H_Unit)
gen_C_Main_Comment_NamedElement = Generalization(general=NamedElement, specific=C_Main_Comment)
gen_C_Main_Element_NamedElement = Generalization(general=NamedElement, specific=C_Main_Element)
gen_C_Main_DeclarationsBlock_Element = Generalization(general=Element, specific=C_Main_DeclarationsBlock)
gen_C_Declarations_Declaration_NamedElement = Generalization(general=NamedElement, specific=C_Declarations_Declaration)
gen_C_Declarations_ConstantDeclaration_Declaration = Generalization(general=Declaration, specific=C_Declarations_ConstantDeclaration)
gen_C_Main_FunctionsBlock_Element = Generalization(general=Element, specific=C_Main_FunctionsBlock)
gen_C_Declarations_SimpleVariableDeclaration_Declarations_VariableDeclaration = Generalization(general=Declarations_VariableDeclaration, specific=C_Declarations_SimpleVariableDeclaration)
gen_C_Declarations_SimpleVariableDeclaration_Abstractions_BlockedElement = Generalization(general=Abstractions_BlockedElement, specific=C_Declarations_SimpleVariableDeclaration)
gen_C_Declarations_PrototypeFunctionDeclaration_Declaration = Generalization(general=Declaration, specific=C_Declarations_PrototypeFunctionDeclaration)
gen_C_Declarations_VariableDeclaration_Declaration = Generalization(general=Declaration, specific=C_Declarations_VariableDeclaration)
gen_C_Declarations_FragmentVariableDeclaration_Abstractions_NamedElement = Generalization(general=Abstractions_NamedElement, specific=C_Declarations_FragmentVariableDeclaration)
gen_C_Declarations_FragmentVariableDeclaration_Declarations_VariableDeclaration = Generalization(general=Declarations_VariableDeclaration, specific=C_Declarations_FragmentVariableDeclaration)
gen_C_Declarations_CompositeVariableDeclaration_VariableDeclaration = Generalization(general=VariableDeclaration, specific=C_Declarations_CompositeVariableDeclaration)
gen_C_Declarations_EnumDeclaration_CompositeVariableDeclaration = Generalization(general=CompositeVariableDeclaration, specific=C_Declarations_EnumDeclaration)
gen_C_Declarations_ArrayDeclaration_Declarations_CompositeVariableDeclaration = Generalization(general=Declarations_CompositeVariableDeclaration, specific=C_Declarations_ArrayDeclaration)
gen_C_Declarations_ArrayDeclaration_Abstractions_BlockedElement = Generalization(general=Abstractions_BlockedElement, specific=C_Declarations_ArrayDeclaration)
gen_C_Declarations_StructDeclaration_CompositeVariableDeclaration = Generalization(general=CompositeVariableDeclaration, specific=C_Declarations_StructDeclaration)
gen_C_Declarations_TypeDefDeclaration_CompositeVariableDeclaration = Generalization(general=CompositeVariableDeclaration, specific=C_Declarations_TypeDefDeclaration)
gen_C_CompilationDirectiveDeclarations_SimpleDirectiveDeclaration_CompilationDirectiveDeclarations_CompilationDirectiveDeclaration = Generalization(general=CompilationDirectiveDeclarations_CompilationDirectiveDeclaration, specific=C_CompilationDirectiveDeclarations_SimpleDirectiveDeclaration)
gen_C_CompilationDirectiveDeclarations_SimpleDirectiveDeclaration_Abstractions_NamedElement = Generalization(general=Abstractions_NamedElement, specific=C_CompilationDirectiveDeclarations_SimpleDirectiveDeclaration)
gen_C_CompilationDirectiveDeclarations_ComplexDirectiveDeclaration_CompilationDirectiveDeclaration = Generalization(general=CompilationDirectiveDeclaration, specific=C_CompilationDirectiveDeclarations_ComplexDirectiveDeclaration)
gen_C_CompilationDirectiveDeclarations_Define_SimpleDirectiveDeclaration = Generalization(general=SimpleDirectiveDeclaration, specific=C_CompilationDirectiveDeclarations_Define)
gen_C_CompilationDirectiveDeclarations_Include_SimpleDirectiveDeclaration = Generalization(general=SimpleDirectiveDeclaration, specific=C_CompilationDirectiveDeclarations_Include)
gen_C_CompilationDirectiveDeclarations_Ifdef_CompilationDirectiveDeclarations_ComplexDirectiveDeclaration = Generalization(general=CompilationDirectiveDeclarations_ComplexDirectiveDeclaration, specific=C_CompilationDirectiveDeclarations_Ifdef)
gen_C_CompilationDirectiveDeclarations_Ifdef_Abstractions_NamedElement = Generalization(general=Abstractions_NamedElement, specific=C_CompilationDirectiveDeclarations_Ifdef)
gen_C_CompilationDirectiveDeclarations_IfDirective_ComplexDirectiveDeclaration = Generalization(general=ComplexDirectiveDeclaration, specific=C_CompilationDirectiveDeclarations_IfDirective)
gen_C_CompilationDirectiveDeclarations_Elif_IfDirective = Generalization(general=IfDirective, specific=C_CompilationDirectiveDeclarations_Elif)
gen_C_Commands_Command_BlockedElement = Generalization(general=BlockedElement, specific=C_Commands_Command)
gen_C_Commands_LabelCommand_Commands_Command = Generalization(general=Commands_Command, specific=C_Commands_LabelCommand)
gen_C_Commands_LabelCommand_Abstractions_NamedElement = Generalization(general=Abstractions_NamedElement, specific=C_Commands_LabelCommand)
gen_C_CompilationDirectiveDeclarations_Ifndef_ComplexDirectiveDeclaration = Generalization(general=ComplexDirectiveDeclaration, specific=C_CompilationDirectiveDeclarations_Ifndef)
gen_C_CompilationDirectiveDeclarations_ElseDirective_ComplexDirectiveDeclaration = Generalization(general=ComplexDirectiveDeclaration, specific=C_CompilationDirectiveDeclarations_ElseDirective)
gen_C_Commands_FlowControlCommand_Command = Generalization(general=Command, specific=C_Commands_FlowControlCommand)
gen_C_Commands_DecisionCommand_FlowControlCommand = Generalization(general=FlowControlCommand, specific=C_Commands_DecisionCommand)
gen_C_Commands_ReturnCommand_FlowControlCommand = Generalization(general=FlowControlCommand, specific=C_Commands_ReturnCommand)
gen_C_Commands_ExpressionCommand_Command = Generalization(general=Command, specific=C_Commands_ExpressionCommand)
gen_C_Commands_IfCommand_DecisionCommand = Generalization(general=DecisionCommand, specific=C_Commands_IfCommand)
gen_C_Commands_Assignment_Command = Generalization(general=Command, specific=C_Commands_Assignment)
gen_C_Commands_SwitchCommand_DecisionCommand = Generalization(general=DecisionCommand, specific=C_Commands_SwitchCommand)
gen_C_Commands_IterativeCommand_Command = Generalization(general=Command, specific=C_Commands_IterativeCommand)
gen_C_Commands_ForCommand_IterativeCommand = Generalization(general=IterativeCommand, specific=C_Commands_ForCommand)
gen_C_Commands_WhileCommand_IterativeCommand = Generalization(general=IterativeCommand, specific=C_Commands_WhileCommand)
gen_C_Expressions_Construction_Expression = Generalization(general=Expression, specific=C_Expressions_Construction)
gen_C_Expressions_FunctionCall_Expressions_Expression = Generalization(general=Expressions_Expression, specific=C_Expressions_FunctionCall)
gen_C_Expressions_FunctionCall_Abstractions_NamedElement = Generalization(general=Abstractions_NamedElement, specific=C_Expressions_FunctionCall)
gen_C_Expressions_ArithmeticExpression_Expression = Generalization(general=Expression, specific=C_Expressions_ArithmeticExpression)
gen_C_Expressions_UnaryArithmeticExpression_ArithmeticExpression = Generalization(general=ArithmeticExpression, specific=C_Expressions_UnaryArithmeticExpression)
gen_C_Expressions_BinaryArithmeticExpression_ArithmeticExpression = Generalization(general=ArithmeticExpression, specific=C_Expressions_BinaryArithmeticExpression)
gen_C_Expressions_CastExpression_Expression = Generalization(general=Expression, specific=C_Expressions_CastExpression)
gen_C_Expressions_AtomicConditionalExpression_Expressions_ConditionalExpression = Generalization(general=Expressions_ConditionalExpression, specific=C_Expressions_AtomicConditionalExpression)
gen_C_Expressions_AtomicConditionalExpression_Abstractions_NamedElement = Generalization(general=Abstractions_NamedElement, specific=C_Expressions_AtomicConditionalExpression)
gen_C_Expressions_ComposedConditionalExpression_ConditionalExpression = Generalization(general=ConditionalExpression, specific=C_Expressions_ComposedConditionalExpression)
gen_C_Expressions_LogicExpression_Expression = Generalization(general=Expression, specific=C_Expressions_LogicExpression)
gen_C_Expressions_ConditionalExpression_Expression = Generalization(general=Expression, specific=C_Expressions_ConditionalExpression)
gen_C_Expressions_SimpleLogicExpression_LogicExpression = Generalization(general=LogicExpression, specific=C_Expressions_SimpleLogicExpression)
gen_C_Expressions_Access_Expressions_Expression = Generalization(general=Expressions_Expression, specific=C_Expressions_Access)
gen_C_Expressions_Access_Abstractions_NamedElement = Generalization(general=Abstractions_NamedElement, specific=C_Expressions_Access)
gen_C_Expressions_ConstantAccess_Access = Generalization(general=Access, specific=C_Expressions_ConstantAccess)
gen_C_Expressions_VariableAccess_Access = Generalization(general=Access, specific=C_Expressions_VariableAccess)
gen_C_Expressions_DisplacementLogicExpression_LogicExpression = Generalization(general=LogicExpression, specific=C_Expressions_DisplacementLogicExpression)
gen_C_Expressions_PointerVariableAccess_VariableAccess = Generalization(general=VariableAccess, specific=C_Expressions_PointerVariableAccess)
gen_C_Expressions_PrototypeAccess_Access = Generalization(general=Access, specific=C_Expressions_PrototypeAccess)
gen_C_Expressions_Literal_Expression = Generalization(general=Expression, specific=C_Expressions_Literal)
gen_C_Expressions_CharLiteral_Literal = Generalization(general=Literal, specific=C_Expressions_CharLiteral)
gen_C_Expressions_ArrayAccess_Access = Generalization(general=Access, specific=C_Expressions_ArrayAccess)
gen_C_Expressions_DoubleLiteral_Literal = Generalization(general=Literal, specific=C_Expressions_DoubleLiteral)
gen_C_Expressions_StringLiteral_Literal = Generalization(general=Literal, specific=C_Expressions_StringLiteral)
gen_C_Expressions_ShortLiteral_Literal = Generalization(general=Literal, specific=C_Expressions_ShortLiteral)
gen_C_Expressions_ConstantExpression_Expression = Generalization(general=Expression, specific=C_Expressions_ConstantExpression)
gen_C_Sequencers_Sequencer_BlockedElement = Generalization(general=BlockedElement, specific=C_Sequencers_Sequencer)
gen_C_Sequencers_Goto_Sequencer = Generalization(general=Sequencer, specific=C_Sequencers_Goto)
gen_C_Expressions_IntLiteral_Literal = Generalization(general=Literal, specific=C_Expressions_IntLiteral)
gen_C_Expressions_FloatLiteral_Literal = Generalization(general=Literal, specific=C_Expressions_FloatLiteral)
gen_C_Sequencers_Break_Sequencer = Generalization(general=Sequencer, specific=C_Sequencers_Break)

# Domain Model
domain_model = DomainModel(
    name="PrimitiveTypes",
    types={C_Types_Type, C_Types_Char, PrimitiveType, C_Types_Int, Types_PrimitiveType, Types_Array, C_Types_Float, C_Types_Double, C_Types_Short, C_Types_Void, C_Types_Typedef, CompositeType, C_Types_Array, C_Types_Struct, C_Types_PrimitiveType, Type, C_Types_CompositeType, C_Types_Enum, C_Types_FromHeader, Types_Type, Abstractions_NamedElement, C_Abstractions_NamedElement, C_Abstractions_BlockedElement, Main_Block, Main_Unit, C_Main_Unit, NamedElement, Main_Comment, C_Main_C_Unit, Unit, Main_Element, C_Main_Program, C_Main_Function, Element, Declarations_Declaration, C_Main_H_Unit, Main_DeclarationsBlock, Abstractions_BlockedElement, C_Main_Block, C_Main_Comment, C_Main_Element, C_Main_DeclarationsBlock, CompilationDirectiveDeclarations_CompilationDirectiveDeclaration, C_Main_FunctionsBlock, Main_Function, C_Declarations_Declaration, C_Declarations_ConstantDeclaration, Declaration, Expressions_Expression, C_Declarations_SimpleVariableDeclaration, Declarations_VariableDeclaration, Declarations_FragmentVariableDeclaration, C_Declarations_PrototypeFunctionDeclaration, C_Declarations_VariableDeclaration, C_Declarations_FragmentVariableDeclaration, C_Declarations_CompositeVariableDeclaration, VariableDeclaration, C_Declarations_EnumDeclaration, CompositeVariableDeclaration, Expressions_Literal, Declarations_CompositeVariableDeclaration, Expressions_Construction, C_Declarations_StructDeclaration, Declarations_SimpleVariableDeclaration, C_Declarations_TypeDefDeclaration, C_Declarations_ArrayDeclaration, C_CompilationDirectiveDeclarations_SimpleDirectiveDeclaration, C_CompilationDirectiveDeclarations_ComplexDirectiveDeclaration, CompilationDirectiveDeclaration, C_CompilationDirectiveDeclarations_Define, SimpleDirectiveDeclaration, C_CompilationDirectiveDeclarations_Include, C_CompilationDirectiveDeclarations_Ifdef, CompilationDirectiveDeclarations_ComplexDirectiveDeclaration, CompilationDirectiveDeclarations_Endif, C_CompilationDirectiveDeclarations_Ifndef, ComplexDirectiveDeclaration, C_CompilationDirectiveDeclarations_CompilationDirectiveDeclaration, C_CompilationDirectiveDeclarations_IfDirective, Expressions_ConstantExpression, C_CompilationDirectiveDeclarations_Elif, IfDirective, C_CompilationDirectiveDeclarations_Endif, C_Commands_Command, BlockedElement, C_Commands_LabelCommand, Commands_Command, C_CompilationDirectiveDeclarations_ElseDirective, C_Commands_FlowControlCommand, C_Commands_DecisionCommand, FlowControlCommand, C_Commands_ReturnCommand, C_Commands_ExpressionCommand, C_Commands_IfCommand, DecisionCommand, Expressions_ConditionalExpression, C_Commands_Assignment, Command, Expressions_Access, C_Commands_SwitchCommand, Expressions_VariableAccess, Commands_CaseOption, Commands_DefaultOption, C_Commands_DefaultOption, C_Commands_IterativeCommand, C_Commands_ForCommand, IterativeCommand, C_Commands_CaseOption, C_Commands_WhileCommand, C_Expressions_Expression, C_Expressions_Construction, Expression, C_Expressions_FunctionCall, C_Expressions_ArithmeticExpression, C_Expressions_UnaryArithmeticExpression, ArithmeticExpression, C_Expressions_BinaryArithmeticExpression, C_Expressions_CastExpression, C_Expressions_AtomicConditionalExpression, C_Expressions_ComposedConditionalExpression, ConditionalExpression, C_Expressions_LogicExpression, C_Expressions_DisplacementLogicExpression, LogicExpression, C_Expressions_ConditionalExpression, C_Expressions_SimpleLogicExpression, C_Expressions_Access, C_Expressions_ConstantAccess, Access, Declarations_ConstantDeclaration, C_Expressions_VariableAccess, C_Expressions_PointerVariableAccess, VariableAccess, C_Expressions_PrototypeAccess, Declarations_PrototypeFunctionDeclaration, C_Expressions_Literal, C_Expressions_CharLiteral, Literal, C_Expressions_ArrayAccess, Declarations_ArrayDeclaration, C_Expressions_DoubleLiteral, C_Expressions_StringLiteral, C_Expressions_ShortLiteral, C_Expressions_ConstantExpression, C_Sequencers_Sequencer, C_Sequencers_Goto, Sequencer, C_Expressions_IntLiteral, C_Expressions_FloatLiteral, C_Sequencers_Break, Commands_LabelCommand, ModifierKind, UnaryOperatorKind, BinaryOperatorKind, DisplacementLogicOperatorKind, SimpleLogicOperatorKind, FunctionModifierKind, RelationalConectorKind, RelationalOperatorKind},
    associations={file1, comment2, elements3, element0, declaration4, return5, body6, ownedParameter9, element11, comment12, directive17, declaration15, function19, initializer20, type21, fragment23, initializer25, ownedParameter28, type29, literal32, inicializer33, elementType34, element37, type38, declaration40, end42, expression45, refersTo46, end43, expression48, expression51, expression53, condition55, id47, thenBlock56, elseBlock59, variable62, case63, default65, body69, body72, body74, inicializer76, value67, condition84, element86, argument88, expression78, updater81, expression92, operand95, extraOperand97, type90, term99, expression101, constant105, variable106, numberOfDisplacement103, index109, expression112, prototype115, array108, refersTo116},
    generalizations={gen_C_Types_Char_PrimitiveType, gen_C_Types_Int_Types_PrimitiveType, gen_C_Types_Int_Types_Array, gen_C_Types_Float_PrimitiveType, gen_C_Types_Double_PrimitiveType, gen_C_Types_Short_PrimitiveType, gen_C_Types_Void_PrimitiveType, gen_C_Types_Typedef_CompositeType, gen_C_Types_Array_CompositeType, gen_C_Types_PrimitiveType_Type, gen_C_Types_CompositeType_Type, gen_C_Types_Enum_CompositeType, gen_C_Types_FromHeader_Types_Type, gen_C_Types_FromHeader_Abstractions_NamedElement, gen_C_Types_Struct_CompositeType, gen_C_Main_Unit_NamedElement, gen_C_Main_C_Unit_Unit, gen_C_Main_Function_Element, gen_C_Main_H_Unit_Unit, gen_C_Main_Comment_NamedElement, gen_C_Main_Element_NamedElement, gen_C_Main_DeclarationsBlock_Element, gen_C_Declarations_Declaration_NamedElement, gen_C_Declarations_ConstantDeclaration_Declaration, gen_C_Main_FunctionsBlock_Element, gen_C_Declarations_SimpleVariableDeclaration_Declarations_VariableDeclaration, gen_C_Declarations_SimpleVariableDeclaration_Abstractions_BlockedElement, gen_C_Declarations_PrototypeFunctionDeclaration_Declaration, gen_C_Declarations_VariableDeclaration_Declaration, gen_C_Declarations_FragmentVariableDeclaration_Abstractions_NamedElement, gen_C_Declarations_FragmentVariableDeclaration_Declarations_VariableDeclaration, gen_C_Declarations_CompositeVariableDeclaration_VariableDeclaration, gen_C_Declarations_EnumDeclaration_CompositeVariableDeclaration, gen_C_Declarations_ArrayDeclaration_Declarations_CompositeVariableDeclaration, gen_C_Declarations_ArrayDeclaration_Abstractions_BlockedElement, gen_C_Declarations_StructDeclaration_CompositeVariableDeclaration, gen_C_Declarations_TypeDefDeclaration_CompositeVariableDeclaration, gen_C_CompilationDirectiveDeclarations_SimpleDirectiveDeclaration_CompilationDirectiveDeclarations_CompilationDirectiveDeclaration, gen_C_CompilationDirectiveDeclarations_SimpleDirectiveDeclaration_Abstractions_NamedElement, gen_C_CompilationDirectiveDeclarations_ComplexDirectiveDeclaration_CompilationDirectiveDeclaration, gen_C_CompilationDirectiveDeclarations_Define_SimpleDirectiveDeclaration, gen_C_CompilationDirectiveDeclarations_Include_SimpleDirectiveDeclaration, gen_C_CompilationDirectiveDeclarations_Ifdef_CompilationDirectiveDeclarations_ComplexDirectiveDeclaration, gen_C_CompilationDirectiveDeclarations_Ifdef_Abstractions_NamedElement, gen_C_CompilationDirectiveDeclarations_IfDirective_ComplexDirectiveDeclaration, gen_C_CompilationDirectiveDeclarations_Elif_IfDirective, gen_C_Commands_Command_BlockedElement, gen_C_Commands_LabelCommand_Commands_Command, gen_C_Commands_LabelCommand_Abstractions_NamedElement, gen_C_CompilationDirectiveDeclarations_Ifndef_ComplexDirectiveDeclaration, gen_C_CompilationDirectiveDeclarations_ElseDirective_ComplexDirectiveDeclaration, gen_C_Commands_FlowControlCommand_Command, gen_C_Commands_DecisionCommand_FlowControlCommand, gen_C_Commands_ReturnCommand_FlowControlCommand, gen_C_Commands_ExpressionCommand_Command, gen_C_Commands_IfCommand_DecisionCommand, gen_C_Commands_Assignment_Command, gen_C_Commands_SwitchCommand_DecisionCommand, gen_C_Commands_IterativeCommand_Command, gen_C_Commands_ForCommand_IterativeCommand, gen_C_Commands_WhileCommand_IterativeCommand, gen_C_Expressions_Construction_Expression, gen_C_Expressions_FunctionCall_Expressions_Expression, gen_C_Expressions_FunctionCall_Abstractions_NamedElement, gen_C_Expressions_ArithmeticExpression_Expression, gen_C_Expressions_UnaryArithmeticExpression_ArithmeticExpression, gen_C_Expressions_BinaryArithmeticExpression_ArithmeticExpression, gen_C_Expressions_CastExpression_Expression, gen_C_Expressions_AtomicConditionalExpression_Expressions_ConditionalExpression, gen_C_Expressions_AtomicConditionalExpression_Abstractions_NamedElement, gen_C_Expressions_ComposedConditionalExpression_ConditionalExpression, gen_C_Expressions_LogicExpression_Expression, gen_C_Expressions_ConditionalExpression_Expression, gen_C_Expressions_SimpleLogicExpression_LogicExpression, gen_C_Expressions_Access_Expressions_Expression, gen_C_Expressions_Access_Abstractions_NamedElement, gen_C_Expressions_ConstantAccess_Access, gen_C_Expressions_VariableAccess_Access, gen_C_Expressions_DisplacementLogicExpression_LogicExpression, gen_C_Expressions_PointerVariableAccess_VariableAccess, gen_C_Expressions_PrototypeAccess_Access, gen_C_Expressions_Literal_Expression, gen_C_Expressions_CharLiteral_Literal, gen_C_Expressions_ArrayAccess_Access, gen_C_Expressions_DoubleLiteral_Literal, gen_C_Expressions_StringLiteral_Literal, gen_C_Expressions_ShortLiteral_Literal, gen_C_Expressions_ConstantExpression_Expression, gen_C_Sequencers_Sequencer_BlockedElement, gen_C_Sequencers_Goto_Sequencer, gen_C_Expressions_IntLiteral_Literal, gen_C_Expressions_FloatLiteral_Literal, gen_C_Sequencers_Break_Sequencer},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)