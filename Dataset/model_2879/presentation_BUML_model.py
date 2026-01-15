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
CoordinateType: Enumeration = Enumeration(
    name="CoordinateType",
    literals={
            EnumerationLiteral(name="TOP_Y"),
			EnumerationLiteral(name="X"),
			EnumerationLiteral(name="Y"),
			EnumerationLiteral(name="CENTER_X"),
			EnumerationLiteral(name="CENTER_Y"),
			EnumerationLiteral(name="LEFT_X")
    }
)

# Classes
presentation_literal_GeneralLiteral = Class(name="presentation::literal::GeneralLiteral", is_abstract=True)
presentation_literal_BooleanLiteral = Class(name="presentation::literal::BooleanLiteral")
GeneralLiteral = Class(name="GeneralLiteral")
presentation_literal_NameLiteral = Class(name="presentation::literal::NameLiteral")
TextLiteral = Class(name="TextLiteral")
presentation_literal_FilenameLiteral = Class(name="presentation::literal::FilenameLiteral")
presentation_literal_Literal = Class(name="presentation::literal::Literal", is_abstract=True)
presentation_literal_NumericLiteral = Class(name="presentation::literal::NumericLiteral", is_abstract=True)
Literal = Class(name="Literal")
presentation_literal_NumberLiteral = Class(name="presentation::literal::NumberLiteral")
NumericLiteral = Class(name="NumericLiteral")
presentation_scenario_PCL = Class(name="presentation::scenario::PCL")
statements_Statement = Class(name="statements::Statement")
presentation_scenario_Scenario = Class(name="presentation::scenario::Scenario")
NamedElement = Class(name="NamedElement")
Header = Class(name="Header")
presentation_literal_TextLiteral = Class(name="presentation::literal::TextLiteral")
presentation_scenario_ScenarioFile = Class(name="presentation::scenario::ScenarioFile", is_abstract=True)
presentation_scenario_Header = Class(name="presentation::scenario::Header")
ScenarioFile = Class(name="ScenarioFile")
HeaderParameter = Class(name="HeaderParameter")
presentation_scenario_SDL = Class(name="presentation::scenario::SDL")
ScenarioObject = Class(name="ScenarioObject")
presentation_parameter_ButtonCodesParameter = Class(name="presentation::parameter::ButtonCodesParameter")
presentation_parameter_ScenarioNameParameter = Class(name="presentation::parameter::ScenarioNameParameter")
NameLiteral = Class(name="NameLiteral")
presentation_parameter_TimeParameter = Class(name="presentation::parameter::TimeParameter")
StimulusEventParameter = Class(name="StimulusEventParameter")
SDL = Class(name="SDL")
PCL = Class(name="PCL")
presentation_parameter_Parameter = Class(name="presentation::parameter::Parameter", is_abstract=True)
presentation_parameter_HeaderParameter = Class(name="presentation::parameter::HeaderParameter", is_abstract=True)
Parameter_ = Class(name="Parameter")
presentation_parameter_StimulusEventParameter = Class(name="presentation::parameter::StimulusEventParameter", is_abstract=True)
presentation_parameter_ActiveButtonsParameter = Class(name="presentation::parameter::ActiveButtonsParameter")
NumberLiteral = Class(name="NumberLiteral")
presentation_parameter_TextParameter = Class(name="presentation::parameter::TextParameter", is_abstract=True)
presentation_parameter_CaptionParameter = Class(name="presentation::parameter::CaptionParameter")
TextParameter = Class(name="TextParameter")
presentation_parameter_BitmapParameter = Class(name="presentation::parameter::BitmapParameter", is_abstract=True)
presentation_parameter_FilenameParameter = Class(name="presentation::parameter::FilenameParameter")
BitmapParameter = Class(name="BitmapParameter")
FilenameLiteral = Class(name="FilenameLiteral")
presentation_parameter_TargetButtonParameter = Class(name="presentation::parameter::TargetButtonParameter")
presentation_parameter_CodeParameter = Class(name="presentation::parameter::CodeParameter")
presentation_parameter_PictureParameter = Class(name="presentation::parameter::PictureParameter", is_abstract=True)
presentation_parameter_BackgroundColorParameter = Class(name="presentation::parameter::BackgroundColorParameter")
PictureParameter = Class(name="PictureParameter")
presentation_stimulus_Stimulus = Class(name="presentation::stimulus::Stimulus", is_abstract=True)
presentation_stimulus_StimulusEvent = Class(name="presentation::stimulus::StimulusEvent", is_abstract=True)
presentation_stimulus_StimulusList = Class(name="presentation::stimulus::StimulusList")
StimulusEvent = Class(name="StimulusEvent")
presentation_parameter_TrialParameter = Class(name="presentation::parameter::TrialParameter", is_abstract=True)
presentation_general_CoordinateDefinition = Class(name="presentation::general::CoordinateDefinition")
presentation_general_NamedElement = Class(name="presentation::general::NamedElement", is_abstract=True)
presentation_picture_PictureStimulusEvent = Class(name="presentation::picture::PictureStimulusEvent")
picture_Picture = Class(name="picture::Picture")
presentation_picture_PicturePart = Class(name="presentation::picture::PicturePart", is_abstract=True)
presentation_picture_Bitmap = Class(name="presentation::picture::Bitmap")
Graphic2D = Class(name="Graphic2D")
FilenameParameter = Class(name="FilenameParameter")
presentation_stimulus_Trial = Class(name="presentation::stimulus::Trial")
StimulusList = Class(name="StimulusList")
TrialParameter = Class(name="TrialParameter")
presentation_stimulus_ScenarioObject = Class(name="presentation::stimulus::ScenarioObject", is_abstract=True)
presentation_picture_Picture = Class(name="presentation::picture::Picture")
Stimulus = Class(name="Stimulus")
picture_PicturePart = Class(name="picture::PicturePart")
presentation_picture_Stimulus2D = Class(name="presentation::picture::Stimulus2D", is_abstract=True)
PicturePart = Class(name="PicturePart")
CoordinateDefinition = Class(name="CoordinateDefinition")
presentation_picture_BitmapStimulus = Class(name="presentation::picture::BitmapStimulus")
Stimulus2D = Class(name="Stimulus2D")
picture_Bitmap = Class(name="picture::Bitmap")
presentation_picture_Text = Class(name="presentation::picture::Text")
CaptionParameter = Class(name="CaptionParameter")
presentation_picture_Box = Class(name="presentation::picture::Box")
presentation_picture_Graphic2D = Class(name="presentation::picture::Graphic2D", is_abstract=True)
presentation_types_Type = Class(name="presentation::types::Type", is_abstract=True)
presentation_types_BasicType = Class(name="presentation::types::BasicType", is_abstract=True)
Type = Class(name="Type")
presentation_types_Bool = Class(name="presentation::types::Bool")
BasicType = Class(name="BasicType")
presentation_types_Int = Class(name="presentation::types::Int")
presentation_types_Double = Class(name="presentation::types::Double")
presentation_types_String = Class(name="presentation::types::String")
presentation_expressions_BooleanExpression = Class(name="presentation::expressions::BooleanExpression", is_abstract=True)
Expression = Class(name="Expression")
presentation_picture_BoxStimulus = Class(name="presentation::picture::BoxStimulus")
picture_Box = Class(name="picture::Box")
presentation_picture_TextStimulus = Class(name="presentation::picture::TextStimulus")
picture_Text = Class(name="picture::Text")
presentation_sound_Sound = Class(name="presentation::sound::Sound")
presentation_expressions_AtomExpression = Class(name="presentation::expressions::AtomExpression", is_abstract=True)
presentation_expressions_BoolExpression = Class(name="presentation::expressions::BoolExpression")
AtomExpression = Class(name="AtomExpression")
BooleanLiteral = Class(name="BooleanLiteral")
presentation_expressions_EqualsExpression = Class(name="presentation::expressions::EqualsExpression")
expressions_Expression = Class(name="expressions::Expression")
presentation_expressions_Expression = Class(name="presentation::expressions::Expression", is_abstract=True)
VariableInitializer = Class(name="VariableInitializer")
presentation_expressions_OrExpression = Class(name="presentation::expressions::OrExpression")
BooleanExpression = Class(name="BooleanExpression")
expressions_BooleanExpression = Class(name="expressions::BooleanExpression")
presentation_expressions_AndExpression = Class(name="presentation::expressions::AndExpression")
presentation_expressions_NotExpression = Class(name="presentation::expressions::NotExpression")
presentation_operators_EqualityOperator = Class(name="presentation::operators::EqualityOperator", is_abstract=True)
presentation_operators_MultiplicativeOperator = Class(name="presentation::operators::MultiplicativeOperator", is_abstract=True)
presentation_operators_UnaryOperator = Class(name="presentation::operators::UnaryOperator", is_abstract=True)
presentation_operators_AdditiveOperator = Class(name="presentation::operators::AdditiveOperator", is_abstract=True)
presentation_operators_Assignment = Class(name="presentation::operators::Assignment")
AssignmentOperator = Class(name="AssignmentOperator")
presentation_operators_Greater = Class(name="presentation::operators::Greater")
RelationOperator = Class(name="RelationOperator")
presentation_operators_Less = Class(name="presentation::operators::Less")
presentation_expressions_StatementExpression = Class(name="presentation::expressions::StatementExpression", is_abstract=True)
presentation_expressions_AssignmentExpression = Class(name="presentation::expressions::AssignmentExpression")
expressions_StatementExpression = Class(name="expressions::StatementExpression")
operators_AssignmentOperator = Class(name="operators::AssignmentOperator")
presentation_expressions_PrimaryExpression = Class(name="presentation::expressions::PrimaryExpression", is_abstract=True)
presentation_operators_Operator = Class(name="presentation::operators::Operator", is_abstract=True)
presentation_operators_AssignmentOperator = Class(name="presentation::operators::AssignmentOperator", is_abstract=True)
Operator = Class(name="Operator")
presentation_operators_RelationOperator = Class(name="presentation::operators::RelationOperator", is_abstract=True)
presentation_statements_Loop = Class(name="presentation::statements::Loop")
statements_StatementList = Class(name="statements::StatementList")
presentation_operators_GreaterOrEqual = Class(name="presentation::operators::GreaterOrEqual")
presentation_operators_LessOrEqual = Class(name="presentation::operators::LessOrEqual")
presentation_operators_Equal = Class(name="presentation::operators::Equal")
EqualityOperator = Class(name="EqualityOperator")
presentation_operators_NotEqual = Class(name="presentation::operators::NotEqual")
presentation_statements_Statement = Class(name="presentation::statements::Statement", is_abstract=True)
presentation_statements_StatementList = Class(name="presentation::statements::StatementList")
presentation_statements_Inclusion = Class(name="presentation::statements::Inclusion")
Statement = Class(name="Statement")
presentation_statements_Assignment = Class(name="presentation::statements::Assignment")
presentation_statements_VariableDeclarator = Class(name="presentation::statements::VariableDeclarator")
common_VariableInitializer = Class(name="common::VariableInitializer")
presentation_common_VariableInitializer = Class(name="presentation::common::VariableInitializer", is_abstract=True)
presentation_common_NamedElement = Class(name="presentation::common::NamedElement", is_abstract=True)
presentation_common_Identifier = Class(name="presentation::common::Identifier")
presentation_statements_VariableDeclaration = Class(name="presentation::statements::VariableDeclaration")
statements_ForInitializer = Class(name="statements::ForInitializer")
statements_ResourceAcquisition = Class(name="statements::ResourceAcquisition")
types_Type = Class(name="types::Type")
statements_VariableDeclarator = Class(name="statements::VariableDeclarator")
presentation_statements_DeclarationStatement = Class(name="presentation::statements::DeclarationStatement")
statements_VariableDeclaration = Class(name="statements::VariableDeclaration")
presentation_statements_ForInitializer = Class(name="presentation::statements::ForInitializer", is_abstract=True)
presentation_statements_ResourceAcquisition = Class(name="presentation::statements::ResourceAcquisition", is_abstract=True)
presentation_program_Block = Class(name="presentation::program::Block")

