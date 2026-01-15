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
Verdict: Enumeration = Enumeration(
    name="Verdict",
    literals={
            EnumerationLiteral(name="none"),
			EnumerationLiteral(name="pass"),
			EnumerationLiteral(name="fail")
    }
)

# Classes
diva_BaseModel = Class(name="diva::BaseModel")
Model = Class(name="Model")
diva_AspectModel = Class(name="diva::AspectModel")
diva_EnumVariable = Class(name="diva::EnumVariable")
Variable = Class(name="Variable")
diva_EnumLiteral = Class(name="diva::EnumLiteral")
diva_BooleanVariable = Class(name="diva::BooleanVariable")
diva_Term = Class(name="diva::Term", is_abstract=True)
diva_AndTerm = Class(name="diva::AndTerm")
NaryTerm = Class(name="NaryTerm")
diva_OrTerm = Class(name="diva::OrTerm")
diva_NotTerm = Class(name="diva::NotTerm")
Term = Class(name="Term")
diva_VariabilityModel = Class(name="diva::VariabilityModel")
ModelContainer = Class(name="ModelContainer")
diva_Variable = Class(name="diva::Variable", is_abstract=True)
diva_Property = Class(name="diva::Property")
diva_Dimension = Class(name="diva::Dimension")
diva_Rule = Class(name="diva::Rule", is_abstract=True)
diva_Constraint = Class(name="diva::Constraint", is_abstract=True)
diva_SimulationModel = Class(name="diva::SimulationModel")
diva_Invariant = Class(name="diva::Invariant")
Constraint = Class(name="Constraint")
diva_Expression = Class(name="diva::Expression")
NamedElement = Class(name="NamedElement")
diva_Model = Class(name="diva::Model", is_abstract=True)
DiVAModelElement = Class(name="DiVAModelElement")
diva_PropertyValue = Class(name="diva::PropertyValue")
diva_VariantExpression = Class(name="diva::VariantExpression")
diva_ContextExpression = Class(name="diva::ContextExpression")
diva_NaryTerm = Class(name="diva::NaryTerm", is_abstract=True)
diva_VariantTerm = Class(name="diva::VariantTerm")
diva_Variant = Class(name="diva::Variant")
diva_VariableTerm = Class(name="diva::VariableTerm", is_abstract=True)
diva_EnumTerm = Class(name="diva::EnumTerm")
VariableTerm = Class(name="VariableTerm")
diva_BooleanTerm = Class(name="diva::BooleanTerm")
diva_NamedElement = Class(name="diva::NamedElement", is_abstract=True)
diva_MultiplicityConstraint = Class(name="diva::MultiplicityConstraint")
Expression = Class(name="Expression")
diva_PriorityRule = Class(name="diva::PriorityRule")
Rule = Class(name="Rule")
diva_PropertyPriority = Class(name="diva::PropertyPriority")
diva_PropertyLiteral = Class(name="diva::PropertyLiteral")
diva_ScoredElement = Class(name="diva::ScoredElement", is_abstract=True)
diva_Score = Class(name="diva::Score")
diva_Annotation = Class(name="diva::Annotation")
diva_DiVAModelElement = Class(name="diva::DiVAModelElement", is_abstract=True)
diva_Scenario = Class(name="diva::Scenario")
diva_Context = Class(name="diva::Context")
diva_VariableValue = Class(name="diva::VariableValue", is_abstract=True)
diva_Configuration = Class(name="diva::Configuration")
diva_Priority = Class(name="diva::Priority")
ScoredElement = Class(name="ScoredElement")
diva_ConfigVariant = Class(name="diva::ConfigVariant")
diva_ModelContainer = Class(name="diva::ModelContainer", is_abstract=True)
diva_BoolVariableValue = Class(name="diva::BoolVariableValue")
VariableValue = Class(name="VariableValue")
diva_EnumVariableValue = Class(name="diva::EnumVariableValue")
diva_ConfigurationModel = Class(name="diva::ConfigurationModel")
diva_SuitableConfiguration = Class(name="diva::SuitableConfiguration")
diva_ContextModel = Class(name="diva::ContextModel")

