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
			EnumerationLiteral(name="pass_"),
			EnumerationLiteral(name="fail")
    }
)

# Classes
diva_AspectModel = Class(name="diva_AspectModel")
diva_EnumVariable = Class(name="diva_EnumVariable")
Variable = Class(name="Variable")
diva_EnumLiteral = Class(name="diva_EnumLiteral")
diva_BooleanVariable = Class(name="diva_BooleanVariable")
diva_Term = Class(name="diva_Term", is_abstract=True)
diva_AndTerm = Class(name="diva_AndTerm")
NaryTerm = Class(name="NaryTerm")
diva_OrTerm = Class(name="diva_OrTerm")
diva_NotTerm = Class(name="diva_NotTerm")
diva_VariabilityModel = Class(name="diva_VariabilityModel")
DiVAModelElement = Class(name="DiVAModelElement")
diva_BaseModel = Class(name="diva_BaseModel")
diva_Variable = Class(name="diva_Variable", is_abstract=True)
diva_Property = Class(name="diva_Property")
diva_Dimension = Class(name="diva_Dimension")
diva_Rule = Class(name="diva_Rule", is_abstract=True)
diva_Constraint = Class(name="diva_Constraint", is_abstract=True)
diva_SimulationModel = Class(name="diva_SimulationModel")
diva_Invariant = Class(name="diva_Invariant")
Constraint = Class(name="Constraint")
diva_Expression = Class(name="diva_Expression")
NamedElement = Class(name="NamedElement")
diva_Model = Class(name="diva_Model", is_abstract=True)
Model = Class(name="Model")
diva_VariantTerm = Class(name="diva_VariantTerm")
diva_Variant = Class(name="diva_Variant")
diva_VariableTerm = Class(name="diva_VariableTerm", is_abstract=True)
Term = Class(name="Term")
diva_NaryTerm = Class(name="diva_NaryTerm", is_abstract=True)
diva_MultiplicityConstraint = Class(name="diva_MultiplicityConstraint")
Expression = Class(name="Expression")
diva_EnumTerm = Class(name="diva_EnumTerm")
VariableTerm = Class(name="VariableTerm")
diva_BooleanTerm = Class(name="diva_BooleanTerm")
diva_NamedElement = Class(name="diva_NamedElement", is_abstract=True)
diva_PropertyValue = Class(name="diva_PropertyValue")
diva_VariantExpression = Class(name="diva_VariantExpression")
diva_ContextExpression = Class(name="diva_ContextExpression")
diva_Context = Class(name="diva_Context")
diva_VariableValue = Class(name="diva_VariableValue", is_abstract=True)
diva_Configuration = Class(name="diva_Configuration")
diva_PriorityRule = Class(name="diva_PriorityRule")
Rule = Class(name="Rule")
diva_PropertyPriority = Class(name="diva_PropertyPriority")
diva_Annotation = Class(name="diva_Annotation")
diva_DiVAModelElement = Class(name="diva_DiVAModelElement", is_abstract=True)
diva_Scenario = Class(name="diva_Scenario")
diva_BoolVariableValue = Class(name="diva_BoolVariableValue")
VariableValue = Class(name="VariableValue")
diva_EnumVariableValue = Class(name="diva_EnumVariableValue")
diva_Priority = Class(name="diva_Priority")
ScoredElement = Class(name="ScoredElement")
diva_ConfigVariant = Class(name="diva_ConfigVariant")
diva_ScoredElement = Class(name="diva_ScoredElement", is_abstract=True)
diva_Score = Class(name="diva_Score")

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

# diva_VariabilityModel class attributes and methods

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

# diva_VariantTerm class attributes and methods

# diva_Variant class attributes and methods

# diva_VariableTerm class attributes and methods

# Term class attributes and methods

# diva_NaryTerm class attributes and methods

# diva_MultiplicityConstraint class attributes and methods
diva_MultiplicityConstraint_upper: Property = Property(name="upper", type=StringType)
diva_MultiplicityConstraint_lower: Property = Property(name="lower", type=StringType)
diva_MultiplicityConstraint.attributes={diva_MultiplicityConstraint_upper, diva_MultiplicityConstraint_lower}

# Expression class attributes and methods

# diva_EnumTerm class attributes and methods

# VariableTerm class attributes and methods

# diva_BooleanTerm class attributes and methods

# diva_NamedElement class attributes and methods
diva_NamedElement_name: Property = Property(name="name", type=StringType)
diva_NamedElement_id: Property = Property(name="id", type=StringType)
diva_NamedElement.attributes={diva_NamedElement_name, diva_NamedElement_id}

