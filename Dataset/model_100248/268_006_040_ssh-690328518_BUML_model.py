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
spreadsheet_Image = Class(name="spreadsheet_Image")
spreadsheet_Table = Class(name="spreadsheet_Table")
spreadsheet_SpreadsheetFile = Class(name="spreadsheet_SpreadsheetFile")
DocumentModel = Class(name="DocumentModel")
spreadsheet_Sheet = Class(name="spreadsheet_Sheet")
spreadsheet_Text = Class(name="spreadsheet_Text")
spreadsheet_Title = Class(name="spreadsheet_Title")
ContentElement = Class(name="ContentElement")
spreadsheet_Point = Class(name="spreadsheet_Point")
spreadsheet_Row = Class(name="spreadsheet_Row")
spreadsheet_Cell = Class(name="spreadsheet_Cell")
spreadsheet_Header = Class(name="spreadsheet_Header")

# spreadsheet_Image class attributes and methods
spreadsheet_Image_width: Property = Property(name="width", type=IntegerType)
spreadsheet_Image_height: Property = Property(name="height", type=IntegerType)
spreadsheet_Image.attributes={spreadsheet_Image_height, spreadsheet_Image_width}

# spreadsheet_Table class attributes and methods
spreadsheet_Table_nbColumns: Property = Property(name="nbColumns", type=IntegerType)
spreadsheet_Table.attributes={spreadsheet_Table_nbColumns}

# spreadsheet_SpreadsheetFile class attributes and methods
spreadsheet_SpreadsheetFile_nbSheet: Property = Property(name="nbSheet", type=IntegerType)
spreadsheet_SpreadsheetFile.attributes={spreadsheet_SpreadsheetFile_nbSheet}

# DocumentModel class attributes and methods

# spreadsheet_Sheet class attributes and methods
spreadsheet_Sheet_name: Property = Property(name="name", type=StringType)
spreadsheet_Sheet.attributes={spreadsheet_Sheet_name}

# spreadsheet_Text class attributes and methods
spreadsheet_Text_textContent: Property = Property(name="textContent", type=StringType)
spreadsheet_Text.attributes={spreadsheet_Text_textContent}

# spreadsheet_Title class attributes and methods
spreadsheet_Title_hiearchy: Property = Property(name="hiearchy", type=StringType)
spreadsheet_Title.attributes={spreadsheet_Title_hiearchy}

# ContentElement class attributes and methods

# spreadsheet_Point class attributes and methods
spreadsheet_Point_x: Property = Property(name="x", type=IntegerType)
spreadsheet_Point_y: Property = Property(name="y", type=IntegerType)
spreadsheet_Point.attributes={spreadsheet_Point_x, spreadsheet_Point_y}

# spreadsheet_Row class attributes and methods

# spreadsheet_Cell class attributes and methods
spreadsheet_Cell_m_getColNumber: Method = Method(name="getColNumber", parameters={}, type=IntegerType)
spreadsheet_Cell_m_getRowNumber: Method = Method(name="getRowNumber", parameters={}, type=IntegerType)
spreadsheet_Cell_m_offset: Method = Method(name="offset", parameters={Parameter(name='spreadsheet_y', type=StringType), Parameter(name='spreadsheet_x', type=StringType)}, type=StringType)
spreadsheet_Cell.methods={spreadsheet_Cell_m_getColNumber, spreadsheet_Cell_m_offset, spreadsheet_Cell_m_getRowNumber}

# spreadsheet_Header class attributes and methods

