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
ActionType: Enumeration = Enumeration(
    name="ActionType",
    literals={
            EnumerationLiteral(name="previousPage"),
			EnumerationLiteral(name="nextPage"),
			EnumerationLiteral(name="firstPage"),
			EnumerationLiteral(name="lastPage"),
			EnumerationLiteral(name="hide"),
			EnumerationLiteral(name="stop"),
			EnumerationLiteral(name="execute"),
			EnumerationLiteral(name="show"),
			EnumerationLiteral(name="verb"),
			EnumerationLiteral(name="fadeOut"),
			EnumerationLiteral(name="sound"),
			EnumerationLiteral(name="none")
    }
)

AnimationsType: Enumeration = Enumeration(
    name="AnimationsType",
    literals={
            EnumerationLiteral(name="enabled"),
			EnumerationLiteral(name="disabled")
    }
)

NodeTypeType: Enumeration = Enumeration(
    name="NodeTypeType",
    literals={
            EnumerationLiteral(name="default"),
			EnumerationLiteral(name="onClick"),
			EnumerationLiteral(name="withPrevious"),
			EnumerationLiteral(name="afterPrevious"),
			EnumerationLiteral(name="timingRoot"),
			EnumerationLiteral(name="mainSequence"),
			EnumerationLiteral(name="interactiveSequence")
    }
)

PresetClassType: Enumeration = Enumeration(
    name="PresetClassType",
    literals={
            EnumerationLiteral(name="custom"),
			EnumerationLiteral(name="entrance"),
			EnumerationLiteral(name="exit"),
			EnumerationLiteral(name="emphasis"),
			EnumerationLiteral(name="motionPath"),
			EnumerationLiteral(name="oleAction"),
			EnumerationLiteral(name="mediaCall")
    }
)

SourceType: Enumeration = Enumeration(
    name="SourceType",
    literals={
            EnumerationLiteral(name="fixed"),
			EnumerationLiteral(name="currentDate")
    }
)

TransitionOnClickType: Enumeration = Enumeration(
    name="TransitionOnClickType",
    literals={
            EnumerationLiteral(name="enabled"),
			EnumerationLiteral(name="disabled")
    }
)

TransitionStyleType: Enumeration = Enumeration(
    name="TransitionStyleType",
    literals={
            EnumerationLiteral(name="none"),
			EnumerationLiteral(name="fadeFromLeft"),
			EnumerationLiteral(name="fadeFromTop"),
			EnumerationLiteral(name="fadeFromRight"),
			EnumerationLiteral(name="fadeFromBottom"),
			EnumerationLiteral(name="fadeFromUpperleft"),
			EnumerationLiteral(name="fadeFromCenter"),
			EnumerationLiteral(name="verticalStripes"),
			EnumerationLiteral(name="horizontalStripes"),
			EnumerationLiteral(name="clockwise"),
			EnumerationLiteral(name="counterclockwise"),
			EnumerationLiteral(name="openVertical"),
			EnumerationLiteral(name="openHorizontal"),
			EnumerationLiteral(name="closeVertical"),
			EnumerationLiteral(name="closeHorizontal"),
			EnumerationLiteral(name="wavylineFromLeft"),
			EnumerationLiteral(name="wavylineFromTop"),
			EnumerationLiteral(name="wavylineFromRight"),
			EnumerationLiteral(name="wavylineFromBottom"),
			EnumerationLiteral(name="spiralinLeft"),
			EnumerationLiteral(name="spiralinRight"),
			EnumerationLiteral(name="spiraloutLeft"),
			EnumerationLiteral(name="spiraloutRight"),
			EnumerationLiteral(name="rollFromTop"),
			EnumerationLiteral(name="rollFromLeft"),
			EnumerationLiteral(name="rollFromRight"),
			EnumerationLiteral(name="rollFromBottom"),
			EnumerationLiteral(name="stretchFromLeft"),
			EnumerationLiteral(name="stretchFromTop"),
			EnumerationLiteral(name="stretchFromRight"),
			EnumerationLiteral(name="stretchFromBottom"),
			EnumerationLiteral(name="verticalLines"),
			EnumerationLiteral(name="horizontalLines"),
			EnumerationLiteral(name="dissolve"),
			EnumerationLiteral(name="random"),
			EnumerationLiteral(name="verticalCheckerboard"),
			EnumerationLiteral(name="fadeFromUpperright"),
			EnumerationLiteral(name="fadeFromLowerleft"),
			EnumerationLiteral(name="fadeFromLowerright"),
			EnumerationLiteral(name="moveFromLeft"),
			EnumerationLiteral(name="moveFromTop"),
			EnumerationLiteral(name="moveFromRight"),
			EnumerationLiteral(name="moveFromBottom"),
			EnumerationLiteral(name="moveFromUpperleft"),
			EnumerationLiteral(name="moveFromUpperright"),
			EnumerationLiteral(name="moveFromLowerleft"),
			EnumerationLiteral(name="moveFromLowerright"),
			EnumerationLiteral(name="uncoverToLeft"),
			EnumerationLiteral(name="uncoverToTop"),
			EnumerationLiteral(name="uncoverToRight"),
			EnumerationLiteral(name="uncoverToBottom"),
			EnumerationLiteral(name="uncoverToUpperleft"),
			EnumerationLiteral(name="uncoverToUpperright"),
			EnumerationLiteral(name="uncoverToLowerleft"),
			EnumerationLiteral(name="uncoverToLowerright"),
			EnumerationLiteral(name="fadeToCenter"),
			EnumerationLiteral(name="horizontalCheckerboard"),
			EnumerationLiteral(name="interlockingHorizontalLeft"),
			EnumerationLiteral(name="interlockingHorizontalRight"),
			EnumerationLiteral(name="interlockingVerticalTop"),
			EnumerationLiteral(name="interlockingVerticalBottom"),
			EnumerationLiteral(name="flyAway"),
			EnumerationLiteral(name="open"),
			EnumerationLiteral(name="close"),
			EnumerationLiteral(name="melt")
    }
)

