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
PNType: Enumeration = Enumeration(
    name="PNType",
    literals={
            EnumerationLiteral(name="PTNET"),
			EnumerationLiteral(name="COREMODEL"),
			EnumerationLiteral(name="SYMNET"),
			EnumerationLiteral(name="HLPN"),
			EnumerationLiteral(name="GSPN")
    }
)

CSS2Color: Enumeration = Enumeration(
    name="CSS2Color",
    literals={
            EnumerationLiteral(name="AQUA"),
			EnumerationLiteral(name="BLACK"),
			EnumerationLiteral(name="BLUE"),
			EnumerationLiteral(name="FUCHSIA"),
			EnumerationLiteral(name="GRAY"),
			EnumerationLiteral(name="GREEN"),
			EnumerationLiteral(name="LIME"),
			EnumerationLiteral(name="MAROON"),
			EnumerationLiteral(name="NAVY"),
			EnumerationLiteral(name="OLIVE"),
			EnumerationLiteral(name="ORANGE"),
			EnumerationLiteral(name="PURPLE"),
			EnumerationLiteral(name="RED"),
			EnumerationLiteral(name="SILVER"),
			EnumerationLiteral(name="TEAL"),
			EnumerationLiteral(name="WHITE"),
			EnumerationLiteral(name="YELLOW")
    }
)

Gradient: Enumeration = Enumeration(
    name="Gradient",
    literals={
            EnumerationLiteral(name="HORIZONTAL"),
			EnumerationLiteral(name="VERTICAL"),
			EnumerationLiteral(name="DIAGONAL")
    }
)

LineShape: Enumeration = Enumeration(
    name="LineShape",
    literals={
            EnumerationLiteral(name="LINE"),
			EnumerationLiteral(name="CURVE")
    }
)

FontAlign: Enumeration = Enumeration(
    name="FontAlign",
    literals={
            EnumerationLiteral(name="LEFT"),
			EnumerationLiteral(name="CENTER"),
			EnumerationLiteral(name="RIGHT")
    }
)

FontDecoration: Enumeration = Enumeration(
    name="FontDecoration",
    literals={
            EnumerationLiteral(name="UNDERLINE"),
			EnumerationLiteral(name="OVERLINE"),
			EnumerationLiteral(name="LINETHROUGH")
    }
)

CSS2FontFamily: Enumeration = Enumeration(
    name="CSS2FontFamily",
    literals={
            EnumerationLiteral(name="VERDANA"),
			EnumerationLiteral(name="ARIAL"),
			EnumerationLiteral(name="TIMES"),
			EnumerationLiteral(name="GEORGIA"),
			EnumerationLiteral(name="TREBUCHET")
    }
)

CSS2FontSize: Enumeration = Enumeration(
    name="CSS2FontSize",
    literals={
            EnumerationLiteral(name="XXSMALL"),
			EnumerationLiteral(name="XSMALL"),
			EnumerationLiteral(name="SMALL"),
			EnumerationLiteral(name="LARGE"),
			EnumerationLiteral(name="XLARGE"),
			EnumerationLiteral(name="XXLARGE"),
			EnumerationLiteral(name="MEDIUM")
    }
)

CSS2FontStyle: Enumeration = Enumeration(
    name="CSS2FontStyle",
    literals={
            EnumerationLiteral(name="NORMAL"),
			EnumerationLiteral(name="ITALIC"),
			EnumerationLiteral(name="OBLIQUE")
    }
)

CSS2FontWeight: Enumeration = Enumeration(
    name="CSS2FontWeight",
    literals={
            EnumerationLiteral(name="NORMAL"),
			EnumerationLiteral(name="BOLD"),
			EnumerationLiteral(name="BOLDER"),
			EnumerationLiteral(name="LIGHTER")
    }
)

LineStyle: Enumeration = Enumeration(
    name="LineStyle",
    literals={
            EnumerationLiteral(name="SOLID"),
			EnumerationLiteral(name="DASH"),
			EnumerationLiteral(name="DOT")
    }
)

GSPNTransitionType: Enumeration = Enumeration(
    name="GSPNTransitionType",
    literals={
            EnumerationLiteral(name="immediate"),
			EnumerationLiteral(name="timed")
    }
)

GSPNArcType: Enumeration = Enumeration(
    name="GSPNArcType",
    literals={
            EnumerationLiteral(name="normal"),
			EnumerationLiteral(name="inhibitor")
    }
)

