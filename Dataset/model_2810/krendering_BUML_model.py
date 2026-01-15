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
LineStyle: Enumeration = Enumeration(
    name="LineStyle",
    literals={
            EnumerationLiteral(name="DASHDOT"),
			EnumerationLiteral(name="DASHDOTDOT"),
			EnumerationLiteral(name="CUSTOM"),
			EnumerationLiteral(name="SOLID"),
			EnumerationLiteral(name="DASH"),
			EnumerationLiteral(name="DOT")
    }
)

HorizontalAlignment: Enumeration = Enumeration(
    name="HorizontalAlignment",
    literals={
            EnumerationLiteral(name="LEFT"),
			EnumerationLiteral(name="CENTER"),
			EnumerationLiteral(name="RIGHT")
    }
)

VerticalAlignment: Enumeration = Enumeration(
    name="VerticalAlignment",
    literals={
            EnumerationLiteral(name="TOP"),
			EnumerationLiteral(name="CENTER"),
			EnumerationLiteral(name="BOTTOM")
    }
)

LineCap: Enumeration = Enumeration(
    name="LineCap",
    literals={
            EnumerationLiteral(name="CAP_FLAT"),
			EnumerationLiteral(name="CAP_ROUND"),
			EnumerationLiteral(name="CAP_SQUARE")
    }
)

ModifierState: Enumeration = Enumeration(
    name="ModifierState",
    literals={
            EnumerationLiteral(name="DONT_CARE"),
			EnumerationLiteral(name="PRESSED"),
			EnumerationLiteral(name="NOT_PRESSED")
    }
)

Trigger: Enumeration = Enumeration(
    name="Trigger",
    literals={
            EnumerationLiteral(name="MIDDLE_SINGLECLICK"),
			EnumerationLiteral(name="MIDDLE_DOUBLECLICK"),
			EnumerationLiteral(name="MIDDLE_SINGLE_OR_MULTICLICK"),
			EnumerationLiteral(name="SINGLECLICK"),
			EnumerationLiteral(name="DOUBLECLICK"),
			EnumerationLiteral(name="SINGLE_OR_MULTICLICK")
    }
)

LineJoin: Enumeration = Enumeration(
    name="LineJoin",
    literals={
            EnumerationLiteral(name="JOIN_MITER"),
			EnumerationLiteral(name="JOIN_ROUND"),
			EnumerationLiteral(name="JOIN_BEVEL")
    }
)

Underline: Enumeration = Enumeration(
    name="Underline",
    literals={
            EnumerationLiteral(name="NONE"),
			EnumerationLiteral(name="SINGLE"),
			EnumerationLiteral(name="DOUBLE"),
			EnumerationLiteral(name="ERROR"),
			EnumerationLiteral(name="SQUIGGLE"),
			EnumerationLiteral(name="LINK")
    }
)

Arc: Enumeration = Enumeration(
    name="Arc",
    literals={
            EnumerationLiteral(name="OPEN"),
			EnumerationLiteral(name="CHORD"),
			EnumerationLiteral(name="PIE")
    }
)

# Classes
krendering_KPosition = Class(name="krendering::KPosition")
krendering_KRendering = Class(name="krendering::KRendering", is_abstract=True)
KGraphData = Class(name="KGraphData")
KStyleHolder = Class(name="KStyleHolder")
krendering_KContainerRendering = Class(name="krendering::KContainerRendering", is_abstract=True)
krendering_KPlacementData = Class(name="krendering::KPlacementData", is_abstract=True)
krendering_KAction = Class(name="krendering::KAction")
krendering_KEllipse = Class(name="krendering::KEllipse")
KContainerRendering = Class(name="KContainerRendering")
krendering_KPolyline = Class(name="krendering::KPolyline")
krendering_KPolygon = Class(name="krendering::KPolygon")
KPolyline = Class(name="KPolyline")
krendering_KImage = Class(name="krendering::KImage")
krendering_KRectangle = Class(name="krendering::KRectangle")
krendering_KRoundedRectangle = Class(name="krendering::KRoundedRectangle")
krendering_KDecoratorPlacementData = Class(name="krendering::KDecoratorPlacementData")
KPlacementData = Class(name="KPlacementData")
krendering_KPlacement = Class(name="krendering::KPlacement", is_abstract=True)
krendering_KArc = Class(name="krendering::KArc")
krendering_KStyle = Class(name="krendering::KStyle", is_abstract=True)
EMapPropertyHolder = Class(name="EMapPropertyHolder")
KRendering = Class(name="KRendering")
krendering_KRenderingRef = Class(name="krendering::KRenderingRef")
krendering_KChildArea = Class(name="krendering::KChildArea")
krendering_KText = Class(name="krendering::KText")
krendering_KRenderingLibrary = Class(name="krendering::KRenderingLibrary")
krendering_KStyleHolder = Class(name="krendering::KStyleHolder")
krendering_KGridPlacementData = Class(name="krendering::KGridPlacementData")
KAreaPlacementData = Class(name="KAreaPlacementData")
krendering_KGridPlacement = Class(name="krendering::KGridPlacement")
KPlacement = Class(name="KPlacement")
krendering_KCustomRendering = Class(name="krendering::KCustomRendering")
krendering_KColor = Class(name="krendering::KColor")
krendering_KAreaPlacementData = Class(name="krendering::KAreaPlacementData")
krendering_KLineWidth = Class(name="krendering::KLineWidth")
KStyle = Class(name="KStyle")
krendering_KLineStyle = Class(name="krendering::KLineStyle")
krendering_KXPosition = Class(name="krendering::KXPosition", is_abstract=True)
krendering_KVerticalAlignment = Class(name="krendering::KVerticalAlignment")
krendering_KHorizontalAlignment = Class(name="krendering::KHorizontalAlignment")
krendering_KYPosition = Class(name="krendering::KYPosition", is_abstract=True)
krendering_KLeftPosition = Class(name="krendering::KLeftPosition")
krendering_KTopPosition = Class(name="krendering::KTopPosition")
krendering_KBottomPosition = Class(name="krendering::KBottomPosition")
krendering_KSpline = Class(name="krendering::KSpline")
krendering_KForeground = Class(name="krendering::KForeground")
krendering_KRightPosition = Class(name="krendering::KRightPosition")
krendering_KColoring = Class(name="krendering::KColoring", is_abstract=True)
krendering_KBackground = Class(name="krendering::KBackground")
krendering_KFontName = Class(name="krendering::KFontName")
krendering_KFontSize = Class(name="krendering::KFontSize")
krendering_KRoundedBendsPolyline = Class(name="krendering::KRoundedBendsPolyline")
krendering_KFontBold = Class(name="krendering::KFontBold")
krendering_KFontItalic = Class(name="krendering::KFontItalic")
krendering_KLineCap = Class(name="krendering::KLineCap")
krendering_KRotation = Class(name="krendering::KRotation")
krendering_KPointPlacementData = Class(name="krendering::KPointPlacementData")
krendering_KTextUnderline = Class(name="krendering::KTextUnderline")
krendering_KInvisibility = Class(name="krendering::KInvisibility")
krendering_KShadow = Class(name="krendering::KShadow")
krendering_KTextStrikeout = Class(name="krendering::KTextStrikeout")
krendering_KStyleRef = Class(name="krendering::KStyleRef")
krendering_KLineJoin = Class(name="krendering::KLineJoin")

