from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class FOLLOW_MESSENGER:

    def __init__(self, _id: str, createdAt: str, userId: str):
        self._id = _id
        self.createdAt = createdAt
        self.userId = userId
        
        pass
    @property
    def createdAt(self):
        return self.__createdAt
    @createdAt.setter
    def createdAt(self, createdAt: str):
        self.__createdAt = createdAt

    @property
    def userId(self):
        return self.__userId
    @userId.setter
    def userId(self, userId: str):
        self.__userId = userId

    @property
    def _id(self):
        return self.___id
    @_id.setter
    def _id(self, _id: str):
        self.___id = _id



class FEEDBACK_COMMENT:

    def __init__(self, createdAt: str, userId: str, feedbackId: str, comment: str, score: int, _id: str, fEEDBACK52: "FEEDBACK" = None):
        self.createdAt = createdAt
        self.userId = userId
        self.feedbackId = feedbackId
        self.comment = comment
        self.score = score
        self._id = _id
        self.fEEDBACK52 = fEEDBACK52
        
        pass
    @property
    def userId(self):
        return self.__userId
    @userId.setter
    def userId(self, userId: str):
        self.__userId = userId

    @property
    def comment(self):
        return self.__comment
    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def createdAt(self):
        return self.__createdAt
    @createdAt.setter
    def createdAt(self, createdAt: str):
        self.__createdAt = createdAt

    @property
    def score(self):
        return self.__score
    @score.setter
    def score(self, score: int):
        self.__score = score

    @property
    def feedbackId(self):
        return self.__feedbackId
    @feedbackId.setter
    def feedbackId(self, feedbackId: str):
        self.__feedbackId = feedbackId

    @property
    def _id(self):
        return self.___id
    @_id.setter
    def _id(self, _id: str):
        self.___id = _id

    @property
    def fEEDBACK52(self):
        return self.__fEEDBACK52
    @fEEDBACK52.setter
    def fEEDBACK52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FEEDBACK_COMMENT__fEEDBACK52", None)
        self.__fEEDBACK52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fEEDBACK_COMMENT53"):
                opp_val = getattr(old_value, "fEEDBACK_COMMENT53", None)
                if opp_val == self:
                    setattr(old_value, "fEEDBACK_COMMENT53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fEEDBACK_COMMENT53"):
                opp_val = getattr(value, "fEEDBACK_COMMENT53", None)
                setattr(value, "fEEDBACK_COMMENT53", self)



class SHOPPING_MESSENGER:

    def __init__(self, _id: str, created_at: str, userId: str, storeId: str, message: str, photos: str, sHOPPING_HISTORY48: "SHOPPING_HISTORY" = None):
        self._id = _id
        self.created_at = created_at
        self.userId = userId
        self.storeId = storeId
        self.message = message
        self.photos = photos
        self.sHOPPING_HISTORY48 = sHOPPING_HISTORY48
        
        pass
    @property
    def photos(self):
        return self.__photos
    @photos.setter
    def photos(self, photos: str):
        self.__photos = photos

    @property
    def _id(self):
        return self.___id
    @_id.setter
    def _id(self, _id: str):
        self.___id = _id

    @property
    def message(self):
        return self.__message
    @message.setter
    def message(self, message: str):
        self.__message = message

    @property
    def storeId(self):
        return self.__storeId
    @storeId.setter
    def storeId(self, storeId: str):
        self.__storeId = storeId

    @property
    def created_at(self):
        return self.__created_at
    @created_at.setter
    def created_at(self, created_at: str):
        self.__created_at = created_at

    @property
    def userId(self):
        return self.__userId
    @userId.setter
    def userId(self, userId: str):
        self.__userId = userId

    @property
    def sHOPPING_HISTORY48(self):
        return self.__sHOPPING_HISTORY48
    @sHOPPING_HISTORY48.setter
    def sHOPPING_HISTORY48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SHOPPING_MESSENGER__sHOPPING_HISTORY48", None)
        self.__sHOPPING_HISTORY48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mESSENGER49"):
                opp_val = getattr(old_value, "mESSENGER49", None)
                if opp_val == self:
                    setattr(old_value, "mESSENGER49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mESSENGER49"):
                opp_val = getattr(value, "mESSENGER49", None)
                setattr(value, "mESSENGER49", self)



class FEEDBACK:

    def __init__(self, _id: str, userId: str, productId: str, wysiwyg: str, photos: str, linkInstagram: str, linkYoutube: str, createdAt: str, updateAt: str, like: str, uSER50: "USER" = None, fEEDBACK_COMMENT53: "FEEDBACK_COMMENT" = None):
        self._id = _id
        self.userId = userId
        self.productId = productId
        self.wysiwyg = wysiwyg
        self.photos = photos
        self.linkInstagram = linkInstagram
        self.linkYoutube = linkYoutube
        self.createdAt = createdAt
        self.updateAt = updateAt
        self.like = like
        self.uSER50 = uSER50
        self.fEEDBACK_COMMENT53 = fEEDBACK_COMMENT53
        
        pass
    @property
    def wysiwyg(self):
        return self.__wysiwyg
    @wysiwyg.setter
    def wysiwyg(self, wysiwyg: str):
        self.__wysiwyg = wysiwyg

    @property
    def linkYoutube(self):
        return self.__linkYoutube
    @linkYoutube.setter
    def linkYoutube(self, linkYoutube: str):
        self.__linkYoutube = linkYoutube

    @property
    def userId(self):
        return self.__userId
    @userId.setter
    def userId(self, userId: str):
        self.__userId = userId

    @property
    def updateAt(self):
        return self.__updateAt
    @updateAt.setter
    def updateAt(self, updateAt: str):
        self.__updateAt = updateAt

    @property
    def like(self):
        return self.__like
    @like.setter
    def like(self, like: str):
        self.__like = like

    @property
    def _id(self):
        return self.___id
    @_id.setter
    def _id(self, _id: str):
        self.___id = _id

    @property
    def linkInstagram(self):
        return self.__linkInstagram
    @linkInstagram.setter
    def linkInstagram(self, linkInstagram: str):
        self.__linkInstagram = linkInstagram

    @property
    def photos(self):
        return self.__photos
    @photos.setter
    def photos(self, photos: str):
        self.__photos = photos

    @property
    def createdAt(self):
        return self.__createdAt
    @createdAt.setter
    def createdAt(self, createdAt: str):
        self.__createdAt = createdAt

    @property
    def productId(self):
        return self.__productId
    @productId.setter
    def productId(self, productId: str):
        self.__productId = productId

    @property
    def uSER50(self):
        return self.__uSER50
    @uSER50.setter
    def uSER50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FEEDBACK__uSER50", None)
        self.__uSER50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fEEDBACKS51"):
                opp_val = getattr(old_value, "fEEDBACKS51", None)
                if opp_val == self:
                    setattr(old_value, "fEEDBACKS51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fEEDBACKS51"):
                opp_val = getattr(value, "fEEDBACKS51", None)
                setattr(value, "fEEDBACKS51", self)

    @property
    def fEEDBACK_COMMENT53(self):
        return self.__fEEDBACK_COMMENT53
    @fEEDBACK_COMMENT53.setter
    def fEEDBACK_COMMENT53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FEEDBACK__fEEDBACK_COMMENT53", None)
        self.__fEEDBACK_COMMENT53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fEEDBACK52"):
                opp_val = getattr(old_value, "fEEDBACK52", None)
                if opp_val == self:
                    setattr(old_value, "fEEDBACK52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fEEDBACK52"):
                opp_val = getattr(value, "fEEDBACK52", None)
                setattr(value, "fEEDBACK52", self)



