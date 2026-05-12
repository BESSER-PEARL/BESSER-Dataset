from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class game_Choix:

    def __init__(self, name: str, game_Choix93: "game_Interaction" = None, game_Choix96: "game_Interaction" = None, game_Choix98: "game_Description" = None, game_Choix101: "game_Condition" = None, game_Choix: "game_Action" = None, game_Choix87: "game_Interaction" = None, game_Choix104: set["game_Action"] = None):
        self.name = name
        self.game_Choix93 = game_Choix93
        self.game_Choix96 = game_Choix96
        self.game_Choix98 = game_Choix98
        self.game_Choix101 = game_Choix101
        self.game_Choix = game_Choix
        self.game_Choix87 = game_Choix87
        self.game_Choix104 = game_Choix104 if game_Choix104 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def game_Choix87(self):
        return self.__game_Choix87

    @game_Choix87.setter
    def game_Choix87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_game_Choix__game_Choix87", None)
        self.__game_Choix87 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "game_Interaction86"):
                opp_val = getattr(old_value, "game_Interaction86", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "game_Interaction86"):
                opp_val = getattr(value, "game_Interaction86", None)
                if opp_val is None:
                    setattr(value, "game_Interaction86", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def game_Choix96(self):
        return self.__game_Choix96

    @game_Choix96.setter
    def game_Choix96(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_game_Choix__game_Choix96", None)
        self.__game_Choix96 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "game_Interaction95"):
                opp_val = getattr(old_value, "game_Interaction95", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "game_Interaction95"):
                opp_val = getattr(value, "game_Interaction95", None)
                if opp_val is None:
                    setattr(value, "game_Interaction95", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def game_Choix101(self):
        return self.__game_Choix101

    @game_Choix101.setter
    def game_Choix101(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_game_Choix__game_Choix101", None)
        self.__game_Choix101 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "game_Condition102"):
                opp_val = getattr(old_value, "game_Condition102", None)
                if opp_val == self:
                    setattr(old_value, "game_Condition102", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "game_Condition102"):
                opp_val = getattr(value, "game_Condition102", None)
                setattr(value, "game_Condition102", self)

    @property
    def game_Choix93(self):
        return self.__game_Choix93

    @game_Choix93.setter
    def game_Choix93(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_game_Choix__game_Choix93", None)
        self.__game_Choix93 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "game_Interaction92"):
                opp_val = getattr(old_value, "game_Interaction92", None)
                if opp_val == self:
                    setattr(old_value, "game_Interaction92", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "game_Interaction92"):
                opp_val = getattr(value, "game_Interaction92", None)
                setattr(value, "game_Interaction92", self)

    @property
    def game_Choix98(self):
        return self.__game_Choix98

    @game_Choix98.setter
    def game_Choix98(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_game_Choix__game_Choix98", None)
        self.__game_Choix98 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "game_Description99"):
                opp_val = getattr(old_value, "game_Description99", None)
                if opp_val == self:
                    setattr(old_value, "game_Description99", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "game_Description99"):
                opp_val = getattr(value, "game_Description99", None)
                setattr(value, "game_Description99", self)

    @property
    def game_Choix(self):
        return self.__game_Choix

    @game_Choix.setter
    def game_Choix(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_game_Choix__game_Choix", None)
        self.__game_Choix = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "game_Action81"):
                opp_val = getattr(old_value, "game_Action81", None)
                if opp_val == self:
                    setattr(old_value, "game_Action81", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "game_Action81"):
                opp_val = getattr(value, "game_Action81", None)
                setattr(value, "game_Action81", self)

    @property
    def game_Choix104(self):
        return self.__game_Choix104

    @game_Choix104.setter
    def game_Choix104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_game_Choix__game_Choix104", None)
        self.__game_Choix104 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "game_Action105"):
                    opp_val = getattr(item, "game_Action105", None)
                    
                    if opp_val == self:
                        setattr(item, "game_Action105", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "game_Action105"):
                    opp_val = getattr(item, "game_Action105", None)
                    
                    setattr(item, "game_Action105", self)
                    

class game_Action:

    pass
class game_Conjonction:

    pass
class game_Recompense:

    pass
class game_Texte:

    def __init__(self, contenu: str, game_Texte: "game_Description" = None, game_Texte58: "game_Condition" = None):
        self.contenu = contenu
        self.game_Texte = game_Texte
        self.game_Texte58 = game_Texte58
        
        pass
    @property
    def contenu(self):
        return self.__contenu

    @contenu.setter
    def contenu(self, contenu: str):
        self.__contenu = contenu


    @property
    def game_Texte(self):
        return self.__game_Texte

    @game_Texte.setter
    def game_Texte(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_game_Texte__game_Texte", None)
        self.__game_Texte = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "game_Description56"):
                opp_val = getattr(old_value, "game_Description56", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "game_Description56"):
                opp_val = getattr(value, "game_Description56", None)
                if opp_val is None:
                    setattr(value, "game_Description56", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def game_Texte58(self):
        return self.__game_Texte58

    @game_Texte58.setter
    def game_Texte58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_game_Texte__game_Texte58", None)
        self.__game_Texte58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "game_Condition59"):
                opp_val = getattr(old_value, "game_Condition59", None)
                if opp_val == self:
                    setattr(old_value, "game_Condition59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "game_Condition59"):
                opp_val = getattr(value, "game_Condition59", None)
                setattr(value, "game_Condition59", self)

class game_Litteral:

    def __init__(self, operateur: str, quantite: int, game_Litteral: "game_Conjonction" = None, game_Litteral50: "game_Objet" = None, game_Litteral53: "game_Connaissance" = None):
        self.operateur = operateur
        self.quantite = quantite
        self.game_Litteral = game_Litteral
        self.game_Litteral50 = game_Litteral50
        self.game_Litteral53 = game_Litteral53
        
        pass
    @property
    def quantite(self):
        return self.__quantite

    @quantite.setter
    def quantite(self, quantite: int):
        self.__quantite = quantite


    @property
    def operateur(self):
        return self.__operateur

    @operateur.setter
    def operateur(self, operateur: str):
        self.__operateur = operateur


    @property
    def game_Litteral(self):
        return self.__game_Litteral

    @game_Litteral.setter
    def game_Litteral(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_game_Litteral__game_Litteral", None)
        self.__game_Litteral = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "game_Conjonction48"):
                opp_val = getattr(old_value, "game_Conjonction48", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "game_Conjonction48"):
                opp_val = getattr(value, "game_Conjonction48", None)
                if opp_val is None:
                    setattr(value, "game_Conjonction48", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def game_Litteral53(self):
        return self.__game_Litteral53

    @game_Litteral53.setter
    def game_Litteral53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_game_Litteral__game_Litteral53", None)
        self.__game_Litteral53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "game_Connaissance54"):
                opp_val = getattr(old_value, "game_Connaissance54", None)
                if opp_val == self:
                    setattr(old_value, "game_Connaissance54", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "game_Connaissance54"):
                opp_val = getattr(value, "game_Connaissance54", None)
                setattr(value, "game_Connaissance54", self)

    @property
    def game_Litteral50(self):
        return self.__game_Litteral50

    @game_Litteral50.setter
    def game_Litteral50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_game_Litteral__game_Litteral50", None)
        self.__game_Litteral50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "game_Objet51"):
                opp_val = getattr(old_value, "game_Objet51", None)
                if opp_val == self:
                    setattr(old_value, "game_Objet51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "game_Objet51"):
                opp_val = getattr(value, "game_Objet51", None)
                setattr(value, "game_Objet51", self)

class game_Description:

    pass
class EntiteLieu:

    pass
class game_ConnaissanceLieu(EntiteLieu):

    pass
class game_Condition:

    pass
class game_Personne:

    def __init__(self, name: str, game_Personne20: "game_Interaction" = None, game_Personne: "game_EntiteLieu" = None):
        self.name = name
        self.game_Personne20 = game_Personne20
        self.game_Personne = game_Personne
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def game_Personne20(self):
        return self.__game_Personne20

    @game_Personne20.setter
    def game_Personne20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_game_Personne__game_Personne20", None)
        self.__game_Personne20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "game_Interaction"):
                opp_val = getattr(old_value, "game_Interaction", None)
                if opp_val == self:
                    setattr(old_value, "game_Interaction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "game_Interaction"):
                opp_val = getattr(value, "game_Interaction", None)
                setattr(value, "game_Interaction", self)

    @property
    def game_Personne(self):
        return self.__game_Personne

    @game_Personne.setter
    def game_Personne(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_game_Personne__game_Personne", None)
        self.__game_Personne = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "game_EntiteLieu"):
                opp_val = getattr(old_value, "game_EntiteLieu", None)
                if opp_val == self:
                    setattr(old_value, "game_EntiteLieu", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "game_EntiteLieu"):
                opp_val = getattr(value, "game_EntiteLieu", None)
                setattr(value, "game_EntiteLieu", self)

class game_EntiteLieu:

    pass
class game_GameElement:

    def __init__(self, name: str, game_GameElement: "game_Game" = None, game_GameElement13: "game_Description" = None):
        self.name = name
        self.game_GameElement = game_GameElement
        self.game_GameElement13 = game_GameElement13
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def game_GameElement(self):
        return self.__game_GameElement

    @game_GameElement.setter
    def game_GameElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_game_GameElement__game_GameElement", None)
        self.__game_GameElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "game_Game7"):
                opp_val = getattr(old_value, "game_Game7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "game_Game7"):
                opp_val = getattr(value, "game_Game7", None)
                if opp_val is None:
                    setattr(value, "game_Game7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def game_GameElement13(self):
        return self.__game_GameElement13

    @game_GameElement13.setter
    def game_GameElement13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_game_GameElement__game_GameElement13", None)
        self.__game_GameElement13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "game_Description"):
                opp_val = getattr(old_value, "game_Description", None)
                if opp_val == self:
                    setattr(old_value, "game_Description", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "game_Description"):
                opp_val = getattr(value, "game_Description", None)
                setattr(value, "game_Description", self)

class game_Explorateur:

    def __init__(self, name: str, tailleInventaire: int, game_Explorateur15: set["game_Connaissance"] = None, game_Explorateur18: set["game_PackObjets"] = None, game_Explorateur: "game_Game" = None):
        self.name = name
        self.tailleInventaire = tailleInventaire
        self.game_Explorateur15 = game_Explorateur15 if game_Explorateur15 is not None else set()
        self.game_Explorateur18 = game_Explorateur18 if game_Explorateur18 is not None else set()
        self.game_Explorateur = game_Explorateur
        
        pass
    @property
    def tailleInventaire(self):
        return self.__tailleInventaire

    @tailleInventaire.setter
    def tailleInventaire(self, tailleInventaire: int):
        self.__tailleInventaire = tailleInventaire


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def game_Explorateur(self):
        return self.__game_Explorateur

    @game_Explorateur.setter
    def game_Explorateur(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_game_Explorateur__game_Explorateur", None)
        self.__game_Explorateur = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "game_Game"):
                opp_val = getattr(old_value, "game_Game", None)
                if opp_val == self:
                    setattr(old_value, "game_Game", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "game_Game"):
                opp_val = getattr(value, "game_Game", None)
                setattr(value, "game_Game", self)

    @property
    def game_Explorateur18(self):
        return self.__game_Explorateur18

    @game_Explorateur18.setter
    def game_Explorateur18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_game_Explorateur__game_Explorateur18", None)
        self.__game_Explorateur18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "game_PackObjets"):
                    opp_val = getattr(item, "game_PackObjets", None)
                    
                    if opp_val == self:
                        setattr(item, "game_PackObjets", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "game_PackObjets"):
                    opp_val = getattr(item, "game_PackObjets", None)
                    
                    setattr(item, "game_PackObjets", self)
                    

    @property
    def game_Explorateur15(self):
        return self.__game_Explorateur15

    @game_Explorateur15.setter
    def game_Explorateur15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_game_Explorateur__game_Explorateur15", None)
        self.__game_Explorateur15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "game_Connaissance16"):
                    opp_val = getattr(item, "game_Connaissance16", None)
                    
                    if opp_val == self:
                        setattr(item, "game_Connaissance16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "game_Connaissance16"):
                    opp_val = getattr(item, "game_Connaissance16", None)
                    
                    setattr(item, "game_Connaissance16", self)
                    

class game_Game:

    def __init__(self, name: str, game_Game: "game_Explorateur" = None, game_Game2: "game_Lieu" = None, game_Game4: set["game_Lieu"] = None, game_Game7: set["game_GameElement"] = None):
        self.name = name
        self.game_Game = game_Game
        self.game_Game2 = game_Game2
        self.game_Game4 = game_Game4 if game_Game4 is not None else set()
        self.game_Game7 = game_Game7 if game_Game7 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def game_Game2(self):
        return self.__game_Game2

    @game_Game2.setter
    def game_Game2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_game_Game__game_Game2", None)
        self.__game_Game2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "game_Lieu"):
                opp_val = getattr(old_value, "game_Lieu", None)
                if opp_val == self:
                    setattr(old_value, "game_Lieu", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "game_Lieu"):
                opp_val = getattr(value, "game_Lieu", None)
                setattr(value, "game_Lieu", self)

    @property
    def game_Game7(self):
        return self.__game_Game7

    @game_Game7.setter
    def game_Game7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_game_Game__game_Game7", None)
        self.__game_Game7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "game_GameElement"):
                    opp_val = getattr(item, "game_GameElement", None)
                    
                    if opp_val == self:
                        setattr(item, "game_GameElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "game_GameElement"):
                    opp_val = getattr(item, "game_GameElement", None)
                    
                    setattr(item, "game_GameElement", self)
                    

    @property
    def game_Game(self):
        return self.__game_Game

    @game_Game.setter
    def game_Game(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_game_Game__game_Game", None)
        self.__game_Game = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "game_Explorateur"):
                opp_val = getattr(old_value, "game_Explorateur", None)
                if opp_val == self:
                    setattr(old_value, "game_Explorateur", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "game_Explorateur"):
                opp_val = getattr(value, "game_Explorateur", None)
                setattr(value, "game_Explorateur", self)

    @property
    def game_Game4(self):
        return self.__game_Game4

    @game_Game4.setter
    def game_Game4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_game_Game__game_Game4", None)
        self.__game_Game4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "game_Lieu5"):
                    opp_val = getattr(item, "game_Lieu5", None)
                    
                    if opp_val == self:
                        setattr(item, "game_Lieu5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "game_Lieu5"):
                    opp_val = getattr(item, "game_Lieu5", None)
                    
                    setattr(item, "game_Lieu5", self)
                    

class GameElement:

    pass
class game_Chemin(GameElement):

    pass
class game_Connaissance(GameElement):

    pass
class game_Lieu(GameElement):

    pass
class game_Objet(GameElement):

    def __init__(self, taille: int, game_Objet51: "game_Litteral" = None, game_Objet: "game_PackObjets" = None):
        self.taille = taille
        self.game_Objet51 = game_Objet51
        self.game_Objet = game_Objet
        
        pass
    @property
    def taille(self):
        return self.__taille

    @taille.setter
    def taille(self, taille: int):
        self.__taille = taille


    @property
    def game_Objet(self):
        return self.__game_Objet

    @game_Objet.setter
    def game_Objet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_game_Objet__game_Objet", None)
        self.__game_Objet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "game_PackObjets27"):
                opp_val = getattr(old_value, "game_PackObjets27", None)
                if opp_val == self:
                    setattr(old_value, "game_PackObjets27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "game_PackObjets27"):
                opp_val = getattr(value, "game_PackObjets27", None)
                setattr(value, "game_PackObjets27", self)

    @property
    def game_Objet51(self):
        return self.__game_Objet51

    @game_Objet51.setter
    def game_Objet51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_game_Objet__game_Objet51", None)
        self.__game_Objet51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "game_Litteral50"):
                opp_val = getattr(old_value, "game_Litteral50", None)
                if opp_val == self:
                    setattr(old_value, "game_Litteral50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "game_Litteral50"):
                opp_val = getattr(value, "game_Litteral50", None)
                setattr(value, "game_Litteral50", self)

class game_Interaction:

    pass
class game_PackObjets(EntiteLieu):

    def __init__(self, quantite: int, game_PackObjets: "game_Explorateur" = None, game_PackObjets65: "game_Recompense" = None, game_PackObjets79: "game_Action" = None, game_PackObjets27: "game_Objet" = None, game_PackObjets44: "game_Chemin" = None):
        self.quantite = quantite
        self.game_PackObjets = game_PackObjets
        self.game_PackObjets65 = game_PackObjets65
        self.game_PackObjets79 = game_PackObjets79
        self.game_PackObjets27 = game_PackObjets27
        self.game_PackObjets44 = game_PackObjets44
        
        pass
    @property
    def quantite(self):
        return self.__quantite

    @quantite.setter
    def quantite(self, quantite: int):
        self.__quantite = quantite


    @property
    def game_PackObjets(self):
        return self.__game_PackObjets

    @game_PackObjets.setter
    def game_PackObjets(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_game_PackObjets__game_PackObjets", None)
        self.__game_PackObjets = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "game_Explorateur18"):
                opp_val = getattr(old_value, "game_Explorateur18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "game_Explorateur18"):
                opp_val = getattr(value, "game_Explorateur18", None)
                if opp_val is None:
                    setattr(value, "game_Explorateur18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def game_PackObjets65(self):
        return self.__game_PackObjets65

    @game_PackObjets65.setter
    def game_PackObjets65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_game_PackObjets__game_PackObjets65", None)
        self.__game_PackObjets65 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "game_Recompense64"):
                opp_val = getattr(old_value, "game_Recompense64", None)
                if opp_val == self:
                    setattr(old_value, "game_Recompense64", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "game_Recompense64"):
                opp_val = getattr(value, "game_Recompense64", None)
                setattr(value, "game_Recompense64", self)

    @property
    def game_PackObjets79(self):
        return self.__game_PackObjets79

    @game_PackObjets79.setter
    def game_PackObjets79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_game_PackObjets__game_PackObjets79", None)
        self.__game_PackObjets79 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "game_Action78"):
                opp_val = getattr(old_value, "game_Action78", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "game_Action78"):
                opp_val = getattr(value, "game_Action78", None)
                if opp_val is None:
                    setattr(value, "game_Action78", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def game_PackObjets27(self):
        return self.__game_PackObjets27

    @game_PackObjets27.setter
    def game_PackObjets27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_game_PackObjets__game_PackObjets27", None)
        self.__game_PackObjets27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "game_Objet"):
                opp_val = getattr(old_value, "game_Objet", None)
                if opp_val == self:
                    setattr(old_value, "game_Objet", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "game_Objet"):
                opp_val = getattr(value, "game_Objet", None)
                setattr(value, "game_Objet", self)

    @property
    def game_PackObjets44(self):
        return self.__game_PackObjets44

    @game_PackObjets44.setter
    def game_PackObjets44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_game_PackObjets__game_PackObjets44", None)
        self.__game_PackObjets44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "game_Chemin43"):
                opp_val = getattr(old_value, "game_Chemin43", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "game_Chemin43"):
                opp_val = getattr(value, "game_Chemin43", None)
                if opp_val is None:
                    setattr(value, "game_Chemin43", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
