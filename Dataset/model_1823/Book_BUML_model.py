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
book_Book = Class(name="book::Book")
book_Page = Class(name="book::Page")
book_Layer = Class(name="book::Layer")
Page = Class(name="Page")
book_Splash = Class(name="book::Splash")
book_Action = Class(name="book::Action", is_abstract=True)
book_Control = Class(name="book::Control")
book_Node = Class(name="book::Node", is_abstract=True)
book_Shape = Class(name="book::Shape")
Node = Class(name="Node")
book_Label = Class(name="book::Label")
book_OpenPage = Class(name="book::OpenPage")
Action = Class(name="Action")
book_Group = Class(name="book::Group")
Control = Class(name="Control")
book_ImageFlash = Class(name="book::ImageFlash")
book_Animation = Class(name="book::Animation", is_abstract=True)
book_Media = Class(name="book::Media")
book_JSAction = Class(name="book::JSAction")
book_Fade = Class(name="book::Fade")
Animation = Class(name="Animation")
book_Move = Class(name="book::Move")
book_Rotation = Class(name="book::Rotation")

# book_Book class attributes and methods
book_Book_title: Property = Property(name="title", type=StringType)
book_Book_author: Property = Property(name="author", type=StringType)
book_Book_version: Property = Property(name="version", type=StringType)
book_Book_description: Property = Property(name="description", type=StringType)
book_Book_bookId: Property = Property(name="bookId", type=StringType)
book_Book_resolution: Property = Property(name="resolution", type=StringType)
book_Book.attributes={book_Book_bookId, book_Book_author, book_Book_description, book_Book_version, book_Book_resolution, book_Book_title}

# book_Page class attributes and methods
book_Page_name: Property = Property(name="name", type=StringType)
book_Page.attributes={book_Page_name}

# book_Layer class attributes and methods
book_Layer_visible: Property = Property(name="visible", type=BooleanType)
book_Layer.attributes={book_Layer_visible}

# Page class attributes and methods

# book_Splash class attributes and methods
book_Splash_duration: Property = Property(name="duration", type=IntegerType)
book_Splash.attributes={book_Splash_duration}

# book_Action class attributes and methods

# book_Control class attributes and methods
book_Control_image: Property = Property(name="image", type=StringType)
book_Control_sound: Property = Property(name="sound", type=StringType)
book_Control.attributes={book_Control_sound, book_Control_image}

# book_Node class attributes and methods
book_Node_enable: Property = Property(name="enable", type=BooleanType)
book_Node_opacity: Property = Property(name="opacity", type=FloatType)
book_Node_background: Property = Property(name="background", type=StringType)
book_Node_foreground: Property = Property(name="foreground", type=StringType)
book_Node_bounds: Property = Property(name="bounds", type=StringType)
book_Node.attributes={book_Node_enable, book_Node_background, book_Node_foreground, book_Node_opacity, book_Node_bounds}

# book_Shape class attributes and methods
book_Shape_lineWidth: Property = Property(name="lineWidth", type=IntegerType)
book_Shape_points: Property = Property(name="points", type=StringType)
book_Shape.attributes={book_Shape_lineWidth, book_Shape_points}

# Node class attributes and methods

# book_Label class attributes and methods
book_Label_text: Property = Property(name="text", type=StringType)
book_Label_font: Property = Property(name="font", type=StringType)
book_Label.attributes={book_Label_text, book_Label_font}

# book_OpenPage class attributes and methods

# Action class attributes and methods

# book_Group class attributes and methods

# Control class attributes and methods

# book_ImageFlash class attributes and methods
book_ImageFlash_images: Property = Property(name="images", type=StringType)
book_ImageFlash_duration: Property = Property(name="duration", type=IntegerType)
book_ImageFlash.attributes={book_ImageFlash_images, book_ImageFlash_duration}

# book_Animation class attributes and methods
book_Animation_duration: Property = Property(name="duration", type=FloatType)
book_Animation_delay: Property = Property(name="delay", type=FloatType)
book_Animation_autoReverse: Property = Property(name="autoReverse", type=BooleanType)
book_Animation_repeat: Property = Property(name="repeat", type=IntegerType)
book_Animation.attributes={book_Animation_autoReverse, book_Animation_delay, book_Animation_duration, book_Animation_repeat}

# book_Media class attributes and methods
book_Media_url: Property = Property(name="url", type=StringType)
book_Media_autoPlay: Property = Property(name="autoPlay", type=BooleanType)
book_Media_duration: Property = Property(name="duration", type=IntegerType)
book_Media_repeat: Property = Property(name="repeat", type=IntegerType)
book_Media.attributes={book_Media_duration, book_Media_autoPlay, book_Media_repeat, book_Media_url}

# book_JSAction class attributes and methods
book_JSAction_javaScript: Property = Property(name="javaScript", type=StringType)
book_JSAction.attributes={book_JSAction_javaScript}

# book_Fade class attributes and methods
book_Fade_fromValue: Property = Property(name="fromValue", type=FloatType)
book_Fade_toValue: Property = Property(name="toValue", type=FloatType)
book_Fade.attributes={book_Fade_fromValue, book_Fade_toValue}