VisibilityType: Enumeration = Enumeration(
    name="VisibilityType",
    literals={
            EnumerationLiteral(name="visible"),
			EnumerationLiteral(name="hidden")
    }
)

TransitionTypeType: Enumeration = Enumeration(
    name="TransitionTypeType",
    literals={
            EnumerationLiteral(name="semiAutomatic"),
			EnumerationLiteral(name="manual"),
			EnumerationLiteral(name="automatic")
    }
)

# Classes
presentation_AnimationGroupType = Class(name="presentation_AnimationGroupType")
presentation_DateTimeDeclType = Class(name="presentation_DateTimeDeclType")
presentation_EObject = Class(name="presentation_EObject")
presentation_AnimationsType1 = Class(name="presentation_AnimationsType1")
presentation_SoundType = Class(name="presentation_SoundType")
presentation_EventListenerType = Class(name="presentation_EventListenerType")
presentation_DateTimeType = Class(name="presentation_DateTimeType")
presentation_DimType = Class(name="presentation_DimType")
presentation_FooterType = Class(name="presentation_FooterType")
presentation_HeaderDeclType = Class(name="presentation_HeaderDeclType")
presentation_HeaderType = Class(name="presentation_HeaderType")
presentation_HideShapeType = Class(name="presentation_HideShapeType")
presentation_FooterDeclType = Class(name="presentation_FooterDeclType")
presentation_HideTextType = Class(name="presentation_HideTextType")
presentation_FormsType = Class(name="presentation_FormsType")
presentation_RectType = Class(name="presentation_RectType")
presentation_NotesType = Class(name="presentation_NotesType")
presentation_PolygonType = Class(name="presentation_PolygonType")
presentation_RegularPolygonType = Class(name="presentation_RegularPolygonType")
presentation_LineType = Class(name="presentation_LineType")
presentation_PolylineType = Class(name="presentation_PolylineType")
presentation_CircleType = Class(name="presentation_CircleType")
presentation_EllipseType = Class(name="presentation_EllipseType")
presentation_GType = Class(name="presentation_GType")
presentation_PathType = Class(name="presentation_PathType")
presentation_PageThumbnailType = Class(name="presentation_PageThumbnailType")
presentation_FrameType = Class(name="presentation_FrameType")
presentation_MeasureType = Class(name="presentation_MeasureType")
presentation_CaptionType = Class(name="presentation_CaptionType")
presentation_ConnectorType = Class(name="presentation_ConnectorType")
presentation_ControlType = Class(name="presentation_ControlType")
presentation_SceneType = Class(name="presentation_SceneType")
presentation_CustomShapeType = Class(name="presentation_CustomShapeType")
presentation_PlaceholderType = Class(name="presentation_PlaceholderType")
presentation_SettingsType = Class(name="presentation_SettingsType")
presentation_ShowType = Class(name="presentation_ShowType")
presentation_PlayType = Class(name="presentation_PlayType")
presentation_ShowShapeType = Class(name="presentation_ShowShapeType")
presentation_ShowTextType = Class(name="presentation_ShowTextType")
presentation_DocumentRoot = Class(name="presentation_DocumentRoot")
presentation_EStringToStringMapEntry = Class(name="presentation_EStringToStringMapEntry")

# presentation_AnimationGroupType class attributes and methods
presentation_AnimationGroupType_presentationAnimationElementsGroup: Property = Property(name="presentationAnimationElementsGroup", type=StringType)
presentation_AnimationGroupType.attributes={presentation_AnimationGroupType_presentationAnimationElementsGroup}

# presentation_DateTimeDeclType class attributes and methods
presentation_DateTimeDeclType_mixed: Property = Property(name="mixed", type=StringType)
presentation_DateTimeDeclType_dataStyleName: Property = Property(name="dataStyleName", type=StringType)
presentation_DateTimeDeclType_name: Property = Property(name="name", type=StringType)
presentation_DateTimeDeclType_source: Property = Property(name="source", type=StringType)
presentation_DateTimeDeclType.attributes={presentation_DateTimeDeclType_source, presentation_DateTimeDeclType_dataStyleName, presentation_DateTimeDeclType_name, presentation_DateTimeDeclType_mixed}

# presentation_EObject class attributes and methods

# presentation_AnimationsType1 class attributes and methods
presentation_AnimationsType1_group: Property = Property(name="group", type=StringType)
presentation_AnimationsType1_presentationAnimationElementsGroup: Property = Property(name="presentationAnimationElementsGroup", type=StringType)
presentation_AnimationsType1.attributes={presentation_AnimationsType1_presentationAnimationElementsGroup, presentation_AnimationsType1_group}

