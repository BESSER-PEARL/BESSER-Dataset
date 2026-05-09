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
EventType: Enumeration = Enumeration(
    name="EventType",
    literals={
            EnumerationLiteral(name="onError"),
			EnumerationLiteral(name="onLoad"),
			EnumerationLiteral(name="workaround"),
			EnumerationLiteral(name="onSubmit")
    }
)

InputType: Enumeration = Enumeration(
    name="InputType",
    literals={
            EnumerationLiteral(name="workaround"),
			EnumerationLiteral(name="text"),
			EnumerationLiteral(name="radio"),
			EnumerationLiteral(name="checkbox")
    }
)

HTMLTag: Enumeration = Enumeration(
    name="HTMLTag",
    literals={
            EnumerationLiteral(name="workaround"),
			EnumerationLiteral(name="button"),
			EnumerationLiteral(name="input"),
			EnumerationLiteral(name="a"),
			EnumerationLiteral(name="form"),
			EnumerationLiteral(name="img"),
			EnumerationLiteral(name="p")
    }
)

MethodType: Enumeration = Enumeration(
    name="MethodType",
    literals={
            EnumerationLiteral(name="workaround"),
			EnumerationLiteral(name="get"),
			EnumerationLiteral(name="post"),
			EnumerationLiteral(name="put"),
			EnumerationLiteral(name="patch"),
			EnumerationLiteral(name="head"),
			EnumerationLiteral(name="delete")
    }
)

ButtonType: Enumeration = Enumeration(
    name="ButtonType",
    literals={
            EnumerationLiteral(name="workaround"),
			EnumerationLiteral(name="button"),
			EnumerationLiteral(name="submit"),
			EnumerationLiteral(name="reset")
    }
)

TargetType: Enumeration = Enumeration(
    name="TargetType",
    literals={
            EnumerationLiteral(name="workaround"),
			EnumerationLiteral(name="self"),
			EnumerationLiteral(name="blank"),
			EnumerationLiteral(name="parent"),
			EnumerationLiteral(name="top"),
			EnumerationLiteral(name="framename")
    }
)

# Classes
PHPMVC_coreMVC_Application = Class(name="PHPMVC_coreMVC_Application")
PHPMVC_coreMVC_PackageController = Class(name="PHPMVC_coreMVC_PackageController")
Controller = Class(name="Controller")
PHPMVC_coreMVC_MVCClass = Class(name="PHPMVC_coreMVC_MVCClass", is_abstract=True)
Attribute = Class(name="Attribute")
PHPMVC_coreMVC_Attribute = Class(name="PHPMVC_coreMVC_Attribute")
PHPMVC_coreMVC_Model = Class(name="PHPMVC_coreMVC_Model")
MVCClass = Class(name="MVCClass")
Identifier = Class(name="Identifier")
PHPMVC_coreMVC_View = Class(name="PHPMVC_coreMVC_View")
ViewComponent = Class(name="ViewComponent")
PHPMVC_coreMVC_Controller = Class(name="PHPMVC_coreMVC_Controller")
PackageModel = Class(name="PackageModel")
PackageView = Class(name="PackageView")
PackageController = Class(name="PackageController")
PHPMVC_coreMVC_PackageModel = Class(name="PHPMVC_coreMVC_PackageModel")
Model = Class(name="Model")
PHPMVC_coreMVC_PackageView = Class(name="PHPMVC_coreMVC_PackageView")
View = Class(name="View")
PHPMVC_coreMVC_Identifier = Class(name="PHPMVC_coreMVC_Identifier")
PHPMVC_extPHP_HTMLElement = Class(name="PHPMVC_extPHP_HTMLElement", is_abstract=True)
HTMLElement = Class(name="HTMLElement")
PHPMVC_extPHP_Form = Class(name="PHPMVC_extPHP_Form")
PHPMVC_extPHP_Button = Class(name="PHPMVC_extPHP_Button")
PHPMVC_extPHP_Text = Class(name="PHPMVC_extPHP_Text")
Method_ = Class(name="Method")
PHPMVC_coreMVC_Method = Class(name="PHPMVC_coreMVC_Method")
PHPMVC_coreMVC_ViewComponent = Class(name="PHPMVC_coreMVC_ViewComponent", is_abstract=True)
Event = Class(name="Event")
PHPMVC_coreMVC_Event = Class(name="PHPMVC_coreMVC_Event")
PHPMVC_extPHP_Anchor = Class(name="PHPMVC_extPHP_Anchor")
PHPMVC_extPHP_Image = Class(name="PHPMVC_extPHP_Image")
PHPMVC_extPHP_Input = Class(name="PHPMVC_extPHP_Input", is_abstract=True)
PHPMVC_extPHP_TextField = Class(name="PHPMVC_extPHP_TextField")
Input = Class(name="Input")
PHPMVC_extPHP_Checkbox = Class(name="PHPMVC_extPHP_Checkbox")
PHPMVC_extPHP_RadioButton = Class(name="PHPMVC_extPHP_RadioButton")