# krendering_KPosition class attributes and methods
krendering_KPosition_m_equals: Method = Method(name="equals", parameters={Parameter(name='other')}, type=BooleanType)
krendering_KPosition_m_setPositions: Method = Method(name="setPositions", parameters={Parameter(name='y'), Parameter(name='x')}, type=StringType)
krendering_KPosition.methods={krendering_KPosition_m_equals, krendering_KPosition_m_setPositions}

# krendering_KRendering class attributes and methods

# KGraphData class attributes and methods

# KStyleHolder class attributes and methods

# krendering_KContainerRendering class attributes and methods

# krendering_KPlacementData class attributes and methods

# krendering_KAction class attributes and methods
krendering_KAction_actionId: Property = Property(name="actionId", type=StringType)
krendering_KAction_trigger: Property = Property(name="trigger", type=StringType)
krendering_KAction_altPressed: Property = Property(name="altPressed", type=StringType)
krendering_KAction_ctrlCmdPressed: Property = Property(name="ctrlCmdPressed", type=StringType)
krendering_KAction_shiftPressed: Property = Property(name="shiftPressed", type=StringType)
krendering_KAction.attributes={krendering_KAction_actionId, krendering_KAction_shiftPressed, krendering_KAction_ctrlCmdPressed, krendering_KAction_altPressed, krendering_KAction_trigger}

# krendering_KEllipse class attributes and methods

# KContainerRendering class attributes and methods

# krendering_KPolyline class attributes and methods

# krendering_KPolygon class attributes and methods

# KPolyline class attributes and methods

# krendering_KImage class attributes and methods
krendering_KImage_bundleName: Property = Property(name="bundleName", type=StringType)
krendering_KImage_imagePath: Property = Property(name="imagePath", type=StringType)
krendering_KImage_imageObject: Property = Property(name="imageObject", type=StringType)
krendering_KImage.attributes={krendering_KImage_imageObject, krendering_KImage_bundleName, krendering_KImage_imagePath}

# krendering_KRectangle class attributes and methods

# krendering_KRoundedRectangle class attributes and methods
krendering_KRoundedRectangle_cornerHeight: Property = Property(name="cornerHeight", type=FloatType)
krendering_KRoundedRectangle_cornerWidth: Property = Property(name="cornerWidth", type=FloatType)
krendering_KRoundedRectangle.attributes={krendering_KRoundedRectangle_cornerWidth, krendering_KRoundedRectangle_cornerHeight}

# krendering_KDecoratorPlacementData class attributes and methods
krendering_KDecoratorPlacementData_absolute: Property = Property(name="absolute", type=FloatType)
krendering_KDecoratorPlacementData_xOffset: Property = Property(name="xOffset", type=FloatType)
krendering_KDecoratorPlacementData_yOffset: Property = Property(name="yOffset", type=FloatType)
krendering_KDecoratorPlacementData_rotateWithLine: Property = Property(name="rotateWithLine", type=BooleanType)
krendering_KDecoratorPlacementData_width: Property = Property(name="width", type=FloatType)
krendering_KDecoratorPlacementData_height: Property = Property(name="height", type=FloatType)
krendering_KDecoratorPlacementData_relative: Property = Property(name="relative", type=FloatType)
krendering_KDecoratorPlacementData.attributes={krendering_KDecoratorPlacementData_rotateWithLine, krendering_KDecoratorPlacementData_absolute, krendering_KDecoratorPlacementData_yOffset, krendering_KDecoratorPlacementData_relative, krendering_KDecoratorPlacementData_xOffset, krendering_KDecoratorPlacementData_width, krendering_KDecoratorPlacementData_height}

# KPlacementData class attributes and methods

# krendering_KPlacement class attributes and methods

# krendering_KArc class attributes and methods
krendering_KArc_startAngle: Property = Property(name="startAngle", type=FloatType)
krendering_KArc_arcAngle: Property = Property(name="arcAngle", type=FloatType)
krendering_KArc_arcType: Property = Property(name="arcType", type=StringType)
krendering_KArc.attributes={krendering_KArc_startAngle, krendering_KArc_arcType, krendering_KArc_arcAngle}

# krendering_KStyle class attributes and methods
krendering_KStyle_propagateToChildren: Property = Property(name="propagateToChildren", type=BooleanType)
krendering_KStyle_modifierId: Property = Property(name="modifierId", type=StringType)
krendering_KStyle_selection: Property = Property(name="selection", type=BooleanType)
krendering_KStyle.attributes={krendering_KStyle_propagateToChildren, krendering_KStyle_modifierId, krendering_KStyle_selection}

