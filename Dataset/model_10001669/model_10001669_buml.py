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

# Enumerations
Enumeration_: Enumeration = Enumeration(
    name="Enumeration",
    literals={
            
    }
)

# Classes
A = Class(name="A")
B = Class(name="B")
C = Class(name="C")
Aeroport = Class(name="Aeroport")
Vol = Class(name="Vol")

# A class attributes and methods
A_attA: Property = Property(name="attA", type=StringType)
A.attributes={A_attA}

# B class attributes and methods
B_attB: Property = Property(name="attB", type=IntegerType)
B.attributes={B_attB}

# C class attributes and methods
C_attC1: Property = Property(name="attC1", type=IntegerType)
C_attC2: Property = Property(name="attC2", type=BooleanType)
C.attributes={C_attC1, C_attC2}

# Aeroport class attributes and methods
Aeroport_nomAeroport: Property = Property(name="nomAeroport", type=StringType)
Aeroport_altitude: Property = Property(name="altitude", type=IntegerType)
Aeroport.attributes={Aeroport_nomAeroport, Aeroport_altitude}

# Vol class attributes and methods
Vol_numeroVol: Property = Property(name="numeroVol", type=StringType)
Vol_etatVol: Property = Property(name="etatVol", type=Enumeration_)
Vol_dateHeureDepart: Property = Property(name="dateHeureDepart", type=StringType)
Vol_dateHeureArrivee: Property = Property(name="dateHeureArrivee", type=StringType)
Vol.attributes={Vol_numeroVol, Vol_etatVol, Vol_dateHeureDepart, Vol_dateHeureArrivee}

# Relationships
A_B: BinaryAssociation = BinaryAssociation(
    name="A_B",
    ends={
        Property(name="b0", type=B, multiplicity=Multiplicity(0, 1)),
        Property(name="a1", type=A, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_Nk8KoM69EeeMV96X50GAvA",
    types={A, B, C, Aeroport, Vol, Enumeration_},
    associations={A_B},
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