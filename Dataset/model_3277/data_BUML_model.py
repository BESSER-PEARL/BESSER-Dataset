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
data_Variables = Class(name="data::Variables")
data_Variable = Class(name="data::Variable")

# data_Variables class attributes and methods

# data_Variable class attributes and methods
data_Variable_id: Property = Property(name="id", type=StringType)
data_Variable.attributes={data_Variable_id}

# Relationships
variables0: BinaryAssociation = BinaryAssociation(
    name="variables0",
    ends={
        Property(name="data_Variable", type=data_Variables, multiplicity=Multiplicity(1, 1)),
        Property(name="data_Variables", type=data_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="data",
    types={data_Variables, data_Variable},
    associations={variables0},
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