# EMapPropertyHolder class attributes and methods

# KRendering class attributes and methods

# krendering_KRenderingRef class attributes and methods

# krendering_KChildArea class attributes and methods

# krendering_KText class attributes and methods
krendering_KText_text: Property = Property(name="text", type=StringType)
krendering_KText_cursorSelectable: Property = Property(name="cursorSelectable", type=BooleanType)
krendering_KText_editable: Property = Property(name="editable", type=BooleanType)
krendering_KText.attributes={krendering_KText_cursorSelectable, krendering_KText_text, krendering_KText_editable}

# krendering_KRenderingLibrary class attributes and methods

# krendering_KStyleHolder class attributes and methods
krendering_KStyleHolder_id: Property = Property(name="id", type=StringType)
krendering_KStyleHolder.attributes={krendering_KStyleHolder_id}

# krendering_KGridPlacementData class attributes and methods
krendering_KGridPlacementData_minCellWidth: Property = Property(name="minCellWidth", type=FloatType)
krendering_KGridPlacementData_minCellHeight: Property = Property(name="minCellHeight", type=FloatType)
krendering_KGridPlacementData_flexibleWidth: Property = Property(name="flexibleWidth", type=StringType)
krendering_KGridPlacementData_flexibleHeight: Property = Property(name="flexibleHeight", type=StringType)
krendering_KGridPlacementData.attributes={krendering_KGridPlacementData_flexibleHeight, krendering_KGridPlacementData_minCellWidth, krendering_KGridPlacementData_minCellHeight, krendering_KGridPlacementData_flexibleWidth}

# KAreaPlacementData class attributes and methods

# krendering_KGridPlacement class attributes and methods
krendering_KGridPlacement_numColumns: Property = Property(name="numColumns", type=IntegerType)
krendering_KGridPlacement.attributes={krendering_KGridPlacement_numColumns}

# KPlacement class attributes and methods

# krendering_KCustomRendering class attributes and methods
krendering_KCustomRendering_className: Property = Property(name="className", type=StringType)
krendering_KCustomRendering_bundleName: Property = Property(name="bundleName", type=StringType)
krendering_KCustomRendering_figureObject: Property = Property(name="figureObject", type=StringType)
krendering_KCustomRendering.attributes={krendering_KCustomRendering_bundleName, krendering_KCustomRendering_className, krendering_KCustomRendering_figureObject}

# krendering_KColor class attributes and methods
krendering_KColor_red: Property = Property(name="red", type=IntegerType)
krendering_KColor_green: Property = Property(name="green", type=IntegerType)
krendering_KColor_blue: Property = Property(name="blue", type=IntegerType)
krendering_KColor_m_setColor: Method = Method(name="setColor", parameters={Parameter(name='blue'), Parameter(name='red'), Parameter(name='green')}, type=StringType)
krendering_KColor_m_equals: Method = Method(name="equals", parameters={Parameter(name='other')}, type=BooleanType)
krendering_KColor_m_setColor: Method = Method(name="setColor", parameters={Parameter(name='color')}, type=StringType)
krendering_KColor_m_setColor: Method = Method(name="setColor", parameters={Parameter(name='kColor')}, type=StringType)
krendering_KColor.attributes={krendering_KColor_green, krendering_KColor_red, krendering_KColor_blue}
krendering_KColor.methods={krendering_KColor_m_setColor, krendering_KColor_m_setColor, krendering_KColor_m_setColor, krendering_KColor_m_equals}

# krendering_KAreaPlacementData class attributes and methods

# krendering_KLineWidth class attributes and methods
krendering_KLineWidth_lineWidth: Property = Property(name="lineWidth", type=FloatType)
krendering_KLineWidth.attributes={krendering_KLineWidth_lineWidth}

# KStyle class attributes and methods

# krendering_KLineStyle class attributes and methods
krendering_KLineStyle_lineStyle: Property = Property(name="lineStyle", type=StringType)
krendering_KLineStyle_dashPattern: Property = Property(name="dashPattern", type=FloatType)
krendering_KLineStyle_dashOffset: Property = Property(name="dashOffset", type=FloatType)
krendering_KLineStyle.attributes={krendering_KLineStyle_dashPattern, krendering_KLineStyle_dashOffset, krendering_KLineStyle_lineStyle}

# krendering_KXPosition class attributes and methods
krendering_KXPosition_relative: Property = Property(name="relative", type=FloatType)
krendering_KXPosition_absolute: Property = Property(name="absolute", type=FloatType)
krendering_KXPosition_m_equals: Method = Method(name="equals", parameters={Parameter(name='other')}, type=BooleanType)
krendering_KXPosition_m_setPosition: Method = Method(name="setPosition", parameters={Parameter(name='relative'), Parameter(name='absolute')})
krendering_KXPosition.attributes={krendering_KXPosition_absolute, krendering_KXPosition_relative}
krendering_KXPosition.methods={krendering_KXPosition_m_equals, krendering_KXPosition_m_setPosition}

# krendering_KVerticalAlignment class attributes and methods
krendering_KVerticalAlignment_verticalAlignment: Property = Property(name="verticalAlignment", type=StringType)
krendering_KVerticalAlignment.attributes={krendering_KVerticalAlignment_verticalAlignment}

# krendering_KHorizontalAlignment class attributes and methods
krendering_KHorizontalAlignment_horizontalAlignment: Property = Property(name="horizontalAlignment", type=StringType)
krendering_KHorizontalAlignment.attributes={krendering_KHorizontalAlignment_horizontalAlignment}