# diva_BaseModel class attributes and methods
diva_BaseModel_m_weave: Method = Method(name="weave", parameters={})
diva_BaseModel.methods={diva_BaseModel_m_weave}

# Model class attributes and methods

# diva_AspectModel class attributes and methods

# diva_EnumVariable class attributes and methods

# Variable class attributes and methods

# diva_EnumLiteral class attributes and methods

# diva_BooleanVariable class attributes and methods

# diva_Term class attributes and methods

# diva_AndTerm class attributes and methods

# NaryTerm class attributes and methods

# diva_OrTerm class attributes and methods

# diva_NotTerm class attributes and methods

# Term class attributes and methods

# diva_VariabilityModel class attributes and methods

# ModelContainer class attributes and methods

# diva_Variable class attributes and methods

# diva_Property class attributes and methods
diva_Property_direction: Property = Property(name="direction", type=StringType)
diva_Property.attributes={diva_Property_direction}

# diva_Dimension class attributes and methods
diva_Dimension_upper: Property = Property(name="upper", type=StringType)
diva_Dimension_lower: Property = Property(name="lower", type=StringType)
diva_Dimension.attributes={diva_Dimension_upper, diva_Dimension_lower}

# diva_Rule class attributes and methods

# diva_Constraint class attributes and methods

# diva_SimulationModel class attributes and methods

# diva_Invariant class attributes and methods

# Constraint class attributes and methods

# diva_Expression class attributes and methods
diva_Expression_text: Property = Property(name="text", type=StringType)
diva_Expression.attributes={diva_Expression_text}

# NamedElement class attributes and methods

# diva_Model class attributes and methods
diva_Model_uri: Property = Property(name="uri", type=StringType)
diva_Model.attributes={diva_Model_uri}

# DiVAModelElement class attributes and methods

# diva_PropertyValue class attributes and methods
diva_PropertyValue_value: Property = Property(name="value", type=StringType)
diva_PropertyValue.attributes={diva_PropertyValue_value}

# diva_VariantExpression class attributes and methods

# diva_ContextExpression class attributes and methods

# diva_NaryTerm class attributes and methods

# diva_VariantTerm class attributes and methods

# diva_Variant class attributes and methods
diva_Variant_weaveLevel: Property = Property(name="weaveLevel", type=StringType)
diva_Variant.attributes={diva_Variant_weaveLevel}

# diva_VariableTerm class attributes and methods

# diva_EnumTerm class attributes and methods

# VariableTerm class attributes and methods

# diva_BooleanTerm class attributes and methods

# diva_NamedElement class attributes and methods
diva_NamedElement_name: Property = Property(name="name", type=StringType)
diva_NamedElement_id: Property = Property(name="id", type=StringType)
diva_NamedElement.attributes={diva_NamedElement_name, diva_NamedElement_id}

# diva_MultiplicityConstraint class attributes and methods
diva_MultiplicityConstraint_upper: Property = Property(name="upper", type=StringType)
diva_MultiplicityConstraint_lower: Property = Property(name="lower", type=StringType)
diva_MultiplicityConstraint.attributes={diva_MultiplicityConstraint_lower, diva_MultiplicityConstraint_upper}

# Expression class attributes and methods

# diva_PriorityRule class attributes and methods

# Rule class attributes and methods

# diva_PropertyPriority class attributes and methods
diva_PropertyPriority_priority: Property = Property(name="priority", type=StringType)
diva_PropertyPriority.attributes={diva_PropertyPriority_priority}

# diva_PropertyLiteral class attributes and methods
diva_PropertyLiteral_value: Property = Property(name="value", type=StringType)
diva_PropertyLiteral.attributes={diva_PropertyLiteral_value}

# diva_ScoredElement class attributes and methods
diva_ScoredElement_totalScore: Property = Property(name="totalScore", type=IntegerType)
diva_ScoredElement.attributes={diva_ScoredElement_totalScore}

# diva_Score class attributes and methods
diva_Score_score: Property = Property(name="score", type=IntegerType)
diva_Score.attributes={diva_Score_score}

# diva_Annotation class attributes and methods
diva_Annotation_key: Property = Property(name="key", type=StringType)
diva_Annotation_value: Property = Property(name="value", type=StringType)
diva_Annotation.attributes={diva_Annotation_value, diva_Annotation_key}

