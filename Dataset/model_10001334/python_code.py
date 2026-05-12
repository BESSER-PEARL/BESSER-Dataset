from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Kommentare:

    def __init__(self, text: str, Kommentare_Post_018: "Beitrag" = None):
        self.text = text
        self.Kommentare_Post_018 = Kommentare_Post_018
        
        pass
    @property
    def text(self):
        return self.__text
    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def Kommentare_Post_018(self):
        return self.__Kommentare_Post_018
    @Kommentare_Post_018.setter
    def Kommentare_Post_018(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Kommentare__Kommentare_Post_018", None)
        self.__Kommentare_Post_018 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Kommentare_Post_119"):
                opp_val = getattr(old_value, "Kommentare_Post_119", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Kommentare_Post_119"):
                opp_val = getattr(value, "Kommentare_Post_119", None)
                if opp_val is None:
                    setattr(value, "Kommentare_Post_119", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Anmelden:

    def __init__(self, email: str, passwort: str, user3: "Benutzer" = None):
        self.email = email
        self.passwort = passwort
        self.user3 = user3
        
        pass
    @property
    def passwort(self):
        return self.__passwort
    @passwort.setter
    def passwort(self, passwort: str):
        self.__passwort = passwort

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def user3(self):
        return self.__user3
    @user3.setter
    def user3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Anmelden__user3", None)
        self.__user3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "login2"):
                opp_val = getattr(old_value, "login2", None)
                if opp_val == self:
                    setattr(old_value, "login2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "login2"):
                opp_val = getattr(value, "login2", None)
                setattr(value, "login2", self)



class Registrieren:

    def __init__(self, vorname: str, nachname: str, email: str, passwort: str, geburtsdatum: str, geschlecht: str, user7: "Benutzer" = None):
        self.vorname = vorname
        self.nachname = nachname
        self.email = email
        self.passwort = passwort
        self.geburtsdatum = geburtsdatum
        self.geschlecht = geschlecht
        self.user7 = user7
        
        pass
    @property
    def geschlecht(self):
        return self.__geschlecht
    @geschlecht.setter
    def geschlecht(self, geschlecht: str):
        self.__geschlecht = geschlecht

    @property
    def vorname(self):
        return self.__vorname
    @vorname.setter
    def vorname(self, vorname: str):
        self.__vorname = vorname

    @property
    def nachname(self):
        return self.__nachname
    @nachname.setter
    def nachname(self, nachname: str):
        self.__nachname = nachname

    @property
    def passwort(self):
        return self.__passwort
    @passwort.setter
    def passwort(self, passwort: str):
        self.__passwort = passwort

    @property
    def geburtsdatum(self):
        return self.__geburtsdatum
    @geburtsdatum.setter
    def geburtsdatum(self, geburtsdatum: str):
        self.__geburtsdatum = geburtsdatum

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def user7(self):
        return self.__user7
    @user7.setter
    def user7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Registrieren__user7", None)
        self.__user7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "registeration6"):
                opp_val = getattr(old_value, "registeration6", None)
                if opp_val == self:
                    setattr(old_value, "registeration6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "registeration6"):
                opp_val = getattr(value, "registeration6", None)
                setattr(value, "registeration6", self)



class Hashtag:

    def __init__(self, name: str, numOfRepeat: int, user13: "Benutzer" = None):
        self.name = name
        self.numOfRepeat = numOfRepeat
        self.user13 = user13
        
        pass
    @property
    def numOfRepeat(self):
        return self.__numOfRepeat
    @numOfRepeat.setter
    def numOfRepeat(self, numOfRepeat: int):
        self.__numOfRepeat = numOfRepeat

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def user13(self):
        return self.__user13
    @user13.setter
    def user13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Hashtag__user13", None)
        self.__user13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hashtag12"):
                opp_val = getattr(old_value, "hashtag12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hashtag12"):
                opp_val = getattr(value, "hashtag12", None)
                if opp_val is None:
                    setattr(value, "hashtag12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Freund:

    pass


class _unnamed:

    def __init__(self, maxChars: str, user9: "Benutzer" = None):
        self.maxChars = maxChars
        self.user9 = user9
        
        pass
    @property
    def maxChars(self):
        return self.__maxChars
    @maxChars.setter
    def maxChars(self, maxChars: str):
        self.__maxChars = maxChars

    @property
    def user9(self):
        return self.__user9
    @user9.setter
    def user9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"__unnamed__user9", None)
        self.__user9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "message8"):
                opp_val = getattr(old_value, "message8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "message8"):
                opp_val = getattr(value, "message8", None)
                if opp_val is None:
                    setattr(value, "message8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Privat:

    pass


class Ver_ffentlich:

    pass


class Group:

    def __init__(self, name: str, user5: "Benutzer" = None, Group_Beitrag_020: set["Beitrag"] = None):
        self.name = name
        self.user5 = user5
        self.Group_Beitrag_020 = Group_Beitrag_020 if Group_Beitrag_020 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def user5(self):
        return self.__user5
    @user5.setter
    def user5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Group__user5", None)
        self.__user5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "group4"):
                opp_val = getattr(old_value, "group4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "group4"):
                opp_val = getattr(value, "group4", None)
                if opp_val is None:
                    setattr(value, "group4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Group_Beitrag_020(self):
        return self.__Group_Beitrag_020
    @Group_Beitrag_020.setter
    def Group_Beitrag_020(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Group__Group_Beitrag_020", None)
        self.__Group_Beitrag_020 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Group_Beitrag_121"):
                    opp_val = getattr(item, "Group_Beitrag_121", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Group_Beitrag_121"):
                    opp_val = getattr(item, "Group_Beitrag_121", None)
                    
                    if opp_val is None:
                        setattr(item, "Group_Beitrag_121", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Beitrag:

    def __init__(self, privatph_re: str, text: str, foto: str, video: str, Audio: str, user1: "Benutzer" = None, Post_public_014: "Ver_ffentlich" = None, Post_secret_016: "Privat" = None, Kommentare_Post_119: set["Kommentare"] = None, Group_Beitrag_121: set["Group"] = None):
        self.privatph_re = privatph_re
        self.text = text
        self.foto = foto
        self.video = video
        self.Audio = Audio
        self.user1 = user1
        self.Post_public_014 = Post_public_014
        self.Post_secret_016 = Post_secret_016
        self.Kommentare_Post_119 = Kommentare_Post_119 if Kommentare_Post_119 is not None else set()
        self.Group_Beitrag_121 = Group_Beitrag_121 if Group_Beitrag_121 is not None else set()
        
        pass
    @property
    def video(self):
        return self.__video
    @video.setter
    def video(self, video: str):
        self.__video = video

    @property
    def foto(self):
        return self.__foto
    @foto.setter
    def foto(self, foto: str):
        self.__foto = foto

    @property
    def text(self):
        return self.__text
    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def Audio(self):
        return self.__Audio
    @Audio.setter
    def Audio(self, Audio: str):
        self.__Audio = Audio

    @property
    def privatph_re(self):
        return self.__privatph_re
    @privatph_re.setter
    def privatph_re(self, privatph_re: str):
        self.__privatph_re = privatph_re

    @property
    def Group_Beitrag_121(self):
        return self.__Group_Beitrag_121
    @Group_Beitrag_121.setter
    def Group_Beitrag_121(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Beitrag__Group_Beitrag_121", None)
        self.__Group_Beitrag_121 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Group_Beitrag_020"):
                    opp_val = getattr(item, "Group_Beitrag_020", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Group_Beitrag_020"):
                    opp_val = getattr(item, "Group_Beitrag_020", None)
                    
                    if opp_val is None:
                        setattr(item, "Group_Beitrag_020", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def user1(self):
        return self.__user1
    @user1.setter
    def user1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Beitrag__user1", None)
        self.__user1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "post0"):
                opp_val = getattr(old_value, "post0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "post0"):
                opp_val = getattr(value, "post0", None)
                if opp_val is None:
                    setattr(value, "post0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Kommentare_Post_119(self):
        return self.__Kommentare_Post_119
    @Kommentare_Post_119.setter
    def Kommentare_Post_119(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Beitrag__Kommentare_Post_119", None)
        self.__Kommentare_Post_119 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Kommentare_Post_018"):
                    opp_val = getattr(item, "Kommentare_Post_018", None)
                    
                    if opp_val == self:
                        setattr(item, "Kommentare_Post_018", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Kommentare_Post_018"):
                    opp_val = getattr(item, "Kommentare_Post_018", None)
                    
                    setattr(item, "Kommentare_Post_018", self)
                    

    @property
    def Post_public_014(self):
        return self.__Post_public_014
    @Post_public_014.setter
    def Post_public_014(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Beitrag__Post_public_014", None)
        self.__Post_public_014 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Post_public_115"):
                opp_val = getattr(old_value, "Post_public_115", None)
                if opp_val == self:
                    setattr(old_value, "Post_public_115", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Post_public_115"):
                opp_val = getattr(value, "Post_public_115", None)
                setattr(value, "Post_public_115", self)

    @property
    def Post_secret_016(self):
        return self.__Post_secret_016
    @Post_secret_016.setter
    def Post_secret_016(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Beitrag__Post_secret_016", None)
        self.__Post_secret_016 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Post_secret_117"):
                opp_val = getattr(old_value, "Post_secret_117", None)
                if opp_val == self:
                    setattr(old_value, "Post_secret_117", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Post_secret_117"):
                opp_val = getattr(value, "Post_secret_117", None)
                setattr(value, "Post_secret_117", self)



class Benutzer:

    def __init__(self, Vorname: str, Nachname: str, Info: str, profilbild: str, post0: set["Beitrag"] = None, login2: "Anmelden" = None, group4: set["Group"] = None, registeration6: "Registrieren" = None, message8: set["_unnamed"] = None, friends10: set["Freund"] = None, hashtag12: set["Hashtag"] = None):
        self.Vorname = Vorname
        self.Nachname = Nachname
        self.Info = Info
        self.profilbild = profilbild
        self.post0 = post0 if post0 is not None else set()
        self.login2 = login2
        self.group4 = group4 if group4 is not None else set()
        self.registeration6 = registeration6
        self.message8 = message8 if message8 is not None else set()
        self.friends10 = friends10 if friends10 is not None else set()
        self.hashtag12 = hashtag12 if hashtag12 is not None else set()
        
        pass
    @property
    def Vorname(self):
        return self.__Vorname
    @Vorname.setter
    def Vorname(self, Vorname: str):
        self.__Vorname = Vorname

    @property
    def profilbild(self):
        return self.__profilbild
    @profilbild.setter
    def profilbild(self, profilbild: str):
        self.__profilbild = profilbild

    @property
    def Info(self):
        return self.__Info
    @Info.setter
    def Info(self, Info: str):
        self.__Info = Info

    @property
    def Nachname(self):
        return self.__Nachname
    @Nachname.setter
    def Nachname(self, Nachname: str):
        self.__Nachname = Nachname

    @property
    def friends10(self):
        return self.__friends10
    @friends10.setter
    def friends10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Benutzer__friends10", None)
        self.__friends10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "user11"):
                    opp_val = getattr(item, "user11", None)
                    
                    if opp_val == self:
                        setattr(item, "user11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "user11"):
                    opp_val = getattr(item, "user11", None)
                    
                    setattr(item, "user11", self)
                    

    @property
    def registeration6(self):
        return self.__registeration6
    @registeration6.setter
    def registeration6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Benutzer__registeration6", None)
        self.__registeration6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "user7"):
                opp_val = getattr(old_value, "user7", None)
                if opp_val == self:
                    setattr(old_value, "user7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "user7"):
                opp_val = getattr(value, "user7", None)
                setattr(value, "user7", self)

    @property
    def message8(self):
        return self.__message8
    @message8.setter
    def message8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Benutzer__message8", None)
        self.__message8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "user9"):
                    opp_val = getattr(item, "user9", None)
                    
                    if opp_val == self:
                        setattr(item, "user9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "user9"):
                    opp_val = getattr(item, "user9", None)
                    
                    setattr(item, "user9", self)
                    

    @property
    def post0(self):
        return self.__post0
    @post0.setter
    def post0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Benutzer__post0", None)
        self.__post0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "user1"):
                    opp_val = getattr(item, "user1", None)
                    
                    if opp_val == self:
                        setattr(item, "user1", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "user1"):
                    opp_val = getattr(item, "user1", None)
                    
                    setattr(item, "user1", self)
                    

    @property
    def login2(self):
        return self.__login2
    @login2.setter
    def login2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Benutzer__login2", None)
        self.__login2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "user3"):
                opp_val = getattr(old_value, "user3", None)
                if opp_val == self:
                    setattr(old_value, "user3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "user3"):
                opp_val = getattr(value, "user3", None)
                setattr(value, "user3", self)

    @property
    def hashtag12(self):
        return self.__hashtag12
    @hashtag12.setter
    def hashtag12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Benutzer__hashtag12", None)
        self.__hashtag12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "user13"):
                    opp_val = getattr(item, "user13", None)
                    
                    if opp_val == self:
                        setattr(item, "user13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "user13"):
                    opp_val = getattr(item, "user13", None)
                    
                    setattr(item, "user13", self)
                    

    @property
    def group4(self):
        return self.__group4
    @group4.setter
    def group4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Benutzer__group4", None)
        self.__group4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "user5"):
                    opp_val = getattr(item, "user5", None)
                    
                    if opp_val == self:
                        setattr(item, "user5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "user5"):
                    opp_val = getattr(item, "user5", None)
                    
                    setattr(item, "user5", self)
                    

