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
DiVAModelElement = Class(name="DiVAModelElement")
diva_BaseModel = Class(name="diva::BaseModel")
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
Model = Class(name="Model")
diva_AspectModel = Class(name="diva::AspectModel")
diva_EnumVariable = Class(name="diva::EnumVariable")
Variable = Class(name="Variable")
diva_EnumLiteral = Class(name="diva::EnumLiteral")
diva_VariabilityModel = Class(name="diva::VariabilityModel")
diva_VariantTerm = Class(name="diva::VariantTerm")
diva_Variant = Class(name="diva::Variant")
diva_VariableTerm = Class(name="diva::VariableTerm", is_abstract=True)
diva_EnumTerm = Class(name="diva::EnumTerm")
VariableTerm = Class(name="VariableTerm")
diva_BooleanTerm = Class(name="diva::BooleanTerm")
diva_NamedElement = Class(name="diva::NamedElement", is_abstract=True)
diva_PropertyValue = Class(name="diva::PropertyValue")
diva_VariantExpression = Class(name="diva::VariantExpression")
diva_ContextExpression = Class(name="diva::ContextExpression")
diva_BooleanVariable = Class(name="diva::BooleanVariable")
diva_Term = Class(name="diva::Term", is_abstract=True)
diva_AndTerm = Class(name="diva::AndTerm")
NaryTerm = Class(name="NaryTerm")
diva_OrTerm = Class(name="diva::OrTerm")
diva_NotTerm = Class(name="diva::NotTerm")
Term = Class(name="Term")
diva_NaryTerm = Class(name="diva::NaryTerm", is_abstract=True)
Expression = Class(name="Expression")
diva_PriorityRule = Class(name="diva::PriorityRule")
Rule = Class(name="Rule")
diva_PropertyPriority = Class(name="diva::PropertyPriority")
diva_Annotation = Class(name="diva::Annotation")
diva_MultiplicityConstraint = Class(name="diva::MultiplicityConstraint")
diva_VariableValue = Class(name="diva::VariableValue", is_abstract=True)
diva_Configuration = Class(name="diva::Configuration")
diva_Priority = Class(name="diva::Priority")
ScoredElement = Class(name="ScoredElement")
diva_ConfigVariant = Class(name="diva::ConfigVariant")
diva_ScoredElement = Class(name="diva::ScoredElement", is_abstract=True)
diva_Score = Class(name="diva::Score")
diva_DiVAModelElement = Class(name="diva::DiVAModelElement", is_abstract=True)
diva_Scenario = Class(name="diva::Scenario")
diva_Context = Class(name="diva::Context")
diva_BoolVariableValue = Class(name="diva::BoolVariableValue")
VariableValue = Class(name="VariableValue")
diva_EnumVariableValue = Class(name="diva::EnumVariableValue")

# DiVAModelElement class attributes and methods

# diva_BaseModel class attributes and methods
diva_BaseModel_m_weave: Method = Method(name="weave", parameters={})
diva_BaseModel.methods={diva_BaseModel_m_weave}

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

# Model class attributes and methods

# diva_AspectModel class attributes and methods

# diva_EnumVariable class attributes and methods

# Variable class attributes and methods

# diva_EnumLiteral class attributes and methods

# diva_VariabilityModel class attributes and methods

# diva_VariantTerm class attributes and methods

# diva_Variant class attributes and methods

# diva_VariableTerm class attributes and methods

# diva_EnumTerm class attributes and methods

# VariableTerm class attributes and methods

# diva_BooleanTerm class attributes and methods

# diva_NamedElement class attributes and methods
diva_NamedElement_name: Property = Property(name="name", type=StringType)
diva_NamedElement_id: Property = Property(name="id", type=StringType)
diva_NamedElement.attributes={diva_NamedElement_id, diva_NamedElement_name}

# diva_PropertyValue class attributes and methods
diva_PropertyValue_value: Property = Property(name="value", type=StringType)
diva_PropertyValue.attributes={diva_PropertyValue_value}

# diva_VariantExpression class attributes and methods

# diva_ContextExpression class attributes and methods

# diva_BooleanVariable class attributes and methods

# diva_Term class attributes and methods

