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
MediaType: Enumeration = Enumeration(
    name="MediaType",
    literals={
            EnumerationLiteral(name="CD"),
			EnumerationLiteral(name="MP3"),
			EnumerationLiteral(name="TAPE")
    }
)

# Classes
music_Artist = Class(name="music::Artist")
music_Work = Class(name="music::Work")
music_MusicLibrary = Class(name="music::MusicLibrary")

# music_Artist class attributes and methods
music_Artist_name: Property = Property(name="name", type=StringType)
music_Artist_notes: Property = Property(name="notes", type=StringType)
music_Artist_m_printState: Method = Method(name="printState", parameters={})
music_Artist.attributes={music_Artist_notes, music_Artist_name}
music_Artist.methods={music_Artist_m_printState}

# music_Work class attributes and methods
music_Work_name: Property = Property(name="name", type=StringType)
music_Work_whenMade: Property = Property(name="whenMade", type=StringType)
music_Work_notes: Property = Property(name="notes", type=StringType)
music_Work_mediaTypes: Property = Property(name="mediaTypes", type=StringType)
music_Work.attributes={music_Work_whenMade, music_Work_name, music_Work_mediaTypes, music_Work_notes}

# music_MusicLibrary class attributes and methods
music_MusicLibrary_name: Property = Property(name="name", type=StringType)
music_MusicLibrary.attributes={music_MusicLibrary_name}

# Relationships
artists1: BinaryAssociation = BinaryAssociation(
    name="artists1",
    ends={
        Property(name="music_MusicLibrary", type=music_Artist, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="music_Artist", type=music_MusicLibrary, multiplicity=Multiplicity(1, 1))
    }
)
works0: BinaryAssociation = BinaryAssociation(
    name="works0",
    ends={
        Property(name="Work", type=music_Artist, multiplicity=Multiplicity(1, 1)),
        Property(name="performer", type=music_Work, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
performer2: BinaryAssociation = BinaryAssociation(
    name="performer2",
    ends={
        Property(name="Artist", type=music_Work, multiplicity=Multiplicity(1, 1)),
        Property(name="works", type=music_Artist, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="music",
    types={music_Artist, music_Work, music_MusicLibrary, MediaType},
    associations={artists1, works0, performer2},
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