# diva_PropertyValue class attributes and methods
diva_PropertyValue_value: Property = Property(name="value", type=StringType)
diva_PropertyValue.attributes={diva_PropertyValue_value}

# diva_VariantExpression class attributes and methods

# diva_ContextExpression class attributes and methods

# diva_Context class attributes and methods
diva_Context_verdict: Property = Property(name="verdict", type=StringType)
diva_Context.attributes={diva_Context_verdict}

# diva_VariableValue class attributes and methods

# diva_Configuration class attributes and methods
diva_Configuration_verdict: Property = Property(name="verdict", type=StringType)
diva_Configuration.attributes={diva_Configuration_verdict}

# diva_PriorityRule class attributes and methods

# Rule class attributes and methods

# diva_PropertyPriority class attributes and methods
diva_PropertyPriority_priority: Property = Property(name="priority", type=StringType)
diva_PropertyPriority.attributes={diva_PropertyPriority_priority}

# diva_Annotation class attributes and methods
diva_Annotation_key: Property = Property(name="key", type=StringType)
diva_Annotation_value: Property = Property(name="value", type=StringType)
diva_Annotation.attributes={diva_Annotation_key, diva_Annotation_value}

# diva_DiVAModelElement class attributes and methods

# diva_Scenario class attributes and methods

# diva_BoolVariableValue class attributes and methods
diva_BoolVariableValue_bool: Property = Property(name="bool", type=BooleanType)
diva_BoolVariableValue.attributes={diva_BoolVariableValue_bool}

# VariableValue class attributes and methods

# diva_EnumVariableValue class attributes and methods

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