# PHPMVC_coreMVC_Application class attributes and methods
PHPMVC_coreMVC_Application_name: Property = Property(name="name", type=StringType)
PHPMVC_coreMVC_Application_routes: Property = Property(name="routes", type=StringType)
PHPMVC_coreMVC_Application_type: Property = Property(name="type", type=StringType)
PHPMVC_coreMVC_Application_locale: Property = Property(name="locale", type=StringType)
PHPMVC_coreMVC_Application.attributes={PHPMVC_coreMVC_Application_name, PHPMVC_coreMVC_Application_locale, PHPMVC_coreMVC_Application_routes, PHPMVC_coreMVC_Application_type}

# PHPMVC_coreMVC_PackageController class attributes and methods
PHPMVC_coreMVC_PackageController_name: Property = Property(name="name", type=StringType)
PHPMVC_coreMVC_PackageController.attributes={PHPMVC_coreMVC_PackageController_name}

# Controller class attributes and methods

# PHPMVC_coreMVC_MVCClass class attributes and methods
PHPMVC_coreMVC_MVCClass_name: Property = Property(name="name", type=StringType)
PHPMVC_coreMVC_MVCClass.attributes={PHPMVC_coreMVC_MVCClass_name}

# Attribute class attributes and methods

# PHPMVC_coreMVC_Attribute class attributes and methods
PHPMVC_coreMVC_Attribute_name: Property = Property(name="name", type=StringType)
PHPMVC_coreMVC_Attribute.attributes={PHPMVC_coreMVC_Attribute_name}

# PHPMVC_coreMVC_Model class attributes and methods

# MVCClass class attributes and methods

# Identifier class attributes and methods

# PHPMVC_coreMVC_View class attributes and methods

# ViewComponent class attributes and methods

# PHPMVC_coreMVC_Controller class attributes and methods

# PackageModel class attributes and methods

# PackageView class attributes and methods

# PackageController class attributes and methods

# PHPMVC_coreMVC_PackageModel class attributes and methods
PHPMVC_coreMVC_PackageModel_name: Property = Property(name="name", type=StringType)
PHPMVC_coreMVC_PackageModel.attributes={PHPMVC_coreMVC_PackageModel_name}

# Model class attributes and methods

# PHPMVC_coreMVC_PackageView class attributes and methods
PHPMVC_coreMVC_PackageView_name: Property = Property(name="name", type=StringType)
PHPMVC_coreMVC_PackageView.attributes={PHPMVC_coreMVC_PackageView_name}

# View class attributes and methods

# PHPMVC_coreMVC_Identifier class attributes and methods
PHPMVC_coreMVC_Identifier_isAutoincremental: Property = Property(name="isAutoincremental", type=BooleanType)
PHPMVC_coreMVC_Identifier.attributes={PHPMVC_coreMVC_Identifier_isAutoincremental}

# PHPMVC_extPHP_HTMLElement class attributes and methods
PHPMVC_extPHP_HTMLElement_tagName: Property = Property(name="tagName", type=StringType)
PHPMVC_extPHP_HTMLElement_isPairedTag: Property = Property(name="isPairedTag", type=BooleanType)
PHPMVC_extPHP_HTMLElement_isEmpty: Property = Property(name="isEmpty", type=BooleanType)
PHPMVC_extPHP_HTMLElement.attributes={PHPMVC_extPHP_HTMLElement_isPairedTag, PHPMVC_extPHP_HTMLElement_tagName, PHPMVC_extPHP_HTMLElement_isEmpty}

