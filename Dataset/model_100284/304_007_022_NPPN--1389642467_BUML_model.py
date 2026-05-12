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
org_k1s_nppn_Arc = Class(name="org_k1s_nppn_Arc")
HasGraphics = Class(name="HasGraphics")
HLArcAddin = Class(name="HLArcAddin")
nppn_Node = Class(name="nppn_Node")
org_k1s_nppn_HasLabel = Class(name="org_k1s_nppn_HasLabel", is_abstract=True)
nppn_Label = Class(name="nppn_Label")
org_k1s_nppn_HasName = Class(name="org_k1s_nppn_HasName", is_abstract=True)
nppn_Name = Class(name="nppn_Name")
nppn_Page = Class(name="nppn_Page")
org_k1s_nppn_Instance = Class(name="org_k1s_nppn_Instance")
org_k1s_nppn_HLAnnotation = Class(name="org_k1s_nppn_HLAnnotation")
Node = Class(name="Node")
org_k1s_nppn_HLArcAddin = Class(name="org_k1s_nppn_HLArcAddin", is_abstract=True)
nppn_HLAnnotation = Class(name="nppn_HLAnnotation")
nppn_HasLabel = Class(name="nppn_HasLabel")
org_k1s_nppn_Name = Class(name="org_k1s_nppn_Name")
HLAnnotation = Class(name="HLAnnotation")
org_k1s_nppn_Node = Class(name="org_k1s_nppn_Node", is_abstract=True)
Object = Class(name="Object")
nppn_Arc = Class(name="nppn_Arc")
nppn_Pragmatic = Class(name="nppn_Pragmatic")
org_k1s_nppn_Label = Class(name="org_k1s_nppn_Label", is_abstract=True)
HasLabel = Class(name="HasLabel")
HasName = Class(name="HasName")
org_k1s_nppn_Page = Class(name="org_k1s_nppn_Page")
nppn_PetriNet = Class(name="nppn_PetriNet")
nppn_Object = Class(name="nppn_Object")
org_k1s_nppn_Object = Class(name="org_k1s_nppn_Object", is_abstract=True)
org_k1s_nppn_PetriNet = Class(name="org_k1s_nppn_PetriNet")
nppn_Monitor = Class(name="nppn_Monitor")
org_k1s_nppn_Place = Class(name="org_k1s_nppn_Place")
PlaceNode = Class(name="PlaceNode")
nppn_RefPlace = Class(name="nppn_RefPlace")
org_k1s_nppn_RefPlace = Class(name="org_k1s_nppn_RefPlace")
nppn_Place = Class(name="nppn_Place")
org_k1s_nppn_RefTrans = Class(name="org_k1s_nppn_RefTrans")
TransitionNode = Class(name="TransitionNode")
nppn_TransitionNode = Class(name="nppn_TransitionNode")
org_k1s_nppn_Transition = Class(name="org_k1s_nppn_Transition")
org_k1s_nppn_TransitionNode = Class(name="org_k1s_nppn_TransitionNode", is_abstract=True)
org_k1s_nppn_Pragmatic = Class(name="org_k1s_nppn_Pragmatic")
org_k1s_nppn_PlaceNode = Class(name="org_k1s_nppn_PlaceNode", is_abstract=True)
org_k1s_nppn_Derived = Class(name="org_k1s_nppn_Derived")
Pragmatic = Class(name="Pragmatic")
nppn_PNPattern = Class(name="nppn_PNPattern")
org_k1s_nppn_Explicit = Class(name="org_k1s_nppn_Explicit")
org_k1s_nppn_PNPattern = Class(name="org_k1s_nppn_PNPattern")
nppn_PlacementConstraints = Class(name="nppn_PlacementConstraints")
org_k1s_nppn_CustomDerivedPragmatics = Class(name="org_k1s_nppn_CustomDerivedPragmatics")
Derived = Class(name="Derived")
CustomPragmatics = Class(name="CustomPragmatics")
Explicit = Class(name="Explicit")
org_k1s_nppn_CustomPragmatics = Class(name="org_k1s_nppn_CustomPragmatics")
org_k1s_nppn_CustomExplicitPragmatics = Class(name="org_k1s_nppn_CustomExplicitPragmatics")
org_k1s_nppn_AbstractTemplateTree = Class(name="org_k1s_nppn_AbstractTemplateTree")
nppn_Principal = Class(name="nppn_Principal")
org_k1s_nppn_PlacementConstraints = Class(name="org_k1s_nppn_PlacementConstraints")
org_k1s_nppn_Principal = Class(name="org_k1s_nppn_Principal")
nppn_Instance = Class(name="nppn_Instance")
nppn_Service = Class(name="nppn_Service")
org_k1s_nppn_Service = Class(name="org_k1s_nppn_Service")
nppn_Block = Class(name="nppn_Block")
org_k1s_nppn_Block = Class(name="org_k1s_nppn_Block")
nppn_PlaceNode = Class(name="nppn_PlaceNode")
nppn_Transition = Class(name="nppn_Transition")
org_k1s_nppn_Container = Class(name="org_k1s_nppn_Container")
org_k1s_nppn_Binding = Class(name="org_k1s_nppn_Binding")
org_k1s_nppn_Atomic = Class(name="org_k1s_nppn_Atomic")
Block = Class(name="Block")
org_k1s_nppn_Loop = Class(name="org_k1s_nppn_Loop")
Container = Class(name="Container")
org_k1s_nppn_Conditional = Class(name="org_k1s_nppn_Conditional")
org_k1s_nppn_Conditinoal = Class(name="org_k1s_nppn_Conditinoal")
org_k1s_nppn_Bindings = Class(name="org_k1s_nppn_Bindings")
nppn_Binding = Class(name="nppn_Binding")

