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
LineKind: Enumeration = Enumeration(
    name="LineKind",
    literals={
            EnumerationLiteral(name="SOLID"),
			EnumerationLiteral(name="DASHED"),
			EnumerationLiteral(name="DOTTED")
    }
)

ShapeKind: Enumeration = Enumeration(
    name="ShapeKind",
    literals={
            EnumerationLiteral(name="CIRCLE"),
			EnumerationLiteral(name="SQUARE"),
			EnumerationLiteral(name="RECTANGLE"),
			EnumerationLiteral(name="ELLIPSE"),
			EnumerationLiteral(name="DIAMOND"),
			EnumerationLiteral(name="TRIANGLE")
    }
)

ContainmentKind: Enumeration = Enumeration(
    name="ContainmentKind",
    literals={
            EnumerationLiteral(name="FREE"),
			EnumerationLiteral(name="HORIZONTAL_ARRANGEMENT"),
			EnumerationLiteral(name="VERTICAL_ARRANGEMENT"),
			EnumerationLiteral(name="EXTERNAL_LINK")
    }
)

IntegrityRestrictionKind: Enumeration = Enumeration(
    name="IntegrityRestrictionKind",
    literals={
            EnumerationLiteral(name="CASCADE"),
			EnumerationLiteral(name="SET_NULL"),
			EnumerationLiteral(name="NO_ACTION")
    }
)

QueryLanguageKind: Enumeration = Enumeration(
    name="QueryLanguageKind",
    literals={
            EnumerationLiteral(name="LINQ"),
			EnumerationLiteral(name="JPQL"),
			EnumerationLiteral(name="SQL"),
			EnumerationLiteral(name="AQL"),
			EnumerationLiteral(name="OCL"),
			EnumerationLiteral(name="XPATH_XQUERY")
    }
)

OutlineKind: Enumeration = Enumeration(
    name="OutlineKind",
    literals={
            EnumerationLiteral(name="SIMPLE"),
			EnumerationLiteral(name="DOUBLE"),
			EnumerationLiteral(name="NONE")
    }
)

# Classes
aredsl_Editor = Class(name="aredsl::Editor")
aredsl_Layer = Class(name="aredsl::Layer")
aredsl_Node = Class(name="aredsl::Node")
aredsl_Edge = Class(name="aredsl::Edge")
aredsl_TrackerAction = Class(name="aredsl::TrackerAction", is_abstract=True)
aredsl_NodeStyle = Class(name="aredsl::NodeStyle", is_abstract=True)
aredsl_Label = Class(name="aredsl::Label")
aredsl_ToolSet = Class(name="aredsl::ToolSet")
aredsl_Model3DNodeStyle = Class(name="aredsl::Model3DNodeStyle")
NodeStyle = Class(name="NodeStyle")
aredsl_Image2DNodeStyle = Class(name="aredsl::Image2DNodeStyle")
aredsl_GeometricShapeNodeStyle = Class(name="aredsl::GeometricShapeNodeStyle")
aredsl_LabelStyle = Class(name="aredsl::LabelStyle")
aredsl_EdgeStyle = Class(name="aredsl::EdgeStyle")
aredsl_DomainOperation = Class(name="aredsl::DomainOperation", is_abstract=True)
Behaviour = Class(name="Behaviour")
aredsl_RemoveOperation = Class(name="aredsl::RemoveOperation")
aredsl_SetOperation = Class(name="aredsl::SetOperation")
aredsl_Tool = Class(name="aredsl::Tool")
aredsl_Behaviour = Class(name="aredsl::Behaviour", is_abstract=True)
aredsl_Action = Class(name="aredsl::Action", is_abstract=True)
aredsl_CreateInstanceOperation = Class(name="aredsl::CreateInstanceOperation")
DomainOperation = Class(name="DomainOperation")
aredsl_SensorBasedAction = Class(name="aredsl::SensorBasedAction")
Action = Class(name="Action")
aredsl_UnsetOperation = Class(name="aredsl::UnsetOperation")
aredsl_GestureAction = Class(name="aredsl::GestureAction")
aredsl_ChangeContextOperation = Class(name="aredsl::ChangeContextOperation")
aredsl_MarkerBasedTrackerAction = Class(name="aredsl::MarkerBasedTrackerAction")
TrackerAction = Class(name="TrackerAction")
aredsl_MarkerLessTrackerAction = Class(name="aredsl::MarkerLessTrackerAction")
aredsl_SupportOperation = Class(name="aredsl::SupportOperation", is_abstract=True)
aredsl_MoveElement = Class(name="aredsl::MoveElement")
SupportOperation = Class(name="SupportOperation")
aredsl_ShowSystemMenu = Class(name="aredsl::ShowSystemMenu")
aredsl_ArrangeElements = Class(name="aredsl::ArrangeElements")
aredsl_Exit = Class(name="aredsl::Exit")
aredsl_VoiceAction = Class(name="aredsl::VoiceAction")
aredsl_MentalAction = Class(name="aredsl::MentalAction")
aredsl_TactileAction = Class(name="aredsl::TactileAction")

