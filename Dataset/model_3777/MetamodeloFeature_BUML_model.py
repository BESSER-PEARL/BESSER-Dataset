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
features_Root = Class(name="features::Root")
features_Feature = Class(name="features::Feature")

# features_Root class attributes and methods

# features_Feature class attributes and methods
features_Feature_nome: Property = Property(name="nome", type=StringType)
features_Feature_mandatory: Property = Property(name="mandatory", type=BooleanType)
features_Feature.attributes={features_Feature_mandatory, features_Feature_nome}

# Relationships
feature0: BinaryAssociation = BinaryAssociation(
    name="feature0",
    ends={
        Property(name="features_Feature", type=features_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="features_Root", type=features_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
feature2: BinaryAssociation = BinaryAssociation(
    name="feature2",
    ends={
        Property(name="features_Feature3", type=features_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="features_Feature1", type=features_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="features",
    types={features_Root, features_Feature},
    associations={feature0, feature2},
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