# org_k1s_nppn_Arc class attributes and methods

# HasGraphics class attributes and methods

# HLArcAddin class attributes and methods

# nppn_Node class attributes and methods

# org_k1s_nppn_HasLabel class attributes and methods

# nppn_Label class attributes and methods

# org_k1s_nppn_HasName class attributes and methods

# nppn_Name class attributes and methods

# nppn_Page class attributes and methods

# org_k1s_nppn_Instance class attributes and methods
org_k1s_nppn_Instance_subPageID: Property = Property(name="subPageID", type=StringType)
org_k1s_nppn_Instance.attributes={org_k1s_nppn_Instance_subPageID}

# org_k1s_nppn_HLAnnotation class attributes and methods

# Node class attributes and methods

# org_k1s_nppn_HLArcAddin class attributes and methods
org_k1s_nppn_HLArcAddin_kind: Property = Property(name="kind", type=StringType)
org_k1s_nppn_HLArcAddin.attributes={org_k1s_nppn_HLArcAddin_kind}

# nppn_HLAnnotation class attributes and methods

# nppn_HasLabel class attributes and methods

# org_k1s_nppn_Name class attributes and methods

# HLAnnotation class attributes and methods

# org_k1s_nppn_Node class attributes and methods

# Object class attributes and methods

# nppn_Arc class attributes and methods

# nppn_Pragmatic class attributes and methods

# org_k1s_nppn_Label class attributes and methods
org_k1s_nppn_Label_m_asString: Method = Method(name="asString", parameters={}, type=StringType)
org_k1s_nppn_Label.methods={org_k1s_nppn_Label_m_asString}

# HasLabel class attributes and methods

# HasName class attributes and methods

# org_k1s_nppn_Page class attributes and methods

# nppn_PetriNet class attributes and methods

# nppn_Object class attributes and methods

# org_k1s_nppn_Object class attributes and methods

# org_k1s_nppn_PetriNet class attributes and methods
org_k1s_nppn_PetriNet_kind: Property = Property(name="kind", type=StringType)
org_k1s_nppn_PetriNet_timeType: Property = Property(name="timeType", type=StringType)
org_k1s_nppn_PetriNet.attributes={org_k1s_nppn_PetriNet_kind, org_k1s_nppn_PetriNet_timeType}

# nppn_Monitor class attributes and methods

# org_k1s_nppn_Place class attributes and methods

# PlaceNode class attributes and methods

# nppn_RefPlace class attributes and methods