# aredsl_Editor class attributes and methods
aredsl_Editor_description: Property = Property(name="description", type=StringType)
aredsl_Editor_fileExtension: Property = Property(name="fileExtension", type=StringType)
aredsl_Editor_name: Property = Property(name="name", type=StringType)
aredsl_Editor_queryLanguageKind: Property = Property(name="queryLanguageKind", type=StringType)
aredsl_Editor.attributes={aredsl_Editor_fileExtension, aredsl_Editor_name, aredsl_Editor_description, aredsl_Editor_queryLanguageKind}

# aredsl_Layer class attributes and methods
aredsl_Layer_id: Property = Property(name="id", type=StringType)
aredsl_Layer_semantics: Property = Property(name="semantics", type=StringType)
aredsl_Layer_description: Property = Property(name="description", type=StringType)
aredsl_Layer.attributes={aredsl_Layer_description, aredsl_Layer_semantics, aredsl_Layer_id}

# aredsl_Node class attributes and methods
aredsl_Node_id: Property = Property(name="id", type=StringType)
aredsl_Node_semantics: Property = Property(name="semantics", type=StringType)
aredsl_Node_contaimentKind: Property = Property(name="contaimentKind", type=StringType)
aredsl_Node_description: Property = Property(name="description", type=StringType)
aredsl_Node.attributes={aredsl_Node_id, aredsl_Node_semantics, aredsl_Node_description, aredsl_Node_contaimentKind}

# aredsl_Edge class attributes and methods
aredsl_Edge_id: Property = Property(name="id", type=StringType)
aredsl_Edge_originSemantics: Property = Property(name="originSemantics", type=StringType)
aredsl_Edge_destinationSemantics: Property = Property(name="destinationSemantics", type=StringType)
aredsl_Edge_description: Property = Property(name="description", type=StringType)
aredsl_Edge.attributes={aredsl_Edge_destinationSemantics, aredsl_Edge_description, aredsl_Edge_id, aredsl_Edge_originSemantics}

# aredsl_TrackerAction class attributes and methods

# aredsl_NodeStyle class attributes and methods
aredsl_NodeStyle_width: Property = Property(name="width", type=IntegerType)
aredsl_NodeStyle_height: Property = Property(name="height", type=IntegerType)
aredsl_NodeStyle_semanticCondition: Property = Property(name="semanticCondition", type=StringType)
aredsl_NodeStyle.attributes={aredsl_NodeStyle_height, aredsl_NodeStyle_width, aredsl_NodeStyle_semanticCondition}

# aredsl_Label class attributes and methods
aredsl_Label_id: Property = Property(name="id", type=StringType)
aredsl_Label_description: Property = Property(name="description", type=StringType)
aredsl_Label_semantics: Property = Property(name="semantics", type=StringType)
aredsl_Label.attributes={aredsl_Label_id, aredsl_Label_semantics, aredsl_Label_description}

# aredsl_ToolSet class attributes and methods
aredsl_ToolSet_id: Property = Property(name="id", type=StringType)
aredsl_ToolSet_description: Property = Property(name="description", type=StringType)
aredsl_ToolSet.attributes={aredsl_ToolSet_id, aredsl_ToolSet_description}

