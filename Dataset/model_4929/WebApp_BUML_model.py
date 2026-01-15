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
webapp_NamedElement = Class(name="webapp::NamedElement")
webapp_Application = Class(name="webapp::Application")
NamedElement = Class(name="NamedElement")
webapp_Router = Class(name="webapp::Router")
webapp_Collection = Class(name="webapp::Collection")
webapp_AbstractView = Class(name="webapp::AbstractView", is_abstract=True)
webapp_Model = Class(name="webapp::Model")
webapp_Attribute = Class(name="webapp::Attribute")
webapp_Parameter = Class(name="webapp::Parameter")
webapp_RouterMapping = Class(name="webapp::RouterMapping")
webapp_Reference = Class(name="webapp::Reference")
webapp_Operation = Class(name="webapp::Operation")
webapp_Widget = Class(name="webapp::Widget", is_abstract=True)
webapp_Form = Class(name="webapp::Form")
Widget = Class(name="Widget")
webapp_FormWidget = Class(name="webapp::FormWidget", is_abstract=True)
webapp_Table = Class(name="webapp::Table")
webapp_Text = Class(name="webapp::Text")
webapp_Video = Class(name="webapp::Video")
webapp_Gallery = Class(name="webapp::Gallery")
webapp_ImagesBlock = Class(name="webapp::ImagesBlock")
webapp_ModelView = Class(name="webapp::ModelView")
AbstractView = Class(name="AbstractView")
webapp_StaticView = Class(name="webapp::StaticView")
webapp_Section = Class(name="webapp::Section")
webapp_CheckBox = Class(name="webapp::CheckBox")
webapp_TextArea = Class(name="webapp::TextArea")
FormWidget = Class(name="FormWidget")
webapp_Spinner = Class(name="webapp::Spinner")

# webapp_NamedElement class attributes and methods
webapp_NamedElement_name: Property = Property(name="name", type=StringType)
webapp_NamedElement.attributes={webapp_NamedElement_name}

# webapp_Application class attributes and methods

# NamedElement class attributes and methods

# webapp_Router class attributes and methods

# webapp_Collection class attributes and methods

# webapp_AbstractView class attributes and methods
webapp_AbstractView_description: Property = Property(name="description", type=StringType)
webapp_AbstractView.attributes={webapp_AbstractView_description}

# webapp_Model class attributes and methods

# webapp_Attribute class attributes and methods
webapp_Attribute_defaultValue: Property = Property(name="defaultValue", type=StringType)
webapp_Attribute.attributes={webapp_Attribute_defaultValue}

# webapp_Parameter class attributes and methods

# webapp_RouterMapping class attributes and methods
webapp_RouterMapping_path: Property = Property(name="path", type=StringType)
webapp_RouterMapping.attributes={webapp_RouterMapping_path}

# webapp_Reference class attributes and methods

# webapp_Operation class attributes and methods

# webapp_Widget class attributes and methods
webapp_Widget_title: Property = Property(name="title", type=StringType)
webapp_Widget.attributes={webapp_Widget_title}

# webapp_Form class attributes and methods

# Widget class attributes and methods

# webapp_FormWidget class attributes and methods
webapp_FormWidget_label: Property = Property(name="label", type=StringType)
webapp_FormWidget.attributes={webapp_FormWidget_label}

# webapp_Table class attributes and methods
webapp_Table_columnNames: Property = Property(name="columnNames", type=StringType)
webapp_Table_rowNames: Property = Property(name="rowNames", type=StringType)
webapp_Table_striped: Property = Property(name="striped", type=BooleanType)
webapp_Table_bordered: Property = Property(name="bordered", type=BooleanType)
webapp_Table.attributes={webapp_Table_bordered, webapp_Table_striped, webapp_Table_columnNames, webapp_Table_rowNames}