# diva_AndTerm class attributes and methods

# NaryTerm class attributes and methods

# diva_OrTerm class attributes and methods

# diva_NotTerm class attributes and methods

# Term class attributes and methods

# diva_NaryTerm class attributes and methods

# Expression class attributes and methods

# diva_PriorityRule class attributes and methods

# Rule class attributes and methods

# diva_PropertyPriority class attributes and methods
diva_PropertyPriority_priority: Property = Property(name="priority", type=StringType)
diva_PropertyPriority.attributes={diva_PropertyPriority_priority}

# diva_Annotation class attributes and methods
diva_Annotation_key: Property = Property(name="key", type=StringType)
diva_Annotation_value: Property = Property(name="value", type=StringType)
diva_Annotation.attributes={diva_Annotation_value, diva_Annotation_key}

# diva_MultiplicityConstraint class attributes and methods
diva_MultiplicityConstraint_upper: Property = Property(name="upper", type=StringType)
diva_MultiplicityConstraint_lower: Property = Property(name="lower", type=StringType)
diva_MultiplicityConstraint.attributes={diva_MultiplicityConstraint_upper, diva_MultiplicityConstraint_lower}

# diva_VariableValue class attributes and methods

# diva_Configuration class attributes and methods
diva_Configuration_verdict: Property = Property(name="verdict", type=StringType)
diva_Configuration.attributes={diva_Configuration_verdict}

# diva_Priority class attributes and methods
diva_Priority_priority: Property = Property(name="priority", type=IntegerType)
diva_Priority.attributes={diva_Priority_priority}

# ScoredElement class attributes and methods

# diva_ConfigVariant class attributes and methods

# diva_ScoredElement class attributes and methods
diva_ScoredElement_totalScore: Property = Property(name="totalScore", type=IntegerType)
diva_ScoredElement.attributes={diva_ScoredElement_totalScore}

# diva_Score class attributes and methods
diva_Score_score: Property = Property(name="score", type=IntegerType)
diva_Score.attributes={diva_Score_score}

# diva_DiVAModelElement class attributes and methods

# diva_Scenario class attributes and methods

# diva_Context class attributes and methods
diva_Context_verdict: Property = Property(name="verdict", type=StringType)
diva_Context.attributes={diva_Context_verdict}

# diva_BoolVariableValue class attributes and methods
diva_BoolVariableValue_bool: Property = Property(name="bool", type=BooleanType)
diva_BoolVariableValue.attributes={diva_BoolVariableValue_bool}

# VariableValue class attributes and methods

# diva_EnumVariableValue class attributes and methods

