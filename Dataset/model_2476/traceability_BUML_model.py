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
traceability_Trace = Class(name="traceability::Trace")
traceability_EObject = Class(name="traceability::EObject")
traceability_TraceComment = Class(name="traceability::TraceComment")
traceability_LogEntry = Class(name="traceability::LogEntry")
traceability_Traces = Class(name="traceability::Traces")
traceability_TraceDiff = Class(name="traceability::TraceDiff")
traceability_DiffCategory = Class(name="traceability::DiffCategory")
traceability_TraceDiffs = Class(name="traceability::TraceDiffs")
traceability_Category = Class(name="traceability::Category")

# traceability_Trace class attributes and methods
traceability_Trace_description: Property = Property(name="description", type=StringType)
traceability_Trace_value: Property = Property(name="value", type=StringType)
traceability_Trace_comment: Property = Property(name="comment", type=StringType)
traceability_Trace.attributes={traceability_Trace_value, traceability_Trace_description, traceability_Trace_comment}

# traceability_EObject class attributes and methods

# traceability_TraceComment class attributes and methods
traceability_TraceComment_comment: Property = Property(name="comment", type=StringType)
traceability_TraceComment_username: Property = Property(name="username", type=StringType)
traceability_TraceComment_date: Property = Property(name="date", type=DateType)
traceability_TraceComment_column: Property = Property(name="column", type=StringType)
traceability_TraceComment.attributes={traceability_TraceComment_username, traceability_TraceComment_date, traceability_TraceComment_comment, traceability_TraceComment_column}

# traceability_LogEntry class attributes and methods
traceability_LogEntry_message: Property = Property(name="message", type=StringType)
traceability_LogEntry_severity: Property = Property(name="severity", type=IntegerType)
traceability_LogEntry_messageType: Property = Property(name="messageType", type=IntegerType)
traceability_LogEntry_comment: Property = Property(name="comment", type=StringType)
traceability_LogEntry.attributes={traceability_LogEntry_severity, traceability_LogEntry_comment, traceability_LogEntry_messageType, traceability_LogEntry_message}

# traceability_Traces class attributes and methods
traceability_Traces_uriMap: Property = Property(name="uriMap", type=StringType)
traceability_Traces_originalSourceURL: Property = Property(name="originalSourceURL", type=StringType)
traceability_Traces_username: Property = Property(name="username", type=StringType)
traceability_Traces_fullName: Property = Property(name="fullName", type=StringType)
traceability_Traces_date: Property = Property(name="date", type=DateType)
traceability_Traces_location: Property = Property(name="location", type=StringType)
traceability_Traces_comments: Property = Property(name="comments", type=StringType)
traceability_Traces.attributes={traceability_Traces_uriMap, traceability_Traces_date, traceability_Traces_fullName, traceability_Traces_username, traceability_Traces_comments, traceability_Traces_location, traceability_Traces_originalSourceURL}

# traceability_TraceDiff class attributes and methods
traceability_TraceDiff_comment: Property = Property(name="comment", type=StringType)
traceability_TraceDiff.attributes={traceability_TraceDiff_comment}

# traceability_DiffCategory class attributes and methods
traceability_DiffCategory_name: Property = Property(name="name", type=StringType)
traceability_DiffCategory_modelIndex: Property = Property(name="modelIndex", type=IntegerType)
traceability_DiffCategory_unequal: Property = Property(name="unequal", type=BooleanType)
traceability_DiffCategory.attributes={traceability_DiffCategory_unequal, traceability_DiffCategory_modelIndex, traceability_DiffCategory_name}

# traceability_TraceDiffs class attributes and methods

# traceability_Category class attributes and methods
traceability_Category_name: Property = Property(name="name", type=StringType)
traceability_Category.attributes={traceability_Category_name}

