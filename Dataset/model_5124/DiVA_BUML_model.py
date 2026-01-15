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
diva_Dimension = Class(name="diva::Dimension")
diva_VariabilityModel = Class(name="diva::VariabilityModel")
DiVAModelElement = Class(name="DiVAModelElement")
diva_BaseModel = Class(name="diva::BaseModel")
diva_Variable = Class(name="diva::Variable", is_abstract=True)
diva_Property = Class(name="diva::Property")
diva_BooleanTerm = Class(name="diva::BooleanTerm")
diva_Rule = Class(name="diva::Rule", is_abstract=True)
diva_Constraint = Class(name="diva::Constraint", is_abstract=True)
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
diva_BooleanVariable = Class(name="diva::BooleanVariable")
diva_Term = Class(name="diva::Term", is_abstract=True)
diva_AndTerm = Class(name="diva::AndTerm")
NaryTerm = Class(name="NaryTerm")
diva_OrTerm = Class(name="diva::OrTerm")
diva_NotTerm = Class(name="diva::NotTerm")
Term = Class(name="Term")
diva_NaryTerm = Class(name="diva::NaryTerm", is_abstract=True)
diva_VariantTerm = Class(name="diva::VariantTerm")
diva_Variant = Class(name="diva::Variant")
diva_VariableTerm = Class(name="diva::VariableTerm", is_abstract=True)
diva_EnumTerm = Class(name="diva::EnumTerm")
VariableTerm = Class(name="VariableTerm")
diva_NamedElement = Class(name="diva::NamedElement", is_abstract=True)
diva_PropertyValue = Class(name="diva::PropertyValue")
diva_VariantExpression = Class(name="diva::VariantExpression")
diva_ContextExpression = Class(name="diva::ContextExpression")
diva_MultiplicityConstraint = Class(name="diva::MultiplicityConstraint")
Expression = Class(name="Expression")
diva_PriorityRule = Class(name="diva::PriorityRule")
Rule = Class(name="Rule")
diva_PropertyPriority = Class(name="diva::PropertyPriority")
diva_Annotation = Class(name="diva::Annotation")
diva_DiVAModelElement = Class(name="diva::DiVAModelElement", is_abstract=True)

# diva_Dimension class attributes and methods
diva_Dimension_upper: Property = Property(name="upper", type=StringType)
diva_Dimension_lower: Property = Property(name="lower", type=StringType)
diva_Dimension.attributes={diva_Dimension_lower, diva_Dimension_upper}

# diva_VariabilityModel class attributes and methods

# DiVAModelElement class attributes and methods

# diva_BaseModel class attributes and methods
diva_BaseModel_m_weave: Method = Method(name="weave", parameters={})
diva_BaseModel.methods={diva_BaseModel_m_weave}

# diva_Variable class attributes and methods

# diva_Property class attributes and methods
diva_Property_direction: Property = Property(name="direction", type=StringType)
diva_Property.attributes={diva_Property_direction}

# diva_BooleanTerm class attributes and methods

# diva_Rule class attributes and methods

# diva_Constraint class attributes and methods

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

# diva_BooleanVariable class attributes and methods

# diva_Term class attributes and methods

# diva_AndTerm class attributes and methods

# NaryTerm class attributes and methods

# diva_OrTerm class attributes and methods

# diva_NotTerm class attributes and methods

# Term class attributes and methods

# diva_NaryTerm class attributes and methods

# diva_VariantTerm class attributes and methods

# diva_Variant class attributes and methods

# diva_VariableTerm class attributes and methods

# diva_EnumTerm class attributes and methods

# VariableTerm class attributes and methods

# diva_NamedElement class attributes and methods
diva_NamedElement_name: Property = Property(name="name", type=StringType)
diva_NamedElement_id: Property = Property(name="id", type=StringType)
diva_NamedElement.attributes={diva_NamedElement_name, diva_NamedElement_id}

# diva_PropertyValue class attributes and methods
diva_PropertyValue_value: Property = Property(name="value", type=StringType)
diva_PropertyValue.attributes={diva_PropertyValue_value}

# diva_VariantExpression class attributes and methods

# diva_ContextExpression class attributes and methods

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

# diva_Annotation class attributes and methods
diva_Annotation_key: Property = Property(name="key", type=StringType)
diva_Annotation_value: Property = Property(name="value", type=StringType)
diva_Annotation.attributes={diva_Annotation_key, diva_Annotation_value}

