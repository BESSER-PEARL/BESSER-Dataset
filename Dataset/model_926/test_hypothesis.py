import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    MethodConfiguration,
    uma_ProcessFamily,
    GraphicPrimitive,
    uma_Ellipse,
    uma_Polyline,
    LeafElement,
    uma_Image,
    uma_GraphicPrimitive,
    uma_TextElement,
    SemanticModelBridge,
    uma_CoreSemanticModelBridge,
    uma_UMASemanticModelBridge,
    uma_SimpleSemanticModelElement,
    GraphElement,
    uma_GraphEdge,
    uma_GraphNode,
    uma_Point,
    GraphNode,
    uma_Diagram,
    ProcessPackage,
    uma_GraphConnector,
    DiagramElement,
    uma_SemanticModelBridge,
    uma_Reference,
    uma_DiagramLink,
    uma_Property,
    uma_LeafElement,
    uma_GraphElement,
    uma_Dimension,
    ProcessDescription,
    uma_DeliveryProcessDescription,
    BreakdownElementDescription,
    uma_ActivityDescription,
    uma_DescriptorDescription,
    ActivityDescription,
    uma_ProcessDescription,
    Process,
    uma_CapabilityPattern,
    uma_ProcessPlanningTemplate,
    uma_DeliveryProcess,
    RoleDescriptor,
    uma_CompositeRole,
    Descriptor,
    uma_ProcessComponentDescriptor,
    uma_WorkProductDescriptor,
    uma_RoleDescriptor,
    Activity,
    uma_Phase,
    uma_Process,
    uma_Iteration,
    MethodPackage,
    uma_ProcessPackage,
    uma_ContentPackage,
    Package,
    ProcessElement,
    uma_WorkOrder,
    BreakdownElement,
    uma_TeamProfile,
    uma_Descriptor,
    uma_ProcessComponentInterface,
    uma_WorkBreakdownElement,
    uma_BreakdownElement,
    WorkBreakdownElement,
    uma_Milestone,
    uma_TaskDescriptor,
    uma_PlanningData,
    ContentCategory,
    uma_RoleSetGrouping,
    uma_Tool,
    uma_CustomCategory,
    uma_Domain,
    uma_DisciplineGrouping,
    uma_WorkProductType,
    uma_RoleSet,
    uma_Discipline,
    ContentDescription,
    uma_TaskDescription,
    uma_RoleDescription,
    uma_BreakdownElementDescription,
    uma_WorkProductDescription,
    uma_PracticeDescription,
    uma_GuidanceDescription,
    Concept,
    uma_Whitepaper,
    WorkDefinition,
    Section,
    uma_Step,
    WorkProductDescription,
    uma_DeliverableDescription,
    uma_ArtifactDescription,
    FulfillableElement,
    WorkProduct,
    uma_Deliverable,
    uma_Outcome,
    uma_Artifact,
    MethodUnit,
    uma_ProcessComponent,
    uma_MethodLibrary,
    uma_MethodPlugin,
    uma_MethodConfiguration,
    uma_ContentDescription,
    Classifier,
    Guidance,
    uma_ReusableAsset,
    uma_TermDefinition,
    uma_Report,
    uma_Practice,
    uma_Roadmap,
    uma_EstimationConsiderations,
    uma_ToolMentor,
    uma_Template,
    uma_Example,
    uma_Guideline,
    uma_Checklist,
    uma_Concept,
    uma_SupportingMaterial,
    VariabilityElement,
    uma_Activity,
    uma_Section,
    DescribableElement,
    uma_FulfillableElement,
    uma_ProcessElement,
    uma_ContentElement,
    uma_ApplicableMetaClassInfo,
    ContentElement,
    uma_Guidance,
    uma_Kind,
    uma_ContentCategory,
    uma_WorkProduct,
    uma_Task,
    uma_Role,
    uma_Element,
    Element,
    uma_NamedElement,
    NamedElement,
    uma_PackageableElement,
    PackageableElement,
    uma_MethodElementProperty,
    uma_MethodElement,
    uma_Type,
    Type,
    uma_Classifier,
    MethodElement,
    uma_DiagramElement,
    uma_WorkDefinition,
    uma_MethodUnit,
    uma_DescribableElement,
    uma_VariabilityElement,
    uma_MethodPackage,
    uma_Constraint,
    uma_Namespace,
    Namespace,
    uma_Package,
    WorkOrderType,
    VariabilityType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_methodconfiguration_is_not_abstract():
    assert not inspect.isabstract(MethodConfiguration)


def test_methodconfiguration_constructor_exists():
    assert callable(MethodConfiguration.__init__)


def test_methodconfiguration_constructor_args():
    sig = inspect.signature(MethodConfiguration.__init__)
    params = list(sig.parameters.keys())



def test_uma_processfamily_is_not_abstract():
    assert not inspect.isabstract(uma_ProcessFamily)


def test_uma_processfamily_constructor_exists():
    assert callable(uma_ProcessFamily.__init__)


def test_uma_processfamily_constructor_args():
    sig = inspect.signature(uma_ProcessFamily.__init__)
    params = list(sig.parameters.keys())



def test_graphicprimitive_is_not_abstract():
    assert not inspect.isabstract(GraphicPrimitive)


def test_graphicprimitive_constructor_exists():
    assert callable(GraphicPrimitive.__init__)


def test_graphicprimitive_constructor_args():
    sig = inspect.signature(GraphicPrimitive.__init__)
    params = list(sig.parameters.keys())



def test_uma_ellipse_is_not_abstract():
    assert not inspect.isabstract(uma_Ellipse)


def test_uma_ellipse_constructor_exists():
    assert callable(uma_Ellipse.__init__)


def test_uma_ellipse_constructor_args():
    sig = inspect.signature(uma_Ellipse.__init__)
    params = list(sig.parameters.keys())
    assert "startAngle" in params, "Missing parameter 'startAngle'"
    assert "radiusY" in params, "Missing parameter 'radiusY'"
    assert "endAngle" in params, "Missing parameter 'endAngle'"
    assert "rotation" in params, "Missing parameter 'rotation'"
    assert "radiusX" in params, "Missing parameter 'radiusX'"

def test_uma_ellipse_has_startAngle():
    assert hasattr(uma_Ellipse, "startAngle")
    descriptor = None
    for klass in uma_Ellipse.__mro__:
        if "startAngle" in klass.__dict__:
            descriptor = klass.__dict__["startAngle"]
            break
    assert isinstance(descriptor, property)

def test_uma_ellipse_has_radiusY():
    assert hasattr(uma_Ellipse, "radiusY")
    descriptor = None
    for klass in uma_Ellipse.__mro__:
        if "radiusY" in klass.__dict__:
            descriptor = klass.__dict__["radiusY"]
            break
    assert isinstance(descriptor, property)

def test_uma_ellipse_has_endAngle():
    assert hasattr(uma_Ellipse, "endAngle")
    descriptor = None
    for klass in uma_Ellipse.__mro__:
        if "endAngle" in klass.__dict__:
            descriptor = klass.__dict__["endAngle"]
            break
    assert isinstance(descriptor, property)

def test_uma_ellipse_has_rotation():
    assert hasattr(uma_Ellipse, "rotation")
    descriptor = None
    for klass in uma_Ellipse.__mro__:
        if "rotation" in klass.__dict__:
            descriptor = klass.__dict__["rotation"]
            break
    assert isinstance(descriptor, property)

def test_uma_ellipse_has_radiusX():
    assert hasattr(uma_Ellipse, "radiusX")
    descriptor = None
    for klass in uma_Ellipse.__mro__:
        if "radiusX" in klass.__dict__:
            descriptor = klass.__dict__["radiusX"]
            break
    assert isinstance(descriptor, property)



def test_uma_polyline_is_not_abstract():
    assert not inspect.isabstract(uma_Polyline)


def test_uma_polyline_constructor_exists():
    assert callable(uma_Polyline.__init__)


def test_uma_polyline_constructor_args():
    sig = inspect.signature(uma_Polyline.__init__)
    params = list(sig.parameters.keys())
    assert "closed" in params, "Missing parameter 'closed'"

def test_uma_polyline_has_closed():
    assert hasattr(uma_Polyline, "closed")
    descriptor = None
    for klass in uma_Polyline.__mro__:
        if "closed" in klass.__dict__:
            descriptor = klass.__dict__["closed"]
            break
    assert isinstance(descriptor, property)



def test_leafelement_is_not_abstract():
    assert not inspect.isabstract(LeafElement)


def test_leafelement_constructor_exists():
    assert callable(LeafElement.__init__)


def test_leafelement_constructor_args():
    sig = inspect.signature(LeafElement.__init__)
    params = list(sig.parameters.keys())



def test_uma_image_is_not_abstract():
    assert not inspect.isabstract(uma_Image)


def test_uma_image_constructor_exists():
    assert callable(uma_Image.__init__)


def test_uma_image_constructor_args():
    sig = inspect.signature(uma_Image.__init__)
    params = list(sig.parameters.keys())
    assert "uri" in params, "Missing parameter 'uri'"
    assert "mimeType" in params, "Missing parameter 'mimeType'"

def test_uma_image_has_uri():
    assert hasattr(uma_Image, "uri")
    descriptor = None
    for klass in uma_Image.__mro__:
        if "uri" in klass.__dict__:
            descriptor = klass.__dict__["uri"]
            break
    assert isinstance(descriptor, property)

def test_uma_image_has_mimeType():
    assert hasattr(uma_Image, "mimeType")
    descriptor = None
    for klass in uma_Image.__mro__:
        if "mimeType" in klass.__dict__:
            descriptor = klass.__dict__["mimeType"]
            break
    assert isinstance(descriptor, property)



def test_uma_graphicprimitive_is_not_abstract():
    assert not inspect.isabstract(uma_GraphicPrimitive)


def test_uma_graphicprimitive_constructor_exists():
    assert callable(uma_GraphicPrimitive.__init__)


def test_uma_graphicprimitive_constructor_args():
    sig = inspect.signature(uma_GraphicPrimitive.__init__)
    params = list(sig.parameters.keys())



def test_uma_textelement_is_not_abstract():
    assert not inspect.isabstract(uma_TextElement)


def test_uma_textelement_constructor_exists():
    assert callable(uma_TextElement.__init__)


def test_uma_textelement_constructor_args():
    sig = inspect.signature(uma_TextElement.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_uma_textelement_has_text():
    assert hasattr(uma_TextElement, "text")
    descriptor = None
    for klass in uma_TextElement.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_semanticmodelbridge_is_not_abstract():
    assert not inspect.isabstract(SemanticModelBridge)


def test_semanticmodelbridge_constructor_exists():
    assert callable(SemanticModelBridge.__init__)


def test_semanticmodelbridge_constructor_args():
    sig = inspect.signature(SemanticModelBridge.__init__)
    params = list(sig.parameters.keys())



def test_uma_coresemanticmodelbridge_is_not_abstract():
    assert not inspect.isabstract(uma_CoreSemanticModelBridge)


def test_uma_coresemanticmodelbridge_constructor_exists():
    assert callable(uma_CoreSemanticModelBridge.__init__)


def test_uma_coresemanticmodelbridge_constructor_args():
    sig = inspect.signature(uma_CoreSemanticModelBridge.__init__)
    params = list(sig.parameters.keys())



def test_uma_umasemanticmodelbridge_is_not_abstract():
    assert not inspect.isabstract(uma_UMASemanticModelBridge)


def test_uma_umasemanticmodelbridge_constructor_exists():
    assert callable(uma_UMASemanticModelBridge.__init__)


def test_uma_umasemanticmodelbridge_constructor_args():
    sig = inspect.signature(uma_UMASemanticModelBridge.__init__)
    params = list(sig.parameters.keys())



def test_uma_simplesemanticmodelelement_is_not_abstract():
    assert not inspect.isabstract(uma_SimpleSemanticModelElement)


def test_uma_simplesemanticmodelelement_constructor_exists():
    assert callable(uma_SimpleSemanticModelElement.__init__)


def test_uma_simplesemanticmodelelement_constructor_args():
    sig = inspect.signature(uma_SimpleSemanticModelElement.__init__)
    params = list(sig.parameters.keys())
    assert "typeInfo" in params, "Missing parameter 'typeInfo'"

def test_uma_simplesemanticmodelelement_has_typeInfo():
    assert hasattr(uma_SimpleSemanticModelElement, "typeInfo")
    descriptor = None
    for klass in uma_SimpleSemanticModelElement.__mro__:
        if "typeInfo" in klass.__dict__:
            descriptor = klass.__dict__["typeInfo"]
            break
    assert isinstance(descriptor, property)



def test_graphelement_is_not_abstract():
    assert not inspect.isabstract(GraphElement)


def test_graphelement_constructor_exists():
    assert callable(GraphElement.__init__)


def test_graphelement_constructor_args():
    sig = inspect.signature(GraphElement.__init__)
    params = list(sig.parameters.keys())



def test_uma_graphedge_is_not_abstract():
    assert not inspect.isabstract(uma_GraphEdge)


def test_uma_graphedge_constructor_exists():
    assert callable(uma_GraphEdge.__init__)


def test_uma_graphedge_constructor_args():
    sig = inspect.signature(uma_GraphEdge.__init__)
    params = list(sig.parameters.keys())



def test_uma_graphnode_is_not_abstract():
    assert not inspect.isabstract(uma_GraphNode)


def test_uma_graphnode_constructor_exists():
    assert callable(uma_GraphNode.__init__)


def test_uma_graphnode_constructor_args():
    sig = inspect.signature(uma_GraphNode.__init__)
    params = list(sig.parameters.keys())



def test_uma_point_is_not_abstract():
    assert not inspect.isabstract(uma_Point)


def test_uma_point_constructor_exists():
    assert callable(uma_Point.__init__)


def test_uma_point_constructor_args():
    sig = inspect.signature(uma_Point.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"
    assert "y" in params, "Missing parameter 'y'"

def test_uma_point_has_x():
    assert hasattr(uma_Point, "x")
    descriptor = None
    for klass in uma_Point.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_uma_point_has_y():
    assert hasattr(uma_Point, "y")
    descriptor = None
    for klass in uma_Point.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)



def test_graphnode_is_not_abstract():
    assert not inspect.isabstract(GraphNode)


def test_graphnode_constructor_exists():
    assert callable(GraphNode.__init__)


def test_graphnode_constructor_args():
    sig = inspect.signature(GraphNode.__init__)
    params = list(sig.parameters.keys())



def test_uma_diagram_is_not_abstract():
    assert not inspect.isabstract(uma_Diagram)


def test_uma_diagram_constructor_exists():
    assert callable(uma_Diagram.__init__)


def test_uma_diagram_constructor_args():
    sig = inspect.signature(uma_Diagram.__init__)
    params = list(sig.parameters.keys())
    assert "zoom" in params, "Missing parameter 'zoom'"

def test_uma_diagram_has_zoom():
    assert hasattr(uma_Diagram, "zoom")
    descriptor = None
    for klass in uma_Diagram.__mro__:
        if "zoom" in klass.__dict__:
            descriptor = klass.__dict__["zoom"]
            break
    assert isinstance(descriptor, property)



def test_processpackage_is_not_abstract():
    assert not inspect.isabstract(ProcessPackage)


def test_processpackage_constructor_exists():
    assert callable(ProcessPackage.__init__)


def test_processpackage_constructor_args():
    sig = inspect.signature(ProcessPackage.__init__)
    params = list(sig.parameters.keys())



def test_uma_graphconnector_is_not_abstract():
    assert not inspect.isabstract(uma_GraphConnector)


def test_uma_graphconnector_constructor_exists():
    assert callable(uma_GraphConnector.__init__)


def test_uma_graphconnector_constructor_args():
    sig = inspect.signature(uma_GraphConnector.__init__)
    params = list(sig.parameters.keys())



def test_diagramelement_is_not_abstract():
    assert not inspect.isabstract(DiagramElement)


def test_diagramelement_constructor_exists():
    assert callable(DiagramElement.__init__)


def test_diagramelement_constructor_args():
    sig = inspect.signature(DiagramElement.__init__)
    params = list(sig.parameters.keys())



def test_uma_semanticmodelbridge_is_not_abstract():
    assert not inspect.isabstract(uma_SemanticModelBridge)


def test_uma_semanticmodelbridge_constructor_exists():
    assert callable(uma_SemanticModelBridge.__init__)


def test_uma_semanticmodelbridge_constructor_args():
    sig = inspect.signature(uma_SemanticModelBridge.__init__)
    params = list(sig.parameters.keys())
    assert "presentation" in params, "Missing parameter 'presentation'"

def test_uma_semanticmodelbridge_has_presentation():
    assert hasattr(uma_SemanticModelBridge, "presentation")
    descriptor = None
    for klass in uma_SemanticModelBridge.__mro__:
        if "presentation" in klass.__dict__:
            descriptor = klass.__dict__["presentation"]
            break
    assert isinstance(descriptor, property)



def test_uma_reference_is_not_abstract():
    assert not inspect.isabstract(uma_Reference)


def test_uma_reference_constructor_exists():
    assert callable(uma_Reference.__init__)


def test_uma_reference_constructor_args():
    sig = inspect.signature(uma_Reference.__init__)
    params = list(sig.parameters.keys())
    assert "isIndividualRepresentation" in params, "Missing parameter 'isIndividualRepresentation'"

def test_uma_reference_has_isIndividualRepresentation():
    assert hasattr(uma_Reference, "isIndividualRepresentation")
    descriptor = None
    for klass in uma_Reference.__mro__:
        if "isIndividualRepresentation" in klass.__dict__:
            descriptor = klass.__dict__["isIndividualRepresentation"]
            break
    assert isinstance(descriptor, property)



def test_uma_diagramlink_is_not_abstract():
    assert not inspect.isabstract(uma_DiagramLink)


def test_uma_diagramlink_constructor_exists():
    assert callable(uma_DiagramLink.__init__)


def test_uma_diagramlink_constructor_args():
    sig = inspect.signature(uma_DiagramLink.__init__)
    params = list(sig.parameters.keys())
    assert "zoom" in params, "Missing parameter 'zoom'"

def test_uma_diagramlink_has_zoom():
    assert hasattr(uma_DiagramLink, "zoom")
    descriptor = None
    for klass in uma_DiagramLink.__mro__:
        if "zoom" in klass.__dict__:
            descriptor = klass.__dict__["zoom"]
            break
    assert isinstance(descriptor, property)



def test_uma_property_is_not_abstract():
    assert not inspect.isabstract(uma_Property)


def test_uma_property_constructor_exists():
    assert callable(uma_Property.__init__)


def test_uma_property_constructor_args():
    sig = inspect.signature(uma_Property.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "key" in params, "Missing parameter 'key'"

def test_uma_property_has_value():
    assert hasattr(uma_Property, "value")
    descriptor = None
    for klass in uma_Property.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_uma_property_has_key():
    assert hasattr(uma_Property, "key")
    descriptor = None
    for klass in uma_Property.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_uma_leafelement_is_not_abstract():
    assert not inspect.isabstract(uma_LeafElement)


def test_uma_leafelement_constructor_exists():
    assert callable(uma_LeafElement.__init__)


def test_uma_leafelement_constructor_args():
    sig = inspect.signature(uma_LeafElement.__init__)
    params = list(sig.parameters.keys())



def test_uma_graphelement_is_not_abstract():
    assert not inspect.isabstract(uma_GraphElement)


def test_uma_graphelement_constructor_exists():
    assert callable(uma_GraphElement.__init__)


def test_uma_graphelement_constructor_args():
    sig = inspect.signature(uma_GraphElement.__init__)
    params = list(sig.parameters.keys())



def test_uma_dimension_is_not_abstract():
    assert not inspect.isabstract(uma_Dimension)


def test_uma_dimension_constructor_exists():
    assert callable(uma_Dimension.__init__)


def test_uma_dimension_constructor_args():
    sig = inspect.signature(uma_Dimension.__init__)
    params = list(sig.parameters.keys())
    assert "height" in params, "Missing parameter 'height'"
    assert "width" in params, "Missing parameter 'width'"

def test_uma_dimension_has_height():
    assert hasattr(uma_Dimension, "height")
    descriptor = None
    for klass in uma_Dimension.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)

def test_uma_dimension_has_width():
    assert hasattr(uma_Dimension, "width")
    descriptor = None
    for klass in uma_Dimension.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)



