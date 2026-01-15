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
trace_TraceModel = Class(name="trace::TraceModel")
trace_GenNodeTrace = Class(name="trace::GenNodeTrace")
trace_GenChildNodeTrace = Class(name="trace::GenChildNodeTrace")
trace_GenLinkTrace = Class(name="trace::GenLinkTrace")
trace_ToolGroupTrace = Class(name="trace::ToolGroupTrace")
trace_AbstractTrace = Class(name="trace::AbstractTrace", is_abstract=True)
trace_MatchingTrace = Class(name="trace::MatchingTrace", is_abstract=True)
AbstractTrace = Class(name="AbstractTrace")
MatchingTrace = Class(name="MatchingTrace")
trace_GenNodeLabelTrace = Class(name="trace::GenNodeLabelTrace")
trace_GenCompartmentTrace = Class(name="trace::GenCompartmentTrace")
GenNodeTrace = Class(name="GenNodeTrace")
trace_GenLinkLabelTrace = Class(name="trace::GenLinkLabelTrace")

# trace_TraceModel class attributes and methods
trace_TraceModel_m_getNodeTrace: Method = Method(name="getNodeTrace", parameters={Parameter(name='visualID')}, type=StringType)
trace_TraceModel_m_getLinkTrace: Method = Method(name="getLinkTrace", parameters={Parameter(name='visualID')}, type=StringType)
trace_TraceModel_m_getAllAbstractTraces: Method = Method(name="getAllAbstractTraces", parameters={}, type=StringType)
trace_TraceModel_m_purgeUnprocessedTraces: Method = Method(name="purgeUnprocessedTraces", parameters={})
trace_TraceModel.methods={trace_TraceModel_m_getNodeTrace, trace_TraceModel_m_purgeUnprocessedTraces, trace_TraceModel_m_getLinkTrace, trace_TraceModel_m_getAllAbstractTraces}

# trace_GenNodeTrace class attributes and methods
trace_GenNodeTrace_m_setContext: Method = Method(name="setContext", parameters={Parameter(name='genNode')})
trace_GenNodeTrace.methods={trace_GenNodeTrace_m_setContext}

# trace_GenChildNodeTrace class attributes and methods

# trace_GenLinkTrace class attributes and methods
trace_GenLinkTrace_m_setContext: Method = Method(name="setContext", parameters={Parameter(name='genLink')})
trace_GenLinkTrace.methods={trace_GenLinkTrace_m_setContext}

# trace_ToolGroupTrace class attributes and methods
trace_ToolGroupTrace_m_setContext: Method = Method(name="setContext", parameters={Parameter(name='toolGroup')})
trace_ToolGroupTrace.methods={trace_ToolGroupTrace_m_setContext}

# trace_AbstractTrace class attributes and methods
trace_AbstractTrace_visualID: Property = Property(name="visualID", type=IntegerType)
trace_AbstractTrace_processed: Property = Property(name="processed", type=BooleanType)
trace_AbstractTrace.attributes={trace_AbstractTrace_processed, trace_AbstractTrace_visualID}

# trace_MatchingTrace class attributes and methods
trace_MatchingTrace_queryText: Property = Property(name="queryText", type=StringType)
trace_MatchingTrace_m_getQueryContext: Method = Method(name="getQueryContext", parameters={}, type=StringType)
trace_MatchingTrace_m_getEClassComparision: Method = Method(name="getEClassComparision", parameters={Parameter(name='eClass'), Parameter(name='varName')}, type=StringType)
trace_MatchingTrace_m_getEStructuralFeatureComparison: Method = Method(name="getEStructuralFeatureComparison", parameters={Parameter(name='varName'), Parameter(name='feature')}, type=StringType)
trace_MatchingTrace.attributes={trace_MatchingTrace_queryText}
trace_MatchingTrace.methods={trace_MatchingTrace_m_getEClassComparision, trace_MatchingTrace_m_getQueryContext, trace_MatchingTrace_m_getEStructuralFeatureComparison}

# AbstractTrace class attributes and methods

# MatchingTrace class attributes and methods

# trace_GenNodeLabelTrace class attributes and methods
trace_GenNodeLabelTrace_m_setContext: Method = Method(name="setContext", parameters={Parameter(name='genNodeLabel')})
trace_GenNodeLabelTrace.methods={trace_GenNodeLabelTrace_m_setContext}

# trace_GenCompartmentTrace class attributes and methods
trace_GenCompartmentTrace_m_setContext: Method = Method(name="setContext", parameters={Parameter(name='genCompartment')})
trace_GenCompartmentTrace.methods={trace_GenCompartmentTrace_m_setContext}

