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
gaml_Entry = Class(name="gaml::Entry")
gaml_StandaloneBlock = Class(name="gaml::StandaloneBlock")
Entry = Class(name="Entry")
gaml_Block = Class(name="gaml::Block")
gaml_StringEvaluator = Class(name="gaml::StringEvaluator")
gaml_Expression = Class(name="gaml::Expression")
gaml_Model = Class(name="gaml::Model")
VarDefinition = Class(name="VarDefinition")
gaml_Pragma = Class(name="gaml::Pragma")
gaml_Import = Class(name="gaml::Import")
gaml_Statement = Class(name="gaml::Statement")
gaml_ExperimentFileStructure = Class(name="gaml::ExperimentFileStructure")
gaml_HeadlessExperiment = Class(name="gaml::HeadlessExperiment")
gaml_Facet = Class(name="gaml::Facet")
gaml_S_Global = Class(name="gaml::S::Global")
Statement = Class(name="Statement")
gaml_S_Species = Class(name="gaml::S::Species")
S_Declaration = Class(name="S::Declaration")
TypeDefinition = Class(name="TypeDefinition")
gaml_S_Experiment = Class(name="gaml::S::Experiment")
gaml_S_Do = Class(name="gaml::S::Do")
gaml_S_Loop = Class(name="gaml::S::Loop")
gaml_S_If = Class(name="gaml::S::If")
gaml_EObject = Class(name="gaml::EObject")
gaml_S_Try = Class(name="gaml::S::Try")
gaml_S_Other = Class(name="gaml::S::Other")
gaml_S_Return = Class(name="gaml::S::Return")
gaml_S_Declaration = Class(name="gaml::S::Declaration")
gaml_S_Reflex = Class(name="gaml::S::Reflex")
gaml_S_Definition = Class(name="gaml::S::Definition")
ActionDefinition = Class(name="ActionDefinition")
gaml_ActionArguments = Class(name="gaml::ActionArguments")
gaml_S_Assignment = Class(name="gaml::S::Assignment")
gaml_S_DirectAssignment = Class(name="gaml::S::DirectAssignment")
S_Assignment = Class(name="S::Assignment")
gaml_S_Set = Class(name="gaml::S::Set")
gaml_S_Equations = Class(name="gaml::S::Equations")
EquationDefinition = Class(name="EquationDefinition")
GamlDefinition = Class(name="GamlDefinition")
gaml_S_Solve = Class(name="gaml::S::Solve")
gaml_S_Display = Class(name="gaml::S::Display")
gaml_speciesOrGridDisplayStatement = Class(name="gaml::speciesOrGridDisplayStatement")
gaml_ArgumentDefinition = Class(name="gaml::ArgumentDefinition")
gaml_ArgumentPair = Class(name="gaml::ArgumentPair")
Expression = Class(name="Expression")
gaml_ExpressionList = Class(name="gaml::ExpressionList")
gaml_VariableRef = Class(name="gaml::VariableRef")
gaml_VarDefinition = Class(name="gaml::VarDefinition")
gaml_TypeInfo = Class(name="gaml::TypeInfo")
gaml_GamlDefinition = Class(name="gaml::GamlDefinition")
gaml_EquationDefinition = Class(name="gaml::EquationDefinition")
gaml_TypeDefinition = Class(name="gaml::TypeDefinition")
gaml_ActionDefinition = Class(name="gaml::ActionDefinition")
gaml_UnitFakeDefinition = Class(name="gaml::UnitFakeDefinition")
gaml_TypeFakeDefinition = Class(name="gaml::TypeFakeDefinition")
gaml_ActionFakeDefinition = Class(name="gaml::ActionFakeDefinition")
gaml_SkillFakeDefinition = Class(name="gaml::SkillFakeDefinition")
gaml_VarFakeDefinition = Class(name="gaml::VarFakeDefinition")
gaml_EquationFakeDefinition = Class(name="gaml::EquationFakeDefinition")
gaml_TerminalExpression = Class(name="gaml::TerminalExpression")
gaml_StringLiteral = Class(name="gaml::StringLiteral")
TerminalExpression = Class(name="TerminalExpression")
gaml_S_Action = Class(name="gaml::S::Action")
S_Definition = Class(name="S::Definition")
gaml_S_Var = Class(name="gaml::S::Var")
gaml_BinaryOperator = Class(name="gaml::BinaryOperator")
gaml_If = Class(name="gaml::If")
gaml_Unit = Class(name="gaml::Unit")
gaml_Unary = Class(name="gaml::Unary")
gaml_Access = Class(name="gaml::Access")
gaml_Array = Class(name="gaml::Array")
gaml_Point = Class(name="gaml::Point")
gaml_Function = Class(name="gaml::Function")
gaml_Parameter = Class(name="gaml::Parameter")
gaml_UnitName = Class(name="gaml::UnitName")
gaml_TypeRef = Class(name="gaml::TypeRef")
gaml_SkillRef = Class(name="gaml::SkillRef")
gaml_ActionRef = Class(name="gaml::ActionRef")
gaml_EquationRef = Class(name="gaml::EquationRef")
gaml_IntLiteral = Class(name="gaml::IntLiteral")
gaml_DoubleLiteral = Class(name="gaml::DoubleLiteral")
gaml_BooleanLiteral = Class(name="gaml::BooleanLiteral")
gaml_ReservedLiteral = Class(name="gaml::ReservedLiteral")

