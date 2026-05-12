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
Reciever = Class(name="Reciever")
Principal = Class(name="Principal")
Sender = Class(name="Sender")
Post = Class(name="Post")
N_Disturb_User = Class(name="N_Disturb_User")
Key = Class(name="Key")
Hashtag = Class(name="Hashtag")
Like = Class(name="Like")
Mention = Class(name="Mention")
Message = Class(name="Message")
Following_Hashtag = Class(name="Following_Hashtag")
Cryptostream = Class(name="Cryptostream")
Comment = Class(name="Comment")
Another_Login = Class(name="Another_Login")
Class_ = Class(name="Class")

# Reciever class attributes and methods
Reciever_user_id: Property = Property(name="user_id", type=IntegerType)
Reciever_id: Property = Property(name="id", type=IntegerType)
Reciever_name: Property = Property(name="name", type=StringType)
Reciever_surname: Property = Property(name="surname", type=StringType)
Reciever_username: Property = Property(name="username", type=StringType)
Reciever_mail: Property = Property(name="mail", type=StringType)
Reciever_password: Property = Property(name="password", type=StringType)
Reciever_phone: Property = Property(name="phone", type=StringType)
Reciever_is_private: Property = Property(name="is_private", type=BooleanType)
Reciever_is_active: Property = Property(name="is_active", type=BooleanType)
Reciever_is_admin: Property = Property(name="is_admin", type=BooleanType)
Reciever.attributes={Reciever_username, Reciever_password, Reciever_is_admin, Reciever_mail, Reciever_id, Reciever_surname, Reciever_is_active, Reciever_user_id, Reciever_phone, Reciever_name, Reciever_is_private}

# Principal class attributes and methods
Principal_id: Property = Property(name="id", type=IntegerType)
Principal_user_id: Property = Property(name="user_id", type=IntegerType)
Principal_followers_id: Property = Property(name="followers_id", type=IntegerType)
Principal_status: Property = Property(name="status", type=StringType)
Principal_creation_date: Property = Property(name="creation_date", type=StringType)
Principal.attributes={Principal_id, Principal_user_id, Principal_creation_date, Principal_followers_id, Principal_status}

# Sender class attributes and methods
Sender_id: Property = Property(name="id", type=IntegerType)
Sender_user_id: Property = Property(name="user_id", type=IntegerType)
Sender_following_id: Property = Property(name="following_id", type=IntegerType)
Sender_status: Property = Property(name="status", type=StringType)
Sender_creation_date: Property = Property(name="creation_date", type=StringType)
Sender.attributes={Sender_user_id, Sender_id, Sender_following_id, Sender_creation_date, Sender_status}

# Post class attributes and methods
Post_id: Property = Property(name="id", type=IntegerType)
Post_text: Property = Property(name="text", type=StringType)
Post_location_id: Property = Property(name="location_id", type=IntegerType)
Post_hashtag_id: Property = Property(name="hashtag_id", type=IntegerType)
Post_total_like: Property = Property(name="total_like", type=IntegerType)
Post_creation_date: Property = Property(name="creation_date", type=StringType)
Post_date_update: Property = Property(name="date_update", type=StringType)
Post_status: Property = Property(name="status", type=StringType)
Post.attributes={Post_status, Post_id, Post_total_like, Post_creation_date, Post_hashtag_id, Post_location_id, Post_date_update, Post_text}

# N_Disturb_User class attributes and methods
N_Disturb_User_id: Property = Property(name="id", type=IntegerType)
N_Disturb_User_user_id: Property = Property(name="user_id", type=IntegerType)
N_Disturb_User_disturb_user_id: Property = Property(name="disturb_user_id", type=IntegerType)
N_Disturb_User.attributes={N_Disturb_User_id, N_Disturb_User_disturb_user_id, N_Disturb_User_user_id}

# Key class attributes and methods
Key_id: Property = Property(name="id", type=IntegerType)
Key_Length: Property = Property(name="Length", type=StringType)
Key_Value: Property = Property(name="Value", type=StringType)
Key_coordinat_y: Property = Property(name="coordinat_y", type=IntegerType)
Key.attributes={Key_coordinat_y, Key_Value, Key_Length, Key_id}

# Hashtag class attributes and methods
Hashtag_id: Property = Property(name="id", type=IntegerType)
Hashtag_tag: Property = Property(name="tag", type=StringType)
Hashtag.attributes={Hashtag_id, Hashtag_tag}

# Like class attributes and methods
Like_id: Property = Property(name="id", type=IntegerType)
Like_post_id: Property = Property(name="post_id", type=IntegerType)
Like_user_id: Property = Property(name="user_id", type=IntegerType)
Like_date_sent: Property = Property(name="date_sent", type=StringType)
Like.attributes={Like_id, Like_user_id, Like_post_id, Like_date_sent}

