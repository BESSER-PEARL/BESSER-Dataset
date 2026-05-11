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
traces_RootOut = Class(name="traces_RootOut", is_abstract=True)
traces_R1_Trace = Class(name="traces_R1_Trace")
Trace = Class(name="Trace")
traces_A = Class(name="traces_A")
traces_D = Class(name="traces_D")
traces_R2_Trace = Class(name="traces_R2_Trace")
traces_B = Class(name="traces_B")
traces_E = Class(name="traces_E")
RootIn = Class(name="RootIn")
traces_C = Class(name="traces_C")
RootOut = Class(name="RootOut")
traces_Trace = Class(name="traces_Trace", is_abstract=True)
traces_RootIn = Class(name="traces_RootIn", is_abstract=True)

# traces_RootOut class attributes and methods

# traces_R1_Trace class attributes and methods

# Trace class attributes and methods

# traces_A class attributes and methods
traces_A_name: Property = Property(name="name", type=StringType)
traces_A.attributes={traces_A_name}

# traces_D class attributes and methods
traces_D_name: Property = Property(name="name", type=StringType)
traces_D.attributes={traces_D_name}

# traces_R2_Trace class attributes and methods

# traces_B class attributes and methods
traces_B_name: Property = Property(name="name", type=StringType)
traces_B.attributes={traces_B_name}

# traces_E class attributes and methods
traces_E_name: Property = Property(name="name", type=StringType)
traces_E.attributes={traces_E_name}

# RootIn class attributes and methods

# traces_C class attributes and methods
traces_C_name: Property = Property(name="name", type=StringType)
traces_C.attributes={traces_C_name}

# RootOut class attributes and methods

# traces_Trace class attributes and methods

# traces_RootIn class attributes and methods

# Relationships
from_0: BinaryAssociation = BinaryAssociation(
    name="from_0",
    ends={
        Property(name="traces_RootIn", type=traces_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="traces_Trace", type=traces_RootIn, multiplicity=Multiplicity(1, 9999))
    }
)
to1: BinaryAssociation = BinaryAssociation(
    name="to1",
    ends={
        Property(name="traces_RootOut", type=traces_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="traces_Trace2", type=traces_RootOut, multiplicity=Multiplicity(1, 9999))
    }
)
s3: BinaryAssociation = BinaryAssociation(
    name="s3",
    ends={
        Property(name="traces_A", type=traces_R1_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="traces_R1_Trace", type=traces_A, multiplicity=Multiplicity(1, 1))
    }
)
t14: BinaryAssociation = BinaryAssociation(
    name="t14",
    ends={
        Property(name="traces_D", type=traces_R1_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="traces_R1_Trace5", type=traces_D, multiplicity=Multiplicity(1, 1))
    }
)
t26: BinaryAssociation = BinaryAssociation(
    name="t26",
    ends={
        Property(name="traces_D8", type=traces_R1_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="traces_R1_Trace7", type=traces_D, multiplicity=Multiplicity(1, 1))
    }
)
s9: BinaryAssociation = BinaryAssociation(
    name="s9",
    ends={
        Property(name="traces_B", type=traces_R2_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="traces_R2_Trace", type=traces_B, multiplicity=Multiplicity(1, 1))
    }
)
t10: BinaryAssociation = BinaryAssociation(
    name="t10",
    ends={
        Property(name="traces_E", type=traces_R2_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="traces_R2_Trace11", type=traces_E, multiplicity=Multiplicity(1, 1))
    }
)
refB12: BinaryAssociation = BinaryAssociation(
    name="refB12",
    ends={
        Property(name="traces_B14", type=traces_A, multiplicity=Multiplicity(1, 1)),
        Property(name="traces_A13", type=traces_B, multiplicity=Multiplicity(0, 9999))
    }
)
refC15: BinaryAssociation = BinaryAssociation(
    name="refC15",
    ends={
        Property(name="traces_C", type=traces_A, multiplicity=Multiplicity(1, 1)),
        Property(name="traces_A16", type=traces_C, multiplicity=Multiplicity(0, 9999))
    }
)
refA17: BinaryAssociation = BinaryAssociation(
    name="refA17",
    ends={
        Property(name="traces_A19", type=traces_B, multiplicity=Multiplicity(1, 1)),
        Property(name="traces_B18", type=traces_A, multiplicity=Multiplicity(0, 1))
    }
)
refE20: BinaryAssociation = BinaryAssociation(
    name="refE20",
    ends={
        Property(name="traces_E22", type=traces_D, multiplicity=Multiplicity(1, 1)),
        Property(name="traces_D21", type=traces_E, multiplicity=Multiplicity(0, 9999))
    }
)
refD24: BinaryAssociation = BinaryAssociation(
    name="refD24",
    ends={
        Property(name="traces_D25", type=traces_D, multiplicity=Multiplicity(1, 1)),
        Property(name="traces_D23", type=traces_D, multiplicity=Multiplicity(0, 1))
    }
)
refD26: BinaryAssociation = BinaryAssociation(
    name="refD26",
    ends={
        Property(name="traces_D28", type=traces_E, multiplicity=Multiplicity(1, 1)),
        Property(name="traces_E27", type=traces_D, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_traces_R1_Trace_Trace = Generalization(general=Trace, specific=traces_R1_Trace)
gen_traces_R2_Trace_Trace = Generalization(general=Trace, specific=traces_R2_Trace)
gen_traces_A_RootIn = Generalization(general=RootIn, specific=traces_A)
gen_traces_B_RootIn = Generalization(general=RootIn, specific=traces_B)
gen_traces_C_RootIn = Generalization(general=RootIn, specific=traces_C)
gen_traces_D_RootOut = Generalization(general=RootOut, specific=traces_D)
gen_traces_E_RootOut = Generalization(general=RootOut, specific=traces_E)

# Domain Model
domain_model = DomainModel(
    name="traces",
    types={traces_RootOut, traces_R1_Trace, Trace, traces_A, traces_D, traces_R2_Trace, traces_B, traces_E, RootIn, traces_C, RootOut, traces_Trace, traces_RootIn},
    associations={from_0, to1, s3, t14, t26, s9, t10, refB12, refC15, refA17, refE20, refD24, refD26},
    generalizations={gen_traces_R1_Trace_Trace, gen_traces_R2_Trace_Trace, gen_traces_A_RootIn, gen_traces_B_RootIn, gen_traces_C_RootIn, gen_traces_D_RootOut, gen_traces_E_RootOut},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)