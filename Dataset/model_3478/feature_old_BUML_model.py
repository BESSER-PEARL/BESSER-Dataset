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
AttributeComparisonOperator: Enumeration = Enumeration(
    name="AttributeComparisonOperator",
    literals={
            EnumerationLiteral(name="equal"),
			EnumerationLiteral(name="unequal"),
			EnumerationLiteral(name="greaterThan"),
			EnumerationLiteral(name="greaterThanOrEqual"),
			EnumerationLiteral(name="lessThan"),
			EnumerationLiteral(name="lessThanOrEqual")
    }
)

SelectedState: Enumeration = Enumeration(
    name="SelectedState",
    literals={
            EnumerationLiteral(name="selected"),
			EnumerationLiteral(name="deselected"),
			EnumerationLiteral(name="undetermined")
    }
)

# Classes
feature_FeatureModel = Class(name="feature::FeatureModel")
feature_Attribute = Class(name="feature::Attribute")
feature_Group = Class(name="feature::Group")
feature_Annotation = Class(name="feature::Annotation")
feature_Feature = Class(name="feature::Feature")
feature_Constraint = Class(name="feature::Constraint")
Identifiable = Class(name="Identifiable")
feature_Domain = Class(name="feature::Domain", is_abstract=True)
feature_EnumDomain = Class(name="feature::EnumDomain")
Domain = Class(name="Domain")
feature_ContinuousDomain = Class(name="feature::ContinuousDomain")
feature_Expression = Class(name="feature::Expression", is_abstract=True)
feature_BinaryExpression = Class(name="feature::BinaryExpression", is_abstract=True)
feature_AtomicExpression = Class(name="feature::AtomicExpression", is_abstract=True)
feature_FeatureReference = Class(name="feature::FeatureReference")
AtomicExpression = Class(name="AtomicExpression")
feature_NotExpression = Class(name="feature::NotExpression")
UnaryExpression = Class(name="UnaryExpression")
feature_AndExpression = Class(name="feature::AndExpression")
BinaryExpression = Class(name="BinaryExpression")
feature_Interval = Class(name="feature::Interval")
feature_UnaryExpression = Class(name="feature::UnaryExpression", is_abstract=True)
Expression = Class(name="Expression")
feature_AttributeOperand = Class(name="feature::AttributeOperand", is_abstract=True)
feature_ExcludesExpression = Class(name="feature::ExcludesExpression")
feature_AttributeReference = Class(name="feature::AttributeReference")
AttributeOperand = Class(name="AttributeOperand")
feature_OrExpression = Class(name="feature::OrExpression")
feature_ImpliesExpression = Class(name="feature::ImpliesExpression")
feature_NestedExpression = Class(name="feature::NestedExpression")
feature_Identifiable = Class(name="feature::Identifiable", is_abstract=True)
feature_AttributeComparisonExpression = Class(name="feature::AttributeComparisonExpression")
feature_AttributeValueLiteral = Class(name="feature::AttributeValueLiteral")

# feature_FeatureModel class attributes and methods
feature_FeatureModel_name: Property = Property(name="name", type=StringType)
feature_FeatureModel.attributes={feature_FeatureModel_name}

# feature_Attribute class attributes and methods
feature_Attribute_name: Property = Property(name="name", type=StringType)
feature_Attribute_value: Property = Property(name="value", type=StringType)
feature_Attribute.attributes={feature_Attribute_value, feature_Attribute_name}

# feature_Group class attributes and methods
feature_Group_minCardinality: Property = Property(name="minCardinality", type=IntegerType)
feature_Group_maxCardinality: Property = Property(name="maxCardinality", type=IntegerType)
feature_Group.attributes={feature_Group_maxCardinality, feature_Group_minCardinality}

# feature_Annotation class attributes and methods

# feature_Feature class attributes and methods
feature_Feature_name: Property = Property(name="name", type=StringType)
feature_Feature_selected: Property = Property(name="selected", type=StringType)
feature_Feature.attributes={feature_Feature_selected, feature_Feature_name}

# feature_Constraint class attributes and methods

# Identifiable class attributes and methods

# feature_Domain class attributes and methods

# feature_EnumDomain class attributes and methods
feature_EnumDomain_values: Property = Property(name="values", type=StringType)
feature_EnumDomain.attributes={feature_EnumDomain_values}

# Domain class attributes and methods

# feature_ContinuousDomain class attributes and methods

# feature_Expression class attributes and methods

# feature_BinaryExpression class attributes and methods

# feature_AtomicExpression class attributes and methods

# feature_FeatureReference class attributes and methods

# AtomicExpression class attributes and methods

# feature_NotExpression class attributes and methods

# UnaryExpression class attributes and methods

# feature_AndExpression class attributes and methods

# BinaryExpression class attributes and methods

# feature_Interval class attributes and methods
feature_Interval_lowerBound: Property = Property(name="lowerBound", type=IntegerType)
feature_Interval_upperBound: Property = Property(name="upperBound", type=IntegerType)
feature_Interval.attributes={feature_Interval_upperBound, feature_Interval_lowerBound}

# feature_UnaryExpression class attributes and methods

