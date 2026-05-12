from __future__ import annotations
from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Int(Enum):
    pass

############################################
# Definition of Classes
############################################










class UserProfileRequestCreate:

    pass


class UserAccount:

    pass


class CrudRepository_Interface:

    pass


class Integer_Interface:

    pass


class profile_UserProfile:

    def __init__(self, id: str, name: str, uid: str, credits: str, attribute: str):
        self.id = id
        self.name = name
        self.uid = uid
        self.credits = credits
        self.attribute = attribute
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def credits(self):
        return self.__credits
    @credits.setter
    def credits(self, credits: str):
        self.__credits = credits

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def uid(self):
        return self.__uid
    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid



class profile_UserProfileController:

    def __init__(self, URL: str, userAccountRepository: account_UserAccountRepository_Interface, attribute: str, userProfileRepository: profile_UserProfileRepository_Interface):
        self.URL = URL
        self.userAccountRepository = userAccountRepository
        self.attribute = attribute
        self.userProfileRepository = userProfileRepository
        
        pass
    @property
    def userProfileRepository(self):
        return self.__userProfileRepository
    @userProfileRepository.setter
    def userProfileRepository(self, userProfileRepository: profile_UserProfileRepository_Interface):
        self.__userProfileRepository = userProfileRepository

    @property
    def userAccountRepository(self):
        return self.__userAccountRepository
    @userAccountRepository.setter
    def userAccountRepository(self, userAccountRepository: account_UserAccountRepository_Interface):
        self.__userAccountRepository = userAccountRepository

    @property
    def URL(self):
        return self.__URL
    @URL.setter
    def URL(self, URL: str):
        self.__URL = URL

    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute



class profile_UserProfileRepository_Interface:

    pass


class account_UserAccountPasswordChange:

    def __init__(self, email: str, oldPassword: str, newPassword: str):
        self.email = email
        self.oldPassword = oldPassword
        self.newPassword = newPassword
        
        pass
    @property
    def oldPassword(self):
        return self.__oldPassword
    @oldPassword.setter
    def oldPassword(self, oldPassword: str):
        self.__oldPassword = oldPassword

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def newPassword(self):
        return self.__newPassword
    @newPassword.setter
    def newPassword(self, newPassword: str):
        self.__newPassword = newPassword



