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

PrimitiveTypes: Enumeration = Enumeration(
    name="PrimitiveTypes",
    literals={
            EnumerationLiteral(name="boolean"),
			EnumerationLiteral(name="natural"),
			EnumerationLiteral(name="clock"),
			EnumerationLiteral(name="float"),
			EnumerationLiteral(name="integer")
    }
)

# Classes
remes_ConditionalConnector = Class(name="remes::ConditionalConnector")
remes_InitPoint = Class(name="remes::InitPoint")
remes_RemesDiagram = Class(name="remes::RemesDiagram")
remes_Mode = Class(name="remes::Mode", is_abstract=True)
remes_ControlPath = Class(name="remes::ControlPath", is_abstract=True)
remes_EntryPoint = Class(name="remes::EntryPoint")
remes_ExitPoint = Class(name="remes::ExitPoint")
ControlPath = Class(name="ControlPath")
remes_Variable = Class(name="remes::Variable")
remes_Resource = Class(name="remes::Resource")
remes_Constant = Class(name="remes::Constant")
remes_CompositeMode = Class(name="remes::CompositeMode")
Mode = Class(name="Mode")
remes_SubMode = Class(name="remes::SubMode")
remes_CompositeEntryPoint = Class(name="remes::CompositeEntryPoint")
remes_CompositeExitPoint = Class(name="remes::CompositeExitPoint")
remes_WritePoint = Class(name="remes::WritePoint")
LogicalRoot = Class(name="LogicalRoot")
remes_Point = Class(name="remes::Point", is_abstract=True)
Point = Class(name="Point")
remes_InitEdge = Class(name="remes::InitEdge")
remes_Edge = Class(name="remes::Edge")
ExitPoint = Class(name="ExitPoint")
EntryPoint = Class(name="EntryPoint")
remes_Referable = Class(name="remes::Referable", is_abstract=True)
Referable = Class(name="Referable")
ActionRoot = Class(name="ActionRoot")
ResourceRoot = Class(name="ResourceRoot")
remes_WriteEdge = Class(name="remes::WriteEdge")

# remes_ConditionalConnector class attributes and methods

# remes_InitPoint class attributes and methods

# remes_RemesDiagram class attributes and methods

# remes_Mode class attributes and methods
remes_Mode_initialization: Property = Property(name="initialization", type=StringType)
remes_Mode_m_findVariableByName: Method = Method(name="findVariableByName", parameters={Parameter(name='name')}, type=StringType)
remes_Mode_m_findResourceByName: Method = Method(name="findResourceByName", parameters={Parameter(name='name')}, type=StringType)
remes_Mode_m_findConstantByName: Method = Method(name="findConstantByName", parameters={Parameter(name='name')}, type=StringType)
remes_Mode.attributes={remes_Mode_initialization}
remes_Mode.methods={remes_Mode_m_findVariableByName, remes_Mode_m_findResourceByName, remes_Mode_m_findConstantByName}

# remes_ControlPath class attributes and methods
remes_ControlPath_name: Property = Property(name="name", type=StringType)
remes_ControlPath.attributes={remes_ControlPath_name}

# remes_EntryPoint class attributes and methods

# remes_ExitPoint class attributes and methods

# ControlPath class attributes and methods

# remes_Variable class attributes and methods
remes_Variable_value: Property = Property(name="value", type=StringType)
remes_Variable_type: Property = Property(name="type", type=StringType)
remes_Variable_vectorSize: Property = Property(name="vectorSize", type=IntegerType)
remes_Variable_global: Property = Property(name="global", type=BooleanType)
remes_Variable_readable: Property = Property(name="readable", type=BooleanType)
remes_Variable_writable: Property = Property(name="writable", type=BooleanType)
remes_Variable.attributes={remes_Variable_type, remes_Variable_vectorSize, remes_Variable_global, remes_Variable_writable, remes_Variable_readable, remes_Variable_value}

# remes_Resource class attributes and methods
remes_Resource_expression: Property = Property(name="expression", type=StringType)
remes_Resource_type: Property = Property(name="type", type=StringType)
remes_Resource.attributes={remes_Resource_type, remes_Resource_expression}

# remes_Constant class attributes and methods
remes_Constant_type: Property = Property(name="type", type=StringType)
remes_Constant_value: Property = Property(name="value", type=StringType)
remes_Constant_global: Property = Property(name="global", type=BooleanType)
remes_Constant.attributes={remes_Constant_value, remes_Constant_global, remes_Constant_type}

# remes_CompositeMode class attributes and methods

# Mode class attributes and methods

# remes_SubMode class attributes and methods
remes_SubMode_invariant: Property = Property(name="invariant", type=StringType)
remes_SubMode_isUrgent: Property = Property(name="isUrgent", type=BooleanType)
remes_SubMode.attributes={remes_SubMode_isUrgent, remes_SubMode_invariant}

