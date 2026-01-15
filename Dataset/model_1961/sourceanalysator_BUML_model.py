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
sourceanalysator_GeneralSource = Class(name="sourceanalysator::GeneralSource")
sourceanalysator_Source = Class(name="sourceanalysator::Source")
sourceanalysator_Article = Class(name="sourceanalysator::Article")
sourceanalysator_Hyperlink = Class(name="sourceanalysator::Hyperlink")
sourceanalysator_Library = Class(name="sourceanalysator::Library")

# sourceanalysator_GeneralSource class attributes and methods
sourceanalysator_GeneralSource_name: Property = Property(name="name", type=StringType)
sourceanalysator_GeneralSource_aliases: Property = Property(name="aliases", type=StringType)
sourceanalysator_GeneralSource_dontCount: Property = Property(name="dontCount", type=BooleanType)
sourceanalysator_GeneralSource.attributes={sourceanalysator_GeneralSource_aliases, sourceanalysator_GeneralSource_dontCount, sourceanalysator_GeneralSource_name}

# sourceanalysator_Source class attributes and methods

# sourceanalysator_Article class attributes and methods
sourceanalysator_Article_title: Property = Property(name="title", type=StringType)
sourceanalysator_Article_localFile: Property = Property(name="localFile", type=StringType)
sourceanalysator_Article.attributes={sourceanalysator_Article_title, sourceanalysator_Article_localFile}

# sourceanalysator_Hyperlink class attributes and methods
sourceanalysator_Hyperlink_url: Property = Property(name="url", type=StringType)
sourceanalysator_Hyperlink.attributes={sourceanalysator_Hyperlink_url}

# sourceanalysator_Library class attributes and methods

# Relationships
sources0: BinaryAssociation = BinaryAssociation(
    name="sources0",
    ends={
        Property(name="Source", type=sourceanalysator_GeneralSource, multiplicity=Multiplicity(1, 1)),
        Property(name="generalSource", type=sourceanalysator_Source, multiplicity=Multiplicity(0, 9999))
    }
)
generalSource1: BinaryAssociation = BinaryAssociation(
    name="generalSource1",
    ends={
        Property(name="GeneralSource", type=sourceanalysator_Source, multiplicity=Multiplicity(1, 1)),
        Property(name="sources", type=sourceanalysator_GeneralSource, multiplicity=Multiplicity(1, 1))
    }
)
article2: BinaryAssociation = BinaryAssociation(
    name="article2",
    ends={
        Property(name="Article", type=sourceanalysator_Source, multiplicity=Multiplicity(1, 1)),
        Property(name="sources3", type=sourceanalysator_Article, multiplicity=Multiplicity(1, 1))
    }
)
hyperlink4: BinaryAssociation = BinaryAssociation(
    name="hyperlink4",
    ends={
        Property(name="Hyperlink", type=sourceanalysator_Source, multiplicity=Multiplicity(1, 1)),
        Property(name="sources5", type=sourceanalysator_Hyperlink, multiplicity=Multiplicity(1, 1))
    }
)
sources13: BinaryAssociation = BinaryAssociation(
    name="sources13",
    ends={
        Property(name="Source14", type=sourceanalysator_Hyperlink, multiplicity=Multiplicity(1, 1)),
        Property(name="hyperlink", type=sourceanalysator_Source, multiplicity=Multiplicity(0, 9999))
    }
)
generalSources6: BinaryAssociation = BinaryAssociation(
    name="generalSources6",
    ends={
        Property(name="sourceanalysator_GeneralSource", type=sourceanalysator_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="sourceanalysator_Library", type=sourceanalysator_GeneralSource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
articles7: BinaryAssociation = BinaryAssociation(
    name="articles7",
    ends={
        Property(name="sourceanalysator_Article", type=sourceanalysator_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="sourceanalysator_Library8", type=sourceanalysator_Article, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
hyperlinks9: BinaryAssociation = BinaryAssociation(
    name="hyperlinks9",
    ends={
        Property(name="sourceanalysator_Hyperlink", type=sourceanalysator_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="sourceanalysator_Library10", type=sourceanalysator_Hyperlink, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sources11: BinaryAssociation = BinaryAssociation(
    name="sources11",
    ends={
        Property(name="Source12", type=sourceanalysator_Article, multiplicity=Multiplicity(1, 1)),
        Property(name="article", type=sourceanalysator_Source, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="sourceanalysator",
    types={sourceanalysator_GeneralSource, sourceanalysator_Source, sourceanalysator_Article, sourceanalysator_Hyperlink, sourceanalysator_Library},
    associations={sources0, generalSource1, article2, hyperlink4, sources13, generalSources6, articles7, hyperlinks9, sources11},
    generalizations={},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)