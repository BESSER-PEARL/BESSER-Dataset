from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class CoordinateType(Enum):
    TOP_Y = "TOP_Y"
    X = "X"
    Y = "Y"
    CENTER_X = "CENTER_X"
    CENTER_Y = "CENTER_Y"
    LEFT_X = "LEFT_X"


############################################
# Definition of Classes
############################################

class presentation_program_Block:

    pass
class presentation_statements_ResourceAcquisition(ABC):

    pass
class presentation_statements_ForInitializer(ABC):

    pass
class statements_VariableDeclaration:

    pass
class statements_VariableDeclarator:

    pass
class types_Type:

    pass
class statements_ResourceAcquisition:

    pass
class statements_ForInitializer:

    pass
class presentation_statements_VariableDeclaration(statements_ResourceAcquisition, statements_ForInitializer):

    pass
class presentation_common_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class presentation_common_VariableInitializer(ABC):

    pass
class common_VariableInitializer:

    pass
class Statement:

    pass
class presentation_statements_Assignment(Statement):

    pass
class presentation_statements_DeclarationStatement(Statement):

    pass
class presentation_statements_Inclusion(Statement):

    pass
class presentation_statements_StatementList:

    pass
class presentation_statements_Statement(ABC):

    pass
class EqualityOperator:

    pass
class presentation_operators_NotEqual(EqualityOperator):

    pass
class presentation_operators_Equal(EqualityOperator):

    pass
class statements_StatementList:

    pass
class presentation_statements_Loop(Statement):

    pass
class Operator:

    pass
class presentation_operators_RelationOperator(Operator):

    pass
class presentation_operators_AssignmentOperator(Operator):

    pass
class presentation_operators_Operator(ABC):

    pass
class presentation_expressions_PrimaryExpression(ABC):

    pass
class operators_AssignmentOperator:

    pass
class expressions_StatementExpression:

    pass
class presentation_expressions_StatementExpression(ABC):

    pass
class RelationOperator:

    pass
class presentation_operators_LessOrEqual(RelationOperator):

    pass
class presentation_operators_GreaterOrEqual(RelationOperator):

    pass
class presentation_operators_Less(RelationOperator):

    pass
class presentation_operators_Greater(RelationOperator):

    pass
class AssignmentOperator:

    pass
class presentation_operators_Assignment(AssignmentOperator):

    pass
class presentation_operators_AdditiveOperator(Operator):

    pass
class presentation_operators_UnaryOperator(Operator):

    pass
class presentation_operators_MultiplicativeOperator(Operator):

    pass
class presentation_operators_EqualityOperator(Operator):

    pass
class expressions_BooleanExpression:

    pass
class BooleanExpression:

    pass
class presentation_expressions_AndExpression(BooleanExpression):

    pass
class presentation_expressions_NotExpression(BooleanExpression):

    pass
class presentation_expressions_OrExpression(BooleanExpression):

    pass
class VariableInitializer:

    pass
class presentation_expressions_Expression(VariableInitializer):

    pass
class expressions_Expression:

    pass
class presentation_expressions_AssignmentExpression(expressions_Expression, expressions_StatementExpression):

    pass
class BooleanLiteral:

    pass
class AtomExpression:

    pass
class presentation_expressions_EqualsExpression(AtomExpression):

    pass
class presentation_expressions_BoolExpression(AtomExpression):

    pass
class presentation_expressions_AtomExpression(BooleanExpression):

    pass
class picture_Text:

    pass
class picture_Box:

    pass
class Expression:

    pass
class presentation_expressions_BooleanExpression(Expression):

    pass
class BasicType:

    pass
class presentation_types_Int(BasicType):

    pass
class presentation_types_String(BasicType):

    pass
class presentation_types_Double(BasicType):

    pass
class presentation_types_Bool(BasicType):

    pass
class Type:

    pass
class presentation_types_BasicType(Type):

    pass
class presentation_types_Type(ABC):

    pass
class CaptionParameter:

    pass
class picture_Bitmap:

    pass
class Stimulus2D:

    pass
class presentation_picture_TextStimulus(Stimulus2D):

    pass
class presentation_picture_BoxStimulus(Stimulus2D):

    pass
class presentation_picture_BitmapStimulus(Stimulus2D):

    pass
class CoordinateDefinition:

    pass
class PicturePart:

    pass
class presentation_picture_Stimulus2D(PicturePart):

    pass
class picture_PicturePart:

    pass
class Stimulus:

    pass
class presentation_sound_Sound(Stimulus):

    pass
class presentation_picture_Picture(Stimulus):

    pass
class TrialParameter:

    pass
class StimulusList:

    pass
class FilenameParameter:

    pass
class Graphic2D:

    pass
class presentation_picture_Text(Graphic2D):

    pass
class presentation_picture_Box(Graphic2D):

    pass