# remes_CompositeEntryPoint class attributes and methods

# remes_CompositeExitPoint class attributes and methods

# remes_WritePoint class attributes and methods

# LogicalRoot class attributes and methods

# remes_Point class attributes and methods

# Point class attributes and methods

# remes_InitEdge class attributes and methods
remes_InitEdge_initialization: Property = Property(name="initialization", type=StringType)
remes_InitEdge.attributes={remes_InitEdge_initialization}

# remes_Edge class attributes and methods
remes_Edge_actionGuard: Property = Property(name="actionGuard", type=StringType)
remes_Edge_actionBody: Property = Property(name="actionBody", type=StringType)
remes_Edge.attributes={remes_Edge_actionBody, remes_Edge_actionGuard}

# ExitPoint class attributes and methods

# EntryPoint class attributes and methods

# remes_Referable class attributes and methods
remes_Referable_name: Property = Property(name="name", type=StringType)
remes_Referable.attributes={remes_Referable_name}

# Referable class attributes and methods

# ActionRoot class attributes and methods

# ResourceRoot class attributes and methods

# remes_WriteEdge class attributes and methods

# Relationships
conditionalConnectors10: BinaryAssociation = BinaryAssociation(
    name="conditionalConnectors10",
    ends={
        Property(name="ConditionalConnector", type=remes_CompositeMode, multiplicity=Multiplicity(1, 1)),
        Property(name="parent11", type=remes_ConditionalConnector, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
modes0: BinaryAssociation = BinaryAssociation(
    name="modes0",
    ends={
        Property(name="remes_Mode", type=remes_RemesDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="remes_RemesDiagram", type=remes_Mode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entryPoint1: BinaryAssociation = BinaryAssociation(
    name="entryPoint1",
    ends={
        Property(name="EntryPoint", type=remes_ControlPath, multiplicity=Multiplicity(1, 1)),
        Property(name="container", type=remes_EntryPoint, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
exitPoint2: BinaryAssociation = BinaryAssociation(
    name="exitPoint2",
    ends={
        Property(name="ExitPoint", type=remes_ControlPath, multiplicity=Multiplicity(1, 1)),
        Property(name="container3", type=remes_ExitPoint, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variables4: BinaryAssociation = BinaryAssociation(
    name="variables4",
    ends={
        Property(name="Variable", type=remes_Mode, multiplicity=Multiplicity(1, 1)),
        Property(name="scope", type=remes_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resources5: BinaryAssociation = BinaryAssociation(
    name="resources5",
    ends={
        Property(name="Resource", type=remes_Mode, multiplicity=Multiplicity(1, 1)),
        Property(name="scope6", type=remes_Resource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
constants7: BinaryAssociation = BinaryAssociation(
    name="constants7",
    ends={
        Property(name="Constant", type=remes_Mode, multiplicity=Multiplicity(1, 1)),
        Property(name="scope8", type=remes_Constant, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subModes9: BinaryAssociation = BinaryAssociation(
    name="subModes9",
    ends={
        Property(name="SubMode", type=remes_CompositeMode, multiplicity=Multiplicity(1, 1)),
        Property(name="parent", type=remes_SubMode, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
initPoint12: BinaryAssociation = BinaryAssociation(
    name="initPoint12",
    ends={
        Property(name="InitPoint", type=remes_CompositeMode, multiplicity=Multiplicity(1, 1)),
        Property(name="container13", type=remes_InitPoint, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
compositeEntryPoint14: BinaryAssociation = BinaryAssociation(
    name="compositeEntryPoint14",
    ends={
        Property(name="CompositeEntryPoint", type=remes_CompositeMode, multiplicity=Multiplicity(1, 1)),
        Property(name="composite", type=remes_CompositeEntryPoint, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
compositeExitPoint15: BinaryAssociation = BinaryAssociation(
    name="compositeExitPoint15",
    ends={
        Property(name="CompositeExitPoint", type=remes_CompositeMode, multiplicity=Multiplicity(1, 1)),
        Property(name="composite16", type=remes_CompositeExitPoint, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
writePoint17: BinaryAssociation = BinaryAssociation(
    name="writePoint17",
    ends={
        Property(name="WritePoint", type=remes_CompositeMode, multiplicity=Multiplicity(1, 1)),
        Property(name="container18", type=remes_WritePoint, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parent19: BinaryAssociation = BinaryAssociation(
    name="parent19",
    ends={
        Property(name="CompositeMode", type=remes_SubMode, multiplicity=Multiplicity(1, 1)),
        Property(name="subModes", type=remes_CompositeMode, multiplicity=Multiplicity(0, 1))
    }
)
parsedInvariant20: BinaryAssociation = BinaryAssociation(
    name="parsedInvariant20",
    ends={
        Property(name="LogicalRoot", type=remes_SubMode, multiplicity=Multiplicity(1, 1)),
        Property(name="remes_SubMode", type=LogicalRoot, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parent21: BinaryAssociation = BinaryAssociation(
    name="parent21",
    ends={
        Property(name="CompositeMode22", type=remes_ConditionalConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="conditionalConnectors", type=remes_CompositeMode, multiplicity=Multiplicity(0, 1))
    }
)
initEdge23: BinaryAssociation = BinaryAssociation(
    name="initEdge23",
    ends={
        Property(name="InitEdge", type=remes_InitPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="connectFrom", type=remes_InitEdge, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
composite35: BinaryAssociation = BinaryAssociation(
    name="composite35",
    ends={
        Property(name="CompositeMode36", type=remes_CompositeExitPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="compositeExitPoint", type=remes_CompositeMode, multiplicity=Multiplicity(0, 1))
    }
)
container24: BinaryAssociation = BinaryAssociation(
    name="container24",
    ends={
        Property(name="CompositeMode25", type=remes_InitPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="initPoint", type=remes_CompositeMode, multiplicity=Multiplicity(1, 1))
    }
)
entryEdges26: BinaryAssociation = BinaryAssociation(
    name="entryEdges26",
    ends={
        Property(name="Edge", type=remes_EntryPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="connectTo", type=remes_Edge, multiplicity=Multiplicity(0, 9999))
    }
)
container27: BinaryAssociation = BinaryAssociation(
    name="container27",
    ends={
        Property(name="ControlPath", type=remes_EntryPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="entryPoint", type=remes_ControlPath, multiplicity=Multiplicity(0, 1))
    }
)
exitEdges28: BinaryAssociation = BinaryAssociation(
    name="exitEdges28",
    ends={
        Property(name="Edge30", type=remes_ExitPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="connectFrom29", type=remes_Edge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
container31: BinaryAssociation = BinaryAssociation(
    name="container31",
    ends={
        Property(name="ControlPath32", type=remes_ExitPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="exitPoint", type=remes_ControlPath, multiplicity=Multiplicity(0, 1))
    }
)
composite33: BinaryAssociation = BinaryAssociation(
    name="composite33",
    ends={
        Property(name="CompositeMode34", type=remes_CompositeEntryPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="compositeEntryPoint", type=remes_CompositeMode, multiplicity=Multiplicity(0, 1))
    }
)
parsedInitialization48: BinaryAssociation = BinaryAssociation(
    name="parsedInitialization48",
    ends={
        Property(name="remes_InitEdge49", type=ActionRoot, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="ActionRoot50", type=remes_InitEdge, multiplicity=Multiplicity(1, 1))
    }
)
parsedActionGuard37: BinaryAssociation = BinaryAssociation(
    name="parsedActionGuard37",
    ends={
        Property(name="LogicalRoot38", type=remes_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="remes_Edge", type=LogicalRoot, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
connectFrom39: BinaryAssociation = BinaryAssociation(
    name="connectFrom39",
    ends={
        Property(name="ExitPoint40", type=remes_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="exitEdges", type=remes_ExitPoint, multiplicity=Multiplicity(1, 1))
    }
)
connectTo41: BinaryAssociation = BinaryAssociation(
    name="connectTo41",
    ends={
        Property(name="EntryPoint42", type=remes_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="entryEdges", type=remes_EntryPoint, multiplicity=Multiplicity(1, 1))
    }
)
parsedActionBody43: BinaryAssociation = BinaryAssociation(
    name="parsedActionBody43",
    ends={
        Property(name="ActionRoot", type=remes_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="remes_Edge44", type=ActionRoot, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
connectFrom45: BinaryAssociation = BinaryAssociation(
    name="connectFrom45",
    ends={
        Property(name="InitPoint46", type=remes_InitEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="initEdge", type=remes_InitPoint, multiplicity=Multiplicity(1, 1))
    }
)
connectTo47: BinaryAssociation = BinaryAssociation(
    name="connectTo47",
    ends={
        Property(name="remes_EntryPoint", type=remes_InitEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="remes_InitEdge", type=remes_EntryPoint, multiplicity=Multiplicity(1, 1))
    }
)
scope51: BinaryAssociation = BinaryAssociation(
    name="scope51",
    ends={
        Property(name="Mode", type=remes_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="variables", type=remes_Mode, multiplicity=Multiplicity(1, 1))
    }
)
scope52: BinaryAssociation = BinaryAssociation(
    name="scope52",
    ends={
        Property(name="Mode53", type=remes_Resource, multiplicity=Multiplicity(1, 1)),
        Property(name="resources", type=remes_Mode, multiplicity=Multiplicity(1, 1))
    }
)
parsedExpression54: BinaryAssociation = BinaryAssociation(
    name="parsedExpression54",
    ends={
        Property(name="ResourceRoot", type=remes_Resource, multiplicity=Multiplicity(1, 1)),
        Property(name="remes_Resource", type=ResourceRoot, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
scope55: BinaryAssociation = BinaryAssociation(
    name="scope55",
    ends={
        Property(name="Mode56", type=remes_Constant, multiplicity=Multiplicity(1, 1)),
        Property(name="constants", type=remes_Mode, multiplicity=Multiplicity(1, 1))
    }
)
connectTo57: BinaryAssociation = BinaryAssociation(
    name="connectTo57",
    ends={
        Property(name="WritePoint58", type=remes_WriteEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="writeEdges", type=remes_WritePoint, multiplicity=Multiplicity(1, 1))
    }
)
connectFrom59: BinaryAssociation = BinaryAssociation(
    name="connectFrom59",
    ends={
        Property(name="remes_ExitPoint", type=remes_WriteEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="remes_WriteEdge", type=remes_ExitPoint, multiplicity=Multiplicity(1, 1))
    }
)
container60: BinaryAssociation = BinaryAssociation(
    name="container60",
    ends={
        Property(name="CompositeMode61", type=remes_WritePoint, multiplicity=Multiplicity(1, 1)),
        Property(name="writePoint", type=remes_CompositeMode, multiplicity=Multiplicity(1, 1))
    }
)
writeEdges62: BinaryAssociation = BinaryAssociation(
    name="writeEdges62",
    ends={
        Property(name="WriteEdge", type=remes_WritePoint, multiplicity=Multiplicity(1, 1)),
        Property(name="connectTo63", type=remes_WriteEdge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_remes_Mode_ControlPath = Generalization(general=ControlPath, specific=remes_Mode)
gen_remes_CompositeMode_Mode = Generalization(general=Mode, specific=remes_CompositeMode)
gen_remes_SubMode_Mode = Generalization(general=Mode, specific=remes_SubMode)
gen_remes_ConditionalConnector_ControlPath = Generalization(general=ControlPath, specific=remes_ConditionalConnector)
gen_remes_InitPoint_Point = Generalization(general=Point, specific=remes_InitPoint)
gen_remes_EntryPoint_Point = Generalization(general=Point, specific=remes_EntryPoint)
gen_remes_ExitPoint_Point = Generalization(general=Point, specific=remes_ExitPoint)
gen_remes_CompositeEntryPoint_ExitPoint = Generalization(general=ExitPoint, specific=remes_CompositeEntryPoint)
gen_remes_CompositeExitPoint_EntryPoint = Generalization(general=EntryPoint, specific=remes_CompositeExitPoint)
gen_remes_Variable_Referable = Generalization(general=Referable, specific=remes_Variable)
gen_remes_Resource_Referable = Generalization(general=Referable, specific=remes_Resource)
gen_remes_Constant_Referable = Generalization(general=Referable, specific=remes_Constant)
gen_remes_WritePoint_Point = Generalization(general=Point, specific=remes_WritePoint)

# Domain Model
domain_model = DomainModel(
    name="remes",
    types={remes_ConditionalConnector, remes_InitPoint, remes_RemesDiagram, remes_Mode, remes_ControlPath, remes_EntryPoint, remes_ExitPoint, ControlPath, remes_Variable, remes_Resource, remes_Constant, remes_CompositeMode, Mode, remes_SubMode, remes_CompositeEntryPoint, remes_CompositeExitPoint, remes_WritePoint, LogicalRoot, remes_Point, Point, remes_InitEdge, remes_Edge, ExitPoint, EntryPoint, remes_Referable, Referable, ActionRoot, ResourceRoot, remes_WriteEdge, ResourceTypes, PrimitiveTypes},
    associations={conditionalConnectors10, modes0, entryPoint1, exitPoint2, variables4, resources5, constants7, subModes9, initPoint12, compositeEntryPoint14, compositeExitPoint15, writePoint17, parent19, parsedInvariant20, parent21, initEdge23, composite35, container24, entryEdges26, container27, exitEdges28, container31, composite33, parsedInitialization48, parsedActionGuard37, connectFrom39, connectTo41, parsedActionBody43, connectFrom45, connectTo47, scope51, scope52, parsedExpression54, scope55, connectTo57, connectFrom59, container60, writeEdges62},
    generalizations={gen_remes_Mode_ControlPath, gen_remes_CompositeMode_Mode, gen_remes_SubMode_Mode, gen_remes_ConditionalConnector_ControlPath, gen_remes_InitPoint_Point, gen_remes_EntryPoint_Point, gen_remes_ExitPoint_Point, gen_remes_CompositeEntryPoint_ExitPoint, gen_remes_CompositeExitPoint_EntryPoint, gen_remes_Variable_Referable, gen_remes_Resource_Referable, gen_remes_Constant_Referable, gen_remes_WritePoint_Point},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)