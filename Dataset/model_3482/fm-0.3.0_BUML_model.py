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
AttributeType: Enumeration = Enumeration(
    name="AttributeType",
    literals={
            EnumerationLiteral(name="BOOLEAN"),
			EnumerationLiteral(name="INTEGER"),
			EnumerationLiteral(name="DOUBLE"),
			EnumerationLiteral(name="STRING")
    }
)

# Classes
fm_FeatureModel = Class(name="fm::FeatureModel")
fm_Feature = Class(name="fm::Feature")
fm_EObject = Class(name="fm::EObject")
fm_Constraint = Class(name="fm::Constraint")
fm_Attribute = Class(name="fm::Attribute")
fm_Group = Class(name="fm::Group")

# fm_FeatureModel class attributes and methods
fm_FeatureModel_name: Property = Property(name="name", type=StringType)
fm_FeatureModel_version: Property = Property(name="version", type=StringType)
fm_FeatureModel_description: Property = Property(name="description", type=StringType)
fm_FeatureModel_comment: Property = Property(name="comment", type=StringType)
fm_FeatureModel_m_getFeaturesById: Method = Method(name="getFeaturesById", parameters={Parameter(name='id')})
fm_FeatureModel.attributes={fm_FeatureModel_name, fm_FeatureModel_description, fm_FeatureModel_version, fm_FeatureModel_comment}
fm_FeatureModel.methods={fm_FeatureModel_m_getFeaturesById}

# fm_Feature class attributes and methods
fm_Feature_id: Property = Property(name="id", type=StringType)
fm_Feature_name: Property = Property(name="name", type=StringType)
fm_Feature_description: Property = Property(name="description", type=StringType)
fm_Feature_comment: Property = Property(name="comment", type=StringType)
fm_Feature_lower: Property = Property(name="lower", type=IntegerType)
fm_Feature_upper: Property = Property(name="upper", type=IntegerType)
fm_Feature_root: Property = Property(name="root", type=BooleanType)
fm_Feature_orphan: Property = Property(name="orphan", type=BooleanType)
fm_Feature_optional: Property = Property(name="optional", type=BooleanType)
fm_Feature_mandatory: Property = Property(name="mandatory", type=BooleanType)
fm_Feature_cloneable: Property = Property(name="cloneable", type=BooleanType)
fm_Feature.attributes={fm_Feature_upper, fm_Feature_name, fm_Feature_optional, fm_Feature_lower, fm_Feature_cloneable, fm_Feature_comment, fm_Feature_orphan, fm_Feature_id, fm_Feature_description, fm_Feature_mandatory, fm_Feature_root}

# fm_EObject class attributes and methods

# fm_Constraint class attributes and methods
fm_Constraint_value: Property = Property(name="value", type=StringType)
fm_Constraint_language: Property = Property(name="language", type=StringType)
fm_Constraint_description: Property = Property(name="description", type=StringType)
fm_Constraint_comment: Property = Property(name="comment", type=StringType)
fm_Constraint.attributes={fm_Constraint_value, fm_Constraint_description, fm_Constraint_comment, fm_Constraint_language}

# fm_Attribute class attributes and methods
fm_Attribute_id: Property = Property(name="id", type=StringType)
fm_Attribute_name: Property = Property(name="name", type=StringType)
fm_Attribute_type: Property = Property(name="type", type=StringType)
fm_Attribute_value: Property = Property(name="value", type=StringType)
fm_Attribute_description: Property = Property(name="description", type=StringType)
fm_Attribute_comment: Property = Property(name="comment", type=StringType)
fm_Attribute.attributes={fm_Attribute_name, fm_Attribute_type, fm_Attribute_value, fm_Attribute_description, fm_Attribute_id, fm_Attribute_comment}