# krendering_KYPosition class attributes and methods
krendering_KYPosition_absolute: Property = Property(name="absolute", type=FloatType)
krendering_KYPosition_relative: Property = Property(name="relative", type=FloatType)
krendering_KYPosition_m_equals: Method = Method(name="equals", parameters={Parameter(name='other')}, type=BooleanType)
krendering_KYPosition_m_setPosition: Method = Method(name="setPosition", parameters={Parameter(name='absolute'), Parameter(name='relative')})
krendering_KYPosition.attributes={krendering_KYPosition_absolute, krendering_KYPosition_relative}
krendering_KYPosition.methods={krendering_KYPosition_m_equals, krendering_KYPosition_m_setPosition}

# krendering_KLeftPosition class attributes and methods

# krendering_KTopPosition class attributes and methods

# krendering_KBottomPosition class attributes and methods

# krendering_KSpline class attributes and methods

# krendering_KForeground class attributes and methods

# krendering_KRightPosition class attributes and methods

# krendering_KColoring class attributes and methods
krendering_KColoring_alpha: Property = Property(name="alpha", type=IntegerType)
krendering_KColoring_targetAlpha: Property = Property(name="targetAlpha", type=IntegerType)
krendering_KColoring_gradientAngle: Property = Property(name="gradientAngle", type=FloatType)
krendering_KColoring_m_setColor: Method = Method(name="setColor", parameters={Parameter(name='green'), Parameter(name='red'), Parameter(name='blue')})
krendering_KColoring_m_setColor: Method = Method(name="setColor", parameters={Parameter(name='color')})
krendering_KColoring_m_setColor: Method = Method(name="setColor", parameters={Parameter(name='color'), Parameter(name='alpha')})
krendering_KColoring_m_setColor2: Method = Method(name="setColor2", parameters={Parameter(name='color')})
krendering_KColoring_m_setColor2: Method = Method(name="setColor2", parameters={Parameter(name='color'), Parameter(name='alpha')})
krendering_KColoring_m_setColor: Method = Method(name="setColor", parameters={Parameter(name='red'), Parameter(name='green'), Parameter(name='alpha'), Parameter(name='blue')})
krendering_KColoring_m_setColorCopyOf: Method = Method(name="setColorCopyOf", parameters={Parameter(name='kColor')})
krendering_KColoring_m_setColorCopyOf: Method = Method(name="setColorCopyOf", parameters={Parameter(name='alpha'), Parameter(name='kColor')})
krendering_KColoring_m_setColorCopiedFrom: Method = Method(name="setColorCopiedFrom", parameters={Parameter(name='coloring')})
krendering_KColoring_m_setColorAndAlphaCopiedFrom: Method = Method(name="setColorAndAlphaCopiedFrom", parameters={Parameter(name='coloring')})
krendering_KColoring_m_setTargetColor: Method = Method(name="setTargetColor", parameters={Parameter(name='color')})
krendering_KColoring_m_setTargetColor: Method = Method(name="setTargetColor", parameters={Parameter(name='red'), Parameter(name='blue'), Parameter(name='alpha'), Parameter(name='green')})
krendering_KColoring_m_setTargetColor: Method = Method(name="setTargetColor", parameters={Parameter(name='blue'), Parameter(name='red'), Parameter(name='green')})
krendering_KColoring_m_setTargetColor2: Method = Method(name="setTargetColor2", parameters={Parameter(name='targetColor')})
krendering_KColoring_m_setTargetColor2: Method = Method(name="setTargetColor2", parameters={Parameter(name='targetAlpha'), Parameter(name='targetColor')})
krendering_KColoring_m_setTargetColorCopyOf: Method = Method(name="setTargetColorCopyOf", parameters={Parameter(name='targetColor')})
krendering_KColoring_m_setTargetColorCopyOf: Method = Method(name="setTargetColorCopyOf", parameters={Parameter(name='targetColor'), Parameter(name='targetAlpha')})
krendering_KColoring_m_setTargetColor: Method = Method(name="setTargetColor", parameters={Parameter(name='alpha'), Parameter(name='color')})
krendering_KColoring_m_setTargetColorCopiedFrom: Method = Method(name="setTargetColorCopiedFrom", parameters={Parameter(name='coloring')})
krendering_KColoring_m_setTargetColorAndAlphaCopiedFrom: Method = Method(name="setTargetColorAndAlphaCopiedFrom", parameters={Parameter(name='coloring')})
krendering_KColoring_m_setGradientAngle2: Method = Method(name="setGradientAngle2", parameters={Parameter(name='angle')})
krendering_KColoring_m_setColors: Method = Method(name="setColors", parameters={Parameter(name='targetColor'), Parameter(name='color')})
krendering_KColoring_m_setColors: Method = Method(name="setColors", parameters={Parameter(name='targetAlpha'), Parameter(name='targetColor'), Parameter(name='color'), Parameter(name='alpha')})
krendering_KColoring_m_setColors: Method = Method(name="setColors", parameters={Parameter(name='angle'), Parameter(name='alpha'), Parameter(name='targetColor'), Parameter(name='color'), Parameter(name='targetAlpha')})
krendering_KColoring_m_setColors: Method = Method(name="setColors", parameters={Parameter(name='angle'), Parameter(name='targetColor'), Parameter(name='color')})
krendering_KColoring_m_setColors: Method = Method(name="setColors", parameters={Parameter(name='color'), Parameter(name='targetColor')})
krendering_KColoring_m_setColors: Method = Method(name="setColors", parameters={Parameter(name='targetColor'), Parameter(name='color'), Parameter(name='angle')})
krendering_KColoring_m_setColors: Method = Method(name="setColors", parameters={Parameter(name='alpha'), Parameter(name='targetColor'), Parameter(name='targetAlpha'), Parameter(name='angle'), Parameter(name='color')})
krendering_KColoring_m_setColorsCopiesOf: Method = Method(name="setColorsCopiesOf", parameters={Parameter(name='targetColor'), Parameter(name='color')})
krendering_KColoring_m_setColors: Method = Method(name="setColors", parameters={Parameter(name='alpha'), Parameter(name='targetAlpha'), Parameter(name='color'), Parameter(name='targetColor')})
krendering_KColoring_m_setColorsCopiesOf: Method = Method(name="setColorsCopiesOf", parameters={Parameter(name='targetColor'), Parameter(name='color'), Parameter(name='angle')})
krendering_KColoring_m_setColorsCopiedFrom: Method = Method(name="setColorsCopiedFrom", parameters={Parameter(name='coloring')})
krendering_KColoring_m_setColorsCopiesOf: Method = Method(name="setColorsCopiesOf", parameters={Parameter(name='alpha'), Parameter(name='targetAlpha'), Parameter(name='targetColor'), Parameter(name='color')})
krendering_KColoring_m_setColorsCopiesOf: Method = Method(name="setColorsCopiesOf", parameters={Parameter(name='targetAlpha'), Parameter(name='alpha'), Parameter(name='angle'), Parameter(name='targetColor'), Parameter(name='color')})
krendering_KColoring_m_setColorsAlphasGradientAngleCopiedFrom: Method = Method(name="setColorsAlphasGradientAngleCopiedFrom", parameters={Parameter(name='coloring')})
krendering_KColoring_m_equals: Method = Method(name="equals", parameters={Parameter(name='other')}, type=BooleanType)
krendering_KColoring.attributes={krendering_KColoring_targetAlpha, krendering_KColoring_alpha, krendering_KColoring_gradientAngle}
krendering_KColoring.methods={krendering_KColoring_m_setColor2, krendering_KColoring_m_setColors, krendering_KColoring_m_setColor2, krendering_KColoring_m_setTargetColor2, krendering_KColoring_m_setTargetColorCopiedFrom, krendering_KColoring_m_setColorAndAlphaCopiedFrom, krendering_KColoring_m_setColors, krendering_KColoring_m_setColor, krendering_KColoring_m_setTargetColor, krendering_KColoring_m_setColors, krendering_KColoring_m_setColorsAlphasGradientAngleCopiedFrom, krendering_KColoring_m_setTargetColor, krendering_KColoring_m_setTargetColor, krendering_KColoring_m_setTargetColorCopyOf, krendering_KColoring_m_setColors, krendering_KColoring_m_setColors, krendering_KColoring_m_setColorsCopiesOf, krendering_KColoring_m_setColorCopyOf, krendering_KColoring_m_setColorsCopiedFrom, krendering_KColoring_m_setColors, krendering_KColoring_m_setColors, krendering_KColoring_m_setTargetColorCopyOf, krendering_KColoring_m_setTargetColor, krendering_KColoring_m_equals, krendering_KColoring_m_setColors, krendering_KColoring_m_setColor, krendering_KColoring_m_setColorCopyOf, krendering_KColoring_m_setColorCopiedFrom, krendering_KColoring_m_setTargetColor2, krendering_KColoring_m_setColorsCopiesOf, krendering_KColoring_m_setColorsCopiesOf, krendering_KColoring_m_setColor, krendering_KColoring_m_setColor, krendering_KColoring_m_setGradientAngle2, krendering_KColoring_m_setColorsCopiesOf, krendering_KColoring_m_setTargetColorAndAlphaCopiedFrom}

