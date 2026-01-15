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
AccessType: Enumeration = Enumeration(
    name="AccessType",
    literals={
            EnumerationLiteral(name="write"),
			EnumerationLiteral(name="read"),
			EnumerationLiteral(name="internal")
    }
)

SimpleType: Enumeration = Enumeration(
    name="SimpleType",
    literals={
            EnumerationLiteral(name="String"),
			EnumerationLiteral(name="Int"),
			EnumerationLiteral(name="Double")
    }
)

Font: Enumeration = Enumeration(
    name="Font",
    literals={
            EnumerationLiteral(name="arial"),
			EnumerationLiteral(name="arialblack"),
			EnumerationLiteral(name="comicsansms"),
			EnumerationLiteral(name="couriernew"),
			EnumerationLiteral(name="georgia"),
			EnumerationLiteral(name="mssansserif"),
			EnumerationLiteral(name="msserif"),
			EnumerationLiteral(name="impact"),
			EnumerationLiteral(name="lucidaconsole"),
			EnumerationLiteral(name="lucidasansunicode"),
			EnumerationLiteral(name="palatinolinotype"),
			EnumerationLiteral(name="tahoma"),
			EnumerationLiteral(name="timesnewroman"),
			EnumerationLiteral(name="trebuchetms"),
			EnumerationLiteral(name="verdana"),
			EnumerationLiteral(name="symbol"),
			EnumerationLiteral(name="webdings"),
			EnumerationLiteral(name="windings")
    }
)

Color: Enumeration = Enumeration(
    name="Color",
    literals={
            EnumerationLiteral(name="aliceblue"),
			EnumerationLiteral(name="antiquewhite"),
			EnumerationLiteral(name="aqua"),
			EnumerationLiteral(name="aquamarine"),
			EnumerationLiteral(name="azure"),
			EnumerationLiteral(name="beige"),
			EnumerationLiteral(name="bisque"),
			EnumerationLiteral(name="black"),
			EnumerationLiteral(name="blanchedalmond"),
			EnumerationLiteral(name="blue"),
			EnumerationLiteral(name="blueviolet"),
			EnumerationLiteral(name="brown"),
			EnumerationLiteral(name="burlywood"),
			EnumerationLiteral(name="cadetblue"),
			EnumerationLiteral(name="chartreuse"),
			EnumerationLiteral(name="chocolate"),
			EnumerationLiteral(name="coral"),
			EnumerationLiteral(name="cornflowerblue"),
			EnumerationLiteral(name="cornsilk"),
			EnumerationLiteral(name="crimson"),
			EnumerationLiteral(name="cyan"),
			EnumerationLiteral(name="darkblue"),
			EnumerationLiteral(name="darkcyan"),
			EnumerationLiteral(name="darkgoldenrod"),
			EnumerationLiteral(name="darkgray"),
			EnumerationLiteral(name="darkgreen"),
			EnumerationLiteral(name="darkkhaki"),
			EnumerationLiteral(name="darkmagenta"),
			EnumerationLiteral(name="darkolivegreen"),
			EnumerationLiteral(name="darkorange"),
			EnumerationLiteral(name="darkorchid"),
			EnumerationLiteral(name="darkred"),
			EnumerationLiteral(name="darksalmon"),
			EnumerationLiteral(name="darkseagreen"),
			EnumerationLiteral(name="darkslateblue"),
			EnumerationLiteral(name="darkslategray"),
			EnumerationLiteral(name="darkturquoise"),
			EnumerationLiteral(name="darkviolet"),
			EnumerationLiteral(name="deeppink"),
			EnumerationLiteral(name="gray"),
			EnumerationLiteral(name="green"),
			EnumerationLiteral(name="greenyellow"),
			EnumerationLiteral(name="honeydew"),
			EnumerationLiteral(name="hotpink"),
			EnumerationLiteral(name="indianred"),
			EnumerationLiteral(name="indigo"),
			EnumerationLiteral(name="ivory"),
			EnumerationLiteral(name="khaki"),
			EnumerationLiteral(name="lavender"),
			EnumerationLiteral(name="lavenderblush"),
			EnumerationLiteral(name="lawngreen"),
			EnumerationLiteral(name="lemonchiffon"),
			EnumerationLiteral(name="lightblue"),
			EnumerationLiteral(name="lightcoral"),
			EnumerationLiteral(name="lightcyan"),
			EnumerationLiteral(name="lightgoldenrodyellow"),
			EnumerationLiteral(name="lightgreen"),
			EnumerationLiteral(name="lightgray"),
			EnumerationLiteral(name="lightmagenta"),
			EnumerationLiteral(name="lightpink"),
			EnumerationLiteral(name="lightsalmon"),
			EnumerationLiteral(name="lightseagreen"),
			EnumerationLiteral(name="lightskyblue"),
			EnumerationLiteral(name="lightslategray"),
			EnumerationLiteral(name="deepskyblue"),
			EnumerationLiteral(name="dimgray"),
			EnumerationLiteral(name="dodgerblue"),
			EnumerationLiteral(name="firebrick"),
			EnumerationLiteral(name="floralwhite"),
			EnumerationLiteral(name="forestgreen"),
			EnumerationLiteral(name="fuchsia"),
			EnumerationLiteral(name="gainsboro"),
			EnumerationLiteral(name="ghostwhite"),
			EnumerationLiteral(name="gold"),
			EnumerationLiteral(name="goldenrod"),
			EnumerationLiteral(name="linen"),
			EnumerationLiteral(name="magenta"),
			EnumerationLiteral(name="maroon"),
			EnumerationLiteral(name="mediumaquamarine"),
			EnumerationLiteral(name="mediumblue"),
			EnumerationLiteral(name="mediumorchid"),
			EnumerationLiteral(name="mediumpurple"),
			EnumerationLiteral(name="mediumseagreen"),
			EnumerationLiteral(name="mediumslateblue"),
			EnumerationLiteral(name="mediumspringgreen"),
			EnumerationLiteral(name="mediumturquoise"),
			EnumerationLiteral(name="mediumvioletred"),
			EnumerationLiteral(name="midnightblue"),
			EnumerationLiteral(name="mintcream"),
			EnumerationLiteral(name="mistyrose"),
			EnumerationLiteral(name="moccasin"),
			EnumerationLiteral(name="navajowhite"),
			EnumerationLiteral(name="lightsteelblue"),
			EnumerationLiteral(name="lightyellow"),
			EnumerationLiteral(name="lime"),
			EnumerationLiteral(name="limegreen"),
			EnumerationLiteral(name="orange"),
			EnumerationLiteral(name="orangered"),
			EnumerationLiteral(name="orchid"),
			EnumerationLiteral(name="palegoldenrod"),
			EnumerationLiteral(name="palegreen"),
			EnumerationLiteral(name="paleturquoise"),
			EnumerationLiteral(name="palevioletred"),
			EnumerationLiteral(name="papayawhip"),
			EnumerationLiteral(name="peachpuff"),
			EnumerationLiteral(name="peru"),
			EnumerationLiteral(name="pink"),
			EnumerationLiteral(name="plum"),
			EnumerationLiteral(name="powderblue"),
			EnumerationLiteral(name="purple"),
			EnumerationLiteral(name="red"),
			EnumerationLiteral(name="rosybrown"),
			EnumerationLiteral(name="royalblue"),
			EnumerationLiteral(name="navy"),
			EnumerationLiteral(name="oldlace"),
			EnumerationLiteral(name="olive"),
			EnumerationLiteral(name="olivedrab"),
			EnumerationLiteral(name="seashell"),
			EnumerationLiteral(name="sienna"),
			EnumerationLiteral(name="silver"),
			EnumerationLiteral(name="skyblue"),
			EnumerationLiteral(name="slateblue"),
			EnumerationLiteral(name="slategray"),
			EnumerationLiteral(name="snow"),
			EnumerationLiteral(name="springgreen"),
			EnumerationLiteral(name="steelblue"),
			EnumerationLiteral(name="tan"),
			EnumerationLiteral(name="teal"),
			EnumerationLiteral(name="thistle"),
			EnumerationLiteral(name="tomato"),
			EnumerationLiteral(name="turquoise"),
			EnumerationLiteral(name="violet"),
			EnumerationLiteral(name="saddlebrown"),
			EnumerationLiteral(name="salmon"),
			EnumerationLiteral(name="sandybrown"),
			EnumerationLiteral(name="seagreen"),
			EnumerationLiteral(name="yellowgreen"),
			EnumerationLiteral(name="wheat"),
			EnumerationLiteral(name="white"),
			EnumerationLiteral(name="whitesmoke"),
			EnumerationLiteral(name="yellow")
    }
)

ButtonType: Enumeration = Enumeration(
    name="ButtonType",
    literals={
            EnumerationLiteral(name="ok"),
			EnumerationLiteral(name="okcancel"),
			EnumerationLiteral(name="yesno"),
			EnumerationLiteral(name="yesnocancel"),
			EnumerationLiteral(name="retrycancel"),
			EnumerationLiteral(name="defok"),
			EnumerationLiteral(name="defcancel"),
			EnumerationLiteral(name="defyes"),
			EnumerationLiteral(name="defno"),
			EnumerationLiteral(name="defretry")
    }
)

EventName: Enumeration = Enumeration(
    name="EventName",
    literals={
            EnumerationLiteral(name="beforecreatemodel"),
			EnumerationLiteral(name="beforecreaterelationinstance"),
			EnumerationLiteral(name="beforedeleteinstance"),
			EnumerationLiteral(name="beforedeletemodel"),
			EnumerationLiteral(name="beforediscardmodel"),
			EnumerationLiteral(name="beforesavemodel"),
			EnumerationLiteral(name="createinstance"),
			EnumerationLiteral(name="createmodel"),
			EnumerationLiteral(name="createrelationinstance"),
			EnumerationLiteral(name="deleteinstance"),
			EnumerationLiteral(name="deletemodel"),
			EnumerationLiteral(name="deleterelationinstance"),
			EnumerationLiteral(name="discardinstance"),
			EnumerationLiteral(name="discardmodel"),
			EnumerationLiteral(name="openmodel"),
			EnumerationLiteral(name="renameinstance"),
			EnumerationLiteral(name="savemodel"),
			EnumerationLiteral(name="setattributevalue"),
			EnumerationLiteral(name="aftercreatemodelingconnector"),
			EnumerationLiteral(name="aftercreatemodelingnode"),
			EnumerationLiteral(name="aftereditattributevalue"),
			EnumerationLiteral(name="toolinitialized")
    }
)

AttrGetParams: Enumeration = Enumeration(
    name="AttrGetParams",
    literals={
            EnumerationLiteral(name="type"),
			EnumerationLiteral(name="value"),
			EnumerationLiteral(name="name")
    }
)

AttrSetParams: Enumeration = Enumeration(
    name="AttrSetParams",
    literals={
            EnumerationLiteral(name="value")
    }
)