# Relationships
participants11: BinaryAssociation = BinaryAssociation(
    name="participants11",
    ends={
        Property(name="traceability_EObject12", type=traceability_LogEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="traceability_LogEntry", type=traceability_EObject, multiplicity=Multiplicity(0, 9999))
    }
)
source0: BinaryAssociation = BinaryAssociation(
    name="source0",
    ends={
        Property(name="traceability_EObject", type=traceability_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="traceability_Trace", type=traceability_EObject, multiplicity=Multiplicity(0, 9999))
    }
)
target1: BinaryAssociation = BinaryAssociation(
    name="target1",
    ends={
        Property(name="traceability_EObject3", type=traceability_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="traceability_Trace2", type=traceability_EObject, multiplicity=Multiplicity(0, 9999))
    }
)
children5: BinaryAssociation = BinaryAssociation(
    name="children5",
    ends={
        Property(name="Trace", type=traceability_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="parent", type=traceability_Trace, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent7: BinaryAssociation = BinaryAssociation(
    name="parent7",
    ends={
        Property(name="Trace8", type=traceability_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="children", type=traceability_Trace, multiplicity=Multiplicity(0, 1))
    }
)
comments9: BinaryAssociation = BinaryAssociation(
    name="comments9",
    ends={
        Property(name="traceability_TraceComment", type=traceability_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="traceability_Trace10", type=traceability_TraceComment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
traces21: BinaryAssociation = BinaryAssociation(
    name="traces21",
    ends={
        Property(name="traceability_EObject23", type=traceability_Traces, multiplicity=Multiplicity(1, 1)),
        Property(name="traceability_Traces22", type=traceability_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
comments13: BinaryAssociation = BinaryAssociation(
    name="comments13",
    ends={
        Property(name="traceability_TraceComment15", type=traceability_LogEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="traceability_LogEntry14", type=traceability_TraceComment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sourceModel16: BinaryAssociation = BinaryAssociation(
    name="sourceModel16",
    ends={
        Property(name="traceability_EObject17", type=traceability_Traces, multiplicity=Multiplicity(1, 1)),
        Property(name="traceability_Traces", type=traceability_EObject, multiplicity=Multiplicity(0, 1))
    }
)
targetModel18: BinaryAssociation = BinaryAssociation(
    name="targetModel18",
    ends={
        Property(name="traceability_EObject20", type=traceability_Traces, multiplicity=Multiplicity(1, 1)),
        Property(name="traceability_Traces19", type=traceability_EObject, multiplicity=Multiplicity(0, 1))
    }
)
participants24: BinaryAssociation = BinaryAssociation(
    name="participants24",
    ends={
        Property(name="traceability_EObject25", type=traceability_TraceDiff, multiplicity=Multiplicity(1, 1)),
        Property(name="traceability_TraceDiff", type=traceability_EObject, multiplicity=Multiplicity(0, 9999))
    }
)
comments26: BinaryAssociation = BinaryAssociation(
    name="comments26",
    ends={
        Property(name="traceability_TraceComment28", type=traceability_TraceDiff, multiplicity=Multiplicity(1, 1)),
        Property(name="traceability_TraceDiff27", type=traceability_TraceComment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
diffs29: BinaryAssociation = BinaryAssociation(
    name="diffs29",
    ends={
        Property(name="traceability_TraceDiff30", type=traceability_DiffCategory, multiplicity=Multiplicity(1, 1)),
        Property(name="traceability_DiffCategory", type=traceability_TraceDiff, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
comparedTraces31: BinaryAssociation = BinaryAssociation(
    name="comparedTraces31",
    ends={
        Property(name="traceability_Traces32", type=traceability_TraceDiffs, multiplicity=Multiplicity(1, 1)),
        Property(name="traceability_TraceDiffs", type=traceability_Traces, multiplicity=Multiplicity(0, 9999))
    }
)
contents33: BinaryAssociation = BinaryAssociation(
    name="contents33",
    ends={
        Property(name="traceability_EObject34", type=traceability_Category, multiplicity=Multiplicity(1, 1)),
        Property(name="traceability_Category", type=traceability_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
narrowDown35: BinaryAssociation = BinaryAssociation(
    name="narrowDown35",
    ends={
        Property(name="traceability_EObject37", type=traceability_TraceComment, multiplicity=Multiplicity(1, 1)),
        Property(name="traceability_TraceComment36", type=traceability_EObject, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="traceability",
    types={traceability_Trace, traceability_EObject, traceability_TraceComment, traceability_LogEntry, traceability_Traces, traceability_TraceDiff, traceability_DiffCategory, traceability_TraceDiffs, traceability_Category},
    associations={participants11, source0, target1, children5, parent7, comments9, traces21, comments13, sourceModel16, targetModel18, participants24, comments26, diffs29, comparedTraces31, contents33, narrowDown35},
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