# fm_Group class attributes and methods
fm_Group_lower: Property = Property(name="lower", type=IntegerType)
fm_Group_upper: Property = Property(name="upper", type=IntegerType)
fm_Group_description: Property = Property(name="description", type=StringType)
fm_Group_comment: Property = Property(name="comment", type=StringType)
fm_Group_xor: Property = Property(name="xor", type=BooleanType)
fm_Group_or: Property = Property(name="or", type=BooleanType)
fm_Group.attributes={fm_Group_or, fm_Group_comment, fm_Group_description, fm_Group_xor, fm_Group_upper, fm_Group_lower}

# Relationships
constraints4: BinaryAssociation = BinaryAssociation(
    name="constraints4",
    ends={
        Property(name="fm_Constraint", type=fm_FeatureModel, multiplicity=Multiplicity(1, 1)),
        Property(name="fm_FeatureModel5", type=fm_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
root0: BinaryAssociation = BinaryAssociation(
    name="root0",
    ends={
        Property(name="fm_Feature", type=fm_FeatureModel, multiplicity=Multiplicity(1, 1)),
        Property(name="fm_FeatureModel", type=fm_Feature, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
orphans1: BinaryAssociation = BinaryAssociation(
    name="orphans1",
    ends={
        Property(name="fm_Feature3", type=fm_FeatureModel, multiplicity=Multiplicity(1, 1)),
        Property(name="fm_FeatureModel2", type=fm_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributes12: BinaryAssociation = BinaryAssociation(
    name="attributes12",
    ends={
        Property(name="Attribute", type=fm_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="feature", type=fm_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
features14: BinaryAssociation = BinaryAssociation(
    name="features14",
    ends={
        Property(name="Feature15", type=fm_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="parentFeature", type=fm_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
groups16: BinaryAssociation = BinaryAssociation(
    name="groups16",
    ends={
        Property(name="Group17", type=fm_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="parent", type=fm_Group, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
featureModel18: BinaryAssociation = BinaryAssociation(
    name="featureModel18",
    ends={
        Property(name="fm_FeatureModel20", type=fm_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="fm_Feature19", type=fm_FeatureModel, multiplicity=Multiplicity(0, 1))
    }
)
parent6: BinaryAssociation = BinaryAssociation(
    name="parent6",
    ends={
        Property(name="fm_EObject", type=fm_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="fm_Feature7", type=fm_EObject, multiplicity=Multiplicity(0, 1))
    }
)
parentFeature9: BinaryAssociation = BinaryAssociation(
    name="parentFeature9",
    ends={
        Property(name="Feature", type=fm_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="features", type=fm_Feature, multiplicity=Multiplicity(0, 1))
    }
)
parentGroup10: BinaryAssociation = BinaryAssociation(
    name="parentGroup10",
    ends={
        Property(name="Group", type=fm_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="features11", type=fm_Group, multiplicity=Multiplicity(0, 1))
    }
)
feature25: BinaryAssociation = BinaryAssociation(
    name="feature25",
    ends={
        Property(name="Feature26", type=fm_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="attributes", type=fm_Feature, multiplicity=Multiplicity(1, 1))
    }
)
parent21: BinaryAssociation = BinaryAssociation(
    name="parent21",
    ends={
        Property(name="Feature22", type=fm_Group, multiplicity=Multiplicity(1, 1)),
        Property(name="groups", type=fm_Feature, multiplicity=Multiplicity(1, 1))
    }
)
features23: BinaryAssociation = BinaryAssociation(
    name="features23",
    ends={
        Property(name="Feature24", type=fm_Group, multiplicity=Multiplicity(1, 1)),
        Property(name="parentGroup", type=fm_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
featureModel27: BinaryAssociation = BinaryAssociation(
    name="featureModel27",
    ends={
        Property(name="fm_FeatureModel29", type=fm_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="fm_Constraint28", type=fm_FeatureModel, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="fm",
    types={fm_FeatureModel, fm_Feature, fm_EObject, fm_Constraint, fm_Attribute, fm_Group, AttributeType},
    associations={constraints4, root0, orphans1, attributes12, features14, groups16, featureModel18, parent6, parentFeature9, parentGroup10, feature25, parent21, features23, featureModel27},
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