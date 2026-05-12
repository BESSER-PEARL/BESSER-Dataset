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
USER = Class(name="USER")
ROLES = Class(name="ROLES")
PRODUCT = Class(name="PRODUCT")
CATEGORIAS = Class(name="CATEGORIAS")
WHISES = Class(name="WHISES")
QUESTIONS = Class(name="QUESTIONS")
SHOPPING_HISTORY = Class(name="SHOPPING_HISTORY")
STATUS = Class(name="STATUS")
SHIPPING_METHODS = Class(name="SHIPPING_METHODS")
SUBSCRIPTION_BENEFITS = Class(name="SUBSCRIPTION_BENEFITS")
STATUS2 = Class(name="STATUS2")
STATUS_SHOPPING_HISTORY = Class(name="STATUS_SHOPPING_HISTORY")
STORE = Class(name="STORE")
FAVORITES = Class(name="FAVORITES")
EVENTS_HISTORY = Class(name="EVENTS_HISTORY")
EVENTS_LIST = Class(name="EVENTS_LIST")
Class_ = Class(name="Class")
NOTIFICATION = Class(name="NOTIFICATION")
REFUND = Class(name="REFUND")
REFUND_MESSAGES = Class(name="REFUND_MESSAGES")
SOCIAL_NETWORKS = Class(name="SOCIAL_NETWORKS")
FOLLOW = Class(name="FOLLOW")
FEEDBACK = Class(name="FEEDBACK")
SHOPPING_MESSENGER = Class(name="SHOPPING_MESSENGER")
FEEDBACK_COMMENT = Class(name="FEEDBACK_COMMENT")
FOLLOW_MESSENGER = Class(name="FOLLOW_MESSENGER")

# USER class attributes and methods
USER__id: Property = Property(name="_id", type=StringType)
USER_createdAt: Property = Property(name="createdAt", type=StringType)
USER_updateAt: Property = Property(name="updateAt", type=StringType)
USER_status: Property = Property(name="status", type=StringType)
USER_email: Property = Property(name="email", type=StringType)
USER_password: Property = Property(name="password", type=StringType)
USER_address: Property = Property(name="address", type=StringType)
USER_telephone: Property = Property(name="telephone", type=StringType)
USER_name: Property = Property(name="name", type=StringType)
USER_surname: Property = Property(name="surname", type=StringType)
USER_verified: Property = Property(name="verified", type=BooleanType)
USER_lastAccess: Property = Property(name="lastAccess", type=StringType)
USER.attributes={USER_verified, USER_status, USER_telephone, USER_updateAt, USER__id, USER_email, USER_name, USER_createdAt, USER_address, USER_password, USER_surname, USER_lastAccess}

# ROLES class attributes and methods
ROLES__id: Property = Property(name="_id", type=StringType)
ROLES_createdAt: Property = Property(name="createdAt", type=StringType)
ROLES_name: Property = Property(name="name", type=StringType)
ROLES.attributes={ROLES__id, ROLES_name, ROLES_createdAt}

# PRODUCT class attributes and methods
PRODUCT__id: Property = Property(name="_id", type=StringType)
PRODUCT_createdAt: Property = Property(name="createdAt", type=StringType)
PRODUCT_statusId: Property = Property(name="statusId", type=StringType)
PRODUCT_storeId: Property = Property(name="storeId", type=StringType)
PRODUCT_name: Property = Property(name="name", type=StringType)
PRODUCT_price: Property = Property(name="price", type=IntegerType)
PRODUCT_sold: Property = Property(name="sold", type=IntegerType)
PRODUCT_isNew: Property = Property(name="isNew", type=BooleanType)
PRODUCT_description: Property = Property(name="description", type=StringType)
PRODUCT_quantity: Property = Property(name="quantity", type=IntegerType)
PRODUCT_photos: Property = Property(name="photos", type=StringType)
PRODUCT_relatedProducts: Property = Property(name="relatedProducts", type=StringType)
PRODUCT_dimensions: Property = Property(name="dimensions", type=StringType)
PRODUCT_attribute: Property = Property(name="attribute", type=StringType)
PRODUCT_color: Property = Property(name="color", type=StringType)
PRODUCT_model: Property = Property(name="model", type=StringType)
PRODUCT_ShippingMethods: Property = Property(name="ShippingMethods", type=StringType)
PRODUCT.attributes={PRODUCT__id, PRODUCT_ShippingMethods, PRODUCT_description, PRODUCT_storeId, PRODUCT_isNew, PRODUCT_price, PRODUCT_color, PRODUCT_relatedProducts, PRODUCT_createdAt, PRODUCT_model, PRODUCT_sold, PRODUCT_name, PRODUCT_quantity, PRODUCT_statusId, PRODUCT_photos, PRODUCT_attribute, PRODUCT_dimensions}