# gaml_Entry class attributes and methods

# gaml_StandaloneBlock class attributes and methods

# Entry class attributes and methods

# gaml_Block class attributes and methods

# gaml_StringEvaluator class attributes and methods
gaml_StringEvaluator_toto: Property = Property(name="toto", type=StringType)
gaml_StringEvaluator.attributes={gaml_StringEvaluator_toto}

# gaml_Expression class attributes and methods

# gaml_Model class attributes and methods

# VarDefinition class attributes and methods

# gaml_Pragma class attributes and methods
gaml_Pragma_name: Property = Property(name="name", type=StringType)
gaml_Pragma.attributes={gaml_Pragma_name}

# gaml_Import class attributes and methods
gaml_Import_importURI: Property = Property(name="importURI", type=StringType)
gaml_Import.attributes={gaml_Import_importURI}

# gaml_Statement class attributes and methods
gaml_Statement_key: Property = Property(name="key", type=StringType)
gaml_Statement_firstFacet: Property = Property(name="firstFacet", type=StringType)
gaml_Statement.attributes={gaml_Statement_key, gaml_Statement_firstFacet}

# gaml_ExperimentFileStructure class attributes and methods

# gaml_HeadlessExperiment class attributes and methods
gaml_HeadlessExperiment_key: Property = Property(name="key", type=StringType)
gaml_HeadlessExperiment_firstFacet: Property = Property(name="firstFacet", type=StringType)
gaml_HeadlessExperiment_name: Property = Property(name="name", type=StringType)
gaml_HeadlessExperiment_importURI: Property = Property(name="importURI", type=StringType)
gaml_HeadlessExperiment.attributes={gaml_HeadlessExperiment_name, gaml_HeadlessExperiment_key, gaml_HeadlessExperiment_importURI, gaml_HeadlessExperiment_firstFacet}

# gaml_Facet class attributes and methods
gaml_Facet_key: Property = Property(name="key", type=StringType)
gaml_Facet.attributes={gaml_Facet_key}

# gaml_S_Global class attributes and methods

# Statement class attributes and methods

# gaml_S_Species class attributes and methods

# S_Declaration class attributes and methods

# TypeDefinition class attributes and methods

# gaml_S_Experiment class attributes and methods

# gaml_S_Do class attributes and methods

# gaml_S_Loop class attributes and methods

# gaml_S_If class attributes and methods

# gaml_EObject class attributes and methods

# gaml_S_Try class attributes and methods

# gaml_S_Other class attributes and methods

# gaml_S_Return class attributes and methods

# gaml_S_Declaration class attributes and methods

# gaml_S_Reflex class attributes and methods

# gaml_S_Definition class attributes and methods

# ActionDefinition class attributes and methods

# gaml_ActionArguments class attributes and methods

# gaml_S_Assignment class attributes and methods

# gaml_S_DirectAssignment class attributes and methods

# S_Assignment class attributes and methods

# gaml_S_Set class attributes and methods

# gaml_S_Equations class attributes and methods

# EquationDefinition class attributes and methods

# GamlDefinition class attributes and methods

# gaml_S_Solve class attributes and methods

# gaml_S_Display class attributes and methods
gaml_S_Display_name: Property = Property(name="name", type=StringType)
gaml_S_Display.attributes={gaml_S_Display_name}

# gaml_speciesOrGridDisplayStatement class attributes and methods

# gaml_ArgumentDefinition class attributes and methods

# gaml_ArgumentPair class attributes and methods
gaml_ArgumentPair_op: Property = Property(name="op", type=StringType)
gaml_ArgumentPair.attributes={gaml_ArgumentPair_op}

# Expression class attributes and methods

# gaml_ExpressionList class attributes and methods

# gaml_VariableRef class attributes and methods

# gaml_VarDefinition class attributes and methods

# gaml_TypeInfo class attributes and methods

# gaml_GamlDefinition class attributes and methods
gaml_GamlDefinition_name: Property = Property(name="name", type=StringType)
gaml_GamlDefinition.attributes={gaml_GamlDefinition_name}

# gaml_EquationDefinition class attributes and methods

# gaml_TypeDefinition class attributes and methods

# gaml_ActionDefinition class attributes and methods

# gaml_UnitFakeDefinition class attributes and methods

# gaml_TypeFakeDefinition class attributes and methods

# gaml_ActionFakeDefinition class attributes and methods

# gaml_SkillFakeDefinition class attributes and methods