# Classes
mMDSL_IncludeLibraryType = Class(name="mMDSL::IncludeLibraryType")
mMDSL_EmbedPlatformType = Class(name="mMDSL::EmbedPlatformType")
mMDSL_EmbedCodeType = Class(name="mMDSL::EmbedCodeType")
mMDSL_IncludeLibrary = Class(name="mMDSL::IncludeLibrary")
mMDSL_EmbedCode = Class(name="mMDSL::EmbedCode")
mMDSL_Method = Class(name="mMDSL::Method")
mMDSL_Root = Class(name="mMDSL::Root")
mMDSL_MethodName = Class(name="mMDSL::MethodName")
mMDSL_InsertEmbedCode = Class(name="mMDSL::InsertEmbedCode")
mMDSL_Enumeration = Class(name="mMDSL::Enumeration")
mMDSL_SymbolStyle = Class(name="mMDSL::SymbolStyle")
mMDSL_SymbolClass = Class(name="mMDSL::SymbolClass")
mMDSL_SymbolRelation = Class(name="mMDSL::SymbolRelation")
mMDSL_Metamodel = Class(name="mMDSL::Metamodel")
mMDSL_Algorithm = Class(name="mMDSL::Algorithm")
mMDSL_Event = Class(name="mMDSL::Event")
mMDSL_Class = Class(name="mMDSL::Class")
mMDSL_Relation = Class(name="mMDSL::Relation")
mMDSL_Attribute = Class(name="mMDSL::Attribute")
mMDSL_ModelType = Class(name="mMDSL::ModelType")
mMDSL_Reference = Class(name="mMDSL::Reference")
mMDSL_Type = Class(name="mMDSL::Type")
mMDSL_RefName = Class(name="mMDSL::RefName")
mMDSL_ClassAttribute = Class(name="mMDSL::ClassAttribute")
mMDSL_EnumType = Class(name="mMDSL::EnumType")
mMDSL_Mode = Class(name="mMDSL::Mode")
mMDSL_SVGCommand = Class(name="mMDSL::SVGCommand")
mMDSL_Rectangle = Class(name="mMDSL::Rectangle")
mMDSL_Circle = Class(name="mMDSL::Circle")
mMDSL_Ellipse = Class(name="mMDSL::Ellipse")
mMDSL_Line = Class(name="mMDSL::Line")
mMDSL_Polyline = Class(name="mMDSL::Polyline")
mMDSL_Polygon = Class(name="mMDSL::Polygon")
mMDSL_Path = Class(name="mMDSL::Path")
mMDSL_Text = Class(name="mMDSL::Text")
mMDSL_Points = Class(name="mMDSL::Points")
mMDSL_PathData = Class(name="mMDSL::PathData")
mMDSL_FontFamily = Class(name="mMDSL::FontFamily")
mMDSL_FillColor = Class(name="mMDSL::FillColor")
mMDSL_VerticalLineTo = Class(name="mMDSL::VerticalLineTo")
mMDSL_CurveTo = Class(name="mMDSL::CurveTo")
mMDSL_SmoothCurveTo = Class(name="mMDSL::SmoothCurveTo")
mMDSL_QuadraticBezierCurve = Class(name="mMDSL::QuadraticBezierCurve")
mMDSL_SmoothQuadraticBezierCurveTo = Class(name="mMDSL::SmoothQuadraticBezierCurveTo")
mMDSL_EllipticalArc = Class(name="mMDSL::EllipticalArc")
mMDSL_PathParametersMLT = Class(name="mMDSL::PathParametersMLT")
mMDSL_PathParametersHV = Class(name="mMDSL::PathParametersHV")
mMDSL_PathParametersC = Class(name="mMDSL::PathParametersC")
mMDSL_MoveTo = Class(name="mMDSL::MoveTo")
mMDSL_LineTo = Class(name="mMDSL::LineTo")
mMDSL_HorizontalLineTo = Class(name="mMDSL::HorizontalLineTo")
mMDSL_PathParametersQ = Class(name="mMDSL::PathParametersQ")
mMDSL_PathParametersA = Class(name="mMDSL::PathParametersA")
mMDSL_PathParametersS = Class(name="mMDSL::PathParametersS")
mMDSL_StrokeColor = Class(name="mMDSL::StrokeColor")
mMDSL_Statement = Class(name="mMDSL::Statement")
mMDSL_SelectionStatement = Class(name="mMDSL::SelectionStatement")
mMDSL_LoopStatement = Class(name="mMDSL::LoopStatement")
mMDSL_Variable = Class(name="mMDSL::Variable")
mMDSL_AlgorithmOperation = Class(name="mMDSL::AlgorithmOperation")
mMDSL_WhileLoop = Class(name="mMDSL::WhileLoop")
mMDSL_ForLoop = Class(name="mMDSL::ForLoop")
mMDSL_BreakContinue = Class(name="mMDSL::BreakContinue")
mMDSL_Expr = Class(name="mMDSL::Expr")
mMDSL_OperatorAssign = Class(name="mMDSL::OperatorAssign")
mMDSL_VarStatement = Class(name="mMDSL::VarStatement")
mMDSL_OperatorMultyAssign = Class(name="mMDSL::OperatorMultyAssign")
mMDSL_OperatorCompare = Class(name="mMDSL::OperatorCompare")
mMDSL_OperatorEqual = Class(name="mMDSL::OperatorEqual")
mMDSL_OperatorAnd = Class(name="mMDSL::OperatorAnd")
mMDSL_OperatorUnary = Class(name="mMDSL::OperatorUnary")
mMDSL_OperatorMultiply = Class(name="mMDSL::OperatorMultiply")
mMDSL_FileOperation = Class(name="mMDSL::FileOperation")
mMDSL_OperatorAdd = Class(name="mMDSL::OperatorAdd")
mMDSL_DirOperation = Class(name="mMDSL::DirOperation")
mMDSL_SimpleUI = Class(name="mMDSL::SimpleUI")
mMDSL_ModelOperation = Class(name="mMDSL::ModelOperation")
mMDSL_InstanceOperation = Class(name="mMDSL::InstanceOperation")
mMDSL_AttributeOperation = Class(name="mMDSL::AttributeOperation")
mMDSL_OperatorOr = Class(name="mMDSL::OperatorOr")
mMDSL_Expression = Class(name="mMDSL::Expression")
mMDSL_EObject = Class(name="mMDSL::EObject")
mMDSL_DirGetWorking = Class(name="mMDSL::DirGetWorking")
mMDSL_DirCreate = Class(name="mMDSL::DirCreate")
mMDSL_DirDelete = Class(name="mMDSL::DirDelete")
mMDSL_DirList = Class(name="mMDSL::DirList")
mMDSL_FileCopy = Class(name="mMDSL::FileCopy")
mMDSL_FileDelete = Class(name="mMDSL::FileDelete")
mMDSL_FileCreate = Class(name="mMDSL::FileCreate")
mMDSL_FileRead = Class(name="mMDSL::FileRead")
mMDSL_FileWrite = Class(name="mMDSL::FileWrite")
mMDSL_DirSetWorking = Class(name="mMDSL::DirSetWorking")
mMDSL_EditBox = Class(name="mMDSL::EditBox")
mMDSL_InfoBox = Class(name="mMDSL::InfoBox")
mMDSL_ErrorBox = Class(name="mMDSL::ErrorBox")
mMDSL_WarningBox = Class(name="mMDSL::WarningBox")
mMDSL_ViewBox = Class(name="mMDSL::ViewBox")
mMDSL_ItemOperation = Class(name="mMDSL::ItemOperation")
mMDSL_RemoveMenuItem = Class(name="mMDSL::RemoveMenuItem")
mMDSL_MenuItem = Class(name="mMDSL::MenuItem")
mMDSL_ContextItem = Class(name="mMDSL::ContextItem")
mMDSL_InsertMenuItem = Class(name="mMDSL::InsertMenuItem")
mMDSL_ModelIsLoaded = Class(name="mMDSL::ModelIsLoaded")
mMDSL_InsertContextItem = Class(name="mMDSL::InsertContextItem")
mMDSL_RemoveContextItem = Class(name="mMDSL::RemoveContextItem")
mMDSL_ModelCreate = Class(name="mMDSL::ModelCreate")
mMDSL_ModelDelete = Class(name="mMDSL::ModelDelete")
mMDSL_ModelDiscard = Class(name="mMDSL::ModelDiscard")
mMDSL_ModelSave = Class(name="mMDSL::ModelSave")
mMDSL_ModelLoad = Class(name="mMDSL::ModelLoad")
mMDSL_ClassInstance = Class(name="mMDSL::ClassInstance")
mMDSL_RelationInstance = Class(name="mMDSL::RelationInstance")
mMDSL_ClassInstanceCreate = Class(name="mMDSL::ClassInstanceCreate")
mMDSL_ClassInstanceDelete = Class(name="mMDSL::ClassInstanceDelete")
mMDSL_ClassInstanceGet = Class(name="mMDSL::ClassInstanceGet")
mMDSL_ClassInstanceSet = Class(name="mMDSL::ClassInstanceSet")
mMDSL_ClassInstanceGetAll = Class(name="mMDSL::ClassInstanceGetAll")
mMDSL_RelationInstanceCreate = Class(name="mMDSL::RelationInstanceCreate")
mMDSL_RelationInstanceDelete = Class(name="mMDSL::RelationInstanceDelete")
mMDSL_RelationInstanceGet = Class(name="mMDSL::RelationInstanceGet")
mMDSL_RelationInstanceSet = Class(name="mMDSL::RelationInstanceSet")
mMDSL_RelationInstanceGetAll = Class(name="mMDSL::RelationInstanceGetAll")
mMDSL_AttributeGet = Class(name="mMDSL::AttributeGet")
mMDSL_AttributeSet = Class(name="mMDSL::AttributeSet")
mMDSL_OrExpression = Class(name="mMDSL::OrExpression")
Expression = Class(name="Expression")
mMDSL_AndExpression = Class(name="mMDSL::AndExpression")
mMDSL_EqualExpression = Class(name="mMDSL::EqualExpression")
mMDSL_CompareExpression = Class(name="mMDSL::CompareExpression")
mMDSL_AdditionExpression = Class(name="mMDSL::AdditionExpression")
mMDSL_MultiplicationExpression = Class(name="mMDSL::MultiplicationExpression")

# mMDSL_IncludeLibraryType class attributes and methods
mMDSL_IncludeLibraryType_name: Property = Property(name="name", type=StringType)
mMDSL_IncludeLibraryType.attributes={mMDSL_IncludeLibraryType_name}

# mMDSL_EmbedPlatformType class attributes and methods
mMDSL_EmbedPlatformType_name: Property = Property(name="name", type=StringType)
mMDSL_EmbedPlatformType.attributes={mMDSL_EmbedPlatformType_name}

# mMDSL_EmbedCodeType class attributes and methods
mMDSL_EmbedCodeType_name: Property = Property(name="name", type=StringType)
mMDSL_EmbedCodeType.attributes={mMDSL_EmbedCodeType_name}

# mMDSL_IncludeLibrary class attributes and methods
mMDSL_IncludeLibrary_name: Property = Property(name="name", type=StringType)
mMDSL_IncludeLibrary.attributes={mMDSL_IncludeLibrary_name}

# mMDSL_EmbedCode class attributes and methods
mMDSL_EmbedCode_embeddedcode: Property = Property(name="embeddedcode", type=StringType)
mMDSL_EmbedCode_name: Property = Property(name="name", type=StringType)
mMDSL_EmbedCode.attributes={mMDSL_EmbedCode_name, mMDSL_EmbedCode_embeddedcode}

# mMDSL_Method class attributes and methods

# mMDSL_Root class attributes and methods

# mMDSL_MethodName class attributes and methods
mMDSL_MethodName_name: Property = Property(name="name", type=StringType)
mMDSL_MethodName.attributes={mMDSL_MethodName_name}

# mMDSL_InsertEmbedCode class attributes and methods

# mMDSL_Enumeration class attributes and methods
mMDSL_Enumeration_name: Property = Property(name="name", type=StringType)
mMDSL_Enumeration_enumvalues: Property = Property(name="enumvalues", type=StringType)
mMDSL_Enumeration.attributes={mMDSL_Enumeration_enumvalues, mMDSL_Enumeration_name}

# mMDSL_SymbolStyle class attributes and methods
mMDSL_SymbolStyle_strokewidth: Property = Property(name="strokewidth", type=StringType)
mMDSL_SymbolStyle_fontsize: Property = Property(name="fontsize", type=StringType)
mMDSL_SymbolStyle_name: Property = Property(name="name", type=StringType)
mMDSL_SymbolStyle.attributes={mMDSL_SymbolStyle_fontsize, mMDSL_SymbolStyle_strokewidth, mMDSL_SymbolStyle_name}

# mMDSL_SymbolClass class attributes and methods
mMDSL_SymbolClass_name: Property = Property(name="name", type=StringType)
mMDSL_SymbolClass.attributes={mMDSL_SymbolClass_name}

# mMDSL_SymbolRelation class attributes and methods
mMDSL_SymbolRelation_name: Property = Property(name="name", type=StringType)
mMDSL_SymbolRelation.attributes={mMDSL_SymbolRelation_name}

# mMDSL_Metamodel class attributes and methods

# mMDSL_Algorithm class attributes and methods
mMDSL_Algorithm_name: Property = Property(name="name", type=StringType)
mMDSL_Algorithm.attributes={mMDSL_Algorithm_name}

# mMDSL_Event class attributes and methods
mMDSL_Event_name: Property = Property(name="name", type=StringType)
mMDSL_Event.attributes={mMDSL_Event_name}

# mMDSL_Class class attributes and methods
mMDSL_Class_name: Property = Property(name="name", type=StringType)
mMDSL_Class.attributes={mMDSL_Class_name}

# mMDSL_Relation class attributes and methods
mMDSL_Relation_name: Property = Property(name="name", type=StringType)
mMDSL_Relation.attributes={mMDSL_Relation_name}

# mMDSL_Attribute class attributes and methods
mMDSL_Attribute_name: Property = Property(name="name", type=StringType)
mMDSL_Attribute_access: Property = Property(name="access", type=StringType)
mMDSL_Attribute.attributes={mMDSL_Attribute_name, mMDSL_Attribute_access}

# mMDSL_ModelType class attributes and methods
mMDSL_ModelType_name: Property = Property(name="name", type=StringType)
mMDSL_ModelType.attributes={mMDSL_ModelType_name}

# mMDSL_Reference class attributes and methods
mMDSL_Reference_name: Property = Property(name="name", type=StringType)
mMDSL_Reference.attributes={mMDSL_Reference_name}

# mMDSL_Type class attributes and methods
mMDSL_Type_simpletype: Property = Property(name="simpletype", type=StringType)
mMDSL_Type.attributes={mMDSL_Type_simpletype}

# mMDSL_RefName class attributes and methods

# mMDSL_ClassAttribute class attributes and methods
mMDSL_ClassAttribute_name: Property = Property(name="name", type=StringType)
mMDSL_ClassAttribute.attributes={mMDSL_ClassAttribute_name}

# mMDSL_EnumType class attributes and methods

# mMDSL_Mode class attributes and methods
mMDSL_Mode_name: Property = Property(name="name", type=StringType)
mMDSL_Mode.attributes={mMDSL_Mode_name}

# mMDSL_SVGCommand class attributes and methods

# mMDSL_Rectangle class attributes and methods
mMDSL_Rectangle_x: Property = Property(name="x", type=StringType)
mMDSL_Rectangle_y: Property = Property(name="y", type=StringType)
mMDSL_Rectangle_width: Property = Property(name="width", type=StringType)
mMDSL_Rectangle_height: Property = Property(name="height", type=StringType)
mMDSL_Rectangle.attributes={mMDSL_Rectangle_width, mMDSL_Rectangle_height, mMDSL_Rectangle_y, mMDSL_Rectangle_x}

# mMDSL_Circle class attributes and methods
mMDSL_Circle_cx: Property = Property(name="cx", type=StringType)
mMDSL_Circle_cy: Property = Property(name="cy", type=StringType)
mMDSL_Circle_r: Property = Property(name="r", type=StringType)
mMDSL_Circle.attributes={mMDSL_Circle_cy, mMDSL_Circle_r, mMDSL_Circle_cx}