# CATEGORIAS class attributes and methods
CATEGORIAS__id: Property = Property(name="_id", type=StringType)
CATEGORIAS_createdAt: Property = Property(name="createdAt", type=StringType)
CATEGORIAS_name: Property = Property(name="name", type=StringType)
CATEGORIAS.attributes={CATEGORIAS_createdAt, CATEGORIAS__id, CATEGORIAS_name}

# WHISES class attributes and methods
WHISES_createdAt: Property = Property(name="createdAt", type=StringType)
WHISES_statusId: Property = Property(name="statusId", type=StringType)
WHISES_userId: Property = Property(name="userId", type=StringType)
WHISES_productId: Property = Property(name="productId", type=StringType)
WHISES__id: Property = Property(name="_id", type=StringType)
WHISES.attributes={WHISES_createdAt, WHISES_userId, WHISES_productId, WHISES__id, WHISES_statusId}

# QUESTIONS class attributes and methods
QUESTIONS__id: Property = Property(name="_id", type=StringType)
QUESTIONS_createdAt: Property = Property(name="createdAt", type=StringType)
QUESTIONS_statusId: Property = Property(name="statusId", type=StringType)
QUESTIONS_userId: Property = Property(name="userId", type=StringType)
QUESTIONS_productId: Property = Property(name="productId", type=StringType)
QUESTIONS_question: Property = Property(name="question", type=StringType)
QUESTIONS_answer: Property = Property(name="answer", type=StringType)
QUESTIONS_score: Property = Property(name="score", type=IntegerType)
QUESTIONS.attributes={QUESTIONS_userId, QUESTIONS_question, QUESTIONS_productId, QUESTIONS_createdAt, QUESTIONS_statusId, QUESTIONS_answer, QUESTIONS__id, QUESTIONS_score}

# SHOPPING_HISTORY class attributes and methods
SHOPPING_HISTORY__id: Property = Property(name="_id", type=StringType)
SHOPPING_HISTORY_created_at: Property = Property(name="created_at", type=StringType)
SHOPPING_HISTORY_status: Property = Property(name="status", type=StringType)
SHOPPING_HISTORY_userId: Property = Property(name="userId", type=StringType)
SHOPPING_HISTORY_storeId: Property = Property(name="storeId", type=StringType)
SHOPPING_HISTORY_productId: Property = Property(name="productId", type=StringType)
SHOPPING_HISTORY_name: Property = Property(name="name", type=StringType)
SHOPPING_HISTORY_price: Property = Property(name="price", type=IntegerType)
SHOPPING_HISTORY_isNew: Property = Property(name="isNew", type=BooleanType)
SHOPPING_HISTORY_photos: Property = Property(name="photos", type=StringType)
SHOPPING_HISTORY_description: Property = Property(name="description", type=StringType)
SHOPPING_HISTORY_quantity: Property = Property(name="quantity", type=IntegerType)
SHOPPING_HISTORY_sold: Property = Property(name="sold", type=IntegerType)
SHOPPING_HISTORY_isSold: Property = Property(name="isSold", type=BooleanType)
SHOPPING_HISTORY_attribute: Property = Property(name="attribute", type=StringType)
SHOPPING_HISTORY_STATUS_SHOPPING_HIST_ID: Property = Property(name="STATUS_SHOPPING_HIST_ID", type=StringType)
SHOPPING_HISTORY_shipArrival: Property = Property(name="shipArrival", type=StringType)
SHOPPING_HISTORY_shipName: Property = Property(name="shipName", type=StringType)
SHOPPING_HISTORY_shipAddress: Property = Property(name="shipAddress", type=StringType)
SHOPPING_HISTORY_shipPrice: Property = Property(name="shipPrice", type=IntegerType)
SHOPPING_HISTORY_score: Property = Property(name="score", type=IntegerType)
SHOPPING_HISTORY_comment: Property = Property(name="comment", type=StringType)
SHOPPING_HISTORY_note: Property = Property(name="note", type=StringType)
SHOPPING_HISTORY.attributes={SHOPPING_HISTORY_isSold, SHOPPING_HISTORY_isNew, SHOPPING_HISTORY_photos, SHOPPING_HISTORY_attribute, SHOPPING_HISTORY__id, SHOPPING_HISTORY_status, SHOPPING_HISTORY_price, SHOPPING_HISTORY_shipPrice, SHOPPING_HISTORY_userId, SHOPPING_HISTORY_quantity, SHOPPING_HISTORY_shipArrival, SHOPPING_HISTORY_sold, SHOPPING_HISTORY_productId, SHOPPING_HISTORY_score, SHOPPING_HISTORY_note, SHOPPING_HISTORY_storeId, SHOPPING_HISTORY_shipAddress, SHOPPING_HISTORY_comment, SHOPPING_HISTORY_created_at, SHOPPING_HISTORY_description, SHOPPING_HISTORY_STATUS_SHOPPING_HIST_ID, SHOPPING_HISTORY_shipName, SHOPPING_HISTORY_name}

