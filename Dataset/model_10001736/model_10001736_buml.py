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
Song = Class(name="Song")
Playlist = Class(name="Playlist")
Playlist_Song = Class(name="Playlist_Song")
Favourites = Class(name="Favourites")
Downloads = Class(name="Downloads")
Recently_Played = Class(name="Recently_Played")
TopMostPlayed = Class(name="TopMostPlayed")
User_Actor = Class(name="User_Actor")
Download_UseCase = Class(name="Download_UseCase")
Play_UseCase = Class(name="Play_UseCase")
Create_playlist_UseCase = Class(name="Create_playlist_UseCase")
Search_UseCase = Class(name="Search_UseCase")
Favorite_UseCase = Class(name="Favorite_UseCase")
Pause_UseCase = Class(name="Pause_UseCase")
Stop_UseCase = Class(name="Stop_UseCase")
Shuflfe_play_UseCase = Class(name="Shuflfe_play_UseCase")
Repeat_Non_UseCase = Class(name="Repeat_Non_UseCase")
Actor_Actor = Class(name="Actor_Actor")
UseCase_UseCase = Class(name="UseCase_UseCase")

# Song class attributes and methods
Song_sID: Property = Property(name="sID", type=IntegerType)
Song_sName: Property = Property(name="sName", type=StringType)
Song_sCateg: Property = Property(name="sCateg", type=StringType)
Song_sArtist: Property = Property(name="sArtist", type=StringType)
Song_sDate: Property = Property(name="sDate", type=StringType)
Song_sIMG_url: Property = Property(name="sIMG_url", type=StringType)
Song.attributes={Song_sArtist, Song_sID, Song_sCateg, Song_sName, Song_sIMG_url, Song_sDate}

# Playlist class attributes and methods
Playlist_pID: Property = Property(name="pID", type=IntegerType)
Playlist_pName: Property = Property(name="pName", type=StringType)
Playlist_pDate: Property = Property(name="pDate", type=StringType)
Playlist.attributes={Playlist_pID, Playlist_pName, Playlist_pDate}

# Playlist_Song class attributes and methods
Playlist_Song_pID: Property = Property(name="pID", type=IntegerType)
Playlist_Song_sID: Property = Property(name="sID", type=IntegerType)
Playlist_Song.attributes={Playlist_Song_pID, Playlist_Song_sID}

# Favourites class attributes and methods
Favourites_fID: Property = Property(name="fID", type=IntegerType)
Favourites_sID: Property = Property(name="sID", type=IntegerType)
Favourites.attributes={Favourites_sID, Favourites_fID}

# Downloads class attributes and methods
Downloads_dID: Property = Property(name="dID", type=IntegerType)
Downloads_sID: Property = Property(name="sID", type=IntegerType)
Downloads.attributes={Downloads_dID, Downloads_sID}

# Recently_Played class attributes and methods
Recently_Played_rpID: Property = Property(name="rpID", type=IntegerType)
Recently_Played_sID: Property = Property(name="sID", type=IntegerType)
Recently_Played.attributes={Recently_Played_rpID, Recently_Played_sID}

# TopMostPlayed class attributes and methods
TopMostPlayed_mpID: Property = Property(name="mpID", type=IntegerType)
TopMostPlayed_sID: Property = Property(name="sID", type=IntegerType)
TopMostPlayed.attributes={TopMostPlayed_sID, TopMostPlayed_mpID}

# User_Actor class attributes and methods

# Download_UseCase class attributes and methods

# Play_UseCase class attributes and methods

# Create_playlist_UseCase class attributes and methods

# Search_UseCase class attributes and methods

# Favorite_UseCase class attributes and methods

# Pause_UseCase class attributes and methods

# Stop_UseCase class attributes and methods

# Shuflfe_play_UseCase class attributes and methods

# Repeat_Non_UseCase class attributes and methods

# Actor_Actor class attributes and methods

# UseCase_UseCase class attributes and methods

# Relationships
Song_Playlist_Song: BinaryAssociation = BinaryAssociation(
    name="Song_Playlist_Song",
    ends={
        Property(name="playlist_Song0", type=Playlist_Song, multiplicity=Multiplicity(0, 1)),
        Property(name="song1", type=Song, multiplicity=Multiplicity(0, 1))
    }
)
Playlist_Playlist_Song: BinaryAssociation = BinaryAssociation(
    name="Playlist_Playlist_Song",
    ends={
        Property(name="playlist_Song2", type=Playlist_Song, multiplicity=Multiplicity(0, 1)),
        Property(name="playlist3", type=Playlist, multiplicity=Multiplicity(0, 1))
    }
)
User_UseCase: BinaryAssociation = BinaryAssociation(
    name="User_UseCase",
    ends={
        Property(name="useCase4", type=Download_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="user5", type=User_Actor, multiplicity=Multiplicity(0, 1))
    }
)
User_UseCase4: BinaryAssociation = BinaryAssociation(
    name="User_UseCase4",
    ends={
        Property(name="useCase46", type=Search_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="user7", type=User_Actor, multiplicity=Multiplicity(0, 1))
    }
)
User_UseCase2: BinaryAssociation = BinaryAssociation(
    name="User_UseCase2",
    ends={
        Property(name="useCase28", type=Play_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="user9", type=User_Actor, multiplicity=Multiplicity(0, 1))
    }
)
User_UseCase3: BinaryAssociation = BinaryAssociation(
    name="User_UseCase3",
    ends={
        Property(name="useCase310", type=Create_playlist_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="user11", type=User_Actor, multiplicity=Multiplicity(0, 1))
    }
)
User_UseCase5: BinaryAssociation = BinaryAssociation(
    name="User_UseCase5",
    ends={
        Property(name="useCase512", type=Favorite_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="user13", type=User_Actor, multiplicity=Multiplicity(0, 1))
    }
)
UseCase_Play: BinaryAssociation = BinaryAssociation(
    name="UseCase_Play",
    ends={
        Property(name="play14", type=Play_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="useCase15", type=Pause_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
UseCase2_Play: BinaryAssociation = BinaryAssociation(
    name="UseCase2_Play",
    ends={
        Property(name="play16", type=Play_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="useCase217", type=Stop_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
UseCase3_Play: BinaryAssociation = BinaryAssociation(
    name="UseCase3_Play",
    ends={
        Property(name="play18", type=Play_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="useCase319", type=Shuflfe_play_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
UseCase4_Play: BinaryAssociation = BinaryAssociation(
    name="UseCase4_Play",
    ends={
        Property(name="play20", type=Play_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="useCase421", type=Repeat_Non_UseCase, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_RzoAMNA_EeeLcIicqHdTUQ",
    types={Song, Playlist, Playlist_Song, Favourites, Downloads, Recently_Played, TopMostPlayed, User_Actor, Download_UseCase, Play_UseCase, Create_playlist_UseCase, Search_UseCase, Favorite_UseCase, Pause_UseCase, Stop_UseCase, Shuflfe_play_UseCase, Repeat_Non_UseCase, Actor_Actor, UseCase_UseCase},
    associations={Song_Playlist_Song, Playlist_Playlist_Song, User_UseCase, User_UseCase4, User_UseCase2, User_UseCase3, User_UseCase5, UseCase_Play, UseCase2_Play, UseCase3_Play, UseCase4_Play},
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