# gaml_VarFakeDefinition class attributes and methods

# gaml_EquationFakeDefinition class attributes and methods

# gaml_TerminalExpression class attributes and methods
gaml_TerminalExpression_op: Property = Property(name="op", type=StringType)
gaml_TerminalExpression.attributes={gaml_TerminalExpression_op}

# gaml_StringLiteral class attributes and methods

# TerminalExpression class attributes and methods

# gaml_S_Action class attributes and methods

# S_Definition class attributes and methods

# gaml_S_Var class attributes and methods

# gaml_BinaryOperator class attributes and methods
gaml_BinaryOperator_op: Property = Property(name="op", type=StringType)
gaml_BinaryOperator.attributes={gaml_BinaryOperator_op}

# gaml_If class attributes and methods
gaml_If_op: Property = Property(name="op", type=StringType)
gaml_If.attributes={gaml_If_op}

# gaml_Unit class attributes and methods
gaml_Unit_op: Property = Property(name="op", type=StringType)
gaml_Unit.attributes={gaml_Unit_op}

# gaml_Unary class attributes and methods
gaml_Unary_op: Property = Property(name="op", type=StringType)
gaml_Unary.attributes={gaml_Unary_op}

# gaml_Access class attributes and methods
gaml_Access_op: Property = Property(name="op", type=StringType)
gaml_Access.attributes={gaml_Access_op}

# gaml_Array class attributes and methods

# gaml_Point class attributes and methods
gaml_Point_op: Property = Property(name="op", type=StringType)
gaml_Point.attributes={gaml_Point_op}

# gaml_Function class attributes and methods

# gaml_Parameter class attributes and methods
gaml_Parameter_builtInFacetKey: Property = Property(name="builtInFacetKey", type=StringType)
gaml_Parameter.attributes={gaml_Parameter_builtInFacetKey}

# gaml_UnitName class attributes and methods

# gaml_TypeRef class attributes and methods

# gaml_SkillRef class attributes and methods

# gaml_ActionRef class attributes and methods

# gaml_EquationRef class attributes and methods

# gaml_IntLiteral class attributes and methods

# gaml_DoubleLiteral class attributes and methods

# gaml_BooleanLiteral class attributes and methods

# gaml_ReservedLiteral class attributes and methods

