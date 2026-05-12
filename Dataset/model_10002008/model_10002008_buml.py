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

# Classes
snake_Backgrounds = Class(name="snake_Backgrounds")
snake_GameScene = Class(name="snake_GameScene")
snake_TAdapter = Class(name="snake_TAdapter")
snake_Main = Class(name="snake_Main")
genmymodelreverse_java_awt_Image = Class(name="genmymodelreverse_java_awt_Image", is_abstract=True)
genmymodelreverse_java_io_IOException = Class(name="genmymodelreverse_java_io_IOException")
genmymodelreverse_java_nio_charset_Charset = Class(name="genmymodelreverse_java_nio_charset_Charset", is_abstract=True)
genmymodelreverse_java_awt_Graphics = Class(name="genmymodelreverse_java_awt_Graphics", is_abstract=True)
genmymodelreverse_java_awt_event_ActionEvent = Class(name="genmymodelreverse_java_awt_event_ActionEvent")
genmymodelreverse_java_awt_event_ActionListener_Interface = Class(name="genmymodelreverse_java_awt_event_ActionListener_Interface", is_abstract=True)
genmymodelreverse_java_awt_event_KeyAdapter = Class(name="genmymodelreverse_java_awt_event_KeyAdapter", is_abstract=True)
genmymodelreverse_java_awt_event_KeyEvent = Class(name="genmymodelreverse_java_awt_event_KeyEvent")
genmymodelreverse_javax_swing_JPanel = Class(name="genmymodelreverse_javax_swing_JPanel")
genmymodelreverse_javax_swing_Timer = Class(name="genmymodelreverse_javax_swing_Timer")
genmymodelreverse_javax_swing_JFrame = Class(name="genmymodelreverse_javax_swing_JFrame")

# snake_Backgrounds class attributes and methods
snake_Backgrounds_backgrounds: Property = Property(name="backgrounds", type=genmymodelreverse_java_awt_Image)
snake_Backgrounds.attributes={snake_Backgrounds_backgrounds}

# snake_GameScene class attributes and methods
snake_GameScene_serialVersionUID: Property = Property(name="serialVersionUID", type=IntegerType)
snake_GameScene_B_WIDTH: Property = Property(name="B_WIDTH", type=IntegerType)
snake_GameScene_B_HEIGHT: Property = Property(name="B_HEIGHT", type=IntegerType)
snake_GameScene_DOT_SIZE: Property = Property(name="DOT_SIZE", type=IntegerType)
snake_GameScene_ALL_DOTS: Property = Property(name="ALL_DOTS", type=IntegerType)
snake_GameScene_RAND_POS: Property = Property(name="RAND_POS", type=IntegerType)
snake_GameScene_DELAY: Property = Property(name="DELAY", type=IntegerType)
snake_GameScene_x: Property = Property(name="x", type=StringType)
snake_GameScene_y: Property = Property(name="y", type=StringType)
snake_GameScene_bodyLength: Property = Property(name="bodyLength", type=IntegerType)
snake_GameScene_apple_x: Property = Property(name="apple_x", type=IntegerType)
snake_GameScene_apple_y: Property = Property(name="apple_y", type=IntegerType)
snake_GameScene_myScore: Property = Property(name="myScore", type=IntegerType)
snake_GameScene_level: Property = Property(name="level", type=IntegerType)
snake_GameScene_leftDirection: Property = Property(name="leftDirection", type=BooleanType)
snake_GameScene_rightDirection: Property = Property(name="rightDirection", type=BooleanType)
snake_GameScene_upDirection: Property = Property(name="upDirection", type=BooleanType)
snake_GameScene_downDirection: Property = Property(name="downDirection", type=BooleanType)
snake_GameScene_inGame: Property = Property(name="inGame", type=BooleanType)
snake_GameScene_timer: Property = Property(name="timer", type=genmymodelreverse_javax_swing_Timer)
snake_GameScene_bodySegment: Property = Property(name="bodySegment", type=genmymodelreverse_java_awt_Image)
snake_GameScene_apple: Property = Property(name="apple", type=genmymodelreverse_java_awt_Image)
snake_GameScene_head: Property = Property(name="head", type=genmymodelreverse_java_awt_Image)
snake_GameScene_bg: Property = Property(name="bg", type=genmymodelreverse_java_awt_Image)
snake_GameScene.attributes={snake_GameScene_upDirection, snake_GameScene_RAND_POS, snake_GameScene_downDirection, snake_GameScene_bodyLength, snake_GameScene_B_HEIGHT, snake_GameScene_inGame, snake_GameScene_y, snake_GameScene_timer, snake_GameScene_apple_x, snake_GameScene_bodySegment, snake_GameScene_DELAY, snake_GameScene_serialVersionUID, snake_GameScene_apple_y, snake_GameScene_DOT_SIZE, snake_GameScene_apple, snake_GameScene_myScore, snake_GameScene_ALL_DOTS, snake_GameScene_B_WIDTH, snake_GameScene_level, snake_GameScene_head, snake_GameScene_x, snake_GameScene_bg, snake_GameScene_leftDirection, snake_GameScene_rightDirection}

# snake_TAdapter class attributes and methods

# snake_Main class attributes and methods
snake_Main_serialVersionUID: Property = Property(name="serialVersionUID", type=IntegerType)
snake_Main.attributes={snake_Main_serialVersionUID}

# genmymodelreverse_java_awt_Image class attributes and methods

# genmymodelreverse_java_io_IOException class attributes and methods

# genmymodelreverse_java_nio_charset_Charset class attributes and methods

# genmymodelreverse_java_awt_Graphics class attributes and methods

# genmymodelreverse_java_awt_event_ActionEvent class attributes and methods

# genmymodelreverse_java_awt_event_ActionListener_Interface class attributes and methods

# genmymodelreverse_java_awt_event_KeyAdapter class attributes and methods

# genmymodelreverse_java_awt_event_KeyEvent class attributes and methods

# genmymodelreverse_javax_swing_JPanel class attributes and methods

# genmymodelreverse_javax_swing_Timer class attributes and methods

# genmymodelreverse_javax_swing_JFrame class attributes and methods

# Domain Model
domain_model = DomainModel(
    name="_j9tz8GIVEemLuYD1bjHUeQ",
    types={snake_Backgrounds, snake_GameScene, snake_TAdapter, snake_Main, genmymodelreverse_java_awt_Image, genmymodelreverse_java_io_IOException, genmymodelreverse_java_nio_charset_Charset, genmymodelreverse_java_awt_Graphics, genmymodelreverse_java_awt_event_ActionEvent, genmymodelreverse_java_awt_event_ActionListener_Interface, genmymodelreverse_java_awt_event_KeyAdapter, genmymodelreverse_java_awt_event_KeyEvent, genmymodelreverse_javax_swing_JPanel, genmymodelreverse_javax_swing_Timer, genmymodelreverse_javax_swing_JFrame},
    associations={},
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