def test_processdescription_is_not_abstract():
    assert not inspect.isabstract(ProcessDescription)


def test_processdescription_constructor_exists():
    assert callable(ProcessDescription.__init__)


def test_processdescription_constructor_args():
    sig = inspect.signature(ProcessDescription.__init__)
    params = list(sig.parameters.keys())



def test_uma_deliveryprocessdescription_is_not_abstract():
    assert not inspect.isabstract(uma_DeliveryProcessDescription)


def test_uma_deliveryprocessdescription_constructor_exists():
    assert callable(uma_DeliveryProcessDescription.__init__)


def test_uma_deliveryprocessdescription_constructor_args():
    sig = inspect.signature(uma_DeliveryProcessDescription.__init__)
    params = list(sig.parameters.keys())
    assert "estimatingTechnique" in params, "Missing parameter 'estimatingTechnique'"
    assert "projectCharacteristics" in params, "Missing parameter 'projectCharacteristics'"
    assert "projectMemberExpertise" in params, "Missing parameter 'projectMemberExpertise'"
    assert "scale" in params, "Missing parameter 'scale'"
    assert "riskLevel" in params, "Missing parameter 'riskLevel'"
    assert "typeOfContract" in params, "Missing parameter 'typeOfContract'"

def test_uma_deliveryprocessdescription_has_estimatingTechnique():
    assert hasattr(uma_DeliveryProcessDescription, "estimatingTechnique")
    descriptor = None
    for klass in uma_DeliveryProcessDescription.__mro__:
        if "estimatingTechnique" in klass.__dict__:
            descriptor = klass.__dict__["estimatingTechnique"]
            break
    assert isinstance(descriptor, property)

def test_uma_deliveryprocessdescription_has_projectCharacteristics():
    assert hasattr(uma_DeliveryProcessDescription, "projectCharacteristics")
    descriptor = None
    for klass in uma_DeliveryProcessDescription.__mro__:
        if "projectCharacteristics" in klass.__dict__:
            descriptor = klass.__dict__["projectCharacteristics"]
            break
    assert isinstance(descriptor, property)

def test_uma_deliveryprocessdescription_has_projectMemberExpertise():
    assert hasattr(uma_DeliveryProcessDescription, "projectMemberExpertise")
    descriptor = None
    for klass in uma_DeliveryProcessDescription.__mro__:
        if "projectMemberExpertise" in klass.__dict__:
            descriptor = klass.__dict__["projectMemberExpertise"]
            break
    assert isinstance(descriptor, property)

def test_uma_deliveryprocessdescription_has_scale():
    assert hasattr(uma_DeliveryProcessDescription, "scale")
    descriptor = None
    for klass in uma_DeliveryProcessDescription.__mro__:
        if "scale" in klass.__dict__:
            descriptor = klass.__dict__["scale"]
            break
    assert isinstance(descriptor, property)

def test_uma_deliveryprocessdescription_has_riskLevel():
    assert hasattr(uma_DeliveryProcessDescription, "riskLevel")
    descriptor = None
    for klass in uma_DeliveryProcessDescription.__mro__:
        if "riskLevel" in klass.__dict__:
            descriptor = klass.__dict__["riskLevel"]
            break
    assert isinstance(descriptor, property)

def test_uma_deliveryprocessdescription_has_typeOfContract():
    assert hasattr(uma_DeliveryProcessDescription, "typeOfContract")
    descriptor = None
    for klass in uma_DeliveryProcessDescription.__mro__:
        if "typeOfContract" in klass.__dict__:
            descriptor = klass.__dict__["typeOfContract"]
            break
    assert isinstance(descriptor, property)



def test_breakdownelementdescription_is_not_abstract():
    assert not inspect.isabstract(BreakdownElementDescription)


def test_breakdownelementdescription_constructor_exists():
    assert callable(BreakdownElementDescription.__init__)


def test_breakdownelementdescription_constructor_args():
    sig = inspect.signature(BreakdownElementDescription.__init__)
    params = list(sig.parameters.keys())



def test_uma_activitydescription_is_not_abstract():
    assert not inspect.isabstract(uma_ActivityDescription)


def test_uma_activitydescription_constructor_exists():
    assert callable(uma_ActivityDescription.__init__)


def test_uma_activitydescription_constructor_args():
    sig = inspect.signature(uma_ActivityDescription.__init__)
    params = list(sig.parameters.keys())
    assert "alternatives" in params, "Missing parameter 'alternatives'"
    assert "purpose" in params, "Missing parameter 'purpose'"
    assert "howtoStaff" in params, "Missing parameter 'howtoStaff'"

def test_uma_activitydescription_has_alternatives():
    assert hasattr(uma_ActivityDescription, "alternatives")
    descriptor = None
    for klass in uma_ActivityDescription.__mro__:
        if "alternatives" in klass.__dict__:
            descriptor = klass.__dict__["alternatives"]
            break
    assert isinstance(descriptor, property)

def test_uma_activitydescription_has_purpose():
    assert hasattr(uma_ActivityDescription, "purpose")
    descriptor = None
    for klass in uma_ActivityDescription.__mro__:
        if "purpose" in klass.__dict__:
            descriptor = klass.__dict__["purpose"]
            break
    assert isinstance(descriptor, property)

def test_uma_activitydescription_has_howtoStaff():
    assert hasattr(uma_ActivityDescription, "howtoStaff")
    descriptor = None
    for klass in uma_ActivityDescription.__mro__:
        if "howtoStaff" in klass.__dict__:
            descriptor = klass.__dict__["howtoStaff"]
            break
    assert isinstance(descriptor, property)



def test_uma_descriptordescription_is_not_abstract():
    assert not inspect.isabstract(uma_DescriptorDescription)


def test_uma_descriptordescription_constructor_exists():
    assert callable(uma_DescriptorDescription.__init__)


def test_uma_descriptordescription_constructor_args():
    sig = inspect.signature(uma_DescriptorDescription.__init__)
    params = list(sig.parameters.keys())
    assert "refinedDescription" in params, "Missing parameter 'refinedDescription'"

def test_uma_descriptordescription_has_refinedDescription():
    assert hasattr(uma_DescriptorDescription, "refinedDescription")
    descriptor = None
    for klass in uma_DescriptorDescription.__mro__:
        if "refinedDescription" in klass.__dict__:
            descriptor = klass.__dict__["refinedDescription"]
            break
    assert isinstance(descriptor, property)



def test_activitydescription_is_not_abstract():
    assert not inspect.isabstract(ActivityDescription)


def test_activitydescription_constructor_exists():
    assert callable(ActivityDescription.__init__)


def test_activitydescription_constructor_args():
    sig = inspect.signature(ActivityDescription.__init__)
    params = list(sig.parameters.keys())



def test_uma_processdescription_is_not_abstract():
    assert not inspect.isabstract(uma_ProcessDescription)


def test_uma_processdescription_constructor_exists():
    assert callable(uma_ProcessDescription.__init__)


def test_uma_processdescription_constructor_args():
    sig = inspect.signature(uma_ProcessDescription.__init__)
    params = list(sig.parameters.keys())
    assert "usageNotes" in params, "Missing parameter 'usageNotes'"
    assert "scope" in params, "Missing parameter 'scope'"

def test_uma_processdescription_has_usageNotes():
    assert hasattr(uma_ProcessDescription, "usageNotes")
    descriptor = None
    for klass in uma_ProcessDescription.__mro__:
        if "usageNotes" in klass.__dict__:
            descriptor = klass.__dict__["usageNotes"]
            break
    assert isinstance(descriptor, property)

def test_uma_processdescription_has_scope():
    assert hasattr(uma_ProcessDescription, "scope")
    descriptor = None
    for klass in uma_ProcessDescription.__mro__:
        if "scope" in klass.__dict__:
            descriptor = klass.__dict__["scope"]
            break
    assert isinstance(descriptor, property)



def test_process_is_not_abstract():
    assert not inspect.isabstract(Process)


def test_process_constructor_exists():
    assert callable(Process.__init__)


def test_process_constructor_args():
    sig = inspect.signature(Process.__init__)
    params = list(sig.parameters.keys())



def test_uma_capabilitypattern_is_not_abstract():
    assert not inspect.isabstract(uma_CapabilityPattern)


def test_uma_capabilitypattern_constructor_exists():
    assert callable(uma_CapabilityPattern.__init__)


def test_uma_capabilitypattern_constructor_args():
    sig = inspect.signature(uma_CapabilityPattern.__init__)
    params = list(sig.parameters.keys())



def test_uma_processplanningtemplate_is_not_abstract():
    assert not inspect.isabstract(uma_ProcessPlanningTemplate)


def test_uma_processplanningtemplate_constructor_exists():
    assert callable(uma_ProcessPlanningTemplate.__init__)


def test_uma_processplanningtemplate_constructor_args():
    sig = inspect.signature(uma_ProcessPlanningTemplate.__init__)
    params = list(sig.parameters.keys())



def test_uma_deliveryprocess_is_not_abstract():
    assert not inspect.isabstract(uma_DeliveryProcess)


def test_uma_deliveryprocess_constructor_exists():
    assert callable(uma_DeliveryProcess.__init__)


def test_uma_deliveryprocess_constructor_args():
    sig = inspect.signature(uma_DeliveryProcess.__init__)
    params = list(sig.parameters.keys())



def test_roledescriptor_is_not_abstract():
    assert not inspect.isabstract(RoleDescriptor)


def test_roledescriptor_constructor_exists():
    assert callable(RoleDescriptor.__init__)


def test_roledescriptor_constructor_args():
    sig = inspect.signature(RoleDescriptor.__init__)
    params = list(sig.parameters.keys())



def test_uma_compositerole_is_not_abstract():
    assert not inspect.isabstract(uma_CompositeRole)


def test_uma_compositerole_constructor_exists():
    assert callable(uma_CompositeRole.__init__)


def test_uma_compositerole_constructor_args():
    sig = inspect.signature(uma_CompositeRole.__init__)
    params = list(sig.parameters.keys())



def test_descriptor_is_not_abstract():
    assert not inspect.isabstract(Descriptor)


def test_descriptor_constructor_exists():
    assert callable(Descriptor.__init__)


def test_descriptor_constructor_args():
    sig = inspect.signature(Descriptor.__init__)
    params = list(sig.parameters.keys())



def test_uma_processcomponentdescriptor_is_not_abstract():
    assert not inspect.isabstract(uma_ProcessComponentDescriptor)


def test_uma_processcomponentdescriptor_constructor_exists():
    assert callable(uma_ProcessComponentDescriptor.__init__)


def test_uma_processcomponentdescriptor_constructor_args():
    sig = inspect.signature(uma_ProcessComponentDescriptor.__init__)
    params = list(sig.parameters.keys())



def test_uma_workproductdescriptor_is_not_abstract():
    assert not inspect.isabstract(uma_WorkProductDescriptor)


def test_uma_workproductdescriptor_constructor_exists():
    assert callable(uma_WorkProductDescriptor.__init__)


def test_uma_workproductdescriptor_constructor_args():
    sig = inspect.signature(uma_WorkProductDescriptor.__init__)
    params = list(sig.parameters.keys())
    assert "activityExitState" in params, "Missing parameter 'activityExitState'"
    assert "activityEntryState" in params, "Missing parameter 'activityEntryState'"

def test_uma_workproductdescriptor_has_activityExitState():
    assert hasattr(uma_WorkProductDescriptor, "activityExitState")
    descriptor = None
    for klass in uma_WorkProductDescriptor.__mro__:
        if "activityExitState" in klass.__dict__:
            descriptor = klass.__dict__["activityExitState"]
            break
    assert isinstance(descriptor, property)

def test_uma_workproductdescriptor_has_activityEntryState():
    assert hasattr(uma_WorkProductDescriptor, "activityEntryState")
    descriptor = None
    for klass in uma_WorkProductDescriptor.__mro__:
        if "activityEntryState" in klass.__dict__:
            descriptor = klass.__dict__["activityEntryState"]
            break
    assert isinstance(descriptor, property)



def test_uma_roledescriptor_is_not_abstract():
    assert not inspect.isabstract(uma_RoleDescriptor)


def test_uma_roledescriptor_constructor_exists():
    assert callable(uma_RoleDescriptor.__init__)


def test_uma_roledescriptor_constructor_args():
    sig = inspect.signature(uma_RoleDescriptor.__init__)
    params = list(sig.parameters.keys())



def test_activity_is_not_abstract():
    assert not inspect.isabstract(Activity)


def test_activity_constructor_exists():
    assert callable(Activity.__init__)


def test_activity_constructor_args():
    sig = inspect.signature(Activity.__init__)
    params = list(sig.parameters.keys())



def test_uma_phase_is_not_abstract():
    assert not inspect.isabstract(uma_Phase)


def test_uma_phase_constructor_exists():
    assert callable(uma_Phase.__init__)


def test_uma_phase_constructor_args():
    sig = inspect.signature(uma_Phase.__init__)
    params = list(sig.parameters.keys())



def test_uma_process_is_not_abstract():
    assert not inspect.isabstract(uma_Process)


def test_uma_process_constructor_exists():
    assert callable(uma_Process.__init__)


def test_uma_process_constructor_args():
    sig = inspect.signature(uma_Process.__init__)
    params = list(sig.parameters.keys())



def test_uma_iteration_is_not_abstract():
    assert not inspect.isabstract(uma_Iteration)


def test_uma_iteration_constructor_exists():
    assert callable(uma_Iteration.__init__)


def test_uma_iteration_constructor_args():
    sig = inspect.signature(uma_Iteration.__init__)
    params = list(sig.parameters.keys())



def test_methodpackage_is_not_abstract():
    assert not inspect.isabstract(MethodPackage)


def test_methodpackage_constructor_exists():
    assert callable(MethodPackage.__init__)


def test_methodpackage_constructor_args():
    sig = inspect.signature(MethodPackage.__init__)
    params = list(sig.parameters.keys())



def test_uma_processpackage_is_not_abstract():
    assert not inspect.isabstract(uma_ProcessPackage)


def test_uma_processpackage_constructor_exists():
    assert callable(uma_ProcessPackage.__init__)


def test_uma_processpackage_constructor_args():
    sig = inspect.signature(uma_ProcessPackage.__init__)
    params = list(sig.parameters.keys())



def test_uma_contentpackage_is_not_abstract():
    assert not inspect.isabstract(uma_ContentPackage)


def test_uma_contentpackage_constructor_exists():
    assert callable(uma_ContentPackage.__init__)


def test_uma_contentpackage_constructor_args():
    sig = inspect.signature(uma_ContentPackage.__init__)
    params = list(sig.parameters.keys())



def test_package_is_not_abstract():
    assert not inspect.isabstract(Package)


def test_package_constructor_exists():
    assert callable(Package.__init__)


def test_package_constructor_args():
    sig = inspect.signature(Package.__init__)
    params = list(sig.parameters.keys())



def test_processelement_is_not_abstract():
    assert not inspect.isabstract(ProcessElement)


def test_processelement_constructor_exists():
    assert callable(ProcessElement.__init__)


def test_processelement_constructor_args():
    sig = inspect.signature(ProcessElement.__init__)
    params = list(sig.parameters.keys())



def test_uma_workorder_is_not_abstract():
    assert not inspect.isabstract(uma_WorkOrder)


def test_uma_workorder_constructor_exists():
    assert callable(uma_WorkOrder.__init__)


def test_uma_workorder_constructor_args():
    sig = inspect.signature(uma_WorkOrder.__init__)
    params = list(sig.parameters.keys())
    assert "linkType" in params, "Missing parameter 'linkType'"

def test_uma_workorder_has_linkType():
    assert hasattr(uma_WorkOrder, "linkType")
    descriptor = None
    for klass in uma_WorkOrder.__mro__:
        if "linkType" in klass.__dict__:
            descriptor = klass.__dict__["linkType"]
            break
    assert isinstance(descriptor, property)



def test_breakdownelement_is_not_abstract():
    assert not inspect.isabstract(BreakdownElement)


def test_breakdownelement_constructor_exists():
    assert callable(BreakdownElement.__init__)


def test_breakdownelement_constructor_args():
    sig = inspect.signature(BreakdownElement.__init__)
    params = list(sig.parameters.keys())



def test_uma_teamprofile_is_not_abstract():
    assert not inspect.isabstract(uma_TeamProfile)


def test_uma_teamprofile_constructor_exists():
    assert callable(uma_TeamProfile.__init__)


def test_uma_teamprofile_constructor_args():
    sig = inspect.signature(uma_TeamProfile.__init__)
    params = list(sig.parameters.keys())



def test_uma_descriptor_is_not_abstract():
    assert not inspect.isabstract(uma_Descriptor)


def test_uma_descriptor_constructor_exists():
    assert callable(uma_Descriptor.__init__)


def test_uma_descriptor_constructor_args():
    sig = inspect.signature(uma_Descriptor.__init__)
    params = list(sig.parameters.keys())
    assert "isSynchronizedWithSource" in params, "Missing parameter 'isSynchronizedWithSource'"

def test_uma_descriptor_has_isSynchronizedWithSource():
    assert hasattr(uma_Descriptor, "isSynchronizedWithSource")
    descriptor = None
    for klass in uma_Descriptor.__mro__:
        if "isSynchronizedWithSource" in klass.__dict__:
            descriptor = klass.__dict__["isSynchronizedWithSource"]
            break
    assert isinstance(descriptor, property)



def test_uma_processcomponentinterface_is_not_abstract():
    assert not inspect.isabstract(uma_ProcessComponentInterface)


def test_uma_processcomponentinterface_constructor_exists():
    assert callable(uma_ProcessComponentInterface.__init__)


