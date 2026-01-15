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
out_RootOut = Class(name="out::RootOut", is_abstract=True)
out_D = Class(name="out::D")
RootOut = Class(name="RootOut")
out_E = Class(name="out::E")

# out_RootOut class attributes and methods

# out_D class attributes and methods
out_D_name: Property = Property(name="name", type=StringType)
out_D.attributes={out_D_name}

# RootOut class attributes and methods

# out_E class attributes and methods
out_E_name: Property = Property(name="name", type=StringType)
out_E.attributes={out_E_name}

# Relationships
refD2: BinaryAssociation = BinaryAssociation(
    name="refD2",
    ends={
        Property(name="out_D1", type=out_D, multiplicity=Multiplicity(0, 1)),
        Property(name="out_D3", type=out_D, multiplicity=Multiplicity(1, 1))
    }
)
refD4: BinaryAssociation = BinaryAssociation(
    name="refD4",
    ends={
        Property(name="out_D6", type=out_E, multiplicity=Multiplicity(1, 1)),
        Property(name="out_E5", type=out_D, multiplicity=Multiplicity(0, 1))
    }
)
refE0: BinaryAssociation = BinaryAssociation(
    name="refE0",
    ends={
        Property(name="out_E", type=out_D, multiplicity=Multiplicity(1, 1)),
        Property(name="out_D", type=out_E, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_out_E_RootOut = Generalization(general=RootOut, specific=out_E)
gen_out_D_RootOut = Generalization(general=RootOut, specific=out_D)

# Domain Model
domain_model = DomainModel(
    name="out",
    types={out_RootOut, out_D, RootOut, out_E},
    associations={refD2, refD4, refE0},
    generalizations={gen_out_E_RootOut, gen_out_D_RootOut},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)