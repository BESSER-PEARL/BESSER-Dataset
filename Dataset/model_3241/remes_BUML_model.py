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
remes_FromCompositeModeInitEdge = Class(name="remes::FromCompositeModeInitEdge", is_abstract=True)
remes_FromCompositeModeEdge = Class(name="remes::FromCompositeModeEdge", is_abstract=True)
remes_SubMode = Class(name="remes::SubMode")
remes_ConditionalConnector = Class(name="remes::ConditionalConnector")
remes_CompositeMode = Class(name="remes::CompositeMode")
Mode = Class(name="Mode")
remes_ToCompositeModeEdge = Class(name="remes::ToCompositeModeEdge", is_abstract=True)
remes_EntryConditionalSubEdge = Class(name="remes::EntryConditionalSubEdge")
FromConditionalConnectorEdge = Class(name="FromConditionalConnectorEdge")
ToSubModeEdge = Class(name="ToSubModeEdge")
Edge = Class(name="Edge")
remes_EntryConditionalTopEdge = Class(name="remes::EntryConditionalTopEdge")
FromCompositeModeEdge = Class(name="FromCompositeModeEdge")
ToConditionalConnectorEdge = Class(name="ToConditionalConnectorEdge")
remes_EntryConditionalTopInitEdge = Class(name="remes::EntryConditionalTopInitEdge")
FromCompositeModeInitEdge = Class(name="FromCompositeModeInitEdge")
InitEdge = Class(name="InitEdge")
remes_EntryEdge = Class(name="remes::EntryEdge")
remes_EntryInitEdge = Class(name="remes::EntryInitEdge")
remes_ExitConditionalSubEdge = Class(name="remes::ExitConditionalSubEdge")
FromSubModeEdge = Class(name="FromSubModeEdge")
remes_ToConditionalConnectorEdge = Class(name="remes::ToConditionalConnectorEdge", is_abstract=True)
remes_FromConditionalConnectorEdge = Class(name="remes::FromConditionalConnectorEdge", is_abstract=True)
remes_Edge = Class(name="remes::Edge", is_abstract=True)
remes_FromSubModeEdge = Class(name="remes::FromSubModeEdge", is_abstract=True)
remes_InitEdge = Class(name="remes::InitEdge", is_abstract=True)
remes_InternalEdge = Class(name="remes::InternalEdge")
remes_Mode = Class(name="remes::Mode", is_abstract=True)
remes_RemesDiagram = Class(name="remes::RemesDiagram")
remes_ExitConditionalTopEdge = Class(name="remes::ExitConditionalTopEdge")
ToCompositeModeEdge = Class(name="ToCompositeModeEdge")
remes_ExitEdge = Class(name="remes::ExitEdge")
remes_ToSubModeEdge = Class(name="remes::ToSubModeEdge", is_abstract=True)

# remes_FromCompositeModeInitEdge class attributes and methods

# remes_FromCompositeModeEdge class attributes and methods

# remes_SubMode class attributes and methods
remes_SubMode_resourceClassC: Property = Property(name="resourceClassC", type=StringType)
remes_SubMode_invariant: Property = Property(name="invariant", type=StringType)
remes_SubMode_isUrgent: Property = Property(name="isUrgent", type=StringType)
remes_SubMode_resourceClassA: Property = Property(name="resourceClassA", type=StringType)
remes_SubMode_resourceClassB: Property = Property(name="resourceClassB", type=StringType)
remes_SubMode.attributes={remes_SubMode_resourceClassC, remes_SubMode_resourceClassB, remes_SubMode_invariant, remes_SubMode_isUrgent, remes_SubMode_resourceClassA}

# remes_ConditionalConnector class attributes and methods
remes_ConditionalConnector_name: Property = Property(name="name", type=StringType)
remes_ConditionalConnector.attributes={remes_ConditionalConnector_name}

# remes_CompositeMode class attributes and methods

# Mode class attributes and methods

# remes_ToCompositeModeEdge class attributes and methods

# remes_EntryConditionalSubEdge class attributes and methods

# FromConditionalConnectorEdge class attributes and methods

# ToSubModeEdge class attributes and methods

# Edge class attributes and methods

# remes_EntryConditionalTopEdge class attributes and methods

# FromCompositeModeEdge class attributes and methods

# ToConditionalConnectorEdge class attributes and methods

# remes_EntryConditionalTopInitEdge class attributes and methods

# FromCompositeModeInitEdge class attributes and methods

# InitEdge class attributes and methods

# remes_EntryEdge class attributes and methods

# remes_EntryInitEdge class attributes and methods

# remes_ExitConditionalSubEdge class attributes and methods

# FromSubModeEdge class attributes and methods

# remes_ToConditionalConnectorEdge class attributes and methods

