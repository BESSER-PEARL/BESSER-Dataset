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
gaml_Facet = Class(name="gaml::Facet")
gaml_S_Global = Class(name="gaml::S::Global")
Statement = Class(name="Statement")
gaml_S_Species = Class(name="gaml::S::Species")
S_Declaration = Class(name="S::Declaration")
TypeDefinition = Class(name="TypeDefinition")
gaml_S_Experiment = Class(name="gaml::S::Experiment")
gaml_S_Do = Class(name="gaml::S::Do")
gaml_Import = Class(name="gaml::Import")
gaml_Statement = Class(name="gaml::Statement")
gaml_ExperimentFileStructure = Class(name="gaml::ExperimentFileStructure")
gaml_HeadlessExperiment = Class(name="gaml::HeadlessExperiment")
EquationDefinition = Class(name="EquationDefinition")
gaml_S_Solve = Class(name="gaml::S::Solve")
gaml_S_Display = Class(name="gaml::S::Display")
gaml_speciesOrGridDisplayStatement = Class(name="gaml::speciesOrGridDisplayStatement")
gaml_Parameters = Class(name="gaml::Parameters")
Expression = Class(name="Expression")
gaml_ExpressionList = Class(name="gaml::ExpressionList")
gaml_ArgumentDefinition = Class(name="gaml::ArgumentDefinition")
gaml_S_Loop = Class(name="gaml::S::Loop")
gaml_S_If = Class(name="gaml::S::If")
gaml_EObject = Class(name="gaml::EObject")
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
gaml_TypeInfo = Class(name="gaml::TypeInfo")
gaml_VariableRef = Class(name="gaml::VariableRef")
gaml_VarDefinition = Class(name="gaml::VarDefinition")
gaml_GamlDefinition = Class(name="gaml::GamlDefinition")
gaml_ArgumentPair = Class(name="gaml::ArgumentPair")
gaml_Function = Class(name="gaml::Function")
gaml_Binary = Class(name="gaml::Binary")
gaml_Unit = Class(name="gaml::Unit")
gaml_Unary = Class(name="gaml::Unary")
gaml_Access = Class(name="gaml::Access")
gaml_Array = Class(name="gaml::Array")
gaml_Point = Class(name="gaml::Point")
gaml_Parameter = Class(name="gaml::Parameter")
gaml_UnitName = Class(name="gaml::UnitName")
gaml_EquationDefinition = Class(name="gaml::EquationDefinition")
GamlDefinition = Class(name="GamlDefinition")
gaml_TypeDefinition = Class(name="gaml::TypeDefinition")
gaml_ActionDefinition = Class(name="gaml::ActionDefinition")
gaml_UnitFakeDefinition = Class(name="gaml::UnitFakeDefinition")
gaml_TypeFakeDefinition = Class(name="gaml::TypeFakeDefinition")
gaml_ActionFakeDefinition = Class(name="gaml::ActionFakeDefinition")
gaml_SkillFakeDefinition = Class(name="gaml::SkillFakeDefinition")
gaml_VarFakeDefinition = Class(name="gaml::VarFakeDefinition")
gaml_EquationFakeDefinition = Class(name="gaml::EquationFakeDefinition")
gaml_TerminalExpression = Class(name="gaml::TerminalExpression")
gaml_S_Action = Class(name="gaml::S::Action")
S_Definition = Class(name="S::Definition")
gaml_S_Var = Class(name="gaml::S::Var")
gaml_Pair = Class(name="gaml::Pair")
gaml_If = Class(name="gaml::If")
gaml_Cast = Class(name="gaml::Cast")
gaml_BooleanLiteral = Class(name="gaml::BooleanLiteral")
gaml_ReservedLiteral = Class(name="gaml::ReservedLiteral")
gaml_TypeRef = Class(name="gaml::TypeRef")
gaml_SkillRef = Class(name="gaml::SkillRef")
gaml_ActionRef = Class(name="gaml::ActionRef")
gaml_EquationRef = Class(name="gaml::EquationRef")
gaml_IntLiteral = Class(name="gaml::IntLiteral")
TerminalExpression = Class(name="TerminalExpression")
gaml_DoubleLiteral = Class(name="gaml::DoubleLiteral")
gaml_ColorLiteral = Class(name="gaml::ColorLiteral")
gaml_StringLiteral = Class(name="gaml::StringLiteral")