# Relationships
base0: BinaryAssociation = BinaryAssociation(
    name="base0",
    ends={
        Property(name="diva_BaseModel", type=diva_VariabilityModel, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_VariabilityModel", type=diva_BaseModel, multiplicity=Multiplicity(1, 1))
    }
)
context1: BinaryAssociation = BinaryAssociation(
    name="context1",
    ends={
        Property(name="diva_Variable", type=diva_VariabilityModel, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_VariabilityModel2", type=diva_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
property3: BinaryAssociation = BinaryAssociation(
    name="property3",
    ends={
        Property(name="diva_Property", type=diva_VariabilityModel, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_VariabilityModel4", type=diva_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dimension5: BinaryAssociation = BinaryAssociation(
    name="dimension5",
    ends={
        Property(name="diva_Dimension", type=diva_VariabilityModel, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_VariabilityModel6", type=diva_Dimension, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rule7: BinaryAssociation = BinaryAssociation(
    name="rule7",
    ends={
        Property(name="diva_Rule", type=diva_VariabilityModel, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_VariabilityModel8", type=diva_Rule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
constraint9: BinaryAssociation = BinaryAssociation(
    name="constraint9",
    ends={
        Property(name="diva_Constraint", type=diva_VariabilityModel, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_VariabilityModel10", type=diva_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
simulation11: BinaryAssociation = BinaryAssociation(
    name="simulation11",
    ends={
        Property(name="12", type=diva_VariabilityModel, multiplicity=Multiplicity(1, 1)),
        Property(name="", type=diva_SimulationModel, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression13: BinaryAssociation = BinaryAssociation(
    name="expression13",
    ends={
        Property(name="diva_Expression", type=diva_Invariant, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_Invariant", type=diva_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
term16: BinaryAssociation = BinaryAssociation(
    name="term16",
    ends={
        Property(name="diva_Term17", type=diva_NaryTerm, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_NaryTerm", type=diva_Term, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
variant18: BinaryAssociation = BinaryAssociation(
    name="variant18",
    ends={
        Property(name="diva_Variant", type=diva_VariantTerm, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_VariantTerm", type=diva_Variant, multiplicity=Multiplicity(1, 1))
    }
)
variable19: BinaryAssociation = BinaryAssociation(
    name="variable19",
    ends={
        Property(name="diva_Variable20", type=diva_VariableTerm, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_VariableTerm", type=diva_Variable, multiplicity=Multiplicity(1, 1))
    }
)
value21: BinaryAssociation = BinaryAssociation(
    name="value21",
    ends={
        Property(name="diva_EnumLiteral22", type=diva_EnumTerm, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_EnumTerm", type=diva_EnumLiteral, multiplicity=Multiplicity(1, 1))
    }
)
model23: BinaryAssociation = BinaryAssociation(
    name="model23",
    ends={
        Property(name="diva_AspectModel", type=diva_Variant, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_Variant24", type=diva_AspectModel, multiplicity=Multiplicity(1, 1))
    }
)
type25: BinaryAssociation = BinaryAssociation(
    name="type25",
    ends={
        Property(name="27", type=diva_Variant, multiplicity=Multiplicity(1, 1)),
        Property(name="26", type=diva_Dimension, multiplicity=Multiplicity(1, 1))
    }
)
propertyValue28: BinaryAssociation = BinaryAssociation(
    name="propertyValue28",
    ends={
        Property(name="diva_PropertyValue", type=diva_Variant, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_Variant29", type=diva_PropertyValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dependency30: BinaryAssociation = BinaryAssociation(
    name="dependency30",
    ends={
        Property(name="diva_VariantExpression", type=diva_Variant, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_Variant31", type=diva_VariantExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
available32: BinaryAssociation = BinaryAssociation(
    name="available32",
    ends={
        Property(name="diva_ContextExpression", type=diva_Variant, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_Variant33", type=diva_ContextExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
required34: BinaryAssociation = BinaryAssociation(
    name="required34",
    ends={
        Property(name="diva_ContextExpression36", type=diva_Variant, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_Variant35", type=diva_ContextExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
literal14: BinaryAssociation = BinaryAssociation(
    name="literal14",
    ends={
        Property(name="diva_EnumLiteral", type=diva_EnumVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_EnumVariable", type=diva_EnumLiteral, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
term15: BinaryAssociation = BinaryAssociation(
    name="term15",
    ends={
        Property(name="diva_Term", type=diva_NotTerm, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_NotTerm", type=diva_Term, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
constraints43: BinaryAssociation = BinaryAssociation(
    name="constraints43",
    ends={
        Property(name="diva_MultiplicityConstraint", type=diva_Dimension, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_Dimension44", type=diva_MultiplicityConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
term45: BinaryAssociation = BinaryAssociation(
    name="term45",
    ends={
        Property(name="diva_Term47", type=diva_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_Expression46", type=diva_Term, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
context48: BinaryAssociation = BinaryAssociation(
    name="context48",
    ends={
        Property(name="diva_ContextExpression49", type=diva_PriorityRule, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_PriorityRule", type=diva_ContextExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
priority50: BinaryAssociation = BinaryAssociation(
    name="priority50",
    ends={
        Property(name="diva_PropertyPriority", type=diva_PriorityRule, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_PriorityRule51", type=diva_PropertyPriority, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
property52: BinaryAssociation = BinaryAssociation(
    name="property52",
    ends={
        Property(name="diva_Property54", type=diva_PropertyValue, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_PropertyValue53", type=diva_Property, multiplicity=Multiplicity(1, 1))
    }
)
property55: BinaryAssociation = BinaryAssociation(
    name="property55",
    ends={
        Property(name="diva_Property57", type=diva_PropertyPriority, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_PropertyPriority56", type=diva_Property, multiplicity=Multiplicity(1, 1))
    }
)
available58: BinaryAssociation = BinaryAssociation(
    name="available58",
    ends={
        Property(name="diva_ContextExpression60", type=diva_MultiplicityConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_MultiplicityConstraint59", type=diva_ContextExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variant37: BinaryAssociation = BinaryAssociation(
    name="variant37",
    ends={
        Property(name="39", type=diva_Dimension, multiplicity=Multiplicity(1, 1)),
        Property(name="38", type=diva_Variant, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
property40: BinaryAssociation = BinaryAssociation(
    name="property40",
    ends={
        Property(name="diva_Property42", type=diva_Dimension, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_Dimension41", type=diva_Property, multiplicity=Multiplicity(0, 9999))
    }
)
variable66: BinaryAssociation = BinaryAssociation(
    name="variable66",
    ends={
        Property(name="diva_VariableValue", type=diva_Context, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_Context", type=diva_VariableValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
configuration67: BinaryAssociation = BinaryAssociation(
    name="configuration67",
    ends={
        Property(name="diva_Configuration", type=diva_Context, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_Context68", type=diva_Configuration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
oracle69: BinaryAssociation = BinaryAssociation(
    name="oracle69",
    ends={
        Property(name="diva_VariantExpression71", type=diva_Context, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_Context70", type=diva_VariantExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
priority72: BinaryAssociation = BinaryAssociation(
    name="priority72",
    ends={
        Property(name="diva_Priority", type=diva_Context, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_Context73", type=diva_Priority, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variant74: BinaryAssociation = BinaryAssociation(
    name="variant74",
    ends={
        Property(name="diva_ConfigVariant", type=diva_Configuration, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_Configuration75", type=diva_ConfigVariant, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variant76: BinaryAssociation = BinaryAssociation(
    name="variant76",
    ends={
        Property(name="diva_Variant78", type=diva_ConfigVariant, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_ConfigVariant77", type=diva_Variant, multiplicity=Multiplicity(1, 1))
    }
)
context79: BinaryAssociation = BinaryAssociation(
    name="context79",
    ends={
        Property(name="diva_Context81", type=diva_Scenario, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_Scenario80", type=diva_Context, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
score82: BinaryAssociation = BinaryAssociation(
    name="score82",
    ends={
        Property(name="diva_Score", type=diva_ScoredElement, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_ScoredElement", type=diva_Score, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
property83: BinaryAssociation = BinaryAssociation(
    name="property83",
    ends={
        Property(name="diva_Property85", type=diva_Score, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_Score84", type=diva_Property, multiplicity=Multiplicity(1, 1))
    }
)
property86: BinaryAssociation = BinaryAssociation(
    name="property86",
    ends={
        Property(name="diva_Property88", type=diva_Priority, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_Priority87", type=diva_Property, multiplicity=Multiplicity(1, 1))
    }
)
annotation61: BinaryAssociation = BinaryAssociation(
    name="annotation61",
    ends={
        Property(name="diva_Annotation", type=diva_DiVAModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_DiVAModelElement", type=diva_Annotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
scenario62: BinaryAssociation = BinaryAssociation(
    name="scenario62",
    ends={
        Property(name="diva_Scenario", type=diva_SimulationModel, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_SimulationModel", type=diva_Scenario, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
model63: BinaryAssociation = BinaryAssociation(
    name="model63",
    ends={
        Property(name="65", type=diva_SimulationModel, multiplicity=Multiplicity(1, 1)),
        Property(name="64", type=diva_VariabilityModel, multiplicity=Multiplicity(1, 1))
    }
)
variable89: BinaryAssociation = BinaryAssociation(
    name="variable89",
    ends={
        Property(name="diva_Variable91", type=diva_VariableValue, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_VariableValue90", type=diva_Variable, multiplicity=Multiplicity(1, 1))
    }
)
literal92: BinaryAssociation = BinaryAssociation(
    name="literal92",
    ends={
        Property(name="diva_EnumLiteral93", type=diva_EnumVariableValue, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_EnumVariableValue", type=diva_EnumLiteral, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_diva_VariabilityModel_DiVAModelElement = Generalization(general=DiVAModelElement, specific=diva_VariabilityModel)
gen_diva_Invariant_Constraint = Generalization(general=Constraint, specific=diva_Invariant)
gen_diva_Variable_NamedElement = Generalization(general=NamedElement, specific=diva_Variable)
gen_diva_Model_DiVAModelElement = Generalization(general=DiVAModelElement, specific=diva_Model)
gen_diva_BaseModel_Model = Generalization(general=Model, specific=diva_BaseModel)
gen_diva_AspectModel_Model = Generalization(general=Model, specific=diva_AspectModel)
gen_diva_EnumVariable_Variable = Generalization(general=Variable, specific=diva_EnumVariable)
gen_diva_VariantTerm_Term = Generalization(general=Term, specific=diva_VariantTerm)
gen_diva_VariableTerm_Term = Generalization(general=Term, specific=diva_VariableTerm)
gen_diva_EnumTerm_VariableTerm = Generalization(general=VariableTerm, specific=diva_EnumTerm)
gen_diva_BooleanTerm_VariableTerm = Generalization(general=VariableTerm, specific=diva_BooleanTerm)
gen_diva_Rule_NamedElement = Generalization(general=NamedElement, specific=diva_Rule)
gen_diva_EnumLiteral_NamedElement = Generalization(general=NamedElement, specific=diva_EnumLiteral)
gen_diva_NamedElement_DiVAModelElement = Generalization(general=DiVAModelElement, specific=diva_NamedElement)
gen_diva_Constraint_NamedElement = Generalization(general=NamedElement, specific=diva_Constraint)
gen_diva_Variant_NamedElement = Generalization(general=NamedElement, specific=diva_Variant)
gen_diva_BooleanVariable_Variable = Generalization(general=Variable, specific=diva_BooleanVariable)
gen_diva_Term_DiVAModelElement = Generalization(general=DiVAModelElement, specific=diva_Term)
gen_diva_AndTerm_NaryTerm = Generalization(general=NaryTerm, specific=diva_AndTerm)
gen_diva_OrTerm_NaryTerm = Generalization(general=NaryTerm, specific=diva_OrTerm)
gen_diva_NotTerm_Term = Generalization(general=Term, specific=diva_NotTerm)
gen_diva_NaryTerm_Term = Generalization(general=Term, specific=diva_NaryTerm)
gen_diva_Expression_DiVAModelElement = Generalization(general=DiVAModelElement, specific=diva_Expression)
gen_diva_ContextExpression_Expression = Generalization(general=Expression, specific=diva_ContextExpression)
gen_diva_VariantExpression_Expression = Generalization(general=Expression, specific=diva_VariantExpression)
gen_diva_PriorityRule_Rule = Generalization(general=Rule, specific=diva_PriorityRule)
gen_diva_Property_NamedElement = Generalization(general=NamedElement, specific=diva_Property)
gen_diva_PropertyValue_DiVAModelElement = Generalization(general=DiVAModelElement, specific=diva_PropertyValue)
gen_diva_PropertyPriority_DiVAModelElement = Generalization(general=DiVAModelElement, specific=diva_PropertyPriority)
gen_diva_MultiplicityConstraint_Constraint = Generalization(general=Constraint, specific=diva_MultiplicityConstraint)
gen_diva_Dimension_NamedElement = Generalization(general=NamedElement, specific=diva_Dimension)
gen_diva_Configuration_ScoredElement = Generalization(general=ScoredElement, specific=diva_Configuration)
gen_diva_ConfigVariant_ScoredElement = Generalization(general=ScoredElement, specific=diva_ConfigVariant)
gen_diva_Scenario_NamedElement = Generalization(general=NamedElement, specific=diva_Scenario)
gen_diva_ScoredElement_DiVAModelElement = Generalization(general=DiVAModelElement, specific=diva_ScoredElement)
gen_diva_Score_DiVAModelElement = Generalization(general=DiVAModelElement, specific=diva_Score)
gen_diva_Priority_DiVAModelElement = Generalization(general=DiVAModelElement, specific=diva_Priority)
gen_diva_SimulationModel_DiVAModelElement = Generalization(general=DiVAModelElement, specific=diva_SimulationModel)
gen_diva_Context_NamedElement = Generalization(general=NamedElement, specific=diva_Context)
gen_diva_VariableValue_DiVAModelElement = Generalization(general=DiVAModelElement, specific=diva_VariableValue)
gen_diva_BoolVariableValue_VariableValue = Generalization(general=VariableValue, specific=diva_BoolVariableValue)
gen_diva_EnumVariableValue_VariableValue = Generalization(general=VariableValue, specific=diva_EnumVariableValue)

# Domain Model
domain_model = DomainModel(
    name="diva",
    types={DiVAModelElement, diva_BaseModel, diva_Variable, diva_Property, diva_Dimension, diva_Rule, diva_Constraint, diva_SimulationModel, diva_Invariant, Constraint, diva_Expression, NamedElement, diva_Model, Model, diva_AspectModel, diva_EnumVariable, Variable, diva_EnumLiteral, diva_VariabilityModel, diva_VariantTerm, diva_Variant, diva_VariableTerm, diva_EnumTerm, VariableTerm, diva_BooleanTerm, diva_NamedElement, diva_PropertyValue, diva_VariantExpression, diva_ContextExpression, diva_BooleanVariable, diva_Term, diva_AndTerm, NaryTerm, diva_OrTerm, diva_NotTerm, Term, diva_NaryTerm, Expression, diva_PriorityRule, Rule, diva_PropertyPriority, diva_Annotation, diva_MultiplicityConstraint, diva_VariableValue, diva_Configuration, diva_Priority, ScoredElement, diva_ConfigVariant, diva_ScoredElement, diva_Score, diva_DiVAModelElement, diva_Scenario, diva_Context, diva_BoolVariableValue, VariableValue, diva_EnumVariableValue, Verdict},
    associations={base0, context1, property3, dimension5, rule7, constraint9, simulation11, expression13, term16, variant18, variable19, value21, model23, type25, propertyValue28, dependency30, available32, required34, literal14, term15, constraints43, term45, context48, priority50, property52, property55, available58, variant37, property40, variable66, configuration67, oracle69, priority72, variant74, variant76, context79, score82, property83, property86, annotation61, scenario62, model63, variable89, literal92},
    generalizations={gen_diva_VariabilityModel_DiVAModelElement, gen_diva_Invariant_Constraint, gen_diva_Variable_NamedElement, gen_diva_Model_DiVAModelElement, gen_diva_BaseModel_Model, gen_diva_AspectModel_Model, gen_diva_EnumVariable_Variable, gen_diva_VariantTerm_Term, gen_diva_VariableTerm_Term, gen_diva_EnumTerm_VariableTerm, gen_diva_BooleanTerm_VariableTerm, gen_diva_Rule_NamedElement, gen_diva_EnumLiteral_NamedElement, gen_diva_NamedElement_DiVAModelElement, gen_diva_Constraint_NamedElement, gen_diva_Variant_NamedElement, gen_diva_BooleanVariable_Variable, gen_diva_Term_DiVAModelElement, gen_diva_AndTerm_NaryTerm, gen_diva_OrTerm_NaryTerm, gen_diva_NotTerm_Term, gen_diva_NaryTerm_Term, gen_diva_Expression_DiVAModelElement, gen_diva_ContextExpression_Expression, gen_diva_VariantExpression_Expression, gen_diva_PriorityRule_Rule, gen_diva_Property_NamedElement, gen_diva_PropertyValue_DiVAModelElement, gen_diva_PropertyPriority_DiVAModelElement, gen_diva_MultiplicityConstraint_Constraint, gen_diva_Dimension_NamedElement, gen_diva_Configuration_ScoredElement, gen_diva_ConfigVariant_ScoredElement, gen_diva_Scenario_NamedElement, gen_diva_ScoredElement_DiVAModelElement, gen_diva_Score_DiVAModelElement, gen_diva_Priority_DiVAModelElement, gen_diva_SimulationModel_DiVAModelElement, gen_diva_Context_NamedElement, gen_diva_VariableValue_DiVAModelElement, gen_diva_BoolVariableValue_VariableValue, gen_diva_EnumVariableValue_VariableValue},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)