def test_uma_processcomponentinterface_constructor_args():
    sig = inspect.signature(uma_ProcessComponentInterface.__init__)
    params = list(sig.parameters.keys())



def test_uma_workbreakdownelement_is_not_abstract():
    assert not inspect.isabstract(uma_WorkBreakdownElement)


def test_uma_workbreakdownelement_constructor_exists():
    assert callable(uma_WorkBreakdownElement.__init__)


def test_uma_workbreakdownelement_constructor_args():
    sig = inspect.signature(uma_WorkBreakdownElement.__init__)
    params = list(sig.parameters.keys())
    assert "isRepeatable" in params, "Missing parameter 'isRepeatable'"
    assert "isOngoing" in params, "Missing parameter 'isOngoing'"
    assert "isEventDriven" in params, "Missing parameter 'isEventDriven'"

def test_uma_workbreakdownelement_has_isRepeatable():
    assert hasattr(uma_WorkBreakdownElement, "isRepeatable")
    descriptor = None
    for klass in uma_WorkBreakdownElement.__mro__:
        if "isRepeatable" in klass.__dict__:
            descriptor = klass.__dict__["isRepeatable"]
            break
    assert isinstance(descriptor, property)

def test_uma_workbreakdownelement_has_isOngoing():
    assert hasattr(uma_WorkBreakdownElement, "isOngoing")
    descriptor = None
    for klass in uma_WorkBreakdownElement.__mro__:
        if "isOngoing" in klass.__dict__:
            descriptor = klass.__dict__["isOngoing"]
            break
    assert isinstance(descriptor, property)

def test_uma_workbreakdownelement_has_isEventDriven():
    assert hasattr(uma_WorkBreakdownElement, "isEventDriven")
    descriptor = None
    for klass in uma_WorkBreakdownElement.__mro__:
        if "isEventDriven" in klass.__dict__:
            descriptor = klass.__dict__["isEventDriven"]
            break
    assert isinstance(descriptor, property)



def test_uma_breakdownelement_is_not_abstract():
    assert not inspect.isabstract(uma_BreakdownElement)


def test_uma_breakdownelement_constructor_exists():
    assert callable(uma_BreakdownElement.__init__)


def test_uma_breakdownelement_constructor_args():
    sig = inspect.signature(uma_BreakdownElement.__init__)
    params = list(sig.parameters.keys())
    assert "hasMultipleOccurrences" in params, "Missing parameter 'hasMultipleOccurrences'"
    assert "isPlanned" in params, "Missing parameter 'isPlanned'"
    assert "prefix" in params, "Missing parameter 'prefix'"
    assert "isOptional" in params, "Missing parameter 'isOptional'"

def test_uma_breakdownelement_has_hasMultipleOccurrences():
    assert hasattr(uma_BreakdownElement, "hasMultipleOccurrences")
    descriptor = None
    for klass in uma_BreakdownElement.__mro__:
        if "hasMultipleOccurrences" in klass.__dict__:
            descriptor = klass.__dict__["hasMultipleOccurrences"]
            break
    assert isinstance(descriptor, property)

def test_uma_breakdownelement_has_isPlanned():
    assert hasattr(uma_BreakdownElement, "isPlanned")
    descriptor = None
    for klass in uma_BreakdownElement.__mro__:
        if "isPlanned" in klass.__dict__:
            descriptor = klass.__dict__["isPlanned"]
            break
    assert isinstance(descriptor, property)

def test_uma_breakdownelement_has_prefix():
    assert hasattr(uma_BreakdownElement, "prefix")
    descriptor = None
    for klass in uma_BreakdownElement.__mro__:
        if "prefix" in klass.__dict__:
            descriptor = klass.__dict__["prefix"]
            break
    assert isinstance(descriptor, property)

def test_uma_breakdownelement_has_isOptional():
    assert hasattr(uma_BreakdownElement, "isOptional")
    descriptor = None
    for klass in uma_BreakdownElement.__mro__:
        if "isOptional" in klass.__dict__:
            descriptor = klass.__dict__["isOptional"]
            break
    assert isinstance(descriptor, property)



def test_workbreakdownelement_is_not_abstract():
    assert not inspect.isabstract(WorkBreakdownElement)


def test_workbreakdownelement_constructor_exists():
    assert callable(WorkBreakdownElement.__init__)


def test_workbreakdownelement_constructor_args():
    sig = inspect.signature(WorkBreakdownElement.__init__)
    params = list(sig.parameters.keys())



def test_uma_milestone_is_not_abstract():
    assert not inspect.isabstract(uma_Milestone)


def test_uma_milestone_constructor_exists():
    assert callable(uma_Milestone.__init__)


def test_uma_milestone_constructor_args():
    sig = inspect.signature(uma_Milestone.__init__)
    params = list(sig.parameters.keys())



def test_uma_taskdescriptor_is_not_abstract():
    assert not inspect.isabstract(uma_TaskDescriptor)


def test_uma_taskdescriptor_constructor_exists():
    assert callable(uma_TaskDescriptor.__init__)


def test_uma_taskdescriptor_constructor_args():
    sig = inspect.signature(uma_TaskDescriptor.__init__)
    params = list(sig.parameters.keys())



def test_uma_planningdata_is_not_abstract():
    assert not inspect.isabstract(uma_PlanningData)


def test_uma_planningdata_constructor_exists():
    assert callable(uma_PlanningData.__init__)


def test_uma_planningdata_constructor_args():
    sig = inspect.signature(uma_PlanningData.__init__)
    params = list(sig.parameters.keys())
    assert "startDate" in params, "Missing parameter 'startDate'"
    assert "rank" in params, "Missing parameter 'rank'"
    assert "finishDate" in params, "Missing parameter 'finishDate'"

def test_uma_planningdata_has_startDate():
    assert hasattr(uma_PlanningData, "startDate")
    descriptor = None
    for klass in uma_PlanningData.__mro__:
        if "startDate" in klass.__dict__:
            descriptor = klass.__dict__["startDate"]
            break
    assert isinstance(descriptor, property)

def test_uma_planningdata_has_rank():
    assert hasattr(uma_PlanningData, "rank")
    descriptor = None
    for klass in uma_PlanningData.__mro__:
        if "rank" in klass.__dict__:
            descriptor = klass.__dict__["rank"]
            break
    assert isinstance(descriptor, property)

def test_uma_planningdata_has_finishDate():
    assert hasattr(uma_PlanningData, "finishDate")
    descriptor = None
    for klass in uma_PlanningData.__mro__:
        if "finishDate" in klass.__dict__:
            descriptor = klass.__dict__["finishDate"]
            break
    assert isinstance(descriptor, property)



def test_contentcategory_is_not_abstract():
    assert not inspect.isabstract(ContentCategory)


def test_contentcategory_constructor_exists():
    assert callable(ContentCategory.__init__)


def test_contentcategory_constructor_args():
    sig = inspect.signature(ContentCategory.__init__)
    params = list(sig.parameters.keys())



def test_uma_rolesetgrouping_is_not_abstract():
    assert not inspect.isabstract(uma_RoleSetGrouping)


def test_uma_rolesetgrouping_constructor_exists():
    assert callable(uma_RoleSetGrouping.__init__)


def test_uma_rolesetgrouping_constructor_args():
    sig = inspect.signature(uma_RoleSetGrouping.__init__)
    params = list(sig.parameters.keys())



def test_uma_tool_is_not_abstract():
    assert not inspect.isabstract(uma_Tool)


def test_uma_tool_constructor_exists():
    assert callable(uma_Tool.__init__)


def test_uma_tool_constructor_args():
    sig = inspect.signature(uma_Tool.__init__)
    params = list(sig.parameters.keys())



def test_uma_customcategory_is_not_abstract():
    assert not inspect.isabstract(uma_CustomCategory)


def test_uma_customcategory_constructor_exists():
    assert callable(uma_CustomCategory.__init__)


def test_uma_customcategory_constructor_args():
    sig = inspect.signature(uma_CustomCategory.__init__)
    params = list(sig.parameters.keys())



def test_uma_domain_is_not_abstract():
    assert not inspect.isabstract(uma_Domain)


def test_uma_domain_constructor_exists():
    assert callable(uma_Domain.__init__)


def test_uma_domain_constructor_args():
    sig = inspect.signature(uma_Domain.__init__)
    params = list(sig.parameters.keys())



def test_uma_disciplinegrouping_is_not_abstract():
    assert not inspect.isabstract(uma_DisciplineGrouping)


def test_uma_disciplinegrouping_constructor_exists():
    assert callable(uma_DisciplineGrouping.__init__)


def test_uma_disciplinegrouping_constructor_args():
    sig = inspect.signature(uma_DisciplineGrouping.__init__)
    params = list(sig.parameters.keys())



def test_uma_workproducttype_is_not_abstract():
    assert not inspect.isabstract(uma_WorkProductType)


def test_uma_workproducttype_constructor_exists():
    assert callable(uma_WorkProductType.__init__)


def test_uma_workproducttype_constructor_args():
    sig = inspect.signature(uma_WorkProductType.__init__)
    params = list(sig.parameters.keys())



def test_uma_roleset_is_not_abstract():
    assert not inspect.isabstract(uma_RoleSet)


def test_uma_roleset_constructor_exists():
    assert callable(uma_RoleSet.__init__)


def test_uma_roleset_constructor_args():
    sig = inspect.signature(uma_RoleSet.__init__)
    params = list(sig.parameters.keys())



def test_uma_discipline_is_not_abstract():
    assert not inspect.isabstract(uma_Discipline)


def test_uma_discipline_constructor_exists():
    assert callable(uma_Discipline.__init__)


def test_uma_discipline_constructor_args():
    sig = inspect.signature(uma_Discipline.__init__)
    params = list(sig.parameters.keys())



def test_contentdescription_is_not_abstract():
    assert not inspect.isabstract(ContentDescription)


def test_contentdescription_constructor_exists():
    assert callable(ContentDescription.__init__)


def test_contentdescription_constructor_args():
    sig = inspect.signature(ContentDescription.__init__)
    params = list(sig.parameters.keys())



def test_uma_taskdescription_is_not_abstract():
    assert not inspect.isabstract(uma_TaskDescription)


def test_uma_taskdescription_constructor_exists():
    assert callable(uma_TaskDescription.__init__)


def test_uma_taskdescription_constructor_args():
    sig = inspect.signature(uma_TaskDescription.__init__)
    params = list(sig.parameters.keys())
    assert "alternatives" in params, "Missing parameter 'alternatives'"
    assert "purpose" in params, "Missing parameter 'purpose'"

def test_uma_taskdescription_has_alternatives():
    assert hasattr(uma_TaskDescription, "alternatives")
    descriptor = None
    for klass in uma_TaskDescription.__mro__:
        if "alternatives" in klass.__dict__:
            descriptor = klass.__dict__["alternatives"]
            break
    assert isinstance(descriptor, property)

def test_uma_taskdescription_has_purpose():
    assert hasattr(uma_TaskDescription, "purpose")
    descriptor = None
    for klass in uma_TaskDescription.__mro__:
        if "purpose" in klass.__dict__:
            descriptor = klass.__dict__["purpose"]
            break
    assert isinstance(descriptor, property)



def test_uma_roledescription_is_not_abstract():
    assert not inspect.isabstract(uma_RoleDescription)


def test_uma_roledescription_constructor_exists():
    assert callable(uma_RoleDescription.__init__)


def test_uma_roledescription_constructor_args():
    sig = inspect.signature(uma_RoleDescription.__init__)
    params = list(sig.parameters.keys())
    assert "synonyms" in params, "Missing parameter 'synonyms'"
    assert "skills" in params, "Missing parameter 'skills'"
    assert "assignmentApproaches" in params, "Missing parameter 'assignmentApproaches'"

def test_uma_roledescription_has_synonyms():
    assert hasattr(uma_RoleDescription, "synonyms")
    descriptor = None
    for klass in uma_RoleDescription.__mro__:
        if "synonyms" in klass.__dict__:
            descriptor = klass.__dict__["synonyms"]
            break
    assert isinstance(descriptor, property)

def test_uma_roledescription_has_skills():
    assert hasattr(uma_RoleDescription, "skills")
    descriptor = None
    for klass in uma_RoleDescription.__mro__:
        if "skills" in klass.__dict__:
            descriptor = klass.__dict__["skills"]
            break
    assert isinstance(descriptor, property)

def test_uma_roledescription_has_assignmentApproaches():
    assert hasattr(uma_RoleDescription, "assignmentApproaches")
    descriptor = None
    for klass in uma_RoleDescription.__mro__:
        if "assignmentApproaches" in klass.__dict__:
            descriptor = klass.__dict__["assignmentApproaches"]
            break
    assert isinstance(descriptor, property)



def test_uma_breakdownelementdescription_is_not_abstract():
    assert not inspect.isabstract(uma_BreakdownElementDescription)


def test_uma_breakdownelementdescription_constructor_exists():
    assert callable(uma_BreakdownElementDescription.__init__)


def test_uma_breakdownelementdescription_constructor_args():
    sig = inspect.signature(uma_BreakdownElementDescription.__init__)
    params = list(sig.parameters.keys())
    assert "usageGuidance" in params, "Missing parameter 'usageGuidance'"

def test_uma_breakdownelementdescription_has_usageGuidance():
    assert hasattr(uma_BreakdownElementDescription, "usageGuidance")
    descriptor = None
    for klass in uma_BreakdownElementDescription.__mro__:
        if "usageGuidance" in klass.__dict__:
            descriptor = klass.__dict__["usageGuidance"]
            break
    assert isinstance(descriptor, property)



def test_uma_workproductdescription_is_not_abstract():
    assert not inspect.isabstract(uma_WorkProductDescription)


def test_uma_workproductdescription_constructor_exists():
    assert callable(uma_WorkProductDescription.__init__)


def test_uma_workproductdescription_constructor_args():
    sig = inspect.signature(uma_WorkProductDescription.__init__)
    params = list(sig.parameters.keys())
    assert "impactOfNotHaving" in params, "Missing parameter 'impactOfNotHaving'"
    assert "purpose" in params, "Missing parameter 'purpose'"
    assert "reasonsForNotNeeding" in params, "Missing parameter 'reasonsForNotNeeding'"

def test_uma_workproductdescription_has_impactOfNotHaving():
    assert hasattr(uma_WorkProductDescription, "impactOfNotHaving")
    descriptor = None
    for klass in uma_WorkProductDescription.__mro__:
        if "impactOfNotHaving" in klass.__dict__:
            descriptor = klass.__dict__["impactOfNotHaving"]
            break
    assert isinstance(descriptor, property)

def test_uma_workproductdescription_has_purpose():
    assert hasattr(uma_WorkProductDescription, "purpose")
    descriptor = None
    for klass in uma_WorkProductDescription.__mro__:
        if "purpose" in klass.__dict__:
            descriptor = klass.__dict__["purpose"]
            break
    assert isinstance(descriptor, property)

def test_uma_workproductdescription_has_reasonsForNotNeeding():
    assert hasattr(uma_WorkProductDescription, "reasonsForNotNeeding")
    descriptor = None
    for klass in uma_WorkProductDescription.__mro__:
        if "reasonsForNotNeeding" in klass.__dict__:
            descriptor = klass.__dict__["reasonsForNotNeeding"]
            break
    assert isinstance(descriptor, property)



def test_uma_practicedescription_is_not_abstract():
    assert not inspect.isabstract(uma_PracticeDescription)


def test_uma_practicedescription_constructor_exists():
    assert callable(uma_PracticeDescription.__init__)


def test_uma_practicedescription_constructor_args():
    sig = inspect.signature(uma_PracticeDescription.__init__)
    params = list(sig.parameters.keys())
    assert "goals" in params, "Missing parameter 'goals'"
    assert "background" in params, "Missing parameter 'background'"
    assert "additionalInfo" in params, "Missing parameter 'additionalInfo'"
    assert "levelsOfAdoption" in params, "Missing parameter 'levelsOfAdoption'"
    assert "application" in params, "Missing parameter 'application'"
    assert "problem" in params, "Missing parameter 'problem'"

def test_uma_practicedescription_has_goals():
    assert hasattr(uma_PracticeDescription, "goals")
    descriptor = None
    for klass in uma_PracticeDescription.__mro__:
        if "goals" in klass.__dict__:
            descriptor = klass.__dict__["goals"]
            break
    assert isinstance(descriptor, property)

def test_uma_practicedescription_has_background():
    assert hasattr(uma_PracticeDescription, "background")
    descriptor = None
    for klass in uma_PracticeDescription.__mro__:
        if "background" in klass.__dict__:
            descriptor = klass.__dict__["background"]
            break
    assert isinstance(descriptor, property)

def test_uma_practicedescription_has_additionalInfo():
    assert hasattr(uma_PracticeDescription, "additionalInfo")
    descriptor = None
    for klass in uma_PracticeDescription.__mro__:
        if "additionalInfo" in klass.__dict__:
            descriptor = klass.__dict__["additionalInfo"]
            break
    assert isinstance(descriptor, property)

def test_uma_practicedescription_has_levelsOfAdoption():
    assert hasattr(uma_PracticeDescription, "levelsOfAdoption")
    descriptor = None
    for klass in uma_PracticeDescription.__mro__:
        if "levelsOfAdoption" in klass.__dict__:
            descriptor = klass.__dict__["levelsOfAdoption"]
            break
    assert isinstance(descriptor, property)

def test_uma_practicedescription_has_application():
    assert hasattr(uma_PracticeDescription, "application")
    descriptor = None
    for klass in uma_PracticeDescription.__mro__:
        if "application" in klass.__dict__:
            descriptor = klass.__dict__["application"]
            break
    assert isinstance(descriptor, property)

def test_uma_practicedescription_has_problem():
    assert hasattr(uma_PracticeDescription, "problem")
    descriptor = None
    for klass in uma_PracticeDescription.__mro__:
        if "problem" in klass.__dict__:
            descriptor = klass.__dict__["problem"]
            break
    assert isinstance(descriptor, property)



def test_uma_guidancedescription_is_not_abstract():
    assert not inspect.isabstract(uma_GuidanceDescription)


def test_uma_guidancedescription_constructor_exists():
    assert callable(uma_GuidanceDescription.__init__)


def test_uma_guidancedescription_constructor_args():
    sig = inspect.signature(uma_GuidanceDescription.__init__)
    params = list(sig.parameters.keys())
    assert "attachments" in params, "Missing parameter 'attachments'"

def test_uma_guidancedescription_has_attachments():
    assert hasattr(uma_GuidanceDescription, "attachments")
    descriptor = None
    for klass in uma_GuidanceDescription.__mro__:
        if "attachments" in klass.__dict__:
            descriptor = klass.__dict__["attachments"]
            break
    assert isinstance(descriptor, property)



def test_concept_is_not_abstract():
    assert not inspect.isabstract(Concept)


def test_concept_constructor_exists():
    assert callable(Concept.__init__)


def test_concept_constructor_args():
    sig = inspect.signature(Concept.__init__)
    params = list(sig.parameters.keys())