# gaml_Entry class attributes and methods

# gaml_StandaloneBlock class attributes and methods

# Entry class attributes and methods

# gaml_Block class attributes and methods

# gaml_StringEvaluator class attributes and methods
gaml_StringEvaluator_toto: Property = Property(name="toto", type=StringType)
gaml_StringEvaluator.attributes={gaml_StringEvaluator_toto}

# gaml_Expression class attributes and methods
gaml_Expression_op: Property = Property(name="op", type=StringType)
gaml_Expression.attributes={gaml_Expression_op}

# gaml_Model class attributes and methods

# VarDefinition class attributes and methods

# gaml_Pragma class attributes and methods
gaml_Pragma_name: Property = Property(name="name", type=StringType)
gaml_Pragma.attributes={gaml_Pragma_name}

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
gaml_HeadlessExperiment.attributes={gaml_HeadlessExperiment_key, gaml_HeadlessExperiment_name, gaml_HeadlessExperiment_firstFacet, gaml_HeadlessExperiment_importURI}

# EquationDefinition class attributes and methods

# gaml_S_Solve class attributes and methods

# gaml_S_Display class attributes and methods
gaml_S_Display_name: Property = Property(name="name", type=StringType)
gaml_S_Display.attributes={gaml_S_Display_name}

# gaml_speciesOrGridDisplayStatement class attributes and methods

# gaml_Parameters class attributes and methods

# Expression class attributes and methods

# gaml_ExpressionList class attributes and methods

# gaml_ArgumentDefinition class attributes and methods

# gaml_S_Loop class attributes and methods

# gaml_S_If class attributes and methods

# gaml_EObject class attributes and methods

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

# gaml_TypeInfo class attributes and methods

# gaml_VariableRef class attributes and methods

# gaml_VarDefinition class attributes and methods

# gaml_GamlDefinition class attributes and methods
gaml_GamlDefinition_name: Property = Property(name="name", type=StringType)
gaml_GamlDefinition.attributes={gaml_GamlDefinition_name}

# gaml_ArgumentPair class attributes and methods

# gaml_Function class attributes and methods

# gaml_Binary class attributes and methods

# gaml_Unit class attributes and methods

# gaml_Unary class attributes and methods

# gaml_Access class attributes and methods
gaml_Access_named_exp: Property = Property(name="named_exp", type=StringType)
gaml_Access.attributes={gaml_Access_named_exp}

# gaml_Array class attributes and methods

# gaml_Point class attributes and methods

# gaml_Parameter class attributes and methods
gaml_Parameter_builtInFacetKey: Property = Property(name="builtInFacetKey", type=StringType)
gaml_Parameter.attributes={gaml_Parameter_builtInFacetKey}

# gaml_UnitName class attributes and methods

# gaml_EquationDefinition class attributes and methods

# GamlDefinition class attributes and methods

# gaml_TypeDefinition class attributes and methods

# gaml_ActionDefinition class attributes and methods

# gaml_UnitFakeDefinition class attributes and methods

# gaml_TypeFakeDefinition class attributes and methods

# gaml_ActionFakeDefinition class attributes and methods

# gaml_SkillFakeDefinition class attributes and methods

# gaml_VarFakeDefinition class attributes and methods

# gaml_EquationFakeDefinition class attributes and methods

# gaml_TerminalExpression class attributes and methods

# gaml_S_Action class attributes and methods

# S_Definition class attributes and methods

# gaml_S_Var class attributes and methods

# gaml_Pair class attributes and methods

# gaml_If class attributes and methods

# gaml_Cast class attributes and methods

# gaml_BooleanLiteral class attributes and methods

# gaml_ReservedLiteral class attributes and methods

# gaml_TypeRef class attributes and methods

# gaml_SkillRef class attributes and methods

# gaml_ActionRef class attributes and methods

# gaml_EquationRef class attributes and methods

# gaml_IntLiteral class attributes and methods

# TerminalExpression class attributes and methods

# gaml_DoubleLiteral class attributes and methods

