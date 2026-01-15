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
Master_Classe = Class(name="Master::Classe")
N = Class(name="N")
B = Class(name="B")
Master_N = Class(name="Master::N", is_abstract=True)
Master_test2_B = Class(name="Master::test2::B")

# Master_Classe class attributes and methods

# N class attributes and methods

# B class attributes and methods

# Master_N class attributes and methods
Master_N_n: Property = Property(name="n", type=StringType)
Master_N.attributes={Master_N_n}

# Master_test2_B class attributes and methods
Master_test2_B_nb: Property = Property(name="nb", type=IntegerType)
Master_test2_B_nb2: Property = Property(name="nb2", type=IntegerType)
Master_test2_B.attributes={Master_test2_B_nb, Master_test2_B_nb2}

# Relationships
eleves0: BinaryAssociation = BinaryAssociation(
    name="eleves0",
    ends={
        Property(name="B", type=Master_Classe, multiplicity=Multiplicity(1, 1)),
        Property(name="Master_Classe", type=B, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_Master_Classe_N = Generalization(general=N, specific=Master_Classe)
gen_Master_test2_B_N = Generalization(general=N, specific=Master_test2_B)

# Domain Model
domain_model = DomainModel(
    name="Master",
    types={Master_Classe, N, B, Master_N, Master_test2_B},
    associations={eleves0},
    generalizations={gen_Master_Classe_N, gen_Master_test2_B_N},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)