# STATUS class attributes and methods
STATUS__id: Property = Property(name="_id", type=StringType)
STATUS_createdAt: Property = Property(name="createdAt", type=StringType)
STATUS_name: Property = Property(name="name", type=StringType)
STATUS.attributes={STATUS__id, STATUS_name, STATUS_createdAt}

# SHIPPING_METHODS class attributes and methods
SHIPPING_METHODS__id: Property = Property(name="_id", type=StringType)
SHIPPING_METHODS_createdAt: Property = Property(name="createdAt", type=StringType)
SHIPPING_METHODS_name: Property = Property(name="name", type=StringType)
SHIPPING_METHODS_arrival: Property = Property(name="arrival", type=StringType)
SHIPPING_METHODS_address: Property = Property(name="address", type=StringType)
SHIPPING_METHODS_price: Property = Property(name="price", type=IntegerType)
SHIPPING_METHODS.attributes={SHIPPING_METHODS_price, SHIPPING_METHODS__id, SHIPPING_METHODS_createdAt, SHIPPING_METHODS_address, SHIPPING_METHODS_name, SHIPPING_METHODS_arrival}

# SUBSCRIPTION_BENEFITS class attributes and methods
SUBSCRIPTION_BENEFITS__id: Property = Property(name="_id", type=StringType)
SUBSCRIPTION_BENEFITS_key_name: Property = Property(name="key_name", type=StringType)
SUBSCRIPTION_BENEFITS_description: Property = Property(name="description", type=StringType)
SUBSCRIPTION_BENEFITS.attributes={SUBSCRIPTION_BENEFITS_key_name, SUBSCRIPTION_BENEFITS_description, SUBSCRIPTION_BENEFITS__id}

# STATUS2 class attributes and methods
STATUS2__id: Property = Property(name="_id", type=StringType)
STATUS2_name: Property = Property(name="name", type=StringType)
STATUS2.attributes={STATUS2__id, STATUS2_name}

# STATUS_SHOPPING_HISTORY class attributes and methods
STATUS_SHOPPING_HISTORY__id: Property = Property(name="_id", type=StringType)
STATUS_SHOPPING_HISTORY_name: Property = Property(name="name", type=StringType)
STATUS_SHOPPING_HISTORY.attributes={STATUS_SHOPPING_HISTORY_name, STATUS_SHOPPING_HISTORY__id}

# STORE class attributes and methods
STORE__id: Property = Property(name="_id", type=StringType)
STORE_createdAt: Property = Property(name="createdAt", type=StringType)
STORE_updateAt: Property = Property(name="updateAt", type=StringType)
STORE_statusId: Property = Property(name="statusId", type=StringType)
STORE_email: Property = Property(name="email", type=StringType)
STORE_address: Property = Property(name="address", type=StringType)
STORE_telephone: Property = Property(name="telephone", type=StringType)
STORE_name: Property = Property(name="name", type=StringType)
STORE_schedule: Property = Property(name="schedule", type=StringType)
STORE.attributes={STORE__id, STORE_name, STORE_schedule, STORE_telephone, STORE_statusId, STORE_email, STORE_createdAt, STORE_address, STORE_updateAt}

