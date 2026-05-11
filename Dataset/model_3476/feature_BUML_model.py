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
feature_Constraint = Class(name="feature_Constraint")
feature_Feature = Class(name="feature_Feature")
feature_FeatureModel = Class(name="feature_FeatureModel")
feature_FeatureTreeNode = Class(name="feature_FeatureTreeNode", is_abstract=True)
FeatureTreeNode = Class(name="FeatureTreeNode")
feature_Attribute = Class(name="feature_Attribute")
feature_Group = Class(name="feature_Group")
feature_Annotation = Class(name="feature_Annotation")

# feature_Constraint class attributes and methods
feature_Constraint_language: Property = Property(name="language", type=StringType)
feature_Constraint_expression: Property = Property(name="expression", type=StringType)
feature_Constraint.attributes={feature_Constraint_expression, feature_Constraint_language}

# feature_Feature class attributes and methods
feature_Feature_name: Property = Property(name="name", type=StringType)
feature_Feature_m_isMandatory: Method = Method(name="isMandatory", parameters={}, type=BooleanType)
feature_Feature.attributes={feature_Feature_name}
feature_Feature.methods={feature_Feature_m_isMandatory}

# feature_FeatureModel class attributes and methods
feature_FeatureModel_name: Property = Property(name="name", type=StringType)
feature_FeatureModel_m_getAllFeatures: Method = Method(name="getAllFeatures", parameters={}, type=StringType)
feature_FeatureModel_m_getMandatoryFeatures: Method = Method(name="getMandatoryFeatures", parameters={}, type=StringType)
feature_FeatureModel_m_getFeatureRecursive: Method = Method(name="getFeatureRecursive", parameters={Parameter(name='feature_base', type=StringType)}, type=StringType)
feature_FeatureModel.attributes={feature_FeatureModel_name}
feature_FeatureModel.methods={feature_FeatureModel_m_getFeatureRecursive, feature_FeatureModel_m_getMandatoryFeatures, feature_FeatureModel_m_getAllFeatures}

# feature_FeatureTreeNode class attributes and methods
feature_FeatureTreeNode_minCardinality: Property = Property(name="minCardinality", type=IntegerType)
feature_FeatureTreeNode_maxCardinality: Property = Property(name="maxCardinality", type=IntegerType)
feature_FeatureTreeNode.attributes={feature_FeatureTreeNode_minCardinality, feature_FeatureTreeNode_maxCardinality}

# FeatureTreeNode class attributes and methods

# feature_Attribute class attributes and methods
feature_Attribute_name: Property = Property(name="name", type=StringType)
feature_Attribute_type: Property = Property(name="type", type=StringType)
feature_Attribute_value: Property = Property(name="value", type=StringType)
feature_Attribute.attributes={feature_Attribute_type, feature_Attribute_name, feature_Attribute_value}

# feature_Group class attributes and methods

# feature_Annotation class attributes and methods

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
parent6: BinaryAssociation = BinaryAssociation(
    name="parent6",
    ends={
        Property(name="FeatureModel7", type=feature_FeatureModel, multiplicity=Multiplicity(1, 1)),
        Property(name="children", type=feature_FeatureModel, multiplicity=Multiplicity(0, 1))
    }
)
constraints17: BinaryAssociation = BinaryAssociation(
    name="constraints17",
    ends={
        Property(name="constrainedFeatures", type=feature_Constraint, multiplicity=Multiplicity(0, 9999)),
        Property(name="Constraint", type=feature_Feature, multiplicity=Multiplicity(1, 1))
    }
)
parentFeature18: BinaryAssociation = BinaryAssociation(
    name="parentFeature18",
    ends={
        Property(name="Feature", type=feature_Group, multiplicity=Multiplicity(1, 1)),
        Property(name="groups", type=feature_Feature, multiplicity=Multiplicity(1, 1))
    }
)
childFeatures19: BinaryAssociation = BinaryAssociation(
    name="childFeatures19",
    ends={
        Property(name="Feature20", type=feature_Group, multiplicity=Multiplicity(1, 1)),
        Property(name="parentGroup", type=feature_Feature, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
constrainedFeatures21: BinaryAssociation = BinaryAssociation(
    name="constrainedFeatures21",
    ends={
        Property(name="Feature22", type=feature_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="constraints", type=feature_Feature, multiplicity=Multiplicity(1, 9999))
    }
)
feature23: BinaryAssociation = BinaryAssociation(
    name="feature23",
    ends={
        Property(name="Feature24", type=feature_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="attributes", type=feature_Feature, multiplicity=Multiplicity(1, 1))
    }
)
feature25: BinaryAssociation = BinaryAssociation(
    name="feature25",
    ends={
        Property(name="Feature26", type=feature_Annotation, multiplicity=Multiplicity(1, 1)),
        Property(name="annotations", type=feature_Feature, multiplicity=Multiplicity(1, 1))
    }
)
constrainingFeatureModel9: BinaryAssociation = BinaryAssociation(
    name="constrainingFeatureModel9",
    ends={
        Property(name="feature_FeatureModel10", type=feature_FeatureModel, multiplicity=Multiplicity(1, 1)),
        Property(name="feature_FeatureModel8", type=feature_FeatureModel, multiplicity=Multiplicity(0, 1))
    }
)
attributes11: BinaryAssociation = BinaryAssociation(
    name="attributes11",
    ends={
        Property(name="Attribute", type=feature_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="feature", type=feature_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
groups12: BinaryAssociation = BinaryAssociation(
    name="groups12",
    ends={
        Property(name="Group", type=feature_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="parentFeature", type=feature_Group, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentGroup13: BinaryAssociation = BinaryAssociation(
    name="parentGroup13",
    ends={
        Property(name="Group14", type=feature_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="childFeatures", type=feature_Group, multiplicity=Multiplicity(0, 1))
    }
)
annotations15: BinaryAssociation = BinaryAssociation(
    name="annotations15",
    ends={
        Property(name="Annotation", type=feature_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="feature16", type=feature_Annotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_feature_Group_FeatureTreeNode = Generalization(general=FeatureTreeNode, specific=feature_Group)
gen_feature_Feature_FeatureTreeNode = Generalization(general=FeatureTreeNode, specific=feature_Feature)

# Domain Model
domain_model = DomainModel(
    name="feature",
    types={feature_Constraint, feature_Feature, feature_FeatureModel, feature_FeatureTreeNode, FeatureTreeNode, feature_Attribute, feature_Group, feature_Annotation},
    associations={constraints0, root1, children4, parent6, constraints17, parentFeature18, childFeatures19, constrainedFeatures21, feature23, feature25, constrainingFeatureModel9, attributes11, groups12, parentGroup13, annotations15},
    generalizations={gen_feature_Group_FeatureTreeNode, gen_feature_Feature_FeatureTreeNode},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)