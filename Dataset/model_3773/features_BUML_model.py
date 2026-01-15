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
features_FeatureSet = Class(name="features::FeatureSet")
FeatureSetDescriptor = Class(name="FeatureSetDescriptor")
features_FeatureSetDescriptor = Class(name="features::FeatureSetDescriptor", is_abstract=True)
features_FeatureDescriptor = Class(name="features::FeatureDescriptor", is_abstract=True)
features_FeatureVersionDescriptor = Class(name="features::FeatureVersionDescriptor", is_abstract=True)
features_Feature = Class(name="features::Feature")
FeatureDescriptor = Class(name="FeatureDescriptor")
features_FeatureVersion = Class(name="features::FeatureVersion")
FeatureVersionDescriptor = Class(name="FeatureVersionDescriptor")

# features_FeatureSet class attributes and methods
features_FeatureSet_identifier: Property = Property(name="identifier", type=StringType)
features_FeatureSet_name: Property = Property(name="name", type=StringType)
features_FeatureSet_description: Property = Property(name="description", type=StringType)
features_FeatureSet.attributes={features_FeatureSet_description, features_FeatureSet_identifier, features_FeatureSet_name}

# FeatureSetDescriptor class attributes and methods

# features_FeatureSetDescriptor class attributes and methods

# features_FeatureDescriptor class attributes and methods

# features_FeatureVersionDescriptor class attributes and methods

# features_Feature class attributes and methods
features_Feature_identifier: Property = Property(name="identifier", type=StringType)
features_Feature_provider: Property = Property(name="provider", type=StringType)
features_Feature_name: Property = Property(name="name", type=StringType)
features_Feature_description: Property = Property(name="description", type=StringType)
features_Feature.attributes={features_Feature_identifier, features_Feature_provider, features_Feature_name, features_Feature_description}

# FeatureDescriptor class attributes and methods

# features_FeatureVersion class attributes and methods
features_FeatureVersion_version: Property = Property(name="version", type=StringType)
features_FeatureVersion_news: Property = Property(name="news", type=StringType)
features_FeatureVersion.attributes={features_FeatureVersion_news, features_FeatureVersion_version}

# FeatureVersionDescriptor class attributes and methods

# Relationships
feature3: BinaryAssociation = BinaryAssociation(
    name="feature3",
    ends={
        Property(name="Feature4", type=features_FeatureVersion, multiplicity=Multiplicity(1, 1)),
        Property(name="featureVersions", type=features_Feature, multiplicity=Multiplicity(1, 1))
    }
)
features0: BinaryAssociation = BinaryAssociation(
    name="features0",
    ends={
        Property(name="Feature", type=features_FeatureSet, multiplicity=Multiplicity(1, 1)),
        Property(name="featureSet", type=features_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
featureSet1: BinaryAssociation = BinaryAssociation(
    name="featureSet1",
    ends={
        Property(name="FeatureSet", type=features_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="features", type=features_FeatureSet, multiplicity=Multiplicity(1, 1))
    }
)
featureVersions2: BinaryAssociation = BinaryAssociation(
    name="featureVersions2",
    ends={
        Property(name="FeatureVersion", type=features_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="feature", type=features_FeatureVersion, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_features_FeatureSet_FeatureSetDescriptor = Generalization(general=FeatureSetDescriptor, specific=features_FeatureSet)
gen_features_Feature_FeatureDescriptor = Generalization(general=FeatureDescriptor, specific=features_Feature)
gen_features_FeatureVersion_FeatureVersionDescriptor = Generalization(general=FeatureVersionDescriptor, specific=features_FeatureVersion)

# Domain Model
domain_model = DomainModel(
    name="features",
    types={features_FeatureSet, FeatureSetDescriptor, features_FeatureSetDescriptor, features_FeatureDescriptor, features_FeatureVersionDescriptor, features_Feature, FeatureDescriptor, features_FeatureVersion, FeatureVersionDescriptor},
    associations={feature3, features0, featureSet1, featureVersions2},
    generalizations={gen_features_FeatureSet_FeatureSetDescriptor, gen_features_Feature_FeatureDescriptor, gen_features_FeatureVersion_FeatureVersionDescriptor},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)