class FOLLOW:

    def __init__(self, _id: str, createdAt: str, userId: str, following: str, followers: str, followingGroup: str, uSER46: "USER" = None):
        self._id = _id
        self.createdAt = createdAt
        self.userId = userId
        self.following = following
        self.followers = followers
        self.followingGroup = followingGroup
        self.uSER46 = uSER46
        
        pass
    @property
    def followingGroup(self):
        return self.__followingGroup
    @followingGroup.setter
    def followingGroup(self, followingGroup: str):
        self.__followingGroup = followingGroup

    @property
    def _id(self):
        return self.___id
    @_id.setter
    def _id(self, _id: str):
        self.___id = _id

    @property
    def following(self):
        return self.__following
    @following.setter
    def following(self, following: str):
        self.__following = following

    @property
    def createdAt(self):
        return self.__createdAt
    @createdAt.setter
    def createdAt(self, createdAt: str):
        self.__createdAt = createdAt

    @property
    def followers(self):
        return self.__followers
    @followers.setter
    def followers(self, followers: str):
        self.__followers = followers

    @property
    def userId(self):
        return self.__userId
    @userId.setter
    def userId(self, userId: str):
        self.__userId = userId

    @property
    def uSER46(self):
        return self.__uSER46
    @uSER46.setter
    def uSER46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FOLLOW__uSER46", None)
        self.__uSER46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fRIEND_LIST47"):
                opp_val = getattr(old_value, "fRIEND_LIST47", None)
                if opp_val == self:
                    setattr(old_value, "fRIEND_LIST47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fRIEND_LIST47"):
                opp_val = getattr(value, "fRIEND_LIST47", None)
                setattr(value, "fRIEND_LIST47", self)



class SOCIAL_NETWORKS:

    def __init__(self, _id: str, updateAt: str, instagram: str, twitter: str, facebook: str, uSER44: "USER" = None):
        self._id = _id
        self.updateAt = updateAt
        self.instagram = instagram
        self.twitter = twitter
        self.facebook = facebook
        self.uSER44 = uSER44
        
        pass
    @property
    def _id(self):
        return self.___id
    @_id.setter
    def _id(self, _id: str):
        self.___id = _id

    @property
    def twitter(self):
        return self.__twitter
    @twitter.setter
    def twitter(self, twitter: str):
        self.__twitter = twitter

    @property
    def facebook(self):
        return self.__facebook
    @facebook.setter
    def facebook(self, facebook: str):
        self.__facebook = facebook

    @property
    def updateAt(self):
        return self.__updateAt
    @updateAt.setter
    def updateAt(self, updateAt: str):
        self.__updateAt = updateAt

    @property
    def instagram(self):
        return self.__instagram
    @instagram.setter
    def instagram(self, instagram: str):
        self.__instagram = instagram

    @property
    def uSER44(self):
        return self.__uSER44
    @uSER44.setter
    def uSER44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SOCIAL_NETWORKS__uSER44", None)
        self.__uSER44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sOCIAL_NETWORKS45"):
                opp_val = getattr(old_value, "sOCIAL_NETWORKS45", None)
                if opp_val == self:
                    setattr(old_value, "sOCIAL_NETWORKS45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sOCIAL_NETWORKS45"):
                opp_val = getattr(value, "sOCIAL_NETWORKS45", None)
                setattr(value, "sOCIAL_NETWORKS45", self)



class REFUND_MESSAGES:

    def __init__(self, _id: str, created_at: str, userId: str, message: str, attach: str, rEFUND42: "REFUND" = None):
        self._id = _id
        self.created_at = created_at
        self.userId = userId
        self.message = message
        self.attach = attach
        self.rEFUND42 = rEFUND42
        
        pass
    @property
    def created_at(self):
        return self.__created_at
    @created_at.setter
    def created_at(self, created_at: str):
        self.__created_at = created_at

    @property
    def message(self):
        return self.__message
    @message.setter
    def message(self, message: str):
        self.__message = message

    @property
    def _id(self):
        return self.___id
    @_id.setter
    def _id(self, _id: str):
        self.___id = _id

    @property
    def attach(self):
        return self.__attach
    @attach.setter
    def attach(self, attach: str):
        self.__attach = attach

    @property
    def userId(self):
        return self.__userId
    @userId.setter
    def userId(self, userId: str):
        self.__userId = userId

    @property
    def rEFUND42(self):
        return self.__rEFUND42
    @rEFUND42.setter
    def rEFUND42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_REFUND_MESSAGES__rEFUND42", None)
        self.__rEFUND42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rEFUND_MESSAGES43"):
                opp_val = getattr(old_value, "rEFUND_MESSAGES43", None)
                if opp_val == self:
                    setattr(old_value, "rEFUND_MESSAGES43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rEFUND_MESSAGES43"):
                opp_val = getattr(value, "rEFUND_MESSAGES43", None)
                setattr(value, "rEFUND_MESSAGES43", self)



class REFUND:

    def __init__(self, _id: str, created_at: str, title: str, message: str, userId: str, productId: str, shoppingHistoryId: str, storeId: str, sHOPPING_HISTORY40: "SHOPPING_HISTORY" = None, rEFUND_MESSAGES43: "REFUND_MESSAGES" = None):
        self._id = _id
        self.created_at = created_at
        self.title = title
        self.message = message
        self.userId = userId
        self.productId = productId
        self.shoppingHistoryId = shoppingHistoryId
        self.storeId = storeId
        self.sHOPPING_HISTORY40 = sHOPPING_HISTORY40
        self.rEFUND_MESSAGES43 = rEFUND_MESSAGES43
        
        pass
    @property
    def message(self):
        return self.__message
    @message.setter
    def message(self, message: str):
        self.__message = message

    @property
    def storeId(self):
        return self.__storeId
    @storeId.setter
    def storeId(self, storeId: str):
        self.__storeId = storeId

    @property
    def _id(self):
        return self.___id
    @_id.setter
    def _id(self, _id: str):
        self.___id = _id

    @property
    def title(self):
        return self.__title
    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def userId(self):
        return self.__userId
    @userId.setter
    def userId(self, userId: str):
        self.__userId = userId

    @property
    def productId(self):
        return self.__productId
    @productId.setter
    def productId(self, productId: str):
        self.__productId = productId

    @property
    def created_at(self):
        return self.__created_at
    @created_at.setter
    def created_at(self, created_at: str):
        self.__created_at = created_at

    @property
    def shoppingHistoryId(self):
        return self.__shoppingHistoryId
    @shoppingHistoryId.setter
    def shoppingHistoryId(self, shoppingHistoryId: str):
        self.__shoppingHistoryId = shoppingHistoryId

    @property
    def rEFUND_MESSAGES43(self):
        return self.__rEFUND_MESSAGES43
    @rEFUND_MESSAGES43.setter
    def rEFUND_MESSAGES43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_REFUND__rEFUND_MESSAGES43", None)
        self.__rEFUND_MESSAGES43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rEFUND42"):
                opp_val = getattr(old_value, "rEFUND42", None)
                if opp_val == self:
                    setattr(old_value, "rEFUND42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rEFUND42"):
                opp_val = getattr(value, "rEFUND42", None)
                setattr(value, "rEFUND42", self)

    @property
    def sHOPPING_HISTORY40(self):
        return self.__sHOPPING_HISTORY40
    @sHOPPING_HISTORY40.setter
    def sHOPPING_HISTORY40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_REFUND__sHOPPING_HISTORY40", None)
        self.__sHOPPING_HISTORY40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rEFUND41"):
                opp_val = getattr(old_value, "rEFUND41", None)
                if opp_val == self:
                    setattr(old_value, "rEFUND41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rEFUND41"):
                opp_val = getattr(value, "rEFUND41", None)
                setattr(value, "rEFUND41", self)



