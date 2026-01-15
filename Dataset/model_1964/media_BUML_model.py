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
State: Enumeration = Enumeration(
    name="State",
    literals={
            EnumerationLiteral(name="PLAYING"),
			EnumerationLiteral(name="PAUSED"),
			EnumerationLiteral(name="STOPPED")
    }
)

# Classes
MediaPlayer_Playlist = Class(name="MediaPlayer::Playlist")
BaseObject = Class(name="BaseObject")
MediaPlayer_MediaObject = Class(name="MediaPlayer::MediaObject")
MediaPlayer_MediaApi = Class(name="MediaPlayer::MediaApi", is_abstract=True)
MediaPlayer_PlayLayer = Class(name="MediaPlayer::PlayLayer")
MediaPlayer_Library = Class(name="MediaPlayer::Library")
MediaPlayer_BaseObject = Class(name="MediaPlayer::BaseObject")

# MediaPlayer_Playlist class attributes and methods
MediaPlayer_Playlist_name: Property = Property(name="name", type=StringType)
MediaPlayer_Playlist_repeat: Property = Property(name="repeat", type=BooleanType)
MediaPlayer_Playlist_m_shuffle: Method = Method(name="shuffle", parameters={})
MediaPlayer_Playlist.attributes={MediaPlayer_Playlist_name, MediaPlayer_Playlist_repeat}
MediaPlayer_Playlist.methods={MediaPlayer_Playlist_m_shuffle}

# BaseObject class attributes and methods

# MediaPlayer_MediaObject class attributes and methods
MediaPlayer_MediaObject_location: Property = Property(name="location", type=StringType)
MediaPlayer_MediaObject_title: Property = Property(name="title", type=StringType)
MediaPlayer_MediaObject_artist: Property = Property(name="artist", type=StringType)
MediaPlayer_MediaObject_year: Property = Property(name="year", type=IntegerType)
MediaPlayer_MediaObject_state: Property = Property(name="state", type=StringType)
MediaPlayer_MediaObject_album: Property = Property(name="album", type=StringType)
MediaPlayer_MediaObject.attributes={MediaPlayer_MediaObject_state, MediaPlayer_MediaObject_location, MediaPlayer_MediaObject_year, MediaPlayer_MediaObject_artist, MediaPlayer_MediaObject_title, MediaPlayer_MediaObject_album}

# MediaPlayer_MediaApi class attributes and methods
MediaPlayer_MediaApi_m_init: Method = Method(name="init", parameters={})
MediaPlayer_MediaApi_m_play: Method = Method(name="play", parameters={Parameter(name='playMe')})
MediaPlayer_MediaApi_m_pause: Method = Method(name="pause", parameters={Parameter(name='pauseMe')})
MediaPlayer_MediaApi_m_stop: Method = Method(name="stop", parameters={Parameter(name='stopMe')})
MediaPlayer_MediaApi_m_dispose: Method = Method(name="dispose", parameters={})
MediaPlayer_MediaApi_m_canPlay: Method = Method(name="canPlay", parameters={Parameter(name='media')}, type=BooleanType)
MediaPlayer_MediaApi_m_updateMediaObjectInfo: Method = Method(name="updateMediaObjectInfo", parameters={Parameter(name='updateMe')})
MediaPlayer_MediaApi.methods={MediaPlayer_MediaApi_m_pause, MediaPlayer_MediaApi_m_stop, MediaPlayer_MediaApi_m_init, MediaPlayer_MediaApi_m_play, MediaPlayer_MediaApi_m_canPlay, MediaPlayer_MediaApi_m_dispose, MediaPlayer_MediaApi_m_updateMediaObjectInfo}

# MediaPlayer_PlayLayer class attributes and methods
MediaPlayer_PlayLayer_m_registerApi: Method = Method(name="registerApi", parameters={Parameter(name='addMe')})
MediaPlayer_PlayLayer_m_unregisterApi: Method = Method(name="unregisterApi", parameters={Parameter(name='unregisterMe')})
MediaPlayer_PlayLayer.methods={MediaPlayer_PlayLayer_m_unregisterApi, MediaPlayer_PlayLayer_m_registerApi}

# MediaPlayer_Library class attributes and methods

