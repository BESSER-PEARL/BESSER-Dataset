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
feature_AnnotatedSimpleFeature = Class(name="feature::AnnotatedSimpleFeature")
SimpleFeature = Class(name="SimpleFeature")
feature_SimpleIdentifier = Class(name="feature::SimpleIdentifier")
feature_Feature = Class(name="feature::Feature")
feature_Value = Class(name="feature::Value")
feature_SimpleOntologyTerm = Class(name="feature::SimpleOntologyTerm")
feature_EvidenceCode = Class(name="feature::EvidenceCode")
feature_FeatureSet = Class(name="feature::FeatureSet")
feature_SimpleFeature = Class(name="feature::SimpleFeature")
SimpleIdentifier = Class(name="SimpleIdentifier")

# feature_AnnotatedSimpleFeature class attributes and methods

# SimpleFeature class attributes and methods

# feature_SimpleIdentifier class attributes and methods

# feature_Feature class attributes and methods

# feature_Value class attributes and methods

# feature_SimpleOntologyTerm class attributes and methods

# feature_EvidenceCode class attributes and methods

# feature_FeatureSet class attributes and methods

# feature_SimpleFeature class attributes and methods
feature_SimpleFeature_valueString: Property = Property(name="valueString", type=StringType)
feature_SimpleFeature.attributes={feature_SimpleFeature_valueString}

# SimpleIdentifier class attributes and methods

# Relationships
annotations0: BinaryAssociation = BinaryAssociation(
    name="annotations0",
    ends={
        Property(name="feature_SimpleIdentifier", type=feature_AnnotatedSimpleFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="feature_AnnotatedSimpleFeature", type=feature_SimpleIdentifier, multiplicity=Multiplicity(0, 9999))
    }
)
values1: BinaryAssociation = BinaryAssociation(
    name="values1",
    ends={
        Property(name="feature_Value", type=feature_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="feature_Feature", type=feature_Value, multiplicity=Multiplicity(0, 9999))
    }
)
unit2: BinaryAssociation = BinaryAssociation(
    name="unit2",
    ends={
        Property(name="feature_SimpleOntologyTerm", type=feature_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="feature_Feature3", type=feature_SimpleOntologyTerm, multiplicity=Multiplicity(1, 1))
    }
)
supportingEvidence4: BinaryAssociation = BinaryAssociation(
    name="supportingEvidence4",
    ends={
        Property(name="feature_EvidenceCode", type=feature_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="feature_Feature5", type=feature_EvidenceCode, multiplicity=Multiplicity(0, 9999))
    }
)
features6: BinaryAssociation = BinaryAssociation(
    name="features6",
    ends={
        Property(name="feature_SimpleFeature", type=feature_FeatureSet, multiplicity=Multiplicity(1, 1)),
        Property(name="feature_FeatureSet", type=feature_SimpleFeature, multiplicity=Multiplicity(0, 9999))
    }
)
type7: BinaryAssociation = BinaryAssociation(
    name="type7",
    ends={
        Property(name="feature_SimpleOntologyTerm9", type=feature_SimpleFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="feature_SimpleFeature8", type=feature_SimpleOntologyTerm, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_feature_AnnotatedSimpleFeature_SimpleFeature = Generalization(general=SimpleFeature, specific=feature_AnnotatedSimpleFeature)
gen_feature_Feature_SimpleFeature = Generalization(general=SimpleFeature, specific=feature_Feature)
gen_feature_FeatureSet_SimpleFeature = Generalization(general=SimpleFeature, specific=feature_FeatureSet)
gen_feature_SimpleFeature_SimpleIdentifier = Generalization(general=SimpleIdentifier, specific=feature_SimpleFeature)

# Domain Model
domain_model = DomainModel(
    name="feature",
    types={feature_AnnotatedSimpleFeature, SimpleFeature, feature_SimpleIdentifier, feature_Feature, feature_Value, feature_SimpleOntologyTerm, feature_EvidenceCode, feature_FeatureSet, feature_SimpleFeature, SimpleIdentifier},
    associations={annotations0, values1, unit2, supportingEvidence4, features6, type7},
    generalizations={gen_feature_AnnotatedSimpleFeature_SimpleFeature, gen_feature_Feature_SimpleFeature, gen_feature_FeatureSet_SimpleFeature, gen_feature_SimpleFeature_SimpleIdentifier},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)