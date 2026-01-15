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
BuiltinLibs: Enumeration = Enumeration(
    name="BuiltinLibs",
    literals={
            EnumerationLiteral(name="WORK")
    }
)

EString: Enumeration = Enumeration(
    name="EString",
    literals={
            EnumerationLiteral(name="TO_UNSIGNED"),
			EnumerationLiteral(name="RISING_EDGE"),
			EnumerationLiteral(name="STD_LOGIC"),
			EnumerationLiteral(name="STD_LOGIC_VECTOR"),
			EnumerationLiteral(name="INTEGER"),
			EnumerationLiteral(name="NATURAL"),
			EnumerationLiteral(name="UNSIGNED"),
			EnumerationLiteral(name="STRING"),
			EnumerationLiteral(name="FALLING_EDGE")
    }
)

ShiftOperator: Enumeration = Enumeration(
    name="ShiftOperator",
    literals={
            EnumerationLiteral(name="SLL"),
			EnumerationLiteral(name="SRL"),
			EnumerationLiteral(name="SLA"),
			EnumerationLiteral(name="SRA"),
			EnumerationLiteral(name="ROL"),
			EnumerationLiteral(name="ROR")
    }
)

SignalKind: Enumeration = Enumeration(
    name="SignalKind",
    literals={
            EnumerationLiteral(name="REGISTER"),
			EnumerationLiteral(name="BUS")
    }
)

RangeDirection: Enumeration = Enumeration(
    name="RangeDirection",
    literals={
            EnumerationLiteral(name="TO"),
			EnumerationLiteral(name="DOWNTO")
    }
)

Mode: Enumeration = Enumeration(
    name="Mode",
    literals={
            EnumerationLiteral(name="IN"),
			EnumerationLiteral(name="OUT"),
			EnumerationLiteral(name="INOUT"),
			EnumerationLiteral(name="BUFFER"),
			EnumerationLiteral(name="LINKAGE")
    }
)

UnaryOperator: Enumeration = Enumeration(
    name="UnaryOperator",
    literals={
            EnumerationLiteral(name="ABS"),
			EnumerationLiteral(name="NOT")
    }
)

MultiplyingOperator: Enumeration = Enumeration(
    name="MultiplyingOperator",
    literals={
            EnumerationLiteral(name="MOD"),
			EnumerationLiteral(name="REM"),
			EnumerationLiteral(name="MUL"),
			EnumerationLiteral(name="DIV")
    }
)

Purity: Enumeration = Enumeration(
    name="Purity",
    literals={
            EnumerationLiteral(name="PURE"),
			EnumerationLiteral(name="IMPURE")
    }
)

RelationalOperator: Enumeration = Enumeration(
    name="RelationalOperator",
    literals={
            EnumerationLiteral(name="EQ"),
			EnumerationLiteral(name="NEQ"),
			EnumerationLiteral(name="LOWERTHAN"),
			EnumerationLiteral(name="LE"),
			EnumerationLiteral(name="GREATERTHAN"),
			EnumerationLiteral(name="GE"),
			EnumerationLiteral(name="ASSOCIATE")
    }
)

LogicalOperator: Enumeration = Enumeration(
    name="LogicalOperator",
    literals={
            EnumerationLiteral(name="AND"),
			EnumerationLiteral(name="OR"),
			EnumerationLiteral(name="NAND"),
			EnumerationLiteral(name="NOR"),
			EnumerationLiteral(name="XOR"),
			EnumerationLiteral(name="XNOR")
    }
)

AddingOperator: Enumeration = Enumeration(
    name="AddingOperator",
    literals={
            EnumerationLiteral(name="PLUS"),
			EnumerationLiteral(name="MINUS"),
			EnumerationLiteral(name="AMPERSAND")
    }
)

Sign: Enumeration = Enumeration(
    name="Sign",
    literals={
            EnumerationLiteral(name="PLUS"),
			EnumerationLiteral(name="MINUS")
    }
)

EntityClass: Enumeration = Enumeration(
    name="EntityClass",
    literals={
            EnumerationLiteral(name="ENTITY"),
			EnumerationLiteral(name="ARCHITECTURE"),
			EnumerationLiteral(name="CONFIGURATION"),
			EnumerationLiteral(name="PROCEDURE"),
			EnumerationLiteral(name="FUNCTION"),
			EnumerationLiteral(name="PACKAGE"),
			EnumerationLiteral(name="TYPE"),
			EnumerationLiteral(name="SUBTYPE"),
			EnumerationLiteral(name="CONSTANT"),
			EnumerationLiteral(name="SIGNAL"),
			EnumerationLiteral(name="VARIABLE"),
			EnumerationLiteral(name="COMPONENT"),
			EnumerationLiteral(name="LABEL"),
			EnumerationLiteral(name="LITERAL"),
			EnumerationLiteral(name="UNITS"),
			EnumerationLiteral(name="GROUP"),
			EnumerationLiteral(name="FILE"),
			EnumerationLiteral(name="NATURE"),
			EnumerationLiteral(name="SUBNATURE"),
			EnumerationLiteral(name="QUANTITY"),
			EnumerationLiteral(name="TERMINAL")
    }
)