# HTMLElement class attributes and methods

# PHPMVC_extPHP_Form class attributes and methods
PHPMVC_extPHP_Form_action: Property = Property(name="action", type=StringType)
PHPMVC_extPHP_Form_method: Property = Property(name="method", type=StringType)
PHPMVC_extPHP_Form_target: Property = Property(name="target", type=StringType)
PHPMVC_extPHP_Form.attributes={PHPMVC_extPHP_Form_action, PHPMVC_extPHP_Form_method, PHPMVC_extPHP_Form_target}

# PHPMVC_extPHP_Button class attributes and methods
PHPMVC_extPHP_Button_disabled: Property = Property(name="disabled", type=BooleanType)
PHPMVC_extPHP_Button_type: Property = Property(name="type", type=StringType)
PHPMVC_extPHP_Button_content: Property = Property(name="content", type=StringType)
PHPMVC_extPHP_Button.attributes={PHPMVC_extPHP_Button_type, PHPMVC_extPHP_Button_disabled, PHPMVC_extPHP_Button_content}

# PHPMVC_extPHP_Text class attributes and methods
PHPMVC_extPHP_Text_language: Property = Property(name="language", type=StringType)
PHPMVC_extPHP_Text_content: Property = Property(name="content", type=StringType)
PHPMVC_extPHP_Text.attributes={PHPMVC_extPHP_Text_content, PHPMVC_extPHP_Text_language}

# Method class attributes and methods

# PHPMVC_coreMVC_Method class attributes and methods
PHPMVC_coreMVC_Method_name: Property = Property(name="name", type=StringType)
PHPMVC_coreMVC_Method.attributes={PHPMVC_coreMVC_Method_name}

# PHPMVC_coreMVC_ViewComponent class attributes and methods
PHPMVC_coreMVC_ViewComponent_name: Property = Property(name="name", type=StringType)
PHPMVC_coreMVC_ViewComponent.attributes={PHPMVC_coreMVC_ViewComponent_name}

# Event class attributes and methods

# PHPMVC_coreMVC_Event class attributes and methods
PHPMVC_coreMVC_Event_type: Property = Property(name="type", type=StringType)
PHPMVC_coreMVC_Event_handler: Property = Property(name="handler", type=StringType)
PHPMVC_coreMVC_Event.attributes={PHPMVC_coreMVC_Event_handler, PHPMVC_coreMVC_Event_type}

# PHPMVC_extPHP_Anchor class attributes and methods
PHPMVC_extPHP_Anchor_target: Property = Property(name="target", type=StringType)
PHPMVC_extPHP_Anchor_hypRef: Property = Property(name="hypRef", type=StringType)
PHPMVC_extPHP_Anchor_content: Property = Property(name="content", type=StringType)
PHPMVC_extPHP_Anchor.attributes={PHPMVC_extPHP_Anchor_hypRef, PHPMVC_extPHP_Anchor_target, PHPMVC_extPHP_Anchor_content}

# PHPMVC_extPHP_Image class attributes and methods
PHPMVC_extPHP_Image_source: Property = Property(name="source", type=StringType)
PHPMVC_extPHP_Image.attributes={PHPMVC_extPHP_Image_source}

# PHPMVC_extPHP_Input class attributes and methods
PHPMVC_extPHP_Input_type: Property = Property(name="type", type=StringType)
PHPMVC_extPHP_Input_value: Property = Property(name="value", type=StringType)
PHPMVC_extPHP_Input.attributes={PHPMVC_extPHP_Input_type, PHPMVC_extPHP_Input_value}

# PHPMVC_extPHP_TextField class attributes and methods

# Input class attributes and methods

# PHPMVC_extPHP_Checkbox class attributes and methods

# PHPMVC_extPHP_RadioButton class attributes and methods

