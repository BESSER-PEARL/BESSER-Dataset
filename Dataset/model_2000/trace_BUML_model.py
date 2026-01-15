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
trace_TracedRule = Class(name="trace::TracedRule")
trace_SourceElement = Class(name="trace::SourceElement")
trace_SourceElementList = Class(name="trace::SourceElementList")
trace_TraceLink = Class(name="trace::TraceLink")
trace_TraceLinkSet = Class(name="trace::TraceLinkSet")
trace_TargetElement = Class(name="trace::TargetElement")
trace_TraceElement = Class(name="trace::TraceElement", is_abstract=True)
trace_EObject = Class(name="trace::EObject")
TraceElement = Class(name="TraceElement")

# trace_TracedRule class attributes and methods
trace_TracedRule_rule: Property = Property(name="rule", type=StringType)
trace_TracedRule_m_getUniqueSourceElement: Method = Method(name="getUniqueSourceElement", parameters={Parameter(name='sourceElement')}, type=StringType)
trace_TracedRule_m_getUniqueSourceElements: Method = Method(name="getUniqueSourceElements", parameters={Parameter(name='sourceElements')}, type=StringType)
trace_TracedRule.attributes={trace_TracedRule_rule}
trace_TracedRule.methods={trace_TracedRule_m_getUniqueSourceElements, trace_TracedRule_m_getUniqueSourceElement}

# trace_SourceElement class attributes and methods
trace_SourceElement_mapsToSelf: Property = Property(name="mapsToSelf", type=BooleanType)
trace_SourceElement.attributes={trace_SourceElement_mapsToSelf}

# trace_SourceElementList class attributes and methods
trace_SourceElementList_m_getSourceObjects: Method = Method(name="getSourceObjects", parameters={}, type=StringType)
trace_SourceElementList.methods={trace_SourceElementList_m_getSourceObjects}

# trace_TraceLink class attributes and methods
trace_TraceLink_overridden: Property = Property(name="overridden", type=BooleanType)
trace_TraceLink_m_getSourceElement: Method = Method(name="getSourceElement", parameters={Parameter(name='create'), Parameter(name='name')}, type=StringType)
trace_TraceLink_m_getTargetElement: Method = Method(name="getTargetElement", parameters={Parameter(name='name')}, type=StringType)
trace_TraceLink.attributes={trace_TraceLink_overridden}
trace_TraceLink.methods={trace_TraceLink_m_getTargetElement, trace_TraceLink_m_getSourceElement}

# trace_TraceLinkSet class attributes and methods
trace_TraceLinkSet_m_getDefaultSourceElement: Method = Method(name="getDefaultSourceElement", parameters={Parameter(name='sourceElement')}, type=StringType)
trace_TraceLinkSet_m_getDefaultSourceElements: Method = Method(name="getDefaultSourceElements", parameters={Parameter(name='sourceElements')}, type=StringType)
trace_TraceLinkSet_m_getLinksByRule: Method = Method(name="getLinksByRule", parameters={Parameter(name='rule'), Parameter(name='create')}, type=StringType)
trace_TraceLinkSet_m_clear: Method = Method(name="clear", parameters={})
trace_TraceLinkSet.methods={trace_TraceLinkSet_m_getLinksByRule, trace_TraceLinkSet_m_getDefaultSourceElements, trace_TraceLinkSet_m_getDefaultSourceElement, trace_TraceLinkSet_m_clear}

# trace_TargetElement class attributes and methods

# trace_TraceElement class attributes and methods
trace_TraceElement_name: Property = Property(name="name", type=StringType)
trace_TraceElement_runtimeObject: Property = Property(name="runtimeObject", type=StringType)
trace_TraceElement.attributes={trace_TraceElement_runtimeObject, trace_TraceElement_name}

# trace_EObject class attributes and methods

# TraceElement class attributes and methods

