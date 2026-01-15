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
db2EntityDsl_EntityColumnMapper = Class(name="db2EntityDsl::EntityColumnMapper")
AbstractColumnMapper = Class(name="AbstractColumnMapper")
db2EntityDsl_Attribute = Class(name="db2EntityDsl::Attribute")

# db2EntityDsl_EntityColumnMapper class attributes and methods

# AbstractColumnMapper class attributes and methods

# db2EntityDsl_Attribute class attributes and methods

# Relationships
entity0: BinaryAssociation = BinaryAssociation(
    name="entity0",
    ends={
        Property(name="db2EntityDsl_Attribute", type=db2EntityDsl_EntityColumnMapper, multiplicity=Multiplicity(1, 1)),
        Property(name="db2EntityDsl_EntityColumnMapper", type=db2EntityDsl_Attribute, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_db2EntityDsl_EntityColumnMapper_AbstractColumnMapper = Generalization(general=AbstractColumnMapper, specific=db2EntityDsl_EntityColumnMapper)

# Domain Model
domain_model = DomainModel(
    name="db2EntityDsl",
    types={db2EntityDsl_EntityColumnMapper, AbstractColumnMapper, db2EntityDsl_Attribute},
    associations={entity0},
    generalizations={gen_db2EntityDsl_EntityColumnMapper_AbstractColumnMapper},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)