# Classes
ptnet_PTArcAnnotation = Class(name="ptnet::PTArcAnnotation")
ptnet_Arc = Class(name="ptnet::Arc")
ptnet_PetriNetDoc = Class(name="ptnet::PetriNetDoc")
ptnet_PetriNet = Class(name="ptnet::PetriNet")
ptnet_PTMarking = Class(name="ptnet::PTMarking")
Annotation = Class(name="Annotation")
ptnet_Place = Class(name="ptnet::Place")
ptnet_Page = Class(name="ptnet::Page")
ptnet_Name = Class(name="ptnet::Name")
ptnet_ToolInfo = Class(name="ptnet::ToolInfo")
PnObject = Class(name="PnObject")
ptnet_Label = Class(name="ptnet::Label", is_abstract=True)
ptnet_PnObject = Class(name="ptnet::PnObject", is_abstract=True)
ptnet_NodeGraphics = Class(name="ptnet::NodeGraphics")
ptnet_Graphics = Class(name="ptnet::Graphics", is_abstract=True)
ptnet_Coordinate = Class(name="ptnet::Coordinate", is_abstract=True)
ptnet_AnyObject = Class(name="ptnet::AnyObject", is_abstract=True)
Graphics = Class(name="Graphics")
ptnet_Position = Class(name="ptnet::Position")
ptnet_Dimension = Class(name="ptnet::Dimension")
ptnet_Fill = Class(name="ptnet::Fill")
ptnet_Line = Class(name="ptnet::Line")
ptnet_Node = Class(name="ptnet::Node", is_abstract=True)
Coordinate = Class(name="Coordinate")
ptnet_ArcGraphics = Class(name="ptnet::ArcGraphics")
ptnet_Offset = Class(name="ptnet::Offset")
ptnet_AnnotationGraphics = Class(name="ptnet::AnnotationGraphics")
ptnet_Font = Class(name="ptnet::Font")
ptnet_Annotation = Class(name="ptnet::Annotation", is_abstract=True)
ptnet_PlaceNode = Class(name="ptnet::PlaceNode", is_abstract=True)
Node = Class(name="Node")
ptnet_RefPlace = Class(name="ptnet::RefPlace")
ptnet_TransitionNode = Class(name="ptnet::TransitionNode", is_abstract=True)
ptnet_RefTransition = Class(name="ptnet::RefTransition")
PlaceNode = Class(name="PlaceNode")
TransitionNode = Class(name="TransitionNode")
ptnet_Transition = Class(name="ptnet::Transition")
ptnet_Attribute = Class(name="ptnet::Attribute", is_abstract=True)
Label = Class(name="Label")
ptnet_GSPNTransition = Class(name="ptnet::GSPNTransition")
Transition = Class(name="Transition")
ptnet_LogicalExpression = Class(name="ptnet::LogicalExpression", is_abstract=True)
ptnet_GSPNArc = Class(name="ptnet::GSPNArc")
Arc = Class(name="Arc")
ptnet_ArithmeticExpression = Class(name="ptnet::ArithmeticExpression", is_abstract=True)
ptnet_GSPNImmediateTransition = Class(name="ptnet::GSPNImmediateTransition")
GSPNTransition = Class(name="GSPNTransition")
ptnet_GSPNTimedTransition = Class(name="ptnet::GSPNTimedTransition")
ptnet_Distribution = Class(name="ptnet::Distribution", is_abstract=True)
ptnet_Deterministic = Class(name="ptnet::Deterministic")
Distribution = Class(name="Distribution")
ptnet_Exponential = Class(name="ptnet::Exponential")
ptnet_Gaussian = Class(name="ptnet::Gaussian")
ptnet_Uniform = Class(name="ptnet::Uniform")
ptnet_Gamma = Class(name="ptnet::Gamma")
ptnet_Weibull = Class(name="ptnet::Weibull")
ptnet_EvaluationList = Class(name="ptnet::EvaluationList")
ptnet_Study = Class(name="ptnet::Study")
ptnet_Measure = Class(name="ptnet::Measure")
ptnet_VariableValues = Class(name="ptnet::VariableValues")
ptnet_EvaluationType = Class(name="ptnet::EvaluationType", is_abstract=True)
ptnet_Expression = Class(name="ptnet::Expression", is_abstract=True)
ptnet_ValueExpression = Class(name="ptnet::ValueExpression")
ArithmeticExpression = Class(name="ArithmeticExpression")
ptnet_MarkingExpression = Class(name="ptnet::MarkingExpression")
Expression = Class(name="Expression")
ptnet_ArithmeticBinaryOperator = Class(name="ptnet::ArithmeticBinaryOperator", is_abstract=True)
ptnet_OpSum = Class(name="ptnet::OpSum")
ArithmeticBinaryOperator = Class(name="ArithmeticBinaryOperator")
ptnet_OpMinus = Class(name="ptnet::OpMinus")
ptnet_OpMultiply = Class(name="ptnet::OpMultiply")
ptnet_OpDivide = Class(name="ptnet::OpDivide")
ptnet_IfThenElse = Class(name="ptnet::IfThenElse")
ptnet_OpTrue = Class(name="ptnet::OpTrue")
LogicalExpression = Class(name="LogicalExpression")
ptnet_OpFalse = Class(name="ptnet::OpFalse")
ptnet_ComparisonOperator = Class(name="ptnet::ComparisonOperator", is_abstract=True)
ptnet_BooleanExpression = Class(name="ptnet::BooleanExpression")
ptnet_OpEqual = Class(name="ptnet::OpEqual")
ComparisonOperator = Class(name="ComparisonOperator")
ptnet_OpGreater = Class(name="ptnet::OpGreater")
ptnet_OpLess = Class(name="ptnet::OpLess")
ptnet_OpGreaterEqual = Class(name="ptnet::OpGreaterEqual")
ptnet_OpLessEqual = Class(name="ptnet::OpLessEqual")
ptnet_OpNot = Class(name="ptnet::OpNot")
ptnet_OpAnd = Class(name="ptnet::OpAnd")
BooleanExpression = Class(name="BooleanExpression")
ptnet_OpOr = Class(name="ptnet::OpOr")
ptnet_SteadyState = Class(name="ptnet::SteadyState")
EvaluationType = Class(name="EvaluationType")
ptnet_InstantOfTime = Class(name="ptnet::InstantOfTime")
ptnet_IntervalOfTime = Class(name="ptnet::IntervalOfTime")
ptnet_IntervalOfTimeAveraged = Class(name="ptnet::IntervalOfTimeAveraged")
ptnet_Variable = Class(name="ptnet::Variable")
ptnet_VariableExpression = Class(name="ptnet::VariableExpression")

# ptnet_PTArcAnnotation class attributes and methods
ptnet_PTArcAnnotation_text: Property = Property(name="text", type=StringType)
ptnet_PTArcAnnotation.attributes={ptnet_PTArcAnnotation_text}

# ptnet_Arc class attributes and methods

# ptnet_PetriNetDoc class attributes and methods
ptnet_PetriNetDoc_xmlns: Property = Property(name="xmlns", type=StringType)
ptnet_PetriNetDoc.attributes={ptnet_PetriNetDoc_xmlns}

# ptnet_PetriNet class attributes and methods
ptnet_PetriNet_id: Property = Property(name="id", type=StringType)
ptnet_PetriNet_type: Property = Property(name="type", type=StringType)
ptnet_PetriNet.attributes={ptnet_PetriNet_id, ptnet_PetriNet_type}

# ptnet_PTMarking class attributes and methods
ptnet_PTMarking_text: Property = Property(name="text", type=StringType)
ptnet_PTMarking.attributes={ptnet_PTMarking_text}

# Annotation class attributes and methods

# ptnet_Place class attributes and methods

# ptnet_Page class attributes and methods

# ptnet_Name class attributes and methods
ptnet_Name_text: Property = Property(name="text", type=StringType)
ptnet_Name.attributes={ptnet_Name_text}

# ptnet_ToolInfo class attributes and methods
ptnet_ToolInfo_tool: Property = Property(name="tool", type=StringType)
ptnet_ToolInfo_version: Property = Property(name="version", type=StringType)
ptnet_ToolInfo_formattedXMLBuffer: Property = Property(name="formattedXMLBuffer", type=StringType)
ptnet_ToolInfo_toolInfoGrammarURI: Property = Property(name="toolInfoGrammarURI", type=StringType)
ptnet_ToolInfo.attributes={ptnet_ToolInfo_toolInfoGrammarURI, ptnet_ToolInfo_version, ptnet_ToolInfo_formattedXMLBuffer, ptnet_ToolInfo_tool}

# PnObject class attributes and methods

# ptnet_Label class attributes and methods

# ptnet_PnObject class attributes and methods
ptnet_PnObject_id: Property = Property(name="id", type=StringType)
ptnet_PnObject.attributes={ptnet_PnObject_id}

# ptnet_NodeGraphics class attributes and methods

# ptnet_Graphics class attributes and methods

# ptnet_Coordinate class attributes and methods
ptnet_Coordinate_x: Property = Property(name="x", type=StringType)
ptnet_Coordinate_y: Property = Property(name="y", type=StringType)
ptnet_Coordinate.attributes={ptnet_Coordinate_x, ptnet_Coordinate_y}

# ptnet_AnyObject class attributes and methods

# Graphics class attributes and methods

# ptnet_Position class attributes and methods

# ptnet_Dimension class attributes and methods

# ptnet_Fill class attributes and methods
ptnet_Fill_color: Property = Property(name="color", type=StringType)
ptnet_Fill_gradientcolor: Property = Property(name="gradientcolor", type=StringType)
ptnet_Fill_gradientrotation: Property = Property(name="gradientrotation", type=StringType)
ptnet_Fill_image: Property = Property(name="image", type=StringType)
ptnet_Fill.attributes={ptnet_Fill_color, ptnet_Fill_image, ptnet_Fill_gradientrotation, ptnet_Fill_gradientcolor}

# ptnet_Line class attributes and methods
ptnet_Line_color: Property = Property(name="color", type=StringType)
ptnet_Line_shape: Property = Property(name="shape", type=StringType)
ptnet_Line_width: Property = Property(name="width", type=StringType)
ptnet_Line_style: Property = Property(name="style", type=StringType)
ptnet_Line.attributes={ptnet_Line_color, ptnet_Line_shape, ptnet_Line_style, ptnet_Line_width}

# ptnet_Node class attributes and methods

# Coordinate class attributes and methods

# ptnet_ArcGraphics class attributes and methods

# ptnet_Offset class attributes and methods

