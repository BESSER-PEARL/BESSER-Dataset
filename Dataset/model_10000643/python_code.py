from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class Player_Actor:

    pass





class Play_Again_external:

    pass


class Announce_Winner_external:

    pass


class Next_Turn_external:

    pass


class Score_Roll_external:

    pass


class Roll_Dice_external:

    pass


class Computer_Turn_external:

    pass


class Game_Start_external:

    pass


class Roll_First_external:

    pass


class Get_Instructions_external:

    pass


class Get_Player_Name_external:

    pass


class Display:

    pass


class Yahtzee_Players1:

    def __init__(self, compScore: str, playerScore: str, display51: "Yahtzee_Display1" = None):
        self.compScore = compScore
        self.playerScore = playerScore
        self.display51 = display51
        
        pass
    @property
    def compScore(self):
        return self.__compScore
    @compScore.setter
    def compScore(self, compScore: str):
        self.__compScore = compScore

    @property
    def playerScore(self):
        return self.__playerScore
    @playerScore.setter
    def playerScore(self, playerScore: str):
        self.__playerScore = playerScore

    @property
    def display51(self):
        return self.__display51
    @display51.setter
    def display51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Yahtzee_Players1__display51", None)
        self.__display51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "players50"):
                opp_val = getattr(old_value, "players50", None)
                if opp_val == self:
                    setattr(old_value, "players50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "players50"):
                opp_val = getattr(value, "players50", None)
                setattr(value, "players50", self)



class Yahtzee_Scoring1:

    def __init__(self, Temp: str, display55: "Yahtzee_Display1" = None, turn56: "Yahtzee_Turn1" = None):
        self.Temp = Temp
        self.display55 = display55
        self.turn56 = turn56
        
        pass
    @property
    def Temp(self):
        return self.__Temp
    @Temp.setter
    def Temp(self, Temp: str):
        self.__Temp = Temp

    @property
    def display55(self):
        return self.__display55
    @display55.setter
    def display55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Yahtzee_Scoring1__display55", None)
        self.__display55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scoring54"):
                opp_val = getattr(old_value, "scoring54", None)
                if opp_val == self:
                    setattr(old_value, "scoring54", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scoring54"):
                opp_val = getattr(value, "scoring54", None)
                setattr(value, "scoring54", self)

    @property
    def turn56(self):
        return self.__turn56
    @turn56.setter
    def turn56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Yahtzee_Scoring1__turn56", None)
        self.__turn56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scoring57"):
                opp_val = getattr(old_value, "scoring57", None)
                if opp_val == self:
                    setattr(old_value, "scoring57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scoring57"):
                opp_val = getattr(value, "scoring57", None)
                setattr(value, "scoring57", self)



class Yahtzee_Turn1:

    def __init__(self, Dice: str, scoring57: "Yahtzee_Scoring1" = None, display53: "Yahtzee_Display1" = None):
        self.Dice = Dice
        self.scoring57 = scoring57
        self.display53 = display53
        
        pass
    @property
    def Dice(self):
        return self.__Dice
    @Dice.setter
    def Dice(self, Dice: str):
        self.__Dice = Dice

    @property
    def display53(self):
        return self.__display53
    @display53.setter
    def display53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Yahtzee_Turn1__display53", None)
        self.__display53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "turn52"):
                opp_val = getattr(old_value, "turn52", None)
                if opp_val == self:
                    setattr(old_value, "turn52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "turn52"):
                opp_val = getattr(value, "turn52", None)
                setattr(value, "turn52", self)

    @property
    def scoring57(self):
        return self.__scoring57
    @scoring57.setter
    def scoring57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Yahtzee_Turn1__scoring57", None)
        self.__scoring57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "turn56"):
                opp_val = getattr(old_value, "turn56", None)
                if opp_val == self:
                    setattr(old_value, "turn56", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "turn56"):
                opp_val = getattr(value, "turn56", None)
                setattr(value, "turn56", self)



class Yahtzee_Display1:

    def __init__(self, Player: Yahtzee_Players, Computer: Yahtzee_Players, Jpanel: Yahtzee_Display, JFrame: Yahtzee_Display, Jlabel: Yahtzee_Display, JRadioButton: Yahtzee_Display, JButton: Yahtzee_Display, JTextField: Yahtzee_Display, JScrollPanel: Yahtzee_Display1, JImageIcon: Yahtzee_Display, Temp: int, Temp1: int, scoring54: "Yahtzee_Scoring1" = None, players50: "Yahtzee_Players1" = None, turn52: "Yahtzee_Turn1" = None):
        self.Player = Player
        self.Computer = Computer
        self.Jpanel = Jpanel
        self.JFrame = JFrame
        self.Jlabel = Jlabel
        self.JRadioButton = JRadioButton
        self.JButton = JButton
        self.JTextField = JTextField
        self.JScrollPanel = JScrollPanel
        self.JImageIcon = JImageIcon
        self.Temp = Temp
        self.Temp1 = Temp1
        self.scoring54 = scoring54
        self.players50 = players50
        self.turn52 = turn52
        
        pass
    @property
    def JTextField(self):
        return self.__JTextField
    @JTextField.setter
    def JTextField(self, JTextField: Yahtzee_Display):
        self.__JTextField = JTextField

    @property
    def Jlabel(self):
        return self.__Jlabel
    @Jlabel.setter
    def Jlabel(self, Jlabel: Yahtzee_Display):
        self.__Jlabel = Jlabel

    @property
    def JScrollPanel(self):
        return self.__JScrollPanel
    @JScrollPanel.setter
    def JScrollPanel(self, JScrollPanel: Yahtzee_Display1):
        self.__JScrollPanel = JScrollPanel

    @property
    def JImageIcon(self):
        return self.__JImageIcon
    @JImageIcon.setter
    def JImageIcon(self, JImageIcon: Yahtzee_Display):
        self.__JImageIcon = JImageIcon

    @property
    def Temp1(self):
        return self.__Temp1
    @Temp1.setter
    def Temp1(self, Temp1: int):
        self.__Temp1 = Temp1

    @property
    def Temp(self):
        return self.__Temp
    @Temp.setter
    def Temp(self, Temp: int):
        self.__Temp = Temp

    @property
    def JButton(self):
        return self.__JButton
    @JButton.setter
    def JButton(self, JButton: Yahtzee_Display):
        self.__JButton = JButton

    @property
    def Player(self):
        return self.__Player
    @Player.setter
    def Player(self, Player: Yahtzee_Players):
        self.__Player = Player

    @property
    def Computer(self):
        return self.__Computer
    @Computer.setter
    def Computer(self, Computer: Yahtzee_Players):
        self.__Computer = Computer

    @property
    def JFrame(self):
        return self.__JFrame
    @JFrame.setter
    def JFrame(self, JFrame: Yahtzee_Display):
        self.__JFrame = JFrame

    @property
    def JRadioButton(self):
        return self.__JRadioButton
    @JRadioButton.setter
    def JRadioButton(self, JRadioButton: Yahtzee_Display):
        self.__JRadioButton = JRadioButton

    @property
    def Jpanel(self):
        return self.__Jpanel
    @Jpanel.setter
    def Jpanel(self, Jpanel: Yahtzee_Display):
        self.__Jpanel = Jpanel

    @property
    def players50(self):
        return self.__players50
    @players50.setter
    def players50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Yahtzee_Display1__players50", None)
        self.__players50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "display51"):
                opp_val = getattr(old_value, "display51", None)
                if opp_val == self:
                    setattr(old_value, "display51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "display51"):
                opp_val = getattr(value, "display51", None)
                setattr(value, "display51", self)

    @property
    def scoring54(self):
        return self.__scoring54
    @scoring54.setter
    def scoring54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Yahtzee_Display1__scoring54", None)
        self.__scoring54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "display55"):
                opp_val = getattr(old_value, "display55", None)
                if opp_val == self:
                    setattr(old_value, "display55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "display55"):
                opp_val = getattr(value, "display55", None)
                setattr(value, "display55", self)

    @property
    def turn52(self):
        return self.__turn52
    @turn52.setter
    def turn52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Yahtzee_Display1__turn52", None)
        self.__turn52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "display53"):
                opp_val = getattr(old_value, "display53", None)
                if opp_val == self:
                    setattr(old_value, "display53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "display53"):
                opp_val = getattr(value, "display53", None)
                setattr(value, "display53", self)



class Yahtzee_Component:

    pass


class Players:

    pass


class Turn:

    pass


class Scoring:

    pass


class Class1:

    pass


class Class:

    pass


class Yahtzee_Players:

    def __init__(self, Name: str, Score: str, turn5: "Yahtzee_Turn" = None, game7: "Yahtzee_Game" = None, scoring9: "Yahtzee_Scoring" = None):
        self.Name = Name
        self.Score = Score
        self.turn5 = turn5
        self.game7 = game7
        self.scoring9 = scoring9
        
        pass
    @property
    def Score(self):
        return self.__Score
    @Score.setter
    def Score(self, Score: str):
        self.__Score = Score

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def game7(self):
        return self.__game7
    @game7.setter
    def game7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Yahtzee_Players__game7", None)
        self.__game7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "players6"):
                opp_val = getattr(old_value, "players6", None)
                if opp_val == self:
                    setattr(old_value, "players6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "players6"):
                opp_val = getattr(value, "players6", None)
                setattr(value, "players6", self)

    @property
    def turn5(self):
        return self.__turn5
    @turn5.setter
    def turn5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Yahtzee_Players__turn5", None)
        self.__turn5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "players4"):
                opp_val = getattr(old_value, "players4", None)
                if opp_val == self:
                    setattr(old_value, "players4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "players4"):
                opp_val = getattr(value, "players4", None)
                setattr(value, "players4", self)

    @property
    def scoring9(self):
        return self.__scoring9
    @scoring9.setter
    def scoring9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Yahtzee_Players__scoring9", None)
        self.__scoring9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "players8"):
                opp_val = getattr(old_value, "players8", None)
                if opp_val == self:
                    setattr(old_value, "players8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "players8"):
                opp_val = getattr(value, "players8", None)
                setattr(value, "players8", self)



class Yahtzee_Display:

    def __init__(self, PanelScorecard: str, PanelChoices: str, PanelPrimary: str, PanelGameName: str, PanelNames: str):
        self.PanelScorecard = PanelScorecard
        self.PanelChoices = PanelChoices
        self.PanelPrimary = PanelPrimary
        self.PanelGameName = PanelGameName
        self.PanelNames = PanelNames
        
        pass
    @property
    def PanelChoices(self):
        return self.__PanelChoices
    @PanelChoices.setter
    def PanelChoices(self, PanelChoices: str):
        self.__PanelChoices = PanelChoices

    @property
    def PanelNames(self):
        return self.__PanelNames
    @PanelNames.setter
    def PanelNames(self, PanelNames: str):
        self.__PanelNames = PanelNames

    @property
    def PanelPrimary(self):
        return self.__PanelPrimary
    @PanelPrimary.setter
    def PanelPrimary(self, PanelPrimary: str):
        self.__PanelPrimary = PanelPrimary

    @property
    def PanelScorecard(self):
        return self.__PanelScorecard
    @PanelScorecard.setter
    def PanelScorecard(self, PanelScorecard: str):
        self.__PanelScorecard = PanelScorecard

    @property
    def PanelGameName(self):
        return self.__PanelGameName
    @PanelGameName.setter
    def PanelGameName(self, PanelGameName: str):
        self.__PanelGameName = PanelGameName



class Yahtzee_Scoring:

    pass


class Yahtzee_Turn:

    pass


class Yahtzee_Game:

    def __init__(self, Player: Class, CompPlayer: Class1, First: int, Again: bool, turn3: "Yahtzee_Turn" = None, players6: "Yahtzee_Players" = None):
        self.Player = Player
        self.CompPlayer = CompPlayer
        self.First = First
        self.Again = Again
        self.turn3 = turn3
        self.players6 = players6
        
        pass
    @property
    def Again(self):
        return self.__Again
    @Again.setter
    def Again(self, Again: bool):
        self.__Again = Again

    @property
    def First(self):
        return self.__First
    @First.setter
    def First(self, First: int):
        self.__First = First

    @property
    def CompPlayer(self):
        return self.__CompPlayer
    @CompPlayer.setter
    def CompPlayer(self, CompPlayer: Class1):
        self.__CompPlayer = CompPlayer

    @property
    def Player(self):
        return self.__Player
    @Player.setter
    def Player(self, Player: Class):
        self.__Player = Player

    @property
    def players6(self):
        return self.__players6
    @players6.setter
    def players6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Yahtzee_Game__players6", None)
        self.__players6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "game7"):
                opp_val = getattr(old_value, "game7", None)
                if opp_val == self:
                    setattr(old_value, "game7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "game7"):
                opp_val = getattr(value, "game7", None)
                setattr(value, "game7", self)

    @property
    def turn3(self):
        return self.__turn3
    @turn3.setter
    def turn3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Yahtzee_Game__turn3", None)
        self.__turn3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "game2"):
                opp_val = getattr(old_value, "game2", None)
                if opp_val == self:
                    setattr(old_value, "game2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "game2"):
                opp_val = getattr(value, "game2", None)
                setattr(value, "game2", self)