# Classes
vhdl_DesignFile = Class(name="vhdl::DesignFile")
vhdl_ContextItem = Class(name="vhdl::ContextItem")
vhdl_LibraryUnit = Class(name="vhdl::LibraryUnit")
vhdl_UseClause = Class(name="vhdl::UseClause")
ContextItem = Class(name="ContextItem")
vhdl_Library = Class(name="vhdl::Library")
vhdl_LibraryClause = Class(name="vhdl::LibraryClause")
vhdl_Package = Class(name="vhdl::Package")
LibraryUnit = Class(name="LibraryUnit")
vhdl_package_declarative_item = Class(name="vhdl::package::declarative::item")
vhdl_package_declarative_part = Class(name="vhdl::package::declarative::part")
vhdl_Architecture = Class(name="vhdl::Architecture")
vhdl_Entity = Class(name="vhdl::Entity")
vhdl_BlockDeclarativeItem = Class(name="vhdl::BlockDeclarativeItem")
vhdl_ArchitectureStatement = Class(name="vhdl::ArchitectureStatement")
vhdl_Generics = Class(name="vhdl::Generics")
vhdl_Ports = Class(name="vhdl::Ports")
vhdl_Port = Class(name="vhdl::Port")
Variable = Class(name="Variable")
vhdl_SubtypeIndication = Class(name="vhdl::SubtypeIndication")
vhdl_Expression = Class(name="vhdl::Expression")
vhdl_Generic = Class(name="vhdl::Generic")
vhdl_Alias = Class(name="vhdl::Alias")
BlockDeclarativeItem = Class(name="BlockDeclarativeItem")
vhdl_SignalDeclaration = Class(name="vhdl::SignalDeclaration")
package_declarative_item = Class(name="package::declarative::item")
vhdl_Signal = Class(name="vhdl::Signal")
vhdl_VariableDeclaration = Class(name="vhdl::VariableDeclaration")
vhdl_Var = Class(name="vhdl::Var")
vhdl_ConstantDeclaration = Class(name="vhdl::ConstantDeclaration")
vhdl_Constant = Class(name="vhdl::Constant")
vhdl_AttributeDeclaration = Class(name="vhdl::AttributeDeclaration")
vhdl_AttributeSpecification = Class(name="vhdl::AttributeSpecification")
vhdl_Component = Class(name="vhdl::Component")
vhdl_ProcessStatement = Class(name="vhdl::ProcessStatement")
ArchitectureStatement = Class(name="ArchitectureStatement")
vhdl_IdList = Class(name="vhdl::IdList")
vhdl_SequentialStatement = Class(name="vhdl::SequentialStatement")
vhdl_ComponentInstantiationStatement = Class(name="vhdl::ComponentInstantiationStatement")
vhdl_GenericMap = Class(name="vhdl::GenericMap")
vhdl_PortMap = Class(name="vhdl::PortMap")
vhdl_EntityInstantiationStatement = Class(name="vhdl::EntityInstantiationStatement")
vhdl_PortMapAssociation = Class(name="vhdl::PortMapAssociation")
vhdl_GenericMapAssociation = Class(name="vhdl::GenericMapAssociation")
vhdl_ConditionalSignalAssignmentStatement = Class(name="vhdl::ConditionalSignalAssignmentStatement")
vhdl_ForGenerateStatement = Class(name="vhdl::ForGenerateStatement")
vhdl_LoopVariable = Class(name="vhdl::LoopVariable")
vhdl_IfGenerateStatement = Class(name="vhdl::IfGenerateStatement")
vhdl_WaitStatement = Class(name="vhdl::WaitStatement")
SequentialStatement = Class(name="SequentialStatement")
vhdl_IfStatement = Class(name="vhdl::IfStatement")
vhdl_IfStatementTest = Class(name="vhdl::IfStatementTest")
vhdl_SequentialSignalAssignmentStatement = Class(name="vhdl::SequentialSignalAssignmentStatement")
vhdl_CaseStatement = Class(name="vhdl::CaseStatement")
vhdl_CaseAlternative = Class(name="vhdl::CaseAlternative")
vhdl_LoopStatement = Class(name="vhdl::LoopStatement")
vhdl_IterationScheme = Class(name="vhdl::IterationScheme")
vhdl_WhileIterationScheme = Class(name="vhdl::WhileIterationScheme")
IterationScheme = Class(name="IterationScheme")
vhdl_ForIterationScheme = Class(name="vhdl::ForIterationScheme")
vhdl_Type = Class(name="vhdl::Type")
Expression = Class(name="Expression")
vhdl_SubtypeDeclaration = Class(name="vhdl::SubtypeDeclaration")
Type = Class(name="Type")
vhdl_TypeDeclaration = Class(name="vhdl::TypeDeclaration")
vhdl_TypeDefinition = Class(name="vhdl::TypeDefinition")
vhdl_AccessTypeDefinition = Class(name="vhdl::AccessTypeDefinition")
TypeDefinition = Class(name="TypeDefinition")
vhdl_CompositeTypeDefinition = Class(name="vhdl::CompositeTypeDefinition")
vhdl_ArrayTypeDefinition = Class(name="vhdl::ArrayTypeDefinition")
CompositeTypeDefinition = Class(name="CompositeTypeDefinition")
vhdl_UnconstrainedArrayTypeDefinition = Class(name="vhdl::UnconstrainedArrayTypeDefinition")
ArrayTypeDefinition = Class(name="ArrayTypeDefinition")
vhdl_ConstrainedArrayTypeDefinition = Class(name="vhdl::ConstrainedArrayTypeDefinition")
vhdl_EnumerationTypeDefinition = Class(name="vhdl::EnumerationTypeDefinition")
vhdl_FileTypeDefinition = Class(name="vhdl::FileTypeDefinition")
vhdl_RecordField = Class(name="vhdl::RecordField")
vhdl_RecordTypeDefinition = Class(name="vhdl::RecordTypeDefinition")
vhdl_Variable = Class(name="vhdl::Variable")
vhdl_ValueExpression = Class(name="vhdl::ValueExpression")
vhdl_ConditionalWaveformExpression = Class(name="vhdl::ConditionalWaveformExpression")
vhdl_RangeExpression = Class(name="vhdl::RangeExpression")
vhdl_MultiExpression = Class(name="vhdl::MultiExpression")
vhdl_LogicalExpression = Class(name="vhdl::LogicalExpression")
vhdl_RelationalExpression = Class(name="vhdl::RelationalExpression")
vhdl_ChoiceExpression = Class(name="vhdl::ChoiceExpression")
vhdl_ShiftExpression = Class(name="vhdl::ShiftExpression")
vhdl_AddingExpression = Class(name="vhdl::AddingExpression")
vhdl_MultiplyingExpression = Class(name="vhdl::MultiplyingExpression")
vhdl_Factor = Class(name="vhdl::Factor")
vhdl_MemberExpression = Class(name="vhdl::MemberExpression")
vhdl_Member = Class(name="vhdl::Member")
vhdl_SliceExpression = Class(name="vhdl::SliceExpression")
vhdl_Value = Class(name="vhdl::Value")
vhdl_BuiltinFuncs = Class(name="vhdl::BuiltinFuncs")
vhdl_Boolean = Class(name="vhdl::Boolean")
vhdl_String = Class(name="vhdl::String")
vhdl_Char = Class(name="vhdl::Char")
vhdl_BitString = Class(name="vhdl::BitString")
vhdl_Others = Class(name="vhdl::Others")
vhdl_Open = Class(name="vhdl::Open")
vhdl_UnitValueExpression = Class(name="vhdl::UnitValueExpression")
ValueExpression = Class(name="ValueExpression")

# vhdl_DesignFile class attributes and methods

# vhdl_ContextItem class attributes and methods

# vhdl_LibraryUnit class attributes and methods
vhdl_LibraryUnit_name: Property = Property(name="name", type=StringType)
vhdl_LibraryUnit.attributes={vhdl_LibraryUnit_name}

# vhdl_UseClause class attributes and methods
vhdl_UseClause_importedNamespace: Property = Property(name="importedNamespace", type=StringType)
vhdl_UseClause.attributes={vhdl_UseClause_importedNamespace}

# ContextItem class attributes and methods

# vhdl_Library class attributes and methods
vhdl_Library_builtin_lib: Property = Property(name="builtin_lib", type=StringType)
vhdl_Library.attributes={vhdl_Library_builtin_lib}

# vhdl_LibraryClause class attributes and methods
vhdl_LibraryClause_name: Property = Property(name="name", type=StringType)
vhdl_LibraryClause.attributes={vhdl_LibraryClause_name}

# vhdl_Package class attributes and methods

# LibraryUnit class attributes and methods

# vhdl_package_declarative_item class attributes and methods

# vhdl_package_declarative_part class attributes and methods

# vhdl_Architecture class attributes and methods

# vhdl_Entity class attributes and methods

# vhdl_BlockDeclarativeItem class attributes and methods

# vhdl_ArchitectureStatement class attributes and methods
vhdl_ArchitectureStatement_label: Property = Property(name="label", type=StringType)
vhdl_ArchitectureStatement.attributes={vhdl_ArchitectureStatement_label}

# vhdl_Generics class attributes and methods

# vhdl_Ports class attributes and methods

# vhdl_Port class attributes and methods
vhdl_Port_mode: Property = Property(name="mode", type=StringType)
vhdl_Port_kind: Property = Property(name="kind", type=StringType)
vhdl_Port.attributes={vhdl_Port_kind, vhdl_Port_mode}

# Variable class attributes and methods

# vhdl_SubtypeIndication class attributes and methods
vhdl_SubtypeIndication_builtin_type: Property = Property(name="builtin_type", type=StringType)
vhdl_SubtypeIndication.attributes={vhdl_SubtypeIndication_builtin_type}

# vhdl_Expression class attributes and methods
vhdl_Expression_unary_operator: Property = Property(name="unary_operator", type=StringType)
vhdl_Expression_attribute: Property = Property(name="attribute", type=StringType)
vhdl_Expression.attributes={vhdl_Expression_attribute, vhdl_Expression_unary_operator}

# vhdl_Generic class attributes and methods

# vhdl_Alias class attributes and methods

# BlockDeclarativeItem class attributes and methods

# vhdl_SignalDeclaration class attributes and methods
vhdl_SignalDeclaration_kind: Property = Property(name="kind", type=StringType)
vhdl_SignalDeclaration.attributes={vhdl_SignalDeclaration_kind}

# package_declarative_item class attributes and methods

# vhdl_Signal class attributes and methods

# vhdl_VariableDeclaration class attributes and methods
vhdl_VariableDeclaration_shared: Property = Property(name="shared", type=BooleanType)
vhdl_VariableDeclaration.attributes={vhdl_VariableDeclaration_shared}

# vhdl_Var class attributes and methods

# vhdl_ConstantDeclaration class attributes and methods

# vhdl_Constant class attributes and methods

# vhdl_AttributeDeclaration class attributes and methods
vhdl_AttributeDeclaration_name: Property = Property(name="name", type=StringType)
vhdl_AttributeDeclaration_type_id: Property = Property(name="type_id", type=StringType)
vhdl_AttributeDeclaration_type_keyword: Property = Property(name="type_keyword", type=StringType)
vhdl_AttributeDeclaration.attributes={vhdl_AttributeDeclaration_type_keyword, vhdl_AttributeDeclaration_name, vhdl_AttributeDeclaration_type_id}

# vhdl_AttributeSpecification class attributes and methods
vhdl_AttributeSpecification_name: Property = Property(name="name", type=StringType)
vhdl_AttributeSpecification_entity: Property = Property(name="entity", type=StringType)
vhdl_AttributeSpecification_class: Property = Property(name="class", type=StringType)
vhdl_AttributeSpecification.attributes={vhdl_AttributeSpecification_class, vhdl_AttributeSpecification_name, vhdl_AttributeSpecification_entity}

