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
FeatureState: Enumeration = Enumeration(
    name="FeatureState",
    literals={
            EnumerationLiteral(name="unbound"),
			EnumerationLiteral(name="selected"),
			EnumerationLiteral(name="deselected")
    }
)

Relop: Enumeration = Enumeration(
    name="Relop",
    literals={
            EnumerationLiteral(name="equal"),
			EnumerationLiteral(name="unequal"),
			EnumerationLiteral(name="greaterThan"),
			EnumerationLiteral(name="greaterThanOrEqual"),
			EnumerationLiteral(name="lessThan"),
			EnumerationLiteral(name="lessThanOrEqual")
    }
)

# Classes
feature_FeatureModel = Class(name="feature::FeatureModel")
feature_Feature = Class(name="feature::Feature")
feature_Domain = Class(name="feature::Domain", is_abstract=True)
feature_Constraint = Class(name="feature::Constraint", is_abstract=True)
feature_Group = Class(name="feature::Group")
Identifiable = Class(name="Identifiable")
feature_Attribute = Class(name="feature::Attribute")
feature_NumericalDomain = Class(name="feature::NumericalDomain")
feature_Interval = Class(name="feature::Interval")
feature_Identifiable = Class(name="feature::Identifiable", is_abstract=True)
feature_DiscreteDomain = Class(name="feature::DiscreteDomain")
Domain = Class(name="Domain")
feature_DomainValue = Class(name="feature::DomainValue")
feature_AttributeReference = Class(name="feature::AttributeReference")
AttributeOperand = Class(name="AttributeOperand")
feature_AttributeValue = Class(name="feature::AttributeValue")
feature_AttributeConstraint = Class(name="feature::AttributeConstraint")
Constraint = Class(name="Constraint")
feature_AttributeOperand = Class(name="feature::AttributeOperand", is_abstract=True)
feature_Imply = Class(name="feature::Imply")
FeatureConstraint = Class(name="FeatureConstraint")
feature_Exclude = Class(name="feature::Exclude")
feature_FeatureConstraint = Class(name="feature::FeatureConstraint", is_abstract=True)

# feature_FeatureModel class attributes and methods
feature_FeatureModel_name: Property = Property(name="name", type=StringType)
feature_FeatureModel.attributes={feature_FeatureModel_name}

# feature_Feature class attributes and methods
feature_Feature_name: Property = Property(name="name", type=StringType)
feature_Feature_configurationState: Property = Property(name="configurationState", type=StringType)
feature_Feature.attributes={feature_Feature_name, feature_Feature_configurationState}

# feature_Domain class attributes and methods

# feature_Constraint class attributes and methods

# feature_Group class attributes and methods
feature_Group_minCardinality: Property = Property(name="minCardinality", type=IntegerType)
feature_Group_maxCardinality: Property = Property(name="maxCardinality", type=IntegerType)
feature_Group.attributes={feature_Group_minCardinality, feature_Group_maxCardinality}

# Identifiable class attributes and methods

# feature_Attribute class attributes and methods
feature_Attribute_name: Property = Property(name="name", type=StringType)
feature_Attribute_value: Property = Property(name="value", type=StringType)
feature_Attribute_deselectedDomainValues: Property = Property(name="deselectedDomainValues", type=StringType)
feature_Attribute.attributes={feature_Attribute_name, feature_Attribute_value, feature_Attribute_deselectedDomainValues}

# feature_NumericalDomain class attributes and methods

# feature_Interval class attributes and methods
feature_Interval_lowerBound: Property = Property(name="lowerBound", type=IntegerType)
feature_Interval_upperBound: Property = Property(name="upperBound", type=IntegerType)
feature_Interval.attributes={feature_Interval_lowerBound, feature_Interval_upperBound}

# feature_Identifiable class attributes and methods
feature_Identifiable_id: Property = Property(name="id", type=StringType)
feature_Identifiable.attributes={feature_Identifiable_id}

# feature_DiscreteDomain class attributes and methods

# Domain class attributes and methods