class presentation_picture_Bitmap(Graphic2D):

    def __init__(self, bitmap_parameters: str, presentation_picture_Bitmap: "FilenameParameter" = None):
        self.bitmap_parameters = bitmap_parameters
        self.presentation_picture_Bitmap = presentation_picture_Bitmap
        
    @property
    def bitmap_parameters(self) -> str:
        return self.__bitmap_parameters

    @bitmap_parameters.setter
    def bitmap_parameters(self, bitmap_parameters: str):
        self.__bitmap_parameters = bitmap_parameters

    @property
    def presentation_picture_Bitmap(self):
        return self.__presentation_picture_Bitmap

    @presentation_picture_Bitmap.setter
    def presentation_picture_Bitmap(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_picture_Bitmap__presentation_picture_Bitmap", None)
        self.__presentation_picture_Bitmap = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FilenameParameter"):
                opp_val = getattr(old_value, "FilenameParameter", None)
                if opp_val == self:
                    setattr(old_value, "FilenameParameter", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FilenameParameter"):
                opp_val = getattr(value, "FilenameParameter", None)
                setattr(value, "FilenameParameter", self)

class picture_Picture:

    pass
class presentation_general_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class presentation_general_CoordinateDefinition:

    def __init__(self, coordinate: str, type: str, right_bottom: str):
        self.coordinate = coordinate
        self.type = type
        self.right_bottom = right_bottom
        
    @property
    def coordinate(self) -> str:
        return self.__coordinate

    @coordinate.setter
    def coordinate(self, coordinate: str):
        self.__coordinate = coordinate

    @property
    def right_bottom(self) -> str:
        return self.__right_bottom

    @right_bottom.setter
    def right_bottom(self, right_bottom: str):
        self.__right_bottom = right_bottom

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

class StimulusEvent:

    pass
class presentation_picture_PictureStimulusEvent(StimulusEvent):

    pass
class presentation_stimulus_StimulusList:

    pass
class PictureParameter:

    pass
class presentation_parameter_BackgroundColorParameter(PictureParameter):

    pass
class FilenameLiteral:

    pass
class BitmapParameter:

    pass
class presentation_parameter_FilenameParameter(BitmapParameter):

    pass
class presentation_parameter_BitmapParameter(ABC):

    pass
class TextParameter:

    pass
class presentation_parameter_CaptionParameter(TextParameter):

    pass
class NumberLiteral:

    pass
class Parameter:

    pass
class presentation_parameter_PictureParameter(Parameter):

    pass
class presentation_parameter_StimulusEventParameter(Parameter):

    pass
class presentation_parameter_TrialParameter(Parameter):

    pass
class presentation_parameter_TextParameter(Parameter):

    pass
class presentation_parameter_HeaderParameter(Parameter):

    pass
class presentation_parameter_Parameter(ABC):

    pass
class PCL:

    pass
class SDL:

    pass
class StimulusEventParameter:

    pass
class presentation_parameter_TargetButtonParameter(StimulusEventParameter):

    pass
class presentation_parameter_CodeParameter(StimulusEventParameter):

    pass
class presentation_parameter_TimeParameter(StimulusEventParameter):

    pass
class NameLiteral:

    pass
class ScenarioObject:

    pass
class presentation_stimulus_Trial(ScenarioObject):

    pass
class presentation_picture_PicturePart(ScenarioObject):

    pass
class presentation_stimulus_StimulusEvent(ScenarioObject):

    pass
class presentation_stimulus_Stimulus(ScenarioObject):

    pass
class presentation_picture_Graphic2D(ScenarioObject):

    pass
class HeaderParameter:

    pass
class presentation_parameter_ActiveButtonsParameter(HeaderParameter):

    pass
class presentation_parameter_ButtonCodesParameter(HeaderParameter):

    pass
class presentation_parameter_ScenarioNameParameter(HeaderParameter):

    pass
class ScenarioFile:

    pass
class presentation_scenario_SDL(ScenarioFile):

    pass
class presentation_scenario_Header(ScenarioFile):

    pass
class presentation_scenario_ScenarioFile(ABC):

    pass
class Header:

    pass
class NamedElement:

    pass
class presentation_stimulus_ScenarioObject(NamedElement):

    pass
class presentation_statements_VariableDeclarator(NamedElement):

    pass
class presentation_common_Identifier(NamedElement):

    pass
class presentation_scenario_Scenario(NamedElement):

    pass
class statements_Statement:

    pass
class presentation_scenario_PCL(ScenarioFile):

    pass
class NumericLiteral:

    pass
class presentation_literal_NumberLiteral(NumericLiteral):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class Literal:

    pass
class presentation_literal_NumericLiteral(Literal):

    pass
class presentation_literal_Literal(ABC):

    pass
class TextLiteral:

    pass
class presentation_literal_FilenameLiteral(TextLiteral):

    pass
class presentation_literal_NameLiteral(TextLiteral):

    pass
class GeneralLiteral:

    pass
class presentation_literal_TextLiteral(GeneralLiteral):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class presentation_literal_BooleanLiteral(GeneralLiteral):

    def __init__(self, value: bool):
        self.value = value
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

class presentation_literal_GeneralLiteral(Literal):

    pass