# vhdl_Component class attributes and methods
vhdl_Component_name: Property = Property(name="name", type=StringType)
vhdl_Component.attributes={vhdl_Component_name}

# vhdl_ProcessStatement class attributes and methods
vhdl_ProcessStatement_postponed: Property = Property(name="postponed", type=BooleanType)
vhdl_ProcessStatement.attributes={vhdl_ProcessStatement_postponed}

# ArchitectureStatement class attributes and methods

# vhdl_IdList class attributes and methods

# vhdl_SequentialStatement class attributes and methods

# vhdl_ComponentInstantiationStatement class attributes and methods
vhdl_ComponentInstantiationStatement_name: Property = Property(name="name", type=StringType)
vhdl_ComponentInstantiationStatement.attributes={vhdl_ComponentInstantiationStatement_name}

# vhdl_GenericMap class attributes and methods

# vhdl_PortMap class attributes and methods

# vhdl_EntityInstantiationStatement class attributes and methods
vhdl_EntityInstantiationStatement_name: Property = Property(name="name", type=StringType)
vhdl_EntityInstantiationStatement.attributes={vhdl_EntityInstantiationStatement_name}

# vhdl_PortMapAssociation class attributes and methods
vhdl_PortMapAssociation_formal: Property = Property(name="formal", type=StringType)
vhdl_PortMapAssociation.attributes={vhdl_PortMapAssociation_formal}

# vhdl_GenericMapAssociation class attributes and methods
vhdl_GenericMapAssociation_formal: Property = Property(name="formal", type=StringType)
vhdl_GenericMapAssociation.attributes={vhdl_GenericMapAssociation_formal}

# vhdl_ConditionalSignalAssignmentStatement class attributes and methods
vhdl_ConditionalSignalAssignmentStatement_postponed: Property = Property(name="postponed", type=BooleanType)
vhdl_ConditionalSignalAssignmentStatement_guarded: Property = Property(name="guarded", type=BooleanType)
vhdl_ConditionalSignalAssignmentStatement.attributes={vhdl_ConditionalSignalAssignmentStatement_postponed, vhdl_ConditionalSignalAssignmentStatement_guarded}

# vhdl_ForGenerateStatement class attributes and methods

# vhdl_LoopVariable class attributes and methods

# vhdl_IfGenerateStatement class attributes and methods

# vhdl_WaitStatement class attributes and methods
vhdl_WaitStatement_label: Property = Property(name="label", type=StringType)
vhdl_WaitStatement.attributes={vhdl_WaitStatement_label}

# SequentialStatement class attributes and methods

# vhdl_IfStatement class attributes and methods
vhdl_IfStatement_label: Property = Property(name="label", type=StringType)
vhdl_IfStatement.attributes={vhdl_IfStatement_label}

# vhdl_IfStatementTest class attributes and methods

# vhdl_SequentialSignalAssignmentStatement class attributes and methods
vhdl_SequentialSignalAssignmentStatement_label: Property = Property(name="label", type=StringType)
vhdl_SequentialSignalAssignmentStatement_postponed: Property = Property(name="postponed", type=BooleanType)
vhdl_SequentialSignalAssignmentStatement_guarded: Property = Property(name="guarded", type=BooleanType)
vhdl_SequentialSignalAssignmentStatement.attributes={vhdl_SequentialSignalAssignmentStatement_guarded, vhdl_SequentialSignalAssignmentStatement_label, vhdl_SequentialSignalAssignmentStatement_postponed}

# vhdl_CaseStatement class attributes and methods
vhdl_CaseStatement_label: Property = Property(name="label", type=StringType)
vhdl_CaseStatement.attributes={vhdl_CaseStatement_label}

# vhdl_CaseAlternative class attributes and methods

# vhdl_LoopStatement class attributes and methods

# vhdl_IterationScheme class attributes and methods

# vhdl_WhileIterationScheme class attributes and methods

# IterationScheme class attributes and methods

# vhdl_ForIterationScheme class attributes and methods
vhdl_ForIterationScheme_variable: Property = Property(name="variable", type=StringType)
vhdl_ForIterationScheme.attributes={vhdl_ForIterationScheme_variable}

# vhdl_Type class attributes and methods
vhdl_Type_value: Property = Property(name="value", type=StringType)
vhdl_Type_name: Property = Property(name="name", type=StringType)
vhdl_Type.attributes={vhdl_Type_value, vhdl_Type_name}

# Expression class attributes and methods

# vhdl_SubtypeDeclaration class attributes and methods

# Type class attributes and methods

# vhdl_TypeDeclaration class attributes and methods

# vhdl_TypeDefinition class attributes and methods

# vhdl_AccessTypeDefinition class attributes and methods

# TypeDefinition class attributes and methods

# vhdl_CompositeTypeDefinition class attributes and methods

# vhdl_ArrayTypeDefinition class attributes and methods

# CompositeTypeDefinition class attributes and methods

# vhdl_UnconstrainedArrayTypeDefinition class attributes and methods
vhdl_UnconstrainedArrayTypeDefinition_index: Property = Property(name="index", type=StringType)
vhdl_UnconstrainedArrayTypeDefinition.attributes={vhdl_UnconstrainedArrayTypeDefinition_index}

# ArrayTypeDefinition class attributes and methods

# vhdl_ConstrainedArrayTypeDefinition class attributes and methods

# vhdl_EnumerationTypeDefinition class attributes and methods
vhdl_EnumerationTypeDefinition_literal: Property = Property(name="literal", type=StringType)
vhdl_EnumerationTypeDefinition.attributes={vhdl_EnumerationTypeDefinition_literal}

# vhdl_FileTypeDefinition class attributes and methods
vhdl_FileTypeDefinition_type: Property = Property(name="type", type=StringType)
vhdl_FileTypeDefinition.attributes={vhdl_FileTypeDefinition_type}

# vhdl_RecordField class attributes and methods
vhdl_RecordField_name: Property = Property(name="name", type=StringType)
vhdl_RecordField.attributes={vhdl_RecordField_name}

# vhdl_RecordTypeDefinition class attributes and methods

# vhdl_Variable class attributes and methods
vhdl_Variable_name: Property = Property(name="name", type=StringType)
vhdl_Variable.attributes={vhdl_Variable_name}

# vhdl_ValueExpression class attributes and methods
vhdl_ValueExpression_value: Property = Property(name="value", type=StringType)
vhdl_ValueExpression.attributes={vhdl_ValueExpression_value}

# vhdl_ConditionalWaveformExpression class attributes and methods

# vhdl_RangeExpression class attributes and methods
vhdl_RangeExpression_direction: Property = Property(name="direction", type=StringType)
vhdl_RangeExpression_operator: Property = Property(name="operator", type=StringType)
vhdl_RangeExpression.attributes={vhdl_RangeExpression_operator, vhdl_RangeExpression_direction}

# vhdl_MultiExpression class attributes and methods

# vhdl_LogicalExpression class attributes and methods
vhdl_LogicalExpression_operator: Property = Property(name="operator", type=StringType)
vhdl_LogicalExpression.attributes={vhdl_LogicalExpression_operator}

# vhdl_RelationalExpression class attributes and methods
vhdl_RelationalExpression_operator: Property = Property(name="operator", type=StringType)
vhdl_RelationalExpression.attributes={vhdl_RelationalExpression_operator}

# vhdl_ChoiceExpression class attributes and methods

# vhdl_ShiftExpression class attributes and methods
vhdl_ShiftExpression_operator: Property = Property(name="operator", type=StringType)
vhdl_ShiftExpression.attributes={vhdl_ShiftExpression_operator}

# vhdl_AddingExpression class attributes and methods
vhdl_AddingExpression_operator: Property = Property(name="operator", type=StringType)
vhdl_AddingExpression.attributes={vhdl_AddingExpression_operator}

# vhdl_MultiplyingExpression class attributes and methods
vhdl_MultiplyingExpression_operator: Property = Property(name="operator", type=StringType)
vhdl_MultiplyingExpression.attributes={vhdl_MultiplyingExpression_operator}

# vhdl_Factor class attributes and methods

# vhdl_MemberExpression class attributes and methods

# vhdl_Member class attributes and methods

# vhdl_SliceExpression class attributes and methods

# vhdl_Value class attributes and methods

# vhdl_BuiltinFuncs class attributes and methods
vhdl_BuiltinFuncs_value: Property = Property(name="value", type=StringType)
vhdl_BuiltinFuncs.attributes={vhdl_BuiltinFuncs_value}

# vhdl_Boolean class attributes and methods
vhdl_Boolean_value: Property = Property(name="value", type=StringType)
vhdl_Boolean.attributes={vhdl_Boolean_value}

