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
simpleanySimplified_Book = Class(name="simpleanySimplified::Book")
simpleanySimplified_Description = Class(name="simpleanySimplified::Description")
simpleanySimplified_MixedText = Class(name="simpleanySimplified::MixedText")
MixedData = Class(name="MixedData")
simpleanySimplified_MixedFeature = Class(name="simpleanySimplified::MixedFeature")
simpleanySimplified_MixedBaseClass = Class(name="simpleanySimplified::MixedBaseClass", is_abstract=True)
MixedBaseClass = Class(name="MixedBaseClass")
simpleanySimplified_Library = Class(name="simpleanySimplified::Library")
simpleanySimplified_MixedData = Class(name="simpleanySimplified::MixedData", is_abstract=True)

# simpleanySimplified_Book class attributes and methods
simpleanySimplified_Book_name: Property = Property(name="name", type=StringType)
simpleanySimplified_Book_title: Property = Property(name="title", type=StringType)
simpleanySimplified_Book_author: Property = Property(name="author", type=StringType)
simpleanySimplified_Book.attributes={simpleanySimplified_Book_author, simpleanySimplified_Book_title, simpleanySimplified_Book_name}

# simpleanySimplified_Description class attributes and methods
simpleanySimplified_Description_keywords: Property = Property(name="keywords", type=StringType)
simpleanySimplified_Description.attributes={simpleanySimplified_Description_keywords}

# simpleanySimplified_MixedText class attributes and methods

# MixedData class attributes and methods

# simpleanySimplified_MixedFeature class attributes and methods

# simpleanySimplified_MixedBaseClass class attributes and methods

# MixedBaseClass class attributes and methods

# simpleanySimplified_Library class attributes and methods

# simpleanySimplified_MixedData class attributes and methods
simpleanySimplified_MixedData_value: Property = Property(name="value", type=StringType)
simpleanySimplified_MixedData.attributes={simpleanySimplified_MixedData_value}

# Relationships
mixed6: BinaryAssociation = BinaryAssociation(
    name="mixed6",
    ends={
        Property(name="simpleanySimplified_MixedData", type=simpleanySimplified_MixedBaseClass, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleanySimplified_MixedBaseClass", type=simpleanySimplified_MixedData, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
description0: BinaryAssociation = BinaryAssociation(
    name="description0",
    ends={
        Property(name="simpleanySimplified_Description", type=simpleanySimplified_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleanySimplified_Book", type=simpleanySimplified_Description, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
descriptions2: BinaryAssociation = BinaryAssociation(
    name="descriptions2",
    ends={
        Property(name="simpleanySimplified_Description3", type=simpleanySimplified_Description, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleanySimplified_Description1", type=simpleanySimplified_Description, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
books4: BinaryAssociation = BinaryAssociation(
    name="books4",
    ends={
        Property(name="simpleanySimplified_Book5", type=simpleanySimplified_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleanySimplified_Library", type=simpleanySimplified_Book, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_simpleanySimplified_MixedText_MixedData = Generalization(general=MixedData, specific=simpleanySimplified_MixedText)
gen_simpleanySimplified_MixedFeature_MixedData = Generalization(general=MixedData, specific=simpleanySimplified_MixedFeature)
gen_simpleanySimplified_Description_MixedBaseClass = Generalization(general=MixedBaseClass, specific=simpleanySimplified_Description)

# Domain Model
domain_model = DomainModel(
    name="simpleanySimplified",
    types={simpleanySimplified_Book, simpleanySimplified_Description, simpleanySimplified_MixedText, MixedData, simpleanySimplified_MixedFeature, simpleanySimplified_MixedBaseClass, MixedBaseClass, simpleanySimplified_Library, simpleanySimplified_MixedData},
    associations={mixed6, description0, descriptions2, books4},
    generalizations={gen_simpleanySimplified_MixedText_MixedData, gen_simpleanySimplified_MixedFeature_MixedData, gen_simpleanySimplified_Description_MixedBaseClass},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)