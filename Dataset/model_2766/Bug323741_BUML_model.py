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
my_Entity = Class(name="my::Entity")
my_Model = Class(name="my::Model")
my_BType = Class(name="my::BType")
my_AType = Class(name="my::AType")
Entity = Class(name="Entity")

# my_Entity class attributes and methods
my_Entity_name: Property = Property(name="name", type=StringType)
my_Entity.attributes={my_Entity_name}

# my_Model class attributes and methods

# my_BType class attributes and methods

# my_AType class attributes and methods
my_AType_m_referenced: Method = Method(name="referenced", parameters={}, type=StringType)
my_AType.methods={my_AType_m_referenced}

# Entity class attributes and methods

# Relationships
bs0: BinaryAssociation = BinaryAssociation(
    name="bs0",
    ends={
        Property(name="my_BType", type=my_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="my_Model", type=my_BType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referencedAttr1: BinaryAssociation = BinaryAssociation(
    name="referencedAttr1",
    ends={
        Property(name="my_BType2", type=my_AType, multiplicity=Multiplicity(1, 1)),
        Property(name="my_AType", type=my_BType, multiplicity=Multiplicity(0, 1))
    }
)
references3: BinaryAssociation = BinaryAssociation(
    name="references3",
    ends={
        Property(name="my_AType5", type=my_BType, multiplicity=Multiplicity(1, 1)),
        Property(name="my_BType4", type=my_AType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_my_AType_Entity = Generalization(general=Entity, specific=my_AType)
gen_my_BType_Entity = Generalization(general=Entity, specific=my_BType)

# Domain Model
domain_model = DomainModel(
    name="my",
    types={my_Entity, my_Model, my_BType, my_AType, Entity},
    associations={bs0, referencedAttr1, references3},
    generalizations={gen_my_AType_Entity, gen_my_BType_Entity},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)