# FAVORITES class attributes and methods
FAVORITES__id: Property = Property(name="_id", type=StringType)
FAVORITES_createdAt: Property = Property(name="createdAt", type=StringType)
FAVORITES_statusId: Property = Property(name="statusId", type=StringType)
FAVORITES_userId: Property = Property(name="userId", type=StringType)
FAVORITES_storeId: Property = Property(name="storeId", type=StringType)
FAVORITES.attributes={FAVORITES_statusId, FAVORITES_createdAt, FAVORITES_userId, FAVORITES_storeId, FAVORITES__id}

# EVENTS_HISTORY class attributes and methods
EVENTS_HISTORY__id: Property = Property(name="_id", type=StringType)
EVENTS_HISTORY_createdAt: Property = Property(name="createdAt", type=StringType)
EVENTS_HISTORY_userId: Property = Property(name="userId", type=StringType)
EVENTS_HISTORY_eventId: Property = Property(name="eventId", type=StringType)
EVENTS_HISTORY_oldValue: Property = Property(name="oldValue", type=StringType)
EVENTS_HISTORY_newValue: Property = Property(name="newValue", type=StringType)
EVENTS_HISTORY.attributes={EVENTS_HISTORY_eventId, EVENTS_HISTORY__id, EVENTS_HISTORY_userId, EVENTS_HISTORY_createdAt, EVENTS_HISTORY_newValue, EVENTS_HISTORY_oldValue}

# EVENTS_LIST class attributes and methods
EVENTS_LIST_createdAt: Property = Property(name="createdAt", type=StringType)
EVENTS_LIST_description: Property = Property(name="description", type=StringType)
EVENTS_LIST_key: Property = Property(name="key", type=StringType)
EVENTS_LIST__id: Property = Property(name="_id", type=StringType)
EVENTS_LIST.attributes={EVENTS_LIST_createdAt, EVENTS_LIST_key, EVENTS_LIST_description, EVENTS_LIST__id}

# Class class attributes and methods

# NOTIFICATION class attributes and methods
NOTIFICATION__id: Property = Property(name="_id", type=StringType)
NOTIFICATION_createdAt: Property = Property(name="createdAt", type=StringType)
NOTIFICATION_message: Property = Property(name="message", type=StringType)
NOTIFICATION_code: Property = Property(name="code", type=StringType)
NOTIFICATION_userId: Property = Property(name="userId", type=StringType)
NOTIFICATION.attributes={NOTIFICATION_message, NOTIFICATION_userId, NOTIFICATION_createdAt, NOTIFICATION_code, NOTIFICATION__id}

# REFUND class attributes and methods
REFUND__id: Property = Property(name="_id", type=StringType)
REFUND_created_at: Property = Property(name="created_at", type=StringType)
REFUND_title: Property = Property(name="title", type=StringType)
REFUND_message: Property = Property(name="message", type=StringType)
REFUND_userId: Property = Property(name="userId", type=StringType)
REFUND_productId: Property = Property(name="productId", type=StringType)
REFUND_shoppingHistoryId: Property = Property(name="shoppingHistoryId", type=StringType)
REFUND_storeId: Property = Property(name="storeId", type=StringType)
REFUND.attributes={REFUND_title, REFUND_storeId, REFUND_userId, REFUND__id, REFUND_productId, REFUND_shoppingHistoryId, REFUND_created_at, REFUND_message}

# REFUND_MESSAGES class attributes and methods
REFUND_MESSAGES__id: Property = Property(name="_id", type=StringType)
REFUND_MESSAGES_created_at: Property = Property(name="created_at", type=StringType)
REFUND_MESSAGES_userId: Property = Property(name="userId", type=StringType)
REFUND_MESSAGES_message: Property = Property(name="message", type=StringType)
REFUND_MESSAGES_attach: Property = Property(name="attach", type=StringType)
REFUND_MESSAGES.attributes={REFUND_MESSAGES__id, REFUND_MESSAGES_attach, REFUND_MESSAGES_message, REFUND_MESSAGES_created_at, REFUND_MESSAGES_userId}