# aredsl_Model3DNodeStyle class attributes and methods
aredsl_Model3DNodeStyle_file: Property = Property(name="file", type=StringType)
aredsl_Model3DNodeStyle.attributes={aredsl_Model3DNodeStyle_file}

# NodeStyle class attributes and methods

# aredsl_Image2DNodeStyle class attributes and methods
aredsl_Image2DNodeStyle_file: Property = Property(name="file", type=StringType)
aredsl_Image2DNodeStyle.attributes={aredsl_Image2DNodeStyle_file}

# aredsl_GeometricShapeNodeStyle class attributes and methods
aredsl_GeometricShapeNodeStyle_color: Property = Property(name="color", type=StringType)
aredsl_GeometricShapeNodeStyle_kind: Property = Property(name="kind", type=StringType)
aredsl_GeometricShapeNodeStyle_outline: Property = Property(name="outline", type=StringType)
aredsl_GeometricShapeNodeStyle.attributes={aredsl_GeometricShapeNodeStyle_color, aredsl_GeometricShapeNodeStyle_kind, aredsl_GeometricShapeNodeStyle_outline}

# aredsl_LabelStyle class attributes and methods
aredsl_LabelStyle_color: Property = Property(name="color", type=StringType)
aredsl_LabelStyle_height: Property = Property(name="height", type=IntegerType)
aredsl_LabelStyle_semanticCondition: Property = Property(name="semanticCondition", type=StringType)
aredsl_LabelStyle.attributes={aredsl_LabelStyle_height, aredsl_LabelStyle_semanticCondition, aredsl_LabelStyle_color}

# aredsl_EdgeStyle class attributes and methods
aredsl_EdgeStyle_color: Property = Property(name="color", type=StringType)
aredsl_EdgeStyle_kind: Property = Property(name="kind", type=StringType)
aredsl_EdgeStyle_width: Property = Property(name="width", type=IntegerType)
aredsl_EdgeStyle_semanticCondition: Property = Property(name="semanticCondition", type=StringType)
aredsl_EdgeStyle.attributes={aredsl_EdgeStyle_width, aredsl_EdgeStyle_semanticCondition, aredsl_EdgeStyle_color, aredsl_EdgeStyle_kind}

# aredsl_DomainOperation class attributes and methods

# Behaviour class attributes and methods

# aredsl_RemoveOperation class attributes and methods
aredsl_RemoveOperation_constraint: Property = Property(name="constraint", type=StringType)
aredsl_RemoveOperation.attributes={aredsl_RemoveOperation_constraint}

# aredsl_SetOperation class attributes and methods
aredsl_SetOperation_feature: Property = Property(name="feature", type=StringType)
aredsl_SetOperation_value: Property = Property(name="value", type=StringType)
aredsl_SetOperation_constraint: Property = Property(name="constraint", type=StringType)
aredsl_SetOperation.attributes={aredsl_SetOperation_feature, aredsl_SetOperation_constraint, aredsl_SetOperation_value}

# aredsl_Tool class attributes and methods
aredsl_Tool_id: Property = Property(name="id", type=StringType)
aredsl_Tool_description: Property = Property(name="description", type=StringType)
aredsl_Tool_precondition: Property = Property(name="precondition", type=StringType)
aredsl_Tool_targetPrecondition: Property = Property(name="targetPrecondition", type=StringType)
aredsl_Tool.attributes={aredsl_Tool_description, aredsl_Tool_targetPrecondition, aredsl_Tool_id, aredsl_Tool_precondition}

# aredsl_Behaviour class attributes and methods
aredsl_Behaviour_description: Property = Property(name="description", type=StringType)
aredsl_Behaviour.attributes={aredsl_Behaviour_description}

# aredsl_Action class attributes and methods
aredsl_Action_description: Property = Property(name="description", type=StringType)
aredsl_Action.attributes={aredsl_Action_description}

# aredsl_CreateInstanceOperation class attributes and methods
aredsl_CreateInstanceOperation_name: Property = Property(name="name", type=StringType)
aredsl_CreateInstanceOperation_feature: Property = Property(name="feature", type=StringType)
aredsl_CreateInstanceOperation_type: Property = Property(name="type", type=StringType)
aredsl_CreateInstanceOperation.attributes={aredsl_CreateInstanceOperation_type, aredsl_CreateInstanceOperation_feature, aredsl_CreateInstanceOperation_name}