# krendering_KBackground class attributes and methods

# krendering_KFontName class attributes and methods
krendering_KFontName_name: Property = Property(name="name", type=StringType)
krendering_KFontName.attributes={krendering_KFontName_name}

# krendering_KFontSize class attributes and methods
krendering_KFontSize_size: Property = Property(name="size", type=IntegerType)
krendering_KFontSize_scaleWithZoom: Property = Property(name="scaleWithZoom", type=BooleanType)
krendering_KFontSize.attributes={krendering_KFontSize_size, krendering_KFontSize_scaleWithZoom}

# krendering_KRoundedBendsPolyline class attributes and methods
krendering_KRoundedBendsPolyline_bendRadius: Property = Property(name="bendRadius", type=FloatType)
krendering_KRoundedBendsPolyline.attributes={krendering_KRoundedBendsPolyline_bendRadius}

# krendering_KFontBold class attributes and methods
krendering_KFontBold_bold: Property = Property(name="bold", type=BooleanType)
krendering_KFontBold.attributes={krendering_KFontBold_bold}

# krendering_KFontItalic class attributes and methods
krendering_KFontItalic_italic: Property = Property(name="italic", type=BooleanType)
krendering_KFontItalic.attributes={krendering_KFontItalic_italic}

# krendering_KLineCap class attributes and methods
krendering_KLineCap_lineCap: Property = Property(name="lineCap", type=StringType)
krendering_KLineCap.attributes={krendering_KLineCap_lineCap}

# krendering_KRotation class attributes and methods
krendering_KRotation_rotation: Property = Property(name="rotation", type=FloatType)
krendering_KRotation.attributes={krendering_KRotation_rotation}

# krendering_KPointPlacementData class attributes and methods
krendering_KPointPlacementData_horizontalAlignment: Property = Property(name="horizontalAlignment", type=StringType)
krendering_KPointPlacementData_verticalAlignment: Property = Property(name="verticalAlignment", type=StringType)
krendering_KPointPlacementData_horizontalMargin: Property = Property(name="horizontalMargin", type=FloatType)
krendering_KPointPlacementData_verticalMargin: Property = Property(name="verticalMargin", type=FloatType)
krendering_KPointPlacementData_minWidth: Property = Property(name="minWidth", type=FloatType)
krendering_KPointPlacementData_minHeight: Property = Property(name="minHeight", type=FloatType)
krendering_KPointPlacementData.attributes={krendering_KPointPlacementData_verticalAlignment, krendering_KPointPlacementData_horizontalMargin, krendering_KPointPlacementData_verticalMargin, krendering_KPointPlacementData_minWidth, krendering_KPointPlacementData_minHeight, krendering_KPointPlacementData_horizontalAlignment}