# mMDSL_Ellipse class attributes and methods
mMDSL_Ellipse_cx: Property = Property(name="cx", type=StringType)
mMDSL_Ellipse_cy: Property = Property(name="cy", type=StringType)
mMDSL_Ellipse_rx: Property = Property(name="rx", type=StringType)
mMDSL_Ellipse_ry: Property = Property(name="ry", type=StringType)
mMDSL_Ellipse.attributes={mMDSL_Ellipse_rx, mMDSL_Ellipse_ry, mMDSL_Ellipse_cx, mMDSL_Ellipse_cy}

# mMDSL_Line class attributes and methods
mMDSL_Line_x1: Property = Property(name="x1", type=StringType)
mMDSL_Line_y1: Property = Property(name="y1", type=StringType)
mMDSL_Line_x2: Property = Property(name="x2", type=StringType)
mMDSL_Line_y2: Property = Property(name="y2", type=StringType)
mMDSL_Line.attributes={mMDSL_Line_x2, mMDSL_Line_y1, mMDSL_Line_x1, mMDSL_Line_y2}

# mMDSL_Polyline class attributes and methods

# mMDSL_Polygon class attributes and methods

# mMDSL_Path class attributes and methods

# mMDSL_Text class attributes and methods
mMDSL_Text_value: Property = Property(name="value", type=StringType)
mMDSL_Text_x: Property = Property(name="x", type=StringType)
mMDSL_Text_y: Property = Property(name="y", type=StringType)
mMDSL_Text_fontsize: Property = Property(name="fontsize", type=StringType)
mMDSL_Text.attributes={mMDSL_Text_value, mMDSL_Text_y, mMDSL_Text_x, mMDSL_Text_fontsize}

# mMDSL_Points class attributes and methods
mMDSL_Points_x: Property = Property(name="x", type=StringType)
mMDSL_Points_y: Property = Property(name="y", type=StringType)
mMDSL_Points.attributes={mMDSL_Points_x, mMDSL_Points_y}

# mMDSL_PathData class attributes and methods
mMDSL_PathData_closepath: Property = Property(name="closepath", type=StringType)
mMDSL_PathData.attributes={mMDSL_PathData_closepath}

# mMDSL_FontFamily class attributes and methods
mMDSL_FontFamily_fontstr: Property = Property(name="fontstr", type=StringType)
mMDSL_FontFamily_font: Property = Property(name="font", type=StringType)
mMDSL_FontFamily.attributes={mMDSL_FontFamily_fontstr, mMDSL_FontFamily_font}

# mMDSL_FillColor class attributes and methods
mMDSL_FillColor_color: Property = Property(name="color", type=StringType)
mMDSL_FillColor_hexcolor: Property = Property(name="hexcolor", type=StringType)
mMDSL_FillColor.attributes={mMDSL_FillColor_hexcolor, mMDSL_FillColor_color}

# mMDSL_VerticalLineTo class attributes and methods

# mMDSL_CurveTo class attributes and methods

# mMDSL_SmoothCurveTo class attributes and methods

# mMDSL_QuadraticBezierCurve class attributes and methods

# mMDSL_SmoothQuadraticBezierCurveTo class attributes and methods

# mMDSL_EllipticalArc class attributes and methods

# mMDSL_PathParametersMLT class attributes and methods
mMDSL_PathParametersMLT_x: Property = Property(name="x", type=StringType)
mMDSL_PathParametersMLT_y: Property = Property(name="y", type=StringType)
mMDSL_PathParametersMLT.attributes={mMDSL_PathParametersMLT_y, mMDSL_PathParametersMLT_x}

# mMDSL_PathParametersHV class attributes and methods
mMDSL_PathParametersHV_x: Property = Property(name="x", type=StringType)
mMDSL_PathParametersHV.attributes={mMDSL_PathParametersHV_x}

# mMDSL_PathParametersC class attributes and methods
mMDSL_PathParametersC_x1: Property = Property(name="x1", type=StringType)
mMDSL_PathParametersC_y1: Property = Property(name="y1", type=StringType)
mMDSL_PathParametersC_x2: Property = Property(name="x2", type=StringType)
mMDSL_PathParametersC_y2: Property = Property(name="y2", type=StringType)
mMDSL_PathParametersC_x: Property = Property(name="x", type=StringType)
mMDSL_PathParametersC_y: Property = Property(name="y", type=StringType)
mMDSL_PathParametersC.attributes={mMDSL_PathParametersC_x, mMDSL_PathParametersC_y, mMDSL_PathParametersC_y2, mMDSL_PathParametersC_x1, mMDSL_PathParametersC_x2, mMDSL_PathParametersC_y1}

# mMDSL_MoveTo class attributes and methods

# mMDSL_LineTo class attributes and methods

# mMDSL_HorizontalLineTo class attributes and methods

# mMDSL_PathParametersQ class attributes and methods
mMDSL_PathParametersQ_x1: Property = Property(name="x1", type=StringType)
mMDSL_PathParametersQ_y1: Property = Property(name="y1", type=StringType)
mMDSL_PathParametersQ_x: Property = Property(name="x", type=StringType)
mMDSL_PathParametersQ_y: Property = Property(name="y", type=StringType)
mMDSL_PathParametersQ.attributes={mMDSL_PathParametersQ_x, mMDSL_PathParametersQ_y, mMDSL_PathParametersQ_x1, mMDSL_PathParametersQ_y1}

# mMDSL_PathParametersA class attributes and methods
mMDSL_PathParametersA_rx: Property = Property(name="rx", type=StringType)
mMDSL_PathParametersA_ry: Property = Property(name="ry", type=StringType)
mMDSL_PathParametersA_xaxisrot: Property = Property(name="xaxisrot", type=StringType)
mMDSL_PathParametersA_largearcflag: Property = Property(name="largearcflag", type=StringType)
mMDSL_PathParametersA_sweepflag: Property = Property(name="sweepflag", type=StringType)
mMDSL_PathParametersA_x: Property = Property(name="x", type=StringType)
mMDSL_PathParametersA_y: Property = Property(name="y", type=StringType)
mMDSL_PathParametersA.attributes={mMDSL_PathParametersA_x, mMDSL_PathParametersA_largearcflag, mMDSL_PathParametersA_y, mMDSL_PathParametersA_xaxisrot, mMDSL_PathParametersA_sweepflag, mMDSL_PathParametersA_rx, mMDSL_PathParametersA_ry}

# mMDSL_PathParametersS class attributes and methods
mMDSL_PathParametersS_x2: Property = Property(name="x2", type=StringType)
mMDSL_PathParametersS_y: Property = Property(name="y", type=StringType)
mMDSL_PathParametersS_y2: Property = Property(name="y2", type=StringType)
mMDSL_PathParametersS_x: Property = Property(name="x", type=StringType)
mMDSL_PathParametersS.attributes={mMDSL_PathParametersS_x2, mMDSL_PathParametersS_y2, mMDSL_PathParametersS_x, mMDSL_PathParametersS_y}

# mMDSL_StrokeColor class attributes and methods
mMDSL_StrokeColor_color: Property = Property(name="color", type=StringType)
mMDSL_StrokeColor_hexcolor: Property = Property(name="hexcolor", type=StringType)
mMDSL_StrokeColor.attributes={mMDSL_StrokeColor_hexcolor, mMDSL_StrokeColor_color}

# mMDSL_Statement class attributes and methods

# mMDSL_SelectionStatement class attributes and methods

# mMDSL_LoopStatement class attributes and methods

# mMDSL_Variable class attributes and methods
mMDSL_Variable_name: Property = Property(name="name", type=StringType)
mMDSL_Variable.attributes={mMDSL_Variable_name}

# mMDSL_AlgorithmOperation class attributes and methods

# mMDSL_WhileLoop class attributes and methods

# mMDSL_ForLoop class attributes and methods
mMDSL_ForLoop_start: Property = Property(name="start", type=IntegerType)
mMDSL_ForLoop_stop: Property = Property(name="stop", type=IntegerType)
mMDSL_ForLoop_interval: Property = Property(name="interval", type=IntegerType)
mMDSL_ForLoop.attributes={mMDSL_ForLoop_stop, mMDSL_ForLoop_interval, mMDSL_ForLoop_start}

# mMDSL_BreakContinue class attributes and methods
mMDSL_BreakContinue_break: Property = Property(name="break", type=StringType)
mMDSL_BreakContinue_continue: Property = Property(name="continue", type=StringType)
mMDSL_BreakContinue.attributes={mMDSL_BreakContinue_continue, mMDSL_BreakContinue_break}

# mMDSL_Expr class attributes and methods

# mMDSL_OperatorAssign class attributes and methods
mMDSL_OperatorAssign_assign: Property = Property(name="assign", type=StringType)
mMDSL_OperatorAssign.attributes={mMDSL_OperatorAssign_assign}

# mMDSL_VarStatement class attributes and methods

# mMDSL_OperatorMultyAssign class attributes and methods
mMDSL_OperatorMultyAssign_addassign: Property = Property(name="addassign", type=StringType)
mMDSL_OperatorMultyAssign_subassign: Property = Property(name="subassign", type=StringType)
mMDSL_OperatorMultyAssign_multiassign: Property = Property(name="multiassign", type=StringType)
mMDSL_OperatorMultyAssign_divassign: Property = Property(name="divassign", type=StringType)
mMDSL_OperatorMultyAssign.attributes={mMDSL_OperatorMultyAssign_multiassign, mMDSL_OperatorMultyAssign_subassign, mMDSL_OperatorMultyAssign_divassign, mMDSL_OperatorMultyAssign_addassign}

# mMDSL_OperatorCompare class attributes and methods
mMDSL_OperatorCompare_greaterequal: Property = Property(name="greaterequal", type=StringType)
mMDSL_OperatorCompare_lesserequal: Property = Property(name="lesserequal", type=StringType)
mMDSL_OperatorCompare_greater: Property = Property(name="greater", type=StringType)
mMDSL_OperatorCompare_lesser: Property = Property(name="lesser", type=StringType)
mMDSL_OperatorCompare.attributes={mMDSL_OperatorCompare_lesser, mMDSL_OperatorCompare_lesserequal, mMDSL_OperatorCompare_greaterequal, mMDSL_OperatorCompare_greater}

# mMDSL_OperatorEqual class attributes and methods
mMDSL_OperatorEqual_equal: Property = Property(name="equal", type=StringType)
mMDSL_OperatorEqual_notequal: Property = Property(name="notequal", type=StringType)
mMDSL_OperatorEqual.attributes={mMDSL_OperatorEqual_notequal, mMDSL_OperatorEqual_equal}

# mMDSL_OperatorAnd class attributes and methods
mMDSL_OperatorAnd_and: Property = Property(name="and", type=StringType)
mMDSL_OperatorAnd.attributes={mMDSL_OperatorAnd_and}

# mMDSL_OperatorUnary class attributes and methods
mMDSL_OperatorUnary_not: Property = Property(name="not", type=StringType)
mMDSL_OperatorUnary.attributes={mMDSL_OperatorUnary_not}

# mMDSL_OperatorMultiply class attributes and methods
mMDSL_OperatorMultiply_multiply: Property = Property(name="multiply", type=StringType)
mMDSL_OperatorMultiply_divide: Property = Property(name="divide", type=StringType)
mMDSL_OperatorMultiply_modulo: Property = Property(name="modulo", type=StringType)
mMDSL_OperatorMultiply.attributes={mMDSL_OperatorMultiply_modulo, mMDSL_OperatorMultiply_divide, mMDSL_OperatorMultiply_multiply}

# mMDSL_FileOperation class attributes and methods

# mMDSL_OperatorAdd class attributes and methods
mMDSL_OperatorAdd_subtract: Property = Property(name="subtract", type=StringType)
mMDSL_OperatorAdd_add: Property = Property(name="add", type=StringType)
mMDSL_OperatorAdd.attributes={mMDSL_OperatorAdd_subtract, mMDSL_OperatorAdd_add}

# mMDSL_DirOperation class attributes and methods

# mMDSL_SimpleUI class attributes and methods

# mMDSL_ModelOperation class attributes and methods

# mMDSL_InstanceOperation class attributes and methods

# mMDSL_AttributeOperation class attributes and methods

# mMDSL_OperatorOr class attributes and methods
mMDSL_OperatorOr_or: Property = Property(name="or", type=StringType)
mMDSL_OperatorOr.attributes={mMDSL_OperatorOr_or}

# mMDSL_Expression class attributes and methods
mMDSL_Expression_true: Property = Property(name="true", type=StringType)
mMDSL_Expression_false: Property = Property(name="false", type=StringType)
mMDSL_Expression_valueString: Property = Property(name="valueString", type=StringType)
mMDSL_Expression_valueRealNumber: Property = Property(name="valueRealNumber", type=StringType)
mMDSL_Expression.attributes={mMDSL_Expression_false, mMDSL_Expression_valueString, mMDSL_Expression_true, mMDSL_Expression_valueRealNumber}

# mMDSL_EObject class attributes and methods

# mMDSL_DirGetWorking class attributes and methods

# mMDSL_DirCreate class attributes and methods
mMDSL_DirCreate_dirname: Property = Property(name="dirname", type=StringType)
mMDSL_DirCreate.attributes={mMDSL_DirCreate_dirname}

