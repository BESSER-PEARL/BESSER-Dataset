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
feaMo_Model = Class(name="feaMo::Model")
feaMo_FeatureModel = Class(name="feaMo::FeatureModel")
feaMo_FeamoFeatureConfig = Class(name="feaMo::FeamoFeatureConfig")
feaMo_FeatureDetails = Class(name="feaMo::FeatureDetails")
feaMo_FeatureDef = Class(name="feaMo::FeatureDef")
feaMo_FeatureConstraint = Class(name="feaMo::FeatureConstraint")
feaMo_FeatureGroup = Class(name="feaMo::FeatureGroup")
feaMo_SimpleFeature = Class(name="feaMo::SimpleFeature")
feaMo_Feature = Class(name="feaMo::Feature")
feaMo_FeamoFSelector = Class(name="feaMo::FeamoFSelector")

# feaMo_Model class attributes and methods

# feaMo_FeatureModel class attributes and methods
feaMo_FeatureModel_name: Property = Property(name="name", type=StringType)
feaMo_FeatureModel.attributes={feaMo_FeatureModel_name}

# feaMo_FeamoFeatureConfig class attributes and methods
feaMo_FeamoFeatureConfig_name: Property = Property(name="name", type=StringType)
feaMo_FeamoFeatureConfig.attributes={feaMo_FeamoFeatureConfig_name}

# feaMo_FeatureDetails class attributes and methods

# feaMo_FeatureDef class attributes and methods

# feaMo_FeatureConstraint class attributes and methods
feaMo_FeatureConstraint_rel: Property = Property(name="rel", type=StringType)
feaMo_FeatureConstraint.attributes={feaMo_FeatureConstraint_rel}

# feaMo_FeatureGroup class attributes and methods

# feaMo_SimpleFeature class attributes and methods

# feaMo_Feature class attributes and methods
feaMo_Feature_name: Property = Property(name="name", type=StringType)
feaMo_Feature.attributes={feaMo_Feature_name}

# feaMo_FeamoFSelector class attributes and methods