def test_uma_whitepaper_is_not_abstract():
    assert not inspect.isabstract(uma_Whitepaper)


def test_uma_whitepaper_constructor_exists():
    assert callable(uma_Whitepaper.__init__)


def test_uma_whitepaper_constructor_args():
    sig = inspect.signature(uma_Whitepaper.__init__)
    params = list(sig.parameters.keys())



def test_workdefinition_is_not_abstract():
    assert not inspect.isabstract(WorkDefinition)


def test_workdefinition_constructor_exists():
    assert callable(WorkDefinition.__init__)


def test_workdefinition_constructor_args():
    sig = inspect.signature(WorkDefinition.__init__)
    params = list(sig.parameters.keys())



def test_section_is_not_abstract():
    assert not inspect.isabstract(Section)


def test_section_constructor_exists():
    assert callable(Section.__init__)


def test_section_constructor_args():
    sig = inspect.signature(Section.__init__)
    params = list(sig.parameters.keys())



def test_uma_step_is_not_abstract():
    assert not inspect.isabstract(uma_Step)


def test_uma_step_constructor_exists():
    assert callable(uma_Step.__init__)


def test_uma_step_constructor_args():
    sig = inspect.signature(uma_Step.__init__)
    params = list(sig.parameters.keys())



def test_workproductdescription_is_not_abstract():
    assert not inspect.isabstract(WorkProductDescription)


def test_workproductdescription_constructor_exists():
    assert callable(WorkProductDescription.__init__)


def test_workproductdescription_constructor_args():
    sig = inspect.signature(WorkProductDescription.__init__)
    params = list(sig.parameters.keys())



def test_uma_deliverabledescription_is_not_abstract():
    assert not inspect.isabstract(uma_DeliverableDescription)


def test_uma_deliverabledescription_constructor_exists():
    assert callable(uma_DeliverableDescription.__init__)


def test_uma_deliverabledescription_constructor_args():
    sig = inspect.signature(uma_DeliverableDescription.__init__)
    params = list(sig.parameters.keys())
    assert "externalDescription" in params, "Missing parameter 'externalDescription'"
    assert "packagingGuidance" in params, "Missing parameter 'packagingGuidance'"

def test_uma_deliverabledescription_has_externalDescription():
    assert hasattr(uma_DeliverableDescription, "externalDescription")
    descriptor = None
    for klass in uma_DeliverableDescription.__mro__:
        if "externalDescription" in klass.__dict__:
            descriptor = klass.__dict__["externalDescription"]
            break
    assert isinstance(descriptor, property)

def test_uma_deliverabledescription_has_packagingGuidance():
    assert hasattr(uma_DeliverableDescription, "packagingGuidance")
    descriptor = None
    for klass in uma_DeliverableDescription.__mro__:
        if "packagingGuidance" in klass.__dict__:
            descriptor = klass.__dict__["packagingGuidance"]
            break
    assert isinstance(descriptor, property)



def test_uma_artifactdescription_is_not_abstract():
    assert not inspect.isabstract(uma_ArtifactDescription)


def test_uma_artifactdescription_constructor_exists():
    assert callable(uma_ArtifactDescription.__init__)


def test_uma_artifactdescription_constructor_args():
    sig = inspect.signature(uma_ArtifactDescription.__init__)
    params = list(sig.parameters.keys())
    assert "notation" in params, "Missing parameter 'notation'"
    assert "representationOptions" in params, "Missing parameter 'representationOptions'"
    assert "briefOutline" in params, "Missing parameter 'briefOutline'"
    assert "representation" in params, "Missing parameter 'representation'"

def test_uma_artifactdescription_has_notation():
    assert hasattr(uma_ArtifactDescription, "notation")
    descriptor = None
    for klass in uma_ArtifactDescription.__mro__:
        if "notation" in klass.__dict__:
            descriptor = klass.__dict__["notation"]
            break
    assert isinstance(descriptor, property)

def test_uma_artifactdescription_has_representationOptions():
    assert hasattr(uma_ArtifactDescription, "representationOptions")
    descriptor = None
    for klass in uma_ArtifactDescription.__mro__:
        if "representationOptions" in klass.__dict__:
            descriptor = klass.__dict__["representationOptions"]
            break
    assert isinstance(descriptor, property)

def test_uma_artifactdescription_has_briefOutline():
    assert hasattr(uma_ArtifactDescription, "briefOutline")
    descriptor = None
    for klass in uma_ArtifactDescription.__mro__:
        if "briefOutline" in klass.__dict__:
            descriptor = klass.__dict__["briefOutline"]
            break
    assert isinstance(descriptor, property)

def test_uma_artifactdescription_has_representation():
    assert hasattr(uma_ArtifactDescription, "representation")
    descriptor = None
    for klass in uma_ArtifactDescription.__mro__:
        if "representation" in klass.__dict__:
            descriptor = klass.__dict__["representation"]
            break
    assert isinstance(descriptor, property)



def test_fulfillableelement_is_not_abstract():
    assert not inspect.isabstract(FulfillableElement)


def test_fulfillableelement_constructor_exists():
    assert callable(FulfillableElement.__init__)


def test_fulfillableelement_constructor_args():
    sig = inspect.signature(FulfillableElement.__init__)
    params = list(sig.parameters.keys())



def test_workproduct_is_not_abstract():
    assert not inspect.isabstract(WorkProduct)


def test_workproduct_constructor_exists():
    assert callable(WorkProduct.__init__)


def test_workproduct_constructor_args():
    sig = inspect.signature(WorkProduct.__init__)
    params = list(sig.parameters.keys())



def test_uma_deliverable_is_not_abstract():
    assert not inspect.isabstract(uma_Deliverable)


def test_uma_deliverable_constructor_exists():
    assert callable(uma_Deliverable.__init__)


def test_uma_deliverable_constructor_args():
    sig = inspect.signature(uma_Deliverable.__init__)
    params = list(sig.parameters.keys())



def test_uma_outcome_is_not_abstract():
    assert not inspect.isabstract(uma_Outcome)


def test_uma_outcome_constructor_exists():
    assert callable(uma_Outcome.__init__)


def test_uma_outcome_constructor_args():
    sig = inspect.signature(uma_Outcome.__init__)
    params = list(sig.parameters.keys())



def test_uma_artifact_is_not_abstract():
    assert not inspect.isabstract(uma_Artifact)


def test_uma_artifact_constructor_exists():
    assert callable(uma_Artifact.__init__)


def test_uma_artifact_constructor_args():
    sig = inspect.signature(uma_Artifact.__init__)
    params = list(sig.parameters.keys())



def test_methodunit_is_not_abstract():
    assert not inspect.isabstract(MethodUnit)


def test_methodunit_constructor_exists():
    assert callable(MethodUnit.__init__)


def test_methodunit_constructor_args():
    sig = inspect.signature(MethodUnit.__init__)
    params = list(sig.parameters.keys())



def test_uma_processcomponent_is_not_abstract():
    assert not inspect.isabstract(uma_ProcessComponent)


def test_uma_processcomponent_constructor_exists():
    assert callable(uma_ProcessComponent.__init__)


def test_uma_processcomponent_constructor_args():
    sig = inspect.signature(uma_ProcessComponent.__init__)
    params = list(sig.parameters.keys())



def test_uma_methodlibrary_is_not_abstract():
    assert not inspect.isabstract(uma_MethodLibrary)


def test_uma_methodlibrary_constructor_exists():
    assert callable(uma_MethodLibrary.__init__)


def test_uma_methodlibrary_constructor_args():
    sig = inspect.signature(uma_MethodLibrary.__init__)
    params = list(sig.parameters.keys())



def test_uma_methodplugin_is_not_abstract():
    assert not inspect.isabstract(uma_MethodPlugin)


def test_uma_methodplugin_constructor_exists():
    assert callable(uma_MethodPlugin.__init__)


def test_uma_methodplugin_constructor_args():
    sig = inspect.signature(uma_MethodPlugin.__init__)
    params = list(sig.parameters.keys())
    assert "supporting" in params, "Missing parameter 'supporting'"
    assert "userChangeable" in params, "Missing parameter 'userChangeable'"

def test_uma_methodplugin_has_supporting():
    assert hasattr(uma_MethodPlugin, "supporting")
    descriptor = None
    for klass in uma_MethodPlugin.__mro__:
        if "supporting" in klass.__dict__:
            descriptor = klass.__dict__["supporting"]
            break
    assert isinstance(descriptor, property)

def test_uma_methodplugin_has_userChangeable():
    assert hasattr(uma_MethodPlugin, "userChangeable")
    descriptor = None
    for klass in uma_MethodPlugin.__mro__:
        if "userChangeable" in klass.__dict__:
            descriptor = klass.__dict__["userChangeable"]
            break
    assert isinstance(descriptor, property)



def test_uma_methodconfiguration_is_not_abstract():
    assert not inspect.isabstract(uma_MethodConfiguration)


def test_uma_methodconfiguration_constructor_exists():
    assert callable(uma_MethodConfiguration.__init__)


def test_uma_methodconfiguration_constructor_args():
    sig = inspect.signature(uma_MethodConfiguration.__init__)
    params = list(sig.parameters.keys())



def test_uma_contentdescription_is_not_abstract():
    assert not inspect.isabstract(uma_ContentDescription)


def test_uma_contentdescription_constructor_exists():
    assert callable(uma_ContentDescription.__init__)


def test_uma_contentdescription_constructor_args():
    sig = inspect.signature(uma_ContentDescription.__init__)
    params = list(sig.parameters.keys())
    assert "mainDescription" in params, "Missing parameter 'mainDescription'"
    assert "keyConsiderations" in params, "Missing parameter 'keyConsiderations'"
    assert "externalId" in params, "Missing parameter 'externalId'"
    assert "longPresentationName" in params, "Missing parameter 'longPresentationName'"

def test_uma_contentdescription_has_mainDescription():
    assert hasattr(uma_ContentDescription, "mainDescription")
    descriptor = None
    for klass in uma_ContentDescription.__mro__:
        if "mainDescription" in klass.__dict__:
            descriptor = klass.__dict__["mainDescription"]
            break
    assert isinstance(descriptor, property)

def test_uma_contentdescription_has_keyConsiderations():
    assert hasattr(uma_ContentDescription, "keyConsiderations")
    descriptor = None
    for klass in uma_ContentDescription.__mro__:
        if "keyConsiderations" in klass.__dict__:
            descriptor = klass.__dict__["keyConsiderations"]
            break
    assert isinstance(descriptor, property)

def test_uma_contentdescription_has_externalId():
    assert hasattr(uma_ContentDescription, "externalId")
    descriptor = None
    for klass in uma_ContentDescription.__mro__:
        if "externalId" in klass.__dict__:
            descriptor = klass.__dict__["externalId"]
            break
    assert isinstance(descriptor, property)

def test_uma_contentdescription_has_longPresentationName():
    assert hasattr(uma_ContentDescription, "longPresentationName")
    descriptor = None
    for klass in uma_ContentDescription.__mro__:
        if "longPresentationName" in klass.__dict__:
            descriptor = klass.__dict__["longPresentationName"]
            break
    assert isinstance(descriptor, property)



def test_classifier_is_not_abstract():
    assert not inspect.isabstract(Classifier)


def test_classifier_constructor_exists():
    assert callable(Classifier.__init__)


def test_classifier_constructor_args():
    sig = inspect.signature(Classifier.__init__)
    params = list(sig.parameters.keys())



def test_guidance_is_not_abstract():
    assert not inspect.isabstract(Guidance)


def test_guidance_constructor_exists():
    assert callable(Guidance.__init__)


def test_guidance_constructor_args():
    sig = inspect.signature(Guidance.__init__)
    params = list(sig.parameters.keys())



def test_uma_reusableasset_is_not_abstract():
    assert not inspect.isabstract(uma_ReusableAsset)


def test_uma_reusableasset_constructor_exists():
    assert callable(uma_ReusableAsset.__init__)


def test_uma_reusableasset_constructor_args():
    sig = inspect.signature(uma_ReusableAsset.__init__)
    params = list(sig.parameters.keys())



def test_uma_termdefinition_is_not_abstract():
    assert not inspect.isabstract(uma_TermDefinition)


def test_uma_termdefinition_constructor_exists():
    assert callable(uma_TermDefinition.__init__)


def test_uma_termdefinition_constructor_args():
    sig = inspect.signature(uma_TermDefinition.__init__)
    params = list(sig.parameters.keys())



def test_uma_report_is_not_abstract():
    assert not inspect.isabstract(uma_Report)


def test_uma_report_constructor_exists():
    assert callable(uma_Report.__init__)


def test_uma_report_constructor_args():
    sig = inspect.signature(uma_Report.__init__)
    params = list(sig.parameters.keys())



def test_uma_practice_is_not_abstract():
    assert not inspect.isabstract(uma_Practice)


def test_uma_practice_constructor_exists():
    assert callable(uma_Practice.__init__)


def test_uma_practice_constructor_args():
    sig = inspect.signature(uma_Practice.__init__)
    params = list(sig.parameters.keys())



def test_uma_roadmap_is_not_abstract():
    assert not inspect.isabstract(uma_Roadmap)


def test_uma_roadmap_constructor_exists():
    assert callable(uma_Roadmap.__init__)


def test_uma_roadmap_constructor_args():
    sig = inspect.signature(uma_Roadmap.__init__)
    params = list(sig.parameters.keys())



def test_uma_estimationconsiderations_is_not_abstract():
    assert not inspect.isabstract(uma_EstimationConsiderations)


def test_uma_estimationconsiderations_constructor_exists():
    assert callable(uma_EstimationConsiderations.__init__)


def test_uma_estimationconsiderations_constructor_args():
    sig = inspect.signature(uma_EstimationConsiderations.__init__)
    params = list(sig.parameters.keys())



def test_uma_toolmentor_is_not_abstract():
    assert not inspect.isabstract(uma_ToolMentor)


def test_uma_toolmentor_constructor_exists():
    assert callable(uma_ToolMentor.__init__)


def test_uma_toolmentor_constructor_args():
    sig = inspect.signature(uma_ToolMentor.__init__)
    params = list(sig.parameters.keys())



def test_uma_template_is_not_abstract():
    assert not inspect.isabstract(uma_Template)


def test_uma_template_constructor_exists():
    assert callable(uma_Template.__init__)


def test_uma_template_constructor_args():
    sig = inspect.signature(uma_Template.__init__)
    params = list(sig.parameters.keys())



def test_uma_example_is_not_abstract():
    assert not inspect.isabstract(uma_Example)


def test_uma_example_constructor_exists():
    assert callable(uma_Example.__init__)


def test_uma_example_constructor_args():
    sig = inspect.signature(uma_Example.__init__)
    params = list(sig.parameters.keys())



def test_uma_guideline_is_not_abstract():
    assert not inspect.isabstract(uma_Guideline)


def test_uma_guideline_constructor_exists():
    assert callable(uma_Guideline.__init__)


def test_uma_guideline_constructor_args():
    sig = inspect.signature(uma_Guideline.__init__)
    params = list(sig.parameters.keys())



def test_uma_checklist_is_not_abstract():
    assert not inspect.isabstract(uma_Checklist)


def test_uma_checklist_constructor_exists():
    assert callable(uma_Checklist.__init__)


def test_uma_checklist_constructor_args():
    sig = inspect.signature(uma_Checklist.__init__)
    params = list(sig.parameters.keys())



def test_uma_concept_is_not_abstract():
    assert not inspect.isabstract(uma_Concept)


def test_uma_concept_constructor_exists():
    assert callable(uma_Concept.__init__)


def test_uma_concept_constructor_args():
    sig = inspect.signature(uma_Concept.__init__)
    params = list(sig.parameters.keys())



def test_uma_supportingmaterial_is_not_abstract():
    assert not inspect.isabstract(uma_SupportingMaterial)


def test_uma_supportingmaterial_constructor_exists():
    assert callable(uma_SupportingMaterial.__init__)


def test_uma_supportingmaterial_constructor_args():
    sig = inspect.signature(uma_SupportingMaterial.__init__)
    params = list(sig.parameters.keys())



def test_variabilityelement_is_not_abstract():
    assert not inspect.isabstract(VariabilityElement)


def test_variabilityelement_constructor_exists():
    assert callable(VariabilityElement.__init__)


def test_variabilityelement_constructor_args():
    sig = inspect.signature(VariabilityElement.__init__)
    params = list(sig.parameters.keys())



def test_uma_activity_is_not_abstract():
    assert not inspect.isabstract(uma_Activity)


def test_uma_activity_constructor_exists():
    assert callable(uma_Activity.__init__)


def test_uma_activity_constructor_args():
    sig = inspect.signature(uma_Activity.__init__)
    params = list(sig.parameters.keys())



def test_uma_section_is_not_abstract():
    assert not inspect.isabstract(uma_Section)


def test_uma_section_constructor_exists():
    assert callable(uma_Section.__init__)


def test_uma_section_constructor_args():
    sig = inspect.signature(uma_Section.__init__)
    params = list(sig.parameters.keys())
    assert "sectionDescription" in params, "Missing parameter 'sectionDescription'"
    assert "sectionName" in params, "Missing parameter 'sectionName'"

def test_uma_section_has_sectionDescription():
    assert hasattr(uma_Section, "sectionDescription")
    descriptor = None
    for klass in uma_Section.__mro__:
        if "sectionDescription" in klass.__dict__:
            descriptor = klass.__dict__["sectionDescription"]
            break
    assert isinstance(descriptor, property)

def test_uma_section_has_sectionName():
    assert hasattr(uma_Section, "sectionName")
    descriptor = None
    for klass in uma_Section.__mro__:
        if "sectionName" in klass.__dict__:
            descriptor = klass.__dict__["sectionName"]
            break
    assert isinstance(descriptor, property)



def test_describableelement_is_not_abstract():
    assert not inspect.isabstract(DescribableElement)


def test_describableelement_constructor_exists():
    assert callable(DescribableElement.__init__)


def test_describableelement_constructor_args():
    sig = inspect.signature(DescribableElement.__init__)
    params = list(sig.parameters.keys())



def test_uma_fulfillableelement_is_not_abstract():
    assert not inspect.isabstract(uma_FulfillableElement)


def test_uma_fulfillableelement_constructor_exists():
    assert callable(uma_FulfillableElement.__init__)


def test_uma_fulfillableelement_constructor_args():
    sig = inspect.signature(uma_FulfillableElement.__init__)
    params = list(sig.parameters.keys())



def test_uma_processelement_is_not_abstract():
    assert not inspect.isabstract(uma_ProcessElement)


def test_uma_processelement_constructor_exists():
    assert callable(uma_ProcessElement.__init__)


def test_uma_processelement_constructor_args():
    sig = inspect.signature(uma_ProcessElement.__init__)
    params = list(sig.parameters.keys())



def test_uma_contentelement_is_not_abstract():
    assert not inspect.isabstract(uma_ContentElement)


def test_uma_contentelement_constructor_exists():
    assert callable(uma_ContentElement.__init__)


