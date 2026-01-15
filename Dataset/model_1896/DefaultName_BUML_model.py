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
Composition: Enumeration = Enumeration(
    name="Composition",
    literals={
            EnumerationLiteral(name="Sequential"),
			EnumerationLiteral(name="Atomic")
    }
)

Branch: Enumeration = Enumeration(
    name="Branch",
    literals={
            EnumerationLiteral(name="Parallel"),
			EnumerationLiteral(name="Alternative")
    }
)

BehaviorType: Enumeration = Enumeration(
    name="BehaviorType",
    literals={
            EnumerationLiteral(name="StateRealization"),
			EnumerationLiteral(name="Selection"),
			EnumerationLiteral(name="Guard"),
			EnumerationLiteral(name="InternalInput"),
			EnumerationLiteral(name="InternalOutput"),
			EnumerationLiteral(name="ExternalOutput"),
			EnumerationLiteral(name="ExternalInput")
    }
)

EventType: Enumeration = Enumeration(
    name="EventType",
    literals={
            EnumerationLiteral(name="InternalInput"),
			EnumerationLiteral(name="InternalOutput"),
			EnumerationLiteral(name="ExternalInput"),
			EnumerationLiteral(name="ExternalOutput")
    }
)

Operator: Enumeration = Enumeration(
    name="Operator",
    literals={
            EnumerationLiteral(name="Reference"),
			EnumerationLiteral(name="Reversion"),
			EnumerationLiteral(name="BranchKill"),
			EnumerationLiteral(name="Synchronize"),
			EnumerationLiteral(name="Conjunction"),
			EnumerationLiteral(name="Disjunction"),
			EnumerationLiteral(name="ExclusiveOR"),
			EnumerationLiteral(name="NoOperator")
    }
)

TraceabilityStatus: Enumeration = Enumeration(
    name="TraceabilityStatus",
    literals={
            EnumerationLiteral(name="Original"),
			EnumerationLiteral(name="Implied"),
			EnumerationLiteral(name="Missing"),
			EnumerationLiteral(name="Updated"),
			EnumerationLiteral(name="Deleted"),
			EnumerationLiteral(name="DesignRefinement")
    }
)

SpecialEdgeEnum: Enumeration = Enumeration(
    name="SpecialEdgeEnum",
    literals={
            EnumerationLiteral(name="Synchronize"),
			EnumerationLiteral(name="Reference"),
			EnumerationLiteral(name="Reversion"),
			EnumerationLiteral(name="BranchKill")
    }
)

# Classes
graphbt_ComponentList = Class(name="graphbt::ComponentList")
graphbt_RequirementList = Class(name="graphbt::RequirementList")
graphbt_FormulaList = Class(name="graphbt::FormulaList")
graphbt_Libraries = Class(name="graphbt::Libraries")
graphbt_StandardNode = Class(name="graphbt::StandardNode")
graphbt_BEModel = Class(name="graphbt::BEModel")
graphbt_BehaviorTree = Class(name="graphbt::BehaviorTree")
graphbt_Node = Class(name="graphbt::Node")
graphbt_Edge = Class(name="graphbt::Edge")
graphbt_SpecialEdge = Class(name="graphbt::SpecialEdge")
graphbt_LayoutList = Class(name="graphbt::LayoutList")
graphbt_AuthorList = Class(name="graphbt::AuthorList")
graphbt_Link = Class(name="graphbt::Link")
graphbt_EmptyNode = Class(name="graphbt::EmptyNode")
Node = Class(name="Node")
graphbt_Attribute = Class(name="graphbt::Attribute")
graphbt_State = Class(name="graphbt::State")
graphbt_Behavior = Class(name="graphbt::Behavior")
graphbt_Component = Class(name="graphbt::Component")
graphbt_CTEdge = Class(name="graphbt::CTEdge")
graphbt_MapInformation = Class(name="graphbt::MapInformation")
graphbt_Library = Class(name="graphbt::Library")
graphbt_Requirement = Class(name="graphbt::Requirement")
graphbt_MethodDeclaration = Class(name="graphbt::MethodDeclaration")
graphbt_Formula = Class(name="graphbt::Formula")
graphbt_OperatorClass = Class(name="graphbt::OperatorClass")
graphbt_TraceabilityStatusClass = Class(name="graphbt::TraceabilityStatusClass")
graphbt_Information = Class(name="graphbt::Information")
graphbt_InputType = Class(name="graphbt::InputType")
GUIImplementable = Class(name="GUIImplementable")
graphbt_OutputType = Class(name="graphbt::OutputType")
graphbt_GUIImplementable = Class(name="graphbt::GUIImplementable")
graphbt_GUI = Class(name="graphbt::GUI")
graphbt_InputGUI = Class(name="graphbt::InputGUI")
GUI = Class(name="GUI")
graphbt_OutputGUI = Class(name="graphbt::OutputGUI")
graphbt_AlternativeClass = Class(name="graphbt::AlternativeClass")
graphbt_Layout = Class(name="graphbt::Layout")
graphbt_Parameter = Class(name="graphbt::Parameter")
graphbt_Button = Class(name="graphbt::Button")
Layout = Class(name="Layout")
graphbt_Author = Class(name="graphbt::Author")