# webapp_Text class attributes and methods
webapp_Text_columnNumber: Property = Property(name="columnNumber", type=IntegerType)
webapp_Text.attributes={webapp_Text_columnNumber}

# webapp_Video class attributes and methods
webapp_Video_path: Property = Property(name="path", type=StringType)
webapp_Video.attributes={webapp_Video_path}

# webapp_Gallery class attributes and methods
webapp_Gallery_imagesPath: Property = Property(name="imagesPath", type=StringType)
webapp_Gallery.attributes={webapp_Gallery_imagesPath}

# webapp_ImagesBlock class attributes and methods
webapp_ImagesBlock_imagesPath: Property = Property(name="imagesPath", type=StringType)
webapp_ImagesBlock.attributes={webapp_ImagesBlock_imagesPath}

# webapp_ModelView class attributes and methods

# AbstractView class attributes and methods

# webapp_StaticView class attributes and methods

# webapp_Section class attributes and methods
webapp_Section_title: Property = Property(name="title", type=StringType)
webapp_Section_description: Property = Property(name="description", type=StringType)
webapp_Section.attributes={webapp_Section_description, webapp_Section_title}

# webapp_CheckBox class attributes and methods
webapp_CheckBox_description: Property = Property(name="description", type=StringType)
webapp_CheckBox.attributes={webapp_CheckBox_description}

# webapp_TextArea class attributes and methods

# FormWidget class attributes and methods

# webapp_Spinner class attributes and methods
webapp_Spinner_values: Property = Property(name="values", type=StringType)
webapp_Spinner.attributes={webapp_Spinner_values}

