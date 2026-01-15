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
TimeUnit: Enumeration = Enumeration(
    name="TimeUnit",
    literals={
            EnumerationLiteral(name="NANOSECONDS"),
			EnumerationLiteral(name="MICROSECONDS"),
			EnumerationLiteral(name="MILLISECONDS"),
			EnumerationLiteral(name="SECONDS"),
			EnumerationLiteral(name="MINUTES"),
			EnumerationLiteral(name="HOURS"),
			EnumerationLiteral(name="DAYS")
    }
)

# Classes
MRPTrace_TraceModel = Class(name="MRPTrace::TraceModel")
MRPTrace_Trace = Class(name="MRPTrace::Trace")
NamedElement = Class(name="NamedElement")
MRPTrace_TraceEntry = Class(name="MRPTrace::TraceEntry")
MRPTrace_RDMElement = Class(name="MRPTrace::RDMElement")
MRPTrace_Event = Class(name="MRPTrace::Event")
MRPTrace_NamedElement = Class(name="MRPTrace::NamedElement", is_abstract=True)

# MRPTrace_TraceModel class attributes and methods

# MRPTrace_Trace class attributes and methods
MRPTrace_Trace_granularity: Property = Property(name="granularity", type=StringType)
MRPTrace_Trace.attributes={MRPTrace_Trace_granularity}

# NamedElement class attributes and methods

# MRPTrace_TraceEntry class attributes and methods
MRPTrace_TraceEntry_description: Property = Property(name="description", type=StringType)
MRPTrace_TraceEntry.attributes={MRPTrace_TraceEntry_description}

# MRPTrace_RDMElement class attributes and methods

# MRPTrace_Event class attributes and methods
MRPTrace_Event_time: Property = Property(name="time", type=StringType)
MRPTrace_Event.attributes={MRPTrace_Event_time}

# MRPTrace_NamedElement class attributes and methods
MRPTrace_NamedElement_name: Property = Property(name="name", type=StringType)
MRPTrace_NamedElement.attributes={MRPTrace_NamedElement_name}

# Relationships
trace0: BinaryAssociation = BinaryAssociation(
    name="trace0",
    ends={
        Property(name="MRPTrace_Trace", type=MRPTrace_TraceModel, multiplicity=Multiplicity(1, 1)),
        Property(name="MRPTrace_TraceModel", type=MRPTrace_Trace, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
consistsOf1: BinaryAssociation = BinaryAssociation(
    name="consistsOf1",
    ends={
        Property(name="MRPTrace_TraceEntry", type=MRPTrace_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="MRPTrace_Trace2", type=MRPTrace_TraceEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nextEntry4: BinaryAssociation = BinaryAssociation(
    name="nextEntry4",
    ends={
        Property(name="MRPTrace_TraceEntry5", type=MRPTrace_TraceEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="MRPTrace_TraceEntry3", type=MRPTrace_TraceEntry, multiplicity=Multiplicity(0, 1))
    }
)
affectedRDMElements6: BinaryAssociation = BinaryAssociation(
    name="affectedRDMElements6",
    ends={
        Property(name="MRPTrace_RDMElement", type=MRPTrace_TraceEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="MRPTrace_TraceEntry7", type=MRPTrace_RDMElement, multiplicity=Multiplicity(0, 9999))
    }
)
cause8: BinaryAssociation = BinaryAssociation(
    name="cause8",
    ends={
        Property(name="MRPTrace_Event", type=MRPTrace_TraceEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="MRPTrace_TraceEntry9", type=MRPTrace_Event, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_MRPTrace_Trace_NamedElement = Generalization(general=NamedElement, specific=MRPTrace_Trace)
gen_MRPTrace_Event_NamedElement = Generalization(general=NamedElement, specific=MRPTrace_Event)

# Domain Model
domain_model = DomainModel(
    name="MRPTrace",
    types={MRPTrace_TraceModel, MRPTrace_Trace, NamedElement, MRPTrace_TraceEntry, MRPTrace_RDMElement, MRPTrace_Event, MRPTrace_NamedElement, TimeUnit},
    associations={trace0, consistsOf1, nextEntry4, affectedRDMElements6, cause8},
    generalizations={gen_MRPTrace_Trace_NamedElement, gen_MRPTrace_Event_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)