# SOCIAL_NETWORKS class attributes and methods
SOCIAL_NETWORKS__id: Property = Property(name="_id", type=StringType)
SOCIAL_NETWORKS_updateAt: Property = Property(name="updateAt", type=StringType)
SOCIAL_NETWORKS_instagram: Property = Property(name="instagram", type=StringType)
SOCIAL_NETWORKS_twitter: Property = Property(name="twitter", type=StringType)
SOCIAL_NETWORKS_facebook: Property = Property(name="facebook", type=StringType)
SOCIAL_NETWORKS.attributes={SOCIAL_NETWORKS_updateAt, SOCIAL_NETWORKS__id, SOCIAL_NETWORKS_facebook, SOCIAL_NETWORKS_instagram, SOCIAL_NETWORKS_twitter}

# FOLLOW class attributes and methods
FOLLOW__id: Property = Property(name="_id", type=StringType)
FOLLOW_createdAt: Property = Property(name="createdAt", type=StringType)
FOLLOW_userId: Property = Property(name="userId", type=StringType)
FOLLOW_following: Property = Property(name="following", type=StringType)
FOLLOW_followers: Property = Property(name="followers", type=StringType)
FOLLOW_followingGroup: Property = Property(name="followingGroup", type=StringType)
FOLLOW.attributes={FOLLOW_createdAt, FOLLOW_followers, FOLLOW_followingGroup, FOLLOW__id, FOLLOW_userId, FOLLOW_following}

# FEEDBACK class attributes and methods
FEEDBACK__id: Property = Property(name="_id", type=StringType)
FEEDBACK_userId: Property = Property(name="userId", type=StringType)
FEEDBACK_productId: Property = Property(name="productId", type=StringType)
FEEDBACK_wysiwyg: Property = Property(name="wysiwyg", type=StringType)
FEEDBACK_photos: Property = Property(name="photos", type=StringType)
FEEDBACK_linkInstagram: Property = Property(name="linkInstagram", type=StringType)
FEEDBACK_linkYoutube: Property = Property(name="linkYoutube", type=StringType)
FEEDBACK_createdAt: Property = Property(name="createdAt", type=StringType)
FEEDBACK_updateAt: Property = Property(name="updateAt", type=StringType)
FEEDBACK_like: Property = Property(name="like", type=StringType)
FEEDBACK.attributes={FEEDBACK_updateAt, FEEDBACK_createdAt, FEEDBACK_linkYoutube, FEEDBACK_photos, FEEDBACK_like, FEEDBACK_wysiwyg, FEEDBACK_linkInstagram, FEEDBACK_productId, FEEDBACK_userId, FEEDBACK__id}

# SHOPPING_MESSENGER class attributes and methods
SHOPPING_MESSENGER__id: Property = Property(name="_id", type=StringType)
SHOPPING_MESSENGER_created_at: Property = Property(name="created_at", type=StringType)
SHOPPING_MESSENGER_userId: Property = Property(name="userId", type=StringType)
SHOPPING_MESSENGER_storeId: Property = Property(name="storeId", type=StringType)
SHOPPING_MESSENGER_message: Property = Property(name="message", type=StringType)
SHOPPING_MESSENGER_photos: Property = Property(name="photos", type=StringType)
SHOPPING_MESSENGER.attributes={SHOPPING_MESSENGER_message, SHOPPING_MESSENGER_userId, SHOPPING_MESSENGER_photos, SHOPPING_MESSENGER__id, SHOPPING_MESSENGER_storeId, SHOPPING_MESSENGER_created_at}

# FEEDBACK_COMMENT class attributes and methods
FEEDBACK_COMMENT_createdAt: Property = Property(name="createdAt", type=StringType)
FEEDBACK_COMMENT_userId: Property = Property(name="userId", type=StringType)
FEEDBACK_COMMENT_feedbackId: Property = Property(name="feedbackId", type=StringType)
FEEDBACK_COMMENT_comment: Property = Property(name="comment", type=StringType)
FEEDBACK_COMMENT_score: Property = Property(name="score", type=IntegerType)
FEEDBACK_COMMENT__id: Property = Property(name="_id", type=StringType)
FEEDBACK_COMMENT.attributes={FEEDBACK_COMMENT_createdAt, FEEDBACK_COMMENT_feedbackId, FEEDBACK_COMMENT_score, FEEDBACK_COMMENT__id, FEEDBACK_COMMENT_comment, FEEDBACK_COMMENT_userId}