# Relationships
featureModels0: BinaryAssociation = BinaryAssociation(
    name="featureModels0",
    ends={
        Property(name="feaMo_FeatureModel", type=feaMo_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="feaMo_Model", type=feaMo_FeatureModel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
details3: BinaryAssociation = BinaryAssociation(
    name="details3",
    ends={
        Property(name="feaMo_FeatureDetails", type=feaMo_FeatureModel, multiplicity=Multiplicity(1, 1)),
        Property(name="feaMo_FeatureModel4", type=feaMo_FeatureDetails, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
defs5: BinaryAssociation = BinaryAssociation(
    name="defs5",
    ends={
        Property(name="feaMo_FeatureDef", type=feaMo_FeatureModel, multiplicity=Multiplicity(1, 1)),
        Property(name="feaMo_FeatureModel6", type=feaMo_FeatureDef, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
constraints7: BinaryAssociation = BinaryAssociation(
    name="constraints7",
    ends={
        Property(name="feaMo_FeatureConstraint", type=feaMo_FeatureModel, multiplicity=Multiplicity(1, 1)),
        Property(name="feaMo_FeatureModel8", type=feaMo_FeatureConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
groups9: BinaryAssociation = BinaryAssociation(
    name="groups9",
    ends={
        Property(name="feaMo_FeatureGroup", type=feaMo_FeatureDetails, multiplicity=Multiplicity(1, 1)),
        Property(name="feaMo_FeatureDetails10", type=feaMo_FeatureGroup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
configs1: BinaryAssociation = BinaryAssociation(
    name="configs1",
    ends={
        Property(name="feaMo_FeamoFeatureConfig", type=feaMo_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="feaMo_Model2", type=feaMo_FeamoFeatureConfig, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
simple11: BinaryAssociation = BinaryAssociation(
    name="simple11",
    ends={
        Property(name="feaMo_SimpleFeature", type=feaMo_FeatureGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="feaMo_FeatureGroup12", type=feaMo_SimpleFeature, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
alt13: BinaryAssociation = BinaryAssociation(
    name="alt13",
    ends={
        Property(name="feaMo_SimpleFeature15", type=feaMo_FeatureGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="feaMo_FeatureGroup14", type=feaMo_SimpleFeature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
or16: BinaryAssociation = BinaryAssociation(
    name="or16",
    ends={
        Property(name="feaMo_SimpleFeature18", type=feaMo_FeatureGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="feaMo_FeatureGroup17", type=feaMo_SimpleFeature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mandatory19: BinaryAssociation = BinaryAssociation(
    name="mandatory19",
    ends={
        Property(name="feaMo_Feature", type=feaMo_SimpleFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="feaMo_SimpleFeature20", type=feaMo_Feature, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
optional21: BinaryAssociation = BinaryAssociation(
    name="optional21",
    ends={
        Property(name="feaMo_Feature23", type=feaMo_SimpleFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="feaMo_SimpleFeature22", type=feaMo_Feature, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
feature24: BinaryAssociation = BinaryAssociation(
    name="feature24",
    ends={
        Property(name="feaMo_Feature26", type=feaMo_FeatureDef, multiplicity=Multiplicity(1, 1)),
        Property(name="feaMo_FeatureDef25", type=feaMo_Feature, multiplicity=Multiplicity(0, 1))
    }
)
details27: BinaryAssociation = BinaryAssociation(
    name="details27",
    ends={
        Property(name="feaMo_FeatureDetails29", type=feaMo_FeatureDef, multiplicity=Multiplicity(1, 1)),
        Property(name="feaMo_FeatureDef28", type=feaMo_FeatureDetails, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
feature130: BinaryAssociation = BinaryAssociation(
    name="feature130",
    ends={
        Property(name="feaMo_Feature32", type=feaMo_FeatureConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="feaMo_FeatureConstraint31", type=feaMo_Feature, multiplicity=Multiplicity(0, 1))
    }
)
feature233: BinaryAssociation = BinaryAssociation(
    name="feature233",
    ends={
        Property(name="feaMo_Feature35", type=feaMo_FeatureConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="feaMo_FeatureConstraint34", type=feaMo_Feature, multiplicity=Multiplicity(0, 1))
    }
)
feature36: BinaryAssociation = BinaryAssociation(
    name="feature36",
    ends={
        Property(name="feaMo_Feature37", type=feaMo_FeamoFSelector, multiplicity=Multiplicity(1, 1)),
        Property(name="feaMo_FeamoFSelector", type=feaMo_Feature, multiplicity=Multiplicity(0, 9999))
    }
)
selected41: BinaryAssociation = BinaryAssociation(
    name="selected41",
    ends={
        Property(name="feaMo_FeamoFeatureConfig42", type=feaMo_Feature, multiplicity=Multiplicity(0, 9999)),
        Property(name="feaMo_Feature43", type=feaMo_FeamoFeatureConfig, multiplicity=Multiplicity(1, 1))
    }
)
fm38: BinaryAssociation = BinaryAssociation(
    name="fm38",
    ends={
        Property(name="feaMo_FeatureModel40", type=feaMo_FeamoFeatureConfig, multiplicity=Multiplicity(1, 1)),
        Property(name="feaMo_FeamoFeatureConfig39", type=feaMo_FeatureModel, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="feaMo",
    types={feaMo_Model, feaMo_FeatureModel, feaMo_FeamoFeatureConfig, feaMo_FeatureDetails, feaMo_FeatureDef, feaMo_FeatureConstraint, feaMo_FeatureGroup, feaMo_SimpleFeature, feaMo_Feature, feaMo_FeamoFSelector},
    associations={featureModels0, details3, defs5, constraints7, groups9, configs1, simple11, alt13, or16, mandatory19, optional21, feature24, details27, feature130, feature233, feature36, selected41, fm38},
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