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
Colour16: Enumeration = Enumeration(
    name="Colour16",
    literals={
            EnumerationLiteral(name="Aqua"),
			EnumerationLiteral(name="Black"),
			EnumerationLiteral(name="Blue"),
			EnumerationLiteral(name="Fuchsia"),
			EnumerationLiteral(name="Gray"),
			EnumerationLiteral(name="Green"),
			EnumerationLiteral(name="Lime"),
			EnumerationLiteral(name="Maroon"),
			EnumerationLiteral(name="Navy"),
			EnumerationLiteral(name="Olive"),
			EnumerationLiteral(name="Purple"),
			EnumerationLiteral(name="Red"),
			EnumerationLiteral(name="Silver"),
			EnumerationLiteral(name="Teal"),
			EnumerationLiteral(name="White"),
			EnumerationLiteral(name="Yellow")
    }
)

Orientation: Enumeration = Enumeration(
    name="Orientation",
    literals={
            EnumerationLiteral(name="undefined"),
			EnumerationLiteral(name="PtoT"),
			EnumerationLiteral(name="TtoP"),
			EnumerationLiteral(name="Inhibitor")
    }
)

# Classes
cpntools_Page = Class(name="cpntools::Page")
cpntools_Group = Class(name="cpntools::Group")
cpntools_Place = Class(name="cpntools::Place")
cpntools_Auxiliary = Class(name="cpntools::Auxiliary", is_abstract=True)
cpntools_Cpnet = Class(name="cpntools::Cpnet")
cpntools_Fusion = Class(name="cpntools::Fusion")
cpntools_Globbox = Class(name="cpntools::Globbox")
cpntools_Binder = Class(name="cpntools::Binder")
cpntools_ColorSet = Class(name="cpntools::ColorSet", is_abstract=True)
cpntools_Initmark = Class(name="cpntools::Initmark")
cpntools_Port = Class(name="cpntools::Port")
cpntools_Trans = Class(name="cpntools::Trans")
Declaration = Class(name="Declaration")
cpntools_Arc = Class(name="cpntools::Arc")
cpntools_DiagramElement = Class(name="cpntools::DiagramElement", is_abstract=True)
DiagramElement = Class(name="DiagramElement")
cpntools_Declaration = Class(name="cpntools::Declaration", is_abstract=True)
cpntools_Block = Class(name="cpntools::Block")
cpntools_AuxText = Class(name="cpntools::AuxText")
Auxiliary = Class(name="Auxiliary")
cpntools_Var = Class(name="cpntools::Var")
cpntools_Globref = Class(name="cpntools::Globref")
cpntools_Ml = Class(name="cpntools::Ml")
cpntools_TransPriority = Class(name="cpntools::TransPriority")
cpntools_TransTime = Class(name="cpntools::TransTime")
cpntools_Annot = Class(name="cpntools::Annot")
cpntools_TransCond = Class(name="cpntools::TransCond")
cpntools_Boolean = Class(name="cpntools::Boolean")
cpntools_Integer = Class(name="cpntools::Integer")
cpntools_LargeInteger = Class(name="cpntools::LargeInteger")
cpntools_Real = Class(name="cpntools::Real")
cpntools_Time = Class(name="cpntools::Time")
cpntools_String = Class(name="cpntools::String")
cpntools_AuxEllipse = Class(name="cpntools::AuxEllipse")
cpntools_AuxBox = Class(name="cpntools::AuxBox")
cpntools_SimpleColorSet = Class(name="cpntools::SimpleColorSet", is_abstract=True)
ColorSet = Class(name="ColorSet")
cpntools_CompoundColorSet = Class(name="cpntools::CompoundColorSet", is_abstract=True)
cpntools_Unit = Class(name="cpntools::Unit")
SimpleColorSet = Class(name="SimpleColorSet")
cpntools_Enumerated = Class(name="cpntools::Enumerated")
cpntools_Index = Class(name="cpntools::Index")
cpntools_Product = Class(name="cpntools::Product")
CompoundColorSet = Class(name="CompoundColorSet")
cpntools_Record = Class(name="cpntools::Record")
cpntools_List = Class(name="cpntools::List")
cpntools_Union = Class(name="cpntools::Union")
cpntools_Subset = Class(name="cpntools::Subset")
cpntools_Alias = Class(name="cpntools::Alias")

