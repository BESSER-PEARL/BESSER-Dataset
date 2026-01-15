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
slolpBPM_DomainModel = Class(name="slolpBPM::DomainModel")
slolpBPM_Type = Class(name="slolpBPM::Type")
slolpBPM_Datatype = Class(name="slolpBPM::Datatype")
Type = Class(name="Type")
slolpBPM_Entity = Class(name="slolpBPM::Entity")
slolpBPM_Feature = Class(name="slolpBPM::Feature")

# slolpBPM_DomainModel class attributes and methods

# slolpBPM_Type class attributes and methods
slolpBPM_Type_name: Property = Property(name="name", type=StringType)
slolpBPM_Type.attributes={slolpBPM_Type_name}

# slolpBPM_Datatype class attributes and methods

# Type class attributes and methods

# slolpBPM_Entity class attributes and methods

# slolpBPM_Feature class attributes and methods
slolpBPM_Feature_name: Property = Property(name="name", type=StringType)
slolpBPM_Feature_many: Property = Property(name="many", type=BooleanType)
slolpBPM_Feature.attributes={slolpBPM_Feature_many, slolpBPM_Feature_name}

# Relationships
elements0: BinaryAssociation = BinaryAssociation(
    name="elements0",
    ends={
        Property(name="slolpBPM_Type", type=slolpBPM_DomainModel, multiplicity=Multiplicity(1, 1)),
        Property(name="slolpBPM_DomainModel", type=slolpBPM_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superType2: BinaryAssociation = BinaryAssociation(
    name="superType2",
    ends={
        Property(name="slolpBPM_Entity", type=slolpBPM_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="slolpBPM_Entity1", type=slolpBPM_Entity, multiplicity=Multiplicity(0, 1))
    }
)
type5: BinaryAssociation = BinaryAssociation(
    name="type5",
    ends={
        Property(name="slolpBPM_Type7", type=slolpBPM_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="slolpBPM_Feature6", type=slolpBPM_Type, multiplicity=Multiplicity(0, 1))
    }
)
feautres3: BinaryAssociation = BinaryAssociation(
    name="feautres3",
    ends={
        Property(name="slolpBPM_Feature", type=slolpBPM_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="slolpBPM_Entity4", type=slolpBPM_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_slolpBPM_Datatype_Type = Generalization(general=Type, specific=slolpBPM_Datatype)
gen_slolpBPM_Entity_Type = Generalization(general=Type, specific=slolpBPM_Entity)

# Domain Model
domain_model = DomainModel(
    name="slolpBPM",
    types={slolpBPM_DomainModel, slolpBPM_Type, slolpBPM_Datatype, Type, slolpBPM_Entity, slolpBPM_Feature},
    associations={elements0, superType2, type5, feautres3},
    generalizations={gen_slolpBPM_Datatype_Type, gen_slolpBPM_Entity_Type},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)