# Relationships
block0: BinaryAssociation = BinaryAssociation(
    name="block0",
    ends={
        Property(name="gaml_Block", type=gaml_StandaloneBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="gaml_StandaloneBlock", type=gaml_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr1: BinaryAssociation = BinaryAssociation(
    name="expr1",
    ends={
        Property(name="gaml_Expression", type=gaml_StringEvaluator, multiplicity=Multiplicity(1, 1)),
        Property(name="gaml_StringEvaluator", type=gaml_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pragmas2: BinaryAssociation = BinaryAssociation(
    name="pragmas2",
    ends={
        Property(name="gaml_Pragma", type=gaml_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="gaml_Model", type=gaml_Pragma, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
imports3: BinaryAssociation = BinaryAssociation(
    name="imports3",
    ends={
        Property(name="gaml_Import", type=gaml_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="gaml_Model4", type=gaml_Import, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
block5: BinaryAssociation = BinaryAssociation(
    name="block5",
    ends={
        Property(name="gaml_Block7", type=gaml_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="gaml_Model6", type=gaml_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statements8: BinaryAssociation = BinaryAssociation(
    name="statements8",
    ends={
        Property(name="gaml_Statement", type=gaml_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="gaml_Block9", type=gaml_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exp10: BinaryAssociation = BinaryAssociation(
    name="exp10",
    ends={
        Property(name="gaml_HeadlessExperiment", type=gaml_ExperimentFileStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="gaml_ExperimentFileStructure", type=gaml_HeadlessExperiment, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
facets11: BinaryAssociation = BinaryAssociation(
    name="facets11",
    ends={
        Property(name="gaml_Facet", type=gaml_HeadlessExperiment, multiplicity=Multiplicity(1, 1)),
        Property(name="gaml_HeadlessExperiment12", type=gaml_Facet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
block13: BinaryAssociation = BinaryAssociation(
    name="block13",
    ends={
        Property(name="gaml_Block15", type=gaml_HeadlessExperiment, multiplicity=Multiplicity(1, 1)),
        Property(name="gaml_HeadlessExperiment14", type=gaml_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr16: BinaryAssociation = BinaryAssociation(
    name="expr16",
    ends={
        Property(name="gaml_Expression18", type=gaml_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="gaml_Statement17", type=gaml_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
facets19: BinaryAssociation = BinaryAssociation(
    name="facets19",
    ends={
        Property(name="gaml_Facet21", type=gaml_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="gaml_Statement20", type=gaml_Facet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
block22: BinaryAssociation = BinaryAssociation(
    name="block22",
    ends={
        Property(name="gaml_Block24", type=gaml_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="gaml_Statement23", type=gaml_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
else25: BinaryAssociation = BinaryAssociation(
    name="else25",
    ends={
        Property(name="gaml_EObject", type=gaml_S_If, multiplicity=Multiplicity(1, 1)),
        Property(name="gaml_S_If", type=gaml_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
catch26: BinaryAssociation = BinaryAssociation(
    name="catch26",
    ends={
        Property(name="gaml_Block27", type=gaml_S_Try, multiplicity=Multiplicity(1, 1)),
        Property(name="gaml_S_Try", type=gaml_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tkey28: BinaryAssociation = BinaryAssociation(
    name="tkey28",
    ends={
        Property(name="gaml_Expression29", type=gaml_S_Definition, multiplicity=Multiplicity(1, 1)),
        Property(name="gaml_S_Definition", type=gaml_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
args30: BinaryAssociation = BinaryAssociation(
    name="args30",
    ends={
        Property(name="gaml_ActionArguments", type=gaml_S_Definition, multiplicity=Multiplicity(1, 1)),
        Property(name="gaml_S_Definition31", type=gaml_ActionArguments, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value32: BinaryAssociation = BinaryAssociation(
    name="value32",
    ends={
        Property(name="gaml_Expression33", type=gaml_S_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="gaml_S_Assignment", type=gaml_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
equations34: BinaryAssociation = BinaryAssociation(
    name="equations34",
    ends={
        Property(name="gaml_S_Assignment35", type=gaml_S_Equations, multiplicity=Multiplicity(1, 1)),
        Property(name="gaml_S_Equations", type=gaml_S_Assignment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
args36: BinaryAssociation = BinaryAssociation(
    name="args36",
    ends={
        Property(name="gaml_ArgumentDefinition", type=gaml_ActionArguments, multiplicity=Multiplicity(1, 1)),
        Property(name="gaml_ActionArguments37", type=gaml_ArgumentDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type38: BinaryAssociation = BinaryAssociation(
    name="type38",
    ends={
        Property(name="gaml_Expression40", type=gaml_ArgumentDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="gaml_ArgumentDefinition39", type=gaml_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
default41: BinaryAssociation = BinaryAssociation(
    name="default41",
    ends={
        Property(name="gaml_Expression43", type=gaml_ArgumentDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="gaml_ArgumentDefinition42", type=gaml_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr44: BinaryAssociation = BinaryAssociation(
    name="expr44",
    ends={
        Property(name="gaml_Expression46", type=gaml_Facet, multiplicity=Multiplicity(1, 1)),
        Property(name="gaml_Facet45", type=gaml_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block47: BinaryAssociation = BinaryAssociation(
    name="block47",
    ends={
        Property(name="gaml_Block49", type=gaml_Facet, multiplicity=Multiplicity(1, 1)),
        Property(name="gaml_Facet48", type=gaml_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right50: BinaryAssociation = BinaryAssociation(
    name="right50",
    ends={
        Property(name="gaml_Expression51", type=gaml_ArgumentPair, multiplicity=Multiplicity(1, 1)),
        Property(name="gaml_ArgumentPair", type=gaml_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exprs52: BinaryAssociation = BinaryAssociation(
    name="exprs52",
    ends={
        Property(name="gaml_Expression53", type=gaml_ExpressionList, multiplicity=Multiplicity(1, 1)),
        Property(name="gaml_ExpressionList", type=gaml_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ref54: BinaryAssociation = BinaryAssociation(
    name="ref54",
    ends={
        Property(name="gaml_VarDefinition", type=gaml_VariableRef, multiplicity=Multiplicity(1, 1)),
        Property(name="gaml_VariableRef", type=gaml_VarDefinition, multiplicity=Multiplicity(0, 1))
    }
)
first55: BinaryAssociation = BinaryAssociation(
    name="first55",
    ends={
        Property(name="gaml_Expression56", type=gaml_TypeInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="gaml_TypeInfo", type=gaml_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
second57: BinaryAssociation = BinaryAssociation(
    name="second57",
    ends={
        Property(name="gaml_Expression59", type=gaml_TypeInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="gaml_TypeInfo58", type=gaml_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left60: BinaryAssociation = BinaryAssociation(
    name="left60",
    ends={
        Property(name="gaml_Expression61", type=gaml_BinaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="gaml_BinaryOperator", type=gaml_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right62: BinaryAssociation = BinaryAssociation(
    name="right62",
    ends={
        Property(name="gaml_Expression64", type=gaml_BinaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="gaml_BinaryOperator63", type=gaml_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left65: BinaryAssociation = BinaryAssociation(
    name="left65",
    ends={
        Property(name="gaml_Expression66", type=gaml_If, multiplicity=Multiplicity(1, 1)),
        Property(name="gaml_If", type=gaml_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right67: BinaryAssociation = BinaryAssociation(
    name="right67",
    ends={
        Property(name="gaml_Expression69", type=gaml_If, multiplicity=Multiplicity(1, 1)),
        Property(name="gaml_If68", type=gaml_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ifFalse70: BinaryAssociation = BinaryAssociation(
    name="ifFalse70",
    ends={
        Property(name="gaml_Expression72", type=gaml_If, multiplicity=Multiplicity(1, 1)),
        Property(name="gaml_If71", type=gaml_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left73: BinaryAssociation = BinaryAssociation(
    name="left73",
    ends={
        Property(name="gaml_Expression74", type=gaml_Unit, multiplicity=Multiplicity(1, 1)),
        Property(name="gaml_Unit", type=gaml_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right75: BinaryAssociation = BinaryAssociation(
    name="right75",
    ends={
        Property(name="gaml_Expression77", type=gaml_Unit, multiplicity=Multiplicity(1, 1)),
        Property(name="gaml_Unit76", type=gaml_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right78: BinaryAssociation = BinaryAssociation(
    name="right78",
    ends={
        Property(name="gaml_Expression79", type=gaml_Unary, multiplicity=Multiplicity(1, 1)),
        Property(name="gaml_Unary", type=gaml_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left80: BinaryAssociation = BinaryAssociation(
    name="left80",
    ends={
        Property(name="gaml_Expression81", type=gaml_Access, multiplicity=Multiplicity(1, 1)),
        Property(name="gaml_Access", type=gaml_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right82: BinaryAssociation = BinaryAssociation(
    name="right82",
    ends={
        Property(name="gaml_Expression84", type=gaml_Access, multiplicity=Multiplicity(1, 1)),
        Property(name="gaml_Access83", type=gaml_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exprs85: BinaryAssociation = BinaryAssociation(
    name="exprs85",
    ends={
        Property(name="gaml_ExpressionList86", type=gaml_Array, multiplicity=Multiplicity(1, 1)),
        Property(name="gaml_Array", type=gaml_ExpressionList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left87: BinaryAssociation = BinaryAssociation(
    name="left87",
    ends={
        Property(name="gaml_Expression88", type=gaml_Point, multiplicity=Multiplicity(1, 1)),
        Property(name="gaml_Point", type=gaml_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right89: BinaryAssociation = BinaryAssociation(
    name="right89",
    ends={
        Property(name="gaml_Expression91", type=gaml_Point, multiplicity=Multiplicity(1, 1)),
        Property(name="gaml_Point90", type=gaml_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
z92: BinaryAssociation = BinaryAssociation(
    name="z92",
    ends={
        Property(name="gaml_Expression94", type=gaml_Point, multiplicity=Multiplicity(1, 1)),
        Property(name="gaml_Point93", type=gaml_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left95: BinaryAssociation = BinaryAssociation(
    name="left95",
    ends={
        Property(name="gaml_Expression96", type=gaml_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="gaml_Function", type=gaml_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type97: BinaryAssociation = BinaryAssociation(
    name="type97",
    ends={
        Property(name="gaml_TypeInfo99", type=gaml_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="gaml_Function98", type=gaml_TypeInfo, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right100: BinaryAssociation = BinaryAssociation(
    name="right100",
    ends={
        Property(name="gaml_ExpressionList102", type=gaml_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="gaml_Function101", type=gaml_ExpressionList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left103: BinaryAssociation = BinaryAssociation(
    name="left103",
    ends={
        Property(name="gaml_VariableRef104", type=gaml_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="gaml_Parameter", type=gaml_VariableRef, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right105: BinaryAssociation = BinaryAssociation(
    name="right105",
    ends={
        Property(name="gaml_Expression107", type=gaml_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="gaml_Parameter106", type=gaml_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ref108: BinaryAssociation = BinaryAssociation(
    name="ref108",
    ends={
        Property(name="gaml_UnitFakeDefinition", type=gaml_UnitName, multiplicity=Multiplicity(1, 1)),
        Property(name="gaml_UnitName", type=gaml_UnitFakeDefinition, multiplicity=Multiplicity(0, 1))
    }
)
ref109: BinaryAssociation = BinaryAssociation(
    name="ref109",
    ends={
        Property(name="gaml_TypeDefinition", type=gaml_TypeRef, multiplicity=Multiplicity(1, 1)),
        Property(name="gaml_TypeRef", type=gaml_TypeDefinition, multiplicity=Multiplicity(0, 1))
    }
)
parameter110: BinaryAssociation = BinaryAssociation(
    name="parameter110",
    ends={
        Property(name="gaml_TypeInfo112", type=gaml_TypeRef, multiplicity=Multiplicity(1, 1)),
        Property(name="gaml_TypeRef111", type=gaml_TypeInfo, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ref113: BinaryAssociation = BinaryAssociation(
    name="ref113",
    ends={
        Property(name="gaml_SkillFakeDefinition", type=gaml_SkillRef, multiplicity=Multiplicity(1, 1)),
        Property(name="gaml_SkillRef", type=gaml_SkillFakeDefinition, multiplicity=Multiplicity(0, 1))
    }
)
ref114: BinaryAssociation = BinaryAssociation(
    name="ref114",
    ends={
        Property(name="gaml_ActionDefinition", type=gaml_ActionRef, multiplicity=Multiplicity(1, 1)),
        Property(name="gaml_ActionRef", type=gaml_ActionDefinition, multiplicity=Multiplicity(0, 1))
    }
)
ref115: BinaryAssociation = BinaryAssociation(
    name="ref115",
    ends={
        Property(name="gaml_EquationDefinition", type=gaml_EquationRef, multiplicity=Multiplicity(1, 1)),
        Property(name="gaml_EquationRef", type=gaml_EquationDefinition, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_gaml_StandaloneBlock_Entry = Generalization(general=Entry, specific=gaml_StandaloneBlock)
gen_gaml_StringEvaluator_Entry = Generalization(general=Entry, specific=gaml_StringEvaluator)
gen_gaml_Model_Entry = Generalization(general=Entry, specific=gaml_Model)
gen_gaml_Model_VarDefinition = Generalization(general=VarDefinition, specific=gaml_Model)
gen_gaml_Import_VarDefinition = Generalization(general=VarDefinition, specific=gaml_Import)
gen_gaml_ExperimentFileStructure_Entry = Generalization(general=Entry, specific=gaml_ExperimentFileStructure)
gen_gaml_S_Global_Statement = Generalization(general=Statement, specific=gaml_S_Global)
gen_gaml_S_Species_Statement = Generalization(general=Statement, specific=gaml_S_Species)
gen_gaml_S_Species_S_Declaration = Generalization(general=S_Declaration, specific=gaml_S_Species)
gen_gaml_S_Species_TypeDefinition = Generalization(general=TypeDefinition, specific=gaml_S_Species)
gen_gaml_S_Experiment_Statement = Generalization(general=Statement, specific=gaml_S_Experiment)
gen_gaml_S_Experiment_VarDefinition = Generalization(general=VarDefinition, specific=gaml_S_Experiment)
gen_gaml_S_Do_Statement = Generalization(general=Statement, specific=gaml_S_Do)
gen_gaml_S_Loop_S_Declaration = Generalization(general=S_Declaration, specific=gaml_S_Loop)
gen_gaml_S_If_Statement = Generalization(general=Statement, specific=gaml_S_If)
gen_gaml_S_Try_Statement = Generalization(general=Statement, specific=gaml_S_Try)
gen_gaml_S_Other_Statement = Generalization(general=Statement, specific=gaml_S_Other)
gen_gaml_S_Return_Statement = Generalization(general=Statement, specific=gaml_S_Return)
gen_gaml_S_Declaration_Statement = Generalization(general=Statement, specific=gaml_S_Declaration)
gen_gaml_S_Declaration_VarDefinition = Generalization(general=VarDefinition, specific=gaml_S_Declaration)
gen_gaml_S_Reflex_S_Declaration = Generalization(general=S_Declaration, specific=gaml_S_Reflex)
gen_gaml_S_Definition_S_Declaration = Generalization(general=S_Declaration, specific=gaml_S_Definition)
gen_gaml_S_Definition_ActionDefinition = Generalization(general=ActionDefinition, specific=gaml_S_Definition)
gen_gaml_S_Assignment_Statement = Generalization(general=Statement, specific=gaml_S_Assignment)
gen_gaml_S_DirectAssignment_S_Assignment = Generalization(general=S_Assignment, specific=gaml_S_DirectAssignment)
gen_gaml_S_Set_S_Assignment = Generalization(general=S_Assignment, specific=gaml_S_Set)
gen_gaml_S_Equations_Statement = Generalization(general=Statement, specific=gaml_S_Equations)
gen_gaml_S_Equations_EquationDefinition = Generalization(general=EquationDefinition, specific=gaml_S_Equations)
gen_gaml_EquationDefinition_GamlDefinition = Generalization(general=GamlDefinition, specific=gaml_EquationDefinition)
gen_gaml_S_Solve_Statement = Generalization(general=Statement, specific=gaml_S_Solve)
gen_gaml_S_Display_Statement = Generalization(general=Statement, specific=gaml_S_Display)
gen_gaml_speciesOrGridDisplayStatement_Statement = Generalization(general=Statement, specific=gaml_speciesOrGridDisplayStatement)
gen_gaml_ArgumentDefinition_VarDefinition = Generalization(general=VarDefinition, specific=gaml_ArgumentDefinition)
gen_gaml_Facet_VarDefinition = Generalization(general=VarDefinition, specific=gaml_Facet)
gen_gaml_ArgumentPair_Expression = Generalization(general=Expression, specific=gaml_ArgumentPair)
gen_gaml_ExpressionList_Expression = Generalization(general=Expression, specific=gaml_ExpressionList)
gen_gaml_VariableRef_Expression = Generalization(general=Expression, specific=gaml_VariableRef)
gen_gaml_TypeDefinition_GamlDefinition = Generalization(general=GamlDefinition, specific=gaml_TypeDefinition)
gen_gaml_TypeDefinition_ActionDefinition = Generalization(general=ActionDefinition, specific=gaml_TypeDefinition)
gen_gaml_VarDefinition_GamlDefinition = Generalization(general=GamlDefinition, specific=gaml_VarDefinition)
gen_gaml_ActionDefinition_GamlDefinition = Generalization(general=GamlDefinition, specific=gaml_ActionDefinition)
gen_gaml_UnitFakeDefinition_GamlDefinition = Generalization(general=GamlDefinition, specific=gaml_UnitFakeDefinition)
gen_gaml_TypeFakeDefinition_TypeDefinition = Generalization(general=TypeDefinition, specific=gaml_TypeFakeDefinition)
gen_gaml_ActionFakeDefinition_ActionDefinition = Generalization(general=ActionDefinition, specific=gaml_ActionFakeDefinition)
gen_gaml_SkillFakeDefinition_GamlDefinition = Generalization(general=GamlDefinition, specific=gaml_SkillFakeDefinition)
gen_gaml_VarFakeDefinition_VarDefinition = Generalization(general=VarDefinition, specific=gaml_VarFakeDefinition)
gen_gaml_EquationFakeDefinition_EquationDefinition = Generalization(general=EquationDefinition, specific=gaml_EquationFakeDefinition)
gen_gaml_TerminalExpression_Expression = Generalization(general=Expression, specific=gaml_TerminalExpression)
gen_gaml_StringLiteral_TerminalExpression = Generalization(general=TerminalExpression, specific=gaml_StringLiteral)
gen_gaml_S_Action_S_Definition = Generalization(general=S_Definition, specific=gaml_S_Action)
gen_gaml_S_Var_S_Definition = Generalization(general=S_Definition, specific=gaml_S_Var)
gen_gaml_BinaryOperator_Expression = Generalization(general=Expression, specific=gaml_BinaryOperator)
gen_gaml_If_Expression = Generalization(general=Expression, specific=gaml_If)
gen_gaml_Unit_Expression = Generalization(general=Expression, specific=gaml_Unit)
gen_gaml_Unary_Expression = Generalization(general=Expression, specific=gaml_Unary)
gen_gaml_Access_Expression = Generalization(general=Expression, specific=gaml_Access)
gen_gaml_Array_Expression = Generalization(general=Expression, specific=gaml_Array)
gen_gaml_Point_Expression = Generalization(general=Expression, specific=gaml_Point)
gen_gaml_Function_Expression = Generalization(general=Expression, specific=gaml_Function)
gen_gaml_Parameter_Expression = Generalization(general=Expression, specific=gaml_Parameter)
gen_gaml_UnitName_Expression = Generalization(general=Expression, specific=gaml_UnitName)
gen_gaml_TypeRef_Expression = Generalization(general=Expression, specific=gaml_TypeRef)
gen_gaml_SkillRef_Expression = Generalization(general=Expression, specific=gaml_SkillRef)
gen_gaml_ActionRef_Expression = Generalization(general=Expression, specific=gaml_ActionRef)
gen_gaml_EquationRef_Expression = Generalization(general=Expression, specific=gaml_EquationRef)
gen_gaml_IntLiteral_TerminalExpression = Generalization(general=TerminalExpression, specific=gaml_IntLiteral)
gen_gaml_DoubleLiteral_TerminalExpression = Generalization(general=TerminalExpression, specific=gaml_DoubleLiteral)
gen_gaml_BooleanLiteral_TerminalExpression = Generalization(general=TerminalExpression, specific=gaml_BooleanLiteral)
gen_gaml_ReservedLiteral_TerminalExpression = Generalization(general=TerminalExpression, specific=gaml_ReservedLiteral)

# Domain Model
domain_model = DomainModel(
    name="gaml",
    types={gaml_Entry, gaml_StandaloneBlock, Entry, gaml_Block, gaml_StringEvaluator, gaml_Expression, gaml_Model, VarDefinition, gaml_Pragma, gaml_Import, gaml_Statement, gaml_ExperimentFileStructure, gaml_HeadlessExperiment, gaml_Facet, gaml_S_Global, Statement, gaml_S_Species, S_Declaration, TypeDefinition, gaml_S_Experiment, gaml_S_Do, gaml_S_Loop, gaml_S_If, gaml_EObject, gaml_S_Try, gaml_S_Other, gaml_S_Return, gaml_S_Declaration, gaml_S_Reflex, gaml_S_Definition, ActionDefinition, gaml_ActionArguments, gaml_S_Assignment, gaml_S_DirectAssignment, S_Assignment, gaml_S_Set, gaml_S_Equations, EquationDefinition, GamlDefinition, gaml_S_Solve, gaml_S_Display, gaml_speciesOrGridDisplayStatement, gaml_ArgumentDefinition, gaml_ArgumentPair, Expression, gaml_ExpressionList, gaml_VariableRef, gaml_VarDefinition, gaml_TypeInfo, gaml_GamlDefinition, gaml_EquationDefinition, gaml_TypeDefinition, gaml_ActionDefinition, gaml_UnitFakeDefinition, gaml_TypeFakeDefinition, gaml_ActionFakeDefinition, gaml_SkillFakeDefinition, gaml_VarFakeDefinition, gaml_EquationFakeDefinition, gaml_TerminalExpression, gaml_StringLiteral, TerminalExpression, gaml_S_Action, S_Definition, gaml_S_Var, gaml_BinaryOperator, gaml_If, gaml_Unit, gaml_Unary, gaml_Access, gaml_Array, gaml_Point, gaml_Function, gaml_Parameter, gaml_UnitName, gaml_TypeRef, gaml_SkillRef, gaml_ActionRef, gaml_EquationRef, gaml_IntLiteral, gaml_DoubleLiteral, gaml_BooleanLiteral, gaml_ReservedLiteral},
    associations={block0, expr1, pragmas2, imports3, block5, statements8, exp10, facets11, block13, expr16, facets19, block22, else25, catch26, tkey28, args30, value32, equations34, args36, type38, default41, expr44, block47, right50, exprs52, ref54, first55, second57, left60, right62, left65, right67, ifFalse70, left73, right75, right78, left80, right82, exprs85, left87, right89, z92, left95, type97, right100, left103, right105, ref108, ref109, parameter110, ref113, ref114, ref115},
    generalizations={gen_gaml_StandaloneBlock_Entry, gen_gaml_StringEvaluator_Entry, gen_gaml_Model_Entry, gen_gaml_Model_VarDefinition, gen_gaml_Import_VarDefinition, gen_gaml_ExperimentFileStructure_Entry, gen_gaml_S_Global_Statement, gen_gaml_S_Species_Statement, gen_gaml_S_Species_S_Declaration, gen_gaml_S_Species_TypeDefinition, gen_gaml_S_Experiment_Statement, gen_gaml_S_Experiment_VarDefinition, gen_gaml_S_Do_Statement, gen_gaml_S_Loop_S_Declaration, gen_gaml_S_If_Statement, gen_gaml_S_Try_Statement, gen_gaml_S_Other_Statement, gen_gaml_S_Return_Statement, gen_gaml_S_Declaration_Statement, gen_gaml_S_Declaration_VarDefinition, gen_gaml_S_Reflex_S_Declaration, gen_gaml_S_Definition_S_Declaration, gen_gaml_S_Definition_ActionDefinition, gen_gaml_S_Assignment_Statement, gen_gaml_S_DirectAssignment_S_Assignment, gen_gaml_S_Set_S_Assignment, gen_gaml_S_Equations_Statement, gen_gaml_S_Equations_EquationDefinition, gen_gaml_EquationDefinition_GamlDefinition, gen_gaml_S_Solve_Statement, gen_gaml_S_Display_Statement, gen_gaml_speciesOrGridDisplayStatement_Statement, gen_gaml_ArgumentDefinition_VarDefinition, gen_gaml_Facet_VarDefinition, gen_gaml_ArgumentPair_Expression, gen_gaml_ExpressionList_Expression, gen_gaml_VariableRef_Expression, gen_gaml_TypeDefinition_GamlDefinition, gen_gaml_TypeDefinition_ActionDefinition, gen_gaml_VarDefinition_GamlDefinition, gen_gaml_ActionDefinition_GamlDefinition, gen_gaml_UnitFakeDefinition_GamlDefinition, gen_gaml_TypeFakeDefinition_TypeDefinition, gen_gaml_ActionFakeDefinition_ActionDefinition, gen_gaml_SkillFakeDefinition_GamlDefinition, gen_gaml_VarFakeDefinition_VarDefinition, gen_gaml_EquationFakeDefinition_EquationDefinition, gen_gaml_TerminalExpression_Expression, gen_gaml_StringLiteral_TerminalExpression, gen_gaml_S_Action_S_Definition, gen_gaml_S_Var_S_Definition, gen_gaml_BinaryOperator_Expression, gen_gaml_If_Expression, gen_gaml_Unit_Expression, gen_gaml_Unary_Expression, gen_gaml_Access_Expression, gen_gaml_Array_Expression, gen_gaml_Point_Expression, gen_gaml_Function_Expression, gen_gaml_Parameter_Expression, gen_gaml_UnitName_Expression, gen_gaml_TypeRef_Expression, gen_gaml_SkillRef_Expression, gen_gaml_ActionRef_Expression, gen_gaml_EquationRef_Expression, gen_gaml_IntLiteral_TerminalExpression, gen_gaml_DoubleLiteral_TerminalExpression, gen_gaml_BooleanLiteral_TerminalExpression, gen_gaml_ReservedLiteral_TerminalExpression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)