def test_uma_contentelement_constructor_args():
    sig = inspect.signature(uma_ContentElement.__init__)
    params = list(sig.parameters.keys())



def test_uma_applicablemetaclassinfo_is_not_abstract():
    assert not inspect.isabstract(uma_ApplicableMetaClassInfo)


def test_uma_applicablemetaclassinfo_constructor_exists():
    assert callable(uma_ApplicableMetaClassInfo.__init__)


def test_uma_applicablemetaclassinfo_constructor_args():
    sig = inspect.signature(uma_ApplicableMetaClassInfo.__init__)
    params = list(sig.parameters.keys())
    assert "isPrimaryExtension" in params, "Missing parameter 'isPrimaryExtension'"

def test_uma_applicablemetaclassinfo_has_isPrimaryExtension():
    assert hasattr(uma_ApplicableMetaClassInfo, "isPrimaryExtension")
    descriptor = None
    for klass in uma_ApplicableMetaClassInfo.__mro__:
        if "isPrimaryExtension" in klass.__dict__:
            descriptor = klass.__dict__["isPrimaryExtension"]
            break
    assert isinstance(descriptor, property)



def test_contentelement_is_not_abstract():
    assert not inspect.isabstract(ContentElement)


def test_contentelement_constructor_exists():
    assert callable(ContentElement.__init__)


def test_contentelement_constructor_args():
    sig = inspect.signature(ContentElement.__init__)
    params = list(sig.parameters.keys())



def test_uma_guidance_is_not_abstract():
    assert not inspect.isabstract(uma_Guidance)


def test_uma_guidance_constructor_exists():
    assert callable(uma_Guidance.__init__)


def test_uma_guidance_constructor_args():
    sig = inspect.signature(uma_Guidance.__init__)
    params = list(sig.parameters.keys())



def test_uma_kind_is_not_abstract():
    assert not inspect.isabstract(uma_Kind)


def test_uma_kind_constructor_exists():
    assert callable(uma_Kind.__init__)


def test_uma_kind_constructor_args():
    sig = inspect.signature(uma_Kind.__init__)
    params = list(sig.parameters.keys())



def test_uma_contentcategory_is_not_abstract():
    assert not inspect.isabstract(uma_ContentCategory)


def test_uma_contentcategory_constructor_exists():
    assert callable(uma_ContentCategory.__init__)


def test_uma_contentcategory_constructor_args():
    sig = inspect.signature(uma_ContentCategory.__init__)
    params = list(sig.parameters.keys())



def test_uma_workproduct_is_not_abstract():
    assert not inspect.isabstract(uma_WorkProduct)


def test_uma_workproduct_constructor_exists():
    assert callable(uma_WorkProduct.__init__)


def test_uma_workproduct_constructor_args():
    sig = inspect.signature(uma_WorkProduct.__init__)
    params = list(sig.parameters.keys())



def test_uma_task_is_not_abstract():
    assert not inspect.isabstract(uma_Task)


def test_uma_task_constructor_exists():
    assert callable(uma_Task.__init__)


def test_uma_task_constructor_args():
    sig = inspect.signature(uma_Task.__init__)
    params = list(sig.parameters.keys())



def test_uma_role_is_not_abstract():
    assert not inspect.isabstract(uma_Role)


def test_uma_role_constructor_exists():
    assert callable(uma_Role.__init__)


def test_uma_role_constructor_args():
    sig = inspect.signature(uma_Role.__init__)
    params = list(sig.parameters.keys())



def test_uma_element_is_not_abstract():
    assert not inspect.isabstract(uma_Element)


def test_uma_element_constructor_exists():
    assert callable(uma_Element.__init__)


def test_uma_element_constructor_args():
    sig = inspect.signature(uma_Element.__init__)
    params = list(sig.parameters.keys())



def test_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_element_constructor_exists():
    assert callable(Element.__init__)


def test_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_uma_namedelement_is_not_abstract():
    assert not inspect.isabstract(uma_NamedElement)


def test_uma_namedelement_constructor_exists():
    assert callable(uma_NamedElement.__init__)


