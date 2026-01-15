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
GraphType: Enumeration = Enumeration(
    name="GraphType",
    literals={
            EnumerationLiteral(name="BAR"),
			EnumerationLiteral(name="PIE"),
			EnumerationLiteral(name="SCALAR"),
			EnumerationLiteral(name="NONE")
    }
)

SelectType: Enumeration = Enumeration(
    name="SelectType",
    literals={
            EnumerationLiteral(name="LIST"),
			EnumerationLiteral(name="COMBO")
    }
)

InputType: Enumeration = Enumeration(
    name="InputType",
    literals={
            EnumerationLiteral(name="TEXT"),
			EnumerationLiteral(name="NUMBER"),
			EnumerationLiteral(name="DATE"),
			EnumerationLiteral(name="EMAIL"),
			EnumerationLiteral(name="RANGE")
    }
)

# Classes
html_View = Class(name="html::View")
html_Label = Class(name="html::Label")
FormElement = Class(name="FormElement")
html_Editable = Class(name="html::Editable", is_abstract=True)
html_Input = Class(name="html::Input")
Editable = Class(name="Editable")
html_TextArea = Class(name="html::TextArea")
html_Select = Class(name="html::Select")
SelectionList = Class(name="SelectionList")
html_Option = Class(name="html::Option")
html_Graph = Class(name="html::Graph")
html_Section = Class(name="html::Section")
html_FormElement = Class(name="html::FormElement", is_abstract=True)
html_Page = Class(name="html::Page")
html_SelectionList = Class(name="html::SelectionList", is_abstract=True)
html_SelectComplex = Class(name="html::SelectComplex")
html_ColumnOption = Class(name="html::ColumnOption")
html_Container = Class(name="html::Container")

# html_View class attributes and methods
html_View_title: Property = Property(name="title", type=StringType)
html_View.attributes={html_View_title}

# html_Label class attributes and methods
html_Label_content: Property = Property(name="content", type=StringType)
html_Label_forText: Property = Property(name="forText", type=IntegerType)
html_Label.attributes={html_Label_content, html_Label_forText}

# FormElement class attributes and methods

# html_Editable class attributes and methods
html_Editable_name: Property = Property(name="name", type=IntegerType)
html_Editable_required: Property = Property(name="required", type=BooleanType)
html_Editable.attributes={html_Editable_name, html_Editable_required}

# html_Input class attributes and methods
html_Input_checked: Property = Property(name="checked", type=BooleanType)
html_Input_type: Property = Property(name="type", type=StringType)
html_Input_min: Property = Property(name="min", type=IntegerType)
html_Input_max: Property = Property(name="max", type=IntegerType)
html_Input_step: Property = Property(name="step", type=IntegerType)
html_Input_maxLength: Property = Property(name="maxLength", type=IntegerType)
html_Input.attributes={html_Input_maxLength, html_Input_checked, html_Input_type, html_Input_min, html_Input_max, html_Input_step}

# Editable class attributes and methods

# html_TextArea class attributes and methods
html_TextArea_rows: Property = Property(name="rows", type=IntegerType)
html_TextArea_maxLength: Property = Property(name="maxLength", type=IntegerType)
html_TextArea.attributes={html_TextArea_maxLength, html_TextArea_rows}

# html_Select class attributes and methods
html_Select_type: Property = Property(name="type", type=StringType)
html_Select.attributes={html_Select_type}

# SelectionList class attributes and methods

# html_Option class attributes and methods
html_Option_content: Property = Property(name="content", type=StringType)
html_Option_value: Property = Property(name="value", type=IntegerType)
html_Option.attributes={html_Option_value, html_Option_content}

# html_Graph class attributes and methods
html_Graph_type: Property = Property(name="type", type=StringType)
html_Graph_title: Property = Property(name="title", type=StringType)
html_Graph.attributes={html_Graph_title, html_Graph_type}

# html_Section class attributes and methods
html_Section_title: Property = Property(name="title", type=StringType)
html_Section_id: Property = Property(name="id", type=IntegerType)
html_Section.attributes={html_Section_title, html_Section_id}

# html_FormElement class attributes and methods
html_FormElement_id: Property = Property(name="id", type=StringType)
html_FormElement_visible: Property = Property(name="visible", type=BooleanType)
html_FormElement.attributes={html_FormElement_visible, html_FormElement_id}

# html_Page class attributes and methods
html_Page_title: Property = Property(name="title", type=StringType)
html_Page_urlToSaveResponses: Property = Property(name="urlToSaveResponses", type=StringType)
html_Page_urlToGetData: Property = Property(name="urlToGetData", type=StringType)
html_Page_urlToGetRelationResult: Property = Property(name="urlToGetRelationResult", type=StringType)
html_Page_description: Property = Property(name="description", type=StringType)
html_Page_id: Property = Property(name="id", type=IntegerType)
html_Page.attributes={html_Page_id, html_Page_title, html_Page_description, html_Page_urlToSaveResponses, html_Page_urlToGetRelationResult, html_Page_urlToGetData}