# Relationships
controllers7: BinaryAssociation = BinaryAssociation(
    name="controllers7",
    ends={
        Property(name="Controller", type=PHPMVC_coreMVC_PackageController, multiplicity=Multiplicity(1, 1)),
        Property(name="PHPMVC_coreMVC_PackageController", type=Controller, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributes8: BinaryAssociation = BinaryAssociation(
    name="attributes8",
    ends={
        Property(name="Attribute", type=PHPMVC_coreMVC_MVCClass, multiplicity=Multiplicity(1, 1)),
        Property(name="PHPMVC_coreMVC_MVCClass", type=Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
primaryKeys9: BinaryAssociation = BinaryAssociation(
    name="primaryKeys9",
    ends={
        Property(name="Identifier", type=PHPMVC_coreMVC_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="PHPMVC_coreMVC_Model", type=Identifier, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
viewComponents10: BinaryAssociation = BinaryAssociation(
    name="viewComponents10",
    ends={
        Property(name="ViewComponent", type=PHPMVC_coreMVC_View, multiplicity=Multiplicity(1, 1)),
        Property(name="PHPMVC_coreMVC_View", type=ViewComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
innerViews11: BinaryAssociation = BinaryAssociation(
    name="innerViews11",
    ends={
        Property(name="View13", type=PHPMVC_coreMVC_View, multiplicity=Multiplicity(1, 1)),
        Property(name="PHPMVC_coreMVC_View12", type=View, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
aPackageModel0: BinaryAssociation = BinaryAssociation(
    name="aPackageModel0",
    ends={
        Property(name="PackageModel", type=PHPMVC_coreMVC_Application, multiplicity=Multiplicity(1, 1)),
        Property(name="PHPMVC_coreMVC_Application", type=PackageModel, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
aPackageView1: BinaryAssociation = BinaryAssociation(
    name="aPackageView1",
    ends={
        Property(name="PackageView", type=PHPMVC_coreMVC_Application, multiplicity=Multiplicity(1, 1)),
        Property(name="PHPMVC_coreMVC_Application2", type=PackageView, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
aPackageController3: BinaryAssociation = BinaryAssociation(
    name="aPackageController3",
    ends={
        Property(name="PackageController", type=PHPMVC_coreMVC_Application, multiplicity=Multiplicity(1, 1)),
        Property(name="PHPMVC_coreMVC_Application4", type=PackageController, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
models5: BinaryAssociation = BinaryAssociation(
    name="models5",
    ends={
        Property(name="Model", type=PHPMVC_coreMVC_PackageModel, multiplicity=Multiplicity(1, 1)),
        Property(name="PHPMVC_coreMVC_PackageModel", type=Model, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
views6: BinaryAssociation = BinaryAssociation(
    name="views6",
    ends={
        Property(name="View", type=PHPMVC_coreMVC_PackageView, multiplicity=Multiplicity(1, 1)),
        Property(name="PHPMVC_coreMVC_PackageView", type=View, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
htmlElements21: BinaryAssociation = BinaryAssociation(
    name="htmlElements21",
    ends={
        Property(name="HTMLElement", type=PHPMVC_extPHP_HTMLElement, multiplicity=Multiplicity(1, 1)),
        Property(name="PHPMVC_extPHP_HTMLElement", type=HTMLElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
methods14: BinaryAssociation = BinaryAssociation(
    name="methods14",
    ends={
        Property(name="Method", type=PHPMVC_coreMVC_Controller, multiplicity=Multiplicity(1, 1)),
        Property(name="PHPMVC_coreMVC_Controller", type=Method_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inParameters15: BinaryAssociation = BinaryAssociation(
    name="inParameters15",
    ends={
        Property(name="Attribute16", type=PHPMVC_coreMVC_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="PHPMVC_coreMVC_Method", type=Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outParameters17: BinaryAssociation = BinaryAssociation(
    name="outParameters17",
    ends={
        Property(name="Attribute19", type=PHPMVC_coreMVC_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="PHPMVC_coreMVC_Method18", type=Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
events20: BinaryAssociation = BinaryAssociation(
    name="events20",
    ends={
        Property(name="Event", type=PHPMVC_coreMVC_ViewComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="PHPMVC_coreMVC_ViewComponent", type=Event, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_PHPMVC_coreMVC_Model_MVCClass = Generalization(general=MVCClass, specific=PHPMVC_coreMVC_Model)
gen_PHPMVC_coreMVC_View_MVCClass = Generalization(general=MVCClass, specific=PHPMVC_coreMVC_View)
gen_PHPMVC_coreMVC_Identifier_Attribute = Generalization(general=Attribute, specific=PHPMVC_coreMVC_Identifier)
gen_PHPMVC_extPHP_HTMLElement_ViewComponent = Generalization(general=ViewComponent, specific=PHPMVC_extPHP_HTMLElement)
gen_PHPMVC_extPHP_Form_HTMLElement = Generalization(general=HTMLElement, specific=PHPMVC_extPHP_Form)
gen_PHPMVC_extPHP_Button_HTMLElement = Generalization(general=HTMLElement, specific=PHPMVC_extPHP_Button)
gen_PHPMVC_extPHP_Text_HTMLElement = Generalization(general=HTMLElement, specific=PHPMVC_extPHP_Text)
gen_PHPMVC_coreMVC_Controller_MVCClass = Generalization(general=MVCClass, specific=PHPMVC_coreMVC_Controller)
gen_PHPMVC_extPHP_Anchor_HTMLElement = Generalization(general=HTMLElement, specific=PHPMVC_extPHP_Anchor)
gen_PHPMVC_extPHP_Image_HTMLElement = Generalization(general=HTMLElement, specific=PHPMVC_extPHP_Image)
gen_PHPMVC_extPHP_Input_HTMLElement = Generalization(general=HTMLElement, specific=PHPMVC_extPHP_Input)
gen_PHPMVC_extPHP_TextField_Input = Generalization(general=Input, specific=PHPMVC_extPHP_TextField)
gen_PHPMVC_extPHP_Checkbox_Input = Generalization(general=Input, specific=PHPMVC_extPHP_Checkbox)
gen_PHPMVC_extPHP_RadioButton_Input = Generalization(general=Input, specific=PHPMVC_extPHP_RadioButton)

# Domain Model
domain_model = DomainModel(
    name="PHPMVC",
    types={PHPMVC_coreMVC_Application, PHPMVC_coreMVC_PackageController, Controller, PHPMVC_coreMVC_MVCClass, Attribute, PHPMVC_coreMVC_Attribute, PHPMVC_coreMVC_Model, MVCClass, Identifier, PHPMVC_coreMVC_View, ViewComponent, PHPMVC_coreMVC_Controller, PackageModel, PackageView, PackageController, PHPMVC_coreMVC_PackageModel, Model, PHPMVC_coreMVC_PackageView, View, PHPMVC_coreMVC_Identifier, PHPMVC_extPHP_HTMLElement, HTMLElement, PHPMVC_extPHP_Form, PHPMVC_extPHP_Button, PHPMVC_extPHP_Text, Method_, PHPMVC_coreMVC_Method, PHPMVC_coreMVC_ViewComponent, Event, PHPMVC_coreMVC_Event, PHPMVC_extPHP_Anchor, PHPMVC_extPHP_Image, PHPMVC_extPHP_Input, PHPMVC_extPHP_TextField, Input, PHPMVC_extPHP_Checkbox, PHPMVC_extPHP_RadioButton, EventType, InputType, HTMLTag, MethodType, ButtonType, TargetType},
    associations={controllers7, attributes8, primaryKeys9, viewComponents10, innerViews11, aPackageModel0, aPackageView1, aPackageController3, models5, views6, htmlElements21, methods14, inParameters15, outParameters17, events20},
    generalizations={gen_PHPMVC_coreMVC_Model_MVCClass, gen_PHPMVC_coreMVC_View_MVCClass, gen_PHPMVC_coreMVC_Identifier_Attribute, gen_PHPMVC_extPHP_HTMLElement_ViewComponent, gen_PHPMVC_extPHP_Form_HTMLElement, gen_PHPMVC_extPHP_Button_HTMLElement, gen_PHPMVC_extPHP_Text_HTMLElement, gen_PHPMVC_coreMVC_Controller_MVCClass, gen_PHPMVC_extPHP_Anchor_HTMLElement, gen_PHPMVC_extPHP_Image_HTMLElement, gen_PHPMVC_extPHP_Input_HTMLElement, gen_PHPMVC_extPHP_TextField_Input, gen_PHPMVC_extPHP_Checkbox_Input, gen_PHPMVC_extPHP_RadioButton_Input},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)