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
SourceType: Enumeration = Enumeration(
    name="SourceType",
    literals={
            EnumerationLiteral(name="CD"),
			EnumerationLiteral(name="CASSETTE"),
			EnumerationLiteral(name="HDD"),
			EnumerationLiteral(name="OTHER")
    }
)

# Classes
MediaLibrary_Ecosystem = Class(name="MediaLibrary::Ecosystem")
MediaLibrary_Library = Class(name="MediaLibrary::Library")
MediaLibrary_Device = Class(name="MediaLibrary::Device", is_abstract=True)
MediaLibrary_MediaSource = Class(name="MediaLibrary::MediaSource", is_abstract=True)
MediaLibrary_Artifact = Class(name="MediaLibrary::Artifact", is_abstract=True)
MediaLibrary_MediaCollection = Class(name="MediaLibrary::MediaCollection")
MediaLibrary_Tablet = Class(name="MediaLibrary::Tablet")
Device = Class(name="Device")
MediaLibrary_Computer = Class(name="MediaLibrary::Computer")
MediaLibrary_Smartphone = Class(name="MediaLibrary::Smartphone")
MediaLibrary_EReader = Class(name="MediaLibrary::EReader")
MediaLibrary_DurationArtifact = Class(name="MediaLibrary::DurationArtifact", is_abstract=True)
Artifact = Class(name="Artifact")
MediaLibrary_AudioBook = Class(name="MediaLibrary::AudioBook")
DurationArtifact = Class(name="DurationArtifact")
MediaLibrary_MusicTrack = Class(name="MediaLibrary::MusicTrack")
MediaLibrary_Video = Class(name="MediaLibrary::Video")
MediaLibrary_Ebook = Class(name="MediaLibrary::Ebook")
MediaLibrary_Image = Class(name="MediaLibrary::Image")
MediaLibrary_ExternalSource = Class(name="MediaLibrary::ExternalSource")
MediaSource = Class(name="MediaSource")
MediaLibrary_Store = Class(name="MediaLibrary::Store")

# MediaLibrary_Ecosystem class attributes and methods

# MediaLibrary_Library class attributes and methods
MediaLibrary_Library_name: Property = Property(name="name", type=StringType)
MediaLibrary_Library.attributes={MediaLibrary_Library_name}

# MediaLibrary_Device class attributes and methods
MediaLibrary_Device_MACAddress: Property = Property(name="MACAddress", type=StringType)
MediaLibrary_Device_resolutionWidth: Property = Property(name="resolutionWidth", type=IntegerType)
MediaLibrary_Device_resolutionHeight: Property = Property(name="resolutionHeight", type=IntegerType)
MediaLibrary_Device.attributes={MediaLibrary_Device_MACAddress, MediaLibrary_Device_resolutionWidth, MediaLibrary_Device_resolutionHeight}

# MediaLibrary_MediaSource class attributes and methods

# MediaLibrary_Artifact class attributes and methods
MediaLibrary_Artifact_author: Property = Property(name="author", type=StringType)
MediaLibrary_Artifact_name: Property = Property(name="name", type=StringType)
MediaLibrary_Artifact.attributes={MediaLibrary_Artifact_name, MediaLibrary_Artifact_author}

# MediaLibrary_MediaCollection class attributes and methods
MediaLibrary_MediaCollection_name: Property = Property(name="name", type=StringType)
MediaLibrary_MediaCollection.attributes={MediaLibrary_MediaCollection_name}

# MediaLibrary_Tablet class attributes and methods

# Device class attributes and methods

# MediaLibrary_Computer class attributes and methods

# MediaLibrary_Smartphone class attributes and methods

# MediaLibrary_EReader class attributes and methods
MediaLibrary_EReader_videoEnabled: Property = Property(name="videoEnabled", type=StringType)
MediaLibrary_EReader_audioEnabled: Property = Property(name="audioEnabled", type=StringType)
MediaLibrary_EReader.attributes={MediaLibrary_EReader_videoEnabled, MediaLibrary_EReader_audioEnabled}

# MediaLibrary_DurationArtifact class attributes and methods
MediaLibrary_DurationArtifact_duration: Property = Property(name="duration", type=IntegerType)
MediaLibrary_DurationArtifact.attributes={MediaLibrary_DurationArtifact_duration}

# Artifact class attributes and methods

