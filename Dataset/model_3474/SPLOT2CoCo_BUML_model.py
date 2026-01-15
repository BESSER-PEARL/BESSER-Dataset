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
sPLOT2CoCo_FM = Class(name="sPLOT2CoCo::FM")
sPLOT2CoCo_Feature = Class(name="sPLOT2CoCo::Feature")
sPLOT2CoCo_ParentChildConstraint = Class(name="sPLOT2CoCo::ParentChildConstraint")
sPLOT2CoCo_FeatureAttribute = Class(name="sPLOT2CoCo::FeatureAttribute")
sPLOT2CoCo_CrossTreeConstraint = Class(name="sPLOT2CoCo::CrossTreeConstraint")
sPLOT2CoCo_TreeConstraint = Class(name="sPLOT2CoCo::TreeConstraint")
sPLOT2CoCo_MandatoryTreeConstraint = Class(name="sPLOT2CoCo::MandatoryTreeConstraint")
TreeConstraint = Class(name="TreeConstraint")
sPLOT2CoCo_OptionalTreeConstraint = Class(name="sPLOT2CoCo::OptionalTreeConstraint")
sPLOT2CoCo_OrAlternativeTreeConstraint = Class(name="sPLOT2CoCo::OrAlternativeTreeConstraint")

# sPLOT2CoCo_FM class attributes and methods

# sPLOT2CoCo_Feature class attributes and methods
sPLOT2CoCo_Feature_name: Property = Property(name="name", type=StringType)
sPLOT2CoCo_Feature.attributes={sPLOT2CoCo_Feature_name}

# sPLOT2CoCo_ParentChildConstraint class attributes and methods

# sPLOT2CoCo_FeatureAttribute class attributes and methods
sPLOT2CoCo_FeatureAttribute_attributeType: Property = Property(name="attributeType", type=StringType)
sPLOT2CoCo_FeatureAttribute_minValue: Property = Property(name="minValue", type=IntegerType)
sPLOT2CoCo_FeatureAttribute_maxValue: Property = Property(name="maxValue", type=IntegerType)
sPLOT2CoCo_FeatureAttribute_defaultValue: Property = Property(name="defaultValue", type=IntegerType)
sPLOT2CoCo_FeatureAttribute_nullValue: Property = Property(name="nullValue", type=IntegerType)
sPLOT2CoCo_FeatureAttribute.attributes={sPLOT2CoCo_FeatureAttribute_nullValue, sPLOT2CoCo_FeatureAttribute_defaultValue, sPLOT2CoCo_FeatureAttribute_attributeType, sPLOT2CoCo_FeatureAttribute_maxValue, sPLOT2CoCo_FeatureAttribute_minValue}

# sPLOT2CoCo_CrossTreeConstraint class attributes and methods
sPLOT2CoCo_CrossTreeConstraint_type: Property = Property(name="type", type=StringType)
sPLOT2CoCo_CrossTreeConstraint.attributes={sPLOT2CoCo_CrossTreeConstraint_type}

# sPLOT2CoCo_TreeConstraint class attributes and methods

# sPLOT2CoCo_MandatoryTreeConstraint class attributes and methods

# TreeConstraint class attributes and methods

# sPLOT2CoCo_OptionalTreeConstraint class attributes and methods

# sPLOT2CoCo_OrAlternativeTreeConstraint class attributes and methods
sPLOT2CoCo_OrAlternativeTreeConstraint_min: Property = Property(name="min", type=IntegerType)
sPLOT2CoCo_OrAlternativeTreeConstraint_max: Property = Property(name="max", type=IntegerType)
sPLOT2CoCo_OrAlternativeTreeConstraint.attributes={sPLOT2CoCo_OrAlternativeTreeConstraint_max, sPLOT2CoCo_OrAlternativeTreeConstraint_min}