def test_uma_namedelement_constructor_args():
    sig = inspect.signature(uma_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_uma_namedelement_has_name():
    assert hasattr(uma_NamedElement, "name")
    descriptor = None
    for klass in uma_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_uma_packageableelement_is_not_abstract():
    assert not inspect.isabstract(uma_PackageableElement)


def test_uma_packageableelement_constructor_exists():
    assert callable(uma_PackageableElement.__init__)


def test_uma_packageableelement_constructor_args():
    sig = inspect.signature(uma_PackageableElement.__init__)
    params = list(sig.parameters.keys())



def test_packageableelement_is_not_abstract():
    assert not inspect.isabstract(PackageableElement)


def test_packageableelement_constructor_exists():
    assert callable(PackageableElement.__init__)


def test_packageableelement_constructor_args():
    sig = inspect.signature(PackageableElement.__init__)
    params = list(sig.parameters.keys())



def test_uma_methodelementproperty_is_not_abstract():
    assert not inspect.isabstract(uma_MethodElementProperty)


def test_uma_methodelementproperty_constructor_exists():
    assert callable(uma_MethodElementProperty.__init__)


def test_uma_methodelementproperty_constructor_args():
    sig = inspect.signature(uma_MethodElementProperty.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_uma_methodelementproperty_has_value():
    assert hasattr(uma_MethodElementProperty, "value")
    descriptor = None
    for klass in uma_MethodElementProperty.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_uma_methodelement_is_not_abstract():
    assert not inspect.isabstract(uma_MethodElement)


def test_uma_methodelement_constructor_exists():
    assert callable(uma_MethodElement.__init__)


def test_uma_methodelement_constructor_args():
    sig = inspect.signature(uma_MethodElement.__init__)
    params = list(sig.parameters.keys())
    assert "presentationName" in params, "Missing parameter 'presentationName'"
    assert "suppressed" in params, "Missing parameter 'suppressed'"
    assert "briefDescription" in params, "Missing parameter 'briefDescription'"
    assert "orderingGuide" in params, "Missing parameter 'orderingGuide'"
    assert "guid" in params, "Missing parameter 'guid'"

def test_uma_methodelement_has_presentationName():
    assert hasattr(uma_MethodElement, "presentationName")
    descriptor = None
    for klass in uma_MethodElement.__mro__:
        if "presentationName" in klass.__dict__:
            descriptor = klass.__dict__["presentationName"]
            break
    assert isinstance(descriptor, property)

def test_uma_methodelement_has_suppressed():
    assert hasattr(uma_MethodElement, "suppressed")
    descriptor = None
    for klass in uma_MethodElement.__mro__:
        if "suppressed" in klass.__dict__:
            descriptor = klass.__dict__["suppressed"]
            break
    assert isinstance(descriptor, property)

def test_uma_methodelement_has_briefDescription():
    assert hasattr(uma_MethodElement, "briefDescription")
    descriptor = None
    for klass in uma_MethodElement.__mro__:
        if "briefDescription" in klass.__dict__:
            descriptor = klass.__dict__["briefDescription"]
            break
    assert isinstance(descriptor, property)

def test_uma_methodelement_has_orderingGuide():
    assert hasattr(uma_MethodElement, "orderingGuide")
    descriptor = None
    for klass in uma_MethodElement.__mro__:
        if "orderingGuide" in klass.__dict__:
            descriptor = klass.__dict__["orderingGuide"]
            break
    assert isinstance(descriptor, property)

def test_uma_methodelement_has_guid():
    assert hasattr(uma_MethodElement, "guid")
    descriptor = None
    for klass in uma_MethodElement.__mro__:
        if "guid" in klass.__dict__:
            descriptor = klass.__dict__["guid"]
            break
    assert isinstance(descriptor, property)



def test_uma_type_is_not_abstract():
    assert not inspect.isabstract(uma_Type)


def test_uma_type_constructor_exists():
    assert callable(uma_Type.__init__)


def test_uma_type_constructor_args():
    sig = inspect.signature(uma_Type.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_uma_classifier_is_not_abstract():
    assert not inspect.isabstract(uma_Classifier)


def test_uma_classifier_constructor_exists():
    assert callable(uma_Classifier.__init__)


def test_uma_classifier_constructor_args():
    sig = inspect.signature(uma_Classifier.__init__)
    params = list(sig.parameters.keys())
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"

def test_uma_classifier_has_isAbstract():
    assert hasattr(uma_Classifier, "isAbstract")
    descriptor = None
    for klass in uma_Classifier.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)



def test_methodelement_is_not_abstract():
    assert not inspect.isabstract(MethodElement)


def test_methodelement_constructor_exists():
    assert callable(MethodElement.__init__)


def test_methodelement_constructor_args():
    sig = inspect.signature(MethodElement.__init__)
    params = list(sig.parameters.keys())



def test_uma_diagramelement_is_not_abstract():
    assert not inspect.isabstract(uma_DiagramElement)


def test_uma_diagramelement_constructor_exists():
    assert callable(uma_DiagramElement.__init__)


def test_uma_diagramelement_constructor_args():
    sig = inspect.signature(uma_DiagramElement.__init__)
    params = list(sig.parameters.keys())
    assert "isVisible" in params, "Missing parameter 'isVisible'"

def test_uma_diagramelement_has_isVisible():
    assert hasattr(uma_DiagramElement, "isVisible")
    descriptor = None
    for klass in uma_DiagramElement.__mro__:
        if "isVisible" in klass.__dict__:
            descriptor = klass.__dict__["isVisible"]
            break
    assert isinstance(descriptor, property)



def test_uma_workdefinition_is_not_abstract():
    assert not inspect.isabstract(uma_WorkDefinition)


def test_uma_workdefinition_constructor_exists():
    assert callable(uma_WorkDefinition.__init__)


def test_uma_workdefinition_constructor_args():
    sig = inspect.signature(uma_WorkDefinition.__init__)
    params = list(sig.parameters.keys())



def test_uma_methodunit_is_not_abstract():
    assert not inspect.isabstract(uma_MethodUnit)


def test_uma_methodunit_constructor_exists():
    assert callable(uma_MethodUnit.__init__)


def test_uma_methodunit_constructor_args():
    sig = inspect.signature(uma_MethodUnit.__init__)
    params = list(sig.parameters.keys())
    assert "changeDescription" in params, "Missing parameter 'changeDescription'"
    assert "version" in params, "Missing parameter 'version'"
    assert "authors" in params, "Missing parameter 'authors'"
    assert "changeDate" in params, "Missing parameter 'changeDate'"

def test_uma_methodunit_has_changeDescription():
    assert hasattr(uma_MethodUnit, "changeDescription")
    descriptor = None
    for klass in uma_MethodUnit.__mro__:
        if "changeDescription" in klass.__dict__:
            descriptor = klass.__dict__["changeDescription"]
            break
    assert isinstance(descriptor, property)

def test_uma_methodunit_has_version():
    assert hasattr(uma_MethodUnit, "version")
    descriptor = None
    for klass in uma_MethodUnit.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_uma_methodunit_has_authors():
    assert hasattr(uma_MethodUnit, "authors")
    descriptor = None
    for klass in uma_MethodUnit.__mro__:
        if "authors" in klass.__dict__:
            descriptor = klass.__dict__["authors"]
            break
    assert isinstance(descriptor, property)

def test_uma_methodunit_has_changeDate():
    assert hasattr(uma_MethodUnit, "changeDate")
    descriptor = None
    for klass in uma_MethodUnit.__mro__:
        if "changeDate" in klass.__dict__:
            descriptor = klass.__dict__["changeDate"]
            break
    assert isinstance(descriptor, property)



def test_uma_describableelement_is_not_abstract():
    assert not inspect.isabstract(uma_DescribableElement)


def test_uma_describableelement_constructor_exists():
    assert callable(uma_DescribableElement.__init__)


def test_uma_describableelement_constructor_args():
    sig = inspect.signature(uma_DescribableElement.__init__)
    params = list(sig.parameters.keys())
    assert "nodeicon" in params, "Missing parameter 'nodeicon'"
    assert "shapeicon" in params, "Missing parameter 'shapeicon'"

def test_uma_describableelement_has_nodeicon():
    assert hasattr(uma_DescribableElement, "nodeicon")
    descriptor = None
    for klass in uma_DescribableElement.__mro__:
        if "nodeicon" in klass.__dict__:
            descriptor = klass.__dict__["nodeicon"]
            break
    assert isinstance(descriptor, property)

def test_uma_describableelement_has_shapeicon():
    assert hasattr(uma_DescribableElement, "shapeicon")
    descriptor = None
    for klass in uma_DescribableElement.__mro__:
        if "shapeicon" in klass.__dict__:
            descriptor = klass.__dict__["shapeicon"]
            break
    assert isinstance(descriptor, property)



def test_uma_variabilityelement_is_not_abstract():
    assert not inspect.isabstract(uma_VariabilityElement)


def test_uma_variabilityelement_constructor_exists():
    assert callable(uma_VariabilityElement.__init__)


def test_uma_variabilityelement_constructor_args():
    sig = inspect.signature(uma_VariabilityElement.__init__)
    params = list(sig.parameters.keys())
    assert "variabilityType" in params, "Missing parameter 'variabilityType'"

def test_uma_variabilityelement_has_variabilityType():
    assert hasattr(uma_VariabilityElement, "variabilityType")
    descriptor = None
    for klass in uma_VariabilityElement.__mro__:
        if "variabilityType" in klass.__dict__:
            descriptor = klass.__dict__["variabilityType"]
            break
    assert isinstance(descriptor, property)



def test_uma_methodpackage_is_not_abstract():
    assert not inspect.isabstract(uma_MethodPackage)


def test_uma_methodpackage_constructor_exists():
    assert callable(uma_MethodPackage.__init__)


def test_uma_methodpackage_constructor_args():
    sig = inspect.signature(uma_MethodPackage.__init__)
    params = list(sig.parameters.keys())
    assert "global_" in params, "Missing parameter 'global_'"

def test_uma_methodpackage_has_global_():
    assert hasattr(uma_MethodPackage, "global_")
    descriptor = None
    for klass in uma_MethodPackage.__mro__:
        if "global_" in klass.__dict__:
            descriptor = klass.__dict__["global_"]
            break
    assert isinstance(descriptor, property)



def test_uma_constraint_is_not_abstract():
    assert not inspect.isabstract(uma_Constraint)


def test_uma_constraint_constructor_exists():
    assert callable(uma_Constraint.__init__)


def test_uma_constraint_constructor_args():
    sig = inspect.signature(uma_Constraint.__init__)
    params = list(sig.parameters.keys())
    assert "body" in params, "Missing parameter 'body'"

def test_uma_constraint_has_body():
    assert hasattr(uma_Constraint, "body")
    descriptor = None
    for klass in uma_Constraint.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)



def test_uma_namespace_is_not_abstract():
    assert not inspect.isabstract(uma_Namespace)


def test_uma_namespace_constructor_exists():
    assert callable(uma_Namespace.__init__)


def test_uma_namespace_constructor_args():
    sig = inspect.signature(uma_Namespace.__init__)
    params = list(sig.parameters.keys())



def test_namespace_is_not_abstract():
    assert not inspect.isabstract(Namespace)


def test_namespace_constructor_exists():
    assert callable(Namespace.__init__)


def test_namespace_constructor_args():
    sig = inspect.signature(Namespace.__init__)
    params = list(sig.parameters.keys())



def test_uma_package_is_not_abstract():
    assert not inspect.isabstract(uma_Package)


def test_uma_package_constructor_exists():
    assert callable(uma_Package.__init__)


def test_uma_package_constructor_args():
    sig = inspect.signature(uma_Package.__init__)
    params = list(sig.parameters.keys())

def test_workordertype_exists():
    # Check that the Enumeration exists
    assert WorkOrderType is not None

def test_workordertype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in WorkOrderType]
    expected_literals = [
        "startToStart",
        "finishToStart",
        "startToFinish",
        "finishToFinish",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in WorkOrderType"

def test_variabilitytype_exists():
    # Check that the Enumeration exists
    assert VariabilityType is not None

def test_variabilitytype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in VariabilityType]
    expected_literals = [
        "na",
        "extendsReplaces",
        "extends",
        "contributes",
        "localReplacement",
        "replaces",
        "localContribution",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in VariabilityType"


# =============================================================================
# HYPOTHESIS STRATEGIES
# =============================================================================

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())
MethodConfiguration_strategy = st.builds(
    MethodConfiguration,
)
uma_ProcessFamily_strategy = st.builds(
    uma_ProcessFamily,
)
GraphicPrimitive_strategy = st.builds(
    GraphicPrimitive,
)
uma_Ellipse_strategy = st.builds(
    uma_Ellipse,
    startAngle=
        safe_text,
    radiusY=
        safe_text,
    endAngle=
        safe_text,
    rotation=
        safe_text,
    radiusX=
        safe_text
)
uma_Polyline_strategy = st.builds(
    uma_Polyline,
    closed=
        safe_text
)
LeafElement_strategy = st.builds(
    LeafElement,
)
uma_Image_strategy = st.builds(
    uma_Image,
    uri=
        safe_text,
    mimeType=
        safe_text
)
uma_GraphicPrimitive_strategy = st.builds(
    uma_GraphicPrimitive,
)
uma_TextElement_strategy = st.builds(
    uma_TextElement,
    text=
        safe_text
)
SemanticModelBridge_strategy = st.builds(
    SemanticModelBridge,
)
uma_CoreSemanticModelBridge_strategy = st.builds(
    uma_CoreSemanticModelBridge,
)
uma_UMASemanticModelBridge_strategy = st.builds(
    uma_UMASemanticModelBridge,
)
uma_SimpleSemanticModelElement_strategy = st.builds(
    uma_SimpleSemanticModelElement,
    typeInfo=
        safe_text
)
GraphElement_strategy = st.builds(
    GraphElement,
)
uma_GraphEdge_strategy = st.builds(
    uma_GraphEdge,
)
uma_GraphNode_strategy = st.builds(
    uma_GraphNode,
)
uma_Point_strategy = st.builds(
    uma_Point,
    x=
        safe_text,
    y=
        safe_text
)
GraphNode_strategy = st.builds(
    GraphNode,
)
uma_Diagram_strategy = st.builds(
    uma_Diagram,
    zoom=
        safe_text
)
ProcessPackage_strategy = st.builds(
    ProcessPackage,
)
uma_GraphConnector_strategy = st.builds(
    uma_GraphConnector,
)
DiagramElement_strategy = st.builds(
    DiagramElement,
)
uma_SemanticModelBridge_strategy = st.builds(
    uma_SemanticModelBridge,
    presentation=
        safe_text
)
uma_Reference_strategy = st.builds(
    uma_Reference,
    isIndividualRepresentation=
        safe_text
)
uma_DiagramLink_strategy = st.builds(
    uma_DiagramLink,
    zoom=
        safe_text
)
uma_Property_strategy = st.builds(
    uma_Property,
    value=
        safe_text,
    key=
        safe_text
)
uma_LeafElement_strategy = st.builds(
    uma_LeafElement,
)
uma_GraphElement_strategy = st.builds(
    uma_GraphElement,
)
uma_Dimension_strategy = st.builds(
    uma_Dimension,
    height=
        safe_text,
    width=
        safe_text
)
ProcessDescription_strategy = st.builds(
    ProcessDescription,
)
uma_DeliveryProcessDescription_strategy = st.builds(
    uma_DeliveryProcessDescription,
    estimatingTechnique=
        safe_text,
    projectCharacteristics=
        safe_text,
    projectMemberExpertise=
        safe_text,
    scale=
        safe_text,
    riskLevel=
        safe_text,
    typeOfContract=
        safe_text
)
BreakdownElementDescription_strategy = st.builds(
    BreakdownElementDescription,
)
uma_ActivityDescription_strategy = st.builds(
    uma_ActivityDescription,
    alternatives=
        safe_text,
    purpose=
        safe_text,
    howtoStaff=
        safe_text
)
uma_DescriptorDescription_strategy = st.builds(
    uma_DescriptorDescription,
    refinedDescription=
        safe_text
)
ActivityDescription_strategy = st.builds(
    ActivityDescription,
)
uma_ProcessDescription_strategy = st.builds(
    uma_ProcessDescription,
    usageNotes=
        safe_text,
    scope=
        safe_text
)
Process_strategy = st.builds(
    Process,
)
uma_CapabilityPattern_strategy = st.builds(
    uma_CapabilityPattern,
)
uma_ProcessPlanningTemplate_strategy = st.builds(
    uma_ProcessPlanningTemplate,
)
uma_DeliveryProcess_strategy = st.builds(
    uma_DeliveryProcess,
)
RoleDescriptor_strategy = st.builds(
    RoleDescriptor,
)
uma_CompositeRole_strategy = st.builds(
    uma_CompositeRole,
)
Descriptor_strategy = st.builds(
    Descriptor,
)
uma_ProcessComponentDescriptor_strategy = st.builds(
    uma_ProcessComponentDescriptor,
)
uma_WorkProductDescriptor_strategy = st.builds(
    uma_WorkProductDescriptor,
    activityExitState=
        safe_text,
    activityEntryState=
        safe_text
)
uma_RoleDescriptor_strategy = st.builds(
    uma_RoleDescriptor,
)
Activity_strategy = st.builds(
    Activity,
)
uma_Phase_strategy = st.builds(
    uma_Phase,
)
uma_Process_strategy = st.builds(
    uma_Process,
)
uma_Iteration_strategy = st.builds(
    uma_Iteration,
)
MethodPackage_strategy = st.builds(
    MethodPackage,
)
uma_ProcessPackage_strategy = st.builds(
    uma_ProcessPackage,
)
uma_ContentPackage_strategy = st.builds(
    uma_ContentPackage,
)
Package_strategy = st.builds(
    Package,
)
ProcessElement_strategy = st.builds(
    ProcessElement,
)
uma_WorkOrder_strategy = st.builds(
    uma_WorkOrder,
    linkType=
        safe_text
)
BreakdownElement_strategy = st.builds(
    BreakdownElement,
)
uma_TeamProfile_strategy = st.builds(
    uma_TeamProfile,
)
uma_Descriptor_strategy = st.builds(
    uma_Descriptor,
    isSynchronizedWithSource=
        safe_text
)
uma_ProcessComponentInterface_strategy = st.builds(
    uma_ProcessComponentInterface,
)
uma_WorkBreakdownElement_strategy = st.builds(
    uma_WorkBreakdownElement,
    isRepeatable=
        safe_text,
    isOngoing=
        safe_text,
    isEventDriven=
        safe_text
)
uma_BreakdownElement_strategy = st.builds(
    uma_BreakdownElement,
    hasMultipleOccurrences=
        safe_text,
    isPlanned=
        safe_text,
    prefix=
        safe_text,
    isOptional=
        safe_text
)
WorkBreakdownElement_strategy = st.builds(
    WorkBreakdownElement,
)
uma_Milestone_strategy = st.builds(
    uma_Milestone,
)
uma_TaskDescriptor_strategy = st.builds(
    uma_TaskDescriptor,
)
uma_PlanningData_strategy = st.builds(
    uma_PlanningData,
    startDate=
        safe_text,
    rank=
        safe_text,
    finishDate=
        safe_text
)
ContentCategory_strategy = st.builds(
    ContentCategory,
)
uma_RoleSetGrouping_strategy = st.builds(
    uma_RoleSetGrouping,
)
uma_Tool_strategy = st.builds(
    uma_Tool,
)
uma_CustomCategory_strategy = st.builds(
    uma_CustomCategory,
)
uma_Domain_strategy = st.builds(
    uma_Domain,
)
uma_DisciplineGrouping_strategy = st.builds(
    uma_DisciplineGrouping,
)
uma_WorkProductType_strategy = st.builds(
    uma_WorkProductType,
)
uma_RoleSet_strategy = st.builds(
    uma_RoleSet,
)
uma_Discipline_strategy = st.builds(
    uma_Discipline,
)
ContentDescription_strategy = st.builds(
    ContentDescription,
)
uma_TaskDescription_strategy = st.builds(
    uma_TaskDescription,
    alternatives=
        safe_text,
    purpose=
        safe_text
)
uma_RoleDescription_strategy = st.builds(
    uma_RoleDescription,
    synonyms=
        safe_text,
    skills=
        safe_text,
    assignmentApproaches=
        safe_text
)
uma_BreakdownElementDescription_strategy = st.builds(
    uma_BreakdownElementDescription,
    usageGuidance=
        safe_text
)
uma_WorkProductDescription_strategy = st.builds(
    uma_WorkProductDescription,
    impactOfNotHaving=
        safe_text,
    purpose=
        safe_text,
    reasonsForNotNeeding=
        safe_text
)
uma_PracticeDescription_strategy = st.builds(
    uma_PracticeDescription,
    goals=
        safe_text,
    background=
        safe_text,
    additionalInfo=
        safe_text,
    levelsOfAdoption=
        safe_text,
    application=
        safe_text,
    problem=
        safe_text
)
uma_GuidanceDescription_strategy = st.builds(
    uma_GuidanceDescription,
    attachments=
        safe_text
)
Concept_strategy = st.builds(
    Concept,
)
uma_Whitepaper_strategy = st.builds(
    uma_Whitepaper,
)
WorkDefinition_strategy = st.builds(
    WorkDefinition,
)
Section_strategy = st.builds(
    Section,
)
uma_Step_strategy = st.builds(
    uma_Step,
)
WorkProductDescription_strategy = st.builds(
    WorkProductDescription,
)
uma_DeliverableDescription_strategy = st.builds(
    uma_DeliverableDescription,
    externalDescription=
        safe_text,
    packagingGuidance=
        safe_text
)
uma_ArtifactDescription_strategy = st.builds(
    uma_ArtifactDescription,
    notation=
        safe_text,
    representationOptions=
        safe_text,
    briefOutline=
        safe_text,
    representation=
        safe_text
)
FulfillableElement_strategy = st.builds(
    FulfillableElement,
)
WorkProduct_strategy = st.builds(
    WorkProduct,
)
uma_Deliverable_strategy = st.builds(
    uma_Deliverable,
)
uma_Outcome_strategy = st.builds(
    uma_Outcome,
)
uma_Artifact_strategy = st.builds(
    uma_Artifact,
)
MethodUnit_strategy = st.builds(
    MethodUnit,
)
uma_ProcessComponent_strategy = st.builds(
    uma_ProcessComponent,
)
uma_MethodLibrary_strategy = st.builds(
    uma_MethodLibrary,
)
uma_MethodPlugin_strategy = st.builds(
    uma_MethodPlugin,
    supporting=
        st.booleans(),
    userChangeable=
        safe_text
)
uma_MethodConfiguration_strategy = st.builds(
    uma_MethodConfiguration,
)
uma_ContentDescription_strategy = st.builds(
    uma_ContentDescription,
    mainDescription=
        safe_text,
    keyConsiderations=
        safe_text,
    externalId=
        safe_text,
    longPresentationName=
        safe_text
)
Classifier_strategy = st.builds(
    Classifier,
)
Guidance_strategy = st.builds(
    Guidance,
)
uma_ReusableAsset_strategy = st.builds(
    uma_ReusableAsset,
)
uma_TermDefinition_strategy = st.builds(
    uma_TermDefinition,
)
uma_Report_strategy = st.builds(
    uma_Report,
)
uma_Practice_strategy = st.builds(
    uma_Practice,
)
uma_Roadmap_strategy = st.builds(
    uma_Roadmap,
)
uma_EstimationConsiderations_strategy = st.builds(
    uma_EstimationConsiderations,
)
uma_ToolMentor_strategy = st.builds(
    uma_ToolMentor,
)
uma_Template_strategy = st.builds(
    uma_Template,
)
uma_Example_strategy = st.builds(
    uma_Example,
)
uma_Guideline_strategy = st.builds(
    uma_Guideline,
)
uma_Checklist_strategy = st.builds(
    uma_Checklist,
)
uma_Concept_strategy = st.builds(
    uma_Concept,
)
uma_SupportingMaterial_strategy = st.builds(
    uma_SupportingMaterial,
)
VariabilityElement_strategy = st.builds(
    VariabilityElement,
)
uma_Activity_strategy = st.builds(
    uma_Activity,
)
uma_Section_strategy = st.builds(
    uma_Section,
    sectionDescription=
        safe_text,
    sectionName=
        safe_text
)
DescribableElement_strategy = st.builds(
    DescribableElement,
)
uma_FulfillableElement_strategy = st.builds(
    uma_FulfillableElement,
)
uma_ProcessElement_strategy = st.builds(
    uma_ProcessElement,
)
uma_ContentElement_strategy = st.builds(
    uma_ContentElement,
)
uma_ApplicableMetaClassInfo_strategy = st.builds(
    uma_ApplicableMetaClassInfo,
    isPrimaryExtension=
        safe_text
)
ContentElement_strategy = st.builds(
    ContentElement,
)
uma_Guidance_strategy = st.builds(
    uma_Guidance,
)
uma_Kind_strategy = st.builds(
    uma_Kind,
)
uma_ContentCategory_strategy = st.builds(
    uma_ContentCategory,
)
uma_WorkProduct_strategy = st.builds(
    uma_WorkProduct,
)
uma_Task_strategy = st.builds(
    uma_Task,
)
uma_Role_strategy = st.builds(
    uma_Role,
)
uma_Element_strategy = st.builds(
    uma_Element,
)
Element_strategy = st.builds(
    Element,
)
uma_NamedElement_strategy = st.builds(
    uma_NamedElement,
    name=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
uma_PackageableElement_strategy = st.builds(
    uma_PackageableElement,
)
PackageableElement_strategy = st.builds(
    PackageableElement,
)
uma_MethodElementProperty_strategy = st.builds(
    uma_MethodElementProperty,
    value=
        safe_text
)
uma_MethodElement_strategy = st.builds(
    uma_MethodElement,
    presentationName=
        safe_text,
    suppressed=
        safe_text,
    briefDescription=
        safe_text,
    orderingGuide=
        safe_text,
    guid=
        safe_text
)
uma_Type_strategy = st.builds(
    uma_Type,
)
Type_strategy = st.builds(
    Type,
)
uma_Classifier_strategy = st.builds(
    uma_Classifier,
    isAbstract=
        safe_text
)
MethodElement_strategy = st.builds(
    MethodElement,
)
uma_DiagramElement_strategy = st.builds(
    uma_DiagramElement,
    isVisible=
        safe_text
)
uma_WorkDefinition_strategy = st.builds(
    uma_WorkDefinition,
)
uma_MethodUnit_strategy = st.builds(
    uma_MethodUnit,
    changeDescription=
        safe_text,
    version=
        safe_text,
    authors=
        safe_text,
    changeDate=
        safe_text
)
uma_DescribableElement_strategy = st.builds(
    uma_DescribableElement,
    nodeicon=
        safe_text,
    shapeicon=
        safe_text
)
uma_VariabilityElement_strategy = st.builds(
    uma_VariabilityElement,
    variabilityType=
        safe_text
)
uma_MethodPackage_strategy = st.builds(
    uma_MethodPackage,
    global_=
        safe_text
)
uma_Constraint_strategy = st.builds(
    uma_Constraint,
    body=
        safe_text
)
uma_Namespace_strategy = st.builds(
    uma_Namespace,
)
Namespace_strategy = st.builds(
    Namespace,
)
uma_Package_strategy = st.builds(
    uma_Package,
)

@given(instance=MethodConfiguration_strategy)
@settings(max_examples=50)
def test_methodconfiguration_instantiation(instance):
    assert isinstance(instance, MethodConfiguration)

@given(instance=uma_ProcessFamily_strategy)
@settings(max_examples=50)
def test_uma_processfamily_instantiation(instance):
    assert isinstance(instance, uma_ProcessFamily)

@given(instance=GraphicPrimitive_strategy)
@settings(max_examples=50)
def test_graphicprimitive_instantiation(instance):
    assert isinstance(instance, GraphicPrimitive)

@given(instance=uma_Ellipse_strategy)
@settings(max_examples=50)
def test_uma_ellipse_instantiation(instance):
    assert isinstance(instance, uma_Ellipse)



@given(instance=uma_Ellipse_strategy)
def test_uma_ellipse_startAngle_setter(instance):
    original = instance.startAngle
    instance.startAngle = original
    assert instance.startAngle == original



@given(instance=uma_Ellipse_strategy)
def test_uma_ellipse_radiusY_setter(instance):
    original = instance.radiusY
    instance.radiusY = original
    assert instance.radiusY == original



@given(instance=uma_Ellipse_strategy)
def test_uma_ellipse_endAngle_setter(instance):
    original = instance.endAngle
    instance.endAngle = original
    assert instance.endAngle == original



@given(instance=uma_Ellipse_strategy)
def test_uma_ellipse_rotation_setter(instance):
    original = instance.rotation
    instance.rotation = original
    assert instance.rotation == original



@given(instance=uma_Ellipse_strategy)
def test_uma_ellipse_radiusX_setter(instance):
    original = instance.radiusX
    instance.radiusX = original
    assert instance.radiusX == original

@given(instance=uma_Polyline_strategy)
@settings(max_examples=50)
def test_uma_polyline_instantiation(instance):
    assert isinstance(instance, uma_Polyline)



@given(instance=uma_Polyline_strategy)
def test_uma_polyline_closed_setter(instance):
    original = instance.closed
    instance.closed = original
    assert instance.closed == original

@given(instance=LeafElement_strategy)
@settings(max_examples=50)
def test_leafelement_instantiation(instance):
    assert isinstance(instance, LeafElement)

@given(instance=uma_Image_strategy)
@settings(max_examples=50)
def test_uma_image_instantiation(instance):
    assert isinstance(instance, uma_Image)



@given(instance=uma_Image_strategy)
def test_uma_image_uri_setter(instance):
    original = instance.uri
    instance.uri = original
    assert instance.uri == original



@given(instance=uma_Image_strategy)
def test_uma_image_mimeType_setter(instance):
    original = instance.mimeType
    instance.mimeType = original
    assert instance.mimeType == original

@given(instance=uma_GraphicPrimitive_strategy)
@settings(max_examples=50)
def test_uma_graphicprimitive_instantiation(instance):
    assert isinstance(instance, uma_GraphicPrimitive)

@given(instance=uma_TextElement_strategy)
@settings(max_examples=50)
def test_uma_textelement_instantiation(instance):
    assert isinstance(instance, uma_TextElement)



@given(instance=uma_TextElement_strategy)
def test_uma_textelement_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=SemanticModelBridge_strategy)
@settings(max_examples=50)
def test_semanticmodelbridge_instantiation(instance):
    assert isinstance(instance, SemanticModelBridge)

@given(instance=uma_CoreSemanticModelBridge_strategy)
@settings(max_examples=50)
def test_uma_coresemanticmodelbridge_instantiation(instance):
    assert isinstance(instance, uma_CoreSemanticModelBridge)

@given(instance=uma_UMASemanticModelBridge_strategy)
@settings(max_examples=50)
def test_uma_umasemanticmodelbridge_instantiation(instance):
    assert isinstance(instance, uma_UMASemanticModelBridge)

@given(instance=uma_SimpleSemanticModelElement_strategy)
@settings(max_examples=50)
def test_uma_simplesemanticmodelelement_instantiation(instance):
    assert isinstance(instance, uma_SimpleSemanticModelElement)



@given(instance=uma_SimpleSemanticModelElement_strategy)
def test_uma_simplesemanticmodelelement_typeInfo_setter(instance):
    original = instance.typeInfo
    instance.typeInfo = original
    assert instance.typeInfo == original

@given(instance=GraphElement_strategy)
@settings(max_examples=50)
def test_graphelement_instantiation(instance):
    assert isinstance(instance, GraphElement)

@given(instance=uma_GraphEdge_strategy)
@settings(max_examples=50)
def test_uma_graphedge_instantiation(instance):
    assert isinstance(instance, uma_GraphEdge)

@given(instance=uma_GraphNode_strategy)
@settings(max_examples=50)
def test_uma_graphnode_instantiation(instance):
    assert isinstance(instance, uma_GraphNode)

@given(instance=uma_Point_strategy)
@settings(max_examples=50)
def test_uma_point_instantiation(instance):
    assert isinstance(instance, uma_Point)



@given(instance=uma_Point_strategy)
def test_uma_point_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=uma_Point_strategy)
def test_uma_point_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=GraphNode_strategy)
@settings(max_examples=50)
def test_graphnode_instantiation(instance):
    assert isinstance(instance, GraphNode)

@given(instance=uma_Diagram_strategy)
@settings(max_examples=50)
def test_uma_diagram_instantiation(instance):
    assert isinstance(instance, uma_Diagram)



@given(instance=uma_Diagram_strategy)
def test_uma_diagram_zoom_setter(instance):
    original = instance.zoom
    instance.zoom = original
    assert instance.zoom == original

@given(instance=ProcessPackage_strategy)
@settings(max_examples=50)
def test_processpackage_instantiation(instance):
    assert isinstance(instance, ProcessPackage)

@given(instance=uma_GraphConnector_strategy)
@settings(max_examples=50)
def test_uma_graphconnector_instantiation(instance):
    assert isinstance(instance, uma_GraphConnector)

@given(instance=DiagramElement_strategy)
@settings(max_examples=50)
def test_diagramelement_instantiation(instance):
    assert isinstance(instance, DiagramElement)

@given(instance=uma_SemanticModelBridge_strategy)
@settings(max_examples=50)
def test_uma_semanticmodelbridge_instantiation(instance):
    assert isinstance(instance, uma_SemanticModelBridge)



@given(instance=uma_SemanticModelBridge_strategy)
def test_uma_semanticmodelbridge_presentation_setter(instance):
    original = instance.presentation
    instance.presentation = original
    assert instance.presentation == original

@given(instance=uma_Reference_strategy)
@settings(max_examples=50)
def test_uma_reference_instantiation(instance):
    assert isinstance(instance, uma_Reference)



