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
myDsl_FM = Class(name="myDsl::FM")
myDsl_Feature = Class(name="myDsl::Feature")
myDsl_FeatureAttribute = Class(name="myDsl::FeatureAttribute")
myDsl_CrossTreeConstraint = Class(name="myDsl::CrossTreeConstraint")
myDsl_TreeConstraint = Class(name="myDsl::TreeConstraint")
myDsl_ParentChildConstraint = Class(name="myDsl::ParentChildConstraint")
myDsl_OptionalTreeConstraint = Class(name="myDsl::OptionalTreeConstraint")
myDsl_OrAlternativeTreeConstraint = Class(name="myDsl::OrAlternativeTreeConstraint")
myDsl_MandatoryTreeConstraint = Class(name="myDsl::MandatoryTreeConstraint")
TreeConstraint = Class(name="TreeConstraint")

# myDsl_FM class attributes and methods

# myDsl_Feature class attributes and methods
myDsl_Feature_name: Property = Property(name="name", type=StringType)
myDsl_Feature.attributes={myDsl_Feature_name}

# myDsl_FeatureAttribute class attributes and methods
myDsl_FeatureAttribute_attributeType: Property = Property(name="attributeType", type=StringType)
myDsl_FeatureAttribute_minValue: Property = Property(name="minValue", type=IntegerType)
myDsl_FeatureAttribute_maxValue: Property = Property(name="maxValue", type=IntegerType)
myDsl_FeatureAttribute_defaultValue: Property = Property(name="defaultValue", type=IntegerType)
myDsl_FeatureAttribute_nullValue: Property = Property(name="nullValue", type=IntegerType)
myDsl_FeatureAttribute.attributes={myDsl_FeatureAttribute_nullValue, myDsl_FeatureAttribute_minValue, myDsl_FeatureAttribute_attributeType, myDsl_FeatureAttribute_maxValue, myDsl_FeatureAttribute_defaultValue}

# myDsl_CrossTreeConstraint class attributes and methods
myDsl_CrossTreeConstraint_type: Property = Property(name="type", type=StringType)
myDsl_CrossTreeConstraint.attributes={myDsl_CrossTreeConstraint_type}

# myDsl_TreeConstraint class attributes and methods

# myDsl_ParentChildConstraint class attributes and methods

# myDsl_OptionalTreeConstraint class attributes and methods

# myDsl_OrAlternativeTreeConstraint class attributes and methods
myDsl_OrAlternativeTreeConstraint_min: Property = Property(name="min", type=IntegerType)
myDsl_OrAlternativeTreeConstraint_max: Property = Property(name="max", type=IntegerType)
myDsl_OrAlternativeTreeConstraint.attributes={myDsl_OrAlternativeTreeConstraint_min, myDsl_OrAlternativeTreeConstraint_max}

# myDsl_MandatoryTreeConstraint class attributes and methods

# TreeConstraint class attributes and methods

# Relationships
relationships1: BinaryAssociation = BinaryAssociation(
    name="relationships1",
    ends={
        Property(name="myDsl_ParentChildConstraint", type=myDsl_FM, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_FM2", type=myDsl_ParentChildConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributes3: BinaryAssociation = BinaryAssociation(
    name="attributes3",
    ends={
        Property(name="myDsl_FeatureAttribute", type=myDsl_FM, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_FM4", type=myDsl_FeatureAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
crossTreeConstraints5: BinaryAssociation = BinaryAssociation(
    name="crossTreeConstraints5",
    ends={
        Property(name="myDsl_CrossTreeConstraint", type=myDsl_FM, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_FM6", type=myDsl_CrossTreeConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent7: BinaryAssociation = BinaryAssociation(
    name="parent7",
    ends={
        Property(name="myDsl_Feature9", type=myDsl_ParentChildConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ParentChildConstraint8", type=myDsl_Feature, multiplicity=Multiplicity(0, 1))
    }
)
treeConstraints10: BinaryAssociation = BinaryAssociation(
    name="treeConstraints10",
    ends={
        Property(name="myDsl_TreeConstraint", type=myDsl_ParentChildConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ParentChildConstraint11", type=myDsl_TreeConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
features0: BinaryAssociation = BinaryAssociation(
    name="features0",
    ends={
        Property(name="myDsl_Feature", type=myDsl_FM, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_FM", type=myDsl_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
feature12: BinaryAssociation = BinaryAssociation(
    name="feature12",
    ends={
        Property(name="myDsl_Feature13", type=myDsl_MandatoryTreeConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_MandatoryTreeConstraint", type=myDsl_Feature, multiplicity=Multiplicity(0, 1))
    }
)
feature14: BinaryAssociation = BinaryAssociation(
    name="feature14",
    ends={
        Property(name="myDsl_Feature15", type=myDsl_OptionalTreeConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_OptionalTreeConstraint", type=myDsl_Feature, multiplicity=Multiplicity(0, 1))
    }
)
features16: BinaryAssociation = BinaryAssociation(
    name="features16",
    ends={
        Property(name="myDsl_Feature17", type=myDsl_OrAlternativeTreeConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_OrAlternativeTreeConstraint", type=myDsl_Feature, multiplicity=Multiplicity(0, 9999))
    }
)
feature221: BinaryAssociation = BinaryAssociation(
    name="feature221",
    ends={
        Property(name="myDsl_Feature23", type=myDsl_CrossTreeConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_CrossTreeConstraint22", type=myDsl_Feature, multiplicity=Multiplicity(0, 1))
    }
)
feature24: BinaryAssociation = BinaryAssociation(
    name="feature24",
    ends={
        Property(name="myDsl_Feature26", type=myDsl_FeatureAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_FeatureAttribute25", type=myDsl_Feature, multiplicity=Multiplicity(0, 1))
    }
)
feature118: BinaryAssociation = BinaryAssociation(
    name="feature118",
    ends={
        Property(name="myDsl_Feature20", type=myDsl_CrossTreeConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_CrossTreeConstraint19", type=myDsl_Feature, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_myDsl_OptionalTreeConstraint_TreeConstraint = Generalization(general=TreeConstraint, specific=myDsl_OptionalTreeConstraint)
gen_myDsl_OrAlternativeTreeConstraint_TreeConstraint = Generalization(general=TreeConstraint, specific=myDsl_OrAlternativeTreeConstraint)
gen_myDsl_MandatoryTreeConstraint_TreeConstraint = Generalization(general=TreeConstraint, specific=myDsl_MandatoryTreeConstraint)

# Domain Model
domain_model = DomainModel(
    name="myDsl",
    types={myDsl_FM, myDsl_Feature, myDsl_FeatureAttribute, myDsl_CrossTreeConstraint, myDsl_TreeConstraint, myDsl_ParentChildConstraint, myDsl_OptionalTreeConstraint, myDsl_OrAlternativeTreeConstraint, myDsl_MandatoryTreeConstraint, TreeConstraint},
    associations={relationships1, attributes3, crossTreeConstraints5, parent7, treeConstraints10, features0, feature12, feature14, features16, feature221, feature24, feature118},
    generalizations={gen_myDsl_OptionalTreeConstraint_TreeConstraint, gen_myDsl_OrAlternativeTreeConstraint_TreeConstraint, gen_myDsl_MandatoryTreeConstraint_TreeConstraint},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)