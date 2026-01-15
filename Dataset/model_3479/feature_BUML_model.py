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
feature_FeatureModel = Class(name="feature::FeatureModel")
feature_Constraint = Class(name="feature::Constraint")
feature_Feature = Class(name="feature::Feature")
feature_Attribute = Class(name="feature::Attribute")
feature_Group = Class(name="feature::Group")

# feature_FeatureModel class attributes and methods
feature_FeatureModel_name: Property = Property(name="name", type=StringType)
feature_FeatureModel_m_getAllFeatures: Method = Method(name="getAllFeatures", parameters={}, type=StringType)
feature_FeatureModel_m_getMandatoryFeatures: Method = Method(name="getMandatoryFeatures", parameters={}, type=StringType)
feature_FeatureModel.attributes={feature_FeatureModel_name}
feature_FeatureModel.methods={feature_FeatureModel_m_getMandatoryFeatures, feature_FeatureModel_m_getAllFeatures}

# feature_Constraint class attributes and methods
feature_Constraint_language: Property = Property(name="language", type=StringType)
feature_Constraint_expression: Property = Property(name="expression", type=StringType)
feature_Constraint.attributes={feature_Constraint_language, feature_Constraint_expression}

# feature_Feature class attributes and methods
feature_Feature_name: Property = Property(name="name", type=StringType)
feature_Feature_minCardinality: Property = Property(name="minCardinality", type=IntegerType)
feature_Feature_maxCardinality: Property = Property(name="maxCardinality", type=IntegerType)
feature_Feature_m_isMandatory: Method = Method(name="isMandatory", parameters={}, type=BooleanType)
feature_Feature.attributes={feature_Feature_minCardinality, feature_Feature_name, feature_Feature_maxCardinality}
feature_Feature.methods={feature_Feature_m_isMandatory}

# feature_Attribute class attributes and methods
feature_Attribute_name: Property = Property(name="name", type=StringType)
feature_Attribute_type: Property = Property(name="type", type=StringType)
feature_Attribute_value: Property = Property(name="value", type=StringType)
feature_Attribute.attributes={feature_Attribute_type, feature_Attribute_value, feature_Attribute_name}

# feature_Group class attributes and methods
feature_Group_minCardinality: Property = Property(name="minCardinality", type=IntegerType)
feature_Group_maxCardinality: Property = Property(name="maxCardinality", type=IntegerType)
feature_Group.attributes={feature_Group_minCardinality, feature_Group_maxCardinality}

# Relationships
constraints0: BinaryAssociation = BinaryAssociation(
    name="constraints0",
    ends={
        Property(name="feature_Constraint", type=feature_FeatureModel, multiplicity=Multiplicity(1, 1)),
        Property(name="feature_FeatureModel", type=feature_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
root1: BinaryAssociation = BinaryAssociation(
    name="root1",
    ends={
        Property(name="feature_Feature", type=feature_FeatureModel, multiplicity=Multiplicity(1, 1)),
        Property(name="feature_FeatureModel2", type=feature_Feature, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
children4: BinaryAssociation = BinaryAssociation(
    name="children4",
    ends={
        Property(name="FeatureModel", type=feature_FeatureModel, multiplicity=Multiplicity(1, 1)),
        Property(name="parent", type=feature_FeatureModel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
childFeatures13: BinaryAssociation = BinaryAssociation(
    name="childFeatures13",
    ends={
        Property(name="Feature14", type=feature_Group, multiplicity=Multiplicity(1, 1)),
        Property(name="parentGroup", type=feature_Feature, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
parent6: BinaryAssociation = BinaryAssociation(
    name="parent6",
    ends={
        Property(name="FeatureModel7", type=feature_FeatureModel, multiplicity=Multiplicity(1, 1)),
        Property(name="children", type=feature_FeatureModel, multiplicity=Multiplicity(0, 1))
    }
)
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
parentFeature12: BinaryAssociation = BinaryAssociation(
    name="parentFeature12",
    ends={
        Property(name="Feature", type=feature_Group, multiplicity=Multiplicity(1, 1)),
        Property(name="groups", type=feature_Feature, multiplicity=Multiplicity(1, 1))
    }
)
feature15: BinaryAssociation = BinaryAssociation(
    name="feature15",
    ends={
        Property(name="Feature16", type=feature_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="attributes", type=feature_Feature, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="feature",
    types={feature_FeatureModel, feature_Constraint, feature_Feature, feature_Attribute, feature_Group},
    associations={constraints0, root1, children4, childFeatures13, parent6, attributes8, groups9, parentGroup10, parentFeature12, feature15},
    generalizations={},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)