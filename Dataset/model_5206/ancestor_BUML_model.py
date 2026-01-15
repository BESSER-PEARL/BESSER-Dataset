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
ancestor_A = Class(name="ancestor::A")
ancestor_B = Class(name="ancestor::B")
ancestor_C = Class(name="ancestor::C")
ancestor_D = Class(name="ancestor::D")

# ancestor_A class attributes and methods
ancestor_A_m_op1: Method = Method(name="op1", parameters={})
ancestor_A_m_op2: Method = Method(name="op2", parameters={})
ancestor_A.methods={ancestor_A_m_op1, ancestor_A_m_op2}

# ancestor_B class attributes and methods
ancestor_B_m_op1: Method = Method(name="op1", parameters={})
ancestor_B_m_op2: Method = Method(name="op2", parameters={})
ancestor_B.methods={ancestor_B_m_op2, ancestor_B_m_op1}

# ancestor_C class attributes and methods
ancestor_C_m_op1: Method = Method(name="op1", parameters={})
ancestor_C_m_op2: Method = Method(name="op2", parameters={})
ancestor_C.methods={ancestor_C_m_op1, ancestor_C_m_op2}

# ancestor_D class attributes and methods
ancestor_D_m_op1: Method = Method(name="op1", parameters={})
ancestor_D_m_op2: Method = Method(name="op2", parameters={})
ancestor_D.methods={ancestor_D_m_op2, ancestor_D_m_op1}

# Domain Model
domain_model = DomainModel(
    name="ancestor",
    types={ancestor_A, ancestor_B, ancestor_C, ancestor_D},
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