# Expression class attributes and methods

# feature_AttributeOperand class attributes and methods

# feature_ExcludesExpression class attributes and methods

# feature_AttributeReference class attributes and methods

# AttributeOperand class attributes and methods

# feature_OrExpression class attributes and methods

# feature_ImpliesExpression class attributes and methods

# feature_NestedExpression class attributes and methods

# feature_Identifiable class attributes and methods
feature_Identifiable_id: Property = Property(name="id", type=StringType)
feature_Identifiable.attributes={feature_Identifiable_id}

# feature_AttributeComparisonExpression class attributes and methods
feature_AttributeComparisonExpression_operator: Property = Property(name="operator", type=StringType)
feature_AttributeComparisonExpression.attributes={feature_AttributeComparisonExpression_operator}

# feature_AttributeValueLiteral class attributes and methods
feature_AttributeValueLiteral_value: Property = Property(name="value", type=StringType)
feature_AttributeValueLiteral.attributes={feature_AttributeValueLiteral_value}

# Relationships
attributes8: BinaryAssociation = BinaryAssociation(
    name="attributes8",
    ends={
        Property(name="Attribute", type=feature_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="feature", type=feature_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
groups9: BinaryAssociation = BinaryAssociation(
    name="groups9",
    ends={
        Property(name="Group", type=feature_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="parentFeature", type=feature_Group, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentGroup10: BinaryAssociation = BinaryAssociation(
    name="parentGroup10",
    ends={
        Property(name="Group11", type=feature_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="childFeatures", type=feature_Group, multiplicity=Multiplicity(0, 1))
    }
)
annotations12: BinaryAssociation = BinaryAssociation(
    name="annotations12",
    ends={
        Property(name="Annotation", type=feature_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="feature13", type=feature_Annotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent1: BinaryAssociation = BinaryAssociation(
    name="parent1",
    ends={
        Property(name="FeatureModel", type=feature_FeatureModel, multiplicity=Multiplicity(1, 1)),
        Property(name="children", type=feature_FeatureModel, multiplicity=Multiplicity(0, 1))
    }
)
children3: BinaryAssociation = BinaryAssociation(
    name="children3",
    ends={
        Property(name="FeatureModel4", type=feature_FeatureModel, multiplicity=Multiplicity(1, 1)),
        Property(name="parent", type=feature_FeatureModel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
root5: BinaryAssociation = BinaryAssociation(
    name="root5",
    ends={
        Property(name="feature_Feature", type=feature_FeatureModel, multiplicity=Multiplicity(1, 1)),
        Property(name="feature_FeatureModel", type=feature_Feature, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
constraints6: BinaryAssociation = BinaryAssociation(
    name="constraints6",
    ends={
        Property(name="feature_Constraint", type=feature_FeatureModel, multiplicity=Multiplicity(1, 1)),
        Property(name="feature_FeatureModel7", type=feature_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
feature19: BinaryAssociation = BinaryAssociation(
    name="feature19",
    ends={
        Property(name="Feature20", type=feature_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="attributes", type=feature_Feature, multiplicity=Multiplicity(1, 1))
    }
)
domain21: BinaryAssociation = BinaryAssociation(
    name="domain21",
    ends={
        Property(name="feature_Domain", type=feature_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="feature_Attribute", type=feature_Domain, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
feature22: BinaryAssociation = BinaryAssociation(
    name="feature22",
    ends={
        Property(name="Feature23", type=feature_Annotation, multiplicity=Multiplicity(1, 1)),
        Property(name="annotations", type=feature_Feature, multiplicity=Multiplicity(1, 1))
    }
)
parentFeature14: BinaryAssociation = BinaryAssociation(
    name="parentFeature14",
    ends={
        Property(name="Feature", type=feature_Group, multiplicity=Multiplicity(1, 1)),
        Property(name="groups", type=feature_Feature, multiplicity=Multiplicity(1, 1))
    }
)
childFeatures15: BinaryAssociation = BinaryAssociation(
    name="childFeatures15",
    ends={
        Property(name="Feature16", type=feature_Group, multiplicity=Multiplicity(1, 1)),
        Property(name="parentGroup", type=feature_Feature, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
expression17: BinaryAssociation = BinaryAssociation(
    name="expression17",
    ends={
        Property(name="feature_Expression", type=feature_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="feature_Constraint18", type=feature_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
operand127: BinaryAssociation = BinaryAssociation(
    name="operand127",
    ends={
        Property(name="feature_Expression28", type=feature_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="feature_BinaryExpression", type=feature_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
operand229: BinaryAssociation = BinaryAssociation(
    name="operand229",
    ends={
        Property(name="feature_Expression31", type=feature_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="feature_BinaryExpression30", type=feature_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
feature32: BinaryAssociation = BinaryAssociation(
    name="feature32",
    ends={
        Property(name="feature_Feature33", type=feature_FeatureReference, multiplicity=Multiplicity(1, 1)),
        Property(name="feature_FeatureReference", type=feature_Feature, multiplicity=Multiplicity(1, 1))
    }
)
intervals24: BinaryAssociation = BinaryAssociation(
    name="intervals24",
    ends={
        Property(name="feature_Interval", type=feature_ContinuousDomain, multiplicity=Multiplicity(1, 1)),
        Property(name="feature_ContinuousDomain", type=feature_Interval, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
operand25: BinaryAssociation = BinaryAssociation(
    name="operand25",
    ends={
        Property(name="feature_Expression26", type=feature_UnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="feature_UnaryExpression", type=feature_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
attribute134: BinaryAssociation = BinaryAssociation(
    name="attribute134",
    ends={
        Property(name="feature_AttributeOperand", type=feature_AttributeComparisonExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="feature_AttributeComparisonExpression", type=feature_AttributeOperand, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
attribute235: BinaryAssociation = BinaryAssociation(
    name="attribute235",
    ends={
        Property(name="feature_AttributeOperand37", type=feature_AttributeComparisonExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="feature_AttributeComparisonExpression36", type=feature_AttributeOperand, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
attribute38: BinaryAssociation = BinaryAssociation(
    name="attribute38",
    ends={
        Property(name="feature_Attribute39", type=feature_AttributeReference, multiplicity=Multiplicity(1, 1)),
        Property(name="feature_AttributeReference", type=feature_Attribute, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_feature_Group_Identifiable = Generalization(general=Identifiable, specific=feature_Group)
gen_feature_Feature_Identifiable = Generalization(general=Identifiable, specific=feature_Feature)
gen_feature_EnumDomain_Domain = Generalization(general=Domain, specific=feature_EnumDomain)
gen_feature_ContinuousDomain_Domain = Generalization(general=Domain, specific=feature_ContinuousDomain)
gen_feature_Constraint_Identifiable = Generalization(general=Identifiable, specific=feature_Constraint)
gen_feature_BinaryExpression_Expression = Generalization(general=Expression, specific=feature_BinaryExpression)
gen_feature_AtomicExpression_Expression = Generalization(general=Expression, specific=feature_AtomicExpression)
gen_feature_FeatureReference_AtomicExpression = Generalization(general=AtomicExpression, specific=feature_FeatureReference)
gen_feature_NotExpression_UnaryExpression = Generalization(general=UnaryExpression, specific=feature_NotExpression)
gen_feature_AndExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=feature_AndExpression)
gen_feature_UnaryExpression_Expression = Generalization(general=Expression, specific=feature_UnaryExpression)
gen_feature_ExcludesExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=feature_ExcludesExpression)
gen_feature_AttributeReference_AttributeOperand = Generalization(general=AttributeOperand, specific=feature_AttributeReference)
gen_feature_OrExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=feature_OrExpression)
gen_feature_ImpliesExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=feature_ImpliesExpression)
gen_feature_NestedExpression_UnaryExpression = Generalization(general=UnaryExpression, specific=feature_NestedExpression)
gen_feature_AttributeComparisonExpression_AtomicExpression = Generalization(general=AtomicExpression, specific=feature_AttributeComparisonExpression)
gen_feature_AttributeValueLiteral_AttributeOperand = Generalization(general=AttributeOperand, specific=feature_AttributeValueLiteral)

# Domain Model
domain_model = DomainModel(
    name="feature",
    types={feature_FeatureModel, feature_Attribute, feature_Group, feature_Annotation, feature_Feature, feature_Constraint, Identifiable, feature_Domain, feature_EnumDomain, Domain, feature_ContinuousDomain, feature_Expression, feature_BinaryExpression, feature_AtomicExpression, feature_FeatureReference, AtomicExpression, feature_NotExpression, UnaryExpression, feature_AndExpression, BinaryExpression, feature_Interval, feature_UnaryExpression, Expression, feature_AttributeOperand, feature_ExcludesExpression, feature_AttributeReference, AttributeOperand, feature_OrExpression, feature_ImpliesExpression, feature_NestedExpression, feature_Identifiable, feature_AttributeComparisonExpression, feature_AttributeValueLiteral, AttributeComparisonOperator, SelectedState},
    associations={attributes8, groups9, parentGroup10, annotations12, parent1, children3, root5, constraints6, feature19, domain21, feature22, parentFeature14, childFeatures15, expression17, operand127, operand229, feature32, intervals24, operand25, attribute134, attribute235, attribute38},
    generalizations={gen_feature_Group_Identifiable, gen_feature_Feature_Identifiable, gen_feature_EnumDomain_Domain, gen_feature_ContinuousDomain_Domain, gen_feature_Constraint_Identifiable, gen_feature_BinaryExpression_Expression, gen_feature_AtomicExpression_Expression, gen_feature_FeatureReference_AtomicExpression, gen_feature_NotExpression_UnaryExpression, gen_feature_AndExpression_BinaryExpression, gen_feature_UnaryExpression_Expression, gen_feature_ExcludesExpression_BinaryExpression, gen_feature_AttributeReference_AttributeOperand, gen_feature_OrExpression_BinaryExpression, gen_feature_ImpliesExpression_BinaryExpression, gen_feature_NestedExpression_UnaryExpression, gen_feature_AttributeComparisonExpression_AtomicExpression, gen_feature_AttributeValueLiteral_AttributeOperand},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)