# presentation_literal_GeneralLiteral class attributes and methods

# presentation_literal_BooleanLiteral class attributes and methods
presentation_literal_BooleanLiteral_value: Property = Property(name="value", type=BooleanType)
presentation_literal_BooleanLiteral.attributes={presentation_literal_BooleanLiteral_value}

# GeneralLiteral class attributes and methods

# presentation_literal_NameLiteral class attributes and methods

# TextLiteral class attributes and methods

# presentation_literal_FilenameLiteral class attributes and methods

# presentation_literal_Literal class attributes and methods

# presentation_literal_NumericLiteral class attributes and methods

# Literal class attributes and methods

# presentation_literal_NumberLiteral class attributes and methods
presentation_literal_NumberLiteral_value: Property = Property(name="value", type=IntegerType)
presentation_literal_NumberLiteral.attributes={presentation_literal_NumberLiteral_value}

# NumericLiteral class attributes and methods

# presentation_scenario_PCL class attributes and methods

# statements_Statement class attributes and methods

# presentation_scenario_Scenario class attributes and methods

# NamedElement class attributes and methods

# Header class attributes and methods

# presentation_literal_TextLiteral class attributes and methods
presentation_literal_TextLiteral_value: Property = Property(name="value", type=StringType)
presentation_literal_TextLiteral.attributes={presentation_literal_TextLiteral_value}

