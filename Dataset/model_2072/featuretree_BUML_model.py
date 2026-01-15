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
featuretree_FeatureTree = Class(name="featuretree::FeatureTree")
core_AbstractModelElement = Class(name="core::AbstractModelElement")
features_IFeatureDomain = Class(name="features::IFeatureDomain")
core_ITopLevelElement = Class(name="core::ITopLevelElement")
featuretree_TreeFeature = Class(name="featuretree::TreeFeature")
Feature = Class(name="Feature")

# featuretree_FeatureTree class attributes and methods

# core_AbstractModelElement class attributes and methods

# features_IFeatureDomain class attributes and methods

# core_ITopLevelElement class attributes and methods

# featuretree_TreeFeature class attributes and methods
featuretree_TreeFeature_mandatory: Property = Property(name="mandatory", type=BooleanType)
featuretree_TreeFeature.attributes={featuretree_TreeFeature_mandatory}

# Feature class attributes and methods

# Relationships
root0: BinaryAssociation = BinaryAssociation(
    name="root0",
    ends={
        Property(name="featuretree_TreeFeature", type=featuretree_FeatureTree, multiplicity=Multiplicity(1, 1)),
        Property(name="featuretree_FeatureTree", type=featuretree_TreeFeature, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
children2: BinaryAssociation = BinaryAssociation(
    name="children2",
    ends={
        Property(name="featuretree_TreeFeature3", type=featuretree_TreeFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="featuretree_TreeFeature1", type=featuretree_TreeFeature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_featuretree_FeatureTree_core_AbstractModelElement = Generalization(general=core_AbstractModelElement, specific=featuretree_FeatureTree)
gen_featuretree_FeatureTree_features_IFeatureDomain = Generalization(general=features_IFeatureDomain, specific=featuretree_FeatureTree)
gen_featuretree_FeatureTree_core_ITopLevelElement = Generalization(general=core_ITopLevelElement, specific=featuretree_FeatureTree)
gen_featuretree_TreeFeature_Feature = Generalization(general=Feature, specific=featuretree_TreeFeature)

# Domain Model
domain_model = DomainModel(
    name="featuretree",
    types={featuretree_FeatureTree, core_AbstractModelElement, features_IFeatureDomain, core_ITopLevelElement, featuretree_TreeFeature, Feature},
    associations={root0, children2},
    generalizations={gen_featuretree_FeatureTree_core_AbstractModelElement, gen_featuretree_FeatureTree_features_IFeatureDomain, gen_featuretree_FeatureTree_core_ITopLevelElement, gen_featuretree_TreeFeature_Feature},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)