# Relationships
features0: BinaryAssociation = BinaryAssociation(
    name="features0",
    ends={
        Property(name="sPLOT2CoCo_Feature", type=sPLOT2CoCo_FM, multiplicity=Multiplicity(1, 1)),
        Property(name="sPLOT2CoCo_FM", type=sPLOT2CoCo_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
relationships1: BinaryAssociation = BinaryAssociation(
    name="relationships1",
    ends={
        Property(name="sPLOT2CoCo_ParentChildConstraint", type=sPLOT2CoCo_FM, multiplicity=Multiplicity(1, 1)),
        Property(name="sPLOT2CoCo_FM2", type=sPLOT2CoCo_ParentChildConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributes3: BinaryAssociation = BinaryAssociation(
    name="attributes3",
    ends={
        Property(name="sPLOT2CoCo_FeatureAttribute", type=sPLOT2CoCo_FM, multiplicity=Multiplicity(1, 1)),
        Property(name="sPLOT2CoCo_FM4", type=sPLOT2CoCo_FeatureAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
crossTreeConstraints5: BinaryAssociation = BinaryAssociation(
    name="crossTreeConstraints5",
    ends={
        Property(name="sPLOT2CoCo_CrossTreeConstraint", type=sPLOT2CoCo_FM, multiplicity=Multiplicity(1, 1)),
        Property(name="sPLOT2CoCo_FM6", type=sPLOT2CoCo_CrossTreeConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent7: BinaryAssociation = BinaryAssociation(
    name="parent7",
    ends={
        Property(name="sPLOT2CoCo_Feature9", type=sPLOT2CoCo_ParentChildConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="sPLOT2CoCo_ParentChildConstraint8", type=sPLOT2CoCo_Feature, multiplicity=Multiplicity(0, 1))
    }
)
treeConstraints10: BinaryAssociation = BinaryAssociation(
    name="treeConstraints10",
    ends={
        Property(name="sPLOT2CoCo_TreeConstraint", type=sPLOT2CoCo_ParentChildConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="sPLOT2CoCo_ParentChildConstraint11", type=sPLOT2CoCo_TreeConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
feature12: BinaryAssociation = BinaryAssociation(
    name="feature12",
    ends={
        Property(name="sPLOT2CoCo_Feature13", type=sPLOT2CoCo_MandatoryTreeConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="sPLOT2CoCo_MandatoryTreeConstraint", type=sPLOT2CoCo_Feature, multiplicity=Multiplicity(0, 1))
    }
)
feature14: BinaryAssociation = BinaryAssociation(
    name="feature14",
    ends={
        Property(name="sPLOT2CoCo_Feature15", type=sPLOT2CoCo_OptionalTreeConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="sPLOT2CoCo_OptionalTreeConstraint", type=sPLOT2CoCo_Feature, multiplicity=Multiplicity(0, 1))
    }
)
features16: BinaryAssociation = BinaryAssociation(
    name="features16",
    ends={
        Property(name="sPLOT2CoCo_Feature17", type=sPLOT2CoCo_OrAlternativeTreeConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="sPLOT2CoCo_OrAlternativeTreeConstraint", type=sPLOT2CoCo_Feature, multiplicity=Multiplicity(0, 9999))
    }
)
feature118: BinaryAssociation = BinaryAssociation(
    name="feature118",
    ends={
        Property(name="sPLOT2CoCo_Feature20", type=sPLOT2CoCo_CrossTreeConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="sPLOT2CoCo_CrossTreeConstraint19", type=sPLOT2CoCo_Feature, multiplicity=Multiplicity(0, 1))
    }
)
feature221: BinaryAssociation = BinaryAssociation(
    name="feature221",
    ends={
        Property(name="sPLOT2CoCo_Feature23", type=sPLOT2CoCo_CrossTreeConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="sPLOT2CoCo_CrossTreeConstraint22", type=sPLOT2CoCo_Feature, multiplicity=Multiplicity(0, 1))
    }
)
feature24: BinaryAssociation = BinaryAssociation(
    name="feature24",
    ends={
        Property(name="sPLOT2CoCo_Feature26", type=sPLOT2CoCo_FeatureAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="sPLOT2CoCo_FeatureAttribute25", type=sPLOT2CoCo_Feature, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_sPLOT2CoCo_MandatoryTreeConstraint_TreeConstraint = Generalization(general=TreeConstraint, specific=sPLOT2CoCo_MandatoryTreeConstraint)
gen_sPLOT2CoCo_OptionalTreeConstraint_TreeConstraint = Generalization(general=TreeConstraint, specific=sPLOT2CoCo_OptionalTreeConstraint)
gen_sPLOT2CoCo_OrAlternativeTreeConstraint_TreeConstraint = Generalization(general=TreeConstraint, specific=sPLOT2CoCo_OrAlternativeTreeConstraint)

# Domain Model
domain_model = DomainModel(
    name="sPLOT2CoCo",
    types={sPLOT2CoCo_FM, sPLOT2CoCo_Feature, sPLOT2CoCo_ParentChildConstraint, sPLOT2CoCo_FeatureAttribute, sPLOT2CoCo_CrossTreeConstraint, sPLOT2CoCo_TreeConstraint, sPLOT2CoCo_MandatoryTreeConstraint, TreeConstraint, sPLOT2CoCo_OptionalTreeConstraint, sPLOT2CoCo_OrAlternativeTreeConstraint},
    associations={features0, relationships1, attributes3, crossTreeConstraints5, parent7, treeConstraints10, feature12, feature14, features16, feature118, feature221, feature24},
    generalizations={gen_sPLOT2CoCo_MandatoryTreeConstraint_TreeConstraint, gen_sPLOT2CoCo_OptionalTreeConstraint_TreeConstraint, gen_sPLOT2CoCo_OrAlternativeTreeConstraint_TreeConstraint},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)