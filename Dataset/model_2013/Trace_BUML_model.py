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
Trace_Level = Class(name="Trace_Level")
Trace = Class(name="Trace")
Trace_Trace = Class(name="Trace_Trace")
Level = Class(name="Level")
Call = Class(name="Call")
Trace_Call = Class(name="Trace_Call")
Index = Class(name="Index")
Trace_Index = Class(name="Trace_Index")

# Trace_Level class attributes and methods

# Trace class attributes and methods

# Trace_Trace class attributes and methods
Trace_Trace_name: Property = Property(name="name", type=StringType)
Trace_Trace.attributes={Trace_Trace_name}

# Level class attributes and methods

# Call class attributes and methods

# Trace_Call class attributes and methods
Trace_Call_methodName: Property = Property(name="methodName", type=StringType)
Trace_Call_DBAccessesNumber: Property = Property(name="DBAccessesNumber", type=StringType)
Trace_Call_DBRowsNumber: Property = Property(name="DBRowsNumber", type=StringType)
Trace_Call_CPUTime: Property = Property(name="CPUTime", type=StringType)
Trace_Call.attributes={Trace_Call_DBAccessesNumber, Trace_Call_CPUTime, Trace_Call_methodName, Trace_Call_DBRowsNumber}

# Index class attributes and methods

# Trace_Index class attributes and methods
Trace_Index_value: Property = Property(name="value", type=StringType)
Trace_Index.attributes={Trace_Index_value}

# Relationships
levels0: BinaryAssociation = BinaryAssociation(
    name="levels0",
    ends={
        Property(name="Level", type=Trace_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="trace", type=Level, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
trace1: BinaryAssociation = BinaryAssociation(
    name="trace1",
    ends={
        Property(name="Trace", type=Trace_Level, multiplicity=Multiplicity(1, 1)),
        Property(name="levels", type=Trace, multiplicity=Multiplicity(1, 1))
    }
)
calls2: BinaryAssociation = BinaryAssociation(
    name="calls2",
    ends={
        Property(name="Call", type=Trace_Level, multiplicity=Multiplicity(1, 1)),
        Property(name="level", type=Call, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
level3: BinaryAssociation = BinaryAssociation(
    name="level3",
    ends={
        Property(name="Level4", type=Trace_Call, multiplicity=Multiplicity(1, 1)),
        Property(name="calls", type=Level, multiplicity=Multiplicity(1, 1))
    }
)
indexes5: BinaryAssociation = BinaryAssociation(
    name="indexes5",
    ends={
        Property(name="Index", type=Trace_Call, multiplicity=Multiplicity(1, 1)),
        Property(name="Trace_Call", type=Index, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="PrimitiveTypes",
    types={Trace_Level, Trace, Trace_Trace, Level, Call, Trace_Call, Index, Trace_Index},
    associations={levels0, trace1, calls2, level3, indexes5},
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