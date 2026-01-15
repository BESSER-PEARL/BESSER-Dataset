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
            EnumerationLiteral(name="integer"),
			EnumerationLiteral(name="boolean"),
			EnumerationLiteral(name="natural"),
			EnumerationLiteral(name="clock"),
			EnumerationLiteral(name="float"),
			EnumerationLiteral(name="string")
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
remes_RemesDiagram = Class(name="remes::RemesDiagram")
remes_Mode = Class(name="remes::Mode", is_abstract=True)
remes_ControlPath = Class(name="remes::ControlPath", is_abstract=True)
remes_EntryPoint = Class(name="remes::EntryPoint")
remes_ExitPoint = Class(name="remes::ExitPoint")
ControlPath = Class(name="ControlPath")
remes_ConditionalConnector = Class(name="remes::ConditionalConnector")
remes_Variable = Class(name="remes::Variable")
remes_Resource = Class(name="remes::Resource")
remes_Constant = Class(name="remes::Constant")
remes_CompositeMode = Class(name="remes::CompositeMode")
Mode = Class(name="Mode")
remes_SubMode = Class(name="remes::SubMode")
LogicalRoot = Class(name="LogicalRoot")
remes_InitPoint = Class(name="remes::InitPoint")
remes_CompositeEntryPoint = Class(name="remes::CompositeEntryPoint")
remes_CompositeExitPoint = Class(name="remes::CompositeExitPoint")
remes_WritePoint = Class(name="remes::WritePoint")
EntryPoint = Class(name="EntryPoint")
remes_Point = Class(name="remes::Point", is_abstract=True)
ExitPoint = Class(name="ExitPoint")
Point = Class(name="Point")
remes_Edge = Class(name="remes::Edge")
remes_Referable = Class(name="remes::Referable", is_abstract=True)
Referable = Class(name="Referable")
ActionRoot = Class(name="ActionRoot")
ResourceRoot = Class(name="ResourceRoot")

# remes_RemesDiagram class attributes and methods

# remes_Mode class attributes and methods
remes_Mode_m_findConstantByName: Method = Method(name="findConstantByName", parameters={Parameter(name='name')}, type=StringType)
remes_Mode_m_findVariableByName: Method = Method(name="findVariableByName", parameters={Parameter(name='name')}, type=StringType)
remes_Mode_m_findResourceByName: Method = Method(name="findResourceByName", parameters={Parameter(name='name')}, type=StringType)
remes_Mode.methods={remes_Mode_m_findResourceByName, remes_Mode_m_findVariableByName, remes_Mode_m_findConstantByName}

# remes_ControlPath class attributes and methods
remes_ControlPath_name: Property = Property(name="name", type=StringType)
remes_ControlPath.attributes={remes_ControlPath_name}

# remes_EntryPoint class attributes and methods

# remes_ExitPoint class attributes and methods

# ControlPath class attributes and methods

# remes_ConditionalConnector class attributes and methods

# remes_Variable class attributes and methods
remes_Variable_value: Property = Property(name="value", type=StringType)
remes_Variable_type: Property = Property(name="type", type=StringType)
remes_Variable_vectorSize: Property = Property(name="vectorSize", type=IntegerType)
remes_Variable_global: Property = Property(name="global", type=BooleanType)
remes_Variable_readable: Property = Property(name="readable", type=BooleanType)
remes_Variable_writable: Property = Property(name="writable", type=BooleanType)
remes_Variable.attributes={remes_Variable_value, remes_Variable_global, remes_Variable_writable, remes_Variable_vectorSize, remes_Variable_readable, remes_Variable_type}

# remes_Resource class attributes and methods
remes_Resource_expression: Property = Property(name="expression", type=StringType)
remes_Resource_type: Property = Property(name="type", type=StringType)
remes_Resource.attributes={remes_Resource_expression, remes_Resource_type}

# remes_Constant class attributes and methods
remes_Constant_value: Property = Property(name="value", type=StringType)
remes_Constant_global: Property = Property(name="global", type=BooleanType)
remes_Constant_type: Property = Property(name="type", type=StringType)
remes_Constant.attributes={remes_Constant_type, remes_Constant_value, remes_Constant_global}

# remes_CompositeMode class attributes and methods

# Mode class attributes and methods

# remes_SubMode class attributes and methods
remes_SubMode_invariant: Property = Property(name="invariant", type=StringType)
remes_SubMode_isUrgent: Property = Property(name="isUrgent", type=BooleanType)
remes_SubMode.attributes={remes_SubMode_invariant, remes_SubMode_isUrgent}

# LogicalRoot class attributes and methods

# remes_InitPoint class attributes and methods

# remes_CompositeEntryPoint class attributes and methods

# remes_CompositeExitPoint class attributes and methods

# remes_WritePoint class attributes and methods

# EntryPoint class attributes and methods

# remes_Point class attributes and methods