# org_k1s_nppn_RefPlace class attributes and methods

# nppn_Place class attributes and methods

# org_k1s_nppn_RefTrans class attributes and methods

# TransitionNode class attributes and methods

# nppn_TransitionNode class attributes and methods

# org_k1s_nppn_Transition class attributes and methods

# org_k1s_nppn_TransitionNode class attributes and methods

# org_k1s_nppn_Pragmatic class attributes and methods
org_k1s_nppn_Pragmatic_name: Property = Property(name="name", type=StringType)
org_k1s_nppn_Pragmatic.attributes={org_k1s_nppn_Pragmatic_name}

# org_k1s_nppn_PlaceNode class attributes and methods

# org_k1s_nppn_Derived class attributes and methods

# Pragmatic class attributes and methods

# nppn_PNPattern class attributes and methods

# org_k1s_nppn_Explicit class attributes and methods

# org_k1s_nppn_PNPattern class attributes and methods

# nppn_PlacementConstraints class attributes and methods

# org_k1s_nppn_CustomDerivedPragmatics class attributes and methods

# Derived class attributes and methods

# CustomPragmatics class attributes and methods

# Explicit class attributes and methods

# org_k1s_nppn_CustomPragmatics class attributes and methods

# org_k1s_nppn_CustomExplicitPragmatics class attributes and methods

# org_k1s_nppn_AbstractTemplateTree class attributes and methods

# nppn_Principal class attributes and methods

# org_k1s_nppn_PlacementConstraints class attributes and methods

# org_k1s_nppn_Principal class attributes and methods

# nppn_Instance class attributes and methods

# nppn_Service class attributes and methods

# org_k1s_nppn_Service class attributes and methods

# nppn_Block class attributes and methods

# org_k1s_nppn_Block class attributes and methods

# nppn_PlaceNode class attributes and methods

# nppn_Transition class attributes and methods

# org_k1s_nppn_Container class attributes and methods

# org_k1s_nppn_Binding class attributes and methods
org_k1s_nppn_Binding_template: Property = Property(name="template", type=StringType)
org_k1s_nppn_Binding.attributes={org_k1s_nppn_Binding_template}

# org_k1s_nppn_Atomic class attributes and methods

# Block class attributes and methods

# org_k1s_nppn_Loop class attributes and methods

# Container class attributes and methods

# org_k1s_nppn_Conditional class attributes and methods

# org_k1s_nppn_Conditinoal class attributes and methods

# org_k1s_nppn_Bindings class attributes and methods

# nppn_Binding class attributes and methods

