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
domainmodel_Feature = Class(name="domainmodel::Feature")
domainmodel_Domainmodel = Class(name="domainmodel::Domainmodel")
domainmodel_Type = Class(name="domainmodel::Type")
domainmodel_DataType = Class(name="domainmodel::DataType")
Type = Class(name="Type")
domainmodel_Entity = Class(name="domainmodel::Entity")

# domainmodel_Feature class attributes and methods
domainmodel_Feature_many: Property = Property(name="many", type=BooleanType)
domainmodel_Feature_name: Property = Property(name="name", type=StringType)
domainmodel_Feature.attributes={domainmodel_Feature_many, domainmodel_Feature_name}

# domainmodel_Domainmodel class attributes and methods

# domainmodel_Type class attributes and methods
domainmodel_Type_name: Property = Property(name="name", type=StringType)
domainmodel_Type.attributes={domainmodel_Type_name}

# domainmodel_DataType class attributes and methods

# Type class attributes and methods

# domainmodel_Entity class attributes and methods

# Relationships
superType2: BinaryAssociation = BinaryAssociation(
    name="superType2",
    ends={
        Property(name="domainmodel_Entity", type=domainmodel_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="domainmodel_Entity1", type=domainmodel_Entity, multiplicity=Multiplicity(0, 1))
    }
)
features3: BinaryAssociation = BinaryAssociation(
    name="features3",
    ends={
        Property(name="domainmodel_Feature", type=domainmodel_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="domainmodel_Entity4", type=domainmodel_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type5: BinaryAssociation = BinaryAssociation(
    name="type5",
    ends={
        Property(name="domainmodel_Type7", type=domainmodel_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="domainmodel_Feature6", type=domainmodel_Type, multiplicity=Multiplicity(0, 1))
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
gen_domainmodel_DataType_Type = Generalization(general=Type, specific=domainmodel_DataType)
gen_domainmodel_Entity_Type = Generalization(general=Type, specific=domainmodel_Entity)

# Domain Model
domain_model = DomainModel(
    name="domainmodel",
    types={domainmodel_Feature, domainmodel_Domainmodel, domainmodel_Type, domainmodel_DataType, Type, domainmodel_Entity},
    associations={superType2, features3, type5, elements0},
    generalizations={gen_domainmodel_DataType_Type, gen_domainmodel_Entity_Type},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)