# ptnet_AnnotationGraphics class attributes and methods

# ptnet_Font class attributes and methods
ptnet_Font_align: Property = Property(name="align", type=StringType)
ptnet_Font_decoration: Property = Property(name="decoration", type=StringType)
ptnet_Font_family: Property = Property(name="family", type=StringType)
ptnet_Font_rotation: Property = Property(name="rotation", type=StringType)
ptnet_Font_size: Property = Property(name="size", type=StringType)
ptnet_Font_style: Property = Property(name="style", type=StringType)
ptnet_Font_weight: Property = Property(name="weight", type=StringType)
ptnet_Font.attributes={ptnet_Font_align, ptnet_Font_decoration, ptnet_Font_style, ptnet_Font_family, ptnet_Font_weight, ptnet_Font_rotation, ptnet_Font_size}

# ptnet_Annotation class attributes and methods

# ptnet_PlaceNode class attributes and methods

# Node class attributes and methods

# ptnet_RefPlace class attributes and methods

# ptnet_TransitionNode class attributes and methods

# ptnet_RefTransition class attributes and methods

# PlaceNode class attributes and methods

# TransitionNode class attributes and methods

# ptnet_Transition class attributes and methods

# ptnet_Attribute class attributes and methods

# Label class attributes and methods

# ptnet_GSPNTransition class attributes and methods

# Transition class attributes and methods

# ptnet_LogicalExpression class attributes and methods

# ptnet_GSPNArc class attributes and methods
ptnet_GSPNArc_type: Property = Property(name="type", type=StringType)
ptnet_GSPNArc.attributes={ptnet_GSPNArc_type}

# Arc class attributes and methods

# ptnet_ArithmeticExpression class attributes and methods

# ptnet_GSPNImmediateTransition class attributes and methods
ptnet_GSPNImmediateTransition_Priority: Property = Property(name="Priority", type=IntegerType)
ptnet_GSPNImmediateTransition_Weight: Property = Property(name="Weight", type=FloatType)
ptnet_GSPNImmediateTransition.attributes={ptnet_GSPNImmediateTransition_Weight, ptnet_GSPNImmediateTransition_Priority}

# GSPNTransition class attributes and methods

# ptnet_GSPNTimedTransition class attributes and methods

# ptnet_Distribution class attributes and methods

# ptnet_Deterministic class attributes and methods
ptnet_Deterministic_Value: Property = Property(name="Value", type=FloatType)
ptnet_Deterministic.attributes={ptnet_Deterministic_Value}

# Distribution class attributes and methods

# ptnet_Exponential class attributes and methods
ptnet_Exponential_Rate: Property = Property(name="Rate", type=FloatType)
ptnet_Exponential.attributes={ptnet_Exponential_Rate}

# ptnet_Gaussian class attributes and methods
ptnet_Gaussian_Variance: Property = Property(name="Variance", type=FloatType)
ptnet_Gaussian_Mean: Property = Property(name="Mean", type=FloatType)
ptnet_Gaussian.attributes={ptnet_Gaussian_Variance, ptnet_Gaussian_Mean}

# ptnet_Uniform class attributes and methods
ptnet_Uniform_Lower: Property = Property(name="Lower", type=FloatType)
ptnet_Uniform_Upper: Property = Property(name="Upper", type=FloatType)
ptnet_Uniform.attributes={ptnet_Uniform_Lower, ptnet_Uniform_Upper}

# ptnet_Gamma class attributes and methods
ptnet_Gamma_Alpha: Property = Property(name="Alpha", type=FloatType)
ptnet_Gamma_Beta: Property = Property(name="Beta", type=FloatType)
ptnet_Gamma.attributes={ptnet_Gamma_Beta, ptnet_Gamma_Alpha}

# ptnet_Weibull class attributes and methods
ptnet_Weibull_Alpha: Property = Property(name="Alpha", type=FloatType)
ptnet_Weibull_Beta: Property = Property(name="Beta", type=FloatType)
ptnet_Weibull.attributes={ptnet_Weibull_Beta, ptnet_Weibull_Alpha}

# ptnet_EvaluationList class attributes and methods

# ptnet_Study class attributes and methods
ptnet_Study_name: Property = Property(name="name", type=StringType)
ptnet_Study.attributes={ptnet_Study_name}

# ptnet_Measure class attributes and methods
ptnet_Measure_name: Property = Property(name="name", type=StringType)
ptnet_Measure.attributes={ptnet_Measure_name}

# ptnet_VariableValues class attributes and methods
ptnet_VariableValues_values: Property = Property(name="values", type=FloatType)
ptnet_VariableValues.attributes={ptnet_VariableValues_values}

# ptnet_EvaluationType class attributes and methods

# ptnet_Expression class attributes and methods

# ptnet_ValueExpression class attributes and methods
ptnet_ValueExpression_value: Property = Property(name="value", type=FloatType)
ptnet_ValueExpression.attributes={ptnet_ValueExpression_value}

# ArithmeticExpression class attributes and methods

# ptnet_MarkingExpression class attributes and methods

# Expression class attributes and methods

# ptnet_ArithmeticBinaryOperator class attributes and methods

# ptnet_OpSum class attributes and methods

# ArithmeticBinaryOperator class attributes and methods

# ptnet_OpMinus class attributes and methods

# ptnet_OpMultiply class attributes and methods

# ptnet_OpDivide class attributes and methods

# ptnet_IfThenElse class attributes and methods

# ptnet_OpTrue class attributes and methods

# LogicalExpression class attributes and methods

# ptnet_OpFalse class attributes and methods

# ptnet_ComparisonOperator class attributes and methods

# ptnet_BooleanExpression class attributes and methods

# ptnet_OpEqual class attributes and methods

# ComparisonOperator class attributes and methods

# ptnet_OpGreater class attributes and methods

# ptnet_OpLess class attributes and methods

# ptnet_OpGreaterEqual class attributes and methods

# ptnet_OpLessEqual class attributes and methods

# ptnet_OpNot class attributes and methods

# ptnet_OpAnd class attributes and methods

# BooleanExpression class attributes and methods

# ptnet_OpOr class attributes and methods

# ptnet_SteadyState class attributes and methods

# EvaluationType class attributes and methods

# ptnet_InstantOfTime class attributes and methods

# ptnet_IntervalOfTime class attributes and methods

# ptnet_IntervalOfTimeAveraged class attributes and methods

# ptnet_Variable class attributes and methods
ptnet_Variable_name: Property = Property(name="name", type=StringType)
ptnet_Variable.attributes={ptnet_Variable_name}

# ptnet_VariableExpression class attributes and methods

