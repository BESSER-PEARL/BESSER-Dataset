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
types: Enumeration = Enumeration(
    name="types",
    literals={
            EnumerationLiteral(name="text"),
			EnumerationLiteral(name="number"),
			EnumerationLiteral(name="button")
    }
)

# Classes
html5_div = Class(name="html5::div")
container = Class(name="container")
html5_Action = Class(name="html5::Action")
html5_table = Class(name="html5::table")
htmlElement = Class(name="htmlElement")
html5_tr = Class(name="html5::tr")
html5_td = Class(name="html5::td")
html5_img = Class(name="html5::img")
html5_label = Class(name="html5::label")
html5_input = Class(name="html5::input")
html5_button = Class(name="html5::button")
html5_option = Class(name="html5::option")
html5_fieldset = Class(name="html5::fieldset")
html5_legend = Class(name="html5::legend")
html5_html = Class(name="html5::html")
html5_container = Class(name="html5::container", is_abstract=True)
html5_dialog = Class(name="html5::dialog")
html5_select = Class(name="html5::select")
html5_htmlElement = Class(name="html5::htmlElement", is_abstract=True)

# html5_div class attributes and methods
html5_div_id: Property = Property(name="id", type=StringType)
html5_div.attributes={html5_div_id}

# container class attributes and methods

# html5_Action class attributes and methods
html5_Action_codigo: Property = Property(name="codigo", type=StringType)
html5_Action.attributes={html5_Action_codigo}

# html5_table class attributes and methods

# htmlElement class attributes and methods

# html5_tr class attributes and methods

# html5_td class attributes and methods

# html5_img class attributes and methods
html5_img_src: Property = Property(name="src", type=StringType)
html5_img.attributes={html5_img_src}

# html5_label class attributes and methods
html5_label_valor: Property = Property(name="valor", type=StringType)
html5_label_value: Property = Property(name="value", type=StringType)
html5_label.attributes={html5_label_value, html5_label_valor}

# html5_input class attributes and methods
html5_input_type: Property = Property(name="type", type=StringType)
html5_input_value: Property = Property(name="value", type=StringType)
html5_input_disable: Property = Property(name="disable", type=StringType)
html5_input.attributes={html5_input_value, html5_input_type, html5_input_disable}

# html5_button class attributes and methods
html5_button_type: Property = Property(name="type", type=StringType)
html5_button_value: Property = Property(name="value", type=StringType)
html5_button_action: Property = Property(name="action", type=StringType)
html5_button.attributes={html5_button_value, html5_button_action, html5_button_type}

# html5_option class attributes and methods

# html5_fieldset class attributes and methods

# html5_legend class attributes and methods
html5_legend_class: Property = Property(name="class", type=StringType)
html5_legend_valor: Property = Property(name="valor", type=StringType)
html5_legend.attributes={html5_legend_valor, html5_legend_class}

# html5_html class attributes and methods

# html5_container class attributes and methods
html5_container_class: Property = Property(name="class", type=StringType)
html5_container.attributes={html5_container_class}

# html5_dialog class attributes and methods

# html5_select class attributes and methods
html5_select_multiple: Property = Property(name="multiple", type=StringType)
html5_select_size: Property = Property(name="size", type=StringType)
html5_select.attributes={html5_select_multiple, html5_select_size}

# html5_htmlElement class attributes and methods
html5_htmlElement_class: Property = Property(name="class", type=StringType)
html5_htmlElement.attributes={html5_htmlElement_class}

# Relationships
actions0: BinaryAssociation = BinaryAssociation(
    name="actions0",
    ends={
        Property(name="html5_Action", type=html5_div, multiplicity=Multiplicity(1, 1)),
        Property(name="html5_div", type=html5_Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tr1: BinaryAssociation = BinaryAssociation(
    name="tr1",
    ends={
        Property(name="html5_tr", type=html5_table, multiplicity=Multiplicity(1, 1)),
        Property(name="html5_table", type=html5_tr, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
td2: BinaryAssociation = BinaryAssociation(
    name="td2",
    ends={
        Property(name="html5_td", type=html5_tr, multiplicity=Multiplicity(1, 1)),
        Property(name="html5_tr3", type=html5_td, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
legend6: BinaryAssociation = BinaryAssociation(
    name="legend6",
    ends={
        Property(name="html5_legend", type=html5_fieldset, multiplicity=Multiplicity(1, 1)),
        Property(name="html5_fieldset", type=html5_legend, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
container7: BinaryAssociation = BinaryAssociation(
    name="container7",
    ends={
        Property(name="html5_container", type=html5_html, multiplicity=Multiplicity(1, 1)),
        Property(name="html5_html", type=html5_container, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements8: BinaryAssociation = BinaryAssociation(
    name="elements8",
    ends={
        Property(name="html5_htmlElement10", type=html5_container, multiplicity=Multiplicity(1, 1)),
        Property(name="html5_container9", type=html5_htmlElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
innercontainer12: BinaryAssociation = BinaryAssociation(
    name="innercontainer12",
    ends={
        Property(name="html5_container13", type=html5_container, multiplicity=Multiplicity(1, 1)),
        Property(name="html5_container11", type=html5_container, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
options14: BinaryAssociation = BinaryAssociation(
    name="options14",
    ends={
        Property(name="html5_option", type=html5_select, multiplicity=Multiplicity(1, 1)),
        Property(name="html5_select", type=html5_option, multiplicity=Multiplicity(0, 1))
    }
)
elements4: BinaryAssociation = BinaryAssociation(
    name="elements4",
    ends={
        Property(name="html5_htmlElement", type=html5_td, multiplicity=Multiplicity(1, 1)),
        Property(name="html5_td5", type=html5_htmlElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_html5_div_container = Generalization(general=container, specific=html5_div)
gen_html5_table_htmlElement = Generalization(general=htmlElement, specific=html5_table)
gen_html5_img_htmlElement = Generalization(general=htmlElement, specific=html5_img)
gen_html5_label_htmlElement = Generalization(general=htmlElement, specific=html5_label)
gen_html5_input_htmlElement = Generalization(general=htmlElement, specific=html5_input)
gen_html5_button_htmlElement = Generalization(general=htmlElement, specific=html5_button)
gen_html5_fieldset_container = Generalization(general=container, specific=html5_fieldset)
gen_html5_dialog_htmlElement = Generalization(general=htmlElement, specific=html5_dialog)
gen_html5_select_htmlElement = Generalization(general=htmlElement, specific=html5_select)

# Domain Model
domain_model = DomainModel(
    name="html5",
    types={html5_div, container, html5_Action, html5_table, htmlElement, html5_tr, html5_td, html5_img, html5_label, html5_input, html5_button, html5_option, html5_fieldset, html5_legend, html5_html, html5_container, html5_dialog, html5_select, html5_htmlElement, types},
    associations={actions0, tr1, td2, legend6, container7, elements8, innercontainer12, options14, elements4},
    generalizations={gen_html5_div_container, gen_html5_table_htmlElement, gen_html5_img_htmlElement, gen_html5_label_htmlElement, gen_html5_input_htmlElement, gen_html5_button_htmlElement, gen_html5_fieldset_container, gen_html5_dialog_htmlElement, gen_html5_select_htmlElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)