# krendering_KTextUnderline class attributes and methods
krendering_KTextUnderline_underline: Property = Property(name="underline", type=StringType)
krendering_KTextUnderline.attributes={krendering_KTextUnderline_underline}

# krendering_KInvisibility class attributes and methods
krendering_KInvisibility_invisible: Property = Property(name="invisible", type=BooleanType)
krendering_KInvisibility.attributes={krendering_KInvisibility_invisible}

# krendering_KShadow class attributes and methods
krendering_KShadow_xOffset: Property = Property(name="xOffset", type=FloatType)
krendering_KShadow_yOffset: Property = Property(name="yOffset", type=FloatType)
krendering_KShadow_blur: Property = Property(name="blur", type=FloatType)
krendering_KShadow.attributes={krendering_KShadow_yOffset, krendering_KShadow_blur, krendering_KShadow_xOffset}

# krendering_KTextStrikeout class attributes and methods
krendering_KTextStrikeout_struckOut: Property = Property(name="struckOut", type=StringType)
krendering_KTextStrikeout.attributes={krendering_KTextStrikeout_struckOut}

# krendering_KStyleRef class attributes and methods
krendering_KStyleRef_referencedTypes: Property = Property(name="referencedTypes", type=StringType)
krendering_KStyleRef.attributes={krendering_KStyleRef_referencedTypes}

# krendering_KLineJoin class attributes and methods
krendering_KLineJoin_lineJoin: Property = Property(name="lineJoin", type=StringType)
krendering_KLineJoin_miterLimit: Property = Property(name="miterLimit", type=FloatType)
krendering_KLineJoin.attributes={krendering_KLineJoin_lineJoin, krendering_KLineJoin_miterLimit}