# Relationships
literal13: BinaryAssociation = BinaryAssociation(
    name="literal13",
    ends={
        Property(name="diva_EnumLiteral", type=diva_EnumVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_EnumVariable", type=diva_EnumLiteral, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
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
        Property(name="SimulationModel", type=diva_VariabilityModel, multiplicity=Multiplicity(1, 1)),
        Property(name="model", type=diva_SimulationModel, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression12: BinaryAssociation = BinaryAssociation(
    name="expression12",
    ends={
        Property(name="diva_Expression", type=diva_Invariant, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_Invariant", type=diva_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
term15: BinaryAssociation = BinaryAssociation(
    name="term15",
    ends={
        Property(name="diva_Term16", type=diva_NaryTerm, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_NaryTerm", type=diva_Term, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
variant17: BinaryAssociation = BinaryAssociation(
    name="variant17",
    ends={
        Property(name="diva_Variant", type=diva_VariantTerm, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_VariantTerm", type=diva_Variant, multiplicity=Multiplicity(1, 1))
    }
)
variable18: BinaryAssociation = BinaryAssociation(
    name="variable18",
    ends={
        Property(name="diva_Variable19", type=diva_VariableTerm, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_VariableTerm", type=diva_Variable, multiplicity=Multiplicity(1, 1))
    }
)
term14: BinaryAssociation = BinaryAssociation(
    name="term14",
    ends={
        Property(name="diva_Term", type=diva_NotTerm, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_NotTerm", type=diva_Term, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
property35: BinaryAssociation = BinaryAssociation(
    name="property35",
    ends={
        Property(name="diva_Property37", type=diva_Dimension, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_Dimension36", type=diva_Property, multiplicity=Multiplicity(0, 9999))
    }
)
constraints38: BinaryAssociation = BinaryAssociation(
    name="constraints38",
    ends={
        Property(name="diva_MultiplicityConstraint", type=diva_Dimension, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_Dimension39", type=diva_MultiplicityConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
term40: BinaryAssociation = BinaryAssociation(
    name="term40",
    ends={
        Property(name="diva_Term42", type=diva_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_Expression41", type=diva_Term, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value20: BinaryAssociation = BinaryAssociation(
    name="value20",
    ends={
        Property(name="diva_EnumLiteral21", type=diva_EnumTerm, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_EnumTerm", type=diva_EnumLiteral, multiplicity=Multiplicity(1, 1))
    }
)
model22: BinaryAssociation = BinaryAssociation(
    name="model22",
    ends={
        Property(name="diva_AspectModel", type=diva_Variant, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_Variant23", type=diva_AspectModel, multiplicity=Multiplicity(1, 1))
    }
)
type24: BinaryAssociation = BinaryAssociation(
    name="type24",
    ends={
        Property(name="Dimension", type=diva_Variant, multiplicity=Multiplicity(1, 1)),
        Property(name="variant", type=diva_Dimension, multiplicity=Multiplicity(1, 1))
    }
)
propertyValue25: BinaryAssociation = BinaryAssociation(
    name="propertyValue25",
    ends={
        Property(name="diva_PropertyValue", type=diva_Variant, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_Variant26", type=diva_PropertyValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dependency27: BinaryAssociation = BinaryAssociation(
    name="dependency27",
    ends={
        Property(name="diva_VariantExpression", type=diva_Variant, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_Variant28", type=diva_VariantExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
available29: BinaryAssociation = BinaryAssociation(
    name="available29",
    ends={
        Property(name="diva_ContextExpression", type=diva_Variant, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_Variant30", type=diva_ContextExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
required31: BinaryAssociation = BinaryAssociation(
    name="required31",
    ends={
        Property(name="diva_ContextExpression33", type=diva_Variant, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_Variant32", type=diva_ContextExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variant34: BinaryAssociation = BinaryAssociation(
    name="variant34",
    ends={
        Property(name="Variant", type=diva_Dimension, multiplicity=Multiplicity(1, 1)),
        Property(name="type", type=diva_Variant, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
scenario57: BinaryAssociation = BinaryAssociation(
    name="scenario57",
    ends={
        Property(name="diva_SimulationModel", type=diva_Scenario, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="diva_Scenario", type=diva_SimulationModel, multiplicity=Multiplicity(1, 1))
    }
)
model58: BinaryAssociation = BinaryAssociation(
    name="model58",
    ends={
        Property(name="VariabilityModel", type=diva_SimulationModel, multiplicity=Multiplicity(1, 1)),
        Property(name="simulation", type=diva_VariabilityModel, multiplicity=Multiplicity(1, 1))
    }
)
variable59: BinaryAssociation = BinaryAssociation(
    name="variable59",
    ends={
        Property(name="diva_VariableValue", type=diva_Context, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_Context", type=diva_VariableValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
configuration60: BinaryAssociation = BinaryAssociation(
    name="configuration60",
    ends={
        Property(name="diva_Configuration", type=diva_Context, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_Context61", type=diva_Configuration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
oracle62: BinaryAssociation = BinaryAssociation(
    name="oracle62",
    ends={
        Property(name="diva_VariantExpression64", type=diva_Context, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_Context63", type=diva_VariantExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
context43: BinaryAssociation = BinaryAssociation(
    name="context43",
    ends={
        Property(name="diva_ContextExpression44", type=diva_PriorityRule, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_PriorityRule", type=diva_ContextExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
priority45: BinaryAssociation = BinaryAssociation(
    name="priority45",
    ends={
        Property(name="diva_PropertyPriority", type=diva_PriorityRule, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_PriorityRule46", type=diva_PropertyPriority, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
property47: BinaryAssociation = BinaryAssociation(
    name="property47",
    ends={
        Property(name="diva_Property49", type=diva_PropertyValue, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_PropertyValue48", type=diva_Property, multiplicity=Multiplicity(1, 1))
    }
)
property50: BinaryAssociation = BinaryAssociation(
    name="property50",
    ends={
        Property(name="diva_Property52", type=diva_PropertyPriority, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_PropertyPriority51", type=diva_Property, multiplicity=Multiplicity(1, 1))
    }
)
available53: BinaryAssociation = BinaryAssociation(
    name="available53",
    ends={
        Property(name="diva_ContextExpression55", type=diva_MultiplicityConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_MultiplicityConstraint54", type=diva_ContextExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
annotation56: BinaryAssociation = BinaryAssociation(
    name="annotation56",
    ends={
        Property(name="diva_Annotation", type=diva_DiVAModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_DiVAModelElement", type=diva_Annotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variable82: BinaryAssociation = BinaryAssociation(
    name="variable82",
    ends={
        Property(name="diva_Variable84", type=diva_VariableValue, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_VariableValue83", type=diva_Variable, multiplicity=Multiplicity(1, 1))
    }
)
literal85: BinaryAssociation = BinaryAssociation(
    name="literal85",
    ends={
        Property(name="diva_EnumLiteral86", type=diva_EnumVariableValue, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_EnumVariableValue", type=diva_EnumLiteral, multiplicity=Multiplicity(1, 1))
    }
)
priority65: BinaryAssociation = BinaryAssociation(
    name="priority65",
    ends={
        Property(name="diva_Priority", type=diva_Context, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_Context66", type=diva_Priority, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variant67: BinaryAssociation = BinaryAssociation(
    name="variant67",
    ends={
        Property(name="diva_ConfigVariant", type=diva_Configuration, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_Configuration68", type=diva_ConfigVariant, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variant69: BinaryAssociation = BinaryAssociation(
    name="variant69",
    ends={
        Property(name="diva_Variant71", type=diva_ConfigVariant, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_ConfigVariant70", type=diva_Variant, multiplicity=Multiplicity(1, 1))
    }
)
context72: BinaryAssociation = BinaryAssociation(
    name="context72",
    ends={
        Property(name="diva_Context74", type=diva_Scenario, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_Scenario73", type=diva_Context, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
score75: BinaryAssociation = BinaryAssociation(
    name="score75",
    ends={
        Property(name="diva_Score", type=diva_ScoredElement, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_ScoredElement", type=diva_Score, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
property76: BinaryAssociation = BinaryAssociation(
    name="property76",
    ends={
        Property(name="diva_Property78", type=diva_Score, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_Score77", type=diva_Property, multiplicity=Multiplicity(1, 1))
    }
)
property79: BinaryAssociation = BinaryAssociation(
    name="property79",
    ends={
        Property(name="diva_Property81", type=diva_Priority, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_Priority80", type=diva_Property, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_diva_AspectModel_Model = Generalization(general=Model, specific=diva_AspectModel)
gen_diva_EnumVariable_Variable = Generalization(general=Variable, specific=diva_EnumVariable)
gen_diva_BooleanVariable_Variable = Generalization(general=Variable, specific=diva_BooleanVariable)
gen_diva_Term_DiVAModelElement = Generalization(general=DiVAModelElement, specific=diva_Term)
gen_diva_AndTerm_NaryTerm = Generalization(general=NaryTerm, specific=diva_AndTerm)
gen_diva_OrTerm_NaryTerm = Generalization(general=NaryTerm, specific=diva_OrTerm)
gen_diva_VariabilityModel_DiVAModelElement = Generalization(general=DiVAModelElement, specific=diva_VariabilityModel)
gen_diva_Invariant_Constraint = Generalization(general=Constraint, specific=diva_Invariant)
gen_diva_Variable_NamedElement = Generalization(general=NamedElement, specific=diva_Variable)
gen_diva_Model_DiVAModelElement = Generalization(general=DiVAModelElement, specific=diva_Model)
gen_diva_BaseModel_Model = Generalization(general=Model, specific=diva_BaseModel)
gen_diva_NaryTerm_Term = Generalization(general=Term, specific=diva_NaryTerm)
gen_diva_VariantTerm_Term = Generalization(general=Term, specific=diva_VariantTerm)
gen_diva_VariableTerm_Term = Generalization(general=Term, specific=diva_VariableTerm)
gen_diva_NotTerm_Term = Generalization(general=Term, specific=diva_NotTerm)
gen_diva_Expression_DiVAModelElement = Generalization(general=DiVAModelElement, specific=diva_Expression)
gen_diva_ContextExpression_Expression = Generalization(general=Expression, specific=diva_ContextExpression)
gen_diva_EnumTerm_VariableTerm = Generalization(general=VariableTerm, specific=diva_EnumTerm)
gen_diva_BooleanTerm_VariableTerm = Generalization(general=VariableTerm, specific=diva_BooleanTerm)
gen_diva_Rule_NamedElement = Generalization(general=NamedElement, specific=diva_Rule)
gen_diva_EnumLiteral_NamedElement = Generalization(general=NamedElement, specific=diva_EnumLiteral)
gen_diva_NamedElement_DiVAModelElement = Generalization(general=DiVAModelElement, specific=diva_NamedElement)
gen_diva_Constraint_NamedElement = Generalization(general=NamedElement, specific=diva_Constraint)
gen_diva_Variant_NamedElement = Generalization(general=NamedElement, specific=diva_Variant)
gen_diva_Dimension_NamedElement = Generalization(general=NamedElement, specific=diva_Dimension)
gen_diva_Context_NamedElement = Generalization(general=NamedElement, specific=diva_Context)
gen_diva_VariantExpression_Expression = Generalization(general=Expression, specific=diva_VariantExpression)
gen_diva_PriorityRule_Rule = Generalization(general=Rule, specific=diva_PriorityRule)
gen_diva_Property_NamedElement = Generalization(general=NamedElement, specific=diva_Property)
gen_diva_PropertyValue_DiVAModelElement = Generalization(general=DiVAModelElement, specific=diva_PropertyValue)
gen_diva_PropertyPriority_DiVAModelElement = Generalization(general=DiVAModelElement, specific=diva_PropertyPriority)
gen_diva_MultiplicityConstraint_Constraint = Generalization(general=Constraint, specific=diva_MultiplicityConstraint)
gen_diva_SimulationModel_DiVAModelElement = Generalization(general=DiVAModelElement, specific=diva_SimulationModel)
gen_diva_BoolVariableValue_VariableValue = Generalization(general=VariableValue, specific=diva_BoolVariableValue)
gen_diva_EnumVariableValue_VariableValue = Generalization(general=VariableValue, specific=diva_EnumVariableValue)
gen_diva_Configuration_ScoredElement = Generalization(general=ScoredElement, specific=diva_Configuration)
gen_diva_ConfigVariant_ScoredElement = Generalization(general=ScoredElement, specific=diva_ConfigVariant)
gen_diva_Scenario_NamedElement = Generalization(general=NamedElement, specific=diva_Scenario)
gen_diva_ScoredElement_DiVAModelElement = Generalization(general=DiVAModelElement, specific=diva_ScoredElement)
gen_diva_Score_DiVAModelElement = Generalization(general=DiVAModelElement, specific=diva_Score)
gen_diva_Priority_DiVAModelElement = Generalization(general=DiVAModelElement, specific=diva_Priority)
gen_diva_VariableValue_DiVAModelElement = Generalization(general=DiVAModelElement, specific=diva_VariableValue)

# Domain Model
domain_model = DomainModel(
    name="diva",
    types={diva_AspectModel, diva_EnumVariable, Variable, diva_EnumLiteral, diva_BooleanVariable, diva_Term, diva_AndTerm, NaryTerm, diva_OrTerm, diva_NotTerm, diva_VariabilityModel, DiVAModelElement, diva_BaseModel, diva_Variable, diva_Property, diva_Dimension, diva_Rule, diva_Constraint, diva_SimulationModel, diva_Invariant, Constraint, diva_Expression, NamedElement, diva_Model, Model, diva_VariantTerm, diva_Variant, diva_VariableTerm, Term, diva_NaryTerm, diva_MultiplicityConstraint, Expression, diva_EnumTerm, VariableTerm, diva_BooleanTerm, diva_NamedElement, diva_PropertyValue, diva_VariantExpression, diva_ContextExpression, diva_Context, diva_VariableValue, diva_Configuration, diva_PriorityRule, Rule, diva_PropertyPriority, diva_Annotation, diva_DiVAModelElement, diva_Scenario, diva_BoolVariableValue, VariableValue, diva_EnumVariableValue, diva_Priority, ScoredElement, diva_ConfigVariant, diva_ScoredElement, diva_Score, Verdict},
    associations={literal13, base0, context1, property3, dimension5, rule7, constraint9, simulation11, expression12, term15, variant17, variable18, term14, property35, constraints38, term40, value20, model22, type24, propertyValue25, dependency27, available29, required31, variant34, scenario57, model58, variable59, configuration60, oracle62, context43, priority45, property47, property50, available53, annotation56, variable82, literal85, priority65, variant67, variant69, context72, score75, property76, property79},
    generalizations={gen_diva_AspectModel_Model, gen_diva_EnumVariable_Variable, gen_diva_BooleanVariable_Variable, gen_diva_Term_DiVAModelElement, gen_diva_AndTerm_NaryTerm, gen_diva_OrTerm_NaryTerm, gen_diva_VariabilityModel_DiVAModelElement, gen_diva_Invariant_Constraint, gen_diva_Variable_NamedElement, gen_diva_Model_DiVAModelElement, gen_diva_BaseModel_Model, gen_diva_NaryTerm_Term, gen_diva_VariantTerm_Term, gen_diva_VariableTerm_Term, gen_diva_NotTerm_Term, gen_diva_Expression_DiVAModelElement, gen_diva_ContextExpression_Expression, gen_diva_EnumTerm_VariableTerm, gen_diva_BooleanTerm_VariableTerm, gen_diva_Rule_NamedElement, gen_diva_EnumLiteral_NamedElement, gen_diva_NamedElement_DiVAModelElement, gen_diva_Constraint_NamedElement, gen_diva_Variant_NamedElement, gen_diva_Dimension_NamedElement, gen_diva_Context_NamedElement, gen_diva_VariantExpression_Expression, gen_diva_PriorityRule_Rule, gen_diva_Property_NamedElement, gen_diva_PropertyValue_DiVAModelElement, gen_diva_PropertyPriority_DiVAModelElement, gen_diva_MultiplicityConstraint_Constraint, gen_diva_SimulationModel_DiVAModelElement, gen_diva_BoolVariableValue_VariableValue, gen_diva_EnumVariableValue_VariableValue, gen_diva_Configuration_ScoredElement, gen_diva_ConfigVariant_ScoredElement, gen_diva_Scenario_NamedElement, gen_diva_ScoredElement_DiVAModelElement, gen_diva_Score_DiVAModelElement, gen_diva_Priority_DiVAModelElement, gen_diva_VariableValue_DiVAModelElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)