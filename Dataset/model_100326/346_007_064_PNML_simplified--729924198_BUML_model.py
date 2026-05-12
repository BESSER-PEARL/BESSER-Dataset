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
PNML_LocatedElement = Class(name="PNML_LocatedElement", is_abstract=True)
PNML_LabeledElement = Class(name="PNML_LabeledElement", is_abstract=True)
PNML_IdedElement = Class(name="PNML_IdedElement", is_abstract=True)
LocatedElement = Class(name="LocatedElement")
PNML_URI = Class(name="PNML_URI")
PNML_PNMLDocument = Class(name="PNML_PNMLDocument")
URI = Class(name="URI")
NetElement = Class(name="NetElement")
PNML_NetElement = Class(name="PNML_NetElement")
IdedElement = Class(name="IdedElement")
PNMLDocument = Class(name="PNMLDocument")
NetContent = Class(name="NetContent")
Name = Class(name="Name")
PNML_NetContent = Class(name="PNML_NetContent", is_abstract=True)
Label = Class(name="Label")
PNML_Label = Class(name="PNML_Label")
LabeledElement = Class(name="LabeledElement")
PNML_Name = Class(name="PNML_Name")
PNML_NetContentElement = Class(name="PNML_NetContentElement", is_abstract=True)
PNML_Arc = Class(name="PNML_Arc")
NetContentElement = Class(name="NetContentElement")
PNML_Place = Class(name="PNML_Place")
PNML_Transition = Class(name="PNML_Transition")

# PNML_LocatedElement class attributes and methods
PNML_LocatedElement_location: Property = Property(name="location", type=StringType)
PNML_LocatedElement.attributes={PNML_LocatedElement_location}

# PNML_LabeledElement class attributes and methods

# PNML_IdedElement class attributes and methods
PNML_IdedElement_id: Property = Property(name="id", type=StringType)
PNML_IdedElement.attributes={PNML_IdedElement_id}

# LocatedElement class attributes and methods

# PNML_URI class attributes and methods
PNML_URI_value: Property = Property(name="value", type=StringType)
PNML_URI.attributes={PNML_URI_value}

# PNML_PNMLDocument class attributes and methods

# URI class attributes and methods

# NetElement class attributes and methods

# PNML_NetElement class attributes and methods

# IdedElement class attributes and methods

# PNMLDocument class attributes and methods

# NetContent class attributes and methods

# Name class attributes and methods

# PNML_NetContent class attributes and methods

# Label class attributes and methods

# PNML_Label class attributes and methods
PNML_Label_text: Property = Property(name="text", type=StringType)
PNML_Label.attributes={PNML_Label_text}

# LabeledElement class attributes and methods

# PNML_Name class attributes and methods

# PNML_NetContentElement class attributes and methods

# PNML_Arc class attributes and methods

# NetContentElement class attributes and methods

# PNML_Place class attributes and methods

# PNML_Transition class attributes and methods

