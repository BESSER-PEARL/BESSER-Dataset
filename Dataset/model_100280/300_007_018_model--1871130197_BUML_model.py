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
			EnumerationLiteral(name="Test")
    }
)

# Classes
model_Page = Class(name="model_Page")
model_Attribute = Class(name="model_Attribute", is_abstract=True)
model_HasId = Class(name="model_HasId", is_abstract=True)
model_HasLabel = Class(name="model_HasLabel", is_abstract=True)
model_Label = Class(name="model_Label", is_abstract=True)
model_Annotation = Class(name="model_Annotation", is_abstract=True)
Label = Class(name="Label")
HasGraphics = Class(name="HasGraphics")
HLAnnotationAddin = Class(name="HLAnnotationAddin")
model_Arc = Class(name="model_Arc")
HLArcAddin = Class(name="HLArcAddin")
HasId = Class(name="HasId")
model_Node = Class(name="model_Node", is_abstract=True)
Object = Class(name="Object")
model_Object = Class(name="model_Object", is_abstract=True)
model_HasName = Class(name="model_HasName", is_abstract=True)
model_Name = Class(name="model_Name")
model_HasToolInfo = Class(name="model_HasToolInfo", is_abstract=True)
model_ToolInfo = Class(name="model_ToolInfo")
HasToolInfo = Class(name="HasToolInfo")
HLAnnotation = Class(name="HLAnnotation")
HasLabel = Class(name="HasLabel")
HasName = Class(name="HasName")
model_PetriNet = Class(name="model_PetriNet")
model_RefPlace = Class(name="model_RefPlace")
model_PlaceNode = Class(name="model_PlaceNode", is_abstract=True)
Node = Class(name="Node")
HLPlaceAddin = Class(name="HLPlaceAddin")
model_FusionGroup = Class(name="model_FusionGroup")
model_Place = Class(name="model_Place")
PlaceNode = Class(name="PlaceNode")
model_Transition = Class(name="model_Transition")
HLTransitionAddin = Class(name="HLTransitionAddin")
CPNToolsTransitionAddin = Class(name="CPNToolsTransitionAddin")
model_HLMarking = Class(name="model_HLMarking")
Annotation = Class(name="Annotation")
model_RefTrans = Class(name="model_RefTrans")
TransitionNode = Class(name="TransitionNode")
model_TransitionNode = Class(name="model_TransitionNode", is_abstract=True)
model_Type = Class(name="model_Type")
model_HLPlaceAddin = Class(name="model_HLPlaceAddin", is_abstract=True)
model_HLTransitionAddin = Class(name="model_HLTransitionAddin", is_abstract=True)
model_CPNToolsTransitionAddin = Class(name="model_CPNToolsTransitionAddin", is_abstract=True)
model_Code = Class(name="model_Code")
model_Time = Class(name="model_Time")
model_HLAnnotationAddin = Class(name="model_HLAnnotationAddin", is_abstract=True)
model_HLArcAddin = Class(name="model_HLArcAddin", is_abstract=True)
model_HLAnnotation = Class(name="model_HLAnnotation")
model_Condition = Class(name="model_Condition")
Place = Class(name="Place")
model_HLDeclaration = Class(name="model_HLDeclaration")
model_DeclarationStructure = Class(name="model_DeclarationStructure")
model_Instance = Class(name="model_Instance")
model_ParameterAssignment = Class(name="model_ParameterAssignment")
model_HLArcType_1 = Class(name="model_HLArcType_1", is_abstract=True)

# model_Page class attributes and methods

# model_Attribute class attributes and methods

# model_HasId class attributes and methods
model_HasId_id: Property = Property(name="id", type=StringType)
model_HasId.attributes={model_HasId_id}

# model_HasLabel class attributes and methods

# model_Label class attributes and methods
model_Label_m_asString: Method = Method(name="asString", parameters={}, type=StringType)
model_Label.methods={model_Label_m_asString}

# model_Annotation class attributes and methods

# Label class attributes and methods

# HasGraphics class attributes and methods

# HLAnnotationAddin class attributes and methods

# model_Arc class attributes and methods

# HLArcAddin class attributes and methods

# HasId class attributes and methods

# model_Node class attributes and methods

# Object class attributes and methods