@given(instance=uma_Reference_strategy)
def test_uma_reference_isIndividualRepresentation_setter(instance):
    original = instance.isIndividualRepresentation
    instance.isIndividualRepresentation = original
    assert instance.isIndividualRepresentation == original

@given(instance=uma_DiagramLink_strategy)
@settings(max_examples=50)
def test_uma_diagramlink_instantiation(instance):
    assert isinstance(instance, uma_DiagramLink)



@given(instance=uma_DiagramLink_strategy)
def test_uma_diagramlink_zoom_setter(instance):
    original = instance.zoom
    instance.zoom = original
    assert instance.zoom == original

@given(instance=uma_Property_strategy)
@settings(max_examples=50)
def test_uma_property_instantiation(instance):
    assert isinstance(instance, uma_Property)



@given(instance=uma_Property_strategy)
def test_uma_property_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=uma_Property_strategy)
def test_uma_property_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=uma_LeafElement_strategy)
@settings(max_examples=50)
def test_uma_leafelement_instantiation(instance):
    assert isinstance(instance, uma_LeafElement)

@given(instance=uma_GraphElement_strategy)
@settings(max_examples=50)
def test_uma_graphelement_instantiation(instance):
    assert isinstance(instance, uma_GraphElement)

@given(instance=uma_Dimension_strategy)
@settings(max_examples=50)
def test_uma_dimension_instantiation(instance):
    assert isinstance(instance, uma_Dimension)



@given(instance=uma_Dimension_strategy)
def test_uma_dimension_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original



@given(instance=uma_Dimension_strategy)
def test_uma_dimension_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=ProcessDescription_strategy)
@settings(max_examples=50)
def test_processdescription_instantiation(instance):
    assert isinstance(instance, ProcessDescription)

@given(instance=uma_DeliveryProcessDescription_strategy)
@settings(max_examples=50)
def test_uma_deliveryprocessdescription_instantiation(instance):
    assert isinstance(instance, uma_DeliveryProcessDescription)



@given(instance=uma_DeliveryProcessDescription_strategy)
def test_uma_deliveryprocessdescription_estimatingTechnique_setter(instance):
    original = instance.estimatingTechnique
    instance.estimatingTechnique = original
    assert instance.estimatingTechnique == original



@given(instance=uma_DeliveryProcessDescription_strategy)
def test_uma_deliveryprocessdescription_projectCharacteristics_setter(instance):
    original = instance.projectCharacteristics
    instance.projectCharacteristics = original
    assert instance.projectCharacteristics == original



@given(instance=uma_DeliveryProcessDescription_strategy)
def test_uma_deliveryprocessdescription_projectMemberExpertise_setter(instance):
    original = instance.projectMemberExpertise
    instance.projectMemberExpertise = original
    assert instance.projectMemberExpertise == original



@given(instance=uma_DeliveryProcessDescription_strategy)
def test_uma_deliveryprocessdescription_scale_setter(instance):
    original = instance.scale
    instance.scale = original
    assert instance.scale == original



@given(instance=uma_DeliveryProcessDescription_strategy)
def test_uma_deliveryprocessdescription_riskLevel_setter(instance):
    original = instance.riskLevel
    instance.riskLevel = original
    assert instance.riskLevel == original



@given(instance=uma_DeliveryProcessDescription_strategy)
def test_uma_deliveryprocessdescription_typeOfContract_setter(instance):
    original = instance.typeOfContract
    instance.typeOfContract = original
    assert instance.typeOfContract == original

@given(instance=BreakdownElementDescription_strategy)
@settings(max_examples=50)
def test_breakdownelementdescription_instantiation(instance):
    assert isinstance(instance, BreakdownElementDescription)

@given(instance=uma_ActivityDescription_strategy)
@settings(max_examples=50)
def test_uma_activitydescription_instantiation(instance):
    assert isinstance(instance, uma_ActivityDescription)



@given(instance=uma_ActivityDescription_strategy)
def test_uma_activitydescription_alternatives_setter(instance):
    original = instance.alternatives
    instance.alternatives = original
    assert instance.alternatives == original



@given(instance=uma_ActivityDescription_strategy)
def test_uma_activitydescription_purpose_setter(instance):
    original = instance.purpose
    instance.purpose = original
    assert instance.purpose == original



@given(instance=uma_ActivityDescription_strategy)
def test_uma_activitydescription_howtoStaff_setter(instance):
    original = instance.howtoStaff
    instance.howtoStaff = original
    assert instance.howtoStaff == original

@given(instance=uma_DescriptorDescription_strategy)
@settings(max_examples=50)
def test_uma_descriptordescription_instantiation(instance):
    assert isinstance(instance, uma_DescriptorDescription)



@given(instance=uma_DescriptorDescription_strategy)
def test_uma_descriptordescription_refinedDescription_setter(instance):
    original = instance.refinedDescription
    instance.refinedDescription = original
    assert instance.refinedDescription == original

@given(instance=ActivityDescription_strategy)
@settings(max_examples=50)
def test_activitydescription_instantiation(instance):
    assert isinstance(instance, ActivityDescription)

@given(instance=uma_ProcessDescription_strategy)
@settings(max_examples=50)
def test_uma_processdescription_instantiation(instance):
    assert isinstance(instance, uma_ProcessDescription)



@given(instance=uma_ProcessDescription_strategy)
def test_uma_processdescription_usageNotes_setter(instance):
    original = instance.usageNotes
    instance.usageNotes = original
    assert instance.usageNotes == original



@given(instance=uma_ProcessDescription_strategy)
def test_uma_processdescription_scope_setter(instance):
    original = instance.scope
    instance.scope = original
    assert instance.scope == original

@given(instance=Process_strategy)
@settings(max_examples=50)
def test_process_instantiation(instance):
    assert isinstance(instance, Process)

@given(instance=uma_CapabilityPattern_strategy)
@settings(max_examples=50)
def test_uma_capabilitypattern_instantiation(instance):
    assert isinstance(instance, uma_CapabilityPattern)

@given(instance=uma_ProcessPlanningTemplate_strategy)
@settings(max_examples=50)
def test_uma_processplanningtemplate_instantiation(instance):
    assert isinstance(instance, uma_ProcessPlanningTemplate)

@given(instance=uma_DeliveryProcess_strategy)
@settings(max_examples=50)
def test_uma_deliveryprocess_instantiation(instance):
    assert isinstance(instance, uma_DeliveryProcess)

@given(instance=RoleDescriptor_strategy)
@settings(max_examples=50)
def test_roledescriptor_instantiation(instance):
    assert isinstance(instance, RoleDescriptor)

@given(instance=uma_CompositeRole_strategy)
@settings(max_examples=50)
def test_uma_compositerole_instantiation(instance):
    assert isinstance(instance, uma_CompositeRole)

@given(instance=Descriptor_strategy)
@settings(max_examples=50)
def test_descriptor_instantiation(instance):
    assert isinstance(instance, Descriptor)

@given(instance=uma_ProcessComponentDescriptor_strategy)
@settings(max_examples=50)
def test_uma_processcomponentdescriptor_instantiation(instance):
    assert isinstance(instance, uma_ProcessComponentDescriptor)

@given(instance=uma_WorkProductDescriptor_strategy)
@settings(max_examples=50)
def test_uma_workproductdescriptor_instantiation(instance):
    assert isinstance(instance, uma_WorkProductDescriptor)



@given(instance=uma_WorkProductDescriptor_strategy)
def test_uma_workproductdescriptor_activityExitState_setter(instance):
    original = instance.activityExitState
    instance.activityExitState = original
    assert instance.activityExitState == original



@given(instance=uma_WorkProductDescriptor_strategy)
def test_uma_workproductdescriptor_activityEntryState_setter(instance):
    original = instance.activityEntryState
    instance.activityEntryState = original
    assert instance.activityEntryState == original

@given(instance=uma_RoleDescriptor_strategy)
@settings(max_examples=50)
def test_uma_roledescriptor_instantiation(instance):
    assert isinstance(instance, uma_RoleDescriptor)

@given(instance=Activity_strategy)
@settings(max_examples=50)
def test_activity_instantiation(instance):
    assert isinstance(instance, Activity)

@given(instance=uma_Phase_strategy)
@settings(max_examples=50)
def test_uma_phase_instantiation(instance):
    assert isinstance(instance, uma_Phase)

@given(instance=uma_Process_strategy)
@settings(max_examples=50)
def test_uma_process_instantiation(instance):
    assert isinstance(instance, uma_Process)

@given(instance=uma_Iteration_strategy)
@settings(max_examples=50)
def test_uma_iteration_instantiation(instance):
    assert isinstance(instance, uma_Iteration)

@given(instance=MethodPackage_strategy)
@settings(max_examples=50)
def test_methodpackage_instantiation(instance):
    assert isinstance(instance, MethodPackage)

@given(instance=uma_ProcessPackage_strategy)
@settings(max_examples=50)
def test_uma_processpackage_instantiation(instance):
    assert isinstance(instance, uma_ProcessPackage)

@given(instance=uma_ContentPackage_strategy)
@settings(max_examples=50)
def test_uma_contentpackage_instantiation(instance):
    assert isinstance(instance, uma_ContentPackage)

@given(instance=Package_strategy)
@settings(max_examples=50)
def test_package_instantiation(instance):
    assert isinstance(instance, Package)

@given(instance=ProcessElement_strategy)
@settings(max_examples=50)
def test_processelement_instantiation(instance):
    assert isinstance(instance, ProcessElement)

@given(instance=uma_WorkOrder_strategy)
@settings(max_examples=50)
def test_uma_workorder_instantiation(instance):
    assert isinstance(instance, uma_WorkOrder)



@given(instance=uma_WorkOrder_strategy)
def test_uma_workorder_linkType_setter(instance):
    original = instance.linkType
    instance.linkType = original
    assert instance.linkType == original

@given(instance=BreakdownElement_strategy)
@settings(max_examples=50)
def test_breakdownelement_instantiation(instance):
    assert isinstance(instance, BreakdownElement)

@given(instance=uma_TeamProfile_strategy)
@settings(max_examples=50)
def test_uma_teamprofile_instantiation(instance):
    assert isinstance(instance, uma_TeamProfile)

@given(instance=uma_Descriptor_strategy)
@settings(max_examples=50)
def test_uma_descriptor_instantiation(instance):
    assert isinstance(instance, uma_Descriptor)



@given(instance=uma_Descriptor_strategy)
def test_uma_descriptor_isSynchronizedWithSource_setter(instance):
    original = instance.isSynchronizedWithSource
    instance.isSynchronizedWithSource = original
    assert instance.isSynchronizedWithSource == original

@given(instance=uma_ProcessComponentInterface_strategy)
@settings(max_examples=50)
def test_uma_processcomponentinterface_instantiation(instance):
    assert isinstance(instance, uma_ProcessComponentInterface)

@given(instance=uma_WorkBreakdownElement_strategy)
@settings(max_examples=50)
def test_uma_workbreakdownelement_instantiation(instance):
    assert isinstance(instance, uma_WorkBreakdownElement)



@given(instance=uma_WorkBreakdownElement_strategy)
def test_uma_workbreakdownelement_isRepeatable_setter(instance):
    original = instance.isRepeatable
    instance.isRepeatable = original
    assert instance.isRepeatable == original



@given(instance=uma_WorkBreakdownElement_strategy)
def test_uma_workbreakdownelement_isOngoing_setter(instance):
    original = instance.isOngoing
    instance.isOngoing = original
    assert instance.isOngoing == original



@given(instance=uma_WorkBreakdownElement_strategy)
def test_uma_workbreakdownelement_isEventDriven_setter(instance):
    original = instance.isEventDriven
    instance.isEventDriven = original
    assert instance.isEventDriven == original

@given(instance=uma_BreakdownElement_strategy)
@settings(max_examples=50)
def test_uma_breakdownelement_instantiation(instance):
    assert isinstance(instance, uma_BreakdownElement)



@given(instance=uma_BreakdownElement_strategy)
def test_uma_breakdownelement_hasMultipleOccurrences_setter(instance):
    original = instance.hasMultipleOccurrences
    instance.hasMultipleOccurrences = original
    assert instance.hasMultipleOccurrences == original



@given(instance=uma_BreakdownElement_strategy)
def test_uma_breakdownelement_isPlanned_setter(instance):
    original = instance.isPlanned
    instance.isPlanned = original
    assert instance.isPlanned == original



@given(instance=uma_BreakdownElement_strategy)
def test_uma_breakdownelement_prefix_setter(instance):
    original = instance.prefix
    instance.prefix = original
    assert instance.prefix == original



@given(instance=uma_BreakdownElement_strategy)
def test_uma_breakdownelement_isOptional_setter(instance):
    original = instance.isOptional
    instance.isOptional = original
    assert instance.isOptional == original

@given(instance=WorkBreakdownElement_strategy)
@settings(max_examples=50)
def test_workbreakdownelement_instantiation(instance):
    assert isinstance(instance, WorkBreakdownElement)

@given(instance=uma_Milestone_strategy)
@settings(max_examples=50)
def test_uma_milestone_instantiation(instance):
    assert isinstance(instance, uma_Milestone)

@given(instance=uma_TaskDescriptor_strategy)
@settings(max_examples=50)
def test_uma_taskdescriptor_instantiation(instance):
    assert isinstance(instance, uma_TaskDescriptor)

@given(instance=uma_PlanningData_strategy)
@settings(max_examples=50)
def test_uma_planningdata_instantiation(instance):
    assert isinstance(instance, uma_PlanningData)



@given(instance=uma_PlanningData_strategy)
def test_uma_planningdata_startDate_setter(instance):
    original = instance.startDate
    instance.startDate = original
    assert instance.startDate == original



@given(instance=uma_PlanningData_strategy)
def test_uma_planningdata_rank_setter(instance):
    original = instance.rank
    instance.rank = original
    assert instance.rank == original



@given(instance=uma_PlanningData_strategy)
def test_uma_planningdata_finishDate_setter(instance):
    original = instance.finishDate
    instance.finishDate = original
    assert instance.finishDate == original

@given(instance=ContentCategory_strategy)
@settings(max_examples=50)
def test_contentcategory_instantiation(instance):
    assert isinstance(instance, ContentCategory)

@given(instance=uma_RoleSetGrouping_strategy)
@settings(max_examples=50)
def test_uma_rolesetgrouping_instantiation(instance):
    assert isinstance(instance, uma_RoleSetGrouping)

@given(instance=uma_Tool_strategy)
@settings(max_examples=50)
def test_uma_tool_instantiation(instance):
    assert isinstance(instance, uma_Tool)

@given(instance=uma_CustomCategory_strategy)
@settings(max_examples=50)
def test_uma_customcategory_instantiation(instance):
    assert isinstance(instance, uma_CustomCategory)

@given(instance=uma_Domain_strategy)
@settings(max_examples=50)
def test_uma_domain_instantiation(instance):
    assert isinstance(instance, uma_Domain)

@given(instance=uma_DisciplineGrouping_strategy)
@settings(max_examples=50)
def test_uma_disciplinegrouping_instantiation(instance):
    assert isinstance(instance, uma_DisciplineGrouping)

@given(instance=uma_WorkProductType_strategy)
@settings(max_examples=50)
def test_uma_workproducttype_instantiation(instance):
    assert isinstance(instance, uma_WorkProductType)

@given(instance=uma_RoleSet_strategy)
@settings(max_examples=50)
def test_uma_roleset_instantiation(instance):
    assert isinstance(instance, uma_RoleSet)

@given(instance=uma_Discipline_strategy)
@settings(max_examples=50)
def test_uma_discipline_instantiation(instance):
    assert isinstance(instance, uma_Discipline)

@given(instance=ContentDescription_strategy)
@settings(max_examples=50)
def test_contentdescription_instantiation(instance):
    assert isinstance(instance, ContentDescription)

@given(instance=uma_TaskDescription_strategy)
@settings(max_examples=50)
def test_uma_taskdescription_instantiation(instance):
    assert isinstance(instance, uma_TaskDescription)



@given(instance=uma_TaskDescription_strategy)
def test_uma_taskdescription_alternatives_setter(instance):
    original = instance.alternatives
    instance.alternatives = original
    assert instance.alternatives == original



@given(instance=uma_TaskDescription_strategy)
def test_uma_taskdescription_purpose_setter(instance):
    original = instance.purpose
    instance.purpose = original
    assert instance.purpose == original

@given(instance=uma_RoleDescription_strategy)
@settings(max_examples=50)
def test_uma_roledescription_instantiation(instance):
    assert isinstance(instance, uma_RoleDescription)



@given(instance=uma_RoleDescription_strategy)
def test_uma_roledescription_synonyms_setter(instance):
    original = instance.synonyms
    instance.synonyms = original
    assert instance.synonyms == original



@given(instance=uma_RoleDescription_strategy)
def test_uma_roledescription_skills_setter(instance):
    original = instance.skills
    instance.skills = original
    assert instance.skills == original



@given(instance=uma_RoleDescription_strategy)
def test_uma_roledescription_assignmentApproaches_setter(instance):
    original = instance.assignmentApproaches
    instance.assignmentApproaches = original
    assert instance.assignmentApproaches == original

@given(instance=uma_BreakdownElementDescription_strategy)
@settings(max_examples=50)
def test_uma_breakdownelementdescription_instantiation(instance):
    assert isinstance(instance, uma_BreakdownElementDescription)



@given(instance=uma_BreakdownElementDescription_strategy)
def test_uma_breakdownelementdescription_usageGuidance_setter(instance):
    original = instance.usageGuidance
    instance.usageGuidance = original
    assert instance.usageGuidance == original

@given(instance=uma_WorkProductDescription_strategy)
@settings(max_examples=50)
def test_uma_workproductdescription_instantiation(instance):
    assert isinstance(instance, uma_WorkProductDescription)



@given(instance=uma_WorkProductDescription_strategy)
def test_uma_workproductdescription_impactOfNotHaving_setter(instance):
    original = instance.impactOfNotHaving
    instance.impactOfNotHaving = original
    assert instance.impactOfNotHaving == original



@given(instance=uma_WorkProductDescription_strategy)
def test_uma_workproductdescription_purpose_setter(instance):
    original = instance.purpose
    instance.purpose = original
    assert instance.purpose == original



@given(instance=uma_WorkProductDescription_strategy)
def test_uma_workproductdescription_reasonsForNotNeeding_setter(instance):
    original = instance.reasonsForNotNeeding
    instance.reasonsForNotNeeding = original
    assert instance.reasonsForNotNeeding == original

@given(instance=uma_PracticeDescription_strategy)
@settings(max_examples=50)
def test_uma_practicedescription_instantiation(instance):
    assert isinstance(instance, uma_PracticeDescription)



@given(instance=uma_PracticeDescription_strategy)
def test_uma_practicedescription_goals_setter(instance):
    original = instance.goals
    instance.goals = original
    assert instance.goals == original