# Relationships
rules0: BinaryAssociation = BinaryAssociation(
    name="rules0",
    ends={
        Property(name="TracedRule", type=trace_TraceLinkSet, multiplicity=Multiplicity(1, 1)),
        Property(name="linkSet", type=trace_TracedRule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
defaultSourceElements1: BinaryAssociation = BinaryAssociation(
    name="defaultSourceElements1",
    ends={
        Property(name="SourceElement", type=trace_TraceLinkSet, multiplicity=Multiplicity(1, 1)),
        Property(name="defaultFor", type=trace_SourceElement, multiplicity=Multiplicity(0, 9999))
    }
)
defaultSourceElementLists2: BinaryAssociation = BinaryAssociation(
    name="defaultSourceElementLists2",
    ends={
        Property(name="SourceElementList", type=trace_TraceLinkSet, multiplicity=Multiplicity(1, 1)),
        Property(name="defaultFor3", type=trace_SourceElementList, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
links4: BinaryAssociation = BinaryAssociation(
    name="links4",
    ends={
        Property(name="TraceLink", type=trace_TracedRule, multiplicity=Multiplicity(1, 1)),
        Property(name="rule", type=trace_TraceLink, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
linkSet5: BinaryAssociation = BinaryAssociation(
    name="linkSet5",
    ends={
        Property(name="TraceLinkSet", type=trace_TracedRule, multiplicity=Multiplicity(1, 1)),
        Property(name="rules", type=trace_TraceLinkSet, multiplicity=Multiplicity(0, 1))
    }
)
uniqueSourceElements6: BinaryAssociation = BinaryAssociation(
    name="uniqueSourceElements6",
    ends={
        Property(name="SourceElement7", type=trace_TracedRule, multiplicity=Multiplicity(1, 1)),
        Property(name="uniqueFor", type=trace_SourceElement, multiplicity=Multiplicity(0, 9999))
    }
)
uniqueSourceElementLists8: BinaryAssociation = BinaryAssociation(
    name="uniqueSourceElementLists8",
    ends={
        Property(name="SourceElementList10", type=trace_TracedRule, multiplicity=Multiplicity(1, 1)),
        Property(name="uniqueFor9", type=trace_SourceElementList, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sourceOf17: BinaryAssociation = BinaryAssociation(
    name="sourceOf17",
    ends={
        Property(name="TraceLink18", type=trace_SourceElement, multiplicity=Multiplicity(1, 1)),
        Property(name="sourceElements", type=trace_TraceLink, multiplicity=Multiplicity(0, 1))
    }
)
mapsTo19: BinaryAssociation = BinaryAssociation(
    name="mapsTo19",
    ends={
        Property(name="TargetElement20", type=trace_SourceElement, multiplicity=Multiplicity(1, 1)),
        Property(name="mapsTo", type=trace_TargetElement, multiplicity=Multiplicity(0, 9999))
    }
)
defaultFor21: BinaryAssociation = BinaryAssociation(
    name="defaultFor21",
    ends={
        Property(name="TraceLinkSet22", type=trace_SourceElement, multiplicity=Multiplicity(1, 1)),
        Property(name="defaultSourceElements", type=trace_TraceLinkSet, multiplicity=Multiplicity(0, 1))
    }
)
uniqueFor23: BinaryAssociation = BinaryAssociation(
    name="uniqueFor23",
    ends={
        Property(name="TracedRule24", type=trace_SourceElement, multiplicity=Multiplicity(1, 1)),
        Property(name="uniqueSourceElements", type=trace_TracedRule, multiplicity=Multiplicity(0, 1))
    }
)
targetOf25: BinaryAssociation = BinaryAssociation(
    name="targetOf25",
    ends={
        Property(name="TraceLink26", type=trace_TargetElement, multiplicity=Multiplicity(1, 1)),
        Property(name="targetElements", type=trace_TraceLink, multiplicity=Multiplicity(0, 1))
    }
)
mapsTo27: BinaryAssociation = BinaryAssociation(
    name="mapsTo27",
    ends={
        Property(name="SourceElement29", type=trace_TargetElement, multiplicity=Multiplicity(1, 1)),
        Property(name="mapsTo28", type=trace_SourceElement, multiplicity=Multiplicity(0, 9999))
    }
)
sourceElements30: BinaryAssociation = BinaryAssociation(
    name="sourceElements30",
    ends={
        Property(name="trace_SourceElement", type=trace_SourceElementList, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_SourceElementList", type=trace_SourceElement, multiplicity=Multiplicity(2, 9999))
    }
)
defaultFor31: BinaryAssociation = BinaryAssociation(
    name="defaultFor31",
    ends={
        Property(name="TraceLinkSet32", type=trace_SourceElementList, multiplicity=Multiplicity(1, 1)),
        Property(name="defaultSourceElementLists", type=trace_TraceLinkSet, multiplicity=Multiplicity(0, 1))
    }
)
uniqueFor33: BinaryAssociation = BinaryAssociation(
    name="uniqueFor33",
    ends={
        Property(name="TracedRule34", type=trace_SourceElementList, multiplicity=Multiplicity(1, 1)),
        Property(name="uniqueSourceElementLists", type=trace_TracedRule, multiplicity=Multiplicity(0, 1))
    }
)
sourceElements11: BinaryAssociation = BinaryAssociation(
    name="sourceElements11",
    ends={
        Property(name="SourceElement12", type=trace_TraceLink, multiplicity=Multiplicity(1, 1)),
        Property(name="sourceOf", type=trace_SourceElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
targetElements13: BinaryAssociation = BinaryAssociation(
    name="targetElements13",
    ends={
        Property(name="TargetElement", type=trace_TraceLink, multiplicity=Multiplicity(1, 1)),
        Property(name="targetOf", type=trace_TargetElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rule14: BinaryAssociation = BinaryAssociation(
    name="rule14",
    ends={
        Property(name="TracedRule15", type=trace_TraceLink, multiplicity=Multiplicity(1, 1)),
        Property(name="links", type=trace_TracedRule, multiplicity=Multiplicity(0, 1))
    }
)
object16: BinaryAssociation = BinaryAssociation(
    name="object16",
    ends={
        Property(name="trace_EObject", type=trace_TraceElement, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_TraceElement", type=trace_EObject, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_trace_TargetElement_TraceElement = Generalization(general=TraceElement, specific=trace_TargetElement)
gen_trace_SourceElement_TraceElement = Generalization(general=TraceElement, specific=trace_SourceElement)

# Domain Model
domain_model = DomainModel(
    name="trace",
    types={trace_TracedRule, trace_SourceElement, trace_SourceElementList, trace_TraceLink, trace_TraceLinkSet, trace_TargetElement, trace_TraceElement, trace_EObject, TraceElement},
    associations={rules0, defaultSourceElements1, defaultSourceElementLists2, links4, linkSet5, uniqueSourceElements6, uniqueSourceElementLists8, sourceOf17, mapsTo19, defaultFor21, uniqueFor23, targetOf25, mapsTo27, sourceElements30, defaultFor31, uniqueFor33, sourceElements11, targetElements13, rule14, object16},
    generalizations={gen_trace_TargetElement_TraceElement, gen_trace_SourceElement_TraceElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)