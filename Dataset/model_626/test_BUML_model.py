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
model_Writer = Class(name="model::Writer")
model_Library = Class(name="model::Library")
model_Book = Class(name="model::Book")
model_Librarian = Class(name="model::Librarian")
model_Computer = Class(name="model::Computer")
model_Mainboard = Class(name="model::Mainboard")
model_PowerBlock = Class(name="model::PowerBlock")
model_Container = Class(name="model::Container")
model_Content = Class(name="model::Content")
model_TableWithMultiplicity = Class(name="model::TableWithMultiplicity")
model_TableContent = Class(name="model::TableContent", is_abstract=True)
TableContent = Class(name="TableContent")
model_TableContentWithValidation = Class(name="model::TableContentWithValidation")
model_TableWithoutMultiplicity = Class(name="model::TableWithoutMultiplicity")
model_TableWithUnique = Class(name="model::TableWithUnique")
model_TableContentWithoutValidation = Class(name="model::TableContentWithoutValidation")

# model_Writer class attributes and methods
model_Writer_Pseudonym: Property = Property(name="Pseudonym", type=BooleanType)
model_Writer_firstName: Property = Property(name="firstName", type=StringType)
model_Writer_lastName: Property = Property(name="lastName", type=StringType)
model_Writer_EMail: Property = Property(name="EMail", type=StringType)
model_Writer_BirthDate: Property = Property(name="BirthDate", type=DateType)
model_Writer_m_validate: Method = Method(name="validate", parameters={Parameter(name='context'), Parameter(name='diagnostic')}, type=BooleanType)
model_Writer.attributes={model_Writer_EMail, model_Writer_Pseudonym, model_Writer_firstName, model_Writer_lastName, model_Writer_BirthDate}
model_Writer.methods={model_Writer_m_validate}

# model_Library class attributes and methods
model_Library_name: Property = Property(name="name", type=StringType)
model_Library_m_validate: Method = Method(name="validate", parameters={Parameter(name='context'), Parameter(name='diagnostic')}, type=BooleanType)
model_Library.attributes={model_Library_name}
model_Library.methods={model_Library_m_validate}

# model_Book class attributes and methods
model_Book_title: Property = Property(name="title", type=StringType)
model_Book_pages: Property = Property(name="pages", type=IntegerType)
model_Book_m_validate: Method = Method(name="validate", parameters={Parameter(name='context'), Parameter(name='diagnostic')}, type=BooleanType)
model_Book.attributes={model_Book_pages, model_Book_title}
model_Book.methods={model_Book_m_validate}

# model_Librarian class attributes and methods
model_Librarian_name: Property = Property(name="name", type=StringType)
model_Librarian_m_validate: Method = Method(name="validate", parameters={Parameter(name='context'), Parameter(name='diagnostic')}, type=BooleanType)
model_Librarian.attributes={model_Librarian_name}
model_Librarian.methods={model_Librarian_m_validate}

# model_Computer class attributes and methods
model_Computer_name: Property = Property(name="name", type=StringType)
model_Computer.attributes={model_Computer_name}

# model_Mainboard class attributes and methods
model_Mainboard_name: Property = Property(name="name", type=StringType)
model_Mainboard.attributes={model_Mainboard_name}

# model_PowerBlock class attributes and methods
model_PowerBlock_name: Property = Property(name="name", type=StringType)
model_PowerBlock.attributes={model_PowerBlock_name}

# model_Container class attributes and methods

# model_Content class attributes and methods
model_Content_uniqueAttribute: Property = Property(name="uniqueAttribute", type=StringType)
model_Content_secondAttribute: Property = Property(name="secondAttribute", type=StringType)
model_Content.attributes={model_Content_uniqueAttribute, model_Content_secondAttribute}

# model_TableWithMultiplicity class attributes and methods

# model_TableContent class attributes and methods

# TableContent class attributes and methods

# model_TableContentWithValidation class attributes and methods
model_TableContentWithValidation_name: Property = Property(name="name", type=StringType)
model_TableContentWithValidation_weight: Property = Property(name="weight", type=IntegerType)
model_TableContentWithValidation.attributes={model_TableContentWithValidation_name, model_TableContentWithValidation_weight}

