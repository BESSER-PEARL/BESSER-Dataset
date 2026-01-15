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
features_Model = Class(name="features::Model")
features_Feature = Class(name="features::Feature")

# features_Model class attributes and methods

# features_Feature class attributes and methods
features_Feature_abstract: Property = Property(name="abstract", type=BooleanType)
features_Feature_name: Property = Property(name="name", type=StringType)
features_Feature_short: Property = Property(name="short", type=StringType)
features_Feature.attributes={features_Feature_short, features_Feature_abstract, features_Feature_name}

# Relationships
isA2: BinaryAssociation = BinaryAssociation(
    name="isA2",
    ends={
        Property(name="features_Feature3", type=features_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="features_Feature1", type=features_Feature, multiplicity=Multiplicity(0, 1))
    }
)
isOfType5: BinaryAssociation = BinaryAssociation(
    name="isOfType5",
    ends={
        Property(name="features_Feature6", type=features_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="features_Feature4", type=features_Feature, multiplicity=Multiplicity(0, 1))
    }
)
contains8: BinaryAssociation = BinaryAssociation(
    name="contains8",
    ends={
        Property(name="features_Feature9", type=features_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="features_Feature7", type=features_Feature, multiplicity=Multiplicity(0, 9999))
    }
)
uses11: BinaryAssociation = BinaryAssociation(
    name="uses11",
    ends={
        Property(name="features_Feature12", type=features_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="features_Feature10", type=features_Feature, multiplicity=Multiplicity(0, 9999))
    }
)
features0: BinaryAssociation = BinaryAssociation(
    name="features0",
    ends={
        Property(name="features_Feature", type=features_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="features_Model", type=features_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="features",
    types={features_Model, features_Feature},
    associations={isA2, isOfType5, contains8, uses11, features0},
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