# ExitPoint class attributes and methods

# Point class attributes and methods

# remes_Edge class attributes and methods
remes_Edge_actionGuard: Property = Property(name="actionGuard", type=StringType)
remes_Edge_actionBody: Property = Property(name="actionBody", type=StringType)
remes_Edge.attributes={remes_Edge_actionGuard, remes_Edge_actionBody}

# remes_Referable class attributes and methods
remes_Referable_name: Property = Property(name="name", type=StringType)
remes_Referable.attributes={remes_Referable_name}

# Referable class attributes and methods

# ActionRoot class attributes and methods

# ResourceRoot class attributes and methods

# Relationships
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
parent18: BinaryAssociation = BinaryAssociation(
    name="parent18",
    ends={
        Property(name="subModes", type=remes_CompositeMode, multiplicity=Multiplicity(0, 1)),
        Property(name="CompositeMode", type=remes_SubMode, multiplicity=Multiplicity(1, 1))
    }
)
conditionalConnectors10: BinaryAssociation = BinaryAssociation(
    name="conditionalConnectors10",
    ends={
        Property(name="ConditionalConnector", type=remes_CompositeMode, multiplicity=Multiplicity(1, 1)),
        Property(name="parent11", type=remes_ConditionalConnector, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parsedInvariant19: BinaryAssociation = BinaryAssociation(
    name="parsedInvariant19",
    ends={
        Property(name="LogicalRoot", type=remes_SubMode, multiplicity=Multiplicity(1, 1)),
        Property(name="remes_SubMode", type=LogicalRoot, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initPoint12: BinaryAssociation = BinaryAssociation(
    name="initPoint12",
    ends={
        Property(name="remes_InitPoint", type=remes_CompositeMode, multiplicity=Multiplicity(1, 1)),
        Property(name="remes_CompositeMode", type=remes_InitPoint, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parent20: BinaryAssociation = BinaryAssociation(
    name="parent20",
    ends={
        Property(name="CompositeMode21", type=remes_ConditionalConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="conditionalConnectors", type=remes_CompositeMode, multiplicity=Multiplicity(0, 1))
    }
)
compositeEntryPoint13: BinaryAssociation = BinaryAssociation(
    name="compositeEntryPoint13",
    ends={
        Property(name="CompositeEntryPoint", type=remes_CompositeMode, multiplicity=Multiplicity(1, 1)),
        Property(name="composite", type=remes_CompositeEntryPoint, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
compositeExitPoint14: BinaryAssociation = BinaryAssociation(
    name="compositeExitPoint14",
    ends={
        Property(name="CompositeExitPoint", type=remes_CompositeMode, multiplicity=Multiplicity(1, 1)),
        Property(name="composite15", type=remes_CompositeExitPoint, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
writePoint16: BinaryAssociation = BinaryAssociation(
    name="writePoint16",
    ends={
        Property(name="remes_WritePoint", type=remes_CompositeMode, multiplicity=Multiplicity(1, 1)),
        Property(name="remes_CompositeMode17", type=remes_WritePoint, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
container26: BinaryAssociation = BinaryAssociation(
    name="container26",
    ends={
        Property(name="ControlPath27", type=remes_ExitPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="exitPoint", type=remes_ControlPath, multiplicity=Multiplicity(0, 1))
    }
)
composite28: BinaryAssociation = BinaryAssociation(
    name="composite28",
    ends={
        Property(name="CompositeMode29", type=remes_CompositeEntryPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="compositeEntryPoint", type=remes_CompositeMode, multiplicity=Multiplicity(0, 1))
    }
)
composite30: BinaryAssociation = BinaryAssociation(
    name="composite30",
    ends={
        Property(name="CompositeMode31", type=remes_CompositeExitPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="compositeExitPoint", type=remes_CompositeMode, multiplicity=Multiplicity(0, 1))
    }
)
entryEdges22: BinaryAssociation = BinaryAssociation(
    name="entryEdges22",
    ends={
        Property(name="Edge", type=remes_EntryPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="connectTo", type=remes_Edge, multiplicity=Multiplicity(0, 9999))
    }
)
container23: BinaryAssociation = BinaryAssociation(
    name="container23",
    ends={
        Property(name="ControlPath", type=remes_EntryPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="entryPoint", type=remes_ControlPath, multiplicity=Multiplicity(0, 1))
    }
)
exitEdges24: BinaryAssociation = BinaryAssociation(
    name="exitEdges24",
    ends={
        Property(name="Edge25", type=remes_ExitPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="connectFrom", type=remes_Edge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parsedActionBody38: BinaryAssociation = BinaryAssociation(
    name="parsedActionBody38",
    ends={
        Property(name="remes_Edge39", type=ActionRoot, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="ActionRoot", type=remes_Edge, multiplicity=Multiplicity(1, 1))
    }
)
scope40: BinaryAssociation = BinaryAssociation(
    name="scope40",
    ends={
        Property(name="Mode", type=remes_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="variables", type=remes_Mode, multiplicity=Multiplicity(1, 1))
    }
)
parsedActionGuard32: BinaryAssociation = BinaryAssociation(
    name="parsedActionGuard32",
    ends={
        Property(name="LogicalRoot33", type=remes_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="remes_Edge", type=LogicalRoot, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
connectFrom34: BinaryAssociation = BinaryAssociation(
    name="connectFrom34",
    ends={
        Property(name="ExitPoint35", type=remes_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="exitEdges", type=remes_ExitPoint, multiplicity=Multiplicity(1, 1))
    }
)
connectTo36: BinaryAssociation = BinaryAssociation(
    name="connectTo36",
    ends={
        Property(name="EntryPoint37", type=remes_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="entryEdges", type=remes_EntryPoint, multiplicity=Multiplicity(1, 1))
    }
)
scope44: BinaryAssociation = BinaryAssociation(
    name="scope44",
    ends={
        Property(name="Mode45", type=remes_Constant, multiplicity=Multiplicity(1, 1)),
        Property(name="constants", type=remes_Mode, multiplicity=Multiplicity(1, 1))
    }
)
scope41: BinaryAssociation = BinaryAssociation(
    name="scope41",
    ends={
        Property(name="Mode42", type=remes_Resource, multiplicity=Multiplicity(1, 1)),
        Property(name="resources", type=remes_Mode, multiplicity=Multiplicity(1, 1))
    }
)
parsedExpression43: BinaryAssociation = BinaryAssociation(
    name="parsedExpression43",
    ends={
        Property(name="ResourceRoot", type=remes_Resource, multiplicity=Multiplicity(1, 1)),
        Property(name="remes_Resource", type=ResourceRoot, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_remes_Mode_ControlPath = Generalization(general=ControlPath, specific=remes_Mode)
gen_remes_CompositeMode_Mode = Generalization(general=Mode, specific=remes_CompositeMode)
gen_remes_ConditionalConnector_ControlPath = Generalization(general=ControlPath, specific=remes_ConditionalConnector)
gen_remes_SubMode_Mode = Generalization(general=Mode, specific=remes_SubMode)
gen_remes_CompositeEntryPoint_ExitPoint = Generalization(general=ExitPoint, specific=remes_CompositeEntryPoint)
gen_remes_CompositeExitPoint_EntryPoint = Generalization(general=EntryPoint, specific=remes_CompositeExitPoint)
gen_remes_InitPoint_ExitPoint = Generalization(general=ExitPoint, specific=remes_InitPoint)
gen_remes_EntryPoint_Point = Generalization(general=Point, specific=remes_EntryPoint)
gen_remes_ExitPoint_Point = Generalization(general=Point, specific=remes_ExitPoint)
gen_remes_Variable_Referable = Generalization(general=Referable, specific=remes_Variable)
gen_remes_Resource_Referable = Generalization(general=Referable, specific=remes_Resource)
gen_remes_WritePoint_EntryPoint = Generalization(general=EntryPoint, specific=remes_WritePoint)
gen_remes_Constant_Referable = Generalization(general=Referable, specific=remes_Constant)

# Domain Model
domain_model = DomainModel(
    name="remes",
    types={remes_RemesDiagram, remes_Mode, remes_ControlPath, remes_EntryPoint, remes_ExitPoint, ControlPath, remes_ConditionalConnector, remes_Variable, remes_Resource, remes_Constant, remes_CompositeMode, Mode, remes_SubMode, LogicalRoot, remes_InitPoint, remes_CompositeEntryPoint, remes_CompositeExitPoint, remes_WritePoint, EntryPoint, remes_Point, ExitPoint, Point, remes_Edge, remes_Referable, Referable, ActionRoot, ResourceRoot, PrimitiveTypes, ResourceTypes},
    associations={modes0, entryPoint1, exitPoint2, variables4, resources5, constants7, subModes9, parent18, conditionalConnectors10, parsedInvariant19, initPoint12, parent20, compositeEntryPoint13, compositeExitPoint14, writePoint16, container26, composite28, composite30, entryEdges22, container23, exitEdges24, parsedActionBody38, scope40, parsedActionGuard32, connectFrom34, connectTo36, scope44, scope41, parsedExpression43},
    generalizations={gen_remes_Mode_ControlPath, gen_remes_CompositeMode_Mode, gen_remes_ConditionalConnector_ControlPath, gen_remes_SubMode_Mode, gen_remes_CompositeEntryPoint_ExitPoint, gen_remes_CompositeExitPoint_EntryPoint, gen_remes_InitPoint_ExitPoint, gen_remes_EntryPoint_Point, gen_remes_ExitPoint_Point, gen_remes_Variable_Referable, gen_remes_Resource_Referable, gen_remes_WritePoint_EntryPoint, gen_remes_Constant_Referable},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)