# GenNodeTrace class attributes and methods

# trace_GenLinkLabelTrace class attributes and methods
trace_GenLinkLabelTrace_m_setContext: Method = Method(name="setContext", parameters={Parameter(name='genLinkLabel')})
trace_GenLinkLabelTrace.methods={trace_GenLinkLabelTrace_m_setContext}

# Relationships
nodeTraces0: BinaryAssociation = BinaryAssociation(
    name="nodeTraces0",
    ends={
        Property(name="trace_GenNodeTrace", type=trace_TraceModel, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_TraceModel", type=trace_GenNodeTrace, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
childNodeTraces1: BinaryAssociation = BinaryAssociation(
    name="childNodeTraces1",
    ends={
        Property(name="trace_GenChildNodeTrace", type=trace_TraceModel, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_TraceModel2", type=trace_GenChildNodeTrace, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
linkTraces3: BinaryAssociation = BinaryAssociation(
    name="linkTraces3",
    ends={
        Property(name="trace_GenLinkTrace", type=trace_TraceModel, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_TraceModel4", type=trace_GenLinkTrace, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
toolGroupTraces5: BinaryAssociation = BinaryAssociation(
    name="toolGroupTraces5",
    ends={
        Property(name="trace_ToolGroupTrace", type=trace_TraceModel, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_TraceModel6", type=trace_ToolGroupTrace, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nodeLabelTraces7: BinaryAssociation = BinaryAssociation(
    name="nodeLabelTraces7",
    ends={
        Property(name="trace_GenNodeLabelTrace", type=trace_GenNodeTrace, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_GenNodeTrace8", type=trace_GenNodeLabelTrace, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
compartmentTraces9: BinaryAssociation = BinaryAssociation(
    name="compartmentTraces9",
    ends={
        Property(name="trace_GenCompartmentTrace", type=trace_GenNodeTrace, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_GenNodeTrace10", type=trace_GenCompartmentTrace, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
linkLabelTraces11: BinaryAssociation = BinaryAssociation(
    name="linkLabelTraces11",
    ends={
        Property(name="trace_GenLinkLabelTrace", type=trace_GenLinkTrace, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_GenLinkTrace12", type=trace_GenLinkLabelTrace, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_trace_MatchingTrace_AbstractTrace = Generalization(general=AbstractTrace, specific=trace_MatchingTrace)
gen_trace_GenNodeTrace_MatchingTrace = Generalization(general=MatchingTrace, specific=trace_GenNodeTrace)
gen_trace_GenChildNodeTrace_GenNodeTrace = Generalization(general=GenNodeTrace, specific=trace_GenChildNodeTrace)
gen_trace_GenNodeLabelTrace_MatchingTrace = Generalization(general=MatchingTrace, specific=trace_GenNodeLabelTrace)
gen_trace_GenLinkTrace_MatchingTrace = Generalization(general=MatchingTrace, specific=trace_GenLinkTrace)
gen_trace_GenCompartmentTrace_MatchingTrace = Generalization(general=MatchingTrace, specific=trace_GenCompartmentTrace)
gen_trace_GenLinkLabelTrace_MatchingTrace = Generalization(general=MatchingTrace, specific=trace_GenLinkLabelTrace)
gen_trace_ToolGroupTrace_MatchingTrace = Generalization(general=MatchingTrace, specific=trace_ToolGroupTrace)

# Domain Model
domain_model = DomainModel(
    name="trace",
    types={trace_TraceModel, trace_GenNodeTrace, trace_GenChildNodeTrace, trace_GenLinkTrace, trace_ToolGroupTrace, trace_AbstractTrace, trace_MatchingTrace, AbstractTrace, MatchingTrace, trace_GenNodeLabelTrace, trace_GenCompartmentTrace, GenNodeTrace, trace_GenLinkLabelTrace},
    associations={nodeTraces0, childNodeTraces1, linkTraces3, toolGroupTraces5, nodeLabelTraces7, compartmentTraces9, linkLabelTraces11},
    generalizations={gen_trace_MatchingTrace_AbstractTrace, gen_trace_GenNodeTrace_MatchingTrace, gen_trace_GenChildNodeTrace_GenNodeTrace, gen_trace_GenNodeLabelTrace_MatchingTrace, gen_trace_GenLinkTrace_MatchingTrace, gen_trace_GenCompartmentTrace_MatchingTrace, gen_trace_GenLinkLabelTrace_MatchingTrace, gen_trace_ToolGroupTrace_MatchingTrace},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)