class NOTIFICATION:

    def __init__(self, _id: str, createdAt: str, message: str, code: str, userId: str, uSER38: "USER" = None):
        self._id = _id
        self.createdAt = createdAt
        self.message = message
        self.code = code
        self.userId = userId
        self.uSER38 = uSER38
        
        pass
    @property
    def createdAt(self):
        return self.__createdAt
    @createdAt.setter
    def createdAt(self, createdAt: str):
        self.__createdAt = createdAt

    @property
    def message(self):
        return self.__message
    @message.setter
    def message(self, message: str):
        self.__message = message

    @property
    def code(self):
        return self.__code
    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def userId(self):
        return self.__userId
    @userId.setter
    def userId(self, userId: str):
        self.__userId = userId

    @property
    def _id(self):
        return self.___id
    @_id.setter
    def _id(self, _id: str):
        self.___id = _id

    @property
    def uSER38(self):
        return self.__uSER38
    @uSER38.setter
    def uSER38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NOTIFICATION__uSER38", None)
        self.__uSER38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nOTIFICATION39"):
                opp_val = getattr(old_value, "nOTIFICATION39", None)
                if opp_val == self:
                    setattr(old_value, "nOTIFICATION39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nOTIFICATION39"):
                opp_val = getattr(value, "nOTIFICATION39", None)
                setattr(value, "nOTIFICATION39", self)



class Class:

    pass


class EVENTS_LIST:

    def __init__(self, createdAt: str, description: str, key: str, _id: str, eVENTS_HISTORY36: "EVENTS_HISTORY" = None):
        self.createdAt = createdAt
        self.description = description
        self.key = key
        self._id = _id
        self.eVENTS_HISTORY36 = eVENTS_HISTORY36
        
        pass
    @property
    def _id(self):
        return self.___id
    @_id.setter
    def _id(self, _id: str):
        self.___id = _id

    @property
    def description(self):
        return self.__description
    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def createdAt(self):
        return self.__createdAt
    @createdAt.setter
    def createdAt(self, createdAt: str):
        self.__createdAt = createdAt

    @property
    def key(self):
        return self.__key
    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def eVENTS_HISTORY36(self):
        return self.__eVENTS_HISTORY36
    @eVENTS_HISTORY36.setter
    def eVENTS_HISTORY36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EVENTS_LIST__eVENTS_HISTORY36", None)
        self.__eVENTS_HISTORY36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eVENTS_LIST37"):
                opp_val = getattr(old_value, "eVENTS_LIST37", None)
                if opp_val == self:
                    setattr(old_value, "eVENTS_LIST37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eVENTS_LIST37"):
                opp_val = getattr(value, "eVENTS_LIST37", None)
                setattr(value, "eVENTS_LIST37", self)



class EVENTS_HISTORY:

    def __init__(self, _id: str, createdAt: str, userId: str, eventId: str, oldValue: str, newValue: str, eVENTS_LIST37: "EVENTS_LIST" = None):
        self._id = _id
        self.createdAt = createdAt
        self.userId = userId
        self.eventId = eventId
        self.oldValue = oldValue
        self.newValue = newValue
        self.eVENTS_LIST37 = eVENTS_LIST37
        
        pass
    @property
    def userId(self):
        return self.__userId
    @userId.setter
    def userId(self, userId: str):
        self.__userId = userId

    @property
    def oldValue(self):
        return self.__oldValue
    @oldValue.setter
    def oldValue(self, oldValue: str):
        self.__oldValue = oldValue

    @property
    def eventId(self):
        return self.__eventId
    @eventId.setter
    def eventId(self, eventId: str):
        self.__eventId = eventId

    @property
    def newValue(self):
        return self.__newValue
    @newValue.setter
    def newValue(self, newValue: str):
        self.__newValue = newValue

    @property
    def createdAt(self):
        return self.__createdAt
    @createdAt.setter
    def createdAt(self, createdAt: str):
        self.__createdAt = createdAt

    @property
    def _id(self):
        return self.___id
    @_id.setter
    def _id(self, _id: str):
        self.___id = _id

    @property
    def eVENTS_LIST37(self):
        return self.__eVENTS_LIST37
    @eVENTS_LIST37.setter
    def eVENTS_LIST37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EVENTS_HISTORY__eVENTS_LIST37", None)
        self.__eVENTS_LIST37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eVENTS_HISTORY36"):
                opp_val = getattr(old_value, "eVENTS_HISTORY36", None)
                if opp_val == self:
                    setattr(old_value, "eVENTS_HISTORY36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eVENTS_HISTORY36"):
                opp_val = getattr(value, "eVENTS_HISTORY36", None)
                setattr(value, "eVENTS_HISTORY36", self)



class FAVORITES:

    def __init__(self, _id: str, createdAt: str, statusId: str, userId: str, storeId: str, sTORE32: "STORE" = None, uSER34: "USER" = None):
        self._id = _id
        self.createdAt = createdAt
        self.statusId = statusId
        self.userId = userId
        self.storeId = storeId
        self.sTORE32 = sTORE32
        self.uSER34 = uSER34
        
        pass
    @property
    def userId(self):
        return self.__userId
    @userId.setter
    def userId(self, userId: str):
        self.__userId = userId

    @property
    def storeId(self):
        return self.__storeId
    @storeId.setter
    def storeId(self, storeId: str):
        self.__storeId = storeId

    @property
    def _id(self):
        return self.___id
    @_id.setter
    def _id(self, _id: str):
        self.___id = _id

    @property
    def statusId(self):
        return self.__statusId
    @statusId.setter
    def statusId(self, statusId: str):
        self.__statusId = statusId

    @property
    def createdAt(self):
        return self.__createdAt
    @createdAt.setter
    def createdAt(self, createdAt: str):
        self.__createdAt = createdAt

    @property
    def sTORE32(self):
        return self.__sTORE32
    @sTORE32.setter
    def sTORE32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FAVORITES__sTORE32", None)
        self.__sTORE32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fAVORITES33"):
                opp_val = getattr(old_value, "fAVORITES33", None)
                if opp_val == self:
                    setattr(old_value, "fAVORITES33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fAVORITES33"):
                opp_val = getattr(value, "fAVORITES33", None)
                setattr(value, "fAVORITES33", self)

    @property
    def uSER34(self):
        return self.__uSER34
    @uSER34.setter
    def uSER34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FAVORITES__uSER34", None)
        self.__uSER34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fAVORITES35"):
                opp_val = getattr(old_value, "fAVORITES35", None)
                if opp_val == self:
                    setattr(old_value, "fAVORITES35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fAVORITES35"):
                opp_val = getattr(value, "fAVORITES35", None)
                setattr(value, "fAVORITES35", self)



