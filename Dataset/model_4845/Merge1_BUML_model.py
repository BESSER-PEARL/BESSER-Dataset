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
merge_Clazz = Class(name="merge::Clazz")

# merge_Clazz class attributes and methods
merge_Clazz_attribute: Property = Property(name="attribute", type=StringType)
merge_Clazz_m_operation: Method = Method(name="operation", parameters={}, type=StringType)
merge_Clazz_m_operation2: Method = Method(name="operation2", parameters={Parameter(name='param')})
merge_Clazz.attributes={merge_Clazz_attribute}
merge_Clazz.methods={merge_Clazz_m_operation, merge_Clazz_m_operation2}

# Relationships
reference1: BinaryAssociation = BinaryAssociation(
    name="reference1",
    ends={
        Property(name="merge_Clazz", type=merge_Clazz, multiplicity=Multiplicity(1, 1)),
        Property(name="merge_Clazz0", type=merge_Clazz, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="merge",
    types={merge_Clazz},
    associations={reference1},
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