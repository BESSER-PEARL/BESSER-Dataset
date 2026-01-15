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
LogLevel: Enumeration = Enumeration(
    name="LogLevel",
    literals={
            EnumerationLiteral(name="SEVERE"),
			EnumerationLiteral(name="WARNING"),
			EnumerationLiteral(name="INFO"),
			EnumerationLiteral(name="CONFIG"),
			EnumerationLiteral(name="FINE"),
			EnumerationLiteral(name="FINER"),
			EnumerationLiteral(name="FINEST")
    }
)

# Classes
trace_Exception = Class(name="trace::Exception")
trace_Trace = Class(name="trace::Trace")
trace_Log = Class(name="trace::Log")

# trace_Exception class attributes and methods
trace_Exception_message: Property = Property(name="message", type=StringType)
trace_Exception.attributes={trace_Exception_message}

# trace_Trace class attributes and methods

# trace_Log class attributes and methods
trace_Log_message: Property = Property(name="message", type=StringType)
trace_Log_source: Property = Property(name="source", type=StringType)
trace_Log_timestamp: Property = Property(name="timestamp", type=DateType)
trace_Log_level: Property = Property(name="level", type=StringType)
trace_Log.attributes={trace_Log_source, trace_Log_message, trace_Log_timestamp, trace_Log_level}

# Relationships
exceptions1: BinaryAssociation = BinaryAssociation(
    name="exceptions1",
    ends={
        Property(name="trace_Exception", type=trace_Log, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Log2", type=trace_Exception, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
logs0: BinaryAssociation = BinaryAssociation(
    name="logs0",
    ends={
        Property(name="trace_Log", type=trace_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Trace", type=trace_Log, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="trace",
    types={trace_Exception, trace_Trace, trace_Log, LogLevel},
    associations={exceptions1, logs0},
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