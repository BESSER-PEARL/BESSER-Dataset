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
domainmodel_DataType = Class(name="domainmodel::DataType")
domainmodel_Entity = Class(name="domainmodel::Entity")
Type = Class(name="Type")
domainmodel_Feature = Class(name="domainmodel::Feature")
domainmodel_Domainmodel = Class(name="domainmodel::Domainmodel")
domainmodel_Type = Class(name="domainmodel::Type")

# domainmodel_DataType class attributes and methods
domainmodel_DataType_name: Property = Property(name="name", type=StringType)
domainmodel_DataType.attributes={domainmodel_DataType_name}

# domainmodel_Entity class attributes and methods
domainmodel_Entity_name: Property = Property(name="name", type=StringType)
domainmodel_Entity.attributes={domainmodel_Entity_name}

# Type class attributes and methods

# domainmodel_Feature class attributes and methods
domainmodel_Feature_many: Property = Property(name="many", type=BooleanType)
domainmodel_Feature_name: Property = Property(name="name", type=StringType)
domainmodel_Feature_type: Property = Property(name="type", type=StringType)
domainmodel_Feature_s: Property = Property(name="s", type=StringType)
domainmodel_Feature.attributes={domainmodel_Feature_name, domainmodel_Feature_many, domainmodel_Feature_type, domainmodel_Feature_s}

# domainmodel_Domainmodel class attributes and methods

# domainmodel_Type class attributes and methods

# Relationships
sd1: BinaryAssociation = BinaryAssociation(
    name="sd1",
    ends={
        Property(name="domainmodel_DataType", type=domainmodel_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="domainmodel_Type2", type=domainmodel_DataType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
superType4: BinaryAssociation = BinaryAssociation(
    name="superType4",
    ends={
        Property(name="domainmodel_Entity", type=domainmodel_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="domainmodel_Entity3", type=domainmodel_Entity, multiplicity=Multiplicity(0, 1))
    }
)
features5: BinaryAssociation = BinaryAssociation(
    name="features5",
    ends={
        Property(name="domainmodel_Feature", type=domainmodel_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="domainmodel_Entity6", type=domainmodel_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements0: BinaryAssociation = BinaryAssociation(
    name="elements0",
    ends={
        Property(name="domainmodel_Type", type=domainmodel_Domainmodel, multiplicity=Multiplicity(1, 1)),
        Property(name="domainmodel_Domainmodel", type=domainmodel_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_domainmodel_Entity_Type = Generalization(general=Type, specific=domainmodel_Entity)

# Domain Model
domain_model = DomainModel(
    name="domainmodel",
    types={domainmodel_DataType, domainmodel_Entity, Type, domainmodel_Feature, domainmodel_Domainmodel, domainmodel_Type},
    associations={sd1, superType4, features5, elements0},
    generalizations={gen_domainmodel_Entity_Type},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)