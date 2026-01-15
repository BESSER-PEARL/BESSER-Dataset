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
formalmetamodel_A = Class(name="formalmetamodel::A")
AA = Class(name="AA")
formalmetamodel_B = Class(name="formalmetamodel::B")
formalmetamodel_FormalModel = Class(name="formalmetamodel::FormalModel")
formalmetamodel_C = Class(name="formalmetamodel::C")
formalmetamodel_AA = Class(name="formalmetamodel::AA", is_abstract=True)

# formalmetamodel_A class attributes and methods
formalmetamodel_A_name: Property = Property(name="name", type=StringType)
formalmetamodel_A.attributes={formalmetamodel_A_name}

# AA class attributes and methods

# formalmetamodel_B class attributes and methods
formalmetamodel_B_name: Property = Property(name="name", type=StringType)
formalmetamodel_B.attributes={formalmetamodel_B_name}

# formalmetamodel_FormalModel class attributes and methods

# formalmetamodel_C class attributes and methods
formalmetamodel_C_name: Property = Property(name="name", type=StringType)
formalmetamodel_C.attributes={formalmetamodel_C_name}

# formalmetamodel_AA class attributes and methods

# Relationships
ab0: BinaryAssociation = BinaryAssociation(
    name="ab0",
    ends={
        Property(name="formalmetamodel_B", type=formalmetamodel_A, multiplicity=Multiplicity(1, 1)),
        Property(name="formalmetamodel_A", type=formalmetamodel_B, multiplicity=Multiplicity(0, 9999))
    }
)
ba1: BinaryAssociation = BinaryAssociation(
    name="ba1",
    ends={
        Property(name="formalmetamodel_A3", type=formalmetamodel_B, multiplicity=Multiplicity(1, 1)),
        Property(name="formalmetamodel_B2", type=formalmetamodel_A, multiplicity=Multiplicity(0, 9999))
    }
)
bb5: BinaryAssociation = BinaryAssociation(
    name="bb5",
    ends={
        Property(name="formalmetamodel_B6", type=formalmetamodel_B, multiplicity=Multiplicity(1, 1)),
        Property(name="formalmetamodel_B4", type=formalmetamodel_B, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
bs7: BinaryAssociation = BinaryAssociation(
    name="bs7",
    ends={
        Property(name="formalmetamodel_B8", type=formalmetamodel_FormalModel, multiplicity=Multiplicity(1, 1)),
        Property(name="formalmetamodel_FormalModel", type=formalmetamodel_B, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
as9: BinaryAssociation = BinaryAssociation(
    name="as9",
    ends={
        Property(name="formalmetamodel_A11", type=formalmetamodel_FormalModel, multiplicity=Multiplicity(1, 1)),
        Property(name="formalmetamodel_FormalModel10", type=formalmetamodel_A, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cs12: BinaryAssociation = BinaryAssociation(
    name="cs12",
    ends={
        Property(name="formalmetamodel_C", type=formalmetamodel_FormalModel, multiplicity=Multiplicity(1, 1)),
        Property(name="formalmetamodel_FormalModel13", type=formalmetamodel_C, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cs15: BinaryAssociation = BinaryAssociation(
    name="cs15",
    ends={
        Property(name="formalmetamodel_C16", type=formalmetamodel_C, multiplicity=Multiplicity(1, 1)),
        Property(name="formalmetamodel_C14", type=formalmetamodel_C, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ca17: BinaryAssociation = BinaryAssociation(
    name="ca17",
    ends={
        Property(name="formalmetamodel_A19", type=formalmetamodel_C, multiplicity=Multiplicity(1, 1)),
        Property(name="formalmetamodel_C18", type=formalmetamodel_A, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_formalmetamodel_A_AA = Generalization(general=AA, specific=formalmetamodel_A)

# Domain Model
domain_model = DomainModel(
    name="formalmetamodel",
    types={formalmetamodel_A, AA, formalmetamodel_B, formalmetamodel_FormalModel, formalmetamodel_C, formalmetamodel_AA},
    associations={ab0, ba1, bb5, bs7, as9, cs12, cs15, ca17},
    generalizations={gen_formalmetamodel_A_AA},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)