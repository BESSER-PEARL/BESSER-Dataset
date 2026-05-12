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
HLArcType: Enumeration = Enumeration(
    name="HLArcType",
    literals={
            EnumerationLiteral(name="Normal"),
			EnumerationLiteral(name="Test"),
			EnumerationLiteral(name="Inhibitor"),
			EnumerationLiteral(name="Reset")
    }
)

TimeType: Enumeration = Enumeration(
    name="TimeType",
    literals={
            EnumerationLiteral(name="Integer"),
			EnumerationLiteral(name="Real")
    }
)

# Classes
model_Annotation = Class(name="model_Annotation", is_abstract=True)
Label = Class(name="Label")
HasGraphics = Class(name="HasGraphics")
HLAnnotationAddin = Class(name="HLAnnotationAddin")
model_Arc = Class(name="model_Arc")
HasId = Class(name="HasId")
HLArcAddin = Class(name="HLArcAddin")
model_Node = Class(name="model_Node", is_abstract=True)
model_Page = Class(name="model_Page")
model_Attribute = Class(name="model_Attribute", is_abstract=True)
model_CPNToolsTransitionAddin = Class(name="model_CPNToolsTransitionAddin", is_abstract=True)
model_Code = Class(name="model_Code")
model_Time = Class(name="model_Time")
model_Priority = Class(name="model_Priority")
model_Condition = Class(name="model_Condition")
model_FusionGroup = Class(name="model_FusionGroup")
Place = Class(name="Place")
model_PetriNet = Class(name="model_PetriNet")
model_HLAnnotation = Class(name="model_HLAnnotation")
model_HLAnnotationAddin = Class(name="model_HLAnnotationAddin", is_abstract=True)
model_HLArcAddin = Class(name="model_HLArcAddin", is_abstract=True)
Annotation = Class(name="Annotation")
model_DeclarationStructure = Class(name="model_DeclarationStructure")
model_HLMarking = Class(name="model_HLMarking")
model_HLPlaceAddin = Class(name="model_HLPlaceAddin", is_abstract=True)
model_Sort = Class(name="model_Sort")
model_HLTransitionAddin = Class(name="model_HLTransitionAddin", is_abstract=True)
model_HasId = Class(name="model_HasId", is_abstract=True)
model_HLDeclaration = Class(name="model_HLDeclaration")
model_Label = Class(name="model_Label", is_abstract=True)
model_HasName = Class(name="model_HasName", is_abstract=True)
model_Name = Class(name="model_Name")
model_HasToolInfo = Class(name="model_HasToolInfo", is_abstract=True)
model_ToolInfo = Class(name="model_ToolInfo")
model_Instance = Class(name="model_Instance")
Node = Class(name="Node")
model_ParameterAssignment = Class(name="model_ParameterAssignment")
model_HasLabel = Class(name="model_HasLabel", is_abstract=True)
HLAnnotation = Class(name="HLAnnotation")
Object = Class(name="Object")
model_Object = Class(name="model_Object", is_abstract=True)
HasLabel = Class(name="HasLabel")
HasName = Class(name="HasName")
HasToolInfo = Class(name="HasToolInfo")
model_Monitor = Class(name="model_Monitor")
model_Place = Class(name="model_Place")
PlaceNode = Class(name="PlaceNode")
model_RefPlace = Class(name="model_RefPlace")
model_PlaceNode = Class(name="model_PlaceNode", is_abstract=True)
HLPlaceAddin = Class(name="HLPlaceAddin")
model_RefTrans = Class(name="model_RefTrans")
TransitionNode = Class(name="TransitionNode")
model_TransitionNode = Class(name="model_TransitionNode", is_abstract=True)
model_Transition = Class(name="model_Transition")
HLTransitionAddin = Class(name="HLTransitionAddin")
CPNToolsTransitionAddin = Class(name="CPNToolsTransitionAddin")

# model_Annotation class attributes and methods

# Label class attributes and methods

# HasGraphics class attributes and methods

# HLAnnotationAddin class attributes and methods

# model_Arc class attributes and methods

# HasId class attributes and methods

# HLArcAddin class attributes and methods

# model_Node class attributes and methods

# model_Page class attributes and methods

# model_Attribute class attributes and methods

# model_CPNToolsTransitionAddin class attributes and methods

# model_Code class attributes and methods

# model_Time class attributes and methods

# model_Priority class attributes and methods

# model_Condition class attributes and methods

# model_FusionGroup class attributes and methods

# Place class attributes and methods