# Relationships
parent0: BinaryAssociation = BinaryAssociation(
    name="parent0",
    ends={
        Property(name="KContainerRendering", type=krendering_KRendering, multiplicity=Multiplicity(1, 1)),
        Property(name="children", type=krendering_KContainerRendering, multiplicity=Multiplicity(0, 1))
    }
)
placementData1: BinaryAssociation = BinaryAssociation(
    name="placementData1",
    ends={
        Property(name="krendering_KPlacementData", type=krendering_KRendering, multiplicity=Multiplicity(1, 1)),
        Property(name="krendering_KRendering", type=krendering_KPlacementData, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
actions2: BinaryAssociation = BinaryAssociation(
    name="actions2",
    ends={
        Property(name="krendering_KAction", type=krendering_KRendering, multiplicity=Multiplicity(1, 1)),
        Property(name="krendering_KRendering3", type=krendering_KAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
points4: BinaryAssociation = BinaryAssociation(
    name="points4",
    ends={
        Property(name="krendering_KPosition", type=krendering_KPolyline, multiplicity=Multiplicity(1, 1)),
        Property(name="krendering_KPolyline", type=krendering_KPosition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
junctionPointRendering5: BinaryAssociation = BinaryAssociation(
    name="junctionPointRendering5",
    ends={
        Property(name="krendering_KRendering7", type=krendering_KPolyline, multiplicity=Multiplicity(1, 1)),
        Property(name="krendering_KPolyline6", type=krendering_KRendering, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
clipShape8: BinaryAssociation = BinaryAssociation(
    name="clipShape8",
    ends={
        Property(name="krendering_KRendering9", type=krendering_KImage, multiplicity=Multiplicity(1, 1)),
        Property(name="krendering_KImage", type=krendering_KRendering, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
childPlacement11: BinaryAssociation = BinaryAssociation(
    name="childPlacement11",
    ends={
        Property(name="krendering_KPlacement", type=krendering_KContainerRendering, multiplicity=Multiplicity(1, 1)),
        Property(name="krendering_KContainerRendering", type=krendering_KPlacement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
children10: BinaryAssociation = BinaryAssociation(
    name="children10",
    ends={
        Property(name="KRendering", type=krendering_KContainerRendering, multiplicity=Multiplicity(1, 1)),
        Property(name="parent", type=krendering_KRendering, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rendering13: BinaryAssociation = BinaryAssociation(
    name="rendering13",
    ends={
        Property(name="krendering_KRendering14", type=krendering_KRenderingRef, multiplicity=Multiplicity(1, 1)),
        Property(name="krendering_KRenderingRef", type=krendering_KRendering, multiplicity=Multiplicity(1, 1))
    }
)
renderings12: BinaryAssociation = BinaryAssociation(
    name="renderings12",
    ends={
        Property(name="krendering_KStyleHolder", type=krendering_KRenderingLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="krendering_KRenderingLibrary", type=krendering_KStyleHolder, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
topLeft15: BinaryAssociation = BinaryAssociation(
    name="topLeft15",
    ends={
        Property(name="krendering_KPosition16", type=krendering_KGridPlacement, multiplicity=Multiplicity(1, 1)),
        Property(name="krendering_KGridPlacement", type=krendering_KPosition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
bottomRight17: BinaryAssociation = BinaryAssociation(
    name="bottomRight17",
    ends={
        Property(name="krendering_KPosition19", type=krendering_KGridPlacement, multiplicity=Multiplicity(1, 1)),
        Property(name="krendering_KGridPlacement18", type=krendering_KPosition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
bottomRight22: BinaryAssociation = BinaryAssociation(
    name="bottomRight22",
    ends={
        Property(name="krendering_KPosition24", type=krendering_KAreaPlacementData, multiplicity=Multiplicity(1, 1)),
        Property(name="krendering_KAreaPlacementData23", type=krendering_KPosition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
topLeft20: BinaryAssociation = BinaryAssociation(
    name="topLeft20",
    ends={
        Property(name="krendering_KPosition21", type=krendering_KAreaPlacementData, multiplicity=Multiplicity(1, 1)),
        Property(name="krendering_KAreaPlacementData", type=krendering_KPosition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
targetColor26: BinaryAssociation = BinaryAssociation(
    name="targetColor26",
    ends={
        Property(name="krendering_KColor28", type=krendering_KColoring, multiplicity=Multiplicity(1, 1)),
        Property(name="krendering_KColoring27", type=krendering_KColor, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
color25: BinaryAssociation = BinaryAssociation(
    name="color25",
    ends={
        Property(name="krendering_KColor", type=krendering_KColoring, multiplicity=Multiplicity(1, 1)),
        Property(name="krendering_KColoring", type=krendering_KColor, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rotationAnchor29: BinaryAssociation = BinaryAssociation(
    name="rotationAnchor29",
    ends={
        Property(name="krendering_KPosition30", type=krendering_KRotation, multiplicity=Multiplicity(1, 1)),
        Property(name="krendering_KRotation", type=krendering_KPosition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
referencePoint31: BinaryAssociation = BinaryAssociation(
    name="referencePoint31",
    ends={
        Property(name="krendering_KPosition32", type=krendering_KPointPlacementData, multiplicity=Multiplicity(1, 1)),
        Property(name="krendering_KPointPlacementData", type=krendering_KPosition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
styles33: BinaryAssociation = BinaryAssociation(
    name="styles33",
    ends={
        Property(name="krendering_KStyle", type=krendering_KStyleHolder, multiplicity=Multiplicity(1, 1)),
        Property(name="krendering_KStyleHolder34", type=krendering_KStyle, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
color35: BinaryAssociation = BinaryAssociation(
    name="color35",
    ends={
        Property(name="krendering_KColor36", type=krendering_KShadow, multiplicity=Multiplicity(1, 1)),
        Property(name="krendering_KShadow", type=krendering_KColor, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
color37: BinaryAssociation = BinaryAssociation(
    name="color37",
    ends={
        Property(name="krendering_KColor38", type=krendering_KTextUnderline, multiplicity=Multiplicity(1, 1)),
        Property(name="krendering_KTextUnderline", type=krendering_KColor, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
color41: BinaryAssociation = BinaryAssociation(
    name="color41",
    ends={
        Property(name="krendering_KColor42", type=krendering_KTextStrikeout, multiplicity=Multiplicity(1, 1)),
        Property(name="krendering_KTextStrikeout", type=krendering_KColor, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
styleHolder39: BinaryAssociation = BinaryAssociation(
    name="styleHolder39",
    ends={
        Property(name="krendering_KStyleHolder40", type=krendering_KStyleRef, multiplicity=Multiplicity(1, 1)),
        Property(name="krendering_KStyleRef", type=krendering_KStyleHolder, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_krendering_KRendering_KGraphData = Generalization(general=KGraphData, specific=krendering_KRendering)
gen_krendering_KRendering_KStyleHolder = Generalization(general=KStyleHolder, specific=krendering_KRendering)
gen_krendering_KEllipse_KContainerRendering = Generalization(general=KContainerRendering, specific=krendering_KEllipse)
gen_krendering_KPolyline_KContainerRendering = Generalization(general=KContainerRendering, specific=krendering_KPolyline)
gen_krendering_KPolygon_KPolyline = Generalization(general=KPolyline, specific=krendering_KPolygon)
gen_krendering_KImage_KContainerRendering = Generalization(general=KContainerRendering, specific=krendering_KImage)
gen_krendering_KRectangle_KContainerRendering = Generalization(general=KContainerRendering, specific=krendering_KRectangle)
gen_krendering_KRoundedRectangle_KContainerRendering = Generalization(general=KContainerRendering, specific=krendering_KRoundedRectangle)
gen_krendering_KDecoratorPlacementData_KPlacementData = Generalization(general=KPlacementData, specific=krendering_KDecoratorPlacementData)
gen_krendering_KArc_KContainerRendering = Generalization(general=KContainerRendering, specific=krendering_KArc)
gen_krendering_KStyle_EMapPropertyHolder = Generalization(general=EMapPropertyHolder, specific=krendering_KStyle)
gen_krendering_KContainerRendering_KRendering = Generalization(general=KRendering, specific=krendering_KContainerRendering)
gen_krendering_KRenderingRef_KRendering = Generalization(general=KRendering, specific=krendering_KRenderingRef)
gen_krendering_KChildArea_KRendering = Generalization(general=KRendering, specific=krendering_KChildArea)
gen_krendering_KText_KRendering = Generalization(general=KRendering, specific=krendering_KText)
gen_krendering_KRenderingLibrary_KGraphData = Generalization(general=KGraphData, specific=krendering_KRenderingLibrary)
gen_krendering_KGridPlacementData_KAreaPlacementData = Generalization(general=KAreaPlacementData, specific=krendering_KGridPlacementData)
gen_krendering_KGridPlacement_KPlacement = Generalization(general=KPlacement, specific=krendering_KGridPlacement)
gen_krendering_KCustomRendering_KContainerRendering = Generalization(general=KContainerRendering, specific=krendering_KCustomRendering)
gen_krendering_KAreaPlacementData_KPlacementData = Generalization(general=KPlacementData, specific=krendering_KAreaPlacementData)
gen_krendering_KLineWidth_KStyle = Generalization(general=KStyle, specific=krendering_KLineWidth)
gen_krendering_KLineStyle_KStyle = Generalization(general=KStyle, specific=krendering_KLineStyle)
gen_krendering_KVerticalAlignment_KStyle = Generalization(general=KStyle, specific=krendering_KVerticalAlignment)
gen_krendering_KHorizontalAlignment_KStyle = Generalization(general=KStyle, specific=krendering_KHorizontalAlignment)
gen_krendering_KSpline_KPolyline = Generalization(general=KPolyline, specific=krendering_KSpline)
gen_krendering_KColoring_KStyle = Generalization(general=KStyle, specific=krendering_KColoring)
gen_krendering_KFontName_KStyle = Generalization(general=KStyle, specific=krendering_KFontName)
gen_krendering_KFontSize_KStyle = Generalization(general=KStyle, specific=krendering_KFontSize)
gen_krendering_KRoundedBendsPolyline_KPolyline = Generalization(general=KPolyline, specific=krendering_KRoundedBendsPolyline)
gen_krendering_KFontBold_KStyle = Generalization(general=KStyle, specific=krendering_KFontBold)
gen_krendering_KFontItalic_KStyle = Generalization(general=KStyle, specific=krendering_KFontItalic)
gen_krendering_KLineCap_KStyle = Generalization(general=KStyle, specific=krendering_KLineCap)
gen_krendering_KRotation_KStyle = Generalization(general=KStyle, specific=krendering_KRotation)
gen_krendering_KPointPlacementData_KPlacementData = Generalization(general=KPlacementData, specific=krendering_KPointPlacementData)
gen_krendering_KTextUnderline_KStyle = Generalization(general=KStyle, specific=krendering_KTextUnderline)
gen_krendering_KInvisibility_KStyle = Generalization(general=KStyle, specific=krendering_KInvisibility)
gen_krendering_KShadow_KStyle = Generalization(general=KStyle, specific=krendering_KShadow)
gen_krendering_KTextStrikeout_KStyle = Generalization(general=KStyle, specific=krendering_KTextStrikeout)
gen_krendering_KStyleRef_KStyle = Generalization(general=KStyle, specific=krendering_KStyleRef)
gen_krendering_KLineJoin_KStyle = Generalization(general=KStyle, specific=krendering_KLineJoin)

# Domain Model
domain_model = DomainModel(
    name="krendering",
    types={krendering_KPosition, krendering_KRendering, KGraphData, KStyleHolder, krendering_KContainerRendering, krendering_KPlacementData, krendering_KAction, krendering_KEllipse, KContainerRendering, krendering_KPolyline, krendering_KPolygon, KPolyline, krendering_KImage, krendering_KRectangle, krendering_KRoundedRectangle, krendering_KDecoratorPlacementData, KPlacementData, krendering_KPlacement, krendering_KArc, krendering_KStyle, EMapPropertyHolder, KRendering, krendering_KRenderingRef, krendering_KChildArea, krendering_KText, krendering_KRenderingLibrary, krendering_KStyleHolder, krendering_KGridPlacementData, KAreaPlacementData, krendering_KGridPlacement, KPlacement, krendering_KCustomRendering, krendering_KColor, krendering_KAreaPlacementData, krendering_KLineWidth, KStyle, krendering_KLineStyle, krendering_KXPosition, krendering_KVerticalAlignment, krendering_KHorizontalAlignment, krendering_KYPosition, krendering_KLeftPosition, krendering_KTopPosition, krendering_KBottomPosition, krendering_KSpline, krendering_KForeground, krendering_KRightPosition, krendering_KColoring, krendering_KBackground, krendering_KFontName, krendering_KFontSize, krendering_KRoundedBendsPolyline, krendering_KFontBold, krendering_KFontItalic, krendering_KLineCap, krendering_KRotation, krendering_KPointPlacementData, krendering_KTextUnderline, krendering_KInvisibility, krendering_KShadow, krendering_KTextStrikeout, krendering_KStyleRef, krendering_KLineJoin, LineStyle, HorizontalAlignment, VerticalAlignment, LineCap, ModifierState, Trigger, LineJoin, Underline, Arc},
    associations={parent0, placementData1, actions2, points4, junctionPointRendering5, clipShape8, childPlacement11, children10, rendering13, renderings12, topLeft15, bottomRight17, bottomRight22, topLeft20, targetColor26, color25, rotationAnchor29, referencePoint31, styles33, color35, color37, color41, styleHolder39},
    generalizations={gen_krendering_KRendering_KGraphData, gen_krendering_KRendering_KStyleHolder, gen_krendering_KEllipse_KContainerRendering, gen_krendering_KPolyline_KContainerRendering, gen_krendering_KPolygon_KPolyline, gen_krendering_KImage_KContainerRendering, gen_krendering_KRectangle_KContainerRendering, gen_krendering_KRoundedRectangle_KContainerRendering, gen_krendering_KDecoratorPlacementData_KPlacementData, gen_krendering_KArc_KContainerRendering, gen_krendering_KStyle_EMapPropertyHolder, gen_krendering_KContainerRendering_KRendering, gen_krendering_KRenderingRef_KRendering, gen_krendering_KChildArea_KRendering, gen_krendering_KText_KRendering, gen_krendering_KRenderingLibrary_KGraphData, gen_krendering_KGridPlacementData_KAreaPlacementData, gen_krendering_KGridPlacement_KPlacement, gen_krendering_KCustomRendering_KContainerRendering, gen_krendering_KAreaPlacementData_KPlacementData, gen_krendering_KLineWidth_KStyle, gen_krendering_KLineStyle_KStyle, gen_krendering_KVerticalAlignment_KStyle, gen_krendering_KHorizontalAlignment_KStyle, gen_krendering_KSpline_KPolyline, gen_krendering_KColoring_KStyle, gen_krendering_KFontName_KStyle, gen_krendering_KFontSize_KStyle, gen_krendering_KRoundedBendsPolyline_KPolyline, gen_krendering_KFontBold_KStyle, gen_krendering_KFontItalic_KStyle, gen_krendering_KLineCap_KStyle, gen_krendering_KRotation_KStyle, gen_krendering_KPointPlacementData_KPlacementData, gen_krendering_KTextUnderline_KStyle, gen_krendering_KInvisibility_KStyle, gen_krendering_KShadow_KStyle, gen_krendering_KTextStrikeout_KStyle, gen_krendering_KStyleRef_KStyle, gen_krendering_KLineJoin_KStyle},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)