# model_Object class attributes and methods

# model_HasName class attributes and methods

# model_Name class attributes and methods

# model_HasToolInfo class attributes and methods

# model_ToolInfo class attributes and methods
model_ToolInfo_tool: Property = Property(name="tool", type=StringType)
model_ToolInfo_version: Property = Property(name="version", type=StringType)
model_ToolInfo.attributes={model_ToolInfo_version, model_ToolInfo_tool}

# HasToolInfo class attributes and methods

# HLAnnotation class attributes and methods

# HasLabel class attributes and methods

# HasName class attributes and methods

# model_PetriNet class attributes and methods
model_PetriNet_type: Property = Property(name="type", type=StringType)
model_PetriNet.attributes={model_PetriNet_type}

# model_RefPlace class attributes and methods

# model_PlaceNode class attributes and methods

# Node class attributes and methods

# HLPlaceAddin class attributes and methods

# model_FusionGroup class attributes and methods

# model_Place class attributes and methods

# PlaceNode class attributes and methods

# model_Transition class attributes and methods

# HLTransitionAddin class attributes and methods

# CPNToolsTransitionAddin class attributes and methods

# model_HLMarking class attributes and methods

# Annotation class attributes and methods

# model_RefTrans class attributes and methods

# TransitionNode class attributes and methods

# model_TransitionNode class attributes and methods

# model_Type class attributes and methods

# model_HLPlaceAddin class attributes and methods

# model_HLTransitionAddin class attributes and methods

# model_CPNToolsTransitionAddin class attributes and methods

# model_Code class attributes and methods

# model_Time class attributes and methods

# model_HLAnnotationAddin class attributes and methods
model_HLAnnotationAddin_text: Property = Property(name="text", type=StringType)
model_HLAnnotationAddin.attributes={model_HLAnnotationAddin_text}

# model_HLArcAddin class attributes and methods
model_HLArcAddin_type: Property = Property(name="type", type=StringType)
model_HLArcAddin.attributes={model_HLArcAddin_type}

# model_HLAnnotation class attributes and methods

# model_Condition class attributes and methods

# Place class attributes and methods

# model_HLDeclaration class attributes and methods

# model_DeclarationStructure class attributes and methods

# model_Instance class attributes and methods
model_Instance_subPageID: Property = Property(name="subPageID", type=StringType)
model_Instance.attributes={model_Instance_subPageID}

# model_ParameterAssignment class attributes and methods
model_ParameterAssignment_parameter: Property = Property(name="parameter", type=StringType)
model_ParameterAssignment_value: Property = Property(name="value", type=StringType)
model_ParameterAssignment.attributes={model_ParameterAssignment_value, model_ParameterAssignment_parameter}

# model_HLArcType_1 class attributes and methods