# Relationships
router0: BinaryAssociation = BinaryAssociation(
    name="router0",
    ends={
        Property(name="Router", type=webapp_Application, multiplicity=Multiplicity(1, 1)),
        Property(name="application", type=webapp_Router, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
collections1: BinaryAssociation = BinaryAssociation(
    name="collections1",
    ends={
        Property(name="Collection", type=webapp_Application, multiplicity=Multiplicity(1, 1)),
        Property(name="application2", type=webapp_Collection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
views3: BinaryAssociation = BinaryAssociation(
    name="views3",
    ends={
        Property(name="AbstractView", type=webapp_Application, multiplicity=Multiplicity(1, 1)),
        Property(name="application4", type=webapp_AbstractView, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
models5: BinaryAssociation = BinaryAssociation(
    name="models5",
    ends={
        Property(name="Model", type=webapp_Application, multiplicity=Multiplicity(1, 1)),
        Property(name="application6", type=webapp_Model, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributes7: BinaryAssociation = BinaryAssociation(
    name="attributes7",
    ends={
        Property(name="webapp_Attribute", type=webapp_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="webapp_Model", type=webapp_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters16: BinaryAssociation = BinaryAssociation(
    name="parameters16",
    ends={
        Property(name="webapp_Parameter", type=webapp_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="webapp_Operation17", type=webapp_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
model18: BinaryAssociation = BinaryAssociation(
    name="model18",
    ends={
        Property(name="webapp_Model19", type=webapp_Collection, multiplicity=Multiplicity(1, 1)),
        Property(name="webapp_Collection", type=webapp_Model, multiplicity=Multiplicity(1, 1))
    }
)
application20: BinaryAssociation = BinaryAssociation(
    name="application20",
    ends={
        Property(name="Application21", type=webapp_Collection, multiplicity=Multiplicity(1, 1)),
        Property(name="collections", type=webapp_Application, multiplicity=Multiplicity(1, 1))
    }
)
mappings22: BinaryAssociation = BinaryAssociation(
    name="mappings22",
    ends={
        Property(name="webapp_RouterMapping", type=webapp_Router, multiplicity=Multiplicity(1, 1)),
        Property(name="webapp_Router", type=webapp_RouterMapping, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
application23: BinaryAssociation = BinaryAssociation(
    name="application23",
    ends={
        Property(name="Application24", type=webapp_Router, multiplicity=Multiplicity(1, 1)),
        Property(name="router", type=webapp_Application, multiplicity=Multiplicity(1, 1))
    }
)
view25: BinaryAssociation = BinaryAssociation(
    name="view25",
    ends={
        Property(name="webapp_AbstractView", type=webapp_RouterMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="webapp_RouterMapping26", type=webapp_AbstractView, multiplicity=Multiplicity(1, 1))
    }
)
operations27: BinaryAssociation = BinaryAssociation(
    name="operations27",
    ends={
        Property(name="webapp_Operation29", type=webapp_AbstractView, multiplicity=Multiplicity(1, 1)),
        Property(name="webapp_AbstractView28", type=webapp_Operation, multiplicity=Multiplicity(0, 9999))
    }
)
references8: BinaryAssociation = BinaryAssociation(
    name="references8",
    ends={
        Property(name="webapp_Reference", type=webapp_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="webapp_Model9", type=webapp_Reference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operations10: BinaryAssociation = BinaryAssociation(
    name="operations10",
    ends={
        Property(name="webapp_Operation", type=webapp_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="webapp_Model11", type=webapp_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
application12: BinaryAssociation = BinaryAssociation(
    name="application12",
    ends={
        Property(name="Application", type=webapp_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="models", type=webapp_Application, multiplicity=Multiplicity(1, 1))
    }
)
type13: BinaryAssociation = BinaryAssociation(
    name="type13",
    ends={
        Property(name="webapp_Model15", type=webapp_Reference, multiplicity=Multiplicity(1, 1)),
        Property(name="webapp_Reference14", type=webapp_Model, multiplicity=Multiplicity(1, 1))
    }
)
widgets35: BinaryAssociation = BinaryAssociation(
    name="widgets35",
    ends={
        Property(name="Widget", type=webapp_Section, multiplicity=Multiplicity(1, 1)),
        Property(name="section", type=webapp_Widget, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
view36: BinaryAssociation = BinaryAssociation(
    name="view36",
    ends={
        Property(name="StaticView", type=webapp_Section, multiplicity=Multiplicity(1, 1)),
        Property(name="sections", type=webapp_StaticView, multiplicity=Multiplicity(1, 1))
    }
)
section37: BinaryAssociation = BinaryAssociation(
    name="section37",
    ends={
        Property(name="Section38", type=webapp_Widget, multiplicity=Multiplicity(1, 1)),
        Property(name="widgets", type=webapp_Section, multiplicity=Multiplicity(1, 1))
    }
)
formWidgets39: BinaryAssociation = BinaryAssociation(
    name="formWidgets39",
    ends={
        Property(name="FormWidget", type=webapp_Form, multiplicity=Multiplicity(1, 1)),
        Property(name="form", type=webapp_FormWidget, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
application30: BinaryAssociation = BinaryAssociation(
    name="application30",
    ends={
        Property(name="Application31", type=webapp_AbstractView, multiplicity=Multiplicity(1, 1)),
        Property(name="views", type=webapp_Application, multiplicity=Multiplicity(1, 1))
    }
)
collection32: BinaryAssociation = BinaryAssociation(
    name="collection32",
    ends={
        Property(name="webapp_Collection33", type=webapp_ModelView, multiplicity=Multiplicity(1, 1)),
        Property(name="webapp_ModelView", type=webapp_Collection, multiplicity=Multiplicity(1, 1))
    }
)
sections34: BinaryAssociation = BinaryAssociation(
    name="sections34",
    ends={
        Property(name="Section", type=webapp_StaticView, multiplicity=Multiplicity(1, 1)),
        Property(name="view", type=webapp_Section, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
form40: BinaryAssociation = BinaryAssociation(
    name="form40",
    ends={
        Property(name="Form", type=webapp_FormWidget, multiplicity=Multiplicity(1, 1)),
        Property(name="formWidgets", type=webapp_Form, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_webapp_Application_NamedElement = Generalization(general=NamedElement, specific=webapp_Application)
gen_webapp_Model_NamedElement = Generalization(general=NamedElement, specific=webapp_Model)
gen_webapp_Operation_NamedElement = Generalization(general=NamedElement, specific=webapp_Operation)
gen_webapp_Parameter_NamedElement = Generalization(general=NamedElement, specific=webapp_Parameter)
gen_webapp_Collection_NamedElement = Generalization(general=NamedElement, specific=webapp_Collection)
gen_webapp_Router_NamedElement = Generalization(general=NamedElement, specific=webapp_Router)
gen_webapp_AbstractView_NamedElement = Generalization(general=NamedElement, specific=webapp_AbstractView)
gen_webapp_Attribute_NamedElement = Generalization(general=NamedElement, specific=webapp_Attribute)
gen_webapp_Reference_NamedElement = Generalization(general=NamedElement, specific=webapp_Reference)
gen_webapp_Form_Widget = Generalization(general=Widget, specific=webapp_Form)
gen_webapp_Table_Widget = Generalization(general=Widget, specific=webapp_Table)
gen_webapp_Text_Widget = Generalization(general=Widget, specific=webapp_Text)
gen_webapp_Video_Widget = Generalization(general=Widget, specific=webapp_Video)
gen_webapp_Gallery_Widget = Generalization(general=Widget, specific=webapp_Gallery)
gen_webapp_ImagesBlock_Widget = Generalization(general=Widget, specific=webapp_ImagesBlock)
gen_webapp_ModelView_AbstractView = Generalization(general=AbstractView, specific=webapp_ModelView)
gen_webapp_StaticView_AbstractView = Generalization(general=AbstractView, specific=webapp_StaticView)
gen_webapp_CheckBox_FormWidget = Generalization(general=FormWidget, specific=webapp_CheckBox)
gen_webapp_TextArea_FormWidget = Generalization(general=FormWidget, specific=webapp_TextArea)
gen_webapp_Spinner_FormWidget = Generalization(general=FormWidget, specific=webapp_Spinner)

# Domain Model
domain_model = DomainModel(
    name="webapp",
    types={webapp_NamedElement, webapp_Application, NamedElement, webapp_Router, webapp_Collection, webapp_AbstractView, webapp_Model, webapp_Attribute, webapp_Parameter, webapp_RouterMapping, webapp_Reference, webapp_Operation, webapp_Widget, webapp_Form, Widget, webapp_FormWidget, webapp_Table, webapp_Text, webapp_Video, webapp_Gallery, webapp_ImagesBlock, webapp_ModelView, AbstractView, webapp_StaticView, webapp_Section, webapp_CheckBox, webapp_TextArea, FormWidget, webapp_Spinner},
    associations={router0, collections1, views3, models5, attributes7, parameters16, model18, application20, mappings22, application23, view25, operations27, references8, operations10, application12, type13, widgets35, view36, section37, formWidgets39, application30, collection32, sections34, form40},
    generalizations={gen_webapp_Application_NamedElement, gen_webapp_Model_NamedElement, gen_webapp_Operation_NamedElement, gen_webapp_Parameter_NamedElement, gen_webapp_Collection_NamedElement, gen_webapp_Router_NamedElement, gen_webapp_AbstractView_NamedElement, gen_webapp_Attribute_NamedElement, gen_webapp_Reference_NamedElement, gen_webapp_Form_Widget, gen_webapp_Table_Widget, gen_webapp_Text_Widget, gen_webapp_Video_Widget, gen_webapp_Gallery_Widget, gen_webapp_ImagesBlock_Widget, gen_webapp_ModelView_AbstractView, gen_webapp_StaticView_AbstractView, gen_webapp_CheckBox_FormWidget, gen_webapp_TextArea_FormWidget, gen_webapp_Spinner_FormWidget},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)