# html_SelectionList class attributes and methods
html_SelectionList_multiple: Property = Property(name="multiple", type=BooleanType)
html_SelectionList.attributes={html_SelectionList_multiple}

# html_SelectComplex class attributes and methods

# html_ColumnOption class attributes and methods
html_ColumnOption_content: Property = Property(name="content", type=StringType)
html_ColumnOption_value: Property = Property(name="value", type=IntegerType)
html_ColumnOption.attributes={html_ColumnOption_content, html_ColumnOption_value}

# html_Container class attributes and methods
html_Container_name: Property = Property(name="name", type=StringType)
html_Container.attributes={html_Container_name}

# Relationships
label5: BinaryAssociation = BinaryAssociation(
    name="label5",
    ends={
        Property(name="html_Label", type=html_Editable, multiplicity=Multiplicity(1, 1)),
        Property(name="html_Editable", type=html_Label, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
options6: BinaryAssociation = BinaryAssociation(
    name="options6",
    ends={
        Property(name="html_Option", type=html_Select, multiplicity=Multiplicity(1, 1)),
        Property(name="html_Select", type=html_Option, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
graphs0: BinaryAssociation = BinaryAssociation(
    name="graphs0",
    ends={
        Property(name="html_Graph", type=html_View, multiplicity=Multiplicity(1, 1)),
        Property(name="html_View", type=html_Graph, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sections1: BinaryAssociation = BinaryAssociation(
    name="sections1",
    ends={
        Property(name="html_Section", type=html_View, multiplicity=Multiplicity(1, 1)),
        Property(name="html_View2", type=html_Section, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
formElements3: BinaryAssociation = BinaryAssociation(
    name="formElements3",
    ends={
        Property(name="html_FormElement", type=html_Section, multiplicity=Multiplicity(1, 1)),
        Property(name="html_Section4", type=html_FormElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pages16: BinaryAssociation = BinaryAssociation(
    name="pages16",
    ends={
        Property(name="html_Page", type=html_Container, multiplicity=Multiplicity(1, 1)),
        Property(name="html_Container", type=html_Page, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
views17: BinaryAssociation = BinaryAssociation(
    name="views17",
    ends={
        Property(name="html_View19", type=html_Page, multiplicity=Multiplicity(1, 1)),
        Property(name="html_Page18", type=html_View, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
otherArea7: BinaryAssociation = BinaryAssociation(
    name="otherArea7",
    ends={
        Property(name="html_TextArea", type=html_Option, multiplicity=Multiplicity(1, 1)),
        Property(name="html_Option8", type=html_TextArea, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
formElements9: BinaryAssociation = BinaryAssociation(
    name="formElements9",
    ends={
        Property(name="html_FormElement11", type=html_Option, multiplicity=Multiplicity(1, 1)),
        Property(name="html_Option10", type=html_FormElement, multiplicity=Multiplicity(0, 9999))
    }
)
columnsOptions12: BinaryAssociation = BinaryAssociation(
    name="columnsOptions12",
    ends={
        Property(name="html_ColumnOption", type=html_SelectComplex, multiplicity=Multiplicity(1, 1)),
        Property(name="html_SelectComplex", type=html_ColumnOption, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
options13: BinaryAssociation = BinaryAssociation(
    name="options13",
    ends={
        Property(name="html_Option15", type=html_SelectComplex, multiplicity=Multiplicity(1, 1)),
        Property(name="html_SelectComplex14", type=html_Option, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_html_Label_FormElement = Generalization(general=FormElement, specific=html_Label)
gen_html_Editable_FormElement = Generalization(general=FormElement, specific=html_Editable)
gen_html_Input_Editable = Generalization(general=Editable, specific=html_Input)
gen_html_TextArea_Editable = Generalization(general=Editable, specific=html_TextArea)
gen_html_Select_SelectionList = Generalization(general=SelectionList, specific=html_Select)
gen_html_SelectionList_Editable = Generalization(general=Editable, specific=html_SelectionList)
gen_html_SelectComplex_SelectionList = Generalization(general=SelectionList, specific=html_SelectComplex)

# Domain Model
domain_model = DomainModel(
    name="html",
    types={html_View, html_Label, FormElement, html_Editable, html_Input, Editable, html_TextArea, html_Select, SelectionList, html_Option, html_Graph, html_Section, html_FormElement, html_Page, html_SelectionList, html_SelectComplex, html_ColumnOption, html_Container, GraphType, SelectType, InputType},
    associations={label5, options6, graphs0, sections1, formElements3, pages16, views17, otherArea7, formElements9, columnsOptions12, options13},
    generalizations={gen_html_Label_FormElement, gen_html_Editable_FormElement, gen_html_Input_Editable, gen_html_TextArea_Editable, gen_html_Select_SelectionList, gen_html_SelectionList_Editable, gen_html_SelectComplex_SelectionList},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)