# Mention class attributes and methods
Mention_id: Property = Property(name="id", type=IntegerType)
Mention_post_id: Property = Property(name="post_id", type=IntegerType)
Mention_user_id: Property = Property(name="user_id", type=IntegerType)
Mention.attributes={Mention_id, Mention_post_id, Mention_user_id}

# Message class attributes and methods
Message_id: Property = Property(name="id", type=IntegerType)
Message_sender_id: Property = Property(name="sender_id", type=IntegerType)
Message_receiver_id: Property = Property(name="receiver_id", type=IntegerType)
Message_message: Property = Property(name="message", type=StringType)
Message_creation_date: Property = Property(name="creation_date", type=StringType)
Message_date_seen: Property = Property(name="date_seen", type=StringType)
Message_is_deleted: Property = Property(name="is_deleted", type=BooleanType)
Message.attributes={Message_id, Message_message, Message_is_deleted, Message_creation_date, Message_date_seen, Message_receiver_id, Message_sender_id}

# Following_Hashtag class attributes and methods
Following_Hashtag_id: Property = Property(name="id", type=IntegerType)
Following_Hashtag_user_id: Property = Property(name="user_id", type=IntegerType)
Following_Hashtag_hashtag_id: Property = Property(name="hashtag_id", type=IntegerType)
Following_Hashtag.attributes={Following_Hashtag_user_id, Following_Hashtag_id, Following_Hashtag_hashtag_id}

# Cryptostream class attributes and methods
Cryptostream_id: Property = Property(name="id", type=IntegerType)
Cryptostream_user_id: Property = Property(name="user_id", type=IntegerType)
Cryptostream_blocked_user_id: Property = Property(name="blocked_user_id", type=IntegerType)
Cryptostream.attributes={Cryptostream_id, Cryptostream_user_id, Cryptostream_blocked_user_id}

# Comment class attributes and methods
Comment_id: Property = Property(name="id", type=IntegerType)
Comment_content: Property = Property(name="content", type=IntegerType)
Comment_post_id: Property = Property(name="post_id", type=IntegerType)
Comment_user_id: Property = Property(name="user_id", type=IntegerType)
Comment_creation_date: Property = Property(name="creation_date", type=StringType)
Comment_comment_id: Property = Property(name="comment_id", type=IntegerType)
Comment.attributes={Comment_user_id, Comment_content, Comment_comment_id, Comment_id, Comment_post_id, Comment_creation_date}

# Another_Login class attributes and methods
Another_Login_id: Property = Property(name="id", type=IntegerType)
Another_Login_user_id: Property = Property(name="user_id", type=IntegerType)
Another_Login_facebook_id: Property = Property(name="facebook_id", type=IntegerType)
Another_Login.attributes={Another_Login_id, Another_Login_facebook_id, Another_Login_user_id}

# Class class attributes and methods