class account_UserAccountPublicInfo:

    def __init__(self, id: str, alias: str, gamesPlayed: str, gamesWon: str, userAccountController4: "account_UserAccountController" = None):
        self.id = id
        self.alias = alias
        self.gamesPlayed = gamesPlayed
        self.gamesWon = gamesWon
        self.userAccountController4 = userAccountController4
        
        pass
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def alias(self):
        return self.__alias
    @alias.setter
    def alias(self, alias: str):
        self.__alias = alias

    @property
    def gamesPlayed(self):
        return self.__gamesPlayed
    @gamesPlayed.setter
    def gamesPlayed(self, gamesPlayed: str):
        self.__gamesPlayed = gamesPlayed

    @property
    def gamesWon(self):
        return self.__gamesWon
    @gamesWon.setter
    def gamesWon(self, gamesWon: str):
        self.__gamesWon = gamesWon

    @property
    def userAccountController4(self):
        return self.__userAccountController4
    @userAccountController4.setter
    def userAccountController4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_account_UserAccountPublicInfo__userAccountController4", None)
        self.__userAccountController4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "userAccountPublicInfo5"):
                opp_val = getattr(old_value, "userAccountPublicInfo5", None)
                if opp_val == self:
                    setattr(old_value, "userAccountPublicInfo5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "userAccountPublicInfo5"):
                opp_val = getattr(value, "userAccountPublicInfo5", None)
                setattr(value, "userAccountPublicInfo5", self)



class account_UserAccountRepository_Interface:

    pass


class account_UserAccountController:

    def __init__(self, URL: str, userAccountRepository: account_UserAccountRepository_Interface, userAccountRepository23: "account_UserAccountRepository_Interface" = None, userAccountPublicInfo5: "account_UserAccountPublicInfo" = None, userAccount7: "account_UserAccount" = None):
        self.URL = URL
        self.userAccountRepository = userAccountRepository
        self.userAccountRepository23 = userAccountRepository23
        self.userAccountPublicInfo5 = userAccountPublicInfo5
        self.userAccount7 = userAccount7
        
        pass
    @property
    def URL(self):
        return self.__URL
    @URL.setter
    def URL(self, URL: str):
        self.__URL = URL

    @property
    def userAccountRepository(self):
        return self.__userAccountRepository
    @userAccountRepository.setter
    def userAccountRepository(self, userAccountRepository: account_UserAccountRepository_Interface):
        self.__userAccountRepository = userAccountRepository

    @property
    def userAccount7(self):
        return self.__userAccount7
    @userAccount7.setter
    def userAccount7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_account_UserAccountController__userAccount7", None)
        self.__userAccount7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "userAccountController6"):
                opp_val = getattr(old_value, "userAccountController6", None)
                if opp_val == self:
                    setattr(old_value, "userAccountController6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "userAccountController6"):
                opp_val = getattr(value, "userAccountController6", None)
                setattr(value, "userAccountController6", self)

    @property
    def userAccountRepository23(self):
        return self.__userAccountRepository23
    @userAccountRepository23.setter
    def userAccountRepository23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_account_UserAccountController__userAccountRepository23", None)
        self.__userAccountRepository23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "userAccountController2"):
                opp_val = getattr(old_value, "userAccountController2", None)
                if opp_val == self:
                    setattr(old_value, "userAccountController2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "userAccountController2"):
                opp_val = getattr(value, "userAccountController2", None)
                setattr(value, "userAccountController2", self)

    @property
    def userAccountPublicInfo5(self):
        return self.__userAccountPublicInfo5
    @userAccountPublicInfo5.setter
    def userAccountPublicInfo5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_account_UserAccountController__userAccountPublicInfo5", None)
        self.__userAccountPublicInfo5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "userAccountController4"):
                opp_val = getattr(old_value, "userAccountController4", None)
                if opp_val == self:
                    setattr(old_value, "userAccountController4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "userAccountController4"):
                opp_val = getattr(value, "userAccountController4", None)
                setattr(value, "userAccountController4", self)



class account_UserAccount:

    def __init__(self, id: str, email: str, password: str, createdAt: str, gamesPlayed: str, gamesWon: str, alias: str, userAccountController6: "account_UserAccountController" = None):
        self.id = id
        self.email = email
        self.password = password
        self.createdAt = createdAt
        self.gamesPlayed = gamesPlayed
        self.gamesWon = gamesWon
        self.alias = alias
        self.userAccountController6 = userAccountController6
        
        pass
    @property
    def gamesPlayed(self):
        return self.__gamesPlayed
    @gamesPlayed.setter
    def gamesPlayed(self, gamesPlayed: str):
        self.__gamesPlayed = gamesPlayed

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def gamesWon(self):
        return self.__gamesWon
    @gamesWon.setter
    def gamesWon(self, gamesWon: str):
        self.__gamesWon = gamesWon

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def createdAt(self):
        return self.__createdAt
    @createdAt.setter
    def createdAt(self, createdAt: str):
        self.__createdAt = createdAt

    @property
    def alias(self):
        return self.__alias
    @alias.setter
    def alias(self, alias: str):
        self.__alias = alias

    @property
    def userAccountController6(self):
        return self.__userAccountController6
    @userAccountController6.setter
    def userAccountController6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_account_UserAccount__userAccountController6", None)
        self.__userAccountController6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "userAccount7"):
                opp_val = getattr(old_value, "userAccount7", None)
                if opp_val == self:
                    setattr(old_value, "userAccount7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "userAccount7"):
                opp_val = getattr(value, "userAccount7", None)
                setattr(value, "userAccount7", self)



class game_GameController:

    pass


class game_Pack:

    pass


class game_Ace:

    pass


class game_Card:

    def __init__(self, name: str, suit: str, deck0: "game_Deck" = None):
        self.name = name
        self.suit = suit
        self.deck0 = deck0
        
        pass
    @property
    def suit(self):
        return self.__suit
    @suit.setter
    def suit(self, suit: str):
        self.__suit = suit

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def deck0(self):
        return self.__deck0
    @deck0.setter
    def deck0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_game_Card__deck0", None)
        self.__deck0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "card1"):
                opp_val = getattr(old_value, "card1", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "card1"):
                opp_val = getattr(value, "card1", None)
                if opp_val is None:
                    setattr(value, "card1", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class game_Deck(ABC):

    def __init__(self, cards: str, card1: set["game_Card"] = None):
        self.cards = cards
        self.card1 = card1 if card1 is not None else set()
        
        pass
    @property
    def cards(self):
        return self.__cards
    @cards.setter
    def cards(self, cards: str):
        self.__cards = cards

    @property
    def card1(self):
        return self.__card1
    @card1.setter
    def card1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_game_Deck__card1", None)
        self.__card1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "deck0"):
                    opp_val = getattr(item, "deck0", None)
                    
                    if opp_val == self:
                        setattr(item, "deck0", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "deck0"):
                    opp_val = getattr(item, "deck0", None)
                    
                    setattr(item, "deck0", self)
                    