# Relationships
page3: BinaryAssociation = BinaryAssociation(
    name="page3",
    ends={
        Property(name="Page", type=model_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="arc", type=model_Page, multiplicity=Multiplicity(1, 1))
    }
)
label4: BinaryAssociation = BinaryAssociation(
    name="label4",
    ends={
        Property(name="Label", type=model_HasLabel, multiplicity=Multiplicity(1, 1)),
        Property(name="parent", type=model_Label, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
sourceArc9: BinaryAssociation = BinaryAssociation(
    name="sourceArc9",
    ends={
        Property(name="Arc", type=model_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=model_Arc, multiplicity=Multiplicity(0, 9999))
    }
)
targetArc10: BinaryAssociation = BinaryAssociation(
    name="targetArc10",
    ends={
        Property(name="Arc11", type=model_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=model_Arc, multiplicity=Multiplicity(0, 9999))
    }
)
name5: BinaryAssociation = BinaryAssociation(
    name="name5",
    ends={
        Property(name="model_Name", type=model_HasName, multiplicity=Multiplicity(1, 1)),
        Property(name="model_HasName", type=model_Name, multiplicity=Multiplicity(0, 1))
    }
)
toolinfo6: BinaryAssociation = BinaryAssociation(
    name="toolinfo6",
    ends={
        Property(name="ToolInfo", type=model_HasToolInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="parent7", type=model_ToolInfo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent8: BinaryAssociation = BinaryAssociation(
    name="parent8",
    ends={
        Property(name="HasLabel", type=model_Label, multiplicity=Multiplicity(1, 1)),
        Property(name="label", type=model_HasLabel, multiplicity=Multiplicity(1, 1))
    }
)
object15: BinaryAssociation = BinaryAssociation(
    name="object15",
    ends={
        Property(name="Object", type=model_Page, multiplicity=Multiplicity(1, 1)),
        Property(name="page16", type=model_Object, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arc17: BinaryAssociation = BinaryAssociation(
    name="arc17",
    ends={
        Property(name="Arc19", type=model_Page, multiplicity=Multiplicity(1, 1)),
        Property(name="page18", type=model_Arc, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
page12: BinaryAssociation = BinaryAssociation(
    name="page12",
    ends={
        Property(name="Page13", type=model_Object, multiplicity=Multiplicity(1, 1)),
        Property(name="object", type=model_Page, multiplicity=Multiplicity(1, 1))
    }
)
petriNet14: BinaryAssociation = BinaryAssociation(
    name="petriNet14",
    ends={
        Property(name="PetriNet", type=model_Page, multiplicity=Multiplicity(1, 1)),
        Property(name="page", type=model_PetriNet, multiplicity=Multiplicity(1, 1))
    }
)
references24: BinaryAssociation = BinaryAssociation(
    name="references24",
    ends={
        Property(name="RefPlace", type=model_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="ref", type=model_RefPlace, multiplicity=Multiplicity(0, 9999))
    }
)
page20: BinaryAssociation = BinaryAssociation(
    name="page20",
    ends={
        Property(name="Page21", type=model_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="petriNet", type=model_Page, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
fusionGroups22: BinaryAssociation = BinaryAssociation(
    name="fusionGroups22",
    ends={
        Property(name="FusionGroup", type=model_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="petriNet23", type=model_FusionGroup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent27: BinaryAssociation = BinaryAssociation(
    name="parent27",
    ends={
        Property(name="HasToolInfo", type=model_ToolInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="toolinfo", type=model_HasToolInfo, multiplicity=Multiplicity(1, 1))
    }
)
ref25: BinaryAssociation = BinaryAssociation(
    name="ref25",
    ends={
        Property(name="Place", type=model_RefPlace, multiplicity=Multiplicity(1, 1)),
        Property(name="references", type=model_Place, multiplicity=Multiplicity(1, 1))
    }
)
ref26: BinaryAssociation = BinaryAssociation(
    name="ref26",
    ends={
        Property(name="model_TransitionNode", type=model_RefTrans, multiplicity=Multiplicity(1, 1)),
        Property(name="model_RefTrans", type=model_TransitionNode, multiplicity=Multiplicity(1, 1))
    }
)
initialMarking29: BinaryAssociation = BinaryAssociation(
    name="initialMarking29",
    ends={
        Property(name="model_HLMarking", type=model_HLPlaceAddin, multiplicity=Multiplicity(1, 1)),
        Property(name="model_HLPlaceAddin30", type=model_HLMarking, multiplicity=Multiplicity(0, 1))
    }
)
type28: BinaryAssociation = BinaryAssociation(
    name="type28",
    ends={
        Property(name="model_Type", type=model_HLPlaceAddin, multiplicity=Multiplicity(1, 1)),
        Property(name="model_HLPlaceAddin", type=model_Type, multiplicity=Multiplicity(0, 1))
    }
)
condition32: BinaryAssociation = BinaryAssociation(
    name="condition32",
    ends={
        Property(name="model_Condition", type=model_HLTransitionAddin, multiplicity=Multiplicity(1, 1)),
        Property(name="model_HLTransitionAddin", type=model_Condition, multiplicity=Multiplicity(0, 1))
    }
)
code33: BinaryAssociation = BinaryAssociation(
    name="code33",
    ends={
        Property(name="model_Code", type=model_CPNToolsTransitionAddin, multiplicity=Multiplicity(1, 1)),
        Property(name="model_CPNToolsTransitionAddin", type=model_Code, multiplicity=Multiplicity(0, 1))
    }
)
time34: BinaryAssociation = BinaryAssociation(
    name="time34",
    ends={
        Property(name="model_Time", type=model_CPNToolsTransitionAddin, multiplicity=Multiplicity(1, 1)),
        Property(name="model_CPNToolsTransitionAddin35", type=model_Time, multiplicity=Multiplicity(0, 1))
    }
)
hlinscription31: BinaryAssociation = BinaryAssociation(
    name="hlinscription31",
    ends={
        Property(name="model_HLAnnotation", type=model_HLArcAddin, multiplicity=Multiplicity(1, 1)),
        Property(name="model_HLArcAddin", type=model_HLAnnotation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
instance38: BinaryAssociation = BinaryAssociation(
    name="instance38",
    ends={
        Property(name="Instance", type=model_ParameterAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="parameterAssignment", type=model_Instance, multiplicity=Multiplicity(0, 1))
    }
)
structure36: BinaryAssociation = BinaryAssociation(
    name="structure36",
    ends={
        Property(name="model_DeclarationStructure", type=model_HLDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="model_HLDeclaration", type=model_DeclarationStructure, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameterAssignment37: BinaryAssociation = BinaryAssociation(
    name="parameterAssignment37",
    ends={
        Property(name="ParameterAssignment", type=model_Instance, multiplicity=Multiplicity(1, 1)),
        Property(name="instance", type=model_ParameterAssignment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
petriNet39: BinaryAssociation = BinaryAssociation(
    name="petriNet39",
    ends={
        Property(name="PetriNet40", type=model_FusionGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="fusionGroups", type=model_PetriNet, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_model_Attribute_Label = Generalization(general=Label, specific=model_Attribute)
gen_model_Annotation_Label = Generalization(general=Label, specific=model_Annotation)
gen_model_Annotation_HasGraphics = Generalization(general=HasGraphics, specific=model_Annotation)
gen_model_Annotation_HLAnnotationAddin = Generalization(general=HLAnnotationAddin, specific=model_Annotation)
gen_model_Arc_HLArcAddin = Generalization(general=HLArcAddin, specific=model_Arc)
gen_model_Arc_HasId = Generalization(general=HasId, specific=model_Arc)
gen_model_Node_Object = Generalization(general=Object, specific=model_Node)
gen_model_Object_HasToolInfo = Generalization(general=HasToolInfo, specific=model_Object)
gen_model_Label_HasToolInfo = Generalization(general=HasToolInfo, specific=model_Label)
gen_model_Name_HLAnnotation = Generalization(general=HLAnnotation, specific=model_Name)
gen_model_Object_HasGraphics = Generalization(general=HasGraphics, specific=model_Object)
gen_model_Object_HasId = Generalization(general=HasId, specific=model_Object)
gen_model_Object_HasLabel = Generalization(general=HasLabel, specific=model_Object)
gen_model_Object_HasName = Generalization(general=HasName, specific=model_Object)
gen_model_Page_HasName = Generalization(general=HasName, specific=model_Page)
gen_model_Page_HasLabel = Generalization(general=HasLabel, specific=model_Page)
gen_model_Page_HasId = Generalization(general=HasId, specific=model_Page)
gen_model_PlaceNode_Node = Generalization(general=Node, specific=model_PlaceNode)
gen_model_PlaceNode_HLPlaceAddin = Generalization(general=HLPlaceAddin, specific=model_PlaceNode)
gen_model_PetriNet_HasToolInfo = Generalization(general=HasToolInfo, specific=model_PetriNet)
gen_model_PetriNet_HasId = Generalization(general=HasId, specific=model_PetriNet)
gen_model_PetriNet_HasLabel = Generalization(general=HasLabel, specific=model_PetriNet)
gen_model_PetriNet_HasName = Generalization(general=HasName, specific=model_PetriNet)
gen_model_Place_PlaceNode = Generalization(general=PlaceNode, specific=model_Place)
gen_model_Transition_TransitionNode = Generalization(general=TransitionNode, specific=model_Transition)
gen_model_TransitionNode_Node = Generalization(general=Node, specific=model_TransitionNode)
gen_model_TransitionNode_HLTransitionAddin = Generalization(general=HLTransitionAddin, specific=model_TransitionNode)
gen_model_TransitionNode_CPNToolsTransitionAddin = Generalization(general=CPNToolsTransitionAddin, specific=model_TransitionNode)
gen_model_HLMarking_Annotation = Generalization(general=Annotation, specific=model_HLMarking)
gen_model_RefPlace_PlaceNode = Generalization(general=PlaceNode, specific=model_RefPlace)
gen_model_RefTrans_TransitionNode = Generalization(general=TransitionNode, specific=model_RefTrans)
gen_model_Type_Annotation = Generalization(general=Annotation, specific=model_Type)
gen_model_HLAnnotation_Annotation = Generalization(general=Annotation, specific=model_HLAnnotation)
gen_model_Condition_Annotation = Generalization(general=Annotation, specific=model_Condition)
gen_model_FusionGroup_Place = Generalization(general=Place, specific=model_FusionGroup)
gen_model_Code_Annotation = Generalization(general=Annotation, specific=model_Code)
gen_model_Time_Annotation = Generalization(general=Annotation, specific=model_Time)
gen_model_HLDeclaration_Annotation = Generalization(general=Annotation, specific=model_HLDeclaration)
gen_model_HLDeclaration_HasId = Generalization(general=HasId, specific=model_HLDeclaration)
gen_model_Instance_Node = Generalization(general=Node, specific=model_Instance)

# Domain Model
domain_model = DomainModel(
    name="model",
    types={model_Page, model_Attribute, model_HasId, model_HasLabel, model_Label, model_Annotation, Label, HasGraphics, HLAnnotationAddin, model_Arc, HLArcAddin, HasId, model_Node, Object, model_Object, model_HasName, model_Name, model_HasToolInfo, model_ToolInfo, HasToolInfo, HLAnnotation, HasLabel, HasName, model_PetriNet, model_RefPlace, model_PlaceNode, Node, HLPlaceAddin, model_FusionGroup, model_Place, PlaceNode, model_Transition, HLTransitionAddin, CPNToolsTransitionAddin, model_HLMarking, Annotation, model_RefTrans, TransitionNode, model_TransitionNode, model_Type, model_HLPlaceAddin, model_HLTransitionAddin, model_CPNToolsTransitionAddin, model_Code, model_Time, model_HLAnnotationAddin, model_HLArcAddin, model_HLAnnotation, model_Condition, Place, model_HLDeclaration, model_DeclarationStructure, model_Instance, model_ParameterAssignment, model_HLArcType_1, HLArcType},
    associations={page3, label4, source0, target1, sourceArc9, targetArc10, name5, toolinfo6, parent8, object15, arc17, page12, petriNet14, references24, page20, fusionGroups22, parent27, ref25, ref26, initialMarking29, type28, condition32, code33, time34, hlinscription31, instance38, structure36, parameterAssignment37, petriNet39},
    generalizations={gen_model_Attribute_Label, gen_model_Annotation_Label, gen_model_Annotation_HasGraphics, gen_model_Annotation_HLAnnotationAddin, gen_model_Arc_HLArcAddin, gen_model_Arc_HasId, gen_model_Node_Object, gen_model_Object_HasToolInfo, gen_model_Label_HasToolInfo, gen_model_Name_HLAnnotation, gen_model_Object_HasGraphics, gen_model_Object_HasId, gen_model_Object_HasLabel, gen_model_Object_HasName, gen_model_Page_HasName, gen_model_Page_HasLabel, gen_model_Page_HasId, gen_model_PlaceNode_Node, gen_model_PlaceNode_HLPlaceAddin, gen_model_PetriNet_HasToolInfo, gen_model_PetriNet_HasId, gen_model_PetriNet_HasLabel, gen_model_PetriNet_HasName, gen_model_Place_PlaceNode, gen_model_Transition_TransitionNode, gen_model_TransitionNode_Node, gen_model_TransitionNode_HLTransitionAddin, gen_model_TransitionNode_CPNToolsTransitionAddin, gen_model_HLMarking_Annotation, gen_model_RefPlace_PlaceNode, gen_model_RefTrans_TransitionNode, gen_model_Type_Annotation, gen_model_HLAnnotation_Annotation, gen_model_Condition_Annotation, gen_model_FusionGroup_Place, gen_model_Code_Annotation, gen_model_Time_Annotation, gen_model_HLDeclaration_Annotation, gen_model_HLDeclaration_HasId, gen_model_Instance_Node},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)