# presentation_SoundType class attributes and methods
presentation_SoundType_actuate: Property = Property(name="actuate", type=StringType)
presentation_SoundType_href: Property = Property(name="href", type=StringType)
presentation_SoundType_playFull: Property = Property(name="playFull", type=StringType)
presentation_SoundType_show: Property = Property(name="show", type=StringType)
presentation_SoundType_type: Property = Property(name="type", type=StringType)
presentation_SoundType.attributes={presentation_SoundType_playFull, presentation_SoundType_type, presentation_SoundType_actuate, presentation_SoundType_href, presentation_SoundType_show}

# presentation_EventListenerType class attributes and methods
presentation_EventListenerType_show: Property = Property(name="show", type=StringType)
presentation_EventListenerType_speed: Property = Property(name="speed", type=StringType)
presentation_EventListenerType_startScale: Property = Property(name="startScale", type=StringType)
presentation_EventListenerType_type: Property = Property(name="type", type=StringType)
presentation_EventListenerType_action: Property = Property(name="action", type=StringType)
presentation_EventListenerType_actuate: Property = Property(name="actuate", type=StringType)
presentation_EventListenerType_direction: Property = Property(name="direction", type=StringType)
presentation_EventListenerType_effect: Property = Property(name="effect", type=StringType)
presentation_EventListenerType_eventName: Property = Property(name="eventName", type=StringType)
presentation_EventListenerType_href: Property = Property(name="href", type=StringType)
presentation_EventListenerType_verb: Property = Property(name="verb", type=StringType)
presentation_EventListenerType.attributes={presentation_EventListenerType_speed, presentation_EventListenerType_show, presentation_EventListenerType_type, presentation_EventListenerType_href, presentation_EventListenerType_eventName, presentation_EventListenerType_verb, presentation_EventListenerType_effect, presentation_EventListenerType_actuate, presentation_EventListenerType_direction, presentation_EventListenerType_action, presentation_EventListenerType_startScale}

# presentation_DateTimeType class attributes and methods

# presentation_DimType class attributes and methods
presentation_DimType_color: Property = Property(name="color", type=StringType)
presentation_DimType_shapeId: Property = Property(name="shapeId", type=StringType)
presentation_DimType.attributes={presentation_DimType_color, presentation_DimType_shapeId}

# presentation_FooterType class attributes and methods

# presentation_HeaderDeclType class attributes and methods
presentation_HeaderDeclType_mixed: Property = Property(name="mixed", type=StringType)
presentation_HeaderDeclType_name: Property = Property(name="name", type=StringType)
presentation_HeaderDeclType.attributes={presentation_HeaderDeclType_mixed, presentation_HeaderDeclType_name}

# presentation_HeaderType class attributes and methods

# presentation_HideShapeType class attributes and methods
presentation_HideShapeType_speed: Property = Property(name="speed", type=StringType)
presentation_HideShapeType_startScale: Property = Property(name="startScale", type=StringType)
presentation_HideShapeType_delay: Property = Property(name="delay", type=StringType)
presentation_HideShapeType_direction: Property = Property(name="direction", type=StringType)
presentation_HideShapeType_effect: Property = Property(name="effect", type=StringType)
presentation_HideShapeType_pathId: Property = Property(name="pathId", type=StringType)
presentation_HideShapeType_shapeId: Property = Property(name="shapeId", type=StringType)
presentation_HideShapeType.attributes={presentation_HideShapeType_direction, presentation_HideShapeType_delay, presentation_HideShapeType_effect, presentation_HideShapeType_speed, presentation_HideShapeType_startScale, presentation_HideShapeType_pathId, presentation_HideShapeType_shapeId}

# presentation_FooterDeclType class attributes and methods
presentation_FooterDeclType_mixed: Property = Property(name="mixed", type=StringType)
presentation_FooterDeclType_name: Property = Property(name="name", type=StringType)
presentation_FooterDeclType.attributes={presentation_FooterDeclType_mixed, presentation_FooterDeclType_name}

# presentation_HideTextType class attributes and methods
presentation_HideTextType_pathId: Property = Property(name="pathId", type=StringType)
presentation_HideTextType_shapeId: Property = Property(name="shapeId", type=StringType)
presentation_HideTextType_delay: Property = Property(name="delay", type=StringType)
presentation_HideTextType_direction: Property = Property(name="direction", type=StringType)
presentation_HideTextType_effect: Property = Property(name="effect", type=StringType)
presentation_HideTextType_speed: Property = Property(name="speed", type=StringType)
presentation_HideTextType_startScale: Property = Property(name="startScale", type=StringType)
presentation_HideTextType.attributes={presentation_HideTextType_speed, presentation_HideTextType_direction, presentation_HideTextType_delay, presentation_HideTextType_pathId, presentation_HideTextType_startScale, presentation_HideTextType_effect, presentation_HideTextType_shapeId}

# presentation_FormsType class attributes and methods

# presentation_RectType class attributes and methods