class STORE:

    def __init__(self, _id: str, createdAt: str, updateAt: str, statusId: str, email: str, address: str, telephone: str, name: str, schedule: str, pRODUCT26: "PRODUCT" = None, uSER28: "USER" = None, sHOPPING_HISTORY31: "SHOPPING_HISTORY" = None, fAVORITES33: "FAVORITES" = None):
        self._id = _id
        self.createdAt = createdAt
        self.updateAt = updateAt
        self.statusId = statusId
        self.email = email
        self.address = address
        self.telephone = telephone
        self.name = name
        self.schedule = schedule
        self.pRODUCT26 = pRODUCT26
        self.uSER28 = uSER28
        self.sHOPPING_HISTORY31 = sHOPPING_HISTORY31
        self.fAVORITES33 = fAVORITES33
        
        pass
    @property
    def telephone(self):
        return self.__telephone
    @telephone.setter
    def telephone(self, telephone: str):
        self.__telephone = telephone

    @property
    def statusId(self):
        return self.__statusId
    @statusId.setter
    def statusId(self, statusId: str):
        self.__statusId = statusId

    @property
    def _id(self):
        return self.___id
    @_id.setter
    def _id(self, _id: str):
        self.___id = _id

    @property
    def schedule(self):
        return self.__schedule
    @schedule.setter
    def schedule(self, schedule: str):
        self.__schedule = schedule

    @property
    def createdAt(self):
        return self.__createdAt
    @createdAt.setter
    def createdAt(self, createdAt: str):
        self.__createdAt = createdAt

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def updateAt(self):
        return self.__updateAt
    @updateAt.setter
    def updateAt(self, updateAt: str):
        self.__updateAt = updateAt

    @property
    def uSER28(self):
        return self.__uSER28
    @uSER28.setter
    def uSER28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_STORE__uSER28", None)
        self.__uSER28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sTORE29"):
                opp_val = getattr(old_value, "sTORE29", None)
                if opp_val == self:
                    setattr(old_value, "sTORE29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sTORE29"):
                opp_val = getattr(value, "sTORE29", None)
                setattr(value, "sTORE29", self)

    @property
    def pRODUCT26(self):
        return self.__pRODUCT26
    @pRODUCT26.setter
    def pRODUCT26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_STORE__pRODUCT26", None)
        self.__pRODUCT26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sTORE27"):
                opp_val = getattr(old_value, "sTORE27", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sTORE27"):
                opp_val = getattr(value, "sTORE27", None)
                if opp_val is None:
                    setattr(value, "sTORE27", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fAVORITES33(self):
        return self.__fAVORITES33
    @fAVORITES33.setter
    def fAVORITES33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_STORE__fAVORITES33", None)
        self.__fAVORITES33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sTORE32"):
                opp_val = getattr(old_value, "sTORE32", None)
                if opp_val == self:
                    setattr(old_value, "sTORE32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sTORE32"):
                opp_val = getattr(value, "sTORE32", None)
                setattr(value, "sTORE32", self)

    @property
    def sHOPPING_HISTORY31(self):
        return self.__sHOPPING_HISTORY31
    @sHOPPING_HISTORY31.setter
    def sHOPPING_HISTORY31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_STORE__sHOPPING_HISTORY31", None)
        self.__sHOPPING_HISTORY31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sTORE30"):
                opp_val = getattr(old_value, "sTORE30", None)
                if opp_val == self:
                    setattr(old_value, "sTORE30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sTORE30"):
                opp_val = getattr(value, "sTORE30", None)
                setattr(value, "sTORE30", self)



class STATUS_SHOPPING_HISTORY:

    def __init__(self, _id: str, name: str, sHOPPING_HISTORY24: "SHOPPING_HISTORY" = None):
        self._id = _id
        self.name = name
        self.sHOPPING_HISTORY24 = sHOPPING_HISTORY24
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def _id(self):
        return self.___id
    @_id.setter
    def _id(self, _id: str):
        self.___id = _id

    @property
    def sHOPPING_HISTORY24(self):
        return self.__sHOPPING_HISTORY24
    @sHOPPING_HISTORY24.setter
    def sHOPPING_HISTORY24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_STATUS_SHOPPING_HISTORY__sHOPPING_HISTORY24", None)
        self.__sHOPPING_HISTORY24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sTATUS_SHOPPING_HISTORY25"):
                opp_val = getattr(old_value, "sTATUS_SHOPPING_HISTORY25", None)
                if opp_val == self:
                    setattr(old_value, "sTATUS_SHOPPING_HISTORY25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sTATUS_SHOPPING_HISTORY25"):
                opp_val = getattr(value, "sTATUS_SHOPPING_HISTORY25", None)
                setattr(value, "sTATUS_SHOPPING_HISTORY25", self)



class STATUS2:

    def __init__(self, _id: str, name: str):
        self._id = _id
        self.name = name
        
        pass
    @property
    def _id(self):
        return self.___id
    @_id.setter
    def _id(self, _id: str):
        self.___id = _id

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name



class SUBSCRIPTION_BENEFITS:

    def __init__(self, _id: str, key_name: str, description: str):
        self._id = _id
        self.key_name = key_name
        self.description = description
        
        pass
    @property
    def description(self):
        return self.__description
    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def key_name(self):
        return self.__key_name
    @key_name.setter
    def key_name(self, key_name: str):
        self.__key_name = key_name

    @property
    def _id(self):
        return self.___id
    @_id.setter
    def _id(self, _id: str):
        self.___id = _id



class SHIPPING_METHODS:

    def __init__(self, _id: str, createdAt: str, name: str, arrival: str, address: str, price: int, sHOPPING_CART20: "SHOPPING_HISTORY" = None, pRODUCT22: "PRODUCT" = None):
        self._id = _id
        self.createdAt = createdAt
        self.name = name
        self.arrival = arrival
        self.address = address
        self.price = price
        self.sHOPPING_CART20 = sHOPPING_CART20
        self.pRODUCT22 = pRODUCT22
        
        pass
    @property
    def arrival(self):
        return self.__arrival
    @arrival.setter
    def arrival(self, arrival: str):
        self.__arrival = arrival

    @property
    def _id(self):
        return self.___id
    @_id.setter
    def _id(self, _id: str):
        self.___id = _id

    @property
    def createdAt(self):
        return self.__createdAt
    @createdAt.setter
    def createdAt(self, createdAt: str):
        self.__createdAt = createdAt

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, price: int):
        self.__price = price

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def pRODUCT22(self):
        return self.__pRODUCT22
    @pRODUCT22.setter
    def pRODUCT22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SHIPPING_METHODS__pRODUCT22", None)
        self.__pRODUCT22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sHIPPING23"):
                opp_val = getattr(old_value, "sHIPPING23", None)
                if opp_val == self:
                    setattr(old_value, "sHIPPING23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sHIPPING23"):
                opp_val = getattr(value, "sHIPPING23", None)
                setattr(value, "sHIPPING23", self)

    @property
    def sHOPPING_CART20(self):
        return self.__sHOPPING_CART20
    @sHOPPING_CART20.setter
    def sHOPPING_CART20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SHIPPING_METHODS__sHOPPING_CART20", None)
        self.__sHOPPING_CART20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sHIPPING21"):
                opp_val = getattr(old_value, "sHIPPING21", None)
                if opp_val == self:
                    setattr(old_value, "sHIPPING21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sHIPPING21"):
                opp_val = getattr(value, "sHIPPING21", None)
                setattr(value, "sHIPPING21", self)



class STATUS:

    def __init__(self, _id: str, createdAt: str, name: str, pRODUCT18: "PRODUCT" = None):
        self._id = _id
        self.createdAt = createdAt
        self.name = name
        self.pRODUCT18 = pRODUCT18
        
        pass
    @property
    def _id(self):
        return self.___id
    @_id.setter
    def _id(self, _id: str):
        self.___id = _id

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def createdAt(self):
        return self.__createdAt
    @createdAt.setter
    def createdAt(self, createdAt: str):
        self.__createdAt = createdAt

    @property
    def pRODUCT18(self):
        return self.__pRODUCT18
    @pRODUCT18.setter
    def pRODUCT18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_STATUS__pRODUCT18", None)
        self.__pRODUCT18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sTATUS19"):
                opp_val = getattr(old_value, "sTATUS19", None)
                if opp_val == self:
                    setattr(old_value, "sTATUS19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sTATUS19"):
                opp_val = getattr(value, "sTATUS19", None)
                setattr(value, "sTATUS19", self)



class SHOPPING_HISTORY:

    def __init__(self, _id: str, created_at: str, status: str, userId: str, storeId: str, productId: str, name: str, price: int, isNew: bool, photos: str, description: str, quantity: int, sold: int, isSold: bool, attribute: str, STATUS_SHOPPING_HIST_ID: str, shipArrival: str, shipName: str, shipAddress: str, shipPrice: int, score: int, comment: str, note: str, uSUARIO14: "USER" = None, pRODUCT16: "PRODUCT" = None, mESSENGER49: "SHOPPING_MESSENGER" = None, sHIPPING21: "SHIPPING_METHODS" = None, sTATUS_SHOPPING_HISTORY25: "STATUS_SHOPPING_HISTORY" = None, sTORE30: "STORE" = None, rEFUND41: "REFUND" = None):
        self._id = _id
        self.created_at = created_at
        self.status = status
        self.userId = userId
        self.storeId = storeId
        self.productId = productId
        self.name = name
        self.price = price
        self.isNew = isNew
        self.photos = photos
        self.description = description
        self.quantity = quantity
        self.sold = sold
        self.isSold = isSold
        self.attribute = attribute
        self.STATUS_SHOPPING_HIST_ID = STATUS_SHOPPING_HIST_ID
        self.shipArrival = shipArrival
        self.shipName = shipName
        self.shipAddress = shipAddress
        self.shipPrice = shipPrice
        self.score = score
        self.comment = comment
        self.note = note
        self.uSUARIO14 = uSUARIO14
        self.pRODUCT16 = pRODUCT16
        self.mESSENGER49 = mESSENGER49
        self.sHIPPING21 = sHIPPING21
        self.sTATUS_SHOPPING_HISTORY25 = sTATUS_SHOPPING_HISTORY25
        self.sTORE30 = sTORE30
        self.rEFUND41 = rEFUND41
        
        pass
    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def userId(self):
        return self.__userId
    @userId.setter
    def userId(self, userId: str):
        self.__userId = userId

    @property
    def productId(self):
        return self.__productId
    @productId.setter
    def productId(self, productId: str):
        self.__productId = productId

    @property
    def description(self):
        return self.__description
    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def storeId(self):
        return self.__storeId
    @storeId.setter
    def storeId(self, storeId: str):
        self.__storeId = storeId

    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, price: int):
        self.__price = price

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def comment(self):
        return self.__comment
    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def quantity(self):
        return self.__quantity
    @quantity.setter
    def quantity(self, quantity: int):
        self.__quantity = quantity

    @property
    def _id(self):
        return self.___id
    @_id.setter
    def _id(self, _id: str):
        self.___id = _id

    @property
    def STATUS_SHOPPING_HIST_ID(self):
        return self.__STATUS_SHOPPING_HIST_ID
    @STATUS_SHOPPING_HIST_ID.setter
    def STATUS_SHOPPING_HIST_ID(self, STATUS_SHOPPING_HIST_ID: str):
        self.__STATUS_SHOPPING_HIST_ID = STATUS_SHOPPING_HIST_ID

    @property
    def isSold(self):
        return self.__isSold
    @isSold.setter
    def isSold(self, isSold: bool):
        self.__isSold = isSold

    @property
    def score(self):
        return self.__score
    @score.setter
    def score(self, score: int):
        self.__score = score

    @property
    def shipArrival(self):
        return self.__shipArrival
    @shipArrival.setter
    def shipArrival(self, shipArrival: str):
        self.__shipArrival = shipArrival

    @property
    def photos(self):
        return self.__photos
    @photos.setter
    def photos(self, photos: str):
        self.__photos = photos

    @property
    def sold(self):
        return self.__sold
    @sold.setter
    def sold(self, sold: int):
        self.__sold = sold

    @property
    def isNew(self):
        return self.__isNew
    @isNew.setter
    def isNew(self, isNew: bool):
        self.__isNew = isNew

    @property
    def shipAddress(self):
        return self.__shipAddress
    @shipAddress.setter
    def shipAddress(self, shipAddress: str):
        self.__shipAddress = shipAddress

    @property
    def shipName(self):
        return self.__shipName
    @shipName.setter
    def shipName(self, shipName: str):
        self.__shipName = shipName

    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self, status: str):
        self.__status = status

    @property
    def created_at(self):
        return self.__created_at
    @created_at.setter
    def created_at(self, created_at: str):
        self.__created_at = created_at

    @property
    def shipPrice(self):
        return self.__shipPrice
    @shipPrice.setter
    def shipPrice(self, shipPrice: int):
        self.__shipPrice = shipPrice

    @property
    def note(self):
        return self.__note
    @note.setter
    def note(self, note: str):
        self.__note = note

    @property
    def sHIPPING21(self):
        return self.__sHIPPING21
    @sHIPPING21.setter
    def sHIPPING21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SHOPPING_HISTORY__sHIPPING21", None)
        self.__sHIPPING21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sHOPPING_CART20"):
                opp_val = getattr(old_value, "sHOPPING_CART20", None)
                if opp_val == self:
                    setattr(old_value, "sHOPPING_CART20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sHOPPING_CART20"):
                opp_val = getattr(value, "sHOPPING_CART20", None)
                setattr(value, "sHOPPING_CART20", self)

    @property
    def rEFUND41(self):
        return self.__rEFUND41
    @rEFUND41.setter
    def rEFUND41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SHOPPING_HISTORY__rEFUND41", None)
        self.__rEFUND41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sHOPPING_HISTORY40"):
                opp_val = getattr(old_value, "sHOPPING_HISTORY40", None)
                if opp_val == self:
                    setattr(old_value, "sHOPPING_HISTORY40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sHOPPING_HISTORY40"):
                opp_val = getattr(value, "sHOPPING_HISTORY40", None)
                setattr(value, "sHOPPING_HISTORY40", self)

    @property
    def sTORE30(self):
        return self.__sTORE30
    @sTORE30.setter
    def sTORE30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SHOPPING_HISTORY__sTORE30", None)
        self.__sTORE30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sHOPPING_HISTORY31"):
                opp_val = getattr(old_value, "sHOPPING_HISTORY31", None)
                if opp_val == self:
                    setattr(old_value, "sHOPPING_HISTORY31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sHOPPING_HISTORY31"):
                opp_val = getattr(value, "sHOPPING_HISTORY31", None)
                setattr(value, "sHOPPING_HISTORY31", self)

    @property
    def mESSENGER49(self):
        return self.__mESSENGER49
    @mESSENGER49.setter
    def mESSENGER49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SHOPPING_HISTORY__mESSENGER49", None)
        self.__mESSENGER49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sHOPPING_HISTORY48"):
                opp_val = getattr(old_value, "sHOPPING_HISTORY48", None)
                if opp_val == self:
                    setattr(old_value, "sHOPPING_HISTORY48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sHOPPING_HISTORY48"):
                opp_val = getattr(value, "sHOPPING_HISTORY48", None)
                setattr(value, "sHOPPING_HISTORY48", self)

    @property
    def uSUARIO14(self):
        return self.__uSUARIO14
    @uSUARIO14.setter
    def uSUARIO14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SHOPPING_HISTORY__uSUARIO14", None)
        self.__uSUARIO14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sHOPPING_CART15"):
                opp_val = getattr(old_value, "sHOPPING_CART15", None)
                if opp_val == self:
                    setattr(old_value, "sHOPPING_CART15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sHOPPING_CART15"):
                opp_val = getattr(value, "sHOPPING_CART15", None)
                setattr(value, "sHOPPING_CART15", self)

    @property
    def sTATUS_SHOPPING_HISTORY25(self):
        return self.__sTATUS_SHOPPING_HISTORY25
    @sTATUS_SHOPPING_HISTORY25.setter
    def sTATUS_SHOPPING_HISTORY25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SHOPPING_HISTORY__sTATUS_SHOPPING_HISTORY25", None)
        self.__sTATUS_SHOPPING_HISTORY25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sHOPPING_HISTORY24"):
                opp_val = getattr(old_value, "sHOPPING_HISTORY24", None)
                if opp_val == self:
                    setattr(old_value, "sHOPPING_HISTORY24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sHOPPING_HISTORY24"):
                opp_val = getattr(value, "sHOPPING_HISTORY24", None)
                setattr(value, "sHOPPING_HISTORY24", self)

    @property
    def pRODUCT16(self):
        return self.__pRODUCT16
    @pRODUCT16.setter
    def pRODUCT16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SHOPPING_HISTORY__pRODUCT16", None)
        self.__pRODUCT16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sHOPPING_CART17"):
                opp_val = getattr(old_value, "sHOPPING_CART17", None)
                if opp_val == self:
                    setattr(old_value, "sHOPPING_CART17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sHOPPING_CART17"):
                opp_val = getattr(value, "sHOPPING_CART17", None)
                setattr(value, "sHOPPING_CART17", self)