# model_PetriNet class attributes and methods
model_PetriNet_timeType: Property = Property(name="timeType", type=StringType)
model_PetriNet_kind: Property = Property(name="kind", type=StringType)
model_PetriNet.attributes={model_PetriNet_kind, model_PetriNet_timeType}

# model_HLAnnotation class attributes and methods

# model_HLAnnotationAddin class attributes and methods
model_HLAnnotationAddin_text: Property = Property(name="text", type=StringType)
model_HLAnnotationAddin.attributes={model_HLAnnotationAddin_text}

# model_HLArcAddin class attributes and methods
model_HLArcAddin_kind: Property = Property(name="kind", type=StringType)
model_HLArcAddin.attributes={model_HLArcAddin_kind}

# Annotation class attributes and methods

# model_DeclarationStructure class attributes and methods

# model_HLMarking class attributes and methods

# model_HLPlaceAddin class attributes and methods

# model_Sort class attributes and methods

# model_HLTransitionAddin class attributes and methods

# model_HasId class attributes and methods
model_HasId_id: Property = Property(name="id", type=StringType)
model_HasId.attributes={model_HasId_id}

# model_HLDeclaration class attributes and methods

# model_Label class attributes and methods
model_Label_m_asString: Method = Method(name="asString", parameters={}, type=StringType)
model_Label.methods={model_Label_m_asString}

# model_HasName class attributes and methods

# model_Name class attributes and methods

# model_HasToolInfo class attributes and methods

# model_ToolInfo class attributes and methods
model_ToolInfo_tool: Property = Property(name="tool", type=StringType)
model_ToolInfo_version: Property = Property(name="version", type=StringType)
model_ToolInfo.attributes={model_ToolInfo_tool, model_ToolInfo_version}

# model_Instance class attributes and methods
model_Instance_subPageID: Property = Property(name="subPageID", type=StringType)
model_Instance.attributes={model_Instance_subPageID}

# Node class attributes and methods

# model_ParameterAssignment class attributes and methods
model_ParameterAssignment_parameter: Property = Property(name="parameter", type=StringType)
model_ParameterAssignment_value: Property = Property(name="value", type=StringType)
model_ParameterAssignment.attributes={model_ParameterAssignment_value, model_ParameterAssignment_parameter}

# model_HasLabel class attributes and methods

# HLAnnotation class attributes and methods

# Object class attributes and methods

# model_Object class attributes and methods

# HasLabel class attributes and methods

# HasName class attributes and methods

# HasToolInfo class attributes and methods

# model_Monitor class attributes and methods

# model_Place class attributes and methods

# PlaceNode class attributes and methods

# model_RefPlace class attributes and methods

# model_PlaceNode class attributes and methods

# HLPlaceAddin class attributes and methods

# model_RefTrans class attributes and methods

# TransitionNode class attributes and methods

# model_TransitionNode class attributes and methods

# model_Transition class attributes and methods

# HLTransitionAddin class attributes and methods

# CPNToolsTransitionAddin class attributes and methods