# presentation_scenario_ScenarioFile class attributes and methods

# presentation_scenario_Header class attributes and methods

# ScenarioFile class attributes and methods

# HeaderParameter class attributes and methods

# presentation_scenario_SDL class attributes and methods

# ScenarioObject class attributes and methods

# presentation_parameter_ButtonCodesParameter class attributes and methods

# presentation_parameter_ScenarioNameParameter class attributes and methods

# NameLiteral class attributes and methods

# presentation_parameter_TimeParameter class attributes and methods

# StimulusEventParameter class attributes and methods

# SDL class attributes and methods

# PCL class attributes and methods

# presentation_parameter_Parameter class attributes and methods

# presentation_parameter_HeaderParameter class attributes and methods

# Parameter class attributes and methods

# presentation_parameter_StimulusEventParameter class attributes and methods

# presentation_parameter_ActiveButtonsParameter class attributes and methods

# NumberLiteral class attributes and methods

# presentation_parameter_TextParameter class attributes and methods

# presentation_parameter_CaptionParameter class attributes and methods

# TextParameter class attributes and methods

# presentation_parameter_BitmapParameter class attributes and methods

# presentation_parameter_FilenameParameter class attributes and methods

# BitmapParameter class attributes and methods

# FilenameLiteral class attributes and methods

# presentation_parameter_TargetButtonParameter class attributes and methods

# presentation_parameter_CodeParameter class attributes and methods

# presentation_parameter_PictureParameter class attributes and methods

# presentation_parameter_BackgroundColorParameter class attributes and methods

# PictureParameter class attributes and methods

# presentation_stimulus_Stimulus class attributes and methods

# presentation_stimulus_StimulusEvent class attributes and methods

# presentation_stimulus_StimulusList class attributes and methods

# StimulusEvent class attributes and methods

# presentation_parameter_TrialParameter class attributes and methods

# presentation_general_CoordinateDefinition class attributes and methods
presentation_general_CoordinateDefinition_coordinate: Property = Property(name="coordinate", type=StringType)
presentation_general_CoordinateDefinition_type: Property = Property(name="type", type=StringType)
presentation_general_CoordinateDefinition_right_bottom: Property = Property(name="right_bottom", type=StringType)
presentation_general_CoordinateDefinition.attributes={presentation_general_CoordinateDefinition_coordinate, presentation_general_CoordinateDefinition_right_bottom, presentation_general_CoordinateDefinition_type}

# presentation_general_NamedElement class attributes and methods
presentation_general_NamedElement_name: Property = Property(name="name", type=StringType)
presentation_general_NamedElement.attributes={presentation_general_NamedElement_name}

# presentation_picture_PictureStimulusEvent class attributes and methods

# picture_Picture class attributes and methods

# presentation_picture_PicturePart class attributes and methods

# presentation_picture_Bitmap class attributes and methods
presentation_picture_Bitmap_bitmap_parameters: Property = Property(name="bitmap_parameters", type=StringType)
presentation_picture_Bitmap.attributes={presentation_picture_Bitmap_bitmap_parameters}

# Graphic2D class attributes and methods

# FilenameParameter class attributes and methods

# presentation_stimulus_Trial class attributes and methods

# StimulusList class attributes and methods

# TrialParameter class attributes and methods

# presentation_stimulus_ScenarioObject class attributes and methods

# presentation_picture_Picture class attributes and methods

# Stimulus class attributes and methods

# picture_PicturePart class attributes and methods

# presentation_picture_Stimulus2D class attributes and methods

# PicturePart class attributes and methods

# CoordinateDefinition class attributes and methods

# presentation_picture_BitmapStimulus class attributes and methods

# Stimulus2D class attributes and methods

# picture_Bitmap class attributes and methods

# presentation_picture_Text class attributes and methods

# CaptionParameter class attributes and methods

# presentation_picture_Box class attributes and methods

# presentation_picture_Graphic2D class attributes and methods

# presentation_types_Type class attributes and methods

# presentation_types_BasicType class attributes and methods

# Type class attributes and methods

# presentation_types_Bool class attributes and methods

# BasicType class attributes and methods

# presentation_types_Int class attributes and methods

# presentation_types_Double class attributes and methods

# presentation_types_String class attributes and methods

# presentation_expressions_BooleanExpression class attributes and methods

# Expression class attributes and methods

# presentation_picture_BoxStimulus class attributes and methods

# picture_Box class attributes and methods

# presentation_picture_TextStimulus class attributes and methods

# picture_Text class attributes and methods

# presentation_sound_Sound class attributes and methods

# presentation_expressions_AtomExpression class attributes and methods

# presentation_expressions_BoolExpression class attributes and methods

# AtomExpression class attributes and methods

# BooleanLiteral class attributes and methods

# presentation_expressions_EqualsExpression class attributes and methods

# expressions_Expression class attributes and methods

# presentation_expressions_Expression class attributes and methods

# VariableInitializer class attributes and methods

# presentation_expressions_OrExpression class attributes and methods

# BooleanExpression class attributes and methods

# expressions_BooleanExpression class attributes and methods

# presentation_expressions_AndExpression class attributes and methods

# presentation_expressions_NotExpression class attributes and methods

# presentation_operators_EqualityOperator class attributes and methods

# presentation_operators_MultiplicativeOperator class attributes and methods

# presentation_operators_UnaryOperator class attributes and methods

# presentation_operators_AdditiveOperator class attributes and methods

# presentation_operators_Assignment class attributes and methods

# AssignmentOperator class attributes and methods

# presentation_operators_Greater class attributes and methods

# RelationOperator class attributes and methods

# presentation_operators_Less class attributes and methods

# presentation_expressions_StatementExpression class attributes and methods

# presentation_expressions_AssignmentExpression class attributes and methods

# expressions_StatementExpression class attributes and methods

# operators_AssignmentOperator class attributes and methods

# presentation_expressions_PrimaryExpression class attributes and methods

# presentation_operators_Operator class attributes and methods

# presentation_operators_AssignmentOperator class attributes and methods

# Operator class attributes and methods

# presentation_operators_RelationOperator class attributes and methods

# presentation_statements_Loop class attributes and methods

# statements_StatementList class attributes and methods

# presentation_operators_GreaterOrEqual class attributes and methods