# Animation class attributes and methods

# book_Move class attributes and methods
book_Move_fromLocation: Property = Property(name="fromLocation", type=StringType)
book_Move_toLocation: Property = Property(name="toLocation", type=StringType)
book_Move.attributes={book_Move_fromLocation, book_Move_toLocation}

# book_Rotation class attributes and methods
book_Rotation_toAngle: Property = Property(name="toAngle", type=FloatType)
book_Rotation_fromAngle: Property = Property(name="fromAngle", type=FloatType)
book_Rotation.attributes={book_Rotation_fromAngle, book_Rotation_toAngle}

# Relationships
layers6: BinaryAssociation = BinaryAssociation(
    name="layers6",
    ends={
        Property(name="book_Layer", type=book_Page, multiplicity=Multiplicity(1, 1)),
        Property(name="book_Page7", type=book_Layer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pages0: BinaryAssociation = BinaryAssociation(
    name="pages0",
    ends={
        Property(name="book_Page", type=book_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="book_Book", type=book_Page, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
splash1: BinaryAssociation = BinaryAssociation(
    name="splash1",
    ends={
        Property(name="book_Splash", type=book_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="book_Book2", type=book_Splash, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
main3: BinaryAssociation = BinaryAssociation(
    name="main3",
    ends={
        Property(name="book_Page5", type=book_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="book_Book4", type=book_Page, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
onExposed10: BinaryAssociation = BinaryAssociation(
    name="onExposed10",
    ends={
        Property(name="book_Action", type=book_Control, multiplicity=Multiplicity(1, 1)),
        Property(name="book_Control11", type=book_Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
onTouched12: BinaryAssociation = BinaryAssociation(
    name="onTouched12",
    ends={
        Property(name="book_Action14", type=book_Control, multiplicity=Multiplicity(1, 1)),
        Property(name="book_Control13", type=book_Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
control8: BinaryAssociation = BinaryAssociation(
    name="control8",
    ends={
        Property(name="book_Control", type=book_Layer, multiplicity=Multiplicity(1, 1)),
        Property(name="book_Layer9", type=book_Control, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
page20: BinaryAssociation = BinaryAssociation(
    name="page20",
    ends={
        Property(name="book_Page21", type=book_OpenPage, multiplicity=Multiplicity(1, 1)),
        Property(name="book_OpenPage", type=book_Page, multiplicity=Multiplicity(0, 1))
    }
)
children15: BinaryAssociation = BinaryAssociation(
    name="children15",
    ends={
        Property(name="book_Node", type=book_Group, multiplicity=Multiplicity(1, 1)),
        Property(name="book_Group", type=book_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
out16: BinaryAssociation = BinaryAssociation(
    name="out16",
    ends={
        Property(name="book_Animation", type=book_ImageFlash, multiplicity=Multiplicity(1, 1)),
        Property(name="book_ImageFlash", type=book_Animation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
in17: BinaryAssociation = BinaryAssociation(
    name="in17",
    ends={
        Property(name="book_Animation19", type=book_ImageFlash, multiplicity=Multiplicity(1, 1)),
        Property(name="book_ImageFlash18", type=book_Animation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_book_Splash_Page = Generalization(general=Page, specific=book_Splash)
gen_book_Shape_Node = Generalization(general=Node, specific=book_Shape)
gen_book_Control_Node = Generalization(general=Node, specific=book_Control)
gen_book_Media_Control = Generalization(general=Control, specific=book_Media)
gen_book_Label_Control = Generalization(general=Control, specific=book_Label)
gen_book_OpenPage_Action = Generalization(general=Action, specific=book_OpenPage)
gen_book_Group_Control = Generalization(general=Control, specific=book_Group)
gen_book_ImageFlash_Control = Generalization(general=Control, specific=book_ImageFlash)
gen_book_JSAction_Action = Generalization(general=Action, specific=book_JSAction)
gen_book_Animation_Action = Generalization(general=Action, specific=book_Animation)
gen_book_Fade_Animation = Generalization(general=Animation, specific=book_Fade)
gen_book_Move_Animation = Generalization(general=Animation, specific=book_Move)
gen_book_Rotation_Animation = Generalization(general=Animation, specific=book_Rotation)

# Domain Model
domain_model = DomainModel(
    name="book",
    types={book_Book, book_Page, book_Layer, Page, book_Splash, book_Action, book_Control, book_Node, book_Shape, Node, book_Label, book_OpenPage, Action, book_Group, Control, book_ImageFlash, book_Animation, book_Media, book_JSAction, book_Fade, Animation, book_Move, book_Rotation},
    associations={layers6, pages0, splash1, main3, onExposed10, onTouched12, control8, page20, children15, out16, in17},
    generalizations={gen_book_Splash_Page, gen_book_Shape_Node, gen_book_Control_Node, gen_book_Media_Control, gen_book_Label_Control, gen_book_OpenPage_Action, gen_book_Group_Control, gen_book_ImageFlash_Control, gen_book_JSAction_Action, gen_book_Animation_Action, gen_book_Fade_Animation, gen_book_Move_Animation, gen_book_Rotation_Animation},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)