# diva_DiVAModelElement class attributes and methods

# diva_Scenario class attributes and methods

# diva_Context class attributes and methods
diva_Context_verdict: Property = Property(name="verdict", type=StringType)
diva_Context.attributes={diva_Context_verdict}

# diva_VariableValue class attributes and methods

# diva_Configuration class attributes and methods
diva_Configuration_verdict: Property = Property(name="verdict", type=StringType)
diva_Configuration.attributes={diva_Configuration_verdict}

# diva_Priority class attributes and methods
diva_Priority_priority: Property = Property(name="priority", type=IntegerType)
diva_Priority.attributes={diva_Priority_priority}

# ScoredElement class attributes and methods

# diva_ConfigVariant class attributes and methods

# diva_ModelContainer class attributes and methods

# diva_BoolVariableValue class attributes and methods
diva_BoolVariableValue_bool: Property = Property(name="bool", type=BooleanType)
diva_BoolVariableValue.attributes={diva_BoolVariableValue_bool}

# VariableValue class attributes and methods

# diva_EnumVariableValue class attributes and methods

# diva_ConfigurationModel class attributes and methods

# diva_SuitableConfiguration class attributes and methods
diva_SuitableConfiguration_score: Property = Property(name="score", type=IntegerType)
diva_SuitableConfiguration.attributes={diva_SuitableConfiguration_score}

# diva_ContextModel class attributes and methods

