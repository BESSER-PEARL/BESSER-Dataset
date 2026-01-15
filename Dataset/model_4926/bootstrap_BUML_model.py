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
bootstrap_Site = Class(name="bootstrap::Site")
bootstrap_Page = Class(name="bootstrap::Page")
bootstrap_MainPage = Class(name="bootstrap::MainPage")
bootstrap_Section = Class(name="bootstrap::Section")
bootstrap_Form = Class(name="bootstrap::Form")
Widget = Class(name="Widget")
bootstrap_FormWidget = Class(name="bootstrap::FormWidget", is_abstract=True)
bootstrap_Table = Class(name="bootstrap::Table")
bootstrap_Text = Class(name="bootstrap::Text")
bootstrap_Video = Class(name="bootstrap::Video")
bootstrap_Gallery = Class(name="bootstrap::Gallery")
bootstrap_ImagesBlock = Class(name="bootstrap::ImagesBlock")
bootstrap_TextArea = Class(name="bootstrap::TextArea")
FormWidget = Class(name="FormWidget")
bootstrap_Widget = Class(name="bootstrap::Widget", is_abstract=True)
bootstrap_Spinner = Class(name="bootstrap::Spinner")
bootstrap_CheckBox = Class(name="bootstrap::CheckBox")

# bootstrap_Site class attributes and methods
bootstrap_Site_title: Property = Property(name="title", type=StringType)
bootstrap_Site.attributes={bootstrap_Site_title}

# bootstrap_Page class attributes and methods
bootstrap_Page_title: Property = Property(name="title", type=StringType)
bootstrap_Page_description: Property = Property(name="description", type=StringType)
bootstrap_Page_name: Property = Property(name="name", type=StringType)
bootstrap_Page.attributes={bootstrap_Page_name, bootstrap_Page_description, bootstrap_Page_title}

# bootstrap_MainPage class attributes and methods
bootstrap_MainPage_title: Property = Property(name="title", type=StringType)
bootstrap_MainPage_description: Property = Property(name="description", type=StringType)
bootstrap_MainPage.attributes={bootstrap_MainPage_title, bootstrap_MainPage_description}

# bootstrap_Section class attributes and methods
bootstrap_Section_title: Property = Property(name="title", type=StringType)
bootstrap_Section_description: Property = Property(name="description", type=StringType)
bootstrap_Section.attributes={bootstrap_Section_title, bootstrap_Section_description}

# bootstrap_Form class attributes and methods

# Widget class attributes and methods

# bootstrap_FormWidget class attributes and methods
bootstrap_FormWidget_label: Property = Property(name="label", type=StringType)
bootstrap_FormWidget.attributes={bootstrap_FormWidget_label}

# bootstrap_Table class attributes and methods
bootstrap_Table_columnNames: Property = Property(name="columnNames", type=StringType)
bootstrap_Table_rowNames: Property = Property(name="rowNames", type=StringType)
bootstrap_Table_striped: Property = Property(name="striped", type=BooleanType)
bootstrap_Table_bordered: Property = Property(name="bordered", type=BooleanType)
bootstrap_Table.attributes={bootstrap_Table_rowNames, bootstrap_Table_bordered, bootstrap_Table_columnNames, bootstrap_Table_striped}

# bootstrap_Text class attributes and methods
bootstrap_Text_columnNumber: Property = Property(name="columnNumber", type=IntegerType)
bootstrap_Text.attributes={bootstrap_Text_columnNumber}

# bootstrap_Video class attributes and methods
bootstrap_Video_path: Property = Property(name="path", type=StringType)
bootstrap_Video.attributes={bootstrap_Video_path}

# bootstrap_Gallery class attributes and methods
bootstrap_Gallery_imagesPath: Property = Property(name="imagesPath", type=StringType)
bootstrap_Gallery.attributes={bootstrap_Gallery_imagesPath}

# bootstrap_ImagesBlock class attributes and methods
bootstrap_ImagesBlock_imagesPath: Property = Property(name="imagesPath", type=StringType)
bootstrap_ImagesBlock.attributes={bootstrap_ImagesBlock_imagesPath}

# bootstrap_TextArea class attributes and methods

# FormWidget class attributes and methods

# bootstrap_Widget class attributes and methods
bootstrap_Widget_title: Property = Property(name="title", type=StringType)
bootstrap_Widget.attributes={bootstrap_Widget_title}

# bootstrap_Spinner class attributes and methods
bootstrap_Spinner_values: Property = Property(name="values", type=StringType)
bootstrap_Spinner.attributes={bootstrap_Spinner_values}

# bootstrap_CheckBox class attributes and methods
bootstrap_CheckBox_description: Property = Property(name="description", type=StringType)
bootstrap_CheckBox.attributes={bootstrap_CheckBox_description}