class QUESTIONS:

    def __init__(self, _id: str, createdAt: str, statusId: str, userId: str, productId: str, question: str, answer: str, score: int, pRODUCT10: "PRODUCT" = None, uSUARIO12: "USER" = None):
        self._id = _id
        self.createdAt = createdAt
        self.statusId = statusId
        self.userId = userId
        self.productId = productId
        self.question = question
        self.answer = answer
        self.score = score
        self.pRODUCT10 = pRODUCT10
        self.uSUARIO12 = uSUARIO12
        
        pass
    @property
    def question(self):
        return self.__question
    @question.setter
    def question(self, question: str):
        self.__question = question

    @property
    def createdAt(self):
        return self.__createdAt
    @createdAt.setter
    def createdAt(self, createdAt: str):
        self.__createdAt = createdAt

    @property
    def userId(self):
        return self.__userId
    @userId.setter
    def userId(self, userId: str):
        self.__userId = userId

    @property
    def _id(self):
        return self.___id
    @_id.setter
    def _id(self, _id: str):
        self.___id = _id

    @property
    def productId(self):
        return self.__productId
    @productId.setter
    def productId(self, productId: str):
        self.__productId = productId

    @property
    def score(self):
        return self.__score
    @score.setter
    def score(self, score: int):
        self.__score = score

    @property
    def statusId(self):
        return self.__statusId
    @statusId.setter
    def statusId(self, statusId: str):
        self.__statusId = statusId

    @property
    def answer(self):
        return self.__answer
    @answer.setter
    def answer(self, answer: str):
        self.__answer = answer

    @property
    def uSUARIO12(self):
        return self.__uSUARIO12
    @uSUARIO12.setter
    def uSUARIO12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QUESTIONS__uSUARIO12", None)
        self.__uSUARIO12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cOMMENTS13"):
                opp_val = getattr(old_value, "cOMMENTS13", None)
                if opp_val == self:
                    setattr(old_value, "cOMMENTS13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cOMMENTS13"):
                opp_val = getattr(value, "cOMMENTS13", None)
                setattr(value, "cOMMENTS13", self)

    @property
    def pRODUCT10(self):
        return self.__pRODUCT10
    @pRODUCT10.setter
    def pRODUCT10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QUESTIONS__pRODUCT10", None)
        self.__pRODUCT10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cOMMENTS11"):
                opp_val = getattr(old_value, "cOMMENTS11", None)
                if opp_val == self:
                    setattr(old_value, "cOMMENTS11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cOMMENTS11"):
                opp_val = getattr(value, "cOMMENTS11", None)
                setattr(value, "cOMMENTS11", self)



