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
ConstraintType: Enumeration = Enumeration(
    name="ConstraintType",
    literals={
            EnumerationLiteral(name="EXCLUDES"),
			EnumerationLiteral(name="REQUIRES")
    }
)

# Classes
featuremodels_Feature = Class(name="featuremodels::Feature")
featuremodels_Instance = Class(name="featuremodels::Instance")
featuremodels_ContainmentAssociation = Class(name="featuremodels::ContainmentAssociation")
featuremodels_Attribute = Class(name="featuremodels::Attribute", is_abstract=True)
featuremodels_FeatureModel = Class(name="featuremodels::FeatureModel")
featuremodels_Constraint = Class(name="featuremodels::Constraint")
featuremodels_SimpleAttribute = Class(name="featuremodels::SimpleAttribute")
Attribute = Class(name="Attribute")

# featuremodels_Feature class attributes and methods
featuremodels_Feature_name: Property = Property(name="name", type=StringType)
featuremodels_Feature_root: Property = Property(name="root", type=BooleanType)
featuremodels_Feature_required: Property = Property(name="required", type=BooleanType)
featuremodels_Feature_lowerBound: Property = Property(name="lowerBound", type=IntegerType)
featuremodels_Feature_upperBound: Property = Property(name="upperBound", type=IntegerType)
featuremodels_Feature.attributes={featuremodels_Feature_required, featuremodels_Feature_name, featuremodels_Feature_lowerBound, featuremodels_Feature_root, featuremodels_Feature_upperBound}

# featuremodels_Instance class attributes and methods
featuremodels_Instance_id: Property = Property(name="id", type=StringType)
featuremodels_Instance_descritpion: Property = Property(name="descritpion", type=StringType)
featuremodels_Instance.attributes={featuremodels_Instance_descritpion, featuremodels_Instance_id}

# featuremodels_ContainmentAssociation class attributes and methods
featuremodels_ContainmentAssociation_upperBound: Property = Property(name="upperBound", type=IntegerType)
featuremodels_ContainmentAssociation_lowerBound: Property = Property(name="lowerBound", type=IntegerType)
featuremodels_ContainmentAssociation.attributes={featuremodels_ContainmentAssociation_upperBound, featuremodels_ContainmentAssociation_lowerBound}

# featuremodels_Attribute class attributes and methods
featuremodels_Attribute_name: Property = Property(name="name", type=StringType)
featuremodels_Attribute.attributes={featuremodels_Attribute_name}

# featuremodels_FeatureModel class attributes and methods
featuremodels_FeatureModel_name: Property = Property(name="name", type=StringType)
featuremodels_FeatureModel.attributes={featuremodels_FeatureModel_name}

# featuremodels_Constraint class attributes and methods
featuremodels_Constraint_name: Property = Property(name="name", type=StringType)
featuremodels_Constraint_type: Property = Property(name="type", type=StringType)
featuremodels_Constraint_rule: Property = Property(name="rule", type=StringType)
featuremodels_Constraint.attributes={featuremodels_Constraint_rule, featuremodels_Constraint_name, featuremodels_Constraint_type}

# featuremodels_SimpleAttribute class attributes and methods
featuremodels_SimpleAttribute_type: Property = Property(name="type", type=StringType)
featuremodels_SimpleAttribute_value: Property = Property(name="value", type=StringType)
featuremodels_SimpleAttribute.attributes={featuremodels_SimpleAttribute_value, featuremodels_SimpleAttribute_type}

# Attribute class attributes and methods

# Relationships
subFeatures1: BinaryAssociation = BinaryAssociation(
    name="subFeatures1",
    ends={
        Property(name="featureParent", type=featuremodels_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="Feature", type=featuremodels_Feature, multiplicity=Multiplicity(1, 1))
    }
)
constraints16: BinaryAssociation = BinaryAssociation(
    name="constraints16",
    ends={
        Property(name="featuremodels_FeatureModel17", type=featuremodels_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="featuremodels_Constraint", type=featuremodels_FeatureModel, multiplicity=Multiplicity(1, 1))
    }
)
featureParent3: BinaryAssociation = BinaryAssociation(
    name="featureParent3",
    ends={
        Property(name="Feature4", type=featuremodels_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="subFeatures", type=featuremodels_Feature, multiplicity=Multiplicity(0, 1))
    }
)
containers5: BinaryAssociation = BinaryAssociation(
    name="containers5",
    ends={
        Property(name="ContainmentAssociation", type=featuremodels_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="parent", type=featuremodels_ContainmentAssociation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
containerParent6: BinaryAssociation = BinaryAssociation(
    name="containerParent6",
    ends={
        Property(name="ContainmentAssociation8", type=featuremodels_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="subFeatures7", type=featuremodels_ContainmentAssociation, multiplicity=Multiplicity(0, 1))
    }
)
attributes9: BinaryAssociation = BinaryAssociation(
    name="attributes9",
    ends={
        Property(name="featuremodels_Attribute", type=featuremodels_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="featuremodels_Feature", type=featuremodels_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subFeatures10: BinaryAssociation = BinaryAssociation(
    name="subFeatures10",
    ends={
        Property(name="Feature11", type=featuremodels_ContainmentAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="containerParent", type=featuremodels_Feature, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
parent12: BinaryAssociation = BinaryAssociation(
    name="parent12",
    ends={
        Property(name="Feature13", type=featuremodels_ContainmentAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="containers", type=featuremodels_Feature, multiplicity=Multiplicity(0, 1))
    }
)
rootFeature14: BinaryAssociation = BinaryAssociation(
    name="rootFeature14",
    ends={
        Property(name="featuremodels_Feature15", type=featuremodels_FeatureModel, multiplicity=Multiplicity(1, 1)),
        Property(name="featuremodels_FeatureModel", type=featuremodels_Feature, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
instances18: BinaryAssociation = BinaryAssociation(
    name="instances18",
    ends={
        Property(name="featuremodels_Instance", type=featuremodels_FeatureModel, multiplicity=Multiplicity(1, 1)),
        Property(name="featuremodels_FeatureModel19", type=featuremodels_Instance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
selectedFeatures20: BinaryAssociation = BinaryAssociation(
    name="selectedFeatures20",
    ends={
        Property(name="featuremodels_Feature22", type=featuremodels_Instance, multiplicity=Multiplicity(1, 1)),
        Property(name="featuremodels_Instance21", type=featuremodels_Feature, multiplicity=Multiplicity(1, 9999))
    }
)

# Generalizations
gen_featuremodels_SimpleAttribute_Attribute = Generalization(general=Attribute, specific=featuremodels_SimpleAttribute)

# Domain Model
domain_model = DomainModel(
    name="featuremodels",
    types={featuremodels_Feature, featuremodels_Instance, featuremodels_ContainmentAssociation, featuremodels_Attribute, featuremodels_FeatureModel, featuremodels_Constraint, featuremodels_SimpleAttribute, Attribute, ConstraintType},
    associations={subFeatures1, constraints16, featureParent3, containers5, containerParent6, attributes9, subFeatures10, parent12, rootFeature14, instances18, selectedFeatures20},
    generalizations={gen_featuremodels_SimpleAttribute_Attribute},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)