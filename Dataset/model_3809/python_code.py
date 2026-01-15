from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class example_Player:

    def __init__(self, compression1: str, example_Player: "example_Codec" = None):
        self.compression1 = compression1
        self.example_Player = example_Player
        
    @property
    def compression1(self) -> str:
        return self.__compression1

    @compression1.setter
    def compression1(self, compression1: str):
        self.__compression1 = compression1

    @property
    def example_Player(self):
        return self.__example_Player

    @example_Player.setter
    def example_Player(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_example_Player__example_Player", None)
        self.__example_Player = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "example_Codec"):
                opp_val = getattr(old_value, "example_Codec", None)
                if opp_val == self:
                    setattr(old_value, "example_Codec", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "example_Codec"):
                opp_val = getattr(value, "example_Codec", None)
                setattr(value, "example_Codec", self)

class example_Codec:

    pass