# cpntools_Page class attributes and methods
cpntools_Page_name: Property = Property(name="name", type=StringType)
cpntools_Page_m_layout: Method = Method(name="layout", parameters={Parameter(name='width'), Parameter(name='height'), Parameter(name='steps')})
cpntools_Page_m_layout: Method = Method(name="layout", parameters={})
cpntools_Page.attributes={cpntools_Page_name}
cpntools_Page.methods={cpntools_Page_m_layout, cpntools_Page_m_layout}

# cpntools_Group class attributes and methods
cpntools_Group_name: Property = Property(name="name", type=StringType)
cpntools_Group.attributes={cpntools_Group_name}

# cpntools_Place class attributes and methods
cpntools_Place_width: Property = Property(name="width", type=IntegerType)
cpntools_Place_text: Property = Property(name="text", type=StringType)
cpntools_Place_height: Property = Property(name="height", type=IntegerType)
cpntools_Place.attributes={cpntools_Place_height, cpntools_Place_width, cpntools_Place_text}

# cpntools_Auxiliary class attributes and methods

# cpntools_Cpnet class attributes and methods

# cpntools_Fusion class attributes and methods
cpntools_Fusion_name: Property = Property(name="name", type=StringType)
cpntools_Fusion.attributes={cpntools_Fusion_name}

# cpntools_Globbox class attributes and methods
cpntools_Globbox_name: Property = Property(name="name", type=StringType)
cpntools_Globbox.attributes={cpntools_Globbox_name}

# cpntools_Binder class attributes and methods
cpntools_Binder_posy: Property = Property(name="posy", type=IntegerType)
cpntools_Binder_posx: Property = Property(name="posx", type=IntegerType)
cpntools_Binder_width: Property = Property(name="width", type=IntegerType)
cpntools_Binder_height: Property = Property(name="height", type=IntegerType)
cpntools_Binder.attributes={cpntools_Binder_posy, cpntools_Binder_width, cpntools_Binder_height, cpntools_Binder_posx}

# cpntools_ColorSet class attributes and methods
cpntools_ColorSet_idname: Property = Property(name="idname", type=StringType)
cpntools_ColorSet_colorSetType: Property = Property(name="colorSetType", type=StringType)
cpntools_ColorSet_timed: Property = Property(name="timed", type=BooleanType)
cpntools_ColorSet_declare: Property = Property(name="declare", type=StringType)
cpntools_ColorSet.attributes={cpntools_ColorSet_colorSetType, cpntools_ColorSet_declare, cpntools_ColorSet_timed, cpntools_ColorSet_idname}

# cpntools_Initmark class attributes and methods
cpntools_Initmark_expression: Property = Property(name="expression", type=StringType)
cpntools_Initmark.attributes={cpntools_Initmark_expression}

# cpntools_Port class attributes and methods
cpntools_Port_portType: Property = Property(name="portType", type=StringType)
cpntools_Port.attributes={cpntools_Port_portType}

# cpntools_Trans class attributes and methods
cpntools_Trans_height: Property = Property(name="height", type=IntegerType)
cpntools_Trans_width: Property = Property(name="width", type=IntegerType)
cpntools_Trans_explicit: Property = Property(name="explicit", type=BooleanType)
cpntools_Trans_text: Property = Property(name="text", type=StringType)
cpntools_Trans.attributes={cpntools_Trans_width, cpntools_Trans_height, cpntools_Trans_text, cpntools_Trans_explicit}

# Declaration class attributes and methods