# presentation_NotesType class attributes and methods
presentation_NotesType_shape: Property = Property(name="shape", type=StringType)
presentation_NotesType_pageLayoutName: Property = Property(name="pageLayoutName", type=StringType)
presentation_NotesType_styleName: Property = Property(name="styleName", type=StringType)
presentation_NotesType_useDateTimeName: Property = Property(name="useDateTimeName", type=StringType)
presentation_NotesType_useFooterName: Property = Property(name="useFooterName", type=StringType)
presentation_NotesType_useHeaderName: Property = Property(name="useHeaderName", type=StringType)
presentation_NotesType.attributes={presentation_NotesType_shape, presentation_NotesType_pageLayoutName, presentation_NotesType_styleName, presentation_NotesType_useDateTimeName, presentation_NotesType_useFooterName, presentation_NotesType_useHeaderName}

# presentation_PolygonType class attributes and methods

# presentation_RegularPolygonType class attributes and methods

# presentation_LineType class attributes and methods

# presentation_PolylineType class attributes and methods

# presentation_CircleType class attributes and methods

# presentation_EllipseType class attributes and methods

# presentation_GType class attributes and methods

# presentation_PathType class attributes and methods

# presentation_PageThumbnailType class attributes and methods

# presentation_FrameType class attributes and methods

# presentation_MeasureType class attributes and methods

# presentation_CaptionType class attributes and methods

# presentation_ConnectorType class attributes and methods

# presentation_ControlType class attributes and methods

# presentation_SceneType class attributes and methods

# presentation_CustomShapeType class attributes and methods

# presentation_PlaceholderType class attributes and methods
presentation_PlaceholderType_height: Property = Property(name="height", type=StringType)
presentation_PlaceholderType_object: Property = Property(name="object", type=StringType)
presentation_PlaceholderType_width: Property = Property(name="width", type=StringType)
presentation_PlaceholderType_x: Property = Property(name="x", type=StringType)
presentation_PlaceholderType_y: Property = Property(name="y", type=StringType)
presentation_PlaceholderType.attributes={presentation_PlaceholderType_height, presentation_PlaceholderType_object, presentation_PlaceholderType_width, presentation_PlaceholderType_y, presentation_PlaceholderType_x}

# presentation_SettingsType class attributes and methods
presentation_SettingsType_animations: Property = Property(name="animations", type=StringType)
presentation_SettingsType_endless: Property = Property(name="endless", type=StringType)
presentation_SettingsType_fullScreen: Property = Property(name="fullScreen", type=StringType)
presentation_SettingsType_mouseAsPen: Property = Property(name="mouseAsPen", type=StringType)
presentation_SettingsType_mouseVisible: Property = Property(name="mouseVisible", type=StringType)
presentation_SettingsType_pause: Property = Property(name="pause", type=StringType)
presentation_SettingsType_show1: Property = Property(name="show1", type=StringType)
presentation_SettingsType_showEndOfPresentationSlide: Property = Property(name="showEndOfPresentationSlide", type=StringType)
presentation_SettingsType_showLogo: Property = Property(name="showLogo", type=StringType)
presentation_SettingsType_startPage: Property = Property(name="startPage", type=StringType)
presentation_SettingsType_startWithNavigator: Property = Property(name="startWithNavigator", type=StringType)
presentation_SettingsType_stayOnTop: Property = Property(name="stayOnTop", type=StringType)
presentation_SettingsType_transitionOnClick: Property = Property(name="transitionOnClick", type=StringType)
presentation_SettingsType_forceManual: Property = Property(name="forceManual", type=StringType)
presentation_SettingsType.attributes={presentation_SettingsType_forceManual, presentation_SettingsType_showEndOfPresentationSlide, presentation_SettingsType_fullScreen, presentation_SettingsType_stayOnTop, presentation_SettingsType_mouseAsPen, presentation_SettingsType_startWithNavigator, presentation_SettingsType_animations, presentation_SettingsType_transitionOnClick, presentation_SettingsType_pause, presentation_SettingsType_startPage, presentation_SettingsType_endless, presentation_SettingsType_mouseVisible, presentation_SettingsType_showLogo, presentation_SettingsType_show1}

# presentation_ShowType class attributes and methods
presentation_ShowType_name: Property = Property(name="name", type=StringType)
presentation_ShowType_pages: Property = Property(name="pages", type=StringType)
presentation_ShowType.attributes={presentation_ShowType_name, presentation_ShowType_pages}

# presentation_PlayType class attributes and methods
presentation_PlayType_shapeId: Property = Property(name="shapeId", type=StringType)
presentation_PlayType_speed: Property = Property(name="speed", type=StringType)
presentation_PlayType.attributes={presentation_PlayType_shapeId, presentation_PlayType_speed}

# presentation_ShowShapeType class attributes and methods
presentation_ShowShapeType_delay: Property = Property(name="delay", type=StringType)
presentation_ShowShapeType_direction: Property = Property(name="direction", type=StringType)
presentation_ShowShapeType_effect: Property = Property(name="effect", type=StringType)
presentation_ShowShapeType_pathId: Property = Property(name="pathId", type=StringType)
presentation_ShowShapeType_shapeId: Property = Property(name="shapeId", type=StringType)
presentation_ShowShapeType_speed: Property = Property(name="speed", type=StringType)
presentation_ShowShapeType_startScale: Property = Property(name="startScale", type=StringType)
presentation_ShowShapeType.attributes={presentation_ShowShapeType_effect, presentation_ShowShapeType_direction, presentation_ShowShapeType_pathId, presentation_ShowShapeType_startScale, presentation_ShowShapeType_speed, presentation_ShowShapeType_delay, presentation_ShowShapeType_shapeId}