# Relationships
pages0: BinaryAssociation = BinaryAssociation(
    name="pages0",
    ends={
        Property(name="Page", type=bootstrap_Site, multiplicity=Multiplicity(1, 1)),
        Property(name="site", type=bootstrap_Page, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mainPage1: BinaryAssociation = BinaryAssociation(
    name="mainPage1",
    ends={
        Property(name="MainPage", type=bootstrap_Site, multiplicity=Multiplicity(1, 1)),
        Property(name="site2", type=bootstrap_MainPage, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
section10: BinaryAssociation = BinaryAssociation(
    name="section10",
    ends={
        Property(name="Section11", type=bootstrap_Widget, multiplicity=Multiplicity(1, 1)),
        Property(name="widgets", type=bootstrap_Section, multiplicity=Multiplicity(1, 1))
    }
)
formWidgets12: BinaryAssociation = BinaryAssociation(
    name="formWidgets12",
    ends={
        Property(name="FormWidget", type=bootstrap_Form, multiplicity=Multiplicity(1, 1)),
        Property(name="form", type=bootstrap_FormWidget, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
form13: BinaryAssociation = BinaryAssociation(
    name="form13",
    ends={
        Property(name="Form", type=bootstrap_FormWidget, multiplicity=Multiplicity(1, 1)),
        Property(name="formWidgets", type=bootstrap_Form, multiplicity=Multiplicity(1, 1))
    }
)
sections3: BinaryAssociation = BinaryAssociation(
    name="sections3",
    ends={
        Property(name="Section", type=bootstrap_Page, multiplicity=Multiplicity(1, 1)),
        Property(name="page", type=bootstrap_Section, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
site4: BinaryAssociation = BinaryAssociation(
    name="site4",
    ends={
        Property(name="Site", type=bootstrap_Page, multiplicity=Multiplicity(1, 1)),
        Property(name="pages", type=bootstrap_Site, multiplicity=Multiplicity(1, 1))
    }
)
site5: BinaryAssociation = BinaryAssociation(
    name="site5",
    ends={
        Property(name="Site6", type=bootstrap_MainPage, multiplicity=Multiplicity(1, 1)),
        Property(name="mainPage", type=bootstrap_Site, multiplicity=Multiplicity(1, 1))
    }
)
widgets7: BinaryAssociation = BinaryAssociation(
    name="widgets7",
    ends={
        Property(name="Widget", type=bootstrap_Section, multiplicity=Multiplicity(1, 1)),
        Property(name="section", type=bootstrap_Widget, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
page8: BinaryAssociation = BinaryAssociation(
    name="page8",
    ends={
        Property(name="Page9", type=bootstrap_Section, multiplicity=Multiplicity(1, 1)),
        Property(name="sections", type=bootstrap_Page, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_bootstrap_Form_Widget = Generalization(general=Widget, specific=bootstrap_Form)
gen_bootstrap_Table_Widget = Generalization(general=Widget, specific=bootstrap_Table)
gen_bootstrap_Text_Widget = Generalization(general=Widget, specific=bootstrap_Text)
gen_bootstrap_Video_Widget = Generalization(general=Widget, specific=bootstrap_Video)
gen_bootstrap_Gallery_Widget = Generalization(general=Widget, specific=bootstrap_Gallery)
gen_bootstrap_ImagesBlock_Widget = Generalization(general=Widget, specific=bootstrap_ImagesBlock)
gen_bootstrap_TextArea_FormWidget = Generalization(general=FormWidget, specific=bootstrap_TextArea)
gen_bootstrap_Spinner_FormWidget = Generalization(general=FormWidget, specific=bootstrap_Spinner)
gen_bootstrap_CheckBox_FormWidget = Generalization(general=FormWidget, specific=bootstrap_CheckBox)

# Domain Model
domain_model = DomainModel(
    name="bootstrap",
    types={bootstrap_Site, bootstrap_Page, bootstrap_MainPage, bootstrap_Section, bootstrap_Form, Widget, bootstrap_FormWidget, bootstrap_Table, bootstrap_Text, bootstrap_Video, bootstrap_Gallery, bootstrap_ImagesBlock, bootstrap_TextArea, FormWidget, bootstrap_Widget, bootstrap_Spinner, bootstrap_CheckBox},
    associations={pages0, mainPage1, section10, formWidgets12, form13, sections3, site4, site5, widgets7, page8},
    generalizations={gen_bootstrap_Form_Widget, gen_bootstrap_Table_Widget, gen_bootstrap_Text_Widget, gen_bootstrap_Video_Widget, gen_bootstrap_Gallery_Widget, gen_bootstrap_ImagesBlock_Widget, gen_bootstrap_TextArea_FormWidget, gen_bootstrap_Spinner_FormWidget, gen_bootstrap_CheckBox_FormWidget},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)