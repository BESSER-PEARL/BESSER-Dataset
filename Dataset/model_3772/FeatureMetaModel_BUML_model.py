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
feature_Model = Class(name="feature::Model")
feature_Feature = Class(name="feature::Feature")

# feature_Model class attributes and methods
feature_Model_features: Property = Property(name="features", type=StringType)
feature_Model.attributes={feature_Model_features}

# feature_Feature class attributes and methods
feature_Feature_attribute: Property = Property(name="attribute", type=StringType)
feature_Feature_max: Property = Property(name="max", type=IntegerType)
feature_Feature_min: Property = Property(name="min", type=IntegerType)
feature_Feature_isSelected: Property = Property(name="isSelected", type=BooleanType)
feature_Feature_name: Property = Property(name="name", type=StringType)
feature_Feature.attributes={feature_Feature_attribute, feature_Feature_min, feature_Feature_isSelected, feature_Feature_name, feature_Feature_max}

# Relationships
features1: BinaryAssociation = BinaryAssociation(
    name="features1",
    ends={
        Property(name="feature_Feature", type=feature_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="feature_Feature0", type=feature_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="feature",
    types={feature_Model, feature_Feature},
    associations={features1},
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