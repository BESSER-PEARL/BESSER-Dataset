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
p_Class3 = Class(name="p::Class3")
p_Class4 = Class(name="p::Class4")
p_Exception1 = Class(name="p::Exception1")
p_Exception2 = Class(name="p::Exception2")
p_Class1 = Class(name="p::Class1")
p_Class2 = Class(name="p::Class2")

# p_Class3 class attributes and methods

# p_Class4 class attributes and methods

# p_Exception1 class attributes and methods

# p_Exception2 class attributes and methods

# p_Class1 class attributes and methods

# p_Class2 class attributes and methods
p_Class2_m_get: Method = Method(name="get", parameters={})
p_Class2_m_get2: Method = Method(name="get2", parameters={})
p_Class2_m_get3: Method = Method(name="get3", parameters={}, type=StringType)
p_Class2_m_get4: Method = Method(name="get4", parameters={})
p_Class2_m_get5: Method = Method(name="get5", parameters={})
p_Class2_m_get6: Method = Method(name="get6", parameters={}, type=StringType)
p_Class2.methods={p_Class2_m_get4, p_Class2_m_get3, p_Class2_m_get6, p_Class2_m_get2, p_Class2_m_get5, p_Class2_m_get}

# Domain Model
domain_model = DomainModel(
    name="p",
    types={p_Class3, p_Class4, p_Exception1, p_Exception2, p_Class1, p_Class2},
    associations={},
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