# graphbt_ComponentList class attributes and methods

# graphbt_RequirementList class attributes and methods
graphbt_RequirementList_projectId: Property = Property(name="projectId", type=StringType)
graphbt_RequirementList.attributes={graphbt_RequirementList_projectId}

# graphbt_FormulaList class attributes and methods

# graphbt_Libraries class attributes and methods

# graphbt_StandardNode class attributes and methods
graphbt_StandardNode_traceabilityStatus: Property = Property(name="traceabilityStatus", type=StringType)
graphbt_StandardNode_operator: Property = Property(name="operator", type=StringType)
graphbt_StandardNode_label: Property = Property(name="label", type=StringType)
graphbt_StandardNode_componentRef: Property = Property(name="componentRef", type=StringType)
graphbt_StandardNode_behaviorRef: Property = Property(name="behaviorRef", type=StringType)
graphbt_StandardNode_traceabilityLink: Property = Property(name="traceabilityLink", type=StringType)
graphbt_StandardNode_leaf: Property = Property(name="leaf", type=BooleanType)
graphbt_StandardNode.attributes={graphbt_StandardNode_componentRef, graphbt_StandardNode_operator, graphbt_StandardNode_label, graphbt_StandardNode_leaf, graphbt_StandardNode_behaviorRef, graphbt_StandardNode_traceabilityStatus, graphbt_StandardNode_traceabilityLink}

# graphbt_BEModel class attributes and methods
graphbt_BEModel_name: Property = Property(name="name", type=StringType)
graphbt_BEModel_subtitle: Property = Property(name="subtitle", type=StringType)
graphbt_BEModel_version: Property = Property(name="version", type=StringType)
graphbt_BEModel.attributes={graphbt_BEModel_version, graphbt_BEModel_name, graphbt_BEModel_subtitle}

# graphbt_BehaviorTree class attributes and methods
graphbt_BehaviorTree_name: Property = Property(name="name", type=StringType)
graphbt_BehaviorTree.attributes={graphbt_BehaviorTree_name}

# graphbt_Node class attributes and methods
graphbt_Node_index: Property = Property(name="index", type=IntegerType)
graphbt_Node_id: Property = Property(name="id", type=StringType)
graphbt_Node.attributes={graphbt_Node_index, graphbt_Node_id}

# graphbt_Edge class attributes and methods
graphbt_Edge_branch: Property = Property(name="branch", type=StringType)
graphbt_Edge_composition: Property = Property(name="composition", type=StringType)
graphbt_Edge.attributes={graphbt_Edge_branch, graphbt_Edge_composition}

# graphbt_SpecialEdge class attributes and methods
graphbt_SpecialEdge_type: Property = Property(name="type", type=StringType)
graphbt_SpecialEdge_destination: Property = Property(name="destination", type=IntegerType)
graphbt_SpecialEdge.attributes={graphbt_SpecialEdge_destination, graphbt_SpecialEdge_type}

# graphbt_LayoutList class attributes and methods

# graphbt_AuthorList class attributes and methods

# graphbt_Link class attributes and methods

# graphbt_EmptyNode class attributes and methods
graphbt_EmptyNode_label: Property = Property(name="label", type=StringType)
graphbt_EmptyNode.attributes={graphbt_EmptyNode_label}

