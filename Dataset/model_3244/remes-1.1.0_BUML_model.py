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
PrimitiveTypes: Enumeration = Enumeration(
    name="PrimitiveTypes",
    literals={
            EnumerationLiteral(name="boolean"),
			EnumerationLiteral(name="integer"),
			EnumerationLiteral(name="natural"),
			EnumerationLiteral(name="clock")
    }
)

ResourceTypes: Enumeration = Enumeration(
    name="ResourceTypes",
    literals={
            EnumerationLiteral(name="cpu"),
			EnumerationLiteral(name="memory"),
			EnumerationLiteral(name="bandwidth"),
			EnumerationLiteral(name="power"),
			EnumerationLiteral(name="port")
    }
)

# Classes
remes_CompositeMode = Class(name="remes::CompositeMode")
Mode = Class(name="Mode")
remes_ToCompositeModeEdge = Class(name="remes::ToCompositeModeEdge", is_abstract=True)
remes_FromCompositeModeInitEdge = Class(name="remes::FromCompositeModeInitEdge", is_abstract=True)
remes_FromConditionalConnectorEdge = Class(name="remes::FromConditionalConnectorEdge", is_abstract=True)
remes_Edge = Class(name="remes::Edge", is_abstract=True)
remes_EntryConditionalSubEdge = Class(name="remes::EntryConditionalSubEdge")
FromConditionalConnectorEdge = Class(name="FromConditionalConnectorEdge")
ToSubModeEdge = Class(name="ToSubModeEdge")
Edge = Class(name="Edge")
remes_EntryConditionalTopEdge = Class(name="remes::EntryConditionalTopEdge")
FromCompositeModeEdge = Class(name="FromCompositeModeEdge")
remes_FromCompositeModeEdge = Class(name="remes::FromCompositeModeEdge", is_abstract=True)
remes_SubMode = Class(name="remes::SubMode")
remes_ConditionalConnector = Class(name="remes::ConditionalConnector")
remes_ToConditionalConnectorEdge = Class(name="remes::ToConditionalConnectorEdge", is_abstract=True)
remes_ExitEdge = Class(name="remes::ExitEdge")
ToConditionalConnectorEdge = Class(name="ToConditionalConnectorEdge")
remes_EntryConditionalTopInitEdge = Class(name="remes::EntryConditionalTopInitEdge")
FromCompositeModeInitEdge = Class(name="FromCompositeModeInitEdge")
InitEdge = Class(name="InitEdge")
remes_EntryEdge = Class(name="remes::EntryEdge")
remes_EntryInitEdge = Class(name="remes::EntryInitEdge")
remes_ExitConditionalSubEdge = Class(name="remes::ExitConditionalSubEdge")
FromSubModeEdge = Class(name="FromSubModeEdge")
remes_ExitConditionalTopEdge = Class(name="remes::ExitConditionalTopEdge")
ToCompositeModeEdge = Class(name="ToCompositeModeEdge")
remes_RemesDiagram = Class(name="remes::RemesDiagram")
remes_ToSubModeEdge = Class(name="remes::ToSubModeEdge", is_abstract=True)
remes_FromSubModeEdge = Class(name="remes::FromSubModeEdge", is_abstract=True)
remes_InitEdge = Class(name="remes::InitEdge", is_abstract=True)
remes_InternalEdge = Class(name="remes::InternalEdge")
remes_Mode = Class(name="remes::Mode", is_abstract=True)
remes_Variable = Class(name="remes::Variable")
remes_Resource = Class(name="remes::Resource")

# remes_CompositeMode class attributes and methods

# Mode class attributes and methods

# remes_ToCompositeModeEdge class attributes and methods

# remes_FromCompositeModeInitEdge class attributes and methods

# remes_FromConditionalConnectorEdge class attributes and methods

# remes_Edge class attributes and methods
remes_Edge_actionGuard: Property = Property(name="actionGuard", type=StringType)
remes_Edge_actionBody: Property = Property(name="actionBody", type=StringType)
remes_Edge.attributes={remes_Edge_actionBody, remes_Edge_actionGuard}