# MediaPlayer_BaseObject class attributes and methods
MediaPlayer_BaseObject_id: Property = Property(name="id", type=IntegerType)
MediaPlayer_BaseObject_propertyChangeSupport: Property = Property(name="propertyChangeSupport", type=StringType)
MediaPlayer_BaseObject_m_addPropertyChangeListener: Method = Method(name="addPropertyChangeListener", parameters={Parameter(name='listener')})
MediaPlayer_BaseObject_m_removePropertyChangeListener: Method = Method(name="removePropertyChangeListener", parameters={Parameter(name='listener')})
MediaPlayer_BaseObject.attributes={MediaPlayer_BaseObject_id, MediaPlayer_BaseObject_propertyChangeSupport}
MediaPlayer_BaseObject.methods={MediaPlayer_BaseObject_m_addPropertyChangeListener, MediaPlayer_BaseObject_m_removePropertyChangeListener}

# Relationships
currentlyPlaying1: BinaryAssociation = BinaryAssociation(
    name="currentlyPlaying1",
    ends={
        Property(name="MediaPlayer_MediaObject2", type=MediaPlayer_MediaApi, multiplicity=Multiplicity(1, 1)),
        Property(name="MediaPlayer_MediaApi", type=MediaPlayer_MediaObject, multiplicity=Multiplicity(0, 9999))
    }
)
currentlyPaused3: BinaryAssociation = BinaryAssociation(
    name="currentlyPaused3",
    ends={
        Property(name="MediaPlayer_MediaObject5", type=MediaPlayer_MediaApi, multiplicity=Multiplicity(1, 1)),
        Property(name="MediaPlayer_MediaApi4", type=MediaPlayer_MediaObject, multiplicity=Multiplicity(0, 9999))
    }
)
mediaList0: BinaryAssociation = BinaryAssociation(
    name="mediaList0",
    ends={
        Property(name="MediaPlayer_MediaObject", type=MediaPlayer_Playlist, multiplicity=Multiplicity(1, 1)),
        Property(name="MediaPlayer_Playlist", type=MediaPlayer_MediaObject, multiplicity=Multiplicity(0, 9999))
    }
)
installedApi6: BinaryAssociation = BinaryAssociation(
    name="installedApi6",
    ends={
        Property(name="MediaPlayer_MediaApi7", type=MediaPlayer_PlayLayer, multiplicity=Multiplicity(1, 1)),
        Property(name="MediaPlayer_PlayLayer", type=MediaPlayer_MediaApi, multiplicity=Multiplicity(0, 9999))
    }
)
myLibrary8: BinaryAssociation = BinaryAssociation(
    name="myLibrary8",
    ends={
        Property(name="MediaPlayer_Library", type=MediaPlayer_PlayLayer, multiplicity=Multiplicity(1, 1)),
        Property(name="MediaPlayer_PlayLayer9", type=MediaPlayer_Library, multiplicity=Multiplicity(0, 1))
    }
)
mediaLibrary10: BinaryAssociation = BinaryAssociation(
    name="mediaLibrary10",
    ends={
        Property(name="MediaPlayer_MediaObject12", type=MediaPlayer_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="MediaPlayer_Library11", type=MediaPlayer_MediaObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_MediaPlayer_Playlist_BaseObject = Generalization(general=BaseObject, specific=MediaPlayer_Playlist)
gen_MediaPlayer_MediaObject_BaseObject = Generalization(general=BaseObject, specific=MediaPlayer_MediaObject)
gen_MediaPlayer_Library_BaseObject = Generalization(general=BaseObject, specific=MediaPlayer_Library)

# Domain Model
domain_model = DomainModel(
    name="MediaPlayer",
    types={MediaPlayer_Playlist, BaseObject, MediaPlayer_MediaObject, MediaPlayer_MediaApi, MediaPlayer_PlayLayer, MediaPlayer_Library, MediaPlayer_BaseObject, State},
    associations={currentlyPlaying1, currentlyPaused3, mediaList0, installedApi6, myLibrary8, mediaLibrary10},
    generalizations={gen_MediaPlayer_Playlist_BaseObject, gen_MediaPlayer_MediaObject_BaseObject, gen_MediaPlayer_Library_BaseObject},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)