# Node class attributes and methods

# graphbt_Attribute class attributes and methods
graphbt_Attribute_name: Property = Property(name="name", type=StringType)
graphbt_Attribute_value: Property = Property(name="value", type=StringType)
graphbt_Attribute_type: Property = Property(name="type", type=StringType)
graphbt_Attribute.attributes={graphbt_Attribute_name, graphbt_Attribute_type, graphbt_Attribute_value}

# graphbt_State class attributes and methods
graphbt_State_name: Property = Property(name="name", type=StringType)
graphbt_State_ref: Property = Property(name="ref", type=StringType)
graphbt_State_desc: Property = Property(name="desc", type=StringType)
graphbt_State.attributes={graphbt_State_desc, graphbt_State_name, graphbt_State_ref}

# graphbt_Behavior class attributes and methods
graphbt_Behavior_behaviorType: Property = Property(name="behaviorType", type=StringType)
graphbt_Behavior_behaviorName: Property = Property(name="behaviorName", type=StringType)
graphbt_Behavior_behaviorRef: Property = Property(name="behaviorRef", type=StringType)
graphbt_Behavior_behaviorDesc: Property = Property(name="behaviorDesc", type=StringType)
graphbt_Behavior_technicalDetail: Property = Property(name="technicalDetail", type=StringType)
graphbt_Behavior.attributes={graphbt_Behavior_behaviorDesc, graphbt_Behavior_behaviorRef, graphbt_Behavior_behaviorType, graphbt_Behavior_behaviorName, graphbt_Behavior_technicalDetail}

# graphbt_Component class attributes and methods
graphbt_Component_componentName: Property = Property(name="componentName", type=StringType)
graphbt_Component_id: Property = Property(name="id", type=IntegerType)
graphbt_Component_componentRef: Property = Property(name="componentRef", type=StringType)
graphbt_Component_componentDesc: Property = Property(name="componentDesc", type=StringType)
graphbt_Component_enumerated: Property = Property(name="enumerated", type=BooleanType)
graphbt_Component_m_getAttribute: Method = Method(name="getAttribute", parameters={Parameter(name='name')}, type=StringType)
graphbt_Component.attributes={graphbt_Component_componentRef, graphbt_Component_componentDesc, graphbt_Component_enumerated, graphbt_Component_componentName, graphbt_Component_id}
graphbt_Component.methods={graphbt_Component_m_getAttribute}

# graphbt_CTEdge class attributes and methods

# graphbt_MapInformation class attributes and methods
graphbt_MapInformation_m_getValue: Method = Method(name="getValue", parameters={Parameter(name='key')}, type=StringType)
graphbt_MapInformation_m_setValue: Method = Method(name="setValue", parameters={Parameter(name='value'), Parameter(name='key')})
graphbt_MapInformation.methods={graphbt_MapInformation_m_setValue, graphbt_MapInformation_m_getValue}

# graphbt_Library class attributes and methods
graphbt_Library_name: Property = Property(name="name", type=StringType)
graphbt_Library_text: Property = Property(name="text", type=StringType)
graphbt_Library_desc: Property = Property(name="desc", type=StringType)
graphbt_Library_location: Property = Property(name="location", type=StringType)
graphbt_Library_id: Property = Property(name="id", type=StringType)
graphbt_Library.attributes={graphbt_Library_location, graphbt_Library_text, graphbt_Library_desc, graphbt_Library_name, graphbt_Library_id}

# graphbt_Requirement class attributes and methods
graphbt_Requirement_Key: Property = Property(name="Key", type=StringType)
graphbt_Requirement_Requirement: Property = Property(name="Requirement", type=StringType)
graphbt_Requirement_Description: Property = Property(name="Description", type=StringType)
graphbt_Requirement_Id: Property = Property(name="Id", type=StringType)
graphbt_Requirement.attributes={graphbt_Requirement_Requirement, graphbt_Requirement_Description, graphbt_Requirement_Key, graphbt_Requirement_Id}

