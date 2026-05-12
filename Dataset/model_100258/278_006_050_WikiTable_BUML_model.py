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
WikiTable_LocatedElement = Class(name="WikiTable_LocatedElement", is_abstract=True)
WikiTable_Table = Class(name="WikiTable_Table")
LocatedElement = Class(name="LocatedElement")
Caption = Class(name="Caption")
Row = Class(name="Row")
WikiTable_Caption = Class(name="WikiTable_Caption")
WikiTable_Row = Class(name="WikiTable_Row")
Cell = Class(name="Cell")
WikiTable_Cell = Class(name="WikiTable_Cell")

# WikiTable_LocatedElement class attributes and methods
WikiTable_LocatedElement_location: Property = Property(name="location", type=StringType)
WikiTable_LocatedElement_commentsBefore: Property = Property(name="commentsBefore", type=StringType)
WikiTable_LocatedElement_commentsAfter: Property = Property(name="commentsAfter", type=StringType)
WikiTable_LocatedElement.attributes={WikiTable_LocatedElement_commentsBefore, WikiTable_LocatedElement_location, WikiTable_LocatedElement_commentsAfter}

# WikiTable_Table class attributes and methods
WikiTable_Table_border: Property = Property(name="border", type=StringType)
WikiTable_Table_style: Property = Property(name="style", type=StringType)
WikiTable_Table_class_: Property = Property(name="class_", type=StringType)
WikiTable_Table.attributes={WikiTable_Table_style, WikiTable_Table_class_, WikiTable_Table_border}

# LocatedElement class attributes and methods

# Caption class attributes and methods

# Row class attributes and methods

# WikiTable_Caption class attributes and methods
WikiTable_Caption_content: Property = Property(name="content", type=StringType)
WikiTable_Caption.attributes={WikiTable_Caption_content}

# WikiTable_Row class attributes and methods

# Cell class attributes and methods

# WikiTable_Cell class attributes and methods
WikiTable_Cell_content: Property = Property(name="content", type=StringType)
WikiTable_Cell_isHeading: Property = Property(name="isHeading", type=StringType)
WikiTable_Cell_align: Property = Property(name="align", type=StringType)
WikiTable_Cell_style: Property = Property(name="style", type=StringType)
WikiTable_Cell.attributes={WikiTable_Cell_content, WikiTable_Cell_isHeading, WikiTable_Cell_style, WikiTable_Cell_align}

# Relationships
caption0: BinaryAssociation = BinaryAssociation(
    name="caption0",
    ends={
        Property(name="Caption", type=WikiTable_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="WikiTable_Table", type=Caption, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rows1: BinaryAssociation = BinaryAssociation(
    name="rows1",
    ends={
        Property(name="Row", type=WikiTable_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="WikiTable_Table2", type=Row, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cells3: BinaryAssociation = BinaryAssociation(
    name="cells3",
    ends={
        Property(name="Cell", type=WikiTable_Row, multiplicity=Multiplicity(1, 1)),
        Property(name="WikiTable_Row", type=Cell, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_WikiTable_Table_LocatedElement = Generalization(general=LocatedElement, specific=WikiTable_Table)
gen_WikiTable_Caption_LocatedElement = Generalization(general=LocatedElement, specific=WikiTable_Caption)
gen_WikiTable_Row_LocatedElement = Generalization(general=LocatedElement, specific=WikiTable_Row)
gen_WikiTable_Cell_LocatedElement = Generalization(general=LocatedElement, specific=WikiTable_Cell)

# Domain Model
domain_model = DomainModel(
    name="PrimitiveTypes",
    types={WikiTable_LocatedElement, WikiTable_Table, LocatedElement, Caption, Row, WikiTable_Caption, WikiTable_Row, Cell, WikiTable_Cell},
    associations={caption0, rows1, cells3},
    generalizations={gen_WikiTable_Table_LocatedElement, gen_WikiTable_Caption_LocatedElement, gen_WikiTable_Row_LocatedElement, gen_WikiTable_Cell_LocatedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)