# diva_DiVAModelElement class attributes and methods

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
expression11: BinaryAssociation = BinaryAssociation(
    name="expression11",
    ends={
        Property(name="diva_Expression", type=diva_Invariant, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_Invariant", type=diva_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
literal12: BinaryAssociation = BinaryAssociation(
    name="literal12",
    ends={
        Property(name="diva_EnumLiteral", type=diva_EnumVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_EnumVariable", type=diva_EnumLiteral, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
term13: BinaryAssociation = BinaryAssociation(
    name="term13",
    ends={
        Property(name="diva_Term", type=diva_NotTerm, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_NotTerm", type=diva_Term, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
term14: BinaryAssociation = BinaryAssociation(
    name="term14",
    ends={
        Property(name="diva_Term15", type=diva_NaryTerm, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_NaryTerm", type=diva_Term, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
variant16: BinaryAssociation = BinaryAssociation(
    name="variant16",
    ends={
        Property(name="diva_Variant", type=diva_VariantTerm, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_VariantTerm", type=diva_Variant, multiplicity=Multiplicity(1, 1))
    }
)
variable17: BinaryAssociation = BinaryAssociation(
    name="variable17",
    ends={
        Property(name="diva_Variable18", type=diva_VariableTerm, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_VariableTerm", type=diva_Variable, multiplicity=Multiplicity(1, 1))
    }
)
value19: BinaryAssociation = BinaryAssociation(
    name="value19",
    ends={
        Property(name="diva_EnumLiteral20", type=diva_EnumTerm, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_EnumTerm", type=diva_EnumLiteral, multiplicity=Multiplicity(1, 1))
    }
)
model21: BinaryAssociation = BinaryAssociation(
    name="model21",
    ends={
        Property(name="diva_AspectModel", type=diva_Variant, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_Variant22", type=diva_AspectModel, multiplicity=Multiplicity(1, 1))
    }
)
type23: BinaryAssociation = BinaryAssociation(
    name="type23",
    ends={
        Property(name="24", type=diva_Variant, multiplicity=Multiplicity(1, 1)),
        Property(name="", type=diva_Dimension, multiplicity=Multiplicity(1, 1))
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
        Property(name="36", type=diva_Dimension, multiplicity=Multiplicity(1, 1)),
        Property(name="35", type=diva_Variant, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
property37: BinaryAssociation = BinaryAssociation(
    name="property37",
    ends={
        Property(name="diva_Property39", type=diva_Dimension, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_Dimension38", type=diva_Property, multiplicity=Multiplicity(0, 9999))
    }
)
constraints40: BinaryAssociation = BinaryAssociation(
    name="constraints40",
    ends={
        Property(name="diva_MultiplicityConstraint", type=diva_Dimension, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_Dimension41", type=diva_MultiplicityConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
term42: BinaryAssociation = BinaryAssociation(
    name="term42",
    ends={
        Property(name="diva_Term44", type=diva_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_Expression43", type=diva_Term, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
context45: BinaryAssociation = BinaryAssociation(
    name="context45",
    ends={
        Property(name="diva_ContextExpression46", type=diva_PriorityRule, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_PriorityRule", type=diva_ContextExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
priority47: BinaryAssociation = BinaryAssociation(
    name="priority47",
    ends={
        Property(name="diva_PropertyPriority", type=diva_PriorityRule, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_PriorityRule48", type=diva_PropertyPriority, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
property49: BinaryAssociation = BinaryAssociation(
    name="property49",
    ends={
        Property(name="diva_Property51", type=diva_PropertyValue, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_PropertyValue50", type=diva_Property, multiplicity=Multiplicity(1, 1))
    }
)
property52: BinaryAssociation = BinaryAssociation(
    name="property52",
    ends={
        Property(name="diva_Property54", type=diva_PropertyPriority, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_PropertyPriority53", type=diva_Property, multiplicity=Multiplicity(1, 1))
    }
)
available55: BinaryAssociation = BinaryAssociation(
    name="available55",
    ends={
        Property(name="diva_ContextExpression57", type=diva_MultiplicityConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_MultiplicityConstraint56", type=diva_ContextExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
annotation58: BinaryAssociation = BinaryAssociation(
    name="annotation58",
    ends={
        Property(name="diva_Annotation", type=diva_DiVAModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="diva_DiVAModelElement", type=diva_Annotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
gen_diva_BooleanVariable_Variable = Generalization(general=Variable, specific=diva_BooleanVariable)
gen_diva_Term_DiVAModelElement = Generalization(general=DiVAModelElement, specific=diva_Term)
gen_diva_AndTerm_NaryTerm = Generalization(general=NaryTerm, specific=diva_AndTerm)
gen_diva_OrTerm_NaryTerm = Generalization(general=NaryTerm, specific=diva_OrTerm)
gen_diva_NotTerm_Term = Generalization(general=Term, specific=diva_NotTerm)
gen_diva_NaryTerm_Term = Generalization(general=Term, specific=diva_NaryTerm)
gen_diva_VariantTerm_Term = Generalization(general=Term, specific=diva_VariantTerm)
gen_diva_VariableTerm_Term = Generalization(general=Term, specific=diva_VariableTerm)
gen_diva_EnumTerm_VariableTerm = Generalization(general=VariableTerm, specific=diva_EnumTerm)
gen_diva_Property_NamedElement = Generalization(general=NamedElement, specific=diva_Property)
gen_diva_BooleanTerm_VariableTerm = Generalization(general=VariableTerm, specific=diva_BooleanTerm)
gen_diva_Rule_NamedElement = Generalization(general=NamedElement, specific=diva_Rule)
gen_diva_EnumLiteral_NamedElement = Generalization(general=NamedElement, specific=diva_EnumLiteral)
gen_diva_NamedElement_DiVAModelElement = Generalization(general=DiVAModelElement, specific=diva_NamedElement)
gen_diva_Constraint_NamedElement = Generalization(general=NamedElement, specific=diva_Constraint)
gen_diva_Variant_NamedElement = Generalization(general=NamedElement, specific=diva_Variant)
gen_diva_Dimension_NamedElement = Generalization(general=NamedElement, specific=diva_Dimension)
gen_diva_Expression_DiVAModelElement = Generalization(general=DiVAModelElement, specific=diva_Expression)
gen_diva_ContextExpression_Expression = Generalization(general=Expression, specific=diva_ContextExpression)
gen_diva_VariantExpression_Expression = Generalization(general=Expression, specific=diva_VariantExpression)
gen_diva_PriorityRule_Rule = Generalization(general=Rule, specific=diva_PriorityRule)
gen_diva_PropertyValue_DiVAModelElement = Generalization(general=DiVAModelElement, specific=diva_PropertyValue)
gen_diva_PropertyPriority_DiVAModelElement = Generalization(general=DiVAModelElement, specific=diva_PropertyPriority)
gen_diva_MultiplicityConstraint_Constraint = Generalization(general=Constraint, specific=diva_MultiplicityConstraint)

# Domain Model
domain_model = DomainModel(
    name="diva",
    types={diva_Dimension, diva_VariabilityModel, DiVAModelElement, diva_BaseModel, diva_Variable, diva_Property, diva_BooleanTerm, diva_Rule, diva_Constraint, diva_Invariant, Constraint, diva_Expression, NamedElement, diva_Model, Model, diva_AspectModel, diva_EnumVariable, Variable, diva_EnumLiteral, diva_BooleanVariable, diva_Term, diva_AndTerm, NaryTerm, diva_OrTerm, diva_NotTerm, Term, diva_NaryTerm, diva_VariantTerm, diva_Variant, diva_VariableTerm, diva_EnumTerm, VariableTerm, diva_NamedElement, diva_PropertyValue, diva_VariantExpression, diva_ContextExpression, diva_MultiplicityConstraint, Expression, diva_PriorityRule, Rule, diva_PropertyPriority, diva_Annotation, diva_DiVAModelElement},
    associations={base0, context1, property3, dimension5, rule7, constraint9, expression11, literal12, term13, term14, variant16, variable17, value19, model21, type23, propertyValue25, dependency27, available29, required31, variant34, property37, constraints40, term42, context45, priority47, property49, property52, available55, annotation58},
    generalizations={gen_diva_VariabilityModel_DiVAModelElement, gen_diva_Invariant_Constraint, gen_diva_Variable_NamedElement, gen_diva_Model_DiVAModelElement, gen_diva_BaseModel_Model, gen_diva_AspectModel_Model, gen_diva_EnumVariable_Variable, gen_diva_BooleanVariable_Variable, gen_diva_Term_DiVAModelElement, gen_diva_AndTerm_NaryTerm, gen_diva_OrTerm_NaryTerm, gen_diva_NotTerm_Term, gen_diva_NaryTerm_Term, gen_diva_VariantTerm_Term, gen_diva_VariableTerm_Term, gen_diva_EnumTerm_VariableTerm, gen_diva_Property_NamedElement, gen_diva_BooleanTerm_VariableTerm, gen_diva_Rule_NamedElement, gen_diva_EnumLiteral_NamedElement, gen_diva_NamedElement_DiVAModelElement, gen_diva_Constraint_NamedElement, gen_diva_Variant_NamedElement, gen_diva_Dimension_NamedElement, gen_diva_Expression_DiVAModelElement, gen_diva_ContextExpression_Expression, gen_diva_VariantExpression_Expression, gen_diva_PriorityRule_Rule, gen_diva_PropertyValue_DiVAModelElement, gen_diva_PropertyPriority_DiVAModelElement, gen_diva_MultiplicityConstraint_Constraint},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)