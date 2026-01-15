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
MediaSourceType: Enumeration = Enumeration(
    name="MediaSourceType",
    literals={
            EnumerationLiteral(name="ExternalArtifact"),
			EnumerationLiteral(name="MediaStore")
    }
)

DeviceType: Enumeration = Enumeration(
    name="DeviceType",
    literals={
            EnumerationLiteral(name="Computer"),
			EnumerationLiteral(name="Smartphone"),
			EnumerationLiteral(name="Tablet")
    }
)

# Classes
mode_MediaLibrary = Class(name="mode::MediaLibrary")
mode_MediaArtifact = Class(name="mode::MediaArtifact", is_abstract=True)
mode_Device = Class(name="mode::Device")
mode_User = Class(name="mode::User")
mode_MediaCollection = Class(name="mode::MediaCollection")
mode_Video = Class(name="mode::Video")
MediaArtifact = Class(name="MediaArtifact")
mode_Music = Class(name="mode::Music")
mode_AudioBook = Class(name="mode::AudioBook")
mode_EBook = Class(name="mode::EBook")

# mode_MediaLibrary class attributes and methods

# mode_MediaArtifact class attributes and methods
mode_MediaArtifact_identifier: Property = Property(name="identifier", type=StringType)
mode_MediaArtifact_name: Property = Property(name="name", type=StringType)
mode_MediaArtifact_source: Property = Property(name="source", type=StringType)
mode_MediaArtifact.attributes={mode_MediaArtifact_identifier, mode_MediaArtifact_source, mode_MediaArtifact_name}

# mode_Device class attributes and methods
mode_Device_name: Property = Property(name="name", type=StringType)
mode_Device_type: Property = Property(name="type", type=StringType)
mode_Device.attributes={mode_Device_name, mode_Device_type}

# mode_User class attributes and methods
mode_User_name: Property = Property(name="name", type=StringType)
mode_User.attributes={mode_User_name}

# mode_MediaCollection class attributes and methods
mode_MediaCollection_name: Property = Property(name="name", type=StringType)
mode_MediaCollection.attributes={mode_MediaCollection_name}

# mode_Video class attributes and methods
mode_Video_length: Property = Property(name="length", type=IntegerType)
mode_Video.attributes={mode_Video_length}

# MediaArtifact class attributes and methods

# mode_Music class attributes and methods
mode_Music_length: Property = Property(name="length", type=IntegerType)
mode_Music.attributes={mode_Music_length}

# mode_AudioBook class attributes and methods
mode_AudioBook_length: Property = Property(name="length", type=IntegerType)
mode_AudioBook.attributes={mode_AudioBook_length}

# mode_EBook class attributes and methods

# Relationships
mediaArtifacts6: BinaryAssociation = BinaryAssociation(
    name="mediaArtifacts6",
    ends={
        Property(name="MediaArtifact", type=mode_MediaCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="collection", type=mode_MediaArtifact, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
synchronisedDevices7: BinaryAssociation = BinaryAssociation(
    name="synchronisedDevices7",
    ends={
        Property(name="Device", type=mode_MediaCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="synchronisedCollections", type=mode_Device, multiplicity=Multiplicity(0, 9999))
    }
)
ownedUser8: BinaryAssociation = BinaryAssociation(
    name="ownedUser8",
    ends={
        Property(name="User", type=mode_MediaCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedCollections", type=mode_User, multiplicity=Multiplicity(0, 1))
    }
)
collection9: BinaryAssociation = BinaryAssociation(
    name="collection9",
    ends={
        Property(name="MediaCollection10", type=mode_MediaArtifact, multiplicity=Multiplicity(1, 1)),
        Property(name="mediaArtifacts", type=mode_MediaCollection, multiplicity=Multiplicity(1, 1))
    }
)
devices0: BinaryAssociation = BinaryAssociation(
    name="devices0",
    ends={
        Property(name="mode_Device", type=mode_MediaLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="mode_MediaLibrary", type=mode_Device, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
users1: BinaryAssociation = BinaryAssociation(
    name="users1",
    ends={
        Property(name="mode_User", type=mode_MediaLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="mode_MediaLibrary2", type=mode_User, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
collections3: BinaryAssociation = BinaryAssociation(
    name="collections3",
    ends={
        Property(name="mode_MediaCollection", type=mode_MediaLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="mode_MediaLibrary4", type=mode_MediaCollection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedCollections5: BinaryAssociation = BinaryAssociation(
    name="ownedCollections5",
    ends={
        Property(name="MediaCollection", type=mode_User, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedUser", type=mode_MediaCollection, multiplicity=Multiplicity(0, 9999))
    }
)
synchronisedCollections11: BinaryAssociation = BinaryAssociation(
    name="synchronisedCollections11",
    ends={
        Property(name="MediaCollection12", type=mode_Device, multiplicity=Multiplicity(1, 1)),
        Property(name="synchronisedDevices", type=mode_MediaCollection, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_mode_Video_MediaArtifact = Generalization(general=MediaArtifact, specific=mode_Video)
gen_mode_Music_MediaArtifact = Generalization(general=MediaArtifact, specific=mode_Music)
gen_mode_AudioBook_MediaArtifact = Generalization(general=MediaArtifact, specific=mode_AudioBook)
gen_mode_EBook_MediaArtifact = Generalization(general=MediaArtifact, specific=mode_EBook)

# Domain Model
domain_model = DomainModel(
    name="mode",
    types={mode_MediaLibrary, mode_MediaArtifact, mode_Device, mode_User, mode_MediaCollection, mode_Video, MediaArtifact, mode_Music, mode_AudioBook, mode_EBook, MediaSourceType, DeviceType},
    associations={mediaArtifacts6, synchronisedDevices7, ownedUser8, collection9, devices0, users1, collections3, ownedCollections5, synchronisedCollections11},
    generalizations={gen_mode_Video_MediaArtifact, gen_mode_Music_MediaArtifact, gen_mode_AudioBook_MediaArtifact, gen_mode_EBook_MediaArtifact},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)