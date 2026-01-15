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
uml2_Classe = Class(name="uml2::Classe")
N = Class(name="N")
B = Class(name="B")
uml2_N = Class(name="uml2::N", is_abstract=True)
uml2_test2_B = Class(name="uml2::test2::B")

# uml2_Classe class attributes and methods

# N class attributes and methods

# B class attributes and methods

# uml2_N class attributes and methods
uml2_N_n: Property = Property(name="n", type=StringType)
uml2_N.attributes={uml2_N_n}

# uml2_test2_B class attributes and methods
uml2_test2_B_nb: Property = Property(name="nb", type=IntegerType)
uml2_test2_B_nb2: Property = Property(name="nb2", type=IntegerType)
uml2_test2_B.attributes={uml2_test2_B_nb2, uml2_test2_B_nb}

# Relationships
eleves0: BinaryAssociation = BinaryAssociation(
    name="eleves0",
    ends={
        Property(name="B", type=uml2_Classe, multiplicity=Multiplicity(1, 1)),
        Property(name="uml2_Classe", type=B, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_uml2_Classe_N = Generalization(general=N, specific=uml2_Classe)
gen_uml2_test2_B_N = Generalization(general=N, specific=uml2_test2_B)

# Domain Model
domain_model = DomainModel(
    name="uml2",
    types={uml2_Classe, N, B, uml2_N, uml2_test2_B},
    associations={eleves0},
    generalizations={gen_uml2_Classe_N, gen_uml2_test2_B_N},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)