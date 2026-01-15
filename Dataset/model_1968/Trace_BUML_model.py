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
trace_Trace = Class(name="trace::Trace")
trace_TraceList = Class(name="trace::TraceList")
trace_TraceBySource = Class(name="trace::TraceBySource")
trace_TraceItem = Class(name="trace::TraceItem", is_abstract=True)
trace_EObject = Class(name="trace::EObject")
trace_M2MTraceItem = Class(name="trace::M2MTraceItem")
TraceItem = Class(name="TraceItem")
trace_M2CTraceItem = Class(name="trace::M2CTraceItem")

# trace_Trace class attributes and methods

# trace_TraceList class attributes and methods

# trace_TraceBySource class attributes and methods

# trace_TraceItem class attributes and methods
trace_TraceItem_kind: Property = Property(name="kind", type=StringType)
trace_TraceItem.attributes={trace_TraceItem_kind}

# trace_EObject class attributes and methods

# trace_M2MTraceItem class attributes and methods

# TraceItem class attributes and methods

# trace_M2CTraceItem class attributes and methods
trace_M2CTraceItem_targetFile: Property = Property(name="targetFile", type=StringType)
trace_M2CTraceItem_token: Property = Property(name="token", type=StringType)
trace_M2CTraceItem.attributes={trace_M2CTraceItem_targetFile, trace_M2CTraceItem_token}

# Relationships
list0: BinaryAssociation = BinaryAssociation(
    name="list0",
    ends={
        Property(name="trace_TraceList", type=trace_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Trace", type=trace_TraceList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
traceBySource1: BinaryAssociation = BinaryAssociation(
    name="traceBySource1",
    ends={
        Property(name="trace_TraceBySource", type=trace_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Trace2", type=trace_TraceBySource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
items3: BinaryAssociation = BinaryAssociation(
    name="items3",
    ends={
        Property(name="trace_TraceItem", type=trace_TraceList, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_TraceList4", type=trace_TraceItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
from5: BinaryAssociation = BinaryAssociation(
    name="from5",
    ends={
        Property(name="trace_EObject", type=trace_TraceItem, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_TraceItem6", type=trace_EObject, multiplicity=Multiplicity(1, 9999))
    }
)
source7: BinaryAssociation = BinaryAssociation(
    name="source7",
    ends={
        Property(name="trace_EObject9", type=trace_TraceBySource, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_TraceBySource8", type=trace_EObject, multiplicity=Multiplicity(0, 1))
    }
)
items10: BinaryAssociation = BinaryAssociation(
    name="items10",
    ends={
        Property(name="trace_TraceItem12", type=trace_TraceBySource, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_TraceBySource11", type=trace_TraceItem, multiplicity=Multiplicity(0, 9999))
    }
)
to13: BinaryAssociation = BinaryAssociation(
    name="to13",
    ends={
        Property(name="trace_EObject14", type=trace_M2MTraceItem, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_M2MTraceItem", type=trace_EObject, multiplicity=Multiplicity(1, 9999))
    }
)

# Generalizations
gen_trace_M2MTraceItem_TraceItem = Generalization(general=TraceItem, specific=trace_M2MTraceItem)
gen_trace_M2CTraceItem_TraceItem = Generalization(general=TraceItem, specific=trace_M2CTraceItem)

# Domain Model
domain_model = DomainModel(
    name="trace",
    types={trace_Trace, trace_TraceList, trace_TraceBySource, trace_TraceItem, trace_EObject, trace_M2MTraceItem, TraceItem, trace_M2CTraceItem},
    associations={list0, traceBySource1, items3, from5, source7, items10, to13},
    generalizations={gen_trace_M2MTraceItem_TraceItem, gen_trace_M2CTraceItem_TraceItem},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)