# remes_EntryConditionalSubEdge class attributes and methods

# FromConditionalConnectorEdge class attributes and methods

# ToSubModeEdge class attributes and methods

# Edge class attributes and methods

# remes_EntryConditionalTopEdge class attributes and methods

# FromCompositeModeEdge class attributes and methods

# remes_FromCompositeModeEdge class attributes and methods

# remes_SubMode class attributes and methods
remes_SubMode_invariant: Property = Property(name="invariant", type=StringType)
remes_SubMode_isUrgent: Property = Property(name="isUrgent", type=BooleanType)
remes_SubMode.attributes={remes_SubMode_invariant, remes_SubMode_isUrgent}

# remes_ConditionalConnector class attributes and methods
remes_ConditionalConnector_name: Property = Property(name="name", type=StringType)
remes_ConditionalConnector.attributes={remes_ConditionalConnector_name}

# remes_ToConditionalConnectorEdge class attributes and methods

# remes_ExitEdge class attributes and methods

# ToConditionalConnectorEdge class attributes and methods

# remes_EntryConditionalTopInitEdge class attributes and methods

# FromCompositeModeInitEdge class attributes and methods

# InitEdge class attributes and methods

# remes_EntryEdge class attributes and methods

# remes_EntryInitEdge class attributes and methods

# remes_ExitConditionalSubEdge class attributes and methods

# FromSubModeEdge class attributes and methods

# remes_ExitConditionalTopEdge class attributes and methods

# ToCompositeModeEdge class attributes and methods

# remes_RemesDiagram class attributes and methods

# remes_ToSubModeEdge class attributes and methods

# remes_FromSubModeEdge class attributes and methods

# remes_InitEdge class attributes and methods
remes_InitEdge_initialization: Property = Property(name="initialization", type=StringType)
remes_InitEdge.attributes={remes_InitEdge_initialization}

# remes_InternalEdge class attributes and methods

# remes_Mode class attributes and methods
remes_Mode_name: Property = Property(name="name", type=StringType)
remes_Mode_initialization: Property = Property(name="initialization", type=StringType)
remes_Mode.attributes={remes_Mode_initialization, remes_Mode_name}

# remes_Variable class attributes and methods
remes_Variable_name: Property = Property(name="name", type=StringType)
remes_Variable_value: Property = Property(name="value", type=StringType)
remes_Variable_type: Property = Property(name="type", type=StringType)
remes_Variable_vectorSize: Property = Property(name="vectorSize", type=IntegerType)
remes_Variable_global: Property = Property(name="global", type=BooleanType)
remes_Variable_readable: Property = Property(name="readable", type=BooleanType)
remes_Variable_writable: Property = Property(name="writable", type=BooleanType)
remes_Variable.attributes={remes_Variable_readable, remes_Variable_type, remes_Variable_name, remes_Variable_global, remes_Variable_value, remes_Variable_vectorSize, remes_Variable_writable}