# graphbt_MethodDeclaration class attributes and methods
graphbt_MethodDeclaration_type: Property = Property(name="type", type=StringType)
graphbt_MethodDeclaration_name: Property = Property(name="name", type=StringType)
graphbt_MethodDeclaration.attributes={graphbt_MethodDeclaration_name, graphbt_MethodDeclaration_type}

# graphbt_Formula class attributes and methods
graphbt_Formula_formulaName: Property = Property(name="formulaName", type=StringType)
graphbt_Formula.attributes={graphbt_Formula_formulaName}

# graphbt_OperatorClass class attributes and methods
graphbt_OperatorClass_operatorLiteral: Property = Property(name="operatorLiteral", type=StringType)
graphbt_OperatorClass.attributes={graphbt_OperatorClass_operatorLiteral}

# graphbt_TraceabilityStatusClass class attributes and methods
graphbt_TraceabilityStatusClass_traceabilityStatusLiteral: Property = Property(name="traceabilityStatusLiteral", type=StringType)
graphbt_TraceabilityStatusClass.attributes={graphbt_TraceabilityStatusClass_traceabilityStatusLiteral}

# graphbt_Information class attributes and methods
graphbt_Information_key: Property = Property(name="key", type=StringType)
graphbt_Information_value: Property = Property(name="value", type=StringType)
graphbt_Information.attributes={graphbt_Information_value, graphbt_Information_key}

# graphbt_InputType class attributes and methods

# GUIImplementable class attributes and methods

# graphbt_OutputType class attributes and methods

# graphbt_GUIImplementable class attributes and methods

# graphbt_GUI class attributes and methods
graphbt_GUI_identifier: Property = Property(name="identifier", type=StringType)
graphbt_GUI_codeImplementation: Property = Property(name="codeImplementation", type=StringType)
graphbt_GUI.attributes={graphbt_GUI_codeImplementation, graphbt_GUI_identifier}

# graphbt_InputGUI class attributes and methods

# GUI class attributes and methods

# graphbt_OutputGUI class attributes and methods

# graphbt_AlternativeClass class attributes and methods
graphbt_AlternativeClass_alternativeAttribute: Property = Property(name="alternativeAttribute", type=StringType)
graphbt_AlternativeClass.attributes={graphbt_AlternativeClass_alternativeAttribute}

# graphbt_Layout class attributes and methods
graphbt_Layout_cRef: Property = Property(name="cRef", type=StringType)
graphbt_Layout_x: Property = Property(name="x", type=IntegerType)
graphbt_Layout_y: Property = Property(name="y", type=IntegerType)
graphbt_Layout_width: Property = Property(name="width", type=IntegerType)
graphbt_Layout_height: Property = Property(name="height", type=IntegerType)
graphbt_Layout_z: Property = Property(name="z", type=IntegerType)
graphbt_Layout.attributes={graphbt_Layout_height, graphbt_Layout_z, graphbt_Layout_y, graphbt_Layout_cRef, graphbt_Layout_width, graphbt_Layout_x}

# graphbt_Parameter class attributes and methods
graphbt_Parameter_name: Property = Property(name="name", type=StringType)
graphbt_Parameter_type: Property = Property(name="type", type=StringType)
graphbt_Parameter.attributes={graphbt_Parameter_type, graphbt_Parameter_name}

# graphbt_Button class attributes and methods
graphbt_Button_label: Property = Property(name="label", type=StringType)
graphbt_Button.attributes={graphbt_Button_label}

# Layout class attributes and methods

# graphbt_Author class attributes and methods
graphbt_Author_name: Property = Property(name="name", type=StringType)
graphbt_Author_contact: Property = Property(name="contact", type=StringType)
graphbt_Author_role: Property = Property(name="role", type=StringType)
graphbt_Author.attributes={graphbt_Author_name, graphbt_Author_contact, graphbt_Author_role}