# DomainOperation class attributes and methods

# aredsl_SensorBasedAction class attributes and methods

# Action class attributes and methods

# aredsl_UnsetOperation class attributes and methods
aredsl_UnsetOperation_feature: Property = Property(name="feature", type=StringType)
aredsl_UnsetOperation_constraint: Property = Property(name="constraint", type=StringType)
aredsl_UnsetOperation.attributes={aredsl_UnsetOperation_feature, aredsl_UnsetOperation_constraint}

# aredsl_GestureAction class attributes and methods

# aredsl_ChangeContextOperation class attributes and methods
aredsl_ChangeContextOperation_expression: Property = Property(name="expression", type=StringType)
aredsl_ChangeContextOperation.attributes={aredsl_ChangeContextOperation_expression}

# aredsl_MarkerBasedTrackerAction class attributes and methods
aredsl_MarkerBasedTrackerAction_markerId: Property = Property(name="markerId", type=IntegerType)
aredsl_MarkerBasedTrackerAction.attributes={aredsl_MarkerBasedTrackerAction_markerId}

# TrackerAction class attributes and methods

# aredsl_MarkerLessTrackerAction class attributes and methods
aredsl_MarkerLessTrackerAction_file: Property = Property(name="file", type=StringType)
aredsl_MarkerLessTrackerAction.attributes={aredsl_MarkerLessTrackerAction_file}

# aredsl_SupportOperation class attributes and methods

# aredsl_MoveElement class attributes and methods

# SupportOperation class attributes and methods

# aredsl_ShowSystemMenu class attributes and methods

# aredsl_ArrangeElements class attributes and methods

# aredsl_Exit class attributes and methods

# aredsl_VoiceAction class attributes and methods

# aredsl_MentalAction class attributes and methods

# aredsl_TactileAction class attributes and methods