# mMDSL_DirDelete class attributes and methods
mMDSL_DirDelete_dirname: Property = Property(name="dirname", type=StringType)
mMDSL_DirDelete.attributes={mMDSL_DirDelete_dirname}

# mMDSL_DirList class attributes and methods
mMDSL_DirList_dirname: Property = Property(name="dirname", type=StringType)
mMDSL_DirList.attributes={mMDSL_DirList_dirname}

# mMDSL_FileCopy class attributes and methods
mMDSL_FileCopy_src: Property = Property(name="src", type=StringType)
mMDSL_FileCopy_dest: Property = Property(name="dest", type=StringType)
mMDSL_FileCopy.attributes={mMDSL_FileCopy_src, mMDSL_FileCopy_dest}

# mMDSL_FileDelete class attributes and methods
mMDSL_FileDelete_filename: Property = Property(name="filename", type=StringType)
mMDSL_FileDelete.attributes={mMDSL_FileDelete_filename}

# mMDSL_FileCreate class attributes and methods
mMDSL_FileCreate_filename: Property = Property(name="filename", type=StringType)
mMDSL_FileCreate.attributes={mMDSL_FileCreate_filename}

# mMDSL_FileRead class attributes and methods
mMDSL_FileRead_filename: Property = Property(name="filename", type=StringType)
mMDSL_FileRead.attributes={mMDSL_FileRead_filename}

# mMDSL_FileWrite class attributes and methods
mMDSL_FileWrite_filename: Property = Property(name="filename", type=StringType)
mMDSL_FileWrite_text: Property = Property(name="text", type=StringType)
mMDSL_FileWrite_append: Property = Property(name="append", type=StringType)
mMDSL_FileWrite.attributes={mMDSL_FileWrite_filename, mMDSL_FileWrite_append, mMDSL_FileWrite_text}

# mMDSL_DirSetWorking class attributes and methods
mMDSL_DirSetWorking_dirname: Property = Property(name="dirname", type=StringType)
mMDSL_DirSetWorking.attributes={mMDSL_DirSetWorking_dirname}

# mMDSL_EditBox class attributes and methods
mMDSL_EditBox_title: Property = Property(name="title", type=StringType)
mMDSL_EditBox_text: Property = Property(name="text", type=StringType)
mMDSL_EditBox_okbuttontext: Property = Property(name="okbuttontext", type=StringType)
mMDSL_EditBox.attributes={mMDSL_EditBox_title, mMDSL_EditBox_okbuttontext, mMDSL_EditBox_text}

# mMDSL_InfoBox class attributes and methods
mMDSL_InfoBox_title: Property = Property(name="title", type=StringType)
mMDSL_InfoBox_text: Property = Property(name="text", type=StringType)
mMDSL_InfoBox.attributes={mMDSL_InfoBox_title, mMDSL_InfoBox_text}

# mMDSL_ErrorBox class attributes and methods
mMDSL_ErrorBox_title: Property = Property(name="title", type=StringType)
mMDSL_ErrorBox_text: Property = Property(name="text", type=StringType)
mMDSL_ErrorBox_buttontype: Property = Property(name="buttontype", type=StringType)
mMDSL_ErrorBox.attributes={mMDSL_ErrorBox_buttontype, mMDSL_ErrorBox_text, mMDSL_ErrorBox_title}

# mMDSL_WarningBox class attributes and methods
mMDSL_WarningBox_title: Property = Property(name="title", type=StringType)
mMDSL_WarningBox_text: Property = Property(name="text", type=StringType)
mMDSL_WarningBox_buttontype: Property = Property(name="buttontype", type=StringType)
mMDSL_WarningBox.attributes={mMDSL_WarningBox_text, mMDSL_WarningBox_title, mMDSL_WarningBox_buttontype}

# mMDSL_ViewBox class attributes and methods
mMDSL_ViewBox_title: Property = Property(name="title", type=StringType)
mMDSL_ViewBox_text: Property = Property(name="text", type=StringType)
mMDSL_ViewBox.attributes={mMDSL_ViewBox_title, mMDSL_ViewBox_text}

# mMDSL_ItemOperation class attributes and methods

# mMDSL_RemoveMenuItem class attributes and methods

# mMDSL_MenuItem class attributes and methods

# mMDSL_ContextItem class attributes and methods

# mMDSL_InsertMenuItem class attributes and methods
mMDSL_InsertMenuItem_name: Property = Property(name="name", type=StringType)
mMDSL_InsertMenuItem_menu: Property = Property(name="menu", type=StringType)
mMDSL_InsertMenuItem.attributes={mMDSL_InsertMenuItem_name, mMDSL_InsertMenuItem_menu}

# mMDSL_ModelIsLoaded class attributes and methods

# mMDSL_InsertContextItem class attributes and methods
mMDSL_InsertContextItem_name: Property = Property(name="name", type=StringType)
mMDSL_InsertContextItem_context: Property = Property(name="context", type=StringType)
mMDSL_InsertContextItem.attributes={mMDSL_InsertContextItem_name, mMDSL_InsertContextItem_context}

# mMDSL_RemoveContextItem class attributes and methods

# mMDSL_ModelCreate class attributes and methods
mMDSL_ModelCreate_name: Property = Property(name="name", type=StringType)
mMDSL_ModelCreate.attributes={mMDSL_ModelCreate_name}

# mMDSL_ModelDelete class attributes and methods

# mMDSL_ModelDiscard class attributes and methods

# mMDSL_ModelSave class attributes and methods

# mMDSL_ModelLoad class attributes and methods

# mMDSL_ClassInstance class attributes and methods

# mMDSL_RelationInstance class attributes and methods

# mMDSL_ClassInstanceCreate class attributes and methods
mMDSL_ClassInstanceCreate_name: Property = Property(name="name", type=StringType)
mMDSL_ClassInstanceCreate.attributes={mMDSL_ClassInstanceCreate_name}

# mMDSL_ClassInstanceDelete class attributes and methods

# mMDSL_ClassInstanceGet class attributes and methods

# mMDSL_ClassInstanceSet class attributes and methods

# mMDSL_ClassInstanceGetAll class attributes and methods

# mMDSL_RelationInstanceCreate class attributes and methods
mMDSL_RelationInstanceCreate_name: Property = Property(name="name", type=StringType)
mMDSL_RelationInstanceCreate.attributes={mMDSL_RelationInstanceCreate_name}

# mMDSL_RelationInstanceDelete class attributes and methods

# mMDSL_RelationInstanceGet class attributes and methods

# mMDSL_RelationInstanceSet class attributes and methods

# mMDSL_RelationInstanceGetAll class attributes and methods

# mMDSL_AttributeGet class attributes and methods
mMDSL_AttributeGet_attrgetparams: Property = Property(name="attrgetparams", type=StringType)
mMDSL_AttributeGet.attributes={mMDSL_AttributeGet_attrgetparams}

# mMDSL_AttributeSet class attributes and methods
mMDSL_AttributeSet_attrsetparams: Property = Property(name="attrsetparams", type=StringType)
mMDSL_AttributeSet_valueString: Property = Property(name="valueString", type=StringType)
mMDSL_AttributeSet_valueRealNumber: Property = Property(name="valueRealNumber", type=StringType)
mMDSL_AttributeSet.attributes={mMDSL_AttributeSet_attrsetparams, mMDSL_AttributeSet_valueString, mMDSL_AttributeSet_valueRealNumber}

# mMDSL_OrExpression class attributes and methods

# Expression class attributes and methods

# mMDSL_AndExpression class attributes and methods

# mMDSL_EqualExpression class attributes and methods

# mMDSL_CompareExpression class attributes and methods

# mMDSL_AdditionExpression class attributes and methods

# mMDSL_MultiplicationExpression class attributes and methods

