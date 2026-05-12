from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class UseCase_UseCase:

    pass


class Actor_Actor:

    pass


class Repeat_Non_UseCase:

    pass


class Shuflfe_play_UseCase:

    pass


class Stop_UseCase:

    pass


class Pause_UseCase:

    pass


class Favorite_UseCase:

    pass


class Search_UseCase:

    pass


class Create_playlist_UseCase:

    pass


class Play_UseCase:

    pass


class Download_UseCase:

    pass


class User_Actor:

    pass





class TopMostPlayed:

    def __init__(self, mpID: int, sID: int):
        self.mpID = mpID
        self.sID = sID
        
        pass
    @property
    def mpID(self):
        return self.__mpID
    @mpID.setter
    def mpID(self, mpID: int):
        self.__mpID = mpID

    @property
    def sID(self):
        return self.__sID
    @sID.setter
    def sID(self, sID: int):
        self.__sID = sID



class Recently_Played:

    def __init__(self, rpID: int, sID: int):
        self.rpID = rpID
        self.sID = sID
        
        pass
    @property
    def sID(self):
        return self.__sID
    @sID.setter
    def sID(self, sID: int):
        self.__sID = sID

    @property
    def rpID(self):
        return self.__rpID
    @rpID.setter
    def rpID(self, rpID: int):
        self.__rpID = rpID



class Downloads:

    def __init__(self, dID: int, sID: int):
        self.dID = dID
        self.sID = sID
        
        pass
    @property
    def dID(self):
        return self.__dID
    @dID.setter
    def dID(self, dID: int):
        self.__dID = dID

    @property
    def sID(self):
        return self.__sID
    @sID.setter
    def sID(self, sID: int):
        self.__sID = sID



class Favourites:

    def __init__(self, fID: int, sID: int):
        self.fID = fID
        self.sID = sID
        
        pass
    @property
    def fID(self):
        return self.__fID
    @fID.setter
    def fID(self, fID: int):
        self.__fID = fID

    @property
    def sID(self):
        return self.__sID
    @sID.setter
    def sID(self, sID: int):
        self.__sID = sID



class Playlist_Song:

    def __init__(self, pID: int, sID: int, song1: "Song" = None, playlist3: "Playlist" = None):
        self.pID = pID
        self.sID = sID
        self.song1 = song1
        self.playlist3 = playlist3
        
        pass
    @property
    def sID(self):
        return self.__sID
    @sID.setter
    def sID(self, sID: int):
        self.__sID = sID

    @property
    def pID(self):
        return self.__pID
    @pID.setter
    def pID(self, pID: int):
        self.__pID = pID

    @property
    def playlist3(self):
        return self.__playlist3
    @playlist3.setter
    def playlist3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Playlist_Song__playlist3", None)
        self.__playlist3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "playlist_Song2"):
                opp_val = getattr(old_value, "playlist_Song2", None)
                if opp_val == self:
                    setattr(old_value, "playlist_Song2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "playlist_Song2"):
                opp_val = getattr(value, "playlist_Song2", None)
                setattr(value, "playlist_Song2", self)

    @property
    def song1(self):
        return self.__song1
    @song1.setter
    def song1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Playlist_Song__song1", None)
        self.__song1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "playlist_Song0"):
                opp_val = getattr(old_value, "playlist_Song0", None)
                if opp_val == self:
                    setattr(old_value, "playlist_Song0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "playlist_Song0"):
                opp_val = getattr(value, "playlist_Song0", None)
                setattr(value, "playlist_Song0", self)



class Playlist:

    def __init__(self, pID: int, pName: str, pDate: str, playlist_Song2: "Playlist_Song" = None):
        self.pID = pID
        self.pName = pName
        self.pDate = pDate
        self.playlist_Song2 = playlist_Song2
        
        pass
    @property
    def pID(self):
        return self.__pID
    @pID.setter
    def pID(self, pID: int):
        self.__pID = pID

    @property
    def pName(self):
        return self.__pName
    @pName.setter
    def pName(self, pName: str):
        self.__pName = pName

    @property
    def pDate(self):
        return self.__pDate
    @pDate.setter
    def pDate(self, pDate: str):
        self.__pDate = pDate

    @property
    def playlist_Song2(self):
        return self.__playlist_Song2
    @playlist_Song2.setter
    def playlist_Song2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Playlist__playlist_Song2", None)
        self.__playlist_Song2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "playlist3"):
                opp_val = getattr(old_value, "playlist3", None)
                if opp_val == self:
                    setattr(old_value, "playlist3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "playlist3"):
                opp_val = getattr(value, "playlist3", None)
                setattr(value, "playlist3", self)



class Song:

    def __init__(self, sID: int, sName: str, sCateg: str, sArtist: str, sDate: str, sIMG_url: str, playlist_Song0: "Playlist_Song" = None):
        self.sID = sID
        self.sName = sName
        self.sCateg = sCateg
        self.sArtist = sArtist
        self.sDate = sDate
        self.sIMG_url = sIMG_url
        self.playlist_Song0 = playlist_Song0
        
        pass
    @property
    def sName(self):
        return self.__sName
    @sName.setter
    def sName(self, sName: str):
        self.__sName = sName

    @property
    def sIMG_url(self):
        return self.__sIMG_url
    @sIMG_url.setter
    def sIMG_url(self, sIMG_url: str):
        self.__sIMG_url = sIMG_url

    @property
    def sCateg(self):
        return self.__sCateg
    @sCateg.setter
    def sCateg(self, sCateg: str):
        self.__sCateg = sCateg

    @property
    def sArtist(self):
        return self.__sArtist
    @sArtist.setter
    def sArtist(self, sArtist: str):
        self.__sArtist = sArtist

    @property
    def sID(self):
        return self.__sID
    @sID.setter
    def sID(self, sID: int):
        self.__sID = sID

    @property
    def sDate(self):
        return self.__sDate
    @sDate.setter
    def sDate(self, sDate: str):
        self.__sDate = sDate

    @property
    def playlist_Song0(self):
        return self.__playlist_Song0
    @playlist_Song0.setter
    def playlist_Song0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Song__playlist_Song0", None)
        self.__playlist_Song0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "song1"):
                opp_val = getattr(old_value, "song1", None)
                if opp_val == self:
                    setattr(old_value, "song1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "song1"):
                opp_val = getattr(value, "song1", None)
                setattr(value, "song1", self)