# Relationships
layer0: BinaryAssociation = BinaryAssociation(
    name="layer0",
    ends={
        Property(name="aredsl_Layer", type=aredsl_Editor, multiplicity=Multiplicity(1, 1)),
        Property(name="aredsl_Editor", type=aredsl_Layer, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
nodes3: BinaryAssociation = BinaryAssociation(
    name="nodes3",
    ends={
        Property(name="aredsl_Node", type=aredsl_Layer, multiplicity=Multiplicity(1, 1)),
        Property(name="aredsl_Layer4", type=aredsl_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edges5: BinaryAssociation = BinaryAssociation(
    name="edges5",
    ends={
        Property(name="aredsl_Edge", type=aredsl_Layer, multiplicity=Multiplicity(1, 1)),
        Property(name="aredsl_Layer6", type=aredsl_Edge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referenceAction7: BinaryAssociation = BinaryAssociation(
    name="referenceAction7",
    ends={
        Property(name="aredsl_TrackerAction", type=aredsl_Layer, multiplicity=Multiplicity(1, 1)),
        Property(name="aredsl_Layer8", type=aredsl_TrackerAction, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nodestyles9: BinaryAssociation = BinaryAssociation(
    name="nodestyles9",
    ends={
        Property(name="aredsl_NodeStyle", type=aredsl_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="aredsl_Node10", type=aredsl_NodeStyle, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
toolsets1: BinaryAssociation = BinaryAssociation(
    name="toolsets1",
    ends={
        Property(name="aredsl_ToolSet", type=aredsl_Editor, multiplicity=Multiplicity(1, 1)),
        Property(name="aredsl_Editor2", type=aredsl_ToolSet, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
label11: BinaryAssociation = BinaryAssociation(
    name="label11",
    ends={
        Property(name="aredsl_Label", type=aredsl_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="aredsl_Node12", type=aredsl_Label, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
contentNodes14: BinaryAssociation = BinaryAssociation(
    name="contentNodes14",
    ends={
        Property(name="aredsl_Node15", type=aredsl_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="aredsl_Node13", type=aredsl_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edgestyles18: BinaryAssociation = BinaryAssociation(
    name="edgestyles18",
    ends={
        Property(name="aredsl_EdgeStyle", type=aredsl_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="aredsl_Edge19", type=aredsl_EdgeStyle, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
middleLabel20: BinaryAssociation = BinaryAssociation(
    name="middleLabel20",
    ends={
        Property(name="aredsl_Label22", type=aredsl_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="aredsl_Edge21", type=aredsl_Label, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
originNode23: BinaryAssociation = BinaryAssociation(
    name="originNode23",
    ends={
        Property(name="aredsl_Node25", type=aredsl_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="aredsl_Edge24", type=aredsl_Node, multiplicity=Multiplicity(1, 1))
    }
)
labelstyles16: BinaryAssociation = BinaryAssociation(
    name="labelstyles16",
    ends={
        Property(name="aredsl_LabelStyle", type=aredsl_Label, multiplicity=Multiplicity(1, 1)),
        Property(name="aredsl_Label17", type=aredsl_LabelStyle, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
behaviours35: BinaryAssociation = BinaryAssociation(
    name="behaviours35",
    ends={
        Property(name="aredsl_Behaviour", type=aredsl_Tool, multiplicity=Multiplicity(1, 1)),
        Property(name="aredsl_Tool", type=aredsl_Behaviour, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
destinationNode26: BinaryAssociation = BinaryAssociation(
    name="destinationNode26",
    ends={
        Property(name="aredsl_Node28", type=aredsl_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="aredsl_Edge27", type=aredsl_Node, multiplicity=Multiplicity(1, 1))
    }
)
actions36: BinaryAssociation = BinaryAssociation(
    name="actions36",
    ends={
        Property(name="aredsl_Action", type=aredsl_Tool, multiplicity=Multiplicity(1, 1)),
        Property(name="aredsl_Tool37", type=aredsl_Action, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
originLabel29: BinaryAssociation = BinaryAssociation(
    name="originLabel29",
    ends={
        Property(name="aredsl_Label31", type=aredsl_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="aredsl_Edge30", type=aredsl_Label, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
destinationLabel32: BinaryAssociation = BinaryAssociation(
    name="destinationLabel32",
    ends={
        Property(name="aredsl_Label34", type=aredsl_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="aredsl_Edge33", type=aredsl_Label, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tools38: BinaryAssociation = BinaryAssociation(
    name="tools38",
    ends={
        Property(name="aredsl_Tool40", type=aredsl_ToolSet, multiplicity=Multiplicity(1, 1)),
        Property(name="aredsl_ToolSet39", type=aredsl_Tool, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_aredsl_Model3DNodeStyle_NodeStyle = Generalization(general=NodeStyle, specific=aredsl_Model3DNodeStyle)
gen_aredsl_Image2DNodeStyle_NodeStyle = Generalization(general=NodeStyle, specific=aredsl_Image2DNodeStyle)
gen_aredsl_GeometricShapeNodeStyle_NodeStyle = Generalization(general=NodeStyle, specific=aredsl_GeometricShapeNodeStyle)
gen_aredsl_DomainOperation_Behaviour = Generalization(general=Behaviour, specific=aredsl_DomainOperation)
gen_aredsl_RemoveOperation_DomainOperation = Generalization(general=DomainOperation, specific=aredsl_RemoveOperation)
gen_aredsl_SetOperation_DomainOperation = Generalization(general=DomainOperation, specific=aredsl_SetOperation)
gen_aredsl_CreateInstanceOperation_DomainOperation = Generalization(general=DomainOperation, specific=aredsl_CreateInstanceOperation)
gen_aredsl_MarkerLessTrackerAction_TrackerAction = Generalization(general=TrackerAction, specific=aredsl_MarkerLessTrackerAction)
gen_aredsl_SensorBasedAction_Action = Generalization(general=Action, specific=aredsl_SensorBasedAction)
gen_aredsl_UnsetOperation_DomainOperation = Generalization(general=DomainOperation, specific=aredsl_UnsetOperation)
gen_aredsl_ChangeContextOperation_DomainOperation = Generalization(general=DomainOperation, specific=aredsl_ChangeContextOperation)
gen_aredsl_MarkerBasedTrackerAction_TrackerAction = Generalization(general=TrackerAction, specific=aredsl_MarkerBasedTrackerAction)
gen_aredsl_SupportOperation_Behaviour = Generalization(general=Behaviour, specific=aredsl_SupportOperation)
gen_aredsl_MoveElement_SupportOperation = Generalization(general=SupportOperation, specific=aredsl_MoveElement)
gen_aredsl_ShowSystemMenu_SupportOperation = Generalization(general=SupportOperation, specific=aredsl_ShowSystemMenu)
gen_aredsl_ArrangeElements_SupportOperation = Generalization(general=SupportOperation, specific=aredsl_ArrangeElements)
gen_aredsl_Exit_SupportOperation = Generalization(general=SupportOperation, specific=aredsl_Exit)
gen_aredsl_GestureAction_Action = Generalization(general=Action, specific=aredsl_GestureAction)
gen_aredsl_VoiceAction_Action = Generalization(general=Action, specific=aredsl_VoiceAction)
gen_aredsl_TrackerAction_Action = Generalization(general=Action, specific=aredsl_TrackerAction)
gen_aredsl_MentalAction_Action = Generalization(general=Action, specific=aredsl_MentalAction)
gen_aredsl_TactileAction_Action = Generalization(general=Action, specific=aredsl_TactileAction)

# Domain Model
domain_model = DomainModel(
    name="aredsl",
    types={aredsl_Editor, aredsl_Layer, aredsl_Node, aredsl_Edge, aredsl_TrackerAction, aredsl_NodeStyle, aredsl_Label, aredsl_ToolSet, aredsl_Model3DNodeStyle, NodeStyle, aredsl_Image2DNodeStyle, aredsl_GeometricShapeNodeStyle, aredsl_LabelStyle, aredsl_EdgeStyle, aredsl_DomainOperation, Behaviour, aredsl_RemoveOperation, aredsl_SetOperation, aredsl_Tool, aredsl_Behaviour, aredsl_Action, aredsl_CreateInstanceOperation, DomainOperation, aredsl_SensorBasedAction, Action, aredsl_UnsetOperation, aredsl_GestureAction, aredsl_ChangeContextOperation, aredsl_MarkerBasedTrackerAction, TrackerAction, aredsl_MarkerLessTrackerAction, aredsl_SupportOperation, aredsl_MoveElement, SupportOperation, aredsl_ShowSystemMenu, aredsl_ArrangeElements, aredsl_Exit, aredsl_VoiceAction, aredsl_MentalAction, aredsl_TactileAction, LineKind, ShapeKind, ContainmentKind, IntegrityRestrictionKind, QueryLanguageKind, OutlineKind},
    associations={layer0, nodes3, edges5, referenceAction7, nodestyles9, toolsets1, label11, contentNodes14, edgestyles18, middleLabel20, originNode23, labelstyles16, behaviours35, destinationNode26, actions36, originLabel29, destinationLabel32, tools38},
    generalizations={gen_aredsl_Model3DNodeStyle_NodeStyle, gen_aredsl_Image2DNodeStyle_NodeStyle, gen_aredsl_GeometricShapeNodeStyle_NodeStyle, gen_aredsl_DomainOperation_Behaviour, gen_aredsl_RemoveOperation_DomainOperation, gen_aredsl_SetOperation_DomainOperation, gen_aredsl_CreateInstanceOperation_DomainOperation, gen_aredsl_MarkerLessTrackerAction_TrackerAction, gen_aredsl_SensorBasedAction_Action, gen_aredsl_UnsetOperation_DomainOperation, gen_aredsl_ChangeContextOperation_DomainOperation, gen_aredsl_MarkerBasedTrackerAction_TrackerAction, gen_aredsl_SupportOperation_Behaviour, gen_aredsl_MoveElement_SupportOperation, gen_aredsl_ShowSystemMenu_SupportOperation, gen_aredsl_ArrangeElements_SupportOperation, gen_aredsl_Exit_SupportOperation, gen_aredsl_GestureAction_Action, gen_aredsl_VoiceAction_Action, gen_aredsl_TrackerAction_Action, gen_aredsl_MentalAction_Action, gen_aredsl_TactileAction_Action},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)