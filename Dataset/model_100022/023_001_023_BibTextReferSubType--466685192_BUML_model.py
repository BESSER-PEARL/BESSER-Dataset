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
BibText_LocatedElement = Class(name="BibText_LocatedElement", is_abstract=True)
BibText_BibTextFile = Class(name="BibText_BibTextFile")
BibText_BibTextEntry = Class(name="BibText_BibTextEntry", is_abstract=True)
LocatedElement = Class(name="LocatedElement")
BibText_Attribute = Class(name="BibText_Attribute", is_abstract=True)
BibText_Article = Class(name="BibText_Article")
BibTextEntry = Class(name="BibTextEntry")
BibText_Year = Class(name="BibText_Year")
Attribute = Class(name="Attribute")
BibText_Author = Class(name="BibText_Author")

# BibText_LocatedElement class attributes and methods
BibText_LocatedElement_location: Property = Property(name="location", type=StringType)
BibText_LocatedElement.attributes={BibText_LocatedElement_location}

# BibText_BibTextFile class attributes and methods

# BibText_BibTextEntry class attributes and methods
BibText_BibTextEntry_key: Property = Property(name="key", type=StringType)
BibText_BibTextEntry.attributes={BibText_BibTextEntry_key}

# LocatedElement class attributes and methods

# BibText_Attribute class attributes and methods
BibText_Attribute_value: Property = Property(name="value", type=StringType)
BibText_Attribute.attributes={BibText_Attribute_value}

# BibText_Article class attributes and methods

# BibTextEntry class attributes and methods

# BibText_Year class attributes and methods

# Attribute class attributes and methods

# BibText_Author class attributes and methods
BibText_Author_name: Property = Property(name="name", type=StringType)
BibText_Author.attributes={BibText_Author_name}

# Relationships
articles4: BinaryAssociation = BinaryAssociation(
    name="articles4",
    ends={
        Property(name="Article", type=BibText_Author, multiplicity=Multiplicity(1, 1)),
        Property(name="author", type=BibText_Article, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entries0: BinaryAssociation = BinaryAssociation(
    name="entries0",
    ends={
        Property(name="BibText_BibTextEntry", type=BibText_BibTextFile, multiplicity=Multiplicity(1, 1)),
        Property(name="BibText_BibTextFile", type=BibText_BibTextEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributes1: BinaryAssociation = BinaryAssociation(
    name="attributes1",
    ends={
        Property(name="BibText_Attribute", type=BibText_BibTextEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="BibText_BibTextEntry2", type=BibText_Attribute, multiplicity=Multiplicity(0, 5), is_composite=True)
    }
)
author3: BinaryAssociation = BinaryAssociation(
    name="author3",
    ends={
        Property(name="Author", type=BibText_Article, multiplicity=Multiplicity(1, 1)),
        Property(name="articles", type=BibText_BibTextEntry, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_BibText_BibTextEntry_LocatedElement = Generalization(general=LocatedElement, specific=BibText_BibTextEntry)
gen_BibText_Article_BibTextEntry = Generalization(general=BibTextEntry, specific=BibText_Article)
gen_BibText_Attribute_LocatedElement = Generalization(general=LocatedElement, specific=BibText_Attribute)
gen_BibText_Year_Attribute = Generalization(general=Attribute, specific=BibText_Year)
gen_BibText_Author_BibTextEntry = Generalization(general=BibTextEntry, specific=BibText_Author)

# Domain Model
domain_model = DomainModel(
    name="BibText",
    types={BibText_LocatedElement, BibText_BibTextFile, BibText_BibTextEntry, LocatedElement, BibText_Attribute, BibText_Article, BibTextEntry, BibText_Year, Attribute, BibText_Author},
    associations={articles4, entries0, attributes1, author3},
    generalizations={gen_BibText_BibTextEntry_LocatedElement, gen_BibText_Article_BibTextEntry, gen_BibText_Attribute_LocatedElement, gen_BibText_Year_Attribute, gen_BibText_Author_BibTextEntry},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)