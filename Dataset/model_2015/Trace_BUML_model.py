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
trace_DebugTraceRegion = Class(name="trace::DebugTraceRegion")
trace_DebugLocationData = Class(name="trace::DebugLocationData")

# trace_DebugTraceRegion class attributes and methods
trace_DebugTraceRegion_label: Property = Property(name="label", type=StringType)
trace_DebugTraceRegion_myOffset: Property = Property(name="myOffset", type=IntegerType)
trace_DebugTraceRegion_myLength: Property = Property(name="myLength", type=IntegerType)
trace_DebugTraceRegion_myLineNumber: Property = Property(name="myLineNumber", type=IntegerType)
trace_DebugTraceRegion_myEndLineNumber: Property = Property(name="myEndLineNumber", type=IntegerType)
trace_DebugTraceRegion_myEndOffset: Property = Property(name="myEndOffset", type=IntegerType)
trace_DebugTraceRegion_useForDebugging: Property = Property(name="useForDebugging", type=BooleanType)
trace_DebugTraceRegion.attributes={trace_DebugTraceRegion_useForDebugging, trace_DebugTraceRegion_myEndLineNumber, trace_DebugTraceRegion_myEndOffset, trace_DebugTraceRegion_label, trace_DebugTraceRegion_myLength, trace_DebugTraceRegion_myOffset, trace_DebugTraceRegion_myLineNumber}

# trace_DebugLocationData class attributes and methods
trace_DebugLocationData_label: Property = Property(name="label", type=StringType)
trace_DebugLocationData_offset: Property = Property(name="offset", type=IntegerType)
trace_DebugLocationData_length: Property = Property(name="length", type=IntegerType)
trace_DebugLocationData_lineNumber: Property = Property(name="lineNumber", type=IntegerType)
trace_DebugLocationData_endLineNumber: Property = Property(name="endLineNumber", type=IntegerType)
trace_DebugLocationData_path: Property = Property(name="path", type=StringType)
trace_DebugLocationData_endOffset: Property = Property(name="endOffset", type=IntegerType)
trace_DebugLocationData.attributes={trace_DebugLocationData_endOffset, trace_DebugLocationData_lineNumber, trace_DebugLocationData_endLineNumber, trace_DebugLocationData_label, trace_DebugLocationData_offset, trace_DebugLocationData_path, trace_DebugLocationData_length}

# Relationships
nestedRegions1: BinaryAssociation = BinaryAssociation(
    name="nestedRegions1",
    ends={
        Property(name="trace_DebugTraceRegion", type=trace_DebugTraceRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_DebugTraceRegion0", type=trace_DebugTraceRegion, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
associations2: BinaryAssociation = BinaryAssociation(
    name="associations2",
    ends={
        Property(name="trace_DebugLocationData", type=trace_DebugTraceRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_DebugTraceRegion3", type=trace_DebugLocationData, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="trace",
    types={trace_DebugTraceRegion, trace_DebugLocationData},
    associations={nestedRegions1, associations2},
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