# Relationships
name10: BinaryAssociation = BinaryAssociation(
    name="name10",
    ends={
        Property(name="Name11", type=PNML_NetContent, multiplicity=Multiplicity(1, 1)),
        Property(name="netContent", type=Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
xmlns0: BinaryAssociation = BinaryAssociation(
    name="xmlns0",
    ends={
        Property(name="URI", type=PNML_PNMLDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="PNML_PNMLDocument", type=URI, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
nets1: BinaryAssociation = BinaryAssociation(
    name="nets1",
    ends={
        Property(name="NetElement", type=PNML_PNMLDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="document", type=NetElement, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
type2: BinaryAssociation = BinaryAssociation(
    name="type2",
    ends={
        Property(name="URI3", type=PNML_NetElement, multiplicity=Multiplicity(1, 1)),
        Property(name="PNML_NetElement", type=URI, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
document4: BinaryAssociation = BinaryAssociation(
    name="document4",
    ends={
        Property(name="PNMLDocument", type=PNML_NetElement, multiplicity=Multiplicity(1, 1)),
        Property(name="nets", type=PNMLDocument, multiplicity=Multiplicity(1, 1))
    }
)
contents5: BinaryAssociation = BinaryAssociation(
    name="contents5",
    ends={
        Property(name="NetContent", type=PNML_NetElement, multiplicity=Multiplicity(1, 1)),
        Property(name="net", type=NetContent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name6: BinaryAssociation = BinaryAssociation(
    name="name6",
    ends={
        Property(name="Name", type=PNML_NetElement, multiplicity=Multiplicity(1, 1)),
        Property(name="net7", type=Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
net8: BinaryAssociation = BinaryAssociation(
    name="net8",
    ends={
        Property(name="NetElement9", type=PNML_NetContent, multiplicity=Multiplicity(1, 1)),
        Property(name="contents", type=NetElement, multiplicity=Multiplicity(1, 1))
    }
)
labels12: BinaryAssociation = BinaryAssociation(
    name="labels12",
    ends={
        Property(name="Label", type=PNML_LabeledElement, multiplicity=Multiplicity(1, 1)),
        Property(name="labeledElement", type=Label, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
labeledElement13: BinaryAssociation = BinaryAssociation(
    name="labeledElement13",
    ends={
        Property(name="LabeledElement", type=PNML_Label, multiplicity=Multiplicity(1, 1)),
        Property(name="labels", type=LabeledElement, multiplicity=Multiplicity(1, 1))
    }
)
net14: BinaryAssociation = BinaryAssociation(
    name="net14",
    ends={
        Property(name="NetElement15", type=PNML_Name, multiplicity=Multiplicity(1, 1)),
        Property(name="name", type=NetElement, multiplicity=Multiplicity(0, 1))
    }
)
netContent16: BinaryAssociation = BinaryAssociation(
    name="netContent16",
    ends={
        Property(name="NetContent18", type=PNML_Name, multiplicity=Multiplicity(1, 1)),
        Property(name="name17", type=NetContent, multiplicity=Multiplicity(0, 1))
    }
)
source19: BinaryAssociation = BinaryAssociation(
    name="source19",
    ends={
        Property(name="NetContentElement", type=PNML_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="PNML_Arc", type=NetContentElement, multiplicity=Multiplicity(1, 1))
    }
)
target20: BinaryAssociation = BinaryAssociation(
    name="target20",
    ends={
        Property(name="NetContentElement22", type=PNML_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="PNML_Arc21", type=NetContentElement, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_PNML_LabeledElement_LocatedElement = Generalization(general=LocatedElement, specific=PNML_LabeledElement)
gen_PNML_IdedElement_LocatedElement = Generalization(general=LocatedElement, specific=PNML_IdedElement)
gen_PNML_URI_LocatedElement = Generalization(general=LocatedElement, specific=PNML_URI)
gen_PNML_PNMLDocument_LocatedElement = Generalization(general=LocatedElement, specific=PNML_PNMLDocument)
gen_PNML_NetElement_IdedElement = Generalization(general=IdedElement, specific=PNML_NetElement)
gen_PNML_NetContent_LocatedElement = Generalization(general=LocatedElement, specific=PNML_NetContent)
gen_PNML_Label_LocatedElement = Generalization(general=LocatedElement, specific=PNML_Label)
gen_PNML_Name_LabeledElement = Generalization(general=LabeledElement, specific=PNML_Name)
gen_PNML_NetContentElement_NetContent = Generalization(general=NetContent, specific=PNML_NetContentElement)
gen_PNML_NetContentElement_IdedElement = Generalization(general=IdedElement, specific=PNML_NetContentElement)
gen_PNML_Arc_NetContent = Generalization(general=NetContent, specific=PNML_Arc)
gen_PNML_Arc_IdedElement = Generalization(general=IdedElement, specific=PNML_Arc)
gen_PNML_Place_NetContentElement = Generalization(general=NetContentElement, specific=PNML_Place)
gen_PNML_Transition_NetContentElement = Generalization(general=NetContentElement, specific=PNML_Transition)

# Domain Model
domain_model = DomainModel(
    name="PrimitiveTypes",
    types={PNML_LocatedElement, PNML_LabeledElement, PNML_IdedElement, LocatedElement, PNML_URI, PNML_PNMLDocument, URI, NetElement, PNML_NetElement, IdedElement, PNMLDocument, NetContent, Name, PNML_NetContent, Label, PNML_Label, LabeledElement, PNML_Name, PNML_NetContentElement, PNML_Arc, NetContentElement, PNML_Place, PNML_Transition},
    associations={name10, xmlns0, nets1, type2, document4, contents5, name6, net8, labels12, labeledElement13, net14, netContent16, source19, target20},
    generalizations={gen_PNML_LabeledElement_LocatedElement, gen_PNML_IdedElement_LocatedElement, gen_PNML_URI_LocatedElement, gen_PNML_PNMLDocument_LocatedElement, gen_PNML_NetElement_IdedElement, gen_PNML_NetContent_LocatedElement, gen_PNML_Label_LocatedElement, gen_PNML_Name_LabeledElement, gen_PNML_NetContentElement_NetContent, gen_PNML_NetContentElement_IdedElement, gen_PNML_Arc_NetContent, gen_PNML_Arc_IdedElement, gen_PNML_Place_NetContentElement, gen_PNML_Transition_NetContentElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)