# feature_DomainValue class attributes and methods
feature_DomainValue_int: Property = Property(name="int", type=IntegerType)
feature_DomainValue_name: Property = Property(name="name", type=StringType)
feature_DomainValue.attributes={feature_DomainValue_int, feature_DomainValue_name}

# feature_AttributeReference class attributes and methods

# AttributeOperand class attributes and methods

# feature_AttributeValue class attributes and methods
feature_AttributeValue_name: Property = Property(name="name", type=StringType)
feature_AttributeValue_int: Property = Property(name="int", type=IntegerType)
feature_AttributeValue.attributes={feature_AttributeValue_int, feature_AttributeValue_name}

# feature_AttributeConstraint class attributes and methods
feature_AttributeConstraint_operator: Property = Property(name="operator", type=StringType)
feature_AttributeConstraint.attributes={feature_AttributeConstraint_operator}

# Constraint class attributes and methods

# feature_AttributeOperand class attributes and methods

# feature_Imply class attributes and methods

# FeatureConstraint class attributes and methods

# feature_Exclude class attributes and methods

# feature_FeatureConstraint class attributes and methods

# Relationships
root0: BinaryAssociation = BinaryAssociation(
    name="root0",
    ends={
        Property(name="feature_Feature", type=feature_FeatureModel, multiplicity=Multiplicity(1, 1)),
        Property(name="feature_FeatureModel", type=feature_Feature, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
domains1: BinaryAssociation = BinaryAssociation(
    name="domains1",
    ends={
        Property(name="feature_Domain", type=feature_FeatureModel, multiplicity=Multiplicity(1, 1)),
        Property(name="feature_FeatureModel2", type=feature_Domain, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
constraints3: BinaryAssociation = BinaryAssociation(
    name="constraints3",
    ends={
        Property(name="feature_Constraint", type=feature_FeatureModel, multiplicity=Multiplicity(1, 1)),
        Property(name="feature_FeatureModel4", type=feature_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
groups6: BinaryAssociation = BinaryAssociation(
    name="groups6",
    ends={
        Property(name="feature_Group", type=feature_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="feature_Feature7", type=feature_Group, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
childFeatures8: BinaryAssociation = BinaryAssociation(
    name="childFeatures8",
    ends={
        Property(name="feature_Feature10", type=feature_Group, multiplicity=Multiplicity(1, 1)),
        Property(name="feature_Group9", type=feature_Feature, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
feature11: BinaryAssociation = BinaryAssociation(
    name="feature11",
    ends={
        Property(name="Feature", type=feature_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="attributes", type=feature_Feature, multiplicity=Multiplicity(1, 1))
    }
)
domain12: BinaryAssociation = BinaryAssociation(
    name="domain12",
    ends={
        Property(name="feature_Domain13", type=feature_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="feature_Attribute", type=feature_Domain, multiplicity=Multiplicity(1, 1))
    }
)
attributes5: BinaryAssociation = BinaryAssociation(
    name="attributes5",
    ends={
        Property(name="Attribute", type=feature_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="feature", type=feature_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
intervals15: BinaryAssociation = BinaryAssociation(
    name="intervals15",
    ends={
        Property(name="feature_Interval", type=feature_NumericalDomain, multiplicity=Multiplicity(1, 1)),
        Property(name="feature_NumericalDomain", type=feature_Interval, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
values14: BinaryAssociation = BinaryAssociation(
    name="values14",
    ends={
        Property(name="feature_DomainValue", type=feature_DiscreteDomain, multiplicity=Multiplicity(1, 1)),
        Property(name="feature_DiscreteDomain", type=feature_DomainValue, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
attribute20: BinaryAssociation = BinaryAssociation(
    name="attribute20",
    ends={
        Property(name="feature_Attribute21", type=feature_AttributeReference, multiplicity=Multiplicity(1, 1)),
        Property(name="feature_AttributeReference", type=feature_Attribute, multiplicity=Multiplicity(1, 1))
    }
)
feature22: BinaryAssociation = BinaryAssociation(
    name="feature22",
    ends={
        Property(name="feature_Feature24", type=feature_AttributeReference, multiplicity=Multiplicity(1, 1)),
        Property(name="feature_AttributeReference23", type=feature_Feature, multiplicity=Multiplicity(1, 1))
    }
)
leftOperand16: BinaryAssociation = BinaryAssociation(
    name="leftOperand16",
    ends={
        Property(name="feature_AttributeOperand", type=feature_AttributeConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="feature_AttributeConstraint", type=feature_AttributeOperand, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rightOperand17: BinaryAssociation = BinaryAssociation(
    name="rightOperand17",
    ends={
        Property(name="feature_AttributeOperand19", type=feature_AttributeConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="feature_AttributeConstraint18", type=feature_AttributeOperand, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
leftOperand25: BinaryAssociation = BinaryAssociation(
    name="leftOperand25",
    ends={
        Property(name="feature_Feature26", type=feature_FeatureConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="feature_FeatureConstraint", type=feature_Feature, multiplicity=Multiplicity(1, 1))
    }
)
rightOperand27: BinaryAssociation = BinaryAssociation(
    name="rightOperand27",
    ends={
        Property(name="feature_Feature29", type=feature_FeatureConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="feature_FeatureConstraint28", type=feature_Feature, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_feature_Group_Identifiable = Generalization(general=Identifiable, specific=feature_Group)
gen_feature_Feature_Identifiable = Generalization(general=Identifiable, specific=feature_Feature)
gen_feature_NumericalDomain_Domain = Generalization(general=Domain, specific=feature_NumericalDomain)
gen_feature_Domain_Identifiable = Generalization(general=Identifiable, specific=feature_Domain)
gen_feature_Constraint_Identifiable = Generalization(general=Identifiable, specific=feature_Constraint)
gen_feature_DiscreteDomain_Domain = Generalization(general=Domain, specific=feature_DiscreteDomain)
gen_feature_AttributeReference_AttributeOperand = Generalization(general=AttributeOperand, specific=feature_AttributeReference)
gen_feature_AttributeValue_AttributeOperand = Generalization(general=AttributeOperand, specific=feature_AttributeValue)
gen_feature_AttributeConstraint_Constraint = Generalization(general=Constraint, specific=feature_AttributeConstraint)
gen_feature_Imply_FeatureConstraint = Generalization(general=FeatureConstraint, specific=feature_Imply)
gen_feature_Exclude_FeatureConstraint = Generalization(general=FeatureConstraint, specific=feature_Exclude)
gen_feature_FeatureConstraint_Constraint = Generalization(general=Constraint, specific=feature_FeatureConstraint)

# Domain Model
domain_model = DomainModel(
    name="feature",
    types={feature_FeatureModel, feature_Feature, feature_Domain, feature_Constraint, feature_Group, Identifiable, feature_Attribute, feature_NumericalDomain, feature_Interval, feature_Identifiable, feature_DiscreteDomain, Domain, feature_DomainValue, feature_AttributeReference, AttributeOperand, feature_AttributeValue, feature_AttributeConstraint, Constraint, feature_AttributeOperand, feature_Imply, FeatureConstraint, feature_Exclude, feature_FeatureConstraint, FeatureState, Relop},
    associations={root0, domains1, constraints3, groups6, childFeatures8, feature11, domain12, attributes5, intervals15, values14, attribute20, feature22, leftOperand16, rightOperand17, leftOperand25, rightOperand27},
    generalizations={gen_feature_Group_Identifiable, gen_feature_Feature_Identifiable, gen_feature_NumericalDomain_Domain, gen_feature_Domain_Identifiable, gen_feature_Constraint_Identifiable, gen_feature_DiscreteDomain_Domain, gen_feature_AttributeReference_AttributeOperand, gen_feature_AttributeValue_AttributeOperand, gen_feature_AttributeConstraint_Constraint, gen_feature_Imply_FeatureConstraint, gen_feature_Exclude_FeatureConstraint, gen_feature_FeatureConstraint_Constraint},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)