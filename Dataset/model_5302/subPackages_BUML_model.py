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
a_ca1 = Class(name="a::ca1")
a_ca2 = Class(name="a::ca2")
a_b_cb1 = Class(name="a::b::cb1")
a_b_cb2 = Class(name="a::b::cb2")
a_d_cd1 = Class(name="a::d::cd1")
a_d_cd2 = Class(name="a::d::cd2")
a_e_ce1 = Class(name="a::e::ce1")
a_e_ce2 = Class(name="a::e::ce2")
a_c_cc1 = Class(name="a::c::cc1")
a_c_cc2 = Class(name="a::c::cc2")

# a_ca1 class attributes and methods

# a_ca2 class attributes and methods

# a_b_cb1 class attributes and methods

# a_b_cb2 class attributes and methods

# a_d_cd1 class attributes and methods

# a_d_cd2 class attributes and methods

# a_e_ce1 class attributes and methods

# a_e_ce2 class attributes and methods

# a_c_cc1 class attributes and methods

# a_c_cc2 class attributes and methods

# Domain Model
domain_model = DomainModel(
    name="a",
    types={a_ca1, a_ca2, a_b_cb1, a_b_cb2, a_d_cd1, a_d_cd2, a_e_ce1, a_e_ce2, a_c_cc1, a_c_cc2},
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