# vhdl_String class attributes and methods
vhdl_String_value: Property = Property(name="value", type=StringType)
vhdl_String.attributes={vhdl_String_value}

# vhdl_Char class attributes and methods
vhdl_Char_value: Property = Property(name="value", type=StringType)
vhdl_Char.attributes={vhdl_Char_value}

# vhdl_BitString class attributes and methods
vhdl_BitString_value: Property = Property(name="value", type=StringType)
vhdl_BitString.attributes={vhdl_BitString_value}

# vhdl_Others class attributes and methods
vhdl_Others_value: Property = Property(name="value", type=StringType)
vhdl_Others.attributes={vhdl_Others_value}

# vhdl_Open class attributes and methods
vhdl_Open_value: Property = Property(name="value", type=StringType)
vhdl_Open.attributes={vhdl_Open_value}

# vhdl_UnitValueExpression class attributes and methods
vhdl_UnitValueExpression_unit: Property = Property(name="unit", type=StringType)
vhdl_UnitValueExpression.attributes={vhdl_UnitValueExpression_unit}

# ValueExpression class attributes and methods

# Relationships
ContextItems0: BinaryAssociation = BinaryAssociation(
    name="ContextItems0",
    ends={
        Property(name="vhdl_ContextItem", type=vhdl_DesignFile, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_DesignFile", type=vhdl_ContextItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
LibraryUnits1: BinaryAssociation = BinaryAssociation(
    name="LibraryUnits1",
    ends={
        Property(name="vhdl_LibraryUnit", type=vhdl_DesignFile, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_DesignFile2", type=vhdl_LibraryUnit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
lib3: BinaryAssociation = BinaryAssociation(
    name="lib3",
    ends={
        Property(name="vhdl_Library", type=vhdl_UseClause, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_UseClause", type=vhdl_Library, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
custom_lib4: BinaryAssociation = BinaryAssociation(
    name="custom_lib4",
    ends={
        Property(name="vhdl_LibraryClause", type=vhdl_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_Library5", type=vhdl_LibraryClause, multiplicity=Multiplicity(0, 1))
    }
)
package_declarative_item6: BinaryAssociation = BinaryAssociation(
    name="package_declarative_item6",
    ends={
        Property(name="vhdl_package_declarative_item", type=vhdl_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_Package", type=vhdl_package_declarative_item, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
package_declarative_item7: BinaryAssociation = BinaryAssociation(
    name="package_declarative_item7",
    ends={
        Property(name="vhdl_package_declarative_item8", type=vhdl_package_declarative_part, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_package_declarative_part", type=vhdl_package_declarative_item, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entity9: BinaryAssociation = BinaryAssociation(
    name="entity9",
    ends={
        Property(name="vhdl_Entity", type=vhdl_Architecture, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_Architecture", type=vhdl_Entity, multiplicity=Multiplicity(0, 1))
    }
)
declaration10: BinaryAssociation = BinaryAssociation(
    name="declaration10",
    ends={
        Property(name="vhdl_BlockDeclarativeItem", type=vhdl_Architecture, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_Architecture11", type=vhdl_BlockDeclarativeItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statement12: BinaryAssociation = BinaryAssociation(
    name="statement12",
    ends={
        Property(name="vhdl_ArchitectureStatement", type=vhdl_Architecture, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_Architecture13", type=vhdl_ArchitectureStatement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
generics14: BinaryAssociation = BinaryAssociation(
    name="generics14",
    ends={
        Property(name="vhdl_Generics", type=vhdl_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_Entity15", type=vhdl_Generics, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ports16: BinaryAssociation = BinaryAssociation(
    name="ports16",
    ends={
        Property(name="vhdl_Ports", type=vhdl_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_Entity17", type=vhdl_Ports, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declaration18: BinaryAssociation = BinaryAssociation(
    name="declaration18",
    ends={
        Property(name="vhdl_Port", type=vhdl_Ports, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_Ports19", type=vhdl_Port, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type20: BinaryAssociation = BinaryAssociation(
    name="type20",
    ends={
        Property(name="vhdl_SubtypeIndication", type=vhdl_Port, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_Port21", type=vhdl_SubtypeIndication, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type26: BinaryAssociation = BinaryAssociation(
    name="type26",
    ends={
        Property(name="vhdl_SubtypeIndication28", type=vhdl_Generic, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_Generic27", type=vhdl_SubtypeIndication, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initial22: BinaryAssociation = BinaryAssociation(
    name="initial22",
    ends={
        Property(name="vhdl_Expression", type=vhdl_Port, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_Port23", type=vhdl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declaration24: BinaryAssociation = BinaryAssociation(
    name="declaration24",
    ends={
        Property(name="vhdl_Generic", type=vhdl_Generics, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_Generics25", type=vhdl_Generic, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initial29: BinaryAssociation = BinaryAssociation(
    name="initial29",
    ends={
        Property(name="vhdl_Expression31", type=vhdl_Generic, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_Generic30", type=vhdl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
alias32: BinaryAssociation = BinaryAssociation(
    name="alias32",
    ends={
        Property(name="vhdl_SubtypeIndication33", type=vhdl_Alias, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_Alias", type=vhdl_SubtypeIndication, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
is34: BinaryAssociation = BinaryAssociation(
    name="is34",
    ends={
        Property(name="vhdl_Expression36", type=vhdl_Alias, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_Alias35", type=vhdl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sig37: BinaryAssociation = BinaryAssociation(
    name="sig37",
    ends={
        Property(name="vhdl_Signal", type=vhdl_SignalDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_SignalDeclaration", type=vhdl_Signal, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type38: BinaryAssociation = BinaryAssociation(
    name="type38",
    ends={
        Property(name="vhdl_SubtypeIndication40", type=vhdl_SignalDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_SignalDeclaration39", type=vhdl_SubtypeIndication, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initial41: BinaryAssociation = BinaryAssociation(
    name="initial41",
    ends={
        Property(name="vhdl_Expression43", type=vhdl_SignalDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_SignalDeclaration42", type=vhdl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
var44: BinaryAssociation = BinaryAssociation(
    name="var44",
    ends={
        Property(name="vhdl_Var", type=vhdl_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_VariableDeclaration", type=vhdl_Var, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type45: BinaryAssociation = BinaryAssociation(
    name="type45",
    ends={
        Property(name="vhdl_SubtypeIndication47", type=vhdl_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_VariableDeclaration46", type=vhdl_SubtypeIndication, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initial48: BinaryAssociation = BinaryAssociation(
    name="initial48",
    ends={
        Property(name="vhdl_Expression50", type=vhdl_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_VariableDeclaration49", type=vhdl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constant51: BinaryAssociation = BinaryAssociation(
    name="constant51",
    ends={
        Property(name="vhdl_Constant", type=vhdl_ConstantDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_ConstantDeclaration", type=vhdl_Constant, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type52: BinaryAssociation = BinaryAssociation(
    name="type52",
    ends={
        Property(name="vhdl_SubtypeIndication54", type=vhdl_ConstantDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_ConstantDeclaration53", type=vhdl_SubtypeIndication, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initial55: BinaryAssociation = BinaryAssociation(
    name="initial55",
    ends={
        Property(name="vhdl_Expression57", type=vhdl_ConstantDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_ConstantDeclaration56", type=vhdl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
is58: BinaryAssociation = BinaryAssociation(
    name="is58",
    ends={
        Property(name="vhdl_Expression59", type=vhdl_AttributeSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_AttributeSpecification", type=vhdl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
generic60: BinaryAssociation = BinaryAssociation(
    name="generic60",
    ends={
        Property(name="vhdl_Generics61", type=vhdl_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_Component", type=vhdl_Generics, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
port62: BinaryAssociation = BinaryAssociation(
    name="port62",
    ends={
        Property(name="vhdl_Ports64", type=vhdl_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_Component63", type=vhdl_Ports, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sensitivity65: BinaryAssociation = BinaryAssociation(
    name="sensitivity65",
    ends={
        Property(name="vhdl_IdList", type=vhdl_ProcessStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_ProcessStatement", type=vhdl_IdList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statement66: BinaryAssociation = BinaryAssociation(
    name="statement66",
    ends={
        Property(name="vhdl_SequentialStatement", type=vhdl_ProcessStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_ProcessStatement67", type=vhdl_SequentialStatement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
genericMap68: BinaryAssociation = BinaryAssociation(
    name="genericMap68",
    ends={
        Property(name="vhdl_GenericMap", type=vhdl_ComponentInstantiationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_ComponentInstantiationStatement", type=vhdl_GenericMap, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
portMap69: BinaryAssociation = BinaryAssociation(
    name="portMap69",
    ends={
        Property(name="vhdl_PortMap", type=vhdl_ComponentInstantiationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_ComponentInstantiationStatement70", type=vhdl_PortMap, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lib71: BinaryAssociation = BinaryAssociation(
    name="lib71",
    ends={
        Property(name="vhdl_Library72", type=vhdl_EntityInstantiationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_EntityInstantiationStatement", type=vhdl_Library, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
genericMap73: BinaryAssociation = BinaryAssociation(
    name="genericMap73",
    ends={
        Property(name="vhdl_GenericMap75", type=vhdl_EntityInstantiationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_EntityInstantiationStatement74", type=vhdl_GenericMap, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
portMap76: BinaryAssociation = BinaryAssociation(
    name="portMap76",
    ends={
        Property(name="vhdl_PortMap78", type=vhdl_EntityInstantiationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_EntityInstantiationStatement77", type=vhdl_PortMap, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
association79: BinaryAssociation = BinaryAssociation(
    name="association79",
    ends={
        Property(name="vhdl_PortMapAssociation", type=vhdl_PortMap, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_PortMap80", type=vhdl_PortMapAssociation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actual81: BinaryAssociation = BinaryAssociation(
    name="actual81",
    ends={
        Property(name="vhdl_Expression83", type=vhdl_PortMapAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_PortMapAssociation82", type=vhdl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
association84: BinaryAssociation = BinaryAssociation(
    name="association84",
    ends={
        Property(name="vhdl_GenericMapAssociation", type=vhdl_GenericMap, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_GenericMap85", type=vhdl_GenericMapAssociation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actual86: BinaryAssociation = BinaryAssociation(
    name="actual86",
    ends={
        Property(name="vhdl_Expression88", type=vhdl_GenericMapAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_GenericMapAssociation87", type=vhdl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target89: BinaryAssociation = BinaryAssociation(
    name="target89",
    ends={
        Property(name="vhdl_Expression90", type=vhdl_ConditionalSignalAssignmentStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_ConditionalSignalAssignmentStatement", type=vhdl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
waveform91: BinaryAssociation = BinaryAssociation(
    name="waveform91",
    ends={
        Property(name="vhdl_Expression93", type=vhdl_ConditionalSignalAssignmentStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_ConditionalSignalAssignmentStatement92", type=vhdl_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
declaration118: BinaryAssociation = BinaryAssociation(
    name="declaration118",
    ends={
        Property(name="vhdl_BlockDeclarativeItem120", type=vhdl_IfGenerateStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_IfGenerateStatement119", type=vhdl_BlockDeclarativeItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exp98: BinaryAssociation = BinaryAssociation(
    name="exp98",
    ends={
        Property(name="vhdl_Expression99", type=vhdl_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_Expression97", type=vhdl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
after101: BinaryAssociation = BinaryAssociation(
    name="after101",
    ends={
        Property(name="vhdl_Expression102", type=vhdl_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_Expression100", type=vhdl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression104: BinaryAssociation = BinaryAssociation(
    name="expression104",
    ends={
        Property(name="vhdl_Expression105", type=vhdl_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_Expression103", type=vhdl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
var106: BinaryAssociation = BinaryAssociation(
    name="var106",
    ends={
        Property(name="vhdl_LoopVariable", type=vhdl_ForGenerateStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_ForGenerateStatement", type=vhdl_LoopVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
range107: BinaryAssociation = BinaryAssociation(
    name="range107",
    ends={
        Property(name="vhdl_Expression109", type=vhdl_ForGenerateStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_ForGenerateStatement108", type=vhdl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declaration110: BinaryAssociation = BinaryAssociation(
    name="declaration110",
    ends={
        Property(name="vhdl_BlockDeclarativeItem112", type=vhdl_ForGenerateStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_ForGenerateStatement111", type=vhdl_BlockDeclarativeItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statement113: BinaryAssociation = BinaryAssociation(
    name="statement113",
    ends={
        Property(name="vhdl_ArchitectureStatement115", type=vhdl_ForGenerateStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_ForGenerateStatement114", type=vhdl_ArchitectureStatement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition116: BinaryAssociation = BinaryAssociation(
    name="condition116",
    ends={
        Property(name="vhdl_Expression117", type=vhdl_IfGenerateStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_IfGenerateStatement", type=vhdl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
waveform95: BinaryAssociation = BinaryAssociation(
    name="waveform95",
    ends={
        Property(name="vhdl_Expression96", type=vhdl_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_Expression94", type=vhdl_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statement121: BinaryAssociation = BinaryAssociation(
    name="statement121",
    ends={
        Property(name="vhdl_ArchitectureStatement123", type=vhdl_IfGenerateStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_IfGenerateStatement122", type=vhdl_ArchitectureStatement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sensitivity124: BinaryAssociation = BinaryAssociation(
    name="sensitivity124",
    ends={
        Property(name="vhdl_IdList125", type=vhdl_WaitStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_WaitStatement", type=vhdl_IdList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
until126: BinaryAssociation = BinaryAssociation(
    name="until126",
    ends={
        Property(name="vhdl_Expression128", type=vhdl_WaitStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_WaitStatement127", type=vhdl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
time129: BinaryAssociation = BinaryAssociation(
    name="time129",
    ends={
        Property(name="vhdl_Expression131", type=vhdl_WaitStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_WaitStatement130", type=vhdl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
test132: BinaryAssociation = BinaryAssociation(
    name="test132",
    ends={
        Property(name="vhdl_IfStatementTest", type=vhdl_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_IfStatement", type=vhdl_IfStatementTest, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statement133: BinaryAssociation = BinaryAssociation(
    name="statement133",
    ends={
        Property(name="vhdl_SequentialStatement135", type=vhdl_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_IfStatement134", type=vhdl_SequentialStatement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition136: BinaryAssociation = BinaryAssociation(
    name="condition136",
    ends={
        Property(name="vhdl_Expression138", type=vhdl_IfStatementTest, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_IfStatementTest137", type=vhdl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statement139: BinaryAssociation = BinaryAssociation(
    name="statement139",
    ends={
        Property(name="vhdl_SequentialStatement141", type=vhdl_IfStatementTest, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_IfStatementTest140", type=vhdl_SequentialStatement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
case142: BinaryAssociation = BinaryAssociation(
    name="case142",
    ends={
        Property(name="vhdl_Expression143", type=vhdl_CaseStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_CaseStatement", type=vhdl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
when144: BinaryAssociation = BinaryAssociation(
    name="when144",
    ends={
        Property(name="vhdl_CaseAlternative", type=vhdl_CaseStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_CaseStatement145", type=vhdl_CaseAlternative, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
choice146: BinaryAssociation = BinaryAssociation(
    name="choice146",
    ends={
        Property(name="vhdl_Expression148", type=vhdl_CaseAlternative, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_CaseAlternative147", type=vhdl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statement149: BinaryAssociation = BinaryAssociation(
    name="statement149",
    ends={
        Property(name="vhdl_SequentialStatement151", type=vhdl_CaseAlternative, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_CaseAlternative150", type=vhdl_SequentialStatement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
var152: BinaryAssociation = BinaryAssociation(
    name="var152",
    ends={
        Property(name="vhdl_LoopVariable153", type=vhdl_LoopStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_LoopStatement", type=vhdl_LoopVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
range154: BinaryAssociation = BinaryAssociation(
    name="range154",
    ends={
        Property(name="vhdl_Expression156", type=vhdl_LoopStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_LoopStatement155", type=vhdl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statements157: BinaryAssociation = BinaryAssociation(
    name="statements157",
    ends={
        Property(name="vhdl_SequentialStatement159", type=vhdl_LoopStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_LoopStatement158", type=vhdl_SequentialStatement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target160: BinaryAssociation = BinaryAssociation(
    name="target160",
    ends={
        Property(name="vhdl_Expression161", type=vhdl_SequentialSignalAssignmentStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_SequentialSignalAssignmentStatement", type=vhdl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
waveform162: BinaryAssociation = BinaryAssociation(
    name="waveform162",
    ends={
        Property(name="vhdl_Expression164", type=vhdl_SequentialSignalAssignmentStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_SequentialSignalAssignmentStatement163", type=vhdl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition165: BinaryAssociation = BinaryAssociation(
    name="condition165",
    ends={
        Property(name="vhdl_Expression166", type=vhdl_WhileIterationScheme, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_WhileIterationScheme", type=vhdl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
in167: BinaryAssociation = BinaryAssociation(
    name="in167",
    ends={
        Property(name="vhdl_Expression168", type=vhdl_ForIterationScheme, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_ForIterationScheme", type=vhdl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
custom_type169: BinaryAssociation = BinaryAssociation(
    name="custom_type169",
    ends={
        Property(name="vhdl_Type", type=vhdl_SubtypeIndication, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_SubtypeIndication170", type=vhdl_Type, multiplicity=Multiplicity(0, 1))
    }
)
constraint171: BinaryAssociation = BinaryAssociation(
    name="constraint171",
    ends={
        Property(name="vhdl_Expression173", type=vhdl_SubtypeIndication, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_SubtypeIndication172", type=vhdl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type174: BinaryAssociation = BinaryAssociation(
    name="type174",
    ends={
        Property(name="vhdl_SubtypeIndication175", type=vhdl_SubtypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_SubtypeDeclaration", type=vhdl_SubtypeIndication, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
is176: BinaryAssociation = BinaryAssociation(
    name="is176",
    ends={
        Property(name="vhdl_TypeDefinition", type=vhdl_TypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_TypeDeclaration", type=vhdl_TypeDefinition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type177: BinaryAssociation = BinaryAssociation(
    name="type177",
    ends={
        Property(name="vhdl_SubtypeIndication178", type=vhdl_AccessTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_AccessTypeDefinition", type=vhdl_SubtypeIndication, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type179: BinaryAssociation = BinaryAssociation(
    name="type179",
    ends={
        Property(name="vhdl_SubtypeIndication180", type=vhdl_ArrayTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_ArrayTypeDefinition", type=vhdl_SubtypeIndication, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constraint181: BinaryAssociation = BinaryAssociation(
    name="constraint181",
    ends={
        Property(name="vhdl_Expression182", type=vhdl_ConstrainedArrayTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_ConstrainedArrayTypeDefinition", type=vhdl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
field183: BinaryAssociation = BinaryAssociation(
    name="field183",
    ends={
        Property(name="vhdl_RecordField", type=vhdl_RecordTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_RecordTypeDefinition", type=vhdl_RecordField, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type184: BinaryAssociation = BinaryAssociation(
    name="type184",
    ends={
        Property(name="vhdl_SubtypeIndication186", type=vhdl_RecordTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_RecordTypeDefinition185", type=vhdl_SubtypeIndication, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value188: BinaryAssociation = BinaryAssociation(
    name="value188",
    ends={
        Property(name="vhdl_Variable", type=vhdl_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_Variable187", type=vhdl_Variable, multiplicity=Multiplicity(0, 1))
    }
)
id189: BinaryAssociation = BinaryAssociation(
    name="id189",
    ends={
        Property(name="vhdl_Expression191", type=vhdl_IdList, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_IdList190", type=vhdl_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
choice192: BinaryAssociation = BinaryAssociation(
    name="choice192",
    ends={
        Property(name="vhdl_ConditionalWaveformExpression", type=vhdl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="vhdl_Expression193", type=vhdl_ConditionalWaveformExpression, multiplicity=Multiplicity(1, 1))
    }
)
left194: BinaryAssociation = BinaryAssociation(
    name="left194",
    ends={
        Property(name="vhdl_Expression195", type=vhdl_RangeExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_RangeExpression", type=vhdl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right196: BinaryAssociation = BinaryAssociation(
    name="right196",
    ends={
        Property(name="vhdl_Expression198", type=vhdl_RangeExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_RangeExpression197", type=vhdl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left199: BinaryAssociation = BinaryAssociation(
    name="left199",
    ends={
        Property(name="vhdl_Expression200", type=vhdl_LogicalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_LogicalExpression", type=vhdl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right201: BinaryAssociation = BinaryAssociation(
    name="right201",
    ends={
        Property(name="vhdl_Expression203", type=vhdl_LogicalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_LogicalExpression202", type=vhdl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left204: BinaryAssociation = BinaryAssociation(
    name="left204",
    ends={
        Property(name="vhdl_Expression205", type=vhdl_RelationalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_RelationalExpression", type=vhdl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right206: BinaryAssociation = BinaryAssociation(
    name="right206",
    ends={
        Property(name="vhdl_Expression208", type=vhdl_RelationalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_RelationalExpression207", type=vhdl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left209: BinaryAssociation = BinaryAssociation(
    name="left209",
    ends={
        Property(name="vhdl_Expression210", type=vhdl_ChoiceExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_ChoiceExpression", type=vhdl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right211: BinaryAssociation = BinaryAssociation(
    name="right211",
    ends={
        Property(name="vhdl_Expression213", type=vhdl_ChoiceExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_ChoiceExpression212", type=vhdl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left214: BinaryAssociation = BinaryAssociation(
    name="left214",
    ends={
        Property(name="vhdl_Expression215", type=vhdl_ShiftExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_ShiftExpression", type=vhdl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right216: BinaryAssociation = BinaryAssociation(
    name="right216",
    ends={
        Property(name="vhdl_Expression218", type=vhdl_ShiftExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_ShiftExpression217", type=vhdl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left219: BinaryAssociation = BinaryAssociation(
    name="left219",
    ends={
        Property(name="vhdl_Expression220", type=vhdl_AddingExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_AddingExpression", type=vhdl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right221: BinaryAssociation = BinaryAssociation(
    name="right221",
    ends={
        Property(name="vhdl_Expression223", type=vhdl_AddingExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_AddingExpression222", type=vhdl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left224: BinaryAssociation = BinaryAssociation(
    name="left224",
    ends={
        Property(name="vhdl_Expression225", type=vhdl_MultiplyingExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_MultiplyingExpression", type=vhdl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right226: BinaryAssociation = BinaryAssociation(
    name="right226",
    ends={
        Property(name="vhdl_Expression228", type=vhdl_MultiplyingExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_MultiplyingExpression227", type=vhdl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left229: BinaryAssociation = BinaryAssociation(
    name="left229",
    ends={
        Property(name="vhdl_Expression230", type=vhdl_Factor, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_Factor", type=vhdl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right231: BinaryAssociation = BinaryAssociation(
    name="right231",
    ends={
        Property(name="vhdl_Expression233", type=vhdl_Factor, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_Factor232", type=vhdl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left234: BinaryAssociation = BinaryAssociation(
    name="left234",
    ends={
        Property(name="vhdl_Expression235", type=vhdl_MemberExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_MemberExpression", type=vhdl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
member239: BinaryAssociation = BinaryAssociation(
    name="member239",
    ends={
        Property(name="vhdl_RecordField240", type=vhdl_Member, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_Member", type=vhdl_RecordField, multiplicity=Multiplicity(0, 1))
    }
)
slice241: BinaryAssociation = BinaryAssociation(
    name="slice241",
    ends={
        Property(name="vhdl_Expression243", type=vhdl_Member, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_Member242", type=vhdl_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
left244: BinaryAssociation = BinaryAssociation(
    name="left244",
    ends={
        Property(name="vhdl_Expression245", type=vhdl_SliceExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_SliceExpression", type=vhdl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
slice246: BinaryAssociation = BinaryAssociation(
    name="slice246",
    ends={
        Property(name="vhdl_Expression248", type=vhdl_SliceExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_SliceExpression247", type=vhdl_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value249: BinaryAssociation = BinaryAssociation(
    name="value249",
    ends={
        Property(name="vhdl_ValueExpression", type=vhdl_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_Value", type=vhdl_ValueExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right236: BinaryAssociation = BinaryAssociation(
    name="right236",
    ends={
        Property(name="vhdl_Expression238", type=vhdl_MemberExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="vhdl_MemberExpression237", type=vhdl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_vhdl_UseClause_ContextItem = Generalization(general=ContextItem, specific=vhdl_UseClause)
gen_vhdl_LibraryClause_ContextItem = Generalization(general=ContextItem, specific=vhdl_LibraryClause)
gen_vhdl_Package_LibraryUnit = Generalization(general=LibraryUnit, specific=vhdl_Package)
gen_vhdl_Architecture_LibraryUnit = Generalization(general=LibraryUnit, specific=vhdl_Architecture)
gen_vhdl_Entity_LibraryUnit = Generalization(general=LibraryUnit, specific=vhdl_Entity)
gen_vhdl_Port_Variable = Generalization(general=Variable, specific=vhdl_Port)
gen_vhdl_Generic_Variable = Generalization(general=Variable, specific=vhdl_Generic)
gen_vhdl_Alias_BlockDeclarativeItem = Generalization(general=BlockDeclarativeItem, specific=vhdl_Alias)
gen_vhdl_Alias_Variable = Generalization(general=Variable, specific=vhdl_Alias)
gen_vhdl_SignalDeclaration_package_declarative_item = Generalization(general=package_declarative_item, specific=vhdl_SignalDeclaration)
gen_vhdl_SignalDeclaration_BlockDeclarativeItem = Generalization(general=BlockDeclarativeItem, specific=vhdl_SignalDeclaration)
gen_vhdl_Signal_Variable = Generalization(general=Variable, specific=vhdl_Signal)
gen_vhdl_VariableDeclaration_package_declarative_item = Generalization(general=package_declarative_item, specific=vhdl_VariableDeclaration)
gen_vhdl_VariableDeclaration_BlockDeclarativeItem = Generalization(general=BlockDeclarativeItem, specific=vhdl_VariableDeclaration)
gen_vhdl_Var_Variable = Generalization(general=Variable, specific=vhdl_Var)
gen_vhdl_ConstantDeclaration_package_declarative_item = Generalization(general=package_declarative_item, specific=vhdl_ConstantDeclaration)
gen_vhdl_ConstantDeclaration_BlockDeclarativeItem = Generalization(general=BlockDeclarativeItem, specific=vhdl_ConstantDeclaration)
gen_vhdl_Constant_Variable = Generalization(general=Variable, specific=vhdl_Constant)
gen_vhdl_AttributeDeclaration_BlockDeclarativeItem = Generalization(general=BlockDeclarativeItem, specific=vhdl_AttributeDeclaration)
gen_vhdl_AttributeSpecification_BlockDeclarativeItem = Generalization(general=BlockDeclarativeItem, specific=vhdl_AttributeSpecification)
gen_vhdl_Component_package_declarative_item = Generalization(general=package_declarative_item, specific=vhdl_Component)
gen_vhdl_Component_BlockDeclarativeItem = Generalization(general=BlockDeclarativeItem, specific=vhdl_Component)
gen_vhdl_ProcessStatement_ArchitectureStatement = Generalization(general=ArchitectureStatement, specific=vhdl_ProcessStatement)
gen_vhdl_ComponentInstantiationStatement_ArchitectureStatement = Generalization(general=ArchitectureStatement, specific=vhdl_ComponentInstantiationStatement)
gen_vhdl_EntityInstantiationStatement_ArchitectureStatement = Generalization(general=ArchitectureStatement, specific=vhdl_EntityInstantiationStatement)
gen_vhdl_ConditionalSignalAssignmentStatement_ArchitectureStatement = Generalization(general=ArchitectureStatement, specific=vhdl_ConditionalSignalAssignmentStatement)
gen_vhdl_ForGenerateStatement_ArchitectureStatement = Generalization(general=ArchitectureStatement, specific=vhdl_ForGenerateStatement)
gen_vhdl_IfGenerateStatement_ArchitectureStatement = Generalization(general=ArchitectureStatement, specific=vhdl_IfGenerateStatement)
gen_vhdl_WaitStatement_SequentialStatement = Generalization(general=SequentialStatement, specific=vhdl_WaitStatement)
gen_vhdl_IfStatement_SequentialStatement = Generalization(general=SequentialStatement, specific=vhdl_IfStatement)
gen_vhdl_SequentialSignalAssignmentStatement_SequentialStatement = Generalization(general=SequentialStatement, specific=vhdl_SequentialSignalAssignmentStatement)
gen_vhdl_CaseStatement_SequentialStatement = Generalization(general=SequentialStatement, specific=vhdl_CaseStatement)
gen_vhdl_LoopVariable_Variable = Generalization(general=Variable, specific=vhdl_LoopVariable)
gen_vhdl_LoopStatement_SequentialStatement = Generalization(general=SequentialStatement, specific=vhdl_LoopStatement)
gen_vhdl_WhileIterationScheme_IterationScheme = Generalization(general=IterationScheme, specific=vhdl_WhileIterationScheme)
gen_vhdl_ForIterationScheme_IterationScheme = Generalization(general=IterationScheme, specific=vhdl_ForIterationScheme)
gen_vhdl_Type_package_declarative_item = Generalization(general=package_declarative_item, specific=vhdl_Type)
gen_vhdl_Type_BlockDeclarativeItem = Generalization(general=BlockDeclarativeItem, specific=vhdl_Type)
gen_vhdl_Type_Expression = Generalization(general=Expression, specific=vhdl_Type)
gen_vhdl_SubtypeDeclaration_Type = Generalization(general=Type, specific=vhdl_SubtypeDeclaration)
gen_vhdl_TypeDeclaration_Type = Generalization(general=Type, specific=vhdl_TypeDeclaration)
gen_vhdl_AccessTypeDefinition_TypeDefinition = Generalization(general=TypeDefinition, specific=vhdl_AccessTypeDefinition)
gen_vhdl_CompositeTypeDefinition_TypeDefinition = Generalization(general=TypeDefinition, specific=vhdl_CompositeTypeDefinition)
gen_vhdl_ArrayTypeDefinition_CompositeTypeDefinition = Generalization(general=CompositeTypeDefinition, specific=vhdl_ArrayTypeDefinition)
gen_vhdl_UnconstrainedArrayTypeDefinition_ArrayTypeDefinition = Generalization(general=ArrayTypeDefinition, specific=vhdl_UnconstrainedArrayTypeDefinition)
gen_vhdl_ConstrainedArrayTypeDefinition_ArrayTypeDefinition = Generalization(general=ArrayTypeDefinition, specific=vhdl_ConstrainedArrayTypeDefinition)
gen_vhdl_EnumerationTypeDefinition_TypeDefinition = Generalization(general=TypeDefinition, specific=vhdl_EnumerationTypeDefinition)
gen_vhdl_FileTypeDefinition_TypeDefinition = Generalization(general=TypeDefinition, specific=vhdl_FileTypeDefinition)
gen_vhdl_RecordTypeDefinition_CompositeTypeDefinition = Generalization(general=CompositeTypeDefinition, specific=vhdl_RecordTypeDefinition)
gen_vhdl_Variable_Expression = Generalization(general=Expression, specific=vhdl_Variable)
gen_vhdl_ConditionalWaveformExpression_Expression = Generalization(general=Expression, specific=vhdl_ConditionalWaveformExpression)
gen_vhdl_RangeExpression_Expression = Generalization(general=Expression, specific=vhdl_RangeExpression)
gen_vhdl_MultiExpression_Expression = Generalization(general=Expression, specific=vhdl_MultiExpression)
gen_vhdl_LogicalExpression_Expression = Generalization(general=Expression, specific=vhdl_LogicalExpression)
gen_vhdl_RelationalExpression_Expression = Generalization(general=Expression, specific=vhdl_RelationalExpression)
gen_vhdl_ChoiceExpression_Expression = Generalization(general=Expression, specific=vhdl_ChoiceExpression)
gen_vhdl_ShiftExpression_Expression = Generalization(general=Expression, specific=vhdl_ShiftExpression)
gen_vhdl_AddingExpression_Expression = Generalization(general=Expression, specific=vhdl_AddingExpression)
gen_vhdl_MultiplyingExpression_Expression = Generalization(general=Expression, specific=vhdl_MultiplyingExpression)
gen_vhdl_Factor_Expression = Generalization(general=Expression, specific=vhdl_Factor)
gen_vhdl_MemberExpression_Expression = Generalization(general=Expression, specific=vhdl_MemberExpression)
gen_vhdl_Member_Expression = Generalization(general=Expression, specific=vhdl_Member)
gen_vhdl_SliceExpression_Expression = Generalization(general=Expression, specific=vhdl_SliceExpression)
gen_vhdl_Value_Expression = Generalization(general=Expression, specific=vhdl_Value)
gen_vhdl_BuiltinFuncs_Expression = Generalization(general=Expression, specific=vhdl_BuiltinFuncs)
gen_vhdl_Boolean_Expression = Generalization(general=Expression, specific=vhdl_Boolean)
gen_vhdl_String_Expression = Generalization(general=Expression, specific=vhdl_String)
gen_vhdl_Char_Expression = Generalization(general=Expression, specific=vhdl_Char)
gen_vhdl_BitString_Expression = Generalization(general=Expression, specific=vhdl_BitString)
gen_vhdl_Others_Expression = Generalization(general=Expression, specific=vhdl_Others)
gen_vhdl_Open_Expression = Generalization(general=Expression, specific=vhdl_Open)
gen_vhdl_UnitValueExpression_ValueExpression = Generalization(general=ValueExpression, specific=vhdl_UnitValueExpression)

# Domain Model
domain_model = DomainModel(
    name="vhdl",
    types={vhdl_DesignFile, vhdl_ContextItem, vhdl_LibraryUnit, vhdl_UseClause, ContextItem, vhdl_Library, vhdl_LibraryClause, vhdl_Package, LibraryUnit, vhdl_package_declarative_item, vhdl_package_declarative_part, vhdl_Architecture, vhdl_Entity, vhdl_BlockDeclarativeItem, vhdl_ArchitectureStatement, vhdl_Generics, vhdl_Ports, vhdl_Port, Variable, vhdl_SubtypeIndication, vhdl_Expression, vhdl_Generic, vhdl_Alias, BlockDeclarativeItem, vhdl_SignalDeclaration, package_declarative_item, vhdl_Signal, vhdl_VariableDeclaration, vhdl_Var, vhdl_ConstantDeclaration, vhdl_Constant, vhdl_AttributeDeclaration, vhdl_AttributeSpecification, vhdl_Component, vhdl_ProcessStatement, ArchitectureStatement, vhdl_IdList, vhdl_SequentialStatement, vhdl_ComponentInstantiationStatement, vhdl_GenericMap, vhdl_PortMap, vhdl_EntityInstantiationStatement, vhdl_PortMapAssociation, vhdl_GenericMapAssociation, vhdl_ConditionalSignalAssignmentStatement, vhdl_ForGenerateStatement, vhdl_LoopVariable, vhdl_IfGenerateStatement, vhdl_WaitStatement, SequentialStatement, vhdl_IfStatement, vhdl_IfStatementTest, vhdl_SequentialSignalAssignmentStatement, vhdl_CaseStatement, vhdl_CaseAlternative, vhdl_LoopStatement, vhdl_IterationScheme, vhdl_WhileIterationScheme, IterationScheme, vhdl_ForIterationScheme, vhdl_Type, Expression, vhdl_SubtypeDeclaration, Type, vhdl_TypeDeclaration, vhdl_TypeDefinition, vhdl_AccessTypeDefinition, TypeDefinition, vhdl_CompositeTypeDefinition, vhdl_ArrayTypeDefinition, CompositeTypeDefinition, vhdl_UnconstrainedArrayTypeDefinition, ArrayTypeDefinition, vhdl_ConstrainedArrayTypeDefinition, vhdl_EnumerationTypeDefinition, vhdl_FileTypeDefinition, vhdl_RecordField, vhdl_RecordTypeDefinition, vhdl_Variable, vhdl_ValueExpression, vhdl_ConditionalWaveformExpression, vhdl_RangeExpression, vhdl_MultiExpression, vhdl_LogicalExpression, vhdl_RelationalExpression, vhdl_ChoiceExpression, vhdl_ShiftExpression, vhdl_AddingExpression, vhdl_MultiplyingExpression, vhdl_Factor, vhdl_MemberExpression, vhdl_Member, vhdl_SliceExpression, vhdl_Value, vhdl_BuiltinFuncs, vhdl_Boolean, vhdl_String, vhdl_Char, vhdl_BitString, vhdl_Others, vhdl_Open, vhdl_UnitValueExpression, ValueExpression, BuiltinLibs, EString, ShiftOperator, SignalKind, RangeDirection, Mode, UnaryOperator, MultiplyingOperator, Purity, RelationalOperator, LogicalOperator, AddingOperator, Sign, EntityClass},
    associations={ContextItems0, LibraryUnits1, lib3, custom_lib4, package_declarative_item6, package_declarative_item7, entity9, declaration10, statement12, generics14, ports16, declaration18, type20, type26, initial22, declaration24, initial29, alias32, is34, sig37, type38, initial41, var44, type45, initial48, constant51, type52, initial55, is58, generic60, port62, sensitivity65, statement66, genericMap68, portMap69, lib71, genericMap73, portMap76, association79, actual81, association84, actual86, target89, waveform91, declaration118, exp98, after101, expression104, var106, range107, declaration110, statement113, condition116, waveform95, statement121, sensitivity124, until126, time129, test132, statement133, condition136, statement139, case142, when144, choice146, statement149, var152, range154, statements157, target160, waveform162, condition165, in167, custom_type169, constraint171, type174, is176, type177, type179, constraint181, field183, type184, value188, id189, choice192, left194, right196, left199, right201, left204, right206, left209, right211, left214, right216, left219, right221, left224, right226, left229, right231, left234, member239, slice241, left244, slice246, value249, right236},
    generalizations={gen_vhdl_UseClause_ContextItem, gen_vhdl_LibraryClause_ContextItem, gen_vhdl_Package_LibraryUnit, gen_vhdl_Architecture_LibraryUnit, gen_vhdl_Entity_LibraryUnit, gen_vhdl_Port_Variable, gen_vhdl_Generic_Variable, gen_vhdl_Alias_BlockDeclarativeItem, gen_vhdl_Alias_Variable, gen_vhdl_SignalDeclaration_package_declarative_item, gen_vhdl_SignalDeclaration_BlockDeclarativeItem, gen_vhdl_Signal_Variable, gen_vhdl_VariableDeclaration_package_declarative_item, gen_vhdl_VariableDeclaration_BlockDeclarativeItem, gen_vhdl_Var_Variable, gen_vhdl_ConstantDeclaration_package_declarative_item, gen_vhdl_ConstantDeclaration_BlockDeclarativeItem, gen_vhdl_Constant_Variable, gen_vhdl_AttributeDeclaration_BlockDeclarativeItem, gen_vhdl_AttributeSpecification_BlockDeclarativeItem, gen_vhdl_Component_package_declarative_item, gen_vhdl_Component_BlockDeclarativeItem, gen_vhdl_ProcessStatement_ArchitectureStatement, gen_vhdl_ComponentInstantiationStatement_ArchitectureStatement, gen_vhdl_EntityInstantiationStatement_ArchitectureStatement, gen_vhdl_ConditionalSignalAssignmentStatement_ArchitectureStatement, gen_vhdl_ForGenerateStatement_ArchitectureStatement, gen_vhdl_IfGenerateStatement_ArchitectureStatement, gen_vhdl_WaitStatement_SequentialStatement, gen_vhdl_IfStatement_SequentialStatement, gen_vhdl_SequentialSignalAssignmentStatement_SequentialStatement, gen_vhdl_CaseStatement_SequentialStatement, gen_vhdl_LoopVariable_Variable, gen_vhdl_LoopStatement_SequentialStatement, gen_vhdl_WhileIterationScheme_IterationScheme, gen_vhdl_ForIterationScheme_IterationScheme, gen_vhdl_Type_package_declarative_item, gen_vhdl_Type_BlockDeclarativeItem, gen_vhdl_Type_Expression, gen_vhdl_SubtypeDeclaration_Type, gen_vhdl_TypeDeclaration_Type, gen_vhdl_AccessTypeDefinition_TypeDefinition, gen_vhdl_CompositeTypeDefinition_TypeDefinition, gen_vhdl_ArrayTypeDefinition_CompositeTypeDefinition, gen_vhdl_UnconstrainedArrayTypeDefinition_ArrayTypeDefinition, gen_vhdl_ConstrainedArrayTypeDefinition_ArrayTypeDefinition, gen_vhdl_EnumerationTypeDefinition_TypeDefinition, gen_vhdl_FileTypeDefinition_TypeDefinition, gen_vhdl_RecordTypeDefinition_CompositeTypeDefinition, gen_vhdl_Variable_Expression, gen_vhdl_ConditionalWaveformExpression_Expression, gen_vhdl_RangeExpression_Expression, gen_vhdl_MultiExpression_Expression, gen_vhdl_LogicalExpression_Expression, gen_vhdl_RelationalExpression_Expression, gen_vhdl_ChoiceExpression_Expression, gen_vhdl_ShiftExpression_Expression, gen_vhdl_AddingExpression_Expression, gen_vhdl_MultiplyingExpression_Expression, gen_vhdl_Factor_Expression, gen_vhdl_MemberExpression_Expression, gen_vhdl_Member_Expression, gen_vhdl_SliceExpression_Expression, gen_vhdl_Value_Expression, gen_vhdl_BuiltinFuncs_Expression, gen_vhdl_Boolean_Expression, gen_vhdl_String_Expression, gen_vhdl_Char_Expression, gen_vhdl_BitString_Expression, gen_vhdl_Others_Expression, gen_vhdl_Open_Expression, gen_vhdl_UnitValueExpression_ValueExpression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)