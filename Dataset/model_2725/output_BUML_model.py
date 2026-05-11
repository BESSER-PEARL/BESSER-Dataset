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
scrShYQYaSD_xvHXdRr = Class(name="scrShYQYaSD_xvHXdRr")
scrShYQYaSD_HVOwDYkMdHvynG = Class(name="scrShYQYaSD_HVOwDYkMdHvynG")
scrShYQYaSD_ak = Class(name="scrShYQYaSD_ak")

# scrShYQYaSD_xvHXdRr class attributes and methods

# scrShYQYaSD_HVOwDYkMdHvynG class attributes and methods
scrShYQYaSD_HVOwDYkMdHvynG_vdjNPHX: Property = Property(name="vdjNPHX", type=StringType)
scrShYQYaSD_HVOwDYkMdHvynG.attributes={scrShYQYaSD_HVOwDYkMdHvynG_vdjNPHX}

# scrShYQYaSD_ak class attributes and methods
scrShYQYaSD_ak_CXmvqzTe: Property = Property(name="CXmvqzTe", type=StringType)
scrShYQYaSD_ak_zBIcb: Property = Property(name="zBIcb", type=StringType)
scrShYQYaSD_ak_MHQpVCYtERyk: Property = Property(name="MHQpVCYtERyk", type=StringType)
scrShYQYaSD_ak.attributes={scrShYQYaSD_ak_MHQpVCYtERyk, scrShYQYaSD_ak_zBIcb, scrShYQYaSD_ak_CXmvqzTe}

# Relationships
njevJtUoy3: BinaryAssociation = BinaryAssociation(
    name="njevJtUoy3",
    ends={
        Property(name="scrShYQYaSD_xvHXdRr4", type=scrShYQYaSD_ak, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="scrShYQYaSD_ak5", type=scrShYQYaSD_xvHXdRr, multiplicity=Multiplicity(1, 1))
    }
)
keJwdNxMQ6: BinaryAssociation = BinaryAssociation(
    name="keJwdNxMQ6",
    ends={
        Property(name="scrShYQYaSD_ak8", type=scrShYQYaSD_xvHXdRr, multiplicity=Multiplicity(1, 1)),
        Property(name="scrShYQYaSD_xvHXdRr7", type=scrShYQYaSD_ak, multiplicity=Multiplicity(0, 1))
    }
)
JZZCZDdtPb9: BinaryAssociation = BinaryAssociation(
    name="JZZCZDdtPb9",
    ends={
        Property(name="scrShYQYaSD_ak11", type=scrShYQYaSD_xvHXdRr, multiplicity=Multiplicity(1, 1)),
        Property(name="scrShYQYaSD_xvHXdRr10", type=scrShYQYaSD_ak, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
kykuZBWLRVLW13: BinaryAssociation = BinaryAssociation(
    name="kykuZBWLRVLW13",
    ends={
        Property(name="scrShYQYaSD_ak14", type=scrShYQYaSD_ak, multiplicity=Multiplicity(1, 1)),
        Property(name="scrShYQYaSD_ak12", type=scrShYQYaSD_ak, multiplicity=Multiplicity(0, 9999))
    }
)
XObnJr15: BinaryAssociation = BinaryAssociation(
    name="XObnJr15",
    ends={
        Property(name="scrShYQYaSD_xvHXdRr17", type=scrShYQYaSD_ak, multiplicity=Multiplicity(1, 1)),
        Property(name="scrShYQYaSD_ak16", type=scrShYQYaSD_xvHXdRr, multiplicity=Multiplicity(0, 1))
    }
)
gQaACsS18: BinaryAssociation = BinaryAssociation(
    name="gQaACsS18",
    ends={
        Property(name="scrShYQYaSD_xvHXdRr20", type=scrShYQYaSD_ak, multiplicity=Multiplicity(1, 1)),
        Property(name="scrShYQYaSD_ak19", type=scrShYQYaSD_xvHXdRr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
VSMbxzKCXwhSgFqrC0: BinaryAssociation = BinaryAssociation(
    name="VSMbxzKCXwhSgFqrC0",
    ends={
        Property(name="scrShYQYaSD_HVOwDYkMdHvynG", type=scrShYQYaSD_xvHXdRr, multiplicity=Multiplicity(1, 1)),
        Property(name="scrShYQYaSD_xvHXdRr", type=scrShYQYaSD_HVOwDYkMdHvynG, multiplicity=Multiplicity(0, 9999))
    }
)
BASoFcxsCI1: BinaryAssociation = BinaryAssociation(
    name="BASoFcxsCI1",
    ends={
        Property(name="scrShYQYaSD_ak", type=scrShYQYaSD_xvHXdRr, multiplicity=Multiplicity(1, 1)),
        Property(name="scrShYQYaSD_xvHXdRr2", type=scrShYQYaSD_ak, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="scrShYQYaSD",
    types={scrShYQYaSD_xvHXdRr, scrShYQYaSD_HVOwDYkMdHvynG, scrShYQYaSD_ak},
    associations={njevJtUoy3, keJwdNxMQ6, JZZCZDdtPb9, kykuZBWLRVLW13, XObnJr15, gQaACsS18, VSMbxzKCXwhSgFqrC0, BASoFcxsCI1},
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