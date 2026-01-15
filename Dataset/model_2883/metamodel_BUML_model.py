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
metamodel_Model = Class(name="metamodel::Model")
metamodel_Type = Class(name="metamodel::Type", is_abstract=True)
metamodel_Datatype = Class(name="metamodel::Datatype")
Type = Class(name="Type")
metamodel_Entity = Class(name="metamodel::Entity")
metamodel_Feature = Class(name="metamodel::Feature")

# metamodel_Model class attributes and methods

# metamodel_Type class attributes and methods
metamodel_Type_name: Property = Property(name="name", type=StringType)
metamodel_Type.attributes={metamodel_Type_name}

# metamodel_Datatype class attributes and methods

# Type class attributes and methods

# metamodel_Entity class attributes and methods

# metamodel_Feature class attributes and methods
metamodel_Feature_name: Property = Property(name="name", type=StringType)
metamodel_Feature.attributes={metamodel_Feature_name}

# Relationships
types0: BinaryAssociation = BinaryAssociation(
    name="types0",
    ends={
        Property(name="metamodel_Type", type=metamodel_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodel_Model", type=metamodel_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type2: BinaryAssociation = BinaryAssociation(
    name="type2",
    ends={
        Property(name="metamodel_Type4", type=metamodel_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodel_Feature3", type=metamodel_Type, multiplicity=Multiplicity(0, 1))
    }
)
features1: BinaryAssociation = BinaryAssociation(
    name="features1",
    ends={
        Property(name="metamodel_Feature", type=metamodel_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodel_Entity", type=metamodel_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_metamodel_Datatype_Type = Generalization(general=Type, specific=metamodel_Datatype)
gen_metamodel_Entity_Type = Generalization(general=Type, specific=metamodel_Entity)

# Domain Model
domain_model = DomainModel(
    name="metamodel",
    types={metamodel_Model, metamodel_Type, metamodel_Datatype, Type, metamodel_Entity, metamodel_Feature},
    associations={types0, type2, features1},
    generalizations={gen_metamodel_Datatype_Type, gen_metamodel_Entity_Type},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)