class WHISES:

    def __init__(self, createdAt: str, statusId: str, userId: str, productId: str, _id: str, pRODUCTO6: "PRODUCT" = None, uSUARIO8: "USER" = None):
        self.createdAt = createdAt
        self.statusId = statusId
        self.userId = userId
        self.productId = productId
        self._id = _id
        self.pRODUCTO6 = pRODUCTO6
        self.uSUARIO8 = uSUARIO8
        
        pass
    @property
    def userId(self):
        return self.__userId
    @userId.setter
    def userId(self, userId: str):
        self.__userId = userId

    @property
    def _id(self):
        return self.___id
    @_id.setter
    def _id(self, _id: str):
        self.___id = _id

    @property
    def createdAt(self):
        return self.__createdAt
    @createdAt.setter
    def createdAt(self, createdAt: str):
        self.__createdAt = createdAt

    @property
    def statusId(self):
        return self.__statusId
    @statusId.setter
    def statusId(self, statusId: str):
        self.__statusId = statusId

    @property
    def productId(self):
        return self.__productId
    @productId.setter
    def productId(self, productId: str):
        self.__productId = productId

    @property
    def uSUARIO8(self):
        return self.__uSUARIO8
    @uSUARIO8.setter
    def uSUARIO8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WHISES__uSUARIO8", None)
        self.__uSUARIO8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fAVORITES9"):
                opp_val = getattr(old_value, "fAVORITES9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fAVORITES9"):
                opp_val = getattr(value, "fAVORITES9", None)
                if opp_val is None:
                    setattr(value, "fAVORITES9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pRODUCTO6(self):
        return self.__pRODUCTO6
    @pRODUCTO6.setter
    def pRODUCTO6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WHISES__pRODUCTO6", None)
        self.__pRODUCTO6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fAVORITES7"):
                opp_val = getattr(old_value, "fAVORITES7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fAVORITES7"):
                opp_val = getattr(value, "fAVORITES7", None)
                if opp_val is None:
                    setattr(value, "fAVORITES7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class CATEGORIAS:

    def __init__(self, _id: str, createdAt: str, name: str, pRODUCTO4: set["PRODUCT"] = None):
        self._id = _id
        self.createdAt = createdAt
        self.name = name
        self.pRODUCTO4 = pRODUCTO4 if pRODUCTO4 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def _id(self):
        return self.___id
    @_id.setter
    def _id(self, _id: str):
        self.___id = _id

    @property
    def createdAt(self):
        return self.__createdAt
    @createdAt.setter
    def createdAt(self, createdAt: str):
        self.__createdAt = createdAt

    @property
    def pRODUCTO4(self):
        return self.__pRODUCTO4
    @pRODUCTO4.setter
    def pRODUCTO4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CATEGORIAS__pRODUCTO4", None)
        self.__pRODUCTO4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cATEGORIAS5"):
                    opp_val = getattr(item, "cATEGORIAS5", None)
                    
                    if opp_val == self:
                        setattr(item, "cATEGORIAS5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cATEGORIAS5"):
                    opp_val = getattr(item, "cATEGORIAS5", None)
                    
                    setattr(item, "cATEGORIAS5", self)
                    



class PRODUCT:

    def __init__(self, _id: str, createdAt: str, statusId: str, storeId: str, name: str, price: int, sold: int, isNew: bool, description: str, quantity: int, photos: str, relatedProducts: str, dimensions: str, attribute: str, color: str, model: str, ShippingMethods: str, uSUARIO2: set["USER"] = None, cATEGORIAS5: "CATEGORIAS" = None, fAVORITES7: set["WHISES"] = None, cOMMENTS11: "QUESTIONS" = None, sHOPPING_CART17: "SHOPPING_HISTORY" = None, sTATUS19: "STATUS" = None, sHIPPING23: "SHIPPING_METHODS" = None, sTORE27: set["STORE"] = None):
        self._id = _id
        self.createdAt = createdAt
        self.statusId = statusId
        self.storeId = storeId
        self.name = name
        self.price = price
        self.sold = sold
        self.isNew = isNew
        self.description = description
        self.quantity = quantity
        self.photos = photos
        self.relatedProducts = relatedProducts
        self.dimensions = dimensions
        self.attribute = attribute
        self.color = color
        self.model = model
        self.ShippingMethods = ShippingMethods
        self.uSUARIO2 = uSUARIO2 if uSUARIO2 is not None else set()
        self.cATEGORIAS5 = cATEGORIAS5
        self.fAVORITES7 = fAVORITES7 if fAVORITES7 is not None else set()
        self.cOMMENTS11 = cOMMENTS11
        self.sHOPPING_CART17 = sHOPPING_CART17
        self.sTATUS19 = sTATUS19
        self.sHIPPING23 = sHIPPING23
        self.sTORE27 = sTORE27 if sTORE27 is not None else set()
        
        pass
    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, price: int):
        self.__price = price

    @property
    def sold(self):
        return self.__sold
    @sold.setter
    def sold(self, sold: int):
        self.__sold = sold

    @property
    def createdAt(self):
        return self.__createdAt
    @createdAt.setter
    def createdAt(self, createdAt: str):
        self.__createdAt = createdAt

    @property
    def isNew(self):
        return self.__isNew
    @isNew.setter
    def isNew(self, isNew: bool):
        self.__isNew = isNew

    @property
    def statusId(self):
        return self.__statusId
    @statusId.setter
    def statusId(self, statusId: str):
        self.__statusId = statusId

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dimensions(self):
        return self.__dimensions
    @dimensions.setter
    def dimensions(self, dimensions: str):
        self.__dimensions = dimensions

    @property
    def color(self):
        return self.__color
    @color.setter
    def color(self, color: str):
        self.__color = color

    @property
    def ShippingMethods(self):
        return self.__ShippingMethods
    @ShippingMethods.setter
    def ShippingMethods(self, ShippingMethods: str):
        self.__ShippingMethods = ShippingMethods

    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def _id(self):
        return self.___id
    @_id.setter
    def _id(self, _id: str):
        self.___id = _id

    @property
    def model(self):
        return self.__model
    @model.setter
    def model(self, model: str):
        self.__model = model

    @property
    def quantity(self):
        return self.__quantity
    @quantity.setter
    def quantity(self, quantity: int):
        self.__quantity = quantity

    @property
    def photos(self):
        return self.__photos
    @photos.setter
    def photos(self, photos: str):
        self.__photos = photos

    @property
    def description(self):
        return self.__description
    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def relatedProducts(self):
        return self.__relatedProducts
    @relatedProducts.setter
    def relatedProducts(self, relatedProducts: str):
        self.__relatedProducts = relatedProducts

    @property
    def storeId(self):
        return self.__storeId
    @storeId.setter
    def storeId(self, storeId: str):
        self.__storeId = storeId

    @property
    def uSUARIO2(self):
        return self.__uSUARIO2
    @uSUARIO2.setter
    def uSUARIO2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PRODUCT__uSUARIO2", None)
        self.__uSUARIO2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pRODUCTO3"):
                    opp_val = getattr(item, "pRODUCTO3", None)
                    
                    if opp_val == self:
                        setattr(item, "pRODUCTO3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pRODUCTO3"):
                    opp_val = getattr(item, "pRODUCTO3", None)
                    
                    setattr(item, "pRODUCTO3", self)
                    

    @property
    def cOMMENTS11(self):
        return self.__cOMMENTS11
    @cOMMENTS11.setter
    def cOMMENTS11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PRODUCT__cOMMENTS11", None)
        self.__cOMMENTS11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pRODUCT10"):
                opp_val = getattr(old_value, "pRODUCT10", None)
                if opp_val == self:
                    setattr(old_value, "pRODUCT10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pRODUCT10"):
                opp_val = getattr(value, "pRODUCT10", None)
                setattr(value, "pRODUCT10", self)

    @property
    def sTATUS19(self):
        return self.__sTATUS19
    @sTATUS19.setter
    def sTATUS19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PRODUCT__sTATUS19", None)
        self.__sTATUS19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pRODUCT18"):
                opp_val = getattr(old_value, "pRODUCT18", None)
                if opp_val == self:
                    setattr(old_value, "pRODUCT18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pRODUCT18"):
                opp_val = getattr(value, "pRODUCT18", None)
                setattr(value, "pRODUCT18", self)

    @property
    def sTORE27(self):
        return self.__sTORE27
    @sTORE27.setter
    def sTORE27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PRODUCT__sTORE27", None)
        self.__sTORE27 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pRODUCT26"):
                    opp_val = getattr(item, "pRODUCT26", None)
                    
                    if opp_val == self:
                        setattr(item, "pRODUCT26", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pRODUCT26"):
                    opp_val = getattr(item, "pRODUCT26", None)
                    
                    setattr(item, "pRODUCT26", self)
                    

    @property
    def sHOPPING_CART17(self):
        return self.__sHOPPING_CART17
    @sHOPPING_CART17.setter
    def sHOPPING_CART17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PRODUCT__sHOPPING_CART17", None)
        self.__sHOPPING_CART17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pRODUCT16"):
                opp_val = getattr(old_value, "pRODUCT16", None)
                if opp_val == self:
                    setattr(old_value, "pRODUCT16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pRODUCT16"):
                opp_val = getattr(value, "pRODUCT16", None)
                setattr(value, "pRODUCT16", self)

    @property
    def cATEGORIAS5(self):
        return self.__cATEGORIAS5
    @cATEGORIAS5.setter
    def cATEGORIAS5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PRODUCT__cATEGORIAS5", None)
        self.__cATEGORIAS5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pRODUCTO4"):
                opp_val = getattr(old_value, "pRODUCTO4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pRODUCTO4"):
                opp_val = getattr(value, "pRODUCTO4", None)
                if opp_val is None:
                    setattr(value, "pRODUCTO4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fAVORITES7(self):
        return self.__fAVORITES7
    @fAVORITES7.setter
    def fAVORITES7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PRODUCT__fAVORITES7", None)
        self.__fAVORITES7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pRODUCTO6"):
                    opp_val = getattr(item, "pRODUCTO6", None)
                    
                    if opp_val == self:
                        setattr(item, "pRODUCTO6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pRODUCTO6"):
                    opp_val = getattr(item, "pRODUCTO6", None)
                    
                    setattr(item, "pRODUCTO6", self)
                    

    @property
    def sHIPPING23(self):
        return self.__sHIPPING23
    @sHIPPING23.setter
    def sHIPPING23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PRODUCT__sHIPPING23", None)
        self.__sHIPPING23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pRODUCT22"):
                opp_val = getattr(old_value, "pRODUCT22", None)
                if opp_val == self:
                    setattr(old_value, "pRODUCT22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pRODUCT22"):
                opp_val = getattr(value, "pRODUCT22", None)
                setattr(value, "pRODUCT22", self)



class ROLES:

    def __init__(self, _id: str, createdAt: str, name: str, usuario0: set["USER"] = None):
        self._id = _id
        self.createdAt = createdAt
        self.name = name
        self.usuario0 = usuario0 if usuario0 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def _id(self):
        return self.___id
    @_id.setter
    def _id(self, _id: str):
        self.___id = _id

    @property
    def createdAt(self):
        return self.__createdAt
    @createdAt.setter
    def createdAt(self, createdAt: str):
        self.__createdAt = createdAt

    @property
    def usuario0(self):
        return self.__usuario0
    @usuario0.setter
    def usuario0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ROLES__usuario0", None)
        self.__usuario0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "roles1"):
                    opp_val = getattr(item, "roles1", None)
                    
                    if opp_val == self:
                        setattr(item, "roles1", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "roles1"):
                    opp_val = getattr(item, "roles1", None)
                    
                    setattr(item, "roles1", self)
                    



class USER:

    def __init__(self, _id: str, createdAt: str, updateAt: str, status: str, email: str, password: str, address: str, telephone: str, name: str, surname: str, verified: bool, lastAccess: str, roles1: "ROLES" = None, pRODUCTO3: "PRODUCT" = None, fAVORITES9: set["WHISES"] = None, cOMMENTS13: "QUESTIONS" = None, sHOPPING_CART15: "SHOPPING_HISTORY" = None, fEEDBACKS51: "FEEDBACK" = None, sTORE29: "STORE" = None, fAVORITES35: "FAVORITES" = None, nOTIFICATION39: "NOTIFICATION" = None, sOCIAL_NETWORKS45: "SOCIAL_NETWORKS" = None, fRIEND_LIST47: "FOLLOW" = None):
        self._id = _id
        self.createdAt = createdAt
        self.updateAt = updateAt
        self.status = status
        self.email = email
        self.password = password
        self.address = address
        self.telephone = telephone
        self.name = name
        self.surname = surname
        self.verified = verified
        self.lastAccess = lastAccess
        self.roles1 = roles1
        self.pRODUCTO3 = pRODUCTO3
        self.fAVORITES9 = fAVORITES9 if fAVORITES9 is not None else set()
        self.cOMMENTS13 = cOMMENTS13
        self.sHOPPING_CART15 = sHOPPING_CART15
        self.fEEDBACKS51 = fEEDBACKS51
        self.sTORE29 = sTORE29
        self.fAVORITES35 = fAVORITES35
        self.nOTIFICATION39 = nOTIFICATION39
        self.sOCIAL_NETWORKS45 = sOCIAL_NETWORKS45
        self.fRIEND_LIST47 = fRIEND_LIST47
        
        pass
    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self, status: str):
        self.__status = status

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def updateAt(self):
        return self.__updateAt
    @updateAt.setter
    def updateAt(self, updateAt: str):
        self.__updateAt = updateAt

    @property
    def telephone(self):
        return self.__telephone
    @telephone.setter
    def telephone(self, telephone: str):
        self.__telephone = telephone

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def createdAt(self):
        return self.__createdAt
    @createdAt.setter
    def createdAt(self, createdAt: str):
        self.__createdAt = createdAt

    @property
    def lastAccess(self):
        return self.__lastAccess
    @lastAccess.setter
    def lastAccess(self, lastAccess: str):
        self.__lastAccess = lastAccess

    @property
    def _id(self):
        return self.___id
    @_id.setter
    def _id(self, _id: str):
        self.___id = _id

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def surname(self):
        return self.__surname
    @surname.setter
    def surname(self, surname: str):
        self.__surname = surname

    @property
    def verified(self):
        return self.__verified
    @verified.setter
    def verified(self, verified: bool):
        self.__verified = verified

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def cOMMENTS13(self):
        return self.__cOMMENTS13
    @cOMMENTS13.setter
    def cOMMENTS13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_USER__cOMMENTS13", None)
        self.__cOMMENTS13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uSUARIO12"):
                opp_val = getattr(old_value, "uSUARIO12", None)
                if opp_val == self:
                    setattr(old_value, "uSUARIO12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uSUARIO12"):
                opp_val = getattr(value, "uSUARIO12", None)
                setattr(value, "uSUARIO12", self)

    @property
    def roles1(self):
        return self.__roles1
    @roles1.setter
    def roles1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_USER__roles1", None)
        self.__roles1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "usuario0"):
                opp_val = getattr(old_value, "usuario0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "usuario0"):
                opp_val = getattr(value, "usuario0", None)
                if opp_val is None:
                    setattr(value, "usuario0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pRODUCTO3(self):
        return self.__pRODUCTO3
    @pRODUCTO3.setter
    def pRODUCTO3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_USER__pRODUCTO3", None)
        self.__pRODUCTO3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uSUARIO2"):
                opp_val = getattr(old_value, "uSUARIO2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uSUARIO2"):
                opp_val = getattr(value, "uSUARIO2", None)
                if opp_val is None:
                    setattr(value, "uSUARIO2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sHOPPING_CART15(self):
        return self.__sHOPPING_CART15
    @sHOPPING_CART15.setter
    def sHOPPING_CART15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_USER__sHOPPING_CART15", None)
        self.__sHOPPING_CART15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uSUARIO14"):
                opp_val = getattr(old_value, "uSUARIO14", None)
                if opp_val == self:
                    setattr(old_value, "uSUARIO14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uSUARIO14"):
                opp_val = getattr(value, "uSUARIO14", None)
                setattr(value, "uSUARIO14", self)

    @property
    def fEEDBACKS51(self):
        return self.__fEEDBACKS51
    @fEEDBACKS51.setter
    def fEEDBACKS51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_USER__fEEDBACKS51", None)
        self.__fEEDBACKS51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uSER50"):
                opp_val = getattr(old_value, "uSER50", None)
                if opp_val == self:
                    setattr(old_value, "uSER50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uSER50"):
                opp_val = getattr(value, "uSER50", None)
                setattr(value, "uSER50", self)

    @property
    def nOTIFICATION39(self):
        return self.__nOTIFICATION39
    @nOTIFICATION39.setter
    def nOTIFICATION39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_USER__nOTIFICATION39", None)
        self.__nOTIFICATION39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uSER38"):
                opp_val = getattr(old_value, "uSER38", None)
                if opp_val == self:
                    setattr(old_value, "uSER38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uSER38"):
                opp_val = getattr(value, "uSER38", None)
                setattr(value, "uSER38", self)

    @property
    def fRIEND_LIST47(self):
        return self.__fRIEND_LIST47
    @fRIEND_LIST47.setter
    def fRIEND_LIST47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_USER__fRIEND_LIST47", None)
        self.__fRIEND_LIST47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uSER46"):
                opp_val = getattr(old_value, "uSER46", None)
                if opp_val == self:
                    setattr(old_value, "uSER46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uSER46"):
                opp_val = getattr(value, "uSER46", None)
                setattr(value, "uSER46", self)

    @property
    def sTORE29(self):
        return self.__sTORE29
    @sTORE29.setter
    def sTORE29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_USER__sTORE29", None)
        self.__sTORE29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uSER28"):
                opp_val = getattr(old_value, "uSER28", None)
                if opp_val == self:
                    setattr(old_value, "uSER28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uSER28"):
                opp_val = getattr(value, "uSER28", None)
                setattr(value, "uSER28", self)

    @property
    def sOCIAL_NETWORKS45(self):
        return self.__sOCIAL_NETWORKS45
    @sOCIAL_NETWORKS45.setter
    def sOCIAL_NETWORKS45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_USER__sOCIAL_NETWORKS45", None)
        self.__sOCIAL_NETWORKS45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uSER44"):
                opp_val = getattr(old_value, "uSER44", None)
                if opp_val == self:
                    setattr(old_value, "uSER44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uSER44"):
                opp_val = getattr(value, "uSER44", None)
                setattr(value, "uSER44", self)

    @property
    def fAVORITES9(self):
        return self.__fAVORITES9
    @fAVORITES9.setter
    def fAVORITES9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_USER__fAVORITES9", None)
        self.__fAVORITES9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uSUARIO8"):
                    opp_val = getattr(item, "uSUARIO8", None)
                    
                    if opp_val == self:
                        setattr(item, "uSUARIO8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uSUARIO8"):
                    opp_val = getattr(item, "uSUARIO8", None)
                    
                    setattr(item, "uSUARIO8", self)
                    

    @property
    def fAVORITES35(self):
        return self.__fAVORITES35
    @fAVORITES35.setter
    def fAVORITES35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_USER__fAVORITES35", None)
        self.__fAVORITES35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uSER34"):
                opp_val = getattr(old_value, "uSER34", None)
                if opp_val == self:
                    setattr(old_value, "uSER34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uSER34"):
                opp_val = getattr(value, "uSER34", None)
                setattr(value, "uSER34", self)