# FOLLOW_MESSENGER class attributes and methods
FOLLOW_MESSENGER__id: Property = Property(name="_id", type=StringType)
FOLLOW_MESSENGER_createdAt: Property = Property(name="createdAt", type=StringType)
FOLLOW_MESSENGER_userId: Property = Property(name="userId", type=StringType)
FOLLOW_MESSENGER.attributes={FOLLOW_MESSENGER_userId, FOLLOW_MESSENGER__id, FOLLOW_MESSENGER_createdAt}

# Relationships
roles_usuario: BinaryAssociation = BinaryAssociation(
    name="roles_usuario",
    ends={
        Property(name="usuario0", type=USER, multiplicity=Multiplicity(1, 9999)),
        Property(name="roles1", type=ROLES, multiplicity=Multiplicity(0, 1))
    }
)
PRODUCTO_USUARIO: BinaryAssociation = BinaryAssociation(
    name="PRODUCTO_USUARIO",
    ends={
        Property(name="uSUARIO2", type=USER, multiplicity=Multiplicity(1, 9999)),
        Property(name="pRODUCTO3", type=PRODUCT, multiplicity=Multiplicity(0, 1))
    }
)
CATEGORIAS_PRODUCTO: BinaryAssociation = BinaryAssociation(
    name="CATEGORIAS_PRODUCTO",
    ends={
        Property(name="pRODUCTO4", type=PRODUCT, multiplicity=Multiplicity(1, 9999)),
        Property(name="cATEGORIAS5", type=CATEGORIAS, multiplicity=Multiplicity(0, 1))
    }
)
FAVORITES_PRODUCTO: BinaryAssociation = BinaryAssociation(
    name="FAVORITES_PRODUCTO",
    ends={
        Property(name="pRODUCTO6", type=PRODUCT, multiplicity=Multiplicity(0, 1)),
        Property(name="fAVORITES7", type=WHISES, multiplicity=Multiplicity(1, 9999))
    }
)
FAVORITES_USUARIO: BinaryAssociation = BinaryAssociation(
    name="FAVORITES_USUARIO",
    ends={
        Property(name="uSUARIO8", type=USER, multiplicity=Multiplicity(0, 1)),
        Property(name="fAVORITES9", type=WHISES, multiplicity=Multiplicity(1, 9999))
    }
)
COMMENTS_PRODUCT: BinaryAssociation = BinaryAssociation(
    name="COMMENTS_PRODUCT",
    ends={
        Property(name="pRODUCT10", type=PRODUCT, multiplicity=Multiplicity(0, 1)),
        Property(name="cOMMENTS11", type=QUESTIONS, multiplicity=Multiplicity(0, 1))
    }
)
COMMENTS_USUARIO: BinaryAssociation = BinaryAssociation(
    name="COMMENTS_USUARIO",
    ends={
        Property(name="uSUARIO12", type=USER, multiplicity=Multiplicity(0, 1)),
        Property(name="cOMMENTS13", type=QUESTIONS, multiplicity=Multiplicity(0, 1))
    }
)
SHOPPING_CART_USUARIO: BinaryAssociation = BinaryAssociation(
    name="SHOPPING_CART_USUARIO",
    ends={
        Property(name="uSUARIO14", type=USER, multiplicity=Multiplicity(0, 1)),
        Property(name="sHOPPING_CART15", type=SHOPPING_HISTORY, multiplicity=Multiplicity(0, 1))
    }
)
SHOPPING_CART_PRODUCT: BinaryAssociation = BinaryAssociation(
    name="SHOPPING_CART_PRODUCT",
    ends={
        Property(name="pRODUCT16", type=PRODUCT, multiplicity=Multiplicity(0, 1)),
        Property(name="sHOPPING_CART17", type=SHOPPING_HISTORY, multiplicity=Multiplicity(0, 1))
    }
)
MESSENGER_SHOPPING_HISTORY: BinaryAssociation = BinaryAssociation(
    name="MESSENGER_SHOPPING_HISTORY",
    ends={
        Property(name="sHOPPING_HISTORY48", type=SHOPPING_HISTORY, multiplicity=Multiplicity(0, 1)),
        Property(name="mESSENGER49", type=SHOPPING_MESSENGER, multiplicity=Multiplicity(0, 1))
    }
)
FEEDBACKS_USER: BinaryAssociation = BinaryAssociation(
    name="FEEDBACKS_USER",
    ends={
        Property(name="uSER50", type=USER, multiplicity=Multiplicity(0, 1)),
        Property(name="fEEDBACKS51", type=FEEDBACK, multiplicity=Multiplicity(0, 1))
    }
)
FEEDBACK_COMMENT_FEEDBACK: BinaryAssociation = BinaryAssociation(
    name="FEEDBACK_COMMENT_FEEDBACK",
    ends={
        Property(name="fEEDBACK52", type=FEEDBACK, multiplicity=Multiplicity(0, 1)),
        Property(name="fEEDBACK_COMMENT53", type=FEEDBACK_COMMENT, multiplicity=Multiplicity(0, 1))
    }
)
STATUS_PRODUCT: BinaryAssociation = BinaryAssociation(
    name="STATUS_PRODUCT",
    ends={
        Property(name="pRODUCT18", type=PRODUCT, multiplicity=Multiplicity(0, 1)),
        Property(name="sTATUS19", type=STATUS, multiplicity=Multiplicity(0, 1))
    }
)
SHIPPING_SHOPPING_CART: BinaryAssociation = BinaryAssociation(
    name="SHIPPING_SHOPPING_CART",
    ends={
        Property(name="sHOPPING_CART20", type=SHOPPING_HISTORY, multiplicity=Multiplicity(0, 1)),
        Property(name="sHIPPING21", type=SHIPPING_METHODS, multiplicity=Multiplicity(0, 1))
    }
)
SHIPPING_PRODUCT: BinaryAssociation = BinaryAssociation(
    name="SHIPPING_PRODUCT",
    ends={
        Property(name="pRODUCT22", type=PRODUCT, multiplicity=Multiplicity(0, 1)),
        Property(name="sHIPPING23", type=SHIPPING_METHODS, multiplicity=Multiplicity(0, 1))
    }
)
STATUS_SHOPPING_HISTORY_SHOPPING_HISTORY: BinaryAssociation = BinaryAssociation(
    name="STATUS_SHOPPING_HISTORY_SHOPPING_HISTORY",
    ends={
        Property(name="sHOPPING_HISTORY24", type=SHOPPING_HISTORY, multiplicity=Multiplicity(0, 1)),
        Property(name="sTATUS_SHOPPING_HISTORY25", type=STATUS_SHOPPING_HISTORY, multiplicity=Multiplicity(0, 1))
    }
)
STORE_PRODUCT: BinaryAssociation = BinaryAssociation(
    name="STORE_PRODUCT",
    ends={
        Property(name="pRODUCT26", type=PRODUCT, multiplicity=Multiplicity(0, 1)),
        Property(name="sTORE27", type=STORE, multiplicity=Multiplicity(1, 9999))
    }
)
STORE_USER: BinaryAssociation = BinaryAssociation(
    name="STORE_USER",
    ends={
        Property(name="uSER28", type=USER, multiplicity=Multiplicity(0, 1)),
        Property(name="sTORE29", type=STORE, multiplicity=Multiplicity(0, 1))
    }
)
SHOPPING_HISTORY_STORE: BinaryAssociation = BinaryAssociation(
    name="SHOPPING_HISTORY_STORE",
    ends={
        Property(name="sTORE30", type=STORE, multiplicity=Multiplicity(0, 1)),
        Property(name="sHOPPING_HISTORY31", type=SHOPPING_HISTORY, multiplicity=Multiplicity(0, 1))
    }
)
FAVORITES_STORE: BinaryAssociation = BinaryAssociation(
    name="FAVORITES_STORE",
    ends={
        Property(name="sTORE32", type=STORE, multiplicity=Multiplicity(0, 1)),
        Property(name="fAVORITES33", type=FAVORITES, multiplicity=Multiplicity(0, 1))
    }
)
FAVORITES_USER: BinaryAssociation = BinaryAssociation(
    name="FAVORITES_USER",
    ends={
        Property(name="uSER34", type=USER, multiplicity=Multiplicity(0, 1)),
        Property(name="fAVORITES35", type=FAVORITES, multiplicity=Multiplicity(0, 1))
    }
)
EVENTS_LIST_EVENTS_HISTORY: BinaryAssociation = BinaryAssociation(
    name="EVENTS_LIST_EVENTS_HISTORY",
    ends={
        Property(name="eVENTS_HISTORY36", type=EVENTS_HISTORY, multiplicity=Multiplicity(0, 1)),
        Property(name="eVENTS_LIST37", type=EVENTS_LIST, multiplicity=Multiplicity(0, 1))
    }
)
NOTIFICATION_USER: BinaryAssociation = BinaryAssociation(
    name="NOTIFICATION_USER",
    ends={
        Property(name="uSER38", type=USER, multiplicity=Multiplicity(0, 1)),
        Property(name="nOTIFICATION39", type=NOTIFICATION, multiplicity=Multiplicity(0, 1))
    }
)
REFUND_SHOPPING_HISTORY: BinaryAssociation = BinaryAssociation(
    name="REFUND_SHOPPING_HISTORY",
    ends={
        Property(name="sHOPPING_HISTORY40", type=SHOPPING_HISTORY, multiplicity=Multiplicity(0, 1)),
        Property(name="rEFUND41", type=REFUND, multiplicity=Multiplicity(0, 1))
    }
)
REFUND_MESSAGES_REFUND: BinaryAssociation = BinaryAssociation(
    name="REFUND_MESSAGES_REFUND",
    ends={
        Property(name="rEFUND42", type=REFUND, multiplicity=Multiplicity(0, 1)),
        Property(name="rEFUND_MESSAGES43", type=REFUND_MESSAGES, multiplicity=Multiplicity(0, 1))
    }
)
SOCIAL_NETWORKS_USER: BinaryAssociation = BinaryAssociation(
    name="SOCIAL_NETWORKS_USER",
    ends={
        Property(name="uSER44", type=USER, multiplicity=Multiplicity(0, 1)),
        Property(name="sOCIAL_NETWORKS45", type=SOCIAL_NETWORKS, multiplicity=Multiplicity(0, 1))
    }
)
FRIEND_LIST_USER: BinaryAssociation = BinaryAssociation(
    name="FRIEND_LIST_USER",
    ends={
        Property(name="uSER46", type=USER, multiplicity=Multiplicity(0, 1)),
        Property(name="fRIEND_LIST47", type=FOLLOW, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="f05037b8_77ed_4cc5_82b5_66436717bd01",
    types={USER, ROLES, PRODUCT, CATEGORIAS, WHISES, QUESTIONS, SHOPPING_HISTORY, STATUS, SHIPPING_METHODS, SUBSCRIPTION_BENEFITS, STATUS2, STATUS_SHOPPING_HISTORY, STORE, FAVORITES, EVENTS_HISTORY, EVENTS_LIST, Class_, NOTIFICATION, REFUND, REFUND_MESSAGES, SOCIAL_NETWORKS, FOLLOW, FEEDBACK, SHOPPING_MESSENGER, FEEDBACK_COMMENT, FOLLOW_MESSENGER},
    associations={roles_usuario, PRODUCTO_USUARIO, CATEGORIAS_PRODUCTO, FAVORITES_PRODUCTO, FAVORITES_USUARIO, COMMENTS_PRODUCT, COMMENTS_USUARIO, SHOPPING_CART_USUARIO, SHOPPING_CART_PRODUCT, MESSENGER_SHOPPING_HISTORY, FEEDBACKS_USER, FEEDBACK_COMMENT_FEEDBACK, STATUS_PRODUCT, SHIPPING_SHOPPING_CART, SHIPPING_PRODUCT, STATUS_SHOPPING_HISTORY_SHOPPING_HISTORY, STORE_PRODUCT, STORE_USER, SHOPPING_HISTORY_STORE, FAVORITES_STORE, FAVORITES_USER, EVENTS_LIST_EVENTS_HISTORY, NOTIFICATION_USER, REFUND_SHOPPING_HISTORY, REFUND_MESSAGES_REFUND, SOCIAL_NETWORKS_USER, FRIEND_LIST_USER},
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