# Relationships
User_Mention: BinaryAssociation = BinaryAssociation(
    name="User_Mention",
    ends={
        Property(name="mention10", type=Mention, multiplicity=Multiplicity(1, 1)),
        Property(name="user11", type=Reciever, multiplicity=Multiplicity(1, 1))
    }
)
Like_Post: BinaryAssociation = BinaryAssociation(
    name="Like_Post",
    ends={
        Property(name="post12", type=Post, multiplicity=Multiplicity(1, 1)),
        Property(name="like13", type=Like, multiplicity=Multiplicity(0, 9999))
    }
)
Comment_Post: BinaryAssociation = BinaryAssociation(
    name="Comment_Post",
    ends={
        Property(name="post14", type=Post, multiplicity=Multiplicity(1, 1)),
        Property(name="comment15", type=Comment, multiplicity=Multiplicity(0, 9999))
    }
)
Hashtag_Post: BinaryAssociation = BinaryAssociation(
    name="Hashtag_Post",
    ends={
        Property(name="post16", type=Post, multiplicity=Multiplicity(0, 9999)),
        Property(name="hashtag17", type=Hashtag, multiplicity=Multiplicity(0, 9999))
    }
)
Hashtag_Following_Hashtag: BinaryAssociation = BinaryAssociation(
    name="Hashtag_Following_Hashtag",
    ends={
        Property(name="following_Hashtag18", type=Following_Hashtag, multiplicity=Multiplicity(1, 1)),
        Property(name="hashtag19", type=Hashtag, multiplicity=Multiplicity(1, 1))
    }
)
Location_Post: BinaryAssociation = BinaryAssociation(
    name="Location_Post",
    ends={
        Property(name="post20", type=Post, multiplicity=Multiplicity(1, 1)),
        Property(name="location21", type=Key, multiplicity=Multiplicity(0, 1))
    }
)
Post_Mention: BinaryAssociation = BinaryAssociation(
    name="Post_Mention",
    ends={
        Property(name="mention22", type=Mention, multiplicity=Multiplicity(0, 9999)),
        Property(name="post23", type=Post, multiplicity=Multiplicity(1, 1))
    }
)
User_Message: BinaryAssociation = BinaryAssociation(
    name="User_Message",
    ends={
        Property(name="message24", type=Message, multiplicity=Multiplicity(0, 9999)),
        Property(name="user25", type=Reciever, multiplicity=Multiplicity(1, 9999))
    }
)
User_Following_Hashtag: BinaryAssociation = BinaryAssociation(
    name="User_Following_Hashtag",
    ends={
        Property(name="following_Hashtag26", type=Following_Hashtag, multiplicity=Multiplicity(0, 9999)),
        Property(name="user27", type=Reciever, multiplicity=Multiplicity(0, 9999))
    }
)
User_Like: BinaryAssociation = BinaryAssociation(
    name="User_Like",
    ends={
        Property(name="like28", type=Like, multiplicity=Multiplicity(0, 1)),
        Property(name="user29", type=Reciever, multiplicity=Multiplicity(0, 1))
    }
)
User_Comment: BinaryAssociation = BinaryAssociation(
    name="User_Comment",
    ends={
        Property(name="comment30", type=Comment, multiplicity=Multiplicity(0, 9999)),
        Property(name="user31", type=Reciever, multiplicity=Multiplicity(1, 1))
    }
)
Comment_Comment: BinaryAssociation = BinaryAssociation(
    name="Comment_Comment",
    ends={
        Property(name="comment32", type=Comment, multiplicity=Multiplicity(0, 1)),
        Property(name="comment33", type=Comment, multiplicity=Multiplicity(0, 9999))
    }
)
User_Another_Login: BinaryAssociation = BinaryAssociation(
    name="User_Another_Login",
    ends={
        Property(name="another_Login34", type=Another_Login, multiplicity=Multiplicity(1, 1)),
        Property(name="user35", type=Reciever, multiplicity=Multiplicity(1, 1))
    }
)
Key_Sender: BinaryAssociation = BinaryAssociation(
    name="Key_Sender",
    ends={
        Property(name="sender36", type=Sender, multiplicity=Multiplicity(0, 1)),
        Property(name="key37", type=Key, multiplicity=Multiplicity(0, 1))
    }
)
User_Blocked_User: BinaryAssociation = BinaryAssociation(
    name="User_Blocked_User",
    ends={
        Property(name="blocked_User0", type=Cryptostream, multiplicity=Multiplicity(0, 9999)),
        Property(name="user1", type=Reciever, multiplicity=Multiplicity(1, 1))
    }
)
User_N_Disturb_User: BinaryAssociation = BinaryAssociation(
    name="User_N_Disturb_User",
    ends={
        Property(name="n_Disturb_User2", type=N_Disturb_User, multiplicity=Multiplicity(0, 9999)),
        Property(name="user3", type=Reciever, multiplicity=Multiplicity(1, 1))
    }
)
User_Followers: BinaryAssociation = BinaryAssociation(
    name="User_Followers",
    ends={
        Property(name="followers4", type=Principal, multiplicity=Multiplicity(0, 9999)),
        Property(name="user5", type=Reciever, multiplicity=Multiplicity(0, 9999))
    }
)
User_Following: BinaryAssociation = BinaryAssociation(
    name="User_Following",
    ends={
        Property(name="following6", type=Sender, multiplicity=Multiplicity(0, 9999)),
        Property(name="user7", type=Reciever, multiplicity=Multiplicity(0, 9999))
    }
)
Post_User: BinaryAssociation = BinaryAssociation(
    name="Post_User",
    ends={
        Property(name="user8", type=Reciever, multiplicity=Multiplicity(1, 1)),
        Property(name="post9", type=Post, multiplicity=Multiplicity(0, 9999))
    }
)
Key_Reciever: BinaryAssociation = BinaryAssociation(
    name="Key_Reciever",
    ends={
        Property(name="reciever38", type=Reciever, multiplicity=Multiplicity(0, 1)),
        Property(name="key39", type=Key, multiplicity=Multiplicity(0, 1))
    }
)
Principal_Reciever: BinaryAssociation = BinaryAssociation(
    name="Principal_Reciever",
    ends={
        Property(name="reciever40", type=Reciever, multiplicity=Multiplicity(0, 1)),
        Property(name="principal41", type=Principal, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_10df3248_c27d_4706_991b_1d85c0e2be06",
    types={Reciever, Principal, Sender, Post, N_Disturb_User, Key, Hashtag, Like, Mention, Message, Following_Hashtag, Cryptostream, Comment, Another_Login, Class_},
    associations={User_Mention, Like_Post, Comment_Post, Hashtag_Post, Hashtag_Following_Hashtag, Location_Post, Post_Mention, User_Message, User_Following_Hashtag, User_Like, User_Comment, Comment_Comment, User_Another_Login, Key_Sender, User_Blocked_User, User_N_Disturb_User, User_Followers, User_Following, Post_User, Key_Reciever, Principal_Reciever},
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