# Relationships
source0: BinaryAssociation = BinaryAssociation(
    name="source0",
    ends={
        Property(name="Node", type=org_k1s_nppn_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="sourceArc", type=nppn_Node, multiplicity=Multiplicity(1, 1))
    }
)
target1: BinaryAssociation = BinaryAssociation(
    name="target1",
    ends={
        Property(name="Node2", type=org_k1s_nppn_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="targetArc", type=nppn_Node, multiplicity=Multiplicity(1, 1))
    }
)
label5: BinaryAssociation = BinaryAssociation(
    name="label5",
    ends={
        Property(name="Label", type=org_k1s_nppn_HasLabel, multiplicity=Multiplicity(1, 1)),
        Property(name="parent", type=nppn_Label, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name6: BinaryAssociation = BinaryAssociation(
    name="name6",
    ends={
        Property(name="nppn_Name", type=org_k1s_nppn_HasName, multiplicity=Multiplicity(1, 1)),
        Property(name="org_k1s_nppn_HasName", type=nppn_Name, multiplicity=Multiplicity(0, 1))
    }
)
page3: BinaryAssociation = BinaryAssociation(
    name="page3",
    ends={
        Property(name="Page", type=org_k1s_nppn_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="arc", type=nppn_Page, multiplicity=Multiplicity(1, 1))
    }
)
hlinscription4: BinaryAssociation = BinaryAssociation(
    name="hlinscription4",
    ends={
        Property(name="nppn_HLAnnotation", type=org_k1s_nppn_HLArcAddin, multiplicity=Multiplicity(1, 1)),
        Property(name="org_k1s_nppn_HLArcAddin", type=nppn_HLAnnotation, multiplicity=Multiplicity(0, 1))
    }
)
parent7: BinaryAssociation = BinaryAssociation(
    name="parent7",
    ends={
        Property(name="HasLabel", type=org_k1s_nppn_Label, multiplicity=Multiplicity(1, 1)),
        Property(name="label", type=nppn_HasLabel, multiplicity=Multiplicity(1, 1))
    }
)
sourceArc8: BinaryAssociation = BinaryAssociation(
    name="sourceArc8",
    ends={
        Property(name="Arc", type=org_k1s_nppn_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=nppn_Arc, multiplicity=Multiplicity(0, 9999))
    }
)
targetArc9: BinaryAssociation = BinaryAssociation(
    name="targetArc9",
    ends={
        Property(name="Arc10", type=org_k1s_nppn_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=nppn_Arc, multiplicity=Multiplicity(0, 9999))
    }
)
pragmatics11: BinaryAssociation = BinaryAssociation(
    name="pragmatics11",
    ends={
        Property(name="nppn_Pragmatic", type=org_k1s_nppn_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="org_k1s_nppn_Node", type=nppn_Pragmatic, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
page12: BinaryAssociation = BinaryAssociation(
    name="page12",
    ends={
        Property(name="Page13", type=org_k1s_nppn_Object, multiplicity=Multiplicity(1, 1)),
        Property(name="object", type=nppn_Page, multiplicity=Multiplicity(1, 1))
    }
)
petriNet14: BinaryAssociation = BinaryAssociation(
    name="petriNet14",
    ends={
        Property(name="PetriNet", type=org_k1s_nppn_Page, multiplicity=Multiplicity(1, 1)),
        Property(name="page", type=nppn_PetriNet, multiplicity=Multiplicity(1, 1))
    }
)
object15: BinaryAssociation = BinaryAssociation(
    name="object15",
    ends={
        Property(name="Object", type=org_k1s_nppn_Page, multiplicity=Multiplicity(1, 1)),
        Property(name="page16", type=nppn_Object, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
page20: BinaryAssociation = BinaryAssociation(
    name="page20",
    ends={
        Property(name="Page21", type=org_k1s_nppn_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="petriNet", type=nppn_Page, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
monitors22: BinaryAssociation = BinaryAssociation(
    name="monitors22",
    ends={
        Property(name="monitors.ecoreMonitor", type=org_k1s_nppn_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="petriNet23", type=nppn_Monitor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
references24: BinaryAssociation = BinaryAssociation(
    name="references24",
    ends={
        Property(name="RefPlace", type=org_k1s_nppn_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="ref", type=nppn_RefPlace, multiplicity=Multiplicity(0, 9999))
    }
)
arc17: BinaryAssociation = BinaryAssociation(
    name="arc17",
    ends={
        Property(name="Arc19", type=org_k1s_nppn_Page, multiplicity=Multiplicity(1, 1)),
        Property(name="page18", type=nppn_Arc, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ref25: BinaryAssociation = BinaryAssociation(
    name="ref25",
    ends={
        Property(name="Place", type=org_k1s_nppn_RefPlace, multiplicity=Multiplicity(1, 1)),
        Property(name="references", type=nppn_Place, multiplicity=Multiplicity(1, 1))
    }
)
ref26: BinaryAssociation = BinaryAssociation(
    name="ref26",
    ends={
        Property(name="nppn_TransitionNode", type=org_k1s_nppn_RefTrans, multiplicity=Multiplicity(1, 1)),
        Property(name="org_k1s_nppn_RefTrans", type=nppn_TransitionNode, multiplicity=Multiplicity(1, 1))
    }
)
patterns28: BinaryAssociation = BinaryAssociation(
    name="patterns28",
    ends={
        Property(name="nppn_PNPattern", type=org_k1s_nppn_Derived, multiplicity=Multiplicity(1, 1)),
        Property(name="org_k1s_nppn_Derived", type=nppn_PNPattern, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
constraints27: BinaryAssociation = BinaryAssociation(
    name="constraints27",
    ends={
        Property(name="nppn_PlacementConstraints", type=org_k1s_nppn_Pragmatic, multiplicity=Multiplicity(1, 1)),
        Property(name="org_k1s_nppn_Pragmatic", type=nppn_PlacementConstraints, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
children29: BinaryAssociation = BinaryAssociation(
    name="children29",
    ends={
        Property(name="nppn_Principal", type=org_k1s_nppn_AbstractTemplateTree, multiplicity=Multiplicity(1, 1)),
        Property(name="org_k1s_nppn_AbstractTemplateTree", type=nppn_Principal, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
principal30: BinaryAssociation = BinaryAssociation(
    name="principal30",
    ends={
        Property(name="nppn_Instance", type=org_k1s_nppn_Principal, multiplicity=Multiplicity(1, 1)),
        Property(name="org_k1s_nppn_Principal", type=nppn_Instance, multiplicity=Multiplicity(1, 1))
    }
)
children31: BinaryAssociation = BinaryAssociation(
    name="children31",
    ends={
        Property(name="nppn_Service", type=org_k1s_nppn_Principal, multiplicity=Multiplicity(1, 1)),
        Property(name="org_k1s_nppn_Principal32", type=nppn_Service, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
service33: BinaryAssociation = BinaryAssociation(
    name="service33",
    ends={
        Property(name="nppn_Instance34", type=org_k1s_nppn_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="org_k1s_nppn_Service", type=nppn_Instance, multiplicity=Multiplicity(1, 1))
    }
)
children35: BinaryAssociation = BinaryAssociation(
    name="children35",
    ends={
        Property(name="nppn_Block", type=org_k1s_nppn_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="org_k1s_nppn_Service36", type=nppn_Block, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
start37: BinaryAssociation = BinaryAssociation(
    name="start37",
    ends={
        Property(name="nppn_PlaceNode", type=org_k1s_nppn_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="org_k1s_nppn_Block", type=nppn_PlaceNode, multiplicity=Multiplicity(0, 1))
    }
)
end38: BinaryAssociation = BinaryAssociation(
    name="end38",
    ends={
        Property(name="nppn_PlaceNode40", type=org_k1s_nppn_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="org_k1s_nppn_Block39", type=nppn_PlaceNode, multiplicity=Multiplicity(0, 1))
    }
)
transition41: BinaryAssociation = BinaryAssociation(
    name="transition41",
    ends={
        Property(name="nppn_Transition", type=org_k1s_nppn_Atomic, multiplicity=Multiplicity(1, 1)),
        Property(name="org_k1s_nppn_Atomic", type=nppn_Transition, multiplicity=Multiplicity(1, 1))
    }
)
children42: BinaryAssociation = BinaryAssociation(
    name="children42",
    ends={
        Property(name="nppn_Block43", type=org_k1s_nppn_Container, multiplicity=Multiplicity(1, 1)),
        Property(name="org_k1s_nppn_Container", type=nppn_Block, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pragmatic44: BinaryAssociation = BinaryAssociation(
    name="pragmatic44",
    ends={
        Property(name="nppn_Pragmatic45", type=org_k1s_nppn_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="org_k1s_nppn_Binding", type=nppn_Pragmatic, multiplicity=Multiplicity(1, 1))
    }
)
bindings46: BinaryAssociation = BinaryAssociation(
    name="bindings46",
    ends={
        Property(name="nppn_Binding", type=org_k1s_nppn_Bindings, multiplicity=Multiplicity(1, 1)),
        Property(name="org_k1s_nppn_Bindings", type=nppn_Binding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_org_k1s_nppn_Arc_HasGraphics = Generalization(general=HasGraphics, specific=org_k1s_nppn_Arc)
gen_org_k1s_nppn_Arc_HLArcAddin = Generalization(general=HLArcAddin, specific=org_k1s_nppn_Arc)
gen_org_k1s_nppn_Instance_Node = Generalization(general=Node, specific=org_k1s_nppn_Instance)
gen_org_k1s_nppn_Name_HLAnnotation = Generalization(general=HLAnnotation, specific=org_k1s_nppn_Name)
gen_org_k1s_nppn_Node_Object = Generalization(general=Object, specific=org_k1s_nppn_Node)
gen_org_k1s_nppn_Object_HasGraphics = Generalization(general=HasGraphics, specific=org_k1s_nppn_Object)
gen_org_k1s_nppn_Object_HasLabel = Generalization(general=HasLabel, specific=org_k1s_nppn_Object)
gen_org_k1s_nppn_Object_HasName = Generalization(general=HasName, specific=org_k1s_nppn_Object)
gen_org_k1s_nppn_Page_HasName = Generalization(general=HasName, specific=org_k1s_nppn_Page)
gen_org_k1s_nppn_Page_HasLabel = Generalization(general=HasLabel, specific=org_k1s_nppn_Page)
gen_org_k1s_nppn_PetriNet_HasLabel = Generalization(general=HasLabel, specific=org_k1s_nppn_PetriNet)
gen_org_k1s_nppn_PetriNet_HasName = Generalization(general=HasName, specific=org_k1s_nppn_PetriNet)
gen_org_k1s_nppn_Place_PlaceNode = Generalization(general=PlaceNode, specific=org_k1s_nppn_Place)
gen_org_k1s_nppn_PlaceNode_Node = Generalization(general=Node, specific=org_k1s_nppn_PlaceNode)
gen_org_k1s_nppn_RefPlace_PlaceNode = Generalization(general=PlaceNode, specific=org_k1s_nppn_RefPlace)
gen_org_k1s_nppn_RefTrans_TransitionNode = Generalization(general=TransitionNode, specific=org_k1s_nppn_RefTrans)
gen_org_k1s_nppn_Transition_TransitionNode = Generalization(general=TransitionNode, specific=org_k1s_nppn_Transition)
gen_org_k1s_nppn_TransitionNode_Node = Generalization(general=Node, specific=org_k1s_nppn_TransitionNode)
gen_org_k1s_nppn_Derived_Pragmatic = Generalization(general=Pragmatic, specific=org_k1s_nppn_Derived)
gen_org_k1s_nppn_Explicit_Pragmatic = Generalization(general=Pragmatic, specific=org_k1s_nppn_Explicit)
gen_org_k1s_nppn_CustomDerivedPragmatics_Derived = Generalization(general=Derived, specific=org_k1s_nppn_CustomDerivedPragmatics)
gen_org_k1s_nppn_CustomDerivedPragmatics_CustomPragmatics = Generalization(general=CustomPragmatics, specific=org_k1s_nppn_CustomDerivedPragmatics)
gen_org_k1s_nppn_CustomExplicitPragmatics_Explicit = Generalization(general=Explicit, specific=org_k1s_nppn_CustomExplicitPragmatics)
gen_org_k1s_nppn_CustomExplicitPragmatics_CustomPragmatics = Generalization(general=CustomPragmatics, specific=org_k1s_nppn_CustomExplicitPragmatics)
gen_org_k1s_nppn_CustomPragmatics_Pragmatic = Generalization(general=Pragmatic, specific=org_k1s_nppn_CustomPragmatics)
gen_org_k1s_nppn_Container_Block = Generalization(general=Block, specific=org_k1s_nppn_Container)
gen_org_k1s_nppn_Atomic_Block = Generalization(general=Block, specific=org_k1s_nppn_Atomic)
gen_org_k1s_nppn_Loop_Container = Generalization(general=Container, specific=org_k1s_nppn_Loop)
gen_org_k1s_nppn_Conditional_Container = Generalization(general=Container, specific=org_k1s_nppn_Conditional)
gen_org_k1s_nppn_Loop_Container = Generalization(general=Container, specific=org_k1s_nppn_Loop)
gen_org_k1s_nppn_Conditinoal_Container = Generalization(general=Container, specific=org_k1s_nppn_Conditinoal)

# Domain Model
domain_model = DomainModel(
    name="org_k1s_nppn",
    types={org_k1s_nppn_Arc, HasGraphics, HLArcAddin, nppn_Node, org_k1s_nppn_HasLabel, nppn_Label, org_k1s_nppn_HasName, nppn_Name, nppn_Page, org_k1s_nppn_Instance, org_k1s_nppn_HLAnnotation, Node, org_k1s_nppn_HLArcAddin, nppn_HLAnnotation, nppn_HasLabel, org_k1s_nppn_Name, HLAnnotation, org_k1s_nppn_Node, Object, nppn_Arc, nppn_Pragmatic, org_k1s_nppn_Label, HasLabel, HasName, org_k1s_nppn_Page, nppn_PetriNet, nppn_Object, org_k1s_nppn_Object, org_k1s_nppn_PetriNet, nppn_Monitor, org_k1s_nppn_Place, PlaceNode, nppn_RefPlace, org_k1s_nppn_RefPlace, nppn_Place, org_k1s_nppn_RefTrans, TransitionNode, nppn_TransitionNode, org_k1s_nppn_Transition, org_k1s_nppn_TransitionNode, org_k1s_nppn_Pragmatic, org_k1s_nppn_PlaceNode, org_k1s_nppn_Derived, Pragmatic, nppn_PNPattern, org_k1s_nppn_Explicit, org_k1s_nppn_PNPattern, nppn_PlacementConstraints, org_k1s_nppn_CustomDerivedPragmatics, Derived, CustomPragmatics, Explicit, org_k1s_nppn_CustomPragmatics, org_k1s_nppn_CustomExplicitPragmatics, org_k1s_nppn_AbstractTemplateTree, nppn_Principal, org_k1s_nppn_PlacementConstraints, org_k1s_nppn_Principal, nppn_Instance, nppn_Service, org_k1s_nppn_Service, nppn_Block, org_k1s_nppn_Block, nppn_PlaceNode, nppn_Transition, org_k1s_nppn_Container, org_k1s_nppn_Binding, org_k1s_nppn_Atomic, Block, org_k1s_nppn_Loop, Container, org_k1s_nppn_Conditional, org_k1s_nppn_Conditinoal, org_k1s_nppn_Bindings, nppn_Binding},
    associations={source0, target1, label5, name6, page3, hlinscription4, parent7, sourceArc8, targetArc9, pragmatics11, page12, petriNet14, object15, page20, monitors22, references24, arc17, ref25, ref26, patterns28, constraints27, children29, principal30, children31, service33, children35, start37, end38, transition41, children42, pragmatic44, bindings46},
    generalizations={gen_org_k1s_nppn_Arc_HasGraphics, gen_org_k1s_nppn_Arc_HLArcAddin, gen_org_k1s_nppn_Instance_Node, gen_org_k1s_nppn_Name_HLAnnotation, gen_org_k1s_nppn_Node_Object, gen_org_k1s_nppn_Object_HasGraphics, gen_org_k1s_nppn_Object_HasLabel, gen_org_k1s_nppn_Object_HasName, gen_org_k1s_nppn_Page_HasName, gen_org_k1s_nppn_Page_HasLabel, gen_org_k1s_nppn_PetriNet_HasLabel, gen_org_k1s_nppn_PetriNet_HasName, gen_org_k1s_nppn_Place_PlaceNode, gen_org_k1s_nppn_PlaceNode_Node, gen_org_k1s_nppn_RefPlace_PlaceNode, gen_org_k1s_nppn_RefTrans_TransitionNode, gen_org_k1s_nppn_Transition_TransitionNode, gen_org_k1s_nppn_TransitionNode_Node, gen_org_k1s_nppn_Derived_Pragmatic, gen_org_k1s_nppn_Explicit_Pragmatic, gen_org_k1s_nppn_CustomDerivedPragmatics_Derived, gen_org_k1s_nppn_CustomDerivedPragmatics_CustomPragmatics, gen_org_k1s_nppn_CustomExplicitPragmatics_Explicit, gen_org_k1s_nppn_CustomExplicitPragmatics_CustomPragmatics, gen_org_k1s_nppn_CustomPragmatics_Pragmatic, gen_org_k1s_nppn_Container_Block, gen_org_k1s_nppn_Atomic_Block, gen_org_k1s_nppn_Loop_Container, gen_org_k1s_nppn_Conditional_Container, gen_org_k1s_nppn_Loop_Container, gen_org_k1s_nppn_Conditinoal_Container},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)