# presentation_ShowTextType class attributes and methods
presentation_ShowTextType_delay: Property = Property(name="delay", type=StringType)
presentation_ShowTextType_direction: Property = Property(name="direction", type=StringType)
presentation_ShowTextType_effect: Property = Property(name="effect", type=StringType)
presentation_ShowTextType_pathId: Property = Property(name="pathId", type=StringType)
presentation_ShowTextType_shapeId: Property = Property(name="shapeId", type=StringType)
presentation_ShowTextType_speed: Property = Property(name="speed", type=StringType)
presentation_ShowTextType_startScale: Property = Property(name="startScale", type=StringType)
presentation_ShowTextType.attributes={presentation_ShowTextType_pathId, presentation_ShowTextType_shapeId, presentation_ShowTextType_delay, presentation_ShowTextType_effect, presentation_ShowTextType_startScale, presentation_ShowTextType_speed, presentation_ShowTextType_direction}

# presentation_DocumentRoot class attributes and methods
presentation_DocumentRoot_mixed: Property = Property(name="mixed", type=StringType)
presentation_DocumentRoot_action: Property = Property(name="action", type=StringType)
presentation_DocumentRoot_animations1: Property = Property(name="animations1", type=StringType)
presentation_DocumentRoot_backgroundVisible: Property = Property(name="backgroundVisible", type=StringType)
presentation_DocumentRoot_class_: Property = Property(name="class_", type=StringType)
presentation_DocumentRoot_classNames: Property = Property(name="classNames", type=StringType)
presentation_DocumentRoot_delay: Property = Property(name="delay", type=StringType)
presentation_DocumentRoot_direction: Property = Property(name="direction", type=StringType)
presentation_DocumentRoot_displayDateTime: Property = Property(name="displayDateTime", type=StringType)
presentation_DocumentRoot_displayFooter: Property = Property(name="displayFooter", type=StringType)
presentation_DocumentRoot_displayHeader: Property = Property(name="displayHeader", type=StringType)
presentation_DocumentRoot_displayPageNumber: Property = Property(name="displayPageNumber", type=StringType)
presentation_DocumentRoot_duration: Property = Property(name="duration", type=StringType)
presentation_DocumentRoot_effect: Property = Property(name="effect", type=StringType)
presentation_DocumentRoot_backgroundObjectsVisible: Property = Property(name="backgroundObjectsVisible", type=StringType)
presentation_DocumentRoot_pathId: Property = Property(name="pathId", type=StringType)
presentation_DocumentRoot_endless: Property = Property(name="endless", type=StringType)
presentation_DocumentRoot_pause: Property = Property(name="pause", type=StringType)
presentation_DocumentRoot_forceManual: Property = Property(name="forceManual", type=StringType)
presentation_DocumentRoot_placeholder1: Property = Property(name="placeholder1", type=StringType)
presentation_DocumentRoot_fullScreen: Property = Property(name="fullScreen", type=StringType)
presentation_DocumentRoot_groupId: Property = Property(name="groupId", type=StringType)
presentation_DocumentRoot_masterElement: Property = Property(name="masterElement", type=StringType)
presentation_DocumentRoot_mouseAsPen: Property = Property(name="mouseAsPen", type=StringType)
presentation_DocumentRoot_mouseVisible: Property = Property(name="mouseVisible", type=StringType)
presentation_DocumentRoot_name: Property = Property(name="name", type=StringType)
presentation_DocumentRoot_nodeType: Property = Property(name="nodeType", type=StringType)
presentation_DocumentRoot_pages: Property = Property(name="pages", type=StringType)
presentation_DocumentRoot_source: Property = Property(name="source", type=StringType)
presentation_DocumentRoot_speed: Property = Property(name="speed", type=StringType)
presentation_DocumentRoot_playFull: Property = Property(name="playFull", type=StringType)
presentation_DocumentRoot_startPage: Property = Property(name="startPage", type=StringType)
presentation_DocumentRoot_presentationPageLayoutName: Property = Property(name="presentationPageLayoutName", type=StringType)
presentation_DocumentRoot_presetClass: Property = Property(name="presetClass", type=StringType)
presentation_DocumentRoot_startScale: Property = Property(name="startScale", type=StringType)
presentation_DocumentRoot_presetId: Property = Property(name="presetId", type=StringType)
presentation_DocumentRoot_presetSubType: Property = Property(name="presetSubType", type=StringType)
presentation_DocumentRoot_show1: Property = Property(name="show1", type=StringType)
presentation_DocumentRoot_showEndOfPresentationSlide: Property = Property(name="showEndOfPresentationSlide", type=StringType)
presentation_DocumentRoot_showLogo: Property = Property(name="showLogo", type=StringType)
presentation_DocumentRoot_styleName: Property = Property(name="styleName", type=StringType)
presentation_DocumentRoot_transitionOnClick: Property = Property(name="transitionOnClick", type=StringType)
presentation_DocumentRoot_transitionSpeed: Property = Property(name="transitionSpeed", type=StringType)
presentation_DocumentRoot_transitionStyle: Property = Property(name="transitionStyle", type=StringType)
presentation_DocumentRoot_transitionType: Property = Property(name="transitionType", type=StringType)
presentation_DocumentRoot_useDateTimeName: Property = Property(name="useDateTimeName", type=StringType)
presentation_DocumentRoot_startWithNavigator: Property = Property(name="startWithNavigator", type=StringType)
presentation_DocumentRoot_stayOnTop: Property = Property(name="stayOnTop", type=StringType)
presentation_DocumentRoot_useFooterName: Property = Property(name="useFooterName", type=StringType)
presentation_DocumentRoot_userTransformed: Property = Property(name="userTransformed", type=StringType)
presentation_DocumentRoot_verb: Property = Property(name="verb", type=StringType)
presentation_DocumentRoot_visibility: Property = Property(name="visibility", type=StringType)
presentation_DocumentRoot_useHeaderName: Property = Property(name="useHeaderName", type=StringType)
presentation_DocumentRoot.attributes={presentation_DocumentRoot_direction, presentation_DocumentRoot_playFull, presentation_DocumentRoot_presetId, presentation_DocumentRoot_action, presentation_DocumentRoot_pages, presentation_DocumentRoot_mouseAsPen, presentation_DocumentRoot_presetSubType, presentation_DocumentRoot_show1, presentation_DocumentRoot_showLogo, presentation_DocumentRoot_transitionStyle, presentation_DocumentRoot_styleName, presentation_DocumentRoot_duration, presentation_DocumentRoot_groupId, presentation_DocumentRoot_presentationPageLayoutName, presentation_DocumentRoot_verb, presentation_DocumentRoot_classNames, presentation_DocumentRoot_nodeType, presentation_DocumentRoot_stayOnTop, presentation_DocumentRoot_source, presentation_DocumentRoot_presetClass, presentation_DocumentRoot_userTransformed, presentation_DocumentRoot_backgroundObjectsVisible, presentation_DocumentRoot_fullScreen, presentation_DocumentRoot_visibility, presentation_DocumentRoot_name, presentation_DocumentRoot_class_, presentation_DocumentRoot_displayHeader, presentation_DocumentRoot_speed, presentation_DocumentRoot_displayDateTime, presentation_DocumentRoot_placeholder1, presentation_DocumentRoot_startPage, presentation_DocumentRoot_startWithNavigator, presentation_DocumentRoot_useDateTimeName, presentation_DocumentRoot_endless, presentation_DocumentRoot_useFooterName, presentation_DocumentRoot_mouseVisible, presentation_DocumentRoot_pathId, presentation_DocumentRoot_transitionOnClick, presentation_DocumentRoot_pause, presentation_DocumentRoot_displayPageNumber, presentation_DocumentRoot_useHeaderName, presentation_DocumentRoot_animations1, presentation_DocumentRoot_startScale, presentation_DocumentRoot_showEndOfPresentationSlide, presentation_DocumentRoot_masterElement, presentation_DocumentRoot_delay, presentation_DocumentRoot_displayFooter, presentation_DocumentRoot_transitionType, presentation_DocumentRoot_mixed, presentation_DocumentRoot_transitionSpeed, presentation_DocumentRoot_effect, presentation_DocumentRoot_backgroundVisible, presentation_DocumentRoot_forceManual}