# presentation_operators_LessOrEqual class attributes and methods

# presentation_operators_Equal class attributes and methods

# EqualityOperator class attributes and methods

# presentation_operators_NotEqual class attributes and methods

# presentation_statements_Statement class attributes and methods

# presentation_statements_StatementList class attributes and methods

# presentation_statements_Inclusion class attributes and methods

# Statement class attributes and methods

# presentation_statements_Assignment class attributes and methods

# presentation_statements_VariableDeclarator class attributes and methods

# common_VariableInitializer class attributes and methods

# presentation_common_VariableInitializer class attributes and methods

# presentation_common_NamedElement class attributes and methods
presentation_common_NamedElement_name: Property = Property(name="name", type=StringType)
presentation_common_NamedElement.attributes={presentation_common_NamedElement_name}

# presentation_common_Identifier class attributes and methods

# presentation_statements_VariableDeclaration class attributes and methods

# statements_ForInitializer class attributes and methods

# statements_ResourceAcquisition class attributes and methods

# types_Type class attributes and methods

# statements_VariableDeclarator class attributes and methods

# presentation_statements_DeclarationStatement class attributes and methods

# statements_VariableDeclaration class attributes and methods

# presentation_statements_ForInitializer class attributes and methods

# presentation_statements_ResourceAcquisition class attributes and methods

# presentation_program_Block class attributes and methods