# gaml_ColorLiteral class attributes and methods

# gaml_StringLiteral class attributes and methods

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
facets14: BinaryAssociation = BinaryAssociation(
    name="facets14",
    ends={
        Property(name="gaml_Facet", type=gaml_HeadlessExperiment, multiplicity=Multiplicity(1, 1)),
        Property(name="gaml_HeadlessExperiment15", type=gaml_Facet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
block16: BinaryAssociation = BinaryAssociation(
    name="block16",
    ends={
        Property(name="gaml_Block18", type=gaml_HeadlessExperiment, multiplicity=Multiplicity(1, 1)),
        Property(name="gaml_HeadlessExperiment17", type=gaml_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr19: BinaryAssociation = BinaryAssociation(
    name="expr19",
    ends={
        Property(name="gaml_Expression21", type=gaml_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="gaml_Statement20", type=gaml_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
facets22: BinaryAssociation = BinaryAssociation(
    name="facets22",
    ends={
        Property(name="gaml_Facet24", type=gaml_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="gaml_Statement23", type=gaml_Facet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
block25: BinaryAssociation = BinaryAssociation(
    name="block25",
    ends={
        Property(name="gaml_Block27", type=gaml_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="gaml_Statement26", type=gaml_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
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
function10: BinaryAssociation = BinaryAssociation(
    name="function10",
    ends={
        Property(name="gaml_Expression12", type=gaml_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="gaml_Block11", type=gaml_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp13: BinaryAssociation = BinaryAssociation(
    name="exp13",
    ends={
        Property(name="gaml_HeadlessExperiment", type=gaml_ExperimentFileStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="gaml_ExperimentFileStructure", type=gaml_HeadlessExperiment, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
equations35: BinaryAssociation = BinaryAssociation(
    name="equations35",
    ends={
        Property(name="gaml_S_Assignment36", type=gaml_S_Equations, multiplicity=Multiplicity(1, 1)),
        Property(name="gaml_S_Equations", type=gaml_S_Assignment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
params37: BinaryAssociation = BinaryAssociation(
    name="params37",
    ends={
        Property(name="gaml_ExpressionList", type=gaml_Parameters, multiplicity=Multiplicity(1, 1)),
        Property(name="gaml_Parameters", type=gaml_ExpressionList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
args38: BinaryAssociation = BinaryAssociation(
    name="args38",
    ends={
        Property(name="gaml_ArgumentDefinition", type=gaml_ActionArguments, multiplicity=Multiplicity(1, 1)),
        Property(name="gaml_ActionArguments39", type=gaml_ArgumentDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type40: BinaryAssociation = BinaryAssociation(
    name="type40",
    ends={
        Property(name="gaml_Expression42", type=gaml_ArgumentDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="gaml_ArgumentDefinition41", type=gaml_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
else28: BinaryAssociation = BinaryAssociation(
    name="else28",
    ends={
        Property(name="gaml_EObject", type=gaml_S_If, multiplicity=Multiplicity(1, 1)),
        Property(name="gaml_S_If", type=gaml_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tkey29: BinaryAssociation = BinaryAssociation(
    name="tkey29",
    ends={
        Property(name="gaml_Expression30", type=gaml_S_Definition, multiplicity=Multiplicity(1, 1)),
        Property(name="gaml_S_Definition", type=gaml_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
args31: BinaryAssociation = BinaryAssociation(
    name="args31",
    ends={
        Property(name="gaml_ActionArguments", type=gaml_S_Definition, multiplicity=Multiplicity(1, 1)),
        Property(name="gaml_S_Definition32", type=gaml_ActionArguments, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value33: BinaryAssociation = BinaryAssociation(
    name="value33",
    ends={
        Property(name="gaml_Expression34", type=gaml_S_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="gaml_S_Assignment", type=gaml_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
args63: BinaryAssociation = BinaryAssociation(
    name="args63",
    ends={
        Property(name="gaml_ExpressionList65", type=gaml_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="gaml_Function64", type=gaml_ExpressionList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type66: BinaryAssociation = BinaryAssociation(
    name="type66",
    ends={
        Property(name="gaml_TypeInfo", type=gaml_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="gaml_Function67", type=gaml_TypeInfo, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exprs68: BinaryAssociation = BinaryAssociation(
    name="exprs68",
    ends={
        Property(name="gaml_Expression70", type=gaml_ExpressionList, multiplicity=Multiplicity(1, 1)),
        Property(name="gaml_ExpressionList69", type=gaml_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ref71: BinaryAssociation = BinaryAssociation(
    name="ref71",
    ends={
        Property(name="gaml_VarDefinition", type=gaml_VariableRef, multiplicity=Multiplicity(1, 1)),
        Property(name="gaml_VariableRef", type=gaml_VarDefinition, multiplicity=Multiplicity(0, 1))
    }
)
first72: BinaryAssociation = BinaryAssociation(
    name="first72",
    ends={
        Property(name="gaml_Expression74", type=gaml_TypeInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="gaml_TypeInfo73", type=gaml_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
second75: BinaryAssociation = BinaryAssociation(
    name="second75",
    ends={
        Property(name="gaml_Expression77", type=gaml_TypeInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="gaml_TypeInfo76", type=gaml_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
default43: BinaryAssociation = BinaryAssociation(
    name="default43",
    ends={
        Property(name="gaml_Expression45", type=gaml_ArgumentDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="gaml_ArgumentDefinition44", type=gaml_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr46: BinaryAssociation = BinaryAssociation(
    name="expr46",
    ends={
        Property(name="gaml_Expression48", type=gaml_Facet, multiplicity=Multiplicity(1, 1)),
        Property(name="gaml_Facet47", type=gaml_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block49: BinaryAssociation = BinaryAssociation(
    name="block49",
    ends={
        Property(name="gaml_Block51", type=gaml_Facet, multiplicity=Multiplicity(1, 1)),
        Property(name="gaml_Facet50", type=gaml_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left53: BinaryAssociation = BinaryAssociation(
    name="left53",
    ends={
        Property(name="gaml_Expression54", type=gaml_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="gaml_Expression52", type=gaml_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right56: BinaryAssociation = BinaryAssociation(
    name="right56",
    ends={
        Property(name="gaml_Expression57", type=gaml_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="gaml_Expression55", type=gaml_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
action58: BinaryAssociation = BinaryAssociation(
    name="action58",
    ends={
        Property(name="gaml_Expression59", type=gaml_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="gaml_Function", type=gaml_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters60: BinaryAssociation = BinaryAssociation(
    name="parameters60",
    ends={
        Property(name="gaml_Parameters62", type=gaml_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="gaml_Function61", type=gaml_Parameters, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
args80: BinaryAssociation = BinaryAssociation(
    name="args80",
    ends={
        Property(name="gaml_ExpressionList81", type=gaml_Access, multiplicity=Multiplicity(1, 1)),
        Property(name="gaml_Access", type=gaml_ExpressionList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exprs82: BinaryAssociation = BinaryAssociation(
    name="exprs82",
    ends={
        Property(name="gaml_ExpressionList83", type=gaml_Array, multiplicity=Multiplicity(1, 1)),
        Property(name="gaml_Array", type=gaml_ExpressionList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
z84: BinaryAssociation = BinaryAssociation(
    name="z84",
    ends={
        Property(name="gaml_Expression85", type=gaml_Point, multiplicity=Multiplicity(1, 1)),
        Property(name="gaml_Point", type=gaml_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ifFalse78: BinaryAssociation = BinaryAssociation(
    name="ifFalse78",
    ends={
        Property(name="gaml_Expression79", type=gaml_If, multiplicity=Multiplicity(1, 1)),
        Property(name="gaml_If", type=gaml_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ref86: BinaryAssociation = BinaryAssociation(
    name="ref86",
    ends={
        Property(name="gaml_UnitFakeDefinition", type=gaml_UnitName, multiplicity=Multiplicity(1, 1)),
        Property(name="gaml_UnitName", type=gaml_UnitFakeDefinition, multiplicity=Multiplicity(0, 1))
    }
)
ref87: BinaryAssociation = BinaryAssociation(
    name="ref87",
    ends={
        Property(name="gaml_TypeDefinition", type=gaml_TypeRef, multiplicity=Multiplicity(1, 1)),
        Property(name="gaml_TypeRef", type=gaml_TypeDefinition, multiplicity=Multiplicity(0, 1))
    }
)
parameter88: BinaryAssociation = BinaryAssociation(
    name="parameter88",
    ends={
        Property(name="gaml_TypeInfo90", type=gaml_TypeRef, multiplicity=Multiplicity(1, 1)),
        Property(name="gaml_TypeRef89", type=gaml_TypeInfo, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ref91: BinaryAssociation = BinaryAssociation(
    name="ref91",
    ends={
        Property(name="gaml_SkillFakeDefinition", type=gaml_SkillRef, multiplicity=Multiplicity(1, 1)),
        Property(name="gaml_SkillRef", type=gaml_SkillFakeDefinition, multiplicity=Multiplicity(0, 1))
    }
)
ref92: BinaryAssociation = BinaryAssociation(
    name="ref92",
    ends={
        Property(name="gaml_ActionDefinition", type=gaml_ActionRef, multiplicity=Multiplicity(1, 1)),
        Property(name="gaml_ActionRef", type=gaml_ActionDefinition, multiplicity=Multiplicity(0, 1))
    }
)
ref93: BinaryAssociation = BinaryAssociation(
    name="ref93",
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
gen_gaml_S_Global_Statement = Generalization(general=Statement, specific=gaml_S_Global)
gen_gaml_S_Species_Statement = Generalization(general=Statement, specific=gaml_S_Species)
gen_gaml_S_Species_S_Declaration = Generalization(general=S_Declaration, specific=gaml_S_Species)
gen_gaml_S_Species_TypeDefinition = Generalization(general=TypeDefinition, specific=gaml_S_Species)
gen_gaml_S_Experiment_Statement = Generalization(general=Statement, specific=gaml_S_Experiment)
gen_gaml_S_Experiment_VarDefinition = Generalization(general=VarDefinition, specific=gaml_S_Experiment)
gen_gaml_S_Do_Statement = Generalization(general=Statement, specific=gaml_S_Do)
gen_gaml_Import_VarDefinition = Generalization(general=VarDefinition, specific=gaml_Import)
gen_gaml_ExperimentFileStructure_Entry = Generalization(general=Entry, specific=gaml_ExperimentFileStructure)
gen_gaml_S_Equations_EquationDefinition = Generalization(general=EquationDefinition, specific=gaml_S_Equations)
gen_gaml_S_Solve_Statement = Generalization(general=Statement, specific=gaml_S_Solve)
gen_gaml_S_Display_Statement = Generalization(general=Statement, specific=gaml_S_Display)
gen_gaml_speciesOrGridDisplayStatement_Statement = Generalization(general=Statement, specific=gaml_speciesOrGridDisplayStatement)
gen_gaml_Parameters_Expression = Generalization(general=Expression, specific=gaml_Parameters)
gen_gaml_ArgumentDefinition_VarDefinition = Generalization(general=VarDefinition, specific=gaml_ArgumentDefinition)
gen_gaml_S_Loop_S_Declaration = Generalization(general=S_Declaration, specific=gaml_S_Loop)
gen_gaml_S_If_Statement = Generalization(general=Statement, specific=gaml_S_If)
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
gen_gaml_ExpressionList_Expression = Generalization(general=Expression, specific=gaml_ExpressionList)
gen_gaml_VariableRef_Expression = Generalization(general=Expression, specific=gaml_VariableRef)
gen_gaml_Facet_VarDefinition = Generalization(general=VarDefinition, specific=gaml_Facet)
gen_gaml_ArgumentPair_Expression = Generalization(general=Expression, specific=gaml_ArgumentPair)
gen_gaml_Function_Expression = Generalization(general=Expression, specific=gaml_Function)
gen_gaml_Cast_Expression = Generalization(general=Expression, specific=gaml_Cast)
gen_gaml_Binary_Expression = Generalization(general=Expression, specific=gaml_Binary)
gen_gaml_Unit_Expression = Generalization(general=Expression, specific=gaml_Unit)
gen_gaml_Unary_Expression = Generalization(general=Expression, specific=gaml_Unary)
gen_gaml_Access_Expression = Generalization(general=Expression, specific=gaml_Access)
gen_gaml_Array_Expression = Generalization(general=Expression, specific=gaml_Array)
gen_gaml_Point_Expression = Generalization(general=Expression, specific=gaml_Point)
gen_gaml_Parameter_Expression = Generalization(general=Expression, specific=gaml_Parameter)
gen_gaml_UnitName_Expression = Generalization(general=Expression, specific=gaml_UnitName)
gen_gaml_EquationDefinition_GamlDefinition = Generalization(general=GamlDefinition, specific=gaml_EquationDefinition)
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
gen_gaml_S_Action_S_Definition = Generalization(general=S_Definition, specific=gaml_S_Action)
gen_gaml_S_Var_S_Definition = Generalization(general=S_Definition, specific=gaml_S_Var)
gen_gaml_Pair_Expression = Generalization(general=Expression, specific=gaml_Pair)
gen_gaml_If_Expression = Generalization(general=Expression, specific=gaml_If)
gen_gaml_BooleanLiteral_TerminalExpression = Generalization(general=TerminalExpression, specific=gaml_BooleanLiteral)
gen_gaml_ReservedLiteral_TerminalExpression = Generalization(general=TerminalExpression, specific=gaml_ReservedLiteral)
gen_gaml_TypeRef_Expression = Generalization(general=Expression, specific=gaml_TypeRef)
gen_gaml_SkillRef_Expression = Generalization(general=Expression, specific=gaml_SkillRef)
gen_gaml_ActionRef_Expression = Generalization(general=Expression, specific=gaml_ActionRef)
gen_gaml_EquationRef_Expression = Generalization(general=Expression, specific=gaml_EquationRef)
gen_gaml_IntLiteral_TerminalExpression = Generalization(general=TerminalExpression, specific=gaml_IntLiteral)
gen_gaml_DoubleLiteral_TerminalExpression = Generalization(general=TerminalExpression, specific=gaml_DoubleLiteral)
gen_gaml_ColorLiteral_TerminalExpression = Generalization(general=TerminalExpression, specific=gaml_ColorLiteral)
gen_gaml_StringLiteral_TerminalExpression = Generalization(general=TerminalExpression, specific=gaml_StringLiteral)

# Domain Model
domain_model = DomainModel(
    name="gaml",
    types={gaml_Entry, gaml_StandaloneBlock, Entry, gaml_Block, gaml_StringEvaluator, gaml_Expression, gaml_Model, VarDefinition, gaml_Pragma, gaml_Facet, gaml_S_Global, Statement, gaml_S_Species, S_Declaration, TypeDefinition, gaml_S_Experiment, gaml_S_Do, gaml_Import, gaml_Statement, gaml_ExperimentFileStructure, gaml_HeadlessExperiment, EquationDefinition, gaml_S_Solve, gaml_S_Display, gaml_speciesOrGridDisplayStatement, gaml_Parameters, Expression, gaml_ExpressionList, gaml_ArgumentDefinition, gaml_S_Loop, gaml_S_If, gaml_EObject, gaml_S_Other, gaml_S_Return, gaml_S_Declaration, gaml_S_Reflex, gaml_S_Definition, ActionDefinition, gaml_ActionArguments, gaml_S_Assignment, gaml_S_DirectAssignment, S_Assignment, gaml_S_Set, gaml_S_Equations, gaml_TypeInfo, gaml_VariableRef, gaml_VarDefinition, gaml_GamlDefinition, gaml_ArgumentPair, gaml_Function, gaml_Binary, gaml_Unit, gaml_Unary, gaml_Access, gaml_Array, gaml_Point, gaml_Parameter, gaml_UnitName, gaml_EquationDefinition, GamlDefinition, gaml_TypeDefinition, gaml_ActionDefinition, gaml_UnitFakeDefinition, gaml_TypeFakeDefinition, gaml_ActionFakeDefinition, gaml_SkillFakeDefinition, gaml_VarFakeDefinition, gaml_EquationFakeDefinition, gaml_TerminalExpression, gaml_S_Action, S_Definition, gaml_S_Var, gaml_Pair, gaml_If, gaml_Cast, gaml_BooleanLiteral, gaml_ReservedLiteral, gaml_TypeRef, gaml_SkillRef, gaml_ActionRef, gaml_EquationRef, gaml_IntLiteral, TerminalExpression, gaml_DoubleLiteral, gaml_ColorLiteral, gaml_StringLiteral},
    associations={block0, expr1, pragmas2, facets14, block16, expr19, facets22, block25, imports3, block5, statements8, function10, exp13, equations35, params37, args38, type40, else28, tkey29, args31, value33, args63, type66, exprs68, ref71, first72, second75, default43, expr46, block49, left53, right56, action58, parameters60, args80, exprs82, z84, ifFalse78, ref86, ref87, parameter88, ref91, ref92, ref93},
    generalizations={gen_gaml_StandaloneBlock_Entry, gen_gaml_StringEvaluator_Entry, gen_gaml_Model_Entry, gen_gaml_Model_VarDefinition, gen_gaml_S_Global_Statement, gen_gaml_S_Species_Statement, gen_gaml_S_Species_S_Declaration, gen_gaml_S_Species_TypeDefinition, gen_gaml_S_Experiment_Statement, gen_gaml_S_Experiment_VarDefinition, gen_gaml_S_Do_Statement, gen_gaml_Import_VarDefinition, gen_gaml_ExperimentFileStructure_Entry, gen_gaml_S_Equations_EquationDefinition, gen_gaml_S_Solve_Statement, gen_gaml_S_Display_Statement, gen_gaml_speciesOrGridDisplayStatement_Statement, gen_gaml_Parameters_Expression, gen_gaml_ArgumentDefinition_VarDefinition, gen_gaml_S_Loop_S_Declaration, gen_gaml_S_If_Statement, gen_gaml_S_Other_Statement, gen_gaml_S_Return_Statement, gen_gaml_S_Declaration_Statement, gen_gaml_S_Declaration_VarDefinition, gen_gaml_S_Reflex_S_Declaration, gen_gaml_S_Definition_S_Declaration, gen_gaml_S_Definition_ActionDefinition, gen_gaml_S_Assignment_Statement, gen_gaml_S_DirectAssignment_S_Assignment, gen_gaml_S_Set_S_Assignment, gen_gaml_S_Equations_Statement, gen_gaml_ExpressionList_Expression, gen_gaml_VariableRef_Expression, gen_gaml_Facet_VarDefinition, gen_gaml_ArgumentPair_Expression, gen_gaml_Function_Expression, gen_gaml_Cast_Expression, gen_gaml_Binary_Expression, gen_gaml_Unit_Expression, gen_gaml_Unary_Expression, gen_gaml_Access_Expression, gen_gaml_Array_Expression, gen_gaml_Point_Expression, gen_gaml_Parameter_Expression, gen_gaml_UnitName_Expression, gen_gaml_EquationDefinition_GamlDefinition, gen_gaml_TypeDefinition_GamlDefinition, gen_gaml_TypeDefinition_ActionDefinition, gen_gaml_VarDefinition_GamlDefinition, gen_gaml_ActionDefinition_GamlDefinition, gen_gaml_UnitFakeDefinition_GamlDefinition, gen_gaml_TypeFakeDefinition_TypeDefinition, gen_gaml_ActionFakeDefinition_ActionDefinition, gen_gaml_SkillFakeDefinition_GamlDefinition, gen_gaml_VarFakeDefinition_VarDefinition, gen_gaml_EquationFakeDefinition_EquationDefinition, gen_gaml_TerminalExpression_Expression, gen_gaml_S_Action_S_Definition, gen_gaml_S_Var_S_Definition, gen_gaml_Pair_Expression, gen_gaml_If_Expression, gen_gaml_BooleanLiteral_TerminalExpression, gen_gaml_ReservedLiteral_TerminalExpression, gen_gaml_TypeRef_Expression, gen_gaml_SkillRef_Expression, gen_gaml_ActionRef_Expression, gen_gaml_EquationRef_Expression, gen_gaml_IntLiteral_TerminalExpression, gen_gaml_DoubleLiteral_TerminalExpression, gen_gaml_ColorLiteral_TerminalExpression, gen_gaml_StringLiteral_TerminalExpression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)