# Relationships
includelibrarytype1: BinaryAssociation = BinaryAssociation(
    name="includelibrarytype1",
    ends={
        Property(name="mMDSL_IncludeLibraryType", type=mMDSL_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_Root2", type=mMDSL_IncludeLibraryType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
embedplatformtype3: BinaryAssociation = BinaryAssociation(
    name="embedplatformtype3",
    ends={
        Property(name="mMDSL_EmbedPlatformType", type=mMDSL_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_Root4", type=mMDSL_EmbedPlatformType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
embedcodetype5: BinaryAssociation = BinaryAssociation(
    name="embedcodetype5",
    ends={
        Property(name="mMDSL_EmbedCodeType", type=mMDSL_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_Root6", type=mMDSL_EmbedCodeType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
includelibrary7: BinaryAssociation = BinaryAssociation(
    name="includelibrary7",
    ends={
        Property(name="mMDSL_IncludeLibrary", type=mMDSL_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_Root8", type=mMDSL_IncludeLibrary, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
embedcode9: BinaryAssociation = BinaryAssociation(
    name="embedcode9",
    ends={
        Property(name="mMDSL_EmbedCode", type=mMDSL_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_Root10", type=mMDSL_EmbedCode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
method11: BinaryAssociation = BinaryAssociation(
    name="method11",
    ends={
        Property(name="mMDSL_Method", type=mMDSL_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_Root12", type=mMDSL_Method, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
includelibrarytype13: BinaryAssociation = BinaryAssociation(
    name="includelibrarytype13",
    ends={
        Property(name="mMDSL_IncludeLibraryType15", type=mMDSL_IncludeLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_IncludeLibrary14", type=mMDSL_IncludeLibraryType, multiplicity=Multiplicity(0, 1))
    }
)
methodname0: BinaryAssociation = BinaryAssociation(
    name="methodname0",
    ends={
        Property(name="mMDSL_MethodName", type=mMDSL_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_Root", type=mMDSL_MethodName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
codesnippetname22: BinaryAssociation = BinaryAssociation(
    name="codesnippetname22",
    ends={
        Property(name="mMDSL_EmbedCode23", type=mMDSL_InsertEmbedCode, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_InsertEmbedCode", type=mMDSL_EmbedCode, multiplicity=Multiplicity(0, 1))
    }
)
enumeration24: BinaryAssociation = BinaryAssociation(
    name="enumeration24",
    ends={
        Property(name="mMDSL_Enumeration", type=mMDSL_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_Method25", type=mMDSL_Enumeration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
embedplatformtype16: BinaryAssociation = BinaryAssociation(
    name="embedplatformtype16",
    ends={
        Property(name="mMDSL_EmbedPlatformType18", type=mMDSL_EmbedCode, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_EmbedCode17", type=mMDSL_EmbedPlatformType, multiplicity=Multiplicity(0, 1))
    }
)
embedcodetype19: BinaryAssociation = BinaryAssociation(
    name="embedcodetype19",
    ends={
        Property(name="mMDSL_EmbedCodeType21", type=mMDSL_EmbedCode, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_EmbedCode20", type=mMDSL_EmbedCodeType, multiplicity=Multiplicity(0, 1))
    }
)
symbolstyle26: BinaryAssociation = BinaryAssociation(
    name="symbolstyle26",
    ends={
        Property(name="mMDSL_SymbolStyle", type=mMDSL_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_Method27", type=mMDSL_SymbolStyle, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
symbolclass28: BinaryAssociation = BinaryAssociation(
    name="symbolclass28",
    ends={
        Property(name="mMDSL_SymbolClass", type=mMDSL_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_Method29", type=mMDSL_SymbolClass, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
symbolrelation30: BinaryAssociation = BinaryAssociation(
    name="symbolrelation30",
    ends={
        Property(name="mMDSL_SymbolRelation", type=mMDSL_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_Method31", type=mMDSL_SymbolRelation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
metamodel32: BinaryAssociation = BinaryAssociation(
    name="metamodel32",
    ends={
        Property(name="mMDSL_Metamodel", type=mMDSL_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_Method33", type=mMDSL_Metamodel, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
algorithm34: BinaryAssociation = BinaryAssociation(
    name="algorithm34",
    ends={
        Property(name="mMDSL_Algorithm", type=mMDSL_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_Method35", type=mMDSL_Algorithm, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
event36: BinaryAssociation = BinaryAssociation(
    name="event36",
    ends={
        Property(name="mMDSL_Event", type=mMDSL_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_Method37", type=mMDSL_Event, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
class38: BinaryAssociation = BinaryAssociation(
    name="class38",
    ends={
        Property(name="mMDSL_Class", type=mMDSL_Metamodel, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_Metamodel39", type=mMDSL_Class, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
relation40: BinaryAssociation = BinaryAssociation(
    name="relation40",
    ends={
        Property(name="mMDSL_Relation", type=mMDSL_Metamodel, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_Metamodel41", type=mMDSL_Relation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attribute42: BinaryAssociation = BinaryAssociation(
    name="attribute42",
    ends={
        Property(name="mMDSL_Attribute", type=mMDSL_Metamodel, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_Metamodel43", type=mMDSL_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
modeltype44: BinaryAssociation = BinaryAssociation(
    name="modeltype44",
    ends={
        Property(name="mMDSL_ModelType", type=mMDSL_Metamodel, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_Metamodel45", type=mMDSL_ModelType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
insertembedcode57: BinaryAssociation = BinaryAssociation(
    name="insertembedcode57",
    ends={
        Property(name="mMDSL_InsertEmbedCode59", type=mMDSL_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_Class58", type=mMDSL_InsertEmbedCode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reference60: BinaryAssociation = BinaryAssociation(
    name="reference60",
    ends={
        Property(name="mMDSL_Reference", type=mMDSL_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_Class61", type=mMDSL_Reference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentrelationname63: BinaryAssociation = BinaryAssociation(
    name="parentrelationname63",
    ends={
        Property(name="mMDSL_Relation64", type=mMDSL_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_Relation62", type=mMDSL_Relation, multiplicity=Multiplicity(0, 1))
    }
)
symbolrelation65: BinaryAssociation = BinaryAssociation(
    name="symbolrelation65",
    ends={
        Property(name="mMDSL_SymbolRelation67", type=mMDSL_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_Relation66", type=mMDSL_SymbolRelation, multiplicity=Multiplicity(0, 1))
    }
)
fromclassname68: BinaryAssociation = BinaryAssociation(
    name="fromclassname68",
    ends={
        Property(name="mMDSL_Class70", type=mMDSL_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_Relation69", type=mMDSL_Class, multiplicity=Multiplicity(0, 1))
    }
)
toclassname71: BinaryAssociation = BinaryAssociation(
    name="toclassname71",
    ends={
        Property(name="mMDSL_Class73", type=mMDSL_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_Relation72", type=mMDSL_Class, multiplicity=Multiplicity(0, 1))
    }
)
attribute74: BinaryAssociation = BinaryAssociation(
    name="attribute74",
    ends={
        Property(name="mMDSL_Attribute76", type=mMDSL_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_Relation75", type=mMDSL_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
insertembedcode77: BinaryAssociation = BinaryAssociation(
    name="insertembedcode77",
    ends={
        Property(name="mMDSL_InsertEmbedCode79", type=mMDSL_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_Relation78", type=mMDSL_InsertEmbedCode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type80: BinaryAssociation = BinaryAssociation(
    name="type80",
    ends={
        Property(name="mMDSL_Type", type=mMDSL_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_Attribute81", type=mMDSL_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type82: BinaryAssociation = BinaryAssociation(
    name="type82",
    ends={
        Property(name="mMDSL_Type84", type=mMDSL_ClassAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_ClassAttribute83", type=mMDSL_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parentclassname47: BinaryAssociation = BinaryAssociation(
    name="parentclassname47",
    ends={
        Property(name="mMDSL_Class48", type=mMDSL_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_Class46", type=mMDSL_Class, multiplicity=Multiplicity(0, 1))
    }
)
refname85: BinaryAssociation = BinaryAssociation(
    name="refname85",
    ends={
        Property(name="mMDSL_RefName", type=mMDSL_Reference, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_Reference86", type=mMDSL_RefName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
symbolclass49: BinaryAssociation = BinaryAssociation(
    name="symbolclass49",
    ends={
        Property(name="mMDSL_SymbolClass51", type=mMDSL_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_Class50", type=mMDSL_SymbolClass, multiplicity=Multiplicity(0, 1))
    }
)
classattribute52: BinaryAssociation = BinaryAssociation(
    name="classattribute52",
    ends={
        Property(name="mMDSL_ClassAttribute", type=mMDSL_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_Class53", type=mMDSL_ClassAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attribute54: BinaryAssociation = BinaryAssociation(
    name="attribute54",
    ends={
        Property(name="mMDSL_Attribute56", type=mMDSL_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_Class55", type=mMDSL_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
enumtype93: BinaryAssociation = BinaryAssociation(
    name="enumtype93",
    ends={
        Property(name="mMDSL_EnumType", type=mMDSL_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_Type94", type=mMDSL_EnumType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name95: BinaryAssociation = BinaryAssociation(
    name="name95",
    ends={
        Property(name="mMDSL_Enumeration97", type=mMDSL_EnumType, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_EnumType96", type=mMDSL_Enumeration, multiplicity=Multiplicity(0, 1))
    }
)
classname98: BinaryAssociation = BinaryAssociation(
    name="classname98",
    ends={
        Property(name="mMDSL_Class100", type=mMDSL_ModelType, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_ModelType99", type=mMDSL_Class, multiplicity=Multiplicity(0, 9999))
    }
)
relationname101: BinaryAssociation = BinaryAssociation(
    name="relationname101",
    ends={
        Property(name="mMDSL_Relation103", type=mMDSL_ModelType, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_ModelType102", type=mMDSL_Relation, multiplicity=Multiplicity(0, 9999))
    }
)
modename104: BinaryAssociation = BinaryAssociation(
    name="modename104",
    ends={
        Property(name="mMDSL_Mode", type=mMDSL_ModelType, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_ModelType105", type=mMDSL_Mode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
classname106: BinaryAssociation = BinaryAssociation(
    name="classname106",
    ends={
        Property(name="mMDSL_Class108", type=mMDSL_Mode, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_Mode107", type=mMDSL_Class, multiplicity=Multiplicity(0, 9999))
    }
)
relationname109: BinaryAssociation = BinaryAssociation(
    name="relationname109",
    ends={
        Property(name="mMDSL_Relation111", type=mMDSL_Mode, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_Mode110", type=mMDSL_Relation, multiplicity=Multiplicity(0, 9999))
    }
)
globalstyle112: BinaryAssociation = BinaryAssociation(
    name="globalstyle112",
    ends={
        Property(name="mMDSL_SymbolStyle114", type=mMDSL_SymbolClass, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_SymbolClass113", type=mMDSL_SymbolStyle, multiplicity=Multiplicity(0, 1))
    }
)
svgcommand115: BinaryAssociation = BinaryAssociation(
    name="svgcommand115",
    ends={
        Property(name="mMDSL_SVGCommand", type=mMDSL_SymbolClass, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_SymbolClass116", type=mMDSL_SVGCommand, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
globalstyle117: BinaryAssociation = BinaryAssociation(
    name="globalstyle117",
    ends={
        Property(name="mMDSL_SymbolStyle119", type=mMDSL_SymbolRelation, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_SymbolRelation118", type=mMDSL_SymbolStyle, multiplicity=Multiplicity(0, 1))
    }
)
modeltypename87: BinaryAssociation = BinaryAssociation(
    name="modeltypename87",
    ends={
        Property(name="mMDSL_ModelType89", type=mMDSL_RefName, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_RefName88", type=mMDSL_ModelType, multiplicity=Multiplicity(0, 1))
    }
)
classname90: BinaryAssociation = BinaryAssociation(
    name="classname90",
    ends={
        Property(name="mMDSL_Class92", type=mMDSL_RefName, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_RefName91", type=mMDSL_Class, multiplicity=Multiplicity(0, 1))
    }
)
svgcommandsmiddle123: BinaryAssociation = BinaryAssociation(
    name="svgcommandsmiddle123",
    ends={
        Property(name="mMDSL_SVGCommand125", type=mMDSL_SymbolRelation, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_SymbolRelation124", type=mMDSL_SVGCommand, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
svgcommandsto126: BinaryAssociation = BinaryAssociation(
    name="svgcommandsto126",
    ends={
        Property(name="mMDSL_SVGCommand128", type=mMDSL_SymbolRelation, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_SymbolRelation127", type=mMDSL_SVGCommand, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
insertembedcode129: BinaryAssociation = BinaryAssociation(
    name="insertembedcode129",
    ends={
        Property(name="mMDSL_InsertEmbedCode131", type=mMDSL_SVGCommand, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_SVGCommand130", type=mMDSL_InsertEmbedCode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rectangle132: BinaryAssociation = BinaryAssociation(
    name="rectangle132",
    ends={
        Property(name="mMDSL_Rectangle", type=mMDSL_SVGCommand, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_SVGCommand133", type=mMDSL_Rectangle, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
circle134: BinaryAssociation = BinaryAssociation(
    name="circle134",
    ends={
        Property(name="mMDSL_Circle", type=mMDSL_SVGCommand, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_SVGCommand135", type=mMDSL_Circle, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ellipse136: BinaryAssociation = BinaryAssociation(
    name="ellipse136",
    ends={
        Property(name="mMDSL_Ellipse", type=mMDSL_SVGCommand, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_SVGCommand137", type=mMDSL_Ellipse, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
line138: BinaryAssociation = BinaryAssociation(
    name="line138",
    ends={
        Property(name="mMDSL_Line", type=mMDSL_SVGCommand, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_SVGCommand139", type=mMDSL_Line, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
polyline140: BinaryAssociation = BinaryAssociation(
    name="polyline140",
    ends={
        Property(name="mMDSL_Polyline", type=mMDSL_SVGCommand, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_SVGCommand141", type=mMDSL_Polyline, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
polygon142: BinaryAssociation = BinaryAssociation(
    name="polygon142",
    ends={
        Property(name="mMDSL_Polygon", type=mMDSL_SVGCommand, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_SVGCommand143", type=mMDSL_Polygon, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
path144: BinaryAssociation = BinaryAssociation(
    name="path144",
    ends={
        Property(name="mMDSL_Path", type=mMDSL_SVGCommand, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_SVGCommand145", type=mMDSL_Path, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
text146: BinaryAssociation = BinaryAssociation(
    name="text146",
    ends={
        Property(name="mMDSL_Text", type=mMDSL_SVGCommand, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_SVGCommand147", type=mMDSL_Text, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
symbolstyle148: BinaryAssociation = BinaryAssociation(
    name="symbolstyle148",
    ends={
        Property(name="mMDSL_SymbolStyle150", type=mMDSL_SVGCommand, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_SVGCommand149", type=mMDSL_SymbolStyle, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
symbolstyleref151: BinaryAssociation = BinaryAssociation(
    name="symbolstyleref151",
    ends={
        Property(name="mMDSL_SymbolStyle153", type=mMDSL_SVGCommand, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_SVGCommand152", type=mMDSL_SymbolStyle, multiplicity=Multiplicity(0, 1))
    }
)
svgcommandsfrom120: BinaryAssociation = BinaryAssociation(
    name="svgcommandsfrom120",
    ends={
        Property(name="mMDSL_SVGCommand122", type=mMDSL_SymbolRelation, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_SymbolRelation121", type=mMDSL_SVGCommand, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
points154: BinaryAssociation = BinaryAssociation(
    name="points154",
    ends={
        Property(name="mMDSL_Points", type=mMDSL_Polyline, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_Polyline155", type=mMDSL_Points, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
points156: BinaryAssociation = BinaryAssociation(
    name="points156",
    ends={
        Property(name="mMDSL_Points158", type=mMDSL_Polygon, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_Polygon157", type=mMDSL_Points, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pathdata159: BinaryAssociation = BinaryAssociation(
    name="pathdata159",
    ends={
        Property(name="mMDSL_PathData", type=mMDSL_Path, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_Path160", type=mMDSL_PathData, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fontfamily161: BinaryAssociation = BinaryAssociation(
    name="fontfamily161",
    ends={
        Property(name="mMDSL_FontFamily", type=mMDSL_Text, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_Text162", type=mMDSL_FontFamily, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fillcolor163: BinaryAssociation = BinaryAssociation(
    name="fillcolor163",
    ends={
        Property(name="mMDSL_FillColor", type=mMDSL_Text, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_Text164", type=mMDSL_FillColor, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
verticallineto171: BinaryAssociation = BinaryAssociation(
    name="verticallineto171",
    ends={
        Property(name="mMDSL_VerticalLineTo", type=mMDSL_PathData, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_PathData172", type=mMDSL_VerticalLineTo, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
curveto173: BinaryAssociation = BinaryAssociation(
    name="curveto173",
    ends={
        Property(name="mMDSL_CurveTo", type=mMDSL_PathData, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_PathData174", type=mMDSL_CurveTo, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
smoothcurveto175: BinaryAssociation = BinaryAssociation(
    name="smoothcurveto175",
    ends={
        Property(name="mMDSL_SmoothCurveTo", type=mMDSL_PathData, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_PathData176", type=mMDSL_SmoothCurveTo, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
quadraticbeziercurve177: BinaryAssociation = BinaryAssociation(
    name="quadraticbeziercurve177",
    ends={
        Property(name="mMDSL_QuadraticBezierCurve", type=mMDSL_PathData, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_PathData178", type=mMDSL_QuadraticBezierCurve, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
smoothquadraticbeziercurveto179: BinaryAssociation = BinaryAssociation(
    name="smoothquadraticbeziercurveto179",
    ends={
        Property(name="mMDSL_SmoothQuadraticBezierCurveTo", type=mMDSL_PathData, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_PathData180", type=mMDSL_SmoothQuadraticBezierCurveTo, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ellipticalarc181: BinaryAssociation = BinaryAssociation(
    name="ellipticalarc181",
    ends={
        Property(name="mMDSL_EllipticalArc", type=mMDSL_PathData, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_PathData182", type=mMDSL_EllipticalArc, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters183: BinaryAssociation = BinaryAssociation(
    name="parameters183",
    ends={
        Property(name="mMDSL_PathParametersMLT", type=mMDSL_MoveTo, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_MoveTo184", type=mMDSL_PathParametersMLT, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters185: BinaryAssociation = BinaryAssociation(
    name="parameters185",
    ends={
        Property(name="mMDSL_PathParametersMLT187", type=mMDSL_LineTo, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_LineTo186", type=mMDSL_PathParametersMLT, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters188: BinaryAssociation = BinaryAssociation(
    name="parameters188",
    ends={
        Property(name="mMDSL_PathParametersHV", type=mMDSL_HorizontalLineTo, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_HorizontalLineTo189", type=mMDSL_PathParametersHV, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters190: BinaryAssociation = BinaryAssociation(
    name="parameters190",
    ends={
        Property(name="mMDSL_PathParametersHV192", type=mMDSL_VerticalLineTo, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_VerticalLineTo191", type=mMDSL_PathParametersHV, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters193: BinaryAssociation = BinaryAssociation(
    name="parameters193",
    ends={
        Property(name="mMDSL_PathParametersC", type=mMDSL_CurveTo, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_CurveTo194", type=mMDSL_PathParametersC, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
moveto165: BinaryAssociation = BinaryAssociation(
    name="moveto165",
    ends={
        Property(name="mMDSL_MoveTo", type=mMDSL_PathData, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_PathData166", type=mMDSL_MoveTo, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lineto167: BinaryAssociation = BinaryAssociation(
    name="lineto167",
    ends={
        Property(name="mMDSL_LineTo", type=mMDSL_PathData, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_PathData168", type=mMDSL_LineTo, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
horizontallineto169: BinaryAssociation = BinaryAssociation(
    name="horizontallineto169",
    ends={
        Property(name="mMDSL_HorizontalLineTo", type=mMDSL_PathData, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_PathData170", type=mMDSL_HorizontalLineTo, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters197: BinaryAssociation = BinaryAssociation(
    name="parameters197",
    ends={
        Property(name="mMDSL_PathParametersQ", type=mMDSL_QuadraticBezierCurve, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_QuadraticBezierCurve198", type=mMDSL_PathParametersQ, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters199: BinaryAssociation = BinaryAssociation(
    name="parameters199",
    ends={
        Property(name="mMDSL_PathParametersMLT201", type=mMDSL_SmoothQuadraticBezierCurveTo, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_SmoothQuadraticBezierCurveTo200", type=mMDSL_PathParametersMLT, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters202: BinaryAssociation = BinaryAssociation(
    name="parameters202",
    ends={
        Property(name="mMDSL_PathParametersA", type=mMDSL_EllipticalArc, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_EllipticalArc203", type=mMDSL_PathParametersA, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters195: BinaryAssociation = BinaryAssociation(
    name="parameters195",
    ends={
        Property(name="mMDSL_PathParametersS", type=mMDSL_SmoothCurveTo, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_SmoothCurveTo196", type=mMDSL_PathParametersS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
strokecolor207: BinaryAssociation = BinaryAssociation(
    name="strokecolor207",
    ends={
        Property(name="mMDSL_SymbolStyle208", type=mMDSL_StrokeColor, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="mMDSL_StrokeColor", type=mMDSL_SymbolStyle, multiplicity=Multiplicity(1, 1))
    }
)
fontfamily209: BinaryAssociation = BinaryAssociation(
    name="fontfamily209",
    ends={
        Property(name="mMDSL_FontFamily211", type=mMDSL_SymbolStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_SymbolStyle210", type=mMDSL_FontFamily, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
insertembedcode212: BinaryAssociation = BinaryAssociation(
    name="insertembedcode212",
    ends={
        Property(name="mMDSL_InsertEmbedCode214", type=mMDSL_SymbolStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_SymbolStyle213", type=mMDSL_InsertEmbedCode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fillcolor204: BinaryAssociation = BinaryAssociation(
    name="fillcolor204",
    ends={
        Property(name="mMDSL_FillColor206", type=mMDSL_SymbolStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_SymbolStyle205", type=mMDSL_FillColor, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
stmnt215: BinaryAssociation = BinaryAssociation(
    name="stmnt215",
    ends={
        Property(name="mMDSL_Statement", type=mMDSL_Algorithm, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_Algorithm216", type=mMDSL_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
selection217: BinaryAssociation = BinaryAssociation(
    name="selection217",
    ends={
        Property(name="mMDSL_SelectionStatement", type=mMDSL_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_Statement218", type=mMDSL_SelectionStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
loop219: BinaryAssociation = BinaryAssociation(
    name="loop219",
    ends={
        Property(name="mMDSL_LoopStatement", type=mMDSL_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_Statement220", type=mMDSL_LoopStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable221: BinaryAssociation = BinaryAssociation(
    name="variable221",
    ends={
        Property(name="mMDSL_Variable", type=mMDSL_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_Statement222", type=mMDSL_Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
algorithmoperation223: BinaryAssociation = BinaryAssociation(
    name="algorithmoperation223",
    ends={
        Property(name="mMDSL_AlgorithmOperation", type=mMDSL_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_Statement224", type=mMDSL_AlgorithmOperation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
insertembedcode225: BinaryAssociation = BinaryAssociation(
    name="insertembedcode225",
    ends={
        Property(name="mMDSL_InsertEmbedCode227", type=mMDSL_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_Statement226", type=mMDSL_InsertEmbedCode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ifcondition228: BinaryAssociation = BinaryAssociation(
    name="ifcondition228",
    ends={
        Property(name="mMDSL_Expr", type=mMDSL_SelectionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_SelectionStatement229", type=mMDSL_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ifblock230: BinaryAssociation = BinaryAssociation(
    name="ifblock230",
    ends={
        Property(name="mMDSL_Statement232", type=mMDSL_SelectionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_SelectionStatement231", type=mMDSL_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
forblock254: BinaryAssociation = BinaryAssociation(
    name="forblock254",
    ends={
        Property(name="mMDSL_Statement256", type=mMDSL_ForLoop, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_ForLoop255", type=mMDSL_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elseifcondition233: BinaryAssociation = BinaryAssociation(
    name="elseifcondition233",
    ends={
        Property(name="mMDSL_Expr235", type=mMDSL_SelectionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_SelectionStatement234", type=mMDSL_Expr, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elseifblock236: BinaryAssociation = BinaryAssociation(
    name="elseifblock236",
    ends={
        Property(name="mMDSL_Statement238", type=mMDSL_SelectionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_SelectionStatement237", type=mMDSL_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elseblock239: BinaryAssociation = BinaryAssociation(
    name="elseblock239",
    ends={
        Property(name="mMDSL_Statement241", type=mMDSL_SelectionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_SelectionStatement240", type=mMDSL_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
whiletloop242: BinaryAssociation = BinaryAssociation(
    name="whiletloop242",
    ends={
        Property(name="mMDSL_WhileLoop", type=mMDSL_LoopStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_LoopStatement243", type=mMDSL_WhileLoop, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
forloop244: BinaryAssociation = BinaryAssociation(
    name="forloop244",
    ends={
        Property(name="mMDSL_ForLoop", type=mMDSL_LoopStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_LoopStatement245", type=mMDSL_ForLoop, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition246: BinaryAssociation = BinaryAssociation(
    name="condition246",
    ends={
        Property(name="mMDSL_Expr248", type=mMDSL_WhileLoop, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_WhileLoop247", type=mMDSL_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
whileblock249: BinaryAssociation = BinaryAssociation(
    name="whileblock249",
    ends={
        Property(name="mMDSL_Statement251", type=mMDSL_WhileLoop, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_WhileLoop250", type=mMDSL_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
breakcontinue252: BinaryAssociation = BinaryAssociation(
    name="breakcontinue252",
    ends={
        Property(name="mMDSL_BreakContinue", type=mMDSL_WhileLoop, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_WhileLoop253", type=mMDSL_BreakContinue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
algorithmoperation270: BinaryAssociation = BinaryAssociation(
    name="algorithmoperation270",
    ends={
        Property(name="mMDSL_AlgorithmOperation272", type=mMDSL_VarStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_VarStatement271", type=mMDSL_AlgorithmOperation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
class273: BinaryAssociation = BinaryAssociation(
    name="class273",
    ends={
        Property(name="mMDSL_Class275", type=mMDSL_VarStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_VarStatement274", type=mMDSL_Class, multiplicity=Multiplicity(0, 1))
    }
)
attribute276: BinaryAssociation = BinaryAssociation(
    name="attribute276",
    ends={
        Property(name="mMDSL_Attribute278", type=mMDSL_VarStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_VarStatement277", type=mMDSL_Attribute, multiplicity=Multiplicity(0, 1))
    }
)
reference279: BinaryAssociation = BinaryAssociation(
    name="reference279",
    ends={
        Property(name="mMDSL_Reference281", type=mMDSL_VarStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_VarStatement280", type=mMDSL_Reference, multiplicity=Multiplicity(0, 1))
    }
)
breakcontinue257: BinaryAssociation = BinaryAssociation(
    name="breakcontinue257",
    ends={
        Property(name="mMDSL_BreakContinue259", type=mMDSL_ForLoop, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_ForLoop258", type=mMDSL_BreakContinue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
opassing260: BinaryAssociation = BinaryAssociation(
    name="opassing260",
    ends={
        Property(name="mMDSL_OperatorAssign", type=mMDSL_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_Variable261", type=mMDSL_OperatorAssign, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
varstatement262: BinaryAssociation = BinaryAssociation(
    name="varstatement262",
    ends={
        Property(name="mMDSL_VarStatement", type=mMDSL_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_Variable263", type=mMDSL_VarStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable265: BinaryAssociation = BinaryAssociation(
    name="variable265",
    ends={
        Property(name="mMDSL_Variable266", type=mMDSL_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_Variable264", type=mMDSL_Variable, multiplicity=Multiplicity(0, 1))
    }
)
expression267: BinaryAssociation = BinaryAssociation(
    name="expression267",
    ends={
        Property(name="mMDSL_Expr269", type=mMDSL_VarStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_VarStatement268", type=mMDSL_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
multyassign297: BinaryAssociation = BinaryAssociation(
    name="multyassign297",
    ends={
        Property(name="mMDSL_OperatorMultyAssign", type=mMDSL_OperatorAssign, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_OperatorAssign298", type=mMDSL_OperatorMultyAssign, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
symbolclass282: BinaryAssociation = BinaryAssociation(
    name="symbolclass282",
    ends={
        Property(name="mMDSL_SymbolClass284", type=mMDSL_VarStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_VarStatement283", type=mMDSL_SymbolClass, multiplicity=Multiplicity(0, 1))
    }
)
symbolrelation285: BinaryAssociation = BinaryAssociation(
    name="symbolrelation285",
    ends={
        Property(name="mMDSL_SymbolRelation287", type=mMDSL_VarStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_VarStatement286", type=mMDSL_SymbolRelation, multiplicity=Multiplicity(0, 1))
    }
)
symbolstyle288: BinaryAssociation = BinaryAssociation(
    name="symbolstyle288",
    ends={
        Property(name="mMDSL_SymbolStyle290", type=mMDSL_VarStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_VarStatement289", type=mMDSL_SymbolStyle, multiplicity=Multiplicity(0, 1))
    }
)
embeddedcode291: BinaryAssociation = BinaryAssociation(
    name="embeddedcode291",
    ends={
        Property(name="mMDSL_EmbedCode293", type=mMDSL_VarStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_VarStatement292", type=mMDSL_EmbedCode, multiplicity=Multiplicity(0, 1))
    }
)
modeltype294: BinaryAssociation = BinaryAssociation(
    name="modeltype294",
    ends={
        Property(name="mMDSL_ModelType296", type=mMDSL_VarStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_VarStatement295", type=mMDSL_ModelType, multiplicity=Multiplicity(0, 1))
    }
)
fileoperation321: BinaryAssociation = BinaryAssociation(
    name="fileoperation321",
    ends={
        Property(name="mMDSL_FileOperation", type=mMDSL_AlgorithmOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_AlgorithmOperation322", type=mMDSL_FileOperation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
diroperation323: BinaryAssociation = BinaryAssociation(
    name="diroperation323",
    ends={
        Property(name="mMDSL_DirOperation", type=mMDSL_AlgorithmOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_AlgorithmOperation324", type=mMDSL_DirOperation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
simpleui325: BinaryAssociation = BinaryAssociation(
    name="simpleui325",
    ends={
        Property(name="mMDSL_SimpleUI", type=mMDSL_AlgorithmOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_AlgorithmOperation326", type=mMDSL_SimpleUI, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
modeloperation327: BinaryAssociation = BinaryAssociation(
    name="modeloperation327",
    ends={
        Property(name="mMDSL_ModelOperation", type=mMDSL_AlgorithmOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_AlgorithmOperation328", type=mMDSL_ModelOperation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
instanceoperation329: BinaryAssociation = BinaryAssociation(
    name="instanceoperation329",
    ends={
        Property(name="mMDSL_InstanceOperation", type=mMDSL_AlgorithmOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_AlgorithmOperation330", type=mMDSL_InstanceOperation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
attributeoperation331: BinaryAssociation = BinaryAssociation(
    name="attributeoperation331",
    ends={
        Property(name="mMDSL_AttributeOperation", type=mMDSL_AlgorithmOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_AlgorithmOperation332", type=mMDSL_AttributeOperation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr299: BinaryAssociation = BinaryAssociation(
    name="expr299",
    ends={
        Property(name="mMDSL_Expression", type=mMDSL_Expr, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_Expr300", type=mMDSL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
op301: BinaryAssociation = BinaryAssociation(
    name="op301",
    ends={
        Property(name="mMDSL_EObject", type=mMDSL_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_Expression302", type=mMDSL_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operand304: BinaryAssociation = BinaryAssociation(
    name="operand304",
    ends={
        Property(name="mMDSL_Expression305", type=mMDSL_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_Expression303", type=mMDSL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
atomic307: BinaryAssociation = BinaryAssociation(
    name="atomic307",
    ends={
        Property(name="mMDSL_Expression308", type=mMDSL_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_Expression306", type=mMDSL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression310: BinaryAssociation = BinaryAssociation(
    name="expression310",
    ends={
        Property(name="mMDSL_Expression311", type=mMDSL_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_Expression309", type=mMDSL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable312: BinaryAssociation = BinaryAssociation(
    name="variable312",
    ends={
        Property(name="mMDSL_Variable314", type=mMDSL_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_Expression313", type=mMDSL_Variable, multiplicity=Multiplicity(0, 1))
    }
)
left316: BinaryAssociation = BinaryAssociation(
    name="left316",
    ends={
        Property(name="mMDSL_Expression317", type=mMDSL_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_Expression315", type=mMDSL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right319: BinaryAssociation = BinaryAssociation(
    name="right319",
    ends={
        Property(name="mMDSL_Expression320", type=mMDSL_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_Expression318", type=mMDSL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dirgetworking345: BinaryAssociation = BinaryAssociation(
    name="dirgetworking345",
    ends={
        Property(name="mMDSL_DirGetWorking", type=mMDSL_DirOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_DirOperation346", type=mMDSL_DirGetWorking, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dircreate347: BinaryAssociation = BinaryAssociation(
    name="dircreate347",
    ends={
        Property(name="mMDSL_DirCreate", type=mMDSL_DirOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_DirOperation348", type=mMDSL_DirCreate, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dirdelete349: BinaryAssociation = BinaryAssociation(
    name="dirdelete349",
    ends={
        Property(name="mMDSL_DirDelete", type=mMDSL_DirOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_DirOperation350", type=mMDSL_DirDelete, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dirlist351: BinaryAssociation = BinaryAssociation(
    name="dirlist351",
    ends={
        Property(name="mMDSL_DirList", type=mMDSL_DirOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_DirOperation352", type=mMDSL_DirList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
filecopy333: BinaryAssociation = BinaryAssociation(
    name="filecopy333",
    ends={
        Property(name="mMDSL_FileCopy", type=mMDSL_FileOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_FileOperation334", type=mMDSL_FileCopy, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
filedelete335: BinaryAssociation = BinaryAssociation(
    name="filedelete335",
    ends={
        Property(name="mMDSL_FileDelete", type=mMDSL_FileOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_FileOperation336", type=mMDSL_FileDelete, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
filecreate337: BinaryAssociation = BinaryAssociation(
    name="filecreate337",
    ends={
        Property(name="mMDSL_FileCreate", type=mMDSL_FileOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_FileOperation338", type=mMDSL_FileCreate, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fileread339: BinaryAssociation = BinaryAssociation(
    name="fileread339",
    ends={
        Property(name="mMDSL_FileRead", type=mMDSL_FileOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_FileOperation340", type=mMDSL_FileRead, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
filewrite341: BinaryAssociation = BinaryAssociation(
    name="filewrite341",
    ends={
        Property(name="mMDSL_FileWrite", type=mMDSL_FileOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_FileOperation342", type=mMDSL_FileWrite, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dirsetworking343: BinaryAssociation = BinaryAssociation(
    name="dirsetworking343",
    ends={
        Property(name="mMDSL_DirSetWorking", type=mMDSL_DirOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_DirOperation344", type=mMDSL_DirSetWorking, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
editbox353: BinaryAssociation = BinaryAssociation(
    name="editbox353",
    ends={
        Property(name="mMDSL_EditBox", type=mMDSL_SimpleUI, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_SimpleUI354", type=mMDSL_EditBox, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
infobox355: BinaryAssociation = BinaryAssociation(
    name="infobox355",
    ends={
        Property(name="mMDSL_InfoBox", type=mMDSL_SimpleUI, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_SimpleUI356", type=mMDSL_InfoBox, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
errorbox357: BinaryAssociation = BinaryAssociation(
    name="errorbox357",
    ends={
        Property(name="mMDSL_ErrorBox", type=mMDSL_SimpleUI, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_SimpleUI358", type=mMDSL_ErrorBox, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
warningbox359: BinaryAssociation = BinaryAssociation(
    name="warningbox359",
    ends={
        Property(name="mMDSL_WarningBox", type=mMDSL_SimpleUI, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_SimpleUI360", type=mMDSL_WarningBox, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
viewbox361: BinaryAssociation = BinaryAssociation(
    name="viewbox361",
    ends={
        Property(name="mMDSL_ViewBox", type=mMDSL_SimpleUI, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_SimpleUI362", type=mMDSL_ViewBox, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
itemoperation363: BinaryAssociation = BinaryAssociation(
    name="itemoperation363",
    ends={
        Property(name="mMDSL_ItemOperation", type=mMDSL_SimpleUI, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_SimpleUI364", type=mMDSL_ItemOperation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
removemenuitem371: BinaryAssociation = BinaryAssociation(
    name="removemenuitem371",
    ends={
        Property(name="mMDSL_RemoveMenuItem", type=mMDSL_MenuItem, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_MenuItem372", type=mMDSL_RemoveMenuItem, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
menuitem365: BinaryAssociation = BinaryAssociation(
    name="menuitem365",
    ends={
        Property(name="mMDSL_MenuItem", type=mMDSL_ItemOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_ItemOperation366", type=mMDSL_MenuItem, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
contextitem367: BinaryAssociation = BinaryAssociation(
    name="contextitem367",
    ends={
        Property(name="mMDSL_ContextItem", type=mMDSL_ItemOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_ItemOperation368", type=mMDSL_ContextItem, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
insertmenuitem369: BinaryAssociation = BinaryAssociation(
    name="insertmenuitem369",
    ends={
        Property(name="mMDSL_InsertMenuItem", type=mMDSL_MenuItem, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_MenuItem370", type=mMDSL_InsertMenuItem, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
modelisloaded393: BinaryAssociation = BinaryAssociation(
    name="modelisloaded393",
    ends={
        Property(name="mMDSL_ModelIsLoaded", type=mMDSL_ModelOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_ModelOperation394", type=mMDSL_ModelIsLoaded, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
modeltype395: BinaryAssociation = BinaryAssociation(
    name="modeltype395",
    ends={
        Property(name="mMDSL_ModelType397", type=mMDSL_ModelCreate, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_ModelCreate396", type=mMDSL_ModelType, multiplicity=Multiplicity(0, 1))
    }
)
modelname398: BinaryAssociation = BinaryAssociation(
    name="modelname398",
    ends={
        Property(name="mMDSL_ModelCreate400", type=mMDSL_ModelDelete, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_ModelDelete399", type=mMDSL_ModelCreate, multiplicity=Multiplicity(0, 1))
    }
)
modelname401: BinaryAssociation = BinaryAssociation(
    name="modelname401",
    ends={
        Property(name="mMDSL_ModelCreate403", type=mMDSL_ModelDiscard, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_ModelDiscard402", type=mMDSL_ModelCreate, multiplicity=Multiplicity(0, 1))
    }
)
modelname404: BinaryAssociation = BinaryAssociation(
    name="modelname404",
    ends={
        Property(name="mMDSL_ModelCreate406", type=mMDSL_ModelSave, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_ModelSave405", type=mMDSL_ModelCreate, multiplicity=Multiplicity(0, 1))
    }
)
menuitemname373: BinaryAssociation = BinaryAssociation(
    name="menuitemname373",
    ends={
        Property(name="mMDSL_InsertMenuItem375", type=mMDSL_RemoveMenuItem, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_RemoveMenuItem374", type=mMDSL_InsertMenuItem, multiplicity=Multiplicity(0, 1))
    }
)
insertcontextitem376: BinaryAssociation = BinaryAssociation(
    name="insertcontextitem376",
    ends={
        Property(name="mMDSL_InsertContextItem", type=mMDSL_ContextItem, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_ContextItem377", type=mMDSL_InsertContextItem, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
removecontextitem378: BinaryAssociation = BinaryAssociation(
    name="removecontextitem378",
    ends={
        Property(name="mMDSL_RemoveContextItem", type=mMDSL_ContextItem, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_ContextItem379", type=mMDSL_RemoveContextItem, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
contextitem380: BinaryAssociation = BinaryAssociation(
    name="contextitem380",
    ends={
        Property(name="mMDSL_InsertContextItem382", type=mMDSL_RemoveContextItem, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_RemoveContextItem381", type=mMDSL_InsertContextItem, multiplicity=Multiplicity(0, 1))
    }
)
modelcreate383: BinaryAssociation = BinaryAssociation(
    name="modelcreate383",
    ends={
        Property(name="mMDSL_ModelCreate", type=mMDSL_ModelOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_ModelOperation384", type=mMDSL_ModelCreate, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
modeldelete385: BinaryAssociation = BinaryAssociation(
    name="modeldelete385",
    ends={
        Property(name="mMDSL_ModelDelete", type=mMDSL_ModelOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_ModelOperation386", type=mMDSL_ModelDelete, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
modeldiscard387: BinaryAssociation = BinaryAssociation(
    name="modeldiscard387",
    ends={
        Property(name="mMDSL_ModelDiscard", type=mMDSL_ModelOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_ModelOperation388", type=mMDSL_ModelDiscard, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
modelsave389: BinaryAssociation = BinaryAssociation(
    name="modelsave389",
    ends={
        Property(name="mMDSL_ModelSave", type=mMDSL_ModelOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_ModelOperation390", type=mMDSL_ModelSave, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
modelload391: BinaryAssociation = BinaryAssociation(
    name="modelload391",
    ends={
        Property(name="mMDSL_ModelLoad", type=mMDSL_ModelOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_ModelOperation392", type=mMDSL_ModelLoad, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nameofclassinstance433: BinaryAssociation = BinaryAssociation(
    name="nameofclassinstance433",
    ends={
        Property(name="mMDSL_ClassInstanceCreate435", type=mMDSL_ClassInstanceGet, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_ClassInstanceGet434", type=mMDSL_ClassInstanceCreate, multiplicity=Multiplicity(0, 1))
    }
)
nameofclass436: BinaryAssociation = BinaryAssociation(
    name="nameofclass436",
    ends={
        Property(name="mMDSL_Class438", type=mMDSL_ClassInstanceGetAll, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_ClassInstanceGetAll437", type=mMDSL_Class, multiplicity=Multiplicity(0, 1))
    }
)
nameofclassinstance439: BinaryAssociation = BinaryAssociation(
    name="nameofclassinstance439",
    ends={
        Property(name="mMDSL_ClassInstanceCreate441", type=mMDSL_ClassInstanceSet, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_ClassInstanceSet440", type=mMDSL_ClassInstanceCreate, multiplicity=Multiplicity(0, 1))
    }
)
modelname407: BinaryAssociation = BinaryAssociation(
    name="modelname407",
    ends={
        Property(name="mMDSL_ModelCreate409", type=mMDSL_ModelLoad, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_ModelLoad408", type=mMDSL_ModelCreate, multiplicity=Multiplicity(0, 1))
    }
)
modelname410: BinaryAssociation = BinaryAssociation(
    name="modelname410",
    ends={
        Property(name="mMDSL_ModelCreate412", type=mMDSL_ModelIsLoaded, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_ModelIsLoaded411", type=mMDSL_ModelCreate, multiplicity=Multiplicity(0, 1))
    }
)
classinstance413: BinaryAssociation = BinaryAssociation(
    name="classinstance413",
    ends={
        Property(name="mMDSL_ClassInstance", type=mMDSL_InstanceOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_InstanceOperation414", type=mMDSL_ClassInstance, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
relationinstance415: BinaryAssociation = BinaryAssociation(
    name="relationinstance415",
    ends={
        Property(name="mMDSL_RelationInstance", type=mMDSL_InstanceOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_InstanceOperation416", type=mMDSL_RelationInstance, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
classinstancecreate417: BinaryAssociation = BinaryAssociation(
    name="classinstancecreate417",
    ends={
        Property(name="mMDSL_ClassInstanceCreate", type=mMDSL_ClassInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_ClassInstance418", type=mMDSL_ClassInstanceCreate, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
classinstancedelete419: BinaryAssociation = BinaryAssociation(
    name="classinstancedelete419",
    ends={
        Property(name="mMDSL_ClassInstanceDelete", type=mMDSL_ClassInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_ClassInstance420", type=mMDSL_ClassInstanceDelete, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
classinstanceget421: BinaryAssociation = BinaryAssociation(
    name="classinstanceget421",
    ends={
        Property(name="mMDSL_ClassInstanceGet", type=mMDSL_ClassInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_ClassInstance422", type=mMDSL_ClassInstanceGet, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
classinstanceset423: BinaryAssociation = BinaryAssociation(
    name="classinstanceset423",
    ends={
        Property(name="mMDSL_ClassInstanceSet", type=mMDSL_ClassInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_ClassInstance424", type=mMDSL_ClassInstanceSet, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
classinstancegetall425: BinaryAssociation = BinaryAssociation(
    name="classinstancegetall425",
    ends={
        Property(name="mMDSL_ClassInstanceGetAll", type=mMDSL_ClassInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_ClassInstance426", type=mMDSL_ClassInstanceGetAll, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nameofclass427: BinaryAssociation = BinaryAssociation(
    name="nameofclass427",
    ends={
        Property(name="mMDSL_Class429", type=mMDSL_ClassInstanceCreate, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_ClassInstanceCreate428", type=mMDSL_Class, multiplicity=Multiplicity(0, 1))
    }
)
nameofclassinstance430: BinaryAssociation = BinaryAssociation(
    name="nameofclassinstance430",
    ends={
        Property(name="mMDSL_ClassInstanceCreate432", type=mMDSL_ClassInstanceDelete, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_ClassInstanceDelete431", type=mMDSL_ClassInstanceCreate, multiplicity=Multiplicity(0, 1))
    }
)
classinstanceto458: BinaryAssociation = BinaryAssociation(
    name="classinstanceto458",
    ends={
        Property(name="mMDSL_ClassInstanceCreate460", type=mMDSL_RelationInstanceCreate, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_RelationInstanceCreate459", type=mMDSL_ClassInstanceCreate, multiplicity=Multiplicity(0, 1))
    }
)
nameofrelationinstance461: BinaryAssociation = BinaryAssociation(
    name="nameofrelationinstance461",
    ends={
        Property(name="mMDSL_RelationInstanceCreate463", type=mMDSL_RelationInstanceDelete, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_RelationInstanceDelete462", type=mMDSL_RelationInstanceCreate, multiplicity=Multiplicity(0, 1))
    }
)
nameofrelationinstance464: BinaryAssociation = BinaryAssociation(
    name="nameofrelationinstance464",
    ends={
        Property(name="mMDSL_RelationInstanceCreate466", type=mMDSL_RelationInstanceGet, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_RelationInstanceGet465", type=mMDSL_RelationInstanceCreate, multiplicity=Multiplicity(0, 1))
    }
)
relationinstancecreate442: BinaryAssociation = BinaryAssociation(
    name="relationinstancecreate442",
    ends={
        Property(name="mMDSL_RelationInstanceCreate", type=mMDSL_RelationInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_RelationInstance443", type=mMDSL_RelationInstanceCreate, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
relationinstancedelete444: BinaryAssociation = BinaryAssociation(
    name="relationinstancedelete444",
    ends={
        Property(name="mMDSL_RelationInstanceDelete", type=mMDSL_RelationInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_RelationInstance445", type=mMDSL_RelationInstanceDelete, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
relationinstanceget446: BinaryAssociation = BinaryAssociation(
    name="relationinstanceget446",
    ends={
        Property(name="mMDSL_RelationInstanceGet", type=mMDSL_RelationInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_RelationInstance447", type=mMDSL_RelationInstanceGet, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
relationinstanceset448: BinaryAssociation = BinaryAssociation(
    name="relationinstanceset448",
    ends={
        Property(name="mMDSL_RelationInstanceSet", type=mMDSL_RelationInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_RelationInstance449", type=mMDSL_RelationInstanceSet, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
relationinstancegetall450: BinaryAssociation = BinaryAssociation(
    name="relationinstancegetall450",
    ends={
        Property(name="mMDSL_RelationInstanceGetAll", type=mMDSL_RelationInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_RelationInstance451", type=mMDSL_RelationInstanceGetAll, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nameofrelation452: BinaryAssociation = BinaryAssociation(
    name="nameofrelation452",
    ends={
        Property(name="mMDSL_Relation454", type=mMDSL_RelationInstanceCreate, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_RelationInstanceCreate453", type=mMDSL_Relation, multiplicity=Multiplicity(0, 1))
    }
)
classinstancefrom455: BinaryAssociation = BinaryAssociation(
    name="classinstancefrom455",
    ends={
        Property(name="mMDSL_ClassInstanceCreate457", type=mMDSL_RelationInstanceCreate, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_RelationInstanceCreate456", type=mMDSL_ClassInstanceCreate, multiplicity=Multiplicity(0, 1))
    }
)
algorithmname483: BinaryAssociation = BinaryAssociation(
    name="algorithmname483",
    ends={
        Property(name="mMDSL_Algorithm485", type=mMDSL_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_Event484", type=mMDSL_Algorithm, multiplicity=Multiplicity(0, 1))
    }
)
nameofrelation467: BinaryAssociation = BinaryAssociation(
    name="nameofrelation467",
    ends={
        Property(name="mMDSL_Relation469", type=mMDSL_RelationInstanceGetAll, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_RelationInstanceGetAll468", type=mMDSL_Relation, multiplicity=Multiplicity(0, 1))
    }
)
nameofrelationinstance470: BinaryAssociation = BinaryAssociation(
    name="nameofrelationinstance470",
    ends={
        Property(name="mMDSL_RelationInstanceCreate472", type=mMDSL_RelationInstanceSet, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_RelationInstanceSet471", type=mMDSL_RelationInstanceCreate, multiplicity=Multiplicity(0, 1))
    }
)
attributename473: BinaryAssociation = BinaryAssociation(
    name="attributename473",
    ends={
        Property(name="mMDSL_Attribute475", type=mMDSL_AttributeOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_AttributeOperation474", type=mMDSL_Attribute, multiplicity=Multiplicity(0, 1))
    }
)
attributeget476: BinaryAssociation = BinaryAssociation(
    name="attributeget476",
    ends={
        Property(name="mMDSL_AttributeGet", type=mMDSL_AttributeOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_AttributeOperation477", type=mMDSL_AttributeGet, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
attributeset478: BinaryAssociation = BinaryAssociation(
    name="attributeset478",
    ends={
        Property(name="mMDSL_AttributeSet", type=mMDSL_AttributeOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_AttributeOperation479", type=mMDSL_AttributeSet, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
valueVariable480: BinaryAssociation = BinaryAssociation(
    name="valueVariable480",
    ends={
        Property(name="mMDSL_Variable482", type=mMDSL_AttributeSet, multiplicity=Multiplicity(1, 1)),
        Property(name="mMDSL_AttributeSet481", type=mMDSL_Variable, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_mMDSL_OrExpression_Expression = Generalization(general=Expression, specific=mMDSL_OrExpression)
gen_mMDSL_AndExpression_Expression = Generalization(general=Expression, specific=mMDSL_AndExpression)
gen_mMDSL_EqualExpression_Expression = Generalization(general=Expression, specific=mMDSL_EqualExpression)
gen_mMDSL_CompareExpression_Expression = Generalization(general=Expression, specific=mMDSL_CompareExpression)
gen_mMDSL_AdditionExpression_Expression = Generalization(general=Expression, specific=mMDSL_AdditionExpression)
gen_mMDSL_MultiplicationExpression_Expression = Generalization(general=Expression, specific=mMDSL_MultiplicationExpression)

# Domain Model
domain_model = DomainModel(
    name="mMDSL",
    types={mMDSL_IncludeLibraryType, mMDSL_EmbedPlatformType, mMDSL_EmbedCodeType, mMDSL_IncludeLibrary, mMDSL_EmbedCode, mMDSL_Method, mMDSL_Root, mMDSL_MethodName, mMDSL_InsertEmbedCode, mMDSL_Enumeration, mMDSL_SymbolStyle, mMDSL_SymbolClass, mMDSL_SymbolRelation, mMDSL_Metamodel, mMDSL_Algorithm, mMDSL_Event, mMDSL_Class, mMDSL_Relation, mMDSL_Attribute, mMDSL_ModelType, mMDSL_Reference, mMDSL_Type, mMDSL_RefName, mMDSL_ClassAttribute, mMDSL_EnumType, mMDSL_Mode, mMDSL_SVGCommand, mMDSL_Rectangle, mMDSL_Circle, mMDSL_Ellipse, mMDSL_Line, mMDSL_Polyline, mMDSL_Polygon, mMDSL_Path, mMDSL_Text, mMDSL_Points, mMDSL_PathData, mMDSL_FontFamily, mMDSL_FillColor, mMDSL_VerticalLineTo, mMDSL_CurveTo, mMDSL_SmoothCurveTo, mMDSL_QuadraticBezierCurve, mMDSL_SmoothQuadraticBezierCurveTo, mMDSL_EllipticalArc, mMDSL_PathParametersMLT, mMDSL_PathParametersHV, mMDSL_PathParametersC, mMDSL_MoveTo, mMDSL_LineTo, mMDSL_HorizontalLineTo, mMDSL_PathParametersQ, mMDSL_PathParametersA, mMDSL_PathParametersS, mMDSL_StrokeColor, mMDSL_Statement, mMDSL_SelectionStatement, mMDSL_LoopStatement, mMDSL_Variable, mMDSL_AlgorithmOperation, mMDSL_WhileLoop, mMDSL_ForLoop, mMDSL_BreakContinue, mMDSL_Expr, mMDSL_OperatorAssign, mMDSL_VarStatement, mMDSL_OperatorMultyAssign, mMDSL_OperatorCompare, mMDSL_OperatorEqual, mMDSL_OperatorAnd, mMDSL_OperatorUnary, mMDSL_OperatorMultiply, mMDSL_FileOperation, mMDSL_OperatorAdd, mMDSL_DirOperation, mMDSL_SimpleUI, mMDSL_ModelOperation, mMDSL_InstanceOperation, mMDSL_AttributeOperation, mMDSL_OperatorOr, mMDSL_Expression, mMDSL_EObject, mMDSL_DirGetWorking, mMDSL_DirCreate, mMDSL_DirDelete, mMDSL_DirList, mMDSL_FileCopy, mMDSL_FileDelete, mMDSL_FileCreate, mMDSL_FileRead, mMDSL_FileWrite, mMDSL_DirSetWorking, mMDSL_EditBox, mMDSL_InfoBox, mMDSL_ErrorBox, mMDSL_WarningBox, mMDSL_ViewBox, mMDSL_ItemOperation, mMDSL_RemoveMenuItem, mMDSL_MenuItem, mMDSL_ContextItem, mMDSL_InsertMenuItem, mMDSL_ModelIsLoaded, mMDSL_InsertContextItem, mMDSL_RemoveContextItem, mMDSL_ModelCreate, mMDSL_ModelDelete, mMDSL_ModelDiscard, mMDSL_ModelSave, mMDSL_ModelLoad, mMDSL_ClassInstance, mMDSL_RelationInstance, mMDSL_ClassInstanceCreate, mMDSL_ClassInstanceDelete, mMDSL_ClassInstanceGet, mMDSL_ClassInstanceSet, mMDSL_ClassInstanceGetAll, mMDSL_RelationInstanceCreate, mMDSL_RelationInstanceDelete, mMDSL_RelationInstanceGet, mMDSL_RelationInstanceSet, mMDSL_RelationInstanceGetAll, mMDSL_AttributeGet, mMDSL_AttributeSet, mMDSL_OrExpression, Expression, mMDSL_AndExpression, mMDSL_EqualExpression, mMDSL_CompareExpression, mMDSL_AdditionExpression, mMDSL_MultiplicationExpression, AccessType, SimpleType, Font, Color, ButtonType, EventName, AttrGetParams, AttrSetParams},
    associations={includelibrarytype1, embedplatformtype3, embedcodetype5, includelibrary7, embedcode9, method11, includelibrarytype13, methodname0, codesnippetname22, enumeration24, embedplatformtype16, embedcodetype19, symbolstyle26, symbolclass28, symbolrelation30, metamodel32, algorithm34, event36, class38, relation40, attribute42, modeltype44, insertembedcode57, reference60, parentrelationname63, symbolrelation65, fromclassname68, toclassname71, attribute74, insertembedcode77, type80, type82, parentclassname47, refname85, symbolclass49, classattribute52, attribute54, enumtype93, name95, classname98, relationname101, modename104, classname106, relationname109, globalstyle112, svgcommand115, globalstyle117, modeltypename87, classname90, svgcommandsmiddle123, svgcommandsto126, insertembedcode129, rectangle132, circle134, ellipse136, line138, polyline140, polygon142, path144, text146, symbolstyle148, symbolstyleref151, svgcommandsfrom120, points154, points156, pathdata159, fontfamily161, fillcolor163, verticallineto171, curveto173, smoothcurveto175, quadraticbeziercurve177, smoothquadraticbeziercurveto179, ellipticalarc181, parameters183, parameters185, parameters188, parameters190, parameters193, moveto165, lineto167, horizontallineto169, parameters197, parameters199, parameters202, parameters195, strokecolor207, fontfamily209, insertembedcode212, fillcolor204, stmnt215, selection217, loop219, variable221, algorithmoperation223, insertembedcode225, ifcondition228, ifblock230, forblock254, elseifcondition233, elseifblock236, elseblock239, whiletloop242, forloop244, condition246, whileblock249, breakcontinue252, algorithmoperation270, class273, attribute276, reference279, breakcontinue257, opassing260, varstatement262, variable265, expression267, multyassign297, symbolclass282, symbolrelation285, symbolstyle288, embeddedcode291, modeltype294, fileoperation321, diroperation323, simpleui325, modeloperation327, instanceoperation329, attributeoperation331, expr299, op301, operand304, atomic307, expression310, variable312, left316, right319, dirgetworking345, dircreate347, dirdelete349, dirlist351, filecopy333, filedelete335, filecreate337, fileread339, filewrite341, dirsetworking343, editbox353, infobox355, errorbox357, warningbox359, viewbox361, itemoperation363, removemenuitem371, menuitem365, contextitem367, insertmenuitem369, modelisloaded393, modeltype395, modelname398, modelname401, modelname404, menuitemname373, insertcontextitem376, removecontextitem378, contextitem380, modelcreate383, modeldelete385, modeldiscard387, modelsave389, modelload391, nameofclassinstance433, nameofclass436, nameofclassinstance439, modelname407, modelname410, classinstance413, relationinstance415, classinstancecreate417, classinstancedelete419, classinstanceget421, classinstanceset423, classinstancegetall425, nameofclass427, nameofclassinstance430, classinstanceto458, nameofrelationinstance461, nameofrelationinstance464, relationinstancecreate442, relationinstancedelete444, relationinstanceget446, relationinstanceset448, relationinstancegetall450, nameofrelation452, classinstancefrom455, algorithmname483, nameofrelation467, nameofrelationinstance470, attributename473, attributeget476, attributeset478, valueVariable480},
    generalizations={gen_mMDSL_OrExpression_Expression, gen_mMDSL_AndExpression_Expression, gen_mMDSL_EqualExpression_Expression, gen_mMDSL_CompareExpression_Expression, gen_mMDSL_AdditionExpression_Expression, gen_mMDSL_MultiplicationExpression_Expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)