# remes_FromConditionalConnectorEdge class attributes and methods

# remes_Edge class attributes and methods
remes_Edge_actionGuard: Property = Property(name="actionGuard", type=StringType)
remes_Edge_actionBody: Property = Property(name="actionBody", type=StringType)
remes_Edge.attributes={remes_Edge_actionBody, remes_Edge_actionGuard}

# remes_FromSubModeEdge class attributes and methods

# remes_InitEdge class attributes and methods
remes_InitEdge_initialization: Property = Property(name="initialization", type=StringType)
remes_InitEdge.attributes={remes_InitEdge_initialization}

# remes_InternalEdge class attributes and methods

# remes_Mode class attributes and methods
remes_Mode_name: Property = Property(name="name", type=StringType)
remes_Mode_initialization: Property = Property(name="initialization", type=StringType)
remes_Mode.attributes={remes_Mode_initialization, remes_Mode_name}

# remes_RemesDiagram class attributes and methods

# remes_ExitConditionalTopEdge class attributes and methods

# ToCompositeModeEdge class attributes and methods

# remes_ExitEdge class attributes and methods

# remes_ToSubModeEdge class attributes and methods

# Relationships
exitEdges0: BinaryAssociation = BinaryAssociation(
    name="exitEdges0",
    ends={
        Property(name="ToCompositeModeEdge", type=remes_CompositeMode, multiplicity=Multiplicity(1, 1)),
        Property(name="connectTo", type=remes_ToCompositeModeEdge, multiplicity=Multiplicity(1, 9999))
    }
)
initEdge1: BinaryAssociation = BinaryAssociation(
    name="initEdge1",
    ends={
        Property(name="FromCompositeModeInitEdge", type=remes_CompositeMode, multiplicity=Multiplicity(1, 1)),
        Property(name="connectFrom", type=remes_FromCompositeModeInitEdge, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
entryEdge2: BinaryAssociation = BinaryAssociation(
    name="entryEdge2",
    ends={
        Property(name="FromCompositeModeEdge", type=remes_CompositeMode, multiplicity=Multiplicity(1, 1)),
        Property(name="connectFrom3", type=remes_FromCompositeModeEdge, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
subModes4: BinaryAssociation = BinaryAssociation(
    name="subModes4",
    ends={
        Property(name="SubMode", type=remes_CompositeMode, multiplicity=Multiplicity(1, 1)),
        Property(name="parent", type=remes_SubMode, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
conditionalConnectors5: BinaryAssociation = BinaryAssociation(
    name="conditionalConnectors5",
    ends={
        Property(name="ConditionalConnector", type=remes_CompositeMode, multiplicity=Multiplicity(1, 1)),
        Property(name="parent6", type=remes_ConditionalConnector, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entryEdges7: BinaryAssociation = BinaryAssociation(
    name="entryEdges7",
    ends={
        Property(name="ToConditionalConnectorEdge", type=remes_ConditionalConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="connectTo8", type=remes_ToConditionalConnectorEdge, multiplicity=Multiplicity(1, 9999))
    }
)
exitEdges9: BinaryAssociation = BinaryAssociation(
    name="exitEdges9",
    ends={
        Property(name="FromConditionalConnectorEdge", type=remes_ConditionalConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="connectFrom10", type=remes_FromConditionalConnectorEdge, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
parent11: BinaryAssociation = BinaryAssociation(
    name="parent11",
    ends={
        Property(name="CompositeMode", type=remes_ConditionalConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="conditionalConnectors", type=remes_CompositeMode, multiplicity=Multiplicity(0, 1))
    }
)
connectFrom16: BinaryAssociation = BinaryAssociation(
    name="connectFrom16",
    ends={
        Property(name="ConditionalConnector17", type=remes_FromConditionalConnectorEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="exitEdges", type=remes_ConditionalConnector, multiplicity=Multiplicity(0, 1))
    }
)
connectFrom18: BinaryAssociation = BinaryAssociation(
    name="connectFrom18",
    ends={
        Property(name="SubMode20", type=remes_FromSubModeEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="exitEdges19", type=remes_SubMode, multiplicity=Multiplicity(0, 1))
    }
)
connectFrom12: BinaryAssociation = BinaryAssociation(
    name="connectFrom12",
    ends={
        Property(name="CompositeMode13", type=remes_FromCompositeModeEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="entryEdge", type=remes_CompositeMode, multiplicity=Multiplicity(0, 1))
    }
)
connectFrom14: BinaryAssociation = BinaryAssociation(
    name="connectFrom14",
    ends={
        Property(name="CompositeMode15", type=remes_FromCompositeModeInitEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="initEdge", type=remes_CompositeMode, multiplicity=Multiplicity(0, 1))
    }
)
parent26: BinaryAssociation = BinaryAssociation(
    name="parent26",
    ends={
        Property(name="CompositeMode27", type=remes_SubMode, multiplicity=Multiplicity(1, 1)),
        Property(name="subModes", type=remes_CompositeMode, multiplicity=Multiplicity(0, 1))
    }
)
connectTo28: BinaryAssociation = BinaryAssociation(
    name="connectTo28",
    ends={
        Property(name="CompositeMode30", type=remes_ToCompositeModeEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="exitEdges29", type=remes_CompositeMode, multiplicity=Multiplicity(1, 1))
    }
)
connectTo31: BinaryAssociation = BinaryAssociation(
    name="connectTo31",
    ends={
        Property(name="ConditionalConnector32", type=remes_ToConditionalConnectorEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="entryEdges", type=remes_ConditionalConnector, multiplicity=Multiplicity(1, 1))
    }
)
connectTo33: BinaryAssociation = BinaryAssociation(
    name="connectTo33",
    ends={
        Property(name="SubMode35", type=remes_ToSubModeEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="entryEdges34", type=remes_SubMode, multiplicity=Multiplicity(1, 1))
    }
)
modes21: BinaryAssociation = BinaryAssociation(
    name="modes21",
    ends={
        Property(name="remes_Mode", type=remes_RemesDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="remes_RemesDiagram", type=remes_Mode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entryEdges22: BinaryAssociation = BinaryAssociation(
    name="entryEdges22",
    ends={
        Property(name="ToSubModeEdge", type=remes_SubMode, multiplicity=Multiplicity(1, 1)),
        Property(name="connectTo23", type=remes_ToSubModeEdge, multiplicity=Multiplicity(1, 9999))
    }
)
exitEdges24: BinaryAssociation = BinaryAssociation(
    name="exitEdges24",
    ends={
        Property(name="FromSubModeEdge", type=remes_SubMode, multiplicity=Multiplicity(1, 1)),
        Property(name="connectFrom25", type=remes_FromSubModeEdge, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)

# Generalizations
gen_remes_CompositeMode_Mode = Generalization(general=Mode, specific=remes_CompositeMode)
gen_remes_EntryConditionalSubEdge_FromConditionalConnectorEdge = Generalization(general=FromConditionalConnectorEdge, specific=remes_EntryConditionalSubEdge)
gen_remes_EntryConditionalSubEdge_ToSubModeEdge = Generalization(general=ToSubModeEdge, specific=remes_EntryConditionalSubEdge)
gen_remes_EntryConditionalSubEdge_Edge = Generalization(general=Edge, specific=remes_EntryConditionalSubEdge)
gen_remes_EntryConditionalTopEdge_FromCompositeModeEdge = Generalization(general=FromCompositeModeEdge, specific=remes_EntryConditionalTopEdge)
gen_remes_EntryConditionalTopEdge_ToConditionalConnectorEdge = Generalization(general=ToConditionalConnectorEdge, specific=remes_EntryConditionalTopEdge)
gen_remes_EntryConditionalTopEdge_Edge = Generalization(general=Edge, specific=remes_EntryConditionalTopEdge)
gen_remes_EntryConditionalTopInitEdge_FromCompositeModeInitEdge = Generalization(general=FromCompositeModeInitEdge, specific=remes_EntryConditionalTopInitEdge)
gen_remes_EntryConditionalTopInitEdge_ToConditionalConnectorEdge = Generalization(general=ToConditionalConnectorEdge, specific=remes_EntryConditionalTopInitEdge)
gen_remes_EntryConditionalTopInitEdge_InitEdge = Generalization(general=InitEdge, specific=remes_EntryConditionalTopInitEdge)
gen_remes_EntryEdge_FromCompositeModeEdge = Generalization(general=FromCompositeModeEdge, specific=remes_EntryEdge)
gen_remes_EntryEdge_ToSubModeEdge = Generalization(general=ToSubModeEdge, specific=remes_EntryEdge)
gen_remes_EntryEdge_Edge = Generalization(general=Edge, specific=remes_EntryEdge)
gen_remes_EntryInitEdge_FromCompositeModeInitEdge = Generalization(general=FromCompositeModeInitEdge, specific=remes_EntryInitEdge)
gen_remes_EntryInitEdge_ToSubModeEdge = Generalization(general=ToSubModeEdge, specific=remes_EntryInitEdge)
gen_remes_EntryInitEdge_InitEdge = Generalization(general=InitEdge, specific=remes_EntryInitEdge)
gen_remes_ExitConditionalSubEdge_FromSubModeEdge = Generalization(general=FromSubModeEdge, specific=remes_ExitConditionalSubEdge)
gen_remes_ExitConditionalSubEdge_ToConditionalConnectorEdge = Generalization(general=ToConditionalConnectorEdge, specific=remes_ExitConditionalSubEdge)
gen_remes_ExitConditionalSubEdge_Edge = Generalization(general=Edge, specific=remes_ExitConditionalSubEdge)
gen_remes_InternalEdge_FromSubModeEdge = Generalization(general=FromSubModeEdge, specific=remes_InternalEdge)
gen_remes_InternalEdge_ToSubModeEdge = Generalization(general=ToSubModeEdge, specific=remes_InternalEdge)
gen_remes_InternalEdge_Edge = Generalization(general=Edge, specific=remes_InternalEdge)
gen_remes_ExitConditionalTopEdge_FromConditionalConnectorEdge = Generalization(general=FromConditionalConnectorEdge, specific=remes_ExitConditionalTopEdge)
gen_remes_ExitConditionalTopEdge_ToCompositeModeEdge = Generalization(general=ToCompositeModeEdge, specific=remes_ExitConditionalTopEdge)
gen_remes_ExitConditionalTopEdge_Edge = Generalization(general=Edge, specific=remes_ExitConditionalTopEdge)
gen_remes_ExitEdge_FromSubModeEdge = Generalization(general=FromSubModeEdge, specific=remes_ExitEdge)
gen_remes_ExitEdge_ToCompositeModeEdge = Generalization(general=ToCompositeModeEdge, specific=remes_ExitEdge)
gen_remes_ExitEdge_Edge = Generalization(general=Edge, specific=remes_ExitEdge)
gen_remes_SubMode_Mode = Generalization(general=Mode, specific=remes_SubMode)

# Domain Model
domain_model = DomainModel(
    name="remes",
    types={remes_FromCompositeModeInitEdge, remes_FromCompositeModeEdge, remes_SubMode, remes_ConditionalConnector, remes_CompositeMode, Mode, remes_ToCompositeModeEdge, remes_EntryConditionalSubEdge, FromConditionalConnectorEdge, ToSubModeEdge, Edge, remes_EntryConditionalTopEdge, FromCompositeModeEdge, ToConditionalConnectorEdge, remes_EntryConditionalTopInitEdge, FromCompositeModeInitEdge, InitEdge, remes_EntryEdge, remes_EntryInitEdge, remes_ExitConditionalSubEdge, FromSubModeEdge, remes_ToConditionalConnectorEdge, remes_FromConditionalConnectorEdge, remes_Edge, remes_FromSubModeEdge, remes_InitEdge, remes_InternalEdge, remes_Mode, remes_RemesDiagram, remes_ExitConditionalTopEdge, ToCompositeModeEdge, remes_ExitEdge, remes_ToSubModeEdge},
    associations={exitEdges0, initEdge1, entryEdge2, subModes4, conditionalConnectors5, entryEdges7, exitEdges9, parent11, connectFrom16, connectFrom18, connectFrom12, connectFrom14, parent26, connectTo28, connectTo31, connectTo33, modes21, entryEdges22, exitEdges24},
    generalizations={gen_remes_CompositeMode_Mode, gen_remes_EntryConditionalSubEdge_FromConditionalConnectorEdge, gen_remes_EntryConditionalSubEdge_ToSubModeEdge, gen_remes_EntryConditionalSubEdge_Edge, gen_remes_EntryConditionalTopEdge_FromCompositeModeEdge, gen_remes_EntryConditionalTopEdge_ToConditionalConnectorEdge, gen_remes_EntryConditionalTopEdge_Edge, gen_remes_EntryConditionalTopInitEdge_FromCompositeModeInitEdge, gen_remes_EntryConditionalTopInitEdge_ToConditionalConnectorEdge, gen_remes_EntryConditionalTopInitEdge_InitEdge, gen_remes_EntryEdge_FromCompositeModeEdge, gen_remes_EntryEdge_ToSubModeEdge, gen_remes_EntryEdge_Edge, gen_remes_EntryInitEdge_FromCompositeModeInitEdge, gen_remes_EntryInitEdge_ToSubModeEdge, gen_remes_EntryInitEdge_InitEdge, gen_remes_ExitConditionalSubEdge_FromSubModeEdge, gen_remes_ExitConditionalSubEdge_ToConditionalConnectorEdge, gen_remes_ExitConditionalSubEdge_Edge, gen_remes_InternalEdge_FromSubModeEdge, gen_remes_InternalEdge_ToSubModeEdge, gen_remes_InternalEdge_Edge, gen_remes_ExitConditionalTopEdge_FromConditionalConnectorEdge, gen_remes_ExitConditionalTopEdge_ToCompositeModeEdge, gen_remes_ExitConditionalTopEdge_Edge, gen_remes_ExitEdge_FromSubModeEdge, gen_remes_ExitEdge_ToCompositeModeEdge, gen_remes_ExitEdge_Edge, gen_remes_SubMode_Mode},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)