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
Trace_Level = Class(name="Trace::Level")
Trace = Class(name="Trace")
Call = Class(name="Call")
Trace_Call = Class(name="Trace::Call")
Index = Class(name="Index")
Trace_Index = Class(name="Trace::Index")
Trace_Trace = Class(name="Trace::Trace")
Level = Class(name="Level")

# Trace_Level class attributes and methods

# Trace class attributes and methods

# Call class attributes and methods

# Trace_Call class attributes and methods
Trace_Call_methodName: Property = Property(name="methodName", type=StringType)
Trace_Call_DBAccessesNumber: Property = Property(name="DBAccessesNumber", type=StringType)
Trace_Call_DBRowsNumber: Property = Property(name="DBRowsNumber", type=StringType)
Trace_Call_CPUTime: Property = Property(name="CPUTime", type=StringType)
Trace_Call.attributes={Trace_Call_DBRowsNumber, Trace_Call_methodName, Trace_Call_CPUTime, Trace_Call_DBAccessesNumber}

# Index class attributes and methods

# Trace_Index class attributes and methods
Trace_Index_value: Property = Property(name="value", type=StringType)
Trace_Index.attributes={Trace_Index_value}

# Trace_Trace class attributes and methods
Trace_Trace_name: Property = Property(name="name", type=StringType)
Trace_Trace.attributes={Trace_Trace_name}

# Level class attributes and methods

# Relationships
trace1: BinaryAssociation = BinaryAssociation(
    name="trace1",
    ends={
        Property(name="#3", type=Trace_Level, multiplicity=Multiplicity(1, 1)),
        Property(name="02", type=Trace, multiplicity=Multiplicity(1, 1))
    }
)
calls4: BinaryAssociation = BinaryAssociation(
    name="calls4",
    ends={
        Property(name="#6", type=Trace_Level, multiplicity=Multiplicity(1, 1)),
        Property(name="05", type=Call, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
level7: BinaryAssociation = BinaryAssociation(
    name="level7",
    ends={
        Property(name="#9", type=Trace_Call, multiplicity=Multiplicity(1, 1)),
        Property(name="08", type=Level, multiplicity=Multiplicity(1, 1))
    }
)
indexes10: BinaryAssociation = BinaryAssociation(
    name="indexes10",
    ends={
        Property(name="Index", type=Trace_Call, multiplicity=Multiplicity(1, 1)),
        Property(name="Trace_Call", type=Index, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
levels0: BinaryAssociation = BinaryAssociation(
    name="levels0",
    ends={
        Property(name="#", type=Trace_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="0", type=Level, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="PrimitiveTypes",
    types={Trace_Level, Trace, Call, Trace_Call, Index, Trace_Index, Trace_Trace, Level},
    associations={trace1, calls4, level7, indexes10, levels0},
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