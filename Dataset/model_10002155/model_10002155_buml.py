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
CUENTA = Class(name="CUENTA")
USUARIO = Class(name="USUARIO")

# CUENTA class attributes and methods
CUENTA_Nombre: Property = Property(name="Nombre", type=StringType)
CUENTA_Tipo_de_Cuenta: Property = Property(name="Tipo_de_Cuenta", type=StringType)
CUENTA_Balance: Property = Property(name="Balance", type=IntegerType)
CUENTA.attributes={CUENTA_Tipo_de_Cuenta, CUENTA_Balance, CUENTA_Nombre}

# USUARIO class attributes and methods
USUARIO_ID: Property = Property(name="ID", type=StringType)
USUARIO_Nombre: Property = Property(name="Nombre", type=StringType)
USUARIO_Contrase_a: Property = Property(name="Contrase_a", type=StringType)
USUARIO.attributes={USUARIO_Nombre, USUARIO_Contrase_a, USUARIO_ID}

# Relationships
USUARIO_CUENTA: BinaryAssociation = BinaryAssociation(
    name="USUARIO_CUENTA",
    ends={
        Property(name="cUENTA0", type=CUENTA, multiplicity=Multiplicity(1, 9999)),
        Property(name="uSUARIO1", type=USUARIO, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_t1XgsE3sEemWEaPMP_Lifw",
    types={CUENTA, USUARIO},
    associations={USUARIO_CUENTA},
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