# model_TableWithoutMultiplicity class attributes and methods

# model_TableWithUnique class attributes and methods

# model_TableContentWithoutValidation class attributes and methods
model_TableContentWithoutValidation_name: Property = Property(name="name", type=StringType)
model_TableContentWithoutValidation_weight: Property = Property(name="weight", type=IntegerType)
model_TableContentWithoutValidation.attributes={model_TableContentWithoutValidation_name, model_TableContentWithoutValidation_weight}

# Relationships
writers0: BinaryAssociation = BinaryAssociation(
    name="writers0",
    ends={
        Property(name="Writer", type=model_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library", type=model_Writer, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
library5: BinaryAssociation = BinaryAssociation(
    name="library5",
    ends={
        Property(name="Library", type=model_Writer, multiplicity=Multiplicity(1, 1)),
        Property(name="writers6", type=model_Library, multiplicity=Multiplicity(0, 1))
    }
)
books1: BinaryAssociation = BinaryAssociation(
    name="books1",
    ends={
        Property(name="model_Book", type=model_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Library", type=model_Book, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
librarian2: BinaryAssociation = BinaryAssociation(
    name="librarian2",
    ends={
        Property(name="model_Librarian", type=model_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Library3", type=model_Librarian, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
writers7: BinaryAssociation = BinaryAssociation(
    name="writers7",
    ends={
        Property(name="Writer8", type=model_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="books", type=model_Writer, multiplicity=Multiplicity(0, 1))
    }
)
books4: BinaryAssociation = BinaryAssociation(
    name="books4",
    ends={
        Property(name="Book", type=model_Writer, multiplicity=Multiplicity(1, 1)),
        Property(name="writers", type=model_Book, multiplicity=Multiplicity(0, 9999))
    }
)
mainboard9: BinaryAssociation = BinaryAssociation(
    name="mainboard9",
    ends={
        Property(name="model_Mainboard", type=model_Computer, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Computer", type=model_Mainboard, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
powerBlock10: BinaryAssociation = BinaryAssociation(
    name="powerBlock10",
    ends={
        Property(name="model_PowerBlock", type=model_Computer, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Computer11", type=model_PowerBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
contents12: BinaryAssociation = BinaryAssociation(
    name="contents12",
    ends={
        Property(name="model_Content", type=model_Container, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Container", type=model_Content, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
content13: BinaryAssociation = BinaryAssociation(
    name="content13",
    ends={
        Property(name="model_TableContent", type=model_TableWithMultiplicity, multiplicity=Multiplicity(1, 1)),
        Property(name="model_TableWithMultiplicity", type=model_TableContent, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
content14: BinaryAssociation = BinaryAssociation(
    name="content14",
    ends={
        Property(name="model_TableContent15", type=model_TableWithoutMultiplicity, multiplicity=Multiplicity(1, 1)),
        Property(name="model_TableWithoutMultiplicity", type=model_TableContent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
content16: BinaryAssociation = BinaryAssociation(
    name="content16",
    ends={
        Property(name="model_TableContent17", type=model_TableWithUnique, multiplicity=Multiplicity(1, 1)),
        Property(name="model_TableWithUnique", type=model_TableContent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_model_TableContentWithoutValidation_TableContent = Generalization(general=TableContent, specific=model_TableContentWithoutValidation)
gen_model_TableContentWithValidation_TableContent = Generalization(general=TableContent, specific=model_TableContentWithValidation)

# Domain Model
domain_model = DomainModel(
    name="model",
    types={model_Writer, model_Library, model_Book, model_Librarian, model_Computer, model_Mainboard, model_PowerBlock, model_Container, model_Content, model_TableWithMultiplicity, model_TableContent, TableContent, model_TableContentWithValidation, model_TableWithoutMultiplicity, model_TableWithUnique, model_TableContentWithoutValidation},
    associations={writers0, library5, books1, librarian2, writers7, books4, mainboard9, powerBlock10, contents12, content13, content14, content16},
    generalizations={gen_model_TableContentWithoutValidation_TableContent, gen_model_TableContentWithValidation_TableContent},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)