# cpntools_Arc class attributes and methods
cpntools_Arc_headsize: Property = Property(name="headsize", type=FloatType)
cpntools_Arc_orientation: Property = Property(name="orientation", type=StringType)
cpntools_Arc_currentcyckle: Property = Property(name="currentcyckle", type=StringType)
cpntools_Arc_order: Property = Property(name="order", type=IntegerType)
cpntools_Arc.attributes={cpntools_Arc_order, cpntools_Arc_orientation, cpntools_Arc_currentcyckle, cpntools_Arc_headsize}

# cpntools_DiagramElement class attributes and methods
cpntools_DiagramElement_lineColour: Property = Property(name="lineColour", type=StringType)
cpntools_DiagramElement_fillFilled: Property = Property(name="fillFilled", type=BooleanType)
cpntools_DiagramElement_lineThick: Property = Property(name="lineThick", type=IntegerType)
cpntools_DiagramElement_posx: Property = Property(name="posx", type=IntegerType)
cpntools_DiagramElement_lineType: Property = Property(name="lineType", type=StringType)
cpntools_DiagramElement_posy: Property = Property(name="posy", type=IntegerType)
cpntools_DiagramElement_fillColour: Property = Property(name="fillColour", type=StringType)
cpntools_DiagramElement_fillPattern: Property = Property(name="fillPattern", type=StringType)
cpntools_DiagramElement.attributes={cpntools_DiagramElement_fillColour, cpntools_DiagramElement_posx, cpntools_DiagramElement_fillPattern, cpntools_DiagramElement_lineType, cpntools_DiagramElement_lineThick, cpntools_DiagramElement_lineColour, cpntools_DiagramElement_posy, cpntools_DiagramElement_fillFilled}

# DiagramElement class attributes and methods

# cpntools_Declaration class attributes and methods

# cpntools_Block class attributes and methods
cpntools_Block_idname: Property = Property(name="idname", type=StringType)
cpntools_Block.attributes={cpntools_Block_idname}

# cpntools_AuxText class attributes and methods
cpntools_AuxText_text: Property = Property(name="text", type=StringType)
cpntools_AuxText.attributes={cpntools_AuxText_text}

# Auxiliary class attributes and methods

# cpntools_Var class attributes and methods
cpntools_Var_idname: Property = Property(name="idname", type=StringType)
cpntools_Var.attributes={cpntools_Var_idname}

# cpntools_Globref class attributes and methods
cpntools_Globref_idname: Property = Property(name="idname", type=StringType)
cpntools_Globref.attributes={cpntools_Globref_idname}

# cpntools_Ml class attributes and methods
cpntools_Ml_expression: Property = Property(name="expression", type=StringType)
cpntools_Ml.attributes={cpntools_Ml_expression}

# cpntools_TransPriority class attributes and methods
cpntools_TransPriority_text: Property = Property(name="text", type=StringType)
cpntools_TransPriority.attributes={cpntools_TransPriority_text}

# cpntools_TransTime class attributes and methods
cpntools_TransTime_text: Property = Property(name="text", type=StringType)
cpntools_TransTime.attributes={cpntools_TransTime_text}

# cpntools_Annot class attributes and methods
cpntools_Annot_text: Property = Property(name="text", type=StringType)
cpntools_Annot.attributes={cpntools_Annot_text}

# cpntools_TransCond class attributes and methods
cpntools_TransCond_text: Property = Property(name="text", type=StringType)
cpntools_TransCond.attributes={cpntools_TransCond_text}

# cpntools_Boolean class attributes and methods
cpntools_Boolean_with: Property = Property(name="with", type=StringType)
cpntools_Boolean.attributes={cpntools_Boolean_with}

# cpntools_Integer class attributes and methods
cpntools_Integer_with: Property = Property(name="with", type=StringType)
cpntools_Integer.attributes={cpntools_Integer_with}

# cpntools_LargeInteger class attributes and methods
cpntools_LargeInteger_with: Property = Property(name="with", type=StringType)
cpntools_LargeInteger.attributes={cpntools_LargeInteger_with}

# cpntools_Real class attributes and methods
cpntools_Real_with: Property = Property(name="with", type=StringType)
cpntools_Real.attributes={cpntools_Real_with}

# cpntools_Time class attributes and methods