# MediaLibrary_AudioBook class attributes and methods
MediaLibrary_AudioBook_currentPosition: Property = Property(name="currentPosition", type=IntegerType)
MediaLibrary_AudioBook.attributes={MediaLibrary_AudioBook_currentPosition}

# DurationArtifact class attributes and methods

# MediaLibrary_MusicTrack class attributes and methods
MediaLibrary_MusicTrack_label: Property = Property(name="label", type=StringType)
MediaLibrary_MusicTrack.attributes={MediaLibrary_MusicTrack_label}

# MediaLibrary_Video class attributes and methods
MediaLibrary_Video_fps: Property = Property(name="fps", type=StringType)
MediaLibrary_Video.attributes={MediaLibrary_Video_fps}

# MediaLibrary_Ebook class attributes and methods
MediaLibrary_Ebook_pages: Property = Property(name="pages", type=IntegerType)
MediaLibrary_Ebook.attributes={MediaLibrary_Ebook_pages}

# MediaLibrary_Image class attributes and methods
MediaLibrary_Image_dateTaken: Property = Property(name="dateTaken", type=StringType)
MediaLibrary_Image.attributes={MediaLibrary_Image_dateTaken}

# MediaLibrary_ExternalSource class attributes and methods
MediaLibrary_ExternalSource_sourceType: Property = Property(name="sourceType", type=StringType)
MediaLibrary_ExternalSource.attributes={MediaLibrary_ExternalSource_sourceType}

# MediaSource class attributes and methods

# MediaLibrary_Store class attributes and methods
MediaLibrary_Store_name: Property = Property(name="name", type=StringType)
MediaLibrary_Store_url: Property = Property(name="url", type=StringType)
MediaLibrary_Store.attributes={MediaLibrary_Store_url, MediaLibrary_Store_name}