# presentation_EStringToStringMapEntry class attributes and methods

# Relationships
presentationAnimationElements1: BinaryAssociation = BinaryAssociation(
    name="presentationAnimationElements1",
    ends={
        Property(name="presentation_EObject2", type=presentation_AnimationsType1, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_AnimationsType1", type=presentation_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
animationGroup3: BinaryAssociation = BinaryAssociation(
    name="animationGroup3",
    ends={
        Property(name="presentation_AnimationGroupType5", type=presentation_AnimationsType1, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_AnimationsType14", type=presentation_AnimationGroupType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
presentationAnimationElements0: BinaryAssociation = BinaryAssociation(
    name="presentationAnimationElements0",
    ends={
        Property(name="presentation_EObject", type=presentation_AnimationGroupType, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_AnimationGroupType", type=presentation_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sound6: BinaryAssociation = BinaryAssociation(
    name="sound6",
    ends={
        Property(name="presentation_SoundType", type=presentation_DimType, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_DimType", type=presentation_SoundType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sound7: BinaryAssociation = BinaryAssociation(
    name="sound7",
    ends={
        Property(name="presentation_SoundType8", type=presentation_EventListenerType, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_EventListenerType", type=presentation_SoundType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sound9: BinaryAssociation = BinaryAssociation(
    name="sound9",
    ends={
        Property(name="presentation_SoundType10", type=presentation_HideShapeType, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_HideShapeType", type=presentation_SoundType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sound11: BinaryAssociation = BinaryAssociation(
    name="sound11",
    ends={
        Property(name="presentation_SoundType12", type=presentation_HideTextType, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_HideTextType", type=presentation_SoundType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
forms13: BinaryAssociation = BinaryAssociation(
    name="forms13",
    ends={
        Property(name="presentation_FormsType", type=presentation_NotesType, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_NotesType", type=presentation_FormsType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rect14: BinaryAssociation = BinaryAssociation(
    name="rect14",
    ends={
        Property(name="presentation_RectType", type=presentation_NotesType, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_NotesType15", type=presentation_RectType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
polygon20: BinaryAssociation = BinaryAssociation(
    name="polygon20",
    ends={
        Property(name="presentation_PolygonType", type=presentation_NotesType, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_NotesType21", type=presentation_PolygonType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
regularPolygon22: BinaryAssociation = BinaryAssociation(
    name="regularPolygon22",
    ends={
        Property(name="presentation_RegularPolygonType", type=presentation_NotesType, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_NotesType23", type=presentation_RegularPolygonType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
line16: BinaryAssociation = BinaryAssociation(
    name="line16",
    ends={
        Property(name="presentation_LineType", type=presentation_NotesType, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_NotesType17", type=presentation_LineType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
polyline18: BinaryAssociation = BinaryAssociation(
    name="polyline18",
    ends={
        Property(name="presentation_PolylineType", type=presentation_NotesType, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_NotesType19", type=presentation_PolylineType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
circle26: BinaryAssociation = BinaryAssociation(
    name="circle26",
    ends={
        Property(name="presentation_CircleType", type=presentation_NotesType, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_NotesType27", type=presentation_CircleType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ellipse28: BinaryAssociation = BinaryAssociation(
    name="ellipse28",
    ends={
        Property(name="presentation_EllipseType", type=presentation_NotesType, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_NotesType29", type=presentation_EllipseType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
g30: BinaryAssociation = BinaryAssociation(
    name="g30",
    ends={
        Property(name="presentation_GType", type=presentation_NotesType, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_NotesType31", type=presentation_GType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pageThumbnail32: BinaryAssociation = BinaryAssociation(
    name="pageThumbnail32",
    ends={
        Property(name="presentation_PageThumbnailType", type=presentation_NotesType, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_NotesType33", type=presentation_PageThumbnailType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
path24: BinaryAssociation = BinaryAssociation(
    name="path24",
    ends={
        Property(name="presentation_PathType", type=presentation_NotesType, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_NotesType25", type=presentation_PathType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
frame34: BinaryAssociation = BinaryAssociation(
    name="frame34",
    ends={
        Property(name="presentation_FrameType", type=presentation_NotesType, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_NotesType35", type=presentation_FrameType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
measure36: BinaryAssociation = BinaryAssociation(
    name="measure36",
    ends={
        Property(name="presentation_MeasureType", type=presentation_NotesType, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_NotesType37", type=presentation_MeasureType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
caption38: BinaryAssociation = BinaryAssociation(
    name="caption38",
    ends={
        Property(name="presentation_CaptionType", type=presentation_NotesType, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_NotesType39", type=presentation_CaptionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
connector40: BinaryAssociation = BinaryAssociation(
    name="connector40",
    ends={
        Property(name="presentation_ConnectorType", type=presentation_NotesType, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_NotesType41", type=presentation_ConnectorType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
control42: BinaryAssociation = BinaryAssociation(
    name="control42",
    ends={
        Property(name="presentation_ControlType", type=presentation_NotesType, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_NotesType43", type=presentation_ControlType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
scene44: BinaryAssociation = BinaryAssociation(
    name="scene44",
    ends={
        Property(name="presentation_SceneType", type=presentation_NotesType, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_NotesType45", type=presentation_SceneType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
customShape46: BinaryAssociation = BinaryAssociation(
    name="customShape46",
    ends={
        Property(name="presentation_CustomShapeType", type=presentation_NotesType, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_NotesType47", type=presentation_CustomShapeType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
show48: BinaryAssociation = BinaryAssociation(
    name="show48",
    ends={
        Property(name="presentation_ShowType", type=presentation_SettingsType, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_SettingsType", type=presentation_ShowType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sound49: BinaryAssociation = BinaryAssociation(
    name="sound49",
    ends={
        Property(name="presentation_SoundType50", type=presentation_ShowShapeType, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_ShowShapeType", type=presentation_SoundType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sound51: BinaryAssociation = BinaryAssociation(
    name="sound51",
    ends={
        Property(name="presentation_SoundType52", type=presentation_ShowTextType, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_ShowTextType", type=presentation_SoundType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
xMLNSPrefixMap53: BinaryAssociation = BinaryAssociation(
    name="xMLNSPrefixMap53",
    ends={
        Property(name="presentation_EStringToStringMapEntry", type=presentation_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_DocumentRoot", type=presentation_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
xSISchemaLocation54: BinaryAssociation = BinaryAssociation(
    name="xSISchemaLocation54",
    ends={
        Property(name="presentation_EStringToStringMapEntry56", type=presentation_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_DocumentRoot55", type=presentation_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
animationGroup57: BinaryAssociation = BinaryAssociation(
    name="animationGroup57",
    ends={
        Property(name="presentation_AnimationGroupType59", type=presentation_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_DocumentRoot58", type=presentation_AnimationGroupType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
animations60: BinaryAssociation = BinaryAssociation(
    name="animations60",
    ends={
        Property(name="presentation_AnimationsType162", type=presentation_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_DocumentRoot61", type=presentation_AnimationsType1, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dateTime63: BinaryAssociation = BinaryAssociation(
    name="dateTime63",
    ends={
        Property(name="presentation_DateTimeType", type=presentation_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_DocumentRoot64", type=presentation_DateTimeType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dateTimeDecl65: BinaryAssociation = BinaryAssociation(
    name="dateTimeDecl65",
    ends={
        Property(name="presentation_DateTimeDeclType", type=presentation_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_DocumentRoot66", type=presentation_DateTimeDeclType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dim67: BinaryAssociation = BinaryAssociation(
    name="dim67",
    ends={
        Property(name="presentation_DimType69", type=presentation_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_DocumentRoot68", type=presentation_DimType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eventListener70: BinaryAssociation = BinaryAssociation(
    name="eventListener70",
    ends={
        Property(name="presentation_EventListenerType72", type=presentation_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_DocumentRoot71", type=presentation_EventListenerType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
footer73: BinaryAssociation = BinaryAssociation(
    name="footer73",
    ends={
        Property(name="presentation_FooterType", type=presentation_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_DocumentRoot74", type=presentation_FooterType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
header77: BinaryAssociation = BinaryAssociation(
    name="header77",
    ends={
        Property(name="presentation_HeaderType", type=presentation_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_DocumentRoot78", type=presentation_HeaderType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
headerDecl79: BinaryAssociation = BinaryAssociation(
    name="headerDecl79",
    ends={
        Property(name="presentation_HeaderDeclType", type=presentation_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_DocumentRoot80", type=presentation_HeaderDeclType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
hideShape81: BinaryAssociation = BinaryAssociation(
    name="hideShape81",
    ends={
        Property(name="presentation_HideShapeType83", type=presentation_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_DocumentRoot82", type=presentation_HideShapeType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
hideText84: BinaryAssociation = BinaryAssociation(
    name="hideText84",
    ends={
        Property(name="presentation_HideTextType86", type=presentation_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_DocumentRoot85", type=presentation_HideTextType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
notes87: BinaryAssociation = BinaryAssociation(
    name="notes87",
    ends={
        Property(name="presentation_NotesType89", type=presentation_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_DocumentRoot88", type=presentation_NotesType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
placeholder90: BinaryAssociation = BinaryAssociation(
    name="placeholder90",
    ends={
        Property(name="presentation_PlaceholderType", type=presentation_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_DocumentRoot91", type=presentation_PlaceholderType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
footerDecl75: BinaryAssociation = BinaryAssociation(
    name="footerDecl75",
    ends={
        Property(name="presentation_FooterDeclType", type=presentation_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_DocumentRoot76", type=presentation_FooterDeclType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
settings94: BinaryAssociation = BinaryAssociation(
    name="settings94",
    ends={
        Property(name="presentation_SettingsType96", type=presentation_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_DocumentRoot95", type=presentation_SettingsType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
show97: BinaryAssociation = BinaryAssociation(
    name="show97",
    ends={
        Property(name="presentation_ShowType99", type=presentation_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_DocumentRoot98", type=presentation_ShowType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
showShape100: BinaryAssociation = BinaryAssociation(
    name="showShape100",
    ends={
        Property(name="presentation_ShowShapeType102", type=presentation_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_DocumentRoot101", type=presentation_ShowShapeType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
showText103: BinaryAssociation = BinaryAssociation(
    name="showText103",
    ends={
        Property(name="presentation_ShowTextType105", type=presentation_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_DocumentRoot104", type=presentation_ShowTextType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sound106: BinaryAssociation = BinaryAssociation(
    name="sound106",
    ends={
        Property(name="presentation_SoundType108", type=presentation_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_DocumentRoot107", type=presentation_SoundType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
play92: BinaryAssociation = BinaryAssociation(
    name="play92",
    ends={
        Property(name="presentation_PlayType", type=presentation_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_DocumentRoot93", type=presentation_PlayType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="presentation",
    types={presentation_AnimationGroupType, presentation_DateTimeDeclType, presentation_EObject, presentation_AnimationsType1, presentation_SoundType, presentation_EventListenerType, presentation_DateTimeType, presentation_DimType, presentation_FooterType, presentation_HeaderDeclType, presentation_HeaderType, presentation_HideShapeType, presentation_FooterDeclType, presentation_HideTextType, presentation_FormsType, presentation_RectType, presentation_NotesType, presentation_PolygonType, presentation_RegularPolygonType, presentation_LineType, presentation_PolylineType, presentation_CircleType, presentation_EllipseType, presentation_GType, presentation_PathType, presentation_PageThumbnailType, presentation_FrameType, presentation_MeasureType, presentation_CaptionType, presentation_ConnectorType, presentation_ControlType, presentation_SceneType, presentation_CustomShapeType, presentation_PlaceholderType, presentation_SettingsType, presentation_ShowType, presentation_PlayType, presentation_ShowShapeType, presentation_ShowTextType, presentation_DocumentRoot, presentation_EStringToStringMapEntry, ActionType, AnimationsType, NodeTypeType, PresetClassType, SourceType, TransitionOnClickType, TransitionStyleType, VisibilityType, TransitionTypeType},
    associations={presentationAnimationElements1, animationGroup3, presentationAnimationElements0, sound6, sound7, sound9, sound11, forms13, rect14, polygon20, regularPolygon22, line16, polyline18, circle26, ellipse28, g30, pageThumbnail32, path24, frame34, measure36, caption38, connector40, control42, scene44, customShape46, show48, sound49, sound51, xMLNSPrefixMap53, xSISchemaLocation54, animationGroup57, animations60, dateTime63, dateTimeDecl65, dim67, eventListener70, footer73, header77, headerDecl79, hideShape81, hideText84, notes87, placeholder90, footerDecl75, settings94, show97, showShape100, showText103, sound106, play92},
    generalizations={},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)