# Relationships
statement2: BinaryAssociation = BinaryAssociation(
    name="statement2",
    ends={
        Property(name="statements_Statement", type=presentation_scenario_PCL, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_scenario_PCL", type=statements_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
header3: BinaryAssociation = BinaryAssociation(
    name="header3",
    ends={
        Property(name="Header", type=presentation_scenario_Scenario, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_scenario_Scenario", type=Header, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameter0: BinaryAssociation = BinaryAssociation(
    name="parameter0",
    ends={
        Property(name="HeaderParameter", type=presentation_scenario_Header, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_scenario_Header", type=HeaderParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
scenario_object1: BinaryAssociation = BinaryAssociation(
    name="scenario_object1",
    ends={
        Property(name="ScenarioObject", type=presentation_scenario_SDL, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_scenario_SDL", type=ScenarioObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
number_literal9: BinaryAssociation = BinaryAssociation(
    name="number_literal9",
    ends={
        Property(name="NumberLiteral10", type=presentation_parameter_ButtonCodesParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_parameter_ButtonCodesParameter", type=NumberLiteral, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
name_literal11: BinaryAssociation = BinaryAssociation(
    name="name_literal11",
    ends={
        Property(name="NameLiteral", type=presentation_parameter_ScenarioNameParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_parameter_ScenarioNameParameter", type=NameLiteral, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
sdl4: BinaryAssociation = BinaryAssociation(
    name="sdl4",
    ends={
        Property(name="SDL", type=presentation_scenario_Scenario, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_scenario_Scenario5", type=SDL, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pcl6: BinaryAssociation = BinaryAssociation(
    name="pcl6",
    ends={
        Property(name="PCL", type=presentation_scenario_Scenario, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_scenario_Scenario7", type=PCL, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
number_literal8: BinaryAssociation = BinaryAssociation(
    name="number_literal8",
    ends={
        Property(name="NumberLiteral", type=presentation_parameter_ActiveButtonsParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_parameter_ActiveButtonsParameter", type=NumberLiteral, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
text_literal19: BinaryAssociation = BinaryAssociation(
    name="text_literal19",
    ends={
        Property(name="TextLiteral20", type=presentation_parameter_CaptionParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_parameter_CaptionParameter", type=TextLiteral, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
number_literal12: BinaryAssociation = BinaryAssociation(
    name="number_literal12",
    ends={
        Property(name="NumberLiteral13", type=presentation_parameter_TimeParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_parameter_TimeParameter", type=NumberLiteral, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
number_literal14: BinaryAssociation = BinaryAssociation(
    name="number_literal14",
    ends={
        Property(name="NumberLiteral15", type=presentation_parameter_TargetButtonParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_parameter_TargetButtonParameter", type=NumberLiteral, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
text_literal16: BinaryAssociation = BinaryAssociation(
    name="text_literal16",
    ends={
        Property(name="TextLiteral", type=presentation_parameter_CodeParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_parameter_CodeParameter", type=TextLiteral, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
number_literal17: BinaryAssociation = BinaryAssociation(
    name="number_literal17",
    ends={
        Property(name="NumberLiteral18", type=presentation_parameter_BackgroundColorParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_parameter_BackgroundColorParameter", type=NumberLiteral, multiplicity=Multiplicity(3, 3), is_composite=True)
    }
)
stimulus_event_parameter22: BinaryAssociation = BinaryAssociation(
    name="stimulus_event_parameter22",
    ends={
        Property(name="StimulusEventParameter", type=presentation_stimulus_StimulusEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_stimulus_StimulusEvent", type=StimulusEventParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
stimulus_event23: BinaryAssociation = BinaryAssociation(
    name="stimulus_event23",
    ends={
        Property(name="StimulusEvent", type=presentation_stimulus_StimulusList, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_stimulus_StimulusList", type=StimulusEvent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
filename_literal21: BinaryAssociation = BinaryAssociation(
    name="filename_literal21",
    ends={
        Property(name="FilenameLiteral", type=presentation_parameter_FilenameParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_parameter_FilenameParameter", type=FilenameLiteral, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
picture_parameter28: BinaryAssociation = BinaryAssociation(
    name="picture_parameter28",
    ends={
        Property(name="presentation_picture_Picture29", type=PictureParameter, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="PictureParameter", type=presentation_picture_Picture, multiplicity=Multiplicity(1, 1))
    }
)
picture30: BinaryAssociation = BinaryAssociation(
    name="picture30",
    ends={
        Property(name="picture_Picture", type=presentation_picture_PictureStimulusEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_picture_PictureStimulusEvent", type=picture_Picture, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
stimulus_list24: BinaryAssociation = BinaryAssociation(
    name="stimulus_list24",
    ends={
        Property(name="StimulusList", type=presentation_stimulus_Trial, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_stimulus_Trial", type=StimulusList, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
trial_parameter25: BinaryAssociation = BinaryAssociation(
    name="trial_parameter25",
    ends={
        Property(name="TrialParameter", type=presentation_stimulus_Trial, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_stimulus_Trial26", type=TrialParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
picture_part27: BinaryAssociation = BinaryAssociation(
    name="picture_part27",
    ends={
        Property(name="picture_PicturePart", type=presentation_picture_Picture, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_picture_Picture", type=picture_PicturePart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
x_definition35: BinaryAssociation = BinaryAssociation(
    name="x_definition35",
    ends={
        Property(name="CoordinateDefinition", type=presentation_picture_Stimulus2D, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_picture_Stimulus2D", type=CoordinateDefinition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
y_definition36: BinaryAssociation = BinaryAssociation(
    name="y_definition36",
    ends={
        Property(name="CoordinateDefinition38", type=presentation_picture_Stimulus2D, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_picture_Stimulus2D37", type=CoordinateDefinition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
bitmap39: BinaryAssociation = BinaryAssociation(
    name="bitmap39",
    ends={
        Property(name="picture_Bitmap", type=presentation_picture_BitmapStimulus, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_picture_BitmapStimulus", type=picture_Bitmap, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
filename_parameter31: BinaryAssociation = BinaryAssociation(
    name="filename_parameter31",
    ends={
        Property(name="FilenameParameter", type=presentation_picture_Bitmap, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_picture_Bitmap", type=FilenameParameter, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
caption32: BinaryAssociation = BinaryAssociation(
    name="caption32",
    ends={
        Property(name="CaptionParameter", type=presentation_picture_Text, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_picture_Text", type=CaptionParameter, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
text_parameter33: BinaryAssociation = BinaryAssociation(
    name="text_parameter33",
    ends={
        Property(name="TextParameter", type=presentation_picture_Text, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_picture_Text34", type=TextParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
box40: BinaryAssociation = BinaryAssociation(
    name="box40",
    ends={
        Property(name="picture_Box", type=presentation_picture_BoxStimulus, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_picture_BoxStimulus", type=picture_Box, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
text41: BinaryAssociation = BinaryAssociation(
    name="text41",
    ends={
        Property(name="picture_Text", type=presentation_picture_TextStimulus, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_picture_TextStimulus", type=picture_Text, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value47: BinaryAssociation = BinaryAssociation(
    name="value47",
    ends={
        Property(name="BooleanLiteral", type=presentation_expressions_BoolExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_expressions_BoolExpression", type=BooleanLiteral, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
arguments48: BinaryAssociation = BinaryAssociation(
    name="arguments48",
    ends={
        Property(name="expressions_Expression", type=presentation_expressions_EqualsExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_expressions_EqualsExpression", type=expressions_Expression, multiplicity=Multiplicity(2, 2), is_composite=True)
    }
)
argument42: BinaryAssociation = BinaryAssociation(
    name="argument42",
    ends={
        Property(name="expressions_BooleanExpression", type=presentation_expressions_OrExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_expressions_OrExpression", type=expressions_BooleanExpression, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
argument43: BinaryAssociation = BinaryAssociation(
    name="argument43",
    ends={
        Property(name="expressions_BooleanExpression44", type=presentation_expressions_AndExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_expressions_AndExpression", type=expressions_BooleanExpression, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
argument45: BinaryAssociation = BinaryAssociation(
    name="argument45",
    ends={
        Property(name="expressions_BooleanExpression46", type=presentation_expressions_NotExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_expressions_NotExpression", type=expressions_BooleanExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
assignmentOperator49: BinaryAssociation = BinaryAssociation(
    name="assignmentOperator49",
    ends={
        Property(name="operators_AssignmentOperator", type=presentation_expressions_AssignmentExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_expressions_AssignmentExpression", type=operators_AssignmentOperator, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression50: BinaryAssociation = BinaryAssociation(
    name="expression50",
    ends={
        Property(name="expressions_Expression52", type=presentation_expressions_AssignmentExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_expressions_AssignmentExpression51", type=expressions_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression55: BinaryAssociation = BinaryAssociation(
    name="expression55",
    ends={
        Property(name="expressions_Expression56", type=presentation_statements_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_statements_Assignment", type=expressions_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
init57: BinaryAssociation = BinaryAssociation(
    name="init57",
    ends={
        Property(name="statements_StatementList", type=presentation_statements_Loop, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_statements_Loop", type=statements_StatementList, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body58: BinaryAssociation = BinaryAssociation(
    name="body58",
    ends={
        Property(name="statements_StatementList60", type=presentation_statements_Loop, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_statements_Loop59", type=statements_StatementList, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition61: BinaryAssociation = BinaryAssociation(
    name="condition61",
    ends={
        Property(name="expressions_BooleanExpression63", type=presentation_statements_Loop, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_statements_Loop62", type=expressions_BooleanExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statement53: BinaryAssociation = BinaryAssociation(
    name="statement53",
    ends={
        Property(name="statements_Statement54", type=presentation_statements_StatementList, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_statements_StatementList", type=statements_Statement, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
variableInitializer68: BinaryAssociation = BinaryAssociation(
    name="variableInitializer68",
    ends={
        Property(name="common_VariableInitializer", type=presentation_statements_VariableDeclarator, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_statements_VariableDeclarator", type=common_VariableInitializer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type64: BinaryAssociation = BinaryAssociation(
    name="type64",
    ends={
        Property(name="types_Type", type=presentation_statements_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_statements_VariableDeclaration", type=types_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variableDeclarator65: BinaryAssociation = BinaryAssociation(
    name="variableDeclarator65",
    ends={
        Property(name="statements_VariableDeclarator", type=presentation_statements_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_statements_VariableDeclaration66", type=statements_VariableDeclarator, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variableDeclaration67: BinaryAssociation = BinaryAssociation(
    name="variableDeclaration67",
    ends={
        Property(name="statements_VariableDeclaration", type=presentation_statements_DeclarationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_statements_DeclarationStatement", type=statements_VariableDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statement69: BinaryAssociation = BinaryAssociation(
    name="statement69",
    ends={
        Property(name="statements_Statement70", type=presentation_program_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_program_Block", type=statements_Statement, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_presentation_literal_GeneralLiteral_Literal = Generalization(general=Literal, specific=presentation_literal_GeneralLiteral)
gen_presentation_literal_BooleanLiteral_GeneralLiteral = Generalization(general=GeneralLiteral, specific=presentation_literal_BooleanLiteral)
gen_presentation_literal_NameLiteral_TextLiteral = Generalization(general=TextLiteral, specific=presentation_literal_NameLiteral)
gen_presentation_literal_FilenameLiteral_TextLiteral = Generalization(general=TextLiteral, specific=presentation_literal_FilenameLiteral)
gen_presentation_literal_NumericLiteral_Literal = Generalization(general=Literal, specific=presentation_literal_NumericLiteral)
gen_presentation_literal_NumberLiteral_NumericLiteral = Generalization(general=NumericLiteral, specific=presentation_literal_NumberLiteral)
gen_presentation_scenario_PCL_ScenarioFile = Generalization(general=ScenarioFile, specific=presentation_scenario_PCL)
gen_presentation_scenario_Scenario_NamedElement = Generalization(general=NamedElement, specific=presentation_scenario_Scenario)
gen_presentation_literal_TextLiteral_GeneralLiteral = Generalization(general=GeneralLiteral, specific=presentation_literal_TextLiteral)
gen_presentation_scenario_Header_ScenarioFile = Generalization(general=ScenarioFile, specific=presentation_scenario_Header)
gen_presentation_scenario_SDL_ScenarioFile = Generalization(general=ScenarioFile, specific=presentation_scenario_SDL)
gen_presentation_parameter_ButtonCodesParameter_HeaderParameter = Generalization(general=HeaderParameter, specific=presentation_parameter_ButtonCodesParameter)
gen_presentation_parameter_ScenarioNameParameter_HeaderParameter = Generalization(general=HeaderParameter, specific=presentation_parameter_ScenarioNameParameter)
gen_presentation_parameter_TimeParameter_StimulusEventParameter = Generalization(general=StimulusEventParameter, specific=presentation_parameter_TimeParameter)
gen_presentation_parameter_HeaderParameter_Parameter = Generalization(general=Parameter_, specific=presentation_parameter_HeaderParameter)
gen_presentation_parameter_StimulusEventParameter_Parameter = Generalization(general=Parameter_, specific=presentation_parameter_StimulusEventParameter)
gen_presentation_parameter_ActiveButtonsParameter_HeaderParameter = Generalization(general=HeaderParameter, specific=presentation_parameter_ActiveButtonsParameter)
gen_presentation_parameter_TextParameter_Parameter = Generalization(general=Parameter_, specific=presentation_parameter_TextParameter)
gen_presentation_parameter_CaptionParameter_TextParameter = Generalization(general=TextParameter, specific=presentation_parameter_CaptionParameter)
gen_presentation_parameter_FilenameParameter_BitmapParameter = Generalization(general=BitmapParameter, specific=presentation_parameter_FilenameParameter)
gen_presentation_parameter_TargetButtonParameter_StimulusEventParameter = Generalization(general=StimulusEventParameter, specific=presentation_parameter_TargetButtonParameter)
gen_presentation_parameter_CodeParameter_StimulusEventParameter = Generalization(general=StimulusEventParameter, specific=presentation_parameter_CodeParameter)
gen_presentation_parameter_PictureParameter_Parameter = Generalization(general=Parameter_, specific=presentation_parameter_PictureParameter)
gen_presentation_parameter_BackgroundColorParameter_PictureParameter = Generalization(general=PictureParameter, specific=presentation_parameter_BackgroundColorParameter)
gen_presentation_stimulus_Stimulus_ScenarioObject = Generalization(general=ScenarioObject, specific=presentation_stimulus_Stimulus)
gen_presentation_stimulus_StimulusEvent_ScenarioObject = Generalization(general=ScenarioObject, specific=presentation_stimulus_StimulusEvent)
gen_presentation_parameter_TrialParameter_Parameter = Generalization(general=Parameter_, specific=presentation_parameter_TrialParameter)
gen_presentation_picture_PictureStimulusEvent_StimulusEvent = Generalization(general=StimulusEvent, specific=presentation_picture_PictureStimulusEvent)
gen_presentation_picture_PicturePart_ScenarioObject = Generalization(general=ScenarioObject, specific=presentation_picture_PicturePart)
gen_presentation_picture_Bitmap_Graphic2D = Generalization(general=Graphic2D, specific=presentation_picture_Bitmap)
gen_presentation_stimulus_Trial_ScenarioObject = Generalization(general=ScenarioObject, specific=presentation_stimulus_Trial)
gen_presentation_stimulus_ScenarioObject_NamedElement = Generalization(general=NamedElement, specific=presentation_stimulus_ScenarioObject)
gen_presentation_picture_Picture_Stimulus = Generalization(general=Stimulus, specific=presentation_picture_Picture)
gen_presentation_picture_Stimulus2D_PicturePart = Generalization(general=PicturePart, specific=presentation_picture_Stimulus2D)
gen_presentation_picture_BitmapStimulus_Stimulus2D = Generalization(general=Stimulus2D, specific=presentation_picture_BitmapStimulus)
gen_presentation_picture_Text_Graphic2D = Generalization(general=Graphic2D, specific=presentation_picture_Text)
gen_presentation_picture_Box_Graphic2D = Generalization(general=Graphic2D, specific=presentation_picture_Box)
gen_presentation_picture_Graphic2D_ScenarioObject = Generalization(general=ScenarioObject, specific=presentation_picture_Graphic2D)
gen_presentation_types_BasicType_Type = Generalization(general=Type, specific=presentation_types_BasicType)
gen_presentation_types_Bool_BasicType = Generalization(general=BasicType, specific=presentation_types_Bool)
gen_presentation_types_Int_BasicType = Generalization(general=BasicType, specific=presentation_types_Int)
gen_presentation_types_Double_BasicType = Generalization(general=BasicType, specific=presentation_types_Double)
gen_presentation_types_String_BasicType = Generalization(general=BasicType, specific=presentation_types_String)
gen_presentation_expressions_BooleanExpression_Expression = Generalization(general=Expression, specific=presentation_expressions_BooleanExpression)
gen_presentation_picture_BoxStimulus_Stimulus2D = Generalization(general=Stimulus2D, specific=presentation_picture_BoxStimulus)
gen_presentation_picture_TextStimulus_Stimulus2D = Generalization(general=Stimulus2D, specific=presentation_picture_TextStimulus)
gen_presentation_sound_Sound_Stimulus = Generalization(general=Stimulus, specific=presentation_sound_Sound)
gen_presentation_expressions_AtomExpression_BooleanExpression = Generalization(general=BooleanExpression, specific=presentation_expressions_AtomExpression)
gen_presentation_expressions_BoolExpression_AtomExpression = Generalization(general=AtomExpression, specific=presentation_expressions_BoolExpression)
gen_presentation_expressions_EqualsExpression_AtomExpression = Generalization(general=AtomExpression, specific=presentation_expressions_EqualsExpression)
gen_presentation_expressions_Expression_VariableInitializer = Generalization(general=VariableInitializer, specific=presentation_expressions_Expression)
gen_presentation_expressions_OrExpression_BooleanExpression = Generalization(general=BooleanExpression, specific=presentation_expressions_OrExpression)
gen_presentation_expressions_AndExpression_BooleanExpression = Generalization(general=BooleanExpression, specific=presentation_expressions_AndExpression)
gen_presentation_expressions_NotExpression_BooleanExpression = Generalization(general=BooleanExpression, specific=presentation_expressions_NotExpression)
gen_presentation_operators_EqualityOperator_Operator = Generalization(general=Operator, specific=presentation_operators_EqualityOperator)
gen_presentation_operators_MultiplicativeOperator_Operator = Generalization(general=Operator, specific=presentation_operators_MultiplicativeOperator)
gen_presentation_operators_UnaryOperator_Operator = Generalization(general=Operator, specific=presentation_operators_UnaryOperator)
gen_presentation_operators_AdditiveOperator_Operator = Generalization(general=Operator, specific=presentation_operators_AdditiveOperator)
gen_presentation_operators_Assignment_AssignmentOperator = Generalization(general=AssignmentOperator, specific=presentation_operators_Assignment)
gen_presentation_operators_Greater_RelationOperator = Generalization(general=RelationOperator, specific=presentation_operators_Greater)
gen_presentation_expressions_AssignmentExpression_expressions_Expression = Generalization(general=expressions_Expression, specific=presentation_expressions_AssignmentExpression)
gen_presentation_expressions_AssignmentExpression_expressions_StatementExpression = Generalization(general=expressions_StatementExpression, specific=presentation_expressions_AssignmentExpression)
gen_presentation_operators_AssignmentOperator_Operator = Generalization(general=Operator, specific=presentation_operators_AssignmentOperator)
gen_presentation_operators_RelationOperator_Operator = Generalization(general=Operator, specific=presentation_operators_RelationOperator)
gen_presentation_statements_Loop_Statement = Generalization(general=Statement, specific=presentation_statements_Loop)
gen_presentation_operators_Less_RelationOperator = Generalization(general=RelationOperator, specific=presentation_operators_Less)
gen_presentation_operators_GreaterOrEqual_RelationOperator = Generalization(general=RelationOperator, specific=presentation_operators_GreaterOrEqual)
gen_presentation_operators_LessOrEqual_RelationOperator = Generalization(general=RelationOperator, specific=presentation_operators_LessOrEqual)
gen_presentation_operators_Equal_EqualityOperator = Generalization(general=EqualityOperator, specific=presentation_operators_Equal)
gen_presentation_operators_NotEqual_EqualityOperator = Generalization(general=EqualityOperator, specific=presentation_operators_NotEqual)
gen_presentation_statements_Inclusion_Statement = Generalization(general=Statement, specific=presentation_statements_Inclusion)
gen_presentation_statements_Assignment_Statement = Generalization(general=Statement, specific=presentation_statements_Assignment)
gen_presentation_statements_VariableDeclarator_NamedElement = Generalization(general=NamedElement, specific=presentation_statements_VariableDeclarator)
gen_presentation_common_Identifier_NamedElement = Generalization(general=NamedElement, specific=presentation_common_Identifier)
gen_presentation_statements_VariableDeclaration_statements_ForInitializer = Generalization(general=statements_ForInitializer, specific=presentation_statements_VariableDeclaration)
gen_presentation_statements_VariableDeclaration_statements_ResourceAcquisition = Generalization(general=statements_ResourceAcquisition, specific=presentation_statements_VariableDeclaration)
gen_presentation_statements_DeclarationStatement_Statement = Generalization(general=Statement, specific=presentation_statements_DeclarationStatement)

# Domain Model
domain_model = DomainModel(
    name="presentation",
    types={presentation_literal_GeneralLiteral, presentation_literal_BooleanLiteral, GeneralLiteral, presentation_literal_NameLiteral, TextLiteral, presentation_literal_FilenameLiteral, presentation_literal_Literal, presentation_literal_NumericLiteral, Literal, presentation_literal_NumberLiteral, NumericLiteral, presentation_scenario_PCL, statements_Statement, presentation_scenario_Scenario, NamedElement, Header, presentation_literal_TextLiteral, presentation_scenario_ScenarioFile, presentation_scenario_Header, ScenarioFile, HeaderParameter, presentation_scenario_SDL, ScenarioObject, presentation_parameter_ButtonCodesParameter, presentation_parameter_ScenarioNameParameter, NameLiteral, presentation_parameter_TimeParameter, StimulusEventParameter, SDL, PCL, presentation_parameter_Parameter, presentation_parameter_HeaderParameter, Parameter_, presentation_parameter_StimulusEventParameter, presentation_parameter_ActiveButtonsParameter, NumberLiteral, presentation_parameter_TextParameter, presentation_parameter_CaptionParameter, TextParameter, presentation_parameter_BitmapParameter, presentation_parameter_FilenameParameter, BitmapParameter, FilenameLiteral, presentation_parameter_TargetButtonParameter, presentation_parameter_CodeParameter, presentation_parameter_PictureParameter, presentation_parameter_BackgroundColorParameter, PictureParameter, presentation_stimulus_Stimulus, presentation_stimulus_StimulusEvent, presentation_stimulus_StimulusList, StimulusEvent, presentation_parameter_TrialParameter, presentation_general_CoordinateDefinition, presentation_general_NamedElement, presentation_picture_PictureStimulusEvent, picture_Picture, presentation_picture_PicturePart, presentation_picture_Bitmap, Graphic2D, FilenameParameter, presentation_stimulus_Trial, StimulusList, TrialParameter, presentation_stimulus_ScenarioObject, presentation_picture_Picture, Stimulus, picture_PicturePart, presentation_picture_Stimulus2D, PicturePart, CoordinateDefinition, presentation_picture_BitmapStimulus, Stimulus2D, picture_Bitmap, presentation_picture_Text, CaptionParameter, presentation_picture_Box, presentation_picture_Graphic2D, presentation_types_Type, presentation_types_BasicType, Type, presentation_types_Bool, BasicType, presentation_types_Int, presentation_types_Double, presentation_types_String, presentation_expressions_BooleanExpression, Expression, presentation_picture_BoxStimulus, picture_Box, presentation_picture_TextStimulus, picture_Text, presentation_sound_Sound, presentation_expressions_AtomExpression, presentation_expressions_BoolExpression, AtomExpression, BooleanLiteral, presentation_expressions_EqualsExpression, expressions_Expression, presentation_expressions_Expression, VariableInitializer, presentation_expressions_OrExpression, BooleanExpression, expressions_BooleanExpression, presentation_expressions_AndExpression, presentation_expressions_NotExpression, presentation_operators_EqualityOperator, presentation_operators_MultiplicativeOperator, presentation_operators_UnaryOperator, presentation_operators_AdditiveOperator, presentation_operators_Assignment, AssignmentOperator, presentation_operators_Greater, RelationOperator, presentation_operators_Less, presentation_expressions_StatementExpression, presentation_expressions_AssignmentExpression, expressions_StatementExpression, operators_AssignmentOperator, presentation_expressions_PrimaryExpression, presentation_operators_Operator, presentation_operators_AssignmentOperator, Operator, presentation_operators_RelationOperator, presentation_statements_Loop, statements_StatementList, presentation_operators_GreaterOrEqual, presentation_operators_LessOrEqual, presentation_operators_Equal, EqualityOperator, presentation_operators_NotEqual, presentation_statements_Statement, presentation_statements_StatementList, presentation_statements_Inclusion, Statement, presentation_statements_Assignment, presentation_statements_VariableDeclarator, common_VariableInitializer, presentation_common_VariableInitializer, presentation_common_NamedElement, presentation_common_Identifier, presentation_statements_VariableDeclaration, statements_ForInitializer, statements_ResourceAcquisition, types_Type, statements_VariableDeclarator, presentation_statements_DeclarationStatement, statements_VariableDeclaration, presentation_statements_ForInitializer, presentation_statements_ResourceAcquisition, presentation_program_Block, CoordinateType},
    associations={statement2, header3, parameter0, scenario_object1, number_literal9, name_literal11, sdl4, pcl6, number_literal8, text_literal19, number_literal12, number_literal14, text_literal16, number_literal17, stimulus_event_parameter22, stimulus_event23, filename_literal21, picture_parameter28, picture30, stimulus_list24, trial_parameter25, picture_part27, x_definition35, y_definition36, bitmap39, filename_parameter31, caption32, text_parameter33, box40, text41, value47, arguments48, argument42, argument43, argument45, assignmentOperator49, expression50, expression55, init57, body58, condition61, statement53, variableInitializer68, type64, variableDeclarator65, variableDeclaration67, statement69},
    generalizations={gen_presentation_literal_GeneralLiteral_Literal, gen_presentation_literal_BooleanLiteral_GeneralLiteral, gen_presentation_literal_NameLiteral_TextLiteral, gen_presentation_literal_FilenameLiteral_TextLiteral, gen_presentation_literal_NumericLiteral_Literal, gen_presentation_literal_NumberLiteral_NumericLiteral, gen_presentation_scenario_PCL_ScenarioFile, gen_presentation_scenario_Scenario_NamedElement, gen_presentation_literal_TextLiteral_GeneralLiteral, gen_presentation_scenario_Header_ScenarioFile, gen_presentation_scenario_SDL_ScenarioFile, gen_presentation_parameter_ButtonCodesParameter_HeaderParameter, gen_presentation_parameter_ScenarioNameParameter_HeaderParameter, gen_presentation_parameter_TimeParameter_StimulusEventParameter, gen_presentation_parameter_HeaderParameter_Parameter, gen_presentation_parameter_StimulusEventParameter_Parameter, gen_presentation_parameter_ActiveButtonsParameter_HeaderParameter, gen_presentation_parameter_TextParameter_Parameter, gen_presentation_parameter_CaptionParameter_TextParameter, gen_presentation_parameter_FilenameParameter_BitmapParameter, gen_presentation_parameter_TargetButtonParameter_StimulusEventParameter, gen_presentation_parameter_CodeParameter_StimulusEventParameter, gen_presentation_parameter_PictureParameter_Parameter, gen_presentation_parameter_BackgroundColorParameter_PictureParameter, gen_presentation_stimulus_Stimulus_ScenarioObject, gen_presentation_stimulus_StimulusEvent_ScenarioObject, gen_presentation_parameter_TrialParameter_Parameter, gen_presentation_picture_PictureStimulusEvent_StimulusEvent, gen_presentation_picture_PicturePart_ScenarioObject, gen_presentation_picture_Bitmap_Graphic2D, gen_presentation_stimulus_Trial_ScenarioObject, gen_presentation_stimulus_ScenarioObject_NamedElement, gen_presentation_picture_Picture_Stimulus, gen_presentation_picture_Stimulus2D_PicturePart, gen_presentation_picture_BitmapStimulus_Stimulus2D, gen_presentation_picture_Text_Graphic2D, gen_presentation_picture_Box_Graphic2D, gen_presentation_picture_Graphic2D_ScenarioObject, gen_presentation_types_BasicType_Type, gen_presentation_types_Bool_BasicType, gen_presentation_types_Int_BasicType, gen_presentation_types_Double_BasicType, gen_presentation_types_String_BasicType, gen_presentation_expressions_BooleanExpression_Expression, gen_presentation_picture_BoxStimulus_Stimulus2D, gen_presentation_picture_TextStimulus_Stimulus2D, gen_presentation_sound_Sound_Stimulus, gen_presentation_expressions_AtomExpression_BooleanExpression, gen_presentation_expressions_BoolExpression_AtomExpression, gen_presentation_expressions_EqualsExpression_AtomExpression, gen_presentation_expressions_Expression_VariableInitializer, gen_presentation_expressions_OrExpression_BooleanExpression, gen_presentation_expressions_AndExpression_BooleanExpression, gen_presentation_expressions_NotExpression_BooleanExpression, gen_presentation_operators_EqualityOperator_Operator, gen_presentation_operators_MultiplicativeOperator_Operator, gen_presentation_operators_UnaryOperator_Operator, gen_presentation_operators_AdditiveOperator_Operator, gen_presentation_operators_Assignment_AssignmentOperator, gen_presentation_operators_Greater_RelationOperator, gen_presentation_expressions_AssignmentExpression_expressions_Expression, gen_presentation_expressions_AssignmentExpression_expressions_StatementExpression, gen_presentation_operators_AssignmentOperator_Operator, gen_presentation_operators_RelationOperator_Operator, gen_presentation_statements_Loop_Statement, gen_presentation_operators_Less_RelationOperator, gen_presentation_operators_GreaterOrEqual_RelationOperator, gen_presentation_operators_LessOrEqual_RelationOperator, gen_presentation_operators_Equal_EqualityOperator, gen_presentation_operators_NotEqual_EqualityOperator, gen_presentation_statements_Inclusion_Statement, gen_presentation_statements_Assignment_Statement, gen_presentation_statements_VariableDeclarator_NamedElement, gen_presentation_common_Identifier_NamedElement, gen_presentation_statements_VariableDeclaration_statements_ForInitializer, gen_presentation_statements_VariableDeclaration_statements_ResourceAcquisition, gen_presentation_statements_DeclarationStatement_Statement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)