# Relationships
image3: BinaryAssociation = BinaryAssociation(
    name="image3",
    ends={
        Property(name="spreadsheet_Image", type=spreadsheet_Sheet, multiplicity=Multiplicity(1, 1)),
        Property(name="spreadsheet_Sheet4", type=spreadsheet_Image, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
table5: BinaryAssociation = BinaryAssociation(
    name="table5",
    ends={
        Property(name="spreadsheet_Table", type=spreadsheet_Sheet, multiplicity=Multiplicity(1, 1)),
        Property(name="spreadsheet_Sheet6", type=spreadsheet_Table, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sheet0: BinaryAssociation = BinaryAssociation(
    name="sheet0",
    ends={
        Property(name="spreadsheet_Sheet", type=spreadsheet_SpreadsheetFile, multiplicity=Multiplicity(1, 1)),
        Property(name="spreadsheet_SpreadsheetFile", type=spreadsheet_Sheet, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
text1: BinaryAssociation = BinaryAssociation(
    name="text1",
    ends={
        Property(name="spreadsheet_Text", type=spreadsheet_Sheet, multiplicity=Multiplicity(1, 1)),
        Property(name="spreadsheet_Sheet2", type=spreadsheet_Text, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
title7: BinaryAssociation = BinaryAssociation(
    name="title7",
    ends={
        Property(name="spreadsheet_Title", type=spreadsheet_Text, multiplicity=Multiplicity(1, 1)),
        Property(name="spreadsheet_Text8", type=spreadsheet_Title, multiplicity=Multiplicity(1, 1))
    }
)
title9: BinaryAssociation = BinaryAssociation(
    name="title9",
    ends={
        Property(name="spreadsheet_Title11", type=spreadsheet_Image, multiplicity=Multiplicity(1, 1)),
        Property(name="spreadsheet_Image10", type=spreadsheet_Title, multiplicity=Multiplicity(1, 1))
    }
)
imagePos12: BinaryAssociation = BinaryAssociation(
    name="imagePos12",
    ends={
        Property(name="spreadsheet_Point", type=spreadsheet_Image, multiplicity=Multiplicity(1, 1)),
        Property(name="spreadsheet_Image13", type=spreadsheet_Point, multiplicity=Multiplicity(1, 1))
    }
)
title14: BinaryAssociation = BinaryAssociation(
    name="title14",
    ends={
        Property(name="spreadsheet_Title16", type=spreadsheet_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="spreadsheet_Table15", type=spreadsheet_Title, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
row19: BinaryAssociation = BinaryAssociation(
    name="row19",
    ends={
        Property(name="spreadsheet_Row", type=spreadsheet_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="spreadsheet_Table20", type=spreadsheet_Row, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
tablePos21: BinaryAssociation = BinaryAssociation(
    name="tablePos21",
    ends={
        Property(name="spreadsheet_Point23", type=spreadsheet_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="spreadsheet_Table22", type=spreadsheet_Point, multiplicity=Multiplicity(1, 1))
    }
)
cell24: BinaryAssociation = BinaryAssociation(
    name="cell24",
    ends={
        Property(name="spreadsheet_Cell", type=spreadsheet_Header, multiplicity=Multiplicity(1, 1)),
        Property(name="spreadsheet_Header25", type=spreadsheet_Cell, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
header17: BinaryAssociation = BinaryAssociation(
    name="header17",
    ends={
        Property(name="spreadsheet_Header", type=spreadsheet_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="spreadsheet_Table18", type=spreadsheet_Header, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
cell29: BinaryAssociation = BinaryAssociation(
    name="cell29",
    ends={
        Property(name="spreadsheet_Cell31", type=spreadsheet_Row, multiplicity=Multiplicity(1, 1)),
        Property(name="spreadsheet_Row30", type=spreadsheet_Cell, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
posCell26: BinaryAssociation = BinaryAssociation(
    name="posCell26",
    ends={
        Property(name="spreadsheet_Point28", type=spreadsheet_Cell, multiplicity=Multiplicity(1, 1)),
        Property(name="spreadsheet_Cell27", type=spreadsheet_Point, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_spreadsheet_SpreadsheetFile_DocumentModel = Generalization(general=DocumentModel, specific=spreadsheet_SpreadsheetFile)
gen_spreadsheet_Title_ContentElement = Generalization(general=ContentElement, specific=spreadsheet_Title)
gen_spreadsheet_Cell_ContentElement = Generalization(general=ContentElement, specific=spreadsheet_Cell)

# Domain Model
domain_model = DomainModel(
    name="spreadsheet",
    types={spreadsheet_Image, spreadsheet_Table, spreadsheet_SpreadsheetFile, DocumentModel, spreadsheet_Sheet, spreadsheet_Text, spreadsheet_Title, ContentElement, spreadsheet_Point, spreadsheet_Row, spreadsheet_Cell, spreadsheet_Header},
    associations={image3, table5, sheet0, text1, title7, title9, imagePos12, title14, row19, tablePos21, cell24, header17, cell29, posCell26},
    generalizations={gen_spreadsheet_SpreadsheetFile_DocumentModel, gen_spreadsheet_Title_ContentElement, gen_spreadsheet_Cell_ContentElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)