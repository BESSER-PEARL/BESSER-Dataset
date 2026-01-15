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
BasicFMmetamodel_FeatureModel = Class(name="BasicFMmetamodel::FeatureModel")
BasicFMmetamodel_Feature = Class(name="BasicFMmetamodel::Feature")
BasicFMmetamodel_CrossTreeConstraint = Class(name="BasicFMmetamodel::CrossTreeConstraint", is_abstract=True)
BasicFMmetamodel_Alternative = Class(name="BasicFMmetamodel::Alternative")
Feature = Class(name="Feature")
BasicFMmetamodel_OrGroup = Class(name="BasicFMmetamodel::OrGroup")

# BasicFMmetamodel_FeatureModel class attributes and methods
BasicFMmetamodel_FeatureModel_name: Property = Property(name="name", type=StringType)
BasicFMmetamodel_FeatureModel_m_getFeature: Method = Method(name="getFeature", parameters={Parameter(name='id')}, type=StringType)
BasicFMmetamodel_FeatureModel.attributes={BasicFMmetamodel_FeatureModel_name}
BasicFMmetamodel_FeatureModel.methods={BasicFMmetamodel_FeatureModel_m_getFeature}

# BasicFMmetamodel_Feature class attributes and methods
BasicFMmetamodel_Feature_id: Property = Property(name="id", type=StringType)
BasicFMmetamodel_Feature_name: Property = Property(name="name", type=StringType)
BasicFMmetamodel_Feature_mandatory: Property = Property(name="mandatory", type=BooleanType)
BasicFMmetamodel_Feature_selected: Property = Property(name="selected", type=BooleanType)
BasicFMmetamodel_Feature_m_isLeaf: Method = Method(name="isLeaf", parameters={}, type=BooleanType)
BasicFMmetamodel_Feature_m_isRoot: Method = Method(name="isRoot", parameters={}, type=BooleanType)
BasicFMmetamodel_Feature.attributes={BasicFMmetamodel_Feature_selected, BasicFMmetamodel_Feature_name, BasicFMmetamodel_Feature_mandatory, BasicFMmetamodel_Feature_id}
BasicFMmetamodel_Feature.methods={BasicFMmetamodel_Feature_m_isRoot, BasicFMmetamodel_Feature_m_isLeaf}

# BasicFMmetamodel_CrossTreeConstraint class attributes and methods

# BasicFMmetamodel_Alternative class attributes and methods

# Feature class attributes and methods

# BasicFMmetamodel_OrGroup class attributes and methods

# Relationships
root0: BinaryAssociation = BinaryAssociation(
    name="root0",
    ends={
        Property(name="BasicFMmetamodel_Feature", type=BasicFMmetamodel_FeatureModel, multiplicity=Multiplicity(1, 1)),
        Property(name="BasicFMmetamodel_FeatureModel", type=BasicFMmetamodel_Feature, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
crossTreeConstraints1: BinaryAssociation = BinaryAssociation(
    name="crossTreeConstraints1",
    ends={
        Property(name="BasicFMmetamodel_CrossTreeConstraint", type=BasicFMmetamodel_FeatureModel, multiplicity=Multiplicity(1, 1)),
        Property(name="BasicFMmetamodel_FeatureModel2", type=BasicFMmetamodel_CrossTreeConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
children4: BinaryAssociation = BinaryAssociation(
    name="children4",
    ends={
        Property(name="Feature", type=BasicFMmetamodel_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="parent", type=BasicFMmetamodel_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent6: BinaryAssociation = BinaryAssociation(
    name="parent6",
    ends={
        Property(name="Feature7", type=BasicFMmetamodel_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="children", type=BasicFMmetamodel_Feature, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_BasicFMmetamodel_Alternative_Feature = Generalization(general=Feature, specific=BasicFMmetamodel_Alternative)
gen_BasicFMmetamodel_OrGroup_Feature = Generalization(general=Feature, specific=BasicFMmetamodel_OrGroup)

# Domain Model
domain_model = DomainModel(
    name="BasicFMmetamodel",
    types={BasicFMmetamodel_FeatureModel, BasicFMmetamodel_Feature, BasicFMmetamodel_CrossTreeConstraint, BasicFMmetamodel_Alternative, Feature, BasicFMmetamodel_OrGroup},
    associations={root0, crossTreeConstraints1, children4, parent6},
    generalizations={gen_BasicFMmetamodel_Alternative_Feature, gen_BasicFMmetamodel_OrGroup_Feature},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)