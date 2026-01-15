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
test2_Classe = Class(name="test2::Classe")
N = Class(name="N")
B = Class(name="B")
test2_N = Class(name="test2::N", is_abstract=True)
test2_test2_B = Class(name="test2::test2::B")

# test2_Classe class attributes and methods

# N class attributes and methods

# B class attributes and methods

# test2_N class attributes and methods
test2_N_n: Property = Property(name="n", type=StringType)
test2_N.attributes={test2_N_n}

# test2_test2_B class attributes and methods
test2_test2_B_nb: Property = Property(name="nb", type=IntegerType)
test2_test2_B_nb2: Property = Property(name="nb2", type=IntegerType)
test2_test2_B.attributes={test2_test2_B_nb, test2_test2_B_nb2}

# Relationships
eleves0: BinaryAssociation = BinaryAssociation(
    name="eleves0",
    ends={
        Property(name="B", type=test2_Classe, multiplicity=Multiplicity(1, 1)),
        Property(name="test2_Classe", type=B, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_test2_Classe_N = Generalization(general=N, specific=test2_Classe)
gen_test2_test2_B_N = Generalization(general=N, specific=test2_test2_B)

# Domain Model
domain_model = DomainModel(
    name="test2",
    types={test2_Classe, N, B, test2_N, test2_test2_B},
    associations={eleves0},
    generalizations={gen_test2_Classe_N, gen_test2_test2_B_N},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)