# cpntools_String class attributes and methods
cpntools_String_with: Property = Property(name="with", type=StringType)
cpntools_String_and: Property = Property(name="and", type=StringType)
cpntools_String.attributes={cpntools_String_with, cpntools_String_and}

# cpntools_AuxEllipse class attributes and methods
cpntools_AuxEllipse_height: Property = Property(name="height", type=IntegerType)
cpntools_AuxEllipse_width: Property = Property(name="width", type=IntegerType)
cpntools_AuxEllipse.attributes={cpntools_AuxEllipse_width, cpntools_AuxEllipse_height}

# cpntools_AuxBox class attributes and methods
cpntools_AuxBox_height: Property = Property(name="height", type=IntegerType)
cpntools_AuxBox_width: Property = Property(name="width", type=IntegerType)
cpntools_AuxBox.attributes={cpntools_AuxBox_width, cpntools_AuxBox_height}

# cpntools_SimpleColorSet class attributes and methods

# ColorSet class attributes and methods

# cpntools_CompoundColorSet class attributes and methods

# cpntools_Unit class attributes and methods
cpntools_Unit_with: Property = Property(name="with", type=StringType)
cpntools_Unit.attributes={cpntools_Unit_with}

# SimpleColorSet class attributes and methods

# cpntools_Enumerated class attributes and methods
cpntools_Enumerated_with: Property = Property(name="with", type=StringType)
cpntools_Enumerated.attributes={cpntools_Enumerated_with}

# cpntools_Index class attributes and methods
cpntools_Index_with: Property = Property(name="with", type=StringType)
cpntools_Index.attributes={cpntools_Index_with}

# cpntools_Product class attributes and methods

# CompoundColorSet class attributes and methods

# cpntools_Record class attributes and methods

# cpntools_List class attributes and methods

# cpntools_Union class attributes and methods

# cpntools_Subset class attributes and methods

# cpntools_Alias class attributes and methods