# Relationships
componentList1: BinaryAssociation = BinaryAssociation(
    name="componentList1",
    ends={
        Property(name="graphbt_ComponentList", type=graphbt_BEModel, multiplicity=Multiplicity(1, 1)),
        Property(name="graphbt_BEModel2", type=graphbt_ComponentList, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
requirementList3: BinaryAssociation = BinaryAssociation(
    name="requirementList3",
    ends={
        Property(name="graphbt_RequirementList", type=graphbt_BEModel, multiplicity=Multiplicity(1, 1)),
        Property(name="graphbt_BEModel4", type=graphbt_RequirementList, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
formulaList5: BinaryAssociation = BinaryAssociation(
    name="formulaList5",
    ends={
        Property(name="graphbt_FormulaList", type=graphbt_BEModel, multiplicity=Multiplicity(1, 1)),
        Property(name="graphbt_BEModel6", type=graphbt_FormulaList, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
libraries7: BinaryAssociation = BinaryAssociation(
    name="libraries7",
    ends={
        Property(name="graphbt_Libraries", type=graphbt_BEModel, multiplicity=Multiplicity(1, 1)),
        Property(name="graphbt_BEModel8", type=graphbt_Libraries, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
reversionNode9: BinaryAssociation = BinaryAssociation(
    name="reversionNode9",
    ends={
        Property(name="graphbt_StandardNode", type=graphbt_BEModel, multiplicity=Multiplicity(1, 1)),
        Property(name="graphbt_BEModel10", type=graphbt_StandardNode, multiplicity=Multiplicity(0, 9999))
    }
)
errorReversionNode11: BinaryAssociation = BinaryAssociation(
    name="errorReversionNode11",
    ends={
        Property(name="graphbt_StandardNode13", type=graphbt_BEModel, multiplicity=Multiplicity(1, 1)),
        Property(name="graphbt_BEModel12", type=graphbt_StandardNode, multiplicity=Multiplicity(0, 9999))
    }
)
dbt0: BinaryAssociation = BinaryAssociation(
    name="dbt0",
    ends={
        Property(name="graphbt_BehaviorTree", type=graphbt_BEModel, multiplicity=Multiplicity(1, 1)),
        Property(name="graphbt_BEModel", type=graphbt_BehaviorTree, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rootNode18: BinaryAssociation = BinaryAssociation(
    name="rootNode18",
    ends={
        Property(name="graphbt_Node", type=graphbt_BehaviorTree, multiplicity=Multiplicity(1, 1)),
        Property(name="graphbt_BehaviorTree19", type=graphbt_Node, multiplicity=Multiplicity(1, 1))
    }
)
edge20: BinaryAssociation = BinaryAssociation(
    name="edge20",
    ends={
        Property(name="graphbt_Edge", type=graphbt_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="graphbt_Node21", type=graphbt_Edge, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
specialE22: BinaryAssociation = BinaryAssociation(
    name="specialE22",
    ends={
        Property(name="graphbt_SpecialEdge", type=graphbt_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="graphbt_Node23", type=graphbt_SpecialEdge, multiplicity=Multiplicity(0, 1))
    }
)
layoutList14: BinaryAssociation = BinaryAssociation(
    name="layoutList14",
    ends={
        Property(name="graphbt_LayoutList", type=graphbt_BEModel, multiplicity=Multiplicity(1, 1)),
        Property(name="graphbt_BEModel15", type=graphbt_LayoutList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
authorList16: BinaryAssociation = BinaryAssociation(
    name="authorList16",
    ends={
        Property(name="graphbt_AuthorList", type=graphbt_BEModel, multiplicity=Multiplicity(1, 1)),
        Property(name="graphbt_BEModel17", type=graphbt_AuthorList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
childNode24: BinaryAssociation = BinaryAssociation(
    name="childNode24",
    ends={
        Property(name="graphbt_Link", type=graphbt_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="graphbt_Edge25", type=graphbt_Link, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
container26: BinaryAssociation = BinaryAssociation(
    name="container26",
    ends={
        Property(name="graphbt_Node28", type=graphbt_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="graphbt_Edge27", type=graphbt_Node, multiplicity=Multiplicity(0, 1))
    }
)
parent30: BinaryAssociation = BinaryAssociation(
    name="parent30",
    ends={
        Property(name="graphbt_StandardNode31", type=graphbt_StandardNode, multiplicity=Multiplicity(1, 1)),
        Property(name="graphbt_StandardNode29", type=graphbt_StandardNode, multiplicity=Multiplicity(0, 1))
    }
)
attributes32: BinaryAssociation = BinaryAssociation(
    name="attributes32",
    ends={
        Property(name="graphbt_Attribute", type=graphbt_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="graphbt_Component", type=graphbt_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
state33: BinaryAssociation = BinaryAssociation(
    name="state33",
    ends={
        Property(name="graphbt_State", type=graphbt_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="graphbt_Component34", type=graphbt_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initialState35: BinaryAssociation = BinaryAssociation(
    name="initialState35",
    ends={
        Property(name="graphbt_State37", type=graphbt_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="graphbt_Component36", type=graphbt_State, multiplicity=Multiplicity(0, 1))
    }
)
relatedTo39: BinaryAssociation = BinaryAssociation(
    name="relatedTo39",
    ends={
        Property(name="graphbt_Component40", type=graphbt_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="graphbt_Component38", type=graphbt_Component, multiplicity=Multiplicity(0, 9999))
    }
)
behaviors41: BinaryAssociation = BinaryAssociation(
    name="behaviors41",
    ends={
        Property(name="graphbt_Behavior", type=graphbt_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="graphbt_Component42", type=graphbt_Behavior, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributes45: BinaryAssociation = BinaryAssociation(
    name="attributes45",
    ends={
        Property(name="graphbt_MapInformation", type=graphbt_State, multiplicity=Multiplicity(1, 1)),
        Property(name="graphbt_State46", type=graphbt_MapInformation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
uses43: BinaryAssociation = BinaryAssociation(
    name="uses43",
    ends={
        Property(name="graphbt_Library", type=graphbt_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="graphbt_Component44", type=graphbt_Library, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributes55: BinaryAssociation = BinaryAssociation(
    name="attributes55",
    ends={
        Property(name="graphbt_Attribute57", type=graphbt_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="graphbt_Library56", type=graphbt_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
traceabilityLink58: BinaryAssociation = BinaryAssociation(
    name="traceabilityLink58",
    ends={
        Property(name="graphbt_StandardNode59", type=graphbt_Requirement, multiplicity=Multiplicity(1, 1)),
        Property(name="graphbt_Requirement", type=graphbt_StandardNode, multiplicity=Multiplicity(0, 9999))
    }
)
methods47: BinaryAssociation = BinaryAssociation(
    name="methods47",
    ends={
        Property(name="graphbt_MethodDeclaration", type=graphbt_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="graphbt_Library48", type=graphbt_MethodDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
states49: BinaryAssociation = BinaryAssociation(
    name="states49",
    ends={
        Property(name="graphbt_State51", type=graphbt_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="graphbt_Library50", type=graphbt_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
behaviors52: BinaryAssociation = BinaryAssociation(
    name="behaviors52",
    ends={
        Property(name="graphbt_Behavior54", type=graphbt_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="graphbt_Library53", type=graphbt_Behavior, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
formula66: BinaryAssociation = BinaryAssociation(
    name="formula66",
    ends={
        Property(name="graphbt_Formula", type=graphbt_FormulaList, multiplicity=Multiplicity(1, 1)),
        Property(name="graphbt_FormulaList67", type=graphbt_Formula, multiplicity=Multiplicity(0, 9999))
    }
)
target68: BinaryAssociation = BinaryAssociation(
    name="target68",
    ends={
        Property(name="graphbt_Node70", type=graphbt_Link, multiplicity=Multiplicity(1, 1)),
        Property(name="graphbt_Link69", type=graphbt_Node, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
source71: BinaryAssociation = BinaryAssociation(
    name="source71",
    ends={
        Property(name="graphbt_Node73", type=graphbt_Link, multiplicity=Multiplicity(1, 1)),
        Property(name="graphbt_Link72", type=graphbt_Node, multiplicity=Multiplicity(0, 1))
    }
)
components60: BinaryAssociation = BinaryAssociation(
    name="components60",
    ends={
        Property(name="graphbt_Component62", type=graphbt_ComponentList, multiplicity=Multiplicity(1, 1)),
        Property(name="graphbt_ComponentList61", type=graphbt_Component, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
requirements63: BinaryAssociation = BinaryAssociation(
    name="requirements63",
    ends={
        Property(name="graphbt_Requirement65", type=graphbt_RequirementList, multiplicity=Multiplicity(1, 1)),
        Property(name="graphbt_RequirementList64", type=graphbt_Requirement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
info74: BinaryAssociation = BinaryAssociation(
    name="info74",
    ends={
        Property(name="graphbt_Information", type=graphbt_MapInformation, multiplicity=Multiplicity(1, 1)),
        Property(name="graphbt_MapInformation75", type=graphbt_Information, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
layouts81: BinaryAssociation = BinaryAssociation(
    name="layouts81",
    ends={
        Property(name="graphbt_Layout", type=graphbt_LayoutList, multiplicity=Multiplicity(1, 1)),
        Property(name="graphbt_LayoutList82", type=graphbt_Layout, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
import76: BinaryAssociation = BinaryAssociation(
    name="import76",
    ends={
        Property(name="graphbt_Library78", type=graphbt_Libraries, multiplicity=Multiplicity(1, 1)),
        Property(name="graphbt_Libraries77", type=graphbt_Library, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters79: BinaryAssociation = BinaryAssociation(
    name="parameters79",
    ends={
        Property(name="graphbt_Parameter", type=graphbt_MethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="graphbt_MethodDeclaration80", type=graphbt_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
authors83: BinaryAssociation = BinaryAssociation(
    name="authors83",
    ends={
        Property(name="graphbt_Author", type=graphbt_AuthorList, multiplicity=Multiplicity(1, 1)),
        Property(name="graphbt_AuthorList84", type=graphbt_Author, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_graphbt_EmptyNode_Node = Generalization(general=Node, specific=graphbt_EmptyNode)
gen_graphbt_StandardNode_Node = Generalization(general=Node, specific=graphbt_StandardNode)
gen_graphbt_InputType_GUIImplementable = Generalization(general=GUIImplementable, specific=graphbt_InputType)
gen_graphbt_OutputType_GUIImplementable = Generalization(general=GUIImplementable, specific=graphbt_OutputType)
gen_graphbt_InputGUI_GUI = Generalization(general=GUI, specific=graphbt_InputGUI)
gen_graphbt_OutputGUI_GUI = Generalization(general=GUI, specific=graphbt_OutputGUI)
gen_graphbt_Button_Layout = Generalization(general=Layout, specific=graphbt_Button)

# Domain Model
domain_model = DomainModel(
    name="graphbt",
    types={graphbt_ComponentList, graphbt_RequirementList, graphbt_FormulaList, graphbt_Libraries, graphbt_StandardNode, graphbt_BEModel, graphbt_BehaviorTree, graphbt_Node, graphbt_Edge, graphbt_SpecialEdge, graphbt_LayoutList, graphbt_AuthorList, graphbt_Link, graphbt_EmptyNode, Node, graphbt_Attribute, graphbt_State, graphbt_Behavior, graphbt_Component, graphbt_CTEdge, graphbt_MapInformation, graphbt_Library, graphbt_Requirement, graphbt_MethodDeclaration, graphbt_Formula, graphbt_OperatorClass, graphbt_TraceabilityStatusClass, graphbt_Information, graphbt_InputType, GUIImplementable, graphbt_OutputType, graphbt_GUIImplementable, graphbt_GUI, graphbt_InputGUI, GUI, graphbt_OutputGUI, graphbt_AlternativeClass, graphbt_Layout, graphbt_Parameter, graphbt_Button, Layout, graphbt_Author, Composition, Branch, BehaviorType, EventType, Operator, TraceabilityStatus, SpecialEdgeEnum},
    associations={componentList1, requirementList3, formulaList5, libraries7, reversionNode9, errorReversionNode11, dbt0, rootNode18, edge20, specialE22, layoutList14, authorList16, childNode24, container26, parent30, attributes32, state33, initialState35, relatedTo39, behaviors41, attributes45, uses43, attributes55, traceabilityLink58, methods47, states49, behaviors52, formula66, target68, source71, components60, requirements63, info74, layouts81, import76, parameters79, authors83},
    generalizations={gen_graphbt_EmptyNode_Node, gen_graphbt_StandardNode_Node, gen_graphbt_InputType_GUIImplementable, gen_graphbt_OutputType_GUIImplementable, gen_graphbt_InputGUI_GUI, gen_graphbt_OutputGUI_GUI, gen_graphbt_Button_Layout},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)