# Relationships
literal11: BinaryAssociation = BinaryAssociation(
    name="literal11",
    ends={
        Property(name="diva_EnumLiteral", type=diva_EnumVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_EnumVariable", type=diva_EnumLiteral, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
term12: BinaryAssociation = BinaryAssociation(
    name="term12",
    ends={
        Property(name="diva_Term", type=diva_NotTerm, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_NotTerm", type=diva_Term, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
context0: BinaryAssociation = BinaryAssociation(
    name="context0",
    ends={
        Property(name="diva_Variable", type=diva_VariabilityModel, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_VariabilityModel", type=diva_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
property1: BinaryAssociation = BinaryAssociation(
    name="property1",
    ends={
        Property(name="diva_Property", type=diva_VariabilityModel, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_VariabilityModel2", type=diva_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dimension3: BinaryAssociation = BinaryAssociation(
    name="dimension3",
    ends={
        Property(name="diva_Dimension", type=diva_VariabilityModel, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_VariabilityModel4", type=diva_Dimension, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rule5: BinaryAssociation = BinaryAssociation(
    name="rule5",
    ends={
        Property(name="diva_Rule", type=diva_VariabilityModel, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_VariabilityModel6", type=diva_Rule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
constraint7: BinaryAssociation = BinaryAssociation(
    name="constraint7",
    ends={
        Property(name="diva_Constraint", type=diva_VariabilityModel, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_VariabilityModel8", type=diva_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
simulation9: BinaryAssociation = BinaryAssociation(
    name="simulation9",
    ends={
        Property(name="SimulationModel", type=diva_VariabilityModel, multiplicity=Multiplicity(1, 1)),
        Property(name="model", type=diva_SimulationModel, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression10: BinaryAssociation = BinaryAssociation(
    name="expression10",
    ends={
        Property(name="diva_Expression", type=diva_Invariant, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_Invariant", type=diva_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type20: BinaryAssociation = BinaryAssociation(
    name="type20",
    ends={
        Property(name="Dimension", type=diva_Variant, multiplicity=Multiplicity(1, 1)),
        Property(name="variant", type=diva_Dimension, multiplicity=Multiplicity(1, 1))
    }
)
propertyValue21: BinaryAssociation = BinaryAssociation(
    name="propertyValue21",
    ends={
        Property(name="diva_PropertyValue", type=diva_Variant, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_Variant22", type=diva_PropertyValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dependency23: BinaryAssociation = BinaryAssociation(
    name="dependency23",
    ends={
        Property(name="diva_VariantExpression", type=diva_Variant, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_Variant24", type=diva_VariantExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
available25: BinaryAssociation = BinaryAssociation(
    name="available25",
    ends={
        Property(name="diva_ContextExpression", type=diva_Variant, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_Variant26", type=diva_ContextExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
required27: BinaryAssociation = BinaryAssociation(
    name="required27",
    ends={
        Property(name="diva_ContextExpression29", type=diva_Variant, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_Variant28", type=diva_ContextExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variant30: BinaryAssociation = BinaryAssociation(
    name="variant30",
    ends={
        Property(name="Variant", type=diva_Dimension, multiplicity=Multiplicity(1, 1)),
        Property(name="type", type=diva_Variant, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
term13: BinaryAssociation = BinaryAssociation(
    name="term13",
    ends={
        Property(name="diva_Term14", type=diva_NaryTerm, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_NaryTerm", type=diva_Term, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
variant15: BinaryAssociation = BinaryAssociation(
    name="variant15",
    ends={
        Property(name="diva_Variant", type=diva_VariantTerm, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_VariantTerm", type=diva_Variant, multiplicity=Multiplicity(1, 1))
    }
)
variable16: BinaryAssociation = BinaryAssociation(
    name="variable16",
    ends={
        Property(name="diva_Variable17", type=diva_VariableTerm, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_VariableTerm", type=diva_Variable, multiplicity=Multiplicity(1, 1))
    }
)
value18: BinaryAssociation = BinaryAssociation(
    name="value18",
    ends={
        Property(name="diva_EnumLiteral19", type=diva_EnumTerm, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_EnumTerm", type=diva_EnumLiteral, multiplicity=Multiplicity(1, 1))
    }
)
property45: BinaryAssociation = BinaryAssociation(
    name="property45",
    ends={
        Property(name="diva_Property47", type=diva_PropertyValue, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_PropertyValue46", type=diva_Property, multiplicity=Multiplicity(1, 1))
    }
)
property48: BinaryAssociation = BinaryAssociation(
    name="property48",
    ends={
        Property(name="diva_Property50", type=diva_PropertyPriority, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_PropertyPriority49", type=diva_Property, multiplicity=Multiplicity(1, 1))
    }
)
available51: BinaryAssociation = BinaryAssociation(
    name="available51",
    ends={
        Property(name="diva_ContextExpression53", type=diva_MultiplicityConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_MultiplicityConstraint52", type=diva_ContextExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
property31: BinaryAssociation = BinaryAssociation(
    name="property31",
    ends={
        Property(name="diva_Property33", type=diva_Dimension, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_Dimension32", type=diva_Property, multiplicity=Multiplicity(0, 9999))
    }
)
constraints34: BinaryAssociation = BinaryAssociation(
    name="constraints34",
    ends={
        Property(name="diva_MultiplicityConstraint", type=diva_Dimension, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_Dimension35", type=diva_MultiplicityConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
term36: BinaryAssociation = BinaryAssociation(
    name="term36",
    ends={
        Property(name="diva_Term38", type=diva_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_Expression37", type=diva_Term, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
context39: BinaryAssociation = BinaryAssociation(
    name="context39",
    ends={
        Property(name="diva_ContextExpression40", type=diva_PriorityRule, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_PriorityRule", type=diva_ContextExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
priority41: BinaryAssociation = BinaryAssociation(
    name="priority41",
    ends={
        Property(name="diva_PropertyPriority", type=diva_PriorityRule, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_PriorityRule42", type=diva_PropertyPriority, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
literal43: BinaryAssociation = BinaryAssociation(
    name="literal43",
    ends={
        Property(name="diva_PropertyLiteral", type=diva_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_Property44", type=diva_PropertyLiteral, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variant67: BinaryAssociation = BinaryAssociation(
    name="variant67",
    ends={
        Property(name="diva_Variant69", type=diva_ConfigVariant, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_ConfigVariant68", type=diva_Variant, multiplicity=Multiplicity(1, 1))
    }
)
context70: BinaryAssociation = BinaryAssociation(
    name="context70",
    ends={
        Property(name="diva_Context72", type=diva_Scenario, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_Scenario71", type=diva_Context, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
score73: BinaryAssociation = BinaryAssociation(
    name="score73",
    ends={
        Property(name="diva_Score", type=diva_ScoredElement, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_ScoredElement", type=diva_Score, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
property74: BinaryAssociation = BinaryAssociation(
    name="property74",
    ends={
        Property(name="diva_Property76", type=diva_Score, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_Score75", type=diva_Property, multiplicity=Multiplicity(1, 1))
    }
)
annotation54: BinaryAssociation = BinaryAssociation(
    name="annotation54",
    ends={
        Property(name="diva_Annotation", type=diva_DiVAModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_DiVAModelElement", type=diva_Annotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
scenario55: BinaryAssociation = BinaryAssociation(
    name="scenario55",
    ends={
        Property(name="diva_Scenario", type=diva_SimulationModel, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_SimulationModel", type=diva_Scenario, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
model56: BinaryAssociation = BinaryAssociation(
    name="model56",
    ends={
        Property(name="VariabilityModel", type=diva_SimulationModel, multiplicity=Multiplicity(1, 1)),
        Property(name="simulation", type=diva_VariabilityModel, multiplicity=Multiplicity(1, 1))
    }
)
variable57: BinaryAssociation = BinaryAssociation(
    name="variable57",
    ends={
        Property(name="diva_VariableValue", type=diva_Context, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_Context", type=diva_VariableValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
configuration58: BinaryAssociation = BinaryAssociation(
    name="configuration58",
    ends={
        Property(name="diva_Configuration", type=diva_Context, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_Context59", type=diva_Configuration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
oracle60: BinaryAssociation = BinaryAssociation(
    name="oracle60",
    ends={
        Property(name="diva_VariantExpression62", type=diva_Context, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_Context61", type=diva_VariantExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
priority63: BinaryAssociation = BinaryAssociation(
    name="priority63",
    ends={
        Property(name="diva_Priority", type=diva_Context, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_Context64", type=diva_Priority, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variant65: BinaryAssociation = BinaryAssociation(
    name="variant65",
    ends={
        Property(name="diva_ConfigVariant", type=diva_Configuration, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_Configuration66", type=diva_ConfigVariant, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variable89: BinaryAssociation = BinaryAssociation(
    name="variable89",
    ends={
        Property(name="diva_ContextModel", type=diva_VariableValue, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="diva_VariableValue90", type=diva_ContextModel, multiplicity=Multiplicity(1, 1))
    }
)
model91: BinaryAssociation = BinaryAssociation(
    name="model91",
    ends={
        Property(name="diva_Model", type=diva_ModelContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_ModelContainer", type=diva_Model, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
property77: BinaryAssociation = BinaryAssociation(
    name="property77",
    ends={
        Property(name="diva_Property79", type=diva_Priority, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_Priority78", type=diva_Property, multiplicity=Multiplicity(1, 1))
    }
)
variable80: BinaryAssociation = BinaryAssociation(
    name="variable80",
    ends={
        Property(name="diva_Variable82", type=diva_VariableValue, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_VariableValue81", type=diva_Variable, multiplicity=Multiplicity(1, 1))
    }
)
literal83: BinaryAssociation = BinaryAssociation(
    name="literal83",
    ends={
        Property(name="diva_EnumLiteral84", type=diva_EnumVariableValue, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_EnumVariableValue", type=diva_EnumLiteral, multiplicity=Multiplicity(1, 1))
    }
)
configurations85: BinaryAssociation = BinaryAssociation(
    name="configurations85",
    ends={
        Property(name="diva_SuitableConfiguration", type=diva_ConfigurationModel, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_ConfigurationModel", type=diva_SuitableConfiguration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variant86: BinaryAssociation = BinaryAssociation(
    name="variant86",
    ends={
        Property(name="diva_ConfigVariant88", type=diva_SuitableConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_SuitableConfiguration87", type=diva_ConfigVariant, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_diva_BaseModel_Model = Generalization(general=Model, specific=diva_BaseModel)
gen_diva_AspectModel_Model = Generalization(general=Model, specific=diva_AspectModel)
gen_diva_EnumVariable_Variable = Generalization(general=Variable, specific=diva_EnumVariable)
gen_diva_BooleanVariable_Variable = Generalization(general=Variable, specific=diva_BooleanVariable)
gen_diva_Term_DiVAModelElement = Generalization(general=DiVAModelElement, specific=diva_Term)
gen_diva_AndTerm_NaryTerm = Generalization(general=NaryTerm, specific=diva_AndTerm)
gen_diva_OrTerm_NaryTerm = Generalization(general=NaryTerm, specific=diva_OrTerm)
gen_diva_NotTerm_Term = Generalization(general=Term, specific=diva_NotTerm)
gen_diva_VariabilityModel_ModelContainer = Generalization(general=ModelContainer, specific=diva_VariabilityModel)
gen_diva_Invariant_Constraint = Generalization(general=Constraint, specific=diva_Invariant)
gen_diva_Variable_NamedElement = Generalization(general=NamedElement, specific=diva_Variable)
gen_diva_Model_DiVAModelElement = Generalization(general=DiVAModelElement, specific=diva_Model)
gen_diva_Dimension_NamedElement = Generalization(general=NamedElement, specific=diva_Dimension)
gen_diva_NaryTerm_Term = Generalization(general=Term, specific=diva_NaryTerm)
gen_diva_VariantTerm_Term = Generalization(general=Term, specific=diva_VariantTerm)
gen_diva_VariableTerm_Term = Generalization(general=Term, specific=diva_VariableTerm)
gen_diva_EnumTerm_VariableTerm = Generalization(general=VariableTerm, specific=diva_EnumTerm)
gen_diva_BooleanTerm_VariableTerm = Generalization(general=VariableTerm, specific=diva_BooleanTerm)
gen_diva_Rule_NamedElement = Generalization(general=NamedElement, specific=diva_Rule)
gen_diva_EnumLiteral_NamedElement = Generalization(general=NamedElement, specific=diva_EnumLiteral)
gen_diva_NamedElement_DiVAModelElement = Generalization(general=DiVAModelElement, specific=diva_NamedElement)
gen_diva_Constraint_NamedElement = Generalization(general=NamedElement, specific=diva_Constraint)
gen_diva_Variant_NamedElement = Generalization(general=NamedElement, specific=diva_Variant)
gen_diva_Variant_ModelContainer = Generalization(general=ModelContainer, specific=diva_Variant)
gen_diva_PropertyLiteral_NamedElement = Generalization(general=NamedElement, specific=diva_PropertyLiteral)
gen_diva_PropertyValue_DiVAModelElement = Generalization(general=DiVAModelElement, specific=diva_PropertyValue)
gen_diva_PropertyPriority_DiVAModelElement = Generalization(general=DiVAModelElement, specific=diva_PropertyPriority)
gen_diva_MultiplicityConstraint_Constraint = Generalization(general=Constraint, specific=diva_MultiplicityConstraint)
gen_diva_Expression_DiVAModelElement = Generalization(general=DiVAModelElement, specific=diva_Expression)
gen_diva_ContextExpression_Expression = Generalization(general=Expression, specific=diva_ContextExpression)
gen_diva_VariantExpression_Expression = Generalization(general=Expression, specific=diva_VariantExpression)
gen_diva_PriorityRule_Rule = Generalization(general=Rule, specific=diva_PriorityRule)
gen_diva_Property_NamedElement = Generalization(general=NamedElement, specific=diva_Property)
gen_diva_ConfigVariant_ScoredElement = Generalization(general=ScoredElement, specific=diva_ConfigVariant)
gen_diva_Scenario_NamedElement = Generalization(general=NamedElement, specific=diva_Scenario)
gen_diva_ScoredElement_DiVAModelElement = Generalization(general=DiVAModelElement, specific=diva_ScoredElement)
gen_diva_Score_DiVAModelElement = Generalization(general=DiVAModelElement, specific=diva_Score)
gen_diva_SimulationModel_DiVAModelElement = Generalization(general=DiVAModelElement, specific=diva_SimulationModel)
gen_diva_Context_NamedElement = Generalization(general=NamedElement, specific=diva_Context)
gen_diva_Configuration_ScoredElement = Generalization(general=ScoredElement, specific=diva_Configuration)
gen_diva_Priority_DiVAModelElement = Generalization(general=DiVAModelElement, specific=diva_Priority)
gen_diva_VariableValue_DiVAModelElement = Generalization(general=DiVAModelElement, specific=diva_VariableValue)
gen_diva_BoolVariableValue_VariableValue = Generalization(general=VariableValue, specific=diva_BoolVariableValue)
gen_diva_EnumVariableValue_VariableValue = Generalization(general=VariableValue, specific=diva_EnumVariableValue)

# Domain Model
domain_model = DomainModel(
    name="diva",
    types={diva_BaseModel, Model, diva_AspectModel, diva_EnumVariable, Variable, diva_EnumLiteral, diva_BooleanVariable, diva_Term, diva_AndTerm, NaryTerm, diva_OrTerm, diva_NotTerm, Term, diva_VariabilityModel, ModelContainer, diva_Variable, diva_Property, diva_Dimension, diva_Rule, diva_Constraint, diva_SimulationModel, diva_Invariant, Constraint, diva_Expression, NamedElement, diva_Model, DiVAModelElement, diva_PropertyValue, diva_VariantExpression, diva_ContextExpression, diva_NaryTerm, diva_VariantTerm, diva_Variant, diva_VariableTerm, diva_EnumTerm, VariableTerm, diva_BooleanTerm, diva_NamedElement, diva_MultiplicityConstraint, Expression, diva_PriorityRule, Rule, diva_PropertyPriority, diva_PropertyLiteral, diva_ScoredElement, diva_Score, diva_Annotation, diva_DiVAModelElement, diva_Scenario, diva_Context, diva_VariableValue, diva_Configuration, diva_Priority, ScoredElement, diva_ConfigVariant, diva_ModelContainer, diva_BoolVariableValue, VariableValue, diva_EnumVariableValue, diva_ConfigurationModel, diva_SuitableConfiguration, diva_ContextModel, Verdict},
    associations={literal11, term12, context0, property1, dimension3, rule5, constraint7, simulation9, expression10, type20, propertyValue21, dependency23, available25, required27, variant30, term13, variant15, variable16, value18, property45, property48, available51, property31, constraints34, term36, context39, priority41, literal43, variant67, context70, score73, property74, annotation54, scenario55, model56, variable57, configuration58, oracle60, priority63, variant65, variable89, model91, property77, variable80, literal83, configurations85, variant86},
    generalizations={gen_diva_BaseModel_Model, gen_diva_AspectModel_Model, gen_diva_EnumVariable_Variable, gen_diva_BooleanVariable_Variable, gen_diva_Term_DiVAModelElement, gen_diva_AndTerm_NaryTerm, gen_diva_OrTerm_NaryTerm, gen_diva_NotTerm_Term, gen_diva_VariabilityModel_ModelContainer, gen_diva_Invariant_Constraint, gen_diva_Variable_NamedElement, gen_diva_Model_DiVAModelElement, gen_diva_Dimension_NamedElement, gen_diva_NaryTerm_Term, gen_diva_VariantTerm_Term, gen_diva_VariableTerm_Term, gen_diva_EnumTerm_VariableTerm, gen_diva_BooleanTerm_VariableTerm, gen_diva_Rule_NamedElement, gen_diva_EnumLiteral_NamedElement, gen_diva_NamedElement_DiVAModelElement, gen_diva_Constraint_NamedElement, gen_diva_Variant_NamedElement, gen_diva_Variant_ModelContainer, gen_diva_PropertyLiteral_NamedElement, gen_diva_PropertyValue_DiVAModelElement, gen_diva_PropertyPriority_DiVAModelElement, gen_diva_MultiplicityConstraint_Constraint, gen_diva_Expression_DiVAModelElement, gen_diva_ContextExpression_Expression, gen_diva_VariantExpression_Expression, gen_diva_PriorityRule_Rule, gen_diva_Property_NamedElement, gen_diva_ConfigVariant_ScoredElement, gen_diva_Scenario_NamedElement, gen_diva_ScoredElement_DiVAModelElement, gen_diva_Score_DiVAModelElement, gen_diva_SimulationModel_DiVAModelElement, gen_diva_Context_NamedElement, gen_diva_Configuration_ScoredElement, gen_diva_Priority_DiVAModelElement, gen_diva_VariableValue_DiVAModelElement, gen_diva_BoolVariableValue_VariableValue, gen_diva_EnumVariableValue_VariableValue},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)