# Relationships
group5: BinaryAssociation = BinaryAssociation(
    name="group5",
    ends={
        Property(name="Group", type=cpntools_Page, multiplicity=Multiplicity(1, 1)),
        Property(name="page", type=cpntools_Group, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
places6: BinaryAssociation = BinaryAssociation(
    name="places6",
    ends={
        Property(name="Place", type=cpntools_Page, multiplicity=Multiplicity(1, 1)),
        Property(name="page7", type=cpntools_Place, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
auxiliarys8: BinaryAssociation = BinaryAssociation(
    name="auxiliarys8",
    ends={
        Property(name="Auxiliary", type=cpntools_Page, multiplicity=Multiplicity(1, 1)),
        Property(name="page9", type=cpntools_Auxiliary, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fusions0: BinaryAssociation = BinaryAssociation(
    name="fusions0",
    ends={
        Property(name="Fusion", type=cpntools_Cpnet, multiplicity=Multiplicity(1, 1)),
        Property(name="cpnet", type=cpntools_Fusion, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
globbox1: BinaryAssociation = BinaryAssociation(
    name="globbox1",
    ends={
        Property(name="Globbox", type=cpntools_Cpnet, multiplicity=Multiplicity(1, 1)),
        Property(name="cpnet2", type=cpntools_Globbox, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
binder3: BinaryAssociation = BinaryAssociation(
    name="binder3",
    ends={
        Property(name="Binder", type=cpntools_Cpnet, multiplicity=Multiplicity(1, 1)),
        Property(name="cpnet4", type=cpntools_Binder, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type21: BinaryAssociation = BinaryAssociation(
    name="type21",
    ends={
        Property(name="cpntools_ColorSet", type=cpntools_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="cpntools_Place", type=cpntools_ColorSet, multiplicity=Multiplicity(1, 1))
    }
)
initmark22: BinaryAssociation = BinaryAssociation(
    name="initmark22",
    ends={
        Property(name="cpntools_Initmark", type=cpntools_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="cpntools_Place23", type=cpntools_Initmark, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
port24: BinaryAssociation = BinaryAssociation(
    name="port24",
    ends={
        Property(name="cpntools_Port", type=cpntools_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="cpntools_Place25", type=cpntools_Port, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fusion26: BinaryAssociation = BinaryAssociation(
    name="fusion26",
    ends={
        Property(name="Fusion27", type=cpntools_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="places", type=cpntools_Fusion, multiplicity=Multiplicity(0, 1))
    }
)
page28: BinaryAssociation = BinaryAssociation(
    name="page28",
    ends={
        Property(name="Page30", type=cpntools_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="places29", type=cpntools_Page, multiplicity=Multiplicity(1, 1))
    }
)
arcs31: BinaryAssociation = BinaryAssociation(
    name="arcs31",
    ends={
        Property(name="Arc32", type=cpntools_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="place", type=cpntools_Arc, multiplicity=Multiplicity(0, 9999))
    }
)
transs10: BinaryAssociation = BinaryAssociation(
    name="transs10",
    ends={
        Property(name="Trans", type=cpntools_Page, multiplicity=Multiplicity(1, 1)),
        Property(name="page11", type=cpntools_Trans, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arcs12: BinaryAssociation = BinaryAssociation(
    name="arcs12",
    ends={
        Property(name="Arc", type=cpntools_Page, multiplicity=Multiplicity(1, 1)),
        Property(name="page13", type=cpntools_Arc, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
binder14: BinaryAssociation = BinaryAssociation(
    name="binder14",
    ends={
        Property(name="Binder15", type=cpntools_Page, multiplicity=Multiplicity(1, 1)),
        Property(name="pages", type=cpntools_Binder, multiplicity=Multiplicity(0, 1))
    }
)
groupElms16: BinaryAssociation = BinaryAssociation(
    name="groupElms16",
    ends={
        Property(name="DiagramElement", type=cpntools_Group, multiplicity=Multiplicity(1, 1)),
        Property(name="group", type=cpntools_DiagramElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
page17: BinaryAssociation = BinaryAssociation(
    name="page17",
    ends={
        Property(name="Page", type=cpntools_Group, multiplicity=Multiplicity(1, 1)),
        Property(name="group18", type=cpntools_Page, multiplicity=Multiplicity(1, 1))
    }
)
group19: BinaryAssociation = BinaryAssociation(
    name="group19",
    ends={
        Property(name="Group20", type=cpntools_DiagramElement, multiplicity=Multiplicity(1, 1)),
        Property(name="groupElms", type=cpntools_Group, multiplicity=Multiplicity(0, 1))
    }
)
places37: BinaryAssociation = BinaryAssociation(
    name="places37",
    ends={
        Property(name="Place38", type=cpntools_Fusion, multiplicity=Multiplicity(1, 1)),
        Property(name="fusion", type=cpntools_Place, multiplicity=Multiplicity(0, 9999))
    }
)
cpnet39: BinaryAssociation = BinaryAssociation(
    name="cpnet39",
    ends={
        Property(name="Cpnet", type=cpntools_Fusion, multiplicity=Multiplicity(1, 1)),
        Property(name="fusions", type=cpntools_Cpnet, multiplicity=Multiplicity(0, 1))
    }
)
page40: BinaryAssociation = BinaryAssociation(
    name="page40",
    ends={
        Property(name="Page41", type=cpntools_Auxiliary, multiplicity=Multiplicity(1, 1)),
        Property(name="auxiliarys", type=cpntools_Page, multiplicity=Multiplicity(1, 1))
    }
)
cpnet42: BinaryAssociation = BinaryAssociation(
    name="cpnet42",
    ends={
        Property(name="Cpnet43", type=cpntools_Globbox, multiplicity=Multiplicity(1, 1)),
        Property(name="globbox", type=cpntools_Cpnet, multiplicity=Multiplicity(0, 1))
    }
)
declarations44: BinaryAssociation = BinaryAssociation(
    name="declarations44",
    ends={
        Property(name="Declaration", type=cpntools_Globbox, multiplicity=Multiplicity(1, 1)),
        Property(name="globbox45", type=cpntools_Declaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
globbox33: BinaryAssociation = BinaryAssociation(
    name="globbox33",
    ends={
        Property(name="Globbox34", type=cpntools_Declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="declarations", type=cpntools_Globbox, multiplicity=Multiplicity(0, 1))
    }
)
block35: BinaryAssociation = BinaryAssociation(
    name="block35",
    ends={
        Property(name="Block", type=cpntools_Declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="declarations36", type=cpntools_Block, multiplicity=Multiplicity(0, 1))
    }
)
place50: BinaryAssociation = BinaryAssociation(
    name="place50",
    ends={
        Property(name="Place51", type=cpntools_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="arcs", type=cpntools_Place, multiplicity=Multiplicity(1, 1))
    }
)
trans52: BinaryAssociation = BinaryAssociation(
    name="trans52",
    ends={
        Property(name="Trans54", type=cpntools_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="arcs53", type=cpntools_Trans, multiplicity=Multiplicity(1, 1))
    }
)
type46: BinaryAssociation = BinaryAssociation(
    name="type46",
    ends={
        Property(name="cpntools_ColorSet47", type=cpntools_Var, multiplicity=Multiplicity(1, 1)),
        Property(name="cpntools_Var", type=cpntools_ColorSet, multiplicity=Multiplicity(1, 1))
    }
)
declarations48: BinaryAssociation = BinaryAssociation(
    name="declarations48",
    ends={
        Property(name="Declaration49", type=cpntools_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="block", type=cpntools_Declaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arcs62: BinaryAssociation = BinaryAssociation(
    name="arcs62",
    ends={
        Property(name="trans", type=cpntools_Arc, multiplicity=Multiplicity(0, 9999)),
        Property(name="Arc63", type=cpntools_Trans, multiplicity=Multiplicity(1, 1))
    }
)
priority64: BinaryAssociation = BinaryAssociation(
    name="priority64",
    ends={
        Property(name="cpntools_TransPriority", type=cpntools_Trans, multiplicity=Multiplicity(1, 1)),
        Property(name="cpntools_Trans65", type=cpntools_TransPriority, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
time66: BinaryAssociation = BinaryAssociation(
    name="time66",
    ends={
        Property(name="cpntools_TransTime", type=cpntools_Trans, multiplicity=Multiplicity(1, 1)),
        Property(name="cpntools_Trans67", type=cpntools_TransTime, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
annot55: BinaryAssociation = BinaryAssociation(
    name="annot55",
    ends={
        Property(name="cpntools_Annot", type=cpntools_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="cpntools_Arc", type=cpntools_Annot, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
page56: BinaryAssociation = BinaryAssociation(
    name="page56",
    ends={
        Property(name="Page58", type=cpntools_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="arcs57", type=cpntools_Page, multiplicity=Multiplicity(1, 1))
    }
)
cond59: BinaryAssociation = BinaryAssociation(
    name="cond59",
    ends={
        Property(name="cpntools_TransCond", type=cpntools_Trans, multiplicity=Multiplicity(1, 1)),
        Property(name="cpntools_Trans", type=cpntools_TransCond, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
page60: BinaryAssociation = BinaryAssociation(
    name="page60",
    ends={
        Property(name="Page61", type=cpntools_Trans, multiplicity=Multiplicity(1, 1)),
        Property(name="transs", type=cpntools_Page, multiplicity=Multiplicity(1, 1))
    }
)
simpleColors68: BinaryAssociation = BinaryAssociation(
    name="simpleColors68",
    ends={
        Property(name="cpntools_SimpleColorSet", type=cpntools_CompoundColorSet, multiplicity=Multiplicity(1, 1)),
        Property(name="cpntools_CompoundColorSet", type=cpntools_SimpleColorSet, multiplicity=Multiplicity(1, 9999))
    }
)
cpnet69: BinaryAssociation = BinaryAssociation(
    name="cpnet69",
    ends={
        Property(name="Cpnet70", type=cpntools_Binder, multiplicity=Multiplicity(1, 1)),
        Property(name="binder", type=cpntools_Cpnet, multiplicity=Multiplicity(0, 1))
    }
)
pages71: BinaryAssociation = BinaryAssociation(
    name="pages71",
    ends={
        Property(name="Page73", type=cpntools_Binder, multiplicity=Multiplicity(1, 1)),
        Property(name="binder72", type=cpntools_Page, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_cpntools_ColorSet_Declaration = Generalization(general=Declaration, specific=cpntools_ColorSet)
gen_cpntools_Place_DiagramElement = Generalization(general=DiagramElement, specific=cpntools_Place)
gen_cpntools_Auxiliary_DiagramElement = Generalization(general=DiagramElement, specific=cpntools_Auxiliary)
gen_cpntools_Initmark_DiagramElement = Generalization(general=DiagramElement, specific=cpntools_Initmark)
gen_cpntools_Port_DiagramElement = Generalization(general=DiagramElement, specific=cpntools_Port)
gen_cpntools_AuxText_Auxiliary = Generalization(general=Auxiliary, specific=cpntools_AuxText)
gen_cpntools_Arc_DiagramElement = Generalization(general=DiagramElement, specific=cpntools_Arc)
gen_cpntools_Var_Declaration = Generalization(general=Declaration, specific=cpntools_Var)
gen_cpntools_Globref_Declaration = Generalization(general=Declaration, specific=cpntools_Globref)
gen_cpntools_Ml_Declaration = Generalization(general=Declaration, specific=cpntools_Ml)
gen_cpntools_Block_Declaration = Generalization(general=Declaration, specific=cpntools_Block)
gen_cpntools_TransCond_DiagramElement = Generalization(general=DiagramElement, specific=cpntools_TransCond)
gen_cpntools_TransPriority_DiagramElement = Generalization(general=DiagramElement, specific=cpntools_TransPriority)
gen_cpntools_TransTime_DiagramElement = Generalization(general=DiagramElement, specific=cpntools_TransTime)
gen_cpntools_Annot_DiagramElement = Generalization(general=DiagramElement, specific=cpntools_Annot)
gen_cpntools_Trans_DiagramElement = Generalization(general=DiagramElement, specific=cpntools_Trans)
gen_cpntools_Boolean_SimpleColorSet = Generalization(general=SimpleColorSet, specific=cpntools_Boolean)
gen_cpntools_Integer_SimpleColorSet = Generalization(general=SimpleColorSet, specific=cpntools_Integer)
gen_cpntools_LargeInteger_SimpleColorSet = Generalization(general=SimpleColorSet, specific=cpntools_LargeInteger)
gen_cpntools_Real_SimpleColorSet = Generalization(general=SimpleColorSet, specific=cpntools_Real)
gen_cpntools_Time_SimpleColorSet = Generalization(general=SimpleColorSet, specific=cpntools_Time)
gen_cpntools_String_SimpleColorSet = Generalization(general=SimpleColorSet, specific=cpntools_String)
gen_cpntools_AuxEllipse_Auxiliary = Generalization(general=Auxiliary, specific=cpntools_AuxEllipse)
gen_cpntools_AuxBox_Auxiliary = Generalization(general=Auxiliary, specific=cpntools_AuxBox)
gen_cpntools_SimpleColorSet_ColorSet = Generalization(general=ColorSet, specific=cpntools_SimpleColorSet)
gen_cpntools_CompoundColorSet_ColorSet = Generalization(general=ColorSet, specific=cpntools_CompoundColorSet)
gen_cpntools_Unit_SimpleColorSet = Generalization(general=SimpleColorSet, specific=cpntools_Unit)
gen_cpntools_Enumerated_SimpleColorSet = Generalization(general=SimpleColorSet, specific=cpntools_Enumerated)
gen_cpntools_Index_SimpleColorSet = Generalization(general=SimpleColorSet, specific=cpntools_Index)
gen_cpntools_Product_CompoundColorSet = Generalization(general=CompoundColorSet, specific=cpntools_Product)
gen_cpntools_Record_CompoundColorSet = Generalization(general=CompoundColorSet, specific=cpntools_Record)
gen_cpntools_List_CompoundColorSet = Generalization(general=CompoundColorSet, specific=cpntools_List)
gen_cpntools_Union_CompoundColorSet = Generalization(general=CompoundColorSet, specific=cpntools_Union)
gen_cpntools_Subset_CompoundColorSet = Generalization(general=CompoundColorSet, specific=cpntools_Subset)
gen_cpntools_Alias_CompoundColorSet = Generalization(general=CompoundColorSet, specific=cpntools_Alias)

# Domain Model
domain_model = DomainModel(
    name="cpntools",
    types={cpntools_Page, cpntools_Group, cpntools_Place, cpntools_Auxiliary, cpntools_Cpnet, cpntools_Fusion, cpntools_Globbox, cpntools_Binder, cpntools_ColorSet, cpntools_Initmark, cpntools_Port, cpntools_Trans, Declaration, cpntools_Arc, cpntools_DiagramElement, DiagramElement, cpntools_Declaration, cpntools_Block, cpntools_AuxText, Auxiliary, cpntools_Var, cpntools_Globref, cpntools_Ml, cpntools_TransPriority, cpntools_TransTime, cpntools_Annot, cpntools_TransCond, cpntools_Boolean, cpntools_Integer, cpntools_LargeInteger, cpntools_Real, cpntools_Time, cpntools_String, cpntools_AuxEllipse, cpntools_AuxBox, cpntools_SimpleColorSet, ColorSet, cpntools_CompoundColorSet, cpntools_Unit, SimpleColorSet, cpntools_Enumerated, cpntools_Index, cpntools_Product, CompoundColorSet, cpntools_Record, cpntools_List, cpntools_Union, cpntools_Subset, cpntools_Alias, Colour16, Orientation},
    associations={group5, places6, auxiliarys8, fusions0, globbox1, binder3, type21, initmark22, port24, fusion26, page28, arcs31, transs10, arcs12, binder14, groupElms16, page17, group19, places37, cpnet39, page40, cpnet42, declarations44, globbox33, block35, place50, trans52, type46, declarations48, arcs62, priority64, time66, annot55, page56, cond59, page60, simpleColors68, cpnet69, pages71},
    generalizations={gen_cpntools_ColorSet_Declaration, gen_cpntools_Place_DiagramElement, gen_cpntools_Auxiliary_DiagramElement, gen_cpntools_Initmark_DiagramElement, gen_cpntools_Port_DiagramElement, gen_cpntools_AuxText_Auxiliary, gen_cpntools_Arc_DiagramElement, gen_cpntools_Var_Declaration, gen_cpntools_Globref_Declaration, gen_cpntools_Ml_Declaration, gen_cpntools_Block_Declaration, gen_cpntools_TransCond_DiagramElement, gen_cpntools_TransPriority_DiagramElement, gen_cpntools_TransTime_DiagramElement, gen_cpntools_Annot_DiagramElement, gen_cpntools_Trans_DiagramElement, gen_cpntools_Boolean_SimpleColorSet, gen_cpntools_Integer_SimpleColorSet, gen_cpntools_LargeInteger_SimpleColorSet, gen_cpntools_Real_SimpleColorSet, gen_cpntools_Time_SimpleColorSet, gen_cpntools_String_SimpleColorSet, gen_cpntools_AuxEllipse_Auxiliary, gen_cpntools_AuxBox_Auxiliary, gen_cpntools_SimpleColorSet_ColorSet, gen_cpntools_CompoundColorSet_ColorSet, gen_cpntools_Unit_SimpleColorSet, gen_cpntools_Enumerated_SimpleColorSet, gen_cpntools_Index_SimpleColorSet, gen_cpntools_Product_CompoundColorSet, gen_cpntools_Record_CompoundColorSet, gen_cpntools_List_CompoundColorSet, gen_cpntools_Union_CompoundColorSet, gen_cpntools_Subset_CompoundColorSet, gen_cpntools_Alias_CompoundColorSet},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)