@given(instance=uma_PracticeDescription_strategy)
def test_uma_practicedescription_background_setter(instance):
    original = instance.background
    instance.background = original
    assert instance.background == original



@given(instance=uma_PracticeDescription_strategy)
def test_uma_practicedescription_additionalInfo_setter(instance):
    original = instance.additionalInfo
    instance.additionalInfo = original
    assert instance.additionalInfo == original



@given(instance=uma_PracticeDescription_strategy)
def test_uma_practicedescription_levelsOfAdoption_setter(instance):
    original = instance.levelsOfAdoption
    instance.levelsOfAdoption = original
    assert instance.levelsOfAdoption == original



@given(instance=uma_PracticeDescription_strategy)
def test_uma_practicedescription_application_setter(instance):
    original = instance.application
    instance.application = original
    assert instance.application == original



@given(instance=uma_PracticeDescription_strategy)
def test_uma_practicedescription_problem_setter(instance):
    original = instance.problem
    instance.problem = original
    assert instance.problem == original

@given(instance=uma_GuidanceDescription_strategy)
@settings(max_examples=50)
def test_uma_guidancedescription_instantiation(instance):
    assert isinstance(instance, uma_GuidanceDescription)



@given(instance=uma_GuidanceDescription_strategy)
def test_uma_guidancedescription_attachments_setter(instance):
    original = instance.attachments
    instance.attachments = original
    assert instance.attachments == original

@given(instance=Concept_strategy)
@settings(max_examples=50)
def test_concept_instantiation(instance):
    assert isinstance(instance, Concept)

@given(instance=uma_Whitepaper_strategy)
@settings(max_examples=50)
def test_uma_whitepaper_instantiation(instance):
    assert isinstance(instance, uma_Whitepaper)

@given(instance=WorkDefinition_strategy)
@settings(max_examples=50)
def test_workdefinition_instantiation(instance):
    assert isinstance(instance, WorkDefinition)

@given(instance=Section_strategy)
@settings(max_examples=50)
def test_section_instantiation(instance):
    assert isinstance(instance, Section)

@given(instance=uma_Step_strategy)
@settings(max_examples=50)
def test_uma_step_instantiation(instance):
    assert isinstance(instance, uma_Step)

@given(instance=WorkProductDescription_strategy)
@settings(max_examples=50)
def test_workproductdescription_instantiation(instance):
    assert isinstance(instance, WorkProductDescription)

@given(instance=uma_DeliverableDescription_strategy)
@settings(max_examples=50)
def test_uma_deliverabledescription_instantiation(instance):
    assert isinstance(instance, uma_DeliverableDescription)



@given(instance=uma_DeliverableDescription_strategy)
def test_uma_deliverabledescription_externalDescription_setter(instance):
    original = instance.externalDescription
    instance.externalDescription = original
    assert instance.externalDescription == original



@given(instance=uma_DeliverableDescription_strategy)
def test_uma_deliverabledescription_packagingGuidance_setter(instance):
    original = instance.packagingGuidance
    instance.packagingGuidance = original
    assert instance.packagingGuidance == original

@given(instance=uma_ArtifactDescription_strategy)
@settings(max_examples=50)
def test_uma_artifactdescription_instantiation(instance):
    assert isinstance(instance, uma_ArtifactDescription)



@given(instance=uma_ArtifactDescription_strategy)
def test_uma_artifactdescription_notation_setter(instance):
    original = instance.notation
    instance.notation = original
    assert instance.notation == original



@given(instance=uma_ArtifactDescription_strategy)
def test_uma_artifactdescription_representationOptions_setter(instance):
    original = instance.representationOptions
    instance.representationOptions = original
    assert instance.representationOptions == original



@given(instance=uma_ArtifactDescription_strategy)
def test_uma_artifactdescription_briefOutline_setter(instance):
    original = instance.briefOutline
    instance.briefOutline = original
    assert instance.briefOutline == original



@given(instance=uma_ArtifactDescription_strategy)
def test_uma_artifactdescription_representation_setter(instance):
    original = instance.representation
    instance.representation = original
    assert instance.representation == original

@given(instance=FulfillableElement_strategy)
@settings(max_examples=50)
def test_fulfillableelement_instantiation(instance):
    assert isinstance(instance, FulfillableElement)

@given(instance=WorkProduct_strategy)
@settings(max_examples=50)
def test_workproduct_instantiation(instance):
    assert isinstance(instance, WorkProduct)

@given(instance=uma_Deliverable_strategy)
@settings(max_examples=50)
def test_uma_deliverable_instantiation(instance):
    assert isinstance(instance, uma_Deliverable)

@given(instance=uma_Outcome_strategy)
@settings(max_examples=50)
def test_uma_outcome_instantiation(instance):
    assert isinstance(instance, uma_Outcome)

@given(instance=uma_Artifact_strategy)
@settings(max_examples=50)
def test_uma_artifact_instantiation(instance):
    assert isinstance(instance, uma_Artifact)

@given(instance=MethodUnit_strategy)
@settings(max_examples=50)
def test_methodunit_instantiation(instance):
    assert isinstance(instance, MethodUnit)

@given(instance=uma_ProcessComponent_strategy)
@settings(max_examples=50)
def test_uma_processcomponent_instantiation(instance):
    assert isinstance(instance, uma_ProcessComponent)

@given(instance=uma_MethodLibrary_strategy)
@settings(max_examples=50)
def test_uma_methodlibrary_instantiation(instance):
    assert isinstance(instance, uma_MethodLibrary)

@given(instance=uma_MethodPlugin_strategy)
@settings(max_examples=50)
def test_uma_methodplugin_instantiation(instance):
    assert isinstance(instance, uma_MethodPlugin)



@given(instance=uma_MethodPlugin_strategy)
def test_uma_methodplugin_supporting_setter(instance):
    original = instance.supporting
    instance.supporting = original
    assert instance.supporting == original



@given(instance=uma_MethodPlugin_strategy)
def test_uma_methodplugin_userChangeable_setter(instance):
    original = instance.userChangeable
    instance.userChangeable = original
    assert instance.userChangeable == original

@given(instance=uma_MethodConfiguration_strategy)
@settings(max_examples=50)
def test_uma_methodconfiguration_instantiation(instance):
    assert isinstance(instance, uma_MethodConfiguration)

@given(instance=uma_ContentDescription_strategy)
@settings(max_examples=50)
def test_uma_contentdescription_instantiation(instance):
    assert isinstance(instance, uma_ContentDescription)



@given(instance=uma_ContentDescription_strategy)
def test_uma_contentdescription_mainDescription_setter(instance):
    original = instance.mainDescription
    instance.mainDescription = original
    assert instance.mainDescription == original



@given(instance=uma_ContentDescription_strategy)
def test_uma_contentdescription_keyConsiderations_setter(instance):
    original = instance.keyConsiderations
    instance.keyConsiderations = original
    assert instance.keyConsiderations == original



@given(instance=uma_ContentDescription_strategy)
def test_uma_contentdescription_externalId_setter(instance):
    original = instance.externalId
    instance.externalId = original
    assert instance.externalId == original



@given(instance=uma_ContentDescription_strategy)
def test_uma_contentdescription_longPresentationName_setter(instance):
    original = instance.longPresentationName
    instance.longPresentationName = original
    assert instance.longPresentationName == original

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=Guidance_strategy)
@settings(max_examples=50)
def test_guidance_instantiation(instance):
    assert isinstance(instance, Guidance)

@given(instance=uma_ReusableAsset_strategy)
@settings(max_examples=50)
def test_uma_reusableasset_instantiation(instance):
    assert isinstance(instance, uma_ReusableAsset)

@given(instance=uma_TermDefinition_strategy)
@settings(max_examples=50)
def test_uma_termdefinition_instantiation(instance):
    assert isinstance(instance, uma_TermDefinition)

@given(instance=uma_Report_strategy)
@settings(max_examples=50)
def test_uma_report_instantiation(instance):
    assert isinstance(instance, uma_Report)

@given(instance=uma_Practice_strategy)
@settings(max_examples=50)
def test_uma_practice_instantiation(instance):
    assert isinstance(instance, uma_Practice)

@given(instance=uma_Roadmap_strategy)
@settings(max_examples=50)
def test_uma_roadmap_instantiation(instance):
    assert isinstance(instance, uma_Roadmap)

@given(instance=uma_EstimationConsiderations_strategy)
@settings(max_examples=50)
def test_uma_estimationconsiderations_instantiation(instance):
    assert isinstance(instance, uma_EstimationConsiderations)

@given(instance=uma_ToolMentor_strategy)
@settings(max_examples=50)
def test_uma_toolmentor_instantiation(instance):
    assert isinstance(instance, uma_ToolMentor)

@given(instance=uma_Template_strategy)
@settings(max_examples=50)
def test_uma_template_instantiation(instance):
    assert isinstance(instance, uma_Template)

@given(instance=uma_Example_strategy)
@settings(max_examples=50)
def test_uma_example_instantiation(instance):
    assert isinstance(instance, uma_Example)

@given(instance=uma_Guideline_strategy)
@settings(max_examples=50)
def test_uma_guideline_instantiation(instance):
    assert isinstance(instance, uma_Guideline)

@given(instance=uma_Checklist_strategy)
@settings(max_examples=50)
def test_uma_checklist_instantiation(instance):
    assert isinstance(instance, uma_Checklist)

@given(instance=uma_Concept_strategy)
@settings(max_examples=50)
def test_uma_concept_instantiation(instance):
    assert isinstance(instance, uma_Concept)

@given(instance=uma_SupportingMaterial_strategy)
@settings(max_examples=50)
def test_uma_supportingmaterial_instantiation(instance):
    assert isinstance(instance, uma_SupportingMaterial)

@given(instance=VariabilityElement_strategy)
@settings(max_examples=50)
def test_variabilityelement_instantiation(instance):
    assert isinstance(instance, VariabilityElement)

@given(instance=uma_Activity_strategy)
@settings(max_examples=50)
def test_uma_activity_instantiation(instance):
    assert isinstance(instance, uma_Activity)

@given(instance=uma_Section_strategy)
@settings(max_examples=50)
def test_uma_section_instantiation(instance):
    assert isinstance(instance, uma_Section)



@given(instance=uma_Section_strategy)
def test_uma_section_sectionDescription_setter(instance):
    original = instance.sectionDescription
    instance.sectionDescription = original
    assert instance.sectionDescription == original



@given(instance=uma_Section_strategy)
def test_uma_section_sectionName_setter(instance):
    original = instance.sectionName
    instance.sectionName = original
    assert instance.sectionName == original

@given(instance=DescribableElement_strategy)
@settings(max_examples=50)
def test_describableelement_instantiation(instance):
    assert isinstance(instance, DescribableElement)

@given(instance=uma_FulfillableElement_strategy)
@settings(max_examples=50)
def test_uma_fulfillableelement_instantiation(instance):
    assert isinstance(instance, uma_FulfillableElement)

@given(instance=uma_ProcessElement_strategy)
@settings(max_examples=50)
def test_uma_processelement_instantiation(instance):
    assert isinstance(instance, uma_ProcessElement)

@given(instance=uma_ContentElement_strategy)
@settings(max_examples=50)
def test_uma_contentelement_instantiation(instance):
    assert isinstance(instance, uma_ContentElement)

@given(instance=uma_ApplicableMetaClassInfo_strategy)
@settings(max_examples=50)
def test_uma_applicablemetaclassinfo_instantiation(instance):
    assert isinstance(instance, uma_ApplicableMetaClassInfo)



@given(instance=uma_ApplicableMetaClassInfo_strategy)
def test_uma_applicablemetaclassinfo_isPrimaryExtension_setter(instance):
    original = instance.isPrimaryExtension
    instance.isPrimaryExtension = original
    assert instance.isPrimaryExtension == original

@given(instance=ContentElement_strategy)
@settings(max_examples=50)
def test_contentelement_instantiation(instance):
    assert isinstance(instance, ContentElement)

@given(instance=uma_Guidance_strategy)
@settings(max_examples=50)
def test_uma_guidance_instantiation(instance):
    assert isinstance(instance, uma_Guidance)

@given(instance=uma_Kind_strategy)
@settings(max_examples=50)
def test_uma_kind_instantiation(instance):
    assert isinstance(instance, uma_Kind)

@given(instance=uma_ContentCategory_strategy)
@settings(max_examples=50)
def test_uma_contentcategory_instantiation(instance):
    assert isinstance(instance, uma_ContentCategory)

@given(instance=uma_WorkProduct_strategy)
@settings(max_examples=50)
def test_uma_workproduct_instantiation(instance):
    assert isinstance(instance, uma_WorkProduct)

@given(instance=uma_Task_strategy)
@settings(max_examples=50)
def test_uma_task_instantiation(instance):
    assert isinstance(instance, uma_Task)

@given(instance=uma_Role_strategy)
@settings(max_examples=50)
def test_uma_role_instantiation(instance):
    assert isinstance(instance, uma_Role)

@given(instance=uma_Element_strategy)
@settings(max_examples=50)
def test_uma_element_instantiation(instance):
    assert isinstance(instance, uma_Element)

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=uma_NamedElement_strategy)
@settings(max_examples=50)
def test_uma_namedelement_instantiation(instance):
    assert isinstance(instance, uma_NamedElement)



@given(instance=uma_NamedElement_strategy)
def test_uma_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=uma_PackageableElement_strategy)
@settings(max_examples=50)
def test_uma_packageableelement_instantiation(instance):
    assert isinstance(instance, uma_PackageableElement)

@given(instance=PackageableElement_strategy)
@settings(max_examples=50)
def test_packageableelement_instantiation(instance):
    assert isinstance(instance, PackageableElement)

@given(instance=uma_MethodElementProperty_strategy)
@settings(max_examples=50)
def test_uma_methodelementproperty_instantiation(instance):
    assert isinstance(instance, uma_MethodElementProperty)



@given(instance=uma_MethodElementProperty_strategy)
def test_uma_methodelementproperty_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=uma_MethodElement_strategy)
@settings(max_examples=50)
def test_uma_methodelement_instantiation(instance):
    assert isinstance(instance, uma_MethodElement)



@given(instance=uma_MethodElement_strategy)
def test_uma_methodelement_presentationName_setter(instance):
    original = instance.presentationName
    instance.presentationName = original
    assert instance.presentationName == original



@given(instance=uma_MethodElement_strategy)
def test_uma_methodelement_suppressed_setter(instance):
    original = instance.suppressed
    instance.suppressed = original
    assert instance.suppressed == original



@given(instance=uma_MethodElement_strategy)
def test_uma_methodelement_briefDescription_setter(instance):
    original = instance.briefDescription
    instance.briefDescription = original
    assert instance.briefDescription == original



@given(instance=uma_MethodElement_strategy)
def test_uma_methodelement_orderingGuide_setter(instance):
    original = instance.orderingGuide
    instance.orderingGuide = original
    assert instance.orderingGuide == original



@given(instance=uma_MethodElement_strategy)
def test_uma_methodelement_guid_setter(instance):
    original = instance.guid
    instance.guid = original
    assert instance.guid == original

@given(instance=uma_Type_strategy)
@settings(max_examples=50)
def test_uma_type_instantiation(instance):
    assert isinstance(instance, uma_Type)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=uma_Classifier_strategy)
@settings(max_examples=50)
def test_uma_classifier_instantiation(instance):
    assert isinstance(instance, uma_Classifier)



@given(instance=uma_Classifier_strategy)
def test_uma_classifier_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=MethodElement_strategy)
@settings(max_examples=50)
def test_methodelement_instantiation(instance):
    assert isinstance(instance, MethodElement)

@given(instance=uma_DiagramElement_strategy)
@settings(max_examples=50)
def test_uma_diagramelement_instantiation(instance):
    assert isinstance(instance, uma_DiagramElement)



@given(instance=uma_DiagramElement_strategy)
def test_uma_diagramelement_isVisible_setter(instance):
    original = instance.isVisible
    instance.isVisible = original
    assert instance.isVisible == original

@given(instance=uma_WorkDefinition_strategy)
@settings(max_examples=50)
def test_uma_workdefinition_instantiation(instance):
    assert isinstance(instance, uma_WorkDefinition)

@given(instance=uma_MethodUnit_strategy)
@settings(max_examples=50)
def test_uma_methodunit_instantiation(instance):
    assert isinstance(instance, uma_MethodUnit)



@given(instance=uma_MethodUnit_strategy)
def test_uma_methodunit_changeDescription_setter(instance):
    original = instance.changeDescription
    instance.changeDescription = original
    assert instance.changeDescription == original



@given(instance=uma_MethodUnit_strategy)
def test_uma_methodunit_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original



@given(instance=uma_MethodUnit_strategy)
def test_uma_methodunit_authors_setter(instance):
    original = instance.authors
    instance.authors = original
    assert instance.authors == original



@given(instance=uma_MethodUnit_strategy)
def test_uma_methodunit_changeDate_setter(instance):
    original = instance.changeDate
    instance.changeDate = original
    assert instance.changeDate == original

@given(instance=uma_DescribableElement_strategy)
@settings(max_examples=50)
def test_uma_describableelement_instantiation(instance):
    assert isinstance(instance, uma_DescribableElement)



@given(instance=uma_DescribableElement_strategy)
def test_uma_describableelement_nodeicon_setter(instance):
    original = instance.nodeicon
    instance.nodeicon = original
    assert instance.nodeicon == original



@given(instance=uma_DescribableElement_strategy)
def test_uma_describableelement_shapeicon_setter(instance):
    original = instance.shapeicon
    instance.shapeicon = original
    assert instance.shapeicon == original

@given(instance=uma_VariabilityElement_strategy)
@settings(max_examples=50)
def test_uma_variabilityelement_instantiation(instance):
    assert isinstance(instance, uma_VariabilityElement)



@given(instance=uma_VariabilityElement_strategy)
def test_uma_variabilityelement_variabilityType_setter(instance):
    original = instance.variabilityType
    instance.variabilityType = original
    assert instance.variabilityType == original

@given(instance=uma_MethodPackage_strategy)
@settings(max_examples=50)
def test_uma_methodpackage_instantiation(instance):
    assert isinstance(instance, uma_MethodPackage)



@given(instance=uma_MethodPackage_strategy)
def test_uma_methodpackage_global__setter(instance):
    original = instance.global_
    instance.global_ = original
    assert instance.global_ == original

@given(instance=uma_Constraint_strategy)
@settings(max_examples=50)
def test_uma_constraint_instantiation(instance):
    assert isinstance(instance, uma_Constraint)



@given(instance=uma_Constraint_strategy)
def test_uma_constraint_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=uma_Namespace_strategy)
@settings(max_examples=50)
def test_uma_namespace_instantiation(instance):
    assert isinstance(instance, uma_Namespace)

@given(instance=Namespace_strategy)
@settings(max_examples=50)
def test_namespace_instantiation(instance):
    assert isinstance(instance, Namespace)

@given(instance=uma_Package_strategy)
@settings(max_examples=50)
def test_uma_package_instantiation(instance):
    assert isinstance(instance, uma_Package)