# Relationships
page3: BinaryAssociation = BinaryAssociation(
    name="page3",
    ends={
        Property(name="Page", type=model_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="arc", type=model_Page, multiplicity=Multiplicity(1, 1))
    }
)
code4: BinaryAssociation = BinaryAssociation(
    name="code4",
    ends={
        Property(name="model_Code", type=model_CPNToolsTransitionAddin, multiplicity=Multiplicity(1, 1)),
        Property(name="model_CPNToolsTransitionAddin", type=model_Code, multiplicity=Multiplicity(0, 1))
    }
)
time5: BinaryAssociation = BinaryAssociation(
    name="time5",
    ends={
        Property(name="model_Time", type=model_CPNToolsTransitionAddin, multiplicity=Multiplicity(1, 1)),
        Property(name="model_CPNToolsTransitionAddin6", type=model_Time, multiplicity=Multiplicity(0, 1))
    }
)
source0: BinaryAssociation = BinaryAssociation(
    name="source0",
    ends={
        Property(name="Node", type=model_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="sourceArc", type=model_Node, multiplicity=Multiplicity(1, 1))
    }
)
target1: BinaryAssociation = BinaryAssociation(
    name="target1",
    ends={
        Property(name="Node2", type=model_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="targetArc", type=model_Node, multiplicity=Multiplicity(1, 1))
    }
)
petriNet9: BinaryAssociation = BinaryAssociation(
    name="petriNet9",
    ends={
        Property(name="PetriNet", type=model_FusionGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="fusionGroups", type=model_PetriNet, multiplicity=Multiplicity(0, 1))
    }
)
hlinscription10: BinaryAssociation = BinaryAssociation(
    name="hlinscription10",
    ends={
        Property(name="model_HLAnnotation", type=model_HLArcAddin, multiplicity=Multiplicity(1, 1)),
        Property(name="model_HLArcAddin", type=model_HLAnnotation, multiplicity=Multiplicity(0, 1))
    }
)
priority7: BinaryAssociation = BinaryAssociation(
    name="priority7",
    ends={
        Property(name="model_Priority", type=model_CPNToolsTransitionAddin, multiplicity=Multiplicity(1, 1)),
        Property(name="model_CPNToolsTransitionAddin8", type=model_Priority, multiplicity=Multiplicity(0, 1))
    }
)
structure11: BinaryAssociation = BinaryAssociation(
    name="structure11",
    ends={
        Property(name="model_DeclarationStructure", type=model_HLDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="model_HLDeclaration", type=model_DeclarationStructure, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sort12: BinaryAssociation = BinaryAssociation(
    name="sort12",
    ends={
        Property(name="model_Sort", type=model_HLPlaceAddin, multiplicity=Multiplicity(1, 1)),
        Property(name="model_HLPlaceAddin", type=model_Sort, multiplicity=Multiplicity(0, 1))
    }
)
initialMarking13: BinaryAssociation = BinaryAssociation(
    name="initialMarking13",
    ends={
        Property(name="model_HLMarking", type=model_HLPlaceAddin, multiplicity=Multiplicity(1, 1)),
        Property(name="model_HLPlaceAddin14", type=model_HLMarking, multiplicity=Multiplicity(0, 1))
    }
)
condition15: BinaryAssociation = BinaryAssociation(
    name="condition15",
    ends={
        Property(name="model_Condition", type=model_HLTransitionAddin, multiplicity=Multiplicity(1, 1)),
        Property(name="model_HLTransitionAddin", type=model_Condition, multiplicity=Multiplicity(0, 1))
    }
)
label16: BinaryAssociation = BinaryAssociation(
    name="label16",
    ends={
        Property(name="Label", type=model_HasLabel, multiplicity=Multiplicity(1, 1)),
        Property(name="parent", type=model_Label, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name17: BinaryAssociation = BinaryAssociation(
    name="name17",
    ends={
        Property(name="model_Name", type=model_HasName, multiplicity=Multiplicity(1, 1)),
        Property(name="model_HasName", type=model_Name, multiplicity=Multiplicity(0, 1))
    }
)
toolinfo18: BinaryAssociation = BinaryAssociation(
    name="toolinfo18",
    ends={
        Property(name="ToolInfo", type=model_HasToolInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="parent19", type=model_ToolInfo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameterAssignment20: BinaryAssociation = BinaryAssociation(
    name="parameterAssignment20",
    ends={
        Property(name="ParameterAssignment", type=model_Instance, multiplicity=Multiplicity(1, 1)),
        Property(name="instance", type=model_ParameterAssignment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent21: BinaryAssociation = BinaryAssociation(
    name="parent21",
    ends={
        Property(name="HasLabel", type=model_Label, multiplicity=Multiplicity(1, 1)),
        Property(name="label", type=model_HasLabel, multiplicity=Multiplicity(1, 1))
    }
)
sourceArc22: BinaryAssociation = BinaryAssociation(
    name="sourceArc22",
    ends={
        Property(name="Arc", type=model_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=model_Arc, multiplicity=Multiplicity(0, 9999))
    }
)
targetArc23: BinaryAssociation = BinaryAssociation(
    name="targetArc23",
    ends={
        Property(name="Arc24", type=model_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=model_Arc, multiplicity=Multiplicity(0, 9999))
    }
)
petriNet27: BinaryAssociation = BinaryAssociation(
    name="petriNet27",
    ends={
        Property(name="PetriNet28", type=model_Page, multiplicity=Multiplicity(1, 1)),
        Property(name="page", type=model_PetriNet, multiplicity=Multiplicity(1, 1))
    }
)
object29: BinaryAssociation = BinaryAssociation(
    name="object29",
    ends={
        Property(name="Object", type=model_Page, multiplicity=Multiplicity(1, 1)),
        Property(name="page30", type=model_Object, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arc31: BinaryAssociation = BinaryAssociation(
    name="arc31",
    ends={
        Property(name="Arc33", type=model_Page, multiplicity=Multiplicity(1, 1)),
        Property(name="page32", type=model_Arc, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
instance34: BinaryAssociation = BinaryAssociation(
    name="instance34",
    ends={
        Property(name="Instance", type=model_ParameterAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="parameterAssignment", type=model_Instance, multiplicity=Multiplicity(0, 1))
    }
)
page25: BinaryAssociation = BinaryAssociation(
    name="page25",
    ends={
        Property(name="Page26", type=model_Object, multiplicity=Multiplicity(1, 1)),
        Property(name="object", type=model_Page, multiplicity=Multiplicity(1, 1))
    }
)
page35: BinaryAssociation = BinaryAssociation(
    name="page35",
    ends={
        Property(name="Page36", type=model_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="petriNet", type=model_Page, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
monitors37: BinaryAssociation = BinaryAssociation(
    name="monitors37",
    ends={
        Property(name="monitors.ecoreMonitor", type=model_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="petriNet38", type=model_Monitor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fusionGroups39: BinaryAssociation = BinaryAssociation(
    name="fusionGroups39",
    ends={
        Property(name="FusionGroup", type=model_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="petriNet40", type=model_FusionGroup, multiplicity=Multiplicity(0, 9999))
    }
)
references41: BinaryAssociation = BinaryAssociation(
    name="references41",
    ends={
        Property(name="RefPlace", type=model_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="ref", type=model_RefPlace, multiplicity=Multiplicity(0, 9999))
    }
)
ref42: BinaryAssociation = BinaryAssociation(
    name="ref42",
    ends={
        Property(name="Place", type=model_RefPlace, multiplicity=Multiplicity(1, 1)),
        Property(name="references", type=model_Place, multiplicity=Multiplicity(1, 1))
    }
)
ref43: BinaryAssociation = BinaryAssociation(
    name="ref43",
    ends={
        Property(name="model_TransitionNode", type=model_RefTrans, multiplicity=Multiplicity(1, 1)),
        Property(name="model_RefTrans", type=model_TransitionNode, multiplicity=Multiplicity(1, 1))
    }
)
parent44: BinaryAssociation = BinaryAssociation(
    name="parent44",
    ends={
        Property(name="HasToolInfo", type=model_ToolInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="toolinfo", type=model_HasToolInfo, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_model_Annotation_Label = Generalization(general=Label, specific=model_Annotation)
gen_model_Annotation_HasGraphics = Generalization(general=HasGraphics, specific=model_Annotation)
gen_model_Annotation_HLAnnotationAddin = Generalization(general=HLAnnotationAddin, specific=model_Annotation)
gen_model_Arc_HasId = Generalization(general=HasId, specific=model_Arc)
gen_model_Arc_HasGraphics = Generalization(general=HasGraphics, specific=model_Arc)
gen_model_Arc_HLArcAddin = Generalization(general=HLArcAddin, specific=model_Arc)
gen_model_Attribute_Label = Generalization(general=Label, specific=model_Attribute)
gen_model_Condition_Annotation = Generalization(general=Annotation, specific=model_Condition)
gen_model_FusionGroup_Place = Generalization(general=Place, specific=model_FusionGroup)
gen_model_HLAnnotation_Annotation = Generalization(general=Annotation, specific=model_HLAnnotation)
gen_model_Code_Annotation = Generalization(general=Annotation, specific=model_Code)
gen_model_HLDeclaration_HasId = Generalization(general=HasId, specific=model_HLDeclaration)
gen_model_HLMarking_Annotation = Generalization(general=Annotation, specific=model_HLMarking)
gen_model_HLDeclaration_Annotation = Generalization(general=Annotation, specific=model_HLDeclaration)
gen_model_Instance_Node = Generalization(general=Node, specific=model_Instance)
gen_model_Name_HLAnnotation = Generalization(general=HLAnnotation, specific=model_Name)
gen_model_Node_Object = Generalization(general=Object, specific=model_Node)
gen_model_Object_HasId = Generalization(general=HasId, specific=model_Object)
gen_model_Object_HasToolInfo = Generalization(general=HasToolInfo, specific=model_Object)
gen_model_Object_HasGraphics = Generalization(general=HasGraphics, specific=model_Object)
gen_model_Object_HasLabel = Generalization(general=HasLabel, specific=model_Object)
gen_model_Object_HasName = Generalization(general=HasName, specific=model_Object)
gen_model_Label_HasToolInfo = Generalization(general=HasToolInfo, specific=model_Label)
gen_model_Page_HasName = Generalization(general=HasName, specific=model_Page)
gen_model_Page_HasLabel = Generalization(general=HasLabel, specific=model_Page)
gen_model_PetriNet_HasId = Generalization(general=HasId, specific=model_PetriNet)
gen_model_PetriNet_HasToolInfo = Generalization(general=HasToolInfo, specific=model_PetriNet)
gen_model_Page_HasId = Generalization(general=HasId, specific=model_Page)
gen_model_Place_PlaceNode = Generalization(general=PlaceNode, specific=model_Place)
gen_model_PlaceNode_Node = Generalization(general=Node, specific=model_PlaceNode)
gen_model_PlaceNode_HLPlaceAddin = Generalization(general=HLPlaceAddin, specific=model_PlaceNode)
gen_model_PetriNet_HasLabel = Generalization(general=HasLabel, specific=model_PetriNet)
gen_model_PetriNet_HasName = Generalization(general=HasName, specific=model_PetriNet)
gen_model_RefTrans_TransitionNode = Generalization(general=TransitionNode, specific=model_RefTrans)
gen_model_Sort_Annotation = Generalization(general=Annotation, specific=model_Sort)
gen_model_Time_Annotation = Generalization(general=Annotation, specific=model_Time)
gen_model_Priority_Annotation = Generalization(general=Annotation, specific=model_Priority)
gen_model_RefPlace_PlaceNode = Generalization(general=PlaceNode, specific=model_RefPlace)
gen_model_TransitionNode_CPNToolsTransitionAddin = Generalization(general=CPNToolsTransitionAddin, specific=model_TransitionNode)
gen_model_Transition_TransitionNode = Generalization(general=TransitionNode, specific=model_Transition)
gen_model_TransitionNode_Node = Generalization(general=Node, specific=model_TransitionNode)
gen_model_TransitionNode_HLTransitionAddin = Generalization(general=HLTransitionAddin, specific=model_TransitionNode)

# Domain Model
domain_model = DomainModel(
    name="model",
    types={model_Annotation, Label, HasGraphics, HLAnnotationAddin, model_Arc, HasId, HLArcAddin, model_Node, model_Page, model_Attribute, model_CPNToolsTransitionAddin, model_Code, model_Time, model_Priority, model_Condition, model_FusionGroup, Place, model_PetriNet, model_HLAnnotation, model_HLAnnotationAddin, model_HLArcAddin, Annotation, model_DeclarationStructure, model_HLMarking, model_HLPlaceAddin, model_Sort, model_HLTransitionAddin, model_HasId, model_HLDeclaration, model_Label, model_HasName, model_Name, model_HasToolInfo, model_ToolInfo, model_Instance, Node, model_ParameterAssignment, model_HasLabel, HLAnnotation, Object, model_Object, HasLabel, HasName, HasToolInfo, model_Monitor, model_Place, PlaceNode, model_RefPlace, model_PlaceNode, HLPlaceAddin, model_RefTrans, TransitionNode, model_TransitionNode, model_Transition, HLTransitionAddin, CPNToolsTransitionAddin, HLArcType, TimeType},
    associations={page3, code4, time5, source0, target1, petriNet9, hlinscription10, priority7, structure11, sort12, initialMarking13, condition15, label16, name17, toolinfo18, parameterAssignment20, parent21, sourceArc22, targetArc23, petriNet27, object29, arc31, instance34, page25, page35, monitors37, fusionGroups39, references41, ref42, ref43, parent44},
    generalizations={gen_model_Annotation_Label, gen_model_Annotation_HasGraphics, gen_model_Annotation_HLAnnotationAddin, gen_model_Arc_HasId, gen_model_Arc_HasGraphics, gen_model_Arc_HLArcAddin, gen_model_Attribute_Label, gen_model_Condition_Annotation, gen_model_FusionGroup_Place, gen_model_HLAnnotation_Annotation, gen_model_Code_Annotation, gen_model_HLDeclaration_HasId, gen_model_HLMarking_Annotation, gen_model_HLDeclaration_Annotation, gen_model_Instance_Node, gen_model_Name_HLAnnotation, gen_model_Node_Object, gen_model_Object_HasId, gen_model_Object_HasToolInfo, gen_model_Object_HasGraphics, gen_model_Object_HasLabel, gen_model_Object_HasName, gen_model_Label_HasToolInfo, gen_model_Page_HasName, gen_model_Page_HasLabel, gen_model_PetriNet_HasId, gen_model_PetriNet_HasToolInfo, gen_model_Page_HasId, gen_model_Place_PlaceNode, gen_model_PlaceNode_Node, gen_model_PlaceNode_HLPlaceAddin, gen_model_PetriNet_HasLabel, gen_model_PetriNet_HasName, gen_model_RefTrans_TransitionNode, gen_model_Sort_Annotation, gen_model_Time_Annotation, gen_model_Priority_Annotation, gen_model_RefPlace_PlaceNode, gen_model_TransitionNode_CPNToolsTransitionAddin, gen_model_Transition_TransitionNode, gen_model_TransitionNode_Node, gen_model_TransitionNode_HLTransitionAddin},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)