# remes_Resource class attributes and methods
remes_Resource_expression: Property = Property(name="expression", type=StringType)
remes_Resource_type: Property = Property(name="type", type=StringType)
remes_Resource.attributes={remes_Resource_type, remes_Resource_expression}

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
modes22: BinaryAssociation = BinaryAssociation(
    name="modes22",
    ends={
        Property(name="remes_Mode", type=remes_RemesDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="remes_RemesDiagram", type=remes_Mode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entryEdges23: BinaryAssociation = BinaryAssociation(
    name="entryEdges23",
    ends={
        Property(name="ToSubModeEdge", type=remes_SubMode, multiplicity=Multiplicity(1, 1)),
        Property(name="connectTo24", type=remes_ToSubModeEdge, multiplicity=Multiplicity(1, 9999))
    }
)
exitEdges25: BinaryAssociation = BinaryAssociation(
    name="exitEdges25",
    ends={
        Property(name="FromSubModeEdge", type=remes_SubMode, multiplicity=Multiplicity(1, 1)),
        Property(name="connectFrom26", type=remes_FromSubModeEdge, multiplicity=Multiplicity(1, 9999), is_composite=True)
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
variables21: BinaryAssociation = BinaryAssociation(
    name="variables21",
    ends={
        Property(name="Variable", type=remes_Mode, multiplicity=Multiplicity(1, 1)),
        Property(name="scope", type=remes_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
connectTo36: BinaryAssociation = BinaryAssociation(
    name="connectTo36",
    ends={
        Property(name="SubMode38", type=remes_ToSubModeEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="entryEdges37", type=remes_SubMode, multiplicity=Multiplicity(1, 1))
    }
)
scope39: BinaryAssociation = BinaryAssociation(
    name="scope39",
    ends={
        Property(name="Mode", type=remes_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="variables", type=remes_Mode, multiplicity=Multiplicity(1, 1))
    }
)
parent27: BinaryAssociation = BinaryAssociation(
    name="parent27",
    ends={
        Property(name="CompositeMode28", type=remes_SubMode, multiplicity=Multiplicity(1, 1)),
        Property(name="subModes", type=remes_CompositeMode, multiplicity=Multiplicity(0, 1))
    }
)
resources29: BinaryAssociation = BinaryAssociation(
    name="resources29",
    ends={
        Property(name="Resource", type=remes_SubMode, multiplicity=Multiplicity(1, 1)),
        Property(name="scope30", type=remes_Resource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
connectTo31: BinaryAssociation = BinaryAssociation(
    name="connectTo31",
    ends={
        Property(name="CompositeMode33", type=remes_ToCompositeModeEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="exitEdges32", type=remes_CompositeMode, multiplicity=Multiplicity(1, 1))
    }
)
connectTo34: BinaryAssociation = BinaryAssociation(
    name="connectTo34",
    ends={
        Property(name="ConditionalConnector35", type=remes_ToConditionalConnectorEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="entryEdges", type=remes_ConditionalConnector, multiplicity=Multiplicity(1, 1))
    }
)
scope40: BinaryAssociation = BinaryAssociation(
    name="scope40",
    ends={
        Property(name="resources", type=remes_SubMode, multiplicity=Multiplicity(1, 1)),
        Property(name="SubMode41", type=remes_Resource, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_remes_CompositeMode_Mode = Generalization(general=Mode, specific=remes_CompositeMode)
gen_remes_EntryConditionalSubEdge_FromConditionalConnectorEdge = Generalization(general=FromConditionalConnectorEdge, specific=remes_EntryConditionalSubEdge)
gen_remes_EntryConditionalSubEdge_ToSubModeEdge = Generalization(general=ToSubModeEdge, specific=remes_EntryConditionalSubEdge)
gen_remes_EntryConditionalSubEdge_Edge = Generalization(general=Edge, specific=remes_EntryConditionalSubEdge)
gen_remes_EntryConditionalTopEdge_FromCompositeModeEdge = Generalization(general=FromCompositeModeEdge, specific=remes_EntryConditionalTopEdge)
gen_remes_ExitEdge_FromSubModeEdge = Generalization(general=FromSubModeEdge, specific=remes_ExitEdge)
gen_remes_ExitEdge_ToCompositeModeEdge = Generalization(general=ToCompositeModeEdge, specific=remes_ExitEdge)
gen_remes_ExitEdge_Edge = Generalization(general=Edge, specific=remes_ExitEdge)
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
gen_remes_ExitConditionalTopEdge_FromConditionalConnectorEdge = Generalization(general=FromConditionalConnectorEdge, specific=remes_ExitConditionalTopEdge)
gen_remes_ExitConditionalTopEdge_ToCompositeModeEdge = Generalization(general=ToCompositeModeEdge, specific=remes_ExitConditionalTopEdge)
gen_remes_ExitConditionalTopEdge_Edge = Generalization(general=Edge, specific=remes_ExitConditionalTopEdge)
gen_remes_SubMode_Mode = Generalization(general=Mode, specific=remes_SubMode)
gen_remes_InternalEdge_FromSubModeEdge = Generalization(general=FromSubModeEdge, specific=remes_InternalEdge)
gen_remes_InternalEdge_ToSubModeEdge = Generalization(general=ToSubModeEdge, specific=remes_InternalEdge)
gen_remes_InternalEdge_Edge = Generalization(general=Edge, specific=remes_InternalEdge)

# Domain Model
domain_model = DomainModel(
    name="remes",
    types={remes_CompositeMode, Mode, remes_ToCompositeModeEdge, remes_FromCompositeModeInitEdge, remes_FromConditionalConnectorEdge, remes_Edge, remes_EntryConditionalSubEdge, FromConditionalConnectorEdge, ToSubModeEdge, Edge, remes_EntryConditionalTopEdge, FromCompositeModeEdge, remes_FromCompositeModeEdge, remes_SubMode, remes_ConditionalConnector, remes_ToConditionalConnectorEdge, remes_ExitEdge, ToConditionalConnectorEdge, remes_EntryConditionalTopInitEdge, FromCompositeModeInitEdge, InitEdge, remes_EntryEdge, remes_EntryInitEdge, remes_ExitConditionalSubEdge, FromSubModeEdge, remes_ExitConditionalTopEdge, ToCompositeModeEdge, remes_RemesDiagram, remes_ToSubModeEdge, remes_FromSubModeEdge, remes_InitEdge, remes_InternalEdge, remes_Mode, remes_Variable, remes_Resource, PrimitiveTypes, ResourceTypes},
    associations={exitEdges0, initEdge1, exitEdges9, parent11, entryEdge2, subModes4, conditionalConnectors5, entryEdges7, connectFrom12, connectFrom14, modes22, entryEdges23, exitEdges25, connectFrom16, connectFrom18, variables21, connectTo36, scope39, parent27, resources29, connectTo31, connectTo34, scope40},
    generalizations={gen_remes_CompositeMode_Mode, gen_remes_EntryConditionalSubEdge_FromConditionalConnectorEdge, gen_remes_EntryConditionalSubEdge_ToSubModeEdge, gen_remes_EntryConditionalSubEdge_Edge, gen_remes_EntryConditionalTopEdge_FromCompositeModeEdge, gen_remes_ExitEdge_FromSubModeEdge, gen_remes_ExitEdge_ToCompositeModeEdge, gen_remes_ExitEdge_Edge, gen_remes_EntryConditionalTopEdge_ToConditionalConnectorEdge, gen_remes_EntryConditionalTopEdge_Edge, gen_remes_EntryConditionalTopInitEdge_FromCompositeModeInitEdge, gen_remes_EntryConditionalTopInitEdge_ToConditionalConnectorEdge, gen_remes_EntryConditionalTopInitEdge_InitEdge, gen_remes_EntryEdge_FromCompositeModeEdge, gen_remes_EntryEdge_ToSubModeEdge, gen_remes_EntryEdge_Edge, gen_remes_EntryInitEdge_FromCompositeModeInitEdge, gen_remes_EntryInitEdge_ToSubModeEdge, gen_remes_EntryInitEdge_InitEdge, gen_remes_ExitConditionalSubEdge_FromSubModeEdge, gen_remes_ExitConditionalSubEdge_ToConditionalConnectorEdge, gen_remes_ExitConditionalSubEdge_Edge, gen_remes_ExitConditionalTopEdge_FromConditionalConnectorEdge, gen_remes_ExitConditionalTopEdge_ToCompositeModeEdge, gen_remes_ExitConditionalTopEdge_Edge, gen_remes_SubMode_Mode, gen_remes_InternalEdge_FromSubModeEdge, gen_remes_InternalEdge_ToSubModeEdge, gen_remes_InternalEdge_Edge},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)