# Relationships
containerPlace0: BinaryAssociation = BinaryAssociation(
    name="containerPlace0",
    ends={
        Property(name="initialMarking", type=ptnet_Place, multiplicity=Multiplicity(0, 1)),
        Property(name="Place", type=ptnet_PTMarking, multiplicity=Multiplicity(1, 1))
    }
)
containerArc1: BinaryAssociation = BinaryAssociation(
    name="containerArc1",
    ends={
        Property(name="Arc", type=ptnet_PTArcAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="inscription", type=ptnet_Arc, multiplicity=Multiplicity(0, 1))
    }
)
nets2: BinaryAssociation = BinaryAssociation(
    name="nets2",
    ends={
        Property(name="PetriNet", type=ptnet_PetriNetDoc, multiplicity=Multiplicity(1, 1)),
        Property(name="containerPetriNetDoc", type=ptnet_PetriNet, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
pages3: BinaryAssociation = BinaryAssociation(
    name="pages3",
    ends={
        Property(name="Page", type=ptnet_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="containerPetriNet", type=ptnet_Page, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
name4: BinaryAssociation = BinaryAssociation(
    name="name4",
    ends={
        Property(name="Name", type=ptnet_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="containerNamePetriNet", type=ptnet_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
toolspecifics5: BinaryAssociation = BinaryAssociation(
    name="toolspecifics5",
    ends={
        Property(name="ToolInfo", type=ptnet_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="containerPetriNet6", type=ptnet_ToolInfo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
containerPetriNetDoc7: BinaryAssociation = BinaryAssociation(
    name="containerPetriNetDoc7",
    ends={
        Property(name="PetriNetDoc", type=ptnet_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="nets", type=ptnet_PetriNetDoc, multiplicity=Multiplicity(0, 1))
    }
)
containerNamePetriNet19: BinaryAssociation = BinaryAssociation(
    name="containerNamePetriNet19",
    ends={
        Property(name="PetriNet20", type=ptnet_Name, multiplicity=Multiplicity(1, 1)),
        Property(name="name", type=ptnet_PetriNet, multiplicity=Multiplicity(0, 1))
    }
)
containerNamePnObject21: BinaryAssociation = BinaryAssociation(
    name="containerNamePnObject21",
    ends={
        Property(name="PnObject23", type=ptnet_Name, multiplicity=Multiplicity(1, 1)),
        Property(name="name22", type=ptnet_PnObject, multiplicity=Multiplicity(0, 1))
    }
)
containerPetriNet24: BinaryAssociation = BinaryAssociation(
    name="containerPetriNet24",
    ends={
        Property(name="PetriNet25", type=ptnet_ToolInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="toolspecifics", type=ptnet_PetriNet, multiplicity=Multiplicity(0, 1))
    }
)
containerPnObject26: BinaryAssociation = BinaryAssociation(
    name="containerPnObject26",
    ends={
        Property(name="PnObject28", type=ptnet_ToolInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="toolspecifics27", type=ptnet_PnObject, multiplicity=Multiplicity(0, 1))
    }
)
objects8: BinaryAssociation = BinaryAssociation(
    name="objects8",
    ends={
        Property(name="PnObject", type=ptnet_Page, multiplicity=Multiplicity(1, 1)),
        Property(name="containerPage", type=ptnet_PnObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
containerPetriNet9: BinaryAssociation = BinaryAssociation(
    name="containerPetriNet9",
    ends={
        Property(name="PetriNet10", type=ptnet_Page, multiplicity=Multiplicity(1, 1)),
        Property(name="pages", type=ptnet_PetriNet, multiplicity=Multiplicity(0, 1))
    }
)
nodegraphics11: BinaryAssociation = BinaryAssociation(
    name="nodegraphics11",
    ends={
        Property(name="NodeGraphics", type=ptnet_Page, multiplicity=Multiplicity(1, 1)),
        Property(name="containerPage12", type=ptnet_NodeGraphics, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name13: BinaryAssociation = BinaryAssociation(
    name="name13",
    ends={
        Property(name="Name14", type=ptnet_PnObject, multiplicity=Multiplicity(1, 1)),
        Property(name="containerNamePnObject", type=ptnet_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
toolspecifics15: BinaryAssociation = BinaryAssociation(
    name="toolspecifics15",
    ends={
        Property(name="ToolInfo16", type=ptnet_PnObject, multiplicity=Multiplicity(1, 1)),
        Property(name="containerPnObject", type=ptnet_ToolInfo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
containerPage17: BinaryAssociation = BinaryAssociation(
    name="containerPage17",
    ends={
        Property(name="Page18", type=ptnet_PnObject, multiplicity=Multiplicity(1, 1)),
        Property(name="objects", type=ptnet_Page, multiplicity=Multiplicity(0, 1))
    }
)
containerNode39: BinaryAssociation = BinaryAssociation(
    name="containerNode39",
    ends={
        Property(name="nodegraphics", type=ptnet_Node, multiplicity=Multiplicity(0, 1)),
        Property(name="Node", type=ptnet_NodeGraphics, multiplicity=Multiplicity(1, 1))
    }
)
containerPage40: BinaryAssociation = BinaryAssociation(
    name="containerPage40",
    ends={
        Property(name="Page42", type=ptnet_NodeGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="nodegraphics41", type=ptnet_Page, multiplicity=Multiplicity(0, 1))
    }
)
containerLabel29: BinaryAssociation = BinaryAssociation(
    name="containerLabel29",
    ends={
        Property(name="Label", type=ptnet_ToolInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="toolspecifics30", type=ptnet_Label, multiplicity=Multiplicity(0, 1))
    }
)
toolInfoModel31: BinaryAssociation = BinaryAssociation(
    name="toolInfoModel31",
    ends={
        Property(name="AnyObject", type=ptnet_ToolInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="containerToolInfo", type=ptnet_AnyObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
toolspecifics32: BinaryAssociation = BinaryAssociation(
    name="toolspecifics32",
    ends={
        Property(name="ToolInfo33", type=ptnet_Label, multiplicity=Multiplicity(1, 1)),
        Property(name="containerLabel", type=ptnet_ToolInfo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
position34: BinaryAssociation = BinaryAssociation(
    name="position34",
    ends={
        Property(name="Position", type=ptnet_NodeGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="containerPNodeGraphics", type=ptnet_Position, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dimension35: BinaryAssociation = BinaryAssociation(
    name="dimension35",
    ends={
        Property(name="Dimension", type=ptnet_NodeGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="containerDNodeGraphics", type=ptnet_Dimension, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fill36: BinaryAssociation = BinaryAssociation(
    name="fill36",
    ends={
        Property(name="Fill", type=ptnet_NodeGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="containerNodeGraphics", type=ptnet_Fill, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
line37: BinaryAssociation = BinaryAssociation(
    name="line37",
    ends={
        Property(name="Line", type=ptnet_NodeGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="containerNodeGraphics38", type=ptnet_Line, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
containerArcGraphics43: BinaryAssociation = BinaryAssociation(
    name="containerArcGraphics43",
    ends={
        Property(name="ArcGraphics", type=ptnet_Position, multiplicity=Multiplicity(1, 1)),
        Property(name="positions", type=ptnet_ArcGraphics, multiplicity=Multiplicity(0, 1))
    }
)
containerPNodeGraphics44: BinaryAssociation = BinaryAssociation(
    name="containerPNodeGraphics44",
    ends={
        Property(name="NodeGraphics45", type=ptnet_Position, multiplicity=Multiplicity(1, 1)),
        Property(name="position", type=ptnet_NodeGraphics, multiplicity=Multiplicity(0, 1))
    }
)
containerAnnotationGraphics46: BinaryAssociation = BinaryAssociation(
    name="containerAnnotationGraphics46",
    ends={
        Property(name="AnnotationGraphics", type=ptnet_Offset, multiplicity=Multiplicity(1, 1)),
        Property(name="offset", type=ptnet_AnnotationGraphics, multiplicity=Multiplicity(0, 1))
    }
)
containerDNodeGraphics47: BinaryAssociation = BinaryAssociation(
    name="containerDNodeGraphics47",
    ends={
        Property(name="NodeGraphics48", type=ptnet_Dimension, multiplicity=Multiplicity(1, 1)),
        Property(name="dimension", type=ptnet_NodeGraphics, multiplicity=Multiplicity(0, 1))
    }
)
offset49: BinaryAssociation = BinaryAssociation(
    name="offset49",
    ends={
        Property(name="Offset", type=ptnet_AnnotationGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="containerAnnotationGraphics", type=ptnet_Offset, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fill50: BinaryAssociation = BinaryAssociation(
    name="fill50",
    ends={
        Property(name="Fill52", type=ptnet_AnnotationGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="containerAnnotationGraphics51", type=ptnet_Fill, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
line53: BinaryAssociation = BinaryAssociation(
    name="line53",
    ends={
        Property(name="Line55", type=ptnet_AnnotationGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="containerAnnotationGraphics54", type=ptnet_Line, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
font56: BinaryAssociation = BinaryAssociation(
    name="font56",
    ends={
        Property(name="Font", type=ptnet_AnnotationGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="containerAnnotationGraphics57", type=ptnet_Font, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
containerAnnotation58: BinaryAssociation = BinaryAssociation(
    name="containerAnnotation58",
    ends={
        Property(name="Annotation", type=ptnet_AnnotationGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="annotationgraphics", type=ptnet_Annotation, multiplicity=Multiplicity(0, 1))
    }
)
containerNodeGraphics59: BinaryAssociation = BinaryAssociation(
    name="containerNodeGraphics59",
    ends={
        Property(name="NodeGraphics60", type=ptnet_Fill, multiplicity=Multiplicity(1, 1)),
        Property(name="fill", type=ptnet_NodeGraphics, multiplicity=Multiplicity(0, 1))
    }
)
containerAnnotationGraphics61: BinaryAssociation = BinaryAssociation(
    name="containerAnnotationGraphics61",
    ends={
        Property(name="AnnotationGraphics63", type=ptnet_Fill, multiplicity=Multiplicity(1, 1)),
        Property(name="fill62", type=ptnet_AnnotationGraphics, multiplicity=Multiplicity(0, 1))
    }
)
containerNodeGraphics64: BinaryAssociation = BinaryAssociation(
    name="containerNodeGraphics64",
    ends={
        Property(name="NodeGraphics65", type=ptnet_Line, multiplicity=Multiplicity(1, 1)),
        Property(name="line", type=ptnet_NodeGraphics, multiplicity=Multiplicity(0, 1))
    }
)
containerArcGraphics66: BinaryAssociation = BinaryAssociation(
    name="containerArcGraphics66",
    ends={
        Property(name="ArcGraphics68", type=ptnet_Line, multiplicity=Multiplicity(1, 1)),
        Property(name="line67", type=ptnet_ArcGraphics, multiplicity=Multiplicity(0, 1))
    }
)
containerAnnotationGraphics69: BinaryAssociation = BinaryAssociation(
    name="containerAnnotationGraphics69",
    ends={
        Property(name="AnnotationGraphics71", type=ptnet_Line, multiplicity=Multiplicity(1, 1)),
        Property(name="line70", type=ptnet_AnnotationGraphics, multiplicity=Multiplicity(0, 1))
    }
)
positions72: BinaryAssociation = BinaryAssociation(
    name="positions72",
    ends={
        Property(name="Position73", type=ptnet_ArcGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="containerArcGraphics", type=ptnet_Position, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
line74: BinaryAssociation = BinaryAssociation(
    name="line74",
    ends={
        Property(name="Line76", type=ptnet_ArcGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="containerArcGraphics75", type=ptnet_Line, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
containerArc77: BinaryAssociation = BinaryAssociation(
    name="containerArc77",
    ends={
        Property(name="Arc78", type=ptnet_ArcGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="arcgraphics", type=ptnet_Arc, multiplicity=Multiplicity(0, 1))
    }
)
source79: BinaryAssociation = BinaryAssociation(
    name="source79",
    ends={
        Property(name="Node80", type=ptnet_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="OutArcs", type=ptnet_Node, multiplicity=Multiplicity(1, 1))
    }
)
target81: BinaryAssociation = BinaryAssociation(
    name="target81",
    ends={
        Property(name="Node82", type=ptnet_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="InArcs", type=ptnet_Node, multiplicity=Multiplicity(1, 1))
    }
)
arcgraphics83: BinaryAssociation = BinaryAssociation(
    name="arcgraphics83",
    ends={
        Property(name="ArcGraphics84", type=ptnet_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="containerArc", type=ptnet_ArcGraphics, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
inscription85: BinaryAssociation = BinaryAssociation(
    name="inscription85",
    ends={
        Property(name="PTArcAnnotation", type=ptnet_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="containerArc86", type=ptnet_PTArcAnnotation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
InArcs87: BinaryAssociation = BinaryAssociation(
    name="InArcs87",
    ends={
        Property(name="Arc88", type=ptnet_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=ptnet_Arc, multiplicity=Multiplicity(0, 9999))
    }
)
OutArcs89: BinaryAssociation = BinaryAssociation(
    name="OutArcs89",
    ends={
        Property(name="Arc90", type=ptnet_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=ptnet_Arc, multiplicity=Multiplicity(0, 9999))
    }
)
nodegraphics91: BinaryAssociation = BinaryAssociation(
    name="nodegraphics91",
    ends={
        Property(name="NodeGraphics92", type=ptnet_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="containerNode", type=ptnet_NodeGraphics, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
containerAnnotationGraphics93: BinaryAssociation = BinaryAssociation(
    name="containerAnnotationGraphics93",
    ends={
        Property(name="AnnotationGraphics94", type=ptnet_Font, multiplicity=Multiplicity(1, 1)),
        Property(name="font", type=ptnet_AnnotationGraphics, multiplicity=Multiplicity(0, 1))
    }
)
referencingPlaces95: BinaryAssociation = BinaryAssociation(
    name="referencingPlaces95",
    ends={
        Property(name="RefPlace", type=ptnet_PlaceNode, multiplicity=Multiplicity(1, 1)),
        Property(name="ref", type=ptnet_RefPlace, multiplicity=Multiplicity(0, 9999))
    }
)
referencingTransitions96: BinaryAssociation = BinaryAssociation(
    name="referencingTransitions96",
    ends={
        Property(name="RefTransition", type=ptnet_TransitionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="ref97", type=ptnet_RefTransition, multiplicity=Multiplicity(0, 9999))
    }
)
initialMarking98: BinaryAssociation = BinaryAssociation(
    name="initialMarking98",
    ends={
        Property(name="PTMarking", type=ptnet_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="containerPlace", type=ptnet_PTMarking, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ref99: BinaryAssociation = BinaryAssociation(
    name="ref99",
    ends={
        Property(name="TransitionNode", type=ptnet_RefTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="referencingTransitions", type=ptnet_TransitionNode, multiplicity=Multiplicity(1, 1))
    }
)
ref100: BinaryAssociation = BinaryAssociation(
    name="ref100",
    ends={
        Property(name="PlaceNode", type=ptnet_RefPlace, multiplicity=Multiplicity(1, 1)),
        Property(name="referencingPlaces", type=ptnet_PlaceNode, multiplicity=Multiplicity(1, 1))
    }
)
annotationgraphics101: BinaryAssociation = BinaryAssociation(
    name="annotationgraphics101",
    ends={
        Property(name="AnnotationGraphics102", type=ptnet_Annotation, multiplicity=Multiplicity(1, 1)),
        Property(name="containerAnnotation", type=ptnet_AnnotationGraphics, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
containerToolInfo103: BinaryAssociation = BinaryAssociation(
    name="containerToolInfo103",
    ends={
        Property(name="ToolInfo104", type=ptnet_AnyObject, multiplicity=Multiplicity(1, 1)),
        Property(name="toolInfoModel", type=ptnet_ToolInfo, multiplicity=Multiplicity(0, 1))
    }
)
Guard105: BinaryAssociation = BinaryAssociation(
    name="Guard105",
    ends={
        Property(name="ptnet_LogicalExpression", type=ptnet_GSPNTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="ptnet_GSPNTransition", type=ptnet_LogicalExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
MultiplicityFunction106: BinaryAssociation = BinaryAssociation(
    name="MultiplicityFunction106",
    ends={
        Property(name="ptnet_ArithmeticExpression", type=ptnet_GSPNArc, multiplicity=Multiplicity(1, 1)),
        Property(name="ptnet_GSPNArc", type=ptnet_ArithmeticExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Distribution107: BinaryAssociation = BinaryAssociation(
    name="Distribution107",
    ends={
        Property(name="ptnet_Distribution", type=ptnet_GSPNTimedTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="ptnet_GSPNTimedTransition", type=ptnet_Distribution, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
studies108: BinaryAssociation = BinaryAssociation(
    name="studies108",
    ends={
        Property(name="ptnet_Study", type=ptnet_EvaluationList, multiplicity=Multiplicity(1, 1)),
        Property(name="ptnet_EvaluationList", type=ptnet_Study, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
measures109: BinaryAssociation = BinaryAssociation(
    name="measures109",
    ends={
        Property(name="ptnet_Measure", type=ptnet_EvaluationList, multiplicity=Multiplicity(1, 1)),
        Property(name="ptnet_EvaluationList110", type=ptnet_Measure, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
vars111: BinaryAssociation = BinaryAssociation(
    name="vars111",
    ends={
        Property(name="ptnet_VariableValues", type=ptnet_Study, multiplicity=Multiplicity(1, 1)),
        Property(name="ptnet_Study112", type=ptnet_VariableValues, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rewardFunction113: BinaryAssociation = BinaryAssociation(
    name="rewardFunction113",
    ends={
        Property(name="ptnet_ArithmeticExpression115", type=ptnet_Measure, multiplicity=Multiplicity(1, 1)),
        Property(name="ptnet_Measure114", type=ptnet_ArithmeticExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
evaluationType116: BinaryAssociation = BinaryAssociation(
    name="evaluationType116",
    ends={
        Property(name="ptnet_EvaluationType", type=ptnet_Measure, multiplicity=Multiplicity(1, 1)),
        Property(name="ptnet_Measure117", type=ptnet_EvaluationType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
place118: BinaryAssociation = BinaryAssociation(
    name="place118",
    ends={
        Property(name="ptnet_PlaceNode", type=ptnet_MarkingExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ptnet_MarkingExpression", type=ptnet_PlaceNode, multiplicity=Multiplicity(0, 1))
    }
)
expression1119: BinaryAssociation = BinaryAssociation(
    name="expression1119",
    ends={
        Property(name="ptnet_ArithmeticExpression120", type=ptnet_ArithmeticBinaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="ptnet_ArithmeticBinaryOperator", type=ptnet_ArithmeticExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression2121: BinaryAssociation = BinaryAssociation(
    name="expression2121",
    ends={
        Property(name="ptnet_ArithmeticExpression123", type=ptnet_ArithmeticBinaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="ptnet_ArithmeticBinaryOperator122", type=ptnet_ArithmeticExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition124: BinaryAssociation = BinaryAssociation(
    name="condition124",
    ends={
        Property(name="ptnet_LogicalExpression125", type=ptnet_IfThenElse, multiplicity=Multiplicity(1, 1)),
        Property(name="ptnet_IfThenElse", type=ptnet_LogicalExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ifTrue126: BinaryAssociation = BinaryAssociation(
    name="ifTrue126",
    ends={
        Property(name="ptnet_ArithmeticExpression128", type=ptnet_IfThenElse, multiplicity=Multiplicity(1, 1)),
        Property(name="ptnet_IfThenElse127", type=ptnet_ArithmeticExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ifFalse129: BinaryAssociation = BinaryAssociation(
    name="ifFalse129",
    ends={
        Property(name="ptnet_ArithmeticExpression131", type=ptnet_IfThenElse, multiplicity=Multiplicity(1, 1)),
        Property(name="ptnet_IfThenElse130", type=ptnet_ArithmeticExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression1132: BinaryAssociation = BinaryAssociation(
    name="expression1132",
    ends={
        Property(name="ptnet_ArithmeticExpression133", type=ptnet_ComparisonOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="ptnet_ComparisonOperator", type=ptnet_ArithmeticExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression2134: BinaryAssociation = BinaryAssociation(
    name="expression2134",
    ends={
        Property(name="ptnet_ArithmeticExpression136", type=ptnet_ComparisonOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="ptnet_ComparisonOperator135", type=ptnet_ArithmeticExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression1137: BinaryAssociation = BinaryAssociation(
    name="expression1137",
    ends={
        Property(name="ptnet_LogicalExpression138", type=ptnet_BooleanExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ptnet_BooleanExpression", type=ptnet_LogicalExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression2139: BinaryAssociation = BinaryAssociation(
    name="expression2139",
    ends={
        Property(name="ptnet_LogicalExpression141", type=ptnet_BooleanExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ptnet_BooleanExpression140", type=ptnet_LogicalExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression142: BinaryAssociation = BinaryAssociation(
    name="expression142",
    ends={
        Property(name="ptnet_LogicalExpression143", type=ptnet_OpNot, multiplicity=Multiplicity(1, 1)),
        Property(name="ptnet_OpNot", type=ptnet_LogicalExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
intervalBegin146: BinaryAssociation = BinaryAssociation(
    name="intervalBegin146",
    ends={
        Property(name="ptnet_ArithmeticExpression147", type=ptnet_IntervalOfTime, multiplicity=Multiplicity(1, 1)),
        Property(name="ptnet_IntervalOfTime", type=ptnet_ArithmeticExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
intervalEnd148: BinaryAssociation = BinaryAssociation(
    name="intervalEnd148",
    ends={
        Property(name="ptnet_ArithmeticExpression150", type=ptnet_IntervalOfTime, multiplicity=Multiplicity(1, 1)),
        Property(name="ptnet_IntervalOfTime149", type=ptnet_ArithmeticExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
intervalBegin151: BinaryAssociation = BinaryAssociation(
    name="intervalBegin151",
    ends={
        Property(name="ptnet_ArithmeticExpression152", type=ptnet_IntervalOfTimeAveraged, multiplicity=Multiplicity(1, 1)),
        Property(name="ptnet_IntervalOfTimeAveraged", type=ptnet_ArithmeticExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
intervalEnd153: BinaryAssociation = BinaryAssociation(
    name="intervalEnd153",
    ends={
        Property(name="ptnet_ArithmeticExpression155", type=ptnet_IntervalOfTimeAveraged, multiplicity=Multiplicity(1, 1)),
        Property(name="ptnet_IntervalOfTimeAveraged154", type=ptnet_ArithmeticExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
instant144: BinaryAssociation = BinaryAssociation(
    name="instant144",
    ends={
        Property(name="ptnet_ArithmeticExpression145", type=ptnet_InstantOfTime, multiplicity=Multiplicity(1, 1)),
        Property(name="ptnet_InstantOfTime", type=ptnet_ArithmeticExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable158: BinaryAssociation = BinaryAssociation(
    name="variable158",
    ends={
        Property(name="ptnet_Variable159", type=ptnet_VariableExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ptnet_VariableExpression", type=ptnet_Variable, multiplicity=Multiplicity(1, 1))
    }
)
variable156: BinaryAssociation = BinaryAssociation(
    name="variable156",
    ends={
        Property(name="ptnet_Variable", type=ptnet_VariableValues, multiplicity=Multiplicity(1, 1)),
        Property(name="ptnet_VariableValues157", type=ptnet_Variable, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_ptnet_PTArcAnnotation_Annotation = Generalization(general=Annotation, specific=ptnet_PTArcAnnotation)
gen_ptnet_PTMarking_Annotation = Generalization(general=Annotation, specific=ptnet_PTMarking)
gen_ptnet_Page_PnObject = Generalization(general=PnObject, specific=ptnet_Page)
gen_ptnet_Name_Annotation = Generalization(general=Annotation, specific=ptnet_Name)
gen_ptnet_NodeGraphics_Graphics = Generalization(general=Graphics, specific=ptnet_NodeGraphics)
gen_ptnet_Offset_Coordinate = Generalization(general=Coordinate, specific=ptnet_Offset)
gen_ptnet_Position_Coordinate = Generalization(general=Coordinate, specific=ptnet_Position)
gen_ptnet_Dimension_Coordinate = Generalization(general=Coordinate, specific=ptnet_Dimension)
gen_ptnet_AnnotationGraphics_Graphics = Generalization(general=Graphics, specific=ptnet_AnnotationGraphics)
gen_ptnet_ArcGraphics_Graphics = Generalization(general=Graphics, specific=ptnet_ArcGraphics)
gen_ptnet_Arc_PnObject = Generalization(general=PnObject, specific=ptnet_Arc)
gen_ptnet_Node_PnObject = Generalization(general=PnObject, specific=ptnet_Node)
gen_ptnet_PlaceNode_Node = Generalization(general=Node, specific=ptnet_PlaceNode)
gen_ptnet_TransitionNode_Node = Generalization(general=Node, specific=ptnet_TransitionNode)
gen_ptnet_Place_PlaceNode = Generalization(general=PlaceNode, specific=ptnet_Place)
gen_ptnet_RefTransition_TransitionNode = Generalization(general=TransitionNode, specific=ptnet_RefTransition)
gen_ptnet_Transition_TransitionNode = Generalization(general=TransitionNode, specific=ptnet_Transition)
gen_ptnet_RefPlace_PlaceNode = Generalization(general=PlaceNode, specific=ptnet_RefPlace)
gen_ptnet_Attribute_Label = Generalization(general=Label, specific=ptnet_Attribute)
gen_ptnet_Annotation_Label = Generalization(general=Label, specific=ptnet_Annotation)
gen_ptnet_GSPNTransition_Transition = Generalization(general=Transition, specific=ptnet_GSPNTransition)
gen_ptnet_GSPNArc_Arc = Generalization(general=Arc, specific=ptnet_GSPNArc)
gen_ptnet_GSPNImmediateTransition_GSPNTransition = Generalization(general=GSPNTransition, specific=ptnet_GSPNImmediateTransition)
gen_ptnet_GSPNTimedTransition_GSPNTransition = Generalization(general=GSPNTransition, specific=ptnet_GSPNTimedTransition)
gen_ptnet_Deterministic_Distribution = Generalization(general=Distribution, specific=ptnet_Deterministic)
gen_ptnet_Exponential_Distribution = Generalization(general=Distribution, specific=ptnet_Exponential)
gen_ptnet_Gaussian_Distribution = Generalization(general=Distribution, specific=ptnet_Gaussian)
gen_ptnet_Uniform_Distribution = Generalization(general=Distribution, specific=ptnet_Uniform)
gen_ptnet_Gamma_Distribution = Generalization(general=Distribution, specific=ptnet_Gamma)
gen_ptnet_Weibull_Distribution = Generalization(general=Distribution, specific=ptnet_Weibull)
gen_ptnet_ValueExpression_ArithmeticExpression = Generalization(general=ArithmeticExpression, specific=ptnet_ValueExpression)
gen_ptnet_MarkingExpression_ArithmeticExpression = Generalization(general=ArithmeticExpression, specific=ptnet_MarkingExpression)
gen_ptnet_ArithmeticExpression_Expression = Generalization(general=Expression, specific=ptnet_ArithmeticExpression)
gen_ptnet_ArithmeticBinaryOperator_ArithmeticExpression = Generalization(general=ArithmeticExpression, specific=ptnet_ArithmeticBinaryOperator)
gen_ptnet_OpSum_ArithmeticBinaryOperator = Generalization(general=ArithmeticBinaryOperator, specific=ptnet_OpSum)
gen_ptnet_OpMinus_ArithmeticBinaryOperator = Generalization(general=ArithmeticBinaryOperator, specific=ptnet_OpMinus)
gen_ptnet_OpMultiply_ArithmeticBinaryOperator = Generalization(general=ArithmeticBinaryOperator, specific=ptnet_OpMultiply)
gen_ptnet_OpDivide_ArithmeticBinaryOperator = Generalization(general=ArithmeticBinaryOperator, specific=ptnet_OpDivide)
gen_ptnet_IfThenElse_ArithmeticExpression = Generalization(general=ArithmeticExpression, specific=ptnet_IfThenElse)
gen_ptnet_LogicalExpression_Expression = Generalization(general=Expression, specific=ptnet_LogicalExpression)
gen_ptnet_OpTrue_LogicalExpression = Generalization(general=LogicalExpression, specific=ptnet_OpTrue)
gen_ptnet_OpFalse_LogicalExpression = Generalization(general=LogicalExpression, specific=ptnet_OpFalse)
gen_ptnet_ComparisonOperator_LogicalExpression = Generalization(general=LogicalExpression, specific=ptnet_ComparisonOperator)
gen_ptnet_BooleanExpression_LogicalExpression = Generalization(general=LogicalExpression, specific=ptnet_BooleanExpression)
gen_ptnet_OpEqual_ComparisonOperator = Generalization(general=ComparisonOperator, specific=ptnet_OpEqual)
gen_ptnet_OpGreater_ComparisonOperator = Generalization(general=ComparisonOperator, specific=ptnet_OpGreater)
gen_ptnet_OpLess_ComparisonOperator = Generalization(general=ComparisonOperator, specific=ptnet_OpLess)
gen_ptnet_OpGreaterEqual_ComparisonOperator = Generalization(general=ComparisonOperator, specific=ptnet_OpGreaterEqual)
gen_ptnet_OpLessEqual_ComparisonOperator = Generalization(general=ComparisonOperator, specific=ptnet_OpLessEqual)
gen_ptnet_OpNot_LogicalExpression = Generalization(general=LogicalExpression, specific=ptnet_OpNot)
gen_ptnet_OpAnd_BooleanExpression = Generalization(general=BooleanExpression, specific=ptnet_OpAnd)
gen_ptnet_OpOr_BooleanExpression = Generalization(general=BooleanExpression, specific=ptnet_OpOr)
gen_ptnet_SteadyState_EvaluationType = Generalization(general=EvaluationType, specific=ptnet_SteadyState)
gen_ptnet_InstantOfTime_EvaluationType = Generalization(general=EvaluationType, specific=ptnet_InstantOfTime)
gen_ptnet_IntervalOfTime_EvaluationType = Generalization(general=EvaluationType, specific=ptnet_IntervalOfTime)
gen_ptnet_IntervalOfTimeAveraged_EvaluationType = Generalization(general=EvaluationType, specific=ptnet_IntervalOfTimeAveraged)
gen_ptnet_VariableExpression_ArithmeticExpression = Generalization(general=ArithmeticExpression, specific=ptnet_VariableExpression)

# Domain Model
domain_model = DomainModel(
    name="ptnet",
    types={ptnet_PTArcAnnotation, ptnet_Arc, ptnet_PetriNetDoc, ptnet_PetriNet, ptnet_PTMarking, Annotation, ptnet_Place, ptnet_Page, ptnet_Name, ptnet_ToolInfo, PnObject, ptnet_Label, ptnet_PnObject, ptnet_NodeGraphics, ptnet_Graphics, ptnet_Coordinate, ptnet_AnyObject, Graphics, ptnet_Position, ptnet_Dimension, ptnet_Fill, ptnet_Line, ptnet_Node, Coordinate, ptnet_ArcGraphics, ptnet_Offset, ptnet_AnnotationGraphics, ptnet_Font, ptnet_Annotation, ptnet_PlaceNode, Node, ptnet_RefPlace, ptnet_TransitionNode, ptnet_RefTransition, PlaceNode, TransitionNode, ptnet_Transition, ptnet_Attribute, Label, ptnet_GSPNTransition, Transition, ptnet_LogicalExpression, ptnet_GSPNArc, Arc, ptnet_ArithmeticExpression, ptnet_GSPNImmediateTransition, GSPNTransition, ptnet_GSPNTimedTransition, ptnet_Distribution, ptnet_Deterministic, Distribution, ptnet_Exponential, ptnet_Gaussian, ptnet_Uniform, ptnet_Gamma, ptnet_Weibull, ptnet_EvaluationList, ptnet_Study, ptnet_Measure, ptnet_VariableValues, ptnet_EvaluationType, ptnet_Expression, ptnet_ValueExpression, ArithmeticExpression, ptnet_MarkingExpression, Expression, ptnet_ArithmeticBinaryOperator, ptnet_OpSum, ArithmeticBinaryOperator, ptnet_OpMinus, ptnet_OpMultiply, ptnet_OpDivide, ptnet_IfThenElse, ptnet_OpTrue, LogicalExpression, ptnet_OpFalse, ptnet_ComparisonOperator, ptnet_BooleanExpression, ptnet_OpEqual, ComparisonOperator, ptnet_OpGreater, ptnet_OpLess, ptnet_OpGreaterEqual, ptnet_OpLessEqual, ptnet_OpNot, ptnet_OpAnd, BooleanExpression, ptnet_OpOr, ptnet_SteadyState, EvaluationType, ptnet_InstantOfTime, ptnet_IntervalOfTime, ptnet_IntervalOfTimeAveraged, ptnet_Variable, ptnet_VariableExpression, PNType, CSS2Color, Gradient, LineShape, FontAlign, FontDecoration, CSS2FontFamily, CSS2FontSize, CSS2FontStyle, CSS2FontWeight, LineStyle, GSPNTransitionType, GSPNArcType},
    associations={containerPlace0, containerArc1, nets2, pages3, name4, toolspecifics5, containerPetriNetDoc7, containerNamePetriNet19, containerNamePnObject21, containerPetriNet24, containerPnObject26, objects8, containerPetriNet9, nodegraphics11, name13, toolspecifics15, containerPage17, containerNode39, containerPage40, containerLabel29, toolInfoModel31, toolspecifics32, position34, dimension35, fill36, line37, containerArcGraphics43, containerPNodeGraphics44, containerAnnotationGraphics46, containerDNodeGraphics47, offset49, fill50, line53, font56, containerAnnotation58, containerNodeGraphics59, containerAnnotationGraphics61, containerNodeGraphics64, containerArcGraphics66, containerAnnotationGraphics69, positions72, line74, containerArc77, source79, target81, arcgraphics83, inscription85, InArcs87, OutArcs89, nodegraphics91, containerAnnotationGraphics93, referencingPlaces95, referencingTransitions96, initialMarking98, ref99, ref100, annotationgraphics101, containerToolInfo103, Guard105, MultiplicityFunction106, Distribution107, studies108, measures109, vars111, rewardFunction113, evaluationType116, place118, expression1119, expression2121, condition124, ifTrue126, ifFalse129, expression1132, expression2134, expression1137, expression2139, expression142, intervalBegin146, intervalEnd148, intervalBegin151, intervalEnd153, instant144, variable158, variable156},
    generalizations={gen_ptnet_PTArcAnnotation_Annotation, gen_ptnet_PTMarking_Annotation, gen_ptnet_Page_PnObject, gen_ptnet_Name_Annotation, gen_ptnet_NodeGraphics_Graphics, gen_ptnet_Offset_Coordinate, gen_ptnet_Position_Coordinate, gen_ptnet_Dimension_Coordinate, gen_ptnet_AnnotationGraphics_Graphics, gen_ptnet_ArcGraphics_Graphics, gen_ptnet_Arc_PnObject, gen_ptnet_Node_PnObject, gen_ptnet_PlaceNode_Node, gen_ptnet_TransitionNode_Node, gen_ptnet_Place_PlaceNode, gen_ptnet_RefTransition_TransitionNode, gen_ptnet_Transition_TransitionNode, gen_ptnet_RefPlace_PlaceNode, gen_ptnet_Attribute_Label, gen_ptnet_Annotation_Label, gen_ptnet_GSPNTransition_Transition, gen_ptnet_GSPNArc_Arc, gen_ptnet_GSPNImmediateTransition_GSPNTransition, gen_ptnet_GSPNTimedTransition_GSPNTransition, gen_ptnet_Deterministic_Distribution, gen_ptnet_Exponential_Distribution, gen_ptnet_Gaussian_Distribution, gen_ptnet_Uniform_Distribution, gen_ptnet_Gamma_Distribution, gen_ptnet_Weibull_Distribution, gen_ptnet_ValueExpression_ArithmeticExpression, gen_ptnet_MarkingExpression_ArithmeticExpression, gen_ptnet_ArithmeticExpression_Expression, gen_ptnet_ArithmeticBinaryOperator_ArithmeticExpression, gen_ptnet_OpSum_ArithmeticBinaryOperator, gen_ptnet_OpMinus_ArithmeticBinaryOperator, gen_ptnet_OpMultiply_ArithmeticBinaryOperator, gen_ptnet_OpDivide_ArithmeticBinaryOperator, gen_ptnet_IfThenElse_ArithmeticExpression, gen_ptnet_LogicalExpression_Expression, gen_ptnet_OpTrue_LogicalExpression, gen_ptnet_OpFalse_LogicalExpression, gen_ptnet_ComparisonOperator_LogicalExpression, gen_ptnet_BooleanExpression_LogicalExpression, gen_ptnet_OpEqual_ComparisonOperator, gen_ptnet_OpGreater_ComparisonOperator, gen_ptnet_OpLess_ComparisonOperator, gen_ptnet_OpGreaterEqual_ComparisonOperator, gen_ptnet_OpLessEqual_ComparisonOperator, gen_ptnet_OpNot_LogicalExpression, gen_ptnet_OpAnd_BooleanExpression, gen_ptnet_OpOr_BooleanExpression, gen_ptnet_SteadyState_EvaluationType, gen_ptnet_InstantOfTime_EvaluationType, gen_ptnet_IntervalOfTime_EvaluationType, gen_ptnet_IntervalOfTimeAveraged_EvaluationType, gen_ptnet_VariableExpression_ArithmeticExpression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)