# Relationships
libraries0: BinaryAssociation = BinaryAssociation(
    name="libraries0",
    ends={
        Property(name="MediaLibrary_Library", type=MediaLibrary_Ecosystem, multiplicity=Multiplicity(1, 1)),
        Property(name="MediaLibrary_Ecosystem", type=MediaLibrary_Library, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
devices1: BinaryAssociation = BinaryAssociation(
    name="devices1",
    ends={
        Property(name="MediaLibrary_Device", type=MediaLibrary_Ecosystem, multiplicity=Multiplicity(1, 1)),
        Property(name="MediaLibrary_Ecosystem2", type=MediaLibrary_Device, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
mediaSources3: BinaryAssociation = BinaryAssociation(
    name="mediaSources3",
    ends={
        Property(name="MediaLibrary_MediaSource", type=MediaLibrary_Ecosystem, multiplicity=Multiplicity(1, 1)),
        Property(name="MediaLibrary_Ecosystem4", type=MediaLibrary_MediaSource, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
mediaArtifacts5: BinaryAssociation = BinaryAssociation(
    name="mediaArtifacts5",
    ends={
        Property(name="MediaLibrary_Artifact", type=MediaLibrary_Ecosystem, multiplicity=Multiplicity(1, 1)),
        Property(name="MediaLibrary_Ecosystem6", type=MediaLibrary_Artifact, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
syncedDevices13: BinaryAssociation = BinaryAssociation(
    name="syncedDevices13",
    ends={
        Property(name="collections", type=MediaLibrary_Device, multiplicity=Multiplicity(1, 9999)),
        Property(name="Device14", type=MediaLibrary_MediaCollection, multiplicity=Multiplicity(1, 1))
    }
)
collections7: BinaryAssociation = BinaryAssociation(
    name="collections7",
    ends={
        Property(name="MediaLibrary_MediaCollection", type=MediaLibrary_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="MediaLibrary_Library8", type=MediaLibrary_MediaCollection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
members9: BinaryAssociation = BinaryAssociation(
    name="members9",
    ends={
        Property(name="MediaLibrary_Artifact11", type=MediaLibrary_MediaCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="MediaLibrary_MediaCollection10", type=MediaLibrary_Artifact, multiplicity=Multiplicity(1, 9999))
    }
)
host12: BinaryAssociation = BinaryAssociation(
    name="host12",
    ends={
        Property(name="Device", type=MediaLibrary_MediaCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="hostOf", type=MediaLibrary_Device, multiplicity=Multiplicity(1, 1))
    }
)
hostOf15: BinaryAssociation = BinaryAssociation(
    name="hostOf15",
    ends={
        Property(name="MediaCollection", type=MediaLibrary_Device, multiplicity=Multiplicity(1, 1)),
        Property(name="host", type=MediaLibrary_MediaCollection, multiplicity=Multiplicity(0, 9999))
    }
)
collections16: BinaryAssociation = BinaryAssociation(
    name="collections16",
    ends={
        Property(name="MediaCollection17", type=MediaLibrary_Device, multiplicity=Multiplicity(1, 1)),
        Property(name="syncedDevices", type=MediaLibrary_MediaCollection, multiplicity=Multiplicity(0, 9999))
    }
)
origin18: BinaryAssociation = BinaryAssociation(
    name="origin18",
    ends={
        Property(name="MediaSource", type=MediaLibrary_Artifact, multiplicity=Multiplicity(1, 1)),
        Property(name="contents", type=MediaLibrary_MediaSource, multiplicity=Multiplicity(1, 1))
    }
)
contents19: BinaryAssociation = BinaryAssociation(
    name="contents19",
    ends={
        Property(name="Artifact", type=MediaLibrary_MediaSource, multiplicity=Multiplicity(1, 1)),
        Property(name="origin", type=MediaLibrary_Artifact, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_MediaLibrary_Tablet_Device = Generalization(general=Device, specific=MediaLibrary_Tablet)
gen_MediaLibrary_Computer_Device = Generalization(general=Device, specific=MediaLibrary_Computer)
gen_MediaLibrary_Smartphone_Device = Generalization(general=Device, specific=MediaLibrary_Smartphone)
gen_MediaLibrary_EReader_Device = Generalization(general=Device, specific=MediaLibrary_EReader)
gen_MediaLibrary_DurationArtifact_Artifact = Generalization(general=Artifact, specific=MediaLibrary_DurationArtifact)
gen_MediaLibrary_AudioBook_DurationArtifact = Generalization(general=DurationArtifact, specific=MediaLibrary_AudioBook)
gen_MediaLibrary_MusicTrack_DurationArtifact = Generalization(general=DurationArtifact, specific=MediaLibrary_MusicTrack)
gen_MediaLibrary_Video_DurationArtifact = Generalization(general=DurationArtifact, specific=MediaLibrary_Video)
gen_MediaLibrary_Ebook_Artifact = Generalization(general=Artifact, specific=MediaLibrary_Ebook)
gen_MediaLibrary_Image_Artifact = Generalization(general=Artifact, specific=MediaLibrary_Image)
gen_MediaLibrary_ExternalSource_MediaSource = Generalization(general=MediaSource, specific=MediaLibrary_ExternalSource)
gen_MediaLibrary_Store_MediaSource = Generalization(general=MediaSource, specific=MediaLibrary_Store)

# Domain Model
domain_model = DomainModel(
    name="MediaLibrary",
    types={MediaLibrary_Ecosystem, MediaLibrary_Library, MediaLibrary_Device, MediaLibrary_MediaSource, MediaLibrary_Artifact, MediaLibrary_MediaCollection, MediaLibrary_Tablet, Device, MediaLibrary_Computer, MediaLibrary_Smartphone, MediaLibrary_EReader, MediaLibrary_DurationArtifact, Artifact, MediaLibrary_AudioBook, DurationArtifact, MediaLibrary_MusicTrack, MediaLibrary_Video, MediaLibrary_Ebook, MediaLibrary_Image, MediaLibrary_ExternalSource, MediaSource, MediaLibrary_Store, SourceType},
    associations={libraries0, devices1, mediaSources3, mediaArtifacts5, syncedDevices13, collections7, members9, host12, hostOf15, collections16, origin18, contents19},
    generalizations={gen_MediaLibrary_Tablet_Device, gen_MediaLibrary_Computer_Device, gen_MediaLibrary_Smartphone_Device, gen_MediaLibrary_EReader_Device, gen_MediaLibrary_DurationArtifact_Artifact, gen_MediaLibrary_AudioBook_DurationArtifact, gen_MediaLibrary_MusicTrack_DurationArtifact, gen_MediaLibrary_Video_DurationArtifact, gen_MediaLibrary_Ebook_Artifact, gen_MediaLibrary_Image_Artifact, gen_MediaLibrary_ExternalSource_MediaSource, gen_MediaLibrary_Store_MediaSource},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)